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
<img src="https://cdn1.telesco.pe/file/nH-tqYKKMcRwPcEk4ndra9ZxDPmNuSaN8scUIoIDDbR3_5D6df29T8sgmTbnglAY3rnKHzavQAhWeQnovWuM27EbPMY8lB5pUL6yeGygtBj2_NvMiJHyGuk5sJqmGDKljsgEHoxxmN7PSc4AXSxnmLMpzObmUkTRGoXQC7Bv1JWtJ_-eWcaHnKngHpQ2IToVvRpQF7WQUxZcpLtMPkzqitI_ZAGaoj-rM1ox6UkHhaP1eKAhb3Kfjo0_DUGnm8M84WCSN2q94-o9CW2sB6kHvde5PpW7xCIAKH286yptJ1BZ88YZeYwq-bjGH_RvDe_aUGLpauaBdyQV0m95GtoWZw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)ارتباط با من:https://linktr.ee/matinsenpai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 17:51:23</div>
<hr>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cvEaJYWqwrOVb6GLalhXW--tu6xY00gXErHFMB6jueMK3lTWF0DpJT2IncyrOMNIIOKH3Q4F7pGrKmNbasjzEyFdyg9Pl_4bZ5rIpB-yIdTZXNdOXUfqgHFxosaXbDSYARPgF_x7QJah4Gs83rhbQm1H73eQ7jEC-vU84QcEq_581m4bmTrnfHTAwENy_nInWbXsuQ534XBczqysrGdSYI2hSswcN9o26qEkOWXXPb-w_czVnFGgIIpRygCSUuoojoOg_dRvdTpTlj5zw5x1kiBxeeOSpr7aOZkgSEOiGsm3UQLwQwyEDonsAaOTWQAY24UbMl77WYgB0AefJuMpcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Lo2XHFiRSPPUKWxZE9gR2w1rEwXbURhj1X4ASO1B5T11rwid4Kjht0CaKz7wMvRKkqIru1roWvw0AuNNuWauGlIkD4mTWopjuldcX5ALa7B7Mi2iAPfXkYtOGMfFGAugaAHA5SluZ4ewwgnqzv8-b7gGvKyNbMCXhfkbhC8s-vrXPUxE-BfeY6g0vXtPrbN6BIQWKITNiqiu2wV54PIsod_cwPRlkpo3msTcM5bm0M31QVzac6V9N9nKXnxi_w1XtZk0IZNqa1UkF4HevXxpNA6Da3zbApWnmMaabIYaOBQ9K7fV2uiOEBTziLk1H9nbe8iaq-z4tPsP-Mgb1__ZjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/MatinSenPaii/5488" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTaleo Comics | مانگا، مانهوا، ناول و کامیک</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gsowjA_eXMYh8vPtOUwWSbvBmTLXOC-NfkbWffbkz5io6LQDkj0Ko0u0VFg6no3GSXVRAPbyoticw-oy0NUWo_1mv4fPRppkdqJmfxYwhb4gkxYrprOK6r2ccjP87DVfZeqH07QYQOBmT8cXQqBuBseSRn_pgMRqq1cv4kJSHAAIzwBFLyN_yO6gKDvd76pMLZQBb195QyekVtuNipov_rxrvQfImJOXbL4slHF5JzZCb9a0wVNiA7z9J4Mgx61G1hSDnMZgFi1Ruuzpp6-XrlbHJ3wjDN1qjpcKn2intrKcwSE0mcHIFwgCy_3jy_KjlChhpaKmvguBvEe_INyJ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔤
🔤
🔤
🔤
🔤
استخدام ادیتور مانگا و مانهوا در تیم تِیلو
😳
شرایط:
1- تسلط به Photoshop(برای ادیت با کامپیوتر) و یا ابزارهای مربوطه در گوشی موبایل
2- حداقل 3 ساعت تایم خالی در روز
3- مسئولیت‌پذیری
4- کار کلین(پاکسازی متن) و تایپ‌ست(جایگذاری متن)
به همراه یکدیگر
انجام می‌شود.
5-
استفاده از هر مدل AI برای بخش Clean، هیچ مانعی ندارد.
وقت شما برای ما ارزشمند است.
حداقل حقوق
به ازای هر چپتر مانگا/کامیک: 60 هزار تومان
حداقل حقوق
به ازای هر چپتر مانهوا/مانها: 40 هزار تومان
نکته‌ی مهم:  پس از استخدام، یک ToolKit کامل افزونه‌ی تایپ اختصاصی برنامه‌نویسی شده‌ی فتوشاپ + اپلیکیشن کلین با هوش مصنوعی در اختیار ادیتور قرار می‌گیرد تا کار، ساده‌تر شود
برای انجام تست اینجا کلیک کنید
🥺
t.me/TaleoCo</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/MatinSenPaii/5487" target="_blank">📅 14:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/MatinSenPaii/5486" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIb2t0ihGOIMcOmWciIGAMA-k4YxDKgHnekm5G7YWVb0-d9fUj3o1IY3YOQ2v4BCybuWTr2oRG5RVRFLMtk3ABXXTh9FSpzc8-r9K2Q1HNOhiNG1E7N3dMOAPHCmNE3YPqfSaI84iWzBjFEDlN61zkdi_OZUyVnvXRICyY9BHu-8MtJxB_ia5pWn3Ds49ND5jjZ64AX_BVOn36hvzAmQvq_zcLT8HobxFpesB1eiPRMG8fjeA8G1EMCh18NaIwINGY93r04eqZ4JXu3A6hpeD0Yfm6O2yw0LzINlfnnI9-JkUvKRf5KLLuC21THiZA92GtlOfT9xLpfkGqPUhwbLfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان دوران بارکدهای سنتی و آغاز سلطه کدهای دوبعدی
بارکدهای تک‌بعدی خطی که ۵۰ سال پیش اولین بار روی آدامس ریگلی تست شدند، کم‌کم از بسته‌بندی‌ها حذف می‌شوند. طبق ابتکار Sunrise 2027 سازمان استانداردهای جهانی GS1، بارکدهای سنتی جایشان را به کدهای دوبعدی مانند QR Code می‌دهند که می‌توانند ۲۰۰ برابر دیتای بیشتری برای رهگیری زنجیره تامین، هشدارهای فراخوان سلامت و تاریخ انقضا در خود نگه دارند.
من هم قبلا یه ویدئوی کامل راجب داستان بارکد و اینکه چطور اختراع شد و سیستمش چطوری کار میکنه، ساختم توی یوتوب:
https://youtu.be/PAHA55mHLWs
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/MatinSenPaii/5485" target="_blank">📅 13:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PdlTFsxvjKhUsnuYINzE62hYmr8VvEaRlgZAl-5MoGVvsBWalOMyecSoApt39JV21drP-lyPsbnaiL3k6K27GOS2l3MhnN95HX-rc654mx2Xxfh1U8admTxthaZ9BDsxk2whD9tEB3eUK6-RR71YLEv9nfbB7WKMoF_gGuaYOjUcxkjHiuKlNfQpZpaCyXzJL9PQFJEZJZ6ZFlIqGzd0NyrN6z-Epvr2r7aSqjaTZXk9kCEsWeI5xqaMJmxTT-Kg0eir0zXQ2bNfVs7PSRtjQSTbgy7hea_iLujTClflRjKMmF7f7OCks7GwvNBVqu2JXr4LOkRjRMHE5isdQLVSSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
عزیزانی که با WhiteAether سخت وصل میشن یا مدام قطع و وصل دارید، این روش رو حتماً تست کنید.
به‌دلیل اختلالات شبکه، ممکنه Endpoint انتخاب‌شده مرتب قطع بشه و Fallback به‌صورت خودکار Endpoint دیگه‌ای رو انتخاب کنه؛ همین سوییچ‌ها می‌تونه باعث کندی و ناپایداری اتصال بشه.
🛠
برای رفع این موضوع :
1️⃣
وارد بخش Routes بشید و از پایین صفحه وارد Endpoint بشید.
2️⃣
اسکن Endpoint رو انجام بدید.
3️⃣
بهترین Endpoint از نظر Ping رو انتخاب کنید و روی اون بزنید تا Pin بشه.
4️⃣
گزینه Fallback رو خاموش کنید.
🚀
حالا دوباره Connect کنید و نتیجه رو تست کنید.
چند نفر با همین تغییر مشکلشون برطرف شده؛ ممکنه برای شما هم در شرایط فعلی شبکه بهتر جواب بده.
@whitedns</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/MatinSenPaii/5483" target="_blank">📅 10:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVIirLAQBjH_Mb3Pv93TttYuUlmY0urdPXbTI14BuLFhzRufk5_TbtZ33bRAyc61aRozI0wZWKuKby1w7X-oUmGM5pkLLJAHUn_ck4NAV0R1yYL8FCQIa9cJveJf5VW3AQmHgSgUW7TEUzn52_7pEFIv3sU-D_Uu-McOiwubOIHjJ47ZPpoit-b9LuJhztBk07yfjEjXothimwXM5O2a-BS0mrnV-1Yd-yHBUMp7krhdbPvqo5iKJ9NYEOHIpC2k8eM65dYuw0v3M_7hEpprnyQuRd5yxKyT_KZgQaoS7v9cd_vMaLheF7uGdK80D_JdGMcR_V7NtTSKIIJffqq-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل رسماً سراغ سوئیفت سمت سرور رفت
گوگل کلاینت‌لایبرری‌های Google Cloud API برای سوئیفت را منتشر کرد؛ مخصوص سوئیفت ۶.۲ به بالا با SwiftNIO، مولتی‌پلکس HTTP/2، انتقال gRPC و ایمنی race در کامپایل‌تایم. گوگل می‌گوید با کانکارنسی سخت‌گیرانه سوئیفت ۶، این زبان با ایمنی شبه‌راست و پرفورمنس قابل‌پیش‌بینی ARC برای میکروسرویس با Hummingbird و Vapor و زیرساخت ابری ایده‌آل شده.
مبارک سوئیفتیا
🎨
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/MatinSenPaii/5482" target="_blank">📅 09:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tFstmDj0rdeG3a8qaNQE_pSXGaW6pmGewKswS7Mw77mpZj_QEpRLQGUuo6oc2FQg_kogaP1tx3Dcd0wa73o8JvEx1HXbrr5Wk_KhN1dMij0b0u6MbQG2lS8ry9d86pIZUBPgH9oKBsTY0SQ65cVFBg7P0TtrC32NUqdgSxQ3naP1ml_pb1oUpiZ2M5FZTKZQNPRHU5bo0CJM60fMTK-09rlvSLsMmYpxoUMNwbTRqmBgtf5ICIqsGTqWxAJII1KkW5MwqyiK8JIxQGpthMCoggj8ztf_VfqvAEmZ7X8aVRDfD50jEsJD2p0JUwP79yolK8d1V8UqThts5yJLZkISNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA  من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5481" target="_blank">📅 18:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XWNwWpST1YIRvuqPE3yC9Z_9qnEhJoxcygZIV5GESC4-11hoekarBpAWHrc559RAz5HZ3VPKP2OpKzQ0l97mzyrZ5gUbOE3XCy8gOvTX8qHzOuiA9NSy2PXI4snE7WXI9mMlMssbEWMtHv3WJrDuXfBork8zBKxjuuvj73rx-8eHKsTBWFst_k9ji97p4s7ZuONZ7goeMHSZFFmt5g2qyz6bSWy1l1lTPPKN-IfVKAlsqIgQSCvnQ6pQl7CZETkP38UTmXGQSzOUCjctQ1L0bdOy5-HL00hKoU5uUwOk78pdbhoYv56DHFjrakwNXTl7Tw5T_bg5PqQjfQ2jfTyMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qFVK8L-xFytmdEhYjtDAFojy7qGd4pKXc6ZxE2Qi8YeJq7gem50f-hHD3tiharqoXfS1JukIHDXBEJtZoGvUtOILg8PbzObIAHnbvVETQqttPk9OE3Pr1iNByESVjb1U8U-fA4ZFiTrkrpgtbWCnM3TACSgObkaLbXLFC_HM2Z5rhSwhCIZdSXdATuECXgfv8db-ZEFDnl8kOG2mAhnqf9MHBF4YHLcznjk3I56TRLWu5UsDE1_pSevVtjE8m3DOZJDkvkDO--RxsVIQxfCLrkqnv5vDccfO36U-NVEuhwaWP5zie2jZjOTa1Y_PAbAI7fNmffF-RtyHeyMY_jgzew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5479" target="_blank">📅 18:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZhOJbTdk83cEpIuoFAEyF-SW5YsOYSIqDE46-97kJlGQyY8IyB6DDxTcf6zKnu8aqWTSrNGBlxHMIczdxVCXRC9r3WS8JgQwprnQ7ipvaMDPD3DgEsiwosKyZ7Rw-Gc5ev_UxH9iltfwm8p3XCklYy6IBiZ_UFFNJ3mvGTY1jS2UpoW6axAFcDxIwZ_HYEFUJUtS23XCjp9OG8JzvvSKi2-bnVv9iMisaE7t8B5G796dybi3w4_YVUe398M-5iDsNwQC-JwgxrtbHCzi1rnjbo15bJZIlTyp2vTL0vQ73uEV6n3kG06HffeHW1-RffsPwNPj0yQCRKba1Ft8DMkxJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA
من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد دادم چه شکلی ازشون استفاده کنید و حتی با اینترنت ملی هم بتونید دانلودش کنید.
امیدوارم که مفید باشه واستون
❤️
دانلود Ollama:
https://ollama.com/download
📹
تماشا در یوتوب:
https://youtu.be/EAF-hMPUMYc</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5478" target="_blank">📅 18:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5477" target="_blank">📅 17:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXrDIndqGoNv245o8NEGXtc35YgR-LtdwTuOPnS_sV5NOz6usePQTagYQ72yaDMxP9UwlAl5dtBc4c122P0iX3nyvDmXsK_rk9ERRZ-2sNEwu8Tyq4HlCIRqBXN_0ybGf9QQ3IHR9fWWu0XvjnMbxuDJgP4ZIA9_6NB-Mnx0Os7_AyDNwA1NBNsS9o7dRgOIrLoRWHYk8xtzjImjA63P4gPI9p_OGdemtzI25Eqdjf8V5ZLXgtjLBm_qSUFoWgkYko63PWzZb176qOPduRgG0snoPOt-N8qmbJTEj7W9sfEYvNEizzqIFpfunmZNlhmqAHPaqMcJaaOyBkJKBs-yRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به جای توضیح دادن «اون دکمه رو می‌گم»، روش کلیک کن
👀
اگه با Codex یا Claude Code رابط کاربری می‌سازین، احتمالا پیش اومده نصف پرامپتتون صرف توضیح دادن این بشه که دقیقا کدوم قسمت صفحه باید تغییر کنه
😅
ابزار Agentation یه نوار ابزار به پروژه اضافه می‌کنه؛ روی المان موردنظر کلیک می‌کنین و می‌نویسین چه تغییری می‌خواین.
مثلا:
«فاصله این دکمه از عنوان، ۱۶ پیکسل باشه و توی حالت loading عرضش تغییر نکنه.»
⭐️
نکته کاربردیش اینه که بازخورد رو همراه selector و اطلاعات المان به agent می‌رسونه. می‌تونین خروجی Markdown رو کپی کنین یا با تنظیم MCP، کامنت‌ها رو مستقیم در اختیار agent بذارین.
برای Claude Code یه skill راه‌اندازی هم داره:
npx skills add benjitaylor/agentation
بعد داخل Claude Code دستور /agentation رو اجرا می‌کنین.
فعلا به React 18+ و مرورگر دسکتاپ نیاز داره و بهتره فقط توی محیط توسعه فعال باشه. تغییر کد رو agent انجام می‌ده؛ نتیجه رو هم همچنان باید بررسی کنین.
برای رفت‌وبرگشت‌های ریز طراحی، ایده کاربردی‌ایه
🔥
معرفی و دمو
·
راهنمای نصب</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/5476" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">در کنار بلاک/فیلتر شدن دامین دریافت کلید وارپ، اومدن sni مسک (Masque) فعلا فقط h2 رو بلاک کردن :))</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/5475" target="_blank">📅 13:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5474" target="_blank">📅 10:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">چطور فاصله‌ی بین Hermes و دستیارهای اختصاصی Dots و Grok رو پر کنیم؟
یکی از کاربرا توی یه راهنمای کاربردی از اکوسیستم هرمس توی ردیت، بررسی کرده که چطور می‌شه بدون نیاز به پلتفرم‌های بسته(مثل grok bot و dots و muse و...)، قابلیت‌های پیشرفته Dots و بات‌های گروک رو توی ستاپ Hermes پیاده کرد. راهکارهاش شامل لایه‌ی مسئولیت‌های موندگار (persistent responsibilities)، سیستم دیده‌بان پرواکتیو (Scout) برای وب و دیتا، مدیریت وضعیت تسک‌ها با SQLite، و تعیین سیاست‌های دسترسی قبل از اجرای ابزارهاست.
که البته خیلی از ۱۱-۱۲ تا قابلیتی که گفته همین الانش هم هست، صرفا دسترسی باید راحتتر بشه توی UX خود هرمس و به نظرم کم کم به اون سمت هم میره
👍
پستش رو توی ردیت بخونید، بد نیست:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5473" target="_blank">📅 09:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مهار دزدی و Distillation Attack مدل‌ها توسط OpenAI
شرکت OpenAI اعلام کرد یه کمپین گسترده و سازمان‌یافته برای استخراج و تقطیر (یا همون Distillation خودمون) قابلیت‌های استدلالی مدل‌های پیشرفته خودش رو متوقف کرده. گویا مهاجم‌ها با کوئری‌های پیچیده در صدد کپی‌برداری غیرمجاز از متدولوژی استدلال منطقی مدل‌ها بودن. اوپن‌ای‌آی دفاعیات و سپرهای نظارتی جدیدی رو برای شناسایی و خنثی‌سازی تریک‌های Adversarial Distillation مستقر کرده.
(ببخشید برادران چینی. راههای جدیدی پیدا کنید
😭
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5472" target="_blank">📅 01:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5471" target="_blank">📅 23:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آرنا توی این ویدئو، قدرت Gemini-4 Argon رو بیشتر توی زمینه‌ی 3D و قدرت پیاده‌سازی گیم‌ها و محیط‌های مختلف بررسی کرده
که خب کامل نیست و باید توی تسک‌های ایجنتیک و کدنویسی و بکند و... ببینیم
انگار که کلا قدرتش کمی پایینتر از GPT 6 sol هست که خب، ازم بپذیرید که قابل قبول نیست برای گوگل، اونم بعد از اینهمه غیبت کبری
توی دیزاینایی که نشون میده، قدرت Sonnet 5.5 هم می‌بینید
😂
خداست این مدل
https://www.youtube.com/watch?v=h5EL5zThKaI</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5470" target="_blank">📅 23:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tMsxgZBHl48Eg_FuqKtRvD3XEKCfyil18o5LElEkNqDw6oG1J0YzbXd7mdq-5zDWfGHfAvhh279bZtAPpnk3tJJvF6cGHXcyAIdhQCtjrlnIj1sHBGP20FoConZqp5hpt2r_dJ8WC0vgfxTdDindsBr1sy-qc7iabgaNlSa_TToi6cTHg7Bc43o0Urvywqm8bfgbw4kJmmjIS98TimIVi1jT5J1QCZGqIxxwZN5wvVuAGxZCpCqudhiNP_CrmUgZyMJqQFe4Qawdt4w-dX2puklvp1vGSm3kV5vcxyeZWXWgjlPWKW7EJmctqtZscXH7IZl1Ik7mKaQKy9vG3cKu-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)
1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا
https://github.com/patterniha/PattNG/releases
)
یا نرم‌افزار PattN(برای ویندوز از اینجا
https://github.com/patterniha/PattN/releases
)
دانلود کنید.
2- کانفیگ V2ray خودتون که با Worker کلودفلر ساختید(آموزش ساخت کانفیگ رایگانش اینجاست:
https://youtu.be/iAbYpjXyLpY
) رو وارد اپلیکیشن(PattNG یا PattN) کنید
3- توی اپلیکیشن اندروید، روی مداد سمت راست کانفیگ و توی اپلیکیشن ویندوز، دوبار روی کانفیگِ وارد شده کلیک کنید تا پنجره‌ی تغییر تنظیماتش باز بشه
4- توی بخش Finalmask raw json، این مقدار رو وارد کنید:
{"tcp": [{"type": "fragment", "settings": {"packets": "tlshello", "lengths": ["0", "104", "1"], "delays": ["0"], "maxSplit": "0"}},{"type": "fragment", "settings": {"packets": "1-1", "lengths": ["114", "1"], "delays": ["1"], "maxSplit": "11"}}]}
5- توی بخش Fingerprint، مقدار رو روی
Unsafe
تنظیم کنید.
6- مقدار Alpn رو روی http/1.1 تنظیم کنید
7- توی بخش Cipher Suits، این مقدار رو کپی پیست کنید:
TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
8- کانفیگ رو ذخیره کنید و پینگ بگیرید. دقت کنید تمام موارد رو انجام بدید. آیپی تمیز
188.114.97.6
عموما کار می‌کنه. اگر کار نکرد، از اسکنر
https://github.com/MatinSenPai/SenPaiScanner/releases
که هم نسخه اندروید داره هم ویندوز و مک و لینوکس، استفاده کنید و آیپی تمیز پیدا کنید.
مقادیر ممکنه عوض بشن، مقادیر جدید رو می‌ذارم خدمتتون.
موفق باشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5469" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILjrPx8Lq9tp9QONJw4ln-RgDchEkH1oUpWOLV_a3k-rhXFDr6wknqHUyeNypbwF9gV4caDNQMawBQaMYKBlCa2vOiCHWsVXhOJidvFHw2acnzH8FjM-CK7Hlt5uvnZFbmAzWZN6RmoQWYnyEtoFwOYI2PkK0lvH2ewVY0COhrqD0x_y9hkj6_dpN68o7BmVf0_mrW5tKk0k6zcHWTculWpVVZbfiDjvquBjFzmGJWz8_IEuWO8gTood0wcPAh716WfXj_pRhm8QqlZhJm1Ip3D_RzhhCVhhVTgcY-7N5T3Hz-88iZuHyeUQ9TWFvcFxRRt8Ttc1q_cOi6ouafZi0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل Airbnb: ایجنت‌های هوش مصنوعی به سیستم‌عامل اختصاصی نیاز دارن
برایان چسکی، مدیرعامل Airbnb، توی گفتگوی جدیدش تأکید کرده که
پارادایم اپلیکیشن‌های فعلی پاسخگوی نیاز ایجنت‌های خودمختار نیست و دنیای هوش مصنوعی نیازمند سیستم‌عاملی مستقل و AI-Native هست تا هماهنگی بین ایجنت‌ها و خدمات به شکلی پایدار صورت بگیره.
خب مشتی یه کاری بکن. ما هم میدونیم
😂
طرح نیاز که خیلی وقته شده
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5468" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بزرگترین مزیتی که ایجنت‌های شرکتی(Muse, Grokbot و Dots) دارن اینه که با مدل خود کمپانی یکپارچه هستن
برای هرمس، یه کم چون دستمون توی انتخاب مدل بازه ممکنه گاهی اوقات گیج بزنه یا دو نفر با کار یکسان، تجربه‌ی متفاوتی داشته باشن
اما همچنان هرمس رو ترجیحش میدم</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5467" target="_blank">📅 19:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">قراره با هم یه اپلیکیشن تمرین زبان با روش Shadowing بسازیم.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5466" target="_blank">📅 18:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qYdcSJwVxlq4oztH8rPdoMKr0NkuWh0wUFpTa2ieq_wjBxt0nzKvuDGxNrkslCToynm2O2noOnQfuodkjMMAdJuojIUCorRZWZgNxJhP5WDDPyGADJAppOP2Aaa6tPsQl756kXJNTvUvFLwEeJ5Y59_onCassMr6s_JpdJ9BX3zUtUxJyb2QaCjbGJS8D9UXOXHSppuwvdkVNZMkYccvugGqsKwkIwb8PXeg5uSmq-I4JmiXG9uSymUTi15Hp64mxxQcIufzZE6QmpW0xMjAqwK4auvbY5-GaNV-RZUdpROJ_sD6axDr7cyeGNbGbmu_HYE90QAV4uif1dPsO-C6Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردیت فیدهای RSS را متوقف و دسترسی عمومی به API را مسدود می‌کند
ردیت اعلام کرد که به دلیل اسکرپ گسترده داده‌ها توسط بات‌های هوش مصنوعی، پشتیبانی از تمامی فیدهای RSS را از ۱۳ نوامبر به پایان می‌رساند. این شرکت همچنین تاریخ توقف کامل دسترسی به API عمومی را مارس ۲۰۲۷ تعیین کرده است. این تصمیم در شرایطی گرفته می‌شود که فروش داده‌های کاربران به غول‌های هوش مصنوعی به بخش پرسودی از درآمدهای ردیت تبدیل شده و این پلتفرم دسترسی رایگان را کاملا محدود می‌کند.
که خبر بدیه برای ما
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5465" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">امروز زیاد ازش استفاده کردم
گفتم یه توضیحی راجبش بدم</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5464" target="_blank">📅 18:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یکی از قابلیت‌های بامزه‌ی یوتوب، Hide user from channel هست
این شکلی که وقتی کسی کامنت دری‌وری می‌ذاره، زمانی که هاید میشه، هنوز می‌تونه کامنت بذاره، اما کامنت‌هاش رو فقط خودش می‌بینه
نه من می‌بینم
نه بقیه
اصلا هم متوجه نمیشه که هاید شده
😂</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5463" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FoMyQFCenFsG9thDMo6an9jOgnCO61Iqe0cbHnD0-kVxo9hKsgkU6VsC_G5ldOEsbVscyLLTDHcNV9GDoUHDZ5lZZ5F-zU8zro9a6446SDe2FuTSDNsY_40Xl3WlIXB-B9dFJQtPVB3-cfMoj6Oexc18J64gYseJy_v7ZXuR6M4P02c_Ac4hHOcdPMJU9hm3-91PqnIi0UbEAoXKU0E7zb7RqNu1-jMuxlwJN6lRXHetjJ0BmczhE55F7P5Wi-VJTExJoQSsVqhbmZEuLm96ky7BGoIeJ3uzRoZHlzIoK09X3THB3chHCfCB2DtLc94rWICyPIMRhV3coaXHSagk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5462" target="_blank">📅 18:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wk9rGK8Y3tCmfStrC-MRSd-SRbRYPLfygP2IutXM4ONUz2qAbv2iMph1bS6vDRgKuJnHf_0f4s6_HyP14vKw89WGL0v4DgoE518nKFDJYOEvEw7q8qOArN1RSBKbUAdWIvygb1OY30RBuEST7phB81T8kMyxPJln8FH6HkRGUGRNzxf4ks5OPQWthZ948Y5JyNZFdfO4tzQcExQQd9vOq143zIwcTrvhF0reC5Bt3QNtp7Bn9TVe4dEums0Zs-Vx0gQ9GAvZRbty2VATKv7q0013bMgHR9BWUpu0uNB1R0fk-3rmvbt1hEUNFeDPIQzuV2lzCf1-nVgXqqFWS2C07Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Decisions API توسط OpenAI برای اتوماسیون فوق‌سریع تصمیم‌گیری در ایجنت‌ها
سم آلتمن از عرضه قابلیت جدیدی به نام Decisions API خبر داد که ساختاری مشابه مدل سریع Jev از استارتاپ TypeSafe دارد. این رابط برنامه‌نویسی به توسعه‌دهندگان اجازه می‌دهد مجموعه‌ای مشخص از گزینه‌ها را به مدل Luna بدهند تا با سرعت بسیار بالا و هزینه بسیار ناچیز، به صورت احتمالی بهترین تصمیم یا اکشن را انتخاب کند. این رویکرد به ویژه برای کنترل ازدحام ایجنت‌ها و اتوماسیون لحظه‌ای نرم‌افزارها کاربرد دارد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5461" target="_blank">📅 17:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GlbC5LwEyVxvJ-ykdqWUM7sFdJ8vHgVxGWIQkZP9UD_o5M6hUzE6S8E9Wm6ri4OzLxrxADEtVwLnXZMAcTSoxL3hL0bn7lliDXnFVKJ6if6Oft9_m5-4PMJNAnPOgOToumkz1HR-VRbz7SccHgd6HJmhziQYjYHSTy_8sAmLKn-i6EXpHCxrqwtz3SMFL5h5okRzyOXQXZZpu2FTTgbkf5V5399FdoTFYv95uooy8JN9sIjHSZK5iJn95ay0eZjHU-j8lPSeg61fctx_lDj1kzaxjKQ2lGthGS616k83tFnYkTZ9Nlz2paalRUtHohO2D9RCKPLMXMhAsNHfxEocIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به قول Theo، چرا واقعا OpenAI هنوز داره از GPT-5.6 Sol استفاده میکنه توی چتش:))
نه تنها 6 sol اومد، بلکه 6.1 sol رو هم دادن و چت هنوز روی 5.6 گیر کرده
اولین باریه همچین چیزی رو میبینم حقیقتا بین کمپانیا</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5460" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R9YIMhgn7EYSyzhjh1NcJ2ePgaf5ZmCrF6kgWHl-D-MGmJvH3tZLUml2y2SiMarBhrEwkqtre5lUWb2EAss4GLx1R3483dkJ6-opfqAuPO_C_yzhBmSTZRp5ddvpAib1dybhFEBqZEzisDn0df2Fxi3k0nyqieQcNxSnRL_8lAA5ilz6FqInw2IFU4dZpI1EAqLCk6mjUIZiNtX181oqTAyXZmI9qbD71L-mlLGJGVyCELHonBdn_EiLNCZu_jA0t1Jvl0SvDRD3TS9XDK_Zmkd-Lk7K-fLJeb3m9RLjcbOxfP4pYSdNa9EnlMr34b3m6lNGQ6VsGr_7mxhjT2mVqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله ما نسل Z هستیم
😂</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5459" target="_blank">📅 12:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oQfD7EmExEjLl2aViEor7JHoAvZ0_9sr7fxfat8guyp1pRxKOtJlkfaM_m6ZmtcxbxxYg1AalEa99eaSquibjQN_eNGSg-SP9Q9QifV-NQ9_PRKR5q1YZKla5wmydL-m5dDRXUvA7AK8Ludib_rRGnt_gvFbYGu5AY_64uzVBBAiQj3J54Ny--eHaSC5HcZx89yeE4hLaQwwWhzZM6b4zXgZBsM2EjHwgvwo54rT6Lf5RmZLeU-LSETVPw4GTpFVdPwZdoZ9dpTgK7zf8CpGAfbLBl_LsCB9uaWODZ7BLb08Cnw2MWQAiki-BO5jmIfmeG2LQt0MjfcmY_HKiLPXIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate
توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب:
https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5458" target="_blank">📅 12:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شدیدا حس میکنم مدلهای چینی اوایل که اومدن غول بودن، بعد از عرضه یهو ضعیف شدن
مثلا هممون به Ox Alpha دسترسی داشتیم، بعدش که glm 5.3 flash معرفی شد اصلا اون هوش رو نداشت.
یا من به Qwen 3.8 preview دسترسی داشتم و خارق‌العاده بود. سرچ کنید توی چنل نوشتم از تجربیاتم. اما الان Qwen 3.8 max وقتی ریلیز شد هم از مدلهای Frontier خیلی عقبت‌تره هم توی بنچمارک و هم توی عمل</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5457" target="_blank">📅 11:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cYwLKYlEUoSTlDAH-u71mpCCQXE56-ov4UFEUwoANmPB_WGg-tEskkRv41v3dSDtVj9A55Fsu8bLvLXwePjRzV4rXUc-t0UfTUu7gLW-6bTKamK2Z6DiFMq-YMNnAOjFhGVToX2j5bomRXXTEef3Wsw6JTRLmUfyxWSjseY9budD3t8S4e_OC6-CG5I5h0xJ98DPOVyNYE8ZEfM3_sBHP2FbtzpSF0XlByV2EQUOwAn2sjaTWYkuAmQhiBgR2q4aVLmFjs_Fi4LCknrzW7nQIp8oQm0-skIyu7wOFB1eq-Jeb8bRIbpQOlKkUqZIvijjn-VHI5y8iYFhcVBtbXxMgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم به نوبه‌ی خودش عالیه
Hallucination یعنی توهم زدن ai
که این یعنی جمنای 4 به ندرت از خودش یه چیزی رو در میاره</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5456" target="_blank">📅 08:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کلا هر مدلی که میاد
این قضیه‌ی Benchmaxxing پیش میاد
نگران نباشید
میگن توی کدنویسی اونقدر هم خوب نیست انگار و باید منتظر موند و دید تا فردا پس‌فردا که شایعات و تست‌ها به کجا می‌بره ما رو</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5455" target="_blank">📅 07:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C-Fl7thtNhrAQs5ri9mkwHZA5F7v5myz86pOG2AWtQsPrxRiF7jdYrzIRsasbd88hOQLQxZPf2nrIZeVo_7G2hk3QFW-CYJuI9jr8jXF7jtbaM8vNhz0sULXFEJ4EZdgo9OTyxZCpB8otfTmvJTalFvT9oWmF0LIdje2utQSFol2_FdJjxPRag8OjpSBmr-aTTkPzeZ72tnhDM2AQPGo18iXSz5C9u85pY_eNd7HGqdQ46LvXFfLI--9uwUG61UF1cae3fKvwxc0JtJU4kSFj8dt4gN0gg4rT3EkQv3ZZMpUuS4LlTEIUIFW7k74PrSPlrlURvighdusNeHktooWaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SPnXRGFWdNbtmUAQhT6d5e_tn0QvD8B-5Yqburbyr1AF8V0MpZB7FA3q4_LA2scOqUwRIbtYOnftz12sMY7wime_VisGN-xqjhW5Rzmyf1JxnoirmYpuHTDRHoKq1h3aYn33pJxCPpC6z-9gU_gcqnEMyCTiABL3MNLPsOyXuA12StruDmLGK7y1Z3WvwTZCXx0d-MOdRN6QUVwTbErMu4rh5OxTmm9sM_7qwX_LIhu7YvzUO85KfzuhsaAM7lXjaeTk1kjAVkhtJpVIyGlsEjsmJXVFwkxZ_BxSuCtA5DeWtGUNSYdeRRZuMSW54_PDnWyV5XTxWc-bXUTCC6Eewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G4UGIoniqwCNWNt_RGJe98v9nkd_c4PuAMKvDY-vl_aruWDxmXU5CQIJzpn7ajFGkDTKuU6NEGP_pSFhJIH2KOFpfMh-ibxeGWXefjKMfQEkuf13LSFDQXbkWKTrkDhb1iJ5ruNpYL4OiSEjjzAFi-oC6W0CXMjLb2D2uuNIIe6trNEhLu0lIKFghMC3-AcCA7GJe-LAdSjzRjy149N6vCwxpcHGI-jbiBbnn71QucGQWsW4m0VwHeMNe-HtjeU1CYvOSaBDrqpTl_DRfdc02DR31nnNEVusgaA2YnRaT7sPhhKx759DaDg99QdzYQWPNVeJGG2LbF0NDsTEkQIDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XubHfQApfmtI7J-mihfuio9UUWh0kyNgIa1On9CPjl9Bivs4qlk9s4mkBtHIbX6_tD2bal7Ak_V8_-qkCrrO_SOU6up_iMdhnSTc6fa7dRbJDFC088Wj7Pu13gjja7XEMneuap3e4QNlVjIHRLbgyec_9xgp-JfbcZUNOkKF4VtIk2NWU2FllfmB6yzfDwh3_00emWO9NTxARJt8ASy1R-jhz04i2KYlr3yig9Twq1fjUSzICWL_brLw5F8ahpQxGNL6WNRqYYZIT2hTRwwK6FKB3nD0nd_7l6W49VdyoBFPlMz9GTkLIG0CNNT1Bx_GWjpHOcyBJdKKVwNK4dDdAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری  گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5451" target="_blank">📅 01:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=ihcvrBwSjKcG10phyLiFHDQRb7ArbMoJ9mH5qAs60vgqi0teW5EEhMO0aH8INHAUPnYj0qCkJk_JaiMF-T0Q5o9vnRqKJMOa6Gos8SrBlGUjcjXX5_XYc2LgL0kaE4HWIEojTWwwPY4N99zmoGEZi38v2yBCwHrcQt4w6fK1j9U-7ri3-SM9U0QOSrjTL3gn6c8ANHQrGqxPy-61Cw8hvX_EhvkLWh_iyJTn4KQbZSA69gougzFl7DZF39W51XDoMjYqeC6YmYia9vI2lbJf6WBL3jv_DmSNI1jiyZNE08EXWRn_xZqFw8JowV6yNF6iTOn90WA8su60dLJ6B-jaKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=ihcvrBwSjKcG10phyLiFHDQRb7ArbMoJ9mH5qAs60vgqi0teW5EEhMO0aH8INHAUPnYj0qCkJk_JaiMF-T0Q5o9vnRqKJMOa6Gos8SrBlGUjcjXX5_XYc2LgL0kaE4HWIEojTWwwPY4N99zmoGEZi38v2yBCwHrcQt4w6fK1j9U-7ri3-SM9U0QOSrjTL3gn6c8ANHQrGqxPy-61Cw8hvX_EhvkLWh_iyJTn4KQbZSA69gougzFl7DZF39W51XDoMjYqeC6YmYia9vI2lbJf6WBL3jv_DmSNI1jiyZNE08EXWRn_xZqFw8JowV6yNF6iTOn90WA8su60dLJ6B-jaKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5450" target="_blank">📅 01:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vDdUYhMUSKfAqcmF8dNqEO9ZxmezN0e7Aiwdye3iAecgGcP0kzGbGNT1Av1-sm4MeD-I5F7iwLVyIulq5fNvQTioF-Be6Z0RBTPbmGKtU-bLis5jeEKI97ZsJQDat-e79UI3gqGIbFKgU1d46_hGZusmKUx2BuRUNLqDGIwYmzStVpi4fhofnAm-bFyrtUg5ndgA336gkNmGrdURGQsmeiWlu0RiACbMJmk_mrpwlVBRJNNxO9SMIMoJyd9bwUpcxsqOt0SL4jv4sc7tUpkFZu1c8aVSel39zAShieltBZN3HPzsrWjCeYK6LAhsUnusQVTYRsbtbeVeuZo1YQElRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری
گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای اکثر مدلا) تولید می‌کنه و توی بنچمارک‌های مهندسی نرم‌افزار (امتیاز ۷۷.۹٪ در DeepSWE v1.1) و امنیت سایبری پیشتاز شده که به زودی می‌ذارمش. آرگون با هدف کارهای سنگین کدنویسی، تحلیل دیتابیس‌های حجیم و کشف خودکار آسیب‌پذیری‌های امنیتی طراحی شده.
هزینه‌اش برای دوره معرفی، قیمت خیره‌کننده‌ی
2$/10$
و بعد از اون،
4$/20$
اعلام شده. با 0.1$(بعدش 0.2$) برای هر یک میلیون Cache ورودی
دقیقا هم‌قیمت با Opus 5.5
باید فردا ببرمش زیر تست ببینم گوگل واقعا پرقدرت برگشت یا هایپ الکیه:)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5449" target="_blank">📅 01:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بیدار شید بیدار شید
جمنای 4 اومدد</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5448" target="_blank">📅 00:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e3w_RawvUIyFUKhYwF_9jTEldY-hyTVQXZ7NaEKN1phDXsf5FrE-rYq8-QC7VVsPGs4U9JcA-pWxlIbPGsIdtdlXjix11e6gHlmP66OJjgMYu-ks7tAYQlM5vW_bKQiwo5gttNKuABhSxdxB9qvpge6ijvg5Lf19iKSZ1j0vUAr0KVdPdpu4B-FCRT6_Ch4xCgEF9kQrpH7ESHjDrttMCU2a9HEfSgXDWCbApO0kmM_SfZ9ogkUDxkvBjYBPB8BtS_10oe7Ql9YM5VRz0rQLsNMG5VsOjCpBp_1Ipv5-CegnINaGkuEMLCv-Wjr1S1AnHRFfflayHPIR1aWJ0d4XWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش هزینه‌های هوش‌مصنوعی با Auto Router در Cloudflare
کلودفلر قابلیت جدید Auto Router رو به سرویس AI Gateway اضافه کرده. این سیستم توی لبه شبکه (Edge) پیچیدگی هر درخواست رو می‌سنجه و به‌صورت خودکار بهینه‌ترین مدل رو انتخاب می‌کنه؛ یعنی برای پرامپت‌های ساده مدل‌های سبک و ارزون‌تر رو صدا می‌زنه و فقط کارهای پیچیده رو به مدل‌های گرون می‌سپاره تا بدون افت کیفیت، هزینه‌های پردازش به‌شدت کم بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5447" target="_blank">📅 23:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">من معتقدم با مدلهای رایگان، مدلهای چینی و ابزارهای رایگان هم میشه به خوبی کد نوشت و ابزار ساخت
و به زودی برای اثباتش، یه سری کار انجام میدم
چون میبینم دور و اطرافم کسایی رو که هیچ کاری نمی‌کنن، تلاشی نمی‌کنن، به بهونه‌ی اینکه من اشتراک Claude یا GPT plus ندارم و...
و این کارو انجام خواهم داد که شاید انگیزه‌ای بشه، و شاید ترغیب بشن یه سری افراد که شروع کنن ایده‌هاشون رو بسازن</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5446" target="_blank">📅 21:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ویژگی‌ای که Dots و Cues و Grok Bot دارن نسبت به هرمس اینه که اومدن قابلیت‌ها رو محدود کردن!
بله درست شنیدین
همین محدود کردن قابلیت‌ها خودش فیچر خوبی بوده(برای اکثر مردم و برای مارکتینگ خودشون) و باعث شده کارهایی که میشه باهاش انجام داد ساده‌تر به نظر بیاد و سرراست تر بشه. از اون طرف، چون با LLM خودشون سازگاری صد درصد داره، به 99 درصد ارورهای مدل‌ها و api و... بر نمی‌خورید. VPS هم که نیاز ندارید دیگه
اونور قضیه، هرمس به شما "کنترل" و "هزینه صفر(روی لوکال)" میده که اون هم ارزشمنده برای قشر عظیمی</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5445" target="_blank">📅 16:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بچه‌ها ما قراره استریم داشته باشیم راجب دانشگاه و انتخاب رشته
اگر سؤالی دارید، می‌تونید به ایمیل matinsdungeon@gmail.com سؤالتون رو بفرستید با Subject استریم
روی استریم می‌خونیم سؤالاتتون و جواب می‌دیم با مهمونای گل</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5444" target="_blank">📅 14:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YnQ86LkbFFC2W7rk_qWOQag8LBsr9MY4U6p3psYY3KzPZcNWN5LMCRA6nqrDktPODLFTRpuK-6XaNTVX5ywFq3XHQIvIFgNQHjvylNcUho5ria8jrj-TMW2XxadN88IflM6-_H7vYmMYuhOqOkPe8vdRc3Z6YK4lsTutd3-YxHfOmhD0dzR6SilaO3X26XTPA8x3OQ_uX09tt4w50MKu2aN6p5ljiIKg9buA70bst9HHPaQguFKAUK7Y5f1iphc4Kg-LIvb88zuguCZkytKad8biHE82tsULXB0etpyzZQJSXaitzjZkSUFM2WQp5_I1kQuBvecjWDlHsEKDsf7-xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری رسمی OpenAI با پلتفرم Hermes
در اعلامیه‌ای جدید، همکاری رسمی OpenAI با اکوسیستم ایجنت هوشمند Hermes(Nous Research) تأیید شده است تا قابلیت‌های مدل‌های جدید و ابزارهای کدکس به شکلی منسجم‌تر در اختیار کاربران و توسعه‌دهندگان این پلتفرم قرار گیرد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5443" target="_blank">📅 14:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بچه‌ها پدی 2500 دلار کردیت OpenAI داره که میخواد باهاش یه اپ بنویسه به انتخاب شما
رأی من زمین بازی سیستم دیزاینه
😂
❤️</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5442" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5441">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-poll">
<h4>📊 کدوم ایده رو با هم بسازیم؟</h4>
<ul>
<li>✓ تمرین انگلیسی با Shadowing</li>
<li>✓ زمین بازی سیستم‌دیزاین</li>
<li>✓ تبدیل کانال تلگرام به وب‌سایت</li>
<li>✓ ایده‌ی خودت رو بگو💡</li>
</ul>
</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5441" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QQ5y_1NsYYMQA3_N_XAL4wq_anxTaIs2hpZ6IMj9O6LmOQPjLI9EdmJMolzC-JZuD_jUuO_2cdbQRH2YoUHn3IcCfE4b0S9jIJXzaswlRV_UVHi1L0WljmVdbPZId8VjKtC-hS57y1w8HPB7B4WFmqcxn27XSEwHGEspPfV_11RfPI0-Dg_ekzroxbyauGHwC59AIPbF6rTO1ANdQ6F4giPEZrlPqrAzGEZzryri4df8qnrflxodN1q-EzrZPl08VQb6_grew6l-FID0Ncc9f5nMD3kh5TTOcb7jhE0vWx6MCxO_oVx7LR4K9V5bunSvIxQ-GJod-CJ1e0DHgH6W5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gv9yHs1GzC9DE4I2g2qKlYSokM1ZNzfYDH7fffWjFRJ6j7TufjwtLT6KBZ3DnaKe7FcOvj-rem5XQenKp4iiMhTKHcAaSnV9u9QV7KZoPKghA8Km_hz9ylGnKAb37-dpDESWm37Hq5oSjZ_ehtXYBPn9SPDmff4mgtwJDroAqRScZECOQFhAedJtaDWn4vNe3dbPeD35WKSY0L-hzy4TzOITkTFTN2JfWz1Z9QrDZTTBVF9Mb8bS2yuW8ahWo-TaK8H_0enspjumeJWEj4qRnKLDY34N_DniV-zXLAC2ymFwfcXDgMbEdsH-mWEETlsyB6iS0jbQgbPX3AqhtdD1Yg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قبلا برای این کار شاید 20 دقیقه زمان می‌ذاشتیم.
پیشرفت ai واقعا عالیه</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5439" target="_blank">📅 14:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5437">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pGZfd9R77Lvzmqvmp-bfZK5gYD3hWIDFwf5gWsv-xM-OyIcC99iFijXhmMTXPpQtB-yrCG3bgDlkGw1A-7Mjepo00DAd3cw9AlrCMGlA1Agmk7-u1d6V7Bb4jykQT4TklmAAR5UC2KXGkDCk_Ak0utTrcIaYz84V9R10FyKz6TZKBG8cmW_zexjT6yJxCzV2kYPQWqVTOJk3A6ftPN35E2UZe1QCd9aasSoiEM3bYT86RTMEQ9OzabFwQs1pP8QSss8TcFfieucpIks6SuthCD2h7hS21oE0VzGXktVB0H5v94FXGbQdPbRVrWBO-qOyUPCwSmlDBYuIkU-7iezF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s6HfgDYu1LUYCgBRtmuSAzsyzJAaEkZsMeSm7fB8ziuzw8O40X_yBMk-5Z4SoYNP0DO8jZ3oFlCe24Yr_2W219J4ZgA_O0IuFIZno76wDs-FnMZJOY7rBY4_xhw1KVmP4k3E-Z-ddLipwAoDb-G-JOJt_RJ0aN5lHarP3dqKb6O19B4UG7WX8UHXWR9Meb3HHsX-ZFWcnVRZ8ReAm7JZjbSgUucjij5gmvc2vB4Q12__ViyQdC1z98GQi1s6hOwJxQbTq5-LGuh86qCWls2hIeaMD6yzCNOHwTmeqFbebQXKNCBzOT8KpceA5Ng6XMhttXFqZ3RysLp_H_n33qYVdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز Manus پلتفرم Cues رو رونمایی کرد
چند ساعت بعدش، OpenAI از Dots
و طراحی بصری ساب ایجنت‌های بامزشون خیلی شبیه هم دیگه‌ست
😂
نمیدونم چه توطئه‌ای در کاره</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5437" target="_blank">📅 12:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گویا همه روی GPT 6.1 Sol مصرف توکن کمتر + قدرت بیشتر تجربه کردن</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5436" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">عرضه نسخه ابری OpenAI Codex در رویداد DevDay
اوپن‌ای‌آی بالاخره بعد از شیشصد سال که رقیبش آنتروپیک این قابلیت رو آورده بود، توی رویداد DevDay بالاخره مدل Codex رو به فضای ابری آورد تا توسعه‌دهنده‌ها محدود به اجرای محلی روی سیستم خودشون نباشن و بتونن از راه دور با گوشی یا هر دستگاه دیگه‌ای ازش استفاده کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5435" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=NMCsJFcbpWpI7KpHvCoZ_hB1ln7YSqVSXg54e9hvNpnVHzmr47nuIUkp6YIjOIznwDtaTOj0BSKtbVJtfQNDv0fTHCB4Y9pCqatTQmm7DyGvoSJ64V82mM5o2m6h9hwDj6QLurZ0jag6CqR1ZPhXwZXPyZcSbxy3dcNnWnxDuSTxbB63rTy3TZbUfWR2lyQg-xeujO-oXoJi44GNTXsxWBUXgwrWKOm-UzbJexVUqDlSLzLPnuMr0aq8i_hTZhsjSRwmf2kGAurRukATKQ1Km1pYc-LVnyLiOme3BTgdgbg1jx2swgBgyt5zsDudvJ5OJ-GS-zb0NoKTkDNuswyMtA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=NMCsJFcbpWpI7KpHvCoZ_hB1ln7YSqVSXg54e9hvNpnVHzmr47nuIUkp6YIjOIznwDtaTOj0BSKtbVJtfQNDv0fTHCB4Y9pCqatTQmm7DyGvoSJ64V82mM5o2m6h9hwDj6QLurZ0jag6CqR1ZPhXwZXPyZcSbxy3dcNnWnxDuSTxbB63rTy3TZbUfWR2lyQg-xeujO-oXoJi44GNTXsxWBUXgwrWKOm-UzbJexVUqDlSLzLPnuMr0aq8i_hTZhsjSRwmf2kGAurRukATKQ1Km1pYc-LVnyLiOme3BTgdgbg1jx2swgBgyt5zsDudvJ5OJ-GS-zb0NoKTkDNuswyMtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5434" target="_blank">📅 08:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حس می‌کنم یه رقابت خیلی سخت بین سرعت ریلیز مدلهای جدید AI و بالا رفتن قیمت دلار شکل گرفته</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5433" target="_blank">📅 08:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5432" target="_blank">📅 00:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مدل Ember-1 از Fireworks: کارایی Kimi K3 با 40% توکن کمتر
تیم تحقیقاتی Fireworks مدل استدلالی Ember-1 رو بر پایه‌ی Kimi K3 منتشر کرد. تمرکز اصلی روی حل مشکل بزرگ مدل‌های reasoning بوده: تکرار بیش‌ازحد مسیر فکر توی خروجی که گاهی بخش اعظم هزینه‌ی توکن‌ها رو می‌بلعید.
چیزی که من خودمم توی ویدئوی کلاد رایگان، سر اون بازی سه بعدی تجربه‌اش کردم و واقعا افتضاح بود. مدل توی thinking خودش گیر میکرد ده‌ها دقیقه.
امبر با بیش از ۵۰ آزمایش و ۲۰۰ ارزیابی جوری آموزش دیده که شاخه‌های غیرضروری استدلال رو حذف کنه و بدون افت کیفیت و دقت کدنویسی، همون نتایج بنچمارک‌ها رو با حدود ۴۰ درصد توکن کمتر تحویل بده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5431" target="_blank">📅 00:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5430" target="_blank">📅 22:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن
به اسم Dots
تقریبا شبیه Muse، یا Grok Bot
https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5429" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5428">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CDzPXy0YwhnvnGPRbJKB-TSAtxqcsvlWXvRwF7SirKxcINq-CARwmZnrEZuwmF7RxbC8L6jWBUQlH54_oi4SQZC6j3zwXFGWuXff1qOffmGv3zq3Pc_DEFd3s-h1hMxt-D5OEhIC9-H6I8dBqYvNKWLNTlgPmPirywSRD-COnjv6ESq1hqSuO5k18D8Uu3mEVUFBrbipWNbiC5KHkzsTt0pnFPLT45JYMFMUU4HeFsP8ok9URjrB0T4wC77ZmBwS_THVqD34DDBDys8ZwY1iMhGOMFnLYwGevsSooH8qAN9CnAhCt1Fc0a6Axcd13VBD7WUq9OvLC9PcPpzDp1Y21Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی خندیدم
توییتر OpenAI کلی گفته بود که امروز به مناسبت Dev Day قراره یه چیز خیلیییی خفن بیاد.
کلی توییت زده بودن
هایپ کرده بودن
حالا حدس بزنین چی دادن؟
GPT 6.1 Sol
😂
😂
😂</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5428" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EGtXlB6lQseza5P3c2j7ju9hj5Kcj9dqQMOH--3j7WZ0Ub7dv4wuR3RivcGd2ij9lqGoot-sKLbaznehnWbTTmha4XIdOxhtRLoNB5iTOBusgNebVDY_UOLfcnrDUPLojWPokiHdNszZQGPejLiaX1vmmSDivLarhR2ltS2lYyWV9HVeo2-l0jCHK2Dc_5EgMq4349EyGbhbp4qKFAbQtVgcijzBCHx1cmV-dVx533MCeNh1Om4zrbrGyf8x-R2_lYiVjHzkcXwWgdXKJiLuDoR0CkN8ikZlIJHuvQ_IsGGi507SeD7mQjru9d4QgcriHVFMhBKxRV0s1Pb-0EXtfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aH_p4Xk4IoNefcKL86GiA9lGQrF9D8pppA3s9MpeYI1fE465h-TyDNeFmEGcf0lj7cC8LRcQSGcZol0qfB9BLH37UK1SO2RpH_6E7ANwQFzZTevNsHPqPZ4uT27vw5XjCzkKqVfLuMI0XFcmeaQcn2ijeVmvwaCsTimxxIfSWCuPfJ9Q49ErJFlJbjD1cpKzhdDROLvOId51WrsuDnqp_1_mPDII1Cp3wHBf39XMClzY8-cCsb9YraH7Rkmxx_niUsroCnssQ7goie0miPEc7IklUJYHwW7Ob5ChC2HQI7HLx7DQIBZoIR_iElep_DogdLsViZsVJy81SYn1TRa6dQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کلی ارتقاش دادم از دیروز که الان داره با یه مدل خیلی ارزون، کارایی انجام میده که Astra نتونسته بود. یه پنل تحت وب نوشتم براش که اینونتوری رو ببینم، یه مدل سوپروایزر براش گذاشتم که بالای سر پلنر باشه و تصمیماتش رو هدایت کنه، بهش حمله کردن و دفاع کردن مقابل…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5426" target="_blank">📅 19:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uDN11s4rHepLaajkFs1qEuzU2EytxSv-Zv33ovIkfNwv5V_viq9q2Lvw-WDX4KOOFi-KyouzoUq5FUbcGCIqCtDmaPnq76BHX4VJEMBE9hDqtpWAw-yj8OI6Ndf3YKksVNaGDqe7EWhNCptI0aqgNU9liRE5L4REC39Nc-qqNrJhW0Fi3DlfdrdNvaPYjPneSHQquSmPLsZM3sYJKuQ7LOH9PzO8eMDhKeVdjgpwvckmWrjHWJy6KF58PwZ15bbv53OCvkKVcxrRSSEGzqFoIuOaO5lQ4sgj8A4WaZi4YAnyD6rB7k1B7TwJ7fmzA4BIeuJ2kZbowMYVZ0JZHq9IRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستیار جدید ماریسا مایر فقط از روی عکس‌های گوشیت می‌فهمه کی هستی
ماریسا مایر، مدیرعامل سابق یاهو، بعد از راند ۸ میلیون دلاریِ seed بالاخره Dazzle رو معرفی کرد:
یه دستیار AI که برخلاف Muse و Instinct، نه خبرنامه‌ات رو می‌خونه نه تقویمت رو؛ کل context از Camera Roll می‌آد. از روی عکس‌ها می‌فهمه چی دوست داری، آخرین سفرت کجا بوده و بچه‌هات به چی علاقه‌مندن.
مثلاً از عکس‌های خود مایر فهمیده خانواده‌اش escape room دوست دارن و چند جایی که نمی‌شناخته پیشنهاد داده
😂
😂
کمی ترسناکه حقیقتا
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5425" target="_blank">📅 18:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ایده بیزنس: یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال" قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط بعدش از…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5424" target="_blank">📅 17:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ایده بیزنس:
یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال"
قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار
هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط
بعدش از سودت برای تبلیغات توی کل شهر استفاده کن و دوباره پول در بیار
سرمایه‌ات که رفت بالا و بالاتر و مردم اعتماد کردن، یهو پول رو بردار و دفترات رو هم جمع کن و فرار کن، همه چیز رو هم بنداز گردن بانک مرکزی و فرار کن د برو که رفتیم</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5423" target="_blank">📅 17:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">در مورد آزمون تورینگ و مقاله‌ی Computing Machinery and Intelligence سرچ کنید و بخونید. جالبه. با اینکه انتقادهای بسیاری بهش وارده که دوست دارم یه روز بشینیم با هم صحبت کنیم راجبش
و دقیقا پرسشیه که اوایل سریال West world مطرح میشه.
"If you can't say I'm human or robot, does it even matter anymore to ask this?"</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5422" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یه جورایی حس مور مور میده ویدئو
از شدت پیشرفت علم کامپیوتر، اینترنت، ai و...</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5421" target="_blank">📅 14:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=QRtyywuRN327mHPVZ3FuN_Tg2z7HZAxGkkFRVZe8wx65AIiNTtLz7ioTpXHJ7Wk_d4X6qqHQCg5YmfoApwJ1bkYmI-OmXTnaD8C5qUKPzJeNJzpo7MRK3jUxwR-YZnsX-YaTyyMdKw64XKmhN4o56_N6OUOigZMs9RUWKJa9pE4CrX89Gjo3xfXL5q6kZ55wTiaXQFRVuddoRzghaHj-nUdXdzUsaac_D_0L19xUX_MqGL-Rgw_4UL327xKcD18HWyLDRi7Rsl3YGTp0GpDUrhiPJPrdthnNAjvaYvAXMXrO_SVfvt0tDnE6XgYCqaAcwGDz_O_N3QG1xj-lu0hhGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=QRtyywuRN327mHPVZ3FuN_Tg2z7HZAxGkkFRVZe8wx65AIiNTtLz7ioTpXHJ7Wk_d4X6qqHQCg5YmfoApwJ1bkYmI-OmXTnaD8C5qUKPzJeNJzpo7MRK3jUxwR-YZnsX-YaTyyMdKw64XKmhN4o56_N6OUOigZMs9RUWKJa9pE4CrX89Gjo3xfXL5q6kZ55wTiaXQFRVuddoRzghaHj-nUdXdzUsaac_D_0L19xUX_MqGL-Rgw_4UL327xKcD18HWyLDRi7Rsl3YGTp0GpDUrhiPJPrdthnNAjvaYvAXMXrO_SVfvt0tDnE6XgYCqaAcwGDz_O_N3QG1xj-lu0hhGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«کلاد ساننت 5.5 این رو ساخت. فقط با کد»
این داداشمون
این ویدئو رو توییت کرده و اینطور گفته
ویدئو در مورد پرسشیه که آلن تورینگ، پدر علوم کامپیوتر مدرن و هوش مصنوعی چهار سال قبل از مرگش مطرح کرد:
- آیا ماشین‌ها می‌تونن «فکر» کنن؟
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5420" target="_blank">📅 13:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=g07uBKPwSoPJZesf4VI3bOasC6upxZ1EjIFH0yiVQAfyuRaj-IUDBswT8roVKB0kiA1GOsZYxHaieKqOWSyqA2HMzB5KCE0cwdI-P5O8tLrEz90pwzms-PU5KyOlx8BTKVPcGnF-pHi8fmTGeGAufgNZy5OxeaQmhsWN5gXzKz8d1WistOfhqJvgPyySstYiyqSTNw9VkzVjOfcCBJUl9fCuLBWDhlHfX9e4451NfgI1nPX8vuiEDqKaihbWf6J1yhO40hztY-Hs67cag-b4-F5bEgmZXBl2yMtMr-uoJtH6Wx40oZSiv16jsWzGuz1-F0b0ujXNLT4sZDVEmn6Ofg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=g07uBKPwSoPJZesf4VI3bOasC6upxZ1EjIFH0yiVQAfyuRaj-IUDBswT8roVKB0kiA1GOsZYxHaieKqOWSyqA2HMzB5KCE0cwdI-P5O8tLrEz90pwzms-PU5KyOlx8BTKVPcGnF-pHi8fmTGeGAufgNZy5OxeaQmhsWN5gXzKz8d1WistOfhqJvgPyySstYiyqSTNw9VkzVjOfcCBJUl9fCuLBWDhlHfX9e4451NfgI1nPX8vuiEDqKaihbWf6J1yhO40hztY-Hs67cag-b4-F5bEgmZXBl2yMtMr-uoJtH6Wx40oZSiv16jsWzGuz1-F0b0ujXNLT4sZDVEmn6Ofg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Claude sonnet ۵.۵ توی بنچمارک Terminal-Bench 4.0 نمره‌ی ۷۰.۶٪ گرفت.
بعد این پرامپت معروف بهش داده شد:
«یه کد به HTML بنویس که یه انیمیشن دوبعدی از یه پلیکان سوار دوچرخه رو با گرافیک SVG نمایش بده. نیازی به تست اضافی نیست.»
توی حالت xhigh: یه SVG سالم توی ۴۱ ثانیه، به قیمت ۰.۰۵۷ دلار.
اما توی حالت max: تمام ۱۲۸ هزار توکن خروجی کاملا خرجِ فکر کردن شد، ۱.۲۸ دلار سوخت، و SVG‌ای هم در نیومد.
گاهی سطح Effort/Reasoning بیشتر، فقط یعنی «شکست» با هزینه‌ی بیشتر.
پس الکی درجه‌ی Effort رو بالا نذارید. برای مدلهایی مثل sonnet، همون High-medium کافیه واقعا
🔗
‌
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5419" target="_blank">📅 12:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DJ7NLLC-7rShOagXT35-nbE5VKFe8IPhp8qT09CF6TL2fBWtVANFEW22Vs544bTUTmMNdfcE18txp2f-CIGscb9Aklj7EqPxtK1wvKI7427yNjJWVeZ6sCDrF-zvVbySHUIOHQrZlzHQMYvVRTG8Zu7lvA_ygibJLZmo1yY9Z8opmvr1LEZh_v2idNBOQGMbHUJ2W04Il8PpBoFjT8kHTRlSk4bv7Iz-n2EUbeQj18VK4pRIX25RwmLh6Igd85FPNv3d2jGqoerB-GC7YP7-CnjpvStGKrW9w7MbNPYdjD7MPYhi8g6unthrcD0b2M6k-aRURQHGoHUAIa50kGzJTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J1gBF_arhKeYQ9Ef_tvHK2ugyVFkqGS9OUv6NuPAd-1TTsszwz6SOjL_yex-5JwVNo7ZiZ_uNO6T8-oPd6SE7R5UTMNY_inIX4-F3P1zKDXfj6jpgTuIPqY5TdzOmezSjgpWe8LIe9V2O0XDVlNy2gMlWEMN_G8RJ9jWVB9pYKbpROid9YfPqJ5CP4RbXcF8cRpq9TGBkMydHmw59xGQi4KYVs89FDjC7tYQN8YEx3CjREjTcb7VZgxDJSZm5wefJq4ho_DcyUzLh-JhylX7I2Fkj5WlPw1X3LcaY0mgdJImrdxbESSangpJanJAzySKmScW6m84h4OwnO77rtDliQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این نسخه از WhiteVPN می‌تونید مشکل فیلترینگ ورکر رو دور بزنید</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5417" target="_blank">📅 10:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5414">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5414" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/W-YXC6f-1KX0dxaddfPf6EXcyTojlh83aGlK6fosHaA2eKdTeRF5nq5oZ6XXvGZdFd5zaJZjQhJOD7Slaq8SXNSvPTgEAec7TDyV_7sIdzXzYBpAj8bpr4v576Ug8EzbpI0L-mSygFNyNAaj1lBJ4LYUk9IqC6uGCUNZsx8YSi5ObWvQzgn261yh0B_dn7ivpLvS7KUqeqnTZYVY4XwOS10Mb8QOi6CSSMoqptDZrvXcaxKbCSIrIsOnUQgczm7oXlCKRDr_B6dhxorjy44EwCMvsZAZq9jL77b89SS9pCy3tK7JfA7U4gI0NKgQNr3OxT5MLFKPVJ8sxgHH9Z-lJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید WhiteVPN منتشر شد (نسخه 1.6.10)
در این نسخه، مشکل نمایش وضعیت «متصل» در شرایطی که ترافیک در شبکه‌های دارای فیلترینگ شدید از تونل عبور نمی‌کرد، به‌طور کامل برطرف شده است.
تغییرات و بهبودهای این نسخه:
تأیید واقعی اتصال:
وضعیت اتصال تنها پس از تأیید نهایی دسترسی به اینترنت آزاد و پایدار ثبت می‌شود.
سوئیچ خودکار هوشمند:
در صورتی که سرور تنها پراکسی محلی ایجاد کند اما دسترسی واقعی به اینترنت نداشته باشد، برنامه بدون وقفه به سرور پایدار بعدی سوئیچ می‌کند.
بازیابی خودکار اتصال:
بررسی‌های ناموفق مداوم پس از اتصال، مستقیماً وارد چرخه بازیابی و اتصال مجدد خودکار می‌شوند.
ثبات سیستم امنیتی:
حفظ و پایداری رفتارهای قبلی در بازیابی آفلاین و مدیریت خطاهای گواهی (Certificate).
افزایش امنیت اشتراک:
الزام و اعتبارسنجی دقیق لینک‌های اشتراک خصوصی در بیلد‌های رسمی برنامه.
📥
هم‌اکنون می‌توانید نسخه 1.6.10 را دانلود یا به‌روزرسانی کنید.
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🆔
@Whitedns</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5413" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i1IvYyB_xLnFR1I7cBZwnseQrDFcT4-VHwsjzJg27GOP8xcs6bQHy8mkqx4oxsV-PfDKd4BOsQ_6VKJ8jiAtGTTKp1jwZ-w8Ab8xwVSRsMjlDQe-Wc3BwvY2tBYnAQqmWtBN4FbjSaAPBFCey6KxnggSmHWiVmwQkzymnsIggrPG6OM--qzbX5Dc0-ys7kZBvpEG9aKK-ZTjvLJVVP0mPHVwkocdPcaA-hPH3V6jmQlfa-NqQbqxVvULBx_LxYtOR1MoSVNNLNv27usv4NX4xBV6WFV-v-FChOpGsJbai1FKUwrYQPtR5Kx5EhKNI5bKDyf5fuBwXpSyOOjrosHuJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10
اسکیل برتر OpenCode
جامعه کاربری OpenCode فهرستی از ۱۰ ریپوی برتر Skillها برای ایجنت‌های کدنویسی جمع کردن که شامل پکیج‌های اتوماسیون تست، دیباگ خودکار و سینک شدن با دیتابیس که کار روزمره دولوپرها رو خیلی سریع‌تر و روون‌تر می‌کنه.
(حواستون به SuperPowers باشه که خیلی توکن می‌بره)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5412" target="_blank">📅 07:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">Matin SenPai
pinned «
اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید: https://youtu.be/dQKfkXnThCE  به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5411" target="_blank">📅 03:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i-cWKhYzWr-6FEvy__muw6P9T6fpKp6yMGZZlVU4IKnYe91y7tAfOU96c6OUOSj8CLBWxeVnWgf0sHIlrqCPPQEO7209IlNboWKMBDHtlQpbsINktHKa7imtrLfMSBZwygGmekyuPvk2-ghvaKQlYmreip8OkhoYCXV0FdJdyO-2aL02SpPWLhAiGHtCxRSvhddQ7ixjI_I7farY3Kei5WCFR_HcvyHIomik2ukhhw8OY8j0LCxRxK1CSDyRcIV25m7Fn6C8EaGboohyuVQEvvSqtX4SSv9hD1LnZtp0jRXIqsoMoiy2WfdM0fYHrd0-1qDzbKQecATFjjVRjTmZpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5410" target="_blank">📅 03:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jcIu4zKH1sQZmdDnYdLpIVk-lCDXr6pLZpv8yl7cOs7xNz0_4oPsgNACkBW9d_VoVqwSm5g_9psULR23Hc33aCwMPjwJQhrRNad3mrua0Xrcjv8Ker4Lj_wAiwrlqHSfeJc3IS8zt_ZeiRJG36MN5WYJZ-OA3Bi9MSGRgN86Jp0-Cm_1d2HYa0s_RaI7audR-R0jfa4FSpIOCRA5oLMFnQSFOfyUDSKzN6GfquvPzYy-5DfLZPo26h0wCyBvbuVEI8aRMwB4A45Dpsvv68WTQquenPaeMHhayWPn83qEkZGn74fNpvZhXUyKbU5RvCcMSUXg4x9wkTP_FsULUopwqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5409" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هرمس خوبیش اینه که سمجه. اگر از ترکیب هرمس + مدل رایگان(مثل mimo) استفاده کنید، واقعا غصه‌ی توکن سوزی یا انجام کارهای سختتون رو ندارید</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5408" target="_blank">📅 23:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مدل Claude Sonnet 5.5 معرفی شد. هم قیمت با GPT-6 Sol، اما به شدت قدرتمندتر! نزدیک به Opus 5.5  • $2/M input • $10/M output • $0.20/M cache reads 1M context + 128K max output
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5407" target="_blank">📅 23:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VWnQoYhdLuNrcsUMAwQjFR_uX2jKcpLd8DIM9KJjiHasuqapOvyneILBsA6Y0D866zxIDA-nEuhL2cGZJph8ADuwu9Gh6WmKQCBlZvMXXHWrxx6EoH3l6MiPJwEF04TPFVq3fvtklLqTVHW2ZRcrgjCVSLF-NsJSSDbFoFHNxVy-IYLGQabF6eUCzCqMbV9V3DbaxuW1IaOtcpDks9qTbi3OWiTIj4Wk3s6JI0O5mJYch4A7S4o0FQRSlYxN7Ghl3vvdG9-kL6IQZmkTJIym4l5G4hdwU27hGl-p2j7CFArisazy1IydRmrggEPrNmzGHEu7En2co4XI_B4VM28AYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Sd2VX1pnWQIH6uOTIXvEt2ZVNibkethMxkXLQQL2Slxql53hSCyE20ThP0v_fPRQXRgBVUqtDBdV2qgJIvrRfupHHf2AjGVvcAc-rquChtbtHjtudxAO42JsecEjC52uUj1NVFwrgeGdHU5YKKMtwJfmVYDI4fa5FnNSODRDNkcYtVrW8hNIwMcU3nh_OpkM5bxQdTotPXtvHaSYQBQmgLfeM3SeVGCckcN-fmdXRTh_rqCctRbmQiqrWDnkR4IEMJamFrl2b71ZfZuRl1VRTr9cPUp9dIyHfY2z4lJ6MpZr6cJNdA5O49D7micWirLkFyghdf-4KEEJ1zdGZ_GWuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5405" target="_blank">📅 22:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5  از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.  هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید. https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5404" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82410567b8.mp4?token=USRpnJ_DTQ6muXOTi-rdMs4vKyy_JMnIxsFzqXdaFV_t6ssw3OH9yPKGKy_1z7EXn40jJrrcMzTj9vl8G9KJu-XqdRWR4dkkZwv72NUMwlIBz3adskhaDdxmBSyQpw8H9n1SqW3rpB_E2sidbBJ2yHb1NloxaZMm6QMW18NxLXz0by034G6AiDdQtOWiVmMe_7dKM4ys5Ie1ExA_NgjOBnmVvXCoAAX7wml5glLyvXC5BKcZ4eNPJYAUK4YfLYnXzKClLzerbTQejY0XncVLYkymrkHl1fWghmntv2vzr9lV_Fd2KFUQiUPgARcAf_vmuCs0iaCnNXPIYvXHHSiD3A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82410567b8.mp4?token=USRpnJ_DTQ6muXOTi-rdMs4vKyy_JMnIxsFzqXdaFV_t6ssw3OH9yPKGKy_1z7EXn40jJrrcMzTj9vl8G9KJu-XqdRWR4dkkZwv72NUMwlIBz3adskhaDdxmBSyQpw8H9n1SqW3rpB_E2sidbBJ2yHb1NloxaZMm6QMW18NxLXz0by034G6AiDdQtOWiVmMe_7dKM4ys5Ie1ExA_NgjOBnmVvXCoAAX7wml5glLyvXC5BKcZ4eNPJYAUK4YfLYnXzKClLzerbTQejY0XncVLYkymrkHl1fWghmntv2vzr9lV_Fd2KFUQiUPgARcAf_vmuCs0iaCnNXPIYvXHHSiD3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5
از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.
هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید.
https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5403" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید:
https://youtu.be/dQKfkXnThCE
به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5402" target="_blank">📅 19:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Au_-8yUiBcfciDm3n_9gCHbuLTrn-5u8V3XWjRJIyQNT7NrRr1MAzFVPaGe6TnImhjLWTIZSVPpPnJWsU24iQgmndBkUx26VVZ2gIU6zqTRQVblF0-8SEjskR-BNSgfqfJmeSTweJBhPQe_sAH40j3B0SBUO-DOKMBURuMXvEyv7IxH-LzSGKB-03iXurwXvZT0Vs00C3fgzEg5MVM4O0KAz23ZzJ740SUgQMVCuHahlPEhvQmx6GSUYlDo1W9CA2gEMeXgiegxkMjMFkYlVMq73pEeaXfS8xwMAZjP7ly73W5bkWeCJH-Khv3R2f_aEms0tRehxEY2EuxSwLTdGFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه‌ی Hermes: از
MEMORY.md
متنی تا گراف دانش
نویسنده این پست ردیت گفته بودش که مثل خیلی‌ها به دیوار
MEMORY.md
دو هزار و دویست کاراکتری خورده بود (۹۹٪ پر و مدام درگیر نوشته‌های کهنه‌ی توی کانتکست). پس برای همین تصمیم گرفت plugin مربوط به ارائه‌دهنده‌ی حافظه‌ی Hindsight رو توی یه کانتینر Docker جدا راه بندازه؛ بعد از کلی تنظیمات مختلف، اولین اجرا و تجمیع گراف تموم شد.
که این باعث میشه:
1- دیگه محدودیت
Memory.md
رو نداشته باشیم
2- سرعت خوندن از حافظه وحشتناک بالا بره
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5401" target="_blank">📅 19:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oHAxInQe9mP77XZ79b40PpjoJWC207270vXbemOu5yICjFpsNwf_XJZFHr6cyaopZCZUkJFgwI10ipdhmRfHHnaMz5YlRxmJ_801SMCbveuITV6mkzyI3ghyMdn6aCKK2i9LlL4Eq6FN5aDi-XOQEGsLyvkRH7u_NHwBaxEgto0g8U-9jOti6i1ADebzhQ-DG7dcof9umnW25wqgaNZ120Ww9aw-zpr1YbylidPiQ8LWss-qvuvu6gIJgjmSPwTkfgiNI5qnXg_wWAwhHVNeCyhWK0uOGxhyiH2dCqCcOEOjf8pRRC-bB6kI-f4NvZ-G5yaRVNdIXoQ92XM1Im_fXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر کنم گوگل چند صد میلیارد توکن از نسخه 4.6 ساننت و اوپوس خریده برای Antigravity و نمیدونه باید باهاش چیکار کنه
😂
مشتی 5.5 اومد 6 هم به زودی میاد ولمون کن دیگه</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5400" target="_blank">📅 18:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eLdLTpOk5lsSnuCBf5cjxXjpPHt4OYjO4_3UXUe_4-VP_h68BJkCR0lAWHvHI8t7GsN_FMK9ebillrsTgHc_2weAf57AsfwCuJxhTQAwq5c6toyczy_gxl0652bNb69lodu6j8sHB2sZKs1AdnlvWMSjreXdRERWgFfBVZ33E4HFgqhtKbmJCd3yUM6YFy7UitAMW5CwO_7yYab62-H5AydSLyqcn4ZHchT6E_kAppVXCOSBdQSw3abpJ0eyq--URZHhMj2uNbWGU4_42vrseCTWuUePGZOMsZmxeyAmOJ806sOwXgGIvZ1y_p5c5sdiZIudDV-j3ku5wiPvsXj0og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی ساخت نرم‌افزار رو آسون کرد، دیده شدن رو سخت‌تر
قبل از AI برای ساختن به توسعه‌دهنده نیاز بود؛ حالا آدم‌های بیشتری همون چیز رو راحت می‌سازن. ولی تعداد کسایی که حاضرن پول بدن، یهو چند برابر نشده. نتیجه: وقتی ساختن برای همه ارزون می‌شه، مزیت واقعی از ساختن می‌ره سمت توزیع، ایده و شناخت مشتری.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5399" target="_blank">📅 17:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NKj9NdtWb3Ga-yTiapuFdzZN3ZqXISH8BRlHNzUSZPJ_aCDNcjeb90HthPcYlz538XnmElvdR7WpBlwGRh4cEsNOBZURQLiziWXTnPDft0zZhZVktLElWg8LFMEPs_RVZrv87hPfv_2Qo2M33lCxb8DFMJ5Dgl0eqcjjrzVErqWssDp4udDAhrX2GOv_8bGSOYkH44eeitySc6-GX9tqNEs2mMmz7QaEaOfS5I44a002zRo_qR_8vo4aGXLceH4uJ_veS3gbqFVb3-ed8m7hwziv915pk5kabyzcMcsl3e8ZqIaCjiiqwabaFD4sPEYo7BhKbxV15kObc9GB40l_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Wb2u2M3HOyEsvIYTCQ1NPQsOhnZOBd3eFxFJGGmft1bXBdty_oGWCTnXfrrjON_W98Zy2972YXM3gfzW0V7MkbaD5261pp4cg4XMsz27QIWgbYSi3gCxGt2I5Bpq4sFctJtySHf43BO0mc7K_rtU4yEXj-Sa1NuaKHEtVDX0DlSGPlGwHEaNweU0iZv5AIfOnqy9kBCuMzi-TgujguL_fhnaTevvwLWiMFdpv86z-dfvMTaMusjCh--JN4-5pXmdg0pkqZr5ig-MQxxLW7n8Ed6-L1bQRMjAJCFXXtFPvAHSYHkUWpQOfyaFhsiksXOlxlk4aw3k1aU467m5kTAwQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این فتوشاپ اوپن سورس که مسخره‌اش کردن یه دوره، سازندش اومد توی ردیت درآمدشو از دونیت‌هاش گذاشت و گفت محصولم خیلی پرطرفدار شده
😂
لینک این فتوشاپ اوپن سورس که اسمش Photon هست:
https://tenzen.studio/photon
لینک پست ردیت:
https://www.reddit.com/r/SaaS/comments/1wsac6d/i_replaced_adobe_photoshop_with_a_free_better/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5397" target="_blank">📅 17:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست
با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5396" target="_blank">📅 16:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">محدودیت آپلود
۶
پکت رو دوباره دارن اعمال میکنن.
از چند روز پیش برخی سرورهای شخصی دچار این محدودیت شدن.
از دیشب وبسوکتِ (alpn/1.1) کلودفلر هم برای برخی دامنه ها مثل
workers.dev
.* دچار همین محدودیت ۶ پکت شده.
در نتیجه کانفیگ‌های ورکر کلودفلر به صورت عادی در دسترس نیستند.
با ech ,
fragment+fingerprint
و چندین روش دیگه میشه این محدودیت رو بر روی کلودفلر دور زد.
فعلا تغییری در وضعیت warp هم مشاهده نشده.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/MatinSenPaii/5395" target="_blank">📅 16:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xs9KTJM1i_-nGOpPVMhVcqkduUTDfSXeUIihgyuOgjmhssClqOoviDkUU92XwZSzRK52cepZ4WijjnYmsM-nom-OYqgN-FOPjlOrrtrsF4jg8QNTkc9Seb9WXmA116Q9ZqJzbB-CSqjhZo2_fCqubt7_sMy4heLOYFPMIFz2SNtfia9CKc0sTKzISgTyo8zSa9Q-KhRnzd5LR8dP0aHtfAevjFTPHUXWnH4UTyeUsm5v-30lB_kyR0FbRwOtRgyTZ_tL3Rp7spK6uTgB0lsPScBcbNKGby82mTRuDQZchteftabRQMZHL33K--7PnCDv_DfqdWJJtidjy8zILIwKPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5394" target="_blank">📅 15:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ggiEKinnoErv3QR-QMlQOdm7-t-iPnWIZJR9Kq_Bxnfageha5iTaaQoRDeBlEVzxZcMfA1QBdqPdlUx-1szrp5TZbD7A505Hazfyj2rar5w0JBTjgGPKDCj-Tp1Wk559UrnFA-3bVgqmOzuSAcNqC1th0sOmHtSfDtwv6FhCcdYqBATQlm_FIF0qUY_HGBQ65Vsqg8zeWi_XQIAE0TEo4WCv9a4Z_Tuf5Hrtprbbhc36dUZf6lx3jIpa8YAMnicD849n9taqooLRX5ZN1qEkq8b-2lNzAqIOlBXAA3d32_LBvo50jNe5btrDXwRGP4jjYe2e1CtlcbeJ88AOP4J_8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک خسته‌کننده نمی‌خواید؟ بشینید جنگ مدلها رو ببینید
🤣
سایت TinyAIArena یه صفحه‌ی ۸×۸ هست که چهار مدل توش دارن واقعی با هم می‌جنگن؛ نه یه جدول امتیاز خشک و خالی. روی هر مچ کلیک کنی می‌تونی تماشاشون کنی و ببینی بالاخره کدوم‌شون باهوش‌تره. کل پروژه هم روی GitHub عمومیه. البته این صرفا سرگرمیه و جدی نیست، اما همچنان برای دیدن اینکه مدل‌ها توی یه محیط محدود چیکار می‌کنن بامزست.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5393" target="_blank">📅 07:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">قضیه‌ی «انسان در حلقه» خودش داره از دور خارج میشه
مارگارت مچل و همکاراش توی یه مقاله استدلال می‌کنن که راه‌حل «انسان رو نگه داریم وسط کار» توی عصر AI، اون‌قدرها هم ساده نیست:
هم طراحی فعلی ایجنت‌ها نظارت مؤثر رو سخت می‌کنه، هم استفاده‌ی طولانی مدت از همین ابزارها، توانایی‌های شناختی خودِ ناظر انسانی رو هم کم‌کم از کار می‌اندازه. پیشنهادشون اینه که نیازهای ناظر رو به‌اندازه‌ی توانایی خودِ ایجنت جدی بگیریم؛ تا هم توی طراحی محصول و هم قضاوت انتقادی تمرین کنه، و هم توی سازمان‌ها با پروتکل‌هایی که اثر اتوماسیون رو جبران کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5392" target="_blank">📅 23:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5391" target="_blank">📅 23:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سندباکس‌های ابری Docker برای ایجنت‌های کدنویسی
داکر سرویس Cloud Sandboxes رو منتشر کرده: محیط‌های اجرای امن و میزبانی‌شده روی زیرساخت خودش، با ایزوله‌سازی microVM توی سطح سخت‌افزار. با یه دستور میشه سندباکس رو بین لپ‌تاپ و سرور جابه‌جا کنیم طوری که فایل‌سیستمش هم منتقل بشه؛ یعنی کار رو محلی شروع کنیم و قبل از خاموش کردن لپ‌تاپ بسپاریمش به کلود. هدف، ایجنت‌هاییه که ساعت‌ها کار می‌کنن و می‌خوایم چندتاشون موازی پیش برن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5390" target="_blank">📅 22:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5389" target="_blank">📅 16:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3vl2lVJaKwrtwiwV_DmK7sLwfySsrm1HnLOQ2ik771RgMRlf_BJlUXktos4-XNaIktTiLWtCRSfW0IcoRUEdaxv5K932Cgt2lCD8_a4bIFeSk4kJ8VuRYUQ-C8JWZRZq2InwbM0JY2Ypu2Nuwuhf8aYrGQvKW6KOnAQVfJkAHMtkxJfpfU_o6NeNYVlKjAAqtYZzmDbw2svElnYwijmZbCPrEgUeQqpqvCf-t_DQaiDqj8iQWOwzTimDHnELXZBJzPj_gh7T9SGT8wJq1xg0ZbTENC02OxlBltB5cV2lsHuJl6aNV7PTlhXTr91OAh9TKxQ6awvCv6j1sxkEp3P9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر بلاگش رو از WordPress کوچ داد به EmDash
کلودفلر جزئیات کوچ دادن بلاگ اصلی‌ش از WordPress به EmDash — سیستم مدیریت محتوای متن‌بازی که خودش داخلی ساخته — رو منتشر کرده. EmDash با TypeScript نوشته شده، روی Worker خود کلودفلر اجرا می‌شه و تا ۷۰۰۰ درخواست در ثانیه تست شده، در حالی که بلاگ معمولا ۷۵ درخواست در ثانیه داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5388" target="_blank">📅 15:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vim1RMvDRJkrLKhtYxeTRg3gK60gNVQjxLpVWDNDP_PKsJQ3ARaUKvUfFNhjdA5RPzza0sanltkoD7x2iJPWKNb_LmG2bAw_cGsme5JKH5vXWl10ueVQJFpz62ETYR82qnL7Tv8vlN7eDy_nRk2FXEZI1pWXHSvUZEn3YMW2iPvSArsWrw9iuOXkvCUIcIne95A4Mr302YtnMwMMzHJqbxxkJGn28BSJNM50sJeIBVYVZIU3c08JVfCi3p8BXw6nTR60Ua4GQXFH3pjrTciMLWi82uLsBQhXTsdVzD3UXbfOV1JLTdDZZ5_2bUJo2qCsDnizUFYcOTmPEBwGkJZxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا حس می‌کنیم هر مدل جدیدی که میاد، انقدر از مدل‌های قدیمی قدرتمندتره؟
باید بگم که این بیشتر از منطقی بودن، «کلک» شرکت‌هاست برای مارکتینگ
اگه یادتون باشه، 2 هفته پیش همه‌ی این بنچمارک‌ها(خصوصا سه بعدی) جوری از GPT Astra تعریف می‌کردن و چیزای خفن می‌ساختن که انگار خدای همه‌ی مدل‌هاست.
بعد که Claude Opus 5.5 اومد، خروجی‌هاش رو جوری نشون دادن انگار اون مقابلش پیامبره.
حالا این قضیه برای هر دوی اونا در مورد Gemini 4 Pro داره تکرار می‌شه
به این کار اکانت‌های بنچمارک و Ai Enthusiast ، قضیه‌ی Strawman Fallacy می‌گن. یعنی مغالطه‌ی آدمکِ پوشالی
توی فلسفه، Strawman fallacy یعنی از رقیب قدرتمندت، یه فرض پوشالی بسازی جلوی مخاطب، شکستش بدی، و بعد خودت رو پیروز جلوه بدی
هم خود کمپانی‌ها، هزینه می‌کنن که اکانت‌های توییتری/ردیتی این کار رو انجام بدن؛ هم خود آدما خیلی وقتا این کارو سر هایپ و ... انجام می‌دن.
چه شکلی انجام می‌شه؟
1- مدل رقیب با پرامپت ساده یا بد تست می‌شه، ولی مدل خودشون با پرامپت بهینه‌شده.
2- قابلیت‌های رقیب مثل reasoning، ابزارها یا context بلند خاموش می‌شه.
3- هایپرپارامترهای رقیب به درستی تنظیم نمی‌شه ولی مال خودشون با دقت tune می‌شه.
این شکلیه که می‌گم هیچوقت به بنچمارک‌های این شکلی توییتری، نمی‌شه اعتماد کرد.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5387" target="_blank">📅 14:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGX3tq-czVTnz5nGb4USWrtDUapr_NjjuSbYBNEZ4fsvbR8vWlWczlNi1-7JT0ImZR79q0w4APsDffpi-fkSWyYpPHWWy2huFkwTU6CQD3ZiTdhVT6_3XrlwATZTwiLS5ehYAInVul1aR9vN2Y-hsZnjKAA6ifDwWixS_pK41j3t1pehprw_IYPjCl3lDhvdtqetR5cG8CdPx6BDX_ktKfOOUt0cbGw6YL8y0WbjI7eqy8RiaEP_J8v4XseuUlgpu_0d5VYh5M7_H2pKPtCoUzBDk1NLFIqZYZNBGuypEqB1i1Xfz6IJDVvqjHHcSRMR1s6HWpDTi7WqOjm8nyXSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ هزار دیتابیس Supabase داده‌های مردم رو لو داده
پژوهش شرکت UpGuard نشون داده حدود ۱۶ هزار دیتابیس میزبانی‌شده روی Supabase بخشی از داده‌های شخصی‌شون رو عمومی کرده: اسم، آدرس، شماره تلفن و گاهی پسورد و توکن.
و بین اینها دیتابیس یه کنسولگری دولتی توی فرانسه هست، پلاک هزاران خودروی یه پارکینگ، و دیتابیسی که برای دریافت رمز یک‌بارمصرف کلاهبرداری استفاده می‌شده. Supabase که امسال به ارزش ۱۰ میلیارد دلار رسیده می‌گه پروژه‌ها پیش‌فرض امنن و امنیت یه مسئولیت مشترکه.
بخشی از ماجرا هم کدهای Vibe Code شده هستن که بدون پیکربندی درست، داده‌های کاربر رو  لو دادن(شبیه یه بنده خدایی که یه بار پروژه اوپن سورس گذاشته بود با به به و چه چه و بعد دیدیم apiهاش توی کد فلاترش هاردکد شده. (طرف مخالف سرسخت ai بود و میگفت به کد ai نمیشه اعتماد کرد)).
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5386" target="_blank">📅 11:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=SmOVbkmS9GlX9aw2WheAyZQhq8-CSPngxe7S0KfAP4peO1jZYUSNPUgBH--M6tkTNlIuHg16DvjhMLOwJuJfPWxHLj7ePDggJ1MKWEncgJK_H_ZDzEV99qzDQJ8oO2RAY2uIMApXMgk8PBi7jxbI31D7kVca0V5Vhet2s7gEA8ajWsQbhS5qVCzBXv9B77X5jGIj_X4bamnFS1nB6k6SUBVblFM7Q0lf8thsfGzCOlDppCDO0RP63FhnWcQn33QCPRLckmVuyqYZ71HElYU9nOp1N3QtTx1S93lEl289mdqHIXgftvoHOdsX42lhHxCenCmZJ6mW6Exvx7e1Xxcgh2-EojnkbmL9SzNrgl6b83o9PoQV0EYdFTgehM05x26jR_Jjj6_TgSbwBNf6fLbLthHlkhpoUicxxdJ5JcUA2ztnJfDRMFNdoo5WztI2rC9yz7LshcAXIDCGuTjS5TUsQQHBctoP9gz-mBet3n1udCKWQ2hN26dcqxuJ3M8awmqas-QOzxjjKYlak53bNWQlmTZeAdCkvwyXTqzhgrRslrAR-O5TRJukvDOAuIBKWPjM6dS-gADuZiY0QVFPdjeWklipBRFJ1iFTS8VCHR9O9ipc6X7tdZA0TlgfmDyG_9QHJspL8p_CgiJyz9LnAD9O8-b6iJdFiOUssIGmPDWoD7s" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=SmOVbkmS9GlX9aw2WheAyZQhq8-CSPngxe7S0KfAP4peO1jZYUSNPUgBH--M6tkTNlIuHg16DvjhMLOwJuJfPWxHLj7ePDggJ1MKWEncgJK_H_ZDzEV99qzDQJ8oO2RAY2uIMApXMgk8PBi7jxbI31D7kVca0V5Vhet2s7gEA8ajWsQbhS5qVCzBXv9B77X5jGIj_X4bamnFS1nB6k6SUBVblFM7Q0lf8thsfGzCOlDppCDO0RP63FhnWcQn33QCPRLckmVuyqYZ71HElYU9nOp1N3QtTx1S93lEl289mdqHIXgftvoHOdsX42lhHxCenCmZJ6mW6Exvx7e1Xxcgh2-EojnkbmL9SzNrgl6b83o9PoQV0EYdFTgehM05x26jR_Jjj6_TgSbwBNf6fLbLthHlkhpoUicxxdJ5JcUA2ztnJfDRMFNdoo5WztI2rC9yz7LshcAXIDCGuTjS5TUsQQHBctoP9gz-mBet3n1udCKWQ2hN26dcqxuJ3M8awmqas-QOzxjjKYlak53bNWQlmTZeAdCkvwyXTqzhgrRslrAR-O5TRJukvDOAuIBKWPjM6dS-gADuZiY0QVFPdjeWklipBRFJ1iFTS8VCHR9O9ipc6X7tdZA0TlgfmDyG_9QHJspL8p_CgiJyz9LnAD9O8-b6iJdFiOUssIGmPDWoD7s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه. - عاااااشقش شدممم. با کدوم ابزار ساختیش؟ + الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5385" target="_blank">📅 09:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xgbr18cXXneSbzFXrDjBo-rA3iAeim0R7cjNBGwzeaXMB1QZk2l6kGUvcvzPUtZyTa_K1_vTneacfsal9cQaMtW6Y7RFqKxWkYEXDVpnaM1Z3c-XZ_pPqQuuuhNWKNi-74vXLIL37dAXEm9FoX6bvtBcLLw0qD_QqJHSBT6tFVT_R0Zs8-54JgsBegdulHGlyeJ-HDI2C9zq_c3AD7BQq0IA9TIGzfkXg5cZhL5_LIBLwWP3RfqrAF9gXPc3sjmogvI7UBDJ5yhDwxp82ugmBwBBcvHLkx9HYZxR9tr9ng0qNfRsjoSUVoy-VDDBXq1xzO1CeKG6tawBhnqvQHMp8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه.
- عاااااشقش شدممم. با کدوم ابزار ساختیش؟
+ الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5384" target="_blank">📅 09:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSRfs4wDfI4Z7MZXykSme9Mri82MtMOmbHsguGStaqYeU4I45b4sBXJXq8JtcL5P8U7TwMf02nADzLJZ3uqI-AiAhj0Pg6VrLetJbuJ1-9aJW_ZgTssovPcTXQ7kn7QhRjBd7TdW8Ldy5hoO7Ll1WR3jxB8dLl0Ib5HC4J862EGkyxkL6xTdRUagAqwOQCoqu07s27iK-sb5mFrIIOFIhTr01XBfCGPjFWjPXX7pT93BAMIGlEzDv6vICdDjF3dqGVJ1onYm7XDB6PkjvxxaPkRZzvHgsPfO9aCphT_FqRqs0ltL_r2KMFsBNAa6YjbIT8gMPXEgkuO5NEBcES6HxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولایا (Ollaya)؛ مثل Ollama ولی برای مدل‌های تصمیم‌گیری
خود Ollama، اپلیکیشنیه برای اجرای مدل‌های Open Weight روی سیستم خودتون. حالا Ollaya، همون Decision Models که Jev ساخته رو می‌خواد لوکال و متن‌باز اجرا کنه: سوال تایپ‌شده از هر متن یا JSON میدی و جواب کالیبره‌شده رو توی چند میلی‌ثانیه می‌گیری. جواب از یه پاس روبه‌جلو میاد، نه از تولید توکن‌به‌توکن: حدود ۸ تا ۱۰ میلی‌ثانیه برای ۵ تا سؤال روی RTX 4090، در برابر ۲۳۶ تا ۲۷۶ میلی‌ثانیه‌ی API عمومی Jev. با API سازگار با TypeSafe کار می‌کنه، پس SDK رسمیش بدون تغییر وصل می‌شه و مدل‌ها هم همونطور که گفتم، open-weight هستن.
اما یه بحثی که وجود داره، API خود Jev انقدر ارزونه که فعلا من با اینهمه کار باهاش 5 دلارمو هنوز تموم نکردم. لوکال اجرا کردن لایا هم خوبه اما شاید بهترین گزینه نباشه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5383" target="_blank">📅 07:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ScB1cIbm68joppZUOc6jHKLvseqgXnMTQolAr-rgogaWLBegv7qlzQ4-5aBnslPJ9xkDJKAK7O9n5P1v-S6BckmUA6CHOAsTinXpkQwvnl8jkHmh3tvA79B0NADo-XPFS9C5-XCYYfwrqTvMissq-c86Hn6yjI91ygBZNKF1B2-DS05MHBBytGtaFN5sOYbs1DMpphtd-FxFHlz1TTABdl2fGll4PAx0vb8su_pZUSRqx0NJAAAhGqnr9Ab13wiD9CoJMkeOCkvH12nRcJTHy4GWZCnG9vBYy9wdFmbcj0QGpZ8FuvHxNH5TT7qXYu3Uj5bu0Ug_ZeoNnmJsq_M0Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک هست دوستان.
گوگل یهو ایران رو تحریم نکرد. سالهاست ما تحریمیم
گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده
این خبر هم اشتباهه
می‌تونید ایمیل بسازید همین الان با گوشیتون و نگران نباشید</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/MatinSenPaii/5382" target="_blank">📅 00:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تانل با دو سه تا یوزر و سرور قوی هر 40 ثانیه یه بار ریست میشه
معلوم نیست دارن چیکار میکنن
کلودفلر هم اکثرا کار نمیکنه واسم آیپیا با نت همراه. فیبر وضعیتش بهتره</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5381" target="_blank">📅 00:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وضعیت اینترنت خیلی افتضاح شده
هم نت هم VPNهای تانل</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5380" target="_blank">📅 00:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAREX9ceuXqlZ5wM9S-aa8vGvaHmBA4BJDAx9QK5UDVjOmb2vU61htfuNg0jU9lqZ0VlJjntf9iCoXwLB6NUXnyuy3aC8jmhmFrKhH97JqbipVAi97y_HCBISv9XV-g6FH1V9aQQD-qFqhjF7jbo-sahXgUrhE6lz4SvphjPfUSPR5gKgRFN8RUq7Tw0Le5e2RZWac3TaVaV9Ow59Y4Q3MLoXt-A5W9P2zEhaao71HIAc5wQumWDPkYQOKa4YCMqlO7ZTN51NDvnaJw5oTxjERNqKP92lyDhfCpDIG-QhgzMgKRaSpHUPuZ-2-mCAMR8TOV5OxG-qPGq11g9Evyoow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابطی رو که توصیف می‌کنید، ایجنت براتون می‌سازتش
گیت‌هاب توی اپ Copilot یه قابلیت به اسم canvases گذاشته: به زبان ساده توصیف می‌کنی چه رابطی می‌خوای و ایجنت یه سطح زنده برات می‌سازه که هم خودت می‌تونی استفاده‌اش کنی و آپدیتش کنی، هم خود ایجنت. هدفش اینه که وقت کمتری رو صرف تطبیق‌دادن با ابزارها بکنی و بیشتر کارت رو پیش ببری.
این کارا فایده نداره گیتهاب جان. پلن‌هات گرون و به درد نخورن
برو این دام بر مرغی دگر نِه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5379" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cmGlWnSmGCYGOZcfohrisUAkp5u9Jil-nJXCTHIDlpHYJsj86uPSsEcEI7x1BjxWp59csl5WPI12UKkvRBzbSSnNW7AHAs9MrG8B9eeH8NQQUzk6xtYuF5Gnl5oFCWO999WmUEuetJkeqXmYYZqkOQgUY4JJ9TcvU_iULW7jQIwf0dAzardAP5VOolZO9MJnRCzJQoc61y22aYIWtUayPkZlAgvBiw4W2JMcIwvMyDON_cuLQpNLIO1BzA0fzO7O1cq31j0lNaUtHTT1jPqh5IpPT4u1ShoRMkHn0POBT1JKOBJ44iqPCc9DNr1H45SJIXUaZf1yJXo6i9THAufuXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">(باید برم ببینم کپچا فارمش چطوری کار میکنه)</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5378" target="_blank">📅 23:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RLHZZa44FLJjM1Ks_T8MLGD6Vd4Q8AV9J_ZolfPXg2u_LfYxvccfVq16E2xdV9ZqH8AvXYxwMUOfku2IDlJycP4EcGLtpqqgGUg7gkkInLzuwawGrzNPOkQrZNHkAU8Q7mmfiPjcMxwmzXDL7j3WVC09qADawrDsrjAjCNT-7PfBNGNVLhVJHI2NZ7OUMVOYepxqPAjoTJXNiNpccuEwA1QREXBOrpv4AmCL2MaY5O1hxgreLRF33rA2lvIiwAaF_0QPamgHpnn-rtuiBvo36WrqVtDXCKenaHJ-GnA686ein2GfabJH77i4Nh5sXRXKgXV7FYDro7NmlSepCyGeKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر سایتی رو برای ایجنت‌ها به API تبدیل کن، بدون Browser Automation
💪
یکی از توسعه‌دهنده‌ها توی ساب ردیت هرمس ابزاری به اسم
agent-data.dev
معرفی کرده که ایده‌ی جالبی پشتشه.
حرف اصلیش اینه که برای خیلی از کارهای تکراری وب، مثل چک کردن قیمت پرواز هر روز صبح، دنبال کردن آگهی‌های شغلی جدید یا سرچ توی یوتیوب، browser automation رابط مناسبی نیست. ایجنت باید سایت رو باز کنه، بفهمه چی روی صفحه‌ست، هی کلیک و اسکرول و اسکرین‌شات بگیره، و هر بار که لازم شد کل این چرخه رو از اول تکرار کنه. وقتی کار در اصل «این سایت رو با این پارامترها سرچ کن و نتیجه رو بده» هست، خیلی منطقی‌تره ایجنت یه API call بزنه و JSON ساختاریافته بگیره.
حالا این agent-data چیکار می‌کنه؟
1- یه کاتالوگ از APIهای آماده برای سایت‌هایی مثل X، Reddit، Zillow و کلی سایت دیگه داره
2- اگه API مورد نظرت نبود، URL رو می‌دی و توضیح می‌دی چه دیتا یا عملیاتی می‌خوای؛ خودش API رو می‌سازه و نگهداری می‌کنه
3- از طریق HTTP، MCP یا CLI قابل استفاده‌ست، پس برای ایجنت شبیه یه tool call معمولی می‌شه
نکات فنی:
😟
به‌جای HTML selector، endpointها رو روی همون network requestهایی می‌سازه که خود سایت برای لود دیتا استفاده می‌کنه؛ برای همین با تغییر layout کمتر می‌شکنه
📱
خود APIها مرتب تست می‌شن و خرابی‌ها خودکار شناسایی و برای تعمیر صف می‌شن
💰
زیرساخت proxy و CAPTCHA رو خودش هندل می‌کنه(باید برم ببینم کپچا فارمش چطوری کار میکنه)
سازنده‌ش گفته قراره نشون بده این روش در مقایسه با browser automation چقدر سریع‌تر، قابل‌اعتمادتر و از نظر مصرف توکن بهینه‌تره.
🔗
وبسایتش:
agent-data.dev
📌
ردیت
اصلی پست
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5377" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">این ویدیوی موشن‌گرافیک رو با مدل Opus 5.5 برای یکی از دوستان ساختم. و باید بگم با ۲ خط پرامپت و یه ویدیوی مرجع برای گرفتن اطلاعات و متن ویدیو عالی عمل کرد. عالی  حدود ۴۰ دقیقه زمان برد و دقیق ۲ خط پرامپت با چندتا فایل فونت.
✍️
Saeiid</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5376" target="_blank">📅 21:35 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
