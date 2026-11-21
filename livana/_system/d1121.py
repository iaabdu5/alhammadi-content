from v4 import *
from art import _svg
SRC='Source: Cavendish Maxwell, Abu Dhabi residential market Q3 2026 (published 18 Nov 2026)'
ICON={'bld':'<path d="M6 42h36M10 42V16l12-8v34M22 42V14l14 6v22"/>','home':'<path d="M6 22L24 7l18 15M11 18v22h26V18"/>','trend':'<path d="M6 36l12-12 8 8 16-16"/><path d="M34 16h8v8"/>','down':'<path d="M6 14l12 12 8-8 16 16"/><path d="M34 34h8v-8"/>'}
def ic(k,s=34): return f'<svg width="{s}" height="{s}" viewBox="0 0 48 48" fill="none" stroke="#B99A5B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICON[k]}</svg>'

# ---------- Slide 1: editorial big-number (account "#1" style) ----------
page('p1.html','''
.k{right:90px;top:200px}
.h{right:90px;top:250px;text-align:right;font:800 70px/1.25 TJ}
.h span{color:#B99A5B}
.en{right:92px;top:430px;font:500 17px MS;letter-spacing:4px;color:#888;text-align:right}
.num{left:84px;top:480px;font:300 230px/1 MS;color:#B99A5B;letter-spacing:-4px}
.unit{left:96px;top:715px;font:700 34px TJ;color:#111;direction:rtl}
.side{right:90px;top:520px;width:420px;text-align:right}
.row{display:flex;justify-content:flex-end;align-items:center;gap:16px;padding:16px 0;border-bottom:1px solid #EFE6D4}
.row .t{font:700 28px TJ}.row .t small{display:block;font:500 13px MS;color:#999;letter-spacing:1px;margin-top:2px}
.row .v{font:300 40px MS;color:#B99A5B;min-width:110px;text-align:left}
.art{left:0;bottom:90px}''',
'''<div class="abs k"><span class="pill a">الربع الثالث 2026</span></div>
<div class="abs h a">سوق أبوظبي<br><span>القيمة ترتفع</span></div>
<div class="abs en">ABU DHABI RESIDENTIAL · Q3 2026</div>
<div class="abs num" dir="ltr">26.4</div>
<div class="abs unit">مليار درهم قيمة المبيعات السكنية</div>
<div class="abs side">
<div class="row"><div class="v" dir="ltr">+40%</div><div class="t a">قيمة المبيعات<small>Sales value, year on year (approx.)</small></div>'''+ic('trend')+'''</div>
<div class="row"><div class="v" dir="ltr">−7.5%</div><div class="t a">عدد الصفقات<small>Number of transactions</small></div>'''+ic('down')+'''</div>
</div>
<div class="abs art">'''+skyline(1080,400)+'''</div>
<div class="src">'''+SRC+'''</div>''')

# ---------- Slide 2: three-column stat cards with villa / towers art ----------
def card(n,u,a,e,art):
    return f'<div class="c"><div class="ar">{art}</div><div class="n" dir="ltr">{n}</div><div class="u a">{u}</div><div class="nm a">{a}</div><div class="e">{e}</div></div>'
mini_t=_svg(160,120,''.join(tower(30+i*26,110,20,40+((i*37)%60)) for i in range(4)))
mini_y=_svg(160,120,'<path d="M20 100 Q80 20 140 100"/><path d="M40 100 Q80 45 120 100" stroke="#D9C7A0"/><path d="M10 100 L150 100"/>')
mini_v=_svg(160,120,villa(14,105,0.42))
page('p2.html','''
.k{right:90px;top:210px}
.h{right:90px;top:250px;font:800 76px/1.2 TJ;text-align:right}.h span{color:#B99A5B}
.en{right:92px;top:360px;font:300 34px CG;font-style:italic;color:#888}
.cards{left:70px;right:70px;top:450px;display:flex;gap:22px}
.c{flex:1;border:1px solid #E6DAC0;padding:26px 18px 30px;text-align:center}
.c .ar{height:120px;display:flex;justify-content:center}
.c .n{font:300 92px/1 MS;color:#111;margin-top:10px}
.c .u{font:700 22px TJ;color:#B99A5B;margin-top:4px}
.c .nm{font:800 32px TJ;margin-top:14px}
.c .e{font:500 13px MS;letter-spacing:2px;color:#999;margin-top:4px}
.bar{left:70px;right:70px;top:960px;display:flex;border-top:1px solid #E6DAC0;border-bottom:1px solid #E6DAC0}
.b{flex:1;text-align:center;padding:30px 0}.b+.b{border-left:1px solid #E6DAC0}
.b .v{font:300 70px/1 MS;color:#B99A5B}.b .t{font:700 26px TJ;margin-top:8px}.b .s{font:500 13px MS;color:#999;letter-spacing:1px}''',
'''<div class="abs k"><span class="kick">WHERE THE DEALS WERE</span></div>
<div class="abs h a">وين راحت <span>الصفقات؟</span></div>
<div class="abs en cg">the most active communities</div>
<div class="abs cards">'''+card('1,200','شقة','جزيرة الريم','AL REEM ISLAND',mini_t)+card('920','شقة','جزيرة ياس','YAS ISLAND',mini_y)+card('1,070','فيلا','الحديريات','AL HUDAYRIYAT',mini_v)+'''</div>
<div class="abs bar"><div class="b"><div class="v" dir="ltr">+11%</div><div class="t a">أسعار الشقق</div><div class="s">APARTMENTS · YEAR ON YEAR</div></div><div class="b"><div class="v" dir="ltr">+8.9%</div><div class="t a">أسعار الفلل</div><div class="s">VILLAS · YEAR ON YEAR</div></div></div>
<div class="src">'''+SRC+'''</div>''')

# ---------- Slide 3: top illustration band + centered text (Sei Saadiyat style) ----------
page('p3.html','''
.art{left:0;top:150px}
.k{left:0;right:0;top:640px;text-align:center}
.h{left:0;right:0;top:680px;text-align:center;font:800 72px/1.2 TJ}.h span{color:#B99A5B}
.rule{left:390px;right:390px;top:790px;height:1px;background:#B99A5B}
.tips{left:150px;right:150px;top:830px}
.tp{display:flex;justify-content:flex-end;align-items:center;gap:22px;padding:18px 0;border-bottom:1px solid #EFE6D4;font:700 30px TJ}
.tp .no{font:300 46px MS;color:#B99A5B;width:60px;text-align:center}
.tp small{display:block;font:500 13px MS;color:#999;letter-spacing:1px;text-align:right}
.cta{left:0;right:0;top:1150px;text-align:center}''',
'''<div class="abs art">'''+louvre_scene(1080,470)+'''</div>
<div class="abs k"><span class="kick">LIVANA TAKE</span></div>
<div class="abs h a">سوق أهدأ؟ <span>اشترِ بذكاء</span></div>
<div class="abs rule"></div>
<div class="abs tips">
<div class="tp"><div class="a">قارن بآخر الصفقات المسجّلة<small>Compare with recent registered deals</small></div><div class="no">01</div></div>
<div class="tp"><div class="a">موعد التسليم والمعروض حوله<small>Handover date &amp; nearby supply</small></div><div class="no">02</div></div>
<div class="tp"><div class="a">اقرأ خطة الدفع قبل التوقيع<small>Read the payment plan first</small></div><div class="no">03</div></div>
</div>
<div class="abs cta"><span class="pill a">احجز استشارتك ←</span></div>
<div class="src">'''+SRC+'''</div>''')

# ---------- Post 2: MOU checklist, split layout with drawn contract ----------
page('q1.html','''
.k{right:90px;top:210px}
.h{right:90px;top:250px;text-align:right;font:800 78px/1.18 TJ}.h span{color:#B99A5B}
.en{right:92px;top:440px;font:600 20px MS;letter-spacing:5px;color:#111}
.en span{color:#B99A5B}
.art{left:60px;top:230px}
.list{left:90px;right:90px;top:700px}
.it{display:flex;justify-content:flex-end;align-items:center;gap:26px;padding:20px 0;border-top:1px solid #EFE6D4}
.it .no{font:300 62px/1 MS;color:#B99A5B;width:80px;text-align:center}
.it .t{font:700 32px TJ;text-align:right}.it .t small{display:block;font:500 14px MS;color:#999;letter-spacing:1px;margin-top:4px}
.note{left:90px;right:90px;top:1150px;text-align:center;font:500 26px TJ;color:#B99A5B}''',
'''<div class="abs k"><span class="kick">BUYER CHECKLIST</span></div>
<div class="abs h a">قبل ما توقّع<br><span>راجع هالـ 4</span></div>
<div class="abs en">BEFORE YOU SIGN <span>THE MOU</span></div>
<div class="abs art">'''+contract_art(420,420)+'''</div>
<div class="abs list">
<div class="it"><div class="t a">ملكية البائع موثّقة<small>Seller ownership verified</small></div><div class="no">01</div></div>
<div class="it"><div class="t a">العقار مرهون؟ رتّب فك الرهن<small>Any mortgage &amp; how it will be released</small></div><div class="no">02</div></div>
<div class="it"><div class="t a">العربون وشروط استرجاعه<small>Deposit &amp; refund terms</small></div><div class="no">03</div></div>
<div class="it"><div class="t a">موعد النقل ومن يدفع الرسوم<small>Transfer date &amp; who pays the fees</small></div><div class="no">04</div></div>
</div>
<div class="abs note a">كل اتفاق شفهي، اكتبه في العقد</div>
<div class="src">General guidance, not legal advice · احفظ المنشور</div>''')

# ---------- STORIES (all new formats) ----------
# S-A teaser post 1: tilted mini post
page('sa.html','''
.k{left:0;right:0;top:300px;text-align:center}
.h{left:0;right:0;top:350px;text-align:center;font:800 110px/1.1 TJ}
.h2{left:0;right:0;top:480px;text-align:center;font:500 44px CG;font-style:italic;color:#B99A5B}
.mini{left:200px;top:640px;width:680px;height:850px;transform:rotate(-3deg);box-shadow:0 30px 70px rgba(0,0,0,.12);border:1px solid #E6DAC0}
.cta{left:0;right:0;top:1580px;text-align:center}
.foot{bottom:90px}''',
'''<div class="abs k"><span class="kick">NEW POST</span></div>
<div class="abs h a">منشور جديد</div>
<div class="abs h2">Abu Dhabi · Q3 2026</div>
<img class="abs mini" src="out/p1.png">
<div class="abs cta"><span class="pill a">اضغط للقراءة ←</span></div>''',story=True)

# S-B glossary "word of the day"
page('sb.html','''
.k{right:100px;top:330px}
.w{right:100px;top:380px;font:300 230px/1 MS;color:#B99A5B}
.ph{right:100px;top:620px;font:500 30px CG;font-style:italic;color:#888}
.rule{right:100px;top:690px;width:120px;height:2px;background:#B99A5B}
.ar{right:100px;left:100px;top:740px;text-align:right;font:800 64px/1.3 TJ}
.d{right:100px;left:100px;top:880px;text-align:right;font:500 38px/1.7 TJ;color:#444}
.e{right:100px;left:100px;top:1170px;font:400 24px/1.6 MS;color:#999}
.art{left:0;bottom:200px}
.foot{bottom:90px}''',
'''<div class="abs k"><span class="kick">WORD OF THE DAY · مصطلح اليوم</span></div>
<div class="abs w">MOU</div>
<div class="abs ph">memorandum of understanding</div>
<div class="abs rule"></div>
<div class="abs ar a">مذكرة التفاهم</div>
<div class="abs d a">أول اتفاق مكتوب بين البائع والمشتري قبل نقل الملكية: فيه السعر، والعربون، وموعد النقل، والشروط.</div>
<div class="abs e">The first written agreement between buyer and seller before transfer: price, deposit, transfer date and conditions.</div>
<div class="abs art">'''+towers_scene(1080,420)+'''</div>''',story=True)

# S-C documents you need
page('sc.html','''
.art{left:0;top:170px}
.k{left:0;right:0;top:720px;text-align:center}
.h{left:0;right:0;top:770px;text-align:center;font:800 88px/1.15 TJ}.h span{color:#B99A5B}
.list{left:150px;right:150px;top:1000px}
.it{display:flex;justify-content:flex-end;align-items:center;gap:22px;padding:22px 0;border-bottom:1px solid #EFE6D4;font:700 36px TJ}
.it .d{width:16px;height:16px;border:2px solid #B99A5B;transform:rotate(45deg)}
.it small{display:block;font:500 16px MS;color:#999;text-align:right;letter-spacing:1px}
.foot{bottom:90px}''',
'''<div class="abs art">'''+mosque_scene(1080,520)+'''</div>
<div class="abs k"><span class="kick">BE READY</span></div>
<div class="abs h a">تبي تشتري؟<br><span>جهّز هالمستندات</span></div>
<div class="abs list">
<div class="it"><div class="a">جواز السفر والهوية<small>Passport &amp; Emirates ID</small></div><div class="d"></div></div>
<div class="it"><div class="a">إثبات القدرة المالية<small>Proof of funds</small></div><div class="d"></div></div>
<div class="it"><div class="a">موافقة التمويل المبدئية (إن وُجد)<small>Mortgage pre-approval, if financing</small></div><div class="d"></div></div>
</div>''',story=True)

# S-D teaser post 2: framed with villa art
page('sd.html','''
.k{right:100px;top:300px}
.h{right:100px;top:350px;text-align:right;font:800 104px/1.12 TJ}.h span{color:#B99A5B}
.mini{left:240px;top:640px;width:600px;height:750px;border:1px solid #E6DAC0;box-shadow:0 24px 60px rgba(0,0,0,.10)}
.fr{left:210px;top:610px;width:660px;height:810px;border:1.5px solid #C9AE77}
.cta{left:0;right:0;top:1500px;text-align:center}
.foot{bottom:90px}''',
'''<div class="abs k"><span class="kick">SAVE FOR LATER</span></div>
<div class="abs h a">احفظها<br><span>قبل ما توقّع</span></div>
<div class="abs fr"></div><img class="abs mini" src="out/q1.png">
<div class="abs cta"><span class="pill a">احفظ المنشور ←</span></div>''',story=True)
