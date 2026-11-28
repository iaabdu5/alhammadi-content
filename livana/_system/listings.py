from v4 import *
from art import _svg
N=lambda s:f'<span dir="ltr">{s}</span>'
ADM='ADM 202501936260'

def money(v): return f'{v:,}'

# ---------- custom scenes per area ----------
def sc_saadiyat(w=1080,h=520):
    b=h-110
    body=DEFS+sun(w*0.66,b-200,220)
    body+=louvre(560,b,420)
    body+=midrise(110,b,170,300,4)+midrise(300,b,150,230,3)
    body+=palm(80,b,130,1)+palm(1010,b,130,-1)+tree(470,b,90,34)
    body+=f'<path d="M20 {b} L{w-20} {b}"/>'+water(b+26,w)
    return _svg(w,h,body)

def sc_raha(w=1080,h=520):
    b=h-110
    body=DEFS+sun(w*0.3,b-220,210)
    for t in [(420,70,330),(510,60,280,1),(590,80,370),(690,58,250,1),(760,66,300)]:
        body+=tower(t[0],b,t[1],t[2],t[3] if len(t)>3 else 0)
    body+=dhow(150,b+40,1)+palm(880,b,140,-1)+palm(960,b,110,-1)
    body+=f'<path d="M380 {b} L{w-20} {b}"/>'+water(b+26,w)
    return _svg(w,h,body)

def sc_shamkha(w=1080,h=520):
    b=h-110
    body=DEFS+sun(w*0.5,b-210,230)
    body+=midrise(200,b,200,260,4)+midrise(430,b,230,320,5)+midrise(690,b,190,230,4)
    body+=tree(150,b,100,40)+tree(930,b,110,44)+palm(60,b,130,1)+palm(1020,b,120,-1)
    body+=f'<path d="M20 {b} L{w-20} {b}"/>'+f'<path d="M120 {b+30} L{w-120} {b+30}" stroke="{L}" stroke-width="1.4"/>'
    return _svg(w,h,body)

def sc_yas(w=1080,h=520): return yas_scene(w,h)
def sc_villa(w=1080,h=520): return villa_scene(w,h)

def sc_alain(w=1080,h=520):
    b=h-110
    body=DEFS+sun(w*0.7,b-230,200)
    body+=f'<path d="M20 {b-60} Q200 {b-260} 380 {b-170} T720 {b-230} T1060 {b-120}" stroke="{L}" stroke-width="1.6"/>'
    body+=midrise(380,b,320,280,6)
    for x in (110,200,860,950): body+=palm(x,b,120+(x%3)*14,1 if x<500 else -1)
    body+=f'<path d="M20 {b} L{w-20} {b}"/>'+f'<path d="M120 {b+30} L{w-120} {b+30}" stroke="{L}" stroke-width="1.4"/>'
    return _svg(w,h,body)

def sc_townhouse(w=1080,h=520):
    b=h-100
    body=DEFS+sun(w*0.5,b-200,220)
    for i in range(3): body+=villa(120+i*290,b,0.85)
    body+=palm(60,b,140,1)+palm(1030,b,140,-1)
    body+=f'<path d="M20 {b} L{w-20} {b}"/>'+f'<path d="M120 {b+30} L{w-120} {b+30}" stroke="{L}" stroke-width="1.4"/>'
    return _svg(w,h,body)

# ---------- data (from Ahmad's sheet, 28 Nov 2026) ----------
L=[
 dict(id='reeman-1br', photo='reeman2_n21', ar='ريمان ليفنج', en='Reeman Living', area='الشامخة', area_en='Al Shamkha', type='شقة', type_en='Apartment',
      br='غرفة وصالة', br_en='1 Bedroom', size='520', price=830000, deal='sale', status='off', scene=sc_shamkha),
 dict(id='parkview-1br', ar='بارك فيو', en='Park View', area='جزيرة السعديات', area_en='Saadiyat Island', type='شقة', type_en='Apartment',
      br='غرفة وصالة', br_en='1 Bedroom', size='1,013', price=1600000, deal='sale', status='ready', scene=sc_saadiyat),
 dict(id='fay-reeman-villa', photo='fay_cgi30_lifestyle_04', ar='فاي الريمان', en='Fay Al Reeman', area='الشامخة', area_en='Al Shamkha', type='فيلا', type_en='Villa',
      br='4 غرف نوم', br_en='4 Bedrooms', size='6,036', price=4160000, deal='sale', status='off', scene=sc_villa),
 dict(id='sama-yas-1br', photo='sama_sam_banner_image_desk_1', ar='سما ياس', en='Sama Yas', area='جزيرة ياس', area_en='Yas Island', type='شقة', type_en='Apartment',
      br='غرفة وصالة', br_en='1 Bedroom', size='1,083', price=2690000, deal='sale', status='off', scene=sc_yas),
 dict(id='rahba-3br', ar='الرحبة 1', en='Al Rahba 1', area='شاطئ الراحة', area_en='Al Raha Beach', type='شقة', type_en='Apartment',
      br='3 غرف + غرفة خادمة', br_en='3 Bedrooms + Maid', size='1,922', price=3780000, deal='sale', status='ready', scene=sc_raha),
 dict(id='manarat3-1br', photo='man_manarat_living_gallery_1', ar='منارات ليفنج 3', en='Manarat Living 3', area='جزيرة السعديات', area_en='Saadiyat Island', type='شقة', type_en='Apartment',
      br='غرفة وصالة', br_en='1 Bedroom', size='758', price=1850000, deal='sale', status='off', scene=sc_saadiyat),
 dict(id='aldeem-th', ar='الديم تاون هاوس', en='Al Deem Townhouse', area='الباهية', area_en='Al Bahia', type='تاون هاوس', type_en='Townhouse',
      br='4 غرف نوم', br_en='4 Bedrooms', size='4,412', price=4700000, deal='sale', status='off', scene=sc_townhouse),
 dict(id='alain-building', ar='بناية في حي المربعة', en='Building · Hai Al Murabaa', area='العين', area_en='Al Ain', type='بناية كاملة', type_en='Whole building',
      br='بناية كاملة', br_en='Whole building', size='7,233', price=4000000, deal='sale', status='ready', scene=sc_alain),
 dict(id='manarat2-1br', photo='man_manarat_living_gallery_2', ar='منارات ليفنج 2', en='Manarat Living 2', area='جزيرة السعديات', area_en='Saadiyat Island', type='شقة', type_en='Apartment',
      br='غرفة وصالة', br_en='1 Bedroom', size='749', price=1950000, deal='sale', status='off', scene=sc_saadiyat),
 dict(id='reeman-studio-rent', photo='reeman2_reeman-living-2_front_image', ar='ريمان ليفنج', en='Reeman Living', area='الشامخة', area_en='Al Shamkha', type='استوديو', type_en='Studio',
      br='استوديو', br_en='Studio', size='280', price=45000, deal='rent', status='ready', scene=sc_shamkha),
]
def st_ar(x): return 'جاهز' if x['status']=='ready' else 'على الخارطة'
def st_en(x): return 'READY' if x['status']=='ready' else 'OFF PLAN'
def deal_ar(x): return 'للبيع' if x['deal']=='sale' else 'للإيجار'
def deal_en(x): return 'FOR SALE' if x['deal']=='sale' else 'FOR RENT'
def unit(x): return 'درهم سنوياً' if x['deal']=='rent' else 'درهم'
def unit_en(x): return 'AED / YEAR' if x['deal']=='rent' else 'AED'
def origline(x): return f'<div class="orig a">السعر الأصلي {N(money(x["orig"]))} درهم</div>' if x.get('orig') else ''

def pic(x,w,h,pos='center'):
    return f'<img src="ph/{x["photo"]}.jpg" style="width:{w}px;height:{h}px;object-fit:cover;object-position:{pos};display:block">'
def art(x,w,h,pos='center'):
    return pic(x,w,h,pos) if x.get('photo') else x['scene'](w,h)

COMMON='''
.cta{display:inline-flex;align-items:center;gap:14px;border:1.5px solid #111;padding:14px 30px;font:700 28px TJ,MS;direction:rtl}
.cta i{font:500 18px MS;font-style:normal;letter-spacing:3px;color:#B99A5B;direction:ltr}
.orig{font:500 24px TJ,MS;color:#999;margin-top:6px}
.adm{position:absolute;left:66px;bottom:26px;font:500 12px MS;letter-spacing:2px;color:#aaa}
'''
def foot_adm(): return ''

# ---------- layout A: porthole + price ----------
def layA(x,fn):
    page(fn,COMMON+'''
.port{left:76px;top:230px;width:440px;height:440px;border-radius:50%;border:1.5px solid #B99A5B;overflow:hidden;display:flex;align-items:flex-end;justify-content:center}
.port2{left:60px;top:214px;width:472px;height:472px;border-radius:50%;border:1px solid #E6DAC0}
.port svg{width:760px;height:366px;margin-bottom:30px}
.k{right:90px;top:250px}
.h{right:88px;top:292px;width:480px;text-align:right;font:800 66px/1.25 TJ,MS}
.ar{right:90px;top:470px;text-align:right;font:500 32px TJ,MS;color:#B99A5B}
.en{right:92px;top:525px;font:500 28px CG;font-style:italic;color:#888}
.line{left:90px;right:90px;top:760px}
.pk{right:90px;top:800px;text-align:right;font:500 28px TJ,MS;color:#666}
.pr{right:84px;top:845px;font:300 140px/1 MS;letter-spacing:-3px;direction:ltr}
.pu{right:92px;top:1000px;font:500 20px MS;letter-spacing:5px;color:#B99A5B}
.specs{left:90px;right:90px;top:1060px;display:flex;direction:rtl;border-top:1px solid #E6DAC0;border-bottom:1px solid #E6DAC0}
.sp{flex:1;padding:22px 0;text-align:center;border-left:1px solid #E6DAC0}.sp:last-child{border-left:0}
.sp b{display:block;font:700 30px TJ,MS}.sp i{display:block;font:500 16px MS;font-style:normal;letter-spacing:3px;color:#999;margin-top:6px;direction:ltr}
.oo{right:90px;top:1000px}
''',f'''<div class="abs port2"></div><div class="abs port" style="{'align-items:center' if x.get('photo') else ''}">{pic(x,440,440) if x.get('photo') else x['scene'](1080,520)}</div>
<div class="abs k"><span class="kick">{deal_en(x)} · {st_en(x)}</span></div>
<div class="abs h a">{x['ar']}</div>
<div class="abs ar a">{x['type']} {deal_ar(x)} · {x['area']}</div>
<div class="abs en">{x['en']}, {x['area_en']}</div>
<div class="abs hl line"></div>
<div class="abs pk a">{'الإيجار' if x['deal']=='rent' else 'السعر'}</div>
<div class="abs pr">{money(x['price'])}</div>
<div class="abs pu" style="right:{92 if not x.get('orig') else 92}px">{unit_en(x)}</div>
{('<div class="abs" style="left:90px;top:1000px">'+origline(x)+'</div>') if x.get('orig') else ''}
<div class="abs specs"><div class="sp"><b class="a">{x['br']}</b><i>{x['br_en'].upper()}</i></div><div class="sp"><b>{N(x['size'])}</b><i>SQ FT</i></div><div class="sp"><b class="a">{st_ar(x)}</b><i>{st_en(x)}</i></div></div>
{foot_adm()}''')

# ---------- layout B: drawing band + gold price bar ----------
def layB(x,fn):
    page(fn,COMMON+'''
.band{left:0;top:190px;width:1080px;height:520px}
.k{right:90px;top:735px}
.h{right:90px;top:775px;text-align:right;font:800 72px/1.2 TJ,MS}
.sub{right:90px;top:870px;text-align:right;font:500 32px TJ,MS;color:#444}
.en{left:92px;top:800px;font:500 30px CG;font-style:italic;color:#888;width:380px;line-height:1.3}
.list{left:90px;right:90px;top:950px;display:flex;direction:rtl;gap:0}
.li{flex:1;text-align:right;padding:0 26px;border-right:2px solid #B99A5B}
.li b{display:block;font:700 30px TJ,MS}.li i{display:block;font:500 15px MS;font-style:normal;letter-spacing:3px;color:#999;margin-top:6px;direction:ltr;text-align:right}
.bar{left:90px;right:90px;top:1085px;height:120px;background:#B99A5B;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 40px}
.bar .p{font:300 76px MS;letter-spacing:-1px}.bar .p small{font:500 20px MS;letter-spacing:4px;margin-left:12px}
.bar .t{font:700 34px TJ,MS;direction:rtl}
.foot{bottom:40px}.cnr.bl{bottom:30px}
.oo{right:90px;top:1212px}
''',f'''<div class="abs band">{('<div style="margin:0 90px;border:1.5px solid #B99A5B;padding:12px">'+pic(x,874,476)+'</div>') if x.get('photo') else x['scene'](1080,520)}</div>
<div class="abs k"><span class="kick">{deal_en(x)} · {x['area_en'].upper()}</span></div>
<div class="abs h a">{x['ar']}</div>
<div class="abs sub a">{x['type']} {deal_ar(x)} في {x['area']}</div>
<div class="abs en">{x['en']}<br>{x['type_en']}</div>
<div class="abs list"><div class="li"><b class="a">{x['br']}</b><i>{x['br_en'].upper()}</i></div><div class="li"><b>{N(x['size'])}</b><i>SQ FT</i></div><div class="li"><b class="a">{st_ar(x)}</b><i>{st_en(x)}</i></div></div>
<div class="abs bar"><div class="p">{money(x['price'])}<small>{unit_en(x)}</small></div><div class="t">{'الإيجار' if x['deal']=='rent' else 'السعر'}</div></div>
{('<div class="abs oo">'+origline(x)+'</div>') if x.get('orig') else ''}
{foot_adm()}''')

# ---------- layout C: framed card with vertical stripe ----------
def layC(x,fn):
    page(fn,COMMON+'''
.card{left:120px;top:210px;width:840px;height:960px;border:1.5px solid #B99A5B}
.stripe{left:120px;top:210px;width:90px;height:960px;background:#B99A5B}
.vt{left:120px;top:210px;width:90px;height:960px;display:flex;align-items:center;justify-content:center}
.vt span{transform:rotate(-90deg);white-space:nowrap;font:600 26px MS;letter-spacing:12px;color:#fff}
.art{left:220px;top:230px;width:720px;height:347px}
.k{right:160px;top:610px}
.h{right:158px;top:650px;text-align:right;font:800 70px/1.2 TJ,MS}
.sub{right:160px;top:745px;text-align:right;font:500 30px TJ,MS;color:#B99A5B}
.en{right:162px;top:798px;font:500 27px CG;font-style:italic;color:#888}
.rows{left:250px;right:160px;top:860px;direction:rtl}
.r{display:flex;justify-content:space-between;padding:14px 0;border-bottom:1px solid #EFE6D3;font:500 28px TJ,MS;color:#666}
.r b{font:700 28px TJ,MS;color:#111}
.pr{left:250px;top:1055px;font:300 84px/1 MS;letter-spacing:-2px;direction:ltr}
.pu{left:254px;top:1145px;font:500 17px MS;letter-spacing:4px;color:#B99A5B;background:#fff;padding:0 8px}
.oo{right:160px;top:1075px}
''',f'''<div class="abs card"></div><div class="abs stripe"></div><div class="abs vt"><span>{deal_en(x)}</span></div>
<div class="abs art">{pic(x,720,360) if x.get('photo') else x['scene'](720,347).replace('width="720" height="347" viewBox="0 0 720 347"','width="720" height="347" viewBox="0 0 1080 520"')}</div>
<div class="abs k"><span class="kick">{st_en(x)}</span></div>
<div class="abs h a">{x['ar']}</div>
<div class="abs sub a">{x['type']} {deal_ar(x)} · {x['area']}</div>
<div class="abs en">{x['en']}, {x['area_en']}</div>
<div class="abs rows"><div class="r"><span>النوع</span><b>{x['br']}</b></div><div class="r"><span>المساحة</span><b>{N(x['size'])} قدم مربع</b></div></div>
<div class="abs pr">{money(x['price'])}</div><div class="abs pu">{unit_en(x)}</div>
{('<div class="abs oo">'+origline(x)+'</div>') if x.get('orig') else ''}
{foot_adm()}''')

def tall_scene(x,w=480,h=760):
    b=h-60
    body=DEFS+sun(w*0.55,b-430,230)
    if x['type']=='بناية كاملة':
        body+=midrise(110,b,260,420,5)+palm(70,b,150,1)+palm(420,b,130,-1)
    else:
        body+=tower(150,b,130,600,1)+midrise(300,b,120,260,3)+palm(70,b,150,1)+tree(440,b,90,32)
    body+=f'<path d="M20 {b} L{w-20} {b}"/>'+(f'<path d="M80 {b+28} L{w-80} {b+28}" stroke="{L}" stroke-width="1.4"/>' if x['type']=='بناية كاملة' else water(b+24,w,3))
    return _svg(w,h,body)

# ---------- layout D: spec sheet left + tall drawing right ----------
def layD(x,fn):
    page(fn,COMMON+'''
.art{right:0;top:300px;width:480px;height:760px;overflow:hidden}
.vline{left:580px;top:300px;width:1px;height:760px;background:#E6DAC0}
.k{right:90px;top:215px}
.h{left:90px;top:300px;width:450px;text-align:right;font:800 64px/1.2 TJ,MS;direction:rtl}
.sub{left:90px;top:470px;width:450px;text-align:right;font:500 28px TJ,MS;color:#B99A5B;direction:rtl}
.rows{left:90px;width:450px;top:560px;direction:rtl}
.r{padding:16px 0;border-bottom:1px solid #EFE6D3;text-align:right}
.r i{display:block;font:500 14px MS;font-style:normal;letter-spacing:4px;color:#aaa;direction:ltr;text-align:right}
.r b{display:block;font:700 34px TJ,MS;margin-top:4px}
.prw{left:90px;right:90px;top:1090px;border-top:1.5px solid #111;padding-top:18px;display:flex;justify-content:space-between;align-items:baseline}
.pr{font:300 96px/1 MS;letter-spacing:-2px}.pr small{font:500 20px MS;letter-spacing:4px;color:#B99A5B;margin-left:12px}
.pt{font:700 32px TJ,MS;direction:rtl}
.oo{left:90px;top:1210px}
.foot{bottom:50px}
''',f'''<div class="abs art">{pic(x,480,760,'70% center') if x.get('photo') else tall_scene(x)}</div><div class="abs vline"></div>
<div class="abs k"><span class="kick">{deal_en(x)} · {st_en(x)}</span></div>
<div class="abs h">{x['ar']}</div>
<div class="abs sub">{x['area']} · {x['area_en']}</div>
<div class="abs rows">
<div class="r"><i>TYPE</i><b class="a">{x['type']}</b></div>
{'' if x['br']==x['type'] else '<div class="r"><i>LAYOUT</i><b class="a">'+x['br']+'</b></div>'}
<div class="r"><i>SIZE</i><b>{N(x['size'])} <span class="a" style="font-weight:500;font-size:26px">قدم مربع</span></b></div>
<div class="r"><i>STATUS</i><b class="a">{st_ar(x)}</b></div></div>
<div class="abs prw"><div class="pr">{money(x['price'])}<small>{unit_en(x)}</small></div><div class="pt">{'الإيجار السنوي' if x['deal']=='rent' else 'السعر'}</div></div>
{('<div class="abs oo">'+origline(x)+'</div>') if x.get('orig') else ''}
{foot_adm()}''')

# ---------- stories ----------
def stA(x,fn):
    page(fn,COMMON+'''
.pill2{right:90px;top:330px}
.h{right:90px;top:420px;text-align:right;font:800 104px/1.15 TJ,MS}
.sub{right:90px;top:560px;text-align:right;font:500 40px TJ,MS;color:#444}
.art{left:0;top:700px;width:1080px;height:520px}
.pr{left:0;right:0;top:1290px;text-align:center;font:300 150px/1 MS;letter-spacing:-3px}
.pu{left:0;right:0;top:1450px;text-align:center;font:500 24px MS;letter-spacing:6px;color:#B99A5B}
.sp{left:0;right:0;top:1520px;text-align:center;font:500 34px TJ,MS;color:#555;direction:rtl}
.cw{left:0;right:0;top:1620px;text-align:center}
.foot{bottom:90px}.cnr.bl{bottom:70px}
''',f'''<div class="abs pill2"><span class="pill">{deal_ar(x)} · {st_ar(x)}</span></div>
<div class="abs h a">{x['ar']}</div>
<div class="abs sub a">{x['type']} في {x['area']}</div>
<div class="abs art">{('<div style="margin:0 90px;border:1.5px solid #B99A5B;padding:12px">'+pic(x,874,470)+'</div>') if x.get('photo') else x['scene'](1080,520)}</div>
<div class="abs pr">{money(x['price'])}</div><div class="abs pu">{unit_en(x)}</div>
<div class="abs sp">{x['br']} · {N(x['size'])} قدم مربع</div>
<div class="abs cw"><span class="cta">راسلنا للتفاصيل<i>DM US</i></span></div>
{foot_adm()}''',story=True)

def stB(x,fn):
    tag=_svg(420,760,keytag(210,400,300,560,'',''))
    page(fn,COMMON+'''
.k{right:90px;top:300px}
.h{right:90px;top:345px;text-align:right;font:800 92px/1.2 TJ,MS}
.sub{right:90px;top:470px;text-align:right;font:500 38px TJ,MS;color:#B99A5B}
.tagtxt{left:330px;top:900px;width:420px;text-align:center}
.tagtxt b{display:block;font:300 58px/1 MS;letter-spacing:-2px}.tagtxt i{display:block;font:500 18px MS;font-style:normal;letter-spacing:5px;color:#B99A5B;margin-top:12px}
.tagtxt span{display:block;font:700 30px TJ,MS;margin-top:28px;direction:rtl}
.mini{left:0;top:1340px;width:1080px;height:260px;opacity:.9}
.cw{left:0;right:0;top:1640px;text-align:center}
.foot{bottom:90px}.cnr.bl{bottom:70px}
.tg{position:absolute}
''',f'''<div class="abs k"><span class="kick">NEW LISTING · {x['area_en'].upper()}</span></div>
<div class="abs h a">{x['ar']}</div>
<div class="abs sub a">{x['type']} {deal_ar(x)} · {st_ar(x)}</div>
<div class="tg" style="left:330px;top:560px">{tag}</div>
<div class="abs tagtxt"><b>{money(x['price'])}</b><i>{unit_en(x)}</i><span>{x['br']}</span><span style="font:500 26px MS;margin-top:10px;direction:ltr">{x['size']} SQ FT</span></div>
<div class="abs mini">{('<div style="margin:0 90px">'+pic(x,900,260)+'</div>') if x.get('photo') else x['scene'](1080,520).replace('width="1080" height="520"','width="1080" height="260"')}</div>
<div class="abs cw"><span class="cta">تبي تشوفه؟ راسلنا<i>DM US</i></span></div>
{foot_adm()}''',story=True)

LAYS=[layA,layB,layC,layD]; STS=[stA,stB]
if __name__=='__main__':
    import subprocess
    for i,x in enumerate(L):
        LAYS[i%4](x,f'L{i+1:02d}.html'); STS[i%2](x,f'S{i+1:02d}.html')
