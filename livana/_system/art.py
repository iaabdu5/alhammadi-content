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

# ---- added 23 Nov 2026 ----
def galleria(x,y,w=380):
    # low mall with long wave roof + glass bays
    out=f'<path d="M{x} {y} L{x} {y-60} Q{x+w*0.25} {y-110} {x+w*0.5} {y-70} T{x+w} {y-80} L{x+w} {y}"/>'
    out+=f'<path d="M{x+10} {y-58} Q{x+w*0.25} {y-98} {x+w*0.5} {y-62} T{x+w-10} {y-70}" stroke="{L}" stroke-width="1.3"/>'
    for i in range(1,int(w/38)): out+=f'<path d="M{x+i*38} {y} L{x+i*38} {y-40}" stroke="{L}" stroke-width="1.1"/>'
    return out

def sowwah(x,y,w=58,h=300):
    # ADGM-style tower with angled crown
    out=f'<path d="M{x} {y} L{x} {y-h} L{x+w*0.5} {y-h-34} L{x+w} {y-h} L{x+w} {y}"/>'
    for k in range(1,int(h/22)): out+=f'<path d="M{x+5} {y-k*22} L{x+w-5} {y-k*22}" stroke="{L}" stroke-width="1"/>'
    out+=f'<path d="M{x+w*0.5} {y-h-34} L{x+w*0.5} {y}" stroke="{L}" stroke-width="1"/>'
    return out

def dhow(x,y,s=1):
    out=f'<path d="M{x} {y} Q{x+60*s} {y+22*s} {x+140*s} {y-8*s} L{x+150*s} {y-14*s}"/><path d="M{x} {y} L{x-10*s} {y-12*s}"/>'
    out+=f'<path d="M{x+70*s} {y+4*s} L{x+70*s} {y-110*s}"/><path d="M{x+70*s} {y-110*s} Q{x+20*s} {y-60*s} {x+20*s} {y-6*s} L{x+130*s} {y-6*s} Q{x+120*s} {y-60*s} {x+70*s} {y-110*s}" stroke="{L}" stroke-width="1.4"/>'
    return out

def maryah_scene(w=1080,h=560):
    # Al Maryah Island: financial-district towers, wave-roof mall, bridge, promenade, dhow on the water
    b=h-140
    body=DEFS+sun(w*0.28,b-260,230)
    body+=sowwah(330,b,62,290)+sowwah(405,b,62,330)+sowwah(480,b,62,310)+sowwah(555,b,62,270)
    body+=tower(650,b,74,220)+tower(735,b,52,170,1)
    body+=galleria(120,b,520)
    body+=bridge(790,1040,b-10)+f'<path d="M790 {b-10} L790 {b} M1040 {b-10} L1040 {b}"/>'
    body+=palm(80,b,110,1)+palm(700,b,100,-1)
    body+=f'<path d="M20 {b} L{w-20} {b}"/>'+water(b+28,w,3)+dhow(620,b+70,0.9)
    return _svg(w,h,body)

def island_map(w=460,h=520):
    # stylised map: Al Maryah between the city and Al Reem, joined by bridges
    body=DEFS+sun(w*0.5,h*0.5,220)
    body+=f'<path d="M30 40 L30 {h-30}" stroke="{L}" stroke-width="1.4"/>'
    body+=f'<path d="M10 60 Q60 160 40 260 T60 {h-40}"/>'  # city coastline
    body+=f'<path d="M190 70 Q250 50 270 120 Q285 220 260 330 Q240 440 200 470 Q160 430 165 320 Q170 200 190 70 Z" fill="#FAF6EE"/>'  # maryah
    body+=f'<path d="M370 30 Q440 80 430 220 Q420 380 450 500 L{w} 500 L{w} 30 Z" stroke="{L}" stroke-width="1.6"/>'  # reem
    for yy in (150,300,420): body+=f'<path d="M48 {yy} L172 {yy}"/><path d="M48 {yy+8} L172 {yy+8}" stroke="{L}" stroke-width="1.1"/>'
    for yy in (180,360): body+=f'<path d="M272 {yy} L418 {yy}"/><path d="M272 {yy+8} L418 {yy+8}" stroke="{L}" stroke-width="1.1"/>'
    body+=f'<circle cx="222" cy="230" r="9" fill="{G}" stroke="none"/><circle cx="222" cy="230" r="20"/>'
    return _svg(w,h,body)

def plan_art(w=420,h=420):
    # architectural floor plan (blueprint line drawing)
    body=DEFS+sun(w/2,h/2,200)
    body+=f'<rect x="50" y="60" width="320" height="300" stroke-width="3"/>'
    body+=f'<path d="M50 200 L180 200 M180 60 L180 150 M180 190 L180 360 M180 260 L370 260 M290 260 L290 360"/>'
    body+=f'<path d="M180 150 A40 40 0 0 1 220 190" stroke="{L}" stroke-width="1.4"/><path d="M110 200 A36 36 0 0 0 74 236" stroke="{L}" stroke-width="1.4"/>'
    body+=f'<rect x="70" y="80" width="80" height="50" stroke="{L}" stroke-width="1.4"/><rect x="220" y="90" width="120" height="70" rx="6" stroke="{L}" stroke-width="1.4"/><circle cx="330" cy="320" r="18" stroke="{L}" stroke-width="1.4"/>'
    body+=f'<path d="M50 390 L370 390 M50 382 L50 398 M370 382 L370 398" stroke="{L}" stroke-width="1.4"/>'
    return _svg(w,h,body)

# ---- added 24 Nov 2026 ----
def coins(x,y,n=5,r=46):
    # stack of coins seen in perspective
    out=''
    for i in range(n):
        yy=y-i*16
        out+=f'<ellipse cx="{x}" cy="{yy}" rx="{r}" ry="{r*0.32}" fill="#fff"/>'
        out+=f'<path d="M{x-r} {yy} L{x-r} {yy+12} M{x+r} {yy} L{x+r} {yy+12}" stroke="{L}" stroke-width="1.2"/>'
    out+=f'<ellipse cx="{x}" cy="{y-(n-1)*16}" rx="{r*0.6}" ry="{r*0.18}" stroke="{L}" stroke-width="1.2"/>'
    return out

def calculator(x,y,w=200,h=280):
    out=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="#fff"/>'
    out+=f'<rect x="{x+18}" y="{y+18}" width="{w-36}" height="{h*0.2}" rx="6" stroke="{L}" stroke-width="1.4"/>'
    out+=f'<path d="M{x+w-40} {y+18+h*0.1-8} L{x+w-40} {y+18+h*0.1+8} M{x+w-48} {y+18+h*0.1} L{x+w-32} {y+18+h*0.1}" stroke="{G}"/>'
    bw=(w-36-30)/4; top=y+h*0.2+36
    for r_ in range(4):
        for c in range(4):
            bx=x+18+c*(bw+10); by=top+r_*(bw*0.78+10)
            out+=f'<rect x="{bx}" y="{by}" width="{bw}" height="{bw*0.78}" rx="5" stroke="{L if c<3 else G}" stroke-width="1.3"/>'
    return out

def calc_scene(w=1080,h=520):
    b=h-110
    body=DEFS+sun(w*0.5,b-170,220)
    body+=villa(150,b,0.9)+tower(780,b,70,240)+tower(860,b,50,180,1)
    body+=calculator(w/2-120,b-330,240,330)
    body+=coins(330,b-14,6,52)+coins(690,b-14,4,44)
    body+=palm(80,b,110,1)+palm(1000,b,100,-1)
    body+=f'<path d="M30 {b} L{w-30} {b}"/>'+water(b+26,w,2)
    return _svg(w,h,body)

def magnifier(cx,cy,r=110):
    out=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff"/><circle cx="{cx}" cy="{cy}" r="{r-14}" stroke="{L}" stroke-width="1.3"/>'
    out+=f'<path d="M{cx-r*0.45} {cy-r*0.55} Q{cx-r*0.62} {cy-r*0.2} {cx-r*0.55} {cy+r*0.05}" stroke="{L}" stroke-width="2.4"/>'
    a=cx+r*0.71; b_=cy+r*0.71
    out+=f'<path d="M{a} {b_} L{a+r*0.75} {b_+r*0.75}" stroke-width="10"/><path d="M{a} {b_} L{a+r*0.75} {b_+r*0.75}" stroke="#fff" stroke-width="4"/>'
    return out

def flag(x,y,h=120):
    return f'<path d="M{x} {y} L{x} {y-h}"/><path d="M{x} {y-h} Q{x+30} {y-h-14} {x+60} {y-h} T{x+120} {y-h} L{x+120} {y-h+56} Q{x+90} {y-h+42} {x+60} {y-h+56} T{x} {y-h+56}" fill="#FAF6EE"/>'

def inspect_scene(w=1080,h=560):
    # magnifier over a listing card with warning flags
    b=h-80
    body=DEFS+sun(w*0.5,h*0.45,240)
    body+=f'<rect x="250" y="70" width="460" height="380" rx="14" fill="#fff"/>'
    body+=f'<rect x="280" y="100" width="400" height="190" rx="6" stroke="{L}" stroke-width="1.4"/>'+villa(380,280,0.7).replace(f'stroke="{G}"',f'stroke="{L}"')
    for k,ww in enumerate((300,240,330)): body+=f'<path d="M280 {320+k*34} L{280+ww} {320+k*34}" stroke="{L}" stroke-width="5"/>'
    body+=magnifier(700,300,120)
    body+=flag(150,b,150)+flag(900,b-30,130)
    body+=f'<path d="M40 {b} L{w-40} {b}"/>'
    return _svg(w,h,body)

def gridshell(x,y,w=420,h=110):
    # Yas hotel style: two blocks wrapped by a flowing diamond-grid canopy
    out=f'<rect x="{x+30}" y="{y-h+20}" width="{w*0.38}" height="{h-20}"/><rect x="{x+w*0.55}" y="{y-h+20}" width="{w*0.38}" height="{h-20}"/>'
    out+=f'<path d="M{x} {y-h+30} Q{x+w*0.25} {y-h-40} {x+w*0.5} {y-h+6} Q{x+w*0.75} {y-h-46} {x+w} {y-h+24}"/>'
    for i in range(0,int(w),26):
        out+=f'<path d="M{x+i} {y-h+20} L{x+i+26} {y-h-14}" stroke="{L}" stroke-width="1"/><path d="M{x+i+26} {y-h+20} L{x+i} {y-h-14}" stroke="{L}" stroke-width="1"/>'
    out+=f'<path d="M{x+w*0.46} {y-h+20} L{x+w*0.5} {y} M{x+w*0.54} {y-h+20} L{x+w*0.5} {y}" stroke="{L}" stroke-width="1.2"/>'
    return out

def theme_roof(x,y,w=360):
    # low flowing theme-park roof (generic, unbranded)
    return f'<path d="M{x} {y} Q{x+w*0.18} {y-34} {x+w*0.5} {y-70} Q{x+w*0.82} {y-34} {x+w} {y}"/><path d="M{x+w*0.12} {y-6} Q{x+w*0.5} {y-56} {x+w*0.88} {y-6}" stroke="{L}" stroke-width="1.3"/>'

def track(x0,x1,y):
    d=f'M{x0} {y} C{x0+120} {y+40} {x0+220} {y-30} {x0+360} {y+10} S{x1-100} {y+40} {x1} {y}'
    return f'<path d="{d}" stroke="{L}" stroke-width="5"/><path d="{d}" stroke="#fff" stroke-width="1.5" stroke-dasharray="10 10"/>'

def yas_scene(w=1080,h=520):
    b=h-130
    body=DEFS+sun(w*0.72,b-200,220)
    body+=gridshell(420,b,460,120)+theme_roof(40,b,330)
    body+=tower(900,b,60,200)+tower(970,b,46,150,1)
    body+=track(40,w-40,b+34)
    body+=palm(380,b,120,1)+palm(895,b,96,-1)
    body+=f'<path d="M20 {b} L{w-20} {b}"/>'+water(b+64,w,2)+dhow(150,b+100,0.7)
    return _svg(w,h,body)

# ---- added 25 Nov 2026 ----
def gauge(cx,cy,r=300,val=0.0,labels=('0%','5%')):
    # semicircle meter, needle at val (0..1, left->right)
    import math
    out=f'<path d="M{cx-r} {cy} A{r} {r} 0 0 1 {cx+r} {cy}"/>'
    out+=f'<path d="M{cx-r+34} {cy} A{r-34} {r-34} 0 0 1 {cx+r-34} {cy}" stroke="{L}" stroke-width="1.3"/>'
    for k in range(21):
        a=math.pi*(1-k/20); l=26 if k%5==0 else 12
        x1=cx+(r-4)*math.cos(a); y1=cy-(r-4)*math.sin(a); x2=cx+(r-4-l)*math.cos(a); y2=cy-(r-4-l)*math.sin(a)
        out+=f'<path d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}" stroke-width="{2 if k%5==0 else 1.2}"/>'
    a=math.pi*(1-val)
    out+=f'<path d="M{cx} {cy} L{cx+(r-70)*math.cos(a):.1f} {cy-(r-70)*math.sin(a):.1f}" stroke-width="5"/><circle cx="{cx}" cy="{cy}" r="16" fill="#fff" stroke-width="3"/>'
    return out

def qasr_watan(x,y,s=1):
    # Qasr Al Watan style: wide palace, big central dome, side domes, arcade
    def dome(cx,b,r,h):
        return f'<path d="M{cx-r} {b} Q{cx-r} {b-h*0.9} {cx} {b-h} Q{cx+r} {b-h*0.9} {cx+r} {b}"/><path d="M{cx} {b-h} L{cx} {b-h-18*s}"/>'
    w=440*s
    out=f'<path d="M{x-w} {y} L{x+w} {y} M{x-w+20*s} {y} L{x-w+20*s} {y-90*s} L{x+w-20*s} {y-90*s} L{x+w-20*s} {y}"/>'
    out+=f'<path d="M{x-w+10*s} {y-90*s} L{x+w-10*s} {y-90*s}"/>'
    for k in range(-9,10):
        xx=x+k*44*s
        out+=f'<path d="M{xx-14*s} {y} L{xx-14*s} {y-46*s} Q{xx} {y-66*s} {xx+14*s} {y-46*s} L{xx+14*s} {y}" stroke="{L}" stroke-width="1.3"/>'
    out+=f'<rect x="{x-120*s}" y="{y-150*s}" width="{240*s}" height="{60*s}"/>'
    out+=dome(x,y-150*s,110*s,170*s)+f'<path d="M{x-80*s} {y-150*s} Q{x} {y-290*s} {x+80*s} {y-150*s}" stroke="{L}" stroke-width="1.3"/>'
    for sx in (-1,1):
        out+=dome(x+sx*230*s,y-90*s,44*s,70*s)+dome(x+sx*350*s,y-90*s,30*s,48*s)
    return out

def qasr_scene(w=1080,h=520):
    b=h-110
    body=DEFS+sun(w*0.5,b-210,250)+qasr_watan(w/2,b,1.05)+palm(40,b,110,1)+palm(1040,b,110,-1)
    body+=f'<path d="M20 {b} L{w-20} {b}"/>'+f'<path d="M140 {b+28} L{w-140} {b+28}" stroke="{L}" stroke-width="1.4"/>'+f'<path d="M260 {b+52} L{w-260} {b+52}" stroke="{L}" stroke-width="1.2"/>'
    return _svg(w,h,body)

def supply_scene(w=1080,h=640,vals=((2027,14.6),(2028,24.2))):
    # two towers whose heights are proportional to the values
    b=h-80; mx=max(v for _,v in vals); out=DEFS+sun(w*0.5,b-260,260)
    xs=[w*0.30,w*0.62]
    for (yr,v),x in zip(vals,xs):
        hh=(h-230)*v/mx; tw=170
        out+=f'<rect x="{x-tw/2}" y="{b-hh}" width="{tw}" height="{hh}" fill="#fff"/>'
        for k in range(1,int(hh/26)):
            out+=f'<path d="M{x-tw/2+10} {b-k*26} L{x+tw/2-10} {b-k*26}" stroke="{L}" stroke-width="1"/>'
        out+=f'<path d="M{x} {b-hh} L{x} {b-hh-30}"/>'
    out+=crane(w*0.83,b,h-200,180) if 'crane' in globals() else ''
    out+=palm(70,b,110,1)+f'<path d="M30 {b} L{w-30} {b}"/>'
    return _svg(w,h,out)

def seal(cx,cy,r=150,text='TAWTHEEQ · REGISTERED · ABU DHABI · '):
    import math
    out=f'<circle cx="{cx}" cy="{cy}" r="{r}"/><circle cx="{cx}" cy="{cy}" r="{r-14}" stroke="{L}" stroke-width="1.2"/><circle cx="{cx}" cy="{cy}" r="{r-62}"/>'
    for k in range(48):
        a=2*math.pi*k/48; out+=f'<path d="M{cx+(r+6)*math.cos(a):.1f} {cy+(r+6)*math.sin(a):.1f} L{cx+(r+14)*math.cos(a):.1f} {cy+(r+14)*math.sin(a):.1f}" stroke="{L}" stroke-width="1.4"/>'
    out+=f'<defs><path id="sp{cx}" d="M{cx-r+38} {cy} A{r-38} {r-38} 0 1 1 {cx+r-38} {cy} A{r-38} {r-38} 0 1 1 {cx-r+38} {cy}"/></defs>'
    out+=f'<text font-family="MS" font-size="19" font-weight="500" letter-spacing="5" fill="{G}" stroke="none"><textPath href="#sp{cx}">{text}{text}</textPath></text>'
    out+=f'<path d="M{cx-34} {cy+2} L{cx-8} {cy+28} L{cx+40} {cy-26}" stroke-width="6"/>'
    return out

def shop(x,y,s=1):
    return f'<path d="M{x} {y} L{x} {y-90*s} L{x+160*s} {y-90*s} L{x+160*s} {y}"/><path d="M{x-10*s} {y-90*s} L{x+170*s} {y-90*s} L{x+160*s} {y-120*s} L{x} {y-120*s} Z"/>'+''.join(f'<path d="M{x+i*32*s} {y-90*s} q{16*s} {22*s} {32*s} 0" stroke="{L}" stroke-width="1.4"/>' for i in range(5))+f'<rect x="{x+20*s}" y="{y-60*s}" width="{60*s}" height="{60*s}" stroke="{L}"/><rect x="{x+100*s}" y="{y-60*s}" width="{40*s}" height="{40*s}" stroke="{L}"/>'

def factory(x,y,s=1):
    return f'<path d="M{x} {y} L{x} {y-60*s} L{x+50*s} {y-90*s} L{x+50*s} {y-60*s} L{x+100*s} {y-90*s} L{x+100*s} {y-60*s} L{x+150*s} {y-90*s} L{x+150*s} {y} Z"/><path d="M{x+120*s} {y-90*s} L{x+120*s} {y-150*s} L{x+140*s} {y-150*s} L{x+140*s} {y-80*s}"/><path d="M{x+130*s} {y-165*s} q12 -12 0 -24 q-12 -12 0 -24" stroke="{L}" stroke-width="1.4"/>'+''.join(f'<rect x="{x+15*s+i*45*s}" y="{y-40*s}" width="{25*s}" height="{20*s}" stroke="{L}"/>' for i in range(3))

def handover_scene(w=1080,h=540):
    # finished tower + villa, big key with tag, crane leaving
    b=h-90
    body=DEFS+sun(w*0.55,b-220,240)
    body+=tower(160,b,90,330)+tower(260,b,64,240,1)+villa(600,b,0.95)
    body+=crane(930,b,300,150).replace(f'stroke="{G}"',f'stroke="{L}"') if 'crane' in globals() else ''
    kx,ky=430,b-200
    body+=f'<circle cx="{kx}" cy="{ky}" r="52" fill="#fff" stroke-width="4"/><circle cx="{kx}" cy="{ky}" r="20" stroke-width="3"/>'
    body+=f'<path d="M{kx+52} {ky} L{kx+190} {ky} M{kx+150} {ky} L{kx+150} {ky+30} M{kx+180} {ky} L{kx+180} {ky+24}" stroke-width="7"/>'
    body+=palm(60,b,110,1)+f'<path d="M30 {b} L{w-30} {b}"/>'+water(b+26,w,2)
    return _svg(w,h,body)

# ---- added 26 Nov 2026 ----
def _cone(bx,by,wb,tx,ty,wt,fill='#fff'):
    # truncated funnel cone (wide top) with elliptical rim, Gehry-style
    out=f'<path d="M{bx-wb/2} {by} L{tx-wt/2} {ty} A{wt/2} {wt*0.16} 0 0 1 {tx+wt/2} {ty} L{bx+wb/2} {by} Z" fill="{fill}"/>'
    out+=f'<ellipse cx="{tx}" cy="{ty}" rx="{wt/2}" ry="{wt*0.16}" fill="{fill}"/>'
    for f in (0.33,0.66):
        out+=f'<path d="M{bx-wb/2+wb*f} {by} L{tx-wt/2+wt*f} {ty+wt*0.15}" stroke="{L}" stroke-width="1.1"/>'
    return out

def guggenheim(x,y,s=1):
    # Guggenheim Abu Dhabi impression: stacked gallery boxes + tilted cones of varying heights
    S=lambda v:v*s
    out=''
    boxes=[(-330,90,200,0),(-150,120,180,0),(10,80,220,0),(-240,60,150,90),(-60,70,170,120),(120,55,140,80),(210,95,160,0)]
    for dx,hh,ww,up in boxes:
        bx=x+S(dx); by=y-S(up)
        out+=f'<rect x="{bx}" y="{by-S(hh)}" width="{S(ww)}" height="{S(hh)}" fill="#fff"/>'
        for k in range(1,int(ww/36)): out+=f'<path d="M{bx+S(k*36)} {by-S(hh)+S(8)} L{bx+S(k*36)} {by-S(8)}" stroke="{L}" stroke-width="1"/>'
    cones=[(-250,150,60,-280,330,110),(-40,200,70,-10,420,150),(170,170,60,210,350,120),(330,90,46,360,250,90),(-380,60,40,-410,200,70)]
    for dx,up,wb,tdx,tup,wt in cones:
        out+=_cone(x+S(dx),y-S(up),S(wb),x+S(tdx),y-S(tup),S(wt))
    out+=f'<path d="M{x-S(440)} {y} L{x+S(440)} {y}"/>'
    return out

def guggenheim_scene(w=1080,h=560):
    b=h-110
    body=DEFS+sun(w*0.62,b-300,250)+guggenheim(w/2,b,1.0)+palm(50,b,110,1)+palm(1030,b,100,-1)
    body+=f'<path d="M20 {b} L{w-20} {b}"/>'+water(b+26,w,3)
    return _svg(w,h,body)

def district_map(w=900,h=620,pins=()):
    # stylised Saadiyat Cultural District: coastline, lagoon, road, pins (x,y,label) drawn by caller
    body=DEFS+sun(w*0.5,h*0.5,300)
    body+=f'<path d="M20 {h*0.72} Q{w*0.25} {h*0.62} {w*0.45} {h*0.70} T{w*0.8} {h*0.66} T{w-20} {h*0.74}"/>'
    body+=water(h*0.80,w,3)
    body+=f'<path d="M{w*0.08} {h*0.12} Q{w*0.5} {h*0.02} {w*0.92} {h*0.18}" stroke="{L}" stroke-width="10" opacity="0.35"/>'
    body+=f'<path d="M{w*0.08} {h*0.12} Q{w*0.5} {h*0.02} {w*0.92} {h*0.18}" stroke-dasharray="14 12" stroke-width="1.4"/>'
    body+=f'<path d="M{w*0.30} {h*0.55} Q{w*0.36} {h*0.48} {w*0.44} {h*0.55} Q{w*0.38} {h*0.60} {w*0.30} {h*0.55} Z" stroke="{L}" stroke-width="1.4"/>'
    for px,py,big in pins:
        r=13 if big else 8
        body+=f'<circle cx="{px}" cy="{py}" r="{r}" fill="{G if big else "#fff"}" stroke="{G}" stroke-width="2.5"/>'
        if big: body+=f'<circle cx="{px}" cy="{py}" r="{r+14}" stroke="{G}" stroke-width="1.4"/>'
    return _svg(w,h,body)

def keytag(cx,cy,w=320,h=560,text1='',text2=''):
    # hotel key tag: rounded-top tag with hole, ring and key
    x0=cx-w/2; y0=cy-h/2
    out=f'<path d="M{x0} {y0+w/2} A{w/2} {w/2} 0 0 1 {x0+w} {y0+w/2} L{x0+w} {y0+h-30} Q{x0+w} {y0+h} {x0+w-30} {y0+h} L{x0+30} {y0+h} Q{x0} {y0+h} {x0} {y0+h-30} Z" fill="#fff" stroke-width="2.5"/>'
    out+=f'<path d="M{x0+16} {y0+w/2} A{w/2-16} {w/2-16} 0 0 1 {x0+w-16} {y0+w/2} L{x0+w-16} {y0+h-40} Q{x0+w-16} {y0+h-16} {x0+w-40} {y0+h-16} L{x0+40} {y0+h-16} Q{x0+16} {y0+h-16} {x0+16} {y0+h-40} Z" stroke="{L}" stroke-width="1.3"/>'
    out+=f'<circle cx="{cx}" cy="{y0+70}" r="22" stroke-width="2.5"/>'
    out+=f'<circle cx="{cx}" cy="{y0-40}" r="58" stroke-width="3"/>'
    kx,ky=cx+40,y0-90
    out+=f'<circle cx="{kx}" cy="{ky}" r="26" fill="#fff" stroke-width="3.5"/><circle cx="{kx}" cy="{ky}" r="9" stroke-width="2.5"/><path d="M{kx+26} {ky} L{kx+130} {ky} M{kx+100} {ky} L{kx+100} {ky+22} M{kx+122} {ky} L{kx+122} {ky+16}" stroke-width="5"/>'
    return out

def door_hanger(cx,cy,w=420,h=900):
    x0=cx-w/2; y0=cy-h/2; r=78
    out=f'<path d="M{x0} {y0+40} Q{x0} {y0} {x0+40} {y0} L{x0+w-40} {y0} Q{x0+w} {y0} {x0+w} {y0+40} L{x0+w} {y0+h-30} Q{x0+w} {y0+h} {x0+w-30} {y0+h} L{x0+30} {y0+h} Q{x0} {y0+h} {x0} {y0+h-30} Z" fill="#fff" stroke-width="2.5"/>'
    out+=f'<circle cx="{cx}" cy="{y0+130}" r="{r}" stroke-width="2.5"/><path d="M{cx+r*0.7} {y0+130-r*0.7} L{x0+w-10} {y0+20}" stroke-width="2.5"/>'
    out+=f'<path d="M{x0+22} {y0+250} L{x0+w-22} {y0+250}" stroke="{L}" stroke-width="1.3"/>'
    return out

def ticket(x,y,w=820,h=420,stub=220):
    # museum ticket with perforated stub and notches
    r=34
    out=f'<path d="M{x} {y} L{x+w-stub} {y} A{r} {r} 0 0 0 {x+w-stub+0.1} {y} L{x+w} {y} L{x+w} {y+h/2-r} A{r} {r} 0 0 0 {x+w} {y+h/2+r} L{x+w} {y+h} L{x} {y+h} L{x} {y+h/2+r} A{r} {r} 0 0 0 {x} {y+h/2-r} Z" fill="#fff" stroke-width="2.5"/>'
    out+=f'<path d="M{x+w-stub} {y+10} L{x+w-stub} {y+h-10}" stroke-dasharray="6 10" stroke-width="2"/>'
    out+=f'<rect x="{x+18}" y="{y+18}" width="{w-36}" height="{h-36}" stroke="{L}" stroke-width="1.2"/>'
    return out

def height_scale(x,y,h=900,maxv=88,marks=(0,22,44,66,88)):
    # vertical ruler with ticks; value v sits at y - h*v/maxv
    out=f'<path d="M{x} {y} L{x} {y-h}" stroke-width="2.5"/>'
    for v in range(0,maxv+1,2):
        yy=y-h*v/maxv; l=34 if v in marks else (18 if v%10==0 else 9)
        out+=f'<path d="M{x} {yy:.1f} L{x+l} {yy:.1f}" stroke-width="{2 if v in marks else 1.1}"/>'
    return out
