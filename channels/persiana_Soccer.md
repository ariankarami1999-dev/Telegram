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
<img src="https://cdn4.telesco.pe/file/ke3b3Gc471rX_h0QW-7LvCQQIhGdjPTTFbT9vtWB-DVPMhbzrA_OG7pX3TxZoD5X9oSv8QZX08TOIblWwfUkBhCNPxfOcP_QNoL5QIFWFJ1jA65qG9oiXk4bQgj56OsJJ9Ve-UraBGRC--1hu0jT0SjtvXkoMh63rKTXfiQ1-b6NotS6pE84nyHVC9JIF_GeHEtzy8ZgtQacCd0I8cpCQHwNAJDjesPJl76r_ifUpMbhGhTJEjTAQsxvuYkqvCuFA-MhGoyfLEeHmCBGkWOsTJpaQi19Y8ygkBFhCbLFin_yV4Fv2yqWtI-kOWTg4h6ybrqZYIQwC5Icfh2bhzMgEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 169K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 19:46:14</div>
<hr>

<div class="tg-post" id="msg-23069">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=T08t_pUkHIYdbzCh5yNJYfHfCM3NqB6AwjfdtiIv5Ai_ydzvELSu1H7A396he6yzgTaPMXAD_j4ZzFMTNytsdfG5wXPS1Uf7VQJop5EFbOmwfgfmd9qZKc3d-q8o4qnOITOaI0DUjsYf8JW36fq8QNOYoPxP8ETTJROeh7wfDZq_IS-pbpLC4jYwCdER5ZisbncrNUtPOAqEXG1IO8wKC6ezM0tSKmI4cJD6G30ucPFRX_rRI-Ob-YSUrSsfs4BWHCnhRkl-VnFVS7FSOT-yC0Qp3bqtF7FxCf_8hIF86bk0rIgZeCkYZ8Z15OmPhwBY3qqDY3Led_iSELQGDy5YLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=T08t_pUkHIYdbzCh5yNJYfHfCM3NqB6AwjfdtiIv5Ai_ydzvELSu1H7A396he6yzgTaPMXAD_j4ZzFMTNytsdfG5wXPS1Uf7VQJop5EFbOmwfgfmd9qZKc3d-q8o4qnOITOaI0DUjsYf8JW36fq8QNOYoPxP8ETTJROeh7wfDZq_IS-pbpLC4jYwCdER5ZisbncrNUtPOAqEXG1IO8wKC6ezM0tSKmI4cJD6G30ucPFRX_rRI-Ob-YSUrSsfs4BWHCnhRkl-VnFVS7FSOT-yC0Qp3bqtF7FxCf_8hIF86bk0rIgZeCkYZ8Z15OmPhwBY3qqDY3Led_iSELQGDy5YLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ؛ مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/persiana_Soccer/23069" target="_blank">📅 19:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23068">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5NXqAl42yoLBK80Q-OdoGd1zuheAsu2yE5NE5Fnk5cUiioEx5_5dMH3l1SW-9IYeq-zMd-XWtAsLqQfT3bA0m-KeeReawGLj_My6sX51V63ctDoiw1F1bBpqNOWUBtvNh8Q5y0WmTswNzjmuAK6c3PrH7VjrwYjt7xbV_v6sHtZ4iGodVCauqUjcxBklRgglJu3FGFuZ-1Aqd52Artyl_tj-t67QRymBND8Bm87e0y-5eEq1IkQYvGi2WVy9rpZBqDvnSbl5z3OBG0qUhLpvNRN4vXkTgBIWzYcIbEqLerg5l_-tvXZTbFdjE514rV0vpPri99t519RRInyXIIWNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا: فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/persiana_Soccer/23068" target="_blank">📅 19:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23067">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUpPcmgf9sxhx4C2q1xqYlGfzsohmO4roNTOku2X_UjcHcV98Q2QwaLs8_B0ZfrtK3AB2tKPV0hF514ySnVeuVFmWvnhDTwi1QoO5gAfbOvgZAvX-f2sGdj9pu3GZy3jF8W6o4faI6D7a8EZeIJZrmqaHYF0SsKkGhYZuCLUZlUgCHJIurWIOaXzZN5mFygP4Y-QKjuOcvNcvnzP5lhRikHTkSndB1UfEFlR4vdhatxoripJniLFQQ6-dyZ5t9pc61Q-cqP_Kngi7T_3mzldFMj0xTcIeopnX8eZUgdG6rTdkIPeln17IvTMKmx1pYcdud38FTLgKSz2YMxHqsG_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
با اعلام حجت کریمی عضو هیات رئیسه فدراسیون فوتبال: تا آخرخرداد اگه استیناف نتیجه ۳ صفر به سود گلگهر رو تایید کنه گل گهر مستقیم میره سطح دو. اگه تایید نشد، ۵ تیر پرسپولیس با چادرملو بازی میکنه برندشون با گل گهر، ۱۰ تیر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/persiana_Soccer/23067" target="_blank">📅 19:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23066">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsF4ta2b8NiaVBaZC-7TS6WPMJR-E6kII_i4vCxRfpCj2CNJGt_8e15oEDLwgugjhZhqnWgRVw-beNAy90b9lD2-Oj_vCRE07wyV5lG1W-WEgJqu9n7cFZyo15zgJsKMwGIB8xjR8BMMk15BBQyOlLwX62SIWe2TJ00lQYiWFPmxt2coRQuwVrMTC3BL4jrqRixxAdFv5GWT2D6rMr9PIbKbYyQkzLwxLFGNRno2alOJWKjWBVX7bxx3b0uXZ1jO3enIr61cOApZV6qpnB4AsQfNXqgqiHwPsyQlD6oWQTvIQuUkhLz3KHEoIY32iM9_xrIaO9L7jezTQnVgEe84ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیست‌کامل‌بازیکنان حاضر در جام جهانی 2026 باتجربه‌قهرمانی‌شیرین و ارزشمند در این تورنمتت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/23066" target="_blank">📅 18:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23065">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuPSBR8UKVCJIKtyEEEpY1w4aCTdP3HigiQ7ocSCETfcFhcAkRZqirq3lc3-ymZHRbIDR8_wGLtBAiys92v3xqeMIY7vVMLfUeXdeu0nFYKielemlVaxaENI1LNdV7-Gx8uYdygEIRyXcP7nHZ2uqSVEfOF4G3KwLywgzjuETXXaTMqYEe1r189wkMXzPXmje030u5xTmGpFXlc61KqZEVVrHq-I8bSpv7JcGPGsU061PLsn6O1d1OvxnzY8bsbEmHu-Irv0KN51i0AX0za3leA6MVhc5ovtYX1fPcBFJ3Bk2FQH2OVlsDSLfCUs9VypefPNlpx0GY5uW1tejYQJmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/23065" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23064">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzLKiMLJ_AqxtovkpbuiiFgRVNKCT0ST644VGydxJPQdhHgTffwlmlYNPLsFNBGaRvvsUFgqWdvdSwjbjmkBjqh2T7SU9QhAM5DK-e0i_ehnIqhTB7-rfEpVXJT7qBVlPdkOP7229ykCFm1v2Jnl0pO2IL7t3i7b85U-NJyuTjNA3-U64gkrI2yiN9eUeul02bOrP_G0avFBJUnZ8anvKjx0kJsfUgNqmCZP78ulFbdT5ifMCgJgkH-Bx79n-RPDZRpNSqL3Nj-0S8K8ZoW9BCWZp7jxakwN0eWkbCXHV-x4pbSoX4mIt-yOOj08UiVhEl3a98jOuQwDpl71T7OhBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/23064" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23063">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbeo5SUk-3EwfvE7C2Bbd4GQRYCS4IH9oecbldJKVY6tuqiiXPOlLRp6jz75RWaP6JHNPYPIPpHjOOr8SWxNTpZn2gyErMSztHrE2FJIqowuNCtk7sKAf0dZCmgQQEyvccEAErhQH1E1QKveT_FQ4MsVV8xaeElO8CObW97kXVnSZ8UYZ-XX6qWimVFwqI0wW0TDMH6dNHIbIrSjhb3ordt31DbmJ6lG3WX21mw7AkLa7hoq2uK0sq4qZD5VZALAFSKON5Ak6bCORhjXJRk4Y08IDi-rpTm52GW5_Nc2S6xpDWlfkfZ3jlMXgXWPykxK90hu0aNRFYxsmqeeLmQrAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا eg19
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/23063" target="_blank">📅 18:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23062">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ucx_P6uuYS9GwoLfxMfV8GaKQ5oEwjO6zgbQn696GdCZyDK-nPze5mrRaS-RtWcP-6q8vOsnXYmkskb5aTy98lgM6gwoBCZEHAV6sP9deT2TdX7a45DOl48G6RSjCX9O9TKp0ATmGEVqrggrT8EGOiARRF1PS_1gz7-_lqTpT-QeT5AD-GEIkX8Dzw8z_6ZxUligHlMPYCl-mBtAI3_lPi2muQAdW9idtV9iVdttF4hMbbQuGTzJ6_Y0kEdM7TJNa81Ac7TAklVyLhHXv-Oh7xPGoUloENBqxIQXMus6H7SW1waFUznBR99s_V4DdJkg-U_QnzaQGqo5vsKJmjHHJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/23062" target="_blank">📅 18:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23061">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49850c982.mp4?token=b-yqmNC7_E8w8oSBhHwjAqYg_nUnjhoMRYBAZPWZ0uSsWfrLLtyyDsSxyA498W1EjZhJOge88vGzTfnKqNF36hZgbKvLgCFPqcqV91vQVQ_At9eWzIl-rYROHMHVejBalFS7LbF2_wNQTAzbzGrqLyrcINY3Cf9oALnhqV1waV1ZJerep3w55wBihPu3dQnuWAj0K45zlM7K_M60mGecAsV1_MQTJtcIZI4HfHxuQMvNBc0Y2FTKKBrQ2NBBiHKZB9Fh5r7LAOT80v0EquPGJFOwaHPCK2rn0XJRMtxt9xdKFiMr3M_bR_snWewMmxIl0-VOoKjWbz6epWSUcKReNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49850c982.mp4?token=b-yqmNC7_E8w8oSBhHwjAqYg_nUnjhoMRYBAZPWZ0uSsWfrLLtyyDsSxyA498W1EjZhJOge88vGzTfnKqNF36hZgbKvLgCFPqcqV91vQVQ_At9eWzIl-rYROHMHVejBalFS7LbF2_wNQTAzbzGrqLyrcINY3Cf9oALnhqV1waV1ZJerep3w55wBihPu3dQnuWAj0K45zlM7K_M60mGecAsV1_MQTJtcIZI4HfHxuQMvNBc0Y2FTKKBrQ2NBBiHKZB9Fh5r7LAOT80v0EquPGJFOwaHPCK2rn0XJRMtxt9xdKFiMr3M_bR_snWewMmxIl0-VOoKjWbz6epWSUcKReNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇧🇪
کم‌ ترین انتظاری که هوادارای رئال مادرید از دروازه‌بان‌‌ تیم‌شون یعنی تیبو کورتوا 34 ساله دارند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/23061" target="_blank">📅 17:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23059">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qezj7_Z3PSIJ1sNta4cGAj4ZlyWUl7UULyV9Pv0tgR9hUMqY8OfFPaFeDw8HfRE9FJpCG8C3pHXN_e5FS5fhF3A6wJd6_zpiL8mmlsRBEQ0eGA_CbJmD6nkTvM8QzAcwY-848I78riRr68WJB-AjoBoWo8DxmLuuyc5ipXzJguvwihyoLnOil9hv1x3_3pO2eM9L7rxQfB6kBDu-QB0JAxhksXedi77105bH3G_EQ7oNAvg5L8z8WYMgZo8dRAU4JNHB8y7IgJoUwJDD8idkEETTM70xHe89KGH5my_mYEznOpyJaG3SXiO22gR2Ft5zREh8mtCibCyZIjnqQRsKMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/krzp-V8A87Zed2RpMmPp7WuEbhIxIlBYEDFPKz3u1DQDwhiTMbRW7qq5EEp-wJpvMhipGO_VwpfKtwjushNLiNyU9wXdNCDrNzsmQinfvCgbbmXHZU7RGiF0VNJIy7jYm29CTeHeBNg47TCGBxYNgDqntyMnv11HrZsXpr9mgdNlewNlDRnioJXUTFt0tK-UOVta_PMQAofYLea95JGZoaa6ybCbGsx-FBdd7GSSwLqxsfoh1Ex-Af_AtXSCjO__SaDfeSz0GyWwvr77sat6F23jLSCOGD0t3m_dgFtXv5Do4OL1Jso2fKfdDdmHuQnKlmSZKIytAlBRpKupGPqL3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نادیا خمز دختر خانوم پاکو سرمربی‌سابق تراکتور: از وصل شدن اینترنت مردم ایران بسیار خوشحالم. بسیاری از فالورهای من‌ایرانی هستند و در این مدت متوجه‌شدم که به اینترنت‌دسترسی ندارند. پدرم یک سال درایران بود که از مردم‌خوب ایران به نیکی یاد میکنه. برای همشون آرزوی…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/23059" target="_blank">📅 17:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23058">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQnsRm5rKv9COKeHpnMyQNwud_ad1Z0Achnp2LNV_s6-MhJAtn89nf5_K36yW7D21Kcq2XCC5tj6UI3YeROKdn7-QTe74U13Ljztq0Pkn1k2envR6dHCNbMiYPylzdIr4YIf2Bi5kPQJ2y0w_iMJ1Ns0bfrbbWu4KcJ8nrb72OplKB2aVin6vuAhZdZWH2j5D5Ir_otB1m2yR0h4yxTEH0m1ywlo7qYaAzRjDfOtyytbfNi2-Rj7m9rGLhwRMFQ3scntLcziOej-tdNMzVi6B7Jo9jsk5MWJvVSXJ8NNDPI_fOTpHVx7Z5p_kItnz5-ScwEk0MrIp74mUapUVKkjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ ارگان‌های امنینی و نهادهای‌ذیربطه به علی تاجرنیا رئیس هیات مدیره تیم استقلال اعلام کرده اند درصورتیکه فرهاد مجیدی تعهدکتبی بدهد و در مصاحبه‌ای عذر خواهی کند مجوز فعالیتش در لیگ برتر صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/23058" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23057">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayxJpdm8AMWhSohTYBEIdc-Q1vgkVB40bKCycV275wQTnXxx8jf3NwlQO5JdISc9WadjB3oFDf570Vu_oGv2ssnSRy5ioAhsDDaHpwTDk54DUNsOqvvamyZ6YPf_Cn67dfud1RG6XFDP7pQPItlg4_vwg4U0obo_qrTIWsa74qPQbLCB7g4hsuyMVzO7aOP9QBj7Fweb70yIbTpcniGkVomKgPIWOseFA_XatrQ485hUu6dyMaXJMdh7PereL9hkjgt8Bd6ZGJjB-C_dBhXJLdquoSdWL-FqEndh_XJEwx5fuirLCpZZQlW-7ByCvnUtTI9gAATT1vaVe7FJmSsqKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بمناسبت شروع تورنمت داغ جام 2026؛ سریع ترین گل‌ها ور تاریخ این رقابت‌ها رو مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/23057" target="_blank">📅 16:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23056">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQxHKV6Ia_zKH58kfAd2YcFkDMEO2ZsfyYHIUuGYZrmE6bm1oOoGcxrehrWL9NV-KDrZz3PZEfXYAvv5CnHBJGDpMZVMbgwsPsn5N_MBNLWcwshUk8TeZrXrLYFXGsWFoJwQUOzXfp8SwenwlZL2dxkn1KvhrKp0t2XlAqle87r9C1Bmg6Kcr22euH9W-OVlh0XUhJGGNDWPc7lylD0mhmNI0WZHuxeBrPewJ9fy_Jeo0g-_YXVUgFfDEFq9PIuWA625T4JrDtEvScEi9B9KUaHCCnn7htSddlS__clhgdMCkA1uVK3fTXRP2WVbXo9Ph3xz1c67SS9im2o5CPTkFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فلورین‌پلتنبرگ‌خبرنگاراسکای: علی رغم تماس های تلفنی با هانسی فلیک؛ خولیان آلوارز ستاره 25 ساله اتلتیکو مادرید از پیوستن به تیم رئال مادرید استقبال کرده و گفته اماده این انتقال هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/23056" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23055">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9MwsZGnibxUquhxbGl3NFi6qWZXNHB6OIcISwdTBnFbd_zVOf_-UwN-4vIflGfG2iSt1DZyyjgcMathPgB9-ZNshmoL7rGV0kUQWnax3lJWpgsd1wNtWmKbxBx_UwVtNcpfg9D59qbBq5h0cMmgsqhBgUWt_rQRFKis42UDcmK244M9JIKRhJGadD0j_KxLGu_nR6UJ9FvJKo7LTLjvzHd7PHcuhVW332nYy9mDn6WaIlsB0zijdy3Rh-whgmcxVaFoJQauBcU-Gk3LOw96kHFem_m3ZNEiykVifsvHMO4HFTdxpRg04eJhahgR6gPGo7tdnmBltOGDhnCcaJt5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
عدالت در میدان، هیجان در جهان؛ جام جهانی با بزرگ ترین تیم داوری تاریخ‌فناوری های پیشرفته VAR و قوانین جدید پا بمیدان میگذارد از شمارش معکوس‌برای‌اتلاف‌وقت‌تا اختیارات‌بیشترکمک داور ویدئویی؛ همه‌چیز برای‌تصمیم‌های‌دقیق‌آماده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/23055" target="_blank">📅 16:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23053">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tq1_ZVeFLnwqlfLideuB7NQqyb2yNzJujAV3AGRP84uQPOmuS86ZBiUOs3Zkf9SprMQRRt43pskOmf3tiTPT6VafZj2aMvSulZCCPghH9ZKjFwrjo4lssKfmINkjyS7q--KRVUPco1xqw6mXBFQvGGNQ6JtDIe1Up6sMkkqikuUgqdO4IFeS865iwJtBxepAfhtEdMg7dss4xD6ao6dQWRhlN3vbmH6-ELC4hD_DcptKj4g77cr5AJw7Xwp5cDGPTLEhOhuGgqWgGXKUyVHDHOT7GXmJOlRFFiWkQ3xOygfjXs2HxYMdcuEYgSo5MRNQjCSG3-wBAzxfQ-5jQFanHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/23053" target="_blank">📅 16:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23052">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=NzcHMK4QQzN8Hg_YQ52-U_W35kcq7UXQ6B5H5x8iWQGEfteFTCFjmKjoeqabDz164sCtrUvM1thQDej8Ws_2bl6am4vGiWK1uqIxvZdSQmo_D-sUFA9jWGlmYQA9kJ-nYpqCkNM_s0T-XBUc4AtIjOExTXUg3Zmtks66n-mLN3VMDhVj4n-LgP0E6SviPTRQRWBgoViqQfOIKq1Np-SVfyuWdil0fhSs_Zpu2pW5acGNYGZutbPxqBvf4wlcdhOJ4Q733WJN4Um9FKhA6O5oKHcyUx_lKE2Bmy3CG1tQR0WvclDmeCOogiXsrooGT0Q5uin1Mb9uvC1Iuwf7l6VBV7EfO22BOODjVktlSPLmuh31BPyKQ8uqenDFdc0bcjDEnHv1jKcOktVSULTWTiR0sFmNVzPb5rEsplpxKj-oi8EdfdCwEEx2m2zbpTVzCqagmhDW0YX6xM0JYieh7jffGjY8jV4e7onYblk1bq6tZ4N4Amol5SBAfUiBaGtADfzHGQc8ZnoIN4uhalIWsSZc1IkM0gX_-kTlUDmbBENRynYCVgwMsbVSNAgFts3iakepstbmekPGoannmpNhtSzz9I7CVqIGAhepVFEVKQVnY096epMy1M8C6996T7j38ylU1Imh3Fb5T6zPCSnY_IUomdATEUVxZvjWPvb_wljuYhs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=NzcHMK4QQzN8Hg_YQ52-U_W35kcq7UXQ6B5H5x8iWQGEfteFTCFjmKjoeqabDz164sCtrUvM1thQDej8Ws_2bl6am4vGiWK1uqIxvZdSQmo_D-sUFA9jWGlmYQA9kJ-nYpqCkNM_s0T-XBUc4AtIjOExTXUg3Zmtks66n-mLN3VMDhVj4n-LgP0E6SviPTRQRWBgoViqQfOIKq1Np-SVfyuWdil0fhSs_Zpu2pW5acGNYGZutbPxqBvf4wlcdhOJ4Q733WJN4Um9FKhA6O5oKHcyUx_lKE2Bmy3CG1tQR0WvclDmeCOogiXsrooGT0Q5uin1Mb9uvC1Iuwf7l6VBV7EfO22BOODjVktlSPLmuh31BPyKQ8uqenDFdc0bcjDEnHv1jKcOktVSULTWTiR0sFmNVzPb5rEsplpxKj-oi8EdfdCwEEx2m2zbpTVzCqagmhDW0YX6xM0JYieh7jffGjY8jV4e7onYblk1bq6tZ4N4Amol5SBAfUiBaGtADfzHGQc8ZnoIN4uhalIWsSZc1IkM0gX_-kTlUDmbBENRynYCVgwMsbVSNAgFts3iakepstbmekPGoannmpNhtSzz9I7CVqIGAhepVFEVKQVnY096epMy1M8C6996T7j38ylU1Imh3Fb5T6zPCSnY_IUomdATEUVxZvjWPvb_wljuYhs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی‌از آندرریتدترین‌مثلثهای‌تاریخ؛
شاید اگه بیل فکروذهنش گلف‌ نبود و ژوزه اخراج نمیشد، چن جام از جمله قهرمانی در پرمیرلیگ رو بدست میاوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/23052" target="_blank">📅 16:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23051">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yew2zAadQ_MFxtB3ZcgHzWzgOoUVanpvxJBpD0sHHEQ_iDUx331AQaYHTvg0Z6GnxV0munlYb1TB6fTJ7lclcDbAAu5UisWzDvr8YULL3XXHpxe-kRNd-Xx0KOclgS6_c-sw1MOl_UCLqsQYX-F1TvLGq2zV28cSvjOLZK5WHe_ZSZBM8AonWoXE-H2oCx9Iuo1-llfdzpxNQLHUq6n2Mg0QL8AZfirnYKoOjFV6ZsgDxhRDavqGeJPoUr09O7fd_l9OoNfMgTrco3hRdvvqP56-rvjMLqTFRr8ifipwh-vJuUwXvByJNMdsPM0lDznRh6DEjYCc-_4G2bXOvH7l_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/23051" target="_blank">📅 14:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23050">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=buWMit-iRtLDuIvztztIzRbLd2mxJhl5DsgLzWy4PpLbR6FYjboe_6EJC3s20yqhcBxMG54fUr3JqPFLPDz6L-pnN-RtSVT3YgGGisTi2yrQSpEM_NyQDjJbegUsi6UsKipgxpyyuBSig7AtX-T35RN6ZiMQhnktvl6ruiWB5Tl1uAamHukx1sBtpdOaz2Os4B5HMHHZrVudBkzG-ZmYfCV100ONaS_BOWYjjsdjyWKK2P2uZofU1-HB1rqzYWsCwjrcc96AmKt9CTlnVtPp6Gx6iX5zFYm0wLctcnaUILlQTW6w4T2PFliZnI56kGGDwocgv_oPZG2D8aCD5JgBzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcda08a029.mp4?token=buWMit-iRtLDuIvztztIzRbLd2mxJhl5DsgLzWy4PpLbR6FYjboe_6EJC3s20yqhcBxMG54fUr3JqPFLPDz6L-pnN-RtSVT3YgGGisTi2yrQSpEM_NyQDjJbegUsi6UsKipgxpyyuBSig7AtX-T35RN6ZiMQhnktvl6ruiWB5Tl1uAamHukx1sBtpdOaz2Os4B5HMHHZrVudBkzG-ZmYfCV100ONaS_BOWYjjsdjyWKK2P2uZofU1-HB1rqzYWsCwjrcc96AmKt9CTlnVtPp6Gx6iX5zFYm0wLctcnaUILlQTW6w4T2PFliZnI56kGGDwocgv_oPZG2D8aCD5JgBzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
تیم برزیل در جام جهانی ۲۰۲۶ با هدایت کارلو آنچلوتی و باترکیبی‌ازستارگان‌باسابقه و جوان، فقط با هدف پایان دادن به انتظار ۲۴ ساله برای ششمین قهرمانی‌جهان‌واردمسابقات شده. اندریک قبل از آغاز ماجراجویی‌هاش در اروپا، تمام دوران رشد و شهرت اولیه‌شو درکشور برزیل و بویژه در باشگاه پالمیراس سپری کرد. اون با درخشش در فوتبال برزیل به یک پدیده جهانی تبدیل شد. رسانه‌ها هم سر شوخی رو باهاش باز کردن و روز تولدش رو با پله که اونم ۲۱ جولای بود و ۱۷۳ سانت قد داشت مقایسه میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/23050" target="_blank">📅 14:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23049">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tsg2etBdzN4lX2AiQmYHts1zp0oFDD6-4C4Xwg3I8_LvQDtBqzrNkl-7TgmvSn6jt3oJ6z7U-hFsI7dsJlpcfXnh2rtZYKJvJ6WnUhmzxfLQ4wnVmupzplYzCNRId3hw4yujFdQZLJodt-kGUKu4NXQWznckh27FUgR5kZaW6HGteYZi1jfsVbRqUyBn-TYOYs6NXIdD8AlyxDueKA2ScI5ZokJvc0BBLNZNA59vNGP0PUkLXeMyrw8MhDfFuz2pBCN4m4De2MZAPLU7rJbQ7v7HffwAwz0FH6ww9V-N95egjMtMmd7qglWcClqoQl5LYvkOvFOmj-XT2T2d1m8YBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/23049" target="_blank">📅 14:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23048">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT7wmEM6szrPOtr-U-zQ6KrBqt9cEfo3eoA8hT5l6NSP6LtjVTWvI-A1ZMPDBvvCorO0sgvAov5UCavA--fkVdh6wRKP8Gfb7OYDj8LVwvUE_9kBqCcebB8gRj69FblmEsBbZlZbehnf26re4SQbtkb4C12kKGpOQJ6znB48h_o7WNwzB9GuuB6lCLmk5BGvj39pauOlYDKwm5dcKd7xrRcXHLs4b1M7P__PHeP6h_wVIg7ZoqUQzB9bnPDHZ4dz_aDJsIBLZO2xFNUeE8DBb2d_CeHIC0Hqt3BJ8VQtHWF56059pivj121jnB6Uw4YHOn0cjVLVGPFAF6Cz04Wezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/23048" target="_blank">📅 14:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23047">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2qe33IPj1kC7tjToouMyU-j_R7N0pq7ASENWGUfNcHrtpIbHaql1HPUdtBG8mcWlXTUZhC1t7GZaKeizMYvXSBAwJM4XaXRPBr89Vx8UMAPmzBT0RlIoJuPCaL6kSW5Hk9sJbizY1H3m_RwZrHviEzQ5YOdg52xs2LwDQzxf5QpKPOBYiP7iuAsUOvD2tLT6emHl3krhMEuyBZTuKd4fnhvgAqXKLQMuWr8Do2dLYiubRcQXv-sOayI7WiSLvekNyNV0mSddN5YSgjEYYqbAx-C8gFH_hyMT1hXsvzUEzgaRrMteZI22dpugQm-OCAa5ISnuWa77q9u2uXvwPvfJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛
باشگاه استقلال مبلغ رضایت نامه عارف آقاسی مدافع 28 ساله‌خود را 80 میلیارد تومان اعلام کرده. گفتنیه باشگاه تراکتور به دنبال جذب این بازیکن هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23047" target="_blank">📅 13:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23046">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMLc16rviNJ38l7Q40CCFvHXoVtGlwHt8iixuLDaUHv2ULvIFOAepM-jpZYRBDrno41t-bUYskQZf9e-V8t_A5cTl0f8uXSJmInT1eDG1yiLQpYWP3gZyEgIzNFFz4ZpiCMeGFKaZkMnCCfauvQEeodkqzusiJfJYI48JixwF4FrskME_oSl5APEu10fz5St2tY08_ps3uW3L1COXTF_2MTu50K97XD5PNAPwBPHB9t4oq9G_s7aW1TFDFET7gU9jc5digrLZOS-ftIXYaJWboU1zUnOgniHHo95usdaLwOBV3XxL42Dn-P0Zr5PMzM4L_4C4L9RZKiKSqbDtsFw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ‏گویا پیام‌رسان واتساپ در برخی نقاط کشور رفع فیلتر شد. از یوتیوب، توییتر یا تلگرام به عنوان هدف احتمالی بعدی نام برده می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23046" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23045">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=krlPoOcEYfklLDQ8a60NUu2DbF1fgL0a_h-FvqAJGI7LHemY8nGyB8x9Pj1Rp6xN8LaI8zyM9c5K99RMqcmT_jmcR9rxkXAIZzee6wzLv2ejiVJGxCCPsT5SQKr2Vxc7OrcSeA-sO3ngGPooZPP9RrYcP0AeZkVJZyPbQ6JHXXjcJC4wk7c5zlVpM0PzUMoJo06VTlaVSeV3O_gcC5ghNEm_LLFFywzATkXYPRwsAZSJY1D3pVy-Ugpip1oyEOL4XyCAu-zuueMzwkIYY3spdIaoqQ2i3aj5HkwEbGsLJZSTaePlMmoKgNGstCMH-l6ii-H6OEHRlQU1nr-BsKZKnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef75c0b0e.mp4?token=krlPoOcEYfklLDQ8a60NUu2DbF1fgL0a_h-FvqAJGI7LHemY8nGyB8x9Pj1Rp6xN8LaI8zyM9c5K99RMqcmT_jmcR9rxkXAIZzee6wzLv2ejiVJGxCCPsT5SQKr2Vxc7OrcSeA-sO3ngGPooZPP9RrYcP0AeZkVJZyPbQ6JHXXjcJC4wk7c5zlVpM0PzUMoJo06VTlaVSeV3O_gcC5ghNEm_LLFFywzATkXYPRwsAZSJY1D3pVy-Ugpip1oyEOL4XyCAu-zuueMzwkIYY3spdIaoqQ2i3aj5HkwEbGsLJZSTaePlMmoKgNGstCMH-l6ii-H6OEHRlQU1nr-BsKZKnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
انتخاب آنتونیو رودیگر و لروی سانه بین کریس رونالدو و لیونل مسی دو اسطوره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/23045" target="_blank">📅 13:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23044">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmbZLcXnc3z2dLT-Nj6eeDUZehMj7eOWysATl40qXTdtUMuEK6LldRKd68uyPC62jvU0gMx3dMhETN_D6HpWA4kImZZlfnhuV6KNLcSqckBH0AfNvgfcipwCeFom6AO2gkq4HZ9KhjTzQkwZmLmZHJhbZq45G3YCMQltClXRv52vrHd5yWbQPrGrl_XPc23p8GHX7UMhTSt2kEgZOrJsKpUb-V9W22ZKT0bb7njaaGFooNPuGJGkV5PfCx1Jsemy6BE96BU2G8cu88u9YOQZpfIILB0TJx4PXoyABBRnxp0gx-1IUdpwd8nnk4ye5ZEf_NqGSX1s6H-HoBNAs6lnnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: خوزه مورینیو از فلورنتینو پرز خواسته هرچه سریع تر از بین یوشکو گواردیول و ریکاردو کالافیوری یکی رو قطعی جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/23044" target="_blank">📅 13:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23043">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAQ7DVWmQi-xpsbtMiqYZk7vvo06l3WF-hO2OxCSZUsoOAMXZES_B6esQWVo3rSB_c-C-5EqQia9s8RwZOFBSAJ9EJxGSbzJ54Zfb_Nqm3r9szzl51VoFu0CCPWfLNvpJXm4CrCBYV6fmiFEi0RVyRHeth1gy3YDV6-lNeyjekjjfS9XIuvrQXyNSUMqf7lKbKXSNqFy2qldWBsaZw0ksc-Bqf0u8Lgq5307wCUrpxhvXAbR4vVKMBZiTcjO7QekkFZ0uROCECJbhEtES3MmwZGLnlHzJNm3XvpiqqJvPgAjE_64Q_aaK6cOJxBf30TgLWp8ADRYoCTJx6OEvNK2zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/23043" target="_blank">📅 12:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23042">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LknVww9Df7rY128ET6TqIfQcmYZG8CeKReUxUjUjVHQwccTEgj3L94ETjWuHk2MvvQuTTrkMR9Sichg33SU5OzzxXJB--T1e7VH3qGK5UKkJlYEco5Aa2au7ahzOg3noMV0CRBHyg9ixn5XJ6UJBpLB6NHcUTuVa-u66WrQYDDnnXWyKSkUO-wFkoL44hIJCOjFfYuecHNd5_p7ZrOWg0jpx8jmWt9z-TgwkAkOKMsYHqSnmo5lYDwThrBbolRGxmHPMcHyOGVBY_xUYKMQLlliSGa-Keg_1E-KIIHVGjZiOE3UDGkQki9xHZ2bcGCUdhqVc86K4zKGfbfBFQnAT0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تمامی‌قهرمانان‌ادوارمختلف‌جام‌جهانی؛ برزیل همچنان پرافتخارترین تیم تاریخ جام جهانی فوتبال است و با ۵ عنوان قهرمانی صدرنشین است. پس از این تیم ایتالیا و آلمان با ۴ قهرمانی در رده های دوم قرار دارند و آرژانتین با ۳ قهرمانی در جایگاه بعدی قرار گرفته است. جای…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23042" target="_blank">📅 12:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23041">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXWBv2UqgRD1JqoB54itNYpcBzCKDZD2JrGGPysBj3g6FTMCHFChL9N8LkLIIatpMDWAODsAcoSIplMhS6UCcr6QPnGqGxQ0lGk4zcom8UTzO4fsBpgowC_vh4fcpDhvp5MMETBuX4jd4E0LzRqEUT8UfOPMsjkShAnwlJsY3thvoAg6OjnpY5nKA3CRkFH1NHWsTLmU3K5yOxGODO_y3BmNjbOlDRrG-3wSUWKqtEYnY8sDTLFZSrb22eFxdadANeKBrenb971w13mQoA_zMZs6jnxMbGp9B1QpogVp8Rf_ASTfKCP3Smzd8t9UnhjRXphUWFQEfo8HY8jloUqPBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/23041" target="_blank">📅 12:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23040">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiWqMVfXBMKmOjRFgaJLfLdkqWw6Wm4RWeVZ_ALp-cEli-bSfSUVUshIv94mHqGimVJP8jKIwXleknD967Woe1hyKDZX7EnWdDz3tuYZ_BXiZYOGYtjmxzn-XiN0GYGBewRBB9-KtByaAkE6qB8dz3mXP_1b51QVlw9vHfqbFx8Ucb8h2qwa51uGqviVydxsSguzJU-PyODWVkucq-XEYyUR-RAOs6lWKAKc6HINLtSZyWTODgkarbQBS02oPYVZC2n78L3dXlIUY2yXGbt3BJhLfxyYeBTWqvVuF0q6MOII95R80Mk9OJEwL9KtRLpLlLS0HtIv23Bl8DE7N4Ti3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ ایجنت کسری طاهری به مدیران باشگاه روبین‌کازان‌اعلام‌کرده که این بازیکن برنامه‌ای برای بازگشت به لیگ روسیه نداره و قصد داره ادامه فوتبالش رو در لیگ برتر بگذرونه. باشگاه روسی‌ هم اعلام کرده هرباشگاهی یک‌میلیون دلار پرداخت کنه رضایت نامه طاهری رو…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/23040" target="_blank">📅 12:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23039">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4860b42130.mp4?token=XKxvPm6p276SByxbf7prwu0_0Pxhdak5faqr-UQY2tSwIdBXI22xgwHzJYpVIjzqJkcZd6JqP53ctPar-w5Q7RQDh5BDsMnYuJa2jVVrX0xlYE2mCioGSO7ZFioFPsUCqPnQFvFx9VKQ6z9fgZLTht59PP8GsSc58hxTpQonQTZJ8ALs8T_pWTadyBxQWpRdILl84JEcGYNd1IwILWfq8qB1CFOAJTtDfNziaF9JZJv4g-HC4BjdMmxqy6S19-5WfvFb3GHt5ttQRtrFkUCODg337FCXb0XOS9hcn55FC1ayc0ukwn6ZKZwbF5oGg5bNjBUq4YTkoTlb69Qyzr5KNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4860b42130.mp4?token=XKxvPm6p276SByxbf7prwu0_0Pxhdak5faqr-UQY2tSwIdBXI22xgwHzJYpVIjzqJkcZd6JqP53ctPar-w5Q7RQDh5BDsMnYuJa2jVVrX0xlYE2mCioGSO7ZFioFPsUCqPnQFvFx9VKQ6z9fgZLTht59PP8GsSc58hxTpQonQTZJ8ALs8T_pWTadyBxQWpRdILl84JEcGYNd1IwILWfq8qB1CFOAJTtDfNziaF9JZJv4g-HC4BjdMmxqy6S19-5WfvFb3GHt5ttQRtrFkUCODg337FCXb0XOS9hcn55FC1ayc0ukwn6ZKZwbF5oGg5bNjBUq4YTkoTlb69Qyzr5KNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویژه برنامه جام جهانی با گذر زمان؛
از عادل به یک مجری وسطی بازی بدرد نخور رسیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/23039" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23038">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmfoiyLAHzGcaOa8SkgH1-9JQxFmPIRo_2cWThvCRKHPxAyhFDpOCKKx1ySgZuOsXmNWI2XDLJRLTqTMwRU95RfDbSXXhBIWDXruNEDSUyZoov3i2QSyYq074s1n_4o_rgduoRim7GVHHNyiw3VioJEpNkOQjsZo91U_d5S0lIx_n6cE5dG1-Dn1Myish3AT9WE5-5LXm7363OpVMfaZsxnTFbdNA1GJhXeVQmTTuJ92iMSkqRyFfr-2qFKS7xJCjfo_ZrkQgNzQ10QGBmS6NLfp65oSf8Lk9fsbn6rPDG1keBZaIaYNCqAmN8Wtgy0hqvIdvOjvC5T6t4VILK4-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تیم‌های ملی رکوردار بیشترین تعداد پیروزی در تاریخ رقابت های جام جهانی؛ برزیل در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/23038" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23037">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWijbUPh0K-U1W2b5o7u3FDjYm1SZhbDJe9uGyyKAkaUcENnNKxAAR5E8ruQZkkxVuI-2K4nLBwvKDMe-V9FdiTuKwTgIKXknmpSSzKcZ3kBxstmO3MoDGqMRwTyQ_8fMpafr8nSYRq-FZwK-0QPGZhWpwGlJiSDk86_xoPYHxWl1PciLcHx9603W6cZN80e6LursdMzdtC0ztNLXo45oUw_0KVXrZEqeUErQCiF6YNMvHu3MeVbEiORj4Rmk10liClIiqnsbNe_Y7AxCNYcvo7e7TMRKnCGewTA5H9q55MO4qt3NQL_4EfEMzg2oBd83Q1xb0CaNMUPJTRNbrjbqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد.
معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس‌اضافه‌به‌ازای اولین واریز
💰
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا er19
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/23037" target="_blank">📅 12:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23036">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYRtMpGi7Mty7ObaJjk9FEmLAzAnvazpY0XjFlWliH9q8VoNJmx1LR1v9XLPt_XsyFEGE8y-O_9bh1DxTZQMNS5KNljdw5ZIFXs76x3GPgbQxvNXhaUMt-5nGw_OZXYjZVXgdKc0BM9j5WnBUF-CKPQ1ev8xTTa84kZ1uF-Zjf4bN7hkQQXBsVPVMi49iPuhPFHczn-ww4eDKFdJoMI5z_lsAMN6Fp5IjGQsvNII2Efxdwo2XM626PM-wk-AG-XBsKsHDE_RDCbhmKbRQodLltd02faz3rHX6GQAbYhp48jbvLch7VPEEynQVmgQtsHZy-4WSJrSphBx5XO8DnmePw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/23036" target="_blank">📅 10:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23035">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0YVhUJXTU10uwXiky_KY0URhm5tDhRUvJYa7xvhdHPUD1Gw2h-9XkmerMmcnDci6JNpag7kqG4KNemJ1ty6Q5JjkzGmaRkT06116ZnaSLOzR7xAdUz7o2ZH2zIX7dV_Ttz_F-i6pcUNjMDJuSsiPzNtMQHcaJFQTaEcY7lDW9aqi0BGD6GdCTZcR9w-YIA4jIt-d5Am1GyPMYlkWu4fGFIbJ_lVGX-rXxGYcphgectLf6ieNy9j7ZHFhDkN6Bl8Ws6ryTxksolj2xF9cJma5WXERXlzgv_1giPhvWLuUsyQCjRlmETxEhvB_CxSa3H3y4m5anKSJx9me9OZBs8ufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/23035" target="_blank">📅 09:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23034">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fkg9zYenmye9UK2ZewhhA8J3Lf4cCllohQoqRj-8ukokFh5x8Uc6swzYFPHAjIzhBKqEblkKQ30RpHzKzGx9ASXyKDd--Q8AePQVoO3riC-ZEtRXIsSkVjPLCqXeG2wNEYm4oFo4C70rTjE8dzWeczIy4YvESPIaEZW674Bqb8NVue4ogizTYeQwV738dsCAVJd92VFVqCP5o8DPa1lZHUMXvuzlbDOqwVAqPBvBG5GmAmPx1D_bblIVjf1afjIfDTsCdyuRyuqIVx9nQYUSmCM92mRTZVSSVvYGcpC5v1VjP3LA6FYvwmxaoGHsE0xh_XXD6iVhOMOKAA4_Jc_xiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|دیمارتزیو:
فرانک کسیه پیشنهاد تمدید قرارداد 12 میلیون‌ یورویی الاهلی رو رد کرده و میخوادبه‌رقابت‌های‌سری‌آ ایتالیا برگرده‌. یوونتوس علاقمند به عقد قراردادی سه ساله با این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23034" target="_blank">📅 09:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23033">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwMR3l4IW5sWy2RMEcSsryLXqh3wYpguqiZ3hejwZyaN6Ld-t_S2XZMCeRjDXHVabRbB9bzU7OQVf6Hv2zokP9W_Fg70emkkJp9I329zqtVt8LdS09CxFEGFrFY0wwA-hrcXe2-GW3YGVP14B9jySOtDXlZrjk4UvLIkuf85s8YFjMxJqt4BNQHtCkayi0G7xzGOi6tUwN0EjPHid7dg8e-AOEa5kJ8CdtF4N4_HklpYLrv-qbSIdRguLPvuAhTUshQ21QHFynIk19Y3yYalpBB5cLX0aaTDucx6yI03ZibNzNL5u6OZELB2WjhoklR3C5OC7bsdMeZUcSzq-MqRqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/23033" target="_blank">📅 09:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23032">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvW4IIxuUozh8nRLHPHUC895F-5jH7M1Sj4m09w1uCLnvXGjk92TMZfM-FhcYS-nQDx6qoyAeNZLCMRkYR2tovGqmOZPacPuxiWzNQ2gaA74pMKzqWrYtW9eaNhcCgo_s9o5_I8-jxMLz7J9cK7eFUZC7edFTwKcl1cHKp4OVG7i_G3gSD6iaix5HVU165UejnGZqkkoo10KmTFPuat48m7VRqe7J74dxhMm7Nl6q54gXRHQIpGtOz6PLpcGuwi3q__wUVPKgP479gb5MLbP2Xl34KtnVe46d2rHywjcqNk9_Hq1ANaxU-7ls6thu_y55dDU7yIj8blJK5yXD05wiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23032" target="_blank">📅 01:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23031">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4rgduGVaTCA3AP1RhEsCRtFK67yOXh2C3bhnWRw65ecRbIV5GjBcPSU8JNfawjrBGF1dIjZKZk61PWrI9cePy6UapTRO-9Hlpdc3iH0tg-fz9p0ZAd3oXmQudpSvDROa1M8emXomeBBg4u82AUmzX6f7KRvUoqr4GHLGmPay9qnNcaOVGsSBpFJBiZUzyFScPgzi4x7mlkf1bnKuh1JnmhO4zIWzi2zVHKwbHKf50Zv12d9s4ZptqpJoc6VUUNbER81ujAIkcfBd3ox4YTASWEyzvU1bvTTRhMhZhx9OW1xiXyO7gZRKLhQb057P_wtSNEvepkE7M8r3B3aDWVDfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌دیدارهای ‌‌‌امروز؛
نبرد تدارکاتی ماتادورها مقابل تیم ملی پرو در صبح امروز در فاصله تنها 48 ساعت تا شروع بزرگ ترین تورنمت تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23031" target="_blank">📅 01:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23030">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itu2OZCf8Bd-tIImbx2mBFdFzSs2fCo6frASPGHJWhHxaciopOzbm8J9RV8_Ilh61YCeSeGOlt2yZnZ-bh8at_CO734XUY-qNhbMkLPrwT_PjmK8B1P-R_20DSrZ9v7kaIIOV8Wi6xoAyHwiKKNraYhx4iT0guicFmlYtladQFTY_0S-I-_O8EzMzKq4cMEPQ9SPQABYAVknplBtvwUHzmmi0Ab1ieD92eZaxOOeBsyfNI5N2c_HazroRD8bKakc_K9cCxCPxxNkUUfLXx1WzfAFRzqo4kNgG7w428h4SOpSjH2mzNcXaHQ1u2xaI99XbOdC9F-JGrqRRxIuFN-3AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
ازبردسخت‌هلندی‌ها مقابل ازبکستان تا برتری خروس‌ها در شب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23030" target="_blank">📅 01:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23029">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=kr-WWsVvvvZvcjfHM-z0ZWsTq0LMIYibqaJeXdVXlsBwhdOV-AlXj0H5AtZ4CN4zFBZTa1AqS2cVWX3KrThw3ZvpFwLucrL7eZtcs-N46RXovg4ZycVXiD-kexjfnwLhpqPrg08o-osZoMqPgrMTWpSewAJm6pshI9PoaLxUezDYE1uLvNPpBwIAA4dVNMNbSRnsC6fnMR9uRE2oJ-BmfMkEQ2qI2r5p7vO1CHDylbaP9hmeqQ_-ep0kDHcOpuMtxhiIjleHKlLIOYjlGlQgv00dYremWPxz3Naj1SHFtzxkSWhWu7-v-2Yffq58YcEr-4h6FV5ytMFbSuVeqE4_rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb89dc70af.mp4?token=kr-WWsVvvvZvcjfHM-z0ZWsTq0LMIYibqaJeXdVXlsBwhdOV-AlXj0H5AtZ4CN4zFBZTa1AqS2cVWX3KrThw3ZvpFwLucrL7eZtcs-N46RXovg4ZycVXiD-kexjfnwLhpqPrg08o-osZoMqPgrMTWpSewAJm6pshI9PoaLxUezDYE1uLvNPpBwIAA4dVNMNbSRnsC6fnMR9uRE2oJ-BmfMkEQ2qI2r5p7vO1CHDylbaP9hmeqQ_-ep0kDHcOpuMtxhiIjleHKlLIOYjlGlQgv00dYremWPxz3Naj1SHFtzxkSWhWu7-v-2Yffq58YcEr-4h6FV5ytMFbSuVeqE4_rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
سوپرگل استثنایی مایکل اولیسه ستاره فرانسوی مدنظر رئال مادرید دربازی دوستانه امشب فرانسه ایرلند پیش از شروع رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23029" target="_blank">📅 00:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23028">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBdnjtzHLS-7xKLim5t_gCLtu3YAOb19oVxfkWge-gQeVxr4Upi917fIfIijyB5F1I_PQEBBS4fTqjQ8i-P9Ml0p8J6ZLbiIiLHRiN8TIBdMpkEl0FDwQyUSeYdwLTtx_979whrp_1L88azMXgHWXQX6aPbC2tuPQY80ixjqqoj87gyvUP0HMiY_i6jV1x2z73OdFfG-z2YQEv01GQmdwLL9AJVf_mSYesXKF8fleGSuweMSI_ym1SkaD096hfKthswNOYYw_XV-MybbdQD--qTKd3WOZdOJ6GYk2netvC06kL-5r3EdlJ4CBdjBYOcX6JTEblAU7tMAdj1-XluJxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا:
فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23028" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23027">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=Bx7ZZHFECw3rowopqyRx1hWoSbKbfyZ3AAAi-_p0ROXlfUqA5nuf3oYN36_Mhy47jQ5XI_eu6VUHQlcvAJMuozrFdAvoZynlUBLuICfMLl3MMb_pI54-8_jRiKD5b7VhCKDoN_Ka-dRPpiV8dFbMRCGnN5iOTdjkUtr7M0akJedRF6zCvWsBN3mu86rTaIcJKPB-VpB0W055lypDl_wU88raWBREtWPM_PnouZFKoZ4-iy_0RcjWYxq8KTQw3ahdnIbaKpBuV4npqpa5WDrsM5FmVBJqh98fv7PhM8L-tEEzXv1V__YmvwUniQqmsjGDWWrpAG_ESf882JgdyPPMkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f877f10f.mp4?token=Bx7ZZHFECw3rowopqyRx1hWoSbKbfyZ3AAAi-_p0ROXlfUqA5nuf3oYN36_Mhy47jQ5XI_eu6VUHQlcvAJMuozrFdAvoZynlUBLuICfMLl3MMb_pI54-8_jRiKD5b7VhCKDoN_Ka-dRPpiV8dFbMRCGnN5iOTdjkUtr7M0akJedRF6zCvWsBN3mu86rTaIcJKPB-VpB0W055lypDl_wU88raWBREtWPM_PnouZFKoZ4-iy_0RcjWYxq8KTQw3ahdnIbaKpBuV4npqpa5WDrsM5FmVBJqh98fv7PhM8L-tEEzXv1V__YmvwUniQqmsjGDWWrpAG_ESf882JgdyPPMkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
باتاییدرامون‌آلوارز؛
مورینیو سرمربی فصل جدید رئال‌ مادرید برای کنترل‌کامل رختکن تیم رئال، پپه رو بعنوان دستیار خودش انتخاب کرده تا بتونه حواشی بازیکن های داخل رختکن رو کنترل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23027" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23025">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=ZXpD48S7IM48cw-WTJSimkVe0Onool0j2mibn1CvyJggW-E_9hZcgTMak1-z2xmAwSIOODFMJDYzKz70HSVAiS_FQj9ztVV7y5yraKcJY4cH9ZuNHTv7_4i6rL-uCV1NAgdOX-v2dWVq8zD-Uf5pcveXWct9ica6mXi5UNMS5_u3w87p59oraOcJ0as3hLeQnqR4uS8WS70FnvHLYrqbU8HdaExuIk8zAPebW80pmd3-CQBHhRBrq4RIdwBH1tUpVoPSCYOylB8a6JtFwZ54durxsutXtJbMdcY6J2700kVf07uMjEdF8UdBAl7HQMJvsaLhlfXbVzysfxVQ3AV7zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61689d1d82.mp4?token=ZXpD48S7IM48cw-WTJSimkVe0Onool0j2mibn1CvyJggW-E_9hZcgTMak1-z2xmAwSIOODFMJDYzKz70HSVAiS_FQj9ztVV7y5yraKcJY4cH9ZuNHTv7_4i6rL-uCV1NAgdOX-v2dWVq8zD-Uf5pcveXWct9ica6mXi5UNMS5_u3w87p59oraOcJ0as3hLeQnqR4uS8WS70FnvHLYrqbU8HdaExuIk8zAPebW80pmd3-CQBHhRBrq4RIdwBH1tUpVoPSCYOylB8a6JtFwZ54durxsutXtJbMdcY6J2700kVf07uMjEdF8UdBAl7HQMJvsaLhlfXbVzysfxVQ3AV7zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
خوزه فلیکس: فلورنتینو پرز در کنار اینکه 150 میلیون یورو برای جذب مایکل اولیسه کنار گداشته؛ 150 میلیون یورو برای جذب یک فوق ستاره دیگهه کنار گذاشته. پرز میخواد این پنجره دو فوق ستاره به‌ارزش 300 میلیون یورو برای مورینیو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23025" target="_blank">📅 00:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23024">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=th4Hz_u_mrpMqrl_zGKhhotfIUjK4IPFrmM9mNnoFC4o5x9iPEAplH5KKmeoL_8mG0A7iYu4TZAWezU2N6ks1TwSko1PAbHHOGr2Zc-QGlmTUaBF45IKJiNQ7G-MzVq2sDRGsgcN4ITVe2BBWEzJD2rA5k365nWQMfMD0RRuWL3mjMyHwV3qNcYggmw57gyEqBNCjH9tjJv2-PpraS5BUbdYY9_3ENCu_YfYiTk2ssJcXyw_IEkIBBdU3QUW5Rah74A1VtJRbTGPDCQXd-sVg9Da79emR7AQJwZSWtEAk_mTpMDcA3aA5vc5HSqs16LrhZxK_DljfvoAcB8v5rcjcZ4dk0is-_ApMUxx0f6jxKi3vEorTSQ_OYy8_M5vpzjr-lBJk5pPpQj4cmsrSpBnN4x34Snju2CDoxM8LH1m6TVfU6Im3FrdQTCB4rv3hhNslaRht30gAX6IvSTzDDv0pNSaVTDo94MU9frRIT8hM5wFyMwpGHrWdQMImHObTwRZFj-79zA-pQzSzbY9ZEZPS1z8HYl1fEeKjGfqRuw5GdcJda6Up6OSKlorAy814DJ_njZ2HxlBEyaEuUNqAVXAMXqNx3ghUPZCbdOxqMzV7uTwO6eSpYAuc4yaNaAtSjuxkifCiXNJTqDAoqLfKSuJ78V34dDWxQoNEDmQu2JJ9ro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fac563f1.mp4?token=th4Hz_u_mrpMqrl_zGKhhotfIUjK4IPFrmM9mNnoFC4o5x9iPEAplH5KKmeoL_8mG0A7iYu4TZAWezU2N6ks1TwSko1PAbHHOGr2Zc-QGlmTUaBF45IKJiNQ7G-MzVq2sDRGsgcN4ITVe2BBWEzJD2rA5k365nWQMfMD0RRuWL3mjMyHwV3qNcYggmw57gyEqBNCjH9tjJv2-PpraS5BUbdYY9_3ENCu_YfYiTk2ssJcXyw_IEkIBBdU3QUW5Rah74A1VtJRbTGPDCQXd-sVg9Da79emR7AQJwZSWtEAk_mTpMDcA3aA5vc5HSqs16LrhZxK_DljfvoAcB8v5rcjcZ4dk0is-_ApMUxx0f6jxKi3vEorTSQ_OYy8_M5vpzjr-lBJk5pPpQj4cmsrSpBnN4x34Snju2CDoxM8LH1m6TVfU6Im3FrdQTCB4rv3hhNslaRht30gAX6IvSTzDDv0pNSaVTDo94MU9frRIT8hM5wFyMwpGHrWdQMImHObTwRZFj-79zA-pQzSzbY9ZEZPS1z8HYl1fEeKjGfqRuw5GdcJda6Up6OSKlorAy814DJ_njZ2HxlBEyaEuUNqAVXAMXqNx3ghUPZCbdOxqMzV7uTwO6eSpYAuc4yaNaAtSjuxkifCiXNJTqDAoqLfKSuJ78V34dDWxQoNEDmQu2JJ9ro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیوخفن‌ببینید اززوج‌های‌مخوف‌حاضر در جام جهانی؛ مراحل‌حذفی‌قراره‌بازی‌های‌جذابی رو ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23024" target="_blank">📅 00:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23023">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjbNaWFhjm-r-oh-3k-Di36HtAk9SLV1RWIR5tcFo2cOgb3XlvcBYb0Uh0JYnIdU4IQ-xbgD75DvkzJmE8sS6fSMJfBgWke8O_18BEV0IWOLeoTAhA_eKZiIE2FUVQegYBI0L-QQyaTyxNO_hSSa8ZRN9QEZOzvqbvUlQQv1BalQHzujGP6nHf8L7LkZHTCrFC23tMnZ7kUN_mtwjavZBi3AFzp_Jt1M5Hhl9kneksjgSnDV8YqE29YDCpPvxkQvvM_XQGCYG54mv42V1_YAh5evBmxQwdpsYePTYaeksbgvZ6tNrxNC_Wes-P21be2Oe5gwbRi2V8a3IJIiKZaucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌جهانی‌فوتبال‌قراره از 21 خرداد شروع بشه. لیگ‌ملت‌های‌والیبال هم از 22 خرداد شروع خواهد شد؛ برنامه‌دیدارهای‌هفته‌اول لیگ ملت‌های والیبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23023" target="_blank">📅 22:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23022">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKiAWFdKZLpT67zTdm0kglgGZBcLcBdqpicyV00iyEX1lpkMAxpwNUNMab22LLVffcVXsAOyYPYcUdbAwUCuKQ0zuOQH7bp0HIHcSqPQIvAPcnLiGvN9ApvG1Hgm55PX8CCT1JgiHlmwutZzpavMtqx-uxwFa2uFeQcKw9qfMWlJ_DM79ziCgzIERv4xN36AXfls01UaztNBw7E0a0xEG3YB600zvvOuUdriH9ukSvJckWHaRBkRqIty9ozNFNkeBDEeGWMFc33TG8VM49-mBWOo4ebOlBKJU0hWBGXdxgzMbhuZR9ORSk5L3E-D7wbB92XrpLCUqNrzfrJOVAPv9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23022" target="_blank">📅 22:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23021">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvG1o-5gKscqyaxBjrmKUIrmwUizyMjXjiPz_kYFot2CV4UsN6YILIcqkisWZaQ3Cl7IF6DjMXCJK9t7Trv0xKK93wTMCJyVuRzqMowWOA1Zx4ww8FdBwl5r_7U0KZRdtD7E6HRVlXcdjgyCqI0zEX3J4KYcWstYBVrb3u2Du6YOi9BETgRy4ksUQdO5ZDqVBEb6a7j1-53DskO1GP03wmlrAro3RHV4FzLczs7oDbAA3u3sh7a_RckWcyjd0gAhvQAaABII3ejDdfCm6EvzNsWvTQ9Er4R6NjX9FjMIUydwa8x3oswks8YnZ0qQqApmT9MFBlDxqHPAvzCSIAQ3Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23021" target="_blank">📅 22:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23020">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=ZuoouspTkyVj0aH-bRDdnUau3XSREdwUqE2y9rrkuUTF7WPE4Eir1uqQNiB2ZW1hSNqQohsQhd5VdYyH4211U9oJbbUSmrm6Ldcxyt_uEgkGL8DSVtmU2A6FQynlAdtbwwUaIvqPcPF50_9JUHqVkrGrCOWeakG1CKXpaVqlhp3KzgUSaLGjnqvNRVqrjzuTY6nXSxtkzDlWyNjopT5EE5oYlmGfHN8QKdCXCdoGdSro4M_N4nrJHbxAST4xHzwKrXC-09tgkS-4O2bUASN5RRRW_XxV0Ya1TdX2gFCtkOyPdWHk0GKawKCACVQz_j1HgTNPBUNfZtmjkQwP1nk6RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f3b11f90.mp4?token=ZuoouspTkyVj0aH-bRDdnUau3XSREdwUqE2y9rrkuUTF7WPE4Eir1uqQNiB2ZW1hSNqQohsQhd5VdYyH4211U9oJbbUSmrm6Ldcxyt_uEgkGL8DSVtmU2A6FQynlAdtbwwUaIvqPcPF50_9JUHqVkrGrCOWeakG1CKXpaVqlhp3KzgUSaLGjnqvNRVqrjzuTY6nXSxtkzDlWyNjopT5EE5oYlmGfHN8QKdCXCdoGdSro4M_N4nrJHbxAST4xHzwKrXC-09tgkS-4O2bUASN5RRRW_XxV0Ya1TdX2gFCtkOyPdWHk0GKawKCACVQz_j1HgTNPBUNfZtmjkQwP1nk6RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی‌پرشیانا توسط علی تاجرنیا رئیس هیات مدیره استقلال: وکلای ما خبرهای بسیار خوبی درخصوص‌پنجره‌باشگاه به ما دادند و تا هفته آینده پنجره نقل و انتقالاتی باشگاه باز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23020" target="_blank">📅 22:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23019">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQx0jLJzHiNZsXJNgDr1vibsLEqWYBZrrgGTS7e9T-tqOg84ufbyX_Zz5X7kD7DIzKK0gWewwYsxiuRj8FsJonzrMitToufF8e-nKbDO6bY-XvUMjNmsV4b68yqjkCz2lzLJtLpkSnSJ0XC4GB3LPlxyiGzoQnyN-IdPDPXrHkwMvBVVoX6NGXfrkn_I5IKDpTcmwdSpvr49xrtl4gNe2xJYT_eturLUE5SzMFbZOFoWlunsTdhO-zqi1jqT2b_B3VR0CvsCN1DhTrqHOGUPRxFGbN9APifr_0HreDR-x4MDQBzZWTgswnL9eEKwbDgz6FyHk3kWRY1Xm45Jn2ysNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛نشریه‌مارکا: فلورنتینو پرز عزمش رو برای جذب خولیان آلوارز در همین تابستون جزم کرده و میخواد بزودی 150 میلیون یورو به حساب باشگاه‌اتلتیکومادرید پرداخت کنه و این فوق ستاره آرژانتینی رو از چنگ فلیک و آبی اناری‌ها در بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23019" target="_blank">📅 22:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23018">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srOhyoH-53dWsxcZ3GVHMintgpHrjKvViE6oGna8WhDl2m3qe0n2Dt6F58TBfd_KXl4bJCnhe8q1oPVD3zPNF7ScB12kEmQhjMB-QYg9R4TJleUKSBxP7HNbUgu6HD0ue3Tl1myn_zW9DmW5YyuX2iZPrhwvfYhCQrcFzec2N8eNPcI4ZUgLlfg4RKr885B3wO6UYV6tDGAWlOEUE0RuA6JfGSCr1VZDknPhG6U1y8mZN1G9ptYoN1OhWjIpnW9qNQ0nWUuL9YQ2JTssh8UVmCeHBdHCLmRs6gKDyENQ5VRPGruHSICl6BgLcIv5ukl0zRauWp1GUWygwzUW5Fs-Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی اسطوره‌داوری ایران در اعتراض به کشتار بیش از ۵۰ هزار نفر توسط نیروی سرکوب جمهوری اسلامی در جریان انقلاب ملی ایرانیان، با بازنشر یک‌ویدیونوشت: «برای بقای کثیف خودتون، جون عزیزانمونو بلعیدید. قرار ما با شما؛ نه دادگاه، نه‌بخشش. رقص و پایکوبی روی…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23018" target="_blank">📅 21:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23017">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0kNwYH_ZLBOayak8ACbKnzKcHjIsLA7dGTn7sctsSMtbXE7daFv_42evz5gKfdeZa-G0f7gSnLu6UHnsHWmgBitS-0OmJS345bYurALu_qpnfYvMdclfsIqcGCHSQYSPEl2qxmEwnwOgoXmgOq93H7Vzz1cNEvOZI-zNZo9NY8mDUHQhonuf1elgxojsH4YHpzGIDJve-kNACYBThC6aTFkqnTi6UcGhxk1uscA5X-U_dAbcr7wnZekymKU-M5U4iKiFGVsSbhQbyPyPK4ZKn89bMFMNwWji7hfqyp9s1_DbwTAl-gzs_zmzZtX0l4qLhOPHJnVQgffkPDdjYuijw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇦🇷
جدول رکورداران کسب بیشترین تعداد جام دربین‌بازیکنان؛ لیونل‌مسی بااختلاف درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23017" target="_blank">📅 21:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23016">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHYeIKfR3K1U6vYznEOi2b7KzMNoyK1f3Df_Wq3KafcHlz30kfB_Q9ZwIARXC0J48P2w0AMitcdKA82Ab_EBzww7sqdv0Xl0SisYzcc8XJoZpiNPPjdhbWGgJ3Ji3iLvC-ws1rIActxA7bBFZ6yZMZkLfD-a0k_H8EbvoNAieycASC2GUyLv1Zu5za5n-L0fT0yGaPd3cEYOE1396Ffv3cgHOgjaxOwz-JsupYIO3K-Bh2faoy-5OY4vro3Bh90HD0QpeEmhSQAnd-tyNDmYIrRpYUEuRnw-bsWiCN146CZhQBcnoAIyxqPj2CNQnaFtjcH4Qmwilxfug9quewsU7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23016" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23015">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDDutxdQ-JVVXNU0hOnv_cmHgGtioD42nChRCOS3LkMoTiDe0kF_ZaHihT08cO3nvncRWQpx8kFpBUVGT6cGGyDfgxbMX6lhIuznh1rfGFPkAwWp2EDz7TyhR-DLGq8OYkrKMbn3CDq8zqZ_PP6Dfz9HD2r7hkbEPCc2ihW592nLCrnf0qzv4zuDcjxQYet4DyMAyytezFlltqTdXlNbsTCU5MBXSJuiacmZaKpkVCd-qYD-LAbU8qJOuTIUDOHCvkbEPaAHnO7KVd2RkqpJL_iJJJ0g1N7RfVbIf_qDXnItL4vqVAetQymxc5xftoOaZYDEjELxPn6gdnpdVvaV_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23015" target="_blank">📅 20:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23014">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=v3ll2NdiVbaU9Uv7s5i3tVfHA5_prxbT4dAviNV4VPppfi8dPL11KbwZWgi5UC0_RNQyWEEd-0u6fxmtrkrRQw1iq0kEadWFNZOLHQO23_jtWMDnYMcKHV-LwL3gDza57qwZKkEEL-5fvva-FJ0M_f04DQmtjWjaCY59s9ac9kXZejaY-4ns648YCE8nHo3-XZjASyuFgUTaEKdAexa9Um-Dchd4uppj0-Q51kiArjiR2IRpLRxCQY5xqgsv5Rjtbb-T2yOs7I5PBmRiBKSJTzxfZaiREY5ahmZITAnceLwBBNmgf4iYRCucCMiq5UB7gWVH5wIsT4SciNMbsjIqpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60571c2f92.mp4?token=v3ll2NdiVbaU9Uv7s5i3tVfHA5_prxbT4dAviNV4VPppfi8dPL11KbwZWgi5UC0_RNQyWEEd-0u6fxmtrkrRQw1iq0kEadWFNZOLHQO23_jtWMDnYMcKHV-LwL3gDza57qwZKkEEL-5fvva-FJ0M_f04DQmtjWjaCY59s9ac9kXZejaY-4ns648YCE8nHo3-XZjASyuFgUTaEKdAexa9Um-Dchd4uppj0-Q51kiArjiR2IRpLRxCQY5xqgsv5Rjtbb-T2yOs7I5PBmRiBKSJTzxfZaiREY5ahmZITAnceLwBBNmgf4iYRCucCMiq5UB7gWVH5wIsT4SciNMbsjIqpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ما
مردمی بودیم
عاشق فوتبال، تو فوتبال هیچ دستاوردی نداشتیم ولی باز هم عاشقانه دنبال کننده بودیم و دل‌کنده‌نمیشدیم‌حتی وقتی هربار بعد از یک شکست‌جمله‌کلیشه‌ای "این باخت چیزی از ارزش‌های تیم ما کم نکرد" میشینیدیم. بامردم ایران که در جام‌ جهانی 2018 روسیه بابت خراب کردن اون موقع طلایی مقابل پرتغال اشک ریختن چیکار کردین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23014" target="_blank">📅 20:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23013">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgz3LfXjQQ5gk5wtO9mAlymxnuDbit2irk5yRDKTPeA-_rdEP3jLQg0C3_W6us3Mx7bUoMazzdJifmDmCm1A5j10sHL0Ym_0bbiNGLG5zNwv1zjRmlER0TsL9GATTOtWqcJU9uCpVYAq9ENu1hxD3hiZe41uqAjJK_jthosC1meVjZKO264GGU7aILDQsjo3fA5A_kaFB4uUelIS6H0eg9UrqQaQe27aAwtaWhJs9VmQsRW7LZQv1h45gm-gVMHe8x6IceNY7OP97p6jUxLTloSqOtjdONew8nimGvHyjfvPIaNQRyUPDh8VQhRlfEA5e5a8ur7lxgU3vwervktKKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23013" target="_blank">📅 20:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23012">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SS1bQFXy1j6pUoK73HADh8TL56zA4xxz3s_aAK2miJtgrqm769Luu7Rfxwkl8Uzss8RNIt7c9iJ_39xPQSw5uYA2Cof4OST2-hmHN1Fx963aLSscohIAU_drz5i_U2moa3bAaOPFHZU0mUKM-Kyi1OBIxl9PCNPp5Hx55XZAXgorHpZorjyvlHlsOpMd0v0M3JQG94AzSH_iAjwgQXzcjVFCRWk3kDb31tb2llC1aXFtSa1Fk8LymIwth5itdyz__2xJ5ZueWi2PPjysPUTZdnJEMaf9pXAE6BFbxQQKLy-EX6VR7JKTyJOmQJ7ifm6uZufmp5tonExo8jiKGwuGDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23012" target="_blank">📅 20:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23011">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29259cd165.mp4?token=q8t3K5VVYENvXuRjMaJCEMIBBQJyoKpB5lkHZvJoR8VUcqwExnPBhXwLpDF-2b8nBG0iQeqn1DT6KK0KmvEbR4RXj75ZRlI4yzJLZFfgWxfzzQqvict2Hj1ZHX2JpUNnO-vXbg4sChQHkc9P6OqbpbYHEPHOrvApOp7co1SEM5q0qTFqNa_CP3vt3OfiEM29fsNyyEQZWf5I8y0xG97d-t75RJ21LtVnMaJHqB9TlrO-1ZvuddX-vmjQMjSN-q30Z2RFftBEVZfsX-EBX12STVeXUXeu58BXaJLSEOsgh6UUtd0TJGQnntEkI_OP3qmZ2wToECpzNZmG-Doo4IdfsUf3v4zG07E9GPYGzDnPhPyOf4w9276n5NbH3SORb8jbDLa1Tv_fQkl_xjAoR-C1Gub_WscdJMmEKgLzxqfWRh3hYRLQzb9YR8pCVFLpx08hhDgul95-8BUYG8RywrcFUQX9JiPm9Sipjod605zEkHwckUn8ftGj7nwL1zY5WJ7RlD6jt42mefgik4gOjcpAVHMFnfpY-t5qwipG5hxPc8PmY3V_hAfkbevdwi3eeYK1kLcS8xVREHpNP08jrHf5isPvOBhJvAtDLlVg7pDGZiXmY9YX10XjkrYz6Pfx9tjCZDVgrSBiE-PWEjTj5z9lnqz7Fla7Wtu3REfioc2zqhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29259cd165.mp4?token=q8t3K5VVYENvXuRjMaJCEMIBBQJyoKpB5lkHZvJoR8VUcqwExnPBhXwLpDF-2b8nBG0iQeqn1DT6KK0KmvEbR4RXj75ZRlI4yzJLZFfgWxfzzQqvict2Hj1ZHX2JpUNnO-vXbg4sChQHkc9P6OqbpbYHEPHOrvApOp7co1SEM5q0qTFqNa_CP3vt3OfiEM29fsNyyEQZWf5I8y0xG97d-t75RJ21LtVnMaJHqB9TlrO-1ZvuddX-vmjQMjSN-q30Z2RFftBEVZfsX-EBX12STVeXUXeu58BXaJLSEOsgh6UUtd0TJGQnntEkI_OP3qmZ2wToECpzNZmG-Doo4IdfsUf3v4zG07E9GPYGzDnPhPyOf4w9276n5NbH3SORb8jbDLa1Tv_fQkl_xjAoR-C1Gub_WscdJMmEKgLzxqfWRh3hYRLQzb9YR8pCVFLpx08hhDgul95-8BUYG8RywrcFUQX9JiPm9Sipjod605zEkHwckUn8ftGj7nwL1zY5WJ7RlD6jt42mefgik4gOjcpAVHMFnfpY-t5qwipG5hxPc8PmY3V_hAfkbevdwi3eeYK1kLcS8xVREHpNP08jrHf5isPvOBhJvAtDLlVg7pDGZiXmY9YX10XjkrYz6Pfx9tjCZDVgrSBiE-PWEjTj5z9lnqz7Fla7Wtu3REfioc2zqhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
یادی ‌کنیم از مصاحبه تاریخی مورینیو بمناسبت بازگشت دوباره به‌یکی‌از داغ‌ترین نیمکت های جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23011" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23010">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9-0SLyOzRi9zwCdbgbxMwT0o8Avaeq8gwWm5P4IvRJb6-V2_5dyQzT63l2UsBKd6ZlC05z6vCM5UBEE_S7vsFzKxUkMsNK7MgxYyvbr6DXbdN09NkHMTEu-EyiCw1-CZPx2ZUwGswmIXJ3-p-0gZleWLbRSNu5FV-EST2bzfkBqTpnPk0njoHsiBqFlY7yaUOl8p8qMjTX8g0qSGY3pjQFLSTUQIZi9dz0KEggNAF8SfjLvu_4oJCk88QuMwhrP1dU6lWuACsK0m449IR9CvK7dO3iv67MOni3yHyvMSSqgmRWcRHhKKFNZbKqbxMP901R81NLG3N-942EDkbjn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23010" target="_blank">📅 20:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23009">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErXregQudX2ukLUtKAKLviiFqg2RxygMtVeAF514cu9Zh16ZgNzrcAAyhl6c9U_TbhKoExI4mJJ9rsZHgsgnxpnv4h3qD-RZNbrfrI6SXAJRHkRoBDsK3kPCRsFVteuRlB5n_2YPhm4UFTr5bMfFIrySHXORKlj4NET8ZXYqpT_m5i48kYYxBKtD2FyGouaiSc0dqMhtI36erz9AzkKq49ZiakhkoYUi1e7dFBfgpKoGsas5CCa_e5QIGWgnnyc9sxK2pEpUdZ2ET1s7kb49vedBYiscXnIC68OrvhQrO20dYzLnw9u8bjOqIi9x4VqWWz-isMI9RRM-s2Mu00Hk2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیست ورودی و خروجی مدنظر اوسمار ویرا برای فصل اینده رقابت‌ها به دستمون رسیده و بزودی کامل پوشش‌خواهیم‌داد. علت اینکه یه چند روز صبر کردیم این بود که همه دوستان عزیز کانال به اینترنت دسترسی پیداکنند. ویو کانال قبل‌جنگ 65 70 کا بود الان با وجود اینکه نت وصله…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23009" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23008">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=dpRqfgwnj8oBxFNcFqHiQpA2tV4bXjCXoX96V0Tmaz3dgspkA_ksWzpoX4BiYE6xX9nsYqto7y8EoFqMRwgCJ6zPk-iWDG6YgYeByRtQpQAY2ly07MgXT57RZS0HPIFre5GICWnfHcJN_sSFIJjoItbstUNAUNgt1_EWJyBkW7UAjShPm7KyUDZdqyahko11DXMox4zQUlfg8j0IDcOjj-ed3YqgTlucO8RO_D_Nb80EL7rf4nbY2Ho38D4hIc8gHjR0njnZvViYQ7v_JYLQ_lZ9QtR65jqRWm8ERA2E0ijnuYL6J87uFK-VyWWRHzPlaUem9WQd_IhSoqBnjFD63g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc2809ee8.mp4?token=dpRqfgwnj8oBxFNcFqHiQpA2tV4bXjCXoX96V0Tmaz3dgspkA_ksWzpoX4BiYE6xX9nsYqto7y8EoFqMRwgCJ6zPk-iWDG6YgYeByRtQpQAY2ly07MgXT57RZS0HPIFre5GICWnfHcJN_sSFIJjoItbstUNAUNgt1_EWJyBkW7UAjShPm7KyUDZdqyahko11DXMox4zQUlfg8j0IDcOjj-ed3YqgTlucO8RO_D_Nb80EL7rf4nbY2Ho38D4hIc8gHjR0njnZvViYQ7v_JYLQ_lZ9QtR65jqRWm8ERA2E0ijnuYL6J87uFK-VyWWRHzPlaUem9WQd_IhSoqBnjFD63g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23008" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23006">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT8FZvjeoAdXAdo8Gg5__0SJX-k8QK0BY7DBKR_OmYAUxxsr3iltXcdocQt1KndErkx4TeWF9MXWCWyf7DCKUMPgKJi6K1a9Zm7WpEDk-WH0sMDxj6Tr85uigLhY2LxQMmkEeENLN_JuBJbRUU7PCGMP8-pNdhLaX20Ft_5_EyoGg4xMGNnWjoTDgF-p5EhJ_5BtvBw5PBAJwEafY5V-kwKIDlgTg5QGu4-XifQIcbSOQpuaHy70nIytoItDU7KIS75OJa-nNgZdV186bHoAqATm9UB1Xd5pm-nsymNQNxGNVYLt9M4CgsvthQbC644mzYewwQ9HjwUCyMuNIztBRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دبل اولیویه ژیرو ستاره39ساله لیل در بازی شب گذشته این‌تیم‌درلوشامپیونه؛ ژیرو در این دیدار نمره 9.0 دریافت کرد و بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23006" target="_blank">📅 18:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23005">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etHkCbQzxgz6fHs3bfLOvWUx78VYG-39mdDlOTXkYt_bJ_-xxFM5SAObFSadfGR-Vb0koenfkF5O1ePOUhxRERSzhJXEBg2Npx-v4Qesy-UDnHCTJrqqZ4Eh36b7Cyb0gfFKDT5hMchDtAiG7-thB_KxWsz3pzzAYW-DyJeYNeR6Knlu0ZFNOXUyzQNBh4kL_YrJESMTNg6_Nn4SQT-Yf8zt2Ct85c3VUpY9ouHYDoGLaZ8t1LpPKIKWPRJO-83pWXCmiE2hhS2cUFSu_6mLXMP9DWLWSjgEi1a-jR4pWas3rK4dbuemYbn2l31_BTXeHT3UmBFuRoDgYy11oGQVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه رسمی فیفا: دیدار دو تیم ایران
🆚
مصر قطعا دیدارافتخارهمجنسگرایان‌خواهدبود و به هیچ عنوان این رویدادلغونخواهدشد.  دراین دیدار ارزش های همجنسگرایی را به جهان نشان خواهیم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23005" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23004">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=IKXAiLvMHQnsLTscrxOLCbsZsQtPcYepOhjhqcjO8lV-g1H2vb0HfLf2HEoJyOajXwqc7HllaS7bEkgfbus8E-l4u0xUiZ0rlCG8l1BnNpZHBrqeClJ-uETgQ22KwO4uFOtHVAKKZVij-VOnHTn_7WZbbiy1L6cFUhbzpsJJucd8IoQ6VFohoTAuAH1O5YIUFoHJm1eILqiIThcLcwr818ns1v6pqKzceQ6woniS5KHOuEZquTFph8gRXF48MriyWibaLtI5tsInxhChzInf2wCTCLqHsZrgKbDB5igGKcBhLS4VqASUqSqzTlbV-cmgWoEc-6JWQPxgoot5y8qdrTACb9Yc1AHUhcjdz4W4BBybdJY4cAWcD_kJ3hdy4KI137zjF1WVdvZikNvtCPA9NGA1fUQyLknwTPnS81lga44Bn4EeH8kqp0f1C0PcI2M_zGHXERsnJ9fZYUVQoqTZACybmN7xZxYCA-pJR6hHalfrwTmsa72MRyyVABKQzTrwCB3wxwydtnSufG3mX-m3hR1I80KTaCHg9SUnkonHLvQEHunQc4PasZf83043_cMmbf4pWjYKj9E65dUA-Do8bLiNp4oWfkD2KxrFPoeDWwr0MmYnqTqVp5vrenfXXYKNDeaFjl0dVbmDLZYEnIsXpKZ73v38pNXfk1bvtEtanZ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a90d5e78.mp4?token=IKXAiLvMHQnsLTscrxOLCbsZsQtPcYepOhjhqcjO8lV-g1H2vb0HfLf2HEoJyOajXwqc7HllaS7bEkgfbus8E-l4u0xUiZ0rlCG8l1BnNpZHBrqeClJ-uETgQ22KwO4uFOtHVAKKZVij-VOnHTn_7WZbbiy1L6cFUhbzpsJJucd8IoQ6VFohoTAuAH1O5YIUFoHJm1eILqiIThcLcwr818ns1v6pqKzceQ6woniS5KHOuEZquTFph8gRXF48MriyWibaLtI5tsInxhChzInf2wCTCLqHsZrgKbDB5igGKcBhLS4VqASUqSqzTlbV-cmgWoEc-6JWQPxgoot5y8qdrTACb9Yc1AHUhcjdz4W4BBybdJY4cAWcD_kJ3hdy4KI137zjF1WVdvZikNvtCPA9NGA1fUQyLknwTPnS81lga44Bn4EeH8kqp0f1C0PcI2M_zGHXERsnJ9fZYUVQoqTZACybmN7xZxYCA-pJR6hHalfrwTmsa72MRyyVABKQzTrwCB3wxwydtnSufG3mX-m3hR1I80KTaCHg9SUnkonHLvQEHunQc4PasZf83043_cMmbf4pWjYKj9E65dUA-Do8bLiNp4oWfkD2KxrFPoeDWwr0MmYnqTqVp5vrenfXXYKNDeaFjl0dVbmDLZYEnIsXpKZ73v38pNXfk1bvtEtanZ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیووک اوریگی مهاجم31ساله سابق لیورپول ساعتی‌قبل‌خیلی‌زود از دنیای‌فوتبال خداحافظی کرد. اوریگی با اون گل تاریخی‌اش به بارسا راه قهرمانی لیورپولِ مدل یورگن کلوپ در UCL رو هموار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23004" target="_blank">📅 18:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23003">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=Ovy9QJlZHd3UX_QZmgsXiiuvSLFZqW-ZmNTplQlKoZLVTam2Zjp-rSQzzDIA_kaXVkjkq6bbzpR49r_yzsr2Syp4wdRBZBo8Ho1w8KNG1r4HujkHj3UTqSiZXmVGOkOdufRl_KClv56F_LP30HkCHThl1woDLiYnS3fcfsZM-TC__2_uBmoJtlOULpK6GUVwmEDe3wEU4AGxRgeJjvwIrAtr65XIrdUn7tP7pN-3jHi19dEqqhiHM3Gjyp1oYge0hK4T5kM43zOJ4UaO4aoQb6C9tXevAAFivN9nyMRByCHJ4TYO8jk5Mw9lspj1Vpy5BY_O5DsW2L1Sn-jtYuKxeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1416a6883e.mp4?token=Ovy9QJlZHd3UX_QZmgsXiiuvSLFZqW-ZmNTplQlKoZLVTam2Zjp-rSQzzDIA_kaXVkjkq6bbzpR49r_yzsr2Syp4wdRBZBo8Ho1w8KNG1r4HujkHj3UTqSiZXmVGOkOdufRl_KClv56F_LP30HkCHThl1woDLiYnS3fcfsZM-TC__2_uBmoJtlOULpK6GUVwmEDe3wEU4AGxRgeJjvwIrAtr65XIrdUn7tP7pN-3jHi19dEqqhiHM3Gjyp1oYge0hK4T5kM43zOJ4UaO4aoQb6C9tXevAAFivN9nyMRByCHJ4TYO8jk5Mw9lspj1Vpy5BY_O5DsW2L1Sn-jtYuKxeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
رحمان عموزاد شب گذشته در حالی که مسابقه اش‌رو 8 بر 0 از حریف‌بلعارستانی‌خود عقب بود در نهایت با یک کامبک تاریخی 17 بر 10 پیروز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23003" target="_blank">📅 17:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23002">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rw0VHlGEKumpBd71wOkV4eT4g_EozapHGc59vZSxIiJMR1qxny_N0xlVor_7bYljkccUMbKgWoOMHVWvBEquNywomKfsM9i0gi8XvBQ5h3dJCcjZO5nxFDvS511iooKsduPnoTjyKmy6P4cNnWfsFyCdDI_4qB-3PJhkbMoHO8bARnlMjJO4MuWRnQJq94fJ3QQvdd3Yz58zDfYyoyaLa_RbaVWM-whccSP7pBOBMRK7QBcU0c-_BsBH9vBNjtiev2J66e0ZL_wdekLak-PCfEQUSSdTkCU8wl-j1y09EpMjD0Uwxo0zr2MtoIwdkuADwhxNiUWP56rYzvlwgTArgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
پُردرامدترین بازیکنان حاضر در جام جهانی 2026؛
کریس رونالدو با اختلاف در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23002" target="_blank">📅 17:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23001">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq_DlFkJspSC09HhwGHn4anKyyPrDl4I1R7TPHCK95mcb0frvvWPvw01QTfWi7m6qlTHo2jNHEayBue6qSZTnV3ckcJEnlYsmaXKzpYFgXnRZ52W-7O4HTTbM8QUU3Z3XZe0afs7UHPvfQ83iaQcfnmOw6mPSMItaWl3EGemNoLDNztfNMmGmwAg8gbD8K4eEhEkm3w6Bak14OsNm_F_b6JRr6T_sog_1PCpdaLBpm2a4Xd7P9EZAuv-vBTrXFdt4JY__vQc65vK9_-fih5qBtZoh5AIpa06glduisswMgppZ0-FrLmpJ7Q1dYOiEXcIcQGHEF1EfSgucL2DE_l6aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌پرسپولیس‌بزودی‌باانتشار بیانیه‌ای جدایی مجتبی فخریان و یاسین سلمانی رو اعلام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23001" target="_blank">📅 17:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23000">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYSe3W-KTFiFHKOPvISJMmwPxu_AbgzKbEAeiAyXANNGJc4QhNgcEmwhEjSLBKsEy7vuUST0tbv35YV01WeiQdW0YW1rJI0XdYnZ79uIGI4whuKGu9BVOEeB30v_RgTkRui7U83MGYG9SFefrKJivBmL5qLJZrDn_9-wxq02e0c6eHRGqnF2r75uL6EB0g7u3CDFPkGWOO5ubpYu7u-wC_kylqC2q_5yrvksc6SvX6qidiXj6QOeQUPcYrciraglV-i27-fX2rryPZrfOe4j05jixwAt6KCZBLv-OM14uknfuDLkh0jR5SVCkTJpqK6iKCxLPmq3oEuNBL99DwsW6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در این تیم، همیشه جایی برای پیرمردها هست؛
ایران و پاناما پیرترین تیم‌های جام جهانی ۲۰۲۶
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23000" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22999">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Il3pg9cWwsBXZH6m43ldRl0buVveLT7dW4gzm2Q_6fOFSj0FA8wiUYZq1gSQrvU_nJ0U6_HeTZtYFD4jOKOM_p9DOXeqY-fjU645LJ2Em0rl3rnxEZ5I6zzMGZj6c7-c2gZ4Cg9DRYeL0mGZ5wLuX2inIGY3CRELtTEsqH_Ti6Mm3BFwYNTur65Jq234Wmz5uWZqgsdDxSNQsCqQKCHsK5_xF8Xem8JMZ4JFi2VSIEp96jVxJzUPgcNdjPKHyHroXamvH-hVj4ki5WDD9VkWC6FT3-JpuL_Y9enwLn8VGgwqB5JQf6viOAGFSVDPOFgH5UpVV-DaPwS68R3dGaaBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛برخی‌دیگه‌ازشبکه‌‌های‌ماهواره‌‌ای‌که‌بازی های جام جهانی رو به بهترین شکل پوشش میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/22999" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22998">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ff-YjFXcQs_uWCCEHCqHOU8FX3iqhcCxGvavl9olaOtYdltEUcucW7hzpzz2vNuRE9QKrNbdg9MUBD3_8oTQINGRWKw3OEkxrbWUJKLUndqPi4PYk_5OW4K0M6UY9svj45VOW8DU686iajTrCN-klWaju3q29RROujqideFoXn9mKphZLhoqZOw5Y-VdLUoNJZGRE-mkOdkile0ABuZM3J1uYks5bAl08N29gaNhF_J0onL-NRYePl7S8YcNP7vPXTFtYH2tbD2a3An5G8MzOFlCJa5rpjDZ3UzJnyA6yEZr8YwtVG9_zE60nUOBB0GXscKBOn3TCiOY_8LN6W3aqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/22998" target="_blank">📅 15:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22997">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjeUFMLoRbQ0Oh4Yc43tUUVx2L2FWteXWRKPXEiN3eeAej1haC_LK69-CFFzI_FSie9itCPZHsFgRTNsihGDPtwy2zcOEzo4tdhixr9YzEd7x9V3c0rOMwyrrXMayGNoRgVXJeuFye6VU-qJUlmE-p4XQrlZrgeKrmG6GVJcwgnR1NfG_BVUWhBo85i5P33TR7hxeBURqPhsNszCogdFCTuIL59OF0UQFBxQC5CmQn6eJp-S5ZbVD0GG-t1nn2CA7rIzWahHMt4EvvQNBU4DmuVZMhwfRoA7V-kKrKGRtcqP30_iRy1kZhywBnOInkPkDRJIv_tqlljhyKLw_01atw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22997" target="_blank">📅 15:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22996">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=nMVevmDR92nwWOkGeHopO9AGwV9N9CtVUeF5NC-ATWLrOcL7ZQHbhovUfnxi35SLjNKJCBrZ1nh1UVdBSf8wOVn4_Q6Ua9GONhPZY1yuovydpTEibre7Cp_kv72dZdQ0o-arAJ34S9_NpmMtslWGhmOSKi1l4tle1kT9cV8RmdtzJdMiFLwQl6phYrOMEWD-cz6c5O-gLEe-s6q7zAFRn_zSK3bhujzUbmXScXuPbi5mOUVpVUtXFzj2B-2oXFf8Nk1h16YgKcEos3Xb4bkZt7D37KmhQEWE2hScRsfWUkYmSHmcR8zVhD6dP_UByj4nDJdY3JkdtqCxv3ryy5BShQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d3e29ee7.mp4?token=nMVevmDR92nwWOkGeHopO9AGwV9N9CtVUeF5NC-ATWLrOcL7ZQHbhovUfnxi35SLjNKJCBrZ1nh1UVdBSf8wOVn4_Q6Ua9GONhPZY1yuovydpTEibre7Cp_kv72dZdQ0o-arAJ34S9_NpmMtslWGhmOSKi1l4tle1kT9cV8RmdtzJdMiFLwQl6phYrOMEWD-cz6c5O-gLEe-s6q7zAFRn_zSK3bhujzUbmXScXuPbi5mOUVpVUtXFzj2B-2oXFf8Nk1h16YgKcEos3Xb4bkZt7D37KmhQEWE2hScRsfWUkYmSHmcR8zVhD6dP_UByj4nDJdY3JkdtqCxv3ryy5BShQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال ستاره تیم‌ملی اسپانیا و بارسلونا درباره دلیل بستن باند روی دستش در حین بازی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22996" target="_blank">📅 15:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22995">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_mjirqfupKsRUwwxraXK-J2QZajNQ_sTNZVK7ziXcbtx93zvr2aUlx2Ik2nRsCQ1xVux9vI7KELMkPuji_yf6GTk-cpSO--sdGNQ17Nfk_sCWhnQOD7n2zzsxCrAWJ6l7cSs2U1zHWpt24W8wvVgyCnvwtixQ3kGWvqJwKHfezZK-rT-67CS2JRqxasogg-MApacrqZi61bJGrqgbsnsVlvmFUVJk6AbgEYEUGd_3f7f30EV-ao53QuccOmCpIUo30Mlg5KMTSw3F1JwWthLs5Ydwjx5fKMrH00SquH1UtyLCZe5UU7CAGClFvyxGDYLO211HWNF_CPfrYeh-Nkbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نقل و انتقالات تابستانی امسال برخلاف تصورات بخاطر بحران‌ مالی‌ باشگاه‌ها؛ بمب های بسیاری زیادی ترکونده خواهدشد. هم پرسپولیس هم استقلال و هم تراکتور و سپاهان خرید های خفنی خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/22995" target="_blank">📅 14:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22994">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=gXKe9mMFL2oVzC6DHKVmm3tOS_qHIgp8HGtLaDymr8joe22eK3kBkvoFND0GoLXI7qDBeTZcnS0gDjofj99IPtJYfpjkEpBk23nSM5-_Z66_OHJpJVSWKg12PAGyw5giseLyplEfS9RdyoZnJNtVyc8y5TSbmJKC8eN8o4jj8y_wsTTMLFe42uojEaEOxSMeeuFq-9nDJ6MPU8UdlQsi-Gh6BANSQpQDdKVSoCx_AYwQYGQBhz3X41YC8NxNP8HEs2ApQ5e6ZBbvpEEocpqGbjs8S3R6bOi_WN9ZzmbdK6uIDr34VVu3la7UTlE1PtC6SyoLRdoWKWWFf77Dy_jauA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b9e0c4e99.mp4?token=gXKe9mMFL2oVzC6DHKVmm3tOS_qHIgp8HGtLaDymr8joe22eK3kBkvoFND0GoLXI7qDBeTZcnS0gDjofj99IPtJYfpjkEpBk23nSM5-_Z66_OHJpJVSWKg12PAGyw5giseLyplEfS9RdyoZnJNtVyc8y5TSbmJKC8eN8o4jj8y_wsTTMLFe42uojEaEOxSMeeuFq-9nDJ6MPU8UdlQsi-Gh6BANSQpQDdKVSoCx_AYwQYGQBhz3X41YC8NxNP8HEs2ApQ5e6ZBbvpEEocpqGbjs8S3R6bOi_WN9ZzmbdK6uIDr34VVu3la7UTlE1PtC6SyoLRdoWKWWFf77Dy_jauA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بازیکنای تیم ملی فرانسه بعد دیدن اون عکس و ژست سمی رایان چرکی اداشو درمیارن
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/22994" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22993">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8KVctKRW_KbUYDqNPcS06FsM5vBmCuB47u1WuoLD6WiqcN60Sftrru3uTOgLTklNJOUOAvO10H99VO1zh4JCcBOLXJnKD7rqkUka7Pud7if_MBxdwI34PqIFzdolYbW2GDZtxCDsoCl5jfzGC37OyzEnEjLhjxCj4caOq9HRo4acjhyiWeL5GDre07nXESnRZHiVDv45tzdAoZP0wopZ25ASPhJaODakv9KmPxTpnlRpYdqvkbonnhsYQZPWC__lj09otcrsUXvwmrgsYc-dwx5fW_-r_GcZT1LrAKQN09FAcLATfoAFCG4lgdYnz_pf8VmGZOan3YtmTH5bGZ87g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/22993" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22992">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POkOYF3IWF2uc4HKE7saodRuWzht8sK9hhV95YN5WhIoURhCrfBayjcpqpNiQ08wVuu9FtLfZhP61DpG5KwKIqVk-EhwlYce98_nOe1Rf28NjyOCbtkBKYrhR8T-H4hNdzgQxCFrFeMgicyZn643ghboht8skM20wwhVvV7PUVQA42LkvFaLDPKsYkuTT6a9cOscOYhoFnb0rsTOuiNVBn-29HmwhzphI6l_T-QqJyo5NuUvCNTmpamP061qG6ucYTDKC-CoFJ6w4bXTUfTHnNdt3_BB9jP8vo3mNnmdKeeC_3BbocK2slUlg_cyulIiNuxsiYUUpwpw8NGEMLecgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/22992" target="_blank">📅 13:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22991">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=vxlIbeq5ih9jrUyc9B0GEcC2aNEoZ94bT0jp-_uOE0ZGPCq2nn2YneTaTv4dMYN1SZUCrH0YmY_FdhSuLcPB_JnAIezzrRNatXd-rx8WG1yDPA_H9Kh1CQ4zoOsdlnHpUjsgck5AGMb5jqJGTcVpIG2sDzaLsASWs-yVaOJyE8CQjItmXcv9H3Xv0PDpq7_cS4EscVF0kFktvN8E0i9F7xFke2EJkV0QNtW6IEyCjYigIsLzhh7kdTyYE-FjoonfNBh_xzKRjz_QKJAE27Fn4fy4srFspIie86gwI0cT2y3obqkoPH1L4W-t6rmQ0hfun-3QfQh2DtWprt7EtoIPcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2579758a5.mp4?token=vxlIbeq5ih9jrUyc9B0GEcC2aNEoZ94bT0jp-_uOE0ZGPCq2nn2YneTaTv4dMYN1SZUCrH0YmY_FdhSuLcPB_JnAIezzrRNatXd-rx8WG1yDPA_H9Kh1CQ4zoOsdlnHpUjsgck5AGMb5jqJGTcVpIG2sDzaLsASWs-yVaOJyE8CQjItmXcv9H3Xv0PDpq7_cS4EscVF0kFktvN8E0i9F7xFke2EJkV0QNtW6IEyCjYigIsLzhh7kdTyYE-FjoonfNBh_xzKRjz_QKJAE27Fn4fy4srFspIie86gwI0cT2y3obqkoPH1L4W-t6rmQ0hfun-3QfQh2DtWprt7EtoIPcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرد البرز که بهترین خط دفاعی لیگ یک را دارد و هیچوقت دریک دیدار ۲ گل دریافت نکرده بود. اما فرزاد حسین خانی با چای نبات و شاگردانش در مس کرمان موفق شد در ورزشگاه خانگی فرد البرز به این تیم ۲ گل بزند و ۳ یا ۴ گل هم ۱۰۰ درصدی هم نزدند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/22991" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22989">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQgR2U1oBBsdT-tpNI2u5p8tnIM7wvzSbjXvfgWlxxKT8KQxlQJvKrxtdwbjpu1T2MfHfG-JoY364-Yqv6ZsZu62B8c5W002YsTsFKvSNNmGdPE15VZ-YkrFTp2pSw9hvMTa4xxAyHdEqICcUZzy4JMsNSiWXTcWaQhcVR2Eep3qFFGzIO_EknXepRVd-w10NwFa_aEYPr9UClhN6wJvyeAU08jo3k8-O3in6EiY89Ui-l8oYee9EpaU9U58DLWuk3SjR9poqc11vKGgFv43BDeIIkB8C7BrM9X3SZTv5PgdaQBntX2pjipS70mRtVmejG_ZuMgUTru3xm8qAe2oDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه‌اتفاق‌خاصی‌رخ‌ندهد؛ اوسمار ویرا برزیلی چهارشنبه یااواخر همین‌هفته‌وارد تهران خواهد شد تا برنامه‌های‌آماده‌سازی‌پرسپولیس‌را از نزدیک دنبال‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/22989" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22988">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2KbHJr8B2j10V-YYYfqlksk5hhyVZMH3bOwgR6pBWaEkiJMtcgVSxPQJ_4OcYoM0bzmSmme4m0BnwWAzPJsUovL_lfkjm1qb5MMzzBl2Gok4C2qx5VGsAKZNOeEmmh7Gq-3ASPX3xIvnM8RU5wCFVtK3WzWk4AKsnsSDC9fXYCabBIjyC53DTbh4wVp78JdGArQBQnY-B3dGlT2OKyCXPuYoY-SLT-ujXCE9PK_sqotJOZV7J_kCx5iyLAUEX1iyNNcp592js9WoBSrXi9B5aN1OP49TIuoGfO_WpkMr3AAD-Y2RuwCaL3ISnXT-O0kpKdmSjfuanFlby3zrDQjRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/22988" target="_blank">📅 11:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22987">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=eXp7Qe57ZgN-rKcB5AK4EMit-esEZTaIVYFuMEenDl0TXpZfcmldIt4t90ndTs4aE_DSfwTiOQU1Jnod1XkvCds9hgQkE5nMh5ermGaaqZbPyX_m98pPC7pOYfE6Ra1O-5fey3rj7JwhFEaqJniDVuZhS-lZV-vNNNsz_N16Tm4uTQyBxcglUL0XgIFCHAaoJrB1pq-rbwfqYO8jGAJyJ3zZctnlrwT0T1-tPwRzOAt9GXHCh0ZpVNDkQRw7hfTh2QJMipv626G-4pipF58ahDjF7gFOOi-fIxsY08o7ANNFYzCL6VUHHcjdp4Pzs4EhdQ7KMzYvcwyEmsUI4CTdvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c19cf6b3c.mp4?token=eXp7Qe57ZgN-rKcB5AK4EMit-esEZTaIVYFuMEenDl0TXpZfcmldIt4t90ndTs4aE_DSfwTiOQU1Jnod1XkvCds9hgQkE5nMh5ermGaaqZbPyX_m98pPC7pOYfE6Ra1O-5fey3rj7JwhFEaqJniDVuZhS-lZV-vNNNsz_N16Tm4uTQyBxcglUL0XgIFCHAaoJrB1pq-rbwfqYO8jGAJyJ3zZctnlrwT0T1-tPwRzOAt9GXHCh0ZpVNDkQRw7hfTh2QJMipv626G-4pipF58ahDjF7gFOOi-fIxsY08o7ANNFYzCL6VUHHcjdp4Pzs4EhdQ7KMzYvcwyEmsUI4CTdvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نه‌داداش جبر جغرافیایی توی پیشرفت آدما اصلا تاثیر نداره؛ محمدصلاح اگه تو مازندران بدنیا میومد:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/22987" target="_blank">📅 10:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22986">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=P3i-oR93tELdb0-yhzfWYzQKBxmVKThGAT7-0QHZcXRyRVEamOV0YOmKwh7YQMIIJogOZVlaxf_Mqm4xGrc_sFgxLixEo_5hDly9O_Kd8oSEFyrYuxUacpCnLNgSlt0t0Fn-HvbinLXTFqA6tqiNNfLM9vdd4CRhwxNiWGtam2rqqOgfERn3CzOO1qWaWSL-otevYMY6938uucUSYRGqz2l1CXm5CyL0ZgbrrPdbzP7YYiIZeFKzZwoXWNev7CVXkY_qUkWKZtjm6HQZ3rsxE8CbjKpm77tbSlhTkyMAQrFoCTN_KhWa-QQUXVReoA4mLJ7vtbs9FY84io_KmnXRTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d73e5ee7c.mp4?token=P3i-oR93tELdb0-yhzfWYzQKBxmVKThGAT7-0QHZcXRyRVEamOV0YOmKwh7YQMIIJogOZVlaxf_Mqm4xGrc_sFgxLixEo_5hDly9O_Kd8oSEFyrYuxUacpCnLNgSlt0t0Fn-HvbinLXTFqA6tqiNNfLM9vdd4CRhwxNiWGtam2rqqOgfERn3CzOO1qWaWSL-otevYMY6938uucUSYRGqz2l1CXm5CyL0ZgbrrPdbzP7YYiIZeFKzZwoXWNev7CVXkY_qUkWKZtjm6HQZ3rsxE8CbjKpm77tbSlhTkyMAQrFoCTN_KhWa-QQUXVReoA4mLJ7vtbs9FY84io_KmnXRTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ
؛
مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/22986" target="_blank">📅 10:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22984">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dsNR0uKQUEmDDYLP9wcG8lEDVc05lNt2Sit6cHDPTWUpQx1FNiV_R8VJyug1XEsogyyzjwQmUMu1dbWHvYXMtkPr6szF-uwLAOkhCNZPEMT43l5xGNTaOLgjBM48oWCJJFPwJ7Mdc6_IQMzvVvX9Ovp46K6yBsF9NHWgRJIUYE-2pqydVZ-zrA9XOXcxzUEt6XjECmDj7tYKc86zxvzfYsmUCtU4EjzgZ6trfDPSqtCoN6lb-35gd0la4_NtHcgBDsj2Q92y47njbrFzRN9nMB8uMa9vH5VcKgxSiL2KALgqR5M1uW3ft-19qt2Ga7Uuvab08waZKmkqpeS7GrTVcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nC1lkNKmHRHoZKyg4TWohjZ_belOaqWOnQd4QoraIeG-Bj3drgPYGI7S6XC5EdNNqO-TKVkQYtyAs3aFtTtiHrPtxCW8Xcth8W_M7onMQ4a3K0Iv4pXKiFR6C9tvMtS01WfHts1LbExnlOSccRae3lhXJqwUlhMucSaXWkCSE76kF03vxCM4yz_Q4ddRgwNS0M4joeLEDAalOWu71YAo58K1pvEYLLg4qngfm0YmVEDhslDS_rM1onuO8ZyBpvi7cdvOOHwpe2yidXv8fFTLd9SGg0imlOHeWUqB2ZYLxlhJbS1gk-K7gacRVutNyBWEHwTdaSbOwFJV3PcwI_hnoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.  مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22984" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22983">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=n0gVV1gJik8urr_S965ONIPX9Kt9GW3sib6eyl_y05ULaBLKxGxu9a8eYb2aMfIppjNvs5jZbNQZmFqCkgR3ofR9ODz2Sw5I0KXcRhEveL5C_lGdI8opmy7i6LoMD9soqvimWrY6_Gl3Vofru_28pfeZhTAxbnGEEZPRLnLHsDNznR5V7QQX4_uMO3_MdHSnAe2wlRgzm-OoFf8e0EaXrAAXLxSP3sV4cxS9gWBE-S-rHh9QUb4hBTCS1T_Oqv1KQC80ME-vqXSaGHUqx9RwxYxqtW5TI8IA4k5-Fbqr4WosynypoXsA1nKrquZCFF6rmdiNb5wS7lUxUZOWZDkVoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa0118288.mp4?token=n0gVV1gJik8urr_S965ONIPX9Kt9GW3sib6eyl_y05ULaBLKxGxu9a8eYb2aMfIppjNvs5jZbNQZmFqCkgR3ofR9ODz2Sw5I0KXcRhEveL5C_lGdI8opmy7i6LoMD9soqvimWrY6_Gl3Vofru_28pfeZhTAxbnGEEZPRLnLHsDNznR5V7QQX4_uMO3_MdHSnAe2wlRgzm-OoFf8e0EaXrAAXLxSP3sV4cxS9gWBE-S-rHh9QUb4hBTCS1T_Oqv1KQC80ME-vqXSaGHUqx9RwxYxqtW5TI8IA4k5-Fbqr4WosynypoXsA1nKrquZCFF6rmdiNb5wS7lUxUZOWZDkVoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نشریه ESPN: بازی دوتیم ایران - مصر در جام جهانی به احتمال فراوان بازی حمایت از همجنسگرا ها خواهد بود و فیفا نظرش رو تغییر نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22983" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22981">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgcAkR1RJStpAO9I1aNAHFPnC7jokLnWzTh_cz065kvwLJXUrR1PVLPsTUzXiZkVgulTGBquZHMRDNDHwyIlND2_5r7fwrgAKk9wMHSSd1e0aieV1IGivcN2P565o5gz-VNmB88z1f0LTYrpTBh9dNPFMshF-IqyvaXKGTBHPrWu1sq5Gb1UFiOPN1G0sXYaM8_av0TWYM4t5p57OR_St529LyLhsDXNSTeAWZQ5KriACGKYXAJDkvf4aZ7aCHN1hpzvsrjq6n1Uw2mmi-IfN0j9nWxMZ111JmmNCrLRTi60vqE86VqXkwM-qMlig19K9tmSQogEVlpLwYZP6ISXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22981" target="_blank">📅 10:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22980">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqImFUHIBxWZCWdTsS_8-_oaTBvCIHr97GbmtvDpcMAv8TwkxqRfrIWleszKpvJCXs3K-3-rSk8EVNwUC5SUsQRvFVTwM7dj_wEvTAT6qKpPCT9F_esRO03cRcfcNDjEtzVWUrO8bW3dR7mJoQu-GXwUYbyRu5VNPxaVH406hMakXn00Gvk6WGesD08AY8YHFCvRawBeLBorgtL9ZBTyCAtkjqif9Is2cqYa1EIQoQGML6qqg4tbPsAMfSWj7giYOfU297tgJUkRPvgi4m5QCxhNHQXNLwvJLhXn9dQXtSzIulLZ4iPfyNsK3A5IQH-bRArquVd-7DDa75g9Vrs03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات
|موندو:
مارک‌کوکوریا به سران چلسی گفته که دراین‌تابستون‌میخواد از این تیم جدا شه. اولویت‌او بازگشت به بارساست. چلسی برای این انتقال حدود 50 میلیون یورو از بارسا میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/22980" target="_blank">📅 09:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22979">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_sODGM4HEajXcRIGzpd4nboZp6aqy9z6lb7uw9uxIeYI_kKY-_YecaMBU_3mbWU1TduqP-F4V9DNemIIgU5Jqn_iBJ3_CcUdcGBin-tecRsGEYMQl7IjKO-V1Oxft9Stw1-SoJpN98IV9cdVPpM2d1vxsEUK9TwMxj01SjPbs9MeFu3MSLw8-X430HpgYuPER4o-a1UBoQ2n7VgZAPy7F4ed9gB5zLjNwePbuEBYCFFtgpAI5kUt5cuv-yLf3P9wXu-fLFZLcoFXolNHb4XK6GGZxnSrZoYfLKhrxpVET_n5k291RU2ajvaz0E08_i6j86JvShK5i7r6wiNKD9WdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تموم شبکه‌ های ماهواره ای مختلف که قراره رقابت‌های جام جهانی رو با کیفیت پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/22979" target="_blank">📅 09:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22978">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/li8YZdzhnD1NStmZiI2eeKY003yMoHXbRbrZ70R53e9nH0ToCa_71TBVUVYkE1cv7nn2-hOVkCeXc7LdgNO8T6ExglgJ9O6_VCK3vpR8qe7J804h30FSek8pG0JI4a_7nb3Faje9DBpBghlGffbScQwHAprRFWWhBFGlg4lF9nd_PSmpeFtrqzbcnlrmG1IBZwPRhDWvRMFdeXuNER0CuEV4gp_hfAcn8-rY4sbIkLjw0GHu_lA8cl6GmCBr7ERzSNITILOl_7toPQLOPDB1GV_7Rq32RD25ATyonCZ67QQ-5DidZ5_k2IJNxRWxVCOYHRrTeOqBU0XTcTs4EjOPPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/22978" target="_blank">📅 02:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22977">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJtlprVH0N1kwFt5qHi7u2stSQUefFSPKH7dRZ-oCO4oRPuaOe3KU7V5ucvqAocYRZjU_hqT9YAGfZR8kpU0YYNW6Trr7BBumfP3ZNh1NL7pjWdPyNWuLJPkABKtdDLMJg9HsEAy5ilAdsQHbF_pSOJuqkmHGBn_CYLu0YwEDz21-OSKwVukcvxDf_MBBp4PkY1VJpGjFcNTGpmmsakjjaqmdthE-kmoXzgblAr9T473TeDdVrsg-u0jFmEY8sc4lPUBhTuk4_BvEig2GbheXpRkWEy5ihO1yJSSFK6Yqrx97BaNdS1Y7zpDRbyK8HkTZPzPVUpTETD4ITaDCb9Gog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/22977" target="_blank">📅 01:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22976">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGC4DKClK-ik6c2Rmeeivx95NmCycowDMqNegDWOUwKYty4Nm6FGlecGp_R60uWHJyx2V4-vSGjUocQEPTWtd1-keZdQ5f5h12icwGZOOkUDeShFB481tiEjiIU7IRHItqemer6j0AplhvP33v8bsWYHLkN7Jzk6YpYTlsiUlKl6JnJ6QcHrlavHalgGi5yEWkN64dv5gvoeUgncd7EIRCW-85Z6gT_wxhvPfwQ2WoMQHHz0DKGQwgvAUuaxT6sBHaLhtJpHHxl7QQGkXWFmBCt9so-ZgJVIHMR3E6fhMv4Oo0Mx4Go2_7DXVX2gwac0c8XKDxUv72IaZ_TT6pfQGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛پرسپولیسی‌های‌حاضر دراردوی تیم ملی از آریا یوسفی مدافع‌راست سپاهان خواسته‌ اند که برای فصل بعد راهی این تیم شود. یوسفی از پرسپولیس آفر قابل توجهی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/22976" target="_blank">📅 01:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22974">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pb0PP6bpebcmKpyD6qNvmP0ywpGno_UH1Ms0NKbfRPftyaikKSbMKi1pRgXgo22zvHcZWk6ynWiqL0GNyS0WclIG2wJnogcpGVuqeYSJEF6RKvkf0AHMWf8m3GRQAu6TEJh0eyhmT0WE0TA7aaE7Bikw21ldkRcwuwaQUCHemVyeDlTxS-5ZNO0pCHKiwXeWPsiDDZ5aAKUVha1nc6aBxS5ytqfjtMzt-p1fNZ_OaoxSqtIbfRWFQ13kSBmZax7kdQorFG7vT3a8ACD4oCllT9j9FO_u0GCdfBZicO8zvCiwUBaEeUdH0nqtwCjNZEVOLmimEy4prl59iwfYawMIkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
از دوئل تدارکاتی شاگردان کومان و کاناوارو تا آخرین بازی فرانسوی‌ها پیش‌ از سفر به کشور آمریکا و جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22974" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22973">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krfmETgblP5HK6SYfmIucqEUJroccseSNTjOL0v2hPSIJa1OLJOW5UtgsaiaS33CkENwcMuvCu1wpjFp3jIjTqniygjQBll-9janNzZPPb9OM9BveuspurriD-LncjzhdH8TODo_EBAs3GSn5nFSB3MkO4DWcHbXMnFUjFZdbjpQKjlvx1VD67-QB5u90_vAkrFwZd1VnKrbZFCHmmZ7ghoRHROS-NW04nCXmbn7pAj7gBypXR3xXa_m9pFovkycwNlJdPUw-xD_205Q1qU4lSEciyctoSj5yu4U_i5j-Z5Wwv6_Zh2OqV6yvzi4loI2tDRAg5VnOgGmtaoZGOjyrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از برد آرژانتینی‌ها در شب‌‌استراحت‌مسی‌تاتساوی درجدال نروژ و مراکش
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22973" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22972">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jO3Sz_8mOTDJdve6axc6ie3VEyfbauB3xkco4GQhX-OnRThmcGjQ-WLhLV8bToFJ1Eqb-OpQ07HpQ0KDvqYXXskaEk1YWCvOX2M3KRL2ouK6XrVm_4cE-Qivi2hNqA3zLWll2JJWo59Cvf4x6uxWrQO8ViXziU2yMTIvOv6efQ2w_ezTEGmjyT2Fqs-ll6Ug9vUVdZKGo-vroNwjBy_X_zEZhLfORr-vqyw3F8JLcEc52xJYPO3Neqv9Myjpor3XOkoEH2WfKTnOHbjWLyoOA1sFYi4GPQ5cOOJiI1pf1YIwvMPOpYbyiuXsVd5e96hsVW0vhQYpFt7h3DwDuz0cxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22972" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22971">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=plfq_L7eXH7TZEgc7wbeVWuTYTRv8Ew20ZPT4lg4iiiejAWrbkH3MDIRGOxOlDcnS5ee5wOgUCRd9q0ztc9fvWmJvQouFW7Y5UN_yOwnkykBpzFJgUt1_I_sov_0M4L0M3zCM946Po7UsELWQcfVxOHu11PEyFkVT0dX4qwJeA4ej9MPAVnu_pf7wKO1yW9uD3HF_MsJv9c83anarG_Cpr9DPeT_CS2K74YLtcYctZpSFzX58JEq9uIg1JYANp49wNz2Ebf3mbNCGUEjc-cWPuSb5wC71ceqWy5uNOl-sRRyUvHEdulXMWupO0qa93UcwjezhLKM0DHajYpD-TZ_E5U7opAGGfknNpLvZ05fFlKDaxxzhVWcY6cVQvaBo8s4Cbrzc6X8txWG6UUjq7vUQQDV7TDZ6ScqVB3cmgAmb4TVyiVmvAXkU5xMQJ1UUUqF5Psa-DBpcudeLF-MYD7kGPZKgCdADVOOK28lZrI8P1Re2_jfBzIXDCd-S-KjRjXCcclKP1W7lGTZEC6d38ihTM18YYlncXj0nPE3y7iPOtXocVisVnfDoijjUOKPqcbAlzwaiSiB1pCw_RTDHZFgnfIMktNSiZXLHt46diJRLKm2-xfTKU3oOawh7bFbyfpz0V8nmNCPiCBCha-N9_CSFSe9r0xX_dPR2Yf1jktPN-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=plfq_L7eXH7TZEgc7wbeVWuTYTRv8Ew20ZPT4lg4iiiejAWrbkH3MDIRGOxOlDcnS5ee5wOgUCRd9q0ztc9fvWmJvQouFW7Y5UN_yOwnkykBpzFJgUt1_I_sov_0M4L0M3zCM946Po7UsELWQcfVxOHu11PEyFkVT0dX4qwJeA4ej9MPAVnu_pf7wKO1yW9uD3HF_MsJv9c83anarG_Cpr9DPeT_CS2K74YLtcYctZpSFzX58JEq9uIg1JYANp49wNz2Ebf3mbNCGUEjc-cWPuSb5wC71ceqWy5uNOl-sRRyUvHEdulXMWupO0qa93UcwjezhLKM0DHajYpD-TZ_E5U7opAGGfknNpLvZ05fFlKDaxxzhVWcY6cVQvaBo8s4Cbrzc6X8txWG6UUjq7vUQQDV7TDZ6ScqVB3cmgAmb4TVyiVmvAXkU5xMQJ1UUUqF5Psa-DBpcudeLF-MYD7kGPZKgCdADVOOK28lZrI8P1Re2_jfBzIXDCd-S-KjRjXCcclKP1W7lGTZEC6d38ihTM18YYlncXj0nPE3y7iPOtXocVisVnfDoijjUOKPqcbAlzwaiSiB1pCw_RTDHZFgnfIMktNSiZXLHt46diJRLKm2-xfTKU3oOawh7bFbyfpz0V8nmNCPiCBCha-N9_CSFSe9r0xX_dPR2Yf1jktPN-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22971" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22970">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=lA6v4bON1Ts6jK5FG11v_Up0l9YsjOIzM3aO8kPW6xIHIzWSjXBJJwKfyE8RCY7xlf8Pl9QmBQLO9sjeN-L99gPI-PTYAPs9jvKlX0jexnE8MQtYiiWJGlmSTYbuvbUkvOOtbavgwJfvWkfbfKmrFLfSR8Bd2ZfJEHozxBlbyShKzFjS7lrp0Y-NkiqP8ZKYrwk7im0hy7KGJxkk4zKeNjz7qJlbVJrUk0pX1SK3s52qTX1x61Xs1R3z1Qsn-GsF_LbNdQMgz-YQokAHOfX39oEDtIJ9M8zxgySBT-uhXxnbm3zNbgjZGvjkUMBCesiwPPQTEGWY-j63uWEJoR3ktQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=lA6v4bON1Ts6jK5FG11v_Up0l9YsjOIzM3aO8kPW6xIHIzWSjXBJJwKfyE8RCY7xlf8Pl9QmBQLO9sjeN-L99gPI-PTYAPs9jvKlX0jexnE8MQtYiiWJGlmSTYbuvbUkvOOtbavgwJfvWkfbfKmrFLfSR8Bd2ZfJEHozxBlbyShKzFjS7lrp0Y-NkiqP8ZKYrwk7im0hy7KGJxkk4zKeNjz7qJlbVJrUk0pX1SK3s52qTX1x61Xs1R3z1Qsn-GsF_LbNdQMgz-YQokAHOfX39oEDtIJ9M8zxgySBT-uhXxnbm3zNbgjZGvjkUMBCesiwPPQTEGWY-j63uWEJoR3ktQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ایکرکاسیاس گلراسبق رئال‌مادرید در مصاحبه با روماریو: «مسی خواب‌وخوراک‌رو ازم گرفته بود.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22970" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22968">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUo1Aw2evzELZpb6yQPNkHO9acHaoDE1ROpPdGA0IkbaZ6KwXzTwtvT3X67wmnvYUfcQQZ12k9BaTvFHumSFQcc2lWdWOwdzGRxCQMcRJS1dlqODswfzkcB2voqdnRK245RKynhMkf5nzt1OUTOuGog6jX0jCNpAoYNNnKCJcDlqKmqlfbzH5ESHWXCRDWFrXZzc-BgAv0z-axwYAX7ZufHJeCnoboh_35BuhjsU59dL94JZldBsF6ijGsOIkhsbhyf6K87JrarIEglwvTHt5vMbw4vhGu8CiiN6lcwP8UAQfq2naqwN444pM9zXUSL9uFfCLRTH7b-cSsevbSAPag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای رسانه‌های روسیه‌ای: دو باشگاه ایرانی خواستار برای جذب کسری طاهری ستاره 20 ساله روبین کازان روسیه به این باشگاه نامه زده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22968" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22967">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=PSssl-JcU6woLSzp-u_flB4dBer-w4KhNw85-PuJSwdAKbCiFz51Gh6kgjDWLKYMYjqhfgDPcJymnJFwr82JnlZwtLFg-8olzND_GsfQQFdcgai79CPrr0iTFU2amoGoXw0rBlmZtRspc3KrCT4xkszNF6kZ11jRNwK0v3R0H6E2P78YWY2Mcmp7rRGLpKPQyTgm_QnzZQBVyvNPa8madoasl_mouSXKVHU3cPbaH0IiqZxan4aCo37WRpz8j8kcbwfa7DXxyiKlcQBVV6aJpCp1mabyiD_pWyQtzM0CAmRuShNEAOscpQ3qm-XCKQKhq2LSfaRI_DqvLvEXOyqvrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=PSssl-JcU6woLSzp-u_flB4dBer-w4KhNw85-PuJSwdAKbCiFz51Gh6kgjDWLKYMYjqhfgDPcJymnJFwr82JnlZwtLFg-8olzND_GsfQQFdcgai79CPrr0iTFU2amoGoXw0rBlmZtRspc3KrCT4xkszNF6kZ11jRNwK0v3R0H6E2P78YWY2Mcmp7rRGLpKPQyTgm_QnzZQBVyvNPa8madoasl_mouSXKVHU3cPbaH0IiqZxan4aCo37WRpz8j8kcbwfa7DXxyiKlcQBVV6aJpCp1mabyiD_pWyQtzM0CAmRuShNEAOscpQ3qm-XCKQKhq2LSfaRI_DqvLvEXOyqvrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🇵🇹
امسال مدعی ترین پرتغال رو پس از سال‌ ها در جام جهانی داریم اما جای یه نفر خیلی خالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/22967" target="_blank">📅 00:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22966">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szO3Gv7TfsFLwBL6YHyeffpefZIfczqnOj-40vP9CtXtePDWraiCHojScYhxtkduLpdZ4F4VIdjyUXhHsPpIF8izKy7Gs1fzqFa2LkOrCRfOlx7NS4hV2Ecd8keW0WHUyMeyKfWSvFtPBOkH34VsqhgPw_97bVfbY224GcqxaQ6EF0M_RMqWfSOKzkfFf4Pjp38NMA_gvBHm3G6AxuUT_Q66vKgEzVgAPk-873VdUuWeMDHAQGa_FCgkpVF1Gp6sLOKxZ0O-b4HA_T69Ia4Q2ax-NLnVis4xlAQyLShd9zVfvMmzeH8zy6M-xiLJdwxY5l8E8rOj-MumSziXuAM0aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/22966" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22965">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OT8Jm4VcvMrpkqfGD9eC4yFRqnKL8l9NLyFZqVXnbjgaDasbRtCvREagid-2J910XR9rueYi-_6jWC5kBu1c3mRdUyjJEkKCDUGlgiCpVr8x_kdyFwgSzNoo89JLNzQcEo8saisvxI2u9LGdlk_toPWaEl6hRaIndkipgShljvjVWEvvg3hMkP8j-EYME5J8XcSDAMNA3md5-BLZcaMQG9nt2HINvUEzFMUOhq52_cbPNiXAivSLgeQPI0elZUiQ61kpR9MTKxhcvwLnMZSkndknFCx440MFA3FKvyJhdkiediYydvRCQbX-v5vXjFxJQ9Klkajpy4ZwSvxT1tvG3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/22965" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22964">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=HbBEtvKgMtNhZho65iwamVdHzdjA8Y5xq_GV_MU66TouBw7Ph-oQWXLLCAAPCbX69c158pgWmgqMNXIG5o9G2gC3bhctlsfeZ5TT-hl1-xe2J4gh_JT2XQaHiuTQM4nnnWCrCrbtk_ekHRIHSvs7drLJPRr1m7WO_b7lrsx59iCZJ5rENztFRDydVEO37MtHCGE_MvZM80vHMkZcJ_nzgsEsh9ojmXlh4KnmvLftnLSn56tMpDvONKuMQgNHPUGjYq2CWZO4GzYzbItmN9GF10X0DNHMKs7Gfm2pNVEOuJUEKSFFTIaWjaR1Grj4qa5Cr4z03asg8HuKUF2K41US7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=HbBEtvKgMtNhZho65iwamVdHzdjA8Y5xq_GV_MU66TouBw7Ph-oQWXLLCAAPCbX69c158pgWmgqMNXIG5o9G2gC3bhctlsfeZ5TT-hl1-xe2J4gh_JT2XQaHiuTQM4nnnWCrCrbtk_ekHRIHSvs7drLJPRr1m7WO_b7lrsx59iCZJ5rENztFRDydVEO37MtHCGE_MvZM80vHMkZcJ_nzgsEsh9ojmXlh4KnmvLftnLSn56tMpDvONKuMQgNHPUGjYq2CWZO4GzYzbItmN9GF10X0DNHMKs7Gfm2pNVEOuJUEKSFFTIaWjaR1Grj4qa5Cr4z03asg8HuKUF2K41US7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/22964" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22963">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇱
🚨
شمال اسرائیل آژیر ها روشن شد دوباره  موشک ها از تبریز و کرمانشاه ارسال شد</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22963" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22962">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtCllEdqtSto-D3DTir1j95hHyjsl5qvOHG9s0fzEA_-xnoyXLVkadlgZBIQLSM_IqKo3sn3XywtsGKFs3AukafKkdUWHZKSXDxlDB9P_wr8GlrfVzbTQetWv1BVjDrvdTXkCjq6CIhm4AlLqOgVCESBWhZiRZ48Xg4kWuWrT-RmJMPMSaDOLC70UOyqU1PvqU7eZ_NlkK9BgNtnnAS_PHuTO0lmBtu_Zw9HCYzjgaxXXRsX6FCsCH6G9n5kPFEh0ih6lu80W1yg7BsnGOvIZ6hxbr9KPZ-vT8IphElOxpS_JApmgCEklKYqTEHTtVe0wnvOwyWVaYMg3GslTwC-Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اتحادیه‌فوتبال دانمارک رسما اعلام کرد کریستین اریکسن هوشیاره و تحت شرایط خوبی قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/22962" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22961">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLOxrXfFM47ch_Ik-x5i72yp-HfZK7DJkNMTnMavKg-RC0M1Axv0UQd0IbZvBIRI1dGx5LonxCel47BcllXOyEeIr0Q9PRpNJjYoF5dZMmJyfvp_uLyJce02IiPnhZQZUHhwzlf3J36pie08bNAdhZLVTkHfNekRKocrj0jcNm_3GUZF4LyeHpu2YP4Ku7id6nk5CfXFPUtKndLRDwDRSUIa-aMVbXJ9Zh3CRygc0aDLYK6PcZUpq9uGXJ4oZd-M5uvdvqPDgjAZCmmJBNcF0IVHxBOxYyfOc9K3rmdWsPpGA0SIrNooD4KhWKHUPMNwoi3JjoyD3EQC3LfzgeU12Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/22961" target="_blank">📅 22:28 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
