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
<img src="https://cdn4.telesco.pe/file/hPcx50AwDt5oNyv-C_yvlUfVjEgdqDRbv_QrwAAkl-mneZLe9IP0LG2O38v7EDn1w7TLvERJcewgzIAztRBXGIUEw0SkNN_zKHE9T6nLSD4UYEXRNJvk22yBrEIqzTdxaYKVt8GVghqnph7Na9fAyZ40luWZdggqdHtNXblQExWQdEe7k8zQlJQ-JCHCtByiDxwxcqOe65wWCMzs2-7rM5ce9AEtrkadXi7On-XvPzanoaoWX3mAZWZTxvY_FnWbSTTFtgOcoyzhuJhQ9XGWdiryG4HGnGPYX7MEqE_tcz1bFGwlag5Le3L01kxZ5urtmEnRTfg7NmTSdvQiF_EV0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 190K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 20:42:49</div>
<hr>

<div class="tg-post" id="msg-67682">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0FvGELUSCcSJpteQp36i9AOuDjVNmRyCsk-h5t1bGAJdqjsZH2uct_oWr5QuSPvwG8VUWXMloMpAbaGUChzW7ujZauxRDVJObKOqhF2fzd1gbsyYzhQuGw4Etu7zqP6p0XL8ZJKgNZv61fKsdZsdp9_3xvnkrNdBYafAFLbC05znSuPgK8sanJlvhuhC8lIdlfYV_ehssjG_VrCuc1f_OqkwhTkowW7KunxdbJFNzqW0LtosYVc_TN64l1Pm6m0EO8lgVrcxAn5BUlgE6D73UQd9AgUBeQHwmH-BeuHsuG7phG8AK7p5E9G0eIxq6K2tArKz59abPXUze0-oZ9NoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو، درباره ایران:
خاورمیانه در سال گذشته شاهد فعالیت‌های بی‌سابقه‌ای بوده است، به ویژه دو عملیات موفقیت‌آمیزی که ما علیه ایران آغاز کردیم.
اگر ما اقدام نمی‌کردیم، ایران به سلاح‌های هسته‌ای مجهز می‌شد.
رژیم تروریستی ایران ضربه سختی خورده است و سیاست ما کاملاً روشن است: چه توافقی وجود داشته باشد و چه نداشته باشد، ایران به سلاح‌های هسته‌ای دست نخواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/news_hut/67682" target="_blank">📅 20:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67681">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apScyXHgDXrS16eCcrMGyPbSIrVWRjwc5eKVpMUUR3JXcms9nvDebtKHAxRc39tIzm4TCTzrYeX758BGqxjXnFcJm6QiuYX08fePAPz24S5eq9j6DVgeRZQc-7BV46o0S8GJvPUDFq9zQqppgKYWsUSW3PFt6fN4JcxEviDwyo5d1Z89R4eyhTPRy5-BQ_CYVqQI0NVskDfSd1-Tsi6gcExg1CgwWjorMI_XhECtbVCitchf4Lov0iHQ-NZbEVxzJj7zFoaCmqPcwZKM4wjLudIrZ0gAf93mmVTRWoamWUx6OZZMejCI9u-yPUOzi74tOlWCnY3r_NYMcoJJ0O30qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید به نقل از مقام آمریکایی:
این تشدید تنش‌ها می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد، بسته به اینکه آیا ایران به حملات خود علیه کشتی‌ها در تنگه هرمز ادامه می‌دهد یا خیر
"ما قصد داریم آن‌ها را کمی تحت فشار قرار دهیم تا متوجه شوند که ما شوخی نمی‌کنیم."
@News_Hut</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/news_hut/67681" target="_blank">📅 19:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67680">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZY4oboMFvjLVqVP0pKIsDILWHEbuDjgIJFB43kSFNyI7jGg3SeW-YgGKXJYIoRdPeXZsomwzYuAOeGe5482s45BfENdzayk3NSHX5xD462daeZuQEj-Ct8TtdbQZe8A89am4lCbq41RYhG8M54M8vTf9nirgltVr5alAXtORDjtM2jxnXNaqu69f_JWHoKWbhN5HdwDCz1xL3rp4V8enRmJc00YaucezQeX3PD-kWQYM0BZO9Zbqv7gDGMG5krzKx3cnDddT7uRjhrIG7NMeD8_8Zdjz3it8m8EcagiuIW2-0iRhfbnSnP1J5hKypMd2Qk5mJ5FXL1rF0c8jRqXXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇮🇱
کانال 14 اسرائیل :
🏴
علی خامنه‌ای حدود 600 میلیارد دلار ثروت داشت؛
رهبر سابق ایران، علی خامنه‌ای، در حالی که تظاهر می‌کرد مثل فقرا زندگی میکنه، املاکی تو ترکیه، کوبا، مکزیک، ونزوئلا، سوریه، دبی، بریتانیا، روسیه، عراق، ارمنستان و صربستان داشت. همچنین مالک چندین هتل تو اسپانیا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/67680" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67679">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=hruGgHfNi21826GJqG_7lfAQX2bDWjjg3mijMbo_6M9Qtaph7Mo5iN1EzaPzFUgI6oLkJbXhogqhsRBMI_UI-thswvzUx14v6BQQ92pC65zs0z3Xpj-xtwu12tDdpCGgbW3lITMY2HrhvOY33GPoxwRMEKvnCYQDSOT6pJrLmmNk1qo_dc8md3d9u2VM6n8pV5h0NA5x3wPcJ4z9oj6LOz_QuengRfcyYKqQHv8AbBhvOSUc7bFbBXcOEtHLhSTVPuNj6mnpsAXrVHWKzeRzamRT2GN7dZ1h6kkMjBX7ZtM-JRrxtJV3STKyUGA8lHmxVm-wqn4kEdUAokf19rUXnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=hruGgHfNi21826GJqG_7lfAQX2bDWjjg3mijMbo_6M9Qtaph7Mo5iN1EzaPzFUgI6oLkJbXhogqhsRBMI_UI-thswvzUx14v6BQQ92pC65zs0z3Xpj-xtwu12tDdpCGgbW3lITMY2HrhvOY33GPoxwRMEKvnCYQDSOT6pJrLmmNk1qo_dc8md3d9u2VM6n8pV5h0NA5x3wPcJ4z9oj6LOz_QuengRfcyYKqQHv8AbBhvOSUc7bFbBXcOEtHLhSTVPuNj6mnpsAXrVHWKzeRzamRT2GN7dZ1h6kkMjBX7ZtM-JRrxtJV3STKyUGA8lHmxVm-wqn4kEdUAokf19rUXnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
علی خامنه‌ای در حسینیه امام خمینی، پیش از بمباران توسط آمریکا و اسرائیل:
آمریکا هیچ غلطی نمی‌تواند بکند (23 اردیبهشت 1393)
اسرائیل هیچ غلطی نمی‌تواند بکند (18 خرداد 1395)
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/67679" target="_blank">📅 18:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67678">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/277d837de0.mp4?token=FSC-fCBzdF5xLPb86Ic2hLt-Sr8P9kbpLecXY0zhNFcWG1oxV_0QeaFL7xmCiod2sirQhDIFvGHd7EyR4XrJWMgtdyeNExnVbOPbUBRgZllEV3yXTFDeKsqPavM1q68wOfLM3BwKSuR69IX9WoMOD6BNyoS1Vkrk6MD7lepDkr-ODcG2Y8cnma47SAmuas_5ctQoez0frwfo-uNdV_7YEDSAXw6HXFMyWKSoc_8DldKZsiTUNZ7SHPmNRrHe6MHCk88Qj9M71V6uBvVs3ehO-8YzLHAQ1ANbmPKH7U-wmOCT1HRMOfRZyaA4n-rV6n4zw-XrEqU4r5rkKppVRoZRhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/277d837de0.mp4?token=FSC-fCBzdF5xLPb86Ic2hLt-Sr8P9kbpLecXY0zhNFcWG1oxV_0QeaFL7xmCiod2sirQhDIFvGHd7EyR4XrJWMgtdyeNExnVbOPbUBRgZllEV3yXTFDeKsqPavM1q68wOfLM3BwKSuR69IX9WoMOD6BNyoS1Vkrk6MD7lepDkr-ODcG2Y8cnma47SAmuas_5ctQoez0frwfo-uNdV_7YEDSAXw6HXFMyWKSoc_8DldKZsiTUNZ7SHPmNRrHe6MHCk88Qj9M71V6uBvVs3ehO-8YzLHAQ1ANbmPKH7U-wmOCT1HRMOfRZyaA4n-rV6n4zw-XrEqU4r5rkKppVRoZRhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیده شده در آذربایجان غربی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67678" target="_blank">📅 17:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67677">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54718627b7.mp4?token=SEAsSICsKnB9YEoOL8vK4kjcYBfbt5dXnh59je0Sp8T9i_Lbq9vFqXgUqP2cwqgA47WAVSYxUdqAADVDrVoUG42E0LwU5gAUqb1eGzyjkEx3WVAewSh3oiKQVB1qLE-lKr3bSsWrcAXT4XifviFVbOwPZShMBiPd5inJZuDyvl7TQtM3IAFaAQMLf8og4OjEeXnU4N5h2egtZBillqY9y1PYnk7y-mGGfHUwtLz034RNqFO35R2_VXoP8YQMz1nTAcr3OzfLELGsmIFUXv95UHgGp3KbkKP33rir89dCRmFQ3ZGJbvQTwc5YHYnf3WVthefgzmcC3sJDigK02FsRmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54718627b7.mp4?token=SEAsSICsKnB9YEoOL8vK4kjcYBfbt5dXnh59je0Sp8T9i_Lbq9vFqXgUqP2cwqgA47WAVSYxUdqAADVDrVoUG42E0LwU5gAUqb1eGzyjkEx3WVAewSh3oiKQVB1qLE-lKr3bSsWrcAXT4XifviFVbOwPZShMBiPd5inJZuDyvl7TQtM3IAFaAQMLf8og4OjEeXnU4N5h2egtZBillqY9y1PYnk7y-mGGfHUwtLz034RNqFO35R2_VXoP8YQMz1nTAcr3OzfLELGsmIFUXv95UHgGp3KbkKP33rir89dCRmFQ3ZGJbvQTwc5YHYnf3WVthefgzmcC3sJDigK02FsRmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدئو جدید از حملات سنگین دیشب آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67677" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67676">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝑵𝑨𝒀𝑳</strong></div>
<div class="tg-text">دختر خانومای عزیز در این شرایط باید ترمز بگیرید که ایشون فکر کنن ترسیدید بعدش گاز بدید بیاید اینه بغل ایشون رو با مشت بشکنید
اگرم امکان خراب شدن ناخوناتون وجود داره سعی کنید با پا بشکونید
بعدش تلاش کنید فرار کنید اگرم نمیتونین یه اسپری فلفل بزارید داخل کیفتون بزنید بغل پیاده شد خواست دعوا کنه بزنین نوش جان کنه بعدش راحت برید</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67676" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67675">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03400665ec.mp4?token=IavZ4JrrdRjZF0XIgwClSuopoCXKVxhkxTi-_rp873lKd-V3vSJ7ERln7jXeAfNNJOT_a94BV5ooENRvmWkqB1NOHk7SLAvu51gn15E7yjIauzkINLYqzCBIh5i9mAGB-4xS0a_6YGbRM70k7fZiKjpBcfzPA72j_g4xOrmguDurTRBbOLJoIKcLSO0NPGMJrJCepYJAp9e42S32h0Hr0NwmUg1OJ4cKaNRhfvCfVqTC5DX0TvE0LwlqcCN9JxEQz72EwB_R9mMpIbc6GKlBUosC3eY-d9Nn99aKGTObxOaF2D63ZwiFcm1tHgpsJUUIth1WKMsKJ0Q1slat3MfykQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03400665ec.mp4?token=IavZ4JrrdRjZF0XIgwClSuopoCXKVxhkxTi-_rp873lKd-V3vSJ7ERln7jXeAfNNJOT_a94BV5ooENRvmWkqB1NOHk7SLAvu51gn15E7yjIauzkINLYqzCBIh5i9mAGB-4xS0a_6YGbRM70k7fZiKjpBcfzPA72j_g4xOrmguDurTRBbOLJoIKcLSO0NPGMJrJCepYJAp9e42S32h0Hr0NwmUg1OJ4cKaNRhfvCfVqTC5DX0TvE0LwlqcCN9JxEQz72EwB_R9mMpIbc6GKlBUosC3eY-d9Nn99aKGTObxOaF2D63ZwiFcm1tHgpsJUUIth1WKMsKJ0Q1slat3MfykQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر داشت از موتور سواریش فیلم می‌گرفت، که یه حرومزاده دلقک این بلا رو سرش آورد!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67675" target="_blank">📅 16:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67674">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RupB3tBmfu-IFHaNW_mstZDYGIaXuy3J2xrXe-K7-Vsxkcn6ZS7lVqSYNayDU6rcJodHiXcQs4hjyH9EmYjxCqEXvYROOjVJZ6r-RNO91IuRlQxC3mf4lYaM27ImztrqJFmsalk_4Ez4ZQJjY0w30UAcBC78phGCpq_niFDCR0vGDj5MLpf-r7aBIBZmFHgF32G6-iuZEwSHqpI4qLlcSYQLwlLivVU6-5AF0r7R2OoE0LFqqEk2Zqov6-gF4fePNzm2Fn0LLZYyFin_Tyb5AluhbOQAv1jM5kWyBZbLD-gW8WBz0iA9B_D-yiqdcqwR_sFNUlswem3EUI0pda_S-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هم اکنون گزارش زنده ترامپ از وضعیت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67674" target="_blank">📅 15:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67673">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=C-MdvsEP3R8NRDGHNlrFvWaK7-IqPqHjBmYfaielEGdhTZKyiAfnwN3tHxP_CJmEbMWBG-dFVqiDUpfGZwGQmqK0BMwrxQNyu6hx7JUU1Sbb88bglQMCU__jFScdOdWNe_diRRnjJ19oeWaTNdm0drrGeNEf_W6g1QlK2amglLai-APtHyNmzy1z_vVxZtjW_rCxWGrwXgLBMB6ceM215gGElNuG3jH8109OxXWemC-R3OqaY6KOb4HkvAt4QCC1FSikR_2wGNR-ZLNzd2sgRUhZzXUq8vLYoAMf8lxZpXy_em1TSjdt_D5jiUDXk8iBgarjAN0H5XhRZu14cQKogDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=C-MdvsEP3R8NRDGHNlrFvWaK7-IqPqHjBmYfaielEGdhTZKyiAfnwN3tHxP_CJmEbMWBG-dFVqiDUpfGZwGQmqK0BMwrxQNyu6hx7JUU1Sbb88bglQMCU__jFScdOdWNe_diRRnjJ19oeWaTNdm0drrGeNEf_W6g1QlK2amglLai-APtHyNmzy1z_vVxZtjW_rCxWGrwXgLBMB6ceM215gGElNuG3jH8109OxXWemC-R3OqaY6KOb4HkvAt4QCC1FSikR_2wGNR-ZLNzd2sgRUhZzXUq8vLYoAMf8lxZpXy_em1TSjdt_D5jiUDXk8iBgarjAN0H5XhRZu14cQKogDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
اسکله بنود بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67673" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67672">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67672" target="_blank">📅 14:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67671">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فعال شدن آژیر های خطر در پایگاه آمریکایی "ویکتوریا" در نزدیکی فرودگاه بغداد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67671" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67669">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRz7vVKslJVLSYB6OfYBY2N-jzP0BN2gYFQD7PR4tMg3n3SsF7oh0B6Qkw9HJakytuIReoxPPr4Wzy-paMAaW8M7yP7F-ISqgcYw7avYF0STCF1HpzcGbZMr3x0o5SPK7NyCd1R6eXrwRsek2IqHmfBD2OnqODHy4_27qXwff517b6TJy7bB3kmMTWMXa7p2UwVR6s2jMOsTFr7-6w0tjMU8Fg0rT4N3AjAe0MkWfEl1zbbshivCSvbCHch9lP4q_4nn8RdyjfZlGnZGAyH32_pEPTJpVu_0okcobYwCqezziDg413Ga-MV_Jw9l_ycWwm7p75KUfKEd2OkTQEi8KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8w9KJjUe30YVEfPHLbRoPb_h9B5ee3LJcVvuv6-GZBgoLUTMtPVcXRONF3T5NoGSisMpI4pg0md7qyr7clYceJgUWjgB0R2nPTIvHiJcnnhl-vOLrIiXkLGvmkig19c0k44OsLoaNnmeDHJGQr-HLaT5tW5ZwFEum_ZoPM4-gIPtqxOK3nVxww-KlBy3RnDcszpSGmHktGkZwo5lMHDSZefLNETEbTikM1h_wAUOv4JSY_wloZNYOq39QA2gkIr-HIn7D4joywmbpbqEwqwz42wuuFi9MBRGYaey9yiBYtL2tdNe8SAlcMdGhUwsTwU8fzPG_aRvKdqTW0galspPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
اسکله بنود شهرستان عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67669" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67668">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptqKEGFqrf1dbbCbAMtpm_b6PKulP-CqlmHChPbI5MtDeMCAiZeXLqe8Njo1q9a4HaAOqFImAqhHfb3sfmInrfxpeRnal0CmL-8voONI7Ct27IKEZtWY-bDclXndywfLEM966zN2LNSRJC-LjcFSMGYiYVGCods7f_18ub6Fesx_U1iptEEw5p3sS23rmtktFjvVZOVDMBTmf0f4_8o6etCZvS-0FXctQjp49OedCFDdlx7QlWjIcW5fTOyNzJTTQc9RHBkN6UNCGetTBKMf7DCaEC8tHN_euG9s9lF0Ca-D2MrdA2wi5BPkg5RoNUyQBUbfBl1QFZ9pBXMGcsPOcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67668" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67667">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان  @News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67667" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67666">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqIrv6xg11mmymbkGNYklRBLXp_lcK8p4RlfTPqEibIYVzm-zyylU-Ya_HydSkJ0tWLJ7Ju_jEXH8lZK_A5_iQBxMbIEITSu0KSg5ZRRorqJbppYDDDxXPEDUcRvyXcKjp3ccQKw8HqXOJMWuLdWk3xtMwNv0u6LaoRLIePetJZWcX2tXqK-zcSanbnv2H1Zw1gcTxQMuUDOnJy3x-ED9IarNNpitf-I5uI40ZAdJNNs8UQ7T14wWiiizqq7sUzQxm_BJeSSPmkmmTSvVJwFP0bKMPLqCFzaTIxkuMxg9Z3whl9e2WeZ2LTt5f9OgqWy0uNq6FyrltjATR2ymsoEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تانکر ترکرز: ‏
تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67666" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67665">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67665" target="_blank">📅 14:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67664">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=Zv1Zjfts_yHmAGeJydjPRGpzbCp5MC4IiDnrAFZ0Dm_ekpeez8UfmHE0taNnF89UWx0IyVpyTUbgv2GnEqzCxmwiGSjgzuRfM2g6A4Uu99gj8aWaXQFwDHyL27hXi665qGgHYIFkapUBE2NKfWXo2XioaKb2DGbXmOgMgPGJnbzpyylTbxp9cFxe5vthKs7W5XCSiWPDBXfTVG7SvdZrHqkAY60HVWwSEr8dRS0BDf3s0RVIyLdPoc6ZxTDpIHGShfQ7u-zvqHhb3P5fUFY2pcHa_3_3-ZsaeAOVwfv2ymxcnFbsGZ-aW-VC4R1DVBfW-yckJiqPW3Zcq3cP-tG1FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=Zv1Zjfts_yHmAGeJydjPRGpzbCp5MC4IiDnrAFZ0Dm_ekpeez8UfmHE0taNnF89UWx0IyVpyTUbgv2GnEqzCxmwiGSjgzuRfM2g6A4Uu99gj8aWaXQFwDHyL27hXi665qGgHYIFkapUBE2NKfWXo2XioaKb2DGbXmOgMgPGJnbzpyylTbxp9cFxe5vthKs7W5XCSiWPDBXfTVG7SvdZrHqkAY60HVWwSEr8dRS0BDf3s0RVIyLdPoc6ZxTDpIHGShfQ7u-zvqHhb3P5fUFY2pcHa_3_3-ZsaeAOVwfv2ymxcnFbsGZ-aW-VC4R1DVBfW-yckJiqPW3Zcq3cP-tG1FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال‌سازی سامانه‌های پدافند هوایی در اردن و به صدا درآمدن آژیرهای هشدار.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67664" target="_blank">📅 14:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67663">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67663" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67662">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=gxCorWM3LrpgqzJIIBBr7NkqcOgqjit3hsRvGhS1g31ls3e8dlC93IUPc1f0SbMPlCmSnlvBNCVy4hp7fSL95yd1OJw5jU2aZlRlFlulGqAwGiKnpg4LWfVpKlbSbW11-Fd7KDPUbTXykcpcsYFlgJOphQOkxAd8VbnYJCoOODajL76IkjPItoqCpVCub_YY9Qd58DcuozhxbF8YfbaJsL2hRJtLOgljRklLc8jqW09BgblKg9Q8kP9O2KW2lUh2t_lwJcrm6taLb45okKjTXbIyiiu4zFrrxauUqjU-lMm32QVB6baejeh4DPF76oW1uJEyH5EH8v5wK6xClZTpMFVTiLLEkEP7L52AZrLKQ3fdkIkAlzGJk_ahyaOwel1a38ojgBtTEAjaMxi6GCr1z0waKbO3kX1gxa0wTQYm9pDlusAs7hGORTu8MhIwqCYt_9DLSSK12-L95H_CaEqluOe3e3kPVwKyudSUugJxpDGBxUfswMhcp9QocleprMJBJgGcHTfyMuw8iwuElRi_5SvAnjUnmgvfZ02MejNke7j3C4rE-h-B7JqAiW_OgzrDyemn--_fW5J55b-Sd_ovoQy4eM0EEUTpv46rbX2dIAqIuGj7yq0tfx4ym93c1PEKF2G1zr3SV3yAYH22IyA-1HIiyLecJ3274BbYemOE5l4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=gxCorWM3LrpgqzJIIBBr7NkqcOgqjit3hsRvGhS1g31ls3e8dlC93IUPc1f0SbMPlCmSnlvBNCVy4hp7fSL95yd1OJw5jU2aZlRlFlulGqAwGiKnpg4LWfVpKlbSbW11-Fd7KDPUbTXykcpcsYFlgJOphQOkxAd8VbnYJCoOODajL76IkjPItoqCpVCub_YY9Qd58DcuozhxbF8YfbaJsL2hRJtLOgljRklLc8jqW09BgblKg9Q8kP9O2KW2lUh2t_lwJcrm6taLb45okKjTXbIyiiu4zFrrxauUqjU-lMm32QVB6baejeh4DPF76oW1uJEyH5EH8v5wK6xClZTpMFVTiLLEkEP7L52AZrLKQ3fdkIkAlzGJk_ahyaOwel1a38ojgBtTEAjaMxi6GCr1z0waKbO3kX1gxa0wTQYm9pDlusAs7hGORTu8MhIwqCYt_9DLSSK12-L95H_CaEqluOe3e3kPVwKyudSUugJxpDGBxUfswMhcp9QocleprMJBJgGcHTfyMuw8iwuElRi_5SvAnjUnmgvfZ02MejNke7j3C4rE-h-B7JqAiW_OgzrDyemn--_fW5J55b-Sd_ovoQy4eM0EEUTpv46rbX2dIAqIuGj7yq0tfx4ym93c1PEKF2G1zr3SV3yAYH22IyA-1HIiyLecJ3274BbYemOE5l4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67662" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67661">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=by_qLuAoLy444ditUoIzDFVt1LNl8JJShN5x6nn-7RJlpn5lIyMpfBYOLSFW2ZTZBg4regShUAo-g60nJprqMLAtl1UoD0piwgMy0brK4jxwI2hO1eu9oiVw53tk3yarSSfQzy5_RNqZWAmifdRJAXAgImTv_ZvwsKvai2dqfEnlp-rWSt8pxJZVMcraZARU1tE70Nyl0N9i24bSCTcRsvCXtProFFwJOk9Lp9K2hGN0WU5H-fgU4xGR2ge5SNXPs9Z8KNnHJM9dwSchDdqgoNrsME1mUOECvqgbOnQH7B8sJx8pAiGYzS-WSwmDHw62aEtwKDHU2jiz-z-ZJctAyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=by_qLuAoLy444ditUoIzDFVt1LNl8JJShN5x6nn-7RJlpn5lIyMpfBYOLSFW2ZTZBg4regShUAo-g60nJprqMLAtl1UoD0piwgMy0brK4jxwI2hO1eu9oiVw53tk3yarSSfQzy5_RNqZWAmifdRJAXAgImTv_ZvwsKvai2dqfEnlp-rWSt8pxJZVMcraZARU1tE70Nyl0N9i24bSCTcRsvCXtProFFwJOk9Lp9K2hGN0WU5H-fgU4xGR2ge5SNXPs9Z8KNnHJM9dwSchDdqgoNrsME1mUOECvqgbOnQH7B8sJx8pAiGYzS-WSwmDHw62aEtwKDHU2jiz-z-ZJctAyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ردپای موشک‌های بالستیک در شهر خمین.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67661" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67660">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
نایا:
شلیک موشک‌های کروز به سمت کشتی‌های آمریکایی در نزدیکی بحرین.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67660" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67659">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=n0PGKZsEOpQ5PFRgQtZFJmqtwj2zbik2tPI2hnD8-TYT1uNMeOO3EwG4Pm1fMs-D_upwAIG9DXUvAOAqbJDQWF2wCag5r31rxLbSWw4fTW7W6bXijbCrCUU5xTT8rcHaM-B3znC3VldDWo_WACKcrXmB7JMeRETTrszoMftifb2HX_SOuxslzbKct6keKJjawPN38AkXQ45x0aQEf8efE47rDTLcgmN3IRAQfkGt5HidKeGzoY1jjw_SqIun9QfjOyJeSDCoxypeAfhflO6HAf6gvamMJEVbljdImBXx8-8GdCly_nbgQF95_joThBS04ZY05hmZ5RcSfyiJr-39pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=n0PGKZsEOpQ5PFRgQtZFJmqtwj2zbik2tPI2hnD8-TYT1uNMeOO3EwG4Pm1fMs-D_upwAIG9DXUvAOAqbJDQWF2wCag5r31rxLbSWw4fTW7W6bXijbCrCUU5xTT8rcHaM-B3znC3VldDWo_WACKcrXmB7JMeRETTrszoMftifb2HX_SOuxslzbKct6keKJjawPN38AkXQ45x0aQEf8efE47rDTLcgmN3IRAQfkGt5HidKeGzoY1jjw_SqIun9QfjOyJeSDCoxypeAfhflO6HAf6gvamMJEVbljdImBXx8-8GdCly_nbgQF95_joThBS04ZY05hmZ5RcSfyiJr-39pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه شلیک شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67659" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67658">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
نایا:
انفجارهایی پایگاه نظامی آمریکایی "الزرقاء" در اردن را لرزاند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67658" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67656">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0Z4drlLg_tIqekvEUSvys_cZqRhm37k4P_GvLyc2Z93ukifiYbG5mZywiRt6DFoCmlC8DA1zc5i8vciRw6dRqRbYcioMAJslyW_IhGCdoEdby4kKOrhjtNm8r5CcAM5eczQzjFcQDhmE1UF7Aqqm519W7X-KcDgFEW9isNcPd65yV7O4m6XosuYf05kXJ5UD98xl7YsC-7ibu7uwtf74FMhpBIc1c7O_m40TVhfRuCLSTtoh-IieGTVvutTb7baocThDdGyegIlPerySmp39khyWBwCzhroEZCwmlwC6Vk1OGETAqrb-2OtEsdpyhVQwzmMyCdLg4k3GoJ-Sv22dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzntyK3wU0DVaJUEPrBVJw_1HGB0oZ7lyEWC5NYyGMumEoedLxeZWErlbkU2WRn0yHcsrt-cnPwdy14dif1_Kib-4NPbxC3l8hPM9VntnR_nNqosv0xZdKHXHT_I21HlVe-Tbjvv3TZ_4mMaZqARXzNeet6dQLbZUp4NeWO52m9JnSBhaaNxD-64pvpPNHy1QOvp4TIC5QqF52AVL0_-AjfSjPGrV4_R3X0cAKSIwvBEE3Vdzt3iXvOG5jKi8ijt47nvCIV2oTtaeG71SO38ogFoxX5e03wOWm-qP0KeEdzCoVHIF-pGr1Vmnj7afPPz6udY1AKDhgcTwkWBBhjKKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
از الیگودرز لرستان موشک پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67656" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67655">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
آژیر های خطر در اردن به صدا در آمدند
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67655" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67654">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpFJeIATxCyvEvldAWWX4JOUiMoiaC7O_GQ_oE5tvgPCegXPrv6cCTduahYHmY0F0Dbk5GZ4kcK-QCcSdVdnz5HJV4RQJQkVD2-bxni88icvzZfpbzE__POnxjIqqTXI-IOwARfMBt7YTOE_MKVyb7X1rhBBFnJqsFq_3xTLawrsf0-vPJu3iPFMkhur2U9za8EGcjktqKFpEUZY84Z4xv_QhcbWmK1pnq9lMScLO1rwnEHuyjEomRq4cLR0-BzoOuWymhqiJP3kBXPTvt70OUdPPiFJhV3BB3mRlXUx7UY09YvtEd2orlKaVHsJ46jmtf9LcUzVJd3Hrrc3gFBvDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از خمین و زنجان موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67654" target="_blank">📅 14:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67651">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKXEK-2L9aplnzWinOdG3r1BP1Fz2zi1iqueSnGv4FKbQ8dyT5Slr78Xw2vELc3OSxst5yL3fUE5WHaWHZ9pLXlb7kJ0Y65lC3diPQCsO7Fxyw7UqJ0QKXxziKUAZKlfM9zlElao08rXY464XchS78MEBCajY75Cp8Rjuzmhw8FpCMVIZGpYk6DK-8OHOD_sp2TJb6TMSsxn3Bd8phd-i9hMKBFzxedA6HjgU40VsRiAJZcagqpOY_57Et-COTcXuizICBKTxBgWIH2o6DzDojPiDNuVucQ0tP8hvnqtaXBjfPVqe4A6ubMkjC6BVm1j9agsW7PpXsCS9k1EJtqKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdPw50F13GaRTzfYNL4KIHEHmAXqndT3wV70aNEUkXOXV5p0gJHVMfVBmEZjhH6rRxPwzGf6yBT2R__Zz0dnKOBavUznoVNB_gx84x_mlcTsnScJ82IORMTeH8yyIXJqKMejZF_xzrRRDUKTwEN8E4C23ygR85PEFrTVv1QurMuKgxSynAYsNxSKNlk7Gmiurxn5I-9LjVejXikNAq_cLDmSZKOvZNLSaAnS3LVlLYVRPVmVpbF52JLBK8mnxFrmf4nighIrzdw9SbrNyYBSP1zGP7X1J4VmNQEXonEbsUDlRTp3f-rDuylow9QimG6-GGu46yYcf-_wEGSoMFS9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i65SXitqmPGUo6iUFGu0DCNNAszxU_YZrrqLvYdHzpggTgTrn78uhd39prjwcXpnFD-Ml6EhUJLFl5SFOwSwevw-SwCZ9gBer6NTydFpcQqNMjfSQ_eecIySwz0nvbiv4fbHa2N8_f5NcbUnB1kBmNZO7yNdwDNLNIFJi_hP_J6ZfWxsztM_gD9m0rEUDnbzXuW27J9uxHI4BVZPHTjSKjjiYQHKrnZNr0ZzuiCeb4jllGNAHM1biz13uWa2oGtq2xiMUyyAc_5EQZ6CwVrzfjxj6XE8XqNFMD0p2efIRd-MjoNKtLP1nIEc0UjVqrbTs95Oyzcj1gTUwgZ8bAv57g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67651" target="_blank">📅 14:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67650">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67650" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67649">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🇺🇸
مجدد حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67649" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67648">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🇺🇸
بندرعباس صدای انفجار شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67648" target="_blank">📅 13:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67647">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67647" target="_blank">📅 13:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67646">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
کانال 12 اسرائیل به نقل از یک مقام اسرائیلی:
طرح‌های تهاجمی آماده‌ای علیه ایران در اختیار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67646" target="_blank">📅 13:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67645">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
دقایقی پیش مردم در بوشهر صدای ۲ انفجار شنیدند که هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67645" target="_blank">📅 13:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67644">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
❌
چندین انفجار در بوشهر گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67644" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67643">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEIzpfrbOHefyYfMjnEF47G0bV_UJgNlWBcZKhY5A__fVP91mfIR6KLuhPPKAffVAUDYgzh2QAsbSQNvXfL2ELwlrjXpeF__8T5XoOJ0fgHuxzwPowq2W8rhBPuqOjLfEz5TAkR_oy3MKhD6Nr7WLVUMGEiCW0QVRY2ePyQqjgoOj7UStieMo0gR8iFWInk-4ZExv49s5mX0eENIXwhIEgsDw2pHOZirpDs9rwouhf91gZuO1zhElU559KGoX-V02DSUWtBcLfrkzvJ2PF_HJdINQuPWBPxTLusq2j5daSgW_LtpiIkDcQGeUOO3hm7-d-LerAI57FCN7Cc5EhMrLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
اگه براتون سواله که چرا آمریکا انقد زومه رو سیریک:
سیریک یکی از نقاطی هست که بدلیل ارتفاع و موقعیت جغرافیاییش اشراف بسیار عالی به تمامی ورودی و خروجی تنگه هرمز داره. توی روزهای عادی و وقتی هوا تمیز هست شما راحت تا خصب(عمان) رو با چشم غیر مسلح میتونید رصد کنید. بدلیل موقعیت نسبتا کوهپایه‌ای منطقه سیریک نیروی دریایی سپاه با کروزهای ضد کشتی بیشترین حمله‌ها به شناورها رو از این منطقه انجام میدادند و سریع متواری میشدن. تمامی تجهیزات ثابتِ راداری و موشکی توی جنگ ۴۰ روزه منهدم شدند ولی نیروهای جمهوری اسلامی بصورت چریکی و پارتیزانی از سمت سیریک هنوز اقدام به پرتاب راکت ضد کشتی میکنند و البته خب سنتکام هم مرتبا با پهپاد و ماهواره تحت نظارت داره و مرتبا پیداشون میکنه و میزنتشون.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67643" target="_blank">📅 12:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67642">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7AGy89lmKvtUxhCxFLg2qq25BZosRfqCbATCxv39gT-72sjLYg9E_tuH8DOgr3Lc7CacWCOcGK62lXt7dG3uLEVaD-coQ3EnexHIp3ZlXYmUMlWk5HxpSOvzqysQzm0UMNFMNcpx1u2cYMNPoZT8B6uUGVwyy4n_QO9n0QnFLmS6QNCtoNDq4qYNWMungJY2mLp8NPnRXBqca-kKPynjosJh32cWRozaV_Os9d_S7Tl7dV_2Grs1lVZ4IhxoHSiACf6ArGEp6n8_eacSGzwuS45a3b5NUhoo4KARv9UC6TvqePb8XMbFopamIiEWRbYjOAR51xrPEs9fCo5hMkTBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه وزارت خارجه جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67642" target="_blank">📅 11:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67641">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67641" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67640">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=v-u4Ldi5_AiuF72rwQW_bEzfJyNjCGUc8wJjKpUhTaSgBgR_gKqis8ehBgARC6Pz6DSDoqTKBxHLvXbQ0Vw29s-VprKtcB1IhkuKnQEUYtpEt3OkHX3Vp2NsusdekieEkunJKn80gvy7ZvAmFYaaR_Wam1-lMaed3jyauOXyuRFm-nAsla4wD381r0imy0G_3KOGIaHic6gcBDt4Z1JS4MlTIGE22eG6YQ70-DGUS0uMKEhxmXyJo0mHsLuACqw6YJ_jdzVh-U0V_aEq2o63nUaBlGTnYoVB2C_-3b7j0RPfowCNHKbPl7-oX98ovsoiz0e6FKujBHLFHikleYTwaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f84fc0204.mp4?token=v-u4Ldi5_AiuF72rwQW_bEzfJyNjCGUc8wJjKpUhTaSgBgR_gKqis8ehBgARC6Pz6DSDoqTKBxHLvXbQ0Vw29s-VprKtcB1IhkuKnQEUYtpEt3OkHX3Vp2NsusdekieEkunJKn80gvy7ZvAmFYaaR_Wam1-lMaed3jyauOXyuRFm-nAsla4wD381r0imy0G_3KOGIaHic6gcBDt4Z1JS4MlTIGE22eG6YQ70-DGUS0uMKEhxmXyJo0mHsLuACqw6YJ_jdzVh-U0V_aEq2o63nUaBlGTnYoVB2C_-3b7j0RPfowCNHKbPl7-oX98ovsoiz0e6FKujBHLFHikleYTwaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدبخت یه چیزی میدونست میگفت شانس ندارم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67640" target="_blank">📅 11:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67639">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=O-DT522z4DYGW_0ip_9WjaEl_AmFpFtMTchaYD6_x1ZR_iTh91iL3-_ns3AhSU-IqjvFPeaEiRSYyJGEklNNS-YBOnMHgg1x1_hoNSRY1u1W99F88i4wsSRQYGzNabHl94ccfYE4hbCoQo16DKwkYPv_lryhQ0Hks-gX2LHxbCeTwCQLmntmyIyw1PlXYmsUUoLyUhx0z3u3KmR7cgI4-Q-FSEBmqt24vWN_RdpHtgWr1l_Yl9zNmjeZ9khl_PvREafHdKP_W1Ognga-Q_ce0w8nxsB7rUWfsvOgzFgWATNq57ux5tbLSE1G1cdMsSRnu8oG1IW_sQPQMQZwX1ewBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7a4381ac.mp4?token=O-DT522z4DYGW_0ip_9WjaEl_AmFpFtMTchaYD6_x1ZR_iTh91iL3-_ns3AhSU-IqjvFPeaEiRSYyJGEklNNS-YBOnMHgg1x1_hoNSRY1u1W99F88i4wsSRQYGzNabHl94ccfYE4hbCoQo16DKwkYPv_lryhQ0Hks-gX2LHxbCeTwCQLmntmyIyw1PlXYmsUUoLyUhx0z3u3KmR7cgI4-Q-FSEBmqt24vWN_RdpHtgWr1l_Yl9zNmjeZ9khl_PvREafHdKP_W1Ognga-Q_ce0w8nxsB7rUWfsvOgzFgWATNq57ux5tbLSE1G1cdMsSRnu8oG1IW_sQPQMQZwX1ewBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
آخوند میرباقری، مرجع تقلید فرقه جلیلی‌ها و پایدارچی‌ها: دشمن به معنای واقعی کلمه هیچ غلطی نمیتونه بکنه، بنظرتون میتونه غلطی بکنه؟
مجری: بله دیگه، رهبر خودش این حرفارو میزد ولی الان کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67639" target="_blank">📅 10:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67637">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fky_Q4gHrQ-1o8krKZhowrE8qIzt2ZE2vTIwalzYxLxA2eIF51uAyjm5LPu2DFupZb885luo5vVRizqUj2G76c5feFhPTPSLp8DueUCm-u1IpR624mWXxNuQOZNlxuYHaqtZy5_1l0JPQdRf2Vw63iT2cYOiOXue3hd5RnpbIf7DaaVfIi1CI7sdFXg7XgETDbB_Bc2ZyaZYKbJ6R641TXJiLbk1BSavy-0zX_peVJ31oImUV3StKIJscR3STUQxXfqtLn8hap9eGwuVv8FbJjL4MmDW6c9A1iOc8II_5NiMIlEfKYwLjweIUex41BG0HM5lcIp36_DLmC-_9ClpXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=qG6fKwox8SZEjEZen9Ew7p0dMAaBFGORQaT_UioSO6YXzzT4B3XAGoIqEt3NukQYCKl16AR3Dl_RLZCERUfCjulKvsDs3T3WhgKdspOVYPcNujI2PfOGcK4lBqi-bvyR8YIDpwU02sYRftwpzciFvS-GUT6atqbvDrW8MvMt0PlIe6Pb-A4xV52UX69ZSMO-7TygxX1SasykOxXeWNt71ky4t7_B-17EgCdjgAIYKN3Ew-ofVZTPCfEhQIFFBlTvpv-y1a0b7wRHUp7K3uN6KdF-EE5pA6bAHuoxIaIS0QUL7KJXv07b9cpkgqN91PceHbCBxaiFJ83lXYWejlbFaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0eec941b2.mp4?token=qG6fKwox8SZEjEZen9Ew7p0dMAaBFGORQaT_UioSO6YXzzT4B3XAGoIqEt3NukQYCKl16AR3Dl_RLZCERUfCjulKvsDs3T3WhgKdspOVYPcNujI2PfOGcK4lBqi-bvyR8YIDpwU02sYRftwpzciFvS-GUT6atqbvDrW8MvMt0PlIe6Pb-A4xV52UX69ZSMO-7TygxX1SasykOxXeWNt71ky4t7_B-17EgCdjgAIYKN3Ew-ofVZTPCfEhQIFFBlTvpv-y1a0b7wRHUp7K3uN6KdF-EE5pA6bAHuoxIaIS0QUL7KJXv07b9cpkgqN91PceHbCBxaiFJ83lXYWejlbFaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ خطاب به قالیباف:
یه محمدفلانی (محمدباقر) اونجاست که با بیل داره یه کارایی می‌کنه؛
ولی محمدفلانی، با این بیل‌ها به هیچ جا نمی‌رسی، حتی بزرگ‌ترین ماشین‌آلات دنیا هم تو شرایط فعلی نمیتونن کمکی بهتون کنن تا به اون اورانیوم‌ها برسید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67637" target="_blank">📅 10:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67636">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=MzUlP_QM7IOTUj2DKl5bCjHb0sE6paQlLFhXb6zKUpn2TPzeopzk9HcRlqEZ9ZjluW3IshK1LLgEBAJa6B33WdKlic8TBTeCTxCdMShwoHbcDXbB0UwCC99cOakOmP1sY_-_P1zEBNUJZbJgJ3aQrvUhK0FmM2RKLR0HRHcEJWRHF2h3CbepQTTuuwwPagb40aADSf5MZ5DusWE5_sgm6Ycn3-tZUicIZ2ofGA-FDmFWp9IYjmhAPDknqulrdFelD8Z_h0Ib8canIf7oqhHA1R8tIZq5kC_7bV1H3gOSWslVFRKTK8BhMYVGrZYIcS9N95AagEu5dOM5ghsgS20tNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3353d5522.mp4?token=MzUlP_QM7IOTUj2DKl5bCjHb0sE6paQlLFhXb6zKUpn2TPzeopzk9HcRlqEZ9ZjluW3IshK1LLgEBAJa6B33WdKlic8TBTeCTxCdMShwoHbcDXbB0UwCC99cOakOmP1sY_-_P1zEBNUJZbJgJ3aQrvUhK0FmM2RKLR0HRHcEJWRHF2h3CbepQTTuuwwPagb40aADSf5MZ5DusWE5_sgm6Ycn3-tZUicIZ2ofGA-FDmFWp9IYjmhAPDknqulrdFelD8Z_h0Ib8canIf7oqhHA1R8tIZq5kC_7bV1H3gOSWslVFRKTK8BhMYVGrZYIcS9N95AagEu5dOM5ghsgS20tNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
🔴
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در تاریخ ۸ ژوئیه دور دیگری از حملات را علیه ایران به انجام رساندند تا توانایی این کشور برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی بی‌گناه در تنگه هرمز را بیش از پیش تضعیف کنند.
🔴
نیروهای آمریکایی حدود ۹۰ هدف نظامی ایران، از جمله سامانه‌های پدافند هوایی، تجهیزات نظارت ساحلی، انبارهای موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران را هدف قرار دادند.
🔴
این حملات جدید در پی اجرای موفقیت‌آمیز حملات تهاجمی در شب پیش از آن صورت گرفت.
🔴
نیروهای سنتکام در تاریخ ۷ ژوئیه حدود ۸۰ هدف نظامی ایران — از جمله بیش از ۶۰ فروند قایق تندرو متعلق به سپاه پاسداران انقلاب اسلامی — را هدف قرار دادند تا در واکنش به نقض آتش‌بس توسط ایران (از طریق حمله به سه کشتی تجاری در حال عبور از تنگه هرمز)، هزینه‌های سنگینی را بر این کشور تحمیل کنند.
🔴
نیروهای ایالات متحده همچنان هوشیار و آماده عملیات بوده و برای اجرای دستورات فرمانده کل قوا آمادگی کامل دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67636" target="_blank">📅 09:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67635">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GN6LW69bQd4d4BAybS_nQbvF7-tRC7O5WvM6_qC2y-ObqdGoRY7Oik64ltoep0AyFUu05Y5HVOLkCxNrO-Vi_XYkTHKvExW6j2YduJSloTl9HQmZ6KEoREQTYjBV3zytM8msjq-Y5AfS5cDOu3NEJRX9gQP04rlHO7NMlDUFBNhUwSXDfZ8ez75MPOiauLoTk2TjI5CCgL8dftp1wfpziGKCnPKt8UdoHNUEQkTlf0sYI4HUjuA3JBbLWHrpcAAVAxFeIDuEqtFl3tVK8pWrdgUm9JD7dUy7KzJS9W_iHllDJ3RalCk6jizjoKoxH_elbcuL5pWdavlKiI3Z_2s64g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت برج ترافیک بندر چابهار پس از حمله ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67635" target="_blank">📅 09:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67629">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M8Bz7RG1Sn7Kf3tvDlwAfKRc9_fN0BnUHYiqizSnwNdbvES45saR-6QIpVOsTpe4DL4wG074zaoFF2aQDk9P1hM3m6KQJvOJUruLcQdBLGhHvppzabn_Ui7dCZmKZ159BGSXKnlw00F6fG-pQfy5PLmrGRezj1fTcN8cUVeiqsU1bY8m9t5O_q6SSHITGUM1xTi4R-sZnisE8GOPhraaym7tpf03OPvcYsjte35ttxelZb8gyic4OeKZKooff0_-w7FgeSMGbdU9fYuj-R3v2mDsWc70kEzm7zTNr6vkLmTKvKVIaSU3tAIjDAopLaMn6O3wp3rceuWgpm4IC9m2vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M0O3RBA79YZ2_d2_POoOiyb7IkVHX9m85TSGIlV3mCjDinJW6wPidyQbxUWKdAtBbYx97N-RzvrMFo9fUyHGTKjMXSRCKcZjagvyO5Hoo8OiwZ3MJxte-8UycSYVjoHqCr1-X-1MNCI9K20Bzf_gD1o9OntafPpK9NG28wW9VCV600Zy_fsOTMhvyXO7fmaNZZKpUbHk4tfLfSqIAIoSOvbjPtgIBtMadNhQXs85yP0O0-SKrsrNpuSI3rPX6RZfNejKXzSxwwqWZquyS_88fqY7ABvyYEYxZacHHAwzq-6JVsMjADAGfcSsdXqmj8De62XdRRAmuZTc75lX5MUyqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=HHVjT45tfo1YZnHMJa8OK3UOVmDFROkTfAjDTjK6pbMWhA2So85jnHOEsRlWhg2d_xR-Z34IgxcikIhS0ctayxri3UFRze4zx8i9YZVi7BQzS6cMnGwE_GHs-Zs91pXDL5UrEHBxHIOB-r17fjKoOEzvipQEAGQlAqSUXlUdcxsT8QBdheZq0I9Ndmq73HYXe_uud2RqT4OTq9ZC7JRRjkMVQwRycpVdYNqsgHckNU0cEy8HR25450fYA5OEkYmfaCgNOAvy3z64mVcG8pFlZLkIOzuJ1XxIQNu2MhRP_nybSTiOcgx8zwpD6z1-UicOFqPXlv6UROddb4AfL6AaLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64ac58e8c.mp4?token=HHVjT45tfo1YZnHMJa8OK3UOVmDFROkTfAjDTjK6pbMWhA2So85jnHOEsRlWhg2d_xR-Z34IgxcikIhS0ctayxri3UFRze4zx8i9YZVi7BQzS6cMnGwE_GHs-Zs91pXDL5UrEHBxHIOB-r17fjKoOEzvipQEAGQlAqSUXlUdcxsT8QBdheZq0I9Ndmq73HYXe_uud2RqT4OTq9ZC7JRRjkMVQwRycpVdYNqsgHckNU0cEy8HR25450fYA5OEkYmfaCgNOAvy3z64mVcG8pFlZLkIOzuJ1XxIQNu2MhRP_nybSTiOcgx8zwpD6z1-UicOFqPXlv6UROddb4AfL6AaLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر مرتبط با لحظه حمله و پس از حمله به خط راه‌آهن گرگان در نزدیک روستای آق‌قلا، پل دگونچی
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67629" target="_blank">📅 09:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67628">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67628" target="_blank">📅 02:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67627">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gju8K9xGlRvBRIf-La9_RnIG4QuTpx9LwOY4TEMCE2FDNGuLSMgZqovawMKXnM3g-6FbqWAiJ5BLEF6idClr2tY1V1WOY1Pq5zV5f2_1OT_e5Sq63rMC3NnzaO-nOXzhL-_stLZm0nP2o4viyLlRyahnOsJuXsOOJibZa-rhKUeMpjgqzJh2aTOZef5EWo8aaZxXOw_8E6r0XkUU7Uj6Kkpd0u5Y53EhnLnTDqz9muPupBOs-IJ74U12l_2px8SYZUPrfzdqXZZ6jme2fbDGh1MjSsWXasf5EmZE-nXhtkf4U6z0jII-JNY16jfLX-9XjD8dew7-bTPTwfeNsRlcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67627" target="_blank">📅 02:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67624">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PRHUVewXMIwRTKHW3r0yCxV9Vg8IqTpPakgsfIpURauWGgHGKpcS1n3cXtvPTp_Gn3m2HElVcpD4Zh2jLNWGqrAGPFTptOFvICWVuy3_zIC6ZF85CxAz0dxAzscsBVOpGcfnb2vrl5i-fr7UKuGvbBd-zBeY_NhnxQPXpUFIXtyaSV_xlX4ahYrX26Cm4HUOHFrVdoachtbrHh67270_a_EOQSrErWbbMU415R77hrJ0suu5vA6VEGl6HK0C55xsszcXhE703Nf_MIT5SsrDnxLOY_c6P8sxwgHmYZVTopcDCQzbW91uQklOKs5jK-1iGTic6Duf53jRNECcNdDB0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dMDz-R0cuKncC906xlEkfV9CzWkOebsQtKrKrwERNlRmI1CNV5c73CrokkWEEMphOsKLn1iyDExyFo-28gtSs4k7GdffFieOt7GlJSyxRGCxIyP7hut-6xJs2lwCQmSY-TEfMzz-OMc0Fh07d3_ROd9xk6Fl0eUVXorXFhAyCx--9-fNvtvGoTeDgnQXsZBSVM2Xm3npIGYD3F05q2h87OJ8L47uXMF6iOpBTyaemqhKBd_baz1fksz21ldhdjzg5_g4yRdjBaIEKXDXTFElgFxxE8VplKzEd0A2dndwkgXzHrWFsAvd2ZdMaYUlzLt48UimRGHFpQYLO0106aeiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tIgWa2F-N7FJeqdafLLbWR2aAGUnQycVxaWP7zfF2fElJ9xZ36pNupo3TthzfFTPbK1VUmJ92Qe_yQ3Nt58NMB6XNmvAEv2OTq8VIk5op-XXU7eklNZikjm1xn7zc2YFo2o5nomw2AcNf1QDwkRIzxo8DHIG2_k4Mf9JGf8LfE1wucHdIOzEG4Ifbl4dnLQqJRraUX3sASxAj6TRkBrIwtJg4p9teg2DvPYFF-xo8Hp_wlzl2v3D5mta3KvF09jSDBZacgO5LDxxmOgwT2I-DNav7_YcZlHQIAPDPABP3NeZWLOp5CawEbqWwSu3r5anXsA5aI5fgvGtSQllzTPoHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
راه آهن نزدیک آق‌قلا در گلستان هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67624" target="_blank">📅 02:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67623">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=sh0jN5Bi2XABjokETfSAzzOY3ZoEjx_7RD-iTExP27G7iC3msJaHIP02uM1HGLvbZzp-prMlSMF-wRuZAo_XefGy_eGbmp3KMEv6Ml4PtaFKZtivfQD3_pbV99PkiRpMbmy5eqpwYIV3_Wb9FwvwbdcCG1iFlcuL5i15vQkrss1bdG4zNJsWg-kWGV4HPo3wzSIwB76-h4w1QzgDw2Q19cUNjhGmmt4lwIPfEG4adA0QBUYbfQwZ-G6QAY2D8ddoXgU9vf33I6MMS6K5NVLm55Jya4bcAi4BIOjUWZt7c2BcsSIa7edLGpuUs7EDpmUzH41OQWgoKukJjYRUUvGOuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4f434f83.mp4?token=sh0jN5Bi2XABjokETfSAzzOY3ZoEjx_7RD-iTExP27G7iC3msJaHIP02uM1HGLvbZzp-prMlSMF-wRuZAo_XefGy_eGbmp3KMEv6Ml4PtaFKZtivfQD3_pbV99PkiRpMbmy5eqpwYIV3_Wb9FwvwbdcCG1iFlcuL5i15vQkrss1bdG4zNJsWg-kWGV4HPo3wzSIwB76-h4w1QzgDw2Q19cUNjhGmmt4lwIPfEG4adA0QBUYbfQwZ-G6QAY2D8ddoXgU9vf33I6MMS6K5NVLm55Jya4bcAi4BIOjUWZt7c2BcsSIa7edLGpuUs7EDpmUzH41OQWgoKukJjYRUUvGOuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار: اگر ایران خواهان یک توافق است، به نظر شما چرا به کشتی‌های تجاری حمله کردند؟
ترامپ: چون... راستش را بخواهید، این موضوع کمی عجیب است. کمی عجیب است. آن‌ها کمی از کنترل خارج شده‌اند.
اما آن‌ها واقعاً خواهان یک توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67623" target="_blank">📅 02:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67622">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518cba3871.mp4?token=EekUVcGQTmGK6O4jnOrg3tNa69XCMsLOymZRaU3f2moI1Oo7CVkXHbIU-fS5a0nYE3sqdTao3Iyn0PrLWfty2WPgqkn4olU4GXu6vWtxC2KbxLqRHm9MGBDMhFeZiREszN1pnYCxrFYWlxg37t7OZw6OdEjP15AC-IvdLhec3QHLFQpgECFyYpsUdKC4WVu_Fmec8vuvj2mU11vqp_qBEmQcqe_tgGLLONR0oZUQWZuuK9aEwqF091DB4MFK8GOdsoctBdnU6NoHtK9w9MsVEIGfaDPSxHWNvxoZnnW1LJlOSYvR4s2pAWRq7WLwZm53vo3Xtd1Tmjux9eHAFY33TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518cba3871.mp4?token=EekUVcGQTmGK6O4jnOrg3tNa69XCMsLOymZRaU3f2moI1Oo7CVkXHbIU-fS5a0nYE3sqdTao3Iyn0PrLWfty2WPgqkn4olU4GXu6vWtxC2KbxLqRHm9MGBDMhFeZiREszN1pnYCxrFYWlxg37t7OZw6OdEjP15AC-IvdLhec3QHLFQpgECFyYpsUdKC4WVu_Fmec8vuvj2mU11vqp_qBEmQcqe_tgGLLONR0oZUQWZuuK9aEwqF091DB4MFK8GOdsoctBdnU6NoHtK9w9MsVEIGfaDPSxHWNvxoZnnW1LJlOSYvR4s2pAWRq7WLwZm53vo3Xtd1Tmjux9eHAFY33TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما از نظر نظامی، پیروز شده‌ایم.
آنها مدتی پیش با من تماس گرفتند. آن‌ها واقعاً می‌خواهند یک توافق انجام دهند. اما من نمی‌دانم که آیا آن‌ها شایسته این توافق هستند یا خیر.
من مطمئن نیستم که آن‌ها به توافق عمل خواهند کرد. این مشکل اصلی است.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67622" target="_blank">📅 02:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67621">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=GXIe0mraTmeiK-vxI0cotMFdNOziZZMaq3DJ98lJWY3qYGx7piO7IssxIpB1FlRAijgEH3B89lfS3obHo8FocX6LjXJCqYkUMN5zW962awAk3_4dXAnnOdScEhzVep3n-6JgRuWJmzsUBdFIVrrQ0viCC85__9kM5mhZnoH9Q760CpvxaOLuK5VumLWlCCnBA40or_OrR2sfu5R1AmJIDhLdXlqlIkBGE05nuCUSvb9nGQHKcnF5RjWLjsW0dwTGnZerHrmEw354B5Q_pFWq-AHrkIht2H4r8Bfp2q4Sh64plXdzSL4UU40VpGENIzrrTR3VEoQJSL8tdNAeDwJBLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba19bbdd9.mp4?token=GXIe0mraTmeiK-vxI0cotMFdNOziZZMaq3DJ98lJWY3qYGx7piO7IssxIpB1FlRAijgEH3B89lfS3obHo8FocX6LjXJCqYkUMN5zW962awAk3_4dXAnnOdScEhzVep3n-6JgRuWJmzsUBdFIVrrQ0viCC85__9kM5mhZnoH9Q760CpvxaOLuK5VumLWlCCnBA40or_OrR2sfu5R1AmJIDhLdXlqlIkBGE05nuCUSvb9nGQHKcnF5RjWLjsW0dwTGnZerHrmEw354B5Q_pFWq-AHrkIht2H4r8Bfp2q4Sh64plXdzSL4UU40VpGENIzrrTR3VEoQJSL8tdNAeDwJBLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ درباره ایران:
ما به آنها ضربه بسیار سنگینی وارد کردیم، و من می‌گویم که ما به آنها 20 برابر ضربه وارد کردیم.
هر بار که آنها به ما ضربه می‌زنند، ما 20 برابر به آنها پاسخ خواهیم داد.
وقتی آنها حمله می‌کنند، ما با قدرت بسیار بیشتری پاسخ می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67621" target="_blank">📅 02:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67620">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db0d252421.mp4?token=TLOOnPtLMAdafUNuluyv5lb1uC1x4aOtiY41ynIkGkTmAwDZvBzgBYV2WA5iJ3n4Ev521XniYYqe9dRKtUt-V4rnWLpYcc3JHKob59scBzF0OEdRNuZgp6wIVIO8PR0EyHyaFV8HcvNF4TigQx8AmKGGL1q9HZVPUYFf6PEW4X4uQ01HAOH00TdAoRFvwf-1pOabuS-zID5NsLYIFoQjEYx0g1w1kS4j9iXPiM4ckJlqRY2J8XyluB_mX8o1nZ34PzZ7neDY635e1hCTN_MvBxgqol6frsGdGTrMBVTqZyxG6aChZ8zJZmfUlJaJfL9voJ0wXEnQSsSJWiRHNAuhJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db0d252421.mp4?token=TLOOnPtLMAdafUNuluyv5lb1uC1x4aOtiY41ynIkGkTmAwDZvBzgBYV2WA5iJ3n4Ev521XniYYqe9dRKtUt-V4rnWLpYcc3JHKob59scBzF0OEdRNuZgp6wIVIO8PR0EyHyaFV8HcvNF4TigQx8AmKGGL1q9HZVPUYFf6PEW4X4uQ01HAOH00TdAoRFvwf-1pOabuS-zID5NsLYIFoQjEYx0g1w1kS4j9iXPiM4ckJlqRY2J8XyluB_mX8o1nZ34PzZ7neDY635e1hCTN_MvBxgqol6frsGdGTrMBVTqZyxG6aChZ8zJZmfUlJaJfL9voJ0wXEnQSsSJWiRHNAuhJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
من در صدر فهرست(ترور) اولویت‌های آن‌ها قرار دارم، قبل از شما.
اما اگر من [مشکلی] پیدا کنم، شما هم [مشکلی] پیدا خواهید کرد. بنابراین، شاید روزی بخواهید شغل خود را تغییر دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67620" target="_blank">📅 02:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67619">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
انفجار سمت آق قلا گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67619" target="_blank">📅 02:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67618">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در گرگان
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67618" target="_blank">📅 02:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67616">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=Vs9t88tJaAP2cvLlQFdROaayou7MnsDPitsRp6q8oq0_K4dN89gRZ9sUA949ABa-zKJXpQDmNZO_q_wsuJlVscFQP7Wl0RYydSgSvwGZX7QqmsLf4hp-A_lHUXbRA9bO65VpfoHPQM9c55RvSv5ewHQFLe5HDGtgZ9AdGBdERfllp3xTEIpP_gL1VAAPps5JHYfX5YhykkmQQrM4fT-nziFHs13IJ9Bw_NvJL0xLcpFGGnWELRyLCrsHFt58Nvm0aZldJebz-JMuKP_J1ilijhM-iPQpKOPVONZzvugZptIwMV5GcC1xeWm9MWaN9Ip9eAr1pNCiEpHQZ6-hdKq3MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c35f85df80.mp4?token=Vs9t88tJaAP2cvLlQFdROaayou7MnsDPitsRp6q8oq0_K4dN89gRZ9sUA949ABa-zKJXpQDmNZO_q_wsuJlVscFQP7Wl0RYydSgSvwGZX7QqmsLf4hp-A_lHUXbRA9bO65VpfoHPQM9c55RvSv5ewHQFLe5HDGtgZ9AdGBdERfllp3xTEIpP_gL1VAAPps5JHYfX5YhykkmQQrM4fT-nziFHs13IJ9Bw_NvJL0xLcpFGGnWELRyLCrsHFt58Nvm0aZldJebz-JMuKP_J1ilijhM-iPQpKOPVONZzvugZptIwMV5GcC1xeWm9MWaN9Ip9eAr1pNCiEpHQZ6-hdKq3MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تابوت نوه خامنه‌ای رو با سرعت دارن کجا میبرن؟!
🧐
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67616" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67615">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhmDG_GSMeWvTGQqh-BuCUb5P3j9kTaGOA5MKH4NX983qL3SsqFn-1qpUfaO_T2Z_Y0EcILh_iizsrWoO0QWstUDUpXu2vSJ3sFPW_zhtjvuUCIgaNPLGrn0s56qa_C1Jw6J0Jd3UUkcCqAi5oua7UAmKsP2KAtaz9D9Fq0PaI7la0rjZLXNR1RSKxGYbA1NuaroC4ybAqNwRAGgeEAQOJmJlPmKbhCYkVgUX6ZVrjRXwAZHbDxEOc6S8o9BQYmYu2xWkrH6FJEakwR2HuQyNLx5_9cBVsHKAAIxZy9WxrjsDryHuzfQXjTAL2AZfvvL4NNPf_m1IG8BgNhKEqudfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نقاطی که امشب توسط آمریکایی ها هدف گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67615" target="_blank">📅 01:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67614">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان:
آتش‌بس موقت با ایران متوقف شده است و وضعیت همچنان بسیار متغیر است. احتمال انجام حملات بیشتر بسیار بالااست.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67614" target="_blank">📅 01:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67612">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfCEdIYoPUlH4OPH4402x6CFD5tl9um9Useinsg6r2WdrOzfZf8W3Npg3nP6wlznxJ8bBO0IOexoZ4XEvSAjj_AI-FctfP7nPYDzHdubBWCQCI58HgTPrhH6tZLjKBsJjGpEl6xf7ELGTOCY6ohWf2ozpUfhAMyKgVGltcwCTfSVDvAGrMVeqW6YwN2VQNnCOUSUhcSotvMKgsFhj00PMLeZLtAPJ2jCWeJ9vwa8JFQsUWD1Vn-hCYU2PELNlOcUm710GRgTF1c7WJ9jFvLyijTAuc9sI4WoipH490ORveFIkJpCaaIFEwBUiMbhY8vQnyVhuPWLaC4l0ZqsM5F55Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=WM-jzl1KfRZkUMtcJbJP40EgruNzw-TCgw4uSuWeqG6swuOzB87zdx6CFJyjp55TxCkEoxuSnX5-RiHEjvCxDGA92JamCkQVmoXYYpRgciJRGOzu715pHkX_JBEkGBEn9eRqhSm3lCD2ggtKo47gqK7HOSZg2MJpFubz3fgIgFiPeil25ZTXtVZts4cdAkVWzW4RTWFhtr6AATSQJWVycKLs4MSR7ILJpo4SezArYnTkGAAEu_xj_EVut3Rp57SbPhZCtJlTHUiwu2PhHpEoOjeVubq5zQ65Cg0pFToI9sRiWXcchw7jCOpN3a29LcWvU449ID-6f7_2ICmNDz1QWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87cdc8ac4.mp4?token=WM-jzl1KfRZkUMtcJbJP40EgruNzw-TCgw4uSuWeqG6swuOzB87zdx6CFJyjp55TxCkEoxuSnX5-RiHEjvCxDGA92JamCkQVmoXYYpRgciJRGOzu715pHkX_JBEkGBEn9eRqhSm3lCD2ggtKo47gqK7HOSZg2MJpFubz3fgIgFiPeil25ZTXtVZts4cdAkVWzW4RTWFhtr6AATSQJWVycKLs4MSR7ILJpo4SezArYnTkGAAEu_xj_EVut3Rp57SbPhZCtJlTHUiwu2PhHpEoOjeVubq5zQ65Cg0pFToI9sRiWXcchw7jCOpN3a29LcWvU449ID-6f7_2ICmNDz1QWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو ای منتسب
به
حملات آمریکا به ایرانشهر( سیستان بلوچستان)
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67612" target="_blank">📅 01:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67611">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h27Z8BoCVOj7Hso3S8kca7YGXXJEyID7FnytH7OLhn502p0i7eaoE7LTQybc8qrOYDHOD-dzFYICgsvs7gVp31eV57jBQEnXsA-4cMIgVw4R_KYg5scYanP44FXMlVul8HrSNnK3YY4XEXLFaGULAxDZqo2BtjCiaJAx92rIGnmbQoBbwaSGK2g-B1lZTCDpSrWBjxrhI30UGMJvhdrMZwl65rlX0pDMjI7kfcYQHfYH9Lpfrg7h73G7wCONkg5TUG_SR3ET3thslN9-LkI0X6htxVWvwfLuGnH7wXiyspOIu8lLXSoB8BrvYw0C7macyu2viZUN2xPgY-tFkGK8JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ :
این یک انتقام برای بمباران دیروز کشتی ها توسط ایران است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار بدتر خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67611" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67608">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oVhFyUrirWMTzSPFqdKOXMMHfcUirIeenuz-2NZPSSWG3YS1Ks1vJfxnVmyuqbQ941G1rrtYygP3BogoQAG7uIsw1kJyAFRllwykAg1vutYUM8Vwq6QRYYqc-kYB5-15xc4BCdBotS8P4lPyMN05Qp3Ty6N4wuDjgb3R1OjJGFWFH2WCtosZBGbwEla-Y_2lotqDFN_cl7429_OXK89NIgqlhfwD0o3oPuuXbXqzPYGABekbYXyD_2YfRDGj76sx6Wyr6iKbkU6Mcoju3gaEAv4c1SLa6tAEn-taiB3rBEYB53Q9cOkMmFxXxlCffdUH8oA6TD_kiAH9imgwwKJF1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OVtgUFGfFHP1ufZww6wXWw50rr8AAAJA7OpQgp0NUsanpHJsBo4zGeVMvOSqGUQR2atN22qadc-tULe1pAror4A97ModjZKRGP0Pe5Ow8AdczGs_1M0ApeNo31jjFrFezkNLGmbBZvXnnk8i3jRPgT3Y0kv019Ou7mJqEkZ4PSvUdnALlhyq2OXLtq-wt_DGH2mKu1c41dbzeIaiRM2vuSf3_NQYdt7ak5ZE5OD_RGjKi0DDJ7bQJHRQ1ZwAEVxPCYPFveNcQPeI6ZjCsic7kL2-w22GvcOu8rP6A2VRsNmWjvuY_8EjVlHMyYk5QVut9X-GU_lJEc6V7ZB-6r2OUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BEOs4AHPTCCbvxqDH0tsnXYIR5dEcgzOuAgyRDQcWrSmGjFte65dr_txIuoMTotdTklkIHX6DI2fcH_8bwlom1BQF1iiZpLc6ZXoyUXAgR4xqrM60GMvWUfbMqsQud3x9Eof8CK9IcIIxJnrTGhvl5d20xh83OQxW4zYd5cXv9nXM5vaHgQ8LUL0EeVo2KPz7NXzRpnYv4XhmeMB9CJIOUygZTxTNIPMvhAL9QDYhjApUeOpK6VmBbtt4XwEIvtW87rexrO6-3IQDQx7hB3VZ8OFU2sI4P-czU0PktcihvNfEr-VKZSadS3OHClzZKdKf615wFE-mZGjTsVSZa6Zxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ تصاویر حمله به جنوب ایران رو در تروث سوشال منتشر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67608" target="_blank">📅 01:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67607">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دلیلِ این چص‌حمله هارو متوجه نمی‌شم واقعا، آخه کسی که زدین رهبرشونو که از نظر اونا جانشین امام زمان بود رو کشتین، اتفاقی افتاد مگه که الان بخواین با زدن توالتای پادگانای سپاه اتفاقی بیفته؟
صرفا این حملات شرایط اقتصادی رو سخت‌تر می‌کنه همونطور که امروز دلار ۱۸۰ تومنی رو دیدیم، خود ترامپ هم می‌دونه تنها راه حمله زمینیه و اولین نقطه هم خارک ولی جرئتش...؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67607" target="_blank">📅 01:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67605">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=aFsNIgHKPgq3u1nm9twjCR0KbqneewPY3g8Nt8sRzIn-lZPYHb79Dbyg6f10nIMM59wiRDoUINMqFxXuci-Eknl2JVW1hFmPR9Je2Z8pccBoPTUXNOiTjfedaaRhQBpkhnndfpz4cXg8YD8tojl3mVeHUt3tAzprwc7wVsD1H-egoRm_shngE9-v4CPpUbzp1m2FX-SqFlOo3Eg3jkjU5QmuXwEi1-f5LPV_iqyZC5AEI5AMIOteGMVgu1TCvp6BlEBB3v-qgHPX7pgzCefth0jJaB9HWUX2TAOdbTY_sA2bcAvWxBLmU1eZLveycCd_Rj4jcoGQKW4D57yhsogTKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=aFsNIgHKPgq3u1nm9twjCR0KbqneewPY3g8Nt8sRzIn-lZPYHb79Dbyg6f10nIMM59wiRDoUINMqFxXuci-Eknl2JVW1hFmPR9Je2Z8pccBoPTUXNOiTjfedaaRhQBpkhnndfpz4cXg8YD8tojl3mVeHUt3tAzprwc7wVsD1H-egoRm_shngE9-v4CPpUbzp1m2FX-SqFlOo3Eg3jkjU5QmuXwEi1-f5LPV_iqyZC5AEI5AMIOteGMVgu1TCvp6BlEBB3v-qgHPX7pgzCefth0jJaB9HWUX2TAOdbTY_sA2bcAvWxBLmU1eZLveycCd_Rj4jcoGQKW4D57yhsogTKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدئوهایی از لحظه حمله آمریکا به برج کنترل دریایی اسکله شهید کلانتری چابهار :
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67605" target="_blank">📅 01:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67604">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
انفجار های مجدد در جزیره بوموسی
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67604" target="_blank">📅 01:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67603">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ماشالا ترامپِ شیردلِ مادرجنده‌ی املاکی
😊
#hjAly‌</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67603" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67602">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67602" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67601">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBEoKCcOyi_019ElQTbqJ59uOoUpBoid-Eqttt10kLeKCifSqEZ5rPJZRKp-K4ZnMhrxqtMJ61pYl-wAxUsHpgRWKFPxMR0aTpoh1q8f6TMNyFv5EGOEG3FQi-4R647w7G_kR9Vpq6CfLa73jpqxOBfO1Xos_nQ-YN6ESMuJ405WdkVJuV8xXmVYzjJXe9a6QGSqfFmPP8LKrQOWxAdoWDT64yJK5dZwS1zuHMPYxURBBU0A36ttsvFjoz8S4GLALzdUDy_SVGw-XMDkNaPcayRauDZiaO7uhdrVKvKhWUjOTbKePRG_tc_CKu8QQQ8ZVRnxuZJaWTb8vu3q--cjVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
یازده فروند سوخت رسان نیروی دریایی آمریکا بر فراز خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67601" target="_blank">📅 00:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67600">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sws4qmh9xmjUt_nErPDUGnMsNws0tp9oiCjpCpafFKG-7GQzZOLm2XSQnwskjstEztumr_bPKKYwqSitfnbhigmUEOaw-wCSjKdLhGiLNM50i66iLDE2DqsOIOlQbAWKRC8Yjbz-4aSwsPdHbAJ-PBLz7gEHwnF2pZxL38aqDHTa3mEx8rV_6fkcDoxbkdWZi72w_s79U99uEdtoQG9m3-hlN1DTeOtxIZLpKFSdptsKN9-BgLHZ9-c2qj_pyjDyj8_VPThNFRP0NpVyFeJZpIjf5e3M-5GwYq0gDx1WQ39lGFV-qzQANKJbHosJdLd3-q6zIYeVXp3nFap26CsTpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت شهباز شریف بعد از حملات آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67600" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67599">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
صداوسیما :
نیروی هوایی آمریکا در حملات به چابهار، اسکله‌های «شهید بهشتی» و «کلانتری» رو به همراه برج کنترل ترافیک دریایی این بندر هدف قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67599" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67597">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BOw2ANMtcphAozjxKrO4evM1C8l8Ied5WQ-KjY6dTDmQO9JYNUNDrK-oHhe5s4jfuAkCYmB-xmRhqfxfb47rlDjIyQ5TFOpB7z6b9cO1qTofw3pIR1bwJSLOeskt5sUI1A27K5Rabr-m4gFrKdxLP0G7zo4W2QKh5T3-OhYIki5pZZM-tkDiFKyI8Jue0E98v5Ek-Pgoyj6qMG_pl-WoODx3i5DzvpzgIyRxQgy202kRZX6j6AVvSUUUWQzGXIgWgJdDPjjNBZxw8ZfdaDx9WdJEbFsGbGvGSBt-tzr3uPwujZ6HATdI02NK7riH7WR49YStfdvNemNSWp3C_UQRFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KIutg4NRtF3aVylM0DITNEho_6HAtHVW8N1GjLFBWDIppSeNt_eIXrVjNv9Dmr5Hb_SEWrVvQngBnccSw0rF1jnbnB4nflZL8wNtlwL6buM5ozaZd2GPJY9rUOT0Eb70cjODTmT8fGXiikKTQ2EsxNxKMGP7UiGqp1b2kCzCQTXhcRyuPQmLHQoWL1ZhIRS53U4chbWlwSo2kLDB5MvTNWXth9VC1CxDhmrgqtMrv69Yqm0WXzj3qeEZmpGmOVqWEpVmrOfILl67k47DV7UcBILdJ0r7fksUsj1dAaIxdRQi0eB9cV2W0gAjuTndgvLGUsFXCEU4duLhtgtu33Phtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
برج دریایی اسکله شهید بهشتی چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67597" target="_blank">📅 00:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67596">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🇮🇷
محسن رضایی مشاور رهبر:
دشمن متجاوز و همدستانش به شدت تنبیه خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67596" target="_blank">📅 00:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67595">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
دقایقی پیش مردم در چغادک استان بوشهر ۳ انفجار نسبتا شدید را حس کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67595" target="_blank">📅 00:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67594">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
چندین انفجاردر بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67594" target="_blank">📅 00:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67593">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
فعلا تمرکز حملات مربوط به خط ساحلی جنوب کشور بوده
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67593" target="_blank">📅 00:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67592">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60497304.mp4?token=XSLFUu-RqgI67ApmdB-YmMKWShA4GflDey0HseuD8CfRH0zPhrjK3-KKf0wO_a4QHSd9Zf1DScjGR0AAxeIHrxEVCBaJ_ZzffXHPHHw04j3Uj6CaDLykS6kaaXQ9VsDye4HEZCKzssJOuk2c39hxfIxQshoCBVqb69h8aJJG1_ILKYJrCOfSrLyjoo1L4W1f5pqCDkv8yFMq6kYp1wcF3ZfLq5PWmuQ-EfazjGP1aE9od3KHlorc8MVnhbUujoAjLzQd2EjIYnWPrJB9YTlhX-s3ctq1tov_DbWV-c30LxWQOYB-3vDdokTZUY5GCZt8bUL7x1GvQVTSaIQ0ySg6Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60497304.mp4?token=XSLFUu-RqgI67ApmdB-YmMKWShA4GflDey0HseuD8CfRH0zPhrjK3-KKf0wO_a4QHSd9Zf1DScjGR0AAxeIHrxEVCBaJ_ZzffXHPHHw04j3Uj6CaDLykS6kaaXQ9VsDye4HEZCKzssJOuk2c39hxfIxQshoCBVqb69h8aJJG1_ILKYJrCOfSrLyjoo1L4W1f5pqCDkv8yFMq6kYp1wcF3ZfLq5PWmuQ-EfazjGP1aE9od3KHlorc8MVnhbUujoAjLzQd2EjIYnWPrJB9YTlhX-s3ctq1tov_DbWV-c30LxWQOYB-3vDdokTZUY5GCZt8bUL7x1GvQVTSaIQ0ySg6Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67592" target="_blank">📅 00:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67591">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67591" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67588">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQanECC-APEdBoo8EEMB1FPbhHvlIi1yqnuC3GntplAXuvvAFVy3-xRFOo3FatWlErxx96qirnoMqxtWRw5TPNsk1kBtpGdCSYegzl5VbW6JsHIzQy0BAYX7M-LXsMcEkLueU0Dzo-s5rT68YdxNjCYcIjXDA0Y5iTvA8EknEVxcS6ozbiZz2Ehq7JFnf93TPver08OvTKtwrkL5Zminbv9EujvZchVzYgWXMbTx67ytPJ_scTr0Bhqx5_bxlxgSYM6UcWkcWXtQaYGDqqggTOwPKbtA_dYRQquLxbKbb8SgEav4X1UXrrfbLIQukIi2lvfY5jgkjxCGy3gakrjfWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6afb0f1898.mp4?token=ruwjN-xeqr8Ohbc5FbSI2QlayJq01joDFO3cPyA6g7fDBXKq9-OPGEzXmkGPKCxVcv5BvuWbkkvbjCv-sW_KYC_oYYwp1btugNluxvQq9OMgM9MmNW3bxS7KSzl9TMMlGGGqvZWGqCiaF-56l1q5YTT2wujOVIj42RJO-ecfWWJBmvCLsLDxyOtk_XkRKK8fEyFufEbxVPY5CLdeakOR9C0sCUFRO4bJkxsr6R579gS72ryuaDHCCtl-LaUFTR0vrVjkfZ1EZ8WJzAoK-lvDuZa4VyFJIyonP0MYJvvlyyM_4LBuI5T1OCoJpDSaWbnWIh8uiGBAHRWE75n2Q9969Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6afb0f1898.mp4?token=ruwjN-xeqr8Ohbc5FbSI2QlayJq01joDFO3cPyA6g7fDBXKq9-OPGEzXmkGPKCxVcv5BvuWbkkvbjCv-sW_KYC_oYYwp1btugNluxvQq9OMgM9MmNW3bxS7KSzl9TMMlGGGqvZWGqCiaF-56l1q5YTT2wujOVIj42RJO-ecfWWJBmvCLsLDxyOtk_XkRKK8fEyFufEbxVPY5CLdeakOR9C0sCUFRO4bJkxsr6R579gS72ryuaDHCCtl-LaUFTR0vrVjkfZ1EZ8WJzAoK-lvDuZa4VyFJIyonP0MYJvvlyyM_4LBuI5T1OCoJpDSaWbnWIh8uiGBAHRWE75n2Q9969Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو منتسب به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67588" target="_blank">📅 00:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67587">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac1596adc1.mp4?token=bYS05A1L_6lYb-UAqnARxqc0B7IDcBi5J3hnxpVHjW7oyw7JwStjE4h09DTd15q6gALL2I0oPZi1mJq8iVHS3SuW1ZOZ0gXFNzWwZogsB4Tvcnq3hAUxmlOqvdTmGy94G_fXENToKOj-odaMjy3TIdUECg3wpmHOYKJ-K_9VwKolljlSFS2zp1OVwW0Sok57-FO1sOo-XUXfPWvqIcMR-94fsoz-ZHOQcMx9-uXC3Jm7olJ7UT8H4A07QG7X01CamSvEXpte2OlCXK5oBEIWQ-Ryim9sytQdmi16s-Ze-ljpbfhrAhiwrQd1-wVk0-KJwKAijBETwDFJ-i3NrT7EkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac1596adc1.mp4?token=bYS05A1L_6lYb-UAqnARxqc0B7IDcBi5J3hnxpVHjW7oyw7JwStjE4h09DTd15q6gALL2I0oPZi1mJq8iVHS3SuW1ZOZ0gXFNzWwZogsB4Tvcnq3hAUxmlOqvdTmGy94G_fXENToKOj-odaMjy3TIdUECg3wpmHOYKJ-K_9VwKolljlSFS2zp1OVwW0Sok57-FO1sOo-XUXfPWvqIcMR-94fsoz-ZHOQcMx9-uXC3Jm7olJ7UT8H4A07QG7X01CamSvEXpte2OlCXK5oBEIWQ-Ryim9sytQdmi16s-Ze-ljpbfhrAhiwrQd1-wVk0-KJwKAijBETwDFJ-i3NrT7EkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
لحظه انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67587" target="_blank">📅 00:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67586">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
دو انفجار در جزیره ابوموسی
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67586" target="_blank">📅 00:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67585">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f9c6b6a4.mp4?token=RZzFbc4X55MT7XWV7ciI2Kag96wo4dbVBf_7_f3jALoQMnShQucaUJfGmrALAZhKXtsFVve02uXWBWD8ZfWYfEzPxhfy2yBr1lMei7m3hwjxbMIftAf5siw4E9PjTdkWb4nb6BseNqRZE3eaSYvgB9WOtgY6-S9oFjRf-ztv8gM3-LErH12GndowKj34D_UNUI1YuCeCvjUX8S10bArOqZ24Ur7TJR1rpafXsq2rfo3HmNz9N282RlMaAmwo5I9ny3QkjI3ioifUKdK6aIhX7iWg1EW4CjDflAGoVCFvvA4BcwINRVY9qFaL3qCXORSDkx761IjLS7kNj3wWck3kOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f9c6b6a4.mp4?token=RZzFbc4X55MT7XWV7ciI2Kag96wo4dbVBf_7_f3jALoQMnShQucaUJfGmrALAZhKXtsFVve02uXWBWD8ZfWYfEzPxhfy2yBr1lMei7m3hwjxbMIftAf5siw4E9PjTdkWb4nb6BseNqRZE3eaSYvgB9WOtgY6-S9oFjRf-ztv8gM3-LErH12GndowKj34D_UNUI1YuCeCvjUX8S10bArOqZ24Ur7TJR1rpafXsq2rfo3HmNz9N282RlMaAmwo5I9ny3QkjI3ioifUKdK6aIhX7iWg1EW4CjDflAGoVCFvvA4BcwINRVY9qFaL3qCXORSDkx761IjLS7kNj3wWck3kOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هم اکنون؛ آنتن زنده شبکه خبر
رئیس کمیسیون امنیت ملی مجلس: آمریکایی‌ها بدانند پاسخ کوبنده‌ای به آنها خواهیم داد و امنیت را در  هر جای دنیا باشند از آنها سلب خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67585" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67584">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36b350a9ac.mp4?token=LPSMfsBt75dmi3-7Fkbi-kp6jgytuB-oXeZXjXJZnfq8MJNSDPBritYsbqkkwjUakK1RBR8SIiyNzhK_pGYK9-uV85l8zKCihQDox4kO2TVHNc6PG6FlqeI75y4jD8csWKy1vjkOaxxhmtQ2xZz3KdkuXamL61kAotvSumQz2oRE2m-_8tfpwhZBJUiF5XfG5JUmNzd4M33D4VE597cUccxBWg_-4cbBK1SeWDERG-2bIKsqCfY9iHKGL6fS9LlRWZEcyIfeaFS3KoGrmVnMmkNcKqLHlGgHWSSELAraFJVGYz-h7A-D0ZWWVLsw_hv3K4YtYsSC_txwKf1GxwuDUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36b350a9ac.mp4?token=LPSMfsBt75dmi3-7Fkbi-kp6jgytuB-oXeZXjXJZnfq8MJNSDPBritYsbqkkwjUakK1RBR8SIiyNzhK_pGYK9-uV85l8zKCihQDox4kO2TVHNc6PG6FlqeI75y4jD8csWKy1vjkOaxxhmtQ2xZz3KdkuXamL61kAotvSumQz2oRE2m-_8tfpwhZBJUiF5XfG5JUmNzd4M33D4VE597cUccxBWg_-4cbBK1SeWDERG-2bIKsqCfY9iHKGL6fS9LlRWZEcyIfeaFS3KoGrmVnMmkNcKqLHlGgHWSSELAraFJVGYz-h7A-D0ZWWVLsw_hv3K4YtYsSC_txwKf1GxwuDUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67584" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67583">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02d221609.mp4?token=jSm72NtE_sAFD_RcHbRbiRS-LNV75yt-_TWzlkrSI6xkquUBY-j5xyjCIWqRV9MrVbigiMjCyhgNXC3iasYlgDPzTOtUquNgSLk0N80H9e7ZL0LeoTuQR7aMYzLw6pEX9TXys2BXTfZgxE9NqyBXQphLaTXY5poXjskvL_I9d1hzCZEb166gnfqBFl-QQMpkwoPzuIxQk3P4ejyWl81d4icQkOnWs6Tq1m07cMmr3-Lay0n1qLDjLad0hS9V_KhxONLLBtLxEb4Rr_-zz6KtClfS7ELExKZYPKwCkJ5YjtcdwQuct_EXPDbS0D5fBlER2Cs8qXVs-F5fOytMLSbrog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02d221609.mp4?token=jSm72NtE_sAFD_RcHbRbiRS-LNV75yt-_TWzlkrSI6xkquUBY-j5xyjCIWqRV9MrVbigiMjCyhgNXC3iasYlgDPzTOtUquNgSLk0N80H9e7ZL0LeoTuQR7aMYzLw6pEX9TXys2BXTfZgxE9NqyBXQphLaTXY5poXjskvL_I9d1hzCZEb166gnfqBFl-QQMpkwoPzuIxQk3P4ejyWl81d4icQkOnWs6Tq1m07cMmr3-Lay0n1qLDjLad0hS9V_KhxONLLBtLxEb4Rr_-zz6KtClfS7ELExKZYPKwCkJ5YjtcdwQuct_EXPDbS0D5fBlER2Cs8qXVs-F5fOytMLSbrog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67583" target="_blank">📅 00:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67582">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
نور نیوز  :
به زودی حملات ایران شروع میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67582" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67581">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c578ded4b.mp4?token=unAemyi8jigMBsVvXRIAdgRAl8QT0UnfnchWs3ZfXcUo_aT2af9N1Q0BSvVIZWCFS3UTNICTNzPGDF7C4p-5Rg-XEhMsQBe0CbUDQBIaBsDCAqOCBOQuB5DSjK3xoFiTe6SwUsLT-EzGk1zolUclJYrDzBzo_0TuJxdbloZRAXwnTQognUngH28tFGaqhgNCyo3-W_mhTHYcuolnWuZUYTHdBEVZFSe14FlrHLvWtNMSlr1TyaVrPgwAybGaJj3wcdVm2S_WNjHTajLSVE0V6N2wRmRd261OVQoqkMlYd_CYgNpo-j4HZ_xhN2GHMsPpUohlTbPLV5QlPoOUfBjpMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c578ded4b.mp4?token=unAemyi8jigMBsVvXRIAdgRAl8QT0UnfnchWs3ZfXcUo_aT2af9N1Q0BSvVIZWCFS3UTNICTNzPGDF7C4p-5Rg-XEhMsQBe0CbUDQBIaBsDCAqOCBOQuB5DSjK3xoFiTe6SwUsLT-EzGk1zolUclJYrDzBzo_0TuJxdbloZRAXwnTQognUngH28tFGaqhgNCyo3-W_mhTHYcuolnWuZUYTHdBEVZFSe14FlrHLvWtNMSlr1TyaVrPgwAybGaJj3wcdVm2S_WNjHTajLSVE0V6N2wRmRd261OVQoqkMlYd_CYgNpo-j4HZ_xhN2GHMsPpUohlTbPLV5QlPoOUfBjpMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ریشهر بوشهر دقایقی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67581" target="_blank">📅 00:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67580">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce96b4303.mp4?token=dyW2PjW9MQ6Bfsuo6MYXhpwLG2N-oT2dS1dQXsmGQycykVgNH6rAO8pyOMDVYNhw8tI-oPMYR3vEqvdrOjdRv_iXdFheFyztisszpD4-g4hTbU1ytptHPyfz_EljDdUCuU2fGyn5a28379_iN94wATMB0BNMLTNd9UFp5m_V0IZrHw_34zj7yRbpNpIrO7Q3mO797xtHEz_nKjjKEynNpQYzvOGqq89cPd8alSZfKT1PiZBHdYIE4X4YcU9g5-Zje0dwkJTUBaIbfrA0D9C49XikOm_QMERv5QC7zbBjVXWfstRQJbb6Bhxx8Suq1vpO4PRhHRAyMt1K74vJiBAoJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce96b4303.mp4?token=dyW2PjW9MQ6Bfsuo6MYXhpwLG2N-oT2dS1dQXsmGQycykVgNH6rAO8pyOMDVYNhw8tI-oPMYR3vEqvdrOjdRv_iXdFheFyztisszpD4-g4hTbU1ytptHPyfz_EljDdUCuU2fGyn5a28379_iN94wATMB0BNMLTNd9UFp5m_V0IZrHw_34zj7yRbpNpIrO7Q3mO797xtHEz_nKjjKEynNpQYzvOGqq89cPd8alSZfKT1PiZBHdYIE4X4YcU9g5-Zje0dwkJTUBaIbfrA0D9C49XikOm_QMERv5QC7zbBjVXWfstRQJbb6Bhxx8Suq1vpO4PRhHRAyMt1K74vJiBAoJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظاتی از حملات آمریکایی به شهر چابهار، ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67580" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67578">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fc_jLae_I3A6_V_tyoMFVH8o35ytOpLWGnfjRCrFq6xn_e6oif_uLwng6K_pQX530TeuB7gIo7LyztHxMA7zhXZzxLh5VPbwGx6GSRfbKG8NLkUm9OVvqiEHIiBkPPd1T47-chfesCPQ_MFCiLC7SIT3ABM-AwIOiPQiayHhwfhuNn9uC5HV1a35fgLqCfjVjOXjL5SRgAN8PkNA9N8WnYBiHCnC_9SQCZkT9sifKB2VzCaO2M4VibiJ6zm9cFyJI9T63Xp-Zdv58vzgB5aPRzLlkOsN9LefvuFTUrmshJqKzTidtw1ymJNKZuXujf-4wEeL3BvxAU-Q_ymJQm_sww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffKLXQ1p2_gHFmb89hEI0X95DL9g4GW2hejnthwCbbs_XVorCjb-jF3flwba_IxqiYUpq0GpcvFvqnOgrtO29ajaEuUvF9v-D_bs_tcvGa5CcLbsX9PxRD-gqu9RmBIpz_XBqEgPEhZkquuhm6iOCLJ9ypHZVHcSKCaU6yK-GhpwSd6LpmT8qapoO0Vez_l8C3eA91TQJHGz7kOEi-JBY_xok2eWgfm6pbjFDzY5AXxB3WhJFYSKeoE9s8L1MSSfk9zTtqwU2_qNvQDO9G28Dd7W7TL0CIDAEVx4dMjWe66EGGg2fHHUJS91x6obNSSP2Qne6V_tnNTgPCecXyBfQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به نیروگاه برق پایگاه نداسا در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/67578" target="_blank">📅 00:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67577">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e60a602e.mp4?token=XGRNlrcLixg7tUFgUdalF8enDsfHuCLchA2TRk65230mihejtbx9j5lquU4XmspGn4C7fmg3IAoyoJ9TWUM1Jq0RTnDe_vfvOCe-mk6aZUA4Mx6O0ULqjZ76oDepuCf-Ah7PuQgKn1yQvBRqryoeeWjkhQVRJG64hfXhUwpN6kI3kDje20RL62zUdKAbdKPqt6f6vTFvFWXRL9C3rjp6ANmog8DY00mFexfO70zaa49HCxVWULzS_LpwOayqKkguAE-js61tAbSka5VnvdyhRhfunE8FOurVeXg18BhVk6qYxUOzTFBxBcV3s0amaIM-02aaSpNsuvclEzqSiMYbcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e60a602e.mp4?token=XGRNlrcLixg7tUFgUdalF8enDsfHuCLchA2TRk65230mihejtbx9j5lquU4XmspGn4C7fmg3IAoyoJ9TWUM1Jq0RTnDe_vfvOCe-mk6aZUA4Mx6O0ULqjZ76oDepuCf-Ah7PuQgKn1yQvBRqryoeeWjkhQVRJG64hfXhUwpN6kI3kDje20RL62zUdKAbdKPqt6f6vTFvFWXRL9C3rjp6ANmog8DY00mFexfO70zaa49HCxVWULzS_LpwOayqKkguAE-js61tAbSka5VnvdyhRhfunE8FOurVeXg18BhVk6qYxUOzTFBxBcV3s0amaIM-02aaSpNsuvclEzqSiMYbcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آتش سوزی در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67577" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67576">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
گزارش‌های اولیه حاکی از آن است که هدف آن‌ها نیروگاه‌ها است. قطعی برق در چابهار گزارش شده است.
هنوز تایید رسمی نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67576" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67575">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
انفجار های پی در پی در بوشهر و کیش.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67575" target="_blank">📅 00:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67574">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از یک مسئول آمریکایی:
حملات به ایران، رادارهای نظامی، پایگاه‌های موشک‌های ضدکشتی و سامانه‌های دفاع هوایی را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67574" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67573">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
❌
گزارش‌های اولیه حاکی از آن است که یک پالایشگاه در جزیره لاوان مورد هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67573" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67572">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coGVnR-9P6yY64eDntWWENHOpK3SyhjtVzSEhfzemcA7EG6_PeXmnB63EoKWyVJaloZyUpyD_83Is2A4Xq6ed5HiFPO_5iv1rCU9p1MTjRkFQIBt5YgIKo8O8NU49ZYj14g-N5dV2MQ_yrf8qx_V3AWgkpaFhh-LpbNWbUAg8oikgjvNxqvn5oMmlfg4pEN8BYiHjdnf143k3WE_M24p2imrbH_92IO8WQLOzf-vGCv717aV_89E_OLDRsqcgV07Ebb3b3ytp64jMGCbPxFVtZHDVPDWq5HifSMCMzhF3E0aIvUWyuK_Usdb5mZ6pO2wPdxUrxkYliJQGLOF9bsbKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
حملات آمریکا به چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67572" target="_blank">📅 23:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67571">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
انفجارها در بوشهر و جزیره خارک
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67571" target="_blank">📅 23:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67570">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67570" target="_blank">📅 23:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67569">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qY47Zf8ZhaFBMtpJBxP27-LvQ50AVVzGGEXPGjk3ncKOLwwod8BlOCLtFa3NtnuXHMoNsNfk9Ysq9q_FruhIp3Yi7j2nPWGvZPCDKmnslKKL7YqWmNF9Ar78kKdQ6eUPzWnZSsOAjJJKAPx2HQa2mWzaoICr9Hfm-e2LDZCbX6MrErxsWj5szf4jbWrU__U5gWV6jgg3RIOqh8FMFO5n4BYjUEEAd17_w4pgSVmPOktxAB8sU_7abQurOQU30JfjxV0GjgPtXkjCrSAEMdEHa-rqF5tYGrHqgJj0QxQz0pes2Phf3jvks4u6GhyhgBOsILexOsRgstWhSCdfDVP3mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده:
به دستور فرمانده کل نیروهای مسلح، نیروهای فرماندهی مرکزی ایالات متحده، عملیات‌های بیشتری را علیه ایران آغاز کرده‌اند تا توانایی این کشور در تهدید آزادی کشتیرانی در تنگه هرمز را بیشتر تضعیف کنند.
ایالات متحده، ایران را مسئول اقدامات تهاجمی اخیر و غیرموجه علیه کشتی‌های تجاری و خدمه غیرنظامی که به صورت آزادانه در یک آبراه بین‌المللی حیاتی تردد می‌کنند، می‌داند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67569" target="_blank">📅 23:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67568">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
صدای چند انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67568" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67567">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از یک مقام آمریکایی:
ارتش آمریکا در حال انجام حملاتی علیه اهداف نظامی ایران در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67567" target="_blank">📅 23:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67566">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
پادگان ارتش در کنارک توسط آمریکا هدف قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67566" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67565">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
دو انفجار در جزیره لاوان
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67565" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67564">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=NuNhv9itW1PTCZoofyULo5nfmjHYSDfD4Tb_w0IJZVDLGWSs1VG5E3H9FIta-xPHmh7vOJZ3g-GAEdaV0WZa-1Y6eOONxVViu7b711Jm8y2KhdP4-NkpwLA-lg0t7VzaqKfBU7FeSOCim-Y1Az8fyti_-If4gZyV-sQuG92qYsnD-DNdYrmEiCbq8qosEj0rzgKVaAWXPi_SAsu4NcSdDiQsgsL6i5Xi-kf6VHmq0iCv0plT7A8XnCCj0Ue1s8kqkbW_myvKv0yCNmMkOZ0qjFpmXe3vMWQKoe8ahm3fJNJVc2QonlLfulg1WSuSuVB13iBDkTwVU0x1-eCQjizm2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=NuNhv9itW1PTCZoofyULo5nfmjHYSDfD4Tb_w0IJZVDLGWSs1VG5E3H9FIta-xPHmh7vOJZ3g-GAEdaV0WZa-1Y6eOONxVViu7b711Jm8y2KhdP4-NkpwLA-lg0t7VzaqKfBU7FeSOCim-Y1Az8fyti_-If4gZyV-sQuG92qYsnD-DNdYrmEiCbq8qosEj0rzgKVaAWXPi_SAsu4NcSdDiQsgsL6i5Xi-kf6VHmq0iCv0plT7A8XnCCj0Ue1s8kqkbW_myvKv0yCNmMkOZ0qjFpmXe3vMWQKoe8ahm3fJNJVc2QonlLfulg1WSuSuVB13iBDkTwVU0x1-eCQjizm2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات سنگین آمریکا به پایگاه سپاه در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67564" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67563">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
حملات آمریکا به بندر کنارک در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67563" target="_blank">📅 23:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67562">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
گزارش صدای چند انفجار سنگین در بندر چابهار
به پایگاه امام علی در چابهار حمله شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67562" target="_blank">📅 23:33 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
