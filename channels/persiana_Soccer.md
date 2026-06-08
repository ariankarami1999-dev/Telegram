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
<img src="https://cdn4.telesco.pe/file/UFZFuPpqtpqT17vPpDYcbvd4_m-jOuj-h8lHn3VLkjmDE2_LEzB9IvJYi5qsXUv_U9GbRilzhets7WB2rtCE3NwdMwYxnmFblglfyAUr0jJ3PBHY_Rm7wJBvaHJvweAMFUhVE3J6QxPp7M5rIfRwB-UhRFppFqGSVqWyu81tlyb5-l7aCBdpPF-nP7UyOZO6pAOteLFjD423rRiiELGcGN79GMAIiBNMnnhORec27RNHW-fgi2cSIz1e6Fjm6hkisI0zt80OwNmi8FOz52aQvBa-IH_SXOG-sKzke8VH2wjng-Yu7-VBAbhrscwKesoQONwExcgC6WXFNb3PyWiZxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 170K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 21:14:30</div>
<hr>

<div class="tg-post" id="msg-23016">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Icg5iHs-Bt91nXWzbCzbgfCIIgt6Y0fID3paa5J2UGA9oU7fDio_IPudUSJ1s9aRALB97TE6PYPy2mZzncRbfrZFqfvDE1ndlK0R14H6BsHeIN2xVLPzwJRvoPahr6tjKJC4mT1RcIuGByJrz6xirPxMfn276cRYWhuI1XoXnhfExldTDy2CD6gbZUF7vMdmoSDLpyLdaPb9QxWpfKdoN7bCcWZi-PXL2PNKMkvboUGtQ7O4oPSZC_YeqZn-QPiDv_fcNBMo5n-Q9QfFCQRcXXLbIiIpjEF8OMJr_wf6IHZ_rwALxQ-NIdpmp4kkJe8r8EiEE_0s4Aw2zh3p66q8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/persiana_Soccer/23016" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23015">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPMxCMZA8bUJhYvRkCMEaiIDM5MHMjFtI6pCl7bosHnapSiY5LEwLHcotcb7zF0KYJcOrdgvu3YGuC-7EJKD58uZYcKuizaxKphP7pRqiGrJOgcKfvyxuK0E_7szKhsrXE9BpcdIq1ZgZnBMIgQYHg7cWxong26seg_UyLkFzmkQ14gXmaASbczvDW0PhyRlBPwn3J2r8ry_5YHt-FPwAAZD84ldZ1rL6sijXD0r-nlLKeyPnQLwZTTg1NcOQW9oT8ta0_4F1QQpZPBMdzVe3Z6HxNYiEYb0FZIY3kAJr9bYfys_0jjc3R9a2XblJbbSSzaKWDBfZiYXIGw6Ysik-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/persiana_Soccer/23015" target="_blank">📅 20:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23014">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=AldWCLXBTHyyKXqkCEfPfEooKom_XKnPrC8LhQB5OZc52xSQqVTm9BqAHibDTngIUVGiHxaWDiEhu2Cc4-fRbBol36qE5TMlOFwhGW4pxcl03CLDNXdaBKByp-8j0-ttJTymZqTiTNmXNAMFfzHSpeb0xbFCs1yyoXNidcljXyyunRU0gOgfHPIJ2HpE8SgnxAZ_T5q-qQ4hYxADS5x9OYX5PQ5MC3gTBk10htvSxIq6b-fFzlQOQMD4QoeYmBDtaniMjp8eODTj_u-IdAIOT4wWKPy59Y1BnZJlGsDDnybSObR_z1YtXuipGp8X1mdb9yIDa91TEBlqw5I4hP-LbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=AldWCLXBTHyyKXqkCEfPfEooKom_XKnPrC8LhQB5OZc52xSQqVTm9BqAHibDTngIUVGiHxaWDiEhu2Cc4-fRbBol36qE5TMlOFwhGW4pxcl03CLDNXdaBKByp-8j0-ttJTymZqTiTNmXNAMFfzHSpeb0xbFCs1yyoXNidcljXyyunRU0gOgfHPIJ2HpE8SgnxAZ_T5q-qQ4hYxADS5x9OYX5PQ5MC3gTBk10htvSxIq6b-fFzlQOQMD4QoeYmBDtaniMjp8eODTj_u-IdAIOT4wWKPy59Y1BnZJlGsDDnybSObR_z1YtXuipGp8X1mdb9yIDa91TEBlqw5I4hP-LbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ما
مردمی بودیم
عاشق فوتبال، تو فوتبال هیچ دستاوردی نداشتیم ولی باز هم عاشقانه دنبال کننده بودیم و دل‌کنده‌نمیشدیم‌حتی وقتی هربار بعد از یک شکست‌جمله‌کلیشه‌ای "این باخت چیزی از ارزش‌های تیم ما کم نکرد" میشینیدیم. بامردم ایران که در جام‌ جهانی 2018 روسیه بابت خراب کردن اون موقع طلایی مقابل پرتغال اشک ریختن چیکار کردین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/23014" target="_blank">📅 20:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23013">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI2jzO_6c5VZgFdSNKiw0SN-ZKtpKSZwApDsv3F4vzLWxwc1HzG3ewPtQ474rJyzgn_okS12CNw5OlFDjkNuL9qF1ByncVOqKMxPDCV0wuXQXPmvoWPYoGyKFaMbk46T03dL1qqPMqIRVxZT0ulWANb4zgXEuXBDveh0uwYZF1_jv11dtvkTya6TUL27a5SwyOvbIx5Z49pS7pbVDtFMzNwyKDa0BSehhJaRR--WWkt8-QUMSB8FZ2AqCEP0QOZtNkljws1In3fFUb-Ig-IVC8Ydv01RkB4VVtw8_b7NzhkXqPGU8Foc6lcQR10FRzJd93q2fvicN4SwTLYWTDMuYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/23013" target="_blank">📅 20:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23012">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbAp2fx5XydXLenPLnJGUwURU4GAFzyVfJiJ4Qw6qhvw4S6WGlxJinZCOj3AlwD9CbRFWGFwK4z9449QmAxwJ5rGmu7qIsV7FDKFMSF8_jhxRZlSYiWmWhJLCXmpzlShvMXF0gWXwPo0aGkrUG9cg1aiNQHnhjoJPN1Dy64c8ZVEe4GQ55sJq0kCYsQaQK_iZIxl1KNqSe8kGt52hNcuyMdJpcoebXYykCJ3oaujk-KCQMVBNQqF7p20rG0m6mc0fD8gmNkCxRy57W-F9aHJCgR6KZbp7PfIimn26D55Q89oIrOljVB-CtHv6d6mqwskKulQppmOcDIAuAqqbaWfRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/23012" target="_blank">📅 20:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23011">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29259cd165.mp4?token=vRzkHXmncDEQEevXAPfUi7aVElcB9uvTGTuYmycaCe9lrMsibgGSpH47C5lsyRfqMNTtnCh8i-522I4h02FS4U1jLFO-gF_vtx4pYrh8SlDdfzjIAjlxc3qjrHMRSc3wvDGvL_dczfa1ammsS1K84q_gVL1NkLeIQzEq1LKVIYach2R9dDD7HtdSywT6vBBNHWMFd3BtqX6039g6GM0BwAANwO85bhenuAcLcZZRApWWzImn2lRyz1NeBvd9bYbzOIwX4kX6tMElak0_N9-TwrLMKTt1lRyjzlC4wnfLcTBKo-2nZfRhc4Kj4xtj4bc2ax9gC-Eb8PO0tSa9D2sGjlbPoR5U1PBEx47BLTzkNbk4Np983sKkRENjGpoGLD0mGDBvrWndQ3KoPr9-5EdCiUIZFPklka6NJgIyCG2iOREaXfYQKaF9cF-aJd4VSnUemOBdqKb29R8xDrYkUj_HOTA1xTj39zOlZFrRAozk6gLdtu11MQxRASE_KHWloIMAGm1XyhMvvt-7mP-9s9wmbcVCDgd9oMviR21cSpX766S61Q24EplLkNYgn03AUqRZ6KIbG_ITR6rKqQYmsU3Gsn1slaZGLHCS5lJRvwHGgZ2mLHn0V9tlsIJHVrMdwVMfxSeeewoD7OSFlhLwrwAlb9xbcqhk-85Vdq3wd8LVHc8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29259cd165.mp4?token=vRzkHXmncDEQEevXAPfUi7aVElcB9uvTGTuYmycaCe9lrMsibgGSpH47C5lsyRfqMNTtnCh8i-522I4h02FS4U1jLFO-gF_vtx4pYrh8SlDdfzjIAjlxc3qjrHMRSc3wvDGvL_dczfa1ammsS1K84q_gVL1NkLeIQzEq1LKVIYach2R9dDD7HtdSywT6vBBNHWMFd3BtqX6039g6GM0BwAANwO85bhenuAcLcZZRApWWzImn2lRyz1NeBvd9bYbzOIwX4kX6tMElak0_N9-TwrLMKTt1lRyjzlC4wnfLcTBKo-2nZfRhc4Kj4xtj4bc2ax9gC-Eb8PO0tSa9D2sGjlbPoR5U1PBEx47BLTzkNbk4Np983sKkRENjGpoGLD0mGDBvrWndQ3KoPr9-5EdCiUIZFPklka6NJgIyCG2iOREaXfYQKaF9cF-aJd4VSnUemOBdqKb29R8xDrYkUj_HOTA1xTj39zOlZFrRAozk6gLdtu11MQxRASE_KHWloIMAGm1XyhMvvt-7mP-9s9wmbcVCDgd9oMviR21cSpX766S61Q24EplLkNYgn03AUqRZ6KIbG_ITR6rKqQYmsU3Gsn1slaZGLHCS5lJRvwHGgZ2mLHn0V9tlsIJHVrMdwVMfxSeeewoD7OSFlhLwrwAlb9xbcqhk-85Vdq3wd8LVHc8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/23011" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23010">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYuy5VYV3-BebA4gB8_S4riHk1yL0RIdMUjld6v9AmYvRm39bcC6rPNyIn5nglZBz_3EekZQHQmNihww_bwI_Hi7xIE_oqW3KYF0ZIE7MtBZYeTesgzjFwXzya3Vw1TYDro3I66jWIUzXE14MSyFiPich3M0vmFGNGmocxTu6MrZlDB3WS2G37qJvpYHL-WCoPKUMqJHJ2xjlDDl_JFsCxE7-49OeYt_RCv1i4nLU3Yn104skW0saC91uw0ISBKr6QuzdkTkadTv0gPFNrWJmz6LDTQJ66vStg1UICj_GSy_nDeDzO07WqBLhlAY0AhqggcoXn_LjctkF_MT7EiXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/23010" target="_blank">📅 20:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23009">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j92rMftzWhqto5RtBsyTKgz74zgizpLk37Oij546OmIFGfIjbLBBg6P_DXosVfLirQcI8MaFJvCXi0JNJnaw3xkVq83TZ_kmIPSNYjsA_TvRvZRv2gRWnvXlIF93scfW_MDJBZSsTwVtAq9Y3-aGSmyJMiLdnecNc5gDo2jRhu_W982N755GIbXHXfWH87f18_r-S5YxlqKKOIPS-NkKbd75VQmHAo4zReldfeqx2OVOgqORy-Z-laABJK3ianeEjh0HeYrsala8_4GYZivMXiRRUF0fXFtpsXBAiu-hlnOWP3ueeSWRqXiwDP1Yiq_FWTHDEQaY1RjSzGg6i6iT5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیست ورودی و خروجی مدنظر اوسمار ویرا برای فصل اینده رقابت‌ها به دستمون رسیده و بزودی کامل پوشش‌خواهیم‌داد. علت اینکه یه چند روز صبر کردیم این بود که همه دوستان عزیز کانال به اینترنت دسترسی پیداکنند. ویو کانال قبل‌جنگ 65 70 کا بود الان با وجود اینکه نت وصله…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/persiana_Soccer/23009" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23008">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=slROzlJYtpUqsKLSw5S7llqc9ebP8-YPX9UbNBrD26krcTg8lm9umE2q0R6QbsoVS8Ua8Fh5UQFMur8u8Hjf3h8wM9Nek2D_pTbdSYvSBdTLwFPfUOfGHw8W5bqwgyvrUFH7Jrq558QeXX3C1_ggllO16Kr-0xnkpwieeXL6TY-Uq2ea766zSZnpIxS3ys34ZbALZqcosXDy-vcr-okytqZE0UeFNYHWohEUJWwu2z6tagek1BECJlFOG8Q5_23AaRtb9O5I22OhxzfJr7L2QvX1Y45v_my8Jmk9EECShTpR0bb-GuFAXBePC9MP8E41C8Jd6fbHvR6sb3Df3rvhcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=slROzlJYtpUqsKLSw5S7llqc9ebP8-YPX9UbNBrD26krcTg8lm9umE2q0R6QbsoVS8Ua8Fh5UQFMur8u8Hjf3h8wM9Nek2D_pTbdSYvSBdTLwFPfUOfGHw8W5bqwgyvrUFH7Jrq558QeXX3C1_ggllO16Kr-0xnkpwieeXL6TY-Uq2ea766zSZnpIxS3ys34ZbALZqcosXDy-vcr-okytqZE0UeFNYHWohEUJWwu2z6tagek1BECJlFOG8Q5_23AaRtb9O5I22OhxzfJr7L2QvX1Y45v_my8Jmk9EECShTpR0bb-GuFAXBePC9MP8E41C8Jd6fbHvR6sb3Df3rvhcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/23008" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23007">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZiJ5b2qhaY4CB_dBCNXXN_uxIZtwLpiTvXxj2ir-JyJM-_ctkUIaDhNCS_pDG4P1R1qUklGVqs8dC_CPL8J9r3pyxQSAnjXS7DZsanswuF5lT1D-roZif7ixcryHK7vnyAIVrNaFEQBXXOVcGq26oJTlNkinsOu6gIAaxeHMYrKNhhpqFF1T0uCFxlFAJV6fDi0ribpAEfeW73HZBaA7SW-8wjt00CJr31Dtkt57ZRtSX4qbe1SHNsFaLul-i7g0ksDZpQoMvIcicJUogW_CgfeAHtSAgtXmzCbEaNiaJN4Z3gdI-Yh6IfqVdKVEcjCUVXx4qhYersMRiuWR6_99Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
باارزدیجیتال‌حسابتو شارژ کن
🅰️
🅰️
🅰️
شارژ اضافی بگیر
✅
🎁
20% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
همراه با درگاه‌
#ریالی
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
18
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/23007" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23006">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUws58UoTO8kclUEERXyAJOArfGdK5zt35ijG_CRw37ZHP8TigtYTVnXqrXUf8B1rGc96Mt8pcmLMUaTbyqEgqehsTRa1MYFB8OpoJRZaAuqNXnhALyBiL20_HmrHa0EPJSeuh_OJxE9jP7NvDwwyDJowJPXKhNn4NTuqxYzdqcbuFgbmQjzF7AWjxpDK91J5fp-3bFFy_YPtmYyzh-JtWj0L05v7HlnPEDVRHNsEH-Imy78v51CP1ksj3BcFjH7_gofNcSJgnSDyp84gNdZoyq1fhBgIC-xU9GdUqFGVbpsywuLnLUxYAxiFsNcbGBxKgRJfNzacqwC___2Z0c7TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دبل اولیویه ژیرو ستاره39ساله لیل در بازی شب گذشته این‌تیم‌درلوشامپیونه؛ ژیرو در این دیدار نمره 9.0 دریافت کرد و بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/23006" target="_blank">📅 18:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23005">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiEFI69UkyialnEvwgqA7HUeyldxMovLhzZQ2MYPEV3parpgrhf88mb6HT6_dF0bLUgWR3U8sKDOHsqnCVqbmP2UBwP3wO-Wu0gSGiILdS_fvn33zLXuK6RBDllQxczfM-B5UAd3gCTmTw6wvV29WGBGfix-upVmaIHNALWJvqn7woffoMN3A1i4-ZAC2iqa-3byGRJ0zT_BkAuqNTJNgQosDtSeAtlmo2vOmZAUZh-lWTEEBLzv-v-kCG6YQxV9NSMVn66TlsPS5CwP3nv1T_865lg98BVM49KCBQeCgTcrnMADLKkgPw7yDt__NpPn392MYeaVeDU_hjyyKMBm-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه رسمی فیفا: دیدار دو تیم ایران
🆚
مصر قطعا دیدارافتخارهمجنسگرایان‌خواهدبود و به هیچ عنوان این رویدادلغونخواهدشد.  دراین دیدار ارزش های همجنسگرایی را به جهان نشان خواهیم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/23005" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23004">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=q0rnqx0laoY--I-DYOswhpwjlbFX3gGLTqyXX_zV52Uz4Pn4acpVPhqRAS3e8tCtFupJ2kGUkIfsuSlMlRcqC_9n5k21fokMN6xDqK8y97_9ID4abmQx_6OlG1QKknKZ6cvBx33FsgZWeoWdl5gYhsoVBr-LamklUFdVgcM-bXuhFbYGdCty1oROPKRkp9CiyzsoH9V6fYra6n-qhDG8OBVWopqqP9sCpWAYdqYwAZvWUFtCQfNPV2ol1lNI2VT6hIskXhH6tbKHJYKw0NRr9PgOMLsXDA2jZukZCBAqaq6QxjudpC0X0p94Bvs9-CvG51UdoH_kjrWoeKY5rpVZzzVvOEitRpW5K9m3cHDrsKp3LUonEJglf1Tf4eCuAdKLI9RVsS9lEK9fd95tAzVuJKTr4OFXijeftRRCQc5rIdET5VolyrLGw3zifwEJHwEO20aYdZH8sv11UFfvaqIM2XjHOKjtu_FFV2L-fncK7JpciQ0JrnmVYan1c7JNFlMK2Kpo7XINks1zl_apkYzyjHxYPlFszh1qh_IoDcWbqDksSOhw9pkXkKHhq-srxjvOk71R7d20bHVXy3-jw7Xldj0zIXgiEeVUM81Esn9xdGykHi913GnP3SSAKt4rSVBU4-n9if2DlQkHTNgNWeHybC0hDX055YS3mDhX1oTchoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=q0rnqx0laoY--I-DYOswhpwjlbFX3gGLTqyXX_zV52Uz4Pn4acpVPhqRAS3e8tCtFupJ2kGUkIfsuSlMlRcqC_9n5k21fokMN6xDqK8y97_9ID4abmQx_6OlG1QKknKZ6cvBx33FsgZWeoWdl5gYhsoVBr-LamklUFdVgcM-bXuhFbYGdCty1oROPKRkp9CiyzsoH9V6fYra6n-qhDG8OBVWopqqP9sCpWAYdqYwAZvWUFtCQfNPV2ol1lNI2VT6hIskXhH6tbKHJYKw0NRr9PgOMLsXDA2jZukZCBAqaq6QxjudpC0X0p94Bvs9-CvG51UdoH_kjrWoeKY5rpVZzzVvOEitRpW5K9m3cHDrsKp3LUonEJglf1Tf4eCuAdKLI9RVsS9lEK9fd95tAzVuJKTr4OFXijeftRRCQc5rIdET5VolyrLGw3zifwEJHwEO20aYdZH8sv11UFfvaqIM2XjHOKjtu_FFV2L-fncK7JpciQ0JrnmVYan1c7JNFlMK2Kpo7XINks1zl_apkYzyjHxYPlFszh1qh_IoDcWbqDksSOhw9pkXkKHhq-srxjvOk71R7d20bHVXy3-jw7Xldj0zIXgiEeVUM81Esn9xdGykHi913GnP3SSAKt4rSVBU4-n9if2DlQkHTNgNWeHybC0hDX055YS3mDhX1oTchoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیووک اوریگی مهاجم31ساله سابق لیورپول ساعتی‌قبل‌خیلی‌زود از دنیای‌فوتبال خداحافظی کرد. اوریگی با اون گل تاریخی‌اش به بارسا راه قهرمانی لیورپولِ مدل یورگن کلوپ در UCL رو هموار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/23004" target="_blank">📅 18:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23003">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=msS-52qvU-DumVl_IYmAzfeyGo1GCuZ6XYmbKoBfOU7x4Ho4TWOIeGI2o3imDPX2-0Yu1ODHXuPrJoXn8uqcHDGCoSuGbEcsm29bc4ZxM5P_Krw1NGvoEDV6_EQxKCF5XHuE8SNG-PGdAqS8zp3F_2BQ_VYorLp8WZPV1fH2r8ndf-DVsLvIrXPHZyjDTHj6xrWTm0JP5Qedn9rYxR0gdK75I6EVISssU8X85-LZWJrt7mSjhhuzi81z67a67xqZ-a19gDOJEwSPKb8M-1zDy2UU-r2WTjCxKe2knJ8UpVkpvZCCa3lq9LpQs41bb_FcHFGeluhLGOXN0J47rzgTbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=msS-52qvU-DumVl_IYmAzfeyGo1GCuZ6XYmbKoBfOU7x4Ho4TWOIeGI2o3imDPX2-0Yu1ODHXuPrJoXn8uqcHDGCoSuGbEcsm29bc4ZxM5P_Krw1NGvoEDV6_EQxKCF5XHuE8SNG-PGdAqS8zp3F_2BQ_VYorLp8WZPV1fH2r8ndf-DVsLvIrXPHZyjDTHj6xrWTm0JP5Qedn9rYxR0gdK75I6EVISssU8X85-LZWJrt7mSjhhuzi81z67a67xqZ-a19gDOJEwSPKb8M-1zDy2UU-r2WTjCxKe2knJ8UpVkpvZCCa3lq9LpQs41bb_FcHFGeluhLGOXN0J47rzgTbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
رحمان عموزاد شب گذشته در حالی که مسابقه اش‌رو 8 بر 0 از حریف‌بلعارستانی‌خود عقب بود در نهایت با یک کامبک تاریخی 17 بر 10 پیروز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/23003" target="_blank">📅 17:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23002">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C78TFYd9rWRqQpFCr69_irg2Qds5CNDPufoEEAa3yBqY25PJQsNE9NQeQ6w-wHVWQsm-UAE157a3-2KCOBI69K9djyhoItu9VJys51tt9UhI55ght7DL7bTMLMB2sW-A9g40UCIHUjDXbzUMKTQ5_eElKo2IcE1q-wEeMifvGlBsgw-5-UJ1wBpFi7pGWGd2mkwRPTeoivOlfladsejjf9ytQqmO_3yt8XZGjCQptM3EvyneWtAF1lwYj386TKStaRuKACfwkJYIxdiCkng2oKVFYTHXjJVKqyme6iSU4czhNEiiqLxpSlHnZPZjPu-mXMeaoY6yOsU-u-FkrZj79w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
پُردرامدترین بازیکنان حاضر در جام جهانی 2026؛
کریس رونالدو با اختلاف در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/23002" target="_blank">📅 17:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23001">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUS5oQvLBGceHA7-JkT_PpMcZv5HTPD-aVRYQiExPia6TKm1_y5Fo9_yJgmygzeDqF1K0udac9Vor1hiYk8GC1pIX1jIjo41MxqD1FoMQxdimIzYiOHEnCOsq-EyeW4w-xxP77giE3HMc88oREtkHtNGF2LgBZ3-J2XCDwNzQgQ3mpHX7tJDWdPsdHKYpnGHpqZZ2h2iNKbo_usSbo6EHIO4lcCprOl05wlSszh7c4Kw6X2NnPldzn7eeLcdvOn8Jqtl_loH0e0yBI3Y3Kfavb5yY2OtFFTyeIxgsPnu2Z88qpbmBov0zmXkiLMSAdByswlPD9aIPT6AFr0IeGkj0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌پرسپولیس‌بزودی‌باانتشار بیانیه‌ای جدایی مجتبی فخریان و یاسین سلمانی رو اعلام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/23001" target="_blank">📅 17:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23000">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S41UrDQ07KVKIe1R_PNXGjy3e6Mw11N1SquGuNSRNcmuUwgeRxi07rTS4JCvXJHbMqopLIvM3oZ9o3rFtPjSpAj7iyw1fOUJ1zHx4jRTbfbsIBiIohM4bZdogfAV1vzUjjwkacEdUuPqSiQAKV-M4k71izTH2nuE8UXQbqBspiKmlCQuzKfIkFLT5qZtY9aDNG-4GJ82L4ZpLm8ziZheal4143-J0TT2uL8WI3d2miHbusar2uxWw_Stq311sat8eL430WbQgJ9DUyWBsGI6GoCBEjgehltF1CbxCTKz_O9iz0edacyXBZuxNX0a70IBozgy40bNMxEEKjYV3BMYUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در این تیم، همیشه جایی برای پیرمردها هست؛
ایران و پاناما پیرترین تیم‌های جام جهانی ۲۰۲۶
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/23000" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22999">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvhFn_ILQc21JtcMMfQVw99qCmzukuy2V9Xxi7UmTeQ6vKlSorAhVQwUFIg5nWQH60j3Y6JPtkpfShbbJpQPjGY_pjM8Dh11oy3Cdo-0f6WlOrzRKu-HQxDsFCGrES0oXYTwR9FsnJ-HW255dEN-EjeKQ1J5Szh14CpKpxnBirw8l_lW3cYwpC2motMLMJvDdyR6yqQCxF9BGr048UDB2Ik9ArqMbziNQOUrxD7CtIUxmkSKNGdIuNMmUZgFhZjha1u9rf6iPwwgAkpUnytu19nbwygHiHxqkbKrPQjNeb-METxr_YC4kuVQlAmArU5GUHQms4LjR5AzfDW_pjBvMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22999" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22998">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbXD-9APXbkff5q35CVGalgeaEGaNhOIRWKck1tQv4wZ9QLz_wPDK3sPS5aFh6dlYicGd9Vd7wASSIyOeTejZJQ0_aMz2sDVaegM2DsRbi7Ux7TZ9gVFs9Hb4Fks1kbpOlacMZeUldHwDBZu6tXH2mw9qZ_i2hZ-jFUuf-_nlQ9ZNi48YgWO2yuo6My6QhC66pRr2J5ycSWN3E7tC4ptVJ_XYELjXxkQq57dZzsmS6hvZZTSg28fKGLk9F2orEsoNEaQZNOOkT3YZA8c3mztfkqhCNAQJChr95QGC0-v69-DJwSlVmulzzL7deeAhKZBEpG961PvBzYzHk_UBnEvsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22998" target="_blank">📅 15:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22997">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9QhhUIe8ce52IX358JgLGGj-d3Kb0b3IJ2B6kZZP2PmNP4NktrMKXpMI7_4A3O_Y-XAUYoApzsxMLAxAR1ZU38m-F-Ztoml98vRmQm4bdcAvoAUKLilH4-_CLoY9ztveXFp-3A-QyoXFbSHhafnSqwbLTWbi4TeLE4BMxmBGH7y6bdg1HsROQSH6wHZsgiIrOhOpJJxiGsaW8YWVFbiL8Qfjwr_eiW4Qzw28Nv2DiscA8Sqp-8zIJxH0_MwMNe_pdwNtjMBA4kRPy9K4PsyZoZUFz_wsrD-ZCioZAk_T4oMQ4-8E0NXMgFiUhs7buycWKsh_cpZQuKIHVCaUg05rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22997" target="_blank">📅 15:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22996">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=VspZuslhOT7MwuKfhqMI0ACbnUQPuKdOLJc5M7StYAFhjSWI-xBIf6zuwJPOhYNsMXdWgDHy6BRR2RgCAohbFzB_DIYCKnfg9s8m2bMGevnWWwSv5XGnieLTY8dyqxtmwshYTzUaqdYdB45cOUo3YHzGYzNjcdyxgAYvTOzgFctjET9oH97kOakce0pXW4Mza8krYci_YYEvNad8lPcbT8M2wMi1h3yowzTwSA68HzWdNY5ZM0XUQ4ooFtX1dnhdI4mLfCyqtpl6Onr-ikZu-dh6LN7QzvLbhFqv3KEGu8wIG9o8TflDVYjbT_civzKSvXv2st-SPa9XSWb-rkXPTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=VspZuslhOT7MwuKfhqMI0ACbnUQPuKdOLJc5M7StYAFhjSWI-xBIf6zuwJPOhYNsMXdWgDHy6BRR2RgCAohbFzB_DIYCKnfg9s8m2bMGevnWWwSv5XGnieLTY8dyqxtmwshYTzUaqdYdB45cOUo3YHzGYzNjcdyxgAYvTOzgFctjET9oH97kOakce0pXW4Mza8krYci_YYEvNad8lPcbT8M2wMi1h3yowzTwSA68HzWdNY5ZM0XUQ4ooFtX1dnhdI4mLfCyqtpl6Onr-ikZu-dh6LN7QzvLbhFqv3KEGu8wIG9o8TflDVYjbT_civzKSvXv2st-SPa9XSWb-rkXPTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال ستاره تیم‌ملی اسپانیا و بارسلونا درباره دلیل بستن باند روی دستش در حین بازی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22996" target="_blank">📅 15:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22995">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GG0MPrhWISxO6oYWhy4nGiRGR7Fx3tXst5lw3DiYcnsevXcD_lXSgOTKgll59r5gADQYe9X-ijHDU8XsTFwBIHsdXJOvl7kZuvrlE2euoSWDsqeZNe-oVFy3ExVb5tNL640kwil1PK0yxRwfbk0kBOCOaMflO7M1I8A-Cd84sJpcwfwMd8hebqMMzQRLl7gWAY_qLG8Unben2n6pL3Am6x0DUx-hB8bNVzLKLtFPJCqLO1P0aMBhQoGjfV2jifjcXpjQh-wAXnplQM0xL6npZuHBwH-3imRaM0MreqIxJHNx-2gR7dOqYFRxyvM_45UJrkA_DIhkIs3NEHj8clGd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نقل و انتقالات تابستانی امسال برخلاف تصورات بخاطر بحران‌ مالی‌ باشگاه‌ها؛ بمب های بسیاری زیادی ترکونده خواهدشد. هم پرسپولیس هم استقلال و هم تراکتور و سپاهان خرید های خفنی خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22995" target="_blank">📅 14:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22994">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=fY4JkHFN17ft7KOSV-POy4SzUhUhC0kktKbYrOHHcTf2mL9z3uxeJlrbo-C0FDjF3yS271w6zvfJZsp-1PyHvGdux4ziorl0qFhwNVlxTn97kR21Z5cPfw0Y3qxd3znaBeMSUqEPU_kJxpCPELPeeeH-8Bcy6x9ouQkcfRDvF_j-kaw08RuDxXKNr_0tMTfEk4am8tLpoERe5FaG8RYSy3iHFa70ri6dpC3wcaJNgyDF6mk1syUY5KmdjpY5kmCnRThmgeBNC7-3HEnet23-VAmY6z33It8KIRHt7IvIlmyboygPeXPGRs-_Ytkpx4yMxpi-SpT0jMNL23bj01zVNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=fY4JkHFN17ft7KOSV-POy4SzUhUhC0kktKbYrOHHcTf2mL9z3uxeJlrbo-C0FDjF3yS271w6zvfJZsp-1PyHvGdux4ziorl0qFhwNVlxTn97kR21Z5cPfw0Y3qxd3znaBeMSUqEPU_kJxpCPELPeeeH-8Bcy6x9ouQkcfRDvF_j-kaw08RuDxXKNr_0tMTfEk4am8tLpoERe5FaG8RYSy3iHFa70ri6dpC3wcaJNgyDF6mk1syUY5KmdjpY5kmCnRThmgeBNC7-3HEnet23-VAmY6z33It8KIRHt7IvIlmyboygPeXPGRs-_Ytkpx4yMxpi-SpT0jMNL23bj01zVNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بازیکنای تیم ملی فرانسه بعد دیدن اون عکس و ژست سمی رایان چرکی اداشو درمیارن
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22994" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22993">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7q-rGHBgR5xIrV7cr9jpNUSnCKLtfqAgLMPG_QzjTdHEo9m1g9EGsoa6vCBD15KYvnvnGZL0nZ_q6yU8WJUuYoabt9dmT2TTCWC83oUSX7qeX8rJ_HOLI8t2Vtx2VN7ez7gEYjGd4GA7hcnasFNRfNHecx-Jdp-GLbWldBckT45XjPjqeW-cgX8U3Rrss3C-umQngN6c8CcFcssJ2f6CaG1xghb79l96HQa88OFMw7oiNVr26l7t8SpTmVFNsaP4A10503jYuSIoGVV6gLCDvDV8AzQ-WsdFd9BNj1MJQhP1mr_kYGNSb9cNb7DhvtMX6LcNw7_AIwjUwZCkP_dvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22993" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22992">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3s7Pqn8dZkWsMbiqN5lgvl2TdRBTxonj38inyyxSbprHaP7iRW1iiaNsu7L4FJ_Ecn9ij8uEV_RwQG2-C7HF5NZLQmEkR0wAXtmomvJlilo_qpqRtrKNcbbXTIVP_bF99zc_QPQmKelEud76HKh6S5UYPLUjUH8_cwGsqsepEen9L-7JOG1zi5Jya8D4y1wLde_2XU8LeSu72iWDs-uPWXzcbmpev_5XYgABSPgfETZwRwLemLskbu2z-Ngy31Br37V-DX1jNSUWZnC1-BBnTyQannFTCXwm67VcfZjxQMjIYowchS33Zm35BUsjQEBheJFgnMqk_TZIT6dC-XJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22992" target="_blank">📅 13:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22991">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=JXvNiuiMDjfb_X44tygrHD2ETQEXQ6iwtZSfcp65oGrxHxhH93_jmOKdZlIg2jySn8ixUIaQJZvtgndqqs08NPCZVllPkKsdegeAWYDwQFY1XOLBOZ5XjimOyQQw3UgQlnlx3wE4iFaZJ01oZVNpfxS5WB72OwUGp_NkEItu2K-sKHGJlr5mKNBm9ZTh-ARjuA1gDf5p-0mqhj1itJ9YLKOqu5JN7POOQwtAMu8r5WfaJAcNynsbQcp_-LJghUtSi6S6Ucy6YvduusgU6GC8qb575-zkSnibqeBm_PNohJ7Z4BQqtuoTcyFNk34yq5gNr1k50wT5agZ-UD0JjMpc_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=JXvNiuiMDjfb_X44tygrHD2ETQEXQ6iwtZSfcp65oGrxHxhH93_jmOKdZlIg2jySn8ixUIaQJZvtgndqqs08NPCZVllPkKsdegeAWYDwQFY1XOLBOZ5XjimOyQQw3UgQlnlx3wE4iFaZJ01oZVNpfxS5WB72OwUGp_NkEItu2K-sKHGJlr5mKNBm9ZTh-ARjuA1gDf5p-0mqhj1itJ9YLKOqu5JN7POOQwtAMu8r5WfaJAcNynsbQcp_-LJghUtSi6S6Ucy6YvduusgU6GC8qb575-zkSnibqeBm_PNohJ7Z4BQqtuoTcyFNk34yq5gNr1k50wT5agZ-UD0JjMpc_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرد البرز که بهترین خط دفاعی لیگ یک را دارد و هیچوقت دریک دیدار ۲ گل دریافت نکرده بود. اما فرزاد حسین خانی با چای نبات و شاگردانش در مس کرمان موفق شد در ورزشگاه خانگی فرد البرز به این تیم ۲ گل بزند و ۳ یا ۴ گل هم ۱۰۰ درصدی هم نزدند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/22991" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22989">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J51L8pvwybOBjv2Leig4GykKBwj4IHde_SQlye_pIahCAU1MIur3w0xGfFRWSk_M-L_kla3RqmuHkOexRu7v1X12Nxm-r6zMipfiK9tWrG47KqGQ58v-txZx_XXPrIaL8fV9bi8zUumhxek2-dVToQzgZUlf9ZW3XQAgEvLaTHipXmTp4IUDosWJArKbwJEOmtFiIEaGK-SZ5Q29Jw3xZszXr1tatK7vBZDGpW4Lvm49VByTas1K3u8-n1zFG-ob17V3a8XGdxnT0T0VACad9SJQYhQDDlS_L2zgJfuzodGsjOT_Dbms4hsuZZuTOK4aWg8DQGZ8WGDv4wc0WLLGdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه‌اتفاق‌خاصی‌رخ‌ندهد؛ اوسمار ویرا برزیلی چهارشنبه یااواخر همین‌هفته‌وارد تهران خواهد شد تا برنامه‌های‌آماده‌سازی‌پرسپولیس‌را از نزدیک دنبال‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22989" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22988">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HroeOGKFzmue2hXxkbEN-2eETIiF5RmjA5G-uHooE54NdKWQKUpdY4a9DNu2MA6FfyJzwDf3PSsAM70e1PK4zGpZbqFBAoLoBiksAjXwrsCS1aziHJw9ETXcZqDkRoztmmiqBEvDxbzG-K8m9JQAPh2P8PJRJ_LSACSIplihPhx7w1aR9DEQeJN0NWBODiDwf76_eH5E-iFwKEfZ6os8wmSrOQ0C-ImIzon3-WH5lNzYU-9JMGh7iFsW9VkYcS7Xvg1PXrKoBavsD_Nq3n3KQPfqjhinhA_woJEoD91bjKUYjrhTRZNQrbTnpjWyXW1_cM-3WAET965VzP12ICa9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22988" target="_blank">📅 11:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22987">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=T5oXp2zTmUfrAyq7lNahAyCxVIJD4lltVa2ixAjkD8TdGrsT2DH5noIMTIRw4pnKc2sNW9fEuv9-GHXaSQXVFEEN3bTodtxCXbC991Bz0KhiMf1fPZSvXTN-6-0f5B9YV2j0kQx94RS8cyw5JetS-SGWF8RMuDmtPFDNCr224lUVJ8OxxjEmFiRMqSEtuWputy6LdUuY4JaK7yoe5LyfKgq0QF0ERUV1zsnpTBCu9lV9Wcjj4duPr_GpFBdwEsvZfxokSuDHBIzKsRqBB3Y1M3OG-f7KKJufBopxmTJ_yWt5pZNWcid8vIdYptzXkQqUDWCj-fZHvgDGO8g7ZL7I7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=T5oXp2zTmUfrAyq7lNahAyCxVIJD4lltVa2ixAjkD8TdGrsT2DH5noIMTIRw4pnKc2sNW9fEuv9-GHXaSQXVFEEN3bTodtxCXbC991Bz0KhiMf1fPZSvXTN-6-0f5B9YV2j0kQx94RS8cyw5JetS-SGWF8RMuDmtPFDNCr224lUVJ8OxxjEmFiRMqSEtuWputy6LdUuY4JaK7yoe5LyfKgq0QF0ERUV1zsnpTBCu9lV9Wcjj4duPr_GpFBdwEsvZfxokSuDHBIzKsRqBB3Y1M3OG-f7KKJufBopxmTJ_yWt5pZNWcid8vIdYptzXkQqUDWCj-fZHvgDGO8g7ZL7I7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نه‌داداش جبر جغرافیایی توی پیشرفت آدما اصلا تاثیر نداره؛ محمدصلاح اگه تو مازندران بدنیا میومد:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22987" target="_blank">📅 10:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22986">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=CEAqr7o5_lCIqdjqiet8iO3W5pMC9qyjUnhTLCyIcSa2Kxjuyl0syyW3gDYvhCeu43hLOGPTTX7bMcxxixsPYPB9Ca0BxMiZ2tiZOq31tk-PdMQcqd7lUe2AT24cNIaOArapTHkhj6c3w4LyGow5AhyEdHg9GCF2GjKheizJS465MS5UUzdr6ctTneRBDf59nOAAT0vVbVf8g1z-5iC_CF4SbVj-Slz3r3jAZJY2CkqIIZ6X0ubDcI36u7ogE3xMqM9pGAx1Ooc2jC7_klC7rZilD2dHUWLbGYR1BQQGTyNNxX09iluudSHJaKnar0M-4gJpwB23CE87hdNwCTmLRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=CEAqr7o5_lCIqdjqiet8iO3W5pMC9qyjUnhTLCyIcSa2Kxjuyl0syyW3gDYvhCeu43hLOGPTTX7bMcxxixsPYPB9Ca0BxMiZ2tiZOq31tk-PdMQcqd7lUe2AT24cNIaOArapTHkhj6c3w4LyGow5AhyEdHg9GCF2GjKheizJS465MS5UUzdr6ctTneRBDf59nOAAT0vVbVf8g1z-5iC_CF4SbVj-Slz3r3jAZJY2CkqIIZ6X0ubDcI36u7ogE3xMqM9pGAx1Ooc2jC7_klC7rZilD2dHUWLbGYR1BQQGTyNNxX09iluudSHJaKnar0M-4gJpwB23CE87hdNwCTmLRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ
؛
مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22986" target="_blank">📅 10:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22984">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PChUvRqqhNa_4Is8T0QoRgpQm8s9rnmu6q3qV5FxN144zetcl0fvrMf2DU2_7MtTqhvPke0QtFy-SDRoQFsHAOheh0pLngdT7CTIO0GNyNAPKr4b0GKnej4CwXnXTM3ARj9SSGcB3mEVb18WHeInYJ38LB8fasG8eGIFkDxAojEfEvEYgsLloci-yfqipPIp5F31Yz9__D1dyKCxs7m3l4vIuI3OvmfsTxxOU2ck-6lEKycDUjFB2GWPKpNJaVb45LQZYxWHGTwok52tsZ6tFe_4A79r0EjRGMZ3i0s2ktnYRTArXs7piBJDzDOJoPHgB1wZjbUBo6C79qZiu_uRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NA28acDsd8L1x2-ZIG977mW43EWgxBt8O5k-E406WbNFcSgZXwLcZ8vm6hDVdDij9B96wAXMClU7t967hugMYJ63Ts4uZI3wl_i4B9tH7Vj_f0qpjNGuzE7JbRARe5Dmg-jR4-G3j9mRjYUjBLaNf8HXq88jfyF_zCiFv5zZEKAUYGUGHKKoWi3XdmrtRPRZhqU7ys7y45OYdaA9XHvOFeo6odkjXTzaLQ9L2uk2scOPG3kK2KS2XIdSZ4qra4PLsJc5IkpjvA1vEvCANW88Ek0w1st1D18K-UQehtI6ySBgjCIB_W9Yt2QWBIB2u47vzO_IeO4SXEluW792l1im5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.  مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22984" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22983">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=fyvVwHJht72WuCVxJu9U0hmOaQUJJzyNKlucaIePXUh-vwE4GxQTtI9TrFm8Zit9gixwW8xPvreCjJcJMmltafoFojSy2kC9GqtpE7xJZFrs8jWOmlcdrqwxjoXYme_pK8N8Gz_bLmStFl0YyNVy-S9TphpfugATaQIfClqFspoFUM2-XYpa89aFxzBarKq72bPu8QgaMd_u9sTiEdfX-oufaJmRFuwCMP5MaxYc79tc2avBgdfaLoeb_YS5FXu6MkMuHq4m8cYNlv158mDUb4jqDudQjIHt0NbCR_z4X1QCuG56fNnem4T-W0keX45abmpoNJZAXRdyR_az_KTTUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=fyvVwHJht72WuCVxJu9U0hmOaQUJJzyNKlucaIePXUh-vwE4GxQTtI9TrFm8Zit9gixwW8xPvreCjJcJMmltafoFojSy2kC9GqtpE7xJZFrs8jWOmlcdrqwxjoXYme_pK8N8Gz_bLmStFl0YyNVy-S9TphpfugATaQIfClqFspoFUM2-XYpa89aFxzBarKq72bPu8QgaMd_u9sTiEdfX-oufaJmRFuwCMP5MaxYc79tc2avBgdfaLoeb_YS5FXu6MkMuHq4m8cYNlv158mDUb4jqDudQjIHt0NbCR_z4X1QCuG56fNnem4T-W0keX45abmpoNJZAXRdyR_az_KTTUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نشریه ESPN: بازی دوتیم ایران - مصر در جام جهانی به احتمال فراوان بازی حمایت از همجنسگرا ها خواهد بود و فیفا نظرش رو تغییر نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22983" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22982">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✈️
معرفی سایت و اپلیکیشن مل‌بت
🔄
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22982" target="_blank">📅 10:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22981">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mf4L-n623iNXuLUY-RgCNgzSGLuNes1Uq0qNa3I1rKhbknRecD-5j4boXt3e9k-JKe8E6G3KAWv2Vk4GSma9tEMFmlrbSrQ8SbW9BRGP512UZZYJM_V7duJrCT8B06P6vC6ZyW-t8VBNjnGhMys63caPxjVnCWKsVVEUq_MghrV7Yo7T9K0GqYMgm9JfBsgiM4KhBd-PDnWQk8daKQi9jXd04x2rsMbk_5nihg8RGxdH8TSBum55BrKrGuqOg83YvPRmIGi_uI3CukRxCkQS3zGwqlAnu8LcZ30HwCPCS1SflQemoX2Yb6carZRGgfte2PeRlmU3fVyUcflZDhi_MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22981" target="_blank">📅 10:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22980">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmHsAoA9VLqcZnwvLn0yiYbUOB1P1GlXzyUWPGXLNcJi6dLKmvgKHO_n8j4f3TLkt4Ko0cHTUSrfSTd0t29kwPTBk1jeWpNlH027B5TfYzE1XE_2JQm8IIxmSYQ-ybPDGJbwfd-vfdRpiNYz2vLwQO7-WQDLebji4KgvhFwPWf16nLVm_YARzJaT4llwLsOwFfQTd2UeXZwjs0LoVWuliVo7_2wfgqDnudV8NjnqFFAoN8lect7BktxPCCZsQngeBDMCJXW9cvdSZyNZcFsvMFPzZ-ep9TbqPU1qVoDt0fxsULghvg8YC6VKH99yUh2wcqMtTarKSpd4VoOWdYrDcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات
|موندو:
مارک‌کوکوریا به سران چلسی گفته که دراین‌تابستون‌میخواد از این تیم جدا شه. اولویت‌او بازگشت به بارساست. چلسی برای این انتقال حدود 50 میلیون یورو از بارسا میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22980" target="_blank">📅 09:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22979">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfsLSjubmT7QtbTTGcZBTP4rXi5PBnQYrkOcSI9h0J-3WabcFIRVLW2_0yoyQkaQmrrDe-ZR7MxQGpRQOIlWSnIktffv_cnztQEi86SEBjh61-otCHcjNYE9e8RnFdK71o3Yg62l67X0_kUmahxeuBv7iFexU787t1qMVKFefHd5FzyQc-ccJuYcv5CXJnf-5sSWLqbz5lvMKw9QlfFVI2Gs7v1oQyJUc0PJ1Yh4m5y5muGIVayljgNHQbWrAq4NosKV7o9ogND3SQfMeTERzQTg8bILpyUZ7v_Fy3d1Xx8pE1_UK6mfMA4r1ZcKiuO6nRLwFyPmZ5QMNspEOFbxKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تموم شبکه‌ های ماهواره ای مختلف که قراره رقابت‌های جام جهانی رو با کیفیت پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22979" target="_blank">📅 09:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22978">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmcpMfNE-WaKje2gp0oThUaeOFSwGuQB_aT7fbuuDhrkcz8H0Cduv0F_CvAjYbvb8DZwcQg48pI3OHXJGwTE_Kj35RxzM9tSls-LnLFJDLVfW5lmG5qszrT18W0K7MyL2-IiRd66fAbUW27SgCybVQ5dkhvC2Tn1akzObl4CqHWr7pH9rWkKOOeHO3fOBlx81EXgMn7MnJ_0npFnUeKSgW6QhIs0_RoM3aBvXqshRXvX8nQcc1RUlv1i2Cbn57VfTYrq1F1UjpJ-zkgxC8odlqppmYUZX95_RWg8uttBLvZPkFHmb1PNUbnmYTyyorEgcbCpvqPbKpiloTmweOoMkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22978" target="_blank">📅 02:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22977">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaQCrrPK8s2Qbqv19fem8IUU6mEpdT0F27Cc8hi8AW-PNkZ1UF7JEzCjxls6Icje2Bhwx2QYvTNLTmfQA09pqMX3yy2UIUxmnVhN1PkpA6nFHds5AWKZwBDf4CuAek-SdOponpd9gqRnRFSD1mZ9_qs6CLc3qrp7mYuBBrkrll2vMXK2-aLGHZennjpK-8CzfrucPas6guM3O-OvLHp3hSTIRQuz8wWDuKi483c_ll30_vZfFdfSkul3KESfYq9TSVJ5vau755acbMEtnLvRDz7yEUEHxtAXorUkhNoeTQ_UPmcNtyNQOjrK0kNTyTlMdjD4iQcEKwbeNrEll1rDvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22977" target="_blank">📅 01:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22976">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noXf63rWj7UaQDzIMzs6Xl9IX1aZsNt_38XsHkMMNn0GGm1Cgw-LKi-ALnmv5CgAFepRzafk15jOioSI5wsaSYL82HnjV9Wtx0Q4quYHO1RKvovc74lMnte4inNwSX0qDXuw_NZBiny7BJEtdrlQMYx7FFNUvHAyXUb8aqVz_j6z-dcSPQ7IiC3oVfGVztprC0nMPIuG9DVNqLoreZnMVrm87k4qzZzh3zQKEyE4VNr6Ww--xVR51ukVs3kdDzzQYql9f8YzDpORKA_2s5L9LjjJOnAyMmhB9dHu94bTeki03rrMyby1i3t04EFauV3oyrMjHOkQJKIt7vTA_2_nGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛پرسپولیسی‌های‌حاضر دراردوی تیم ملی از آریا یوسفی مدافع‌راست سپاهان خواسته‌ اند که برای فصل بعد راهی این تیم شود. یوسفی از پرسپولیس آفر قابل توجهی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22976" target="_blank">📅 01:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22974">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbuH35ptNoz37kyS_sl2FdMBnQr8CxAO16fVbFOBewmgzsQ4ucUmh-aTSNF-Th_J-HkdLOoE8q0neuDC0Shu63djVDJ82WAlOsPjl6SI4ieyha7_kbBJ3H5T5KVmyL5QV5FRoaN__N78jkIuAmp86Lgd9rMFwSIhjoLeoTfP6lU4aM19oJLFm0I4gBqLW1cwHiiTkDcLj2OzB89wpcfT-P043dKFy-teBeDxj9rY1CVWjS-HIM9nIXe8e14VHWK1-FqOrJLG391kW3wrtBdX7PK1CRzbxDsqPkyWvWebmfArRIbCL4EuV82XSSh3WM8CCl0SXlg3iE1GFLuJguXszQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
از دوئل تدارکاتی شاگردان کومان و کاناوارو تا آخرین بازی فرانسوی‌ها پیش‌ از سفر به کشور آمریکا و جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22974" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22973">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrsl0_kbQgeW0PcUVtyRK9j3Bah2Kpe-40R5mkeAUzqQyLtboDCbnEEnibh-FSmhg9bGuF9H8aR38_ujdI-eLDUKyIBjeAoGHCjoj6XgwzYCeX1euva6JlFTvv8vjE2aIpBnqhLi9Aq-RZbCK5mz5iJua8-Lb9hldYIoGiIP6HsZIiaRrGzSuWn1eiUw-eJLifV3X8dXlr58HvM3InLmpb45eQ0uaNxny1PDgXx2y_lKhgDDHh82Z2FxyB3hVPTM4hKf3rXyYosU1kQ7JvruNyO-QBdBsvKF5445nLW1VScO3SWH6vUmqDM8uf7CPkFSZ0IvUbVWsCbrnPcumITKKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از برد آرژانتینی‌ها در شب‌‌استراحت‌مسی‌تاتساوی درجدال نروژ و مراکش
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22973" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22972">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lsg8CEDKDyY1pUG7hP7_2DDQbG4mcF5iVS8GuNEueNSkInR6-_jDYxsiqfqBz395Wn7CjozIoTyX3a1ZoCSjekYyybx_4UqJs3hL2CSDfY3bQmcnL4_hN-lHo8uoN01FW1EltoXhH80PZhLEF62M3GTGyiWXv-PRHmxTm3YfQffl2t3btAV8pyaa-zZW8yndTUellN1WUPS4QFFNErpKMK3Dm5ycou7Xdg8fjq0Ig_vqLnwUoANQ8IMFhM-H9-uoybXRyPPN3woRpGDNcogrkv9cjoWz5PNgoOpBmFEQxv_8mY-e8zhN_kfy4w8oJ0CMYbggJEY7EpaVzBLixCKHSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22972" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22971">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=Aeea5xwR0qSCQzOgqZg3nOZjrXo0nJAy136pbHf2NbVVzzCWuNaKO_sYbdGi8XjSZpnxjOhg1l7373V1DyHedI1XCZrM9w4lV6KJAiaghfWUNn8MRGUoADFCwxcmEgBiu8Ue8UCIGSVDm8Fm3bUW4HF_2TyBMoW7hhvCIzpKS0wWEXnproUwPt4p0ruxfD4PfH-pZPmKVtEJW0lC45i-uwG23HFYN8UC1ZgA4NdyCfHqUIVUo_CNNqDboM9S5mMCR5CoRkc8MX3gbqd58ci7KzU0JKR5xd_IAICMz8cnGuO-ynCgimJr7oTwnksFqPNQsUk6qAgbVwOA1wS7WEwM2b-uZxzFtNwBQKNIHGOW8yU5aufJLuGo0s-eFY9-JTFg3iTWlQQKNeOB6x6VGKGpFVHWPu-JMXs9pnn6Ao7aoLNgd2TtOaPxqzCIwkPAxvIplqJ8-vzwiF4OIUa4M7XhaNKKeKblij7jhfNXSgHrwvaQTQLNCCZwzndPuOQDksr_TMOpOQQVQH3cPX0tzm0Ql_czDja4o-pMEyFh9cX8ZR1Bvs5p0huRQmj5hXnvLI63G85h4UlbWQVyij-JFZvLE7ILRmjup_uU29dgiKpKNVbhBKd_wJI0xuGni3cXX92nPjN8UQjasStdcTmrybMrkzM8H3KPHH4SJ28Rc5XR2B0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=Aeea5xwR0qSCQzOgqZg3nOZjrXo0nJAy136pbHf2NbVVzzCWuNaKO_sYbdGi8XjSZpnxjOhg1l7373V1DyHedI1XCZrM9w4lV6KJAiaghfWUNn8MRGUoADFCwxcmEgBiu8Ue8UCIGSVDm8Fm3bUW4HF_2TyBMoW7hhvCIzpKS0wWEXnproUwPt4p0ruxfD4PfH-pZPmKVtEJW0lC45i-uwG23HFYN8UC1ZgA4NdyCfHqUIVUo_CNNqDboM9S5mMCR5CoRkc8MX3gbqd58ci7KzU0JKR5xd_IAICMz8cnGuO-ynCgimJr7oTwnksFqPNQsUk6qAgbVwOA1wS7WEwM2b-uZxzFtNwBQKNIHGOW8yU5aufJLuGo0s-eFY9-JTFg3iTWlQQKNeOB6x6VGKGpFVHWPu-JMXs9pnn6Ao7aoLNgd2TtOaPxqzCIwkPAxvIplqJ8-vzwiF4OIUa4M7XhaNKKeKblij7jhfNXSgHrwvaQTQLNCCZwzndPuOQDksr_TMOpOQQVQH3cPX0tzm0Ql_czDja4o-pMEyFh9cX8ZR1Bvs5p0huRQmj5hXnvLI63G85h4UlbWQVyij-JFZvLE7ILRmjup_uU29dgiKpKNVbhBKd_wJI0xuGni3cXX92nPjN8UQjasStdcTmrybMrkzM8H3KPHH4SJ28Rc5XR2B0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22971" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22970">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=vS5ZH8pjrXRxhBZ4PX_WDrrL4Jtx7bcPk1P5VccByb_yROIT0C8oLsiVzDlC5YrrOLh7meLMrawkfz5FkYU5dDuSxehlCSJUbpoTiNZIMLTVDmSe2EX0ukv-y7dEyycP8WoKFWcRGch-Dgf1HNYToFosTbFOVptVtRI4_pMkneUOGvgjgmXo8TuVWm74grnAuW3xGyCkTQ8JjNbPGS8GsvGtoSbxREp0ye3Mz8Nc7QUu_RvlPJQxUr1LXFj4rs1p7XzVLp8R7VT-JSXMq_Yn1izO55OsAvs332DGTzho68ffWSyvXO_-vKDDDKHuSoB7CoCt1Z8ArUK-Njmo8G9_iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=vS5ZH8pjrXRxhBZ4PX_WDrrL4Jtx7bcPk1P5VccByb_yROIT0C8oLsiVzDlC5YrrOLh7meLMrawkfz5FkYU5dDuSxehlCSJUbpoTiNZIMLTVDmSe2EX0ukv-y7dEyycP8WoKFWcRGch-Dgf1HNYToFosTbFOVptVtRI4_pMkneUOGvgjgmXo8TuVWm74grnAuW3xGyCkTQ8JjNbPGS8GsvGtoSbxREp0ye3Mz8Nc7QUu_RvlPJQxUr1LXFj4rs1p7XzVLp8R7VT-JSXMq_Yn1izO55OsAvs332DGTzho68ffWSyvXO_-vKDDDKHuSoB7CoCt1Z8ArUK-Njmo8G9_iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ایکرکاسیاس گلراسبق رئال‌مادرید در مصاحبه با روماریو: «مسی خواب‌وخوراک‌رو ازم گرفته بود.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22970" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22968">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGeyr-JpsH3t4XtD-yUnr_VxtM-1Zf8QdCFvEFMNNTps-7W8TXKFBS5pihhp2qRaZ5r0z2QWWre-968Z4R1hQi2BSOv_4p1NgK-iXZoICgyIOzefuFwJxEREIgcy2VOgPj7mVBuPhv8auOkSwaKNBd-WJZWRx4huOEIZ7G2kqflzEiVI34gM1r6cg0plLGvw4KioR4zuw7thZ_ia2Vlg3-Jnp0ZCWquIX0ELDq32un015BKVwTWgOOmFqPrhaKzJ3oAwuVKCUmcNbsfjX1IfxaBO__E7j8ejxfiF_DAZiaq1kzq8VH1Zys8MKUS7B4ZdnXNti6Bz_ekuqNfjunJ-Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای رسانه‌های روسیه‌ای: دو باشگاه ایرانی خواستار برای جذب کسری طاهری ستاره 20 ساله روبین کازان روسیه به این باشگاه نامه زده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22968" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22967">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=TEz3wfpDM43EJUEo6Ekhaye70F4gyxW9_p8QbnTwSGipoX7nzifr4wORp-EDq5BVn4dOsEHg0q4uL-ItqNwhxChGdDwqvxGbFgSMApo6mj-ra4r8kMIRZ_1UhT7yBXWxrH3DcUsH1lRwd71SWV9PI1h5aUxnfl-fSOzozhQzhaMAz6stdW7WBfwjynW3f31tMQicIeCXgxfHBncG9MGQ01XkwZUHOQyRb1F3x9m4NUBbZbamUdbZXNZmmabzmvpYZnO_woMWqh06q0aNc1Kx1nl3Vls_SVXk4Qxw-fPHoN1Xi4ha3Dp1rPglnZvW-WUSGwf9o1rwVp8VUnTXbLACtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=TEz3wfpDM43EJUEo6Ekhaye70F4gyxW9_p8QbnTwSGipoX7nzifr4wORp-EDq5BVn4dOsEHg0q4uL-ItqNwhxChGdDwqvxGbFgSMApo6mj-ra4r8kMIRZ_1UhT7yBXWxrH3DcUsH1lRwd71SWV9PI1h5aUxnfl-fSOzozhQzhaMAz6stdW7WBfwjynW3f31tMQicIeCXgxfHBncG9MGQ01XkwZUHOQyRb1F3x9m4NUBbZbamUdbZXNZmmabzmvpYZnO_woMWqh06q0aNc1Kx1nl3Vls_SVXk4Qxw-fPHoN1Xi4ha3Dp1rPglnZvW-WUSGwf9o1rwVp8VUnTXbLACtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🇵🇹
امسال مدعی ترین پرتغال رو پس از سال‌ ها در جام جهانی داریم اما جای یه نفر خیلی خالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22967" target="_blank">📅 00:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22966">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NobPEuBYrXKYCSoLyFbw0DEBxTyBoX_ADT0xTGKetjhhUb74ObexeSVWxesj6hmK3WZy4dOcklZKfdVauQIX8SYAljH9NjF2e94ZmEkHueShAqEvF79TjaGx6FND27xthn9vy9CK4ZiBNBAzYAasR31eFz_-4yAQ8BZ1otyW4wc7Qhiu_TD78SqbdYtT_bv0eZr1-ZZnibkHYEfDEF4UZRXK8UH60WXgnw03yILxfM6lS_rto3Ye2T9-dJDeEd2Q1CJBEitWms2FL732lbPkV0_fh26253hdCoGd5ox6rgbIoG8zZ397KfcD_pH9SdC2WYoS28Dr6r9FVXXgjMYDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/22966" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22965">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9YElPGdOsTiZLbxl0hv4Eg1PEhJHVO-ZiMpj7dLNw6EkQNIi5K8bIrRFNY1gwi_787bXV0GR9QNdM8T2cMSahEJBqm0FPjq8xghUnsM4A7weELoG0DajoMFroAQhBnn1Pkx6TOWBs5Y-E8mUybB-PiB4cMvKtgUAS7juvoaflcveQseqDQ4TbFADpb_LQlvR-CaeH-1kk9BCy6slbsQk82Be0rS9KjmmnNNoNle3z7-6u4nQf5OO1Tj5cQSyyPsEVR1QJWw06PJYBmf8O31kOtIko7rMTHuiF_D08JxLo-l-_Sg7ix3vnApeMl-mh_cHVRmOpfal6uUhBiedGhDWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/22965" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22964">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=Vg-5NphaJKJGfbeJOZ3xZ3IdfeDZngPT-fGX8xLK9Kg57krOFP7bxUhRDAO_yeriYa8y2eYNq2HGzcjguIEWrFnL5DdmRj7eRsZg-toFewECukU-Ja_SqfekUuRjAWQXdEEVwSExCuSKsW2ZjptC2I_YvDxmWr6Hzb90tuojJemmeRDiFte0iBhX6ljgYGDfypyEJXnFAVG4yThIqtX40mHd0pmZfNWUHGjXWhgYon4vAabfJI5q7_KgbuFaOywHd2BjTGUlLOlfNppnUfSYPTGhMSxIObXpYTHqWMKJVq78LD2RLU03JgnHOnw6_xjC9Wssa0SlBSgfZx1TR_aCXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=Vg-5NphaJKJGfbeJOZ3xZ3IdfeDZngPT-fGX8xLK9Kg57krOFP7bxUhRDAO_yeriYa8y2eYNq2HGzcjguIEWrFnL5DdmRj7eRsZg-toFewECukU-Ja_SqfekUuRjAWQXdEEVwSExCuSKsW2ZjptC2I_YvDxmWr6Hzb90tuojJemmeRDiFte0iBhX6ljgYGDfypyEJXnFAVG4yThIqtX40mHd0pmZfNWUHGjXWhgYon4vAabfJI5q7_KgbuFaOywHd2BjTGUlLOlfNppnUfSYPTGhMSxIObXpYTHqWMKJVq78LD2RLU03JgnHOnw6_xjC9Wssa0SlBSgfZx1TR_aCXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/22964" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22963">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇱
🚨
شمال اسرائیل آژیر ها روشن شد دوباره  موشک ها از تبریز و کرمانشاه ارسال شد</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22963" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22962">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0Qaf-67DIwaHCwSMHEmA6rBw6s0XLv8fD8W23c02bSr16YkPFNOnW3jnxzHYw35_P4ULs-ZMaVb_L7QTr7LZO1CiT7dmlyQ5S9IOC6hDapgqYMuUZ2eiuuZ4-eOiy1FmNJ9HlSDU3As9Ge-k78q_Vd0qDYDlsquJAkXftm9_xr4Z6RraL3-7qyqFFd_JPPpWnZsUmt-dd3Bpx-_53I7eAz5WGw_r5gF3GuqAbmDB-LvXL6PJB9Bo4pAm1puyN7LlmTYufScR_RbLu_GO7pJo7Fb81DK5lWcY8q7reoWXzt4hYSriBKsTT8MNYSMp4zDr0pt8Ien5-XTAN7X9eMs7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اتحادیه‌فوتبال دانمارک رسما اعلام کرد کریستین اریکسن هوشیاره و تحت شرایط خوبی قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/22962" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22961">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQ8BabrmM6K1uO8FqenAPVKVCTwkSueS4kltJwcEafRVas7H6YdTGMIrrYr-7PdEGHJ_AeVuEWNFvIrkKO_G-rhFhXnzSbnJQx0QNHM9xKQlU8dBxRKfstufEAP87Nc0jGlyzI6A06U0EpBTsr-MyRuiL92RhWQ_w2_AFV8T_X663h6JyMjCE1XXvmAaI_eB13KsQAr14PJfOh2rHgNYIVmhZIuR3OwvGHZcW9-L8KzHQHBHg2wN_8S-QyDKr_H9Bz05cJV-JRuXuUX18UwPXcUN0Go04-bpKmiTyfP4Pxxs-6OUDs4WqsfA3hxJun9icW9Ekri9CXtfNSlJKB57zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22961" target="_blank">📅 22:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22960">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdRmT0ajWGbN-dKyyMFXLmg9UhzzX0S-ZroVBWMZ2Nb-yn_rPbNUTTrWiBCP_glPnUvzMEIQs0hO8fNdCPyyZEPGY6Mx8BY721itFl2J9r-1LYU9pvyKz1DqOVs1s9YjxfHuf99D_XQNmszc0rDoJhEzUkzymiuSKjST1ldCbJfVlYViecdMXejPxO-M0WfKXM66eIkuuk2te8p0w5qQfcAHWz3gGZ5y8LJNoIYRjRpYh1Xt4KwJxdCTsVsUH2cOExajSB_McKclIBZFCrJ1LVxhX0ns6y424A8QuzVUCigeavHUFZfZ98KrlHp2gR3hhLnsCn9MaWcY6ROfX8_bMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری
؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22960" target="_blank">📅 22:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22959">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLuIUeU4Splgflslej4FFxQpTkvcFwyyJ62UZ7-gufmM6Vo0yYr_HgRu8P1YMq0AyT1yyhnRHnW7E4uyfxtFNXHOibU38OOq1G5wNqtTTPL8Nz_TOn8aXkbMA-_2wp4CJ944u3JU-__Ch_7LCbLTl6OU1saJhw5deTzCIDrHjqT2mynlcMfhQedc4jFUdY_pjObzlSSuKHLlE-90hkkDT0kroAmDHPHa5QnLryjRTee1TEmwQqdRMbrdhKya1TRUCjb8tCC-nQFo3zEes9yYzIIup-uv9YgeJ4n6mxUB94_--PaDIejrqFevA88zd-wLACeOowsarJ6Han9DVDQleQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22959" target="_blank">📅 22:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22958">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=nlEhw5mAmvQRxWWOtz0BhzD1aSYWdQxgH7WHlH4kgr2Ux62EAuYn2jCFsXrbv_uDQp7xwMQSIIdPMvmmDWYn9POZwaE2SxtAxbrkTnMpO7iWS4JSPevKE7GJpT1ydtPMqOT_nLgo6awoklKhUwwCqOlFR7dKn1K_4tP59slHW4AwLGmm_utiRBL6AVUL9X17Lmuf8Ef5bpvT42H20LhLAwLxtY4acDjivKNs4ZvOyVOc1FMV0gg3rjguQfr6NWE0aSkPY6FoL7FpcrDKxHS0L296yjUooPeSBFWhODWkWTxOixRlfl9VRI0m_kMu2gOIEHVBqBZVD8LrbNKoNItPVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=nlEhw5mAmvQRxWWOtz0BhzD1aSYWdQxgH7WHlH4kgr2Ux62EAuYn2jCFsXrbv_uDQp7xwMQSIIdPMvmmDWYn9POZwaE2SxtAxbrkTnMpO7iWS4JSPevKE7GJpT1ydtPMqOT_nLgo6awoklKhUwwCqOlFR7dKn1K_4tP59slHW4AwLGmm_utiRBL6AVUL9X17Lmuf8Ef5bpvT42H20LhLAwLxtY4acDjivKNs4ZvOyVOc1FMV0gg3rjguQfr6NWE0aSkPY6FoL7FpcrDKxHS0L296yjUooPeSBFWhODWkWTxOixRlfl9VRI0m_kMu2gOIEHVBqBZVD8LrbNKoNItPVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22958" target="_blank">📅 22:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22957">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKiMjQKxM-jpXpjP-IXRoJrvI6oK4c4_ddFRTqrjtXXPPQXqrBNXoV-1n_xmusNBpWOfC0NspDnUae5XA7pj_HiAiJLBKsoR_jGLckFmXz_9qTV-HvFdFbSDIUdcAbklBvu81DPgPxLU06yPHRGxnER8M02yGcUjptFWqnAJTnVX_GJLRB-mgSgwgdxCvCppbVRDsyeoHp5fiGhk4fo9XbhV7UJFfnnpjHXFPY3INJ46hBT292KmGGrgyl1CKqtkt_VTpdrJYqgIQmmk0x7mk0AtMHwVsYGkjUuCNR067HBQPT72qAtWVqLeSe79hPAdp4tiFTF3MRgCjVk5VJpCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ به‌احتمال فراوان آنتونیو آدان راهی لیگ امارات خواهدشد. او دو آفر از باشگاه‌ های اماراتی‌دریافت‌کرده.همانطور در روزهای‌قبل خبر دادیم جدایی آدان از استقلال قطعی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22957" target="_blank">📅 21:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22956">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=XEZ7mpK7JB_CzJDISR-JU2XxtbxCgarooBhnv_lb07YLEkpiugEaUj4QqNVFH4IIzg1wI-wUTi1SC56Aj-P3JBnq45Np6oUYbtezycdSbVdWOFDuyrScWfwzwBCx0KhPY36rG9rR9IFfO3dHfB7qwFugRgfCFTSo1NVtHAx8DAHUSn7IwKKK5BjgfrYZON9k5A3BlTNdi3kc7D2qf7iQLXHWhYKy8Qsooca6BedkFCmUIbCJ08vaWzFANi95Xsw6DNws4GAIaJLIeugu25dJDncWUpY2_0PhDk319tNJjkp1PzEtVZhkvRamIS9hh3Ah5TKWkWiiFEFg5FTH6bgRXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=XEZ7mpK7JB_CzJDISR-JU2XxtbxCgarooBhnv_lb07YLEkpiugEaUj4QqNVFH4IIzg1wI-wUTi1SC56Aj-P3JBnq45Np6oUYbtezycdSbVdWOFDuyrScWfwzwBCx0KhPY36rG9rR9IFfO3dHfB7qwFugRgfCFTSo1NVtHAx8DAHUSn7IwKKK5BjgfrYZON9k5A3BlTNdi3kc7D2qf7iQLXHWhYKy8Qsooca6BedkFCmUIbCJ08vaWzFANi95Xsw6DNws4GAIaJLIeugu25dJDncWUpY2_0PhDk319tNJjkp1PzEtVZhkvRamIS9hh3Ah5TKWkWiiFEFg5FTH6bgRXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری
؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22956" target="_blank">📅 21:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22955">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWd_pucLyHpwc-ha_vvCf5dxP0rTCoPWqZERCQVMQer_9cToOmg46ZwTufzK4sHWOKCf3qjZ0j2DI2ix187XTMuncn7g_2gBJteb1rsdCAjHRn5gIPVnQEItMS6GK0tJdbsn2gwU_OHHrIEye6bNcKSaZuwPeSiFWEXwwO3Lk6WaJh9_l657BKsm6TK4ggM4Ycv1FRaEqMVWT-go8Dy5RMO-HFHrRWuSc8hxAwSfb9IFPrwt_9L0W3nw-Hy7pKyZX8EYutwi99NcCaxMAVpQ2PfyqDK-vxj7bSFEKpaj5eQNJNIn9kgs_kjnnB_AeVLu6haUmbzMa07XmWX83KJfHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ کادناسر: بعیده که‌سرانPSG ویتینیا یا ژائو نوس رو با رقم 150 میلیون یورو بفروشند. برای هرکدوم از این دو نفر حداقل 200M€ میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22955" target="_blank">📅 21:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22953">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LEPPFXZJjdPkhgtMqu4NSQcIL1g8AHKjzqNH0KkgOS9CjL8Sfcf-iUpsYncvj-ExGLB-Aqp4UsLmImYW1aQ9tUWFFq0lRWQ6yESMbOgZcDNOPRWV8lBLPfV2C-BpdP6hT0JATD75U9jK-ZA65NjzoYWIcegre_BeUU4Kt3039JcJ6phiwhKKyZQZM6IbQFjR2-tsg6_rdUFL_dCv3Gt5dokQ87tC-q4kzUUqpiqm2CUjUOwK7iIlSiu3v57I6YSvXXrJGlxeuFDk-tIyOv-HSTHc6ZEvasx9OBU_VbRJINKuiKTIptv6RxMgkuMKF9rH4D0DX_saigyRDc29JxbyuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l8UrPtR-eNgm0H9GLjtb1J7l5gKwt7hlW8fu8Zp-VeNdDy0cU04HiHlSUF3vGNnW35Egtbfht-4Cs9OubaHRRiPRPlLs1RtUjCrfxcAwfiXcKgj5UA-F-E68jyVXkR5hAqWyTVfZesCAMrwBpQzMdSTXr3TwwQuMoZNpUAw1hovj1-9vVd6Ls4NtxmRO1hD_lb-UUu7FHI9D4rZBuKZz0gqEz_CtHOmItaJ1K7phGQczEYeEQjcgNnPSy2eNK_-yHNYNkYSkRICRv6iWc6ALTZHibhZek2AOh0cWBezXx1Ms_ieNCk1Iz0rZ8Rfb6qisyjJARDKVyfzkBaa1b8uw0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22953" target="_blank">📅 21:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22952">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNcl6U2tF7E_kDTDOEsniEzg8zcCJ0aGuHZm7zZHb_Jz_UFOgX4fs-Zn4KwvkehFbnlEKLtS_B0kcqs9gqRSZS5PtOpE01dmvE7x3sIBiVzvBvB4xNc_kb8O6aN498GQoEDOjeK6KXVscwSApzY-hOj0Fp2zt6uKy-M2ssYcKbiFNd3HiFVbh9CqYK5EMyRAo61XLTPNCBy3urc6NehPNHG1A7cpS1Ibmql6MGP8xAJxLl4enGjT6JBR1ftDq08pxf_HkZxUGD6UzMDWMXxVJyvG1PA-xwIntqLjNJM3s5w3ZDOeHCRrquf0zQIfh78g4Km2eaF0DqICnBQM_0-iPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
حواشی‌ دیدارآینده ایران
🆚
مصر در رقابت‌ های جام جهانی 2026 از نگاه هوش مصنوعی ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22952" target="_blank">📅 21:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22951">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=oS9Acgph2AcgbAmS12ZRP3j4A1YiPMECavoqTvuymS7PWxUII10Z-j4bHIldP4OR195lhcyXFrfLaPdvSraQvwdNF4ZRi-6epoEUwv_KEv9dnlW4p-W3t1Th8CMvu6zSr-3_RDWzvD3VxEBvnEsmepNCcUrBPZ3eIxBoDovtGj3TI-oJdeL6f0fu63BIWRJSY5IdeuG7UnNOF2X7fEUd3yQqAlOusSUDYBg8PqjR6EST3tm0TZVuQSoULId7XTHBK5_V_uxaiu21XnbGLDp-8SPN9KMLb5thKwc2zAFfsDMXTO_NqQ36ssveVGPLKWKPQ3qMztvxu4MF3rjn7OVBuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=oS9Acgph2AcgbAmS12ZRP3j4A1YiPMECavoqTvuymS7PWxUII10Z-j4bHIldP4OR195lhcyXFrfLaPdvSraQvwdNF4ZRi-6epoEUwv_KEv9dnlW4p-W3t1Th8CMvu6zSr-3_RDWzvD3VxEBvnEsmepNCcUrBPZ3eIxBoDovtGj3TI-oJdeL6f0fu63BIWRJSY5IdeuG7UnNOF2X7fEUd3yQqAlOusSUDYBg8PqjR6EST3tm0TZVuQSoULId7XTHBK5_V_uxaiu21XnbGLDp-8SPN9KMLb5thKwc2zAFfsDMXTO_NqQ36ssveVGPLKWKPQ3qMztvxu4MF3rjn7OVBuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیکه‌های سنگین ابوطالب حسینی به تاج رئیس فدراسیون فوتبال درباره عدم صادر شدن ویزاش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22951" target="_blank">📅 20:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22950">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJfQc0_tD61IPvxgpxdVT5gG5bwYsCn1SOkeyY2cUVcdug6ppQnMdrX-HvYQIiukn1i_JBaxLhJ7XQCCWq87_wNdjjribsOxT0ruHVpn7RHhUo5QVp1FNYxGTPQsqdOGGyUHRk22po6HqzkjJ7g806m2_sLk-N7omc6j5EVPYYHEM4S-aVke28ntJXuUfaHFr4HTaoG52N3qNjTC2zQToGbRBj5zOvkYukWdcJhtRJk_VY9m2hQkBdj-jL5c1Fn3gVMsP6KPL6tuag7JkrIC_3Tblp5NweO4SUFUZNvKpMPzJul9FF2yumWqa0hHfd1IuvnQm1dwogkvRM9AGcJezA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22950" target="_blank">📅 20:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22949">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGUH4guqdxFyvELyqDCz4grZLAkIiXrtvkAzvTLa-_bG_YEs_0s3x4_PdQVb4Fze9M1u5qLetwXGqho3IBI-5kVF_qTUs-1Af4KS-_pNcpbbn6-3-ByOvT1sdURIvIalNWlmQGnI1ef-9trltVi78yKRGifQvxbbYT5hJwAIsH8iqDV4hxZg3uzzfBmWL9wfIRZ8ZZlUrks23EAyHml42jra61jmDtg1F6Xt9Rpkd5nb9dKDKR1sj2Km6VZg_9A9e3RoYLFGYxIHM4KsqWb2LDwQwmRX3HTTKU1mr6wNL3EG_1Lq7Iz-CbwaiYIY6puXLjD35DQgffWV-z0gRVLmQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛ اگه کریس رونالدو در جام جهانی 2026 موفق به گلزنی شود؛ به مسن ترین بازیکن تاریخ این رقابت ها تبدیل خواهد شد که گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22949" target="_blank">📅 19:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22948">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kl92jESJibfV0W9t9FhVEu70i2Po-ambYn3g79P_S7gNbyATTBACLD7TW4n0K6ZvMSMFtvsPgZYHYwB2dBCjCWpJ0P6DWok6y2a_Kii7_9vOBPoSRyUxUYL9pylkasKn9cusDRX69KyJZ79DVjwjCsvS_M5OqvlCUgyKbyadKZk8r7LP4SFZCfLMkT-X7cGUqXw4rKeiGBqFOOa4tTjlCVUMAoKUezhMu6Ety0brG5vToTv_h2a6YokYxy4LW34ZarKB44_kNdygdAoWDPiEPZ2nePj0t-jn3b_uRrdm871c9bEtqLJiuFU4AX7Paba9_f3TfO4nIUcloYqDfiyZAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22948" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22947">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=dO13Kdw7xOTR1S0STW28wOzSY97dt3KejFY3xH_Ax3VJVcD1dNOm5vDE7AMS4FnlMQR9cJLJrD_N6SQ8nteCSv3S5g_FXxGKosBoHxAKBuxkCPM3gcrdTXrkfErgGDMhmoDWGT0yWSBfQzbi0UZ1s9lf6H_ggRhmnOmeT7LIdosXXtdRm8jRbEgR6_gD94kPnX44DDqjDpSIM2ifnsYQLw1qJMUURPZOQTH2oNOCI1nLs8x5-fUm3-uo4hPW9-pCFuwKcDzGL0BFDEPmHxaOyP2eJ2ocLWkjsI8_UEPjHDEPfjrvFIda7agf05HD-bdkxbtJz1uXqXHAMoX1WOqq7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=dO13Kdw7xOTR1S0STW28wOzSY97dt3KejFY3xH_Ax3VJVcD1dNOm5vDE7AMS4FnlMQR9cJLJrD_N6SQ8nteCSv3S5g_FXxGKosBoHxAKBuxkCPM3gcrdTXrkfErgGDMhmoDWGT0yWSBfQzbi0UZ1s9lf6H_ggRhmnOmeT7LIdosXXtdRm8jRbEgR6_gD94kPnX44DDqjDpSIM2ifnsYQLw1qJMUURPZOQTH2oNOCI1nLs8x5-fUm3-uo4hPW9-pCFuwKcDzGL0BFDEPmHxaOyP2eJ2ocLWkjsI8_UEPjHDEPfjrvFIda7agf05HD-bdkxbtJz1uXqXHAMoX1WOqq7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
آقای‌ممفیس‌دپای‌هستن مهاجم هلندی اسبق بارسا منچستر و اتلتیکو که داخل و بیرون زمین می‌نوازد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22947" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22945">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvlnUD5IVpRPlVxNo9-Y2OGKcesrb8a0rSbJfgu96s8hZ2_6_I9PS9wEYp8OhbsEEeZTJ8Oe3I7-e7vPF7lw1gZeECbdsacienIqxGIqjHEZV4FRAkxPal_Z5R4qq0pmbd_XdW8SyWJWbKj0TBQDCOCARNXH1gNM2TTxowLFxgGIi0o-JI34Xe5ILNM_bhoPQAlAd4D2WEjihXuuceTbtln1bVX-2OZDRIg85P37xW35qKDbr-7GHxSeyWZKokBM5U9Q8Jh0VOPeww1ZW1DybaWvaavxWPK71o8Z_6oyhvaYyH3uwB7aDZmx5y_v_E3jyb6-5q0R0KwC1xJJuYYTbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22945" target="_blank">📅 18:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22944">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYMAS_lCSutAtLxoALjxlu_jg6hjsQLDAfwcxFS12RfPC5saIf5lMklvSRlmBdgtBbjJ8KqBVUsui9cuMbGBoxPy8knIdLsa6C3GkMcIHH2mUCVnyCV7ahm-_dl0l0pW7VaJNpyNkI6gZAqV9703XB8o8bdYIWIGp7IXXrH2SYk2Ck8gHgxdeWRJv_Hv0T95Sn5D684_Bd4mPGMDR3RKg-JmKlGZu0346P9n8rc-DzRBIZBb5ArzJ7q28GLEwRYoY92-wcFLud9CC5MNHW2LoJtRx2rrPGjDE9Gm_a7J1zclU6lGEZdBQ6mQLKo7wMb4dChrCcGapVWm-3xbpg7QmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: منتظرحمله‌این هفته فلورنتینو پرز برای نهایی کردن قرار داد مایکل اولیسه از بایرن مونیخ باشید. پرز قصد داره به هر قیمتی که شده فوق‌ستاره‌فرانسوی باواریایی‌ها رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22944" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22943">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaBFh9-OkVtt7umfdgDiEVDcv9EhlYdk3-DXbYQiKE4SoEa6c_UAS8e7MVSiuh8bZqMCw4BlJFRnqxoGgvLgeLJ6Ma1jo4XKDzHkbgHiQwYhUTn-vXf3QzWxMoBe49ztvuH8_yO3xtYzQEndUT1n82umWqlk5c_uUsZ2Yx6ZjmyxI1FiXfvggQ_CeJuOvl7H5zdCCE54p97pSmmJD3QVo3Pstpzm93SnfDdChdtre5D22-eFBES4EXZSpOoxETIjPFMoJ8LQ9id2ayIDu6MzlL7xbmQuQ7aHLYRxxIRLqw4g2cdThSy2J4HPkI5o4x4eg2wJfarM3kEM8IXZqz_3Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22943" target="_blank">📅 18:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22942">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=JHbCDOhLPODsQ1OquqdMAA59cLD5wXQJ2Bc520CqfNh051piiOmIKBopQBxbOVVDLQQKp5iOga109Z-fucgdVuGwKUPADFTJuod7vAZdDDzq-Vf9YlvOy6Ms1xafHCFB9sUSrlv9KQx1gu9LXRgGZBwUZbSfdyzbtw68gIG-6QhBnMAdM9vNmetx003luuPhdwjLhQGLoq-GyzXQw2GmSSRVeh4raSs7QQ3KNY3dizkji2UdLe5ijuqzGugW-x4AsbFTlukRIfP_Muu86ywbykbfWd2ymLCInpXhG2iM4zRUwS7KpUKcLU3MPNlht-zRAatMnBr3ajfIYoRDpo_5_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=JHbCDOhLPODsQ1OquqdMAA59cLD5wXQJ2Bc520CqfNh051piiOmIKBopQBxbOVVDLQQKp5iOga109Z-fucgdVuGwKUPADFTJuod7vAZdDDzq-Vf9YlvOy6Ms1xafHCFB9sUSrlv9KQx1gu9LXRgGZBwUZbSfdyzbtw68gIG-6QhBnMAdM9vNmetx003luuPhdwjLhQGLoq-GyzXQw2GmSSRVeh4raSs7QQ3KNY3dizkji2UdLe5ijuqzGugW-x4AsbFTlukRIfP_Muu86ywbykbfWd2ymLCInpXhG2iM4zRUwS7KpUKcLU3MPNlht-zRAatMnBr3ajfIYoRDpo_5_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی‌از مسابقه‌کاراته‌معلولین؛ این چه حرکتی بود تو زدی آخه؟ چرا از روی‌ویلچره انداختیش پایین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22942" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22941">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNvenRmJcvvXIZIbsjonH_GSRl1eXiSdNiZtVE0NArqfXygdpHLH0eGLCBwJytsy3IBN7SlVd0liT8aV59w1OWymINcDqjD4fgFbluvtVzH6DRVYEa5l4tpVGXW54lRPc1x-2KbQeFOx546U_A2JbMqI8USLOFJTrvdXapGuX4x2zwMeuIxo3CCcCrtdEopiHMgBjyCedfLKqKVmEwviU15--TewowETwDT33MtjAnK8nDJ2-R4YSdITzwQXJ3RGWujpPXL4sTl_Bl2bc-UHxBtfIUUpraAeMNN1yIkKPjmlt1lqlQoZB4xRo4NfCIcqKK_5wP2RaUf_loduzKIlzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22941" target="_blank">📅 17:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22940">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pK0mpbIZnBiYp_M_zmgt4CYljbIpFIgLMcKRUdVNalZEDPmw9KgjuU5ccaEKRnqo9PghvlZDvMzVvHmDif1B4J3QEFlxBCsgPSXyET-AjvoTSfoLw69_Z0lb3EHE9rN9zjXrNHcn4X_8nEPEsdpYDlmLhqjj3sWXRL_EOLuQD59l_1WX2EoPMUu46tX39yZem1A0_2eiaxk1Dx8opNgpddmwZWMBNv9_7C3H0gJ2H7ntgkkaL8Sez_Ld4nrFT29yXRXDiBYxx_drw-N2mufPimdlI9SAEUPEAULEvhxDcqyJUpmmZ9KjuHHunp_8LVnMrIe22kbJlCIuMJiMoPvoYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ مدیریت باشگاه استقلال به دراگان اسکوچیچ پیشنهادداده‌که تنها دستیاری ایرانی‌اش در فصل آینده سهراب بختیاری‌زاده باشد که درصورتیکه جنگ پیش آمد و اسکوچیچ مجبور به ترک ایران شد بختیاری زاده سکان هدایت تیم رو بر عهده بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22940" target="_blank">📅 17:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22939">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdpN9kV_0weS26_EMxSEmf6tbwSz4rKD2gL7QNM5HITV2txkwd0M6Yp6yr3uzBuglB-4Fldj0XijWbjRddm-fyQq0V1fHHCWOfb6OxvK7ON5NPfDaamGLUjr8rO6aJfk1oIDOg3NmuWOYEaaVTIYK3KLSIczb13pefs3qJYAJY0CX1JxNaOv4SM95ZJvmibSBvZeGTTJkPq5chxdxVCJjfQQ6hx5BLGD5p0DO0jQnquNBWHx4Sel9nMWw428zoEBrfH8wWlcb7XjLOEDRMvYaeAWoo0fau4g08QKwW0zTLeS6CZLDHPbHrEtmFEvY8JuErNaU3jq-x9chLg24h72-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌ های رسانه پرشیانا؛ باشگاه پرسپولیس در تلاشه که مجوز فعالیت افشین پیروانی در لیگ برتر رو از نهادهای ذیربط بگیره و در فصل جدید رقابت‌ها به نیمکت سرخپوشان برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22939" target="_blank">📅 17:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22938">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktaMH5F29eFHtxoT5yMA6sWwvB9x4EJ9dr9gevuzpR0jDfkqM02BexpphbJTO5bFFQnXAad_KXqvnYh8m5eP5XiIxMFbL-x-scZT6C5OFgtTtU9mbUJo5oVOrltaT6XAme65Mpj4xgbtDq1ePmhyKPfAPrLxWABqUpujWpSoCfeGt2vdzH_Sitpg8a_4WXIhBCRG3sYtlwn_A1lEaf7P1PwGCvpUs_PSSHbePXWY8I8zuGPspi78RRQBTCGgdNcOWdl-WIHaND2B_I9xzFFobggF-NgBneHS2SY0gacV2zK8PRdlksrHhab9S95xi3Wo5PV_Ycl5K2JFHZ-Dc0hDCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22938" target="_blank">📅 17:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22937">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7ai-9VGGonIllYd9tntiPXJOX7E_0OvoJMZYbqe1YbixYMjZeWL5fOKQo01czvItWwpwlEJUrjV28RBsZ0TSDNb6PVqlElhwWzHWHo0uEFvnFmtznNsFGulXRTybbomU4HmQiU39kmJxF-pfmoyOp-eVd16OJG1pQz-jDA_p9gUhaR3kR-XAqFZiy5cS269R1oY82MpAWTkrdR30cTQMfPUVdjYrz47fsZBMmlM2oSKEpOOcWkAhhEqEhp-i73Z_i0q1hG1osheJ-H5Td2vgR1GPZeSP6NMfJ3Zu4Ive6dt719HCAf39YtzqcvIkoRncJBKbSqspPydgHXLr-UN29us" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7ai-9VGGonIllYd9tntiPXJOX7E_0OvoJMZYbqe1YbixYMjZeWL5fOKQo01czvItWwpwlEJUrjV28RBsZ0TSDNb6PVqlElhwWzHWHo0uEFvnFmtznNsFGulXRTybbomU4HmQiU39kmJxF-pfmoyOp-eVd16OJG1pQz-jDA_p9gUhaR3kR-XAqFZiy5cS269R1oY82MpAWTkrdR30cTQMfPUVdjYrz47fsZBMmlM2oSKEpOOcWkAhhEqEhp-i73Z_i0q1hG1osheJ-H5Td2vgR1GPZeSP6NMfJ3Zu4Ive6dt719HCAf39YtzqcvIkoRncJBKbSqspPydgHXLr-UN29us" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اجرا چالش فوق العاده سخت ورزشکار روسی توسط یک ورزشکار ایرانی با رکورد زنی روسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22937" target="_blank">📅 16:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22936">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIjo4Fn17hX3lKlsIvWFw-rnyApxJsxZ_YILzgrckow13KZtCH1yJ21KAZVWuhYj-4p_WOoehiHRiaJxrxPHKOsGUwj8sWsK5-gI-gwH6TQ8EmdhXWS_e18kF1YIFSQdzk0G_ajEJrLjDdFefaR0EQQPT1XF7gMma3-ApaP_8ZkffJGioyVTREAyOWbFUFkBfnhEgR-M3edBRPlfKe-462SqO_jK5xtf7bK0n3fdmc5yMib31fje49066j4VRKfrn2ySBtsypBWKCFpEealXdNaHt1_QhdmAUYeJZf2wtaFPgKisI05hBj1QA6cZ8yiSlCEnky8Pf8nOycnG9XVOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22936" target="_blank">📅 16:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22935">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6Pt1rwnLAepKX5UB-a3Ok-nlCmBeVju5b_Yrf942yXSeS9lDiil0RnzILoXrCbzZU5mkAksVI-kmkT19A-jN_Ti4ozgfRtcu40TAeonwgnrbFqa1JHAknUjAWUGybtOLKzmnE4FYalVy_LxLypzBHyoT6E6CUa2ZBmlp33o146bVSlEqxNNveaRPuog_68AOcEuXrVapFlrTU0OfQ70awN5qetJHld5FVgenuDGZflfmzW-W9s6IM9onemLIxSjqi9v9KfMbIzsnZvK-uP5tvWNN4Z3gZ9-iOOptTdRderUgXoG9HNrmkMMzUsYQ3oYIZxfLVukHnjxzTdfP5fhNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌انتقالات|گستون‌ایدول‌ خبرنگار آرژانتینی: با جرأت بگم که آلوارز درنهایت از اتلتیکومادرید جدا میشه. مقصد بعدی آلوارز صدرصدر بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22935" target="_blank">📅 16:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22934">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lfq2LWS2r-AN70FGB2tBPJ9uSzB6dNuL0qphjUTHwWu9R12MndEZx02M2nCcw3gzS5hGl3eDYMgPLxxtpKCZqfFwpd0ZCFbSBA97bS2195Sax6BjgX5wyThANhBOW71LUOBfFs39VQyu2BP4DJirL4caSLyxMHlORpk5iyBVitotdAyhp0mg1FW97bupyHd2nRvTTy6HFPCr5aXQ2nBc6l23VRIkFg17LJ0R9ZvbYVIRcXuiVPpK5zWlXG5v3vw_K_9-_X9y-0WR3DoWb8gY5UEs0tVPdtSzX2f9K13AmMfO_4olO6NZQqCEKXKhZV6ruOzISziz-wQiAAO7MwZR0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22934" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22933">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=p3RK2nqcOhsmB2ck6glldOlYn8xxakp03j4gy0bsWfPluKELVKhVyjaO_Dyc_05YJDOB3yj-m8jtWev3bWjuBKEtt_DvtNt4LuYaZMU_5YKRTdnSf1496YYibGjr-HFtJ8cq86BHukHNrvX9EICnyXHMN_cQGJMkqMbQ3i6iBZFOrjbr06W8HvTHbMNGzrKOoQ2X8_vrK478Ic6vXIc4puWDy8iTDA3HgzUDSY4hYRr76rHojVGGZ0CbIEorHKSX_4InvNIzfG5WfQ6unv58-oNN3PGUyViJB4SAX8S8LL5_fqD7AvouaD1s_9NOLqu6MGs4UsdVRUjMYdMvhLEX4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=p3RK2nqcOhsmB2ck6glldOlYn8xxakp03j4gy0bsWfPluKELVKhVyjaO_Dyc_05YJDOB3yj-m8jtWev3bWjuBKEtt_DvtNt4LuYaZMU_5YKRTdnSf1496YYibGjr-HFtJ8cq86BHukHNrvX9EICnyXHMN_cQGJMkqMbQ3i6iBZFOrjbr06W8HvTHbMNGzrKOoQ2X8_vrK478Ic6vXIc4puWDy8iTDA3HgzUDSY4hYRr76rHojVGGZ0CbIEorHKSX_4InvNIzfG5WfQ6unv58-oNN3PGUyViJB4SAX8S8LL5_fqD7AvouaD1s_9NOLqu6MGs4UsdVRUjMYdMvhLEX4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آدریانا اولیوارس مدل مکزیکیم رو بدنش عکس تک تک بازیکنای جام‌جهانی رو چسبوند و از دخترای مکزیکی دیگم خواست این چالشو انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22933" target="_blank">📅 15:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22932">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5DZe4UCsQBBgIMy9ayTjiVikMsdGqDIRNa8dlGlwH6W53Rue2AnjvUo84OooEvBIe45PaRd_AUWLUNJq1GVnsh5nvqCpcfXe1GQqK-GM_a-n92a40cAPHEaHDIt1NGJ48c55NPBy0u_sAeL_hCTi0ndGYbKnpQbKHaNFsm-pSSldjw7rbR1jj5gwux5NlIJLkUd2NWkYIXQfnM_2AFqy7mQHtIf4RDMNfXhVKmxSxwKX-Fner7fHvkHVlulp5KPvDewGcsKDmULAvnenRrud7W6_MgSMkkRl1hC60PhYIzwHCBGYHQMkzmfjoudDL5ODEWrVz__hxNwZdbLJj_6mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
انتخابات‌ریاست‌باشگاه رئال‌مادرید از دقایقی قبل شروع شده و تاپایان امشب هم مشخص خواهد شد ریاست کهکشانی‌ها به کی خواهد رسید. شانس فلورنتینو پرز بسیار بیشتر از انریکه خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22932" target="_blank">📅 15:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22931">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJWFGNqeXC5PgjErzknIPH3BqzdMTbsCfQCXH5sDe661rPk9FuQHyUbu8E2FTyXxb1kt70SdqNJ-HgIWliedv-F14_U0ItI-O47noJj8eXZgR0UFdxZdc-42eL2-GIE_wNJo-FsxmyIbozd9Uf8gdu73H2A88y1X7kjMnxfq5L_p0kDPEmcYuAP6_P3CjUnVi9i4SfpmfuyZ5FdWLubZty9eMRcnC_4eF9dZDvEl-HXKlm_BbSiz8KtlKgQNtOX7x3fi37lIzBs5Yfo3wEErjKcb1bb1zEmAYYwh7Nj4vs-EM7buBAIY_tbV_9NS0Mpw9LqqpeQo18c2LaJi1W_v-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22931" target="_blank">📅 15:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22930">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lD764gMbOsy8zwIr1ilxtfHYOn-7zoN4QGnVJmduuvHf7ZZgiHMgztdjn7NQO78nDj4lZW2inw0gmqDACdzZyCs2OUi2BqTKjr9GKN0wK-9RtZUTyCQhfT-k0uAvNJizPTxsccthym-tSHZ9jpww6DHci-5dytbj3lhYdGuV5_vbXbShI7oIVzkXyjRjxKWDtNtphej2spWcxyvNyjulOfPReyq1lmbLE3tnKNxRzQ-0ds-J1jasl8FW4455McRZtYm_tl-hUXNPCeNz4jLKP3Lr2YHer7T4kSzAstS3_-FY1jPKAo6mJiqYt73rXJ0OQGto1NMYAB6I2XvNIycUTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22930" target="_blank">📅 14:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22929">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfCybdqRatxr2Dq7Vbj2RYBR-whiRxmoTJTX1szMd2lUtz05M_9T7rlUJ5APnzy9JwqvF5Hl38_EWxEejPWNXVRiakZ2JYzuVvoGAmtBVBmnkBXxFidh_Qriw4of_Dy6SqUqPbcHku3rJsIGg7KDpsITEJ0YuHgOzbRI26KLyHVn5oLDbWDIbvLBdtyzUes9c3omWiz5i-7a-DTZNwNF5GPzALlo9kgPjBfObEQe3dLEbO-mrMXXQ9g6K_zkHjqCgyuRLVPSU69i--tQVP7otQpWBRgWP7rPpkzOYbQD3_IWHF5HFNikxDGKQLusXgrUGUz7J_1lGBA7eGex1pTjNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22929" target="_blank">📅 14:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22927">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XIW0G0vvxHUihwWUN8OdHA1FEKOIOC2WA6Oej1QagkIv8zxqAGnG6iSssBuhPjiQZjAyi4Y7zg7VTx1Td_Ana5yIzAdCvCGyYlKmdxI6Jc4U2KwLOVpYWXkV-jPiwkR_2B6WtRr8GOx4_idpzgKHK1HP0eeDT4SVPcUmOn3V9EAJmB3xOzbM-lRSMHTuvOAGM5hC9iNJFL3SxRvqSJlxD7ZUuF32P07y_DkR7vZ5PguVQMZI3CsWMES_I6R6WFOTFRkH5H36tQCuDwfjKbsljz3FdacQh6eBCa9GvIGdhAIQYxCljNuazmXpRrdVhccX-4HLzlm0anqt2eqLOWGCiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S8TR_Jo2STE67w7XBuHrSFDe59WzIGe-lk-N1nGLAdi8-WF5Id2YdEsCmojdpwbgUXZ_hkOUAUmqjTApoGJvR1Ij5drj_9ShwT9rzhHQpMkrt64T73LFCm3Zn5Y0qXUvfBDzF2Rffngk7nRLRPPmnV9c1UFlM02tNrZfL4wqxZcxiC3PjrB8XBz89OUidsgbpBBOx_CVJkMliJYp4Awf391EB44eIJ5O3s2cfgMDoWYu0jcTnfjfRfr6QHr91cQ7yhW2KUmOsi6ou8EnKpmK-CXY-bUnbrkqVZmL1NjXyJJym1BCcfxnzw_r_ijNkQEIkXA1eNhTv-n_OjLh5D7OhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22927" target="_blank">📅 14:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22926">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jo00sDTfC8y0LFfZTlD3wg3OvHdvVdDTUnSdPcaE11KawxYvGCIh3uMlZG8LrnxH1xxzwsq7mhrJmOq8mWKKesEgZWH8oMQJUBbCv2tyzl7Lv-UN0ftA_7_UTalz80xv2fLUrFKHyDL-AaKr0ZSgsIDjgLjmte02_XmW-oEzhG5xw1JPw6Bp-qL4kTdRtcTomrTQxAqm-HAUbkuYE5asMWVyMMdvQUsIz0MCqXtmzY_bxD3o9LkY_3UKWiY61HCpfvpACBjNjFNZvBisscnzKirM-4KtcHdpKKg9J1c3DgnJznZq-V0vonMS_c8yAzS_79D118T_aZPKtpRW8MxnUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22926" target="_blank">📅 13:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22925">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgZzrds-zBK3p9ngTMzQ0OlKHJr-FME2f5zmm40B0QPps7Pd65h7_K2roYXIHFJIOl51KnUHJJP26hzXJ_tGsOCjv8kguPzBa-HBoAjJw0vXonLBw88W0kHxhBSUC3zPivoRjKaUJ7shS0etLWHK9UEY-ipfaRAMhZEsDG8DMIF5nIVkLzNI4Tcp4NmtRglBLih_-bBO2xySkccbeRh_P65IXwsFx7xXbJVLfzQXRvEQsqmmxhKbJVJu4GM05ENnassdIOlnClSqvF_7hFmI1eUTiGv3dWpbi522-ep6BCeyDxy_GBLwUk5H03fWne-hSNC72qffxTNQcOhETUicLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی‌کنیم از این ویویو بسیار قدیمی امیر تتلو درباره استقلالی و پرسپولیسی‌بودنش در زمان‌های مختلف
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22925" target="_blank">📅 12:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22924">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I708N2tPHTT034cqqrs_hA52OO5qpAXaBfNHInbtr9KD-2BL6Torp3NseLe-sugZssrcMchb7ICFMwyRYn_nSyDqLvAn2QTu9vARYLF3FJYja8jbn0qQXMQp1MczP1CLm__Wp0XsekJEEUOKXSpADuiszKL1zFC4NDNvTQIjIMdp4ivaJmV9vmNBdMxtNJzj_RwfF3oR6oGUqhI2J9YM0pZ65rU5UKQJtkx9w0zZglx5A_XK1rzh6qIieKAr20aL67CZ6lLCWXDbracojM_INjkqZDJhQPbmOtQWKzoiV5_d6ZGRd-1oaygSaazMVMaf0fJGIiIfeogbev2Vnkzmog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ هفت سال پیش در چنین روزی؛
ادن هازاد باعقدقراردادی به‌ارزش بیش از 100 میلیون یورو از چلسی به رئال مادرید پیوست. او در طول 4 فصل حضور در‌این‌تیم 76 بازی انجام داد و تنها تونست که 7 گل بثمربرسونه مابقیش مصدوم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22924" target="_blank">📅 12:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22923">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a056081.mp4?token=eJZ3llqXtoRPd67oTjg8dMwGOzH7Url28DvvSBTcYmfYAZIfZ5saf503fMfo1hHvZzSaGAbdpLZHxXwJVpnvB5FJrRMcuFHU_VTnuURgjZBHzCEPwTBZNwXlMbBw8Z1g2moYIYxtqQJ-d1azHlUEp6EGTgIh9Lie51Zz7i2JKgh3-MQb8WV4Et08wtOp8l5Be48Htx1z3T-8ztRiobV1ZTsqFGrS4Qrc9KpfWNJtGF_lcaSYRiPJyUSpCHHmEMsv-d6_kFIRl-kEud9I00Qe2WVbYldmubY3MJWX51tbkFf7LcrVq9D3LLtEyEO4lhyLJpqqzj4kpszhptSKC7feIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a056081.mp4?token=eJZ3llqXtoRPd67oTjg8dMwGOzH7Url28DvvSBTcYmfYAZIfZ5saf503fMfo1hHvZzSaGAbdpLZHxXwJVpnvB5FJrRMcuFHU_VTnuURgjZBHzCEPwTBZNwXlMbBw8Z1g2moYIYxtqQJ-d1azHlUEp6EGTgIh9Lie51Zz7i2JKgh3-MQb8WV4Et08wtOp8l5Be48Htx1z3T-8ztRiobV1ZTsqFGrS4Qrc9KpfWNJtGF_lcaSYRiPJyUSpCHHmEMsv-d6_kFIRl-kEud9I00Qe2WVbYldmubY3MJWX51tbkFf7LcrVq9D3LLtEyEO4lhyLJpqqzj4kpszhptSKC7feIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
وضعیت‌‌آکادمی‌های‌ژاپن؛
قشنگ‌ مشخصه دارند برنامه میریزن که یه روزی قهرمان جام‌جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22923" target="_blank">📅 12:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22922">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bU1lp1nWT0YDtORI-veMaFrvaNuDlUbKxlLzsWneB3xJiojaVSdWZRVbTw4qZK9OPF5j70sqfiJzE45hN7YibGk2W0tU_ChB0FxYpszIa9dvX-y-HndAeM8Evc5-oh2hPCFXyfvNTwYJBrSQw3wHeTsXRycp6fsgqAojtmW8XAWdnV12fl-Hv_5T4tIWYJmJvFJteLUv-HkBKBD36fAZbmiISM3ZnQt4cN7vjxrb3KpPRaTQSrTNlfbmwHq8RlAOm4XAKcefkEzK1dsZCc9ebx9dUKu5ejBA1eP3fP3kpcBCdzGk9KkXyTl4MbGOcUqcfGdMR5lLmzqQ39uKSFXM6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حدادی مدیر عامل باشگاه پرسپولیس هفته آینده جلسه‌ای با مدیربرنامه مارکو باکیچ برگزار خواهد کرد تا تکلیف نهایی موندن یا رفتن این ستاره مونته‌نگرویی مشخص‌شه. باکیچ علاقمند به موندنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22922" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22921">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=G5JE-l4saW0sBQrBjZPXDO2LKzmwdj0BLqFq0p9IYJQkfp0D2L0JfTwBSwYED_t9GOf27y5aO1A-OKqCwrBnEc9ZhZJGcuuyhz-3nDpX8uQFNXpYaV9Bkxps1QMuIcU1SRTlVYp3gKLyrQPJQhART8ocuHXJqMniI0k9Ka6Xg36hCb9oyK_HrMG4Y4kR2GyLRyYxpAMcAMfqDDWghW6BW4nRElazFj4BhI6PxU75vLEttZw3HcdvjzodifhNii44gLhP-bfuRXyIcGe3WixpEtPSRCdRFltPb68IqpU98sDQ5BdWxp-RBRJwl8uqPXfIzgxAAyqqXBhHkYczTz9Isg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=G5JE-l4saW0sBQrBjZPXDO2LKzmwdj0BLqFq0p9IYJQkfp0D2L0JfTwBSwYED_t9GOf27y5aO1A-OKqCwrBnEc9ZhZJGcuuyhz-3nDpX8uQFNXpYaV9Bkxps1QMuIcU1SRTlVYp3gKLyrQPJQhART8ocuHXJqMniI0k9Ka6Xg36hCb9oyK_HrMG4Y4kR2GyLRyYxpAMcAMfqDDWghW6BW4nRElazFj4BhI6PxU75vLEttZw3HcdvjzodifhNii44gLhP-bfuRXyIcGe3WixpEtPSRCdRFltPb68IqpU98sDQ5BdWxp-RBRJwl8uqPXfIzgxAAyqqXBhHkYczTz9Isg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیبروین یجوری به تیبو کورتوا پاس میده که انگار هنوز از دستش‌بابت دزدیدن دوست‌دخترش فشاریه و میخواد کاری کنه در تیم ملی سوتی بده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22921" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22919">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odF4R993-ZdHgLKwlXRRdTNNV0e1gMGMxaXTPFGUt35jfedFhEKCfPU_5snUB4Ktbj-cqO5_2NKVJ-oin7MSBlgygJ_2mk6TCUIKxQteEhsXMHv7I7NGujapBgOVKreoouFI2_SBnbtbz4ZpVI_yayg9ygg_2wJcEr8DVJ_bXTbGuNIbBY-k1JpC6JlUxTBnB1F-M5H8fNEcM7ayDiQAM3baBB8YD-iyYj6z5WPKSF3Gs4OtCqS3P5UdSPo6amVvDqoNyh5DejHup-lCxsVLaSlK7IHlKbG9Ne3umZy01JW0KaHI-hcBKe39PC26hIELRYY13cSITqhrsbpNizCU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/22919" target="_blank">📅 11:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22918">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hf_nZBMfo6TCz7j5fOOoQAahwXPhUYL7pV2nzn9in7l98xTOZwiOIkznO2yQzAkd3I9u490eS8jO9JofC2EmTmdNpMFwkK__BsFgJdRAN7GTwEaIoxrHemFIdGmPH1h9H3-plkeEvv52OvCKKt5rSnejwuHygDHFEyg0xFlFa4t0TRHm6bRfg2JC1rw3-8QmEwOgOAwQlyXZWfqiRARAChYJH45H1eV6MZwhhh1qmACU85RpSudrDQ00ikZESKnlohvC1HPsqM-77JGme2KkgHrIEAZCI81pCVCDdWmE8-HTxSZZtiv3rtUCtEhMsxufOg-oSc-miM2iqmBoUItRmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22918" target="_blank">📅 10:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22917">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=V2N3jXoDz8bl_OwfSXdiSsiAfgU7B_fiG3KXQ80eGMgnYl4u9gnz3gxS-qp_lFIAIXREe_k4qNBPheB32IF8WROoidk41Ds-32CdLxG1GduKI18l84DFEOuEeUMRRKWRqyHWnb5c138AL2KSzX1tWzBNTbuirNQUt8XuvR9ZMe4xjsNN7v0jH9LygU9YYouwL66Lhf6z1wmqspHxKabh-F6CfFPs7s9pOGnqM8i26gY58Tp6WJC47_-kxXC_4Pyfsibm6oDz6E4EEGlZqfFHzc0zYxi8NgcR3uaCWfD9ioLhwvloZ1h-TNbjvUSzQo5-ZFgRRWB5gL45YuUFag885A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=V2N3jXoDz8bl_OwfSXdiSsiAfgU7B_fiG3KXQ80eGMgnYl4u9gnz3gxS-qp_lFIAIXREe_k4qNBPheB32IF8WROoidk41Ds-32CdLxG1GduKI18l84DFEOuEeUMRRKWRqyHWnb5c138AL2KSzX1tWzBNTbuirNQUt8XuvR9ZMe4xjsNN7v0jH9LygU9YYouwL66Lhf6z1wmqspHxKabh-F6CfFPs7s9pOGnqM8i26gY58Tp6WJC47_-kxXC_4Pyfsibm6oDz6E4EEGlZqfFHzc0zYxi8NgcR3uaCWfD9ioLhwvloZ1h-TNbjvUSzQo5-ZFgRRWB5gL45YuUFag885A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایگزین تشویق ایسلندی رونمایی شد، تشویق وایکینگی هوادارای نروژ؛ تو جام‌جهانی اینکارو بکنن ارلینگ هالند جوگیر میشه به هر تیم 5 6 گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22917" target="_blank">📅 09:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22916">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4BA33U3qlgzcQPbuFa9Ss75EHSpCSFa3pSVkx1yK8xS01KwJZ4ynFGsyHANt6clC4oIpyyBZJnwFmyAoeJWMI82LFCHiEk1p6Wdv7JZhElo0NWppGQxP4L3rCRNewyWAZoEzegqDtmFE-K7uhSdDtCx_uimD_z3sDpMWVa4scIJtupfdXE31dSyF3v5KHqquIAJrGaW2CECiycuC2Gm6IJOb0riN7ha0qo8uw_BR9HAaPvrBG9GRPZZ2uBtOg_64d0mMdYVBwsBeWa4TRVUQEaRHIBsGRef2opY9L3yLnoz3M47ZEpkPFF5a13nA0_IR-gnPOEgBuSKlWcrtwKX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصاحبه تاریخیی کاکا:
برام مهم نیست که بچه‌ هام بدونن یه زمانی بهترین بازیکن دنیا بودم؛ فقط می‌خوام منو به‌عنوان بهترین پدر دنیا بشناسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22916" target="_blank">📅 09:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22914">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACdtSeEuM0d5i-i_mRlpuzoVrEOfPMkZP-NbKObrTgfUZ8lFtxLFIdNcj9AOEn-kAdWjcDV07_aTKPtga48POtdTehZSdZC8qL5d936_rHOm8zv6-pDDu9yA_cbxsi8Q11Em1w1hw4DhI2sah5SaU9AEL71OW2oQCVjyD02lCX5uqU0LrwpspJoDRjNAekrrlTsSYI0TpuF0Bw8_sYwC98cPyDrXeeGYSeWNHW4ApQSg1X2BMVJxMdAhzvXk0L648eDqXUcU6s7i2fBOla6UowEdq2_WQNdPsZI0HMYU9OS1UAOVfs-0N-WiyYSx28Li1YJ4ulwU-rygR5RcPOkvzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
تقابل شاگردان کارلتو با مصری‌ها و جدال یاران مسی برابر هندوراس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/22914" target="_blank">📅 01:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22913">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tle8SA5mCqjhoQOBYrxnNwa8662Hmt1Gb5SGgcKioZSXsRVAeVRrlMHR6xTB3pUKJkxFU92cndDIqYXzA4NFUDQKMunX52FuvTsuUrNxrZ3V9IndLkKZC8rB7ODxzcDyxXq3e-ijoSfKm6UCHgijSBmhg85av4OyDJEPINn0nOJ9K2tjpqD_Wcc0l5hlavf6xuwxgwm_XGOIsS43Y4VjNOVPA18JgXlAEljxbsWWJKsiWr2y84XxHUEhKRDAJhmkyMD8EQYzSmEMuOwdVfwSGjiiejHnD5Y41pwsuOrc7rXANsBv2n0IfZZxRq9sl6z-iDW_DSJa4PpSjQthYdsxiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از بردپرگل بلژیکی‌ها مقابل تونس تا برتری تیم ملی پرتغال برابر شیلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/22913" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22912">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwkDGUonMGXaU6oaZ-Wu4gRcI90K8NXLPOM6jqZh0TlQxPD5h3d0IiRqam6LOtIAdvBg_ODssvByWbGfUUjYjpDvIvRchEqMIxRmQXbNYRqp8rskEFAcTI00dM7SJW4eU2bS7rqeb-ABUvfmnxWgwH69lDBqnJdKcACRd6jyLHkENZLevKCVCdXUSFBHUkJLqZmOj_FXrK3hoY62DpkRcIMwMPMQ4FboGlmZOXJECrGtBQgmsOD4dtGLKKMDEszVjMYSCF4JvrBrlObYRvVt8b7ZdoqD7H-3uD1kYEtYU7rA0sSnBt8XiFmuf1DpS7rJ-Iq_IrUUm2z3DNLn-g8agA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/22912" target="_blank">📅 00:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22911">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=j4aEVlcGdsEWLqml_zCZCllIZfvqaYVRuLAM7o6Jg2IDIr2LUTrQHm8U5UDeJsAfYJG3ddQ6lTVZOzJahCJREZmSOQ24up9KV3-6zSRr1-SqyPGoNFSkOIHZjF2XDZb1uBNiz726sQQVu1dCJe3Pr0OZPZG3U6BzhBzHtvhGLKYQ2sIA79tOeQalIhV0eCM_T-xpP-Cu9uJaLLx1jvFZOA-dTeXf37p3VxIpViNk43igwiHtM3-k5-QYnJRQeluggsJEGTMMvqBr2SIWbHLre5sTKAxAmiibjXTvmDJ0VcT6wC2jO3F761QjIC34H7JF0qkYyn_ID4g-ZkjGf-STcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=j4aEVlcGdsEWLqml_zCZCllIZfvqaYVRuLAM7o6Jg2IDIr2LUTrQHm8U5UDeJsAfYJG3ddQ6lTVZOzJahCJREZmSOQ24up9KV3-6zSRr1-SqyPGoNFSkOIHZjF2XDZb1uBNiz726sQQVu1dCJe3Pr0OZPZG3U6BzhBzHtvhGLKYQ2sIA79tOeQalIhV0eCM_T-xpP-Cu9uJaLLx1jvFZOA-dTeXf37p3VxIpViNk43igwiHtM3-k5-QYnJRQeluggsJEGTMMvqBr2SIWbHLre5sTKAxAmiibjXTvmDJ0VcT6wC2jO3F761QjIC34H7JF0qkYyn_ID4g-ZkjGf-STcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصدومیت شدید مهاجم صنعت نفت؛ ویدیویی که روزتونو میسازه؛ فقط کامنت‌ها رو بخونید
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/22911" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22910">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=aAnmBkUujf8sqzhveUK3TALmrRF-CQK5KMQMCU9PyQHaS_lZ8tAvRvpxIlRE5kwHa7bI2V5_Ro3xp3ekHTJCyb8MBTFwm8_n_e89hD72k1jexXw0YcBmeheRnUT_Hs7CL8swxlt7rF1LsHcB6E2ljt6wJXbfmqkS7vXhvuwbxBDZwpv0yIgRmg7EdyGdnyMCcR6eOXuqu1aLBCjRxUjH3fCtYFwyvHM3Wx_XD_-jAly_6vxz-NqdAXYeUBBF4afMApdLiGDEFxdfRl9HdlWtx8T1cs5LAwsKYxK8jGSTWToReIE3KAMqNsre55iUTwjqDyGRQxyfbUeE6RMMVIqscw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=aAnmBkUujf8sqzhveUK3TALmrRF-CQK5KMQMCU9PyQHaS_lZ8tAvRvpxIlRE5kwHa7bI2V5_Ro3xp3ekHTJCyb8MBTFwm8_n_e89hD72k1jexXw0YcBmeheRnUT_Hs7CL8swxlt7rF1LsHcB6E2ljt6wJXbfmqkS7vXhvuwbxBDZwpv0yIgRmg7EdyGdnyMCcR6eOXuqu1aLBCjRxUjH3fCtYFwyvHM3Wx_XD_-jAly_6vxz-NqdAXYeUBBF4afMApdLiGDEFxdfRl9HdlWtx8T1cs5LAwsKYxK8jGSTWToReIE3KAMqNsre55iUTwjqDyGRQxyfbUeE6RMMVIqscw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
امباپه27سالش‌شده؛هالند 25، اولیسه امسال وارد 25 سالگی میشه. اینم لیونل مسیه در 25 سالگی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22910" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22907">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=s1Hl_A2oQC3fAIzN2POkN_an6sAHTkfYBytz2H2hGOM7jQ0mHtHkkrd-tXf9BYtKsmpZ91FnD5u0s0u9aevYArgUZojJJ2DpQ6bgbdT4e2J6F0OioIq2b_zpE0_lso93I3tSBSB3BRtoe70ltFTJPtQdPxvxSC47-3pXZ7XtspDTb6u45qGYT16zZUn-_2O0ZWDBEdNn_lhUxZoPOSX5iBu_Jz85ouTYFW4DsH-Ubsh6ESr2cBcIvKsPwAC9SkjxcrJEoEJ5e6bBJivtEa4URIFcIvawtMF26Muh9kBI13OP1YeWbNJfgm_aTXW2dWeTh6ghD9tngPadt9Rtj2h8FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=s1Hl_A2oQC3fAIzN2POkN_an6sAHTkfYBytz2H2hGOM7jQ0mHtHkkrd-tXf9BYtKsmpZ91FnD5u0s0u9aevYArgUZojJJ2DpQ6bgbdT4e2J6F0OioIq2b_zpE0_lso93I3tSBSB3BRtoe70ltFTJPtQdPxvxSC47-3pXZ7XtspDTb6u45qGYT16zZUn-_2O0ZWDBEdNn_lhUxZoPOSX5iBu_Jz85ouTYFW4DsH-Ubsh6ESr2cBcIvKsPwAC9SkjxcrJEoEJ5e6bBJivtEa4URIFcIvawtMF26Muh9kBI13OP1YeWbNJfgm_aTXW2dWeTh6ghD9tngPadt9Rtj2h8FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی‌داماد مجلس خیلی فوتبالیه، کریس رونالدو فن هست و به‌هیچ‌وجه هم اضطراب اجتماعی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22907" target="_blank">📅 00:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22906">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=OEeJKHNZpXbClJn-OrDzIX5R8iZbFLmD-_isJhVgmXnUGx1bnmzgNeVas8o5UgQOn6UYRMEkHgPC1Dzs1fAukTZz0zEPJBROKikncm5k3YIepDaUDuRS2OD98zxTlhE6a21hXTMzgc2qg9ow2VNsVK_Kch2F3iXuVXbRjUIM9KZ2cWaoE6twng2vzlx0qeSqr-Nq86nHOS--pDJDFU83OuOpEcwPfN5vWwqb1QKvQGDKgqajLBRJRX88xgoo3MPqKqcroZVM3PbXug50x-1yawf5LpwI6lHfV-3SjVVaxeQ6Z3S2sOVAWAzSuBv6Dm7AouVFl5kN6wPDeqhoafrSQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=OEeJKHNZpXbClJn-OrDzIX5R8iZbFLmD-_isJhVgmXnUGx1bnmzgNeVas8o5UgQOn6UYRMEkHgPC1Dzs1fAukTZz0zEPJBROKikncm5k3YIepDaUDuRS2OD98zxTlhE6a21hXTMzgc2qg9ow2VNsVK_Kch2F3iXuVXbRjUIM9KZ2cWaoE6twng2vzlx0qeSqr-Nq86nHOS--pDJDFU83OuOpEcwPfN5vWwqb1QKvQGDKgqajLBRJRX88xgoo3MPqKqcroZVM3PbXug50x-1yawf5LpwI6lHfV-3SjVVaxeQ6Z3S2sOVAWAzSuBv6Dm7AouVFl5kN6wPDeqhoafrSQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/22906" target="_blank">📅 23:32 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
