from v4 import *
from art import _svg
SRC1='Illustration, not to scale · Livana area guide'
SRC3="Source: What's On; Global Business Outlook (17 Nov 2026) · Illustration"

# ---------- M1: cover — arch window with Al Maryah drawing ----------
page('m1.html','''
.k{right:90px;top:200px}
.h{right:90px;top:250px;text-align:right;font:800 84px/1.18 TJ,MS}.h span{color:#B99A5B}
.arch{left:140px;top:520px;width:800px;height:640px;border:1.5px solid #C9AE77;border-radius:400px 400px 0 0;overflow:hidden}
.arch .in{position:absolute;left:-140px;top:96px}
.name{left:0;right:0;top:1180px;text-align:center;font:300 40px MS;letter-spacing:18px;padding-left:18px}
.ser{left:90px;top:212px;font:500 30px CG;font-style:italic;color:#888}
''','''<div class="abs k"><span class="pill a">اكتشف مع ليفانا</span></div>
<div class="abs ser">Discover with Livana</div>
<div class="abs h a">جزيرة الماريه<br><span>قلب أبوظبي المالي</span></div>
<div class="abs arch"><div class="in">'''+maryah_scene(1080,560)+'''</div></div>
<div class="abs name">AL MARYAH ISLAND</div>
<div class="src">'''+SRC1+'''</div>''')

# ---------- M2: map left + 5 facts right ----------
def f(n,a,e): return f'<div class="it"><b>{n}</b><div><div class="t a">{a}</div><div class="e">{e}</div></div></div>'
page('m2.html','''
.k{right:90px;top:200px}
.h{right:90px;top:240px;text-align:right;font:800 76px/1.2 TJ,MS}.h span{color:#B99A5B}
.map{left:60px;top:430px}
.lab{font:600 13px MS;letter-spacing:3px;color:#999;position:absolute}
.list{right:90px;width:500px;top:420px;direction:rtl}
.it{display:flex;gap:20px;padding:20px 0;border-bottom:1px solid #EFE6D4;align-items:flex-start}
.it b{font:300 34px MS;color:#B99A5B;width:46px;flex:none}
.it .t{font:700 30px/1.35 TJ,MS;text-align:right}
.it .e{font:500 13px MS;letter-spacing:1.5px;color:#999;margin-top:5px;direction:ltr;text-align:right}
''','''<div class="abs k"><span class="kick">WHY AL MARYAH?</span></div>
<div class="abs h a">ليش الناس<br><span>تختارها؟</span></div>
<div class="abs map">'''+island_map(460,520)+'''</div>
<div class="lab" style="left:70px;top:965px">CITY</div><div class="lab" style="left:236px;top:965px">AL MARYAH</div><div class="lab" style="left:440px;top:965px">REEM</div>
<div class="abs list">'''+
f('01','مقر سوق أبوظبي العالمي ADGM','HOME OF ADGM FINANCIAL CENTRE')+
f('02','ذا غاليريا: تسوّق ومطاعم على الواجهة','THE GALLERIA AL MARYAH ISLAND')+
f('03','مستشفى كليفلاند كلينك أبوظبي','CLEVELAND CLINIC ABU DHABI')+
f('04','فنادق فاخرة وممشى على البحر','LUXURY HOTELS &amp; PROMENADE')+
f('05','جسور تربطها بوسط المدينة والريم','BRIDGES TO DOWNTOWN &amp; REEM')+
'''</div>
<div class="src">'''+SRC1+'''</div>''')

# ---------- M3: news hook — big stacked number rows ----------
def row(v,a,e): return f'<div class="r"><div class="v" dir="ltr">{v}</div><div class="tx"><div class="t a">{a}</div><div class="e">{e}</div></div></div>'
page('m3.html','''
.k{right:90px;top:200px}
.h{right:90px;left:90px;top:240px;text-align:right;font:800 58px/1.3 TJ,MS}.h span{color:#B99A5B}
.rows{left:90px;right:90px;top:500px}
.r{display:flex;justify-content:space-between;align-items:center;padding:30px 0;border-top:1px solid #E6DAC0}
.r:last-child{border-bottom:1px solid #E6DAC0}
.v{font:300 92px/1 MS;color:#111}.v small{font-size:36px;color:#B99A5B;margin-left:10px;font-weight:400}
.tx{text-align:right}.t{font:700 32px TJ,MS}.e{font:500 14px MS;letter-spacing:1.5px;color:#999;margin-top:6px}
.note{right:90px;left:90px;top:1080px;text-align:right;font:500 27px/1.6 TJ,MS;color:#555;direction:rtl}
.cta{left:90px;top:1186px}
''','''<div class="abs k"><span class="kick">NEW · 17 NOV 2026</span></div>
<div class="abs h a">إعمار وشركة العين لإدارة الأصول<br><span>5 مشاريع بعلامات فندقية</span></div>
<div class="abs rows">'''+
row('8<small>BILLION AED</small>','مليار درهم قيمة المشاريع','TOTAL PIPELINE VALUE')+
row('5','مشاريع: Address · Palace · Vida','BRANDED RESIDENTIAL PROJECTS')+
row('4.7<small>M SQ FT</small>','مليون قدم² تقريباً','APPROX. TOTAL AREA')+
'''</div>
<div class="abs note">من ضمنها Address Residences في جزيرة الماريه، أول مشروع بعلامة Address في أبوظبي. الأسعار وخطط الدفع لم تُعلن بعد.</div>
<div class="abs cta"><span class="pill a">← تابعنا لأول التفاصيل</span></div>
<div class="src">'''+SRC3+'''</div>''')

# ---------- R1: post 2 — ready vs off-plan comparison ----------
def cmp(a,l,r): return f'<div class="c"><div class="m">{l}</div><div class="lb a">{a}</div><div class="m">{r}</div></div>'
page('r1.html','''
.k{left:0;right:0;top:190px;text-align:center}
.h{left:0;right:0;top:230px;text-align:center;font:800 76px/1.2 TJ,MS}.h span{color:#B99A5B}
.heads{left:90px;right:90px;top:420px;display:flex;justify-content:space-between;direction:rtl}
.hd{width:400px;text-align:center}.hd svg{display:block;margin:0 auto}
.hd .t{font:800 40px TJ,MS;margin-top:8px}.hd .e{font:500 14px MS;letter-spacing:3px;color:#B99A5B;margin-top:4px}
.vs{left:0;right:0;top:530px;text-align:center;font:300 48px MS;color:#B99A5B}
.tbl{left:90px;right:90px;top:740px;direction:rtl}
.c{display:flex;align-items:center;border-top:1px solid #EFE6D4;padding:20px 0}
.c:last-child{border-bottom:1px solid #EFE6D4}
.c .m{width:370px;text-align:center;font:500 27px/1.4 TJ,MS;color:#333;direction:rtl}
.c .lb{flex:1;text-align:center;font:600 18px TJ,MS;color:#B99A5B;letter-spacing:1px}
''','''<div class="abs k"><span class="kick">READY VS OFF-PLAN</span></div>
<div class="abs h a">جاهز ولا على الخارطة؟<br><span>أيهم يناسبك</span></div>
<div class="abs heads">
<div class="hd">'''+keys_art(170)+'''<div class="t a">جاهز</div><div class="e">READY</div></div>
<div class="hd">'''+plan_art(170,170).replace('viewBox="0 0 170 170"','viewBox="0 0 420 420"')+'''<div class="t a">على الخارطة</div><div class="e">OFF-PLAN</div></div>
</div>
<div class="abs vs">VS</div>
<div class="abs tbl">'''+
cmp('السكن','تسكن أو تأجّر فوراً','تنتظر لين التسليم')+
cmp('الدفع','مبلغ أكبر وقت الشراء','دفعات موزّعة على مراحل')+
cmp('المعاينة','تشوف العقار بعينك','تعتمد على المخطط والمطوّر')+
cmp('المخاطرة','أقل: الوحدة موجودة','تأخير محتمل في التسليم')+
cmp('يناسب','اللي يبي دخل إيجار الحين','اللي يخطط على المدى البعيد')+
'''</div>
<div class="src">General guidance, not financial advice · احفظ المنشور</div>''')

# ---------- STORIES ----------
# S1 word of the day — centered, gold circle
page('s1.html','''
.k{left:0;right:0;top:300px;text-align:center}
.ring{left:190px;top:420px;width:700px;height:700px;border:1.5px solid #C9AE77;border-radius:50%}
.ring2{left:220px;top:450px;width:640px;height:640px;border:1px solid #EFE6D4;border-radius:50%}
.ar{left:0;right:0;top:620px;text-align:center;font:800 120px/1.1 TJ,MS}
.en{left:0;right:0;top:790px;text-align:center;font:300 64px MS;letter-spacing:10px;color:#B99A5B}
.d{left:130px;right:130px;top:1200px;text-align:center;font:500 42px/1.7 TJ,MS;color:#333;direction:rtl}
.e{left:150px;right:150px;top:1480px;text-align:center;font:400 25px/1.6 MS;color:#999}
.foot{bottom:90px}''','''<div class="abs k"><span class="kick">WORD OF THE DAY · مصطلح اليوم</span></div>
<div class="abs ring"></div><div class="abs ring2"></div>
<div class="abs ar a">التملّك الحر</div>
<div class="abs en">FREEHOLD</div>
<div class="abs d a">تملك العقار والأرض اللي عليها ملكية كاملة باسمك، بدون مدة تنتهي. في أبوظبي متاح لغير المواطنين في مناطق استثمارية محددة.</div>
<div class="abs e">Full ownership of the property and its land, with no expiry. Open to non-nationals in designated investment zones.</div>''',story=True)

# S2 did you know — map on the left, text right
page('s2.html','''
.k{right:100px;top:300px}
.h{right:100px;top:360px;text-align:right;font:800 104px/1.15 TJ,MS}.h span{color:#B99A5B}
.map{left:60px;top:700px}
.big{right:100px;top:760px;width:430px;text-align:right;font:500 40px/1.65 TJ,MS;color:#333;direction:rtl}
.big b{color:#B99A5B}
.bar{left:100px;right:100px;top:1340px;height:1px;background:#E6DAC0}
.q{left:100px;right:100px;top:1390px;text-align:center;font:700 44px TJ,MS;direction:rtl}
.foot{bottom:90px}''','''<div class="abs k"><span class="kick">DID YOU KNOW · هل تعرف؟</span></div>
<div class="abs h a">جزيرة<br><span>بين جزيرتين</span></div>
<div class="abs map">'''+island_map(460,520)+'''</div>
<div class="abs big a">جزيرة الماريه تقع بين <b>وسط المدينة</b> وجزيرة <b>الريم</b>، ومرتبطة بالاثنين بجسور، وفيها مقر سوق أبوظبي العالمي.</div>
<div class="abs bar"></div>
<div class="abs q a">اليوم الظهر نكتشفها معاً في منشورنا 👀</div>''',story=True)

# S3 teaser post 1 — phone frame
page('s3.html','''
.k{left:0;right:0;top:260px;text-align:center}
.h{left:0;right:0;top:310px;text-align:center;font:800 100px/1.15 TJ,MS}.h span{color:#B99A5B}
.ph{left:250px;top:600px;width:580px;height:1020px;border:2px solid #111;border-radius:60px;padding:24px;background:#fff;box-shadow:0 30px 70px rgba(0,0,0,.10)}
.ph img{width:100%;border-radius:10px;margin-top:150px;border:1px solid #EFE6D4}
.ph i{position:absolute;left:230px;top:22px;width:120px;height:26px;background:#111;border-radius:13px}
.ph .u{position:absolute;left:44px;top:90px;font:600 22px MS}
.cta{left:0;right:0;top:1680px;text-align:center}
.foot{display:none}''','''<div class="abs k"><span class="kick">NEW POST · DISCOVER</span></div>
<div class="abs h a">اكتشف<br><span>جزيرة الماريه</span></div>
<div class="abs ph"><i></i><div class="u">livana_realestate</div><img src="out/m1.png"></div>
<div class="abs cta"><span class="pill a">← المنشور الحين في الصفحة</span></div>''',story=True,foot=False)

# S4 checklist — viewing checklist with tick boxes
def ck(a,e,on=False): return f'<div class="ck"><div class="bx{" on" if on else ""}"></div><div><div class="t a">{a}</div><div class="e">{e}</div></div></div>'
page('s4.html','''
.art{left:620px;top:260px}
.k{right:100px;top:300px}
.h{right:100px;top:350px;text-align:right;font:800 84px/1.18 TJ,MS;width:620px}.h span{color:#B99A5B}
.list{left:100px;right:100px;top:740px;direction:rtl}
.ck{display:flex;gap:30px;align-items:center;padding:30px 0;border-bottom:1px solid #EFE6D4}
.bx{flex:none;width:54px;height:54px;border:2px solid #B99A5B;border-radius:8px;position:relative}
.bx.on:after{content:"";position:absolute;left:16px;top:4px;width:14px;height:28px;border:solid #B99A5B;border-width:0 4px 4px 0;transform:rotate(45deg)}
.t{font:700 42px TJ,MS;text-align:right}.e{font:500 18px MS;color:#999;letter-spacing:1px;margin-top:4px;text-align:right;direction:ltr}
.foot{bottom:90px}''','''<div class="abs art" style="left:100px">'''+plan_art(250,250).replace('viewBox="0 0 250 250"','viewBox="0 0 420 420"')+'''</div>
<div class="abs k"><span class="kick">VIEWING CHECKLIST</span></div>
<div class="abs h a">رايح تعاين؟<br><span>شيّك على هذي</span></div>
<div class="abs list">'''+
ck('ضغط الماء والتكييف','Water pressure &amp; A/C',True)+
ck('الرطوبة وآثار التسريب','Damp or leak marks',True)+
ck('اتجاه الشمس والإطلالة','Sun direction &amp; view')+
ck('الإزعاج من الشارع','Street noise')+
ck('المواقف والمرافق','Parking &amp; amenities')+
ck('رسوم الخدمة السنوية','Annual service charges')+
'''</div>''',story=True)

# S5 insight — quote card with big quotation mark and dhow drawing
page('s5.html','''
.q1{left:90px;top:300px;font:300 360px/1 CG;color:#D9C7A0}
.k{right:100px;top:330px}
.t{right:100px;left:100px;top:560px;text-align:right;font:800 84px/1.4 TJ,MS;direction:rtl}.t span{color:#B99A5B}
.s{right:100px;left:100px;top:1060px;text-align:right;font:500 38px/1.6 TJ,MS;color:#555;direction:rtl}
.art{left:0;top:1320px}
.foot{bottom:90px}''','''<div class="abs q1">&ldquo;</div>
<div class="abs k"><span class="kick">LIVANA INSIGHT</span></div>
<div class="abs t a">اختر الموقع اللي<br>بتعيشه <span>كل يوم</span>،<br>مو اللي يعجبك<br><span>مرة بالسنة</span></div>
<div class="abs s a">قرب الدوام والمدارس والخدمات يفرق في راحتك، وفي طلب المستأجرين لو قررت تأجّر.</div>
<div class="abs art">'''+_svg(1080,420,'<path d="M40 300 L1040 300"/>'+water(326,1080,3)+dhow(420,290,1.6))+'''</div>''',story=True)

# S6 teaser post 2 — split halves
page('s6.html','''
.half{left:0;right:0;height:560px}
.top{top:330px;border-bottom:1px solid #E6DAC0}
.l1{left:0;right:0;top:360px;text-align:center}
.l2{left:0;right:0;top:1000px;text-align:center}
.t{font:800 96px TJ,MS}.e{font:500 20px MS;letter-spacing:6px;color:#B99A5B;margin-top:8px}
.vs{left:470px;top:820px;width:140px;height:140px;border-radius:50%;background:#B99A5B;color:#fff;font:300 46px/140px MS;text-align:center}
.q{left:100px;right:100px;top:1470px;text-align:center;font:700 52px/1.4 TJ,MS;direction:rtl}.q span{color:#B99A5B}
.cta{left:0;right:0;top:1680px;text-align:center}
.foot{display:none}''','''<div class="abs half top"></div>
<div class="abs l1">'''+keys_art(240)+'''<div class="t a">جاهز</div><div class="e">READY</div></div>
<div class="abs vs">VS</div>
<div class="abs l2"><div class="t a">على الخارطة</div><div class="e">OFF-PLAN</div>'''+plan_art(220,220).replace('viewBox="0 0 220 220"','viewBox="0 0 420 420"')+'''</div>
<div class="abs q a">أنت من أي فريق؟<br><span>المقارنة كاملة في منشورنا</span></div>
<div class="abs cta"><span class="pill a">← شوف المنشور</span></div>''',story=True,foot=False)
