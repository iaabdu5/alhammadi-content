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

# ---- added 22 Nov 2026 ----
def pavilion(x,y,w,h,peaks=3):
    # gallery pavilion with saw-tooth (studio) roof
    out=f'<path d="M{x} {y} L{x} {y-h}'
    pw=w/peaks
    for i in range(peaks):
        out+=f' L{x+i*pw+pw*0.7} {y-h-26} L{x+i*pw+pw*0.7} {y-h} L{x+(i+1)*pw} {y-h}'
    out+=f' L{x+w} {y}"/>'
    for i in range(int(w/46)):
        out+=f'<rect x="{x+14+i*46}" y="{y-h*0.62}" width="26" height="{h*0.45}" stroke="{L}" stroke-width="1.3"/>'
    return out

def screen(x,y,w=150,h=84):
    # rooftop cinema screen on legs + little rows of seats
    out=f'<rect x="{x}" y="{y-h-30}" width="{w}" height="{h}"/><path d="M{x+16} {y-30} L{x+16} {y} M{x+w-16} {y-30} L{x+w-16} {y}"/>'
    out+=f'<path d="M{x+30} {y-h-4} q{w*0.2} -24 {w*0.4} 0" stroke="{L}" stroke-width="1.3"/><circle cx="{x+w*0.72}" cy="{y-h-8}" r="9" stroke="{L}" stroke-width="1.3"/>'
    return out

def bridge(x0,x1,y):
    out=f'<path d="M{x0} {y} Q{(x0+x1)/2} {y-40} {x1} {y}"/><path d="M{x0} {y-26} Q{(x0+x1)/2} {y-66} {x1} {y-26}" stroke="{L}" stroke-width="1.4"/>'
    for k in range(1,8):
        xx=x0+k*(x1-x0)/8; t=k/8; yy=y-160*t*(1-t)
        out+=f'<path d="M{xx} {yy} L{xx} {yy-26}" stroke="{L}" stroke-width="1.1"/>'
    return out

def creative_scene(w=1080,h=520):
    # NOMA-style creative district: studio pavilions, rooftop cinema, bridge, palms, Louvre dome far right
    b=h-100
    body=DEFS+sun(w*0.74,b-230,230)
    body+=pavilion(90,b,260,120,4)+pavilion(380,b,200,170,3)
    body+=f'<path d="M380 {b-170} L580 {b-170}"/>'+screen(405,b-170,150,80)
    body+=bridge(600,800,b-60)+f'<path d="M600 {b-60} L600 {b} M800 {b-60} L800 {b}"/>'
    body+=louvre(820,b,220)
    body+=palm(60,b,130,1)+palm(1040,b,120,-1)
    for xx in (330,355): body+=f'<circle cx="{xx}" cy="{b-26}" r="16" stroke="{L}" stroke-width="1.4"/><path d="M{xx} {b-10} L{xx} {b}"/>'
    body+=f'<path d="M20 {b} L{w-20} {b}"/>'+water(b+26,w,3)
    return _svg(w,h,body)

def crane(x,y,h=360,jib=300):
    out=f'<path d="M{x} {y} L{x} {y-h} M{x+22} {y} L{x+22} {y-h}"/>'
    for k in range(int(h/30)):
        yy=y-k*30; out+=f'<path d="M{x} {yy} L{x+22} {yy-30}" stroke="{L}" stroke-width="1.2"/>'
    out+=f'<path d="M{x-90} {y-h} L{x+jib} {y-h} M{x-90} {y-h+16} L{x+jib} {y-h+16} M{x+11} {y-h-50} L{x-90} {y-h} M{x+11} {y-h-50} L{x+jib} {y-h}"/>'
    out+=f'<rect x="{x-96}" y="{y-h+16}" width="40" height="30"/>'
    hx=x+jib*0.7; out+=f'<path d="M{hx} {y-h+16} L{hx} {y-h+150}"/><path d="M{hx-10} {y-h+150} L{hx+10} {y-h+150} L{hx} {y-h+165} Z"/>'
    return out

def frame_tower(x,y,w,h,floors_done):
    # building under construction: finished floors with windows, upper floors open frame
    out=''; fh=h/12
    for k in range(12):
        yy=y-(k+1)*fh
        if k<floors_done:
            out+=f'<rect x="{x}" y="{yy}" width="{w}" height="{fh}"/>'
            for i in range(int(w/30)): out+=f'<path d="M{x+10+i*30} {yy+fh*0.3} L{x+10+i*30} {yy+fh*0.75}" stroke="{L}" stroke-width="1.2"/>'
        else:
            out+=f'<path d="M{x} {yy} L{x+w} {yy}" stroke="{L}" stroke-width="1.4"/>'
    out+=f'<path d="M{x} {y} L{x} {y-h} M{x+w} {y} L{x+w} {y-h} M{x+w/2} {y-floors_done*fh} L{x+w/2} {y-h}" />'
    return out

def construction_scene(w=1080,h=520):
    b=h-90
    body=DEFS+sun(w*0.3,b-250,220)
    body+=frame_tower(380,b,180,360,7)+frame_tower(620,b,140,280,9)+crane(300,b,400,420)
    body+=tower(830,b,60,200)+tower(900,b,50,150)+palm(120,b,130,1)
    body+=f'<path d="M20 {b} L{w-20} {b}"/><path d="M80 {b+28} L{w-80} {b+28}" stroke="{L}" stroke-width="1.4"/>'
    return _svg(w,h,body)

def louvre_dome(w=1080,h=600):
    # close-up of the Louvre dome lattice with light rays, over water
    b=h-130; cx=w/2; R=430
    body=DEFS+sun(cx,b-40,300)
    body+=f'<path d="M{cx-R} {b} Q{cx} {b-R*0.62} {cx+R} {b}"/><path d="M{cx-R+30} {b+6} Q{cx} {b-R*0.5} {cx+R-30} {b+6}" stroke="{L}" stroke-width="1.4"/>'
    for k in range(-6,7):
        xx=cx+k*R/7; t=(xx-cx)/R; top=b-R*0.31*(1-t*t)*2*0.99
        body+=f'<path d="M{xx} {top} L{xx+k*6} {b}" stroke="{L}" stroke-width="1"/>'
    for k in range(1,9):
        yy=b-8-k*13
        body+=f'<path d="M{cx-20-k*14} {yy+80} L{cx-60-k*24} {b-6}" stroke="{L}" stroke-width="0.9"/><path d="M{cx+20+k*14} {yy+80} L{cx+60+k*24} {b-6}" stroke="{L}" stroke-width="0.9"/>'
    for px in (cx-R*0.62,cx,cx+R*0.62):
        body+=f'<path d="M{px} {b-R*0.31*(1-((px-cx)/R)**2)*2+4} L{px} {b+40}"/>'
    body+=f'<path d="M30 {b+40} L{w-30} {b+40}"/>'+water(b+66,w,3)
    return _svg(w,h,body)

def keys_art(s=200):
    body=f'<circle cx="{s*0.32}" cy="{s*0.32}" r="{s*0.2}"/><circle cx="{s*0.32}" cy="{s*0.32}" r="{s*0.07}" stroke="{L}"/>'
    body+=f'<path d="M{s*0.46} {s*0.46} L{s*0.88} {s*0.88} M{s*0.72} {s*0.72} L{s*0.8} {s*0.64} M{s*0.82} {s*0.82} L{s*0.9} {s*0.74}"/>'
    return _svg(s,s,body)
