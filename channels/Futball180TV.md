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
<img src="https://cdn5.telesco.pe/file/tS9HPWfA7Ikzxf5PPvdCp6RYUyh-gAGuq4iTc_HDSOV-avpnosRA_giQAEOYq-be6o-S8oSfEz2-AnAk8cMIDWP0Y1CvqmHm0ogUDBCWdGpHIuTY-241vwuJSu_EREUL_7PIobSvLgj0ECr0ZrKkbnNGx8T2ofthoZAOl8NzxIqvZNQVh6_aWjbo8pwRVVYgSkTnU-ZiOwilyyzkB84YskQKVzaRTULg9qzN9X8wvNOxqPGuKKgqz-Jcso5CLFaer5xaij9GBKTOR039lJfOwYZEggPYkN9QuJWIK_fkleogQ3ICjLkrdT0EBHrJPZhS94OntIRiAjqS0J7TYe2BzQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 435K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 00:47:45</div>
<hr>

<div class="tg-post" id="msg-105134">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DAVU3y8EQCGTjsMRCRmQO6zeKPXTh89IbbXbus12xpTgCBvQ8JcI6q4gnKhrycL3SA-Clvt7Uar93AK0m0HUjJdDSecEzDEh8jbytf10bEGeOYTXk-OT9i2qI7TzAuwPDyw087dxYOFZPuLnl-MzUN5hgUiN6j8DAlzjz_EyTP2L8GtQF6dRqcT4_f28HxKrszSx4uoEkeJ34hk0-8xik2rVlzZHyYEqv-vLb3k7SrUlrQkqwwsHN-CrXZwdETUKbzjJlkORHGIUOi99LEZ04Rz7296AdMjzGKvW0BMOBQVezhostQ6Le5UWDetyMShRNekDioS4NT58Ovf0BaSXfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇫🇷
جدول لوشامپیونه تا پایان هفته‌دوم مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/105134" target="_blank">📅 00:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105133">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370a134319.mp4?token=hpmmTaZiN_JcMfEd31uUyjCu6A_BqJ-7lWpobMsV8IX3Jh4vMEZYxb7r6ZzAF2-fW8WK3M-0O9pJT1qFKUa3fHV8ma7MBFMCuE-VhpMSLoMYg9zuAXVKEp7RcPz7EjInpI1rFNYEZMuauuyNj3N9Vvw5yyRJNf01FyIjUHtXa34OpXkxJkRaLVvAfH6hVNJdDjSuHmAR36bfkE9J3f1vRiT4g3b_3wUnkEBz1Wyi_a0M6NJPByaF-ySJljk2KmZYDXuXEqyBjNFmfdwiAa7X0yk7747sAJ5AqI_NF8_3A_mLoMlFKYhZP4txL4yAs8Gwq7KzcRpq8bl53D2cux1yrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370a134319.mp4?token=hpmmTaZiN_JcMfEd31uUyjCu6A_BqJ-7lWpobMsV8IX3Jh4vMEZYxb7r6ZzAF2-fW8WK3M-0O9pJT1qFKUa3fHV8ma7MBFMCuE-VhpMSLoMYg9zuAXVKEp7RcPz7EjInpI1rFNYEZMuauuyNj3N9Vvw5yyRJNf01FyIjUHtXa34OpXkxJkRaLVvAfH6hVNJdDjSuHmAR36bfkE9J3f1vRiT4g3b_3wUnkEBz1Wyi_a0M6NJPByaF-ySJljk2KmZYDXuXEqyBjNFmfdwiAa7X0yk7747sAJ5AqI_NF8_3A_mLoMlFKYhZP4txL4yAs8Gwq7KzcRpq8bl53D2cux1yrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇱
نتانیاهو:
ایران در تلاش است تا برنامه هسته‌ای خود را از سر بگیرد، و مادامی که در این سمت باشم، مانع از این کار خواهم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/105133" target="_blank">📅 00:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105132">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
در پی حمله ارتش آمریکا به جزیره لارک، شماری از افراد سپاهی کشته شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/105132" target="_blank">📅 23:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105131">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
در پی حمله ارتش آمریکا به جزیره لارک، شماری از افراد سپاهی کشته
شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105131" target="_blank">📅 22:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105130">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_a8KikaC5eEqjH7YFnsVQi1t1YfctQCCGtVbP4JdfjalWvMz4RLZvNMr7nRcwe3aJGjn_yBytZh5N3WN0AFLd-nfa9nbm_ImRYMNaA3rFmfkn4YrAilx_ZFBF-XvRUPxUrShYFPJ1LMcRny4qcw33vPvE58wSXfe6xt6K8PQXg_xsa-eOcopwJJ17eivoamm1lxnwEYtNg3CZvDfQTFgnk4o84ZoLgGOOAIo5Kl65lb_Z0TMSIUR2s9oFnAE-PDuKwpUgwMWJvcvCEHt9oTx6foEgNw0hI2Z47ycwj1XKAjaXmlkbhgYrY83_QbL15f2EteYWGj6z6Ygp2SBQld6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180؛ کوپال‌ناظمی از سوی کمیته داوران شانس اصلی قضاوت در دربی روز چهارشنبه معرفی شده و قرار است تا روز دوشنبه تصمیم‌گیری نهایی صورت بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105130" target="_blank">📅 22:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105129">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
✅
‼️
تایید خبر اختصاصی فوتبال180
🔻
در اتفاقی عجیب و کم‌سابقه، از بین نفرات دعوت شده به تیم‌ملی امید تنها سهیل صحرایی از گل‌گهر و مسعود محبی از خیبر خرم‌آباد خود را به کادرفنی تیم‌امید معرفی کرده و سایر نفرات از حضور در اردو سرباز زده‌اند! قرار است عبدی فردا…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105129" target="_blank">📅 22:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105128">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c996886b7e.mp4?token=eS96nE17axiZwDMxTmo5auQI1UMXuAMCNKaZeZ2m2EGkehtUTjKC09MWalCPk2TYutGNgXXOJMeRpuQwnuQPTWC5KcpHBxczy4bSptCyi0ovel6dbZnEbky-2HwgxDEU8kBTFY8Krrc6dP9zImDW4vXT92KyLQYtR2SIscWcxSQD3x7KNXZyHCK5iyhI963nEggCAf9F6tBL-vuyhZ-_sOvtzgNTNbllqFMnOb4-ydGlqgQxcHbSJ-DYJqJBNpWJCdth2nmDBbQSinJ2_K1i2D9wieQKDnCd8AX4l5J5SJ6Oj0HGmp3XxEiqnkalMsn6QNZAKneU_ZntZgNjREZqkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c996886b7e.mp4?token=eS96nE17axiZwDMxTmo5auQI1UMXuAMCNKaZeZ2m2EGkehtUTjKC09MWalCPk2TYutGNgXXOJMeRpuQwnuQPTWC5KcpHBxczy4bSptCyi0ovel6dbZnEbky-2HwgxDEU8kBTFY8Krrc6dP9zImDW4vXT92KyLQYtR2SIscWcxSQD3x7KNXZyHCK5iyhI963nEggCAf9F6tBL-vuyhZ-_sOvtzgNTNbllqFMnOb4-ydGlqgQxcHbSJ-DYJqJBNpWJCdth2nmDBbQSinJ2_K1i2D9wieQKDnCd8AX4l5J5SJ6Oj0HGmp3XxEiqnkalMsn6QNZAKneU_ZntZgNjREZqkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کنایه نیکبخت واحدی به رامین رضاییان
📝
نیکبخت واحدی: من نه در کوچه و خیابان می دوم ولی سیکس پک دارم! (شوخی) اسم نبرید آقا از کسی، من نیکبختم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105128" target="_blank">📅 22:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105127">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d54666045.mp4?token=EwLCFie1OLDDrn_MnYuR6sUwXqkrqIN00T90xpN4G2G-m1ba6ovGR8z97-B8XWvSCchrg0FHC25Nv_g_2n7pQT0CDX09yR1gqDwvund6xvTrGGIrQBEnwg1eKahGNezGS0-QqKUD45oItT9fejbQtlhErXTkT3QvGSk0gOjGTWFZCwsF7ZZcAMXjwAFMPfmA4xbuKCn9wDlu8GxJElyLCGLKjVC7-7ArCc5YPq0tqt26FGQiuxHHgY8j_0QPf4vl7npBJdNMjCPTlBeuLvMzQPEEBFInEvi7ma4ET7LW40_XMDMnVcHG_zx4qFqDG6FYpRWdszlWn4mPfUkCvKoMCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d54666045.mp4?token=EwLCFie1OLDDrn_MnYuR6sUwXqkrqIN00T90xpN4G2G-m1ba6ovGR8z97-B8XWvSCchrg0FHC25Nv_g_2n7pQT0CDX09yR1gqDwvund6xvTrGGIrQBEnwg1eKahGNezGS0-QqKUD45oItT9fejbQtlhErXTkT3QvGSk0gOjGTWFZCwsF7ZZcAMXjwAFMPfmA4xbuKCn9wDlu8GxJElyLCGLKjVC7-7ArCc5YPq0tqt26FGQiuxHHgY8j_0QPf4vl7npBJdNMjCPTlBeuLvMzQPEEBFInEvi7ma4ET7LW40_XMDMnVcHG_zx4qFqDG6FYpRWdszlWn4mPfUkCvKoMCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
😳
کسخل‌کردن مهدی‌طارمی توسط بازیکن شباب‌الاهلی در بازی اخیر الوصل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105127" target="_blank">📅 21:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105126">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grY5Az3fSi5HUww4bT9HILr_xdkaMLnb_NRyzRohdJqs62tl8u7x3b4FX5OtUD0MxfihQZEmnetB8qu6NdbgjuEdvHkegiFhZKdd0aBqIj-ndjypEFLfaMbsWo2yLBsxgglfh38b6mt7yIURIsp2e_eyjL7pxZDAxh7i5127cBKJ3t0FyrKLN_UgoJBhm1JNUfWLJhruVuQf4x9TwTfJOrLuGzWPLcIW0Vm9UtGxiW2T_suKHq9SPUQ5xPXx2UjOuUA-s8Baz1V8Z5PtontC_iruCEpJ-w00lzUjMRBMhOW6uHQPH01I9ckzhwq9Zy7MZ0oPIFq2l1EsXRJXNpqI2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گگگل چهارم رئال‌مادرید توسط آردا گولر</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105126" target="_blank">📅 20:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105125">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">منچستر سه تا به ایپسویچ زده برونو فرناندز دبل کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105125" target="_blank">📅 20:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105124">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گگگل چهارم رئال‌مادرید توسط آردا گولر</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105124" target="_blank">📅 20:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105123">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌برونو فرناندز مقابل ایپسویچ‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105123" target="_blank">📅 20:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105122">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🔵
❌
کریم‌بنزما فرانسوی بزودی باشگاه الهلال عربستان را ترک خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105122" target="_blank">📅 20:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105121">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26beec0b11.mp4?token=hxMunbKZ1FhHuWg95M_m0ipTNNG-QB4uizfzGLo5LcuKciTwloD51GwrN5MtRnBuLsmxU3CevwM0a0D0zrrmxtYNDoJlvBM2KVaP7iOqH2GEmzn6ciy3B_wNxpLXbbSyeDMu3pKFz6vF0fe08cWC_SqLlWH9X9d8khJij-rVHvH-V4MoS37tCN4ZL8x3YEKXFz-SfnKmAVVuLcy9XT1NB5tUiW-x5GG8l9j1JLruh1MnZOkBmbRULiBbjuOF0FKDqx7V0wRcOsxNLlJeQpdLitVxuVVAlDm9V-vsrZ2UqCfw37K0fNKd0XoSu1m08A7w5eHT_C3xuFrf0P-ONymE2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26beec0b11.mp4?token=hxMunbKZ1FhHuWg95M_m0ipTNNG-QB4uizfzGLo5LcuKciTwloD51GwrN5MtRnBuLsmxU3CevwM0a0D0zrrmxtYNDoJlvBM2KVaP7iOqH2GEmzn6ciy3B_wNxpLXbbSyeDMu3pKFz6vF0fe08cWC_SqLlWH9X9d8khJij-rVHvH-V4MoS37tCN4ZL8x3YEKXFz-SfnKmAVVuLcy9XT1NB5tUiW-x5GG8l9j1JLruh1MnZOkBmbRULiBbjuOF0FKDqx7V0wRcOsxNLlJeQpdLitVxuVVAlDm9V-vsrZ2UqCfw37K0fNKd0XoSu1m08A7w5eHT_C3xuFrf0P-ONymE2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇦🇪
فرشید باقری: بعد از باخت ۶-١ استقلال به العین منصوریان در آسانسور بلند بلند می‌خندید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105121" target="_blank">📅 19:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105120">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04532a5e26.mp4?token=Vd5a3j1pVlH1h2zBeqJXIbqIjo587k8v2_TVIgM6sijcOBjklWEKjvSDzr8PG4QHIrNLyV0O0rtHKDxc09vogFRO8TXIn2uf5VyhdCUl-FBuUDFWW8VTN3nX36K8dNTR5K2SZ2GqiogZounD9xstcco5sGuiiE96Bu7U66loABzmFEe1Ji3l4Cjqib8YsPE_4ra-oyIUXZHYjyPdMM2jKXQq7-CEXvRCcxtT4RGgN1bZvvN_9cfoXksqJgK_ySyMNj5OD0EIDZEmNs-Zs4HCw22DoXZo30W6x6htDrwa016hEgbTqv912l6xW-zPwYbe72WRbuGkYmLthjVCERJERXTYG9lPnMqd6AluFYsAiullXyq-UF_JsULLG27qWjQehfEwHUhHXABLSONAZsOt1R6H8-8Ler7HJTNaioC_EjdxiM4V8kOKBEix-Y2miq39AKNGoxa5FxHcbTFQwEmlRyBK-3ixNYZV76w4G_jWwb3XVcJZBiJGzptjpPKxas4YUT3GwvUtQ2ZQro8t768e00R-N18u0ImYIaH1VjGskYiY8K_c6M5FNWxQ6km8n23z2tJwppI0CnsyJlfPX1wxgJk5knFurKyREFHPjR3VxrgTQEUrqe6_WeKamJQuVmCPzFXpi8L-q75piWNt7w7o5-S4v_kxIk3ZGFP-87uoXl4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04532a5e26.mp4?token=Vd5a3j1pVlH1h2zBeqJXIbqIjo587k8v2_TVIgM6sijcOBjklWEKjvSDzr8PG4QHIrNLyV0O0rtHKDxc09vogFRO8TXIn2uf5VyhdCUl-FBuUDFWW8VTN3nX36K8dNTR5K2SZ2GqiogZounD9xstcco5sGuiiE96Bu7U66loABzmFEe1Ji3l4Cjqib8YsPE_4ra-oyIUXZHYjyPdMM2jKXQq7-CEXvRCcxtT4RGgN1bZvvN_9cfoXksqJgK_ySyMNj5OD0EIDZEmNs-Zs4HCw22DoXZo30W6x6htDrwa016hEgbTqv912l6xW-zPwYbe72WRbuGkYmLthjVCERJERXTYG9lPnMqd6AluFYsAiullXyq-UF_JsULLG27qWjQehfEwHUhHXABLSONAZsOt1R6H8-8Ler7HJTNaioC_EjdxiM4V8kOKBEix-Y2miq39AKNGoxa5FxHcbTFQwEmlRyBK-3ixNYZV76w4G_jWwb3XVcJZBiJGzptjpPKxas4YUT3GwvUtQ2ZQro8t768e00R-N18u0ImYIaH1VjGskYiY8K_c6M5FNWxQ6km8n23z2tJwppI0CnsyJlfPX1wxgJk5knFurKyREFHPjR3VxrgTQEUrqe6_WeKamJQuVmCPzFXpi8L-q75piWNt7w7o5-S4v_kxIk3ZGFP-87uoXl4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌برونو فرناندز مقابل ایپسویچ‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105120" target="_blank">📅 19:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105119">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یونایتد ذلیل مرده دوباره گل خورد
😐
😂</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105119" target="_blank">📅 19:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105118">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c131dd4b.mp4?token=tQzOpaAUyDuXTebi_3DhYDaYOVwLsAWPbe1YzLbmF7uTwTtDv-ady0Wid8Ez9is9OmnLV7-I64nN1K-bfFTVJlovxTeO_E2OUAHb75xUe0Na8vlhYL38e1swAN-yU0YNhZkGmFt2M5KWPj5FO2KRtOYBVDkUUOUGAmckyVvSU21N3POCDV7s0VX2mkaLxjJl0dbR4qdWuU-M1_yXkwfEVBjJ5IibQTT8l4hwRfOPqgBYAaCo946mv4XcqMFy3YoIfLxmnFtk6HL9-JrzWo-562PgD03d8N5XIPZk3Nkn4A3b_KTTNBFoLRCPsK_JibTia4TcRzYbvS-SE-0v0xXsEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c131dd4b.mp4?token=tQzOpaAUyDuXTebi_3DhYDaYOVwLsAWPbe1YzLbmF7uTwTtDv-ady0Wid8Ez9is9OmnLV7-I64nN1K-bfFTVJlovxTeO_E2OUAHb75xUe0Na8vlhYL38e1swAN-yU0YNhZkGmFt2M5KWPj5FO2KRtOYBVDkUUOUGAmckyVvSU21N3POCDV7s0VX2mkaLxjJl0dbR4qdWuU-M1_yXkwfEVBjJ5IibQTT8l4hwRfOPqgBYAaCo946mv4XcqMFy3YoIfLxmnFtk6HL9-JrzWo-562PgD03d8N5XIPZk3Nkn4A3b_KTTNBFoLRCPsK_JibTia4TcRzYbvS-SE-0v0xXsEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بیچاره اسطوره فرگوسن با این وضعیت میاد اولدترافورد بازی تیم‌فلک‌زده کریک رو ببینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105118" target="_blank">📅 19:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105117">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یونایتد ذلیل مرده دوباره گل خورد
😐
😂</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105117" target="_blank">📅 19:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105116">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
حمیدرضا گرشاسبی مدیرعامل فولاد علیه استقلال: شروع‌کننده اتفاقات بازی، هواداران استقلال تهران بودند که پرچم فولاد را آتش زدند هواداران ما بعد از ورود هواداران استقلال وارد ورزشگاه شدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105116" target="_blank">📅 19:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105115">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4630f9e156.mp4?token=GvFFSZtLPoVqa-EZuNFk6rQf_xPu5rfx_4GTr6SxIBSgMEV9PB4PJKfbP05SVUU7nYkJDAvD2eX4P-002GUR8AbGrZiGekb5d5OWk45ubD1w5Kg6No4VrFwEUIusyRJ6I3p1GULvXGtjQqhdDW0D1-BhZQxV0Cdhc2jWDuF7Jxm0IadIBrfqjDNI3nakPXFj26C5XkGIlfw0qgCHfhJigqCCVY1R-pALpi1KufY5pAEG0r_USg-RmeUfFRlkFifzQtmTamJwsEs_C-GY117AvwCNHKNCk6tVklMFVGcnyaKQQHriBa6Vk9PB111NTtoZhinx9pVzmStEugZNdAElNXgceVqF4Ee3HeTNtYKjRVlmcQxbfQu4Nc4J8MNbzys8Ct3xEhTCZfP8yyVJMH4qx-VWPbnE9XUueO9LhwVAg2fvXOd-75KKH4I5cUrWa6gbPCBP0csPIwVp7b-44EADsb6vNmy6ItNCxJI9JvxSAmVcq94Nqr-S6Rsway3bkYWqjHlUl8B5BRxAFAX5Wr6vVU-ZVMCFpfHAhtJiGzTMAK4DbzFNESgRTAWpyrRCjh2-kDDcQ0-pm25FCqTbOrSbJmvfau1v-dUHoHOOfITxf0hQhnE0303H8k539IobkHLI0a2NyYU9RN1mZUngCJM1gVVCPYWEHS1a-HTLZsH7pgI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4630f9e156.mp4?token=GvFFSZtLPoVqa-EZuNFk6rQf_xPu5rfx_4GTr6SxIBSgMEV9PB4PJKfbP05SVUU7nYkJDAvD2eX4P-002GUR8AbGrZiGekb5d5OWk45ubD1w5Kg6No4VrFwEUIusyRJ6I3p1GULvXGtjQqhdDW0D1-BhZQxV0Cdhc2jWDuF7Jxm0IadIBrfqjDNI3nakPXFj26C5XkGIlfw0qgCHfhJigqCCVY1R-pALpi1KufY5pAEG0r_USg-RmeUfFRlkFifzQtmTamJwsEs_C-GY117AvwCNHKNCk6tVklMFVGcnyaKQQHriBa6Vk9PB111NTtoZhinx9pVzmStEugZNdAElNXgceVqF4Ee3HeTNtYKjRVlmcQxbfQu4Nc4J8MNbzys8Ct3xEhTCZfP8yyVJMH4qx-VWPbnE9XUueO9LhwVAg2fvXOd-75KKH4I5cUrWa6gbPCBP0csPIwVp7b-44EADsb6vNmy6ItNCxJI9JvxSAmVcq94Nqr-S6Rsway3bkYWqjHlUl8B5BRxAFAX5Wr6vVU-ZVMCFpfHAhtJiGzTMAK4DbzFNESgRTAWpyrRCjh2-kDDcQ0-pm25FCqTbOrSbJmvfau1v-dUHoHOOfITxf0hQhnE0303H8k539IobkHLI0a2NyYU9RN1mZUngCJM1gVVCPYWEHS1a-HTLZsH7pgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحنه گل‌سوم رئال‌مادرید توسط امباپه
🔥
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105115" target="_blank">📅 19:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105114">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlSeqWoy_ekQoZPo9sFTAWP3IHN6ZsWa7rha7fGQo5RvcY_SJgJAWhQD1xXwn2IrwB98Jf3QFUISvu_XHZGBggzht_Ru3z-FxLMol8nX6l31MvjpeQRAEnt3AM_xeY1p9tt3oB9boKmCeZYgv8s-6EIbdiM1kGoSqH1xteatkUPnYupuVJd_PPsuQ6hs7rbFOkDcA8-V-4UcKTlkKeDDAbbw0DOPersX59JRc_IWCq6f1McM0n2-tOI7TjqrRFqWpM7RIeQUZzscWcEFSpX2y5Y6-JD6WTm1nh6qpy8mfkviaNV1zkcKqOJvvSpeHRmHsKPMMywk5ptPJzp2C5VklA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
استر اکسپوزیتو دوست دختر امباپه تو ورزشگاهه و داره بازی رئال مادرید رو می‌بینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105114" target="_blank">📅 19:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105113">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c6217fdf7.mp4?token=cqaQcVDLnyt5VtmWoblghOVTA1puIpG9KTWP8E84WLqQZHrFFqX9lCA9H6GhLxALUBvV9JFN5ZWbubwTTThRJW3UrTgFK91HZ6nFcfNMW94hIDlkfTJtAVZ7PP_1MaxlYi7un1nMQJhDVVfWQVGtyYfPHNfBU748sKvoLEvyQ8ps5cYTig2b763T2EggS8QmokFOlges5mnYFBnK5RylfywZdhiZudtpWbwk66660eAj9Uc6rC2WwDHXrHQbA1kglBIGJqshHNq3bBKFdaf7SeQMSdd0gd95OQJhRu6l9G5VJFLYeCvGw4tj5KDTfPBTVo1kFaBjPCfDuxHv6o_1n36cyLpduYTfg1CJd-v4E6joYwZ3oMH_Y_FtYGQ7X_Zcd6l_RLwKiKdES26w9CiOJH7746hGzlurotKEjyeMhoAMNwxm5ILNP0QCjda11EzH3f1TJpd6Jd07Nvk8fghLbUxhOMggyGdL0lxcDAnZtCjQSm65qe22loI4kHZTZP4pZMBT7OPmUKl-aCjIkOSlFfdd7J0U2p7hPObtVaIJFpggmpdaSjrZhK8IxtFKj-PZNV4gwWntcWt_4dtTdnyYmtD2QIMkpunLHUUD4WgDtijtLG5WZyv8SsB27V1bA4kGF640PQoqpgOgd5vRXT3pfI5Em3sYbXqjNUyAydqbvKI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c6217fdf7.mp4?token=cqaQcVDLnyt5VtmWoblghOVTA1puIpG9KTWP8E84WLqQZHrFFqX9lCA9H6GhLxALUBvV9JFN5ZWbubwTTThRJW3UrTgFK91HZ6nFcfNMW94hIDlkfTJtAVZ7PP_1MaxlYi7un1nMQJhDVVfWQVGtyYfPHNfBU748sKvoLEvyQ8ps5cYTig2b763T2EggS8QmokFOlges5mnYFBnK5RylfywZdhiZudtpWbwk66660eAj9Uc6rC2WwDHXrHQbA1kglBIGJqshHNq3bBKFdaf7SeQMSdd0gd95OQJhRu6l9G5VJFLYeCvGw4tj5KDTfPBTVo1kFaBjPCfDuxHv6o_1n36cyLpduYTfg1CJd-v4E6joYwZ3oMH_Y_FtYGQ7X_Zcd6l_RLwKiKdES26w9CiOJH7746hGzlurotKEjyeMhoAMNwxm5ILNP0QCjda11EzH3f1TJpd6Jd07Nvk8fghLbUxhOMggyGdL0lxcDAnZtCjQSm65qe22loI4kHZTZP4pZMBT7OPmUKl-aCjIkOSlFfdd7J0U2p7hPObtVaIJFpggmpdaSjrZhK8IxtFKj-PZNV4gwWntcWt_4dtTdnyYmtD2QIMkpunLHUUD4WgDtijtLG5WZyv8SsB27V1bA4kGF640PQoqpgOgd5vRXT3pfI5Em3sYbXqjNUyAydqbvKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبل جود بِلینگهام مقابل مالاگا
🔥
🔥
🔥
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105113" target="_blank">📅 19:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105112">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔥
🔥
🔥
رئال‌مادرید
😆
-
😏
مالاگا  دقیقه ۳۰</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105112" target="_blank">📅 19:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105111">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">امباپه سومیییییییی زدددددددد
🔥
🔥
🔥
🇪🇸</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105111" target="_blank">📅 19:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105110">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گلگلگگلگلگلگگلگلگلگ</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105110" target="_blank">📅 19:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105109">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/28e9c89379.mp4?token=mZRqzLduZONBkSP80yVVKOll64Cszr25McYC6iEGnDEE8g4xEyIgSfTXo_FaU7mXVpabX28dTNM7iF1rs0aVQNuONLgC6MWq-OU1BalDC_xN5_MdRj1pLwo5ux4ejB8p99MoJSKJWL5e71RzFcjZZ_KHOlz6gI3obFPVqmepqT88eJGQ3ZNy_nl4OvaAVH9V6DpgkKQeaUJZG0XUOHViPd96EWv8wva5kIxsgaWJMcXQuQ3KdlKj6tKbYUwr8OA9qUeN9ecm-Y4lMUDjfeaPmZY5ikvHkHpMw4guat1vaTwqiPr1CX-TusZxpT6b5RWdBmDrCfy_79bZWpzCWoqurDLXev0F9o1MYczK0mPMCClbxhN_FxNTgX9zheFOWUgHhOq0rjN1gC0bTxRcoB7mQl9wlpHbPBBmdSeezcBFVI72sqvLOqzXEhDdDHRQlYqpy-5JK5LKY6g2hoLy92E24xVqhWHprnS2j76_wsxSK4O3pFD2J8qlo621_Yn1qeuGL0AezOg_xAMlKvVyVifZZF69aWuVeTN_IlIay2IAjzeyE80q97QV35SnoMI9I1jM_E5prSXYii7awhCiCHaSQ0h0rS4S8U50OhQ61HpPbYyamNoUSjJSqw9lnjWzGaT4DfaeX0u9G0kClIZ8qw-MsLK3htKIu1pC3JU-QjrzJik" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/28e9c89379.mp4?token=mZRqzLduZONBkSP80yVVKOll64Cszr25McYC6iEGnDEE8g4xEyIgSfTXo_FaU7mXVpabX28dTNM7iF1rs0aVQNuONLgC6MWq-OU1BalDC_xN5_MdRj1pLwo5ux4ejB8p99MoJSKJWL5e71RzFcjZZ_KHOlz6gI3obFPVqmepqT88eJGQ3ZNy_nl4OvaAVH9V6DpgkKQeaUJZG0XUOHViPd96EWv8wva5kIxsgaWJMcXQuQ3KdlKj6tKbYUwr8OA9qUeN9ecm-Y4lMUDjfeaPmZY5ikvHkHpMw4guat1vaTwqiPr1CX-TusZxpT6b5RWdBmDrCfy_79bZWpzCWoqurDLXev0F9o1MYczK0mPMCClbxhN_FxNTgX9zheFOWUgHhOq0rjN1gC0bTxRcoB7mQl9wlpHbPBBmdSeezcBFVI72sqvLOqzXEhDdDHRQlYqpy-5JK5LKY6g2hoLy92E24xVqhWHprnS2j76_wsxSK4O3pFD2J8qlo621_Yn1qeuGL0AezOg_xAMlKvVyVifZZF69aWuVeTN_IlIay2IAjzeyE80q97QV35SnoMI9I1jM_E5prSXYii7awhCiCHaSQ0h0rS4S8U50OhQ61HpPbYyamNoUSjJSqw9lnjWzGaT4DfaeX0u9G0kClIZ8qw-MsLK3htKIu1pC3JU-QjrzJik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
گل‌اول رئال‌مادرید توسط جود بِلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105109" target="_blank">📅 18:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105108">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔥
🔥
🔥
رئال‌مادرید
😀
-
😏
مالاگا  دقیقه ۲۵</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/105108" target="_blank">📅 18:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105107">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دبلللللللل بلینگهاممممممم
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/105107" target="_blank">📅 18:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105106">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105106" target="_blank">📅 18:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105105">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYkMVVAXDAZCI06Bwl4hKVIgCb2zTc8lwh8h5G3fWbsK5Wc0GAjOOicnmL1rZQREwz2I71q04BJLy12N5nfNz-n1RqIEqZJMg7lJYj-ITzLkGopdrULRQKjS3nE3IUKHKJ5jtPuyyTlxwZ8ur2hyqvvyK36z9L_9GPVJ6g2Mp42oC0jFk2gAt22osdCiiTC3lPmBMsNaqeZ51GV0qlSgpBKeVQSW4fx2g5OS-6J3rW3AufCNXgS1oIfN3tQNnsJMT8HvM7nl5DD3wtcidvWkOIA6g9R7-jnraajtFTqsL72QQHteAEqk5y0x0NiCQFXNt2r0jogyA9-Z9-BNvXu5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
‼️
تایید خبر اختصاصی فوتبال180
🔻
در اتفاقی عجیب و کم‌سابقه، از بین نفرات دعوت شده به تیم‌ملی امید تنها سهیل صحرایی از گل‌گهر و مسعود محبی از خیبر خرم‌آباد خود را به کادرفنی تیم‌امید معرفی کرده و سایر نفرات از حضور در اردو سرباز زده‌اند! قرار است عبدی فردا…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105105" target="_blank">📅 18:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105104">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔥
🔥
🔥
رئال‌مادرید
😃
-
😏
مالاگا  دقیقه ۱۹</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/105104" target="_blank">📅 18:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105103">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بلینگهاااامممممممممم
🔥
🔥
🔥
🔥
🇪🇸</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/105103" target="_blank">📅 18:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105102">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گلگگلگلگگلگگلگلگاگاگگاگاگاگاگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105102" target="_blank">📅 18:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105101">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebsvStXTWyxIRFGq0hAWP5AaZ5yZDlFVt3hBj3sDh1mq4zkz3ZovFQaHV0DxbYPgS1LJITLmdP95z6vCxSVEOKlrVyQB9jCL8gzlxRePdWdqkxFzzP4C-eQEvRSRC3ACZdL2-iM3ejmGfg5VSZHEUE6H7xpr1CeOlKvjeOpjHRL1pe9z9VVkQr7HOwg-ukjUcF4vuYS5Dr8oR1dl0bWEsqvPYmRLzeZyLeIPl0fWMMUVVyi8yQkXgTXWgCojbrqb1Mghwjqyu32Ybukyx8V-s9ItnP_hniIoW7b6HvWgNWCj06NARoX2BdprXE8PCbtN2xth3KpMxEJVuc2fCZ5-dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
مقایسه خط حمله الهلال و‌ النصر عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105101" target="_blank">📅 18:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105100">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcWWPc_tz6mJJfzhcAiY-RuKmqLuHLgY93Ojaxmy9qgNh9gET3jDrYow7_vRap9xNubqeWeBvmVA6kzeDgvAYI1Z7qVXWbNRtx6TimmZ7ePQ9lVbBYsqFpODoiKUnYBhre24WmERGfvLCZ_Jq9H8SpOtq50F4km2uc2PUBGKieJxDabOQITzRNyPSBk8p0Q4zex_pm2bMXzE-M64zHFiRxNSo1V6p_pnbLyp8m3QDCytRPhOYOjgjKFucah8QdDwDEdA9ZKG3C5IwZ2X1RTlwgew_y6xiG38lyUBCUodS2YUDrS0oWgMwNOhTRSjFaGlOwz81uOm2bYaviLvMTz5LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
#فوووووری؛ گابریل مارتینلی از آرسنال به الهلال عربستان؛ HERE WE GO
💸
مبلغ 65 میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/105100" target="_blank">📅 18:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105099">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی پرگل و دیدنی چلسی 4-3 برایتون با گزارش شایان آقایی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/105099" target="_blank">📅 18:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105098">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tG4UDoktLs2_d_5i4vkvyIXFAA0fvXJ7ljK_7mJti0_7rriPOHTVX5xQXW6HczsHAwiLAegATy5-5LORd9K_-bY05zG1vPQBCqUxae_mJCaPGQZroO8Gk7IdLY4pOWl9lloB6p0hVV957T6mNrCxmcIyRr6pxplexnFH8z79qw9oQeyvBUrlS60nAVUC2AoYvDQipXphFPuouz7jdiscVdICf9nhUoLT1fIh9-kS0niP3vvLX9jQwRvaiCn9Rr02QA6bBy-3WIKA8vDgDctvTbOxOWoGOX5mZg0GwuZjdMNpS8Ay4t079FwoizEgRHz437Ph_I2ym5QTNFeo-MZ22g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم پریمیرلیگ؛ پیروزی سخت شیرین در روز رونمایی از مارتینز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی
😀
-
😆
برایتون
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/105098" target="_blank">📅 18:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105097">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qby75rxE93-txDD11t9_Mo_EVEi_mBMmwBscIY0_8skAo28nCkz07iG7Ic_-2CaR91L4ENtOfGeAQqZ_CTa1XhM0QkEMqj5QXHqBxKCQM4v53GRO7rGBVNzobi34csyk4LgOW99RJn8n8Kkez_LtEqCFOT6KoaEj44V6oA5ghhYOOLyakH70eHbjuqdWgWm5bIsz86zVlfWHAjl49psVSxjH7OMtpTjjHoSzkueVgM0pDbT9XehWF4saEmjz-teNMPKeBCkmZ_Ls-OgQsvMqNM2xFi-oRxIqhb7otaL4ZJO9zvK9ZAkhPVYYkMthY1v8dUg8j0IV13orSidqRo6JCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/105097" target="_blank">📅 18:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105096">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8QS_YAEyVUetTDqZ-RHnKfiOtVTS9noy2c_27xQCA8buTG_z3wt8Z4Iw1QIRrOudo5_GeDN8mLEvOfB5CFYeHMljCm7UUykN0YTXTC1NDnZ2TInTrfFE9q_GHTu_VCYRbmAz2zvktdXE1WfjPmtYhSb3xWP_fSCdtNSAD7TvUdotXFLMkcxRZ4Vc-orLWjp3jSqcbQz0wtWXjc9SoBGdiCwJBOSonX9IL6a0iZHvb_P9ATlwXqs5PmRfkB6gSqaM-MpZXNAV3QnZKR3omeWTjllysvGzjblZtfH9ToX-8J6Nruz99s68GXMs2V-97g0mf8DKXtEdI-PKKboFGzYnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم‌پریمیرلیگ؛ ترکیب منچستریونایتد مقابل ایپسویچ؛ ساعت 19
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/105096" target="_blank">📅 18:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105095">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9709b25451.mp4?token=qqL0CwqhYhwNUHD7BZFy6xwBuxI1saM-j2Bzwx23Ewtt31MDpKPmG6kpsfgWGDjqly3_bwP4iXplL0zWoSB8xjGdwEUeqDaN6OMeCEqaaNOcDKVamR-LJ-RUZCztcI1cQFXVwpYdX6e_hbm9CYNGdF5-iZAGQM3dapF5D0w6-xDAcPBH85GId7Ur73afFNzP8qPg-6jvTm_-9x_WhScAmVkw70au5nEqGT6qW6P9fh9WxZCJt2GS3YConI5B2fgcB7G8uiWdR_amCj1naSrpTiulT0rfzlQx5PjXr57tW-aZjnuzh5ZDkY4ux27I9zbIXudoz-YeRkaeDSzv1QjOMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9709b25451.mp4?token=qqL0CwqhYhwNUHD7BZFy6xwBuxI1saM-j2Bzwx23Ewtt31MDpKPmG6kpsfgWGDjqly3_bwP4iXplL0zWoSB8xjGdwEUeqDaN6OMeCEqaaNOcDKVamR-LJ-RUZCztcI1cQFXVwpYdX6e_hbm9CYNGdF5-iZAGQM3dapF5D0w6-xDAcPBH85GId7Ur73afFNzP8qPg-6jvTm_-9x_WhScAmVkw70au5nEqGT6qW6P9fh9WxZCJt2GS3YConI5B2fgcB7G8uiWdR_amCj1naSrpTiulT0rfzlQx5PjXr57tW-aZjnuzh5ZDkY4ux27I9zbIXudoz-YeRkaeDSzv1QjOMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇮🇷
فوتبال خیابانی روی زمین چمن؛ هنر این روزهای تیوی‌بیفوما در ترکیب پرسپولیس
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/105095" target="_blank">📅 17:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105094">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIqLSWpY2178OUkO92MrBZpk3Kz2HKALo8qf4smAHJXFJ6TumZFgheXuXAktsh0em6vQ85R_4b1_RTiOjcjEY-PfmeefV7mZzWdrRd1Bg8WcJmywKgUfek47kBaTErFpLRIe2LirotA_0W1nmkZB1BWWXewN-8nU1O9NGkrgkWkobcoMmEXpp59B47dd-J8qDSqPGARpMv6jf-a5kUY8WFC0D3P7XfKp0r_TFqTQCNaCLdSATgDLCfKCKac8YfUIFZljwe9-6J9FbdNUT9D5kYPOdfe7xsnVmsK8vGKXakyVJUeFwUCyJEI4BfBEwzMf89H4hq8YESnXUQDw0YLN_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
هفته‌سوم لالیگا؛ شماتیک ترکیب رئال‌مادرید مقابل مالاگا؛ ساعت ۱۸:۳۰ شبکه‌سه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105094" target="_blank">📅 17:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105093">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOe4hoHMZV-f7cdfblXAI5TDwNlDwY2CvNntbZ1-bPdYa7F4j1Lw2W5Za0-x9pt4a1rrzYcVQ-VgJNc3iFtbBR8iRqHfcac8cXlpKiOXO352gMRtCAdOrVJSSeDs83DPVrXjpX3pfJUPN6w8cg4sW6j3qZzAPFPmSMPowAFpV5BFbpGQsnkpMMIKtAkD0u1VFI9Fl58T2bLC-ESQxZ460lLvzUdWE-5S9hnYXpsTebFUa0vL1ut7byBbEhnmsqvRQpDHUyyNc3A6Nr35I_BR_cR47aofGi_lBqlsfQB7KqdXakKo08qkqmSXkpDeSZxdmFwTR4tc3HSJW380Zh3K9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
#فوووووری
؛ گابریل مارتینلی از آرسنال به الهلال عربستان؛ HERE WE GO
💸
مبلغ 65 میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105093" target="_blank">📅 17:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105092">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8czCL4qQxROqAdLlQXPAfew22vB9VhoVhYH2JpSGBmiqeblWlIH8Jv-KT9_Qfl-v9FALlVw_srMLv1mKgsJqqIElgt5IqI6eImQFQQFtcAkyYpeeM_rTlFikAo1_xzuupFh_LcgPJ0h5G5rT7wxSw-ckyDckvuoQ53IMVNFM1403tWmHrzycy158U4APpaOmJdAe_zkq9xC3uReMcuPgFuY64ZBNk1QzKbfG2AsLBtiUTXH0Vqp2l9K0pMd14ID_I3fXIu5I8UfX8H1GFCYFhnrF-b-Fpi-J56-CBUcmM_XUbs43rqJsQKPPdaIT_bsTi9B0GZott5VjjxTdNnxQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇸
جرارد رومرو: گابریل‌ژسوس با نظر مستقیم هانسی‌فلیک در ساعات پایانی نقل‌وانتقالات جذب شده و نظر کاملا مثبتی روی این بازیکن در رختکن بارسلونا وجود داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105092" target="_blank">📅 16:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105091">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7uuBB6Qz89WwEVTMVO_YdEts_ZxOIJBBfBBoYlNJbYIhwGQz77iXW4J0Va_By4z-x1bh-xstW-XOvSahIX0eWDHrlCMRJxJS6k-Q4bZoVBNE-bWrHN77p8Ph613pal9Aq8CyZhrHZno8VpYmegbWmUe_oXl7sDw8ctR3DQOEA-JONqOE3FJACOldxLbMnaGo1WFPA0z6Gv0bhao4-nrOHYxzzc2b3BoJpH9nU9cbC2H0G9bNoa30IWehzT9Hfs55ivYgKdPXATwjPqUASQ7itfWbZQcn0sO-drCcd2vU6ZXGKZR30VEV6x_5y3EvY-d_ICdDkYqT-s_4uIJbC3ILw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
بازی‌های فوق‌العاده سخت بارساییا بعد فیفا‌دی اکتبر؛ جهنم واقعی قراره تجربه کنن
📅
۱۹ مهر - ختافه
🏟
📅
۲۲ مهر - گالاتاسرای
✈️
📅
۲۵ مهر - بتیس
✈️
📅
۲۸ مهر - پاری‌سن‌ژرمن
✈️
📅
۳ آبان - ال‌کلاسیکو
🏟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105091" target="_blank">📅 16:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105090">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f55f5f095b.mp4?token=CDOh7SzKXN2u32ZpsT7XYI_XW9m_KoJiw_WM3_sJj5VsAWjBH9jacZ_Q7qePFpYPz9fNdGU4hpxiR5SlKbGD-A_5p_kuLK1gtsH2Mexnqw3C4Vgx85gd7Rex1VHh1hTiOC7a02hzyOnhKC9VxKk2bUdtPlJrWNCqhOT-BIhCHX5L5NoOtizS6KrDf2UC9qL4HJBaJzI95k7JuZIeJ_H_kf8sqPIBHl8QZ4Cvy9GcxywA4-wAMKs9LLcUQep5gpMDGjN69a8L8-qnfdLYk8VzzL3HPmgg6ZrzkZq3-e-9yb5fr1SyE8CleXygn4Hg25jKy-_VE95ib9L_O_eHf2xLEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f55f5f095b.mp4?token=CDOh7SzKXN2u32ZpsT7XYI_XW9m_KoJiw_WM3_sJj5VsAWjBH9jacZ_Q7qePFpYPz9fNdGU4hpxiR5SlKbGD-A_5p_kuLK1gtsH2Mexnqw3C4Vgx85gd7Rex1VHh1hTiOC7a02hzyOnhKC9VxKk2bUdtPlJrWNCqhOT-BIhCHX5L5NoOtizS6KrDf2UC9qL4HJBaJzI95k7JuZIeJ_H_kf8sqPIBHl8QZ4Cvy9GcxywA4-wAMKs9LLcUQep5gpMDGjN69a8L8-qnfdLYk8VzzL3HPmgg6ZrzkZq3-e-9yb5fr1SyE8CleXygn4Hg25jKy-_VE95ib9L_O_eHf2xLEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
یه‌سوپرگل فوق‌العاده از مسابقات هندبال بانوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105090" target="_blank">📅 16:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105089">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCfPJIErbsAOmoFcrZFU0bX3T1LRDMjOIFdFHbbfq1lh6RxiYZ3W9uXGZX2ck0n79mXcvxP9d4-Y9FDJge-5MjpsaZHpIDjEqigKQDp4s5BJ1zinrbGvlW5wb0V07S894vqESsuyclgO0AM1aB9bkQoxOvuVS-x-GBePZJBdfk847aTna-_JPVAnh_NXc2UITHz7AL4IWCpDiR1Uxx0BUo80o56hppNjZ280ThTsV9Wj5FnH_HfEFuFi9nK471S4YeEpThnHsvQ6FwndjXpxGPc89djuOTGwRTvhCXALpn7PS-xvoPjwGDkjbjmhWtsQiYSTAtk3R8ztTHknCDEm1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
🥶
مقایسه عملکرد وینیسیوس و رافینیا از آغاز فصل 2024/25 تاکنون!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105089" target="_blank">📅 16:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105088">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09cf549f8.mp4?token=Z-wp71T22Aa1UWYJjfIUl0aqrK_88lXzgUKGBbOeLYqdwmNNlgk5BqAKuFqgVmsmoa7YlUVWCW6xAl7qpsuhmnD2S4_DswRuyGWgYgU5-_2O5SRQZ_sXFDLtMQNrKXjkiuCeeaZVjBZkuJ0kKM0z5DshdCT1BgWlLXo4tuArK9drq0hsS71zfvAZgG7cOoEleyB11NYSx9Sw2gucIhXxXodSdx0Ylx35Ik6xCdm792czq7u8yup-p_lBurgUZTSj1pdg-5Oexr6AdY8XvmNT3_x2aZJ7zJ7BSByr70IWs-yS2U4TDFhlm5CSw1tlWCE0mLFnpwVT8PPogqIhthxOQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09cf549f8.mp4?token=Z-wp71T22Aa1UWYJjfIUl0aqrK_88lXzgUKGBbOeLYqdwmNNlgk5BqAKuFqgVmsmoa7YlUVWCW6xAl7qpsuhmnD2S4_DswRuyGWgYgU5-_2O5SRQZ_sXFDLtMQNrKXjkiuCeeaZVjBZkuJ0kKM0z5DshdCT1BgWlLXo4tuArK9drq0hsS71zfvAZgG7cOoEleyB11NYSx9Sw2gucIhXxXodSdx0Ylx35Ik6xCdm792czq7u8yup-p_lBurgUZTSj1pdg-5Oexr6AdY8XvmNT3_x2aZJ7zJ7BSByr70IWs-yS2U4TDFhlm5CSw1tlWCE0mLFnpwVT8PPogqIhthxOQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
تیکه‌های فوق‌سمی مهران مدیری در سریال مرد سه‌هزار چهره به عباس‌عراقچی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105088" target="_blank">📅 15:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105087">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4dfc3046d.mp4?token=KcVjt9EaSLACYtfhyFE60LN20_qnfs8OUjNIrOQtJWaOP27FkG4wTDnBVj03DFj8r9U1JfjmLMo9IPhft-fwavhvr0grZpVMU2-KdnU4Nnk4y3Ww69CmlWAK_16WAd1SYcIbno-AqtCmp9YgwFUStngFOJ4p9diR0Kr1N2thQaH89jeu-9f3HmVCFEeVSVQLjRsa_SVCwi32C0AcFk61CjSb0ehgkWRInkvMWovjQNwHXRPMOO3Dn7JlBl8y8PE8AksvRB4kW-zmByhSqCnJjTi1jIq5zpJgpFMc4KGFk1x54vkzg6Q3sq_HmD0HvH_gI7W9kpKYm4ZVxRWd784W1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4dfc3046d.mp4?token=KcVjt9EaSLACYtfhyFE60LN20_qnfs8OUjNIrOQtJWaOP27FkG4wTDnBVj03DFj8r9U1JfjmLMo9IPhft-fwavhvr0grZpVMU2-KdnU4Nnk4y3Ww69CmlWAK_16WAd1SYcIbno-AqtCmp9YgwFUStngFOJ4p9diR0Kr1N2thQaH89jeu-9f3HmVCFEeVSVQLjRsa_SVCwi32C0AcFk61CjSb0ehgkWRInkvMWovjQNwHXRPMOO3Dn7JlBl8y8PE8AksvRB4kW-zmByhSqCnJjTi1jIq5zpJgpFMc4KGFk1x54vkzg6Q3sq_HmD0HvH_gI7W9kpKYm4ZVxRWd784W1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها ۲۲ گل تا رسیدن کریستیانو رونالدوی افسانه‌ای به هزارمین گل دوران حرفه‌ایش باقی مونده.
☠️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105087" target="_blank">📅 15:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105086">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhZfkhcHl6GGWbMuR98SeEAjPPKVIvESSXNuy3CAEw-CiZr5LeTdmfh-CRdwBd0Uw7sTiZ7Ve4HT3eU_n-5JHMlCSzGVfzFqbPwoycLAtPLa11aN-AoXw1z_jrYXHlxPR4bw0xTG_ItC2IiJIeKS8cEfHtLuErg7wDuLJbq4FybUCFwTdOLyv6A4KIT5sYWXc42one0_n3RoB-OSu7kAMdgBkXucg4SPiSPaZfLdYimVGSiIG-touVa2l-G51_ZYwiUSBrdfcf4iWOnv8U3LkmJ3Z4qfRfAtliBlU7M0IH8LGZ-vjOP9ygF8bVq2lSrakXhThdj28TG1NoaIVobTzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😳
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بلایی که دیروز آلیسون بکر سر تابلو تعویض داور چهارم بازی لیورپول آورد بخاطر اینکه داور کسمشنگ تعویض تیمشو دیر انجام داده بود و در نهایت همین اتفاق باعث گل‌‌خوردن لیورپول شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105086" target="_blank">📅 14:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105085">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14f04c2611.mp4?token=djcRywZBoV2zTv3DKlev3Ex9ULE_fRnKIlORVG5cIbCOY2GO9741ruyIUyv9X4CBg-C3xeFew-sTdAINWly5Y_vTjNT-7gRv7hprXCXvKC68aMUbWwIN3vLzh36YgEhUxfr9dhvz8pZkd1IchNJK4TOp6Hix93J-ofjlEj6m7QgCEvdcxF60S6ffIolXKOGNLV1ZV-V1pkOz40vxkGKT5IkGeydt_g4Y7sll_kU3cec0oBslECKe-kkS7UZRf0E4oCvrj9AVxkGWBEzj8oIp3Mxo29EAFhVWUCI5QY3TGDoWvd-lLdzvoy6sxC4lFEfZew9YT3yeCQ3PK2vftq-Wxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14f04c2611.mp4?token=djcRywZBoV2zTv3DKlev3Ex9ULE_fRnKIlORVG5cIbCOY2GO9741ruyIUyv9X4CBg-C3xeFew-sTdAINWly5Y_vTjNT-7gRv7hprXCXvKC68aMUbWwIN3vLzh36YgEhUxfr9dhvz8pZkd1IchNJK4TOp6Hix93J-ofjlEj6m7QgCEvdcxF60S6ffIolXKOGNLV1ZV-V1pkOz40vxkGKT5IkGeydt_g4Y7sll_kU3cec0oBslECKe-kkS7UZRf0E4oCvrj9AVxkGWBEzj8oIp3Mxo29EAFhVWUCI5QY3TGDoWvd-lLdzvoy6sxC4lFEfZew9YT3yeCQ3PK2vftq-Wxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستان دعوای عجیب‌و غریب خداداد عزیزی با رسول مجیدی روی آنتن زنده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105085" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105084">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3436f33e7.mp4?token=E-GyjMxuRmvAHlZOLUnHBIXFpSMc_-NbQuqxUzaW8DQKyO-Ae8mVVXmGfUnT0KwBU59N3Bx91s4DSPLTRA_EGo_24TwJY8xIoZw-6xCap7yX-iK2enfdQ7FmV04tNssIpajUnoekIlwSrlWH7R8kC_ZE7K0FvX-9NrSllHnEnCoX3zsya97HUxuKumB_uNbkVmAl5b2kM3HeZ4B3X0GC9wayKoJEFtfu-1m2TfTR-M4LWoeQogbMzIJ8gHMkIbyKi2tFkj449S5YIajvFTej8xywqIIKfknwOp9ANz1TSARtEX_ZNptKnSZfwxo1HJLW2kP1yXwZT8wOiufl4O2oug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3436f33e7.mp4?token=E-GyjMxuRmvAHlZOLUnHBIXFpSMc_-NbQuqxUzaW8DQKyO-Ae8mVVXmGfUnT0KwBU59N3Bx91s4DSPLTRA_EGo_24TwJY8xIoZw-6xCap7yX-iK2enfdQ7FmV04tNssIpajUnoekIlwSrlWH7R8kC_ZE7K0FvX-9NrSllHnEnCoX3zsya97HUxuKumB_uNbkVmAl5b2kM3HeZ4B3X0GC9wayKoJEFtfu-1m2TfTR-M4LWoeQogbMzIJ8gHMkIbyKi2tFkj449S5YIajvFTej8xywqIIKfknwOp9ANz1TSARtEX_ZNptKnSZfwxo1HJLW2kP1yXwZT8wOiufl4O2oug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🇪🇸
🇪🇺
وضعیت روانی رئالیا بعد از قرعه‌کشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105084" target="_blank">📅 14:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105083">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLMb8BtxMoeC2apumZO6fA-b-8jRXlkY4mMF6B-lW8EJ0DofvVAucTikrNeVuycJmreCBwWOY7xNOX-fhz97GOeePs_GbBoiUcGFzTyicq-UUeRrWuQUkAAHajc1RbhG7_mqgBw9XvgyktTij9dGKzNRTtLbhAqHJ_vuhwxPVJsRsuOMQ8HIAEsQJlF_410mQUAiqS859ozJYldgn0xS9_E_BMjTs77Q54GL3iEyDEy7jqtqZSedFkUkSZCXlP1x7aLawBiRT9VNIIWWbpmuE2OMFaGsTucPuzYqiIpDVrFN44vCDzMd1LBDlh0XGv1cN6aeUua_wSg1jmRM4_nDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
✅
🇮🇷
هوادار بانوی فولاد در بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105083" target="_blank">📅 13:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105082">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzPKYWfozbqWJHe0Xe-eZGy2EBJc1QTuEmrl8aCpHCUNI0QqYwSoJQCLXh4lN0x3sqTtl0IipcfNhCGRmZ2Af0WjPeNlTlPF9dPZAp6F08P5me6L3IeWXBGr84FhbsVVnqYxhmfO0adAYpnf9Sy7uZawfQo5_09w-mJGfwYaQtsuoyb-Hl1--4wiZ75WNrbulh6j0GpWbKiN5JicjTh8jNO82_m3Yy4liWCfVQBXu6ic2d7NtIm07dGelq2NRRDA2eMqzoyZbkcENh_pzT8HpcYiB9ewYDyrn3oxGmscjLUlrx_mZJkyKW3hU1wETFPHcZQICKkvDFZzvkEen5ZgNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
🇪🇸
مبارک اتلتیکویی‌ها؛ آلوارز به تمرینات گروهی تیمش برگشت و بارسا و این حرفا سرش گِرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105082" target="_blank">📅 13:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105079">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RYtq4njhJiXMnwtINMLlWUYeVpoRYNG9jeTqTJLAyy6tCGlB3NSopCrVZdm4SRBtRdQG19fwX1JxWp13IoFyCYUDFubNImKVnNrSXlVYGWr4p1McSageB77RpnZgxZ3W8voQHWBIJ3FWgCmzni81F51fuftNTCuaXZ7X_FYTz28vTfYbr74R2jPOBwmLty0ZdeoNcqMBvNaObL0gaJhMt6e_OwsgpNfTGSkoGW74vwDz2gLGOokUw9_mxFhTm9WXfoXMAzjjNM1Eo9hcnOUq-jBr0gnwHj3tmhr3JEDtH1lYxHN6w10Jzs0x_MNyNLuqrPxqD8oJ-gPN4Sdn2_IFlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgp535ubgnz_CDkCKr53KRdioFRvhBIkfsDOjG_-FozNSI7kYCgMvXtxdAi2BoN3Ltdqn8W0vZL1E5mxR2RzYgPwNkt3ECdtBhFWOg1aCNPo1drQRvi6tBkbG0dlqFPKilTB7NdfoA4wIND-DXvKl_2jQHG-95l0aEAOzbAMW7RZJ-utY0waXIiA1yzIleqEOG9PZyzeu4bJ2DfbKeMXUzWuXP452SoRhARKT5mkTgFTGsfQgXiKFjUUpDy1_zLun_VGa35Z5ThCSGARe9Do1uSCiMhXcZq0m1x9LT9E0MS3j3_Os-Mcea5iF7oV4lkfUTyQlAbyeayrsCM72bNH6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OFWXfSJx26fVF2PyscmYkb85SrsSF_iyspkda7RjE3TOtbRy_-C8AITWR8qK71qy5nE2Gq4dwNBbYA97aZIejwCd2d2-XSGXQc_P1YrI1hv60WQ-E6yl8gc1InLnC8R23v9YQAll0c5JutwYCN8bhrh-puDQ5vIUbXdenlo-MC6bmdrlXh6COuUYKd-ywhyT7v6rA8HyyB3qZTy9zCkS1ZtLSxLNOK9jc9y74S3vco27Y8lxestwCNLQ5SU8vnleoVAdKDz4loOJgq_yRG_1l_C5k0K6egJoWVOdq_ygtNxnN0TfFtaD5qhz4W_rFe05WX9sAnRu7fvzOWOFkerA2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
💥
بساط ممد مورایس برای تولد ۲۹ سالگی شیدا مقصودلو همسر ایرانی‌ش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105079" target="_blank">📅 13:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105078">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e0dee25f.mp4?token=vPSQDODAmLXWY8nJvkvreVksInJPok74gdN8tWqGKuNdJ3rjINCk8kqO6Tjv67vqJILKfyii8o0u8p_J0-lbAIy6lCtPsxP4csvFsUyneM6pnE2LGksHzcxCwIQdSREqOX-gWs5TqVDlY65V9L6JyN_uzlcl3mex-7PSbdDw2J8A0hKf7OrbdC_aTzJGRmccgxAYUklu20BDoA4MkF4GM-GiVFsTs-REViQroOKUR3GWxAAdK5HlPBMMdRJ39ZMBW8OQQCGRbKQydJ5JGwffOJmhxCZ0xcCZBLajuVklqGlsiYBFIJr0olEC7A6piq1Znh5U-AOvIorX36sv60yhXjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e0dee25f.mp4?token=vPSQDODAmLXWY8nJvkvreVksInJPok74gdN8tWqGKuNdJ3rjINCk8kqO6Tjv67vqJILKfyii8o0u8p_J0-lbAIy6lCtPsxP4csvFsUyneM6pnE2LGksHzcxCwIQdSREqOX-gWs5TqVDlY65V9L6JyN_uzlcl3mex-7PSbdDw2J8A0hKf7OrbdC_aTzJGRmccgxAYUklu20BDoA4MkF4GM-GiVFsTs-REViQroOKUR3GWxAAdK5HlPBMMdRJ39ZMBW8OQQCGRbKQydJ5JGwffOJmhxCZ0xcCZBLajuVklqGlsiYBFIJr0olEC7A6piq1Znh5U-AOvIorX36sv60yhXjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
🇮🇷
امین کریمیان معاون فرهنگی و ارتباطات باشگاه سپاهان: اگر در دربی به امکانات نقش‌جهان آسیب برسد، از استقلال و پرسپولیس غرامت میگیریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105078" target="_blank">📅 12:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105077">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180؛ کوپال‌ناظمی از سوی کمیته داوران شانس اصلی قضاوت در دربی روز چهارشنبه معرفی شده و قرار است تا روز دوشنبه تصمیم‌گیری نهایی صورت بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105077" target="_blank">📅 12:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105076">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3d5a56b7.mp4?token=WZ0eL2R3glKl8a2mkF6iGUOz38-9whI5sclqQLHoPJevDEhKpDWTVqgiC0YNO8_Pnw0zeD0BqgHWHAbIFF_ebpdDxNr6TudH6pDW22rJD8u0TwuUbSyl36ImfHN6Gq7azcxLE7KWSAwc_0q47cREopumA0x4b1wCYI-yjLtO9XJsVxy4azp1kJb9hXOR-i1TeBZxu4EAmbKtokdLAJ-inSCb5o0Efu8sjar8wmjtqE7a_Wdu8xIxUXzBfpOIk1alUhxPH14k-L_qpQ5jF0VdKJ8goxsyT2CznkzJLKElrtSOjwd2jnvzNDAlYR99iyYXqH1TtYgtCTQp4LNJlSlVow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3d5a56b7.mp4?token=WZ0eL2R3glKl8a2mkF6iGUOz38-9whI5sclqQLHoPJevDEhKpDWTVqgiC0YNO8_Pnw0zeD0BqgHWHAbIFF_ebpdDxNr6TudH6pDW22rJD8u0TwuUbSyl36ImfHN6Gq7azcxLE7KWSAwc_0q47cREopumA0x4b1wCYI-yjLtO9XJsVxy4azp1kJb9hXOR-i1TeBZxu4EAmbKtokdLAJ-inSCb5o0Efu8sjar8wmjtqE7a_Wdu8xIxUXzBfpOIk1alUhxPH14k-L_qpQ5jF0VdKJ8goxsyT2CznkzJLKElrtSOjwd2jnvzNDAlYR99iyYXqH1TtYgtCTQp4LNJlSlVow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پروژه تبلیغاتی فوق‌کسشر و خطرناک روز گذشته در آفریقای جنوبی که نزدیک بود دوتا هواپیما به سقف ورزشگاهی برخورد کنن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105076" target="_blank">📅 12:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105075">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d58cb930.mp4?token=qx5PKs4paR3Q9oGAnI1C_Bw0RiWwqWPvAdeym7vP00NWAgclOdzLjEerg8GB5_Cm2vFRJxbkUoMatHzbsFClTzvWayjxgfXDt7wuewfNkUW2Ko0UDFhC05mFdMo3ZKfB6C1dooSvj6i-CoXrYSifBRNVG-IDUKbtLdMbTujN60887CwUV0w7pPzQfYqPLa8HKJuHeOF-P8GRNjYTzNKSxuzR6YSN0Y--UXsN4Fx_-XyQEKXucHanpv3HCRvWo-L1OgVg8fobIV5ilCWM2AGYuCED-YnO_Sl3iGw1bqKIAhxu97WRVa_5Z9qBXGul5zNRskpiY3RWIw-sxWDM-dCSjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d58cb930.mp4?token=qx5PKs4paR3Q9oGAnI1C_Bw0RiWwqWPvAdeym7vP00NWAgclOdzLjEerg8GB5_Cm2vFRJxbkUoMatHzbsFClTzvWayjxgfXDt7wuewfNkUW2Ko0UDFhC05mFdMo3ZKfB6C1dooSvj6i-CoXrYSifBRNVG-IDUKbtLdMbTujN60887CwUV0w7pPzQfYqPLa8HKJuHeOF-P8GRNjYTzNKSxuzR6YSN0Y--UXsN4Fx_-XyQEKXucHanpv3HCRvWo-L1OgVg8fobIV5ilCWM2AGYuCED-YnO_Sl3iGw1bqKIAhxu97WRVa_5Z9qBXGul5zNRskpiY3RWIw-sxWDM-dCSjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🔴
یه خانم مُسِن پرسپولیسی : من پرسپولیسی ام الان 55 سالمه و از شش سالگی فوتبال نگاه کردم یعنی کم کمش 49 ساله که پرسپولیسی‌ام
‼️
🇮🇷
دختر کناریش که استقلالیه: خاله تا حالا قهرمانی آسیا هم دیدی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105075" target="_blank">📅 11:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105074">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrWlOcT4xm52_eZfFsWIwz99h3eh3Kmkcatb1r1Z15qKP8qQsiR1FbOBLOkmAgoFdN-jT7bY-SH_IPv4-ZfHQyY2z-KbWr5yoLsdKrXzXf6a_-TV5KlPl4226XsWEkDRyfgxnTyMXaCATfwPr2E81LjjbtCur4S4Iyse6L3cfMC_OPPKsw27KP3jsA8TwAlBPTwXsGwRZKjquqkVUGWkAXV2wxIj2QNpzyaUavIdXN-krFEW4S-19R2Ghd4oG3U5uLo_31u-WzNUvjcX3rv1YI0vKafbg0z69k0ZfR6Sgm3Tn4_mbkN9Ic9dnY77GXMqzpNsaDqh8uYPp-gtldXYlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
سنگ‌بازی دیشب هوادارای استقلال و فولاد حین خروج از ورزشگاه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105074" target="_blank">📅 11:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105073">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105073" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105073" target="_blank">📅 11:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105072">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxRxRubxiMSQmQNBwDz6GLQ38o4j8TKtY-dNJ5KCAA2kVU3QUfurDmfzvYH_KcYSGO5A6eChV1nyeUxawI14a_qQFAyFbtlERkrqLQrB1_tbB55EX22Pk1MAZNsReJ-QQ7YCNPOYRt6kWwA3wrWGd7-MbVPiOxgnIV5hADKtbzBddDLUtSMayz8vRJS-B8FdhtdHPLu7UxuT8xG1dFNd5GB4XY0vMPNE15tw2HpcUr9g2xbW3ZrvnfSvrbHyQZOYJO4aqGa7ptP3SLO_85CWoNHTaziVK6tuHdo0CE4dO1JhsF_NNEwmriQflzOY_5NDd_muLybEmwfahrV34f24nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN
.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105072" target="_blank">📅 11:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105071">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9q7MOm1xdzG1BHuloJl06UGFooE-ZStq7ebsARPd0AZ-jXvYvztG2lOEPCxZzdBK44HHLT0ugQOqhI9hVSLf8VBBU1kb9tYB6cHr3oYxPcqjZGuejGxVzKy_oqquoRrfdFRcbUyV-0A4QAs9_Ft2bGll1s41sxQTxtP1PnXJAHDZATtfIexEXZrgeukDavnD_XQG7HL4s6NEYL5MnsMhrkXmDHe6IEc8Ws_sPFYHH1t3X04irJ4RAdb0sRWy_QXzOQE7BJXl7UKQRRIAg9s9XPg9JNnmFLoa7SPk1xFSCwPyYrpncf1Fzz0FUxAuLStxbS2OIVuD9_LYheUea0VkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
#رسمییییی
؛ املیانو مارتینز سنگربان تیم‌ملی آرژانتین با قراردادی دوساله به چلسی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105071" target="_blank">📅 11:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105070">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3poZvT-bU5MiS4NpIQ4W1bu3fbY4LOgoQSDdX23uPTF6SOCt24KIF9chgvOz9pgMqqzX4d4Xiiapjg5eEPCjGeRUe1GE39fji2J95UJ07oBLhey3fANuFsRwimSX8LDQoueDLG_mHZYWs7vu0MYud8oXQjLKYaey7_x0qo_c-v6BehPu5PDv4i91Nkry_geseYBgXxncS1QAeZCgWFYLBUgdBFnCxw-7Ux7u73dwcMMnbxYtDTSYRHEc0Lu_iayTWJec8G3OASbPeJ00Lw1OQU4-bACORv_Z19q6zXu809U6RPnzelno_gKoc3iu64WSUS22PQhrxXgDDe-YZiLuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
👀
🇪🇸
🇦🇿
بارسلونا در آخرین بازی لیگ‌قهرمانان خودش باید مسافت بیش از ۴ هزار کیلومتری برای سفر به آذربایجان طی کنه. چیزی حدود ۵ ساعت پرواز!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105070" target="_blank">📅 11:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105069">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad71709b9e.mp4?token=R3w0UexCD2DVtTCdFRIGGngCyuxK0HezpaDwZbbEQPtAoryOQ6pZyUtYb27O--T8zrwHZZ2dlPKL1NFLehIWinmsgcg0z9tnnHc8hdQ9TfRMxqe99D0F6En0LjvEj6lXPhjK1d1g3Dq_Ah0dCfyYNt92zuwdn4aU-SNhcpg9WmN9NmeUkWHFH8QTyzByPl49qif53fhJuRZdvoUH0hzPEOxxBzJ0YCvysiu0uBuMSPMIL-jarn9d7RCewXHakDlZN5owYlirsZMJkStsE1pKWMjaayoPDtL0fD88XHMytBBgKmlOx0NULNWBaDecLYmCYNgKHHyZYVfBptxx90f8ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad71709b9e.mp4?token=R3w0UexCD2DVtTCdFRIGGngCyuxK0HezpaDwZbbEQPtAoryOQ6pZyUtYb27O--T8zrwHZZ2dlPKL1NFLehIWinmsgcg0z9tnnHc8hdQ9TfRMxqe99D0F6En0LjvEj6lXPhjK1d1g3Dq_Ah0dCfyYNt92zuwdn4aU-SNhcpg9WmN9NmeUkWHFH8QTyzByPl49qif53fhJuRZdvoUH0hzPEOxxBzJ0YCvysiu0uBuMSPMIL-jarn9d7RCewXHakDlZN5owYlirsZMJkStsE1pKWMjaayoPDtL0fD88XHMytBBgKmlOx0NULNWBaDecLYmCYNgKHHyZYVfBptxx90f8ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
🇮🇷
دیشب خدا دوستان‌فانتزی‌باز لیگ‌برتر رو خیلی دوست داشت که کیری بازی این جیمی‌جامپ عزیز باعث گل‌خوردن پیام‌نیازمند نشد
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105069" target="_blank">📅 11:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105068">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeeb0876ab.mp4?token=Ig7HcqgJQQ2zQQ0dCDeMH8riFXqczMYwhHgxTxOlC35hfz70zkFyTLrl7-H1_zTJAhZEGvrN6C9pnk57J9RYMFNYwwZfYrkmDlPNAHAYBOSPqfI7CrDf1c4_VtDgA-MBx6N0yKaVan5x7oGB2usHySdO4w8cd6RHnsA84C_kivIJH4v2nXGyuADlVLJ0A1q21e24Lr2p7qMjIr00NXqEO2s4cRAIjaIbFwtc4V1a1v16HwGCadj-x-Vka0MrboXVqVW8iydAXb3966j5KBwPAOsFQH8hKDUm3-htrusrgoUqKYg9lJ75JnX_YgJO0PJZTpbltI6oR0d5ex05YuVePA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeeb0876ab.mp4?token=Ig7HcqgJQQ2zQQ0dCDeMH8riFXqczMYwhHgxTxOlC35hfz70zkFyTLrl7-H1_zTJAhZEGvrN6C9pnk57J9RYMFNYwwZfYrkmDlPNAHAYBOSPqfI7CrDf1c4_VtDgA-MBx6N0yKaVan5x7oGB2usHySdO4w8cd6RHnsA84C_kivIJH4v2nXGyuADlVLJ0A1q21e24Lr2p7qMjIr00NXqEO2s4cRAIjaIbFwtc4V1a1v16HwGCadj-x-Vka0MrboXVqVW8iydAXb3966j5KBwPAOsFQH8hKDUm3-htrusrgoUqKYg9lJ75JnX_YgJO0PJZTpbltI6oR0d5ex05YuVePA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
این یوتیوبر استرالیایی میره سراغ مردم عادی و بهشون پیشنهاد میده در ازای ۲۰۰ دلار براش غذا بپزن. دیروز اتفاقی میره سراغ یک خانم ایرانی که قبول می‌کنه و ادامه ماجرا ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105068" target="_blank">📅 11:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105067">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a3fe4297a.mp4?token=G2X6kqNMmjAk5E3fey-PKmb_T9RLgRnzaimFBxCjbpM-F6UzHoDuUtDWbAq_H-RfYgGfo0igyKNOq6OeCfwIAvKjdNpXbFqpUQK6xeeWPqqVXcfKuZXELK7f-knPFhibq1RVqgPMWgwAlywOr_5fd-CZVjg4NS-kloC0tiE62QFpPG_KNDIf3yTXIQT9RhxSn5COkqANhdmK0H39BBc6AmMYxsqcIhcrSIY-t42aus3VM_AMPbsibnw9zrCau84va1ylaNwzfLsEdev0Bc7P8TTJWmAmjHBJbQ56SfUxb0poArV1YenHWqZrNla4R3OIgTrY03Qh70wS9y5pDfrZdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a3fe4297a.mp4?token=G2X6kqNMmjAk5E3fey-PKmb_T9RLgRnzaimFBxCjbpM-F6UzHoDuUtDWbAq_H-RfYgGfo0igyKNOq6OeCfwIAvKjdNpXbFqpUQK6xeeWPqqVXcfKuZXELK7f-knPFhibq1RVqgPMWgwAlywOr_5fd-CZVjg4NS-kloC0tiE62QFpPG_KNDIf3yTXIQT9RhxSn5COkqANhdmK0H39BBc6AmMYxsqcIhcrSIY-t42aus3VM_AMPbsibnw9zrCau84va1ylaNwzfLsEdev0Bc7P8TTJWmAmjHBJbQ56SfUxb0poArV1YenHWqZrNla4R3OIgTrY03Qh70wS9y5pDfrZdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
پست سمی تیم‌ذلیل آلاوس که بعد سه هفته و با یه بازی بیشتر صدرنشین لالیگا شده
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105067" target="_blank">📅 10:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105066">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghovOP4QhDnTazQ3PQ-X-0kJ3_UV6oLLnVEyhRRk1cElDygJC_Gd_VbfIS4M4ihi_drMW9twRjrcKq4sIqlPIDHIyUleJ7DFWH53Wkj7xpUZJD9tvuEZ1uPXFuBzR2dj-uAPuGpEP9bIOoPOyDB2BO7k0UNWx3WGz0zCjAWwGTpdKHnvgPcRl_9KJWvYd0xp5NnCndLUvYqaiPN7QzmGy4joDfY2S2SvH7O6V5OgAiHAPy-U_tlTgNFmg6jd9VqWvKfHIO9K2V5RyVbmnWpkplG3MEW_qb8JboeRd35sxCd46OgkiuH5J5hWIS0KWgtCa8tP5jgdKHD8pAgyt_Qoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🇮🇷
هوادار فجرسپاسی در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105066" target="_blank">📅 10:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105065">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c6851cddf.mp4?token=bXETxVCkkAb0zO8pPYZyT_V86Qjq24eDUiu0OR27vxKrCXoWbsxmP_7C_Qv3yoTT_N-H3-K2yBYFM2UpmhHleCecCjAVqDyDyW3Hx8iWlwHa6_FglgmaPoPlj5H4GK9ML1qd2DMPSm6j_sXjRSFDPjuJz7vfSjx05WLR0qNSuDnD6EvQylR3HQCXVwJekULEob-ztaKPKmLzZsy5FzmLyG40bKqvyXzXApXlRIx7gFJW5JyBMtF7sz2P_kt1H9TUJu-k4Qti7D_Pr0O39K04vVid-d-DALnq81JGlIqHGxzKcAM4vdB4Qs7GZt-dM6nE3SBl-BnUfffdyNExPLPLJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c6851cddf.mp4?token=bXETxVCkkAb0zO8pPYZyT_V86Qjq24eDUiu0OR27vxKrCXoWbsxmP_7C_Qv3yoTT_N-H3-K2yBYFM2UpmhHleCecCjAVqDyDyW3Hx8iWlwHa6_FglgmaPoPlj5H4GK9ML1qd2DMPSm6j_sXjRSFDPjuJz7vfSjx05WLR0qNSuDnD6EvQylR3HQCXVwJekULEob-ztaKPKmLzZsy5FzmLyG40bKqvyXzXApXlRIx7gFJW5JyBMtF7sz2P_kt1H9TUJu-k4Qti7D_Pr0O39K04vVid-d-DALnq81JGlIqHGxzKcAM4vdB4Qs7GZt-dM6nE3SBl-BnUfffdyNExPLPLJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚑
❌
🇮🇷
یک‌سایت خبری روزگذشته مدعی شده که مهدی‌ترابی در بازی با چادرملو دچار پارگی رباط صلیبی شده و فصل رو از دست داده! باید منتظر تایید یا تکذیب این خبر باشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105065" target="_blank">📅 10:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105064">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac5342ab00.mp4?token=nKRiryET_vHLPnoXuy6s8oDSrjQ_ewmRJRk8cBYTFkCfvSt3CI2-cBUijnds5gmD1LA1u9HLswnTnPogn1yUansJYFd2k7gp6XD-liwcpxrXJ-ASAoCGfmHM0Az7L56ve-JREO2b4KMu60InzlvAK4E771Hy2RX9KZ3UQ3PyxJyT4FYpNcw4R0tgAfyf4RMoU21MNYLhyGfUa3dhsTPuAGft3Oz5FIZaG-aoITr0gFCSL80JA7Ul-4v39xA5HWvuXuu-0ZuYsGjf8Pq01LpbU-QlQx0NGsdAuNHoXeA2nU-TaGZz-iTZDN18Rla3tXVjM0bl_DndChKP9XkGRbpoqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac5342ab00.mp4?token=nKRiryET_vHLPnoXuy6s8oDSrjQ_ewmRJRk8cBYTFkCfvSt3CI2-cBUijnds5gmD1LA1u9HLswnTnPogn1yUansJYFd2k7gp6XD-liwcpxrXJ-ASAoCGfmHM0Az7L56ve-JREO2b4KMu60InzlvAK4E771Hy2RX9KZ3UQ3PyxJyT4FYpNcw4R0tgAfyf4RMoU21MNYLhyGfUa3dhsTPuAGft3Oz5FIZaG-aoITr0gFCSL80JA7Ul-4v39xA5HWvuXuu-0ZuYsGjf8Pq01LpbU-QlQx0NGsdAuNHoXeA2nU-TaGZz-iTZDN18Rla3tXVjM0bl_DndChKP9XkGRbpoqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
فرونشست فوق‌کیری دیروز در اصفهان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105064" target="_blank">📅 09:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105063">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/891ec9c375.mp4?token=f-Kv5EgCaTL6iy_CWun_k00YcvQH0Kivxqft4Lb5qojeYv-pzwP9wmLjSzYIqtf3kPJeJqMxiTtGDKfBwQ8-BDCbmo0g1-zDuU32SscC4hi096nEDXMw2JlrYbCPWOcKYWqqCVY6IsPAKt4l9l7LDPoL80c58xkZeQ_VDsNmfKM2smFV4wqbnS-OAxWliQUYhL7d3mKohiMnCwTqTYEtc7in7UNJAO0nixsFerTWPCKdalL87uhw2yo7U0qDwwbrwascWGb54_zAEyIPHc2RGfJSHJAWWhlxvAoESD48lyUElORS1UCKQqRM_7ZaCSDVpQXafbUPnrbzo6fRFX8iZoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/891ec9c375.mp4?token=f-Kv5EgCaTL6iy_CWun_k00YcvQH0Kivxqft4Lb5qojeYv-pzwP9wmLjSzYIqtf3kPJeJqMxiTtGDKfBwQ8-BDCbmo0g1-zDuU32SscC4hi096nEDXMw2JlrYbCPWOcKYWqqCVY6IsPAKt4l9l7LDPoL80c58xkZeQ_VDsNmfKM2smFV4wqbnS-OAxWliQUYhL7d3mKohiMnCwTqTYEtc7in7UNJAO0nixsFerTWPCKdalL87uhw2yo7U0qDwwbrwascWGb54_zAEyIPHc2RGfJSHJAWWhlxvAoESD48lyUElORS1UCKQqRM_7ZaCSDVpQXafbUPnrbzo6fRFX8iZoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇹🇷
ویدیو جدید از استقبال پشم‌ریزون رافائل لیائو در قلب ترکیه و توسط گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105063" target="_blank">📅 09:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105059">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pYK5OAUpRqZG1Dxs9VDCt17YnYYdW2C0zZ8mU2RcJ6bG-iU8tNYKbeH0vjWaeX4S4mO1vZZrYIgArwCI0rtP9PunLirUXQeYSLYG4uAQ20_WHOLeCNp7GIKXXrM4UCDQycB3i1U2EcCJSggCqOT-385AyMfbwpoughc3aw_m5EKj8eSxpCLVe9ly6HvVMNl9EdmApMHjlgG0vX4Wb79IwzRvzQPDCIjiG5ByOtNNd0EpJJsUnYnQL3--nwJqyZ3U6JgpjKh2sN63Z1MSIMGUa12eZbh7bq01lj2IjsjAUGZkY99jd4nhiOYWJhASGiL1m3VKZ8lAW3rpaVDqKERmuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Db_OEw9CysrvTKU8Z0EyFwHsuy6xfDwXtu3ekL4ET9IhmTx0CV7uqv8WYQbylDROF7LaoZ7diQJPRLK1GNfPbP2LaDLxT1-VXhxC6JF-Lu7QhYtgZjOFMWtvUVoUZ8sYmAm7mfEgvuKQUVNEe4JA3QApIVd2uot6qg9lgsGXhsJToTCWYIucIhOkE4Yhr68TkRol9QBK_xAAmhqXnbvir4vk4tEChg3rKTnkx9qjiaVs--dAtWV1fqlbEL__aEI-kfw-2y_wZRI4HDLbIUYX4soF2iEFWZypl0NQFI-1dBdPHmuzWJje9vM9sXFTLG5R4mSKKtTjH2iG5jcp65hJtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZmkcfs3ySwIDo_Z6_xNGX97RW_C2uVdEG3yVAbhCfSjJlheGvPXK239yfnnZ6vE1_L9a4tULAv5UU0K7jRXgBAiIIF5KNUhXid_cp22sAoe3K9lgpCWENAzzDSU4WyGbltTKcHn1SNRc8WVDXt9NSGX6C7kpKmrZeZLQ0moUIKouUq8g7hsIz15VawaknJRYhINV4KMUdmoxiHLFkeWNCv4-kNzf54FP7UnkaQXAbATjLEc3Dvir1M05XGQxgiTGm1vONYV95t2kZA6i1dq3cQRkr41L3TIzfwU6TcVh5pWI0N3EZCNyUkHmG9VUZVUNSN4RS2D_agIph40KeTy4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QI-Aptsen9XBO4Hf22wlb5QF4f_96PChEP8VYlNyRtvQXFSkm30TojomgKkaVNyJB5HmAt6W4AuVuwCtqpva2CQj6r0sL5N4hCv7l_StMHK8UECLP3qA0gaXU8YzbizFjQyR3FZyuHstiBH6bnj0wDqhRcaeJGDjIw7cMF15FyWu4CkrpMCHNzWfr6CnuKLoKpw4mqSGn0oZTzDBfCN7Im3JAlJd18E_N-5igiraxMV_z_Q3k1JGNUPidAVYTXayDelr-Y4_N6lek98F5aOj1TH3qoOMcuD1MUPPE445SCwbKteCKNkLn3RMiw313EQ5gJfwxirPmWTc4EUUYSqGOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇮🇷
بانوان جذاب پرسپولیس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105059" target="_blank">📅 09:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105058">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1503ea5fd.mp4?token=cuFP8fG9l82QKXQks54rUiLXP25DuI8omnZMYuA8va6bcq5Jr2bLBvS36rhTojYQuE3Owrzl3KmRFz_79k3uU5-eaTfEV3LS8dwnAWnB_O7hnmblfT5OkC8l_Nm38frvuK0yu1-YTmgqP8Ir63r1v_EQwAbYqsfHuZE9-zUMHqaEuU-j6zGDL5_iyuCCgk8lpPAlTLc1-H4ijCtyu3jwOH18kTmZ7qT2aP4z8syGCOYcN4SgJVR4TYS3vEdrVyGWVBYItVy_MCUCRp_-vCDYNgHVSO6_FrA0hR0N7x1bpWy-e_tOQpRrhiSBFknCZnEgOhlzxRHVXssk2GMQ4hsf2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1503ea5fd.mp4?token=cuFP8fG9l82QKXQks54rUiLXP25DuI8omnZMYuA8va6bcq5Jr2bLBvS36rhTojYQuE3Owrzl3KmRFz_79k3uU5-eaTfEV3LS8dwnAWnB_O7hnmblfT5OkC8l_Nm38frvuK0yu1-YTmgqP8Ir63r1v_EQwAbYqsfHuZE9-zUMHqaEuU-j6zGDL5_iyuCCgk8lpPAlTLc1-H4ijCtyu3jwOH18kTmZ7qT2aP4z8syGCOYcN4SgJVR4TYS3vEdrVyGWVBYItVy_MCUCRp_-vCDYNgHVSO6_FrA0hR0N7x1bpWy-e_tOQpRrhiSBFknCZnEgOhlzxRHVXssk2GMQ4hsf2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🟣
در جریان پیروزی 1_7 اینتر میامی مقابل مونترال، لیونل مسی موفق شد چهار بار گلزنی کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105058" target="_blank">📅 08:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105057">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFlh9sLBj7QyisgzlvIyrZvGhsjYma89L9qW-9nmUxHDpvEb0_LxRvuvgJEjvZLJPkVtrxvCoQbSvsKwyUzEyoZLqvohfatYIuG0pQMvFtnAhAAOdagzRwVXM4lmaPrOGW6hKM6R3Fi_UVO3768e5DrrHBB9F4tZyiFCX37PICm0wfp04wGtSIHGwaaR3wZ6xDvQ6rlckiKN2Tk-UgypXFGSijnmrq-SNLO1wdiLkomC-71hW-dcEj9KnHS70wM1eSeXA1HGD5WA4aORis6oIve7--3HXEGdzFM0VqW51yCH-eJ0Yof27rNgJ1VTfebJMwQfYI0FkEJuH5YUtYsl0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/105057" target="_blank">📅 01:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105056">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/105056" target="_blank">📅 01:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105055">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAnQ6sD1v5ZG39Uy5TwMSglBcMRTMwUrW6lDjCHQvU9n3TnKvROAxKzCx2h5gDdbLyZcOo2uzfUEhnN7OHAmrJWfOB6UtJhFTAorFjX8MUtwZqcMfJUrG_Jd9qvE6YeSmcIsXzFsfKwwIzcGcNYvHk6aYf2cnLWCZ2Wh54mNzCDf35iPeydV7ZkHR8I7NaMzHyZ4Mo3KfuwF4IzLNDZ5EO8VqlPf5XsrYsMbOFRXmYmBqJ9ECLVRKpGiy6hpFWRFoaXCGLR00YaeNvh2DffdxoVwBSBDWep6F29U8VXa3N4rACWmzEipsvR7oU9qbK-9_GXDuntjxJ8XFHnpiATVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🇪🇸
متئو مورتو: اینتر تا این لحظه با جدایی دی‌مارکو به مقصد بارسلونا موافقت نکرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/105055" target="_blank">📅 01:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105054">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfKZpjZ4EJhW41E60uBGc0mLWG5Sll0fWtEQLtGibHoGpJ8dxktcrnUOsq62EVOVZcI3xfsyjyJVQqT5E9e9b5Kj4MNT654BN7vdSgfdAGcayGELjhZScC_OVhnDJrsNNVAgRqvXarWzUnUstTw8QoB54Z8OiQgQG01xSYUGga8A40OEBbsw2qZZgPlweEJoiDGlNIu1cMysPsKnrZZvrJwxZtpu8XsvzUKIm6zhzssssIVrfqaRW6wmfrYfcXeYrfq0_iBBOWDBVwPkf6RMiiDV6f8f_1-UqJb21IHXFL7fFVChzKl3xR6iLLHDoPm7gmChZV1usUOYZHVshX_Lng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
سردار آزمون با انتشار یک استوری به صورت غیرمستقیم از دعوت شدن به تیم‌ملی برای فیفادی خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/105054" target="_blank">📅 01:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105053">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGG77-lT7hA417ScbPQBRNXlUG_0WHqi7upFHQ-AIUpWDNhrkRp-ojUpjlXrJJubezu47xYJORqgnx_8YubrLWkuvLnLiS-LDG_p0l6U0rMC4yFheGlkfXdWG8ku782-_m4OXTaS-7ZntlfY4qTXl_uvWGSfsCJ1UtVTrGy9G4XDu8RPCw55wdcg9Bf4UGRwIgVXyfg7bKV32cIUtgeq9aa0gMo46dqdRsFZDNm1Dp6DtRA-GJd5bxi9Jo50Bx5rFnMJ_oC3JFsba3fxI9TR8Emyrkd9iySO5xfZnx1plOwvgGjtH1CFjGjiH8fwT89VKH7CV-jAKoAgnjXey1Y7Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سرجی کاپدویا :
🔻
🇪🇸
🇮🇹
بارسلونا و اینتر چند روزه که روی یک معاوضه احتمالی بین «بالده و دی‌مارکو» کار می‌کنن.
‼️
این انتقال بسیار پیچیده‌س و اینتر فعلا چراغ سبزی برای انجام آن نشان نداده. بالده هنوز حتی یک دقیقه هم در لالیگا بازی نکرده و بارسلونا به دنبال…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/105053" target="_blank">📅 00:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105052">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Re2acytrD2PnzPf2SN8un4nG1zzJOStLixVXDieC1VOxF-JT7e_mUd9GK8a4v5bQjVQO3dlorGN-SUSyn0WBGXS-nMkxCsJwF9VgNk3aIncGtDgWnFjCLcTvsK7_eVSqhUpERhLnPclaXwwA_8yB2D6MIoioKccGO78zbnSltbrDmx0aWXA9y1XDe1Ff7n8idE7V1ql-8rCUH-UTM8yZsF_lGRiK5kcaUy6G0JRqD2c8Pi3rOiXgGw1iDUNnuW-3tTw0XX7NpGABt3GbbpeI0OiZ1b6vA9_uR6Mdwj_UCWExekZ4D-L75wNwpuq8y5FfAOuiEdCLGlkrsNDbWs14eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
#اختصاصی_فوتبال‌180؛
❌
باشگاه استقلال با ارسال نامه‌ای به فدراسیون فوتبال اعلام کرد که تا پیش از بازی السد هیچ‌یک از سه بازیکن خود یعنی سحرخیزان، قلی‌زاده و رزاقی‌نیا را به تیم‌ملی امید نخواهد داد!
‼️
این درحالیست که بازیکنان دعوت‌شده باید تا فرداشب…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/105052" target="_blank">📅 00:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105051">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAzDAKSB18QY9u2IvZS5MQVszHTz9Gi7Oe7qnv9Jx_NcIJtDukJzX9ZXw1sKFbTKM4oToig5Q2cHw9Dfvpo6NMynL1pAGtobRDX2e1zUhtWxTYnYBuMcQzE3UU6s7z0OpjzRwiGZxjND_saobfGw1vXUJ7Z_4_Jn-vkvVNPZcZTYlZL-yKZzFz0Fiu2nSssnWVgWyNTiiqnH9ApvMbkF2QcMpm7RXs1yD1a2_s_e9KCVOvDLf4j4X5Z6Vc9vUihbQrNz5OZjji0akX-pXEX4OpS2Y0KumXT1roedHQs4TCPRHrGV30TB-KUu587GeoVUH6Y4WvScO40pEtcKJmxHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از نشریه تایمز: منچسترسیتی تقریبا با لیورپول برای جذب کودی گاکپو به توافق نهایی رسیده و احتمالا امشب یا فردا خبر رسمی منتشر میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/105051" target="_blank">📅 00:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105050">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LK-Z7mQF4oNjopkNx8uwQCn0qQuKg7i_OEm84-_QBpbPJ4nd9mCLgzx4WHWMrPDXsGpEtdwy3sDLZiDQYZpb4qamHXjgUaQw4wqA7zEwo_O9WeuD2IU_IwROurCwKUdsAeqbAS3ql7STGiMnlTZ5mBNQTvIBLgrjxXgj4DHITjfiLvBRNHFE79XV0C1Bn-yKo1SKoYs7a5ANHYNIWHDyJBJSQwQnV8ALxl-eJMU0nJLtwXqu8mvq8tgXY_34NYTtD5ajUrWbKqmXdrxAkEhEaN1lfEgRae3y--vNb_vpndDNvFRnRyDEJGI_u_QlxOZZjCBZv0uYB-v16JwW1oExqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سرجی کاپدویا :
🔻
🇪🇸
🇮🇹
بارسلونا و اینتر چند روزه که روی یک معاوضه احتمالی بین «بالده و دی‌مارکو» کار می‌کنن.
‼️
این انتقال بسیار پیچیده‌س و اینتر فعلا چراغ سبزی برای انجام آن نشان نداده. بالده هنوز حتی یک دقیقه هم در لالیگا بازی نکرده و بارسلونا به دنبال راهی برای جدایی اوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/105050" target="_blank">📅 23:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105049">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22168159c1.mp4?token=L76Mi40fAGzolPty1VPBxF0w5D-WHOGeMVFqex7SWqdVgCSA_EE-1oJL2qmHRfaI5Ov0aDxFMQ93IdBlEdNmm4ILsWBDYQwAVKmlSI21bY8V8ONhLCylYtbYbUg_vzmzfpf4fn0g-FaPschYEtFgM1A15AKlbzNxK1Rk-vSV155aJXx1x3pSF39-xvw-8IlgHPSTiKTXqNN5EzKCM8Zpnjh_M7op_Qs0YrF2lWEOvPu2DfJLGz71kWrupHgjDFNi0jp-1oAjEWvU8e5ZSch_TFlJjluNEjC0-DZQuhCQ7ne52B06OvB35cGvgs4bZL3xhRYzO5zZ46wk9r6Y7Hu8pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22168159c1.mp4?token=L76Mi40fAGzolPty1VPBxF0w5D-WHOGeMVFqex7SWqdVgCSA_EE-1oJL2qmHRfaI5Ov0aDxFMQ93IdBlEdNmm4ILsWBDYQwAVKmlSI21bY8V8ONhLCylYtbYbUg_vzmzfpf4fn0g-FaPschYEtFgM1A15AKlbzNxK1Rk-vSV155aJXx1x3pSF39-xvw-8IlgHPSTiKTXqNN5EzKCM8Zpnjh_M7op_Qs0YrF2lWEOvPu2DfJLGz71kWrupHgjDFNi0jp-1oAjEWvU8e5ZSch_TFlJjluNEjC0-DZQuhCQ7ne52B06OvB35cGvgs4bZL3xhRYzO5zZ46wk9r6Y7Hu8pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🇹🇷
استقبال پشم‌ریزون از رافائل لیائو خرید جدید تیم گالاتاسرای در استانبول!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/105049" target="_blank">📅 23:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105048">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128d699010.mp4?token=VZqOr6NA2a8SWksxJgwc4YzwJCJx7tGv-vP0hmPEAViNuKRlfbDU0TJkIrzseKuJ-_De2W41QecGXdORWbNvxqojSkxKfSbS9BkuH40MBBGsOqzCw-mQ-4Lz52atjgMX_Mg1auXzK-TWxNkgq15wHsvRJ-ZrJC_iuizECWWm9FlFtBUcRXaWLrrOTWJ1RWbBuBg_3cN20Wh53fhUHIFwzGhcdwNH4dWDmc0hhcRCH1wXgyEvlEhA2Cteuwt_v1WgsRDu1sQqpBcxpj1ikJZzGJYIlxuGgYyXjqkclxely1LTEoux38SOVx81Tnc3hIDDz_i2JgtnUyO8AB4M2bc9xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128d699010.mp4?token=VZqOr6NA2a8SWksxJgwc4YzwJCJx7tGv-vP0hmPEAViNuKRlfbDU0TJkIrzseKuJ-_De2W41QecGXdORWbNvxqojSkxKfSbS9BkuH40MBBGsOqzCw-mQ-4Lz52atjgMX_Mg1auXzK-TWxNkgq15wHsvRJ-ZrJC_iuizECWWm9FlFtBUcRXaWLrrOTWJ1RWbBuBg_3cN20Wh53fhUHIFwzGhcdwNH4dWDmc0hhcRCH1wXgyEvlEhA2Cteuwt_v1WgsRDu1sQqpBcxpj1ikJZzGJYIlxuGgYyXjqkclxely1LTEoux38SOVx81Tnc3hIDDz_i2JgtnUyO8AB4M2bc9xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
❤️
کریم باقری خطاب به هواداران پرسپولیس: موضوع ارونوف را به کادرفنی واگذار کنید. پرسپولیس بزرگتر از هر بازیکنی است؛ فقط تیم را تشویق کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/105048" target="_blank">📅 22:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105047">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc84af493.mp4?token=eC44xG28lvODl0M4TmA8ncZSYoYtnsVmdtPzYIKOg06zw2qJlq1LQDQH0jQSaYaqhuC0IFMS-7-kAey1DJyB74GnVYrYDW8YEKHpuJTDax2-LpG_RtJCdSjRFCf5MWf3azsiweNjZy_K8vBDCUlQaYGq6vZLvMoKV19_e_oCGOnI8I7CXolN3l2tekF6-QpTHkcjurMb2xsF4HK-9CN9l8WDFkYiDqxM7qK0bBhnd--qHzb6tb1ON79BkQKMuycm3F5dwfqb0IsVX9OZ0Ub8cPX9JjY3_F2K_oCQQfuOBLyvdvHlP-RRfN3ffztmPfSC2FZB62dqgfpG_PnnUxD0Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc84af493.mp4?token=eC44xG28lvODl0M4TmA8ncZSYoYtnsVmdtPzYIKOg06zw2qJlq1LQDQH0jQSaYaqhuC0IFMS-7-kAey1DJyB74GnVYrYDW8YEKHpuJTDax2-LpG_RtJCdSjRFCf5MWf3azsiweNjZy_K8vBDCUlQaYGq6vZLvMoKV19_e_oCGOnI8I7CXolN3l2tekF6-QpTHkcjurMb2xsF4HK-9CN9l8WDFkYiDqxM7qK0bBhnd--qHzb6tb1ON79BkQKMuycm3F5dwfqb0IsVX9OZ0Ub8cPX9JjY3_F2K_oCQQfuOBLyvdvHlP-RRfN3ffztmPfSC2FZB62dqgfpG_PnnUxD0Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❤️
کریم باقری: دعوای بین باشگاه‌ها و تیم امید؟ زور هرکی بیشتر باشد همان می‌شود. اگر قرار است قانون اجرا شود باید لیگ را تعطیل کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/105047" target="_blank">📅 22:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105046">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubXiE2VqZcSg3Ba8Bwi4SXsppitn67o0n5SxCZXgjUPtCKCQ3uqb_0gd6r5sBlLkUL5rolVcftvWmap3BRKfaFuToGmv9FWGXGW1W481zetg3BKyHsn82WDYuJLUsZDnemTkSsNyEiY0xDXZ6im0LaC2k_BABgsVOHGC1bFNo2ptftkXTStj3kkiLS9ym7ovNYdg7jHFWZPrhw4texOo_yaDZGwwZ8EIUJcofZej8lv_p1y1Kw3xwhk6IgWOezOQRnAsnWjc3-uL3ChY8wWRsF3ddkTLpwNJMTvVIWpf4F4NNE082Ca8L_4QwBaoxfQCZ8DBI05yEQTDvHOzPVGegg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
مهدی‌تارتار سرمربی پرسپولیس بدلیل شادی زیاد و افت فشار نتوانست در کنفرانس خبری بعد از بازی با ملوان شرکت کند و کریم‌باقری حضور یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/105046" target="_blank">📅 22:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105045">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e97755c4d.mp4?token=M-r4JuHyjXVyUICsBFOhPNcfOU1KIsKYMh70CLCQJTQdvYri1PThPV5rvmmodZHXYwwbf1JmpI0CErmZoU4LtnlJCtg3AnDiKpzhH3JGYyy5vy-cRoNUTFn0uLXSkfQgDftZzDNsNOXP9mldcqqQ355meRC6bW6fSHDaxqqntN6LttZ3PIoUksXC0ETYOXuI5P505g74Hd6-d071nUG6_2qdilhyzqM1C0D10gh43Eovi5pqrMzC69BPnKLUSxVdubyN14-p7st48u_X01VLgW4-qj10qoeyWbR07oqh1RilBAYAB8n6pe9pOZPNwf1jjf5cCS4k1qaNmBdKtCfR0mTCV_iigZ-BdPMjK88273fzYkgQ-46E6QebGTqeN1UJuj710aIOPiM5_0zfqewPZz015Q28neNvZrqPqnuVU_FVPG1qupLviM1KMXuGHDSmxG55T7ZCQ6psd_IMaQt2od_vrWRCUF2eNhdClQoHZl0NCX3dX29owadyYjDN2TbP_b05h-LZGvmIeTudTeyUPuROgPKEOEVVD2fXeSFqqBkEGkXCF-VBW2usgKk-V5PDYNyOzmkiXSC7O_OGyrQ3OYrphKRk_qj_A4oqlXimmpBIPnWRGsS2oQi7dbR1P2yqRfVonTecxqNOHHJTStGHP-HsAaj3lsM22tuf87vif1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e97755c4d.mp4?token=M-r4JuHyjXVyUICsBFOhPNcfOU1KIsKYMh70CLCQJTQdvYri1PThPV5rvmmodZHXYwwbf1JmpI0CErmZoU4LtnlJCtg3AnDiKpzhH3JGYyy5vy-cRoNUTFn0uLXSkfQgDftZzDNsNOXP9mldcqqQ355meRC6bW6fSHDaxqqntN6LttZ3PIoUksXC0ETYOXuI5P505g74Hd6-d071nUG6_2qdilhyzqM1C0D10gh43Eovi5pqrMzC69BPnKLUSxVdubyN14-p7st48u_X01VLgW4-qj10qoeyWbR07oqh1RilBAYAB8n6pe9pOZPNwf1jjf5cCS4k1qaNmBdKtCfR0mTCV_iigZ-BdPMjK88273fzYkgQ-46E6QebGTqeN1UJuj710aIOPiM5_0zfqewPZz015Q28neNvZrqPqnuVU_FVPG1qupLviM1KMXuGHDSmxG55T7ZCQ6psd_IMaQt2od_vrWRCUF2eNhdClQoHZl0NCX3dX29owadyYjDN2TbP_b05h-LZGvmIeTudTeyUPuROgPKEOEVVD2fXeSFqqBkEGkXCF-VBW2usgKk-V5PDYNyOzmkiXSC7O_OGyrQ3OYrphKRk_qj_A4oqlXimmpBIPnWRGsS2oQi7dbR1P2yqRfVonTecxqNOHHJTStGHP-HsAaj3lsM22tuf87vif1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
تیکدری: دربی 3 امتیاز دارد. فقط به برد در آن بازی فکر می کنیم. تیم ما آنقدر بازیکن دارد که با بازی های کم فاصله فشار زیادی وارد نمی شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/105045" target="_blank">📅 22:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105044">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=N7S_oWvSUAdjvPkOJVGTPMbCrO21m9p7uWZWOofXiyrjrZhT-x37oxswVnDiK_vs914Lfn4ElqVV96K644qYzOQOGWh5t_BiGKstuj-omJO1hgxuWjsM-0Sm3Mr1VT3bmfVLSvmtUl_vg5zPzkQ8z8veYlH1oJiNxbmVgndgvcm96jhPBDFXXsl3-r23n92X0jr8ByE7WTWzAuKAkykDu4E4KZRger8XXSGx2MBgMB04fNg67PNXwa7AGmt0zLcLSGKLQNLwIpiAEPuM3JLN8ekzXZD3aP_ZqJRFC9q5E6gt8NeMmXqVRZZH-xZ_7fFVwPtM4MExhbmD9UHf_XyyjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=N7S_oWvSUAdjvPkOJVGTPMbCrO21m9p7uWZWOofXiyrjrZhT-x37oxswVnDiK_vs914Lfn4ElqVV96K644qYzOQOGWh5t_BiGKstuj-omJO1hgxuWjsM-0Sm3Mr1VT3bmfVLSvmtUl_vg5zPzkQ8z8veYlH1oJiNxbmVgndgvcm96jhPBDFXXsl3-r23n92X0jr8ByE7WTWzAuKAkykDu4E4KZRger8XXSGx2MBgMB04fNg67PNXwa7AGmt0zLcLSGKLQNLwIpiAEPuM3JLN8ekzXZD3aP_ZqJRFC9q5E6gt8NeMmXqVRZZH-xZ_7fFVwPtM4MExhbmD9UHf_XyyjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
کنایه فوق‌العاده شدید مازیار زارع به خبرنگار برنامه فوتبال برتر: دوست ندارم تصویر من را در برنامه تان پخش کنید. شما اینجا باشید من مصاحبه نمی کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/105044" target="_blank">📅 21:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105043">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxKYwAHnnjfUIm2tWD5yY7XfJl-uCpVgfNgu3tNMZ6z8mABea6_g8xVP59GR8xBBNnqjb3gnaxfWwODAJSbyd2EFybWj38sMF64wi_o5zRCjbZWF3CuExbbmGbRRO9c6qqoTiBRYF-yc9NQS1EuunTvMKhU00VGgVvg0vm5tBq4lubIuuXHQckD78QRI0hmJObtejh7aW6Uj83nH6pPN0FcvRbsVk5pZL8yls_zXwCuytX2WXECn-59v3FNaNzgFV9bgngWqSCauToqE4quHFgROkmM1QTc2n2bS-nnF-xMKxQjM6prYqrBoEX-ZzcprfTApGP9gqHg8c1LG8ZBEiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180
؛ کوپال‌ناظمی از سوی کمیته داوران شانس اصلی قضاوت در دربی روز چهارشنبه معرفی شده و قرار است تا روز دوشنبه تصمیم‌گیری نهایی صورت بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/105043" target="_blank">📅 21:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105042">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d2706c562.mp4?token=uY_uwhMWaqfYLNC0n69JEtVGnHBnKV_0p6nF_61GDptRYdBnGG3fhAqmVXcqd-dy3Q5d1FFMLsKVVNVfTbEWhXCGZQFJf6j_Cgz6dzGRy9f-wGrE4a6RnuPETsHBODtd9sjYj7MMBNwAVcsMmAmd_OI-maeRi7BLtftOn6IRal-mCCikXL54bsYit0LZmelOqDEwRhdaJ61Dv3FTs9uJ4N9ShLEVo5LTpbFtPVZ-YxfTSXsYF5gAAEN83b1opD0VAIkXGWNTsaxFlseTn5WlCPC9ZW1wggngleDRxvlGLZll-QN7LRk1mejnIABcxMpGpHXlVesvpwYDiEEu0T6ZEjWJgk_rzVMP8plAG7XrQb-0hCGega8pGKj1va00BJ2bn0sNY_m-5JwZF9HmSXZqlwYsLL2AIAqIktypoIP39DhVMDiTaTNVQe6Xxw84IuZfAEwaMsivlcx4qw8HfZ0bJdvn52yFlvfKIpVP3928fGQXprAiZHoU_PCJ2VkqsSaJsGYlzh5f2z753oOljqutdsNENFWquVHLZXmQJoKHRz4H810QtvtLfF2PZdyY49Hu3o5TV8LXuAG8jHvDhB_MmiY8ZLn4hqeMPXcwBAMuVmm_MzZn2-uO43o3UnEr4jv5D2pZE2VWnfZmT3V4XGxqPZtBDALtLLzOooYrBqARb9o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d2706c562.mp4?token=uY_uwhMWaqfYLNC0n69JEtVGnHBnKV_0p6nF_61GDptRYdBnGG3fhAqmVXcqd-dy3Q5d1FFMLsKVVNVfTbEWhXCGZQFJf6j_Cgz6dzGRy9f-wGrE4a6RnuPETsHBODtd9sjYj7MMBNwAVcsMmAmd_OI-maeRi7BLtftOn6IRal-mCCikXL54bsYit0LZmelOqDEwRhdaJ61Dv3FTs9uJ4N9ShLEVo5LTpbFtPVZ-YxfTSXsYF5gAAEN83b1opD0VAIkXGWNTsaxFlseTn5WlCPC9ZW1wggngleDRxvlGLZll-QN7LRk1mejnIABcxMpGpHXlVesvpwYDiEEu0T6ZEjWJgk_rzVMP8plAG7XrQb-0hCGega8pGKj1va00BJ2bn0sNY_m-5JwZF9HmSXZqlwYsLL2AIAqIktypoIP39DhVMDiTaTNVQe6Xxw84IuZfAEwaMsivlcx4qw8HfZ0bJdvn52yFlvfKIpVP3928fGQXprAiZHoU_PCJ2VkqsSaJsGYlzh5f2z753oOljqutdsNENFWquVHLZXmQJoKHRz4H810QtvtLfF2PZdyY49Hu3o5TV8LXuAG8jHvDhB_MmiY8ZLn4hqeMPXcwBAMuVmm_MzZn2-uO43o3UnEr4jv5D2pZE2VWnfZmT3V4XGxqPZtBDALtLLzOooYrBqARb9o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
نبود توالت در استادیوم مس‌شهربابک که معضل هواداران این‌تیم شده
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/105042" target="_blank">📅 21:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105041">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e73d84229.mp4?token=M1wxo56Qe-f4fHP7adZnqePrHY05bmLgDvbZptWf0ofv1HHfusVYFkynClB0xL5InoxdN14d3iERkR6QhjFRfrYZyRFL2qSGfohbTd_p47g_m4NyqnG69JOAUCol3D6pP3ShEtyGH9ZRumQDZ56j_uIl6vh8Tf_EalRrIpeUNHzclFevBupMgq5ndtUfXe28FQYq0Leu7_LGaCYgwW8LidWAWzOokuphHl9Mvct90dMfXZi3GIpBrBz7QAdyq7fDGDAT_CHR3XPt0tIkvZRz9_wK8kZnkKI-yxTUr1flBZzbseFgqK0ctpLR82iFVedgjtG9qi8OBxpr53KHVtmWJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e73d84229.mp4?token=M1wxo56Qe-f4fHP7adZnqePrHY05bmLgDvbZptWf0ofv1HHfusVYFkynClB0xL5InoxdN14d3iERkR6QhjFRfrYZyRFL2qSGfohbTd_p47g_m4NyqnG69JOAUCol3D6pP3ShEtyGH9ZRumQDZ56j_uIl6vh8Tf_EalRrIpeUNHzclFevBupMgq5ndtUfXe28FQYq0Leu7_LGaCYgwW8LidWAWzOokuphHl9Mvct90dMfXZi3GIpBrBz7QAdyq7fDGDAT_CHR3XPt0tIkvZRz9_wK8kZnkKI-yxTUr1flBZzbseFgqK0ctpLR82iFVedgjtG9qi8OBxpr53KHVtmWJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
ابوالفضل جلالی:‌ حضورم در دربی؟ هنوز هیچ چیز مشخص نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/105041" target="_blank">📅 21:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105040">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fd696124f.mp4?token=rq2TjwtgB-6NvwH8pWquBVk6HMy8V9T4w3TOtA0w-BHU4WDyDcJ7oqEaEQEt0aW9MnrXvGYvs5H3LhgaS2LZdtsgAGXo8xMEdkWNPtuhafkBuGTYyv_hHPF6FNfY6zXdDc2_NqpWcFqtqtxo35omvg9f1aCtAENA5dz6KuwcYB4uP-0T98YYYhlRGYJ9v0yqAS6E5OLGSnblxgp662Wxp_daErrkLjfg9jkNQi66gBUaFOEKIOtTFFPJIBE0fzc_t78zjVWVqrSbJ-VjQPRsDi7HUzg4BY8fUUx-7waiTDvDjKuynsB9JDqI-XVCfXoj4LLTeFYQ2gfA4b75wdux-W3Xwy46yGz2-QNHBzWWaVgVPuiVVr5TnHloz1M30qysyLLNa4D43lop6Isdma3CukNzcP4GeiGTdu9EArcvr-D808ctvAds8SHxD2j7q90xIem5NUnPAXoyBwrMoAUhG2daGxdb2WgMFoscRP7B6v2DgDrhe6mEMooJ1sEphv46tHNaYEQYkTrV2n3acFqzBA0fX_82MVWhv3W3JNRS8pzXAHpB1Cu0cUm0DwJ2a0VhmAIn9lWa38qLktJ0P_woUuVnVK6oHzboW4hyFR5YJ2SckoNfl3LBiTq7W6yLaIpcu3bL0DLuSUZZJRoSdLEDeGoiZUohbPepOh7qP7aY1KU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fd696124f.mp4?token=rq2TjwtgB-6NvwH8pWquBVk6HMy8V9T4w3TOtA0w-BHU4WDyDcJ7oqEaEQEt0aW9MnrXvGYvs5H3LhgaS2LZdtsgAGXo8xMEdkWNPtuhafkBuGTYyv_hHPF6FNfY6zXdDc2_NqpWcFqtqtxo35omvg9f1aCtAENA5dz6KuwcYB4uP-0T98YYYhlRGYJ9v0yqAS6E5OLGSnblxgp662Wxp_daErrkLjfg9jkNQi66gBUaFOEKIOtTFFPJIBE0fzc_t78zjVWVqrSbJ-VjQPRsDi7HUzg4BY8fUUx-7waiTDvDjKuynsB9JDqI-XVCfXoj4LLTeFYQ2gfA4b75wdux-W3Xwy46yGz2-QNHBzWWaVgVPuiVVr5TnHloz1M30qysyLLNa4D43lop6Isdma3CukNzcP4GeiGTdu9EArcvr-D808ctvAds8SHxD2j7q90xIem5NUnPAXoyBwrMoAUhG2daGxdb2WgMFoscRP7B6v2DgDrhe6mEMooJ1sEphv46tHNaYEQYkTrV2n3acFqzBA0fX_82MVWhv3W3JNRS8pzXAHpB1Cu0cUm0DwJ2a0VhmAIn9lWa38qLktJ0P_woUuVnVK6oHzboW4hyFR5YJ2SckoNfl3LBiTq7W6yLaIpcu3bL0DLuSUZZJRoSdLEDeGoiZUohbPepOh7qP7aY1KU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
مصاحبه سمی با هوادار پرسپولیس قبل از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/105040" target="_blank">📅 21:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105039">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rB31PgI88U8lCBRPDFKMaAsgM2vbXTV-RH5MEMUSpZHUsKXH2suAUx9EHs_LFS0bhTsFqxQlAgEEe0mYrqitQ81TvIxnyNgfPXBNhT4i9yJa0MZNVxWxbqE4pSheZ-UXWIfgvrPwN8Wo1cXOEEdoRetFNtGhZmxx7Q-e1xznXX6Y9mNZ8RVaZTKlyUQ19g3ZkTVYvqzjCJplWieo_xpRYsMU5iD5GndaPLZlWoy_tvwv5mer4St7ssnvT2eKb5K-FmPsEhgKLB2qtXixblnY03lRtUF3Tp5M9RfwXGv8sP9z4Q7SSNtKBqy_ClZY00lvUqMK1kw5Z1fZ5qwrA4lbLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
هفته‌چهارم لیگ‌برتر فوتبال؛ یک نمایش روان و دیدنی در شهرقدس؛ بیفوما همچنان درخشان است؛ تارتار با پاسخ به منتقدان به استقبال دربی رفت
🇮🇷
پرسپولیس
😆
-
😏
ملوان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/105039" target="_blank">📅 21:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105038">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adIby5AgmbjfcScRiwkq8HnVF9BrJDh4JnbNeA9uz0NWe7bZ8gAY3Pxi6yqCoPsX8LH69nXdfRWqhEYQE5aZYZurCvknOsJdCr9JfHFHSXC1hMWnQ9GOjf-o6RMO0MrLyo-DDFQE7vCUloa-tMKy1F_JC1pRDtMONP7tkXAkl8aBh9-8Hv6WCW703m1jxDRgEOqV1oE73rfxkYWwnZY3r8mmV13PfVFSIdX5ZmB_C84TJ1hDyz98apqEp7x8KBq2EmgpXWN5zShMVNept3SIOiT2CwnDBra2cgMDY4JCMrnT14CYLBTDWGmx2OiHibSlaPZY0ZTQx0r1qI3tjBgEow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
✅
هفته‌چهارم لیگ‌برتر فوتبال؛ یک نمایش روان و دیدنی در شهرقدس؛ بیفوما همچنان درخشان است؛ تارتار با پاسخ به منتقدان به استقبال دربی رفت
🇮🇷
پرسپولیس
😆
-
😏
ملوان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/105038" target="_blank">📅 21:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105037">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
پایان‌بازی؛ فجرسپاسی صفر - ذوب‌آهن صفر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105037" target="_blank">📅 21:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105036">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApR6ai0JJTMSHOUNO7AS669FLWS24D4LZDmvin1IPUy2YfNGh4LUmOVqFYc2iSCYZ8Zp4201car3vqRossWGpdILlzeUAoUITX-jThox8sxcV-pDt0baWBq9aXPr0fO4LdBbwe7wdsYdX6NNR3oBqOLJGb8FMvaVCNJog7szl5lN9oiWF4IrO3KhLBaNRddLWCjm_tpArzR6bNHUI61H5QGlBG6CUXp5mZmU1LKFiZsk2EZs5OSTN8cOJuxeULLsK_XvZxaLf_-Hnldsoc6i1vFHHeP5L6gkWV4b5mtlUNYntbHsw_SvBxKLdYnLnwJe8zxFSj2UCisKv8HWx7qjDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پایان
‌بازی؛ فجرسپاسی صفر - ذوب‌آهن صفر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/105036" target="_blank">📅 21:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105035">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🟥
بازیکن ملوان از زمین اخراج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105035" target="_blank">📅 20:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105034">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bd7def575.mp4?token=N4cTd6UEAS20FxrHL7MovKSrpW4b0nJ8GMnz46ZJrPtYUWFyFmE_pmRyHtJVkxQtz0_5MTcFv9LZqsD8wxzPE8g_vAFoFHz3msyJy4_MY5fT1NAQuUrt-RD-LHEEiwyC3BdARJ8PQNo4LsM58tEPy1zgLlPu1MlwCJDBa_679hRLdAMHCTGpPao8eqL1vx6zJJOyp48YTN6T51zfTSR1SED7sXGv3fgc_7bey_ZbuFRIMVRtul-NFQtYb1u8E0N8BqpKPqStHOFJQEs9Yf7dCPUYmYHVYOXFJYry7QgjkGUleaxj0pz_JbwAUTvtq395Sir3KyVpBvtcL0bCbXRbHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bd7def575.mp4?token=N4cTd6UEAS20FxrHL7MovKSrpW4b0nJ8GMnz46ZJrPtYUWFyFmE_pmRyHtJVkxQtz0_5MTcFv9LZqsD8wxzPE8g_vAFoFHz3msyJy4_MY5fT1NAQuUrt-RD-LHEEiwyC3BdARJ8PQNo4LsM58tEPy1zgLlPu1MlwCJDBa_679hRLdAMHCTGpPao8eqL1vx6zJJOyp48YTN6T51zfTSR1SED7sXGv3fgc_7bey_ZbuFRIMVRtul-NFQtYb1u8E0N8BqpKPqStHOFJQEs9Yf7dCPUYmYHVYOXFJYry7QgjkGUleaxj0pz_JbwAUTvtq395Sir3KyVpBvtcL0bCbXRbHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
مازیار زارع کارد بهش بزنی خونش در نمیاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105034" target="_blank">📅 20:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105033">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a373e346f5.mp4?token=rnGEdkv97Jlkw4ZCMCZLugbX-gCNmgDfHq-JILABRfvm9RkpD6PibV1YeAL-b2ceJO5vErOB0e08tEp1XOD-cbve_xNYto-CrEkPCKk8qCJw_a6ySv4JXdFECZwooyLhr6k0nB90rt9YuCxgxFNJqdlesRUXE0I0__dGrb7oxTsw0lhJvFvI6Qn9fupIdqNTmiRynPtgu-JkzvBaFzztKmH9JpTfJeGhaM01BkG_liRslqdCSTqLlLKWi-qrD4KEz749sK2sCP5Rri36JoPQLcl63-9524BfElQw5R6TgV6qODloJqnAgHJrESrdKoSy2TbSBUWHPh-sSrQwpIURp1Jrs7sGtkL1LzW75OqT7OgGetXBG-fwqxNlZY6cfTMLpWmQZroeYYPfygWtddoc-vIDQcBdnu0vPvj7bER8PzBMh-6jYJ2LopfnzxQHFd8Pr2ySu2oKmGrNiHffub3kvr_wXWld500zqDEIKP2HARrRKBu2LFkRqZSd8sUvOjcCQoi7QSAKnGD46uPMJVuuQv0FmHl98WbI_gTXxf2R_ZFNJiWr6bGKDbC_EoUu8JHmECiF3K5F5t3RaR0avuxT9YCBwxXKdGsaStvcScYCAWIcFal1mG5kqW871W6Xwk-oPhuyOVXeHlrM5A0xG5BWQ7ebYwZNsia6QARGVtxfwnM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a373e346f5.mp4?token=rnGEdkv97Jlkw4ZCMCZLugbX-gCNmgDfHq-JILABRfvm9RkpD6PibV1YeAL-b2ceJO5vErOB0e08tEp1XOD-cbve_xNYto-CrEkPCKk8qCJw_a6ySv4JXdFECZwooyLhr6k0nB90rt9YuCxgxFNJqdlesRUXE0I0__dGrb7oxTsw0lhJvFvI6Qn9fupIdqNTmiRynPtgu-JkzvBaFzztKmH9JpTfJeGhaM01BkG_liRslqdCSTqLlLKWi-qrD4KEz749sK2sCP5Rri36JoPQLcl63-9524BfElQw5R6TgV6qODloJqnAgHJrESrdKoSy2TbSBUWHPh-sSrQwpIURp1Jrs7sGtkL1LzW75OqT7OgGetXBG-fwqxNlZY6cfTMLpWmQZroeYYPfygWtddoc-vIDQcBdnu0vPvj7bER8PzBMh-6jYJ2LopfnzxQHFd8Pr2ySu2oKmGrNiHffub3kvr_wXWld500zqDEIKP2HARrRKBu2LFkRqZSd8sUvOjcCQoi7QSAKnGD46uPMJVuuQv0FmHl98WbI_gTXxf2R_ZFNJiWr6bGKDbC_EoUu8JHmECiF3K5F5t3RaR0avuxT9YCBwxXKdGsaStvcScYCAWIcFal1mG5kqW871W6Xwk-oPhuyOVXeHlrM5A0xG5BWQ7ebYwZNsia6QARGVtxfwnM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل سوم پرسپولیس به ملوان توسط علیپور(56)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105033" target="_blank">📅 20:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105032">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8553440b1.mp4?token=YLUqXanm9opzkAy-boKyywE8NT1jjb_XRsLMl_Fp3mpPzw_wwfRYLLKtbLyuAN18-zZ4NjCeBvnha5z1SObF1kW80oMRtCACzz-Piez-sOdbz0gSmaAdnqtKfHQQxrbeuKUVNm1fQT3IxpPE7T56kaettBvp_mpsk-uhKOrTxQ1A_0xR4yMQ2GZZx8NoEscTfGNJ2QpefSVfs3DDPi_yPi5jBIcGrXw2jrQTv_xqeCFRW3ZrHbUFP_JcxixaJ-MIRHkhtJ6l-wkgpsGzvy0Qy-YMflx-NSBfc3mfFdMlcgaoch9pYsdv3qi4i0A2zqjucSZfo9DUzwfYtmD_bfMjxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8553440b1.mp4?token=YLUqXanm9opzkAy-boKyywE8NT1jjb_XRsLMl_Fp3mpPzw_wwfRYLLKtbLyuAN18-zZ4NjCeBvnha5z1SObF1kW80oMRtCACzz-Piez-sOdbz0gSmaAdnqtKfHQQxrbeuKUVNm1fQT3IxpPE7T56kaettBvp_mpsk-uhKOrTxQ1A_0xR4yMQ2GZZx8NoEscTfGNJ2QpefSVfs3DDPi_yPi5jBIcGrXw2jrQTv_xqeCFRW3ZrHbUFP_JcxixaJ-MIRHkhtJ6l-wkgpsGzvy0Qy-YMflx-NSBfc3mfFdMlcgaoch9pYsdv3qi4i0A2zqjucSZfo9DUzwfYtmD_bfMjxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
سوپرایزی که دانیال اسماعیلی‌فر ستاره تراکتور برای تولد همسرش تدارک دیده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105032" target="_blank">📅 20:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105031">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgzJ1RyL3GztIGmWEQUj54v94a8UKO1_DtMl8f8lLydTofu1aDp-KaCXTjXVkhlp_M-TULbjkEn4v_7eszuNciB_G9WihuPm3HwM0YMNR_CRsxMdvlPePRpHLrhTYFLHAOoUpH1D0zN__nDPwatQDnX3GhSPHrIJqQEoivCJCTSoaJAv2X_eebg_-uMvz7BvBSIj1UqM2BX83hsgb3WmAsp6Jm1ZZrUbljebgJ-kh3JR9KwNnsRqjQFJZUq4Giz9S-obDbelx1f0OdJPMl3y_ROexoBHrWDtZh4oL1xI8tKQDycROYr-EVU_RuZzvywo61GTnz--zgoIplPWsgfCGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
تونی فرشا کاندید سابق ریاست بارسا:
جولیان آلوارز می‌تواند آزاد شود، به شرطی که به‌عنوان غرامت، مبلغی معادل سرمایه‌گذاری باشگاهش روی او و دستمزد باقی‌مانده‌اش را به لالیگا پرداخت کند؛ یعنی چیزی حدود ۱۲۰ میلیون یورو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105031" target="_blank">📅 20:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105030">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce507e717.mp4?token=CyXZ2EJy3z13rFKD5A94XRys0gm28o4TCnBj9svO0khxS76ZGXJwgp8IAyxYchq7jsH1fzLMwA19XmNOWIkJwKeH9xaPbP9apWI7k8zsC9bN4dxnxXy3pvtXua97zZY_aaIlEm5yNsEE3Z35Xf1DVP-NNWi7SzaE1k5Kshifa2YX0xkJd1A8rUPqyuwQ4wKgdLwzn0vHEiRhJNRxOhRdkSUT_7848cyaqNmu09X0bnlcITvciGGvCnr3KQq0FtMEBprNsIunIuTHtgnUwJC5qOzIH3bNRyuY5xdcQb7KYXhQnkxCezykUJQP8PpGRkmnopSy5Vp-I0RuJDTY_7l6Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce507e717.mp4?token=CyXZ2EJy3z13rFKD5A94XRys0gm28o4TCnBj9svO0khxS76ZGXJwgp8IAyxYchq7jsH1fzLMwA19XmNOWIkJwKeH9xaPbP9apWI7k8zsC9bN4dxnxXy3pvtXua97zZY_aaIlEm5yNsEE3Z35Xf1DVP-NNWi7SzaE1k5Kshifa2YX0xkJd1A8rUPqyuwQ4wKgdLwzn0vHEiRhJNRxOhRdkSUT_7848cyaqNmu09X0bnlcITvciGGvCnr3KQq0FtMEBprNsIunIuTHtgnUwJC5qOzIH3bNRyuY5xdcQb7KYXhQnkxCezykUJQP8PpGRkmnopSy5Vp-I0RuJDTY_7l6Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
ریدمان باورنکردنی علیپور در موقعیت سه به تک
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105030" target="_blank">📅 20:03 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
