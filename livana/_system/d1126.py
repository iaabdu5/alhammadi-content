from v4 import *
from art import _svg
SRCG='Sources: DCT Abu Dhabi announcement · The National (28 Jul 2026) · Gulf News'
SRCN="Sources: Boutique Hotel News (23 Nov 2026) · Spear's (25 Nov 2026)"
GEN='General guidance, not financial advice · Livana'

# ---------- G1: cover — date + Guggenheim drawing ----------
page('g1.html','''
.k{right:90px;top:210px}
.h{right:90px;top:252px;text-align:right;font:800 88px/1.18 TJ,MS}.h span{color:#B99A5B}
.dt{left:90px;top:470px;font:300 112px/1 MS;letter-spacing:6px;direction:ltr}.dt i{font-style:normal;color:#B99A5B}
.dl{left:94px;top:600px;font:500 17px MS;letter-spacing:6px;color:#999}
.art{left:0;top:650px}
.sub{left:110px;right:110px;top:1150px;text-align:center;font:500 31px/1.5 TJ,MS;color:#444;direction:rtl}
.en{left:0;right:0;top:1212px;text-align:center;font:500 27px CG;font-style:italic;color:#888}
''','''<div class="abs k"><span class="kick">SAADIYAT CULTURAL DISTRICT</span></div>
<div class="abs h a">غوغنهايم أبوظبي<br><span>يفتح أبوابه</span></div>
<div class="abs dt">11<i>.</i>12<i>.</i>26</div><div class="abs dl">OPENING DAY · يوم الافتتاح</div>
<div class="abs art">'''+guggenheim_scene(1080,500)+'''</div>
<div class="abs sub a">من تصميم فرانك غيري، في المنطقة الثقافية بجزيرة السعديات</div>
<div class="abs en">Guggenheim Abu Dhabi opens on 11 December 2026</div>
<div class="src">'''+SRCG+'''</div>''')

# ---------- G2: numbers beside a height ruler ----------
def nr(v,u,a,e): return f'<div class="nr"><div class="v">{v}<small>{u}</small></div><div class="t a">{a}</div><div class="e">{e}</div></div>'
def mkcone(H,base,top):
    return _svg(260,H,f'<path d="M95 {base} L40 {top} A85 22 0 0 1 210 {top} L165 {base} Z" fill="#fff"/><ellipse cx="125" cy="{top}" rx="85" ry="22"/><path d="M118 {base} L95 {top+20} M142 {base} L155 {top+20}" stroke="#D9C7A0" stroke-width="1.2"/><path d="M0 {base} L260 {base}"/>')
cone=mkcone(900,880,40)
page('g2.html','''
.k{right:90px;top:200px}
.h{right:90px;top:240px;text-align:right;font:800 74px/1.2 TJ,MS}.h span{color:#B99A5B}
.rl{left:70px;top:290px}.cn{left:150px;top:290px}
.m{left:130px;font:600 20px MS;color:#B99A5B;letter-spacing:2px}
.list{left:440px;right:90px;top:480px}
.nr{padding:34px 0;border-bottom:1px solid #EFE6D4;text-align:right}
.v{font:300 92px/1 MS;direction:ltr}.v small{font:400 30px MS;color:#B99A5B;margin-left:10px}
.t{font:700 32px/1.4 TJ,MS;margin-top:10px}.e{font:500 14px MS;letter-spacing:2.5px;color:#999;margin-top:4px}
''','''<div class="abs k"><span class="kick">BY THE NUMBERS · بالأرقام</span></div>
<div class="abs h a">متحف<br><span>بحجم مدينة</span></div>
<div class="abs rl">'''+_svg(60,900,height_scale(4,880,840,88))+'''</div>
<div class="abs cn">'''+cone+'''</div>
<div class="abs m" style="top:316px">88 M</div><div class="abs m" style="top:1160px">0</div>
<div class="abs list">'''+nr('80,000','m²','مساحة البناء الإجمالية','TOTAL BUILT-UP AREA')+nr('11,600','m²','مساحات عرض داخلية','INDOOR GALLERY SPACE')+nr('10','×','مخاريط يوصل ارتفاعها إلى <span dir="ltr">88</span> متر','SCULPTURAL CONES, UP TO 88 M')+'''</div>
<div class="src">'''+SRCG+''' · Illustration not to scale</div>''')

# ---------- G3: district map with pins + legend ----------
pins=[(150,300,0),(330,250,0),(520,230,0),(700,290,0),(430,360,1)]
def lg(n,a,e,big=False): return f'<div class="lg{" b" if big else ""}"><span class="n">{n}</span><span class="a">{a}</span><span class="e">{e}</span></div>'
page('g3.html','''
.k{left:0;right:0;top:195px;text-align:center}
.h{left:0;right:0;top:236px;text-align:center;font:800 76px/1.2 TJ,MS}.h span{color:#B99A5B}
.map{left:90px;top:400px}
.pl{position:absolute;font:600 30px MS;color:#B99A5B;width:40px;text-align:center}
.leg{left:100px;right:100px;top:930px;display:grid;grid-template-columns:1fr 1fr;gap:6px 50px;direction:rtl}
.lg{display:flex;align-items:baseline;gap:14px;padding:12px 0;border-bottom:1px solid #EFE6D4}
.lg .n{font:300 34px MS;color:#B99A5B;width:36px}.lg .a{font:700 27px TJ,MS}.lg .e{display:none}
.lg.b .a{color:#B99A5B}
.note{left:100px;right:100px;top:1185px;text-align:center;font:500 26px/1.5 TJ,MS;color:#555;direction:rtl}
''','''<div class="abs k"><span class="kick">NEIGHBOURS · جيران في حي واحد</span></div>
<div class="abs h a">المنطقة الثقافية<br><span>تكتمل</span></div>
<div class="abs map">'''+district_map(900,500,pins)+'''</div>
'''+''.join(f'<div class="pl" style="left:{90+x-20}px;top:{400+y-56}px">{i+1}</div>' for i,(x,y,_) in enumerate(pins))+'''
<div class="abs leg">'''+lg(1,'متحف اللوفر أبوظبي','')+lg(2,'متحف زايد الوطني','')+lg(3,'متحف التاريخ الطبيعي','')+lg(4,'تيم لاب فينومينا','')+lg(5,'غوغنهايم أبوظبي','',True)+'''</div>
<div class="abs note a">وقريب منها حي <span dir="ltr">NOMA</span> الإبداعي الجديد من الدار، شمال منارة السعديات</div>
<div class="src">'''+SRCG+''' · Boutique Hotel News · Map illustrative, not to scale</div>''')

# ---------- G4: three columns of questions + CTA ----------
def col(n,a,e): return f'<div class="cl"><div class="n">{n}</div><div class="t a">{a}</div><div class="e">{e}</div></div>'
page('g4.html','''
.k{right:90px;top:210px}
.h{right:90px;top:250px;text-align:right;font:800 78px/1.2 TJ,MS}.h span{color:#B99A5B}
.cols{left:80px;right:80px;top:470px;display:flex;direction:rtl}
.cl{flex:1;padding:0 30px;border-left:1px solid #E6DAC0;text-align:center}.cl:last-child{border-left:none}
.n{font:300 120px/1 MS;color:#B99A5B}
.t{font:700 32px/1.45 TJ,MS;margin-top:30px;min-height:190px}
.e{font:500 13px MS;letter-spacing:2px;color:#999;margin-top:14px}
.cta{left:0;right:0;top:900px;text-align:center}
.art{left:0;top:990px}
''','''<div class="abs art">'''+louvre_scene(1080,270)+'''</div><div class="abs k"><span class="kick">LIVING NEARBY · تبي تسكن قريب؟</span></div>
<div class="abs h a">قبل ما تختار<br><span>بيتك في السعديات</span></div>
<div class="abs cols">'''+col('1','المسافة الفعلية عن المتاحف والشاطئ','REAL DISTANCE')+col('2','الزحمة وقت الفعاليات والمواسم','EVENT-DAY TRAFFIC')+col('3','رسوم الخدمة ومرافق المجتمع','SERVICE CHARGES')+'''</div>
<div class="abs cta"><span class="pill a">نساعدك تختار المجتمع المناسب، راسلنا ←</span></div>
<div class="src">'''+GEN+'''</div>''')

# ---------- H1: post 2 — branded residences, key tag ----------
def q(n,a): return f'<div class="q"><span class="n">{n}</span><span class="a">{a}</span></div>'
page('h1.html','''
.k{right:90px;top:200px}
.h{right:90px;top:240px;text-align:right;font:800 72px/1.22 TJ,MS}.h span{color:#B99A5B}
.tag2{left:60px;top:500px}
.tt{left:110px;width:320px;text-align:center}
.news{left:470px;right:90px;top:470px;font:500 28px/1.55 TJ,MS;color:#444;direction:rtl;text-align:right}
.ql{left:470px;right:90px;top:680px;direction:rtl}
.q{display:flex;gap:18px;align-items:baseline;padding:20px 0;border-bottom:1px solid #EFE6D4}
.q .n{font:300 40px MS;color:#B99A5B;width:44px;flex:none}.q .a{font:700 30px/1.4 TJ,MS}
''','''<div class="abs k"><span class="kick">BRANDED RESIDENCES · سكن فندقي</span></div>
<div class="abs h a">بيت باسم فندق؟<br><span>4 أسئلة قبل تشتري</span></div>
<div class="abs tag2">'''+_svg(420,820,keytag(210,470,300,560))+'''</div>
<div class="abs tt" style="top:770px;font:300 34px/1.3 MS;letter-spacing:6px">THE<br>HOXTON<br>HOMES</div>
<div class="abs tt" style="top:950px;font:500 15px MS;letter-spacing:4px;color:#B99A5B">NOMA · SAADIYAT</div>
<div class="abs tt a" style="top:1000px;font:500 22px/1.4 TJ,MS;color:#777">أول مشروع للعلامة<br>في العالم</div>
<div class="abs news">أعلنت <span dir="ltr">Aldar</span> بالشراكة مع <span dir="ltr">Ennismore</span> عن أول فندق <span dir="ltr">Hoxton</span> في أبوظبي، وأول مساكن بعلامة <span dir="ltr">The Hoxton Homes</span> في العالم، داخل حي <span dir="ltr">NOMA</span>.</div>
<div class="abs ql">'''+q('01','مين يدير العقار والخدمات؟')+q('02','رسوم الخدمة كم، وتشمل إيش؟')+q('03','تقدر تؤجّره؟ وفيه برنامج تأجير؟')+q('04','وش الخدمات الفندقية للسكان؟')+'''</div>
<div class="src">'''+SRCN+' · '+GEN+'''</div>''')

# ================= STORIES =================
# S1 09:30 countdown — giant number in a clock ring
import math
ring=''.join(f'<path d="M{450+430*math.cos(2*math.pi*k/60):.1f} {450+430*math.sin(2*math.pi*k/60):.1f} L{450+(430-(30 if k%5==0 else 14))*math.cos(2*math.pi*k/60):.1f} {450+(430-(30 if k%5==0 else 14))*math.sin(2*math.pi*k/60):.1f}" stroke-width="{2.5 if k%5==0 else 1.2}"/>' for k in range(60))
ring+='<circle cx="450" cy="450" r="440" stroke-width="1.5"/><circle cx="450" cy="450" r="370" stroke="#D9C7A0" stroke-width="1.2"/>'
page('s1.html','''
.k{left:0;right:0;top:270px;text-align:center}
.gm{left:0;right:0;top:320px;text-align:center;font:800 74px TJ,MS}
.rg{left:90px;top:440px}
.big{left:0;right:0;top:620px;text-align:center;font:300 330px/1 MS}
.dy{left:0;right:0;top:960px;text-align:center;font:700 54px TJ,MS;color:#B99A5B}
.art{left:0;top:1430px}
.s{left:100px;right:100px;top:1290px;text-align:center;font:700 46px/1.4 TJ,MS;direction:rtl}
.foot{bottom:90px}''','''<div class="abs k"><span class="kick">GOOD MORNING · صباح الخير</span></div>
<div class="abs gm a">باقي على الافتتاح</div>
<div class="abs rg">'''+_svg(900,900,ring)+'''</div>
<div class="abs big">15</div><div class="abs dy a">يوم</div>
<div class="abs s a">وغوغنهايم أبوظبي يفتح في السعديات</div>
<div class="abs art">'''+guggenheim_scene(1080,420).replace('width="1080" height="420"','width="1080" height="380"')+'''</div>''',story=True)

# S2 09:30 word of the day — door hanger
page('s2.html','''
.k{left:0;right:0;top:250px;text-align:center}
.dh{left:300px;top:300px}
.in{left:330px;width:420px;text-align:center}
.foot{bottom:90px}''','''<div class="abs k"><span class="kick">WORD OF THE DAY · مصطلح اليوم</span></div>
<div class="abs dh">'''+_svg(480,1400,door_hanger(240,700,420,1180))+'''</div>
<div class="abs in" style="left:330px;top:620px;font:500 16px MS;letter-spacing:5px;color:#B99A5B">PLEASE · DO NOT DISTURB</div>
<div class="abs in a" style="top:700px;font:800 72px/1.2 TJ,MS">سكن<br>بعلامة<br>فندقية</div>
<div class="abs in" style="top:1010px;font:300 25px/1.5 MS;letter-spacing:7px;color:#B99A5B">BRANDED<br>RESIDENCE</div>
<div class="abs in a" style="top:1140px;left:360px;width:360px;font:500 32px/1.6 TJ,MS;color:#444">بيت تملكه، بتصميم وخدمات تحمل اسم علامة فندقية، وغالباً تديره الشركة الفندقية</div>''',story=True)

# S3 12:30 teaser post 1 — museum ticket
page('s3.html','''
.k{left:0;right:0;top:300px;text-align:center}
.h{left:0;right:0;top:360px;text-align:center;font:800 100px/1.2 TJ,MS}.h span{color:#B99A5B}
.tk{left:70px;top:700px;transform:rotate(-4deg)}
.t1{left:150px;top:790px;font:500 18px MS;letter-spacing:6px;color:#B99A5B;transform:rotate(-4deg)}
.t2{left:150px;top:840px;font:300 54px/1.15 MS;letter-spacing:3px;transform:rotate(-4deg)}
.t3{left:150px;top:990px;font:600 30px MS;letter-spacing:4px;color:#B99A5B;transform:rotate(-4deg)}
.st{left:770px;top:770px;font:500 18px MS;letter-spacing:6px;color:#B99A5B;writing-mode:vertical-rl;transform:rotate(-4deg)}
.s{left:120px;right:120px;top:1270px;text-align:center;font:500 42px/1.6 TJ,MS;color:#555;direction:rtl}
.cta{left:0;right:0;top:1520px;text-align:center}
.foot{display:none}''','''<div class="abs k"><span class="kick">NEW POST · منشور جديد</span></div>
<div class="abs h a">موعدنا<br><span>في السعديات</span></div>
<div class="abs tk">'''+_svg(940,460,ticket(10,20,900,420,190))+'''</div>
<div class="abs t1">ADMIT ONE</div><div class="abs t2">GUGGENHEIM<br>ABU DHABI</div><div class="abs t3">11 · 12 · 2026</div>
<div class="abs st">SAADIYAT</div>
<div class="abs s a">الافتتاح، الأرقام، والجيران في المنطقة الثقافية. كل التفاصيل في منشورنا الحين.</div>
<div class="abs cta"><span class="pill a">شوف المنشور ←</span></div>''',story=True,foot=False)

# S4 16:30 did you know — ruler + cone
page('s4.html','''
.k{right:100px;top:300px}
.h{right:100px;top:360px;text-align:right;font:800 96px/1.2 TJ,MS}.h span{color:#B99A5B}
.rl{left:110px;top:560px}.cn{left:200px;top:560px}
.m{left:100px;font:600 24px MS;color:#B99A5B;letter-spacing:2px}
.big{right:100px;top:760px;font:300 210px/1 MS;text-align:right}.big small{font:400 60px MS;color:#B99A5B}
.d{left:520px;right:100px;top:1020px;text-align:right;font:500 40px/1.6 TJ,MS;color:#333;direction:rtl}
.foot{bottom:90px}''','''<div class="abs k"><span class="kick">DID YOU KNOW · هل تعرف؟</span></div>
<div class="abs h a">ارتفاع يشوفه<br><span>كل السعديات</span></div>
<div class="abs rl">'''+_svg(60,1100,height_scale(4,1080,1040,88))+'''</div>
<div class="abs cn">'''+mkcone(1100,1080,40)+'''</div>
<div class="abs m" style="top:560px">88 M</div>
<div class="abs big">88<small>m</small></div>
<div class="abs d a">أعلى مخروط من المخاريط العشرة في غوغنهايم أبوظبي يوصل ارتفاعه إلى <span dir="ltr">88</span> متر.</div>
<div class="src" style="bottom:40px">The National · Gulf News · Illustration not to scale</div>''',story=True)

# S5 16:30 checklist — clipboard
def cb(a): return f'<div class="ci"><span class="o"></span><span class="a">{a}</span></div>'
page('s5.html','''
.k{left:0;right:0;top:280px;text-align:center}
.h{left:0;right:0;top:330px;text-align:center;font:800 88px/1.2 TJ,MS}.h span{color:#B99A5B}
.bd{left:130px;right:130px;top:640px;height:1000px;border:2px solid #C9AE77;border-radius:28px;padding:150px 60px 0}
.clip{left:390px;top:600px;width:300px;height:90px;border:2px solid #B99A5B;border-radius:18px;background:#fff}
.clip:after{content:"";position:absolute;left:115px;top:-36px;width:70px;height:46px;border:2px solid #B99A5B;border-bottom:none;border-radius:35px 35px 0 0;background:#fff}
.ci{display:flex;gap:28px;align-items:center;height:190px;border-bottom:1px solid #EFE6D4;direction:rtl;font:700 40px/1.4 TJ,MS}
.o{flex:none;width:52px;height:52px;border:2px solid #B99A5B;border-radius:50%}
.foot{bottom:90px}''','''<div class="abs k"><span class="kick">CHECKLIST · قائمة تحقق</span></div>
<div class="abs h a">مشروع بعلامة فندقية؟<br><span>اطلب هذي الأوراق</span></div>
<div class="abs bd">'''+cb('اتفاقية الإدارة ومدتها')+cb('تفاصيل رسوم الخدمة')+cb('شروط التأجير والبرنامج الفندقي')+cb('قائمة الخدمات المشمولة')+'''</div>
<div class="abs clip"></div>''',story=True)

# S6 19:30 teaser post 2 — key tag
page('s6.html','''
.k{left:0;right:0;top:290px;text-align:center}
.tg{left:290px;top:360px}
.tt{left:390px;width:300px;text-align:center}
.h{left:0;right:0;top:1290px;text-align:center;font:800 96px/1.2 TJ,MS}.h span{color:#B99A5B}
.s{left:120px;right:120px;top:1530px;text-align:center;font:500 40px/1.6 TJ,MS;color:#555;direction:rtl}
.cta{left:0;right:0;top:1710px;text-align:center}
.foot{display:none}''','''<div class="abs k"><span class="kick">NEW POST · منشور جديد</span></div>
<div class="abs tg">'''+_svg(500,900,keytag(250,560,300,560))+'''</div>
<div class="abs tt" style="top:770px;font:300 34px/1.3 MS;letter-spacing:6px">THE<br>HOXTON<br>HOMES</div>
<div class="abs tt" style="top:950px;font:500 15px MS;letter-spacing:4px;color:#B99A5B">NOMA · SAADIYAT</div>
<div class="abs h a">بيت باسم فندق؟<br><span></span></div>
<div class="abs s a">4 أسئلة لازم تسألها قبل تشتري. المنشور نزل الحين.</div>
<div class="abs cta"><span class="pill a">شوفه واحفظه ←</span></div>''',story=True,foot=False)
