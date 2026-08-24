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
<img src="https://cdn4.telesco.pe/file/hgncm8MDeYMuTtg13gus1jZ9Veg4vkeDdTH_VIxn8TWlFWBUMGIS46F2_SJj1sctRJgFkYH_2EY1Qm1QxcMDwu6Apgmpgb04tE20aRKk7DYLlCOFfDY1ti2NfRr2zlnEmmXsD9o4wDo6uQD0M1-V3JKbTeGotrQgO6aJoLQBVrkNFHStaXafH5Hrlgntt_Vl8zcOInsjiRY_TNLmCAYjjxikynbsFt0HWET7VjRwmsk6ZrSkswZdBt6vGq9Dl8oopsMwQfliCVUC8sFEwQM7nf48psOpe58y3AsL_mQPzfZEUkO4ZKlp4DMJjyrLqPKPzBRZOjId0eJLebwp2sjvXg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 610K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 21:24:56</div>
<hr>

<div class="tg-post" id="msg-28418">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e283ffe059.mp4?token=dfFtyRoB1B-dtyeNZl5PTZKurjWWIzZNh-sOz0HZugdYGMvgzqC9yj0RzNx21FaZFjdzZhiwjcJDqBCeGAL9qyZ6HVinNJoCNCLChJHpJzQ7e-rJnCCUIABa-e2vFGIfQJ5aNFTbOO8IFgf0RyNlRhrn3z7ynIrcYsfK2DDoNbsxZemiKHUKDH2klL5fVMD_0YRZRcZm59aCbt8PahXUJ_OsRKUJ3BmrUo0qynwanmqrLfz7XjiBLtuJ3r5Sko0BbJhS6bqoaOy4Ci4b4HtorVElJ9EL7DM61mybsHtbXYSQa2SNc28p15Nbq7QaT8p8tphsUc-szsFNaccbZisDTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e283ffe059.mp4?token=dfFtyRoB1B-dtyeNZl5PTZKurjWWIzZNh-sOz0HZugdYGMvgzqC9yj0RzNx21FaZFjdzZhiwjcJDqBCeGAL9qyZ6HVinNJoCNCLChJHpJzQ7e-rJnCCUIABa-e2vFGIfQJ5aNFTbOO8IFgf0RyNlRhrn3z7ynIrcYsfK2DDoNbsxZemiKHUKDH2klL5fVMD_0YRZRcZm59aCbt8PahXUJ_OsRKUJ3BmrUo0qynwanmqrLfz7XjiBLtuJ3r5Sko0BbJhS6bqoaOy4Ci4b4HtorVElJ9EL7DM61mybsHtbXYSQa2SNc28p15Nbq7QaT8p8tphsUc-szsFNaccbZisDTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسینی فر مدافع ذوب آهن در بازی امشب مقابل مس شهر بابک به این شکل تماشایی دروازه خودی رو باز کرد؛ جدول آنلاین هم پست ریپلای شده ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/persiana_Soccer/28418" target="_blank">📅 21:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28417">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQjrsT_a0lE1I3sbSEPigjO7KH2wm8Gx49nWOuNZRpQ7oPZQOCq4M4MwTCYY2jxtRR56uhzzMpI34QIDq5hvmHEVrZ7vROMUqSUQ4yUGKvlIxUs2iv87WK5bnXnaqnf8zEH9y32rafwTK6bHAOVzALjBhRz42Ry7yP103iuBRXUhZwb9G4EcGnJ6JpPhr8ssMV3BMaeTCLnRnMn-kY9qI1FsCONsN82c6m04tKT-qfkztGjFcTyQSkLsII9dFShDih5HbWVsnN4cTBj3XHrYEjeny6kPOke6jhSTHZAQ15iF36FB-6YHUluCWHh_wIZR5wZcO28J9u1MBXDsqOwe6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برخی‌ازرسانه‌های پرسپولیسی خواستار استعفای مهدی تارتار ازهدایت‌پرسپولیس شده‌اند و مقصر این شکست در حساس‌ترین بازی فصل رو او میدانند.
‼️
ترکیب‌پرسپولیس‌بعداز اومدن مهدی تارتار در این سه هفته هیچگاه لو نرفته که گویا به بعضیا برخورده و منتظر اولین شکست بودند…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/28417" target="_blank">📅 21:08 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28416">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87affc8d0d.mp4?token=rUqlxPGPSEXS0T7Jp_nXHQ0hAPHv5-Ju-MZ0N4VVkzfb2jCIj4VnxpokfwRmUb-KXWADp_VpCWRoevYzWtO93PgZYDwLGB9wqZJqU3mjwMlKKxNleCR94Dge45fROzmtxqMMk8idmBr6QGFvC4A9ort56kL3QhhuUuU8zQ54YQ2bsQXDm5Hv-HFYqqYl57YuXkIFm8wUSF_aO7sW8bJ6llPeF1xZ583HeKAJSjy_Z8aqJTiNKDzKoSNWZd8N0zMoMQB2dafaIpLJvZiIA_QY93UCEawhpSfJjFf23lTL01oQhlgetC0DPJqenpBrbIgWDl2gp3GLAFe6OE3mv7sE1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87affc8d0d.mp4?token=rUqlxPGPSEXS0T7Jp_nXHQ0hAPHv5-Ju-MZ0N4VVkzfb2jCIj4VnxpokfwRmUb-KXWADp_VpCWRoevYzWtO93PgZYDwLGB9wqZJqU3mjwMlKKxNleCR94Dge45fROzmtxqMMk8idmBr6QGFvC4A9ort56kL3QhhuUuU8zQ54YQ2bsQXDm5Hv-HFYqqYl57YuXkIFm8wUSF_aO7sW8bJ6llPeF1xZ583HeKAJSjy_Z8aqJTiNKDzKoSNWZd8N0zMoMQB2dafaIpLJvZiIA_QY93UCEawhpSfJjFf23lTL01oQhlgetC0DPJqenpBrbIgWDl2gp3GLAFe6OE3mv7sE1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول آنلاین رقابت‌های لیگ برتر بعد از پیروزی تراکتور مقابل پرسپولیس در هفته سوم لیگ برتر.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/persiana_Soccer/28416" target="_blank">📅 21:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28415">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0ZWNjP-6pTDfzHRC9sCThJdfM7rM3TwOA_9vYMoNIxtPHoDvEqcTfzoSWH8UQ8TME7IoLySvfcbNitc-MSgtvxgBCo_YW0unMb9gV4kHbZrfRdYCUTGOVmWZ-Eu_DoK8-mVCpuvTSdhVTyjylXkM4mZOdSLBYpodvzTCPa6SrltGefcIIgDAUPdV-3_Q-7i1tVhSx3LirgYe0uUqLce3SN9IgPzNbugf2s2RAfaPBJwnD0IxPZm4i9-hm2DIZPX1N-f4byYiD9HAilROSB_68kgvJh8hI6AO1rJVbdSOVPt7M5d7-0Kf54HGN33xlboWfMkCT5Db39LRgPrmFJWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی خانگی شاگردان جواد نکونام در یادگار تبریز و دشت سومین پیروزی پیاپی و ثبت اولین شکست فصل پرسپولیسِ تارتار!
🔴
تراکتور
1️⃣
-
0️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/28415" target="_blank">📅 20:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28414">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGGDWjThShntWqNvzRzM7tUtu0woQGP3a40iLpOnmBLtT4igVz1JQO3AL9QGrThvvjaItNpRk2cg_FVG7wIpbqSc_dcojgyorm0GdQMlZeBJaTe1HYdfv5q3DCpwmKKQkqzoZ_uuA8qjqhyhWWz8iu9oesAAukMFeEPank_CbsJMdEmWFxiJ_ZuHCbFox64cw-LZSgO7tcBd7-PK6A6zoyl9LjAbt_tS-DcyVApSlbpgOM3a0fI5TQrJVKLWV4DGKertUjeIhJhMsHWtoEKdBnnPTtgOuOjUIZwZ9mMAgC8dYMzPMLdGjZMth5lwZaAN1cKsz3x4R6lde0i5QDeJ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی خانگی شاگردان جواد نکونام در یادگار تبریز و دشت سومین پیروزی پیاپی و ثبت اولین شکست فصل پرسپولیسِ تارتار!
🔴
تراکتور
1️⃣
-
0️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/28414" target="_blank">📅 20:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28413">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxT6ci6YAdG6YF1Ztm7rZMNlESIOIcpawJ4_U1KgGHWvIZWAqgoCDlL42Q6odGN1IsTcATPuQeluN5HpBuh9DepJcpG3hRtpE-h2XFj5-EwNoS_3yrPYTJh_AYwjL1StYHxoOPWuhwqFZjFAuyD73GgD83JinaRUrTSyqiVBijLf8w_xbYBjat847i4YVM9saQla7jRFaoRhLcRTZv1U18aTjYewKPId3C-EmXecI-D1yX1UntgXe0d0hm7UVgcOhPPaYaqAGV5YYHcaxqVxu8Pvuu7GkaPWwmZScI0v3Cx9pNdutuXQH0nGacNDbovdaa-mN4DVtxDC6x5VozRnrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی خانگی شاگردان جواد نکونام در یادگار تبریز و دشت سومین پیروزی پیاپی و ثبت اولین شکست فصل پرسپولیسِ تارتار!
🔴
تراکتور
1️⃣
-
0️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/28413" target="_blank">📅 20:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28412">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HP3S_qNxRD1eD20Clzr9FezfyUlfIXPjfEeokPSpk_El8Z3C0LE8bs-FqLD40e-rBTMs-Wz3IgRJVsOV4Z11i-KLIFxTcLEW7vgZp_ngcD-_ZEKw39VrEeo_314IG0zDHBNeHrxMifV2swwZRv2Uk7zACmT4Ciim7G09Me3Py2BuJvb4Ydn4rPlrjwztF8LalzW7dgh_FlBuTA1Jmxfk8Ok7oY-dwvQ9AAodNmslzSBi_YHSUZoYNK2-sQvzy4id00EEN46Jalxcn1-NQwbkY2YWlPaiXAiqgklaVFG9DUlTRizsselM57YviexD-nGoznsv2cXN5dOmHjhn8xbJnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار دو تیم تراکتور
🆚
پرسپولیس؛ نمایشی کسل کننده از شاگردان جواد نکونام و تارتار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/28412" target="_blank">📅 20:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28411">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8596f7941.mp4?token=lzjxfvPLY7Y3pSadaZqnhTkBUzEo5W60EPJe2auMrckfZw9xSGHU9A7Re213sWX4WHC5e6XkVzx-YJFY8F0upcEOkx01Ta9wrywt2YQlWZ1j7b7P8l5egri0LqHpc74ibDqSwrsa2sXkQvvoY1f6RFTWKwsnJNKFSSINCSJgR50cNJsZOWAbtjT7sORmZxapPpmq4CQG-0dRZPxskffCrnWvVAVjJ-hcYLn4hjxsja0dQpyuCtHBltaOLoN1yFbnZle985YWC9Sky_8R63cyEbHThD3q_aeiQMo87xfq546mPShSDlmb_0ZEiEhCMU4wh-LdgFBQxbWkZ_X5ORwpBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8596f7941.mp4?token=lzjxfvPLY7Y3pSadaZqnhTkBUzEo5W60EPJe2auMrckfZw9xSGHU9A7Re213sWX4WHC5e6XkVzx-YJFY8F0upcEOkx01Ta9wrywt2YQlWZ1j7b7P8l5egri0LqHpc74ibDqSwrsa2sXkQvvoY1f6RFTWKwsnJNKFSSINCSJgR50cNJsZOWAbtjT7sORmZxapPpmq4CQG-0dRZPxskffCrnWvVAVjJ-hcYLn4hjxsja0dQpyuCtHBltaOLoN1yFbnZle985YWC9Sky_8R63cyEbHThD3q_aeiQMo87xfq546mPShSDlmb_0ZEiEhCMU4wh-LdgFBQxbWkZ_X5ORwpBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار دو تیم تراکتور
🆚
پرسپولیس؛ نمایشی کسل کننده از شاگردان جواد نکونام و تارتار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/28411" target="_blank">📅 20:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28410">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130f6f7f0d.mp4?token=e0OX3o2UOXfGyrxk-Juq54oMfYASTbPGsworRSoQHkChn2S-JVLhNrFj6bqCoAlpMZoNSr--8KTDmd3gZIIQa2-m7MxqPwKqWlPM4zdiPw-jyciScAoZA_Z8mn_usXpudyBcN_v2ByqB-qiX9JUHEmrTTVsSe33JOM6ZaLNch_2YlSjJgfXJTVBgn9Czjunja9ggRgOhBootKR6Qrlr88zoq3HJ_TSZhoiXCNsYFZQ4tYPnQBDiKjsG6NvcPB33HDYi-Xdge3mRAqr0_FB4x2QtutAxw7OuS3GqVezFoEljrtJrxdy8cXGi873KcAJ-Wjz8y5SqYJ8R6IniDZw7KcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130f6f7f0d.mp4?token=e0OX3o2UOXfGyrxk-Juq54oMfYASTbPGsworRSoQHkChn2S-JVLhNrFj6bqCoAlpMZoNSr--8KTDmd3gZIIQa2-m7MxqPwKqWlPM4zdiPw-jyciScAoZA_Z8mn_usXpudyBcN_v2ByqB-qiX9JUHEmrTTVsSe33JOM6ZaLNch_2YlSjJgfXJTVBgn9Czjunja9ggRgOhBootKR6Qrlr88zoq3HJ_TSZhoiXCNsYFZQ4tYPnQBDiKjsG6NvcPB33HDYi-Xdge3mRAqr0_FB4x2QtutAxw7OuS3GqVezFoEljrtJrxdy8cXGi873KcAJ-Wjz8y5SqYJ8R6IniDZw7KcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از این صحبت های جواد خیابانی روی انتن زنده صداوسیما که سال گذشته به زبان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/28410" target="_blank">📅 20:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28409">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56bd5f94c2.mp4?token=Y2QdxJPs08qHgAd4YYOcbLKehkd7e9rBkk6jBwc5RS6hrHZFOKlG4JYbefGfGviJ3cHFE35S-OtXlKJz656DWi7vtF205lYEmgBx8otHLMmNAuB0LPSffpMBHZn1mHl-cpgWcDdyAFWmrJZM8FB9fxzSzEHAkWH48o4xvVa0Fagicujs4yV9mVHRdNU95iOMB412-QgqbsztHdOQk0C95r6S9qnfHdSPGDuRWFrvLULGYUSV46uulpeJeVfaN0vdvufucbMM60B6dbXauqjPxXc5p1tpdf4m8laxtQexD6kf0BN0P2YxmNQCE_M7UNYGwCG2x4DZiwDcI5wEYlA_og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56bd5f94c2.mp4?token=Y2QdxJPs08qHgAd4YYOcbLKehkd7e9rBkk6jBwc5RS6hrHZFOKlG4JYbefGfGviJ3cHFE35S-OtXlKJz656DWi7vtF205lYEmgBx8otHLMmNAuB0LPSffpMBHZn1mHl-cpgWcDdyAFWmrJZM8FB9fxzSzEHAkWH48o4xvVa0Fagicujs4yV9mVHRdNU95iOMB412-QgqbsztHdOQk0C95r6S9qnfHdSPGDuRWFrvLULGYUSV46uulpeJeVfaN0vdvufucbMM60B6dbXauqjPxXc5p1tpdf4m8laxtQexD6kf0BN0P2YxmNQCE_M7UNYGwCG2x4DZiwDcI5wEYlA_og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار دو تیم تراکتور
🆚
پرسپولیس؛ نمایشی کسل کننده از شاگردان جواد نکونام و تارتار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/28409" target="_blank">📅 19:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28408">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7_AzI-YrHLHNPKEw-3N6mqrWFKPf5iC787p9HtjI-8rrL8XWSGAIlu7XwStomvqtNMH3zXTGCNGzDoTKabqZmJh1h5P5KcZ1CJv6xVpx960W4EDxScsqFwzQF77KEnchPhtu4ifVSuKpgN9lBTi11liLqPtWbc0t4bpyzvDIIZccMzLNmh5wn5dgbs03HcNy1GhOBcY5sK53M20Npb_gkVJNNG9agKM0qrySUN4Qb9nQxiR3Tl3qyOX3uWZ0SkfzTN3z_8iqdB8W-QJTAO8F9F_NhqVaumClzwsxuqpSznP_9fMU7HHb8P5CKQi4wBiYLT6yvfpf_lQY2605SBq-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💵
🔵
درامد باشگاه منچسترسیتی در این پنجره با فروش ستاره‌های این تیم: بیش از ۴۰۰ میلیون یورو!
‼️
ساوینیو ۹۵میلیون‌یورو؛تیجانی ریندرز ۶۱ میلیون یورو؛ رودری ۶۰میلیون‌یورو؛ عمر مرموش: ۵۸ میلیون یورو؛نیکوگونزالس۵۵ میلیون‌یورو؛ جیمز ترفورد ۴۶.۷ میلیون یورو؛ آکانجی ۱۵ میلیون یورو؛ آکه ۸ میلیون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/28408" target="_blank">📅 19:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28407">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2y4vJdCHc-Yxusr2tFVqpmZEfJ7V5860GdAUnFWqflBEcOLhcavMqhdjjK3QsMpMlErYGG8DoH748qXf-eRzTperH8F3x7fdqYkmhcaH4T2Bz2KulYzodDlTUFx1UbG9gB-mmnl-Lek3XCxczs3iRAU8pUdTAYIVZg8NHV-RuIPtAVvWzUxAdwUkcGNkj2qNz7sVS98BwJs6x3WkicFypy6RRRp1haBmxUQjGiERQLfw2aVVrj3Ygtit395RubLIfviYW0K6o3Z8Wdtn4dx5Txw3NkUI1pL3MMf-Te3qQeGo_z2mivUccZWpP3AxC6ArLLaNtxIGtX5s6EuZvrLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔴
🔴
شماتیک‌ ترکیب دو تیم پرسپولیس و تراکتور برای دیدار حساس امروز؛ ساعت 18:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/28407" target="_blank">📅 19:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28406">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKqazKyWpGW99q1_V9NbdXInJt7p85AYOqGs7ERCv__RHU17a0pREEuT9rfXHAXh7FqfN44-metPNnEF1UFQMeR8lS9O926UFaBeHS8rorZudsgiKccHHYgFtM5a3JI8zdHklaF5jGPYhJWbLAlyR2VFI56xY_Yem0jcJ9eOArbijyxa9os0_EnM-0vVKNK8Rv2En9A08sfEvgWrJV6Vr7O-ZtNth86t0I25Z14eva0VldTN2dKZ8itkHsv8Z52LZq1tj7OnoMANQRYb0vFvdteW0Mzo_qMHl9pEXT3Xvwd7nzzI4-Ormxcr6NlX7ltFyI-2E5jZdUZeqPZVVmLq1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه استقلال طی روزهای آینده 70 میلیارد تومان به باشگاه ملوان انزلی پرداخت خواهد کرد و مدیریت این باشگاه هم رضایت نامه بهشتی رو برای آبی‌ها صادر خواهد کرد. تمام توافقات لازم بین طرفین انجام شده. بهشتی تا نیم فصد قرضی در باشگاه…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/28406" target="_blank">📅 18:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28405">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NERw0dZqq4LxiE1bg5TuDRxn2MwFT-XODh3EBKnYZj7yfdXLnuYZ553cPg_Qlt5GPGGhHQDceYcadmEjn_OiunFK9SUPWtDPOy2KYccTwy5HlW_h-R-_VTv7LUdAI_7zKI_BhpagRjhqCVzUUDgkNlCKjwJHV1PfxSroL-MmQs5KxICYru5gW20xAW5FpCQak-ErS4oB2eMqUEkLXmcRKGNGbTfrgG7XWklfoNpr3hLx74n17x0TlejMmRMvStCEHwLtdnzEbc9QguyrnbV9kIPfULmdkbapnGqCcPZa4PaLq6_ndG4IYcvk99tvunk60Gg9J95blWYLzmY48iJaew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیاناتوسط سازمان لیگ
🔵
بااعلام‌رسمی‌سخنگوی سازمان لیگ؛ یاسر آسانی یک قرارداد دوساله تو سازمان لیگ داره و الانم داره سال دومش روسپری‌میکنه و قرارداد جدیدی منعقد نشده بنابراین هیچ مشکلی در این باره وجود نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/28405" target="_blank">📅 18:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28404">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNILLhO27Scw_ielWBxz7t7iSqqXrnoP0obc2u48mNR-DZL0QxWdt_pCrEqfy1AOxhhoCxHxb6f2CN3Ie1Wj1xAdZD_HkFfG8y_X5s0QamOM08a-h2aXEZSFc2VkzC27zyqthSHBNdqox-Uz73gjECkEiSk7eucMpDaqVSseT4KneMHUFziSfOs2YPvWrduQcKsiOdoQBcqqoivKEGAGWkT_5Lnmy8QjQIlF6nX1v047qAjpMXXNs5rZE0BbPHTIfaL24zn9rILw1bU5NLhB481MQv93J_0wARVVZCGwo0cFJdYDSbUyj9KdNEo4W5MgOwkUkyiINUYSfQavMHoQTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
آمارتارتارسرمربی‌پرسپولیس درتقابل‌هایش با تراکتور: 25 مسابقه، 13 شکست، 10 مساوی، 2 برد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/28404" target="_blank">📅 18:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28403">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-01NUtLWuPHqB0ejRxbLrtrRNwCQS2wUfL4Wm_OMBc38WwH91E_O6Mmsn4ehue5dVAnqvtbShbyD74dCmxorWPizXm9YXmgkMa-nA6phNR3BkeuSn1hh995-wogkkrToeN7zXWFdUqLk1PGAtFmljzoGOuIPMORGoDr4Lcl9R80CZvHJ1HKoOvx_QMtJnOZaUeaTrRysM4FDxVpPjQ5dI88Rg_6RjyD-J4uQqTzzlF-RRvN5YqoFCSrOE4b5IqTYzMlNnGrylvHxFATRUx3wq5FI2c9hhrNEXF-MF0IXIn8-JkyfbVzyTX81WXHQ13rPSKVQB4uge6aDdk5pl677Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نشریه اسپورت: باشگاه اتلتیکو مادرید آمادست که خولیان آلوارز رو با دریافت 150 میلیون یورو به تیم‌آرسنال‌بده و توپچی‌هاهم برای پرداخت این رقم اعلام آمادگی کرده‌اند و حالافقط‌رضایت الوارز باقی مونده. سران اتلتیکومادرید به آلوارز گفته اند تو رو به هر تیمی که…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/28403" target="_blank">📅 18:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28402">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRv5Ruy2p6l4pDGO08ZDMEzmseKh2wSLOgRQjHnC13y82QcSdse9ubFkgbsjU03eNkrWpJ7jFn93uC13Vkc58Ni__iyKs4Gj1gvL1YIhEDrFSH5VeNsN1augVSfa8-A7P4Nr-Fy-j9xCRTppbQ6RHcf6uNRRnKLESqz5h39uYcR8AiZZAN6_KtcgCroG6ramiNn32rHsa-a6wy_27TcsXLWlD9nzY1SMNGEIjm4lgsqG-QLb2C3bLpc-VAyPoqZB3Kf3zsuZFW2GZp_Q2FVUz79p-9_EZmtbbU-MxPZCX6bMwBDepaKzTW8bY5ZfsRdjJYQfk81yPGNHyTsNoLhC1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تا ۲۰۰ میلیون وام بگیر فوری!
🔥
‼️
با اسنپ‌پی می‌تونی بدون نیاز به ضامن و فقط با یه برگ چک صیادی تا ۲۰۰ میلیون تومن وام بگیری و تو اقساط بلند مدت تا ۲۴ ماه پرداخت کنی
😎
تا ۶ شهریور ۲۰٪ هم تخفیف اشتراک داری
🤩
پس همین حالا از لینک زیر وامت رو بگیر:
👇🏻
https://l.snpy.ir/zj65d
https://l.snpy.ir/zj65d
https://l.snpy.ir/zj65d</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/28402" target="_blank">📅 18:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28400">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pqQEdChxvW8xEgBW3AfVjUyRIivqEGIQcEuPHnbwk-coQ_xkY1nprFJ2PWkCycK0am3RmPBDjKlBb6I0oWbJ2fAhF7hr1yHFecGnxW9fgCEsWaT9Ak8yBHkyydCub501TCDytWHpsN8NZyJBYEG3suTNlAOwHAEoeWbc6wT3BLBDlXzUdwChOiPsShGzThOPEaJnX4NFx4u_wnRLM5znEMBh_eY9TN0RnIMx406O1cf5t7gRlFH_zxUk4DPfcw7X35qpPpqpRAXyI86mBn2nh-X6hD3l2O6J5wb1CNqCdHALTfRcbO315os1Rw5ApfpbpgDSOWCGax7AgRzW4hlVwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JLe8KsMwOkDZlFx0S3E34ZAytL0UPXarfIMfFbYyFha01cSImqLpkzxPUIfhjIlSePWeF6TsBnE7MOz1get8hAXGaczkUIn7BkGBiBCOPKULFzRDx3DCzPMGHJzQp5a99SSbaEyLFyPZqUBE5qkx9WGr1oe4p_WnPMmXujpVUN9G4e1tHpvCam1DX4WlY0oSkg9ITEyS1PGuhoUM9PGhj9gxDgdN9Zz5ujZauCtIG7RzIbZ7VmRxWJMTw0BVBm4zYkDVQsSvRQpB6wCjeoqVJ5yuJenk37RSywp7QxPQ-EQoLGZyq-CNud7lmX46NIqe8-hyaKRqbXMh-y7zFbiBoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته سوم لیگ برتر؛ ترکیب رسمی تراکتور برای دیدار حساس امشب مقابل پرسپولیسِ مهدی تارتار!
🔴
علیرضابیرانوند،شجاع‌خلیل‌زاده، محمد دانشگر، مهدی شیری، دانیال اسماعیلی‌فر، محمد نادری، سید مهدی حسینی، اودیل‌جان خامروبکوف، امیرحسین حسین‌زاده، مسعود زائر کاظمینی و…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/28400" target="_blank">📅 17:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28399">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s39ORoxwWykrbnzmJwW0Z363DYfjXfAh-_uihlkYyepUKSw_-uCBOrIFcVT9eRO2qUe-cn8PpdlKI0cYB2Gf4pF9CZC7e7iZdbsj9ViScITge7UVmIUZZENpmKc5RqWtzHDejd9cf6EWIu9GFV_NHVD7oaKyzCveWuIYna5mL8fkPfVIYuEYrPi1SVZq_GaNU5A8bxIRJYFEjpl7eg8I4rGps6g6_Hys-VEhny9sLR4Jii5Jvh_Qj3zD88Hn0c3biRJAXYWrCLk8AxV4clYhFVfBtZCK54OAfb5f3TqnYOv5Ai2oaHVVmB-BFTctRWtBAUNLUgIUVLZ-92vCFNR42w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدازجلسه روزگذشته مهدی تارتار با مدیریت باشگاه‌پرسپولیس؛ سرمربی‌سرخ‌ها تیوی ییفوما رو از لیست‌مازاد این‌تیم خاج‌کرد اما روی جدایی دانیل گرا مدافع 33 ساله باشگاه پرسپولیس اصرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/28399" target="_blank">📅 17:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28398">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfu0sstxDHIzZkHyj-EzktyXLB-KmnyFuc4KhJNKafR93ZVLNisGwg4Ybsf9-xT0u1Z5Y52zol7V0Gjyn1Plqahu8mJKXElhu-IZI_fdH0aslVr97DPEyfFDrBuOxNdZKOmbw28BoKemYHAx6hOTZr1g3a_t1cszVIotXuFNF3tiQDLL-9SS1GLnX-xCvt3Qt0qKfwBGlIMfhsrKj-4X05glCCADUjWn5TKAqeW5smQ7jhNLF8lDL53X5AD-HE0znsiq1X360WpylKCb-grJ9KanlhED4G-5KpKlSaf4KcVmlVj5TGL6rZ2HEsTCssFIhxHqitOQnl3bh_beP5k62A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر؛ ترکیب‌رسمی تیم پرسپولیس برای دیدار حساس مقابل تراکتور؛ ساعت 18:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/28398" target="_blank">📅 17:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28397">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lp-kQt_-W9qJlPjoAL0gY0LPWs_n9iyYGNP3AxRp45BRUbLNuoWl1M_ZXESzAzecEFZwgByhZ5BybpcwTSSfJtHggHC4_PENN8irl2lFQ1xvh1pulm0izGoJF6go0SLLIa7ytdzVEAK8KTbktyzMASkV03bSoHqHK3_A_hu8v62gOF7DO4fQKsgVqAd10gFVx9p_cmrJl-meNNL0_Q6L2yBxocLNKk2RMrLRgRbTvIMwJ_QKBhk-tdY6Hhn08-qE45koSbjiThhA5yVaIPOLB4fIXORp-YHzM5kLtvikLfEi0whvFE4c_AXCSrxYwl1z_vimsXQVnjxK14lXjTM2Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته سوم لیگ برتر؛ ترکیب رسمی تراکتور برای دیدار حساس امشب مقابل پرسپولیسِ مهدی تارتار!
🔴
علیرضابیرانوند،شجاع‌خلیل‌زاده، محمد دانشگر، مهدی شیری، دانیال اسماعیلی‌فر، محمد نادری، سید مهدی حسینی، اودیل‌جان خامروبکوف، امیرحسین حسین‌زاده، مسعود زائر کاظمینی و…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/28397" target="_blank">📅 17:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28396">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBt9fHqkPnWVKqfAkh1e7ksV3eSGX5X3FszemTIelLcJFHF34QSWjLv6ySvo0zbyDAA7fgfE5yYximfvye1uFizhzijY7PJYyHVBw59goPrHDePWPo8v1P4R8DVILtpcwInNSiJfPHmIEVR5LMZZSXKzsMhzUReeGLMD5bjIzQgeULEsn3PrZX__LBR63bO4nyJRvqLQA5d5rgnUh5sN8xJP0_C1hGBt24re4LcVJi0-Md99wCRBZ4XJKPfz2L08r835XZqIzlMWykKyonCb63DKliVg_nZii5lPovGkzPEqp3jvKEsKylhhii0FfcxestCg4Y7tTjl8m_VHxmVtRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌هااز تبریز؛ تیم جوادنکونام فردا با این ترکیب بمصاف پرسپولیس مهدی تارتار خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/28396" target="_blank">📅 17:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28395">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlNFLaLAt2itIFO97lofbOBUqxUK0m5ENdAbCzWk99wEEOc4soIm9dtudb2aq-S9GIXzsF2wQ84R6f2esCS0Gn5Su1_4TIvfAfx8mXJ_e6gYKn6sSm28IAMCVB6QVmtiRLQOsEfaWtleGSz5hK4bFhTHkIzQGGJmMDsMFwZ4PIymQDX8Q37gyo9NDgmUleB2ASJJJHRKpsbeCP85O-Q87Bxqcso2ByZqMqyOFrhSI-eh2KX_fTCaw6CvJgnwNTm8S0stEAbAemeTznYwq5Susop3IIc0OiE2wooq5hE6SGIkwxzoa4DmN8Aw6tzhBeDMzTqDqdNppIT-fplPyxwwFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ توافق‌نهایی بین دوباشگاه انجام شد؛ نیما اندرز مدافع راست20ساله تیم لگانس برای عقد قراردادی پنج ساله با باشگاه استقلال به توافق کامل رسید و نیم فصل به این تیم خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/28395" target="_blank">📅 16:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28394">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EG5AaAv39ylkAQ7871F-Mlh0Ix-Ud5XAOg1gNKGt1TlhUwfAtr5x6rSJI4jgeqz1ksbRUJgA8qP3h704npRzfYATXTFL1FIU2kwkcMrNIi-idjqKhD72IYECLiFwStmV3Nnn9JSG2V5cbIy3fHGKMek1TmhX3KYJTAHrVOiWL7XMLN6gBC5tCrjVRuqcje4lCIkWzN__rkipJNuUHxX4N-EbaWCUqhX1xXh0FYFOLRvSvY_0hsZyg0penaoRBzm8Q0uSVdd19thdthBzvedREmlmMaGQyKIagagZX74hTKLKO5pjm7M3N0Hr2rnVJBQob5wlehcQxGrNlXQUAIylYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ویدیویی از مراسم عروسی شب گذشته گابریل مارتینلی ستاره برزیلی آرسنال با پارتنرش؛ مارتینلی حدود 8 ساله که با دوست دخترش بود و بالاخره دیشب باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/28394" target="_blank">📅 16:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28392">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIOzZrhw5DlF6FhCY0ytenzQ5ogBIjt8v31sdA-nSReipWaWBNeIi5zh6rmiqgY0Abm0REIf2rhGfx-SqZQQ1a1kI213KMiyBFjIqal3aY7_FOIp2Xc1ucyj9HMynZucZ2QmiSiBJBAWuuqFB71WxorR5pwn1Hs6ucGUo9NkIDwzTjmOrgFr1OFldGzOTU7_vRdyMXafuyRl8r8bSWb0s2DvMlCTvvetcFO9-45_qzcDCvzDnDUp512IMHr8papgbWAF6boFT7YvGCpEZIZ4bFpgzX36gTfZe5V7gHcb8-G-9dUiGiBrlA1IsLxD7KgqspP7fB8_BzYICyIJa9GASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
به مناسبت دیدار حساس امشب؛ تمام تقابل‌های جوادنکونام باپرسپولیس درتمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/28392" target="_blank">📅 16:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28391">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJvuwoLDm8zl_BCJudBEQCD3LdI-PuMUBjh32i1r4SU__MMTdtLE-GV00O_AL2rI4V-vLpW8-fCs2IUXUMla_W5Wm3dYxS4c3BMylcEgp-zWwbOH1MBD8bGxeHsa9CNyynixn6q_GtaMAB6ETQsaFLLKtd8h-U_fyYweBF4y5phZ3d399Eolh141Zb7-othq_x9gu0N4wsodS0ASHqWwfk5akjJR1fy3Fkwtbxpdx_0r393mnj-4FjedrkeEUSIx7j7wefnt7hYpdtTwqrK6VIj9LTroIO5cAom60nckp5vYsf_7aeheb9BacT8iX0YVKmwMFLFmG4VTR-F-lNviXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
جوادنکونام‌سرمربی‌تراکتور به همراه نساجی، فولاد و استقلال‌مجموعا ۱۲ بارمقابل پرسپولیس قرار گرفته و آمار دو برد، چهار تساوی و ۶ باخت را دارد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/28391" target="_blank">📅 16:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28390">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j084czcqDT7oi-Xc07SpT_oQ206CBY-A4VgC_dED2UtDT-zHH1bSV97P7bpKt5AfX3A3CgeRrBYxDPCwDclU02KT-uA8o-fbcVWufCiYhzgehEFNl5Zj5b3SEOZwrByL4Dohr8aS3sbLAGxX7yYIbHZxAiZ-UnVNAzJKQle1V-7f8aSR5a-SgUteRRZz9-QV_W6b_3mIBifcdh76ACkvom7MZeanumWvRypyMKzPWlVaZ7YGhOEi8DDoeySCwe4rAuw8-fV9BWC8GvG-Ki9evkvBRYmXDkvzNtuH-Xn5X_HOfNDDz-Huw_eOuaiG1cRaYUulcfGB8BDKPbl0jjX5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات|اسپورت: فلیک به شدت علاقمند به‌جذب سرهو گیراسی مهاجم29ساله تیم دورتمونده. سران بارسا قصد دارند که در ژانویه مذاکرات خود را با مدیران دورتموند آغاز کنند. گیراسی بند فسخ 50 میلیون یورویی در قراردادش گنجانده شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/28390" target="_blank">📅 15:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28389">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPbSR8pRMXgG8AaQ7NPzM7olcQ6OQq7reiE4VkDujU9vk029Hgy61PBe0WveRnwzRa0Jw-vASiNYF4J-uFZPITUbV_afapc53ubl5nxZSPHK5Y50WB55Bn0L0iOnOOSkpT9FIjDZ58yh3D6b6mcznCRwkG_rkCH7-lpEBwLosqioZD1izv1aDhZWqhkDB760Ybr1EDF2I7I4v2YoQYyBTar9Ixna1jc9n6c8HnBdiBRy4zWUG_jQENwki6ZExss02n2CRWobbwwOfRqnPygNeeoo7lBxTA6OmmKex23RfPR0pifaoLAWg06G13wqB2oIE2RdSmvPomGHuHo2w06iRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
رستم‌آشورماتف مدافع29ساله‌استقلال که در بازی شب‌گذشته‌مقابل‌سپاهان دچار مصدومیت جزئی شد بااعلام‌پزشکان‌این‌باشگاه هیچ مشکلی برای دیدار روز جمعه با فولاد در خوزستان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/28389" target="_blank">📅 15:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28388">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjRT6cmuTbip7yZSMs2KR9nNjBNaRQ7AUeOAdDsFdNlTbZpeiML8rJGX3N-5OkuL_evNQI3Dmms3dqeHsgVD2zHMJ3l0UVY54apRJJWbv98MBXBtU-XZwyQYfv5CGimBJKCLAQIo7jbJH2uqskrJapCBP9Oca3kuiSZJHp3Z23DtHHjJGbbjw6nZQ_lwo6fwHBFXmHAG-ARGjx5vxxjbZ5vvnDMNi8uVZJuDdm6VtmaERP9PpL8PBw5dyQS3w1bZQUpB4bfWXToxX21ifOkaIiM3LGu21-yXXwuPZNffDVEonUVnu3OChrLazGOAGud6QKA4152GNkSICzJPs1m4Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ایشون خبرنگار باشگاه الوصل هستند که از این به بعد در پایان هر بازی این تیم در لیگ با مهدی طارمی ستاره قناری‌ها مصاحبه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/28388" target="_blank">📅 14:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28387">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuuqSS8V4hsf5LlocNnkrsywf9-USKpHIj_w6nUZU3gS5xX-1hkjRoy3JWpqCU5TjB1ahY-6IcfccABIgHociAoB9CoMFYcafVyl7xEnIUm1XirGqDY2LRgu3npA9-pFv40syxWdTVWoqPtQQF3s21QS4Cns0LnCsytv7VkOzJYxu2NxCaKnaCw0RW-u94Yuy30CSfZvVBtqQ9h2tn7vwd4uE7jhsCazidqUwQWzRW-UM-AfHTB9hjTK35UvEzMkL7oQJtqd3iqY4eX1injRn_oR46pTHRrP4VVObBUaRRfEVo9xd_h9WbUVQYk0QEo-tP7KhbC1e_zmY2nx2qdfcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خلاصه‌دیدار تماشایی امشب‌ استقلال
🆚
سپاهان در هفته سوم رقابت های لیگ برتر جام خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/28387" target="_blank">📅 14:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28386">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4ca0f39b.mp4?token=JpOOk9LsZjUl_-DyTTBYybqKGAGX7c68TI17vsmv5wgIPqBJMgPOAY88MbQkqpduHi8h8VtW3kDQgP9h3TL8tOKyF0xi0--ykDO6_VA0gqFODYyLsudfFlfRg7-e2-sO4vicX0arb4OYEJm_OzXvygrMhhEWi0rDoTtSRDSkWQ4rGH5OW_mclthl7_q4THl8Hbs3wzvn4YFvcyiBzbJCUijxSoTMRwZW9UCQtjmZutjzYrbOjhN4jcWy6toPH64VvhRoZYWuv3bKrqdg3CAv3j6dqZ0YhvL2GKZpgpQK7GobaV38KdNsIXdhk5xOSrVkDQhAW7C90-A9Do9Vm3YPYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4ca0f39b.mp4?token=JpOOk9LsZjUl_-DyTTBYybqKGAGX7c68TI17vsmv5wgIPqBJMgPOAY88MbQkqpduHi8h8VtW3kDQgP9h3TL8tOKyF0xi0--ykDO6_VA0gqFODYyLsudfFlfRg7-e2-sO4vicX0arb4OYEJm_OzXvygrMhhEWi0rDoTtSRDSkWQ4rGH5OW_mclthl7_q4THl8Hbs3wzvn4YFvcyiBzbJCUijxSoTMRwZW9UCQtjmZutjzYrbOjhN4jcWy6toPH64VvhRoZYWuv3bKrqdg3CAv3j6dqZ0YhvL2GKZpgpQK7GobaV38KdNsIXdhk5xOSrVkDQhAW7C90-A9Do9Vm3YPYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز اولین‌تیزر سریال
«مرد سه‌هزار چهره»
به کارگردانی و بازی مهران مدیری منتشر شد؛ مجموعه‌ ای که ادامه‌ماجراهای «مسعودشصت‌چی» را روایت می‌کند و قرار است از اوایل شهریور ۱۴۰۵، به‌صورت هفتگی از شبکه سه سیما روی آنتن برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/28386" target="_blank">📅 14:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28385">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaS3dIpuJ7eEncJ0SOcJCN7LNsQwkKLqUMy5nOKFpNy1U4Qc5VGeWIs60oUZ2vxH-FIQBbr_ddG8DHkfJf4B6U2RpEk7omHHfw0Dbsy0rvQn3kPfSA2pL5BHb5Oq_MaEOxaI1S5YqpcxlfjhQ0dbM2mjgi-YxsPQUlLxWTONPHlID2mVCF7L1EGbwFJLVzhsyndn_Yh55KNnEbpFZSGimvh4AM86HBmUcU8HMR30RgjvwJOFWjNLdUlEE3Hvn1mLLtPNoAZQatQwDwfkyOXoidHRW6sQDCzOIJZj7tftNF7jkhkNnu5gM4FDAji-2Ei_chBoxRRNffLERvJV_N3Tkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته سوم لیگ برتر ایران
🔴
تراکتور
🆚
پرسپولیس
🔴
⏰
ساعت ۱۸:۳۰
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ ‌‌بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/28385" target="_blank">📅 14:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28384">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQBbcEiHDQCHt9xcc2aIo9OK3O2Ocxuwu8RZvQxA1bvvy96_yniVtqps1x3jkO6G3cBOkR8TGOClKAHjZ6WPFvtxo3XfFwvsKn324tGIdYYxQL4a7qnuFxcAuMRvcoxF2INhh6x7bX7qOhprU5OCRSmsxbNZ5vCKJy0s-lf7Q1aiFKPMGCZ5N7TuQBey6mlZdUz_L26VCcDgrmiVwI4b_VUP8x635tG4fMqxoloxYe3Sdq8IBQ225PK8vXJf_lYF07mo3bXsCJIVL4RTXromQw6emyFRoM_mtUzrDDliMMcGQ7IGmPycFGKU3JzPEKgPOEN_q-51oS60-ne09aeZ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری دردناک محمد فرهنگ یکی از عکاسان زحمت‌کش فوتبال‌ایران:
دلار شده 204 هزار تومان! الان من‌چطوری اعتراض‌کنم که بهم انگ وطن فروش نزنن و از کار هم بیکارم نکنن. خداوکیلی دیگه خسته شدیم از بس دویدیم و تهش هم هیچی نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/28384" target="_blank">📅 13:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28383">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGgXQhtvrhccuFKesIeMjhAcibj_gBH5j1wBqtZK4krJ8Wc90PNiMZdNRJbRR1ipq5gGYd-8fhxJjVSauEVPVKROM9x8jnT6J1bD5nqMPd1oPOtG6unLjl8JUO1UUhOW2c33UlMKANR2vpB0Iua8MjwcVa3EB9CSsL1cBe6MPS87JK5V5lMWj3KBMOIr9gNw6suD6khgD7CzyirbpYU1770Bo1QZWx8_T9eNNr_X5MDCRQFb1VvxYk2PPIlvKMFCJPsR3vSba4fzv3pIR0Q86HIGdLqoqSKpGEVpDlJfLhb5EyUAk2gJwTWb3u1YdKRzWjMZcUSOi2vMBovAAnNUWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
عصبانیت شدید هواداران اتلتیکو مادرید از خولیان آلوارز؛ستاره‌آرژانتینی‌اتلتیکو دیشب بعد بازی باویارئال بدون‌توجه به هم‌تیمی‌هاش به رختکن رفت که هواداران اتلتیکو بشدت علیه او شعار دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/28383" target="_blank">📅 13:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28381">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MC25Laqcpg88daltE3B82RXRTm41fcWp10QgWb2xMfMh2UHkVHMRzf9YffwhXZW6L7gimpBinmsle0G-cFKvqzuS6szizxOQep8QYKVa7OBfOn4puF7rvXKRL0NFcKrNZrcjpDLddyBa5GDfYpaKXi5KgXK45s-AaCmiKUl6VO0-Ny231OcZ9K1GsXqz8IyLETMQlDq4MpVZuYv02NE2PziMR2Ir43GPvCa3dJIcaYfSZmt6nQ8gYnxUxDf-S_hOaVy3SKzVtkyE_AXLkp4Ul3P2Lm8oU4J7FfyIh6yQs9BfFORqgHAj-5u9p3Q0KPFV84rlyIEjA9D7rlHWzTDP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WxbEwevLWyn_uXG_fTjupy2TQAQEz9ZB_Oe1-64Bht-wohFISOxkPfD2VvYRN5aMVsj_c_iFhG1ZilHbHapiTPtqx4Mj2RVDZBa7m26lrCh-0-jLnOFv5KjZmgYYrEptPUVTXqiNWNqpkV8ApNzARnYGOZFYlBfE6FdKZk339qphOgNU1jNjKdB3Ff_JpTjee4fzg5zHQGQTXip4607RbLkn_0g7_LUPV9HXhfhxvdyV6m4NWZ0Ns_vrRz958J0kx_2c7Cs41-E48og61WcZC4ytrTGRatvr0RQkK0G7zdvRQ9GhDQULx_7uKIddmCSNgpNUR0rijdgLoK7IrvFJIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
رافینیا ستاره بارسلونا که از ناراحتی خولیان الوارز ستاره‌تیم‌ اتلتیکو خبر داشت دیشب بعد از گلزنی این خوشحالی مختص به آلوارز رو انجام داد و به نوعی از او حمایت کرد تا روحیه اش رو برای ادامه فصل بدست بیاره. آلوارز خیلی دوس داشت بره بارسا اما مدیران اتلتیکو…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/28381" target="_blank">📅 13:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28380">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad50390910.mp4?token=Bt-grxW2uZmKTt__sK7VQ-bhNmiZbBqXqhWuotQyTh3WdQwTegPZaXCGidl6tGfQPI1QdlC2y_g-mu6Jr6q4XZ71Ngyxo_wHZXn9n9qvHlUtLch834O9B79F0nnHNpxmqgW54gVrm7SSkRNAQVt0B2TVOAW-FoSb5uObJnX1kvNc9vGxt8u1EL-XnFJiyFRs3Z6yulsp1Oks9BH-EFdyYhleBWpWcQkdhlfeX1NkUFO7NxProM9_6oS9M-dKELWWt9t-YRCA7nHDukmVFyoad4A-TrXnAHXYKJ4eaEQe1LlCfNUNQRYbN-b7jtVlg9PICaR-0yBURxndN4UVSA-r6IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad50390910.mp4?token=Bt-grxW2uZmKTt__sK7VQ-bhNmiZbBqXqhWuotQyTh3WdQwTegPZaXCGidl6tGfQPI1QdlC2y_g-mu6Jr6q4XZ71Ngyxo_wHZXn9n9qvHlUtLch834O9B79F0nnHNpxmqgW54gVrm7SSkRNAQVt0B2TVOAW-FoSb5uObJnX1kvNc9vGxt8u1EL-XnFJiyFRs3Z6yulsp1Oks9BH-EFdyYhleBWpWcQkdhlfeX1NkUFO7NxProM9_6oS9M-dKELWWt9t-YRCA7nHDukmVFyoad4A-TrXnAHXYKJ4eaEQe1LlCfNUNQRYbN-b7jtVlg9PICaR-0yBURxndN4UVSA-r6IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه‌ای درحاشیه دیدار شب گذشته استقلال و سپاهان که لحظه‌به‌لحظه داشت عجیب تر میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28380" target="_blank">📅 12:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28379">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbc809efb.mp4?token=PMMyoD7mhHjLdqF3NzXBFa3uZ7LI50r6Khs3CEe2YFmBmzYy4IBZX5EJ8nQyv-DtUjM34oIMv41gvrD5UDQpO3-ZPBX-gZm-_nq8Bxu0_YrLXqe-vBQz7YEsU4tKeSwUJ_ySoofFgdQqFw_yY4FMS4NKtn2Up0QDPK5MH1oe_f2-VX6EksiQ4WlqgaSG7Kp8TZQJK4F4JrE6oSoGoS7pXzWeZhrtlduDEX9h6xLcvaL65SIPMXstG9iYulKKkoZJPMkHimbcu2Wm6X_140zyB7w2mdO4fEYZWPZXoFCoGEMv_eh6-jCPQUmVbw3EMLvOib6TccD4TI3vA2n5lBvkKIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbc809efb.mp4?token=PMMyoD7mhHjLdqF3NzXBFa3uZ7LI50r6Khs3CEe2YFmBmzYy4IBZX5EJ8nQyv-DtUjM34oIMv41gvrD5UDQpO3-ZPBX-gZm-_nq8Bxu0_YrLXqe-vBQz7YEsU4tKeSwUJ_ySoofFgdQqFw_yY4FMS4NKtn2Up0QDPK5MH1oe_f2-VX6EksiQ4WlqgaSG7Kp8TZQJK4F4JrE6oSoGoS7pXzWeZhrtlduDEX9h6xLcvaL65SIPMXstG9iYulKKkoZJPMkHimbcu2Wm6X_140zyB7w2mdO4fEYZWPZXoFCoGEMv_eh6-jCPQUmVbw3EMLvOib6TccD4TI3vA2n5lBvkKIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه بکش‌بکشی راه انداختن دیشب بین بازیکنان دو تیم آلومینیوم‌اراک
🆚
شمس‌آذر قزوین! اون یارو تدارکات‌چیه به قصد کشت زد تو سر بازیکنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/28379" target="_blank">📅 12:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28378">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMq34RklWsXOdOzivHJOZUYbTUU-m1ZAWf_fC8FsSFZGmzImcJPKRl0CIECZz1wBA4Fx5MmqaPvQVa_5DzTT6X_b7FqriZiVp_8aOXwyF4UmdFZ_fZm7fJOcYUGlE5-nBJnmkcswJqYbPz2r8_EF0gDlLnqk2AxYGfQgRopkOLx6YQQqvnSz1Nsm6ejOQZl_FptoHe40Zpml2hdW7x5d96I0Mipv5jR8_gsDKC0EQdEyramm07ueYFlrS9W7T8LwFKjgkdMb3Chx3wN2bBJ3I5AcOmbvTtts1_ecJcIXPccpFgPLebgYgmGmQYQ6KXYnFdzDbQklr05C9XBwuJqKGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
#تکمیلی؛ جواهر ایرانی بابندفسخ 2 میلیون یورویی راهی فوتبال پرتغال شد؛ رونمایی بزودی.
‼️
همانطورکه بارها اعلام کردیم باشگاه ماخاچ قلعه قصد داره به هرشکلی‌که شده محمد جواد حسین نژاد رو بفروشه و حسین نژاد اعلام کرده بود که حداقل تا نیم فصل به لیگ‌برترنخواهد…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28378" target="_blank">📅 12:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28377">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a084028cd.mp4?token=teH_JsSIMGizLPgqNEiEjRRko42Y5Skf9kFG5ftVcSsQ4vVCte-DgLVOTg8PxTcn_K1_mpUb4SOdRvFAC6vh1FFzvqcFAS11n_OSQ4S2UVgbSfpiApS61d1XF7W2AnJ1Ktgg6ROfRfBo0qu-pX7-F50xW1cthO3E2KhofQOkwTai8Hw5epDKNrFVZjzOlTniOwh-9htUq2Jmz0xZaGS-KQCuHQoT39rtlCKfyCMncHYuuSUzsisjvJK5neiDRtSl5VURpzzcJIX0Od5dtOIUxi0-enOQufv-I4brGn_zcswhdaOy6BFMev6PLplkYdC7M7SqIZYkItfY09g5NaKGyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a084028cd.mp4?token=teH_JsSIMGizLPgqNEiEjRRko42Y5Skf9kFG5ftVcSsQ4vVCte-DgLVOTg8PxTcn_K1_mpUb4SOdRvFAC6vh1FFzvqcFAS11n_OSQ4S2UVgbSfpiApS61d1XF7W2AnJ1Ktgg6ROfRfBo0qu-pX7-F50xW1cthO3E2KhofQOkwTai8Hw5epDKNrFVZjzOlTniOwh-9htUq2Jmz0xZaGS-KQCuHQoT39rtlCKfyCMncHYuuSUzsisjvJK5neiDRtSl5VURpzzcJIX0Od5dtOIUxi0-enOQufv-I4brGn_zcswhdaOy6BFMev6PLplkYdC7M7SqIZYkItfY09g5NaKGyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمدصلاح که‌سالی 17 میلیون‌یورو از ترابزون اسپور میگیره در اولین بازی‌اش برای این تیم چنگی به دل نزد و چند سوتی داد. بقول حسین حسینی از شانس بدش توپ هم باهاش همکاری نمیکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/28377" target="_blank">📅 11:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28376">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔵
🇳🇴
واکنش‌های جالب جک گریلیش، پپ گوردیولا و زلاتان ابراهیموویچ به‌مدل‌موی جدید ارلینگ هالند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/28376" target="_blank">📅 11:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28375">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ta9fyESqt0hzlvVzgDJXJItdTux8kSsVLaJ47U3Ab6v1kcKstglOwjZhDeTynuBfrc0Q9j-JGR9I2teDP_6cp8OjZSsaGJ9vTgOJHaW7dW2HX9ZW3Hqj73j8tM6TKKn2XQyNAYGS-cnxxe_NahgwpAYFlZ5N4PA9m-dH8bnLfxRCTwd0Pc4lq39KxwGWQq3dbEhYtfHFN5hWg5IcJYONxHXOJ9HSe3aCyAw9BnZkFamA8L-C2OedDZJBrU9-f9OCs2xpj71Aq7EXsvV51EOFOB2e0aL3clrdbuKNi6JEjrzTfTbLNKWCw9ydXRXRpeNAsRJGp5KU6d0kQyuljClNiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
عصبانیت شدید هواداران اتلتیکو مادرید از خولیان آلوارز؛ستاره‌آرژانتینی‌اتلتیکو دیشب بعد بازی باویارئال بدون‌توجه به هم‌تیمی‌هاش به رختکن رفت که هواداران اتلتیکو بشدت علیه او شعار دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/28375" target="_blank">📅 10:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28374">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJ4-ybVGd0NP1sUGX08DhmaHUlSzBvJ2cBLW6iyWUTwSTQ629aLFMIDUtvkTvfEKN-a4mwQiIMue98YS6z7sI_tE9JZ7zeibHw0c-P6HoK0J6g1OQLv5KQR8dAD1N_RL-BkGNhIfOf68747VgOlvCN8tvVOMETB4WH9KcnaAuFmSMTydL8lohb8x7pAGjzjYtm9UDWhbeHwVKFslZUPsQR42qT7nnMVu6ZE4xbktk4lP6Kkfx8a-YKG7g9EyxFdnEmVF4HXe8Xif2ccAVVLYi_yhgyLQ551H-m86CivXoDaaIKyDQdb2vDk0ChT8JoS6cjqADcv2mGXG5bN3wVAb-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حرکت دور از انتظار عارف حاجی عیدی هافبک سپاهان خطاب به هواداران باشگاه استقلال در پایان بازی امشب؛ حاجی‌عیدی در دوران حضور نکونام در استقلال تلاش کرد به این تیم بیاد که نخواستنش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/28374" target="_blank">📅 10:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28373">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ml0Zyqi1wztS82eCGczHwdUnifECPXpXm-aqw0QUyeez6N08CLZjZDxVibdbUVy5ZuaDplms5O9o_EsrhEbQSTS64daSNJ5KGw6grH4nw_4Sn-mkPmOPbxj-KIysSWaApkCj2_Aj1FoXiAg75E_J5oRndv9qW9FhKfT5l7QggC0HZD9E8VlcAIT8kfNAUq-Zo8gUDbR0EWE8vcWtqEUZNWSD7-gBZyEn9QBXsO3WpTYUlsjmH_pumETsqKzQGNdXZ4RPKrEU7J9XqFQIjQYK5G5f55DGMjZjnTZCRXIs3RZ5TktVKTXjxYzOZiQ17ScRFXG-duv1qaDNwD5qfMaNiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج10تقابل‌اخیرپرسپولیس
🆚
تراکتور در تمام رقابت‌ها: 6 بردپرسپولیس، 2 برد تراکتور، 2 مساوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/28373" target="_blank">📅 10:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28372">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400b87e841.mp4?token=m1viMBBHFLkrUC-nx_9MyVQU2G1_RRAAt3lKWplumWPzvnAc2CYLcNXDmI_-TxcA9-JenSM-YYlYI5UQbKIVI4i_j42f8LrqfotcHxR7PRO6A_DxdWIimW9Z9hs2Lh6eaS4RhP0XTPJ8vdWmJz6S3LbuIR-z9xLI-BkDJLdX2w0JIv9Q5ok2mNUa1EodqjMrlNG9Kp_NFI6f2i811AKaP2c5a-BhfEVs6rh31OHJ10yRBicSb1QziFnsttCiT8OUoYEENAIVJR3kmN3RZ4QgLyXelS6ahrCTEw9c3al6mbww_pErr4W_ziF5ybLo-9I9uREQrkJKPquURRgqBIxtmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400b87e841.mp4?token=m1viMBBHFLkrUC-nx_9MyVQU2G1_RRAAt3lKWplumWPzvnAc2CYLcNXDmI_-TxcA9-JenSM-YYlYI5UQbKIVI4i_j42f8LrqfotcHxR7PRO6A_DxdWIimW9Z9hs2Lh6eaS4RhP0XTPJ8vdWmJz6S3LbuIR-z9xLI-BkDJLdX2w0JIv9Q5ok2mNUa1EodqjMrlNG9Kp_NFI6f2i811AKaP2c5a-BhfEVs6rh31OHJ10yRBicSb1QziFnsttCiT8OUoYEENAIVJR3kmN3RZ4QgLyXelS6ahrCTEw9c3al6mbww_pErr4W_ziF5ybLo-9I9uREQrkJKPquURRgqBIxtmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو برای چند سال پیش نیست برای همین چندماه‌پیشه و خیلی‌زود به حرفای ابوطالب که گفته بود دلمون برای دلار 78 تومنی تنگ میشه رسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/28372" target="_blank">📅 10:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28371">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5flENcpm4_hYGD5oU473Ifok-CL1upuxYoHyZ-Z2lnC0gKHkzmcVk8zq7KgPLtM5p6HeAfR9U34XvUQwBywF3Q1rfnO_zAy0QjhMmRA-fFisGLyRqETluzbHv7EUEAV2UX-Jgdi73-whsMiQAuC4w2P0WycS7AR3QiQYYQ2TwD0TzEnt8Fws789EwLZ_CUJbue6DimFP_ofG25zGy0al3sEEEZZ1LluJ4yqQyhyRNuoR7h5dJQdM1zMsD8ELXtdMledVZm8EUZaBnG8vzVBud7CdrrD_sH70PTLzxRrCkhDRrON_jp68G4v28k7Ade75rf0sUdUuKEtcPLbX-CAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《 لینک سایت برای کاربران ایرانی》
👍
《 دانلود اپلیکیشن اندروید》
❤️
https://telegram.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/28371" target="_blank">📅 10:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28370">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7561a592bc.mp4?token=h2MUfsTs4CAZlgDMMkz56JK5zGmWFyjRVcdu2tJGy0bZDRuBG7Wql9NMLtxcgoLz8x1IQDMJ7uW6Pl2PJBrltq7JAT8xQpFA2Y69IJ3c2kmU0z6j7-wWBEEFWKw9S_1b2IwsUplRJLU3hXke1pahg7J31cuJzM2hIGcnlUZ_nfP5FJ_C08DTaFtJKVoSXC3N6Q0uRgLCYUkVZgpn1RqLPKiXz-jQFo9gvl5bgaxFsxPex25da17cUBS5RiyGLtM0MFgKwczjWEObVRY5q5HuQxVmlLikH200D7d73WWl4H4OiOd0mUi_UTUH-Vc9nA17UUssS7rtEI80UWK5eAsoNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7561a592bc.mp4?token=h2MUfsTs4CAZlgDMMkz56JK5zGmWFyjRVcdu2tJGy0bZDRuBG7Wql9NMLtxcgoLz8x1IQDMJ7uW6Pl2PJBrltq7JAT8xQpFA2Y69IJ3c2kmU0z6j7-wWBEEFWKw9S_1b2IwsUplRJLU3hXke1pahg7J31cuJzM2hIGcnlUZ_nfP5FJ_C08DTaFtJKVoSXC3N6Q0uRgLCYUkVZgpn1RqLPKiXz-jQFo9gvl5bgaxFsxPex25da17cUBS5RiyGLtM0MFgKwczjWEObVRY5q5HuQxVmlLikH200D7d73WWl4H4OiOd0mUi_UTUH-Vc9nA17UUssS7rtEI80UWK5eAsoNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
این واکنش و چهره عبوس رونالدو بعد دیدن رئیس فیفا در شبکه‌های اجتماعی داره وایرال میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/28370" target="_blank">📅 09:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28369">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b7f7aa5f.mp4?token=heb5e3128rpMEoh9S_JJhwUbJHMNSAxvtaNwdZztI-qI93nVwA6qDrDbfbBbh-wiqEYVB4pSsDrMLLQbsKZ6-J1joSlemWZZ1Sf5_U44U8aoSEL8NHx8eL_pbqBpqOjXdxN13h51pNFWgPOqbbr760oCkaFhkKQJ3_TaIpDnS49b82Zo3L5-i0JIrkCl88X7gHHolcxgzMSxoC07Pu6exnfMYWEowhfWFScW97lHkToSVPRn9VUPj674K1nCe2TVPQ1EpRV01X4DIJr3sl-hIRGbYhpbCOcSaBDJfsQXgvrNq-G9-xft9FRO2CakEKCNpLNDqYMA2Kw8wYXlCd5lXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b7f7aa5f.mp4?token=heb5e3128rpMEoh9S_JJhwUbJHMNSAxvtaNwdZztI-qI93nVwA6qDrDbfbBbh-wiqEYVB4pSsDrMLLQbsKZ6-J1joSlemWZZ1Sf5_U44U8aoSEL8NHx8eL_pbqBpqOjXdxN13h51pNFWgPOqbbr760oCkaFhkKQJ3_TaIpDnS49b82Zo3L5-i0JIrkCl88X7gHHolcxgzMSxoC07Pu6exnfMYWEowhfWFScW97lHkToSVPRn9VUPj674K1nCe2TVPQ1EpRV01X4DIJr3sl-hIRGbYhpbCOcSaBDJfsQXgvrNq-G9-xft9FRO2CakEKCNpLNDqYMA2Kw8wYXlCd5lXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رافینیا ستاره بارسلونا که از ناراحتی خولیان الوارز ستاره‌تیم‌ اتلتیکو خبر داشت دیشب بعد از گلزنی این خوشحالی مختص به آلوارز رو انجام داد و به نوعی از او حمایت کرد تا روحیه اش رو برای ادامه فصل بدست بیاره. آلوارز خیلی دوس داشت بره بارسا اما مدیران اتلتیکو…</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/28369" target="_blank">📅 09:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28367">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82aeca8f4.mp4?token=XgockX_2cd4-psybdM81NMCjNb_Mh5LZ5TfJfNqF79T_W4np9lgFuQPbims4GXSaeFKsdYICa5n6aAacXYAV9V_xotb8-bY-fBIwwSsCLCXvvTOtfZTlb4QeRLyBIl7vrEbJv52iYDrQM5q3cntyyfBGcpwJt0yhp3TrG4YM0HYCfxVQha3u3nMdwmFT_bOnE7wseE_T80hMx-IlQWA7O0RCuQIPIj1XCJTHjJCHgNFwUF1qWDj87bgCmorJ1godRnTrEj42l4HHY5CeQpbonnyp8R9QD5pPB-5o4blLyKX0DQbvuKCL_oim0CIJEXqX2WhFk_ZTtpIKLF02RGJlAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82aeca8f4.mp4?token=XgockX_2cd4-psybdM81NMCjNb_Mh5LZ5TfJfNqF79T_W4np9lgFuQPbims4GXSaeFKsdYICa5n6aAacXYAV9V_xotb8-bY-fBIwwSsCLCXvvTOtfZTlb4QeRLyBIl7vrEbJv52iYDrQM5q3cntyyfBGcpwJt0yhp3TrG4YM0HYCfxVQha3u3nMdwmFT_bOnE7wseE_T80hMx-IlQWA7O0RCuQIPIj1XCJTHjJCHgNFwUF1qWDj87bgCmorJ1godRnTrEj42l4HHY5CeQpbonnyp8R9QD5pPB-5o4blLyKX0DQbvuKCL_oim0CIJEXqX2WhFk_ZTtpIKLF02RGJlAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
چهره درهم آلوارز در دیدار اتلتیکو
🆚
ویارئال؛ ای‌غم کمی تخفیف بده ما که مشتری هر روز توییم.
‼️
خیلی‌تلاش کرد دراین‌پنجره‌بره بارسلونا؛ هفته‌ای چهل بار مصاحبه‌میکرد و میگفت‌علاقه ای به موندن در اتلتیکو ندارم اما مدیران اتلتیکو بجای اینکه 150 میلیون یورو به جیب…</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/28367" target="_blank">📅 09:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28366">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/292f9f2a3b.mp4?token=ApmDWB70IbdLWJviJXr57YFqumJrp9FnUNHnIQYAJWQcgGrVVLVJkJ457DefREvCZGh_L0ee7riMEK6ZlT-t4nq5BraD6tYOWgsOEblFplG9k8QZQZ_TAxj9WXr5V8eqJwUwoh61HAQAM3FKO4eVryDigY_w_BhkPZtbiaW4FxpQvBMN-XjEjn06h-HINgasGd3zXL-0SSFOihcNUGmHfF81JCZI1TZtvpX3UdtxY289ve7vDlc4bwi1iS-KbtVG3u6fPWGvW61LvdLbpI6P2e-X3DAcKS8bxwdaAlXHO7k1_Z-UFaogus17Q8KVNHXuRRRtbu_27MzmfeBMwXqQp3c743Cj9y-2-7DpS51BpKWYHZIor8n3Tccwz6T3ow0h-GJFiypBXuJSy_yrloDtV9gQl01g-8p--BwekJ4VoDHr1Mn4s87Y5cttDjkrSL0qux07VdVVDsFPkq2gY4pMJ3eMlQR-C-rYRT4CwCCy237UewS2oQMbZ9x6U6HjYNe-D5b6OpbTy73HkIlmh6__I3ttJeRpNv2XqGOVYPe9TLPgrfIvR98OpHHlJOWCnqM_QOkl9MzJDROSxG9_7vlrXk1_xg5PUWqmXl8hrJmB46HBrPsntzr61wS-NDAbfk4Oydjkl-BpO3Uo8Bm86GC13-xuYtsbnNDMjZAIoFrpWBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/292f9f2a3b.mp4?token=ApmDWB70IbdLWJviJXr57YFqumJrp9FnUNHnIQYAJWQcgGrVVLVJkJ457DefREvCZGh_L0ee7riMEK6ZlT-t4nq5BraD6tYOWgsOEblFplG9k8QZQZ_TAxj9WXr5V8eqJwUwoh61HAQAM3FKO4eVryDigY_w_BhkPZtbiaW4FxpQvBMN-XjEjn06h-HINgasGd3zXL-0SSFOihcNUGmHfF81JCZI1TZtvpX3UdtxY289ve7vDlc4bwi1iS-KbtVG3u6fPWGvW61LvdLbpI6P2e-X3DAcKS8bxwdaAlXHO7k1_Z-UFaogus17Q8KVNHXuRRRtbu_27MzmfeBMwXqQp3c743Cj9y-2-7DpS51BpKWYHZIor8n3Tccwz6T3ow0h-GJFiypBXuJSy_yrloDtV9gQl01g-8p--BwekJ4VoDHr1Mn4s87Y5cttDjkrSL0qux07VdVVDsFPkq2gY4pMJ3eMlQR-C-rYRT4CwCCy237UewS2oQMbZ9x6U6HjYNe-D5b6OpbTy73HkIlmh6__I3ttJeRpNv2XqGOVYPe9TLPgrfIvR98OpHHlJOWCnqM_QOkl9MzJDROSxG9_7vlrXk1_xg5PUWqmXl8hrJmB46HBrPsntzr61wS-NDAbfk4Oydjkl-BpO3Uo8Bm86GC13-xuYtsbnNDMjZAIoFrpWBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شاگردان هانسی فلیک در هفته نخست لالیگا؛ آتش بازی راه انداختند و دردیداری خارج از خانه با پنج گل الچه رو درهم‌کوبیدند‌. فرمین لوپز دبل کرد‌. کریم ادیمی هم نیومده برای آبی اناری‌ها گلزنی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28366" target="_blank">📅 08:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28365">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a4c023812.mp4?token=hLxzeBoRrLyTwU0mt35FNYumQyjJM4XISbtyQtCt3dw1zmGsSh2GmvNX-EjXc_zRLf_hEL6c0yetBA3uT9p3dhUX9CX0owD-fwenmmNfcQ1-b2YjAjkHV4i9cupH_BLlWTcNKBksTXb7j7JWrdSxHKtgxKgOEicJCVQZIE8idNAsBZ2gwCxhRal-MuWdFsusI4PBXlzWja64Ytbbaxl_D3OVLUjnCeS_DmNouAomVMOXmzKU2S9XH0uoczZQN7NdjNdzqxflnmx5WJsf5GIdFH5OIshOwYHklF4o16_dEIO2012FCHuBlu5behSpa38yY4CS__uTQAKTpQLxA99Ytpd-PctgOuonL_zTIy-VgtYv5C8Uf1v_ZRzwnravR0D7QHWuoXY0Ay_JpjqBf4YbR2PCPH1VJvx7mgZFNYP831mXcmSCKnDjMMQSPlGpySNBZPmulOtXi0Xj1B-PFiVZlXInVZOVKWRtdPniJBJIR3HLFE2CZDZ76aXieBzGX65egIfLUun0ey4eNmK9uGkc9Nc0bKWovFCsoYVVFb49KWwIzZ8r5fcRKKHY7xOvOtcJ8I2zf4kECShxfswcFsDVt9FD_MySFVCNqe7LsfG4h9tVKwLMbaZGEfOFQQSZGoCBBF4nr-vCwcva3m5Y3Z15O2MOHo2xgmqacjNWWWg6qEo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a4c023812.mp4?token=hLxzeBoRrLyTwU0mt35FNYumQyjJM4XISbtyQtCt3dw1zmGsSh2GmvNX-EjXc_zRLf_hEL6c0yetBA3uT9p3dhUX9CX0owD-fwenmmNfcQ1-b2YjAjkHV4i9cupH_BLlWTcNKBksTXb7j7JWrdSxHKtgxKgOEicJCVQZIE8idNAsBZ2gwCxhRal-MuWdFsusI4PBXlzWja64Ytbbaxl_D3OVLUjnCeS_DmNouAomVMOXmzKU2S9XH0uoczZQN7NdjNdzqxflnmx5WJsf5GIdFH5OIshOwYHklF4o16_dEIO2012FCHuBlu5behSpa38yY4CS__uTQAKTpQLxA99Ytpd-PctgOuonL_zTIy-VgtYv5C8Uf1v_ZRzwnravR0D7QHWuoXY0Ay_JpjqBf4YbR2PCPH1VJvx7mgZFNYP831mXcmSCKnDjMMQSPlGpySNBZPmulOtXi0Xj1B-PFiVZlXInVZOVKWRtdPniJBJIR3HLFE2CZDZ76aXieBzGX65egIfLUun0ey4eNmK9uGkc9Nc0bKWovFCsoYVVFb49KWwIzZ8r5fcRKKHY7xOvOtcJ8I2zf4kECShxfswcFsDVt9FD_MySFVCNqe7LsfG4h9tVKwLMbaZGEfOFQQSZGoCBBF4nr-vCwcva3m5Y3Z15O2MOHo2xgmqacjNWWWg6qEo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
هایلایتی‌ازعملکرددرخشان‌یاسرآسانی ستاره آلبانیایی استقلال دربازی شب گذشته برابر سپاهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28365" target="_blank">📅 08:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28364">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXuqJNHFpkuYWpgPUPFMu-03fhwnRhjBhMReF5OdRjr-yaPlL6zARhftCs0FNmCQNkL2kiOe0MDPC4LzGHrlqxwQJR81kxBH20FI-M5Yee5RjhCb0NiKQJGtfEZH5AHrCOLHUWkWe8N2-9kCiWX4pMRDoMPiSpHK1p229x8yDTOW322hHO4kR5za4YGLLtO0yHGqjkALt0zs-DRxdF2jExwRsu7Bc-C8CoyVMXQzJVQDLwFTeg116P7TR8bMH2f7P8ggkJRLORIt6Cjl2UZsDPzLR2KcY3I4VtzDBy1Txc4QsXIt1A4gTGLPthNW6M5-u98Y2rgTfkFl_E9FW_da5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
یاسرآسانی، اسماعیلی‌قلی‌زاده و حبیب فرعباسی به‌ترتیب با نمرات 8.5، 8.3 و 7.9 بهترین بازیکنان دیدار امشب استقلال
🆚
سپاهان انتخاب شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28364" target="_blank">📅 02:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28363">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHoBzQ04pb-XaQxD0h9KuEQeUGzslFy_sypTDbpekdYAvJPfxYEkypxQ3JIE3bnCl-5eFMmOawsOxdGkst8T5h6x_GWGovK619ofvESYSm1WJwcyvdPQZcJacGMDmpaJB_eeETP6xntKHH9fE4u2_x7UgvcD7-PvyknuRRSmhNvRnBBkKhrzI3R1ATHeirQ24rYedsUTlJoHccaNSVAMrTK-w7wjjMhp5NBlIAOw9IRUz_cwn2ETeEn__jPehMUpWx1T13AhytxUEfnwvq_kE1WVaJwfnXXjepACRgv1NCDVqIwF_Rjq0oq7EQiUWUUNiLO-wAYkQ2gyS11uG9DqCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بخت در خونت رو بزنه همین میشه‌ها. مردی داشت با هال‌سیتی مذاکره میکرد بره این تیم که‌یهوسروکله رئال مادرید پیدا شد. تو اولین بازیش ازرو نیمکت اومده جور ناکامی امباپه و وینسیوس و یان دیومانده رو کشید و گل پیروزی تیمشو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28363" target="_blank">📅 01:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28362">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔵
🇪🇸
پاریسن ژرمن با درخشش و دبل فران تورس ستاره جدید خود مقابل رنی‌ها از شکست فرار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28362" target="_blank">📅 01:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28361">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1704880194.mp4?token=cGX8rICQRYlSHo56_vgPZPD6F-PShLt2MgMZNh8UD25_V4QxG9sEF9vGoZNcL-RpASofUq6_iYklXppC0AzuCnbmEPWxO3vfz_geG8ii36bawbGdxQiAJVykwwAHsUhUniOh0CESbOfNt9jlLvbMSQdxEKYFrp9CUGJTF1Vdtx0EhQtpyk3nTJpLeFG3y-sa8NBZZfT-ZAwKXza3sfZk1chsGaoTuMvbltex2GgDS3wGkmF7DhZnD4vja5y3xRh6x9XDCvT4ocIp_S6Df31i-GT4LLnXsePK8jdFSI2F4lNB5XUljQam6VRqxj2VPCTDxbHkI3NQ4Pdj6zCqY4JTqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1704880194.mp4?token=cGX8rICQRYlSHo56_vgPZPD6F-PShLt2MgMZNh8UD25_V4QxG9sEF9vGoZNcL-RpASofUq6_iYklXppC0AzuCnbmEPWxO3vfz_geG8ii36bawbGdxQiAJVykwwAHsUhUniOh0CESbOfNt9jlLvbMSQdxEKYFrp9CUGJTF1Vdtx0EhQtpyk3nTJpLeFG3y-sa8NBZZfT-ZAwKXza3sfZk1chsGaoTuMvbltex2GgDS3wGkmF7DhZnD4vja5y3xRh6x9XDCvT4ocIp_S6Df31i-GT4LLnXsePK8jdFSI2F4lNB5XUljQam6VRqxj2VPCTDxbHkI3NQ4Pdj6zCqY4JTqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لالیگا|برد سخت و نفس گیر شاگردان مورینیو در ایستگاه نخست با گلزنی کارلوس اسپی.
🟠
اسپانیول
1️⃣
-
2️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28361" target="_blank">📅 01:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28360">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVpswnX6EfHRfO14WCqf4pwLQFDlNaAm_Lu754CNCnWt9GzUUeJtYem4Gsdq5NtVfSlu3i-9DAAPPFtg4U7XG3YA45y_fB4GDWxLR90h6sTeh1mIPtg4eOlFR2evFaXB8mBc_lTw1CWA7ZUulEXoD2liFsRdr5dvi7OzQ8uEUBgjO7N5kAfIWZD2l1cPF7v85vzrarrqsgF4zHc2_NbfuCfHQifiDAQ5KjUl61gqh1jKyaYRL-meI1uLrzlII7HOnalEpES2fEZVLyJQ7qNIE0IAmwFKhwq_UMCKVXnZAiPs9kSVN-iktqcU6LFZbI9Ak9rrKhg7ljgb46AmSiOmtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
جدال سرخ‌ها با شاگردان نکونام و رونمایی‌ازچلسی‌تحت هدایت ژابی آلونسو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28360" target="_blank">📅 01:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28359">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cl0O0h01y_UErs5D45ACImmbXu7Sa8wrkWi-xEvJ4eD654K40LadjXjVPxmYRGPeDpdmm1Hg8esCSsR_apagM47VyXHj2MGqjzVqY-JMWQPxSCw-8ZZweiY1T6H1hEMKj-AH7o7WWIMGW9NnaQ1fCEcqGRFUJJhewkqvFT6CpeCi_c-eJ5_Ae3TCdeaBzVzCixma1dGEPQUjKfpvCrw4u_2KUOLn2ziLraZHOrYcVX43km8KPsEChOliwaXmOYcJs-2Gw_ze63moB16tYc08eb6sy3lIXUSttUpEZ4TllGNhqPQirLpJjc3Qmh9JvLeCq80WumaLWHOAIx1tCq8B4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌ دیروز؛
سومین برد و کلین‌شیت پیاپی استقلالی‌ها در لیگ، برتری دشوار سیتیزن‌ها با درخشش‌چرکی و جشنواره گل کاتالان‌ها در گام اول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28359" target="_blank">📅 01:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28357">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyANJEs2Q1dGHOKYz9vB_1w7LMB3AOo6oPYDBq1ljnPrUAQurRh49Tgh65n4SpxgKbtVVLGoMX3J1PH2agX66qRq8NI0GKpan5YzRCGKuWXNMkOACyOW7UHsqtnxqu9-REmOkDAO0HMFY833qYf7s8z9flVmM4kA8FJy6kzRVd7FYWM4AFrI0kRGwddilm1LrzhFrm9-0IGPnUkExjo4oyiU_YmeuvmfwioU50HjvuF9fkvFGkAEzs4obkVcg8V8kGN1XxcCFIl87VsY7uBivSFravOijMR79xxVbGjcYcAk1dtT8RTWOch_7ClBdo-zx4R7z8wQaBlNxerplROH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لالیگا|شماتیک‌ترکیب‌بارسلونابرای دیدار امشب با الچه؛ ساعت 23:00 از پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28357" target="_blank">📅 01:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28356">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da75343e43.mp4?token=CpxrhV4jJm1Klhta9XwukPo2cxq1LKix-avlfI79mMhhso3CsF356SFQNuaTmstqSgregxID29mLxlcijANJ76I4dG6-BobFAKkDsgP3-UtnSxWT5KLokEJR1jGTzyEF9qdCIhu8l3JK0Pj7k3VUCLwBP_0WqQ3biWZHfJATVrVaKYUfzf0ui87EBatOCpB3ZLyemjub4fkOSuapvrJSq81uClVkviYXPYW3eC58x98PKb61oE55lSswfNR218JfTg5ER5ipbP0En4WQwZopRM2PoGDyuAhuSL-EZCnLr_77AyWIqtczznmwexm5pKeE4P4ddUw52SUhbHP58p-TEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da75343e43.mp4?token=CpxrhV4jJm1Klhta9XwukPo2cxq1LKix-avlfI79mMhhso3CsF356SFQNuaTmstqSgregxID29mLxlcijANJ76I4dG6-BobFAKkDsgP3-UtnSxWT5KLokEJR1jGTzyEF9qdCIhu8l3JK0Pj7k3VUCLwBP_0WqQ3biWZHfJATVrVaKYUfzf0ui87EBatOCpB3ZLyemjub4fkOSuapvrJSq81uClVkviYXPYW3eC58x98PKb61oE55lSswfNR218JfTg5ER5ipbP0En4WQwZopRM2PoGDyuAhuSL-EZCnLr_77AyWIqtczznmwexm5pKeE4P4ddUw52SUhbHP58p-TEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ عملکرد حسین‌ حسینی دروازه‌بان سپاهان در تقابل‌های‌ خود با استقلال: چهار بازی، سه شکست، یک‌ مساوی، 5 گل خورده. 0 پیروزی و 0 کلین شیت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28356" target="_blank">📅 00:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28355">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHt4lENyG0BIowtgrgfUtnQJbKm9mwB7RY02gbzHDLRGLndMU7w3Wct7MT8gngoFDWxPSN8d5BTwZkqKA-8CZrdjYHUhj3mQEXMnUiUZPG8qJp2U6Xbs-uDKhSQMSyDs9mUA14EmtXSBVusL6J6VLyQRnTqTwxE7u6hsOS4q0kbakKO2BZ3Klov2ITm2Kmqpcqs1H_miDwT8y5KL8-x965o22wi-HrBD73S43bLXHbsGsf0c32Lz56yzAWtlLfTkEN5IqknCDeu0jD8tE812Em4iXIajgEkrxqX52yahi_FB7O3W9zNZ2it9dvzB6g8BBnP9YZ-SH5l-kobJLgD_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌رقابت‌های‌باشگاهی؛مدافع‌ عنوان قهرمانی سری‌آ فصل جدید رو با پیروزی پر گل شروع کرد؛ تاتنهام همچون یونایتد شروعی نا امید کننده داشت و 3-0 بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28355" target="_blank">📅 00:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28354">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMu0eEq93h01KOgT5kOEjknXLTQogqVHfUbwqD7TI7dvPfWtoowLdBj6Kumwd5uAd2eEcPHOYyC-aKNL0V04508R1lWSL88lx92R_nYDHDB7pVqtaJ41iO-ccQrjD_kGVB41GBSUZoYsPmUkABtV_1fd--IoalaObsWyf5LgjYofUnnYNqSH8UL9YNLa7-IHY4KNlqAI_j2SBeLAG2CuiPySata5d8JnqZrwllNR-kzv0z-pj2K_YlgTrA6Td7yD6CLNdDIjYaI8P_ITZ8JUxqd4VWb3_kVWUTJJTJ44MsvfoamlrQ2fHeqeFmXlDBFIfIJqB-r4eSxtx3t66pFXog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
پاریسن ژرمن با درخشش و دبل فران تورس ستاره جدید خود مقابل رنی‌ها از شکست فرار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28354" target="_blank">📅 00:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28353">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkHpdaLRiwKZAiydvOLFKVM7ugoM7DicuS_YZmi9GBP-dlbzFEuYC8Trqcj1MRVYsnwDw4u1i1o9OOvFEVPh2yckwfRjMIsquQZShborgP5B_dQKIgzDHQY1qhSQnnBCpJHrLR6DKBGv02bW_7ZhtGqn0t8PbkqEcIwGIjpsRIOYt2kNKCmZHRziR4Z9-BIhnUFdsSG_gOSUIHVSGK5t6Gf6vLzJzhdVVnKtPoDDP2ic1uljIuwp3i1CvsIvjguO9txu4LnGoJf-kExTaJ-2b4j3dQX5PgHg9-EIASPI8vGFqvy072E0y7ljanTMcek4KEFDLnwzz9HnqsyTGGLaCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفاصله‌چندساعت‌تابازی‌تراکتور و پرسپولیس؛ هواداران تیم تراکتور مقابل‌هتل بازیکنان پرسپولیس تجمع کرده اند و شعارهایی سر داده اند تا به نوعی شاگردان مهدی تارتار نتونن به راحتی بخوابند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28353" target="_blank">📅 00:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28352">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e759f195.mp4?token=P49wdk6FEywADJnJguhH151jok1fUbuzSCkQiu9DhbRxHQoWy6Yu-odJHSCSDvMYDBYuPpniWbtgAINbAZOAdMJrz5WyaxmscjtqTLO2HUI3Ca9ibKpq_TAbWog0oj1VRf5QefflTP6z6Urns14X3VLemTxMeIVCVo8iirzyOURkMCFyd7hzdrETzEGEZR3CPtHUmt2r7BPenA-rnfeieG014lq4en2TMuLdu5S53Q2MbxTC6f_ZnH3MXPxrSyIEWXs2h4r_csVGI8H_wzIwM6KzZzA3D2v9gmlIVv4Hp2rG1ol1rBQB2Tp8oS52jEWmon-1yTMRvYPcqk8bsi90vWPtAA02ihP-Ao5Z3aM9GZuG_LQN9h3cDdHvxH0RSpMVlxSOmp8_jXXhr1093Z-2FWTRcEoC0PPjhGTde10X_wa9F_tUB9fVl-DAz3xVqsVZ0-EJWGdAkRQJhD4z_Y4pNFyuxSvvQEYM-1Juoo0itQBRYz128lzIxyJ3MWx5-GF7zUYXNgaQZthKlknA2TltuG5dWsSNZaK4kJJEjtqH_B2IirFPZTTmiH1FnQe90GcCw-xUZqnsytFOO46Ro-tmrWaYHNS3NJ4y6PWcbSa5XCk4b9wbOHZafvFVB-gwb37oTPYrTfoj3NQeow5yJbi9zclum4JFD4cPyZKbctXI1XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e759f195.mp4?token=P49wdk6FEywADJnJguhH151jok1fUbuzSCkQiu9DhbRxHQoWy6Yu-odJHSCSDvMYDBYuPpniWbtgAINbAZOAdMJrz5WyaxmscjtqTLO2HUI3Ca9ibKpq_TAbWog0oj1VRf5QefflTP6z6Urns14X3VLemTxMeIVCVo8iirzyOURkMCFyd7hzdrETzEGEZR3CPtHUmt2r7BPenA-rnfeieG014lq4en2TMuLdu5S53Q2MbxTC6f_ZnH3MXPxrSyIEWXs2h4r_csVGI8H_wzIwM6KzZzA3D2v9gmlIVv4Hp2rG1ol1rBQB2Tp8oS52jEWmon-1yTMRvYPcqk8bsi90vWPtAA02ihP-Ao5Z3aM9GZuG_LQN9h3cDdHvxH0RSpMVlxSOmp8_jXXhr1093Z-2FWTRcEoC0PPjhGTde10X_wa9F_tUB9fVl-DAz3xVqsVZ0-EJWGdAkRQJhD4z_Y4pNFyuxSvvQEYM-1Juoo0itQBRYz128lzIxyJ3MWx5-GF7zUYXNgaQZthKlknA2TltuG5dWsSNZaK4kJJEjtqH_B2IirFPZTTmiH1FnQe90GcCw-xUZqnsytFOO46Ro-tmrWaYHNS3NJ4y6PWcbSa5XCk4b9wbOHZafvFVB-gwb37oTPYrTfoj3NQeow5yJbi9zclum4JFD4cPyZKbctXI1XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه دیدارهای فردا ادامه هفته‌سوم لیگ که در حساس ترین دیدار تراکتور باپرسپولیس بازی میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28352" target="_blank">📅 23:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28351">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ay9qXdFC-u2wRdABsvYWCMJkZjODX6kz2G6C2nPsaKukj-Bddrw71XTZmUSv5lvPB89wyCC4R5fSmvS_azzFKRx_MwmmaAx5HmjPqNGP41TI9x8ItHSp66VrnZgF8s56woxcw99pciFqUL5ktY_TFw3XbtPilzuRwvOHR-gup_tPB2OBplE9rITBZgGJ3UPd9tcZ4qZUqspD5mHAK6btpfmvyUx4yZ5tUH8SyEXOoxSTgMn-H80ot3zbWKt6JEEujSGTZ2VROTpvj0fPZbj_0p6nNJbr-pKVrbZNi7_48IXTEtr9td0N6F5LeVOBcQ2OJPWOhv9rqIHK0adQ94eRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برنامه کامل دیدارهای هفته چهارم لیگ برتر که قراره روزهای جمعه و شنبه پیش رو برگزار بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28351" target="_blank">📅 23:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28350">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8101aef2d7.mp4?token=QNkuHht2flHFt9yOeCyHhClVenDCmN_bskb5AIKTAxzFdiWNNzxBkeahT4U-CjecFj8byKdS5vHnHds6DT7dlnKkS4lqtx1AAXl7tIPSgYewYKYVsk3logkxhCCu_macm2T7bFPZlgBeOx1lLt71ecYres1hmq5wYGSSKNxKfp-UkzmnHqCkqwLIhpL3zbG_Y6IWd-Zpan7pLiLLlJoRuwapNcOq5q_Wg74BeFHk0UzTibl7tXkT2KrC1R0OXq8d8hUhMRNRki9LWOTurb7yimYsjMyTx2rFK_cP-ffWlqvzkKTr9nWtFCBfc00evVNaDaWd40qG277UeMRtPOiNg4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8101aef2d7.mp4?token=QNkuHht2flHFt9yOeCyHhClVenDCmN_bskb5AIKTAxzFdiWNNzxBkeahT4U-CjecFj8byKdS5vHnHds6DT7dlnKkS4lqtx1AAXl7tIPSgYewYKYVsk3logkxhCCu_macm2T7bFPZlgBeOx1lLt71ecYres1hmq5wYGSSKNxKfp-UkzmnHqCkqwLIhpL3zbG_Y6IWd-Zpan7pLiLLlJoRuwapNcOq5q_Wg74BeFHk0UzTibl7tXkT2KrC1R0OXq8d8hUhMRNRki9LWOTurb7yimYsjMyTx2rFK_cP-ffWlqvzkKTr9nWtFCBfc00evVNaDaWd40qG277UeMRtPOiNg4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
بانوان‌هوادار استقلال در ورزشگاه شهر قدس در بازی امشب آبی‌ها مقابل سپاهان در هفته سوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28350" target="_blank">📅 23:10 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28348">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvFmhJWt5Qb1E4f-xgg3_9p-CyQqyhIlYxtG1l41l0Nty7k6lTMOQlG6m2BTCSdc-Nx9zX0IIO462Aft7ch4sVoCCzjBcRcj8luSDsyY4qkOwFT47n-ca2BH3-0CgRPL7iFiEpqoLGeAiEzIwU-x4nGjaY2ElaK4Ku3VPQJyuH9RBQ7G4MmlYgmGOnVLmSfI4LZeNR-6ldVQBAhe9fciYIfmtgGuh39PbXj5Zq1Q1WFCvvXeYYwjBYZsy8rQx4ASDou4xAQVZhHyQeirgxdo3RRfOltXbePlhzjh81LFk-jTyU1tf8QGTP4Rl0XRauBwbiUG3Vw4ch-v7G3cEX635g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfpTpO4oTAWrpPnBhwwaXH53y6xZIAasKvrdmjSBlchlqFnX9GQ4LdJIVuyNvUKIn5hq8E2Omf4VTUnR--ROEFVs3EkKPvPx-TSBnqzp0P3t6rRmcFXt5cFiQG2WUD47NBEfsglLiCGIJLCmnwottfb5fTrVzAiWPPjqE2DpuuFypKZNf5U24mWc1h4tOS2ym-OJPyyDcr02HWEjy-9hK_jM9oSPsTk16B5b9gc_Xj82TpeX3MPplsFPq5DcbfxOnDc8pJXSi-iA6eGwGlPVPspjpKcSR8hc7hPuuBzUONd0udw-hFxrDHoCNpoqpL4QV2fAeDVuZDIDPTGkceunRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
👤
بااعلام ایجنت مهدی طارمی؛ باشگاه الوصل برای‌خرید مهدی طارمی تنها 400 هزار دلار به باشگاه المپیاکوس پرداخت‌کرده درحالیکه این باشگاه یونانی برای جذب طارمی 2 میلیون یورو هزینه کرده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/28348" target="_blank">📅 22:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28347">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5NA8QmTWfv_BQSnmwNSc8ZUXd8baPiyYiMED5qWBiEaqKo8Y0aI7hVBX9KgTQwt2HX13u3Da0KYEfimXTkQdbVxSqABoo5jVhaCjfmhA8BKpz0fB2h-erJTLQujtBFwqiaNfqjhoAYgFOKUQbR6derVTuHB-Vb2wr58fTV35YvcVKKvnEEKpmN_W081VEmvZ18pwumlK5IOhkc0AA_u0A0gBXwgTj0fTgNioQPX5D6xW-PTD6j1GylY4WuDY8Ig0n3X8cNsDncI6CUtu2wAUw8FGCSuTt0GxIOD2S14OcpYJ8pg4ZZfedcK2AwFqHdHK5KUtskKg6l3iIPl5BN1Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
باشگاه خیبر خرم‌آباد پیشنهاد معاوضه ابوذر صفر زاده مدافع‌چپ‌جدید این تیم با حسین ابرقویی مدافع میانی پرسپولیس رو به مدیریت سرخ‌ها ارائه کرده است. صفرزاده فصل گذشته درملوان بود و در مقطعی شاگرد مهدی تارتار دراین تیم نیز بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/28347" target="_blank">📅 22:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28346">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulAgyuE3BZ-oxH80iv_ryGrZoZ_iSdRfG97kiX8pZxAzr47LB-GsntOeyzSi_ajASyfoLsl5WtlbIRUAU8Dwih_Si0WVEaucPL1kko6hHFpZbC90puxUwxTQbkrfZ56YwFXceHVBMEF_dhabOiRDYW5-SMtucUiKezl7Dw0vibtkHvIJERFMYoiNfj3RO5uZyW6Pi2vU6FELI1Odhft21aqLYzVbFeBGRdq5G8tHrnpy_sSSabjuSBSumcTXJKgGl5a943OjYZr8d9Q7IJxPpIOB78uBPu8uT5yTgoalpwkhcFxPW5nQvMkNSCrE_2QQ2SzyVgKyEK2EAeKV0CsYAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بدون کلین‌شیت بدون پیروزی؛ حسینی به‌دنبال اولین برد مقابل‌استقلال؛ سیدحسین حسینی تاکنون ۲ بار با لباس ملوان و یک‌بار به همراه سپاهان مقابل تیم استقلال قرار گرفته و حاصل آن یک تساوی و ۲ شکست برای او بوده. او در این ۳ بازی گل خورده و اصلا نتوانسته مقابل تیم…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/28346" target="_blank">📅 22:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28344">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/djOiflUtgY359mZRZogfv_6rGevLwAZyj-wT5y_vgwxbBZuhYQyrvu4zkVL-TlXm0T7swsLVzBCkYixlkW3iKAdfw_KDpMFRc_TOKrJYe0gPljtPtZySgAl-5diXl1VCRi6QKSbe_TD1eQE41FOgngseAop4Ho0EnOQ0a-43aJcTNW-zVoLPIMGx0py0I8mQ1od5ZLPMHgeYRQLh7aiaPyZRDNBW7SR7H4zhrRpqCfYmJ47VFgPmaQrP_fUFA_kWf-P2JHUtwU2f-8ACl6v31ybTpuICDAXY7PcSgvaX3x62vg-cTnC47eg-s8ZM0CoTNoiyG9ETBCs6jSTCRqfghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TezgxwTB_I4JOABEWv_3eXz0MOflU26HKkOWdAwUM0sakJWLTC_3R9KqXdU2eWXOzlm4gVV7GeTVSNRUhh1Y4SMtikPost81-ByI1Z4nINxwcrrL2bldfqRmcKZ5g4a5EqX_fxR1fdnc94H_q6U443OG9MQFEbNIkuJ6MZwQsT7V5CSb3MVWFfh2EPFJmFrUwe82tviSCukyt8v6g-eDIakFhkXHl8mfIv6lsWRWe_46dELeEP9Vl1Sd3d4fBWSs3bvrneMdATvQNznYw_leFUumQ5xLz8mixqxTZ_dH5g06LayJOQxA7dgAfbAVwk3tQ9Xq_aOO-P0o2sc81EOgCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
جواد کاظمیان:
اگه ازم بپرسن بهشت چه شکلیه، میگم این شکلی: با جام قهرمانی و توپ طلا، کنار سرخانمم مونیکا بلوچی عزیز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/28344" target="_blank">📅 22:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28343">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVapUqfVjFVfeDXd6jer0ybQ9gPX-JErckBEDX5ZCVz1nfe4j667nBm_2Zj1ZYIVZE1Oqe4Q0-gLEHsOKbxSozcg_C4oNeSpfsDm7LqgpYP7iz84TYH4nPKnwerR7hLnelYydGExdXD7dhR7eYtsMF0sPsVoBWQmICChG80j_Ul5G-Byhz2UfoEMKm5-SFHk-0WzOdmGW0ds8io7ShxSwe_5gpjFMBsowWdbYrGk4f_YcU5BrjX9qbyLBDRBadrAahsRwKAzt68NHdOAj2V_MHIc58V_dfZbXiRO2HgZLoCkC8x3TXIBlhZuvgp4Ss6b7ik8v87W6xQZPtfzqWCSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی پرسپولیس در استانه دیدار با تراکتور: به جز تایم فیفادی به هیییچ عنوان بازیکنی به تیم ملی بزرگسالان و تیم امید نمیدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/28343" target="_blank">📅 21:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28342">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vD3sKnt1LjDy8ENt5WTpcm-xFH95yHZosaP3WTpl9ymlV43AKDKWOAxPnim0cnaJr8IWrqjybnxYSBkhBNlSm44eLrzAJZJ99-eLpfmkZURfDg1vAi9hdvX_OMn3ss-M_PfdBpj_cg-ySIuim8tPu-AYphLdeoTch_vsSB78KJLaW4VB5lTBZgc1wJwMpYjkC4SHY1jDi4_rh25gLxg9nc2-5kEnwhjhMFskHGCAMzxMmgeVtl2D7kgQrBipLSwOIP3aRmi5hgwJmhlRk9H3ddnMacg8WtC72VkZkBZiHWJWWWJEcpvnZGhr8CcQ9JJ6UCFxkZcr9WApSeLHwsvk3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
به مناسبت بازی امشب بارسا مقابل الچه در هفته اول لالیگا؛ نگاهی‌بندازیم به اسکواد نهایی تیم هانسی فلیک درفصل‌جدید رقابت‌ها باجذب رودری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28342" target="_blank">📅 21:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28341">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
خلاصه‌دیدار تماشایی امشب‌ استقلال
🆚
سپاهان در هفته سوم رقابت های لیگ برتر جام خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28341" target="_blank">📅 21:46 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28340">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeQDzBL1wwWCR-Rpb0zqLua_E2x_Sv2VxWZlQgssPBQTvyfQuzEyxuKaqWOPPSMXZCRTQGlNLMtib3fC2Qfx5lAGPd3p__eiDcIKHod8E-0K6uE1OjdeCnrwh6hbfAyinY0S8PdFpZWMjGCJubD6IeHxokc6G05yVCatDGDoe5j2oGxI6mkISJUHkIOVOmsI-_uLe7x6SKUNbhGuUHukxaAcenD4HnfwApyxn_NZarD0jCYGXOh8WTtRLseK_WBWYh9YhITnD3eyYqsj7BDUDJGjL56HBgxwMYJTEHQVU3BPw_thjdJl9U8kofkHHH6PJm7gBqCzUISyukVA6JKDPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم ملی امید برای مسابقات آسیایی ناگویا اعلام شد که امیرحسین حسین زاده ستاره تراکتور تنها بازیکن بزرگسال این لیست است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/28340" target="_blank">📅 21:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28339">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VP6LlggwX1YUd1IuBy8SKkUVYduDGOo7tSNv3luQd9WEc8caTqHee-XWuHHQ01NLj5Jx0ToOG9crmzAJu3HOAteg_E9O2nmX22Uojaw-52e9c_LVo3HD4--4RkYPt2Suv-b151P2ZUeTOgWo28Nz-szB3l8J4IDQzIVT6fEzUct0JSBbWvUGBX2TbTQS-UiTiWX6G2ftTA-sQaRAfsVtzAy6n-ncazlNKl7_Dx7-NWs2h-uxGJ4HFMh2M8ZtY_0ZNcMl2QUylMNg_G77tzbPdEFtzQvyucTcJu35w9D0jUn9kGceOiEbmzW2LctHOSNpqsjK8I1dH2ywFwpU6WdQFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی ارزشمند و حیاتی آبی ها در تقابل با طلایی پوشان زاینده رود با طعم کلین شیت؛ محرم نویدکیا باز هم به استقلال باخت.
🔵
استقلال
2️⃣
-
0️⃣
سپاهان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28339" target="_blank">📅 21:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28338">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkprdPQhBp5CfOa_igOB23j8c1hDHHWdSQppboqoaUQ3P6hPBRnD1O_mx0JQv2_QDlveKsr6Qc40Ueus-LxfYwzBMV2QK_aeOWgVygeFVlFhbH9mnlLLxcm0XQvqVFrc1JaMeDR3LlzRQkO732gZTaqGa1BDYjv6xezmB5x7LaEwawCdjwTbFz-ius9PactVZp0eio6LSMsk19RnqnTGcWWparJDcUOR5oZBjf0MpDgBhuNqJ7r9Kj6LgWIhw0fY7BHl1BPVJVZ-SUkIhhigsFCUUFzKP9_D5yOOQwFUaZx4gCAuK_cfFNc_0S1UjabbaliafCTdVqR9QB78Gus_hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی ارزشمند و حیاتی آبی ها در تقابل با طلایی پوشان زاینده رود با طعم کلین شیت؛ محرم نویدکیا باز هم به استقلال باخت.
🔵
استقلال
2️⃣
-
0️⃣
سپاهان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28338" target="_blank">📅 21:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28337">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZo6rhiKSq-IhGB8PcG1ey8DqVKTKZ36yUKM6s-wy6qIEWtenFNUv69EdgBno87ty9wAXQWrXtNo_qe1t2NCOxDcLIp-koQz2UP2Y4glBKSXm1hPV-S4-c3sG9XLq-X9erA6W54L9NltaD0Na-mUim-pCv1RIZJ5qja4S0RMJUlNGMq3CjF4ZXioCg111wjvhviMjMD48u7Vg9eaDBCPt6sx_eo228Mj1UrFEWWzviXfXcjA2iC3xiOq5NvlHTxRipaLBkpNs6GE6GKih9PyiH2uazY-Rn-yMcfD-xeFUmKGTW9XKWxy6SZo4zXziAO-xkdyr8FQgP5hdZpz8Jo23g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
حسینی دومی هم از آبی‌ها خورد؛ گل دوم استقلال به سپاهان اسماعیل قلی‌زاده در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28337" target="_blank">📅 21:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28335">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXUSSxSIEltR3G0fseSqsYL5_akKc8jNdVPlsr5xI2vTH40mp5gSCBIoN6GyZ2m4ObnourhKqfSAwnA72TODr_7r_y_swo9dmKGXCuwiQaX1FvsiI1KY85WW5XrzHkdmz2rluN2TMxS9az5uGuqeVA21j_WaZFb_f24gpAWAD8X2Ys-luRkJRfNGn0G8IdUuX-AOuuqxJzQ98XtDLV2JZK1jzGSB8fvCJ7z831bpHhK0nEAvhOOtdfI-MdctBYi8FSvrEh_QUDfKC9sFTFkb1INoEs9hi1UrciR19FaAJ14RZjkG-EnAta4RcnkhsHaNNnfcY3FjNAlGiRYDVeACwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXQIywC1ZKv2o0xt-yLpAW4KNakaHjtW1Cp8ellieFWbImMa3-3t_qeBDQoaL7iglIcME-u4uBUI761D8rUxQHCV5b8A8S6bD-l77ImAM6XBhek07LXhD7UO6hdRtOopJvuLrfcYHeFUhspeutD7PGwn4ewYQkIqZAcxRUnCD_MBBEK5iUQgpbEiITyS2fLmMIt902OYZl4Q15AtPkfM4qMW21_0hybd19DvrEvya3krQsVUsxK8zXiTUCjOdSqIURX96DuZufF5bGSkq3nMkIK2xQkIhDC22LzGmOfzu0IBQmr3vm9dqRvmMbfTorFmUyAERyklYTEignjSFkIDnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نتیجه دو دیدار مهم امشب
؛ فرار سیمئونه از شکست در گام اول لالیگا با گلزنی پسرش و تساوی پرگل و دیدنی لک‌لک‌ها و کلاغ‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28335" target="_blank">📅 21:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28334">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d47b1892e.mp4?token=CdgJVMYn5mU469YdGxYIzP7DPdO9wOTDNnXwjMpX0Xo7nr-iyU3wpLOOojtq8MXXj1tI_Hppk85vdgMVI_xyLXXlpWZQbYkkH85rUS3RcUo8fbM1mdEHbvp4rX5B0AsFBMRK1_V26Kjk8k-YXlYIAMyo3t3cDFsFj7EkwElkzmzHqUgeltr1Pa3_CnLjOeuH3IrEW7ELwLPXPvfIA8iVSZ_Gf4Ed6iamGLi8s-rejXn7U24dpjByuBZjyaqPMlCLQg28pzAXp9LjhFHEJNcRB0joxR7E8pb0_BxDBZOs0tN8cJQrDFnKbDI3kwzW8dtjVuTCbNinWN4GuIFNveD24g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d47b1892e.mp4?token=CdgJVMYn5mU469YdGxYIzP7DPdO9wOTDNnXwjMpX0Xo7nr-iyU3wpLOOojtq8MXXj1tI_Hppk85vdgMVI_xyLXXlpWZQbYkkH85rUS3RcUo8fbM1mdEHbvp4rX5B0AsFBMRK1_V26Kjk8k-YXlYIAMyo3t3cDFsFj7EkwElkzmzHqUgeltr1Pa3_CnLjOeuH3IrEW7ELwLPXPvfIA8iVSZ_Gf4Ed6iamGLi8s-rejXn7U24dpjByuBZjyaqPMlCLQg28pzAXp9LjhFHEJNcRB0joxR7E8pb0_BxDBZOs0tN8cJQrDFnKbDI3kwzW8dtjVuTCbNinWN4GuIFNveD24g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔵
گل تماشایی ابوالفضل کوهی در بازی امشب نساجی مقابل استقلال خوزستان روی حرکت انفرادی خود؛ کوهی درآستانه پیوستن به سپاهان قرار داشت اما در نهایت شاگرد مجتبی حسینی در نساجی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/28334" target="_blank">📅 20:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28333">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu_DPm29bdkO3qjpY00iTGMDGGhZStXm3876ZI17NJGt0Bx9df6yCig5_ZKcam6wkNwEwGgS1-xlFwKmaC_e09NThvSASfnVRteMZZLodhf2foaNThTUVkg9cwWuCHUbpnu4DCsfHvUo22e4176DTt2VUphgfMlYLHH7icnVmjxc2mJxJ6QT7mL0qtoEWHNUQBB2BqxWRVpCMR6Z4KyZ9C2gCTZUzvpV8QwMS7PxzLmYDIXBouun30ADWKLx1mEPmjmY9m4U9b2qjWxQcrJQZLcJ-gKGsjlZNZj692NPE-XslfOkjDBKVH3CJjVzTS63xxB-gzI3_yVvdRkXeVLXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
دروازه تیم محرم خیلی زود باز شد؛ گل اول استقلال‌به‌سپاهان توسط یاسر آسانی در دقیقه چهار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28333" target="_blank">📅 20:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28332">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YS2lyQeIcXSkJ5FziRMH7jSrNviy34pAzP_jHeGQbN3j52ZxIH8OTvQAxlVvkcl23Ez-R_35Mn4tKUMwdNt7dRGJ_4yc27NlmkGebvD2ZuvPCWC5VxZyFfAzMQ7rJ7gvXJ5vmsJWaZh1nN_cbrdvNQmVLwkL6FFcvEiu0mCWhMVRLUkmpbvlm6HyjUXvGxsM_BOykIT6iIJFmBF_f6pIJhWvUYPSK5uL6TAHv66nr83YdKA4SxtQ2-ifZnNxD9817YPfjCbWFAPxYot87TcjzNO9R7XfMURENnh1021AxfWdRlAIi_h-gEnZMgruXqkr4wz9QBc06EjOAY6ETt8Vug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
حسینی دومی هم از آبی‌ها خورد؛ گل دوم استقلال به سپاهان اسماعیل قلی‌زاده در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28332" target="_blank">📅 20:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28331">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3797b4f0c.mp4?token=Ti6eJdWNn6AcCrFIqA1ZqvRaWXOI8LL3A9jG-MJrxa9I1FJZN2AwEZeYuzguC6aeLFyxVQAWlE1othd_yKx83I5yzd7MvdQwQ1XButIk1nFYtCBiQRUtSHj-zgCojLZSFNI1wQ4VoNiXvd6QddJkdXRWi1XT8utztqphpd2fdVi82Et73M5XZZBjduOj2c5p7SDHMSqgVnioH8LXQR1dV01acwy1PN6VYM8WAHsAtLoA7PMmCY9q55LGxp6gNUYLWr7TxSpjqkEjBU46XbO0O7JCcgvatO6Z7sIweQ2n-sMMS4mpwb969LVl9DAHj93nP04aR9EANAqqw7G1Pp8mmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3797b4f0c.mp4?token=Ti6eJdWNn6AcCrFIqA1ZqvRaWXOI8LL3A9jG-MJrxa9I1FJZN2AwEZeYuzguC6aeLFyxVQAWlE1othd_yKx83I5yzd7MvdQwQ1XButIk1nFYtCBiQRUtSHj-zgCojLZSFNI1wQ4VoNiXvd6QddJkdXRWi1XT8utztqphpd2fdVi82Et73M5XZZBjduOj2c5p7SDHMSqgVnioH8LXQR1dV01acwy1PN6VYM8WAHsAtLoA7PMmCY9q55LGxp6gNUYLWr7TxSpjqkEjBU46XbO0O7JCcgvatO6Z7sIweQ2n-sMMS4mpwb969LVl9DAHj93nP04aR9EANAqqw7G1Pp8mmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
حسینی دومی هم از آبی‌ها خورد؛ گل دوم استقلال به سپاهان اسماعیل قلی‌زاده در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28331" target="_blank">📅 20:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28330">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/620ce5c574.mp4?token=mxkreyPMQjQSUeUsRIwyLebIG3RsVAmIZ0uFBV6DGQcQy1ehkeuvKGWriYdA_FOKZTITCisMM-Ont7cZ13I7peBI5ZEC0HvoWpYPr6uQWRP9_coPX5Ch82O_UUFRBDYFadG6cQmqV3dZB1eTXaFxVJDIvEI7plO-IOFxwEzXxe2LgVJ9sL8jDghvwe3ALz17MwEMSJPv0V-BjobE9knFnD52sOVs6aTcyoXGEPrewQ1omjROeb0EQN55Y3n3RVcSuFJcLdKj-kMVvevOjSKwTaZ5HWQEYAEstciitDb6h12DQQgG0BiquB5V9DL19sAxIOebvrnf1mwmGQXJfNhLeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/620ce5c574.mp4?token=mxkreyPMQjQSUeUsRIwyLebIG3RsVAmIZ0uFBV6DGQcQy1ehkeuvKGWriYdA_FOKZTITCisMM-Ont7cZ13I7peBI5ZEC0HvoWpYPr6uQWRP9_coPX5Ch82O_UUFRBDYFadG6cQmqV3dZB1eTXaFxVJDIvEI7plO-IOFxwEzXxe2LgVJ9sL8jDghvwe3ALz17MwEMSJPv0V-BjobE9knFnD52sOVs6aTcyoXGEPrewQ1omjROeb0EQN55Y3n3RVcSuFJcLdKj-kMVvevOjSKwTaZ5HWQEYAEstciitDb6h12DQQgG0BiquB5V9DL19sAxIOebvrnf1mwmGQXJfNhLeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🤩
پس از کش و قوس‌های فراوان خولیان آلوارز رضایتش رو برای موندن در اتلتیکو مادرید اعلام کرد و این بازیکن درجمع‌شاگردان سیمئونه موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28330" target="_blank">📅 20:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28329">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8acaeec43c.mp4?token=X0gokZm1TtpWSmgG74fXsNgzn3wjPQYGTT9KCfMbcN0mu_Z5_ICbOjzYdK2tCsWtaKF8Wa9HsTXGcTYyij5d3mGp0h-VfwCWVyr0kNnXWaJ5PbJGZigoabeaH18FWCgjV2WKfJ9gN83fWCEvfn881PRp9g3EZ-plekTDeef82U03oEOXXFE2Fl6fpZTF1cGV8nszTMkAo09bidDrbww2A-1qF7phQ681QC0DBWWBowAKhyxSpUkrYaBM8buv5vVf7ip1ZzUaVB5SPofk87cmI9BS9WhiYy-XOPN51KnD-bFqdFly6LKQkqOF4wGHHeIlbRiQElkUpQGAFy3h0ZLa5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8acaeec43c.mp4?token=X0gokZm1TtpWSmgG74fXsNgzn3wjPQYGTT9KCfMbcN0mu_Z5_ICbOjzYdK2tCsWtaKF8Wa9HsTXGcTYyij5d3mGp0h-VfwCWVyr0kNnXWaJ5PbJGZigoabeaH18FWCgjV2WKfJ9gN83fWCEvfn881PRp9g3EZ-plekTDeef82U03oEOXXFE2Fl6fpZTF1cGV8nszTMkAo09bidDrbww2A-1qF7phQ681QC0DBWWBowAKhyxSpUkrYaBM8buv5vVf7ip1ZzUaVB5SPofk87cmI9BS9WhiYy-XOPN51KnD-bFqdFly6LKQkqOF4wGHHeIlbRiQElkUpQGAFy3h0ZLa5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
دروازه تیم محرم خیلی زود باز شد؛ گل اول استقلال‌به‌سپاهان توسط یاسر آسانی در دقیقه چهار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28329" target="_blank">📅 19:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28328">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f358d6852.mp4?token=Ov3I9_I-LdmV7IOPXZ-sk6gHOA1rsim7V9d_QSSYi7kgTCetOr_EGaqXKlnqmg-I92YDYiqsJexgKyUeGKM21ZU8VFVvoRUHzwc3qgtqcxI3VV92eJTZ2g7OEK2sxyCRF09tMmH0_r79E13a0mCEXMYVK9rLjsI8s7AppzWHvXDH4jXGcJx3ihzgXv76_6a75ymOTu-AExemfDw3xz2jBBbgszUjovdDfeX9EO4zHgyjUoHyAyOeJkjeE9KwqQamcDxS7eLRybpzVuFNoEXk-NQplq6vgNrMpTUlH57pgHNhQ-c5lDMqixIpU1S-Dlv8GKmkYWZCkggxmfcPmJCEBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f358d6852.mp4?token=Ov3I9_I-LdmV7IOPXZ-sk6gHOA1rsim7V9d_QSSYi7kgTCetOr_EGaqXKlnqmg-I92YDYiqsJexgKyUeGKM21ZU8VFVvoRUHzwc3qgtqcxI3VV92eJTZ2g7OEK2sxyCRF09tMmH0_r79E13a0mCEXMYVK9rLjsI8s7AppzWHvXDH4jXGcJx3ihzgXv76_6a75ymOTu-AExemfDw3xz2jBBbgszUjovdDfeX9EO4zHgyjUoHyAyOeJkjeE9KwqQamcDxS7eLRybpzVuFNoEXk-NQplq6vgNrMpTUlH57pgHNhQ-c5lDMqixIpU1S-Dlv8GKmkYWZCkggxmfcPmJCEBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
🔵
شعاراحساسی هواداران تیم استقلال پیش از دیدار با شاگردان محرم نوید: سپاهان دوست داریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28328" target="_blank">📅 19:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28327">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ae17874e.mp4?token=EtkGMssv2h09iuFFGNpmamFELDjP34ecdwYIkUwqCaUvJUP3yfHKiziIK6dSe6I3zPOFM-jeYVEAdTwXggnJDC1-QbBwEt93GY6Z3yCDC4OTAYtyJdHQAumBszT5ewLiOC3EI3jilgItFaDs98yiZspeiU0RtIh0UL3o81O0SujG9i-7Id-Fc_PK0W2t5HAGbfomZuV5yUBimVmaExcLNKkEaT8V79MHS1gQWXDKmTG8q_FHfPIYEStfoCnIHcmF_OtUWe3OrX_zLUm8BpF30pxxg8mvrsYUGMpH-Osb4mT8zymMyV90zSfpP5Om1_LnMAAXCPm_CpUITqhSNWCD_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ae17874e.mp4?token=EtkGMssv2h09iuFFGNpmamFELDjP34ecdwYIkUwqCaUvJUP3yfHKiziIK6dSe6I3zPOFM-jeYVEAdTwXggnJDC1-QbBwEt93GY6Z3yCDC4OTAYtyJdHQAumBszT5ewLiOC3EI3jilgItFaDs98yiZspeiU0RtIh0UL3o81O0SujG9i-7Id-Fc_PK0W2t5HAGbfomZuV5yUBimVmaExcLNKkEaT8V79MHS1gQWXDKmTG8q_FHfPIYEStfoCnIHcmF_OtUWe3OrX_zLUm8BpF30pxxg8mvrsYUGMpH-Osb4mT8zymMyV90zSfpP5Om1_LnMAAXCPm_CpUITqhSNWCD_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
شماتیک ترکیب رسمی استقلال برای دیدار امشب مقابل تیم سپاهان اصفهان در هفته سوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28327" target="_blank">📅 19:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28326">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8b132a0ac.mp4?token=YrHGuaK0uMOfmFEJgF1wyzgsU3VGaKu57ZwdG8pUv0RuRlIMuvgh1pwvxGmb2bVOBuynk2hGngXmOwosARbb8qlcK0aPlwPJLgOFCoUcqkjkcHTEzT-sHgIRyvUYeifTDUyyIfc1Gui36mniqj2rsHKSr2MeobM4NZq5DQJZJOhswI-FcukeDUUZMC9i5RJxH7eWq90pHisexnUJPS_9G2nhutcUUKSfwtb-AABV70PCZjgy_jIdxiuzVtIRTZ4vSrnkeloOz-XCLkxTP3zVf3O56DyZDqbvEQa0EWz5WI6NG7kdnbQbz2tsnH1l2Qo3Bx01QDR16RBvMdI6yXiNEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8b132a0ac.mp4?token=YrHGuaK0uMOfmFEJgF1wyzgsU3VGaKu57ZwdG8pUv0RuRlIMuvgh1pwvxGmb2bVOBuynk2hGngXmOwosARbb8qlcK0aPlwPJLgOFCoUcqkjkcHTEzT-sHgIRyvUYeifTDUyyIfc1Gui36mniqj2rsHKSr2MeobM4NZq5DQJZJOhswI-FcukeDUUZMC9i5RJxH7eWq90pHisexnUJPS_9G2nhutcUUKSfwtb-AABV70PCZjgy_jIdxiuzVtIRTZ4vSrnkeloOz-XCLkxTP3zVf3O56DyZDqbvEQa0EWz5WI6NG7kdnbQbz2tsnH1l2Qo3Bx01QDR16RBvMdI6yXiNEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترلان پروانه بعدِکات‌کردن باشروین حاجی‌پور:
بزرگ ترین اشتباهم وارد رابطه شدن با این آقا بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28326" target="_blank">📅 19:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28324">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CT-mH9uUPPMVyRyNcfhEKUk_CUcJoUXb49KJCxKR2uGZdMVLHHcjuf8rAeiDW7r1fVIekZJfTz3RqhAX5pwVJ9fxYGvMNNMeu-1Rv2dtFZJWQhqWPYadeVluIxddFuHDY2L35BXNeCsHFKE9zuZ8tJUKoYjeEQnbqdIea03o6zACkaa3aPna3BBtlRKKmMuy142Of-bbJuWkxV61aaGyPOzNR4JxUptoc9LwfzzuSw0kdSeZ9yK6vO5XBUNylpXviMxnoHle0qi6KqHGzhIuuP-3qh_yA0OAMh_o87RGBNycWL3ng2xDlGaAICx16Oa8PTPOR1vx0-WvMTmKFC4hqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
10ستاره‌تیم‌منچسترسیتی که همگی بعد از جدایی پپ گواردیولا از جمع سیتیزن‌ها جدا شدند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28324" target="_blank">📅 19:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28323">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhSVHPAXhbRwylllTcZofn4Itxqlh6DdTfx0xCRiNlqUp-lS8MyoQCiguKbJLt_2U9dXkBqxVh1JzwmdCwn6-93yDcjtUfQ-OrC4BcasleGY3RfNzgJg1uWzEk_OBYVG6JGgxecb0dGQk-C1LYF_4n23L0bQLKAE9tChEompagFCH25alL1kZ5HHPAFMU0gc_Qaa_BugRlVCxvf1ayZdZCXzoJ3olBRhOwxcYJjONTWdstxztNwgFSU4eLv4AeGsGI94pC5Wf0IMsBOx6nknyOvvQjjynTIlPcxpqHRwXVnozQraA5wkdf1UCi6QMnYtTnbv77bJWpMMXGYJ0qwY-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی هاشم نژاد دیگر ستاره پرشورها نیز به دلیل مصدومیت دیدار با سپاهان در هفته دوم و دیدار با پرسپولیس در هفته‌سوم رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28323" target="_blank">📅 18:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28322">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN4DRuB0WGHUsjuGs6I3xY21L9dYwT_O1tu32kW_H7A2EPRh_5T2o-WqOKx2I7FlUtv-RIFlX7iT9_JrKneBAambeeB9YYtYt0Oxw9I-4iXy-PGILNxXgo2Mi7aCrHmq5lKiGBHqeaAJ_vOoJvgXwoVqhYoPyp6DmGKJyDHSD8EY_sjCpG1R4g6rPxp_H9jCzi_3QC0uK6iCjgQ2RZLg3i0vMDdp4V4g2P_06qzbzzuRTFZTuc1omKD3sDaL_148ipzi46pwPk4zj2ANc7FTlsE_IHEKVIvZl6vNJLubm4ZLpMoArmo9f1-fjPMF_sYm7R1czd148CbupHIuGiUwGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شماتیک ترکیب رسمی استقلال برای دیدار امشب مقابل تیم سپاهان اصفهان در هفته سوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28322" target="_blank">📅 18:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28321">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVjgBKwKrGt9bTpnhwo62v8JpBeTf1OASii90wcoukA55lQcK8-vPzLEc_J_WJs3TbMR0VSDG8UTm4Ax5dHv0WZEU5jvkVgr4YEdnObO3LXcnranOatm7dOGOIho570X_IZ_N_BuD2xcW0tqBwdczDur74e3060iLjANtpbA_HQGYvOVS1I1XsaUkE2kFSJr9HSNA5try4GGcs--r8wjCJwSmxMspuzMbjYlGYQOmSB825vVuQuekE5YuCCnAty1khLqNlJWcCkr8ks5UXKBbUq5LPlliqq7ZIl7XIFUG3f6JgoypjElTBwyOhe0mhEC_yV3_Cdk8dBKIOVE1qVJMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته سوم لیگ برتر؛ ترکیب استقلال برای دیدار مقابل سپاهان اصفهان؛ ساعت 19:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28321" target="_blank">📅 18:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28320">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHYenjoZoKnuCfW_vhfMCgj4Ikn_etZAtu1qa2Cmtg84L8PrSOgYkuG8FcKy04CWWdzBlP_VYBrSyIdbeDW8Q-akwf6RtoBNcKq7evtkUZPU9wDRbWWrDMH_2243_7OzlSzX-xL3KgODiJ8xCzqD0O2QO8trSE2D6pGfAB0q6aJxaoGpHapggaD7M4AY0W1Z3FnpxWWmYzhFEJyoIH12XmU1GWPT-a9X4w8yuTdgvPnVL9bgVCD1rmTYNK3q_VVfY3LcbfwKmI5XE1QcdLO5kULK-n5kh0y0Gpg2xjdIlogWi7Php9W1R1I7Ose5XSYKJM4Lz-m34aBNv8CvPLbAzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
ترکیب احتمالی استقلال
🆚
سپاهان برای دیدار حساس امشب؛ ساعت 19:30 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28320" target="_blank">📅 18:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28319">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXH2OVAqPVit1epcBSiY7mgsbI2MN-ZKrO1OMddaLrwkcp5gEBmKVsTWYJ8Urnsz-KPaiKVa6rn_mmyfoyOFuy5F4Ts7SmVzuVqUgRmQa3v_cWK22Uo05oCTsO-yDSPahRXX5HU3iNQFvo7FrAYQNI1t71aKTK3xrwKlC7b5p2cpj-fNbcaN-oXnHERFjc2YcTD8K1s3vn_qQc5zrCEw2gVoGlpyrJXACTLkGfAoqLtKgOoCpcd4qe-jkQ1-fLPydudnQUKoAWsUEDnyMnO6IefezxrZkr3otJqsE6mm7Jz7vXwk73YaYG5hKx-5JPCpT-C_weqIlIB7h26YdbPt7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌‌ها؛ مجید حسینی مدافع تیم ملی آمادگی‌اش را برای بازگشت به استقلال اعلام کرده و درصورت موافق بختیاری زاده با او قرارداد میبندند. حسینی از نیم فصل میتونه برای آبی‌ها بازی کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28319" target="_blank">📅 18:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28318">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afotAbHh8VU-7MfniRktire0MTZiCU7YwOQSiahuW3_ipdygBe0xbAoBI6arJ77YlE0VBl2O4qPINc2V3E9gjT99ifYTzMXi_ooOylUIPN88U_E-mjpmlQ9-1R897PHICakkZdj7-FmxppETlQfqLl-13m_sYIeAEVta4Hir1X7fQhvZ6ytezZyWKZecofKzfaxX0lp4MlJpJ-TRqFgy3emZca-T5BlN0VYfihhsfR_7z67C9DEe-kd8W2MSuGZacOtOGuJfUxK1ET_fBzSepK4wUQzvy2cEY77MmdEJ9XfqYjfurNuaCovbMcu0xTLChxhsG1el1NBTWXiq_-VWXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
باشگاه خیبر خرم‌آباد پیشنهاد معاوضه ابوذر صفر زاده مدافع‌چپ‌جدید این تیم با حسین ابرقویی مدافع میانی پرسپولیس رو به مدیریت سرخ‌ها ارائه کرده است. صفرزاده فصل گذشته درملوان بود و در مقطعی شاگرد مهدی تارتار دراین تیم نیز بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28318" target="_blank">📅 17:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28317">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3040660e7.mp4?token=upX3THF-E8XiFJVtfb6SL9-QKHkxbz9j7zFELY-bmTxPLPGz3uvnnZBBnIp80iH3_cKuBiXgJnxFes6OTz6QS6RrFc_CBdI0yVoTHFWq4u-R0uzatDnb_K7fyn2YmfqOVWb1Ax4mGJIHO5xkJQJWZMf4wimGwyPKdrH7O-A4OJD2IToqe5cJRM7EPsRKno0PCuq_Tpk0nv1neNUjowZiY9-HsTCPI_WdQV32X58TMu98Is7Yl65cWmQLTt83vYJxTvL2pc8zasuDBoQ56Duk89x9MP57N3WJcnWNExpjt8nEdDexWm_AJ5YfPajXkImGZuXfKks1KFVhDxfBu26smw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3040660e7.mp4?token=upX3THF-E8XiFJVtfb6SL9-QKHkxbz9j7zFELY-bmTxPLPGz3uvnnZBBnIp80iH3_cKuBiXgJnxFes6OTz6QS6RrFc_CBdI0yVoTHFWq4u-R0uzatDnb_K7fyn2YmfqOVWb1Ax4mGJIHO5xkJQJWZMf4wimGwyPKdrH7O-A4OJD2IToqe5cJRM7EPsRKno0PCuq_Tpk0nv1neNUjowZiY9-HsTCPI_WdQV32X58TMu98Is7Yl65cWmQLTt83vYJxTvL2pc8zasuDBoQ56Duk89x9MP57N3WJcnWNExpjt8nEdDexWm_AJ5YfPajXkImGZuXfKks1KFVhDxfBu26smw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
🔴
باشگاه خیبر خرم‌آباد پیشنهاد معاوضه ابوذر صفر زاده مدافع‌چپ‌جدید این تیم با حسین ابرقویی مدافع میانی پرسپولیس رو به مدیریت سرخ‌ها ارائه کرده است. صفرزاده فصل گذشته درملوان بود و در مقطعی شاگرد مهدی تارتار دراین تیم نیز بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28317" target="_blank">📅 17:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28315">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qa_ZqIJwHkO_6f9rWvjXQ21UyqQs99mvphzE5cMuQAokiICcbFxtfKkQFj1x-fm7YVaujH7hL_RYBxdurvqeYbaWUzmKey21CxenAKb5erkoypCNI10ecn2A2iBNPPhZkmLkiPLDDIJCpjZFlKZkJSY17P3TH6x59sKjF9CBm-LI1LITzWc8acyg8rf2DKsdeOQ01teGAq1eshMwk31A2F5fWw3YeqNLC4Kqn-93SVOByBziXZN5wJ5TD9UYc0jddF9BI_8vxFTYuCv7KarwH6okhYLspxdwUYivX6Um2QAF2oj3fhQQ0g-rRG18hAiHQXwB3aq4adUjOEBKLv-4kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8f8039bd8.mp4?token=oe9Hz1K68eEQkmdw281vmb1BO7uyUsTyxHrn-0w380HhX-wg014bRnGTTHnBdK5Ufy8Bis0KaUeRMv4YLtdxRG3yCXynbHI7NoPnhZ5wi9pPUNMcBH8dZsKH7YkAHi5pCGoBw8ZwccKtY-QHN-5EzxIItI0JWgWSMH_Ar9VnmvHLWzYahfyIrtvwxg46x6QgkHYSw2FrFDnKIObeWq2XgV-zs3-d5SQ8Ny-sj50wpA5vgKqJHt_LMMpog9SCH5gEukSDzkR6ET9pO_vCMkwrjOptQxhqpDB1UdnKe2hvNQan6XkdBWix-qcm7MeXcENYos6I32yNlHxjnCJwXVeWQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8f8039bd8.mp4?token=oe9Hz1K68eEQkmdw281vmb1BO7uyUsTyxHrn-0w380HhX-wg014bRnGTTHnBdK5Ufy8Bis0KaUeRMv4YLtdxRG3yCXynbHI7NoPnhZ5wi9pPUNMcBH8dZsKH7YkAHi5pCGoBw8ZwccKtY-QHN-5EzxIItI0JWgWSMH_Ar9VnmvHLWzYahfyIrtvwxg46x6QgkHYSw2FrFDnKIObeWq2XgV-zs3-d5SQ8Ny-sj50wpA5vgKqJHt_LMMpog9SCH5gEukSDzkR6ET9pO_vCMkwrjOptQxhqpDB1UdnKe2hvNQan6XkdBWix-qcm7MeXcENYos6I32yNlHxjnCJwXVeWQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
🔵
ترکیب احتمالی استقلال
🆚
سپاهان برای دیدار حساس امشب؛ ساعت 19:30 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28315" target="_blank">📅 17:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28314">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psdgfDxEdJDReRAfMpIYJX7q3ZiVPt2mO6YOA9o7onX1fcrWhy8Lv1O6tX8wUlILgwClrmvlQ0y566IH1hltDpi86e8yTXe7tVTP4pv3d3UkA7ETF_Pb9AoZ5g2PiTW7aYfM91UWMM4kSR5ipGHn08D_F1j-h3ohSjrP0_heTvoV6sDSo3cGYHOHOblOjPUqetiWzE-Iz_zep_e9vWUH1ZgRfKR33zXZ6BCC2q-FVegmax9pWhG5RyS-UFe2K-AHsqRPNF2CmtI_pCng_gpAB_8X-VQXBy1_rzf9kafvDe9oV08mS5bod9IawInHfzrdCzUE_bgu1GeL49N_lPJ0dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محمد عمری ستاره 25 ساله تیم پرسپولیس دچار مصدومیت جزئی شده و ممکنه کادرفنی به او استراحت‌بده و دربازی‌حساس‌باتراکتور غایب باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28314" target="_blank">📅 16:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28313">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00386372ad.mp4?token=KChE9lRn0ArGnf1K-_UN3sD4ofn6jnc5lYRn4tsKb05O5LN590L5toSFolWwDY_MY044YLifapqKTBARdfVeAYpLNA5vZNNGQKFkH6q7OJaz_TwzLmpplt77w5aXiDUHTyTL_lberUoUJHdUYafmkUze3rs4xlGcWsy8ADyWY4x2q1zP5m7pmBWiPgc2xSjBRQVcDHi0Q2Rmkf1oIfwHsp7riEu_zw8duQ1AaWnc4VrNG0in-NJIzTnYVTX54Xn9Uiw7K5Tws2lrqlxCagmTJXfE4pK1XXH8pO9VvJpkPgVg__K7pcwsylaKKUI-eV49X1XkCXCxNeOQ5Lg4AZHJnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00386372ad.mp4?token=KChE9lRn0ArGnf1K-_UN3sD4ofn6jnc5lYRn4tsKb05O5LN590L5toSFolWwDY_MY044YLifapqKTBARdfVeAYpLNA5vZNNGQKFkH6q7OJaz_TwzLmpplt77w5aXiDUHTyTL_lberUoUJHdUYafmkUze3rs4xlGcWsy8ADyWY4x2q1zP5m7pmBWiPgc2xSjBRQVcDHi0Q2Rmkf1oIfwHsp7riEu_zw8duQ1AaWnc4VrNG0in-NJIzTnYVTX54Xn9Uiw7K5Tws2lrqlxCagmTJXfE4pK1XXH8pO9VvJpkPgVg__K7pcwsylaKKUI-eV49X1XkCXCxNeOQ5Lg4AZHJnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
🇳🇴
واکنش‌جالب پپ گواردیولا به مدل موی جدید ارلینگ هالند؛ هالند دهن سرویس بعد از اینکه بازکات کرده اولین نفر با پپ ویدیو کال گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28313" target="_blank">📅 16:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28312">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dbo6E3t5b9dJM6t4bJgQXxaYWHT4B1F-pjmV-wHf4VgeW_Co3BAkvqqQ5ROtSf1q6oa-LrAZ2nR3eLn4G6gZSTwFxcPFR6rA2EMOuC4FRLOvSmG-nbIcsYsK1G0KhtJ1_gTgQBC1qqWiLzfUw34UpD4pCyhEGvSMVAXBvfQ0POeXgRRuMtVJzXUNin20oe2Pd-L0h6VeDt-uBf6ZC3KkItqaiZMiz5RJT-roiEAtWS9yEjfXQQCqJ0VIbT2cODJLnrePEQ_hBEOUhLR8y2Fm-_m8_lLb9gH9tomtq52i-IUrTDFm-9usQS8S9t-T5Ir_YFJRzdbRyfoENd25iOhQYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شماره‌لباس‌خریدهای جدید بارسا در فصل جدید مشخص شد: آنتونی گوردون شماره 17، کریم آدیمی شماره 14 و رودری هرناندر شماره 16؛ شماره 9 آبی اناری‌ها همچنان خالی نگه داشته شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28312" target="_blank">📅 16:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28311">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZ23My3fwPG0zisWpjfc8B7djPRThkj2Fr3IhLusde5f_JVbVKyY-Oj2hMsz3xGfG5n9-RC3q-Pj8y7LsZM6zNOaiAfXXjAdvOvaMc0wwvXKndrZpQkaJ-mAhCE4wD1M8jWxwyz1bbRGGoU3E6kSweENYAyrhVcxKEq40pw3Lp930hlqHlSUbMFmwKyEhg0ipOrskgWrT2T3kCDcNANVfg__XFaxD0HrbBoqoazAJcyhn92BlGW7EYDZJkytOf7BnpfE9CKo5lxxJgnCzZmof69dwRcNKOQP2KcaJrxU3ZQX11y5D5wOzF6v8vEWzMA8RlmQaxu7s144LrKQ-A4PTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ازهواداران تیم شباب‌الاهلی امارات هستن که علاقه‌زیادی به سعید‌عزت‌اللهی هافبک ایرانی این تیم داره و با پیراهن عزت‌اللهی رفته استادیوم مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28311" target="_blank">📅 15:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28310">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsTPx4RsmpzZ7pcprvzfqvN9yV3KLQnbEwI3Ge95KE0wJl8SWP8P8qhbY9AHuhOQTtd2t2V9fuYaHdQvtqoG-FPfJH3hvApYamojUvktObjmQop1gpD34uA6nZk8QvhKe9o4r1c1ELRg9_Iyb6zr_r19pBanzXsP4A-UitTg2HZ_fQLTBoiWQERQUwKs09aRDOtEb4xzs96-w2vtL0cs3X05ZzOEl9RQN-rcS1nEdoF7Y4e8H7hKlMgC_gSCY_QtaNteB_Wyxf36TdZIlGcgEMHzTh1_7BrkAoAGQsVO3t6PNfTvbUoLEGZYeV3HebFDIBJtkE1rkrN69_BL79ZtOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا: ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28310" target="_blank">📅 15:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28308">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa9e980fe.mp4?token=e1q4X1Nb7iPg_dbWXTPP0y3XW-5PLAh9icLMA3QstH3JtXK7vGaMOkeTGHwV4awZshrMA83HMutae-qOBLs2moJ-ojH5S8gHo6lZMg-fgZ5I-74r-PGuoyL2k6zjVNKoqEiabjITeoRNU3S2ksOEQ0NYNBYtpksoTnWJqnw-rlWlSwT3b75vBiJOb-2tw8usO2JbzvDJzE7GPDfOxEXFs-O5pTuaY7tK-i5v4hLIYR6EuVmqamgprb5dJlnx2Gfggzzphua1XSdj0FiUAel0PfYEslXFGJ8puc6twze0-NUNU8xHR9xh5q_CMxH4aqwSFlhKetc4a-WJjNIRnPDawQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa9e980fe.mp4?token=e1q4X1Nb7iPg_dbWXTPP0y3XW-5PLAh9icLMA3QstH3JtXK7vGaMOkeTGHwV4awZshrMA83HMutae-qOBLs2moJ-ojH5S8gHo6lZMg-fgZ5I-74r-PGuoyL2k6zjVNKoqEiabjITeoRNU3S2ksOEQ0NYNBYtpksoTnWJqnw-rlWlSwT3b75vBiJOb-2tw8usO2JbzvDJzE7GPDfOxEXFs-O5pTuaY7tK-i5v4hLIYR6EuVmqamgprb5dJlnx2Gfggzzphua1XSdj0FiUAel0PfYEslXFGJ8puc6twze0-NUNU8xHR9xh5q_CMxH4aqwSFlhKetc4a-WJjNIRnPDawQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترابزون‌اسپورقراره‌دستمزد ۱۷ میلیون یورویی به محمد صلاح توی این‌سن و سال بده. صلاح این سالها پیشنهادهای زیادی از سعودی داشت. الاتحاد تابستون ۲۰۲۳ بهش حقوق‌هفتگی عجیب و غریب ۲.۴۵ میلیون پوند پیشنهاد داده بود. سال‌گذشته هم یکی دو تا تیم عربستانی دیگه بهش مبالغ…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28308" target="_blank">📅 15:09 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
