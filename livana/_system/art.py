# Gold line-art illustrations of Abu Dhabi (hand-drawn look), all SVG, no photos.
G='#B99A5B'; L='#D9C7A0'
def _svg(w,h,body,vb=None):
    vb=vb or f'0 0 {w} {h}'
    return f'<svg width="{w}" height="{h}" viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="{G}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'

def water(y,w,n=4,gap=14):
    s=''
    for i in range(n):
        yy=y+i*gap; x0=40+i*30; x1=w-40-i*50
        d=f'M{x0} {yy}'
        x=x0
        while x<x1:
            d+=f' q12 -5 24 0 t24 0'; x+=48
        s+=f'<path d="{d}" stroke="{L}" stroke-width="1.6"/>'
    return s

def palm(x,y,h=120,s=1):
    t=f'<path d="M{x} {y} q{6*s} {-h*0.5} {2*s} {-h}" />'
    cx,cy=x+2*s,y-h
    for dx,dy in [(-46,10),(-34,-14),(0,-30),(34,-14),(48,12),(-20,26),(22,26)]:
        t+=f'<path d="M{cx} {cy} q{dx*0.5} {dy*0.6-14} {dx} {dy}" />'
    return t

def etihad(x,y,s=1):
    # five curved towers
    out=''
    for i,(hh,ww) in enumerate([(330,40),(300,38),(280,36),(250,34),(230,34)]):
        bx=x+i*46*s; h=hh*s; w=ww*s
        out+=f'<path d="M{bx} {y} L{bx} {y-h*0.75} Q{bx+2} {y-h} {bx+w*0.55} {y-h} Q{bx+w} {y-h*0.95} {bx+w} {y-h*0.6} L{bx+w} {y}"/>'
        for k in range(1,9):
            yy=y-k*h/10
            if yy>y-h*0.72: out+=f'<path d="M{bx+5} {yy} L{bx+w-5} {yy}" stroke="{L}" stroke-width="1.2"/>'
    return out

def aldarhq(x,y,r=90):
    out=f'<circle cx="{x}" cy="{y-r-20}" r="{r}"/>'
    out+=f'<path d="M{x-14} {y} L{x-10} {y-22} L{x+10} {y-22} L{x+14} {y}"/>'
    for k in range(-3,4):
        out+=f'<path d="M{x+k*r*0.28} {y-20-r+((r*r-(k*r*0.28)**2)**0.5)} L{x+k*r*0.28} {y-20-r-((r*r-(k*r*0.28)**2)**0.5)}" stroke="{L}" stroke-width="1.2"/>'
    return out

def louvre(x,y,w=420):
    h=w*0.16
    out=f'<path d="M{x} {y} Q{x+w/2} {y-h*1.6} {x+w} {y}"/>'
    out+=f'<path d="M{x+20} {y} Q{x+w/2} {y-h*1.25} {x+w-20} {y}" stroke="{L}" stroke-width="1.4"/>'
    for k in range(1,12):
        xx=x+k*w/12
        out+=f'<path d="M{xx} {y-2} L{xx+(xx-x-w/2)*0.08} {y-h*0.9*(1-((xx-x-w/2)/(w/2))**2)}" stroke="{L}" stroke-width="1.1"/>'
    out+=f'<path d="M{x+w*0.18} {y} L{x+w*0.18} {y+22} M{x+w*0.82} {y} L{x+w*0.82} {y+22} M{x+w*0.5} {y} L{x+w*0.5} {y+22}"/>'
    return out

def mosque(x,y,s=1):
    out=''
    def dome(cx,b,r):
        return f'<path d="M{cx-r} {b} Q{cx-r} {b-r*1.5} {cx} {b-r*1.9} Q{cx+r} {b-r*1.5} {cx+r} {b}"/><path d="M{cx} {b-r*1.9} L{cx} {b-r*2.3}"/><circle cx="{cx}" cy="{b-r*2.4}" r="{3*s}"/>'
    out+=f'<path d="M{x-200*s} {y} L{x+200*s} {y} M{x-160*s} {y} L{x-160*s} {y-70*s} L{x+160*s} {y-70*s} L{x+160*s} {y}"/>'
    for k in range(-3,4):
        out+=f'<path d="M{x+k*40*s-12*s} {y} L{x+k*40*s-12*s} {y-38*s} Q{x+k*40*s} {y-56*s} {x+k*40*s+12*s} {y-38*s} L{x+k*40*s+12*s} {y}" stroke="{L}" stroke-width="1.3"/>'
    out+=dome(x,y-70*s,60*s)+dome(x-110*s,y-70*s,26*s)+dome(x+110*s,y-70*s,26*s)
    for mx in (x-200*s,x+200*s):
        out+=f'<path d="M{mx-8*s} {y} L{mx-8*s} {y-200*s} L{mx+8*s} {y-200*s} L{mx+8*s} {y}"/><path d="M{mx-12*s} {y-120*s} L{mx+12*s} {y-120*s} M{mx-11*s} {y-170*s} L{mx+11*s} {y-170*s}"/><path d="M{mx-8*s} {y-200*s} Q{mx} {y-226*s} {mx+8*s} {y-200*s}"/>'
    return out

def tower(x,y,w,h,style=0):
    out=f'<path d="M{x} {y} L{x} {y-h} L{x+w} {y-h-(14 if style==1 else 0)} L{x+w} {y}"/>'
    step=18
    for k in range(1,int(h/step)):
        out+=f'<path d="M{x+4} {y-k*step} L{x+w-4} {y-k*step}" stroke="{L}" stroke-width="1"/>'
    return out

def villa(x,y,s=1):
    out=f'<path d="M{x} {y} L{x} {y-90*s} L{x+180*s} {y-90*s} L{x+180*s} {y} M{x+180*s} {y-60*s} L{x+300*s} {y-60*s} L{x+300*s} {y}"/>'
    out+=f'<path d="M{x-14*s} {y-90*s} L{x+194*s} {y-90*s} M{x+170*s} {y-60*s} L{x+314*s} {y-60*s}"/>'
    for i in range(3):
        out+=f'<rect x="{x+18*s+i*55*s}" y="{y-70*s}" width="36*{s}" height="40" stroke="{L}"/>'.replace(f'36*{s}',str(36*s))
    out+=f'<rect x="{x+205*s}" y="{y-44*s}" width="{70*s}" height="{44*s}" stroke="{L}"/>'
    return out

def sun(cx,cy,r):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#sg)" stroke="none"/>'

DEFS='<defs><radialGradient id="sg"><stop offset="0" stop-color="#F3E7CC"/><stop offset="1" stop-color="#F3E7CC" stop-opacity="0"/></radialGradient></defs>'

def skyline(w=1080,h=520):
    b=h-110
    body=DEFS+sun(w*0.62,b-260,230)
    body+=etihad(90,b,1)+aldarhq(470,b,82)+tower(600,b,70,300)+tower(690,b,56,240,1)+tower(760,b,48,190)+louvre(800,b,250)
    body+=palm(60,b,120,1)+palm(1030,b,130,-1)
    body+=f'<path d="M20 {b} L{w-20} {b}"/>'+water(b+26,w)
    return _svg(w,h,body)

def louvre_scene(w=1080,h=480):
    b=h-120
    body=DEFS+sun(w*0.5,b-120,260)+louvre(210,b,660)+palm(140,b,140,1)+palm(940,b,150,-1)+f'<path d="M20 {b+22} L{w-20} {b+22}"/>'+water(b+48,w)
    return _svg(w,h,body)

def mosque_scene(w=1080,h=520):
    b=h-110
    body=DEFS+sun(w*0.5,b-180,250)+mosque(w/2,b,1.15)+palm(80,b,130,1)+palm(1000,b,130,-1)+f'<path d="M20 {b} L{w-20} {b}"/>'+water(b+26,w)
    return _svg(w,h,body)

def villa_scene(w=1080,h=440):
    b=h-90
    body=DEFS+sun(w*0.3,b-170,200)+villa(330,b,1.3)+palm(250,b,170,1)+palm(860,b,150,-1)+f'<path d="M40 {b} L{w-40} {b}"/>'+f'<path d="M120 {b+30} L{w-120} {b+30}" stroke="{L}" stroke-width="1.4"/>'
    return _svg(w,h,body)

def contract_art(w=420,h=420):
    body=DEFS+sun(210,210,200)
    body+='<path d="M110 70 L270 70 L320 120 L320 350 L110 350 Z"/><path d="M270 70 L270 120 L320 120"/>'
    for k in range(5): body+=f'<path d="M140 {150+k*30} L{290 if k%2==0 else 250} {150+k*30}" stroke="{L}" stroke-width="1.6"/>'
    body+='<path d="M150 315 q20 -26 38 0 t36 -6 t30 4"/>'
    body+='<path d="M330 150 L350 130 L270 230 L250 250 L245 240 L235 245 L255 225 Z"/>'
    body+='<circle cx="290" cy="300" r="26"/><path d="M290 286 L290 300 L300 306"/>'
    return _svg(w,h,body)

def towers_scene(w=1080,h=520):
    b=h-110
    body=DEFS+sun(w*0.4,b-230,240)
    xs=[(120,60,260),(200,80,340,1),(300,56,230),(370,70,400),(460,90,300,1),(570,60,360),(650,76,270),(745,58,330,1),(820,66,240),(905,54,200)]
    for t in xs: body+=tower(t[0],b,t[1],t[2],t[3] if len(t)>3 else 0)
    body+=f'<path d="M20 {b} L{w-20} {b}"/>'+water(b+26,w)
    return _svg(w,h,body)
