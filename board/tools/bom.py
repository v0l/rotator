import glob, json, os, re, sys, time, tomllib, urllib.request

os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/..")
BOARDS = 5
KEY = tomllib.load(open(os.path.expanduser("~/.config/agentee/distributors.toml"), "rb"))["mouser"]["api_key"]
CACHE = "tools/.mouser_cache.json"
ELSEWHERE = {
    "V8BR-1AX1-GH": ("Farnell 3588276", 9.31),
}
cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}


def mouser(mpn):
    if mpn in cache:
        return cache[mpn]
    body = json.dumps({"SearchByPartRequest": {"mouserPartNumber": mpn, "partSearchOptions": "Exact"}}).encode()
    req = urllib.request.Request(
        f"https://api.mouser.com/api/v1/search/partnumber?apiKey={KEY}", data=body, headers={"Content-Type": "application/json"}
    )
    for _ in range(4):
        try:
            parts = json.load(urllib.request.urlopen(req, timeout=40))["SearchResults"]["Parts"]
            break
        except Exception:
            time.sleep(8)
    else:
        return None
    hit = next((p for p in parts if p["ManufacturerPartNumber"].upper() == mpn.upper()), parts[0] if parts else None)
    out = None
    if hit:
        breaks = [(int(b["Quantity"]), float(re.sub(r"[^\d.,]", "", b["Price"]).replace(",", "."))) for b in hit.get("PriceBreaks", [])]
        out = {"sku": hit["MouserPartNumber"], "stock": int(hit.get("AvailabilityInStock") or 0), "breaks": breaks}
    cache[mpn] = out
    json.dump(cache, open(CACHE, "w"), indent=1)
    time.sleep(2.5)
    return out


def price(breaks, n):
    p = None
    for q, v in sorted(breaks):
        if n >= q:
            p = v
    return p if p is not None else (sorted(breaks)[0][1] if breaks else None)


lines = {}
for f in sorted(glob.glob("*.sch.toml")):
    for part in tomllib.load(open(f, "rb")).get("parts", []):
        ref, fields = part["ref"], part.get("fields", {})
        if ref.startswith("H") or part.get("dnp") or fields.get("assembly") == "no":
            continue
        key = fields.get("mpn", "")
        line = lines.setdefault(key, {"refs": [], "value": part.get("value", ""), "mfr": fields.get("mfr", "")})
        line["refs"].append(ref)


def refkey(r):
    m = re.match(r"([A-Z]+)(\d+)", r)
    return (m.group(1), int(m.group(2)))


rows, total1, totaln = [], 0.0, 0.0
for mpn, line in sorted(lines.items(), key=lambda kv: refkey(sorted(kv[1]["refs"], key=refkey)[0])):
    refs = sorted(line["refs"], key=refkey)
    qty = len(refs)
    if mpn in ELSEWHERE:
        src, unit = ELSEWHERE[mpn]
        p1 = pn = unit
        stock = ""
    else:
        m = mouser(mpn) if mpn else None
        if not m:
            print("no Mouser hit:", mpn, refs, file=sys.stderr)
            continue
        src, stock = "Mouser " + m["sku"], m["stock"]
        p1, pn = price(m["breaks"], qty), price(m["breaks"], qty * BOARDS)
    total1 += p1 * qty
    totaln += pn * qty * BOARDS
    rows.append((" ".join(refs), qty, line["value"], mpn, line["mfr"], src, stock, p1, pn))

out = ["| Refs | Qty | Value | MPN | Maker | Source | Stock | EUR each (1 board) | EUR each (%d boards) |" % BOARDS, "|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    out.append("| %s | %d | %s | %s | %s | %s | %s | %.3f | %.3f |" % r)
out.append("")
out.append("Parts for 1 board: EUR %.2f. Parts for %d boards: EUR %.2f (EUR %.2f a board)." % (total1, BOARDS, totaln, totaln / BOARDS))
open("tools/bom.md", "w").write("\n".join(out) + "\n")
print("\n".join(out[-1:]))
