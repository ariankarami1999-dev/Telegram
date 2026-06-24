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
<img src="https://cdn4.telesco.pe/file/tdn0nNdQz1I-CRPn6gpL4ftYOHYtPunv4G84ObMTusyPIA4YKEfQs2t_CkkPj_bDR8O9lPJcotI3hyY219t-45s64ebtXNg2AbSICPhrp9E4lZfvz0hGPTDpcj-0mbriKuzbtvzlHoyA17VTchsYLFNA1kjh6kIgWk9SAP5y6-CC39pLAk6mUwEssv-ln6JqaTIcW7hw7mYEfYCSfm7of37GOErcym20yquEQHiRzkupaJUq8Z6InLkjz9vjjSHjDkQyXQn8_d61c31-GskcUv7n2Mm31dyhScHtppgiJRda2fQtiK4rm-UMzp7HPEA2PZe2FO0psAl7kELalLz-Eg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 944K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 22:38:16</div>
<hr>

<div class="tg-post" id="msg-130082">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
کانال 14 اسرائیل :اسرائیل در حال آماده‌سازی برای احتمال حمله دوباره به حوثی‌های یمن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/alonews/130082" target="_blank">📅 22:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130081">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0DGaSLjgxdxnqSn4OugbEFnQYTxNSCsC3qUACuKUckTQmFpfYRkUOr8Q6tnv1pAFhl6VLVHgEluM2EGArTCxk2eyc0IcXxRUyhvumu1hlSBm7W5ME1Xd_h9Jvzh2M0z_l4rAcbDGOIMC2xIqOyCmgIuZ_WE7cwUVf3bd2j6mOUfBNaYYoDSTz1J0ew9-oqfpnSIP9_sqm7Ay4YyS0CdlJb86-e5jvD-BS2GjCgkaYQUEKOO5n8PX8dCqihIlvhsBnvPjMTi77w3ABC4oLonrAx4BmLnXC80JJVqT9ja7tNICTqdipg1MeYmsCfOP2ujr39IN8d-1qJMHv6wItRyDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسخ مشاور وزیر ارتباطات به معاون آقامیری(دبیر شورای عالی فضای مجازی)  که از مخالفان بازگشایی اینترنت بودند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/130081" target="_blank">📅 22:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130080">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
در نشست ناهار امروز ترامپ با سناتورهای جمهوری‌خواه در کنگره، بیل کَسیدی بر سر تفاهم‌نامه مربوط به ایران با ترامپ درگیر بحث شد.
🔴
به گفته یک منبع، لحن کَسیدی آن‌قدر تند بود که عملاً سر ترامپ فریاد می‌زد. این خبر را MS NOW گزارش کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/130080" target="_blank">📅 22:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130079">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ: ایرانی ها خیلی مهربان بودند و هر چیزی که خواستم موافقت کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/130079" target="_blank">📅 21:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130078">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOfsLKAFk-hX-zlitWiLvP63hLZzHF22ph3RgSkDx43_glQfg5J4rJ0usweCTuEAuj70iw6sN-DKoe0Exk6zPA8Sb3laI6KkYODHeKE3j50a42dvbD44g9KHBunpPfEPV5hnLXTx4Nub1-uroOAm_TwPvyUtsEshjtJDcuGquzo-XkFm7GuUGZHUZ2vJH15iGRP_pzyBy30-SNufUcqYUXbbA1Pdec1G4eR7M8gN6Vih9f_oA802nKO3aIOGQWPeKy2Y5JzDXqNXEEtTyfUBYXCJu0eHkXCfIn0L9QT_iV0KAQt60qHMdo5N0qCySR317zQrmmkbXDE5_FyX8xjoAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کارشناس صدا و سیما: باید فرعون زمان را سرنگون و تحقیر کنیم و دنیا را آزاد کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/130078" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130077">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
مارک روبیو  در سومین ایستگاه از سفر به جنوب خلیج فارس، بعد از امارات و کویت، وارد پایتخت بحرین شد.
🔴
او در فرودگاه مورد استقبال همتای بحرینی قرار گرفت. بحرین میزبان پایگاه دریایی آمریکاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/130077" target="_blank">📅 21:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130076">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
وزیر انرژی آمریکا مدعی شد: بازگشت جریان نفت به حالت عادی به دلیل مین‌های ایران به تأخیر افتاده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/130076" target="_blank">📅 21:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130075">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
یدیعوت آحارونوت: فرمانده سنتکام به زودی وارد اسرائیل می‌شود و با وزیر جنگ و رئیس ستاد ارتش دیدار می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/130075" target="_blank">📅 21:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130074">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/450a87f549.mp4?token=D9DrBxqcxbSNCjNgVNbNsRQd91WMxhR0Vg1c5_toOdlrKWgJn1IiYkiu63uvG1KxQuuKGk96wEIJVJezArRxVMfKTIDM8vGzQju9oyPR2ofJXkxUW40_GqiC8cA0B9vcBUuLd56BddYKXqImNA7rcDzGVHtUheULAiUU1qNW1jDK6mOcrVhEXiDbjClcfylUWY4lx0xgNwvX_bh08Pnw_yZ3P0P4lYbnA8EcCNRz92hx4QZMkY5z_5uf9-zZBQS9k-p6iUHf2rJLqyOiGDc0srTOZ4WVTI1v2cs74J2Qr8AmXguyr0FVcxUBysNgkpByHoma76j69hIdfqEyhMY5nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/450a87f549.mp4?token=D9DrBxqcxbSNCjNgVNbNsRQd91WMxhR0Vg1c5_toOdlrKWgJn1IiYkiu63uvG1KxQuuKGk96wEIJVJezArRxVMfKTIDM8vGzQju9oyPR2ofJXkxUW40_GqiC8cA0B9vcBUuLd56BddYKXqImNA7rcDzGVHtUheULAiUU1qNW1jDK6mOcrVhEXiDbjClcfylUWY4lx0xgNwvX_bh08Pnw_yZ3P0P4lYbnA8EcCNRz92hx4QZMkY5z_5uf9-zZBQS9k-p6iUHf2rJLqyOiGDc0srTOZ4WVTI1v2cs74J2Qr8AmXguyr0FVcxUBysNgkpByHoma76j69hIdfqEyhMY5nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دسته های عزاداری تو انگلیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/130074" target="_blank">📅 21:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130073">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
تانکر ترکرز: ایران از ۱۵ ژوئن (۲۵ خرداد) تاکنون ۴۰ میلیون بشکه نفت خام صادر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/130073" target="_blank">📅 21:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130072">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز گفت که برای دسترسی به آن مواد عجله‌ای وجود ندارد، زیرا در پی عملیات «چکش نیمه‌شب» در زیر زمین دفن شده‌اند.
🔴
رئیس‌جمهور آمریکا ادعا کرد: «آنها با این موضوع موافقت کرده‌اند، با بازرسان موافقت کرده‌اند.»
🔴
ترامپ به فاکس نیوز گفت که بازرسان آمریکایی در بازرسی از تأسیسات هسته‌ای ایران، به آژانس بین‌المللی انرژی اتمی ملحق خواهند شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/130072" target="_blank">📅 21:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130071">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
آکسیوس: اولین دور مذاکرات اسرائیل و لبنان در واشنگتن بدون نتیجه پایان یافت و گفت‌وگوها در فضایی به شدت پرتنش برگزار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130071" target="_blank">📅 20:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130070">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
یک منبع آمریکایی به العربیه گفت: «در مذاکرات مربوط به سازوکارهای اجرای خروج اسرائیل از لبنان و استقرار مجدد نیروها، پیشرفت حاصل شده است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/130070" target="_blank">📅 20:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130069">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
خبرنگار: آیا شما هم مثل برخی از بخش‌های نهادهای اطلاعاتی آمریکا معتقدید که اسرائیل به دنبال تضعیف یادداشت تفاهم فعلی است؟
🔴
روبیو: من نمی‌دانم از کدام ارزیابی اطلاعاتی صحبت می‌کنید؟
🔴
خبرنگار: این موضوع گزارش شده. آیا واقعیت دارد؟
🔴
روبیو: نه، من اصلاً نمی‌دانم این حرف‌ها را از کجا می‌آورید. اسرائیلی‌ها دقیقاً می‌دانند که ما داریم روی چه چیزی کار می‌کنیم. تمام شرکای ما در منطقه هم باخبرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130069" target="_blank">📅 20:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130068">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ترامپ : ایران امتیازات بسیار مهمی می‌دهد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/130068" target="_blank">📅 20:49 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130067">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ : ایران امتیازات بسیار مهمی می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/130067" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130066">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
تلگراف: ترامپ ممکن است پس از انتخابات خواستار توافق جدیدی با ایران شود
🔴
روزنامه تلگراف به‌نقل از منابع نزدیک به ترامپ مدعی شد که رئیس‌جمهور آمریکا احتمالاً پس از انتخابات میان‌دوره‌ای کنگره، توافق فعلی با ایران را کنار می‌گذارد و به‌دنبال توافقی جدید خواهد رفت.
🔴
به‌گفته این منابع، ترامپ برای مهار فشارهای اقتصادی و حفظ موقعیت جمهوری‌خواهان در انتخابات، به توافق کنونی با ایران نیاز داشته است.
🔴
منابع آگاه به تلگراف گفته‌اند بازگشایی تنگه هرمز و دستیابی به تفاهم با تهران، نگرانی بخشی از جمهوری‌خواهان را کاهش داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130066" target="_blank">📅 20:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130065">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
مارکو روبیو : کمیته فنی در تاریخ ۲۹ این ماه (پنج روز دیگر) برای ازسرگیری مذاکرات با ایران به سوئیس بازخواهد گشت. به گفته روبیو، گفت‌وگوهای فنی با ایران دربارهٔ تحریم‌ها و مسئله هسته‌ای است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130065" target="_blank">📅 20:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130064">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
روبیو ، وزیر خارجهٔ آمریکا: تمام دنیا با هر سازوکاری که برای استفاده از یک آبراه بین‌المللی [یعنی تنگهٔ هرمز] هزینه دریافت کند، مخالفت خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130064" target="_blank">📅 20:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130063">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkRiDDKJjn0nDBQ9fyGuWvBQk_ww9CbsvGRt4bqLsaspbG-km-q2U2zK_g9NXy-1DuA0BrdVGCuKfbucRFXFD2o3KMiFslmE3L1xrmBeds7RJdBCTSaAq87K5NGZGJqr9NS6S7_yPyRQZGUuggLg1eI-mGlJddmANs173mTsEE69H_HQvrNWqhLDpr-lV6PYe1GyWBIVDwrQ8smlEedEl8WxVXCcw1lVw4m9Ss-N3DmqEiL4iQCGrAH9YnwY1BQUeq4wB-S--81kFIstzILySnfAjS-rXsto_e0K-AyEY9v-_p_WYPu1vGpx1WGVuE4jKU4MtXfweWu-mab2YLCpIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعاتی قبل زمین‌لرزه‌ای به بزرگی ۳.۴ ریشتر و در عمق ۹ کیلومتری زمین در منطقه انابد رخ داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130063" target="_blank">📅 20:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130062">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZq0z0jg6w24havMeIsXRHwDSh2BSQ5Aq6iYI-9Xbl49hMYRFM-LQL0vWo9pdZzGOpXigVUwVIGDJl9S-9_-Cv6KXYxCKgiqui7zZt2bEBnob9fpR3IqbuDMtcz-0RyBmfbaaUaG3uvZqcob31gucVBXLLK-94odiRvOcUgk7ayIbvZcIgqeaetxVvvdsyU1Ani68cVoaDbgcannEGzNbtU7-37Q-Ootv8mAotABeW156ooEA_ji57VnNBivKd3l7rLQrL2HqQ94uFeujaa3PuAXApe_1Ejj7DGOzGU5zrhM1UJ7qhilgJ1TOLRc_ZEJcF1qC6oshM8ecku9lR1vqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت تتر به ۱۶۶ هزارتومن افزایش یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130062" target="_blank">📅 20:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130061">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
شبکه سی‌بی‌اس: ده‌ها کشتی پس از اعلام عمان و سازمان بین‌المللی دریانوردی مبنی بر گشایش مسیر موقت برای خروج کشتی‌ها، از تنگه هرمز عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130061" target="_blank">📅 20:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130060">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
دبیر انجمن واردکنندگان گوشت و فرآورده‌های دامی: با حذف ارز ترجیحی شاهد جهش قیمت گوشت در شهریور ماه خواهیم بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130060" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130059">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtC3f8RHTfNrq2g1BNBg0ZVrrxLuqNfF7Rbz3V_pJVdQuL9iikOpPYsMj10t4F4NBFfvV40UV4eqxXZPRDjEENJlHeqDlhTvBpLwNl9xxU_Ir3AfPF_DpYTs7lGkrlXOyReZZhOMThTZZ72FUuXvSeJvIIDgcvXUGQmCo3D6SsZmS8zUCPBvBH4eXo7TtKYjvH3uWrxYXbX36m0QfNhKF7LqnJxXsXOJPIK1uVw5waXvDnEN-7-744m7JjSPx5Z0jY4v9eVhRC-4BkCS0iwtKH0ZNA05bPPwOGUJCmLz6UUKVY8e4gn3NL7DsrFAGNlYj1he48G1Byr3lNZxaG0HSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در سال ۱۹۹۰ میلادی، اسرائیل و ایران تقریباً سرانه تولید ناخالص داخلی یکسانی داشتند. امروز، سرانه تولید ناخالص داخلی اسرائیل تقریباً ۲۰ برابر بیشتر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/130059" target="_blank">📅 19:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130058">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
روبیو: ما گزینه‌های زیادی داریم، از جمله اعمال تحریم علیه ایران در صورت عدم پایبندی به توافق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/130058" target="_blank">📅 19:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130057">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmJS6DQwq0zS9BqVcKHQ1RBByxQ1OoeA3xq1EyidFUTi3XeRoSPLnvjEug3f2db_H_cwo0av8JSUiNYWYVHb43Jkx2ds2RqsjDL5_G2lapXLIWr3lqwMITZJvfdWiHVrHzI9xTR-lM0lL382HkWfDwAXUJRw-U8nDAdU46lvA6rAQpmw2xA4pj8OZk6V4WdahiSGMrlKKhQYkhHvK_i3m-b8qjV_8Pm5lOqg-UWTlmvwUlS0ulmeLNPw_Opfb2isrO5K-gsFK5zfrQjDX2wn9zoHdVzBbdAVelyU81gPWfjEvcoiPFBN_KbPft6ZTrHHeuGkdTdLZY-scQx6_Tofjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه حمله پهپادی اسرائیل به النبطیه الفوقا، لُبنان انجام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/130057" target="_blank">📅 19:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130056">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: نتانیاهو امشب جلسه امنیتی در مورد لبنان و سوریه برگزار خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130056" target="_blank">📅 19:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130055">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4FJQ7ONHsiR6cdmKomKI9rrp_9ig9eE_mxYdlEwI54mjycW7gdA2S4Rq8xV_Jg7db9W-xfZhfqfn1aj_aZeDg7xVBNqYywSIJ2WOlJjlK6qYKHf4qy0DjNUQIEi4ifjTvgX8HnmYs4sYfBjNPfpyMW-o3PCyL-dko_adQFL8g-DSadjgwyAVF-s8APkYLRLEhNhbHUhn-WjZP4uM89dRdoxnNM_yhPh7oqSCOlankj_bLp6yxWW80g6zk3_Qnu6NCVApqEg3NyafLRWLA2IwQZI3cq3zj60jTPBxv1Ij3Uuaqg5pTSelJS5LCEzdCuUpOSnvT26TU9Vj05YeYckdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ جونیور: قیمت‌های آتی نفت اکنون به زیر ۷۰ دلار رسیده است به دلیل توافق صلح رئیس‌جمهور ترامپ برای پایان دادن به جنگ در ایران.
🔴
قیمت‌های پایین‌تر بنزین در راه است برای آمریکایی‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130055" target="_blank">📅 19:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130054">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ابراهیم رضایی: تنگه هرمز را با مذاکره فتح نکردیم که با مذاکره واگذار کنیم
🔴
تنگه هرمز تا ابد ایرانی است، ما این تنگه را با مذاکره فتح نکرده‌ایم که اکنون با مذاکره واگذار کنیم، والسلام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130054" target="_blank">📅 19:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130053">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وزیر اقتصاد: در جنگ میدان پیروز شدیم اما جنگ اقتصادی تازه شروع شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130053" target="_blank">📅 19:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130052">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lY6MTSCVm0CA5siJgEcQaDMVgxN6B3UjIaEhFwrm9n253s36spxrLAkyQA2yQSOHsOzCNuSPkRvyX-8p_PjI7VMcgmh3mLsYlPbRfr0E9QGDYITiHXKU-L1NyYXBMnudCpmg1bEesvOEG13ZIl-yI4t2YWElDTSFtDFW6tec2NsxhVTau1na61nXQU5J2KVKpBBjHNuLRCq01I_XlJits5p582fGZ8ONwJpJ1skREZ9QSLDT_baR2xgIISvdKUZYZj7bHatchekhepjwxG-jyB7py70nTB7u0XJ29hzp58szhTQcOGP2EsJOHPkmlnFu_awFDH_cpJx8NuB8lHbj6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی: برنامه‌ای برای دسترسی به تاسیسات هسته‌ای مورد حمله قرار گرفته نداریم
🔴
معاون وزارت خارجه نوشت: هیچ نشستی با گروسی در سوئیس برگزار نشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130052" target="_blank">📅 19:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130051">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a25fe3090.mp4?token=W8mPHyhHKM4OQzOoSx9Jptd9TPqSFRTJgT1Wr9BktHte7Om-p3on_Eu7eeCyhMt76myPmuh20TXqSnxD3I3vMvag1_xqFoKfXGUuGkUTwlWLNm1oOmrRWQSqagCn3RziG2ai9kGDmXrwqA44a2GVIcM77a6SuV5IyQNNIMbXHNowwdHmAdOl-BKEhFdqsNqQGeiWELqals4C3puc2AkCDa2V8CMTRQBQYIuVRP4OGE32csXkWRomJYsuJQmlMnJwjsjAIBMVzKNxqzH-1ewl8yuUQnoe_djymJKIMk_K0iJUf2k3CgoERNbw7ZRVUsEOeo20pygLxKp9a_tHQYcA8yYM0D7dpwKOHHD4SjnzAPmp7tNY7aDb0xLvx-wc2vkkA7eYAr78JA7qzfEMDLaDK1vaelMqSfebyCsQEe0Zuv1oTzan0xI3zTnAPX_4TEIIC7Psx3pvbpoR03rV6bVUNYIQZ6NKXc7QfTWn3XlurUbkrA7ebJhHFOtRUOJPNG1pjr-N2jHGvPYkD65V1rXgdM9-YaDhKgemIwDwiIOGiFpwn4j6cvXtAGQrKJxf8wIhRmj_MG-FHDL3_uRoqQYXw5P0erLyGXyEJiZIsZc4GulnfY8M3buywWd2QZjKR9t-GyXfz-2foHKerH-cWgl-q3GXxWniHZkWEKo6o2iFoKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a25fe3090.mp4?token=W8mPHyhHKM4OQzOoSx9Jptd9TPqSFRTJgT1Wr9BktHte7Om-p3on_Eu7eeCyhMt76myPmuh20TXqSnxD3I3vMvag1_xqFoKfXGUuGkUTwlWLNm1oOmrRWQSqagCn3RziG2ai9kGDmXrwqA44a2GVIcM77a6SuV5IyQNNIMbXHNowwdHmAdOl-BKEhFdqsNqQGeiWELqals4C3puc2AkCDa2V8CMTRQBQYIuVRP4OGE32csXkWRomJYsuJQmlMnJwjsjAIBMVzKNxqzH-1ewl8yuUQnoe_djymJKIMk_K0iJUf2k3CgoERNbw7ZRVUsEOeo20pygLxKp9a_tHQYcA8yYM0D7dpwKOHHD4SjnzAPmp7tNY7aDb0xLvx-wc2vkkA7eYAr78JA7qzfEMDLaDK1vaelMqSfebyCsQEe0Zuv1oTzan0xI3zTnAPX_4TEIIC7Psx3pvbpoR03rV6bVUNYIQZ6NKXc7QfTWn3XlurUbkrA7ebJhHFOtRUOJPNG1pjr-N2jHGvPYkD65V1rXgdM9-YaDhKgemIwDwiIOGiFpwn4j6cvXtAGQrKJxf8wIhRmj_MG-FHDL3_uRoqQYXw5P0erLyGXyEJiZIsZc4GulnfY8M3buywWd2QZjKR9t-GyXfz-2foHKerH-cWgl-q3GXxWniHZkWEKo6o2iFoKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
یک چالش خاص وجود دارد—آنچه من «پروژه منهتن» می‌نامم.
ما اولین کسانی خواهیم بود که مشکل پهپادهای انفجاری (FPV) را در جهان حل می‌کنیم. این یک مشکل جهانی است.
اما ما آن را حل خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130051" target="_blank">📅 19:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130050">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cbc84ad96.mp4?token=eLA4c_3i5eIw2jGAqm6a96rAgz47VEwgXzk0sQ1OCWd8y9Fgy7VYD2jhg94G7vxS-xeFj_Ja-eFmgnRqb1nZeNeugePd4hVU6niM2Vw5Jcent6ruZM1HP6kZjghKjsIMaVaSm1jHbNLeFCdMWt940bI3FXfpK0HUDHy2icfydhKoLXvT3VEGkUu_-55lPmjCH4hAlKuvw3yoW1ylTJET1n4zQukRB7fQ9NP3RyxOExbT_XHNhVZGSsEggp1pv71aBiNz9zpzCyj65_WxL6I7bI4vNYJF23BRaUERW0ZANk144NTWuV8xRmS6ZDpPrwVUlkjtZ91ELZE2NPlIhpOUFld8a1bfu3PFnllYbWSGrLgAR43giXTJHwMdlNLXmWLsU6nYeTgyRcT4k0KRzDIuq1GD3merXu3LQpSi9feQ3hnBETmK51PT9TWx_1Xpaj9T-OV6LB8A1QuPDBJD20bixot47iP8hbrHpVCEXfKue4goE-_-4tmankMoc3YlyPuZMuIgliHZmURWcHTAjF9UPhJCTCn2v8_PnzF-I_Jcjz_to_ISyVAVvbsL1UDmUseN8gGXqBklK2xlBpnDf8x-c5ik9hOpSQ6HtxILY4bj0g0VrzUzErE9Sbm-vtPjJkGKzrP9LO1C8FSTMuXFMECaVjROuTPEEeY8Oon6aB79kkI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cbc84ad96.mp4?token=eLA4c_3i5eIw2jGAqm6a96rAgz47VEwgXzk0sQ1OCWd8y9Fgy7VYD2jhg94G7vxS-xeFj_Ja-eFmgnRqb1nZeNeugePd4hVU6niM2Vw5Jcent6ruZM1HP6kZjghKjsIMaVaSm1jHbNLeFCdMWt940bI3FXfpK0HUDHy2icfydhKoLXvT3VEGkUu_-55lPmjCH4hAlKuvw3yoW1ylTJET1n4zQukRB7fQ9NP3RyxOExbT_XHNhVZGSsEggp1pv71aBiNz9zpzCyj65_WxL6I7bI4vNYJF23BRaUERW0ZANk144NTWuV8xRmS6ZDpPrwVUlkjtZ91ELZE2NPlIhpOUFld8a1bfu3PFnllYbWSGrLgAR43giXTJHwMdlNLXmWLsU6nYeTgyRcT4k0KRzDIuq1GD3merXu3LQpSi9feQ3hnBETmK51PT9TWx_1Xpaj9T-OV6LB8A1QuPDBJD20bixot47iP8hbrHpVCEXfKue4goE-_-4tmankMoc3YlyPuZMuIgliHZmURWcHTAjF9UPhJCTCn2v8_PnzF-I_Jcjz_to_ISyVAVvbsL1UDmUseN8gGXqBklK2xlBpnDf8x-c5ik9hOpSQ6HtxILY4bj0g0VrzUzErE9Sbm-vtPjJkGKzrP9LO1C8FSTMuXFMECaVjROuTPEEeY8Oon6aB79kkI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
امروز ما در تقریباً ۷۰٪ از نوار غزه حضور داریم. ما حماس را خفه کرده‌ایم. یکی از آخرین رهبران ارشد آن، عزالدین الحدّاد را از بین بردیم. او دیگر نیست.
و می‌دانید بعد از اینکه او را از بین بردیم چه اتفاقی افتاد؟ هیچ چیز.
نه راکتی، نه موشکی، نه حتی یک شلیک.
بله، حماس هنوز آنجاست. و ما با آن هم برخورد خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130050" target="_blank">📅 19:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130049">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QHHPnqvi0XAfGmA_b7GUsDonUXVzHzs9Lq3CIkrwq4yFzc85uDcLk6WKktMR_mnAtj6A9rLKIwy2Nlx0Lu8Uy8OXZX0--ndATdIZUh8W82VQJfmADNi8qF0D2bD0pdifQRGHcEtRTq1kI9AzKaskN7m0t9WtnL1kGJF7JFOz0c9vqDKDfZhgnWbVlgNOxAzNMOdjwtSkYX-ObBqJcixTv_ESoZtFM7DYZVKTAazqFDdjQPTTZ6CcT3Y1tLxnmS4Z335X2061QtRbmNf9a0WoIFMc3lkSQpS6tSubUpiEL4Jj81AmCkR25EyqLLfcUo7vGAkHsjDV0EQV00DqOpKI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت هر اونس طلا که در آبان 1404 به 5300 دلار رسیده بود، امروز با افت شدید به کمتر از 4000 دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130049" target="_blank">📅 19:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130048">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
الجزیره از حمله پهپادی اسرائیل به خودرویی در نزدیکی شهرک کفر رومان در جنوب لبنان خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/130048" target="_blank">📅 19:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130047">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزارت خارجه پاکستان:
مذاکرات بین آمریکا و ایران هفته آینده از سر گرفته می شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/alonews/130047" target="_blank">📅 18:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130046">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vu-1rbctnylFAmw1pextHFUjsD2jFp5gBqXXP0-XbMj6Rvul4S90EZ_CJ-eJnVx2CYcq2rWZuOlJDGRNr1mlcO9xUGbRC1RLerp3rGx0hLbI1NqfuarELLt0xvJLF82EyDaFyP4c8fywyuuq3-rA3HNPeyaeyrjqu6Skj_3YNkXEeb9N6ag8REgnh013uwpcoMZDt5bsW1D8bvt-KwHu2hLrQc0h7VSBmT7Tbhwk2ucYg_0kZPNCFIllCxdMcxrMGPtCsCxZ11ozoxHw5GXz28v6bAklnF9G4yU8qXF76IXLV168gPdTfF6pKavNY0R9iv5SWV0eITq0JmGfLyb6eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: داماد ترامپ به جمع میلیاردرها پیوست
🔴
منبع اصلی این ثروت افسانه‌ای، همانطور که در گزارش فوربس آمده، شرکت سرمایه‌گذاری "افینیتی پارتنرز" (Affinity Partners) است که کوشنر در ژانویه ۲۰۲۱، یعنی درست پس از پایان دوره اول ریاست جمهوری ترامپ، تأسیس کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/130046" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130045">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/130045" target="_blank">📅 18:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130044">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس:
تنگه هرمز رو با مذاکره فتح نکردیم که با مذاکره واگذار کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130044" target="_blank">📅 18:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130043">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130043" target="_blank">📅 18:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130042">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/130042" target="_blank">📅 18:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130041">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/130041" target="_blank">📅 18:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130040">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/130040" target="_blank">📅 18:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130039">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fb4DJcmQUX7LLPzgTX6JoVIo-WAiSAi9D5a95BtUTvsXQF4aglYrkuSZs120NJHE_yGJOPUdV7Hk_8HK72BdmzzxGaOT_UoLmH5FWZ4X8Vy6ci-zRHqXYYuHmlA3he47lG0XK-L_ChF0TNw4D4ilZdqUGxaJTXmvP3nbaVXwaUe6tTd_LvCxeBhpinVUjMDhkBOPokum4XCFAHlgYzyiUmF9iJVRPGe-TB56aX5YN42JEf3Kcc6wIWaV1kB5ztprNOet5oMw4Lnx_KwfdMLR1GQ9ZW9diC7RD1Gm6H3-mU2I4FZpxBy0fWbFTRqVmIfaiC6ujZZ9gU44IEmQv1zimQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو : عملیات تو لُبنان تموم نشه
🔴
بی‌وقفه و خستگی‌ناپذیر برای این نبرد تلاش می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/130039" target="_blank">📅 18:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130038">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو، در گفت‌وگو با فاکس‌نیوز
: اوکراین در میدان نبرد عملکرد خوبی دارد.
آن‌ها هر ماه حدود ۳۰ تا ۳۵ هزار نیروی روسی را کشته یا به‌شدت زخمی می‌کنند.
این اعداد واقعاً شگفت‌انگیز هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130038" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130037">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa3c9d8282.mp4?token=RrREUHoJF1yngg5DOgpYIZk6T3kBFihNuqNmtE7LHlctlBoBHIUM2tLERqXQRoxkoBwx9n6riG-EIYUBiddtflnngx8FJ009yrwRJ3pJFH5bSKPqu6NkEBeTBUsu05Y7JKskowVqiRlkw0jd5SCDdfCuFN_oEZR3j_HwqPyOQ5JBo6GUQOqbDE7RVA9d-fevlc1lYXoWtJ-LW2J5dUB35im1jlBNL3pEk2B2V8QKSmCOKCxrrr12uSEIsQ6s9v4PUOu5aqGV5ar2Uu9BR9tjRQjlhKMWVuiY3OrE6-xqCTviKKjSWHGgteGYyLQ2aK43izao7mwIMF9A7WNdUMWMk4IJPD5dv0PqT3A9HM8baES50x23rc5gwwzaBfExqn1DqVsgJSyvo4XQLN5MNDjlI3-KEZLQwtH-WSuwS6aSbDbdBFgKspUahX-zM7lWFqpOENIow3TvxkvnStG3-LqMS2XuAMzP_Ujwm4RocThDKexbd79uckaPmDtz52-m3XPpW-HGAYcKM8ULiegm9Ba_vpeSiAM68zmi0-Dr7cbE-ghz6LmjCBtl2en8RGCbNzIG7HOZPihd89dOJDBB5wOPjyTT6QY5PjnLkOvQH_jBXrdriZh9t9VZbG7PP5xl41OOSCLOYxa_c7D2J8zL2TIvhrKyWEUQ7bg_BnnSQJhv3VE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa3c9d8282.mp4?token=RrREUHoJF1yngg5DOgpYIZk6T3kBFihNuqNmtE7LHlctlBoBHIUM2tLERqXQRoxkoBwx9n6riG-EIYUBiddtflnngx8FJ009yrwRJ3pJFH5bSKPqu6NkEBeTBUsu05Y7JKskowVqiRlkw0jd5SCDdfCuFN_oEZR3j_HwqPyOQ5JBo6GUQOqbDE7RVA9d-fevlc1lYXoWtJ-LW2J5dUB35im1jlBNL3pEk2B2V8QKSmCOKCxrrr12uSEIsQ6s9v4PUOu5aqGV5ar2Uu9BR9tjRQjlhKMWVuiY3OrE6-xqCTviKKjSWHGgteGYyLQ2aK43izao7mwIMF9A7WNdUMWMk4IJPD5dv0PqT3A9HM8baES50x23rc5gwwzaBfExqn1DqVsgJSyvo4XQLN5MNDjlI3-KEZLQwtH-WSuwS6aSbDbdBFgKspUahX-zM7lWFqpOENIow3TvxkvnStG3-LqMS2XuAMzP_Ujwm4RocThDKexbd79uckaPmDtz52-m3XPpW-HGAYcKM8ULiegm9Ba_vpeSiAM68zmi0-Dr7cbE-ghz6LmjCBtl2en8RGCbNzIG7HOZPihd89dOJDBB5wOPjyTT6QY5PjnLkOvQH_jBXrdriZh9t9VZbG7PP5xl41OOSCLOYxa_c7D2J8zL2TIvhrKyWEUQ7bg_BnnSQJhv3VE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو، در گفت‌وگو با فاکس‌نیوز:
۵۰۰ هواپیمای آمریکایی از پایگاه‌های آمریکا در ایتالیا به پرواز درآمدند تا از عملیات Epic Fury حمایت کنند.
این یک عملیات بسیار بزرگ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130037" target="_blank">📅 18:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130036">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95dd83e81c.mp4?token=AsPraGxAGnlqJGE5qU-57zAiJTyI4bOUe7osjJBuktFgzTR3VaOb9K_hNAolXSs9VBYtlAL3c_326_qOaZOXxRxM2NUlzVFPyXKppmv8hmhDDIhof-NUBWPFBTz_rXTumb4qjIeMhdTlHWSMLq8z1IEp79HRGMjIvY6gUo4zLIs8se2xuVrRczf_vbIVWtbyN7nZbEshVtmUBjOEXbNWpqSzF4e-my4EdVUINIRfYaJwvzFzFc5EHTCE2NtSzIZGA_465CW-0-AqXuelb2DgIITBlZsEWRIfAVqDaXQYjelSknZpL4BMN_Y5qNsRb5xSr9I3CwQ893cZwnScKAOqXokvJYBIswk6FFtJCTBoTZ9XKvE7RuQ4QHgTGlQ9g5QEF1yDzLoXCdttExfTF42-ONZP4-_IjxJ2XjzLYoGye3QlhuQ8_4sCQiogQXeGgPYFlFVFO-BM5Mkq6J6o_vwBZHgHDyVDpf_M4xprZPBs03MpXyXcLRFaiC95N_qUwp0MxrXSty__uYLXIzpVV2iVn21j1kLxvZsLl8a5cfiMZlT_zqoiGrE85Xo7--QfGSohf03YQiYtuXPq8LVMT1Hc05Fo7OPDnxX5JrxFUqeMmFgrw80VHX90i_zRPZxlOk1bUv9yIHb6_d-4mEtytFS1yTccRAn7h56DrWT6Obf-gxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95dd83e81c.mp4?token=AsPraGxAGnlqJGE5qU-57zAiJTyI4bOUe7osjJBuktFgzTR3VaOb9K_hNAolXSs9VBYtlAL3c_326_qOaZOXxRxM2NUlzVFPyXKppmv8hmhDDIhof-NUBWPFBTz_rXTumb4qjIeMhdTlHWSMLq8z1IEp79HRGMjIvY6gUo4zLIs8se2xuVrRczf_vbIVWtbyN7nZbEshVtmUBjOEXbNWpqSzF4e-my4EdVUINIRfYaJwvzFzFc5EHTCE2NtSzIZGA_465CW-0-AqXuelb2DgIITBlZsEWRIfAVqDaXQYjelSknZpL4BMN_Y5qNsRb5xSr9I3CwQ893cZwnScKAOqXokvJYBIswk6FFtJCTBoTZ9XKvE7RuQ4QHgTGlQ9g5QEF1yDzLoXCdttExfTF42-ONZP4-_IjxJ2XjzLYoGye3QlhuQ8_4sCQiogQXeGgPYFlFVFO-BM5Mkq6J6o_vwBZHgHDyVDpf_M4xprZPBs03MpXyXcLRFaiC95N_qUwp0MxrXSty__uYLXIzpVV2iVn21j1kLxvZsLl8a5cfiMZlT_zqoiGrE85Xo7--QfGSohf03YQiYtuXPq8LVMT1Hc05Fo7OPDnxX5JrxFUqeMmFgrw80VHX90i_zRPZxlOk1bUv9yIHb6_d-4mEtytFS1yTccRAn7h56DrWT6Obf-gxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو، در گفت‌وگو با فاکس‌نیوز
: می‌دانم که درباره ناتو انتقادها و نارضایتی‌هایی وجود دارد.
اما باید توجه کنیم که این موارد، استثنا هستند، چون واقعیت بزرگ‌تری هم وجود دارد.
کشور پشت کشور، متحد پشت متحد، پایگاه‌های خود را برای عملیات Epic Fury در اختیار آمریکا قرار داده‌اند.
هزاران پرواز عملیاتی از پایگاه‌های اروپایی انجام شده تا از این عملیات حمایت شود.
بنابراین اروپا عملاً به سکوی پرتاب قدرت آمریکا تبدیل شده و امکان اجرای این عملیات را برای ایالات متحده فراهم کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130036" target="_blank">📅 18:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130035">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acce89e784.mp4?token=nDgk_u79HC6YkPF0mdlgw2pVXy6qlhbieMwI-A1dsoyBinFonfBoZKw5TtpT5nI2z7AM_CQH_IUBC17kv7JVMcemGvXbgikNxBExdADp5aCbpxQuB0OmjEG6G-csOJTXgCYKsIzakT3qH7lmOK3M0u8sXJV6Z170uCSz-_24Bd-edLfZVjnNafvgXU2xsEj0x_r4jTUPiM-Q_KfiNTHNwgUKFGpOKStMtVWaifRGFS613khsm-rO9_5kpcuVlaGJx2Tth5W4nL2ljuNOQ3R_RiuDx-gQjfvKsgVtr5fCf6QLPcJYy2nkzhqrJ9lA-MC5vLnM_SHUMh0MJulZPuWRYV4tIQdKntzIjIr1TBPIrB6zu6PgF8QGyf7jjz24s6U8JJkLmbZRL5IRr204piMsro-iveJjCiMaf874Bt1hk7UXzKY7Xep6EtDjafhm9zWOcJPv_cXWpN0d5Ta9rvMi_kUojd1KdtiJzV8dblyR1pGE0W_n7lOSkp_8hxUxWdxZxJErQIhn-3hyURuEoRFamPM1TCX1J75qX98xZMuHmpEWCsTyHbvH-mmzX6Ftw7e9afcqBK7aMDjpadYmb-tj9n79_LTZITbgPzT2-Xm6UOZdTg_P4d3rRrtIo1Qa1h_x7HHU-R7iQeWkmeuSbh9bqXpMZaOnG-QpwPD4Sy979Mk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acce89e784.mp4?token=nDgk_u79HC6YkPF0mdlgw2pVXy6qlhbieMwI-A1dsoyBinFonfBoZKw5TtpT5nI2z7AM_CQH_IUBC17kv7JVMcemGvXbgikNxBExdADp5aCbpxQuB0OmjEG6G-csOJTXgCYKsIzakT3qH7lmOK3M0u8sXJV6Z170uCSz-_24Bd-edLfZVjnNafvgXU2xsEj0x_r4jTUPiM-Q_KfiNTHNwgUKFGpOKStMtVWaifRGFS613khsm-rO9_5kpcuVlaGJx2Tth5W4nL2ljuNOQ3R_RiuDx-gQjfvKsgVtr5fCf6QLPcJYy2nkzhqrJ9lA-MC5vLnM_SHUMh0MJulZPuWRYV4tIQdKntzIjIr1TBPIrB6zu6PgF8QGyf7jjz24s6U8JJkLmbZRL5IRr204piMsro-iveJjCiMaf874Bt1hk7UXzKY7Xep6EtDjafhm9zWOcJPv_cXWpN0d5Ta9rvMi_kUojd1KdtiJzV8dblyR1pGE0W_n7lOSkp_8hxUxWdxZxJErQIhn-3hyURuEoRFamPM1TCX1J75qX98xZMuHmpEWCsTyHbvH-mmzX6Ftw7e9afcqBK7aMDjpadYmb-tj9n79_LTZITbgPzT2-Xm6UOZdTg_P4d3rRrtIo1Qa1h_x7HHU-R7iQeWkmeuSbh9bqXpMZaOnG-QpwPD4Sy979Mk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو، در گفت‌وگو با فاکس‌نیوز
: فکر می‌کنم ترامپ دقیقاً همان کاری را انجام می‌دهد که لازم است؛ یعنی تضعیف توانایی هسته‌ای ایران.
می‌توانید تصور کنید اگر ایران به سلاح هسته‌ای دست پیدا کند؟
ایران صادرکننده آشوب است. صادرکننده تروریسم است.
این مسئله برای منطقه فاجعه‌بار خواهد بود و برای کل جهان هم فاجعه‌بار خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/130035" target="_blank">📅 18:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130034">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYEM_LqiiPFmWq8EpWnlnpWQwmYL4zGSSC8xhjdqm7HPEyvySExEWBt_ODPz6vPa0kUvPf-Ga9A9P_HeWaGfbxAZanXDI5hrtSAIQC-Yl62Kyae0QQAzxoDn2oNeHTNi-m6TSZO0xNbWZU2UgS9DWToyctHpXOxZzBTCTwNROuwcqxKAjgGZLmvipXuLFRHJWKdsBNUpqIUpv6DQWddvkvrE3HIZuH_0-oC1-JiIDhKtc2M0K60JxdERDJ89hCrKtpqJPAg2dV384kzWneMYIbEUG86p8Pv_nKWPrm851eqhP9x7VcyzpNkXir1NOA3hhd_dsrLe_M5qrSEGCpSegw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ
: کنفرانس خبری و مراسم امضای مربوط به مسکن که قرار بود امروز برگزار شود، تا زمانی که قانون بسیار ضروری SAVE AMERICA ACT تصویب نشود، لغو می‌شود.
من این موضوع را یک وضعیت اضطراری ملی می‌دانم.
از توجه شما به این موضوع متشکرم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130034" target="_blank">📅 18:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130033">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGGbGQYt0lsHuxt4a6Y1fyNlGmwbmq1K7Tbbn6E3rpnoDhtjVrxiBtwAQdUgfCF24_LoxKp4Or3ua8RKIgulscj4cfVb2VNI9znpyMBvUTimjKHgiT2cerl5fuLHoi6dMPa_0M7Ppa4nSjAW7vKnF-_tUBFzswug5mlrIBcvDyTAb7kkkCeGCHlfk12D9B8PEB5z_3yr13XIk73Rk2bmc6cChLDRJmY3dDQqxz04enteyL47qqUetc3OJI942N0e0FKGGnxqt9uzux-MieCbToooxG6o94QQvzUgdvolfddOgiIw4lj4NQRSGdXJ4rk9zstWIvbdR9J7lvnSwMgAQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت انواع سکه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130033" target="_blank">📅 18:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130032">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxVSKqkH3rvahW7Cyg7odvc28CurNeaPZ3m4uQE7N6wxLHeaOhCj9-58AtWbiTSg7ObymNPPN2kcPcOUgcqglFr1mTqarRARRCZk-IHszPb4RsH5VG18I_aPRP1sZbDHkfCyIProSBcMZxVD7g4ER450VycFeWhvvIGNOmZviLCHLJmsRfhpeAXYBQuctQvTbDd6ZprdEBBca74Td4cb9jrQhFMu9gHh0SbJqbXdDDmqYl0_jU2pRbzZGuTiTjXVGyaE6jIpO-3tlE10IRp0mIC20BySY60bk-aOwaDekWmIF2RG73NR4tevnT1jFIvpr1hbEP5m7WBr7bI1xrerIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت طلا و نقره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130032" target="_blank">📅 18:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130031">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEs93So2-8OVN8gj_mmx5cav6HnSE4M7wtLCIcJH1QbryD2LpjJhRdUXrVrxaf65fzQeK3GYG7exRAlhYdVT7RS6Pacu-V6OXtJYAaaMwuIGJKHVUV60sF6_65gl6ev31fEszuP5tHhMl8qTDn-3W_NLhCWpFqoVz7rlufNB_8CbMjiUf97NfwvHIb0ZQOH-Fx2CZoHH3DPwm2UwwZKOTFpNKhcB8VVJdBaI09wSoPNi5LcclDVdMdtxFHGkLH8mqjQpNsI6NgTECwgAJg6zJGI9sKfu4ZCFgJfffmEUAm0bTxOFQ9zRmFlZZ5_jwFNrCds6FKfWvxJrsDdznoaG8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت انواع ارزها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/130031" target="_blank">📅 18:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130030">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
جاده عین عرب به الوزانی در جنوب لبنان توسط نیروهای ارتش اسرائیل مسدود شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130030" target="_blank">📅 18:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130029">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOTPvvwh9LeW3Wpiai3eOVxBXueEY0c50RU7iHpkrqrKlmSo2IFWScU1wdPI1XmodHhS1bOgnM-fyKbm4TGgKnt10vycs7EXzx4Kq9z8NZKJHbSTBWsVMzKCfwU-M1dbssY7AXsO1oetTX2_VQZSFKywVdtrbkAGw6MT8ttPJYps_5aypch7iiiB4PvgbtyVpw-esqfSsPwSQLY_cjW-ZYqVh7zEIgsnqc6_co96FTAAaMBSPWjV-MjMcCrRy5oAoYHiGGXeh1ee5QcgmvMGX1kCFQIGPZ7I5BbbCwo68CDpx5202wCReTEehw5QiKCcSCGyQnsjhmIYh6L0C1AUIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شماری از مناطق گردشگری در فرانسه در سال‌های اخیر به گردشگران هشدار می‌دهند که اگر با بالاتنه برهنه در خیابان‌، میدان‌ یا مناطق تاریخی شهر دیده شوند، ممکن است تا ۱۵۰ یورو جریمه شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130029" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130028">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvgiZTAqgSxI4_rrW7hplWDQolCiB1dPpx3ej_KRbM2lSa_mflQnjocPrz-7yp3sKgHcdgqrGSFCb7N5AZC-MEFuUOL5Ii4zQh35iNVJlZYaTH63o-tWB9sXIwUa3DCbzLS1n-lIoYiRCMQCvVph9OD7k1Z3vzY-nETSwzDkqXJuJfSgGSSqFR388oYF_eYqWwYmnBrqpIMa_E_654m_yKLppSZlUZnqnX_OXT415liHwhzUrDBmZKQWgkI9pM3I8q_Cy9KSY-ZVtKhEa6abce5d7kpA6gfGj65wXgoMjYudCtXj7o-CSTWZLoo_WUfpXiO0wCdnz_oPZLZWg3LpfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کامران غضنفری، نماینده مجلس:
دیدار نخست‌وزیر پاکستان با رهبری، برنامه آمریکا و اسرائیل برای زمینه‌سازی شهادت ایشان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130028" target="_blank">📅 17:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130027">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APvbj_6Aq4W4xyF4akpmw4li7Fk5nUeItQG4yYlxfeD6q2gxcMelfnl2hVbmbeo2WKmPwcY8NkpYhkDYxu_f_aTHWwLYVx31HtVub-yiFGbvHxWyrAIt-Kj7Cni66FfjA8U05J5ZxRqP_KlU_sGGHsneDFezJM5UmZcvhLbzuu_YCh6EvIw0UDxXqvvUPwZPYgWYyYQFFBiW0jbMFQFrGtG42BM0G7sJACRdfL6wjy-zDumZey7zB8OePmEPIUye5R__XRb11kpcAbATtQRDVZJKzQQ3_4Mor1K548TzLcHKV6HzYMO7Zzep-vhOwp1_DikNS_wO5IvZmp3sbnKJNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: برای دسترسی به مواد هسته‌ای عجله‌ای وجود ندارد، زیرا در پی عملیات «چکش نیمه‌شب» در زیر زمین دفن شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/130027" target="_blank">📅 17:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130026">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBhiV01M6w5ENhnkNDhEMB7JyTlNUhL8dW4JfVrFZdD9iCxKbxOKy4UpxLdFLVQbRHRVUzMgaFHyjRyV0OTzNIO7l3JAba9UE46W7kW4dZeyXdJrIE0JbH15Hm-07MUiJZb8BaGg4Y1HldIPCtW57b-4XYqYID5FTqRIgFTRbxaRrZvHu4FyQDoErjBrTQ0RP18b84bI1NscfdgLW9S0GrKktDjiiA9k0ZFGhbGXs1Y6-kTrMhBmbdhVycwXOAp96KMWLJl1kqLio4foE_U3GiRSMpUH639nw2U4vQ7kk9IYXWxBcMUNcJjZ1uZVifubhHnNHMgQTKEmKYUhmHDaLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: ایران و پاکستان در آرمان‌ها و امیدهای خود اشتراکات عمیقی دارند؛ تلاش بی‌دریغ پاکستان برای گسترش صلح در منطقه ریشه در فرهنگ غنی این کشور دارد
🔴
در سفرم به پاکستان به منظور تقدیر از میانجیگری‌های پاکستان، درباره گسترش تعاملات با برادرانم آصف زرداری، شهباز شریف و عاصم منیر صحبت کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130026" target="_blank">📅 17:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130025">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtW_tUHIKrdMwbvdbnvE7ntvg4l4ANPHjEGks0G65YoWVTTc7p5BycxzhSYGz7E6nIBwCxgovumSZt204ITng9So5hPGDYCH4pMWSPpjcEOBrBysoVCqbHx3AT-i-p6Fbpb66o5JFEuHkIBxabpZCbpOxXrQNrMly9Ev-6LgFGdhazlAoGwW8cN0-K8Sy5_DygfR1pnB3pVeQqWUf1K5n2UoHc7DCrC5scHmgLB-RAuATeOuUexEutVyhfD9plImUO2H8glREaGJ5uW7znCAi8FwVkwsc3xGWixWfEINmtyyyJN1YgiWCwJBygtejrnqHa3c3YtjwlIHdox8bggiyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ
:
رای های من اکنون به بالاترین حد خود رسیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/130025" target="_blank">📅 17:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130024">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZShHFAmUcEVtjVcTZZ2ZT2uSftR2sYt3uvMQ4XTCUXIBtygcYO2BdZyBbGGcfo9YkGQezJtLuTudxVZT1rMv2UvYax4TsDgNRUx2u3OUe5E1cpXuK0h2QkQ6xrpeKBpaDWU6dFG8pY2wT7EqgJ-uihTHzlMY8knKC9_sr8D6WZClFPjcArXMA43bv1CBXMjRBy8HUGV0bagyMs5cXckFdovcNKG_Q6-A-hQqLv3aMMvlh-xce4BCmDh8Hjva0QM3ixqVXltt_EDDYr5ihovZYarVwMlhVx999Anzy6zsgqZl8ba4wxT0b1DrsADBVxg1lRM2cLbeu422sA9OUQnpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرزیدنت ترامپ:
شهردار ممدانی با حمایت سه کمونیست تمام‌عیار به پیروزی رسید و رسانه‌های جعلی هم با سروصدای زیاد و به‌صورت یکپارچه برایش کف زدند. تبریک آقای شهردار!
من دیشب ۱۶ برد از ۱۶ داشتم و به انتخاب میهن‌پرستان فوق‌العاده آمریکایی کمک کردم، اما رسانه‌ها حتی یک کلمه هم درباره‌اش نمی‌گویند.
در دو سال گذشته، حمایت و تأیید من باعث ۲۵۹ پیروزی در انتخابات مقدماتی شده و تقریباً هیچ شکستی نداشته است، با این حال هیچ توجهی از سوی رسانه‌ها دریافت نکرده‌ام!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130024" target="_blank">📅 17:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130023">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
مدودف: اختیارات زلنسکی مدت‌ها پیش منقضی شده است و این واقعیت او را از هرگونه مصونیتی محروم می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/130023" target="_blank">📅 17:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130022">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZDlP7uHi6j3U_a2g7VvnKEKVDems2onwr-Z1h-w9KAzdmJ7N-dLRuCJGtzuNR5yIj8MSR4lsmDMa8r6-eOsxgfD5Zr7WhEirgSPkwAv1-PLCV2mFMoEf6ikLqeEcz1_pkIB1risZA7KFctPYSucUPtZuBrMM_kJ8jPIRPbJkxAUPlChIpF6uJ8fnZL822_Zp2rE5DlRQ3JPY9E8cf97u-bxz1rkuOZsD0e6FBwT3VPPyeSegfVsrLuJDGFw-3FyAgHZcyXAKKeItQ2BGDpL_v1smr0tHcH-gm51qEVwLoR8h5PR1hKV5ocwbBMkGa9VZcUd-P6WhMrpWtN75kZMIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین تو این مدت جوری پالایشگاه‌های روسیه رو زده که نصف روسیه درگیر کمبود بنزین و گازوئیل شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130022" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130021">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbuwg6Fe5PDoeq-IRyucSXHLZO8ZYm0hPh9AaBA21LRGUphGA4kbUrMjabI3eZ0Vcyk-Fyua7xK658Avdb-Bgh8dihXCQaUik9IezxxfEbO79pQa-fI6K3drlB2_Z2aOhPj--x879RGMYYpj1ndiI-D20lv68KLtZYPVVnv2HsMEIU_i7Xhxt8L0-3XYidkebYsYyJaYf4mQwpHY12Li_PCap31nAgHewb9Dh4m6qJPFVgIA-GIDgLxiX50Qd9AdT0_1WdGuF5HbouWVoQ-_bKo9Q93Yj8IQAN2gW-hLXFPO-pAEGPBIu47JRLvNlJDvjmS-YLMOI_nydwFSXCShPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه ایالات متحده روز چهارشنبه سوم تیرماه اعلام کرد که مارکو روبیو، وزیر امور خارجه این کشور، در دیدار با شیخ محمد بن زاید آل نهیان، رئیس دولت امارات متحده عربی، درباره یادداشت تفاهم با جمهوری اسلامی ایران گفتگو کرده است.
🔴
بر اساس بیانیه این وزارتخانه، دو طرف در این نشست علاوه بر بررسی مفاد این تفاهم‌نامه، در خصوص تضمین تردد ایمن و آزاد شناورها از تنگه هرمز و همچنین اهمیت حیاتی برقراری و حفظ صلح و ثبات در منطقه خاورمیانه به بحث و تبادل نظر پرداختند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130021" target="_blank">📅 17:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130020">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Or4Lyb0Xe7hb7aQRwTAvAiOR4V_U3Bm-qMzWmaNASfOiVIUC6-QYlWT0f9wDKZpeVGIt-MMk0menma1_-a7w7bpr5VFEsvAd0uINYQXpHdEBkbkGBLrUjVwjl4_Ef2aM5rd47XoHwbgOlIYX148fzg4JzrqrKWmmbpuy-0U6jtUzMfD0vfKMboF8hFGZC8Ray68iTnCOLzVwwj2IGpASAPHVZIGfcESufYnDr8cskKH8nBjMSlp5JXjc0dovLUdMy20pUPtdxoAHtBe9DEz7vSXyho_or5MigHCH55uekncnJW5mZzvb1eKBOHUo9Xo8hKXIDzQ4JoeOMWkWEZrgGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سقوط عجیب طلای جهانی/طلا به زیر 4 هزار دلار رفت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130020" target="_blank">📅 17:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130019">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEDOknJnXebqYHbc5rxoMUkXF4N1qroUvy99W9UhtcA_Fh6WIVh3exLCNZ67B7d_Y6kaScRBr3ivNAu6YfoySE4h9_TUdGtWpcBK3FMKdC8NE3Ge2SgqxIRqv2I2jppBsX2863dAlNqbVsO3akWHbCdDaj_sHAbNi3y5cQgRHpg43W0ovdjr0zIfV9AiMh6lklT8tbC_lV4AiHpu-ZXmtvSNHRaJYz6ITK5m1GceR3cLWignkbQcygqKyW3xw2TuHSFQg6pdZ1EwaVwjIiGo6JXQinaqh71XZg5d7RMU6tGQrUlY0aNlOiW9VgWCVTrEWoHBe9UiwF19Fi2IU6g3cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قضاوت جنگ صدرنشینی گروه K به فغانی و تیم داوریش سپرده شد
@AloSport</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130019" target="_blank">📅 17:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130018">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db753fb80.mp4?token=JXctKpgLbySV22eyQsXw1wiiqnVN7D2HexFo-iORcISvWz0IATut98C3HkPWY_GaGB-NTXJlLzFROlnVd-AANoIddLrMWAZUM8E7e6luaOPBD7Rdc_9XvdIfa-d1DAL_-P88PtOznYo2z32QYDUJAAd6P8rTwuhzlHjmdGgClFTskE38B6rDACTCSwEAs8dG9fenptZGTAHGvDtVK4YMxTMH3XuxMVX7tyPLzzMVDhdD3BlsPBuvNKQY2P75ZfofXc-4XuiXv7PnedOfd1bfZyXFp7JMsRcTvU4fkGgLUikM0knCDkj8G0b7YZ9bjcvM8mrOe3IgvI2YwxuW3_eLyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db753fb80.mp4?token=JXctKpgLbySV22eyQsXw1wiiqnVN7D2HexFo-iORcISvWz0IATut98C3HkPWY_GaGB-NTXJlLzFROlnVd-AANoIddLrMWAZUM8E7e6luaOPBD7Rdc_9XvdIfa-d1DAL_-P88PtOznYo2z32QYDUJAAd6P8rTwuhzlHjmdGgClFTskE38B6rDACTCSwEAs8dG9fenptZGTAHGvDtVK4YMxTMH3XuxMVX7tyPLzzMVDhdD3BlsPBuvNKQY2P75ZfofXc-4XuiXv7PnedOfd1bfZyXFp7JMsRcTvU4fkGgLUikM0knCDkj8G0b7YZ9bjcvM8mrOe3IgvI2YwxuW3_eLyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از حجم بسیار زیاد آب رودخانه سیمره در شهرستان دره‌شهر ایلام
🔴
نیروهای امداد و نجات هم از پس سیمره برنمی‌آمدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130018" target="_blank">📅 17:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130017">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6001bc8d37.mp4?token=MUsAZs_-u0r8-Lb0RKlHIx7DBEUtlkeZy6S_faQunoZmnCfmkage80FbBW-gu0XGZtXQjVpRczyordei0m6AeJK53NWwpG8Qg2JIzhyN9bZgYolRt9YK5pZ_1JbvpyJBSB6FhmDgyBeU_IAXexk0iKvzu0x-2pkLwDz_gr5KkOLeE81Uoaurk7-EsQZCHHmgzo1g5NnIbcmxKccuWoJzvqnTZxDoxAgMkzpPdWPMEFQFQY2hGm6R-sm2EFvYdkJjreDvE6mVtNX-URiMqigHOd87K8I8kqEbbtHjHh8VJJ1Zdm2cgklgFvm5wJOvLDb6-cvCONuyErqC7DImwegefIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6001bc8d37.mp4?token=MUsAZs_-u0r8-Lb0RKlHIx7DBEUtlkeZy6S_faQunoZmnCfmkage80FbBW-gu0XGZtXQjVpRczyordei0m6AeJK53NWwpG8Qg2JIzhyN9bZgYolRt9YK5pZ_1JbvpyJBSB6FhmDgyBeU_IAXexk0iKvzu0x-2pkLwDz_gr5KkOLeE81Uoaurk7-EsQZCHHmgzo1g5NnIbcmxKccuWoJzvqnTZxDoxAgMkzpPdWPMEFQFQY2hGm6R-sm2EFvYdkJjreDvE6mVtNX-URiMqigHOd87K8I8kqEbbtHjHh8VJJ1Zdm2cgklgFvm5wJOvLDb6-cvCONuyErqC7DImwegefIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا، بسنت : سلطه دلار خیلی مهمه
🔴
همه کارهایی که ترامپ داره انجام می‌ده، دلار رو دوباره محور تجارت جهانی می‌کنه
🔴
تو ونزوئلا و حتی مذاکرات با ایران هم می‌بینیم که معاملات قراره با دلار انجام بشه
🔴
در کل، همه این اقدامات جایگاه دلار رو دوباره تقویت می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130017" target="_blank">📅 17:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130016">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tK-0tBs0t_T0tQ9m5oBQ6GW4Li-1NI_IaPFymimxzqLkMhkmik0MvtWrQv4MuOY9fKcmcmjII-8hwoiEVpjHbqFydta9xOpkBe-m7JiTVEgAKAqNizG_fEh3O_9K8vWkSl1qEr0v_7T0AwHxujrc24MqqiHs0Qy3A9H-LVojXmkgOvhi5Wn79NQj_Ekmm-vIJzsuH0Z2r6LlGBKq3vdyDhuoLOqzf8H5qDkbJHwbnUYv1Vk9Z94XO7xc8sQtAvwtxl5p291d6Hwzn0NwksGIB_MpCUV0OzA8Mh_ypRZhMKdAReIUCXBJGnyhiG-SgDvnTDOZ-tcL4LadGGnGQrPgfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت آمریکا به زیر 70 دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130016" target="_blank">📅 17:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130015">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
یک دیپلمات آگاه به خبرگزاری AFP می‌گوید که مذاکرات آشتی کشورهای حاشیهٔ خلیج‌فارس و ایران در عربستان سعودی برگزار شود.
🔴
این دیپلمات می‌گوید که پیش‌بینی می‌شود نشانی سطح بالا با هدف ترمیم روابط میان کشورهای خلیج‌فارس، ایران و احتمالاً سایر همسایگان منطقه‌ای در پی جنگ، در ریاض برگزار شود، اما تاریخ دقیقی مشخص نکرده است.
🔴
او می‌افزاید که این نشست‌ها مستقل از مذاکرات جاری بین ایالات متحده و ایران خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/130015" target="_blank">📅 17:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130014">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kh8igqnXIPUlswPSkAxw-Wc9WWHBZ1L859m6IGXHmhjnl38S7XRVx1as-oMtZc6ahRaaegg22fRIrKkQbRmq5IoSXDPoC9p4dnNtFOB09TRegw3ou5mHYpcnwD9YUMtjU7Mv4b3FRKKYNfTNSYZpEdpN1Ce-llFcPWNZkKXNmK_9oeopI86YiIvVzg157dOou6ptr_18VxZ6h6U3x2MvroTeIq2aZc9grN9-LyiIK2iraKKxnh550BQZdJUNu8LdhG3Zrz6csjRXat-X5BQYCqPCyM2qAYn0O6UkCITNS-8DNK1qQtePwgdIba_WblpMlct2xijVeoTLeFCYrrB3CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکسی از اسکورت هواپیمای پزشکیان توسط جنگنده های پاکستانی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/130014" target="_blank">📅 17:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130013">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5WoSlHkCt1EAVkqHeRBxS-wcnggR3iqvx9_IaZtLhn0XoMR1OmFeN6E94TXFy8a8QkXINI7ozm1znlxqSaAff75Z-KNB8LOQgtnmQG079FCh455gnKPtgLO8ji3emZvrkireWsHF5edPwQoQCxAQZf1lLbRJK6Y_JePtlTDzXWpOx2DgsWy1XXkGMyaJWFZcZvGOH_1lRP3fFvhaiw8gw_Srh6cc5wINY6iNTnKrXr0WJJpOzFPjWh5sgxrsE8fUMqtfCYq9Ww42OI6iYRGipvwPTEuczhe7ctOFVLaJcj5Dn9fEaXpDXw9hr6j5gYOmIA4u6QJCbhhctu1alquVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شواهد نشان میدهد مدیران دفتر انتشارات مجتبی خامنه‌ای دقیقاً امضای ابزار یکسان ، نسخه یکسان و سیستم عامل یکسان دفتر انتشارات قالیباف استفاده کرده اند.
🔴
در‌نتیجه هر دو نامه قالیباف و مجتبی خامنه ای با یک کامپیوتر نوشته شده در ابتدا و بعد از اوایل ماه ۶ میلادی، اوایل خرداد ماه، رایانه را از مک به رایانه ویندوزی تغییر داده‌اند.
🤔
قالیباف همون مجتبی خامنه‌ایه. خلاص
🔴
حالا طرفداران بیت رهبری محکم تر بزنن تو سرشون
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/130013" target="_blank">📅 17:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130012">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc80afd3b.mp4?token=ekNzm0K2CdUuUCrqFyqiOlYtliXrvKvTeqcbnRR5eG93OQ5EO86cFXMdByiaURhVYI1XdnyMVfYbWFO84s73I3YPaKGF3Gu0L-WXlNMJEOQoMmwxqAfEOmXLPL9pOede39Az6SoLCABpLKunKx-QhQxRRyKVGAuwQvM006FZRuV6KfQOc-TDC2oMcSBj7wb3nqDER6tYk1Ghr2IPH83agU4g5u8sro2PLb0uQ8xoIq1Pfm0hkOf2cOKEInRgULydKoZ0gBpC1E1bH3VOyckC6lzIHy5zzkEJC9__rdinXEQmpNPt021ei_kdtlhMKSRn7rSbiGPdgdVCyzZCdUEAeDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc80afd3b.mp4?token=ekNzm0K2CdUuUCrqFyqiOlYtliXrvKvTeqcbnRR5eG93OQ5EO86cFXMdByiaURhVYI1XdnyMVfYbWFO84s73I3YPaKGF3Gu0L-WXlNMJEOQoMmwxqAfEOmXLPL9pOede39Az6SoLCABpLKunKx-QhQxRRyKVGAuwQvM006FZRuV6KfQOc-TDC2oMcSBj7wb3nqDER6tYk1Ghr2IPH83agU4g5u8sro2PLb0uQ8xoIq1Pfm0hkOf2cOKEInRgULydKoZ0gBpC1E1bH3VOyckC6lzIHy5zzkEJC9__rdinXEQmpNPt021ei_kdtlhMKSRn7rSbiGPdgdVCyzZCdUEAeDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه، برای دومین مرحله از تور خاورمیانه خود به کویت رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/130012" target="_blank">📅 17:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130011">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eG30e-R7XenAPMbMdQnzhqTYXIKaMC5-0BDkmJnwvMe8jagP4lFZXSIEdtK_d-FKn-U6ydRksY5El31s6ql7l0nfoJmmRl2SrQtJd7taGm5RMTd0t2ej5sE69EvJ1ys6BUUhCLVI9SqO-wdcRg23SLaDsj74DPcysht3dNH0qTmG0qTTZlgI9k209fi-Y8bNlDNW6MKiJP-ao2GsD5kVE4gvAiIUFHLVZwixhblsLW2ZMP0FY8t46c5mxieg8nsUPWwwna9pK65AwscdP0z5huYa1lPIGmff4A4JYHP26xu79hGzF7MeQhcGZLo2y9tq5B9YtLNF0kSFp1ydiho60Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به زودی کتاب جدید وزیر امور خارجه عباس عراقچی:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130011" target="_blank">📅 16:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130009">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41470bf010.mp4?token=YFoNmkhqlZtaVV7hVjrDzg0G8iLyXJQqVrvfT1fv3jmtNFld8-2zoxAVhTjRTYnvC3Mxp9WDVOsp5EZEY0Pkg7V1U4vb2_V-HK8j3RU8wSOAST_9-EH3mLMGkAAhYKZXIEfj30TZsfKGm3G4-xwVxepM7Ctln_SHQA9u5GaWsHPG0_uqQjYm-lQF06tVpy101BaBujBTixg-8Gc02ER30SgTDxvOvZy3dM3RJBqP70F6nGKJaa-GTnm-Fur2aI3CWTkaeTmyAkaamRsJwYf8pBHhKuZOfRFbYYAgcDSjFZpmNAD3sAWKWvyp_Lg0N5_uy2kiCva-UBYGG8Mrd6U2YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41470bf010.mp4?token=YFoNmkhqlZtaVV7hVjrDzg0G8iLyXJQqVrvfT1fv3jmtNFld8-2zoxAVhTjRTYnvC3Mxp9WDVOsp5EZEY0Pkg7V1U4vb2_V-HK8j3RU8wSOAST_9-EH3mLMGkAAhYKZXIEfj30TZsfKGm3G4-xwVxepM7Ctln_SHQA9u5GaWsHPG0_uqQjYm-lQF06tVpy101BaBujBTixg-8Gc02ER30SgTDxvOvZy3dM3RJBqP70F6nGKJaa-GTnm-Fur2aI3CWTkaeTmyAkaamRsJwYf8pBHhKuZOfRFbYYAgcDSjFZpmNAD3sAWKWvyp_Lg0N5_uy2kiCva-UBYGG8Mrd6U2YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عزاداری‌های زیبا در سراسر کشور
از خون جوانان وطن لاله دمیده
🥀
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/130009" target="_blank">📅 16:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130008">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a64587f2d.mp4?token=u_5ixfpaifKUaT337lJT_EC0Gl2KmwqI3eIhWs_aIcENC92Xybld4yD1CSOHZidagBuDg9-xZOdlmw3LVbqg0OK_KMgZWRYj8KY1IrIUQk5gwyebzRirj4dZIVoapb98Yd6ADmXGMN0qgfw9NWuVAoUMHVZ2oR4I9XAwHeBLMkRsJO8g2VbAVzC1p62Flpw6IkYh0QPgYRUgZSuWqYIVW3gJQot3ktGPrIpiOsyg1ZtY-yvtoJyy6_4EgAR8JU2KBFHNhoezDMkYcGIt4Zdu6YCU0W0vSoGEsxQT9nMXPN80YkA-6zhnWoBQ2GQ9g3ZlpuiiWS5wIR7Nu2NdnwZxUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a64587f2d.mp4?token=u_5ixfpaifKUaT337lJT_EC0Gl2KmwqI3eIhWs_aIcENC92Xybld4yD1CSOHZidagBuDg9-xZOdlmw3LVbqg0OK_KMgZWRYj8KY1IrIUQk5gwyebzRirj4dZIVoapb98Yd6ADmXGMN0qgfw9NWuVAoUMHVZ2oR4I9XAwHeBLMkRsJO8g2VbAVzC1p62Flpw6IkYh0QPgYRUgZSuWqYIVW3gJQot3ktGPrIpiOsyg1ZtY-yvtoJyy6_4EgAR8JU2KBFHNhoezDMkYcGIt4Zdu6YCU0W0vSoGEsxQT9nMXPN80YkA-6zhnWoBQ2GQ9g3ZlpuiiWS5wIR7Nu2NdnwZxUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری شبکه دو: به یه جاتون بربخوره دیگه...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130008" target="_blank">📅 16:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130007">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سنتکام:
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در تاریخ ۱۹ ژوئن در شمال غرب سوریه حمله هوایی انجام دادند که منجر به کشته شدن یک رهبر ارشد داعش شد.
این حمله دقیق علی حسین العلوی را کشت و بخشی از تلاش‌های مداوم ایالات متحده برای مختل کردن و از بین بردن تروریست‌هایی است که به دنبال حمله به آمریکایی‌ها در خارج یا خاک ایالات متحده هستند. نیروهای CENTCOM به همکاری با شرکای منطقه‌ای ادامه می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/130007" target="_blank">📅 16:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130006">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: بازرسان آمریکایی برای بازرسی سایت های هسته ای ایران به آژانس بین المللی انرژی اتمی می پیوندند‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130006" target="_blank">📅 16:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130005">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
فحاشی بسیار رکیک یک دوازده امامی به یک شش امامی در صحن حرم امام حسین
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/130005" target="_blank">📅 16:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130004">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f20ebd3f0.mp4?token=oNmtDYrTiX16f-iKk-VxkSXprhZ-lFZ2yX6L3L3fzEDsBv8_fCjxsHiSDNYSbgLs_D3Dey4DcAEFjQkr3CS2T4hnatH2yqWjBHG-2X98wD-Dhp8uUVvfkLkYbmTwyAYo72xjsfe-vMOEMCfNNKBhqveYICqdVB_FuXRO5ZU89ZaU1jvqGdHGIZhel7cRQe5-m7xGJ3donUbUCvQnrRDj0CCDYXO4FY4G-TO52TSDlN73M_jJsVSpvt6ngVcpndhD8qaHvq5EtlySx0TSec7dX727cpcH2ZcOSgH2N-cnarQusdnsOiE2Q-mBO6P2fk7wqb80aIdBbA3kb4kYiFYINw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f20ebd3f0.mp4?token=oNmtDYrTiX16f-iKk-VxkSXprhZ-lFZ2yX6L3L3fzEDsBv8_fCjxsHiSDNYSbgLs_D3Dey4DcAEFjQkr3CS2T4hnatH2yqWjBHG-2X98wD-Dhp8uUVvfkLkYbmTwyAYo72xjsfe-vMOEMCfNNKBhqveYICqdVB_FuXRO5ZU89ZaU1jvqGdHGIZhel7cRQe5-m7xGJ3donUbUCvQnrRDj0CCDYXO4FY4G-TO52TSDlN73M_jJsVSpvt6ngVcpndhD8qaHvq5EtlySx0TSec7dX727cpcH2ZcOSgH2N-cnarQusdnsOiE2Q-mBO6P2fk7wqb80aIdBbA3kb4kYiFYINw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فحاشی بسیار رکیک یک دوازده امامی به یک شش امامی در صحن حرم امام حسین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130004" target="_blank">📅 15:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130003">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CRwtTj6CZXy7VeXmHloDSQ3kE4VcqFs1mCJ9oL_P390Nb4RME2RbkqlJS3LdXm5xFDzWHN4olzio1pXUMtW_qrJUILu9MF11yyUqksuA5ZDL3pj4hhtPkEVe9_-cM8Ng01s05L5nsz3YXKYoZaDjyLO_LIs6jYrz7TyBORsh2rjKGMT7QTN01g3arGbgUTSO3fhy6LvZX--bkXSYoKxxAf9KlgRMQmWZrpJn15WX5L-_SlXE9Ee5_FccBf9_2Rjw15zYz20ihazHoK0k991KJGAmWDurWoOThIluaw1km4ncVQJPH5a2n4ta1VjKAaJARr8WgpEIXiY9vuLnKqkiaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دادگستری هرمزگان:
حتی تار مویی از ماکان نصیری هم پیدا نشد، احتمالا موشکی که به مدرسه میناب شلیک شده بود مستقیماً به بدن «ماکان» اصابت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130003" target="_blank">📅 15:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130002">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaNTdsZg171-Zopih0zce59BU5XL0v52LPoZM913OrM5ZfKw4f4hwSvfcuUXpYH-IuupJFfX7fEkjUJhekOpyN5tNmkGeuU3vkAgSUP4bm46aVDEHAl1dXMzPZTMyKLIoluBZej_4GRSz9jpWV6feSIyfEyUcFR1qPQAeqfPTN18FdYU9wXGIJGF-BDJ_wy3z_EgnCZ_NH92XB1KGXyrOpXBzNxptLkVtP1HI2vvr3Whv9pjMzpItxNULdisUJ8n17flyo6nVfVGR9lzdzK-OFqRp3pyhP3b36xTOmyUp3oMiM7bRcY0Cq0haiPZPcg0X12wO_BQEUpakZ1F2n99Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ یه پست گذاشته و از خودش بابت اینکه اجازه نداده ایران به سلاح هسته ای دست پیدا کنه تشکر کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130002" target="_blank">📅 15:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130001">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iz5xKlcocjOhoYW1PTY67O3wp8AEXLtibJNxtYoGv7UZhB121JuvhF6c-oa3kGSUeins1HQGJO3hbx1giJjG5wcfebUkhADyh8gltbSGoDUbrlFpXrViF-BTJJWQquFgZ0vBVg5ilvNRQ6snJdr4ogty9Guqgjo1d-4agsZ5I-80Pzh1UGVvwDfsxDdehica7JhsWUXWbBuiN5Wx-oGxAxj9bB9qxTXGrSeqrjvQYsYxUcrELAB7nozIyyvIGkjMR_QkEb7l5hq5z3j2JhuXMVYsaKyY0UimiTF8uwRiXDL-kN_INExu1KRJ_XEtdWgxgWFQfjjmm5UdB19FF2WehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار قالیباف و الهام علی‌اف در باکو
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130001" target="_blank">📅 15:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130000">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزیر خارجه اسرائیل: مذاکرات جاری در واشینگتن میان اسرائیل و لبنان تاریخی و بسیار حائز اهمیت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130000" target="_blank">📅 15:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129999">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEeuSLIdSoS2Pj_NyCKjT3K0l3ubgl20COyENPqXihIVfY66ehMYK91CX5AxRAhbdAB1ll9XoPxU9IyiI4O8uDMX4dSxr-0nsYWJ6LczkTMY56S4_WtZLGz9m0dECH7yq7jKERmfuTbeHsYcSqJ_sYm_lHk8bneKJj5u9ipx2qtUNgvIebxxccF3ECtvGmRlt3AjZHEUTqNLlIlRgE89gt_LJ9g79pxwpf8Ty6rrIwKA4vd8814SHXvxboEkxPeaTrHVje-09NgjaQeA7MT4skvGJO1oSBkza42F7adZPjUwVPqYigpTRhc4Q3lmT-ZztoWNogRTuEb1vtwefRuwuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: ایران به آمریکا اطلاع داده است که برخلاف گزارش‌های دروغین اخبار جعلی، «هیچ عوارض گمرکی، هیچ حق بیمه و هیچ پرداخت دیگری از هر نوعی توسط ایران برای عبور کشتی‌ها از تنگه هرمز درخواست یا دریافت نمی‌شود»
🔴
اگر این اطلاعات نادرست باشد، مذاکرات فوراً متوقف…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129999" target="_blank">📅 15:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129998">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEINl8nLwOUl9CZvU_XuCBWxFS8uBjhRp8cklym7H-vTX3MS3eWrXgdoVqaiaQZXmDCE5g-BwBuV-VL_BIPN03ItlqgTXe2Q1FJLpA2DbFEry6pwRQ-BDI3cWntRjfAvWg8TW_R3Defibb_Uo3aZ82P1uXYVbSx3AoBhbGWVtC43E8kIvkonYpTAFU0minXMZTuyrQi4T16Li5kgbXrJbzLtEZbtZkAgXXGjHQJUl-ivHcIsF22FgEgPfZUCpBP4835LHopa6bo-klQqwAD7NQQZl-vFGPpUC4xIOyAUl97TxE0WXJNbFjFrxvjhWZhMLQbl8IClzfvImLwHE3KQZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ
: ایران به آمریکا اطلاع داده است که برخلاف گزارش‌های دروغین اخبار جعلی، «هیچ عوارض گمرکی، هیچ حق بیمه و هیچ پرداخت دیگری از هر نوعی توسط ایران برای عبور کشتی‌ها از تنگه هرمز درخواست یا دریافت نمی‌شود»
🔴
اگر این اطلاعات نادرست باشد، مذاکرات فوراً متوقف خواهد شد! علاوه بر این، هیچ پولی به ایران منتقل نشده و هیچ منابعی از صندوق‌های آنها توسط آمریکا آزاد نشده است
🔴
ما بخشی از پول آنها را که کاملاً تحت کنترل ماست، به کشاورزان و دامداران خود اختصاص خواهیم داد تا ذرت، گندم، سویا و سایر مواد غذایی را خریداری کنند
🔴
ایران به شدت به غذا نیاز دارد و ما آن را صرفاً از ایالات متحده برای آنها خریداری خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129998" target="_blank">📅 15:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129997">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vU7GzRP2RpyUC1K_8hFPNO0CUJAd0v5EBred4AHvhcpPq7VHWobXmy_yioaxZ57EGS--MB_HL6UlL-Igy-X2TeCbA96CzLBkRH22ingjcLF5SSOdT3j33X4vPNsZwz3OS6O_ozBSK1MRmvzFksEYBhjIjZZ4_QDb9dx9BN4SHQqSw8EcRO2PFrhfAw8-gtZV-wUTmkfhUf9eQ578g00subsepatnJ-f7bi8ZvJwiBaKUiR6271KB4qsSW7XSEt3GJb_JnUKs91XrculzF5YMNKeTAgixZEaKuVlK0XPUzJUnVnybESFnSmb3g6cW7RQ4legQdoWiEgbECuVvsV98fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مصاحبه وزیر میراث فرهنگی با خبرنگار اسپانیایی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129997" target="_blank">📅 15:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129996">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=RK3bHP895GB0T6UFx3b4q7osV_elrqVTl_tymduFDQiZMvfks-kBe462f37rdhLidicvNhv3OLDpKC9PQPl1XiHDoGgcTdf959Yy-xGqMWK5QBHcC7fUA5e0WgWoQFefzaAAgnG7rLUpQF6Tw8Rq6jZjJ87dq-jJWZoyTF5EPVGd6lYkZ1217KIXgGZpEOL3KAlS0qyMf8or_yb6Y1WUWn9dmGdbyYuWVu4GkWGMuupp_tvSlB9nrJvcTj1xXUtAC_HTsHqFRc59SIusSDcBZLDqzvmdjo0pjCWJIDOIdzxc42jQso2cFkyXVCPbVn9TgI2bAirPt0cfFogMVUuPAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=RK3bHP895GB0T6UFx3b4q7osV_elrqVTl_tymduFDQiZMvfks-kBe462f37rdhLidicvNhv3OLDpKC9PQPl1XiHDoGgcTdf959Yy-xGqMWK5QBHcC7fUA5e0WgWoQFefzaAAgnG7rLUpQF6Tw8Rq6jZjJ87dq-jJWZoyTF5EPVGd6lYkZ1217KIXgGZpEOL3KAlS0qyMf8or_yb6Y1WUWn9dmGdbyYuWVu4GkWGMuupp_tvSlB9nrJvcTj1xXUtAC_HTsHqFRc59SIusSDcBZLDqzvmdjo0pjCWJIDOIdzxc42jQso2cFkyXVCPbVn9TgI2bAirPt0cfFogMVUuPAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب صداوسیما یه نماهنگِ سرطان پخش کرد؛
بعدش دیدن خیلی کسشر و آبرو بره، کلا گرفتن از آرشیو شبکه سه هم حذفش کردن
😂
😂
😂
علی بیرو تو دروازه یا نیازمند ، کنارش شجاع و کنعانی میشن پدافند
تنگه هرمز ما تو دستای سعیده
شوت‌های قدوس و رامین مثل خیبرشکن، مستقیم به قلب دروازه‌ی دشمن میرن
ترابی دریبل‌زنه، نعمتی هم حامیشه، مثل هایپرسونیک از لای دفاع رد میشه
یه طرف میلاد و ازون طرف جهانبخش، پهباد شاهد رو روی دروازه میکنن پخش
حاج صفی ، حردانی و یوسفی مثل شیرن
توپ‌های علی علیپور از پاتریوت هم در میرن...
@AloSport</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/129996" target="_blank">📅 14:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129995">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptkWMUcSBZEoR4InsZeQqGnXUNP2LOVoBvp1f9_jLV_WXQy4tmDWbHQGmcG-6SFAyoge2WdlneVIubmaZXjsuXs8TCTM3KnaisZH3mezWumZwIo8Y5QGoivB_X1qekFwQBspsMXQHNnnO91Y9iDGxM4jEWuQEVKEUb_lF21PRk7OPx1hhZnbPD3e6C_fdXOMvGOEB4B9tJOFwqe7BGERy3BQdzjqmeGYxHrI1xqtUO33u7VyCDMa3WxFl6YmDb6HbDO08apQQ9PnkCoy8ZsNjo_GRAN9zg_4o5K7jbk8i1XRUmMelMp0f_GpMZsX9NLrh7JWiV-8hH5ZY6x_wXKlUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فارن پالیسی:
توافق ایران زمینه درگیری‌های بیشتری را فراهم می‌کند
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129995" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129994">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XLmOKG3YPmXOORzohv3iYT3TJl9upQiIelkDjuT0UbxgeCCZ2iW1tUVkZRCBKnOWNObdf8_oXCKtOKaCEuIYK_Xs_VOts_T0bERzEEkOc-HuAJXRniaQX0U3XVKmnnj1GYi8xcdXTKtcYk4PyWTGyQ0RwSM-48eZjrw1ZilpNZuHauM47O0lMIQkIJS-krBozT26cEWUcsrXHPWPqlJrLNm6fbh_6M28OZFZlVlDu8eOzweSeKG_IvY1EjNZIQMlGex4fA_oj_46_8Rcn2OwT1aOgXE9_AMDrK2LuTL8uUN-BS3jjfmyYKtvZNuvwu5uwwnULZa9oqAB3KwaocJd2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا ایران ۱۰ فروند هواپیمای مسافربری بوئینگ ۷۷۷ به صورت دسته دوم از عربستان خریداری کرده
🔴
تصویر ماهواره‌ای ادعایی از اولین فروند تحویلی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/129994" target="_blank">📅 14:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129993">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل:
حتی اگر واشنگتن از ما بخواهد، از جنوب لبنان عقب‌نشینی نخواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129993" target="_blank">📅 14:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129992">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uz5qBDJkBGbApcD07QtnswCrbGHberOE96G5OmbET2wlAlV-uhSsUU4xk7_c46BnPex-PqpUJMU-AvLdr0btef87GsNu3b_BwwCInFEtZlFDdt3znHI2zunJP-sZ4W04Hx1y6nA885xeq0Vt5FfmSQ5wte_SGBwWbyq5vLK9nVtp58tyDdiNuJD3EAmBAxpeyx1rx6jR98wTw6upPPgkao6CQD6u6y-ajK7O3jp1LTK4O2-pNMXrFtv8zmXeBUfHQ5DzQF0C1zHVZ8YBgZEBYUMP9rCfYQK4aKsxEHwGvdd-8UNjlSiurJTT-J3adipB-WImXC1rkUkZlBYJB9V3lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی: برنامه‌ای برای دسترسی به تاسیساتِ مورد حمله واقع شده و مواد هسته‌ای وجود ندارد‏
معاون وزارت امور خارجه:
🔴
در سوییس هیچ نشستی با گروسی، علیرغم درخواست وی، برگزار نشد.
🔴
هیچ برنامه ای نیز برای دسترسی به تاسیساتِ مورد حمله واقع شده و مواد هسته ای وجود ندارد.
🔴
این مباحث صرفا در چارچوب توافق نهایی و در نتیجه اقدام عملی طرف مقابل در خاتمه تمامی تحریم ها و... بررسی و تعیین تکلیف خواهند شد.
🔴
نمی توانید با هیاهوی رسانه ای، سیاست "راه بینداز و جا بینداز" را پیش ببرید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/129992" target="_blank">📅 14:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129991">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
دلار با افزایش قیمت به ۱۶۵۰۰۰ تومن رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/129991" target="_blank">📅 13:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129990">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سخنگوی پوتین: سلاح‌های هسته‌ای تنها چیزی هستند که از جهان در برابر یک جنگ جهانی محافظت می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/129990" target="_blank">📅 13:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129989">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وقوع تیراندازی در آنکارا
🔴
رسانه‌ها از وقوع حادثه تیراندازی در آنکارا خبر می‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/129989" target="_blank">📅 13:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129988">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ایسنا: اختلال خدمات کارت محور بانک‌های کشور برطرف شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/129988" target="_blank">📅 13:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129987">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baGRjlpiFapIw431STi7vZVPjtKX7A60HGxkVg4QEySbpId5nKnzv-k_CB9zoZpIGgQyvXPp33lv0S5_8ycGFKJ6DHE_jFRUorv3BXU8xCiEyn1fwAzKTo0iYIErlLoqpURZHBtQ-yi-sjAzhQ_oGY_avWB4nSimGvF3X9S3leVaItBcrQaj6uH-IhWkyiCLnagObF2ZUPc3NFN0FtaNCwLUkSHf-76gDEQn9hYraaIcmVL2MXT4JhbBdDmTBgy1FD35sx52lxp0t0HfB5vi315v6tomxZ56B0OGMR5uP8N-wb2Kj1cZXbokqjFPRMbGxQIph71oLocywcsRRFQ1vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تایید 4 سال زندان برای دو ورزشکار ایرانی در کره جنوبی به دلیل تجاوز
🔴
دادگاه عالی شهر دائگو در کره جنوبی با رد درخواست تجدیدنظر، حکم چهار سال حبس دو عضو کاروان دوومیدانی ایران را که پیش‌تر در پرونده تعرض جنسی محکوم شده بودند، تأیید کرد و به این ترتیب، رأی صادرشده جنبه قطعی پیدا کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/129987" target="_blank">📅 13:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129986">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egHpGPYqArjWTTND0DSCiE08tNzBcO4en_eWDA5gd32OMvSrDg72ic4fqOa8Is7pMClIMwJ3dZvK3jrR6w496KVwEN7LGlrcaofhnr_n6At2A-EqyhghozYjXfYuhbSTUgeNzV9JcdHo8jUzPtmwLalrX_etmcGYQpD84fBtXeh0qv4U_fX34U-AqVYkcL8refkkfdK_AWupzVqIUr8OtJTcC2_GsM7dbqPCrtXYBwBSpLZhaYjIV9HVQvetG-8zJJUPsXnh8FhQUPkvlenw-0_GdOYmKlbv9RxSmqizHmQ7CM9qj9_1fcPfRNO-s1D9TYcqqz8SpPJ3w01jr2DZJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: تاسوعا رو تسلیت عرض میکنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129986" target="_blank">📅 12:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129985">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=UlR94t-JqqFHjBI_3rmVMLN1cdFV5ohjgwxXvbx7bQk1OnyPPR2nB8439o5hZnc53vbMjl8FeXdaRGnS9IWuRp63-MV1JG4XbU9g3Z1Ha9AQuVuQQ7qNphrEtg7xxzCIZ1Y7gmd28uVqRylna30IDLekG1JvMgRfBD4NFs8-UazFRJkiLH11uoxYGGt9eNEPjtdGlQFxmDFV86GGyi7-9yM_wi1El-O9wFVgBQLpCX81t5Ggf4zyMKA0XkM50nnDSmB-QIR21lRp9BpefWyQVxr_6ILPHyN5B3hmkwfL404j_Elc5rQ5lxQNk_pw6BG1j-OtmhGJ3_Qte0j-Qq94mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=UlR94t-JqqFHjBI_3rmVMLN1cdFV5ohjgwxXvbx7bQk1OnyPPR2nB8439o5hZnc53vbMjl8FeXdaRGnS9IWuRp63-MV1JG4XbU9g3Z1Ha9AQuVuQQ7qNphrEtg7xxzCIZ1Y7gmd28uVqRylna30IDLekG1JvMgRfBD4NFs8-UazFRJkiLH11uoxYGGt9eNEPjtdGlQFxmDFV86GGyi7-9yM_wi1El-O9wFVgBQLpCX81t5Ggf4zyMKA0XkM50nnDSmB-QIR21lRp9BpefWyQVxr_6ILPHyN5B3hmkwfL404j_Elc5rQ5lxQNk_pw6BG1j-OtmhGJ3_Qte0j-Qq94mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرباز روسی که با پهپاد اوکراینی روبه‌رو شده بود، از اپراتور درخواست کرد که اول دوست کنارش رو بزنه تا بتونه سیگارشو قبل مرگ تموم کنه
🔴
اپراتور پهپاد درخواستش رو قبول میکنه، اول سرباز دیگه رو میزنه و بعد سربازی که درخواست کرده بود رو میزنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/129985" target="_blank">📅 12:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129984">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
بعضیا هیئت عزاداری سیدالشهدا رو به میتینگ سیاسی تبدیل کردن تا به امیال خودشون برسن
تف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/129984" target="_blank">📅 12:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129983">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa3359d12.mp4?token=dGcy9O-aNy_Q18JHnfigpJPU92JMnnFKtQTCG9JF190iWAFUmN8gy9SfwDaPkP_MtbsTdii0BLOMEI_bjJoQz2pOHnYWRiQ6OXpogIH-YU0XHHmkU0SV4bkv5IF_dCiHNPLTEW7gYiDvmq33va1EtZoFrxFpHyjrx9FS7wuPSeFtEL59kESw2mGQHA2ts7IJV_3pRgT-y28j81HE8TqnjPvpqomXzGP_CDwGVLKrgawSpJnvLPd-VZhi6C-as9hFDitgNNn-WJ1aTPr6jDpsHxjH99ixarhd_mbWRqONBAW8rAVcnCPYLbm5ovpcEn4BJbxu9Fji6cCuRoMCmCLp2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa3359d12.mp4?token=dGcy9O-aNy_Q18JHnfigpJPU92JMnnFKtQTCG9JF190iWAFUmN8gy9SfwDaPkP_MtbsTdii0BLOMEI_bjJoQz2pOHnYWRiQ6OXpogIH-YU0XHHmkU0SV4bkv5IF_dCiHNPLTEW7gYiDvmq33va1EtZoFrxFpHyjrx9FS7wuPSeFtEL59kESw2mGQHA2ts7IJV_3pRgT-y28j81HE8TqnjPvpqomXzGP_CDwGVLKrgawSpJnvLPd-VZhi6C-as9hFDitgNNn-WJ1aTPr6jDpsHxjH99ixarhd_mbWRqONBAW8rAVcnCPYLbm5ovpcEn4BJbxu9Fji6cCuRoMCmCLp2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بند دوم تفاهم‌نامه نقض شد
🔴
شعار مرگ بر آمریکا در حسینه زنجان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129983" target="_blank">📅 12:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129982">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
اینم یه عزاداری زیبای دیگه
از خون جوانان وطن لاله دمیده
🥀
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129982" target="_blank">📅 12:34 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
