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
<img src="https://cdn4.telesco.pe/file/arViCvswGiuJrbxt5iQoBfah-JJsuKylYbupPHyKDhjc2m2-jRGgl-T-27JmeP0R0CXMfi1tfMGHQJzMJfX0sRHLnyvIw4yJwett0aYqSA_4nr0Jir6NfyWXzXl1yTba65iSHubQ7uFEFcsdY97sYjYkKPXR4IPnQuSkkEv1Fl3t4cBgbZT3z3desD_6vEP0WnfuhzRcFznbyy_9XVI4cIQeCeD2n8yytOhVGMonyiH4a9vgqlWK0pqFvuFFuVTkVreLf6FbVSROsw9shOSYwsZ3GexcThtCAFQaYpD0W3nvDEH8NnI9nnXzc0qBbjPnfiLIE5tsnagw3ibCg7BTzQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 915K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 22:38:00</div>
<hr>

<div class="tg-post" id="msg-147284">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536ffda598.mp4?token=hmGCDiWd6XNnCOKKT8W81C7Lbva5xWI7LiBL3pQIg84sn3nv_Bo9dXN72jIYSVfukgkHy31BG6einDnHDvwsBXehTnXqCeMVQCVAucl5gb-tlk5aOcxvrge7rRRL9tYnev6mMRJdUztd1HxYC-4kuZnT5NHqV9ZvP5821yjeFXoOn3ZFRCckgzuyQW3tp_RgBLedZ0x4d6iG1otfaM1828Kop5CPpFHEYUnpxuZSGoMeU9WsYullUP8jbvylv0SZyhos8cOKwbiRBECdjd4h-hU0Vi3ASR1j2FkVRgq6Pcad8-26h4QYujhz6qgVxkCbiTtxNsW5xwPQQuXnRGgJ-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536ffda598.mp4?token=hmGCDiWd6XNnCOKKT8W81C7Lbva5xWI7LiBL3pQIg84sn3nv_Bo9dXN72jIYSVfukgkHy31BG6einDnHDvwsBXehTnXqCeMVQCVAucl5gb-tlk5aOcxvrge7rRRL9tYnev6mMRJdUztd1HxYC-4kuZnT5NHqV9ZvP5821yjeFXoOn3ZFRCckgzuyQW3tp_RgBLedZ0x4d6iG1otfaM1828Kop5CPpFHEYUnpxuZSGoMeU9WsYullUP8jbvylv0SZyhos8cOKwbiRBECdjd4h-hU0Vi3ASR1j2FkVRgq6Pcad8-26h4QYujhz6qgVxkCbiTtxNsW5xwPQQuXnRGgJ-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک جانسون، رئیس مجلس نمایندگان ایالات متحده: به نظر من، این ترکیبی از کشورهای متحد ما، دوستان ما در ناتو و سایر کشورهای عربی خواهد بود ... که با هم متحد می‌شوند تا اطمینان حاصل کنند که تنگه هرمز باز بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/alonews/147284" target="_blank">📅 22:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147283">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
تسنیم: حذف سهمیه بنزین ۱۵۰۰ و ۳۰۰۰ تومانی خودروهای بالای یک میلیارد تومان تکذیب شد؛ سهمیه‌بندی مثل گذشته ادامه داره وق فقط نرخ سوم بنزین از ۵ به ۱۰ هزار تومان افزایش پیدا کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/alonews/147283" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147282">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ed9b90c6.mp4?token=NA-wvq2MMzl3qs3kvuaALR70vtvhOfo9NWR8DxLr3ae6eF5Pw1JFwg_0nTfz-3Ty4YDzSuCCUm42rpY1BltnxTceV8jN1C-qDI9U2YKzOpMv9d7LAm_fpFhlqFbQnTSUkXRy8KKAxy_FGBExjGuqacZ14-5ZyPzRK6YMMaC-pYL6801jhRpBudb5FbIwISPzJCJtxb7HxFLvuk9-Rvo2c9_B298om-MAglmrOASR125jXLxIpDairHPOdtBpsl7KCm6t7lEJWlVGgNAiV3mW2oatydhT3E73PzkhUlEUsWFUbrPn-K_zfHb80IlNbonErfmNK-6Y-yZEF7tmnNqsQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ed9b90c6.mp4?token=NA-wvq2MMzl3qs3kvuaALR70vtvhOfo9NWR8DxLr3ae6eF5Pw1JFwg_0nTfz-3Ty4YDzSuCCUm42rpY1BltnxTceV8jN1C-qDI9U2YKzOpMv9d7LAm_fpFhlqFbQnTSUkXRy8KKAxy_FGBExjGuqacZ14-5ZyPzRK6YMMaC-pYL6801jhRpBudb5FbIwISPzJCJtxb7HxFLvuk9-Rvo2c9_B298om-MAglmrOASR125jXLxIpDairHPOdtBpsl7KCm6t7lEJWlVGgNAiV3mW2oatydhT3E73PzkhUlEUsWFUbrPn-K_zfHb80IlNbonErfmNK-6Y-yZEF7tmnNqsQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس مجلس نمایندگان آمریکا:ایران‌ها شرکای قابل اعتمادی در مذاکرات نیستند. البته، آن‌ها هر روز دروغ می‌گویند. آن‌ها سر میز مذاکره می‌آیند، یک چیز به شما می‌گویند و عمل متفاوتی انجام می‌دهند
🔴
برای برخی از آن‌ها، این بخشی از دینشان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/147282" target="_blank">📅 22:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147281">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/147281" target="_blank">📅 22:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147280">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyQIGCwAHe-4u298UE8Wk6GZ_wFevSwRb_JU56rQYW0etRYFTZ2X6XZHpFSiRNoPzMF4Lb_YX1hiPDc3kO4Of4hrhDrTrZpYX5IbSI9-24f_C9qQJciuwmkYBUTPDgqdRCiAOc_A9YbF6DCNxSta_7Si4UUstBFxWD9DZMhYB9JlO7K_I8lZ4Ydqd3SA_gq908XWBMeXCfaMfh960Xw_r2uHynizPQFUuAd0JWkaFRX03GVar4Z4r1om3zk4iUCPAwAY-Qgw-EHBj1H_6np7EEK1hj0d0aaga9TgCMzBRfIqZchzjtgUqIJ7Yg65wH8dHB6fbmpbSrQpU9-FoodM_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فانا: مدیرکل دارو: واکسن آنفلوآنزا در اواخر شهریور و اوایل مهر ماه می‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/147280" target="_blank">📅 22:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147279">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
شی جین‌پینگ رئیس‌جمهور چین ممکن است از دیدار در اواخر این ماه با «دونالد ترامپ» رئیس جمهور آمریکا، خودداری کند.
🔴
دلیل این تصمیم احتمالی از سوی پکن، اعلام تایید فروش تسلیحات جدید از سوی آمریکا به تایوان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/147279" target="_blank">📅 22:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147278">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d776b60914.mp4?token=a2cXxNX6aRTjEu1GGDWHI8kv1s2-BFvZDbk9wGcvODTr4ZkBjQAANMH33iWpuX6kCi1bv8AM-aZx0k7RYuwN1s3eN_gxwwGtz8YGhVIGbdDs2pEWn_YhchtCBmqcyNqYXSyd_b0EwfQvqT25IYwNw3-551tF3P3So_OlqU0ffI8p7ezyIuK5rLk7tdk86O_hQCWms0gwVjsK1KS_e2xLAhcNuXTP5tiHK1Dd8GyM3fOh8NVQxDjrxUX2RR2Mp9JXMld2o1Fj96HgmGa36TpBgvwQt2IbRHJgrWypnXkr8kUE9H0G5kUSBqPWfRF378KP15e0YNEsgvqnHK4PFWr3zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d776b60914.mp4?token=a2cXxNX6aRTjEu1GGDWHI8kv1s2-BFvZDbk9wGcvODTr4ZkBjQAANMH33iWpuX6kCi1bv8AM-aZx0k7RYuwN1s3eN_gxwwGtz8YGhVIGbdDs2pEWn_YhchtCBmqcyNqYXSyd_b0EwfQvqT25IYwNw3-551tF3P3So_OlqU0ffI8p7ezyIuK5rLk7tdk86O_hQCWms0gwVjsK1KS_e2xLAhcNuXTP5tiHK1Dd8GyM3fOh8NVQxDjrxUX2RR2Mp9JXMld2o1Fj96HgmGa36TpBgvwQt2IbRHJgrWypnXkr8kUE9H0G5kUSBqPWfRF378KP15e0YNEsgvqnHK4PFWr3zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند : شطرنج، پاسور و سودوکو باعث احضار اجنه میشوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/147278" target="_blank">📅 22:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147277">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
پزشکیان وارد تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/147277" target="_blank">📅 22:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147276">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سازمان رسانه‌ای اسرائیل مدعی شد ارتش اسرائیل به صورت محدود از ارتفاعات «علی الطاهر» به سمت قلعه «شقيف» در جنوب لبنان عقب‌نشینی کرده‌ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/147276" target="_blank">📅 21:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147275">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
خبرگزاری تسنیم: از روز سه‌شنبه ۲۴ شهریور گردهمایی جانفداها برای آموزش کار با اسلحه شروع میشه و بعد از آموزش به گردان های نیروهای مسلح اضافه میشن تا برای جنگ با دشمن آماده بشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/147275" target="_blank">📅 21:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147274">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b41b26dc.mp4?token=kxzGuE4cxtetqVpJA04Jce9IPb-k3nQTDHhQT3vgVxjK0tp0WtwG9RXHLLc_oEVJ5QvdvkhSpdrcemDDzLPkALQ1ERiqRQB_WUxAAtOEcbAE13Mo-vlyedoWuMQ-NO4EFWDi2SNy4GGn5mn9PXMH8gVl0Uo4UzU8GaCMi5sQD8FWeoVt6R_TWUlyr2VC-BvOa0DUE0LiwJqZs_6lP1nZVVAuwMPBfzZ0yj-MzwfRFM2FzKtVMq2uP2S3Wj4hp2yEns4bgZVixYRunT8hv81kgTyVDPuJ9ogPOjq84-9580io5mPMfy-jLPxv0FvYowCKmVqb27nw5RNf9bJPBaAKsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b41b26dc.mp4?token=kxzGuE4cxtetqVpJA04Jce9IPb-k3nQTDHhQT3vgVxjK0tp0WtwG9RXHLLc_oEVJ5QvdvkhSpdrcemDDzLPkALQ1ERiqRQB_WUxAAtOEcbAE13Mo-vlyedoWuMQ-NO4EFWDi2SNy4GGn5mn9PXMH8gVl0Uo4UzU8GaCMi5sQD8FWeoVt6R_TWUlyr2VC-BvOa0DUE0LiwJqZs_6lP1nZVVAuwMPBfzZ0yj-MzwfRFM2FzKtVMq2uP2S3Wj4hp2yEns4bgZVixYRunT8hv81kgTyVDPuJ9ogPOjq84-9580io5mPMfy-jLPxv0FvYowCKmVqb27nw5RNf9bJPBaAKsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف در واکنش به قیمت ۹.۹۹ دلاری سوخت در آمریکا، ویدیویی از سیمپسون‌ها منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/147274" target="_blank">📅 21:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147273">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJs77_WJ4QfqnqkN986s7pAfl66gMTjh8Hrb0YPkoRcAVAwkAe-0iZ3-zwuMao1GzRhVXsnvi8gMyg6FjDOVxmghSdb4jl8WXlSu2S3fq98ytZ3GDOPjXw_uCSB2GXxJmZFHEDqB2leEzS7j5-88q4mIs-fkoJRcdvgGKpb8V3A7v9t-ze9KM4q1Qi7w5SHdtcraSBtU7V0-hUWKEGXe1E1ALvtkzTDe5a2nA3BusmUhA-Gd7d2cUsXLEZpIf4AOEdSUJrd_RhGW6RMjuhoyLvkO6nkHzahwVdocNO2Z_-h-4K9EzhJ2sjv016m_JTr8h0u2sU18J2c4EgDhSXd28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار بمب مقابل یک کلیسا در شهر حماه سوریه
🔴
یک بمب دست‌ساز مقابل یکی از کلیساهای شهر حماه سوریه منفجر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/147273" target="_blank">📅 21:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147272">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
الجزیره: پیشروی سریع انصارالله در یمن «قطعاً یک نقطه عطف» در جنگ منطقه‌ای است
🔴
حملات هوایی به رهبری عربستان به‌تنهایی احتمالاً برای بیرون راندن انصارالله کافی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/147272" target="_blank">📅 21:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147271">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
حوثی‌ها (انصارالله) اعلام کردند که ائتلاف تحت رهبری عربستان سعودی در ۲۴ ساعت گذشته، ۵۸ حمله هوایی در مناطق مختلف یمن انجام داده است که این حملات مناطق تعز، لحج، الجوف، حجه، البیضا و صعدا را هدف قرار داده‌اند.
🔴
این حملات توسط جنگنده‌های اف-۱۵ که از پایگاه هوایی خمیس مشیت عملیات انجام می‌دهند، صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/147271" target="_blank">📅 21:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147270">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سی‌ان‌ان: عمان پیشنهاد ایران برای دریافت اجباری عوارض را رد کرد و پرداخت‌های داوطلبانه برای ایمنی ناوبری و زیست‌محیطی را پیشنهاد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/147270" target="_blank">📅 21:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147269">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سازمان بین‌المللی مهاجرت: حدود ۸۵ هزار نفر به دلیل جنگ در یمن مجبور به ترک خانه‌های خود شده‌اند و حدود ۲۰۰۰ نفر به جیبوتی رسیده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/147269" target="_blank">📅 21:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147267">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
لهستان: اگر روسیه حمله می‌کرد، فورا شکستش می‌دادیم!
🔴
وزیر خارجه لهستان : ما در قدرت هوایی برتری قاطعی نسبت به روسیه داریم.
🔴
اگر اوکراینی‌ها نیمی از ظرفیت پالایشگاهی روسیه را در شش ماه از کار انداخته‌اند، ما می‌توانیم این کار را در شش هفته انجام دهیم و نیم دیگر را از بین ببریم.
🔴
اگر روسیه به ما حمله می‌کرد، ورشو فورا مسکو را شکست می‌داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/147267" target="_blank">📅 21:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147266">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سه منبع ناشناس به خبرگزاری رویترز گفته‌اند عربستان سعودی در بندر دریای سرخ خود در ینبع تنها به اندازه پنج تا هفت روز ذخیره نفت دارد و مقدار کمتری نیز در مصر ذخیره کرده است
🔴
توانایی عربستان برای دور زدن تنگه هرمز و ادامه صادرات نفت پس از حمله به خط لوله شرق به غرب این کشور به‌شدت محدود شده است.
🔴
این خط لوله روز بعد از حمله، به‌عنوان «اقدامی احتیاطی» متوقف شد. این مسیر، تنها گزینه اصلی عربستان برای صادرات نفت بدون اتکا به تنگه هرمز محسوب می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/147266" target="_blank">📅 20:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147265">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=jyxb7gP241sSpYOGe1OjU0mQhEoaLPNMjB_Ja1qr3u8XTCSZ5rvf1khsJ9vri1oHT_2PSXYOIZZFxfkrjQBarXxS0z5vIW9wf4eY7ousfzTHVtucSZY5X8Q4b00FI4UveqvozvXUeVgs4ZMe0hPO6sfuV3jaK91T720S_v_zVS832cGbHt9goXMxZ_xnITCkTowGxOjL8sKO_nBxdk1_-bnpG0v83DwC3OA9Yg63vjvwY2idBWjiSIQMloeLwGqkmRFzsYhtv4K7y84x5gEAxwJfFkjPg0hKbEUcQHTVsi59YCk1ZIbIKfsI7GzZy8FWWCwcqkAuo9hxBms_NnuBOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=jyxb7gP241sSpYOGe1OjU0mQhEoaLPNMjB_Ja1qr3u8XTCSZ5rvf1khsJ9vri1oHT_2PSXYOIZZFxfkrjQBarXxS0z5vIW9wf4eY7ousfzTHVtucSZY5X8Q4b00FI4UveqvozvXUeVgs4ZMe0hPO6sfuV3jaK91T720S_v_zVS832cGbHt9goXMxZ_xnITCkTowGxOjL8sKO_nBxdk1_-bnpG0v83DwC3OA9Yg63vjvwY2idBWjiSIQMloeLwGqkmRFzsYhtv4K7y84x5gEAxwJfFkjPg0hKbEUcQHTVsi59YCk1ZIbIKfsI7GzZy8FWWCwcqkAuo9hxBms_NnuBOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محسن هاشمی: من خبر دارم مسئولین در هر دو جنگ از تونل‌های مترو به عنوان دفتر کار استفاده کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/147265" target="_blank">📅 20:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147264">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0fa531cab.mp4?token=H0uDwrGh8JZhm6t7b3F2jN6bFSpDH-0iCTGAfA-brodx20CNuj7W4SqI1qQ9Rr1r3qgQpKubt6w5RZW4IXr0LycoxQ6A5_PVQq7VnIHMUsmP-JBgsrBHn9t00Z1baoELuS9jea1CPMerA9i63qtSosLKPEywRNeLJ2NyAQvqn8mwPIcTc7TozDhEZM7SqeIHNyrGXVzzQxaTP2dYxqXkFXJQK_LDXqDNJrFF77JhQ-oQb758eGYjyAp3FKGPF4WFa778tayGvspw1sM1Ae0IJFCMGG7ZsF59k5yhG5n824ZxqdxHpAaKdxIn9Lc-BtJk51q-nLI0Z-hPbtJi5OZZPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0fa531cab.mp4?token=H0uDwrGh8JZhm6t7b3F2jN6bFSpDH-0iCTGAfA-brodx20CNuj7W4SqI1qQ9Rr1r3qgQpKubt6w5RZW4IXr0LycoxQ6A5_PVQq7VnIHMUsmP-JBgsrBHn9t00Z1baoELuS9jea1CPMerA9i63qtSosLKPEywRNeLJ2NyAQvqn8mwPIcTc7TozDhEZM7SqeIHNyrGXVzzQxaTP2dYxqXkFXJQK_LDXqDNJrFF77JhQ-oQb758eGYjyAp3FKGPF4WFa778tayGvspw1sM1Ae0IJFCMGG7ZsF59k5yhG5n824ZxqdxHpAaKdxIn9Lc-BtJk51q-nLI0Z-hPbtJi5OZZPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرمانده مرکز فرماندهی نیروهای مسلح ایالات متحده (CENTCOM)، ادمیرال برد کوپر، می‌گوید که نگرانی‌ای درباره کمبود مهمات نظامی ایالات متحده ندارد.
🔴
«ما به خوبی تسلیح شده‌ایم و برای هر سناریوی احتمالی آماده هستیم.»
🔴
در پاسخ به پرسشی مبنی بر اینکه آیا نگران تهدیدات آینده است یا خیر، کوپر پاسخ داد:  «من نگران نیستم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/147264" target="_blank">📅 20:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147263">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
با وجود عدم پیشرفت در مذاکرات مستقیم دولت لبنان با اسرائیل، سفارت آمریکا در بیروت، از دور جدید مذاکرات دو طرف در ماه اکتبر در رم خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/147263" target="_blank">📅 20:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147261">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزیر خارجه ترکیه: تنگه هرمز اقتصاد جهان را «بحرانی» کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/147261" target="_blank">📅 20:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147260">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پرسیدن دلار 235 تومنی خریدم ریخته؛ چیکار کنم؟</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147260" target="_blank">📅 20:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147259">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
قبیله بنی حشیش علیه حوثیا اعلام جنگ کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147259" target="_blank">📅 20:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147258">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
مدیر سامانه هوشمند سوخت گفته خودروهای بالای یک میلیارد تومن دیگه سهمیه نرخ یک و دو نمی‌گیرن
🔴
پ.ن: خب قرمساق مگه الان ماشین زیر ۱ت داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/147258" target="_blank">📅 20:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147257">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
رئیس مجلس نمایندگان آمریکا؛ جنگ علیه ایران ادامه ندارد و اقدامی که اکنون سعی در انجام آن داریم، حل‌وفصل جنگ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147257" target="_blank">📅 20:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147256">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سازمان ثبت احوال: در کارت ملی‌های جدید از هوش مصنوعی و بلاکچین استفاده کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/147256" target="_blank">📅 20:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147255">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Inp0rY-BpKXTC1XSfZsRn_Gw55C9MdJ0qOqiC3Wkq96jiGeMp6E2MsGQiGeq_weT34jZZlFEm-J2xCLOIcYcC5Zjj-GMSmpsGPjyJavbhZUZVrFDIKH5QnFhOUtOcrO5-aivGiusjdE4f3WLKuZyMpn_ITmvqOVFluPb72D4cu6OPt7JIOFhEEfaAZRctTNkMSIFU-MXtcegCsqVa3yFh9O_j4mpxuvVptUHZanmVdGvxsWZfH4o2MZn-SJNSMXo1uIuKJ0eY7XgWiztYSBFSumANCa2L_U8VKH2zvllb_iwz7GE02YTIRPZqE0QdCP7MazAIJszPOUwiVBHU2mD2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک حمله هوایی اسرائیلی به منطقه‌ای بین شهرهای زوطر شرقیه و مایفادون در جنوب لبنان هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/147255" target="_blank">📅 20:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147254">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhPNZiyiIliMEn8t-nn0kDGOhqHHQmpX1qZfWP94saZbBIH0ddpdhjxjcW7cPuWMFjyPWedgt01Dmk_UftSkkjDs5nSR2_Ova16q-3neYP1owRyJxNcQ5U92boVO8cwakLZdKaCLaPjT6KavBHAE7uSZRt8pcPULeFfxmd_ThBNqW_3sMOQnIjHp7jm0bRxKMwhBMV3Tt8W2ZNZU2vNhqFgfYyJNUOsMwbGTpR_aw95jwt-lDTjrgT70nVMVlA3TqdNa7tk-PadDulmZA-HIUPPscohIaTpLfz1erchI9ns3phA3qcvADZoNrqrL1cpn4Z7uiItymxHtc2KasGDuKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لیست قیمت انواع موبایل ریجستری در بازار
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/147254" target="_blank">📅 20:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147253">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
روزنامه رای‌الیوم: اولتیماتوم سخت عربستان و اردن به عراق؛ گروه‌های مسلح را منحل کنید یا منتظر پاسخ باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/147253" target="_blank">📅 19:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147252">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a702c90e1.mp4?token=bJak475-ygva5pmvleqbWgidor8GOukNvViLIdy5NtTXZEx47Z85Hu0TbNc1n0dipe2mJkz3rSr6lztGkrkh6s3NegaECtFnGdQqWlWolylEJD5qGKh3yHJSy9b3k5XPC__vnCoRa6O3LBXNVHDqs_Z34OxPZm7egYtb3tgqC3NoERD9RvgWTizuOqAXIuuC5wJxRFu1tiYS0qVE-UhZ42t2_6_kn77bUxSkm51xw4GchUqW1y_JEkcWL4CNAk-GVxCcFMELIvAsmvEwF0kkkRsq1R9CnEooMlFCcmpgcP9dYwTf1Yh_R2Lx3mikTkKsfoCovh8MeR9iqPbiDisJeCbJWHpE92kKt2RdmKhTrROc0YHX5pk2nK_5I09v4_RudE4OgNUJ3YELXqOAlPxZM-18-pCvXYN62uschz7uF0rK27R7wVJhSIV76z-plplJnxk4iD4-PdS2MtmdqNXjgpnXiDfkN2TcqHofY5O_4HbrMa8ziCan4bJzyBc9euB7W2UBZYOF0WNcla56-28dHAxJwlKhXHszKWd8-WzQ0vSoAzZZVY3yLErY-90ONr2-mbmka4FLETgWcJ6B4kj2Vf97xzhQs6W8sr8PzSjMAR2tEJI6T0I0uIKLlp5_rG440_uExXSNfgZ6Q-mbTDZeiIlOT7AfZcskI0yRXxkkWhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a702c90e1.mp4?token=bJak475-ygva5pmvleqbWgidor8GOukNvViLIdy5NtTXZEx47Z85Hu0TbNc1n0dipe2mJkz3rSr6lztGkrkh6s3NegaECtFnGdQqWlWolylEJD5qGKh3yHJSy9b3k5XPC__vnCoRa6O3LBXNVHDqs_Z34OxPZm7egYtb3tgqC3NoERD9RvgWTizuOqAXIuuC5wJxRFu1tiYS0qVE-UhZ42t2_6_kn77bUxSkm51xw4GchUqW1y_JEkcWL4CNAk-GVxCcFMELIvAsmvEwF0kkkRsq1R9CnEooMlFCcmpgcP9dYwTf1Yh_R2Lx3mikTkKsfoCovh8MeR9iqPbiDisJeCbJWHpE92kKt2RdmKhTrROc0YHX5pk2nK_5I09v4_RudE4OgNUJ3YELXqOAlPxZM-18-pCvXYN62uschz7uF0rK27R7wVJhSIV76z-plplJnxk4iD4-PdS2MtmdqNXjgpnXiDfkN2TcqHofY5O_4HbrMa8ziCan4bJzyBc9euB7W2UBZYOF0WNcla56-28dHAxJwlKhXHszKWd8-WzQ0vSoAzZZVY3yLErY-90ONr2-mbmka4FLETgWcJ6B4kj2Vf97xzhQs6W8sr8PzSjMAR2tEJI6T0I0uIKLlp5_rG440_uExXSNfgZ6Q-mbTDZeiIlOT7AfZcskI0yRXxkkWhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نظر علی دایی درباره مافیای خودرو در ایران:  کجای جامعه مافیا ندارد که صنعت خودرو نداشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147252" target="_blank">📅 19:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147251">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
روزنامه اسرائیل هیوم به نقل از منابع دیپلماتیک منطقه‌ای نوشت محمد بن‌سلمان از طریق آمریکا با اسرائیل تماس گرفته و خواستار دریافت اطلاعات و کمک‌های دیگر شده است
🔴
به نوشته این روزنامه، هدف این درخواست جلوگیری از بسته‌شدن تنگه باب‌ المندب توسط انصارالله بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/147251" target="_blank">📅 19:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147250">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJU3I8mmz14R82U5Ax2X8zMaEVIBddiG7s4AnEDC--q26GogLEHCaJ3kxNbKaadCJqv8it_7IeIZpYpUMLZX9gGtMbStDRhBAMxG73l6BTm1RSH3oxT5nr9LjcQf8f1OLamBZSISLrcsCdrl4Sl2xz_gQuJz3HP-ERBI9kdhrOYno2v6sFDatLLJd3WYv00JWdAIHN-5Yd3fT2uki-aIxLa06qsBw62EXVsVeRctur76CICOxjX8-AGAt4jPGG7LzLRvOnihRSQuX0VsrwWbxUNaDEqhQYKvsTb7e-VOLAWMOx42UdEI7QHM-5f6foBWul1SAOouO5QUHdJ6v0cSGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع عربی: جنگنده‌های سعودی جزیره حنیش در یمن را هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/147250" target="_blank">📅 19:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147249">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک منبع ارشد ایرانی:
نشست روز دوشنبه در عمان بخشی از برنامه ایران برای تقویت اعتماد میان کشورهای منطقه است
🔴
با این حال، توافق به معنای بازگشایی خودکار تنگه هرمز نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/147249" target="_blank">📅 19:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147248">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOGT_h67-g5SDFmEwjZoQFwGTTLsb0FRUmGymemwjdqQqpwtEMOSkdJeSFTAzvM4KevbcMwdDH1QTdctmN3ho63hweWiF_Srd2HCsuAiyPzH31z-68d-6ZGT48fM14JeGYst6WKimsrhavXZ7d8FzdKYqhCTweptMJZwQb2Fx9guogRBQdJhtyEG-zg6TVCAVU08qRaA1-VxxZaLQgYlef46YEgZLlAdyCm06sAsKuvahOjozvlTGqEDy9FPYHRZr6d0ipeNeELXeukxG9c95c53Zl78Ys4jgcLpL-DvU1hdT2Q4OB7g2gtnl5h2mi54rmjCvhBZA0-Ef916you7Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
نقدعلی:
رژیم آمریکا رفتنی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/147248" target="_blank">📅 19:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147247">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6466153e9f.mp4?token=L1rcrrgHuIFsddLmGsZRgAzwK-agpEU5zhkdz0rBL_yxAPTl-i17TvqpGaaHbkDAr3c5Aj96uV2n8ZnmnC8ITRCP4vuV9LfnloV-dBTkmnwUPXgM9-KjPVz3Hy8b_5kraGiK-G2093-KvndHAiTc70JDZWjmeRE8IPEr53ofJ1LkMbfn0aL1UlVV4vGYcWR6xO35ubnVRsvHZFNpJ33Ez8VMoqvMncVkMO-M40AwO-8JFWNbTA392YXlcXkQ1Qi2CqJkkiAkF_kpzRFT5UxSnBbuHHuWJurFqQri7OGXGSv51u-e343hewYh_HCmXMzyKQeqir5isTwAzxrgnpib9jFNAbitYH8FUoEvqgGWgHgngf1kx8Nqc4Kx_9h2aVqHyYSucttM3ccxJaLNXxfTXuBqD2VrgfqN5hsFGFvP4_-GS1aq9iKOisUClOMqbldz8EM51hMxcnlKxOh_9KY-3e3DnRQfafF4zyTTjAqZBEvh29foRygzA5G0bJ5JHWaWXfLKoTqbljCee-DM7vEXwjxnTsh1OCjTzhGpca6Yxf3z0bLk9Ax9iyp-lZMzibn0WMUr0jgFvqB5FG4wj_7M0BCi5AwkUgBn6dEGwGFxF0eePgZsObo36GxRqLYYk_ajv2KdXR7TcLQa8p6KL6G1XWd2BbIjuMRZ3Bevg8R-u4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6466153e9f.mp4?token=L1rcrrgHuIFsddLmGsZRgAzwK-agpEU5zhkdz0rBL_yxAPTl-i17TvqpGaaHbkDAr3c5Aj96uV2n8ZnmnC8ITRCP4vuV9LfnloV-dBTkmnwUPXgM9-KjPVz3Hy8b_5kraGiK-G2093-KvndHAiTc70JDZWjmeRE8IPEr53ofJ1LkMbfn0aL1UlVV4vGYcWR6xO35ubnVRsvHZFNpJ33Ez8VMoqvMncVkMO-M40AwO-8JFWNbTA392YXlcXkQ1Qi2CqJkkiAkF_kpzRFT5UxSnBbuHHuWJurFqQri7OGXGSv51u-e343hewYh_HCmXMzyKQeqir5isTwAzxrgnpib9jFNAbitYH8FUoEvqgGWgHgngf1kx8Nqc4Kx_9h2aVqHyYSucttM3ccxJaLNXxfTXuBqD2VrgfqN5hsFGFvP4_-GS1aq9iKOisUClOMqbldz8EM51hMxcnlKxOh_9KY-3e3DnRQfafF4zyTTjAqZBEvh29foRygzA5G0bJ5JHWaWXfLKoTqbljCee-DM7vEXwjxnTsh1OCjTzhGpca6Yxf3z0bLk9Ax9iyp-lZMzibn0WMUr0jgFvqB5FG4wj_7M0BCi5AwkUgBn6dEGwGFxF0eePgZsObo36GxRqLYYk_ajv2KdXR7TcLQa8p6KL6G1XWd2BbIjuMRZ3Bevg8R-u4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان:‌ با ولیعهد ابوظبی توافق کردیم به آینده نگاه کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/147247" target="_blank">📅 19:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147246">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کانال ۱۴ اسرائیل گفته ایران داره آماده آزمایش بمب اتم میشه  قبلش هم میخواد از npt خارج بشه!   البته ممکنه این بهونه حمله به تاسیسات کوه کلنگ باشه.  @AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147246" target="_blank">📅 19:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147245">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECbXGovs4yRKQOEJw4lhLiyE-mU310ZHHcQamwyKHbJ4SebDzy3sWYyzuHHi0gaA74_r8mQ9cb8nwuqU_adDS5NuSVq-M3wPcNx0ZkeibBtazYOJc2QKPK2mTWzUdyV59cWx2p_UM3Uvzcj1kXvKRU3MxD29b1fwEjWRVdv_q9A3AyMw-v9Y2JM_rDMqqVbqUgdtJiFQiEZF-bqK1YA3yDIQsaYy2JefJon2kF0xodNmHiRraSYAukxTvU9Pd32koadbk369QeJTlY8deu9L57IyPOrtRHMBXOnJoCzGgkk1KMpBnIjDKnHW9NzYzGwCBzudSX30xQx-Rqo5KTQCVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبر خوب/استاد خوش چشم که بخاطر تحلیل‌های کصشر و اشتباهش ممنوع التصویر شده بود از امشب مجدد به صداوسیما میره تا مجدد تفت بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/147245" target="_blank">📅 19:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147244">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
فارس: اگه جنگ بشه، جانفداها میفرستیم‌ جلو
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147244" target="_blank">📅 19:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147243">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94a010ef6.mp4?token=K6ziD4ru9E8kKCO5wchF13uf7HtD_VMug__q_TEbHRCv7P7FpYwrD0SLfl8XnBd6dxX6NpZDfO6QhUjg7tzEQyDGP0a91oSEiPsnzEnqMIRg2fBF0GxOqf1imjrX2nL5kNBSK2bqrM_SQe41uDoBqjz3Yx8KaYTuyd3NO-zudeSDeWmE9NkbkZyKxU_SsDqUdFAfhVYfjlHiNhAI3k0hrf9zxdYyQNYK4GIBfKbVVyxs2nQEK3IBOY_g0idoGFy-QB2_Zuh8tWrOhNVVCLwLPIVRZeiGUe90_kdVJNSzcsD_KYMgKDwyEjTqTruEfIFDACCZI1OaBU6kyOGBRlugVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94a010ef6.mp4?token=K6ziD4ru9E8kKCO5wchF13uf7HtD_VMug__q_TEbHRCv7P7FpYwrD0SLfl8XnBd6dxX6NpZDfO6QhUjg7tzEQyDGP0a91oSEiPsnzEnqMIRg2fBF0GxOqf1imjrX2nL5kNBSK2bqrM_SQe41uDoBqjz3Yx8KaYTuyd3NO-zudeSDeWmE9NkbkZyKxU_SsDqUdFAfhVYfjlHiNhAI3k0hrf9zxdYyQNYK4GIBfKbVVyxs2nQEK3IBOY_g0idoGFy-QB2_Zuh8tWrOhNVVCLwLPIVRZeiGUe90_kdVJNSzcsD_KYMgKDwyEjTqTruEfIFDACCZI1OaBU6kyOGBRlugVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رؤیت شده در شب نشینی‌ها؛ عرزشی‌ها شعارهایی علیه حسن روحانی دادن و گفتن «از آمریکا تو دل بکن، خیلی خطر داره حسن».
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/147243" target="_blank">📅 19:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147241">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🤫
اگه توام دنبال کد تخفیف
🆓
📌
دیجی کالا و اسنپ و ..... هستی بیا
👇
🛍
https://t.me/off_khooneh
🛍
https://t.me/off_khooneh</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/147241" target="_blank">📅 18:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147240">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
محسن زنگنه، نماینده مجلس: من نماینده مجلس بی‌تعارف میگم ما رانت داریم؛ این مسائل قابل حل نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147240" target="_blank">📅 18:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147239">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏
👈
تسنیم: جانفداها اماده شن که قراره ببریمشون کنار نیروهای مسلح
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/147239" target="_blank">📅 18:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147238">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
مقامات جمهوری اسلامی به نیویورک تایمز:
🔴
ژنرال‌های تندرو، از جمله سرتیپ
سید مجید موسوی
، فرمانده نیروی هوافضای سپاه پاسداران، یک طرح جنگی مفصل را به شورای عالی امنیت ملی ارائه کردند.
🔴
این طرح خواستار گسترش حملات علیه نیروهای آمریکایی و زیرساخت‌های نفتی منطقه از سوی سپاه و گروه‌های متحد آن، به ویژه حوثی‌ها (انصارالله) در یمن و شبه‌نظامیان شیعه در عراق بود.
🔴
رئیس‌جمهور مسعود پزشکیان و رئیس مجلس، قالیباف با این طرح مخالفت کردند و هشدار دادند که این طرح می‌تواند کشور را به یک جنگ بسیار بزرگ‌تر بکشاند، باعث افزایش حملات هوایی آمریکا شود و بحران اقتصادی این کشور را عمیق‌تر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147238" target="_blank">📅 18:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147237">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a1d14cafc.mp4?token=OcoPfBB6l9Tn_CE-la0-H4LBB7ZfdpwmyexhKrRjAxziZdSCrJi4dmgta0GyQGXi8DRyxGxkMDF5MQliNlc9Cpm_Q-NZWmpR3GuLbYHr5hmzBio5uGlwMP2ElOAU7UbJScx-rjKiS7YtIvmnzIVHaALx4yCFutMJOOXzBRCMhTbDJ-1DjoaxdS91fSqAwb28YQNm9G_YPiUjmfDDJdvFDHHHL4-KtvPidaf8J-xMaVD-Ev2ckC0O776w8GYkSD6gXpzHhU54JBZtrb17AIHl_V6JR1UHuCyWKYr4113MEnehFTd0ykkB-fKn-U7yip5SBDtHmOeeJreRBAOY1IXlaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a1d14cafc.mp4?token=OcoPfBB6l9Tn_CE-la0-H4LBB7ZfdpwmyexhKrRjAxziZdSCrJi4dmgta0GyQGXi8DRyxGxkMDF5MQliNlc9Cpm_Q-NZWmpR3GuLbYHr5hmzBio5uGlwMP2ElOAU7UbJScx-rjKiS7YtIvmnzIVHaALx4yCFutMJOOXzBRCMhTbDJ-1DjoaxdS91fSqAwb28YQNm9G_YPiUjmfDDJdvFDHHHL4-KtvPidaf8J-xMaVD-Ev2ckC0O776w8GYkSD6gXpzHhU54JBZtrb17AIHl_V6JR1UHuCyWKYr4113MEnehFTd0ykkB-fKn-U7yip5SBDtHmOeeJreRBAOY1IXlaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا و سیما: آمریکایی‌ها بارها گفتن با زدن تأسیسات ایران تونستن ظهور امام زمان رو عقب بندازن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/147237" target="_blank">📅 18:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147234">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOXvCp8fVs7CW2EcJtbO0oOxvhPit26hWyxq1Uchm0dGtyitYQYrkNG0td6avMbOGF87_I33_Tt3zNP1e3l4knD6f2r0yLQpGmv5EaCMpFVIvA9r_P5JM8DhL0jvdX2M5WnLQF_k_FvwGr18ZbcMABF7rn6t7rzu5429g0ov-SOicUFqqvZOFMsd4ALnHN__8yzgmB77O0LoRB6WM490pkPlDAtL5w8mQk7vcwbE0NP1GJk75Rnj58kEZNZ_pAEWLZD4qUYcOsUySccpjk2bCT2Wnhs5HymM0Z4wj4qJGF7MSGaiSJcxCLJTQTK5S0edYu18UcCfcqdsz2Vd5nciuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QIbpzWVwNytp-EBLWhsJjEB873jPvEZdFG2iQhonNVDio7WMzpyYwesGkDl6c_sHAUlfo9mBaCu-gSk0xt6eTMgT5ONqBhFUdqj5T-WYnxt5WFqkxhvkDmCZFPwdUjAsgWGEmTYw5xhzNaFdKNg2RnPtuWrpumSaW6fjuCBMXv0iAiyR25kHAfqdPPTEw4Jyb6Ema95sKrMGULtU7j8RicZOwqKqJiIbKFZfqMTRy6EWKYEIN47Wl8DJcgCvhnFrncwVJcStVW_pl6qtu0jFlRcJrXg2Wy9mJ0TRKB_7YEpXEbMG4Pru5Dt6BYFJN6uaiMq1jVVFrt0TYpkQBD3joA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ahmc1SP6-cQ4tPaRAotgdwmQ4Ch-qLElM26tOsPxIRJgg7rdM6RJMRGLhCRD7_bPOjxx_L75hxP3qPO-plyLM7zBrlGvgzD1DHdaj7XFqB_grQMBB-A5SKIdgFLgiZlK6dJrQK8Il_VZlzpKqajxSqjHy4M4kNdEJT8UKXzvqZV2QUDjJK24lOofJNXkaatqKAW1HXRZAsgyOZQ2lYmTFB034o1chFUTXdUNqIb9rrQ0sMx52BB2i-_rIco8qNtxAT_RU8SeqrFCqjxF0gD5UM-SGEjjsu6XvlRcqWbT6TYjgyzleyUiPf4XBvmfeB6vtDZ43XHfnaf7keKsPfhULg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از حملات تازه‌ی اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147234" target="_blank">📅 18:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147233">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10fc0802be.mp4?token=YZ0DPsxRIStCkAtut9knEr9rX9N3HjPChuMtigDPDVb8lVtUiXHwjfHWTgBd1MSIJ2XCY9ob7cmIHDqOEO91a-V7s-Is11_4wMqNu6iYr0-J32mvpCZympsXfR7GX1boa_Ue-4Xo1XvutvqvADsJo81mQQWt4hwkZWSDxR7FvU7UqH6Ej2m3MwxJNsMO2QsV57SEKaMe4EckmA5Fz5Y2z2txVPym7qzHRBVYw_j5JH488YppOBF_KCxgRFQweFtsKP3Y1uifJuX-opiUPuJKuNJVZLMnNLtDHhY0BYYeGp93pY-YqyaNNuFPw6NEF75tVkyQZkjKGtJs9hjC96J3xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10fc0802be.mp4?token=YZ0DPsxRIStCkAtut9knEr9rX9N3HjPChuMtigDPDVb8lVtUiXHwjfHWTgBd1MSIJ2XCY9ob7cmIHDqOEO91a-V7s-Is11_4wMqNu6iYr0-J32mvpCZympsXfR7GX1boa_Ue-4Xo1XvutvqvADsJo81mQQWt4hwkZWSDxR7FvU7UqH6Ej2m3MwxJNsMO2QsV57SEKaMe4EckmA5Fz5Y2z2txVPym7qzHRBVYw_j5JH488YppOBF_KCxgRFQweFtsKP3Y1uifJuX-opiUPuJKuNJVZLMnNLtDHhY0BYYeGp93pY-YqyaNNuFPw6NEF75tVkyQZkjKGtJs9hjC96J3xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمب‌افکن B-1B از پایگاه فرفورد بلند شد
🔴
یک بمب‌افکن B-1B لنسر از پایگاه هوایی فرفورد به پرواز دراومد. صدای غرش موتورش تو منطقه شنیده شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/147233" target="_blank">📅 17:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147232">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏
👈
تسنیم: جانفداها اماده شن که قراره ببریمشون کنار نیروهای مسلح
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/147232" target="_blank">📅 17:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147231">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⚠️
پارسال میگفتن ماشین‌های نوشماره زیر یه میلیارد سهمیه ۱۵۰۰ و ۳۰۰۰ تومنی دارن  اگه ماشینی هست که زیر یک میلیارده سایپا و ایران خودرو یه افزایش قیمت بدن درست میشه
‼️
🆔
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/147231" target="_blank">📅 17:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147230">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
رسانه‌های غربی:
امروز قطار حامل مقام‌‌های اروپایی از جمله نخست‌وزیر آلمان با یک فروند پهپاد مورد حمله قرار گرفته است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147230" target="_blank">📅 17:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147229">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee9bf5d0bf.mp4?token=XYt8k6ymybQiu5qYhxumsjkO5Nqvq_KMTqZtuScBSDpwnmVx9UMqZ1Bqzngo3i1CPneBrU6wmOPokFH51xeBuvwp0drE24MuEm_Ay8p99L3_PNj6snug6XXvkjFZKdZhGdr6xxYbtPJYa_miPpjdT-SK3nYl-uoQO9VeVapyjRdu16szzr6HWKuDCM_EpwicmpOwS80WrmwlDORZGYEpj2jGngaAXn_2X1LiOfHow9nkG8hmDR3bI3hV-XcuaGfkAOl9wI9D5q_k5fXSOc-2OqlKCHw2HrNz5H3AH0jm63JD8NbwzAdNr0SYN9P-Nx6TVWBtpF9oYQgBesP8xC5beWu6ILhSxrqLx9nG-9preoulzgAH4KdhIGFEIHa-NQ95ej-i18umSqOXNipQk6-mFlfW0mZ05daqxWdr-C1AC6bQH3wki80BbC55PXDYSkD6EEaBWW0K4i8kizzjVnRWJtsHi3sNJlHp0r76y5pyQn_dprrKcWX7S6Te_sZqKikO3a4mBbbW2YNI9xGnmIfngYRZvXquBTBDJyqRnAcOoBx43J19kx_1haREIqLIfWcZ6xxW9Lp_Z1yfI_O0J7HfZ_8ZoygBrtRLJGPC0c5wRtA-xC1DzBrdCOfB2wl8PSfsX_nOnes8iJZDCnjtP1IabzWj_pz5XNDXCDwPqY8qgWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee9bf5d0bf.mp4?token=XYt8k6ymybQiu5qYhxumsjkO5Nqvq_KMTqZtuScBSDpwnmVx9UMqZ1Bqzngo3i1CPneBrU6wmOPokFH51xeBuvwp0drE24MuEm_Ay8p99L3_PNj6snug6XXvkjFZKdZhGdr6xxYbtPJYa_miPpjdT-SK3nYl-uoQO9VeVapyjRdu16szzr6HWKuDCM_EpwicmpOwS80WrmwlDORZGYEpj2jGngaAXn_2X1LiOfHow9nkG8hmDR3bI3hV-XcuaGfkAOl9wI9D5q_k5fXSOc-2OqlKCHw2HrNz5H3AH0jm63JD8NbwzAdNr0SYN9P-Nx6TVWBtpF9oYQgBesP8xC5beWu6ILhSxrqLx9nG-9preoulzgAH4KdhIGFEIHa-NQ95ej-i18umSqOXNipQk6-mFlfW0mZ05daqxWdr-C1AC6bQH3wki80BbC55PXDYSkD6EEaBWW0K4i8kizzjVnRWJtsHi3sNJlHp0r76y5pyQn_dprrKcWX7S6Te_sZqKikO3a4mBbbW2YNI9xGnmIfngYRZvXquBTBDJyqRnAcOoBx43J19kx_1haREIqLIfWcZ6xxW9Lp_Z1yfI_O0J7HfZ_8ZoygBrtRLJGPC0c5wRtA-xC1DzBrdCOfB2wl8PSfsX_nOnes8iJZDCnjtP1IabzWj_pz5XNDXCDwPqY8qgWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
:
به نظرتون چه زمانی انتخابات دموکراتیک در ونزوئلا برگزار می‌شه؟
🔴
ترامپ
:
وقتی که آماده باشن. مردم ونزوئلا الان خیلی خوشحالن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147229" target="_blank">📅 17:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147228">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
واکنش ترامپ به نشست دوشنبه ایران و کشورهای عربی: برایم اهمیتی ندارد
خبرنگار:
🔴
نظر شما درباره دیدار کشورهای حوزه خلیج [فارس] با ایران چیست؟
ترامپ:
🔴
برایم اهمیتی ندارد. این به خودشان مربوط است. ما در نهایت از آنجا خارج خواهیم شد. مگر اینکه تصمیم بگیریم بمانیم و نفت را برداریم! مثل ونزوئلا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147228" target="_blank">📅 17:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147227">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ: رابطه فوق‌العاده‌ای با چین داریم
دونالد ترامپ، رئیس جمهور آمریکا:
🔴
به نظرم در سال‌های اخیر پکن با ما بسیار منصفانه رفتار کرده است.
🔴
ما رابطه فوق‌العاده‌ای داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/147227" target="_blank">📅 17:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147226">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXzU8Ruc8iPjPkMMkBfjuczuSYN30ESVn0aegU33FxBivS9g7aMS0N2UyqQfIiKMb0bBJKDalbdaBbOu28-ob9P7jr9n0KaZ-yl2ln68PQgDlsT5RrNTtLnH3YxwohwirdDfcoJCOMgx0zDi4QFGrXgbNZLYN9Af0M3d2-aADFcRvw2NEBGNx7MQyHwoRT6cWFI8bc1mcNKglMKeFVh3w4LTiPqMhxW1PtFxdSXpPeDEGO24aZwmJ7fY_Sv3HgqpPom7g07E7St5ACwDOY9XGWgHdsxkEmjettZeq52vb9a95QmaOo27TmUkjyqEFctr6RNCC2S40Br--PaTSCwTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجیب اما واقعی
‼️
👈
این پسره ماهان پارسال همین موقع گفته بود که شهریور ۱۴۰۵ دلار به ۲۳۰هزار و طلا به گرمی ۲۴میلیون میرسه و اون زمان همه مسخرش کردن اما دقیق گفت
😐
الانم یه تحلیل خیلی عجیب گفته
😐
👇
https://t.me/mahaneconomy
https://t.me/mahaneconomy</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/147226" target="_blank">📅 17:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147225">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ: به نظر من، شما ایرلند شمالی و ایرلند را دارید.
🔴
به نظر من، یکی از بدیهیات این است: آن‌ها را با هم متحد کنید.
🔴
این فقط نظر من است، و البته، بسیاری از افراد با این نظر موافق هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/147225" target="_blank">📅 17:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147224">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ:زلنسکی باید حمله به تأسیسات تولید و پالایش سوخت دیزل در روسیه را متوقف کند.
🔴
او باعث ایجاد کمبود سوخت دیزل شده است.
🔴
این وضعیت ناشی از خاورمیانه نیست؛ بلکه نتیجه آن چیزی است که میان روسیه و اوکراین در حال رخ دادن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/147224" target="_blank">📅 16:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147223">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ترامپ
:
جنگ با ایران قبل یا بلافاصله پس از انتخابات میان‌دوره‌ای پایان خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147223" target="_blank">📅 16:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147222">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e81d794a7c.mp4?token=KoGaWGzwGhKRwjyttyGOsjHpXa0uKDOf9ek1M7WYtgOUm0xooH-w19WcoVbsShvia7RSV5zZjdw8cWfIJhfF4q9Lnu2ZCwkQFeb9QXBtObFG5IxQLAeQpdOEQf4b8JPspOpSSB9Uk6C_y0zXZJ0ZEQGnXr3OJjfzHxlgqAJx8J4BF5d__qPqvhkfaRT4JlTFVqK70--8rdpTCCR59yMb52ok27T5k8Zc5yAVQM263HPZoSmJ1F2bagJdnZEZJce3ouTqEUX9B-kuDVbuqX4-MVuvtwf_aU34UD-ON2mSSquFxfpGqy9o5F-nn6s9TcfmuZXqTDGC2d5PlpVvepxK7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e81d794a7c.mp4?token=KoGaWGzwGhKRwjyttyGOsjHpXa0uKDOf9ek1M7WYtgOUm0xooH-w19WcoVbsShvia7RSV5zZjdw8cWfIJhfF4q9Lnu2ZCwkQFeb9QXBtObFG5IxQLAeQpdOEQf4b8JPspOpSSB9Uk6C_y0zXZJ0ZEQGnXr3OJjfzHxlgqAJx8J4BF5d__qPqvhkfaRT4JlTFVqK70--8rdpTCCR59yMb52ok27T5k8Zc5yAVQM263HPZoSmJ1F2bagJdnZEZJce3ouTqEUX9B-kuDVbuqX4-MVuvtwf_aU34UD-ON2mSSquFxfpGqy9o5F-nn6s9TcfmuZXqTDGC2d5PlpVvepxK7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جرد کوشنر درباره غزه: اسرائیل این عملیات را در دوحه انجام داد، که یک کار فاجعه‌بار بود. این عملیات از نظر نظامی ناموفق بود و در نتیجه، اسرائیل به صورت جهانی منزوی شد.
🔴
ما از این وضعیت برای تحت فشار قرار دادن آن‌ها به منظور دستیابی به توافقی استفاده کردیم که اکنون، امروز، آن‌ها از آن بسیار راضی هستند.
🔴
در آن زمان، آن‌ها کمی نسبت به آنچه ما آن‌ها را به انجام آن تشویق می‌کردیم، احساس ناراحتی می‌کردند.
🔴
اما در نهایت، این موضوع برای آن‌ها و همچنین برای مردم غزه، بسیار سودمند بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/147222" target="_blank">📅 16:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147220">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ: ایران می‌خواهد به هر قیمتی توافق کند، اما من توافقی را که بی‌نقص نباشد امضا نمی‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/147220" target="_blank">📅 16:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147219">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
فیدان: سوریه می‌تواند جایگزین مسیر هرمز شود
🔴
وزیر خارجه ترکیه گفت سوریه می‌تواند با اتصال به اردن، عربستان، عراق و ترکیه، نقش مهمی در ایجاد مسیرهای جایگزین تنگه هرمز ایفا کند؛ مسیری که قرار است از طریق راه‌آهن، بزرگراه و خطوط لوله عملیاتی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147219" target="_blank">📅 16:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147218">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
واس: ولیعهد عربستان سعودی و نخست‌وزیر پاکستان در تماسی تلفنی درباره آخرین تحولات و تلاش‌ها برای کاهش تنش در منطقه گفت‌وگو کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147218" target="_blank">📅 16:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147217">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
پزشکیان: با ولیعهد امارات گفتگوی خوبی داشتیم و قرار شد گذشته را کنار بگذاریم و آینده خوبی بسازیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/147217" target="_blank">📅 16:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147216">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da2aacdd5d.mp4?token=PjUAHUA5g_6dCjwwebQr97QvwqOjjSLb7_tSyDWjCNCnfwM1psCJAKeq4OSnGhPDmk4JjLhL43I6t0zrDllrGRf15To63AxJ7XzLU4VEr5TPiCO07S0pf0bUx32FMvPGdrns446N7h0VWhLPjP1sM3VWM2gtH8SA-TL4mNKSNn_LoKlGr0Gz-WS0Rhlc4mBDdahYz9Z5tbB4yPXc5_SpBwY9nKjUsVgCTqn3uHx2xcbIgnujW9WIGIBDfxJMZgdsTzPwldt0yX22L5IKxOmfQtwhyXus6uggRsC4A2Tw69Uagi1SxYBDpc7Y4YkHT9r_W12onmhJuYE0qXPVs1RLFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da2aacdd5d.mp4?token=PjUAHUA5g_6dCjwwebQr97QvwqOjjSLb7_tSyDWjCNCnfwM1psCJAKeq4OSnGhPDmk4JjLhL43I6t0zrDllrGRf15To63AxJ7XzLU4VEr5TPiCO07S0pf0bUx32FMvPGdrns446N7h0VWhLPjP1sM3VWM2gtH8SA-TL4mNKSNn_LoKlGr0Gz-WS0Rhlc4mBDdahYz9Z5tbB4yPXc5_SpBwY9nKjUsVgCTqn3uHx2xcbIgnujW9WIGIBDfxJMZgdsTzPwldt0yX22L5IKxOmfQtwhyXus6uggRsC4A2Tw69Uagi1SxYBDpc7Y4YkHT9r_W12onmhJuYE0qXPVs1RLFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: راه جدیدی در ارتباط ایران و هند خواهیم داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147216" target="_blank">📅 16:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147215">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
پزشکیان: وزیر اقتصاد با سران و وزرای اقتصادی اعضای بریکس جلسه داشت
🔴
گفتگوهای سازنده با بانک توسعه بریکس داشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147215" target="_blank">📅 16:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147214">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
رویترز به نقل از منابع: اگر عربستان ظرف چند روز خط لوله اصلی انتقال نفت خود به دریای سرخ را دوباره راه‌اندازی نکند، ذخایر نفتش برای صادرات به پایان خواهد رسید؛ در نتیجه ممکن است تا ۴ درصد از عرضه جهانی از بازار حذف شود
🔴
شاید تعمیر این خط لوله پنج تا شش هفته طول بکشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147214" target="_blank">📅 16:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147211">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تنش‌های اخیر و اهرم باب‌المندب کار خودشونو کردن، تردد تو تنگه‌ی هرمز به شدت پایین اومده  دیروز فقط یه نفتکش از تنگه رد شده!
🆔
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/147211" target="_blank">📅 15:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147210">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
مدیر سامانه هوشمند سوخت: خودروهای بالای یک میلیارد تومان مشمول بنزین ۳ و ۵ هزار تومانی نمی‌شوند و تنها ۱۱۰ لیتر بنزین با نرخ ۱۰ هزارتومان در کارت سوختشان شارژ می‌شود
🔴
پ.ن : مگه خودرو زیر یک میلیارد هم داریم الان ؟!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147210" target="_blank">📅 15:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147209">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLg9Wtef1I0nDlA21oWLydv7eAq6pAskbN6pVJumfZsvxlqxjdob857uTTeC9zGMjUBSV97xH4TBfK_zXqSlDldqiWp404WKxHol-zjWvFqrtkMZsYUX-s0cQ3hYXZlhJnWeStXRAneEdoCY_oTmhWFxivIA6oniKZxtdm8U6iRdupTIxT7rVKsFF-T1rRTTWHfLY8k3XFlOt2GM2SXahhXD5M3hs6NZ2GjsUvyBqUwXtbRCrGKUp06LOUPp_1rwiDMObAqWbKpWWPhy--ZnvuOqPHmbOk61RFoh0AuPYr11X3FLscOCVhZ6U2-wWz-OLyfOefD6smjYOM2V2TflPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چهار سال پیش در چنین روزی، جاویدنام مهسا امینی، دختر پاک ایران زمین توسط مامورین گشت منحوس ارشاد به قتل رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/147209" target="_blank">📅 15:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147208">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
توی مشهد این همه معتاد یهو باهم از کمپ فرار کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/147208" target="_blank">📅 15:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147207">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cfbe5e94.mp4?token=SCrXPNZcit8cD4D8mRrxkT-YuWt14YqDCiY3Pe4WDRuzi_5rvfCuteXUQ4Mb4ifdQo_3GSz7DCSV1JswDS6up826awah0251h2F_FhZ2mbSCy33_wonrkH6GI_J_7nepye1Txf3hwVOTxEWMT0vgmvYk46BnwhSnleZ2uoXVKbfs4QEVMbGcumD8GaKlbGSB28dmUIGVFr1NKBmMJViu1lTKubmSSDlCMECTh9D371ptPK9yCCCIZ41cJx_vHWzGbIZbqEuY7r8SGpeHCBvW0ToPW6bFzcohL4q17yjX1Tr0imYn1vsIASDl51X_IOEl91aDZ_nkzDqMiFNrNqGglJl19S7KR3N50iflz7ehLt58wNqfTc-pPFfRDLlQfVHgH4rUOGNPeCwUe0O5xGotASbG3HhbWGgsfFsof8-l9p2nWiZFspDQqTRa85mnmOYoeISmZXmmG07XDfWegmZzkXWmpfG_DF4DBcwuOQ5UDMeYasMgazF9odsVzpDXbamvttR5SW7LXzu2CaFiPlBMYBdIibj7ppMoh6KaQdqN_CnQ-uVwWx1t-GCjwo55SqwNHIam7Sz-Q_rY3M5AsTeloeK0SjIe2BrAoF6D4x8F2hCmoRuR7z5gynQL1pUt5vhoKZBLCIN-y3NPoTs1YV6MUDfOlyQMgSrPPPxHkntenxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cfbe5e94.mp4?token=SCrXPNZcit8cD4D8mRrxkT-YuWt14YqDCiY3Pe4WDRuzi_5rvfCuteXUQ4Mb4ifdQo_3GSz7DCSV1JswDS6up826awah0251h2F_FhZ2mbSCy33_wonrkH6GI_J_7nepye1Txf3hwVOTxEWMT0vgmvYk46BnwhSnleZ2uoXVKbfs4QEVMbGcumD8GaKlbGSB28dmUIGVFr1NKBmMJViu1lTKubmSSDlCMECTh9D371ptPK9yCCCIZ41cJx_vHWzGbIZbqEuY7r8SGpeHCBvW0ToPW6bFzcohL4q17yjX1Tr0imYn1vsIASDl51X_IOEl91aDZ_nkzDqMiFNrNqGglJl19S7KR3N50iflz7ehLt58wNqfTc-pPFfRDLlQfVHgH4rUOGNPeCwUe0O5xGotASbG3HhbWGgsfFsof8-l9p2nWiZFspDQqTRa85mnmOYoeISmZXmmG07XDfWegmZzkXWmpfG_DF4DBcwuOQ5UDMeYasMgazF9odsVzpDXbamvttR5SW7LXzu2CaFiPlBMYBdIibj7ppMoh6KaQdqN_CnQ-uVwWx1t-GCjwo55SqwNHIam7Sz-Q_rY3M5AsTeloeK0SjIe2BrAoF6D4x8F2hCmoRuR7z5gynQL1pUt5vhoKZBLCIN-y3NPoTs1YV6MUDfOlyQMgSrPPPxHkntenxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از کشتی ایرانی که امروز در نزدیکی جزیرۀ هنگام مورد حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147207" target="_blank">📅 15:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147206">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501e83f6c2.mp4?token=O6MaIvjQeogTz8UVDHWRel5vf5I4UIVcUIxv4wSQUpWLBVSOzN8thxtdo_NPTNCOWzFDZe0LczEjZNRP7yuytwwIYnoRsN1C4IeSAI5WglhqFNdoJuMzg5QOvGVDZ6RfTJnDjtPs_7k99O9qTmH2zs_V_g3MMEKz1r9aenzryzWkuH8yrQx2mgcxVctkqVIJuLFBrJ4U_2qfCjRVhDukg-aCWhGJtF0868zn2SB6Zu-3qqBcIsFN6gxZAGQ4t7tyrxO8eDa3PbEJLxIqVHiYDCbB9joSgRxbVlQoEb_QoAeP2czDr9lnj_nOmhYhwMBUeSuHCUmoki3tVo0NYIa3ICM0ZD3Ri8IlhMlV-fny155vrCntijTYtUc0AthT6VWTzqp4Q0oBmbdmcNmxw4Sq2MlkrmkrdbpxmPcEwlOyp6vFmPfW6pLpdsH43gcpLu15m-ESHhbdOCadaaFZvXXd3pjFNryh-NCgOwAR165RHKQvknX4U3dVKJ4cOrxO12I-92TuqkSov8qEAxmttmVorIgCgk9-EXkRG9TthR5aus2DR8kqDYcASO25wuAzAlF_h5PrUsxfkfsSOXPa1s-VKQbOw-3FPSCCYXGvvgrbdEA9ixBHEOvTkQNpSDWgFTOdlFabTRrSAMzCPDeGxlCHIVAkWPtGFPfGbXuKpa5ifZo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501e83f6c2.mp4?token=O6MaIvjQeogTz8UVDHWRel5vf5I4UIVcUIxv4wSQUpWLBVSOzN8thxtdo_NPTNCOWzFDZe0LczEjZNRP7yuytwwIYnoRsN1C4IeSAI5WglhqFNdoJuMzg5QOvGVDZ6RfTJnDjtPs_7k99O9qTmH2zs_V_g3MMEKz1r9aenzryzWkuH8yrQx2mgcxVctkqVIJuLFBrJ4U_2qfCjRVhDukg-aCWhGJtF0868zn2SB6Zu-3qqBcIsFN6gxZAGQ4t7tyrxO8eDa3PbEJLxIqVHiYDCbB9joSgRxbVlQoEb_QoAeP2czDr9lnj_nOmhYhwMBUeSuHCUmoki3tVo0NYIa3ICM0ZD3Ri8IlhMlV-fny155vrCntijTYtUc0AthT6VWTzqp4Q0oBmbdmcNmxw4Sq2MlkrmkrdbpxmPcEwlOyp6vFmPfW6pLpdsH43gcpLu15m-ESHhbdOCadaaFZvXXd3pjFNryh-NCgOwAR165RHKQvknX4U3dVKJ4cOrxO12I-92TuqkSov8qEAxmttmVorIgCgk9-EXkRG9TthR5aus2DR8kqDYcASO25wuAzAlF_h5PrUsxfkfsSOXPa1s-VKQbOw-3FPSCCYXGvvgrbdEA9ixBHEOvTkQNpSDWgFTOdlFabTRrSAMzCPDeGxlCHIVAkWPtGFPfGbXuKpa5ifZo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان : «آنها به مردمی حمله می‌کنند که هیچ ارتباطی با جنگ ندارند و حالا همان مردم را نیز تحریم می‌کنند.
🔴
اصلاً اینها انسان هستند؟ چرا با ما می‌جنگند؟
ما
چه کرده‌ایم
؟
🔴
این یک فاجعه است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147206" target="_blank">📅 15:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147205">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gctFMmuPOnHqcYQZ_eBJe-pFoxlQNmJt4A9A5NgAn4cQ1zH2LXtT__3ufE6rlPhZ83TEHeJEQmz1DyrBC1fwe6MWqwnT9ce60FON40S3IC9fxjih2YtucZE2n5APMP0uL8mURMLTNTVtJvxZPPOYqKOhGlXzXK0kyGRNXOkhtH4R6aO_Z1N3oJedh6KibsY5hu_j0rD76SrGXJbjyM29UJ6-BOFu3FAlnm04G98woV-_kn_wGZKDX99470OjQ-viIK09_KceiitCnfL4rLZbaExbddD9Y3J4UiyUnyahFzXtrqYW21SZ3rkpibhCxXyucNvv6L4f5LIG_GPIaWU6Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش ۹۷ درصدی تردد نفتکش‌ها در تنگه هرمز؛ تنها یک نفتکش روز جمعه از این آبراه عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147205" target="_blank">📅 15:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147204">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره:
تهران نشست مسقط را اقدامی مثبت برای بازسازی اعتماد با کشورهای همسایه می‌داند.
🔴
حضور عراق نیز مهم است، هرچند یکی از کشورها دیدگاهی مبنی بر عدم مشارکت عراق در این نشست داشته است.
🔴
این نشست می‌تواند زمینه‌ای برای بازسازی ترتیبات امنیتی در منطقه باشد؛ اما اکنون نگاه‌ها به واشنگتن، واکنش آن و مسائل دیگر دوخته شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/147204" target="_blank">📅 15:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147203">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دلار (تتر) از دیروز ۸ هزار تومن ریزش داشته
‼️
امیدوارم همینجوری که هر روز بالا میره، هر روز بیاد پایین
🔴
با این حال الان روی ۲۳۰ معامله میشه
🆔
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/147203" target="_blank">📅 15:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147202">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCaOKDjh0--k8kRYWbpzKPSOVuEqECHak_YIEc3nbgB6cnbM4N4g9407rN3ShBWD0VjQJzEEBEuPpDJMT9rnXb4SG7n5UxQaIhZzW-4w_Eg6RXl-KRuEOtl8lj8QZrbbPW-Y4eOHa--ulwn3i3KS2PXDkbu_-5uZfRKeX0DTuQapc3tuDAjMGV0qP8_pZimD6Yjh7UZetRz1pMjdCQLemMcGLhMYlxBs5d4kQaAVBXnM28klzsIqkJcGfD0upX4Sk0KaflMSCzbHWuqZD12Un8k8Fr62nZ5gJEHs5M1gcaVy8qb1I0WDzDMi-M45WhBNo8BC6ZFCHr5zvv16E1AtDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / به گزارش روزنامه تلگراف، نخست‌وزیران ایرلند شمالی، اسکاتلند و ولز قصد دارند در نشست مشترک خود در کاردیف، یک یادداشت تفاهم امضا کنند تا بتوانند درخواست برگزاری همه‌پرسی برای استقلال را مطرح کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/147202" target="_blank">📅 14:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147201">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
تلویزیون سوریه: نیروهای اسرائیلی در حال پیشروی به سمت منطقه جورا اللوز در نزدیکی تل بت‌الورده در محدوده بیت جِن هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147201" target="_blank">📅 14:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147200">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90b0f7822b.mov?token=IuRlAnp8a3DQM8CgcdAiG4vSyL2dbFhN-ovlmXXO5eR5Ur40OLfPw8GEEPF1czNP42NjE0Hs6dWKN5rkCzfjYxRXpPQsBd5vKxeV1xxHh7_q2fmxVKYGSY2e3LzRwWol34A47UCSOq1-qaul1aslKSS0jsdpwNjWzEQCQb-ysiMj9gxHDs76BRKYi9cTdi4MCGbJFGx8WgKWgAVZm0YHfnOn5cgqv3LQ6MhwNhUMNvnoOmD6gbzixrc1BvLJL1vtjoq6xST8FnkzTwngBTndggx1cGWfs1FP0DSr2d-eyhjPWplrfIyy7maT7wYrPAgpkG0B6XJzGa5E04q7tZhWHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90b0f7822b.mov?token=IuRlAnp8a3DQM8CgcdAiG4vSyL2dbFhN-ovlmXXO5eR5Ur40OLfPw8GEEPF1czNP42NjE0Hs6dWKN5rkCzfjYxRXpPQsBd5vKxeV1xxHh7_q2fmxVKYGSY2e3LzRwWol34A47UCSOq1-qaul1aslKSS0jsdpwNjWzEQCQb-ysiMj9gxHDs76BRKYi9cTdi4MCGbJFGx8WgKWgAVZm0YHfnOn5cgqv3LQ6MhwNhUMNvnoOmD6gbzixrc1BvLJL1vtjoq6xST8FnkzTwngBTndggx1cGWfs1FP0DSr2d-eyhjPWplrfIyy7maT7wYrPAgpkG0B6XJzGa5E04q7tZhWHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه: در حال کار کردن برای رفع موانع موجود برای پیوستن به بانک توسعه نوین هستیم
🔴
برخی کشورها مانع هستند که در حال رایزنی‌های لازم  هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147200" target="_blank">📅 14:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147199">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8JssdK22djzT396PwywjTDPVoYIRIfVFPu6PHqRfTMAyN46w_tZe8-3Bz0_ojeiOcKl3Te_7IZBeN7qsWrsPtOxo_Yo4SUma-qJI2pvjpfYiMjHwzxsIiJQ5fme9knAB2DQoSzFDeUvm1aaWZhfI7S_LtWZT7M-TMSnwhN7XvbIM9eGG1IfFv9fd7kRTtjvysMuXTnfFSRSWMiIUfvl8U_oFUVoGF51VZRGPYW3kzlavGSVuLPJZBsefhVWZWZB5m8Gx0hFhwdhOfxsppVmYO1H_OcbDa2lVwsOIXKTcjb8pSnOCIW0nHko6FxFMQ-ulEJbjyYthorD7RCMUNW1Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر جدید دیگری از
گلوله‌باران اسرائیل علیه بیت جِن
در حومه غربی دمشق منتشر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147199" target="_blank">📅 14:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147198">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
به گزارش فایننشال تایمز، ایران امسال از روسیه خواسته پهپادهای پیشرفته «گران» را برای استفاده در درگیری با اسرائیل و آمریکا در اختیارش قرار دهد.
🔴
این ادعا به نقل از مقام‌های امنیتی غربی و یک فرد نزدیک به کرملین مطرح شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147198" target="_blank">📅 14:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147196">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDHepJdkX8nl9AAUSKdPMN53DQaI-cZdTtgioMk46um2MousioKWXzMm-AieI2yL24KfwoEXdDk5PcIAFsknusXNkMple2wfx6ZHycYTNE0IokWDaXmPnd8hVfarWdXQZx7i6ivZkIj4uHY22O7mMwQirOd7hskscgAi2Jiu0_v2AvzLxgFXUO-m_UImesnaaVL5uBXFMAV3ZfB8RUrR1RNA_rOt9gYmNyJZKR4WEdWdFDxwnEDma-hXNtHgkDKohgAWPksTfdw-CVCZJWlPIVqqMIwn9vqxbebTWNMg5_Ep58Ns4-eI4dtPs7PReue2T_MH52OCVXhUOug7EblAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_X6PA3jl_evkT1ElZjQ7eNpfPx9xhMP8YCW72JT16gtDOCLIinpIHdlG3mj-xCT4B1ugRYqz75zg2-kXs9cqRMsI4XwkHK9lwQ4DlHzVlvD8MnlNLriJw5llDFB1cBIEsIC-yPMi7yuypI8cMt5gkoaUbN8xu8_DKJ4uAtEoDJHDJ1AmuHppIW9Uk9r22dZjnEFC76x5I7Q6k6xWVPAnGmzbkWiXmnDjO5i0n_B_ofxMR54kMySUurm9fdzEC1mhoThZRdnMusWedbe3_4CXRqIl2R9ogUvLK9rO76W3gkw454TJcJhHQ8XCShM0zGj1_RTi5SuA9Aig8p8Mp6O8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دود غلیظی از پالایشگاه یِنبوی عربستان سعودی به هوا برخاسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/147196" target="_blank">📅 14:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147195">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
نیروهای وفادار به عربستان سعودی اعلام کردند که در درگیری‌های اخیر در سواحل غربی با ارتش یمن، بیش از 500 نفر از نیروهایشان کشته و حدود 1500 نفر دیگر مجروح شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147195" target="_blank">📅 14:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147194">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
دیمیتری پسکوف، سخنگوی کرملین:
روسیه احتمال برگزاری مذاکرات سه جانبه درباره اوکراین را در ماه اکتبر منتفی نمی‌داند.
🔴
روسیه خواسته‌های خود را برای حل منازعه در اوکراین تشدید نکرده است؛ این خواسته‌ها بدون تغییر باقی مانده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147194" target="_blank">📅 13:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147193">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14334fab5e.mp4?token=YMFTEK7Jo79v5LLVdrQovCsKMITFyEHIBRqzMxRHmNZEkNBJcaXY9zdseL3ddAAL7iOAaXj6ou_yEN9hK9ADdSNJwcUYdOAQbHxoru6DIpdWZgMp9cY7qnw4RpiJvTWy9CDY9dN7rqfQXFazxZPgbP5v-OOr0cej2MOLcQInlsTWEF0Gzs2FMuIU5MMIJHjwIKPOdFuuwQAIH7IEASrUcKV24iSMzaLdAAzP8S-P_EhKmKziu88JHmxEBwMTINtrLc6hMW_lmnnD648nRJCvgcVghjJkonWK7zwrvE63DVvHI71ciM5Ijh-2OhbATZ9B9T98btDAkNJKbFHCJMWnww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14334fab5e.mp4?token=YMFTEK7Jo79v5LLVdrQovCsKMITFyEHIBRqzMxRHmNZEkNBJcaXY9zdseL3ddAAL7iOAaXj6ou_yEN9hK9ADdSNJwcUYdOAQbHxoru6DIpdWZgMp9cY7qnw4RpiJvTWy9CDY9dN7rqfQXFazxZPgbP5v-OOr0cej2MOLcQInlsTWEF0Gzs2FMuIU5MMIJHjwIKPOdFuuwQAIH7IEASrUcKV24iSMzaLdAAzP8S-P_EhKmKziu88JHmxEBwMTINtrLc6hMW_lmnnD648nRJCvgcVghjJkonWK7zwrvE63DVvHI71ciM5Ijh-2OhbATZ9B9T98btDAkNJKbFHCJMWnww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک نقطه مرزی بین لهستان و اوکراین مورد حمله روسیه قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/147193" target="_blank">📅 13:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147192">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
عباس عراقچی: توافق با سلطنت عمان به هیچ وجه به معنای بازگشایی تنگه هرمز نیست.
🔴
شرط ایران برای بازگشایی تنگه هرمز، بازگشت آمریکا به تعهدات خود در تفاهم‌نامه اسلام‌آباد است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147192" target="_blank">📅 13:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147191">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJXf56MvHUSu8kT60JqgCjNDSBi0hUFTEgDzpHhn81_NEymewoJkh150s0LVVlH4kk4cTn8EAHGb2ysGBgiAOSzuCELz9GBtCpbMabbh4OBTLRD6ybvlqAg0-ayUpOkbUZ4-jwmrrrDdwVSRDmptwIEY17459eCdzNXFx8LGAxlHSKUuyoXrxQ8izGWFZKY3RqxSgZDEDgH6jcx_ttuIW4jf-kIVWOqQfmj4-Se0O_5qPGh_EZ9NAoypUHRYkkjYNP_FoCwLBIgY1eL0DNNoRhqHmn-QD0-Umfx9jmTt1IgNtmrrjxm-dBXsKBAg4h3kFQ08OB59sDEuGIMw5QrNEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیده شده در تجمعات امت معکوس
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/147191" target="_blank">📅 13:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147190">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
مترو تا دو ماه دیگر در تهران رایگان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147190" target="_blank">📅 13:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147189">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f86d227afe.mp4?token=O_uxXNiIsRITsFfv69Qvn3WDP97x5BQ5G8kcQ5T1D2BBcJBQKByfIAh8e7xdvMPWTN8nqVirFk5qL4lJ2tGD8bHjMm4ssVj1zLiM_QFE7JYF4oEkAGoJXBxfCI8Ro2q3dcROzi0PbFgJpVRa77TFrseJgVMOGYhMfJJPsg_ML2wIeVXWGT47-Vei8S3jR1xFOPN9Dz9fCvzHzeKKVPIXmr5g3UdscmpYoER1F7BfKT7XqxZ0ETzvWKX-Zqp8-OffVWb0EujNildoCVXmKZFeQ9GglqeBbGe8F8osONo66o_nw3A2r220EiTNOfvFn-0jMKZZCmGdqVvbvu9AJ-OY0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f86d227afe.mp4?token=O_uxXNiIsRITsFfv69Qvn3WDP97x5BQ5G8kcQ5T1D2BBcJBQKByfIAh8e7xdvMPWTN8nqVirFk5qL4lJ2tGD8bHjMm4ssVj1zLiM_QFE7JYF4oEkAGoJXBxfCI8Ro2q3dcROzi0PbFgJpVRa77TFrseJgVMOGYhMfJJPsg_ML2wIeVXWGT47-Vei8S3jR1xFOPN9Dz9fCvzHzeKKVPIXmr5g3UdscmpYoER1F7BfKT7XqxZ0ETzvWKX-Zqp8-OffVWb0EujNildoCVXmKZFeQ9GglqeBbGe8F8osONo66o_nw3A2r220EiTNOfvFn-0jMKZZCmGdqVvbvu9AJ-OY0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیمان دفاعی مکه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147189" target="_blank">📅 13:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147188">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">با اینکه دلار اومده پایین، طلای ۱۸ عیار هنوز حدود ۲.۵٪ حباب منفی داره؛ الان طلا روی 23/500 معامله میشه و ارزش ذاتیش روی 24/100
🆔
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147188" target="_blank">📅 13:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147187">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
کوشنر: اگر اوکراین تا خط موردنظر پوتین عقب‌نشینی کند، توافق ممکن است
🔴
جرد کوشنر گفته اگر اوکراین تا خطی که ولادیمیر پوتین تعیین کرده عقب‌نشینی کند، امکان نهایی شدن توافق وجود دارد؛ اما کی‌یف حاضر به پذیرش این شرط نیست.
🔴
او همچنین جنگ را «بازی با حاصل جمع منفی» توصیف کرده و گفته در چنین وضعیتی همه طرف‌ها متضرر می‌شوند.
🔴
اظهارات کوشنر نشان می‌دهد اختلاف اصلی در مذاکرات صلح همچنان بر سر خطوط ارضی و میزان عقب‌نشینی اوکراین متمرکز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/147187" target="_blank">📅 13:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147186">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d522fc2430.mp4?token=cAAEdZTFPJ4vICtfg278BLKLUEiA2UKp8i6XH491KBwFqdz4ZYiTge7qcqHxqFKDMnDi3w96Mw_w1GN7n-I2FjDvzaQpZsz3Ur9gpM336yd-cNU8uwl1gLBWjqZBeBkaYCLtDZ7v7kv7Hj98bmMHznvyt4G6w20WjhDRmFzuSJe6dpjXicMq_0OA56-EgpSuEjAXvx0D2pHvHLn9hWoWnKeyFVFRs-DG7Slv0lsA08LnrrxiDAKgdhrj0qGXPVgHkAJQG-t2VLccUuD6HnNfQDMLnb33yYCXoszAnjeO0bZT8lrSS0fg4oX0vYLcDaXBscDls0oQeRHtK0Bmm0D4R2WbXxZ3vRk5FISr2Rs_XOvGc7kFF67FCwxXwUR5MuOTmr64shxqEGNN8uYLIZ7EZN5uTyubUZRMAdWdrVtCi8fl6quIwiX-isggCYYRr9cCo_EpO80cghmL77OTUDIkJ2fyqQkAzwwT2PvZ6HNj9oaEVWinBHXrVP0Edj0HjNmIXxlKhil0MJeBt2VBlXtXuNSLjUSA0Yt9YLmIysuB8nt7SwnBGcuFoOFH75AYta1laEoPUfdl3653FmK7bFkso5ORz1bZNesotqJYJxPzo3kx56BPbxbsrWRmpGE5CjuBVDHl2au_6CqbB84dXnC9-l5p6B0Td80M13PKmdinnEU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d522fc2430.mp4?token=cAAEdZTFPJ4vICtfg278BLKLUEiA2UKp8i6XH491KBwFqdz4ZYiTge7qcqHxqFKDMnDi3w96Mw_w1GN7n-I2FjDvzaQpZsz3Ur9gpM336yd-cNU8uwl1gLBWjqZBeBkaYCLtDZ7v7kv7Hj98bmMHznvyt4G6w20WjhDRmFzuSJe6dpjXicMq_0OA56-EgpSuEjAXvx0D2pHvHLn9hWoWnKeyFVFRs-DG7Slv0lsA08LnrrxiDAKgdhrj0qGXPVgHkAJQG-t2VLccUuD6HnNfQDMLnb33yYCXoszAnjeO0bZT8lrSS0fg4oX0vYLcDaXBscDls0oQeRHtK0Bmm0D4R2WbXxZ3vRk5FISr2Rs_XOvGc7kFF67FCwxXwUR5MuOTmr64shxqEGNN8uYLIZ7EZN5uTyubUZRMAdWdrVtCi8fl6quIwiX-isggCYYRr9cCo_EpO80cghmL77OTUDIkJ2fyqQkAzwwT2PvZ6HNj9oaEVWinBHXrVP0Edj0HjNmIXxlKhil0MJeBt2VBlXtXuNSLjUSA0Yt9YLmIysuB8nt7SwnBGcuFoOFH75AYta1laEoPUfdl3653FmK7bFkso5ORz1bZNesotqJYJxPzo3kx56BPbxbsrWRmpGE5CjuBVDHl2au_6CqbB84dXnC9-l5p6B0Td80M13PKmdinnEU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسیج قبایل حوثی: صفوف طولانی خودروهای مسلح تویوتا در مناطق بیابانی دیده می‌شود؛ تصویری کلاسیک از جنگ یمن.
🔴
قبایل بنی حَشیش آمادگی خود را برای حرکت به سمت مأرب، آخرین پایگاه مهم دولت یمن در شمال، اعلام کرده‌اند.
🔴
خودروهای وانت تویوتا مجهز به سلاح‌های نصب‌شده همچنان ستون فقرات توان زمینی حوثی‌ها را تشکیل می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/147186" target="_blank">📅 13:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147185">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ced64a46.mp4?token=C9Hzu-S2Ijdyx85k9cwrONsdTjI3-Nk6hbVxQI-8lQRGyB-znIAuwgHpqwk8WGoBI_XeYOr8cvaHL_e3T1mr3CsF9IRB8paKbCbqGarL4R8WYCKfs4lmuPXOd2GaaGx0Rv6GLbtP2V8i7r4VDIwF2KkRPOwOx6YkzFKpkM9cL35eiKZOSb2QkrLzVP7IxMkMZg7y38Q8c9IS8LNAW01pnrqTOkBrkmp_r9BJGyucQ96kqluTEQXnzT8FU_17vXZ1pkRqBI9xb5V1DUubDzosfLxgEZCxrRWhW2ZGirLZQLl9kP3tn4yQ4-QnRedcisvQKmNVvV81nKhF1u788E4gYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ced64a46.mp4?token=C9Hzu-S2Ijdyx85k9cwrONsdTjI3-Nk6hbVxQI-8lQRGyB-znIAuwgHpqwk8WGoBI_XeYOr8cvaHL_e3T1mr3CsF9IRB8paKbCbqGarL4R8WYCKfs4lmuPXOd2GaaGx0Rv6GLbtP2V8i7r4VDIwF2KkRPOwOx6YkzFKpkM9cL35eiKZOSb2QkrLzVP7IxMkMZg7y38Q8c9IS8LNAW01pnrqTOkBrkmp_r9BJGyucQ96kqluTEQXnzT8FU_17vXZ1pkRqBI9xb5V1DUubDzosfLxgEZCxrRWhW2ZGirLZQLl9kP3tn4yQ4-QnRedcisvQKmNVvV81nKhF1u788E4gYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
احمد اروزان کارشناس ترک: خلبانان اسرائیلی برای حمله به ایران در قونیه ترکیه تمرین میکردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147185" target="_blank">📅 12:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147184">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c6b4134ab.mp4?token=JuA8UmzrYMenRIX-dh_2Ju3u0BPkLWyZQp_LT09JD8CgQCbwtyh-ipGGuNX8Xa_S60qxQxBqRLCkyW3pKXz01iKJWzymIYKBE-CmtrQu0tPpMjaHkjpDBHiIe4aT7lwqMXDXvtpvNbtsbB-Wqx3NY-oSfy3UvZcEHCdGy5IQVu6iq5Bp33ByCqsC1bLhgw6Ngq8xth9jCQfHVbfGgDxXMUljMuJSRPAG7s0ZSPY-npI37Zwwn58XnZ28aj7Ydk03bBobkdpaAzRiKUxL89hbL2swKvDHH0n43G86wuqrsRM8mke_4U0k_tM_VrB9C0PFRKYyfVfPczbAFucd9C9ICQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c6b4134ab.mp4?token=JuA8UmzrYMenRIX-dh_2Ju3u0BPkLWyZQp_LT09JD8CgQCbwtyh-ipGGuNX8Xa_S60qxQxBqRLCkyW3pKXz01iKJWzymIYKBE-CmtrQu0tPpMjaHkjpDBHiIe4aT7lwqMXDXvtpvNbtsbB-Wqx3NY-oSfy3UvZcEHCdGy5IQVu6iq5Bp33ByCqsC1bLhgw6Ngq8xth9jCQfHVbfGgDxXMUljMuJSRPAG7s0ZSPY-npI37Zwwn58XnZ28aj7Ydk03bBobkdpaAzRiKUxL89hbL2swKvDHH0n43G86wuqrsRM8mke_4U0k_tM_VrB9C0PFRKYyfVfPczbAFucd9C9ICQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ربات‌های نمازخون در عربستان
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/147184" target="_blank">📅 12:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147183">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی به حسن روحانی: تقاضای برخورد با ایشان را به دستگاه قضایی ارسال کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147183" target="_blank">📅 12:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147181">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFb2RKS2nWwIQrG4Lbxt8K0uUcattZ-pUZhlBkqd5F4c6xSJNmKppdkZgHPlYr9vWkePr4i9uiZAyIP2HgP7ZyA-DubID0-MXQ9lYFk7Vsv6UkWinYqbPef4OVo15ew53JDoWmlincD1a1wM56DmlLyixT_HSdxOFoQd6X2lNsev-LE8KwSkGCZlIIFC3HKoJnm1av_ALFa8NzEtA2VZDz0TDadY2f5o2SXL2zKcm1wPSJsHg-EK_fBRUvtgbfgzZfSHQw-q-Y_9ZzVP-GJMfLLWLw19-DvTz2UfOwyv0eeA96kO3qETrPOBRFehBECtInNKU-BP6GpZl2ZNJEuo1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f9f639cc.mp4?token=W31wa56_gfckOG9Pbn2HGdJ9pkiMFSXFSw5BDxjnwvmRShg9DZvmoQGOtjQapI8KAm0JpUEer9UAaPHmmnMfm3lwVL-_1dnFTbmV5SoB9wGW_RgYWMq9N8WZqZIvD-q45nCEEjuwisVcA_0A8lmvo4MAUEodUWqTXOmfXcT-O6wMUM7BewWbCj1-JFOLBtEgEr5tQgJuJLAkjq5lmtcFu_PcHNzrKRdlzadAyyqKE-Rd9qTT1siP8nmd4muPixyCVE5_u9plYdeGdiGuU_i_iOTq2nNiuGju7pCkZXQayCoftjr7V2hWYHHQ8jg-29rTxECDeech1ZmP7pwKM10kYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f9f639cc.mp4?token=W31wa56_gfckOG9Pbn2HGdJ9pkiMFSXFSw5BDxjnwvmRShg9DZvmoQGOtjQapI8KAm0JpUEer9UAaPHmmnMfm3lwVL-_1dnFTbmV5SoB9wGW_RgYWMq9N8WZqZIvD-q45nCEEjuwisVcA_0A8lmvo4MAUEodUWqTXOmfXcT-O6wMUM7BewWbCj1-JFOLBtEgEr5tQgJuJLAkjq5lmtcFu_PcHNzrKRdlzadAyyqKE-Rd9qTT1siP8nmd4muPixyCVE5_u9plYdeGdiGuU_i_iOTq2nNiuGju7pCkZXQayCoftjr7V2hWYHHQ8jg-29rTxECDeech1ZmP7pwKM10kYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات هوایی اسرائیل ارتفاعات
علی‌الطاهر
در جنوب لبنان را هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/147181" target="_blank">📅 12:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147180">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1da3b0c051.mp4?token=p45jDevsOmtT38hOlMaqvq8nqC8hOCWa-S4fQgJfHHLrU6jdNhzjKzd-DOSJ7SvbbSZcGFacFVqRztWksnuNm5sJubZuf2T2VHDM2k5cfXUTfpa7lEnV_TFbZMantkKpa4BuhNag4kQ9v7fphJ4xUE7ZslQf4UPHVPIjHXu-RZzoYMxwitz4idA7e_RczFTz1n6LG6cl38xDd5qWvFLZ8HhvymQPeSrVB4cX1CMl1rrTjJH4ff_wBpidx-ILS3XLEjCvQfFNzLhVlJeh2gp5bkpC_pKXj9RMUo68wOAoYpNdfy6AnfLllCvoUtZ0U7oKVu5v4zdytS6VxLR2cfMzsTsHHJMxs2epC_wM6gFUH6SKkHTMCS2CGDeYKR_YpCGDhgm39Mg19lhhS93UHRrA2WXITvelUGc5DVkCwa9JUCoXgc1InWgkspnZ4HARIvCpb6U0Gqo1UlNlrYHEJ0LGA5TtuKPddWpfOir5Mg142BvNoZlm5BWTNpkvB10LZ6ZNNhKhxWXkV2wEm_kk7cIeo1IKczn3rEDG9k3NZD6c_flhKRtQ7xs783JODAwolaD3poaFeeQDnLBIF_4vB-SVUXvyOQzRaLpL9PWLyqBAUB-yZXVsAYd1en_pceNcyFAWO9w11m7Kw0ieXb_2T9Vzu6UsX9BB97XS_H1EOcC7Bp4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1da3b0c051.mp4?token=p45jDevsOmtT38hOlMaqvq8nqC8hOCWa-S4fQgJfHHLrU6jdNhzjKzd-DOSJ7SvbbSZcGFacFVqRztWksnuNm5sJubZuf2T2VHDM2k5cfXUTfpa7lEnV_TFbZMantkKpa4BuhNag4kQ9v7fphJ4xUE7ZslQf4UPHVPIjHXu-RZzoYMxwitz4idA7e_RczFTz1n6LG6cl38xDd5qWvFLZ8HhvymQPeSrVB4cX1CMl1rrTjJH4ff_wBpidx-ILS3XLEjCvQfFNzLhVlJeh2gp5bkpC_pKXj9RMUo68wOAoYpNdfy6AnfLllCvoUtZ0U7oKVu5v4zdytS6VxLR2cfMzsTsHHJMxs2epC_wM6gFUH6SKkHTMCS2CGDeYKR_YpCGDhgm39Mg19lhhS93UHRrA2WXITvelUGc5DVkCwa9JUCoXgc1InWgkspnZ4HARIvCpb6U0Gqo1UlNlrYHEJ0LGA5TtuKPddWpfOir5Mg142BvNoZlm5BWTNpkvB10LZ6ZNNhKhxWXkV2wEm_kk7cIeo1IKczn3rEDG9k3NZD6c_flhKRtQ7xs783JODAwolaD3poaFeeQDnLBIF_4vB-SVUXvyOQzRaLpL9PWLyqBAUB-yZXVsAYd1en_pceNcyFAWO9w11m7Kw0ieXb_2T9Vzu6UsX9BB97XS_H1EOcC7Bp4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تنبیه عجیب دو راننده جوان که با صدای موسوم به کاتاف در نیمه شب برای مردم شهر تبریز مزاحمت ایجاد می‌کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/147180" target="_blank">📅 12:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147179">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
بلومبرگ: بسیاری از ذخایر نفتی که در روز‌های نخست جنگ به کاهش شدت کمبود عرضه انرژی در جهان کمک کرده بودند، اکنون رو به اتمام هستند
🔴
ذخایر نفت آمریکا به شدت کاهش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147179" target="_blank">📅 12:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147178">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7e-tfiWw2AJ_hdEUtH60AX_e4JsptX-MU1eN4pMQU82yxwOOGPMktB7FokVnu31aMYY2eXhROazTw4KBv400AUif17SsHVAyay9E2Rx3zoHqhALFrOfoDMm1r35zOHoeEy_EtM4ULulb8pPDA63IgY-pOuT-iuhiCD5fOBLOh4kUzf4uVbc0qcX6sjVLBn0XFOcdwVW1S6dqfXP8TwEXT-Nx5FGbNpt8uAA7rxfvP8hLOW2jY9J1O7pnZ-bMJeVr8cpHdCsC137_PZyWgljutS3TdS1TCmy0K741X7UulJm7caaAL392SOymd45nXi1nK20bIikvhUF-G9kXEqB8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار المیادین گزارش داد که حملات هوایی عربستان منطقه الربیعی در شمال غرب استان تعز و شهرستان مرزی باقم در استان صعده را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147178" target="_blank">📅 12:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147177">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
اگه میخوای بدونی طلا رو کی بخری و بفروشی تحلیلای این پسره رو ببین
👇
@AlirezaMehrabi_ir
@AlirezaMehrabi_ir</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147177" target="_blank">📅 12:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147176">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
تحلیل الجزیره: هم‌زمانی بحران‌های تنگه هرمز و باب‌المندب، خلیج فارس را در وضعیت «بین دو فک گازانبر» قرار داده
🔴
واشنگتن درگیری با تهران را بدون در نظر گرفتن منافع کشورهای خلیج فارس مدیریت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147176" target="_blank">📅 12:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147175">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKKMD2mggetTeeGBAM16z7Y91ReJbj3gLdV3X4Tj1g_QXkD5gTrEiL3Xo1phqKUfpDxlg65wLqOUmaD7kdVotWa3JK8fasQwbklEmg4fCQOMvTCmKGE98PYYVWCDXIsSq0bwKi6FT6CeE3jb30kD-tn_8nwVR08KTlMKvSWBra6uGtjhXdXrg3j0zuDNg0q6NdxUKmEk1_b_riYnZMJ5NC3CerrvLew2hmRzTuAyDrbUnGLRRyMT3yFpIBzjiOKiUuxWuLxFJMd6hudsFwQfhgPRL7O860DOsgIWG5-k644RAd0qJ7h8upx0zCt2RqCpj4Zc240FKcy6GnjVycciBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش محمدجواد ظریف به پیشنهاد رئیس‌جمهور چین برای ایفای نقش در مذاکرات صلح بین ایران و آمریکا: ابتکارات سازنده رئیس‌جمهور شی جین‌پینگ، فرصتی به‌موقع برای کاهش تنش‌ها فراهم می‌کند. امنیت پایدار منطقه‌ای نیازمند احترام به حاکمیت، توقف اجبار و پایبندی به حقوق بین‌الملل است.
🔴
دیپلماسی چندجانبه تنها مسیر عملی به سوی صلح است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147175" target="_blank">📅 11:50 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
