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
<img src="https://cdn4.telesco.pe/file/jhWrHEXaDTewVdE73FgELzETTSfQ3LI-ETZeGK3gNg4Pi0uP9yal59u1pPDFG9oX_lpbn0ofCgfaFVyHfgUZ-r3K_x7XPF1FXToEJcWtHpvL_GIS7jLwFi82wz_uQ_n2PoHKb80ZP83-wdFm6Ba_jXYAs6XhOGrOEB2xssd4ulb1O2Ek3J4co0O53SMaScyRpwa7XDKEmGOdF7qAu4qwR7w5eI-T35odgi9RrOnAlVuPX1jqbLFp5cxDSriBQQocha2NZ3YMvDz8Z5PzeK5npMO70OyrE5wJASwCQPY--laJRE2eeAm3Ku0prJeqP6InbzFlwRI91l-oQ6XIs0Mr3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 992K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 01:54:42</div>
<hr>

<div class="tg-post" id="msg-139267">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/261b2bbe98.mp4?token=ZkCaymL2Q9s4XCVqtRmM_Mcq-YxypO7Z1QJA3rYWb9xlMbDwtibFkq6WUj-OwrwumFqkwqc4HKg2hbhNNWFrbte4JGxKHAelhHla_YZOxhFMMCcJwMZwSRnZtXFqKlKPeZR2FBLOetq1bLPOydbz07PjL2suZW5bSsULJEaB4rQMiZ3JauJ2GShMx2zrOlwiP9cc_wW3zdVHTM-K6Px1hLT08_kevo2WJTl6me-TsAYk4TstYtDLGTA80mmLzd8oJ_DpnntsYubKyfhcpHfpcbUMfYpY7pfckJrJN_disbrFWd2UWPXYVb-dcmKK5krERLQRI0aBXprMHiDzSVmcUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/261b2bbe98.mp4?token=ZkCaymL2Q9s4XCVqtRmM_Mcq-YxypO7Z1QJA3rYWb9xlMbDwtibFkq6WUj-OwrwumFqkwqc4HKg2hbhNNWFrbte4JGxKHAelhHla_YZOxhFMMCcJwMZwSRnZtXFqKlKPeZR2FBLOetq1bLPOydbz07PjL2suZW5bSsULJEaB4rQMiZ3JauJ2GShMx2zrOlwiP9cc_wW3zdVHTM-K6Px1hLT08_kevo2WJTl6me-TsAYk4TstYtDLGTA80mmLzd8oJ_DpnntsYubKyfhcpHfpcbUMfYpY7pfckJrJN_disbrFWd2UWPXYVb-dcmKK5krERLQRI0aBXprMHiDzSVmcUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراد ویسی:
اگه آمریکا به ایران حمله کنه کجاهارو مورد هدف قرار میده؟ آمریکا دست‌ کم به ده دسته از اهداف کلیدی و استراتژیک تو سراسر کشور هدف حملات هوایی و موشکی انجام میده.
1- بمباران مداوم مراکز نظامی سپاه پاسداران در جنوب
2 - شهرهای موشکی و پهپادی در عمق خاک ایران
3 - تاسیسات هسته‌ای "کلنگ گزلا"
4 - مراکز نظامی در تهران و بقیه استان ها
5 - سامانه های پدافندی و راداری
6 - پایگاه های هوایی نیرو هوایی ارتش
7 - مراکز و نهاد های حکومتی
8 - ساختار های سرکوب
9 - مقامات ارشد باقی مونده
10 - صدا و سیما
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/139267" target="_blank">📅 01:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139266">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
رهگیری در اربیل در اقلیم کردستان عراق.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/139266" target="_blank">📅 01:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139265">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
کانال 14: بیمارستان‌های اسرائیل در وضعیت آماده‌باش بالا قرار داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/139265" target="_blank">📅 01:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139264">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjqHnjcR5uf3oIy3GygNTD3QC9LwLiODWH5U3Uy05ZUY8iLR2pxjltYulc5UU2KxxO6S9e4iIAN5q8iqIvF2IMj2T9HIkp9eGZegLPtdb5c_9c3j7KcSs6IznPrb6MMfeEoKxAOkqwu_QfDOTKHhLLHMcLeaZt1mSE7Ak3mPPGfChd-l9UN3-ep_xu_M3_ZF7XSqLwP0b6IySZ8j-NzOSbJw2Qn4FQ_QH70Tiw0oTiLji32B9zHoXXe0Q0pYtde-uBa7Mda65MEkLw2m3_5BDoWueD3LTUaLtwb9dYJtpsThlzpvhoLOnY5VExqXAdzTAALNakY_oaxaFSIsA20snA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
سخنگوی وزارت خارجه به جای استفاده از نام «بحرین» آن را «رژیم جدا شده از ایران» خواند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/139264" target="_blank">📅 01:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139263">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQMX5QtQ8UTRTRE4mQyKD46-H5Nav9Mthuy1EJMI97ZtZTQMgnL5zuWwkErIrOhK9QU5vFg2b-zbk9mKZAAwu5INd-j5jz3MrrqNsfGXo9AOZhYHYbdX3PEfHYlpOOQsh0FXAzBeLFSuI_XY-k_S2qk_hilozCqW5d9wxu4s4DEvXosfaFe9VXjFluQ2r7RDjt-guboij3hXEn5dewsz_442W9Wuyc0KV-Rfrk8TYjNXXro4BX__yrRUtwavmLAQGpuSZ58rw3RLcVoNUozOqnK5E-EB8Lv9j-mKwq3B7YDP5SJ0Vlx67zyS6tACcnlmciV_4lXkvgEDgrH0ZvDLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سه فروند هواپیمای سوخت‌رسان آمریکایی از نوع KC-35R پایگاه هوایی شاهزاده سلطان در عربستان سعودی را ترک کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/139263" target="_blank">📅 00:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139262">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=rYDwWhsqGL22uSR42A9COlt7Xf8Oupon_YwyXNZZ95Z44Pvli4o4o1vI2LNs2HhrQx0y6qehVFqYDaPBuuvtWvCMKuv7O27iLJUdzAw3wOvA3QBUDOC5xw2dv_r_fiFfKhQ5DYIM6VVDmsJ5lOAZWBYE2_khIxZsg5khYOaIO3xl2Mbc8WUZooHFta0gXWtKmBQt_rRQlznQwsQ51EKrchsy2XfXkUT55gfhGzFy9ZPRKQbTU1CvtGfilTnX4Y1rZa4Za2IjgRDk3ooCYt4fubJDDwX2vXgaivssV0aFTtZMmpUcbAQmqMYMVLZ4qOqWEJEZKYj8Xwskdj4pIbEZWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=rYDwWhsqGL22uSR42A9COlt7Xf8Oupon_YwyXNZZ95Z44Pvli4o4o1vI2LNs2HhrQx0y6qehVFqYDaPBuuvtWvCMKuv7O27iLJUdzAw3wOvA3QBUDOC5xw2dv_r_fiFfKhQ5DYIM6VVDmsJ5lOAZWBYE2_khIxZsg5khYOaIO3xl2Mbc8WUZooHFta0gXWtKmBQt_rRQlznQwsQ51EKrchsy2XfXkUT55gfhGzFy9ZPRKQbTU1CvtGfilTnX4Y1rZa4Za2IjgRDk3ooCYt4fubJDDwX2vXgaivssV0aFTtZMmpUcbAQmqMYMVLZ4qOqWEJEZKYj8Xwskdj4pIbEZWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداسیما:
مسعود رجوی (رئیس سابق مجاهدین خلق) فرد باسواد و کتاب‌خونده‌ای بود و قطعا خیلی باهوش‌تر از رضا پهلوی بود.
رضا پهلوی یه نادون و کودنه، بنظرم مشکل ضریب هوشی داره و اُسکل بازی درمیاره.
تنها کسی که لایق این صحبت‌هاس رضا پهلویه، تازه در اوج قدرت خودش، چهره‌ی خیلی ترحم برانگیزی هم داره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/139262" target="_blank">📅 00:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139261">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
شبکه سی‌بی‌اس: جمعه گذشته، جلسات مهمی در آمریکا درباره قطع برق در کل شهر تهران برگزار شد، اما تا کنون ، هیچ تصمیمی اتخاذ نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/139261" target="_blank">📅 00:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139260">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c122b721dd.mp4?token=JMTrahZP5k-gCvCNMLno8EzB0YMxPAL6rMbEfdv9Uik9f-I0D_FJH8GYbhOii-wtkGOPApLOgqZ632PTVuYSgIldXcJRZ46ZuNQaS-RrHYbI-hWvNAsu6OgvG7gybhlDYbl5pa2mEVCx-UJcwVaQwxsH7VZVllShuNxV1-8eqye2g9fMATtHYAzLoHcAKNpoNGL2PhwEYIbunZxLoittSa1woeBQiO9ROFgpZD3o2tqxAmn3cB322y5lkq7aMwNu7fbxHZpZdMW5PwlHkS5aGH4BitSQx5uhdI1fqyvJ1Xm-Ox99XykeHfs9tVwlqYg6nAU3v2PFEj651gcqblCii4pXz_1VYPLCoa5V95AaNRnpoobAyXA_kqt4IUGEeYC_A-H2DH-TM5UeQmxANX9S772vPypMEf2drTihMpN1RkbeEZQkBKykoEfqdoif60nqMHBZJ1vTNPXW0Rvy2nH-1L-4S3F2hQXvkFulYWI2qKD4IbRdgqkkixkCvKVCGZCW4ZmNNGVRalX_7ouPEuhyar0U6IU0NR5N4FbXWDvjf6DyXlcHKVydDcxR23d0weuQbMXvhXKBzxVZuAFF3V1l_kZRKHh6o2IhoZBsvAlbQhdzmcQjntHkE7WfaV8fw-T4fxAO6E7k8cDVIBcXLMC-MG4GI3JJjcEKnSODlQ-DJo4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c122b721dd.mp4?token=JMTrahZP5k-gCvCNMLno8EzB0YMxPAL6rMbEfdv9Uik9f-I0D_FJH8GYbhOii-wtkGOPApLOgqZ632PTVuYSgIldXcJRZ46ZuNQaS-RrHYbI-hWvNAsu6OgvG7gybhlDYbl5pa2mEVCx-UJcwVaQwxsH7VZVllShuNxV1-8eqye2g9fMATtHYAzLoHcAKNpoNGL2PhwEYIbunZxLoittSa1woeBQiO9ROFgpZD3o2tqxAmn3cB322y5lkq7aMwNu7fbxHZpZdMW5PwlHkS5aGH4BitSQx5uhdI1fqyvJ1Xm-Ox99XykeHfs9tVwlqYg6nAU3v2PFEj651gcqblCii4pXz_1VYPLCoa5V95AaNRnpoobAyXA_kqt4IUGEeYC_A-H2DH-TM5UeQmxANX9S772vPypMEf2drTihMpN1RkbeEZQkBKykoEfqdoif60nqMHBZJ1vTNPXW0Rvy2nH-1L-4S3F2hQXvkFulYWI2qKD4IbRdgqkkixkCvKVCGZCW4ZmNNGVRalX_7ouPEuhyar0U6IU0NR5N4FbXWDvjf6DyXlcHKVydDcxR23d0weuQbMXvhXKBzxVZuAFF3V1l_kZRKHh6o2IhoZBsvAlbQhdzmcQjntHkE7WfaV8fw-T4fxAO6E7k8cDVIBcXLMC-MG4GI3JJjcEKnSODlQ-DJo4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک از حامیان حکومت:
از دار دنیا یه کامیون داشتم که روش کار میکردم که به عشق رهبر شهید فروختمش ۱.۶ میلیارد و خرج موکب کردم. اشکالی نداره خدا روزی رسونه. قبل از شهادت خیلی بهش فحش میدادم انشالله حلال کنه. الانم پیرو اقا مجتبی هستم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/139260" target="_blank">📅 00:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139259">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGWEO9s4fTTuTn49SdTwsdcxLAgx0WxhaLr7D7SR9s8kT9_sNRM957iYWDIJzriCO4r6vHotHXHZ2FLW0A_cYPjFhyJc1q_QEH8zEZt_BQqu4hABilBY15OZgByt7n6yaJlTY3WF62fb_y0EnlKg-AgIGBfSYAJ-tq0s09MsJmSJ_k3IkDRDTVEEJa6nvTuPa6y5kCFmo2w-HXxOZilQ01vsek-E7dKXkf07UrWO8891kSNjmjTmLlGimPPg9b-tUCnCKThdaw2TWMHNRKpZxxAT5WOZr2WBtgBcKxeMtgmQkOrJwQHDCaRK6RfteZDQl2tyRileCM5iN_h2Q2oxvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آیا رادار اف-۱۴ هنوز در برابر جنگنده‌های مدرن کارایی دارد؟
🔴
اف-۱۴ زمانی یکی از پیشرفته‌ترین جنگنده‌های جهان بود و رادار AN/AWG-9 آن در دهه ۱۹۷۰ یک شاهکار مهندسی محسوب می‌شد.
🔴
این رادار می‌توانست اهداف را از فاصله بسیار دور کشف کند، همزمان ۲۴ هدف را رهگیری و تا ۶ هدف را با موشک فونیکس درگیر کند.اما امروز شرایط تغییر کرده است.
🔴
نقاط قوت: • برد کشف بالا • توان رهگیری همزمان چند هدف • عملکرد مناسب علیه هواپیماهای بزرگ و اهداف غیرپنهانکار
🔴
محدودیت‌ها: • فناوری قدیمی و آنتن مکانیکی • مقاومت کمتر در برابر جنگ الکترونیک و جمینگ • پردازش داده بسیار ضعیف‌تر نسبت به رادارهای ارایه فازی • عملکرد محدود در برابر جنگنده‌های پنهانکار مانند F-35
🔴
رادار اف-۱۴ هنوز می‌تواند جنگنده‌های نسل چهارم مانند F-15 را در شرایط مناسب کشف کند، اما در نبردهای امروزی که جنگ الکترونیک، شبکه‌محوری و رادارهای ارایه فازی نقش اصلی را دارند، دیگر در رده رادارهای پیشرفته جهان قرار نمی‌گیرد.
🔴
برد زیاد به‌تنهایی کافی نیست؛ امروزه کیفیت پردازش، مقاومت در برابر اخلال و توان ادغام اطلاعات، تعیین‌کننده برتری یک رادار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/139259" target="_blank">📅 00:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139258">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db38e025b0.mp4?token=BQhLcf-eDb3HeAJdwHcRz4PFeGxKGQVRsQ4Y7p99TmO_AKVkuKn5jLpMXhPi6kSgi_4Og6D0McC9TnpaIri5tj_K_ct7iGRpFU_aNBJQ1iHJQZAjzqpHwh3tELLs3vLb7NcXKnAlewJcHYvJN-XNVEHwz8RSrwvDlqEV5pgoec0NhuWZN9GVogd3bCt4U6BdaMM5S5VrHSS0DJNtv9HV57CPS8fxPVcumswYhgPIYE4EL6pd2BvuQLV09ZOYMMbnX8XTBpcWxLlpOh9E7QWuF0_hi46l-oWc0hN792GohApdb86uPtHj_5jh6k1uN3o4g812SFXWVZhJW5iZE-JgzjW2aEtFqMLnXDkJfhimexLeExHS7UhQEbfKuj9QJJIqHpC40Ph5unmYAvDA0g6jMz5IdzKm-Hx4CUfCsh1ISSsspdqCuRWLrlODw3Lx60xeWjSMqv25_YdAhD8lIVg5CM-Pgh6UC617gFq2QP2o3ez8dH6e1GEN--1v7ww6rJFyrEwoMSb-MBjGUu2E1STbvISpEhDwBQmyurNqudF2n2H23tsDaLbkbyimH_d7hkA5JIO73cSvlTG8qm6sNMnLHsa2ouFJ8KM-s_mlxIo9Q79vS0CMxdNhB7Gv-DMLL05Hzd52rrDGcxpEO6rNBY6E9c-xfeDpjXK4AZPdehbhZQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db38e025b0.mp4?token=BQhLcf-eDb3HeAJdwHcRz4PFeGxKGQVRsQ4Y7p99TmO_AKVkuKn5jLpMXhPi6kSgi_4Og6D0McC9TnpaIri5tj_K_ct7iGRpFU_aNBJQ1iHJQZAjzqpHwh3tELLs3vLb7NcXKnAlewJcHYvJN-XNVEHwz8RSrwvDlqEV5pgoec0NhuWZN9GVogd3bCt4U6BdaMM5S5VrHSS0DJNtv9HV57CPS8fxPVcumswYhgPIYE4EL6pd2BvuQLV09ZOYMMbnX8XTBpcWxLlpOh9E7QWuF0_hi46l-oWc0hN792GohApdb86uPtHj_5jh6k1uN3o4g812SFXWVZhJW5iZE-JgzjW2aEtFqMLnXDkJfhimexLeExHS7UhQEbfKuj9QJJIqHpC40Ph5unmYAvDA0g6jMz5IdzKm-Hx4CUfCsh1ISSsspdqCuRWLrlODw3Lx60xeWjSMqv25_YdAhD8lIVg5CM-Pgh6UC617gFq2QP2o3ez8dH6e1GEN--1v7ww6rJFyrEwoMSb-MBjGUu2E1STbvISpEhDwBQmyurNqudF2n2H23tsDaLbkbyimH_d7hkA5JIO73cSvlTG8qm6sNMnLHsa2ouFJ8KM-s_mlxIo9Q79vS0CMxdNhB7Gv-DMLL05Hzd52rrDGcxpEO6rNBY6E9c-xfeDpjXK4AZPdehbhZQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤴
رضا شاه روحت شاد
🔴
یه ایران مدیون این بزرگ مرد هستش.
🤔
تنها کسی که به خوبی میدونست ملاها چه مفت خورهایی هستن که هم زندگی مردم و هم دین رو به گند میکشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/139258" target="_blank">📅 00:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139257">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👑</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/139257" target="_blank">📅 00:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139256">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAzgFaaxNqfTm0W0tAMJC1tjlL0e_zCO8u6eKG2j0t5AoJ_gFoB8L_xeOHxEGipBc8uWK96I4HaAyTecvyv568N_4gItF9JQoBR3wYY90qxKxVT7EUjAmkwO-AOo50skC52KJa3pjYPZ17emc4ElT7HUkDXWknkiFEyfpF6p3ezygQUHApCTYO1zyD8eQrp1o43Mvkjx_fjcXp8Uu8BonFvNqfYKWWmPO_zVJlVzoquqHXLxMfdk2tMa5ioM_Ju1YbqphiRQhge-h0P8PZ1Pbob8mkRmd32GF21tZlO7FneG4sTiO016uJD34XrmUGlSVT9L2y9JSajugqTAXHOKnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق اعلام برخی منابع پاکستانی، فیلد مارشال عاصم منیر قصد دارد به تهران سفر کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/139256" target="_blank">📅 00:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139255">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏
✅
‏فوری/گزارشات از پرواز تعداد زیادی سوخت رسان به سمت غرب آسیا  @TitrDaily</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/139255" target="_blank">📅 00:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139254">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
مرندی: پاسخ ما به هر حمله‌ای بلافاصله هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/139254" target="_blank">📅 00:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139253">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">یادتونه تو مدرسه همیشه یه بچه بود که هرچقدر میزدیمش باز بلند میشد گنده گوزی میکرد؟
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/139253" target="_blank">📅 00:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139252">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06d1c0174.mp4?token=nbu9lBkMOSMEZxpzt0FBcielwOECaEz24pg9BXa18L7DQ1qhxep2yojU8GhOpFLI2Gmm0ijU47lXnMaqbFesxmeo2xAL1LScKwFYVl-sBK9hP4ZYWx7c_crQGMNiqDqXV5LQ6Th7jnk-C7nrw3wdgshC9D76FGL9T9pkJdnB0kbUB33Ogbew3S7jotwGqHDw0OuEAxmDnbs5gzTOqR3Dq5XYhF3HVchsYJlyJ98dYb2iaF09x67A__V1TSprrB3RL6gbpTnXTdMAYoK0zj7eLBsvyCS9jAnkNZ0lpvZ82z981riXDPwImsjAtgTGSKl81hvPwUAbb91F_8XOAVINrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06d1c0174.mp4?token=nbu9lBkMOSMEZxpzt0FBcielwOECaEz24pg9BXa18L7DQ1qhxep2yojU8GhOpFLI2Gmm0ijU47lXnMaqbFesxmeo2xAL1LScKwFYVl-sBK9hP4ZYWx7c_crQGMNiqDqXV5LQ6Th7jnk-C7nrw3wdgshC9D76FGL9T9pkJdnB0kbUB33Ogbew3S7jotwGqHDw0OuEAxmDnbs5gzTOqR3Dq5XYhF3HVchsYJlyJ98dYb2iaF09x67A__V1TSprrB3RL6gbpTnXTdMAYoK0zj7eLBsvyCS9jAnkNZ0lpvZ82z981riXDPwImsjAtgTGSKl81hvPwUAbb91F_8XOAVINrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقتی ایتا و روبیکا رو باز میکنی
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/139252" target="_blank">📅 00:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139251">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
المیادین:
اطلاعاتی وجود داره که تایید میکنه گروه های کُرد دارن توی خاک عراق خودشونو آماده میکنن تا از غرب کشور به ایران حمله کنن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/139251" target="_blank">📅 00:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139250">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
خبرها حاکی از اینه که آمریکا، برنامه گسترده برای هدف قرار دادن نیروگاه‌های برق داره!
ناترازی برق۲۵ هزار مگاواتی، سدهای کم‌آب، نیروگاه‌های فرسوده، کمبود سوخت و تحریم، کشور رو وارد بحران مزمن کرده.
تو گرمای تابستون، حتی فشار محدود به شبکه برق، میتونه رادارها، پدافند، خنک‌سازی و ژنراتورهای پشتیبان رو از کار بندازه.
سیستم های موشکی و خنک کننده ها که وابسته به این شبکه ان، از کار میفتن.
و بعد از اون، فشار روانی شدید به مردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/139250" target="_blank">📅 00:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139249">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/139249" target="_blank">📅 00:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139248">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
عراقچی طی 1ساعت گذشته به تمام سران منطقه زنگ زده و هشدار داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/139248" target="_blank">📅 00:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139247">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifZ4f4APhnqH2tL7B0YS35j0MyoGAUww4ph9zx3gPbn5pNfxThrwF5lBCZu3vmifjh9Q8gG9dXtt6oPIEgQeJ8uJEtZtS6bk-srvFpOHzna8bBdMNWASmtW8Eu4mQpolwW26pmhPFfiqEniUUTLnduB1SjY2ft0Pe3pZ_BsJYiwVzjQIu9wsJl6w4_2mlc3N_JNTfm04Wuhx3YPLGOBSHHnYTTn4N35jl_TR69YQWpAuKwg549sIMj4Y9xuWykvZlVNRGM7t0QGOHkUOSl_CFlwAUfhMb6nmQLGFbh65-p3XqmVmCRf3RKX2E6jPkzs9HYL0e-G1nUXffEsGZscDIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت ترامپ مدیا: میتونید اشتراک 100هزار دلاری بخرید تا توئیت‌های رئیس جمهور رو دقایقی زودتر از مردم جهان مشاهده کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/139247" target="_blank">📅 00:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139246">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIGA5PkkRBNYXxHm3h737ZKt1nzmvQnVnB7iAKBBM4XjDAX2Vb9dkMgYye9rTKGugIYEHSThnewJ1RBSE5Ngj1rayX9mgl9kP9fTw1QzvyD4zD89QAxndUnLXa810ovIFND_c7P8iv_yoymhLL0z-GYIJpPMXGnlM4F2KjZyloEiPKVPJyuaWkLIPbD9ii5kTWSrtcqd1MHnVV3hSZ_KSijPdNWtsS-S52-r6FeKcw53qERnW56O8qu4xdmhd1lwjdI8SffhtPpGRV241MMCli5ZEEY9FZ1huxCak9145cUvuEmBJ6mJLWHd7Gviz9FvuEpieRO9yxh0_hvCI2wcFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
قیمت‌ها شکسته شد!
🔹
🎁
قبل از خرید، ۵ گیگ
تست رایگان
دریافت کنید
🔔
دسترسی همزمان به کشورهای :
🇮🇷
🇫🇷
🇳🇱
🇬🇧
🇫🇮
🇨🇦
🇺🇸
🇹🇷
🇮🇹
🇧🇬
❤️
برای دریافت سرویس تست رایگان کلیک کنید
👇🏻
👇🏻
▶️
https://t.me/V2RayMizbanRoBot
▶️
https://t.me/V2RayMizbanRoBot</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/139246" target="_blank">📅 00:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139245">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
هم اکنون تحرکات شدید نیروی هوایی ایالات متحده در سراسر منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/139245" target="_blank">📅 00:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139244">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری/کان نیوز: نیروی هوایی اسرائیل در آماده باش صد در صدی جهت حمله به ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/139244" target="_blank">📅 00:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139243">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
زمین‌لرزه‌ای استان کرکوک در شمال عراق را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/139243" target="_blank">📅 00:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139242">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d0d50aa445.mp4?token=RN7HKk8oookmFYKWR48UfZWK7WHRzhUtBUa5_wj2--5zwAfUDVaJqzliq3M9doOZrHuj34iMLtmN8A2u03ukVxs2P98unSynzkDhnb8OQwLjsRwyViUvegxs6AzSyaJieW853pVB9hJUNyBThStz1GrCG8RfZCHnmwOvfGIy1CHzX2YLLpY0sphUX_GOLca2ZxmU47JmaebDE2vxr0PxXvbNKeDQy1iEmZp0GpNKq2Dxxed4fuaXqhcR4I_E8IBMZCoO-wzf0NGvp5fYq5Pyt0DtWclNpo1Mce8VPkeUGxh_V04hlzofyWRmXW7toGfO1f-1eSXTLUC8p4tEtIaczg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d0d50aa445.mp4?token=RN7HKk8oookmFYKWR48UfZWK7WHRzhUtBUa5_wj2--5zwAfUDVaJqzliq3M9doOZrHuj34iMLtmN8A2u03ukVxs2P98unSynzkDhnb8OQwLjsRwyViUvegxs6AzSyaJieW853pVB9hJUNyBThStz1GrCG8RfZCHnmwOvfGIy1CHzX2YLLpY0sphUX_GOLca2ZxmU47JmaebDE2vxr0PxXvbNKeDQy1iEmZp0GpNKq2Dxxed4fuaXqhcR4I_E8IBMZCoO-wzf0NGvp5fYq5Pyt0DtWclNpo1Mce8VPkeUGxh_V04hlzofyWRmXW7toGfO1f-1eSXTLUC8p4tEtIaczg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کمیته ملی ضدتروریسم روسیه: یک زن با حمل وسیله انفجاری دست‌ساز قصد ورود به رستورانی در مرکز مسکو را داشت که پیش از انفجار متوقف شد؛ در این حادثه ۳ نفر از جمله عامل حمله، یک نگهبان و یک مشتری کشته و ۲۱ نفر زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/139242" target="_blank">📅 23:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139241">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
الجزیره به نقل از منابعی در وزارت امور خارجه ترکیه: هاکان فیدان در تماس با عراقچی بر تلاش برای پایان دادن به درگیری‌ها و تثبیت صلحی پایدار تأکید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/139241" target="_blank">📅 23:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139240">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
گزارش ها از تماس تلفنی اضطراری عراقچی با فرمانده ارتش پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/139240" target="_blank">📅 23:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139239">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hr4O6ikwzUXWuNSaQw8Zq_OCsJq4-SEIvRcuYI_YwQ80eHZZCsLYjJhH0ifwBm64WJjHccSmDsuw9CA1CsvR9ePQqwi2TTL5xpAGWPbvL6ekgLIWEdEd7LjRosfFsuRCMW0tk3FQlWqdxwCoeYp6l1jZaKGvRyXL9YF8ejJ_rh6stfq1YeQXueGSrExzjecmGI85wZTM2K6hiXZBFKmvCzHQ2mZ5EglRHlZx32_Tpi7u9Jl1ZXOfGFN5ggRoda7Zu3b8Ih9mBQkp1a0LfS80dfmUOeyTtOmTdyv-oxDn4B-v3Nyb6pvdu5t0E5ExO-qnza_HbFF6YbAr1crE9abD8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علاوه بر این، هواپیمای آمریکایی E-3B AWACS که وظیفه شناسایی و کنترل هوایی را بر عهده دارد، دقایقی پیش پایگاه هوایی شاهزاده سلطان را ترک کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/139239" target="_blank">📅 23:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139238">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhqXm2eTbkoUWYLxvqCFzWSKS9hRIpY8cIR1ZXDiGMprzOUYn6i4h8rVA6Ot5ch1KeWDxDTCXy0jIq_SMg0mBx-BMH2I5DilWeT2MxfXSkTbXIUS7si69My1yT1bQWZDRYN4KQdjmNRJdLjhG92G8sPzjRLZMonIKwnAJDM3rBubmuZzCzuijQcmRJRVEjwnW0qgsgHa3XjuMxyPwe5OOqXhZqTpzkiNTqyzcFprWvmGGLgDmVfZih12dqMvp4UyUdcoMTqiKBoHPQna1QJpQC96CAnTDwDcDGELmcz_HCXMWgsFsmF-ERMeT2u36tKWl7gujLqa52WMy3DLK7KvIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو فروند هواپیمای تانکر آمریکایی، فرودگاه بن‌گوریون را ترک کردند
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/139238" target="_blank">📅 23:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139237">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a70294dfc.mov?token=Z3wdU4cT4zoVpDIvVG-rQKXoXkBM2AYhEIdzmOu4MxAUORvIkSO_xYzD7Bbx8crp05Ti6r-U_-sNWaexgh97Ncp9fya_qhebAdk1Sfg8rv6SE1UdW9aDZa9S0HgzDAvfeN8cOtWzGN0VnYMnwEFKrfhube2D5RlJLNU5csxXPNw2mx_yKGfKJf6BFFLLCtadIdgt_VimKprNJfZ6ZN_r6vobltC13hnS46FdnN4A0SolEnDLqzsfVX3vXoEhyhXTSaOWaeW9vwgTWoLwiuWYhG9fkFQAIDHAe57Dkgf4R4GpzJy6AGQ9l-4ZdZM6MK8zs9C6HO1W45ZElhJuH3Eh_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a70294dfc.mov?token=Z3wdU4cT4zoVpDIvVG-rQKXoXkBM2AYhEIdzmOu4MxAUORvIkSO_xYzD7Bbx8crp05Ti6r-U_-sNWaexgh97Ncp9fya_qhebAdk1Sfg8rv6SE1UdW9aDZa9S0HgzDAvfeN8cOtWzGN0VnYMnwEFKrfhube2D5RlJLNU5csxXPNw2mx_yKGfKJf6BFFLLCtadIdgt_VimKprNJfZ6ZN_r6vobltC13hnS46FdnN4A0SolEnDLqzsfVX3vXoEhyhXTSaOWaeW9vwgTWoLwiuWYhG9fkFQAIDHAe57Dkgf4R4GpzJy6AGQ9l-4ZdZM6MK8zs9C6HO1W45ZElhJuH3Eh_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظاتی پیش گزارش شده است یک بمب در محل جشن تولد ژنرال الکساندر چایکو،فرمانده نیروی هوافضای ارتش روسیه منفجر شده است و چندین فرمانده نظامی روس کشته یا زخمی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/139237" target="_blank">📅 23:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139236">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
گزارش ها از تماس تلفنی اضطراری عراقچی با فرمانده ارتش پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/139236" target="_blank">📅 23:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139235">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
العربیه : دولت سوریه به عراق هشدار دادیم که اگه هر حمله‌ای از خاک این کشور انجام بشه، پاسخ متقابل می‌دیم
🔴
همچنین بغداد رو از تحرکات مشکوک شبه‌نظامیان نزدیک مرز باخبر کردیم
🔴
این هشدار رو مستقیماً به مقام‌های عراقی منتقل کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/139235" target="_blank">📅 23:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139234">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
شنیدن صدای هواپیماهای بدون سرنشین در آسمان سلیمانیه در شمال عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/139234" target="_blank">📅 23:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139233">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
اسرائیل هیوم: اسرائیل در صورت حمله احتمالی آمریکا به ایران، مشارکت نخواهد کرد، مگر اینکه خودش مورد حمله قرار گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/139233" target="_blank">📅 23:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139232">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBfaHuc5T725TnVh9NXbHBsLUpYFfN81h3-ERveA6eL1zPmZFItYcGqt9Rl-RV0pPZq9835OgeII-mwoM6X5AplVoHKUv61m-YFKoL8ofkPSmcfcbpJ6PhOkaiH-pRt_HCPydbknWMx0PUXNJ0f_unt6jjQC7rPsZhHuXkkpZiXMX-KYdSSEKTG4ebS8oJAReeyzvY4L_bfIuy2AhQ6fOJqXuAH0mMaaQxVj57kAXMmIRspLNAHFwoh74j88oMQ6pDkvAbuncLAexycjku-wxr_TH_d26B8M8a8y2NZ4Pt2qKpe9N5MCkFCYChE1W_Zd6JhctcuH7tyl6BVHI2M9Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار در منطقه کونین، شمال شهر بنت جبیل، لبنان، رخ داد. به احتمال زیاد، این انفجار ناشی از عملیات تخریب گسترده توسط اسرائیل  بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/139232" target="_blank">📅 23:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139231">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/112c8c980c.mp4?token=omfuR8Zvyp-rJYw5xOOlu8Yvw0-fJazYTGoZ8ACamw-hH9LWUieKB-TDPycMvAFzbnjuV8nibw3iceNFrlUqZ3G0IGqwbdMADhDhJqs1d7Y73w17l-O5g01S_ngt9zogqJMFqS7J933nPBvqIcfL3ZIRRFvMuMmGBc-ydXlHKio7_LqlBDly0SS1CfpzqoMnItAXeskF1RbqOTRVS0IzleDDyie8VxCuNgny6Pa-cXm3m2cletanjXm2sFswvxQ46smSlQShZltzUaWZiO580HnNlc6P6Y2QrP1jFQiCiBBjEaY-U28X0fUJq5kMjZfG8lZK7yGYMrWOkgAc-N1QAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/112c8c980c.mp4?token=omfuR8Zvyp-rJYw5xOOlu8Yvw0-fJazYTGoZ8ACamw-hH9LWUieKB-TDPycMvAFzbnjuV8nibw3iceNFrlUqZ3G0IGqwbdMADhDhJqs1d7Y73w17l-O5g01S_ngt9zogqJMFqS7J933nPBvqIcfL3ZIRRFvMuMmGBc-ydXlHKio7_LqlBDly0SS1CfpzqoMnItAXeskF1RbqOTRVS0IzleDDyie8VxCuNgny6Pa-cXm3m2cletanjXm2sFswvxQ46smSlQShZltzUaWZiO580HnNlc6P6Y2QrP1jFQiCiBBjEaY-U28X0fUJq5kMjZfG8lZK7yGYMrWOkgAc-N1QAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) با تیربار به سمت منطقه حداثا در جنوب لبنان تیراندازی کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/139231" target="_blank">📅 23:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139230">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjpdbzKivaeOA59ACxDPPVOy_qZLCG8KmgAFkSR9iE7pWxOGyOXNnEtWkp3ryZvueyOBEtHbXGXcZu9X7JMRAQ4v2XlpJibrGKaohFBUPVYQB1bODA_bwqQe880WS579LTagR4jvYocp0hkyhk6x6K9a5jzTKEJJH-bBJgI19gAWZ0x6Ic6Sun_FdUddOf5oOEzNebVg0edDiRdWa_OAJD3BiFkL2UZmUAeUTj-kGwY2KLnXVQofmdLsrYMt1jj5SxRUMu-ZoKRZ3oxo9g0NgwPRHMxg_WOCbmf7Jp9g5qS3IqKO3FCTG_VsPgRCFrjBJl1W47fzeTEQ5X5qCObHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: با افزایش تنش میان تهران و واشنگتن، تلاش‌های میانجیگری منطقه‌ای برای جلوگیری از تشدید درگیری و تسهیل گفت‌وگوها همچنان ادامه دارد و تغییری در وضعیت نظامی آمریکا مشاهده نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/139230" target="_blank">📅 23:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139229">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
هم اکنون حملات ناگهانی و شدید اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/139229" target="_blank">📅 23:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139228">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNu2O7OUefsZvt0bQnErZzB8-HK9IkooiLcB00O4LdjxCOBZ1uVHPvZyyybGK5-yWkG5cNGJtjvrmkrfUqz3sbY8mGToPKya0F3FGfQ6Gapw5NIj8CJy1ArXNqJN6R9bDjcPJ5AJaJIZYww8fM33zzuwCl2HCaPAV9fxCIYlOM0lfx2Jdfgm8fDKt0watzkW1EXZcLtFU_vDuCKqoE7NpJYmRFJPzicTk_bMn3ATgJ1H5Ifs7pQzIYHw31IxlXRkQ-pwNjT3Z5QQ1jdOzSgwZv_o3qoVZEltKqHnApu7HaV3fKmw9GE7BvI-EY03JpyboAdpf4ZDbDVkhRHvj-mAUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جواب خبرگزاری های داخلی به کاخ سفید: خدایا، حافظ رزمندگان اسلام باش
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/139228" target="_blank">📅 23:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139227">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4QpTK6X5CO6yKfJaJpACL9B9mbsvS6OqXmOsVtaJ-tWrMMd37q7MN3CSxGZC7IUv0NyAgoqhbJjhrid0z8LZyI8uIa4JGzmqiYEscu5G-CNtK--pok9hCzJ-unIRsnBddiHECwxHFL29caKKnDVQ89y6oNqSFqwV91XKTslumLakohBFo-y6FuC4QHdkQjUF9Dgy-M5gt8pV-JvST4bxgQQ76XJ9C5Fo-jTO4xeXGSjQZytFimQ_Ri5l7p7RXgkPBFuc14MiJw6ePjJkqivN4b6yYL6ZgD8TX9Jou45_Q9XfNTyS0bXDqBGNh8GJZlUpngm1RORNM7eRiUakdVlRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موسویان: شاید میدان آرژانتین تهران به میدان اسپانیا تغییر کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/139227" target="_blank">📅 23:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139226">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpAiN4YvAoIydxE515NTRiWybKZ5RyWb9z-6CWimC4iDFGYqAfh9gu973u60LdMUcewVx-XhVORQZgjAxSMQ_BdzxyHCj9-HsAa4qhitP2nCMD9a4bC5m0HI5RawMx_AtRSBKVJUm2j_KagtflhYNmq80XNJ1Gnc7DjD2GOtNkitYicvGeMv_Y-tDt2ngeSdyCEC4KAfANw6Zlbk7kjpCzuYIq3EqlQeRLXjvWNYH2pusVIPRzWnfcsnfuze8aMeLN2s4YAM4mYpzz8WqjAAu1gMXQuNKUxbaTdAWgrMYbMfxAHH6Eq4qk1hRp6VdDDtIVXs2x_bHkzi4VS49Ow_Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
ما به سوی میدان جنگ پرواز میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/139226" target="_blank">📅 23:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139225">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/awA7a4hJ6Vr7Wb0QWZJopsAoD5eEz-2HDd44HyRNyY_jyf21Z-xJTQQ0jw3djMovk_EvO6cR2qqS0LbsaK0Yo7MEFxRD2wgdAhixywt-DkLOka9ZopNfgmvBgO-rCfWGsdCzWzdHREPse1gPuhXsPaX6fscDwL-pLsSQu36ACLiOtnjGplQnEqPCBa3JFSccg4fZVENgOabLhxzhGl0w7H51GgY0qbVIsvKEFZWS7E5GBVZ11Nv98jU9liM9iG8-b1GnGWD2Yjr_ncEHZ8E_tMg0Tcice0hrGOmeJTA5Qb6KOLBxwCSd8RSO2Oi0sGyX8QbTyd2rlYHQMgmKFXWZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید حساب رسمی وزارت جنگ آمریکا
:
مرا بفرست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/139225" target="_blank">📅 23:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139224">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">امشب میزنه؟
👍
👎</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/139224" target="_blank">📅 22:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139223">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWdwnqB38mXwB23LPktmEtO0U6wiZHFGvGigZHxej6D-h0I6KM3fTTfg1G4CM_92nSTocQYBmJCFe4Ee6YdS73p7HWCtkvIg43IoF8kWqJm-JdgbROsiNU0ZdnDhh4Vt7W8bLXlMzUyr09qCsuDazEM1WNKEDdAARIGQhSgHGk45fXHxHcp3MeuiBgOfM2lh4PrGXZu1UezUmV5102s3xH5dZ8b5Rp0r4jXnFuv4HaHBqX2baBzlY0E2bRUPisLWrxD5ypdgm1Z75D4g3frUPJYffSU3lDRHzeNt4p6FiYhq-nkgUsdWzPOPVBGCILdpRU7UGyFy6ROD_WSq7QNZEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: آقایون بسه دیگه! کار آمریکا و اسرائیل رو یسره کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/139223" target="_blank">📅 22:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139222">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c29c1e71.mp4?token=kYSsu_LFSeaG_TyciCJs_zZehJcDFPq9-JEAm-73-ZGmMLDcRNtR01ZzwWI3oB-WsM8blCRSCZsNnfSlS0ZIvLq0Dd8gNnmwP0Kr6tPzYWWbtQNvwmXMTFUcOQVM8UhrRAc5g8PG9ZCazRCJpj-90vghxSu7CPD-mZKGm5XCuxe4ABqRopFc59-VQgKZZWcPbPLt-1fJ0ITftgdO0jqmykBg14UusyRL-dzjopLPolCG9yeqac3nkDVM8exYKcgHeXYhdGhw3WdM72SfRZfSoSgsACAbN0RlXc6Mplu-ZxAjkRXqnuz6uEFqm9BqP09YyXy9dvaybCuOCIGI3c3TXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c29c1e71.mp4?token=kYSsu_LFSeaG_TyciCJs_zZehJcDFPq9-JEAm-73-ZGmMLDcRNtR01ZzwWI3oB-WsM8blCRSCZsNnfSlS0ZIvLq0Dd8gNnmwP0Kr6tPzYWWbtQNvwmXMTFUcOQVM8UhrRAc5g8PG9ZCazRCJpj-90vghxSu7CPD-mZKGm5XCuxe4ABqRopFc59-VQgKZZWcPbPLt-1fJ0ITftgdO0jqmykBg14UusyRL-dzjopLPolCG9yeqac3nkDVM8exYKcgHeXYhdGhw3WdM72SfRZfSoSgsACAbN0RlXc6Mplu-ZxAjkRXqnuz6uEFqm9BqP09YyXy9dvaybCuOCIGI3c3TXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کانال 13 اسرائیل: ترامپ تصمیم خودشو برای حمله گرفته
میانجی‌ها که آدم‌های خیلی خوشبینی‌ان و همیشه میگن راه مذاکره بازه، حتی اونا هم میگن حمله‌ی آمریکا از هر وقت دیگه‌ای نزدیکتره.
آمریکا هم از طریق سفارت خونه‌هاش به مردمش تو خاورمیانه هشدارهایی داده که اینم یه نشونه بزرگه برای حمله مگه اینکه ایران همه رو سوپرایز کنه و برگرده به مذاکره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/139222" target="_blank">📅 22:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139221">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">به جای خرید طلا از پلتفرم های آنلاین که اگر مملکت به هم بریزه نمیتونید برید طلاتون رو بگیرید، توکن XAUT (همون انس جهانی طلا) رو از صرافی های خارجی بگیرید، زیر سر خودتون هست.  ترفند امن خرید طلا با پول کوچیک  تتر که خداروشکر همتون بلدید بخرید ( ریال رو ببرید…</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/139221" target="_blank">📅 22:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139220">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
روزنامه والا اسرائیل:
در ساعات اخیر، اسرائیل تمرینات شبیه‌سازی اضطراری را با حضور نیروی هوایی اسرائیل برگزار کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/139220" target="_blank">📅 22:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139217">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jl3NfW2Gs_whiMLeFIw6qTqVxz9jk7mREV6AvUaNPXZ5RlobsiNyUPEVvx2pcDNjg1jO2mqLM1rKtOdNjCdfHTK-DDVWHfXYkIchNky7UNdZZ5HTY0rCRbpJKuRU4xxoIQRGZIh1thrJebT6kF7u1QH5u0z1ujGV-LZyWS-jFDpvwsV6fntKPmw4avHmnMxuCwji3AAbGGDlgKtY7fK7VPVOwnt3lqUiZd_izKa5ODq_Y7dftFUIlWE79H34oPQtl604Or4DZ2_PgYzQdXRNzrhOEPyVGJjP4gDqRoaxmbUJvkpwSSrTuaeGBfk_ajTaLubpyGn62TU8nYIsoFv3Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XoLnG9H1SAXA-sMLMa-0H8gBKkqr-O0-bw39_G6MdkMtDy2whW5DlSF3njrdsYLpj8Pjko5bLhE6MPiF2qHbLZyxvyyHcByj9u66BBSmhgSyTRbEGJAWbDz8hszb14gviugefH7OohZ0jCxkiFWF5kSly7ndK03HKp0fCoZQ-bNOmJpbpg82glGLyQPvAxprSliqgtT1G7oi37PfViKEaWdnbiagsnFzn17sJjyWKHv0uo1m4_-8UvVpoSv8ylSxbURhswZI2PUUnWeENt8Dt5ScmdG5cgPDtprTbmHhtZbPxmaZaSf7TdYBJ76E1L2JJS-6G-GkkfzJ6Ma3ChqJLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mm07OFWTJDJYjfs-rFz--S6SVCnr8--_usRY73sTYlR4VXBtdJIQ_PBAIDAMxRpH_fu97Hdc1IbAEc514Cb5l3lSAPx6EoNpvPLh1KOmCEyHE5_qUGD6-UqVR9RWSumAkKyMM4emxV9G8Gs3VxaPaZYGIPkwOiaJ22ici1ha-OJTnz3TjD-y61bQbpfz3bvudd10eMEIyYeZSB6qRsU0h_028mu0Id0ALl6YTxamy-pitmmslrmJT_0SsmrhIa7IYx28WWU_SEQlTnECacGVqyW_J6-YsvWBWA1T7lQhvF7062tZe1Ba8i-jqpLUAEn-AV_xSJm1ymq8fw2RH1ZQrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
وزارت خارجه :
- برای دفاع از حقوق، منافع و امنیت ملی ایران، از همه ابزارهایی که در اختیار داریم استفاده می‌کنیم
- اقدامات آمریکا و اسرائیل رو تجاوز می‌دونیم و در برابرش کوتاه نمی‌آییم
- در عین حال، حفظ روابط دوستانه با همسایه‌ها و دفاع از استقلال و حاکمیت کشور رو ادامه می‌دیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/139217" target="_blank">📅 22:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139216">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
کامالا هریس درباره جنگ علیه ایران:
این جنگ، جنگی انتخابی است که ترامپ همراه با اسرائیل وارد آن شده است، بدون آنکه مسئله روشنی در حوزهٔ امنیت ملی برای ما مطرح باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/139216" target="_blank">📅 22:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139215">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPsVg5VhBkxCJx8SEiljabBRQhc-VhflSPn4pQE1OwRrKm8NGr8sblYkTxgnKLzj2jHT7wt4BJxaVEabj1xLQoYT3FWFW9pJRlyjBlrmhLpdMd9cy2mXliB3x88b83cJtS6Eeko_1SqlY7bXjB464Zi7jSprlDA3ZJAmV8-LGTzYD_hAwDs_TJrq25bIhea_cH7GNPuUeNIWOSu0HKZ47N-f08JiKp5slWKgMRZWpTT1hvOUgA4Mx_SEOPlGXFzrAMBfwqGp-zScFmjCTilofr5QT2kx7TRdBwU93xwLdKP19bx2HxzuzbNDc7N8UCGDWQV9lhxcNz3XgJupO5bb8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خضریان، نماینده نزدیک به جلیلی: باید بودجه فاضلاب شهرها رو قطع کنیم‌ تا هزینه جنگ دربیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/139215" target="_blank">📅 22:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139214">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت…</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/139214" target="_blank">📅 22:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139213">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R25gQCRABMI1WvWiV38L1TdL77OWZ2z5EFFhs6kWCmHpQioq5LpphH6lDhVCyj-SsmDfMyHl4L4CSRq_k5k6VM1NSD_89oT7JPtKAd6n-3dvS8t1SV428dAKkiMjbXpUSoaBiwo_wxMpK-WtlTg6IyVN5158U3PLe5kuOPBB2kylB5C-HzL2eSY60lI9L2DI6dzh03JubxC2pYzPiTq7QgLroWaXbV38j0SlCe6qU2dC0dHifP9PKp0DfS01tUjtRy8f2Qif1RKFsGSW6Tl2UXlxAd93vEZjsrhteFo6fpRg3w7I5h4OiDA_8L27zuNROfbhR91M1pG11pB667GTGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کوچک‌زاده، نماینده:
با لایحۀ جدید مجلس، مجازات نتانیاهو و ترامپ حبس و جزای نقدی می‌شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/139213" target="_blank">📅 22:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139212">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNEhRLwKa5JoORi7L4GaQXl_EZXHyH9oeSO2jhIQk8pmAj-GEzLcEdX2pr3Ko2wBca9BvctmpcJA4EMwElOV51p3cnlnckU6z8YJvofylCzq5T2Fejotl9LtUGXo5AWLsg2BAjRruZGG0n2y6fDhHTkb6vHSqqPw3vpjWSJnniBzLXwFIXKZnjWeiVARsJhnKWTMOMbGFcVrZRC9d2dJk928cPtWqQrQ0zTGlUeVbfDoAQd9L0-R4NS4zT0hS_qJcl8c8OqQmVpOhIyG6HTR2GdmETSAh5pENIIQRy-UhRXpxayMxecGDkK3KN2WyNTfQyVG56tTgMmu-3E_QrMFBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: هیچ هزینه‌ای بالاتر از زدن آقا برای ما نبود و باید تا تهش بریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/139212" target="_blank">📅 22:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139211">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAxmDveAN8gzw906diHS-60plNz-aC2vXGnTqPA_YE3f_nVX-xe_MlV4OM3j5LR1gBIzEgCgIbRlNgMiXCVqbsYWh32t6k943-5svongkBI51CpGDnEm5pk7vFNnxYFKlth6LeLmnRvoXF3gHPV0zRC1tjZQ8s5DKbM1tWAK6w6_lX_us4-d714H1EMRzxWf3mTyyAeHwLwP_kQ-moSq3nlJHrCi8ohx6PZ7A6D6rZ2p15hkxa6IgjowXOvLHmVvT6J7J5JZDxXZ45Cq0o32DUmbux1Z7FducTlmSgh7y7Z-itba2y-DTnK9K9SGEuXIje7nCxLQoUCogl0AI2aBjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اهداف احتمالی حملات آمریکا و اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/139211" target="_blank">📅 22:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139209">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRMNIh3uz96fthbr4nvKhA6nELY0inc6yiCpXY0eZ6bBsQuDROSiN9AF16S8xMKBaIyrnxV3GUgf63cAaGOVDYLNXKlj5WsqpMVSLnH8mRM5skaRckxqtOtfhNPa0HipabHAgfAUPrjlYnKa3zyuqpu7UjUAioR24WQvbv7iAdnyg2oC6vUAGDyIuB7Jv0XetUsI7dwNZ5gW68Zt-vTMAJ3rsTzE24k9G89lRvUGo6DqwX5AyN0deWFCTGBswpfOHaWlTTb7AhFKC5riF2xrMCWSPkDZof-Ve9D9kYW5zAFpNTqKzVc9Rh2aWiFVmsMiM4TJ5QAduYagcM8AhtMFZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست ترامپ: ترامپ برعکس عمر میکنه! (یعنی هر روز جوان تر میشه بجای اینکه پیر بشه!)
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/139209" target="_blank">📅 22:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139208">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzXQ0Cv19ySScO1VLPTzsXVhY6sNhjBsSBP4mb1N16nP55siohdpjGYGDN5oNMHHecIbC4oAhpoTBqww6_VLga75WFuHGkqH_vJEcyku29bpOsRt57gJ9oeJeLl5psw0DMspYoxIemS9eKOcea0cWRsKL8WFC06B60BMl_PGEWOBBA4hrAR8ngZLb5eZI8spOszgOxfVefLFd51radJiKrd_xSr-OSb17QaAswJgFOAEMp763TAyn3v-JKWwDBh_pFkCpWVzbCNVkfORVPE2HpSaCkXlC7CtD3btLBeDS1Ya2v7FgdKqIvNg0awsNBHoC3EQSpcJ4Ip7iPDGYJWwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلهکی:
ایران بنا دارد اگر «زیرساخت‌های انرژی‌»اش در حمله آمریکا و اسرائیل مورد آسیبِ گسترده قرار بگیرد، تا حدِ توان «زیرساخت‌های حیاتیِ منطقه و اسرائیل» را هدفِ حمله قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/139208" target="_blank">📅 22:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139207">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خدا بخیر کنه
🚨</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/139207" target="_blank">📅 21:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139206">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ: در حال نابودی کامل ارزش پول ایران هستم. در شروع دوران ریاست جمهوری من دلار ۹۰ هزار تومن بوده؛ الان شده ۱۹۰ هزار تومن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/139206" target="_blank">📅 21:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139205">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApcHPZB1NmYr_1-XzetOIWQwDVg0rzVnj2Y29ieZxbEs88Y2wUdA4Xc0I1RnbqvmW4ZKtyaRv_4-TEnrDBwYOfgEQpxlBoJCaKGOFhvyEG8kr8wj67BMPeZDdqg7ViaGvzRHYn97T-BRkmulL7uJW64u7mwhHZrGc2w49mN7TzdXl3MqtBUCloKatXZwbaSegJDgMNl7V7r7fnf0ue7szDi1tZfXeM94yCaBFyhi5c27U6WyyvtihM1e6sN8iRKqbTJXdMj2Xej9D0F932JoOTsXOyCCD2f5-_0U1BTkIzY8OZ-vQBD-TD-KdBBUaRrQdz8B56FEE1cJVSBQ56BZQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
در حال نابودی کامل ارزش پول ایران هستم. در شروع دوران ریاست جمهوری من دلار ۹۰ هزار تومن بوده؛ الان شده ۱۹۰ هزار تومن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/139205" target="_blank">📅 21:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139204">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnpxS3QUNDxkF7XxzS7jztt3oHcSKCWUvM3b4QU8t8e6T49Iu8bV9KJSDUcZS4WWKReDR_hgKCT_5j2xFfczo6qQr_XB-_vInas8EtPKx6G51OKiEwcxpYGoE78tiwbst3wTmqmSHoeUPdy1HmLCjqn6NNKJhHYyBeRyZoQuMdL2PX3MUKaE8WBwHK2uDvCVODc9nefp5elkuB8iz2DT3hW9jujWzZG51kA09RvVp1Ed5ei55LB5Pt47A22240Vg1KgjfdhmlZh-hbIdkSyjZ0Zlh5pVR65n82LuCJahS96Kxv-HvlsgL31I3kloSvsvIz4cgvxVrWB_HBAy8CVETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: ایالات متحده به اسرائیل می پیوندد و کنترل مراکش بر صحرای غربی را به رسمیت می شناسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/139204" target="_blank">📅 21:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139202">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1NoNquxftGhZ_8tia3dspydD7h7VNATwOz0h7HZJbi2ILwPwnQHgdoJ8LyiIoKKpwXm16C-ufhkwVCSD9OLnDQi-d6tqfSJo8uOvgpFvAQIBYsM_FENA8-0TxN5bU8By3WgqCSd7Wq8oJFhB7DNIVF8fzsiMh-EqRR8xjAceWRe30rAq12ALgxOuzRogeztP1ARWV5hM7OasNv6WigeH-rGj0tF3ZzRTo8SZrb52Xhfy3hsT_weqAy0h8E1LIx0gV4n0BnUHUu1Wc5CoEOZDx9UZe-nZRPqS88Hcexq9paGcyYd9fGv1EsSsivZQbbOVoOFgmVJc1J7dhqWBM_4lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eAw9mFfq3byox71e2BfeyzV0jPEV93MzT-1bssdZcDFKzzgmj5XNKcJmODRBDIJg-SacO4j4AKZaWuxkZW-6APb_FQJh85ZgDvCUl0YwYgjkwP0VzFEkOSEBoENi64tuPcL4hyre8WpFw0EyPIWUS7sFzyynuxuij7NaLWik-7iniMf2x8abrzq5MCYb5iHEyx6kiLYs3xTiaa6cL5AaigOtpMFnZcJwOn4jVvquHRY8w2bPky-G0dCJ89UzSvMkHCeCltDcBtMPYoNkSzTzydKeNEALx6pb6B_RBNlIbtwFpFd5951V0aow8fZyFXCVXRlgWqiXsFECkSpbVO8axg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ تصاویری دیگر از جنگنده آمریکایی و غرق‌کردن کشتی‌های ایرانی پست کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/139202" target="_blank">📅 21:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139201">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZckF5sTXxOBpjkPucTFBdAZsSNA_mbpvlWYH7BIs8lX4eVu_OIe2EAKSDVs4Z6W5G1Cm1ULnc_pGtbLuc3f8FxKsiU6KeD-OeGKQmcYQS5zHBAxSjxIPRZaKrRLozHksqbTr3QF5O1vQ0sF1hyG8QEzk_hQbHBsrhGzJXOJXEEbZplo8oZijcb1PjdQqiSTis5uUAiKt3ylzJEexwejmryLT8wiyNcv5OHpTVFBF1EvF58tvTjYS4f3yPoiuuxTTt83zbdC3TXMCNfn9kbmwNExIMCZAKe0EfsTzKizfjOQLe9ABu0ARqBbCjmDPmx3z_CBeATPtpIr2Zb66z6IQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ ونزوئلا رو ایالت ۵۱ ام آمریکا خطاب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/139201" target="_blank">📅 21:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139200">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A7XqWJKkbU-OpNKbpZjqZxP54uCqjq97sufqjsRDhP-4evfsfPI702WpugKBIdyTCX1RxOnwUQy0ZGUGge3SC0agyeNWfe4YFgI-3oTZORdmvzOrXB_1v8tmCkuaewUaA8sHg2O2fmkT6Bbgm3eZiKNd5FAze8751ofKFo0Mfx6MzIzPaPwltXYG5OHxE3xScgwuzsi97snIArOyUYQ6ib5DVBxkDZhUb404NM70W24PmMQ6eDt0Lace8AjNkD2oH9wX8HmwUULkKLOqk4AdlIzmpbPOOZU3kHzrLbyuBnc1vWwNPTkw4RiZFKBN0UKB8Hn7b-kKe4V2rB2lFNvBPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : تصویری از مجسمه "هنرهای ایثار" را در شبکه اجتماعی Truth Social منتشر کرد. این مجسمه بخشی از مجموعه دو مجسمه "هنرهای جنگ" است که در پل یادبود آرلینگتون، در واشنگتن دی.سی. قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/139200" target="_blank">📅 21:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139199">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
هاآرتص:ارتش اسرائیل سطح آماده‌باش خود را به حداکثر درجه رسانده است تا در صورت حمله احتمالی آمریکا به ایران، آماده باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/139199" target="_blank">📅 21:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139198">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
نفتالی بنت، نخست‌وزیر پیشین اسرائیل: قطر امروز برای ما از ایران خطرناک‌تر است. چرا؟ چون حداقل ایران آشکارا می‌گوید که می‌خواهد اسرائیل را نابود کند. اما قطر به مکان‌های نفوذ دست می‌یابد؛ دانشگاه‌های آمریکا، و حتی مقدس‌ترین مکان برای امنیت اسرائیل: دفتر نخست‌وزیری.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/139198" target="_blank">📅 21:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139197">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGwIJ90XUWPfhTsnqkqPxKLcAmm5Emco3lkrKIDa72FOsJlYaPKfuWB7MUbrqS-4tt0uMpzhphtfZUkQ9GO8xMbnsAh5xSuM0ZASKRtyrArW_GXcmhqkoOnVATk5yQhchRZPk7E_AvnckQ48AFSMUp2JvMPe4pc7jy6jG56OsCzG5F-ocNEvxISFBJlN8PSTAFhlbUW9ojeK1HofqTbllUu6E2_DtB-oBbmQ4hnfwXRGfGm27ug0-vs53wJ3WSnD5RPjKF66nXDV3yFSz88rVspdnIlLYh1HEnmiuWEc6N0jM6nt9074zfTbD2aKK4MgunSj4E1CxttYKT7XR1tdEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۲ عبری :  ارزیابی اینه که ترامپ از هر زمان دیگری به انجام یک حمله بزرگ علیه ایران نزدیک‌تر شده، اما هنوز قطعی نیست
🔴
تنش‌ها به بالاترین حد خودش رسیده و اوضاع در آستانه انفجار قرار داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/139197" target="_blank">📅 21:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139196">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jT43CeOsFghMiRslyAnyP4GTrsUZ6Rcf-EpMc3TFVAdXrgfIwxZDdPR9X44S9sFuOlxmn2zJr8WWw_HFsbBb-9gucT4HsxPeN6GXMLu6JzMZv8dPLWbNxDuDl08qnkFTf1s4zLLboxN60aOOXVZYPN-detanRS8sS4XkpCeOAnfy5XoWrvpGaXFmxuqJ8FI6dFySweRIFp2_78p97NfF1dTv_NZX184Rl0zXf2ZcfwFQ68rksdCbhcyShE2XucXNNyqhc5gh5erTxsiJmEKiWin4YqMxbuHdeatZRWJXK6L2no2TV-MDcMbDtiUu9wSzaW8SuT1fpgWSnoFDy47KqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای ناشناس آمریکایی که احتمالا جنگنده است از پایگاه هوایی الظفره به پرواز در آمد تا بر فراز خلیج فارس عملیات کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/139196" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139195">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
به گزارش بلومبرگ، شیوع ویروس ابولا در جمهوری دموکراتیک کنگو به بزرگ‌ترین همه‌گیری ثبت‌شده در تاریخ این کشور تبدیل شده است.
🔴
این گزارش می‌افزاید روند ابتلا همچنان شتاب گرفته و ویروس تاکنون به پنج استان گسترش یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/139195" target="_blank">📅 21:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139192">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9E2yvzkLhiy246hZNtffyid-ARyEsRy5166n0qZ0F3SIfEcmLjKKcmJSD-LwUSZcxfjDFpiXemXcbL2dQ-7I5_UQW9b0s7jy3gb0O9cxfCI8yzuBqt3g69lPHNfLqCK3AP8767jUGxezLDX_jCPX1HT5H3YOySwKxgfZGMt1j33jXJnQnciHioKTjlEby_7b8TSyBPwxjqZ-3_VVfNqR3qTYWTIfIbswOzlvMc6BorbNULlz1XwXa_S4BftGqlZkKKY8NQxyn3gawgC4DWNBh6sDXGu5kiVRfQX3oVIKxH41y0ou_qQGlqTnd1mKBr1voARG9UKaQdOA1ZFM8R0-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDAl5rQs1DDHADU01kL11odX9hiy-DyYqd2Y_FS9P5QCcONqfG0ZgWLXzzJ9ZH766lTNJvxhgYwWIc58IjCBaRbbSy9_KSnLrXCwIMaU_kY01HbevL_rGM-FsB6g3gHkEIuYU9WKb38UPrW2eDuEQJ2qSA5OnWylDGQbJixgi1hsuSQxbOOvGcw2GgTzcxwRMTm1TvZWUKGS65NJvvys5_KmFvlZjC2nsDDiYGtu_mOvwqptTg3yexc6nHR5KHwzOlF2YoOHW0sRqhhpWf1y1e5nNItlk28OSvchRe8eeyMJjXE4waTUXzvwYHoo_Tw5yA0J_YFgkgSqGXwkfx37ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nlHJ6eYsKnC70lg5ozP468Q87aMaP9F9HGlZ97PZGXQpDNXsQPdSMcUbjf7_Yf0HD6f7hkPRc8-c2aYLqKs0NAU_6KrqsboktmIlQ6u7XdwyUQ2_qPWJEpX4rb8Lo1tafD7HcPfSCTz1TSnDtR0TTAYutv5vKdb8dndE5WlmPlxVmmVUuDhdxBDMCCMUSruafairuO40qeM11BE94fD6EA8xpQ59J_Nr5gqMSUMo_ldwWVpVuPgXuL-Pz0hUOd2BsJcoqbejXSXigLWraiNWQ7u13846Kw_d2WU1Aj7nYBWI6xBeYkXKDZIfsm40ZhjNRUtyqglj4MG1otwCC6yL0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پست‌های جدید ترامپ بدون هیچ کپشنی
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/139192" target="_blank">📅 21:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139191">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حوصلم سر رفته بود این گردونه صراف رو زدم، 5 دلار داد
😐
😂
گفتم لینکشو بذارم شما هم بیکارید یه تستی بکنید ببینید چی میده بهتون
👇
https://r.saraf.app/s/agrd220</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/139191" target="_blank">📅 21:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139190">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTAm3EKYiOGqC9LY9S9sgAusZrg8DOGailxlvADLawagOLBPWHtPq9XMpR0mhxicmNdiF0z7yrDIOKZrnHF2G7Gwh6pvWtOmfuj6td1QdhlvjhzzHLZs-MOFulWBVS8TH2x9n0hVGmqiaO_mrwOGRsMc-EWdA2DBQTTa46dCwn8pv-ebFsqkbBQXbsX6NrP1fRVYTxAa_5TMS28sk0M1oR7mB6GfNCkex0tp6Hvlt8yQQk0C2OiRHOUGOPhA8S_gQaUAACqzu9Z6jw2wU3KD1uBhJxiy8P7YE91qw9VopsoXiq7_Id7WgKaNarXuLmQgoCknNC4zZMamqqJCwQvMKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لحظاتی قبل، وضعیت پروازی آسمان منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/139190" target="_blank">📅 21:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139189">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
یک مقام نظامی اسرائیلی به نشریه "The War Reporter":
اسرائیل از سوی ایالات متحده مطلع شده است که واشنگتن عملیات نظامی علیه ایران را از سر خواهد گرفت، و افزود که "این منطقه در آستانه یک تشدید جدی قرار دارد.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/139189" target="_blank">📅 20:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139188">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
مشاور تیم مذاکره‌کننده، محمد مرندی:
«شاید امشب آخرین شب از دوران عادی بودن در خاورمیانه باشد»
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/139188" target="_blank">📅 20:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139187">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
کانال ۱۳ عبری به نقل از مقام‌های ارشد:
انتظار می‌رود ترامپ دستور ازسرگیری درگیری‌ها را صادر کند و آن‌ها ساعات آینده را “بسیار سخت و بحرانی” توصیف می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/139187" target="_blank">📅 20:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139186">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
یک منبع رسمی اردنی به العربیه: ما به عراق پیامی ارسال کردیم مبنی بر اینکه در صورت حمله به اردن، گروه‌های شبه‌نظامی مورد حمایت ایران مورد هدف قرار خواهند گرفت.
🔴
اردن همچنین اطلاعاتی را به عراق درباره برنامه‌های این گروه‌ها برای حمله به خاک خود ارائه داده است.
🔴
انتظار می‌رود عراق اقداماتی را برای مهار این گروه‌ها انجام دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/139186" target="_blank">📅 20:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139185">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: تخمین‌ها حاکی است که آمریکا یک حمله قوی علیه ایران انجام خواهد داد، بدون مشارکت اسرائیل.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/139185" target="_blank">📅 20:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139184">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
فعالیت ادارات ایلام فردا و پس فردا ۲ ساعت کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/139184" target="_blank">📅 20:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139183">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVTJkOVfyigflP762KyOj6ypIj87y3pV7GEWSTxtnbIl4Q6_GIFSt0LDRItKg1bWmOD8IQKU88KE5yPOKGNth7-bil3PXmTReQDN7h-k5RFrHEbeBGYl23riN5y9CuW1IaOasl5xNW_papTx-obFZiJmF--5xMYorf7xtWC_2wLCg2f62XpCbHI3Py_jpYkK8xtafYe9igHtzNbge_ASlfNpqlyZsbh0GjOiTw7FLJtkXSwErU3Z2HK0sW0x3RYsKTfkj7_Ar9PG8IYrCYFACGZ6YcJmLla_mv8AdD-EgcXHP2Xh7uiFLtMyfiteiP9Fi8_wM9GvoA07AvyVkUVktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واشنگتن پست: ایران ممکن است منافع آمریکا در سراسر جهان را هدف قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/139183" target="_blank">📅 20:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139182">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
واشنگتن‌پست:
کشورهای خلیج فارس، به رهبری قطر، در حال مخالفت با تجدید جنگ با ایران هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/139182" target="_blank">📅 20:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139181">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjqwERJfmqzZgFKQYE2gT808cpbNP7oSj0OZL1sCKeugtp8sUwXF2P9AVTTvQfsW-Ba88GaQhSR1jM9sV3ZI7fN57RB8TyfIimzJzG38ndKzUALsWPdDqiCwN-qinEnfOhzDdORAZeieB5Ai2v3D9DrpitYSCtwfvJGb1K6O-MTyVgfDE0UmGM7i_nTBHW1szUCWpsILvuoliAJQBiA2LMcJIYkqpGJ-CBakvHeVIMbR-VnT_MJy-8syRimFwSOT_qrT7v_YFeH_PkUziCsCX5FIlW4TCQ9pbgQq-QNs5gAIga-6nb_p0SsUvMZy1FBzlaO-TLpQh0C0M1J5RoVSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : از طریق شبکه اجتماعی Truth Social: من به طور کامل با جینین پیرو، دادستان ایالات متحده برای منطقه کلمبیا، در مورد حوضچه بازتاب (Reflecting Pool) مخالفم. نمی‌دانم او به چه فکر می‌کرد؟
🔴
به نظر من، این یک مورد آشکار از تخریب بود که شامل چمن نیز می‌شد، که روی آن با حروف بزرگ عدد 86 47 نوشته شده بود، و همچنین سایر قسمت‌های اطراف.
🔴
ممکن است مشکلاتی با پیمانکاران وجود داشته باشد، اما خسارت اصلی توسط افراد خرابکار وارد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/139181" target="_blank">📅 20:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139180">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فوری/اکسیوس:
ترامپ در حال بررسی امکان صدور دستور فوری برای حمله به "تاسیسات انرژی" در ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139180" target="_blank">📅 20:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139179">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
تخلیه پایگاه‌های هوایی آمریکا در بحرین، پیش از حملات احتمالی و تشدید تنش‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/139179" target="_blank">📅 20:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139178">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
گفته میشه در بنادر حاشیه خلیج فارس برای کشتی‌ها دستور تخلیه صادر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/139178" target="_blank">📅 20:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139177">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
استرالیا با طرح شکایت قضایی علیه تلگرام، این پیام‌رسان را به کوتاهی در حذف محتوای تروریستی مرتبط با حملات «کرایست‌چرچ» و «بافلو» متهم کرده و مدعی است با وجود گزارش کاربران، بخشی از این محتوا همچنان در دسترس بوده است.
🔴
بر اساس اسناد دادگاه، تلگرام ۱۰ مورد از ۱۲ پست گزارش‌شده را حذف نکرده و در صورت اثبات تخلف، ممکن است تا ۵۴.۶ میلیون دلار استرالیا جریمه شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/139177" target="_blank">📅 20:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139176">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC7Sz_CpM7KFjHuMgm5CEF5udWfrCqsl79K8SOryc8etVpIQj0ljo_WjIHMFPFGeQc4AkujUJFtd4bjw02a3ZSMOL4_30b0dHRejlmARmQIFeG_HPyHz_B_hr657vg3Ho2xy5hFfvITPeHTPk-vAmtCIBQ-0vwcWJOYntiP8dgqMRO4Q1utYP6qqwPre8_mIiPVe7ELMdjEISbc_8MU1aorLoXJlzd9CwlErNT1LWG7FPTdh9ZmGzrxI7q9mjoB72RDVPv2Jv40OlqfymVVVfcGGcNpnpylVwHbZy3lqVrd8neZSJkNpORWtE4wuEVHqXeWBfW_ORy5qe_jRilW7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت ساعت پیش سنتکام:
یک هلیکوپتر CH-47 چینوک ارتش ایالات متحده در حال آماده‌سازی برای فرود در خاورمیانه است. چینوک یک هواپیمای دو ملخه است که برای حمل پرسنل، تجهیزات و تأمینیه در محیط‌های مختلف طراحی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139176" target="_blank">📅 20:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139175">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وای‌نت: پدافندهای اسرائیل به علت بالا رفتن تنش‌ها با ایران در آماده‌باش هست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/139175" target="_blank">📅 20:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139174">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16152d790d.mp4?token=kegcHYqFCfL4N8yhZFNvgmDHJIXEWm1C9f5vl27mPJl_gGp-IS0qrusAtg-JmpE6Nc2OVvKftldj3VxrvITbBC8_X1bRrYFo0lKsJZIwl8omFQQgkW-w4MBus8Y5oDjYpAY8BNkzOt2hI7vBmGdhIo1cmia2zyqmRVmsS3LiWb1P6KnQoPvazd4qvwUiS18i-OEJ8pkK3-Gcs9qhOHVXbYIALTh1aY8vV0nN6u-O1FAklGFzoZAUy_h7XHgN_NEIH9RM1w0BpyHzJbB1-N5EJbhZvHsFeEt9Yvralqb4ayVhcUX-2y6b00FC8anYDaOXI7HqPWPCqwrSYvnU9onjJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16152d790d.mp4?token=kegcHYqFCfL4N8yhZFNvgmDHJIXEWm1C9f5vl27mPJl_gGp-IS0qrusAtg-JmpE6Nc2OVvKftldj3VxrvITbBC8_X1bRrYFo0lKsJZIwl8omFQQgkW-w4MBus8Y5oDjYpAY8BNkzOt2hI7vBmGdhIo1cmia2zyqmRVmsS3LiWb1P6KnQoPvazd4qvwUiS18i-OEJ8pkK3-Gcs9qhOHVXbYIALTh1aY8vV0nN6u-O1FAklGFzoZAUy_h7XHgN_NEIH9RM1w0BpyHzJbB1-N5EJbhZvHsFeEt9Yvralqb4ayVhcUX-2y6b00FC8anYDaOXI7HqPWPCqwrSYvnU9onjJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
امروز تو بازی والیبال ژاپن و آمریکا  تو ست پنجم یکی از خفن ترین رالی‌های تاریخ والیبال رقم خورد. پشمای حضار و گزارشگر ریخته بود
🔥
آمریکا این بازی رو 3-2 برد تا اولین باخت ژاپن رو رقم بزنه و به فینال بره
@AloSport</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/139174" target="_blank">📅 20:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139173">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ارسال کنوانسیون «خزر» به مجلس برای تصویب
🔴
سخنگوی وزارت امور خارجه: تصویب این سند، زمینه ایجاد یک چارچوب حقوقی روشن میان کشورهای ساحلی خزر را فراهم می‌کند و مانع از سوءاستفاده‌هایی خواهد شد که ممکن است در نبود چنین چارچوبی، به‌ویژه از سوی بازیگران خارج از منطقه، شکل گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139173" target="_blank">📅 20:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139172">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
الی کوهن در مورد دیدار ترامپ و نتانیاهو:
🔴
اهداف هر دو کشور علیه ایران مشخص است ما یک فرصت رویایی برای سرنگونی رژیم داریم و آن را استفاده خواهیم کرد
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139172" target="_blank">📅 20:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139171">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از مقام‌های آمریکایی: دامنه حملات سایبری به سامانه‌های آب در ایالات متحده دست‌کم به هفت ایالت گسترش یافته
🔴
هنوز مسئولیت ایران در این حمله به‌طور قطعی تأیید نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139171" target="_blank">📅 20:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139170">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a34401b5b0.mp4?token=V6cm1fs8Fs6dogziIax0VnPW9b4eINqyeRWG7-P5HWLFEPHcemwlJDlwwbE2Mw20axUBX9KgubH4OIr5wRQeODr0XmQpRJ24dgbBoTngQvCkfGW4HJhKcpo_HPx5oUYXgEHFetdPvPJ4pBDcqUcjGPb_R0e9cY2wL72KFf7nCH1kfGV0O3kaWDvrfIbEXfWrGpp-mQ-VX9KtCrJu4VpnP2ZFKghWZAqo8z5Kf1N80QV7PfOJalsMw92kqtBLB-hsFxQYCHjz3Zjb0XeXQqzKU8URSNuL8EctfRWst0-pKteF-DEn6nBioGaNGcmy6hM0eXt5wqBY0ijuiSbSDW9YlXRUD0xcv_11D0oAXUs9L8rbyLndy1cWEXm8RZpsxmwWEcpRvONoAE5vtavs87T6eGfGUiwVc9LzigeOaC-PKacLEoc7hL-CUE8K6s2JDjFxx8hUXzXA99jBmZlKVaQKE-sux7Z7Ngbc-p5o-Oj1rFT8lprjiVxH2Uj4iF6VoPC7Y8uBpC9X5KQv3C8UEnPVAmJPOyic1eVKeFYxYDqoK9_ujkCaenD7yoTO1-w0fGB5hcDVMoLnRoONJfBIoM6gzhzeRD7iJ-JuWUDZwEK8kKFLhRhiXuueCzLyMp4HojYeIwJamM2hPOT4D2u5wqQ6HDP2hsKvukUvTxnH7B9umgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a34401b5b0.mp4?token=V6cm1fs8Fs6dogziIax0VnPW9b4eINqyeRWG7-P5HWLFEPHcemwlJDlwwbE2Mw20axUBX9KgubH4OIr5wRQeODr0XmQpRJ24dgbBoTngQvCkfGW4HJhKcpo_HPx5oUYXgEHFetdPvPJ4pBDcqUcjGPb_R0e9cY2wL72KFf7nCH1kfGV0O3kaWDvrfIbEXfWrGpp-mQ-VX9KtCrJu4VpnP2ZFKghWZAqo8z5Kf1N80QV7PfOJalsMw92kqtBLB-hsFxQYCHjz3Zjb0XeXQqzKU8URSNuL8EctfRWst0-pKteF-DEn6nBioGaNGcmy6hM0eXt5wqBY0ijuiSbSDW9YlXRUD0xcv_11D0oAXUs9L8rbyLndy1cWEXm8RZpsxmwWEcpRvONoAE5vtavs87T6eGfGUiwVc9LzigeOaC-PKacLEoc7hL-CUE8K6s2JDjFxx8hUXzXA99jBmZlKVaQKE-sux7Z7Ngbc-p5o-Oj1rFT8lprjiVxH2Uj4iF6VoPC7Y8uBpC9X5KQv3C8UEnPVAmJPOyic1eVKeFYxYDqoK9_ujkCaenD7yoTO1-w0fGB5hcDVMoLnRoONJfBIoM6gzhzeRD7iJ-JuWUDZwEK8kKFLhRhiXuueCzLyMp4HojYeIwJamM2hPOT4D2u5wqQ6HDP2hsKvukUvTxnH7B9umgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش پزشکیان به تاخیر ۱۰ روزه در  پرداخت حقوق اعضای هیئت علمی دانشگاه‌ها: این واقعاً قابل قبول نیست، کاری کنید که اساتید بیش از این ناراضی نشوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139170" target="_blank">📅 20:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139169">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VszP8knlkjk7yfwrIrvk2dsAy9OQoLF7ahkvtlIguu-X3-OLnNrnu_RWSWcGmHsxT5DVBeWL9899DhjVXQD3r-EcmJweLP6RPWE8Ogy0HbHgerSElU2PUbfZuaNArgdg_tbdGSkva0OMz_E7o6jknNJSbtbvr1NCLc72CXzXTW_dIEoiKjbX8Q_q5GA48St5NK_7FWvYTBYDF9eafuEYJX_ToERyqoDctznSEvGq4jYeyClOT-XnxbOh7y9z3WvctetmkdyQjOGaqYTgF43pfY-2x5ksYFnFjqYuJyADEh53Y_8KNPGBwhJ9hSb7bZ25KKoEs7I8Kg07S4kjnan16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موبایل سامسونگ A26؛
پنجشنبه 52 میلیون بود و امروز شده 87 میلیون!
فقط در عرض 2 روز، 35 میلیون گرون شده!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/139169" target="_blank">📅 20:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139168">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8e8dae83.mp4?token=sa9JvhvRyZn289LlF691Xs2xUj9YpAETXlFO4y-pTVVgfjwMPWJulB1Vs2bKXB29JiRPttOXYYGsWvmtzytuC1esH0_XrgsDFg0LJ2sTVRscIV3FqXOFQoQceXOjabD1_fQmcoDX8NwNjjc9Kiq9p4Jg3ogi37a0VwO5yFjucxVacytFHw70P6SqMVcB-4CEyjoHd9DvdLMqDT0EA-LSFCPZbOOBuhjsLcA7U2uOgl-3nadyOXPdu0INPTFwx5s80XdXMrCkJeWxnOC7B1prjLGAIHe7rn1H-myXjGZJAN8k_lwtM9pEkdDqp1YzAIeJQ-lDJamvzMl-O_5xuUror3Ds-aAkehNlm0ppsryo5XqMSHJqpj9plAgR2t_6S0vHdXHtl0KJRsirr6m9ydqK9zfS6l7-eyFXoq-ykoBOkgGZDIRqqniJLXtj0Yyq0w4PjK55NScblm2wbpQxXdp4CsxKbzx8Uc8_vZZbX31YG_OtOqLRgLhS3Bz3iH77YM15O8bnj-BXqonEBxDGyjO8Rb46V2f1vtiLunWXMHQBphWV_56uYsIeg0tmCSDto6w_e199SThMOZJ-Dlh8GgyGyNzLi7hQruOxJCcbdrr64jLQjrOxIOsUpESVJZPEO9ONVb_FUN2Bk_2RCutFy297asNCNTK6U3RhJPnIqO7iW1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8e8dae83.mp4?token=sa9JvhvRyZn289LlF691Xs2xUj9YpAETXlFO4y-pTVVgfjwMPWJulB1Vs2bKXB29JiRPttOXYYGsWvmtzytuC1esH0_XrgsDFg0LJ2sTVRscIV3FqXOFQoQceXOjabD1_fQmcoDX8NwNjjc9Kiq9p4Jg3ogi37a0VwO5yFjucxVacytFHw70P6SqMVcB-4CEyjoHd9DvdLMqDT0EA-LSFCPZbOOBuhjsLcA7U2uOgl-3nadyOXPdu0INPTFwx5s80XdXMrCkJeWxnOC7B1prjLGAIHe7rn1H-myXjGZJAN8k_lwtM9pEkdDqp1YzAIeJQ-lDJamvzMl-O_5xuUror3Ds-aAkehNlm0ppsryo5XqMSHJqpj9plAgR2t_6S0vHdXHtl0KJRsirr6m9ydqK9zfS6l7-eyFXoq-ykoBOkgGZDIRqqniJLXtj0Yyq0w4PjK55NScblm2wbpQxXdp4CsxKbzx8Uc8_vZZbX31YG_OtOqLRgLhS3Bz3iH77YM15O8bnj-BXqonEBxDGyjO8Rb46V2f1vtiLunWXMHQBphWV_56uYsIeg0tmCSDto6w_e199SThMOZJ-Dlh8GgyGyNzLi7hQruOxJCcbdrr64jLQjrOxIOsUpESVJZPEO9ONVb_FUN2Bk_2RCutFy297asNCNTK6U3RhJPnIqO7iW1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هر وعده غذایی که تو مراسم اربعین میخورن ، یک نفر در اثر نبود غذا و دارو داخل ایران فوت میکنه.
🔴
آهوهایی که در مراسم اربعین سلاخی میشوند برای جزیره قشم هستند. همان آهوهایی که رژیم میگفت با صدای موشک آمریکایی میترسند.
🤔
لعنت به شما حرام زاده های حکومتی که با نام دین هر جنایتی میکنین ولی کورین مشکلات مردم رو نمیبینین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139168" target="_blank">📅 20:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139167">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/121b4f43ef.mp4?token=YNLer4av89x5XMEMRVOHwiQpT2tfWCaSEHbSvK-NTPbVUc4751d1Nq1A7vg6uitid1Or3-FOWqkojRYwZllTSinn8QP6Pv2ImKtPGO4F9Wd6Vj-Qtte0kxlHJgirsbJ5OufxI5HErsVo1FuI6F2lfggCfwKHXHRauX4J3aXmCx2SAt7twIYe4rynbVzoZvRDhKdMVnQ9-pngTiY3C4JtyGXRefhYg2bN7a7M3xlBd7txOllFrVvihoVRF2WCU5fz8ImcQoCe8Kh3HSt_IbEDrkIOmWdY3w2vsPI-K-6JvbwruIHTh0ZI7AS9ljndGjI2F5sdg6EBalv5SriQ54NJgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/121b4f43ef.mp4?token=YNLer4av89x5XMEMRVOHwiQpT2tfWCaSEHbSvK-NTPbVUc4751d1Nq1A7vg6uitid1Or3-FOWqkojRYwZllTSinn8QP6Pv2ImKtPGO4F9Wd6Vj-Qtte0kxlHJgirsbJ5OufxI5HErsVo1FuI6F2lfggCfwKHXHRauX4J3aXmCx2SAt7twIYe4rynbVzoZvRDhKdMVnQ9-pngTiY3C4JtyGXRefhYg2bN7a7M3xlBd7txOllFrVvihoVRF2WCU5fz8ImcQoCe8Kh3HSt_IbEDrkIOmWdY3w2vsPI-K-6JvbwruIHTh0ZI7AS9ljndGjI2F5sdg6EBalv5SriQ54NJgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این ماشینا دارن خاک میخورن تا ما پراید سوار بشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/139167" target="_blank">📅 20:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139166">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
به گزارش بلومبرگ، ترکیه و عراق به توافقی برای تمدید یک‌ساله قرارداد منقضی‌شده خط لوله نفت دست یافته‌اند.
🔴
این توافق مسیر صادراتی را حفظ می‌کند که امکان انتقال نفت بدون عبور از تنگه هرمز را فراهم می‌سازد..
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139166" target="_blank">📅 19:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139165">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ارتش اسرائیل: تعدادی از عناصر حزب الله را در ارتفاعات علی‌الطاهر هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139165" target="_blank">📅 19:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139164">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16ccfb85d5.mp4?token=Kd4OsRb2aMOLjmwWP2_rr7p1k7zntCAqy9AKwxOjPjYJYN_FCykJ3SwvWqIBfdfT7KhD915LdqzAMe2ToLtHLBKZMimzv6RrLV8_jV4Iqwrw_8b_PM1mwswl9FMtUleJ87zi5i8KMF5DRB6MAxkmR02o3KNNCzDm-HxgDS2PZ94F2mOJcqJXD66ROpZYVRIXEjR0PSguQ_48cMn28Q9RflSvdXzByse8wTRezJE4ZRJb_Vul62kaNm3HmzIwnCS2HhS_vx45HP7YqCULYuKRsDL6xAw76E3d8n9QkX_CHDms9YKMHyrqE6vXu7Cz_z8n8YtCcQwU9ud5jfr8Q5cuNl11VvEQ9FaMkOk9j-Tb_uHJ6boVkCeGO4dB9rFSxbQBc3ekIH1uFxEgP82wDbIFObwRzwStRKBLcS5Y3nDFdC71HgDe6pVm0j2opakHHjq3mB8x56WBVZMmBKSIgE1G18jdFR6IUP_5upQVr6qtVEGV7DCQjLoMs-_nyZOiG_Ebu2oUPncETJMMWUZ5m-fwZDc0xURuQlC7gijohQsjTm0uMLm3CF1Uh7dC8dQjZnRHGVd9i7LtNLVtFckxycmU2funE1aADnh5afEZIW7cTTENdvB0D-cMrPhLKubKBfr7m8s6_MRA3U-HKh_gr-JkjeE_5STyrtfOU1y6GyUAfHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16ccfb85d5.mp4?token=Kd4OsRb2aMOLjmwWP2_rr7p1k7zntCAqy9AKwxOjPjYJYN_FCykJ3SwvWqIBfdfT7KhD915LdqzAMe2ToLtHLBKZMimzv6RrLV8_jV4Iqwrw_8b_PM1mwswl9FMtUleJ87zi5i8KMF5DRB6MAxkmR02o3KNNCzDm-HxgDS2PZ94F2mOJcqJXD66ROpZYVRIXEjR0PSguQ_48cMn28Q9RflSvdXzByse8wTRezJE4ZRJb_Vul62kaNm3HmzIwnCS2HhS_vx45HP7YqCULYuKRsDL6xAw76E3d8n9QkX_CHDms9YKMHyrqE6vXu7Cz_z8n8YtCcQwU9ud5jfr8Q5cuNl11VvEQ9FaMkOk9j-Tb_uHJ6boVkCeGO4dB9rFSxbQBc3ekIH1uFxEgP82wDbIFObwRzwStRKBLcS5Y3nDFdC71HgDe6pVm0j2opakHHjq3mB8x56WBVZMmBKSIgE1G18jdFR6IUP_5upQVr6qtVEGV7DCQjLoMs-_nyZOiG_Ebu2oUPncETJMMWUZ5m-fwZDc0xURuQlC7gijohQsjTm0uMLm3CF1Uh7dC8dQjZnRHGVd9i7LtNLVtFckxycmU2funE1aADnh5afEZIW7cTTENdvB0D-cMrPhLKubKBfr7m8s6_MRA3U-HKh_gr-JkjeE_5STyrtfOU1y6GyUAfHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ با سربازان آمریکایی در نیوجرسی دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/139164" target="_blank">📅 19:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139163">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjfD09u_qNtVYfQjN0kSRiR_xX58cDe7x2tbmqID5c4pw9tOAPE4iUBEIMvYOs9it_g31PRVm4Sin82OnOtFlxq-jG7gTBkY9wprp8V6H4SBtcqqzJhd_WqjZ6wERKnoERaw1956CkoybdqNYRfrB9cnpNWrXDPmn3w_XAKZUKaZY11l9BOHyOOmIk7NzEJmXoElPgvIBZ6bhZrFT_yKrOscJHgVE2N3hEUGs9pF4imzZ6FCpvfi32LiHFz1z1h0B3kjtBNfSngX3Ug9O59K1GAiNeFi73362VE4ajRSfayDubl8iYQfdEaXRnwcTekLY5nBO7C_Ms53e0IFgihRGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / کاخ سفید: خداوند سربازان ما را حفظ کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/139163" target="_blank">📅 19:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139162">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رویترز: انصارالله گزارش‌ها درباره دریافت عوارض از کشتی‌های عبوری از باب‌المندب را رد کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/139162" target="_blank">📅 19:27 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
