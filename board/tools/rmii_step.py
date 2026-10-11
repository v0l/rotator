import os
import numpy as np
def read_snp(path):
    lines=[l for l in open(path) if l.strip() and not l.startswith('!')]
    hdr=[l for l in lines if l.startswith('#')][0].split(); data=" ".join(l for l in lines if not l.startswith('#')).split()
    v=np.array(data,float); n=14; per=1+2*n*n
    v=v.reshape(-1,per); f=v[:,0]; S=(v[:,1::2]+1j*v[:,2::2]).reshape(-1,n,n)
    return f,S
f,S=read_snp(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ctl-rmii.s14p"))
names=["MCU_TXD0","MCU_TXD1","MCU_TXEN","MCU_RXD0","MCU_RXD1","MCU_CRSDV","MCU_REFCLK","PHY_TXD0","PHY_TXD1","PHY_TXEN","PHY_RXD0","PHY_RXD1","PHY_CRSDV","PHY_REFCLK"]
ix={n:i for i,n in enumerate(names)}
lines=[("TXD0","MCU_TXD0","PHY_TXD0","mcu"),("TXD1","MCU_TXD1","PHY_TXD1","mcu"),("TXEN","MCU_TXEN","PHY_TXEN","mcu"),
       ("RXD0","PHY_RXD0","MCU_RXD0","phy"),("RXD1","PHY_RXD1","MCU_RXD1","phy"),("CRSDV","PHY_CRSDV","MCU_CRSDV","phy"),("REF_CLK","PHY_REFCLK","MCU_REFCLK","phy")]
Z0=50.0
def two_port(a,b):
    i,j=ix[a],ix[b]; return S[:,[[i,i],[i,j]],[[i,j],[j,j]]] if False else np.array([[S[:,i,i],S[:,i,j]],[S[:,j,i],S[:,j,j]]]).transpose(2,0,1)
def H(Sp,w,Zs,Cl):
    # source Zs, load capacitor Cl; reflection coefficients
    Zl=1/(1j*w*Cl); gs=(Zs-Z0)/(Zs+Z0); gl=(Zl-Z0)/(Zl+Z0)
    s11,s12,s21,s22=Sp[:,0,0],Sp[:,0,1],Sp[:,1,0],Sp[:,1,1]
    gin=s11+s12*s21*gl/(1-s22*gl)
    # voltage at port1 for source Vs: V1 = Vs * (1+gin)*(1-gs)/(2*(1-gs*gin))
    v1=(1+gin)*(1-gs)/(2*(1-gs*gin))
    # b2/a1 with load: s21/(1-s22*gl); a1 = V1/(1+gin) (in sqrt Z0 units)
    a1=v1/(1+gin); b2=a1*s21/(1-s22*gl); v2=b2*(1+gl)
    return v2
fmax=8e9; df=f[1]-f[0]; N=int(round(fmax/df))
fg=np.arange(N+1)*df
def step(Sp,Zs,Cl,tr):
    Hf=np.zeros(N+1,complex)
    w=2*np.pi*f
    h=H(Sp,w,Zs,Cl)
    Hf[1:len(f)+1]=h
    Hf[0]=1.0
    # above measured band roll off with ideal short line extrapolation: use last phase slope, magnitude of last point
    k=len(f)
    ph=np.unwrap(np.angle(h)); slope=(ph[-1]-ph[-10])/(f[-1]-f[-10])
    fe=fg[k+1:]; Hf[k+1:]=abs(h[-1])*np.exp(1j*(ph[-1]+slope*(fe-f[-1])))*np.exp(-((fe-f[-1])/1e9)**2)
    # Gaussian edge with 10-90 rise tr
    sig=tr/2.563
    G=np.exp(-(2*np.pi*fg*sig)**2/2)
    imp=np.fft.irfft(Hf*G*np.exp(-2j*np.pi*fg*5e-9),n=2*N)
    t=np.arange(2*N)/(2*fmax)
    s=np.cumsum(imp)
    return t,s
for name,a,b,side in lines:
    Sp=two_port(a,b)
    i,j=ix[a],ix[b]
    il=20*np.log10(abs(S[:,j,i])); rl=20*np.log10(abs(S[:,i,i]))
    others=[k for k in range(14) if k not in (i,j)]
    xt=max(20*np.log10(abs(S[np.argmin(abs(f-2e8)),k,i])+1e-12) for k in others)
    cl=2e-12 if side=="mcu" else 5e-12
    res=[]
    trs=[1.4e-9,1.9e-9] if side=="mcu" else [1.0e-9]
    for tr in trs:
        for Zs in (30,50):
            t,s=step(Sp,Zs,cl,tr); fin=np.median(s[int(len(s)*0.3):int(len(s)*0.45)])
            res.append(f"tr {tr*1e9:.1f}ns Zs {Zs}: overshoot {100*(s.max()/fin-1):.1f}%")
    k200=np.argmin(abs(f-2e8))
    print(f"{name:8s} S21@200MHz {il[k200]:.2f} dB  S11@200MHz {rl[k200]:.1f} dB  worst xtalk@200MHz {xt:.1f} dB")
    for r in res: print("    ",r)
print("--- sanity")
ideal=np.zeros((len(f),2,2),complex); ideal[:,0,1]=ideal[:,1,0]=1
for Zs in (30,50):
    for tr in (1.0e-9,1.9e-9):
        t,s=step(ideal,Zs,2e-12,tr); fin=np.median(s[int(len(s)*0.3):int(len(s)*0.45)]); print("ideal",Zs,tr,round(100*(s.max()/fin-1),2), round(fin,3))
# delayed ideal line 250ps
d=np.exp(-2j*np.pi*f*250e-12); line=np.zeros((len(f),2,2),complex); line[:,0,1]=line[:,1,0]=d
for Zs in (30,50):
    for tr in (1.0e-9,1.9e-9):
        t,s=step(line,Zs,2e-12,tr); fin=np.median(s[int(len(s)*0.3):int(len(s)*0.45)]); print("line50",Zs,tr,round(100*(s.max()/fin-1),2))
