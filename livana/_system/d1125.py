from v4 import *
from art import _svg
SRC1='Sources: Abu Dhabi Government / ADREC (2 Jun 2026) · Gulf News · Baker McKenzie'
SRC3='Source: Cavendish Maxwell projections via Khaleej Times, 23 Nov 2026 · estimates'
GEN='General guidance, not legal advice · Livana'

# ---------- K1: cover — gauge meter at 0% ----------
page('k1.html','''
.k{left:0;right:0;top:200px;text-align:center}
.h{left:0;right:0;top:246px;text-align:center;font:800 84px/1.2 TJ,MS}.h span{color:#B99A5B}
.g{left:140px;top:520px}
.big{left:0;right:0;top:745px;text-align:center;font:300 150px/1 MS;letter-spacing:4px}
.lab{top:935px;font:500 22px MS;color:#999;letter-spacing:2px}
.sub{left:110px;right:110px;top:1000px;text-align:center;font:500 32px/1.5 TJ,MS;color:#444;direction:rtl}
.en{left:0;right:0;top:1112px;text-align:center;font:500 30px CG;font-style:italic;color:#888}
''','''<div class="abs k"><span class="kick">ABU DHABI RENTS · الإيجارات</span></div>
<div class="abs h a">تجدّد عقد الإيجار؟<br><span>الزيادة المسموحة الحين</span></div>
<div class="abs g">'''+_svg(800,420,gauge(400,400,360,0.0))+'''</div>
<div class="abs lab" style="left:150px">0%</div><div class="abs lab" style="right:150px">5%</div>
<div class="abs big">0%</div>
<div class="abs sub a">سقف زيادة الإيجار السنوية نزل من <span dir="ltr">5%</span> إلى <span dir="ltr">0%</span>، مؤقتاً ولحين إشعار آخر</div>
<div class="abs en">Abu Dhabi rent-increase cap: 5% → 0%, in force since 2 June 2026</div>
<div class="src">'''+SRC1+'''</div>''')

# ---------- K2: what it means — two horizontal cards ----------
def card(top,tag,en,icon,items):
    li=''.join(f'<li class="a">{x}</li>' for x in items)
    return f'<div class="abs cd" style="top:{top}px"><div class="tb a">{tag} <i>{en}</i></div><div class="ic">{icon}</div><ul>{li}</ul></div>'
ic_t=_svg(200,200,f'<circle cx="70" cy="100" r="40" stroke-width="4"/><circle cx="70" cy="100" r="15" stroke-width="3"/><path d="M110 100 L185 100 M160 100 L160 124 M180 100 L180 118" stroke-width="6"/>')
ic_l=_svg(200,200,tower(40,180,60,150)+tower(110,180,50,110,1)+'<path d="M20 180 L190 180"/>')
page('k2.html','''
.k{right:90px;top:200px}
.h{right:90px;top:240px;text-align:right;font:800 76px/1.2 TJ,MS}.h span{color:#B99A5B}
.cd{left:80px;right:80px;height:330px;border:1.5px solid #C9AE77;border-radius:20px;padding:56px 50px 0 40px}
.tb{position:absolute;right:44px;top:-24px;background:#fff;padding:0 18px;font:800 34px TJ,MS;color:#B99A5B}.tb i{font:500 15px MS;letter-spacing:3px;color:#999;font-style:normal}
.ic{position:absolute;left:30px;top:60px}
ul{list-style:none;margin-left:230px}
li{font:500 29px/1.45 TJ,MS;color:#222;text-align:right;padding:7px 30px 7px 0;position:relative}
li:before{content:"";position:absolute;right:0;top:22px;width:10px;height:10px;border-radius:50%;background:#B99A5B}
''','''<div class="abs k"><span class="kick">WHAT IT MEANS · وش يعني لك؟</span></div>
<div class="abs h a">القرار بالتفصيل</div>
'''+card(420,'للمستأجر','TENANT',ic_t,['عند التجديد، المرجع هو الإيجار في آخر عقد مسجّل في <b>توثيق</b>','يشمل العقارات السكنية والتجارية والصناعية','عقدك جدّدته وسجّلته قبل القرار؟ غالباً ما يشمله'])+card(820,'للمالك','LANDLORD',ic_l,['ما فيه زيادة على الإيجار وقت التجديد حالياً','الخدمة والصيانة الزينة تحافظ على المستأجر','عقارك في الماريه أو الريم (نطاق ADGM)؟ تأكد من القواعد'])+'''
<div class="src">'''+SRC1+'''</div>''')

# ---------- K3: supply — towers proportional to deliveries ----------
page('k3.html','''
.k{right:90px;top:200px}
.h{right:90px;top:240px;text-align:right;font:800 76px/1.2 TJ,MS}.h span{color:#B99A5B}
.art{left:0;top:470px}
.v{font:300 64px MS;text-align:center;width:300px}
.y{font:500 20px MS;letter-spacing:6px;color:#B99A5B;text-align:center;width:300px}
.u{font:500 24px TJ,MS;color:#888;text-align:center;width:300px;direction:rtl}
.note{left:110px;right:110px;top:1150px;text-align:center;font:500 31px/1.55 TJ,MS;color:#444;direction:rtl}
''','''<div class="abs k"><span class="kick">NEW SUPPLY · المعروض الجاي</span></div>
<div class="abs h a">وحدات جديدة بالطريق<br><span>وخيارات أكثر للمستأجر</span></div>
<div class="abs art">'''+supply_scene(1080,640)+'''</div>
<div class="abs v" style="left:174px;top:600px">14,600</div><div class="abs y" style="left:174px;top:680px">2027</div>
<div class="abs v" style="left:520px;top:440px">24,200</div><div class="abs y" style="left:520px;top:520px">2028</div>
<div class="abs u" style="left:174px;top:712px">وحدة متوقعة</div><div class="abs u" style="left:520px;top:552px">وحدة متوقعة</div>
<div class="abs note">مع تجميد الزيادة ودخول وحدات جديدة، التوقعات إن المنافسة بين العقارات القائمة والجديدة بتزيد</div>
<div class="src">'''+SRC3+'''</div>''')

# ---------- K4: before you renew — seal + steps ----------
def sp(n,a,e): return f'<div class="sp"><div class="n">{n}</div><div><div class="t a">{a}</div><div class="e">{e}</div></div></div>'
page('k4.html','''
.seal{left:70px;top:170px;transform:rotate(-12deg)}
.k{right:90px;top:220px}
.h{right:90px;top:262px;text-align:right;font:800 80px/1.2 TJ,MS}.h span{color:#B99A5B}
.list{left:90px;right:90px;top:560px;direction:rtl}
.sp{display:flex;gap:30px;align-items:center;padding:28px 0;border-bottom:1px solid #EFE6D4}
.n{flex:none;font:300 64px/1 MS;color:#B99A5B;width:90px;text-align:center}
.t{font:700 36px/1.35 TJ,MS;text-align:right}.e{font:500 14px MS;letter-spacing:2px;color:#999;margin-top:6px;text-align:right;direction:ltr}
.cta{left:0;right:0;top:1140px;text-align:center}
''','''<div class="abs seal">'''+_svg(340,340,seal(170,170,140))+'''</div>
<div class="abs k"><span class="kick">BEFORE YOU RENEW</span></div>
<div class="abs h a">قبل ما<br><span>تجدّد عقدك</span></div>
<div class="abs list">'''+
sp('01','راجع قيمة الإيجار في آخر عقد توثيق','CHECK YOUR LAST TAWTHEEQ RENT')+
sp('02','اتفق على الشروط كتابياً وسجّل العقد الجديد','AGREE IN WRITING &amp; REGISTER')+
sp('03','قارن مع الوحدات الجديدة قبل ما تقرر','COMPARE WITH NEW UNITS')+'''</div>
<div class="abs cta"><span class="pill a">عندك سؤال عن عقدك؟ راسلنا ←</span></div>
<div class="src">'''+GEN+' · Rules may change; check with ADREC'+'''</div>''')

# ---------- H1: post 2 — developer track record scorecard ----------
def row(n,a,e): return f'<div class="r"><div class="ck">✓</div><div class="tx"><div class="t a">{a}</div><div class="e">{e}</div></div><div class="nn">{n}</div></div>'
page('h1.html','''
.k{left:0;right:0;top:190px;text-align:center}
.h{left:0;right:0;top:232px;text-align:center;font:800 70px/1.22 TJ,MS}.h span{color:#B99A5B}
.art{left:0;top:390px}
.tbl{left:90px;right:90px;top:850px;border-top:1.5px solid #C9AE77}
.r{display:flex;align-items:center;gap:22px;height:66px;border-bottom:1px solid #EFE6D4;direction:rtl}
.nn{order:-1;flex:none;width:44px;font:300 30px MS;color:#B99A5B;text-align:center}
.tx{flex:1;display:flex;align-items:baseline;justify-content:space-between;gap:14px}
.t{font:700 28px TJ,MS;text-align:right}.e{font:500 12px MS;letter-spacing:1.5px;color:#999;direction:ltr;white-space:nowrap}
.ck{flex:none;width:36px;height:36px;border:1.5px solid #C9AE77;border-radius:50%;font:600 18px/34px MS;color:#B99A5B;text-align:center}
''','''<div class="abs k"><span class="kick">DEVELOPER CHECK · فحص المطوّر</span></div>
<div class="abs h a">تشتري من مطوّر؟<br><span>شوف سجلّه قبل كلامه</span></div>
<div class="abs art">'''+handover_scene(1080,460)+'''</div>
<div class="abs tbl">'''+
row('01','مشاريع سلّمها قبل، وهل سلّمها في موعدها؟','DELIVERY RECORD')+
row('02','زُر مجتمع سلّمه وشوف الجودة بعينك','VISIT A HANDED-OVER PROJECT')+
row('03','اسأل السكان عن خدمة ما بعد التسليم','AFTER-SALES SERVICE')+
row('04','رسوم الخدمة في مشاريعه القائمة','SERVICE CHARGES')+
row('05','التشطيب الفعلي مقارنة بالشقة النموذجية','SHOW UNIT VS REALITY')+'''</div>
<div class="src">'''+GEN+'''</div>''')

# ================= STORIES =================
# S1 word of the day — seal
page('s1.html','''
.k{left:0;right:0;top:290px;text-align:center}
.seal{left:240px;top:370px}
.ar{left:0;right:0;top:1000px;text-align:center;font:800 140px/1 TJ,MS}
.en{left:0;right:0;top:1170px;text-align:center;font:300 44px MS;letter-spacing:18px;padding-left:18px;color:#B99A5B}
.d{left:110px;right:110px;top:1290px;text-align:center;font:500 42px/1.65 TJ,MS;color:#333;direction:rtl}
.foot{bottom:90px}''','''<div class="abs k"><span class="kick">WORD OF THE DAY · مصطلح اليوم</span></div>
<div class="abs seal">'''+_svg(600,600,seal(300,300,270))+'''</div>
<div class="abs ar a">توثيق</div>
<div class="abs en">TAWTHEEQ</div>
<div class="abs d a">نظام تسجيل عقود الإيجار في أبوظبي. وآخر عقد مسجّل فيه هو المرجع لقيمة إيجارك عند التجديد.</div>''',story=True)

# S2 good morning — Qasr Al Watan in a tall postcard frame
page('s2.html','''
.fr{left:90px;right:90px;top:260px;height:1180px;border:1.5px solid #C9AE77;border-radius:460px 460px 24px 24px;overflow:hidden}
.fr .in{position:absolute;left:-90px;top:560px}
.gm{left:0;right:0;top:420px;text-align:center;font:800 120px/1.15 TJ,MS}.gm span{color:#B99A5B}
.en{left:0;right:0;top:720px;text-align:center;font:500 46px CG;font-style:italic;color:#888}
.nm{left:0;right:0;top:1490px;text-align:center;font:800 64px TJ,MS}
.nme{left:0;right:0;top:1580px;text-align:center;font:300 28px MS;letter-spacing:14px;color:#B99A5B}
.src{bottom:40px}.foot{bottom:90px}''','''<div class="abs fr"><div class="in">'''+qasr_scene(1080,560)+'''</div></div>
<div class="abs gm a">صباح الخير<br><span>من أبوظبي</span></div>
<div class="abs en">Good morning, Abu Dhabi</div>
<div class="abs nm a">قصر الوطن</div>
<div class="abs nme">QASR AL WATAN</div>
<div class="src">Illustration, not to scale</div>''',story=True)

# S3 teaser post 1 (12:30, live now)
page('s3.html','''
.k{left:0;right:0;top:300px;text-align:center}
.h{left:0;right:0;top:360px;text-align:center;font:800 100px/1.2 TJ,MS}.h span{color:#B99A5B}
.g{left:90px;top:700px}
.big{left:0;right:0;top:930px;text-align:center;font:300 180px/1 MS}
.s{left:120px;right:120px;top:1290px;text-align:center;font:500 42px/1.6 TJ,MS;color:#555;direction:rtl}
.cta{left:0;right:0;top:1560px;text-align:center}
.foot{display:none}''','''<div class="abs k"><span class="kick">NEW POST · منشور جديد</span></div>
<div class="abs h a">إيجارك وقت<br><span>التجديد؟</span></div>
<div class="abs g">'''+_svg(900,470,gauge(450,450,400,0.0))+'''</div>
<div class="abs big">0%</div>
<div class="abs s a">وش يعني قرار تجميد زيادة الإيجار لك، مستأجر أو مالك؟ التفاصيل في منشورنا الحين.</div>
<div class="abs cta"><span class="pill a">شوف المنشور ←</span></div>''',story=True,foot=False)

# S4 did you know — three property types
def pt(svg,a,e): return f'<div class="pt"><div class="ic">{svg}</div><div class="t a">{a}</div><div class="e">{e}</div></div>'
page('s4.html','''
.k{right:100px;top:300px}
.h{right:100px;top:360px;text-align:right;font:800 104px/1.18 TJ,MS}.h span{color:#B99A5B}
.row{left:60px;right:60px;top:820px;display:flex;justify-content:space-between;direction:rtl}
.pt{width:300px;text-align:center}.ic svg{display:block;margin:0 auto}
.t{font:800 44px TJ,MS;margin-top:20px}.e{font:500 16px MS;letter-spacing:3px;color:#999;margin-top:8px}
.hl{position:absolute;left:100px;right:100px;top:1240px}
.d{left:110px;right:110px;top:1300px;text-align:center;font:500 42px/1.65 TJ,MS;color:#333;direction:rtl}
.foot{bottom:90px}''','''<div class="abs k"><span class="kick">DID YOU KNOW · هل تعرف؟</span></div>
<div class="abs h a">التجميد ما يشمل<br><span>السكني بس</span></div>
<div class="abs row">'''+
pt(_svg(240,240,villa(10,220,0.75)+'<path d="M0 220 L240 220"/>'),'سكني','RESIDENTIAL')+
pt(_svg(240,240,shop(40,220,1)+'<path d="M0 220 L240 220"/>'),'تجاري','COMMERCIAL')+
pt(_svg(240,240,factory(45,220,1)+'<path d="M0 220 L240 220"/>'),'صناعي','INDUSTRIAL')+'''</div>
<div class="hl"></div>
<div class="abs d a">قرار سقف الزيادة <span dir="ltr">0%</span> في أبوظبي يشمل العقارات السكنية والتجارية والصناعية، مؤقتاً ولحين إشعار آخر.</div>''',story=True)

# S5 checklist — notepad with ruled lines
def nl(a): return f'<div class="nl"><span class="bx">✓</span><span class="a">{a}</span></div>'
page('s5.html','''
.k{left:0;right:0;top:290px;text-align:center}
.h{left:0;right:0;top:340px;text-align:center;font:800 96px/1.2 TJ,MS}.h span{color:#B99A5B}
.pad{left:120px;right:120px;top:640px;height:960px;background:#FDFBF6;border:1px solid #E6DAC0;border-radius:6px;padding:110px 60px 0;transform:rotate(-1.5deg)}
.pad:before{content:"";position:absolute;left:0;right:0;top:0;height:60px;background:#F3EAD8;border-bottom:1px solid #E6DAC0}
.pad:after{content:"";position:absolute;right:120px;top:60px;bottom:0;width:1.5px;background:#E9C9C0}
.nl{display:flex;gap:28px;align-items:center;height:170px;border-bottom:1.5px solid #E6DAC0;direction:rtl;font:700 42px/1.35 TJ,MS}
.bx{flex:none;font:600 46px MS;color:#B99A5B;width:60px;text-align:center}
.foot{bottom:90px}''','''<div class="abs k"><span class="kick">RENEWAL CHECKLIST</span></div>
<div class="abs h a">ملف التجديد<br><span>جاهز؟</span></div>
<div class="abs pad">'''+nl('عقدك الحالي مسجّل في توثيق')+nl('عرفت قيمة الإيجار المسجّلة')+nl('الشروط الجديدة مكتوبة وواضحة')+nl('سجّلت العقد بعد التوقيع')+'''</div>''',story=True)

# S6 teaser post 2 (19:30, live now)
page('s6.html','''
.art{left:0;top:300px}
.k{left:0;right:0;top:880px;text-align:center}
.h{left:0;right:0;top:940px;text-align:center;font:800 104px/1.2 TJ,MS}.h span{color:#B99A5B}
.s{left:120px;right:120px;top:1230px;text-align:center;font:500 42px/1.6 TJ,MS;color:#555;direction:rtl}
.cta{left:0;right:0;top:1520px;text-align:center}
.foot{display:none}''','''<div class="abs art">'''+handover_scene(1080,540)+'''</div>
<div class="abs k"><span class="kick">NEW POST · منشور جديد</span></div>
<div class="abs h a">قبل ما<br><span>تختار المطوّر</span></div>
<div class="abs s a">5 أشياء تكشف لك سجلّ المطوّر الحقيقي. المنشور نزل الحين.</div>
<div class="abs cta"><span class="pill a">شوفه واحفظه ←</span></div>''',story=True,foot=False)
