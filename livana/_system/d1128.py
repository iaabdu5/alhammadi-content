from v4 import *
from art import _svg
SRCA='Source: Aldar statement via WAM · The National · Gulf Today (27 Nov 2026); phase 1: Aldar via Zawya (31 Jul 2026)'
GEN='General guidance, not legal or financial advice · Livana'
N=lambda s:f'<span dir="ltr">{s}</span>'

# ---------- A1: porthole drawing + giant 900 ----------
scene=canopy_scene(1080,520)
page('a1.html','''
.port{left:76px;top:225px;width:420px;height:420px;border-radius:50%;border:1.5px solid #B99A5B;overflow:hidden;display:flex;align-items:flex-end;justify-content:center}
.port2{left:60px;top:209px;width:452px;height:452px;border-radius:50%;border:1px solid #E6DAC0}
.port svg{width:680px;height:327px;margin-bottom:40px}
.k{right:90px;top:250px}
.h{right:84px;top:295px;width:470px;text-align:right;font:800 60px/1.3 TJ,MS;white-space:nowrap}.h span{color:#B99A5B}
.n{left:76px;top:760px;font:300 300px/1 MS;letter-spacing:-6px;color:#111}
.u{left:650px;top:830px;font:500 34px/1.35 MS;letter-spacing:6px;color:#B99A5B}.u i{display:block;font:300 26px MS;font-style:normal;color:#777;letter-spacing:4px}
.line{left:90px;right:90px;top:1110px}
.sub{right:90px;top:1135px;text-align:right;font:500 30px/1.5 TJ,MS;color:#444;width:900px}
.en{left:92px;top:1145px;font:500 27px CG;font-style:italic;color:#888}
''',f'''<div class="abs port2"></div><div class="abs port">{scene}</div>
<div class="abs k"><span class="kick">MARKET PULSE · YAS ISLAND</span></div>
<div class="abs h a">مبيعات تتجاوز<br><span>{N("900")} مليون درهم</span><br>في إطلاق واحد</div>
<div class="abs n">900</div>
<div class="abs u">MILLION+<i>AED · IN SALES</i></div>
<div class="abs hl line"></div>
<div class="abs sub a">ذا كانوبيز سانكتشواري من الدار · وجهة ياس بوينت</div>
<div class="abs en" style="top:1200px">The Canopies Sanctuary, Yas Point</div>
<div class="src">{SRCA}</div>''')

# ---------- A2: horizontal progress bars ----------
def bar(top,num,ar,en,pct):
    return f'''<div class="abs row" style="top:{top}px">
<div class="num">{num}</div><div class="lab a">{ar}<i>{en}</i></div>
<div class="trk"><div class="fil" style="width:{pct}%"></div></div></div>'''
page('a2.html','''
.k{right:90px;top:215px}
.h{right:90px;top:255px;text-align:right;font:800 64px/1.25 TJ,MS}.h span{color:#B99A5B}
.row{left:90px;right:90px;height:220px}
.num{position:absolute;left:0;top:0;font:300 120px/1 MS;letter-spacing:-2px}
.lab{position:absolute;right:0;top:14px;width:520px;text-align:right;font:500 34px/1.4 TJ,MS;color:#222}
.lab i{display:block;font:500 22px CG;font-style:italic;color:#999;direction:ltr;text-align:right;margin-top:6px}
.trk{position:absolute;left:0;right:0;top:150px;height:12px;background:#F1EADB;border-radius:6px}
.fil{height:12px;background:#B99A5B;border-radius:6px}
.ph{left:90px;right:90px;top:960px}
.pt{font:500 15px MS;letter-spacing:5px;color:#B99A5B;margin-bottom:22px}
.pr{display:flex;align-items:center;gap:22px;margin-bottom:22px;direction:ltr}
.pb{height:44px;border:1.5px solid #B99A5B;border-radius:4px}
.pb.f{background:#B99A5B}
.pl{font:500 28px TJ,MS;color:#333;direction:rtl}
.pl b{font:300 36px MS;color:#111;margin-left:8px}
''',bar(430,'85%+','من الوحدات انباعت','of homes sold',85)+bar(660,'67%','من المبيعات لمقيمين ومشترين من الخارج','residents & overseas buyers',67)+f'''
<div class="abs k"><span class="kick">THE LAUNCH IN NUMBERS</span></div>
<div class="abs h a">الأرقام <span>باختصار</span></div>
<div class="abs ph"><div class="pt">TWO PHASES · SALES</div>
<div class="pr"><div class="pb f" style="width:420px"></div><div class="pl a"><b>1.5</b>مليار درهم · المرحلة الأولى (يوليو)</div></div>
<div class="pr"><div class="pb" style="width:252px"></div><div class="pl a"><b>900+</b>مليون درهم · الإطلاق الجديد (نوفمبر)</div></div></div>
<div class="abs a" style="right:90px;top:1185px;font:500 24px TJ,MS;color:#777">استوديو، غرفة، غرفتين و{N("3")} غرف · حدائق {N("11,000")} متر مربع</div>
<div class="src">{SRCA}</div>''')

# ---------- A3: staggered takeaways + CTA ----------
icons=[_svg(110,110,tree(55,104,100,30)),_svg(110,110,globe(55,48,38).replace('stroke-width="1.3"','stroke-width="1"')),_svg(110,110,keys_art(110,110) if False else '<circle cx="34" cy="55" r="24"/><circle cx="34" cy="55" r="9"/><path d="M58 55 L100 55 M88 55 L88 70 M76 55 L76 66"/>')]
tk=[('الطلب على ياس مستمر','بعد مرحلة أولى بـ'+N('1.5')+' مليار، الإطلاق الثاني انباع أغلبه بسرعة.'),
    ('المشترين من كل مكان','الإمارات، بريطانيا، الهند، البرازيل وهولندا من أعلى الجنسيات شراءً.'),
    ('السرعة مو سبب تستعجل','اقرأ العقد وخطة الدفع وتاريخ التسليم المتوقع قبل أي دفعة.')]
cards=''
for i,(t,d) in enumerate(tk):
    side='right:90px' if i%2==0 else 'left:90px'
    cards+=f'''<div class="abs cd" style="{side};top:{420+i*240}px"><div class="ic">{icons[i]}</div><div class="tx a"><b>{t}</b>{d}</div><div class="no">0{i+1}</div></div>'''
page('a3.html','''
.k{right:90px;top:215px}
.h{right:90px;top:255px;text-align:right;font:800 64px/1.25 TJ,MS}.h span{color:#B99A5B}
.cd{width:780px;height:200px;border:1.5px solid #E6DAC0;background:#fff;display:flex;align-items:center;gap:26px;padding:0 34px;direction:rtl}
.ic{width:110px;flex:none}
.tx{font:500 27px/1.5 TJ,MS;color:#444}.tx b{display:block;font:800 34px TJ,MS;color:#111;margin-bottom:4px}
.no{position:absolute;top:-22px;left:30px;background:#fff;padding:0 12px;font:300 34px MS;color:#B99A5B}
.dots{left:538px;top:600px;width:2px;height:500px;border-left:2px dotted #D9C7A0}
.cta{right:90px;top:1150px;text-align:right}
.ct2{right:90px;top:1210px;font:500 22px CG;font-style:italic;color:#999}
''',f'''<div class="abs k"><span class="kick">WHAT IT MEANS FOR YOU</span></div>
<div class="abs h a">وش يعني <span>هذا لك؟</span></div>
{cards}
<div class="abs cta a"><span class="pill">تبي تعرف المتاح في ياس؟ راسلنا</span></div>
<div class="src">{GEN} · {SRCA.split(';')[0]}</div>''')

# ---------- B1: glossary cover with book + index tabs ----------
tabs=['EOI','RESERVATION','SPA','PAYMENT PLAN','HANDOVER']
tb=''.join(f'<div class="tb" style="top:{i*96}px;right:{-150 if i%2 else -128}px">{t}</div>' for i,t in enumerate(tabs))
page('b1.html','''
.k{right:90px;top:215px}
.h{right:90px;top:260px;text-align:right;font:800 78px/1.25 TJ,MS}.h span{color:#B99A5B}
.bk{left:110px;top:640px;width:560px;height:520px;border:1.5px solid #B99A5B;background:#fff}
.bk:before{content:"";position:absolute;left:18px;top:-12px;width:560px;height:520px;border:1px solid #D9C7A0;z-index:-1}
.bk:after{content:"";position:absolute;left:36px;top:-24px;width:560px;height:520px;border:1px solid #EFE6D3;z-index:-2}
.tbs{position:absolute;right:0;top:40px}
.tb{position:absolute;height:64px;width:150px;padding:0 14px;display:flex;align-items:center;justify-content:flex-end;border:1.5px solid #B99A5B;border-left:none;background:#fff;font:600 14px MS;letter-spacing:2px;color:#B99A5B;white-space:nowrap;border-radius:0 6px 6px 0}
.tb:nth-child(1){background:#B99A5B;color:#fff}
.bt{position:absolute;left:50px;top:70px;font:300 92px/1 MS;letter-spacing:8px}
.bt2{position:absolute;left:54px;top:186px;font:500 17px MS;letter-spacing:6px;color:#B99A5B}
.ln{position:absolute;left:54px;right:60px;height:1px;background:#EFE6D3}
.en{right:90px;top:560px;font:500 28px CG;font-style:italic;color:#888}
''',f'''<div class="abs k"><span class="kick">OFF-PLAN GLOSSARY</span></div>
<div class="abs h a">{N("5")} كلمات بتسمعها<br><span>في أي إطلاق عقاري</span></div>
<div class="abs en">Five words you will hear at every launch</div>
<div class="abs bk"><div class="bt">A—Z</div><div class="bt2">LAUNCH DAY TERMS</div>
{''.join(f'<div class="ln" style="top:{270+k*44}px"></div>' for k in range(5))}
<div class="tbs">{tb}</div></div>
<div class="abs a" style="right:90px;top:1195px;text-align:right;font:500 30px/1.6 TJ,MS;color:#444">احفظ البوست قبل ما تحضر أي إطلاق، واسحب للكلمات</div>
<div class="src">{GEN}</div>''')

# ---------- B2: stacked index cards ----------
terms=[('EOI','Expression of Interest','إبداء اهتمام: مبلغ مبدئي يعطيك أولوية الاختيار يوم الإطلاق. اسأل دائماً: هل هو مسترد؟'),
       ('RESERVATION','Booking form','الحجز: تختار الوحدة، توقّع نموذج الحجز وتدفع عربون الحجز.'),
       ('SPA','Sale & Purchase Agreement','اتفاقية البيع والشراء: العقد الأساسي، فيه السعر وخطة الدفع وتاريخ التسليم المتوقع.'),
       ('PAYMENT PLAN','Instalment schedule','خطة الدفع: جدول الدفعات أثناء البناء وعند التسليم، وأحياناً بعده.'),
       ('HANDOVER','Completion & keys','التسليم: تستلم الوحدة بعد الإنجاز والفحص وإتمام الإجراءات.')]
cs=''
for i,(t,e,a) in enumerate(terms):
    rot=(-0.5,0.4,-0.3,0.5,-0.4)[i]
    cs+=f'''<div class="abs ic" style="top:{300+i*196}px;transform:rotate({rot}deg)"><div class="tab">{t}</div><div class="ee">{e}</div><div class="aa a">{a}</div></div>'''
page('b2.html','''
.k{right:90px;top:200px}
.ic{left:90px;right:90px;height:164px;border:1.5px solid #D9C7A0;background:#fff;padding:26px 34px 0}
.ic:nth-child(odd){border-color:#B99A5B}
.tab{position:absolute;left:30px;top:-20px;background:#fff;border:1.5px solid #B99A5B;padding:4px 16px;font:600 17px MS;letter-spacing:3px;color:#B99A5B}
.ee{position:absolute;left:34px;top:30px;font:500 21px CG;font-style:italic;color:#999}
.aa{position:absolute;right:34px;left:34px;top:62px;text-align:right;font:500 28px/1.5 TJ,MS;color:#222}
''',f'''<div class="abs k"><span class="kick">THE GLOSSARY · القاموس</span></div>
{cs}
<div class="abs a" style="right:90px;top:1290px;font:500 20px TJ,MS;color:#999"></div>
<div class="src">{GEN}</div>''')

# ================= STORIES 1080x1920 =================
SC='.logo{top:80px}.tag{top:150px}.foot{bottom:90px}.cnr.tr{top:80px}.cnr.bl{bottom:80px}'

# S1 area: giant pale YAS letters + drawing
page('s1.html',SC+'''
.big{left:0;right:0;top:430px;text-align:center;font:300 400px/1 MS;letter-spacing:60px;color:#F3ECDD;padding-left:60px}
.dr{left:0;top:640px}
.k{right:90px;top:280px}
.h{right:90px;top:320px;text-align:right;font:800 84px/1.2 TJ,MS}.h span{color:#B99A5B}
.ls{right:90px;left:90px;top:1260px;direction:rtl}
.it{display:flex;align-items:center;gap:22px;font:500 38px TJ,MS;color:#333;padding:22px 0;border-bottom:1px solid #EFE6D3}
.it i{width:18px;height:18px;border-radius:50%;border:2px solid #B99A5B;flex:none}
''',f'''<div class="abs big">YAS</div>
<div class="abs dr">{yas_scene(1080,620)}</div>
<div class="abs k"><span class="kick">GOOD MORNING · AREA SPOTLIGHT</span></div>
<div class="abs h a">صباح الخير<br><span>من جزيرة ياس</span></div>
<div class="abs ls a"><div class="it"><i></i>واجهات بحرية وممشى</div><div class="it"><i></i>حدائق ومساحات خضراء</div><div class="it"><i></i>ترفيه وفعاليات طول السنة</div></div>''',story=True)

# S2 word of the day in a speech bubble
page('s2.html',SC+'''
.k{right:90px;top:300px}
.h{right:90px;top:345px;font:800 70px TJ,MS}
.bb{left:70px;top:520px}
.w{left:0;right:0;top:640px;text-align:center;font:300 210px/1 MS;letter-spacing:24px;padding-left:24px}
.ph{left:0;right:0;top:880px;text-align:center;font:500 22px MS;letter-spacing:6px;color:#B99A5B}
.mn{left:150px;right:150px;top:950px;text-align:center;font:500 40px/1.5 TJ,MS;color:#333}
.ex{left:110px;right:110px;top:1320px;border-right:4px solid #B99A5B;background:#FAF6EE;padding:30px 36px;text-align:right;font:500 34px/1.6 TJ,MS;color:#444}
.ex b{display:block;font:600 16px MS;letter-spacing:4px;color:#B99A5B;margin-bottom:10px;direction:ltr;text-align:right}
''',f'''<div class="abs k"><span class="kick">WORD OF THE DAY</span></div>
<div class="abs h a">كلمة اليوم</div>
<div class="abs bb">{_svg(940,640,speech_bubble(4,4,930,560,'left'))}</div>
<div class="abs w">EOI</div>
<div class="abs ph">/ EXPRESSION OF INTEREST /</div>
<div class="abs mn a">إبداء اهتمام: مبلغ مبدئي يحجز لك أولوية الاختيار يوم إطلاق المشروع</div>
<div class="abs ex a"><b>TIP</b>قبل ما تدفع، اسأل: هل المبلغ مسترد لو ما حصلت الوحدة اللي تبيها؟</div>''',story=True)

# S3 teaser post A: donut ring 85%
import math
r=300;c=2*math.pi*r
ring=_svg(720,720,f'<circle cx="360" cy="360" r="{r}" stroke="#F1EADB" stroke-width="22"/><circle cx="360" cy="360" r="{r}" stroke="#B99A5B" stroke-width="22" stroke-linecap="butt" stroke-dasharray="{c*0.85} {c}" transform="rotate(-90 360 360)"/><circle cx="360" cy="360" r="{r-46}" stroke="#E6DAC0" stroke-width="1"/>')
page('s3.html',SC+'''
.k{right:90px;top:300px}
.h{right:90px;top:345px;text-align:right;font:800 74px/1.25 TJ,MS}.h span{color:#B99A5B}
.rg{left:180px;top:600px}
.n{left:180px;width:720px;top:850px;text-align:center;font:300 190px/1 MS;letter-spacing:-4px}
.n2{left:180px;width:720px;top:1060px;text-align:center;font:500 20px MS;letter-spacing:6px;color:#B99A5B}
.t{left:110px;right:110px;top:1400px;text-align:center;font:500 40px/1.5 TJ,MS;color:#333}
.go{left:0;right:0;top:1560px;text-align:center}
''',f'''<div class="abs k"><span class="kick">NEW POST · YAS POINT</span></div>
<div class="abs h a">إطلاق جديد في ياس<br><span>انباع أغلبه</span></div>
<div class="abs rg">{ring}</div>
<div class="abs n">85%</div><div class="abs n2">OF HOMES SOLD</div>
<div class="abs t a">أكثر من {N("900")} مليون درهم مبيعات · كل الأرقام في البوست الجديد</div>
<div class="abs go a"><span class="pill" style="font-size:30px;padding:12px 30px">شوف البوست ←</span></div>''',story=True)

# S4 did-you-know: globe + 5 countries
cs=['الإمارات','المملكة المتحدة','الهند','البرازيل','هولندا']
ce=['UAE','UK','INDIA','BRAZIL','NETHERLANDS']
page('s4.html',SC+'''
.k{right:90px;top:300px}
.h{right:90px;top:345px;text-align:right;font:800 72px/1.25 TJ,MS}.h span{color:#B99A5B}
.gb{left:90px;top:620px}
.ls{right:90px;top:640px;width:430px;direction:rtl}
.it{display:flex;align-items:baseline;gap:18px;padding:20px 0;border-bottom:1px solid #EFE6D3}
.it b{font:300 40px MS;color:#B99A5B;width:50px}
.it span{font:700 38px TJ,MS}.it em{font:500 16px MS;font-style:normal;letter-spacing:3px;color:#999;margin-right:auto}
.t{left:110px;right:110px;top:1320px;text-align:center;font:500 38px/1.55 TJ,MS;color:#333}
.s{left:0;right:0;top:1560px;text-align:center;font:400 18px MS;color:#aaa}
''',f'''<div class="abs k"><span class="kick">DID YOU KNOW?</span></div>
<div class="abs h a">هل تعرف؟<br><span>المشترين جايين من كل مكان</span></div>
<div class="abs gb">{_svg(440,520,globe(220,220,190))}</div>
<div class="abs ls a">{''.join(f'<div class="it"><b>{i+1}</b><span>{a}</span><em>{e}</em></div>' for i,(a,e) in enumerate(zip(cs,ce)))}</div>
<div class="abs t a">من أعلى الجنسيات شراءً في إطلاق ذا كانوبيز سانكتشواري بجزيرة ياس</div>
<div class="abs s">Source: Aldar via The National (27 Nov 2026)</div>''',story=True)

# S5 checklist: gold side tabs
ck=['اسأل إذا المبلغ مسترد، ومتى','خذ إيصال رسمي باسم المطور','لا تحوّل لحساب شخصي أبداً','اعرف موعد الإطلاق وطريقة اختيار الوحدات','اطلب خطة الدفع وتاريخ التسليم المتوقع']
page('s5.html',SC+'''
.k{right:90px;top:300px}
.h{right:90px;top:345px;text-align:right;font:800 74px/1.25 TJ,MS}.h span{color:#B99A5B}
.rw{left:90px;right:90px;height:150px;border:1.5px solid #E6DAC0;display:flex;align-items:center;direction:rtl}
.tb{width:110px;height:100%;background:#B99A5B;color:#fff;font:300 56px MS;display:flex;align-items:center;justify-content:center;flex:none}
.tx{padding:0 34px;font:500 37px/1.4 TJ,MS;color:#222;flex:1}
.bx{width:46px;height:46px;border:2px solid #B99A5B;margin-left:34px;flex:none}
.g{left:0;right:0;top:1640px;text-align:center;font:400 18px MS;color:#aaa}
''',f'''<div class="abs k"><span class="kick">CHECKLIST</span></div>
<div class="abs h a">قبل ما تدفع<br><span>{N("EOI")} لأي مشروع</span></div>
{''.join(f'<div class="abs rw a" style="top:{640+i*186}px"><div class="tb">{i+1}</div><div class="tx">{t}</div><div class="bx"></div></div>' for i,t in enumerate(ck))}
<div class="abs g">{GEN}</div>''',story=True)

# S6 teaser post B: fanned flashcards
fc=[('EOI',-6,60,800),('SPA',0,375,740),('HANDOVER',6,690,800)]
page('s6.html',SC+'''
.k{right:90px;top:300px}
.h{right:90px;top:345px;text-align:right;font:800 76px/1.25 TJ,MS}.h span{color:#B99A5B}
.fc{width:330px;height:460px;border:1.5px solid #B99A5B;background:#fff;box-shadow:0 10px 30px rgba(185,154,91,.12);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:20px}
.fc b{font:300 40px MS;letter-spacing:2px}.fc i{width:60px;height:1px;background:#B99A5B}.fc em{font:500 18px MS;font-style:normal;letter-spacing:5px;color:#B99A5B}
.t{left:110px;right:110px;top:1460px;text-align:center;font:500 40px/1.5 TJ,MS;color:#333}
.go{left:0;right:0;top:1600px;text-align:center}
''',f'''<div class="abs k"><span class="kick">NEW POST · GLOSSARY</span></div>
<div class="abs h a">{N("5")} كلمات لازم تعرفها<br><span>قبل أي إطلاق</span></div>
{''.join(f'<div class="abs fc" style="left:{x}px;top:{y}px;transform:rotate({r}deg)"><em>OFF-PLAN</em><i></i><b>{t}</b><i></i><em>0{n}</em></div>' for n,(t,r,x,y) in zip((1,3,5),fc))}
<div class="abs t a">القاموس الكامل في البوست الجديد، احفظه</div>
<div class="abs go a"><span class="pill" style="font-size:30px;padding:12px 30px">شوف البوست ←</span></div>''',story=True)
