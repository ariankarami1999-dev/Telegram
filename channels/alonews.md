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
<img src="https://cdn4.telesco.pe/file/ETp76c6biJqfO4-WKWsg4UcrPlENKBpSujwTBGKHzVoQrvcAYFqozNcLeLmJbkKEnmR60IOEEASsiuCnAc8ZDjCUz8XBbNoY88rNAQi5IQ3HqW_s0sB7BGlMN30ibF5whCieic5sQ8aDmcVeZAi1tmxqb3Jee3199BPGVmFQqpq4YUq8oPU-g7M92ki-cONUWbnE1eZfqIbnXoioNeRH0bVbIlBxglp9RfYoEkx6zVuLD3hWkEIWRw2WLf9FNGhO0kWv0q0arbS6kPyQdOlyrv8RppdGLfCPQLUAvrU7FkHXWzddfodyZl0sR7vHVBHiDilCLabArTzdLU708NqU0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 943K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 12:08:39</div>
<hr>

<div class="tg-post" id="msg-134673">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
الحدث: حملات دیشب آمریکا به مکان هایی نزدیک پایتخت ایران نشون دهنده گسترش عملیات و تغییر عملیات به اهداف جدید در شمال ایرانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/134673" target="_blank">📅 11:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134672">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
خبرگزاری فرانسه: پاکستان از آمریکا و ایران خواسته است تا مذاکرات را از سر بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/134672" target="_blank">📅 11:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134671">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMozv39wZxVrDej9ztjL0zzEwLx5pZ-WnoT6SCnWZlZJsSBOCmd-IJZ6i6_jTZRvACferM9Z-OkB01_4M0Gy78IKEZhEh2oyJP0767LB3Q7xEU9zxjgCpyqjGknuOlTFknpi96S6FarCs7b7onGm2KRENgKTnMPuELz_9bx2Bv6pZ4qufkkZNbrGOph020sRYc3t3jVwKcgu5JjWkGMktLRNYjdHbnbx9grXK1Dr256WLHodyP__Y6E6faOZxgsC8GqaWd51WyuVpUGzd3ighYU8EKdIIHH0K4bKSAJdGI3L273bG_wyncigkFP91CQqfpzOU7lpkJ1hHczEF3ULNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد امضا کنندگان کارزار «درخواست حضور اعضای جبهه پایداری در مناطق جنگی در جنوب کشور» ۱۱۲ هزارتایی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/134671" target="_blank">📅 11:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134670">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de798daa31.mp4?token=LEUekTjGrGYwJILX1z6bX87yGwdJmSj0Jcf8z0mitM4CE5psCdzxm5j6OY2S27Cv9BJoN5iOKJtp6f3lK2gfpaCEA4ByekOjylAy3ALAndynhjk0ohi9zoQRd883p155NDdbrGIpOngZcebrRudSfSaqorOODacX9m3ddWha6qeqnNWpotfoe9G_16xMTLHBhkp8eIk6gYjO9e9ecHy8pDFDeMNqBK0ms30qPrxE7ZtRXZb1khT5vjLwm71tCQWPLfvcRzvWH-rnFNBqkgRIPfxpZimMw8uXYj_Qzo86nnaDzdca3dwV_AJWNVEHm83jtn5g-36BYEI8G0pgJgtSxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de798daa31.mp4?token=LEUekTjGrGYwJILX1z6bX87yGwdJmSj0Jcf8z0mitM4CE5psCdzxm5j6OY2S27Cv9BJoN5iOKJtp6f3lK2gfpaCEA4ByekOjylAy3ALAndynhjk0ohi9zoQRd883p155NDdbrGIpOngZcebrRudSfSaqorOODacX9m3ddWha6qeqnNWpotfoe9G_16xMTLHBhkp8eIk6gYjO9e9ecHy8pDFDeMNqBK0ms30qPrxE7ZtRXZb1khT5vjLwm71tCQWPLfvcRzvWH-rnFNBqkgRIPfxpZimMw8uXYj_Qzo86nnaDzdca3dwV_AJWNVEHm83jtn5g-36BYEI8G0pgJgtSxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توقیف کامیون با رانندگیِ دختر ۱۰ ساله در هرمزگان!
🔴
رئیس پلیس راه استان هرمزگان:یک کامیون کشنده که توسط دختری ۱۰ ساله هدایت می‌شد، توقیف شد.
🔴
این اقدام، مصداق آشکار به خطر انداختن امنیت ترافیکی و جان کاربران جاده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/134670" target="_blank">📅 11:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134669">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/673fc2d1a7.mp4?token=VLOgEjS4udOvJJrTrBNkJ3LP8hBvO554Gp9Mbnswo5jFUSaQYHtXyxb9rj9ifOYstLaEIcOkoN-8Ew939ZUEbUEbNlMneSOH4k45mfr87Vusby5vifzwEWyoXakxv1uGHzGlc5dwJJT3CjF06b2aEr4yNdrPwCkry5vc4KuOyVy1ZEDZRY-OGhK7yYSrRR4wy4CkGt1rTwmUK4tTItjk1Odm0dAG5pjNA-S5Y757dI1_XlZYhG06jIMQm-Jev2bFmEh5GKwhTrLINW83jV4rIAK-AsOOlwbmSzZbRpCavCxl4NWR6DFEg8paYdrLFenzNrM2-mk03P50dxFkGfbcpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/673fc2d1a7.mp4?token=VLOgEjS4udOvJJrTrBNkJ3LP8hBvO554Gp9Mbnswo5jFUSaQYHtXyxb9rj9ifOYstLaEIcOkoN-8Ew939ZUEbUEbNlMneSOH4k45mfr87Vusby5vifzwEWyoXakxv1uGHzGlc5dwJJT3CjF06b2aEr4yNdrPwCkry5vc4KuOyVy1ZEDZRY-OGhK7yYSrRR4wy4CkGt1rTwmUK4tTItjk1Odm0dAG5pjNA-S5Y757dI1_XlZYhG06jIMQm-Jev2bFmEh5GKwhTrLINW83jV4rIAK-AsOOlwbmSzZbRpCavCxl4NWR6DFEg8paYdrLFenzNrM2-mk03P50dxFkGfbcpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبت‌های مهدی مطهرنیا در مورد احتمال حمله اتمی به ایران
🔴
باراک اوباما هم در آخرین سال ریاست جمهوری گفته بود پایتخت‌های ایران و کره شمالی در مقابل حمله با بمب‌های کنترل‌شده هسته‌ای استثنا هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/134669" target="_blank">📅 11:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134668">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وزارت خزانه داری آمریکا؛ ۱۳۰ میلیون تتر دیگه از دارایی های ایران رو مسدود کرد!
🔴
جمع کل تترهای مسدود شده بانک مرکزی هم تو یک سال گذشته از ۱ میلیارد تتر عبور کرده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/134668" target="_blank">📅 11:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134667">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbRbYn9P5ZdLWb4LC2p2aD-xRfIpc3EY8-32DZrFEzOp-EukpmA03ux0UvGhA52Vc5mURR-Lmr3tzLJZyLqxgy47SdOYjUqkxMUrmtK9KdxH1VqcAI-6QPN7P3fdEJm1WiGu9D5_2fGJM3yyTDX0o_RK_hsa1M_yPWM73AO7IKctQoIweWrQ3f3j9vsKF2wuJcb-h3O4YdXIApMvvsJcVwJJGusVDztjjPnEdiLMsQ5YDn4NQKV_L4pthiEY9oufdPTVC1TVsSMVxmeXviL0kjdWuMbHGAx3iOsOjQKDjanRBo4kJxvytTJLGttXxfodwU1TMTILga-Y9uTLbnIMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرآنلاین: احضار برخی نمایندگان تندرو در پی ماجرای تحصن مقابل مجلس
🔴
مجید نصیرپور، عضو کمیسیون اجتماعی مجلس، در گفت‌وگو با خبرآنلاین با انتقاد از عملکرد برخی جریان‌های سیاسی و رسانه‌ای در دوران جنگ، گفت بخش زیادی از تریبون‌های رسمی و رسانه‌ای در اختیار یک جریان خاص قرار داشت و انتشار برخی روایت‌ها و اظهارنظرهای هزینه‌ساز، زمینه شکل‌گیری شعارها و برخورد با مسئولان کشور را فراهم کرد.
🔴
وی با بیان اینکه برخی افراد با وجود مسئولیت و جایگاه خود نباید به اختلافات دامن بزنند، مدعی شد بر اساس شنیده‌هایش، تعدادی از چهره‌های مرتبط با تحصن مقابل مجلس از سوی مراجع مسئول احضار و به آنان تذکر جدی داده شده است.
🔴
نصیرپور همچنین تأکید کرد برخی جریان‌های سیاسی، بقای خود را در ایجاد دوقطبی و اختلاف‌افکنی می‌بینند و معتقدند با از بین رفتن این فضا، سرمایه و حیات سیاسی خود را از دست خواهند داد؛ موضوعی که به گفته او، در نهایت هزینه آن بر کشور و مردم تحمیل می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/134667" target="_blank">📅 11:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134666">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
روسیه: جایگزینی برای حل‌ دیپلماتیک بحران تنگه هرمز وجود ندارد
🔴
متأسف هستیم که رویارویی‌ها پس از امضای یادداشت تفاهم، بار دیگر از سرگرفته شده
🔴
امیدواریم که مذاکرات ادامه پیدا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/134666" target="_blank">📅 11:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134665">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
قیمت دلار آزاد امروز به ۱۸۸/۶۰۰ تومان رسید...
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/134665" target="_blank">📅 11:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134664">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
روسیه: شب گذشته سلسله حملاتی را علیه تأسیسات صنایع نظامی در کی‌یف و زیرساخت‌های بندر یوژنی در اودسا انجام دادیم
🔴
وزارت دفاع روسیه سه‌شنبه ۲۳ تیر اعلام کرد نیرو‌های این کشور شب گذشته سلسله حملاتی را علیه تأسیسات صنایع نظامی در کی‌یف و زیرساخت‌های بندر یوژنی در استان اودسا انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/134664" target="_blank">📅 11:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134660">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nl4avOmbwqh1n-R8T4HZ4xODKDDV74TeyNh2AlzWcenMKUiyyX6QcOicJ_ebAM5JwJFQsUVFtAkP8aIQjjbKr84f2YKcv0ZgmMyn4ORdOzU6AsX8ekfvmrC8kOrgY7-cIgmTgqxutXVFYKQlfs9Uonj778Dwd0YPkeg3f9PqHSmGdHIC0bgNapVEDPP5m_IXXBfOoUzznOPJtSGwXfWn-GElEbz8bpqgidSgGgJ0-xRYxXq3ItqRs15rcYQhcn4TksYJwkDgEVQ0G_5I0pvH13J-vXNzh-Qm18QTt1NW8NVMvA6JQfRd6BVgcEsCecitWW7mB_YIi5--S4SkAYw-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRXrNdHk1ZgDvUbcECWrKy-gDLmRAFaSKV0p5mOjHaaGvHBKPlkRKbQD0UVCT4xlxy43s4lmJ92VAxpWwmPnZs_F1upxGiFviXvEYFGTRIEgafZU5KeLWS64GmGxmJOUKkcoPo1btlQCI7rUrY73Amc7U7G0gUuEzDRXkuFRHaq3iXOlqtlPncVybbmF5uaP4SIc3xuMmePrBqh91U1jjbvNzJ-nfyv1rgwXB9qcpEKMaEY9afr57OXwJ3_0AJ9J80cK1gi-nCeAklJyrkghYbEjEAXuFxTsKzILO6zOFwrRsFjPV_1OvzZHsgfGhcu5xOA3r3eyZT4YlTiqEd_rGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgYAP6aFCwz9T1rFYE3bHLc10IgUIp3Rb4XmWv5kr87hXS7Fl_I5JLBKlbn3qZo7q52NYLZ9thwCXv_d1dG0CA39Dgy9Gi3XjCX2TG86jMU2MeRf2J6aR-9fGmf7XKCAnkOVwN935O2SCYMKueJTvCSfZUF53YeSmOs9jbteFZTSdBYkGvxiztsDzuAqg06wCUEkzhsQFY23i7njFJSVMDHowXr1XiGhH-sHQWO8jjVF8WPXL3M3vfXILbY8LW0zlK8c0aI8tAwQGKQmEjCvAkzx_RsJJsUrs4j4LLDQXV7JkeL66ygjQ6ollwTXnHLcM6CH3eqOjRu8PHd68pExdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVMR6jeIAa_j90Irep-Rn3kwwF4nhl6hXUR-aa4EfPatcs4drFxth14NowIpulxQKDy-GLMzjFvu53m4R2PJEuvgLO9Z66U4DDtAUCOjk_-F7sdfkYAejVL0LkQwJZ848vPJ1WnOCqRN9dTrd5_HdVAcKZN5QM8-pjb7Krix8qkrLVAQOAcX3zhPtkwl-bWLwI0ihEUn5elL9UCI4hZYZsLpJjFfe-_B7uAH2sc-FwriMPKHX4nk6qvLl0_ea9FnIHx_BL-t1Nf3m49Fm5EEyVxRb9DSIAeuqlHFD6g0LJvJlSC2wo8Wf7QYq8AXlDCpVJoxQ4yDXMGIUyId8I32Hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بازیکنان آرژانتین بطری آب جردن پیکفورد پیدا کردند؛ بطری‌ای که روش نوشته شده هر بازیکن پنالتی‌ به کدوم سمت میزنه.
خنده‌های انزو فرناندز که مقابل اسمش نوشته شده بود “وسط بایست” (یعنی پنالتی رو به وسط دروازه می‌زنه)
@AloSport</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/134660" target="_blank">📅 11:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134659">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c9b24d606.mp4?token=slmQJ4MbKetlw6x8wmTrzchpjfTeahOSVdfyRJAxoWIiiU564l5dxtLp7ldEG-nwVFCNZJmys2hPwQmCSTuq5UAWTWTpjNzo0y06X3QrbpyC-Gz15Ej3ofb08nF-sGUS1DJXs76soyA5-8wWF-4C9zg8NnPjXz4Cb8KN3-EW9kAHeQto-6gbpskze5GcQygkDEO92H3AkBudJkzwsfpvA7L5ZL3by3a6oRF5U_g32ZgzJ5jKhM_i0FUAB7YYvJQE6oHm0zdUmh_-ZLuhBnvB_069ucyho5j7NtlEeuSILRG67aUrBqlsl81QPqr5qxZoi5C8hdhl-Q_woMiu1lNjqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c9b24d606.mp4?token=slmQJ4MbKetlw6x8wmTrzchpjfTeahOSVdfyRJAxoWIiiU564l5dxtLp7ldEG-nwVFCNZJmys2hPwQmCSTuq5UAWTWTpjNzo0y06X3QrbpyC-Gz15Ej3ofb08nF-sGUS1DJXs76soyA5-8wWF-4C9zg8NnPjXz4Cb8KN3-EW9kAHeQto-6gbpskze5GcQygkDEO92H3AkBudJkzwsfpvA7L5ZL3by3a6oRF5U_g32ZgzJ5jKhM_i0FUAB7YYvJQE6oHm0zdUmh_-ZLuhBnvB_069ucyho5j7NtlEeuSILRG67aUrBqlsl81QPqr5qxZoi5C8hdhl-Q_woMiu1lNjqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از ماهواره های استارلینک ایلان ماسک در آسمان ایران، دیشب
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/134659" target="_blank">📅 11:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134658">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزارت خارجه آمریکا بامداد پنجشنبه از موافقت با فروش ۲ میلیارد دلار سامانه‌های موشکی نقطه‌زن به عربستان سعودی خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/134658" target="_blank">📅 11:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134657">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFwItLBuUFtN8h_qiprC9EyGZpcnvVCIFts_r5om1B6OFHj6J6FfHMfqCGhOni7PWTTm6J1PC4b3415Z6Wslilh_GNPx6l7GMLhLkWdRZyJd-JcLl1Wj_I5u7Q6nG-fjQMP5m2FXlbni3oLVKRiVVZk1H-E-jXeu7TlNYzO34tRs0XsN8MOs1oYgHkWeuLt97vUciCOh9Psy_Y_dlKmr9HloSX4AI9Fo2FgfNGHuZbZXi1FK8frqlYKLcBEFTXo3kILXkP8N5aZAIuvteCuxEC9SEhZoHcJsHA1T8l03un68FI-QABikjAAeSXs8LVf-8giSSXYPHzYcZIn9dmpJGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غضنفری، نماینده مجلس: پزشکیان و قالیباف حاضر نیستند اعلام کنند تفاهمنامه با آمریکا عملا نابود شده
🔴
شجاعت و صداقت عذرخواهی از مردم را هم ندارند. اسمش را جنگ بگذارند یا نگذارند "جنگ سوم" عملا شروع شده
🔴
ترامپ، ونس، روبیو، کوشنر، نتانیاهو باید قصاص شوند. نه تنها یک دلار در جریان تفاهم نامه را آزاد نکردند، بلکه آمریکا در حدود یک میلیارد دلار ارز دیجیتال ما را هم توقیف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/134657" target="_blank">📅 11:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134656">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی وزرای جنگ اسرائیل و آمریکا
🔴
هگست، همتای خود را از فعالیت‌های نظامی ایالات متحده در ایران مطلع کرد
🔴
کاتس بر اصرار تل‌آویو برای ماندن در مناطق امنیتی در سوریه، غزه و لبنان تأکید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/134656" target="_blank">📅 10:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134655">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
صدای انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/134655" target="_blank">📅 10:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134654">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
وزارت امور خارجه پاکستان: ما به تعامل فعال با طرف‌های اصلی ادامه داده‌ایم تا از تلاش‌ها برای کاهش تنش‌ها و گفت‌وگوها حمایت کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/134654" target="_blank">📅 10:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134653">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سخنگوی ارتش: در صورت تداوم حملات آمریکا، جنگ به عرصه‌های جدید کشیده خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/134653" target="_blank">📅 10:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134652">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiRgSdkw0cFJQMpqohHsf7ajP45lcSuQHZmFh1buW84X9YgZCoNrV7FVxZXvEjiP51bva-9eE2OmVbb-Zn1tf_IItkarlwKAEhZTDRKk-RXaH4MFben2wrO2VEZEUvADTyw_3IIdtIxHAnxZ2a6-D0ZzHXCFCqahJOJCY996De4uYSwdP_pGTIo-52MYpfW3uCzevp_A0tk2dEmFUqMKOZnEkvNSqZZVNl92X0EwY7O5dIZxMQu7z1fYVUdxxP0hsFSGzFfil6eCB7Vo4KGSTEoLxah-CLTNbrUFoKxgR4DWdrcYiiVG3uNE83hva7hocdNVsTeLVkElJ6ZExckyiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عقب نشینی نفت برنت به 84 دلار
🔴
قیمت این لحظه برنت: 84,69 دلار.
🔴
نفت آمریکا: 79,42 دلار.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/134652" target="_blank">📅 10:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134651">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
شبکه آمریکایی سی‌بی‌اس فاش کرده است که رئیس‌جمهور آمریکا، دور از چشم دوربین‌ها، از رد پیشنهاد ایران برای توافق هسته‌ای ابراز پشیمانی کرده است.
🔴
طبق این گزارش، ترامپ بر این باور است که واشنگتن با رد پیشنهاد تهران برای محدود کردن برنامه هسته‌ای‌اش، فرصت جلوگیری از طولانی شدن درگیری را از دست داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/134651" target="_blank">📅 10:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134650">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc1a68ea8.mp4?token=sZX4TlPgSDO6dbqFOKwl1WA-4kucwMlPUMasXzJ3tJOt3BmRY_kl8tQnzzl93mixIYxv-ntgATdEXt6p9N9cQOHRdS36F8m20JIppDK_6tZjGTo-QS6t0DfGIIw6L0AmhotN8M8_kK0pZE29eRT-RS5cLB315zv1uhJi4lppc-zj9mdVNpop8kCy_VOe7qyn5lxqi2gRS2g6R3uVc7441NeGxRWYjh_tA5-_K50aWhtUpVRBfx3i_pbj4wQGk68OyB-BwnyrnXjebgHsz_Djd8KEI5WnmYFowiS0YsCchaSUpAdWr0IU159lEdlBc_pXD5W9iKXzk3th8zY7xIhqtJ1NU3ZphuH5f2lUFiQdvVWhCcGINMRvYuf7vd-vbmHM_4MVeexzoAhwisCpNd_mQMs3eWASqnODxjpOGFNdO7ykGBP1hnvpaidne3XveR9CXP-BhVzd1U2KYXesNd2e4zDXc87tVEIsSWqT5KsH8T8QgaqDdGcwyYJ_rYXvkT5Fg4yASdLLC5-81Guq71TDcbK-N2_A7fKLhymAy5YMh97i6lVT3I9D4_RmKswZ_CDfiTgRiDNMSIQMquRxgT1rT6eqsFkNA7q0n-OUw0e9lPAg-9OCahuEdv6_UsKqciLqWJWbvyqGFayFS-bIGJunlMX7cTuDkEyV-WzLBvAuD-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc1a68ea8.mp4?token=sZX4TlPgSDO6dbqFOKwl1WA-4kucwMlPUMasXzJ3tJOt3BmRY_kl8tQnzzl93mixIYxv-ntgATdEXt6p9N9cQOHRdS36F8m20JIppDK_6tZjGTo-QS6t0DfGIIw6L0AmhotN8M8_kK0pZE29eRT-RS5cLB315zv1uhJi4lppc-zj9mdVNpop8kCy_VOe7qyn5lxqi2gRS2g6R3uVc7441NeGxRWYjh_tA5-_K50aWhtUpVRBfx3i_pbj4wQGk68OyB-BwnyrnXjebgHsz_Djd8KEI5WnmYFowiS0YsCchaSUpAdWr0IU159lEdlBc_pXD5W9iKXzk3th8zY7xIhqtJ1NU3ZphuH5f2lUFiQdvVWhCcGINMRvYuf7vd-vbmHM_4MVeexzoAhwisCpNd_mQMs3eWASqnODxjpOGFNdO7ykGBP1hnvpaidne3XveR9CXP-BhVzd1U2KYXesNd2e4zDXc87tVEIsSWqT5KsH8T8QgaqDdGcwyYJ_rYXvkT5Fg4yASdLLC5-81Guq71TDcbK-N2_A7fKLhymAy5YMh97i6lVT3I9D4_RmKswZ_CDfiTgRiDNMSIQMquRxgT1rT6eqsFkNA7q0n-OUw0e9lPAg-9OCahuEdv6_UsKqciLqWJWbvyqGFayFS-bIGJunlMX7cTuDkEyV-WzLBvAuD-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر از یک کشتی مسافربری که ارتش آمریکا آن را منهدم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134650" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134648">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WVVHF7XH00T_RIicPsYNh1oO4vGDzVwvUhusiCh171mBuKZmfbr2lYSKKZfiPysVf9VSgc985d84QhDBHA6VAfyHhthdU_MJOM8-NlK1FrQmswuygoJjn8AEQprkP8NnrO88_GjV3Ik1SbIdZcWqjjgr20Q07rrb-IyCrjVe7PNbdVSt6rWaO7R8kcDGUwXOqVE9_QTb5Ajbu1W532TeKdhMcz3_nFGYX_syLNqlYhDucMvTyLVqV2EyJyzh8mwcFHMj3UD-T7SBEBnejI5LKXen33VfIGEfN6z3tY7N8bKOOjOphIHBh2lOztb3XNMwhHNZSU2Wq4AAAJUTBuYgSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/abBERpPVkT3WRHopEfhtvaiKqFL5n8Kfz4ZjvQLS4McfY7qBw5po2TMo5bexeM-ChvFg3r2Bx-5jQVoCwaoOjaGng7OqIC5hNcKDWdlX7a8Y8TyPqRChPleC2hoAuIY7VTUuaD0uCeC0pq8jKh2Ic_RpFwUXcChGhH7_Cy3LTlsFeoxv9B5RtLUuR4hAaVmUw-R1OyJ857fz3Q00VGHTdA9K3wKnzVx6S4qEkgyb3R7jqTuJTp0UnD2r1TbragTcOcaXDn9eGDg3_zaR8rbIxjdkJEcDTrFX9sMjo9YEL5NUB4aKe60rZtDJ5KSHYf4D10LVNuwUqEdHDxSDJB-0JA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
ولی ما میدونیم چرا!</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134648" target="_blank">📅 10:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134647">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه روسیه: بحران تنگه هرمز تنها از مسیر دیپلماسی قابل حل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/134647" target="_blank">📅 10:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134646">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6657e40491.mp4?token=qxcfGw7F6jLOitI3T96ueDId2KaKCwde-M3vo1_Fp_EVUhhg-TMGtZf19iUQDMxZI644bHI79A9_7YnXW_M0N5x0m9aJhCqpD5ZfzHKIbUSHiwkE_z2bwKjnagxCemD3SKwsS2xzsZF-UrxHmVbtFfLmMcvalVrJ9oFhfq5pn4JOYKKSvJejth7xLNhOyE2y00oGbcuqjx9cYqhmE8NSYjqFYsEROgyqXxPCKgJzna6j4nlZNda0nNbc5hFT0W0gqFx1tCnKghytkgVS8E6ip2Scbg2sKXNvXTUfVnAEriQZNey5QzpJMts5daefNliOCWaTcPnfjJ_tZeFmWcja2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6657e40491.mp4?token=qxcfGw7F6jLOitI3T96ueDId2KaKCwde-M3vo1_Fp_EVUhhg-TMGtZf19iUQDMxZI644bHI79A9_7YnXW_M0N5x0m9aJhCqpD5ZfzHKIbUSHiwkE_z2bwKjnagxCemD3SKwsS2xzsZF-UrxHmVbtFfLmMcvalVrJ9oFhfq5pn4JOYKKSvJejth7xLNhOyE2y00oGbcuqjx9cYqhmE8NSYjqFYsEROgyqXxPCKgJzna6j4nlZNda0nNbc5hFT0W0gqFx1tCnKghytkgVS8E6ip2Scbg2sKXNvXTUfVnAEriQZNey5QzpJMts5daefNliOCWaTcPnfjJ_tZeFmWcja2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس: اگه رژیم بپاشه، ۹۴ میلیون آدم درمانده به اروپا و ایالات متحده سرازیر میشن! و وقتی تروریست‌ها در همه جای دنیا پخش میشن، زیرساخت تروریستی‌ شکل می‌گیره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/134646" target="_blank">📅 10:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134645">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8vn1Pnbo5w4twZwNmrH54nGSQ-qSBo7-Ydx1eWmNzEO4xazkjClTKC08Lbo3E5KLjCRllhbi4a1qAAvuFCueRtggREZ3C4zNbawswBh2TYoP2-3qabDWWR0Tohjq-3rE-t5oq2AOFOHLGRySAGuuIUVVfJgkAJVVRWCORPxKeS1fUHUe4vQl_0tE1pEisD13F8_kRMigkN6Yp6t3GXSPPTvxppk2bBhrBSKW0c_9tmFn-YVOjZSmNyaPXt0Ppn1p-NeovkSXcRDPLIH7lDZ57o8xMkem05o6kCSEmB15PmrMFnLuMGp2869mfCr44_M40vQ9taj36gubszuk795oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشف جالب مسی و یارانش از گلر انگلیس
🔴
بازیکنان آرژانتین پس از پایان بازی با انگلیس به‌طور اتفاقی بطری آب جردن پیکفورد را پیدا کردند. او تمام عادات پنالتی زدن بازیکنان آرژانتین را روی این قمقمه یادداشت کرده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/134645" target="_blank">📅 10:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134644">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوری /  آمریکا برای حمله به کوبا آماده می‌شود
🔴
شبکه «سی‌بی‌اس» بامداد پنجشنبه به نقل از مقام‌های آمریکایی گزارش داد که پنتاگون در حال آماده‌سازی برای حمله نظامی و تجاوز زمینی به کوبا است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/134644" target="_blank">📅 09:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134643">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سخنگوی قرارگاه خاتم‌ : اگر زیرساخت بزنید، هرچه زیرساخت در منطقه باقی‌مانده را می‌زنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/134643" target="_blank">📅 09:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134642">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
جی‌دی‌ونس در مصاحبه با پادکست «جو روگن اکسپرینس»
🔴
کسانی که از مذاکره با ایران امتناع می‌کنند، هیچ راه حل واقع‌بینانه‌ای ندارند و تنها پیشنهاد آنها بمباران بی‌پایان و بیهوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134642" target="_blank">📅 09:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134641">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سپاه: مرکز ارتباطات ماهواره‌ای و رادار هشدار اولیه پایگاه هوایی آمریکا در علی السالم و اسکله نظامیان آمریکایی در شعیبیه کویت منهدم گردید
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/134641" target="_blank">📅 09:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134640">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
اکسیوس: نخست‌وزیر عراق، درخواست‌های ایران مبنی بر عدم سفر به واشنگتن را رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/134640" target="_blank">📅 09:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134639">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
فارس: آمریکا در حملات بامدادی خود نقاطی در کبودرآهنگ، استان همدان را هم مورد هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134639" target="_blank">📅 09:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134638">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ تعرفه 25 درصدی بر واردات از برزیل را وضع کرد
🔴
مارکو روبیو وزیر امور خارجه آمریکا در سخنانی اعلام کرد که ترامپ، به نماینده تجاری ایالات متحده دستور داده است تا تعرفه 25 درصدی بر اکثر واردات از برزیل را اعمال کند.
🔴
روبیو در صفحه شخصی خود در ایکس نوشت: لولا رئیس جمهور برزیل و دولتش با حسن نیت با ایالات متحده آمریکا مذاکره نکرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134638" target="_blank">📅 09:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134637">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68cd351ed4.mp4?token=VZCjGMN-Z4MTuemWfRJS3gVSaJ0zAe0Wh0v6aCdKRT6s1lsEtp9kNbV-Otx5jipkuMtU9gu4pzR2edN56DN9MYeGZbcIYZq-0xrmXDeNchndQFzwz3iIyEzKtAZuIaWmrCp4KMFgA0ndVn-a0pg_hPXZuBTcBJ1xazynsNWxnTpotvGtS-OwqH2rj1neR_pmdLlpBEvdQwDlh7Vw1AOIiQrZfZWcbYdzfUej56BUI9Z2RSg9rOZt0KfDmDPlNCjZkdwivN54SclZvon9qK5CQ26Hanv7OsRTolRapazALBtMOEumjfQP0IGY1E4qBpeeVzXTDHwd8cRg6gRy1kkQqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68cd351ed4.mp4?token=VZCjGMN-Z4MTuemWfRJS3gVSaJ0zAe0Wh0v6aCdKRT6s1lsEtp9kNbV-Otx5jipkuMtU9gu4pzR2edN56DN9MYeGZbcIYZq-0xrmXDeNchndQFzwz3iIyEzKtAZuIaWmrCp4KMFgA0ndVn-a0pg_hPXZuBTcBJ1xazynsNWxnTpotvGtS-OwqH2rj1neR_pmdLlpBEvdQwDlh7Vw1AOIiQrZfZWcbYdzfUej56BUI9Z2RSg9rOZt0KfDmDPlNCjZkdwivN54SclZvon9qK5CQ26Hanv7OsRTolRapazALBtMOEumjfQP0IGY1E4qBpeeVzXTDHwd8cRg6gRy1kkQqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه وقوع یک انفجار بسیار مهیب و باورنکردنی در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134637" target="_blank">📅 09:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134636">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQe0_TFbmtMcdBKtJshicnKXVcCHrSJgv71hPlaE9eCLoD3xoVScVJ7LwvZo5MGVuT1wKWzss5u3qbp9hXG5FhDzQjnZDluJ9Tbg1D5H6wesyLTLRAUts1-a131TF_reLYM8cDRFtqrydQskb83K46SgiBSTMA1XdFqQsu3QArwSj0lNw-XSUYEtOuwJLTbbMhOOQENITQIjOcqSjzCxcLfJJepZjGSGx6XzFHuhOXPhzrEjha9B6oKYBplB6HElCySKa4lzQmQJERqwUcMyrMx0OaK7C7mTFnkrXdcXWscGPzF-lHu3WRyDvesESus7J5CFbu08AlySqPNi-WAZcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌ان‌ان: چرا ترامپ در حال دریافت گزینه‌هایی برای گسترش عملیات نظامی در ایران بوده است
🔴
به گزارش سی‌ان‌ان، دونالد ترامپ پس از فروپاشی آتش‌بس در ۱۰ ژوئیه، در حال بررسی گزینه‌هایی برای تشدید عملیات نظامی در ایران است.
🔴
این طرح‌ها که در نشستی در «اتاق وضعیت» مطرح شده، بر کاهش تسلط ایران بر تنگه هرمز متمرکز است.
🔴
آمریکا در پنج روز اخیر حملات روزانه‌ای به مواضعی از جمله «تنب بزرگ» انجام داده تا توانایی ایران برای مسدود کردن مسیر کشتی‌های تجاری را تضعیف کند.
🔴
ترامپ علاوه بر تهدید زیرساخت‌های غیرنظامی و انرژی، گزینه‌هایی نظیر تصرف جزیره خارگ و بمباران تأسیسات «کوه کلنگ‌گیر» که گمان می‌رود با برنامه هسته‌ای مرتبط باشد را در دست بررسی دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/134636" target="_blank">📅 08:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134635">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ونس:  کارزاری با بودجه‌ کلان سعی دارد مذاکرات را از مسیر خارج و توافق را نابود کند
🔴
برای این کار، افرادی از یک مشاور سابق ترامپ حقوق گرفته‌اند
🔴
خود این فرد از عناصری در دولت اسرائیل دستمزد گرفته است.
🔴
این افراد به من حمله می‌کنند و می‌گویند نباید با ایران مذاکره کنیم بلکه باید کارزار نظامی را ادامه دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/134635" target="_blank">📅 08:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134634">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
حمله آمریکا به فرودگاه سمنان
🔴
بامداد پنجشنبه، بخش‌هایی از فرودگاه سمنان هدف حملات هوایی آمریکا قرار گرفت.
🔴
این حملات خسارت جانی در پی نداشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134634" target="_blank">📅 08:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134633">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
کیهان: آمریکا از اینکه ایران به بحرین و کویت حمله کند دردش نمی‌آید
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/134633" target="_blank">📅 08:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134632">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وزیر علوم، تحقیقات و فناوری با تأکید بر فراهم بودن شرایط برگزاری آزمون‌ها اعلام کرد که کنکور سراسری مطابق برنامه زمان‌بندی اعلام‌شده برگزار خواهد شد و همه هماهنگی‌های امنیتی و اجرایی برای برگزاری ایمن آزمون‌ها انجام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/134632" target="_blank">📅 08:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134631">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سنتکام: این موج از حملاتمان علیه ایران پایان یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/alonews/134631" target="_blank">📅 05:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134630">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
انفجار در سمنان و همدان
✅
@AloNews</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/alonews/134630" target="_blank">📅 04:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134629">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/alonews/134629" target="_blank">📅 04:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134628">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777fa47436.mp4?token=pPXYB4UJw0q598uNzQZd_5RK5Et4PYNfvw1E95LW5huYy-F67fAysC0g0OdbipzmO3JDYlaWQV7dVn2xUE5Y4Jb1OSVvAPerRwn-DybmhlmEcTEWU1AzfwNNhD_4AS_8wPyUHh6Ckd06-rSIk7CKOVNDVZWgMDf9K56wg7V3EoXCTkDOFaRFmh6wEMkqQrV3HA-__rMjPUVxC9cNzqm2l8hYVlqVgIxnKc6Hb1ystq0ngjpw94NfJFDF7WPv6GpkIohyto7LRrSDMpSO-hTjtnMKvrmNHHlITTr4pIICB0xPpEhpWe7qYqWnJwZF_0zRutLzsOEKz8WXGpm3M78iVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777fa47436.mp4?token=pPXYB4UJw0q598uNzQZd_5RK5Et4PYNfvw1E95LW5huYy-F67fAysC0g0OdbipzmO3JDYlaWQV7dVn2xUE5Y4Jb1OSVvAPerRwn-DybmhlmEcTEWU1AzfwNNhD_4AS_8wPyUHh6Ckd06-rSIk7CKOVNDVZWgMDf9K56wg7V3EoXCTkDOFaRFmh6wEMkqQrV3HA-__rMjPUVxC9cNzqm2l8hYVlqVgIxnKc6Hb1ystq0ngjpw94NfJFDF7WPv6GpkIohyto7LRrSDMpSO-hTjtnMKvrmNHHlITTr4pIICB0xPpEhpWe7qYqWnJwZF_0zRutLzsOEKz8WXGpm3M78iVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این وسط ماهواره‌های ایلان ماسک بصورت خطی دارن میرن و تو ایران هم قابل رویت هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/alonews/134628" target="_blank">📅 04:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134627">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
دفاع‌های هوایی اردن فعال هستند و در حال تلاش برای رهگیری موشک‌های سپاه می‌باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/alonews/134627" target="_blank">📅 04:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134626">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3314d4420.mp4?token=ujAOHGiawT38gBiXavvGdrQamTGxcQ-jTk9K7zgPcrzu41c-3wfsUTL_8PESS0xc4OGNg7MV8-kjJfbhmWUb2LToc1xDum6PNpjQkYOOim0DZ8g2N5esViWluXRY6tHpwm8pTTiGpH5R7C1qntLt1lJ6Tke-43A9I1xOb5NH4xC6LKYyvzbpp4GHELQZH4HmxtGRRPue5iAkM2jKP636m-maCuTRSbnqJYGjmlaIKiZlSK2b-1P3bWuvl5gXbSM4XXRiBwCk-wLIqL0O-SiMP_zHMdCvHVsjn7NmCctfx5nsXwGAGILlTEXO9NmUnHcJPKL85apLyM86RTXeMmjd9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3314d4420.mp4?token=ujAOHGiawT38gBiXavvGdrQamTGxcQ-jTk9K7zgPcrzu41c-3wfsUTL_8PESS0xc4OGNg7MV8-kjJfbhmWUb2LToc1xDum6PNpjQkYOOim0DZ8g2N5esViWluXRY6tHpwm8pTTiGpH5R7C1qntLt1lJ6Tke-43A9I1xOb5NH4xC6LKYyvzbpp4GHELQZH4HmxtGRRPue5iAkM2jKP636m-maCuTRSbnqJYGjmlaIKiZlSK2b-1P3bWuvl5gXbSM4XXRiBwCk-wLIqL0O-SiMP_zHMdCvHVsjn7NmCctfx5nsXwGAGILlTEXO9NmUnHcJPKL85apLyM86RTXeMmjd9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت پدافند در شهر ری
✅
@AloNews</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/alonews/134626" target="_blank">📅 04:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134625">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a093d1ef.mov?token=gown-aFIuorLj2-xPiD1U_mpNW9Bn4NC46xsrx8VkY-ch1I7GeiS5_lgyCOLBgS1rVoBXddHIqDLMHJigFuSz6moIVo3HiPiA-yUBMFQpwaHqJ6hbChoUp0WZI2j9XhOnoZX99aMZBp4TqbUCYNKXvbtUatQPEE5Zm8krSSys4oFCxuRxFZVlQpI7fQMo2QbjhuOJ3GDY68NkOdUjT5DLdzx1yBM5cnRMz-bNcgPLHoF5Sc4MuvpRfy8LlzTH3Xm3YB2diTNVK4BsdKvIwqvvPbdtY1sHwySH6E0aQfZ4_qTEwiuOW3hg4v7gxJI-6YrpJR3yzk1hemMQkZdHAmGYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a093d1ef.mov?token=gown-aFIuorLj2-xPiD1U_mpNW9Bn4NC46xsrx8VkY-ch1I7GeiS5_lgyCOLBgS1rVoBXddHIqDLMHJigFuSz6moIVo3HiPiA-yUBMFQpwaHqJ6hbChoUp0WZI2j9XhOnoZX99aMZBp4TqbUCYNKXvbtUatQPEE5Zm8krSSys4oFCxuRxFZVlQpI7fQMo2QbjhuOJ3GDY68NkOdUjT5DLdzx1yBM5cnRMz-bNcgPLHoF5Sc4MuvpRfy8LlzTH3Xm3YB2diTNVK4BsdKvIwqvvPbdtY1sHwySH6E0aQfZ4_qTEwiuOW3hg4v7gxJI-6YrpJR3yzk1hemMQkZdHAmGYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاکدشت تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/alonews/134625" target="_blank">📅 04:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134624">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فووووووووووری/صدای انفجار در تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/134624" target="_blank">📅 04:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134623">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411fc596e1.mp4?token=jnwKdqegDYwEUsM-JSoVwWIufQcAgp7wL4-YP3z-GXrI4r4Npq0Kgdsuqzk-PrKbGOFnstCwJAhnY-rlgKlPdCONEk7rR308V7fyEXsNwiebMUvkmyQEXzQRDcwzFFRhoOFRGicZ7vAo2lZw6PAq1xTfT6xe8StMktDLEwhu5JpsKBP1_L9XpWiQdpl9tFUcO9bjc0vdtCmM5Nm5dnsP1I5ZWQCGhPBKomCgSZjgYrzgLLDy6zDJqliUEQK7vQ565PTtv56pkiGK54BQAB5p7XY49enlAgoL8RrfK6JQf1pWkxgq0jKSpNGiteCyDO_4DGUySxB05_yr9wDbf5is2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411fc596e1.mp4?token=jnwKdqegDYwEUsM-JSoVwWIufQcAgp7wL4-YP3z-GXrI4r4Npq0Kgdsuqzk-PrKbGOFnstCwJAhnY-rlgKlPdCONEk7rR308V7fyEXsNwiebMUvkmyQEXzQRDcwzFFRhoOFRGicZ7vAo2lZw6PAq1xTfT6xe8StMktDLEwhu5JpsKBP1_L9XpWiQdpl9tFUcO9bjc0vdtCmM5Nm5dnsP1I5ZWQCGhPBKomCgSZjgYrzgLLDy6zDJqliUEQK7vQ565PTtv56pkiGK54BQAB5p7XY49enlAgoL8RrfK6JQf1pWkxgq0jKSpNGiteCyDO_4DGUySxB05_yr9wDbf5is2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/فعالیت پدافند تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/134623" target="_blank">📅 04:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134622">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فوری/انفجار در خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/134622" target="_blank">📅 04:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134621">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری/پدافند مرکز تهران فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/134621" target="_blank">📅 03:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134620">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری/پدافند غرب تهران فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/134620" target="_blank">📅 03:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134619">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">💢
فووووووووری/جنگنده در تهران  احتمالا خودی
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/134619" target="_blank">📅 03:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134617">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
گزارش شلیک موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/134617" target="_blank">📅 03:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134616">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
پدافند تهران فعاله
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/alonews/134616" target="_blank">📅 03:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134615">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
اطلاعات اولیه حاکی از آن است که سایت هسته‌ای طالقان ۲ واقع در منطقه پارچین هدف حمله قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/alonews/134615" target="_blank">📅 03:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134614">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
انفجار در پارچین، شرق تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/alonews/134614" target="_blank">📅 03:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134613">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/718dd6f75e.mp4?token=DcM-umaRMQ1WUpXw4irt52lrh3y3IxepNIxGpcOkKSYUjCwzplTpKV35mi25_7TunbU6I49Kykp9CW1yYt2VJxSl18pvQTlUvT7iH70i14uIvfYitxKmaSAYbnuPTgPgM_FNUH5k8fy9hyR3NtlHhcXie7K2fHQwo2rUinh7OEtNKce4Ad2bHyMmUq4YgwS_YsKRmIVgvq3n0VAKJOF0H-M74cF_09W7-Msm4LMYc2Z0X3UhLkMAmXRLa1sAkMVtwkVDCnieYDa5fE8ElJoU699x_FA_Z4ADWtRL9DpKKh8WLlyHqHIdkcJvrp-GzbKikaIl1VBlf2XaPRRHaqbOdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/718dd6f75e.mp4?token=DcM-umaRMQ1WUpXw4irt52lrh3y3IxepNIxGpcOkKSYUjCwzplTpKV35mi25_7TunbU6I49Kykp9CW1yYt2VJxSl18pvQTlUvT7iH70i14uIvfYitxKmaSAYbnuPTgPgM_FNUH5k8fy9hyR3NtlHhcXie7K2fHQwo2rUinh7OEtNKce4Ad2bHyMmUq4YgwS_YsKRmIVgvq3n0VAKJOF0H-M74cF_09W7-Msm4LMYc2Z0X3UhLkMAmXRLa1sAkMVtwkVDCnieYDa5fE8ElJoU699x_FA_Z4ADWtRL9DpKKh8WLlyHqHIdkcJvrp-GzbKikaIl1VBlf2XaPRRHaqbOdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار ها در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/alonews/134613" target="_blank">📅 02:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134612">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826a7e9343.mp4?token=fYDNAY9pZdqLDXMmYHlGx122oabsPRC2CjKgYQhEDGGfRFXqZAmD7M45r8iSN_ScTLB4HvpMJa40vPModKqC0a9Wp4VqZrUjV1Kqu4DPGkw4M4IG6UMgj3W4Rssq0YvuPyney3iF2P7bcaj5bjo-UgComD1icreL23x0wADVDNNKa3whvM3va3NpwmhJysteq72h1zk2TpXKMpCJW8LSilsuPpQkeCYfjMYwbe4PM5cJqmXpemFoohvapijDPn5QmCOBei1KZtjQcJGAygLVQgt689KcLTUL8oUze7RLGIkWNL5auDsO_lBKlp28M_-78ADvu6KPubd8QfSAr6_jRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826a7e9343.mp4?token=fYDNAY9pZdqLDXMmYHlGx122oabsPRC2CjKgYQhEDGGfRFXqZAmD7M45r8iSN_ScTLB4HvpMJa40vPModKqC0a9Wp4VqZrUjV1Kqu4DPGkw4M4IG6UMgj3W4Rssq0YvuPyney3iF2P7bcaj5bjo-UgComD1icreL23x0wADVDNNKa3whvM3va3NpwmhJysteq72h1zk2TpXKMpCJW8LSilsuPpQkeCYfjMYwbe4PM5cJqmXpemFoohvapijDPn5QmCOBei1KZtjQcJGAygLVQgt689KcLTUL8oUze7RLGIkWNL5auDsO_lBKlp28M_-78ADvu6KPubd8QfSAr6_jRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرسشگر: آیا شما برای ایران ضرب‌الاجل تعیین می‌کنید؟
🔴
ترامپ: «آنها تقریباً از همه چیز باخبر هستند. آن‌ها باید رفتار مناسبی داشته باشند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/alonews/134612" target="_blank">📅 02:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134611">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
گزارش قطعی برق در برخی نقاط تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/alonews/134611" target="_blank">📅 02:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134610">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
۱۰ انفجار قوی در بحرین
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/alonews/134610" target="_blank">📅 02:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134609">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4XJ-sXaq3zRtfVdnEUe34pejMOwgeekqmzY5hPpdScfEGPdwQYzdOWfshb21SyTBk-vnBq-WDumOG-cUsO5fTiHSoVirq6CXsLBoSNZRPvaWNU_-0MtAKMaYHsm-0SQSRxReTDuRJDqm3FdKbTJgh5xIiG2i6xtNCLS8I0OIZHk0C7PLdh5iCThZ21uzbmDF4hyVfrh0lNNOZsKleFQgDwjctiJymKRaxBZeB_CmENbqOygHnZKUEREu0hhb7s70fyvu0bIXnxAH7bgGzkDDv2BOsld7qy0k4kJd-VN_yL32VNSsM2LQ_9TySwBEURlkwjwZr2w2HTHwPuIxC6w6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری و رسمی /افتخار ایرانیان واقعی
🔴
علیرضا فغانی داور فینال جام‌جهانی بین اسپانیا و آرژانتین شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/alonews/134609" target="_blank">📅 02:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134608">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwsAidXeDFC_C_9yJyx0pGrYqfrO6CF9_7STXX6vrUNnX1P_jZMNwzzcq3A5KKIoYEX-4AaD28FTvSf8vwGkuCv9Ts2jgTlIwjmABJFkbD5NQs6RWPrIqotSpXrxReof6hrjEbjol6Pbs3o-2A24wSPKSm9GAqTLcc3TxtYiu9cgVSeRsNlQcJLPAxZ6DfBQiui4922IfwkeqzB5HCyTmuHgB17dA-E1azcAwUAXsF1sfzgqOOs6NiFybVNl8A5FwoSR1OF743xJg7PDWYx5LJwH8D9imug8vAl9D0lnwl3X1aUUI9EK_j-WJK6sNvLBRzPve9adSHO4Rgj6Xyy78A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:«ایران به یک شهروند آمریکایی که در دسامبر ۲۰۲۴ در دوران «ریاست‌جمهوری» جو بایدن خواب‌آلود به‌طور ناعادلانه بازداشت شده بود، اجازه داد تا آن کشور را ترک کند. او اکنون در امنیت خارج از ایران و در شرایط خوبی است. ایالات متحده آمریکا از این اقدامِ مبتنی بر حسن نیت ایران قدردانی می‌کند!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/134608" target="_blank">📅 02:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134607">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
چندین انفجار در بندرعباس گزارش شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/alonews/134607" target="_blank">📅 02:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134606">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/134606" target="_blank">📅 02:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134605">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJA_2_cCB7SH2EGh6Vxo6OMqnxe_cqrQ6dvgykiJhs1HxjlxCJMCyVBoBs9p3iaO7zxE-VPTgLG17P39DgDKYyc1Wft3EpEql5q2StdRBZCf-zyhxXBfMxotKCQYp1v2YP-JuKmTU0DH5fHvOu_EYhtAeDEUf0XgDes7GIYDBGjvzt4cD1i1NxDJcp1eMQ47X7mIwsQnKg-Y2TKEfHRcvzIEfxhhVcf_dJX1luKQ38qf6Q4YjDszpqcoS08JdxydDE7ZDm5e1O-n4RvwKzCPxKMYhdrkowIVaSB0t7Z13yLGVlQ5HykYWE8l8jQAt4qOkDRN3qQ7exdscWKiv-Z2iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انهدام یک پهپاد جاسوسی در تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/alonews/134605" target="_blank">📅 02:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134604">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfca85fe5e.mp4?token=sywY-553XA3VwLPoKhXSohdOvTz8y_JLXZCxBSEkKJ5TWCBC7TGMXnFy57bxwL_t_T1ENfmYIJUsZvupEuoe8Ih9jgGe6uGA4W3cAmU0o9L-b0xK7Y-JPZC8m4JBb4zfIZBczNMPMQ8290dgPg2HRCjT7aVFDakmuEjebu0esToLSp-mfFMLPscIam5k3r8nKRrQGIbugBgTNy1uuySZHrbHjTIkQFerplqwW-tyAH_iFWnYCmt_oCf_uDXs9dUZ5XPEVFqeNta399IYgnRs8OzC02-SK5kFFUZE9SMBPqA_wI99WS_FtTmFuJsIJ6gG0o9SFWwT-uBMxHB6pi0HXjzcBXjNZsqtSahR_LaQzEn2J_7FgXN_D6E1CoGMgu4vLCULOHd9V13Ld1ugMeDbwIFGC79dSR-sdIlb61HYOhl1IVD0V-9J-KKS2SxW391Y9D9Btqxygi2M071y0cq_TVo8CTzr8lbnhJeml2B0LbG-pFxgZXHVeVOvZhFlIOECjLZDS3OzOduwNUvJXf9VcnCD5Yy4CthfE6ggLA2vA-7HwX_6-BvgCYR4PEsn0Hz4tLQ1pWSewzFckxKzFq0IpS_5FcmNO_V9yS5jxU5b0v5v1ARJ5ChcoyB9h2rfvgXYqza4INq57_0daB3HNu5FgdPlAUzDfZobLu1Dt-MFHzY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfca85fe5e.mp4?token=sywY-553XA3VwLPoKhXSohdOvTz8y_JLXZCxBSEkKJ5TWCBC7TGMXnFy57bxwL_t_T1ENfmYIJUsZvupEuoe8Ih9jgGe6uGA4W3cAmU0o9L-b0xK7Y-JPZC8m4JBb4zfIZBczNMPMQ8290dgPg2HRCjT7aVFDakmuEjebu0esToLSp-mfFMLPscIam5k3r8nKRrQGIbugBgTNy1uuySZHrbHjTIkQFerplqwW-tyAH_iFWnYCmt_oCf_uDXs9dUZ5XPEVFqeNta399IYgnRs8OzC02-SK5kFFUZE9SMBPqA_wI99WS_FtTmFuJsIJ6gG0o9SFWwT-uBMxHB6pi0HXjzcBXjNZsqtSahR_LaQzEn2J_7FgXN_D6E1CoGMgu4vLCULOHd9V13Ld1ugMeDbwIFGC79dSR-sdIlb61HYOhl1IVD0V-9J-KKS2SxW391Y9D9Btqxygi2M071y0cq_TVo8CTzr8lbnhJeml2B0LbG-pFxgZXHVeVOvZhFlIOECjLZDS3OzOduwNUvJXf9VcnCD5Yy4CthfE6ggLA2vA-7HwX_6-BvgCYR4PEsn0Hz4tLQ1pWSewzFckxKzFq0IpS_5FcmNO_V9yS5jxU5b0v5v1ARJ5ChcoyB9h2rfvgXYqza4INq57_0daB3HNu5FgdPlAUzDfZobLu1Dt-MFHzY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سربازی که چند روز از خدمتش مانده بود و آرزوی یک پژو پرشیا داشت اما زیر حملات آمریکا اونو تو پادگان نگه داشتن و شهید شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/alonews/134604" target="_blank">📅 02:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134603">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
جی دی ونس: کارزاری با بودجه‌ کلان سعی دارد مذاکرات را از مسیر خارج و توافق را نابود کند
🔴
برای این کار، افرادی از یک مشاور سابق ترامپ حقوق گرفته‌اند/خود این فرد از عناصری در دولت اسرائیل دستمزد گرفته
🔴
این افراد به من حمله می‌کنند و می‌گویند نباید با ایران مذاکره کنیم بلکه باید کارزار نظامی را ادامه دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/alonews/134603" target="_blank">📅 01:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134602">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
حمله موشکی به کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/alonews/134602" target="_blank">📅 01:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134601">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
دو انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/alonews/134601" target="_blank">📅 01:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134600">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
خبرگزاری فارس :
موشک‌های آمریکا به اطراف یه بیمارستان (بقایی) کودکان سرطانی تو اهواز برخورد کرده و بیماران هم چند دقیقه پیش تخلیه شدن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/134600" target="_blank">📅 01:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134599">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGBorCQE4btqMFpROr_Y2Xvt5RLXe1ocKKbv8QjqEkdeQUUkwCg_maPX9KVjK7fp_ZiQI-4NvPrTTN2XlGrvxoAp8OFye0SZ_kGo-Pf31tFGUVas4Juj_kbXcCQaK7E-LRj3Yqt2DFuQwFutard2mZqhoH9N7Dz_2GHogTtwKcUKwzAR4kOUNQ2-0mNx6QAjDMuFmbCz1M5x6Q0DdJeXoMhGrOGsddm7NmRBQGucjEUrQZ1cWDF-l-nTT_mA4HLkiwSIUgf9SowgiwTTaxF7CwJj1NUzgY457z4NlCxJyOMTd3bOlPRpkVJY9HNPSTY1RvI1blX63lCR5rl5kz7vYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون شرح
‼️
چرا باید پادگان ولیعصر سپاه کنار بیمارستان اطفال باشه؟
🔴
موقع ساخت حواسشون نبود؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/134599" target="_blank">📅 01:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134598">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e619333efb.mp4?token=fkFD9W0tckPtKmauBAdSKwl8dRPXsrgh2VDEGTZWqqH7hFVAtv09edqjjufz7v5KnBxpZwIDDULXBGaQZfVLwPsZ2Yhka0-qVEoPhXCiOwYo5sORNIJQ29b5R11_zj99nSoDvWuowLMeqmnFKopziNQPBb5ApBNIHbSXE81wo8fnXGTUQv3MTa0eNsLN0HvS76x8Y__dzCxkwuzl1ifyoaKS0ifngSj4AnROYHdBKqJs3hqejgNHOqQ2796uavey1wz6qDeIktE9rkl1eJH6vVatJ1DWLG3abYUHJ-dXeTA7npw1theaiKNnWYNv6KF9D8R3PlbX1ejVZgXvxhQXfYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e619333efb.mp4?token=fkFD9W0tckPtKmauBAdSKwl8dRPXsrgh2VDEGTZWqqH7hFVAtv09edqjjufz7v5KnBxpZwIDDULXBGaQZfVLwPsZ2Yhka0-qVEoPhXCiOwYo5sORNIJQ29b5R11_zj99nSoDvWuowLMeqmnFKopziNQPBb5ApBNIHbSXE81wo8fnXGTUQv3MTa0eNsLN0HvS76x8Y__dzCxkwuzl1ifyoaKS0ifngSj4AnROYHdBKqJs3hqejgNHOqQ2796uavey1wz6qDeIktE9rkl1eJH6vVatJ1DWLG3abYUHJ-dXeTA7npw1theaiKNnWYNv6KF9D8R3PlbX1ejVZgXvxhQXfYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بله این جنگ تو جنوب نتیجه رقاصه بازی و گنده گوزی عده‌ای تو صد و خورده‌ای شب به صرف شربت و شیرینی و فالوده و.... با چاشنی عربده تو خیابون هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/alonews/134598" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134597">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
چندین انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/alonews/134597" target="_blank">📅 01:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134596">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
تایید شد/پادگان لشکر 92 اهواز بمباران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/134596" target="_blank">📅 01:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134595">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری/پرواز 11 سوخت رسان امریکایی بر فراز خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/134595" target="_blank">📅 01:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134594">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">💢
فووووووووری/جنگنده در تهران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/134594" target="_blank">📅 01:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134593">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/134593" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134592">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/134592" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134591">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
همچنان صدای انفجار در اهواز به گوش میرسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/134591" target="_blank">📅 00:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134590">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پشمااااااااااااام
😐
هوادار معروف آرژانتینی بازم تو استادیوم لباسش درآورد تا به بازیکنا روحیه بده
😐
◀️
◀️
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/134590" target="_blank">📅 00:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134589">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/gnEOMANCHD2bE9amZGqX9yb8aWCGCLEo9j6iYv2hq_W_HmRpRQsqmF3LOgsYYw2v62ogZYzCXo_mUHLFVPoGKUztPNxvrosYIJd8P1-GJ-DZZM5K6gi0Lpf9dFSXb4eW82iykcXv3KNfkb0-xlsbO58ZRO2efKZlE4zPW97AvhlwcJm1Vw134AiQzB0PIEox-Bwmos3Ad4sI1TnuU_nq2ihitECkN_kvni_UdrSPgFKrIklC8vZoH9rT7bz1S4c1rd3t5yOAF15M-RfbPocbBGvFl5onsO8AnZ7gsXlZShme__GWlLHKlA2qR_KyYGcKFsjE-fvLVT_xCxi_5EPB1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بعد دستِ خدا ، انگلیس طعمِ زهرِ پای چپ پادشاه رو هم چشید؛
آرژانتینِ مسی به دراماتیک‌ترین شکل ممکن به فینال جام جهانی 2026 رسید!
🇦🇷
آرژانتین 2-1 انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
@
AloSport</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/134589" target="_blank">📅 00:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134588">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
آرژانتین با شکست روباه پیر(اربابان پایدارچی) به فینال رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/alonews/134588" target="_blank">📅 00:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134587">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06951345cf.mp4?token=hFzYml-upKjDP_8HahQfNE_zBDhJLpmH7Iip2nKuEjs7_ReUMc26K64DNpaDvtLfXpo8oAxkLyLbZfZN37p_v1wtx99BD6RzalsMDu40KWAIf0rqneGRWe_Nq5D7iSTvu58tSpDUqSZHwLB6m8PMla7XYjrhqxj0293dmiCafMxKkX3x2YcrKn6pzA-Yl7JGlKFqH_uiOePo25eocduWScF5FJXbhabJoK5JuGiqxa9NISvQbNhUljK1tbKhsd03WUI-GgzaLECFhZ3lB6RDAiSVi-jBy99Bi5zEtVYRfIpkLhLAEqu_10Y3dscpuF4f_CLwS4ZtzjnDxBCWf4ogew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06951345cf.mp4?token=hFzYml-upKjDP_8HahQfNE_zBDhJLpmH7Iip2nKuEjs7_ReUMc26K64DNpaDvtLfXpo8oAxkLyLbZfZN37p_v1wtx99BD6RzalsMDu40KWAIf0rqneGRWe_Nq5D7iSTvu58tSpDUqSZHwLB6m8PMla7XYjrhqxj0293dmiCafMxKkX3x2YcrKn6pzA-Yl7JGlKFqH_uiOePo25eocduWScF5FJXbhabJoK5JuGiqxa9NISvQbNhUljK1tbKhsd03WUI-GgzaLECFhZ3lB6RDAiSVi-jBy99Bi5zEtVYRfIpkLhLAEqu_10Y3dscpuF4f_CLwS4ZtzjnDxBCWf4ogew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گل دوم آرژانتین به انگلیس توسط مارتینز رو پاس لیونل مسی
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/134587" target="_blank">📅 00:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134586">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران: «ما قرار نیست فقط بمباران کنیم، بمباران کنیم و باز هم بمباران کنیم.
🔴
ما تلاش خواهیم کرد از نیروی نظامی‌مان به‌عنوان یکی از ابزارهای متعددی که در اختیار داریم برای حل این مشکل استفاده کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/alonews/134586" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134585">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آرژانتین چی کرد
😐
😐</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/alonews/134585" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134584">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گلللللللللل</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/alonews/134584" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134583">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8b8b35f7.mp4?token=s3fonU3OIbZUGKx1VX77FA5Qi0JezuLh1F7S1NRldrkQBXVjL5aP3olQgoS8hpgcDqWmgXokcLDg3r3ho7p-SjjxvtbN_6MW2OCkDmIn2cgLhbpb27OQDZH5VKOO74ICEsPtvVOZOROufimHgfNilUzobjZPTOr-KiYmaX5DY4NrZYXXN7va499o7Yv8vJufbZZOjRstPJrDEFUnfM51Ctj-QEO9ZMFz47-lUBjfKUiBbS63MpuRHewmC3YjeKU909iluVnLbTBurcGiI6V9zZcOEuHKIPSWJBU7oIAOagyxdTVlBLLdVyJ5e3GNF8LMfx0SBcMC67q5hD9XAQHeZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8b8b35f7.mp4?token=s3fonU3OIbZUGKx1VX77FA5Qi0JezuLh1F7S1NRldrkQBXVjL5aP3olQgoS8hpgcDqWmgXokcLDg3r3ho7p-SjjxvtbN_6MW2OCkDmIn2cgLhbpb27OQDZH5VKOO74ICEsPtvVOZOROufimHgfNilUzobjZPTOr-KiYmaX5DY4NrZYXXN7va499o7Yv8vJufbZZOjRstPJrDEFUnfM51Ctj-QEO9ZMFz47-lUBjfKUiBbS63MpuRHewmC3YjeKU909iluVnLbTBurcGiI6V9zZcOEuHKIPSWJBU7oIAOagyxdTVlBLLdVyJ5e3GNF8LMfx0SBcMC67q5hD9XAQHeZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گل اول آرژانتین به انگلیس توسط انزوووو فرناندز رو پاس مسی
✅
@AloNews</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/alonews/134583" target="_blank">📅 00:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134582">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f9afce47.webm?token=kR2PeQgwjmvGJ0B2i5AsqzGkGyLACH7JvdvWwKx2HDSDbkcVtG3EFr1Nra7Lz3KEROSiq-wd7lYW0AW4V3XFzh-4XK-e2ucAnS-DqVvaHtHQ4E174gjd5j1sF5F9NTnWLF6t8erm_erPsCzmREJThy0dWXUcb3kq-208bh7sx8rTLjUgwN2ZaKNaB6nSuMCpa-K7DMEEMaqNykRJbjjeduNnzCDAznjVvKVzmKr6ZSw0JDKvTOvrQLnrsDt4HzXe3a8hQmUh1fhonNqitrAxEUDyyGEXRNML01GtOHXQ7cFhBnfJmOOLA9BMJqxB446kmAAxq5g1SxVQEOE0czA_XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f9afce47.webm?token=kR2PeQgwjmvGJ0B2i5AsqzGkGyLACH7JvdvWwKx2HDSDbkcVtG3EFr1Nra7Lz3KEROSiq-wd7lYW0AW4V3XFzh-4XK-e2ucAnS-DqVvaHtHQ4E174gjd5j1sF5F9NTnWLF6t8erm_erPsCzmREJThy0dWXUcb3kq-208bh7sx8rTLjUgwN2ZaKNaB6nSuMCpa-K7DMEEMaqNykRJbjjeduNnzCDAznjVvKVzmKr6ZSw0JDKvTOvrQLnrsDt4HzXe3a8hQmUh1fhonNqitrAxEUDyyGEXRNML01GtOHXQ7cFhBnfJmOOLA9BMJqxB446kmAAxq5g1SxVQEOE0czA_XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/134582" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134581">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">چی زد
😐</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/134581" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134580">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/026bdaa5ca.mp4?token=vHydpzxMKoFmlOkSn_UtviCkLuWq6ohRN8f3DQ6jn_qiV8G4FZKJjc4Lt87PW8xYAOcw6d_SBFN9CNBSBfbimqNKDjfCWH3TCQTMm_ipt5AuPuoC0VP1szjrV8gaOk6zGFEAnV6OcWtZZTntUoqyEf1_O89oiunv1gpNoBKJL8asOTT8ENttcplKng2hsO7qZ6SBzmNgb1ihCVFLnwToMsgIMC-tgMpKX8R5PIM3eTVhVSFaT8CaVPLbn_PSuR2_TbhBRayr0QhT4uD-cHE2yNMz2ra4H1cUcX-y-suIZQzdX4TNlDr789pnqZRpG-xNYQfqdr60Jc9dAcDcQq8LpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/026bdaa5ca.mp4?token=vHydpzxMKoFmlOkSn_UtviCkLuWq6ohRN8f3DQ6jn_qiV8G4FZKJjc4Lt87PW8xYAOcw6d_SBFN9CNBSBfbimqNKDjfCWH3TCQTMm_ipt5AuPuoC0VP1szjrV8gaOk6zGFEAnV6OcWtZZTntUoqyEf1_O89oiunv1gpNoBKJL8asOTT8ENttcplKng2hsO7qZ6SBzmNgb1ihCVFLnwToMsgIMC-tgMpKX8R5PIM3eTVhVSFaT8CaVPLbn_PSuR2_TbhBRayr0QhT4uD-cHE2yNMz2ra4H1cUcX-y-suIZQzdX4TNlDr789pnqZRpG-xNYQfqdr60Jc9dAcDcQq8LpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/134580" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134579">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
شبکه المیادین به نقل از منابع خبري  گزارش داد در حملات امشب به اربیل واقع در شمال عراق، چندین نظامی آمریکایی کشته شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/134579" target="_blank">📅 00:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134578">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
صداوسیما: ساکنان اهواز شدت انفجارها بالاست؛ از خانه‌ها خارج نشوید و تو خونه بمونید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/alonews/134578" target="_blank">📅 00:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134577">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
انفجار های شدید در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/alonews/134577" target="_blank">📅 00:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134576">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وال‌ استریت ژورنال:
دیروز پرزیدنت ‌ترامپ یک جلسه ویژه برای بررسی گسترش جنگ و تصرف جزایر ایران در کاخ سفید برگزار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/alonews/134576" target="_blank">📅 23:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134575">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e118a97982.mp4?token=aa6SBi8HKwz6Sgq8N_izpK-YY0AOfHJd8frso_rV-ezfbTUOtsjAoHn9G-Aj5IPPuJ8W9acNUtQxIL_NfOUxeR1VI50geRqv9G65PfR5GCADB1sU_3h_QVv6RdRTK6RQf-k6EpJikGKjNDejf17a7r7cB9odZpmePefzxYui-5sIXY9X0_an9CNcC-cKBi3IDoyt_bn6XJ1rUmwDexDV8HMwYtlBM_wLCVGaWjKa06ZllFbg_NQwU8jXsD0pTeAf2Df1WdbDnkP0L3t33iShnJq-FKjSlEuGu4QGDJiaK8esKKhuY84UNYDVjpZ2svqsi0bHqAHfWkCRgawLSp6V4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e118a97982.mp4?token=aa6SBi8HKwz6Sgq8N_izpK-YY0AOfHJd8frso_rV-ezfbTUOtsjAoHn9G-Aj5IPPuJ8W9acNUtQxIL_NfOUxeR1VI50geRqv9G65PfR5GCADB1sU_3h_QVv6RdRTK6RQf-k6EpJikGKjNDejf17a7r7cB9odZpmePefzxYui-5sIXY9X0_an9CNcC-cKBi3IDoyt_bn6XJ1rUmwDexDV8HMwYtlBM_wLCVGaWjKa06ZllFbg_NQwU8jXsD0pTeAf2Df1WdbDnkP0L3t33iShnJq-FKjSlEuGu4QGDJiaK8esKKhuY84UNYDVjpZ2svqsi0bHqAHfWkCRgawLSp6V4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گللللللللللل اوووووول انگللیییس به ارژاااااانتیییین تووووسط گوردووون دقیقههه54
@AloSport</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/alonews/134575" target="_blank">📅 23:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134574">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/026bdaa5ca.mp4?token=IaFNntzmrLfDwBwHPsZw-xwOVcSy8-C5nE9klaW0lBw_xqr6I1-Vzbp75Q583u-UeC7j2ZlXI_0JdT85Lycubdw1RYdbF97t_GJgLiA8kegfSrlljMpj2X6kHAxFelsdYEZxVv1rnAT3MbPzscPC1_poTh2kMHQ7hKvN51F-Qs1Nah4SSfzZcwyJuJVm2rblQ63CIhFIdasat8MQUVMSCw_YXIOgkLVdANrttPIpQYx7JuDa3siOobGlyv1q83DkiNb6j5V6CZlH7te4R-gFTClx37_3bdlTIbBeUT1kk51ikn78JDyjJ6ku16BETH977oYg0EN-wCtOnQY9aq7wuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/026bdaa5ca.mp4?token=IaFNntzmrLfDwBwHPsZw-xwOVcSy8-C5nE9klaW0lBw_xqr6I1-Vzbp75Q583u-UeC7j2ZlXI_0JdT85Lycubdw1RYdbF97t_GJgLiA8kegfSrlljMpj2X6kHAxFelsdYEZxVv1rnAT3MbPzscPC1_poTh2kMHQ7hKvN51F-Qs1Nah4SSfzZcwyJuJVm2rblQ63CIhFIdasat8MQUVMSCw_YXIOgkLVdANrttPIpQYx7JuDa3siOobGlyv1q83DkiNb6j5V6CZlH7te4R-gFTClx37_3bdlTIbBeUT1kk51ikn78JDyjJ6ku16BETH977oYg0EN-wCtOnQY9aq7wuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/134574" target="_blank">📅 23:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134573">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: زمانی که ایران به ثبات برسد، قیمت نفت به ۵۵ دلار به ازای هر بشکه خواهد رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/134573" target="_blank">📅 23:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134572">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3619cfce23.mp4?token=oGNDc9MxGGyAunn2MkopYkG3YdDPhK3W-fgVUozZhEdvBaruxavURplIT6X9OGmNtf0g6so_xhEq_BUX59eB7qMnQWcIF8kmKcZPzWfP1TEEkfDlJgumWet8k2RErQqHSrfVf-voBb-hIJz5_qj3yEPmb7ptBNgCYThEGcRhIuHoLDyxnpnxdFnqNnjFZqDgOhKNaMrTS6UMHacyn6JcrUdLEQ0_-6ILzGUSwl8eFirsepmDLHW_daArPjRk-g1Ui5VeeBYkdKng0YVVzXQ6eI2FQtpE4TXyd5HanxORUdWFYSBkegGvNp7kuxuhcScUcelsTzwO9njiY7pRCdBxyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3619cfce23.mp4?token=oGNDc9MxGGyAunn2MkopYkG3YdDPhK3W-fgVUozZhEdvBaruxavURplIT6X9OGmNtf0g6so_xhEq_BUX59eB7qMnQWcIF8kmKcZPzWfP1TEEkfDlJgumWet8k2RErQqHSrfVf-voBb-hIJz5_qj3yEPmb7ptBNgCYThEGcRhIuHoLDyxnpnxdFnqNnjFZqDgOhKNaMrTS6UMHacyn6JcrUdLEQ0_-6ILzGUSwl8eFirsepmDLHW_daArPjRk-g1Ui5VeeBYkdKng0YVVzXQ6eI2FQtpE4TXyd5HanxORUdWFYSBkegGvNp7kuxuhcScUcelsTzwO9njiY7pRCdBxyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس اذعان می‌کند: ما کاملاً ارتباطات پرونده‌های اپستین را خراب کردیم. ما همین الان این کار را کردیم.
🔴
اما آیا فکر می‌کنم دلیل خراب کردن ارتباطات این بود که سعی داشتیم چیزی را پنهان کنیم؟ خیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/134572" target="_blank">📅 23:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134571">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وال استریو ژورنال:  ترامپ تمایل دارد فعالیت‌های نظامی آمریکا را در ایران گسترش دهد، این تصمیم پس از روزهای مشورت با مقامات ارشد مشاورانش اتخاذ شده است.
🔴
از جمله گزینه‌های مورد بررسی: گسترش حملات هوایی، اعزام نیروهای زمینی برای تصرف جزایر ایرانی نزدیک تنگه…</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/134571" target="_blank">📅 23:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134570">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ترامپ درباره جمهوري اسلامي : ایران به زودی شکست خواهد خورد.
🔴
آن‌ها گفتند «قابل دسترس بودن»، این یک کلمه جعلی است که از آن استفاده می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/134570" target="_blank">📅 23:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134569">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
انفجار های سنگین و پی در پی در اهواز...
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/alonews/134569" target="_blank">📅 23:39 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
