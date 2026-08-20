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
<img src="https://cdn4.telesco.pe/file/V-IDURumeBKRfzRWD2XFEYpkC81_byU5ueuSUek1tmZ6q8Omaffbwo876uIg47sJedshZnnTZ3BSkELKc7iNMKaS8y4DA0b1-pUi8GamC7iEH4lN-bpVwpBfkunEwqN3fP5MW0wbLeHWBIZfDF0IS-pY-wiSDyjRtqXRclY65FS_hQMryS7b31KNg-qhlW0xNH_eVorMb3i7dx0CsyeePrK5eYi2ki4YpK2-xA4aCNg49P3vXkC7ZbeAI6ecd9SWG9WXNEb1XjPCMdO7qz1zpFMvY9--xco0OblMJDBicrRM2bFxRb0vTynrROP_81O7uAaQmCS2xdECmmdjOQwBQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 993K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 21:54:56</div>
<hr>

<div class="tg-post" id="msg-142903">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4Q2wvyrS8vj4E68qLsVisoQhwtqIqsCwW95t66fCNnHqxULNr0ePRt0tyyhFsJuHUUQFHVfcsbSO54Hn4P23Yl4ZdOgnnzKAgYRZz3uy9G1m5qBU74WGbweIrKR4I1kWFGW4Gt9Y1IZkKtZ4W6b8IEJ2x5DYgPgv9G0g-ltXkz_dyNqnthzQLAUQS2M2WnbROZ1IcbphXdgWZPrmYUmPiXMNmNrBK-aHiwx5ICNqgjH1R3hDh_-gms-y5vJfwqRA-TbPGcApbmDNZZOgS7NW-83iiY5Jbi7HYtI-gPMRpUpdxsdrDe1vZc-w7usl-QYHYNPzRMUuo-toQrxjShvxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طارق صالح، معاون ریاست جمهوری یمن: تشدید تنش های اخیر از طرف حوثی ها مستقیما از سپاه پاسداران در ایران نشات می گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/142903" target="_blank">📅 21:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142902">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
گردان‌های "جنوب"، که با شورای سیاسی یمن (PLC) همسو هستند، تصاویری منتشر کردند که نشان می‌دهد تک‌تیراندازان آن‌ها در حال تمرین با استفاده از تصاویر برش‌خورده از عبدالمالک الحوثی، رهبر عالی‌مقام ایران، مجتبی خامنه‌ای، و سایر فرماندهان حوثی (أنصارالله) هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/142902" target="_blank">📅 21:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142901">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777ea22755.mp4?token=uO5i15ctxcWOvJuNk8daAkkh0B6QTvmKs-10Z4J53DEbyryvmh-ZR5kjRi75kNqitWydxuX5-PcS0XlbpwXz7ZAN7kugsIJpQQo0BxKcYrAYmQPuf-uqxmtRu8q_VFcQp0dTKofFljTm6iB-5lxpmokh6vdBYsvxOrMAwv2WaN3MXTAA3zphhx_b9FPkWkDEMlpXHzCYZ_hrnsD-b92omMKkHD4nmmotpInPIBEn6yl04GChj6gU4GiCGpBPV1Gl-tOAGnJN4gArkTKakyj6OSFTs4wbJZbVvYRG6cpY-W3iLYinnZ1hAgdGXbMqMkQLLIkqJ8Yq7wsOGoA4JsEbeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777ea22755.mp4?token=uO5i15ctxcWOvJuNk8daAkkh0B6QTvmKs-10Z4J53DEbyryvmh-ZR5kjRi75kNqitWydxuX5-PcS0XlbpwXz7ZAN7kugsIJpQQo0BxKcYrAYmQPuf-uqxmtRu8q_VFcQp0dTKofFljTm6iB-5lxpmokh6vdBYsvxOrMAwv2WaN3MXTAA3zphhx_b9FPkWkDEMlpXHzCYZ_hrnsD-b92omMKkHD4nmmotpInPIBEn6yl04GChj6gU4GiCGpBPV1Gl-tOAGnJN4gArkTKakyj6OSFTs4wbJZbVvYRG6cpY-W3iLYinnZ1hAgdGXbMqMkQLLIkqJ8Yq7wsOGoA4JsEbeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس‌جمهور، جِی.دی. ونس، اساساً دولت جو بایدن را مسئول افزایش بدهی ایالات متحده به ۴۰ تریلیون دلار می‌داند
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/142901" target="_blank">📅 21:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142900">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
رئیس جمهور پزشکیان: شرایط ناشی از ناترازی‌ها به دلیل آسیب‌ های ناشی از جنگ، موجب افزایش فشار بر صنعت برق شد
🔴
سیاست دولت، استمرار تأمین برق صنایع و جلوگیری از توقف خطوط تولید است
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/142900" target="_blank">📅 21:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142899">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cce6c887b.mp4?token=sOmAriS-T5Fq5B9X7lgTiZ38nUeaDXfCGZYovkmJF1Qr7lsJkRtGQeKrafNMqL4xGg0Xo1P4hX2qi1J4l6oaQQPJa-6QJSKNZ5Jxz_x24CvfJkZYMs2l1_BPOy4XlBiFNeXhlOYkWGWV7aD5orj2X0PYtFYG_JFnZcMWqQTjE2X6m5w2XwnoAjaBhBfgzN2n-TpFR63pQ5hBqm83DjCWQX-NqJ55Ua-85WGPXJIf6GTHz5mnPSCZ-wgXrvzddmR9Ok4dQJhjL8gP2fmAzi8HeMzAGAmYXfGArzKKfH-ebakm-ogR_wqws1rTihTY9F0k7S8eedomE_CRAMKinnce1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cce6c887b.mp4?token=sOmAriS-T5Fq5B9X7lgTiZ38nUeaDXfCGZYovkmJF1Qr7lsJkRtGQeKrafNMqL4xGg0Xo1P4hX2qi1J4l6oaQQPJa-6QJSKNZ5Jxz_x24CvfJkZYMs2l1_BPOy4XlBiFNeXhlOYkWGWV7aD5orj2X0PYtFYG_JFnZcMWqQTjE2X6m5w2XwnoAjaBhBfgzN2n-TpFR63pQ5hBqm83DjCWQX-NqJ55Ua-85WGPXJIf6GTHz5mnPSCZ-wgXrvzddmR9Ok4dQJhjL8gP2fmAzi8HeMzAGAmYXfGArzKKfH-ebakm-ogR_wqws1rTihTY9F0k7S8eedomE_CRAMKinnce1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش وزیر خزانه داری آمریکا به نفت ۹۴ دلاری
🔴
بسنت: امروز شاهد افزایش ناگهانی قیمت نفت بودیم که من واقعاً دلیل آن را نمی‌فهمم
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/142899" target="_blank">📅 21:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142898">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا لیست جدیدی از تحریم‌ها را علیه اشخاص و نهادهای مرتبط با جمهوری اسلامی ایران وضع کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/142898" target="_blank">📅 21:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142897">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
به گزارش بلومبرگ، شرکت فیدلیتی قصد دارد سه سال پس از راه‌اندازی، از واحد صندوق سرمایه‌گذاری کاملاً تحت مالکیت خود در چین خارج شود.
🔴
این تصمیم در شرایطی اتخاذ می‌شود که برخی شرکت‌های مالی جهانی در حال بازنگری در حضور خود در بازار چین و ارزیابی دوباره فرصت‌ها و ریسک‌های این کشور هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/142897" target="_blank">📅 21:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142896">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
پالایش ملی: با ۹۰ میلیون جمعیت، روزی ۱۵۳ میلیون لیتر مصرف بزنین داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/142896" target="_blank">📅 20:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142895">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-fhKGJzAzCx6DEVA5MttuKWVbM_rhVss_VpPuJxu0y0vvHV3TClyGibdzpAr8ASLUPG94TK2rqkfoOFnu0Pkk20EdhjUg4YL4OmuoRUekY0Fdq-dd0swObqe50xjVjT0c_6h6lwP2Z_BApmGVDI8KQeO2x4T_HSoJXPJJGKbWwcv0-DP6bonMb2y3-fl3m7xyPqFvkYJQU1o_3__dEx28fRkr0HxJKzrGSMp32RdVBfi8fLWSIaNZVA7gchp-aN1rsMjGDjVL3h4oUY74qxOie9ZDO3oFe7GvRgO9Ptyda1jmG4j_-gqkdOMOx94u440T7GVSxQUFlvkM1lMKcS-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار لبنانی: دو منبع به من گفتند که ایالات متحده امروز رسماً حزب‌الله را به عنوان وابسته به سپاه پاسداران انقلاب اسلامی ایران (IRGC) معرفی خواهد کرد و آن را یک سازمان ایرانی و نه لبنانی در نظر خواهد گرفت. انتظار می‌رود وزارت امور خارجه ایالات متحده امروز بیانیه‌ای صادر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/142895" target="_blank">📅 20:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142894">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
بیانیه مشترک بریتانیا، فرانسه، آلمان و ایتالیا: تصمیم اسرائیل برای برگزاری مناقصه‌های پروژه شهرک‌سازی E1 غیرقابل قبول است.
🔴
شهرک‌های اسرائیلی در کرانه باختری غیرقانونی هستند.
🔴
پروژه شهرک‌سازی E1 اسرائیل، راه‌حل دو کشوری را به خطر می‌اندازد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/142894" target="_blank">📅 20:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142893">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2-4DIaBqM8OG1zCE07-quLVWu57MDH10-H0oBK4_2nNIiH03W87FNHJofNP94wyIN8BhrmxbRG02xbuqO4aKgZX5YFJLSuzY8txuSU2q5_w8KR6kTxn1AMS8I-XyejFMakzRyUjoRhb62I7in1AzCX1EmxUELiZ0gVh_NAnxbxXT8RFmAxCqhxgT9ECRXQQK4Y7jfNgRVUSZZr-uxKKnCPUd0LCa-S5-KHmycOxj7B-Q8XtKGsVG_Kx73kPBkBTO-9UnxwxZSLRkm7jF1591YLLt0N4ZX5BCAvKHwhJzPv_BIWTFQFp0MPq02mXIWviyAFLZjrIDnasIBn83nz8FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلتفرم X زیر توییت رئیس پارلمان عراق با عنوانی جعلی برای خلیج فارس، یادآوری کرده که خلیج فارس درست است
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/142893" target="_blank">📅 20:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142892">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه چین در واکنش به مطالب ایران ستیزانه رئیس جمهوری آمریکا گفت که تحریم و فشار به تنش‌های خاورمیانه پایان نمی‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/142892" target="_blank">📅 20:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142891">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
نخست‌وزیر عراق: دولت در مسیر قانونی کردن فعالیت‌های حشدالشعبی پیش می‌رود
🔴
جایگاه حشدالشعبی را به عنوان بخشی از پیکره نیروهای مسلح عراق، تثبیت خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/142891" target="_blank">📅 20:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142890">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
طبق داده‌های کپلر امروز چندین ابرنفتکش از آبراه جنوبی تنگه هرمز خارج شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142890" target="_blank">📅 20:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142889">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LD1zZUXqMzhZ4gNGizk2gWwZAdwk14OvMzPtUKf6pSzG5wyQj82MsYrvMdkBbU4cNnWjdxtHcvJsiud9BvUxN4JocL6UPBo7thE0QNCzjn4orsGJ6La_Q2EpEgPFwfeN7yd27NenI98v_1TwjKJoCAHQhzrFA-IMn6t46VtRqCKg5eKiR1gGGwHEUT3VG9ICeU9MHry_Un6EFGBSXcLjP0wJKqnb1UKHv8PqTUgvxScxlQAF10Grbv4ltt11Au_j135DlkAMhJGO0aZm4OM5a0XlO2e4y9MH7T3ALUjCrS5xZ41Rjx8HiEUqLgBscs46IFhPHOroAPHpFb5s2KBWJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نورمن، خبرنگار وال استریت ژورنال: این اولین باری است که یک مقام ارشد دولت ترامپ پس از مدت‌ها خواستار تغییر نظام در ایران شد
🔴
اسکات بسنت در صحبت‌های امروز خود از تغییر نظام در ایران صحبت کرد. بازگشت به اهداف ۲۸ فوریه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/142889" target="_blank">📅 20:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142888">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f44565584.mp4?token=dAYpzlXdc4WyCxDK2Trq66u7dD1S2WNKQhfFKzZ4y8Mx4CPI2WkAVLw3wR9epcKskofF-Y1zv2fNneDBnjIrW-VYgIfNKO5eyUgFw_cD8QKHxC0ECpTL5wirYCSZXFh5vQDc22f4BBYxZ960PJt3LUssS6G5k4kVTaH05BysSYgYtVbFl7kw993AsXWc6chsAkPkP4KDnjYP8sNAuVmvEPdFv3nWLstKMSmm1o-nCF4CtmEC64L5onDKzKi2etA9tq0B1wB2DU3GyAYDleX1ETpRkmDvRLNJhQ2rlkKbnLrviQBPAJEJjJuUMzB7LuL-a4HgEaikQQdzzvI63i7aoA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f44565584.mp4?token=dAYpzlXdc4WyCxDK2Trq66u7dD1S2WNKQhfFKzZ4y8Mx4CPI2WkAVLw3wR9epcKskofF-Y1zv2fNneDBnjIrW-VYgIfNKO5eyUgFw_cD8QKHxC0ECpTL5wirYCSZXFh5vQDc22f4BBYxZ960PJt3LUssS6G5k4kVTaH05BysSYgYtVbFl7kw993AsXWc6chsAkPkP4KDnjYP8sNAuVmvEPdFv3nWLstKMSmm1o-nCF4CtmEC64L5onDKzKi2etA9tq0B1wB2DU3GyAYDleX1ETpRkmDvRLNJhQ2rlkKbnLrviQBPAJEJjJuUMzB7LuL-a4HgEaikQQdzzvI63i7aoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیامدهای حمله بمباران با پهپاد به تپه تل الدبشه در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/142888" target="_blank">📅 20:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142887">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUPh3Q2WNIMLxf_ikWX6K6v-48UDlOjwubZEXLeODxt4XtPoB6Tn1dYTt2W1yOU-Y5_GonzgFugefSnH9Rgh8ZknQlcgN0GNN0_8g8ycjOaWrjo1oYZsK-bN5Q9HtEyD0VmIuyGwCaRo1dsN-4zpfogzZMKszGBHQr9ZQGS_RRbvFibBriqE0WAcgEovUyabHY_VjeK1NU6eEUBLqmJskN4EZPzgQkUAZWPtPgVD4dV81r4paPaAf7gOWau4xehYTPafWfZTPGc59Wxm3fY8eZVPjzi1y-2-tjUD2Ssx4PbnPc-FJ7BMtWUIUZw0k_sEpudzczX-Vrlraotng3lUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر اقتصاد دولت رئیسی: تمام نشانه‌ها از آشوب و جنگ در شهریور و مهر حکایت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/142887" target="_blank">📅 20:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142886">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
شلیک ارتش اسرائیل (IDF) در نزدیکی تپه علی الطاهر، هم‌زمان با رها کردن بمب توسط پهپاد بر تپه تل الدبشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/142886" target="_blank">📅 20:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142885">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOnZT_g4AprNz9pc1HSyWyVykwZR060MeiE3fdhovkdATna9TXdscA-IP171LluZbJyipBPdBYkhTlIVl51zTnqw5cKTRYyjlcrfOW1ONnKJ8RpOI1cDrOeh7Dq7j3hkYTkJWTdAcYmsgl8YySGQYSQruaH76EoPxxNciY3k4jHMpKVB4ZUODSESNKJOMcIpTbGNcm7_FQNv3ZxrrfPHe2gMWvsPHfl2xQC5239wOQVL6YlEN6qD11do4iKk8t-ls1H2rcP6KBusDc7q_H-PAlPKl5SHvUdqEynBARLF0d8xIJM7lc4AdF9E2biJcx9UNLS8_O-QtQvbW_mdSELEcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام : هواپیمای ترابری و چندمنظوره MV-22B Osprey متعلق به تفنگداران دریایی آمریکا، هنگام حرکت ناو آبی‌خاکی USS Boxer (LHD 4) در دریای عرب، از عرشه پروازی این ناو به پرواز درآمدند. این ناو همچنان به اجرای محاصره دریایی آمریکا علیه ایران ادامه می‌دهد.
🔴
تا ۲۰ اوت، نیروهای آمریکایی برای اطمینان از رعایت مقررات محاصره، ۶۷ فروند کشتی تجاری را تغییر مسیر داده، ۳ فروند را از کار انداخته و ۲ فروند را مورد بازرسی قرار داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/142885" target="_blank">📅 20:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142884">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izBaH4TcKaK05k8gvHLZfYLkxZzcYYUNP_ULnMq6AYkoNUsTI70JZiPcoeyFyxFHi68ubOeq4MServnAUKcxlqXcBiKpGODJzLN5F3ZqojMQjY-fAgMBRhI7QoMH7Omx9rY6R5W7wEgFi0TR6dVtIrv9uOQ9-lBrOPj9KumbwJH976qYKkJt1cyHmbbRVhG2aDQNWRqCpxttTlfjtjxsZbddRGMU9JuOTITqeywfGcM88a7HgM9vvLuVOGnILuvxHbIfsjzQEvKDOOrRL-pCnMs1uEnZV2BMRCGYt6prwcUiJxFWQ7rGPqwvnmeCxx3B_5r2WzMN7_xa_PFxKIp4BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیباکلام: کشوری بنام فلسطین وجود نداشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/142884" target="_blank">📅 20:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142883">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
اسرائیل هلیکوپترهای تهاجمی آپاچی‌ خود را به مرزهای سوریه منتقل کرد
‏
🔴
اسرائیل در بحبوحه تشدید نگرانی‌ها از تحولات سوریه و افزایش تنش با ترکیه، آرایش نظامی خود را در شمال اسرائیل تغییر داد و طی عملیاتی اسکادران ۱۹۰ بالگردهای جنگی آپاچی را از جنوب به پایگاه هوایی «رامات‌دیوید» منتقل کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/142883" target="_blank">📅 20:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142882">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
عسگری، رئیس‌ کمیسیون کشاورزی مجلس: وزارت جهاد کشاورزی قصد داشت ۲۰ هزار تن مرغ تاریخ مصرف گذشته رو که یک ماه بود از تاریخ انقضاش گذشته بود؛ سه ماه تاریخش رو تمدید کنه و وارد بازار کنه. بخشی از این مرغ ها وارد بازار شده ولی جلوی بقیشو گرفتیم.
🔴
گویا الان چندین تن مرغ تاریخ مصرف گذشته وارد بازار شده و مردم بدون اطلاع مصرف میکنن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/142882" target="_blank">📅 19:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142881">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDj_XbcN_cXdsPXz0vxuBMUW6rFH7ehb0t4WePoYK-Bg6TOYINGWTrzgVMaBgARy8pxdQjnozRJsCSZqP--kEpH-SeFAsn4RVcVXXZ9CxZkxVGzrGNEIs3krFhC-ZYNsv9DmthAdd1LKn6c7q8fJYDYnzuzOy4pItieDeNDOsV4pZxPL5jt02ogl2t891Xc4fbq7rHPiDS0h7QrAL9W7SjCnC6bUwe9P2NCcskWhq-ht3ROTdwfH21Vi41b-1zeYq0-btr2JhaebhAiAvSEOETQkA8viRpxtS23HIeAGSol6TRtywg_ryWlsr8YnFMjFnnzLAzKhyOa2PERR4Io03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسیب قوی مرکز، یکی از فرماندهان کلیدی جبهه مقاومت ملی ضد طالبان (NRF) امروز توسط نیروهای ویژه طالبان کشته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/142881" target="_blank">📅 19:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142880">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
دزدان دریایی سومالیایی تانکر محصولات نفتی SIBU 1 را در خلیج عدن به غارت بردند. این کشتی پیام «دزدان دریایی در کشتی، کمک» را پخش کرد در حالی که دزدان دریایی سومالیایی کنترل آن را به دست گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/142880" target="_blank">📅 19:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142879">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وال استریت ژورنال: مقام‌های عرب معتقدند ایران در نهایت به افزایش فشار اقتصادی، واکنش نظامی نشان خواهد داد، در نتیجه، جنگ دوباره می‌تواند شدت بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/142879" target="_blank">📅 19:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142878">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سنتکام: گروه رزمی ناو هواپیمابر «جورج واشنگتن» پس از ورود به حوزه عملیاتی فرماندهی مرکزی آمریکا در روز گذشته، در جریان یک استقرار برنامه‌ریزی‌شده در خاورمیانه مشغول فعالیت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/142878" target="_blank">📅 19:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142877">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
آنیتا هایپر، سخنگوی اتحادیه اروپا: آنچه ما از جانب خود انجام می‌دهیم، دعوت به خویشتنداری همه طرف‌ها و همچنین از سرگیری تلاش‌های دیپلماتیک است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/142877" target="_blank">📅 19:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142876">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
به گفته بسنت وزیر خزانه‌داری آمریکا، احتمالاً ایالات متحده جنگ گسترده‌ای را علیه ایران از سر نخواهد گرفت، زیرا فشار اقتصادی خود را افزایش می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/142876" target="_blank">📅 19:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142875">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0005fb25b.mp4?token=TpTV1jA2kam31sU9BCvyAT25zTXOt0M1yedWnwSGOU7gsMx-tL45c87pyChnHO-w9TkVMdh7qHwJjXTdTlWxiB78Z0pwv0ictaycolKPjPR93d0FiW17WWg8aqdVPGS4J1VelFWGoh9KzdEkbLXE60PFEBp1kf3Iw55O68uVvMydzSr44IVo34ODi0LLvS8FGPrw5dqixrSxlzd19dCMG0u7ojhTEsQSjBdQLHCzsnjlb8-ssNbCcGhmECBPsaXUG14KAMAsDJIuSoZlRvKqbyX2cb1tgts-NkWcFUs_za7Ry2CWt_05-60iVwpxKwdkKcXaIWeMu7h_pTIxY0mjvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0005fb25b.mp4?token=TpTV1jA2kam31sU9BCvyAT25zTXOt0M1yedWnwSGOU7gsMx-tL45c87pyChnHO-w9TkVMdh7qHwJjXTdTlWxiB78Z0pwv0ictaycolKPjPR93d0FiW17WWg8aqdVPGS4J1VelFWGoh9KzdEkbLXE60PFEBp1kf3Iw55O68uVvMydzSr44IVo34ODi0LLvS8FGPrw5dqixrSxlzd19dCMG0u7ojhTEsQSjBdQLHCzsnjlb8-ssNbCcGhmECBPsaXUG14KAMAsDJIuSoZlRvKqbyX2cb1tgts-NkWcFUs_za7Ry2CWt_05-60iVwpxKwdkKcXaIWeMu7h_pTIxY0mjvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روایت تکان دهنده زنگنه از قاچاق بنزین
🔴
خود پالایشگاه ها مبدا قاچاق بنزین هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/142875" target="_blank">📅 19:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142874">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
دلار هم اکنون 190,000 تومان...
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/142874" target="_blank">📅 19:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142873">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: زمان آن فرا رسیده است که متحدان و بقیه جهان به تعامل با ایران پایان دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/142873" target="_blank">📅 19:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142872">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از منابع آگاه گزارش داد که آمریکا از امارات خواسته فشارهای اقتصادی علیه ایران را تشدید کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/142872" target="_blank">📅 19:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142871">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: انزوای اقتصادی ایران بزرگ‌ترین انزوای اقتصادی در تاریخ خواهد بود.
🔴
زمان آن رسیده است که متحدان آمریکا و سایر کشورهای جهان از تعامل با نظام ایران دست بکشند.
🔴
ما کنترل تنگه هرمز را در اختیار داریم و حجم زیادی از نفت از این تنگه عبور می‌کند.
🔴
ما شدیدترین تحریم‌ها را علیه ایران اعمال خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/142871" target="_blank">📅 18:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142870">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/857974ab2e.mp4?token=U4ZhV67IoTHFhjEFlrUl0nODXi2uoVOERITnWTg2hxY0xr9ayNP6WLbxnDTJKFOPiA0Plyk5ifFQnGxPhGo8yzaMAByaUjxWB067zWrYiIMtBP-_etC-0h_2TnGyQB9CfhB27W3VQZnajlE1DIjLp4LrfKcFr8tHdrHeJwAAEjNKHKrIs9QvxB-DmsoOTC0WD9aYLjsdMg-myrefb2w_vzczE4yXW5BIYW2K_c1G_9DgScbovAhbYRXXs3Le2rX7-8hvPxs6ruscccPIdMv98apAqMuxfKooRUO07GTYp6zCpXy9JzExZE-kcjzjrs_UUq5gpzxnEN8uo1z9mfc7nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/857974ab2e.mp4?token=U4ZhV67IoTHFhjEFlrUl0nODXi2uoVOERITnWTg2hxY0xr9ayNP6WLbxnDTJKFOPiA0Plyk5ifFQnGxPhGo8yzaMAByaUjxWB067zWrYiIMtBP-_etC-0h_2TnGyQB9CfhB27W3VQZnajlE1DIjLp4LrfKcFr8tHdrHeJwAAEjNKHKrIs9QvxB-DmsoOTC0WD9aYLjsdMg-myrefb2w_vzczE4yXW5BIYW2K_c1G_9DgScbovAhbYRXXs3Le2rX7-8hvPxs6ruscccPIdMv98apAqMuxfKooRUO07GTYp6zCpXy9JzExZE-kcjzjrs_UUq5gpzxnEN8uo1z9mfc7nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: آیا کارزار اقتصادی علیه ایران شامل چین هم می‌شود؟ چون چین شریک اصلی اقتصادی ایران است
🔴
بِسِنت: بسیاری از گفت‌وگوها بهتر است در محافل خصوصی انجام شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/142870" target="_blank">📅 18:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142869">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iH2k8MNf2T_VPo9-kwrLTEWI0v8IwXtnEg6CnVr_iKtOdZZKqshHOozG_i0fj6raa4MONDg6Jvbwxjh096kH2WHNAcP441BIPXsRIvqtvNyy2-TgtYL1y1s3NtVmk0Kd8ooabV9ceCsTMS16srfTERdnE46m444B5lmDF4424BmBTPXemmAgBT1Tsl4J4VLSvudbaU43MKUqtorrEMlOT7KF_Y0RAVmrU6_0Tq0sd7RypJXDe1YYPYWfGbLs9ZR1hmrG8tJbnoQ6ggw-hBn5jaPC-mY2gsJH7r1nW9fLBM7FtfRlOI6gS3d4S0C71L5zXJocNm-SJ4oh4wCwj638Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا:
ما نظام ایران را سرنگون خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/142869" target="_blank">📅 18:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142868">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0378fbc38e.mp4?token=Bh8xRmNCNheEy6h8aqUAWWTm6a_gNdvxq2ft0ZgmIikOkNfupCinrBI76e2aaixCQGlUf4cCe4OZNgY38Mx4B6d4GjVLzHWcoCiq6YE5wq_O1X2Zx67usdbP0jfPJhjzNOzC9Jlvi13ORMze39SVyqGRCJQvbArEVYPjouUxo2W6_mSWPVpwf3PibgMInk6-ee9Qdro9EMuKQ3qI-9hDtM5SPFag8xCJ-06MkFz5IvXfB594AghW7byk3KgLUPhNzBR6aFWlUghob-4LTa-tnt9UQDtFJGx-TXxxZ9vq68isvTX3HzY3rb4wCFPnFK5f0zKkWzmndDhOQjS7ejrosg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0378fbc38e.mp4?token=Bh8xRmNCNheEy6h8aqUAWWTm6a_gNdvxq2ft0ZgmIikOkNfupCinrBI76e2aaixCQGlUf4cCe4OZNgY38Mx4B6d4GjVLzHWcoCiq6YE5wq_O1X2Zx67usdbP0jfPJhjzNOzC9Jlvi13ORMze39SVyqGRCJQvbArEVYPjouUxo2W6_mSWPVpwf3PibgMInk6-ee9Qdro9EMuKQ3qI-9hDtM5SPFag8xCJ-06MkFz5IvXfB594AghW7byk3KgLUPhNzBR6aFWlUghob-4LTa-tnt9UQDtFJGx-TXxxZ9vq68isvTX3HzY3rb4wCFPnFK5f0zKkWzmndDhOQjS7ejrosg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناسان آمریکایی معتقدن ترامپ به احتمال زیاد از بمب اتم علیه ایران استفاده خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/142868" target="_blank">📅 18:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142867">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e81d0658cd.mp4?token=t8XnzT3zfqrdIsbheuETwsUBeOOWHimvweZkqz60gg-A50P0FM2j5VFL62jgwHcYex8rdBUU6UR0CwCNqJDPsN7j1_j-isIN8op6hrSSwhobskUi8Igj-Diie9xgRK_laKb06Umtd9A4cZTUqyAkbv2r60k1ZZfUFrk9It-FU6S8h1e-zK1jTimYWrwZgFjL0CDBXoa5yvDI6ckiFPMRjoHwXR0Vi2OhX9GpJcK72eGugG18_Z_zZqR_wcuUKx5vBpzBhP2-TCNTw4cTCoV787xD-pgHOoLhNC3xRE1sgzSRZQAyVQSPtxAg7BBzyhBYCO2rJLKof0rWX8UBIzn4wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e81d0658cd.mp4?token=t8XnzT3zfqrdIsbheuETwsUBeOOWHimvweZkqz60gg-A50P0FM2j5VFL62jgwHcYex8rdBUU6UR0CwCNqJDPsN7j1_j-isIN8op6hrSSwhobskUi8Igj-Diie9xgRK_laKb06Umtd9A4cZTUqyAkbv2r60k1ZZfUFrk9It-FU6S8h1e-zK1jTimYWrwZgFjL0CDBXoa5yvDI6ckiFPMRjoHwXR0Vi2OhX9GpJcK72eGugG18_Z_zZqR_wcuUKx5vBpzBhP2-TCNTw4cTCoV787xD-pgHOoLhNC3xRE1sgzSRZQAyVQSPtxAg7BBzyhBYCO2rJLKof0rWX8UBIzn4wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت درباره ایران
: این درگیری با ایران... ما از این وضعیت عبور خواهیم کرد. ما نمی‌دانیم چه زمانی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/142867" target="_blank">📅 18:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142863">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cI-O8pBewKJKS4BIqY_tNSLHUTDhLgw2fXdRI74INHwi0e7eSWtuj0v8CMHvjavdllbY7A6IyDK6oVBpL2X9DZ-tSPQxA6j4t37gSaMx_0EEopDv6ZhHQij48DFsCROEaFL2tvIzoEk9sWvsiYliNGyMwJhLwXdusG8FwnGPml9XFJjozG04pc4HyE4TavOC9rSWRES93nNpjs4Xh_stz148jjk62rlOr9CNZQIpCq33E7IeyrnTh7Ip1lhH_TQT3dXufb9YphF1HZnlkd6mUsCCTSw0SsxiRBfOr-EvDd4SWxf9DOmMHqEUpZAYnJr1c3oumCukyfbPWcT6nhESFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ggtgCH-jwoqHPeFemJGsAPBXLk26Kc53toaGoC1OzzRZtY_YhEHU_rEfqYJqGvgoaYNHm8maHA9VCAqG9EUl4-JW0EWZs2Nf2tOHOEiYpsMZ2sICwHO8kXwBAp1PVFtdoq-oV7CphClaeCviE-C0_NzMEJfjXxNP3CFqc9fBbB9mJ_LBKlp6yDWrl0prrAA9Hlj02lMIt8a0qiEF_H9pA6n3BpPklZQqoq_ILAyIcshZ-uj-2xPi2sOXPGqMgL34ySBuIWyN0HAKMB_p0O-1z1_3Ddu0gvY3zwckTl_OPQiOd9UH69-7q55SYTSlgbnyg4UlvRCdOQL4-XSLTqCteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pY5zfZFn-K1ssg79nESnSO32MXDApHQEgu18FsS-LWXLEDfYAaNCl5vf9CtWXJfVeja0nU9SINrSD-ZscJql0WbVxny4qdGaLKA7PJjjvLLis-5UbFOGezjReY_SbDijWaMAe1d_7TCGMhX5IVuI566_CxEoM8h7eQU7X_NjNK2POJdZyFEaVW1Hw2F9cqo8cEXUpG3rdrdWFH5pqtDNUJvx7tbrrrh_LXqe97C7VlPljmu2AVmm5b2fqKSZJqvWoofUxiotvVs2R5Bv3QyAsLIZao3taW5ppAvrN4h4rQzlx-wdHnaHjcQSGDqDmUf0hxPLvIA1pwjtjSuJ-8eMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0tmrZ4SSqrOnyPncLp5wY4pEhLpoTuK3SZsY8beme6w6HKQDH5eJ1bntwKvwGRBJV6jhda8HkWsDgtUZkOzJWfLXg88UbUNGJVVIeqewhHnwzvrytJBzWpOhcvzNvcR_taswbb9edeRa_u1FHbMWrLe-wB4KKcz98CF5ueOGjF6AHtW-sZShYfh-n7Yg2bnfYDwULa1-mQidmw0c_Lxv5mvJ9DGKezjM4cOyIYPDyxhxYq86LQu2kwXEJxKu84BHEwo7tsiqCOOWYG9XV-apkX_w8NIxQWPTdGqBVzdF3FhdyqdYkWhI5B0ntWm6YQPHo9RjkcrthG715-_m8NFqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از کنکور سراسری امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/142863" target="_blank">📅 18:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142862">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0X1jTAhxuevrDKMT6gxESpggbhzQYyoyPwfsAEOFtekysbSAgEhDUhlbC9e5GZjFnDnI2eGaZqtyy73hdVYhyRqDZTiP3nqzSQfE2Z3KvL1Tc7j51JG3fAbE8gTXyqs-YmL5he8g64DVFZy8HlFsCpWPF8ORFGGe61-YVNdUMppP_4RfMzfbpW1pZ6G4gvtNE6YwhOWg-YQy2dq4VG18Zzrx3d3FrooSN3CnB8cLfAq5eDNo--bBJcw8-alblRLkOU-mkcnGXzUE6rjh_WaZWNRtWdjG-XHA_aNXs_o1eNmySnFU5rSp0N3_ICMSMl_glAO2xDp9Qu_zemIc4rt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثبت تصویر بی نظیر از یوز ایرانی، خراسان
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/142862" target="_blank">📅 18:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142861">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
معلوم نیست تو تایم جنگ چند لایه پاکسازی شده که سراغ پایین‌ترین درجه دار سپاه رو هم می‌گیری می‌گن کشته شده.
🤔
هیچ صدایی هم ازش در نمیارن که بگن ما کشته نداشتیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/142861" target="_blank">📅 18:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142860">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627b8da31b.mp4?token=Sm5bct2KFdHINHccmx6ABgyA72mVs6IC2by45H21fCPZP_cRbznLR4zJUPtBaD0pKtV88EqYy4f-xVYFEk_mLb3461a_8O4GeRcirxZmh4W8Ie9rC2M55uuYFjwcCuHoApz8TxUYhyNnjAsF-_znvL9jdmm6HB3-vuEicTUsjseLQY6BcwFifH3WGL04gkl9N7BBTX72gzJM5CbHsUlBFXvJIYvvhisNvmLPMlID5VJUqU41qTFdf7WiU4Rm2SRMJa8CU3Oi6CpRCq495ZxUm2fG4YN6VGlk_y2EPVTdfUvIMsKYxOaOBmpcLib6RzGKqPTAzif_S0ctlN-wYgj_gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627b8da31b.mp4?token=Sm5bct2KFdHINHccmx6ABgyA72mVs6IC2by45H21fCPZP_cRbznLR4zJUPtBaD0pKtV88EqYy4f-xVYFEk_mLb3461a_8O4GeRcirxZmh4W8Ie9rC2M55uuYFjwcCuHoApz8TxUYhyNnjAsF-_znvL9jdmm6HB3-vuEicTUsjseLQY6BcwFifH3WGL04gkl9N7BBTX72gzJM5CbHsUlBFXvJIYvvhisNvmLPMlID5VJUqU41qTFdf7WiU4Rm2SRMJa8CU3Oi6CpRCq495ZxUm2fG4YN6VGlk_y2EPVTdfUvIMsKYxOaOBmpcLib6RzGKqPTAzif_S0ctlN-wYgj_gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه آی‌فیلم داره سریال "متهم گریخت" رو برای بارِ پنجاهم پخش میکنه، بعد این سری دوتا از صحنه‌های معمولیِ طنز سریال رو به بهونه‌ی غیراخلاقی بودنشون سانسور کرده تا نیو ارزشیا تحریک نشن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/142860" target="_blank">📅 18:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142859">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏
👈
مدیرعامل توانیر مدعی شد: کاهش ۶۳ درصدی قطعی برق در کشور
‏
🔴
محدودیت‌های اعمال‌شده در شبکه عمومی نیز ۶۳ درصد نسبت به سال گذشته کاهش یافته و تا ۲۰ تیرماه هم خاموشی خانگی نداشتیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142859" target="_blank">📅 18:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142858">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سخنگوی ستاد فرماندهی مرکزی ایالات متحده (سنتکام) به شبکه الجزیره: نیروهای ما از اوایل ماه مه گذشته عبور ۱۳۰۰ کشتی را از تنگه هرمز تسهیل کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/142858" target="_blank">📅 18:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142853">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oHn5ZpqWF-PJECphZ5Tg_yv11Ai1_pGpAY9zScKViiVjTmXfwVHpyuKmQRQLPmE80nY6xq903-n9BjPhQmUBYawrPgjpkjXrQigujB3fdHpxUlLkVz6WY-nJ2_tV-VvgkWGkz52Jh3ZprvRXlXE3j3u923DEowWQ6jjsQ0bYML43grby8Spqeoo_1115bV-rrS6mi_7aukcMshmeMEbD2qxkdOd2Sbi8sJhmKboOp886vfEf-S6xhvgdlyn1QBguO7jBqkx1F37HitrdVupgshAs-ugfGQpFMUnlubdBN782SDLdBSl8cGxYouR7peAWos7kpWQg_8epuJVfPP2QEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V_gikAnQGup-BuPN_YzGfIfQrBkOEiPQ220dEtuN0Q7cedPNa5Kdninb41ygSoo9uBTGePd3NAW-S-6gwne3wE1XakL0Ds8-JShM9gslIS58T0H1Uql7iLiSKmXDqNE6-U1kGwyo1VSI9JFbX1oduTi9v9pz_yM5oZi8bAh-h2UyotyrQa5KQAugQ8OCdwB0jh91UksP1P6LQsHcDXo4I2xJhFlMNfAPNuRrK2QoRnWjkKJ0h7ytAKGsd2K8kdPheAQAQOzTRP8ypVvC1BVcpO_vk2gIFmWuaKRPkAqIth4x6zBgRhxv7_R9yqUBIfXKffYp3WqDzM3o6xZaV_5Nbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YejX2_sV3_mgBuVmZloiDsHedj4_jpZWu3vh9a8nT51hzKEirS08fY0enGo-cc4hNwCL9ySWsw97CQwchhYVt8hcukonVqaiUwzkyc4-_ABVBoN-enrN9cUatyP7h3unUIA5Z1jxAMWXXEUfzVLaKWo1GILgSv7tqzO-NAR-T2RAlBFwzeIy7a_ZrG-FTmT3pWdN0aAKW6L5maSTHB-i7soDi0juRv5jUw7brmGUF8C2fRbm0KJX7k3wJDzOB6Qv_vO0ThYb3HqeMw0YixKwNr2rcNY57VK50KU_cRfNMAUUElUvoGUX_-yDlg0w2n9hwC1AJFjNa4bXzQdNsQQxdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=QCg7LXLcN273-qr6sJTSUhdUbVS-UG7c08s5AHujv4uEQSzWFVujPDbMn_qwEyDXOyoI2k9K9cbipBJCJV7t10YJYqBQYD64ILnJURhvF5MX34Z3RaXXrNRH08v4Ug5_d8t18CawFwNEoik70caCeAHKSJMNRNQlBgUBi5pOrZsvmupUGpG0Jx5Wv6XwnNwTT4ZVY20uI4WbsCKB8I59luwuUIFBRPXTR9L5poBH1R1OraBCURsflfDNa3ptFamXYN3AqUI0aQcpmJSj6Q75-aqrhDjvvspG-1MQiP9SltvSE8q5bABTil-8JGe2t95xA4B6izXU1wGwWh4xMlXrK0T0XeRMOHWnKVmY5sfhdyE8zRPxZwgN4u4M5WQeucMDnXhx8UABLZh51AUYP25QN4ky9FnN2Mj93SsIGWx2LRs6FjvuSJ3pBAgJYJKu7Duc4HQZWxSiS56afAot3pGhH6dg-CpPllRPxTkidHnT_v9IDj7cLkVn2QflT0HPWdHwSEVTQPe--PV7c_TC07Pf6FQaCfJDrINxG1xsqGHfBNSsvNusebQn3v4HekEt8AdY3pGFDXhPylntI8A8_4Eafb89v6_TcbXeuHlRmR7NUBL0yr31AtVrtAtY-7Ojx9-WKUXyvH_RP4vLWgfiygPd87x_tc2CYBnOg5S0kRQM9tI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=QCg7LXLcN273-qr6sJTSUhdUbVS-UG7c08s5AHujv4uEQSzWFVujPDbMn_qwEyDXOyoI2k9K9cbipBJCJV7t10YJYqBQYD64ILnJURhvF5MX34Z3RaXXrNRH08v4Ug5_d8t18CawFwNEoik70caCeAHKSJMNRNQlBgUBi5pOrZsvmupUGpG0Jx5Wv6XwnNwTT4ZVY20uI4WbsCKB8I59luwuUIFBRPXTR9L5poBH1R1OraBCURsflfDNa3ptFamXYN3AqUI0aQcpmJSj6Q75-aqrhDjvvspG-1MQiP9SltvSE8q5bABTil-8JGe2t95xA4B6izXU1wGwWh4xMlXrK0T0XeRMOHWnKVmY5sfhdyE8zRPxZwgN4u4M5WQeucMDnXhx8UABLZh51AUYP25QN4ky9FnN2Mj93SsIGWx2LRs6FjvuSJ3pBAgJYJKu7Duc4HQZWxSiS56afAot3pGhH6dg-CpPllRPxTkidHnT_v9IDj7cLkVn2QflT0HPWdHwSEVTQPe--PV7c_TC07Pf6FQaCfJDrINxG1xsqGHfBNSsvNusebQn3v4HekEt8AdY3pGFDXhPylntI8A8_4Eafb89v6_TcbXeuHlRmR7NUBL0yr31AtVrtAtY-7Ojx9-WKUXyvH_RP4vLWgfiygPd87x_tc2CYBnOg5S0kRQM9tI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مادر پرنیان دبیری با انتشار ویدیویی گفت دختر ۱۶ ساله‌اش پس از اصابت گلوله به کهریزک منتقل شد و پیکرش در محوطه این مرکز روی سطح آسفالت قرار داشت.
🔴
او همچنین گفت هنگام پیگیری تحویل پیکر دخترش، یکی از ماموران با قنداق تفنگ به او ضربه زد و تهدید شد که در صورت ادامه اعتراض، پیکر پرنیان تحویل داده نخواهد شد.
🔴
او خواستار پاسخگویی عاملان کشته‌شدن دخترش شد.
💔
این جاویدنام ۱۹ دی ۱۴۰۴ همراه پدر و مادرش در خیابان بود و از پشت سر با گلوله جنگی سرکوبگران هدف گرفته شد.
🤔
حرام زاده حکومتی حسین حسین کردنت رو باور کنیم؟!
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/142853" target="_blank">📅 18:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142852">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
مشاور شورای امنیت ملی عراق خطاب به قالیباف: قانون اساسی ما اجازه وجود گروه های شبه نظامی در خاک ما را که تهدیدی برای امنیت ملی و همسایگان ما هست رو نمی دهد. دولت در حال جمع آوری تمامی تسلیحات از تمامی گروه های شبه نظامی در عراق است
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142852" target="_blank">📅 18:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142850">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVg8JhukdJQElNk8-7agcwRi1pCqibxtW1lI57twSpkdUL5A9FZ1g24vEoTn0bQbLFoIZBK1MG_ogzTBF6vu25PFYzb_X2QNav5RpUi4i6fIs3gsNS7AjMZ7N-hBo5PbZ8Jgy9k6UzQN_NxIti-al-ZUecxyyO-pwN6tedEZLrY-2aByDR-f4AVkRN8NZ8GQKrbocHXqAStKmj0hdEpYlmEIJfu0Phog5JbqSVZpCVZaDS5uemZYs7fsdwj9wHJik0ypM4kdfPuO-x4FF8DcQlsSmnkzCG3xoUVUZPHAbQtmcS0jbwBzhOt168NyUOSM8Pqjqntb34rlyJ5a0Kbkvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1080cad72b.mp4?token=i7a9AWizrl5p7b-KvTn7zmiJ1LLPZeZyZ8dB2zfoOXNjGjbLJRvfuFL0n2Dh71sqUS_Pktn6TvEASFRx8y--ns4NWYb3Dt2--DRcA4J4F1CKAwHfRrs-n8Lrl1j3eCbTVHOSn7iyjECsXzcKIcSpLsZwd_qeZsTrHhF2b-Tw7Z_dAREeB_Dn212oEpK-tFwrQ6KiRaCk-kVrzHpZQNfvFdHbFi1WS0dXPeNp6hYCO3kos-uHu_knb1vLbblU75HooyjPqgKwDA0gPvJRJYdgzYBlHmoS_mHQVWtt0_a1Dp3miDFU4GOE9u1R-OqbOnNVzC4a_LzbtHk2y_1eVAmKTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1080cad72b.mp4?token=i7a9AWizrl5p7b-KvTn7zmiJ1LLPZeZyZ8dB2zfoOXNjGjbLJRvfuFL0n2Dh71sqUS_Pktn6TvEASFRx8y--ns4NWYb3Dt2--DRcA4J4F1CKAwHfRrs-n8Lrl1j3eCbTVHOSn7iyjECsXzcKIcSpLsZwd_qeZsTrHhF2b-Tw7Z_dAREeB_Dn212oEpK-tFwrQ6KiRaCk-kVrzHpZQNfvFdHbFi1WS0dXPeNp6hYCO3kos-uHu_knb1vLbblU75HooyjPqgKwDA0gPvJRJYdgzYBlHmoS_mHQVWtt0_a1Dp3miDFU4GOE9u1R-OqbOnNVzC4a_LzbtHk2y_1eVAmKTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای، توسعه بیشتر فعالیت‌های پشتیبانی لجستیکی ایالات متحده در شهر ینبع عربستان سعودی را نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/142850" target="_blank">📅 18:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142849">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCd6D5jvrGJr6aeqzanteqgHAtIftAwqMo-MQVH7qmBkD6VHvgyWF0YGnQmpKIPKb1iVPsp0p6kxcLgbq_3XzNCGSo2JC_lVxWYeZHEYjkKIslKgt2I8dyV3MNcjDkQ3wQnTk8Fug3e1RC5Ermgr0KWMy30D59VQ7WWbg_Dlv8BWqC0_NsnWHffOZUlag1LMhtt3TDrpeA3XBkHwkGYB2Xsx4VHB4z9y13YxDmJaXn8rhSGjQ3_cMnP-uJhiy46cO8dG1mUU5kQNLEMl2HTsZUUIiBwMaN9d7Q5f_qzaFD7dolrXWUeMiPK2lMq5KTBeR9YCVWlvh-5en2Ra8v00ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ضرغامی: از اول انقلاب تحریم بودیم ولی کشور رشد کرده، پیرزن رو از تاکسی خالی نترسونین!
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/142849" target="_blank">📅 18:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142848">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwb1ePm_BD2zW7ZfqgMrZ8_pVDYK7LPFikC8nSoU8t3RuYfJCbLxLRMTCgSnETpND-CyL0dYRNHoUmIgw6zvV-ZgYVti1Dh4-SpD6QZnHfw0zWaJAA3FP_ooWCstC0REmOSL1eouEmvAbPdSo6GnW9eTIbpLS2LbR9JUK9FQpJ6V8ueVBbjU_oqq5FLbxjpbl3zxn6_E8r6iftyb9WJRxUM9mxjOLY_ifAU6ts2XgtIHRRbnlx-PTtIKmCbR5ozUNR4PnMXYsG9MV8lirqreiE0Ei6NXgQLear7igfUQpj3K7xnNkmro6L7sfApSNKWkaQW2hJwbG4o2rYa3CoTlLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه وزارت امور خارجه درباره تحریم‌های اقتصادی جدید آمریکا علیه ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/142848" target="_blank">📅 18:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142847">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AB0IMl6YI43laCi3PokJDudkxZMcxX65rg91Dwdoji7C0ye3ZGDkJuaj4yo6INNxbZ2BTEW9A0MAp6JftdYpK2saGOOZBfoJyjK2RPI5k7rxagKmnaIl8r52SsH80hIvZlXuI0Iwtt0oTEkRyhKNVVg2RqlTp_CBjR-g7zAy0UfI3y1UOBkHA4NE44uGMtyc10joE3DNxmkQduXFG76U1MOYE2NEHrMJf0hkD0Luw3_7qJnOY9paLvyEEf6Po4m2sdX106coLO6ocVPnAJwNghoe4ZHYwSopjUDkXdUiGJR4AUYiTlkOPX5_RQut85S_G7FFIDBx0Yke0STTsf1gfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تخلیه کامل اسکله بندر المخا پس از حملات اخیر یمن
🔴
تصاویر ماهواره‌ای نشان می‌دهند که اسکله بندر المخا، که تحت کنترل نیروهای وفادار به عربستان سعودی در یمن قرار دارد، به طور کامل تخلیه شده است، این اتفاق در نتیجه حملات اخیر ارتش یمن در هفته گذشته رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/142847" target="_blank">📅 18:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142846">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f6dcaf8e6.mp4?token=AuvrdPoTo-bKkDZWC6PcQK7gfi60RL3gD3il_7DPKH2CeDBlGXEStFLEJKrL8ryT_fVNmlSD3wBJxx7fdpv633NaCo_u40dSinKuz1ASD6jwb8FYk9z0-bZJLyz6VUWm1v18gQ5YuVQh_kSSAWyCC-9kU9IlR027QznRi117eA7BbPHf3e4HHH_9iYGkWvEl85gz9lcOm5KB92amnEc6M0PD4-VXXCZZZw4nmEEukU8VqMbv45hWZn7NNZb6xloCQXt2bNzYfVdoCB6zxM_e5wcBasTkheMWA5i0_9wxQtpcY5QrJa4o_mlWY5qiuWsTqhAlT2hNdb1WS-rYjRu38Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f6dcaf8e6.mp4?token=AuvrdPoTo-bKkDZWC6PcQK7gfi60RL3gD3il_7DPKH2CeDBlGXEStFLEJKrL8ryT_fVNmlSD3wBJxx7fdpv633NaCo_u40dSinKuz1ASD6jwb8FYk9z0-bZJLyz6VUWm1v18gQ5YuVQh_kSSAWyCC-9kU9IlR027QznRi117eA7BbPHf3e4HHH_9iYGkWvEl85gz9lcOm5KB92amnEc6M0PD4-VXXCZZZw4nmEEukU8VqMbv45hWZn7NNZb6xloCQXt2bNzYfVdoCB6zxM_e5wcBasTkheMWA5i0_9wxQtpcY5QrJa4o_mlWY5qiuWsTqhAlT2hNdb1WS-rYjRu38Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انهدام یک پهپاد در نزدیکی میدان گازی «نپتون دیپ» رومانی
🔴
جنگنده‌های F-16 رومانی در عملیاتی ضربتی، یک پهپاد انتحاری دریایی (USV) را در فاصله چند صد متری پروژه گازی «نپتون دیپ» در دریای سیاه منهدم کردند تا از بروز یک فاجعه در زیرساخت‌های انرژی جلوگیری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142846" target="_blank">📅 18:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142845">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزیر امور خارجه لبنان، یوسف راجی، از ایران انتقاد کرد: مقامات ایرانی باید دخالت خود در امور لبنان را متوقف کنند، به ویژه پس از اظهاراتی که اخیراً رئیس مجلس ایران مطرح کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/142845" target="_blank">📅 18:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142843">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCeoLrROsp68g6VWeLCrbbl_7Q8tiIk8-VmHEGEawXITUJjYPY5W5N94tjluear4f-SJK7q8i16UF7GebedUsGs0qWmtDCqo8ZWlrTtIM1dhS8nmuk9kY8eFC_4Fff6iP_OfDwnVhBgSDZfHeLKOGJuEU2wZahINfuqz-YUjSMKOzSG0iBk68Nic4Aeez1ovHpJYnSCm6pztQngY-jGJi5zpiz9Gr-UjrJIbfTmNwnTHxlkTTS5yCXA8yhSrRBZsvn-on3y79P_mfOKWlSYVpi91j1atimjGpl2RQCs5H9rFzTjDGKm2rQneYtFN2ei0hMjL6vTL2R8wCN4ihvSY8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kg9Jg0eJJ-r3RYrtxoz49VVTX0krMn3XOX1WqmlsGgN3U3B-ugmQQ7tM2gkzILDKBTbvDn5lDb4oq2W_lK03i2O7k3Gjh2wPrOiwsy4T0xxls97-ZgMD_vaVhm4G718raA8efKrkvppvF_Qk2MyAktgd6loPG1LV2DfAisrkaaQrS-M2VT_o-0F_m4yf__xkDDuSHV9yN9naTkd0dKg4pMtDGQ_O7jYXaIl4d91fJNLcu2t57NUMka3ntt6xpkCsFvAgR9tzReuuJP7nWAP3bFhuPzDIh5hTR031q2VHzaGebEpsF2fNmvfW4CgTWD54tLsOEXUttv8G67vHUVv1LA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای Sentinel-2 از روز گذشته، یک ناو هواپیمابر آمریکایی کلاس نیمیتز را در حال حرکت در دریای عمان نشان می‌دهد.
🔴
این ناو احتمالاً یکی از این دو است:
USS George H.W. Bush
USS Abraham Lincoln
🔴
همچنین دست‌کم یک ناوشکن موشک‌انداز هدایت‌شونده کلاس Arleigh Burke این ناو را همراهی می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/142843" target="_blank">📅 18:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142842">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41cef2cdf.mp4?token=EYpHndUHi3rpdl1aLKozd4ickyx_8pO1fIAQCM86rERNxFn4hTa9-409vsbhNhv-JfWPoJOD7drOkLPfazuvqeL0e06FUp4TdBz71V2q1GHP8S4eCKyZ3AZzzteE745W83m9WN2RjyX8TK590MOQsZ56nrnxKJ9ECcNn0ZEWT7LHt2S443y8zU8xP3bv67Uy9QbQgxCQKgLP3p_clOSa02AF8KSwcFSt26GVKCFV-J9N-DnkpxiY7uKjGCyhLsjJhuDJH-j5HRMu31dm4WKodWqueW3VKjlX1wu-LBH6zIvmqA10-UNYTrFuN94DPQ1yqX7vzxMw9tni0KpF_as64Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41cef2cdf.mp4?token=EYpHndUHi3rpdl1aLKozd4ickyx_8pO1fIAQCM86rERNxFn4hTa9-409vsbhNhv-JfWPoJOD7drOkLPfazuvqeL0e06FUp4TdBz71V2q1GHP8S4eCKyZ3AZzzteE745W83m9WN2RjyX8TK590MOQsZ56nrnxKJ9ECcNn0ZEWT7LHt2S443y8zU8xP3bv67Uy9QbQgxCQKgLP3p_clOSa02AF8KSwcFSt26GVKCFV-J9N-DnkpxiY7uKjGCyhLsjJhuDJH-j5HRMu31dm4WKodWqueW3VKjlX1wu-LBH6zIvmqA10-UNYTrFuN94DPQ1yqX7vzxMw9tni0KpF_as64Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قیافه نقدعلی نماینده مجلس، زمانی که قالیباف می گوید؛ به نمایندگی از رهبر انقلاب به عراق آمده ام، سوژه رسانه ها شده است
🔴
نقدعلی چندروز قبل گفته بود قالیباف اصلا دیداری با رهبری نداشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/142842" target="_blank">📅 17:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142841">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
حوثی‌های یمن (انصارالله) اعلام کردند که دو حمله با استفاده از پهپاد علیه اهداف سعودی انجام داده‌اند، که در آن یک سایت حساس در فرودگاه ابها و یک تاسیسات متعلق به شرکت آرامکو در ابها مورد هدف قرار گرفت.
🔴
این گروه اعلام کرد که این حملات در پاسخ به نقض حریم هوایی یمن در منطقه صعده توسط یک پهپاد سعودی انجام شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/142841" target="_blank">📅 17:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142840">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fX_q8yQRQ65k5SesK93XJ4kpTUl6fkzAZFvo3thGlDig7zv5lff0aqZzIMZ0U4t-CCn9NxD_axV8AQIRhZsn1D6RPAd4cLThS31DklaW3XUkizWin6RUmJZWQd7Rn19AQ8xDgwvzarW4kFrsFevRp1B8HrBEdrFnPwqJgmych1x6vI9MPqleljr1EEkrup0Q-vVJ2tUNOiSaBTdWkF7v3qHymoyLENe0iZMesBCp9nWReiKfHS9_iw7mfS6fVR3F24SaxupaUW0hty9x1pdM_hut1YeXPt-cGs2yuO3uIm_TkI3rKTyo0hO7zWAUQRxHiBPJtB-uHR7IN0kOswR7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، از طریق شبکه اجتماعی Truth Social: جیمز براید، مدیر امور مجلس ما، در ماه سپتامبر از کاخ سفید استعفا خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142840" target="_blank">📅 17:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142839">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
به گفته دانش آموزان کنکوری، قطعی برق در دانشگاه شهید چمران اهواز موجب تاریکی و گرمای سالن شد که به سروصدا و به هم ریختگی نظم سالن جلسه انجامید.
🔴
دانشگاه شهید چمران اهواز میزبان هشت هزار داوطلب کنکوری سراسری بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142839" target="_blank">📅 17:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142838">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
پلیس گزارش داد: کشف بیش از ۱۷ تن انواع موادمخدر و ۷۸۶ هزار لیتر سوخت قاچاق در ۴۸ ساعت گذشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142838" target="_blank">📅 17:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142837">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7428f74560.mp4?token=PHwbemqSgBdNpJqb4tod_UGn9CGJZNJRc0pmS5WNQwYNUVHn8NUvnZEyFv0rG332upKbr_XS-OE3cJ_c8183jVatoMPNFLN1sV0rdn7I-t0Hkn-lQw03NwLOaMRLd7YsAQmky5qjhlPc4Aiym_sbmbEmmpFRV2EkR1iUyOpBHPhe1a_g9gInho5NRevA5KCnRyjaC10mmcurR4Tjd4YOkSMyA8-PSC1EIcj3fIRm8pm1ep-fMDZ5eEl5efwgSVz3CQFIdNsG6jym6M1SZGAf9t3_vhOLmFFSnWHWLZICS2Qvp6TftgrZeh8lwiCCt3sxknQ-GJsTUxEEx-S0CDRRAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7428f74560.mp4?token=PHwbemqSgBdNpJqb4tod_UGn9CGJZNJRc0pmS5WNQwYNUVHn8NUvnZEyFv0rG332upKbr_XS-OE3cJ_c8183jVatoMPNFLN1sV0rdn7I-t0Hkn-lQw03NwLOaMRLd7YsAQmky5qjhlPc4Aiym_sbmbEmmpFRV2EkR1iUyOpBHPhe1a_g9gInho5NRevA5KCnRyjaC10mmcurR4Tjd4YOkSMyA8-PSC1EIcj3fIRm8pm1ep-fMDZ5eEl5efwgSVz3CQFIdNsG6jym6M1SZGAf9t3_vhOLmFFSnWHWLZICS2Qvp6TftgrZeh8lwiCCt3sxknQ-GJsTUxEEx-S0CDRRAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش گرفتن هواپیمای مالزی در فرودگاه توکیو
‏
🔴
یک فروند هواپیمای شرکت «مالزی ایرلاینز» که عازم کوالالامپور بود، هنگام آماده‌شدن برای برخاستن از فرودگاه ناریتای توکیو دچار حادثه در موتور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/142837" target="_blank">📅 17:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142836">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
نایب‌رئیس مجلس: وقتی قیمت نفت بالا می‌رود یعنی ما برنده‌ شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/142836" target="_blank">📅 17:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142835">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRKPHkcdEz8eoBWiY2U3pAmJMsh9-C2Vg73wFnziDrg35qy0LHYQLffwYFd2J8wyjO0gsOb8H3ofUq8pnSWO10qaxZ9xsBDfv-Jv8VZtkRsFOOCd4xUemF66qD1rNBICnhKTo81JX8evIIHUlj2jd_AJA6ArwY93TD-sIKpKl49mS7g-dbvpvk_nxEYJe33ZtSGhuSo2BWaltfnZ7o2-ShGa-Ul22d8qfA0NLcn6lPoDMheruE9LTG3HhRXy48ijG7LkZl-0ZJwEryeimuAEBCSU551ZVJBCZ4F2Kzg3QbsHhTYxU73G1a34vSomHeqH0bmB3dJibDNgBFj1Vi46-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مرندی به ترامپ: جمهوری اسلامی فرعون را به زانو در خواهد آورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/alonews/142835" target="_blank">📅 17:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142834">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وزیر امور خارجه قطر: ما خواهان بازگشت وضعیت تنگه هرمز به زمان قبل از جنگ آمریکا و اسرائیل علیه ایران هستیم.
‏
🔴
پیامدهای جنگ علیه ایران نه‌تنها برای منطقه خلیج فارس، بلکه برای سایر نقاط جهان فاجعه‌بار بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142834" target="_blank">📅 17:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142833">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
پوتین: روسیه قصد دارد حدود ۳۰ گیگاوات ظرفیت جدید تولید برق هسته‌ای، از جمله نیروگاه‌های هسته‌ای کوچک، راه‌اندازی کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142833" target="_blank">📅 17:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142832">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRjhQIEccTGZbi3HVGYey3X0eQ3pkXSNoNc8xbQBLMjSRiMinXXM6FLp59F-kTdSAlay4fV5ex9PHzk629RQoSV9cKvxt4SlPbfRGZsWHhzWHz9pXUK-aTM27qpuFklNIoOhh-pC3Ip-8hvuaJRO1Nl0eZSzvbiTlKko97_EiUEeAvcyzedAfZXjD6hO2k8eFrJDKwx80uxR4ZS2BGeoxmWR-Qw58KxluCRbECDDTXJXf1gUpJ7mwku7RshniifIQdq7Ya69C3IC98kxFSDLtRvmuUYVvM5a4Af-uOGWFZl-by3uJzpnoMgupYEa3PhLC6lfnD3joTOLHHm79fheDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت اسپانیا اعلام کرد که موج گرما در طول سه ماه اخیر، سبب جان باختن ۴۵۰۰ نفر در این کشور شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142832" target="_blank">📅 17:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142831">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
پدیده‌ی «دوست‌پسر اجاره‌ای» به‌تازگی تو ایران خیلی فراگیر شده، مخصوصاً تو شمال تهران؛  قبلاً این موضوع تو ایران خیلی کم دیده می‌شد، ولی گویا الان خیلی بیشتر شده و دخترا هم انگار استقبال زیادی از این قضیه کردن. ماجرا از این قراره که بعضی دخترای سینگل می‌تونن…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/142831" target="_blank">📅 17:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142830">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t13fTNE1f7T0vZhxsmzl7FSrOlP4TFoZJqjhbJfrmMQXaEejgWIE-stctNAxdLB3dxmwaEtvYUkJB7hAUiTFwCa4mwyS5XravCG6ifN1xD5vU0JpoptsXiLnos0YY_91Z5z8dl3OO0Q8cakMTC8uYXgBwc-V7sVaO7hturFH_lvIbq7c6sCOBFWvaTzFlZyv5rTbJ320u91tpB8C_yG0Q7-bAinCgZitJFHfiqFGpzX4F5JZe-eSnDnXFx8cDfmPZBq8ZRMYteEsr7OKD6X5B7Yue_6HpDHnVCnU1tQss_Yfo9ClKGqiM1LlxbGcGN3jEulxzALyL7mM0VAt7np4Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پدیده‌ی «دوست‌پسر اجاره‌ای» به‌تازگی تو ایران خیلی فراگیر شده، مخصوصاً تو شمال تهران؛
قبلاً این موضوع تو ایران خیلی کم دیده می‌شد، ولی گویا الان خیلی بیشتر شده و دخترا هم انگار استقبال زیادی از این قضیه کردن.
ماجرا از این قراره که بعضی دخترای سینگل می‌تونن برای چند ساعت یه پسر رو به‌عنوان پارتنر و همراه اجاره کنن و باهاش برن مهمونی، دورهمی، کافه، رستوران یا خرید (ولی قرار نیست پسر هیچ خرجی کنه)؛ یعنی طرف برای مدت مشخص نقش دوست‌پسر یا همراهشون رو بازی می‌کنه.
طبق شنیده‌ها، هدف اینه که فرد تو جمع تنها نباشه یا با همراه جذاب‌تری ظاهر بشه (هرچی پسر جذاب‌تر یا خوش‌هیکل‌تر باشه، پول بیشتری در ازاش میدن).
طبق گزارش‌های منتشرشده، قبلاً رقم‌هایی مثل حدود یک میلیون تومان برای چهار ساعت مطرح شده و گزارش‌هایی از تهران، شیراز، کرج و اصفهان هم منتشر شده ولی الان گویا قیمت‌ها بیشتر شده و برای هر ساعت از حدود 2 میلیون تومان شروع میشه و بالاتر میره (بستگی به پسر داره که چقدر جذاب و خوش‌هیکل باشه...)
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142830" target="_blank">📅 16:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142829">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQ39Ol2p0gS50d-0_kC9wEPlpBU5Tk_PbR2OuisgVD9aOpaIi3oZMBW_84R_09NLHOHCj42b5oBE0VH_SUEscDq3dJLCWfaoKsm5r6xiQ4iOWM31zd4j0W9a1VaG6SAsd72MuBUsMdrDOUh2krCKu4F9MWlBOaP0donjSSd-HPMg6xIZXHvwhoFSzgCy5cdWZHQLWDuECnor8ujot3DdBiaR0Dvr29SGi4nzMDaDJ5-ryDHakB7uMaJ3h8-dWy_LmfMHc7mEqGgYeAZUmghrpP5spmGd9kDQLSyhBP0QyEOnRgFEYuH2xdcUFp5JR-_mYG1hGBEGg2ANMKoYork-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
چین میلیون‌ها بشکه نفت خام عربستان خریداری کرد
‏
🔴
به گزارش بلومبرگ، چین میلیون‌ها بشکه نفت خام عربستان را که از طریق یک مناقصه کم‌سابقه و همچنین قراردادهای بلندمدت عرضه شده بود، خریداری کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/142829" target="_blank">📅 16:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142828">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95183641d5.mp4?token=oT5_eytzZpXOQmUKwOjyOKrEUuVcM1Bl2YjrN0VSU3jKj7PvqzWl4dLum2_c2_6HqVpWphpq5pDR5X3Z0ccamJQ-IJa944AYYCep4l3C8-O9LBwVjHHz7rtaQIXcLfz4fhusRVo8MofYpw_aqrbi_UiixQjdPWZpY2Bu_CxTYdzWp8RAmJgHf7gtydnSTX4v3huaKdfZITXUeS7WLvfXD-lQHEpEoCn2Bvr4G9nkxszen9ooXt22_PznNLRuzvBgaEkxHYlGZmsLwKWp-63xkaqEDBr3kQRv1YiwjGGkbIfcrvg4K6frPrQJUvWR2cO9wpTbKB88NwBO0lvzyKAhXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95183641d5.mp4?token=oT5_eytzZpXOQmUKwOjyOKrEUuVcM1Bl2YjrN0VSU3jKj7PvqzWl4dLum2_c2_6HqVpWphpq5pDR5X3Z0ccamJQ-IJa944AYYCep4l3C8-O9LBwVjHHz7rtaQIXcLfz4fhusRVo8MofYpw_aqrbi_UiixQjdPWZpY2Bu_CxTYdzWp8RAmJgHf7gtydnSTX4v3huaKdfZITXUeS7WLvfXD-lQHEpEoCn2Bvr4G9nkxszen9ooXt22_PznNLRuzvBgaEkxHYlGZmsLwKWp-63xkaqEDBr3kQRv1YiwjGGkbIfcrvg4K6frPrQJUvWR2cO9wpTbKB88NwBO0lvzyKAhXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: روز اول اومدم دیدم نهاد ریاست جمهوری، استخر داره، گفتم خاموشش کنید
🔴
بعد دیدم به چمنا هم آب میدم گفتم خشکش کنید چمن چه بدرد میخوره
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/142828" target="_blank">📅 16:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142827">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142827" target="_blank">📅 16:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142826">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
یارانه 1.5 دلاری مرداد به حساب سرپرستان خانوار دهک‌های ۴ تا ۹ واریز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/142826" target="_blank">📅 16:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142825">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWHhM38iEpxidKBgEFfSAL3isjjEUROB21sEzPTkScB__vM5-g30Jw5JFob7LpZdOyA333S-JFLyL_v8MWYu0xUulhMJMxaIF_JvPKjDEB84yEueVs8pqPC1MEHvrerpfM9J_3eEHidMdlhNcb8l1TLYOGGa4Na8_OYOZZ6URiGdrgnhVN9hHpm9KG_EhYO0FhcHpmvC1d-VAAF40jxbFzHwrxfGixF8tU_vBM_6iB5IpP7fE1pwNz4GQHlLeAi-M6nTxnV5JCOIWq-L7rLbkEtoduICba90qNDDvO3k_rMiPwdLODu1UBB39jQPVspVBSzcZ4gBbA18h2AYHvDYTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۲۹ مرداد روزی که جنگ ۸ ساله ساعت ۶:۳۰ صبح با یک آتش‌بس پایان یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142825" target="_blank">📅 16:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142824">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGeDNSf80-VOpiWNwX7GWfqKZgDV2UzORVw8hIsnqtIuGMbgBDaQ9iIPQ9mcNcHRPOFIIPt0Rw1vNE9hcg86-sJB1syGUjPEm8LfBd86RkVO02ffa0mBFbN-LckMxsG-kN4FZnBOhCBjyLFnEYpgtZIyLBeZ0TpyOTaPjDzuRxBX2jYMhyoZxB5MzXh-Z1jTZw5f6EQbmQFKX1PZMvJr1Kot4kpzb7n-p5_KHRHJHd2CA6bgTorerNwOinK90BNA27RWbjSKn6Ves8nou02Nqk5-MhPJMM-kOrc6bOLkUjMOakRTssgn5ieDo20-Bx0WZkIIRz72GdaQ1T9qtZEQ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قائم حسینی از اتباع افغانستانی، یکی از بازداشت‌شدگان اعتراضات دی ماه پارسال تو پرونده‌ی میدون علیخانی اصفهان، صبح امروز اعدام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142824" target="_blank">📅 15:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142823">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvoiB81RfRXM5FppuDhzQoSc_qv1EfjPqoUyF_TU6ZR8nUOaNlgeFPUZMuAxC2VKeVbcTlCLQsb5fVfg-L5fQ4Ux88rmp8PWb0eV83G39lDSrXZ61Fw9olBjkDVbcbphyOXkDGz3H0gpzFu1avpSbD9vj42cOZ_tgBhrAZkJd5u2ONAoNFeovzmEeEss7M2TlDIa0xpR5ZkX8Ti7oAjz5FFF4Klk27g-ggcl-jfFLqkgcKvVjY6E1Q_aYi868m1X3dXQu74DDvsX6HHHWTKw7Hct-61OWm7lhfD9rQ8hzenYdlGvBUMIM9jhMQPR10Jf80U1j1SroRBfpsW7kja7ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
عباس عراقچی :
تهدید به «شروع عملیات اقتصادی» علیه ایران، در واقع برای انحراف افکار عمومی مردم آمریکا از بحران‌های مالی داخلی و مشکلات اقتصادی آمریکا است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/142823" target="_blank">📅 15:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142822">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDH0qIzSYi72pcyepINu-xBN5x7vUGRyaNOKCDbYSDJ0_cYDLC2OfLfY2vTk6luH85O_vlNi7EtGx8H9sVf53xyYro9_h4z2ZWcjSUD9-KeO0_3oGNJ8jZGAZllYDCoa8HgPK4odkTLCrL1YnVQoU31pjwjeAN4B1ZkYwDXSV6BHe9Uu_INMAUyg1FK-BXksLBOjLCG9iErd0X29o6kWfTHrw90tvdcHR3WOfWXHGBgYu2zCEUmZEBthhSftdNA5lVPiJ2iTRB8obpp1BxacInSTIMO2meeezBZjchnkJ7OiX5c4mrTePylNfoHC6ApLV_wOpyIvVjlQDsdioTlPhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس مجلس عراق در واکنش به این عکس قالیباف، از خود عکسی منتشر کرد که در پشت سر او، بجای خلیج فارس، خلیج عربی نوشته شده!
و خودش هم بالای عکس نوشت خلیج عربی!
او همین دیروز با قالیباف دیدار داشت!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/142822" target="_blank">📅 15:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142821">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6f667bdd.mp4?token=qDJoIJVVe-IbPFli43ab6OOyjfpppB52n7bf751Q2fuCaDQmGlzSsleH2vnvfGJUvXFemDvZ7RN5DpGSdVBacziMfCYG_5ZTIKeMOxpV1jz38zmplVz62jKdxPOsjzJ7Q2C-FhgEVAx55FA2M7Glbo7VY9s9C5benUifsQ-o1WgyxRg6Ad-slSfUm36KQFPUhph4Axk4trqsinrnPERUY5wIjATwlT2L5Nf52JYgoYrZeIkbwwe3N_TH65K8tEdpKRalZkUtQAanlrXJdxtMXPZHeNhGSl4fJqz5Ymq1Mvhmbg_M-sQQMEqcMFdlGE44nmed3KwSK8W6f0PodTsm2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6f667bdd.mp4?token=qDJoIJVVe-IbPFli43ab6OOyjfpppB52n7bf751Q2fuCaDQmGlzSsleH2vnvfGJUvXFemDvZ7RN5DpGSdVBacziMfCYG_5ZTIKeMOxpV1jz38zmplVz62jKdxPOsjzJ7Q2C-FhgEVAx55FA2M7Glbo7VY9s9C5benUifsQ-o1WgyxRg6Ad-slSfUm36KQFPUhph4Axk4trqsinrnPERUY5wIjATwlT2L5Nf52JYgoYrZeIkbwwe3N_TH65K8tEdpKRalZkUtQAanlrXJdxtMXPZHeNhGSl4fJqz5Ymq1Mvhmbg_M-sQQMEqcMFdlGE44nmed3KwSK8W6f0PodTsm2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رحمان قهرمان پور تحلیلگر نزدیک به عراقچی: آمریکا در حال آماده شدن برای جنگ فراگیر با ایران در آبان یا آذر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142821" target="_blank">📅 15:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142820">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏
👈
فرماندهی مرکزی ارتش آمریکا:
هم اکنون ناو هواپیمابر جورج واشنگتن وارد خاورمیانه شد و به سمت دریای عمان در حال حرکت است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/142820" target="_blank">📅 15:16 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142819">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a7407cb81.mp4?token=omnN9UcZvo9-HpZ4TMVaDjrQ492dtiduM1R7SVcwOMeco2q5OXKdVh7FHA5Vi-v4GWQSd86Hfl0UhuuMqiP3_swC5Fm7_pJ3ACsqBE70urh0CF71PotLfcUifUtH0LG24docj4vUuFjOWTeKw-_e0lMmBrPy0XYnuT0j3SJQWAQyoQjGqw0nISkGIbLdFd-lmQ8_3GcDr_X_prHxofADEYpFldn94yP-aFRW4JFm1d9Qoeb31nRcVkiX7A9X-TOH5Sx0YzkJnf2aCgK6hcaue0VoAdHc7_jy25yU0m-1uBVV9JMang5DEK3x47CKFMAg09Dv5nXA60jQ7VRIuoYg6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a7407cb81.mp4?token=omnN9UcZvo9-HpZ4TMVaDjrQ492dtiduM1R7SVcwOMeco2q5OXKdVh7FHA5Vi-v4GWQSd86Hfl0UhuuMqiP3_swC5Fm7_pJ3ACsqBE70urh0CF71PotLfcUifUtH0LG24docj4vUuFjOWTeKw-_e0lMmBrPy0XYnuT0j3SJQWAQyoQjGqw0nISkGIbLdFd-lmQ8_3GcDr_X_prHxofADEYpFldn94yP-aFRW4JFm1d9Qoeb31nRcVkiX7A9X-TOH5Sx0YzkJnf2aCgK6hcaue0VoAdHc7_jy25yU0m-1uBVV9JMang5DEK3x47CKFMAg09Dv5nXA60jQ7VRIuoYg6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
ماشین جدید رضا گلزار، تنها رولز رویس کولینان منصوری ایران :
قیمت این ماشین بالای ۵۰۰ هزار دلاره.!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/142819" target="_blank">📅 15:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142818">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15778d6d8.mp4?token=JWEAIoUzsAaHgex9LC8NUEUB0v6QCDiplUMIo63KIAHnHSqnJJJWbSUK9NivcZddhzwXR30S6A8Iv8xmHqRpLHPPaDXHSwS20XRSsmHieJU1Mb7jjGdwcm0YRmbtlBpujnVreoQGA1GINFCjXluMOcULeCqpLXKw8hanknro__5k6MtkTRPYmPMvXVU7rwga2qmLEkf65MKy8nZNHfRSUJetClIQxHdiIP2nfk3QmNQe2fmaSTNhJ9W2OUv2NcYnmeWx1bkV_s-9L5UYzAQ1KTVuzP8Lvt5B1fQK-7xk2qK5ddaW0EJWjzgPbTArigEU15K_aEtcWN7alIdSIt1jxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15778d6d8.mp4?token=JWEAIoUzsAaHgex9LC8NUEUB0v6QCDiplUMIo63KIAHnHSqnJJJWbSUK9NivcZddhzwXR30S6A8Iv8xmHqRpLHPPaDXHSwS20XRSsmHieJU1Mb7jjGdwcm0YRmbtlBpujnVreoQGA1GINFCjXluMOcULeCqpLXKw8hanknro__5k6MtkTRPYmPMvXVU7rwga2qmLEkf65MKy8nZNHfRSUJetClIQxHdiIP2nfk3QmNQe2fmaSTNhJ9W2OUv2NcYnmeWx1bkV_s-9L5UYzAQ1KTVuzP8Lvt5B1fQK-7xk2qK5ddaW0EJWjzgPbTArigEU15K_aEtcWN7alIdSIt1jxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرودگاه بن گوریون پس از بسته شدن و توقف پروازها، به یک سالن رقص تبدیل شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/142818" target="_blank">📅 14:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142817">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwqjMf_PgiQ6OioAytXDvzdBNUZbBv1VOfVn1E3hnRQdOuve_w-zwIfVZEe5MdRBBs0X7aZ5042oS_k_yzPVzqZ-yPQ6S4U941PmQLAYW2E15-5q35jGKmkpq2oQfxGjhIvuakfmvEDmVqifeo-l-6-QCuw1m84xhL7HxNcP-X4M6oU1T9-od-7uFabASTcYxbZmyc4b4lM7jGmT806Xomdn078dOnR7IJWQX42U0Vjtnho7OLJU8TnhkuMKVrQNZgPOp8_-viK_Hp_36tlY8EPtfUrpSeGqh1mddCiATkrhw6aP8ULyhrPXeXuEbMl2V8eI-3eULwUfDeJQylEIrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیشرفت نیروی دریایی چین
🔴
از 2016 تا 2026
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/142817" target="_blank">📅 14:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142816">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mC0a5nvycfovvvlaehcWFWPkCi-LDHtDWXZpnN-BZtU8tkaMevd5IpQ_Zch6AT5H_C3FY26meDv-Qwtdbg2RH7imZUbjq9vxxXs-tB0fpNAXXEG8JnXD7VNMdVQRvyTlfuxBSGKmx3UIk9qPWPKVqk1SXLQBSX-hWOySANkXxQIGkkrLnR3YP_qAelQ3HpsEO_hLG0Bnj-Auce1YiLdPuxNtJiJ9QCyejjaWK6q-JmFk9E50aaaui86ccUiawHcdPh0qDfjhqJOELun8ywi_ZNm-shOmsg6v9bS3-jolH6ljrT2sz4hmxlHcc8rC1WdZYTdrDMiH5yW8HKAB4kMWrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم:
باید حزب الله واشنگتن رو ایجاد کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/142816" target="_blank">📅 14:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142815">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzkWM_2L2z9EJUdvTxl66cqOSj2AkQKBvWvwOVWxxVSPuBrP79M3QUpjxktdkASqZwLNv9sV3nPUSUDKsxb2E9gbSWhELeKbL4DqBAUqFPVlQwdO4AUquJ6D-eo730VHKC7XcOl_hKkKqPpeB_JxoTHTucHd7paRa2lTdEUJtGgW7KKsUc8QpTwsEWLjz3Q9Y6Z0D19OpvgjKt43Vfk5DcZbhIFTXiSy6wDAsWm1xGvr25DXrG_AAap9FPDxXKedicy7uBFCoFVWCPAHB2IpdNuEJVstMqmCbu41eZYqqPq2zsKjWagYFqzyNH2o6kJ5g0y6KCWllomgZWSlwmS9gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خارجه مصر تأکید کرد که به هیچ کشوری، فارغ از اینکه کدام کشور باشد، نمی‌توان اجازه داد مانع دریانوری شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142815" target="_blank">📅 14:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142814">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323763dbb7.mp4?token=hSCnCcVmXICbCSjokr3pHvLETc2Hj-uL6KEvEhNqrkcBEhPJ68FMh96MCb9XIkU8i8rKCF8qmz9k8nmlZCAHNAKUcXLEJoiR3NvsKR5GF1WPuuzHcNgdK9AZ636xqa1mJPFj1tVXeJWg4GwVVVKFMi4ICoZvkGEsCQE3ze3w1hyNPLyJXdfwA0T5ryavQfCZ4PJ4PhutXrqXSKi9GFkRK7nZ6oaGJNMhbf2N6sVSihC0aDluZklVqkccy6gUit7kiW7o_vCML3aUrV0k3X61YGABz73elTdDxJZXmFe6iyJ0tukaD1x3ThFispti5BMHBN9SpJMnvJCtl_w13OqW_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323763dbb7.mp4?token=hSCnCcVmXICbCSjokr3pHvLETc2Hj-uL6KEvEhNqrkcBEhPJ68FMh96MCb9XIkU8i8rKCF8qmz9k8nmlZCAHNAKUcXLEJoiR3NvsKR5GF1WPuuzHcNgdK9AZ636xqa1mJPFj1tVXeJWg4GwVVVKFMi4ICoZvkGEsCQE3ze3w1hyNPLyJXdfwA0T5ryavQfCZ4PJ4PhutXrqXSKi9GFkRK7nZ6oaGJNMhbf2N6sVSihC0aDluZklVqkccy6gUit7kiW7o_vCML3aUrV0k3X61YGABz73elTdDxJZXmFe6iyJ0tukaD1x3ThFispti5BMHBN9SpJMnvJCtl_w13OqW_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
توی استان زنجان دو تا دختر ۱۷ ساله، این شکلی با موتور رفتن تو تریلی و هم اکنون توی کما هستن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/142814" target="_blank">📅 14:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142813">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزیر خارجه سوریه در مصاحبه با باراک راوید: ترکیه هیچ قصدی برای تاسیس پایگاه نظامی در سوریه ندارد و اسرائیل هیچ دلیل موجهی برای حمله به خاک سوریه ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142813" target="_blank">📅 14:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142812">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
پروازهای مستقیم بندرعباس به رشت و گرگان پس از وقفۀ چندماهه مجدد از سر گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142812" target="_blank">📅 14:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142811">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079a21a394.mp4?token=LfF0k8FS7lRjYHsTu4IgyLqku2uTC_javx1-KJKz5FsLS2L2Fg7IDgP5AnVUgAgsttYLgo3JI_y0KjOdr3G4r_BOE7FGVIXq8WaILTDWRP2q99EhJW8LDRr7I7t3ZQN-VoKQ3piScRnr0po3bl3wrrOcu9Orpn-lHStNiZk5wu6kOz--VIKwAWNDnWCuTriJo7yJcMdeKnuLAhzEulLgEQHvg424ITwrfu8fexUjw3nnCNP_VnvNgsPeuc5W4_YQqN2G7W8z2zS4KoVyXaQganyex9uIb3wrhLZbbkzIeyBFKoTePExTTSW9NSjchbWRNU6J4xK3iOwe8Jc-_g6eiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079a21a394.mp4?token=LfF0k8FS7lRjYHsTu4IgyLqku2uTC_javx1-KJKz5FsLS2L2Fg7IDgP5AnVUgAgsttYLgo3JI_y0KjOdr3G4r_BOE7FGVIXq8WaILTDWRP2q99EhJW8LDRr7I7t3ZQN-VoKQ3piScRnr0po3bl3wrrOcu9Orpn-lHStNiZk5wu6kOz--VIKwAWNDnWCuTriJo7yJcMdeKnuLAhzEulLgEQHvg424ITwrfu8fexUjw3nnCNP_VnvNgsPeuc5W4_YQqN2G7W8z2zS4KoVyXaQganyex9uIb3wrhLZbbkzIeyBFKoTePExTTSW9NSjchbWRNU6J4xK3iOwe8Jc-_g6eiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فواد ایزدی:
آمریکا در فکر حمله اتمی به سایت‌های موشکی ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/142811" target="_blank">📅 14:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142810">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b95291bdcf.mp4?token=W9S_tcjkqB9Ge1FvFJhdKkf0ZODfAlNoWL7iRK5MXjGyqXqJDrJV2lNQUV_QT5u-A5WwIlyqdQqiWJg2MbKO1gpMYIrdwT7VFCXozIVLHZpjxdGRBNspZD6Nq8aH1Zf5GcsguwVKM4Kf9u_6NihRsPsF_K5o-c7K_fihyGpryi57lCfGIqgXBOgoVNr8OMRd7dQytto-zLbzGSKuL42j9UewAIaqjudjFbgZYht2Txk5d0JfjOtBvpvhJjw840g18qPNavO8gCA9VmR5Xf6HtOAOfI90EiFoZDPxqzNg23ZUiHUM7w1hNkxY5qhdSCuEQ2LQBF8JUwtpXtFGIE9ofqftQtGbd4yrs0n_Csh4cTT7vWqusr4cmw9u0SRObOdaAQROC03bL44jGt4uYQu2fdgedKBPl12JxnhcZjZu6EdJI09SaxhkOlOppngZNVDKCZPo_vkvcxd2QhTMWPghOS6FoqpxOqMTd5LoVgPiexSFPQjEAlErF4UWWWy7CmOSgypPy6z-XpOUvP4gyggOx2E3UZFO4ht_4IOLEbCgH_wNtzeor45diT7yANIeLRW_tCSo6phz5QyxNujZpNz9OU68HaZmQ2c4jSOK8YFIaE2NkDkIiM3Fj9A8WSTSPz-pQpVdQgKeEQ-uOCGQLnwWv_NJokDFt0Lvon6h7BPNQzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b95291bdcf.mp4?token=W9S_tcjkqB9Ge1FvFJhdKkf0ZODfAlNoWL7iRK5MXjGyqXqJDrJV2lNQUV_QT5u-A5WwIlyqdQqiWJg2MbKO1gpMYIrdwT7VFCXozIVLHZpjxdGRBNspZD6Nq8aH1Zf5GcsguwVKM4Kf9u_6NihRsPsF_K5o-c7K_fihyGpryi57lCfGIqgXBOgoVNr8OMRd7dQytto-zLbzGSKuL42j9UewAIaqjudjFbgZYht2Txk5d0JfjOtBvpvhJjw840g18qPNavO8gCA9VmR5Xf6HtOAOfI90EiFoZDPxqzNg23ZUiHUM7w1hNkxY5qhdSCuEQ2LQBF8JUwtpXtFGIE9ofqftQtGbd4yrs0n_Csh4cTT7vWqusr4cmw9u0SRObOdaAQROC03bL44jGt4uYQu2fdgedKBPl12JxnhcZjZu6EdJI09SaxhkOlOppngZNVDKCZPo_vkvcxd2QhTMWPghOS6FoqpxOqMTd5LoVgPiexSFPQjEAlErF4UWWWy7CmOSgypPy6z-XpOUvP4gyggOx2E3UZFO4ht_4IOLEbCgH_wNtzeor45diT7yANIeLRW_tCSo6phz5QyxNujZpNz9OU68HaZmQ2c4jSOK8YFIaE2NkDkIiM3Fj9A8WSTSPz-pQpVdQgKeEQ-uOCGQLnwWv_NJokDFt0Lvon6h7BPNQzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امنیت ملی اسرائیل، ایتامار بن‌گور، درباره لبنان:من پسری دارم که اکنون با واحد شناسایی خود به لبنان می‌رود و می‌آید و به شما می‌گویم: او و دوستانش شایسته‌اند که ما بیروت را بمباران کنیم و آن‌ها را له کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142810" target="_blank">📅 14:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142809">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
العربیه: ۳ نفر از نیروهای سپاه پاسداران در حملات به مواضع حوثی های یمن کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/142809" target="_blank">📅 14:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142808">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
مقام آمریکایی: مذاکرات ایران و عمان شکست خورده
🔴
این مذاکرات به دلیل احتمال وضع عوارض برای عبور از تنگه هرمز و پیش بردن مسیری که جدا از مذاکرات تهران و واشنگتن بود، موجب نارضایتی ترامپ شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142808" target="_blank">📅 13:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142807">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuJ-9SmcnkMyaltMZ30-TjtkFliaK6F-mZqlAjkleIeSN0bgkAn3ezD7Y5uhBYOWgYCRFOLrbCjAyl0ThOyPq0bhWRBrjPEIgMboqsGBvsd48GKGVCEK-1KvL4xAkcYibdaTUGVGxouYdvzzAKHDTTi1K68UecPxeromvS77cmrV43DpndqqFT1cqNFb2JuZ0MA3Duqw2jtGnBqx4zYGhX60ZNuFTGxuHq-uQ5_i7Zc_rtb5Ne3SUON3JqM-42oUxtJ1AiDoJtnWTH9zdjqSZg27PDxbwnH6YO9RtY6i69nR_zNRZ7PJY05BVXxyjqyclzP3kzWSN29K2HUGIUQUFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش نرخ ۸۲ قلم داروی دیگر
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/142807" target="_blank">📅 13:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142806">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزیر خارجه عمان: ما با هرگونه تشدید بیشتر تنش‌ها یا درگیری در منطقه مخالفیم.
🔴
باید ریشه‌ها و عوامل اساسیِ بی‌ثباتی در منطقه مورد بازنگری و بررسی قرار گیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142806" target="_blank">📅 13:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142805">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a475b96a1.mp4?token=D8opmABSWrqFIQvsiADcnE8yPnelVXNlhS-r8eanfAW6_XwRRbO7Zh5f6BGlXsrF8KS2DGzw2CbpMZ0MqhwERfUyr96Y5HI5bqIAox75R5q_LwPzC6SR7rFRLHtrQVo4ZaHvdK1cW8MoFeNHi2_Dj4R3KZ1RsCOSpNLmxpnLPR0XMaLjzcPgI7XE-w_umGHhf9YT4L-c2HYI0lrgSLws0XSNTjEwLFpEmz1-aQp5QEN_Dpr2YSJdM1xvyGtGR0VSdimb4uo7jDG8pX-Icqrn-_D-k-5gFm_S673A_2Ur1jQC_ggSRPC3pGQbhdGxnDnAK4pGqqk9K41zZlHfrOsm6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a475b96a1.mp4?token=D8opmABSWrqFIQvsiADcnE8yPnelVXNlhS-r8eanfAW6_XwRRbO7Zh5f6BGlXsrF8KS2DGzw2CbpMZ0MqhwERfUyr96Y5HI5bqIAox75R5q_LwPzC6SR7rFRLHtrQVo4ZaHvdK1cW8MoFeNHi2_Dj4R3KZ1RsCOSpNLmxpnLPR0XMaLjzcPgI7XE-w_umGHhf9YT4L-c2HYI0lrgSLws0XSNTjEwLFpEmz1-aQp5QEN_Dpr2YSJdM1xvyGtGR0VSdimb4uo7jDG8pX-Icqrn-_D-k-5gFm_S673A_2Ur1jQC_ggSRPC3pGQbhdGxnDnAK4pGqqk9K41zZlHfrOsm6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آکسیوس: روزانه ۱۰میلیون بشکه نفت از تنگه هرمز خارج میشود و ایران هم شلیک دقیقی نمیتواند بکند و عملا تنگه باز است
🔴
پ.ن: اینم از تنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/142805" target="_blank">📅 13:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142804">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
یک حادثه در نزدیکی سواحل یمن رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/142804" target="_blank">📅 13:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142803">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
آکسیوس: روزانه ۱۰میلیون بشکه نفت از تنگه هرمز خارج میشود و ایران هم شلیک دقیقی نمیتواند بکند و عملا تنگه باز است
🔴
پ.ن: اینم از تنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142803" target="_blank">📅 13:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142802">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
آکسیوس: روزانه ۱۰میلیون بشکه نفت از تنگه هرمز خارج میشود و ایران هم شلیک دقیقی نمیتواند بکند و عملا تنگه باز است
🔴
پ.ن: اینم از تنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/142802" target="_blank">📅 13:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142801">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5tf3eWQWYbyHOo-C1r9FWnZwTjDapHIWGBsoXZ8tux4f3iZVc6PVPg-f_F_-R3cTpAbj4vw8YD9Hj_tT2qz_UxapVagDr4FDZk4xhx7jpYBSfWeDB0idtHaQCuhRpr0gm_kqeWTUjg2egnTnAsVtrd8zm3pzGb9YZIJ0uikr4iYBna04QbbS6AUqy-DNrhgH_xPIHCa77yBMKhzmO65D6XehkyGgXziD5dH1TAuZoaNid3zzVjsnvAUDmjbyGmUcKijScfovjh1fXCi5kXIV_z0u6hssn_BcNJ8UHnPTjvMwXcETOnsWDRbIpQpHIQmyWgpjk59tWEomMpPYB55Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک حادثه در نزدیکی سواحل یمن رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142801" target="_blank">📅 13:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142800">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csxkq7MzX2jPnWZZZX67v8OiazMwHRsQnjDXFJmlukRkIXqn5nzcRYdmY20amtSqPd3uu4Qku3nc7BG67MtGqIucfuczQRggQtlvuD_o0u3-ezSlAV_xYwfTlkGbflQMwn2ktx9WbioxfWQGxdxnunXvP8eCtWJUaAOl32z5rS93Rk8M_yJv1k8UH6YqO7uOBvEWDcd7_8qb5hbxprNmhPagyltZIGhcASdXy6wisQjq29fRmk0l1RnTjPV7yoESr2QcWrfjevFlfWQ9P_k_6Lcdc8qudpaqKD5AZ7T1G-AA6_3D7X5YzdJ2eUwhbGSkzlET3lir1g4gYfDUsp-L1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۹۳.۸۳ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142800" target="_blank">📅 13:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142799">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSS1omGigjYkGtP_Xsd9awUQPyVYsaftbjtnUfzzR51JOXDJZkkT0k17a_768wI50XMXwyvFx_A4UCKwBPGF8CVFC39OXRz-2Gpk8J-eWqn1khwtgs4BzOG9stT6LM34d3DZx8Jg_xFhbJfHcpvVilmKIOkkRZGScoc7jS2TigzpSbuhf6_DGc1zth2gEHAgC8OaUau2FSChYz-Z-z3I6QWGNkOrIXWc950r_fozY2o-JtAW_Dz2bS2oxyZU_SGTZh82xSbZevAaZkoerIvkAXnTDAh6DpD5yDj3WZa5U9eHj9dFcyTo6oUYjz5BdjaM0UTLDxGIxHZjK3Tq6YqQQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثروتمندترین مرد آسیا به حبس ابد محکوم شد
‏
🔴
بنیان‌گذار گروه «اورگرند» چین که زمانی ثروتمندترین مرد آسیا بود، روز پنجشنبه از سوی دادگاهی در چین به حبس ابد محکوم شد؛ پنج سال پس از آنکه فروپاشی این شرکت، اقتصاد و بازارهای مالی چین را تحت تاثیر قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142799" target="_blank">📅 13:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142798">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سازمان بهینه‌سازی: مسئله بنزین بحرانی شده و نیازمند یک راه‌حل فوری است
🔴
دست‌کم به حدود ۱۵ میلیون لیتر واردات روزانه بنزین نیاز داریم، اما تأمین مالی و دسترسی ارزی در مسیرهای جنوبی، محدودیت‌ ایجاد کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/142798" target="_blank">📅 13:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142797">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdTmS3F7DlIQCb5wNDiq2QvX1aHGS4Vp11Uh3yE3JyGMtJauxyb1eRNWvKMQdajlQZXNPdxUDOpanMVsdm5cg-2zBc0gVRKC5ZFA8MBUen-WJXPHBfmMQqKh7wdZjVDzvLri7zQy55BKAvUVGbgD55L9E96j7R7ApgZB4JATzrsRonv0dhX-9N8WXjEr4wtyclDq1XnlcUIY8dIr0p9X-kQsJHY3vuPlrBh5fZMQ1X7yeeT6n17MlIdstkT9BzVETQxKC6f9R-MGDa4HmV_ZjsQ0QH1a3o7ZL1JtWLGZvg8DC_WJ8MRuHhPz-AIkPYRgGf5AhrhpsUqyoepY1hm4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش لورا روزن، خبرنگار ارشد المانیتور به وعده اعمال تحریم های شدیدتر علیه ایران توسط ترامپ
🔴
ما کاری انجام می‌دهیم تا مجبور نشویم دوباره به تشدید نظامی روی بیاوریم (عمدتاً به این خاطر که موشک‌های رهگیرمان تمام شده، و شاید هم تشدید نظامی جواب نمی دهد)
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142797" target="_blank">📅 13:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142796">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
سازمان سنجش: میزان تاثیر معدل در کنکور امسال، ۶۰ درصد است
🔴
۴۳ درصد به پایه دوازدهم و ۱۷ درصد به یازدهم اختصاص دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142796" target="_blank">📅 12:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142795">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
قیمت هر بشکه نفت خام برنت از ۹۳ دلار گذشت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142795" target="_blank">📅 12:53 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
