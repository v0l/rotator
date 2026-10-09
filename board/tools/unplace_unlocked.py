p='ctl.pcb.toml'
s=open(p).read()
i=s.index('[[footprints]]')
head=s[:i]
rest=s[i:]
tail=''
for key in ('\n[[tracks]]','\n[[vias]]','\n[[zones]]','\n[[fills]]','\n[[stitching]]','\n[[graphics]]'):
    j=rest.find(key)
    if j>=0 and (tail=='' or j<len(rest)-len(tail)):
        pass
blocks=rest.split('[[footprints]]')[1:]
out=head.rstrip()+'\n'
extra=''
for b in blocks:
    body,sep,after=b.partition('\n[[')
    if 'locked = true' in body:
        out+='\n[[footprints]]'+'\n'.join(l for l in body.split('\n') if not l.startswith('label')).rstrip()+'\n'
    if sep:
        extra+='\n[['+after
open(p,'w').write(out+extra)
