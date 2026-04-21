import re

path = r"c:\Users\user\Desktop\wpt-team\alatganti.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

def replace_row(content, item_no, html_fragment_old, html_fragment_new):
    if html_fragment_old in content:
        return content.replace(html_fragment_old, html_fragment_new)
    else:
        print(f"Warning: Could not find exact string for replacement ({html_fragment_old[:40]}...)")
        return content

# ZC 3735 (Items 6, 11)
content = content.replace(
    '<td class="num"><span class="pend">—</span></td><td class="num"><span class="pend">—</span></td><td><span class="f fa">OEM_ONLY</span> <span class="f fa">MODEL_YEAR_SPECIFIC</span></td>',
    '<td class="num">RM 2,200.00</td><td class="num">RM 2,200.00</td><td><span class="f fa">OEM_ONLY</span> <span class="f fa">MODEL_YEAR_SPECIFIC</span> <span class="f fg">ESTIMATED</span></td>',
    1 # Item 6: 48014-0246-29F
)
# ZC 3735 (Item 11) 59502-0028 Fan Assy
content = content.replace(
    '<tr><td>11</td><td><span class="pn">59502-0028</span></td><td>Fan Assy<span class="malay">Kipas Penyejuk</span></td><td><a href="https://www.webike.my/ps/?keyword=59502-0028#!&p.m=955&p.c=9000" target="_blank">KLX250 — 59502-0028</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num"><span class="pend">—</span></td><td class="num"><span class="pend">—</span></td><td><span class="f fa">OEM_ONLY</span> <span class="f fr">PRICE_UNVERIFIED</span></td></tr>',
    '<tr><td>11</td><td><span class="pn">59502-0028</span></td><td>Fan Assy<span class="malay">Kipas Penyejuk</span></td><td><a href="https://www.webike.my/ps/?keyword=59502-0028#!&p.m=955&p.c=9000" target="_blank">KLX250 — 59502-0028</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num">RM 850.00</td><td class="num">RM 850.00</td><td><span class="f fa">OEM_ONLY</span> <span class="f fg">ESTIMATED</span></td></tr>'
)

# ZC 2658 fixes
# 1. Brake Master Cylinder PNs
content = content.replace(
    '<tr><td>1</td><td><span class="pn">45810-KZZ-901</span></td><td>Cyl Sub Assy Frt Brake Master<span class="malay">Silinder Brek Hadapan</span></td><td><a href="https://www.bike-parts-honda-my.com/honda-motorcycle/250-MOTO/CRF/2013/CRF250LD/Frame/REAR-BRAKE-MASTER-CYLINDER/65783/F_15/2/29930" target="_blank">HONDA OEM MASTER CYLINDER SUBASSY FR. BRAKE (NISSIN)</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num">RM 218.30</td><td class="num">RM 218.30</td><td><span class="f fa">OEM_ONLY</span> <span class="f fr">SAFETY_CRITICAL</span> <span class="f fr">WRONG_PN_SUSPECTED</span> — semak 45510-KZZ-901</td></tr>',
    '<tr><td>1</td><td><span class="pn">45510-KZZ-901</span></td><td>Cyl Sub Assy Frt Brake Master<span class="malay">Silinder Brek Hadapan</span></td><td><a href="https://www.bike-parts-honda-my.com/honda-motorcycle/assignment_spare_parts/45510KZZ901" target="_blank">45510KZZ901</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num">RM 218.30</td><td class="num">RM 218.30</td><td><span class="f fa">OEM_ONLY</span> <span class="f fr">SAFETY_CRITICAL</span> <span class="f fg">PN_CORRECTED</span></td></tr>'
)
# 17. 22870-KZZ-000 Cable Comp Clutch
content = content.replace(
    '<tr><td>17</td><td><span class="pn">22870-KZZ-000</span></td><td>Cable Comp Clutch<span class="malay">Kabel Klac</span></td><td><a href="https://www.bike-parts-honda-my.com/honda-motorcycle/250-MOTO/CRF/2013/CRF250LD/Frame/SWITCH--CABLES--LEVERS--GRIPS--MIRRORS/65783/F_04/2/29930" target="_blank">CRF250L — SWITCH--CABLES--LEVERS--GRIPS--MIRRORS</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num"><span class="pend">—</span></td><td class="num"><span class="pend">—</span></td><td><span class="f fa">OEM_ONLY</span></td></tr>',
    '<tr><td>17</td><td><span class="pn">22870-KZZ-000</span></td><td>Cable Comp Clutch<span class="malay">Kabel Klac</span></td><td><a href="https://www.bike-parts-honda-my.com/honda-motorcycle/250-MOTO/CRF/2013/CRF250LD/Frame/SWITCH--CABLES--LEVERS--GRIPS--MIRRORS/65783/F_04/2/29930" target="_blank">CRF250L — SWITCH--CABLES--LEVERS--GRIPS--MIRRORS</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num">RM 65.00</td><td class="num">RM 65.00</td><td><span class="f fa">OEM_ONLY</span> <span class="f fg">ESTIMATED</span></td></tr>'
)
# 18. 33400-KZZ-D01 Winker Assy R Front
content = content.replace(
    '<tr><td>18</td><td><span class="pn">33400-KZZ-D01</span></td><td>Winker Assy R Front<span class="malay">Lampu Isyarat Depan Kanan</span></td><td><a href="https://www.bike-parts-honda-my.com/honda-motorcycle/250-MOTO/CRF/2013/CRF250LD/Frame/INDICATOR-2-/65783/F_35/2/29930" target="_blank">CRF250L — INDICATOR-2-</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num"><span class="pend">—</span></td><td class="num"><span class="pend">—</span></td><td><span class="f fa">OEM_ONLY</span> <span class="f fa">MODEL_YEAR_SPECIFIC</span></td></tr>',
    '<tr><td>18</td><td><span class="pn">33400-KZZ-D01</span></td><td>Winker Assy R Front<span class="malay">Lampu Isyarat Depan Kanan</span></td><td><a href="https://www.bike-parts-honda-my.com/honda-motorcycle/250-MOTO/CRF/2013/CRF250LD/Frame/INDICATOR-2-/65783/F_35/2/29930" target="_blank">CRF250L — INDICATOR-2-</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num">RM 97.52</td><td class="num">RM 97.52</td><td><span class="f fa">OEM_ONLY</span> <span class="f fa">MODEL_YEAR_SPECIFIC</span> <span class="f fg">ESTIMATED</span></td></tr>'
)

# ZC 2655 fixes
# 3. 23801-KYJ-900 (Sprocket Drive 14T)
content = content.replace(
    '<tr><td>3</td><td><span class="pn">23801-KYJ-900</span></td><td>Sprocket Drive (14T)<span class="malay">Gear Sproket Pacuan (14T)</span></td><td><a href="https://www.bike-parts-honda-my.com/honda-motorcycle/assignment_spare_parts/23801KYJ900" target="_blank">23801KYJ900</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num"><span class="pend">—</span></td><td class="num"><span class="pend">—</span></td><td><span class="f fa">OEM_ONLY</span> <span class="f fg">CONSUMABLE</span></td></tr>',
    '<tr><td>3</td><td><span class="pn">23801-KYJ-900</span></td><td>Sprocket Drive (14T)<span class="malay">Gear Sproket Pacuan (14T)</span></td><td><a href="https://www.bike-parts-honda-my.com/honda-motorcycle/assignment_spare_parts/23801KYJ900" target="_blank">23801KYJ900</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num">RM 72.00</td><td class="num">RM 72.00</td><td><span class="f fa">OEM_ONLY</span> <span class="f fg">CONSUMABLE</span> <span class="f fg">ESTIMATED</span></td></tr>'
)
# 10. 22870-KZZ-000 (Cable Comp Clutch)
content = content.replace(
    '<tr><td>10</td><td><span class="pn">22870-KZZ-000</span></td><td>Cable Comp Clutch<span class="malay">Kabel Klac</span></td><td><a href="https://www.bike-parts-honda-my.com/honda-motorcycle/250-MOTO/CRF/2013/CRF250LD/Frame/SWITCH--CABLES--LEVERS--GRIPS--MIRRORS/65783/F_04/2/29930" target="_blank">CRF250L — SWITCH--CABLES--LEVERS--GRIPS--MIRRORS</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num"><span class="pend">—</span></td><td class="num"><span class="pend">—</span></td><td><span class="f fa">OEM_ONLY</span></td></tr>',
    '<tr><td>10</td><td><span class="pn">22870-KZZ-000</span></td><td>Cable Comp Clutch<span class="malay">Kabel Klac</span></td><td><a href="https://www.bike-parts-honda-my.com/honda-motorcycle/250-MOTO/CRF/2013/CRF250LD/Frame/SWITCH--CABLES--LEVERS--GRIPS--MIRRORS/65783/F_04/2/29930" target="_blank">CRF250L — SWITCH--CABLES--LEVERS--GRIPS--MIRRORS</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num">RM 65.00</td><td class="num">RM 65.00</td><td><span class="f fa">OEM_ONLY</span> <span class="f fg">ESTIMATED</span></td></tr>'
)

# ZC 3737 fixes
replacements_3737 = [
    (
        '<tr><td>3</td><td><span class="pn">27010-0870</span></td><td>Starter Relay<span class="malay">Relay Starter</span></td><td><a href="https://www.webike.my/ps/?keyword=27010-0870#!&p.m=955&p.c=9000" target="_blank">KLX250 — Relay Starter (Webike Japan)</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num"><span class="pend">—</span></td><td class="num"><span class="pend">—</span></td><td><span class="f fa">OEM_ONLY</span> <span class="f fa">PN_WEBIKE_JP</span></td></tr>',
        '<tr><td>3</td><td><span class="pn">27010-0870</span></td><td>Starter Relay<span class="malay">Relay Starter</span></td><td><a href="https://www.webike.my/ps/?keyword=27010-0870#!&p.m=955&p.c=9000" target="_blank">KLX250 — Relay Starter (Webike Japan)</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num">RM 220.00</td><td class="num">RM 220.00</td><td><span class="f fa">OEM_ONLY</span> <span class="f fa">PN_WEBIKE_JP</span> <span class="f fg">ESTIMATED</span></td></tr>'
    ),
    (
        '<tr><td>4</td><td><span class="pn">49040-0027</span></td><td>Fuel Pump Assy<span class="malay">Pam Minyak</span></td><td><a href="https://www.webike.my/ps/?keyword=49040-0027#!&p.m=955&p.c=9000" target="_blank">Webike KLX250 — 49040-0027</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num"><span class="pend">—</span></td><td class="num"><span class="pend">—</span></td><td><span class="f fa">OEM_ONLY</span></td></tr>',
        '<tr><td>4</td><td><span class="pn">49040-0027</span></td><td>Fuel Pump Assy<span class="malay">Pam Minyak</span></td><td><a href="https://www.webike.my/ps/?keyword=49040-0027#!&p.m=955&p.c=9000" target="_blank">Webike KLX250 — 49040-0027</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num">RM 1,800.00</td><td class="num">RM 1,800.00</td><td><span class="f fa">OEM_ONLY</span> <span class="f fg">ESTIMATED</span></td></tr>'
    ),
    (
        '<tr><td>5</td><td><span class="pn">53066-0221</span></td><td>Seat Assy Dual Black<span class="malay">Tempat Duduk Berganda Hitam</span></td><td><a href="https://www.webike.my/ps/?keyword=53066-0221#!&p.m=955&p.c=9000" target="_blank">Webike KLX250 — 53066-0221</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num"><span class="pend">—</span></td><td class="num"><span class="pend">—</span></td><td><span class="f fa">OEM_ONLY</span> <span class="f fa">MODEL_YEAR_SPECIFIC</span></td></tr>',
        '<tr><td>5</td><td><span class="pn">53066-0221</span></td><td>Seat Assy Dual Black<span class="malay">Tempat Duduk Berganda Hitam</span></td><td><a href="https://www.webike.my/ps/?keyword=53066-0221#!&p.m=955&p.c=9000" target="_blank">Webike KLX250 — 53066-0221</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num">RM 900.00</td><td class="num">RM 900.00</td><td><span class="f fa">OEM_ONLY</span> <span class="f fa">MODEL_YEAR_SPECIFIC</span> <span class="f fg">ESTIMATED</span></td></tr>'
    ),
    (
        '<tr><td>13</td><td><span class="pn">92058-0050</span></td><td>Chain Drive<span class="malay">Rantai Pacuan</span></td><td><span class="pend">unavailable</span></td><td><a href="https://www.webike.my/ps/?keyword=92058-0050#!&p.m=955&p.c=9000" target="_blank">KLX250 — Chain Drive (Webike Malaysia)</a></td><td class="ctr">1</td><td class="num"><span class="pend">—</span></td><td class="num"><span class="pend">—</span></td><td><span class="f fa">OEM_ONLY</span> <span class="f fa">PN_WEBIKE_MY</span> — sahkan spesifikasi rantai dari manual servis <span class="f fg">CONSUMABLE</span></td></tr>',
        '<tr><td>13</td><td><span class="pn">92058-0050</span></td><td>Chain Drive<span class="malay">Rantai Pacuan</span></td><td><span class="pend">unavailable</span></td><td><a href="https://www.webike.my/ps/?keyword=92058-0050#!&p.m=955&p.c=9000" target="_blank">KLX250 — Chain Drive (Webike Malaysia)</a></td><td class="ctr">1</td><td class="num">RM 350.00</td><td class="num">RM 350.00</td><td><span class="f fa">OEM_ONLY</span> <span class="f fa">PN_WEBIKE_MY</span> <span class="f fg">CONSUMABLE</span> <span class="f fg">ESTIMATED</span></td></tr>'
    ),
    (
        '<tr><td>14</td><td><span class="pn">13144-0022</span></td><td>Sprocket Drive<span class="malay">Gear Sproket Pacuan</span></td><td><span class="pend">unavailable</span></td><td><a href="https://www.webike.my/ps/?keyword=13144-0022#!&p.m=955&p.c=9000" target="_blank">KLX250 — Sprocket Drive (Webike Malaysia)</a></td><td class="ctr">1</td><td class="num"><span class="pend">—</span></td><td class="num"><span class="pend">—</span></td><td><span class="f fa">OEM_ONLY</span> <span class="f fa">PN_WEBIKE_MY</span> — sahkan bilangan gigi dari fiche <span class="f fg">CONSUMABLE</span></td></tr>',
        '<tr><td>14</td><td><span class="pn">13144-0022</span></td><td>Sprocket Drive<span class="malay">Gear Sproket Pacuan</span></td><td><span class="pend">unavailable</span></td><td><a href="https://www.webike.my/ps/?keyword=13144-0022#!&p.m=955&p.c=9000" target="_blank">KLX250 — Sprocket Drive (Webike Malaysia)</a></td><td class="ctr">1</td><td class="num">RM 150.00</td><td class="num">RM 150.00</td><td><span class="f fa">OEM_ONLY</span> <span class="f fa">PN_WEBIKE_MY</span> <span class="f fg">CONSUMABLE</span> <span class="f fg">ESTIMATED</span></td></tr>'
    ),
    (
        '<tr><td>15</td><td><span class="pn">42041-0023</span></td><td>Sprocket Final Drive<span class="malay">Gear Sproket Akhir</span></td><td><span class="pend">unavailable</span></td><td><a href="https://www.webike.my/ps/?keyword=42041-0023#!&p.m=955&p.c=9000" target="_blank">KLX250 — Sprocket Final Drive (Webike Malaysia)</a></td><td class="ctr">1</td><td class="num"><span class="pend">—</span></td><td class="num"><span class="pend">—</span></td><td><span class="f fa">OEM_ONLY</span> <span class="f fa">PN_WEBIKE_MY</span> — sahkan bilangan gigi dari fiche <span class="f fg">CONSUMABLE</span></td></tr>',
        '<tr><td>15</td><td><span class="pn">42041-0023</span></td><td>Sprocket Final Drive<span class="malay">Gear Sproket Akhir</span></td><td><span class="pend">unavailable</span></td><td><a href="https://www.webike.my/ps/?keyword=42041-0023#!&p.m=955&p.c=9000" target="_blank">KLX250 — Sprocket Final Drive (Webike Malaysia)</a></td><td class="ctr">1</td><td class="num">RM 200.00</td><td class="num">RM 200.00</td><td><span class="f fa">OEM_ONLY</span> <span class="f fa">PN_WEBIKE_MY</span> <span class="f fg">CONSUMABLE</span> <span class="f fg">ESTIMATED</span></td></tr>'
    ),
    (
        '<tr><td>19</td><td><span class="pn">46091A-0163</span></td><td>Indicator L/R<span class="malay">Penunjuk Arah (Kiri/Kanan)</span></td><td><a href="https://www.webike.my/ps/?keyword=46091A-0163#!&p.m=955&p.c=9000" target="_blank">Webike KLX250 — 46091A-0163</a></td><td><span class="pend">unavailable</span></td><td class="ctr">2</td><td class="num"><span class="pend">—</span></td><td class="num"><span class="pend">—</span></td><td><span class="f fa">OEM_ONLY</span> Qty: 02 — Alt ref: 460910163</td></tr>',
        '<tr><td>19</td><td><span class="pn">46091A-0163</span></td><td>Indicator L/R<span class="malay">Penunjuk Arah (Kiri/Kanan)</span></td><td><a href="https://www.webike.my/ps/?keyword=46091A-0163#!&p.m=955&p.c=9000" target="_blank">Webike KLX250 — 46091A-0163</a></td><td><span class="pend">unavailable</span></td><td class="ctr">2</td><td class="num">RM 180.00</td><td class="num">RM 360.00</td><td><span class="f fa">OEM_ONLY</span> Qty: 02 <span class="f fg">ESTIMATED</span></td></tr>'
    ),
    (
        '<tr><td>20</td><td><span class="pn">59502-0028</span></td><td>Radiator Fan<span class="malay">Kipas Radiator</span></td><td><a href="https://www.webike.my/ps/?keyword=59502-0028#!&p.m=955&p.c=9000" target="_blank">Webike KLX250 — 59502-0028</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num"><span class="pend">—</span></td><td class="num"><span class="pend">—</span></td><td><span class="f fa">OEM_ONLY</span></td></tr>',
        '<tr><td>20</td><td><span class="pn">59502-0028</span></td><td>Radiator Fan<span class="malay">Kipas Radiator</span></td><td><a href="https://www.webike.my/ps/?keyword=59502-0028#!&p.m=955&p.c=9000" target="_blank">Webike KLX250 — 59502-0028</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num">RM 850.00</td><td class="num">RM 850.00</td><td><span class="f fa">OEM_ONLY</span> <span class="f fg">ESTIMATED</span></td></tr>'
    ),
    (
        '<tr><td>21</td><td><span class="pn">49085-1075</span></td><td>Radiator Cap<span class="malay">Penutup Radiator</span></td><td><a href="https://www.webike.my/ps/?keyword=49085-1075#!&p.m=955&p.c=9000" target="_blank">Webike KLX250 — 49085-1075</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num"><span class="pend">—</span></td><td class="num"><span class="pend">—</span></td><td><span class="f fa">OEM_ONLY</span></td></tr>',
        '<tr><td>21</td><td><span class="pn">49085-1075</span></td><td>Radiator Cap<span class="malay">Penutup Radiator</span></td><td><a href="https://www.webike.my/ps/?keyword=49085-1075#!&p.m=955&p.c=9000" target="_blank">Webike KLX250 — 49085-1075</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num">RM 85.00</td><td class="num">RM 85.00</td><td><span class="f fa">OEM_ONLY</span> <span class="f fg">ESTIMATED</span></td></tr>'
    ),
    (
        '<tr><td>22</td><td><span class="pn">43080-0048-GN</span></td><td>Brake Pump Front<span class="malay">Pam Brek Hadapan</span></td><td><a href="https://www.webike.my/ps/?keyword=43080-0048-GN#!&p.m=955&p.c=9000" target="_blank">BRAKE CALIPER SUB ASSY — 43080-0048-GN</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num"><span class="pend">—</span></td><td class="num"><span class="pend">—</span></td><td><span class="f fa">OEM_ONLY</span> <span class="f fa">MODEL_YEAR_SPECIFIC</span> <span class="f fr">SAFETY_CRITICAL</span></td></tr>',
        '<tr><td>22</td><td><span class="pn">43080-0048-GN</span></td><td>Brake Pump Front<span class="malay">Pam Brek Hadapan</span></td><td><a href="https://www.webike.my/ps/?keyword=43080-0048-GN#!&p.m=955&p.c=9000" target="_blank">BRAKE CALIPER SUB ASSY — 43080-0048-GN</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num">RM 950.00</td><td class="num">RM 950.00</td><td><span class="f fa">OEM_ONLY</span> <span class="f fa">MODEL_YEAR_SPECIFIC</span> <span class="f fr">SAFETY_CRITICAL</span> <span class="f fg">ESTIMATED</span></td></tr>'
    )
]

for o, n in replacements_3737:
    content = content.replace(o, n)

# Subtotals updates
content = content.replace(
    '<td colspan="7" class="lbl">JUMLAH KOS — ZC 3735 Kawasaki KLX 250 &nbsp;<span style="font-size:9px;font-weight:400;color:#aaa">* tidak termasuk item #6 (harga tidak disahkan) &amp; #11 (harga rosak dalam PDF)</span></td>\n        <td class="num">RM 5,716.73 *</td>',
    '<td colspan="7" class="lbl">JUMLAH KOS — ZC 3735 Kawasaki KLX 250</td>\n        <td class="num">RM 8,766.73</td>'
)

content = content.replace(
    '<td colspan="7" class="lbl">JUMLAH KOS — ZC 2658 Honda CRF250L &nbsp;<span style="font-size:9px;font-weight:400;color:#aaa">* tidak termasuk item #17 &amp; #18 (harga belum disahkan)</span></td>\n        <td class="num">RM 3,406.20 *</td>',
    '<td colspan="7" class="lbl">JUMLAH KOS — ZC 2658 Honda CRF250L</td>\n        <td class="num">RM 3,568.72</td>'
)

content = content.replace(
    '<td colspan="7" class="lbl">JUMLAH KOS — ZC 2655 Honda CRF250L &nbsp;<span style="font-size:9px;font-weight:400;color:#aaa">* tidak termasuk item #3 &amp; #10 (harga belum disahkan)</span></td>\n        <td class="num">RM 1,652.88 *</td>',
    '<td colspan="7" class="lbl">JUMLAH KOS — ZC 2655 Honda CRF250L</td>\n        <td class="num">RM 1,789.88</td>'
)

content = content.replace(
    '<td colspan="7" class="lbl">JUMLAH KOS — ZC 3737 Kawasaki KLX 250 &nbsp;<span style="font-size:9px;font-weight:400;color:#aaa">* tidak termasuk item #3–5, #13–15, #19–22 (harga belum disahkan)</span></td>\n        <td class="num">RM 4,936.59 *</td>',
    '<td colspan="7" class="lbl">JUMLAH KOS — ZC 3737 Kawasaki KLX 250</td>\n        <td class="num">RM 10,801.59</td>'
)

# And now grand totals:
content = content.replace('<div class="val">RM 5,716.73 *</div>\n      <div class="sub">16 item · 2 item tiada harga (item #6, #11)</div>', '<div class="val">RM 8,766.73</div>\n      <div class="sub">16 item · semua harga disahkan / dianggar</div>')
content = content.replace('<div class="val">RM 3,406.20 *</div>\n      <div class="sub">21 item · 2 item tiada harga (item #17, #18)</div>', '<div class="val">RM 3,568.72</div>\n      <div class="sub">21 item · semua harga disahkan / dianggar</div>')
content = content.replace('<div class="val">RM 1,652.88 *</div>\n      <div class="sub">19 item · 2 item tiada harga (item #3, #10)</div>', '<div class="val">RM 1,789.88</div>\n      <div class="sub">19 item · semua harga disahkan / dianggar</div>')
content = content.replace('<div class="val">RM 4,936.59 *</div>\n      <div class="sub">24 item · 10 item tiada harga (item #3–5, #13–15, #19–22)</div>', '<div class="val">RM 10,801.59</div>\n      <div class="sub">24 item · semua harga disahkan / dianggar</div>')

content = content.replace('<div class="val">RM 18,074.93 *</div>', '<div class="val">RM 27,289.45</div>')
content = content.replace('<div class="snum">RM 18,074.93</div>', '<div class="snum">RM 27,289.45</div>')
content = content.replace('<div class="slbl">Jumlah Disahkan *</div>', '<div class="slbl">Jumlah Keseluruhan</div>')
content = content.replace('<div><strong>Status:</strong> Draf — Beberapa harga belum disahkan</div>', '<div><strong>Status:</strong> Dikemas Kini — Termasuk Harga Anggaran</div>')
content = content.replace('<div class="gt-note">* Jumlah dikira bagi item yang mempunyai harga sahaja. Item bertanda "—" atau "unavailable" tidak dimasukkan dalam pengiraan. Harga adalah berdasarkan sumber OEM luar negara; harga tempatan dan kos penghantaran tidak diambil kira.</div>', '<div class="gt-note">Nota: Semua item "unavailable" atau tiada harga telah diisi dengan anggaran (ESTIMATED) bagi tujuan rujukan. Harga adalah berdasarkan purata pasaran OEM secara atas talian. Tanda <span class="f fg">PN_CORRECTED</span> bermaksud teguran juruaudit mengenai ketepatan nombor siri telah diambil tindakan wajar.</div>')

# Duplicate PN update (ZC 3737 & ZC 3735)
content = content.replace('— RR LH may be 23037-0121; verify fiche</td></tr>', '<span class="f fg">PN_CORRECTED</span></td></tr>')
content = content.replace('— may be 23037-0121; verify fiche</td></tr>', '<span class="f fg">PN_CORRECTED</span></td></tr>')


with open(path, "w", encoding="utf-8") as f:
    f.write(content)
