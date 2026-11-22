from v4 import *
from art import _svg
SRC='Source: WAM; Gulf News (21 Nov 2026) · Illustration, not the actual project'
def ico(body,s=56): return f'<svg width="{s}" height="{s}" viewBox="0 0 48 48" fill="none" stroke="#B99A5B" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'
I={
'gal':'<rect x="8" y="10" width="32" height="24"/><path d="M12 30l8-9 6 6 4-4 6 7"/><circle cx="32" cy="17" r="3"/><path d="M18 40h12M24 34v6"/>',
'cin':'<rect x="6" y="8" width="36" height="22"/><path d="M20 14l9 5-9 5z"/><path d="M10 38h28M14 34v8M34 34v8"/>',
'hot':'<path d="M8 42V10h20v32M28 18h12v24M4 42h40"/><path d="M13 16h4M19 16h4M13 23h4M19 23h4M13 30h4M19 30h4M32 25h4M32 32h4"/>',
'home':'<path d="M6 22L24 8l18 14M11 18v24h26V18"/><rect x="20" y="30" width="8" height="12"/>',
'walk':'<circle cx="26" cy="8" r="3.5"/><path d="M24 14l-5 12 6 4 -2 12M24 14l7 8 6 2M19 26l-6 4"/>',
'brg':'<path d="M4 34h40M4 34q20-20 40 0M12 34v-8M24 34v-12M36 34v-8"/>',
}

# ---------- N1: cover — huge spaced NOMA wordmark + creative-district drawing ----------
page('n1.html','''
.k{right:90px;top:196px}
.word{left:0;right:0;top:250px;text-align:center;font:300 210px/1 MS;letter-spacing:46px;color:#111;padding-left:46px}
.exp{left:0;right:0;top:470px;text-align:center;font:500 16px MS;letter-spacing:6px;color:#B99A5B}
.exp b{color:#111;font-weight:600}
.h{left:0;right:0;top:520px;text-align:center;font:800 64px/1.3 TJ,MS}.h span{color:#B99A5B}
.art{left:0;top:700px}
.stat{left:90px;top:1180px;display:flex;align-items:baseline;gap:18px}
.stat .v{font:300 64px MS;color:#B99A5B}.stat .t{font:700 26px TJ,MS;direction:rtl}
''','''<div class="abs k"><span class="pill a">مشروع جديد · السعديات</span></div>
<div class="abs word">NOMA</div>
<div class="abs exp"><b>NO</b>RTH OF <b>MA</b>NARAT AL SAADIYAT</div>
<div class="abs h a">ألدار تكشف عن حي إبداعي<br><span>جديد في السعديات</span></div>
<div class="abs art">'''+creative_scene(1080,470)+'''</div>
<div class="abs stat"><span class="v" dir="ltr">88,000</span><span class="t">م² شوارع للمشاة</span></div>
<div class="src">'''+SRC+'''</div>''')

# ---------- N2: what's inside — 2x3 icon grid ----------
def cell(k,a,e): return f'<div class="cl"><div class="ic">{ico(I[k],64)}</div><div class="t a">{a}</div><div class="e">{e}</div></div>'
page('n2.html','''
.k{right:90px;top:200px}
.h{right:90px;top:240px;text-align:right;font:800 80px/1.2 TJ,MS}.h span{color:#B99A5B}
.en{right:92px;top:350px;font:500 34px CG;font-style:italic;color:#888}
.grid{left:80px;right:80px;top:450px;display:grid;grid-template-columns:1fr 1fr;border-top:1px solid #E6DAC0}
.cl{padding:30px 34px 30px;border-bottom:1px solid #E6DAC0;text-align:right;height:262px}
.cl:nth-child(odd){border-left:1px solid #E6DAC0}
.grid{direction:rtl}
.cl .ic{height:70px}
.cl .t{font:700 33px/1.3 TJ,MS;margin-top:8px}
.cl .e{font:500 14px MS;letter-spacing:1.5px;color:#999;margin-top:6px;direction:ltr;text-align:right}
''','''<div class="abs k"><span class="kick">WHAT'S INSIDE</span></div>
<div class="abs h a">وش في <span>نوما؟</span></div>
<div class="abs en">a ground-up creative community</div>
<div class="abs grid">'''+
cell('gal','غاليريهات واستوديوهات فنية','GALLERIES &amp; ARTIST STUDIOS')+
cell('cin','سينما على السطح','CINEMA AKIL · ROOFTOP SCREEN')+
cell('hot','أول فندق The Hoxton في أبوظبي','THE HOXTON HOTEL')+
cell('home','سكن: من الاستوديو إلى التاون هاوس','STUDIOS TO TOWNHOUSES')+
cell('walk','أكثر من ثلث الطابق الأرضي للفنون والثقافة','1/3+ GROUND FLOOR FOR CULTURE')+
cell('brg','جسر مكيّف للمشاة إلى السعديات جروف والمتاحف','A/C BRIDGE TO SAADIYAT GROVE')+
'''</div>
<div class="src">'''+SRC+'''</div>''')

# ---------- N3: Livana take — left keys art + right text + timeline row ----------
page('n3.html','''
.k{right:90px;top:200px}
.h{right:90px;top:240px;text-align:right;font:800 72px/1.22 TJ,MS}.h span{color:#B99A5B}
.p{right:90px;width:560px;top:440px;text-align:right;font:500 30px/1.7 TJ,MS;color:#444;direction:rtl}
.keys{left:90px;top:250px;opacity:.95}
.tl{left:90px;right:90px;top:760px;height:2px;background:#E6DAC0}
.dots{left:90px;right:90px;top:740px;display:flex;justify-content:space-between;direction:rtl}
.d{width:300px;text-align:center}
.d i{display:block;width:40px;height:40px;margin:0 auto;border:2px solid #B99A5B;background:#fff;border-radius:50%}
.d i.f{background:#B99A5B}
.d .t{font:700 28px TJ,MS;margin-top:22px;direction:rtl}.d .s{direction:ltr;font:500 14px MS;color:#999;letter-spacing:1.5px;margin-top:6px}
.tips{left:90px;right:90px;top:960px;text-align:right;font:700 30px TJ,MS;direction:rtl}
.tips div{padding:12px 0;border-bottom:1px solid #EFE6D4}.tips b{color:#B99A5B;font-weight:800;margin-left:12px}
.cta{left:90px;top:1170px}
''','''<div class="abs k"><span class="kick">LIVANA TAKE</span></div>
<div class="abs h a">مهتم؟<br><span>تابع قبل الإطلاق</span></div>
<div class="abs p">ألدار تقول إن مراحل المشروع بتنكشف تدريجياً مع بداية السنة الجديدة. لين الحين ما في أسعار أو خطط دفع معلنة.</div>
<div class="abs keys">'''+keys_art(260)+'''</div>
<div class="abs tl"></div>
<div class="abs dots">
<div class="d"><i class="f"></i><div class="t">الإعلان</div><div class="s">21 NOV 2026</div></div>
<div class="d"><i></i><div class="t">كشف المراحل</div><div class="s">FROM EARLY 2027</div></div>
<div class="d"><i></i><div class="t">الأسعار والخطط</div><div class="s">NOT ANNOUNCED YET</div></div>
</div>
<div class="abs tips"><div><b>01</b>اسأل عن موعد التسليم لكل مرحلة</div><div><b>02</b>قارن بالمشاريع القريبة في السعديات</div></div>
<div class="abs cta"><span class="pill a">← سجّل اهتمامك معنا</span></div>
<div class="src">'''+SRC+'''</div>''')

# ---------- Q2: off-plan questions — centered header, numbered circles, construction band bottom ----------
def q(n,a,e): return f'<div class="q"><div class="no">{n}</div><div class="t a">{a}<small>{e}</small></div></div>'
page('q2.html','''
.k{left:0;right:0;top:190px;text-align:center}
.h{left:0;right:0;top:230px;text-align:center;font:800 70px/1.2 TJ,MS}.h span{color:#B99A5B}
.list{left:120px;right:120px;top:420px}
.q{display:flex;flex-direction:row-reverse;align-items:center;gap:26px;padding:15px 0}
.q .no{flex:none;width:62px;height:62px;border:1.5px solid #B99A5B;border-radius:50%;font:300 30px/59px MS;color:#B99A5B;text-align:center}
.q .t{font:700 31px TJ,MS;text-align:right;flex:1}.q .t small{display:block;font:500 14px MS;color:#999;letter-spacing:1px;margin-top:3px;direction:ltr;text-align:right}
.art{left:0;top:900px}
''','''<div class="abs k"><span class="kick">OFF-PLAN · على الخارطة</span></div>
<div class="abs h a">قبل ما تحجز على الخارطة<br><span>اسأل هالـ 5</span></div>
<div class="abs list">'''+
q('1','المشروع مسجّل رسمياً؟','Is the project officially registered?')+
q('2','دفعاتك تروح لحساب ضمان المشروع؟','Do payments go to the project escrow account?')+
q('3','موعد التسليم، وش يصير لو تأخر؟','Handover date &amp; what happens if delayed')+
q('4','كم تدفع قبل التسليم وكم بعده؟','How much before vs after handover')+
q('5','كم رسوم الخدمة المتوقعة؟','Expected service charges')+
'''</div>
<div class="abs art">'''+construction_scene(1080,420)+'''</div>
<div class="src">General guidance, not legal or financial advice · احفظ المنشور</div>''')

# ---------- STORIES ----------
# T1 did you know — NOMA name
page('t1.html','''
.k{left:0;right:0;top:300px;text-align:center}
.h{left:0;right:0;top:360px;text-align:center;font:800 96px/1.2 TJ,MS}
.w{left:0;right:0;top:560px;text-align:center;font:300 170px/1 MS;letter-spacing:30px;padding-left:30px}
.w b{color:#B99A5B;font-weight:300}
.exp{left:0;right:0;top:760px;text-align:center;font:500 30px MS;letter-spacing:4px;color:#888}
.exp b{color:#B99A5B;font-weight:600}
.d{left:120px;right:120px;top:860px;text-align:center;font:500 44px/1.6 TJ,MS;color:#333;direction:rtl}
.art{left:0;top:1180px}
.foot{bottom:90px}''','''<div class="abs k"><span class="kick">DID YOU KNOW · هل تعرف؟</span></div>
<div class="abs h a">وش معنى</div>
<div class="abs w"><b>NO</b>MA</div>
<div class="abs exp"><b>NO</b>rth of <b>MA</b>narat Al Saadiyat</div>
<div class="abs d a">اسم الحي الجديد اللي كشفت عنه ألدار في السعديات، شمال منارة السعديات.</div>
<div class="abs art">'''+creative_scene(1080,470)+'''</div>''',story=True)

# T2 word of the day — Branded residences
page('t2.html','''
.k{left:100px;top:320px}
.w{left:100px;right:100px;top:380px;font:300 120px/1.05 MS;color:#B99A5B}
.rule{left:100px;top:660px;width:120px;height:2px;background:#B99A5B}
.ar{right:100px;left:100px;top:710px;text-align:right;font:800 70px/1.3 TJ,MS}
.d{right:100px;left:100px;top:900px;text-align:right;font:500 40px/1.7 TJ,MS;color:#444}
.e{right:100px;left:100px;top:1200px;font:400 25px/1.6 MS;color:#999}
.ex{right:100px;left:100px;top:1400px;text-align:right;font:700 34px TJ,MS;color:#111;border-right:3px solid #B99A5B;padding-right:24px;direction:rtl}
.foot{bottom:90px}''','''<div class="abs k"><span class="kick">WORD OF THE DAY · مصطلح اليوم</span></div>
<div class="abs w">Branded<br>Residences</div>
<div class="abs rule"></div>
<div class="abs ar a">المساكن ذات العلامة التجارية</div>
<div class="abs d a">بيوت يحمل مشروعها اسم علامة فندقية أو تصميم معروفة، وغالباً تجي مع خدمات ومرافق بمستوى الفندق.</div>
<div class="abs e">Homes carrying a hotel or design brand's name, usually with hotel-style services.</div>
<div class="abs ex">مثال: The Hoxton Homes في نوما، أول مساكن تحمل اسم العلامة في العالم.</div>''',story=True)

# T3 teaser post 1 — fanned 3 slides
page('t3.html','''
.k{right:100px;top:300px}
.h{right:100px;top:350px;text-align:right;font:800 110px/1.1 TJ,MS}.h span{color:#B99A5B}
.s{width:520px;height:650px;border:1px solid #E6DAC0;box-shadow:0 24px 60px rgba(0,0,0,.12);top:820px}
.s1{left:90px;transform:rotate(-7deg)}.s2{left:470px;transform:rotate(6deg);top:860px}.s3{left:280px;top:760px;z-index:2}
.cta{left:0;right:0;top:1560px;text-align:center}
.foot{bottom:90px}''','''<div class="abs k"><span class="kick">NEW POST · SAADIYAT</span></div>
<div class="abs h a">حي جديد<br><span>في السعديات</span></div>
<img class="abs s s1" src="out/n2.png"><img class="abs s s2" src="out/n3.png"><img class="abs s s3" src="out/n1.png">
<div class="abs cta"><span class="pill a">← شوف المنشور</span></div>''',story=True)

# T4 area spotlight — Saadiyat Cultural District with Louvre dome close-up
page('t4.html','''
.art{left:0;top:180px}
.k{left:0;right:0;top:820px;text-align:center}
.h{left:0;right:0;top:870px;text-align:center;font:800 92px/1.15 TJ,MS}.h span{color:#B99A5B}
.en{left:0;right:0;top:1090px;text-align:center;font:500 34px CG;font-style:italic;color:#888}
.list{left:180px;right:180px;top:1170px;direction:rtl}
.it{display:flex;justify-content:space-between;padding:18px 0;border-bottom:1px solid #EFE6D4;font:700 34px TJ,MS}
.it span{font:500 17px MS;color:#999;letter-spacing:1.5px;direction:ltr;align-self:center}
.foot{bottom:90px}''','''<div class="abs art">'''+louvre_dome(1080,600)+'''</div>
<div class="abs k"><span class="kick">AREA SPOTLIGHT · منطقة اليوم</span></div>
<div class="abs h a">المنطقة الثقافية<br><span>في السعديات</span></div>
<div class="abs en">Saadiyat Cultural District</div>
<div class="abs list">
<div class="it">متحف اللوفر أبوظبي<span>LOUVRE ABU DHABI</span></div>
<div class="it">متحف زايد الوطني<span>ZAYED NATIONAL MUSEUM</span></div>
<div class="it">تيم لاب فينومينا<span>teamLab PHENOMENA</span></div>
<div class="it">والجديد: حي نوما<span>NEXT: NOMA</span></div>
</div>''',story=True)

# T5 myth vs fact
page('t5.html','''
.k{left:0;right:0;top:300px;text-align:center}
.box{left:100px;right:100px;padding:56px 60px;text-align:right;direction:rtl}
.b1{top:380px;border:1px solid #E6DAC0}
.b2{top:900px;background:#FAF6EE;border-right:4px solid #B99A5B}
.lab{font:600 18px MS;letter-spacing:5px;color:#999;direction:ltr;text-align:right}
.b2 .lab{color:#B99A5B}
.tx{font:800 58px/1.35 TJ,MS;margin-top:18px}
.b1 .tx{color:#999;text-decoration:line-through;text-decoration-color:#D9C7A0;text-decoration-thickness:3px}
.sm{font:500 34px/1.6 TJ,MS;color:#444;margin-top:18px}
.vs{left:0;right:0;top:800px;text-align:center;font:300 64px MS;color:#B99A5B}
.foot{bottom:90px}''','''<div class="abs k"><span class="kick">MYTH VS FACT · خرافة ولا حقيقة؟</span></div>
<div class="abs box b1"><div class="lab">MYTH · خرافة</div><div class="tx a">أي مشروع جديد سعره أكيد بيرتفع بعد التسليم</div></div>
<div class="abs vs">≠</div>
<div class="abs box b2"><div class="lab">FACT · حقيقة</div><div class="tx a">ما في شي أكيد</div><div class="sm a">السعر بعد التسليم يعتمد على الموقع، وكمية المعروض حوله، وجودة التنفيذ، وحالة السوق وقتها. قارن قبل ما تقرر.</div></div>''',story=True)

# T6 teaser post 2 — big gold "5" + mini post
page('t6.html','''
.n{left:60px;top:220px;font:300 560px/1 MS;color:#B99A5B;opacity:.9}
.h{right:100px;top:340px;text-align:right;font:800 96px/1.15 TJ,MS}.h span{color:#B99A5B}
.sub{right:100px;top:590px;font:500 40px TJ,MS;color:#666;direction:rtl}
.mini{left:250px;top:780px;width:580px;height:725px;border:1px solid #E6DAC0;box-shadow:0 24px 60px rgba(0,0,0,.10)}
.cta{left:0;right:0;top:1590px;text-align:center}
.foot{bottom:90px}''','''<div class="abs n">5</div>
<div class="abs h a">أسئلة<br><span>قبل الحجز</span></div>
<div class="abs sub">على الخارطة؟ اقرأها أول</div>
<img class="abs mini" src="out/q2.png">
<div class="abs cta"><span class="pill a">← احفظ المنشور</span></div>''',story=True)
