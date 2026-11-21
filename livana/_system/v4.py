from art import *
CSS='''@font-face{font-family:TJ;font-weight:400;src:url(tajawal-arabic-400-normal.woff2)}
@font-face{font-family:TJ;font-weight:500;src:url(tajawal-arabic-500-normal.woff2)}
@font-face{font-family:TJ;font-weight:700;src:url(tajawal-arabic-700-normal.woff2)}
@font-face{font-family:TJ;font-weight:800;src:url(tajawal-arabic-800-normal.woff2)}
@font-face{font-family:MS;font-weight:300;src:url(montserrat-latin-300-normal.woff2)}
@font-face{font-family:MS;font-weight:400;src:url(montserrat-latin-400-normal.woff2)}
@font-face{font-family:MS;font-weight:500;src:url(montserrat-latin-500-normal.woff2)}
@font-face{font-family:MS;font-weight:600;src:url(montserrat-latin-600-normal.woff2)}
@font-face{font-family:CG;font-weight:500;src:url(cormorant-garamond-latin-500-normal.woff2)}
@font-face{font-family:CG;font-weight:600;src:url(cormorant-garamond-latin-600-normal.woff2)}
@font-face{font-family:CG;font-style:italic;font-weight:500;src:url(cormorant-garamond-latin-500-italic.woff2)}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;position:relative;overflow:hidden;background:#fff;color:#111;font-family:MS;font-variant-numeric:lining-nums}
.a{font-family:TJ,MS;direction:rtl}
.abs{position:absolute}
.gold{color:#B99A5B}
.logo{position:absolute;left:64px;top:56px;height:62px}
.tag{position:absolute;left:66px;top:126px;font:500 11px MS;letter-spacing:3px;color:#666}
.tag:before{content:"";display:inline-block;width:34px;height:1px;background:#B99A5B;vertical-align:middle;margin-right:10px}
.cnr{position:absolute;width:90px;height:90px;border-color:#C9AE77;border-style:solid}
.cnr.tr{right:56px;top:56px;border-width:1.5px 1.5px 0 0}
.cnr.bl{left:56px;bottom:56px;border-width:0 0 1.5px 1.5px}
.kick{font:500 15px MS;letter-spacing:5px;color:#B99A5B}
.pill{display:inline-block;background:#B99A5B;color:#fff;font:700 22px TJ;padding:8px 22px;border-radius:4px}
.hl{height:1px;background:#E6DAC0}
.cg{font-family:CG}
.src{position:absolute;left:66px;bottom:26px;font:400 12px MS;color:#aaa}
.foot{position:absolute;right:66px;bottom:66px;display:flex;gap:26px;font:500 15px MS;color:#555;align-items:center}
.foot b{color:#B99A5B;font-weight:600}
'''
def page(name,css,body,story=False,corners=True,foot=True):
    st='body{height:1920px}' if story else ''
    c='<div class="cnr tr"></div><div class="cnr bl"></div>' if corners else ''
    f='<div class="foot"><span>livana_realestate</span><b>·</b><span>+971 50 647 5663</span></div>' if foot else ''
    open(name,'w').write(f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}{st}{css}</style></head><body>{c}<img class="logo" src="logo_black.png"><div class="tag">YOUR REAL ESTATE DESTINATION</div>{body}{f}</body></html>')
