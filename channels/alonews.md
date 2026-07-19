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
<img src="https://cdn4.telesco.pe/file/SCNDJvpLe9ryw6ZYHRC0G8-arji2s-I_48XobwpVxRZzDzjW8RmIIHtsYH1CozwxvER-GNVtP5C9uUO4JUBoomHneXtD7ilh-UTw0nxwpXnav-YBn7xTtwxzCrbLAF8n_8FfDMhjrz7XmGGosLG8Z41KV4iEwIEhOd7zpb7SVlUxYZyCKJmhq2AhzW2go2Wc0Bhr1RieNNz24xL60wrxl8tjiq9BITvcpyJQQAjBsou88LF0ktPzN9k15lBtOxfCYNW65W7KqNSfI2m9F4j307IsOuId6p7r7celpO3Q1NPzbqrp6816p3jzWKUcR6aRkoMF8Opk_q7hdEhIWxeoqg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 938K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 23:33:16</div>
<hr>

<div class="tg-post" id="msg-135776">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
اسرائیل هیوم: مقامات می‌گویند سفر برنامه‌ریزی‌شده نتانیاهو به آمریکا برای شرکت در مراسم تشییع جنازه سناتور لیندسی گراهام در هفته آینده به دلیل تنش‌های امنیتی منطقه‌ای در معرض خطر لغو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/alonews/135776" target="_blank">📅 23:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135775">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgMXBNtUcFQYPDT9EWPjYINEaJVv-BLwBkJypERCWBfw14a-O2jwziY6qZqsVYRgDFLcBJHPaNz25xWgEIcZiii9ZoV0cQgio_yHOK6TP-1Z5CdHI8ty0rTO0z500SNjh0zm7F3gA6IdjMj5caJlgje3egchuXU6qS_x3mR3V2IOT9aKfY7vrtheHMoofwSzfi6TS6Q28LuJHj8ywgVGNbomCBh6D0SQ75OuN35y1Kg5UzuU14yeXEG5N2KVGk1cxX-gZ9TGzl_1gRe8G7PV9p2GFTjZfIy9anEZCRTqw1RlWlwKOJDiHBqaegWmA0xCa7GU4aXUYNxRm9UY3YvP4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه پشمااااااااااااام
😐
😂
هوادار معروف آرژانتینی بازم تو استادیوم لباسش درآورد تا به بازیکنا روحیه بده
😐
◀️
◀️
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/135775" target="_blank">📅 23:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135774">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
نیمه اول تموم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/135774" target="_blank">📅 23:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135773">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88873c492c.mp4?token=p_UUF8TmKJE477JXmy9Pqp70appydzIx5oDMJBV_-pNsM-7eAWmJMl50QWW2SwDp2tWkXBXDtBFsmMQtGDLHdTfl4-QlAz9CJmCSpG9HppuJKUROcOVXMooRrjSEEHG_eYKskJtdgqg3ccb29O92pMqsYXy9jvti06UMNKOl1my6yhQPTxtTm20AM_hbL4mPRpXJUwyRAHDv4-Z-W-y120__GNbY3PRQHi4LI9_EldokNs64Ggb_u7gTNWn5xJ-rN0NrxMF57RQ70uuA6_Tv-jF3acgqrcI6DhmY28XYJsaN6Jsw_hy_k8rqv29sUaUZYHD-Q4GSlFFKwqm1gK56IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88873c492c.mp4?token=p_UUF8TmKJE477JXmy9Pqp70appydzIx5oDMJBV_-pNsM-7eAWmJMl50QWW2SwDp2tWkXBXDtBFsmMQtGDLHdTfl4-QlAz9CJmCSpG9HppuJKUROcOVXMooRrjSEEHG_eYKskJtdgqg3ccb29O92pMqsYXy9jvti06UMNKOl1my6yhQPTxtTm20AM_hbL4mPRpXJUwyRAHDv4-Z-W-y120__GNbY3PRQHi4LI9_EldokNs64Ggb_u7gTNWn5xJ-rN0NrxMF57RQ70uuA6_Tv-jF3acgqrcI6DhmY28XYJsaN6Jsw_hy_k8rqv29sUaUZYHD-Q4GSlFFKwqm1gK56IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی: کشورهای حاشیه خلیج فارس بداند وضعیتش در پایان این جنگ عادی نخواهد بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/135773" target="_blank">📅 23:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135772">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/750cf8516c.mp4?token=YCQ5DK5qFO7dEOIX0IaisLrYASu0SmXRWfHeQ8jIw06UZ_t9wFfk-RpfM3JkWGiS92ZN8N3Tr8GsI8U1D3xZAJXkkGZ0XRKHi7oseQofkfVq7TZmxdlC9WjHpDQy7sebaoY_WBQifqp-KJMfiM8EB8DtcTQx09fzJOECFNo6jgKSk5lQLjluC0ilnUrfIRnOCLy5x77jDeva4UdZ7zlCw59dwwfFOAbtELlFohY74BakQk8HHS6nDZsRUAFLqHejp53KNIsMsHAGrtZwWnEgptLG0xbuaRPrgHcIcGBOIaswAC_veYipShmRtywylTkdyn1SIFqjGmoPKEjWG7wqzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/750cf8516c.mp4?token=YCQ5DK5qFO7dEOIX0IaisLrYASu0SmXRWfHeQ8jIw06UZ_t9wFfk-RpfM3JkWGiS92ZN8N3Tr8GsI8U1D3xZAJXkkGZ0XRKHi7oseQofkfVq7TZmxdlC9WjHpDQy7sebaoY_WBQifqp-KJMfiM8EB8DtcTQx09fzJOECFNo6jgKSk5lQLjluC0ilnUrfIRnOCLy5x77jDeva4UdZ7zlCw59dwwfFOAbtELlFohY74BakQk8HHS6nDZsRUAFLqHejp53KNIsMsHAGrtZwWnEgptLG0xbuaRPrgHcIcGBOIaswAC_veYipShmRtywylTkdyn1SIFqjGmoPKEjWG7wqzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک تایسون قهرمان اسبق بوکس جهان با لباس آرژانتین
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/135772" target="_blank">📅 23:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135771">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ca28438f.mp4?token=PkkRWtra4DBPCL-s1arCvwBJuZNUX3rcR3nprCNLljjYRtGlWkAtwNznWDiwxtO8d4iaDuEqhEJToyn_p22gQyQaNYYjDPZD-ZYiZSZCQVmO603tpEXZbOmdGM76ZZhH1_hoNygZrkbxiuvmPygcEzvcajl2ygKK3lm2iP5DD6WuP0ehAbUDdVWKTEk9uOETiDov_A1yAS3iTGHDgMj3N_KFi26rqFC61_FkYrmwFhcpKLpZuy61SenC0Kybi4Z3o9a_wVWyGGDIwJEyRODcieqPXl9qymJtuY08I0ChmzHIK93dx0rsQ1kXHmWRZnltIxMOtBqE3pARTTBnjxTQFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ca28438f.mp4?token=PkkRWtra4DBPCL-s1arCvwBJuZNUX3rcR3nprCNLljjYRtGlWkAtwNznWDiwxtO8d4iaDuEqhEJToyn_p22gQyQaNYYjDPZD-ZYiZSZCQVmO603tpEXZbOmdGM76ZZhH1_hoNygZrkbxiuvmPygcEzvcajl2ygKK3lm2iP5DD6WuP0ehAbUDdVWKTEk9uOETiDov_A1yAS3iTGHDgMj3N_KFi26rqFC61_FkYrmwFhcpKLpZuy61SenC0Kybi4Z3o9a_wVWyGGDIwJEyRODcieqPXl9qymJtuY08I0ChmzHIK93dx0rsQ1kXHmWRZnltIxMOtBqE3pARTTBnjxTQFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رونالدو جام‌ جهانی را به ترامپ اهدا کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/135771" target="_blank">📅 23:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135770">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74a6cda5ad.mp4?token=BhPNjdeuAyS-n6j64aTWioljIXx21tr2Y6RknTnlt8B4dhCgBJQv5HzNeJdFI2RYncum9N-t0bLbxSFRHvILBKZkoE_AUDehn3V139Ds9O-cKF41u0j7tFgdT0HKMLuKlSyPSX9H-kfN7nbYP5gZG-lM0jdUcmTYBq9TOA93jd6AYny8M8vCRWmGwsFE7OKrs99Rgf5Pk2hkhrif8lfU1yASGcmXW5F8SkGqgZ-sCiuqWXRboFB6JoJNDjaZSIFXaP3FV8W5SfcwJdvBkZ5vyqMnOQL3Sc7EeWKu9QjjIV3Mh63FBdApbNxTO1I6tJQGwy0PI4OhJjJaTWHDJesYuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74a6cda5ad.mp4?token=BhPNjdeuAyS-n6j64aTWioljIXx21tr2Y6RknTnlt8B4dhCgBJQv5HzNeJdFI2RYncum9N-t0bLbxSFRHvILBKZkoE_AUDehn3V139Ds9O-cKF41u0j7tFgdT0HKMLuKlSyPSX9H-kfN7nbYP5gZG-lM0jdUcmTYBq9TOA93jd6AYny8M8vCRWmGwsFE7OKrs99Rgf5Pk2hkhrif8lfU1yASGcmXW5F8SkGqgZ-sCiuqWXRboFB6JoJNDjaZSIFXaP3FV8W5SfcwJdvBkZ5vyqMnOQL3Sc7EeWKu9QjjIV3Mh63FBdApbNxTO1I6tJQGwy0PI4OhJjJaTWHDJesYuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چه کسی به خوزستان شلیک کرد؟!
🔴
چه کسی خوزستان را کُشت؟!
🔴
یادتان می‌آید؟ دقیقا همین روزها، پنج سال پیش، تیر ۱۴۰۰، زن خوزستانی فریاد می‌کشید: «چرا تیر می‌ندازی؟ تو که خاکتو نبردن! ما آب و زمینمون رو می‌خوایم.»
🤔
هر طرف این حکومت و طرفدارهاش رو میبینی حرام زادگی بیداد میکنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/135770" target="_blank">📅 23:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135769">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
وزارت خارجه قطر در جریان رایزنی‌های جداگانه با وزرای خارجه عمان و عربستان بر ضرورت کاهش تنش و تضمین آزادی کشتیرانی در تنگه هرمز تأکید کرد.
🔴
همچنین بر احترام به حاکمیت عمان و پایبندی طرف‌ها به دیپلماسی تصریح شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/135769" target="_blank">📅 23:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135768">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری / روزنامه «معاریو» به نقل از یک منبع لبنانی مدعی شد ژوزف عون رئیس‌جمهور لبنان و مارکو روبیو وزیر خارجه آمریکا، به توافقی درباره خروج کامل نظامیان اسرائیلی از جنوب لبنان دست یافته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/135768" target="_blank">📅 23:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135767">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
گزارشگر صداوسیما : خیالتون راحت باشه که تا پایان بازی هیچ تصویری از ترامپ کودک کش و جنایتکار پخش نمیشه تا اذیت نشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/135767" target="_blank">📅 23:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135766">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWEXElFgmV_sv6SSdz48WWCZR7txUC7I1Es3K13QENEstekxdTEK5VuD0wzioFIRGqAXg9q1WUhTU5YCbLjp-wMV1O_68Jx1EfCMPKjGq1p_EmYa2vN4s6MVl7VZQoFEJWH0JgoQhrCSaqRKvY9E5LN976pI_pRiQXumaZ5f7-zuJ5yRxxPGAzcMu8kEgzZ95v2phYnUT1r9uzbk98UG1jIkCA6jpq-ktNlOrp0TF3mpBVQxDU4mgBMFrXcEkGFe5n2vh3gH070jpcATPu73SjoTpTvIUdnw3oeW2BllNDe-YB4JZfDBwLgJ9f7aK0Uki9aN3fYDdSeIKWP1zQaf-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
المیادین: صدای انفجار در اطراف شهر اربیل، مرکز اقلیم کردستان عراق، شنیده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/135766" target="_blank">📅 23:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135765">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAloMedia | پخش زنده ماهواره و مسابقات ورزشی | اَلومِدیا</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ie_GM3540DEFV3-MixkdTLwDqGpWKOKZqgoOVuU-VpgLXblBGvfzHUK4KcdcT3ztVmTaCI3kpHPkUuSE4cgl3c2WDY7D0WOc2oBGhDGTIpWVAYcEA_HjSk2ctHUS2G5smq83Ef0KzYaLMCi2v9ovgGYtbXJHIouO5JOpfJTEwibqsUunhIlrLMrvtCnG75WfWc8BpT7cuZD7z6RMOkkKaNVCsKB0fT8-9SMM25XSFFWGHToKrkgfk_YxRpaze7yyRPjFhWUw9plYX4SF1AmlPIS_reNLIr7eA-kKDEd3OJtM_8812FVRUFtgrHjZxLfRxOL6_DITCfFINKr66sjTiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پخش زنده فینال جام جهانی
🇦🇷
👊
🇪🇸
▶️
کیفیت FULL HD
▶️
رایگان
▶️
بدون سانسور
🎥
شروع پخش زنده</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/135765" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135764">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی: کویت بداند وضعیتش در پایان این جنگ عادی نخواهد بود؛ کویت درس عبرت بقیه می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/135764" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135763">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fb1ac4cac.mp4?token=jyunEP928FqxIy-48zrKpYiOL6Q9PbKIEnG_bgXkqk805cuIaNoRGyVRAh5G_610utpUYKQIbyWGpdPztbbJWeryHUX5f2YH8NWjz1v4RcooJZaBezgiumBXlk8ajCAnrHeYxfFNbed39xcjm6vgg1mFC9XqHdBlrhpuRofvcE6xCnVSuYb7zmlReC6p_8KTwv5fKxJoaFpdqLwEGklIOdKDss015RzOtvF-YNV2vZVUINRx0Cxofp6iAZ1AackgQmBhm_2iXEMiZ5St3-Zg0AgSd8mmq6SDJJT5tWosJ-RW9qg27WVXJ4ItHDbZoukaDxDm_1c20bQO32cid1Yqpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fb1ac4cac.mp4?token=jyunEP928FqxIy-48zrKpYiOL6Q9PbKIEnG_bgXkqk805cuIaNoRGyVRAh5G_610utpUYKQIbyWGpdPztbbJWeryHUX5f2YH8NWjz1v4RcooJZaBezgiumBXlk8ajCAnrHeYxfFNbed39xcjm6vgg1mFC9XqHdBlrhpuRofvcE6xCnVSuYb7zmlReC6p_8KTwv5fKxJoaFpdqLwEGklIOdKDss015RzOtvF-YNV2vZVUINRx0Cxofp6iAZ1AackgQmBhm_2iXEMiZ5St3-Zg0AgSd8mmq6SDJJT5tWosJ-RW9qg27WVXJ4ItHDbZoukaDxDm_1c20bQO32cid1Yqpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خداداد عزیزی: آقای قلعه نوعی اوت شدین.
🔴
تو این تحریما مردم نون ندارن بخورن تو ساعت ۱۰ میلیاردی تو نشون مردم میدی
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/135763" target="_blank">📅 22:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135762">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgvtWbCZvCgeDi574cND2iyUpIv7hZrTXb47g1eDey0e8CI_kuGG9mpffosZATiqbEYPx_d1_WroYN1GIc1-BIMSfUvX0ZrfXjFuUoniSXzLsvSFcjr2i2VH3-5QMLZTyBqti7ekTOz3Giiymuhc9_0YM2TogRQkE05xhj3pJEoMOwMkb-dVAQsBjVgLsz_1OvU0ReCotj5AJsBR5F28qpxSBL5722Su62u4UodVPsjdjE4vh2tdjWzjrH7C4pe6-r41gsSn_xDIU1_jMJDVYTFMMcV6rWfoyFZ-niBdhEzC9Gyir-0rLZixiIOxcP7pXV_koC7QxnJogPB1mA8NJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ هم اینجوری داره پشت شیشه ضدگلوله بازی فینال جام جهانی رو میبینه:
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/135762" target="_blank">📅 22:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135761">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91d43bfdaa.mp4?token=iXjo5FtPfJD4e_SVbXlXSSCkKIicvWYfdgn9eZkQWEQTgunZnrK5X6cu6tWQMbDgLLgXrPtRbWMkz9a5e9cUam3SyeTw41yHvcLn0wiDfA6Q-hMukdxNULCmHjrJcs-sAyR0cKFYRb34UExOP2zup3O766YVdk3p2DegTbS-w8LDys13VNOWz9czjbGSzM8NZjhTYDP9CAynkQvGU_OvX8KhY8fi1MfZlJqIY9CvKv9ssq0P2Qf1QDMs3QAUGBu8snCACYiDPLouAi7EXQVBUUuNrhd3UlW8nzp9DbFbnCHmTE9A-D8BfTD2PbHkeikgPbDpS1CFlpzeHS0wRzxTMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91d43bfdaa.mp4?token=iXjo5FtPfJD4e_SVbXlXSSCkKIicvWYfdgn9eZkQWEQTgunZnrK5X6cu6tWQMbDgLLgXrPtRbWMkz9a5e9cUam3SyeTw41yHvcLn0wiDfA6Q-hMukdxNULCmHjrJcs-sAyR0cKFYRb34UExOP2zup3O766YVdk3p2DegTbS-w8LDys13VNOWz9czjbGSzM8NZjhTYDP9CAynkQvGU_OvX8KhY8fi1MfZlJqIY9CvKv9ssq0P2Qf1QDMs3QAUGBu8snCACYiDPLouAi7EXQVBUUuNrhd3UlW8nzp9DbFbnCHmTE9A-D8BfTD2PbHkeikgPbDpS1CFlpzeHS0wRzxTMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: هم رونالدو را دوست دارم و هم مسی را
🔴
من همیشه رونالدو را دوست داشته‌ام، همیشه مسی را دوست داشته‌ام. من اخیراً با مسی آشنا شدم... آنها زندگی خیلی خوبی دارند.
🔴
من فکر می‌کنم آنها زندگی خیلی خوبی دارند، در واقع خیلی راحت‌تر از زندگی من. من دوست دارم حدود یک ماه یا بیشتر زندگی‌ام را عوض کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/135761" target="_blank">📅 22:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135760">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7b2786fce.mp4?token=aNPxzxAVhoULtZ_lX4fkXmkbrTrGTWkTjmvT8uOfk6VMRQLT-FkyuNFXKGnqbvxGmwWm9WlT0iAUhdEjPhRGEE6FCGEe_vuAuqo9URpdoK7yVKUWnbtzswLWXBaTM3qOnUyXai4rSnIT1G1djEDZsZ5KEYQgx9SDbx_nJgPW8Ew6WJ6yiATZlKOdXVT1Dcj55kbzxrNaXoRjj_J-WNbzx_aAU7K0r1ymtuIwJS2_goP_iGcEYD5VyT2zfJqNHtMYQFcjhU2JusbX7XqHagB7QuPZxydEzY1Yh4IcArheWC2mBcwhr-MiKh7GgJNeHqZw8O4oQT980qzVnYMEigb9CjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7b2786fce.mp4?token=aNPxzxAVhoULtZ_lX4fkXmkbrTrGTWkTjmvT8uOfk6VMRQLT-FkyuNFXKGnqbvxGmwWm9WlT0iAUhdEjPhRGEE6FCGEe_vuAuqo9URpdoK7yVKUWnbtzswLWXBaTM3qOnUyXai4rSnIT1G1djEDZsZ5KEYQgx9SDbx_nJgPW8Ew6WJ6yiATZlKOdXVT1Dcj55kbzxrNaXoRjj_J-WNbzx_aAU7K0r1ymtuIwJS2_goP_iGcEYD5VyT2zfJqNHtMYQFcjhU2JusbX7XqHagB7QuPZxydEzY1Yh4IcArheWC2mBcwhr-MiKh7GgJNeHqZw8O4oQT980qzVnYMEigb9CjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
موگویی: «ترامپ درباره مشهد درست گفته بود، مشهد سقوط کرده بود.»
🔴
یادتونه ترامپ اون شب چی توییت کرده بود: یک میلیون نفر در مشهد تظاهرات کردند!
🔴
یک میلیون نفر در یک شب فقط در مشهد  اومدن بیرون، جمهوری اسلامی قتل عامشون کرد و هنوز داره تک به تک جوون‌ها رو اعدام، بازداشت و شکنجه می‌کنه و چپ و اصلاح‌طلب خائن ایرانی هم فریاد مردم، ابهت بی‌نظیر حضورشون و بزرگترین قتل عام خیابانی تاریخ رو انکار و کوچک نمایی می‌کنه.
🤔
شرم بر شما حرام زاده ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/135760" target="_blank">📅 22:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135759">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3cfd8ff5.mp4?token=MDf624_dysnEWOrDw5lLVrNxyEcdO5Te9bfpH-3be7X7rwW4rpVKc4bTc_fA12hRPCBTPPxRYnMMUQie-EbAs9mzHul6SlEA0LldP42_85dyX9miPn3ZlhMy71_3gaLDy5npnNdBViAM5OzRTErNZn31op6ltQhJXFPUfF_wxjNxohneBRwac3cLQ5Tf7l7CgoqkuY12nw58kLsSXSPtP4BdG7XYbFFELOGf7GzWXPwVWd9iooWyuqSkQjEjWTdXieyqrkPHI4vqRFkkKKvqah3hY4GNdN2_6DsGtDmdXXTZygvw8glZZR7zP5oCrRLZnKl9fI0R465S9TKT9i-0O6h3R_vRFC-dlO0AyxpKXWEd5rVX2ZvbnjRgE2rvar9vtkADbJaD_pjNY4Ss9sUsojUqCbQQVr4OLXrMYG39YAIXSrvy5nFaMM4r4lohnkhqGU7VyKe8t5Q9i7bb4jnLs13m1Pu-nOy99GhF3ew6aSVMvhjdjxqBpCqK5Me1BAMJPUzKKB0G-3nzd_8GGVtCZW_sJCknga-nw29IcRORoeDsdckZR-fjCm00eRpteJiOKDGGB1M6rW0KDadCWK_3UCRafZwOqWuTVeG1HAVS-KH0OHCkHmpLgPGU0OMAS103c0E7YIrD4pmEpNNePNAJI7B-K1U5riW2KRWBbKoO6FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3cfd8ff5.mp4?token=MDf624_dysnEWOrDw5lLVrNxyEcdO5Te9bfpH-3be7X7rwW4rpVKc4bTc_fA12hRPCBTPPxRYnMMUQie-EbAs9mzHul6SlEA0LldP42_85dyX9miPn3ZlhMy71_3gaLDy5npnNdBViAM5OzRTErNZn31op6ltQhJXFPUfF_wxjNxohneBRwac3cLQ5Tf7l7CgoqkuY12nw58kLsSXSPtP4BdG7XYbFFELOGf7GzWXPwVWd9iooWyuqSkQjEjWTdXieyqrkPHI4vqRFkkKKvqah3hY4GNdN2_6DsGtDmdXXTZygvw8glZZR7zP5oCrRLZnKl9fI0R465S9TKT9i-0O6h3R_vRFC-dlO0AyxpKXWEd5rVX2ZvbnjRgE2rvar9vtkADbJaD_pjNY4Ss9sUsojUqCbQQVr4OLXrMYG39YAIXSrvy5nFaMM4r4lohnkhqGU7VyKe8t5Q9i7bb4jnLs13m1Pu-nOy99GhF3ew6aSVMvhjdjxqBpCqK5Me1BAMJPUzKKB0G-3nzd_8GGVtCZW_sJCknga-nw29IcRORoeDsdckZR-fjCm00eRpteJiOKDGGB1M6rW0KDadCWK_3UCRafZwOqWuTVeG1HAVS-KH0OHCkHmpLgPGU0OMAS103c0E7YIrD4pmEpNNePNAJI7B-K1U5riW2KRWBbKoO6FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ و بانوی اول ایوانکا ترامپ در کنار اینفانتینو در بخش وی آی پی استادیوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/135759" target="_blank">📅 22:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135758">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuBWLx0EB0Q5331gUe6X8DscdeLVkLebzSzo472ojSAqgyG5R-s8hFx4iKCPwISz04ghMixT59VHGm8QHx_3hj6e_pQbdU9h-NBcvcfedlP_SWNg9ZbRd0YHJbIrkNiKefMH9jB2-NzZOiYfUDHaHwSL5Ycp5AmfhtJYwc-LmgwO6VJubbm4tRkBz6Xm7KP-5WzEPnw94kjjjC09g5Juif011cNpaa1l484edWFqxPFRFEcMqORwrB5h4JJcnCt0Fq9vKEQOiS8Q7Wp9qOCXQWscZzptmBDZJJJkaDlfyCCwglbouL6K5MbGpaHZu0H7u_e_vbkY7Ak9_PGWR0m6hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک نظامی دیگر آمریکایی کشته شد
🔴
سنتکام: فرماندهی مرکزی ایالات متحده (سنتکام) روز گذشته اعلام کرد که در پی حمله ایران در تاریخ ۱۷ ژوئیه، دو نظامی آمریکایی در اردن کشته شدند و یک نظامی دیگر در وضعیت مفقودی قرار دارد.
🔴
پس از یک عملیات جست‌وجوی گسترده، نیروهای ارتش آمریکا امروز بقایای ناشناس یک فرد را در محل حادثه پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.
🔴
به‌طور جداگانه، یک نظامی آمریکایی در شمال عراق در تاریخ ۱۸ ژوئیه، هنگام انجام عملیات انفجار کنترل‌شده مهمات منفجرنشده باقی‌مانده از یک پهپاد تهاجمی یک‌طرفه ایرانی که سرنگون شده بود، در جریان عملیات کشته شد.
🔴
یک نظامی دیگر نیز زخمی شد و همچنان برای جراحت جزئی تحت درمان پزشکی قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/135758" target="_blank">📅 22:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135757">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⭕️
چند نکته بسیار مهم برای حفظ امنیت شما در تلگرام
🔴
برای تنظیم بیشتر موارد، وارد مسیر Settings > Privacy and Security شوید.  ۱. مخفی‌کردن شماره تلفن وارد Phone Number شوید و این گزینه‌ها را تنظیم کنید: Who can see my phone number: روی Nobody Who can find me…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/135757" target="_blank">📅 22:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135756">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
گفت‌وگوی وزیر خارجه قطر با وزاری خارجه عمان، اردن و عربستان درباره تلاش‌های انجام‌شده برای کاهش تشدید تنش در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/135756" target="_blank">📅 22:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135755">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gf8f7HM0Wx_BQTo6PTcPXMJtXztq6laWBqmpD_IXG_VM9tSW3JwlrWvaPCxIyIdk34m3c9inY78tMa77KExOQ2PWBgaW19GpDtmqBQ1KcsRfaPxsZw8INbBKQuvycZC9RBNGglOJK3i1ENBl1jGSfkA6lGtlazVYG71O_AIxOeSxmG7w3W0EjZ7DqOvSCcyIHMMEzyryK6QzKqfCxsPX112ogIWMBjhjYIUpoiRnd-xe8tACqzIs7fgGaVrMWzPbWrFXDr2Bsp9DLbfOK9t7bVe0q7rfkun_T9mqMB50oGspsGwS1wqkWlU9J4V6ISkqfeFKpT2Ot8EeoMX3xGaLOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ با هلیکوپتر وارد ورزشگاه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/135755" target="_blank">📅 22:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135754">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doQWz6bXOOF_HTmg6NHcQawiK26uussfYsFouqUAhmyO5xJJgLvU4HpD22TOikIzNeLTZ3CTBfllXlOK71FyldDk03tcg5pLk79Ys69LrPWu5nUkM2DwnvmNCxWPs0IyB4jRrVAK7ahWNH4mgifA-4eaTBZoBizdpes7eETNwDJLntkZTpOI_dx6SGCeGU2mRtWkyLAXsiVj7vPIW2MqcD-CVMp1M5UO_5Jo4woSdrONw8yfzIi0cwVx3caX-ulZNOPSR3pWT_f98qY8kJh9eZ-gVjdnyJO-taiagUKecDZzVPJfiqN5WZCpGDyb23Yvi5eHQyhUTGSseGQYCeGm4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری از دونالد ترامپ و جیانی اینفانتینو در ورزشگاه مت لایف
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/135754" target="_blank">📅 22:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135753">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d206001ec.mp4?token=ugQJ58_Zn5xO8G7zGlDSVEvNsStqi1zZWwqJcbJxVF3sgYyotHunm9EG9TDJjEkeOPkrwfcfT2X0bFOLYEEHXpqGKEu24z-hcezFW2tA6QUwh3ULM7zmheRPDfTZ7cHQMfRbgMwl8IgRsmfjUXpLwmQGh-vRuzFcMp84nDfyGAi3SCjp8CiGDS3e9kOMSBYL8zkGEu9TECeN5zzxXPGg8f8IZu9s-AcF5up_UHdBkvnc95Sg_rBoMGAYRqDXv3XOF3bdesMhoInl4McpmxOjYsQiqS_kuSwU2y8-xhz7PBLqsU7kuLPKeMaIokL9qSGX3SiEGN8kuZp7vhbaSxEJzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d206001ec.mp4?token=ugQJ58_Zn5xO8G7zGlDSVEvNsStqi1zZWwqJcbJxVF3sgYyotHunm9EG9TDJjEkeOPkrwfcfT2X0bFOLYEEHXpqGKEu24z-hcezFW2tA6QUwh3ULM7zmheRPDfTZ7cHQMfRbgMwl8IgRsmfjUXpLwmQGh-vRuzFcMp84nDfyGAi3SCjp8CiGDS3e9kOMSBYL8zkGEu9TECeN5zzxXPGg8f8IZu9s-AcF5up_UHdBkvnc95Sg_rBoMGAYRqDXv3XOF3bdesMhoInl4McpmxOjYsQiqS_kuSwU2y8-xhz7PBLqsU7kuLPKeMaIokL9qSGX3SiEGN8kuZp7vhbaSxEJzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کانال 14 عبری: دستورالعمل‌هایی برای گروه‌های مختلف در عراق صادر شده است تا برای رویارویی آماده شوند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/135753" target="_blank">📅 22:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135752">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
خبرگزاری عراق: نخست‌وزیر عراق در پایان هفته از تهران بازدید خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/135752" target="_blank">📅 22:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135749">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8rKz6nawNYrkvjiEjK1Th2hHrsBoKACd0908jfA3ACQS-k-JCteFCYUOTApj0ICfl4GhNEt5QbDTpRMMLNeGTBtxIW9swaFw0ariJffFmaaK04CzOF6Q1A8JPCsOC-4tY4izGXI_bhhRYjwmc1HGyrzckyxZJ5OvwcWytY8MQuQMb0wZJcDWJgZZxZEeq7GY5qwLoq2RcThgmAgDOPWoxd0dJNQJL8nnJlnfX1ENFhFbVJ6shf4B0CLVT15KXLTgn-vT1N50F_1rhWjqrMmL0TwXWGqX2MN-I_eg6vAcezqbxxXdUKkCv20K7evOshXEHLkupFMWNTJELTsvEDUpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mvp2Of2lhq4nSf7KbI9H_xjbhjDaKqBmaiauCPKrCUd3nDpVnaAtsvZ8taRv6Rv0yh_d3_zhfPGQ3H8bETe4hKUstqwFmojAzNzQeePffm8FOjApFOTGlYxBsYfQxoCGW0XOfcrZ_E9izZH-29wx6FddI4uSYexfSRhHGThtxp4eOjsOBvhagT8_IqN5nhLzN_Vt9eGjrCLxz_9tWQft5JNcsmV_Hpgl2-P-VfiJe0Qmkl_oJY6swZF6gJQHPxNn6zX3aGkY4Fpwyqm4b-KEmNjf5l31lSEaepvme3P7GcQ7ql5gB_zOwarmpB_Z_IY-Sbe2Whxq0Vyfp0xuyCo9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-q6_ezigMdcXLN_XAuBf_5XqJqf2gI_yAMk40KKCWXR-8Ir0Eorf-OUbQke_wsoZXsJBRJlTZ9ApfJpmpa8pqBaBn7teZKXWvm9YE64mkizW37JW4SzUYGxHJcBVH-5GM5C8BNs_n_fgWMv0fUO7QJTyLL1jN3Afgsnnf_Il9IuHsDQNpD9i64WUPt3NIFksGlbK4Kj8XNSPe1vlxPcQ5lLcp95TQLbD1IVF6FWVROUbtpdGKs1HasbEy6WcNBJOJboGcdk-N_-SN4d2GZvEk9kPCiRwCAtFNeD7WwQ0kJ7Msh4cHbRtsDtlP4lW8D1akWoB0rqeXUnCFxSQpRcuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ در Truth Social:
کاشت درختان زیبا در کاخ سفید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/135749" target="_blank">📅 22:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135748">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
کانال ۱۳: ترامپ به میانجی‌ها گفته اگر تا پایان هفته آتش‌بس نشود، باید خود را برای تشدید تنش آماده کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/135748" target="_blank">📅 22:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135747">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
بر اساس اعلام مقامات آمریکایی، ایالات متحده جنگندههای اف-۱۶ و اف-۳۵ بیشتری را به همراه هواپیماهای سوخترسان به خاورمیانه اعزام میکند.
🔴
این اقدام که پیش از حمله اخیر ایران در اردن که به کشته شدن دو سرباز آمریکایی انجامید، دستور داده شده است، همزمان با افزایش تنشها با ایران صورت میگیرد.
🔴
به گفته یک مقام نظامی اسرائیلی، ممکن است برخی از این هواپیماهای اضافی در پایگاههای هوایی نیروی هوایی اسرائیل مستقر شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/135747" target="_blank">📅 22:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135746">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
استدلال این هم وطن کاملا درسته که میگه سرباز آمریکایی سگش شرف دارد به کل جمهوری اسلامی و طرفداراش
🤔
هرچی از حرام زاده بودن طرفدارهای جمهوری اسلامی بگیم کم گفتیم.</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/135746" target="_blank">📅 22:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135744">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N9J2o-n4bdZaHgj4F562i3OoWq-relBgq0P2T5SzmJ90ZoyNXtlJ0OdLt1VmaLTJyjOnqydOL402jvBwy0AFJR6T3eprtnNEO_opEBNvbaDfL5YYaiuXxolqSLozgTtJzQpUW1A6PNG68fK4URdsj1Wx2qvqKOo28Gp1UTOYBjk7VBPfOHXM7kdEyAxN3bquhfohjI-KawEWktIFwaY86TS_8YWDSHb8mv8r9miFwFETb4hkuXHNOlTNHbFhdkjPBl9-5D6_qNicmUs6IE4-fG0i-eO2sjEHim6J4CUuxbMP-ERM6W_ipUviVNa7rwyFDYym-FU2uBqpiiIISaKWuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fUa80J9WwaafcLAnyg3fTFHNd1C_C0dgVvh6JPDLQrhbngeJcClRFVej1YB5Zzp3Az2wfRh8_Sg2VL11x9uTivB-xa7HuW9kuDDGlDAi_RR91PxCZZbdmf-qTjMFao9O6POE9-N4r01MUHQySlUV--L78lE7uybLbvbx-AQne1eOexKmIQYcwguEO2KWmDDnf2Aa917intRywGu3IIzh2ZBN0_IUFcJhI47QBNdAvkuazHe8N7bHYTFSy6F4imvt4_g3UQtfyBbit-l2yqMNX5ZdBRiXqNfGm4eYqPj2ukkDm15UGUCXm5mjpl2uLmVgQImJhPUeUjFMfc9RTDANMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای منتشرشده، آسیب به پست برق یک مرکز داده بتلکو (Batelco) در بحرین را نشان می‌دهد.
🔴
این تاسیسات به عنوان یک مرکز فرماندهی و کنترل نظامی ایالات متحده و هاب پردازش داده‌های هوش مصنوعی عمل می‌کند. تصاویر به نظر می‌رسد آسیب به پست برق را نشان می‌دهند، در حالی که خود ساختمان مرکز داده ظاهراً سالم مانده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/135744" target="_blank">📅 22:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135743">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
نیویورک‌تایمز:  دسته جدیدی از جنگنده‌های F-16 و F-35 از پایگاه‌های اروپا در راه خاورمیانه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/135743" target="_blank">📅 21:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135742">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وقوع انفجار در اربیل عراق
🔴
هنوز جزئیات بیشتری درباره علت انفجار یا تلفات احتمالی منتشر نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/135742" target="_blank">📅 21:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135741">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
شبکه کان اسرائیل:  در حال حاضر، ایالات متحده می‌خواهد اسرائیل را از دور جدید تشدید تنش‌ها دور نگه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/135741" target="_blank">📅 21:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135740">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb133ceefe.mp4?token=cWS-sBaiZAeg56ShTRbpwPYzMzC1-i5QSLJvGV2q3INTu2IUxv3174YSxiwuhAivxb1fMqv74eWU4JH6xBJ6joYXJHeTkLOQTigK9iGF2-QGTd-Xx_JWrojW98jtlukLlKwhdYa-KTwuPpGtU9SnCPE5X6jhNoEYIRrsKaPhFXsY3BpkZI_WPE4oMfeVO8krRaT69CGrtXNxhMaixIcrGvamLupHvgRsKz64w7g4yV46Hq4IVlPHBd-LE32upvU8f4bzVUb094WarL-lXyoL-W9jcyNBE1yUh3w3PHTZl_feL30yZjQdpknf8y5RaJHbMVATuFjCEbxO2bhgozxrwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb133ceefe.mp4?token=cWS-sBaiZAeg56ShTRbpwPYzMzC1-i5QSLJvGV2q3INTu2IUxv3174YSxiwuhAivxb1fMqv74eWU4JH6xBJ6joYXJHeTkLOQTigK9iGF2-QGTd-Xx_JWrojW98jtlukLlKwhdYa-KTwuPpGtU9SnCPE5X6jhNoEYIRrsKaPhFXsY3BpkZI_WPE4oMfeVO8krRaT69CGrtXNxhMaixIcrGvamLupHvgRsKz64w7g4yV46Hq4IVlPHBd-LE32upvU8f4bzVUb094WarL-lXyoL-W9jcyNBE1yUh3w3PHTZl_feL30yZjQdpknf8y5RaJHbMVATuFjCEbxO2bhgozxrwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه کان به نقل از مقامات ارشد اسرائیلی: ترکیه تهدید کرده بود که در صورت حمله نیروهای کرد«گروهک های تروریستی» به خاک ایران به عنوان بخشی از عملیات زمینی به رهبری موساد با هدف سرنگونی رژیم، از ایران پشتیبانی هوایی خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135740" target="_blank">📅 21:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135739">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
منابع الحدث:وزیر کشور ایران فردا در اسلام‌آباد با مقام‌های ارشد و رهبران پاکستان دیدار خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135739" target="_blank">📅 21:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135738">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
انفجارهای مهیب کویت را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/135738" target="_blank">📅 21:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135737">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
کان نیوز به نقل از دو مقام اسرائیلی مدعی شد اسرائیل ممکن است تحت سه سناریو به حملات علیه ایران بپیوندد:
اگر ایران به اسرائیل حمله کند، اگر اطلاعات اسرائیل تشخیص دهد که ایران در حال آماده شدن برای پرتاب موشک یا پهپاد به سمت اسرائیل است، یا اگر ترامپ رسماً از اسرائیل درخواست مشارکت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/135737" target="_blank">📅 21:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135736">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
نیویورک‌تایمز به نقل از یک مقام اسرائیلی: واشنگتن تصمیم گرفته است هواپیماهای سوخت‌رسان بیشتری را در پایگاه‌های اسرائیل مستقر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135736" target="_blank">📅 21:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135735">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
کانال ۱۳ عبری : پیام ترامپ به کشورهای حاشیه خلیج فارس: اگر ظرف این هفته آتش بس حاصل نشد، برای تشدید تنش با ایران آماده باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135735" target="_blank">📅 21:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135734">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری/وزارت خارجه قطر: پیشنهاد جدید آتش‌بس را برای ایران و آمریکا فرستادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135734" target="_blank">📅 21:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135733">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
الجزیره مدعی شد: خبرگزاری رسمی اسرائیل به نقل از منابع اسرائیلی و آمریکایی گفته که واشنگتن به اسرائیل اطلاع داده است که قصد دارد حملات علیه ایران را در روزهای آینده تشدید کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/135733" target="_blank">📅 21:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135732">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvxUFBwJaNRjtSDlX4mGUErXg4LC0SubmOuSxfsl5pW_wyUiPQ-5vwSODedbuLBOP72pKZzDqatvFBF_8S695-H0WJzbhfQ8wAJZTy946x6HYNMvhjQZE0i5i4zoPS24oP7pZyHfMa1Szq2d5Oxjd8WMvTH9NZ-w4oSOS0f6DG8zsfBhMMao5pPqFnh_Sh_zMaCYNkZ-jlxwA-paEm3s3LmrMg2wuIwiUFcg5_Iqudf__rUJvIph4gj3YY9Sd1CbB3rb0LytjctdU7X8LMP-PP04OJMHgf3IonHPakUdHFbIhzPFdiwVoH-RLlfRVSq9SuavKwqxtXSbfcyvDQhfYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیژن مرتضوی و تام کروز قبل از شروع فینال جام‌جهانی در ورزشگاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135732" target="_blank">📅 21:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135731">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
خبرگزاری وای نت: انتظار می‌رود تعداد هواپیماهای سوخت رسان آمریکایی که این هفته وارد اسرائیل می‌شوند از دوران جنگ پیشین نیز بیشتر باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/135731" target="_blank">📅 20:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135730">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: ممکن است آمریکا از اسرائیل بخواهد به کارزار نظامی بپیوندد
🔴
برآورد اسرائیل این است که ایران طی روزهای اخیر در حال بررسی و بحث درباره این موضوع بوده که آیا به اسرائیل حمله کند یا نه، اما تاکنون هیچ تصمیمی در این‌باره گرفته نشده است.
🔴
ارزیابی دیگری نیز حاکی از آن است که ممکن است آمریکا از اسرائیل بخواهد حتی در صورت عدم حمله ایران، به کارزار نظامی بپیوندد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135730" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135729">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری /
شبکه 14 اسرائیل
:
ایران به دنبال یک حمله زمینی به پایگاه‌های آمریکایی در کویت است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135729" target="_blank">📅 20:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135728">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نیویورک پست: ترامپ در دفاع از جنگ با ایران به کشته‌های ویتنام اشاره کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135728" target="_blank">📅 20:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135727">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
تسنیم: گزارش‌ها از شنیده شدن صدای انفجار در استان سلیمانیه اقلیم کردستان عراق حکایت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135727" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135726">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فوری/وزارت خارجه قطر: پیشنهاد جدید آتش‌بس را برای ایران و آمریکا فرستادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135726" target="_blank">📅 20:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135725">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزارت خارجه اردن اعلام کرد کاردار سفارت ایران در امان را احضار و پیام اعتراضی این کشور در خصوص حملات موشکی را به او ابلاغ کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135725" target="_blank">📅 20:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135724">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وزیران امور خارجه عمان و اردن نسبت به احتمال تشدید درگیری‌ها و وخیم‌تر شدن اوضاع در منطقه هشدار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135724" target="_blank">📅 20:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135723">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rptLhJn_GHwKElnwuBRTwlnfcYUkNNMBW1RtOdRRntkncA0wjSCtxM44C4UUXBl1TOxMWJ204bhJSpBSm3g-CxTCB1Mf_3MWfTdlPnXv41AszM6F8FwOOWbp0W60pfb_j7yLZmtN_83F0ye-duMsWjY5bY53xOnjEryhRhlGlcVsiNhsTB_LEzX1nrzM5f3pQRPCUSIWFWCViPo8j5eNvh2MAVIRvXPR_aYOsInTBmUWdcZClS0sL8nwy9VHXSuw5iWgQ84m96EUaFdLKEp7g4FSqPwVJmQjwCU2qz6cxfEhcHegAjDnbSdV11hBp-f2TPykncZ76GewdNp-kPrczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کویت اعلام کرد که نیروگاه برق الصبیعه برای دومین بار در دو روز توسط سپاه پاسداران انقلاب اسلامی هدف قرار گرفته است که منجر به آتش‌سوزی و اختلال در چندین واحد تولیدی شده است.
🔴
تیم‌های امدادی در حال تلاش برای بازگرداندن عملیات هستند، در حالی که مقامات می‌گویند شبکه ملی برق همچنان پایدار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135723" target="_blank">📅 20:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135722">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا و جوزف عون، رئیس جمهوری لبنان درباره اجرای توافق موسوم به «چارچوب» بین بیروت و تل آویو که در فضای داخلی لبنان مورد انتقاد است، دیدار و گفت و گو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/135722" target="_blank">📅 20:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f004577c.mp4?token=HTho3PVvSs3MRgmZcFqh-IFlwizU12S1YarGng_SSGEgbnZ4AY2NnDOef53eFeTjmyPf9f4o0rzBrq-pI1dSFkPFiyCFbg6qRpl3-yYB7kQKTx9WbJrBQrCCQ4jW06wl-iAKM8s8GtPNee5QqH-xfLyF_Fmpu7bivJSxuQaDRui3owtfTUz5SBQSzLTJQZp3azT84Yt3mXrKyPQaCH-Rvs0xBH78Uehk8NdUG7bZij-jRKgWn2rjZeAeHF-721Ji5hh7gKhErwKOqjp3lyRyRpTUcVqUIY002n5of0230PoW3gHY8cuZjXMTYKMVegp98uDnMtc3Oso7htFvIw9ycA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f004577c.mp4?token=HTho3PVvSs3MRgmZcFqh-IFlwizU12S1YarGng_SSGEgbnZ4AY2NnDOef53eFeTjmyPf9f4o0rzBrq-pI1dSFkPFiyCFbg6qRpl3-yYB7kQKTx9WbJrBQrCCQ4jW06wl-iAKM8s8GtPNee5QqH-xfLyF_Fmpu7bivJSxuQaDRui3owtfTUz5SBQSzLTJQZp3azT84Yt3mXrKyPQaCH-Rvs0xBH78Uehk8NdUG7bZij-jRKgWn2rjZeAeHF-721Ji5hh7gKhErwKOqjp3lyRyRpTUcVqUIY002n5of0230PoW3gHY8cuZjXMTYKMVegp98uDnMtc3Oso7htFvIw9ycA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کد عجبب عراقچی
‼️
🔴
مجری: آتش بس با نظر آقا مجتبی هست؟
🔴
عراقچی: این چایی
دکوره
یا برا خوردن؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/135721" target="_blank">📅 20:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135720">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
اتحادیه عرب تحت کنترل عربستان خواستار تنش زدایی فوری میان واشنگتن و تهران است و از هر دو طرف می خواهد به مذاکرات بازگردند و از تشدید بیشتر در منطقه جلوگیری کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/135720" target="_blank">📅 20:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135719">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkwgKebO1nxo4DDT7AVUPbdadVk26ECSavZzgpdS2YJObR0SpNX0SsFWLw7YBuCcLOlsu7A0Nz0AJCHYxL8td2FTxya3cEk5_ZuzkB5mENUj0KbJV8mtggAKxT7V5MAd8mlBA-A0JazgaynQ_V4Buy5o6K-xzynycNrVaU-rNmkIjDsk_RIR3PcPYgie-Ku_wsNn4a9DV5rOwi058bbI6eAWCOOiG1fuAwbY1i42P0IstduLWl9T7FwsH6SyQB5Rivon7ltcornej9CKzfNBuHpOF_FZ2WL05vjeV7rEcypLqFMGMrXLi-b3nPWZw4tISUIMmgM5DwDaamvM6tfC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امشب ترامپ جام رو به تیم قهرمان اهدا میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/135719" target="_blank">📅 20:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135718">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83cb4f4b3b.mp4?token=JzIBNMNuKJgjPxowB8EUOWUgufy6N7Gps8ApfWNqAYUgBv098PsjTpFHG7HfsqjD28tmUJ3Ck3hqIb0ob_Xo-kW37PKy2Ijhi3HbNhuXZgC37gPv1s_HMAoPX_Pxk09SZCrYLL1cSSwomArjDjzOt_wdIr9u-Gcr-oUaxC9or9BJJSiki5-HG8vTJu2t_lsbk6oCUOVgvQnFX7dTpvc3s16ihmFxs9FAGv6OKxPfXm4T7JQJNkepEa32VyJRK45_k7gN8cIx-rczWiYG41vZh09EHmw19YBeMa90rfMt3_C8EDz4lYDrhSY4JA6M6V87Hp6WFeEqG13bsMsizxvJ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83cb4f4b3b.mp4?token=JzIBNMNuKJgjPxowB8EUOWUgufy6N7Gps8ApfWNqAYUgBv098PsjTpFHG7HfsqjD28tmUJ3Ck3hqIb0ob_Xo-kW37PKy2Ijhi3HbNhuXZgC37gPv1s_HMAoPX_Pxk09SZCrYLL1cSSwomArjDjzOt_wdIr9u-Gcr-oUaxC9or9BJJSiki5-HG8vTJu2t_lsbk6oCUOVgvQnFX7dTpvc3s16ihmFxs9FAGv6OKxPfXm4T7JQJNkepEa32VyJRK45_k7gN8cIx-rczWiYG41vZh09EHmw19YBeMa90rfMt3_C8EDz4lYDrhSY4JA6M6V87Hp6WFeEqG13bsMsizxvJ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف حق جواد کاظمیان: من الان زن بگیرم که چی بشه؟
به بچه‌‌ای رو به دنیا بیارم که چیکار کنه؟
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/135718" target="_blank">📅 20:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135717">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d827bf4609.mp4?token=JQfuJ64VZM2kPqvhzrj1vsP1s4ebWW4qVazCFgvQ0JzbzQ3n48HfkML7Ac2dcfUib5r9-ZgWYTWM5k6FCiFOhX_AS8FQKHotfippAlmkptjQpUNvlesKctZz_WMWIkQC76ffpclCSeJIP8dBQAUQz8bDrH5_RnsEpDpHCtZxPzoA99zs9NVwrlO9jwU5KvLZLwvf9eCNaAtd2k8y2iIzaqzcow3sS8kDk0fMzNik0h9Opzq-H2e4Y0Bpmd1NPLJq5RCWCNuaPRb3ekRgZGmaf11jTqXftH3oK7e_KmLHV7FUPt3sjbJpfSSh8qEaG6PVnFCLhKKAh1qU5bu8Vf3yqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d827bf4609.mp4?token=JQfuJ64VZM2kPqvhzrj1vsP1s4ebWW4qVazCFgvQ0JzbzQ3n48HfkML7Ac2dcfUib5r9-ZgWYTWM5k6FCiFOhX_AS8FQKHotfippAlmkptjQpUNvlesKctZz_WMWIkQC76ffpclCSeJIP8dBQAUQz8bDrH5_RnsEpDpHCtZxPzoA99zs9NVwrlO9jwU5KvLZLwvf9eCNaAtd2k8y2iIzaqzcow3sS8kDk0fMzNik0h9Opzq-H2e4Y0Bpmd1NPLJq5RCWCNuaPRb3ekRgZGmaf11jTqXftH3oK7e_KmLHV7FUPt3sjbJpfSSh8qEaG6PVnFCLhKKAh1qU5bu8Vf3yqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
استدلال این هم وطن کاملا درسته که میگه سرباز آمریکایی سگش شرف دارد به کل جمهوری اسلامی و طرفداراش
🤔
هرچی از حرام زاده بودن طرفدارهای جمهوری اسلامی بگیم کم گفتیم.</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/135717" target="_blank">📅 20:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135716">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل به نقل از ایلی کوهن، وزیر اسرائیلی، گزارش داد نشست‌هایی میان اسرائیل و شماری از کشورهای خلیج فارس برای تقویت مسیری جایگزین تنگه هرمز برگزار شده است.
🔴
کوهن مدعی شد با ایجاد این مسیر، ایران دیگر نخواهد توانست از تهدید بستن تنگه هرمز به‌عنوان ابزار فشار استفاده کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/135716" target="_blank">📅 20:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135715">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-8HeoAfzvBspuEk0VaFapLM2N4NClRv1p0VuFJGFqpgLG8ev0YC_Ph-JmNh9XotQl4Kg70xzpcb5fKPL_BkwHFtBIo7Fn_MJt7_VCXLSoiqggdHLG4Jc-Xl7iywZJRLZTTSK5z3CJacks1jLxOP4HLZy8_X3IbRL3lMrd2j7PY0FO9W9Gi721C8f_HDLXF_lXKWvFuBM5-joJe06M967b-_R_FzbtfDoD88xC0TGtw7W91vap5OajHa5HwKlonFT4JQzlANi9TasnskiUNWbHkAzTuW7SLDcsfXEhQQR4TEpZm7Vtw2nwoz85ACwbnDxnTmgNsvwl4sk7-w5BNw0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیافه پزشکیان قبل ریاست جمهوری و دوسال بعدش
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135715" target="_blank">📅 20:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135714">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
رسانه عبری: تا نهم مرداد تخریب صدها ساختمان در دو منطقه لبنان تکمیل می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135714" target="_blank">📅 20:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135713">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF): کمی پیش، نیروی هوایی اسرائیل یک پهپاد را در منطقه مرز اسرائیل-سوریه رهگیری کرد.
منشأ پرتاب در حال بررسی است.
🔴
سیگنال‌های هشدار طبق پروتکل صادر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/135713" target="_blank">📅 19:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135712">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
فرمانده ستاد کل ارتش اسرائیل :
اوضاع ایران رو لحظه‌به‌لحظه زیر نظر داریم
🔴
سطح آمادگی‌مون بالاست و هر لحظه لازم باشه، آماده‌ایم دوباره وارد جنگ بشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/135712" target="_blank">📅 19:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135711">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff128e3610.mp4?token=aeEx5oU4yaR68FAh_JmyzrV7HOOwQeEs0T_P0JR2Hing6ZYNXGPU2wJL-DM18WXQYh2WHnhcbooxoKKoI6r8M1InSHo3f3Tn1-EznlmtHuxZ5CRAGDX4inbSXYxn8LT5QIrM9pbztnSEkv4ccNXPwqPjLfAkvYCFexAsZuTsPsfzWw_XOfTlaMP2-FNHZGqmzdlpdYAQmeIJRJ2wu_HP0UBJZgMAufDIJ9VX3UJwFLVtrkdchFrHjprt2DAfKR9k7FXpNmjOmyHQ6wyTnuTz755sdpddEzD8o5c93tph0OuBs_dfvRUZZ9FyIkRW8YHt5eOCzyS2SOXMMsNU7tjZwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff128e3610.mp4?token=aeEx5oU4yaR68FAh_JmyzrV7HOOwQeEs0T_P0JR2Hing6ZYNXGPU2wJL-DM18WXQYh2WHnhcbooxoKKoI6r8M1InSHo3f3Tn1-EznlmtHuxZ5CRAGDX4inbSXYxn8LT5QIrM9pbztnSEkv4ccNXPwqPjLfAkvYCFexAsZuTsPsfzWw_XOfTlaMP2-FNHZGqmzdlpdYAQmeIJRJ2wu_HP0UBJZgMAufDIJ9VX3UJwFLVtrkdchFrHjprt2DAfKR9k7FXpNmjOmyHQ6wyTnuTz755sdpddEzD8o5c93tph0OuBs_dfvRUZZ9FyIkRW8YHt5eOCzyS2SOXMMsNU7tjZwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کره شمالی: در کنار روسیه تا پیروزی نهایی ایستاده‌ایم
🔴
چوی سون هوی، وزیر خارجه کره شمالی در دیدار با ولادیمیر پوتین در کاخ کرملین، بر حمایت قاطع و بدون تزلزل پیونگ‌یانگ از روسیه در جریان عملیات نظامی ویژه تأکید کرد.
🔴
وزیر خارجه کره شمالی رسماً اعلام کرد که کشورش تا دستیابی روسیه به پیروزی نهایی، با تمام قوا در کنار مسکو باقی خواهد ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135711" target="_blank">📅 19:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135710">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
حمله ایران به نیروگاه برق حطین در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135710" target="_blank">📅 19:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135709">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
فرماندار جاسک: آب‌شیرین‌کن بونجی که در پی حمله موشکی آمریکا و اسراییل آسیب دیده بود، کمتر از ۴۸ ساعت پس از حادثه، امروز وارد مدار می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/135709" target="_blank">📅 19:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135708">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری / رسانه‌های عبری: ارزیابی‌های امنیتی اسرائیل نشان می‌دهد فرماندهی ایران دستور حمله به اسرائیل را صادر خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135708" target="_blank">📅 19:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135707">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
رئیس هلال احمر:  در تشییع میلیونی نه تنها یک فوتی هم نداشتیم بلکه شاهد چندین تولد نوزاد نیز بودیم :/
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135707" target="_blank">📅 19:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135705">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uNMZOLJ9WO2S0uVSL0F4eRs44vhR3EDKemhGLsXTxsPWFqt3z22uZ6yPA5vuzFNjvReNzecvehhm_Ck5RqF7FUoDrVIDZK2WoRs0OTTFUE4cwREHo8lXVQmQA8qgFWfYMiHsS8xfDkLCiAMqj0Z6in-rKxxu8cqb8iX54L9MAllr24oVlTKZiHyfxwS8WqU938gQAkxawLCsBOrAsa91y814UbMlAfOIOHhCN324TMEVtF_kN6z0LLjXsEirNfKp26Znz77Z1ZFOrpFC6q4C29bhWFqNMnUf60SkzmeRbLCnF7qSn6601j8ItWdvY3h0uhZCOTkKXZnb3T5jXEounQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/grWmE24n9SVeErMreeU9IHERupqdJxXTbVKCb5WIyeFLLkBrCWcP5eKBHQZLPwf-Vkjk3srxjoh0ih7MT1LfRlQVBoe6ICt40hJDZ3CGcgIA1hxVJ7G5c_GuRJ4qblQncoQJ2N3m_rYsCHyD5zcZsvHXHQcUHClp03wUb-iiunGLevJNeCbm0vHqjeHZPBCsbpHm9dAmNGFRCAuFtuAQfhWy3EDxr1F690z08X4A0D3sXiGYt7MpHhYI-oCZh1rdJNOtw3ojEW3OKNAt2IZcWB91xRjjElQFGsqb1n_4jMBiBTDTg0rg5czmQKO7Xw7FXGZbiGbcywqHfDDHqN1YUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از انهدام انبار مرکزی قطعات لجستیکی نیروی هوایی آمریکا در پایگاه هوایی العدید قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/135705" target="_blank">📅 19:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135704">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7091c7c4c.mp4?token=TeIz9GfpZmFKnC7tfJH0ZbyGxzxC4WE4LIj6b5ARltYOskN3sja-g8urEKz2_GE8AjpIDNMapX5nvFI95A1Vnxrq2x5FH0fYnZzqoxobIQHBt-__6IrSFKiNxwiVQfNnL42Jmqiufi3VUpVZtY3oIWf5jBQlgEOKQNfV0PraxY88pyUDUUp-LKGjWdPVf0-q8uLIEpsGr8DPOmpDbqr9rOTZj2qnytL2vWBW-VJOXsUK3tav3Y0HuKZR-gvOt6qznMeb6Nz8oU3soq2O2vxKBXd_qFHblHviqf05KsBdym2LgOBcGnLoI5-0Gm_rIa58EUM8ONM7roFykl4vh4z4ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7091c7c4c.mp4?token=TeIz9GfpZmFKnC7tfJH0ZbyGxzxC4WE4LIj6b5ARltYOskN3sja-g8urEKz2_GE8AjpIDNMapX5nvFI95A1Vnxrq2x5FH0fYnZzqoxobIQHBt-__6IrSFKiNxwiVQfNnL42Jmqiufi3VUpVZtY3oIWf5jBQlgEOKQNfV0PraxY88pyUDUUp-LKGjWdPVf0-q8uLIEpsGr8DPOmpDbqr9rOTZj2qnytL2vWBW-VJOXsUK3tav3Y0HuKZR-gvOt6qznMeb6Nz8oU3soq2O2vxKBXd_qFHblHviqf05KsBdym2LgOBcGnLoI5-0Gm_rIa58EUM8ONM7roFykl4vh4z4ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: آرژانتین امشب قهرمان جام‌جهانی میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135704" target="_blank">📅 19:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135703">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa71ce2aae.mp4?token=lXI3OnHz5jYEXJvIOXoQjV9La5jivLRfNjYnVYnR7HtYHFlfyeul0P9Z79DNrgvrp6MqiumlsAqM416thckTtr_qF1B2ommv-c3Rs0rfF63XQvUTmBVIpqYHb4gIV38APm5XnefME-LV0j3K1nrOTk1ya13e8zysihAFFmkOz5RIYDWHL2A1B3Tg4sjHv3h3CcsWjIwn8VssS5Wnd4J-Mgo00FogUYKk1zIDvuhnTZ9SRf4xEqjRVJepCbLyd02YRg6v5u7jHNLqtLa3HSD-nOCjg-21rcvsRR46oR9X4XRN9hmuU-kl7NgScpRJ6ZahFudgQfZLux96y62B3cS30g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa71ce2aae.mp4?token=lXI3OnHz5jYEXJvIOXoQjV9La5jivLRfNjYnVYnR7HtYHFlfyeul0P9Z79DNrgvrp6MqiumlsAqM416thckTtr_qF1B2ommv-c3Rs0rfF63XQvUTmBVIpqYHb4gIV38APm5XnefME-LV0j3K1nrOTk1ya13e8zysihAFFmkOz5RIYDWHL2A1B3Tg4sjHv3h3CcsWjIwn8VssS5Wnd4J-Mgo00FogUYKk1zIDvuhnTZ9SRf4xEqjRVJepCbLyd02YRg6v5u7jHNLqtLa3HSD-nOCjg-21rcvsRR46oR9X4XRN9hmuU-kl7NgScpRJ6ZahFudgQfZLux96y62B3cS30g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آبادان پس از برخورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/135703" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135702">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4557e032e.mp4?token=pjq4pQguuUh2iWfHpVhYON7ECONjDdQBNfxWtro1lZib-you52IvdVn5yqXFFfI15DJMhd6nvft14zb3HsHM_eyITGMUSjILEaHdSxCM9hR7BFxGHwLEy-RutYXZsxC2lNy2iZ4atuJPgkdzcE15Pkt4DULDAAOvoreiKa72G-6cG-4I7b-uEhDT1KcEYs3SZELBc8Ud-sj-WyPASfSutxWI5PDGBaf2NHS2lcsosdinSTA_VO6MySiVgOeHcMNdLRpVTGJL5OGsoLCTf0O0-saG7Yii_LGOsBi3ox1GsDzOUlxuaEcQaNV0IiMOkkyWJ1OXr0QPy4asOF3k4Ym4sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4557e032e.mp4?token=pjq4pQguuUh2iWfHpVhYON7ECONjDdQBNfxWtro1lZib-you52IvdVn5yqXFFfI15DJMhd6nvft14zb3HsHM_eyITGMUSjILEaHdSxCM9hR7BFxGHwLEy-RutYXZsxC2lNy2iZ4atuJPgkdzcE15Pkt4DULDAAOvoreiKa72G-6cG-4I7b-uEhDT1KcEYs3SZELBc8Ud-sj-WyPASfSutxWI5PDGBaf2NHS2lcsosdinSTA_VO6MySiVgOeHcMNdLRpVTGJL5OGsoLCTf0O0-saG7Yii_LGOsBi3ox1GsDzOUlxuaEcQaNV0IiMOkkyWJ1OXr0QPy4asOF3k4Ym4sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مربی بی سواد: از نظام عزیزمون میخوام با عادل برخورد کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135702" target="_blank">📅 19:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135701">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/853ed69eaf.mp4?token=hhFa1wN4B4kKszi9s9ig-i2AnRfiTej1qcNnEnLPXDZj_4-xrEAbrOnE_A6fTifblZVCFagGQaAMSvcS1kU75acLfpiDyRoX9bsjj8js4uLWlEkh0IgQBSLosZfhcx9Pzetl5jznAP8hZh4HIL73FI4Hu23m4UEfIKyv3HXZm6U_gMd8hpYehEmCUl1pKGCOOpojGYX0v4xHgddASsLe-MD1GddbfKmg78O3bL8zCgr8dnd8QcY70mZxiAvhB03tvbimGevUZj8bYLywPxCq2pbYALdfRqeGCYSbmgKsnWMdKv94Qqi8m4SgZ-eQ_jucsz1yqK_MH_ZEJoA_C-V64A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/853ed69eaf.mp4?token=hhFa1wN4B4kKszi9s9ig-i2AnRfiTej1qcNnEnLPXDZj_4-xrEAbrOnE_A6fTifblZVCFagGQaAMSvcS1kU75acLfpiDyRoX9bsjj8js4uLWlEkh0IgQBSLosZfhcx9Pzetl5jznAP8hZh4HIL73FI4Hu23m4UEfIKyv3HXZm6U_gMd8hpYehEmCUl1pKGCOOpojGYX0v4xHgddASsLe-MD1GddbfKmg78O3bL8zCgr8dnd8QcY70mZxiAvhB03tvbimGevUZj8bYLywPxCq2pbYALdfRqeGCYSbmgKsnWMdKv94Qqi8m4SgZ-eQ_jucsz1yqK_MH_ZEJoA_C-V64A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جواد موگویی و عراقچی: تو ۱۸ و ۱۹ دی هیچکس فکر نمیکرد اون سیل عظیم جمعیت معترض به خیابون بیاد و چند هزار نفر کشته شدن
🔴
مشهد تو ۳ساعت سقوط کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/135701" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135700">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135700" target="_blank">📅 19:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135699">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
موشک سپاه به نیروگاه برق در کویت خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135699" target="_blank">📅 18:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135698">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94279117e7.mp4?token=rQB6fXWl8qZXpW17drYT9YEjMARdgIpS_ddHAsohyk5pFysbh9PNdDyhJq-XAcIEznoSxWK7c_mX7B0MrwUj5_N5X4sMJ5h4Qn91n2ufvpLtTvJsihtgOItFwX7T8HxuSDx3rRPt9itxLXFtOxOR5bXXP5-X181FlJIiXv4_Z5Qk1_aWZ31XughmBJK4Pexwv6i6d6EaET03hC-Y6Iqa60i8lo4UXNEp4-v1SQ2iDQm2dFrxYyDqw8tZlbuDrICe6dC8z4YBUtkCgCnh2v7_VIgO5yBrjyTT0WrhbTQJdUi9Czg1Q7HhbVfS9l-ZirF6BhWIOnNFXpnTVTCaT79zpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94279117e7.mp4?token=rQB6fXWl8qZXpW17drYT9YEjMARdgIpS_ddHAsohyk5pFysbh9PNdDyhJq-XAcIEznoSxWK7c_mX7B0MrwUj5_N5X4sMJ5h4Qn91n2ufvpLtTvJsihtgOItFwX7T8HxuSDx3rRPt9itxLXFtOxOR5bXXP5-X181FlJIiXv4_Z5Qk1_aWZ31XughmBJK4Pexwv6i6d6EaET03hC-Y6Iqa60i8lo4UXNEp4-v1SQ2iDQm2dFrxYyDqw8tZlbuDrICe6dC8z4YBUtkCgCnh2v7_VIgO5yBrjyTT0WrhbTQJdUi9Czg1Q7HhbVfS9l-ZirF6BhWIOnNFXpnTVTCaT79zpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک سپاه به
نیروگاه برق در کویت
خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/135698" target="_blank">📅 18:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135697">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0a2a1085e.mp4?token=AHflkUlb5Bs135J80HbHWWadUnrV09XrVfPrH-jRwmieulhvXUpPG_bexZmUCY5JSzY3P_njd9e9McVVz8tURA5Q8MgXh9ybRLlTYbPMRKZN01tSzOs5jfniz1TYVsNFXUhat7FSJzTAnKTntyJKzGBC-2wDLWSJzX-ecSTmCSeRmdTwVcQ8BBZdHih1wPMmjdxzwt4SCOdAt_Z7RDij2aHqb-J7kvSG0KUKUD_KMDOyT8XMDPxXrttHyU_b-G2GV3NFczU2wHLZqhPKT0HGl_XhhsuJplXbHZZiFZepiWSUKkbQDc5NALgYud6Cq8upk3h27E5YQq6qTBPCvCpO3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0a2a1085e.mp4?token=AHflkUlb5Bs135J80HbHWWadUnrV09XrVfPrH-jRwmieulhvXUpPG_bexZmUCY5JSzY3P_njd9e9McVVz8tURA5Q8MgXh9ybRLlTYbPMRKZN01tSzOs5jfniz1TYVsNFXUhat7FSJzTAnKTntyJKzGBC-2wDLWSJzX-ecSTmCSeRmdTwVcQ8BBZdHih1wPMmjdxzwt4SCOdAt_Z7RDij2aHqb-J7kvSG0KUKUD_KMDOyT8XMDPxXrttHyU_b-G2GV3NFczU2wHLZqhPKT0HGl_XhhsuJplXbHZZiFZepiWSUKkbQDc5NALgYud6Cq8upk3h27E5YQq6qTBPCvCpO3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند حامی حکومت:
آقا مجتبی رو اول امام زمان انتخاب کرده و بعد مجلس خبرگان رفتن ببینن امام زمان کی رو به عنوان نایبش انتخاب کرده. دیدن آقا مجتبی رو انتخاب کرده. اونام اقا مجتبی رو به عنوان رهبر معرفی کردن.
#دروغ
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135697" target="_blank">📅 18:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135696">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
قلعه‌نویی:
میگن مردم این تیم ملی رو دوست نداشتند ولی همه رستوران‌ها و سینماها با بازی‌های ما پر می‌شد و ۶ میلیارد نفر اخبار ما را پیگیری می‌کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135696" target="_blank">📅 18:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135695">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNsisjYDofhKdPFJx16BvFk5sHKq7CmEyGnFPpdPZi52rH5Fq-GY2xSH6Cxk0yms5OBtmafs7DLmMF30NHnB_sg2ObHqiM4OH57rtJP6dR3_eNxVgUlVfoBd-Wlx6RtKwq7anfaBbdkBcWLfNRJDk-UJxmOt1KhZMj3rXpcDAKqxiN5q6gjjShEOPtidPzxp1aKjfZLLBjY-zZCVQFsvp8Rqt5mbZACfU5XoowEUqR8pB9kJDRZBsouzFgPTzqlXmh5yEX7J8KqS-O0ghxu6IelrNqHQD_saXZq1j1TJF4SKRlO5MscH5vn5DbirPXvXJbsmusMK4wz5JR0h1lH97Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهاجری: بعضیا الکی الکی کشور رو سر تنگه هرمز به جنگ کشیدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135695" target="_blank">📅 18:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135694">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tX70GNRhx2qnP4cjkfG7mLhY24R_JnBuu_lQExJOEJ50aHy3tcgFzlkNcD55CEj-AsJGfLS02pJaXrcHxLnlRJilUqzQCkEaRdFNiFDbQySNDPjMuRE6qA4hsJdHifOwdRn3dCcH11IX7QdybZM7wo5lNSWzh56WkoZ6P8UgIXFRORr9Pv4TQ_8cIESZCGNK2UGCVRES7AkDdp0KdhVMeF1Wk3THZOPBn2FbXzlS8sc38GGwQJF4h0X2sOkfzlUXY9EpJ1DCItoWgGA6peIWs-Eo2MgfW_5ShDlFKL0_-FOk8_TzDkLstttyJreUp6MK6kW4zww2galL9qobpTttqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکونومیست: عراق به‌دنبال نزدیکی بیشتر به آمریکا در برابر ایران
🔴
اکونومیست نوشت نخست‌وزیر جدید عراق انگیزه شخصی برای حفظ روابط نزدیک با دونالد ترامپ دارد؛ در عین حال، جانبداری قاطع‌تر بغداد از آمریکا در برابر ایران می‌تواند مزایای اقتصادی گسترده‌تری نیز برای عراق به همراه داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135694" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135693">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
تندروهای جنگ طلب تا ایران رو به غزه تبدیل نکنن بیخیال نمیشن، یه مشت عقب افتاده ترسو عصر حجری
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/135693" target="_blank">📅 18:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135692">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
گزارش‌ها از ورشکستی هتل‌های کیش
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135692" target="_blank">📅 18:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135691">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
کریس رایت، وزیر انرژی آمریکا:
ما در حال حاضر روی تضمین عبور نفت و گاز از طریق تنگه هرمز کار می‌کنیم
🔴
ترامپ همواره به دنبال راه‌حلی دیپلماتیک است و می‌خواهد این موضوع را با توافق به پایان برساند.
🔴
اگر ایران برای راه‌حل دیپلماتیک آماده باشد، همین راه‌حل خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/135691" target="_blank">📅 18:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135690">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcNNz7G5S7uoiEFAGyOeTCwE5hLojDjfK2-GwLiMe7TIxpukhy-h1ERGVVNmnNuFZTGpVWIuD23mobPDKMBpo_PHagVRJjp8pHSt0tMjGAH4Ga6Rj_ILHPrLsrpBn-5vVZ8NoV8LwDxMGpJi1kFnY4Q9n5h5xnri3Y0lgLpJE5e9NcLURYWPWoUlysJ26hwmZ5FZWWddoBZC16l8RRjLV6ojje-XNhOSGZLORl91dBCBhIY5xwTMm8Wt6Dw5oMxWZXSVzKzBkuDHORZhVAmOHBHNlrzKyMJ6Iac2rPx1W1pj9lcTxxQtbTH4H8UZohh-2Y9jpwruISvK0z_czZCdrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بهای تحمل جنگ به جنوبی‌ها داده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/135690" target="_blank">📅 17:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135689">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4e70751a.mp4?token=u94fZ38TygZpGzEsKA6I4woAwwWM_c45-DwKr10ws0EjD3jP4qKPokUu1ZLJuCzAhH0Ks7wvGpd4OTCftKyja_kbTSjTG63iTVInQ1VpDfx_cBafpEfD0-QVlBJXTYa3zHyhoxFIsO5PY9W8gQmJ36si-MU78i3XV9ncT9PimWpqXKvJIc9qZqHhFn24hQFV_4CJaC-Lh1wsMmrJntOIFp2f3hTVEhX-c-aXgC2erVvIN8Fq0gJvcci4cESdpSYRiKsdAz0Hh6fAbB_1O5QiXO-kT-C8stuSalp1Tfspiq38blLJ5kZOhtAg0Ozy8qFmIbMWbA4U9jcKiTQj6DL4QmJN2w0x5xgXtLomaEoxHkjv6r0DzmaMPQmDSjsTy81zJUlpAuhW7EbYIeWgs7DgL-q6hADeFT6hrVDXgBpySqfi99FkXMVNeLLVxGrG5wdfiil_snVQW6SYg5irXoz_oAlmkRg5w1gj4xta2afvmg5ncWnpZ2TDq4fAvRfAbscS0Me_HfsftKLgt21D9UM_c6Y5fu0SjQSNo4du9_gn4-AZJFgWXrDKTMUVOZOrqYz44aAviS4P4osFkU8RmHBmjk_eCT58MYFotnX-l4CcMqhdXkNw_ozNHMDGBXGOtmdAMvrYte_Q_sAmUnD_uedLEF5aRgtC1Jb2gJJaL6TN3JI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4e70751a.mp4?token=u94fZ38TygZpGzEsKA6I4woAwwWM_c45-DwKr10ws0EjD3jP4qKPokUu1ZLJuCzAhH0Ks7wvGpd4OTCftKyja_kbTSjTG63iTVInQ1VpDfx_cBafpEfD0-QVlBJXTYa3zHyhoxFIsO5PY9W8gQmJ36si-MU78i3XV9ncT9PimWpqXKvJIc9qZqHhFn24hQFV_4CJaC-Lh1wsMmrJntOIFp2f3hTVEhX-c-aXgC2erVvIN8Fq0gJvcci4cESdpSYRiKsdAz0Hh6fAbB_1O5QiXO-kT-C8stuSalp1Tfspiq38blLJ5kZOhtAg0Ozy8qFmIbMWbA4U9jcKiTQj6DL4QmJN2w0x5xgXtLomaEoxHkjv6r0DzmaMPQmDSjsTy81zJUlpAuhW7EbYIeWgs7DgL-q6hADeFT6hrVDXgBpySqfi99FkXMVNeLLVxGrG5wdfiil_snVQW6SYg5irXoz_oAlmkRg5w1gj4xta2afvmg5ncWnpZ2TDq4fAvRfAbscS0Me_HfsftKLgt21D9UM_c6Y5fu0SjQSNo4du9_gn4-AZJFgWXrDKTMUVOZOrqYz44aAviS4P4osFkU8RmHBmjk_eCT58MYFotnX-l4CcMqhdXkNw_ozNHMDGBXGOtmdAMvrYte_Q_sAmUnD_uedLEF5aRgtC1Jb2gJJaL6TN3JI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهدی مطهرنیا:
تجزیه ایران به هیچ وجه شدنی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/135689" target="_blank">📅 17:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135688">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
انفجار مجدد در آبادان
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135688" target="_blank">📅 17:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135687">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
تحلیل آینده طلا و دلار
اینجارو داشته باش و سود کن</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/135687" target="_blank">📅 17:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135686">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری/رویترز: حملات حوثی‌ها و ایران به عربستان، پاکستان را به شدت از تهران خشمگین کرده و ممکن است پاکستان به درگیری عربستان و یمن کشیده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/135686" target="_blank">📅 17:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135685">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt60_GKT0FHQTmOZ_LwH4VfAr29QB3lIf7rVAMTYejmWuMGxxm1AB6IglKbDvYZaIQgniJTODLe_nAhzqvc2DthwTYaEl9A2EUy1wj4yJpKBWOJU_w6tx0rutfoyCKMdTVdVr-TwB9az8SUBPmQiw_TTOefzpL7oVBuM4n0MnxzJy7AKBttZweqahRuR6kOQSF3_k2Poc5kQBk6NG4szZe2pCXbhpgOcJ4qCL4j7Muf7INGBm8rEQ91EHcfruufE-Jy0Jx-bxDQW2EEDzbzoR5hNfRZdbXiXesGmczu6Dhy8VoaAMjZBsgsehQCleEvrq_5ZCOhOMUIFTe2CjgdPIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دفاع اسرائیل کاتز:
اگر جمهوری اسلامی به اسرائیل موشک شلیک کند، ما با قدرت و بدون هیچ وابستگی یا شرایطی به آن ضربه خواهیم زد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/135685" target="_blank">📅 17:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135684">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0fb2383c1.mp4?token=IQjzaB0mEQIZ8GCgjh4FGTspjQjPkk1NaqYP-ZA0XpMAuY1LyB-s6_QywdpQ9Ry1YH4toPgo9BSax12RFv3hiQTDhe-987AbMsKHD1UK2g7rAp20f-huZ66B3KIM-a5hKtgve2oXzOgWYrQiw9KES1O2QrZrj0Ga_o8DoqvUHd2wvVl6JU8URwdtLetSNTs0fDPgqkUsJFXevwaR2hNPq8b8m8KPIn_5BxOHRjAtaXvKVORQxTr-TwF6s7ew92GTC4R5YZks5WwmmaF-BC4WxlojnhQyA2sr6zWYVKP5XdoZSVIXqqB8M2vue3vSsYOVtthvI3DIq7TGx8sfg4BeUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0fb2383c1.mp4?token=IQjzaB0mEQIZ8GCgjh4FGTspjQjPkk1NaqYP-ZA0XpMAuY1LyB-s6_QywdpQ9Ry1YH4toPgo9BSax12RFv3hiQTDhe-987AbMsKHD1UK2g7rAp20f-huZ66B3KIM-a5hKtgve2oXzOgWYrQiw9KES1O2QrZrj0Ga_o8DoqvUHd2wvVl6JU8URwdtLetSNTs0fDPgqkUsJFXevwaR2hNPq8b8m8KPIn_5BxOHRjAtaXvKVORQxTr-TwF6s7ew92GTC4R5YZks5WwmmaF-BC4WxlojnhQyA2sr6zWYVKP5XdoZSVIXqqB8M2vue3vSsYOVtthvI3DIq7TGx8sfg4BeUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله قلعه نویی به علی دایی
‼️
🔴
قلعه‌نویی درباره ساعت معروفش :
وقتی میام ساعت میندازم و کت‌شلوار می‌پوشم، شما باید بگی به به چه مربی خوش‌تیپی ولی شروع کردید به مسخره کردن!
🔴
حتما باید یقه باز بذارم و زنجیر طلا بندازم؟ (کنایه به علی دایی)
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/135684" target="_blank">📅 17:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135683">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9286ee216.mp4?token=O9OnVdAyptrgIsN5fnP8ePt0LNIMY6oGbgvW9YSg5Pqr3MuzTpxqnjoYcBsYVxj7l6GycSIOeAJPfiZWH1rqSrwIfSC8zveluMeb68nz9LOX6FlvP0dkbfxCXXV0Y-JAEta9I82LKnpWaenw5u27eeGOvc8yTndDZCkWdCypTTLEOu8t3UMP32-ImOMYmoqpvXhs6x3ZATZQDAiDFpE5N4gEoN2kUlKu6JZ6ghxuDdrMlufWDj2G-wble8KZXySm3aorQwc2RmWoNv13b7ONUkZ_9YwRgj4r7MMfh2yk8yly22nJo2MI2Gn_shgfbTHoCBIeUCwyE9CUC9S-n8yy6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9286ee216.mp4?token=O9OnVdAyptrgIsN5fnP8ePt0LNIMY6oGbgvW9YSg5Pqr3MuzTpxqnjoYcBsYVxj7l6GycSIOeAJPfiZWH1rqSrwIfSC8zveluMeb68nz9LOX6FlvP0dkbfxCXXV0Y-JAEta9I82LKnpWaenw5u27eeGOvc8yTndDZCkWdCypTTLEOu8t3UMP32-ImOMYmoqpvXhs6x3ZATZQDAiDFpE5N4gEoN2kUlKu6JZ6ghxuDdrMlufWDj2G-wble8KZXySm3aorQwc2RmWoNv13b7ONUkZ_9YwRgj4r7MMfh2yk8yly22nJo2MI2Gn_shgfbTHoCBIeUCwyE9CUC9S-n8yy6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اعلام کرد که یک پهپاد انتحاری لاکاس متعلق به ایالات متحده را در جنوب ایران سرنگون کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/135683" target="_blank">📅 17:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135682">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f376bb044e.mp4?token=O1l4ry1CLKLHic7XX4OsvMD4fornqGaZ8R29xXeKWYoMMQOIugmW5lcrwFHf0U1iZ8KVXB1Df0aFCmhB_iYHjK-wRCKCWBhPc6s76NQLLop-KSXFUEpW3Aohh97l8MtgEBCDso7fY1cquh3DZj3_LC_K2KnCBDfe9kCVXHBNkmX6UxzK_sjaDQTiqyJvqppWCFTZjxDO7RYM0swuTQEVgYNchtySDkqjTXADHvfZtVMfThi_UbEQSbYlIVtVg91Ro_WAgSTLOo71oE_67OYUhm18ftm7cYz6JptJ6-p5eq4b1HJqKe-r3uG8ar9oNpRadqO2dA-jJEL0yLlTmbLdAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f376bb044e.mp4?token=O1l4ry1CLKLHic7XX4OsvMD4fornqGaZ8R29xXeKWYoMMQOIugmW5lcrwFHf0U1iZ8KVXB1Df0aFCmhB_iYHjK-wRCKCWBhPc6s76NQLLop-KSXFUEpW3Aohh97l8MtgEBCDso7fY1cquh3DZj3_LC_K2KnCBDfe9kCVXHBNkmX6UxzK_sjaDQTiqyJvqppWCFTZjxDO7RYM0swuTQEVgYNchtySDkqjTXADHvfZtVMfThi_UbEQSbYlIVtVg91Ro_WAgSTLOo71oE_67OYUhm18ftm7cYz6JptJ6-p5eq4b1HJqKe-r3uG8ar9oNpRadqO2dA-jJEL0yLlTmbLdAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روایت عراقچی از لحظه اصابت موشک به بیت رهبری در ۹ اسفند: به آقای حجازی گفتم آقا اینجان، گفت نمی‌دانم
🔴
با آقای حجازی در بیت جلسه داشتم که ۳موشک اصابت کرد و از زیر آوار خودمان را بیرون کشیدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135682" target="_blank">📅 17:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135681">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">علی خامنه‌ای رهبر پیشین جمهوری اسلامی، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135681" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135680">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
پرس‌تی‌وی: گزارش‌های غیررسمی حاکی از آن است که صدای انفجارها مجدداً در کویت شنیده شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135680" target="_blank">📅 17:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135679">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b003e9e7d1.mp4?token=vPiTyPJVnvuD2Bt9vpdWyhJ2oslABsNvVN61g0yshccYWgUqGmM1ciHLSBSIi12QR7T3F9qQKD_poz7VFkEIhqez1Lg1pV7dH6f4W8gjP4fhRSkD6uXxb6WqIWXGvL74hAO_ENBkDz_nXMvgYXXJ4QJUkW4KW1fbPy9Y1d7kV6rF5ioh485Cp-e6MulAeFElxmoPa56FjeAc6nr9Iepi-honK-8vZQw5nl3mRx-6XJ-PdIQywMZLvEAwlFGkhp_wSc6rDJNtXmbBMCoX4HUO_zyiV3ORYtQy52jjXxtecdNutOUhPb8DFH-T7J3P6xYjdPOfk1_4QwAP4e9DV39BfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b003e9e7d1.mp4?token=vPiTyPJVnvuD2Bt9vpdWyhJ2oslABsNvVN61g0yshccYWgUqGmM1ciHLSBSIi12QR7T3F9qQKD_poz7VFkEIhqez1Lg1pV7dH6f4W8gjP4fhRSkD6uXxb6WqIWXGvL74hAO_ENBkDz_nXMvgYXXJ4QJUkW4KW1fbPy9Y1d7kV6rF5ioh485Cp-e6MulAeFElxmoPa56FjeAc6nr9Iepi-honK-8vZQw5nl3mRx-6XJ-PdIQywMZLvEAwlFGkhp_wSc6rDJNtXmbBMCoX4HUO_zyiV3ORYtQy52jjXxtecdNutOUhPb8DFH-T7J3P6xYjdPOfk1_4QwAP4e9DV39BfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از ایلات خروج یک زیردریایی موشک‌انداز ارتش اسرائیل (IDF) را نشان می دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/135679" target="_blank">📅 16:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135678">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری / چندین انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135678" target="_blank">📅 16:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135677">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوری / گزارش ها از شنیده شدن صدای انفجار در بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135677" target="_blank">📅 16:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135676">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
منابع خبری محلی در جنوب لبنان از حملات نظامی جدید اسرائیل در مناطق مرزی خبر دادند.
🔴
ارتش اسرائیل دقایقی پیش اقدام به یک انفجار مهیب در اطراف شهرک «کفرتبنیت» واقع در جنوب لبنان کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135676" target="_blank">📅 16:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135675">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ارتش: فردا قراره تو شرق تهران بمب های عمل نکرده رو منهدم کنیم پس اگه صدا اومد نگران نباشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135675" target="_blank">📅 16:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135674">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‌
👈
پلیس راهور فراجا: تمام مسیرهای آسیب‌دیدهٔ هرمزگان بازگشایی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/135674" target="_blank">📅 16:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135673">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری / چندین انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/135673" target="_blank">📅 16:48 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
