$path = "c:\Users\user\Desktop\wpt-team\alatganti.html"
$content = Get-Content $path -Raw -Encoding UTF8

# master cyl fix
$content = $content.Replace(
    '<span class="pn">45810-KZZ-901</span></td><td>Cyl Sub Assy Frt Brake Master<span class="malay">Silinder Brek Hadapan</span></td><td><a href="https://www.bike-parts-honda-my.com/honda-motorcycle/250-MOTO/CRF/2013/CRF250LD/Frame/REAR-BRAKE-MASTER-CYLINDER/65783/F_15/2/29930" target="_blank">HONDA OEM MASTER CYLINDER SUBASSY FR. BRAKE (NISSIN)</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num">RM 218.30</td><td class="num">RM 218.30</td><td><span class="f fa">OEM_ONLY</span> <span class="f fr">SAFETY_CRITICAL</span> <span class="f fr">WRONG_PN_SUSPECTED</span> — semak 45510-KZZ-901',
    '<span class="pn">45510-KZZ-901</span></td><td>Cyl Sub Assy Frt Brake Master<span class="malay">Silinder Brek Hadapan</span></td><td><a href="https://www.bike-parts-honda-my.com/honda-motorcycle/assignment_spare_parts/45510KZZ901" target="_blank">45510KZZ901</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num">RM 141.74</td><td class="num">RM 141.74</td><td><span class="f fa">OEM_ONLY</span> <span class="f fr">SAFETY_CRITICAL</span> <span class="f fg">PN_CORRECTED</span>'
)

# zc2658 total fix
$content = $content.Replace('<td class="num">RM 3,482.76 *</td>', '<td class="num">RM 3,406.20 *</td>')
$content = $content.Replace('<div class="val">RM 3,482.76 *</div>', '<div class="val">RM 3,406.20 *</div>')

# grand total fix
$content = $content.Replace('<div class="snum">RM 18,151.49</div>', '<div class="snum">RM 18,074.93</div>')
$content = $content.Replace('<div class="val">RM 18,151.49 *</div>', '<div class="val">RM 18,074.93 *</div>')

# ZC 3735 RR LH
$content = $content.Replace('<tr><td>3</td><td><span class="pn">23037-0120</span></td><td>Lamp Assy Signal RR LH<span class="malay">Lampu Isyarat Belakang Kiri</span></td><td><a href="https://www.webike.my/ps/?keyword=23037-0120#!&p.m=955&p.c=9000" target="_blank">Webike KLX250 — 23037-0120</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num">RM 104.90</td><td class="num">RM 104.90</td><td><span class="f fa">OEM_ONLY</span> <span class="f fr">DUPLICATE_PN</span> — may be 23037-0121; verify fiche</td></tr>', '<tr><td>3</td><td><span class="pn">23037-0121</span></td><td>Lamp Assy Signal RR LH<span class="malay">Lampu Isyarat Belakang Kiri</span></td><td><a href="https://www.webike.my/ps/?keyword=23037-0121#!&p.m=955&p.c=9000" target="_blank">Webike KLX250 — 23037-0121</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num">RM 104.90</td><td class="num">RM 104.90</td><td><span class="f fa">OEM_ONLY</span> <span class="f fg">PN_CORRECTED</span></td></tr>')

# ZC 3737 RR LH
$content = $content.Replace('<tr><td>8</td><td><span class="pn">23037-0120</span></td><td>Lamp Assy Signal RR LH<span class="malay">Lampu Isyarat Belakang Kiri</span></td><td><a href="https://www.webike.my/ps/?keyword=23037-0120#!&p.m=955&p.c=9000" target="_blank">Webike KLX250 — 23037-0120</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num">RM 102.30</td><td class="num">RM 102.30</td><td><span class="f fa">OEM_ONLY</span> <span class="f fr">DUPLICATE_PN</span> — RR LH may be 23037-0121; verify fiche</td></tr>', '<tr><td>8</td><td><span class="pn">23037-0121</span></td><td>Lamp Assy Signal RR LH<span class="malay">Lampu Isyarat Belakang Kiri</span></td><td><a href="https://www.webike.my/ps/?keyword=23037-0121#!&p.m=955&p.c=9000" target="_blank">Webike KLX250 — 23037-0121</a></td><td><span class="pend">unavailable</span></td><td class="ctr">1</td><td class="num">RM 102.30</td><td class="num">RM 102.30</td><td><span class="f fa">OEM_ONLY</span> <span class="f fg">PN_CORRECTED</span></td></tr>')

# Sprockets ZC 2658
$content = $content.Replace('41201-KZZ-000</span></td><td>Sprocket Drive (MT)', '41201-KZZ-000</span></td><td>Sprocket Final Drive (MT)')
$content = $content.Replace('23801-KZZ-900</span></td><td>Sprocket Final Drive', '23801-KZZ-900</span></td><td>Sprocket Drive')

# Regex replace for Shopee links:
$content = [System.Text.RegularExpressions.Regex]::Replace($content, '<a href="https://shopee\.com\.my[^"]+" target="_blank">Shopee Anti-Counterfeit Search</a>', '<a href="https://shopee.com.my/search?keyword=Shopee+Mall+Bendix+Moto+Malaysia+Official" target="_blank">Shopee Mall — Bendix Premium</a>')

# Save file safely
[System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::UTF8)
