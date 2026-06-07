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
<img src="https://cdn4.telesco.pe/file/JrsEPndXhLSjgYLqJVYtMPs8BKmyyFw6I7YufMwrAmGr0ltk2v91X0R6QEfJP_UaeGn28zUvMlTG0FUF_mH5St4Y4_fYF5xAISMptj1K59NCaCBeUCYIObIal48mL2bcQGyHXLZ_1sJzera8WgmnXupcWYiHwXsoxntCvG2JyyeAIP4oURvC4rqelfBpsMBacRGGXHbuqFnpFfrbQPSEIKAFhtGdilZ8gAFX-EPz-jQUWrHzICM1lYnfobjsc-6_CW5WvkYHpqLqWU6o7R8VHwUJAIbNOtQUKPSjRdu67mw0tu53ahnVKrK2IO8_APifon-X93ujEtC7H1BBwdGFmw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 172K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 16:26:06</div>
<hr>

<div class="tg-post" id="msg-22935">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lax9yhjKNL9vJ_rldEiGHvr5zW8Gq9qoZTiGGwjt0-BqE9KGiVEQIvh5wMpkvYPmjI77wipqWd5lCKHUh9fJsxhpEVfbV9uGgQWU24WmpqF0udAaHM7_NDRNZBQrNAWxXdzRHWWPDnXsycTjhJCMiskVQZ6vq2gwnSRVImDb1DX1GIWTfCWh4moLC7beDzlben6Y4hmakti5qd8yigLXiBKsILU_CHvHjI3oGkapZU-ISbsSDj_dfYUwCA9jE1pCApkwWTV_F3PDOqZMPKqAGzjaDavK3jeO7yjlYzxpHG9DbhiTLx6GDPuJ3k7IlFk8MBWhEtaRTvW1ymSGCaB54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌انتقالات|گستون‌ایدول‌ خبرنگار آرژانتینی: با جرأت بگم که آلوارز درنهایت از اتلتیکومادرید جدا میشه. مقصد بعدی آلوارز صدرصدر بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/persiana_Soccer/22935" target="_blank">📅 16:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22934">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGb4bf1aCCyq8tuGJ5mvYk5fT2TvU2YIOv3PTNnLs_2-y_Z1atgivEOjM_MWkpPA3HQj-fGN5RgYrq0VXXKIEuFL0rkXHttGTH5pkqyqTQzdmEDVJ4NODfcCZltxY3HqhAHHYBdTu5N_glROUyDovTrL3QoAK5i-sgLTK9gURw6EeMIMGFY-aX1kwPhHHQaR-vybV9arduGsVX4eVwbWG5j-L1r12oU5LElUz0EXKWzMMEMXLtsMYwKyloxJ01OetbKSbKVAuYwDmhQ85x8HM2-90ImFWPJTsye5urEOXgIB9c_BZTmt0mERtma9sVuQVdGkshcXk5ogMXbAqF_FZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/persiana_Soccer/22934" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22933">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=XkARHvqKBgZkA05ewjraQ5MTp94QtQjnNjc1iI3JMkQ2cHMu-rsr9XOPBdOwisFiInSU_uF0oNoK7QhtyyBlAKOj8w23wLhcwr9jl5Q_eJGE-UwPBMmGBY_2fSouINCnk1WBsf_9DsrNQqFScNvMZ32BbOd8RkO0B9LrV8ZD0NZ_xeWmY2RtdsNH4CRL40BtxQEqZGGnLe2v2DQzzP4gucWqPvWHxwxjU-2sQQnEEzAPYWTqg2uC6VLE-8vphzv7pY2M5gcBy3qgbDc_nl48rMVIe3sXnlGgWZEC1vVezgHIKPGu7nLJRx-_9AGB49lx_BAAf-hIZM-I_jdK6Iz-Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=XkARHvqKBgZkA05ewjraQ5MTp94QtQjnNjc1iI3JMkQ2cHMu-rsr9XOPBdOwisFiInSU_uF0oNoK7QhtyyBlAKOj8w23wLhcwr9jl5Q_eJGE-UwPBMmGBY_2fSouINCnk1WBsf_9DsrNQqFScNvMZ32BbOd8RkO0B9LrV8ZD0NZ_xeWmY2RtdsNH4CRL40BtxQEqZGGnLe2v2DQzzP4gucWqPvWHxwxjU-2sQQnEEzAPYWTqg2uC6VLE-8vphzv7pY2M5gcBy3qgbDc_nl48rMVIe3sXnlGgWZEC1vVezgHIKPGu7nLJRx-_9AGB49lx_BAAf-hIZM-I_jdK6Iz-Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آدریانا اولیوارس مدل مکزیکیم رو بدنش عکس تک تک بازیکنای جام‌جهانی رو چسبوند و از دخترای مکزیکی دیگم خواست این چالشو انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22933" target="_blank">📅 15:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22932">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icyxPyIMZLXOhBnszi35S8RatgFTuemTgjKWycB06ecJQF1CE7oE8D2uRfWfpGq8MPhhghIAOGgio9DV2rzWJ6FTB540MMUaqEGO2JEM_tIQof5YYfwZxdNP2LUysVdBz6_uZnKc5gKePympxw9b59Xfgon_4LHOh56rXpAdGv-X71IV_fOUQTaqOjmvtVwwBTe-wXCQThNIdBhoNQwRez4tEuin8y6_QaQM2CxdOdvzLrYsbx1uH-4Ssfn-X3D1cIaZfvGIXh_8Mr-dEsZG8o4G5FUqN0YKxB46OtkhpSA4aUvL_loQA3C-oglqH337dZAmcosOSOLc0HmTTQ_w9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
انتخابات‌ریاست‌باشگاه رئال‌مادرید از دقایقی قبل شروع شده و تاپایان امشب هم مشخص خواهد شد ریاست کهکشانی‌ها به کی خواهد رسید. شانس فلورنتینو پرز بسیار بیشتر از انریکه خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22932" target="_blank">📅 15:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22931">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu3cCPiB9biljzNroIHYzHyC89wbuPEBbARpbRLYq0Cm5gWvEqqkZeJgaq7ffeOaeEfH9mNTmxEczRW_zWx0HQs-8YvIYax3pjf5ISUkGWbpQywvM8yIo5k2EwzpKvK_-IllC1THLR9aCGvuHkpsixcGG3wKaQot2TsSSFyygcGDSOm3Xvn6BMz923GtXYWcr1Q4XwVKRkcV7OyIVS9srylj4oVSxs1oIse42mqBP-s-ktKnM5DgoztYdCYE3qhi7bGk9zvuYKT0zvpCjCfELURJ-uo07tt2J4dwGqrzqUmWhQuYgS-JTNpZzTNGzGDVekZMfRt0n1EPY3zTiYYMGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/persiana_Soccer/22931" target="_blank">📅 15:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22930">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvhkRFYyRgNlK-o_v4rpmEogdBCaM5gcd_UpFF7oQKzr4yzAQiG2BGm10gp7bc2HdalE6he3RQps4PrRds9vH8yfH0rsux6Sw-H3SO_F3U0s0I7MdKFRAMKQT_9e-GRjW_Dw4jUxa7kVxwA8I35fj0BjhkAREoBPfsJ7zreTrz_j622H3aocOYow6UXGLBsHUi5PV6ZFWCG0vmyq0qXEVGlVCvmjRX3Ci9jAW14xKmdmx2JsG2-Xb6xkjSkYshK8j0XVACLubgK_DCz3h-2Ehslj0TRxqsV7qOp1A7mtXjiagi_9MCd0Pxbd1z6NmQeoBWYGAB0iMkUleN9aBU5u-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/22930" target="_blank">📅 14:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22929">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZl1mcDoI_JdnFB42XtXrYojR63BnVD3abjvllFIOeXuNhAFgQunmic6pVr0gK64ccnsf5_4FSr1ydBWXx84W6axrtVLpYdB9LBBH9f09pnwj7d46I3I7voEuSpPNRoG5jeEH81E--R0LoLVI9Z0cVg3XZCgGPwayf9SApwvGJINzcIXbuQltH3arXKpkkGclXCTsuejlzVeWmEL531IAuiopnl7e389Z1o9tLPQ2HGV6KRvG0WBV7pd69s0pyOy9esz8u1yWr-cwHopVPT05upQ78bYa7uhWTZmeMiJZqhv8u7ikLV36-XMa90qn-T4uVisARe8T_e3MQAeixzgXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/22929" target="_blank">📅 14:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22927">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fq1YDIVfOjXgt2_yDpN6M-hVNnKckgY2c4cViBNErqKiXb5aRM9AjPyaiGGHJU-ME-ADEQ7OYm2jpQy1OUCGc1j7MJWliiQjnj_1fhM3IcmEPItjgmvLoisopdWOSaTISVMjFwayNhNJC_zMkFk9DtvwQu7NfalD-Wu0d9x5nL_oHjhhTdGAe7peTw1KPDKShMBsQgPwmUz07zq8GfJk63bSLkzXgP0ziPGZ7m4pTEAWhzHkNibcI_mQJ7GP72I2dqNe8vfhdSfWtFSPgr-d9HHOTX4iDWhKuhwT15MPuk-eXvrEGlcsj2hD71i9fk53ErSnZ-p-1bDQOsrkg1XJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGpnqHYCr0dQ_DyiXnVBayshFJ4LuhoXSzR_Jmq5XbtBGnpuNZS7j1bxhDoNQTlHh8KlEqVDEzEmk5eDE88VHmutflqJemHm7Zitez9Yf5WlTFz23jy8UvM32QsqgzHIJcejE0xg_ZFym2zoA8Y9-zeT3_I4KlDCURbGRzU5_8niK2P_uPNcliZ1U9-0TVsJdVuoxVYzi-ndLem9TzXeagOO_5L6VHmX-q7lTWZivqqqJ9eVAN4U1T42QaydtBmaKPWqGWL42XHYROHukcXmf0UdqSGqguyRueCUUCL4LxCh0VpUhP9TYJVjmkmKXIiDo6PkCSRjosidSPTBMa2XOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/22927" target="_blank">📅 14:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22926">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZRbNBgpsVD2311F6i1IL-lk3Lj8sYXnf0ZdZnM_1Ox0PBmhYOJ7cecOV46KNXdqTsoNjBkJXdw8y3GXCKk3Q5wNa_j6Ju08XGIyU_pFvmK4Z7qwgYeUm_URcCrzTcs1Xx15hZOZkOlW2xY9MkJ-BUt0lw-De13pVs4LMw40LZR0pegjeDF-dFSTXfEqRvM2rnXZcn7WIh7g-qr3l4sRqI2f52KrLWJrCmNp1y4X3uFf1G_VIVgQl5GopJSXoooJY6HyZ_tweCxB-Uhyx0ItutGmQVPIZsuMdUJS6xVFdMkPWOQgDa_APUAtFqwcdJya1eP-NKcXku2BrX77pI_low.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/persiana_Soccer/22926" target="_blank">📅 13:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22925">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moUtooTgecRiJfSZkBFiXpQEe9gpqP-n619GsI_RbrUGl4ZJuJ66PQ7uZMXBG5XALrjO7RelA1AIN4IDJbu3AKo6ijWnId5RA9o2Ns97yQKTny-huZMcZGf6hEgYg0W2J-lcAcj_vJHFI9wL-UEUdaB4JO5q32zAh4yxAIEuDJRPVETWBzQXZ1Y1ZhHzVUvM5kaWpG85VvO-PfiLJbR1xT8hyWkrW_jRsX1X4MmvsqhMOTGZJNEEaZlSTKzNuM3Wst1wNGg2DC8JhrD4_dyKkLnKOVMfv2p5_8Acxed2WUYd-Vd0FwWqWAGSQ5ruU1e4F0QRmNa_6NEglyAeH7uvhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی‌کنیم از این ویویو بسیار قدیمی امیر تتلو درباره استقلالی و پرسپولیسی‌بودنش در زمان‌های مختلف
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22925" target="_blank">📅 12:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22924">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYFOij0AgEd0DxBV4rQUdrdAcRzSvtLbM9gaFcBQMcJ5mbeFgMfpmKd0-tXrnARchmxvWoaFoga4dLvyXmELkuaTZBl7GlvhJmS6lhQE2wCvdyBuBtyA9bfBVNG5SIq65mObeqFZzuHR9WHQdob19IFGfdoznqRiKDEgADVb5Jc9q3RFRinpbkh6kYC0kfz0BrHwta2zhGbWKlGSEiwNYgVZsmk7HH5BrMJAltrndrg1vGhRHpGEebupPTkm2OnG2R51T1ZKdhhUYWMOT6I8MRt-F38oF0eqwBKbQzyKt1niIn8Yym4DP4xLcLUmWeszpyxQIdr5ue0SQOcb900LZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ هفت سال پیش در چنین روزی؛
ادن هازاد باعقدقراردادی به‌ارزش بیش از 100 میلیون یورو از چلسی به رئال مادرید پیوست. او در طول 4 فصل حضور در‌این‌تیم 76 بازی انجام داد و تنها تونست که 7 گل بثمربرسونه مابقیش مصدوم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22924" target="_blank">📅 12:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22923">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a056081.mp4?token=JvFX29dfyr3k6eZoNzbbizD2pHcgYcYd9ObKJf6fvHB13GErjG5qDn9Sqq4OuAI9uJUEA1Rbt--SICKN-knnrdtWwgMhDodGpR-vVqnwfZNdU876nZ0Tg_bOoCMa6IzIOH0i5HTbECln6_nEyxurW0S53VZAKg-6h-BCJWHeafM3Ep8rg_QnrPTznprIHv832X4H7hX-Gv_h0QgxMBHl6YUaKVhxGDcKdM-atWTG9U7kqRNrVAdBmlHVe34BDy1aiIB1rt-6khjRGSuES_fVgL36QMidInK9Kf9WdBrGuykFBRIT7JDoDnVAw4nkgR4QIxE6fFlOxW4JZJhbKHYHWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a056081.mp4?token=JvFX29dfyr3k6eZoNzbbizD2pHcgYcYd9ObKJf6fvHB13GErjG5qDn9Sqq4OuAI9uJUEA1Rbt--SICKN-knnrdtWwgMhDodGpR-vVqnwfZNdU876nZ0Tg_bOoCMa6IzIOH0i5HTbECln6_nEyxurW0S53VZAKg-6h-BCJWHeafM3Ep8rg_QnrPTznprIHv832X4H7hX-Gv_h0QgxMBHl6YUaKVhxGDcKdM-atWTG9U7kqRNrVAdBmlHVe34BDy1aiIB1rt-6khjRGSuES_fVgL36QMidInK9Kf9WdBrGuykFBRIT7JDoDnVAw4nkgR4QIxE6fFlOxW4JZJhbKHYHWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
وضعیت‌‌آکادمی‌های‌ژاپن؛
قشنگ‌ مشخصه دارند برنامه میریزن که یه روزی قهرمان جام‌جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22923" target="_blank">📅 12:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22922">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKnxU1o3xGCGkeus0PDmo-Vm-nH9h0ktOfQnd1Wu7ujFzwI1BtMayhq98EAeE382smq_RaiHXnlcyWjfmlX5dBhMT9cN19xhtzglL6ktj5tWc766Zczz846iRA3Gk1KiSd8zHap8qi3rEi05LzMuXnCRQzU_7AFVP_13CQgSQcFDiQzLZpUbmVAEVqBkXBCOLvZe-lJeWDeZ1kBSwPViW30E6qh2zgztLko054Voxliv3fxInDZm6cs6D99i04NpFvelBsB4oyyIoCJwTnXRgLVXyghaqSouGHIMDwwsRIb9UgAq-vkG7gcj2XKz_sYozNT5NzXrouLPWbr47pkwqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حدادی مدیر عامل باشگاه پرسپولیس هفته آینده جلسه‌ای با مدیربرنامه مارکو باکیچ برگزار خواهد کرد تا تکلیف نهایی موندن یا رفتن این ستاره مونته‌نگرویی مشخص‌شه. باکیچ علاقمند به موندنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22922" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22921">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=n3OgRashE32iQ5Kt0TzVA-6iyCFhjq-z0wbAAUPrgMJH8ID95-YevPfbS6UUmMzWsDc54Nwq6pK2REdzeAoClbEhp6S9JFvOMPoG5Qfw1j8vENjOENjU-d6fGDa8Fe1ns6dtp2m7rSDivnpJYBEY1z3SkMazkd4yB4s4V3rj8-aTVf1T0KS3tspyruSNAR9gQ8-ZAd0SHbhU8BDHxH_ktgNPxrDwMbN1kMZUGdvAX5XzJCF3ptqsH-OF7xUE6_PYdrtEmDTyp23rYzCOlUI0XjualbVtrmHrEPc2zUd9BNLN6lJR95_6olhd5_Evh2bYPOC09wwFaCaTM9ITNSt8NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=n3OgRashE32iQ5Kt0TzVA-6iyCFhjq-z0wbAAUPrgMJH8ID95-YevPfbS6UUmMzWsDc54Nwq6pK2REdzeAoClbEhp6S9JFvOMPoG5Qfw1j8vENjOENjU-d6fGDa8Fe1ns6dtp2m7rSDivnpJYBEY1z3SkMazkd4yB4s4V3rj8-aTVf1T0KS3tspyruSNAR9gQ8-ZAd0SHbhU8BDHxH_ktgNPxrDwMbN1kMZUGdvAX5XzJCF3ptqsH-OF7xUE6_PYdrtEmDTyp23rYzCOlUI0XjualbVtrmHrEPc2zUd9BNLN6lJR95_6olhd5_Evh2bYPOC09wwFaCaTM9ITNSt8NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیبروین یجوری به تیبو کورتوا پاس میده که انگار هنوز از دستش‌بابت دزدیدن دوست‌دخترش فشاریه و میخواد کاری کنه در تیم ملی سوتی بده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22921" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22920">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22920" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22919">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okeDmGPSsnfqlz1TZJHa7O4wjFo_t4dttwoBH1LsumkFzCKGiffhsB76nIyI-FrV57MfqyHkKegCYw9QmQORBlt-b-GzixJbRC_5PtkHVwOTWVaFnEjJMbDBS55UDD6FEsEBQuSIVfYZOaWPqu2MXvmzErCNQ-NtR0bQ2pzBM1gOkEdC7D2h5prblUJ6lh_KOr3S6sHdDX4zLVsiAHnbp4ddDZE7Yd3gTEK800xrsnpCDIImcU91pPZu3LQtg3VrT7WCqu-zFdrF4VEd5ix5IDlxPagQUUK-fjAl8G6npUCfUTBCgUQqYXP0tU3Hh4ka7-Q6NKEM4p4fluZkmtaPMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/22919" target="_blank">📅 11:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22918">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dM4Xz-Yhsz4-X-MYe5JzaoOoy6D2L-9-Utnhl7qb7Vn1MBYflfNf8fUDuE4Xt9DI4jmFB91Yn4Yjlguqnchkk2ybVMNt39t4p8oV3gnr9ne1apvw0kZFePwDmk0aQLZIdAcorJmCtHtww8jUNlhjeJCzig3K6dQ_WV8P3f0RutBHNqqfuk8f48NPultnBT1oILtbFFjKJ2D2X98SxBmUNq5R82jedrBfBrW9jThbYlvNpLw9jvqDtsNGHUKqY3y6dfkrHO7CTeSArYfE7t6sWUPZb7XvRiYrdvNnt2iEt7xUejNB9GMn1o-gdpbb8cB9Btk9FQ15-CutxXg6FYjBJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22918" target="_blank">📅 10:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22917">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=hFq31mxM-BgQJnkonvEESD6sw0nclzNL_mZm-kRfsfx1lud0rECa9jj5AZopwpjAXxkNeamFJPN87tj_0iRbgcZbpgd4WsbdDnZTURq666njweXUBkFtiMtEIFbDodxXf3OWkn9LrZ5KS8_whZ5crnF6WnkJ4Y4QVZwMewnNgxJ7NgCGUdBXMxT1P9Fst0XLvi-BYU2WJihgKZ50hOxpSqXfWeLWm8lM9qCiB-N4rvaThWGZhVpW7cK-FQk1bLMDFnozvAE7aeTG_cAFw_mDvfCzDN7Z6L4e5PM_LANu7QrNmoId2h2LfMABl2s7Bm97MtwEBktSemKV2w4qUb4_gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=hFq31mxM-BgQJnkonvEESD6sw0nclzNL_mZm-kRfsfx1lud0rECa9jj5AZopwpjAXxkNeamFJPN87tj_0iRbgcZbpgd4WsbdDnZTURq666njweXUBkFtiMtEIFbDodxXf3OWkn9LrZ5KS8_whZ5crnF6WnkJ4Y4QVZwMewnNgxJ7NgCGUdBXMxT1P9Fst0XLvi-BYU2WJihgKZ50hOxpSqXfWeLWm8lM9qCiB-N4rvaThWGZhVpW7cK-FQk1bLMDFnozvAE7aeTG_cAFw_mDvfCzDN7Z6L4e5PM_LANu7QrNmoId2h2LfMABl2s7Bm97MtwEBktSemKV2w4qUb4_gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایگزین تشویق ایسلندی رونمایی شد، تشویق وایکینگی هوادارای نروژ؛ تو جام‌جهانی اینکارو بکنن ارلینگ هالند جوگیر میشه به هر تیم 5 6 گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22917" target="_blank">📅 09:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22916">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCQr5lQIG7pUefNUFLKc9DF19gJDTnsNQIy5dYYVjB92oPIs9QwUFoL5VjsIByr957khbqeCWJHlDdd0t2hFR8_jghTL90r3HOugdh0bQrd14q_d0hMSt4ANIzqyHEGP9SJgcecHUi3l4BbUxp7W_VjC00PygSZ06xnCZFBfcRRIEyg3erq09KE_DwX74hCTX33hYC6wQ5EHaK-1Eq9_RUa6hd6i2UMpBzU71HRCjIKLrpFuvsxeVxnbk_jEu7XchUipjJt2k5z2vp8E8qGBLWR9B5gag40gbPlFleF3UQXeSUjyxOH4Z3ufgIhgd9zWuel5nhcotgHt69z5EbMbUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصاحبه تاریخیی کاکا:
برام مهم نیست که بچه‌ هام بدونن یه زمانی بهترین بازیکن دنیا بودم؛ فقط می‌خوام منو به‌عنوان بهترین پدر دنیا بشناسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22916" target="_blank">📅 09:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22914">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcIZKiInmeKjbz7gucWvpbmiH-8Jm1qXw_c5t7QROBxAg02RiFwLoR6yQL9qwYWtKPmXgs2AMDjYbjQzjvU-QgwWpyMtr03k6tptKbzXRMdFLI0gXi1vQMzsHunH8V5IvOecny5d-plp_J6YofntItmxTZdh9ynoIy6zCioFiZV8X-80M8RvMm5rCmtEYykH9Ucaqlz7s4AheKzZn6iS4LmlKDe4G-e2HVmDVcAZ2rGPfLJtnzmEwsMfZolF74anuO462lVFwDgoAVszKlmJ7lmf60o0YUE-9BpG6opaXrM4-QpqQEyHyoX65hOgs8XzDcK1F_tAYykYX4jDDamBsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
تقابل شاگردان کارلتو با مصری‌ها و جدال یاران مسی برابر هندوراس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22914" target="_blank">📅 01:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22913">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_cGA5EC6fNsiEC6Qt-xtpJczXqgLl8Lnx6RdJyKz4MnkXVWkSCaEXKM7EVEWs9jJ0osaSIxqXaTnlWSzmKlrON8p3NO6fIhgCgIjT_F4Qgs2ENSbz6hyFRmmMBgpivZZT8MPTuGkiGGgsOjXqLfIPYNwqeB-qaLI6Vs-jy2sEi35_z7YYhXnje-aJ1DRw7vkORdCuIzM3oRmsK7yWE2SaiAC-wvXzYRU_VOeVJNM7eM688R5AZo-Y72eYybcOqJcVSMygucWGIK3IVYQxKqlROcnsg7b4Siin6BYt96LfX3_aoMYPIqn-NAdAFeSrDVdkqbfD12T5qw2Q62z1qllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از بردپرگل بلژیکی‌ها مقابل تونس تا برتری تیم ملی پرتغال برابر شیلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22913" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22912">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvLLkO536MxvJoQ7KU1-KR4WS0P02LRidK6-ZYsBtsgBCJhqzJftDuuasfmZFnYate8GFC39tMDkOkTe60w7SwT0iCZvgUizLVue9KWqMKvUy391C3xyLD-9mTqrZeVBYAU6PU_XhrlKbY5aIwTY4X9koGNvWketwRmYd6Dy_2WL9UH1mnmgrYQS6gWkl0ptu8KOrlnGgR1Hqh4PxDinbXnRFg9F3pXM2_7_B6xV-ur_9d748Bn7me6r0JoKr9Wsv043HX8wcztNsNtESJil_ZM7yT1WKRpqfIbr0-mVp9aP43Zser5cAtAQOE7IZyfYpt_CCB0RTleT9cSHwP5Xnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22912" target="_blank">📅 00:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22911">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=gVWPXJSDehIUvFzo66Z1Ik3gjlSeHz6H6tpScPffSNJuyo-3yNi5Y7f4cQVLZ73VyEZWd6AXl1Gzfc6rCRAcAYGF2o25xZeYmFKW2RoLi5lZYpU040PZJOL6a5hajYKtf51R1yPSlZCpFSB0DtTqO-ojD5eiLHzg7VdRXo4DrtaaLNeM0ej_YcQjTfQYllcUkO4lSijhnWzT7JjaO8s2hPQFgpH8vP2qSvRMp_2iStLt0nD9eCfqa2_fgh6OxzDy2DwP39tQBKQFhD07RB9Acm3RoxFHgmT1AZfT56-kXGUq_u2Z0ebzpSPQzu8HGqh3pkge34UID06mQhIwuCoDdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=gVWPXJSDehIUvFzo66Z1Ik3gjlSeHz6H6tpScPffSNJuyo-3yNi5Y7f4cQVLZ73VyEZWd6AXl1Gzfc6rCRAcAYGF2o25xZeYmFKW2RoLi5lZYpU040PZJOL6a5hajYKtf51R1yPSlZCpFSB0DtTqO-ojD5eiLHzg7VdRXo4DrtaaLNeM0ej_YcQjTfQYllcUkO4lSijhnWzT7JjaO8s2hPQFgpH8vP2qSvRMp_2iStLt0nD9eCfqa2_fgh6OxzDy2DwP39tQBKQFhD07RB9Acm3RoxFHgmT1AZfT56-kXGUq_u2Z0ebzpSPQzu8HGqh3pkge34UID06mQhIwuCoDdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصدومیت شدید مهاجم صنعت نفت؛ ویدیویی که روزتونو میسازه؛ فقط کامنت‌ها رو بخونید
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22911" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22910">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=EyT_SoeODX6M9dbgPDppUXaIuIMiPvEJAdDf8g60eJ2NHInNJ1oV9W-xJ3GBWNI9hE6NnIrQL7Pss2mItcrTWfhXd-dxUgC8uq4l6n7oA8LQLW47cfSztJkEySynMyD2EKw5-YmVqZKZjTMFr0We-AK6wH1syTlV3BGjvTuDfK-IkosjQImpl-5_QiVQ-1nIuJrmnF-aj0b-KIUphqB2QR91IHBAzm_jQuHn67g2ZB4rGEsNmJnvIvAg9l7h5q2-XnHIELyYqqQ1Iwjt0g-3H3ZoApJy8xDovXgf-pCjKfeCH9l9oKq06qHI70ArlOz-fneDCQjg9zvfqOUCM7M1Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=EyT_SoeODX6M9dbgPDppUXaIuIMiPvEJAdDf8g60eJ2NHInNJ1oV9W-xJ3GBWNI9hE6NnIrQL7Pss2mItcrTWfhXd-dxUgC8uq4l6n7oA8LQLW47cfSztJkEySynMyD2EKw5-YmVqZKZjTMFr0We-AK6wH1syTlV3BGjvTuDfK-IkosjQImpl-5_QiVQ-1nIuJrmnF-aj0b-KIUphqB2QR91IHBAzm_jQuHn67g2ZB4rGEsNmJnvIvAg9l7h5q2-XnHIELyYqqQ1Iwjt0g-3H3ZoApJy8xDovXgf-pCjKfeCH9l9oKq06qHI70ArlOz-fneDCQjg9zvfqOUCM7M1Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
امباپه27سالش‌شده؛هالند 25، اولیسه امسال وارد 25 سالگی میشه. اینم لیونل مسیه در 25 سالگی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22910" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22907">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=kiRhr7cs0u-e-IypNX1shV8rmJxEoiMVlu_-ufdXLUg6o-nPnEIK4zzEmcFyFU5IDZfr2pC8eH6Xsw_UuKiDKNcN_tT-wAvodlUSIyBQa3krmccOp575wO6RIdAt-1aQTZVm2nXbpPO9-ZPxKaFhT67V3J49wJcTAbKheOPlhtBC5k3MYRH_1d2zNOW4R2jGateKFZWp3rfALnpDrJRXXOEjYRjuP4bTwJzqD0hTAXjL3lllJmWFvC1yHJ591DuTJGyxWAIXigNTvl07jur3NsbJMP_uA3qTU48qdyzZcGh4IB52G5ZIWPQcFUjP-JK_ohm5BemB9woVWJ3wNeovEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=kiRhr7cs0u-e-IypNX1shV8rmJxEoiMVlu_-ufdXLUg6o-nPnEIK4zzEmcFyFU5IDZfr2pC8eH6Xsw_UuKiDKNcN_tT-wAvodlUSIyBQa3krmccOp575wO6RIdAt-1aQTZVm2nXbpPO9-ZPxKaFhT67V3J49wJcTAbKheOPlhtBC5k3MYRH_1d2zNOW4R2jGateKFZWp3rfALnpDrJRXXOEjYRjuP4bTwJzqD0hTAXjL3lllJmWFvC1yHJ591DuTJGyxWAIXigNTvl07jur3NsbJMP_uA3qTU48qdyzZcGh4IB52G5ZIWPQcFUjP-JK_ohm5BemB9woVWJ3wNeovEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی‌داماد مجلس خیلی فوتبالیه، کریس رونالدو فن هست و به‌هیچ‌وجه هم اضطراب اجتماعی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22907" target="_blank">📅 00:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22906">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=vB0eRPgWDTtQyXCebQ2haugYCsxpxihIl9YHmM6zlHaB3f9qg7IiPakKLLy8VD8JsfOLltFq3IAglr5PDo_GOBLGOi2oONKG-QF3Eoc32a5YpmlQrcI0jQGBON4TmCpqqtwEcQbxVIunDo5GZJeY5snhZrhAsfDWOxK5jONdwh2QS2LjbV1kYbFYWp6v4CO5CipT5-UMXS1HzSSnxbv0KXoI9rmV6B2w0sdHOTBGB7yq3c2QD6fOO_S7ID_KZ6gEEHKG6YSxlt7RvARCIzxI6UDtaA5htf6WTtN5M4N5LIL5O5Z7faH67REwVIOlMXqwaqbJ9CLHsrAn-9XZEwM8hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=vB0eRPgWDTtQyXCebQ2haugYCsxpxihIl9YHmM6zlHaB3f9qg7IiPakKLLy8VD8JsfOLltFq3IAglr5PDo_GOBLGOi2oONKG-QF3Eoc32a5YpmlQrcI0jQGBON4TmCpqqtwEcQbxVIunDo5GZJeY5snhZrhAsfDWOxK5jONdwh2QS2LjbV1kYbFYWp6v4CO5CipT5-UMXS1HzSSnxbv0KXoI9rmV6B2w0sdHOTBGB7yq3c2QD6fOO_S7ID_KZ6gEEHKG6YSxlt7RvARCIzxI6UDtaA5htf6WTtN5M4N5LIL5O5Z7faH67REwVIOlMXqwaqbJ9CLHsrAn-9XZEwM8hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22906" target="_blank">📅 23:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22905">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtB1zB68hpxpTBnZKUp5x-vIzcV16x-5mY0ZkcapYPDOAqPC3rkj17NI9WhOKupnFt2we3wSseISKmfQIgnUQ89u2MMvY94wYOFwSjMj0zMWc5YuQQ11mRzhpH975mI473nyZz1NbYx2I3dbDicPNO963_-zlxGjp1WcDmmBtdu7iO1qDmRcVK35Gl1u5VbD563aHPS8IXcXaoKkoLEWEhQiwXbtc8QtwftbPpjF65kNcjENzfa4Kg4sbPV_GrVXs28-qy-uZw0MJlrKkrLE9k7oJraNQGZyLK1s6u_MTxikNKl--TVDwii5hZeaolf7aipYKoe5pOC7bJHJhFtjDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
#تکمیلی؛خوزه‌فلیکس دیاز: مایکل اولیسه از طریق‌نماینده‌اش‌به‌مدیران بایرن مونیخ اعلام کرده که بعداز جام جهانی 2026 تمایلی به ماندن در آلیانز آرنا نداره و قصد داره راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22905" target="_blank">📅 23:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22904">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7O4ED3dK706BpzIKC5oRiik3YNibmNFsiqwCTfpfm5z1fuRmcLhdBdLHBD9cxlzgwqHm-mOU2X8vHL4ZZACgLjbLxbzu3e8_dSGYlf2NWZIDxP3xALUWuJ7picSkqDaFAYAEXtYTyhxSkEJFGUFB254lx0OpPXgYlkzly7xfIS2cV2IIpPntYSFnZsO36F2-pVXG8JbPu6fbo_vrtrrqDhODVPvK7V_z9iL2dUhnCYSULGYYdWUoGZHSsGsUISuw_F_D4_d93js7WYozU6375ZXTL15mDxpbVMxoS4QW2o1VW_xeLISisiwT1KQkCEckducJYIPj_nRNuC7Cxt0Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق گفته رسانه ها؛ یوتیوب بزودی طی روزهای آینده بطورکامل رفع فیلتر خواهد شد و همین الانشم روبعضی اپراتورها مثل مخابرات رفع فیلتر شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22904" target="_blank">📅 22:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22903">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsTp3zPjiS3VyQvtgOBj5NLyIZZ7QRA2dgmk2lakvx2HQuS484AnF-p43pBc3tlNZyrlAmyYmpm1jDByRmtj9ImxJ_KMH3uby33g659ZwxxNvrw4d9Hdv5fKC2s7Nxgn-AtsYV-ThyiI1zOEgb5oukzpINyuEof_FKscekM_tMhSkSnM-OvAjE8PYX9dDBStTair7ObE2NhbDpL0rczi3mFMLHLobqP3Ff79ArB-DYr_YIqqtWVJRy37gTGrEM-9yKL-xv_DFU6oTYUd1usp3cfFrQolh1j1_fPgMmA0zuxjaXJX4FVVKC4VoDlio7dJkgtgCZUBAghkGnWFw0xTBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌اخباردریافتی‌رسانه پرشیانا
؛ ریکاردو آلوز ستاره پرتغالی سپاهان که با شروع فصل جدید چهار ماه از همراهی طلایی پوشان محروم خواهد بود به مدیران این باشگاه اعلام کرده درصورتی که محرومیت او لغو نشود یا به حالت تعلیقی در نیاید قید حضور در فوتبال ایران رو خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22903" target="_blank">📅 22:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22902">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhsJtp8HlHJ2ayvkDCnPaLqnzk_MHpLPjJNujYbIiRDJPcPpiAQ8yW_HCvDDRSNxgP9MsMXKpZPoygZqNM6KndasVVFSXT01jHY9yeFOGk8DexVZV-LvzGvwXOHv7BOxqkAMK4yYKQwNaXwoU9CYtEFjifjTVcx47zyjyJtqJd3_wGNvzoRTolxwsujrteXVXhz-g9GaAg9yWEJnkhQKfTzAJnVD8s8Jm0XUYxxvqD__hPpsKJK3lb3eJl3LVsg_N_5ALsGZGdr5gD6PR0kDBq1PGKDHtaW1Pj0yHS-fLjSZlWDyB7oelgnUD_-zbC7Hu_K6NmGf640PA84qnUfQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22902" target="_blank">📅 21:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22900">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBfsvKoly6_bLn28_7FiU2WZCEzBKrRzr29k6HoMkNjQDUcrpsM_xG5kMFkCs55BrocHlF-BlGW5MQX4HmJn239q7nNWG82GGvrevsCpYeMz4leZgdZGepXnJhtGAbZUyvzqo9-Qg8B_5y1PuArYukdOEGK-vmzMTg3rHDH9PS09t1G7qpFyDm-KuFITNUJrIvwfnw8Ar8Nv3U3ybTk2RRitXWnWr2juG3M7PSDsdqRkdC975wiHItBEetgY3NaDcn9JyviKLHDpk6ULfpYOwY0qxSauzqVZB0rOiA6EzYK5S6Yr5ekH8caZuOUdLZk8F93_GvtENBZANtfjO9JYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j7PQgrnq4H4LpvVi6UB4i3nHDdE3H0Fff2htHfgdngA8HpVi6C0zzMtwE35EM9nKLZA9q0RA6kF_FV4gatX4QMlDg4Rdgj6kCTEBnPKcGUI7_kkOleClRCWaZSGPCbrdGhCYbqMxHnyqGMAxf_mIZsxolRNP_n5cYmUs0hKXFpTZZ2V0en9FEazpJ1C7RI4WUrQC1NObH3sZoQdVxIbh408i5zPHLgIXzxo_-WYCBS7PQVyvEoihTW2r5YODe3tx5wrOAYl6edpotJqGHaUxuaiFyZigxwqdaKuI09tTRJTijxQqzOBa5urdFHDYAXmjizLX3NMoLC-gHdCMqWMmzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار
؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.
مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی نسبتا جالبی را پیش‌ بینی کرده: تیم ملی برزیل در مرحله یک‌شانزدهم نهایی توسط ژاپن حذف میشه، آرژانتین تنها نماینده آمریکای جنوبی در ¼ نهایی خواهد بود و در آن مرحله مقابل پرتغال‌میخوره و در نهایت‌ فینال بین هلند - پرتغال برگزار شده و تیم ملی هلند نیز قهرمان می‌شود. البته این فقط یک پیش‌بینی آماریه و تضمینی برای رخ دادن قطعی آن وجود ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22900" target="_blank">📅 21:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22899">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBSAeiqmRDWubKHCtpghixLQIz_veQ4FEuccDxi4Y8rfgiCXcsJvrd07LrQkC1BdowBN4Ube28re3Rlc7ddRml4gCBb3Y1zomIH4e_0PrDk68A--yi3Fk5ABmb-VjlyxdZ_MTHhKun291k6uoKs-EMvKtA9aQVCh1EMxLXNXKfZHAqhqlsJU6HRw6x_5IvzD9GxYCDkpz1szYNO2enrbbczSI2mbFS8JbcpxY_0lDXbiwKomscqp_1A_2UFCyNzEf1Ey5atQGJ-hnPsG3Up772wFj3Cwdh81CirJQAwRqeXv33SncwnJ0Om_7G-dQ3h4e51PetYTrfa2m2Tnn06i5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22899" target="_blank">📅 21:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22898">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDcjEtjTflPuTBoFKo6EBeWO7_TDG5NDKK8kglSccSpxIfoU6OsQXHrC5roEPlFK8kNmUOYvAulwQTO9mRdnO-R59_JG9DT_GZMPlyXEu_nXPG4skK-a9aZ3rgGqumnUaCpbgeos4P8-vbDbPu2RlAIRTy8qekdM0t-G3EaEh6QCkiOxJQWCCAQuDrQ05-ukdOi-_fydUymF7wk0dIgOc78SUlhdTHp8OlyXJnxdBQUcONUzBTgB429GwgIQuoOw1SVCmHFR2_W4URRZvlorkqu_HzW46qK8d_p0t7wda65ZKAgVh4VKDJnhWtHVM3dfjTXbxwnwqP85LT9OvKp6Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌استقلال با فروش جوئل کوجو به تیم نفتچی ازبکستان‌موافقت‌کرده و بزودی این انتقال‌ صورت میگیره و کوجو رسما از استقلال‌جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22898" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22897">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73008adba.mp4?token=HPpqGv9dfLr8jZEtAEVtpRREXZOfaTlpcpZFOSxc0UZD-y9qj23ITq-pUJht9A7az6j2JadjgawJCQ-JVHDeJZFnbSZAJpasVzWbqUXsxbE_NBxWR9k-xlSGwMb3G8QPnH3fCc2UIkpPI5wRj5P2LLI6_L3XzDTon5yPrZDvRJgV8qQJpTroP-dK5bGs0bZvSlcOm6V9QNsmsSGEmuuuRTZhfuL8IcUHflW_zHBCIBswfN0g6Ms8UaO2A1hGSY7BoLQ2nCUNHB5jjYjG0CHzTbvY4qPKIXEx77r78y-zvhlWCb3n8mm2eIFztppsC8iFNU1lTZWR5oPS-U7xq-l4Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73008adba.mp4?token=HPpqGv9dfLr8jZEtAEVtpRREXZOfaTlpcpZFOSxc0UZD-y9qj23ITq-pUJht9A7az6j2JadjgawJCQ-JVHDeJZFnbSZAJpasVzWbqUXsxbE_NBxWR9k-xlSGwMb3G8QPnH3fCc2UIkpPI5wRj5P2LLI6_L3XzDTon5yPrZDvRJgV8qQJpTroP-dK5bGs0bZvSlcOm6V9QNsmsSGEmuuuRTZhfuL8IcUHflW_zHBCIBswfN0g6Ms8UaO2A1hGSY7BoLQ2nCUNHB5jjYjG0CHzTbvY4qPKIXEx77r78y-zvhlWCb3n8mm2eIFztppsC8iFNU1lTZWR5oPS-U7xq-l4Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیکه‌مسی شخصیت‌منفی بود؛
آرژانتین ـ هلند؛ یک چهارم نهایی‌جام‌جهانی 2022. درگیری بین بازیکنا به حدی زیاد بود که به نیمکت دو تیم کشیده شده بود و این موضوع باعث‌شد مسی به قدری عصبی‌شه که یه نسخه از خودشو نشون بده که کسی تاحالا ندیده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22897" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22895">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOBQ7IFImwswuiMZKWw6SQLoFj2a8hD2TqnCvVZ_VEdF6K3e-iGDwtJYEMevV8DWcJlSeb9bvaxhnFS-Vvps3gwUkvueUaCEIH_EcYtJvJtuW39F7aUiaT9FNjKp8-VM4BNPRv9Y4IAoYuXrU041rRnvQ_aQLQdeDyhoZnxFly6bZSEsesd6JZtogvQZBy1ZHpFW0-tWqlJFTiflr1yxDTikSyft7ivGZ1GCc7_51c2AS6O1I36I67t1-6FjO7NptpfYr6SENI0_YAWjocpVMZ97FGQIzDtnTfQbOFbv1QCqQGmI-EeWOkpkg8n3b5wo6NUbZmpAUK8KlDT1gQMQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22895" target="_blank">📅 20:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22894">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=Ux6DEyXiSZg1nnorePiCtXeVSNPndQFuO3jQtMvY6v_GKtw2VbvvkKvC2fa2igqGgpN9qZZbyOxnfH32ozDIlM3jpi0omYuPpFJ7J4MUa9qHCMJFJtfK-DIYdxlOdMl2a-P4z7Y8ydXJIC-OF1ZtdbfFHMYt_zFmxY-YpmSRkSf2VqU9fW6ClL7boIYFdKsjXsc6kQaFTYYAkx-arEIMjDzUYBVh38_VMWAadWy5QDjOatmkijeVXpBXJyXsz0ZAbGfEzGMliLKn00D4AXMgZxMZzFm8AqyVyEtxJHcHz-THBf1MK_RcO80Flq7TCQjjmIKh04w8DaC7Ar3u6Ued6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=Ux6DEyXiSZg1nnorePiCtXeVSNPndQFuO3jQtMvY6v_GKtw2VbvvkKvC2fa2igqGgpN9qZZbyOxnfH32ozDIlM3jpi0omYuPpFJ7J4MUa9qHCMJFJtfK-DIYdxlOdMl2a-P4z7Y8ydXJIC-OF1ZtdbfFHMYt_zFmxY-YpmSRkSf2VqU9fW6ClL7boIYFdKsjXsc6kQaFTYYAkx-arEIMjDzUYBVh38_VMWAadWy5QDjOatmkijeVXpBXJyXsz0ZAbGfEzGMliLKn00D4AXMgZxMZzFm8AqyVyEtxJHcHz-THBf1MK_RcO80Flq7TCQjjmIKh04w8DaC7Ar3u6Ued6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇨🇴
وقتی بازی‌های باشگاهی تموم شده و از بازی در کنار هری کین میرسی به بازی در کنار این:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22894" target="_blank">📅 20:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22893">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZn8I9yTAuKXWI-l0YUXfAus01I95Wh84w49JhZnVBSEcct8WFnI2qQjlMtmpspoACCaaSgmW6xFHW0zZjiBwSjTy9nlzyThYEB8IEXvuuuBw0bCUGtjYPlQv_-Exo4-cFz2LcSttg2GmqNsk31kqZLd9hISI1kfnA3pP2dip0lQJu8PVk9khN6YoasLfZjHId9BcNFRC-6CkZlx4f93OZAjRvhdGq2YTz9zsFUWoan_TT77IyCyTibL9uhvTm17OekwaPIiWEXbhsQJdsk3LvyR9P8jhH0rBjVq7l0WZWqWm1dPVRi99Z3FIHMORDmvXGJD_5kFjwMU2XXmU_JLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22893" target="_blank">📅 19:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22892">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnnJd1XxBkjbgBWIDQn3PZRrwELIEvv-cRgmq5hGXqWJhjKn0xjYM4qqXJ16kjKZ8Feim5rISj9kDClowpXr8BWaO0danU_yR_tBOb-URd-5jLPX0Y93w6MnTANGwATn8sin03adfKJEDGtcjU-GsjTT8BU7Xk-jY24j86XMWDq3vZU4-y11zRHaAxpvCQ-GteH-0OMIGrgj9HUWrGwLtOIcBvS4b1IGPNi8-a78VFEAuGJziPj4oQBbTWQD14nmlPG6aCvwafGMlrOCtYt4miwAOQD4xBlTEaEAqWjiD-jBn3dSgTie7fHclgnXPL2m2d1Bg9ObQ-CQDU-rS-3uHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22892" target="_blank">📅 19:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22891">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=M3Ln5cidRHBbERdA9WFn5uWlHhivlpgZkFa5x_szcxSdZXnK6p2wB_xfxrkUuxAgeiyB3Wo9l19YlRaRcyJkymfUhd3jQVehuQmh2HIrg2PajOy44S_KVyuUTvpSxtD_K-zNGVMmcXrB7itmT1rkqX4JmczLACmlpstpSvKBe4eznWPYVB8j6KbgUYEjkomkiEU0SlT3Iw2EmcvgKw8OtFZrK5-xforA-rfRK8eFB4tjQzF0rfDuGci741pz4LF9WgvjI9MRWtte10Pt8El9485NdvVKH9VG_4IIXhIr9fytQV8bvF_cr3VPlMGil6vHf2NrOZiAAybq-xUaKZqIdZ9PJBmWO8kjlwI-79gdoK0UXQAHg60wclEVNsYCThBPo-yJdxAC2ccN1opji2VnDjx38tg4hCoVyyWhnDGUp9F2Q_XEc9ObUtfIs46Y9j-NpUHYdtb7zwASzksmVqk_-vh7K7wjhEIpTVJ5PNFXslbb_UXIaSBoMnqE4MHGmSRxBEhOVeyNeJZ_lYOZtc2nlOEeONcVnoda6i1cZWRStDCOTQBbCdiOadXFOerY89XXaabd5Q44oq_Z3yx3NY_bGXzBSR0xxFSgxv0Yt6MkN7DJLYxNLepd09wPSE9xi8VUlxuwL2TW04b1esKUsCmMB7sart0fiucnxbXF3xBpgfc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=M3Ln5cidRHBbERdA9WFn5uWlHhivlpgZkFa5x_szcxSdZXnK6p2wB_xfxrkUuxAgeiyB3Wo9l19YlRaRcyJkymfUhd3jQVehuQmh2HIrg2PajOy44S_KVyuUTvpSxtD_K-zNGVMmcXrB7itmT1rkqX4JmczLACmlpstpSvKBe4eznWPYVB8j6KbgUYEjkomkiEU0SlT3Iw2EmcvgKw8OtFZrK5-xforA-rfRK8eFB4tjQzF0rfDuGci741pz4LF9WgvjI9MRWtte10Pt8El9485NdvVKH9VG_4IIXhIr9fytQV8bvF_cr3VPlMGil6vHf2NrOZiAAybq-xUaKZqIdZ9PJBmWO8kjlwI-79gdoK0UXQAHg60wclEVNsYCThBPo-yJdxAC2ccN1opji2VnDjx38tg4hCoVyyWhnDGUp9F2Q_XEc9ObUtfIs46Y9j-NpUHYdtb7zwASzksmVqk_-vh7K7wjhEIpTVJ5PNFXslbb_UXIaSBoMnqE4MHGmSRxBEhOVeyNeJZ_lYOZtc2nlOEeONcVnoda6i1cZWRStDCOTQBbCdiOadXFOerY89XXaabd5Q44oq_Z3yx3NY_bGXzBSR0xxFSgxv0Yt6MkN7DJLYxNLepd09wPSE9xi8VUlxuwL2TW04b1esKUsCmMB7sart0fiucnxbXF3xBpgfc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شنیده‌های‌پرشیانا
؛ایجنت‌مطرح فوتبال ایران که ارتباط‌خوبی باستاره‌های‌خارجی‌داره؛ بار دیگر ارتباط خود را با خامس رودریگز ستاره 34 ساله سابق رئال مادرید و بایرن مونیخ برقرار کرده تا درصورت تمایل او رو برای فصل آینده به لیگ برتر ایران بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22891" target="_blank">📅 19:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22890">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=rWvSUEC-gfbfRM8_m8YGhotY8IspBhmpW68DT0j6Q2KIBMZFonDj2DdI7ivlz-BpdzwDI_4zUn5KrcgyaRFF0YOxncF2R0N2A0rfpPtD6JuSCb06mrRz3CvGQXwaAenlu0JwO1wiQOQLWMi83TlFAwsxPdGsEWO1ZeI7xrMa_YKYcmcs8zBP6zet0qDjKKSpI39O2BoBDD-i0D0V-hYJz7AcI0PMF7VfkCArhNXOkffE9KZEudCsHSdSuBPF_q1qs2t4RWV9Ey81Nw7b0mgIp9LuPNU3_2n36a2pYKKo131QlLC5XAxPLQhG8lSU51ynSYs5V7gchClK5modBv_qFk6r5puBppULeX3Aqq1DchV6c6ebmVsgyZA22FXni2kB17wk4kBy6V5UiR90DD4y1XlTO5cUBiE6s9bX9kUEC-KSoDy7q1E32ADNmKiAMz2LUP7CrUrDQhJ2g7_D3D3BaX7WXeh_f5fmfyGm2FdPnoR2maZl-pHDp1-TeHcrMU7x5jDNXmHHmFCDpm9TtxSQfpzBqIx7rwXoOfwaGL-kd8YBcrz-WOjYuehgrFN1xaP-vuRBNcyoUc74BrITiOhLAGkAJEO_R59efjESEJPiH4qTrQGryzKNnPPyRRMpK9FxbVl4T7TIieDBl4-fNUWVte4d5z947eXYRxwMRIRAct4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=rWvSUEC-gfbfRM8_m8YGhotY8IspBhmpW68DT0j6Q2KIBMZFonDj2DdI7ivlz-BpdzwDI_4zUn5KrcgyaRFF0YOxncF2R0N2A0rfpPtD6JuSCb06mrRz3CvGQXwaAenlu0JwO1wiQOQLWMi83TlFAwsxPdGsEWO1ZeI7xrMa_YKYcmcs8zBP6zet0qDjKKSpI39O2BoBDD-i0D0V-hYJz7AcI0PMF7VfkCArhNXOkffE9KZEudCsHSdSuBPF_q1qs2t4RWV9Ey81Nw7b0mgIp9LuPNU3_2n36a2pYKKo131QlLC5XAxPLQhG8lSU51ynSYs5V7gchClK5modBv_qFk6r5puBppULeX3Aqq1DchV6c6ebmVsgyZA22FXni2kB17wk4kBy6V5UiR90DD4y1XlTO5cUBiE6s9bX9kUEC-KSoDy7q1E32ADNmKiAMz2LUP7CrUrDQhJ2g7_D3D3BaX7WXeh_f5fmfyGm2FdPnoR2maZl-pHDp1-TeHcrMU7x5jDNXmHHmFCDpm9TtxSQfpzBqIx7rwXoOfwaGL-kd8YBcrz-WOjYuehgrFN1xaP-vuRBNcyoUc74BrITiOhLAGkAJEO_R59efjESEJPiH4qTrQGryzKNnPPyRRMpK9FxbVl4T7TIieDBl4-fNUWVte4d5z947eXYRxwMRIRAct4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
5 سوپرگل دیدنی‌از روی ضربات ایستگاهی؛
از بین این پنج تا کدومش رو بیشتر دوس داشتی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22890" target="_blank">📅 18:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22889">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWHnOLi99ZPVEt9JnxVZD9aSZf8NG8jwCB6p4lqix7uyXRq1IibzFmx21QZ76qBpZhxmJHNZGYSfGLVWMR1Q8PWneblZCvZHYKR0yup2n3Lo8NRkf5_xQeZStKi4Wn1i-Yjs5SMUELrJmmseXCk3eLFWgnJrRN4nSE16UEeHc68zL4kLnV7oU1CO6fQ1E_s0mFWLYoN6FAwv4pJTZWOVXwEj7aLN76p3DK8CkH3uXT7CaKCqPBxnScZ2sIxeLuqJ05U2x9yeViXqjVLc3fRC4W5h4O18lXG1m0V2F9O8RCNkaZICl_63bjPpUAIsYM5TMxrsLcWF6ISqr2ySC2b7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22889" target="_blank">📅 18:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22888">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=pgpqlPYYYGRnkYFR6mIyjMu9bUXtaEuZ7mzxpNGpOlu5aeUuNfa2sTBHfAp_wf0CHQFdidJmES6pWoCN-CYq2UHgZviuMs4OWr8nZiLxJh7RjuVR8lHvuAqYrefuCfNyYgrUSOF9R6MMPudZ4zA2098MSoD3dsfmKAyLbY76w0G70103zpNH4NpozXNaV3tcLWOcjE9lHSUitBANyFR0GdcElZYUOpvy3h3A9OfJbJMDv9py-7zgowrGUZRyAjV2tvRlhPX9tkLfo8LqDSXEnq31aetTWwQGkO9fbRqsK6HtSTQbyOboqHJIJMFkYwYEc4AhzM3oK2um972K7hjiTTzBqnixPLb_m5n4M7NgRFKZ6pH_CXk3iDf5zUtsXvXAan0OBRFZHF0dm0kYZLjoPRG8qPqEE4bJk7b8J6pZ0lwgW9r7jjShKnDIQ7KJY5FafFS9z60qVth728elc3URQa5HqXYLy7KYzmLp8dPkd_iof_UrDPpuJO48sJefyg5k-W6t9smmvdnLYSlfP7Vd_lmJBobA2XgjBS2v-T574ZxjW-7LR4BJ34sg4Z0yqLKaL5nA8-opYkHQlwJxNVAvgLmEx1Az33dGJSFifcYKg24yWGmiAmFI-mfdMxLmJd9iEg88aMlCcglaoB1JEkE7EsHytpB-mZoTUebatWYPfE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=pgpqlPYYYGRnkYFR6mIyjMu9bUXtaEuZ7mzxpNGpOlu5aeUuNfa2sTBHfAp_wf0CHQFdidJmES6pWoCN-CYq2UHgZviuMs4OWr8nZiLxJh7RjuVR8lHvuAqYrefuCfNyYgrUSOF9R6MMPudZ4zA2098MSoD3dsfmKAyLbY76w0G70103zpNH4NpozXNaV3tcLWOcjE9lHSUitBANyFR0GdcElZYUOpvy3h3A9OfJbJMDv9py-7zgowrGUZRyAjV2tvRlhPX9tkLfo8LqDSXEnq31aetTWwQGkO9fbRqsK6HtSTQbyOboqHJIJMFkYwYEc4AhzM3oK2um972K7hjiTTzBqnixPLb_m5n4M7NgRFKZ6pH_CXk3iDf5zUtsXvXAan0OBRFZHF0dm0kYZLjoPRG8qPqEE4bJk7b8J6pZ0lwgW9r7jjShKnDIQ7KJY5FafFS9z60qVth728elc3URQa5HqXYLy7KYzmLp8dPkd_iof_UrDPpuJO48sJefyg5k-W6t9smmvdnLYSlfP7Vd_lmJBobA2XgjBS2v-T574ZxjW-7LR4BJ34sg4Z0yqLKaL5nA8-opYkHQlwJxNVAvgLmEx1Az33dGJSFifcYKg24yWGmiAmFI-mfdMxLmJd9iEg88aMlCcglaoB1JEkE7EsHytpB-mZoTUebatWYPfE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
انریکه بال؛
سبک بازی فوق‌العاده و تماشایی تیم پاری سن ژرمن که ۲ ساله هیچ رقیبی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22888" target="_blank">📅 18:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22887">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miRA47l1wWbczRPUquI-zCnK1mQwugzW732wHJKDaXt0bmvQYMjCdL5HzcbjLXgc6rSap87JTSKD6d6XcaZV32TQfXSqGYzVdI-glSWLyzeF-a3PSPcYBZWAq_hPVK8WbtbFv1-3u92bS1_hy7KDB0fvtsr5Rq1mZYjxLZg0Bd7ssy5czbLrdCWhKAJX97kVL99K41FdWCAJi-xO07PdbugasY20EG6Un0MgYgFk7zJzJlztexZlfKL3RF7H7pL1rMjqjsupOyBO5Vr_S4NxXH47Gi0IUt9MKnD_ztSwvD71Z3B7uZol2u4PxzZpl3mNZtDb1sKsTwwtwxtn9yGvXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌ بندی لیگ برتر بعد از سه هیچ شدن بازی گل گهر - چادرملو بسودشاگردان مهدی تارتار؛ پرسپولیسِ اوسمار ویرا برتبه پنجم راه پیدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22887" target="_blank">📅 16:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22886">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=couni3_i9qN0T7yhUgK3g2JehuqYLkLEHOyWHR4NfZ2xpAil3QTmuneSmFZdhu0Y4yONJP9JBnlivyoX-szZpixoWfF3ZIUuVyPwFDXXOs8TeAY1oReopQJiKluVU8L3tThmiZMiRHIGKGFQPUMfQ8BL56_wVIEZHYHRHVR_MV9P87FH45K8M_x0kvRmVXpC6nQUcnD8pAHeqiDCzapDO_rBqMDVralNr58mkTjgfIfD_sSl_hZ2MKKwCjU1Rag_3JD8kct-dItbY2rPAcqgCUmWU86GtGFNEmo1Vxu879WDTYb4EUyRPI6tntf2jwEtEv593swhHqGHuBDHvuCgPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=couni3_i9qN0T7yhUgK3g2JehuqYLkLEHOyWHR4NfZ2xpAil3QTmuneSmFZdhu0Y4yONJP9JBnlivyoX-szZpixoWfF3ZIUuVyPwFDXXOs8TeAY1oReopQJiKluVU8L3tThmiZMiRHIGKGFQPUMfQ8BL56_wVIEZHYHRHVR_MV9P87FH45K8M_x0kvRmVXpC6nQUcnD8pAHeqiDCzapDO_rBqMDVralNr58mkTjgfIfD_sSl_hZ2MKKwCjU1Rag_3JD8kct-dItbY2rPAcqgCUmWU86GtGFNEmo1Vxu879WDTYb4EUyRPI6tntf2jwEtEv593swhHqGHuBDHvuCgPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد‌هاوقتی‌میبازن
🆚
وقتی‌میبرن؛ لبخند برای پنهان کردن درد و اشک برای رها شدن از سال‌ها جنگیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22886" target="_blank">📅 16:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22884">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cpwVgp9s1ofl4lYsp2EkBJz_jUA6zif5n_iZj3jfgHnKx0QyQX1WD3iY-YGyW9mE1fv1-fL68VYdkIkuOMOSKhnFYqzTihR4MfNH46kjYxPCCBp34vogzvA-GG41G6EBKsOhoHcOM5IMOuahnCDCcBNdTcquBpxSQ4ca13b2ZDFmwAungKbKCMgGfNmGBygHiNGtSebi5pFU6G0oKbIdeHT8uIp4uVSOSw9yz8tB6vyNn9d38pqNzGWvKWUkJCL-u6kCju72oC1aomW-fXLeGOB-4I8_kcCIptYnMdXrzGqPYdMlsJvcd0-W84qFzm1IGT8dWDhDfR8MUiG-UEFRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDNB4M1cbdq65D57DNSKXkhubEMMR51D35MjrnSvpe3ouHgYqKDrr1YNSWHnxc603v1GtsClf4YlSgRIICJ0QZhz22OVAMOpVzha28Xu7PTa719jEf8wJCDyBJXTrMqltVlZnKFXgMWQqpzEJ9tUEY0bkWmBZRnGVhAGTQbHaF7EludJWocdbq-ght9207gC0NK7mUMWzvvf25AhfXNMej3gKvRQwbNqK65137a7n6RYn4RbNmVF5XFZK5Z2Tnbq7y7m5c9tLkHu-GYSoksnDLYtTCrewdPfNXgTbbp0mex6QsIRLOXA-Ikbp_1E7iYAY7WWgme_Cm1D3whcbd6bhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🟡
🔴
#نقل‌انتقالات
|شنیده‌ میشود آتوسا یوسفی خواهر آریا یوسفی ستاره‌بانوان سپاهان مدنظر تیم بانوان‌پرسپولیس قرارگرفته. آریا هم مدنظر تیم آقایون پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22884" target="_blank">📅 16:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22883">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej23QF5MfeA6CJPNGUhPCrUNMsRhyAfOy-4IFbIQ9aetVkCPi_Ro_HG1l5Nqy1awhvZ1OyIP5HQvd4jUUHjNwOAWuT3KMc1vw8PKRRv_-dGGq-qByVDpTDrEIOuIqNpJellhfL1hKVbbDsCks7Ctms-fE_7w5ofKGvBOo0WkYBqEpYqxgbAa6jsMNuWgB-hBuuWwm6UHV2-InWTkN8dU3emtirOeahHJ1uIF1_ceHHCX9jJsUVVis1NbWN7WWQ5HdMop0DbVedXfS9FBULO8yltr_K-_-Td-f8Q1VK6RRNnrbiVgpBfy9fsqaY-tgczbMM2i5XDUvx8o_MBsPyaEyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#تکمیلی؛دولت‌آمریکا: به افرادی‌که حضورشون درجام جهانی ضروری‌بود ویزا دادیم. دلیلی نداره به تروریست های جمهوری اسلامی هم برای حضور در جام جهانی ویزا بدهیم. ما هرگز اجازه نخواهیم داد پای همچین افرادی به خاک آمریکا باز شود.
‼️
مهدی‌تاج:اصلا درخواست ویزا ندادم…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22883" target="_blank">📅 16:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22882">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uau4_XtyLpsg9qxtyytnTNjMl_V2tV_fbRmqrDeJqcbY1qd6hZe6C4Oipej-q3bEocOcMnk1hKqh74K7akSqAqNaiEEZdjgx33r0dBf0ByvUa1vvVF58Rmbcsux3AL2d0V0veOK4dhFk9mb-NODkbGscnKN9GGQhJJOfn8g4NkpstaX3eM5cKZasYICDYwicNPXUzYIBz-VEJhQ5KLp6ZfS3UCMaCNIEDSyuVL0PZB4XAFEvItjAODAGkgCsE35XMXAzYWeWGhag47orOHo6xOsijvamta2OXgTKhTIgyFXLRpm0J0_Bekz90tlOnGlnlvEbrsVm8_lNkFtPH9TqcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22882" target="_blank">📅 16:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22881">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qu6JvjiGOBWoiCa-p4HYWJ-9eAKn0v-556morFtYpXX3kttl1mz7a8DyJCGFvZtzv8aHgNOy2sZMnQPF1NhQAkv7nVWgJxS8VrgUfo18neNnVGEocPLir-Kc7MAB5E-ofcOdV2oyMXwTtzf_WDr42YWEVPGrAd3L_2qPFbMjw7xmiRohbBEPWp3R_Pc4M1FZab-VVfxs5sp2Nis0zFemXTxttti40qAuLDymo4sDo1zfBlTSuXaNubBSVL8Qzk1kRaiJaGuCvqsRfn0MdqL22mkuV6jfFP7Bsv9zn_xCmx12x0gn9xpUnPBdS7A74wvOkL46qcG2EC71Rf4O6OMdhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22881" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22879">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cibEcDIGfT22ZyDlYPb1WbYMnlkf4Hhh_sNp5BIo93eixVwEYgZE5y2BGS756c40362rPC0RaWzANI2_0SpnsfJ0bodvND-MAbvgSct7D0XQYq5sH901UYdI-78C1OYJaVbxMcXdkDsM5qnJBONfWc2tepCFCygcY7bW_ss48e5FS8maBCcxcCFOLC8YP5iXCGyw_ain96sYlY9Vh1peqk02udViTisbe9Gm-weXXEK1dAn0aoRZ4wtyUZfN9UtQrWkgls8qbbnAHWxxPrkIkuLX00lMfQ73UqsDjN9V4FdjGNcEhtzqtxhWJ4Al48i_iAGbZb7jjq85p2lAD_lyEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ga17V4ZVAryoXuQtK5_pg1kY9ITNpLMHmfmj8sXo9ipLb4Q4V1Wwx3sU0fPKBuSnpAfTT6T-WWHwJ0CpPHlmrS84-snlrDsDw5QJlDsaGYwTx7QT8zu7p3OSSjVL3wUaQNnlzEYptZgTAD0jDLoGFyWCTQxJZE_tNAw0Krz0okDAuUce9tHNMq9NDvqk6h3AXMN9ZWyvRa_YyuzRlXtoegB_3aGoKuuJill6SWn6XWXCWf_dmaa0ADSjLreO8ljkkH3KxouwWE1GOwPuEE2z5LOGYS_adoFjc8Xx8GK7ldEMnldAhTUZmOcfv8wtWREA1qktnyjP9ShnKZbjtA1Hsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
خط حمله هشت تیم مدعی اصلی قهرمانی در رقبت‌های جام جهانی 2026 آمریکا
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22879" target="_blank">📅 14:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22878">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWoXO1i6RN_UBt7pj0YGWcxYoqri5occ4a0rIhGBZFgNLe2ZMIEqQPHggtU0tfgJhhG2s1OOzo5uT9wcFXkqmAZ1LUO6i_g5s3xQc7biYaCgRAsD0PO-Hfh1DPEMCVtwEYxOMBiWOBshtw-_4agHbQQ7l2YwjQMqrZ6HRcZRi6d9OT73yf6sdHPOXsikMm1KeRc9rZlCBGKS9i1Kj-kxYHOLfbYeIaJJrgA1VM9SfMvPw0rRexg_Lqk2c7GdmmM_u0IZWQLrUGHuULsa41dmUsJHBf8YDfgoFzSuW-z8hps4XptVxh6Bbyf0rKLEFudpD1Hpa8kw9eQ_1S1vT892-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22878" target="_blank">📅 14:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22876">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhRrS8PSkW9ffIQ5ac14FjhJOfWw5PQKP6VpjtTnUJJOYlAIUPVJAmTNB2RinxZ3MJfa8qo5ImclYjDBHs9KZOUJuHP-hj3WmuMCw5ap-bXuGAiPVLRoNuR40I2nhbbw-Dp3VYljRoPz91qpJDzJZohv_sI7DAMNmNbvNClm3D6Yzb7YLYRqOdv2126sYNtil70p8IkU433ewaJfRViKIHEej1twOKQ5R-PqNIiqzgu5gehtdqImUEw8XfK5VelK8WP1hfnYvI60PXcb3DtCUOahzQqRZYPcq7-xti6pxlngDht81trqDXoz8WVrMhXhbjZPlfq4dv8b_3HG81Ss4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال با مدیر برنامه‌های موسی جنپو برای فسخ توافقی‌ قرارداد این بازیکن‌به‌توافق کامل رسید‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22876" target="_blank">📅 13:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22875">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=AuOL2UbF0OP7j5_fzzeqL7WjcBMZxxKPCGFlgiacxvkIfLGVaYQ1r1ItU1G1nF_XKAxNROApEE0kw92GcEeqqbvIQy8DD7H3rP-RInqJI4ayT_uVmy6y8CRaBdXvHCW7wBRW_0EGDY46MzHQ5aXkgz9I8rzlvkS_jQLyQKmZPqw6TI1-Fn7G4zPbS1zV8kjOrYP3Npu83kyn0UBtmonWCUr_fptcFWlmgkzIiQVCGSqQZw4uAqgKKIxQ48dwAEa-TFeds5OPHWMq0DFG67ZWpdr7kexwRf_Lkk1BrlEpatTHIGXn0naCwxXuFvLoyshuW_EL8FqKIoYctD3dBeoo9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=AuOL2UbF0OP7j5_fzzeqL7WjcBMZxxKPCGFlgiacxvkIfLGVaYQ1r1ItU1G1nF_XKAxNROApEE0kw92GcEeqqbvIQy8DD7H3rP-RInqJI4ayT_uVmy6y8CRaBdXvHCW7wBRW_0EGDY46MzHQ5aXkgz9I8rzlvkS_jQLyQKmZPqw6TI1-Fn7G4zPbS1zV8kjOrYP3Npu83kyn0UBtmonWCUr_fptcFWlmgkzIiQVCGSqQZw4uAqgKKIxQ48dwAEa-TFeds5OPHWMq0DFG67ZWpdr7kexwRf_Lkk1BrlEpatTHIGXn0naCwxXuFvLoyshuW_EL8FqKIoYctD3dBeoo9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22875" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22874">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2YNfT7CPwIY-yolw0HinlNwyQK14VLr93bL9rNBZrVa9KJwfthCmvIoHXlozvXqbJGxF9IzxS9FyRq3GKOZlCP5CyVEBZXF7lvpQbxOs1CoxKoQasMSLijmx0VQZr8B535aMMLlQmsy-DR4Vs7Ni7vegMJ7wWfv8EfO6nk1npsdiUDC51-IJBLxie_OgJxd5l0vAbuENc_Rz0c87kdyoqZ2Pq81Xo5mK8CsvNYqcAx0k79IrWeOpSUf6d1Ukft_zh9Kj3vGfaaXV_kTOfmU4Q71--vq7vuIMh9BxVvUdM5wgzRWnde_BAMuGw1qi0MOMXzTwJ7ScEd0b6VJI2WuTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22874" target="_blank">📅 12:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22873">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IV9vS7X01V1C0OAUGAyRXVcMp4t63ANWXC1O8fwqzenC0tUU3Sidb3S3aKtr6Kidekml6fL0f2XUpCmri8xXP1qAiTDh0Z4nYkCtApVFp6WEEcX30QMQTl64cU87lgQLaGC5MmopXrJLpCorvGHh_mxfGZXLEj82IHXGTIZBE0TmKdJ5F3HCq7QWE0VffQ7A-Nj588Z-73q_-cKUc3xQr5c2m6nwy0_AbIuoDYQMBPMHoNLBWheRNZxeEmU0PjukQ8n-bwzsVw936hr7gMBO4vflms5_5p9Gs0Cp5wub141SolG8YkvRZA6BCEnMWWNsNZwIwYI582tO6mk-hXrRQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
#تکمیلی؛باشگاه‌آلومینیوم‌اراک: در روزهای اخیر مذاکرات مثبتی با یکی از اعضای هیات مدیره باشگاه استقلال برای فروش محمد خلیفه و بهرام گودرزی دو ستاره جوان خود به آبی پوشان به توافق کامل رسیدیم و به احتمال فراوان این انتقال بزودی رسمی خواهد شد و پول خوبی به‌باشگاه…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22873" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22872">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQRLj97AcGkGLyIaNoU0b-Yo4oShsJB-ZV5egaGkmp62J8k9yBJgJHlrTu52mCoQx4Cd8m82WuyMQbGFH7BZJ2aWLmBsnA_HFWsfDl7OQAuZ7uaEImWNxOEi8jIdtras79pj0kBpja-mEDAleqMfisNnVfEZnhwxpD8BohxcrPH24zF9WaHRKFi7jJZGxqTg8Hj17XHJQT-LK4CpOzW-w1n5xTurF4Pmo2ZmIfMP8bZhvAJGoQ_fIPvLBBmKvgCMOlm8VM04XTaQ00I0JyK6dCdTzL16stTW-c-K68_WiQtT8-GsOf_gEjDFHpVMK4im68ilcGVtjym6VwZC1htNYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل‌نفراتی که دولت آمریکا براشون ویزا صادر نکرده و گفته حق ورود به آمریکا رو ندارید.
‼️
مهدی‌تاج رئیس‌فدراسیون، مهدی محمدنبی مدیر تیم، هدایت‌ممبینی دبیرکل فدراسیون، محسن معتمد کیا مدیررسانه‌ای، مهدی‌خراطی مدیراجرایی، مسعود اردشیر افسر امنیتی، مهدی ملک…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22872" target="_blank">📅 11:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22871">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdPGKu5mzM6uNxO3NCkUDspU6UMKUwHVqPlbbYGA0pqD27EJhgZ3aAGDLbLQIqiVXd17VS9gPIsSwnLGAJZoPkZ0Y408Lf_lN--rbSYdnF4wq94ChPaDFqFIm_CeSglX0T-d9LkUFgZ--NRBvTBENOJyfZ1QuOqSh8CLiBqaPFN9Gzokv667HgduB5Yl74DcUZQ2Po2H6V64DsDh5yjbojgYqNypFuhHqi5epmLtduf-Lsb_MYDjhwCzIWqN7B19scGSWaH7TIzP1Dw8QKyeGYUP4APhk4-uWWdH59iqNgUewczw5fj9fR2Nt7IdypLSP__JV9ty0I1tWlWofEA3pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام رسانه‌های معتبر خارجی از غیب احتمالی چندبازیکن تیم‌ملی ایران در رقابت‌های جام جهانی 2026 به دلیل عدم صادر کردن ویزا از سوی دولت آمریکا به دلیل خدمت در سپاه خبر میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22871" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22870">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=rK7HW38znZeduUGe77taNYXWL4iHmAc4pkot7dQLt1jLy8tEianX-vvQvC3t8eXfSsU9oP1oR5G80-1eIrtta8gQiPYBs1IEWBwU00B_FxjCoSBwdy1XEENoxphdsZ_Rk2eB4jCPcCRnvpwnSbYwi5oEVnE6TEnYb8z9cvDk9LjoDbuewSZqunBIeOdIw_78gKYwMaQDx8CPXY4I0AsGzCSM8gMoUpoUYo_ViLB8HW6o3o5z_FvfNo4Lm7G70YAEvy46qVssOE6eVrNIjKqy67NyGPCOdtRdTFiLq9bSazXkfI4HOIiqJiwUf_jUaj7mpx37rzt7PB7julkoOvkyZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=rK7HW38znZeduUGe77taNYXWL4iHmAc4pkot7dQLt1jLy8tEianX-vvQvC3t8eXfSsU9oP1oR5G80-1eIrtta8gQiPYBs1IEWBwU00B_FxjCoSBwdy1XEENoxphdsZ_Rk2eB4jCPcCRnvpwnSbYwi5oEVnE6TEnYb8z9cvDk9LjoDbuewSZqunBIeOdIw_78gKYwMaQDx8CPXY4I0AsGzCSM8gMoUpoUYo_ViLB8HW6o3o5z_FvfNo4Lm7G70YAEvy46qVssOE6eVrNIjKqy67NyGPCOdtRdTFiLq9bSazXkfI4HOIiqJiwUf_jUaj7mpx37rzt7PB7julkoOvkyZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اجرا‌ها و موزیک‌ ویدیو‌های شکیرا برای جام‌های جهانی ازسال 2006 تا 2026؛ کدومشون بهتر بود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22870" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22868">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLvXYdTHJnjllkHM0-UPE6HbRbMxiz3pvnqjuriyWxxCBPHU4H38uyeshf1lojIaFl8Vpe2x2FZUTHFzUL_tZlJJ3K7_GyjfAcPUC2ErkFef76K3slLmq67CGzx2gxD2DtEORnl8FCYp7lfLUBd7hsOrQxmOS7nJtvuXLQnzcXSmcAblMnOpQtAdWffv29PQ3nkkOIrWRtQWns3vhfdDhDnoHaGx1GkIqb8dCkSYI4v9ZtVNq2kTBodtJAujGhM7silHMz1SYWga4ccZJceRI7oTJJUTOgQsw2yFP9VFlYdP0_MQgdeLnD0DD5mMLCsae7J1hNKTSj3hO7zUocxRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22868" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22867">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Evvc-XuN5oqx15FGDmR238kx3_CPTtHYA9UnwerWPRTHppBNAzzYwUC1P4AN5XKqea1RIMjGvpKCTqo1_ROsgD_8VjEFhVMzPqGln4Xqv9qbLEB77gw349WZyIxvZtYj8TAzt_h3s_I0R7mdPCQJE60q6ndEis5s4rGb_BF-H_oCDxomcsYR9ANoxKmQjLXhfNc0WSzXHaFvKPAFqVZqTJUBDCpm6KCjAYXpjEhLWJFaX8LW_hccxwp3LFmGEctt5OqYA4bjPB-qETIPuiCLgMV6RcP0iFJuALLvPk_PnTlpKHa_FiOJjvZMJRT1FndV6da3-1o8qbEGEs3cSELGaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22867" target="_blank">📅 11:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22866">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=a8hq8NcNQ6dPpeFDgyfhXmw1z5mz8ZB0_5f3A5S1fFCkmVe-txPWLOP4MO3nk57AcI1su68E_DCxedkzorMGyARSpIymE9OCqZrKDAkQYnfuwkeSEv6otlbUuPzOzhp-AHQyfSzEZgpMkASyUSylQBz0Bjmhs5DIeHJi3E-TCZpH-xjkrlsV0jFefDFYoGahcU9gnLD6KysmVXh6Vkh8MRyTzSU8vyNrbd9ejZUHcCXQPS-jLt_nw0lFFf16dmopppwsP7pWL6mv97ljqyC1Qw2TznlOQs4lMaVM4DnBqSLL6x41j2HUD0_q7AA1NezsF-Xu3Gm4L8-IPb2LYT5Rbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=a8hq8NcNQ6dPpeFDgyfhXmw1z5mz8ZB0_5f3A5S1fFCkmVe-txPWLOP4MO3nk57AcI1su68E_DCxedkzorMGyARSpIymE9OCqZrKDAkQYnfuwkeSEv6otlbUuPzOzhp-AHQyfSzEZgpMkASyUSylQBz0Bjmhs5DIeHJi3E-TCZpH-xjkrlsV0jFefDFYoGahcU9gnLD6KysmVXh6Vkh8MRyTzSU8vyNrbd9ejZUHcCXQPS-jLt_nw0lFFf16dmopppwsP7pWL6mv97ljqyC1Qw2TznlOQs4lMaVM4DnBqSLL6x41j2HUD0_q7AA1NezsF-Xu3Gm4L8-IPb2LYT5Rbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تعدادی از هواداران پرسپولیس مقابل فدراسیون فوتبال جمع‌شده‌اند و شعارمیدهند که پرسپولیس رو به جای گل گهر سیرجان به لیگ دو آسیا بفرستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22866" target="_blank">📅 11:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22865">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">▶️
هایلایتی‌کوتاه‌ازعملکردخیره‌کننده مایکل اولیسه دربازی این فصل بایرن مونیخ مقابل پاری‌سن ژرمن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22865" target="_blank">📅 10:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22863">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=RMB2TYMIlHZPybd84hKikcoXdAKtnT_Uo3eUfYGBioLv5F20HZ-Oyx4YjPBwfNZDKxf61sWzoy1opxFyzGchkB8MdakX_VtInvBI_bSUZAxSBONeymHgN1lnBlL3FtHT0fpWyQSUTYx9-fTCa9t6m1Bhom3HGqPFpynQG-raJXzpTnBoTkR1DC8ISiTNSaHUsmrBsitdthg-dKCvfKWItjI0yfHvmifkzgTvHoLPLvbJXGbO1I1eubMG2sW7QMc4M-zEt-9xP3RyoJ-TCmAnsWaYPaeIwskdgx2Ol-PVuBd-Eky4sK-fOdyUqWEi6_kERZbOFVtxCFl6rpIMDonyZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=RMB2TYMIlHZPybd84hKikcoXdAKtnT_Uo3eUfYGBioLv5F20HZ-Oyx4YjPBwfNZDKxf61sWzoy1opxFyzGchkB8MdakX_VtInvBI_bSUZAxSBONeymHgN1lnBlL3FtHT0fpWyQSUTYx9-fTCa9t6m1Bhom3HGqPFpynQG-raJXzpTnBoTkR1DC8ISiTNSaHUsmrBsitdthg-dKCvfKWItjI0yfHvmifkzgTvHoLPLvbJXGbO1I1eubMG2sW7QMc4M-zEt-9xP3RyoJ-TCmAnsWaYPaeIwskdgx2Ol-PVuBd-Eky4sK-fOdyUqWEi6_kERZbOFVtxCFl6rpIMDonyZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کیلیان امباپه: همه فوتبالی‌ها قبول دارند که رئال مادرید بزرگ‌ترین باشگاه جهانه جز هواداران بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22863" target="_blank">📅 10:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22862">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHtYVW-4t1cdXq06HRMxtEWdUuskCONKs5F9xdBlTNjVmkQP0vAXFF-ormDyEi7gGlApMu7yp1vjmCbT-rOLqGI5_5axdRccInRfzidbQ_ppsXXJlZ0OkfLorxB9gtj5Ak0S1B4s0nmZ8Jyq4FhDy6SiQPSTlQ2WqTinZToUh_Q2YP7ZZ12HIyM_f7sN0HTK0rtjuk04nAutPhzn77eFIuJ_Zhv02mgQ8IfMV8yD8DjlVj8RH96s34j5p9RCxJbqTVTIiZAjSX9ofpsLWAlpII9IKn4GBpwsb5jF6j78wOXE2czM0-THVdDpXNPYqXiXaNCBt4I5_0_9hI6aEwB6oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین‌سرچ‌های‌ایرانیان‌بعدِ88روزقطعی؛
بعدِ بازگشت اینترنت مردم اول دنبال چه چیزی گشتند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22862" target="_blank">📅 09:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22861">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=IY83QOuVQHSY-9Uhoi-SAG9CXdbd4ycSG5axF8uS4FiWmSijXA246-1NXyG5u_mIxLF7rfdeMb5lmIToPtxh07W-gxAI-2_in-E_iductJr_u0y5bAr47f4a6JXuiC77OA7BlMFRVEwEg9tSyQyVWHSxBBnvaGXDR_p5gVxY-eOk-sSN2Jhh0Z5GkMF2hkF3YpUVOLeLEJw81LIRjPyFYQVtQ81tlSWFA7F_dr-MMuZZC0qfDsBwNb99YRJ1m1nOmEcFjrc2iY9AbvPt3oe4PWEKJNjrOZljqKBpdYaWXswVWaq3BatF_zBVD2pX89D0iKk6ZaV3QmCovg2q5Fq7fXvcbxflL9A3ITZ4xB2TqSpsx148EeEwEWTSyrbhmC9Pbv-ndbkzmh5CWJPbYB8_R3u5wNU1z2G9tuNS_CNrtDkARCrUiGLVJ_J7vCdUKp-O8O02p0HWY8LY9CzEt4Y0EYTo5D4KVRp_Zqaq1pxkhvuCalp_AoGqDAxpDF_4CJ3GTnZVDImftxWGrbkNum3kHk3xqrTIKCqIDOvVkq7rjGAcwL_9c4LVNd_NBx6JbXAYIYjmZU7aQBGPSbAA7FrkeORJiExBs-PkDtr9AWiokpmG_bEEwyL9J90FVxThhel7ZZvljB6dtmx1O_fjGBOD_O_7ckK6tzYanlwcI1L-R-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=IY83QOuVQHSY-9Uhoi-SAG9CXdbd4ycSG5axF8uS4FiWmSijXA246-1NXyG5u_mIxLF7rfdeMb5lmIToPtxh07W-gxAI-2_in-E_iductJr_u0y5bAr47f4a6JXuiC77OA7BlMFRVEwEg9tSyQyVWHSxBBnvaGXDR_p5gVxY-eOk-sSN2Jhh0Z5GkMF2hkF3YpUVOLeLEJw81LIRjPyFYQVtQ81tlSWFA7F_dr-MMuZZC0qfDsBwNb99YRJ1m1nOmEcFjrc2iY9AbvPt3oe4PWEKJNjrOZljqKBpdYaWXswVWaq3BatF_zBVD2pX89D0iKk6ZaV3QmCovg2q5Fq7fXvcbxflL9A3ITZ4xB2TqSpsx148EeEwEWTSyrbhmC9Pbv-ndbkzmh5CWJPbYB8_R3u5wNU1z2G9tuNS_CNrtDkARCrUiGLVJ_J7vCdUKp-O8O02p0HWY8LY9CzEt4Y0EYTo5D4KVRp_Zqaq1pxkhvuCalp_AoGqDAxpDF_4CJ3GTnZVDImftxWGrbkNum3kHk3xqrTIKCqIDOvVkq7rjGAcwL_9c4LVNd_NBx6JbXAYIYjmZU7aQBGPSbAA7FrkeORJiExBs-PkDtr9AWiokpmG_bEEwyL9J90FVxThhel7ZZvljB6dtmx1O_fjGBOD_O_7ckK6tzYanlwcI1L-R-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
#تقویم؛ یازده سال پیش در چنین شبی؛ بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22861" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22859">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D5_tkp3wjAhLgjmGBWJHRKNxYBHk9SS-VD2w4IQIi30Vj9e5mvL5pWiUdoKmXWh0phkMgwV5e1_D3XHfd9pqbtoGuUjZ7CD_bVNa5nPRo9guRP7vIIhjCC1E9dNhi_RGMLLAN6GtjpUFfboKqx7sfPiBTwKyVluwHgbcpN1VdVkOjia8yJxL_NLklwj12DdqtxC3hHF1VmmyX0BEyuJRn35wyKyjDWyRfxBWJU1z2-ALG53907SBr1aS1mdqWxUZzCbcNoVuOTfZqL1jPqlPj5Mfi9ojhTJOiDQMNh6wvIHGKU-qpaQFs7Sdy8-AkjS3e-dp68pOQziY8PrLzFpM-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MzXoiMi32xspJO-QjHZGQRm4KN3iNG1_G1g0Gvg0WixgyeoSqsmNmeHnsDC3B0otmaMUAI4oVsPMrgcj2kKn3FvYYVkuDoRl3vTf88A2e-1bzOTcUcHXV0pr1NN8z3gVrBepGSNHOeV9MQLlaz0QMZ8idD94lAlOYmyTh3uGD2VftdsmrxLfREJu2IN9n1liAJRSVwxzIacFXFF9IMy5Lvw3JO4ONPAt4zjkJUOlU0gi41KNQ0oyNBTSC4KjYWAQMqdZMV0X1JQeg0CBmkSTqJa9Dl6UO3BKWnefFg9BrcQOFgcvEwqa8CiKagnPs1upSpEjHt_8efrhzQx9Azyr-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
#تقویم
؛ یازده سال پیش در چنین شبی؛
بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22859" target="_blank">📅 01:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22858">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tU3tOcPIoF9K-TSRMU8nzTySZK-y-Ot7kJ_bX3JMvKrL3tg8XwkdJBJUnSd8MWCrKqEvfY6sX_puelNCgW6x2sYfTAqjOtaqKQkZCQRZS9wt6cF1r9ZxpaWFWE6pRJo683PcViKqrx00izvHLdtmCDv6ROQqIaBViG261swgcfpmfd55NKAYn4vg2VCDZ1oywYu75nHs2_-3Kf1Hu8dVCTsPNrJcI8qMGVCg5xeq3w2mY5XQTcmSWAgtPXmAJRZwC2R-4oU13NNstj10Wlsftztnz3JvOa9Ezh8mCRL95yLCyhSwuP1HJP0gHTz0AwPhpcIzMRS5lAgLfW-OJwFOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌کامل‌دیدارهای‌‌‌امروز؛
ازجدال‌یاران رونالدو برابر شیلی تا تقابل آلمانی‌ ها با شاگردان پوچتینو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22858" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22857">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOrYo-el_t9UNiljjR9cicXJEq81-9SnKWuqyq8mosV56C5JyPatH8WeYfDGe7_fRCXol61hic7uxgU4wwO7cDU0F4y4Gc0QVlmIrOhLXcq_PqctkdOh9NznZVM-RZgJXgKrthDCt2X45hhFp8v8IPXRji_LupTKHVbsd81Bo4Qd9Om9ebWzcZy6Y3-3-3jsM95LifSLyALb9nDNhtenxuL8WZUvn6ZeaRn-PMEsS1OKsvI1QgLy1yG06yzqfuUUXnjZeb_DgSfitIIeVReQajCK31Oc84aNHeUtjNangUyxNncLmFvcxJwxUJhWBv5MK-MeufWyazmiTgabKjUMbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌ روز گذشته؛
استقبال مکزیکی‌ها از جام‌جهانی 2026 با جشنواره گل برابر صربستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22857" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22856">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDjlK4L7coTfqf4OvmrNBj-PROlAW0JM5TV3XS8CfzCt8QW0Fe9JTwNQ6mMaKoOog-xb1ydq61xo5m55swTStX3R26i93fx5KeAFekriYZV7wl-DTrS_DyEA0Am5iSgfWbUzW1crrySAeHUd9PfNAefLNyM-H5H205J1Yzb_O4T_Uf50zO77EHl8CA_wWe106FpcmHevDgp6-b5Iw4UHdRLRgw6J0Bph0aVTFYTrio-kUUei1te5a_YKf1bvTIptDjHXfJ5AFN7Vfic1QiQwvvuOT_fvAo9jeuU7tynCh-OHm7yhWajuazE-2qNJogGwcG3dCOsit8Wt1w4DflMeSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شوک‌دراردوی‌ژرمن‌ها
؛ لنات‌کارل‌ستاره 18 ساله تیم‌ملی آلمان درتمرین امروز این تیم بشدت مصدوم شد و رقابت‌های‌ جام‌جهانی رو از دست داد. ناگلزمن سرمربی‌ژرمن‌ها بلافاصله آسان اودرائوگو ستاره 20 ساله لایپزیگ رو به اردوی تیم ملی آلمان دعوت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22856" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22855">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeX6yryPK3yOw9jjjawEcVHC18-P2efjH3XZ_XlGytyY8j5KwOGcUvJt17LK7OZvMwpadUaeNEdyH_QQA7ZA6saQ1T1wjRlj2rThNap-9vzDBYmJYoUvdeiyYfl1qd2KvmCIF6BRGyJ9bw7GkGQtayY-MH2o01fxfXl6xOIRZJ1bcjthaGNpWWMTglTJw2rWz6ngeEx5-UM7Pzl9g13PebkCvxXJv4l7arhMuvmws8pxGYQJBZXoRzyjX8UR3gvxFWhAbZvgFcwayMvhxjD2BPcwBm2sQQE7GPJYawanZHZ16rMCkNVq0wgGLhHOOsNdVK2eboIIQ14h5jqplhBJqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22855" target="_blank">📅 00:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22854">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSx45ueRi8qZkk4iGQIk9CDbvdO19nGbKlDvxYO8MCwvnnqZNcl4mvWe_bpS_L4d_ygkdtDl54G6mFyapGb2VOV4IOfGSVn4-PLIamnhCLTh1sTMx_bzzw3Wa3tzWXrkMZAVt0tVwjS6YZP_OHPOzOzG7F2f96gTm9o-JbpLVjpBeKxYhaSweCkPV_OzmkROdZLMGgOQU5avbRoOLlrJ-T9VKR6c5-YpyWwdDPiXhNjdwMhuPVLUMYaMfUROiIni4vmlMZk4o3NmKiuOOZUqSWyGpCFoINMGpUbLf45LKPKap_FpaItBSPPua5Wns2tLZXxcjUIAwbUlX_fpL8NG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چت‌جی‌پی‌تی،دیپ‌سیک و گراک بدون فیلترشکن در دسترس قرار گرفت. همه برنامه ها دارن رفع فیلتر میشن جز تلگرام،اینستاگرام و توییتر؛ سه‌برنامه‌ای که بیشترین استفاده کاربردی رو دارند باید فیلتر بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22854" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22853">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=dw0P9fd-9-3EpmSpm5sSPC1yiJ6q88_pC8ifCmkuf-lV0fK1ssqY3L0xXuLWPTJMVbE2CCRaXUB6-dSzjckMa2Vmx5y6nPqBJ89E_a0Q1L3kA-7mpudUmQcGa0vrWtxylpWK9wc0mE1FWeNTHpuGD1Udr1Wavgy0Gj6sJmwi2UojM0V-h7KI8orH8d6FuteIyLLyncDgLhZmBNEH-HwXhDh4Ir-CA328nwCQpiu2bbh2Vn93O_ETYCr2Oke_nIQCrC2VIsaZDta4OcSryRAV8iiKolxNHSpNT9YZN9jt-wdzr3fpwINpvVtmlqn83cbT0sqcPvhHLeXjxw2fdgxB-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=dw0P9fd-9-3EpmSpm5sSPC1yiJ6q88_pC8ifCmkuf-lV0fK1ssqY3L0xXuLWPTJMVbE2CCRaXUB6-dSzjckMa2Vmx5y6nPqBJ89E_a0Q1L3kA-7mpudUmQcGa0vrWtxylpWK9wc0mE1FWeNTHpuGD1Udr1Wavgy0Gj6sJmwi2UojM0V-h7KI8orH8d6FuteIyLLyncDgLhZmBNEH-HwXhDh4Ir-CA328nwCQpiu2bbh2Vn93O_ETYCr2Oke_nIQCrC2VIsaZDta4OcSryRAV8iiKolxNHSpNT9YZN9jt-wdzr3fpwINpvVtmlqn83cbT0sqcPvhHLeXjxw2fdgxB-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ابراهیم کوناته مدافع جدید باشگاه رئال مادرید هستن دربازی روزگذشته با ساحل عاج؛ واقعا مدافع قحطی بود که فلورنتینو پرز رفت این رو گرفت؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22853" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22851">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktBqosyM_6xl_6_dgJoFmkhpWQcHgf-x3gqYu0_SpBeDAnHuxtzICzUicmc3aDE9pTOleB0C5rD-CwBaXbcGs13l107ZaW8UHqhdYfUT3Uzwmuqx1MLXITtPvifcODY8H3wbIgvT3llzDqz3P36AFYTbAVJnarupjxK2kudJHwZY8kCr2XKOLFqftVJ4OQdjqHU-XGfHfqVbBAsBQcl607S_CHVrr--f7M_FL2jdO5nwq44GqD9E4ILbGxY2InF6o_fdHqkepR60H69eT7JA8qm8__VdU7r33gAnKciYkG2TmmB_j7r32rRDYmIIVHrBUUtF7emZlQI-x5Xv6ufvpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
علی‌‌تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: یک‌‌نفر از اعضای‌هیات‌مدیره تیم استقلال در طی روز های گذشته با مدیران باشگاه آلومینیوم اراک صحبت کرده‌ تا انتقال محمد خلیفه رو نهایی کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22851" target="_blank">📅 00:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22850">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nn78Y2KbDIuNhm9tLmtxfKJAjOyO_OBVZSevoJQqz31RYyGjhdr2aj_woGqGvS7O7llCXZTSG6-oExZFcqyQ4-8UKUxX4YLTHSV2hNShrkxHvYLgqMhXdyKH04nx0bzCoPaSG_mdemvRW__naDWZoBFQiD-uZhiLsBBNebODZXvfLLiAbkYAgjBS_HgBtCty4JLnkdU-XrDoiUgZJvFPEeKFjqf9YZ__yD2zNLSEO2MXtVAOszeT9wON6qNre3nljfRrDHCGrzv3cItrPyCfdrQP5VV5ngGI6vUpY9yh5g1LvrON6J7uIssPkmHFtFo0L0lfPeQFuEI0pUBLptBdkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22850" target="_blank">📅 23:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22849">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=sCs_H5Mf-cCodRU-bvjlvuizdQRoLxDcuY8GZfcnBtx22EQsbQtyFRSe1MP6-OAlZTklZ_gLmxWnh00ypjH9kWXmzao3m_RJpS7VJhkj6Xn14xiN1psELFyZyi5fo3bwqekoUCQwqAHmPsh3MPOqUjTLAGjuA6ymJZB8CAujr-nLkwHjtM3GCLseexotXYWGg6noz-xkACfORUoujWhujl7kCmW2LrMUy1I7Z0rQOyIWOzIH_Me4-LHXRDxbyiAnta76reNVTL4FZZ7x8yBsXq_NleA0c37y1i898mHHJdc4I78-7r4X2U6pdi92KogALMFXIFyQYyiIEgirzM4oMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=sCs_H5Mf-cCodRU-bvjlvuizdQRoLxDcuY8GZfcnBtx22EQsbQtyFRSe1MP6-OAlZTklZ_gLmxWnh00ypjH9kWXmzao3m_RJpS7VJhkj6Xn14xiN1psELFyZyi5fo3bwqekoUCQwqAHmPsh3MPOqUjTLAGjuA6ymJZB8CAujr-nLkwHjtM3GCLseexotXYWGg6noz-xkACfORUoujWhujl7kCmW2LrMUy1I7Z0rQOyIWOzIH_Me4-LHXRDxbyiAnta76reNVTL4FZZ7x8yBsXq_NleA0c37y1i898mHHJdc4I78-7r4X2U6pdi92KogALMFXIFyQYyiIEgirzM4oMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه پرشیانا؛ باشگاه آلومینیوم اراک اعلام کرده‌است‌که هر باشگاهی محمد خلیفه رو میخواهد باید 100 میلیارد تومان ناقابل تنها بعنوان رضایت نامه این بازیکن به ایرالکو پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22849" target="_blank">📅 23:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22848">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=Tqn4M50T7l_6D5TKL32pGSFVICZUjY-QGJsqnibCIGGTeCjinZr5jllk2WLn2O5F0mLUFSxAKXoJJoape6Q1m6BieSduKByAJeual62VtW6l0tgdNEjoaotj1ufLw_bKbcjAFlRGMxdh0FMtDqvypT6O2fvw_acTUgi0oHfdfiYh09TnEnNhAhJRsgZjRVOs3hThdCykn4NR6OXBOED-k-qccPeoz6fXBMaPrwGtAXNgasLBGIRuQabJunmHnm_wbYWzBosxWn1aIGK0dNh3oYg5EZ-6TaMNeYpqMHGRXd6T3DkzW6N3kpnz8AXMAY8uYa2OfUUqrB8BOrYuZa4S1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=Tqn4M50T7l_6D5TKL32pGSFVICZUjY-QGJsqnibCIGGTeCjinZr5jllk2WLn2O5F0mLUFSxAKXoJJoape6Q1m6BieSduKByAJeual62VtW6l0tgdNEjoaotj1ufLw_bKbcjAFlRGMxdh0FMtDqvypT6O2fvw_acTUgi0oHfdfiYh09TnEnNhAhJRsgZjRVOs3hThdCykn4NR6OXBOED-k-qccPeoz6fXBMaPrwGtAXNgasLBGIRuQabJunmHnm_wbYWzBosxWn1aIGK0dNh3oYg5EZ-6TaMNeYpqMHGRXd6T3DkzW6N3kpnz8AXMAY8uYa2OfUUqrB8BOrYuZa4S1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22848" target="_blank">📅 23:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22847">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfPJ54DviPFr4ZOTtG9tWWA4W4SF8ukFm7LR_s52mi3t6hBIrT4I8qpyac9yZLqrXTEg2C5XOM-0zW-nOkPe0JqjCZbIVeN_XZ6A9BGJuOZ45iJttwxId8cH8BJqduWpmlZ_t8432MHvWh9mYeNs0TdraSEMtCDPCcVWrLm6hD6rvFKPTqCQp8z7U0921Y8ZmzrbbntTqbqD5OYcsHGjTyKejcNGU6RItAcfzvGBeoL6nLhfdn8-VmT7ru4HG9e7YHKl2KHP2QTF5aNzsb9pPoR2T5R32E4ca8v-PHhUG7VM7enxLsjIZiOT1JA9LgRZ2fMJ97Ob3c_PlygFEOjDWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه ستاره رئال مادرید: به پیوستن مایکل‌اولیسه به رئال‌مادرید بعداز چام جهانی بسیار خوش‌بین هستم و امیدوارم هرچه زودتر این انتقال دوسر برد برای ما رقم‌بخوره و اولیسه رو بزودی در تمرینات رئال ببینیم. او یک بازیکن فوق‌العادست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22847" target="_blank">📅 23:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22846">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">▶️
انتشار موزیک ویدیو جدید شیدا مقصودلو همسر ایرانی خوزه‌مورایس‌پرتغالی برای جام جهانی
🔥
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22846" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22845">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=NgM8A0ahBvm77xQYBzGiz2qYP48DqWxnYweZ78j5oK7FSQZsrRWTTwRHxqnRHZwlcY8Egr5sCeObVVmPKM6haefJXVcffL6DRDaF2BhQXnQ1SeruvjToN6UfGTAInldby7L3uecC7Vou4RkcAUOxgp0Qal3SMK5X5WikXmt7gU2AR7yFK1f_xHB9rQka2Z3fBqZ9AwgbnIsC-NT1c8C8W2NlDcGcdeuyDmn6PJ3HRR29T9kSKf8kfLRb1te-LfNKBNGE5mZFUPT1nOzINP717ufKm0s_4ZoGhITxBE4L6d6erNTyJ3K9PYMz3k2I0oS8inp_yzFHqs-nMTDweCOMEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=NgM8A0ahBvm77xQYBzGiz2qYP48DqWxnYweZ78j5oK7FSQZsrRWTTwRHxqnRHZwlcY8Egr5sCeObVVmPKM6haefJXVcffL6DRDaF2BhQXnQ1SeruvjToN6UfGTAInldby7L3uecC7Vou4RkcAUOxgp0Qal3SMK5X5WikXmt7gU2AR7yFK1f_xHB9rQka2Z3fBqZ9AwgbnIsC-NT1c8C8W2NlDcGcdeuyDmn6PJ3HRR29T9kSKf8kfLRb1te-LfNKBNGE5mZFUPT1nOzINP717ufKm0s_4ZoGhITxBE4L6d6erNTyJ3K9PYMz3k2I0oS8inp_yzFHqs-nMTDweCOMEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22845" target="_blank">📅 22:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22844">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=QLwz7Jhx4S__iYPNg8ePMuGmdcESV4SCJYUjoL3cDqjpfqKQq2WpRnKDBjQVsYjWQolnNuyDjjXaOImt50i4kLufKuGY9HjCRsMc1WBX2GD0N5J31i3wHNYL9k54inQVFbFTqWFdCOJbNrxMN8bCsGabv8E_WBSOAo4pKcVPST5udJjPlUCpTzJNzw-PN0OYgxBqYdqbSTMKf7_4RH1J7qu-5tY1M9OLhIl5_G_qqj1AWoSTOndudgCO1_lh9McsvDbLojxVJA7jHUJxBU3wwzr1GAnERdZpEkhWwq_hEFd4pPJkxzmJ5nQXW6RIARfvDkGrkn1ZvF1xJnF6uYgmWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=QLwz7Jhx4S__iYPNg8ePMuGmdcESV4SCJYUjoL3cDqjpfqKQq2WpRnKDBjQVsYjWQolnNuyDjjXaOImt50i4kLufKuGY9HjCRsMc1WBX2GD0N5J31i3wHNYL9k54inQVFbFTqWFdCOJbNrxMN8bCsGabv8E_WBSOAo4pKcVPST5udJjPlUCpTzJNzw-PN0OYgxBqYdqbSTMKf7_4RH1J7qu-5tY1M9OLhIl5_G_qqj1AWoSTOndudgCO1_lh9McsvDbLojxVJA7jHUJxBU3wwzr1GAnERdZpEkhWwq_hEFd4pPJkxzmJ5nQXW6RIARfvDkGrkn1ZvF1xJnF6uYgmWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ویدیویی‌از قهرمانی تیم زهراگونش در سوپرلیگ ترکیه؛ زهرا گونش بهترین بازیکن فصل لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22844" target="_blank">📅 22:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22843">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=j1RRVOODxGI9Hqd2pemdZrGplKSIZzTJ75ILFjnaL4bF-2oXCzgmnj-_Kfpvz3os9rnuLKEPUniCmuVgo0_kZRv7-_AY6uvuqe82XK3uUU_WzsMhfU-xjENLhRweRLWEjoriZvUKProDsK2ZOtBW0HFy-R2HBZ_L3oAZXrKY0KUzAf8LG8fHwKZeA4MKEGLX3tY_YM2MdnQz1imW_UHrjEd7oiROzQiqtYohJvd9CHHdvBruRosYsUWYT8OK-nC3ptqjsu9lf-0Y9HZIN_tv1ZzG5ZHV3KP7VX5DMX8Dyb4Ig-lQbPkFnVplapxmDio8Fg9VuFxV1tmCvriD6ld3JkPtaQ-vxc1m9xHsOc-_BWLYccmQpqA-KvXOR5HX3x51wd26g3IdQ0j0jtzrgUeTU5Y8zI2NvXQIQIjXr0tfJL2UpJcGx7pIyQcU7XECTIHaMyLuxCN2wWhWsczYAhnfTijKB9ljkgKLHzozwO-QuokYkNvWgmS3HO8srK6PiNk1Jmh9C1fBKmjPiCMRSwm8fxcrw9iTDdlqBD86swMvGjHJBnACZHa-1iWtBRWz5ytsYxiCN_tsUm5DgpL69Rw_tA_h7M3hT6g_OgCz_mIyc6SGmWi8ZiODtTg6kWSDN8x0W1Q4qya-HxgXlt2AYISbANDaUP5pT0GF_9IIR21Jmuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=j1RRVOODxGI9Hqd2pemdZrGplKSIZzTJ75ILFjnaL4bF-2oXCzgmnj-_Kfpvz3os9rnuLKEPUniCmuVgo0_kZRv7-_AY6uvuqe82XK3uUU_WzsMhfU-xjENLhRweRLWEjoriZvUKProDsK2ZOtBW0HFy-R2HBZ_L3oAZXrKY0KUzAf8LG8fHwKZeA4MKEGLX3tY_YM2MdnQz1imW_UHrjEd7oiROzQiqtYohJvd9CHHdvBruRosYsUWYT8OK-nC3ptqjsu9lf-0Y9HZIN_tv1ZzG5ZHV3KP7VX5DMX8Dyb4Ig-lQbPkFnVplapxmDio8Fg9VuFxV1tmCvriD6ld3JkPtaQ-vxc1m9xHsOc-_BWLYccmQpqA-KvXOR5HX3x51wd26g3IdQ0j0jtzrgUeTU5Y8zI2NvXQIQIjXr0tfJL2UpJcGx7pIyQcU7XECTIHaMyLuxCN2wWhWsczYAhnfTijKB9ljkgKLHzozwO-QuokYkNvWgmS3HO8srK6PiNk1Jmh9C1fBKmjPiCMRSwm8fxcrw9iTDdlqBD86swMvGjHJBnACZHa-1iWtBRWz5ytsYxiCN_tsUm5DgpL69Rw_tA_h7M3hT6g_OgCz_mIyc6SGmWi8ZiODtTg6kWSDN8x0W1Q4qya-HxgXlt2AYISbANDaUP5pT0GF_9IIR21Jmuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
کاشته‌های‌دیدنی رونالدو در تمرین امروز تیم ملی پرتغال در استانه شروع رقابت‌های جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22843" target="_blank">📅 22:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22842">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvkbIQDCxdi8yj4yzhBGks5yGneboXUvtLm8bWRdcyE4h2VFVfJykbBwr52mHknLnS6G0BPCrs6KE9IfSIYjSHG_K7EkhBuOvkkjQFsVWiBh_WrseitFYqn5b_EmalAwleTZ6EYCEjQiCLqrkJAP1q1C_Z_p9Xqn4eZ_b6HmQkyOL7bXLdBlVeSX3eJ79yKLa03VxI4TxeM2UgW0oe6vVGk4icwmJOzohFvRTHZipZmgEleWN-XWW2NOElw4TKfJBD_9N2zPCjNp0WiG8Rji9zTuDA9Kw5JxvLpz6XH3leicvmGmt2BkmolHCikZ48eF-WYc-4BE5TiYv9zdhmvSLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22842" target="_blank">📅 21:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22841">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP5bXRLGbBAah7ccYEC-cjT366bOHMOONEfMbdsHIuqPbVOZYXwCLepqCBWNuVRKXYobEOqKZfxXThW5f5y9gWzyVHsomnBDsD-yCqf1Qi2ahoVCj8C7Jbsa5FMMte7rhIfJWaci_mKES8kO_xV8l13gJXWe9KDStSboDh0rDUX9ofM_dbm03KXue59420CcLKYJzfr7KUc5f0XO2auBsgN87X9KKPwLRuRxsrUDOG6ryKI3juN-U526UyOSvCuGPkoiJlO3Z-otqA-d6MttVDDkWq8UoO5pbmVQ6TD6mF1_iSlWIHQmB-2v-ZBxpQC5MJrC9D3xkcRzFJHJyeaXbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22841" target="_blank">📅 20:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22840">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=JMmgvjWsKs9XH-ML6RdrWi2YKmUoIUyTkdJKEFU-xj4IOU8ca4nua78UKYovfAJ-Plk29p8rdNEroPx1k3KOsNv4fDLbZ0mQx1kyICrNLSdR0GOsF8cwXRvHMAj2cH5vfy2hrf5J7ppJWhQToq6ub86EIexsHNmi3v0wCBjVA7f7uaUgmUeaGKfLcgKqtHyVH9ZBCN6IoJfG5EHoGyr6PiPhVORchl2Xj6j8juWYBMdgELQi1L-8bXtNPxbDKTMRRpxtDiBUD0pNIzJmyvPtqig4EWIx3KEr5eY69BpRXtJJm81V1sLGC5e2LWhtwxYPIpuAKljRH0E65isTtl9BWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=JMmgvjWsKs9XH-ML6RdrWi2YKmUoIUyTkdJKEFU-xj4IOU8ca4nua78UKYovfAJ-Plk29p8rdNEroPx1k3KOsNv4fDLbZ0mQx1kyICrNLSdR0GOsF8cwXRvHMAj2cH5vfy2hrf5J7ppJWhQToq6ub86EIexsHNmi3v0wCBjVA7f7uaUgmUeaGKfLcgKqtHyVH9ZBCN6IoJfG5EHoGyr6PiPhVORchl2Xj6j8juWYBMdgELQi1L-8bXtNPxbDKTMRRpxtDiBUD0pNIzJmyvPtqig4EWIx3KEr5eY69BpRXtJJm81V1sLGC5e2LWhtwxYPIpuAKljRH0E65isTtl9BWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
@Persiana_Soccer
| Out Of Context</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/22840" target="_blank">📅 20:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22839">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgtc9jWRH3SdCicSdA76wzMF9J8L0Y3LzhLcLD_Qac6OkgGfQvxN6EhJ9JBlr9KWUcjC6yUB1rZnSI28mFIYKH3FZpe14kaalqGCxQK1sdzQ_Zxdx8COsCXqM6cHsUGwFOD_j6k38He6cysX85WhxdmpRnfuDfX5q_ky973WMB546EgizztnKSNNljfrm6C9CGUQc4DDKWvUcXItFdlNdikBqmDOIib8Nt06lDal3Fx5FlE_5zlv3YtUfT3z4cSj5eeLQg15NzjnKFP-dPJFzL8lPH9dD0YFghcySJBuZWsPACD-p-aC4LvI9oAFILMSYJqaIfLr5wDz42Ns7rqgoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#نقل‌وانتقالات|ادعای اسپورت: آرن اسلات بعداز بر کناری از تیم لیورپول به گزینه اصلی هدایت باشگاه آث میلان تبدیل شده و مذاکرات بین این سر مربی و سران روسونری بزودی شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22839" target="_blank">📅 19:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22838">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0dJJPN3OE_nofjhev_ib7T7G4DHqEn-emowlNWA9FuOtEupq1xmrwPulZWJ1Oe58L543BuT-VtIQ41kWfXAVnYfqsC08ATs4wTtML_ZHSsBnp6vwOBzSEqVZCR4vApdCuCTHfF7WL2Kj0d7luSn3pJJA4oiRR-eHnJn2_4p1uhl1__fsfT0y6b18r_C2IMN8KtdyoDeKx-gZ5MlvGbbQMHdXGav1VMXF6YTWYzMIdr6XnwuzYQykAnQNEjUXHLDrqk3RA9RQIQ9OluptIzSJu6eNeY2d3jgcienhXCBF_q9pAtHjhSEnNN345jXqy_2NsxsI5mLEN4pQX15MP1dRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22838" target="_blank">📅 19:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22836">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPXqxSfPac1xFwLuw8yFk5nPDPmg1zAr_rb0Ky1y0M5MRAfEBJPRjU_dWiQVhX3V1p3K6nOhpco0OGWvqq9-HmO56d5hvsHiSR5Vf1tKLtSLSTA3pwv4ml89UgQbLFwZk7PNvT0uS8tlUzOUD6CH1z16SNgKJUa2LXffXXyQQxlYHqzPnXmqRADr-w-5PZATz6b_jeFNN0va6mRVSYskl7Dkf5tHfQl5HqxDAOpFYLupqxqs6a51CiaI8CaRR1D00ovRdfuo9HILE8U7cccZ9hmRd9y7_c5v84VNv9IdmAQgEzEnV8PwPLSb5a6zBbuoERNPWhhtCqazkzYFQoreOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=gQGPhNWo9iY_LEaypsEj2qN4QNfdBrUbm-N7My6xPXKi7x0zu4vixRrkHtZdYNVbnQ7KFOGqivoERA-S6l2HQXu9T7hLFkCpoO31baS1SFuCf76vcfDVgADxq91Ck2FngyfVj_ScgJbrlMnsLsholVZdeA6izK9ammtUu-XMyT4F7NT_QvW8h4riej4J900TewCqeT_IW8HtMXPGN1Hq5yJyazwHZ3MbkoOJkTubebui8DgBhtq55iRwT2leqLy_hghwDwz2g0CQmoCr03xbAyePnFUdmpnUe805qYi86QcZ-hAOC44fjApLcjLOGvM13nN7C3shPxY7Fz7tBNtKZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=gQGPhNWo9iY_LEaypsEj2qN4QNfdBrUbm-N7My6xPXKi7x0zu4vixRrkHtZdYNVbnQ7KFOGqivoERA-S6l2HQXu9T7hLFkCpoO31baS1SFuCf76vcfDVgADxq91Ck2FngyfVj_ScgJbrlMnsLsholVZdeA6izK9ammtUu-XMyT4F7NT_QvW8h4riej4J900TewCqeT_IW8HtMXPGN1Hq5yJyazwHZ3MbkoOJkTubebui8DgBhtq55iRwT2leqLy_hghwDwz2g0CQmoCr03xbAyePnFUdmpnUe805qYi86QcZ-hAOC44fjApLcjLOGvM13nN7C3shPxY7Fz7tBNtKZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارلینگ هالند جدیدا تکثیر شده؛ نسخه هالند جونیور، نسخه هالند پیر، نسخه هالند دختر:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22836" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22835">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArLjkwZ4rECnRl6k8CdEYxArLoPJT9mrZO2YFePlha_m_rSBXWxeZ5ZpfWwlRH01CrmKTWKrvnKvCzvRtSW7T1dGTn7ulmM9hGBHpAVfkVzXUEmVTXTULULu4gfm-qj-JBRiY1W0KjUTl8e52U-m3DvtFtQVUUneFKklP31CSvlykFwnH5_iVA5RG6BYl9BIldI5rT6MeLK6PVOx9RcW5d7un2DbQJS01MXqYofbouJGnTb9MS4yETMhx_YA9RC-G_XRMBK_L1cYl-yPyN9VE1CFJVMimf1dIl8iIpKPoNVpbPqyC0_OdqevH7NAKfJ2xiP4PfxYG5tQMnazq9ZIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22835" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22833">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIAxUbQWtuGgHgiSQcJ-Y_04FxZp_kGYO_8TeIWspdiuqXUnP7aNtd_TVHLs2y24WPeWnHnFk-E7FA0D_EdNt6iEqahsezahLTdWd3K_j6_OeUPXPOcKEV43pBW_3nNPRD07ExznjBChFgRkYzovbFrsHTvUwChXubOfMz7ePeZ7505WsdB3qm3jwGmXRfjUWpPpd8IrTNOLHV4Tg-dX0N6uI08Np0EnzekzAnjsfbK7VoqpG5VRgdOjo5AxWhSvIwvX89ghxPPP9Ny-gYLHpeTLY3OAk82vRrYvPywJHgV3PCpO5he_iRtqY36zwK1Fsnreb8SzGfvItI4VQ4tNKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا محمد دستیار تارتار در گل‌گهر: باشگاه پرسپولیس باتارتارمذاکره‌کرده واگر اوسمار برنگردد تارتار سرمربی می‌شود! او می‌تواند تیم پرسپولیس راقهرمان کند! باید چه کند تا سرمربی شود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22833" target="_blank">📅 18:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22832">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnM37mQrTOFSmjQpYL9ed-vHV0kiifugymvjaZ9_XU0PP3L2lbFfXF1ah5FC0KbO3cZuJVyIHb0zBysM9JJspNlkW1S5tPDv9enDY9lzU5taK9KqC1WV8cj9dZaozc6nMAvZg_FaZdgAyCuV9aiBljRXTTyD-swuhNYdNYjZAMPbYz4DmJq_8Gy4vTnGPh04pHqtJ1TzuvvG_ONPWl4hUMdKkFYcCX5GL98xyKHjQn3ZlSEYwdphf8vXgfkIx9dDzAtiEFfAtyZbvQqOldo60cepv1sc1nzx1Lh75rtJszCPq8fqOz5ekDjDKCTwLfae5m9ybMOPldsFsz6al6dcKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22832" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22831">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1lzA1SmLrGED4_GCer2eueko-CnnbmXBIssw1Unsu_y03knWNxTVG-2a37cIxcQ5pEVC7l9ZAeZ8M6q6Q2MErTPTcpgGIw_0HhzMNct91kGma3m-Nkhw6yT-TzdaLtyyesjOG0K_onQblE6RgvWpwOWO895KwShu0SLrQRaUwxUJuTQx1t0PlQrFPuTRjUt_MxhC6lYJwOIj8SS2Q8G6ty_hM4XtjlMu2vyV2yw9KXYV2nS3pocF9EFZJ6GFLpWse7WDi5Mk5RXhS2Y7YAr0yw-g0vfeTpZbMoJKOVhgyHS351I3szlWG1tVCkvNbEQ2mQe2nW4s1g4K8PqDuU26Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛‌خوزه‌فلیکس‌دیاز:طبق اطلاعاتی که بدست آورد مطمئن‌شدم‌که‌منظور فلورنتینو پرز همون مایکل اولیسه وینگر فرانسوی‌بایرن‌مونیخه و روز سه شنبه پیش رو آفر 150 میلیون یورویی خود را تقدیم سران باشگاه بایرن مونیخ خواهد کرد. خودِ اولیسه هم در جریانه که پرز میخواد…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22831" target="_blank">📅 17:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22830">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwmAm5xb9s8YC-_OQFgDdL1o1MBiRcrH9xHYN-YdEXQBK4LUOSHAtCQ_uccYwf73aqRm5B3nCYkBBftiCWitpuppQhIiNJAHzfwhkK0yiO2e7BInEbcvsVRlyW_s8OpvKk0ABhWFdvpbIEoiCwE8rMlJQNgfF38a5waLfqPOAHMt32iDvGizWyj6USOQst84R7d27K4KTFWIHF5E0McduRCQR1Y_CPOhvHinLC5kWOXZIb23pRqZph-2jC1fzPO36v0cBLudOHouwJSLgBAMrS7ZGjLgorpWmcAJ7KGm5Dtb1Nhwc7t8Ych2d3V3syjk7a3y-BhhxMmoXy_1QzkYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خوزه فلیکس دیاز: علی رغم تکذیبیه شب‌گذشته فلورنتینو پرز؛ باشگاه رئال مادرید بشدت علاقمند به پیوستن مایکل اولیسه به این تیم است و قطعا در این تابستان برای جذبش تلاش خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22830" target="_blank">📅 17:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22829">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976cd07773.mp4?token=arQp27TKBY4vNF87ki60X6tBqWOHbhXgbgctDCdBrL1UcpTLuQccoqR9YAfpznbB3bN40ympFJRgPChYrvr1ysH0fUvcTSvhX7CPBg0t-yRIeK0OS1d7wLfm7rMGjb7nni61XVjMv0RWsJJ2ATGr14fjqMpMHQ-_0jawYGbPOxDvf7sLaOOPYhCgpUIQnJSt7OAYnPtoJEb2sKXXPn_Zzss3DM6gIlE9P8AnqAiwP3a7mC957O5yHt3huzy2WfPX722F5uKijpJY68cgCVo38o5UaozgySggtQfEJ4-sL8t7dq4t1ZnXyXi2qpRd0KoZsdQi20Mr0SPD6MqMrOq1RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976cd07773.mp4?token=arQp27TKBY4vNF87ki60X6tBqWOHbhXgbgctDCdBrL1UcpTLuQccoqR9YAfpznbB3bN40ympFJRgPChYrvr1ysH0fUvcTSvhX7CPBg0t-yRIeK0OS1d7wLfm7rMGjb7nni61XVjMv0RWsJJ2ATGr14fjqMpMHQ-_0jawYGbPOxDvf7sLaOOPYhCgpUIQnJSt7OAYnPtoJEb2sKXXPn_Zzss3DM6gIlE9P8AnqAiwP3a7mC957O5yHt3huzy2WfPX722F5uKijpJY68cgCVo38o5UaozgySggtQfEJ4-sL8t7dq4t1ZnXyXi2qpRd0KoZsdQi20Mr0SPD6MqMrOq1RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین‌ابوطالب‌به‌تیم قلعه نویی:
شک نکنید این تیم قلعه نویی تا فینال جام جهانی میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22829" target="_blank">📅 16:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22828">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCR765JteFNctuZQEgS78Q6pIYdMyWpYvOwjo8yfPKG7WZANhZQouOYn5ot71EALEvfMMC8ZQhO4XhFcReAcs-2ghsDrB4wt4bPAYvsEuNlp5uY-8G0p82oH-bi8Syr-mrxAr7PfMYIzB8XWmbnaA3m_g1963-K7nR0dKN4VQu8LtNfSg4RMg00WQDY-yk3fDweUuzHHLbDOZ0FYvZalwMLWzgQMGIBR5lEjfFFw6tpg-8zir2aZbrUWITS6cXlHrutm148XpkK6VV8sO00Clm1e3r6PDKPCz4gbwmks5HUjdXlYK1FK1meI3DPhaW-87gKigd9Kf5_D1wbboj2TBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بین‌گلگهر و پرسپولیس؛ احتمال زیاد پرسپولیس راهی لیگ دو آسیا خواهد شد. اگه اتفاق خاصی رخ ندهد! گل گهر رضایت نسبی خود را اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22828" target="_blank">📅 16:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22827">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFePER85Ab6rHO43H3rQXFYhUfCK8Hy3JlZsUwLf21dEvm_6mG6HTAJPtgEIChXpb1IAiZm9yGRCe2mVGiSQJl1iOMz7O13uY-X8bxpn2HxC2EkKK8i7QMZnQNVOUcioBfP_fsvMwNqGRsO1YZQNEwac3b3ni-L5VfE1zvLnVDvsLnklGRhsIU--WLHa7DFLKLKH6jYoqdOWo8U30bfhtdtQ8NTQeVYGMPOaj6bsZnhqJ6puJ3WGcnsOoP2aKa4hUEas-K-fr2pFdu1Plo7-mmdEz_bz22Hwi2F3B2_1e0xp2WRBA2ztWAOehZQHXMjzoJxDt-2F0-HhNLEc-daDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22827" target="_blank">📅 16:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22826">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=i3ZeL0X5VQCvrfTRd1QpWV-wwYJC4_FemNjWmu_WMyp5zzHB47toZyVp_p9faGc97mjwIO5CSPxg82uHpvbxGcjsXPANCfw7zPwZqO0S3vJea_BJe3Jzg3iXte9zUwK78nPdbI9FBMU4AFUYDH5CIQUGJ0XpPDhy0eu_2R71BEDTJ_iFmeC23behWdZyphmE0oXr5WR9mnrPrSLFF2hIR3OWRwJvpmtNc5ROLN9AIBDAz_LcUroz0rpP7-4W_vcESMheWtX3AVKyVlN613rRytOyrG5Yrv3jMI8hpGZBOZQxU_dGwk3HqD6MqADCPObhe37SFvT_jcIyZDVSWihtjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=i3ZeL0X5VQCvrfTRd1QpWV-wwYJC4_FemNjWmu_WMyp5zzHB47toZyVp_p9faGc97mjwIO5CSPxg82uHpvbxGcjsXPANCfw7zPwZqO0S3vJea_BJe3Jzg3iXte9zUwK78nPdbI9FBMU4AFUYDH5CIQUGJ0XpPDhy0eu_2R71BEDTJ_iFmeC23behWdZyphmE0oXr5WR9mnrPrSLFF2hIR3OWRwJvpmtNc5ROLN9AIBDAz_LcUroz0rpP7-4W_vcESMheWtX3AVKyVlN613rRytOyrG5Yrv3jMI8hpGZBOZQxU_dGwk3HqD6MqADCPObhe37SFvT_jcIyZDVSWihtjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22826" target="_blank">📅 16:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22825">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXkkRVz9H0GNwqlSrsg9b7WQYrQu23uvDFOHJTwimUXjE_m0mjL2Q06o-_9yyJ4sPsULvQUazAPEPi6abytg06kyW1xJFFW9jVHmQ5WzpZwTo2lwfwSTX9lo1gThJOTS4H1Bmi-H3bS85_UnJle92Ze1LAkIOq9CwLUu2tkjeMXXFcXmo0X-XNA1GXsaQQhXr8mn2W9avZRmC7TKPHEHFBUAnloTTSZfHOZDzMa0TRBrEVlzmIqMrJU0GH1EYrjjejcDIjzbZ9NCnTn29URt1yTwqSLJkGaOg-QdaOA5cSuGuKwCUSi8FUtT_ahvOIOn3SMegKX3d63pbJPMPkUuaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل هفته سوم رقابت‌های جام جهانی؛ از روز 3 تیرماه هفته سوم شروع میشه تا 7 تیرماه‌‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22825" target="_blank">📅 15:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22824">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tg5wBRewR5ZQPiLSJyprlr_fwJ-GipngU0D_vMrmviV-PREH0iwYoEkmIqKhSRblqqrbSCcFP_0bYbXVus94NVfmY1fYqfn85U7ySuclHMiaL7TpZVduD_NGIsj3-G7Fm4Nq_G9WImZ2g3jC9osKe8Kmw3eyOgeIYbsnm3jWcyjQGtudWig96rpVNU5FX_FJOeBlaKtyyRafVlBrV5Cvu9End0QhKgcuoovIenKhdA3EgQTOdNBhwBF-jPsTIlGQbqMJTDrPT7_CDkqNMyT_3EokaZRaMRH9C7JhglN0ofRa-CgGRuA8dORCfeSWfpAWagM0a2R_LDEeqlYoT_yc4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ نشریه‌ کوپه: رابطه فلورنتینو پرز و خورخه مندس ایجنت فوق‌ ستاره‌ها خوب شده و مندس به پرز گفته هر بازیکنی بخوای رو باشگاهش متقاعد میکنم. ایجنت ویتینا و نوس همین مندسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22824" target="_blank">📅 15:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22823">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rd0A6Q4EyY7FpWulJMAPcIJKX1wFAOThQTSD9MoSkbRq6ZltUZyNAaLf5ljHAc5S3qi4lyqiXo9wHKaxMA4FOWz7OKfwmHgADy-JpjO-S4qrHHsYK6OdKn4f3jgMRYItkjUBsD42sgeWM_MtxzkaPbS4_fYdGn_De9mPbcRm1QakX6F_mhz3SbMrEF5U4r3H0WDlndCDByEVFhLlwatc_SgX4dK3mQUVSiX_HWzHrNvSVgbntcjxAVhdYrmdvCMVaRBVb_5dGwLzPjD9CUcgeU7wd8J03SXSvz_VVDumufKFkx_j2iKWXvizBUqcn4yWuNB3ixab1pg0jxAMZPiyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22823" target="_blank">📅 14:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22822">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD7QlesWN3TGhrRenuSC60XM-gYGEEbUELtYu-Q5zxO2kDVcWoGufc8oIQb30CVGJt65I7KgLvetswo7fYTTq6_d52FIUe8f1ZwxrzkwLEq_1fgWY47RufCsDpR82aJYIvD9vzpYRIT77Fk5XDid3qrZAgSYnIkrm3---8zJnyfAz2IchXD5-jHJxWxmKT92QcoL0z-QJwbns1mlh0mCCxPENLHrIgzKFYeVdHT8m7JDMej22hG4Hiwdl29P1y3d6LWWX5bKAuVJlNmufwesdBzxicbcfJWHy9Rg08TepjbFa3pF2kc5xXJQkqcdiO5opGaG-DMCp_0dpRBUddFDng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22822" target="_blank">📅 14:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22821">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=F-F3CSn82dIf-7ZPFp27-gJIOsqzRXhRsgCFlEIXzXRcP-V6D9-PgWwY5vlsz3BxQ4dSh_e8MCHFiBEj-ofQq3CVWUVebLrMtVQv9JhgG2fxE7IBj7fHK4Wabu-3UEfCPtjnv-iM5XLmzMzRiHfy8lb4tDxq8wiHW9l_BYPSxpz_aoXQm7J_0rhE-U57Zif5TFC7rXV2sjouIzc-mtO6E0LA0UmV8uq7HBbGppzEjGtuWj-FT1M5vf9zyyoXrjC6FB424aDG3fyKeMfX-60BwFoehIcQtOj0CRlG2BjXQQfav60haSOyM5mtD4sUKAdZsMXw2WauX7S0P1gLgKHZVJZ3cdFKr7yrJKWBXnPRYWM45bI3u2jKhTKEodDQv6hG5s--uLFRw3eYFBvBOsXGS4M3tgSAB-ik0SjmYCl0hWyoypkkRHxRmx-Rus5YeUS8HijggvNGzuVpa1GoR3m_GHp5Rk31icXzZKSFtxkCREV8iLIRuoM4PVl6fpWEsrTtKl3_PLRwMCv3akAi16tiJytlxisY1s8zVbbUYUgndruQ8TUHCTfdwlBtwCROPgKNvhZGkHgCyAzDeWooGY229In0mHd69UvGWWIIytigpJ05IcWWaNq9pnplsU0Jwr1ZBCN9FEUXnbVuaCD07xTI4azL2P7t1zdaQCPWIgmIoSM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=F-F3CSn82dIf-7ZPFp27-gJIOsqzRXhRsgCFlEIXzXRcP-V6D9-PgWwY5vlsz3BxQ4dSh_e8MCHFiBEj-ofQq3CVWUVebLrMtVQv9JhgG2fxE7IBj7fHK4Wabu-3UEfCPtjnv-iM5XLmzMzRiHfy8lb4tDxq8wiHW9l_BYPSxpz_aoXQm7J_0rhE-U57Zif5TFC7rXV2sjouIzc-mtO6E0LA0UmV8uq7HBbGppzEjGtuWj-FT1M5vf9zyyoXrjC6FB424aDG3fyKeMfX-60BwFoehIcQtOj0CRlG2BjXQQfav60haSOyM5mtD4sUKAdZsMXw2WauX7S0P1gLgKHZVJZ3cdFKr7yrJKWBXnPRYWM45bI3u2jKhTKEodDQv6hG5s--uLFRw3eYFBvBOsXGS4M3tgSAB-ik0SjmYCl0hWyoypkkRHxRmx-Rus5YeUS8HijggvNGzuVpa1GoR3m_GHp5Rk31icXzZKSFtxkCREV8iLIRuoM4PVl6fpWEsrTtKl3_PLRwMCv3akAi16tiJytlxisY1s8zVbbUYUgndruQ8TUHCTfdwlBtwCROPgKNvhZGkHgCyAzDeWooGY229In0mHd69UvGWWIIytigpJ05IcWWaNq9pnplsU0Jwr1ZBCN9FEUXnbVuaCD07xTI4azL2P7t1zdaQCPWIgmIoSM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لحظاتی‌از عملکرد خیره‌کننده لامین یامال ستاره 18 ساله بارسلونا در رقابت‌های فصل گذشته لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22821" target="_blank">📅 14:07 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
