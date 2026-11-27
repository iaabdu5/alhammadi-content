from v4 import *
from art import _svg
import calendar
SRCH='Sources: The National · Khaleej Times · Gulf News (13 Nov 2026), MoHRE / FAHR announcement'
SRCU='Source: ADREC figures via Gulf News & Khaleej Times (Nov 2026)'
GEN='General guidance, not financial advice · Livana'

# ---------- A1: Eid Al Etihad 55 cover — flag on pole left, giant outlined 55 ----------
page('a1.html','''
.fl{left:70px;top:260px}
.k{right:90px;top:230px}
.h{right:90px;top:275px;text-align:right;font:800 86px/1.2 TJ,MS}.h span{color:#B99A5B}
.n55{right:70px;top:500px;font:300 400px/1 MS;color:#B99A5B;letter-spacing:-4px}
.yr{right:96px;top:910px;font:500 18px MS;letter-spacing:7px;color:#999}
.sub{right:90px;left:560px;top:980px;text-align:right;font:500 32px/1.55 TJ,MS;color:#444;direction:rtl}
.en{right:92px;top:1170px;font:500 28px CG;font-style:italic;color:#888}
''','''<div class="abs fl">'''+_svg(520,960,DEFS+sun(260,330,240)+flag_wave(60,930,250,190,560)+water(950,520,2))+'''</div>
<div class="abs k"><span class="kick">EID AL ETIHAD · عيد الاتحاد</span></div>
<div class="abs h a">كل عام<br><span>والإمارات بخير</span></div>
<div class="abs n55">55</div>
<div class="abs yr">1971 — 2026</div>
<div class="abs sub a">إجازة طويلة جاية. هذي تواريخها، وكيف تستغلها لو تدوّر بيت</div>
<div class="abs en">The 55th Eid Al Etihad long weekend</div>
<div class="src">'''+SRCH+'''</div>''')

# ---------- A2: December calendar grid with holiday days ----------
weeks=calendar.Calendar(0).monthdayscalendar(2026,12)
cells=''
for wk in weeks:
    for d in wk:
        cls='' if d==0 else (' pub' if d in (2,3) else (' fri' if d==4 else (' we' if d in (5,6) else '')))
        cells+=f'<div class="c{cls}">{d if d else ""}</div>'
hd=''.join(f'<div class="hd">{x}</div>' for x in ['MON','TUE','WED','THU','FRI','SAT','SUN'])
page('a2.html','''
.k{right:90px;top:200px}
.h{right:90px;top:240px;text-align:right;font:800 74px/1.2 TJ,MS}.h span{color:#B99A5B}
.mo{left:90px;top:252px;font:300 64px/1 MS;letter-spacing:10px}.mo i{display:block;font:500 16px MS;font-style:normal;letter-spacing:6px;color:#B99A5B;margin-top:14px}
.cal{left:90px;right:90px;top:470px;display:grid;grid-template-columns:repeat(7,1fr);gap:10px}
.hd{text-align:center;font:600 15px MS;letter-spacing:3px;color:#999;padding-bottom:10px;border-bottom:1px solid #E6DAC0}
.c{height:92px;display:flex;align-items:center;justify-content:center;font:300 40px MS;color:#333}
.c.pub,.c.fri{position:relative;color:#fff}
.c.pub:before,.c.fri:before{content:"";position:absolute;width:80px;height:80px;border-radius:50%;background:#B99A5B;z-index:-1}
.c.fri{color:#B99A5B}.c.fri:before{background:#fff;border:2.5px solid #B99A5B;box-sizing:border-box}
.c.we{color:#B99A5B}
.lg{left:90px;right:90px;top:1020px;direction:rtl;display:flex;flex-direction:column;gap:22px}
.r{display:flex;align-items:center;gap:22px;font:700 30px/1.4 TJ,MS}.r small{font:500 24px TJ,MS;color:#777;margin-right:10px}
.dot{flex:none;width:34px;height:34px;border-radius:50%;background:#B99A5B}.dot.o{background:#fff;border:2.5px solid #B99A5B}
''','''<div class="abs k"><span class="kick">HOLIDAY DATES · التواريخ</span></div>
<div class="abs h a">إجازة<br><span>عيد الاتحاد</span></div>
<div class="abs mo">DEC<i>2026</i></div>
<div class="abs cal">'''+hd+cells+'''</div>
<div class="abs lg">
<div class="r"><span class="dot"></span><span class="a">الأربعاء والخميس <span dir="ltr">2–3</span> ديسمبر <small>إجازة للقطاعين العام والخاص</small></span></div>
<div class="r"><span class="dot o"></span><span class="a">الجمعة <span dir="ltr">4</span> ديسمبر <small>إجازة للقطاع الحكومي، والدوام يرجع الاثنين <span dir="ltr">7</span></small></span></div>
</div>
<div class="src">'''+SRCH+'''</div>''')

# ---------- A3: 5 tear-off calendar leaves = 5-day plan ----------
def leaf(n,d,a):
    return f'''<div class="lf"><div class="ic">{_svg(130,130,calendar_leaf(15,26,100,96,2))}<span class="dn">{n}</span><span class="dd">{d}</span></div><div class="tx a">{a}</div></div>'''
page('a3.html','''
.k{left:0;right:0;top:200px;text-align:center}
.h{left:0;right:0;top:240px;text-align:center;font:800 76px/1.2 TJ,MS}.h span{color:#B99A5B}
.list{left:110px;right:110px;top:470px;direction:rtl}
.lf{display:flex;align-items:center;gap:34px;height:132px;border-bottom:1px solid #EFE6D4}
.ic{position:relative;flex:none;width:130px;height:130px;direction:ltr}
.dn{position:absolute;left:0;width:130px;top:62px;text-align:center;font:300 40px MS}
.dd{position:absolute;left:0;width:130px;top:32px;text-align:center;font:600 11px MS;letter-spacing:2px;color:#B99A5B}
.tx{font:700 33px/1.4 TJ,MS}.tx small{display:block;font:500 23px TJ,MS;color:#777}
.cta{left:0;right:0;top:1170px;text-align:center}
''','''<div class="abs k"><span class="kick">LONG WEEKEND PLAN · خطة الإجازة</span></div>
<div class="abs h a">تدوّر بيت؟<br><span>استغل الإجازة</span></div>
<div class="abs list">'''+leaf(2,'WED','احتفل مع أهلك<small>اليوم للعيد والعائلة</small>')+leaf(3,'THU','زور المجتمع اللي في بالك<small>شوف الحركة والخدمات بنفسك</small>')+leaf(4,'FRI','جرّب مشوارك اليومي<small>المسافة للمدارس والدوام وقت الذروة</small>')+leaf(5,'SAT','رتّب أوراقك<small>الهوية، كشف الراتب، والموافقة المبدئية</small>')+leaf(6,'SUN','احجز معاينة<small>وقارن الخيارات مع مستشار</small>')+'''</div>
<div class="abs cta"><span class="pill a">نرتب لك جولة معاينات، راسلنا ←</span></div>
<div class="src">'''+GEN+'''</div>''')

# ---------- B1: Friday quiz cover — signpost ----------
boards=((1,0),(-1,1),(1,2),(-1,3))
lab=[('A','شاطئ ومتحف'),('B','ملاهي وفعاليات'),('C','مقهى وسط المدينة'),('D','ممشى على البحر')]
def bl(i,d,row,X=540,Y=1230,H=860,bw=300,bh=86):
    by=Y-H+60+row*(bh+44); x0=X+20 if d>0 else X-bw
    return f'<div class="bl" style="left:{x0}px;top:{by}px;width:{bw-20}px;height:{bh}px"><b>{lab[i][0]}</b><span class="a">{lab[i][1]}</span></div>'
page('b1.html','''
.k{left:0;right:0;top:195px;text-align:center}
.h{left:0;right:0;top:235px;text-align:center;font:800 78px/1.2 TJ,MS}.h span{color:#B99A5B}
.sp{left:0;top:0}
.bl{position:absolute;display:flex;align-items:center;gap:14px;padding:0 18px;direction:rtl}
.bl b{font:300 42px MS;color:#B99A5B}.bl span{font:700 23px TJ,MS;white-space:nowrap}
.q{left:0;right:0;top:1075px;text-align:center;font:500 31px/1.5 TJ,MS;color:#444;direction:rtl}
.en{left:0;right:0;top:1135px;text-align:center;font:500 26px CG;font-style:italic;color:#888}
''','''<div class="abs sp">'''+_svg(1080,1350,DEFS+sun(540,760,300)+signpost(540,1030,600,boards,300,86)) +'''</div>
<div class="abs k"><span class="kick">FRIDAY QUIZ · سؤال الجمعة</span></div>
<div class="abs h a">ويكندك المثالي<br><span>وين يكون؟</span></div>
'''+''.join(bl(i,d,r,540,1030,600) for i,(d,r) in enumerate(boards))+'''
<div class="abs q a">اختار حرفك، وشوف أي منطقة تناسبك في السلايد الجاية</div>
<div class="abs en">Pick a letter, swipe for your Abu Dhabi match</div>''')

# ---------- B2: answers — 4 rows with mini drawings ----------
def mini(kind):
    if kind=='A': return _svg(200,120,louvre(10,100,180)+water(108,200,1),)
    if kind=='B': return _svg(200,120,gridshell(10,104,180,70))
    if kind=='C': return _svg(200,120,tower(40,110,34,90)+tower(84,110,40,104,1)+tower(134,110,30,70))
    return _svg(200,120,dhow(30,92,0.9)+water(104,200,1))
def ans(k,a,e,t):
    return f'<div class="an"><div class="lt">{k}</div><div class="tx"><div class="ar a">{a}</div><div class="e">{e}</div><div class="t a">{t}</div></div><div class="mi">{mini(k)}</div></div>'
page('b2.html','''
.k{right:90px;top:200px}
.h{right:90px;top:240px;text-align:right;font:800 74px/1.2 TJ,MS}.h span{color:#B99A5B}
.list{left:80px;right:80px;top:470px}
.an{display:flex;align-items:center;gap:30px;height:178px;border-bottom:1px solid #EFE6D4;flex-direction:row-reverse}
.lt{flex:none;width:96px;height:96px;border:1.5px solid #B99A5B;border-radius:50%;display:flex;align-items:center;justify-content:center;font:300 50px MS;color:#B99A5B}
.tx{flex:1;text-align:right}
.ar{font:800 38px TJ,MS}.e{font:500 14px MS;letter-spacing:3px;color:#B99A5B;margin-top:2px}
.t{font:500 25px/1.45 TJ,MS;color:#555;margin-top:6px}
.mi{flex:none;width:200px}
''','''<div class="abs k"><span class="kick">YOUR MATCH · نتيجتك</span></div>
<div class="abs h a">حرفك يقول<br><span>تسكن هنا</span></div>
<div class="abs list">'''+ans('A','السعديات','SAADIYAT ISLAND','شواطئ، والمنطقة الثقافية: اللوفر وغوغنهايم')+ans('B','جزيرة ياس','YAS ISLAND','ملاهي، حلبة ياس مارينا، وفعاليات طول السنة')+ans('C','جزيرة الريم','AL REEM ISLAND','أبراج سكنية قريبة من قلب المدينة')+ans('D','شاطئ الراحة','AL RAHA BEACH','واجهة بحرية وممشى، وقريبة من المطار')+'''</div>
<div class="src">Light Friday quiz · Livana</div>''')

# ---------- B3: comment CTA — four big letters ----------
page('b3.html','''
.k{left:0;right:0;top:260px;text-align:center}
.h{left:0;right:0;top:305px;text-align:center;font:800 84px/1.25 TJ,MS}.h span{color:#B99A5B}
.row{left:120px;right:120px;top:580px;display:flex;justify-content:space-between}
.L{width:180px;height:180px;border:1.5px solid #B99A5B;border-radius:50%;display:flex;align-items:center;justify-content:center;font:300 96px MS;color:#B99A5B}
.L.on{background:#B99A5B;color:#fff}
.s{left:130px;right:130px;top:860px;text-align:center;font:500 34px/1.6 TJ,MS;color:#444;direction:rtl}
.cta{left:0;right:0;top:1060px;text-align:center}
''','''<div class="abs k"><span class="kick">YOUR TURN · دورك</span></div>
<div class="abs h a">علّق بحرفك<br><span>ونرشّح لك</span></div>
<div class="abs row"><div class="L">A</div><div class="L on">B</div><div class="L">C</div><div class="L">D</div></div>
<div class="abs s a">قول لنا حرفك في التعليقات، ونرسل لك مشاريع تناسب أسلوب حياتك في نفس المنطقة</div>
<div class="abs cta"><span class="pill a">أو راسلنا مباشرة ←</span></div>''')

# ================= STORIES =================
# T1 09:30 Jumu'ah — hanging lanterns
art=_svg(1080,1100,DEFS+sun(540,560,360)+lantern(300,0,0.95,330)+lantern(540,0,1.25,120)+lantern(800,0,0.85,420)+crescent(880,200,58)+star4(200,240,18)+star4(700,330,12)+star4(420,520,10))
page('t1.html','''
.art{left:0;top:180px}
.k{left:0;right:0;top:1230px;text-align:center}
.h{left:0;right:0;top:1280px;text-align:center;font:800 120px/1.2 TJ,MS;color:#B99A5B}
.en{left:0;right:0;top:1440px;text-align:center;font:500 36px CG;font-style:italic;color:#888}
.d{left:130px;right:130px;top:1530px;text-align:center;font:500 40px/1.65 TJ,MS;color:#333;direction:rtl}
.foot{bottom:90px}''','''<div class="abs art">'''+art+'''</div>
<div class="abs k"><span class="kick">FRIDAY · الجمعة</span></div>
<div class="abs h a">جمعة مباركة</div>
<div class="abs en">Jumu'ah Mubarak</div>
<div class="abs d a">اللهم اجعل هذه الجمعة خيراً وبركةً لنا ولأهلنا</div>''',story=True)

# T2 09:30 word of the day — file folder card with tab
page('t2.html','''
.k{left:0;right:0;top:270px;text-align:center}
.fd{left:110px;right:110px;top:470px;height:1080px;border:2px solid #C9AE77;border-radius:0 28px 28px 28px;background:#fff}
.tb{left:110px;top:400px;width:380px;height:72px;border:2px solid #C9AE77;border-bottom:none;border-radius:24px 24px 0 0;background:#FBF6EA;display:flex;align-items:center;justify-content:center;font:600 18px MS;letter-spacing:5px;color:#B99A5B}
.in{left:170px;right:170px;text-align:right}
.st{right:160px;top:540px}
.foot{bottom:90px}''','''<div class="abs k"><span class="kick">WORD OF THE DAY · مصطلح اليوم</span></div>
<div class="abs tb">FILE · 27.11</div><div class="abs fd"></div>
<div class="abs in a" style="top:600px;font:800 96px/1.2 TJ,MS">موافقة<br><span class="gold">مبدئية</span></div>
<div class="abs in" style="top:860px;font:300 30px/1.5 MS;letter-spacing:7px;color:#B99A5B">MORTGAGE<br>PRE-APPROVAL</div>
<div class="abs in" style="top:990px"><div class="hl"></div></div>
<div class="abs in a" style="top:1040px;font:500 40px/1.65 TJ,MS;color:#444">موافقة أولية من البنك توضّح كم تقدر تقترض تقريباً، قبل ما تختار العقار. تخلّيك تفاوض وأنت عارف ميزانيتك.</div>
<div class="abs in a" style="top:1420px;font:500 26px/1.5 TJ,MS;color:#999">معلومة عامة، والشروط تختلف من بنك لبنك</div>''',story=True)

# T3 12:30 teaser post 1 — big tear-off calendar "2 DEC"
page('t3.html','''
.k{left:0;right:0;top:280px;text-align:center}
.h{left:0;right:0;top:340px;text-align:center;font:800 96px/1.2 TJ,MS}.h span{color:#B99A5B}
.cl{left:240px;top:640px}
.m{left:240px;width:600px;top:720px;text-align:center;font:600 34px MS;letter-spacing:12px;color:#B99A5B}
.d{left:240px;width:600px;top:830px;text-align:center;font:300 330px/1 MS}
.s{left:120px;right:120px;top:1330px;text-align:center;font:500 42px/1.6 TJ,MS;color:#555;direction:rtl}
.cta{left:0;right:0;top:1560px;text-align:center}
.foot{display:none}''','''<div class="abs k"><span class="kick">NEW POST · منشور جديد</span></div>
<div class="abs h a">إجازة<br><span>عيد الاتحاد</span></div>
<div class="abs cl">'''+_svg(600,640,calendar_leaf(10,40,580,580,3))+'''</div>
<div class="abs m">DECEMBER</div><div class="abs d">2</div>
<div class="abs s a">التواريخ للقطاعين، وخطة خمس أيام لو تدوّر بيت. في منشورنا الحين</div>
<div class="abs cta"><span class="pill a">شوف المنشور ←</span></div>''',story=True,foot=False)

# T4 16:30 did you know — unit grid (1 square = 10,000 homes)
sq=''.join(f'<div class="q{" f" if i>=41 else ""}"></div>' for i in range(48))
page('t4.html','''
.k{right:100px;top:290px}
.h{right:100px;top:345px;text-align:right;font:800 88px/1.2 TJ,MS}.h span{color:#B99A5B}
.g{left:120px;right:120px;top:620px;display:grid;grid-template-columns:repeat(8,1fr);gap:18px}
.q{aspect-ratio:1;border:2px solid #C9AE77;border-radius:10px}.q.f{background:#B99A5B;border-color:#B99A5B}
.r{left:120px;right:120px;display:flex;justify-content:space-between;align-items:baseline;direction:rtl}
.r b{font:300 96px/1 MS;direction:ltr}.r span{font:700 36px/1.4 TJ,MS}
.key{left:120px;right:120px;top:1650px;text-align:right;font:500 26px TJ,MS;color:#999;direction:rtl}
.foot{bottom:90px}''','''<div class="abs k"><span class="kick">DID YOU KNOW · هل تعرف؟</span></div>
<div class="abs h a">كم بيت<br><span>في أبوظبي؟</span></div>
<div class="abs g">'''+sq+'''</div>
<div class="abs r" style="top:1330px"><span class="a">وحدة سكنية تقريباً اليوم</span><b>409,000</b></div>
<div class="abs r" style="top:1470px"><span class="a gold">وحدة إضافية متوقعة بحلول <span dir="ltr">2030</span></span><b class="gold">+71,000</b></div>
<div class="abs key a">كل مربع ≈ <span dir="ltr">10,000</span> وحدة</div>
<div class="src" style="bottom:40px">'''+SRCU+'''</div>''',story=True)

# T5 16:30 checklist — pinned note card with folded corner
def ck(a): return f'<div class="ci"><span class="o"></span><span class="a">{a}</span></div>'
page('t5.html','''
.k{left:0;right:0;top:270px;text-align:center}
.h{left:0;right:0;top:320px;text-align:center;font:800 86px/1.2 TJ,MS}.h span{color:#B99A5B}
.nt{left:150px;right:150px;top:640px;height:1000px;background:#FBF6EA;border:2px solid #C9AE77;transform:rotate(2deg);padding:120px 60px 0}
.fold{left:792px;top:1515px;width:120px;height:120px;border-left:2px solid #C9AE77;border-top:2px solid #C9AE77;background:#fff;transform:rotate(2deg)}
.pin{left:500px;top:600px}
.ci{display:flex;gap:28px;align-items:center;height:180px;border-bottom:1px dashed #D9C7A0;direction:rtl;font:700 40px/1.35 TJ,MS}
.o{flex:none;width:50px;height:50px;border:2px solid #B99A5B;border-radius:8px;background:#fff}
.foot{bottom:90px}''','''<div class="abs k"><span class="kick">CHECKLIST · قائمة تحقق</span></div>
<div class="abs h a">رايح معاينة؟<br><span>خذ معك</span></div>
<div class="abs nt">'''+ck('قائمة أسئلة عن رسوم الخدمة')+ck('صورة الهوية أو الجواز')+ck('متر قياس وجوالك للصور')+ck('ميزانيتك والموافقة المبدئية')+'''</div>

<div class="abs pin">'''+_svg(80,90,pushpin(40,30,1.4))+'''</div>''',story=True)

# T6 19:30 teaser post 2 — signpost question
boards6=((1,0),(-1,1),(1,2),(-1,3))
def bl6(i,d,row,X=540,Y=1400,H=900,bw=300,bh=100):
    by=Y-H+60+row*(bh+44); x0=X+20 if d>0 else X-bw
    return f'<div class="bl" style="left:{x0}px;top:{by}px;width:{bw-20}px;height:{bh}px"><b>{lab[i][0]}</b></div>'
page('t6.html','''
.k{left:0;right:0;top:270px;text-align:center}
.h{left:0;right:0;top:320px;text-align:center;font:800 96px/1.2 TJ,MS}.h span{color:#B99A5B}
.sp{left:0;top:0}
.bl{position:absolute;display:flex;align-items:center;justify-content:center}
.bl b{font:300 60px MS;color:#B99A5B}
.s{left:120px;right:120px;top:1480px;text-align:center;font:500 42px/1.6 TJ,MS;color:#555;direction:rtl}
.cta{left:0;right:0;top:1690px;text-align:center}
.foot{display:none}''','''<div class="abs sp">'''+_svg(1080,1920,DEFS+sun(540,1000,320)+signpost(540,1400,900,boards6,300,100))+'''</div>
<div class="abs k"><span class="kick">NEW POST · منشور جديد</span></div>
<div class="abs h a">أي حرف<br><span>يشبهك؟</span></div>
'''+''.join(bl6(i,d,r) for i,(d,r) in enumerate(boards6))+'''
<div class="abs s a">سؤال الجمعة نزل الحين. جاوب واعرف أي منطقة تناسبك</div>
<div class="abs cta"><span class="pill a">جاوب الحين ←</span></div>''',story=True,foot=False)
