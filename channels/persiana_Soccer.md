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
<img src="https://cdn4.telesco.pe/file/seWo4KNzTNqOLr2RlujRDogO1mhYdUARB6CO1L05YV-_8mUW25AL4HV-r3NIYCujKXJLMihCaSWzhFOT544PywaIffKK2yV_LeBazTX29bClhVFTD5nJPUDx-Ly3Ei_FNy8Y20r6hd0cNHlQBnK_lfJp5iN3Zk7zpoq-pVV555DlrARwVqZcQZOQYM5yW0ud86DDSlfzbLvKfV8L9oybQRQ-lvEE3IcMTS1UyCPsSsQPlGuM9BnRT-tRiVJiYOdRSjsZdJ9DIUm7CI-gJyIf37ZadT3vGVy8qNZfhKXL6rl9hC5JbmYDF57Yw10at5Usl590tAnJvCXk7TjlxTwIgA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 489K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 10:14:23</div>
<hr>

<div class="tg-post" id="msg-31074">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5V6VSFyNjiteZSQDDlD5ZUECJSmruL7H0tv289ESeAj5z5CFAXkTYegHPugZDus6WeiZn8kXzUBtkQ5nb7rn2jBpSw2hCiguioeGfkje8GqgiXGOxNYi33iyPrzffC-ul39hEnn0eX2iD5YyKbTtVfepa7jh4EZbr5Lrjg6Xo8cesU8E6xnvbAN-8DcwCkj3zleiPohzc_GG3FOHtOTd7AiLjNql_xTZcPWA4F1yT39DzIE-t8agKefKOyhoF9WWAomRlT6TDJA50NUCA94hW9jzL02WX3Lkll-Va7rpzbLbjks7xhAh1H6VJa-Vu84G0DGWYUy7gHUBk5leuoM8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسامی داوران هفته هشتم لیگ؛
وحید کاظمی داور مسابقه تراکتور
🆚
استقلال شد. احمد محمدی مسابقه پرسپولیس
🆚
صنعت نفت رو سوت میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/persiana_Soccer/31074" target="_blank">📅 10:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31072">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LfHQ0yW-pUS3SQgZMJVf0f6M92QWZV_fHbTdVdXUYM2Q-yJeKgFOrp7fcPUZvQFyUzwGXboOI5gkSLyB_vLPNj19GmEuEylS9HcPmcol0HcIu3K2FCPMrRAJiAgmqgzx7WSESQPy3CCrKDpo0mJZq-RjQ0ExCMAtvVvMQWB1O-Yt8NDkZCWXh2tPL6QcIFMu4p75aZbztMsyBrWL7Hmsiur4es9ii6oTZK5TRgyhbPm_D1EzRBLA1XuWjCmBvGdmynRa5dk7pmzFav41KUL26MV-iX8uN-rT_pyvv1psq_PiOuxxTCBdYnXrjzv7gy2YRNEFBmzT6OPaDC5hItPERA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QNaLL8Md36YLVuF9_dKKK9iO7Me9NblORoeEbHQaZZtwubx0Z7nI4y-a5Yk_4XMMNZYEloLWuW_rYrEdK6Oo_lU5rhgnwxpnUI-I569K9bldhbq1wl0WCP7AuDssdCFanjgld2nqbU5ub8QPCRiK3jc1PIVCHYGp0q3dUV_q3jd7GqhU_kAuermIEEy6DO90zeCpjgIByT7qKcRnVcnakrBxzio16xLKx3S7wQYPWax_M_fbqpWmQ9kWIpo8aftYs47_cHn0jZ8PLFJDXG8tcyIujwwbhvXbuA9ecEfqEj6X6ZKmy9bh2STR0kUpnLLwUEwRfyTfkNfxi8zrggGgdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
👤
سنگ تموم پپ گواردیولا برای لیونل مسی: تنهاجایی که ۶ اکتبرخواهم‌بود آرژانتینه تا در مراسم خداحافظی مسی شرکت کنم. من به مسی مدیونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/persiana_Soccer/31072" target="_blank">📅 10:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31071">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ac8f2e13.mp4?token=T2-T64RHeYm3OBKMAAliZJJZ_RyRF2sSsPk2gJrQ_sOXX_4kzH3ZIyg2sTASuwNA2858c1h7oBLAICBCKQ70c0-v_8ch_iRLUcvfupC2s8n82F-KXvl_GTKVnuId8L8zNMpPhQMEpad0YToDXKhipYsGJ8kUee-3IkA0EbnSmF2vqHq72Z9E8lIvweyL4RyIv2hBJP1mmCOpksN73DrPavqj9dURd7LuqCw-a9174uXeezPd9i8zdtH6WMw-JyAo9MctudXQx__424l52SrD7iyYJLID9pLGWX1SBfZ0LZRco4ZosNXOKwYVoUSeNwbPD4q3rf17-OMzttqHvxKQug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ac8f2e13.mp4?token=T2-T64RHeYm3OBKMAAliZJJZ_RyRF2sSsPk2gJrQ_sOXX_4kzH3ZIyg2sTASuwNA2858c1h7oBLAICBCKQ70c0-v_8ch_iRLUcvfupC2s8n82F-KXvl_GTKVnuId8L8zNMpPhQMEpad0YToDXKhipYsGJ8kUee-3IkA0EbnSmF2vqHq72Z9E8lIvweyL4RyIv2hBJP1mmCOpksN73DrPavqj9dURd7LuqCw-a9174uXeezPd9i8zdtH6WMw-JyAo9MctudXQx__424l52SrD7iyYJLID9pLGWX1SBfZ0LZRco4ZosNXOKwYVoUSeNwbPD4q3rf17-OMzttqHvxKQug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌ های‌ سنگین‌ و جنجالی ابوطالب‌ حسینی‌ به هادی چوپان
؛ هانی رامبد دیگه‌بهت برنامه تمرین نمیده؟ ایرادی نداره بیا خودم بهت برنامه بدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/persiana_Soccer/31071" target="_blank">📅 09:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31069">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmRAPtS8F8u3YwECevmhtxF6GLNEB0sNmfcKaXHG55WQ2Or6kyivkHdzqnAj-3l_FJNmmLMDJxvo1fHYPAIinlEENwU1zrmJ095trn-abeBQ2neqLIFKNOfyTF_VTvR_3gXXeirLoUJHaIx_rxy_MON5mcVyYzbjzGygHMnksRF3gMDEiybGyEfg2RLZYtLFqUdeEe7DTkycXs-aFLRC_i3Y-MLx_OKw5NHLnVSk9tgGfj4vXhKOk7tKNQiF1J81OeuwUM-y3Bg-zFHXV-8N8aW2cBAJ7LsiTH9PybY35z9VtTeU7hXlaj8dBGKJwyr_b8ayRSQR3bjCwDthpwbn-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
جالبه‌بدونیدکه؛ سال 2013 تیم رئال مادرید میخواست تونی کروس رو از بایرن مونیخ بگیره که مخالفت شد اما سال بعدش این انتقال انجام شد.
‼️
سال 2020 کهکشانی‌ ها باز هم خواستن داوید آلابا رو از باواریایی‌هابگیرند که‌مخالفت شد اما سال بعدش قطعی شد. سال2026سران…</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/persiana_Soccer/31069" target="_blank">📅 09:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31068">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rd4akD-u4047_r1GkfJKm90TPypFQW1sKamTeeXKkBZ-NErtyxOZZ5mla-9oYf2D9Zw-7rdflNY7UMSMOLvAsyAJUdmZ578tMoJw3sgwUvZbRxCNW2084ULS9bK17XqIHBCUOhfDQJc_irIrmPSzcfs204Vk6koPDgr69izKZ9jh1wJR4Xh9o7hcoNmI94ZJb_Q-aRe84deYCUC0as4eL_wSX03H1tfRSHsBXlDqIKnmsxZ76mox0pe3Hi80t8CRtn9tX_EZME5fpSDsW9qgCvnbrXv097qMy2PFnUbVEIAcKXIzS2CxVqPfBuDVnn6prtTeH0mkYeGcjjxVW2QzEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛نشریه‌بیلد: باشگاه بایرن مونیخ امادگی خود را برای‌ تمدیدقرارداد مایکل اولیسه همراه با بند فسخ200میلیون‌یورویی‌اعلام کرده. سران باواریایی‌ ها حاضر نیستند با رقم زیر 200 میلیون یورو فوق ستاره فرانسوی خود را بفروشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/31068" target="_blank">📅 09:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31066">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTYsxKJfBQolMiXH63X804GFoi2W4zcBze_tsaQmdCoBGWTX9tc33_gy_bdP-wKBYd9Dl4HJ0O3Bbl72JfFO9fTx5Bgh9fzddLQ400aazkKGqjZlE6uWSsxZ-NoTe5uPORKFAkT_kSWacD2af6VMunP8glh6dliaADHLYkwyYowmKRC_905jdDNd8dNIhnMDSbq2dKxo5ifXehKttFXIsOwu7dY4e4vMDLTFKWT36ji04OU5yoZZvkhrddA29Hta7SNl4MqxbiWYtjRApyiuLqB4kBcpi0t9kk-5DOm_TOox4kXhXMJpIhcj-SBK4LEFwG24qRgCL4gT_Ug4ewdEIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84daabae54.mp4?token=AeDeIsNnHcyfG_9RPhWUvOPXWGQ2C242-tjxEkPRYlEL74czysQkOJtp683Fv7ibyr58CPRfWih2XWISShyBop4OvWpM9cNPBJK2IqbY3efhPWYDHj1Kc5jdFDLTDaElS0v25ZhM_XHwUVirKC5EO_OTOTBloWfznPLuJvcrTRoCzeDHcZ4KLqtHD_zotPdE4cXPzQ6kx8TmdCn8wGE8YshxLPn3mtlaIU7xQzze_PkE5NSBEJtUY5EJ6MBYPhHz-A5NxZM914yCHxXaVyXYtb-EtY9CKLWzt2GE9UtYU6ajRe4sm87y7M-cHF4LY3eaBAkQxNVV1qyG_-6eW52PlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84daabae54.mp4?token=AeDeIsNnHcyfG_9RPhWUvOPXWGQ2C242-tjxEkPRYlEL74czysQkOJtp683Fv7ibyr58CPRfWih2XWISShyBop4OvWpM9cNPBJK2IqbY3efhPWYDHj1Kc5jdFDLTDaElS0v25ZhM_XHwUVirKC5EO_OTOTBloWfznPLuJvcrTRoCzeDHcZ4KLqtHD_zotPdE4cXPzQ6kx8TmdCn8wGE8YshxLPn3mtlaIU7xQzze_PkE5NSBEJtUY5EJ6MBYPhHz-A5NxZM914yCHxXaVyXYtb-EtY9CKLWzt2GE9UtYU6ajRe4sm87y7M-cHF4LY3eaBAkQxNVV1qyG_-6eW52PlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
گل‌های دیدار امشب دوتیم فرانسه
🆚
بلژیک و دیدار ایتالیا
🆚
ترکیه در لیگ ملت‌های اروپا
👤
شروع‌فوق‌العاده زین الدین زیدان با فرانسه: چهار مسابقه، سه پیروزی، 1 مساوی، 0 باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/31066" target="_blank">📅 09:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31064">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5ztf_MJ9-hTkYgayIf_adJlUbiUIY_XoreTBHDihsYryQ9I96-eHiZ-ARwj-1aSj9q-lIajj7snW0leUxQEIwZvKE-1t2EJo1iqN_8Zxkf2epJUyBmB97k4PO5OQIRIqob30Mvd960v8K7TIxRRbxHg41c_Ypv15y6vQ5bow3hZ1Qlh-AtUmZufdahSMODUP88kzvzSseN2ZKJbZHEYeJe3BUQQ1ZN_Ukhvu_TbwLMreZ7opG2zYPrNXklnmkWOv36kEc7rqE0rh9Yn8KmLiGJUe3tYubB3dLZYkyOBYHytgEItUYv0OnrB8BQdIYJod4NaWtiZJm1RxfeFLLPqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
برد چهارگله خروس‌ها مقابل بلژیک و دومین برد ایتالیایی‌ها با مانچینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/31064" target="_blank">📅 08:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31063">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPYTloHwVc5m4J2kXQfg_6eGeTVURCVvW1v6CC9KIXrDtIAcFskHP5Jv0OyWIM9iA-zfyqYuo7uox05Te57mhIhFEHFVGj8QZCSr2a6B8SKC2m_r7gw2YjMsLKTmnTZHgFhP7cjPK78AsHyAUpTbVrV4YWoxhB1G0PN56A9IVtJMcFjrRlZKCQpD_H28WjtmwqpOP5TmDVtYNJhm3JqiPXcmbB0og1uYMLrHrDuIYu-JpnosSecNe0qjijpJLKoE5JDJi0bRIurnuvBO4Zh_UOFQOT8gyEpFDFPUvak57WMmWYGju8ASfrrUVyAf7GNZW2kSFw2Eg6DpFkdjNeaeZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ جدال خانگی کروات‌ها با اسپانیای دلافوئنته پس از تحقیر مقابل انگلیس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/persiana_Soccer/31063" target="_blank">📅 08:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31062">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e146e3bea.mp4?token=TQsJmZmtTrX3qogcjZL6VMgYYAiSwnIBqZDdGuEd4ANmZKTxB2D_46YPC6nmr2Rrh_3ni_DQGF91bQj8djuGj1wUJ70lvt2ISLoVGKHJZrwmiGsnVb1nJIPKtcrYdwCu0ZEGccuMu3kBzSskMmeHI2crtKmhg9FEiQ9OWLHt_tAV8G5gL2ce0nRWq14RONZ9JET6nmTggmO1TWKaF8cXif-aOahWyYMm7cdB5IihCGl5wGCw7MfzGS3cjeiajJh3AX_ds49gAPFoXDnSCNfBbh2cpsMigoGBJ30pqwVtfsX59sisXsR-L5z7DjZZq9uf4gVhrJEc0ou2OanM1q3I3rRmXwNQYJMWVM3RZVj1MCfywVhPZ-ZQXjUoQhO_PfmCQpMuJO-tNVRNNJbrppqn4TzyZkLi6dDL-HjxHm9xnuSFzQRVXpl6wiKySfF3RsrtgytwUWSfzZyR7GV38lqZ50kF1H88xCatGe5TeuENccqocJhR32AIy8Tza5Mj5RwVzc3Vo7TOhOOuthfGsMx0QS3ifO0U_w7bGpvEneKP7vvJ_oe1qPC4IyE3pVD2y5svt8VEBItIymHvDE1npkPM6hKV9sS7ND7hn0peU3xqc-Kkx7Vf4bpSdZp14Z08NGMb5e53fNSofBOFM5y1TB4YbVkKcccJHlS5o8774-TCiRI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e146e3bea.mp4?token=TQsJmZmtTrX3qogcjZL6VMgYYAiSwnIBqZDdGuEd4ANmZKTxB2D_46YPC6nmr2Rrh_3ni_DQGF91bQj8djuGj1wUJ70lvt2ISLoVGKHJZrwmiGsnVb1nJIPKtcrYdwCu0ZEGccuMu3kBzSskMmeHI2crtKmhg9FEiQ9OWLHt_tAV8G5gL2ce0nRWq14RONZ9JET6nmTggmO1TWKaF8cXif-aOahWyYMm7cdB5IihCGl5wGCw7MfzGS3cjeiajJh3AX_ds49gAPFoXDnSCNfBbh2cpsMigoGBJ30pqwVtfsX59sisXsR-L5z7DjZZq9uf4gVhrJEc0ou2OanM1q3I3rRmXwNQYJMWVM3RZVj1MCfywVhPZ-ZQXjUoQhO_PfmCQpMuJO-tNVRNNJbrppqn4TzyZkLi6dDL-HjxHm9xnuSFzQRVXpl6wiKySfF3RsrtgytwUWSfzZyR7GV38lqZ50kF1H88xCatGe5TeuENccqocJhR32AIy8Tza5Mj5RwVzc3Vo7TOhOOuthfGsMx0QS3ifO0U_w7bGpvEneKP7vvJ_oe1qPC4IyE3pVD2y5svt8VEBItIymHvDE1npkPM6hKV9sS7ND7hn0peU3xqc-Kkx7Vf4bpSdZp14Z08NGMb5e53fNSofBOFM5y1TB4YbVkKcccJHlS5o8774-TCiRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باشگاه‌استقلال‌خطاب‌به‌فدراسیون‌فوتبال: شما جام قهرمانی فصل‌گذشته لیگ‌برتر رو به ما بدهید ما خودمون نمادین اون روتقدیم شهدای میناب میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/31062" target="_blank">📅 02:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31061">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612b743bd9.mp4?token=r1LL5W_bJmbC0xt3AYtT5Zds2gxtafb5fnrGBwlWPLfkPZ7v8PSrtluri5Gh16ZEFMYsfuciuqNCgMi4LReXMZhfbriFaNQkHjTZ7j_Vzv8sLZewDDlQN7H276kTdgcf9j0A1Gre-MQGq4n79k7tXh0D0x38SQpWZV8Bh_LnU4GLpxigHpbhjE9tkEDg55qkefzJmik36K8AS7DVp9CbQdq1w6yVrGr8lANt99piaV7DpiPy1iJGeZ9Z1YH1uwZ8fSNOA2Bz018aN_qMuwNg8_Ixncc1gEuOAGCKvdJaSuzRaYeMC7PQ7jH5YaFIzV1yMuvwm4P6BceyUmcxUdEFYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612b743bd9.mp4?token=r1LL5W_bJmbC0xt3AYtT5Zds2gxtafb5fnrGBwlWPLfkPZ7v8PSrtluri5Gh16ZEFMYsfuciuqNCgMi4LReXMZhfbriFaNQkHjTZ7j_Vzv8sLZewDDlQN7H276kTdgcf9j0A1Gre-MQGq4n79k7tXh0D0x38SQpWZV8Bh_LnU4GLpxigHpbhjE9tkEDg55qkefzJmik36K8AS7DVp9CbQdq1w6yVrGr8lANt99piaV7DpiPy1iJGeZ9Z1YH1uwZ8fSNOA2Bz018aN_qMuwNg8_Ixncc1gEuOAGCKvdJaSuzRaYeMC7PQ7jH5YaFIzV1yMuvwm4P6BceyUmcxUdEFYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل برنامه امشب عادل فردوسی پور با برسی اتفاقات اخیر فوتبال ایران برای دوستانی که علاقمند هستند برنامه رو کامل تماشا کنند.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/31061" target="_blank">📅 02:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31060">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906c18ef7c.mp4?token=gz59V8NyH_5Sy9IFWa8JOF47hXdlvx_kjsIpfdE_ca8wJPjUmrLPvCTKwVHf_cJwAXOlDED59O5ku48XOR_v2ECPySiB_Smim5XIA-gLqbXi0yuwPC1ZIDu7gV6EqfJF_wLYzl0-evYuGhvxKIaQ5R4-E1-bfbyYVw9T29DOpoSmdwIj6g1gy4lg5gT4jd_oXykA2bTxPoI7Vxb3He-vyw1lvxpYFXcuVurrVJoNzVuEnLhvYDKlooiUMOZ461Tb2yzxbnEOo_KiwziIAXmSipT71X8LGC5hzIeIVI2VlnRhtQHG-2rynEGYONbSsvhWtDiCMMBCTyrE4JqEJeVqYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906c18ef7c.mp4?token=gz59V8NyH_5Sy9IFWa8JOF47hXdlvx_kjsIpfdE_ca8wJPjUmrLPvCTKwVHf_cJwAXOlDED59O5ku48XOR_v2ECPySiB_Smim5XIA-gLqbXi0yuwPC1ZIDu7gV6EqfJF_wLYzl0-evYuGhvxKIaQ5R4-E1-bfbyYVw9T29DOpoSmdwIj6g1gy4lg5gT4jd_oXykA2bTxPoI7Vxb3He-vyw1lvxpYFXcuVurrVJoNzVuEnLhvYDKlooiUMOZ461Tb2yzxbnEOo_KiwziIAXmSipT71X8LGC5hzIeIVI2VlnRhtQHG-2rynEGYONbSsvhWtDiCMMBCTyrE4JqEJeVqYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیا از باخت‌های پی‌درپی و پیش‌بینی‌های شانسی خسته شدید؟
درکانال ما خبری از حدس و گمان نیست. ما اینجا با آنالیز دقیق‌آماری،شرایط تیم‌ها، مصدومیت‌ها و فرم اخیر بازیکنان، بهترین گزینه‌ها رابرای.شما استخراج می‌کنیم.
✅
آنچه در کانال ما دریافت می‌کنید:
🔹
پیش‌بینی‌های رایگان روزانه با ضریب بالا
🔹
فرم‌های پیشنهادی (BTTS، Over/Under، نتیجه دقیق)
🔹
پوشش کامل بازی‌های ملی، باشگاهی و تورنمنت‌های حساس
دیگر وقت آن است که هوشمندانه بازی کنید. همین حالا وارد کانال ما شوید و استراتژی برنده را یاد بگیرید.p13
🔗
[لینک کانال
https://t.me/+-M99R2qSbdVhOGI0
]
🔗
[لینک گروه گفتگو و تبادل نظر]
https://t.me/+M_YAiGu22l05YzM0</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/31060" target="_blank">📅 02:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31059">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoqOcvr364I3NzE4EPJemfmHZ-LYDkmaY5IVWO_0DHzwMrPB17qLcSOZPiXQyNvArxVfjYmz-mL3vyC6iCdyvbyAe4kW6OECEVPSpq2L_AKcyGXI1LH_K3tPF9JpfFeKNo2V1SJSwVP9CcIPKZk0tnsx58914DRml-mCPc0KqbrPZSvDSNBSsAvciFH7VwmX0kRTIzH9WHRlMNvsYt_P5IdNtN6XpyrWAwIG2-_i9oRRzD1L8WrHuoD7uYa7TUobbBNHiWRa0MX-ALdCsNcC-yLFohywiDLlmdr9Xx07Va_gYrUWrbz3DDntSuZG_Bfg6vatu--T2ak9QGoVYEBrMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روماریو:
امروزه مد شده به فوتبالیست‌ها میگن بهتره شبِ قبل بازی رابطه جنسی نداشته باشید ولی من باهاش‌موافق‌نیستم. من‌شب قبل بازی با همسرم میخوابیدم، صبح هم که بیدار میشدم دوباره باهاش میخوابیدم، آدم باید تو زمین احساس سبکی کنه. به بازیکنان توصیه میکنم این حرکت رو بزنند معجزهه میکنه. دو راند نیم ساعته قبل هر بازی توصیه منه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/31059" target="_blank">📅 01:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31058">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1edc763594.mp4?token=BRVR1wKUVuc8j7inOLIAvnd-bdcq3tCo4_1aWGG0QysTnITpEJ9L0J3YaBjdfQiPOBcgAPKjwclMTALj1yCHfA64r5NTQGaDeweo2bUv9JwgzX83belxaclGd67n_ekFPa1sxth7roTe1rZx-VbBZF-90XoFOYbGL_l5ySuUtm0ztjPbU0IsLvnBn6U9iw4lyvR7W3-ruP11XV6W8-J3QhC4J66_AzwiBa2R62IGT-SE4UtzFGE3AYq18TB49E1OG_mYXBNDY3b-wpRYZr7Yg66C6vGthiO6lymU7D2pbv21TAUO6uGCVgIQAkRGfFyFXmoAVK5drTQq9i0FYOhiZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1edc763594.mp4?token=BRVR1wKUVuc8j7inOLIAvnd-bdcq3tCo4_1aWGG0QysTnITpEJ9L0J3YaBjdfQiPOBcgAPKjwclMTALj1yCHfA64r5NTQGaDeweo2bUv9JwgzX83belxaclGd67n_ekFPa1sxth7roTe1rZx-VbBZF-90XoFOYbGL_l5ySuUtm0ztjPbU0IsLvnBn6U9iw4lyvR7W3-ruP11XV6W8-J3QhC4J66_AzwiBa2R62IGT-SE4UtzFGE3AYq18TB49E1OG_mYXBNDY3b-wpRYZr7Yg66C6vGthiO6lymU7D2pbv21TAUO6uGCVgIQAkRGfFyFXmoAVK5drTQq9i0FYOhiZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ تیکه های سنگین عادل فردوسی پور به مجریان صداوسیما: توکه‌حامی قلعه نویی بودی. رنگ عوض نکن. حق انتقاد ازش رو نداری دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/31058" target="_blank">📅 00:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31056">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇪🇺
درهفته‌چهارم لیگ ملت‌های اروپا؛ شاگردان زین الدین زیدان باطعم‌کامبک‌مقابل‌بلژیک آتش بازی به پا کردند. ایتالیا هم بادرخشش کالافیوری ترکیه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/31056" target="_blank">📅 00:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31055">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA9TlgUUBSNUi0C8SEH0HLZbteOx9PpI8LGC7hjzADCRlSfKj6vBkoJ6QJ4cs6SmnghzuqJqtQ1Y17553-O80M_gWvv_q6I4sEB8clp_giPS-WMgjIIHzzIVs7sU4BbekKWXTKHySGk4_brpLADC8XCr5aJ257m4LWoteIsoC-zUFczNG5NeqQzcDnTQwK0fHLvF8wdulL3aiK7fs_2tcnC6N_wowth7E3Z87LfsDlMbi3RcFqS2T5RFJlo-_UHfV2iLC67uqJz5bmClT1nHX29_4stCgqUhBwc1TZSdI4WDhfUyTRQxBfzq2ci9ozNBu6JDNvF78o1pjSUct-AmsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز؛ مصاف خانگی شاگردان زیدان بابلژیکی‌ها و نبرد آتزوری برابر سرخ‌های ترکیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/31055" target="_blank">📅 00:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31054">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmuLSahyxpuNNYIylvvxGAssX2TvTtuAIkltRcCqReIBsgk_2PfIXzThK2SPI3wC3B2adchqSaz4CTMYDhsAWPzi2h9Ot3VKcNx8C_c5M_u27DIZ-ClKqKM5q5qsloXz_XD6nUUCYHbAd_aFMQbpZxSZqO5UF0D_6D27gJW8B7Xl8sjSl44Y5GMOZb8xKZsQk43HpKQOkqY9CN8JGtPZrsh8SW-dWRCUgGDhpZE5w9UUNohJzlX8RYbeMawK1p9qVTBGkhKRE7LQsDFBtuNeXGTgfS6VAU6Vf_drq5zbvCjzaIGAMjGrofGASkLBdB4ZtvTMkWNW5YXfFfrkQKx8Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
از کیت عظیم و ۳۰ متری آرژانتین با عبارت «متشکرم ۱۰» در پشت آن به افتخار مسی در میدان شهرزادگاه لئو یعنی‌روساریو قبل‌از آخرین بازی ملی وی رونمایی شد. امشب مسی خدافظی میکنه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/31054" target="_blank">📅 00:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31053">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9410553bb0.mp4?token=IVNy4VOJ04nvBNOj9F234F0GB7P8Vyw-GH8-CgUK2TCI616LxVY1NC4wkGfE9TYc7wGa25X-7Ftw_cP_zulUJigDjAn8tfMlHdzfypfChiKZyzX4v90mS7omOwdhIQ_bMf4ld64zLr9SXfD3ZNgF5MWKnstG4Kw6IJ4gYEW6pImTepdHr8F5U5ndf8i_xtWacluq7KIFSvSLHo0ISctnlPS53-9WkjiCpb7Vx3O99voaXO1g86JnfRuSspHSo_QHCWeOWgUP933ASMZp8hYKj0TyGCE67qqQPa6ZNU1BzHyP3Bu-kfK8CjuuNVvIIBQcktOJuIO5JRfF9cK53IwY2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9410553bb0.mp4?token=IVNy4VOJ04nvBNOj9F234F0GB7P8Vyw-GH8-CgUK2TCI616LxVY1NC4wkGfE9TYc7wGa25X-7Ftw_cP_zulUJigDjAn8tfMlHdzfypfChiKZyzX4v90mS7omOwdhIQ_bMf4ld64zLr9SXfD3ZNgF5MWKnstG4Kw6IJ4gYEW6pImTepdHr8F5U5ndf8i_xtWacluq7KIFSvSLHo0ISctnlPS53-9WkjiCpb7Vx3O99voaXO1g86JnfRuSspHSo_QHCWeOWgUP933ASMZp8hYKj0TyGCE67qqQPa6ZNU1BzHyP3Bu-kfK8CjuuNVvIIBQcktOJuIO5JRfF9cK53IwY2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ ادامه تیکه‌های سنگین امیر مهدی ژوله به فدراسیون‌فوتبال و کادرفنی تیم‌ملی درباره حاضر نشدن گینه بیسائو برای دیدار دوستانه با تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/31053" target="_blank">📅 00:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31052">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSb39FRvedwZvyFzamjhkd6lYvOHdbMpBKe_qCkruAMQHAqouEh4G1RT4zj2L_gENRBFIzOv_60rsIJnqo9zD4JgI3kr5TooAeP1EYx7RFN2CNI6fxxHSZk0CCze93ly9wKf1CNStRtzZtWTeJCYtR2X4RCqNDap62fGxjRZO79ri7OOl8mzzhJSu_BoWb4SMojnWwhtggK-ndoaZbY-RXAtNmNLkwaEWwISdVkUS2pSZQivYm-vkaBSIfdguIP_1jjmv9MprEPvI1V2RD8x7TEbytIH35V5-4yVgpXPfluAf9Nr6rJggAkH9AwO6sqA8CN4oHI_hp1aDTe86N9DVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه ژسوس سرمربی‌تیم‌ملی‌پرتغال گفته چرا باید از کریس رونالدو عذر خواهی کنم؟ نه نیازی به عذر خواهی از او نیست!!! پس بشین تا برگرده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/31052" target="_blank">📅 23:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31051">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQNbfbUVB_eWf2SCV5pSmD-aHeNtBLQeuvhAQ7Y2nHFN3XJw6jsF_JmAZUvSa6XMISDvyW0-BgQntVRSZsI2Fe3xF9zKYXeAAjLq2NPt0ft454N2RiBbBGafSzZnnakb3H5i8xpBh8gCbtPhBT1VNPE7hARxo0wFCKeZGOaY0Ir6sJljlrIxYOzz2A-CQSVrtdJ75QYnXvnb3y_KB-uJuxuYshpT00wvt79dBAtPI9aPXLAgHe5Hd3RqpsBIZ8d7vip3qxNWnLZQwRHKyweaF7ioKzB1xK298PBRf5IZF0veM1sv_1GyojtsQ1nE2VLKltIIM05fQjl6neRbzIoqfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/31051" target="_blank">📅 23:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31050">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbe125227.mp4?token=HrzfwQ3Bjb5uGrDA9upCl2WM5uUtH1MHN9EnJ9JQvjMCIpfog8K4Tdh4cRVAfQygZR2hvWtKhdFLoM0Sp3I92Q38KXwD3GQRsohGHlNVhSLbAuJU88t3Nil5j86n8oWHcuIydT49zn-5BtA5bZaLpPFfscYlkWgzYyNf-7KiMlKRFLdmB0TH8uuuvNxEhPC6BVCXAQgfd5OxI1O1zxl_qizXFD30DQOWTO7KYxibrE8M9AltuSA3gmNx6v6xa9R8YUCMJGQtjnxqo4MqpJY3pKHGM8pTqsblkMmJicTc8enK4_0hQkmgJ4eRkMr65PXcxmTUARkUaFqVoei4k_jGsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbe125227.mp4?token=HrzfwQ3Bjb5uGrDA9upCl2WM5uUtH1MHN9EnJ9JQvjMCIpfog8K4Tdh4cRVAfQygZR2hvWtKhdFLoM0Sp3I92Q38KXwD3GQRsohGHlNVhSLbAuJU88t3Nil5j86n8oWHcuIydT49zn-5BtA5bZaLpPFfscYlkWgzYyNf-7KiMlKRFLdmB0TH8uuuvNxEhPC6BVCXAQgfd5OxI1O1zxl_qizXFD30DQOWTO7KYxibrE8M9AltuSA3gmNx6v6xa9R8YUCMJGQtjnxqo4MqpJY3pKHGM8pTqsblkMmJicTc8enK4_0hQkmgJ4eRkMr65PXcxmTUARkUaFqVoei4k_jGsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری جالب عادل فردوسی از تعویض عحیب تیم ملی در بازی دوستانه مقابل تیم ملی روسیه: قلعه نویی تو بازی با روسیه از عملکرد محبی راضی نبوده گفته خودت رو بزن به مصدومیت تا تعویضت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/31050" target="_blank">📅 23:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31049">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7niBtYNVZK1igA3Z5N5WgoF_AVz_dRsHaYXjNrmXddwnYaPxcv2lrWyKqiPqRaMInFopZSEk3e7x43btXOeKi48lO6aq5wH_z0AMF0VssHxT9Bc0pvyphFuuHWilFTtGvvlrShauCMTVTVIiVjqj-zfCpe8ocWiwUJoe0x7gv1QJyxzSZnJA3WC4UrUErFeCeH-tW-iKbTdEYzH5MSPmAj7wnw40YX7SSI4yQQ7NGeInZ5l1gpdwBbxFz_E-dcECwqyFRjw0LqnbbGU59HKZ4GEGkc9Nek1StSiw_Gz-Eut6E8EG1GAtpYKwBv7C_tnp9XO1w7hXSszgSZjGMgz7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سکانسی جنجالی و جنسی از فیلم جدید دوس دختر کیلیان امباپه که سروصدای زیادی به پا کرده. کانال دومم داشته باشید کاملش رو اونجا میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/31049" target="_blank">📅 23:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31048">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39c5af2a82.mp4?token=NJnwpBDd8ARi4DYx5DB9HzdqSdltE73nJ0h1T3tdjiHBF4MhJlJ0V_NJA5GC-J33NwW6cPHql_Q9aykLMEy2aXvXzmz5SNHYLxy2iMXW-2z563bul7a9cQ06bsjIglMK4SE_XXNz_DtKCpWioKHF8WoaHt8xI_1YV6KI16Ji_g-lWIAONFCkaNAeocuPgFhaCClZNXQafqxZqD-xTMoj0N1F7vY6a8WhBHej76wLudh6tC8rE_UKldDYVYfxbaMKDUlGNDYU2-ZGzq6FO3-DzoaaHt_D00ZCdbMZyRYWgtgpXsfXDcPD9Gi1ViVs1rhlAyTVpaX_1YeK0ZixoOJt5FTItb2HKMoQcnhA4usi7Hxy6wvM3-cXWhtssVozt_Px_1mNRxAgQVh3Zz_HNl_alUPQ8uhV8GKnMaeEVCPzf3e_1o1zt7JnM_1wsruqIEUSDATvqZz3hbK19BND0XB5326wDp2Fm4Aqjdsik5dF1PQaoFFqWD-TzCQqXOwWW3PdccqzlYbt1zXyixhcerMGCfyzrUlwDLYZ73F1bK1-tr6xmjnpSQP5pj92f7lc9X-r5eORIyBgIBQhAk5evVII1W9vaLIyRlE0rSvwcGYuj0E3q8X_neN7EoDptMFumi_a1s6kr_7EBx7cdF37KtE8WKqYU2U-iPHZTdKQUYblsUo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39c5af2a82.mp4?token=NJnwpBDd8ARi4DYx5DB9HzdqSdltE73nJ0h1T3tdjiHBF4MhJlJ0V_NJA5GC-J33NwW6cPHql_Q9aykLMEy2aXvXzmz5SNHYLxy2iMXW-2z563bul7a9cQ06bsjIglMK4SE_XXNz_DtKCpWioKHF8WoaHt8xI_1YV6KI16Ji_g-lWIAONFCkaNAeocuPgFhaCClZNXQafqxZqD-xTMoj0N1F7vY6a8WhBHej76wLudh6tC8rE_UKldDYVYfxbaMKDUlGNDYU2-ZGzq6FO3-DzoaaHt_D00ZCdbMZyRYWgtgpXsfXDcPD9Gi1ViVs1rhlAyTVpaX_1YeK0ZixoOJt5FTItb2HKMoQcnhA4usi7Hxy6wvM3-cXWhtssVozt_Px_1mNRxAgQVh3Zz_HNl_alUPQ8uhV8GKnMaeEVCPzf3e_1o1zt7JnM_1wsruqIEUSDATvqZz3hbK19BND0XB5326wDp2Fm4Aqjdsik5dF1PQaoFFqWD-TzCQqXOwWW3PdccqzlYbt1zXyixhcerMGCfyzrUlwDLYZ73F1bK1-tr6xmjnpSQP5pj92f7lc9X-r5eORIyBgIBQhAk5evVII1W9vaLIyRlE0rSvwcGYuj0E3q8X_neN7EoDptMFumi_a1s6kr_7EBx7cdF37KtE8WKqYU2U-iPHZTdKQUYblsUo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های عادل در مورد بالا رفتن سرسام آور و تلخ قیمت دلار از آغاز هفته اول لیگ برتر تا به امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/31048" target="_blank">📅 22:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31047">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f9838cf82.mp4?token=MbBUbgMFXkKsshPgBkwMNwrNQjrrvIgSYJealMLUTHk6FBGzyiQP_MtOctFsZLYx5-3py-FAcJyOicL_1wsmi-g3b1D-6nOdE6eGeaAux1pcJ656qXFwJ6GsJeQsCSJ3xl8mJ0QLIg2jm-xZ3C03GU-PxNfmCbWRv12WvJI2IeWBj9mhL5ZNDeLIgX6P8oL2mUDzgsiZVJU9k5jshj_la8uCJXiDcwsyFvyR6HTSSKqX8ikLi8z1i2AwYuJN06sixR9luk2RC_EdsagDpYNbTWW0jpH-Nb5Rqq6ICvvH03sPc6EWRoHLXn-ZLX018t2vO5dyUeoH8kipc2GTRSNnvDUKz8f-fTKP41XzuEz9FIikMUE4cBlWS1duEYWe5lGKvh7IYuZbYg1Tm1NL9dYIe0UXW5j_I5qlazxiV9owp9qnH3dxz0MFcFZvRpKjphcvrY552srtVKqkO4llAnUkmJnofOEi9Jt0utoI9AeB6x3a9ygeDGbveaorly1J8eXBnCYUSG25eVh037SHDxW1mDWZkEgJ79u0VlYvs33TxNVqDx0gWwHv_-HE0eYE8E71L5TfuCNAPRN4R1HBRWT1XSN9QTx9duPHao23aBQzzBrSb9jFscTXBwiYPJJxVP7bWugZuMUhX9LUrF9QZy972ijxaa8v5ZtBC12tirX043s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f9838cf82.mp4?token=MbBUbgMFXkKsshPgBkwMNwrNQjrrvIgSYJealMLUTHk6FBGzyiQP_MtOctFsZLYx5-3py-FAcJyOicL_1wsmi-g3b1D-6nOdE6eGeaAux1pcJ656qXFwJ6GsJeQsCSJ3xl8mJ0QLIg2jm-xZ3C03GU-PxNfmCbWRv12WvJI2IeWBj9mhL5ZNDeLIgX6P8oL2mUDzgsiZVJU9k5jshj_la8uCJXiDcwsyFvyR6HTSSKqX8ikLi8z1i2AwYuJN06sixR9luk2RC_EdsagDpYNbTWW0jpH-Nb5Rqq6ICvvH03sPc6EWRoHLXn-ZLX018t2vO5dyUeoH8kipc2GTRSNnvDUKz8f-fTKP41XzuEz9FIikMUE4cBlWS1duEYWe5lGKvh7IYuZbYg1Tm1NL9dYIe0UXW5j_I5qlazxiV9owp9qnH3dxz0MFcFZvRpKjphcvrY552srtVKqkO4llAnUkmJnofOEi9Jt0utoI9AeB6x3a9ygeDGbveaorly1J8eXBnCYUSG25eVh037SHDxW1mDWZkEgJ79u0VlYvs33TxNVqDx0gWwHv_-HE0eYE8E71L5TfuCNAPRN4R1HBRWT1XSN9QTx9duPHao23aBQzzBrSb9jFscTXBwiYPJJxVP7bWugZuMUhX9LUrF9QZy972ijxaa8v5ZtBC12tirX043s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فلش بک بزنیم؛
به وقتی دوست‌دخترِ کالافیوری اونو درحال‌مصاحبه با یه زن دید احساس خطر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/31047" target="_blank">📅 22:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31046">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GC7Ykaul3nWdOBSIKNOH9Ava0GLsKDeF8SSlkgEZ0djOu4_3JqtlagUbpFZeJsEBYG7Ed0kpM18gmr4TYzrGjJwxOpwwwvSajKV-ilHTEhTqoWvJYdWH_jVsU3V3W2Dcn-wyl11XvqGtSmN_V6i0TrF_EB02Okadehr7rPme74SMvS6YYtdGIXakJB7ooZDQpkZaNhZiSbBHAECFVeFrfsVJvy0wSQX9M7RRyxLFZKHZ2LfOcHXoa77hlmWeb1yGh6MqTRYWoLwgw-lwISGTH66my8bUt-wADkK_xySIGYhUbVbJMUoI4E7Rfjo-VOcfrq5wFI7Kf5mwObUlf0HZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالیکه هفته‌اخیر سارقان تو اتوبان همت تهران تلفن همراه‌آیفون17پرومکس پیمان حدادی مدیرعامل پرسپولیس رو زده بودند. امروز همین اتفاق تو اتوبان تهران - کرج برای مهدی تارتار سرمربی سرخ‌ها اتفاق افتاد و گوشی جدید آیفون 18 پرومکس او مورد سرقت قرار گرفت. خداروشکر امنیت داریم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/31046" target="_blank">📅 21:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31045">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe541534a.mp4?token=SFeDzZQ0Dl89I8R0LNOm-9S-KySIb97QJyAbVxKv7jy4g0g679ARJqiTjKf00-GPCbzjdkT1OdJrlXrMtCIiUetQe6-G1K4UDHfttlhSPPuJ28bbYNKwrW3aIOgWqAe0HyzFL0UYT272gOLuAR6ICOavsq0pGq1_7UtWdWXmjK_Te4FFCqMWyM4BVec4NCn1Gc4YM7-w4yjaQueB3fPw9QC1EZRpPzfBN6YXIiFqtA_0qURqyuueH3lKpNSJzm1ILKr4Ip9ru9Komc1fHY3ngywLDSjlfz4LihG69Jc97gZcJsgRAGePeMSYVdioa9NFfqUI_tC8emB9kAHUCjOcJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe541534a.mp4?token=SFeDzZQ0Dl89I8R0LNOm-9S-KySIb97QJyAbVxKv7jy4g0g679ARJqiTjKf00-GPCbzjdkT1OdJrlXrMtCIiUetQe6-G1K4UDHfttlhSPPuJ28bbYNKwrW3aIOgWqAe0HyzFL0UYT272gOLuAR6ICOavsq0pGq1_7UtWdWXmjK_Te4FFCqMWyM4BVec4NCn1Gc4YM7-w4yjaQueB3fPw9QC1EZRpPzfBN6YXIiFqtA_0qURqyuueH3lKpNSJzm1ILKr4Ip9ru9Komc1fHY3ngywLDSjlfz4LihG69Jc97gZcJsgRAGePeMSYVdioa9NFfqUI_tC8emB9kAHUCjOcJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین ژوله به امیر قلعه‌نویی: من یکی دیگه فرصتی به تو نمیدم. در طول این چند سالی که سرمربی بودی میدونی چقدر خون‌ها ریخته شد؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/31045" target="_blank">📅 21:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31044">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RX-HSAy8DACTE-tXoitNwuPbdDFzIvcsPK2mkhMNsd13ppW83mklRAb2ue_8HduIEYrd5rM2H_3gQ4gh78s66SAr40CFhQnSiN2am9WaM38PwKg70lyxEPdgCiuZgPBJKThnf3arNkqM7KST82wuLvvoxe_mOB8VH_oRJaCMS1aO5on1y_Uz2ygZ_OidSsh-Uc2mqxAmNjc1apdSDvEjPiC3YuHY0ujoqoBJPWsFrmn-C7mbQkssOdgDWp3xqUPcjOcA1FGON3RxgNrIAIu_uySBoJJg7mCytqhnWwixPe2ltn9-Lct6EkFS7UWKXTdmRnOSNVLSpVviDuS4UBmSuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
مدیر ورزشی النصر عربستان: با کریستیانو رونالدو برای‌قطع‌همکاری‌به‌توافق رسیده‌ایم و ایشون درپنجره نیم فصل از تیم ما جدا خواهد شد. مقصد بعدی فوق ستاره پرتغال فوتبال اروپا خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31044" target="_blank">📅 21:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31043">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📹
ویدیو کامل قسمت دوم فان فصل جدید با امیر مهدی ژوله؛ عالی بود. از دست ندید و حتما ببینید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31043" target="_blank">📅 20:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31042">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJSr4UaCqDlAwg77ETAGWXZ8pvwEMuyHvkzUZPmPcGtD1LvQMlakIm60cAppJOsp6bmN484FyAsbUV0Rpqtdcz-1O5EhA_HtLs1dZwmkRoRPuVdTUUHqLAuOW9Cky2tmhJtSmMMqYhAzOkifSJ5g1Hi2F6turD3xkYTRpAZLSRhMtcFeJK6fhC7VlrrpvYeKM4xQoyZ8rprHk0u_SFfX0FCCf_c2mo1DrxejkVIGgw_aKkRNe_DqDXaKjFYMEo_eK7v8NoONAN___SV-RBXLxlOghQ1ASBAGbENaQOH90UoZtBEpshROC6xF9LYqNkqnBf6K_buweQrPmtZisZD94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان پنج لیگ معتبر اروپایی تا این جای فصل؛ رافینیا دیاز فوق ستاره بارسا در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31042" target="_blank">📅 20:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31041">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJoOEhx2JqDllo_OTrcKcsC4oD3bOb59Sc923qgGIkdD25IhyF0pYrlphVW3cD3KSU6rizQZLZ-N2oU4-SyvumZ3IMdWyvWu4QCkwGn2HaTTv_mzavffreRGQjtuV4yjjYy9K4Y8C71d5MXykj_qscmmlEps3X_nh8RhR952-R5GbHPxa3z7cJ7cDzc8ZPDeLvcckHToDCjcAOCJgDO_NHi-DDjm1bgmqFmqyf8-KML6rnNeseEY9culN7OSJo3rx4BMkh5XT_XARVpiWTEgy8g2rD7s7IIZJ-8JgilPBEemKSEr2NGGS8jOw_ooWxUCBiULjTpfkM7lA1pAdbjzZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکردخیر‌ه‌کننده و درخشان جودبلینگهام ستاره 23 ساله انگلیس در سه بازی اخیرش برای این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/31041" target="_blank">📅 20:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31039">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7381a71b01.mp4?token=hM0LwubBZlHb_YanRUcm8sDPyfCKWCH7yB5Wx-2QDrGquumvGl4nts4aYc3-ep3eWxmIyEZt13pR5J4oHRBTmJnymg8ihk1h3W9s1sKtndGPvp6-yYt0NnuzPP-Rkv07x03Z2wdO6Ta0IV3fgNTDBLQ4vK3I925CtQNcdOUKizZqJeaBYnjIBf7kKhpJd_c3l0nwlfx46c-3aYgmMa-t6dQP-RRv-SIoCgzyosy0TqeaZTVinGcLUSQZodaLln5tAGOT2Nv6osRs_AzZu15nDnjoYT1_Ofe94TcKn76bFxXaVIc8bf6Cx-1ob9NbiQgtOgeFxK2HfHlC9uFQ8lGsDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7381a71b01.mp4?token=hM0LwubBZlHb_YanRUcm8sDPyfCKWCH7yB5Wx-2QDrGquumvGl4nts4aYc3-ep3eWxmIyEZt13pR5J4oHRBTmJnymg8ihk1h3W9s1sKtndGPvp6-yYt0NnuzPP-Rkv07x03Z2wdO6Ta0IV3fgNTDBLQ4vK3I925CtQNcdOUKizZqJeaBYnjIBf7kKhpJd_c3l0nwlfx46c-3aYgmMa-t6dQP-RRv-SIoCgzyosy0TqeaZTVinGcLUSQZodaLln5tAGOT2Nv6osRs_AzZu15nDnjoYT1_Ofe94TcKn76bFxXaVIc8bf6Cx-1ob9NbiQgtOgeFxK2HfHlC9uFQ8lGsDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل قسمت دوم فان فصل جدید با امیر مهدی ژوله؛ عالی بود. از دست ندید و حتما ببینید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/31039" target="_blank">📅 20:24 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31038">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPZyv-jiw3k9hyeyGdGPhfL7hy6pv0zFb5_QdqOEB5-98OT29MlMvKstwIG2_7A9Y65-t_rrRz4UJ2p0nG7Xsf5Nsha0mmpeLc1uFDhxVFkAl8WlYTVLn4tuz3ibbF3XJHCaZrzkMFMpxJFR87w-vgIhIW_sdr9N-px78RpLgBQb_6eRAnlSpEKg2zE2Vml1fnLuncIQ1E0I6j-Nm06Q2n1Ax2Ij2OpgXgPV4xQo9uKwK5TnXNhCDyX4yU7nVCav5h4aItr-v_zAWzYiMHTS_NcgqwsI0LJm9aSM7QkrTFlu5GHcUEv667znI6SMa4IjSl5xyRL8qsItVKJh6E-6nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
🇧🇷
#تکمیلی؛ با تاییدیه کادرپزشکی باشگاه بارسلونا؛ مصدومیت جزئی رافینیا دیاز برطرف شده و او مشکلی برای همراهی آبی اناری‌ها در بازی مقابل ختافه در هفته هشتم رقابتای لالیگا نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/31038" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31037">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXIm8oMzLofXt2rX48Rpszrn-ItdeRKjb6aVD0bNSC8lXX8vUwtUUUg81KJMdMlSuSI7lJSWN11MPUMM9SSI49-EfWJnNeWKI1HseQzbP3yhYg98QEVehXI-7UuiNsb6Bs2F-Xc49AGFhiac5ffa_MbjHmsjHuN8v1AEu1usLKjZgbPu2ygVwNz8LauV6ASm2g699G5klNwKGEMEVYPGDHSG89anlUGlhXkw-Z2EuYKdQwIfkxbQJrsNdW7xiZLXTeV36G9qkpH9SA9eP3c5xQw_G7defGzq_gTaDC3Vcua39aRdOflE1H-mz469Hy7R9k5lkyyvQlURGijmJEzYkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
مهدی طارمی مهاجم 34 ساله تیم الوصل در اقدامی خیر خواهانه 8 زندانی در تهران رو آزاد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/31037" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31036">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from؛</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snfilwBHiYZJ3ZTUVXXBZno1p7rtsZxohxBQ_Tso3DMG5z1vy41uHni-EEMIwl7zCiRRW6-L_4Y-b7IABoN5cj-LnImXq4Mn9-XOzokMBKmVeKrL9u0Cx0DTKkDi2AH0XLLI1Tt9obkKqGS7Dbb0jgrNTK8XrxN06f8cGJCbVVmM1hONWfe_pg6cMAjiNZ8257m-taUuzNN_lPo28aS1aBzjcW3360lO9VRuGV2sx_gN0i6Ta9kCMyacE09KJ43TLrCANxtvg_6nUkvs1lz0vLTPMpVQ3ScNTTvmfApZgR76QjjJ6r_0eEonmMM__2My8oQ97YqkwssbRdBq3n79Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
هنوز شانسی بت میزنی؟
💖
فرم Vip امشب با
ضریب 2.25
بصورت رایگان قرار گرفت
✈️
@best_form</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/31036" target="_blank">📅 19:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31035">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvB1jK8mBkjeHzo2tnNoJ6x24z_pMsHr94VSM_L8dz7erWUEvwkFD9b88h9eChwzYcxrokiXI71NpUdPtBGDFBmkCclRAD7cDtC9lCFMP0DvI7344pAFu8J-vcrLG_AZYix4Hp6ISltiGxXyfbEzGZ5SsLAC-LEgpv1zViZqnsqxgppnJvlZ5nZcGIPchPLS4750NUpmPbCQ-Tk5NiDbs_6A65aJ8Vk4LFnU_f7MbPN7CP0BJ9u8MoDwkrrJKHefQofvcUZojqqCrMjI2pbPXM5SP2sWkC5p8gDb2djm9Pmf2XpVSbheVPO41pbX-Hr9uIKMDfIhhPxodfscCTiz5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های‌جالب ساغر مرادی و فاطمه از هدایت یک میلیاردی سردار آزمون: این کادو برای ما خیلی با ارزشه. سردار همیشه به بانوان نگاه ویژه‌ای دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/31035" target="_blank">📅 19:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31034">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFrvmyOFaodmFAgucb2wAw_1ShzbOPSCxsNQPl4gjDfVlkZQ2mZc079XBMfSgmtsvWLJc4m7pmc1bV6vDgmYkr7UhhO5J1jmmcNWuK8Pb_HtYb6us7Atj5kt3t2Yu3TNvt5Sw5Od5SVt_G3jnOtQcy0KjkyAXjTHifzyHCNOk65mtVJRq_58YFJ9d2LYqL2R2LxGjCmTPvPqtbS6muDFyeQ6McYSWcddU_3l-a5nV6XlL9ossX_DMml8Ss3c86IDagywIDb2DcAY0tBYB2ICW0mFgVyznPfeMsifxuzy5Vj0ZwVc1fJbJnbQWmMGSfj7eO8rrmAYuKwXZd6jubQFgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوزلو مهاجم36ساله‌اسپانیایی سابق رئال مادرید و الغرافه باعقدقراردادی یک ساله به السیلیه پیوست. خوزه‌لو پارسال با الغرافه به قلعه حسن خان اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/31034" target="_blank">📅 18:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31033">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOHQDv97l6UUmj_yPqP20HEOsIlx731dhBjtwEre0tM2_15GGn9kb2Vqsl9MfU3jqSjQ_aKM4l05GKp-kp3WgkJBicZo0jrjPAOjoQLEoO1sPriWi0r9uE8bxE0JYkgCaCSgSljdzmVhoCj_K17D3lF3x7ha--SUwPOlxGOJ5pwSUzGGoVAFvv_Dp4D2XLorBtvt6Kw8SKJn1c9wlCDLK1JZTPfzQGtqMRwsCjjJBjkK1tYi-aJePsdknXbBbVHWDz47xTbBPWtXmyj0omRPM99NZLXQwsYzxvnjLu_d49cjVKEsxVSYvIkJ0dGPXe1GE0aQAm6Q9MjVV7zqkpSDYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
تیم‌ملی برزیل در سومین بازی دوستانه خود درفیفادی ساعتی قبل بانتیجه‌پرگل چهار بر صفر هند رو شکست داد. یه‌زمانی‌همه میگفتن که هند هم مگه فوتبال داره اما حالا فوق ستاره‌ها دنیا این تیم رو در فیفادی انتخاب میکنند. اینور هم حتی تیم گینه بی صحاب هم حاضر نیست…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/31033" target="_blank">📅 18:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31032">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yxa8wqA8sZp_YO79tRAHPLW0NmhPj793fOlG05rh0R70wZmq1AmEeYT_ep3B8ddlcbWkfp4xHK3hX7Dyos4K40bCYjFdUITtpfp6-YiGazcf6Hik7xyPLWqkyolUS-uUj3eYs4Lla1MRK6YNqn1AcMtIpimvluUzNlvezPn4U0P0c_02mrQz1H3FJ1Y8-BfEghKkwZ_OLDOjEiSvF5iSPmidh1zgLJJf8LSz1eEiedzPcMSj9ju6b0h_R5XnKDAhm47U4MxMdGgCcEe6uzYxeweqxDAUyQkMiyx-Zt1M0DAJ1v4YhgN0wO7wFMshtImM1VuWJ5wajsfgTrRiq-zutw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوزلو مهاجم36ساله‌اسپانیایی سابق رئال مادرید و الغرافه باعقدقراردادی یک ساله به السیلیه پیوست. خوزه‌لو پارسال با الغرافه به قلعه حسن خان اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/31032" target="_blank">📅 18:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31031">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMCOrF06160M0PS8zeuezlj_h2HOwHwwIt1c8989ewK9t8Auaht3odshIlGtZX9icVQqqvavvF2umW-LMejc6onOfZSsFI7ZCSD1CLCqtbb1BgbMSBK8yeucGY3Prmu0rFMs2x8sgkkTdEKJQ4Ke-VBZPQ9Uh6QlK8W5xcCydr6790ak-FRCt1hk9OQhvATuD9XHRx108uxYzUjW6PQnnH2ZhyCxqD2cNVb8XeUhu_3pdNNP8tB0b4V_a-A7YA_28UW1QvHcpGJ9BEoJ-yGKSZADshE-uvMYCW3HEaAPphwCOOxeNczXmGN3kmztYToxupPEsMsejTUiGrnX9MQ4eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گزارش ESPN از ایده جدید AFC برای جذاب شدن بازیای ملی:
کنفدراسیون فوتبال آسیا بزودی با الگوبرداری‌از اروپالیگ‌ملت‌های آسیا AFC Nations League رو راه‌اندازی می‌کنه. 8 تیم برتر سطح اول مسابقات به مرحله حذفی صعود می‌کنن و مرحله یک چهارم نهایی‌رفت‌وبرگشت‌برگزارمیشه و نیمه نهایی و فینالم بصورت متمرکز و تک بازی داخل یه کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31031" target="_blank">📅 17:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31030">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZ9ETo-5qnrW0-EGrOXSR9fqKcckDgIi_59aA1wOIyZL765psBl3hIgtj5ufyxQFpLmjhFu8GqwGuzvuqIQUzoF90zCJH_yWMftCMycqDR7mqlihD3lcO5vFNS6133uf1JUhnI-eZhbAzRHI0TmUnHPxfvRUXUcRaAC58QH8BCgvtYeGNakGNlryEyehtyAGmceFoOIgfMAT9wyoMQPb08BicbjbIP2olca0O0XhcfH9Llnbr1IE8rS_kr2FQ38wUYVlWc1pCOV8tJBAkQrYLTNsZKcOWwyEG01Na7YryFPMcsUuVPI8uhQxic9SbXwznx2-bgA7iAeLwa9YFKdolw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کلودیا پینا ستاره 25 تیم بانوان بارسا در بازی شب گذشته مقابل رئال مادرید موفق به ثبت پوکر شد اما فوتموب باز هم راضی نشد نمره 10 از 10 به‌این‌ستاره آبی اناری‌ها بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/31030" target="_blank">📅 17:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31029">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUyUo8Y-YwxrtTObe5PBghn22uaIo1YrAbl3S816N9j0KnN-3mGiHRq2oYtTbT3sp5mQOXHs6aNTFS0MyVTDzFU2zHkvRRjaYgYiVIcpv6KJqVlWFgqUpUSr7GRsgLXqijwqat9R-8BfRmMXOltNvtWeFfCXi5-vnWSnIZm6AHrGy74IBUMPyv78o30HCn5vlIy7r22yvyX85c-NZnQSYAaA4QEqlEYsKeuhDtHleve6BDdJFnT3lwNUuP89Tp9DH1XGoL49ooc4jm2EtDO0UtwBAZaKUIjKdjGxDVFNIeATLZyWYrjAwjVsbmSNl9SybqJsewhnMlc5HuJeNphaFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
تیم ملی ژاپن امروز در سومین بازی دوستانه‌ اش در فیفادی؛ دو بر یک نیوزیلند رو شکست داد. ژاپن در 16 مسابقه آخر خود در تمام مسابقات تنها متحمل دو شکشت‌شده‌بود که یکی از آن‌ها مقابل تیم ملی برزیل در رقابت های جام جهانی 2026 آمریکا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31029" target="_blank">📅 17:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31028">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cf5abb84.mp4?token=gMpidDY2TJkKMK9v07P7BqPGHkdFdMtNBtd7DA0vrbUcGyEtf2msRgApSE_3sxwpKMSfPVOHzUwsC0MEX4qr97gW3QJAxI1QSVjaswF6jdZKUIf7OE0XLyBr9CbLN0IFujUuGX_TDa7fo3ac8-zw6XEo5FDEGxdqO_AigIIT1tSaRBAJkQRnq1e-ZoQyWK0Oh-tkppcFzLbX8_VSiSYnZzIYna_mvsv63UUM_TOc0FkzwRe5d6zYMa_S9r9GnYMP8FmXb5AQir39z1-bDkcU4dPvtAMhuTBu240Z0BBpsjHLeWLSSmt9klCslSE548Fj5xUP7MEu36Slh45DZzJuhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cf5abb84.mp4?token=gMpidDY2TJkKMK9v07P7BqPGHkdFdMtNBtd7DA0vrbUcGyEtf2msRgApSE_3sxwpKMSfPVOHzUwsC0MEX4qr97gW3QJAxI1QSVjaswF6jdZKUIf7OE0XLyBr9CbLN0IFujUuGX_TDa7fo3ac8-zw6XEo5FDEGxdqO_AigIIT1tSaRBAJkQRnq1e-ZoQyWK0Oh-tkppcFzLbX8_VSiSYnZzIYna_mvsv63UUM_TOc0FkzwRe5d6zYMa_S9r9GnYMP8FmXb5AQir39z1-bDkcU4dPvtAMhuTBu240Z0BBpsjHLeWLSSmt9klCslSE548Fj5xUP7MEu36Slh45DZzJuhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماجرای‌شجاع و حمال‌گفتنش به دانيال اسماعیلی‌ فر دربازی‌اخیر تراکتور؛ عادل: یه روز باید یه مصاحبه با شجاع بگیریم و قطعا اون روز دعوامون میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31028" target="_blank">📅 17:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31027">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQtgC6zx7DywAqPZks9aCOBYYsA-KnqaNTPHH_CprnBPVWBBX4TvHWn_OTp_IPhxubBbzBL6pwI_f3jFIaYbXgNQ4CtXDFBFQtolaYgB3m3Bk9jrZthuVNS_WltmQmQcej3oihBKwB3r6SY_hLs8xuC6zJ1NSVLunP-P79DnOBFzIPpgDC5l2tahJHXTOHTNe3PnSZYKBGLdCy_80JpUb5vat3yPUQZv3InXf7L4FonN46AAvLYFAomEUqKmhTnLAGJUE-Tpwd5qRBHQeX0wXQloK1A_BF3Dydam5-yDhsIlj29OF7KTEQEl1POmpwf3Dv_TF1qTpY-ejZPRULS9vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌سوم‌لیگ‌ملت‌های اروپا؛ شاگردان توماس توخل درشب‌درخشش هری‌کین و جود بلینگهام آتش بازی به پا کردند و با گل کل یاران مودریچ رو بردند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/31027" target="_blank">📅 16:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31026">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eadafe2e38.mp4?token=X26AFDTRJpw94t8EYJYXnqw7N6Jd3qnTelWuxeNuMuBXKHWsWewemaB__hgMLnOQUPC-j-ywjb048jsc1Xk4PTiwgFY8rgYLrXN07cMcCVPpSmA_7aVKQxQQqiaOTBNS8kNn6u13sKoLvvieDb09vT_5aHD0ls3wrO_l116QJBGKG9O9zjBdaV2jZmMxBHN1CYQ-SIIlLeUJ7T1h5Th9_Q0WL9JLeEbWPSAR74Spx6_QjC5n6QC3AhS4OhuZFlXhjQ50zcvJ31N4kPW82Vp0qScKebeYJvbWBjut0HIk5eb0zS7JpT-W_OynyDJ2UPAgclZLhr7N_N_mNhsePSqfIZoeuoerv5A_3GAVMJ2WOD1dm7BU6mEakeRuhTF8Cd5dHz5aUN5XFSYot8vDz8NdnJ_Sh6QdJKsFA36mg9LXxFTEFBidO4g5xUF4DPUGy2CBuUr6jfYwbyuFZlfMO4DsnsTCRVrsMM3KamrmsL8Ct1SIkH_80gPSvh_76Ec3D7fRktGOrTpMgN38vdd-aRKJ36Rj911qkUjJ_zSv6PVhxIsoFNj9uEc0XiG0e7Np2jAbea2hB-Acg205uO0AGnjsaE2daLkpDiHVkWff8yUfkr3JK1tksI_N92nz_oa-6PmPjL44tAE5zqE3jy1T0f4bn-kBqtNE5hysBUTWyp1lHUo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eadafe2e38.mp4?token=X26AFDTRJpw94t8EYJYXnqw7N6Jd3qnTelWuxeNuMuBXKHWsWewemaB__hgMLnOQUPC-j-ywjb048jsc1Xk4PTiwgFY8rgYLrXN07cMcCVPpSmA_7aVKQxQQqiaOTBNS8kNn6u13sKoLvvieDb09vT_5aHD0ls3wrO_l116QJBGKG9O9zjBdaV2jZmMxBHN1CYQ-SIIlLeUJ7T1h5Th9_Q0WL9JLeEbWPSAR74Spx6_QjC5n6QC3AhS4OhuZFlXhjQ50zcvJ31N4kPW82Vp0qScKebeYJvbWBjut0HIk5eb0zS7JpT-W_OynyDJ2UPAgclZLhr7N_N_mNhsePSqfIZoeuoerv5A_3GAVMJ2WOD1dm7BU6mEakeRuhTF8Cd5dHz5aUN5XFSYot8vDz8NdnJ_Sh6QdJKsFA36mg9LXxFTEFBidO4g5xUF4DPUGy2CBuUr6jfYwbyuFZlfMO4DsnsTCRVrsMM3KamrmsL8Ct1SIkH_80gPSvh_76Ec3D7fRktGOrTpMgN38vdd-aRKJ36Rj911qkUjJ_zSv6PVhxIsoFNj9uEc0XiG0e7Np2jAbea2hB-Acg205uO0AGnjsaE2daLkpDiHVkWff8yUfkr3JK1tksI_N92nz_oa-6PmPjL44tAE5zqE3jy1T0f4bn-kBqtNE5hysBUTWyp1lHUo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعداد سوپرگل پشم ریزون دومینیک سوبوسلای فوق‌ستاره‌مجارستانی لیورپول بااین پیراهن این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31026" target="_blank">📅 16:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31025">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/476bc74d95.mp4?token=mlgqwGjIYx2zx22Re5limyBuGXY20uKHfW0z1ZQMScGXlJ6JYnfQl6TSTkgiP26ZhCniPraGvcG5jnmTwS3EPDIh1QTgpSlQEEiZ38lA3qFQijmeDG2xRCxz8LKl84trWePBxaQEGl8934OiYE6CZc6TfxIOANy1KbT4qM3GgLjpBjZ28T4npYcDDXNz6VxPU0eLxSIjy5mk5JEg6tu-6XS3mjdlKC8UKjXcHkS9BilPHVMR9uEXjgIO5K6ABbcX7yOcvVfrl97-5Ze1QGMyKqkMmpFPNtGx9smkIySwkWx4bpXad9m4LnmToGOpwlZRRC-sXu8u5bVewxYwUgovKE3jzZM6XAc1WNpjLpvqCDmjDXHhQL76dU2FErYyHWUNiFuiPGQoyrJB7ZiHTPvoSZK-BIBaTaRciwyCZTFbMqSja2Ro28VYkoNfM95oOREc1kOqgiRwTBdbp_EJMtfJ17_s3pueNf4NuhEqGUdSjLRp4kA1tD5yEjrkPbFDDISXUaMLSUQ37FTW6ZdQZQfFWDydsOXH0K42ALve4bBUuy6hd8Mi9a2H0OqriXUY7VyOSovrJ6890csMfnXDE8PVyk68-nCVEHdFqVtnNKbcfrLYYuZdaBYlJpbkc9Kuv0wG36gu-V6pR74bO_QBo_uBHXGnX8iq_kgd4qxAx-Ys9Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/476bc74d95.mp4?token=mlgqwGjIYx2zx22Re5limyBuGXY20uKHfW0z1ZQMScGXlJ6JYnfQl6TSTkgiP26ZhCniPraGvcG5jnmTwS3EPDIh1QTgpSlQEEiZ38lA3qFQijmeDG2xRCxz8LKl84trWePBxaQEGl8934OiYE6CZc6TfxIOANy1KbT4qM3GgLjpBjZ28T4npYcDDXNz6VxPU0eLxSIjy5mk5JEg6tu-6XS3mjdlKC8UKjXcHkS9BilPHVMR9uEXjgIO5K6ABbcX7yOcvVfrl97-5Ze1QGMyKqkMmpFPNtGx9smkIySwkWx4bpXad9m4LnmToGOpwlZRRC-sXu8u5bVewxYwUgovKE3jzZM6XAc1WNpjLpvqCDmjDXHhQL76dU2FErYyHWUNiFuiPGQoyrJB7ZiHTPvoSZK-BIBaTaRciwyCZTFbMqSja2Ro28VYkoNfM95oOREc1kOqgiRwTBdbp_EJMtfJ17_s3pueNf4NuhEqGUdSjLRp4kA1tD5yEjrkPbFDDISXUaMLSUQ37FTW6ZdQZQfFWDydsOXH0K42ALve4bBUuy6hd8Mi9a2H0OqriXUY7VyOSovrJ6890csMfnXDE8PVyk68-nCVEHdFqVtnNKbcfrLYYuZdaBYlJpbkc9Kuv0wG36gu-V6pR74bO_QBo_uBHXGnX8iq_kgd4qxAx-Ys9Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سردارآزمون به ساغرمرادی و فاطمه احمدی دو تکواندو کار ایرانب که در مسابقات بازی‌های آسیایی ناگویا به ترتیب مدال طلا و برنز کسب کردند، نفری یک‌میلیارد تومن هدیه نقدی با هزینه شخصی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31025" target="_blank">📅 15:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31024">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6e4569c9e.mp4?token=gE7ESD7b8DOqa6zNBHYalIU0C0GAlxXIOH41t3bNPUNaQeFq919XXwlAXradJcSPWB7Qlc2RfewUc-Klc24rbkV_BOIqtPIwsjBb3n9Myz2dDCEcEQxOBSBzfbHg-IIxDXl0GcE0mjap3oGv3zA3jcs-YFoQWBcH1r2TbtcbYEiz1kE7184XlCtcwgTHNnrqWPup3C8C1-8Ks2F9hghGld3KjDd1t6e-fC5w_YHh8E4vO89jimjGnNqR5WAinPZADgKR7Gqgtk8Q_xo0prOUwDvkRaqsR86yFJuy2jawHLcKemFKfjOeG5EmjNPXmi1qSzzOaCWt14a3dYffDW_iaoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6e4569c9e.mp4?token=gE7ESD7b8DOqa6zNBHYalIU0C0GAlxXIOH41t3bNPUNaQeFq919XXwlAXradJcSPWB7Qlc2RfewUc-Klc24rbkV_BOIqtPIwsjBb3n9Myz2dDCEcEQxOBSBzfbHg-IIxDXl0GcE0mjap3oGv3zA3jcs-YFoQWBcH1r2TbtcbYEiz1kE7184XlCtcwgTHNnrqWPup3C8C1-8Ks2F9hghGld3KjDd1t6e-fC5w_YHh8E4vO89jimjGnNqR5WAinPZADgKR7Gqgtk8Q_xo0prOUwDvkRaqsR86yFJuy2jawHLcKemFKfjOeG5EmjNPXmi1qSzzOaCWt14a3dYffDW_iaoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صفحه رسمی جام ملت‌ های آسیا با ویدیویی از بازی ایران
🆚
ژاپن درجام ملت‌های آسیا نوشت: تنها 94 روز تا شروع رقابت‌های داغ جام ملت‌های آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31024" target="_blank">📅 15:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31023">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYVCqs-5rn7sVRkcS22ngECM3LQuqzMjMp_bnVsxSawFx2s6r0ybvJV_VNTpzTC89JyjCpNP44SGEAWWcT-sNFz9O_-HvTvUKvFJfjtaDYJ60FawqgXCFWbivrBjsYduj5GXevETPKS5N4SwKDjVvEn7DZBIGTUW70JVPBJMBkLYG4Y7lfzR5tnfelXU6lYmtzDAhUmHxJOn16My7XWMzTIhKdQf5fXuRlHUzFZ84H9fuNs1VbdwCWtm-VNIbAHICR7r9-QdNgybBqBga5JgqTpjyR7FqCahR-e3BGXsm5tSjOJlBWjfM6Y3lJtdQi7SU7TwcAAr0tQ7XMGCBB1sgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کمیته استیناف بعد از برسی کامل قرارداد یاسر آسانی با باشگاه استقلال؛ با انتشار بیانیه‌ ای شکایت سپاهان و مس شهربابک از ستاره آبی‌ها را رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31023" target="_blank">📅 15:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31022">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LK0zgu2LatLfWdR3D_eM2cCjENdfCjxBoq-KDXQvSJJ61vkJJ5OyaVT7PBODqktZxJzPtXbGz986nb2d-wP68nPEVPyNY6mJt8IU9Fo6a_5UHVn6lBbtzd4NTQnxOVACYKnh_K6nQ9M6A1FsRO7nC4ntuYhkySIDU_S64rmOFOEmjFU6O5MpL-5ls_2IBk3XgXhbVFJJhciC7lgnTaipAgESK4yhiDgfFdqLQqHdgHQjUxrwiZkUZCSLq52l45t41eHCVnIwu-5qGN0niciqC17XNRTuTdsvTscEjbGs86fRdQ5f3unyg2OLplJZuEP4xkun0Edwnjf5paL-GLIs7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ خبر کوتاه است و دردناک: لیونل مسی آخرین بازی خودش رو با پیراهن آلبی سلسته از ساعت ۰۲:۳۰ روز بامداد چهارشنبه انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31022" target="_blank">📅 14:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31021">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8fOLOJmyUYHshDF3MGjbwFKUopGxu66MbEMYgGN4r-Sb8drxCcjOI6tWxbNqRrqwJpSKJrU3xcsw13j338TS-G4X9KQlRrcZXvz5VqB8dFObNOnXW3JxaUi2MIIQH6VsHXaKgErILYFz5gdL0DxweCyVsw7Jeg_kKOss1jkmqiggnAoNCt4y6mKYbmp0S2RCz6vO3nJT7tU8pweSjryETJ6A022jH_v5wWCXAFOLS3MA0pXO8aIT_HgEachQAvMq2_JQEGw8XhJXVjtkw8dcRmE6ljRAzfevBFXGD6Qb-kg7JtoVN0LOImMBwQVFC5Cs-37ygyHpu__So6Q0IBMdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
بیشترین تعداد گل زده برای دو تیم ملی آرژانتین
🆚
پرتغال در کل دوران حرفه‌ ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31021" target="_blank">📅 13:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31019">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oq_0u9KrBZS4zwpjlhREIxsetoRQFgUoqEgIS8fSUdQvKPlitcrwUzIqKQzrOAJ-CfibC6n2uSx7VBA223Hkzj5HoGn1bTiho9HAVTnVGQ53HGvFgTw3J4BJ1qFOmanp7uRn5UBbHuu29IgbJIB4mJO-yiYZu8JzYSrmSz_nkJHbfcIIzkmG5Cn8txy7l0pxUdNjDT0n25MW_bXiqBR4x79_R1grV6b6uAQjNn-km9X6EsFuALsrwP4TqRHdKlU02IoSBTCLMsyvXiiKPG4G-8nI2o6u6y8_n8VR8TJvq7s46w-7r0wVFO1ETukU8ad-ucfageTYfzzXdwCplPDf4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-oMyZhqkehN5FChNgUJvGjAV3lQFmCPaJT1HMQQERtn2WbOKBqGwt7mneQs8LZLCPwFoSfYG_YDSkNHdk8cHwOSwyKVzLsXAqsmkAWhO3LpgonHCxVKlclT5oGEw3EdRHb28eiXfEqhz9Lwct5LgjBH4NSxln4Kl2fsJbhOCocVfH7oMujSBfJQUOty7mLrC2IdbwK9yq_EoAl0bWKj0E6Es2WzFrHYMJ6KspDr22cQi1JXX0gmB0uZKTatCs57B_f1YZo9uOz7WOlvWgVEb3DDtjSlchmvGqKhhV6z2WsurdtkO40OKODfWhaBniJJHzis0Siv-RSDr1jtBOFfow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇦🇷
بیشترین تعداد گل زده برای دو تیم ملی آرژانتین
🆚
پرتغال در کل دوران حرفه‌ ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31019" target="_blank">📅 13:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31018">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLjVzel0ub7bcE7031k4wRCXLvII1X_n_Ngo92LE2iF5AGsrDQUpck3qbuKMDnJor4LfWuf3BYn6pvO_GEGlJBHRYfcEuxoKOqOl74XsUsdWE0eQiLEwXqkqxPxxAV6nnhBbnMlmbxodcia6Za5pXRdDCnKsd_8DkwiXEeftQKQZJ8wrLJ0Gyow_0TpeyC6Cc19PzNaDvGJMvNz0G6-mUiU-KDJQAb9bSZ7ll2zf3Bb4rlcbdmZyHPNqO_PgilQP3QBsiEK6VvSUVDmqrJ1bQJh1buHC-IXQNvYdlPGcPc-vddkqJJgl74tVJ6hDrMRNqd8KcmHoNPOWmf1tU0EL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خورخه ژسوس سرمربی‌تیم‌ملی‌پرتغال گفته چرا باید از کریس رونالدو عذر خواهی کنم؟ نه نیازی به عذر خواهی از او نیست!!! پس بشین تا برگرده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31018" target="_blank">📅 13:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31017">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/034d1249e3.mp4?token=fi-2EsDflj7eY_lVat40ZeLv3lZZyss2RUiGfPt4M3fgMdw5wUL9MUbJGxrDEdhbtkGUsAiT4BWWG66GgsqxjT5EbVIODajdO1jvwQ5rLsRgknSMXQ69_PK8hmYRl_FQub8BIgjzgoXNybDfsPRktDjkXc6_M0No70fJoXKDcz7peevJLGcPcukFUJAmZBJDUs6GiqHasAx3NR3-xJdpY-73-sZowYmitXE_tqqDtI_Ujbiu8R477mFNyCuxjbh-nUd0IDBYx64homP8_DzLRvKEez0r4-u1y4IK_gO3Serp0FfNKDMhTm7BJIt0hKmcDjlim8mI8WDO0Wx5ndQsZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/034d1249e3.mp4?token=fi-2EsDflj7eY_lVat40ZeLv3lZZyss2RUiGfPt4M3fgMdw5wUL9MUbJGxrDEdhbtkGUsAiT4BWWG66GgsqxjT5EbVIODajdO1jvwQ5rLsRgknSMXQ69_PK8hmYRl_FQub8BIgjzgoXNybDfsPRktDjkXc6_M0No70fJoXKDcz7peevJLGcPcukFUJAmZBJDUs6GiqHasAx3NR3-xJdpY-73-sZowYmitXE_tqqDtI_Ujbiu8R477mFNyCuxjbh-nUd0IDBYx64homP8_DzLRvKEez0r4-u1y4IK_gO3Serp0FfNKDMhTm7BJIt0hKmcDjlim8mI8WDO0Wx5ndQsZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
چراغ سبز سرمربی تیم‌پرتغال برای بازگشت کریس رونالدو؛ خورخه‌ژسوس: پرتغال همیشه خونه کریستیانو رونالدو بوده و هست ولی‌اون خودش باید تصمیم نهایی رو بگیره. من هیییچ مشکلی با بازگشت او به تیم ملی ندارم. یه سوتفاهم پیش اومده بود که برطرف شد. همه ما منتظر بازگشت…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31017" target="_blank">📅 13:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31015">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TT4anz9JMvVO1F-lGyLcqpFdar5Az106SVLUcBUmyQFqaSBSg4G8FhCTiNqt6E6lvwp_NmNfMKK0_HIga6Vzc8lDCLVXG10TUnl_ZyHCsMCllUuqItSfytUUU27R8f33I-jmiY8XA8dNZbrDRvJ1xh7N7OCfIy9aityCzZLgFW15Inc4QrIAfbFxDtQdMxvASaun8IpcwpPqhii1a_NinizKwtPrpl7Xz9JEq12QZddiFlF47PqFlUVyGab1wRPrjhvbgXxDtHhW63HuWxu-Qhe7hPqaI8RhZLT02r5lbpAdA8R-Lvnut0Pq90qCIUq1ruAtQleCEtAmqsT3-oQE7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NcNajzErtTqGs3NGHURYIt2Yvb5p1oKPmFjaiXgJwmAgAnRtJAzEjLDmVE1fdqRCFYxNADZX7ifR9ZhD84juakwCcouYKxAvKJO4Ia1T5c2pUD9ddmA1S3bwpF3oOMteBpgUR0bPNDsgGeZzleHk3_xMExYyl4mVs_TC0o_MqcM_5fGudcFuWvbIbmo1BgGM4F04TE35V3g9A3pHgeTdio6a2uZeTXoMcFc4UVD3jg8IflDdBtRMqIjb-VX5AcRFnBYvfBGo0Rx3OVFB_3mk8eGkogdsM2J7MptfxGWbk4RfpRIfB4gd08CaiROTMRnOtk1fzjRbStNuTzSSvnviUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
#تکمیلی؛ هفت‌گل‌تیم‌بانوان‌بارسا به رئال مادرید در بازی شب گذشته؛ وضعیت دفاع رئال مادرید رو ببینید. قشنگ میزارند بازیکنان بارسا هر کاری که دوست دارند در محوطه جریمه انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31015" target="_blank">📅 11:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31014">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiIa34SmIP2zYqy8TA8apS__fH5Y9L1MxXH5oHBRj7SAB3Da4V50sSEeNzVtuGJhYNLepetdTKIIflUMrscyEbyfkWY3FT_ZDxPj9ofsRltAM1Q4bClB-Yd43YlwOGPHW2pUDY7VpZiNr4wUVvz7RmP-pU6EZF47qQiJ8OFxqp_B0U-uG5MmI6dHyuwd2rOFk-QQfxbrbTdSYuDN_SH9pztOE11H6RNHZ_7aYFAgFWDSP210bOgBtWTwMy4QZapMKiJv2V14ryE73hAWpAjaGdnODHqHb0poTo9hfAo2DTloY5IqvhnLCDNiS0We9Cj62eQpGgzns0_iA8bN-EKjKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تتلو آزاد میشه! پست‌جدیدصفحه یوتیوب تتلو: امروز دادستان و رئیس کل دادگستری با تتلو صحبت کردن. درصورت‌ارائه‌گزارش‌مثبت‌تتلو فرداآزاد میشه!
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/31014" target="_blank">📅 10:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31013">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9IVnLgzg5ASq5xFMIlCir0vx4V80q2DUt2kCjWNxlqIeIpqiktB-07ElIw4PtClYqbHuVTi_OddANtcUUGwdCdXqQ0PRfxABiL7L9j8Dljxy5cgrBlNwGt75RW3O32I9RmazoNqpzBNVw3pzjFB2dWVsFVILa5QkC4gHr8CNCS7TMAs03xIcGVZyhKjtBcYPvN7FLER7yOYi7ZZcLQO2TGK45Q_emBQ0NPHGKH6r2iIPAs3NrbfqRTHWptVxtmk2J7owoGCASaSDt7-OGRJhAM5HN34WgRbRxWyepUlpXjAlBc3M1glcR5XA2oHY2LA25SCCPMPb5wXpA8M5FyAUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق جدیدترین اخبار دریافتی رسانه پرشیانا؛ کمیته استیناف فدراسیون فوتبال بعد از برسی کامل پرونده یاسر آسانی به درخواست باشگاه پرسپولیس مبنی بر غیر قانونی بازی کردن یاسر آسانی آلبانیایی برای استقلال پاسخ منفی داده است و بزودی سایت فدراسیون دربیانیه‌ای این…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31013" target="_blank">📅 10:23 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31012">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crsHbkcof5AdmF3WROmz56g68Fgnaw_-Qofv2W9vVJUnWNd572TLFchMGtYbY5JnpMoLg88BD0p6emaItRbzY8dzJzeJI2Fp-WhamOZXCq8fjyKjzMa_HAj9ECDbL7-YEfLe4NbDN_q9kR9_BnXV6br0vouuPU4rBx1zWaSxbRIzgMx1KhjwLI_GvcUYPiUM7RSOjKRluApO_Y-bAZ1qTdss4xiuUsSdj348SvTk7y_mZRWdStWPpSEoz4UhNY0f3JSoNzvXDUiIIK_xXrMq8r8TP6hWu65Ze7J1skCL8YF4w06FpbdixMgQX4ySMgm46W8WHr0Caewf07szfnytbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یاسر آسانی و نامزدش بعداز چهار سال از همدیگه جدا شدن! یاسر گفته بخاطر استقلال میخوام برگردم ایران که نامزدش‌همچون‌همسر منیر الحدادی مخالف برگشتش بوده و آسانی سر همین ازش جدا شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31012" target="_blank">📅 09:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31011">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU6oftHWsvwhbs7EijvZ6FJEl0haGEZP6N_p-LO-mjcXXMutfv8RtqxVZlLkj2GWQWrnnCNLa4pFa21uFRpu9oIRTU9oIYDZp3jPtgilgCbDiLos9kZxggrLSGO84Dykput67nYkcncQjMw503cI0rDvotQAiMl2o7f1HpKhJOMh5zITJqwUSqkeKjHX1vrJ9IsoMwB8zW28Bkj2k0eOmO-XyiIcK1nh5SaOV-hDwsGJvherVq7S7jYS1fYf2IMyPJWAPBe1T0zdHE96zhWyIT9kQRhePE0x-VQuyr_qkCAx5dfliufKOjifkNerSbW1BRFhB--uhGUUvDCBNbnUrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزنامه آاس:
بعد از فیفادی رئال مادرید قراره از وینیسیوس‌جونیورتستDNA بگیره و نتیجه‌ش رو با هوادارا به اشتراک بذاره تا بشایعات و تئوری‌هایی که توی شبکه‌های اجتماعی مطرح شده پایان بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31011" target="_blank">📅 09:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31010">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2e1347c85.mp4?token=ccNuVxWpAiBtlyr-DHu3BkMAUQ7li0Lpdk7OoyU4GOVjUL4FY8CAmgl06yfui1UP0U5M4G5k5PtSiASuxaAznvUFO411oihR2zqrcKdDuL4ubCOSATuMAjX_J0s6J20QFVXX8nR1lwU6dSoc9V3qYULOhekcAndUt8CJQPneRATsOVSc-uNuIVUhSiH6oM1M_twN6kTh7cN2PWzw00tWhCHCLpwOPRoxpebYpJteX_O0nA3rxk_KFImZajGAEdvwqd7ao-6sttU3JxXPZyQSFJghAxRRk3JOz1nrDGgh2R3pWHhv5o--SbDE07HT-3jr24GE9Fr_2ZwhS4zOWZI8AYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2e1347c85.mp4?token=ccNuVxWpAiBtlyr-DHu3BkMAUQ7li0Lpdk7OoyU4GOVjUL4FY8CAmgl06yfui1UP0U5M4G5k5PtSiASuxaAznvUFO411oihR2zqrcKdDuL4ubCOSATuMAjX_J0s6J20QFVXX8nR1lwU6dSoc9V3qYULOhekcAndUt8CJQPneRATsOVSc-uNuIVUhSiH6oM1M_twN6kTh7cN2PWzw00tWhCHCLpwOPRoxpebYpJteX_O0nA3rxk_KFImZajGAEdvwqd7ao-6sttU3JxXPZyQSFJghAxRRk3JOz1nrDGgh2R3pWHhv5o--SbDE07HT-3jr24GE9Fr_2ZwhS4zOWZI8AYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
تیم بانوان بارسا در هفته ششم لالیگا؛ با هفت‌گل رئال‌مادرید رو درهم کوبید و با شش پیروزی پیاپی در صدر جدول رقابت‌ها قرار گرفت. تیم رئال مادرید هم با 13 امتیاز در رتبه سوم قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31010" target="_blank">📅 09:47 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31008">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Im5_nqspB-i9cyJuXKZrhXBh7OKUi8fYoucVR2hAJDoFoI-sinqr9uSWW9cpNdHEwl9FXzGPfi-1XWygxFHhGcoKeiVqPXYvKRd48cT8tJcIal-brmESri1Artax68rNAaqHs82d007V17jCtct9iWkuSW9URTct9p_Elwyf6TQVIHxPttn6_M6iC8O9MEVeGlOk6HHtuHqXNblcB3-pG8TqBdQJN1aB6tZAeDS95rpId3dZwl7N1d4mZmuo8jHxa1amEisZYoVLQbeH1bm0jFAw_RQdoJ1kIetqFyBeUqAcnhyhwEzZLMIEcx8WVUF78VyEWNQCnSFNXKnW1pPH6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج‌دیدارهای‌امشب لیگ‌ملت‌های‌اروپا؛ لاله‌های نارنجی تحت‌هدایت ژاوی هرناندر صربستان رو بردند؛ ژرمن‌ها متوقف شدند. یونان همچنان نمیبازد. پرتغالم با درخشش راموس دو بر یک نروژ رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/31008" target="_blank">📅 09:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31007">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-zL_lHclxOWvZFmSTN6h0lxeCAIbZZoE0-tmduFtnu3Rf1vvLnatwlTvAcbLTXP4QkCIlW5CyT33_Qks3TUHkPQ2QCtZx7ilmOCz45V41E_Q1zYb_oZomM0VL4bvvG6nak5YjVJnvtrKYexJmTSRmnk7SHuex7VDAipgC9mac-G8DQIc13qz19sEN77ABPHTMvJB1HqkMMp6am7bHpeHrrWjwnR-ewsHAlg3Gbkv9enj0vSRtx-6yTjgZSQBetb37a5xxfxQKVzNAXdSzYqPDBwixyi87U64--D_BpCEDp4WhlF1SVf3u42o2WdUxnHZR-V75_E-33-mOMFRlG8SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از نگاه بیشتر بنگاه‌های شرط‌بندی؛ لامین یامال فوق‌ستاره‌اسپانیایی بارسلونا بالاتر از هری کین و لئو مسی بیشترین شانس گرفتن توپ طلا رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31007" target="_blank">📅 09:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31006">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d013eebfa.mp4?token=TeANuKPUjOwlKeF2InXiIoYNp82LT2NfoSFfFkG3KtFrjQcrxupN11z9PKhrq6MmoYb5uZGop5VU1nN2woxEjPHuZ_gE1hgAQO8TotT-hlc-Cd-HjK094GfJeKjUi68vNJLGbQTk2MqUevJYlVDE35rs8M3B1ZHYmVlQt01mII7KDgg61pxHTvAY0AtvQzk8DzPUven8UtZJu3W72rev9eQltLU9QlPZe1-81QPlqGGG-MJOZMZomMZTsdpbMifQWfoLZOzOEMsYTLQho--5eT7-fCMjVddRcFJJIWRME4J8VeKTH6XX8Dtq6hpgWROde1qC7wv37hZW4Y6RlkmRnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d013eebfa.mp4?token=TeANuKPUjOwlKeF2InXiIoYNp82LT2NfoSFfFkG3KtFrjQcrxupN11z9PKhrq6MmoYb5uZGop5VU1nN2woxEjPHuZ_gE1hgAQO8TotT-hlc-Cd-HjK094GfJeKjUi68vNJLGbQTk2MqUevJYlVDE35rs8M3B1ZHYmVlQt01mII7KDgg61pxHTvAY0AtvQzk8DzPUven8UtZJu3W72rev9eQltLU9QlPZe1-81QPlqGGG-MJOZMZomMZTsdpbMifQWfoLZOzOEMsYTLQho--5eT7-fCMjVddRcFJJIWRME4J8VeKTH6XX8Dtq6hpgWROde1qC7wv37hZW4Y6RlkmRnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لئو مسی اسطوره‌آرژانتینی تاریخ برای انجام آخرین بازی خود با پیراهن تیم ملی کشورش دقایقی قبل به اردوی تیم ملی فوتبال آرژانتین اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31006" target="_blank">📅 08:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31004">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2V-sLQL2lTRgQaFJrcNUkzvZp6HS02Y4LcpvwTctYmDkiA3OlSnM6d1hTDWmhwVY2eVr7BmVxWntyB8u2yKX8HrRlFcifZzxELB4EjegF4lkdWyOaolu3U2iX5GtZiK6jD602G97EuJwe77_m4T2A-5JdSICH6EDv0czRZFlOcHPc1q-ddqQAxc0lNifj2COr_PX1YjQfcRPUSNtg7GY7CSULC-u-BARHTcnZbzdBlqVZEERmaEZrm1t81GbDmp1EkJNSq88Wlt_uC3h4EiWWuf9zEyHRXsNNysm6eSqM_-i-rJiVnH8asIgM9UXasvr67L323CdLDkthZ0U6MKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ مصاف خانگی شاگردان زیدان بابلژیکی‌ها و نبرد آتزوری برابر سرخ‌های ترکیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/31004" target="_blank">📅 01:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31003">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDuOh50c0Zwdq0iLrRDQi-xJUoEdMAst_MkOyZSHgFJVR47B31dOObOqxt9wDPILLwJZ9eJp2pt0wiQXnFULK4YVhpck5Neyx3hPpWrk5cJrZy4fx2_GqgVjPgCqigqtI06eFVIrmViBDd1MmCM1v9-mctXmKY0JtcsYZVbUDqQMj6072TNF4GwC91_gkarGwPRI5mFmxMe-9b5UeqmS9-8ifqiIw5VaHAahDinCYWZarDYPzUelx29RRrfbtRYYAd73ZMxc9Pv2iipC2KvZZo15bXfn0Umko9tSiqk8_uB-ML32wNH1wT3UG7da1PNobhTQmW4y1u9pLIDSQaUuVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدار های‌‌‌ دیروز؛
چهار برد از 4 بازی برای شاگردان ژسوس و تساوی بدون گل ژرمن‌ها در یونان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31003" target="_blank">📅 01:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31001">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMca-qgIvy9sKuvIPBS9Bi4r0SkxBFZATNcYisBuL0ztexrDxURZzdKUiG2wPbnUToEY6UbouK1_ue1ZqRuIymVXXH-YmCIpe8t-Z8k46CgdLbrTXK6gnEmYOwC3bGNTV7i3Fi7fzI9eBWZyRKSuJllf1jlPpb38BdmFwHGZq8vwFafnhMGToFzX39bZ1LdjT98xLssviPhZI_639Pfs4ic6OHvUA5OSOzx-317mOMyc_Qqq2-iXal73iO-YXepcHosvNrxwmN4dStlBpy6t4Lst9QWPtWffVwxUdR9YxkTkZHnLR7FTN7YlmWocfc5ppUP7odA7a1LNGHHQAOpoRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
فابریزیو رومانو: تکلیف‌کریس رونالدو امشب مشخص میشه. رونالدو توقع داره که بعدِ بازی امشب پرتغال با نروژ در لیگ ملت‌های اروپا؛ خورخه ژسوس سرمربی پرتغال درباره برخورد زشتی که با او داشته توضیحاتی‌بده و احتمال‌بازگشت CR7 به تیم پرتغال در صورت دلجویی سرمربی…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31001" target="_blank">📅 01:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31000">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoTvBNOvhK1hJZZNBQ8fVUQosktGwI83pasArSOwXI2dkIgT0FpDysa3RW8s_bTGd0MB_uaD0kZ3w4wm1onpj6yUYqtCIz9t0fieDdnzR8B3OqVfWBAXYaq6hRQ5b7FMJ-4raXjQp1KvOhRqakJq795A2Bt5hLV0dR494y6m3AJZYNmnyquU-ZY3Ox9Ac6WWfdpYmORGuSTExMGtV1qOiR_UQLMITRjX8dQveCmIoSNHY7juPtMjI8i5HEJmiAfFNlTp0cDvQaybETPJfIzw-5kipHQc0sZQSlxjFJjNwf4Fg3a39B6qao6VfPuoM_68TXm_Uw_Vfp4GzT651EgcGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31000" target="_blank">📅 00:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30999">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇵🇹
چهار مسابقه چهار پیروزی؛ تیم ملی پرتغال به عنوان اولین تیم رقابت‌ها به مرحله یک‌چهارم نهایی مسابقات جام ملت‌های اروپا 2026 صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30999" target="_blank">📅 00:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30998">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xb3BQdCbOM11TA7NdnXk_4QREsSHbEcjxwSNBWyk_v1iWOvEsb_HrD49y98VTyM-G7pvQfXlceoenR0h12xk1kDafs3xC2XRN_H7-YED5P7zq7FHX_b27BMsk1-ZQGmyyAT0KN8jrUCLZfZIHK_2epYyu-fx0u3oOO0MHe35mhEuqcxN4rv39lC8HjR6zoWTdyi7zlpREPXkwO7J0E9nADWdtulJKhqtyYRcMPSL1BcThd2Y6Fml9RY_wcIja917Y9R_zzEC4Mfz09ONGN7M2knWqoP6JCLE7faaHvuyyInYTd2tqDTrOrB4FAQ-05WsxVtrdi1T745BKxQSEUmUNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج‌دیدارهای‌امشب لیگ‌ملت‌های‌اروپا؛ لاله‌های نارنجی تحت‌هدایت ژاوی هرناندر صربستان رو بردند؛ ژرمن‌ها متوقف شدند. یونان همچنان نمیبازد. پرتغالم با درخشش راموس دو بر یک نروژ رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30998" target="_blank">📅 00:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30997">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRoUwQAjmci6C6UCtJGI0LC3MbQFhdaKb0bNh8M5F7a9rhn6ZI_DOTJMk54w3xuPNbyQ-5xPcWwIVMB6lKz_xpYFDlt-G5KzAb8m84nC6k-TbbTaVqTqL4B6C6uIeGZO7S8qLDHQmHCQMb6v3Cx6Xx0eFT4XKuVfFYcayBAnBPnbRhNppUMKoDHXOTk2Ruu_w0gJkdPDX9mZ7K_frT4E-3F2g0GDJUoN-XRkSkjIllDcrfVRuQrJ6XOEW8C7EJuUHpSv6vNR05PNoAqrH2qlGKRaCA8GFwQk2GZu-lbngzxg_qFZSGs_iD9-nE1W63tv7I5bvxV-5pYlk_hUHw2PPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌امروز؛ هفته چهارم لیگ ملت‌های اروپا باتقابل‌مجدد پرتغال vs نروژ در غیاب رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30997" target="_blank">📅 00:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30996">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sB4X7qucWH8TDRZE0R54IyyrG3fsMYv_PRyenN7rJgnTcfhEBaLIWRzowVn52ZToCluiOp366zEgqOQfipw9xL4VmjU1LDz2PMzG-4A-zwTDY6i79UMfdO-kFVbirycijVjwZY5Jg75Q8p2UK2JKeqA41XG-DHUcJiVsDE-ncgojGr6pn1HKXi46_eCnL3v0nEXCY1JTegL2ul8mTEDxaaLMTxwWrEDo_zkChRtzRCnpHgElf5tqa4JtkEXTUGkg68fX1vcB-h1eJYkKxOfuiHR63nI0TE6Jdg93PRwxtHOrxYXiaAVfl5mvPXsDIYls0HdvZHdr_lgz1Aqd0-uNeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
فابریزیو رومانو: تکلیف‌کریس رونالدو امشب مشخص میشه. رونالدو توقع داره که بعدِ بازی امشب پرتغال با نروژ در لیگ ملت‌های اروپا؛ خورخه ژسوس سرمربی پرتغال درباره برخورد زشتی که با او داشته توضیحاتی‌بده و احتمال‌بازگشت CR7 به تیم پرتغال در صورت دلجویی سرمربی…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30996" target="_blank">📅 23:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30994">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9256e00306.mp4?token=Y7Ia0MIeAf8WIHMtg0eIklC277urD9USVYIuVxHrfEzrZthVkruHM4xCjTiw81fyiczCMnc8SoMcYImjRqEg1UE7mMAPgT93VR5uOf2WC3-a1Rm9Oj6QQxFGx3RvksiaKJOhblg3gU44bBGwLQ5EUunw-Fue-cCjUFyuBpxk2EsvMl0t1Q31YtSZJO0zNakBDnLd8B5hum0boaZXv0eRwViVHrjt4XKw2c4o158TYwf2mcVSPAsJwmM9mByTffAtIvyNFLjSQWHpIj6mhjBq9b5PDy16i6qNYXcx5q4Il60VFd54X-bT9q9W9mL8EYI36VM1EtK5q4nTBGDUa7g9Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9256e00306.mp4?token=Y7Ia0MIeAf8WIHMtg0eIklC277urD9USVYIuVxHrfEzrZthVkruHM4xCjTiw81fyiczCMnc8SoMcYImjRqEg1UE7mMAPgT93VR5uOf2WC3-a1Rm9Oj6QQxFGx3RvksiaKJOhblg3gU44bBGwLQ5EUunw-Fue-cCjUFyuBpxk2EsvMl0t1Q31YtSZJO0zNakBDnLd8B5hum0boaZXv0eRwViVHrjt4XKw2c4o158TYwf2mcVSPAsJwmM9mByTffAtIvyNFLjSQWHpIj6mhjBq9b5PDy16i6qNYXcx5q4Il60VFd54X-bT9q9W9mL8EYI36VM1EtK5q4nTBGDUa7g9Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شکیرا همسرسابق‌جرارد پیکه: برای‌اولین باره که این‌موضوع‌روبیان‌میکنم‌ وقتی‌از پیکه جدا شدم. یکی از هم تیمی‌های سابق او که اتفاقا رفیق صمیمی پیکه هم بود به من‌ گفت که بهت‌علاقمندم و در این سال‌ها علاقه‌ام روپنهان‌کردم و الان بسیار خوشحالم که جدا شدی. یه لحظه…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30994" target="_blank">📅 23:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30993">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkxOwPbVMnhvEFOr-m5sn1sJet2WbjSO3MQRUZn-oerIFCoEiMd9xNyzxrQ9qwDVhS_L13PMYvLvxRcCza_BeaJbO4d5bIcHrzB7LvudQCKTJdiJYq7SQq_5RITlbJLYh9F6nCcJUMzZWn37G4p25_YPL_c9cyCyvuareOb_xH5cLB3uVuF4oMfVapvsOoCP1kq8TVGwENcG8cCJ853kuhZHkFliiGePEfoI5Kkv5HO8_nNwjhPnb3adPnMBmQSJWqGbQQUIbNy5F5YeXqKwI8wiPDQUu7Uu-3h2kmhSWtchJy3OzB-Z8WaTrhEFgaawJM7tuuW8lLVJupF7fM76xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30993" target="_blank">📅 23:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30992">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f8925e4e.mp4?token=Acv5eJKvUsZyE9H_102faBm0f6kIAPAErBDsbrkW03ELlS914iK2upwva7tbC5SDj1bGHbj3kLGKLzbzIJmCrQSLGWe41gMmvVi54k0fJsgID07ogs1VmGGb2kRcR-GchnaB1E83DYaLssbT4VFylYFOU8yjA138USn0AvqQ5iOXfFwTAgLFKVH1wdYHaqDsjronSpO4mW2KpXz0jcW3H5jLtnfdVAy2rUqC-QynIdyZv-PeEfTqOREeBJ6I6Ydlr3cVmfOqymd9CCYLxuSgTsoscEg-4AHMg5eNchC--vRfm4YzSuccFYxX4IPgQySaOG-Yz2ESlxGNwU5fNdCy4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f8925e4e.mp4?token=Acv5eJKvUsZyE9H_102faBm0f6kIAPAErBDsbrkW03ELlS914iK2upwva7tbC5SDj1bGHbj3kLGKLzbzIJmCrQSLGWe41gMmvVi54k0fJsgID07ogs1VmGGb2kRcR-GchnaB1E83DYaLssbT4VFylYFOU8yjA138USn0AvqQ5iOXfFwTAgLFKVH1wdYHaqDsjronSpO4mW2KpXz0jcW3H5jLtnfdVAy2rUqC-QynIdyZv-PeEfTqOREeBJ6I6Ydlr3cVmfOqymd9CCYLxuSgTsoscEg-4AHMg5eNchC--vRfm4YzSuccFYxX4IPgQySaOG-Yz2ESlxGNwU5fNdCy4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
صحبت‌های پیمان حدادی مدیرعامل باشگاه پرسپولیس درباره شکایت از یاسر آسانی: مدارکی از ستاره‌آلبانیایی‌استقلال داریم که به کمیته انضباطی ندادیم و اون رو به دادگاه عالی ورزش داده ایم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30992" target="_blank">📅 22:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30991">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAbLhpJXazaf2mQ_vesLKSKjEK66d98UwZpg9q1oDjD911JDfaCAeoV2bAXxb5D4uF01g3oQFsQ8XBJr_1AJYq98fxij-pUYI9or9qs_pFGRIBhqxmB9oBxKMm4s57m7rOf-QKX9-LcaDNrWFWWz2PMM1l92XCEU0HbB1BYd7YUDSj6DeRD4Ji_xTriuga16WMuJArxDUnKp4bsBwSCD_f_Xw6sM6aQlm4EjuNYxhjK-Qm454arJIRpxBty_SXm0GR-FjNmAJtv1rV6kYYP5Lvu4b3bV8f_QXqzd2shDktzcp-A2GLZsjgkQjsKGrw9dWyMJHI4KS_G6wqv2dNQQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
ادعای میگل پریرا خبرنگار پرتغالی: کریس رونالدو مصممه که هزارمین گل دوران بازی خود را با پیراهن تیم ملی پرتغال به ثمر برساند بنابراین احتمالا درسال2027 به میادین‌بازی‌های‌ملی بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/30991" target="_blank">📅 22:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30990">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byETnMqNdEzXcl95rkiOzqJA74P1fgHY2T6hk5pqWzUj56lBUN6OpuuGA92n8wcaVFwXwm9JDcLoM3MSMuqsJBzGLq-tDsq9L_aqq_8th1rw5S54Qq4SZGGJquhbw8Jn0gOZkTetUpIouWzbmxnpEDRwhHeGFuplkueA1doHWpOIYpuYscXvP_v4OaVzp_g3o8ErVX1c5gBPCBocj8WTbOb0jLrGo2VoMGh_PcHWaRmfpeKI6RvbtvAH2K5gQxBPRwbKAmqHX3xDWGlqhyWGa6-9OXv5NWId1PnZLehwGTgtWNM87ulpzALTndO_Fr55j87tHGN7tvvahjgvDwwGlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درمسابقه‌ امشب الکلاسیکو زنان؛ بانوان بارسلونا تاپایان نیمه اول چهار بر صفر از رئال جلو افتاده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/30990" target="_blank">📅 22:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30989">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FisubgtNJx_-4C387Jk4BFLiyKlzNmzqUJtNlZcArdmi0EkyyU33i5D-Qnv8liqDqhctExKcnRP74Tsv25bb-R6efrvXqvXc4rOtCWcRgslAuXQtHhFdcstKVvwGh5-aBhGmDx9PaZuI56nqAG858V_5sb2n4H9mgOYttAI5ZNCGZoLisHktYPs0coVPnJddylQLUPLevhILqDoyr6KV2IUqLwk3AclmQckmCyR5cI3Vns775VUEDblPqN7Gldb_eGQI5cgNOr8VS1oRB52U76lXJUGMbwupKFXbx-NxsWDL9iozC4MH8GcAUPimcKkJhpfucZPl0OBvTqFz01CBvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یاسر آسانی و نامزدش بعداز چهار سال از همدیگه جدا شدن! یاسر گفته بخاطر استقلال میخوام برگردم ایران که نامزدش‌همچون‌همسر منیر الحدادی مخالف برگشتش بوده و آسانی سر همین ازش جدا شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/30989" target="_blank">📅 22:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30987">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlpGUNWo9R0ipBOrkufQCyhmix6lbW7bVWKniW5JdTC8iEc1swTBwUpe2GZQmmhkiNHVzWow_gMA_koRoDJOsCxJJouQLlfEKfpLWNi58blK9Z3vDWcxYL8U2tIjoBjDz8zoX0QJ5uX2a6QfeiXnbYIo9NLHr7j9vJkEMHtPOl2spMGegBz1-t0NqJKqza8fFUcYMLc1rJT9Zpp83ME7Fx7y74P2nrEnqCkRN6UFAkD7GtRAGn32UWg2tsfkS5EUyNQ9NkWjQQn_1_2_6FZHZl_7EKBk9Z7Pc6C3Illz14_q3A3CxCGTySQa8U0vqnV4OmJjrqhoa0ief3adRvRxvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3028cac52.mp4?token=bRzrdq0-e1HUpq2gDxqtx8qA88yRv6VhW2WsADHukNVOQZVWgAOhNaFhVOaTMDI5KK_RIfqRkIbH6HMDxYbrRLh4V8VYpsCu1DwbmZ9wfPlIZpzO5KFESsJvqGDr9t1coleo6bSjRuBBrIBE8RrKJyHnTnOl_3UCLgpF7I1twp1iw-uY8CVVk24cnZZK0lX9FTJ0AqnyIgZIm4DSh6zQ4d7Jl4wlRnOyrdZm7Z1-CcrXMOqwv7uTXO2m9yZBsyZltn9AR00fnJta9ONaWKWkQ-LjIejCEqfUAkX2nsm5UTMkDbpY8EMtWV2yqf9HLBLA-WfpwKHqvjFPYkakLp6eiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3028cac52.mp4?token=bRzrdq0-e1HUpq2gDxqtx8qA88yRv6VhW2WsADHukNVOQZVWgAOhNaFhVOaTMDI5KK_RIfqRkIbH6HMDxYbrRLh4V8VYpsCu1DwbmZ9wfPlIZpzO5KFESsJvqGDr9t1coleo6bSjRuBBrIBE8RrKJyHnTnOl_3UCLgpF7I1twp1iw-uY8CVVk24cnZZK0lX9FTJ0AqnyIgZIm4DSh6zQ4d7Jl4wlRnOyrdZm7Z1-CcrXMOqwv7uTXO2m9yZBsyZltn9AR00fnJta9ONaWKWkQ-LjIejCEqfUAkX2nsm5UTMkDbpY8EMtWV2yqf9HLBLA-WfpwKHqvjFPYkakLp6eiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ ویدیوکامبک‌تاریخی‌پرسپولیسِ برانکو ایوانکوویچ درورزشگاه‌مملو از تماشاگر آزادی با گزار مزدک میرزایی؛ اون دوران الدحیل تو 51 بازی فقط یه‌باخت داشت که اونم جلو پرسپولیس برانکو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/30987" target="_blank">📅 22:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30986">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et5g4nsVIHtOwWAsabs_Ze70a8nbkRg9no9iMBwvsIy258QmZtGls6CT77C-xH00Sh0mvDeTQVKO8NET8eUvv8AarUa543tQXt12B1Jfb8cGW_YI-7zl3e5z06gm_SNm4j-iPXzLO8HXez1Zvuw7nFv5w9mYXDGmU2EH9VEQJgb7Ji1UWdgVkxBVHmdklemnOVQRm6b0RxQK1eqMl3Wqy7H2uccb0g4fIka2467ozbPgb4LAZ0Nh-pTXUv5k6-GJxJszCbvvELD1VHyuZo-mbh6tJYykoxHxpOAqMe9w4SwU337tXdEqiR0CNCg0rLbmnUmZdPCDnczqXGsd8lQOaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خرید جدید تیم بانوان تراکتور برای فصل جدید هستند؛ نازنین دواتگر مدافع میانی که سرخابی های پایتخت نیز بدنبال جذب او بودند در نهایت با عقد قراردادی یک ساله به تیم بانوان تراکتور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/30986" target="_blank">📅 21:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30985">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18eb463e8a.mp4?token=StJowq_3120E3BNJWZec4oRKkwZzNYXT15NKzrYNLMUPXMQ2XdHQHe59yAK7covIPY-RcMGCbNW-eUnVJLwWizHPMXJx-QDvJt5fg9vH_w3JkB0aCWBO4XufnhdL-WCeJaoBiwj-jvH6IW9aCa6qvfg3qdqyk1criBzPpsNeHe-G5mob2p2-_HcvKxUnRBHe08cnznw_RUv6Ht6Cg_cFs5eymbykHTXTQYwegjGOt8p_5ZiDetXY0KTD6lJ5qX3oiSPVU_wUptx2VHue2ZSwViW0aZG_wQUlaU2EDGwc5RvkfwuANkpjO-7hi9x7cGB3Q09rwJBek1b-3bthUQQsKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18eb463e8a.mp4?token=StJowq_3120E3BNJWZec4oRKkwZzNYXT15NKzrYNLMUPXMQ2XdHQHe59yAK7covIPY-RcMGCbNW-eUnVJLwWizHPMXJx-QDvJt5fg9vH_w3JkB0aCWBO4XufnhdL-WCeJaoBiwj-jvH6IW9aCa6qvfg3qdqyk1criBzPpsNeHe-G5mob2p2-_HcvKxUnRBHe08cnznw_RUv6Ht6Cg_cFs5eymbykHTXTQYwegjGOt8p_5ZiDetXY0KTD6lJ5qX3oiSPVU_wUptx2VHue2ZSwViW0aZG_wQUlaU2EDGwc5RvkfwuANkpjO-7hi9x7cGB3Q09rwJBek1b-3bthUQQsKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا به‌امروز اوستون اورونوف، سید پیام نیازمند و محمد حسین کنعانی زادگان بازیکنانی هستند که موافقت‌خود را برای تمدید قرارداد خود با باشگاه پرسپولیس به مدت دو فصل اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/30985" target="_blank">📅 21:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30984">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfzRra0WZUJZtJ91lzQkYP0OlI_d5JQbHVh8imgmAwvaLCfBz_FkoF4PSKHD5gPOwU8ZPiitgIlbYwFCFEhN_BQQqaWMQ1nTH0OgQ2lgmtDE87Bvm0HzgQuqxq4GCIzT4GU17qfGVTXLpyYX49m4kpptICyGpQXHJTCUv4iVwDEZ2qw9stp0MA5g_l6gCTELvOdTXCPT7-vqmXSbrtt_sjoYOUO111NAZsAyLAS2p_kTlASri5Zb4h-1TD5V7aQXeDBp4vpDqfl48RaTEUg32q-Uoi7IIM7pMsC0bGXsLNVxtGEyTCD6VXoNy1JM4ipy6sU9CB9O4vyQ72FEoYTZUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد کریس رونالدو و لیونل مسی زیر نظر کارلو آنجلوتی و پپ گواردیولا در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30984" target="_blank">📅 21:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30983">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTVC4PHM94AhEv7unGgIqcklUG5qiB4NAZrLXA_pxXDtmPDGG8x1ASHMUitfXafEO23csU_IylaOLD8V_p2ppKZi2AxPue0v5JlQpdzMQY6wLW3MC6Sw-ThFQEFjPNOlgkMhyCmsC4i_k1k5qdtnkX5T8IZZzlzTkbzw38XvURknDq9v9qZJHYRChirSVOizDM3yNMG69_p4WgeASPhnPaP89Jll9xZXVLG-LNLpwm9E5340Etsei0m6FiNvPwnueLQau227ZmCE6ak3qItHyI-aTNuO6PBXnIfJVoxiJ8RUvee66pykNv1Cs0zmGe2Iy4DpWTFiX2ldALLT3SSO0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی و زنش درتهران: متاسفیم برای فضای مجازی. مردم در واقعیت خیلی به ما لطف و محبت‌دارن و هرجامیریم یه ساعت باهامون عکس‌میگیرن. مردم‌ایران خوشحالن!
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30983" target="_blank">📅 21:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30981">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2561d16fdc.mp4?token=hcXtkH6CmTeKR58LhOlwUJERRxvrdNrfHL3SQjA_UfR14xpXJuMDjHinkC8jAgoQGm2TlTk5q3uq3Sv-lS5-aaW24-SV1A6i73XysGyZY2crIKqemiX7k3Z9EtrDm24AOuZi6PEKEbDKT7yWAo6ve3_8ZVIivjzBWqeZs7ubp5YDr1isEo_jFAl-m3g1iP85Kl1s2MhNq98J9M3R_jn2Ktsldhr_tHUdTzGCYYfbmdgI00GMJ5jdbxCrwFA7bycPqNEW0UpyoERWp_lfQvT_xTm9lJANLBhCQM94VLf9pv0ArIPzccuv2kpiDivzDnzgbW2OyKWO5csg0rzM4Iywpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2561d16fdc.mp4?token=hcXtkH6CmTeKR58LhOlwUJERRxvrdNrfHL3SQjA_UfR14xpXJuMDjHinkC8jAgoQGm2TlTk5q3uq3Sv-lS5-aaW24-SV1A6i73XysGyZY2crIKqemiX7k3Z9EtrDm24AOuZi6PEKEbDKT7yWAo6ve3_8ZVIivjzBWqeZs7ubp5YDr1isEo_jFAl-m3g1iP85Kl1s2MhNq98J9M3R_jn2Ktsldhr_tHUdTzGCYYfbmdgI00GMJ5jdbxCrwFA7bycPqNEW0UpyoERWp_lfQvT_xTm9lJANLBhCQM94VLf9pv0ArIPzccuv2kpiDivzDnzgbW2OyKWO5csg0rzM4Iywpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توییت یکی از طرفدار رونالدو: تو امتحان امروز به سوال شماره7جواب ندادم تا به رونالدو و میراثش احترام بزارم؛ رافائل لیائو لعنت بهت تو چجوری دلت اومد اخه شماره کریستیانو رونالدو رو بر تن کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30981" target="_blank">📅 21:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30980">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jndCZyBYRVkW5JvnZsz5DhAtzH1cag_aFy3_v_5YcxncR0aQqJiRXsMDI7TPDTHy5D2zszqBHq271YoOX4gP7Oj2_PofaBhNqmJ3YOR9RWTHLV8k1chtRVY76VLMjPqCkFRll4vGqkj8061b86SSvZokfMUDRT_kY8ql95_rP9MhP3r6iXFe_YQuJ_AK7xZwtY2doNudBCsyXQ0WvfN6DMmIFOPuM5uGfTCT3hGgiiHK6zppDKLViVPMIHRrAXuRjVL3Cj2HfP68uYcI53RZhRl5GC4iZ6HuCkzh_lKqynyESxUa8qzleZPCprsrts4OD2lH658A-evAmodjuhJGWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درفوق‌العاده‌بودن رابرت لواندوفسکی همین بس که تعداد گل‌های ملی‌اش از تعداد گل های ملی کریم بنزما، لوئیزسوارز، نیمارجونیور و هری کین بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/30980" target="_blank">📅 20:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30979">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cy6a2pTEzMleWfKzkyRCuQ7ulzcqHaH13l2494dqWoqD6gIprWRyrL2NbFVUOu-OR90qkSkCek-HuB53xyDwBf9GVTYiH5rCO4D1Qqe_uwo0Mv9EDUCm7y4RGbEEWbdCHV3t7VBgqwKaSk7XI2gWfvmdrALtlcWscxk0MNGYBn2wUUaLwyUth6rorUS1UzL4EshPOpSwpZmjqNjX7D1JepIaeyEuyf2BmkSxzJVuZ6amRGWjtDYrVmEOVhra8BTrT2KYBvUy9-Dd5hC4BiIIvFFh9gvZ0KuY3KuKxfXni9-A1vhV3kHr1bn2ZtLiw9Vxt8rsvm3U3HG6JVTnBx4AtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌آخرین‌اخباردریافتی پرشیانا؛ مدیریت باشگاه پرسپولیس میخواد تا اوایل آبان ماه قرارداد سید پیام نیازمند دروازه‌بان 31 ساله خود را بمدت دوفصل تمدید کنه. همان طور در پست ریپلای شده خبر دادیم تمام توافقات‌لازم برای تمدیدقرارداد این بازیکن با باشگاه…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/30979" target="_blank">📅 20:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30978">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkytJohp5kK8V-VOIipRUP42CrpriNTBi7elJCtI3jixP6hV0IwgWGrG-TpsQ8ZoBYmiHNFv560tW_8Zc1jDNu3nOYTcckTfjV69gLCsI50eFIbH-3or1mPqQedJEczJZKrxEiJdalIkvqE3jbWU2y2O9r368rVHxQS_oVCM7eA2IYLtTJa_gFw8VedMwUbIMJwyWxLiLB7bFTJnNHhKza54AFxfM-vqKzKossxG0hVCqlACVhdSUEE0wXErFTvTy7BVQax31vega93FdgploDsLlRFAxqojf_0Os2UNhL176BVkc9hTXbxgpInfK6lKHM1X7hop0FVKxLA6pK6eIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه پرسپولیس با مدیربرنامه های سید پیام نیازمند برای تمدید قرارداد این‌بازیکن 31 ساله به مدت 2+1 سال به توافق‌کامل‌رسیده‌است و باشگاه قصد داره بزودی قرارداد دروازه بان ملی پوش خود را تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/30978" target="_blank">📅 19:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30977">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FohzDYcyoC_UzkuTLwvzcnDsYcD-BGf8iHL-JitwpeXEhpsM6LujqYL8u16ETFUmhAUZX0S3HCB0JRXVQfZ4zkDkHMm5kkofiIejxK28lwnZPkKF7uyPz0pjD8qjkqLs7lumtB0DZfIQrPxoT52HmUQJbMieY9wPIQLqOFXcJJIw_M45KNZqafBGV9AZtwsJ_Td5OgXtpvkyWdVmpDmYMTb2Fhn37IxiRH9s1vI_QlgQB_iPx4sO016td6Xv3CTV0Cxmu7mSQe4qfN3Tb3V9M-rv9-V3jrZmBfE7jZLVy4HdyYQoWD2WRYbL1MSDhrrIWTzJ0FiCZZVwRzHHRlzpaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
لیونل مسی دو اسطوره تاریخ فوتبال در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/30977" target="_blank">📅 19:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30976">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/30976" target="_blank">📅 19:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30975">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJiYnaIDdw5BUANjfBlCD2IkE4vsQ9cq812YRCHpIGmQCjXwq6RSNBdnS0IfaRcMd314GGlL2hMfjZn6RUYTR-X21Vneftsk05ZJRikVQGEAOCRRnw0JffQ-Eg1Svtn-eySR_1xnf3kzzvENQmbo2wmJ81rGO7ZgjWeTMRFdakQir2mkFkZ-YpCOpK5UQyAkG0mrKsBYiFZiVtTAtnjj8Ws2eTmTOmZ9Yhigghhn9TDEHuuXbfssbh_IdKEl2TjsQY1SUpzIphLMEZkvbUzx2yw20DNJsof7J_v3Pce3JhJKfHNNB-NMmOMmRghBJscF2W4iWsLC9vl8MDizqXxOJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی بازی‌های آسیایی 2026 ناگویا؛ چین با اقتدار در این مسابقات اول شد. ایران هم ششم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30975" target="_blank">📅 19:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30973">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6CurV37pQjO1q8oXiRL_yS8khp5fkDSegwFoo0HXEmCX3XqZ0-swdf2VA8DnJuyNEbg_ZregqiyKUMABL-j0rjv0wNC4sIcVsW_QOc3RVfr5BuF_b8EgqVWuuGfWfbJr2fiyi5nnteSEAAORXiaYqppMsnh3lwl3ypg8TbsX71xbSNWMPciufBkgxxUZhBN0pgsKOe2dQmbTltUBk_r0GwrZyIeN5iwGtSMTUCk2M4M3KRwmDqHEiOlXnRiUa6Q3t6L02tTnqaDMZMagUSrSIFQs64Mnh8gdSTHeapOpOVVt0HB2-lfWvyWxFEeHGk-F4o6teqIIuGs_eh7zBQfsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هایلایتی از عملکرد درخشان و خاطره انگیز نیمار جونیور درسال2016 دربازی مقابل اسپورتینگ لیسبون در UCL با حضور لئو مسی و لوئیز سوارز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30973" target="_blank">📅 18:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30972">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇪🇸
👤
هایلایتی از عملکرد درخشان و خاطره انگیز نیمار جونیور درسال2016 دربازی مقابل اسپورتینگ لیسبون در UCL با حضور لئو مسی و لوئیز سوارز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30972" target="_blank">📅 18:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30971">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J66a0M-3sYJgirZGHV7C_dpwbzcsUbg_1JA0Lf7W_dXHxVbNPh1ptyzvdkodqmCtOB8E1gx6e-MJ7T4l7zw7Tywoc_9ciFDD2q60lwhlMsAtn3k9-NgKTpYg0_MfwkerevYASdqZFvKaSFl67gCS29AIcxrt8rasvaKIEcek6Rp6KJz0Pi83Y0WgbsEBwra-6qe6V91awwEPGv7wFCFjf_Ft9wmTUiy1FfsMJVc7Zbl7qI-sPsWyBdxtQ_1-9FaeUQ0EXZd5R-H-1f8HGzxjAEguSSK7hYz3UjaCnogyFA7WqZ2J1wd1ms2uZruuoUJqiSYKgToRuc0e_GqlUwuu0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از شکست شب گذشته دهوک در لیگ عراق؛ مدیریت این باشگاه عراقی تصمیم نهایی خود را برای قطع همکاری با یحیی‌گلمحمدی گرفته اند و نهایتا یک بازی دیگر به او فرصت خواهند داد. یحیی رو بزودی در لیگ برتر و یک باشگاه بزرگ خواهیم دید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30971" target="_blank">📅 17:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30970">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbSP7iiXTJr9y0q6BRNVrf1PQYyunVibHjI_M1NBPCTegPrg4ZcQwqOwEduoC8xjq-sV10NqjDPj2mbn-EIjvwyPIM79k_008T5gQZSZmYrZMB6k_nHNvcRPlf_xoSaVeJxX_rqVcbReJAybcahwvEnhXGL1AO1fPYG1pDgkGEAhDshgF03K_WdOay3EvPpiDbqSx7HqBZfXWf3UUw19Cy7UR7YNIuVsvx9eTaaVemPLUe8xx_M0ytD6aUINJiY26dv64rxcQmDznU0tCp8e3SOIaXYPjAa0dHxTceFx1PFdJVWAzwPltkeJSYiHa1jfVRuaqrUl_eX4Xz-rzxmNcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر مارتینلی ستاره الهلال در مراسمی که اخیرا برای پزشکان در عربستان گرفته شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/30970" target="_blank">📅 17:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30969">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjrKa2TJpFg-ygh7yteHdyz9u8fmrDQSwlI0IeEEZPdHcfo-v_ZR_retD4bBb16goWvPi8yiqzcGE19OwsMzJpoSx6AYpD7qO2Ekksxkl8DbKC8ipE647PmfTglWdAc9jx0jz9HbwgI7W3vLOCLDIGiqYysGDgJkkbNfuoS_fy_lDLyGwTzS0xNqwLbBSdvcl3lyKdxEr8Vc0JgySu3mH7ZuNMzj3pP20tqn9N-MzXFN8OAO5ObtNG1ZPwKBlTsNLClgmGsOtBt2pKuZAOlksSjWec6uiEhJqLYJZ8RaV8B3_3gap6sfvu-suoc_oxKV_nBssONSkOmH56_j3c3Rrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ضربه بزرگ فیفادی به تارتار؛ علاوه بر دانیال ایری،محمدحسین کنعانی زادگان و علی علیپور دو کاپیتان‌اول و دوم پرسپولیس به دلیل مصدومیت به احتمال‌زیاد بازی با صنعت‌نفت‌رو از دست میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30969" target="_blank">📅 17:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30968">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6HrESorH9IloXQ1UpuqTfPaL4bozCH84ODhv5ASSGL-gAfxSrvDLPZtjtJ05THGBaYLDyqOQF6zdWFbA4cH7dvjBu4y5IIiu2jNbsx8hvJSFJhxNtnXO-IPef_CVIqkvqcQPOF2DHLCMnBSGpVlh9ipiFBb6qJCBodWkDef6oCELcsV0-37C3U_2tehY-wrsK9PJHbUbpADJku6VsTOon3mijKSN6Cuji9iqgYXp2NKMT4vLkZakqRriyWO_YBVwApZCrUjsxxGA36kbgZEg_9I7OpDLCGjjY8ehtkyQURKQHtfRywsptjT3dWw4k3v_3c5QR7fRDObdxH0ho8j7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رافائل لیائو: پوشیدن‌پیراهن‌شماره هفت تیم ملی برای من خیلی خاص بود چون رونالدو از دوران کودکی الگوی من بوده. فرزندام هم در روز هفتم ماه به دنیا اومدن و به همین دلیل از این موضوع بسیار خوشحالم.  تمام تلاشم روکردم تابه‌این شماره و این پیراهن احترام بذارم.…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30968" target="_blank">📅 16:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30967">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZdK1XPW8p9KhvMpcri3MRysBzl2k5ukQK3fD7OaV0OyMDlj_7MZdkfRpe_DMFKixoIZGrIOtEyK4ugTSQHtgNjo_SLli3LdosIE1r3vkbsPx0JfNissNUFRrbNA5ELzSd7kJV7tgaMWj6wOsjT9QthW6syJwHlgZ406zKx04V5v3X-7IHDLbsVa9i6j-OEXbHHPoBCGifw3leFyqc3FvFATyygCg4f1eO_RskYqNZeP1OaTB1rA8fUIpx0umhQx5GW3Tr0UGx6S4BVol5bmhi8e7fQVlwfI7-JZeKadkhl-sv9o84NeVDjKVWlxedPlUyzn2nDN60TuhyoOz5JlDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فدراسیون‌پرتغال‌میخواد این هفته یک جلسه با کریس رونالدو و خورخه ژسوس برگزار کنه و مانع‌خدافظی کریس رونالدو از تیم‌ملی بشه. البته خیلی بعیده رونالدو در جلسه حضور پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30967" target="_blank">📅 16:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30966">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های مهدی مهدوی کیا درباره برخورد زشت و ناراحت کننده پرتغالی‌ها با کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30966" target="_blank">📅 16:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30965">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYq5eXidh-sQ3744NsKKTAkntMCsSTVl1ueDZdntyWNm-fhRN3YGL72w-5X36rPcFrgcCXuLL1PVtnZYsT7NTWj_oHO7S5_cx8QitOTe2RHgLndvFgqxjWAip7BgXfCb-Fm7KB6rwJ-M4h_koIyUlsxfZQNoHyQ-GXgKdKJMPBSEQXVJ0dpeZ-owZBUNJxYxMUcMS2Vq3lxk_mf6GrulUC8hBjsxc9ax-a2mb6e66gFeuTKS0Mgb-RRW4M4v-IPtaXNrqXEzk8LsLddYHq6bjy1BbMYWf-2wETo2dXUjRh_9iU-1iRCemWqwUQm8MS8eva_D2RBcS3UB2XBQ81g1Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
حسین نژاد در گفتگو با روزنامه همشهری: باشگاه استقلال رضایت نامه‌ام رو از باشگاه ماخاچ قلعه روسیه بگیرد در نیم فصل با این تیم میبندم.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30965" target="_blank">📅 15:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30963">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3rhdf9S-1GEQeVaNGdI7Ao-HLY0pGKenwlDjSo3QoLWvN6Uy-g2oY5GQMtgRC8l7pJBW_u_H64Re7l5QkoeRUgX6544zEhbujnz8SGF8M5hZfUCYtICiq_NbDnxzKT6juoAqg_l_NyE3Z_6BzuyrZKLu2n12ltXfTzEZsTODuQX6lFzyZzyTM2zuRUqcVodr38336j8VgxwRH1NBtlhhz08--jykH6pA2jXftg4tXkpUenLlfn2kDGTXLXzife9bVuj8ZaaSI_DUAhTA8KpwCJWcb1ocEUsp7JYOf00JN41S0ctXztlvoZDfis7qVqfgDQYFFFuOO7JyNGeLEFJMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzAvdN8uXlGAULaPjptZYDGp4LKrnoxwadlH2HebJ6gj0F4hSnEvVUpj_8Wr5aRnb2LWnV-gwBa2TxMkivGcfJQm6S5g8KUgyBp-YiwMq8GKbtSPAxhKjuvIjWfenVLKasJkuviCPgyplOs1FtmDxC4f0FONKum0RrPGNaR-ufjI0ON1c2OQ4iKmIokYujRIJh92pjh2IedcLw2xEZ4RBKCYvDbSf9WUApCz8ZK88g9DxtzSoN1cNAawWm3uXgmQTBseyqeG_m_bT9nWx-YgItw8bu-sT5_hjLPCW9gJ-6_KobUefcCSE5TvKdeQFQ4IBrS045NCo3DfhwDgfLeCbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
طبق‌ گفته رسانه‌های عربستانی؛ همسر مارتینلی ستاره‌الهلال که دندونپزشکه رایگان دندونای 50 بچه عربستانی که از فن‌های الهلال بوده رو درست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30963" target="_blank">📅 15:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30962">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVk2EmgYYHFhYKflgXxMQd1SqLpBsXpiFY_Z1EhVZjDTbKnpKpdrdMF-fGyI9Hm27_0apu7JwXe8ZKcbrjWUWvk1IWJH39Q8HBq6QEjnE0NSNzmDphSlFuuU0pTMNERRR-wx82rrGWT-55m4d5yWhlJXKjBB4gYnSddyxPkXZAy4Hd4lzNbGPs-HP77rX8Ipx0wnAnSm422JRxO_ITMcpMmTHOGzKAeJm2LipjFMcyJlF3YD_fHUNsl3uJqp3jsZY-mR5ifcU7sAg4EAyHRUAdebFeAIgS1gVIDKf53N1L9HvEW0bjlp33zUbZ7YmgHc4dezAUwlnRKT9dB_jVJu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌‌های رسانه پرشیانا؛ روز دوشنبه هفته‌آتی‌باشگاه‌استقلال 30 هزار دلار به مسعود جوما پرداخت خواهدکرد و پرونده شکایت او بسته خواهد شد. حالا تسویه حساب با دیدیه اندونگ، داکنز نازون، موسی جنپو و کاریله برزیلی باقی موندهه که حدود 2.5 میلیون دلار برای…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30962" target="_blank">📅 14:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30961">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5a6f91b47.mp4?token=HSfP26II-vyFP5dFpZRO2zJ0bJaRnM5TkXzqzQcB-vYTQVu18B2cBGtzl5UHwqTCAobkklYAwgw3OOH60jJzkX3xtECL0nW4DOiGD6rF6N_jvNda442kutm6xNqbvW68cblbs180DcoVox2fUbzQwXTKnfKOGzHTcS6q5GUKuJnBLLPy009SB81EP1TzpWKzs0E1dxWI9F4I0fQyJfLgX9834ubF37eSOPon4tOT9y7s9T-zWcdX_sz4B-2JrVTwLp-jznKiYOUyVhb4VewlEwqI6oAek7llnydAVF7tO3DDgR0GS_soLdwY-InVlTa6o4yvMkmqpQrcztEu2pIA5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5a6f91b47.mp4?token=HSfP26II-vyFP5dFpZRO2zJ0bJaRnM5TkXzqzQcB-vYTQVu18B2cBGtzl5UHwqTCAobkklYAwgw3OOH60jJzkX3xtECL0nW4DOiGD6rF6N_jvNda442kutm6xNqbvW68cblbs180DcoVox2fUbzQwXTKnfKOGzHTcS6q5GUKuJnBLLPy009SB81EP1TzpWKzs0E1dxWI9F4I0fQyJfLgX9834ubF37eSOPon4tOT9y7s9T-zWcdX_sz4B-2JrVTwLp-jznKiYOUyVhb4VewlEwqI6oAek7llnydAVF7tO3DDgR0GS_soLdwY-InVlTa6o4yvMkmqpQrcztEu2pIA5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های مهدی مهدوی کیا درباره برخورد زشت و ناراحت کننده پرتغالی‌ها با کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30961" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30960">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRiLoFKir0lUAagpT_J9YDArX-loGlztCWITJxZuMB9KQNY9u--nlIvLFNbbAuCaHEVJhs6vla5-3k8kDP4bqHuSflk1xcHPs_9WZIqFpAGwU7mQSa1zDDRkz1tMYB0MnrhIhXoMmDPrbZinGXyPRKloF3doHak3IiUL5-ECuBf6itkkOPIiuXytdWvdFVP5O7KdqURsb-iK257No0b06nZv3P5TlYQDv0ZNwQdKEA6LsTddOORg0o8ivcvqguiC2cmi_zsY_gkIX7J8mfLyaw1Fj9LhUIjwfvc_SXmr_QZvRX2VFlSOqjhvzNP7tlFgnyYVb_Q949Y-olBDlQOETg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ با منتفی شدن بازی تدارکاتی سوم تیم‌ ملی ایران، هفته هشتم لیگ‌ بدون تغییر و طبق برنامه از پیش اعلام شده از شانزده مهرماه آغاز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30960" target="_blank">📅 14:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30959">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVpv4veBa1tQPJwrgiTpzqpWyET_IYo8yDH7P0MgDKCVa2OTb6OYTwjGKFNIgXfQlpI34EWZDgHhJBtKYoFr8dxYX73AzFc3Kav0U_PlfJSYCyPZrcsIc2ZG37K2eGTjn44J3HFnfPI62R8rAp_RJz_rE34gtvXalHK7x2E2gQzAxFgwdjnI8aAMB1-Kg5K_SlfWyJ_CxmqLoXH9oWXMPrqwqzNqeMMLVMo0V2XcaUbbpL4Y9bpKPEGjxx3WSS9d0Js1JOaPYI2ny96IUkVwmTyFlzbhtiU1qOSZnZObJAVwiRqy1bnNbJksqmcCkkbIsa1Sr6xwsY3Aqavdys7FIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌اوس‌جواد لامین یامال را یامال سیبیلو خطاب کرد؛ جواد خیابانی: به خونه ام برگشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30959" target="_blank">📅 14:17 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
