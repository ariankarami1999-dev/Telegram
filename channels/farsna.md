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
<img src="https://cdn4.telesco.pe/file/gnvcvypaf-6VsBmdxcUJ2vPtKzhOnkF7u8zOdGGR7p2RzYpIeSXv7umsxHN1VZO73VW9iawa0VmJ4ZIu8s5Apy6KpV8IzAjXsSMQdUSxx_pDhjbkKIrm19rpDXyKpeQ_tHQG0Nkj5_WAADcz82dtlwG36YD7cjxy9HZHu4tZGC2VsFs5FciaPtUG1XRp7fQPtWqT-kfLTl2YnQPFEiGXZwKne2CFtz96HVyYw2Qt7zh23aLHJs71x7Qzw0t39p4i-6et8mlexI_IEq3wx3Qndu-YAp7V-N9dIorebuEAL37_ZewRS-BaVjhBAPop5njd0pX0YgzqzZKqerzdBCpuRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 08:01:41</div>
<hr>

<div class="tg-post" id="msg-449568">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
سپاه: مخازن سوخت، سامانه‌های پاتریوت و FPS به طور کامل منهدم شدند
🔹
به استحضار مردم شریف ایران می‌رسانیم، رزمندگان پرافتخار نیروی هوافضای سپاه، در سومین مرحله از عملیات مقابله به‌مثل و پاسخ به تجاوزات رژیم مستکبر و متجاوز آمریکا، مخازن سوخت و سامانۀ پدافند…</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/farsna/449568" target="_blank">📅 07:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449567">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گرما فعلا ماندگار است
🔹
هواشناسی: از امروز دوشنبه تا چهارشنبه در اکثر نقاط کشور جوی آرام پیش‌بینی می‌شود و تا پایان هفته ماندگاری هوای گرم ادامه خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/farsna/449567" target="_blank">📅 07:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449566">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
رسانه‌های خبری از فعال‌ شدن پدافند هوایی پاتریوت آمریکایی در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/449566" target="_blank">📅 07:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449565">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گزارش‌ها از حمله به یک شرکت تجاری آمریکا در بحرین
🔹
برخی منابع مدعی شدند که مقر یکی از شرکت‌های تجاری آمریکایی در بحرین مورد هدف موفق قرار گرفته و درحال سوختن در آتش است.  @Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/449565" target="_blank">📅 07:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449563">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d296bb0b4e.mp4?token=kxIMbfc8u1y9PSQBjTMHNjET-OfaruHD4MvKuBNMB-WzOokLNcodgRsFflfWWDJyNXsa8jhxzF8oiPCcbIP3mVYiFIjAAUZX_iB44mzNlHRdGMXakzHop8M_Wd0iI-tE1nx0IwAKFySBBOZ3b4hqpDUx1pXiNdbJyCpq7pDFmoXsIbwLBT0d6Wzjf9OUXd1sFsIoT1mV2F2m5APtSZGLKCvkyP0BKqGmaivWN5GcJJ-5ck4WDe1Rjumi_T_EO6MfsxLD1qAFovDa53Qz_bkElWX8gUjelRfWI_BhCOVD13HNsUlheZE3IYua6ZpSd9FLiA9bqnSboK2dn-shUWuiUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d296bb0b4e.mp4?token=kxIMbfc8u1y9PSQBjTMHNjET-OfaruHD4MvKuBNMB-WzOokLNcodgRsFflfWWDJyNXsa8jhxzF8oiPCcbIP3mVYiFIjAAUZX_iB44mzNlHRdGMXakzHop8M_Wd0iI-tE1nx0IwAKFySBBOZ3b4hqpDUx1pXiNdbJyCpq7pDFmoXsIbwLBT0d6Wzjf9OUXd1sFsIoT1mV2F2m5APtSZGLKCvkyP0BKqGmaivWN5GcJJ-5ck4WDe1Rjumi_T_EO6MfsxLD1qAFovDa53Qz_bkElWX8gUjelRfWI_BhCOVD13HNsUlheZE3IYua6ZpSd9FLiA9bqnSboK2dn-shUWuiUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
ادامۀ حملات پهپادی ارتش به پایگاه‌های آمریکا در منطقه
🔹
در پاسخ به تکرار حملات غیرقانونی آمریکا علیه  کشورمان، ساعاتی قبل و در دور جدید حملات پهپادی ارتش جمهوری اسلامی ایران، محل استقرار نیروهای آمریکایی،سامانه های پدافندی و موشکی، جان پناه و سوله های…</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/449563" target="_blank">📅 07:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449562">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae4fe3415.mp4?token=kGkhz2F7_p4cR9QEi0kNR-1WnbpqHKi0xuXfP1fNTMlxiF8iXxzKo2XsD79hofxDlM0pWu2MB4_hYNPPlnJCbdYcP1oGvdLHIGXHP8aXcbibndT_s-7ZYSszID0MnVlNoM4UHEjo_0ssEcjHiJJkwCvAGH8pHOVyqE1CIs1dQSXetPAXq-5OP2ta0FLapttjQyajr-iRwvBUOe7OweOwv3ZgKoZWxhmRpQIMvTcszzCXvNNAjBtqB5RKk8J78udEUQit7DntUNoV-nRIwkeAUzdzegonlZDy4cUsDcMhKpD0PKzjBVctjVQM5dL-GaPCPd1npT9fEzR7h2dNwjaQMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae4fe3415.mp4?token=kGkhz2F7_p4cR9QEi0kNR-1WnbpqHKi0xuXfP1fNTMlxiF8iXxzKo2XsD79hofxDlM0pWu2MB4_hYNPPlnJCbdYcP1oGvdLHIGXHP8aXcbibndT_s-7ZYSszID0MnVlNoM4UHEjo_0ssEcjHiJJkwCvAGH8pHOVyqE1CIs1dQSXetPAXq-5OP2ta0FLapttjQyajr-iRwvBUOe7OweOwv3ZgKoZWxhmRpQIMvTcszzCXvNNAjBtqB5RKk8J78udEUQit7DntUNoV-nRIwkeAUzdzegonlZDy4cUsDcMhKpD0PKzjBVctjVQM5dL-GaPCPd1npT9fEzR7h2dNwjaQMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کنایۀ خبرنگار آمریکایی به وداع با سناتور جنگ‌طلب فقط با یک گل!
🔹
یک خبرنگار آمریکایی در مقایسۀ مراسم باشکوه تشییع پیکر رهبر شهید انقلاب با مرگ سناتور جنگ‌طلب آمریکایی، با انتشار ویدیویی از خانۀ او نوشت: آمریکا ۳۵۰ میلیون نفر جمعیت دارد، اما تنها چیزی که نصیب این سناتور شد یک دسته گل کوچک مقابل خانه‌اش بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/449562" target="_blank">📅 07:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449561">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گزارش‌ها از حمله به یک شرکت تجاری آمریکا در بحرین
🔹
برخی منابع مدعی شدند که مقر یکی از شرکت‌های تجاری آمریکایی در بحرین مورد هدف موفق قرار گرفته و درحال سوختن در آتش است.
@Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/449561" target="_blank">📅 07:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449560">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYD5fe0tJtVqtqg-QlDVZ-fv5mSOosgQuJ0mBsjwvy0Y71VFaQHPsuuQRUZ4YnpBQfdZv2_l5aW3dRjjRcUThJLltPx7JcOVaQC8s3kE_sPCV2G7HMU4JUasWtgoglTVtWP6fEu34ctspW1z5lbItGsDtbpS7o0uBsuvvEEOR3aRKjKHU8ETrIFeN14n3SRvR_2OUmk1I56Bg-UMVBdMTQbr26096x4Mz9RsMa1q_eIzOXyYFkGwi7swwawjI9CkBhqnTWu1U-6-fU3ovc3ViCWSARns7vmKGKrFIVGcVJpB8L6ith-4xCvQ6YkSjOF7qI7ndalC4b4GtSNr6LcTug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد قربانیان زمین‌لرزه‌های ونزوئلا به ۴۴۹۰ نفر افزایش یافت
🔹
طبق اعلام رئیس‌ مجلس ملی ونزوئلا، تعداد قربانیان دو زمین‌لرزه ونزوئلا به ۴۴۹۰ نفر افزایش یافته است.
🔹
طبق گزارش خبرگزاری آناتولی، بر اساس آمار رسمی، بیش از ۱۶,۷۰۰ نفر مجروح شده‌اند و نزدیک به ۱۹,۶۰۰ نفر در اردوگاه‌های موقت اسکان داده شده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/449560" target="_blank">📅 06:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449559">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
سپاه: مخازن سوخت، سامانه‌های پاتریوت و FPS به طور کامل منهدم شدند
🔹
به استحضار مردم شریف ایران می‌رسانیم، رزمندگان پرافتخار نیروی هوافضای سپاه، در سومین مرحله از عملیات مقابله به‌مثل و پاسخ به تجاوزات رژیم مستکبر و متجاوز آمریکا، مخازن سوخت و سامانۀ پدافند…</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/449559" target="_blank">📅 06:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449558">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
سپاه: مرکز فرماندهی و کنترل پهپادی ارتش آمریکا در بحرین درهم کوبیده شد
🔹
رژیم شرور و جنگ زیست آمریکا که از آغاز تاسیس تاکنون زمان‌های اندکی را بدون جنگ و شرارت نظامی سپری کرده و از شکست‌های اخیر در مواجهه با رزمندگان اسلام هم درس عبرت نگرفته و به تجاوزات…</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/449558" target="_blank">📅 06:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449557">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
سپاه: مخازن سوخت، سامانه‌های پاتریوت و FPS به طور کامل منهدم شدند
🔹
به استحضار مردم شریف ایران می‌رسانیم، رزمندگان پرافتخار نیروی هوافضای سپاه، در سومین مرحله از عملیات مقابله به‌مثل و پاسخ به تجاوزات رژیم مستکبر و متجاوز آمریکا، مخازن سوخت و سامانۀ پدافند هوایی پاتریوت در پایگاه آمریکایی در علی السالم کویت و همچنین یک سامانۀ راداری راهبردی FPS در پایگاه احمد الجابر را به‌طور کامل منهدم کردند.
🔹
عملیات مقابله به‌مثل فرزندان غیور شما ادامه دارد.
🔸
تنگۀ هرمز سرزمین ماست و اجازه نخواهیم داد یک ارتش یاغی و کودک‌کش از آن سوی دنیا به دخالت‌های غیرقانونی خود در آن ادامه دهد.
@Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/449557" target="_blank">📅 06:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449556">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
سپاه: مرکز فرماندهی و کنترل پهپادی ارتش آمریکا در بحرین درهم کوبیده شد
🔹
رژیم شرور و جنگ زیست آمریکا که از آغاز تاسیس تاکنون زمان‌های اندکی را بدون جنگ و شرارت نظامی سپری کرده و از شکست‌های اخیر در مواجهه با رزمندگان اسلام هم درس عبرت نگرفته و به تجاوزات خود ادامه می‌دهد.
🔹
در پاسخ به این شرارت‌ها، رزمندگان هوافضای سپاه در مرحله دوم عملیات مقابله به مثل خود مراکز مهم تعمیرات و نگهداری بالگردی، آشیانه هواپیمای جنگ الکترونیک پی ۸ و مرکز فرماندهی و کنترل پهپادی ارتش کودککش آمریکا در پایگاه آمریکا در شیخ عیسی بحرین را در هم کوبیدند.
🔹
عملیات مقابله به مثل ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/449556" target="_blank">📅 06:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449555">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a490ee038.mp4?token=fQPjq4Ch_vHuT6WLhmKfJprpd4HAX-Agc5TI5igUac6VxgXrrhbej3m6bpvMjuVGXSQXmhTWbOE2GeZzgEJ1oZCSKELKLlbSiHsQOeqlEZqRWdiVjvfuFkDkCmXnhBO_bfa9fMlCvGm8Ju43kHbu0BHO_3I_HtDZeCpmd5nlrpKSJoLc7Duktu5d6fr-SPPaY9-PnTt_qgdOJD7SgXoXux8iDlYbxnP3QqB4Yz_Ph9lghD8r_ZP2iXLS3wQ-5p6rvrCzkMnWO8AVLwq3X1xixAYCMz3yFb7b6sgfRtqAwCPYYl0FzZiiYIXenhcCL6BZ-4bTW0dHD_zvgG5MBCelcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a490ee038.mp4?token=fQPjq4Ch_vHuT6WLhmKfJprpd4HAX-Agc5TI5igUac6VxgXrrhbej3m6bpvMjuVGXSQXmhTWbOE2GeZzgEJ1oZCSKELKLlbSiHsQOeqlEZqRWdiVjvfuFkDkCmXnhBO_bfa9fMlCvGm8Ju43kHbu0BHO_3I_HtDZeCpmd5nlrpKSJoLc7Duktu5d6fr-SPPaY9-PnTt_qgdOJD7SgXoXux8iDlYbxnP3QqB4Yz_Ph9lghD8r_ZP2iXLS3wQ-5p6rvrCzkMnWO8AVLwq3X1xixAYCMz3yFb7b6sgfRtqAwCPYYl0FzZiiYIXenhcCL6BZ-4bTW0dHD_zvgG5MBCelcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بلند شدن ستون دود از پایگاه آمریکا در بحرین  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/449555" target="_blank">📅 05:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449554">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
سپاه: مخازن سوخت و زاغه مهمات پایگاه هوایی پرنس حسن در اردن به آتش کشیده شد
🔹
شب گذشته به‌دنبال عملیات نیروی دریایی سپاه در متوقف کردن دو کشتی متخلف که با خاموش کردن سامانه‌ها و حرکت در مسیر غیرقانونی، کشتیرانی در تنگۀ هرمز را به مخاطره انداخته بودند، ارتش کودک‌کش آمریکا که خود محرک این حرکات غیرقانونی و خطرناک بود، بار دیگر با تجاوز به پایگاه‌های ساحلی نیروهای مسلح جمهوری اسلامی ایران خوی وحشی‌گری خود را آشکار ساخت.
🔹
رزمندگان غیرتمند اسلام در اولین مرحله از پاسخ به این تجاوزات، چندین زاغۀ بزرگ موشکی و مخازن سوخت پایگاه هوایی پرنس حسن در اردن را با شلیک موشک و پهپاد به آتش کشیدند.
🔹
عملیات مقابله به‌مثل رزمندگان ادامه دارد و نتایج آن در اطلاعیه‌های بعدی به استحضار شما خواهد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/449554" target="_blank">📅 05:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449553">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
منابع خبری از وقوع انفجار‌هایی در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/449553" target="_blank">📅 05:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449552">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6ejX67NLin9Qwi14-ZhNCl3x4a0TJip7asxaVIwAfcZttPNv_c-FcABxfy0UE-zROQDcHGB1qNclkNmg84dsH205RafQvw_JzCCcXRhzSpCaR3vT9Rsa5UxJoH9YZHGJYg9IJPVKk4zdbwJojk5J9DG6E1GzqaRBOJCrKTIGN7ESubb3_LeblpwikR1F4JUq-pSRIMOV4pGrzPSxsZ0jI11UTVm77PTnLTihrFLhmK8mpca15vUcbJk4kksqgiOycS0n5kn9UTTQvloMKHwujNxpgvq3VJx7NBj_y9Yxno0gy1MJx2Kq-FNAmXxhzOgh0iICU0ujLYkD5FUP3SEoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلند شدن ستون دود از پایگاه آمریکا در بحرین
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/449552" target="_blank">📅 05:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449551">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
برخی منابع از حملۀ موشکی به بحرین و به صدا درآمدن آژیرهای هشدار خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/449551" target="_blank">📅 05:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449549">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
برخی منابع از شنیده‌شدن صدای انفجار در اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/449549" target="_blank">📅 04:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449548">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شهادت نگهبان یک ایستگاه پمپاژ آب در خوزستان
🔹
معاون استاندار خوزستان: در پی تهاجم بامداد دوشنبه دشمن آمریکایی، و اصابت یک پرتابه به ایستگاه پمپاژ آب کشاورزی در شهرستان ماهشهر، نگهبان این مجموعه به شهادت رسید و چهار نفر دیگر مجروح شدند.
🔹
وضعیت مجروحان توسط دستگاه‌های امدادی و درمانی در حال پیگیری است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/449548" target="_blank">📅 04:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449546">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OwH4JHlGjLSKdBgha7FcSWFsy_6b_7ttrThxfk2MjJdms0Q-SbulE-IDXLu9zYNa6ho0RNW58cC7SvaaUSlKtdJRZ35UeKypr51HFtPPGF6ThKd2HSuJgyQAuZA3N8AGW9cWEpbDPbDyBKySR5QfBzx8HNYCkmcubE3t9SZrKKl5vD-wZNMgw_eyMIW2_W2YIKYg_BVVdAbAtDHnElNrQ3j2IrIiZMqUX0lgkK0JDVodWY7JoVtFlP09VISMu--R9JL-L2cxtBWJJgi33u6SmjG-gWtH7TLwVSNI-i8iK4iMQ5uis376wpPvHh3rtLj0GqdP6-XtWmEOMswT4lHITw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dx7dx_gt_2SS8MhcTJw1HalUmtQi18-CSDqntKGW-29EVK-y-iE-TZkDpY5MZf3DefGJk68iMWJPfV7MZpswU0rqOuq1XGRSsopKrYtFxX9WvrDeJag2rHl2FR2K6dLV5Rx3Z6yLlLlr3k9lKrLAeqMD75dKpXCedFF3MpUO5QWWpg8g-PKh8_v7HGr2ZZZ-xTCnKaNM6aAvLpmWJgbMfJrzbSIArDml3qm-tJiHi1w2BRa8sJKNtWrlR1c_y4QyXXgMWNYnzeEFzAOn9HWo_g_6O_2-2TUteGS6xv4UIyIsg79ntGh_Teh6UXBNsyeguqrWyYj8BLK_PTksnlV1pQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزی که تنورهای قم لقمه‌های مادرانه می‌پخت
🔹
در یکی از خانه‌های قدیمی قم، زن‌های محله گرد تنور جمع شده بودند برای پخت لقمه‌هایی که قرار بود با عطر محبت مادرانه، راهی دست‌های عزاداران مراسم تشییع حضرت آقا شود.
🔹
می‌گفتند همه چیز از یک احساس دین شروع شده؛ احساس کرده‌یم وظیفه داریم تا جایی که می‌توانیم از زائران و عزاداران ایشان پذیرایی کنیم.
🔗
روایت کامل لقمه‌های مادرانۀ بانوان قمی برای عزاداران امام شهید را
اینجا
بخوانید.
@Farana</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/449546" target="_blank">📅 03:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449545">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3018e7f48d.mp4?token=VZJTPptFnJhbjK8orqD1haG-0nCv84q7URAk4tTFaXfsLSC-zMLOJX93HRg0TiUOwInb-yvxo7COu2ebq12c_tT9LGviFEOS2iPwuwPQrhsGRWbr8C1TU_fXvJFDHuRxFHCSvoSHcF56EXBrsdqLGbiHX3ERMnBFTpn2puJAOdwPMgk19DtW5lIY-YylQNJKfjJ8kVj2JLl9zqZCBl46ehQa2HHti6-XvOzujjgQ8D5VU5v-04J5ZBqnG_wmSaRy3rP5tHjomFG2ShYSNRofNgI2dFFV5bVv2iUsQQdbG_Kv1qKV99gZ_uNGULZk8JcR05FqCGC5lOlO3LrkZNYcTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3018e7f48d.mp4?token=VZJTPptFnJhbjK8orqD1haG-0nCv84q7URAk4tTFaXfsLSC-zMLOJX93HRg0TiUOwInb-yvxo7COu2ebq12c_tT9LGviFEOS2iPwuwPQrhsGRWbr8C1TU_fXvJFDHuRxFHCSvoSHcF56EXBrsdqLGbiHX3ERMnBFTpn2puJAOdwPMgk19DtW5lIY-YylQNJKfjJ8kVj2JLl9zqZCBl46ehQa2HHti6-XvOzujjgQ8D5VU5v-04J5ZBqnG_wmSaRy3rP5tHjomFG2ShYSNRofNgI2dFFV5bVv2iUsQQdbG_Kv1qKV99gZ_uNGULZk8JcR05FqCGC5lOlO3LrkZNYcTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دارالذکر در نیمه‌شب‌های حرم امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/449545" target="_blank">📅 03:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449544">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
استانداری هرمزگان: تاکنون اصابتی در بندر خمیر گزارش نشده و صداهای شنیده‌شدۀ احتمالی ممکن است از سمت دریا باشد.
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/449544" target="_blank">📅 02:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449543">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
نقاطی در آبادان و اطراف شادگان مورد اصابت پرتابۀ دشمن قرار گرفت
🔹
معاون استانداری خوزستان: در ساعت ۲ و ۲۰ دقیقۀ بامداد امروز نقاطی در شهرستان‌های آبادان و شادگان مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/449543" target="_blank">📅 02:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449542">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZB00Z3tXj0gYQfNtjdhGXk3MjW9B8JiuNn8NngOr9UdWDE9SSkSzLHqYvLDjHHO3oNpDKcabW8mef13msCTbaqtNtTKz9MyXxzhaN8xSj2Vu4X1jvGAcELNCN9LH1gfEth9jNejiKUKEMsZFwVLHMkVifejiVZMk7PDjwcxgGH2sJA8eP-TNnogVTVLG4420ssrz5qWkAWrTFN7bGymHIyLXkx1UxH1bN8RrfHy1xpmkDP7P2aBqN46EzYEgU6ZyCprWh14PgCCmUvI1n3OZRlbAtsjW7TV2a1fl9ktHqevnX3GXI6ASidLY-eiOShjvajh8jaeuT1Spo0pN8shfDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود اف‌بی‌آی به پروندۀ مرگ لیندسی گراهام
🔹
رئیس اف‌بی‌آی: درحال همکاری با مقامات محلی هستیم و تمام منابع لازم را در اختیار آن‌ها قرار داده‌ایم. @Farsna - Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/449542" target="_blank">📅 02:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449541">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
۴ نقطه در امیدیه و ماهشهر هدف پرتابه‌های دشمن قرار گرفت
🔹
معاون استانداری خوزستان: دقایقی پیش چهار نقطه در شهرستان‌های امیدیه و ماهشهر مورد اصابت پرتابه‌های دشمن قرار گرفت.
🔹
دستگاه‌های مربوطه در حال ارزیابی خسارات احتمالی این حادثه هستند و گزارش‌های تکمیلی در این زمینه متعاقباً اعلام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/449541" target="_blank">📅 02:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449540">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
سازمان تروریستی سنتکام از حمله به ایران خبر داد
🔹
سنتکام اعلام کرد به دستور ترامپ حملاتی را علیه ایران آغاز کرده تا توانایی ایران را در اعمال مدیریت بر تنگهٔ هرمز کاهش دهد‌. @Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/449540" target="_blank">📅 02:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449539">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
پرتابه‌های آمریکایی به نقاطی در ۳ شهر خوزستان اصابت کرد
🔹
معاون استانداری خوزستان: ساعت یک و ۳۵ دقیقه بامداد امروز دوشنبه، دو نقطه در اطراف اهواز مورد تهاجم پرتابه‌های دشمن آمریکایی واقع شد.
🔹
همچنین در ساعت یک و ۴۰ دقیقۀ نقاطی در شهرستان‌های بهبهان و دزفول مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.
🔹
در حال ارزیابی اماکن آسیب‌دیده هستیم و گزارش تکمیلی متعاقبا اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/449539" target="_blank">📅 02:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449538">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در خنداب
🔹
مردم خنداب از شنیده‌شدن صدای دو انفجار در این شهر خبر دادند.
🔹
معاون استانداری مرکزی در این‌رابطه گفت: صدای شنیده شده مربوط به پرتابه‌های دشمن به یک محدودۀ خارج از شهر خنداب بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/449538" target="_blank">📅 02:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449537">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رویترز: قیمت نفت در پی حملات میان آمریکا و ایران در خاورمیانه و کاهش عرضه از طریق تنگۀ هرمز، بیش از ۲ درصد افزایش یافت.
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/449537" target="_blank">📅 01:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449536">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
استانداری هرمزگان: در حملات جدید آمریکا به برخی نقاط استان، هنوز مصدوم غیرنظامی یا خسارات به زیرساخت‌های مسکونی و تجاری  گزارش نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/449536" target="_blank">📅 01:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449535">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6a4Js_Rd4VXNilaU_kj5c3YwFOrmBSur43oA_jSrul3Ji7AQAN-QA2ByYt0X27vjcsWg4CX7hB4ewUcVT3ARUpX5SIMbixLPpziKcXlzltdJJGHyW5GkVJ-41-qjoyudEtOKO1o2-Ui2mHfP4XsXeL82Cm6x-Rqk5d236mR8WFy-ZaQs7HB4t4gmd5qzUxmzMwWGoDptuufxQYU2n86RiNXWa-cYe8yHtD2wRFJegnSRwZfORquUqgK60l6B8co_TpEu6Jxx75AnD7mF6AWXKAohyIGvxeF1gx3XLn2KpW6pd5SA88IgRqKjdFrSpJ1kByj4fxl2A-WQrPXfbr6tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زینب سلیمانی خطاب به ترامپ: مرگ راحت برایتان آرزو خواهد شد
🔹
دختر شهید حاج‌قاسم سلیمانی خطاب به رئیس‌جمهور آمریکا نوشت: خواب راحت از چشمان‌تان رخت برمی‌بندد و مرگ راحت برای‌تان آرزو خواهد شد. این پیش‌بینی تحقق یک وعده صادق است؛ به اذن‌الله.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farsna/449535" target="_blank">📅 01:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449530">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DwmF9SykbYfyFz9fQRS3GFq771E9g5GtTMqJJITKgNA1dcoXeeg1Yjm9H4dO08w4s-uEfnwffTX1S_NJL6zdWrBlfUSDvvp_Ig8XpegLBSvd38uTVpuUlytgHUVbJC2Gc6wXCEBWG1TfAOjzYbGv8xKKMM2mS6UQF8dvRaJbtjncPy8X-YkHNucgud8ZevOVuFyhN1ufFP4EAl3Dsdj6z_7pKhzUKbNW61FblOa1apPRfsK8UysUoh9vtOrwrXArRy2Dz1uulZ_lcIsqZ2D5tWCkdaL5xRHrM-pK1hgSF1RYkC0MUAwto4ag-XfScuL_xJzPGODVbFPyjn1hIPS3Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1PaqKnNLKOVdVToaaxibuwTeVEtwSxortj6JGUErgW_t58IUS81jktnuGbyBZ8JuzYFsVq37YsdvI18Ig9gjItMlPVKVXKi6wQBoIGKZroPV2mI3Qpt8NbxClUfjaBr4ynwaT-Vb56_CyMVEN17GPfqQ2nfBj7y-277FD5XfsMeUnwJ8ZwcoP_y9HXN-meemwAR59NBC1NupaSZadQygEWYUSsNdHpXOKShiiIytZsGIatNUCQ9nOIQXNjvwDLcrQ4vA3HIHzjGCUT5F_A4X2dX6NOiqgA9Qb8hfm9w5QI1y6AUAIWvJtAZbm_01uFu5Zh3zuP09ZKIMJWiti2RIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V3LpLH8-hdpNY2f6fCfPFQ0zFgIKW9r5EIUr49YjScHCaMN6_rW-SPtNedi2pmpn0kLejvN4pP6DE2ckUKeWhqTtxvXVnUmd6TF4AgN18niY43v7uaHgx5M76kidr9aY2FppFSoLcolILpHcA0UzD7PhIGg-VwSDCEug9jviSkyKLBiEoQn7pdV38UkWD0TPLPA-njcDb4_ufjgGIjPIh1VEalglG8a9E-jbnLfVQn08dJ0ZadtXO36hizG5S70YGjF56fg4DkFRIjjybWR03RnuqvoMeWqU18XcXW13PDmNB0SliaqnPp4_rcvvK6_0Za4wywuaAk4k7Icn5AdTNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YTmPVfvqSHHbkZS8uHjDaW6XV9SuShn7zHIAsQdHyoRk-QtokYR42rGvvHJ8enstnW46G31aQ_p5MUtx4Wv-XM4G370lOHdXB1yUjFSVi6ID5WFqLGG_5n6Zde3kmY6gUSJ3hcWyUJVbYh9mEYv7be9hR8iIhLHJzUZFgQUUXnK4OWdK18V5Hy7VQNNrtEPK-cAg56tBzFInbTA3ahUDvCjg83GbqlzLl40tkj26D1EhGbr2ccHe8S1LEt80P9KwRQjd8kwZzdRX0cWoRH-zHEWsWzqNN-lW05LeV0hVsKJD7e7AF7GnSibszhBNIrYq257c_H9hFYq0GLyedyNVpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mIcskE_x00fnNgiymcNeZZa4zOWeaLgtJ5qMbr90tmPhY1hvlA5mgjCJYeTM0Et57X4ziWcB7XzjntzJB_hOWuW9jGKHKQSzSPFDDlnOE37i2kk2B6uHHagM1HArJCKnKlJbarqJQawlBoeClEM-EXdEiB7wf4mEfzNx7UL1NqoLrcZyrc6zPAS2qp96mbU0oLdRoKxSgwIkgkroZ7TAKhZs2Cg_yGotueRdeYxnoZC4CkLHki-wCSUXfTt6x1xYDYj8VMnBarhfNskuiu7MHjVi28PaWhGbKY4WPNTqZqUwpjX1H9vwQMCdtsXMkWCmzt55pBjiwsV-3iwx1BO7pA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۲۲ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/449530" target="_blank">📅 01:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449520">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dgE8wg8Xak3calZZSPHqd6zV3QqDGKcTqeMMhBaB1MEdNWLRTf2WOk-rkbVn_AXwU05gPiLbuuNcwI9V4F8kTYFDPrXUzVzt8bmvFDtX3Nd5B9qqg2M1gdFSP8dzBcEvxqUbEoKAyWB-Rmhp-pdxCMeoxzBk1k0fh7Eyt2VHGMkMfZohboQ_XnVC_YttvBK0_hoPpQC4J5CdBBR_mA1lEmfvuU3EZ9WsoQ50m19SK27mbWTbLAi4kFkrFvvQR2HVG6auSNZ4myDxtS8oSV6naYmnscLgOadk0Dc01pvcS-Wxon8yM-c9KTxZSyyNs1ZpSWYbxZzEhqu6G3Bmx8WfNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXB_v2wuUXIkvO7fUK_xTZnQ_HLMt3O527inuVr3Naa55dZrVCml5PAgjlr8TjiCBgSLQaFKW1EsDZ9kYe3Kx0vLNkAOSzxDyedZsvRIj7m6MUw8ev30tkAxRF5Ltb_trHcVONnGJB_iWZcyEz-MK8rYiBGjSlg3gqyk7TxKXMX8xnUwe_3ymC8fboYEXiMyjQFCryWo74SJ6KdMpU8NXErBh6T9p9CTDjAfzcnDQNDSfIqKumlMwFRXb_sXwILLacGfTsXVzK7DWAIAmIcAbTnH3AcoxXrD75Ql5O0Ycebj6KuGc5S6wUeYCxTM8ye27lEqag6qoiL1DSm4pz105Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S7aLzVwvRlHQV7ttV6vqeDL8cjh9A2LizfMUd3MEjGD6kqFxki4M2Xw6P4qVnl_5slS_QeiJcj7jhLVKEyJIrJRA9w7QkeM7DtUlWU3tDc7LDiajnMgcavXTkLudWFv5cvk-ioqdbJ2Mfx9v9EJLRL435YREwe63H1z1KGOCsDEnkrgxO-mOz_f3FQSl8mJJxJHXXYQa6nVfRbCVdSMRkdMtslkI5c6YpNL7d_nG3M-Ra2bR_Dqtl8KoSCeNzbbomFqGPfqFscS9Lq7qqZpK_lxSGZFw9e3dGbPBROn-CCNzgEUj8l83ywlyCcIP7BMBzDEF9cntDoUTeN2Arydl3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dfF2Byg7hrdM1iDT9XDJM88PcbmOkElGRUdjV1ZK_Sh0JV_FaGRxmy1vOqoLPNc1aGLKc8piUzOAr2ygPsFWxTz2IP1Xl769xNV30TE-Lu8zZdqFSRYMSfE5A1kVg7CEHI-jmlRrZ4JFy-g9Db-WUgEG-kTOch_V2milrr6T75xJhcy7a1OVw0cfjTqUFytH0sHbBibzwL2c0n51iyiIOMrRBWL5H2RNV0gaM150GxfOUHBxcCBXCPVUl5tNEJQLoHCMsWNLN65uEe-ofu5lN6b0WfzUvXvm-9kH0xh1jy2fv88_eHvT2C70e_A_iZTQ8wTE27Z9jmkrxKB1Zm83UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oFUVfp7qWegtc12It9MfoiEgJ_4ePDhKd_aQay2j86Js2W9lBZzL7lD7kKeWmZCp_z3XWVQ5yHUuslleRe06j8148B7g6YjkTgWgrEHTwagL08UHjEtyUh4gNwzo9Iv6BLRjDdWds4OMorHTmot77ajVA5UExBP-MYO_ETbvoITg4V57AHED0iCZwEZv-z0cGDID4i13M_XgZlXD857uns-N83xk3tsxp1SqsruFT1uwvF9XQHaXe8b_YaIZUBAaKyJ49GcEs4LCKUm3GZmHkGXUkZpy5CxRLtR_zP6N_G9KDJATPxUbKoCa-bwiiMegriUG6y0PFyX2f3uj_KItEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GU7oZd1Ha5ZZs1wPAH9dbK6DXNjWyrFSdef35c7FZpGxH3wSH7WZmtJQFzOFoN4-bkCUfz88aiy1j-e9lEfv1JB9G8A-TC0S_ylIPA_3MdxG0bSlz688LKSFrrHHBLLkyFtYNJ_q0qj_6F_Zcyj95TU4syir0s7Lv9MHtUtbN30JuPe0SoSp_0xP7aJuLAiOdFJPyDQkP0BhJMURxiobMzz4wvD_wWSgE0c8wXMiMdVlB6bn7J_iyalIF3pvWHpzrySwgfV_KGX37_5bO9-QbKfyKpehf97-Vdcq19lu-zXdXPtvhjuITEGmwRgIEKzRIvwlJynu6Kbakwo3-vH2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PDylfR6eMJu8F_Mg7Ox9Kl8ZjGVbUMoskQJtKhip72gvArFzjA0qX54idGqxn-UwrvDTzjB2qQ2Ctr3zJ1Ygdkto9KUrS38_k8upy-JfojmTuUDPD-ih3HBNK9Ixk1EW5vA902I_AE1fsI_kSomS2niV04nX5a0d2DQjI8-38evuq0uu1WR1A1AsUj0PBT-Xz2JQVWqzp8jqTP5zvK5hMjCl-xr9P15_nPqrZdW9nO-uocJHyvakOHVvi6oDxo551H3I97bAh-PcKD_-llfIXk5C5PuCXjNR9u3Z5ZtEO2SsXqeR-U_Nx8AeTlu9e97REXqymbwv5WdKSqsLWpy70Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/soneZqhvQeOn0_HnsW2lEgVeWyxzG5ZTNsv41PlpEJLfHgrYqPgGSKFl250ESgKBdAsfTSse7gp2GDRuz0YUkq_IvaRkIAEEFiuIA0uNpxF2QtMhJ9XPorDwopJC-VxPNQ9ozzGK6FNOpX0rTMCe1G9Kuh8o8ETubEX-bXBPxZ-XPzJgWNi-bcRIfLYR-_X5mzcN4VYdqF7Jm_kPqcT4_BxxRXvOK3RLKGSycFWEVZ4xGYoArpc5pPchtDhSgsYq3Jdictgv8cUQoVoJJA_LO_wbffzCuHQv2B4fC12b878Mysg4Ou0bq5XLhH2hLv83sOJV8eCLJAX0_4aEIjCZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6TwcSGrt1TpIilFyj80YhS0cQ_OADu2yebKnw2iHt474itNL8NmmnFIed7xcpn9pKjSJPS8ToHdgVQebK4lQqYiPQZFufATYiyqn6vF5Cx-qc0_EPuBgaiaOe0CTCzuOcxTxfoWpzclXuFiNFkcdx-bANngHdKp7eMr6z_vnOXSQjD2QQOGS4CaZTw-k17Ir3W0xU4QZniiaLRWpQWW27DWmwZmUs_mLoLdPtCgSnsyFGf7SfhRTn3cd71lPSGTtnu05F-QI1hraZkD_yJDbIhFRK9wtB4lJhTxRk_TNF3XNkVJfD7SOyXpD33HMbl8PiBDeo_RIXZ7lE0TbhlLfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZUPxD1wwB5cXMUKOKgO-F0Q1AAzfDk3KyR10OskvZ5hKmoqCYdvaMkFU5WXx9ASh93OCu7Zzu-MgMRw5gCxLed7wNvHZDVsWSny96Zo7pM-ftdtGCOhomgGKoDJ5mpKb7bqY3OvAyAAXfI6A2JQlKQwMgAlkjMJBlmEWawbOpsQg2XUrLCa3DgD15FdLEp1cp0naiXo_WirBODG7_3nhCYAVvGPlNLQ4XpR4CYQCrwo5GSz_baYVAFs5BVspOSCVd0Jdrhi5uoShMuPBlXCRa7-eB1ykMVHQHF9byowbUokw-Qb3Ab0qeTJDtaq0TQWPXtrOZ-zxIHpOhsRCu6QvKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/449520" target="_blank">📅 01:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449519">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
شنیده شدن صدای انفجار در جاسک و جنوب جزیرۀ قشم
🔹
منابع محلی صدای چند انفجار در جاسک، و هم در جنوب جزیره قشم را گزارش کردند.
🔹
هنوز محل دقیق این انفجارها مشخص نیست.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/449519" target="_blank">📅 01:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449518">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxA7RG82RBiua_alZRx5J5dcD0mbU6XqTIeBDlSP2glKibtdsgu0AbqWcwl4eRmknkdkVrNZz_Y79syr59f_zFMuMCmnynFab4WofNpLdDK7C3cRZ-GDEMYSSk-sGZOcZ9VoCPyZEjp4GQMOq5lz2YGmNVLSVINyqPZOHmJckSg8XwcyQ-ZnQLa-wi7dFRG3Qx-3dQrTqscRe95MYBtOsjqlunWpILoEIdm0URC01mtIze_jwYvXVn3IMrKREJCErZEMky-j0WWj9tSuBlNqcJNovX7ZxrKxoQWyuwWph3Cr_fYhGGFvjZFIQ8Zl-cGgL5GAe3XwId6UJzJ4WwmPuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وقوع چندین انفجار در سیریک و بندرعباس
🔹
حوالی ۱۲:۳۰ امشب صدای بیش از ۱۰ انفجار در بندرعباس و سیریک شنیده شد.
🔹
هنوز محل دقیق این انفجارها مشخص نیست.
🔹
پیگیری‌های خبرنگار فارس برای مشخص شدن جزییات این انفجارها ادامه دارد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/449518" target="_blank">📅 00:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449517">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
وقوع چندین انفجار در سیریک و بندرعباس
🔹
حوالی ۱۲:۳۰ امشب صدای بیش از ۱۰ انفجار در بندرعباس و سیریک شنیده شد.
🔹
هنوز محل دقیق این انفجارها مشخص نیست.
🔹
پیگیری‌های خبرنگار فارس برای مشخص شدن جزییات این انفجارها ادامه دارد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/449517" target="_blank">📅 00:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449516">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czND_qa_2Gky_3irLAz6p8zRqg6uPpu-UxWw19BXDizyjQ9blWtG556wcPWUQe0LN-4RUEG2yAZYj5FRwxUvdBpNOKH4WJlwusA8X-cfPzcEAs4Exe9hVo1jzL0cxgAjWiolVoFKGyT3viYZpifo0PT9ebTGIbn5nCLmRu61EdYnqjz94N7uoW87l_nOYa1O3I9aN1Hz5F6X0vlNDyqgZidWjJgDnaeBpko8c7gt61MTD-1TxHW3zis0hlEKMZTOz4858pqlHZ3wgdm40gZekf7KDbqaaO1pGJRR-UhdUqNK9L1OQbEapk-yPqT2SU8Q3meJy-DcLOG_J7cbaFjacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیۀ وزارت امور خارجه دربارۀ تجاوز نظامی آمریکا علیه ایران
🔹
در حالی که تنها ۲۵ روز از امضای تفاهم خاتمۀ جنگ گذشته است، رژیم آمریکا تقریبا همۀ اجزای آن توافق را آشکارا نقض کرده و با حمله به زیرساخت‌های حمل و نقل ایران، قایق‌های ماهیگیری و لنج‌های حمل‌بار، تاسیسات و ساختمان‌های هواشناسی، مرتکب شنیع‌ترین جنایات جنگی شده است.
🔹
رژیم آمریکا همچنین با مداخلۀ آشکار در فرآیند اجرای ترتیبات لازم در تنگه هرمز توسط ایران، موجب بازگشت ناامنی در تنگه هرمز و اخلال در کشتیرانی تجاری بین‌المللی گردیده است.
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/449516" target="_blank">📅 00:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449515">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN4GFJxO-4t06rKPV77SzfgGFDuGrv3CFuonEjctSDCDvN3UswFdQr7na0IiK46KmnBx_5FBeFT4PyI1xOHWsB4yLcEkBRF2Pb2BZ8IloRhG_Bhe8Vi_DWjL71s9eRGw4bcKCKEuLUGIz35pk-miurs5x-1-ngY9UFRpCCUh8iVg99vy2D1B0RZ07Tit0s9Kq3Na8wecUS6k8Ol1r0PpsXZe_LocSDrFRyjZ2KmT3wht0dmyblgnqTAhyD94JWroNH1kgqFg94LzjvTK5DZc01xJ_gKqDIrTxCitv45Ex16gMx8L--cRd60SOe0iq22aSDHn1Gxnw4rntY4fuSemqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سپاه: مراکز پشتیبانی لجستیکی ناوها و سکوهای سوخت‌گیری ناوهای هواپیمابر آمریکا در بندر دُقم عمان، با یک حملۀ سنگین و غافلگیرانه درهم کوبیده شد. @Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/449515" target="_blank">📅 00:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449514">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmffvUoYp3wlKWNUOUGxo_olfWRCrw6H5FY_eYIO6wxjBPPAn_2EGLEzjZ8NlH34N9fXJ--irx6M-UNke84CUcLD2p5in30ROAOh-Kf2k0fUovcEeIhI_gQ3mvnCoEUKjnLoK6J1jAXzxRJEVeZieu47vxDVjRd_OCxg3ICe2z0_Qnw1FkJLmJdITeZUPTaV40jIIFi-sCRwnM4ZgHaQ7_QAOPBOG1caKh9Nnv5mqaRY37zVyjLaQax6pt9bbSy5N-Ce_6dCxd9YCJXqRf73ErHzkKmBbvLDNa40yAAntPKuplPmmRtD05C26eH6kOuYhgBA-SjXnZy4d6p9ME9Qxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۲۱۴ دستگاه ماینر از یک واحد صنعتی در مرودشت فارس
🔹
شرکت برق شیراز: پس از اعلام گزارش‌های مردمی ۲۱۴ دستگاه ماینر غیرمجاز در شهرستان مرودشت در یک مکان صنعتی شناسایی و کشف شد.
@Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/449514" target="_blank">📅 00:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449513">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سخنگوی وزارت خارجه: شماتت کردن ایران به‌خاطر دفاع از خود در برابر تجاوز، غیرمسئولانه و ناروا است
🔹
این وضعیت، «برخورد نظامی» نيست بلکه ادامه تجاوز آشکار نظامی است که از ۲۸ فوریه توسط آمریکا و رژیم صهیونیستی علیه ایران آغاز گردید.
🔹
ایران به جایی حمله نکرده است؛ ضربات ایران علیه پایگاه‌ها و دارایی‌های نظامی متعلق به آمریکا، مستقر در کرانه جنوبی خلیج فارس، اعمال حق ذاتی دفاع مشروع طبق حقوق بین‌الملل است.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/449513" target="_blank">📅 00:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449512">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c6a1f590f.mp4?token=E0w5BLSfYSw63l_mbQmJCmM11Pev5Jx0PFSq1pOoGJhqe-TdROETwFruGiJptd1omN9m2L1fHI3pDdSggWM7-aC0WiGAtBzfSymqXipTQZBOknbqLkegWMApGsGZuDoLvFI4t16w5_VLPmcDaUJmWxeS6MtPglQ_KyRh8NBIIV6pPP9hd_FBIhJR2_7aKUcYKdkyE0LnECPqrpf52g6Vc4B_CZtMu0D_FCpjcuA5RgN6Lvb61ugenlMJ1EL9ZuKc2WWFVQJdX2uxlC1XddBspMdmvIB1BrvqTD783QxgzfiZs272ePof8bjx5cQ_ZTKxGKKyGD3bK6CdhD_euLH2SrId3QeTzXiB5NGalXkgnjwq-iHeU1q9rozxayimX8q0j2FZ767zg49ZmfXSK8FSpY8w8r9QHN3loFrBTi0GwVpYsZN6Yh-8cz03WeT9NFzQ0A210NwvXS__Eau1dY5SIRWrQDNAemRpeY5giWkB4WPCQaUSMM7speSr0842Ys7N64Sfk8R6jZOoIEeaXNmjzAm8qpHIrlooWz063t7fK_qaAu0SVhZyqEdICY6X4BFqtthLn_N8LVkXk97RgJLiKnUF_4-idnqjFtrmFQJ3xHVi0WSwrVxFCK7jtwbj54aEiPUPz7-VXZsXCTiumX0tHO0lsMcGf5LLjp5pCM4jLPM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c6a1f590f.mp4?token=E0w5BLSfYSw63l_mbQmJCmM11Pev5Jx0PFSq1pOoGJhqe-TdROETwFruGiJptd1omN9m2L1fHI3pDdSggWM7-aC0WiGAtBzfSymqXipTQZBOknbqLkegWMApGsGZuDoLvFI4t16w5_VLPmcDaUJmWxeS6MtPglQ_KyRh8NBIIV6pPP9hd_FBIhJR2_7aKUcYKdkyE0LnECPqrpf52g6Vc4B_CZtMu0D_FCpjcuA5RgN6Lvb61ugenlMJ1EL9ZuKc2WWFVQJdX2uxlC1XddBspMdmvIB1BrvqTD783QxgzfiZs272ePof8bjx5cQ_ZTKxGKKyGD3bK6CdhD_euLH2SrId3QeTzXiB5NGalXkgnjwq-iHeU1q9rozxayimX8q0j2FZ767zg49ZmfXSK8FSpY8w8r9QHN3loFrBTi0GwVpYsZN6Yh-8cz03WeT9NFzQ0A210NwvXS__Eau1dY5SIRWrQDNAemRpeY5giWkB4WPCQaUSMM7speSr0842Ys7N64Sfk8R6jZOoIEeaXNmjzAm8qpHIrlooWz063t7fK_qaAu0SVhZyqEdICY6X4BFqtthLn_N8LVkXk97RgJLiKnUF_4-idnqjFtrmFQJ3xHVi0WSwrVxFCK7jtwbj54aEiPUPz7-VXZsXCTiumX0tHO0lsMcGf5LLjp5pCM4jLPM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: اگر دشمن زیاد فشار بیاورد نمی‌تواند مثل حادثۀ صلح امام حسن(ع) را تحمیل کند؛ بلکه اینجا حادثۀ کربلا اتفاق خواهد افتاد. ۱۳۷۹/۰۲/۰۱
◾️
انتشار برای نخستین‌بار
@Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/449512" target="_blank">📅 00:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449511">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/461d5b5eb1.mp4?token=GchXPPJDjXTuQGMU8jRbYTJH-wG6VfO4wEZO5EwoMTLBPHpxsAvulQ5-lA96faMKg6hjthpIqmVDf1NM-_oV6ztCRNCYemglF263R4aXZ4-oxeB1GJ0_KljyAw5l54tbEDz0mt3a9hKESAIpc2GsmHhOHKVW6PTNpnzieUvADPQRIj16lv1_f53DkBax8f0O1AcZa6fZz3hgWsowAQCdsqbeSIWSnSrhLOHoIbBIefwJv4HWCzpFfeVotqZyVhVcE76FoAqMOcnoQgv0CYbZ_ZtEF8HHZfWc5nKn5M5G3zEQ1wioqSAE4avlHifENnp3h9yf9fw7V2Lxz7guB2TMBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/461d5b5eb1.mp4?token=GchXPPJDjXTuQGMU8jRbYTJH-wG6VfO4wEZO5EwoMTLBPHpxsAvulQ5-lA96faMKg6hjthpIqmVDf1NM-_oV6ztCRNCYemglF263R4aXZ4-oxeB1GJ0_KljyAw5l54tbEDz0mt3a9hKESAIpc2GsmHhOHKVW6PTNpnzieUvADPQRIj16lv1_f53DkBax8f0O1AcZa6fZz3hgWsowAQCdsqbeSIWSnSrhLOHoIbBIefwJv4HWCzpFfeVotqZyVhVcE76FoAqMOcnoQgv0CYbZ_ZtEF8HHZfWc5nKn5M5G3zEQ1wioqSAE4avlHifENnp3h9yf9fw7V2Lxz7guB2TMBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای تجمع امشب دامغانی‌ها با پرچم‌های سرخ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/449511" target="_blank">📅 23:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449510">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWes55tpIxp0NBKUo1g96m5nzw5b5CyN3IMGFgHIflPygL-_nUtwl6bnNRRhLeX3L58jAFavcGBXZQLJCt47z1oscAyoa3Bbic4nsKQ4OPdN0qobC5Q-Xs5iMbR3o13lZoJvZPyYMW9xAVZAA7kyUsH3-Hkibqsmdovs4TnyhR70_gh_-4XC4oI3KPW6B2bsRQ5dQPZ20WKV52yTK3VcgD3zRI5sBJLF2dO8mXZ_gc9b3AfNA3VfJmgvF22snBKFnriJNb7kgPFLw64GRcFYLHC04QSWmH_4TJjwyWSW4_SiJY611uzKssrf0mGGXkMYwuuJY6gPITL1hcS8doFFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگنده‌ای با ۱۰ موشک
🔹
تصاویر تازه منتشرشده از جنگنده جی-۱۶ نیروی هوایی چین، این جنگنده را در یکی از سنگین‌ترین آرایش‌های تسلیحاتی دیده‌شده نشان می‌دهد؛ وضعیتی که کارشناسان آن را «حالت هیولا» نامیده‌اند و نشان‌دهنده تمرکز پکن بر افزایش قدرت آتش در نبردهای هوایی است.
🔹
در این آرایش، جی-۱۶ با ۸ فروند موشک هوا‌به‌هوای دوربرد پی‌ال-۱۵ و ۲ موشک کوتاه‌برد پی‌ال-۱۰ مجهز شده است.
🔹
این نوع تسلیح سنگین البته یک انتخاب تاکتیکی دارد؛ افزایش تعداد موشک‌ها باعث کاهش چابکی و افزایش وزن جنگنده می‌شود.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/449510" target="_blank">📅 23:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449509">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/465bd37a8b.mp4?token=YVxgFjKzsq3mAbZbfYbf3ylDuWkFEVwfXftABv_gyv0Vxl4A7YDGVmkYGoFeAKM46btl-QuGcFq44caw2zGQnW08i1j35t8FSU4mQ90irou3PgZe6MVn5PB1Gg5fVNx30DZXsn4UGUFXB3HN_6kVXXYf_lU1uVILzXBcdKbCY_qdQaFimnGVou3FR0WN1s-vv_Kr2kvdu6dbT15Qkx1WiRs5fMhCppP_E3cY3Hg_NvG2JnehJsa98Laacz_gR5dmKJ2kp9_AluOrcTcVVjGcYtFGvw9fNOxsRgvOBPh9PoeANVFNgl5ZeD084DV56aiTxS4TIGzyCZDkkiflgyH5CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/465bd37a8b.mp4?token=YVxgFjKzsq3mAbZbfYbf3ylDuWkFEVwfXftABv_gyv0Vxl4A7YDGVmkYGoFeAKM46btl-QuGcFq44caw2zGQnW08i1j35t8FSU4mQ90irou3PgZe6MVn5PB1Gg5fVNx30DZXsn4UGUFXB3HN_6kVXXYf_lU1uVILzXBcdKbCY_qdQaFimnGVou3FR0WN1s-vv_Kr2kvdu6dbT15Qkx1WiRs5fMhCppP_E3cY3Hg_NvG2JnehJsa98Laacz_gR5dmKJ2kp9_AluOrcTcVVjGcYtFGvw9fNOxsRgvOBPh9PoeANVFNgl5ZeD084DV56aiTxS4TIGzyCZDkkiflgyH5CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین فریاد خون‌خواهی در نیشابور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/449509" target="_blank">📅 23:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449508">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8e2301a85.mp4?token=D9LQI8CibQnWkIl_xgVeMY2vA5mpP50GjrY20hIi5oop3GQblTGfC6WEQNs3pn2d1FdL4SKUtg0vmC22_-iNQuEXEkv0Occ-sKZDEXfbLfHPWWubVuh3IvD2HVRDZmanDzN9NSe1JYcjsbaFplA9-LtoNv-_8eeN_a06ahKSo_-vwVKRiLAEPJbQrHY0pm3UYR7nz9dVr93UHdxfGw_UOpsEyC6v3cjduim2RQ6VDQ2jAhplxgO05tmRmxk2ybXNXnLSdPaaZNFp5hNWSkylp70r1bMBOtYHS8wL7pH0LCSblfdwjH-NKO6duVn9mpLWkmzE-7Z9peZ0v17c5TQf8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8e2301a85.mp4?token=D9LQI8CibQnWkIl_xgVeMY2vA5mpP50GjrY20hIi5oop3GQblTGfC6WEQNs3pn2d1FdL4SKUtg0vmC22_-iNQuEXEkv0Occ-sKZDEXfbLfHPWWubVuh3IvD2HVRDZmanDzN9NSe1JYcjsbaFplA9-LtoNv-_8eeN_a06ahKSo_-vwVKRiLAEPJbQrHY0pm3UYR7nz9dVr93UHdxfGw_UOpsEyC6v3cjduim2RQ6VDQ2jAhplxgO05tmRmxk2ybXNXnLSdPaaZNFp5hNWSkylp70r1bMBOtYHS8wL7pH0LCSblfdwjH-NKO6duVn9mpLWkmzE-7Z9peZ0v17c5TQf8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده نیروی دریایی سپاه: آمریکایی‌ها در خلیج فارس بهترین ابزارها را دارند، ناو و جنگنده دارند ولی یک چیزی ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/449508" target="_blank">📅 23:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449507">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce8403c6f.mp4?token=LQQRYGTJSa0NirfYNrHFEVqmfSBgXnGdc9fgvaaoEXX_mE_hCo14a74l4uezXxcW8c3FEUkDsIA1xrSe1TedESkd-QixLmE9irj9J2lqSWJ59XcgblBBsqtOY_3Kv0y-HdpPxEYVv9HibutGQcXLtUtVpRC4_lQKMvhQozSWh47CT7tDqW0BcrBULQ1_okNYSTZT9Vf0hRAARlSffQRwOw-cGb5MWo--icUhKEFavDvRF3bokmGadkQnhI84_rov0YlhaFkiT8dyzp6zB7nJNCLOcqQLa0sBOLYT2KY7aPG0OmeEiCM5uOScDX4NWJpQJz1fn5Egoc38h4L3WVA3fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce8403c6f.mp4?token=LQQRYGTJSa0NirfYNrHFEVqmfSBgXnGdc9fgvaaoEXX_mE_hCo14a74l4uezXxcW8c3FEUkDsIA1xrSe1TedESkd-QixLmE9irj9J2lqSWJ59XcgblBBsqtOY_3Kv0y-HdpPxEYVv9HibutGQcXLtUtVpRC4_lQKMvhQozSWh47CT7tDqW0BcrBULQ1_okNYSTZT9Vf0hRAARlSffQRwOw-cGb5MWo--icUhKEFavDvRF3bokmGadkQnhI84_rov0YlhaFkiT8dyzp6zB7nJNCLOcqQLa0sBOLYT2KY7aPG0OmeEiCM5uOScDX4NWJpQJz1fn5Egoc38h4L3WVA3fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراسم تکیه‌خوانی و علم‌کشی در تکیه درکه تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/449507" target="_blank">📅 23:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449506">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5ba4fa4e0.mp4?token=otSQ2wESd0dVmzbpgcs1Yu2LRstlB4yWmKi6VsXCmioRwLY8hWRr9L-w4Llv6AkDhXbH-lLz2wOtMW2Ou8MD-ogFQcqlYKrU1UMd9xFPhsNlGoStyR2ArAoXi1n3ZpRbZ4EVNLoj6fsvx_Sji41_Ws2ihZaV6hNniSFMtYOYPpfEx-Ul_NjW88u0vrMts36xUiKu1VTSONnv1Xjj9mIPaJoFcrgpY0ffYZ9MB-r-PsmE7auhiYR6tyf_bBNCWn7MqyhLuEmQIVpaRjq3eanb0LZYFBfXb2QDGkjP5vhuqYjb8JT_dQzQUaPd8rcAsuz-Zo3mkxHO1oIn8YAL--7FAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5ba4fa4e0.mp4?token=otSQ2wESd0dVmzbpgcs1Yu2LRstlB4yWmKi6VsXCmioRwLY8hWRr9L-w4Llv6AkDhXbH-lLz2wOtMW2Ou8MD-ogFQcqlYKrU1UMd9xFPhsNlGoStyR2ArAoXi1n3ZpRbZ4EVNLoj6fsvx_Sji41_Ws2ihZaV6hNniSFMtYOYPpfEx-Ul_NjW88u0vrMts36xUiKu1VTSONnv1Xjj9mIPaJoFcrgpY0ffYZ9MB-r-PsmE7auhiYR6tyf_bBNCWn7MqyhLuEmQIVpaRjq3eanb0LZYFBfXb2QDGkjP5vhuqYjb8JT_dQzQUaPd8rcAsuz-Zo3mkxHO1oIn8YAL--7FAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: دربارۀ تنگه هرمز از من سوال نکنید
🔹
مجری: ایران اعلام کرده که تنگه هرمز را بسته است؛ آیا این درست است، آقای رئیس‌جمهور؟
🔹
ترامپ: از نظر ما، این تنگه باز است؛ درباره این موضوع سوال نکنید. درباره دلیلی که از من خواستید صحبت کنم، صحبت کنید.
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/449506" target="_blank">📅 23:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449505">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تکذیب حمله به نیروگاه اتمی و انتشار مواد رادیواکتیو در بوشهر
🔹
عصر امروز خبری مبنی بر حمله آمریکا به سایت پسماند نیروگاه اتمی بوشهر و انتشار مواد رادیواکتیو در فضای مجازی پخش شد.
🔸
معاون سیاسی و امنیتی استانداری بوشهر در گفت‌وگو با خبرنگار فارس ضمن تکذیب…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/449505" target="_blank">📅 23:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449500">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VkUiRxo2ODZAsKOkwqIZ8TcON0iHTts6Iu5Cz6nFBLI1orpa4dFzkTJJwrR8xayHbSRGHrOSRFOfD3VGRZ1VUhG9-uRG4CGmPLJvJI5IpGxyciVMEsmNywUc7ohxfVSAc8FBqVlrhJCOcapYrKHkYTObwQtlwuHK6NzODePyZ8fpmOnKSYBgl1XiVNbiO4HVrbe5CKAW_imLtqkBw3vNjbXEIMR5XMN-o58Ao9MpQaOfst6pXfoG6XPLLejBON1iGwpSOpGoHuDclwFe2OXraTiVE05Gy_6NSaST6UlBbxrHpuWG__SZDOVC7y6I5gD_7cVTdlh_9igcN-R8YdIhSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O6Zf5CW55BH1zSm_zNsFP4pD2Wzry6l3SFA9gsiySmSEllV5f_PjCvsaB_zXoAwdFAPpsvoUnOw7o_G5o08Pu8Ex80ToZWFi9rIyqgRka4R3O7l3m0Tuh7QrRYuyBtbpZ4QIfA1pufIJtQoAt0f1lQ03qda_N37As4WsdEB1s2FU71EGxHYkN8bRjSDJGPJ5jGpjf6SBpKdXURGx9wCRxYaIcekzcv_rKMUHd-_6RylSNyJBUX9GLNmbqWw2bFfiG7QzGP1QLQqoVJf-pjNsa2GZk_J5s2zGKg8yrd_TteZLoOpqC6ZozDpfSd6DsGxmrV2lHUAx0WNMohAnTebeQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAnv4P1HMKH_ylyviGbLSSiBlYDpyAtSYrjAkX__b2bUgqnjqMJlFeDmMPv8720t8Cwq7zNBScOE6KYt5xvC9b5aBV3GOsxmlGw7-sz2aaqwIJfkr1jifODgkIhzLLXSaX_C3V646aY-NeOM96t0ItHlozvplQGUu782GOit6KkwiltRgxp3pjV-ojHGuaulbWhyE-WVz6jNtHDin5RMD5vKi_sPAd3_K2upTasQSTXqBVOVL5cYdo-SlYAsXGYIgPXdNnVxNRNpJTJQBmlhFHiiyfCm-vf0y1SzPhOfsVmRPZ8kJX-CxxeRtb3djb_mPZltrxA25IVgW2Ahc9g2XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GfBz8PdAsF5sFdKyCppYeEEIC8FNxsNIOKZ2JhH2iofdVvArjSq7nUntXUai7WLugKSP_GUE-syYLSJBVsiy64vRTQBoptBCA93GWzog0HNrDJF4y51Obfa1fCouAP1H51t-cZN8G6WIYt8H9dR1kBKK4swU0Uw4wbvgupjlE9cjS86JhnCIEo9I6AFDjymDi5354bTtOArBOzCXOx0hiZqF91rLloeYbwuyBEwGo7-glza8k1Cu3pBqa2kogcnMzByfFX6i5O4kpXtSwBlhadZ7E4FHnHLjupj7RxZg8otUNn--4yFetM5IxN1aMKX5l9pR1W0_71hvc4jVXcOokA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ddYUM382ut9QHFJCL2C2p0lcg6fRuDL2bwLZ2Dp3kPVxzShgU-fal7ZcmaPPhuISqVTpzTbagOjlV6LAJf-tsREO8YSsMs4HGtSHOGpzBcR7nG-Pq6wAro20WnekUViyr1To83FeJkLyPD7KC1LgDMzvuHowQlGxWI1k8nqbKqeq4QCh0GeubiqddFF3smBd7AcncnBdsy5CnrmoHfbJrm19CXuEXaJK1_p3d1DmBqOwZJWNWDYfNVG8uQirUHpAN25MZoGiB11MmFT4Bj6zkgUExE8jDiAl6u0N52t5xylfflp4aUHR7u_yuH83VO-bTDkcY7l8U9j3xVsrivus7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
چرا تنگه هرمز را بستیم؟
🔹
روایت درگیری‌های چند شب گذشته در جنوب کشور و تلاش ناکام آمریکا و برخی کشورهای حوزۀ خلیج‌فارس برای دورزدن «ترتیبات ایرانی در تنگه هرمز» که موجب بسته‌شدن این تنگه راهبردی شد.
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/449500" target="_blank">📅 23:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449499">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ef22eb00.mp4?token=kKz1SMJxX-7Doq__tDwLa-s2oNApoCPfoPmqlZ2zg6twus0rk9PGr3cVqtq-Qo_YNLZcAbU7Dim7wdVD__o8U-hsiW7Htu_XXcJ2u2MN7KB_JZV0lPBBmaXC-ExOf9so2Z3fZ3CXkU-j_DI6QYBzznDAxMZRkOZ25isxnG_pgiQPRkVzpNC8x-C9b6KZy-v_jtb86hRjaDIzu6h12VjCMYHyKrT75FN-mE968Y5sliSq2jPMYYqVouCmqAShLOqu0HvOnmsdopUQJRbGYfPz3gw3wO-FrdozsGqVwJRkMmS-E_A96zCSmlW65AF1DiRlNiaM8VocuiMvptZgA_KbsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ef22eb00.mp4?token=kKz1SMJxX-7Doq__tDwLa-s2oNApoCPfoPmqlZ2zg6twus0rk9PGr3cVqtq-Qo_YNLZcAbU7Dim7wdVD__o8U-hsiW7Htu_XXcJ2u2MN7KB_JZV0lPBBmaXC-ExOf9so2Z3fZ3CXkU-j_DI6QYBzznDAxMZRkOZ25isxnG_pgiQPRkVzpNC8x-C9b6KZy-v_jtb86hRjaDIzu6h12VjCMYHyKrT75FN-mE968Y5sliSq2jPMYYqVouCmqAShLOqu0HvOnmsdopUQJRbGYfPz3gw3wO-FrdozsGqVwJRkMmS-E_A96zCSmlW65AF1DiRlNiaM8VocuiMvptZgA_KbsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لاریجانی: باج‌دادن به آمریکا سایهٔ جنگ را دور نمی‌کند؛ چیزی که جنگ را دور می‌کند آمادگی کامل و چند ساله برای دفاع است
🔹
آمادگی فقط نظامی نیست؛ باید دولت خودش را با اقتصاد جنگی هماهنگ کند. باید آمریکا ببیند که ما برای جنگ ۳-۴ ساله آماده‌ایم. @Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/449499" target="_blank">📅 22:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449498">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e2ddf3dc.mp4?token=VPc4cumYwoXInASoquxtJNCDkFVqy2nQBIsGQoz07FCvy077EhiAaIIqvEDh2hRNZb6f3lU7yciSYsvzD5LmMtXFN_JHskK8mToXnkbwUGh2d50wk7MPfF3vv9_Pt0KjTiVliv9OG8OAesxPys5xjx_lb-CVUBOteMRrJw9ym2nj9kgZ2iFZb1_mDnSMqMbP1w717ylbPpJQBqlly__nun2A1nRMc6WVZgl2c3tra40ONOHyuokVuk_CtGdgBVFWnpNKRzk7Q2Nb22xmjIR65JyLGnCoHvgVpDeK6XoapTm3l7YLVn6m5GNDMmLxIyRbRY3PSunbxzh50xlAGzIulA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e2ddf3dc.mp4?token=VPc4cumYwoXInASoquxtJNCDkFVqy2nQBIsGQoz07FCvy077EhiAaIIqvEDh2hRNZb6f3lU7yciSYsvzD5LmMtXFN_JHskK8mToXnkbwUGh2d50wk7MPfF3vv9_Pt0KjTiVliv9OG8OAesxPys5xjx_lb-CVUBOteMRrJw9ym2nj9kgZ2iFZb1_mDnSMqMbP1w717ylbPpJQBqlly__nun2A1nRMc6WVZgl2c3tra40ONOHyuokVuk_CtGdgBVFWnpNKRzk7Q2Nb22xmjIR65JyLGnCoHvgVpDeK6XoapTm3l7YLVn6m5GNDMmLxIyRbRY3PSunbxzh50xlAGzIulA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم گرگان: خون‌خواه اوییم، تا صبح محشر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/449498" target="_blank">📅 22:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449497">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g20pRgD_B_rpZvdof8ibEbf0r8F_EjaWoOq4TPctD5Mb-atqHZ6U3GITTAr4eYW1DvWoVBSc7ylW5DJ0PggI3WDljJNmF6Rm4q_Ty9YfIQCAsiReDs6Pbc8N_q1P_maS2PERjFiDYJjrMSjW5OVX8EXHff1gDCI5oIjPAtuPXBfKvyIIY7qm9UyxtXVz9454u3PyZRLQT42shOJUDRxmzTSsJPNFH7cjNI8We8CBYqVfsPI4-O6PN2SKPMLAJrCdlGu9cVrGW1dvIa1iLxdlKB7iXeinVSbtikwW5BzLdIjBfSLOcT8Aht99iwLHoy2fQeVbrNMETHipV7dmASTeoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
مقاومت اسلامی عراق با صدور بیانیه‌ای اعزام هیئتی از دولت عراق برای سفر به آمریکا را به‌شدت محکوم کرد
🔹
مقاومت اسلامی عراق در بیانیۀ خود همچنین به دولت جدید عراق دربارۀ عمل به وعده‌های خود دربارۀ خروج نیروهای آمریکایی عراق و حفظ استقلال اقتصادی عراق از آمریکا هشدار داده است.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/449497" target="_blank">📅 22:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449492">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5bgPPtAFzOvLB7DyxkCrWnHEmV-G4HlIVKBTaftJZbA6dz7n2jdoNnMGV-6LSJXvsvaf3AYXn7yk9_oh9FyllcH5LGjVQnWqxnb7VUNPdtA_rc8xRJAaTmccvZ3VdxBldeYmkfbd6adRPb7nkS9f_2AX0BeMHhto3kRNtuZ724uEgrxi860Wlw2Q8vGDrNZIVwzvc83Og6S_R0jhpBSrBz42SD_0Owi4wXifx-mmY9Gh2p39tet8XOPVYz9BEg8aoPhoSKGD56ym1XvCe7JIkb2xh16i_GrOL1omP1ABaMUCueFhsjOW4WMfKGKD_QK_Gs8B5yK-iThoJwWv1bZ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0mJXqnfoLfhQH6P0hSuzQy6FEq_slkXABhyPVGtAokUhbUXnUPbkV4XMOeL5G1KEmK8aLttQoGnETvfrr319PbNy_a0-kpFgxWBKdHMxXUoj4NoUnqGOlszmrJEnXYLowpix6Ax97OCX_1aAa2f0gOa18MdzhCHp_HzeNAG08VqvQeN_LgRZzJ0cy58KPjV1yVqWSlmHbAZyFqjD-OdyLfA7PvLq4Cy0k2T7QIhbFXrcZ0_rWLk71ECWw2snzMTfq6elh-Yt_nvUGQIuT31VT1BE1J3wWFzssROWX4hcNZPQi83ENbGtBpa6y6Q0ntg8S5FFegXLYegSpEieEN01g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MFeB62l4XhLds_sHfu1Vqgna33gc7d08CYytFHh5BbxJc0k-GELeItiB5TpAEGp13MdLqdCJ3RsKvlG_06OwCUTvlRwHmAfunpZu9OoSwphDj8ZQidCxtajqeRzGr1ImS2Jrau26HexWPCpdKKUqIQFmaWX6oYbiF6TP4Wf5JSiSynbfPBS8RwO1f35PPI8Ghha-7igNWCoAJwO-R0Sfe300xuSsG2-ysizFTFZWY_Gt-thXimYOBZHQsdEUuKiNfKgk35Xqo2DmUSyPVelwjOSyQGQlrygO24VraVh-QQew4t1I72tqRlNBjNl6CqY69rq5RV_mRjv_lp9kwpvh6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-fMkSUFluVR5cNbjHt1YdYt7PbhWcrzHirRkQcMqsJiU4UDnxEcfwcKOzoJbb2NNb3ecx04RpSRuJ0gddZMscWySXNoE5JoQwpGdxml-v_-CEhNnwyM3GmJ_ybJCc23UbpHTBL_11gba84gP2IrKAhki4RRBo9796t_2X3IU0FsyMBnWYOKBc47AsAhpbWJuYGRHoMJkM5z5xTIcVVZxh6Hetg1ZYbTazCCzTTsTn9OZRXDTuw9Xr2ZBr3WAJa_tIpSF42k-b1Im7NrkYUNQ3vSfOyziejRUg0gHCsvYiiTMIb6t_eMinQ63KHqnNTsivntIlO40Avi0XkfVoL7Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMhAdhsbNO5p69nQ1xntvAd7rpWbtdTZQkdQ2vJ6ys6y8gNVivAXyiYBUEPUTqbYNyvMLgqMZK1UYWQJHCjw2kx5uRBb9hSkS-ui3dTg1s8kZmIiZ0QppPVn_TKJaunF8hUopscxEHPErNP9TpQMTWQbidQsyTyIvHPYPsaSw_hV3RMFgwoeKSDFiiA0z5obC8EiEKdq_RZfx4uYbXRMqldl0DZYTa3Mew0dBKOhnlyXMrSEg8liAaoUJpRPo0iLwfSF3R7gmLizTYt_TKktduLBCIehu7sxbxr6FWHHF8GYce_sWZPZ-LZlrxbyG0JQMvm4-uvvOHFUBpJblLGJCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت رهبر شهید انقلاب در حرم مطهر رضوی
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/449492" target="_blank">📅 22:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449490">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiGGesg7xhlMYgt6vC1JixnVBD1bgnVwzYBc-P3-N3NGZQoA1mgmz9vAXEpA0xGCajjGJz-6aXq7iCaG1GUILV6A7MGVa3S-kDPEyMf45DcGprDUU2scKf79x97HZBKOB6H5UY3Mg-joVYMUM4lBRZKzabDrUvJ8UJlWbynJ7xHBu3TlF11vs71hdbYBnF1RzwmTSwVd50kUJ531noh0Qo1sbimuZAlo-mtDUdjl2FkaOAgwhe2_SaB_XOBZW7tdz0GVdqQ-_oD8fSgXT9lsws9N574d_0dQJk22s4lohqX0g4koZWoCrFFOr_JJkvCbtTYcoQFtDrHcXuzIjhs7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله خاتمی: انتقام‌ و خونخواهی مطالبه امت اسلامی است
🔹
یکی از برجسته‌ترین پیام‌های مراسم تشییع رهبر شهید، مطالبه عمومی امت اسلامی برای انتقام و خونخواهی از عاملان این جنایت بود.
🔹
برافراشته شدن پرچم‌های سرخ و شعارهای مردم نشان داد که خون رهبر شهید فراموش نخواهد شد و ملت ایران این مطالبه را با جدیت دنبال می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/449490" target="_blank">📅 22:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449489">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e60fa26a88.mp4?token=ISMCFxu5AyLdSsN9nl7Ad0oGAWeETPrALWZkVdVXZukw__e28dN5bqsoUc0sX1WUc9w39X0F7Exslx8Yi5DXLik8dAPZ5IE3qzKoYO0mIItDRnLr1A0RBuOCAEvDj5l6XwWo672AUyJO5LwhKmND2qh5VcW1FvlthjErNU_UGd00jLLs03ZMekS42zB5-kGXjNtri8N00Wz9DTuhQjNNiFm8CzqxJIgPM3JpKTP5gOCloZNjNmEPzUf88EI10gE-fG6mZ-W0x0hiyWQ1pO6eiZ9hAYfL1lMQRE1dAGvRSrPRKxopWbU5lhoP1Tv2gzGYvwGEaX-B5CLbq_np8ESeCnLMIzZRWrcfQQhW9oIQLYtCMcHnb3EzvPpog0WOObtjKNZ58MSUvxDooaxVDKOqhsJQgk0qWy6xYUHsW2bUbAILSQC7oT22WdTalhwB-pHgYTTwXbcddHNU3fjN6X3YJi56O0XC3UvkSdv77opZEfmQTuh6FnvV8McXecPQrT9eD-f1OGN-99gDbRx_VF89C6O1GdNTgjp8NQ_wfrMj42jPJEzi1SVGb8dAvOWXLWCxQgR4gfMU82GPrQWmQVoxWlhFqEyd0apCe25jbuCIOEYQF2gRKuaHxu14lLJM8wjvVDeDKct_XblAxeoFkUjZwHHUfJHrku2mfR1rCy5RtSs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e60fa26a88.mp4?token=ISMCFxu5AyLdSsN9nl7Ad0oGAWeETPrALWZkVdVXZukw__e28dN5bqsoUc0sX1WUc9w39X0F7Exslx8Yi5DXLik8dAPZ5IE3qzKoYO0mIItDRnLr1A0RBuOCAEvDj5l6XwWo672AUyJO5LwhKmND2qh5VcW1FvlthjErNU_UGd00jLLs03ZMekS42zB5-kGXjNtri8N00Wz9DTuhQjNNiFm8CzqxJIgPM3JpKTP5gOCloZNjNmEPzUf88EI10gE-fG6mZ-W0x0hiyWQ1pO6eiZ9hAYfL1lMQRE1dAGvRSrPRKxopWbU5lhoP1Tv2gzGYvwGEaX-B5CLbq_np8ESeCnLMIzZRWrcfQQhW9oIQLYtCMcHnb3EzvPpog0WOObtjKNZ58MSUvxDooaxVDKOqhsJQgk0qWy6xYUHsW2bUbAILSQC7oT22WdTalhwB-pHgYTTwXbcddHNU3fjN6X3YJi56O0XC3UvkSdv77opZEfmQTuh6FnvV8McXecPQrT9eD-f1OGN-99gDbRx_VF89C6O1GdNTgjp8NQ_wfrMj42jPJEzi1SVGb8dAvOWXLWCxQgR4gfMU82GPrQWmQVoxWlhFqEyd0apCe25jbuCIOEYQF2gRKuaHxu14lLJM8wjvVDeDKct_XblAxeoFkUjZwHHUfJHrku2mfR1rCy5RtSs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لاریجانی: باج‌دادن به آمریکا سایهٔ جنگ را دور نمی‌کند؛ چیزی که جنگ را دور می‌کند آمادگی کامل و چند ساله برای دفاع است
🔹
آمادگی فقط نظامی نیست؛ باید دولت خودش را با اقتصاد جنگی هماهنگ کند. باید آمریکا ببیند که ما برای جنگ ۳-۴ ساله آماده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/449489" target="_blank">📅 22:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449488">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgQEDitv3wNiZVmjZWbJf0GzKPmJixXDKEkXEosxaIe7zrt_jIosLYfe14E0vkNYkag-NhMv531NPhq97d3MNMpu7UwkxKjjw-NV8ZVrbnOP-2fr5xuWGlMOkxa-74dW-z67ty9ClOYTxkCzFEtlIHmRomTHlJdthIsebJFFstVqL64gH7Xf0qazAs2htYnnTqKPCt_4807ntXIfKXXPWSgon2eWVp8OyIy0yVpg0vcIXIv03aAn9mIjUYsPueRtiXClkQiOdl_qVI_hwdEH8oLEu-M4CectI5IINriCOltidt_1tTdwOg5K0JQQDIQhhbIimA6ztBecKPnjzYHCHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناریوی جدید ضدانقلاب با کشته‌سازی تکراری دی‌ماه!
❌
اینترنشنال که از تشییع ۴۰ میلیون‌نفری رهبر شهید برآشفته شده، دست به دامان دروغ‌های قدیمی خود شد.
❌
این رسانه ضدایرانی در یکی از گزارش‌های اخیر خود، بار دیگر دیانا بهادر را که در بهمن ۱۴۰۴ (چند روز پس از حوادث دی‌ماه) جان باخته بود، به‌عنوان کشته‌ اغتشاشات جا زد.
✅
فیلم منتشر شده در همان زمان و توضیحات رئیس پلیس راه گلستان نشان داد که این بلاگر ساعت ۲۲:۳۰ روز سوم بهمن‌ماه در محور جنگل گلستان به گالیکش با خودروی پژو ۲۰۷ دچار سانحه شد و در بیمارستان فوت کرد.
✅
کریم مخامی، پدر دیانا در آن ایام توضیح داد که چگونه دخترش حین رانندگی دچار حادثه شد.
@Fals_News
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/449488" target="_blank">📅 22:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449487">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
لطفاً صدای اساتید حق‌التدریس و دستیاران آموزشی دانشگاه آزاد باشید. از بهمن ۱۴۰۳ تاکنون حقوق آموزشیاران را پرداخت نشده است. مبلغ حق‌التدریس برای استاد دستیار حدوداً ساعتی ۳۰ هزار تومان (بدون بیمه) است که هنوز پرداخت نشده، در حالی که اعضای هیئت علمی هر ماه حقوق کامل و بیمه دریافت می‌کنند، مگر کار ما با آن‌ها فرق دارد که این‌گونه است؟ دانشگاه به ما نیاز دارد و ساعات تدریس ما حتی بیشتر از هیئت علمی است. چرا پس از ده‌ها سال خدمت، جذب نمی‌شویم؟
🔹
۱۴ سال است متقاضی مسکن مهر شهر پردیس، فاز ۸ پروژه شمس راه ماهان هستم. پروژه توسط شرکت مادرتخصصی عمران پردیس اجرا می‌شود. پس از ۱۴ سال تمام پول را واریز کرده‌ام، سند ۵ برگی و سند خرید عرصه را هم در دست دارم اما هنوز هیچ خانه‌ای تحویل نداده‌اند و هیچ مسئولی پاسخگو نیست. افراد زیادی مثل من در این وضعیت هستند. خواهشمندم پیامم را به مقامات مسئول برسانید.
🔸
در مورد تحویل خودروهای پیش‌فروش شرکت سایپا هیچ‌کس پاسخگو نیست. اگر قطعات نداشتند چرا پیش‌فروش کردند؟ پول مردم دو سال است در سایپا بلوکه شده اما از تحویل خودروها خبری نیست.
🔹
لطفا پیگیری کنید که در مورد تبدیل وضعیت نیروهای شرکتی اقدام کنند. اینجانب نیروی شرکتی شهرداری زاهدان هستم. ما همیشه در برابر زن و بچه‌مان خجالت‌زده‌ایم چون حتی پول خرید یک وسیله ساده هم نداریم. چندین سال است قول تبدیل وضعیت می‌دهند ولی خبری نیست.
🔸
ما در منطقه اسلام‌آباد شرقی شهرستان کارون هستیم. این منطقه اولین نقطه ورودی شهرستان کارون است اما هیچ رسیدگی به آن نمی‌شود. انگار متروکه است! یک خیابان را آسفالت می‌کنند، ولی دو سه ماه بعد دوباره خراب می‌شود. بچه‌ها هیچ جایی برای بازی ندارند. نه پارک داریم و نه محوطه مناسب. لطفاً نماینده و شهرداری بازدید میدانی داشته باشند.
🔹
اینجانب از مشهد پیام می‌دهم. پسرم در دبستان دولتی شمس‌آبادی (ناحیه ۴ مشهد) تحصیل می‌کند. حدود یک ماه پیش به طور ناگهانی به اولیا اعلام کردند باید پرونده دانش‌آموزان را بگیرید چون مدرسه قرار است منحل شود. حالا حدود ۴۰۰ دانش‌آموز بلاتکلیف مانده‌اند. مدارس اطراف بسیار شلوغ هستند و کلاس‌ها بالای ۴۰ نفر دارند. دلیل انحلال مدرسه مشخص نیست.
🔸
وقتی برای دریافت وام ودیعه مسکن به شعب بانک مراجعه می‌کنیم، می‌گویند چنین وامی وجود ندارد یا بودجه نداریم. حالا ما چگونه باید کرایه و رهن خانه‌مان را پرداخت کنیم؟ لطفاً به این موضوع رسیدگی کنید.
🔹
اینجانب یکی از هزاران مال‌باخته تعاونی مسکن برق تهران در زمین‌های هشتگرد هستم. شکایت قانونی هم انجام شده، اما متأسفانه بی‌نتیجه بود. لطفاً پیگیری کنید.
🔸
لطفا پیگیر لیزینگ خودرو فرهنگیان باشید. بعد از شش ماه و ارسال بخشنامه واریز وجه، تعداد ۳۵۰ نفر از همکاران هنوز ردیف قرارداد برایشان نیامده است. بعد از پیگیری‌های مکرر از طریق ایران‌خودرو متوجه شدیم که لیزینگ پول‌هایی که برج ۱۰ سال ۱۴۰۴ از فرهنگیان گرفته را به حساب ایران‌خودرو واریز نکرده و عملا خودرویی خرید نکرده است.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/449487" target="_blank">📅 22:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449482">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwpCN7pRmzLN0t2QsBFEQyd8PgtiZXX1hAcN-tp74OEhvETVym5RM8oTmEDwy3rJKBcDWq6a7BCdTcSVh_fsG_bSsEmxqdKAvvFcoMWL2Nhr56AfVZ1xmEDSoVzHnuVyD1OVq63u2ix8UK0NqcIFir9hjpCzukMBQP5rJZvLJUFIPnEBJx6kXhmNUfcfw8lsoMiwGlo6vLB53GAWBiUui86tzCILCF9tR4H5gEAlJpi1QpLskWPNb83tpfDrL2XALrKYNj9n57tNjmwo_2SvL9r2aSnQ3lWQS496JKkzUyg-IWEU-3V5i1rKPdm0znG9knDQKLUb6OZTP8BEuc6UbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VNlrf9Bx2BMQYL-EghVi0TwRPX2KskiMP8HWUwhkpUgIsoZkcLcikS4zfi4M6MVTmByPDF-S5fO5Iky5xoIgYTBVRhZZ4Do3SrXhprXfzZ3YugA9yXCQJUeM_QApJn1AJhsqZOz265qaOAeUxNja606Z6ls2CfHRj2vP2SeCL54bfGq1feyYXcV8RPkBq_htzWlH_x4PvTFDkbutEJtcJvm8Zv_XUW_D5Aoevr3NwJun4o2d9O4oLVDULvYwC91HLniMiG_B7zlbiMKZm0gCMStsPtNDnHaao9nF_WoZGnj1FrnCMyufo3ASYAJcu_Io-EBDO56N30l8yFzVNS44cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MjAvq97J3xegvWdGxmZJfBzEwN4w_zqlFphn-8avCeH0mPU1teFwicStgK0NpdyPQ62dS266vJmnlmUh9_vdM38733xbybA4thCb6a2juA9Qp7WlqrkjNtGuS7IMyh8zAd__b6Smqi5ipbHhF7sAsUW_nxCyBCKHNa365_ylHNtG5NdBV0Ul4yissUwvsVLkJCJJqBJDCSPX285jPuf5sMHVJUAXevawev1FQpw1FYOun538pyrWeRzEM-qpU_IcCSPA48t26Fqbl6qBSqRaNhHC8iLr7ZrCONtoNaDc6gGvHE6e6FsEhE8LxtrRe9LY2OEgGKjaaMzDLX9cpbefvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j5ZNe85iYqyGwAAmeN58TzG2EQuggvox9aVn3XvTjhpCc9uIgi8ZMWLWOj15zhNGHNBp1He-OxWnz2eh1m9OB8GihaW8sbibir8xWW-0UwZXkv6s7dCVgSK8EqxCp122FyPgHIAEXJH3ydMVSmVsJxMq-njkoxK5oApisaVeMYJB7bL9_ecH90qZ4RDq44c4f2rcmgfRBIe_EVDMbRAFD20Q29GmfFOe39XdS7w2j3QZ-vTcFM5N7IiLokoFsWTr-5v9DjErAdGV0DomoyXv2EKYVjb2h26K1tDs058PLwg_oHGcphIooha0o-4e1GkragnhSpS70FNIfC18b3RDig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZswmwNii2lknw9yRvuOwpMw23wCALsjNX0D7y3pWa3iQZaFcX-BldTj8hOnfh_EZP0MYda3mScDjjygkMIvJnSXD2s5b7bzgk-aGbthooyQQzVTcUemBY5_9bovM2odaOOVRtfhMhhZjC-89wndSjV4xGYhhbvARyKoW9kKwp0V9nA4i4CM8WJ5Lyrg0s69nzkjoGzBXopQOxmxLxJHXRPCLU6ln0J9uvxaR9D4c8gFIySaWh_eIqTkUeNMsgecHM2hz6TzZjSFFQ0YcUd8D--mKXz9fR3TQ1h3gfMHgFFkbvUB_oL4QiegkpIgosB52pCarVNu-J4jXpFYnqm8dzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین بزرگداشت رهبر شهید در حرم حضرت معصومه(س)
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/449482" target="_blank">📅 22:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449481">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afa38c5c9c.mp4?token=H_tIFtm4mXwWUS5RPjHZ5Tz_7nvc-2ZXiYG64kvYH9Ag7_RAucKh2WwzqfjYGeg6H4mQ4iYQgF6nqCfGWB23qPNE0oHwotWLwHB91yDSQs9simc0MObNFPhMPldV86t_9cVhcxvU6hj4lHsgDJLFOQtizxI4fJaJVqHcGWjBX2tLyUEw415kHuOAQvUCizcIo4ZW-HhbN8rlBpZkPqZrarVNUT7K7td2zP_LmT8lVNHxIz52vF-EWGZ_DyLaYfudErkT0QmMwgceWErcvcU0OHriUR4B2x0m7NmTlacd0Xve96eCFnBWlbGhKb-S4qeGEDw7ivP8pR0e2ckK7CgujA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afa38c5c9c.mp4?token=H_tIFtm4mXwWUS5RPjHZ5Tz_7nvc-2ZXiYG64kvYH9Ag7_RAucKh2WwzqfjYGeg6H4mQ4iYQgF6nqCfGWB23qPNE0oHwotWLwHB91yDSQs9simc0MObNFPhMPldV86t_9cVhcxvU6hj4lHsgDJLFOQtizxI4fJaJVqHcGWjBX2tLyUEw415kHuOAQvUCizcIo4ZW-HhbN8rlBpZkPqZrarVNUT7K7td2zP_LmT8lVNHxIz52vF-EWGZ_DyLaYfudErkT0QmMwgceWErcvcU0OHriUR4B2x0m7NmTlacd0Xve96eCFnBWlbGhKb-S4qeGEDw7ivP8pR0e2ckK7CgujA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان داری مردم استوار مراغه آذربایجان شرقی در شب ۱۳۴ تجمعات مردمی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/449481" target="_blank">📅 22:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449480">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugIuWeqaPCmsIOvhpcMpkSP2SfOh12x65MapyeK1SbQDlHp00mCzj-iaUixIfAfhMULGNqOimqQT2JpgQDzq8w8l-v6DhWQ9Fc-emO_I1sS-WBoAEHnGjFab_5us-qDo97RK0q16hoex9G4S4QtRWD3he7tOAFo2IZnlFNxQkkovD3N63y70JFPso73KVMIt5RdaDeaTGa5iYuROmjHKpNJRwg0C254-qTVMZuFfZLzLZkI9oinlVyYnvaBv30LHaMNGYBtVJ7VIj7mh4XpWMkgLitUFDQdj3p3O4Utnh0xYcgogFsaevShoOKq_NLn9UqKnCzEvcxi8fzg1HkBJ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفس لوور زیر موج گرمای فرانسه به شماره افتاد
🔹
از دیروز یک‌چهارم فرانسه از جمله منطقه پاریس در بالاترین سطح هشدار گرمای سازمان هواشناسی این کشور قرار گرفت.
🔹
موج گرما دو موزه مشهور پایتخت فرانسه را به تعطیلی واداشت؛ موزه لوور، پربازدیدترین موزه جهان، اعلام کرد از جمعه تا دوشنبه هر روز ساعت ۱۶ تعطیل خواهد شد. موزه اورسی نیز خبر داد به دلیل گرمای شدید، از شنبه تا چهارشنبه ساعت ۱۷ فعالیت خود را متوقف می‌کند.
🔸
گرمای هوا، همزمان با آغاز تعطیلات آخر هفته و سفر میلیون‌ها نفر پیش از فرارسیدن روز ملی فرانسه، باعث ازدحام گسترده در جاده‌ها و خطوط ریلی شده‌است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/449480" target="_blank">📅 22:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449479">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBbyytcOUICfJ96GzmjesELSJkBV_8tB5QC8eR47hOLsqQegZRX2zlQ1Gb4YwrPLKdHKThosMeZalN5270I6l8zzG0I2dbn7QOavpUJKJohvxqFuL0IF9SE6PBv23-71OAtqXqxYYWZJUZLmdg_KAyRTpAADxeX5OlKbCKoFmOP8z1kYqTQ0F7g0I_soqvqbJyn92GNXRhkR9TaEPptlJ6jAiBQ0Ap1Z17E0Z1LThr1NB5rfgIn95crY7sUnVNmexMnrM4hXBl0XC9h8yu__F-bFHvPf5C1P__G_HZ8mWcUukNMxRmtSNtKmCuVr_4IEKuTcAGVJMjhMdtP5Vv5e2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خروج ۶۰ تن زباله از یک خانه در بجنورد
🔹
رئیس مدیریت پسماند شهرداری بجنورد: با شناسایی دپوی زباله در یک منزل مسکونی، ۶۰ تن زباله از این ملک خارج و پرونده قضایی برای مالک تشکیل شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/449479" target="_blank">📅 22:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449478">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBti2chLJZC_vvT2QHXsPA5FuKAab9Na1fbxZXVVy0DDBz8oJcf3GtYh9Q7D-ZluGFIjU--4anlxqcAilBUb8_rCoWnPbSofZJWomLPIOTAnSz7Cia8udm89IqKS848gSvJPu_Myj9CmsLW75v1kO-6iszVzHUC1RHn_RqFZGe7obp41Q276MMwJEkUteHlsbCugU2Ptgs7Cw__T4aoJqIR_8Zxl_aqhb7Ky3p3r5fZwTiCITvblo9TCKycOflsgtjOE_AI0KZaYW61d76uFZSmDtkmCoH36KpPmShNnux-hBnLwMD-6WR6NmZjBX7LxRVqy-14gsdKwYs2Xemw_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گیمرها تنها می‌شوند
🔹
هر بار بحث آیندهٔ صنعت بازی مطرح می‌شود، این سؤال راهبردی قدیمی دوباره بر سر زبان‌ها می‌افتد که «آنچه بازی‌های ویدیویی را ماندگار می‌کند، روایت‌های فراموش‌نشدنی است یا تجربه‌های چندنفره‌ای که نسل‌ها با آن خاطره ساخته‌اند؟»
🔹
شاون لیدن، مدیر سابق بخش سرگرمی‌های تعاملی سونی در آمریکا، معتقد است برخلاف تصور برخی، بازی‌های تک‌نفره و داستان‌محور نه‌تنها از بین نخواهند رفت، بلکه همچنان مهم‌ترین تکیه‌گاه صنعت بازی‌های ویدیویی باقی می‌مانند.
🔹
با این حال، همهٔ گیمرها با لیدن هم‌نظر نیستند. هم‌زمان با انتشار صحبت‌های او، تصویری مقایسه‌ای در شبکه‌های اجتماعی مورد توجه کاربران قرار گرفته که دو نسل از تجربهٔ بازی را کنار هم قرار می‌دهد.
🔹
در نهایت، آنچه از صحبت‌های شاون لیدن و واکنش گیمرها برمی‌آید، این است که آیندهٔ صنعت بازی‌های ویدیویی نه در حذف بازی‌های داستانی رقم می‌خورد و نه در برتری مطلق تجربه‌های چندنفره.
🔹
روایت‌های قدرتمند همچنان می‌توانند میلیون‌ها مخاطب را با خود همراه کنند و در سوی دیگر، بازی‌های چندنفره نیز خاطراتی می‌سازند که سال‌ها در ذهن گیمرها باقی می‌مانند.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/449478" target="_blank">📅 22:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449477">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbc2faae6.mp4?token=LhR1dNBoycwksgOnqR-gqJqSwKUj3eva6IRhsMscp-Ly_3CTo1kYmgClpNw4pcHDEXIDGcGd394uO3idutrusiXwh7B5M4D8SnCKBXeVHrcG4ZiUOCoW_R4EW01pPPRt68M_aDm8FYzXJwAZ7PUilw2GEmTkdOS6QbAOrSPFTsWDmDwQvqhpJXjlse6h09BrBCbl33H2W5vmWVmG8VcEupUP9iDINxzMlMz97XYOYJPKepi9jcTWrD_N2XbgX1xGDWpYTkvLvBV-ChScdnVb5X0xcXsZxz0tpQKH3MK3cxhzL0cW7wKemjX-iBf78hW4JIVFRpTUxRSwCDsiItzmpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbc2faae6.mp4?token=LhR1dNBoycwksgOnqR-gqJqSwKUj3eva6IRhsMscp-Ly_3CTo1kYmgClpNw4pcHDEXIDGcGd394uO3idutrusiXwh7B5M4D8SnCKBXeVHrcG4ZiUOCoW_R4EW01pPPRt68M_aDm8FYzXJwAZ7PUilw2GEmTkdOS6QbAOrSPFTsWDmDwQvqhpJXjlse6h09BrBCbl33H2W5vmWVmG8VcEupUP9iDINxzMlMz97XYOYJPKepi9jcTWrD_N2XbgX1xGDWpYTkvLvBV-ChScdnVb5X0xcXsZxz0tpQKH3MK3cxhzL0cW7wKemjX-iBf78hW4JIVFRpTUxRSwCDsiItzmpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مردم بندرعباس در تجمعات شبانه علی‌رغم حملات دشمن در روزهای گذشته
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/449477" target="_blank">📅 21:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449476">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a60f730f6.mp4?token=KCm5caJkPOmw-AIjhKDy_rWUS1dwUievRzBIlTDafuJrtz2rx-p4nouWrutMgx7R19Kp-i5WxRQP0em0S0fDRfGpudfCBJJ0HT8RCykFAZW1rXL4643oQJHXhEYGIyWrH8XpxKTe-rewHIjcq27DTKZcxPR_ahK6g0BeTWX-EoLwLFnNE1Omxc3bMNTOlHO1ZM7bY7mIcr7ZQR4NEcCXbbp4jCWn6riqCVajKFSBww5OinqGljdNW_ctkLeywpI0H0NgjIfRHj6bYAEA1WOlXgqMPneNLl8ZqoBkoVQHMwI86qhzQoTuQG7pLYpSUz9WYTHHqo8CCQ1CDJ1BJjqAHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a60f730f6.mp4?token=KCm5caJkPOmw-AIjhKDy_rWUS1dwUievRzBIlTDafuJrtz2rx-p4nouWrutMgx7R19Kp-i5WxRQP0em0S0fDRfGpudfCBJJ0HT8RCykFAZW1rXL4643oQJHXhEYGIyWrH8XpxKTe-rewHIjcq27DTKZcxPR_ahK6g0BeTWX-EoLwLFnNE1Omxc3bMNTOlHO1ZM7bY7mIcr7ZQR4NEcCXbbp4jCWn6riqCVajKFSBww5OinqGljdNW_ctkLeywpI0H0NgjIfRHj6bYAEA1WOlXgqMPneNLl8ZqoBkoVQHMwI86qhzQoTuQG7pLYpSUz9WYTHHqo8CCQ1CDJ1BJjqAHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مؤمن در میدانِ امتحان نمی‌ترسد
🔹
بخشی از سخنرانی حجت‌الاسلام علیزاده در آخرین شب مراسم بزرگداشت رهبر شهید انقلاب در حرم رضوی.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/449476" target="_blank">📅 21:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449469">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ga-3oOx4phbJE5yhgly0T_ou_8-MQBXi2c4cQZiGEA2H0s0kddXJ0MJ0LHiGB-rD8GNWlmnSuEv2-AZk_PvzqSdsTeS0CRSlOP6JFcWYmykv_XdI70cyaVSMb0Sf8B-fN69DIw63NtKEiv9I2bSsm3L-YhQeB-sdxrEfvEoxX6IyItjD8x9eXKuyG6rxWob1oG5szxo1-MAswTJkmU9xBBXahDhAnBnN4wGo7MQ0DjJLrbUUGEewqXG5SEunWcBpSWzvioNeIkmNDHUO8_bVisP3Gv6FZNLjuwDhifAr8lNkWXI6ITmpeNLcj-xabvvC4UMDE9cyg2WU9yy8EiL4AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQgDkqFdF2YqeTC9OtjPM3WxrTync4zQA0u7B487fo8ZK7yRrAybb_Q_gOqCJdc1_uZGRo7d2Z9j3S5fS-xGsgX3Twl8xCtI44IvkLzliwqmphUnH5K81kgldEKZM10i-tiVmt_7ma4wYCWUEtOPbUzZbpgBJXiyKwDb6-de5jbB-5krcQy0_UFarcRJLbpM0cStPRtzftShtHlYz_cpOttNSNXexYQPml9Y67wrbo2Ohyk5P_vENaLGjFiNe6qJuJ2dCf5GyDlUoT70HmBkq7FxR2IokXFwEp2OIO957RNkmsdpWdXLQ95t_KJBad1GxaoE5VvhX8iRdXKJnSYcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4qwEVrjeWcyhVW68jwI9o14hi9rUbaHmfEWg1CNRzgjzV45UCQIaW7iukFFER-l0lpxcBy7BJB4s7rN9yAqzRHlXlrnmURnHTIZ53ieTwdL1fDBofKK008Y46JyK1Wh2-acxkS8n1leCj2WvBvnvVzciJhrkTJlJrothJVo4lAOyBzma_SPkNJ8Hxo-iPhr2ktnGPdZP4bot23hAwJqXas2XS45XE-W7wozH2Atph5c1s-BQQA4WfH0UJPMHNxZUW7YoSCJvDHNW8R-8cueDSRtSnjBPp3jtM7q3UKNXftCaGkTzLHLsXzbjNFbyd1p2zCUqF9lqQTcDuVbZ6rvIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwUGITKYOxz_vWuDoeQTD7VEvtC-w2VLQrOFvYrs0nEd78s-AGEBiYYORXl5HlPAvNy6h17mesznQvxw-fTC83MdyVXPtubkQCVovGkpbIEUfHJmKPAEgfdOq6zeJTEt5qa6W2NBmfqXUZAxniV99iuIHfcsNJ6HjH8a6FzSILlW9Qp8IuLgT_3l-BV6z0gpzU2zKQeSCOV4x_RMEAPMthlfp-3uHTANf7K2zxsL-JnsJhdJzC-gYd8KornRZ5AL26D6A0nNQA9vssGfFyyn0eAN8iTw3xyqlWtG3u61NpMWI6HGCrqfGKQQms_DCwJ7d5w_Y-8d0DKhPy90MOojRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szSXZ7LpT256FVYLCdAAxjKexrguovrwEVl8faRmYYmNiCX5G0Y09Gtx9ML_8zfnDkOLjF0sQsxuKtnsLu5xTNiZQc3srt4uKSEBLVeW4cZogeBev3awDymjzJaCDvGZXbRPFq0PUT932U4UCt7QLxeFTckOrFGJCq2wmbwiV9Gl5a45TanOx6kht9TVO2lsiFyXVuD3CkL8q22urrENi3Si2J6T3kJ5M4xXVZlY1Mz7vA1sU3U8g2vRhQKu7QJzDbKmqczDtWbWMHCLeP4MP0lqK9AjFQrWwJaF11nIh1zqIxklSa6NtRmBaYqhe_a_wNZ1lUFWm9OKEmnw6Gx6yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YUcl6EpU0v5zVVE46EGlufMsc8SRCGF2mqeE0uptP29KeTUGTR223ZKzr4033U9AWWWTIPb1rsvD-IZPN_Ofvrw26qsaRobpirPfVgCaEnsJmbGJkrGRuwHRoAbrCZrVxO3bEXzLbhHwqauT6RyCrhXDKjdDt8zNlBLwy0OfemUi8yi8mybnTfrD-Ct2XOmWVRN1zHDhEp5hufYX-tQVi_TjfySaZpdimYuU_iOKtzcCPQcWUC8LrvG9l5FYcmmw7Zc3mX9Rd_8pE7eKtQDCWDI0e-fZNbgXZVTp5nT30zFnAHcZD03lTXL3eT4orilBb2dW7aju0pJRTt1jXylM-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/czDEo1vS88dkrjGamGoYjJAyZBxfbeQJEfRky67iBaWk1ugKIkcL0D4cLRMdUHb-pMPXiZu0HasOG0YSwoS4LUI8-NUN63mXT08kvuQLaeKsnK0IjxrbpJiiPd2Yw73EUlHZIMa9agPaRi3b5P_5zp1tYK6BqqMlB2nRLApgMXORj-b8kPO9mw00QxDy1701hWZC9WPbOissVPVi10kAsrW7GuN8S4vCzpLNSFjiZCRluj2M_9cAwGfbHh21TNe-ea-omSzy4bUOGSSO25ycAXjxd5YOU3Qc1GkNJ3rQgdgqPHTRUeCqiqgwZISHBPehrCyQOs_LOI8AOS8meCSgYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آبادان، میزبان پرچم‌داران کربلا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/449469" target="_blank">📅 21:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449468">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🎥
روایتی از کوچک‌ترین نوۀ رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/449468" target="_blank">📅 21:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449467">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CL-ohK8wXmNxDtPXNcrskJqA8S0nVbhaqXagQ4s3_CkZDzSBF21fHhgy65TigEh9JOBIz38tl0JC9Meqbu39KJtSrUYr68Kl9kTjyssPq5JijUP_1trgtAc2hQ7N7JU7rVMx05PppKPa3z9zwHOAnI4xkSyGiADg9oFzZBwID2uk-jMc_6GVfqfDbrlG_yw71kt8yKEIQGnwlQJUZxd_iVPjOZ7fcvh5pTmEoGdMVfhRhxhOkJL-vsA7Vwj7qcOPoj-ZLWd0hZC9XjsQJnVFFbL1xlZdEWHS7o8LAuV4mJHAyB9yyagJGdi-xWoWBLatPrwgFnn0_fyLmp8uAvU_Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توضیح فیاض زاهد درپی انتشار یک ویدیوی بحث برانگیز
🔹
«آنچه دربارهٔ رهبری و «بخشش» گفته‌ام، ناظر به رابطه حکومت و ملت و گذشت از شرکت‌کنندگان حوادث ۱۸ و ۱۹ دی است؛ نه چیز دیگر.
🔹
انتقام از آمریکا و رژیم جنایتکار اسرائیل حق مسلم ایران بر پایهٔ حقوق بین‌الملل است و هم واکنشی عقلانی و درست.»
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/449467" target="_blank">📅 21:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449466">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pywtEq_0jplydjonMIXqjk6zL8ioqN8MPyTFijk37q67MI9gdut6kHOlyW24MQggj5rOWAOCeOM1gdZ4Tcct7JPoEnmf_SCVlSDDOyDwsQnJsicR1SbFYBK3XUbra7rQ4g7u9nwTwxXmc4JaXHky_PRzVKDnbcR-exVvZLCeM57ZiR5PIlSIMSYtSHzRquKgC373kk_gggDYi5-cNG_nSrPrjp_UzCPUrQVVmOggfYDZerygOd7-NMg2QrgsD09wR8fVp5BBlppavQX7nyP1IrssE0OsbYGCVL9Ki346uITPg3DigelfVJ1KPwrOi0PFCkdO04qRUe-uN8N-rdJhKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همدستی اردن با آمریکا در حمله به ایران
🔹
داده‌های رصد ناوبری هوایی هم‌دستی اردن با آمریکا در تجاوز دیشب به خاک ایران را تایید می‌کند.
🔹
طبق رصدهای هوانوردی، هواپیمای جنگ الکترونیک نیروی دریایی آمریکا از پایگاه هوایی موفق السلطی برخاسته و هواپیماهای سوخت‌رسان…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/449466" target="_blank">📅 21:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449465">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تکذیب حمله به نیروگاه اتمی و انتشار مواد رادیواکتیو در بوشهر
🔹
عصر امروز خبری مبنی بر حمله آمریکا به سایت پسماند نیروگاه اتمی بوشهر و انتشار مواد رادیواکتیو در فضای مجازی پخش شد.
🔸
معاون سیاسی و امنیتی استانداری بوشهر در گفت‌وگو با خبرنگار فارس ضمن تکذیب شایعهٔ حمله به نیروگاه اتمی بوشهر گفت: انتشار مواد رادیو اکتیو و ایجاد تشعشعات اتمی در سایت پسماند نیروگاه به‌هیچ‌وجه صحت ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/449465" target="_blank">📅 21:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449464">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a19de53e2.mp4?token=blGl5sTi89XDyw9hpU63FiFJdjk9htDY_gQ2E7EZNMMA0Uz2D-pW05q2mldQH4TUn3bjUTOkVVILOS9vMQyxAG7JkY86yZMMTNShC6f-B-wOUsZr6PMKPw8WCxVXcHba8MQ5TTs3SqvhKQkrRshRgfFxPjx-kczjilnnX6O7lk_0D6G2pyFZ3KpFbq-tysAasK1oWzu3OKc-IAF1A2hua4n37Yk0O9NlrR_qf3-wxfhentfYRdCUaNIzno0bgGOjCjhImlh9KTxvdni3CCt9dT8dYmmpOFS9DStGGvR1lgiNSInjwltinQz6bNf18aAUA08uTEwgSr9OujVLmcXsug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a19de53e2.mp4?token=blGl5sTi89XDyw9hpU63FiFJdjk9htDY_gQ2E7EZNMMA0Uz2D-pW05q2mldQH4TUn3bjUTOkVVILOS9vMQyxAG7JkY86yZMMTNShC6f-B-wOUsZr6PMKPw8WCxVXcHba8MQ5TTs3SqvhKQkrRshRgfFxPjx-kczjilnnX6O7lk_0D6G2pyFZ3KpFbq-tysAasK1oWzu3OKc-IAF1A2hua4n37Yk0O9NlrR_qf3-wxfhentfYRdCUaNIzno0bgGOjCjhImlh9KTxvdni3CCt9dT8dYmmpOFS9DStGGvR1lgiNSInjwltinQz6bNf18aAUA08uTEwgSr9OujVLmcXsug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش کاربران خارجی به مرگ لیندسیِ جنگ‌طلب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/449464" target="_blank">📅 21:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449463">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
منابع عراقی از شنیده‌شدن صدای انفجار در سلیمانیۀ عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/449463" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449462">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxY7OjJlxl3LBqkpwgGEJqelFS29hny8v70PhKU7LxaKx8nheb406luPHXssocJ3YPkkDFs5bMsT5J1gEFcO3Up9dXbYid4Y4CV_0PesL3c0PWrNYyZ9iQS6tXIoX_lcsp_GAFANIggycWTODS8DfebDmY-ayPd5h7H0RsADzWkCJevYufFI7oq0lZBWf9YnJfk6Fa-8ZXjZoy5diGcX7JPlFoF1dAjH_q7jjTTPoCxgjpvGs3HuVxUIKFUjdWQmdAM96rblAw24MTKbz20Ru3eoCvs6oE_SXES7VEteIzfOt4TknBZWS7REkpYLc8ErZyDuj4LTZ5KZV3reK82hOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فناوری به جانِ جام جهانی افتاد
🔹
گزارش رویترز نشان می‌دهد تصمیم‌های مبتنی بر VAR، آفساید نیمه‌خودکار و حسگرهای هوشمند، بیش از هر دوره دیگری اعتراض بازیکنان، مربیان و هواداران را برانگیخته است.
🔹
کارشناسان معتقدند استفاده گسترده از فناوری باعث شده روند طبیعی مسابقات بارها متوقف شود و بسیاری از تصمیم‌های حساس، به‌جای آنکه با قضاوت داور در زمین گرفته شوند، به اتاق VAR منتقل شوند. موضوعی که به باور منتقدان، از هیجان و جریان بازی کاسته است.
🔹
دامنه استفاده از فناوری نسبت به دوره‌های گذشته به شکل محسوسی افزایش‌یافته و همین مسئله، جام جهانی را به میدان جدال میان فوتبال سنتی و فوتبال مبتنی بر داده و تکنولوژی تبدیل کرده است. بسیاری از مربیان و بازیکنان نیز معتقدند فناوری باید در خدمت داور باشد، نه اینکه جایگزین تصمیم‌گیری او شود.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/449462" target="_blank">📅 21:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449461">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b397539a5e.mp4?token=kUVlxeDd5Z1LZcweJZ-4g5rhcSE8OL5cfFDYz55qPfKUsEwmG9MsAJfDh4KDd_YQI8COrwqIvDtzAVdFsVerOtrGF08AMP_XZOaNc0C_uronCoDfbWwSP0No-JFfJGSbXnLFtxfWM1nMvjWT-BtOaqAlrnjBWGG3XSDrRiNirswgtIj2yhqim_qP57UkYRGrps1bVbfPNHVi6GDzw1H3qhvTwiJLBVm6CaYqepovuxyvRE9TiNgTp1DzKpAsT5HOx8POgw9gTPV1NqM2n8oVs6p_ySYXnKBCTVPKy59iWP0Okw0mUeWrUWvYoPgAKvEU1nfL_nHYOjixP1DRdIeMb4jcc0bwznM6_Shimh3VAKGz0CKVRE0gcBmuzM5pAesh5n9VxWLPGj1snnlqy65Arl2UaJDv8Ln8KBcOz3mmJivoTSfHeoJMsXknJeu7DdSkmJoquCqkx0XFbmnPCGNhsMLg9vQDz0hgw0R8RMIgCWHUverpknD_ok6sExpmJJCEKmROwyyy_-6uSD1zl5dxUT2emnJ7q23fTkV7jYFSh29eVt_7lY-pSL046NH_22lzbaJ1WtnhYCe5rBux7PYowrS8xUWoWZt6S7xrW0rYG0oCkqoNL41LsgBR5Y7xY6TNP7Tvp8wgqekGsp1AV9mppkEtJ63zQTnG0kHN0siL2jM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b397539a5e.mp4?token=kUVlxeDd5Z1LZcweJZ-4g5rhcSE8OL5cfFDYz55qPfKUsEwmG9MsAJfDh4KDd_YQI8COrwqIvDtzAVdFsVerOtrGF08AMP_XZOaNc0C_uronCoDfbWwSP0No-JFfJGSbXnLFtxfWM1nMvjWT-BtOaqAlrnjBWGG3XSDrRiNirswgtIj2yhqim_qP57UkYRGrps1bVbfPNHVi6GDzw1H3qhvTwiJLBVm6CaYqepovuxyvRE9TiNgTp1DzKpAsT5HOx8POgw9gTPV1NqM2n8oVs6p_ySYXnKBCTVPKy59iWP0Okw0mUeWrUWvYoPgAKvEU1nfL_nHYOjixP1DRdIeMb4jcc0bwznM6_Shimh3VAKGz0CKVRE0gcBmuzM5pAesh5n9VxWLPGj1snnlqy65Arl2UaJDv8Ln8KBcOz3mmJivoTSfHeoJMsXknJeu7DdSkmJoquCqkx0XFbmnPCGNhsMLg9vQDz0hgw0R8RMIgCWHUverpknD_ok6sExpmJJCEKmROwyyy_-6uSD1zl5dxUT2emnJ7q23fTkV7jYFSh29eVt_7lY-pSL046NH_22lzbaJ1WtnhYCe5rBux7PYowrS8xUWoWZt6S7xrW0rYG0oCkqoNL41LsgBR5Y7xY6TNP7Tvp8wgqekGsp1AV9mppkEtJ63zQTnG0kHN0siL2jM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خواندن زیارت امین‌الله در سومین شب بزرگداشت رهبر شهید انقلاب و شهدای خانوادهٔ ایشان در حرم امام رضا(ع)  @Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/449461" target="_blank">📅 21:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449459">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‌ اذعان رسانه‌های صهیونیستی به تلفات نظامیان آمریکایی در کویت
🔹
المیادین: رسانه‌های اسرائیلی می‌گویند «به‌نظر می‌رسد در حملۀ موشکی ایران به پایگاه آمریکایی در کویت، تلفاتی در میان نظامیان آمریکایی وجود دارد». @Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/449459" target="_blank">📅 20:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449457">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a41578c32.mp4?token=Sfb2Pkbl1RmLeIqCRe7Q5Q9t4M0jU1L361s3PVBo6POUTsq0kVxd7Synox2wNeFg4Rmj_wD35tspyHrPcUorHfp74Do4WLhNq5ryrRVieRmz6339DwlME8-ZBSav2MhOi-aTnF0faIshI3YYvh-qbgboc5-XSiMoYXcXfj9qR7ctpZ8gLUFmUi_v5BVw-6Oae8IZWAE6bJdRFgadcsPJos8BzfNm5_bLw-MACrCoWDBkvbQDZ-lpVbGMhvIN1zq-Sesfkw6YNGnksRH55uUuVI_DLMCImeQXhHWDCgiHR_n0ImOFxs2yE4Gk3fUCWISi2KX4QasduOS5uRrrdzjXMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a41578c32.mp4?token=Sfb2Pkbl1RmLeIqCRe7Q5Q9t4M0jU1L361s3PVBo6POUTsq0kVxd7Synox2wNeFg4Rmj_wD35tspyHrPcUorHfp74Do4WLhNq5ryrRVieRmz6339DwlME8-ZBSav2MhOi-aTnF0faIshI3YYvh-qbgboc5-XSiMoYXcXfj9qR7ctpZ8gLUFmUi_v5BVw-6Oae8IZWAE6bJdRFgadcsPJos8BzfNm5_bLw-MACrCoWDBkvbQDZ-lpVbGMhvIN1zq-Sesfkw6YNGnksRH55uUuVI_DLMCImeQXhHWDCgiHR_n0ImOFxs2yE4Gk3fUCWISi2KX4QasduOS5uRrrdzjXMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۳ پیام عملیات امروز ایران علیه اهداف آمریکایی
🔸
سیمیاری، کارشناس مسائل سیاسی: نخستین پیام عملیات امروز ایران، اشراف کامل نیروهای ایرانی بر تحرکات دریایی و نظامی آمریکا در خلیج فارس و رصد دقیق تمامی تحرکات دشمن است.
🔸
دومین پیام را ناکارآمدی اقدامات و استقرارهای…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/449457" target="_blank">📅 20:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449455">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کاهش ۴۲۰۰ مگاواتی ظرفیت شبکه برق درپی خسارات جنگ
🔹
مدیرعامل توانیر: در جریان تجاوزهای اخیر، بیش از ۲ هزار نقطه از شبکه برق کشور آسیب دیده و ظرفیت تولید برق حدود ۴۲۰۰ مگاوات کاهش یافته است.
🔹
خسارت واردشده به شبکه و تجهیزات صنعت برق از ۶۰ هزار میلیارد تومان فراتر رفته است.
🔹
گرمای هوا باعث فشار بر شبکه برق شده. از مردم می‌خوهیم با مدیریت مصرف، استفاده بهینه از وسایل سرمایشی و کاهش مصارف غیرضروری، صنعت برق را در عبور از روزهای گرم تابستان همراهی کنند.
@Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/449455" target="_blank">📅 20:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449454">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMPJFdVm7f6MMXV7aG7FGCxu-t-QYkpd06AjN7ZAwZhQYQz0ZJ4UJ39xhPwZqNcCUmem2mhCHhgbaQgXE5Ts3W-iimO9_SiJafcvYjPeXsRasnhcCQQC5t-kdcKWpz5s55fFNpO29yzmSQGGscwrrlYvUClO2qN9DZCEF6hLkaXcoDRSLyt-tVP907ni1uY4CUDAPvD0c2A4imaKgC74eL_AGXlCbICBW4t3LA-1o5lsOYfzeBOCRY4MNVF4Th8Xk8gfPrAg4Ch0sRhp7gl9greOF3bjiJnXOO7ng1b5SfT76hI26VIg5jIKwNiFX-meSUSHvv41lswM48wSJvyk4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رهبر انقلاب: انتقام خواست ملّت ماست و به‌طور حتمی باید صورت بگیرد
🔹
به پیشوای شهیدمان عرض میکنم: ای قتیل مظلوم! ای مظلوم سرافراز! ای بنده‌ی صالح خدا! حال که با چشمان اشکبار و دلهای شکسته با پیکر شما وداع میکنیم، با شما عهد می‌بندیم که مکتب شما را پاس بداریم…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/449454" target="_blank">📅 20:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449453">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌  خبرهایی درباره هلاکت ۳ نظامی آمریکا در حملات موشکی به کویت
🔹
برخی منابع گزارش دادند علاوه بر این ۳نفر، چند نظامی آمریکایی دیگر هم در جریان این حملات زخمی شده‌اند.
🔸
هنوز منابع رسمی، این خبر را تأیید نکرده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/449453" target="_blank">📅 20:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449451">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‌
🔴
وزارت دفاع کویت: ۳ پایگاه مرزی زمینی کویت هدف حمله قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/449451" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449450">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‌  خبرهایی درباره هلاکت ۳ نظامی آمریکا در حملات موشکی به کویت
🔹
برخی منابع گزارش دادند علاوه بر این ۳نفر، چند نظامی آمریکایی دیگر هم در جریان این حملات زخمی شده‌اند.
🔸
هنوز منابع رسمی، این خبر را تأیید نکرده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/449450" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449449">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRTuxOuoN7kZmNcgDMH9Kmxo_hZv3AmNXROPhfuBil8L6G4ByNMcATMUahWsgyAYK80OctPn0nmvsUYgPxJ7YSVVXhmag4WDHrVRX6vvtvl7uPCfSd4Z44qFEBJBtSmS9JCNtAOHWS49El0nJ5gN8HJh1CDkIIqqSCoassduNb13H_2kr_jPKw1a2wsXKA1I-4U5JwCPljK31YNixYjdyaqvMEWboB4tCRvwbCgi9_kmubp4OGGiULlIhmo5Sv8j7biEHVWgpJwUnFK4QYJxREkQ9dPipEZBDXaUpUuHJfC8gMXJooq45fPkB4BaahgkjbRvv7UleM32cm1jkhCAfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات ان‌بی‌سی نیوز از مرگ لیندسی گراهام
🔹
شبکه ان بی سی نیوز با انتشار جزئیاتی از مرگ سناتور لیندسی گراهام گزارش داد، نیروهای امدادی شامگاه شنبه پس از دریافت گزارشی مبنی بر «ایست قلبی» به منزل وی در منطقه کاپیتول‌هیل واشنگتن اعزام شدند. تصاویر منتشرشده نیز…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/449449" target="_blank">📅 20:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449448">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3e0923355.mp4?token=PLIxpj1PwgzAlplm0p230QTzmnC8h014Zvv4otF_hMCV4XTL_ZvS2Ch3iLsySGQsqmZRlqjjwMkPZ9vHM7Ko7iZT_E_xDBjqPJMuOUdgevvrghmeUg2tcIho_Wi6dvsAyfWFOb3G4KzPiYsKpkaDhxSm-G3CXBVyc7_kdkNRMTlBBwK3ke9SQEgkTJWNYO_av4ao2ftuCp1KmbiscbQ4tNTY4T9Fm4Md37loqLebP0eYQoXFh4U7LUakUN7TpoPI2na3GBfYe5J-IGzKNe5q4DWH5MZ6P__ehIBhuRadVNY13o98QfepWtjZYAKPpFBz4qkbUHY8r4zcOmb2a-inig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3e0923355.mp4?token=PLIxpj1PwgzAlplm0p230QTzmnC8h014Zvv4otF_hMCV4XTL_ZvS2Ch3iLsySGQsqmZRlqjjwMkPZ9vHM7Ko7iZT_E_xDBjqPJMuOUdgevvrghmeUg2tcIho_Wi6dvsAyfWFOb3G4KzPiYsKpkaDhxSm-G3CXBVyc7_kdkNRMTlBBwK3ke9SQEgkTJWNYO_av4ao2ftuCp1KmbiscbQ4tNTY4T9Fm4Md37loqLebP0eYQoXFh4U7LUakUN7TpoPI2na3GBfYe5J-IGzKNe5q4DWH5MZ6P__ehIBhuRadVNY13o98QfepWtjZYAKPpFBz4qkbUHY8r4zcOmb2a-inig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خواندن زیارت امین‌الله در سومین شب بزرگداشت رهبر شهید انقلاب و شهدای خانوادهٔ ایشان در حرم امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/449448" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449446">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiMNQ9U7j002raJU7kdR_vlmdyKcSllA8NLTTZPmGplH-l0NLIZ2r80gMh5rIf6I9tIZpTHPXRuSe730MmtXYy0dkjIV8tAVf9xrZs2rfJHggJ30-igQNkagWk8hosxDuSc6xU_7D9WngoS5gTjHrjCA4hDPUihKd9Gv2lLbTCBh440nmfgo67yWSV9pldtgDrblAgzNOetEjH2EIgdf3na30R4U8ymQS_Q3ScD0QUpvGMAAOt5Z5WZFHWWw_I7IhIV7234zaHNq8fYFo-MB2Ju0GgXeoVESqrW9ti_VFsRzIs_QEBveidM5xEhxffaSWBCyFeVfx_bsG8urRkFCjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارز اربعین از بازار آزاد هم گران‌تر شد
🔹
در شرایطی که قیمت دینار در بازار آزاد تا ۱۱۰ هزار تومان کاهش یافته، زائران امروز ارز ویژه اربعین را نزدیک به ۱۲۹ هزار تومان دریافت کردند.
🔹
کارشناس اقتصادی محمدرضا صدری می‌گوید که «کاهش فاصله نرخ ارزهای دولتی با بازار…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/449446" target="_blank">📅 20:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449444">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">📷
منابع خبری از شلیک ۳ موشک بالستیک به‌سمت منطقه المینا در کویت و محل شلیک موشک‌های آمریکایی ATCAM گزارش می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/449444" target="_blank">📅 19:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449443">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abb9e83072.mp4?token=TUzP0Q_TgTw1cvvO3ilzwf_F9IQokoEguMCRvO_yVbs5tI7B1FHYXH7rT3kess7mv20NlVQX83JSkC5eROHzEvYlp5SHDE9ZbP-Xou2yBiC_B3Fqwcg8Fpll9to9cUNLwYScGz4KbsnY7eXdVC6l3DLnHIpwS2ePcP10OolOEZ5LnyIyMasGxKH5gtgg7WmwTHFUXGHhSrMEuuLekLc7iwfHfFrKDMRhxKCAs1_Rjsxf_D6qnMfyOugHh5UftJsOy03_9TwP01u8o-suG6NC9H7GjMm8EP3LfQsOVA0Idlgt-la6j3kFVFUvpypTiWE2Y6bzKNDX2hQ2yrO8VVeRlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abb9e83072.mp4?token=TUzP0Q_TgTw1cvvO3ilzwf_F9IQokoEguMCRvO_yVbs5tI7B1FHYXH7rT3kess7mv20NlVQX83JSkC5eROHzEvYlp5SHDE9ZbP-Xou2yBiC_B3Fqwcg8Fpll9to9cUNLwYScGz4KbsnY7eXdVC6l3DLnHIpwS2ePcP10OolOEZ5LnyIyMasGxKH5gtgg7WmwTHFUXGHhSrMEuuLekLc7iwfHfFrKDMRhxKCAs1_Rjsxf_D6qnMfyOugHh5UftJsOy03_9TwP01u8o-suG6NC9H7GjMm8EP3LfQsOVA0Idlgt-la6j3kFVFUvpypTiWE2Y6bzKNDX2hQ2yrO8VVeRlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژنرال بازنشسته فرانسوی: تلاش ایران برای هدف قرار دادن ترامپ کاملاً طبق قواعد بازی است؛ در واقع، این خود او بود که ترور مقامات را آغاز کرد؛ پس اقدام تهران رفتاری متقابل و در چارچوب منازعه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/449443" target="_blank">📅 19:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449442">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsxgfvMgBc-PQs9f1zBhfABeeeOfaZtRXlY0dTrDqyCB-ToML4-KNvV7TSQ-j5yNq6A1IgsGZAUgI2cqQDRDWXv0LHyIK_QXxjZ76-ad06Q8xWuiLZFa2R_oLjqbRlDTMuoHej9_HS81zWe2dX8TRGervlTb1KT2qd7wr3X_aoswlZEsjg6u5EzlR--6erAvC3-gZCdxXAY4r8HtM4X6fZW8NHO2XGnH4zd4tqpXboZmXaUMMMu1EE6gtI8NFafRbhb9BpXWq_ckHKoXj5be0M1D2uz0eOEceujQzRNDNG2w7ayNaHeYnP_rTIxLwhKTKyL4SFDjiQHE1DDwhZQEGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرود اضطراری هواپیمای اماراتی در پاکستان
🔹
یک فروند هواپیمای باری بوئینگ ۷۷۷ شرکت «امارات اسکای‌کارگو» که از اوساکا به دبی در حال پرواز بود، پس از اعلام بروز مشکل فنی در یکی از موتورهای هواپیما، مسیر خود را تغییر داد و در کراچی فرود آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/449442" target="_blank">📅 19:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449441">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bca0ef46b.mp4?token=XHGoI9wcI81igrcYfTUKkPyJGbAH97_vnY9qgt9jjcutEz65Y3aPkzIWDkzGByHdtGeFiSeXSVw3k3pIy0H9HaWqlzpJ8_qR__sJOvme31EbrNeU7qhHCtcdNKmVEiRWlEO84CEQb7H63cr7-Re-QeqoVzhtYVraMOlY5OacKv3MIYjaHf52u4bU0JMmBiXEBIl2KDP_xui9LX9K8buf1EgV-1aIXjn2Y3BMKMrXMfmnvvFYhJ2VEZCN5ruhCKGIRTeFlgMl5wPFcLO2ojsQAQDW90OFIsUsizT1lx_RMjIrV2YpYWa5KHOFNnACOuhZ0rLIX-VYqZq1t5iJHl7_xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bca0ef46b.mp4?token=XHGoI9wcI81igrcYfTUKkPyJGbAH97_vnY9qgt9jjcutEz65Y3aPkzIWDkzGByHdtGeFiSeXSVw3k3pIy0H9HaWqlzpJ8_qR__sJOvme31EbrNeU7qhHCtcdNKmVEiRWlEO84CEQb7H63cr7-Re-QeqoVzhtYVraMOlY5OacKv3MIYjaHf52u4bU0JMmBiXEBIl2KDP_xui9LX9K8buf1EgV-1aIXjn2Y3BMKMrXMfmnvvFYhJ2VEZCN5ruhCKGIRTeFlgMl5wPFcLO2ojsQAQDW90OFIsUsizT1lx_RMjIrV2YpYWa5KHOFNnACOuhZ0rLIX-VYqZq1t5iJHl7_xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان رامشیر در جادۀ عشق به سوی کربلا
🔸
کاروان عشاق‌الحسین(ع) شهرستان رامشیر در پنجمین روز از مشایه پیاده‌روی خود را در مسیر آبادان به کربلای معلی ادامه داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/449441" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449440">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
شنیده‌شدن صدای چند انفجار در بندرعباس و قشم
🔹
دقایقی پیش صدای چند انفجار از سمت شرق بندرعباس و محدودهٔ دریایی قشم شنیده شد.
🔹
همچنین اهالی منطقهٔ مسن در جنوب جزیرهٔ قشم نیز صدای چند انفجار را شنیده‌اند.
🔹
ماهیت انفجارها هنوز مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/449440" target="_blank">📅 19:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449439">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3af5e768c4.mp4?token=dvjPUDWkdouHu2ghbLqzK-eCfX3nZp5rVozAEGcby--wbYftwlIEHCulOiblV6Eg-gN14SnWLpYRgS5D2Nmwxn3DTXwy11NpuOsLmbgILpKUz60Tt6_9RkRO--ee-7AgyoESiRdx2m7GRJsO-WPM0WPKxvu2lsU8rh9aEHEvUpC6_elK6T2uciGfqFVtptIcM0L7EWNlf5iU6qU620xEylxa3Ho0ETqR66S9Ae2hw2jMYOCLWS33MkPgJ6K_r29fhB8E9TfOOZ5teoFF9OUrMlHONgDUT-AajgdJNG7wiej1Pxdg8myQwHUuKQhfQRmHKKyceCfE4dKZzf03CdsnlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3af5e768c4.mp4?token=dvjPUDWkdouHu2ghbLqzK-eCfX3nZp5rVozAEGcby--wbYftwlIEHCulOiblV6Eg-gN14SnWLpYRgS5D2Nmwxn3DTXwy11NpuOsLmbgILpKUz60Tt6_9RkRO--ee-7AgyoESiRdx2m7GRJsO-WPM0WPKxvu2lsU8rh9aEHEvUpC6_elK6T2uciGfqFVtptIcM0L7EWNlf5iU6qU620xEylxa3Ho0ETqR66S9Ae2hw2jMYOCLWS33MkPgJ6K_r29fhB8E9TfOOZ5teoFF9OUrMlHONgDUT-AajgdJNG7wiej1Pxdg8myQwHUuKQhfQRmHKKyceCfE4dKZzf03CdsnlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
️مدیرعامل تامین‌اجتماعی: از میان ۲۹۰ هزار متقاضی بیمۀ بیکاری، درخواست ۱۷۰ هزار نفر تأیید شده است
🔹
بیمۀ بیکاری ۱۰۰ هزار نفر پرداخت شده و باقی پرداخت‌ها در هفتۀ آینده انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/449439" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449438">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnomjObrcSSftYbiSQgeedYMPWGMDSf4tICa3IWuIRCY3W9lRNOpndZZGAaALxv4JSkFl4A9Hr2j-FB1vp3hiFq-aiscqNp0PojxpDula7LY-HK-KKtf3jvdzY8yyyv498KoqyJxu8ZKOcJzkLiVd2RrduaTiCCokP4FMNStwNSQ8EjAv09y-8OlYn8uVMef18Q_QZO-StOTYlvKBvKDbtHK0YGovIFFW8p5C1KdM-lY6OXFXrp6-CyLDL9KNer1sfcgVwSrFr6P3Md1HgdpUvimxnavRPQzIgjhOiguTnlPBJs2VEZOPP0NynGN8VJGFEEqwPCRdrfrL3H4h6-PoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات برنامه‌های وداع، تشییع و تدفین ۲
شهید بسیجی در مشهد
دوشنبه:
◾️
مراسم وداع: همزمان با نماز ظهر در رواق امام خمینی(ره) حرم رضوی
◾️
مراسم وداع: ساعت ۲۱:۰۰ در میدان سلمان فارسی
◾️
مراسم تشییع: ساعت ۲۲:۰۰ از چهارراه برق به سمت حرم رضوی
سه‌شنبه:
◾️
مراسم تدفین: ساعت ۸ صبح؛ پیکر شهید سیدسجاد علوی در آرامستان خواجه‌ربیع و پیکر شهید مهدی هنرمند در مزار شهدای بهشت رضا (ع) آرام خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/449438" target="_blank">📅 19:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449437">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZyZo_axVixB0QvZgxTcadAFkfTC-_rNp3nWUtLgXq9FSHUD9y_lfOMSiUSc4UG3U8imIP9AB9J-i5cJLwMd3UuqsIo7djMtKtCVPHuSiQ7d8ggV8EuiasjjukhP8vN3afpdWCF516rR-N_Ri45lazadMRPwoz3taD9RbqYrCKmS6_Fu7QG_gWay_C3Ng93crvZNIztblel-zAO5INAkg7VU8xZ6CpmXkI4dQX_5j7UAUr4pmKuKRll7ydwL70EzF3jhW4oi0-K50otl2Wt2O4AdlD1cLThfC_oj1y_KpFkBTXsTwgcuV4Hs-p_fuf17TSKnQZAr7APdsoZlyRtKdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع خبری از وقوع انفجار‌هایی در کویت خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/449437" target="_blank">📅 18:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449432">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yrd4r6xaS4ODt7TjqnAv0J2nlIRHjBHqxofhIda0Siz3NP_Hi-RGFqqQUb9TavEVZqXv7FpT3raa9JKh32KQF5yMVMG2o-3pJm1zZrGEqVS772dJ1nnXp58C9pS38eMoiOlOt4Fp-EV8eTJruq4QX1Fj9Ksh11dpetP0r8ZeM1EzQVwvz70NAFA5dMSK1DlxtuL_yv0wmNpUK7uO8vdO0HftYSm0CDhrhwx4vRXdXtx0CuCSwyFf2XSE3D8O_QjbDCvEtZ7I49fvRVYkbALGqTCSyKMqAKeNXGMwwn_gzAvfZF7XvYzwiQJSKMDJIkDcmFk1t2zoI21bfgLTe8NGRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kjM1HjF-aZV0xdDX84AND2W-c3ywkdBBHOEhTAVlkrgj8u_abQ702FYUuCxF1j7CRr-zbylIi-BkaCHXWDXKKNYRFPJY3TXnHx584KBXY1x158DppmjPVaAOqRveCG74rAEwi6sB_F1QAwXwso0NKarzk7H_iKKmqQsSspAAc2KhsJ9_zxVn11ECZ2dJx4o2GqAfMC9wQImybKERW3oZ9T0zcy9NcYRTvK5E4Tar6fHbazdgETOiOUhQkyNSfc6XP1W1ivw7iIRixrCsADVlMwHqEjGOKhaXE_TvkN0b69ajzhWJDOEl8YzfE3hHdMUGw9_ihziPOb5B3g_b4ocmqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmT1aP4GL4Zi0gzxw8e7qRqKXbXN2lqbSc8EQFusJWe39I4H6VMa4sOIfPwAoF1m_68zekKTNuNOzjbfasvXb9lbm7125keF36bvgcn7P5IYdrQWLfJT46ryAwL07PdaYkNpL7lVdVeWj7T9gLdZmePd32sdjy9k7ntJz79VFcdQEJ5uQvelKXOulrzEaBWkXcefkZu5_0abTDnX-h4gALG-2BrzKhz6hG6sTQgqwttUvVNCNbTB-u3CP2trt7_6njxWcJiI3zWW35ysE7l4e6L4fPG3_A9jxDPVCxp-bzwrKrKVxV9lwQy4sJosFraijWkSfNjjdv1ZmRpi_1OoEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UGgSXTkm87gx1_GCznQBpWcCfdfUtYajRsbW5CuqIg93P3f0uEYeks7rvoLvLLiwnyo86vCUyxhhPR88f7QZ__LQLwG1tYT4HcuPEFckAgqNIwnMYmZ0aEpMLcOps1KlyhSgBhI98MmfT7GFbotgCEFOjP2ddiX-FdCzVo-eq9YUi8LCY85EB0-qWSofz5UXcA3SKAv1WHKeKsYJGKTFyvqa7X-GiSr2j46IVFy5_IlcRhpDN5nBoy16Icr8JWWVL_ADvDfYYfJ_q8TuPrgWMCON2nzsWihOpJAiTGtDdolQiqA8eIwN4mqdYk9S_Fi3FqPT6V02leHGiJOB0h8WRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KRlTitGqq9UA8lFBQ1A0Kr-WBBwuCN-aCKHOwI8radaWhXp-3Xsc9fBGHfQhXb9zcwKN7E7RRysKigvVvC_IWMoAltdWZFgoxrPD2UXtKF9SNcNGkTQMb5sst5Gsa0JTvmcoIe-_rILuPXGj3MXEvvvJOcdX3RY7TBAodjb5e2Z36S2su-x_rNKifjtuztWM0R5_AnakyCZ3S98p1uTJkZk1SAFGW_RRnoQuQMuEKuKv3XH6t15TR-v1ZjP97594CtdNFAOcEmnRWGrCW6YCHmZvb-KnYPgMmS5OGKpBzQtQPrB0dB-Kn5VAktbjZhD846T73u9u5dMG7NNQI-vu4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
این عکس‌ها بهترین‌های سال ۲۰۲۶ شدند
🔹
برندگان دومین دورۀ مسابقه عکاسی هوایی بین‌الملی سال ۲۰۲۶ مشخص و عظیم خان رانی  از بنگلادش عکاس برتر این رویداد شد.
🔗
مجموعۀ کامل این عکس‌ها را از
اینجا
ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/449432" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449431">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
منابع خبری از وقوع انفجار‌هایی در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/449431" target="_blank">📅 18:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449430">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GV2cpxeMUVGJBh1x1QTDN-qxFFgg9LNt1nZpmrSwLb_EmhsTNPq9HeWCDj5pKC_WoPdrt3yWSPMOMD8PFv6jxmEMpkKN5cb-_BmpJ65yJhpf7mtkQ7kUVhHZspLRXZZNb1mwu7BFJfSQtFMZHkoDmizeFNHwS-LlSo59QVMrZqytP42sL9NCL0BFmTH-TXAeTarlbwAtTHRtEQNJpOoxuT5lm1xvCaVv6S5a9PCIXNYXxkSkjaEAV-xJQjsySKFKdyDeN3KN2XERbF5R4syzxUrSmhdi41qcOSw0ZG_DVflTUZVy5CYfFhgLACi4D3s6HDJ5CM3zB7Ggin8LOMEbCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبت‌نام زائران اربعین از مرز نیم‌میلیون نفر گذشت
🔹
معاون سازمان حج و زیارت : در کمتر از ۲ هفته از آغاز نام‌نویسی، تاکنون بیش از ۵۰۰ هزار نفر در سامانهٔ سماح نام‌نویسی کرده‌اند.
🔸
استان‌های تهران، خوزستان و خراسان رضوی بیشترین تعداد متقاضیان را به خود اختصاص داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/449430" target="_blank">📅 18:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449429">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjvhVCQKSoYiozJ3NrSBh2EFmZgAnIR4By1b-lL2oaDEo3nE5B-NQE_h1SwSvXruaXiEwee5mxvsTbh35lZQIMV3-OxgMaJlfDCtF46MUqJYZHuhz8qfURJyuiD3R-HRlX7v4N3D5cJm0jWB1rk64r7HaKK1pZfo3n8v0EoRHSOSSQwKXOb2muYs4mccFEkO9xxHvuk819UfxpAHPXzgRkrWyqqAUg-TaronvyI4-206jRMbYjIewbmhtJZtMKDuDmsdVerDvQ7cBfBdG6uRKrQKY4tSh3cGFduUF9FURvJThkDefG2_-jNMsfRpx3UhXruQf938yBA0Y0qdGIdgsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف یک محراب تاریخی در پاسارگاد
🔹
اداره میراث فرهنگی شهرستان پاسارگاد: یک محراب تاریخی در جریان عملیات ساماندهی و مرمت کاروانسرای محوطه جهانی پاسارگاد کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/449429" target="_blank">📅 18:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449428">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27759874bd.mp4?token=ZGGJmVJNU6OzsQ0LxF9KAmjm8oWsvIQ2YNRxGOyuv8q2aBUlzKDdxEYdCHeZ_82AgRIiJrRWVLetG6BKMIfOhd-fEd2V5PZDXsWw6peKxfyE9HjAQGMx-QNh99jc57Fle95jHTJwnbCUqcR_1W_0NVNf6M2UMXj7aV2ALg09Oc1-5pVDZDDXuvjw0MadPNpZpAZzBhAG3m7lj1-iMLMo8mI_vrBaepkHmPMg2v2f4aSbTchPByEr5sseejqfDzhziBR2X_4gpQibLXX00I-c9eUI3q8QnMutZgnkmHZd3TgMOonSp0js4JmuH_H3qAraZdxNtS-bdCjjbsskkX-eZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27759874bd.mp4?token=ZGGJmVJNU6OzsQ0LxF9KAmjm8oWsvIQ2YNRxGOyuv8q2aBUlzKDdxEYdCHeZ_82AgRIiJrRWVLetG6BKMIfOhd-fEd2V5PZDXsWw6peKxfyE9HjAQGMx-QNh99jc57Fle95jHTJwnbCUqcR_1W_0NVNf6M2UMXj7aV2ALg09Oc1-5pVDZDDXuvjw0MadPNpZpAZzBhAG3m7lj1-iMLMo8mI_vrBaepkHmPMg2v2f4aSbTchPByEr5sseejqfDzhziBR2X_4gpQibLXX00I-c9eUI3q8QnMutZgnkmHZd3TgMOonSp0js4JmuH_H3qAraZdxNtS-bdCjjbsskkX-eZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حکم اعدام ترامپ و نتانیاهو باید صادر بشه
🔹
اگر میخواهید به جمع خون‌خواهان رهبر شهید اضافه شوید
اینجا
کلیک کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/449428" target="_blank">📅 18:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449427">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1bff11a8.mp4?token=Bq6skfv_Kzx09Vte6slJI0OyAHacD2t9zwj1jiMeOfUu-Gi_7DuFB9ndTolb974KqpceuAEiXK8IRgEeRwlHKLsc62skZkdtTSmknpowGXCLOQwNhWhHEcT5hnEgu836-QQ8KZdlFIeDiV0QZmlZm7tym5QWcp3MJbafMNdO7GWC6wONgo1ec_kq9NOgUlT9f0THqEVaZq0pJ3ietB8IUgrcdNGqeBa_q5HrmujY2iEi2QlG70A-TWQGvPGxKHaCs7Io5ICy_PfCRlkjw0AGD_mCzGbGjmuFwreyGig_1K_CNZIJEUXANashJi9QslOdJgwywij7sl17NopsP5rJkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1bff11a8.mp4?token=Bq6skfv_Kzx09Vte6slJI0OyAHacD2t9zwj1jiMeOfUu-Gi_7DuFB9ndTolb974KqpceuAEiXK8IRgEeRwlHKLsc62skZkdtTSmknpowGXCLOQwNhWhHEcT5hnEgu836-QQ8KZdlFIeDiV0QZmlZm7tym5QWcp3MJbafMNdO7GWC6wONgo1ec_kq9NOgUlT9f0THqEVaZq0pJ3ietB8IUgrcdNGqeBa_q5HrmujY2iEi2QlG70A-TWQGvPGxKHaCs7Io5ICy_PfCRlkjw0AGD_mCzGbGjmuFwreyGig_1K_CNZIJEUXANashJi9QslOdJgwywij7sl17NopsP5rJkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«عمو لیندسی» که امروز مُرد که بود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/449427" target="_blank">📅 17:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449426">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BC1njZ74pYCXI5ukckkBTdnsPSv-jLh1NmaZvvYu55IWeL2874Ip2pGq41Q2ljtzWH42zO8cYcJbK0pUOdjBghkkJkPiF6XTt8aR2HxQB8by6ME916CnZgDr6HWQ2mA3-00ZMPj81jj94eK4W-FK3EUwt460aLGdc8hodZr9Dk3ubBjEKVa3CFxtfpGwSSKbDPmKXtpWBBdK_o13-2oUN559EZj1Ti_H4f441giTbpkzCPc5FmFHDOlMdZ4w_-vzTG1TXkamMeoICZcXu4WKdOMWDjd1Tr9RCGSYUMRK17M7qi8-KXVS0v6Po5plBKp9w4JopdV4bmoLoJ-2ygM5qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین چاپ بافت زنده در فضا با موفقیت انجام شد
🔹
شرکت زیست‌فناوری «آکسیلیوم بیوتکنولوژیز» برای نخستین‌بار موفق شد بافت‌های زنده کلیه و کبد را با چاپگر زیستی سه‌بعدی در ایستگاه فضایی بین‌المللی تولید کند؛ دستاوردی که می‌تواند مسیر ساخت بافت‌ها و اندام‌های پیوندی در آینده را هموار کند.
🔹
نمونه‌های چاپ‌شده اکنون به زمین بازگشته‌اند و در حال بررسی هستند. این فناوری هنوز تا چاپ اندام کامل فاصله دارد، اما می‌تواند در آینده برای ترمیم اندام‌های آسیب‌دیده و تولید بافت‌های پیوندی به کار گرفته شود.
@Fransa
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/449426" target="_blank">📅 17:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449425">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPeeQi5nZtB0pz1o7XC-Liy4hZ53kjQuAPVCUtwIbnN0sdUatHiNx_z2gBncyIlPX13oNOXQfn8zJUeGee4hU-HxTJJFJtF0rfwP4Zip5yUXZoHli-wrs9imU3p5Igi7PoHDKBd6N9m52qQDWQtJzD3HMX6070snhUmmMg7CqCx_fKvov0vrftxXch8zgwRJELmArcY0WayDmaXOO4TqgnXI093hP7p4iURaEZOaifZ4YNqwUQPDTHaMB32YQ3BAcPsIE_-jq5a4we4LCrOtKxx9T4YqgHHzE8KaIT9OXGETWpdcvXxgHv_wX6dlL87L_Wp3BlATYBM64yq-jg_b9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توهین مجدد ترامپ به ایران
🔹
رئیس‌جمهور آمریکا دونالد ترامپ در مصاحبه با ان‌بی‌سی گفت: ما دیشب آن‌ها را به شدت بمباران کردیم. آن‌ها آدم‌های شرور و بیماری هستند.
🔹
رئیس‌جمهور آمریکا ادعاهای خود درباره توافق را تکرار کرد و مدعی شد: ما دیدارهایی با آن‌ها داشتیم. آن‌ها دیروز یک توافق را پذیرفته بودند. یک توافق عالی برای ما، بدون هسته‌ای، بدون هیچی.
🔹
او مدعی شد که ایران «از همه چیز چشم پوشیده بود»، اما پس از جلسه، حملات را از سر گرفت.
🔹
ترامپ در حالی به عدم پایبندی ایران به توافقات اصرار دارد که آمریکا حتی به اولین بند یادداشت تفاهم عمل نکرده است.
🔸
نقض مکرر آتش‌بس از سوی آمریکا با واکنش قاطع ایران همراه شده و نیروهای مسلح ایران ضمن هدف قرار دادن پایگاه‌های آمریکا در منطقه، بسته شدن تنگه هرمز را اعلام کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/449425" target="_blank">📅 17:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449424">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wn714pM2xii0diKyjYlbdRIKtcC7Q6BLr6PWWFWXl79lVI0egUaP4uPsd_fHe2uU2pgXGTQ9rehSZOR6ASSe6guk4Dp_cOfS1uvFwb65a3EQUtRJvrx0bGPR6CfzzTJCjMWW92g3A7tCn4ZlMMuA4w6YgLzLCYB6BBVgBqAwjjTLHpuPt1dt4Skwh1RSuZzgUbmkMxsXh2oJcuCWuLQ-Dps8oG9eSHovL2t9RZ7TLJJrqu5c9bmc5h7cvU5VSNg0qGmSjS3rY3-bAC2oxXSg_pgQcieHC39cGc6E8VfWErIt7_ch5l32lOIkVwBqLxR0_CvTPRb7p_o_EJewY_KIDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوت امیر سابق قطر
🔹
دیوان امیری قطر، نهاد عالی دولتی این کشور، روز یکشنبه اعلام کرد که امیر سابق این کشور شیخ حمد بن خلیفه آل ثانی،  در سن ۷۴ سالگی درگذشت.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/449424" target="_blank">📅 17:41 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
