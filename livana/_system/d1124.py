from v4 import *
from art import _svg
GEN='General guidance, not financial or legal advice · Livana'

# ---------- E1: cover — equation + drawing at the bottom ----------
page('e1.html','''
.k{right:90px;top:200px}
.h{right:90px;top:250px;text-align:right;font:800 92px/1.18 TJ,MS}.h span{color:#B99A5B}
.eq{left:0;right:0;top:560px;text-align:center;font:300 88px MS;letter-spacing:6px;color:#111}
.eq b{font-weight:300;color:#B99A5B;display:inline-block;width:110px;height:110px;line-height:104px;border:1.5px solid #C9AE77;border-radius:50%;margin:0 18px}
.sub{left:0;right:0;top:700px;text-align:center;font:500 30px CG;font-style:italic;color:#888}
.art{left:0;top:760px}
''','''<div class="abs k"><span class="pill a">نصيحة استثمارية</span></div>
<div class="abs h a">سعر العقار<br><span>مو هو تكلفتك</span></div>
<div class="abs eq">PRICE + <b>?</b> = COST</div>
<div class="abs sub">The real cost of buying property in Abu Dhabi</div>
<div class="abs art">'''+calc_scene(1080,500)+'''</div>
<div class="src">'''+GEN+'''</div>''')

# ---------- E2: receipt slip ----------
def li(a,e): return f'<div class="li"><span class="t a">{a}</span><i></i><span class="e">{e}</span></div>'
page('e2.html','''
.k{left:0;right:0;top:190px;text-align:center}
.h{left:0;right:0;top:232px;text-align:center;font:800 66px/1.25 TJ,MS}.h span{color:#B99A5B}
.slip{left:170px;width:740px;top:450px;height:600px;background:#FDFBF6;border:1px solid #E6DAC0;border-bottom:none;padding:46px 56px}
.slip:after{content:"";position:absolute;left:-1px;right:-1px;bottom:-22px;height:22px;background:linear-gradient(-45deg,transparent 16px,#FDFBF6 0) 0 0/32px 22px,linear-gradient(45deg,transparent 16px,#FDFBF6 0) 0 0/32px 22px}
.st{display:flex;justify-content:space-between;font:600 15px MS;letter-spacing:4px;color:#B99A5B;border-bottom:1.5px dashed #D9C7A0;padding-bottom:18px}
.li{display:flex;align-items:baseline;gap:14px;padding:16px 0;direction:rtl}
.li .t{font:700 30px TJ,MS;white-space:nowrap}
.li i{flex:1;border-bottom:2px dotted #D9C7A0;transform:translateY(-6px)}
.li .e{font:500 14px MS;letter-spacing:1.5px;color:#999;white-space:nowrap;direction:ltr}
.tot{display:flex;justify-content:space-between;align-items:center;border-top:1.5px dashed #D9C7A0;margin-top:10px;padding-top:22px;direction:rtl}
.tot .t{font:800 34px TJ,MS}.tot .v{font:300 40px MS;color:#B99A5B}
''','''<div class="abs k"><span class="kick">THE REAL RECEIPT</span></div>
<div class="abs h a">وش يضاف فوق السعر؟<br><span>6 بنود احسبها من البداية</span></div>
<div class="abs slip"><div class="st"><span>LIVANA</span><span>BUYER COSTS</span></div>
'''+li('رسوم التسجيل والنقل','REGISTRATION')+li('عمولة الوسيط','BROKER FEE')+li('رسوم التمويل والتقييم','MORTGAGE &amp; VALUATION')+li('رسوم الخدمة السنوية','SERVICE CHARGES')+li('الصيانة والتأثيث','MAINTENANCE &amp; FIT-OUT')+li('فترة بدون مستأجر','VACANCY PERIOD')+'''
<div class="tot"><span class="t a">التكلفة الحقيقية</span><span class="v" dir="ltr">PRICE + ?</span></div></div>
<div class="src">'''+GEN+' · Fees vary by property; confirm with your broker &amp; bank'+'''</div>''')

# ---------- E3: tip — three steps row ----------
def stp(n,a,e,svg): return f'<div class="sp"><div class="ic">{svg}</div><div class="n">{n}</div><div class="t a">{a}</div><div class="e">{e}</div></div>'
ic1=_svg(130,130,calculator(25,8,80,114))
ic2=_svg(130,130,coins(65,100,5,40))
ic3=_svg(130,130,'<path d="M15 110 L115 110"/><path d="M25 95 L50 70 L72 82 L110 30" /><path d="M92 30 L110 30 L110 48"/>')
page('e3.html','''
.tip{left:84px;top:180px;font:300 150px/1 MS;color:#EFE6D4;letter-spacing:10px}
.k{right:90px;top:210px}
.h{right:90px;top:260px;text-align:right;font:800 72px/1.25 TJ,MS}.h span{color:#B99A5B}
.row{left:70px;right:70px;top:560px;display:flex;direction:rtl;justify-content:space-between}
.sp{width:300px;text-align:center;position:relative}
.sp:not(:last-child):after{content:"";position:absolute;left:-30px;top:65px;width:40px;height:1px;background:#C9AE77}
.ic svg{display:block;margin:0 auto}
.n{font:300 30px MS;color:#B99A5B;margin-top:14px}
.t{font:700 32px/1.4 TJ,MS;margin-top:8px}.e{font:500 13px MS;letter-spacing:2px;color:#999;margin-top:8px}
.note{left:120px;right:120px;top:990px;text-align:center;font:500 30px/1.6 TJ,MS;color:#555;direction:rtl;border-top:1px solid #E6DAC0;padding-top:34px}
.cta{left:0;right:0;top:1160px;text-align:center}
''','''<div class="abs tip">TIP</div>
<div class="abs k"><span class="kick">LIVANA TIP</span></div>
<div class="abs h a">قبل ما تقرر<br><span>سوّها بهالترتيب</span></div>
<div class="abs row">'''+
stp('01','احسب كل البنود<br>مو السعر بس','LIST EVERY COST',ic1)+
stp('02','خلّ لك هامش<br>للمصاريف المفاجئة','KEEP A BUFFER',ic2)+
stp('03','قارن العائد<br>بعد المصاريف','COMPARE NET YIELD',ic3)+'''</div>
<div class="abs note">الصفقة الزينة هي اللي أرقامها واضحة من أول يوم. وإذا محتار، نحسبها معك خطوة بخطوة.</div>
<div class="abs cta"><span class="pill a">احفظ المنشور وتواصل معنا ←</span></div>
<div class="src">'''+GEN+'''</div>''')

# ---------- F1: post 2 — red flags in listings ----------
def rf(n,a,e): return f'<div class="rf"><div class="fl"><svg width="34" height="40" viewBox="0 0 34 40" fill="none" stroke="#B99A5B" stroke-width="2"><path d="M4 38 L4 3"/><path d="M4 4 L30 4 L24 13 L30 22 L4 22" fill="#FAF6EE"/></svg><b>{n}</b></div><div><div class="t a">{a}</div><div class="e">{e}</div></div></div>'
page('f1.html','''
.k{right:90px;top:200px}
.h{right:90px;top:240px;text-align:right;font:800 70px/1.22 TJ,MS}.h span{color:#B99A5B}
.art{left:-20px;top:390px}
.grid{left:80px;right:80px;top:880px;display:grid;grid-template-columns:1fr 1fr;column-gap:50px;direction:rtl}
.rf{display:flex;gap:16px;align-items:flex-start;padding:18px 0;border-top:1px solid #EFE6D4}
.fl{flex:none;width:44px;text-align:center}.fl b{display:block;font:400 16px MS;color:#B99A5B;margin-top:2px}
.t{font:700 28px/1.35 TJ,MS;text-align:right}.e{font:500 12px MS;letter-spacing:1.5px;color:#999;margin-top:4px;text-align:right;direction:ltr}
.wide{grid-column:1 / span 2}
''','''<div class="abs k"><span class="kick">RED FLAGS · علامات تحذير</span></div>
<div class="abs h a">إعلان عقاري يشكّك؟<br><span>انتبه لهالـ 5</span></div>
<div class="abs art">'''+inspect_scene(1120,500)+'''</div>
<div class="abs grid">'''+
rf('01','سعر أقل بكثير من السوق','FAR BELOW MARKET PRICE')+
rf('02','يطلب عربون قبل المعاينة','DEPOSIT BEFORE VIEWING')+
rf('03','ما يقدر يوريك العقار','CAN&#39;T SHOW THE UNIT')+
rf('04','يرفض اتفاق مكتوب ورسمي','NO WRITTEN AGREEMENT')+
'<div class="wide">'+rf('05','وسيط بدون ترخيص أو يرفض يعطيك رقم ترخيصه','UNLICENSED BROKER')+'</div>'+'''</div>
<div class="src">'''+GEN+'''</div>''')

# ================= STORIES =================
# W: word of the day — dictionary entry
page('w.html','''
.k{right:100px;top:300px}
.bar{right:100px;top:400px;width:6px;height:520px;background:#B99A5B}
.ar{right:140px;top:400px;text-align:right;font:800 132px/1.15 TJ,MS}
.ph{right:140px;top:720px;font:400 40px MS;letter-spacing:8px;color:#B99A5B}
.pos{right:140px;top:800px;font:500 30px TJ,MS;color:#999;direction:rtl}
.d{right:100px;left:100px;top:1010px;text-align:right;font:500 44px/1.7 TJ,MS;color:#222;direction:rtl}
.ex{right:100px;left:100px;top:1340px;background:#FAF6EE;border-right:4px solid #D9C7A0;padding:30px 36px;text-align:right;font:500 34px/1.6 TJ,MS;color:#555;direction:rtl}
.ex b{color:#B99A5B}
.art{left:90px;top:300px}
.foot{bottom:90px}''','''<div class="abs k"><span class="kick">WORD OF THE DAY · مصطلح اليوم</span></div>
<div class="abs art">'''+_svg(220,220,coins(110,180,6,70))+'''</div>
<div class="abs bar"></div>
<div class="abs ar a">رسوم<br>الخدمة</div>
<div class="abs ph">/ SERVICE CHARGE /</div>
<div class="abs pos a">مصطلح · تكلفة سنوية</div>
<div class="abs d a">مبلغ سنوي يدفعه المالك لصيانة المبنى ومرافقه المشتركة: الأمن، التنظيف، المسبح، النادي والمصاعد.</div>
<div class="abs ex a"><b>مثال:</b> قبل ما تشتري، اسأل كم رسوم الخدمة السنوية واحسبها من مصاريفك، لأنها تأثر على العائد الصافي.</div>''',story=True)

# T1: teaser post 1 — calculator drawing + equation
page('t1.html','''
.art{left:0;top:280px}
.k{left:0;right:0;top:880px;text-align:center}
.h{left:0;right:0;top:940px;text-align:center;font:800 104px/1.2 TJ,MS}.h span{color:#B99A5B}
.eq{left:0;right:0;top:1230px;text-align:center;font:300 80px MS;letter-spacing:6px}.eq b{color:#B99A5B;font-weight:300}
.s{left:120px;right:120px;top:1380px;text-align:center;font:500 40px/1.6 TJ,MS;color:#555;direction:rtl}
.cta{left:0;right:0;top:1600px;text-align:center}
.foot{display:none}''','''<div class="abs art">'''+calc_scene(1080,560)+'''</div>
<div class="abs k"><span class="kick">TODAY 12:30 PM · اليوم الظهر</span></div>
<div class="abs h a">السعر<br><span>+ وش بعد؟</span></div>
<div class="abs eq">PRICE + <b>?</b></div>
<div class="abs s a">6 تكاليف ناس كثير تنساها وقت الشراء. نكشفها اليوم الساعة <span dir="ltr">12:30</span> الظهر.</div>
<div class="abs cta"><span class="pill a">فعّل التنبيهات 🔔</span></div>''',story=True,foot=False)

# Y: area spotlight — Yas Island, drawing inside a circle
def yb(a,e): return f'<div class="yb"><i></i><div><div class="t a">{a}</div><div class="e">{e}</div></div></div>'
page('y.html','''
.k{left:0;right:0;top:270px;text-align:center}
.circ{left:190px;top:340px;width:700px;height:700px;border-radius:50%;border:1.5px solid #C9AE77;overflow:hidden;background:#fff}
.circ .in{position:absolute;left:0;top:190px}
.ring{left:170px;top:320px;width:740px;height:740px;border-radius:50%;border:1px solid #EFE6D4}
.name{left:0;right:0;top:1100px;text-align:center;font:800 96px TJ,MS}
.en{left:0;right:0;top:1230px;text-align:center;font:300 34px MS;letter-spacing:16px;padding-left:16px;color:#B99A5B}
.g{left:100px;right:100px;top:1340px;display:grid;grid-template-columns:1fr 1fr;gap:26px 40px;direction:rtl}
.yb{display:flex;gap:16px;align-items:flex-start}.yb i{flex:none;width:12px;height:12px;border-radius:50%;background:#B99A5B;margin-top:18px}
.t{font:700 36px/1.3 TJ,MS;text-align:right}.e{font:500 15px MS;letter-spacing:1.5px;color:#999;margin-top:4px;text-align:right;direction:ltr}
.src{bottom:40px}
.foot{bottom:90px}''','''<div class="abs k"><span class="kick">AREA SPOTLIGHT · منطقة اليوم</span></div>
<div class="abs ring"></div><div class="abs circ"><div class="in">'''+yas_scene(1080,520).replace('width="1080" height="520"','width="700" height="337"')+'''</div></div>
<div class="abs name a">جزيرة ياس</div>
<div class="abs en">YAS ISLAND</div>
<div class="abs g">'''+yb('حلبة مرسى ياس','YAS MARINA CIRCUIT')+yb('ياس مول','YAS MALL')+yb('مدن ترفيهية عالمية','THEME PARKS')+yb('شاطئ ومرسى','BEACH &amp; MARINA')+'''</div>
<div class="src">Illustration, not to scale</div>''',story=True)

# D: did you know — giant outlined question mark
page('d.html','''
.qm{left:-40px;top:180px;font:800 900px/1 TJ;color:transparent;-webkit-text-stroke:2px #E6DAC0}
.k{right:100px;top:330px}
.h{right:100px;top:390px;text-align:right;font:800 110px/1.15 TJ,MS}.h span{color:#B99A5B}
.box{left:100px;right:100px;top:880px;border:1.5px solid #C9AE77;border-radius:28px;padding:56px 60px;background:#fff;text-align:right;font:500 44px/1.7 TJ,MS;color:#222;direction:rtl}
.box b{color:#B99A5B}
.e{left:120px;right:120px;top:1420px;text-align:center;font:400 26px/1.6 MS;color:#999}
.foot{bottom:90px}''','''<div class="abs qm">؟</div>
<div class="abs k"><span class="kick">DID YOU KNOW · هل تعرف؟</span></div>
<div class="abs h a">معاملات عقارك<br><span>من جوالك</span></div>
<div class="abs box a"><b>داري DARI</b> هي المنصة الرقمية لمركز أبوظبي العقاري، ومنها تنجز معاملات العقار مثل التسجيل وتوثيق عقود الإيجار.</div>
<div class="abs e">DARI is the Abu Dhabi Real Estate Centre&#39;s digital platform for property transactions.</div>''',story=True)

# T2: teaser post 2 — inspection drawing
page('t2.html','''
.k{left:0;right:0;top:300px;text-align:center}
.h{left:0;right:0;top:350px;text-align:center;font:800 100px/1.2 TJ,MS}.h span{color:#B99A5B}
.art{left:-20px;top:680px}
.s{left:120px;right:120px;top:1290px;text-align:center;font:500 42px/1.6 TJ,MS;color:#444;direction:rtl}
.cta{left:0;right:0;top:1560px;text-align:center}
.foot{display:none}''','''<div class="abs k"><span class="kick">TONIGHT 7:30 PM · الليلة</span></div>
<div class="abs h a">إعلان حلو<br><span>بزيادة؟</span></div>
<div class="abs art">'''+inspect_scene(1120,520)+'''</div>
<div class="abs s a">5 علامات تحذير لازم تعرفها قبل ما تتواصل مع أي معلن. الليلة الساعة <span dir="ltr">7:30</span> في منشورنا.</div>
<div class="abs cta"><span class="pill a">لا يفوتك 👀</span></div>''',story=True,foot=False)

# C: deposit checklist — vertical timeline
def tl(n,a,e): return f'<div class="st"><div class="nd">{n}</div><div><div class="t a">{a}</div><div class="e">{e}</div></div></div>'
page('c.html','''
.k{right:100px;top:300px}
.h{right:100px;top:350px;text-align:right;font:800 88px/1.2 TJ,MS}.h span{color:#B99A5B}
.line{right:139px;top:700px;width:2px;height:900px;background:#E6DAC0}
.list{right:100px;left:100px;top:680px;direction:rtl}
.st{display:flex;gap:36px;align-items:center;height:184px}
.nd{flex:none;width:80px;height:80px;border-radius:50%;border:2px solid #B99A5B;background:#fff;font:300 34px/76px MS;color:#B99A5B;text-align:center;position:relative;z-index:2}
.t{font:700 42px/1.35 TJ,MS;text-align:right}.e{font:500 18px MS;letter-spacing:1px;color:#999;margin-top:6px;text-align:right;direction:ltr}
.foot{bottom:90px}''','''<div class="abs k"><span class="kick">BEFORE YOU PAY A DEPOSIT</span></div>
<div class="abs h a">قبل ما تحوّل<br><span>أي عربون</span></div>
<div class="abs line"></div>
<div class="abs list">'''+
tl('1','تأكد إن الوسيط مرخّص','Licensed broker')+
tl('2','تأكد من ملكية البائع رسمياً','Verified ownership')+
tl('3','اتفاق مكتوب بشروط العربون','Written deposit terms')+
tl('4','حوّل بطريقة موثّقة، مو كاش','Traceable payment')+
tl('5','احتفظ بالإيصال والمراسلات','Keep every receipt')+'''</div>''',story=True)
