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
<img src="https://cdn4.telesco.pe/file/Sw6rLk3K6jIHpErAQS9UTOwgOjR6XoONE_D-mcaAx6JgAVHlXVWrHwyeCoV6jzwdO7ki2Pzyq_8qMqVxj-OjoJzNaOrrhStf6oZ9qFYpzYx0gT507yi9OjRcNfIy00vl6sZfrMCngTljYVb8wat6UJOob0MU2GLOakTIzRgXOEX9F-U84xnMrWpid69u3miIUMVdy51OEJVbxySkyzn_mYbNBgxkOItOLrz2TsxLdwNu-sxZForYckdASU2gvAoW8iF8d0aBOpfZJUKJy0vuaoIeVQ_TmwGicxsrjz6dgkAMpChq8rXMwX7f8jYadHmnyJ_nw4vgBh-wv0kyspOLsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 988K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 13:26:02</div>
<hr>

<div class="tg-post" id="msg-142603">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
رئیس اتحادیه کسب‌وکارهای مجازی: حدود دو هفته است که مجدداً صدور مجوز پلتفرم‌های آنلاین طلا متوقف شده است. قرار نیست نظارت مانع فعالیت کسب‌وکارها شود
🔴
باید میان بانک مرکزی، اتحادیه و سایر نهادهای نظارتی تقسیم کار شفافی در این حوزه انجام شود.
🔴
معتقدیم باید چارچوب‌ها به‌ صورت شفاف مشخص شود تا کسب‌وکارها بدانند چه نهادی مسئول چه بخشی است و فعالیت آنها در چه چارچوبی باید انجام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/alonews/142603" target="_blank">📅 13:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142602">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qz4AI2CqtXzC8B_bt9Gn0vy1mZnQ7_lPNwo__lng9mIISCNebrGZfx_nz0qZjlBduao1hqbt-yXBgl2OaA8m3S9JXPNTwY5E-PClsjZadmDEyTV0Xqx1mO8uI2OMONlmQqWLqfTq0sBF7Wvv3KNvdEoL0BEOPVlLMnxOYc9w4uBgRZ6l9izx4M-A3a4DACARzL8rJj0hdec0D4DnS3vP0NEOsJaSkx3hkl23hfvv3qwiVH_DhRgleVAcNLS7ja0wyRvneOgN8PIBYU4R1XBAYtWRDSG8EeldoZSui71R8larkutXLtmZrv9UifOcqkz6gPH_8198zZo5qJx0K4D7hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار محمدباقر قالیباف با رئیس جمهور عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/alonews/142602" target="_blank">📅 13:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142601">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وال استریت ژورنال: مقام‌های عرب می‌گویند ما «بین ایران و آمریکا گیر افتاده‌ایم»
🔴
آن‌ها معتقدند ایران در نهایت به افزایش فشار اقتصادی، واکنش نظامی نشان خواهد داد، در نتیجه، جنگ دوباره می‌تواند شدت بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/142601" target="_blank">📅 13:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142600">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
بلومبرگ گزارش داده دو نفتکش غول‌پیکر مرتبط با چین در میانه افزایش خطرات کشتیرانی در تنگه هرمز، مسیر خود را تغییر داده‌اند
🔴
نفتکش «سی ۵» که حامل نفت عراق بود، پس از حرکت به‌سوی هرمز تغییر مسیر داده و در میانه تنگه لنگر انداخته است. نفتکش «هستیا» نیز پس از ورود به خلیج فارس، مسیرش را برگردانده و از منطقه خارج شده است.
🔴
وقتی نفتکش‌های بزرگ هم ترجیح می‌دهند برگردند، نگرانی از امنیت هرمز دیگر فقط روی کاغذ نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/142600" target="_blank">📅 13:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142599">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
روسیه و اوکراین ۲۰۶ اسیر جنگی را مبادله کردند
🔴
وزارت دفاع روسیه: ۱۰۳ نظامی روس از قلمرو تحت کنترل رژیم کی‌یف بازگردانده شده و در مقابل ۱۰۳ اسیر اوکراینی تحویل داده شدند.
🔴
براساس اعلام این وزارتخانه، تبادل اسرای جنگی با اوکراین با میانجیگری امارات انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/142599" target="_blank">📅 13:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142598">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نایب رئیس کمیسیون امنیت ملی مجلس:
به زودی یک «معبر جدید» در تنگه هرمز، غیر از مسیر جنوبی، در قالب بیانیه‌ای مشترک با کشور عمان اعلام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/142598" target="_blank">📅 12:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142597">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2424f78cb2.mp4?token=OcNtyTRh4ASyUCUXZRWUd3hsajl9ybBlPKLZRXn-f7f0_VpmHzEjQhWrlDENkGI03HzCMDhLWkN2YW-jPZfEpx5-fAwdm-5t5IlRoviq-0SeE-9bz_94W8nUzxOrE8YmRbGsBddqkjJZN6T0Gdd3BGQz49V7cxOIfSYGLFxERmbrXPlcAkNBcRTLS4qV_R7nDJOPGQBcMdPzyd24gHcukjBPjD3vtaIbLuK_gGeIi0VKFq_DbWk-9fnQJ19P3WY8pijAcUWExNZ4xR9xnPktCIebsok4yqJNkPvftzjxLvfWRZ9pFx8AE8ZZfB4S7ahH30UEiBGvmbMSh_wKL5UAX6Ph_IPNZ2OSO3YalIsQpUBA0eP84-UtDw-2_i6x9lDpVPG4Qt2lS6qA7hVVWMK1ScRI4bOFqeRHR7y24hyTQsI7uhGZ9ZpkUA8kkSUjOhDZf0i0STzemhwx8OLiOzKcfLaFkZ6CRa-JKix55kWFmWYhMQM0y4fUVys6Nv8EEcKPixcwXWDjYiFuvxL90ln-zPu16mIh-mls2kZhCnrS9OxE9TXkfMNK1BduFqBhsqkKOHXN28puLZXhTYM6FAGJ8rFf-91jKQCt6UzsIX6i-F7Cd8BeZ2ISSBwa4oOnjvkfMVWznhC9LFsY8sE74ItJNoWkgjFrYNbVvmURJ4Z5V48" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2424f78cb2.mp4?token=OcNtyTRh4ASyUCUXZRWUd3hsajl9ybBlPKLZRXn-f7f0_VpmHzEjQhWrlDENkGI03HzCMDhLWkN2YW-jPZfEpx5-fAwdm-5t5IlRoviq-0SeE-9bz_94W8nUzxOrE8YmRbGsBddqkjJZN6T0Gdd3BGQz49V7cxOIfSYGLFxERmbrXPlcAkNBcRTLS4qV_R7nDJOPGQBcMdPzyd24gHcukjBPjD3vtaIbLuK_gGeIi0VKFq_DbWk-9fnQJ19P3WY8pijAcUWExNZ4xR9xnPktCIebsok4yqJNkPvftzjxLvfWRZ9pFx8AE8ZZfB4S7ahH30UEiBGvmbMSh_wKL5UAX6Ph_IPNZ2OSO3YalIsQpUBA0eP84-UtDw-2_i6x9lDpVPG4Qt2lS6qA7hVVWMK1ScRI4bOFqeRHR7y24hyTQsI7uhGZ9ZpkUA8kkSUjOhDZf0i0STzemhwx8OLiOzKcfLaFkZ6CRa-JKix55kWFmWYhMQM0y4fUVys6Nv8EEcKPixcwXWDjYiFuvxL90ln-zPu16mIh-mls2kZhCnrS9OxE9TXkfMNK1BduFqBhsqkKOHXN28puLZXhTYM6FAGJ8rFf-91jKQCt6UzsIX6i-F7Cd8BeZ2ISSBwa4oOnjvkfMVWznhC9LFsY8sE74ItJNoWkgjFrYNbVvmURJ4Z5V48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاسگاه پلیس ترکیه هدف پهپاد قرار گرفت
🔴
طبق گزارش رسانه‌های ترکیه‌ای یک ایستگاه پلیس در استان «ترابزون» که در ساحل دریای سیاه قرار دارد، هدف یک پهپاد قرار گرفت.
🔴
«ترکیه تودی» گزارش کرد که این حادثه دیشب در منطقهٔ آرسین رخ داده و تلفاتی نداشته است. فرماندار ترابزون هم پس‌از بازدید از محل حادثه گفت: «اطلاعات پس‌از تکمیل تحقیقات در مورد منشأ هواپیما ارائه خواهد شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/142597" target="_blank">📅 12:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142596">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: وجود یک رادار پیشرفته ترکیه‌ای در خاک سوریه به آزادی عمل هوایی، نه تنها در سوریه، بلکه در ایران نیز آسیب خواهد زد. حتی هواپیماهایی که تلاش کنند مخفیانه به سمت ایران به پرواز درآیند ممکن است کشف شوند، و این نشان‌دهنده میزان خطر بالقوه در سوریه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/142596" target="_blank">📅 12:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142595">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoVgsrLthmV8p2XYHvykFC3q4ps4wPJD-ZO31Mfqh3wsL6Mm7WyDP7voW75I5gJNpe9IEY3l7oCPYZIZSlM0VmgY-utb4rGPl_thr-OLrxBPPjLffiOOCpGPB8fe1fsNCefbzTf7Vv1AIMQH9qC1o4GsEDK3Sjv7zMJmEVwwtNvYuNOefs-7xHF5eBikAShPFrPNg5S1tSGbVYWeUkwiD7aR0U51EYFUrJ4FuzYo2_wRVboZMUeYYLL-0ELLSZmPfZ62pv7vS68vuZxTGNXtG8U2UG-mXQwT460XGPxuQ9WnJjAc85ErLIRZNROesVupw2I0-4SPQcr4IgVl-7kZIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یاسر جبرائیلی، فعال سیاسی: بنزین ۸۷ هزار تومنی در کرمان عملیات فریب بود. بنزین شده لیتری ۳۰ هزار تومن و به زودی اجرایی میشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/142595" target="_blank">📅 12:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142594">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: تهران عملاً مسیر کشتی‌ها در هرمز را تعیین می‌کند
🔴
آنچه امروز در تنگه هرمز دیده می‌شود، بیش از آنکه نشانه موفقیت محاصره آمریکا باشد، محدودیت قدرت واشنگتن در برابر توان ایران برای مختل‌کردن یکی از حیاتی‌ترین شریان‌های جهان را نشان می‌دهد.
🔴
بر اساس این گزارش، ایران عملاً بر مسیر عبور کشتی‌ها اثر گذاشته و آمریکا میان پاسخ نظامی و خطر گسترش جنگ گرفتار شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/142594" target="_blank">📅 12:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142593">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
خوش‌چشم تحلیلگر صداسیما: باید آب‌های فلوریدا رو با مین‌های هوشمند مین‌گذاری کنیم؛ این کار می‌تونه یک حواس‌پرتی استراتژیک بزرگ برای آمریکا ایجاد کنه و واشنگتن رو مجبور کنه بخشی از تمرکز و توان نظامی خودش رو از خاورمیانه به سمت سواحل خودش منتقل کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/142593" target="_blank">📅 12:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142592">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
مدیر شرکت ملی پخش فرآورده‌های نفتی منطقه کرمان از افزایش سهمیه بنزین کارت سوخت شخصی شهروندان استان به ۱۶۰ لیتر از ابتدای شهریورماه خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/142592" target="_blank">📅 12:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142591">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
فارس: ۷.۵ میلیارد دلار ارز نفتی مرتبط با فروش ۴ ماه اول سال در اختیار بانک مرکزی قرار گرفت
🔴
فروش نفت کشور در ۴ ماه اول سال همه مخارج ارزی دولت تا دی‌ماه را پشتیبانی می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/142591" target="_blank">📅 12:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142590">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
اکبر رنجبرزاده، عضو کمیسیون صنایع و معادن مجلس: آتش‌بس پس از جنگ‌های اخیر فرصتی طلایی برای بازسازی و نوسازی تجهیزات نظامی بود و اکنون توان دفاعی جمهوری اسلامی به مراتب بالاتر از زمان جنگ ۱۲ روزه شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/142590" target="_blank">📅 12:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142589">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRJQWZMu5HOjodIwHKEkIxMM8vYxL1wLHRYES4jiyG62V48FpBtTap6gpQJqoat6cdYEcqh1CDMsrKz6COYeuygS5Dn-H6C3Igf0MeOubL5SHhoH34_bU_NoWeG1Dzspl8YJ-I_EsyVZgbvU3KoTLZJChf414-kZ3DfwnRZiRYdoFdscu2ok-7EwoZb2UjnOuH8JbTfd8tMjjPAZL6SHXAp7O9Td8SDtdCWbENKpcUTA42lAKa7NNCR7fvsinWB6eFOiCgDSnRPnuXU8b6zVsE7CiolHMHamgSbjOEAEZrjc-Jtce4NGHG1QST4i7IbbxdkKQ2l9PWiaQI1XlEjSZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زاکانی: مردم عزیزمون بالاخره طعم ناب مدیریت انقلابی را خواهند چشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/142589" target="_blank">📅 12:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142588">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">طلای آنلاین نخرید
⁉️
حتما اینجا چک کنید
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/142588" target="_blank">📅 12:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142587">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sk0w2U7fHil29SiTrf1Us5atCzlyFh9cnO4oj_kmomOfUbuMG5tN6aywjsKO6GJpT7r7C5BZD_v7hP-AfVlxCLSyzxnnn0W83pvtopV1hQEhdzfkcqegY_v1DFUlj7iHlhVel8mnkT8sxeG9FhRd4CiU6O9cRljGI3dh37jmMVoqlECrNXUJ-wLoXWG4qMLuJxma7p1CWAnAMbHXAbouYiyDviC9w7rHqGgdEJng7ZHlWdGKj7Azq7n_1BvC5fcELR1NpgCqCMUGM1mgP0D8PYRZZFWstbFSriZ4HIhO1gvAxb5ieTytrOl6QgHzt_IVuEXNRgEMBDPR2wIoXySsCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار رئیس ستاد کل نیروهای مسلح: هرگونه کمک و تسهیل‌گری به آمریکا به منزله مشارکت با نیروهای نظامی آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/142587" target="_blank">📅 12:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142586">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وزارت دفاع امارات: هدف حملات موشکی امروز شناورهای دریایی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/142586" target="_blank">📅 12:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142585">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سازمان سنجش: در کنکور امسال ۶۵ درصد خانم‌ها و ۳۵ درصد آقایان شرکت کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/142585" target="_blank">📅 12:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142584">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2IUPFlgSMN5va3OT4trWmeaOTMRAqUPyi9hQ2BfyKHr0P6qlukS8BUyfZSPF5meQDo6N-xvc6Nac3H629AuBwQznCGfj4nDZ8x2GRJ2gHOa-zVNkCzCqahApS_PW6rh8Cne5SRVvAtYJvhXDLFBmmx7oKoRSEbcstgIUa92_O3wwjrIeqqbzct1xtz-oNjvVTR-4-YiBea0YiF2OLFlagoU3t1pPfzXa2EfBT3fPupDxlmol2DUFlieiXRB_ZqSwQVt-RsgOwDLz3ZyZiTxrtgDMvt-eirIvQa8FlErKUBl-3odMP3A2t79jWQvG_AEqcxmNdUwPwK_xcfQLhLjPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آنژی نیکسون، نماینده مجلس ایالت فلوریدا، فعال سابق اتحادیه‌ها و عضو سازمان سوسیالیست‌های دموکراتیک آمریکا، با یک پیروزی غیرمنتظره، در انتخابات مقدماتی سنای ایالات متحده از حزب دموکرات در فلوریدا، به پیروزی رسید.
🔴
او الکساندر ویندمن را شکست داد، در حالی که هزینه کمپین او تقریباً ۱۷ برابر کمتر از رقیبش بود. اکنون او در ماه نوامبر با اشلی مودی، نماینده فعلی جمهوری‌خواه، رقابت خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/142584" target="_blank">📅 11:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142583">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏
👈
مرگ ۱۸ زن موتورسوار در اصفهان در ۴ ماه
‏
🔴
فرمانده انتظامی استان اصفهان از جان باختن ۱۸زن موتورسیکلت‌ سوار در حوادث رانندگی ۴ ماهه امسال خبر داد.
‏
🔴
بر اساس قانون،هیچ یک از شرکت های بیمه، متهعد به پرداخت خسارت مالی و جانی به موتورسوران بدون گواهینامه نیستند و به محض وقوع حادثه، موتورسیکلت متخلفان توسط پلیس توقیف می شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142583" target="_blank">📅 11:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142582">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
جروزالم پست: تام باراک، فرستاده آمریکا، هشدار داد که حمله هوایی اسرائیل به پایگاه هوایی ابوالظهور در نزدیکی ادلب در سوریه می‌توانست به تشدید تنش و رویارویی نظامی مستقیم، احتمالاً با ترکیه، منجر شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/142582" target="_blank">📅 11:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142581">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
شبکه CNN به نقل از مقامات ارشد کاخ سفید: در روز های آینده تحریم های بی سابقه و بسیار شدیدی علیه ایران اعمال خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/142581" target="_blank">📅 11:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142580">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
رئیس سازمان سنجش: از عضویت در کانال‌های خرید و فروش سؤالات کنکور خودداری کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142580" target="_blank">📅 11:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142579">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cee250a30.mp4?token=TC1ZP9GIs6ySFwCjRT8AVJIaHiwrHYag0vY3tDwhARBfF2deKsrh5SU2WMqdJNrWJXwVhhMa3YmRiNZm8YXy0pIodWRC8PCBaipYJjplkpZNBFQPCHbZbfZ-WB0avlERyGobpIk4ng_TkRe3QcW79j7GuWxdrHR53mDtivc3wpomgjAKCpDXZ0qeLwZLZz2LYlhid-m_Il5a27_cPW7mSz6x6GKDNheUdSR5Zx7BCI0DyUd1RBkBBqK35odOKl784geO6Pt7ws4zttp0u8j-Waptc-4LOiftgD7_Ohvzl1AprGnP94g2zYRvws7WXXtKulI0XncUGEogM2Md8yOD7gQhIAOeqQAP60qs0SDcS48cTnQJUNaQjg6GrYJCl8v8VsSxQacjPlHlnrqLh_SlMBQK5OUPqJ148O2X-hHYcg3vblPpLiBNhZ2NU1BWxbz7wf0asHNAi3WxItGpGIwsYv2Fd7ZgFQW5mqime95UmJs6ILIvRpqtt95RxzTFm5CxUPoTDTfzuJugkGqdqczxPzFQWqK46qWdoQS2QL7vw65rQ5uM75KzWfEprXj_7eYxcOI1nofVWLAhSSBQmxeRdv_CJCYASxX_qR1S1DTktos9Be-elQYL3Nbqb-g8YhGSIABBobiZizHxWpBOjqXru-4wWzhY2kdAIVJNHjCj0kc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cee250a30.mp4?token=TC1ZP9GIs6ySFwCjRT8AVJIaHiwrHYag0vY3tDwhARBfF2deKsrh5SU2WMqdJNrWJXwVhhMa3YmRiNZm8YXy0pIodWRC8PCBaipYJjplkpZNBFQPCHbZbfZ-WB0avlERyGobpIk4ng_TkRe3QcW79j7GuWxdrHR53mDtivc3wpomgjAKCpDXZ0qeLwZLZz2LYlhid-m_Il5a27_cPW7mSz6x6GKDNheUdSR5Zx7BCI0DyUd1RBkBBqK35odOKl784geO6Pt7ws4zttp0u8j-Waptc-4LOiftgD7_Ohvzl1AprGnP94g2zYRvws7WXXtKulI0XncUGEogM2Md8yOD7gQhIAOeqQAP60qs0SDcS48cTnQJUNaQjg6GrYJCl8v8VsSxQacjPlHlnrqLh_SlMBQK5OUPqJ148O2X-hHYcg3vblPpLiBNhZ2NU1BWxbz7wf0asHNAi3WxItGpGIwsYv2Fd7ZgFQW5mqime95UmJs6ILIvRpqtt95RxzTFm5CxUPoTDTfzuJugkGqdqczxPzFQWqK46qWdoQS2QL7vw65rQ5uM75KzWfEprXj_7eYxcOI1nofVWLAhSSBQmxeRdv_CJCYASxX_qR1S1DTktos9Be-elQYL3Nbqb-g8YhGSIABBobiZizHxWpBOjqXru-4wWzhY2kdAIVJNHjCj0kc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سموتریچ، وزیر مالی اسرائیل، درباره طرح ترامپ برای غزه: ما هرگز این توافق 20 ماده‌ای را در یک تصمیم دولتی تصویب نکردیم.
🔴
در این طرح، اشاره‌ای به مسیری برای ایجاد یک کشور فلسطینی شده است، که به نظر من فاجعه‌بار خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/142579" target="_blank">📅 11:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142578">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۶ امروز وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/142578" target="_blank">📅 11:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142577">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏
👈
تحلیل الجزیره: این ترامپ نیست که مانع عبور کشتی‌ها از تنگه هرمز می‌شود، بلکه شرکت‌های بیمه این کار را خواهند کرد
‏
🔴
تا زمانی که تهدید فیزیکی علیه تردد دریایی وجود داشته باشد، این شرکت‌ها از قدرت مالی خود برای جلوگیری از عبور کشتی‌ها استفاده خواهند کرد
‏
🔴
بدون تضمین‌های قاطع مبنی بر اینکه کشتی‌ها از حملات ایران در امان خواهند بود، مالکان حاضر نمی‌شوند که در تنگه تردد کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142577" target="_blank">📅 11:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142576">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وزیر خارجه کره جنوبی: پیام ترامپ که در آن دستور کاهش رزمایش‌های نظامی مشترک داده شده بود، حاوی فشار بر ما جهت مشارکت در جنگ علیه ایران است
🔴
چو هیون، وزیر خارجه کره جنوبی، گفت پیام دونالد ترامپ، رئیس‌جمهور آمریکا، که در آن دستور کاهش رزمایش‌های نظامی مشترک داده شده بود، به نظر می‌رسید حاوی فشاری بر سئول برای مشارکت در جنگ علیه ایران باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/142576" target="_blank">📅 11:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142575">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سی‌ان‌ان: ایران بخش قابل توجهی از کنترل بر تنگه هرمز را از دست داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/142575" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142574">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏
👈
انتصابات جدید در قوه قضاییه
‏
🔴
ناصر عتباتی رئیس کل دادگستری استان آذربایجان غربی به عنوان رئیس کل دادگستری استان تهران
‏
🔴
ذبیح الله خداییان رئیس سازمان بازرسی کل کشور به عنوان رئیس حوزه ریاست قوه قضاییه
‏
🔴
سیدعلی کاظمی رئیس پژوهشگاه قوه قضاییه با حفظ سمت به عنوان سخنگوی قوه قضاییه
‏
🔴
اصغر جهانگیر معاون اجتماعی و پیشگیری از وقوع جرم قوه قضاییه به عنوان رئیس سازمان بازرسی کل کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/142574" target="_blank">📅 11:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142573">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
گزارش ها از هدف قرار گرفتن یک فروند کشتی در تنگه باب‌المندب
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/142573" target="_blank">📅 10:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142572">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
الجزیره به نقل از منبع دیپلماتیک سوری:
رد وجود هر گونه توافق امنیتی میان سوریه و اسرائیل؛ ادعا‌های تل‌آویو در این زمینه نادرست است
🔴
دمشق نمی‌تواند وارد توافقی شود که مانع ساخت نهاد‌های غیر نظامی و نظامی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142572" target="_blank">📅 10:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142571">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
آکسیوس گزارش داده حمله اسرائیل به پایگاه هوایی «ابوالظهور» در سوریه، نارضایتی مقام‌های ارشد آمریکایی را به‌دنبال داشته و شکاف میان دولت ترامپ و نتانیاهو را آشکارتر کرده است.
🔴
برخی مقام‌های آمریکایی معتقدند این حمله ممکن است تا حدی تحت تأثیر انتخابات پیش‌روی تل‌آویو در ماه اکتبر بوده باشد؛ آن هم در شرایطی که دمشق در تلاش برای ایجاد سازوکار هماهنگی مورد حمایت آمریکا با اسرائیل بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142571" target="_blank">📅 10:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142570">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
کانال ۱۲ (عبری): پروازها بین تل‌آویو و مراکش، پس از سه سال وقفه، امروز از سر گرفته می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/142570" target="_blank">📅 10:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142569">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سرلشکر عبداللّهی رئیس ستاد کل نیروهای مسلح : کشور های عربی حاشیه خلیج فارس مراقب رفتارشان و استقرار نیروهای آمریکایی در خاک کشورشان باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142569" target="_blank">📅 10:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142568">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
فاکس نیوز به نقل از مقام وزارت جنگ آمریکا: ترامپ بودجه‌ای بیش از یک تریلیون دلار پیشنهاد کرده، زیرا بازسازی ارتش هزینه‌های زیادی دارد
🔴
مدت قرارداد‌های خرید تسلیحات را از ۵ به ۷ سال افزایش داده‌ایم تا امکان بالا رفتن تولید کارخانه‌ها فراهم شود
🔴
طی این ۷ سال، ۱۴ هزار سامانه پاتریوت تولید خواهد شد
🔴
در حال مذاکره با شرکت‌های جدید برای انعقاد قرارداد‌های تولید موشک‌های کروز کم هزینه هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142568" target="_blank">📅 10:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142567">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وال‌استریت ژورنال: ترامپ در دیدار احتمالی با کیم جونگ اون در ماه نوامبر، می‌خواهد اون را برای دست کشیدن از برنامه هسته‌ای کشورش متقاعد کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/142567" target="_blank">📅 10:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142566">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfe76fe9dc.mp4?token=CJL7E5HETmXaFCilNA6DA8WS33xYdFSCk4LZUm0bYnhhmgAN-En3lwYvKyRFI21fvO_INovuuTUQXnq9-49sSs5NNiXjSR6hNX3rgWgm2giZatqNGaTEk66zaenSQ3-MvwXZoEXhqBy7fRiWI0cnZ0cR-qlot1zlAMpcagn6a4yfKu5ODdwwtMeiOFYKkweJpD34fOPJw_bWgSNrJu5XAgAvY4Uz09rGgflTWWjZQPZ94VmcZCaLxzb-1MuGadZ_OjqFWYbPNqdoM0qvheANuFBMjws__MkCPTt-ccIxH9URFKDowR8_4KIxkIeskzdzuJ6BWwbBUJ3xdUqQL8Gf-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfe76fe9dc.mp4?token=CJL7E5HETmXaFCilNA6DA8WS33xYdFSCk4LZUm0bYnhhmgAN-En3lwYvKyRFI21fvO_INovuuTUQXnq9-49sSs5NNiXjSR6hNX3rgWgm2giZatqNGaTEk66zaenSQ3-MvwXZoEXhqBy7fRiWI0cnZ0cR-qlot1zlAMpcagn6a4yfKu5ODdwwtMeiOFYKkweJpD34fOPJw_bWgSNrJu5XAgAvY4Uz09rGgflTWWjZQPZ94VmcZCaLxzb-1MuGadZ_OjqFWYbPNqdoM0qvheANuFBMjws__MkCPTt-ccIxH9URFKDowR8_4KIxkIeskzdzuJ6BWwbBUJ3xdUqQL8Gf-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
یوسفی نماینده مجلس: دلیل مصرف 130 میلیون لیتر بنزین در روز، کیفیت پایین خودروی داخلی حتی مدل صفر آن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/142566" target="_blank">📅 10:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142565">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
شاخص کل بورس تهران در دقایق ابتدایی معاملات امروز با افت ۸۰ هزار واحدی به رقم ۵ میلیون و ۸۶۶ هزار واحد کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142565" target="_blank">📅 10:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142564">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d1f7c464.mp4?token=HwBZB0mlGd00pvacVBkjGozoLhs1tEKxvuEWMKqNoealUY9ei6ciQILDzD7ErzcmBOvPsjWKR-ngybkDDaztWCR1AvJuvo4AKAaZQfPRDFiSkUedhJ9QBbOny7ojgR4W0YQKCFX66kFJ4D_4YQyQqbe6sS85Lwqa9U_eKGGgDgNRjtBlD60TNlPW5XboBAH6wT5fiXu2GAHVaVJE9JCoGj9v-xUKcjXEbdgp0vV-remRT69xHUPN3JN9xyc-4VYQoTrHvq6HQkf_eHkGnDIXQeKy68VZYcJZUTgTdXdlIfUh16U2kYBCvIENfDHLuX1QPVisRygUUQCSqppOBBFTJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d1f7c464.mp4?token=HwBZB0mlGd00pvacVBkjGozoLhs1tEKxvuEWMKqNoealUY9ei6ciQILDzD7ErzcmBOvPsjWKR-ngybkDDaztWCR1AvJuvo4AKAaZQfPRDFiSkUedhJ9QBbOny7ojgR4W0YQKCFX66kFJ4D_4YQyQqbe6sS85Lwqa9U_eKGGgDgNRjtBlD60TNlPW5XboBAH6wT5fiXu2GAHVaVJE9JCoGj9v-xUKcjXEbdgp0vV-remRT69xHUPN3JN9xyc-4VYQoTrHvq6HQkf_eHkGnDIXQeKy68VZYcJZUTgTdXdlIfUh16U2kYBCvIENfDHLuX1QPVisRygUUQCSqppOBBFTJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخورد موشک اسپیس‌ایکس با ماه گودال ۱۸ متری ایجاد کرد
🔴
تصاویر ناسا وجود گودالی به قطر حدود ۱۸ متر روی سطح ماه را نشان می‌دهد که گفته می‌شود در پی برخورد بخشی از موشک فالکون ۹ متعلق به شرکت اسپیس‌ایکس با سطح ماه ایجاد شده است.
🔴
این موشک در ژانویه ۲۰۲۵ با هدف انتقال کاوشگر «بلو گوست» و ایستگاه «ریزیلیِنس» به فضا پرتاب شد، اما مرحله دوم آن به دلیل کمبود سوخت نتوانست به زمین بازگردد.
🔴
مرحله دوم موشک در نهایت با سرعتی حدود 9 هزار کیلومتر بر ساعت با سطح ماه برخورد کرد و گودالی به قطر حدود ۱۸ متر بر جای گذاشت. تصاویر ناسا این عارضه را پس از برخورد ثبت کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142564" target="_blank">📅 10:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142563">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4t1OYzSmbH-aIPDSs3bQOEKgn-xw6eF8Om0v5uh3c6z43Vm0idV6feIr0wZWce3uzLNf4BlSYaiI5Oqj-3-JaLrGNPpiGZSLncCjMxQCsU-Rh6u4unRb7Z-4qK2fu18ep7G74j2SnfntYoeWAY7ugXkFfpdnj-usrSDrkgCOf81UH_kHrfCqWzR3FLlMUa7Ico5PSCfyLfFivPHStiAcyvEjyc4OMedDqh69NwVsyLKe24iNZK4nXypMLW9v_SU7jNjOfD23E-FwK1jHLTsMS8BI_fYlD5fsO0cTjrDBIKX0OBNNpfYvCbcZU781RFOA_vF_A3wDEoY8HDoFnpuHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس رنگی شده، از شیراز؛ سال ۱۹۱۱ میلادی، هم‌زمان با پادشاهی احمدشاه قاجار
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/142563" target="_blank">📅 10:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142562">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d4b1d33fe.mp4?token=eUe9s-x0AavWmnotdRYXh8YK2lAojtTQxjzBZUmlTP9M3MKKjrHFlDh-BHm5h7o26yUEk59FjT3kkOaY1zIh_7edbUCIB7egs0mhAzyL3tUBzTXEdauxUdvu4mvAxHuwVUp_gRl4DvtUBaG37CJSdY541Tp1rcwbT4e0NXZhD4JcN_jl3Sx_sFznmrDstGCLfN3AlITeAcX5lkVoH6IlA8sW4gI9kVrS-AM1xxTiT1qSyn2OMksf4NZ9vqMk9yHJ9MLeI-wN0zL9PbVlAlDZyUIivZwxzU0gwmqfU7-cxZivcjZX8MgbFgBpKkTr8sSucp7ZbmX2UTykbMMNQZpaLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d4b1d33fe.mp4?token=eUe9s-x0AavWmnotdRYXh8YK2lAojtTQxjzBZUmlTP9M3MKKjrHFlDh-BHm5h7o26yUEk59FjT3kkOaY1zIh_7edbUCIB7egs0mhAzyL3tUBzTXEdauxUdvu4mvAxHuwVUp_gRl4DvtUBaG37CJSdY541Tp1rcwbT4e0NXZhD4JcN_jl3Sx_sFznmrDstGCLfN3AlITeAcX5lkVoH6IlA8sW4gI9kVrS-AM1xxTiT1qSyn2OMksf4NZ9vqMk9yHJ9MLeI-wN0zL9PbVlAlDZyUIivZwxzU0gwmqfU7-cxZivcjZX8MgbFgBpKkTr8sSucp7ZbmX2UTykbMMNQZpaLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک شرکت چینی از ربات انسان‌نمای پرسرعت «سوپرمن» رونمایی کرده که می‌تواند ۲ متر به‌صورت ایستاده بپرد و به سرعت ۱۲.۶۶ متر بر ثانیه، معادل حدود ۴۵ کیلومتر بر ساعت، برسد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/142562" target="_blank">📅 09:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142561">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b5a92c64.mp4?token=bT02B86t_om2bxT9VcT-R3D3zAMXgwnNmLNT3NG53wseRNOhsZM-HUcJQDG60MtYurxsVzaKySiVV29BuGMJK4Fo1Pp-9lVkqN1n5-7oRgZebVfUpTYuuhoJM3gajAmG4mJhND75Q8V9AVGaHELSnyyR7_0A9yRVtP4jTRqoOTalHO0o0HhRysq2UtXnNbf63diLvBGt6nT4_hFU6_otKnsiKmZ4isWrJZanCC1bros35SJx7aUQQyzz710uTsp1gwAcQYBfJ49PHescQLr8_facHtE86fbyTSSssiv5mrIaR8jrMXyfGv09QhmmuKkH3XhiG8__wV2sutKOqIn4Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b5a92c64.mp4?token=bT02B86t_om2bxT9VcT-R3D3zAMXgwnNmLNT3NG53wseRNOhsZM-HUcJQDG60MtYurxsVzaKySiVV29BuGMJK4Fo1Pp-9lVkqN1n5-7oRgZebVfUpTYuuhoJM3gajAmG4mJhND75Q8V9AVGaHELSnyyR7_0A9yRVtP4jTRqoOTalHO0o0HhRysq2UtXnNbf63diLvBGt6nT4_hFU6_otKnsiKmZ4isWrJZanCC1bros35SJx7aUQQyzz710uTsp1gwAcQYBfJ49PHescQLr8_facHtE86fbyTSSssiv5mrIaR8jrMXyfGv09QhmmuKkH3XhiG8__wV2sutKOqIn4Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای، آلودگی آب را در نزدیکی سواحل عمان نشان می‌دهند. این آلودگی ناشی از نشت نفت از یک نفتکش حامل حدود یک میلیون بشکه نفت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142561" target="_blank">📅 09:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142560">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
فایننشال تایمز: ایران در حال بررسی این گزینه است که در صورت تشدید جنگ توسط ترامپ، به اهداف نظامی آمریکا در اروپا حمله کند.
🔴
منابعی که به حکومت نزدیک هستند، مدعی‌اند که نیروهای ایرانی در حال ارزیابی امکان حمله به تاسیسات در کشورهای جنوب شرقی مانند بلغارستان هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142560" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142559">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0wlpcZoeBmeUG5RfzYHL0RJRMDfKCeDqaskdjelPr0L-iSzWY38BZ2Ss3ORw-Cz29vXq6nAjATT-oiSXKWwbfFYy-H3ZrXZ3ESOmMkISfNDJq8_UC0ddBvMHOxfR5IyQvUuiPpAAnHew_2UltxOb9yxsUEW1nvHIckrsEPMOPVy6cIpkkeaNRYLijszPIPGadP3xgE9ZZnm9eAaO9ViqXUw6Od2-LtVn2LaOK4qpTOjiomODv_4lJ16Epdwa-t-68KUoro-mQRWB2c8_zSFv5Qj1BMCcs-UkmNwxSTyB3atI8XDKelNE1IzLlgjGajgM7bmBsoYzMDi2HacZsSjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: تعرفه‌های ۵۰ درصدی علیه کانادا را که قرار بود فردا صبح اجرا شود، برای سه روز به حالت تعلیق درآوردم، چون کانادا و آمریکا با نهایی شدن اسناد، به توافق رسیده‌اند!
🔴
خط لوله بزرگ کی‌استون ایکس‌ال که سال‌ها پیش توسط جو بایدن خواب‌آلود کشته شد، شاید دوباره از قبر زنده شود! از توجه شما به این موضوع متشکرم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/142559" target="_blank">📅 09:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142558">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Th7iyfQbTALKYxuD1lBRYGNkVVxEtT5tmzYdcbErGomrogtdmfLP8pGvnvBLEp9KiqLI09rPYfdrX4jAsoqJhpqPyd4FukNT3INuQAq_WnlaWaZUe6mhe-3ZGYQUBED4C3kGYHsxlLk0bPczbANLd5av1AaVK7RL3OOscTbxfvIyL8sL47XYZXegfg6cgcR28n5IGRBRaV-CvHUOV3I7yJxfTIFiTEbr8LLGOjRObAn4SDYV4Nsut7qOsUq7dL4tuYbhFFEvbJ9KXtxpXn7icf966TYl6oEaMAa308529dQuBoclq8xxp4hPDmQPKdFcEQzKdsacWrtvrkmBizAPYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف وارد بغداد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142558" target="_blank">📅 09:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142557">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec90dc737.mp4?token=ZUff5dRQdBAsqMSRm0cuHDWH2QQeuho34x7458dZkuVHgUi9Mc39i8Bg67yy-dS1IHWZH42ZcoD0avQjv2JTwG0amGHEfBNl51Csa2wOca5zCe1fcs_0oPN4garUW2dG0wKnzIu0UH8vXjhvLZ-cl6wDcMbk5NvIVRp6vIv9IS0WejdoebaKnFXzV-eGzbF8l_P4ydAkcyYpap7vbP4P5Dkl4bfs7LMSedkt-APbyg8Eu8QHVPUklFBsUMFnPwYwlq-gcQRbwxPwwo_mcmwlv4ni1QJ4A5owPWJSAg3xohe4zTRCvht_hhwVJv3vNScEsfpjH_rLF30gTlRRifD7sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec90dc737.mp4?token=ZUff5dRQdBAsqMSRm0cuHDWH2QQeuho34x7458dZkuVHgUi9Mc39i8Bg67yy-dS1IHWZH42ZcoD0avQjv2JTwG0amGHEfBNl51Csa2wOca5zCe1fcs_0oPN4garUW2dG0wKnzIu0UH8vXjhvLZ-cl6wDcMbk5NvIVRp6vIv9IS0WejdoebaKnFXzV-eGzbF8l_P4ydAkcyYpap7vbP4P5Dkl4bfs7LMSedkt-APbyg8Eu8QHVPUklFBsUMFnPwYwlq-gcQRbwxPwwo_mcmwlv4ni1QJ4A5owPWJSAg3xohe4zTRCvht_hhwVJv3vNScEsfpjH_rLF30gTlRRifD7sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی: به نظر می‌رسد از جمعه به‌بعد تهران دمای ۳۸ درجه به خود نبیند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142557" target="_blank">📅 09:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142556">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
قالیباف پیش از سفر به عراق: روابط دوجانبه بغداد و تهران در تحولات منطقه، بسیار مهم و اساسی است
🔴
سفر مذکور با توجه به اینکه بعد از پیروزی ایران در جنگ ۴۰ روزه انجام می‌شود، خیلی اهمیت دارد
🔴
بدون شک ما در آینده منطقه شاهد نظم جدیدی خواهیم بود
🔴
این سفر می‌تواند زمینه‌ساز نگاه و فرصتی که پیش روی ماست، باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142556" target="_blank">📅 09:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142555">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
یک مقام آمریکایی به "اکسیوس" گفت:
دولت ترامپ از سوریه خواسته است که پس از حملات هوایی اسرائیل، خویشتن‌داری نشان دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142555" target="_blank">📅 09:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142554">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سفیر ایران در روسیه: اوکراین هنوز بابت حمله به کشتی ایرانی در دریای خزر، غرامت پرداخت نکرده
🔴
تهران و کی‌یف در حال حاضر درباره پرداخت غرامت مذاکره می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/alonews/142554" target="_blank">📅 09:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142553">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
داده‌های اولیه نشان می‌دهد تردد دریایی از تنگه هرمز روز سه‌شنبه کاهش یافته است، زیرا بیشتر مالکان کشتی‌ها به دلیل نبود نشانه‌های روشن درباره بازگشایی این گذرگاه حیاتی، از عبور از آن خودداری کردند.
‏
🔴
بر اساس داده‌های شرکت کپلر، از روز سه‌شنبه تا صبح چهارشنبه تنها ۶ کشتی حامل کالاهای اساسی از تنگه عبور کردند؛ این رقم در روز پیش از آن ۹ کشتی بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/142553" target="_blank">📅 08:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142552">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/728a43b1b4.mp4?token=Vb8KaaVEceHKx9u0fbrMuSLUOV0Sa1XdvnOGX9t2KW6Z9DYw0JbHZEhmiemiqFCfBbHKBawX47lzlRcYsdbsKL9hDRuqY9Iz4Aa5Qd17rsDEy47GCatlU6B5Aedl8fKwQzzpqBZIG3bczpo7Y3w_EmuYZsWSsF7vxX0QmOF2URCZmGK6FKK25gmlySVypNYX0uHVZTB-4K_UmKiRlaXbbtEsVUoD6sRv40xJOoFAFE0_U27RmYT154IJdbEgcS8HsKICd94e_3ArSiKdpEZdgsG5qPLKSIJuI15YB_l9_2Xe6eLjeI6pWXiWyIeAo0RxZCEfKgbIxyW4Ii5qLTed9p2k8Js22dX7E_wBdBYNW-34VCC_DlhY5AwMGl6BmpYmBmZR3N7wbqocrSk3jGtpskU-mjnC3AcGHVJTSPEty7Th_sjgN9BxEDx0rtFaqilGGbn0ieBf_b9RGQ1ivQxgENYobw6yvbz18o-rsks-fU8df3xp4XPqvoj3CCerEP1U1ZRr2NNs6Dg-1cMpuhTrv_a_VzyLrg9gWYvAwzoQGio-6YDL1hyXYf0qY0JoLNPRacFKobqoCbsuPWGbDz1wW1cC5jwold8JSN7tYQgAawpOe1WaIy3-9lIde4YovyS6U4zThcycCAs8GoO4MViP1anSI9mQ8dSwiwFC_iqhB0s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/728a43b1b4.mp4?token=Vb8KaaVEceHKx9u0fbrMuSLUOV0Sa1XdvnOGX9t2KW6Z9DYw0JbHZEhmiemiqFCfBbHKBawX47lzlRcYsdbsKL9hDRuqY9Iz4Aa5Qd17rsDEy47GCatlU6B5Aedl8fKwQzzpqBZIG3bczpo7Y3w_EmuYZsWSsF7vxX0QmOF2URCZmGK6FKK25gmlySVypNYX0uHVZTB-4K_UmKiRlaXbbtEsVUoD6sRv40xJOoFAFE0_U27RmYT154IJdbEgcS8HsKICd94e_3ArSiKdpEZdgsG5qPLKSIJuI15YB_l9_2Xe6eLjeI6pWXiWyIeAo0RxZCEfKgbIxyW4Ii5qLTed9p2k8Js22dX7E_wBdBYNW-34VCC_DlhY5AwMGl6BmpYmBmZR3N7wbqocrSk3jGtpskU-mjnC3AcGHVJTSPEty7Th_sjgN9BxEDx0rtFaqilGGbn0ieBf_b9RGQ1ivQxgENYobw6yvbz18o-rsks-fU8df3xp4XPqvoj3CCerEP1U1ZRr2NNs6Dg-1cMpuhTrv_a_VzyLrg9gWYvAwzoQGio-6YDL1hyXYf0qY0JoLNPRacFKobqoCbsuPWGbDz1wW1cC5jwold8JSN7tYQgAawpOe1WaIy3-9lIde4YovyS6U4zThcycCAs8GoO4MViP1anSI9mQ8dSwiwFC_iqhB0s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مشاور قالیباف: نبویان به کسی که پیش‌تر از او اسناد محرمانه دریافت می‌کرد، مراجعه کند؛ شاید سند جدیدی وجود داشته باشد که نظر او درباره تفاهم را تغییر دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/alonews/142552" target="_blank">📅 08:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142551">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا، با شیخ طحنون بن زاید، مشاور امنیت ملی امارات، درباره مسائل امنیتی منطقه از جمله لبنان گفتگو کرد.
🔴
دو طرف درباره ادامه هماهنگی آمریکا و امارات برای «پاسخگو کردن ایران و نیروهای نیابتی‌اش در قبال حملات مداوم» رایزنی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/142551" target="_blank">📅 08:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142550">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
یک مقام کاخ سفید: ایالات متحده ابزارهای فشاری در اختیار دارد که رئیس‌جمهور می‌تواند در هفته‌ها و ماه‌های پیش رو آن‌ها را علیه ایران تشدید کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/alonews/142550" target="_blank">📅 08:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142549">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faded5dcce.mp4?token=Lsmf7d7SaCtOZcXqbthRnsgFVwCXiCXvyFEE8g9hfzYUq3zsMkcaDpyP49fQevrvx8s56_cNVftnvE6J9sXP7q2V4yWApNOCnG_XZiWJpVl6v_PlhpSgupG26sN3DmxJeCTG14jNmZd_oMQymmtiCRDtqCzLMh7lJYQPukaO2WBC5f3aO827w0xUXmTzkG-pTgv55IgkJf9nrKp4_RnMUThLFaOHpd34uQ1o_r2oon2k1ZEOHxyiDsaetZPMFZ1yGYhFAg7_O13xj125Dc4IFVoggWmYqf5AjlHc3QCt2EYXxZ5HB7PbyePGdNRT_n8rUtTOl6GidlXN8v1wOwJY_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faded5dcce.mp4?token=Lsmf7d7SaCtOZcXqbthRnsgFVwCXiCXvyFEE8g9hfzYUq3zsMkcaDpyP49fQevrvx8s56_cNVftnvE6J9sXP7q2V4yWApNOCnG_XZiWJpVl6v_PlhpSgupG26sN3DmxJeCTG14jNmZd_oMQymmtiCRDtqCzLMh7lJYQPukaO2WBC5f3aO827w0xUXmTzkG-pTgv55IgkJf9nrKp4_RnMUThLFaOHpd34uQ1o_r2oon2k1ZEOHxyiDsaetZPMFZ1yGYhFAg7_O13xj125Dc4IFVoggWmYqf5AjlHc3QCt2EYXxZ5HB7PbyePGdNRT_n8rUtTOl6GidlXN8v1wOwJY_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف تهران را به مقصد بغداد ترک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142549" target="_blank">📅 08:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142548">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiMPXt_hLpJzw3evb3-qpF3cvSq0e3Q1OZA0eZOkyQF2nqPmq8q5u8C-cnUGA2AwjxiDx-0gnx3-XFFwKk5qMa10fXBQO64fvzbJcZxXGAzRg-b5gv5KeDJrq8vt2wy1qBjmRGG0M7KWDY8GEjvksnU41vA7HXL7dHH-LZey_jXKcmr7BxpZLFQedFJlxKLM8DDCTBOXvIgpm9z47bwabPcYqQ41tOzne937af0M1Re_L5RuC50k7UifUMG3MJCua1rY1ZYUHsYkX87kUOBss5uXN6gvHVW_82OWAAf63BCjJmPCIlw13CM2Xm2Fh3gkmkhGj0KdLx6JrBgEgxRndw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفتکش توقیف شدۀ اماراتی که در کریدور شمالی تنگۀ هرمز توقیف شده بود، به سمت بندرعباس تغییر مسیر داد.
‏
🔴
مقصد این نفتکش ابتدا بندرجبل‌علی تعیین شد اما حالا به سمت بندرعباس می‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/142548" target="_blank">📅 08:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142547">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
رویترز:
ترامپ از مقامات ارشد دولت خود خواسته است تا تمام مذاکرات با ایران را متوقف کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/142547" target="_blank">📅 02:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142546">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYgy2boTY4idWc5Ey5YFg-nEKpaqzq2hXbZStv-Lo9TKWnuZNiFNPlDopDomEJjarteQktWS-sD3kTxc_vBlpB6YHYDt57Kxm6V4cVYdNSuafMRzt-mzsQmFw9U8uCm2BEMidE8bZq9_1KxM0pockA8rG_lmC6pykYtNlM20jkD5s7TliQPGZBt0luFfc3jSQTol06zzw0PP4iFQju4KjuEbYVLSHboNfc3dMNtQuDGKllni6_Kn9yhWvIkMxHTRN0l7-4Xdgh2ZPNVmVs-_H93NJ7jD2ZdDKc2MuK62CdSoc2S7u43HY7PDhgL3V1msUtjhJ8fFfRsNUjVenH-Jqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی جنگنده‌های اسرائیلی به شهرک کفررمان در جنوب لبنان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/142546" target="_blank">📅 01:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142544">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lu3axBz-pZ9XYRErpF4y6bTA3Bs3DbyAOBK8AWnZmkbgpU-SrNbm8PUqZXrt4WTScAfVFXs7lah4HABn3vR8FM2_x2JX-qLYxeg7bxjkL-rhpVwH0Q7-YNrSCGg5bQailfry4Z1JrgHffyR0qLqQNs2ZHhfwpN9EcREzLXZQJyflrDbLA1JJ2MfB5Qu3wna-X3Rx94HTR_yCcMfhU4vyzTucuz0k_VtbiOPlCzNa1ShjOCt8R_LC3tpRPQiI0eeKyjAqQ1syHX_JnmdwLtrk4auv_FXMv0NHxj-x2DEQvqJlO0Id9n4kcrejiVcnFWAsozAl59O9i9w27J1lj0UfHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2a74dcb034.mp4?token=ntVHsUNZYxkDO08-Ec8_HOBVXDh3Ny_Trsfj1NyzS0Z1lACwn55Ov0adbqBKsX85P8H3p9VTzuL7H-ACFYYWyWKRUWHajozmjJnIqfGZx3n4fKXmo6Fg1luzDmd-pZ9k4S7OoNYw24LXD0dnzw_FnTBVxpJlwmXtKog9VUFZVo9ZPJNixTkYsNmJEXxAOjK1JIxJf2-juB4JrD9gtdW0SA1K1Rszw8l4o1R-fEVg_B9GlQvPcdLnaLv-DQHhRrTmf_f-UNd-bqHmAg__DgnoSZtU6rK4wqekjb87Y7dFAzb3r8VPWj-uwLZyIkTs4zfWbcMTTYxaMV6kR2hdLpqojw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2a74dcb034.mp4?token=ntVHsUNZYxkDO08-Ec8_HOBVXDh3Ny_Trsfj1NyzS0Z1lACwn55Ov0adbqBKsX85P8H3p9VTzuL7H-ACFYYWyWKRUWHajozmjJnIqfGZx3n4fKXmo6Fg1luzDmd-pZ9k4S7OoNYw24LXD0dnzw_FnTBVxpJlwmXtKog9VUFZVo9ZPJNixTkYsNmJEXxAOjK1JIxJf2-juB4JrD9gtdW0SA1K1Rszw8l4o1R-fEVg_B9GlQvPcdLnaLv-DQHhRrTmf_f-UNd-bqHmAg__DgnoSZtU6rK4wqekjb87Y7dFAzb3r8VPWj-uwLZyIkTs4zfWbcMTTYxaMV6kR2hdLpqojw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز ۲۸ مرداد، تولد جاویدنام مهرداد مشتاقی هست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/142544" target="_blank">📅 01:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142543">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6mpPiwjudQmckw89liddaO-yL5Wllp7aM0WgDSvnibFCCy9lV-lc-k6j83oZld7v1LOR8egu2vWcaJOMqU6UCcIvjASSBylCYZzAuYHnF6B7LUGuPrpgAGBp3RRD8NKa_cV945YmUztzp6lfPEpjByj1oAx3QDTNz4fTv8_jIwLbSGAKnZx6NokBu-Qe2h-H3Riqw3z1eepN5-24ra_cfPkQzJhH73Po0w-vjms7OS3tMCk81m9pPeBeiUECNQJjLD8Cuj3s8gtTkkDB1CqkUWTjbHGtfMBVTY6VXk1GBVBeViO1J_hyEqmRNEV4V6ahPmpqq15OE9dZgi_ZU1yJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر اقتصاد: هدف اول ما اینه که تاب آوری مردم جلوی مشکلات اقتصادی زیاد بشه و مقاوم بشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/142543" target="_blank">📅 01:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142542">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np6jDtFn3hGoS-jSozuCWbONvLcJF6DU2k8WkNL4Yfoj42wQ64JMTO7KyhDlgYihXgA8ZFOtD9PxZbrBmaXh7PT43-cnYXYZOlEpQcVGkZ_FD60KGZpX88Nd0B0CwPzg0EUhmxy1mGGwH-xAQu2CYY39Em66XEBoTyTPUdQ0kUpMB3VbXMv23NIdtEMD5dW_pK1yFMI6PlztkEgukRhkV4gzIJwc-db6Bs_dunz4SLQdhp8YK55XkbHqXQehfrOyrb24e7dnJiSi5a7jNUmop9fOvLyK_6J4cdE_yY8PrByLPiMbhxGum0CUDklbMRZVw52GQPfrJnkUJWUTXxLHqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
«مردم ایران همیشه در حال آه و ناله و غر زدنن؛ حتی اگه وضع اقتصادی هم خوب باشه، باز فرقی نمی‌کنه. مردم جز غر زدن و ناله کردن چیز دیگه‌ای بلد نیستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/142542" target="_blank">📅 00:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142541">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سی ان ان: ترامپ استراتژی خود در قبال ایران را تغییر داده و به فشار بلندمدت متمایل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/142541" target="_blank">📅 00:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142540">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25be82ab31.mp4?token=kEVulpCEl6yeRhNSz4AbrXa5cRt-cP1dxpgDXVuAziXtLCYwJgdJy6--L_Y_8Ry-kp4UOVkBr3HXpz4DJQOhTgxuju9JaySc7mmfhHV1xEQEeaQ6ZhQzg3yVZsrtLLJZFzP58e03xq6FQdjI2svNm-0RG0qklvcfWLUmz8D562p8OLCpHVhPeUZT0s8EVcLMzIqHoPxiFS8YyZJLxRHBQ6zV0YVdYdeeB8wFBRAi9vqF8KUIvEIVrVaJhxQ2NQLhLwnv4pHXc3AZxlUmHEWk_kbs28NcIaq4MrEqegYMs32kbzyYpxHLEzoc225BIpO92vDisO9Kn0bHcpFoAqo80Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25be82ab31.mp4?token=kEVulpCEl6yeRhNSz4AbrXa5cRt-cP1dxpgDXVuAziXtLCYwJgdJy6--L_Y_8Ry-kp4UOVkBr3HXpz4DJQOhTgxuju9JaySc7mmfhHV1xEQEeaQ6ZhQzg3yVZsrtLLJZFzP58e03xq6FQdjI2svNm-0RG0qklvcfWLUmz8D562p8OLCpHVhPeUZT0s8EVcLMzIqHoPxiFS8YyZJLxRHBQ6zV0YVdYdeeB8wFBRAi9vqF8KUIvEIVrVaJhxQ2NQLhLwnv4pHXc3AZxlUmHEWk_kbs28NcIaq4MrEqegYMs32kbzyYpxHLEzoc225BIpO92vDisO9Kn0bHcpFoAqo80Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به یه دختر غواص تو جنوب گیر دادن که لباس غواصیت تحریک کنندس، اونم با چادر رفت غواصی
😂
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/142540" target="_blank">📅 00:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142538">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GLh50elCvwBLvz-Zh5a1hZWOKpfSoXEjJeZ8cn0Cq7tZ6XkoauSS6yzF9f2odMk-CN4ThCA2VJLcgV5_Ck2L59_VbCSVA5Ejg3Zt5KAf_yoGCKb81yYrorc_pmxlDiQhIBQR5ZggJfRyrq3ysUXA2AyuKi1AWjsXbYbUPy5KnQHDNQ2-kMhUdSKKVEXK2tj-EnigCrq9dgScBDP_NKFHPffd6n19Tb268MB1dBLxhEkv_evnsNOELihdG8L-81ekbll6SUuaNmrkxMLPg6bS_rE0FBAKAk3pivVH9ZhD7eY_TnXDFZg7GfnhiDwMhReVROHgWojGjz3rFmrldEl6CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صداوسیما یه گیمر فرستاده که بازی های مختلف رو بررسی کنه
بعد یکی از بازی‌ها کالاف دیوتی وارفر بوده که باید قاسم سلیمانی رو توش ترور کرد
گیمر صداوسیمام با خشونت شدید، قاسم سلیمانی رو هدشات کرد و نوشتن:
آقا ما بخدا نمی‌دونستیم این بازی همچین صحنه‌ای داره، ترو خدا بازی نکنین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/142538" target="_blank">📅 00:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142537">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏
👈
اسماعیل بقایی: شلیک موشک کار ما نبوده‌‌ و کشورهای منطقه باید از اتهام‌زنی بی‌اساس علیه ما دست بکشن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/142537" target="_blank">📅 00:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142535">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دنبال وامی
⁉️
بیا اینجا شرایط بخون
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/142535" target="_blank">📅 00:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142534">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e54Cg0tj0-4qvJYskDfSG9iuy5Jg2Dh6WpfZ32w5lyZO2ZvPbV3YPsAt-nKNss_mTQu2nBpHv6bsY5qEyReVFSabq5JwOm0SMZeFek2BtvyIIzNkr9W2u9TEy2gxxRCfrYxVLmdnyKTMEI1Or2mBcXpJUJC_BzgA1UJNnkATBgy2-UxCUYltrLC8Rj3JQzYN5B8NnOFrWjlbFX3UbG1mjg8QsBvOZAgdTdK1iR-tBSF70NeiY8MCS9WGrKnhXj6i7ouN1naNcLJVhINfssDXisFqGxs9bBP2z2Fr3zjbMmSX88EBULxQNmFM5mV5tn05vaE3jc7tI_YzUI1_3cDOEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: گرونی‌ها کار دشمنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/142534" target="_blank">📅 00:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142533">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
امارات متحده عربی اعلام کرده است که تمامی مبادلات تجاری، روابط اقتصادی و تراکنش‌های مالی با ایران را تا اطلاع ثانوی متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/142533" target="_blank">📅 00:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142532">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
آسوشیتدپرس: مقام‌های منطقه‌ای می‌گویند دلیل تهدید ترامپ برای حمله به عمان، نارضایتی او از توافق این کشور با ایران برای مدیریت تردد کشتی‌ها در تنگه هرمز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/142532" target="_blank">📅 23:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142531">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سی‌بی‌اس: دولت ترامپ به عمان اطلاع داده است که با بخش‌هایی از توافقی که هنوز اعلام نشده، مخالفت دارد. این توافق شامل مدیریت مشترک بین ایران و عمان برای مسیر عبور از تنگه هرمز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/142531" target="_blank">📅 23:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142530">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
کانال ۱۲ به نقل از یک مقام اسرائیلی:
ما به راحتی از آنچه به دست آورده‌ایم دست نخواهیم کشید؛ این یک برگ برنده استراتژیک در مذاکرات با سوریه است.
🔴
ما می‌توانیم در ازای خروج از سوریه به دستاوردهای سیاسی دست یابیم و این اتفاق در زمان مناسب رخ خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/142530" target="_blank">📅 23:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142529">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وزارت دفاع امارات: دو فروند موشک بالستیک ایرانی که امروز شناسایی شدند، ترافیک دریایی را هدف گرفته بودند و عمداً به سمت امارات شلیک نشده بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/142529" target="_blank">📅 23:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142528">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
حزب‌الله تصاویری از عملیات‌هایی را منتشر کرد که در آن، گروه‌هایی از سربازان و خودروهای ارتش اسرائیل در حومه جنوبی شهر زوتار الشرقیه هدف قرار گرفتند. این عملیات‌ها قبل از امضای توافق آتش‌بس در ماه ژوئن انجام شد و با استفاده از دسته‌ای از پهپادهای تهاجمی صورت گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/142528" target="_blank">📅 23:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142527">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsZ1KvTZeFA90hV_oydBQWMgr135ELvsWxLEk5IisDdPhdfbAeAmS_Ck4YSNg3EdsqVMDfTZ3g_siHT3190AEwtJJUdFk8e-AdEhluGlhsryXeQP6sIWoNyqjMBVEDdpeAyL5Byr0IkB93POVfIn5PbRrZFsj0TRp2hU9lcma0e5t68AvNUDeXZJZ1zQh_L28YRMjqigNLtNA-N6wdZz3Iz407GwMkiUK3dKlDCYdBCzU5TxyXAiKwM0muAAkMbs3Gdnl0tTXQy5chjgSctn1PaXXeOzte4i5o7_cGZegP95zyEQHpokB3u8HH7BYnuQVPR45uGw3vAkoa3fuutSkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حداد عادل: مجتبی خامنه‌ای بعضی اوقات فقط سه ساعت می خوابید و بقیه روز را به مطالعه و عبادت می پرداخت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/142527" target="_blank">📅 23:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142525">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
یک نفتکش غول‌پیکر چینی هم‌اکنون از طریق مسیر عمانی در حال عبور از تنگه هرمز است و سامانه شناسایی خودکار (AIS) آن فعال است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/142525" target="_blank">📅 23:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142524">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
عراقچی: وقتی ژاپن بودم یه بچه پوست شکلاتش از دستش افتاد تو رودخونه و چند دقیقه همونجا موند و از ماهی های رودخونه عذرخواهی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/142524" target="_blank">📅 23:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142523">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سفیر ایران در کویت با چهار تبعه ایرانی که از حدود سه ماه پیش در این کشور در بازداشت به سر می‌برند، دیدار کرده است.
🔴
هنوز جزئیات بیشتری درباره علت بازداشت یا روند پرونده این افراد منتشر نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/142523" target="_blank">📅 23:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142522">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سازمان تجارت دریایی انگلیس: کشتی باری حادثه دیده در نزدیکی بندر المخای یمن، مورد اصابت چندین موشک قرار گرفته و به‌طور کامل منهدم شده‌است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/142522" target="_blank">📅 23:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142521">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
مجله مدرن دیپلماسی، با ارزیابی داده‌های اطلاعاتی محرمانه مدعی شد:آمریکا و اسرائیل احتمالا دو هفته پیش از انتخابات سراسری اسرائیل در 5 آبان ماه، به ایران حمله می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/142521" target="_blank">📅 23:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142520">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
طبق گزارشات وضعیت اینترنت بسیار وخیم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/142520" target="_blank">📅 23:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142519">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc18d01f13.mp4?token=AyHZf2lJ8m7vTA-HjdHU_m3vmOOqJJMG4pP8eC9a96mcXXDRjtQMSbyYI3T5JdF8Xe1ByIA0_iqISNjrfAvuDhgAsJsCcYegvxwxOQrZVz3GlslDSOPfpkkII-6Y35M8eHWNuvNbQt6GmM709PQ1L4Ge-uX0n5tcEhvFVpIft6iGN1lRqKrNt2GGZW84gMIqtnZsUGtepa01Mr0EO1R0XhpJOfKPdLEvlzwxPY5ez0AAia-X001L6i8p3D9sZRGK_psepbC-3Qd7sHC2uRaN7TcNDSrSRM0DyblEV3kAxIEe0my0CDu5rneBrO7R6UddnWi4IUV1r20PvDsvQTLFiijNspqCtjWeO8So0tYcEVSoCCZwGGHjG7-MkKgaaNEC4Bms5y-diM8E2aglpWoDhhlA1DTftGZJ4OaYsDB13m7uINgs5CizrkK0j2pR380kYWggan9VAoztbOob7L59GMoDxLf7MAI8SaE11M3rEnDdvI3z8YHeWy2kfwqenNvu5dNoW9piaRQXQuzc2cVB_PB_tm01U9abgas5Ap2ZEEtbljLKbPPl5z5JYYcjGjXjvZZkYjzdeOog9g1vgrznIEOlMw6T4f2OmsFn3KS3Ez0WKbW0DMnqhwyBXBokVqzNfTag960zz4w3-86Pyh3yaUcW_RFsJ2d-x1O_rttmqsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc18d01f13.mp4?token=AyHZf2lJ8m7vTA-HjdHU_m3vmOOqJJMG4pP8eC9a96mcXXDRjtQMSbyYI3T5JdF8Xe1ByIA0_iqISNjrfAvuDhgAsJsCcYegvxwxOQrZVz3GlslDSOPfpkkII-6Y35M8eHWNuvNbQt6GmM709PQ1L4Ge-uX0n5tcEhvFVpIft6iGN1lRqKrNt2GGZW84gMIqtnZsUGtepa01Mr0EO1R0XhpJOfKPdLEvlzwxPY5ez0AAia-X001L6i8p3D9sZRGK_psepbC-3Qd7sHC2uRaN7TcNDSrSRM0DyblEV3kAxIEe0my0CDu5rneBrO7R6UddnWi4IUV1r20PvDsvQTLFiijNspqCtjWeO8So0tYcEVSoCCZwGGHjG7-MkKgaaNEC4Bms5y-diM8E2aglpWoDhhlA1DTftGZJ4OaYsDB13m7uINgs5CizrkK0j2pR380kYWggan9VAoztbOob7L59GMoDxLf7MAI8SaE11M3rEnDdvI3z8YHeWy2kfwqenNvu5dNoW9piaRQXQuzc2cVB_PB_tm01U9abgas5Ap2ZEEtbljLKbPPl5z5JYYcjGjXjvZZkYjzdeOog9g1vgrznIEOlMw6T4f2OmsFn3KS3Ez0WKbW0DMnqhwyBXBokVqzNfTag960zz4w3-86Pyh3yaUcW_RFsJ2d-x1O_rttmqsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سید محمد خاتمی درباره یادداشت تفاهم اسلام آباد: بعد از جنگ جهانی دوم هیچ سندی که به امضاء رئیس جمهوری آمریکا رسیده باشد، اینقدر امتیاز به طرف مقابل نداده/ در موضع عزت به این تفاهم نامه رسیدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/142519" target="_blank">📅 23:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142518">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نان بزودی گران خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/142518" target="_blank">📅 22:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142517">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
زلزله ۴.۷ ریشتری در نزدیکی کاریز خراسان رضوی
🔴
محل وقوع: افغانستان
🔴
نزدیک‌ترین شهرها:
🔴
۸۲ کیلومتری كاريز (خراسان رضوی)
🔴
۸۴ کیلومتری تايباد (خراسان رضوی)
🔴
۹۴ کیلومتری سميع آباد (خراسان رضوی)
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/142517" target="_blank">📅 22:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142516">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
بی‌اس: دولت ترامپ به عمان اطلاع داده است که با بخش‌هایی از توافقی که هنوز اعلام نشده، مخالفت دارد. این توافق شامل مدیریت مشترک بین ایران و عمان برای مسیر عبور از تنگه هرمز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/142516" target="_blank">📅 22:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142515">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVNQLogMcsDDnTGziQMJJh5S5IrCwNd1bsBNW4hRtmjxS2ISv3lCni35YV_WWSFkTFFG1l32lm60dOtX8sXc1dMFzg-xUwODvRCjX1Z3N6t3-KnDadT9bvngeVGvc-ye9mYInhPi_X87wPBKInp7MEwAXQ76-OpsI5VckXPf1LTXQMlvwz-aXBmAgNX7YK7JB7Wo1XsJDL9zsOlUJXziTk-iCDJv6Dff43Xv39YWpUnSAJ6HiQDrjmaSGalhirnrIsY3NRYpHt7B0i-2Yjfpaah0WKpdxOwXPBCkTfq1N8K51nRWDoMkiB2oAokK2UprsW3hWguyMTg8IU1xUSo3lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور نیروهای ارتش اسرائیل در کلمبیا برای امدادرسانی به زلزله زدگان
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/142515" target="_blank">📅 22:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142514">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
کاخ سفید: مذاکرات با ایران تا اطلاع ثانوی لغو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/142514" target="_blank">📅 22:28 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142513">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51557e821f.mp4?token=QdnpofIA1SSo0E8Y2-R-dALUTwJlkmm7w-ZILLndAGswifhnXaOwdhhqQmcF1xBnaWCQpXDCABQloZkgrNyV8ue54yM-3xk1iOuLEZEDSYBQzNZD53UGMqjdehh2YD-0kCevautCdl0y06LxCePHRTAoZ83jkJUsoKkSmvrH-rpgbECaWL2ry93uitQ-q4t2vFb0lUBaqJsr1menLGJfNjcnJigkcZ4Oyl8sw44KFX9zIAtDDCvavqF-HxVVt8uHO_HfvpIBE6XuB1VWimlOyfYliEEp0Y-ON3Qdwq2lski7BkFmrX3EUsXHPL_HuTyJkJEn-tFe1OX6s8IZNnyt6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51557e821f.mp4?token=QdnpofIA1SSo0E8Y2-R-dALUTwJlkmm7w-ZILLndAGswifhnXaOwdhhqQmcF1xBnaWCQpXDCABQloZkgrNyV8ue54yM-3xk1iOuLEZEDSYBQzNZD53UGMqjdehh2YD-0kCevautCdl0y06LxCePHRTAoZ83jkJUsoKkSmvrH-rpgbECaWL2ry93uitQ-q4t2vFb0lUBaqJsr1menLGJfNjcnJigkcZ4Oyl8sw44KFX9zIAtDDCvavqF-HxVVt8uHO_HfvpIBE6XuB1VWimlOyfYliEEp0Y-ON3Qdwq2lski7BkFmrX3EUsXHPL_HuTyJkJEn-tFe1OX6s8IZNnyt6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیدمحمد خاتمی: بعضی‌ها می‌گویند ما حیات‌مان در جنگ است
🔴
می‌گویند اول پدر آمریکا را در اینجا در‌می‌آوریم بعد می‌رویم در قلب آمریکا با او می‌جنگیم؛ آخر با کدام واقعیت‌ها
🔴
من هم احساساتم جریحه‌دار شد وقتی رهبرم را کشتند
🔴
از چشمان آدم خون می‌بارد؛ اما مسئله مدیریت جامعه نباید بر اساس احساسات باشد
🔴
ببینید مصلحت کشور، نظام و اسلام در چیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/142513" target="_blank">📅 22:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142512">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/febff14175.mp4?token=Vt4Jii7iPXXZ0h9jwLgaZzR5KEgLl2by0KNPOS3yjfVN791o5VsaDVU9yOYoKxzY6wArpz_YyTGav9o2UCO6wJYSTMHF6Wx3Skk_n5gsZGPd1ARstq64Oiid_uQDVMeIWBXPwz6nj43gc0IJU8fdFPnDb9w1Zv5MJ4YuJ3Mz50-WSxfHw5dpHMqbqDbh9clHP2TQJeArZUxnOUbYTGmFW6zVLOe7emDzOhnzA0DZcNgj5iv0ac7XAl_KWP2HFOFB0GeOh5xJWT1KyGwwqSFf5aGVjZKVc9c3YtwhbAdRskCxTY7hoZsgjInfTxuv6m0i0PVHiiZS5SYxsPQixASD7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/febff14175.mp4?token=Vt4Jii7iPXXZ0h9jwLgaZzR5KEgLl2by0KNPOS3yjfVN791o5VsaDVU9yOYoKxzY6wArpz_YyTGav9o2UCO6wJYSTMHF6Wx3Skk_n5gsZGPd1ARstq64Oiid_uQDVMeIWBXPwz6nj43gc0IJU8fdFPnDb9w1Zv5MJ4YuJ3Mz50-WSxfHw5dpHMqbqDbh9clHP2TQJeArZUxnOUbYTGmFW6zVLOe7emDzOhnzA0DZcNgj5iv0ac7XAl_KWP2HFOFB0GeOh5xJWT1KyGwwqSFf5aGVjZKVc9c3YtwhbAdRskCxTY7hoZsgjInfTxuv6m0i0PVHiiZS5SYxsPQixASD7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی عجیب از تجمعات شبانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/142512" target="_blank">📅 22:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142511">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/142511" target="_blank">📅 22:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142510">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وزارت دفاع روسیه: نیروهای روسیه و قرقیزستان رزمایش تاکتیکی مشترکی را با تمرکز بر مقابله با گروه‌های مسلح غیرقانونی ساختگی در یک منطقه مرزی تکمیل کردند.
🔴
این مانورها شامل عملیات هماهنگ با هدف شناسایی، مهار و خنثی سازی تهدیدات شبیه سازی شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/142510" target="_blank">📅 22:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142509">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
دولت ترامپ همچنین وکیل ارشد دادگاه، عبدولای سیه از سِنگال را به عنوان بخشی از کمپین گسترش‌یافته خود علیه دادگاه کیفری بین‌المللی (ICC) تحریم کرده است.
🔴
روبیو گفت که واشنگتن قصد تشدید کمپین خود علیه دادگاه کیفری بین‌المللی را دارد و از سایر کشورها خواسته است از تأمین مالی و مشارکت خودداری کنند و هشدار داد که اقدامات بیشتر از سوی ایالات متحده ممکن است دنبال شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/142509" target="_blank">📅 22:13 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142508">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
عراقچی: به میانجی‌ها گفتیم آتش‌بس را قبول نمی‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/142508" target="_blank">📅 22:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142507">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‼️
شرایط وام بدون ضامن تا سقف ۳۰۰میلیون
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/142507" target="_blank">📅 22:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142506">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزارت دادگستری آمریکا اعلام کرد ۱۷ شهروند ایرانی را به اجرای یک پویش گسترده برای سرقت اطلاعات از طریق حملات سایبری متهم کرده است.
🔴
طبق ادعای این وزارتخانه، متهمان ۱۴۴ دانشگاه آمریکایی، ۱۷۸ دانشگاه خارجی، ۴۲ شرکت و شماری از نهادهای دولتی را هدف حملات سایبری خود قرار داده‌اند.
🔴
متهمان بیش از 31 ترابایات اطلاعات را به سرقت برده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/142506" target="_blank">📅 21:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142505">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19b515710a.mp4?token=TJllpAlZZIosZSsLAvuI6wP3j_VGLSOcC35jdrncecdVLWQ0YQhIqVxLZtJHX0IXeyJ9UM74DFkv4sKVdJrFZBkilf9lIdfU_sPyPFmmJSATCNpO0L_PJuQCDfEp5Zbzxo4mhgooGPe7wG5mTKSOPBjentzrrckE5pMHoM3fo4eyE-2OaPWePrp4EutZ__D5kVRy612J8nmUNoYEsezOrZIQpgVbsxhEU72o3kPUEM3k8h-krK7zXgL9SWNGV5oX8abCn3dKrneZdkNKbcyqU5zI6KO4lKCMd9YoefMbgv22uKtYWwqBs-AFYuQRK3t3nGu0Ze2eVWRunNFJ1xcAkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19b515710a.mp4?token=TJllpAlZZIosZSsLAvuI6wP3j_VGLSOcC35jdrncecdVLWQ0YQhIqVxLZtJHX0IXeyJ9UM74DFkv4sKVdJrFZBkilf9lIdfU_sPyPFmmJSATCNpO0L_PJuQCDfEp5Zbzxo4mhgooGPe7wG5mTKSOPBjentzrrckE5pMHoM3fo4eyE-2OaPWePrp4EutZ__D5kVRy612J8nmUNoYEsezOrZIQpgVbsxhEU72o3kPUEM3k8h-krK7zXgL9SWNGV5oX8abCn3dKrneZdkNKbcyqU5zI6KO4lKCMd9YoefMbgv22uKtYWwqBs-AFYuQRK3t3nGu0Ze2eVWRunNFJ1xcAkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور خارجه روسیه، لاوروف:
روسیه حق دارد مداخله مستقیم بریتانیا در حملات علیه روسیه را مشارکت در جنگ با تمام پیامدهای ناشی از آن تلقی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/142505" target="_blank">📅 21:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142504">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزارت خارجه: ۲ دیپلمات فرانسوی به‌عنوان عناصر نامطلوب شناخته شدند
🔴
ورود آنها به ایران ممنوع خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/142504" target="_blank">📅 21:44 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142503">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
بر اساس یک سند دولتی اروپایی که شبکه ان بی سی؛ به آن دست یافته است، روسیه از طریق دریای خزر در حال ارسال مواد منفجره، قطعات پهپاد و مهمات به ایران است تا به تهران در بازسازی ذخایر تسلیحاتی آسیب‌دیده‌اش در حملات آمریکا و اسرائیل کمک کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/142503" target="_blank">📅 21:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142502">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا، توموکو آکانه، رئیس دیوان کیفری بین‌المللی را تحریم کرد.
🔴
این تحریم‌ها هرگونه دارایی او در ایالات متحده را مسدود کرده و تا حد زیادی او را از سیستم مالی ایالات متحده محروم می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/142502" target="_blank">📅 21:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142501">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b672ecc080.mp4?token=TTLorQsUUqlUJdLc9lRZWFXI5dbwqKapIcu24Kagbm1F3gZdJn7BJRu-Qm-U8jQNjsNfP4B6TZRWfFlSBoCt8r7io7Tp3DYOWEZPL2E78qS2oy_zC-9mTTGlhrtqSDkL8Q-tPNGbX76ADxMJJxsRttshgbdU10ACO3sYTUz9u4f8MWaLywTNpXMjGBpYbfXfAjgfCjej2hfSL45uKRf3xDgWFFB9V0_IQ5baFCNMmXiLDRqpluYnD32Dp-1fEQA4jayU4oge6sUazk-T68wjFQCHwe5IhmKcWG0SeuagcEzI5XbY8BFRjddACHutPUohj5F2JkkwAKboIgVscsrFwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b672ecc080.mp4?token=TTLorQsUUqlUJdLc9lRZWFXI5dbwqKapIcu24Kagbm1F3gZdJn7BJRu-Qm-U8jQNjsNfP4B6TZRWfFlSBoCt8r7io7Tp3DYOWEZPL2E78qS2oy_zC-9mTTGlhrtqSDkL8Q-tPNGbX76ADxMJJxsRttshgbdU10ACO3sYTUz9u4f8MWaLywTNpXMjGBpYbfXfAjgfCjej2hfSL45uKRf3xDgWFFB9V0_IQ5baFCNMmXiLDRqpluYnD32Dp-1fEQA4jayU4oge6sUazk-T68wjFQCHwe5IhmKcWG0SeuagcEzI5XbY8BFRjddACHutPUohj5F2JkkwAKboIgVscsrFwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عارف: جنگ‌طلب نیستیم، اما جنگجویان قدرتمندی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/142501" target="_blank">📅 21:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142500">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
هواشناسی : از روز شنبه دمای هوا میاد پایین و دیگه کم کم به سمت خنک شدن هوا میریم و از سه هفته دیگه بارش بی سابقه باران و برف تو ایران آغاز میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/142500" target="_blank">📅 21:33 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
