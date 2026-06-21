<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn5.telesco.pe/file/b286uuEr2HykUh3sspM44DvyTD6wkTz7WRqs9UvE78b9WurSwgm2DRO_5fI-NKln9enchnkccnOAmFsZZt4lHg6nb98uWwQgxuXKb0SjOhC5rZLZlVGqNWbifBg7cW-uMLeDF6CIEDIfkOYWmuHit4T8oWfvpkYfTgae3HO4sRoxxclLNdzpGJdy0yCxIMKPyOGlhRashMCR5_gnVkSIb2xC3o9KpJDMOWbg_e0ytexBJhgpltLF2O1WtaRNLuYDK7Pi0TdelIK-PIksolR3HsD2jfiAcV8wnqNKaFE70XP0JulAf2bEbbi40z6ozSOh_8_yBi9hAD6gAJ_AmUCArg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 690K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 06:21:08</div>
<hr>

<div class="tg-post" id="msg-94827">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lgf0P2MXBTIddTlYoERRtQhy2XIemmi_L8qPne2vwdLlEjbBO_jzls9EIVIUj2gDPONbuY8gPTxYden9Cgxg-nQwecQL2rPPkk-Mnv616XFDYXsZw7SKcl89K1GsWe9B8tejT7aq-JT-pvn_-P7C68SJ_OIiHf5lJzW3LaTQVND0T7HbXjB93WJf9gl__dC0jmy4_ALr0Bd28ZZnzraFKYLcbWDFCoE8uvfB0AiTFNNkEZ6x6qoEEXCi_cgvLaMraeyYyyaGTP0KI0XdX08HQVd7Z-YiqkXkLFruNeL9zXaE_6fTyeMHhDDCQof-yYfEblpTzhOzqc9FHQ2qXtUzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇯🇵
ترکیب ژاپن‌مقابل تونس؛ ساعد ۷:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/Futball180TV/94827" target="_blank">📅 06:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94826">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bvt2lkd-XA7fuQ4ykozg2KxraGsn5L_pjAGKNp3UIJUT3ABKZxmkeGBFOUr4EbATJB7IJwF4J06uZLiHQxVo_ziy8jNPn3juFusM8zTRw8kGbMGAm1XTNC6o6WoiYLLvxxTnG49qp6vVbGpFWMzzm1siJWMg_9O6kJt1NFbjK1j92kAKdduf2nZROh6VoYQXXTsGEnHvJ4M9hk7oXwSMzZpsq3Of0Wlt2N9Kwdsx4knl6extFuiAdd_PbaemfvJTFIPwzxU1EKiWU9ByIicmiKoVR0ZLrPmsGCyl5C6anzJ8BIvEL3lk-8y3-i55xpp42WkRUFV_sUevqFgo8GtJhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇹🇳
ترکیب‌تیم‌ملی تونس مقابل ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/Futball180TV/94826" target="_blank">📅 06:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94825">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzcpvDLFVteFG_OyEwja1SSiKN-Rij7tyNJSR7Bt2Lkq_szTmNLSs2gzHoo7Wyh2NCs3m3wxEIUQcv924ESUicWMSffI6O9lzsmg--PKlH_gsf1mgtA7RKpK3mQpXnN1jeV97Fbov3CO4RXzZ6i4FYIisNnpEY0wE976-uDFS0Xcifqz2qIh7tSNSVSvUqayv_RPvaODnvVoqGCNlgr44qIqqWTNCn2boQ4-5MSHybHgTcQlM4Bbax0nnNzRvSQm9YlbxnQFnW4zvtgWuC3uysW5Nag5i4yMfHa1avv5vKyBpUgSuMeo2Ayd-o0n0RVg-WpDEOaVUEJCDkDLcnK3bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
کم‌جمعیت‌ترین کشورهای جهان که در جام جهانی امتیاز کسب کرده‌اند:
‏کوراسائو (۱۹۳ هزار نفر) مقابل اکوادور در سال ۲۰۲۶.
‏ایسلند (۳۳۰ هزار نفر) مقابل آرژانتین در سال ۲۰۱۸.
‏کیپ ورد (۴۹۰ هزار نفر) مقابل اسپانیا در سال ۲۰۲۶.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/Futball180TV/94825" target="_blank">📅 05:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94823">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BHtRsiwMLj18sOsnWg6prsFHQi3KsgHAEfaZA7XbMTw0e9kuV6alMvpudKZ9Q1zGmO8yLshPjnb9dbaDYgzr1cwlZR_T5DttpYh0tcMfQn50Tax7-tON0tV-LqtTtQj73HWx3ZJSHZEbkfFDa03a5k-NB_GXJK_BTbybykaDnbpLkyYVgWnnTwnVIdSKGsoOXuRHQBpT94rdLu_-Jfcn38uaatEcls4fdYWgMyCYJOYMkcNhDa1K281yE9LANiQhEPay9KhA2hyzXkkUWjoWJwgaQvoY-lqw9L_xSLQlJ2JllL5VmxcS6-Nei1Lj_FtDmO660U_pPC0t9cVu9URZ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EB2X7HJXmmPstN0C5SwgF3PcLGNOOD5uXasp4xgfNf5o9LZQDsnWcG4HdA20dFeYFeAcZdeXAHCb7RbhUhuDfJh3BcvuE6XlsLnpQsdj6KaRgQf2MTHp2h8wgDLWBa1FCsMJboL0wxYRkIjYCk0WzQzivV1QOQTjPSWf3sOGjipUQEYgaxAHAcauo1JhP3dcnCAhSwKa4yvUBGkCdtQFZ-prUtIDz-UPBcqYxHWIcIpHrc3JuyRlJ217aeIpchyQ2IbcotFjAG34x9pHWibBJlqGcyBJfZxCgDcTGqq-qEECWKl92_pPzvPOF00lymZtjqKYFeXfYsrR8PTj8-7HWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در عرض چند دقیقه 300 هزار فالوور به پیج اینستاگرام دروازبان کوراسائو اضافه شد
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/Futball180TV/94823" target="_blank">📅 05:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94822">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9LojSjxuD1gfoZDtv-PdLjlUjYQcBtZibtSVMnZXu7aZyyMA6lQlX56RiiZTyq9shxui5ZDFZAf-j7UkPnKOcAQYFRRvyIWcGY2wdTFyxtm7gF0idgO5LIjYAxM646TWDqCNQvWJgfU7zaLeLJdKuVlTHkr3IZG3cr8RsRMAxYQ6XbaPHyjFIENRlFqjRBQBz2vPZe0fGa8a_1nJVHf6OHmpPtL713cLMg6FQYNdKRmTRzqL7riGlyS1OEhdWuwGLR3dTNJLrCymswEraP07_UCPYpbMnVt20V7lLZv0r1g15obit1PnAHxEabR6dPreltYNVB2M8YIeJ2CQY5DZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
همچنان شگفتی‌های جام جهانی ادامه داره..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/Futball180TV/94822" target="_blank">📅 05:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94821">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lII8kPWu78rFmboqs4W8_8n1lsYM8qMI8DMaYablmmq91JJe_ahgikgpjFXbVTDKueTIpAygfRvkYRp76MAv6AjuTvAcGb8bDFfLDkoFRc5Vv_-w6gL3a2CWCcCyYLW6y31McMGuEEmGDV07IpJbWfT44ORHertIfXtDJoAnvItI0z1-SNCcFVdKDa9mL68URCmJhPEg0NxZddFEjoV8iuNV8egmB-IT7daPPozwvRn6ncBMdfwqQsV4flvwcdFU2d3DsSgY6_kPMZejyPZN9RdSz1eBQ_XAN9oWfL3YE9cMNuHbI6BjTOwreBCEJaKPszmUKzto0MBOQegJreIgWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این آمار هنوز بازی گل نداشته
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/Futball180TV/94821" target="_blank">📅 05:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94820">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2GgLtM8VS4sDqRGBjZd8wTJ_0Z1V2kJZ7zjcVF56umrbEEb-YbGeaeg9KU_E1v8LFqgwwdp3ZmzwCBkr-GehGyG03OYInSk8Ls85fHyHM_ISRz0Nz1Z9Hf7PORwe27aCwxtt9zRVJAuu5F_kw5nafM5RZpCsIJd0Sy2InKwNZu4HO8saZafWGENcP2CEQfkhVZBp-y-h0jkeBLCCkAAB1xoaYw3Bsj7c0c5ThiytC3xO81g0drIck-t0bzJ0SuJT2TpHEA6865o3UxHxBvsHOzwlzMtbNpBtbG0U_4gMHQGYZQtMnP-2LOhEIvOkSt9x1J9XZJmfXDA_c_1HMrkEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
جدول گروه E مسابقات جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/Futball180TV/94820" target="_blank">📅 05:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94819">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">با این آمار هنوز بازی گل نداشته
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/Futball180TV/94819" target="_blank">📅 05:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94818">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vfm7DEl6Nl5Kb42LfVF4PJCPGcAPDI2THIVhCs97WvfFW4DRch_-TzhyEU_0ziCLq-TBGVrSENI3Is1ZpgU2Flp7DPgh4AqZO3MU5gpPYL7eJIXjrpH8IToCy0WepDq4uMwZAKv8dxTpmj1PzgGG7GRqTAr8NVocuRqkizLLOEicFEPLLyhTA4ls_ise3o4WpQLLsCOnk2ivjG3_ToVpavURFT-Ev1u_EafXYb820BmdmA00J8jczaiN-BsFDP2j0PF3zyd4mExJB4jfGvoEgcZbg6STFZxGQJt1yytKPwvdJ8F7X1bbG6bwPPEu6XY1b1km2LgOV0CCkCJgkIHGkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این آمار هنوز بازی گل نداشته
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/Futball180TV/94818" target="_blank">📅 05:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94817">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4DRNwAtldCQeawdJXiDaT9Mf-C9xJmsxjfxy-gpYgEDwME6gOETQPCrLBFRMb0cVI6UxIFOhs5oh0XsG7UDBBY7V6l65WgNdbfB5ZAKkDCYI8d__2zIQiooOKcy-SdlBhdu6TrirdNgdoBWHP-2yxNwrblDOzmOsSrBtxlPf795_c-Ctax1wRhDp2eKKIziKMXBbn8F2HJOc21uQVswcuKTNDg_UUb7_j5HySA70b2FkGbYpYHVR_9kE6wvVn3FdhSuHooG8Ua_dZ0o0nA1f57T9q5KNEFp5Nl1l_nw5Z92wsYOdE5FHptfKLEE0a5waa3XjRM1PnFRsCklTXflNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
🇹🇳
استادیوم محل برگزاری بازی ژاپن - تونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/Futball180TV/94817" target="_blank">📅 04:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94816">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgwuqRJOc76yq3oulcPzkg4sFZ2KPDP59NcHpeJinoXlHTHUATOawv_eVzzWwBtqUj3zVi9_U4MvOls4RSHz3vGCgfEsuu5pIWVTz7bPqCmmVw4Jc6XDjZhOqtPavuTRs3hx1udJckwjyXmnfsGnTa7ZkaxapqC5o7X0RYsGJzTjUmXFDzGxyxb3PgrvB4KKTUJhSaOxnbFdMyqPGYxkBfV1gDEwr83rn61MrMYCa1H1aYTLw8U8xG-3nE48s7t_-yC4z1_vSDcOWwA9H5VmHM1JumKTsOvzhacjCDiKcRYdkyF4d1kpvNVYXAC6OcVbtO36WlDIcriIMu7f6-U3zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
#فورییییییی
از رومانو:
⚪️
رئال مادرید قصد داره رائول آسنسیو رو در این تابستون بفروشه و ژوزه مورینیو
هم موافقت خودشو اعلام کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/Futball180TV/94816" target="_blank">📅 04:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94815">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نیمه دوم بازی کوراسائو و اکوادور شروع شد.</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/Futball180TV/94815" target="_blank">📅 04:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94814">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97542a60bc.mp4?token=KrJy2hWUXxwjic1G3zOUDQ3K6S6dWHRoHRlqr71KisWbimfXdfkNQHV92TITY_lNgId7HS5E3Qg-4gbXiw_TLE-FgcZ2nBQAEdjHUf31eKJZKDAJ2vfSqz1Hytxnyg4-MXEWGlM2Hie63dyWHRZh3WjXkIyLB6-gfIb1RplM1_QyiRu758UNzhNsaYK5CrAAYd5yaknMsJXdjxPBUmhbaXmFqvjm1per_c9g5MruJf5ZBsWzp1nDmgYMq3wdk3B-uj9sFr6X4Lm4Wjvu4iqCdL81GFoXVuAwjsFykQOn9n8gsmW5h5Xdqx0wwD2w4xCboQOWQQWGpjxhsPnDcHQbRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97542a60bc.mp4?token=KrJy2hWUXxwjic1G3zOUDQ3K6S6dWHRoHRlqr71KisWbimfXdfkNQHV92TITY_lNgId7HS5E3Qg-4gbXiw_TLE-FgcZ2nBQAEdjHUf31eKJZKDAJ2vfSqz1Hytxnyg4-MXEWGlM2Hie63dyWHRZh3WjXkIyLB6-gfIb1RplM1_QyiRu758UNzhNsaYK5CrAAYd5yaknMsJXdjxPBUmhbaXmFqvjm1per_c9g5MruJf5ZBsWzp1nDmgYMq3wdk3B-uj9sFr6X4Lm4Wjvu4iqCdL81GFoXVuAwjsFykQOn9n8gsmW5h5Xdqx0wwD2w4xCboQOWQQWGpjxhsPnDcHQbRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کابوس کوین دیبروینه شب قبل از بازی با ایران
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/Futball180TV/94814" target="_blank">📅 04:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94813">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اینقدر بازی جذاب بود نفهمیدیم کی نیمه اولش تموم شد.</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/Futball180TV/94813" target="_blank">📅 04:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94812">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436443b2d6.mp4?token=Scsq-xSeFL3RIq554MqMsTG24-9s0fJAwGhJaSjCyMAjpu-Xk2O2RYnlvSl5RbYM3nmuOuQ6EHJQ38Rf1_XeaKxP_tQW8WEr3-ie2J3jD-1mdOQtlPrR9hb6F655MWXc-W-1DoQCGYIjgmX7uS60CMHibC-Q93-IHnAdljaJvn2vNOIToH_gKBx97uaXGrJHp9AFeFkH6P-YwTOcFypmcGcWWaml0Gw19NUEm7-W7qkk47D802aLN-B5daaCLvD2Pw-9RCYuoDy0nGPdhYpSmMHxiOS3to9eC3oyQRRcR9QyKNLHoDkMYZ2e53HmHLwl44288CGHUqhvGMfbzI9LDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436443b2d6.mp4?token=Scsq-xSeFL3RIq554MqMsTG24-9s0fJAwGhJaSjCyMAjpu-Xk2O2RYnlvSl5RbYM3nmuOuQ6EHJQ38Rf1_XeaKxP_tQW8WEr3-ie2J3jD-1mdOQtlPrR9hb6F655MWXc-W-1DoQCGYIjgmX7uS60CMHibC-Q93-IHnAdljaJvn2vNOIToH_gKBx97uaXGrJHp9AFeFkH6P-YwTOcFypmcGcWWaml0Gw19NUEm7-W7qkk47D802aLN-B5daaCLvD2Pw-9RCYuoDy0nGPdhYpSmMHxiOS3to9eC3oyQRRcR9QyKNLHoDkMYZ2e53HmHLwl44288CGHUqhvGMfbzI9LDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دیگو دالوت در حمایت از رونالدو: "فکر می‌کنم دیگه همه بدون کریستیانو چقدر توی کنار اومدن با انتقادها مهارت داره."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/Futball180TV/94812" target="_blank">📅 03:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94811">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n62tgVPJM_6IVy9I-Kzn3ChA1tdDXp6Kg15GnL8pcAzJ-o-lGQ5NHbuWKt2Aev38l9DMCDtk-Il1rSFgz03ywSLQk0Kh218OGMFDO-4kjWBNJqbplx5aQdhxvw6gaXlbLHhrTeAMjGM8XHi05Agef7sCXnUe7rv0GajOPK0QRSIAX6BK3NXWBqWfVUr-hHQZEP-rpst4brwyudOcnVY2pYRTS7WAML1ct4aY5LSvUOuWh7DHpsb0PO_U1DqlXOJBUdsPcz9P16mGpDF_nWPWqJEsCVrSAoVXLtstyKr0mjVxOINH8TKaQcO5hGqaj5uRXx9jX4a4lczhx_8kG4jIZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این رفیقتون بازم اومده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/Futball180TV/94811" target="_blank">📅 03:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94810">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOikkW3E5Mau0Lw3L8RbS8DtCrZj_D0yTbO23ltTTbdrz1DbAdfRxcsb7GrVkBtpr3AsxrgT4kedIfGiF-ksz5PJCaiy6m3j1c5v7t6RaKJjo9ub1tGj7QVeL3zNsnriTGFei31AnB25NShDeBeEBpznqpRzezRFM6I1-Ps6DHrrDT_K19mk2cwV-IMxlZWXftOU9xsHlPVyA0cI3dM9PjMDlQqTKyg6eYvoyKGI3-6Ne5D36yJ7VdFPvfKoKYWnLxoTWSE3gxvL3YufrHAWg83-5IdzR9OTmCKrESqmPVhn9d81TnaKfSMQLqITvXDiMKRgDoZgGwmK1LonSxKYIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دنیز اونداو به عنوان بهترین بازیکن دیدار آلمان و ساحل عاج انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/Futball180TV/94810" target="_blank">📅 03:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94809">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOM6gywXtEQhMS6bLZyb5Qa8knE2Z3aqHFq4VzJ-wwc0MSU-Ad1FKsMZ7i4emGeVBrWMEc-DvIcMWCYNriK1iLZQG9j48nUw9hRRhcea9LZA5dshza_fVogHGRxXqV04ilSBZBAhhKBmoH9yyWhEDdhU96QId1PW5ZM_vWmqzdd8LYuNtQG-Xl2L6Zhg9S4YCoVAq2izT93_ST8n2dNC6_nYSu0WH38eQmTElbmRg1KXdLzISrCwB5Az1fAEwt4dXtf2McB28hFYtd-DZ3K4UUFExUzK7bc_Q6vGSB_M6KUDGrL4nYYJmK0QQ-KJY7EUeG_buJDGu01jAPHdNm3TLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اردوی پاور لیفتینگ بانوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/94809" target="_blank">📅 02:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94808">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e3566aaa.mp4?token=TFCprHTc_tyBm3OcOC4H8mE6Bwjh9sYbK0-v1aWMrIFwfBsNZIIhX_dNglvHnIXKA8l2HsbLfuKN9aleXPdbQP_qYEkBmDs3vgMqNbpBRb2fWZgsfeYzfvJ2w7B-jiScKjkGLdv3gSwQNJ1N7bv72mHecsAA6FPkiDgULS14mSgSRimB550kf9IaoRX3eKJ8PbbwurXKu4lYLo2SWstet5BeFmwhRBNiMiEI7d7QxL9m2j0nB7mu58ImmpmpVQjY0RaN9E6fxTLyc_au_gx7mGfuTA1MRazpHIzUEMRot_C0O4Lbkn4QvZlrQIxSlrdHoGjVthNqSBnCf5Zd64Uo6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e3566aaa.mp4?token=TFCprHTc_tyBm3OcOC4H8mE6Bwjh9sYbK0-v1aWMrIFwfBsNZIIhX_dNglvHnIXKA8l2HsbLfuKN9aleXPdbQP_qYEkBmDs3vgMqNbpBRb2fWZgsfeYzfvJ2w7B-jiScKjkGLdv3gSwQNJ1N7bv72mHecsAA6FPkiDgULS14mSgSRimB550kf9IaoRX3eKJ8PbbwurXKu4lYLo2SWstet5BeFmwhRBNiMiEI7d7QxL9m2j0nB7mu58ImmpmpVQjY0RaN9E6fxTLyc_au_gx7mGfuTA1MRazpHIzUEMRot_C0O4Lbkn4QvZlrQIxSlrdHoGjVthNqSBnCf5Zd64Uo6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت تمرینات و سطح تفکر اعضای کره‌جوبی و ترکیه در جام‌جهانی که حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/94808" target="_blank">📅 02:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94807">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGkOEfnRA9U-IPDH-8bRmigVDmS_jvl5F4sCbZ6CUJOhf8arKkQJp7r-C_Lyyi-TOI7ai2KYlr9ahLhdEXng9vbFbreWCvbWJHEXQvTlWLbreIaIRBhp1n0iVnJ0i0mFPtnrz_Q0d269u4qTloGjoYQ0PD9xKxvd--WAex5GwiRPm8CCa5JGScz-nNc0X_2H0N5vTzhQTkoachn6GqdPlDyWnXYkD_ADl4NNzavVLuV_TXrdxPWflFHxxgQKpx5DWVFMrQ4omKQDepWU4BWvKQ__fhddambZYojritZcmKBVvC9mJPJZPZBJ9j6ROIPy_2DnKKvRGC_qLHZUNSrf5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در 2 دوره اخیر جام جهانی هیچ بازیکنی به اندازه دومفریز پاس‌گل نداده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/94807" target="_blank">📅 02:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94806">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/94806" target="_blank">📅 02:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94805">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qyWkSYLnwOf1HXG3dZ84XqR_yq81cnt4kAbhIfgRM_Ik19UralGqt2AJ7vd-09J8FjE-s_qOBwvf6oZ7HhJ1nModpohAXvlK6ZLIHdFw-ZyTz5oncHTPIDsc_LrZ2J0aGqQP_7MBuOKn9DzyoKejLguPrCCtwqGCvWW_yUbpml-zrFK5z49b6b7kpMDkZbm_I8z51A6Hyf7vCSVQTHZ8oO6pXPCxydtGH3g7Iak0PV6YH2S5Om4hCMsuCLZudF-G8-wutJLQHyPxLS3IjhsRUjv2CPg4_vhThOV_KMMBtcrl8GHos2w0ufF_HwOMc90xunbpZ8KGT3j9FOlY8RI6kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/94805" target="_blank">📅 02:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94803">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TVbzM5Y71wU8tNwUTdjnPKP7JIR5glwGk2BNy6hrAFZphAxLvZ5e8B5ZrTR0hsjTlVa4GCe3ge_6b34Ov_UTOcXCpJCxUpFpGMAfPiU0fdtOzKan7me5mOrLm7ANGJHEpls5vi2w37xCwRpAFNU2x-edzAM59i3SvwdezLl7hV0-GwwncLb9FhbrJaMwy68UDrxDWkaoBEdkuPwZhPjx0AsCD8_CbjUdkHhKD6zeb32aXLQZP5NA6tcghVoXp06_YdeXc8-e3ETXaW4eArs_ia5DruciPuUh02Ktk8zfDNdr2sRoipXHxUweVoc1NMJLyh85R96TTh75QtHtrRqIyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0PnJDHGWw7Wl6FFbtT_7CHSbmMbcUxsYztiMh62lJL9_wM922bJOvjwcH4yQZyEU9SDdFrO_U2SusYtGnUnthhwwrfH8HYhpQbGmgOx7n5AMhMeXfbt2h5QFkyrB_9UqhV5dsYuncvkTaSFt4hf9n8OyQUdhomCJXMN8ya5krJW8KVadUN_TDTuvw7_LjXz_LqQgsT-o5_jFAhwLQ1grYONO-TDB-e9DxlzrFWRaMSpBGGHtawJX2anGCqBhDNG3bvu1EONN5eJhj5Hs4Pg9PgNFGzGSUHl-0SHJtiipW-Dos_SwO_HrdHFQ51Iy98NkD92JTVNtYqfDTiip0ELsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇼
🇪🇨
ترکیب کوراسائو و اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/94803" target="_blank">📅 02:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94802">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
ناگلزمن: به نظر می‌رسد اشلوتربرگ از رباط زانو آسیب دیده است. اوضاع خوب به نظر نمیرسد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/94802" target="_blank">📅 02:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94801">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFiMZUZjD5IOEsNEKNhfVJDZNzjjdUlpCDsLG8Z5T3h-VblGtJCgndn13JyUxeBDOpqgl_5WIRKB63GcOzGU-CHqRbcJb7apRzi1Qkpfgxc1gbTle9hIEKm2OuFJzXnBMujZ645wZcMGobNBfMFDK0RuOJ79aiZizPv8W5fH0VFD_zQ5yB70M5vugs8ot3TGrchJaMbPTOWuhpNHJp361zBk42YTV64vvBcUQ_vg-HMEV0_NAKnbGXk6tda2vDT7nF0oyw24A7KyGdHhTW44AmRiDJGaN_Q1_2y9XfNqQy3Bih81_Ni-D4iWYIF4ypP4igkxzaC6cjnrI5DnESD-ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
آلمان برای اولین بار پس از جام جهانی 2006 دو بازی اول خود در جام جهانی را برد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/94801" target="_blank">📅 01:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94800">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7FmlKwyjgitIYM1qlNxVajmumvnX8GWoIEtUgTIaok5d6xkIdHGSA1nvS8M9Z-TpDoH21DpDrZPMMgHS6Yx54tQt_SOJEpYwJOhzc_daHFhf3jxbU3SnauzkRD9Pr1CxS7_j-AXPI46Lh2CKYDXkyjOdSl4W-NcrtWc6rkXrWdxSCSFkrRyD8fk95dHt84GF63_AHkL22J1Wz52nbYxgFJ0d4MqH0ELeV_DpserX_-nT8IDteq0n-HOzHZNvuat3_DngaM0pidEoEadIC2LDDJSgS9YYoLJ-ZFRVg_Tg7Ne0nvTWa9cI3U-RIE385pcjhhw9y2uLt5iCAAKj0dX_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دنیز اونداو به عنوان بهترین بازیکن دیدار آلمان و ساحل عاج انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/94800" target="_blank">📅 01:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94799">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJRqgPGzv9gkKlYfuBRxaEBudlYKa5xziShy0tibbzJ0c7VZxW5sFGJGS8AEBDyUkF8kVjrlViQOKxkmtJdvL5o1rykUb_GEm6m9ata6a7DDWx4q1a-GmrRhUiIYmLW5Zf_BqNxS8xPlBfg59n8_ywr8d-wYUEPhlUKf6lzL2u9mV3AzPzIxrsB4eP1h4B12S5x1ghWoAp2LnLorGPG6dql1EToxYdTeZS3Y2ePNN4t3isj9AhL3vecnbEGJfNsG4XAXbDPNgXZ_aptv4GfCqcLmvUfUKAefOCdUFpLwdB8_UbzmyRg0yQZnQb6hrQGG8Dw2rELP6KqCZwt3thO3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آلمان به عنوان سومین تیم به دور حذفی جام‌جهانی صعود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/94799" target="_blank">📅 01:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94798">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-bCWQLtxNyfwEYMSn0LWliR8XAXSzvfiN0o5p9k-VocRTaQxdePQu6-VzQBSk9_WTEvgJi0iMoji9faX06nvfc51zL7Nhr-zn7y8P3-rQt8xxZ-iL5PKgkW662vw2U7GDaYclzPdZp4Lh6MOrfmv8XQ0t41IhPOLwvcfdSU-3kRfB78MeAzjSRv2uK7blTqxEN-7I6-qQhiuA6UHNqN2q_iJLo-gqwnSUOW2ECXRhwfr5p8QkZgN6EOp2W3e36ifj7WsKJPPHOUhfkDbhoBfdXiscaHuxRrc_ul8CO4A4PjIpciK4KKZm0cLfX2TkX34CrOPKUgQIyFqS6DTxhFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | کامبک شاگردان ناگلزمن تکمیل شد
🇩🇪
آلمان 2 -
🇨🇮
ساحل عاج 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/94798" target="_blank">📅 01:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94797">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">زندگی سخت شده بچه ها   میبندم روی برد اسپانیا مقابل یه تیم کصشعر مساوی میشه  میبندم روی برد برزیل مقابل مراکش میرینه  میبندم روی برد پرتگال نوس و رونالدو میرینن توش  میبندم روی برد آلمان کسیه نشون میده واس خودش کسیه🫩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94797" target="_blank">📅 01:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94796">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfdc8c5f07.mp4?token=neiBBA7A8phmsCS3XjS-ppg6fdXRuEWrHlVJ11M9qAaxJHBBRoJWk-GO0rw_qi5H2Xw35lGpcWThh3KU8Aq6SwmxmTxIAsWnE554G-of4CcHBnKbOaOCC6HGVmlscW0lMYDupoc06fn3NniKJlKY3lLtA24fhoYUG5LJS3UtIwHi3tvOvjKtFZ2tyrIhH33hWqe3UngHMPYM4PgbHafI8msnL6ssYTxXNI2tHwkH4r8Lnk74C9C2CaFZTI81BM4UGTJA9BHOBOYQaOcAMgfrt0wAfUlqZuvqTwpXiyahaNScI3jh7ApWcQJSsR5DgrcAOrGd_Bqlx8XunZt0QTV3jw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfdc8c5f07.mp4?token=neiBBA7A8phmsCS3XjS-ppg6fdXRuEWrHlVJ11M9qAaxJHBBRoJWk-GO0rw_qi5H2Xw35lGpcWThh3KU8Aq6SwmxmTxIAsWnE554G-of4CcHBnKbOaOCC6HGVmlscW0lMYDupoc06fn3NniKJlKY3lLtA24fhoYUG5LJS3UtIwHi3tvOvjKtFZ2tyrIhH33hWqe3UngHMPYM4PgbHafI8msnL6ssYTxXNI2tHwkH4r8Lnk74C9C2CaFZTI81BM4UGTJA9BHOBOYQaOcAMgfrt0wAfUlqZuvqTwpXiyahaNScI3jh7ApWcQJSsR5DgrcAOrGd_Bqlx8XunZt0QTV3jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم آلمان به ساحل عاج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/94796" target="_blank">📅 01:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94795">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">چه دقیقه‌ ای</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/94795" target="_blank">📅 01:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94794">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آلمان دومی رو زددددد</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/94794" target="_blank">📅 01:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94793">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/94793" target="_blank">📅 01:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94792">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آلمان چه توپی رو از دست داد</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/94792" target="_blank">📅 01:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94791">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">این وسط هم آلمریا تیم
رونالدو
به مالاگا باخت و مالاگا موفق شد  بعد ۸سال به لالیگا برگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/94791" target="_blank">📅 01:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94790">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d006b86423.mp4?token=BRnC666mNEkdPgOYbEyKvPDVqoyFl9ne3iNbYez7AQXHC32B-WgTYfj6oFkg093YmhJyIjUf6-meoWoshsdQlSzVnwtIop2fNB-Uec3rabUhRkv9f-gNZ5DLevkGIuLAidHsB5eLghWDkmfgmyoeBl4aOXjf6cMu93F-cCflra7BrQzSHHRc5_UumefEIAMcUxzmfw9C8CazJ5_StMx4S4gMpnl_Qs2gQfv80iH3HM4uXSGFu5s1frXqHyyq02SiEF4yDra7Pz91NOWwqVnQ4LdESp7bnZofY9XYplxAR5rdJ145fv3cAOiuKzB968fUnU8UGaIOiVPSt56UPm59rjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d006b86423.mp4?token=BRnC666mNEkdPgOYbEyKvPDVqoyFl9ne3iNbYez7AQXHC32B-WgTYfj6oFkg093YmhJyIjUf6-meoWoshsdQlSzVnwtIop2fNB-Uec3rabUhRkv9f-gNZ5DLevkGIuLAidHsB5eLghWDkmfgmyoeBl4aOXjf6cMu93F-cCflra7BrQzSHHRc5_UumefEIAMcUxzmfw9C8CazJ5_StMx4S4gMpnl_Qs2gQfv80iH3HM4uXSGFu5s1frXqHyyq02SiEF4yDra7Pz91NOWwqVnQ4LdESp7bnZofY9XYplxAR5rdJ145fv3cAOiuKzB968fUnU8UGaIOiVPSt56UPm59rjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول آلمان به ساحل عاج
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94790" target="_blank">📅 01:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94789">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آلمان گل مساویو زد</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/94789" target="_blank">📅 01:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94788">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/94788" target="_blank">📅 01:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94787">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4c0CmwjbLGDgCixUHywnhwl6eq52Zcw29RbtZhSXTHQ0kd3WmX4sxHE0J8c9wiC6n8GVVFPI5ro1_dWwnM3as-7SVkvoopqLuvoCrIcSH9M3wC3E1HM7R8BGR5ldw6zaGK5imFwOW9l08OF-E4NtszjMLoeXkwfdOum5xbrtQ6Z3TVAaIr9Z6eTuqNgUgd7BViwamhhx3wD5YUG2aIb5CUUtTvmN72lipehJc9mSriZGoXIteSp8NkIIiUPzAH0IEJoYYZIDOM8cwKl2TMDEDzAuZ6Hi5M9rM3noWNdSonjC50yh7BTuSZmOia-m8HYAL5-BIleBvL6PRQvbZKKyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلژیک بترس که اعضای تیم ملی آنالیزت کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/94787" target="_blank">📅 00:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94786">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">زندگی سخت شده بچه ها
میبندم روی برد اسپانیا مقابل یه تیم کصشعر مساوی میشه
میبندم روی برد برزیل مقابل مراکش میرینه
میبندم روی برد پرتگال نوس و رونالدو میرینن توش
میبندم روی برد آلمان کسیه نشون میده واس خودش کسیه🫩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/94786" target="_blank">📅 00:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94785">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJVzuKZIQb0arGeTIhSEGUUGlt2D7dHkQZCy6i_FlM6-xWfyI54PFpMN10hvu_UYOdsiVv_Nuqzjf6KknWoI3JY1VZs7ppkgjoaKaa1uHaCbpZS5K2SswlKSKHHmCTH0RGNfLJ5dhMqnGdyQ7D5aWUGFsStqBranZeS7f0-fBtOb0DSZ92sXU9Ok0V6ym7lMTP82y5tYqYRPTsDFPmy9s0I_kjgUH5RpEybreWqz0QU2Rsqob8Qo4zOnhyGOivDqxK2fE3pCKSLJlnyVjXy_OhA_55qebSkMBNMilsI2zNQVwdycPjrwNpB1sTz_3wZf4VbXJTByW_sk6p5o63HqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف شایعات ساعت ارزشمند ژنرال رو ندزدیدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94785" target="_blank">📅 00:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94784">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
👀
💥
با توجه به نتایج فعلی، شاهد تقابل آلمان و فرانسه در دور یک‌شانزدهم نهایی خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/94784" target="_blank">📅 00:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94783">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اشلوتربرگ مدافع آلمان تعویض شده</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94783" target="_blank">📅 00:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94782">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بریم واسه شروع نیمه دوم</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/94782" target="_blank">📅 00:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94781">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvgDahAw1rKE1klNMq-6ZetORc3-EUInedoemGl7Il14lQ-VvvrnuIgOaBEXXAAilSH5vnlDV5aHyxvBZXDRBhNCC-uGo3cae7ml_Bvo3ogwx_PXThQoizbfuEGSKusFm50qunCgd4KL8lBXTpaDTQv_K5OxwAYPCUKG2Kttpnuf4OsaiPBC6gO9HO-6CVexlFETlny6bB7CIiIKQT_NHgR-ua-5cYB2jxF5nDgwmbC3fZdZBEIOvME55MeDSYAxwjfdUBcfboAhR_7BdqmfBw3ChQ7ggdzuM7GqzRsUu_bDDHZSiQUoaVOnDXJm_DmTVYDP81wVFdPXuzK5VFlu1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇫🇷
🇮🇶
#فوووووری
؛ هواشناسی آمریکا به فیفا اطلاع داده که بدلیل شرایط نامناسب جوی باید دیدار دوشنبه عراق و فرانسه لغو شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/94781" target="_blank">📅 00:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94780">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYcm8Lle4g_ri4lI9tKUN_LhiHzTdB4OJZUjbJlWel_ykgzYFZjletuWuEf9364RQxBAr1ayZC-_9f_cifR1RtU-nRY5sgdCRYK_FZVxb4TgiHU6haz5dbKVMADFqp0iPDQeOLBdnSBEYxRGI6Xt-8avNJXQMrZArrvboqXwDbEEr3S6wk2K3oLAUzjA7RNOM13717LsLJZhy8zh80xso8V5TIsxjnUvBUlEW802TnerV7JPPYp_KBYqnLRU6swHOiTT5XOfyBhh-toRrU-qKWda6MEuvf1NxunuFE1OTVLbOiCIHDMpVk_FgzxocL1joSas1rjA6_WdzX8pcq9BlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مانوئل نویر تو 8 بازی آلمان تو جام‌جهانی کلین شیت نکرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94780" target="_blank">📅 00:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94779">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پایان نیمه اول
🇩🇪
آلمان 0 -
🇨🇮
ساحل عاج 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94779" target="_blank">📅 00:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94778">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آلمان گل زد بازم خطا اعلام شد</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/94778" target="_blank">📅 00:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94777">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c338e8257.mp4?token=ZOii1FBbnH_cS8Ihu_b63xm0WK4ERMfpZsCoFEc2cD-e6D-20MXEYlPWF3R5zYEMIi3h5Lo8vxAOM6rZbCFQbisgwBJCOXSt3NXqmccW0toRbbVK9F-sqGTjziEtIW9mDa6KHeundWLauk4JxoxZf1Cwq9QufvbSCgWivzC2gKmdwjZ82G1FbYDjexnFS0NujZJQ42I5J7A_72VA4x4aK4c0vG6ZIZEzQVRdAGxmxLGSJeN7vwKvptgFPoMvVNPUy5WR7dl_bBo-d80bwLPo1LGPjmQyXCTmv5IYo1Axu2hfnhZ4PvNXTanSxP4BP66LeThVzcMfwc1x0ZoGZ-0YcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c338e8257.mp4?token=ZOii1FBbnH_cS8Ihu_b63xm0WK4ERMfpZsCoFEc2cD-e6D-20MXEYlPWF3R5zYEMIi3h5Lo8vxAOM6rZbCFQbisgwBJCOXSt3NXqmccW0toRbbVK9F-sqGTjziEtIW9mDa6KHeundWLauk4JxoxZf1Cwq9QufvbSCgWivzC2gKmdwjZ82G1FbYDjexnFS0NujZJQ42I5J7A_72VA4x4aK4c0vG6ZIZEzQVRdAGxmxLGSJeN7vwKvptgFPoMvVNPUy5WR7dl_bBo-d80bwLPo1LGPjmQyXCTmv5IYo1Axu2hfnhZ4PvNXTanSxP4BP66LeThVzcMfwc1x0ZoGZ-0YcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول ساحل عاج به آلمان توسط فرانک کسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/94777" target="_blank">📅 00:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94776">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ساحل عاج گل زدددد</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/94776" target="_blank">📅 23:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94775">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پشمام</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/94775" target="_blank">📅 23:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94774">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgwdUXZaRBiUxKYpM62cNLWeONVqdycVoDK_LCoVye8RzYQSCEZ8ZJXWk1vhnfhuW4903EE3LcsDxEb-2MeztU-rjT0nN4g_1K78gB8n5kyY1haqKlFV_0_oEZx3ySeMO24taLdm7YiAeUjVwPz_zFdA5LWPzxM89fWMw4_YGwZY_gzxCj7MTBtgPTaRwWFEb3pMqikzLDcgWpXqjdSbtU8X4eNITC9Hs9Z06TaXOtTirX_SexRefgTuTZPUqMviJwWjRBYNnWZqTTtkiLzJuaWD9M9LdqqBOmUGNMGHLlemZ4kDwZFOiSD0JVGhiAYTR4DJMylvomyQ8C9NjgUxVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇧🇷
#فووووووری؛ شایعات رسانه‌های برزیل: رافینیا بدلیل مصدومیت از ناحیه همسترینگ ادامه جام‌جهانی را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/94774" target="_blank">📅 23:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94772">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آلمانننننن زددددد ولی رد شددد</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/94772" target="_blank">📅 23:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94771">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آلمانننننن زددددد ولی رد شددد</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94771" target="_blank">📅 23:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94770">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلگلگگلگاگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/94770" target="_blank">📅 23:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94769">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نزدیک بود موسیالا بزنه</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/94769" target="_blank">📅 23:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94768">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
❌
نبویان نماینده مجلس و عضو تیم مذاکره‌کننده داشت یه نامه محرمانه از مجتبی خامنه‌ای میخوند که در اون به صورت محکمی خلاف مذاکرات صحبت میشد  به سرعت آنتن رو ازش گرفتن  صداوسیما بیانیه داد گفت نبویان ناقص و بصورت گزینشی داشته نقل میکرده و ما قضایی پیگیری میکنیم…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/94768" target="_blank">📅 23:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94767">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کم کم بریم سراغ بازی حساس امشببب</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/94767" target="_blank">📅 23:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94766">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SD9ZSd_qBbiVek8Z4N37JX6GZbUoNvnMuFNs1D8GqRDbVKct6HEqhOJ67VhTMHxLDG03EfBRChGdpIe9dwcCO80EZlNyDxjiPvd6r9i9OdjJ_JZ4GLb7AizWYOXV1J2gdojAMjIcN0iLqjZUtevj9-7OEl5ZtNRrDxt53J9o3s6o8ZwW3O8esbz3hR_Kb2mNPstsAwG3sjWNxkzi2TOr9YMZJIz-3w6jrhlXmbgYaAzeAj-HpmFWuWJ7nlzrXv8oDprVsZ3EYGrEoqoYL7k55s9tkN2_kGUYE0g60rBnpm-QxS_R2L5tCCsXidIvvnLAXDStYrqKFqR7zZCldKhZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
⚽️
تا این لحظه ۱۰۱ گل در جام جهانی ۲۰۲۶ به ثمر رسیده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/94766" target="_blank">📅 23:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94765">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RH77s31UmZ7mi4HPAneOfBSuNzgQs8tTOTym4EU1m_HnyRIC8cmJuscyKON56sz8D-4-W0z0_FRb7E4hwCqeGZUAr6T6BOPIuGkWt9tSGW7tjht99DosBHQxMf4KhUPEEG2TxPQ4M1Uryt5nNSXo5Ujq9gUrufFMAu-XpjCnYLrelWLkFwIPg3WOfkcCBxlqyQpV4zMdvxbnQb7uEaPxWzlagirHxs1JR1ZG7sKHBaD-aq35MZs3lePF36fUFVNgH66aHSdwJ9wGVncBsg6t9LoQunHBj3mLgyiyCZXf_0PHhobQR1OuE6HTV29_uWy5YEylLMVF-rmFTZF6m_rGnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
کاگپو بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/94765" target="_blank">📅 23:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94764">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAZeGBkRNSIDtB27mpasjU3SC7-RZR14SZhF-pH2XEJgMTYygJOHJM0EPzV34GB4eDsVAfH8Ek0TeZImnnY473irY0C17aXae_VCXUjtUkNB_c5XW5hjuADWV2cGiJPGLEP_Su9ZNBDMeyXLEjPR56sAOpbaTNV2nuhnz8eIG_TxiLt19m-iICCPP4O3WEI-ulirg6SVXNHrqJ415-AqA7UAi5ocizrUxDQljBmkpRo3KxTYII15WGKGitPgStDP81dtKk4r-BDalyFvMo15ZIA_N4OQYNRGueU-xwNLwDv0K3vx9bToDb90gEDk_z1-ABlcd9bxzm8MzBWwZNO1XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین مشارکت در گل‌های جام جهانی 2026 تا اینجای مسابقات:
🥶
4 مشارکت گل —
🇸🇪
الکساندر ایساک
⚽️
3 مشارکت گل —
🇦🇷
لیونل مسی
⚽️
3 مشارکت گل —
🇨🇦
جاناتان دیوید
⚽️
3 مشارکت گل —
🇩🇪
اونداف
⚽️
3 مشارکت گل —
🇧🇷
وینیسیوس جونیور
⚽️
3 مشارکت گل —
🇳🇱
کودی خاکپو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94764" target="_blank">📅 23:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94763">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حمله تند اسطوره فوتبال هلند به رونالدو: او فقط برای نشان دادن خودش عطش دارد و همین موضوع بازی تیم پرتغال را خراب کرده است/ در دو سال گذشته، پرتغال بدون رونالدو بهتر بازی کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94763" target="_blank">📅 23:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94762">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6zN-HVrXMvNhwDEKqJvwWLphNoxFKgI8plexOwhdjjgxWw1AAZjTkJiBLzf8nztdyulgEGvT03tUFJ0EtEbLFn2pc19X5d_21kXyrzYSKINkLnfxmvEya-SLhxB_OFcgtphDJiZmFVXXiS7uae3fnr4H40w2B1C_bW0y9vbhYCDZ-WlIhSLGitfDFrN2wAn3re1ythDOfUFGsuV1-6lXm2tZWvi3WV8GuJXS62De3EpcIWQhyt2cjT97VkMCHrwSsjRFft9sDaKPGWfiX-YbwrmIV4j3Ta9NL_SYkTc8aUkjo8kdQ6x1aZfWKgV8eEtVp8Y_fcq0T0hikMVPS3Mvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مانوئل نویر با پشت سر گذاشتن هوگو لوریس به دروازه بانی با بیشترین حضور در تاریخ جام جهانی تبدیل شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94762" target="_blank">📅 22:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94760">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7d1NqAIYlHLHyrE4CdhYsr1RV_Zee0xdH91VyiB4KBMqIWBDQRFc6H_auSS_RLnmCzhZkt1EtdOrKn0ugKQ0SvdWxWg-BMhQ7yeKZASZf5hpGoOxmf7nbi3h4q1l-4kEPK0vSwG_kbtoPgZrfSiMROztmF67WbQCG9L81ADC2_NK-RMwXtkfSxyw9cYqK2lKQeN3rls26LoekJ6Kx3u3Q-pwGBPzuvpY3ojJHADzj3-Z0rPt8NMnyKyAKXWlRMy-TkiK5TChRZaVfFC5jFlVbmWatVLUY_e1JEJEtV3d4oAGTqrbyrdTqEGKPlUyIAPGUBSfQ8MXlQkpJuohEIhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0iwzXYI_DqDSm7ihVL0l3YmdLIbsszCaxPOxaE-zyXSNbvNO87U2aB_tJS88-ze5qKFSlWhBEGR0bkqT_IVutXxD2sCo91OOTZ4HsO27vjwGgA4i-uBEmKWAproq-OxGpk0R8FN0r1h61QHCizi8mXIIYrHqEUggyLuJRilJGDbpVp5wpI3LtV9fTVG8SRqVvy-hTqA0dwSdsBqdO81pljzPCCwHbnJfz6QlCwV-1GzO9Jepspump9Q5RCBSarF8fyggZ6knI382fMWjD9DAz-enZHoRcRIAPYhPEenU9o75WDOhEshppFPgrD2in7KNP3XwOeLqxJiDdUw5-wE-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇳🇱
کودی خاکپو با گل دومش مقابل سوئد، از آریان روبن عبور کرد و حالا تعداد گل‌های بیشتری نسبت به اسطوره هلند در تورنمنت‌های بزرگ ملی به نام خودش ثبت کرده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94760" target="_blank">📅 22:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94759">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spzpX3CBFSr258iP5JcBlNHtwOz7Irq_Jl1oQw0Ittyx2_qDPfOMEtmkAzb_CPoZm-OLSxYMmvOHoYt7KqXC0IgYuy6tE2y9DmFpyM0Flt8mnDDUxN5oJYZmL1g7sGjBkJYewJJ-rDd6jsdAYtn8k7Glpfbm819LgXcbcwtgx81cnVowgH0K4k0Lq-5DbGJCDVtnIaVo1_0RBWy0TTyRJyE6S7x9R773L2rQgzoWMs8-3XBOEtiYq44-VmFkMpP_mRlmPiMl8YdH9lA85dafCaOtxKkRQxuC1JNanAsZ7iwcTKINC1q-tkNz72pYlFAxBRbjVnXcEHTJxISN-2AI9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر دی یونگ با پسرش تو تماشاچیا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94759" target="_blank">📅 22:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94758">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAJXDcGXcGb8fyGp0q2CuIbtSLpdq2nTgAjqp1tbLmuB8KFAoOFWJxBqVwxkNfMXnZ4bmnJAOXR226LGttw_x3EkahJI2O54hOHedb_0tt2q5dsmSmHXmivJeQmKOYm9_f9Vdy-DJsRsYUbns3-earLwDr0_f_wqko88yzSQCktod8OXuQ7bRn03Fi79HDIKDbtTGXWUV9YYUtjt4oFNl5s9CCrcmqZmlisu4fNV1lbe9XPvuR1JS2PZ_d2l9zK3UMpOJdu1Wde8sLS23o3AyjsU-690pVmMfRg91klUxVHnxzErdp_kfqf0obvyCUsAKA-ZbAdv1TlauEpxwBWPyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
با یه عکس فوتبال رو نشون بده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94758" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94757">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef53d28320.mp4?token=f8V0Skdj12MPomQLs4oAZtZ49hJaottpro9w1iMWVLRFIH5ejrZsAmZniDpz9oyDsp80AkeShi8gNRfsST2TN267u-FwwnWZ5cs3ZfGnpeE4L0or-wsHLPC-GdCQt55p6E1Wr2OYFHkEJ-aq3orebIyIcjzN1w9LhI9wi4EiHhsjNgah6NCar34aDOo6wo34oN_9jz5xNC78gb6XKBGL5kT-Jn6vUdgR_hwjUrVixcPoX62eGFX6nBvesIFxMqsxD99RUBKv1-vpRbGW6mV9-JfAV1rpBjVT66vBA9FOlPqwH93I_yYE8Y0WMYR-Qpx6t5ajlhnHzdbQK4Td_v3rAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef53d28320.mp4?token=f8V0Skdj12MPomQLs4oAZtZ49hJaottpro9w1iMWVLRFIH5ejrZsAmZniDpz9oyDsp80AkeShi8gNRfsST2TN267u-FwwnWZ5cs3ZfGnpeE4L0or-wsHLPC-GdCQt55p6E1Wr2OYFHkEJ-aq3orebIyIcjzN1w9LhI9wi4EiHhsjNgah6NCar34aDOo6wo34oN_9jz5xNC78gb6XKBGL5kT-Jn6vUdgR_hwjUrVixcPoX62eGFX6nBvesIFxMqsxD99RUBKv1-vpRbGW6mV9-JfAV1rpBjVT66vBA9FOlPqwH93I_yYE8Y0WMYR-Qpx6t5ajlhnHzdbQK4Td_v3rAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
نبویان نماینده مجلس و عضو تیم مذاکره‌کننده داشت یه نامه محرمانه از مجتبی خامنه‌ای میخوند که در اون به صورت محکمی خلاف مذاکرات صحبت میشد
به سرعت آنتن رو ازش گرفتن
صداوسیما بیانیه داد گفت نبویان ناقص و بصورت گزینشی داشته نقل میکرده و ما قضایی پیگیری میکنیم
مدیر کل شبکه خبر هم مجبور به استعفا شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/94757" target="_blank">📅 22:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94756">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLX03-eD1gJw5Gs8daAC9DPALIPPv3D2x0dsLFNXonoCBi91vLgxxTLbkipOAPlqV8LEYRKnxMw3gYuryDaDEIeNNEYLLiYZ0YQEpg8ax84lDo5yiWUAN6H1eCol0N5nyOnv5sM-gPdSok_6_GMbQJ4F-qg0N2TsqwbScNfVRTJ3tAV7HIWJEAf3e6lsXsgrpC-Be48Gpmui-Gsr3V1FiIdE0Mt7PZGPBq-cXe2FfpYHBgt5OZRtTQ1aFaMmwgGLDPHRlAuGWpZJdwfYOcUO6SyGUVJlp_cQzTTozR4D2G-N6VKzyI6VwwyorGE3wp7TqGYOG4dfBJ5MrwmeK3GJcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
کاگپو بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/94756" target="_blank">📅 22:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94755">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فرانک دی بوئر، اسطوره فوتبال هلند: عملکرد رامین رضاییان در ۳۶ سالگی باورنکردنی است/ اولویت ایران باید نباختن در مقابل بلژیک باشد و همه انرژی خود را برای بازی مقابل مصر صرف کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/94755" target="_blank">📅 22:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94754">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Akq5T12SVHxHSbJSnjIcmVqJV6SlNVFVSHeW6EknyV2km3h3kVdN1jFrIXQFQjJTEZ4Os12OLSxxfPOYF9AzMkK6ATlWM_eHyrE4EnXzYhSW2uI2WL6cn1ro-ZELUhZ5rXCmQs8ogYjJdjRk0MdBLMWHoXSHTwQypL_cSweRb84q9DHKTcA0yVUfL3dPgkXCSOldOOEQSWjaCgewNCdlYcoN5S6yOiXouwul5mlcHHJZkiyS1Ocvsc6myhm8Si8ncj1RqO7Lz181TfSlyyygYZSMR2pB29Aoa9s82RzD-F2e63btVp3H-7FXCSgbb0ZRCsD5BbU8wA5RrM3vZbRQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|نمایش قدرت هلند؛ سوئد قربانی شب درخشان نارنجی‌ها.
🇳🇱
هلند
😄
-
😃
سوئد
🇸🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/94754" target="_blank">📅 22:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94753">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ef7ea27fa.mp4?token=DZ1xeNDbwluFOjpO_pU66SI1v0QnyYO7KNz9Wx8g6COjuggHnqBVWly9u0MYzbetYlCwlVvrtQ3kDI8jyR1yY0bMXVhbpEmiRV5_1Qr78tMYRRIP29dvUPfkKBqQo32abY2LjKVw7mGs_nvhniKhcM8GkoyJqfr5B8DCYsZEx8GM8Bv3Koe03J2iK2u00vocD_BxBZI1_zxsm9Engq4QkI0HT_HkBvTjQ2zBIpFKSu_hFZWG6oq17z7EQjWpFlwjNKcy57MF730V_uim_kxd760I61-B7Kit3mQDLZke6l5sGe6IQz0HGSP__FkBZrBjoQyAQ5mQjkvQKE24S31ojA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ef7ea27fa.mp4?token=DZ1xeNDbwluFOjpO_pU66SI1v0QnyYO7KNz9Wx8g6COjuggHnqBVWly9u0MYzbetYlCwlVvrtQ3kDI8jyR1yY0bMXVhbpEmiRV5_1Qr78tMYRRIP29dvUPfkKBqQo32abY2LjKVw7mGs_nvhniKhcM8GkoyJqfr5B8DCYsZEx8GM8Bv3Koe03J2iK2u00vocD_BxBZI1_zxsm9Engq4QkI0HT_HkBvTjQ2zBIpFKSu_hFZWG6oq17z7EQjWpFlwjNKcy57MF730V_uim_kxd760I61-B7Kit3mQDLZke6l5sGe6IQz0HGSP__FkBZrBjoQyAQ5mQjkvQKE24S31ojA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل پنجم هلند به سوئد توسط سامروویل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94753" target="_blank">📅 22:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94752">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گلللللللللللل پنجمیییی هلند</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/94752" target="_blank">📅 22:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94750">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OhFUOb87k-KN2PYsEOjPNHRE4Qr9plzvZDERMisW__H8tIBazq3hQylmjPqu0aYQnYHUwvJd9ThPvpfibsgZ1We5KxaHI0pLIvNdP-nfFi0WGzGYO9HmIFXZqRWUu62aEjF8F9-hS-xgQltOMmLeWIaaRu5kxhN7bgf0hOr9aZKBeKFCplB9pVdC_HWoB2CoZwHq0dMA5qJK2e9JL--LspxxMjikYq1zlZ2aEmbUASG-nHIdTY9r7h6hoccFlM_nJPftEiBJr1Z6DOfeT03xhJKfnKoQMFjMhHWvj3kYb7DB9eK11v6uxS_LRbU5-KHpsGBnq4cgTDJODYKeovvOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cHToEGBS-fExwp3oBEO552RqZTwIysFjcIEKJwxCc28FK6yi5SHfG4s_G_dqrOq2QxHXFZ-8UmLaZOn-1bf6Mhu3djU-1EK--MeRI21hBYsRGKZm9s6iPfis02zCLLpplFyX9-4hG9gthId2EtJTDnW19AlLNX_MSmQX6RebHlF-ZGP7H4CVeT1O6B3v2fjzAWJAq6EQzCzajnKhYULghkqrvTZ5xRzI2I5bKQCgaM67kE6sXMApwmPZROkENH75ry55mEp7-HWzqJMmPN0nQq1ULkZR6FbWq9laSZQw4LIISEjWOEXp24HGjW5521sofoauMJORgUhDcQ70Y4rTqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇮
🇩🇪
ترکیب آلمان و ساحل عاج، ساعت ۲۳:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94750" target="_blank">📅 22:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94749">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAxi3LGazbi5DbSqjLuzThDgpMl6Ps9VvVkr34Zc2CJ-fleuw4QJhiJ9U0RQ6WShfn4hp0tydzMdS7LH5-Ca3Vi9w808gqhuaWTvoiGERC_wq8ATKw_wbFj-BIFx6q6peTp4Tvm5NvKznpTorKQRGrKtyGs_H86Fa2Mh5LwQ5Koqr05apYr5Svwo2MhDIOdK6aip6g-fVaXT9i8fljtDwIRhS2oKLH9hQqYgVf9pZjBo5-rQX4CMZIfx1R2VO-8jAt84N8sOZwO2bnm28V2xtc4bEMlP_Oram4A7fMZOYZUIaR1aWpa2PRy5ZxclCwFKoFuCExPeUbGwaivtz-GpmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاح تونل ویکی فن دوین توسط الانگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94749" target="_blank">📅 22:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94748">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">این دخترای سوئدی چقدر خوشگلن</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/94748" target="_blank">📅 22:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94747">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">چه لایی خوشگلی انداخت الانگا</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/94747" target="_blank">📅 21:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94746">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9b4fed19a2.mp4?token=ayGSLr-UsyhNloYkRp1MTNt_SPr2zXEcCVF8I6fuk8Z1BHDHKyxK-EOwSySr4V-oa8Ft3j7EbNEuC2-tYVpkwfEg6E5W08ACjItKe5EUmGdhxJjYAFFKvTut4tqVIQpFHaL4KC-uByAWkWCmL2O-IKOVd4ni3D39zpRJgdYbYANU-FnMc_BHZpChagpJ01gYVFpg1O_lJ2ala36AJ_t4dVoLaWaRNAfDr7_K-0ZQEgbRWc1CpVlpYC8yDmLd2S0sxlDsnTYVCUvCP9tX2YC_RnILu5Ut9Vb8MzPRk18ZzsR2da18xRkWLbVT4HDXxAJ3tmz7EuC7UsUTvOxwJ4Ol3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9b4fed19a2.mp4?token=ayGSLr-UsyhNloYkRp1MTNt_SPr2zXEcCVF8I6fuk8Z1BHDHKyxK-EOwSySr4V-oa8Ft3j7EbNEuC2-tYVpkwfEg6E5W08ACjItKe5EUmGdhxJjYAFFKvTut4tqVIQpFHaL4KC-uByAWkWCmL2O-IKOVd4ni3D39zpRJgdYbYANU-FnMc_BHZpChagpJ01gYVFpg1O_lJ2ala36AJ_t4dVoLaWaRNAfDr7_K-0ZQEgbRWc1CpVlpYC8yDmLd2S0sxlDsnTYVCUvCP9tX2YC_RnILu5Ut9Vb8MzPRk18ZzsR2da18xRkWLbVT4HDXxAJ3tmz7EuC7UsUTvOxwJ4Ol3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇪
گل اول سوئد به هلند توسط الانگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94746" target="_blank">📅 21:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94745">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گلللللللللللل سوئددددد</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/94745" target="_blank">📅 21:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94744">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b48414ae5d.mp4?token=smOMszu-oean8pmRCKFqLMA9DOpe5T76PqVrS_xYvLtg7nVd15_FPALbB6mzsZXlV-VB4-L9HGpLinPFN91ChCvDt3506GFceIxRHtA4nIb8cK6_qNKRrD4X14Og5iiNsrnOKhEXmSLkMY8d7T-QD8Q3beKrrFHM9TTfWn2iOdQx5jk_eNAnGjsEj-JX0g36doRRIQaWCfSF0GOwQOVtYdVAe8Vb6TUh4xGfxXQYuTpGHmpEmcnpBJIEIZkstCu8gyB_Nc1uUbZ968LOMeS7WRif3QwJwGrMlPpOFVuW9hpEI4IAqjtl86-87zheEI30C8StDqu8zNDqtNdfvtLqXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b48414ae5d.mp4?token=smOMszu-oean8pmRCKFqLMA9DOpe5T76PqVrS_xYvLtg7nVd15_FPALbB6mzsZXlV-VB4-L9HGpLinPFN91ChCvDt3506GFceIxRHtA4nIb8cK6_qNKRrD4X14Og5iiNsrnOKhEXmSLkMY8d7T-QD8Q3beKrrFHM9TTfWn2iOdQx5jk_eNAnGjsEj-JX0g36doRRIQaWCfSF0GOwQOVtYdVAe8Vb6TUh4xGfxXQYuTpGHmpEmcnpBJIEIZkstCu8gyB_Nc1uUbZ968LOMeS7WRif3QwJwGrMlPpOFVuW9hpEI4IAqjtl86-87zheEI30C8StDqu8zNDqtNdfvtLqXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل چهارم هلند به سوئد با دبل خاکپو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/94744" target="_blank">📅 21:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94743">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">چه تیمیه این هلللللللللند
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/94743" target="_blank">📅 21:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94742">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گلللللللللللل چهارم هلند بازم خاکپو</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/94742" target="_blank">📅 21:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94741">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/81850e4c97.mp4?token=qlR-QTxWGg3f87X6d8IbvmPOUQWuwDrZXxBsu7X7PJtvSLU6YISPQosH2x1n9fach2rGUQV2n0ZhiRKttDADuVrfs_gY2QFrcuqznB5nm6a1RHSVy6bRz-PRJNVKp7UnPZqZ-i-c0kvQkhvf8ZdC4uSbUzm0EUBqGvprR056hkmUDDFxfE92VBGg64_lQGeFCdN9K7YA78X4-k3wFC00vfdMSbYTwi530TfeHGI3xWhjdQWf3OswQie1pzQ70IqyJwQuZ_R_3Y0RD9VCNFZXydBaTjVVhqYyRNJBCHXQgSPE0XMjKDhYfDZBw92UYaxPNZnnQaz7oPnd_5Lxb9svAHmZEZWLlRNP7gWctXnA1ThXiqYmG_mFWsk6ISJanmDYdL3iMN_snOUqP1yUasm8_yov1UkH8Plk3sDsxSBSpuWYEYPQo-Wejt_sZA-WlFpodtvUgiG40EO9Pt01UL440SQLFSw_QCXNNf8bh335Ic_J1J2KC8CjBoQJqTak3nqjxsV7O0WPbE-zmalziYG3we-S9qLHHsaelKuMZr2N6x1WLleH0dhVgXgLrKsXBo11SwBhEDAGB8qnw_2tVm4I_m7J5s4HA0GlosXzlBuVOcw0FdQBsCs6NCMw5dEpt9KmpDEDRMYEquIgKQA0fQMLb84mMGS2enGL9pzgtVeoFNA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/81850e4c97.mp4?token=qlR-QTxWGg3f87X6d8IbvmPOUQWuwDrZXxBsu7X7PJtvSLU6YISPQosH2x1n9fach2rGUQV2n0ZhiRKttDADuVrfs_gY2QFrcuqznB5nm6a1RHSVy6bRz-PRJNVKp7UnPZqZ-i-c0kvQkhvf8ZdC4uSbUzm0EUBqGvprR056hkmUDDFxfE92VBGg64_lQGeFCdN9K7YA78X4-k3wFC00vfdMSbYTwi530TfeHGI3xWhjdQWf3OswQie1pzQ70IqyJwQuZ_R_3Y0RD9VCNFZXydBaTjVVhqYyRNJBCHXQgSPE0XMjKDhYfDZBw92UYaxPNZnnQaz7oPnd_5Lxb9svAHmZEZWLlRNP7gWctXnA1ThXiqYmG_mFWsk6ISJanmDYdL3iMN_snOUqP1yUasm8_yov1UkH8Plk3sDsxSBSpuWYEYPQo-Wejt_sZA-WlFpodtvUgiG40EO9Pt01UL440SQLFSw_QCXNNf8bh335Ic_J1J2KC8CjBoQJqTak3nqjxsV7O0WPbE-zmalziYG3we-S9qLHHsaelKuMZr2N6x1WLleH0dhVgXgLrKsXBo11SwBhEDAGB8qnw_2tVm4I_m7J5s4HA0GlosXzlBuVOcw0FdQBsCs6NCMw5dEpt9KmpDEDRMYEquIgKQA0fQMLb84mMGS2enGL9pzgtVeoFNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل سوم هلند به سوئد توسط خاکپو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/94741" target="_blank">📅 21:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94740">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گلللللللللللل سومممممم هلند خاکپو</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/94740" target="_blank">📅 21:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94739">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWiUUhoH-4xVP2iVc-xYwKRWG6SNN9GPVyOUWYS40sW7UT1igZyLG0sBixf-ihWp9Zv0aV37QyKzL8RWJAZTCKDZKKrIhL878QV7NonvdKCYharBuYheWKgWkiZ5lGXzCaFziIGomVo3rb5emYagnviM-jD0DrO3MlEn8lH2085e8MgY6_3ImT8qKXquy8aJwRZ56AHRitJeonNkBwUPgDsMqyLFDESdkw3aQiSWELLDEzk9SKPaHP36z_eQRMtOd1A15a7b0SdrYEtwUTMnqAyyZbrZfd51IsQlgU7W7xDD2gR3SgFURYRA3EDis4JLprLp7wjoRzPVzjF-2WVNWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇧🇪
#
فووووری
؛ جرمی‌دوکو ستاره تیم‌ملی بلژیک دیدار مقابل ایران را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94739" target="_blank">📅 21:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94738">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بریم سراغ نیمه دوم</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/94738" target="_blank">📅 21:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94737">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOFwvts6oZ28hOQrztvMPOWZ4eZm4liS3yiG94UfLQ7ZZlBdVQAGLAaIqMiMjCBbymqkctpnoZtg9x9zZQhD5ONd5AV22z_lohA1v__FuHCcYU3Ozp24KaxN0zbj0FHeFD7tcS3znk_YkV_sd3zv1ELwZCX_A5wKfnOKr--1zFB6_2bEsLqGXdN2F1ecbP2W9BVJT5W50YvUjOxFHX9rt93gmn2frVhMK_3JPc8IGb68YOgs0mjqy8702U3pQWgaCkai13tbL0Qu3qM1xu8vmlcTidQe3Oxzdz5RteW3bBZgXJsiaNkI8L1Bl1R4QFrO9toSPUlou0zFN0DC7x8eCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
‏
📊
بروبی مهاجم هلند در نیمه اول مقابل سوئد:
‏- ۲ شوت به سمت دروازه
🎯
‏- ۲ گل
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94737" target="_blank">📅 21:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94736">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZb-icbeZpN4oVBIcgsrkJkgre2_c2MY5QTPVF22mlaEpZAs7NdsF6fOhU3I6NWn9g-0-BG-DwxB55cBoe8-ZSOkjY-gvuM3AJK8WHldK47-LhJZ4vZX7yev5S0J98u5Rq7QSN6ro29GBr06Jk-JVpP7VkwftyM1I5oGTK6HUh-Vyk_CY1qn-qM8pi2KHXJza3jOO7lB3jUC_N2b38QvhCnzhKYXZAsIpQ7eqwXP3Uf__9IC7yZ8cldeVJZne2aUn68r_svg-R1Vyz948ypPorWsfJRkNiqrvYtSE8TDhF0xRg8K8rOKn3YESIOWakgfFktIX_Y92XNCEdXJLgMS0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇸🇪
آمار نیمه اول بازی دو تیم هلند-سوئد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/94736" target="_blank">📅 21:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94735">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIpqx6JgC7eAvmSrOGj5hZAW9zhiX9Ol5YhGdZN4d1yvBIwRL3knb5PVH-ls_2VhSd2vA5rTc-Tw-Xg-7XtsOcNbZ9pc9Kvw_0Zk3u4g0uHt0h9_ruKIvMZfB4LdYGFYQBEa8wBI2ikNYCbHsTQeGbxvoj-DFQkPVW3Pda-PXdgYkLi7iXW__J0S5k-iaQD5g7FkLpOCiKGFndG_vMosu422iwZCHLKoezxwqqhd_p-H_-jYTtFCPPe9Fmlrjw4nEQJzg8QWABSKX-7__cdGKYToe2l4GYkgMdDHUsqKAY5TY4q2pHZnz47VyDs9gwyJvHnZcTNti0LEol6ya6zdVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔺
رومانو:
انتقال انزو فرناندز به رئال مادرید با سرعتی مشابه داستان مارک کوکوریا در حال پیشرفت است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/94735" target="_blank">📅 21:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94734">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پایان نیمه اول؛
🇳🇱
هلند 2 - 0 سوئد
🇸🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94734" target="_blank">📅 21:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94733">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گلر هلند چه سوپره</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/94733" target="_blank">📅 21:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94732">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">البته رد شدددددد</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/94732" target="_blank">📅 21:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94731">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">البته رد شدددددد</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/94731" target="_blank">📅 21:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94730">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سوئدددددد یکی زددددد</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/94730" target="_blank">📅 21:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94729">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گلگلگاگگاگا</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/94729" target="_blank">📅 21:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94728">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY44kEbFaZw8bl_EP7oOvlBuylWk9y7LW_q33iKXw848Pdvb7wgNiYGrXv7sbtGc_U8xLWIibLst76URi5vrdCG851yQFt2_VD2e-uOHGCHNQ_QLTmr9h3v626BuDxj66fEGz9yNHueKwpyJOPryi0j-T6-tEShc101MH9fPrbj_ztWaGlf0XdCPY-odKLu-dzDET1WfgWAsyFFjN_n_fVKaj2LXej4igWxqZgJQvevKaIebdEMglKgt87Wg4WWVT9VxO_X3kT702fxE_eeuIvk9cqynDhbdE9n73ZB4mrtT5fhj2giVA84M1j6M69rfEXB3FPas2ZJDegKeBsoslA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب شاهکاریه این
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94728" target="_blank">📅 21:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94727">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رفقا سلام و درود
اگه محبت کنید حدود چهار دقیقه زمان بذارید این چند سوال ساده پایان‌نامه رو پر کنید کمک بزرگیه.
شرط خاصی نداره. ایرانی باشید کافیه
💙
یک دنیا ممنون
https://survey.porsline.ir/s/ngmblc2l</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/94727" target="_blank">📅 21:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94726">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">واااااای چیوووو از دست داد سوئدددد</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94726" target="_blank">📅 20:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94725">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dc96d2cae0.mp4?token=qSL7eAvbNjjCp5wZjAeCs-viKeVmE47CzLhIxs5UlnpLm-qkWozfeA25hxpIy5DpZdkdGNyjcoey8y_ND8yfSiW5WeeHwupm33HUlvZcqHGjFBkOemqxHs49Fkg03hAeT4wq7_4TngF9DvA7l6nxZ4_3jEQsAD_DM4wYok7ezYynLtmBLZ7ZCYWDVt4t7rEoHbh3eCo6MfxV6r00l6vF-sXtIQbAtIJJcRoxFo-fbOzxjtLlm63oc0iSFsMRNxh6YfR8IOwbv6zUXsn64qqKxmNcN7V-lNgMf0x68CIewwxzNQgPqfWSxZ1mM7wNchtwNSrEInbRG2baPHpDi003-Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dc96d2cae0.mp4?token=qSL7eAvbNjjCp5wZjAeCs-viKeVmE47CzLhIxs5UlnpLm-qkWozfeA25hxpIy5DpZdkdGNyjcoey8y_ND8yfSiW5WeeHwupm33HUlvZcqHGjFBkOemqxHs49Fkg03hAeT4wq7_4TngF9DvA7l6nxZ4_3jEQsAD_DM4wYok7ezYynLtmBLZ7ZCYWDVt4t7rEoHbh3eCo6MfxV6r00l6vF-sXtIQbAtIJJcRoxFo-fbOzxjtLlm63oc0iSFsMRNxh6YfR8IOwbv6zUXsn64qqKxmNcN7V-lNgMf0x68CIewwxzNQgPqfWSxZ1mM7wNchtwNSrEInbRG2baPHpDi003-Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل دوم هلند به سوئد با دبل بروبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/94725" target="_blank">📅 20:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94724">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">عجب بازی ای شده
🔥
🔥</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94724" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94723">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دبل برووووووووبی</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/94723" target="_blank">📅 20:46 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
