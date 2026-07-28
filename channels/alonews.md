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
<img src="https://cdn4.telesco.pe/file/NN4HfmiDHW0sqdnzSg7OUi4qHOzjbIdiVVC_KKl3ycV5uKohRGQ9O2m4FnlHP_x8PWY6wNz1m2xFs3IiwlRVrazdN256QAxqVpP2VhLgLoBZ9YehYMVfNFp8_EYGjNmrSzO0fXN6e7pQUr4D_GMvoAtrpNQ_jNhKr3T7oBlDA3QHzGqLgoRU9zwH45RKTlopK5AlbRE_trmUvGH-zD39t1eHNTjKGBLhUTH3KyFCjCVm8yIwJNQZ0TAY6P2TLVc7qZ0ZtZvQk1lnMeaGXod6v7XfOIruruDk3REBXePd5iSLyRAzWqXSJLDwB_L0zz3XrEHbn3iK2OQK3TxYG5RIxg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 974K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 14:01:43</div>
<hr>

<div class="tg-post" id="msg-138125">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز:
نتانیاهو به دستاوردی رسید که چِرچیل نتوانست.
🔴
او ترامپ را با ما متحد کرد تا علیه ایران اقدام کنیم، به طوری که آمریکا را متقاعد کرد قبل از وقوع یک حادثه مشابه پرل هاربر، وارد عمل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/alonews/138125" target="_blank">📅 13:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138124">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teXAQIMKSKL95NFznXgJ93Y8nVtrNAoWIXRKMoRn9Tu6ejMlX61HDw0dLfZSKRZ7i9ibjIciY3BjRErTAZj4M9Ux6c35Kxoaizf_WMn2JY3UwssiMH1wR9zf8QorBF2vmDXpGTRngcfTmj71b46doeCrqkmUQXBSzBnJrs6YhwOPkjAHr_NUpUCv6pxe1HdJPzTTxPah04VcvSB7Nrrfay8o0AY4_OBYwbkw6p_JnOm00-M1BwMl3sf_ZwZCCKe1Yh4ZwHsQ1Vb5LWV_CHNO6ZyBW-udHRqo9YFFATXavdU-VFadGmXnEjhqINeplEauVwpdFkRnfnBchqFTOfSovQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام آمریکایی : تصمیم به عدم تشدید تنش پس از جلسه کاخ سفید در روز جمعه گرفته شد. دو منبع اعلام کردند ژنرال دن کین (رئیس ستاد مشترک ارتش) و جی‌دی ونس (معاون رئیس‌جمهور) نگرانی خود را از تشدید جنگ ابراز کردند.
🔴
کین به ترامپ هشدار داد که اگرچه ارتش قادر به اجرای گزینه‌هاست، اما پیامدهای منفی از جمله کاهش ذخایر مهمات وجود دارد.
🔴
کمبود مهمات یکی از عوامل کلیدی در تصمیم‌گیری ترامپ و تیم امنیت ملی بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/138124" target="_blank">📅 13:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138123">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f005de3ae2.mp4?token=fO-r5D9lTVmOREOLNk4sGNjLz-oIhLSEXbuNYQlxi44g4ywX2g2Po76ZBaTDS27M0s-pVejZqSpfcJAhmDKEPIur9xvKspiHo_FRLc9_d5v9aVHTu7iHlD5fd0W2JtKPbGksdpZJq8Ree1wNYsSWXmgq6A_gzuezTvu-vvomPYLzEAXBPcF9bFQPfCjPoRPMIPpDn0Q4pwe4XGHva7i2tkTE3uuTtbgJnwFqMrfBhWYO6jZ7vQOJNmj55U06q1A9YWxM5bSC59TzixsIepqhgKREH9hPZR62ExrK6-pfrNDS6VMv-eCVQEkaOhLoNQNnSiByfP80Ej9qJimQvyiVWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f005de3ae2.mp4?token=fO-r5D9lTVmOREOLNk4sGNjLz-oIhLSEXbuNYQlxi44g4ywX2g2Po76ZBaTDS27M0s-pVejZqSpfcJAhmDKEPIur9xvKspiHo_FRLc9_d5v9aVHTu7iHlD5fd0W2JtKPbGksdpZJq8Ree1wNYsSWXmgq6A_gzuezTvu-vvomPYLzEAXBPcF9bFQPfCjPoRPMIPpDn0Q4pwe4XGHva7i2tkTE3uuTtbgJnwFqMrfBhWYO6jZ7vQOJNmj55U06q1A9YWxM5bSC59TzixsIepqhgKREH9hPZR62ExrK6-pfrNDS6VMv-eCVQEkaOhLoNQNnSiByfP80Ej9qJimQvyiVWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش ها از وقوع انفجار های مهیب در مسکو پس از حملات پهپادی صبح امروز اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/138123" target="_blank">📅 13:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138122">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز: در غزه، ما نه تنها آنچه را که زیر زمین است نابود می‌کنیم، بلکه تمام خانه‌ها را نیز ویران می‌سازیم.
🔴
امروز، تقریباً ۷۰ درصد غزه ویران شده است.
🔴
بیست و چهار روستای لبنانی، صدها سال قدمت دارند — ما تمام ساختمان‌ها را نابود کردیم، نه خانه به خانه، بلکه کل روستاها را.
🔴
نابودی آن‌ها به پایان رسیده است. باید درک کنید: ۱۵,۰۰۰ تا ۲۰,۰۰۰ خانه در تمام ۲۴ روستا نابود شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/138122" target="_blank">📅 13:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138121">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/000767d83f.mp4?token=OtubK-VkenvJOuxZBcLPhcVyd-LU3nxUtyVzEkg0vimQNxp7s27utYOjAlm1U4GDAOeICWXzC9StXy27eXOje0s7L_J6tAD7HtW-bYe_Edgi2KeI7-_WUc8hxYHact58NUCQfQwMapiarZATkT8yDQV-GtVTGRy3CiDwjKsIl6H7Y4Zb55rwrD9EZX_O2mKH9ck65Z-5xEpE-5-pvFEyGphxkl9guPuBGQpF2gQ_ORNRgov10hIXBeDsv1yYfQhoqalr7Bv2D2RIwH3oU-xB9bD_Lt5h_tK4YkSYH_VaijhU1PavhAjE9hahIAFjtIOlGoDuYpH67j2JtiQZBeINMJnHbOfDIkFGAmwxWKZFt3Q0AP2HkkeJGEStC-1-OAVFC7q22spgaRG2SVA03-GSCzdSsD2pWvv7WfFTLEroO9CdjT5SJ4IOY8DRRszEttZQpTjH52rHAOkfxMPNgkN0bu1w2nF2rMpghplrh8pTIwk7EVUJdXqwfJL_bIuDStk0ZrzCMpgubY5qXooPQK3h0mYa1KFF6tAoktcetXbNNcIW3TfIJrEqYKALZBPQUWryC9It_JPdsa3yTHXsXN952wMGO3z4phwB585I_UMlch99Q5rOyIRfPIx9qWek2fCbdwk7588O4HTi30Fqb7Kt70bisayxE0Gwyrez_3O7U2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/000767d83f.mp4?token=OtubK-VkenvJOuxZBcLPhcVyd-LU3nxUtyVzEkg0vimQNxp7s27utYOjAlm1U4GDAOeICWXzC9StXy27eXOje0s7L_J6tAD7HtW-bYe_Edgi2KeI7-_WUc8hxYHact58NUCQfQwMapiarZATkT8yDQV-GtVTGRy3CiDwjKsIl6H7Y4Zb55rwrD9EZX_O2mKH9ck65Z-5xEpE-5-pvFEyGphxkl9guPuBGQpF2gQ_ORNRgov10hIXBeDsv1yYfQhoqalr7Bv2D2RIwH3oU-xB9bD_Lt5h_tK4YkSYH_VaijhU1PavhAjE9hahIAFjtIOlGoDuYpH67j2JtiQZBeINMJnHbOfDIkFGAmwxWKZFt3Q0AP2HkkeJGEStC-1-OAVFC7q22spgaRG2SVA03-GSCzdSsD2pWvv7WfFTLEroO9CdjT5SJ4IOY8DRRszEttZQpTjH52rHAOkfxMPNgkN0bu1w2nF2rMpghplrh8pTIwk7EVUJdXqwfJL_bIuDStk0ZrzCMpgubY5qXooPQK3h0mYa1KFF6tAoktcetXbNNcIW3TfIJrEqYKALZBPQUWryC9It_JPdsa3yTHXsXN952wMGO3z4phwB585I_UMlch99Q5rOyIRfPIx9qWek2fCbdwk7588O4HTi30Fqb7Kt70bisayxE0Gwyrez_3O7U2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز:شین بت در برابر تهدید بسیار جدی ایران که علیه نتانیاهو و رهبری سیاسی و نظامی اسرائیل متمرکز است، محافظت می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/138121" target="_blank">📅 13:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138120">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b128a10dae.mp4?token=XeJRGuyeNHeuj9PPDVqXIPq-G3IECamvSspJBm7pppTbRUIhh5AyZ1V6i_IuyuPDQ7RvqGrc6Rut0a5-DYiHGcTd6Ee1Lv8Dow03aAOEW-uiuUmugXJ5eWXh9i7XJlZ6bLQUwP0Ui2n9RVKM5aLj3quV6Z3UOzcaB6fxau4HXN8WEVFvCG2ND0Z29TZ38j7inZHskNrXj_O1Rz-JVP_IMilV31iEz2ZcgiuWupjVRgA3gO2jishxhzp4957L3O3vcI-q8dRUi4c0Wg5M1_I8OLMLsGOWHhHuzup_9Jad858Dkm0D0a223alnTALy29a24jHgitRGxtyupq8rNknxT6Hb2Vo_7wJKpTNxjoa8W9poIwB2KL087ecKBu-lAAcsgq1uDkfYCHB-vIR8fllsn24t1P8bUSmYaGGNUVTeXXZkCSq4kJl10ywWAZj3FejV9BcvzKh6a8sroU1jxw2Z5aEfddSUmPyyiUN16SkvegzqqMiBTJmWBqdfzP17aoIPrMPWA0sLQEGbneKqhfcUs8JN_cKNQMvj0v3Fx_1OkXf1vphz1Mu4C8uE47X18v0RNEKEGkfSD0-dBv9riMf_sRI90JaL5nxp9UjarS9OJ8tId6DZobnfpm7aoTKHSsvSUOQF_7V3F0g0sO8miUvxEdAwiaWJ1Ap0dbYY6UvjQdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b128a10dae.mp4?token=XeJRGuyeNHeuj9PPDVqXIPq-G3IECamvSspJBm7pppTbRUIhh5AyZ1V6i_IuyuPDQ7RvqGrc6Rut0a5-DYiHGcTd6Ee1Lv8Dow03aAOEW-uiuUmugXJ5eWXh9i7XJlZ6bLQUwP0Ui2n9RVKM5aLj3quV6Z3UOzcaB6fxau4HXN8WEVFvCG2ND0Z29TZ38j7inZHskNrXj_O1Rz-JVP_IMilV31iEz2ZcgiuWupjVRgA3gO2jishxhzp4957L3O3vcI-q8dRUi4c0Wg5M1_I8OLMLsGOWHhHuzup_9Jad858Dkm0D0a223alnTALy29a24jHgitRGxtyupq8rNknxT6Hb2Vo_7wJKpTNxjoa8W9poIwB2KL087ecKBu-lAAcsgq1uDkfYCHB-vIR8fllsn24t1P8bUSmYaGGNUVTeXXZkCSq4kJl10ywWAZj3FejV9BcvzKh6a8sroU1jxw2Z5aEfddSUmPyyiUN16SkvegzqqMiBTJmWBqdfzP17aoIPrMPWA0sLQEGbneKqhfcUs8JN_cKNQMvj0v3Fx_1OkXf1vphz1Mu4C8uE47X18v0RNEKEGkfSD0-dBv9riMf_sRI90JaL5nxp9UjarS9OJ8tId6DZobnfpm7aoTKHSsvSUOQF_7V3F0g0sO8miUvxEdAwiaWJ1Ap0dbYY6UvjQdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز، اعتراف کرد: امروز شجاعیه وجود ندارد، جابلیا وجود ندارد. تمام آن مکان‌های وحشتناکی که به یاد دارید دیگر وجود ندارند.
🔴
رئیس فرماندهی جنوب به من گفت: «من خانه‌هایی را نمی‌بینم، من سواحل را می‌بینم.»
🔴
ما غزه را نابود کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/138120" target="_blank">📅 13:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138119">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/102fae8e7f.mp4?token=TzOQBGOTGjySXr-csYQeWNXJCzJGwd5TGymrtyOLcdMR8YTaxR5dopA7kwdK_sumIYfMtcq2oX02DofhF0uWBYe7xxYXvLnxppe0Rbw1gE6Hg3fINkVcJjGx_nYdy468hlGVKZTzVWKSyr4YpOw0y-4-OM-ZFHFfCWm_OdDZwjDdfHPuAf5rEylCKQYMmBTN5lPLEuzR6cOmSd3n2DLb6O1JxNvfowXrN8382w1Hc69RjkRIyieYxJRx-9grfYfQ_ci-4yJXlj4ba6HElp-NW7u4UcjhbUWEx0jn-B3fdSJkFB20eUqyi0HMSj5VAGvuwPm7PGHRhd2wITbmqf2I0ystIUpn8MMRXrcaBzj0h7qewQ0w_5XLvk2TckEpPXWasnqvW0tA8Qmz8YU230r23hJ4a7LvZ9uu6XY94-Vb6go11TH8En0zO_vzi-gu9j8KX9GQ6w28TVGXYC25BLROdKRwKeZ659vT_aL1Qw_T16iBYPhFqGn5tY6xaW2nEr6BEMOksdEk6o8miQdkTIXvMqUDlMrFz9Jg-GbGsJu8QPQBugYKWIs80d892y5MMkX4KDrirBtVOoUWJA8abj8EiAo6vaJlw64a-kke-n9LzMtlPsRf2eQehY0EruKnulsmCIBz3FGJr9ja6AFdkDeggkGG-ghJFYNr9b9vbO1sbbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/102fae8e7f.mp4?token=TzOQBGOTGjySXr-csYQeWNXJCzJGwd5TGymrtyOLcdMR8YTaxR5dopA7kwdK_sumIYfMtcq2oX02DofhF0uWBYe7xxYXvLnxppe0Rbw1gE6Hg3fINkVcJjGx_nYdy468hlGVKZTzVWKSyr4YpOw0y-4-OM-ZFHFfCWm_OdDZwjDdfHPuAf5rEylCKQYMmBTN5lPLEuzR6cOmSd3n2DLb6O1JxNvfowXrN8382w1Hc69RjkRIyieYxJRx-9grfYfQ_ci-4yJXlj4ba6HElp-NW7u4UcjhbUWEx0jn-B3fdSJkFB20eUqyi0HMSj5VAGvuwPm7PGHRhd2wITbmqf2I0ystIUpn8MMRXrcaBzj0h7qewQ0w_5XLvk2TckEpPXWasnqvW0tA8Qmz8YU230r23hJ4a7LvZ9uu6XY94-Vb6go11TH8En0zO_vzi-gu9j8KX9GQ6w28TVGXYC25BLROdKRwKeZ659vT_aL1Qw_T16iBYPhFqGn5tY6xaW2nEr6BEMOksdEk6o8miQdkTIXvMqUDlMrFz9Jg-GbGsJu8QPQBugYKWIs80d892y5MMkX4KDrirBtVOoUWJA8abj8EiAo6vaJlw64a-kke-n9LzMtlPsRf2eQehY0EruKnulsmCIBz3FGJr9ja6AFdkDeggkGG-ghJFYNr9b9vbO1sbbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز:
محور اخوان المسلمین محوری است که با گذشت زمان می‌تواند به همان اندازه خطرناک شود. ترکیه و قطر بخشی از آن محور هستند.
🔴
اخوان المسلمین نه تنها علیه اسرائیل عمل می‌کند، بلکه برای سرنگونی رئیس‌جمهور السیسی در مصر و پادشاه عبدالله در اردن نیز تلاش می‌کند.
🔴
این همان چیزی است که ما می‌بینیم. شاید ایالات متحده آن را متفاوت ببیند، اما ما مسئول منافع خودمان هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/138119" target="_blank">📅 13:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138118">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
کاتز ، وزیر جنگ اسرائیل: امپراتوری بزرگ ایران که مغرور بود و به دنبال نابودی اسرائیل بود، فروپاشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/138118" target="_blank">📅 13:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138117">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkJfslyxquzvdW2sJ7fGMDMnlXeQFkk5Cdp4NCZlRE3JflXrB7FVyl49_4UIpED1fYRF1iRwjp5Ae_bLAcKt8W6-HGy_ANyPFqU5Wa8SbnyiN6-wVn1OY-N9t9KFtDzvQZowgo3isAgHAahSbVAlJFFJP1sL3lVBzrLjUu00ABBaQErVQ974e3hHT9quyfc7ZrTMvzogOVyOAq0cANpO8_07v2HjSbbxLOi2INPW8ZZvUSwkIDtJ6g5cagYnVT8n7AQU3YY7vxdAJjo8nKL7C6JzfyXFhC5hCikAvbHrhZ6oppG7szcfl0Jcjbf5ynambFEKW6SvKZQ-yqZ9XgkveA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست ‌وزیر عراق عازم ترکیه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/138117" target="_blank">📅 13:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138116">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کاتز، وزیر دفاع اسرائیل: ما دو بار به ایران حمله کردیم و برای بار سوم هم آماده‌ایم
🔴
ارتش اسرائیل هم دستور گرفته و آماده‌ست که حتی به‌تنهایی به ایران حمله کنه
🔴
البته الان تنها نیستیم و آمریکا هم کنار ماست، باید دید واشنگتن دوباره وارد عملیات می‌شه یا از…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/138116" target="_blank">📅 13:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138115">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
کاخ کرملین:حمله اوکراینی به یک کشتی ایرانی، به منزله حمله به ایران تلقی می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138115" target="_blank">📅 13:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138114">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رئیس کمیسیون انرژی اتاق بازرگانی: در پی حوادثی که در جنگ ۴۰ روزه برای کشور رخ داد، روزانه بیش از ۴۵۰ میلیون متر مکعب کسری گاز داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138114" target="_blank">📅 13:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138113">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: ما به شدت خواهان حمله به تأسیسات انرژی ایران هستیم، اما ایالات متحده در حال حاضر اجازه این کار را نمی‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/138113" target="_blank">📅 13:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138112">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
نتانیاهو و ترامپ امشب ساعت ۱۸:۰۰ دیدار خواهند کرد. این دیدار بدون حضور خبرنگاران برگزار می‌شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/138112" target="_blank">📅 13:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138111">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
فایننشال تایمز ادعا کرد؛ چرخش ژئوپلیتیک بن زاید؛ امارات در حال احیای کانال‌های دیپلماتیک و اقتصادی با ایران است
🔴
ابوظبی به دنبال تنش‌زدایی با تهران است
🔴
گفت‌وگوی مستقیم سران امارات و ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/138111" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138110">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: ما به شدت خواهان حمله به تأسیسات انرژی ایران هستیم، اما ایالات متحده در حال حاضر اجازه این کار را نمی‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/138110" target="_blank">📅 13:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138109">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwOJz1ABdlswHBb0PCdqVW7ZpLsIOWh_KJ5Q_MdR9YaTXdgimTDXdqd_0B4FOmlOIQVtD1WehvIAWwR5JPH1faTcSub5WJaYHvskkv8z1mSWdSmw_vwGGR0bpw0Kw6uI2aEWCuH5bt9Thay7gRWT81bx3ba0o7Y43bAdKPmqbkfa1mkoQCNN1qhZwqXTXOPM9K7XqrClUilCMDmTj285EjzPbTOjc_mNUe2nVOhe9psShjqjwUzC0OCKXg7kdXLiPCu-l-dFtoTscberj569ESK0jyUmU-WSvshnJ7W-asNeezAgjOofjGi18U-reCGaYwVm4Mi5NJuStC-O3Fh5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۱۷ هکتار از مراتع و جنگل‌های بخش مرکزی سردشت در آذربایجان غربی طعمه حریق شد که پس از پنج ساعت تلاش، این آتش مهار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/138109" target="_blank">📅 12:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138108">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
طبق گزارش شبکه i24، عراق در روزهای گذشته، ۲۰ پهپاد به سمت اسرائیل، اردن و عربستان سعودی پرتاب کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/138108" target="_blank">📅 12:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138107">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش ۵۷ هزار واحدی به ۵ میلیون و ۱۰۹ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/138107" target="_blank">📅 12:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138106">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84bdc994db.mp4?token=RuJBtulgomzXY6DBJXA6F0rT6pi1uC58Q4rN0Rn_gyUeI_0ZXbXl5fNtbNMt_QXMLHrGVtf24U85LHAKLaxZmURDWnxui67CaYa0QJtLDYXZ4NUp_67rxd33DLEkAfq_QboyYXJV4n5f63edlUd4-cTb0K1_4EeaJ5ZFTC0Tcx0RQx7NQ1JUg45ER3RauC68nZ4185apQe4g-QRrx_Ihzj_kp-78kreMq8NuCjzUd2B6D1-4t2HybgGooMbEX-638fqKs14kGlcDySAMAqcM_tJRxkM6aP4qF-9kfm_7qqxrF7_3175kBP1L8txbM49BNjWfqNBPG1UQG2WGw80ukQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84bdc994db.mp4?token=RuJBtulgomzXY6DBJXA6F0rT6pi1uC58Q4rN0Rn_gyUeI_0ZXbXl5fNtbNMt_QXMLHrGVtf24U85LHAKLaxZmURDWnxui67CaYa0QJtLDYXZ4NUp_67rxd33DLEkAfq_QboyYXJV4n5f63edlUd4-cTb0K1_4EeaJ5ZFTC0Tcx0RQx7NQ1JUg45ER3RauC68nZ4185apQe4g-QRrx_Ihzj_kp-78kreMq8NuCjzUd2B6D1-4t2HybgGooMbEX-638fqKs14kGlcDySAMAqcM_tJRxkM6aP4qF-9kfm_7qqxrF7_3175kBP1L8txbM49BNjWfqNBPG1UQG2WGw80ukQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر انرژی اسرائیل، الی کوهن: ما دخالت‌های ترکیه در سوریه را نخواهیم پذیرفت.
🔴
اگر ترکیه پایگاه‌هایی در سوریه ایجاد کند، ما نیز اقدام خواهیم کرد تا پایگاه‌هایی را در داخل خود سوریه ایجاد کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/138106" target="_blank">📅 12:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138105">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وزیر انرژی اسرائیل، الی کوهن:
عربستان سعودی به صلح با کشور اسرائیل بسیار بیشتر از آنکه ما به صلح با عربستان سعودی نیاز داشته باشیم.
🔴
امروزه، همه کشور اسرائیل را به عنوان قدرتمندترین کشور در خاورمیانه می‌بینند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/138105" target="_blank">📅 12:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138103">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/040423a442.mp4?token=UDQupKi4R5YehTsqjk0y6TP6n0Pid0o7dN-n77c0Iaxyb5TlY4PxgXh0y5TN9PZikg73YK8ZVtFF5EXSXuPggrjWp6GJSWa_pij0ZJ4HFzgjyYMbKCbA_XHLNTkeeAdWoBhVlUt3zATMw_jeLi1Le7ISJpNF1z5Fx8Q6FuALELhbnbfaUv-QcaECE0i5i4R2-U0CnIEGQ_yIn2lh33cb35UHDjOaG-yJndxfeA8WMOLGtmalwlvGhCHmnFEJKwvJneV1IWwFHNdc0kf4n9cdiGnQLQFPYeNp-Xss4Yw53NwQqmDQ3EPJU4tYcVq_WvudXQxSYC6Bk0MVlaDB42tAZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/040423a442.mp4?token=UDQupKi4R5YehTsqjk0y6TP6n0Pid0o7dN-n77c0Iaxyb5TlY4PxgXh0y5TN9PZikg73YK8ZVtFF5EXSXuPggrjWp6GJSWa_pij0ZJ4HFzgjyYMbKCbA_XHLNTkeeAdWoBhVlUt3zATMw_jeLi1Le7ISJpNF1z5Fx8Q6FuALELhbnbfaUv-QcaECE0i5i4R2-U0CnIEGQ_yIn2lh33cb35UHDjOaG-yJndxfeA8WMOLGtmalwlvGhCHmnFEJKwvJneV1IWwFHNdc0kf4n9cdiGnQLQFPYeNp-Xss4Yw53NwQqmDQ3EPJU4tYcVq_WvudXQxSYC6Bk0MVlaDB42tAZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از زلزله ۷.۱ ریشتری در ژاپن
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/138103" target="_blank">📅 12:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138102">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
نایب‌رئیس مجلس: افزایش قیمت بنزین منتفی است/ جابه‌جایی سهمیه در دستور کار دولت قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/138102" target="_blank">📅 12:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138101">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
استانداری کرمانشاه اعلام کرد مراکز آموزشی و ادارات این استان، چهارشنبه، ۷ مرداد بخاطر گرمای هوا و مصرف انرژی تعطیل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/138101" target="_blank">📅 12:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138100">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3Y_M-5Pqx_UPKBFrA4vqGc_68v40zJnhe8M8H1dN4N9R-Fql09AgYvyofBBxCnKIyCdQrqiirNdPN9D5A3J3LtT6wXRvlXcqOgq4d9LuCbZnLhxhj6ugfBwedPoiEcCygJ94tozToBzosRGp3YMtv3C2sm0heX-3iNM_0uaysJlTVj8I9Un1cpwPjljELDQxq4iWHghXIt42l968GBWO-9vez8IYsaOQklgD66vpu5hsN8rHU6Sw5MGao4J1CMDkaWMODqHYeCx8H6XHctNiPVPyBkUwFJ79hqZSG4Y_sVgOJdI6q-MmtTsWDoPC8gQalBdkM_ic25UBBgQT6gC1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی، فعال سیاسی: مراقب باشید پاسخِ احتمالی به اوکراین، کل اروپا را همراه با آمریکا علیه ایران بسیج نکند
‏
🔴
به یاد داشته باشیم که ایران خبر اصابت کشتی خود را رسانه‌ای نکرد و این کی‌یف بود که خواست آن را منتشر کند! حال به چه علت؛ درگیر کردن اروپا در جنگ با ایران یا پیوند زدن پرونده «جنگ روسیه_اوکراین» با «جنگ ایران_آمریکا»؟ شرایط پیچیده‌ای است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/138100" target="_blank">📅 12:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138099">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
یک‌چهارم نفت دنیا قطع شد
🔴
براساس گزارش روزنامۀ وال‌استریت ژورنال، حملات نیروهای مسلح یمن به کشتی‌های مرتبط با عربستان در دریای سرخ و تنگۀ باب‌المندب، ریاض را با یک معضل راهبردی جدی مواجه کرده و مسیر جایگزینی که برای دور زدن تنگه هرمز ایجاد کرده بود را نیز با تهدید روبه‌رو ساخته است.
🔴
وال‌استریت ژورنال می‌نویسد اختلال همزمان در دو آبراه استراتژیک تنگه هرمز (۲۰ درصد) و باب‌المندب (۵ درصد)، حدود یک‌چهارم (۲۵ درصد) از عرضۀ نفت خام جهان را مختل کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/138099" target="_blank">📅 12:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138098">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-LCK59m-C5HtecA81gACXJvgL4dj2WjmONulkrJLn2kV99tGwbDoZfra18Q-XvN7cNZqxNUHSN_5dZq_TR45z2jCZnRF7JDjntQOcXNkc1LCCO2f60H3TKPhqF6nns6-7MSBhpWzX3Wuuvzj7WVWIuFvtcZ3uDea0YoWQmxqVXC_9WBw26xLSz5_Xu6pBUJUjqHoMd_Sb5ZxOWurdUy4sdUOXDCdhOzHfuFwE_FP8p3UCAAX6ImbVb-5cqfaVQgIqwDtv8Rz-2Bovoox8KsR6MwzT4OYtgKnAqIEYZ_9dn0f1UVLbQhDfn1FQnQx6vLIPDaRLmNRZoDQdSfa49lig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع روسی: اوکراین تا پاییز امسال توان شلیک موشک بالستیک جدید به مسکو را خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138098" target="_blank">📅 12:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138097">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
صبح امروز جلسه شورای هماهنگی مجلس شورای اسلامی با حضور قالیباف، اعضای هیئت رئیسه و رؤسای کمیسیون‌های تخصصی تشکیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/138097" target="_blank">📅 12:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138093">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d321b0eb.mp4?token=j9-eGtH_mvhrA41FlnyqOVQ7xjUMbeSkO488vAYlTLHtv8aSe7_divK3sDVAAZToX-Gefdd6lpWkTsyKIPTvmqeuqdH_xXTqo7Q4eCEC_KZ-FXpA-7GQa4wnLWWr_1fV55XIvcVSfjebmG25mVHFIo8lUFlSHVcnBYU8KgL6kyLEGM_hoe45Kp510HuspKE9gYpIi3oq-brjHpC8poKPq61y9LFyQbJL4acCCFvqfoW2JmD8sc3p4mNJLeoX2ln9jmEo3CJou2gPZZjxYEXcHG_XGrJ3mlvyYmIM6VzbkDcdo3gYgiLHFrqJ6D6WnvpwPP-xYMedMT-fc5WS57ejFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d321b0eb.mp4?token=j9-eGtH_mvhrA41FlnyqOVQ7xjUMbeSkO488vAYlTLHtv8aSe7_divK3sDVAAZToX-Gefdd6lpWkTsyKIPTvmqeuqdH_xXTqo7Q4eCEC_KZ-FXpA-7GQa4wnLWWr_1fV55XIvcVSfjebmG25mVHFIo8lUFlSHVcnBYU8KgL6kyLEGM_hoe45Kp510HuspKE9gYpIi3oq-brjHpC8poKPq61y9LFyQbJL4acCCFvqfoW2JmD8sc3p4mNJLeoX2ln9jmEo3CJou2gPZZjxYEXcHG_XGrJ3mlvyYmIM6VzbkDcdo3gYgiLHFrqJ6D6WnvpwPP-xYMedMT-fc5WS57ejFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیشب بیش از ۴۰۰ پهپاد اوکراینی مناطقی در مسکو را هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/138093" target="_blank">📅 12:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138092">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رم میزبان مذاکرات جدید لبنان و اسرائیل تحت نظارت آمریکا
🔴
قرار است ظرف روزهای آینده، پایتخت ایتالیا میزبان دور جدیدی از مذاکرات میان لبنان و اسرائیل با نظارت آمریکا برای بررسی عقب‌نشینی اسرائیل و اختلافات مرزی در جنوب لبنان باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/138092" target="_blank">📅 12:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138091">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c84fdbd6c.mp4?token=l0akeusgIbO9Z8QwXMbgvkUfyWLIgkUf-gO4ttMkAhyGu-VewVkTCq5ajkXou85N_yHSvZ2TPYq5SE7XkyQ89M8-sd0LzpPzWyOsf-SWtSw-QPggNXX3VbV2IeS9RRYX1LBsobAl7g8-QqE0ERx-8IZulED2Bv5ecvXi9Mr63ltahcXfGniGEaTqESN-cdVb8vwkvUwWNDoslPcFbBDpy084be_Lxt8jeXKQ6TsAcjzqIwqYlTFJHW2CiFBYgQsC8c2D1s5CWFs53YiTbc-pChmeDt7PTi7QQHnbk0-AZA33rCUSgCasZgnzyMCYoC0Ew6lU7ITp0ZbTNIPHkNMdDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c84fdbd6c.mp4?token=l0akeusgIbO9Z8QwXMbgvkUfyWLIgkUf-gO4ttMkAhyGu-VewVkTCq5ajkXou85N_yHSvZ2TPYq5SE7XkyQ89M8-sd0LzpPzWyOsf-SWtSw-QPggNXX3VbV2IeS9RRYX1LBsobAl7g8-QqE0ERx-8IZulED2Bv5ecvXi9Mr63ltahcXfGniGEaTqESN-cdVb8vwkvUwWNDoslPcFbBDpy084be_Lxt8jeXKQ6TsAcjzqIwqYlTFJHW2CiFBYgQsC8c2D1s5CWFs53YiTbc-pChmeDt7PTi7QQHnbk0-AZA33rCUSgCasZgnzyMCYoC0Ew6lU7ITp0ZbTNIPHkNMdDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهاجرانی: تحریم ما را به سمت تراستی‌ها برد؛ یکی از تالی فسادهای تحریم که به کشور ضربه وارد کرد
🔴
تلاش تیم دیپلماسی ما در امتداد میدان برای رفع تحریم‌هاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/138091" target="_blank">📅 11:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138090">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
مهاجرانی، سخنگوی دولت: هواپیمایی که به‌تازگی خریداری شده بود در فرودگاه بوشهر مورد اصابت موشک قرار گرفت و تنها قسمتی از دم آن باقی ماند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/138090" target="_blank">📅 11:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138089">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2bb5e80a.mp4?token=IqQi2OXTycT-e1PAoIPslj9ilE57AjQ_dP91UyeC8EEnODKFoRAc8bY6g5h1qS4LpZkCn-AEAXaMJeCnWIvbmGkY7frjQc7XJPKb7AgUqAF_rz8q-gAIdFaYloDyLLcNSrDm7V0O-MR0AoWtr_noBwsrp-9gIoK8RWvJXfSTPnFrIT0R7fHxGsPM_YYJd7fs-YohUgIL_B3u3Wz-EWexJEPN3zi5PoiyunMSqr0ixne4CgoxJR7SJdwPowviLbxVrPBfgIOnWXpDEcpzw6q-DuBlJt5nyv37UxleUayAWR9upx4-0H460eK7TtEGTe7RtBTSfGgnUpIgqb1QCM9eXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2bb5e80a.mp4?token=IqQi2OXTycT-e1PAoIPslj9ilE57AjQ_dP91UyeC8EEnODKFoRAc8bY6g5h1qS4LpZkCn-AEAXaMJeCnWIvbmGkY7frjQc7XJPKb7AgUqAF_rz8q-gAIdFaYloDyLLcNSrDm7V0O-MR0AoWtr_noBwsrp-9gIoK8RWvJXfSTPnFrIT0R7fHxGsPM_YYJd7fs-YohUgIL_B3u3Wz-EWexJEPN3zi5PoiyunMSqr0ixne4CgoxJR7SJdwPowviLbxVrPBfgIOnWXpDEcpzw6q-DuBlJt5nyv37UxleUayAWR9upx4-0H460eK7TtEGTe7RtBTSfGgnUpIgqb1QCM9eXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کپلر: طبق داده های مسیر یابی تردد کشتی‌ها از تنگه باب المندب در روز دوشنبه به 28 کشتی افزایش یافته که بالاترین سطح در چهار روز گذشته است، در حالی که تردد از تنگه هرمز همچنان پایین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138089" target="_blank">📅 11:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138088">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
الجزیره به نقل از رسانه‌های آمریکایی و انگلیسی: سفر فعلی نتانیاهو به آمریکا، حساس‌ترین سفر از زمان آغاز جنگ علیه ایران است
🔴
ممکن است که تل‌آویو در جریان این سفر، خود را ملزم به ارائه امتیازاتی در چندین پرونده منطقه‌ای بداند
🔴
اولویت‌های ترامپ و نتانیاهو دیگر به اندازه ابتدای جنگ، با یکدیگر هم‌خوانی ندارد
🔴
بزرگترین چالش پیش روی نخست‌وزیر اسرائیل، تغییر عمیقی است که در نگاه آمریکایی‌ها به اسرائیل ایجاد شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/138088" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138087">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
رویترز: عمان سازوکار جدیدی برای مدیریت هرمز پیشنهاد داده است
🔴
رویترز به نقل از یک منبع خلیج فارس مدعی شد: عمان پیشنهادی برای سازوکار منطقه‌ای مشترک برای مدیریت تنگه هرمز با هزینه‌های داوطلبانه به ایران ارائه کرده است.
🔴
براساس این پیشنهاد، ایران به تنهایی کنترل آبراه حیاتی را اعمال نخواهد کرد.
🔴
این پیشنهاد برگرفته از تنگه مالاکاست؛ کسانی که از این تنگه استفاده می‌کنند داوطلبانه به ناوبری، حفاظت از محیط زیست، جستجو و نجات کمک می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/138087" target="_blank">📅 11:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138086">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
مهاجرانی: مرکز هواشناسی بوشهر چیزی از آن باقی نمانده است
🔴
کسب‌وکار های گردشگری به شدت آسیب دیدند
🔴
فرودگاه بوشهر به هیچ عنوان قابل استفاده نیست و باید از اول ساخته بشود
🔴
۱۲ دستگاه پل و ۲ دستگاه تونل آسیب دیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/138086" target="_blank">📅 11:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138085">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
کانال 12 اسرائیلی در پوشش خبرهای سفر نتانیاهو به آمریکا، از برنامه ویژه تیم او برای اعلام خطوط قرمز اسرائیلی در قبال مذاکرات با ایران خبر داده است.
🔴
در این گزارش ادعا شده است که یکی از ابتدایی‌ترین خطوط قرمز، وجود هر گونه اورانیوم غنی‌شده در ایران است.
🔴
ارتش اسرائیلی به آماده‌باش جنگی سطح قبل از درگیری درآمده است.
🔴
کارشناسان اسرائیلی، ادعای نگرانی از کمبود و مشکلات ذخایر موشک‌های سیستم‌های دفاع هوایی در منطقه برای توجیه توقف حملات آمریکا را مضحک می‌دانند و از چنین کمبودی بی اطلاع و از ادعای درباره آن شگفت‌زده هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/138085" target="_blank">📅 11:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138084">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
روزنامه «نیویورک‌پست» گزارش داد، بنیامین نتانیاهو در جریان سفر به واشینگتن قرار است اطلاعات و ارزیابی‌های امنیتی مربوط به سایت ایرانی «کوه کلنگ» را به دونالد ترامپ ارائه کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/138084" target="_blank">📅 11:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138082">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/oHgfExZehoAdmroZmudyv8gfplerZXG__INEftx4KUD0XW_4vEhREgtMdVY6Vxyk7nhOt9fEWE8yM7jt2MbdUMWLIibe2F9XlY3q2os2PNkGt2UH05MgjmNWa4b24PQRCVZnaauudvXyeULlmULfVkdyUbalhLYTYuGBxo68n2RZJXq4M4p0bhhHw_eTVMZleW_xlHNYVrBHkmSvpONQd6qpEvP12oi5K_HS_Y56IMEya_EF4eh2j4AR8lRBnGiG-4Zw9bSRq8bC5miMx4f0dSGqL3iArIXpaCvMITT6jOPYdolVCr4aLAHf4eeETrGuo6SZkoCA6WsF8bLJbg_ylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/IN3aqCkIbRnl1am7Oiyq-LPKhs_3d34SxeV-KNNVMkXTYVAG2vhL4KU8RjcgwACEq_XM3tLBWBDSKbc90prqrLcE7ygIusqvFAx9oGRF680KsszGiu0gtLATogA33VcRgOl3ZFY3Pz3Eq1dpSl1qd9V_GCpwLX857HebUldR8IPucya8PhNsluYwMOZ_Ipr9qAylBa1TNgOEbQTMP-rsRuU7fdnSQ5sIgnIL02oOLq4VfEB1Srvb_NMehKz4ZZD31WPC6hYbWzI5_GwTr8PQzm5vjH17t3l7ogetS4mZjw_oWT_dqse9_zWKuC7Py8t2RIIFo6RVEIZoLfuHpf-Yog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
فووری: کریستیانو رونالدو قراره به عنوان تهیه کننده و بازیگر وارد دنیای سریال‌ها بشه!
طبق گزارش‌ها، رونالدو توی سریال فوتبالی «
Day 1s
» که با همکاری «
متیو وان
»، کارگردان فیلم‌های Kingsman ساخته می‌شه، حضور داره.
داستان این سریال درباره زندگی یه ایجنت معروف فوتباله و «
دیمین لوئیس
»، بازیگر سرشناس انگلیسی و ستاره سریال‌های "Homeland و "Billions"، نقش اصلی اون رو بازی می‌کنه.
«
تیری آنری
» و رپر معروف «
Dave
» هم قراره توی این پروژه حضور داشته باشن.
جالب اینجاست که خود کریستیانو رونالدو هم علاوه بر
تهیه‌کنندگی
، قراره توی این سریال
نقش‌آفرینی
کنه.
فیلم‌ برداری این سریال هم الان توی لندن در حال انجامه و قراره به زودی منتشر بشه.
@AloSport</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/138082" target="_blank">📅 11:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138081">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab6c540c9.mp4?token=E4FxLigNOsyu0dTSSVmxhioMETk5Gsg06dzRPny6dZk_aanNI3Q0TOCtFxY1RZSq45ZKY4b2rEKqWPnDOo180GmSuEuh1MKRQzf8JlQ73ze9UV1MedmFwAsuDEOktf3sb_IG11ABC1fBWXB8U3VyzG2lqV2onc4Gfih4ELnI8Pe6NC3LGYbc7g1ONiLYWhXzxTX4G2NGtKAA-f_jREwWQ0dg6y0k0xJf6PV9qB_bhpOvOhVMvRowmPBomgMftXnxsyMC1UQyFNniZfO8X9xssQBBT4SB59eamWjOXBdUk-J-TRBaZqj8UaJKSFOSF3M1khgurulfC_qsJM27d8BBvTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab6c540c9.mp4?token=E4FxLigNOsyu0dTSSVmxhioMETk5Gsg06dzRPny6dZk_aanNI3Q0TOCtFxY1RZSq45ZKY4b2rEKqWPnDOo180GmSuEuh1MKRQzf8JlQ73ze9UV1MedmFwAsuDEOktf3sb_IG11ABC1fBWXB8U3VyzG2lqV2onc4Gfih4ELnI8Pe6NC3LGYbc7g1ONiLYWhXzxTX4G2NGtKAA-f_jREwWQ0dg6y0k0xJf6PV9qB_bhpOvOhVMvRowmPBomgMftXnxsyMC1UQyFNniZfO8X9xssQBBT4SB59eamWjOXBdUk-J-TRBaZqj8UaJKSFOSF3M1khgurulfC_qsJM27d8BBvTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بهمن ننگین 57 حمله عنقلابیون به پادگان ارتش و سوزاندن سربازان و کشتن افسران ارتش.
🔴
اونموقع این اغتشاش نبود؟ اموال عمومی نبود؟
🤔
از شما حرام زاده های عرزشی دروغگو به عنوان بیناموس هایی تو تاریخ یاد میشه که حشدالشعبی، فاطمیون، حزب الله، حماس رو به وطنتون راه دادید تا به ناموستون رسیدگی کنن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/138081" target="_blank">📅 11:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138080">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ادعای «العربی الجدید» به نقل از منبع آگاه ایرانی:
🔴
تحرکات دیپلماتیک برای کاهش تنش در منطقه و دستیابی به راه‌حل دیپلماتیک در روزهای اخیر شتاب بیشتری گرفته است.
🔴
در دو هفته گذشته، پیشنهادهایی از سوی میانجی‌ها بین دو طرف مبادله شده، اما هنوز به پیشرفت چشمگیری منجر نشده است.
🔴
تبادل پیام‌ها بین تهران و واشنگتن به طور مستمر و بدون وقفه و از طریق بیش از یک کانال ادامه دارد.
🔴
تهران به واشنگتن ابلاغ کرده است که پیش از پایان محاصره دریایی آمریکا و بازگشت این کشور به اجرای تعهداتش، اقدامی برای بازگشایی تنگه هرمز انجام نخواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/138080" target="_blank">📅 11:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138079">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDav6z6yjlNuyxjhXnk-KZmoTE-bGjft6rzbc_V2uOlRs93Gp9yD44y7ahfwV2t5lOV8PcipAlXis7nvAk4K1Ka_B9hevuubcCLGCp05076Trt0uqO6r3DtCLiLX5rREivnrgUvKcDaqx8RRYbYG9ooLWWXMKDsIsEYLaBTrXMB4CvwvlAhWqKoB2TnqDsQu3jcLrjjkAoa8WNLcLF2RBclmwyMWtLiEbOk5nKa6YKYXfpCOtw5ugo_hqNH7aGxrjjJjwJts77s_JaRYn27fZzgb3UcVfYGl0OS44Strwpa97bGmsXObVyvo-XGi7DOmkz9vcJbbXNsMy3dCNkE3Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وقوع زلزله۷.۱ ریشتری در ژاپن
🔴
زمین لرزه ای به بزرگی ۷.۱ ریشتر جزیره کیوشو در ژاپن را لرزاند.
🔴
در این رابطه هشدار سونامی صادر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/138079" target="_blank">📅 11:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138077">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lugvtxXj_ShWxV3Wm13HHg3aFzgHyNp2QobaivrFbksJXBKLNo23OnWQjA6LHWw5m2yWl4XUu-ny580bBfCkMa0wQHYewQHmUNNOXfbqf8s8QecU9GhzJNNAzcwmToAoTowmNXQ3RrkfLL9S10zu0vyTEl96d2DF0nd5l2MB9q5RY6w1NFRYtbYAvOY79o8sGogLDbkVIUTiC_pSBtR6Gv-x7mTXIzICeJiEAtr9eAkItHTWTvcPmOHs-zkt35HqCCqYRzFw-7HyookF_ycLKlu70A0DVNmfqYUMABnayxtRwj2wAtwjxrk6l8PX6nZ2XrroVK6-wWNcsBznShpquA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbT25RmYEnNEBxxsUpTDmsLN5a1oLhkZLk8LEeNamRIxWqZL4oLS0MTf7XcxJID5Jga403YAEailDsY3J7ymOzqqe60Sdvb9DFUsdl303qHZjkLOBsQmm2PJ1yCtv_TtpcWSCXLlp2M0HS3RUGHhuginQ_CmZtM5DGsTUSa5N6sPkvYonjj5n0pwiXWb-3nx5WoAqWpkAX9PQln35Cn93nzAEu-W3tnnjZ-8j3fqKxl5Fu0oMqblJ0oh8wb_2bWU9hbx7MzF4wGI7M51k2v11JBn_PzV-zrVN6_gRb2DB6RQrS4ipw-Hy9oFSjN2lIwneRfgdsFdxafOuBQn9ffkSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تو‌ جلدی که مجله اکونومیست از سال 2026 منتشر کرده بود؛ زلنسکی درحالی که دوربین دستشه، داره به یه کشتی ایرانی نگاه میکنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/138077" target="_blank">📅 11:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138076">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3de200d8a.mp4?token=Uli2phxHrlVNwHFIch-c4wHR8CG2mV8hW0NHeNoaD8KdU0o-f0dLW0gf7ZD7yhBkcF5e54uLXgL8CxtN3Ekld86vpHKhypnUH9SaZ__v1ksSnVFBsp5aDpvPxsh59Rjga26vyFnHzuPx3ttCf7ZWlu4obDY6hke2tgaknb1ROYas8zdM7BVwNjA-By94JTRqSUbYJLOr9x92PFQZ_IelyO0Me4GnrH6kttSXcnjAo6Yartc1Cgyrcn_kLZ1xt6h_9IDogpLnqW13r08SNSEy4KYsK7-arRIJTA7CssA8vwtC9UrowhwwguS7jLc2w1EWx08Y3cgCKQqUY0u9av1bYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3de200d8a.mp4?token=Uli2phxHrlVNwHFIch-c4wHR8CG2mV8hW0NHeNoaD8KdU0o-f0dLW0gf7ZD7yhBkcF5e54uLXgL8CxtN3Ekld86vpHKhypnUH9SaZ__v1ksSnVFBsp5aDpvPxsh59Rjga26vyFnHzuPx3ttCf7ZWlu4obDY6hke2tgaknb1ROYas8zdM7BVwNjA-By94JTRqSUbYJLOr9x92PFQZ_IelyO0Me4GnrH6kttSXcnjAo6Yartc1Cgyrcn_kLZ1xt6h_9IDogpLnqW13r08SNSEy4KYsK7-arRIJTA7CssA8vwtC9UrowhwwguS7jLc2w1EWx08Y3cgCKQqUY0u9av1bYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برشی از یک مناظره/جمهوری اسلامی تنها با زور اسلحه و کشتار باقی مانده
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/138076" target="_blank">📅 11:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138075">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=e8P_qhjY8V2O45doXp3XJ4VkrREogNUN3mwqcBVUCxiQ-ORUHSDxu2vVnpe0Apwqo4WVd727azWcrfpckNjqnAycgqnLz-2AZ5LbVsSHOBFKYb22ALWR3cQuoyFLr4jI7tSBcIs5j-bZ7ADWK8zB5-KKbKjSfT0nGo7AyM0vwTIufQQPupXgg5gOi-vlelU6Mi_MMXNh78CBwrF-1jPEkuAE3bfQwgjuwF3giLufZ456BlCXNtocaK4jnTom6TtnnzXtgL9c-T-y5UMV3MYfwTJ8LYHrvhlZeiaaLNJQAvWY9Fkv_LdzjyI2iLzpYr_NBrTp-d_oBXavkjVpV_w4nztwMmUXvV-o0aiiGDncAM9EImTsI0KapQglUrIDVEpYAGrBmNrma3qD6m_JXAJg_ZAFcVyQQh2vCLI3GUq5DKLOMmPi7kL03ZlH8PJgQ7Tw921_cVR1jJiuRODsGt8eXTDa_FdcUOIDX0--9uTW_Hwh8ujp83VZSKGTQssQGSbhJlzJOjlAFDqbdGfory34Yric5UeeAFoQLyIjhMV_EuVQlmnUAuCqM6Wfjnoof1vhhKYEfDvMxdgzVO4rCL3CUE07FdB4Rqw9hp-8gubv1Na4ptfxYXwtVLcVT-aztGkJOtvLG2C_Br9FSyfkMhmgoNuLwa1ofeUllz5ypQyMHP0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=e8P_qhjY8V2O45doXp3XJ4VkrREogNUN3mwqcBVUCxiQ-ORUHSDxu2vVnpe0Apwqo4WVd727azWcrfpckNjqnAycgqnLz-2AZ5LbVsSHOBFKYb22ALWR3cQuoyFLr4jI7tSBcIs5j-bZ7ADWK8zB5-KKbKjSfT0nGo7AyM0vwTIufQQPupXgg5gOi-vlelU6Mi_MMXNh78CBwrF-1jPEkuAE3bfQwgjuwF3giLufZ456BlCXNtocaK4jnTom6TtnnzXtgL9c-T-y5UMV3MYfwTJ8LYHrvhlZeiaaLNJQAvWY9Fkv_LdzjyI2iLzpYr_NBrTp-d_oBXavkjVpV_w4nztwMmUXvV-o0aiiGDncAM9EImTsI0KapQglUrIDVEpYAGrBmNrma3qD6m_JXAJg_ZAFcVyQQh2vCLI3GUq5DKLOMmPi7kL03ZlH8PJgQ7Tw921_cVR1jJiuRODsGt8eXTDa_FdcUOIDX0--9uTW_Hwh8ujp83VZSKGTQssQGSbhJlzJOjlAFDqbdGfory34Yric5UeeAFoQLyIjhMV_EuVQlmnUAuCqM6Wfjnoof1vhhKYEfDvMxdgzVO4rCL3CUE07FdB4Rqw9hp-8gubv1Na4ptfxYXwtVLcVT-aztGkJOtvLG2C_Br9FSyfkMhmgoNuLwa1ofeUllz5ypQyMHP0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرگزاری تسنیم روز دوشنبه با انتشار ویدیویی حاوی اطلاعاتی درباره فروشگاه‌های مورد علاقه ملانیا ترامپ، از کسانی که آن‌ها را «آزادی‌خواهان جهان» نامید، خواست بانوی اول ایالات متحده را هنگام مراجعه به این فروشگاه‌ها به قتل برسانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/138075" target="_blank">📅 11:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138074">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dec70a1e2.mp4?token=vJYFJhOp5FX2suVy0sYOqKJUpE5w_1w70ZYmZE7i7gTVLP9QnVKeiTtcWMcVh6E1BybQbiwJ-Fn0NgPKVI2zy4FqluNoQIi1Gv7BR3KXFNTZEiwtj0B27Oa4RDcZOmzLkwnJvNBr7SqsGdxBTEONqOcf9QzoCCuf28LnSALhQu0coGmXNzwa4C_sXnXWNAWgRM4tRbMWRf6WUnCxnmeNbnShzLxMhYKnHlO0xs6nxoJuCbtAsmvnoKooNA9QCtYWWEB_aP8JUDcgy4eSS0FtQDhO9UzpiGnbvIzmsSvQWaXrUxXIwbq1yFsv1xp1Sbx2V8yi9JaEjR39ij5r9tGoqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dec70a1e2.mp4?token=vJYFJhOp5FX2suVy0sYOqKJUpE5w_1w70ZYmZE7i7gTVLP9QnVKeiTtcWMcVh6E1BybQbiwJ-Fn0NgPKVI2zy4FqluNoQIi1Gv7BR3KXFNTZEiwtj0B27Oa4RDcZOmzLkwnJvNBr7SqsGdxBTEONqOcf9QzoCCuf28LnSALhQu0coGmXNzwa4C_sXnXWNAWgRM4tRbMWRf6WUnCxnmeNbnShzLxMhYKnHlO0xs6nxoJuCbtAsmvnoKooNA9QCtYWWEB_aP8JUDcgy4eSS0FtQDhO9UzpiGnbvIzmsSvQWaXrUxXIwbq1yFsv1xp1Sbx2V8yi9JaEjR39ij5r9tGoqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بدون شرح از یک حجری
🔴
پ.ن: راهکار ساده هست زن سیبیلو نگیرید تا با دیدن اشخاص دیگه مشکل براتون پیش نیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/138074" target="_blank">📅 11:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138073">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
توهین‌های داماد دوزاری علیرضا پناهیان به آیت الله سیستانی مرجع اعلم شیعیان جهان!
🔴
پ.ن: آیت الله سیستانی بزرگترین مرجع ۲ دهه اخیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/138073" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138072">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVPJNGT-QuQsCOwUP__oe_EKEF7gMr65DfD0drgf8DyuhpE8INVJHh8aEnej9F-Dr3oc-jIyAl7E6o0JGUIRQKolsj1HldACT7RbpxJ9Y1XMRK0RWllnwtEmOvIUhhWCjb7jUhn3qePQo69moVACElpU2T-xsPfWm6aZzurCbknAd7OA0DIn252SlZKA6FOsWBRDdHK6tHXefpJY6EAdUS_6f9PbLKpTsZ6o2wU5KsUtTAylod3aKYHilN4Olxa2kMSHB-2nLkutRBwMb6KE4KQfXAk2j4kt9UCa5oaS_e_0yxVSUXti4m0ptYX_-1VoRHMZE_lZW3XE1-ypNwjl6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل به جنوب لبنان حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/138072" target="_blank">📅 11:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138071">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a635b8a91.mp4?token=YD54F59RHw5o7pI9CECdeqYw82haPyfeu43YynoWrG0PEw1mbI095A0DVcruxl1eSwyL1JUS62vBBx88tujqb93RuZmF_d6KdEwfjwULnxIBGpCB0fxV2kMlDMvuwZCYE0ycUL8AnVB5N3NvNK4bd-6d6xiobGCtzstxYslLDKHnwQvm6f0gExmvaVPTgyV5ZIEPo9Iahn1z43MaiFdxWeX_Ps47qi74NmLVi_DaF1nSVtbMPO5MracAlaTOQfNSFvo9iB1gPJEwgjQP1HXfNVgOU7om0GCyJlZ6mwAnNypcFgSiBML_iR-by1RG6gj3k0R74mor-BFRtzW5QgUs2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a635b8a91.mp4?token=YD54F59RHw5o7pI9CECdeqYw82haPyfeu43YynoWrG0PEw1mbI095A0DVcruxl1eSwyL1JUS62vBBx88tujqb93RuZmF_d6KdEwfjwULnxIBGpCB0fxV2kMlDMvuwZCYE0ycUL8AnVB5N3NvNK4bd-6d6xiobGCtzstxYslLDKHnwQvm6f0gExmvaVPTgyV5ZIEPo9Iahn1z43MaiFdxWeX_Ps47qi74NmLVi_DaF1nSVtbMPO5MracAlaTOQfNSFvo9iB1gPJEwgjQP1HXfNVgOU7om0GCyJlZ6mwAnNypcFgSiBML_iR-by1RG6gj3k0R74mor-BFRtzW5QgUs2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی دولت: قیمت بنزین سهمیه‌ای تغییر نمی‌کند/ هیچ تصمیمی برای افزایش قیمت بنزین غیرسهمیه‌ای اتخاذ نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/138071" target="_blank">📅 10:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138070">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PH2BVJysmsbbn1n0-JVRu3EmjesJAgreF1SmyxzBOXVParSwcFjUZdOSl4TkYnEKbYivs4Q10P4zsbss4xQuboLyCAsfSIrM6le34hvvb1t_pt4e6gDWvDprlUEe1qreXTdsKLgPC4O2ZNY9FtyBlTM8lBk13DTkGzwcABRbSVMxV56wdSxv8A7tyhEppw8WpdP09VSR-HH2hsKG7i-b_jL0i5wTh3hA67OqDk9EgZinLr_q8vm5721NtDVmiZqAyVu_4RzPGBbNl2fh013BKv_J4BWrXW5WKyNkaBauOancy0yDmnjK2TQafS0ZNHobyFzaIkm680S6AoXmNmSvTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احتمال یک آتش بس پایدار با ایران تا پایان ماه جولای ( تا یکشنبه هفته بعد) با یک جهش بزرگ در پلی مارکت به ۵۵ درصد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/138070" target="_blank">📅 10:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138069">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سخنگوی دولت: فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138069" target="_blank">📅 10:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138068">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
فعال‌سازی سامانه‌های پدافند هوایی در نزدیکی پالایشگاه‌های نفتی بقیق در عربستان سعودی، به دلیل حمله با پهپادها
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/138068" target="_blank">📅 10:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138067">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
حزب‌الله: با حمایت ایران، لبنان رو آزاد می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/138067" target="_blank">📅 10:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138066">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAZ4MWcrdP9_SQFAXYh6b58NArK7hlIqxaNR_9gMX9YTpLqvvDuFfyEqlnZZ42dwLeT1WZQ4r31NCgAPNeKMshCZhWFut_OYzpA49vJX_7_lWmSCI0MtEixnremZ4bpSJhii2GKM0MbNc1UuSffP3NVTCYrj7AfkrtkeaqC9ZGK0snACyl6v_l9O6EK8y0Wk353OfqcA5o1JdVd80LochtXmSsjhx3UXQP8GzzPovXZlodvRgRX__kauKUU8BExypl25GmgdE1PH8KBKTDW3tePFb0l9gEmuqFeYB8w6iXIGESbUTVtc-bB6NOKmXE6oNdo7krHMmT5Ivbbwc7WEYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پوتین: شناورهای تندروی ایران در درگیری با آمریکا عملکردی موثر داشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/138066" target="_blank">📅 10:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138065">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoXl88anJ2_41iAn0omqETNcsSpZ0l5WKBbOg4k-pdgD8EJyg1WJKlvJE2GPikWJFRK8Rgb4y3Wx8TzOtwWNVBmzOSKIxhja-sIDFPxozjX-rS-H9Wa6DHfmYV1-kIRURx3B7sd2QtS-HklDH-tAHLa-GfA7LDncdxcvxnTurNnh_yrdqERGedkQr6iJDl7gNuFTf-jrjejzDiCiSLuFx52arz6hqU_Tzc5Qt3ue5TtC1FF0aJclnlN0-gyNa9x1jjYs6GNrOkWIz8USijnTE_f9x85psVpFdamEi3PFjQ52HnancfVVeOVrGt1guzRFrT2ZIvHq3RpudvZ9DlY1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش مارک لوین به اعدام و سرکوب مردم در اصفهان:
🔴
با این نازی‌ها مذاکره نکنید. مردم رو مسلح کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/138065" target="_blank">📅 10:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138064">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
فرمانداری امیریه : دلیل انفجارهای امروز امیدیه انهدام مهمات عمل نکرده‌است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138064" target="_blank">📅 10:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138063">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سفیر ایران در روسیه با اشاره به هماهنگی مستمر تهران و مسکو در حوزه‌های امنیتی و دفاعی، از تداوم تماس میان نهادهای مسئول دو کشور درباره حمله اوکراین به یک کشتی تجاری ایرانی در دریای خزر خبر داد و بر ادامه همکاری‌های راهبردی ایران و روسیه تأکید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/138063" target="_blank">📅 10:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138062">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وال استریت ژورنال: هدف از مذاکرات ایران و عمان، توافق بر سر مسیری در تنگه هرمز است که کشتی‌ها بتوانند از آن عبور کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138062" target="_blank">📅 10:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138061">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
همشهری: ۱۵۵ نماینده در نامه‌ای خواستار اجرای قانون برای جلوگیری از رشد بی حجابی شدند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/138061" target="_blank">📅 10:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138060">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0pbJAorLBafTU-C61JHis27iQAmRVWRrj0EpD1Mh22qJr7Yka5Vh0Wy8JsY39AlO477TRWyt6mOYp6mUEQ_MnbyWmmvPzwiHKZz8h7SdM-tJ4G-iy5oks9TV1KUqQ2ACy0wpjJGBfNlzw-_YpTW3vvi39f5qugy_nZL69zv4Tx_wAeyOxqhB2rQOxMKJ4MDHXw__Ib664HmrL_I80qvII-ohUqQ690sixqWqSUmm6CbTYlj7_3VgRK-zKGG_DlNtZsuSgx00dhh8kVq1L3Wmglz-TGpCKZzviEcvxxaFMZWb--9wpitXhz47KpvTJAzjK_cCy2O4nnLqFyPNZgqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش وال استریت ژورنال: دونالد ترامپ، رئیس جمهور آمریکا به طور فزاینده‌ای در مورد چشم‌انداز اوکراین در جنگ علیه روسیه خوش‌بین شده است در حالی که پیش از این به مدت بیش از یک
سال به مشاوران خود گفته بود که کی‌یف در این جنگ شکست خواهد خورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138060" target="_blank">📅 09:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138059">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک مقام ارشد کاخ سفید گزارش داد که دونالد ترامپ امروز میزبان بنیامین نتانیاهو خواهد بود و دو طرف درباره جنگ با ایران گفت‌وگو خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138059" target="_blank">📅 09:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138058">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
کیهان: صحبت از «مذاکره» و «حل بحران از طریق گفت‌و‌گو»، اگر خوش‌خیالی نباشد، ساده‌اندیشی محض است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138058" target="_blank">📅 09:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138057">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وال استریت ژورنال: مرگ لیندسی گراهام و مشکلات جدید اسرائیل
🔴
مرگ لیندسی گراهام، اسرائیل را با مشکلی بزرگ‌تری در آمریکا مواجه می‌کند، زیرا واسطه‌ ماهری مانند او، به هموار کردن اختلافات ترامپ و نتانیاهو درباره ایران کمک می‌کرد.
🔴
جایگاه اسرائیل در میان دموکرات‌ها و جمهوری‌خواهان در حال افول است و دیگر کسی مانند لیندسی گراهام با آن وزن سیاسی که دوست نادر اسرائیل باشد، وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138057" target="_blank">📅 09:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138056">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KyFHCPKU6-mib0tN1ooLHY2I2mgtZC2yudN9bBE3KspgjE86V4cvHNNoFbHzNBlOZlMIB_fGevsc1UC28YQx3Urayw-vRVH5VNMFz_pCelgpVo5_JpFZ_7Y8jsj8mMsSYuXBKFMLEGrXmtAURBjPzIafwbZM628LP_YTx0dv-2JeKh7Yuyjo18nxrmHo81ZfQjqVCGBNyJAMujlFnS45c2L9Kvrq5FWSRQnHWBV0og4SyldpZiA8_iZUG47mxNrp4JW3ltjq1GntCgiJs0PkXEtfpGH4cKSaqikfUAg0EyAuJ2a9LNgeu6EszI5rfBv7DoMgtiU97XVbTFUhh25kPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اداره برق به جز اینکه برق رو قطع میکنه؛ یه اپلیکیشنم طراحی کرده که پول میگیره قطعی برق رو بهت اطلاع میده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138056" target="_blank">📅 09:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138055">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وال استریت ژورنال: هدف از مذاکرات ایران و عمان، توافق بر سر مسیری در تنگه هرمز است که کشتی‌ها بتوانند از آن عبور کنند
🔴
مسقط پیشنهاد ایجاد یک کنسرسیوم منطقه‌ای برای تنگه را مطرح کرده که بر امنیت دریایی و سایر همکاری‌ها نظارت دارد
🔴
این پیشنهاد شامل تأمین مالی داوطلبانه از سوی کشورهای منطقه و صنایع کشتیرانی و نفت است
🔴
آمریکا به طور مستقیم در این مذاکرات شرکت ندارد، اما عمان این کشور را در جریان می‌گذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138055" target="_blank">📅 09:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138054">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
صادرات قند هم آزاد شد
🔴
سازمان توسعه تجارت در نامه‌ای به گمرک با صادرات قند به‌صورت مشروط موافقت کرد.
🔴
۳ روز پیش نیز وزارت صمت ممنوعیت صادرات ۱۵ قلم کالای کشاورزی از جمله کشمش را لغو کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138054" target="_blank">📅 09:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138053">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ارتش اردن اعلام کرد که یک پهپاد را که وارد فضای کشور شده بود، سرنگون کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138053" target="_blank">📅 09:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138052">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=spKi-jsYejbBzQiF8mK1Y4uyGwJmPCQgBsBNu7VOeojBHJMtyiLPg4yEMXENyyKAHmoVzMbJ3Z8mP0LHkGHMpxkm3xJyLwAlHacl74mIRnJNFl-9GkisW4rjPvZFMcY8Xlb9arQqiJ89JR-ju9MebEXiqrZgQxXTJX6rGIK-NG1HI9sEvJ8hOAAPUPDvY2or9iwIO65RatWl3P0Y_Y6AmqjLMcVmvTKQWDlH-elAFwL3JqnijViBoHdgXeEKFgB6tpyDUlXTEdJR2ldCsuUtijvrk8gj_9SeXdsFgfY-VEdY8x0M0Kf4ZIRcejsc-OhdzypQiFdKhImZWb2n6sUeaRTA-On5hywBuU6IvzX0GWm3mbu6URLnGTvlPybvjhMrWylO2JT_AtHG23olyDaCW7HfGqGJhHtlLNQIQUrLGiwmAx9x34sIv-IMUG8uUnbY6O1jN10x1aVo_9e7oKL7t75ERFzZP-VVNCTeigcSxMLFqQ5XpXwb9ZuvwyFlkvsHfWpPh13O0vgQwaaHXadWCgCZnAt4HcFZaf1OC9ybF93icIApsGwuwMM84zeftJRP4h2RoPcIAyaWuFBUEyCw_Ajz3w6Dsia4eEk8EopaFHefE_p8pW3s7pTkmbMT-8aF4jFm86bojTYgkItH7FbY-4BgE6kg2tmwNtW4la-hwwk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=spKi-jsYejbBzQiF8mK1Y4uyGwJmPCQgBsBNu7VOeojBHJMtyiLPg4yEMXENyyKAHmoVzMbJ3Z8mP0LHkGHMpxkm3xJyLwAlHacl74mIRnJNFl-9GkisW4rjPvZFMcY8Xlb9arQqiJ89JR-ju9MebEXiqrZgQxXTJX6rGIK-NG1HI9sEvJ8hOAAPUPDvY2or9iwIO65RatWl3P0Y_Y6AmqjLMcVmvTKQWDlH-elAFwL3JqnijViBoHdgXeEKFgB6tpyDUlXTEdJR2ldCsuUtijvrk8gj_9SeXdsFgfY-VEdY8x0M0Kf4ZIRcejsc-OhdzypQiFdKhImZWb2n6sUeaRTA-On5hywBuU6IvzX0GWm3mbu6URLnGTvlPybvjhMrWylO2JT_AtHG23olyDaCW7HfGqGJhHtlLNQIQUrLGiwmAx9x34sIv-IMUG8uUnbY6O1jN10x1aVo_9e7oKL7t75ERFzZP-VVNCTeigcSxMLFqQ5XpXwb9ZuvwyFlkvsHfWpPh13O0vgQwaaHXadWCgCZnAt4HcFZaf1OC9ybF93icIApsGwuwMM84zeftJRP4h2RoPcIAyaWuFBUEyCw_Ajz3w6Dsia4eEk8EopaFHefE_p8pW3s7pTkmbMT-8aF4jFm86bojTYgkItH7FbY-4BgE6kg2tmwNtW4la-hwwk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش تند چند آخوند به حسن روحانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138052" target="_blank">📅 09:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138051">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوری /  صداى 6 انفجار در نزدیکی‌ تأسیسات نفت و گاز واقع در منطقه شرقی عربستان سعودى شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/138051" target="_blank">📅 08:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138050">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
گزارش ها از برگزاری یک رزمایش نظامی بسیار بزرگ و بدون اطلاع قبلی که به صورت بی سابقه توسط تمام کشور های عرب متحد آمریکا در خاورمیانه و آمریکا در خلیج فارس طی ساعات آینده خبر می‌دهند.
🔴
یک نوتام( منطقه پرواز ممنوع) برای بخش بزرگی از خلیج فارس صادر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138050" target="_blank">📅 08:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138049">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
با اعلام خبرگزاری فارس، حکم اعدام هر ۳ نفر اجرا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138049" target="_blank">📅 08:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138048">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
المانیتور به نقل از منابع آگاه: وضعیت عجیب است؛ ترامپ می‌تواند جنگ با ایران را از سر بگیرد، اما نمی‌خواهد؛ نتانیاهو می‌خواهد، اما نمی‌تواند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/138048" target="_blank">📅 08:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138047">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از مقامات آمریکایی و میانجیگران: ایالات متحده با چالش محدودیت موجودی موشک‌های رهگیر پدافند هوایی مواجه است، در حالی که ایران همچنان زرادخانه عظیمی از موشک‌های بالستیک و پهپادها را در اختیار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/138047" target="_blank">📅 08:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138046">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
جو شدید امنیتی در میدان علیخانی اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/138046" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138045">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2b428aa9.mp4?token=k9GHbCQLrOzIDePa6FOM1lGWmLvHb05O500sGPadvYzTBcQriMv-1SuGoYEeIBVjaXmkNb0CT7Gyi4Ao7-llHvyCdSIh2e_GwkiQxtdyaxvb7plcYmXTz8jfdjAtV1WPSQk2GYpy4cpyAlikgQtUY8L0a4XgDDiC6O4nSsPytOP3ycUa7DzQAK-MH2f27c9ESqHG4K-As3yiPZwNdnL-jntjUA3rQxi18oFZZ_FSXoVsl86JUyUwf9rR1TybajEmiqJM15-6ZryCfwSTQo7zdNAAUWLe5pTPh2fep86WlWypJ9nLB_Yp1NJuzajrhE1vg7B1VaHSphbaa87hFObXAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2b428aa9.mp4?token=k9GHbCQLrOzIDePa6FOM1lGWmLvHb05O500sGPadvYzTBcQriMv-1SuGoYEeIBVjaXmkNb0CT7Gyi4Ao7-llHvyCdSIh2e_GwkiQxtdyaxvb7plcYmXTz8jfdjAtV1WPSQk2GYpy4cpyAlikgQtUY8L0a4XgDDiC6O4nSsPytOP3ycUa7DzQAK-MH2f27c9ESqHG4K-As3yiPZwNdnL-jntjUA3rQxi18oFZZ_FSXoVsl86JUyUwf9rR1TybajEmiqJM15-6ZryCfwSTQo7zdNAAUWLe5pTPh2fep86WlWypJ9nLB_Yp1NJuzajrhE1vg7B1VaHSphbaa87hFObXAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه ورود نتانیاهو در واشنگتن دی‌سی
🔴
نخست‌وزیر اسرائیل امروز با ترامپ دیدار می‌کند تا درباره ایران و اهداف احتمالی «تأسیسات هسته‌ای» گفتگو کند.
🔴
گزارش‌ها حاکی از آن است که نتانیاهو «اطلاعات محرمانه‌ای» درباره تأسیسات هسته‌ای کوه کلنگ ایران آورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/138045" target="_blank">📅 03:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138044">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb91a1151e.mp4?token=JsI8apk9veM2ZfhWvtpE3_zT91BifGKslaDl1w7aDQXuVJ939diCwv9lPqBvJRNvvFjhrZZiuJzQ-MjJVo2Qw2KYwrNx8BwkV3zTNgS0XuNvOuennS47s2VlJ8cS2-DGfBkR88XSAbnTyMZ9Iy1VqSLe-KqdBFwbpXwJXNRcyPbsB66CMSVVwopi_GFpEyR0twz1kI-Dr3H5AGEj-cznoDbTQtBUTHBBv2AJTZOSIZHnWDNPPPAe2Aa6gTZzNmhsmMJoi3e5wDpHZWFJMwEj6cg54F11z2ybnvr5Dz3WPWWceGpspxpWvZxGChIKsxKYcXjVl8GgvzSY5--V9r-Sww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb91a1151e.mp4?token=JsI8apk9veM2ZfhWvtpE3_zT91BifGKslaDl1w7aDQXuVJ939diCwv9lPqBvJRNvvFjhrZZiuJzQ-MjJVo2Qw2KYwrNx8BwkV3zTNgS0XuNvOuennS47s2VlJ8cS2-DGfBkR88XSAbnTyMZ9Iy1VqSLe-KqdBFwbpXwJXNRcyPbsB66CMSVVwopi_GFpEyR0twz1kI-Dr3H5AGEj-cznoDbTQtBUTHBBv2AJTZOSIZHnWDNPPPAe2Aa6gTZzNmhsmMJoi3e5wDpHZWFJMwEj6cg54F11z2ybnvr5Dz3WPWWceGpspxpWvZxGChIKsxKYcXjVl8GgvzSY5--V9r-Sww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گریه خانواده اعدامی‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/138044" target="_blank">📅 03:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138043">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOgI9zBzXaS9-1dY-cQiNagLhGQ7nhKUX4Djes6KEsEEshV-TUHKNF9F11qIEms574Shn25gloA3GSMfnvfCS2ohL9phTnrtqKj3OjMqswLKNISh0CKBfAcA2fmqEeFXvE6WVnvXQjd3_sMq1Gxwpvs2RDLnX1CNw8MhIAjYZEsbiQ3_Y65oTAnQkmvqtvUtDSB7AYSoDgB6kXOvsU0N3eRt4T7jJS3s_NXsScB2i3lrXXyx1ygFSZq7IOGj8u2easdGgC4shdMA1iCTdQCxDklrIZ4JC7W8IkRHgX4jfU_6osntT5H924K16K2H4HNGtFXygcAOLnMfGoIxL99PdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آزاده آل ایوب(خاله نرگس): نباید به بازداشتی‌های اعتراضات عفو داد و باید همشون رو اعدام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/138043" target="_blank">📅 03:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138042">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c96ac69ef8.mp4?token=VReDsNLqvkrir6AWAf562g26Qy91aSoTzDJvBOEIt3lo8BqiaxT4xc2BTnbsnUEm4CAUxMPYBbwKXhiaIjcj_kk8FfnDkXQ9oR5KNdmICrvStCeMsnb0vtwPtlAMtA9I0JmC2VKMYVHSG07apn438ZcGgWMhSBMpLqiqV_ZyOnkJAyi3X-SFOHy5Sp7ybLeIwcHxeRI19dmdZ219IXjB2d4oOJBktcyF9dzIHvWmRTN1DrFnTVZE7A6-ZShzvOpuR31_wFJg1begJzTjlsvMDm5vzliGMxu290XX348SKQEfSZ4X9nV3zMCYciWio_hmNOl5v1RrneZfWTnFmUH6j01Sf83vE0oMOyAXMe8bgqnvMI_XgOuTDjOXpFB9LqERBYCFrAkdRBBHliFVW1Xc6akWNyFUetZ99fZuor8OiAYoOqskcMLDlgFVgt74w4zFpzsxdYSxBX8xIKjCWVYV4QySOtE9ir4BecLSo0h5JuDBvTHb37Ubp0eHSw2zW6BPvmW4a-EktiukzBVQSfhpcDwm6WloPtA3vbdE7uVIUwtiYUb5dsJB2zZSU1YL8ye8JaNi89smJrEt2M8Pb853DnEVijccSEQe4OlQ6Xv2jrffwQG5gdp4JTRcZVs6fMKyXATeFqHQbdqsNOVU9woWVDtgrJgRj14qkiV4jS3IesA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c96ac69ef8.mp4?token=VReDsNLqvkrir6AWAf562g26Qy91aSoTzDJvBOEIt3lo8BqiaxT4xc2BTnbsnUEm4CAUxMPYBbwKXhiaIjcj_kk8FfnDkXQ9oR5KNdmICrvStCeMsnb0vtwPtlAMtA9I0JmC2VKMYVHSG07apn438ZcGgWMhSBMpLqiqV_ZyOnkJAyi3X-SFOHy5Sp7ybLeIwcHxeRI19dmdZ219IXjB2d4oOJBktcyF9dzIHvWmRTN1DrFnTVZE7A6-ZShzvOpuR31_wFJg1begJzTjlsvMDm5vzliGMxu290XX348SKQEfSZ4X9nV3zMCYciWio_hmNOl5v1RrneZfWTnFmUH6j01Sf83vE0oMOyAXMe8bgqnvMI_XgOuTDjOXpFB9LqERBYCFrAkdRBBHliFVW1Xc6akWNyFUetZ99fZuor8OiAYoOqskcMLDlgFVgt74w4zFpzsxdYSxBX8xIKjCWVYV4QySOtE9ir4BecLSo0h5JuDBvTHb37Ubp0eHSw2zW6BPvmW4a-EktiukzBVQSfhpcDwm6WloPtA3vbdE7uVIUwtiYUb5dsJB2zZSU1YL8ye8JaNi89smJrEt2M8Pb853DnEVijccSEQe4OlQ6Xv2jrffwQG5gdp4JTRcZVs6fMKyXATeFqHQbdqsNOVU9woWVDtgrJgRj14qkiV4jS3IesA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جو شدید امنیتی در میدان علیخانی اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/138042" target="_blank">📅 03:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138041">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ به سی بی اس: مایل به توافق هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/alonews/138041" target="_blank">📅 03:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138040">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
یه سری کانال خبری هم که فاز مردمی برداشتن دیدن ویو خوبه بین خبر اعدام تبلیغ شرطبندی گذاشتن تا پول بیشتر گیرشون بیاد
🔴
یه حقیقت تلخی هست تو این مملکت هیچکس دلش به کسی نمیسوزه و همه منفعت طلب شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/138040" target="_blank">📅 02:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138039">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIEV_1gKVwIexNskcaImjZjdVou_7QaMhA95zQLH_HT-6vOBCI0czX32rZEAbVI1W2vgqXgQQZsIlHX60mS-_vyAQTSihClaeJP4rnZ07gbmk_RW7H6Umao4jfswKqHfqaDd_ojXTyrGTpgEMPEg7E5dKepnsunoR-q57ybqT-LPupSFxIKw6GB8wk7ultZme0k9Wr59_ZG8eNcyCnfP1prHa7AbdcvUI9DK7QWfu5OaEPvEqtRKD5Fdg70a9cl-0LNV9PeTaKm4kVFtbKka7OEsbJPkbP--x-9OXMb-OoxN13-8DO7DUiwgQsGsOREoDGZdzzWAHbVNNFDeIESfPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اعدامی‌ها رو آوردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/138039" target="_blank">📅 02:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138038">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5c5d18645.mp4?token=XiuPptiJqjIZ3uJTm6dC_G2grbI9sTZ47AIJiEXkTOQdXEiSZftffrPBfYltOZuRjvFM3Qc8ZHFbLu-tRX8c6Gg_hmWb-B4icAE-GIvs7feS1oyMXUEJwTYOB0AG57ZmpOkq02E8ErIPRlbI6vUf0E4SjK8TM9a9veMM9De33zKIKsS6nNaRvBV7WyLeRxZOKutrsDHWfAtXk0gwK5vmGkDFvg0AlXSRoFkGQBgdW23byhfxB7n64m9LwqMmk_aXrSh51QQaNGlqGvCkoGrK4KIbiuUsGNfegKbR8kN0beJIIEf7OMM8xhmXa5oE4z8VgEIkBmrpf68ryMAM-XEj9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5c5d18645.mp4?token=XiuPptiJqjIZ3uJTm6dC_G2grbI9sTZ47AIJiEXkTOQdXEiSZftffrPBfYltOZuRjvFM3Qc8ZHFbLu-tRX8c6Gg_hmWb-B4icAE-GIvs7feS1oyMXUEJwTYOB0AG57ZmpOkq02E8ErIPRlbI6vUf0E4SjK8TM9a9veMM9De33zKIKsS6nNaRvBV7WyLeRxZOKutrsDHWfAtXk0gwK5vmGkDFvg0AlXSRoFkGQBgdW23byhfxB7n64m9LwqMmk_aXrSh51QQaNGlqGvCkoGrK4KIbiuUsGNfegKbR8kN0beJIIEf7OMM8xhmXa5oE4z8VgEIkBmrpf68ryMAM-XEj9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعدامی‌ها رو آوردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/alonews/138038" target="_blank">📅 02:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138037">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
طبق گزارش‌ها، دقایقی پیش چند دستگاه آمبولانس و ون انتظامی وارد میدان علیخانی شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/138037" target="_blank">📅 02:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138036">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/710f6ceb7e.mp4?token=Avxjs4n2yyLxU5xKAmBeVGHTl5YRINr_30B70SmCP_X9FJ1IQNeXNF-idR8dTCFh61uC7GK57JTPoo9SFi21Pd46VV-39wSyh214zJ5DNRLNlAqymAdP_PAIBsYwLuD4bJLTTcsbjcbzwJAiODqnGtg4JMv-2KW7Nr3FGFgZ1hJe_g1uVY4t7OdXwJMznlGbGyXZ-icAfBssZLDAgP27Wg6baIzt7Q5jDtcm9M8s2Relbc3AWjaeC7WJJpqBBGXrVyBVmFqUW89pTGRrTGUVLKWU9XN-4IbLEGnjIJwiFjKEQbXNbrW1y499IZQ2JSCXZ8pWIXl7lPPANmnQswPxgot2AxQz9Cq9VYDyQy0Kyc6FC3NEzHtDQ6UgUvQA_PUP5vM3Sf-vcZhQCUo3cNOWip2ggaDZ0fs-fAxHaWC9Dd3KvY6Sa-FcstsdbZIxkJpy6M0cC7Ao_IyWJvCcs814g7T9Carldil-01bN7fdQKIbzCDcA4Nv9msOzlRcJJ0yuMo4kTfZwVsBNRRh-oeSDwDG7SXevr4sgsiqeF2OEYmu5o1wUee8NFc08HJYV_50RCMMElIRLFBoYWLmd3_6bgqHlsN8C4vj99XDQaIDpj_2zRkgUvqqIKK_QumZeG8xJ7oYDbe5Wd784SCSKALYsGKnUiR8U41UeaFPGuUTB1q4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/710f6ceb7e.mp4?token=Avxjs4n2yyLxU5xKAmBeVGHTl5YRINr_30B70SmCP_X9FJ1IQNeXNF-idR8dTCFh61uC7GK57JTPoo9SFi21Pd46VV-39wSyh214zJ5DNRLNlAqymAdP_PAIBsYwLuD4bJLTTcsbjcbzwJAiODqnGtg4JMv-2KW7Nr3FGFgZ1hJe_g1uVY4t7OdXwJMznlGbGyXZ-icAfBssZLDAgP27Wg6baIzt7Q5jDtcm9M8s2Relbc3AWjaeC7WJJpqBBGXrVyBVmFqUW89pTGRrTGUVLKWU9XN-4IbLEGnjIJwiFjKEQbXNbrW1y499IZQ2JSCXZ8pWIXl7lPPANmnQswPxgot2AxQz9Cq9VYDyQy0Kyc6FC3NEzHtDQ6UgUvQA_PUP5vM3Sf-vcZhQCUo3cNOWip2ggaDZ0fs-fAxHaWC9Dd3KvY6Sa-FcstsdbZIxkJpy6M0cC7Ao_IyWJvCcs814g7T9Carldil-01bN7fdQKIbzCDcA4Nv9msOzlRcJJ0yuMo4kTfZwVsBNRRh-oeSDwDG7SXevr4sgsiqeF2OEYmu5o1wUee8NFc08HJYV_50RCMMElIRLFBoYWLmd3_6bgqHlsN8C4vj99XDQaIDpj_2zRkgUvqqIKK_QumZeG8xJ7oYDbe5Wd784SCSKALYsGKnUiR8U41UeaFPGuUTB1q4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قوه قضاییه:
علت حکم اعدام متهمین میدون علیخانی اصفهان اینه که این افراد در 18 دی ماه تو میدان علیخانی، مامورها رو با طناب به تابلو بسته بودن و بعد از اینکه با سنگ زخمیشون کرده بودن روشون بنزین ریختن و آتیش‌شون زدن و درحالی که مامورا زنده بودن اونا رو روی زمین میکشیدن و با چاقو تیکه تیکه‌شون کردن و فیلمش رو برای رسانه‌های معاند فرستادن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/138036" target="_blank">📅 02:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138035">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jIautNwdWHjtVTi4XVLJTpNKLBkO2d9N9MOEdn3M_s8vVjGBITYL5ma_1P_l8xx4g8tKK7DwXDcJQdXrMEvF2m-vg_Cxl-XD2-G2HI1_EoXH1ze4fSh0UCF5yslsxhsVjfdf6xg_w_6nwO93ZlQFkpBo12IyWhQYAoWKD2GD3SPKLf77B9OLcpwEA-EQPNvoU65HbGROzrjhKtoW0kgrEPf-6o-_LVkOeCbEY9owOyd0b_p5KDTnEHVk-crsuVb66Bto2LEDvNpZZMnR5i91Tuz8qPsc5XDxQnKyHCkPZ0dh74NC_Crvew21u2-DGt0avmziztpyflY4DCwx-e4TNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا همزمان با اذان صبح، مهدی ظریف 23 ساله هم بخاطر شرکت در اعتراضات دی ماه، در مشهد قراره اعدام بشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/138035" target="_blank">📅 02:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138034">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ql2ISSGRfkWmL5zsWx1byQkrsSr8dKQWNmN5jvai-Kf3DTHTHmTt9xVnt1XZbT48_s1AUWmHME9AqmhJ87HkSETslNIEeytRZKSFoT2fDlihniI4WxbgrNRQqyHxCivs-fOW5cv6vD95pNgD-oVNPSI0ewj2g3QNTntwcBHTBhqMDGx8mwTxEI_zthn-Hw-vYY6u_7zYzsghuWO0gqx-kKzzBEpbEXInRN2oyD2rYObzJyMC3ihvVmkX2UGUXdPwFMFroxQIh9HmC9c2LZ2UyxPtbsp7Hz4KRw_wRVSro5vxEDD3SSYZLnU2iBROf48SMBqVWY2fCIYcUCxD4YGv2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بنر نصب شده در میدان علیخانی اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/138034" target="_blank">📅 02:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138033">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/780d746559.mp4?token=hObqQ-EjI3-ylu7ExeCB2vtNWLsvepEMxTl9s0hnTxBTLJZnFbmKRtNg0NrqfPE9wyG_vgL45QRqthHEUosSVVczppyE_ZlZm4f9EanOrkWzL_Xiv70VoGnEY_SIytghwJy9ZBbdMr49awNVqyunJbHPumkzgzCXi_Z9P15g1tcI7m1TE-e5e9mIre2KysAfw5-9f8x3jac1LoaZcI4Dp-2IVgS-UhH_atXmIKklSJ5E5xt7wdbVGvbt_jYxHasLuyaKjipFFZM2P7Xvk7j-iiSWwWHipJt_GGr9ZZTytuC2zH8WfvtBWo-GTOCe49d_FmU5FMNRz6aGIu_79qEERQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/780d746559.mp4?token=hObqQ-EjI3-ylu7ExeCB2vtNWLsvepEMxTl9s0hnTxBTLJZnFbmKRtNg0NrqfPE9wyG_vgL45QRqthHEUosSVVczppyE_ZlZm4f9EanOrkWzL_Xiv70VoGnEY_SIytghwJy9ZBbdMr49awNVqyunJbHPumkzgzCXi_Z9P15g1tcI7m1TE-e5e9mIre2KysAfw5-9f8x3jac1LoaZcI4Dp-2IVgS-UhH_atXmIKklSJ5E5xt7wdbVGvbt_jYxHasLuyaKjipFFZM2P7Xvk7j-iiSWwWHipJt_GGr9ZZTytuC2zH8WfvtBWo-GTOCe49d_FmU5FMNRz6aGIu_79qEERQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون میدان علیخانی اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/138033" target="_blank">📅 02:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138032">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">#نه_به_اعدام</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/138032" target="_blank">📅 02:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138031">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1dfac21ffc.mp4?token=K1uDZ_SraTF9hxGgnCx9elK5F_6DL0WPJaJcB3ab7pLeu0WsAE3UB7c_M5r1-OnikmYwbsKkptPoLcnN8bVTAqeuKNM8isQzQrHr8e4ecf_k3fY2_xRPPpRfDMdDaYecLDfwTBSqMm4aItGB2oHtbr7jxO7jgH0cL3QdsIZdrlvAbeqj79i3qVf9ZrjuNI8IwEUF4_LnL6yFPDwEa_7QvnXAyTDDrfGWRDrtLGexbXHn0t6PMJLm00Q393ZixhBiAIBZpN9Wy4KPWjhCsF4BwJGMSFmDyoeWyxsWDkbwKSddQa8x_4hAbR5inHILYuuKfxEjRYHHHrtrZOc63vp4lw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1dfac21ffc.mp4?token=K1uDZ_SraTF9hxGgnCx9elK5F_6DL0WPJaJcB3ab7pLeu0WsAE3UB7c_M5r1-OnikmYwbsKkptPoLcnN8bVTAqeuKNM8isQzQrHr8e4ecf_k3fY2_xRPPpRfDMdDaYecLDfwTBSqMm4aItGB2oHtbr7jxO7jgH0cL3QdsIZdrlvAbeqj79i3qVf9ZrjuNI8IwEUF4_LnL6yFPDwEa_7QvnXAyTDDrfGWRDrtLGexbXHn0t6PMJLm00Q393ZixhBiAIBZpN9Wy4KPWjhCsF4BwJGMSFmDyoeWyxsWDkbwKSddQa8x_4hAbR5inHILYuuKfxEjRYHHHrtrZOc63vp4lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون میدان علیخانی اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/138031" target="_blank">📅 02:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138030">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uoG3okuTm6EYpHiStGWwYU1oWGngyZpMqUXRdOBD5szIN_WCw2BXQ8VNGm1Rhi6P7JVW1l8xELwfMbBD_lIAAzp2hy4JiEBVNqBEY6_feJs7PvTWIWiOJrrTayU5RxWcNThRZtX66H5C7NA4MtLf64EH9Z2zoaoH_57m5dXy_ZLAZ8IZiUCGqVUkRvPn1JPyZURt_KLJDU0QxaDbOIBfU82fBqb3OlX5RNQdojpgpWUb9Yy_9z_NjU6AqT9wFg6iX6PEvZRROhPwBbD8td21yEmNnX8HVdA-SkD5zJ3GCRhmf4NUGHrF5osBl0ymupU2_AXUmSTw8y1BWZeW6dqFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه نگاه به دستای امیرحسین صفری بندازین!
🔴
این طفلی اصلا معلوله! آخه چطوری میتونه یه مأمور رو کشته باشه! چطوری دلتون میاد اعدامش کنین
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/138030" target="_blank">📅 02:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138029">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d0967f8fa4.mp4?token=jzTEtWlxAm_5YaqjaCF1YACgtQt8K3Tj4hQInPOYQLt84XmOiK4jnsdcEzBjreujnpr2eHEyQtSS7Ns8c3IrlTsHFwJih8QKDj3StH7ybCLFhG8t222U85JBG4y_4n48pe12TgeMpRuNqR3qUKlLMAzquxTlo9IKkOwLFzD3pwV9nZwEMyL0_1tSspxRl1CJW2TfAjF8XihMOhZqAE0P3mzclBql5fkMEQlM3f1hrZlf5UvgP7lOQAsPSCk1VTn2TBLybYvBOH7eVek7yoT-7JsB92_CKM9v0_fVt5eUXuquKW6K-QZqGUMx3svJAAjf6yYN62TyCPp2YF_czUZu_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d0967f8fa4.mp4?token=jzTEtWlxAm_5YaqjaCF1YACgtQt8K3Tj4hQInPOYQLt84XmOiK4jnsdcEzBjreujnpr2eHEyQtSS7Ns8c3IrlTsHFwJih8QKDj3StH7ybCLFhG8t222U85JBG4y_4n48pe12TgeMpRuNqR3qUKlLMAzquxTlo9IKkOwLFzD3pwV9nZwEMyL0_1tSspxRl1CJW2TfAjF8XihMOhZqAE0P3mzclBql5fkMEQlM3f1hrZlf5UvgP7lOQAsPSCk1VTn2TBLybYvBOH7eVek7yoT-7JsB92_CKM9v0_fVt5eUXuquKW6K-QZqGUMx3svJAAjf6yYN62TyCPp2YF_czUZu_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون میدان علیخانی اصفهان که قراره ۳تا جوان رو اعدام‌ کنن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/138029" target="_blank">📅 01:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138028">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
هواپیما بی‌بی نتانیاهو دقایقی پیش در واشینگتن به زمین نشست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/138028" target="_blank">📅 01:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138027">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
به صدا درآمدند آژیرهای خطر در کنسولگری آمریکا در استان اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/138027" target="_blank">📅 01:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138026">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501833108d.mp4?token=cZuRciusYkU4xTbolikwfOQRAkVNyyZgUElenDU_EMzizkG1PBa2ugYUzpV8j-yX-TMwbQI1ZxHm6g8iBxLbSXLTvjURemPz4glHpKV_0O_ma7DdCZT1V4sx4y0ECUYAXsk_9tSdX8T8wYrSquvS10Y0XbNmRbjSJJeDfRYfmMgKgRxA5HiRf-kQfDHKi7aXxxu9m46wkqY4sdtjy-mDzEduf1nKcRjq0ltlg78bnHYxJ6CDfhvQchATisavkM75FdLhYTBnj17keYMNNoHdDbr63BJBmafzndUcDO_URT5uiDKN44P8WYLdFCozIOy19OkWpbd9NBv_p14JfI79dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501833108d.mp4?token=cZuRciusYkU4xTbolikwfOQRAkVNyyZgUElenDU_EMzizkG1PBa2ugYUzpV8j-yX-TMwbQI1ZxHm6g8iBxLbSXLTvjURemPz4glHpKV_0O_ma7DdCZT1V4sx4y0ECUYAXsk_9tSdX8T8wYrSquvS10Y0XbNmRbjSJJeDfRYfmMgKgRxA5HiRf-kQfDHKi7aXxxu9m46wkqY4sdtjy-mDzEduf1nKcRjq0ltlg78bnHYxJ6CDfhvQchATisavkM75FdLhYTBnj17keYMNNoHdDbr63BJBmafzndUcDO_URT5uiDKN44P8WYLdFCozIOy19OkWpbd9NBv_p14JfI79dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش حمله و انفجار در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/138026" target="_blank">📅 01:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138025">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=sQ3GmXnFgoyn1EtgB85VO-2W_qUnExGLK4f5U1ZsYG4UsGPhSCXVp3PtwiGjjtSgC3UOvmhapDIO4DeHkBR7FYRyJ2BmJuqM5rSB5iLVs9LwFG-cjWdNvUb2cJYtHIwz0lBQI6p4Uf1McwobjQ9PE9jHQij_t1YGILqnS5TdjKtNbdu0dpzMwxygLZcjmuZjVIA8E4HRjUjeuOhZ9PlBsNOzLBySe1WvOSlXhzNtd9y7yLfNhjYxuc6mU1Kuuh-IED3cYO8zUsR0ESo1J5XXeoTskMQbObkYYo0B3AN0vm9JlNE6fHqn7bIUhWzyU0nuLzIfX8DnonIAFMuTszEgG4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=sQ3GmXnFgoyn1EtgB85VO-2W_qUnExGLK4f5U1ZsYG4UsGPhSCXVp3PtwiGjjtSgC3UOvmhapDIO4DeHkBR7FYRyJ2BmJuqM5rSB5iLVs9LwFG-cjWdNvUb2cJYtHIwz0lBQI6p4Uf1McwobjQ9PE9jHQij_t1YGILqnS5TdjKtNbdu0dpzMwxygLZcjmuZjVIA8E4HRjUjeuOhZ9PlBsNOzLBySe1WvOSlXhzNtd9y7yLfNhjYxuc6mU1Kuuh-IED3cYO8zUsR0ESo1J5XXeoTskMQbObkYYo0B3AN0vm9JlNE6fHqn7bIUhWzyU0nuLzIfX8DnonIAFMuTszEgG4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بخش‌هایی از سخنرانی ترامپ در میشیگان:
🔴
آن‌ها ۴۷ سال است ــ که در واقع نزدیک به ۵۰ سال می‌شود، چون دست‌کم سه سال است همه می‌گویند ۴۷ سال ــ مذاکره می‌کنند و تنها کاری که انجام می‌دهند این است که همه را معطل نگه می‌دارند.
🔴
همچنین نمی‌توانیم اجازه دهیم آنچه در ایران اتفاق می‌افتاد و هنوز هم اتفاق می‌افتد ادامه پیدا کند. آن‌ها در یک دورهٔ چهارماهه ۵۲ هزار معترض را کشتند؛ تصورش را بکنید، ۵۲ هزار نفر در ایران.
ترامپ: ... ونزوئلا.. پس از آنکه تقریباً ظرف ۴۸ دقیقه پیروز شدیم، گفتند: «اوه، حرکت خوبی بود.» خب، همین اتفاق اکنون در ایران در حال رخ‌دادن است.
مردم هنوز متوجه نمی‌شوند. ما نیروی دریایی‌شان را نابود کرده‌ایم. نیروی هوایی‌شان را نابود کرده‌ایم. رهبری‌شان را نابود کرده‌ایم. تسلیحات ضدهوایی‌شان را نابود کرده‌ایم.
پهپادهایشان اکنون با حدود هفت درصد ظرفیت قبلی تولید می‌شوند. بخش عمدهٔ توانایی تولید پهپاد و توانایی تولید موشکشان را نابود کرده‌ایم.
اکنون با ما دربارهٔ دستیابی به یک توافق صحبت می‌کنند؛ اما اگر ما این کار را انجام نداده بودیم، هیچ مذاکره‌ای در کار نبود.
آن‌ها ۴۷ سال است ــ که در واقع نزدیک به ۵۰ سال می‌شود، چون دست‌کم سه سال است همه می‌گویند ۴۷ سال ــ مذاکره می‌کنند و تنها کاری که انجام می‌دهند این است که همه را معطل نگه می‌دارند.
آن‌ها قلدر خاورمیانه و قلدر ما بودند. اوباما ۱٫۷ میلیارد دلار پول نقد سبز به آن‌ها داد. یادتان هست؟ پول‌ها را داخل یک بوئینگ ۷۵۷ گذاشتند و به تهران فرستادند؛ ۱٫۷ میلیارد دلار پول نقد.
او تصور می‌کرد می‌تواند به آن‌ها رشوه بدهد؛ اما آن‌ها در عوض با خودشان گفتند: «این کشور چقدر احمق است.»
نه، نمی‌توانید به آن‌ها رشوه بدهید. باید شکستشان بدهید و ما داریم حسابی شکستشان می‌دهیم. اما خواهیم دید نتیجه چه می‌شود.
اکنون مذاکراتی بسیار دوستانه در جریان است.
نیروی دریایی ما در اجرای محاصره چقدر خوب عمل کرده است؟ حتی یک قایق [نتوانسته عبور کند]. آن‌ها می‌گویند: «دیگر محاصره را نمی‌خواهیم. لطفاً، لطفاً، محاصره نکنید.»
---
ترامپ:
اکنون قیمت تخم‌مرغ بسیار پایین‌تر از زمانی است که کار را آغاز کردیم. خواهید دید پس از آنکه تهدید هسته‌ای ایران را از میان برداریم ــ که بسیار زود اتفاق خواهد افتاد ــ اوضاع چگونه خواهد شد.
اما افزایش قیمت‌ها ربطی به من نداشت.
---
یکی از سخنرانان همراه ترامپ:
۴۷ سال طول کشید تا کسی بایستد و بگوید دیوانه‌ها نباید سلاح هسته‌ای داشته باشند.
همچنین چندین دهه طول کشید تا مشاغل را دوباره به داخل کشور بازگردانیم.
---
ترامپ:
نمی‌توانستیم اجازه دهیم آنچه در ونزوئلا اتفاق می‌افتاد ادامه پیدا کند و اقدامی که انجام شد بسیار قاطع بود.
همچنین نمی‌توانیم اجازه دهیم آنچه در ایران اتفاق می‌افتاد و هنوز هم اتفاق می‌افتد ادامه پیدا کند. آن‌ها در یک دورهٔ چهارماهه ۵۲ هزار معترض را کشتند؛ تصورش را بکنید، ۵۲ هزار نفر در ایران.
اما هزینهٔ عملیات ونزوئلا، همان‌طور که گفتند، تاکنون جبران شده است. به همین ترتیب، در برابر جمهوری اسلامی ایران نیز با اختلاف زیادی در حال پیروزی هستیم و تضمین می‌کنیم که آن‌ها هرگز به سلاح هسته‌ای دست پیدا نکنند.
وقتی کسی می‌پرسد: «چرا این کار را انجام می‌دهیم؟» پاسخ این است که نمی‌توانیم اجازه دهیم شما سلاح هسته‌ای داشته باشید. همین تنها چیزی است که لازم است بگوییم.
اگر قدرت سلاح‌های هسته‌ای را درک می‌کردید، دقیقاً متوجه می‌شدید که چه می‌گویم.
---
بار دیگر می‌گویم: ایران هرگز سلاح هسته‌ای نخواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/138025" target="_blank">📅 01:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138023">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GnJE4BMiAOivG3oxJfPjnh_-DkNmcBxYGcKF5AsWm49h3cLyBfc35VHruhWg2LM3d-66CsvZkA7W8SdZv0R9L4_9QPWZ6IKyG0jbTRc1CGXDH_Ua_NuZCg2f0B7T_weT6ssBUZBilXyQ_pVlAZmapD20W8wptNgCXUKAie0vn4ymAMqycRWVGfFXvjz0lnqC-D07FeTM_WHtywQ-Rv9i8jcpDLIpUqQJ9_t_bIJmizXLlZl0s8gpFAnuA-rH0QIh3EHq8Nn8XhhH73a2AGGpV9VfZirkdioCyMMB4NcTiE-RndhP5oPO5mplpl-1Ea3tmHbJkKzTrh3uJE-2C9Qiig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WR4lekXWRhR4B6vup1MGPBVWitY1oY1ehyS5vThq7W5RenVTmUx9Mkun_Y0O_fKTwMSYrDYpZ0hqpHAx6h7rgi4z1VRragHiMm0IAJPJu33MEgKd-JFpDpa3R_1i0WiCZmBqEHH9Cm_8WrHoO5rLkOKTFVBYhTJ4laL0TMjMoqmG-jX5vwU75OEdinE6nSDZe_FhGNfHXYGebgr5bVaiPkXPbLOQpjHo0kCzMaA_Q-4V2kzC1ewdL0oBvZJKUBkI5hfZ04U5PsoC6n6b1EZlIrNTwRBpgOXROFY0ImOMyAxYrtPshGW_PGGyToXRo63juFFdoSp9XWzwlIn4lO58YA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یه پسر ۱۱ ساله داشته بازی می‌کرده که از ارتفاع ۱۰ متری سقوط میکنه و از شانس بدش، میله آهنی مستقیم فرو میره توی باسنش!
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/138023" target="_blank">📅 01:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138022">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9b8525811.mp4?token=bHgxvUk5shwnrZHKyunQXDr7ni3w5tnT2PSqXPGswLy2RSwgX7VCWA0GZsoVhFMcXPg5y_MKR9Pf1g8uhgVA1jAMcEwkucFmFPGsGchvc10PrHWeH2p98-GxAG0Ps0dnKXFqaixgvBhbLQwnXeWr0Ip9_zQ3AF4rZK_S4zyXAnytvAObM6Ef5Kw4Ip1C_PyO4Q2vM2IYES054sXVtwPeLGOVY6QYJRzimHN12n_UeXzkAOlUk2f3EvnfKj8IukZVVffwp4G8LGl0MPta-OzKxV0OWkD537geV7eFCYFTPX_vL0EJiwgPMrq3L6Eqs8zgJWx0F1d-PRXfoFwy6wB7Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9b8525811.mp4?token=bHgxvUk5shwnrZHKyunQXDr7ni3w5tnT2PSqXPGswLy2RSwgX7VCWA0GZsoVhFMcXPg5y_MKR9Pf1g8uhgVA1jAMcEwkucFmFPGsGchvc10PrHWeH2p98-GxAG0Ps0dnKXFqaixgvBhbLQwnXeWr0Ip9_zQ3AF4rZK_S4zyXAnytvAObM6Ef5Kw4Ip1C_PyO4Q2vM2IYES054sXVtwPeLGOVY6QYJRzimHN12n_UeXzkAOlUk2f3EvnfKj8IukZVVffwp4G8LGl0MPta-OzKxV0OWkD537geV7eFCYFTPX_vL0EJiwgPMrq3L6Eqs8zgJWx0F1d-PRXfoFwy6wB7Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مصاحبه زنده یاد کیانوش سنجری با شبکه (آیت الله) بی بی سی که حرفاش به مذاق این شبکه خوش نیومد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/138022" target="_blank">📅 01:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138021">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
گزارش‌های تائید نشده از حمله به کنسولگری آمریکا در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/138021" target="_blank">📅 01:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138020">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b4fa9f23e.mp4?token=nZznTEV8JaIteFCOIWlPFoSAjkqX9VwGj25C1aFofFZh63c4xXbIlLwdnwU7uaZuuFn2n2aqG7VNG6ElNeJylKqJxvs1appNhn2mjwA5ZSuNJEjEy7COlhPiNzRJR2-YErpKKfkMDK6y6VoWLyykCnjWTdXYS_AdYbjAVOZwsClJah2GDTKslWEoQlNCjmhB2Ihnnv-U1eZlvM2Y3xQJCi9zxjEt4Ws-MLJaJKGBmmDKVuUiQbSK1cYjK6rbBQKif8bLTwCnlPSbkKiZg88uniA01A2v0XUXTHWs0WZhXfZZUfJBZ3QZW_pOdrpvGYKcHr44VAie0i-QS1X36NMmKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b4fa9f23e.mp4?token=nZznTEV8JaIteFCOIWlPFoSAjkqX9VwGj25C1aFofFZh63c4xXbIlLwdnwU7uaZuuFn2n2aqG7VNG6ElNeJylKqJxvs1appNhn2mjwA5ZSuNJEjEy7COlhPiNzRJR2-YErpKKfkMDK6y6VoWLyykCnjWTdXYS_AdYbjAVOZwsClJah2GDTKslWEoQlNCjmhB2Ihnnv-U1eZlvM2Y3xQJCi9zxjEt4Ws-MLJaJKGBmmDKVuUiQbSK1cYjK6rbBQKif8bLTwCnlPSbkKiZg88uniA01A2v0XUXTHWs0WZhXfZZUfJBZ3QZW_pOdrpvGYKcHr44VAie0i-QS1X36NMmKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حکم جلب این بلاگر طرفدار حکومت بخاطر نوع انبه خوردنش صادر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/138020" target="_blank">📅 00:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138019">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رئیس صداوسیما : اعتماد مردم به صداوسیما از اعتماد مردم به دولت بیشتر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/138019" target="_blank">📅 00:44 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
