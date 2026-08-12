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
<img src="https://cdn4.telesco.pe/file/WPcZrfs_eJ9rPXoSQzDSTH9J9gkSP4p5WxFxpEbqaDeobq7LlH9sanTMq_r8EGDEysZUL3r-CHwVxmlHKZxJ7FMzlsNOS5_eqnmaW3t1s99g1SFs_mLQGEFW8LarcdKuByXcZ79OIyVVfDLTGeHVbtSPpBh1ZTvhueGemk91PAyJICPL5nWMeZkSJ4wla34q-a8lrZltZVJ7VapHC1mXvla3Oz3BYvMsZ9bagef70e1bnYWufbkEdP-OYDhITvdGMc1cw1BkvVTdN6rCS3siYrUpF9iG3VBS0oE1ymhJObBnncdnhBcdV28_bVFxHm5DJ8pZvDblMk41MwLtm5yjbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 624K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 18:56:42</div>
<hr>

<div class="tg-post" id="msg-27588">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWM5B4WqQlAlNDMcYd5Bn2qmoo0JZWaO5JGkFu2g0jVl1E3JaXR4iEfYgzGpxLK4OfMqIZWMaAq3LhXSSq4ZlH7EtVEmtVs0EfdvDc_ghBka3yT0ioYSM1503G6w8udX1m_2edJCur4d3bx-h5gty2rWxtzeBlRb44THy-uiIBOYFVqKNyDCNOEdpQjdsyoKmdu9jw73LwyhGWn6D70DmSq6SF2bExWvgxTyyIfrkjlQxAEk1e7c5xeAKB-J6GvlKG31qwHObrrEa4fhw_Mq7UgxTqGosfiRUQAmuPMb7GsKx2wnrqCKlAmkPN710id2B_WplpDPxWkqdE0PNKXpbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغام سعداوی برای‌خدمت‌سربازی راهی ملوان شد‌.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/persiana_Soccer/27588" target="_blank">📅 18:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27587">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpXzPA1K7kxaeRsrW66viw6ztHq0rqFo5cTAq61fV5vxx-SYtd6GxNw9xah_plgGkeR01jKZo-yyqs4S0gr-POFUqreoCcmLO1GbJ-7jpvpQuoteSn8uTjm6Gz-uVwxS3F3FwALSorICoUBHmOqwuL5YuRlz7FBPNxgKrg1aMCyz1D30eKF5RTnMCCmrZRwbn0ktAWxDVNqiFXmX1oW23Z1fjluW4KaddJ5mFEaSJCEOGfLp6JS9n9eD2Ltyds73EqpRFIan9Ge28dTYKQoI8GKYnAMwmcrNHLlxsVHfqLTTimpWeNeTNQAhyAL50ow2W0Xy0GBW8M3mClw2bv6t4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/27587" target="_blank">📅 17:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27586">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DU7hxA2wnJe4ukOMPvBs_ZOF8ljwbgSK9smn1tP1zMDvHk58IdmCpkQ1hTgjFFtZtc7yTfuk8RuYO36ZcEuQicz28e3Dwb9IyNzA2V2nDAVAyM-ly2TBfwXJDBZF_Am9DMp5hCY6Tf1JBsNEHrdi_EP0dDDUBUZfVf9BHOd1q5wL5fieIgA48liwo0hP2Wa6kKou_3_1FsUxKqK3yEdzTUwDW6qw_mv56ZF7-lbW1c6bM-F9XfyU7Fz5LuE0amKDnUt5gJe5DPEcTegTdqkavizKPO3PyWmczYjGQy3KzSvJVHUw6fnKsxFsOBSHgdbFryS-hxGm2jR7lVrIUadPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🇮🇷
مقصد بعد محمد قربانی یکی از دو تیم تراکتور یا پرسپولیسه؛مشاوره نقل و انتقالاتی باشگاه تراکتور حدود سه‌هفته‌پیش که در کانال زدیم در هتل المپیک‌تهران با محمد قربانی جلسه‌گذاشت و همونجا به توافق شخصی رسیدند و منصور عظیمی به قربانی قول دادکه ظرف 72 ساعت‌آینده…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/27586" target="_blank">📅 17:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27585">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ktx5itSYO7ehn_y9-0ePxTb7f_yp8ANEcbwhxaXlQ92wBNO3dkHK66wvuR1ozhc-XtiqeVYM7XRGuIjJ-1BF1HRTwrkYR8_lm552LehyNpvEB2NUe-hVpbU5HQSvaIPqKz3uKTLrbKSQLb4C32YyBcFKgHZU1u5d25eMKTScqN8dBe88Ax9SQvN7DtrNDoRedAICqA-Fjo1lZQb09TrhD0SjjpXS4kaogefyvJDU8APwtlKL-66BiL9wF24NuGPRg_cuDWo0fUZ5FWOJfqm2MhLhwy3j4L5QC_bguCBHgk_JnjVAuX5IoYL5LIlgnrKcl2jpbD3yc1nft6ud2R0CQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه اینترمیلان برای جانشینی دنزل دامفریس هلندی؛ جِد اسپنس مدافع‌راست26 ساله‌تاتنهام رو به خدمت‌گرفت. هزینه‌این انتقال 31 میلیون یورو شد. اسپنس انگلیسی فصل گذشته 44 مسابقه برای تیم تاتنهام به میدان رفت نه گلی زد نه پاس گلی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/27585" target="_blank">📅 17:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27584">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0r34kpljLJIcHiSAgektvh_yfOwpHE-kg9Zhk-oPRTcOHvgg55cN8xRLmy9-_Id7gcj6GKJ0w7zc8j3ZhhGjxUCpIaa2_ashXYIsx9MbGmFVtp01K1oDHAIZlKq0MgKRnJOL8HqQeFrr-4D13Nt2ebTl-yEIG7UJi0oqRUG8rcqbmPS3hbJNz8TDvuaVmrPCeTDKzaa4jnNAfqU_b7q2o9KGPmwMXdgeSaOt2-6o61WjSoMgL9kehb-BjSAp7Gz10SI3YDpVgpYwM4670iAhUlBgpgFVrIovBmx7nH29VkX7S6g-df3vlbJYClAuUGKED12ua7r1UbSOkWf_MQIXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس‌رونالدو به لئومسی تسلیت‌گفت: «در این روزای سخت‌آغوش بزرگی برای تو و خانواده‌ات می‌ فرستم لئو. برای همه‌تون آرزوی قدرت زیادی دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/27584" target="_blank">📅 17:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27583">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odpG9R5mPgXK3TLWy7WsBLn5mbB4khGcHQ1VrHnjL4rvOoKeZvh_ULhhgbAefGrOIn-1buWlz4jM6d6r1RSCLISgjas8O-w3NSbSzHh1UXToiliyxK4_2bgkrKAJXs8JOTYhkDDEoGk81335DVMe_LZVGiPBPBYa1oQsgAzKQDzJnHFghOLJkyL7X5NcZCoS3spuNyOMkhjuUYeZt2NsSfsgkZCnFnvnIBnVjJDkEmLj-sb5zNrc9NSjG5pS_6Cg0Sy8zAF6lM1ne29E7B25VZrm8sV1EUNTZpNYNdnMRhCgYYLTgT30jdMdW2MRoKUGB39GojCqq3g0ynpkTbNCOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس‌رونالدو به لئومسی تسلیت‌گفت:
«در این روزای سخت‌آغوش بزرگی برای تو و خانواده‌ات می‌ فرستم لئو. برای همه‌تون آرزوی قدرت زیادی دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/27583" target="_blank">📅 17:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27582">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAdSVqpV8my8c8x-Q1LWwP9rMuEcojI_xloW6OirBie9MM2LFhhpYZ6qr3QYvRFFx0S5eH-3pRlKgOuzOcXExILSDjuW_SHV7_LbKH8o7mrmgKdjKIL6BnhaLgNh60a4BvjvZ1RhlqPFJRWKEN1tspFe1aielGGq5U8FM4JT7gHY7pD9hllsaLSEcn8PdlCdsmpWgubMj0cGndk1dlo7zy9mxv0CAiFHP7nIrmeRo4Lmrbts6To7vhxQ9jKGEyASCwOtCP545Szna21rpPrPyOGy7qeD_STnpDdKon3LbAd3IsNqdSjYULUo2fZ3RBhCqIZp4nkfkxAxGt0cKkioYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
فیفا کارت‌بازی یاسر آسانی ستاره استقلال رو برای فصل جدید صادرکرد و به مدیریت باشگاه اعلام کرده هیچ مشکلی برای همراهی آسانی وجود ندارد؛ باشگاه بزودی نامه فیفا رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/27582" target="_blank">📅 16:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27581">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvDnaL-El_SV636BkHWaQVxBndFEpp3qeVBn7wMWTKuAwlUtr0eoda9yIDr2yQidOPWb0O5sHHnVX5T5CH2G6ytD1tq18902B8CLQzzqmCCnysk_WbhGn_S2VTaVCd0s0AfQ9ncNak7nqIF_G2fUpEcgMFjXjkGGz-E0AC3oYuHUR4oBGA-WS-CKNPBRUJZfo8N6so3zR2l0lRjxoMznxjqnZy-L9ZWMhcfPUYV3JA_VJkYehnh4b05FzVmNeG1LcTWfmwCIuBpbPmaHj0RGswg6wNz_ANG6L7o88SNW75dkt2V9cBCB7IUuQP2aMaCvmARPfDIRtP5MI2YKmZXN7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
درآستانه شروع فصل جدید رقابت‌ها؛ از کیت سوم دو باشگاه بارسلونا
🆚
رئال مادرید رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/27581" target="_blank">📅 16:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27580">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEXCTJpPdlBLgKhY3vZ4OGK7KmrlHU1usLyUpK6jcDl8ZhfK7TKbcroBMCFV9LzM5Rb9prXbriV1EQbnPEEgqiTIPHl8gW8UpQLX9ZVy3SN2GuafEHMSTJAP7vjymLR45MSv4sfJEgqQYIhcN1jc7uQwgxqhtfjZZ-AQAs8m_hzDMEl2_Cim4wNCoNhyw_2pdJmFU7Lz158aLPs-6HTbslCTA_uPx0cAi0FeuQFxqSSsUE0Tl0Nrki3d4xuaVCM40XipweJF39uNHbIy65NWoZG1kuTTKR1ms0HB6VPjxTyz693kM7sVvKpXfMmaePkXiIrIhQU9jL-Q7ydb5-ZZjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/27580" target="_blank">📅 15:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27579">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFICh4Ktln74Trnr7WFH_oK-mU5qGR2_oIJUEDF72wEHnyoT-BDuafXE41LPqUG1m4ioioDmX5zd9cen54KfTc3nAgN8RsumnykrPeeM3WzP3p4yGU3eVazIxAkRYMYMW43HCaUSJhV-uC7CruJnSO53ruj89J_EThvIsPEDxpQMeWp3RxzXcD283t7nVf004O2MDIpyre1qxlWzW51zoL2FG4poFzWf0pm92iHUr8GW9jENWwZoKYV_Ou6Aa880mS2lMckbDI7Vnw-69G1fYa0zbQwbkndkh_u87moSrPbB9NjPbAVfgF5lkauZT6-lWqN3bXxBUNFQihRDv_iFQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
چنین‌روزی درسال2014
؛ تونی کروس اولین بازی رسمی خود را برای رئال مادرید انجام داد. او در این بازی، اولین جام خود را به دست آورد. این جام، سوپر جام اروپا بود که در برابر سویا به دست آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/27579" target="_blank">📅 15:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27578">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTLsc2LynphsAU1SDrXzIJvModL6VovRFxP_B8-83E7aP57luyDWQIyQjLVotPzDfFfFPnp7pnJ9eL9IFK1LNxS4Bv8wjnJ9bsu6hlfL5kXUkB7uQR3K5a-7_yxFudWE_uKRj6k0ppiEKhpTFb3W7Y6j9I8Eyk1wiO4LUsc6VWEm6g1TkO2nf9_tfkj70LYr8WDp37E--15K6M7ok3kQow086ks0DfobcGmZjfk1sGxYPL3RSOBC5avguendTFTupyIrxWdy3gHV_4wx3VZza8MXafOwT5JzJ9xoOYqC907qvYc9hUjcWDCpkxZu48CcV2R-Ki4BM6WVw9z97mA9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال طبق قرارداد بسته شده باید 200 هزار دلار برای فصل قبل و 400 هزار دلار برای پیش پرداختی فصل جدید به داکنز نازون پرداخت کنند. بنابر این نازون چه برای تیم استقلال بازی کند چه‌نکند باید این مبلغ به او پرداخت شود. اگر نشود‌ باکوچیک ترین شکایت داکنز…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/27578" target="_blank">📅 14:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27577">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjAqcDx0ENZ0nsn4JhHJBaDw9d4B8xvKAlEZqrKiW9aXcwMu0EXlQHUU6Fk8yeoqKntpsFSJz3s1NdhT9Zo85oOcbRgeDhGGMMlKCbIA2jN_vkWCN4VFjZFvA1S8ARRj63IdTa5iH2PbvBkGhfIeqq40vPv3U0DWK2M30eWG-ozeyMpkGfj1uP1oWDqc1bG0QXzcjtJmo0m7HTL_Fk0DiQlXaPUOWVHofa7IEf8X0U5hqbH2Yh5kXZIvSKKoBgtFthRUziVQqEozFaPiwunFX3iCutlJiN-8-SusceICBfjKlnHxhFPiudOhu6VbO62Ung7yNWZZlNRMHBih3yau_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
#تکمیلی؛ باشگاه نساجی 20 میلیارد تومان تخفیف داده و باشگاه سپاهان نیز قول داده که فردا 150 میلییارد تومان به حساب باشگاه نساجی واریز کنه و قرارداد 5 ساله‌ کسری طاهری رو نهایی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/27577" target="_blank">📅 14:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27576">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHSf3JyT6DtUz8mD2ZO-YIzJfzEZcFcuJAXf4JHA2PH9OmwUs675Kvdv866tgnpAbFGKl4cWtTBT_M4eW1-HEkCok4ZhReXG7c-5eJHkmmcwPn19al5U0lnyBtOt8kDxB08WcAZck82ve8NqhKfaisBPgfGhKDLEkSgr_5xOgTdXCqPDP6K7khIg4--s_7Oc4MqU7yILoZZ4VuLnrMU1kRCUJO7S_BCevQEab7rR9Ts3Vq33_N0RWsic_uo_YKj--ZF8RozQnKD6TdwnXDPydgmjjjYHVlqYEvi8ssNnlQLnCWA9V_P0A4d9LKS84_2yg4Y8IUTj6SdHUYWowq_J8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش روزبه سینکی به صحبت‌های شب گذشته رامین رضاییان روی آنتن زنده: به تخم مردم نیست‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/27576" target="_blank">📅 14:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27575">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq66RhJ6MlS4R_xvhDe5cZJxdfS0303K10-jZAFilfwFz5s5QmXMADlRZFuDFU8GRbOuOS0Wm9e3u2ZYED9Af46WvkY9vYr8aLoa_960teu-gmIw9kRBWkdFLnzKi0-MtpKQkkw_PEIsQviTChHGrFxsgsOwoWgAHt6g1GGWpotNtx7bfk_vEYzjwYhOIIRbgxk_b0hHePHfWl3pZPsfZ2HEVp4cJvNmS0et_AkQotIqfFkwOfBWqlrV-FR4DbGPDw7aMhiDeAAYfTMRiMIUHs92OVban7cyRFTLjKfluEuMvC7jyNaMW1ikD-XwwPyHRNrgdJgePJaG2ASpEBD1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مهران احمدی هافبک تهاجمی تیم استقلال به دلیل مصدومیت دیدار هفته اول با مس شهر بابک رو از دست داد. باتوجه به این رقابت های این فصل بسیار فشرده‌تر از فصل قبل برگزار میشه‌. اگه‌دوره‌بدنسازی‌خوب انجام‌نشده‌باشه دهن بازیکنان لیگ‌برتری سرویسه‌. هرسه روز…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/27575" target="_blank">📅 13:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27574">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-8ZHFLj-rgmG0aeKQeCCVNPWCcQojDPR_4-Q8BzPa1VA51yB9PEcxlpGIhWnn45LfFCjZ-fePHDsQJrxQEUM0_iIzYC-88WVNLuZ-wIe1lxaesrFwqW17ZLbqjYReO73kfu77rnmdFTV6nChAK07QN8lnZcSuYE07pPH91vU2VMLB006PCq5G05p96lBcjUJBv59Z7yweECaY1NoBQKTd0P30Ub-VQ28TnZg6msnK8O3Lp9SmKm1dC52OGIbbHzDmgeITNjFGuVruxb4w3ScPgxr9itmARyGwNGlEH8fyG6zEUBwf7bS3N28jpTX9FgfHcCBh4OfzqAoEs38hnw1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🇮🇷
مقصد بعد محمد قربانی یکی از دو تیم تراکتور یا پرسپولیسه؛مشاوره نقل و انتقالاتی باشگاه تراکتور حدود سه‌هفته‌پیش که در کانال زدیم در هتل المپیک‌تهران با محمد قربانی جلسه‌گذاشت و همونجا به توافق شخصی رسیدند و منصور عظیمی به قربانی قول دادکه ظرف 72 ساعت‌آینده…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/27574" target="_blank">📅 13:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27573">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOun21i5izNeYOcsPETbqO_yoR77jpMkj3OaVM40bAGc4qykw7YuLPJX9WbmbqJw-Cj-TRJaxECJafSKfNguit2zzkBVRClfJu1L-uTg33IxR8lbvAxcOe2wEESbguYjrF7zZ8-zfkMraktrqelUL_trm4Z9BCg-HHgayotFt_cpgAwAwy6hUxt7jitw4mg7LjlBNwjNf8K5Kq8jRLYRNYaiwmgFpZwNJ0m4KJkN3g6qZwB5Ck2SAxBAWiPYrjJJP7uq0mMG9f-7r0kh-FRP5Lp91dngd8z5AlR-qzci0L1MmHdoBgSgX6pNgxjzSCHkyUhXaBxApnZREAozJJu5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیر برنامه‌ های داکنز نازون: قرارداد نازون با‌تیم‌استقلال درفیفا فسخ‌نشده و باشگاه بخواهد این بازیکن به تمرینات تیم استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/27573" target="_blank">📅 13:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27572">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/polUpzMrolXYH7EA75wLFNpqQbwEJWonTQ6yRTivPL3REK7vBlp2pMlzk_IX_IL2rOTCF5RjNCFeRV6oWTWHnWeFEoXSuVLb1p1Ag3v-jMCwOm9eVbIFKcSFVLcu1lkJQZmWv5gbFybPkbmF5vAHVoJcXdSl92P0SNDnH4CeFpAIlvdp-3w8a-AW78nBhicyoxpziRDWxHtHueJIZnz5ggsjxnlHD0Nea9Ez2cMViutpZ0vi1T-ZYSrx_pawcfrFUngAyFgAGUNCtucGEdioH04j1Yb-OKGLPqeEeDgaiw1guCzF4TzIBp6F_2parmUi-eeWqatOsCZiChHi9VIu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
بیمه ی
🤩
🤩
🤩
درصدی سوپرکاپ اروپا
برای اولین‌بار درایران
🎲
درصورت شارژ حساب و پیشبینی اشتباه‌بازی‌سوپرکاپ 2 برابر مبلغ شرط از وینرو فری بت هدیه بگیرید
‼️
⚽️
پاری سن ژرمن
🗼
✖️
⚽️
استون ویلا
⏰
امشب ساعت 22:30
🚨
ورزشگاه ردبول آرنا
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🤩
🤩
🤩
🤩
بونوس اولی
ن واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده ی تمام مسابقات
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr21
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/27572" target="_blank">📅 13:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27571">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OV2fO4KiG_KIOfrMx5H43FyZcbsg50EKaO18ttsWLsJA2SgFjcL2_jof3GYci_S6_ixwV_6C9gPW592tGVwbckwcJv7YB_ap6guS7lW8HaTdc38xg5kqVGRrxrLnz2uZ4_nSq8H-X3N3I9YjwI0WHkcw0MT0v6baLO0A-C07vozQ5fh1hlSefFrh27PtFm4EDHL6HArFS3fp0Ayy7jlkqqkv9fLnbfc9goEL2zgzYWdgFF73gE3T4BI0BJdyWvDRTYscQK6A_L5D3UBvQ1r_I6ix7OFS04iLzxfVZAVQykiUtPHtKWmEQ-fmI2mUjsQLpsGAARaBq2GCZ1C1nhUIfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌سائوپائولو داشته‌ازکشور واسه‌بازی دوستانه خارج میشده که تو اتوبوس تیم 86 کیلو ماری‌جوانا پیدا میکنن؛ حالا سه نفر از اعضای تیم و چندین نفر از کارمندای باشگاه مظنون شدن و در حال بررسین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/27571" target="_blank">📅 13:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27569">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIiHqTncLMcVCYwxMl-j93H2FzLgHXt9HwjCEdCs_2cLvWaE7Y8WjBHUn3tp5UstsGGXLwdFNPOisB3ZohunAGN4EtAbM32ck19Mq0JXpiMlmXxJgY8NyzUpSsCEGjg3YldByJLBTkvdbrVZWCKlE3jrYBp8sNjOjBbOQtxCRnIlhPvlZ-X0TNylbWj17dIArYXrIfBvyaAHN_cJn3GdkNC6KjxoxcBmVHZljGihQm4r_tnLfxkaOJh4u_s3RxCbbPpYNILW318-usuorvMdk8KOKG9boHAbGZrZo74wtxxhm41HwZR8HfQ779usGRnzT1AEZuJcMMCI0dHsXsOkhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو بمناسبت ازدواج رسمی‌اش با جورجینا یک قصر در عربستان به ارزش 22 میلیون یورو ناقابل به او هدیه داد و به نام خانومش زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/27569" target="_blank">📅 12:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27568">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‼️
#فوری؛ بعداز حرفای‌دیشب تاج برای اهدای جام قهرمانی فصل گذشته به باشگاه استقلال؛ مدیران دو باشگاه‌سپاهان و تراکتور به فدراسیون اعلام کرده اند یک‌تورنمنت سه‌جانبه برای تعیین قهرمان برگزار کنند. به‌اینصورت‌که تراکتور - سپاهان به مصاف هم برند و برنده اون‌بازی…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/27568" target="_blank">📅 12:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27567">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dn13Vx2Zbxx8q-6pA4iFgGq40Xywak8wO75r8sjjz4cY-zuEyS0s8xcjVcvkt1dXflFukOkKDhMLDuGAtxem1QWRWzT2rvgAMNcbXHkKOoBQj8-oDc5OZFkqeTTLmhVLMt8zjch2MfKQUMTaFrgCgT6s5ZyBqygrx4ToCjmEiIZZASNIK9q4-CCqvFxja2A1Syk0U-DkTnWC54ryQ98KwxiCQcfpM3phsB_XFyNx0Spj_-7i8QiAoWAztNP7UVA3pJBzrJWkiSomHbW4M4sDUj9k7j5vABTxkYBZYTpGQDgeA1eahhQFPh0p0BpgV46mv3N6JjpE88oGWxkW2WUfLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
بااعلام سازمان لیگ؛ دیدار این هفته استقلال مقابل مس شهربابک در ورزشگاه شهر قدس با حضور هواداران تیم استقلال برگزار میشود. بعد از 229 روز بالاخره پای هواداران فوتبال به استادیوم باز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/27567" target="_blank">📅 11:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27566">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ec3WuAPauD5BSa0TlBXLT_rleq_NQtUXWLozgkdB536Qni9dJ6LMJ2jiJVP2UbHl7BK-x5X-sRKLy64T7fgwzq7EqaOMq0DmtcY07yHaY0eRIIOndqRDIZ7U4W_zQNEY-bM4IscBpvHbKzYt1EhqQjJxcjdWZO5B19DZyHMnM5RJYAJYFqzZ1hw9ZlLubOVRBHZm_1BZAoXo1bk9Whti0WNIjKqrRyFmlP3XMDuj_jasyz4SvT-7NOUzwN8Ri9sU0ivx0xfML2iQFOyzMMxEBHXeM18qNPzPAwBLmkyfSDrlEXz9S1lw0Ko4jtpR3HXvFBYrHEFr-kshOKOg2GqDXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/27566" target="_blank">📅 10:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27565">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7L5PV6ewBSgNb8JRsiO53Lh8C9QwRi603LriGUJ18R0MXMIJzm73tzhR8t4z1TLm5WLBT0LN-CQzv9YH5Z8eKA4hPEUG3vyLoGLfJYZvLbR4ayyoEeyN7a85-bCLNMykXnSGwurIPFiwZAROTaM5pYkBM5WiD1fn6hQ4_gISbvbrbMWKyHQ1dcvdbH4b3AX0XvwffwwJ6lHG06Cst72PacjHECEhB9E8Tv1KMLeWcX84D9Ebt9y6qdVRi4d9U0AvpylySVYXER90lhnNudg4HcSDrkM0y4Ofi9ZsbnIITUVUQMKtxQiNpQ4FngiRydtUnGUf_XprrsYWbl_UH_XcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/27565" target="_blank">📅 10:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27564">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAN6-7ViViUNG0DL8ud_FY4GhNzpshkX7mHZ-nOIiocmqBi7jn7_tj5WcTg9jr48VR-FZ3Z6L9JUghYkCZVcMMuFkfRX6EwP1rleDEckm_GMw_mwXi-MROYJeNjOOHzHZ4sEvikd8Hn163WN0o5crwYfkSG4Rmv_TIQkq_AWfqmiIyfE0_qdE6AnzfBCNHFQfuW20yxlawSMPERWT5eofHTDokmy039-Qv2nqWIeFaTlLDYr4LqQpUt-X8v9oEPJ8ITYweL6a_Fk9eyz6WSJeGFMru4bHSzTrM0-0LOV32mcwYaKi-ii50wiEtdH8eKP722x3hY6E0v84ReheEzSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
دوشان ولاهوویچ مهاجم فصل‌گذشته یوونتوس باعقدقراردادی 3 ساله به‌باشگاه بشیکتاش پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/27564" target="_blank">📅 10:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27563">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZkL3H0Yk66PdNihoXSRfiql0xDAoaLDVS2BfXqkSfK0DMCYXgcwYo0obQUppejI6J-QEpZY0WK7R9BDCFS1MA6V4EaBFpwCBKRVV23LYaqbT-DyDaKUZwgPeNMTgp9RIlg_blbp8i77xiyItm0U8s-2XVoHmEw8FTNWzelnBPiTqsqQKwajqb7CRtCctCj-bn6zgp3dvUePpF7T6r-X1TDQHx9-S8LT6dQSbr835cuTjOxdpQJ8dGSxFfPpzk5_GMDGMMuOEQQxFn1buRwge-C6aq8iEMLzHI5PEwgkVt4sco2Ec2-8hO-QcAgXy7WHzwjdc9_fwMOxD9OTYT4lmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔴
خبراومده‌که‌باشگاه پرسپولیس عملا قید جذب محمد قربانی رو به‌دلیل بالا بودن رقم رضایت نامه زده. در واقع باشگاه پرسپولیس با جذب لطیفی‌ فر و پورعلی عملا برنامه‌ای‌برای‌جذب قربانی نداشت و با تراکتوری‌ها نیز به‌توافق رسیده بود که ما محبی رو میگیریم قربانی هم…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27563" target="_blank">📅 09:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27562">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofRPtuAG0dJ2mXea8OJmpjenqw9IpmBFFTg_vuv9R4iu0bIfmHk_k1v85nTR0r0PR35WN_e-z8DOxAawo7EO9sxadxwYUKSH7IfGqKtJ20IEg_1nM6nstLEJ_VBGM0NTu3yZZDNOIbO36J3LwEME54qSQsynunyG4RHJkPZr1HpPps0TJqsjHHjAoGVW3lrku2gvmrN7BvgFsTGHzUcgm639Ylit_8X0jPJuNaDtWfMqaQ_aqbwe8ALsHuHJGeBE75VLCuxF-hu8Z158xXdRgq89OSIY0ROM_5IeX7VFV0Tk3oYapCCtdgSJ2Q4Q3s384jZu74UA6ZmXemDV6hzQoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
#تکمیلی؛ باشگاه نساجی 20 میلیارد تومان تخفیف داده و باشگاه سپاهان نیز قول داده که فردا 150 میلییارد تومان به حساب باشگاه نساجی واریز کنه و قرارداد 5 ساله‌ کسری طاهری رو نهایی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27562" target="_blank">📅 01:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27561">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbVgnyGVe1jxYavEKUeiNQTGtgRuJsH3AWxeaDArRUIZqkec1sN2UzsYHLzGHbHc7FldtRqt0bkj5gkfQWUZo3ZdCZ-Za0ooEuQeIgCdcvixiWyPUy10eTBtLfvO-nhnDqxKJtQMBpFKbS9tJyN30ejkWnHj8PFtDZk5b9nOjsV3Rp2Ppkb5xOOP0yNI5Gr1HiPAkZBm0SYlZWIYanZtF1a5xi9IcelqjIZs2jCqdtyKpLJE-eR9PHRgL7Yg3rr-1Z7meGW965Dx7IEiHvRHp1hxsLPd4mbmBYbqf66EJlwounYQDFQYPUG2DlTCaDkwa2S22jnYX8QXe9TI7xGaug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌بازی‌های‌امروز؛
تقابل‌شاگردان‌انریکه و امری درسوپرجام اروپا و مصاف‌رئالی‌ها با یاران اوبامیانگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27561" target="_blank">📅 01:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27560">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9XRHXE53NnmG1S9XK92xD1JOVTk2YWHyh3MqFdvY2NtO_ho5Vvi3ZU-ejDsWU13j0QhdW0wjZw6IXSwerP2JKnHg8dx4fo47NKjlgbZnlQiEdzWy3Zm8JYSst9zyda_IXjE6o_SIV8Deyxd4IHmrli3wZsSaZp3m0qM7Buey1t99ZnPSOASgBdPWUcy3_regaB_zExAwAAy0CTi7Oj9antWJZCw-3I_I1h-psOFJlqYO6s_eK1q1EMc655n1iL2fnEnSu1WfUQcOpPqyy6xaJqy0KPTZtYpflMaIkqMngBGsMvkDwwVCufp-Biy0TClkvFfKOEwpPpaikDBJA9ikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
کامبک‌المپیک لیون در بازی برگشت و برتری فنرباغچه با ‌گل تالیسکا در دور سوم پلی‌ اف UCL؛ کارتال و فنرباغچه عالی مینوازند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27560" target="_blank">📅 01:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27559">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f71c3312d.mp4?token=XUeTnItkRDPDAD5bsZgNT60vDxk1AsiYRNd6gdiF4P0c7wClHivWn0AX2M6vMY_4CBYgkyW1iVkqIRx-emHQGEtpfYgftndLAf4EHsBV5wC42zymMTvRaIigA6Fy3D6p9A3wDXLfW1OnGCuOKrds6iCxZ4LefOxY_R9yZL0OKxI-MEBgOWrySln2vtGSfe_yGs1aZ4wU3SsWXSKr9LAWXaH1bNjQLga6HWwO_36TyNLL0iyiJMf3bguPDrnV-aagG08a1Nt1TTd8ktmV7yueVsr7wreAUO-iRiv2iT22c5z4YRK4xs16TyStgfmJ3Y0IxWcUyAHU6PsWPzfPq7kt2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f71c3312d.mp4?token=XUeTnItkRDPDAD5bsZgNT60vDxk1AsiYRNd6gdiF4P0c7wClHivWn0AX2M6vMY_4CBYgkyW1iVkqIRx-emHQGEtpfYgftndLAf4EHsBV5wC42zymMTvRaIigA6Fy3D6p9A3wDXLfW1OnGCuOKrds6iCxZ4LefOxY_R9yZL0OKxI-MEBgOWrySln2vtGSfe_yGs1aZ4wU3SsWXSKr9LAWXaH1bNjQLga6HWwO_36TyNLL0iyiJMf3bguPDrnV-aagG08a1Nt1TTd8ktmV7yueVsr7wreAUO-iRiv2iT22c5z4YRK4xs16TyStgfmJ3Y0IxWcUyAHU6PsWPzfPq7kt2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارما به‌روایت‌تصویر
؛ روایت تلخی مردی که به خاطر مسخره کردن پدرش نابینا شد. حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27559" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27558">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea240a7d2c.mp4?token=h14zzWGWcAn6P3LKItdgcKqq0T3c1lQ8uQ8BrkLckCg3oVx22Sr_otxk3Gm3f0qrbjhCvXggYWYHnEZ9T7vsYLCGeLbe_kU59AK_BWYZz9LXJ9_nnsJKmz2A6ItKEajXzRM_uas7GH86VQ2plAC5q_JIYFz6wqUpQme7NX8F-5-EydwhFvott3IToHizFXH8VgnEokzeNePLHbJOllVfulU-nUMWsoArS-gGhc_6GHuHGawZZLets51dI3wqAvVwo8jNjfJojXAHByQC9Z48oMAMrjos5P6OCsWlkd8IKvHcq-lvbk12xpyMh6QjQ8JjJivAjzeKlfCc2VuUt4Iq0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea240a7d2c.mp4?token=h14zzWGWcAn6P3LKItdgcKqq0T3c1lQ8uQ8BrkLckCg3oVx22Sr_otxk3Gm3f0qrbjhCvXggYWYHnEZ9T7vsYLCGeLbe_kU59AK_BWYZz9LXJ9_nnsJKmz2A6ItKEajXzRM_uas7GH86VQ2plAC5q_JIYFz6wqUpQme7NX8F-5-EydwhFvott3IToHizFXH8VgnEokzeNePLHbJOllVfulU-nUMWsoArS-gGhc_6GHuHGawZZLets51dI3wqAvVwo8jNjfJojXAHByQC9Z48oMAMrjos5P6OCsWlkd8IKvHcq-lvbk12xpyMh6QjQ8JjJivAjzeKlfCc2VuUt4Iq0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رکوردی‌فوق‌العاده‌برای CR7؛ پست اینستاگرامی رونالدو در فاصله سه ساعت از مرز 10 میلیون لایک گذاشت. فک کنم بعد از 24 ساعت عدد خفنی بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27558" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27556">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbSHv0LNbcEhKDShkKETpX_lZch_oeeWmCymEnFkaFM8lx8wzj8zmAFh4nsBkuRMsUQLB8KIgSaYVnNRMT0PWOEBnB3kngx9TQpMYuveDvwtAQwRKCiFCEHdiMRJrioq9VbnZzrP7XJ9aBcxr_oZ6mEWD6nN88y0ijNZ6KYNo1r0ZzG1wZHPlcwUf0QfzNqbe8FangBqgfNbQUSYkG4BhJeVL3ZqlZ1fiCDKtrAcSTrNa0IS1uyz0xMzmg_rCseO6I2R4-gUwbpqOdMf99lC6E5IiBPgKKBcT2kJzXPB5jBawJsZWuhcTPBWkIF2k3SpOiLlGmgneRr-noFx-Wm_cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
سانتی آئونا: باشگاه‌پاری‌سن ژرمن و بارسلونا برسر انتقال فران تورس به‌جمع شاگردان لوئیز انریکه به‌توافق‌کامل رسیدند. پاریسی ها 50 میلیون یورو به آبی اناری‌ها خواهند داد و این‌انتقال‌نهایی خواهد شد. کار دیگه تموم شده‌ست تورس پاریسی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27556" target="_blank">📅 00:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27555">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtAJjzrTW5IHQOghLKLhZlIOJMENNQKT8KxeCCJFSyn415ic5y5VNmma07Xp4HZHy078TNjT41ZpV-6R4dIeyxO2g2H0nx8cKNl_4gXG66_71mqEFtyoT3u1q1n2LcBV9ppzdfRh75UFCZfBr9VH2tQR9E6s8EobC5SW-osGLZiSdVsl7lbc6D-BtI9bHiZ5thD0uNeKO9LRFXYuMs9d6KkmAPShCLKZGJ9XzshR4XSems5rH9K4XKP_ns0MAbF6fCFuVtumaY17Dh3czerOLXDmroW3_ewORDDfhaD0cO6MxBIF3l8nBj0c_DgNCBCZVJsQXYrX2ju67LWz6b9hBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
درمصاحبه‌جدیدخانواده‌نیمار؛همسر نیمار از قلب بزرگ او گفت؛ ازکمک‌هایی‌که حتی دور از چشم همه برای اطرافیان و گاهی حتی غریبه‌ها انجام می‌دهد.
‼️
البته ستاره واقعی این مصاحبه شیرین، شیطنت‌ های بامزه دخترکوچولوی فوق ستاره سابق بارسلونا بود که تمام مدت توجه‌ها…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27555" target="_blank">📅 00:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27554">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHv6DcR2MZ9ilfMvizuUMtC7e-DD5mPa9AKYUGdWVuIJOL4g6iLe-8FI2OsRoEwzbEg1JIsKzvkgmg2dB6v048_U4P1Ds4_xfeW32U-98o2qRO15osYo8PG41Mc7UrfXA5HH2pHhrjmj3AR476f6OhSriqYTLb6Czd1W1AW5SM9955UJGzDXSiJsSab4jLEUsntA9TIkVwUKFLi4zay0oSxhiW0f2uBF7BfD1a6Dx0eNSMO0cw4R5PCP0UFRMjbLq7PVHawYxQlB09UQeh0gRGNKtUAPnPVg3P_ulXLQf5Xww--B4g75rEcOOcaWrU43naBHeTHkxJ_7rW2bwHMoEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27554" target="_blank">📅 00:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27553">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BC8LGFRFLT25K4kWe9-dNO8a8HqqfJvzTsCWwCzQAgC1PnJaYhZuriyF8-0PhwYVm9_wAnEad6wmmF0kxp__RVFuEBBoxKNNC_y5pYyMf7wtKGIjIKMighjlUMuFB7lr2tP70Gm_cIThvYDVU6hWtoNXWZCjBzwjsGAW3NXEL5RrEtCUXf1UfXX08LGGKkiRNTu9O1JXBT_G8pZla1zoe7p9PshObsws5Km5C8pid_KrNdn0tndybBOcRPSjGNGWnoixs8T7HsKJ_tm_jHIXIqs11GOtBniMOxxNvRPkfyeUkWw2D4CuLRjyhdJOH98Nerpy_X3Aa9ye12L8xmcw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو اسطوره‌پرتغالی‌جهان با انتشار این پست خبر از ازدواج رسمی‌اش با جورجینا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27553" target="_blank">📅 23:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27552">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇹
🇧🇷
ویدیویی از عملکرد فوق العاده دیدنی و برگ ریزون رونالدینیو شاعرفوتبال‌جهان در فصل 2009
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27552" target="_blank">📅 23:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27551">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAZbD2ekPGCp6pum-16b0TQ0zy04C-b0QsHlbQUTo8qZYJc_U_2gJ7BRBQW7d7OowO_ngGRTT8_aHwub_L1_wEBl_8R-TLINNm8_yn8dOqhJZSPj8-dh12GPtoV9wv4-yMSW4Tv4ps1cEzT9DfROezpfYXJnDnWNoCiueiIGZDzjkNrs5jQ3ge_c48M6Vm_0TJuZkUOsBP10oHAwm1q_57rz3O1YaVGhIJ5u7aXnoUvxLDl7TgzX0kL5CvrHu1juuQ7cVlJlEooBF07u6zOvZFFTpvZYrMUL4RP60ul7KnjwoazzZVfwMTAAgATTbR37swxpFkGKpBkyb3_SEtPvEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27551" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27550">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3Z7j4FhQSFdJOXtXAWwjpviYQX1Bs_DsE3g30yu3nGUgZ9Z7025PAkkKmDTYJYrsX5DO7KjT_GnklK96kUqktkpmsC7jX2n9ASRQeTSpOAvl24hNN0cRcXE2mW83Gk8qRoyF7hKdWraM9_q2WpQOqOXRRBTEZGoOg5NoZ8W0tqCJ8hwUJOWKODIY4e-HkYRNkAHj5qW0OsjXLE74bHl1VCzKUvuwr2ZdkdREEpTdEq8qht_CdW4HgMrGwY0TZFydVjOLLvCc-mNxPSpaHqETR-S_QMiaiuOka_xYQXUDcacLT7ddWLuLB0Ad0l1NRzm-Yq5wTx2i6iP0hm_767evw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا: به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش…</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27550" target="_blank">📅 22:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27549">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsG59KFl8oEZOZJIKM18-L9RYcDbHEdK0E6aQ3Jr_TeLDJuVtE2PD8yG2GThor9pTBGfuvh4fv6XJyNrBa3ekr5azR9zhGAU0Jq2cpdVBBPmcmkh1tBo9C1eNzxNy3xekARN6kitSVSL6P-6tSV9s47bHdueB5v1JLEi_QSfw2A35G6afcE3CutjCdHtiReLWfgCoPwEKMJNMFEfaFML0arCG-3gMQ_wYAMWhpK6ZGvDnaDRwclgxQz2hUEb6ZRybCG-C18Wbimz-DCuZ6fVNW45ereDshk8AMdW1WcJjsl05FnAIaA1_4PKRgYdrtORUoXXxFLavg9xF5Ld5DXd_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27549" target="_blank">📅 22:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27548">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4G3z5BHpC9Ifr3-Aeuo_S9sLzHgqVjim9DdygNh5wvOwNdzpmIMzAlJuBI10bLLwW5qv8NRSELbf5RAyp4zsHtptPCGOG4qwsoI2k41bBLxmY7240T9Nw0s3rP8YffV_dQvfcOdvkPL48Hf5HiDyKA6Q08idkFPyAZ3xcnA6j_QiszJGxQ3nlMZQjHVBoFY10kMBINUxc9XDa8fsASy2yyGThlPoftTyNCUinWIcLvnjZdY9pam8i0oOJjHawP-FRsktWppmL1rEg-jO4NTwbzYXowJFyr--zIPA3iYZD_vliyMSbwUDxXIKE7vHJrkz66d40aHIIBcMSbgGC8h8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام‌باشگاه‌پرسپولیس؛ سرژ اوریه مدافع‌راست ساحل‌عاجی بعداز توافق مالی با مدیران این باشگاه رسما از جمع سرخپوشان جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27548" target="_blank">📅 22:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27547">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2udjgj2H0xwwB4QHG-zOb11KbS7Iiy5adgmETVfuEVVfdewzYdmG_Bf66lKNhBzcYXvnBSI3MYqdzJUkJOpara6s2zRFNEYcCIJotBnavYgw5ysF2FlpgQBmX56EEsMMPksZRy5SpV4P6zqkUOqy0_gxJ11Qjms6LtP6chaNazs6_Cn63IFkcaA2KZtsDSEltqWp-bU7_enTKepBgNmiXauB1lqaBApVhydp6C_biD3DFQyEUVgidnePb_bUf89iEkZ_pfiCmlrkltTV3fg31aZKHnuk_ZF0-hUm4bSQbKQeHLs5Fegkd_ItAFDFef0kEDbCaCEa3ElVBYw3inEKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
پاختاکور درپلی‌آف‌لیگ‌نخبگان در شب گلزنی بشار سه بر 0 الحسین رو شکست داد و راهی مرحله گروهی لیگ نخبگان آسیا شد. این تیم اخیرا مرتضی پورعلی گنجی مدافع سابق پرسپولیس رو به خدمت گرفت و با این بازیکن در آسیا حضور خواهد داشت. پورعلی گنجی به بازی امشب پاختاکوری…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27547" target="_blank">📅 21:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27546">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGdro5-iURRH4nBaPe7ljUCTinDaDbwByQA2M2MoTQvQT71KWChDD7J-2bhPYENQSQEHBbEm0Eqs5ytFPBJig77tXmnmUp4FRJJDyZBLUMJ1VebMA1HI6Y6WmFFg3hZFHZjRDYZf_54PDohJBhxTMiS7C53fyOZ6ZTY30hXZ2J1ucHQe2yp35m3caDzL68c7s5rlPIS8D73eqatos786vwkLZ4Xces5-VF0sXTG9Sc8c0lKs8zCLTk3sfeZ1NVVXi0srKRiGFFFkFBhcjPYQ66vyJQth4Ja5YJDTOzy55zyxiXXe5YCRLS2oMdXapOwf9OntU8rOwHh9jlqgjeOIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ توافق‌نهایی بین دوباشگاه انجام شد؛ نیما اندرز مدافع راست20ساله تیم لگانس برای عقد قراردادی پنج ساله با باشگاه استقلال به توافق کامل رسید و نیم فصل به این تیم خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27546" target="_blank">📅 21:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27545">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4PE7r1WrwewpjwqZC6d0FLakOgYSWImANbpD0Pwna9eHHp6R76gmwVdpa3h0vVu5kgsXUIm5MCihUugaoyLjZ3OHhOCjrgeyKP0KCA83uqTd0D7jVLPfqkNTXAYpad67a23e4zyPws1YH0aWoA8VKCAFKLtwjvnW8wdTTAjI8_mCPfYtD5VIZ_7jf6QhlZ4DG1N7rkPdJz02ByFEoZ9RU0Kneq66YN6XBAq8ODIWGXsoKwRpccArZYs4-IYdGbdlxpeDYW6Q4LA63s1X0lGpZd9F7WWHPSWMcXfaL7th7XzEd-SyGxvZAH6YthlwsKyI0CUkiC-C-5AuwkhjrCN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزیکشنبه پیش رو یک جلسه مهم در ساختمان فدراسیون‌بین‌هیات‌رئیسه فدراسیون فوتبال برگزار خواهد شد و اعضای هیات رئیسه برای اهدای جام قهرمانی به استقلال رای گیری خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27545" target="_blank">📅 21:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27544">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jal0JWMFcAU4KmrMOVIH8FmUNEdjq6NVpFyvRk1MjRsj3Ju51T2-f8K19fUkru77yZGRGtIt5pPS73GchVM1BFDVP6QNWk8KvGQWO-Y8LaP0uJRyMAQLht9-D6sdK-_7jA7bn9gJFuDamL_taMMMmjbEFSXY1tsi3OMHT6RYZ_WzlRmtg41BfqHBJdaXJqIKShj8zFmNG74mQT0TscHNRykVZ_fsGOHrJLZXu8sVkKD_cs7-4EyWQityu7_m-OW5eaF4tda0fteagRy3HKru9T8lTFzdvBN3_TG92J-5He0h3cuWJbORbLK62Wj97lP8jO-p_6iFE77rGgsVMTNfdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
بازگشت‌دوباره‌پُل‌پوگبا به‌فوتبال پس‌از ۲۶ ماه دوری! در شب شکست ۴-۱ موناکو مقابل رن، پل پوگبا از دقیقه ۸۵وارد زمین‌شد.  پل پوگبا بلافاصله بعداز سوت پایان مسابقه سجده شکر به‌جا آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27544" target="_blank">📅 21:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27543">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8xb45l2IkNZsB2rjmgARdVjmaZg6bmWHJjEHQxNjKOWpUOBRxyNvilfzAxUcAOlVXkAUJa0vgq9c1k_7fhJ5MaeNtK3AuETG-ARg1TGlO6voMY4j7IMr690G4691TX0xr6clpLAWW5qNxW558bcjq57b6Y4jO4Y7FvfmrkQtSQ3b3HLdTyeihYCRUWe-NCc97ZeaAu_MShBuwVgvvHrOFuuroDmrGn-44fhvoN0EX3detojAjv0dsNs_yuWpGEzwPkZ--garq7SFS5tZmLhF3Nha_vWAR9yOoFk_nEBVk0vVSntm2XjddFnj6Mqa6PjaCMWz7hfmsODGF9liGveXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مرتضی پورعلی‌گنجی مدافع 34 ساله سابق پرسپولیس با عقد قراردادی یک ساله به ارزش 600 هزار دلار به باشگاه پاختاکور ازبکستان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27543" target="_blank">📅 20:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27542">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
#تکمیلی؛ 7 گل فوق العاده تماشایی در مستطیل سبز روی ضربات‌کات‌دار و ماهرانه ستاره‌های فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27542" target="_blank">📅 20:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27541">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_JV_cRWB0svxSHoyFetCOy6NQ0-Zawdw6mFrtQ-KvJFqBxtFbO8v8OfqnUKOYu-bPCaIKZ9s-yRuYwxbff-idq3R-36uclFpmiwElqjjWpcz8wcawhGlABek_JUXlA0nthfC0ozk4AQLzvXnjBuVniZqbyz854c_ZxX6U11FDPZE0jmpwhh4iNbTbG6fAomX35bHx9CFmlQ8eyLuZ_3ngq8UeXLMzWCyG3upAyFa04AvWlw2RRKgY4dpfBslzS_PTtXX2aCCL_c9GmS_8c8d05LIP53ffnaGdHwlcR5C671Gu2ZGmZa1BSGvoLSxl4AJrNfmieEDu9xCCnAyqnXKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال تخفیف است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27541" target="_blank">📅 19:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27540">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSnr5wbnNHRoz84EoIBkkhSfz866Pj0EBjWJpYAuLev7jeHTLGoSkmK50A6pHUKVtfdZWeJd2N_ue1-dyd3lxVCebuIcpRvA7bw4uiimeZAXcybGSWYaClfhOy3ySCQx2eUZB0IUZxyzy79OURuS8kqdZg3RzpxkAkGUuCsqaQDuQwtbNaCNWHOmP7cWsuBg63T20DsvrR5m9REiVtvzKYhQCf2M9JwEpnCJUqHDBAeZot-lTHwFoB-FpH60hQnHgCo8IP2R4L4MZPEW2IiXj6jmr1plShGp5ZyduUXxsmMfAeP7EvsvkisztmptGWOaMUDPDviC_bhDSe5l3GsorA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27540" target="_blank">📅 19:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27539">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk7RQvXFZnS3Z_FJHixfLs-O9kwn50t8AT9bh9pwmGXSKn-MccwzTWGYLa5g3f0_XVx4kavjtZXEk3VHLBGt9Bf_alc9lv4neKDDBy2JBZZI3MrvqjeIxrKZfZ6CBiqsXbrYUzguhv0sUXaAUUtMnaTQYceZwKUNIsRB-6bF7hkl-yCmfRWRqQBpTiii9W3i0Ptw-vPT-CU6IW9Lc9mhoXwSobG_q-Y0ewWSt6GzL1qlJFXUR4fz3cnWe1HQsl4-cj4tp3TOWe2iQur5fvTC8SH4HA3m8e8QHvcjBNt_g1Gz5udFC9nsLKuyOISRHqDevzGM5fvfm_UmSNuzeWaOQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخبار دریافتی‌رسانه پرشیانا؛ بانک شهر بودجه‌لازم رو برای پرداخت رضایت نامه دانیال ایری دراختیارمدیریت باشگاه پرسپولیس گذاشته و انتطار میرود ظرف 72 ساعت‌آینده این انتقال انجام شود و ایری با قراردادی چهار ساله رسما پرسپولیسی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27539" target="_blank">📅 19:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27538">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jV4vewRJAzaJSgO0gXGuXzDdPgAolYAze3vz8hgmwU6U5MU3bMdwcD_UFoAV2D3VjlR8wbFklZ1WznLqx35ZLhfIh6Bffa2QBFxdAPltx5dZ9nilUmhQfhgmRHBpYifbLzWuX2K0PIzYPAZ8fGZIR0BI6ruSBdverORwIW6quseyqZmNFmAeBl-2pgIo47Wu6_QZkyGA4dRRGUpTY5y4vuV2hBMbn4rnS9knhZEWaO8--sTQF3978CgBNAN1bfjSiYu_we853yBlZQy6XypsxkXBAi_9PJvSswvi0ZqODi4cpSFD0vJHgjy7IBPdYiIgjcJ1YikulBG7MyMq1ASnYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
سه‌روزتاشروع‌لیگ‌برتر
؛نگاهی‌ به‌ ترکیب احتمالی چهار باشگاه بزرگ ایران در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27538" target="_blank">📅 19:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27537">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F58c7SwGjsT7Y3kJovyUzLJVvq-UlJsh9_XhmRzDjv4r9VI4TzNxyfwCExq6UwA3vi63XW1aYIxVAl1os--ONMakqsNQHfdbAKkZHM4DL51LwIVe6OUDIa_IB3peFvf7oxkAQqOrni8YFjrwUjr9D8VaSGb3LA3RGcwhz5nFKyXujJscqZ8Nt-DroIc5cnsb0jKUbXxodvmAySrveffU4usHp8Q34b-x05OmeWa8MYPcFlObYlBJU0qrrXl71WeLGUCoTiIxwxsPwtuXGC8lKEd2ISm4rMsFSRHB4JlikG16xd67BmE1Yzw0_-mQ_mmSWWIRl9qq8yErjEbriqVsFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
آنتونیو گالیاردی مربی‌جوان‌ایتالیایی‌که چند هفته ای دستیار امیر قلعه نویی در تیم ایران بود به عنوان دستیار روبرتو مانچینی درتیم‌ملی‌ایتالیاانتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27537" target="_blank">📅 19:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27536">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ceb12a118.mp4?token=ShBHs4JuRkrbh3KAxXxr31rxObkoGrUtaDaUBgDHfzoIfM7dHERirkp0Atc-dJHacdgeOdh2CwMifQ1IdQD9ibB745nVaSA1dmePy5bAFxxw-8Iw2ZSyzwmtXlumY2jeLVxkaK8iKBurLin4hIHchFyqyRQvugLKohq5stpyYFJR5v5s81nczfVHwR7kGmb_Pvf-D023RHcbp1VXf0vx99CBTUK_0JVhFXx6SMSwOx0M48VX9Nl2RT_ejuF4HpRU-VtDzKsHugQn3ylo-96Jo0iz0LQ0UkMo2IIGUNHTKo3f-bz37EQd_nQFS8jiSAicIOJm4EayZnYwetpLlj5EdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ceb12a118.mp4?token=ShBHs4JuRkrbh3KAxXxr31rxObkoGrUtaDaUBgDHfzoIfM7dHERirkp0Atc-dJHacdgeOdh2CwMifQ1IdQD9ibB745nVaSA1dmePy5bAFxxw-8Iw2ZSyzwmtXlumY2jeLVxkaK8iKBurLin4hIHchFyqyRQvugLKohq5stpyYFJR5v5s81nczfVHwR7kGmb_Pvf-D023RHcbp1VXf0vx99CBTUK_0JVhFXx6SMSwOx0M48VX9Nl2RT_ejuF4HpRU-VtDzKsHugQn3ylo-96Jo0iz0LQ0UkMo2IIGUNHTKo3f-bz37EQd_nQFS8jiSAicIOJm4EayZnYwetpLlj5EdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جورجینا: به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27536" target="_blank">📅 19:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27534">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BghJKfOzHqlFxXczLWvxAhZzb-1mqjvz56ul-GZVM5WIgrMm84V0LJdP2PzB6uyCFkx8s2zSOMVw_2KD8B6WS_QZutenC73LIVFCo6JdzMXhcyvCNOSsSN0xrfzbG_zTbxK7jLSLgszpDrdkvtbiCOpd3OG8LdIjWi4hkIbb-zRaAwXlwajV4L8gUSq5ydoA4LpCKnIqaU3_NN0O-zq1Bb9vyIEB4g1H70Np3_15IspKoV68FiIlimLxEKTLFdMDD1u2qibXuB1wl3uIfL6qQ5CU2qTOT1zTIYeLwQY72TasplY4NewrSsFSmUNG9Po0JoYNS7A2G5rWz0TlBKkt2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#فوری؛مدیربرنامه‌های رامین‌رضاییان ستاره سابق پرسپولیس، استقلال و سپاهان برای قرار دادی یک ساله با فولاد خوزستان به توافق نهایی رسیده و اگر اتفاق خاصی رخ ندهد بزودی باشگاه فولاد از او رونمایی خواهدکرد. رقم قرارداد 65 میلیارد تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27534" target="_blank">📅 18:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27533">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwJU1KrG9vcnipdEiKUzl7GTs1gYyCAGUL5_loTvwOfA9oJwFw9itzP_whKQBy3ItC3TUbd9rL0nnf6a3SDxT7hIV8DLtSMvMtcfD8yymplebDw0MOGAQMu1x8mi2WpRP71f7R3DMBWhMY9z5D23WM8bA4d16GfRNJ1ZBE5JeBKNCjdPLYEJy_QK8VxFpAhQnmTJfLGHZblYdHKq3iET6xJ3Td0VQnK0PXyJpY2P3gsRZ0RRUyAeT9w2JrSlsFRoMYa0xNkE1lfOnIFkYLlObVbH0JS5SfVoCQIIW672EEv_vB5pt157yUM9EdiIFskiC4fVd8PF5MMQcJwlJPB1vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین‌رضاییان‌ستاره‌سابق‌سرخابی‌های پایتخت: ظرف 48 ساعت آینده از تیم جدیدم برای فصل آینده رسما رونمایی میکنم. در لیگ برتر ایران خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27533" target="_blank">📅 18:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27532">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmLFGE4vkQpBUijNWupI4tVt6QY7_pqeSAhzk5n7V5RvilYzdLuAYJzZF5uFd0M2ToWgHyurxD-nfSZmpTSPXnKHfsnxthoVwaw-8eP6xhNAb-CQ5szEeuzP9M6eeVgOxS2R6zp8UIwvo_oOl4gDfvFY0R3aGFduaTWkcMad4af6EIkZ2b8wvgX4e0tyzPsTBhcphuif890IqJ8KAZpa8w3L-GRWWJyft3yDKzFwwNqophIDmcv9pwYOCHYjDnowULD7zuQK4W9Pijq1E3uzg7n2ILtMMiRD7FBDOLEi789XRzfxjfI3KGhM1o8UTdhylcuDjUJiFOM9dRcuucZLrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا:
به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش گفتم، ازدست‌دادن کسی که دوستش داری میتونه آدم رو کاملاً نابود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27532" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27531">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇪🇸
🇵🇹
هفت گل تماشایی از روی ضربات ایستگاهی با هوش و زیرکی بازیکن کاشته زن رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27531" target="_blank">📅 17:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27530">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0n7DZkdO7huVUkpQhsbit9HFAzYpWvy3DBfxwh57bm9GDIruwbFwPNo8lSSFpZKVhwsV23mbFzpA-zg3XqmuhuM23jGJmtMp8S9tKHy7P-xMDKMQEbFTbwN7F2gy2bYVlb1NJFYwAnBQlzH4fU-ISCXjWqVFi9_8zLd3kbo1mbWAlV-jH3bqJjSGkd7YfRi_ad3ceiEMkCA4ztKCduGlK_h607IqZc0bWrNtL9ZFLRdl9zIoFUNQAtsCf7w7kcC-wDEHtFTy5m2ANvxPF4MmjXtoAZwA9WBiO7j1q0kcexP1UHZNrmlU87ha-f0LrJecgb1z9l9rftFlGj9egmTtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ سعید واسعی برای عقد قراردادی یک ساله با سپاهان به‌توافق‌نهایی‌رسید و اگر اتفاق خاصی رخ ندهد فردا قراردادش رو باطلایی‌پوشان‌امضا خواهد شد. ارزش قرارداد واسعی در سپاهان 10 میلیارد تومان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27530" target="_blank">📅 17:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27529">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4NUN2btSvcAP0RmGDgWmrNPZCubOpbBX2Gv6Kg8hHC0-hTOsmCPep0YhrUZy15AR3TWjwWbp-OGEAZx45jMTK5CrwMusOAilrLhq6_aRolKeRaODgEcQe_0QwBU1g01-A1dQcDA3qcmvqg_psrJqlkzU8Kv01tpMrqjoDmbk-p3-Jbt47rVsto-WdvXYCziIuMlPWKlm_J0idd75qIwqdZeX24yweFiqfsscXYeLqSv6mg6jbl-smLEbLRn77sbrm53qY5PQu6yTBQj7NmRPiPx9T6FTowA7RZZZ0G4Ow5CLDo1sFKmn8JftAxPuJKMUW5mCyc2aL5UYapMBH-K1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛ یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/27529" target="_blank">📅 17:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27528">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMfmnsHkqGgQI3W26Fjjjbpy5AkFof6XSNDjuBef8HYKGBzoq2J2er4LZkBC79vlxz4x85DhRtvIRzpZ2ZkKVe0csG5t23v66jXlcOYF19uLHGPIUznfpTeVYsxUuTAeXvti3z04sCgnU4XSb9PK3E7-dbdIS0scHAXICER7w6YVQlLnnRweqECkY6GApmIb1B7ubMC-BPZk63jQCR7WYqg9e0tPIGyt7spdLEI4pYupaC87bvlWWAp8TPo1BziCzkGSKN_NlpR0CQJ2RTFPVUPLfO3bQLBPgJeFuPY2mMqYokFq0uggRMvMGLmatauAVwy2LAI7nYD_3OHbL1VRrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🔵
بیانیه حسین زاده رییس هیات مدیره هلدینگ خلیج‌فارس خطاب‌به‌هوادران استقلال: استقلال تحت حمایت کامل مالی هلدینگ خلیج فارسه. در نیم فصل و با باز شدن پنجره قطعا تیم رو تقویت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/27528" target="_blank">📅 17:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27527">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxvXvrKzVSItLlPxU_cIPGG4HZaVBiYVKGkHJlc8cy2z1ytjICnD1LQNE6wXWNkY-BUDbmIeUIAaxhd8Abt7u9uPYciixMrJOyUQE1pyGLPMW3eZNYOCwZfHvUBal_mjyYSpT3xaPISpm-aKqxeud8NBY7c_ZjiS8XBGcBDd02VGOjV-pkSSRBsWXNOkYff-2gL8NyxCQ_KnoAK66Z2RVxsXNey4YmkpD1EbFYW0hPT8cNO_D7dm8B5f7T_AyYB3XvpYeItCniyvweHCnRLXpOJULEVfiu5pKuH_EKWB0YurlDodmaQsKe1npy_P20JYhEe4JZE1r9b_7FIggvD4eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌های انجام شده مشخص شد؛
باشگاه‌جنوا ایتالیا باارسال‌آفری 1.2 میلیون یورویی خواستار جذب آریا یوسفی ستاره 24 ساله سپاهان شده و این آفر روی میز مدیران این باشگاه است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27527" target="_blank">📅 17:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27526">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-QryhAgCd_kFl_DqUHiAYxrFqYZ-rN9k4rzRPPMtHER4UvIh_x41ccvdm7cY4QkYIzvMUOCKJHs4fv-KZyRutjz04_jx8z1FVoMwtGSbXLzposhdHWdHJNLQMm-FRufKaUHoZSSi2QYEDTjP8D-1Ii8zyisvuwdf8h6ewCmcrzxyt9FzqzLzX-4pQ7ea7XBuiggHC1ccxdxUlN8n8s68RL7lsNqa5SuKmnDYWZxBF5DgW7_Q0szMTyca3kJ_nghPepQR8wLojEtaBTsU16veeaCZAnqIA_meeu1mWHZ9BkMPXDKxfsyahREhlBY4i4NeujKCRZD-qTd0CWzH7tbUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇪
#تکمیلی؛روملو لوکاکو مهاجم 33 ساله سابق منچستریونایتد و اینترمیلان با عقدقراردادی دو ساله‌ به‌ارزش‌هفت میلیون یورو به فنرباغچه ترکیه پیوست و شاگرد اسماعیل کارتال دراین تیم شد. کارتال دست گذاشته رو هر بازیکنی مدیریت فنرباغچه نه نگفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27526" target="_blank">📅 16:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27525">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2d2f027.mp4?token=mtpuM9mys81afNetngv9ZRIyLr9EYOMpcAtGzhwrPFSzvLi2-Glg1yAmk6dD1Bwzf4FpmOfupx1M1fRHY9iLIE_6efAjW7EGbxeEaDFYCfIj7_xtYfOiayHBCtLQ4GU8yhAHakFGBN3DZEuQyxF296QIENp8RwOn8eh33OezSJ9ythdgGhrmtRlPIjfIEkDATsKOGs3-alAKPf9GTgd3TRs8M_YXH6Xz5q2OzPqK2tiwIo01cmyXVDnhWKAQH_tkKAMimp9Q7-7qirwP4N6BkJuGLTTCZNNLVS6fEp4cpxP6zHDXratif3mZ1CwfBdHKdf1n4lrkyUW0-MCnp6KHBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2d2f027.mp4?token=mtpuM9mys81afNetngv9ZRIyLr9EYOMpcAtGzhwrPFSzvLi2-Glg1yAmk6dD1Bwzf4FpmOfupx1M1fRHY9iLIE_6efAjW7EGbxeEaDFYCfIj7_xtYfOiayHBCtLQ4GU8yhAHakFGBN3DZEuQyxF296QIENp8RwOn8eh33OezSJ9ythdgGhrmtRlPIjfIEkDATsKOGs3-alAKPf9GTgd3TRs8M_YXH6Xz5q2OzPqK2tiwIo01cmyXVDnhWKAQH_tkKAMimp9Q7-7qirwP4N6BkJuGLTTCZNNLVS6fEp4cpxP6zHDXratif3mZ1CwfBdHKdf1n4lrkyUW0-MCnp6KHBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دخترخانوم‌رضارشیدپور مجری‌سابق‌ برنامه حالا خورشید شبکه سه به این شکل که در ویدیو میبینید پدرش رو به مناسبت روز تولدش سورپرایز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27525" target="_blank">📅 16:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27524">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y66ZL3jsMkoOoRPozEpypXhOkWp4cSJeGGcfSuZ0A5jk0xDPwTxPwjxto-OSiwbnTn-XmGWHK9FydmBDuFidi1CLx7XFE_HOXk3D9YCARb6OgUEypbCSZpIFjGhv_hVCXpyvf8jnW0i5CtOAeGNVKkPwZWntnpYzpB0N_iYL7ie6N_0Rlbe2ZYwv3v1fpCyd5Y9CsLSEtERH-AT6BDwDE1X3c2hgmP-GAeutZu6ymyR1HYYXxM8iiYbY0GWbTcnY2ekJ1HXrTx3SsKJYDw7hOjx6u_1aSsLP7NpugwYLwy3jTuZuV4kt7yrApD0DC9HQBH4VyyM-rLlr1DbrnvGAYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27524" target="_blank">📅 15:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27523">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‼️
بااختلاف‌بهترین‌ویدیووترولی‌که‌میتونیداز دعوای علی دایی و کاشانی تو برنامه نود ببینید؛ شاهکاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27523" target="_blank">📅 15:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27522">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gE2XTcr4Th3qM2WDtWs7J-M1crguWiPrGAMX2SSnHLm7eEoPtKI8P8Mbbu0qCpTNRTjvEHvEuzUWHbn-4nsm9zHHiCX-B1u9Apqlfn0qzK8yYjzfZ52HbkJSum_dVbPjg9X8cVOzw7s2DQpD6L57fDAQZw227Wt63Tca_8sLekotpzpVakndZQv_v8aLfA1nSgzJbLrWdK7sRafAGjifbR8snr3bojFg8ltwQRe2yg0ICF9ZlbX_JVvwEZwmyORJnyJKTWOR2Gbv-EMZAoRiK1qm1hEpIyE5PUvRKhgXqflVXCCvD4bOQwmOhlMyeUcOuV4lIFCKU2JkU-6sTaXcCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
وینیسیوس جونیور بعد از 9 فصل حضور در تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27522" target="_blank">📅 15:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27521">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyy4AyREj-I44gmykHWMtjezkADd_qwZHJHMzwLByfxQ0OJiKLU8SKrf-ylGz0aevxWOA03llAplUFh2CzNCUxUlImDuW4vMap-SsApVxBFVp7cFiuM6k-abMvDPKIZ130sRYtChwVDQ275qoqzyC1NWy8H8cHlSdYqcJ3inu5cMtRTBnpbBBibCHmw_9dTFVgS1dwM1ge3ATQlE4UE4QEWX46rDiRNiybHhkdG_lF6lyxMmemt3DpVC061ZFxzGpAGO4n7JPWpwi9XIaSvxd6YSXU3uWjmsvroK66huHCgoe04pR8c_CeO5--tVNrnVsbxtyohyOQ9JOhBGvY5Qcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدازجلسه روزگذشته مهدی تارتار با مدیریت باشگاه‌پرسپولیس؛ سرمربی‌سرخ‌ها تیوی ییفوما رو از لیست‌مازاد این‌تیم خاج‌کرد اما روی جدایی دانیل گرا مدافع 33 ساله باشگاه پرسپولیس اصرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27521" target="_blank">📅 14:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27520">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hebq4R0kWidT_cHW2hVF7TBZND9afHNBGprloVh7XKOE35Q0TauLJ2CbFTG0I_6FQdtW_dRpnKhJpoBrykxC0seZlWDIKCDEcnRXJBHniyUC-WqVgf25zFRpE5D_miECDMdBG-NEpWEIBBM4WhYobWuvvXKerXgyF-1QMYac3tgcgMmb-3Dkk8HXKSMBdIxUBy1N69Wkhu42m3wxX-xxs6My1XcRJNao-1Q3WGkDK0itDgF2PvzlYkOa-TZPZmzb88WXcjg8zAsPlXL5utYgh1ckUp3FxL3la9gl7D4-eF2FBcntS6dZ7BOU7CPBTJuTtn9mPxToJb3hWsZBzgzgTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال تنها 10 روز فرصت داره تا طلب پنجاه هزار دلاری زیلیکیچ وینگر سابق خود که یک دقیقه هم برای آبی‌‌ها بازی نکرد و احمد شهریاری اون رو به استقلال اورد پرداخت‌کنه درغیر اینصورت آبی‌ها از چهار پنجره پیش‌رو نیز محروم خواهند کرد. پرونده های ساپینتو،…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27520" target="_blank">📅 14:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27519">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a376b4a33f.mp4?token=EFGX9uTNbtkvxsvtPc_34t6cz1-pkoJQAgGkSNPcJLia9CWbdUjAn15ZyxaKel8BS7zwjBVKWGLURfwq2BFJ0u4kiz98v3M2tCls6Cqa5l8MkmODNVn86njCiu1fqTIVA_3xa3EkSv7i0IidTFHzzACMieao0e_fNgwNoLybsfhFJzdIBjtUgU3ezA2bArmgIaQgTTszdNCUR7lcXeBHil_cnzYVY-zJan3DoiG6NNLdeM5BR7WLVh7GCC1fgqfH3-GkHrxVXfayrQ7E5r3uQE__n_mX8bN730cCwCLIe8cMQhEX7APlzs3imGtM0fzTgvrBom_wwqr4k3VK0pGBkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a376b4a33f.mp4?token=EFGX9uTNbtkvxsvtPc_34t6cz1-pkoJQAgGkSNPcJLia9CWbdUjAn15ZyxaKel8BS7zwjBVKWGLURfwq2BFJ0u4kiz98v3M2tCls6Cqa5l8MkmODNVn86njCiu1fqTIVA_3xa3EkSv7i0IidTFHzzACMieao0e_fNgwNoLybsfhFJzdIBjtUgU3ezA2bArmgIaQgTTszdNCUR7lcXeBHil_cnzYVY-zJan3DoiG6NNLdeM5BR7WLVh7GCC1fgqfH3-GkHrxVXfayrQ7E5r3uQE__n_mX8bN730cCwCLIe8cMQhEX7APlzs3imGtM0fzTgvrBom_wwqr4k3VK0pGBkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇵🇹
ژوزه‌مورینیو سرمربی تیم رئال مادرید:
هر کاپیتانی نمیتونه‌رهبرتیم باشه. رهبر تیم رو نه میشه خرید نه میشه ساخت، اگه یکی از این بازیکنان توی تیمتون باشه، همیشه یه گام از حریف جلو ترید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27519" target="_blank">📅 14:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27518">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tm9UvKNuHhJtejGzL4Y19lkqtf_qqouWxgNOHih_Kd4UzZDK2w1n8Z5W_JsU3L4k2k_dqSKIPLkDGV_bc4pCNUb4NGcfO3EWrXbxSlP-UMlV18EhzER6BHT82HwmzTRyEpHM64YhLppOb7KrZcDtWBLsPDWpQGWi51fIHGYjolKO9RI6KrrzkYL9XqTecJm8VJKeXlmMhsiUjOfRfA2g_SHdwfhCgL3wJXR-XmbaauQ2ThkmZHU7ua7FdKwsBgGCWykHiPcIn1xZG61zW13qE9Ckpe0DM2ekDdGNd8J4vBoynEWuq6p8r-Y3NOV7mzv7otVaTst8w2yexy4uYzsMHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین‌رضاییان‌ستاره‌سابق‌سرخابی‌های پایتخت: ظرف 48 ساعت آینده از تیم جدیدم برای فصل آینده رسما رونمایی میکنم. در لیگ برتر ایران خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27518" target="_blank">📅 13:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27517">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnSG63PVk44d9XwWRoQzx8tVEK4Em2z5swdgKc7PGsyj4TNPiZB0iEh7uwR9aMH21FK5Wfn7pgAp-Icc3_tg7WJIhXjOmS0wiQavSDnvEeYZfmgr6UShPB00_iaDKnBBQFPX9nOAnW-Kcpo0oPqr7xMjiFr770HvVCiJcymbG_F1IN9QS5xjsY7jM7X07dj4LXBvNpKvey05gk_WNFIE0UJM8XHLev7C9MUDCBilZvOE6hoDDFhIPZ5aPrja34zg4ANUTT6OW_iJnUdg6EcB1JEPAnGHhn16mnnsJjasR2IikZ_ILNMieC_mSzFpVo10YNGIRZF8232x-c95wup3OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
مورد جالب دروازه‌بان سامورائی‌ها؛ سوزوکی دروازه‌بان تیم‌ملی‌ژاپن‌پدربزرگش نیجریه‌ایه، پدرش غناییه، مادرش کلمبیاییه، تو آمریکا متولد شده، تو پارمای ایتالیا بازی میکنه، تیم ملیش هم ژاپن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27517" target="_blank">📅 12:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27516">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇪🇸
🇵🇹
هفت گل تماشایی از روی ضربات ایستگاهی با هوش و زیرکی بازیکن کاشته زن رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27516" target="_blank">📅 12:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27515">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ag2VFeQEkrLJ1jix85fp3Ozt08XodkdmqS6E8HDiz1bczpgs6p-N1Jm8J18Kq_hNMFSE_GDx3fLK7ha8zcfcY9GinXcz5tscf0M5vaqzjIoPoQGUodQB4P2L59pHJQHH90EmlUbJCFDnw-eIPj3mQzpNeze9rOPKgNYu4aVHix22ew3uDQD0cOUt29ywLb1JRlRwDXnjUhJu3flZTX56zoiZX3L5n-OgHf7MS_HPTInf6zx2QvS_UTad1P3XgjwAfrOvR9HDFxlWdmS0WwHUVIMoKYSqYBNszUkwet5e1m3boyCedOvNsA8Fh8yF97R6G09izq0u1RFvIS9C5zl_MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🇧🇪
باشگاه‌‌فنرباغچه که سرمربی‌آن اسماعیل کارتال سرمربی‌سابق پرسپولیسه برای عقد قراردادی سه ساله با روملو لوکاکو به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27515" target="_blank">📅 12:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27514">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTVsIiOWKlGO0V6II1KIALfbH9GGzMI3jaEZWHSNnIkUiyUV2yizml3s4S0r-wDyj76F2R0jaDM7pnpHjupQb-iUAJKAc2SKUUQ9c5xb386c9Uicz36pRNCrQ1EIrWfgrwZTCpKR0eJ4Wz1hAwWmuft-ObghHE3XEY8FLdBsUPU_nhfPKUd2zPBNl3yyfI1F7g-onJusEDHGmCOwBEejRgFtKd4EBf62IOTKZmg5yfg5wmEisFacoe-3B1Vi4aB-Lep9sNNsQDi-WL9Oj0Z_1bz-VRPv9wmswLRY_cU1SuyCuFN2aX5ymt22u3ZZA0qHeY_frfpRT3_S1ZPuvzYKqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
سانتی آئونا: باشگاه‌پاری‌سن ژرمن و بارسلونا برسر انتقال فران تورس به‌جمع شاگردان لوئیز انریکه به‌توافق‌کامل رسیدند. پاریسی ها 50 میلیون یورو به آبی اناری‌ها خواهند داد و این‌انتقال‌نهایی خواهد شد. کار دیگه تموم شده‌ست تورس پاریسی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27514" target="_blank">📅 12:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27513">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQLDf7_6A9cCiNXimXIeJG_2eArQ2oTSOoj2k5YmtfRo-noLcxsqUHh3nf76_iYuN0upCM68PCrDUgNeqk01oX-Ah5hcmKa9vf9c8wj0PLuiWW5DET3xShzShg7nvj8qA_2Noydv1WrE4dFae-InTShBYCGf-jhh3C72w6K3dNSSqMLnSYGWgfD0itEEXUQRHd6bkUZkCfYww-APqiZsyga3of05LzzOvGSv_TLrcNwkZbxnw42H3ZfE_qmAL6JYjSFzyaShehCSSNSIW1xnXg4Nct_L6iwOBSCdtsTpQup9VtWn5LYBxYHe91MM6Ai3u60uNBRqVWF4TmesTDdv8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
باشگاه المپیاکوس ظرف 48 ساعت آینده با مهدی‌طارمی و مدیربرنامه‌هاش جلسه‌ای مهم برگزار خواهد کرد تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27513" target="_blank">📅 11:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27512">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOwPRXXgWm56CJh3XQ1zKfHNdPMRJVdKil_vZ_22Vw5Qcz9Omwr87IGlNwQc_ts4L0k2eCuuSHwq4W3epLs_9xAKZTLWxujnVatKv88AwKh2eFvsTZwmwJTy-2WU4ZQqRUnlWSe2XVLoCJO7RHVX8285pC-lY99kNSxEzJm6T57vM6Byc2upJrtKTAPvtLUOtuXPUWFUQ7nmPtrFlE2RFYx0Qj39o6kFdF_Y1r35fHFsW-vpar0usz_SiXh_opFiXEE68kKbXHSr2GZmLRb1C99qWFsPamrvfLRScYEgkryzOt575Z8UZRiFIkIgQTspsX3Kxa5QIUzO0AsCNwLyOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
رامین رضاییان فوق‌ستاره‌فوتبال‌ایران امشب ابتدا به‌این‌شکل‌وارد برنامه فوتبال‌برتر شد که یکی از دکمه‌‌‌های پیراهن بازبود که با تذکر عجیب اتاق فرمان مجبور به‌بسته‌شدن دکمه پیراهن شد. داشتیم تحریک میشدیم که خیلی سریع دگمه لباس رامین رو بستن:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27512" target="_blank">📅 11:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27511">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb87b4574.mp4?token=nXbZJl_5OfIhIuwkT9pOeGG6WNtTTJDOMzMO8AvggcNs51lP-zx-1vZ3Z7arCma80JmfQazruylzE6uKeCcXiQJZFIjNcVC48_t2K9_nkCG_nGR7EICk_gOTj1h9aoTxuzG9iiyPijH3lrVOOFuK0Csr0xtNlNiAjhvEhfA3zUX7f8bfIUEeaTP4xXurvB5U2GLeTLm_0mdJWkIdpsz6qixW0mSd4y2ouDeJeJENA2_TuCsiSrbuTrtak3Niie9r5JR_OAieqZJmQO-sUVvHjP6oyrwLrAskou76Og-DVIcE7xMrWqJ8lNn15l62yIxBtcT9eyh_Bo1dQqnQo44E57THIimzIIx4Sbqo8ELIau5Q5wV8oNlyBr4Lp8YVmJr_k8xoWpNM0z0-9ScYjlmj1s1uE5dWG3CIH6VNfFj2MjrpdVuqwRmN2yQRWi1ie09zC-EPp08WoBiMZuFc_hktpx7QCxjntZXp5qrnDStj_g-8gJ36yKnRSEfscrmqCvgzrs8g8MRtYbXJpi5IcCnTks4tG67m-A7-ok2cLQWKut7Z7k2dCUp-ig3pfaljgHigxLhI04pB4YsAOC2Bs9n0vewydICFFVs_fdIVlvo85ot-DbqHrKb9WCs8izIsKVroioi7-bRHfZlAHUQErbDUfYrvYBgYBXjeBGFDwhiNsGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb87b4574.mp4?token=nXbZJl_5OfIhIuwkT9pOeGG6WNtTTJDOMzMO8AvggcNs51lP-zx-1vZ3Z7arCma80JmfQazruylzE6uKeCcXiQJZFIjNcVC48_t2K9_nkCG_nGR7EICk_gOTj1h9aoTxuzG9iiyPijH3lrVOOFuK0Csr0xtNlNiAjhvEhfA3zUX7f8bfIUEeaTP4xXurvB5U2GLeTLm_0mdJWkIdpsz6qixW0mSd4y2ouDeJeJENA2_TuCsiSrbuTrtak3Niie9r5JR_OAieqZJmQO-sUVvHjP6oyrwLrAskou76Og-DVIcE7xMrWqJ8lNn15l62yIxBtcT9eyh_Bo1dQqnQo44E57THIimzIIx4Sbqo8ELIau5Q5wV8oNlyBr4Lp8YVmJr_k8xoWpNM0z0-9ScYjlmj1s1uE5dWG3CIH6VNfFj2MjrpdVuqwRmN2yQRWi1ie09zC-EPp08WoBiMZuFc_hktpx7QCxjntZXp5qrnDStj_g-8gJ36yKnRSEfscrmqCvgzrs8g8MRtYbXJpi5IcCnTks4tG67m-A7-ok2cLQWKut7Z7k2dCUp-ig3pfaljgHigxLhI04pB4YsAOC2Bs9n0vewydICFFVs_fdIVlvo85ot-DbqHrKb9WCs8izIsKVroioi7-bRHfZlAHUQErbDUfYrvYBgYBXjeBGFDwhiNsGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇦🇷
5 سال‌پیش درچنین‌روزی؛ لیونل مسی فوق ستاره آرژانتینی درانتقالی‌آزاد و با قراردادی دو ساله ازبارسلونا به پاریسن‌ژرمن پیوست. عملکرد لئو مسی درپاریسن‌ژرمن: 75 بازی، 32 گل‌زده و 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27511" target="_blank">📅 11:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27509">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMNym43Q9_HjpZS9z_fwAwgrW8OokBcrEscnyyMUnPPsx18B_5zIpK4MAwxlXy58pd-tvC9dVIdf4f0tJj0UGp2vib7eBgU3skmMqCWAv3o4TTZXfWw4G1xauMgSRHwKg4PlQ6Lx1yCgw_YhJJuQhyskx1Ba5rjwgYelPUeNL-BJXHRNiC6i2hE3vYq2vRpHMKtB5Vl_rNmOOA_ov2DI_dYsJfbIMCHHilBSvfoBAkzxxoDXZJYPJt83GIdbgFlyWbiBSlGBEwMTQ2P7EXEMlsVei_38jI1KAjqn7tb5UgDlCJjtBQP2ZPex4LXtbAkZyg86aHGZIQXQrLQTJsbEcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی تا روزچهارشنبه به‌باشگاه پرسپولیس فرصت داده تا رقم رضایت‌نامه دانیال ایری رو پرداخت کند. درصورتی‌ که ظرف این 48 ساعت مبلغ 120 میلیارد تومان به حساب‌باشگاه‌نساجی واریز نشود این انتقال منتفی خواهدشد و این‌جابجایی…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27509" target="_blank">📅 10:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27508">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaGGgcW8ApWc77xPtMKnz4uGaJ7oVRNNfOfi2Ju5t5yaHJdhHmZ97TAeiMzqWxMeoixEoCRJK5ZiupqlWKpCCN_Hr2oDk3-uQYlZ6cYUVf1Y3172jJnO00oJAyJkqWuhvxjI1mzIwf7Ei8IvhLptmOhm04uo0oiultp3A5PylZScUs2OeljdWD3fw_LrJYh27E2SrbfY0HlT7tHUSLXEKcUf2IsQpdwZil_qinPeCt8tq8fH_mjn4PTglt9ZExeKtmTpVH5MVGznoVE8oxaHSUPAra87dNEuRkbG84NP9XAnlgi0My5Q1zOR0KN-YJMpB4VeTH0TWtIplpmZSje1WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یکی از مسئولان تیم نساجی: دلیل نهایی نشدن انتقال دانیال ایری به‌پرسپولیس‌کوتاهی مدیریت این باشگاه است. برای چندمین بار با ما تماس گرفتند و برای پرداخت رضایت‌نامه 120 میلیارد تومانی ایری اعلام امادگی کردند اما موقع پرداخت تعلل میکنند. بانک شهر و مدیریت‌باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27508" target="_blank">📅 10:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27507">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6296bc604.mp4?token=d1sbT0D9slRIZHwfQJHyGSgvgAK6Va0Cqc_OQ-edz1fDOdchvqUBO8FBdq7GZlz5xf0Wt4WX6y6mPDtdl8VvLCT_hLswDcfEk0isOdoJHwMZJk2rbTmzfGwp6skbRCBr8iHgOZDWpM0N_Kx7SP3oxS-Q0xScof4FSuJspy6Fq2oUd0P53CjJ9Eb1V-qXy5fqvn7oZurRYqOouqf1pmFPYAetvRPl37H14rHnwt7IHIVNJgGbhasjTcCcpDq2gawiGPmnAFZPW8IuA5uBexremDnry_zkBuO9sqD9FFVXavKXt_nUx0fg1ZP2S8G5c8IMyqKk7wVw8euKxoJgAX1IEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6296bc604.mp4?token=d1sbT0D9slRIZHwfQJHyGSgvgAK6Va0Cqc_OQ-edz1fDOdchvqUBO8FBdq7GZlz5xf0Wt4WX6y6mPDtdl8VvLCT_hLswDcfEk0isOdoJHwMZJk2rbTmzfGwp6skbRCBr8iHgOZDWpM0N_Kx7SP3oxS-Q0xScof4FSuJspy6Fq2oUd0P53CjJ9Eb1V-qXy5fqvn7oZurRYqOouqf1pmFPYAetvRPl37H14rHnwt7IHIVNJgGbhasjTcCcpDq2gawiGPmnAFZPW8IuA5uBexremDnry_zkBuO9sqD9FFVXavKXt_nUx0fg1ZP2S8G5c8IMyqKk7wVw8euKxoJgAX1IEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شماره تمام بازیکنان رئال مادرید در فصل جدید رقابت‌ها مشخص شد؛ دیومانده 25، اندریک 9.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27507" target="_blank">📅 10:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27506">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwNeTyJ_8_YxQzQam2-KRsbw52EKNHr8n6rEvYU1cOogRUYkXflG6bn3VyPoISuc6SgvHeUu7ACyrcHiWLRrSM_nldK-IMzq0o4Drf4Tvg4i43zXRJH49XbHiALOEP-iodCwhyPW4fawQuj3l9Z9Z2GLn4dH-9RVfnj3r8OiUKb7_li6LbXIkzdoWFAyBgPhxnXLZwjGWI_xEjrFkLdRwTLQKg9drAjUMXweZ-P9-rKfC23VdNohGYVMiewsXeeMhWnBgEFOemGEsw32ly1GUjr-FlFzvWe0DGxi8ZyAs5Fq-f5MBxsjDSL76qX9SkPdXkheiNsd7JYaZ74VmSDkoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام اسامی داوران هفته اول لیگ:
موعود داور دیدار استقلال شد. بیژن هم قاضی دیدار پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27506" target="_blank">📅 09:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27505">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgSX_6TnovM6vCtDAFCfse-US74j1OIhye-m1CMRYD4xmK5auCFPLezYpgiTBDZRTCPGqkV-UNotv2AaGo17tnR2SqLYnx6OvYo121Ua1F_j6yhp1ioboy21mZXv3VKEMLMOfeKhALakKOAS4Rk_kv2ofv5EAbhOnJ0ASH6nYosg_7Es5jwDziJMusPAIIMTBvRUMQLh195YLk2PLwb2JbgNP_YERvsMSNWA5hBM0uQNbj7gOCCjI7WAVDka50uSNDtzJOAKcBYMvFWGhEXglb_YSbVShfEPmlybG678Vlus0PgNIXqKQS8CTwO09iupLI0uGxjgyuqhvOQhhgsgzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
مهدی طارمی بازهم‌ازلیست المپیاکوس یونان خط خورد تا در آستانه جدایی از این تیم قرار بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27505" target="_blank">📅 09:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27504">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83568bad0c.mp4?token=f-H7It8QiJBsmh1nOVhKP9EVKYIlZ7we8sBjzf19aSE45OqUycKKtyOCcEzeVND72UGDuYfFysgb6rErOJYLMnumXtx8Z2qFFchWB5Fc8bAovYwc-NO8rlhqRy8YTDkMx_dea_sEfmApZijP9KM6mjskkrABTve2losH7o_9C52APPr6dlK0JOYVqqjK94pPWAF9Tr5M4YPydi9PEB4luZzGJRZXz_WZPcuh0bReU0vJhauyKUUPLkx2MKpZ5IzWGT9-TaPiSlE9Rjsib2MhseYiZHRFYV8lGMO5eHrzl1V-8y-d9QwVpC_qvQ0BlmpvkdP5S7KrJCxHPBBqvdT98g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83568bad0c.mp4?token=f-H7It8QiJBsmh1nOVhKP9EVKYIlZ7we8sBjzf19aSE45OqUycKKtyOCcEzeVND72UGDuYfFysgb6rErOJYLMnumXtx8Z2qFFchWB5Fc8bAovYwc-NO8rlhqRy8YTDkMx_dea_sEfmApZijP9KM6mjskkrABTve2losH7o_9C52APPr6dlK0JOYVqqjK94pPWAF9Tr5M4YPydi9PEB4luZzGJRZXz_WZPcuh0bReU0vJhauyKUUPLkx2MKpZ5IzWGT9-TaPiSlE9Rjsib2MhseYiZHRFYV8lGMO5eHrzl1V-8y-d9QwVpC_qvQ0BlmpvkdP5S7KrJCxHPBBqvdT98g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مقایسه‌درامدبرخی‌ازشغل‌هادرمملکت؛قلعه نویی یه‌زمانی حرف خوبی زد گفت 40 ساله هیچ عدالتی تو این مملکت نبوده از این به بعدم نخواهیم دید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27504" target="_blank">📅 02:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27503">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhVQbKHziuKEzXWI0K-mQiXwNAZHcW8F6Wb6WFi6SMFRaf4NzYa8avymjCmDny6alTsYvLB_PU-2KnsQ2XZp3aduPwRq9-yhYjixBhJ50TCAaUDZJi7AynzYGSdCe8vZYeXCB5gA9YzzLMIjfnraUW9OGiH8djKa-8LUIwv3uQdw2UskeKd5bVxKverKb-bhUzpzbyXMJ1aBqNh_1EzPGgEFp1tb6R_VS0xagBKzonxwBYZtLUei6ZsIPR186VWAsf8aIKBNcJdxID2iNlEwRCoZPboi7CVTbUr8E9aXrMLiM0DL2qSZvARX4SMM4f_CG1uxtfROeuwhZsLUnuoIWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
الکسیس سانچز ستاره شیلیایی سابق آرسنال و بارسلونا: من‌درجریان‌اعتراضات مردم ایران علیه حکومت کشورشون هستم. میخواهم به مردم ایران بگویم که جهان صدای شما رو شنیده است و قطعا پیروزی نهایی از آن مردم مظلوم ایران خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27503" target="_blank">📅 02:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27502">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea74d7e98.mp4?token=kPoO6CZ3sIf1ITa2QWKqbVBb0VYD5h7aN9pN37lpW51y_FV7xP0UYcCOXK43Rvv3V6sI0a0oUhHiUQTi0am4YNsXC4uDVhLRvLz9oD8z6Ii-BZlPno4cZTtiNY65JN0CViTsKyUutLpvIpNA4hbinl-bhkORmvjEzvGHrLJwF_sXyFnvQvga_Oaeam83-r6tCiom84ZGV5-vt0LMVxYwtZpGraMXh_hnmLwrwTMvI9OQsCNsJpT_jzdZMr9QtYWMOYYq96i3AX3C4WxdNI6iwgksEbrIKY4qm7WtE0FhzXH_l-NmY6LJQtVAU-qMsgegF8eAOvNXTEQBNBFEYqjc-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea74d7e98.mp4?token=kPoO6CZ3sIf1ITa2QWKqbVBb0VYD5h7aN9pN37lpW51y_FV7xP0UYcCOXK43Rvv3V6sI0a0oUhHiUQTi0am4YNsXC4uDVhLRvLz9oD8z6Ii-BZlPno4cZTtiNY65JN0CViTsKyUutLpvIpNA4hbinl-bhkORmvjEzvGHrLJwF_sXyFnvQvga_Oaeam83-r6tCiom84ZGV5-vt0LMVxYwtZpGraMXh_hnmLwrwTMvI9OQsCNsJpT_jzdZMr9QtYWMOYYq96i3AX3C4WxdNI6iwgksEbrIKY4qm7WtE0FhzXH_l-NmY6LJQtVAU-qMsgegF8eAOvNXTEQBNBFEYqjc-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلندشدن رامین‌رضاییان‌از روی‌صندلی روی آنتن زنده: بخدا منم‌فقروبدبختی رو یه روزی کشیدم. الانم نه ساعت دستم کردم نه گردنبند گردنمه. همه لباسامم ایرانیه و معمولیه. از مسئولین میخوام هوای مردم رو داشته باشند که با این فوتبال "تیم ملی" آشتی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27502" target="_blank">📅 02:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27501">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvbcvgJYXFsmN1QWZkdILlQqsN6Z8wS0oeuCoLwNIi3-O3mgaeERgcadeN7AiXesjqL5w2Pe-FTCrzcZhxG0hKEl45Gk2mJBv2mYuMU_F8IvIh1wZWLJzoH60RZIc-6qlswkb9SzJf0a3KycafveQNZuYEWY7_HFFwolmxV6TEKs4wff7HAkhyYr5jR07QQreUTQyCkN1jOKqnlLkj9eARdzg1cBUZ1UKys2oI73bWWAf7KkLH3Nqgxr8EAFUbBIPtIAw-sSE_IHp-GUGlHHtRSooSNtmPTdh9GrCP8_B8KbFLyNr_UilL9QDUS_P-va4dP-g9HJ8qFBK4XsN3oeyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
روزنامه AS: با صلاح دید ژوزه مورینیو اندریک مهاجم‌برزیلی رئال‌مادرید در این تیم موندنی شد و شماره9کهکشانی‌ها درفصل جدید برتن خواهد داشت. آلونسو بشدت علاقمند بود اندریک رو برای چلسی به خدمت بگیره که مورینیو مخالفت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27501" target="_blank">📅 02:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27500">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f41aa6e732.mp4?token=arddpJ_FTWHIAPvOM6y8U81reRLPCRkHLoBaoPDIao-OX4lj0q1QE3Bgzq337V-UU2RsBgaheYqd9TM1Dx2uJ-PW9I-bd0gPBHMaZRjK4lw-FTXOQKXRlMgElG4XMUFP59NXf4XoqjwsiUFoUbYtKfO_DP4bn_G-B7WCtuy5FcIwJJX2RYKUDnj39SAGK_zQ_pAeSMtYo5kKLrjuHcTi4kNeirhhwbOSb3VNyuhM613Yhn_31Do_kCVVCCW1Oh_R31mf_FbmzdunA4asGcyhR_u0KE0tdmsK-k3F8SzsA5dyf8NqrorPebNVldz8mpf3hDfOdTsjc0iGtZ0kLaapwk4aIPqmeDd5YOsrZX4qcSXYl-byHVxonrevYuJbgciUkBc3xQo_S4R0iGVHsBnS0_R2P6XtJEXEMG7T94qczyH2GCg8N3CfBGZl4B6w-aNz4SSrI5-c5yPyp7SYQ9Avx3UfhS761bXfSSUOBT7kLUtSpbYY-jHP1cWYJraKt6Emj-m0E_J9x6tLOtIRxpz6Yh-Oj0ySFequDvvuO7gXts1SMCCfXfOXEJnXUwK7bnGlznLTUa-bcBckjKtESRga8UZSeENIwWeNrtbDbHXI2gpBILZms7gite61NRVOcsQ-ekYKGy-YAtvvm7Mn6iVsWFqp3g682ys4lt10UQctj70" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f41aa6e732.mp4?token=arddpJ_FTWHIAPvOM6y8U81reRLPCRkHLoBaoPDIao-OX4lj0q1QE3Bgzq337V-UU2RsBgaheYqd9TM1Dx2uJ-PW9I-bd0gPBHMaZRjK4lw-FTXOQKXRlMgElG4XMUFP59NXf4XoqjwsiUFoUbYtKfO_DP4bn_G-B7WCtuy5FcIwJJX2RYKUDnj39SAGK_zQ_pAeSMtYo5kKLrjuHcTi4kNeirhhwbOSb3VNyuhM613Yhn_31Do_kCVVCCW1Oh_R31mf_FbmzdunA4asGcyhR_u0KE0tdmsK-k3F8SzsA5dyf8NqrorPebNVldz8mpf3hDfOdTsjc0iGtZ0kLaapwk4aIPqmeDd5YOsrZX4qcSXYl-byHVxonrevYuJbgciUkBc3xQo_S4R0iGVHsBnS0_R2P6XtJEXEMG7T94qczyH2GCg8N3CfBGZl4B6w-aNz4SSrI5-c5yPyp7SYQ9Avx3UfhS761bXfSSUOBT7kLUtSpbYY-jHP1cWYJraKt6Emj-m0E_J9x6tLOtIRxpz6Yh-Oj0ySFequDvvuO7gXts1SMCCfXfOXEJnXUwK7bnGlznLTUa-bcBckjKtESRga8UZSeENIwWeNrtbDbHXI2gpBILZms7gite61NRVOcsQ-ekYKGy-YAtvvm7Mn6iVsWFqp3g682ys4lt10UQctj70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌خفن رامین رضاییان درگفتگو امشب روی آنتن زنده: ما با پرواز زمینی اینو اونور میرفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27500" target="_blank">📅 01:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27498">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96336dd60e.mp4?token=hANPul3UpQ-7gET5oBQdC0iHgINgqixE5hSOcgIZeOH4Vgtp4T-KBvFKxVUGhsjIQYKGHgUGaqOhoIOCVqxn94K-HIavp3nmJ3gq0TgKTlp0Md7i2wsWxOdijJCIuLmthsvh0O8iR-NU-s-i7E3_y12NLG_wZujRFnL62JmzY1PlDdm8uZDL-iaWRFqINe0_Iw25aiqKwXJMxwGIXFGqT7hUHVRq0nvl-Qq1QaOob_6r35i3HIN3Oxgtmmgfec-nIOPJa0CeyiAp5VxO8RRuVNk9bitUjg_DxXj93Y0ruFjmNJyRv7nLfejyMteWkGeN38MFLqViu1qnqxoAVQ97qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96336dd60e.mp4?token=hANPul3UpQ-7gET5oBQdC0iHgINgqixE5hSOcgIZeOH4Vgtp4T-KBvFKxVUGhsjIQYKGHgUGaqOhoIOCVqxn94K-HIavp3nmJ3gq0TgKTlp0Md7i2wsWxOdijJCIuLmthsvh0O8iR-NU-s-i7E3_y12NLG_wZujRFnL62JmzY1PlDdm8uZDL-iaWRFqINe0_Iw25aiqKwXJMxwGIXFGqT7hUHVRq0nvl-Qq1QaOob_6r35i3HIN3Oxgtmmgfec-nIOPJa0CeyiAp5VxO8RRuVNk9bitUjg_DxXj93Y0ruFjmNJyRv7nLfejyMteWkGeN38MFLqViu1qnqxoAVQ97qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
با اعلام باشگاه آژاکس؛ مارک آندره‌ ترشتگن گلر 34 ساله بارسا با قراردادی قرضی یکساله به این تیم پیوست.ترشتگن‌اول ناراضی‌بود بعد راضیش کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27498" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27497">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRBsFQLGTo6RBULczoR1f7tJhrES1qe8kpAPDSSmAKvhDp6y5Hr46Zgt4KTXG6v7oRIkD_9hEK4TmO_OPIioFRau4ykWvYewc8IdBLXTN3TewdqSvFlImnRjnrBlYTH6x2nZo2VS0v5wbtmHzWZEaSgXFTUP4mcYzSK-kqMOdluDy4g0QCTSxBF8xGp8l4QmLuchzLolxvVHy7JeuyWuiIOF2TkdfwHGKIEWJyCVyhsvDcGPsFYDeBWrPJZySvXW2BYigscCjadTYt0iVxUTVVdegMKWfps4KX09DdFEwEe5Cj0XFedSpZ-qzF_lZFGTQZxcXvtRI7Kz_vBYyPypvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌ امروز؛
از بازی دوستانه یووه با پالرمو تا بازی پلی‌اف لیگ نخبگان و چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27497" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27495">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c2114992.mp4?token=q9PZUGhXJauTqcnaL9WXKZsTfgFE1gPg6aEArIBE-ujfdZLy5t2mMj5Mlv3nwiXcMUcIWssELUrhCCqxsELVsPHe3W6OHEsV8aWJ_GfcFzIZUmLBAIEKwWXnfYF77bDHSd12YMRQs05Neo2xcRTDZoWLB9e5Jn8NM26gCjufIACnRVlschq8M8sOU2LC-Ep_t-UqbAKqjHs7Y6YxCmZNWUAPhBNLKm0fCsOgFhqghKi5pjo5HpvhMWj6tNxwWytTzdVmVboSNvLQ5ibQX0CK4X-6r4q_OkbW_UdjjdtndJJ2c6Km8Ugc7IRwDqfDZSFr4Lbd1EZPKvMXS5gWfN_6Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c2114992.mp4?token=q9PZUGhXJauTqcnaL9WXKZsTfgFE1gPg6aEArIBE-ujfdZLy5t2mMj5Mlv3nwiXcMUcIWssELUrhCCqxsELVsPHe3W6OHEsV8aWJ_GfcFzIZUmLBAIEKwWXnfYF77bDHSd12YMRQs05Neo2xcRTDZoWLB9e5Jn8NM26gCjufIACnRVlschq8M8sOU2LC-Ep_t-UqbAKqjHs7Y6YxCmZNWUAPhBNLKm0fCsOgFhqghKi5pjo5HpvhMWj6tNxwWytTzdVmVboSNvLQ5ibQX0CK4X-6r4q_OkbW_UdjjdtndJJ2c6Km8Ugc7IRwDqfDZSFr4Lbd1EZPKvMXS5gWfN_6Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌خفن رامین رضاییان درگفتگو امشب روی آنتن زنده:
ما با
پرواز زمینی
اینو اونور میرفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27495" target="_blank">📅 00:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27493">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6mp2MSrDfWjAZvMRK72Q-5EBVMDtiiTMey2jT7KeHp-3vkTKQxnmOM8GQHEoXOZ4CFH4kQHUAV_xV5W5lJjbnVwMxHDyz2hiahI0sJJhSHMtJIoE0QB3s4qR3rmQARwBvgpLOhNM7YpY-N9xzm_FXLPispxS1HN8yYFkOTQU0f1oNekh0D8yQlW-xxNkqAd1-zD3GmKstOVGwfLiSrqLrj8QhWuQvVshfCCjIy_PD_t7Yxtu9HbB7DD0X5P6D7KVl6YtCRqgkoZPOjFhzo7qCUUn1T8llxq8p3HehaoTa-aZxBU8giZJzRB_lycEoud_lz18Ktp37paFZhpZq2GfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
رامین رضاییان: قرار شد ۵ تا ۱۰ میلیارد بند فسخ قرارداد من‌باشد امامدیران استقلال به جز علی تاجرنیا گفتندنیازی‌نیست و مبلغ روکردن ۱۰۰ میلیون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27493" target="_blank">📅 00:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27492">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLlTHS6QedTLJ9iq7iudtV4t5KF-wuKYyY_2cCUNOVj2xSnJWF851GCW4wTMYljFP77lIEC8FPWiyicT95vIBV38fYMyq5qHP4XPK1BrXOe-6bKRgP-cjCWCntDkbAmVzkeYQSq_MJ0qaycqEosR6fPpDHU5OcHO6YEVWvtdzJIpy-FUJ63Mmgt1KmrPQdxmewklDwKx-ytxLZCrcUy2hQ_MtKbM_Of8hbDwTT-g1PtIGj3rRKNGRUd_MaOCtP67s9Z8BXVjIQ6B2v0ibEodqyEuI5zF3wuWUfK3DivPQH37J1pZr3igmneeGrV2R46pDMBkuDFtjdxPKwh8FRDFmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج‌رئیس‌فدراسیون‌فوتبال:درروزهای آینده جشن برترین‌های فصل گذشته لیگ برتر برگزار میشود و ممکنه جام‌قهرمانی‌لیگ‌برتر به باشگاه استقلال اهدا شود و این تیم رسما قهرمان لیگ معرفی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27492" target="_blank">📅 00:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27491">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbHxiwWOsvAqDIIZVbLjDkUkDjQLNEERHW4Vknyu-hzH7e3tJrupoEvUEtszniAfTE2N-QmXNqeo4PcFmYp6rPmFdjFYRkuf4eYH-bvFV8XHO5gK4QekSfda_PdN6KbVHQcLp5x6KrcLnVo0kZfrtPC2ueLa-IfKinLvSs4mLZBNpP4Fqomg1PUTq7wjT64vrwy31lVDiMkybyn3PpO4OXGvRFqw2yhgCwEpN5xiE1uMUYlpwmoVAkEha4E7wEyTgdTYSp9KuU7MZ4cUaXFttF8PfsVBq8pkG2MQqd4gOaHOjuGN_KU1h0vjTLv7ZxeSADEhUDmMWIzz8Hy6Pi69Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عجیب‌اما واقعی؛ رامین رضاییان تنها باپرداخت 100 میلیون‌تومان قراردادش رو با باشگاه استقلال فسخ کرده است. در واقعا زمانیکه نیم فصل باشگاه استقلال قرارداد رضاییان رو تمدید میکنه بند فسخ 100 میلیون‌تومانی‌درقرارداد رضاییان میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27491" target="_blank">📅 00:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27490">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIoF5ZSInwOac3dnb_5dFEOLLQJI0pXHgA52rohMOXg4-GCcKt-_hjdYuNQDwfExq0yHM1967vogpd1DgkQUipNHqGnlJFf_mOtAyMRw8yvWdq0Fq4TDrA_lGzpXBWzFytYAzPaSsb5YUUvTMKAlRV2SVoBup3MNE1dA0biSU3E1v9PXRN8Mx3dWL0uhkSZJIdU0xfmWBaHLZPHuuqJ61aaFlq2rdyRQc9PhHbqib7Tj-afqNHjhmIULhDkhOF-mw9otGB3cqIKfv1gfKkpTl8h-j6zxnkz2TEZbiFb0e3S9k1-im1W-IPh9xMArgKbYIFzvdko-uCm_NySRbUrXGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27490" target="_blank">📅 23:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27489">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_eh3N7LqiZYB4y9uf0b6yh3R3gW4q4mHbNjwNyT89gAOC9XAXqA5AeJoO8mHe1IlGz833EbZEQn5cbCGvRTiJrILdv0N9xS73DyGGRsZ00elLPlZ6n9wj72DSJuFX16U2SgcBQYCBDV52bdF49KutjtNzz1F1jcN0GMabkKuROgTVU2ZIUulN5W111y12wvm7ZwhehSz0QJKN8MSnlR232fMoG3sUuSMmzjZAuWrAZyFMGkoxq4thoc_JgNyvkE1WkgYESx0fyTFBKCbRICD5HzbAkuR8NQ0XCS-A4olTPpiY_w3NXt8PVASFaaZG_YN97m5dLF91aT5_9Ax5xVTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سعید مهری هافبک‌سابق‌استقلال و پرسپولیس با عقد قراردادی دو ساله به فجر پیوست. رقم قرارداد مهری برای دو فصل 30 میلیارد تومان ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27489" target="_blank">📅 23:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27488">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdAl_tj78hjZiIAq8__7IAj73zWQGrnvZIU63rsfNk_F42RRHnnXcK2z2R91dmAcLK6oj2Gjk0jiNxtD3_WB7egGUqCa1ydUkzNv-oYopkckyP7BJaBiK8ZPXgWL42vt1WpueILIQQfozhc5pGQkEwfj7YVu7MtFmWtoJPWYJ5eEsDVBe1uiD2hm2yRS0OMzrUIW8Qb4TEoJYFskHzsUinQCJrnoM-Wa6YCCw0FR1rj4ACAE_y407NjXxcuS2StHSAWocgtq3dB3NTK5ku1rajPmEV37spoCaaeg4GtN5wn_apIIk0o3FlI5Vrtq5WfPk9l_7uw-isLrYLzssWgRNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27488" target="_blank">📅 23:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27487">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MU1oTYgrIeptfiJIG0S12U-GCQ1Nc5gtqPaO2q14UZ3RKU9se256MY7myweiHFlJK18dToyX1j_yxAFA3fWWm84njBOEdyjBo1r8WCF3mfLvtTbAr7rcPe1S1a5HX1py9YWHH1GCDUtAquc7e0Xa5ya4Ynet1qtlCKl5B_sQYNRPfIMt11hpZKBGHF-c6UmQdCLV0o0W9-8k0VEiR7P9tvdyEdCu4Xw5m4G4LUB1epRRXFxCGcijEDAhWYEUqqv7DiL8DTPirhDPhmQEZGmJrTB1NOE6pj2YWGyYFUycTiEsgDGHxPmIIwMwvfj4iIfqi8WIdC5KVm-MMCVOeKVO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق اخبار دریافتی رسانه پرشیانا؛ سعید واسعی هافبک تهاجمی‌سابق تراکتور و مس برای عقد قراردادی دو ساله با سپاهان با مدیریت این باشگاه به توافق رسیده‌است و بزودی باحضور در دفتر مدیریت قراردادش رو امضا خواهدکرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27487" target="_blank">📅 23:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27486">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOBARAhsaOrmWYMPyMNIzrQdh4-Kyc_0CL2DJDXM43Yc03XpuzxYxbs7HawbZjJwC42o_oMRwHM9jYFuHxRiEx_jFV0m4kLay1ON6YfIwnPOJ0B6N7BbYBu6RnEwOY0H9RsD2jprHjvjb24cgKQRWZElSiKk3Rf2GLwT21IbSe7b3h2NcE0xkcWkoxpCzN2dSRA87-PJTBtZJH19BGxlgZmz8EBHcmRkKGz87jN4UhyTqa1U22DBfEijbny6CrQmWX42a9k_hA19eMi9MHj9BR3thCHXzmOcocpKsL9iJfW7uzW-aTt8mW1NDJeWVPfdMmrWjkHauxszAVSha0FCKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
ژابی آلونسو بعد از اینکه با جذب دنی ولبک و هندرسون تجربه تیمش روبالا برد حالا طبق ادعای اسکای‌اسپورت ازمدیران چلسی خواسته اندریک رو جذب کنن که پرز گفته فقط قرضی بهتون میدمش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27486" target="_blank">📅 22:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27485">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6YMQsFUysfsgH09imBp5yqtA6F2YN1milPHit-6783J46nLTzAOwh8ayBuKDa2_n0No8SFf-YKDTghg_GuomEGxTO2Zlkcubr41lJ7W7sOQRrc0bbe95kL0r8tu5QvDys4y3SV9HCMA1GLwJn4Sg0jO1-CF7kR6efTw4w9uJ4bmmg14A5zgWAqufcvyc_AvCYLHzMYP7QL5W7yhgEWyCNpEtiJ_4-6B7C-J5MfN7-E8GlnhZDXxXrLzfaXkeAnNva79ap8NmNresqpKHrwzddJZNo9UdiEbGLPmJO_MSq6NtKRLb8J0GTIyaX3e5aoE2KvhduV4bUv92-cH95wK6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌سپاهان‌دقایقی پیش به‌این‌شکل‌از کیت‌های اول و دوم‌خود برای فصل جدید رونمایی کرد. باشگاه پرسپولیس و استقلال هم ظرف 48 ساعت آینده از کیت های جدیدشون رونمایی خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27485" target="_blank">📅 22:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27482">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o2TFoOeyOyjVOSxNyTRCgDQVldb0_9vYOGbQX6ZsU0IHJP498mszp-F0VRjtnL_0WysL8r1tApuAD1ym3hNWeJ39m1z2b3r-REWi36PZwHezLm02VqY-BdOmt_nxhjn3rUlZuJ2ECTJhFaGSl4X7eYSU7sBIijV0ghZMb6GUANFp-B_OR_ss5lqA8cpqrSd-hVDjQrPttQzHu2dmLpJtepj1PuFH2vhxtKMNfQlPIdgAtwOpIf15VnhskJgM1HI8sGq_lLAWeWAGPMSbP8pTBAUDHgj7Qis9RX6I2Q6TkrOLsB7gvr1VWdzGyVTh4Fgl5w9vzujTN21wD-5VIouqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z9d3RHvNVjV6cP_ORdHtV4DQk2X8rmmEYMfuNS2FBMNzgX_tCHQPltyWLHWlvobFR2dWm27ZazC2zJAHq5f8tFsle1o226N7Y4KEAL0x44rrkjolA5v3-UlINE_Y8b-RA_GjSS_-A7pgeqWRqSMZG0xFF3hFeoIFZ8mTkRLkOLrdNUy7LaDWr2vPZRv7OM430RtYicNlSdhaFx1FoyT8Yh8R2v6aSoEtTAAndV6xPEh0aImAFe7IakZzLiXwrkR4OKbKuxYaTNgQ-uhXtkbFAt-w6Di6vqHnm90P4qMKKCfyz2U-E_1vs7Sf7QDCeX42pqAFrMfeMyfQ9QwYbjQyVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
پدرو پورو مدافع 26 ساله تیم ملی اسپانیا که بهترین مدافع راست جام جهانی شد اخیرا به این شکل از دوست دخترش خواستگاری کرد و پاسخ مثبت نیز از او گرفت. دوس دخترش سه سال از پدرو پورو اسپانیایی کوچیک تره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27482" target="_blank">📅 22:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27481">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVeNY00el1ZKxEVDdDpp49YI1jiMGnSFpRPQEf0upPev3L4P29t3hlfxR7oYQkzCtz2GEPTq9Tznk6P3m5cMd6Qu8MOG_csX_rXIqK7JbAyGJGY9ovSmVImt7MbWIdOTxWS8fBKiEkAylE2crRz4mr9IrLTU_fqV7VGWR_TjGxoDlc740sJSccVAKz_NpOiT8LePWokXcLUNsRhPxvRXfQ3QiUjEPzBqlaOF8Xh_PRI61N2cWtRj0DV85h67UCWClADWtKQFQVETfzV3Gxa75IU9rSjVwhm3Og1GfquqBYVnhNCoGQHuahl5do8GauDP6fyDEOOqj7gCPPo7fY0TaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ سران‌بارسا قصد دارند بعداز نهایی کردن‌قرارداد رودری برای‌جذب‌کریستین‌رومرو مدافع میانی 28 ساله تاتنهام و تیم‌ملی آرژانتین اقدام کنند. رومرو برای پیوستن به بارسا چراغ سبز نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27481" target="_blank">📅 21:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27480">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kpy-jnsAaBWHIcJXdKbwev09ls3qgz0eQSQnOMfSCnI_dXcRxOPDbgGqpNrTaBnBLTdI9zWrLiwL998Kgo9jWgS9DUB2TMk2kquXWCgi9_EaB9G2MVYBWGf96Ohsu-eYoh-V_ENO0IPCSJOljB6PZQZuBvnWPjgzjFeY9YcXM7VPm4UZsnz8MrGov1d-oTKoLZeukqGeVt8B9V2cJVFvY46bLzspvDVCreiUyQJVQsT5KvbWkQMlED0vNtKYwZE10w_bkVEQLONfjDiV2qU8cPKryX-R9ehyFzVKEazf0qL4c1iuA_Ss9xAKL6kPKn_hn1axeeqvYrcBp3TI5I9_0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تاییدشد؛ بااعلام باشگاه استقلال؛ استعلام فیفادرخصوص‌قرارداد یاسر آسانی صادر شده و این بازیکن هیچ مشکلی برای همراهی آبی‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27480" target="_blank">📅 21:13 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
