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
<img src="https://cdn4.telesco.pe/file/nf9YSxSbNLBdPe-iswn91_VEdqkZ5EbOZg59p21ymn3w63JluuuUNIui75zALQ9XWa0ljKCom9LMlL6xnmJKeOxOb7sHCmrPGF3kMTO0wd02wKi8qodDNjBf6o8_ANgtHlOrngk7rIW06KdL6Pr_D1ocSJVB4cBzGqVKFtXS-XdiU9zraGgGYs5m-mIaGYYhs-MiieZ-AXL3HUqdqNLHMECdJjE8sbb3bAzDFQ-ERTVBo1h3uPAZQMP2dByaccwy2Jdya9h207-oRiCIzJ2OMnrzONsTFvBPHiKLDBUlJPBbAwjvG3M-hSW1vdzVWJxYx-IQVFJPTX2ZEf-j9dGCzQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 332K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 10:19:16</div>
<hr>

<div class="tg-post" id="msg-16186">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5553987fa9.mp4?token=dGV98CL5XhV468ROz7YdyAZL5RYmusSDK07wXseY0HfRrgKGS28XbGwO9vIkrPZG4P9ZZffXBRF2y6Rgj3pX_vCi5Y93Ilh1mN14cC8_DgOe8iLdcSftKwipj1WGLB4O55B7HCDRjtoGGO7FyyhvixnN-BUUP_XHWLYcS5vpjhYfzZp3tGWpplFMZp2R_WG3YFwJWuMRNyDO305OQ0Qyg8D06Og0RTBvrTh2Wkhmn1y6tKJ5YPEB1JLzdGWndQ2ohwvFUpDNGWP9P2nx7c2v2hKr6WktSYh19ystu5lbAmlQ6M8xYKtRXwXTXrdDMT_O1iR-r0NErXmqNnOYSEWrcDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5553987fa9.mp4?token=dGV98CL5XhV468ROz7YdyAZL5RYmusSDK07wXseY0HfRrgKGS28XbGwO9vIkrPZG4P9ZZffXBRF2y6Rgj3pX_vCi5Y93Ilh1mN14cC8_DgOe8iLdcSftKwipj1WGLB4O55B7HCDRjtoGGO7FyyhvixnN-BUUP_XHWLYcS5vpjhYfzZp3tGWpplFMZp2R_WG3YFwJWuMRNyDO305OQ0Qyg8D06Og0RTBvrTh2Wkhmn1y6tKJ5YPEB1JLzdGWndQ2ohwvFUpDNGWP9P2nx7c2v2hKr6WktSYh19ystu5lbAmlQ6M8xYKtRXwXTXrdDMT_O1iR-r0NErXmqNnOYSEWrcDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قنبریان سخنران صداوسیما: اگر ترامپ را قصاص نکنیم رهبر فعلی باید بدون شک تا ابد در مخفیگاه باشد
@withyashar</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/withyashar/16186" target="_blank">📅 10:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16185">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oulF2vLsEoKBB4IBnnjiXKDzLqe3LyYTF2oTFIkP4fwTrcgncLIJ465BoBkUcISlBwAu0CYjVHg02od0yCdLHygZ7u5Mmmt_UTgOM9e7_5t-evDlZH0s_hoA5bcFZBSyQSFBjqkUlSxv1O_M8ymG_dx9evIvMtmi7gdSylTFqpdXtFcGwcFClpQnNzhEgcgNpDE79xNwvsV24CuA-hpeh9IytNi1CKnA83P0qqR55ehqSBu1ktm-sVBm8jo8FoPSmtRO0KxLVRf-kDQQk-W7-73xVgaezVVZoi6JDhITT-uxPhFBNN2Ay2aHKhaQE7XZDtTtXWqGmPM_L6bj8di4bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو نیروی سپاه پاوه ترور شدند
روابط عمومی سپاه استان کرمانشاه:
طی اقدامی، افرادی با تیراندازی درب منزل در شامگاه دوشنبه هشتم تیرماه، «برهان کریسانی» و «خالد خالدی‌نیا» دو تن از نیروهای بومی ما را هدف قرار دادند
در‌این عملیات خالد خالدی نیا بهمراه خواهر و خواهر زاده‌اش کشته شد﻿
@withyashar</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/withyashar/16185" target="_blank">📅 10:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16184">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اسناد محرمانه هک شده مادربرد و تراشه جدید آیفون ۱۸ پرو مکس فاش شدند.
بیش از ۶۳۰ گیگابایت اطلاعات از جزئیات کلیدی آیفون ۱۸ پرو و آیفون ۱۸ پرو مکس اپل به سرقت و فاش شد.
رویترز : فایل‌های حساس شامل فهرست قطعات و تأمین‌کنندگان، و حتی عکس‌هایی از مدل‌های در دست‌توسعه آیفون 18 پرو از طریق نشت داده در شرکت هندی Tata Electronics توسط هکر ها روی دارک‌وب منتشر شد.
@withyashar</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/withyashar/16184" target="_blank">📅 10:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16183">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حزب‌الله:
قمار سر توافق ننگین بی‌نتیجه است
حسن عزالدین، عضو ارشد فراکسیون وفاداری به مقاومت در پارلمان لبنان:
صهیونیست‌ها مکان‌هایی را در به اصطلاح
مناطق آزمایشی
گنجانده‌اند که اصلاً جای پایی در آنجا ندارند مانند شهرک فرون.
دولت لبنان اساساً خودش را فروخته
و به دنبال فروش قدرت لبنان است.
پرونده لبنان همچنان در اولویت ایران قرار دارد
و جمهوری اسلامی ایران این پرونده را به هیچ طرف دیگری واگذار نخواهد کرد. معادله‌ای که تهران ایجاد کرده همچنان پابرجاست و ادامه می‌یابد.
@withyashar</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/withyashar/16183" target="_blank">📅 09:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16182">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شروع حذف‌های هدفمند؟
دریادار دوم محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه، متولد ۱۳۵۰ بود و در زمان سانحه رانندگی و درگذشت(دیروز)،حدود  ۵۵ سال داشت. او تازه سه هفته پیش، در روز دوشنبه ۱۸ خرداد ۱۴۰۵ معادل ۷ ژوئن ۲۰۲۶، در فهرست تحریم‌های اتحادیه اروپا قرار گرفته بود!
وی در ماه‌های اخیر در سخن‌رانی‌ها و مواضع مرتبط با امنیت خلیج فارس و نظارت بر حضور نیروهای خارجی فعال بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/withyashar/16182" target="_blank">📅 09:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16181">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دیوان عالی آمریکا امروز سه پرونده سرنوشت‌ساز برای دولت ترامپ را تعیین تکلیف می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/withyashar/16181" target="_blank">📅 09:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16180">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jv-O2nvAbpFKtTC-Uzh-SoSGskVGi_4rscfIKvS1AEzeSVftZru4cIUwZdAu20vYdITSIqd5XvDB5HDEjFMPHFjs1RTdd3-QKwpnswhktTl-MckFcdn2oUByrq3C5Nu5qMxfs_-s2iAFwcINL1ZpcwTflRN17RxtODPiDH0nCDJc4kXjTo1uVZ-1Ap_UKzjW8qSv7jpkOeaHKfnU9kKcfKOzm7idsijVgSh3EW9wg5nuR-A4fvAZYYP6fUvDS2BWBkVPVt0tjTd6HJtKIT6PyrHUSsHh8kq1-CjBMpp-d6khQ7VLm1rGnL8yICfyPhTE4u-5t4KtuOFE9pHa66r2hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید روزنامه همشهری :  انتقام قطعی است
@withyashar</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/withyashar/16180" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16179">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">روبیو: احتمال شکست مذاکرات با ایران وجود دارد
شبکه «ام‌اس ناو» به نقل از منابع مطلع: روبیو در جلسه توجیهی با اعضای کنگره آمریکا، گفت که دولت ترامپ هیچ توهمی ندارد که مذاکرات با ایران آسان خواهد بود.
روبیو به کنگره گفت که احتمال شکست مذاکرات وجود دارد، اما دولت می‌خواهد به مسیر دیپلماتیک فرصتی بدهد.
@withyashar</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/withyashar/16179" target="_blank">📅 09:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16178">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ به شرکت‌های نفتی: «قیمت‌ها را کاهش دهید - وگرنه مشکلات بزرگی پیش خواهد آمد!»
@withyashar</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/withyashar/16178" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16177">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Me1GJsoXbzPAUlZ_Ml8fBA2rYxQ97gudWvOAoyyieApJj3F4tuUwk9IQtDln2IbfNnPuOC-4lPOL56q5PHlb4XpMqep0I-Kvqsz2qJKM14iiGx6aw2FHC9BUYRyokmtCEMOhJn9Q-IQxtSw4jYg0xhF_dIdtnTpjEmuL1Cd0ukrYHLgCE2cmycbjPPEgSwfTbXfD3QJnmSjMk4zuB6tJtfm1rD76T1bxb8b9w3BS_b9fx4Inovwc3ln01nnABv1CEa7m-NTUjd27_faM0eDApkRHAWSU9pmip1E0S48OiPMBlzofxvaJx_TUuRXd3-GawrZPv9mZ-b0BMh45Jk9m-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار هدفمند در موناکو فرانسه
۳ اکراینی نفر زخمی شدند که حال دو نفر از آنها وخیم است.
پلیس در جستجوی مظنون فراری پس از انفجار «هدفمند» در موناکو است که شامل یک وسیله انفجاری جاسازی شده بود.
@withyashar</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/withyashar/16177" target="_blank">📅 08:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16176">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حمله مسلحانه به ایست بازرسی پاوه در کرمانشاه باعث کشته شدن 3 سپاهی شده که یکی از این افراد نقش مهمی در قتل عام مردم در سال 401 داشت که به هلاکت رسید
@withyashar</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/withyashar/16176" target="_blank">📅 08:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16175">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نتانیاهو : اگر از غزه خارج میشدیم، خامنه‌ای، نصرالله و اسد الان در قدرت بودن.
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/16175" target="_blank">📅 00:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16174">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nj8T26SDxojPQtXjsgEuBgsjnGoylhbla0tYUpK2MwGJw_9zN1GAOjqJiWpf465jZHlwnaMF9dPxnWnvZM9LA3vlAjkADA0XH6Vz9XdP40P7PxEq5a_RkPY26FDgbopiQN1QBO7zuvaGC0Cr1CxJ8hxtxuRCWvL9eqvmv9KYKUuejuczoaMdtvVl4QZpBNw6bj7dvUij5I3E5J28V8j-k2dNzidtlwT_tseC-2o6AhYqa3_tG5x5b_Wu0MIf9Z9GOhY6mBw4qhUrvIMmLr5sFgDMhrxvT6XPrHyi3NRIKgArPrmOux0SdRfywMJol7Sqm6lvZEUClE-nfeXKFjVv6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات سنگین اسرائیل به مواضع حماس در خان یونس
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/16174" target="_blank">📅 00:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16173">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCBdvTbH-PUlQO_XvqWWWnPxwN1HsI1cVzJP0v9Tkdph6WP5-QSr3H8fysdw-6ksO23qoAmw4Go7GAj1lOSlPJIHz89iTnd674Z2OhLIoRHUPRtT3uFUfJIiXAQy77_8YhV-pB08I6nfSvGB297uev3zxYRyxFQE4dvYkfu4zKoMx6ovcAzoVrPdQsNz9wm8vHIZ0V9Z8OFdbIkGOs5VyWamxm4y443_yVPwdkrZWzNDMzEMZO4lqU66t25KRqLu83JimZblZ4Fx5BQRoQspo2Oz0cDE1ipCSR4KZrkpTzpSrM0f7Y4vVeSEXU44xMBBxI0q6knnXS-Q2R6cmbtBdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید باور نکنید ولی؛
امیر قلعه نویی قبل از شروع جام جهانی از فدراسیون فوتبال
۱ میلیون دلار
پاداش طلب کرده بود و فدراسیون پرداخت کرده
۱میلیون دلار هم بازیکنا و سایر اعضا دریافت کردن
اول یک میلیون دلار (۱۷۰ میلیارد تومن) رو گرفت بعد نشست رو نیمکت.
نتیجه: حذف در مرحله گروهی در آسان ترین گروه.
@withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/16173" target="_blank">📅 00:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16172">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وزیر دفاع اسرائیل:آغاز جنگ مجدد با ایران ممکن است در عرض 2 روز آینده رخ دهد و ارتش اسرائیل آماده عملیات و هدف قرار دادن اهداف در ایران در صورت شلیک موشک‌های بالستیک در پاسخ به نقض‌ها در لبنان هستند،اسرائیل در حالت هشدار قرار گرفتند.
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/16172" target="_blank">📅 23:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16171">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">موافقت عمان با اخذ هزینه خدمات دریایی
وزیرخارجه عمان تفاوت میان عوارض عبور و خدمات دریایی، زیست‌محیطی و مالی را توضیح داد که می‌توانند به‌طور داوطلبانه با کشورها و شرکت‌های ذی‌نفع مورد بحث قرار گیرند.
او افزود که برخی خدمات ممکن است شامل افزایش ایمنی ناوبری، حفاظت از آب‌ها در برابر آلودگی و ارتقای آمادگی برای مقابله با حوادث یا شرایط اضطراری باشد.
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/16171" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16170">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50a48fb273.mp4?token=IPlvDmEJiAOv3tD2wauy7I3_cZnbfzGXWoGBPdKKZwl1EcRuUab3kPrbVngOW1rtDmIXzOCjdQTZI6_d_JD0TZmknmxNt7eVrRg_hPXABSPHCt-ROn1JvV1WxwGrP942NKIi5IwN06VAq6zpAoWEtm2KQgqnCJf3V7VVs84MgIstX42uS1-NRtg7avdrf_Jdmvvxk36cDWlPFVSBmrJkzF5DCqgJDKix6ORb1ieeDDwla6p3uwxdfE-lUOYLB18r841xCIlO28RTbFa2Z_HR_5VM06atLCO1gpURdT1NNCie0IqkmSyyMBcb4jOvSiluF8AlXjIhTFp5VuU4K0zt5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50a48fb273.mp4?token=IPlvDmEJiAOv3tD2wauy7I3_cZnbfzGXWoGBPdKKZwl1EcRuUab3kPrbVngOW1rtDmIXzOCjdQTZI6_d_JD0TZmknmxNt7eVrRg_hPXABSPHCt-ROn1JvV1WxwGrP942NKIi5IwN06VAq6zpAoWEtm2KQgqnCJf3V7VVs84MgIstX42uS1-NRtg7avdrf_Jdmvvxk36cDWlPFVSBmrJkzF5DCqgJDKix6ORb1ieeDDwla6p3uwxdfE-lUOYLB18r841xCIlO28RTbFa2Z_HR_5VM06atLCO1gpURdT1NNCie0IqkmSyyMBcb4jOvSiluF8AlXjIhTFp5VuU4K0zt5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در‌ مورد کمونیست:
آنها مردم را به خاطر تعمیر ماشینشان دستگیر می‌کردند.
این حتی باورکردنی نیست
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16170" target="_blank">📅 23:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16169">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6615611a73.mp4?token=WydA0Ebhcd7TrJBxZ3yrpZ3LzgWnTFUuO9EL4i163hzfBBIOnC1JIVIwm416WNgQEsYNkNYmd1VoUCH6aAhvh_aCQirULAJyS4t8_za3RD3itCdtyQW65HxmQEQ5E6_yWCR7uC_4B96eBXWajCx1xm6fXnIYMd_zc4389lqIj1I8BSityBLkYslVHx8NiwOAi7g7MnzyfA1c7XkZvrq1PQet0Ggw4UFjrXCb5y9Px_54wD8uxNgcpdBqemKxXBDyMYQMWljFcpD49pavUwJBvauOeOG3_DFKCV-eubR0_lSJv1JjBM-PCAPwoe7ca0Kr4RpAoy9bV0uJQUaQyuellQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6615611a73.mp4?token=WydA0Ebhcd7TrJBxZ3yrpZ3LzgWnTFUuO9EL4i163hzfBBIOnC1JIVIwm416WNgQEsYNkNYmd1VoUCH6aAhvh_aCQirULAJyS4t8_za3RD3itCdtyQW65HxmQEQ5E6_yWCR7uC_4B96eBXWajCx1xm6fXnIYMd_zc4389lqIj1I8BSityBLkYslVHx8NiwOAi7g7MnzyfA1c7XkZvrq1PQet0Ggw4UFjrXCb5y9Px_54wD8uxNgcpdBqemKxXBDyMYQMWljFcpD49pavUwJBvauOeOG3_DFKCV-eubR0_lSJv1JjBM-PCAPwoe7ca0Kr4RpAoy9bV0uJQUaQyuellQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ما از نظر نظامی در حال پیروزی هستیم. به نظر من، تقریباً از نظر نظامی پیروز شده‌ایم.
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/16169" target="_blank">📅 23:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16168">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82e78ece16.mp4?token=qYKXa1zfSA7HkHQJO3puczJ4hjjQ9AXNMu1RMp3msxu4vaVq05GC6fudfIWLvslNEqHtvEJudZCGG37VUT-Nr2eQLwaVXQ6QO95Y1Nh6jwpyAARAkmRQp0YpR_MfIIya4NrGXJgmWm021WCgoOVH08nADADEAxa6BISbmD09eZhd9gQSuT1D4q_ZjP1LH-su6lxoIqL2UC7Wac_YsMB1tcwKEZvPSyhNuzjW6zceOqORebEzBavPE8ybe5WzyGjUgNyjVxndgY6ZBJvsEAx5px56u6LH-srfbjAqri_Opz2WAwm87bjSfNlblPKaVdqJpzjo3S3jNMMuKBcpJmFIXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82e78ece16.mp4?token=qYKXa1zfSA7HkHQJO3puczJ4hjjQ9AXNMu1RMp3msxu4vaVq05GC6fudfIWLvslNEqHtvEJudZCGG37VUT-Nr2eQLwaVXQ6QO95Y1Nh6jwpyAARAkmRQp0YpR_MfIIya4NrGXJgmWm021WCgoOVH08nADADEAxa6BISbmD09eZhd9gQSuT1D4q_ZjP1LH-su6lxoIqL2UC7Wac_YsMB1tcwKEZvPSyhNuzjW6zceOqORebEzBavPE8ybe5WzyGjUgNyjVxndgY6ZBJvsEAx5px56u6LH-srfbjAqri_Opz2WAwm87bjSfNlblPKaVdqJpzjo3S3jNMMuKBcpJmFIXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: نشست دوحه شاید مهم باشد، شاید هم نه؛ خواهیم دید
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/16168" target="_blank">📅 23:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16167">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کانال ۱۲ اسرائیل : وزیر دفاع اسرائیل، کاتز، دستورالعملی از ارتش اسرائیل بر آماده‌سازی «عملیات آبی و سفید» برای یک کمپین احتمالی علیه جمهوری اسلامی اعلام کرد و تأیید کرد که اسرائیل تا زمانی که «خلع سلاح سازمان‌های تروریستی» انجام نشود، مناطق امنیتی در غزه، لبنان و سوریه را ترک نخواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/16167" target="_blank">📅 22:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16166">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">برخواستن جنگنده از مهرآباد
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/16166" target="_blank">📅 22:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16165">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a561d8b149.mp4?token=OCDwFuwEZ8RusyRRSeDIwFaC9Y_a-WISkEXPkI3qXrBXu6cyehGS1mMj4tHOwsm0CaXXBseQEOomKuLenJU8MGnibJMaUF-d0moET_BzPx0DsFaJB-gYU9gRkrJLoQH0jiBJghpZ-8NIWat3F7bhEJBwssS_8zzzcrQ_Me4es5q2SsW1HMJxzGZWPzE8Je68xJPCJD5N-nv28oyHwTDXNOGGUX1K1NDS0S7B6C_NyU1i-RIzF1ILiN-Z0EiQninErbGOo33wqBPRNxv3-Ouw0qijBBl4lcss7qSSxgMKGyRr6g2db_o5U0BRAZtCM_EuKR8y737fPb7b6F5DMffbxzRo-55broW9PnYw7CY1TUaem2DUNH29OmFqv0xGyatROEdmqsbN_IHwq9azx1-FpL7hkT7cXCh9z6WHpPVOj2KQaNn16xNQL52AP9EpnIFV9MoWJEvIy8CuXlHN1dRf5Qx_OKOVFU_Gf2lpK8-tm30otiLNLknTTob486QkaY06Qlrt6hBDnQFPuoo-_SHbkooySXuMUpUqhWoitJuxGMA2hJDZx5Hf8nrxvKWjO3Bx87HEVrbLuUQFiLtbK3XUUPxImdQnUTqGexUV8989JyXzXtrohRX7a-qpw5IJAMtZ2lgqE81XjP7BOR7LOBu63EqMEAP9LX1DK40k_VgAWz0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a561d8b149.mp4?token=OCDwFuwEZ8RusyRRSeDIwFaC9Y_a-WISkEXPkI3qXrBXu6cyehGS1mMj4tHOwsm0CaXXBseQEOomKuLenJU8MGnibJMaUF-d0moET_BzPx0DsFaJB-gYU9gRkrJLoQH0jiBJghpZ-8NIWat3F7bhEJBwssS_8zzzcrQ_Me4es5q2SsW1HMJxzGZWPzE8Je68xJPCJD5N-nv28oyHwTDXNOGGUX1K1NDS0S7B6C_NyU1i-RIzF1ILiN-Z0EiQninErbGOo33wqBPRNxv3-Ouw0qijBBl4lcss7qSSxgMKGyRr6g2db_o5U0BRAZtCM_EuKR8y737fPb7b6F5DMffbxzRo-55broW9PnYw7CY1TUaem2DUNH29OmFqv0xGyatROEdmqsbN_IHwq9azx1-FpL7hkT7cXCh9z6WHpPVOj2KQaNn16xNQL52AP9EpnIFV9MoWJEvIy8CuXlHN1dRf5Qx_OKOVFU_Gf2lpK8-tm30otiLNLknTTob486QkaY06Qlrt6hBDnQFPuoo-_SHbkooySXuMUpUqhWoitJuxGMA2hJDZx5Hf8nrxvKWjO3Bx87HEVrbLuUQFiLtbK3XUUPxImdQnUTqGexUV8989JyXzXtrohRX7a-qpw5IJAMtZ2lgqE81XjP7BOR7LOBu63EqMEAP9LX1DK40k_VgAWz0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیم
ا
: جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/16165" target="_blank">📅 22:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16164">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، گزارش داد
محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه پاسداران، در یک «سانحه رانندگی بر اثر واژگونی خودرو» در یکی از محورهای استان کرمان کشته شد.
فارس نوشت پس از وقوع حادثه، نیروهای پلیس و اورژانس در محل حاضر شدند و اکبرزاده به مرکز درمانی منتقل شد، اما به دلیل شدت جراحات جان باخت.
این رسانه وابسته به سپاه افزود بررسی علت و جزئیات این سانحه از سوی مراجع ذی‌ربط آغاز شده است.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/16164" target="_blank">📅 21:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16163">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFyRlycVe0wp9CY05vvUthpSGTac33ETWQpLmS6xc8ZLoAbYvHpv5raCEYj_yzHboWchG3LPsFC2iwApViufur9VajW-796QFq-5d5u8GvXD26Yqzs8WnRg97At5cBcVoItzKp0pYhDgIugejuW26Y2g5UFAicpRFww-jM__OvcerIe-_UZdYG0-Eyd7vmZBCoA2x0lSqEdG8cOU66__-qO12LaYfpLWJQWwozwQlJuO-N1X1qLgDPwQ0qo5m8WP2ncxWADE_5piYN0q6uucWCzA1sz04pKswaRqUqYdY_MwpS3FoGkB2XlqMhXbQ7gQPCUj755J1wOWboDF94PkBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون پیام هشدار سفر از طرف سفارت/کنسولگری چین
🚨
🚨
🚨
🚨
«وزارت امور خارجه چین و سفارت چین در ایران به هم‌وطنان چینی توصیه می‌کنند که در
حال حاضر از سفر به اصفهان ، قم ، مرکزی ، بوشهر و مناطق دیگر خودداری کنند
. لطفاً وضعیت امنیتی محلی را با دقت دنبال کنید، از مناطق با تنش و درگیری بالا دوری کنید، سطح هوشیاری را افزایش دهید و تدابیر امنیتی را تقویت کنید.
رعایت قوانین محلی، خودداری از حمل مشروبات الکلی، گوشت خوک و سایر اقلام ممنوعه در هنگام ورود، و پرهیز از عکس‌برداری در مکان‌هایی غیر از نقاط مجاز ضروری است. اگر امکان استفاده از کارت بانکی، کارت اعتباری یا چک مسافرتی ندارید، از پیش برای آن برنامه‌ریزی کنید. برای اطلاعات بیشتر، اپلیکیشن “China Consular Affairs” را دانلود کنید.
شماره اضطراری در ایران: 110
شماره امداد: 115
خط اضطراری جهانی وزارت امور خارجه چین برای حفاظت کنسولی و خدمات: +86-10-12308 / 65612308
شماره کنسولگری سفارت ایران: +98-9122176035
شماره کنسولگری سفارت ابوظبی: +98-9914240393
اداره فرهنگ و گردشگری چین در بخش گردشگری نیز توصیه می‌کند: “سه رعایت، سه نه” یعنی امنیت را آموزش بدهید، ادب را رعایت کنید، به بهداشت توجه کنید؛ سر و صدا نکنید، بی‌نظمی ایجاد نکنید، و قوانین را نقض نکنید.»
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/16163" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16162">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/16162" target="_blank">📅 20:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16161">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">معاون وزیر امور خارجه:
ایران به تنهایی عملیات پاکسازی مین‌ها از تنگه هرمز را طبق یادداشت تفاهم بر عهده خواهد داشت.
هیچ کشوری در پاکسازی مین‌های تنگه هرمز با ما مشارکت نخواهد کرد و از نظر اصولی اجازه این کار را نخواهیم داد.
@withyashar</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/16161" target="_blank">📅 20:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16160">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یک مقام آمریکایی: ما به ایران به‌روشنی توضیح دادیم که تنها در صورت تحقق پیشرفت در پرونده هسته‌ای، دارایی‌های مسدودشده این کشور آزاد خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/16160" target="_blank">📅 20:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16159">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه با فرمول پس زدن خاک از اجزای خامنه‌ای وضعیت رو نگاه کنیم ، با توجه به اتفاقاتی که داره می‌افته، این فرضیه درمیاد که یه درگیری دوباره پیش میاد تا این تشییع انجام نشه ! و اینا مثل فوتبال در دقیقه ۹۵ ضایع بشن ! و هی زجر بکشن…
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/16159" target="_blank">📅 20:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16158">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سفارت ایران در قطر : قصد مذاکره با آمریکا را نداریم.
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/16158" target="_blank">📅 19:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16157">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68787096d3.mp4?token=Q4QzavZcNZaXSWmc-3-mx9s0Y0oNOfhv7MS2lklYf5xvsHKpfRQ-b9UVzMsaJ01Pc6qqIrkzhJ3O0geK9eUH5VnvdWhGvLthFekgZCc8ghH07LK54pE8OMuTygGOTqrC5L9XNnkCBNQE1blbLuLvb6nY3ezlqCHRIgVTYSa5OR3uPQZDzD_hYnbBuIINLi_5sfISdhQ5HSqyBrQe-cEOXQnSc7M07e07l2kfuDxnDSZuUHvVCLmkgkPYEQtG52NzClZyMD2apO8I2HDRd7g8VxUnmbAzDciQMSpCEe18n86Rl8dfT35HeNKGTR4w2os6GAiKXvbqZqvl1R_oq2ypHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68787096d3.mp4?token=Q4QzavZcNZaXSWmc-3-mx9s0Y0oNOfhv7MS2lklYf5xvsHKpfRQ-b9UVzMsaJ01Pc6qqIrkzhJ3O0geK9eUH5VnvdWhGvLthFekgZCc8ghH07LK54pE8OMuTygGOTqrC5L9XNnkCBNQE1blbLuLvb6nY3ezlqCHRIgVTYSa5OR3uPQZDzD_hYnbBuIINLi_5sfISdhQ5HSqyBrQe-cEOXQnSc7M07e07l2kfuDxnDSZuUHvVCLmkgkPYEQtG52NzClZyMD2apO8I2HDRd7g8VxUnmbAzDciQMSpCEe18n86Rl8dfT35HeNKGTR4w2os6GAiKXvbqZqvl1R_oq2ypHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : در جریان سفری مداوم به خاورمیانه، دریاسالار برد کوپر، فرمانده سنتکام، با رهبران ارشد غیرنظامی و نظامی در اسرائیل و لبنان گفتگو کرد. کوپر و کارکنانش در لبنان با رئیس جمهور جوزف عون و فرمانده نیروهای مسلح لبنان، ژنرال رودولف هیکل، دیدار کردند. این رهبران در مورد مسیر پیش رو برای اجرای یک توافق‌نامه تاریخی که روز جمعه در واشنگتن دی سی امضا شد، گفتگو کردند.
سنتکام : بیش از ۵۰ هزار نفر از نیروهای نظامی آمریکایی در حال حاضر در سراسر منطقه در حال فعالیت هستند و هوشیار و آماده باقی مانده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/16157" target="_blank">📅 19:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16155">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وزیر جنگ اسرائیل: ما در حال آماده شدن برای نبرد جدیدی با ایران هستیم که هر لحظه ممکن است رخ دهد و ما از لبنان عقب‌نشینی نخواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/16155" target="_blank">📅 18:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16154">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔸
قطر فعالیت‌های دریایی خود را تا اطلاع ثانوی متوقف کرد
وزارت راه و ترابری قطر با صدور اطلاعیه‌ای اعلام کرد به‌منظور حفظ ایمنی عمومی، تمامی فعالیت‌های دریایی در این کشور به‌طور موقت متوقف می‌شود.
این وزارتخانه از تمامی مالکان و استفاده‌کنندگان وسایل دریایی خواست موقتاً از حرکت در دریا خودداری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/16154" target="_blank">📅 18:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16153">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یک مقام آمریکایی به سی‌ان‌ان:
آمریکا و ایران پس از چند روز درگیری و تبادل آتش در نزدیکی تنگه هرمز، فعلا از تشدید تنش خودداری خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/16153" target="_blank">📅 18:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16152">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دولت عراق تا پایان شهریور به مقاومت عراق مهلت داده است تا سلاح خود را تحویل دهد
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/16152" target="_blank">📅 17:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16151">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بیانیه دولت لبنان پس از دیدار عون با فرمانده سنتکام
ریاست جمهوری لبنان:
رئیس‌جمهور عون با فرمانده فرماندهی مرکزی ایالات متحده درباره آماده‌سازی برای آغاز اجرای توافق چارچوب با اسرائیل گفتگو کرد.
رئیس‌جمهور عون بر مصمم بودن برای اعمال حاکمیت دولت از طریق نیروهای مسلح خود تا مرزهای بین‌المللی جنوبی تأکید کرد.
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/16151" target="_blank">📅 17:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16150">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فرمانده سنتکام، دریادار براد کوپر، برای دیدار با فرمانده ارتش لبنان، رودولف هیکل، به بیروت رسید
هدف اعلام‌شده، نظارت بر آغاز اجرای فاز آزمایشی است
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/16150" target="_blank">📅 17:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16149">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21080c94a8.mp4?token=ruRUnz8SmYh2Xsj17p2M71TYdiDzb1NwQVXiYJ_VdaLJa83bRzp9-lBTwkTTYGDeiQPh-JZ_BWX4wsUvF03M4tEzpg5nGG5e5tUO0h-Pi41xfpB3SzTNC2Ptbq5N_lHTYyvJZIGxJ3klDORelKspc-J1ISCoPvLqgfcjKx0bJCEhckCIS2Xv12PCdhjZYENjnjg_LZ0vbrPorZ__rp6vFPGyCo4CATOXNnyOgrVb3Bk3rNNW8tR8nNn28RLPrOOjq6x84JdtQyPms-YrA95wyk1DbEWLGB6PleYSNrF4T9mVXjmLCs1_Ju4hefcRJddQfp8uTZ7G-1XvSIGqOZtFng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21080c94a8.mp4?token=ruRUnz8SmYh2Xsj17p2M71TYdiDzb1NwQVXiYJ_VdaLJa83bRzp9-lBTwkTTYGDeiQPh-JZ_BWX4wsUvF03M4tEzpg5nGG5e5tUO0h-Pi41xfpB3SzTNC2Ptbq5N_lHTYyvJZIGxJ3klDORelKspc-J1ISCoPvLqgfcjKx0bJCEhckCIS2Xv12PCdhjZYENjnjg_LZ0vbrPorZ__rp6vFPGyCo4CATOXNnyOgrVb3Bk3rNNW8tR8nNn28RLPrOOjq6x84JdtQyPms-YrA95wyk1DbEWLGB6PleYSNrF4T9mVXjmLCs1_Ju4hefcRJddQfp8uTZ7G-1XvSIGqOZtFng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاخ سفید؛ پاسخ خشونت با خشونت داده خواهد شد،
سخنگوی کاخ سفید اعلام کرد که آمریکا به هرگونه حمله، به‌ویژه حملات اخیر به کشتی‌های تجاری، پاسخ نظامی داده و این روند ادامه خواهد داشت. او تأکید کرد رئیس‌جمهور هم‌زمان به دنبال پیشبرد روند صلح است و از ایران خواست «توافق خوبی» با آمریکا امضا کند، در غیر این صورت واشنگتن آماده استفاده از قدرت نظامی خود است.
وی با اشاره به عملیات‌های «چکش نیمه‌شب» و «خشم حماسی» گفت در هر سناریویی آمریکا برنده خواهد بود: در صورت پیشرفت صلح، توافق‌ها ادامه یافته و کاهش قیمت انرژی تداوم می‌یابد؛ اما اگر ایران نقش «مخرب» داشته باشد، به گفته او با انزوای بیشتر در منطقه مواجه خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/16149" target="_blank">📅 16:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16148">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">فاکس نیوز : ویتکاف و کوشنر به سمت قطر حرکت کردند
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/16148" target="_blank">📅 15:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16147">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTKW_dvtVvwiWPzma9xftskYhR8O-OzJeNL5Nt1-SwakzxxmuyOcL8mVSSBQ-x4tihpyHpooRETfR3yw9n7vJfG_nwiIJE8VG10lcsIzN9Uie423JKxNSmT-liVwm4vrMRejis2IKanSUGg3vjiV9GcOK6sDC3cvkYkzDQi_AaxuhJrmswwrxgOmBTWKr1IZ2JnPZde4jJXzYok1Anebi0TYbBIaheCic7e46FAgZA-trW19sDKGQ1Mu_mGc3OYbJi58w1srOHm1DrFFy9TQQfRlmSFTQ02SljUgYx_j_DDT7_Bu3ElttKSz8C3JpBVV76g6v_KWH-GR4j2qwxhDtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث : نفت خام ۶۹ دلار، و در حال کاهش است. این کمتر از مقداری است که پیش از آغاز غیراتمی‌سازی ایران بود
قیمت بنزین به سرعت پایین می‌آید! هرگونه تخلف در سطح خرده‌فروشی را گزارش دهید!!
@withyashar</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/16147" target="_blank">📅 15:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16146">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWCpKflsQpv7ZzLEeEU4bSAlKI0YZol6eC_F5svhzuasg88jQ-6ZGMXWw1J9wJIsbb-cy__eDXe_5ImERF26rXFXXDRbHx2_cCgPqSe5cZGMTafVCh0stfVIsJsYVXXsybNjzs2Tea-kW709nGO0R0udUjyCuBqf6tOgvOfTbErkmpZ_20cxo6CcpV6uibQ2WLRR4jiJF3CftlAOC4K-9rT6DGeoqgEMlds2WF7uDp9wyNQ4axCE-lm00azP9HWXmPS_01kwFatoYypzcmu13-CEIVKpvYxPkbVMYGR-xD5QrxLvezBhGsLfhE8JXXwBKsNNtX1DPeyV7V56OhxBOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران درخواست ملاقات کرده است. این ملاقات فردا در دوحه برگزار می‌شود! رئیس‌جمهور DJT
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/16146" target="_blank">📅 15:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16144">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DwWptg0oZnBaE7ihVR4qb508aLkz_HTk9AbQy3N9idJ8IYb6s64SuphQ-Wc_kvygBZhhtZAFE_P6d_EakNhtjX3IE5Ge2Hg7i6cw8rjdyBdFvL5Apjk4mKt8AuEmfvANKGLGcfLb06WehJU-gEoW3MjfNtK4mFqcIdiznFVJpirEaoNtocDB7ASkhoo7g9aUVI35cbJtpLcdQ_u9NPON3F68YJrOe2_bPVPGq8s6vrkbzuZSjkHIFrt2qhU2Dq8D0Pa38axC95UxhkkrQpZdhbO6Z8mFyUZX7WXP9naaBGuvZRgqApmC_PSJwwCuhTKxbkcFB2mcTyFU0Q0nlWxBbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n34EBI9E8xB49mGG5-QULRTpVsnzsgDUwqRBIi4LTy-etjDeGFsDQ0vxApvTRtzv0I9g4IaX2KTpZrPx1tP1VZyAEQ_fPkMzyA9IfGu0zgly_OChqhryVr96IQp-sisB-YLKqYPVZxANuXPDWCMRfxUBckbY3ruRe62dGyCBgXELs6K75_eN3LL4FbDA8qhuYZikG9hFXiN6Z9mlvOaafpYsVmm0lLBlXy2MkMDgVblIls40ieMGIXYXPGqRnuFlPWJ9l1BZ_uFkN0LouVB0H85rxlKtjv8NhWcnTO2_vyFHEHIUb-_jo6KGCngLqvjXFJjWpjCabF8ohCg1H0DOoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نفتکش شرق لیما، المحبوبه (شماره IMO 9340415) با پرچم عربستان سعودی است که از چین حرکت می‌کند با سرپیچی از دستورات سپاه پاسداران عبور فقط از جنوب جزیره لارک از کریدوری تحت حمایت آمریکا و در میان اسکورت سنگین هوایی نیروی هوایی ایالات متحده، از تنگه هرمز عبور کرد.
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/16144" target="_blank">📅 14:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16143">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">رویترز: ایران شرکت در مذاکرات فنی را لغو کرد.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/16143" target="_blank">📅 14:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16142">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g41j72_ywRfI66G_CuA-vXo9NJ-BcyKpYdO06FPit4dexrKmkYRhNS_ndO2oOF60-I69meoGj0mfQoOae4PDmM9aR952MZPo4JYBjKufbGydQbmCWpiymJSM3s0TOdrFcumP3TQx7eATdWbW56H2gk4krbs7AeOPlPibFQjRVx4tvv5Js-WmWusXlKmU2n4Nf9Sxr_kAAjy6YV1ua8CioS9STqBd1PqnxIbeO1M52UTI6GFBNafl49z9Glvy1nXHBzxpNGe6Ec4juYzujZeCsDeqUDg-HNIWjbaJ6tT0LBiH59B6uMCTiNnAQ1bj6oILY3rdKHfH5q1XjlDC39lmQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل اسرائیل، ایال زمیر در‌جلسه به مناسبت ۱۰۰۰ روزه شده مبارزه : الان جنگ به یه مرحله حساس رسیده
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/16142" target="_blank">📅 14:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16141">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgvMrI6T1TBxs1QPVZjAipyQa54ARSOdh-Z567Pc2GefpGrVc35vj2STbcn4sa3Q-mEQiJSRjebeGNJ1B6PC8DhUPJTFADIz7mJbKy3SZsP_VLQORSmn2QLTCtGbs4GW718suoXuGaB_EdOZCdlxUb9uv6uBXqCQyj0OsDEXFKANXow0KnNUo8bWKSqHaLm8ULR4mX1V5_3ZA2igvrSgXXLWIR0G6LMUjYY7sVT8lxwo43wXXYnrt9Ka2W0dpthrr8cZZUrFXFpYvbpcEEPHj-tanGzFK2Nydd5jmuwSyJ678rO3nnhTtfC9npbh3gSvM7xcVBymIwHJHS3VNqGnpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : بالاترین آمار نظرسنجی‌ها تا کنون. حتی بالاتر از روز انتخابات، ۵ نوامبر. این علیرغم این واقعیت است که ایران سلاح هسته‌ای نخواهد داشت!
@withyashar
یاشار : نردبون ایران
😂</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/16141" target="_blank">📅 14:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16140">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کانال 12 اسرائیل: جی دی ونس و افرادش کسانی بودند که طرح مخفی موساد برای تغییر حکومت در ایران با کمک کردها را به اردوغان، لو دادن
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/16140" target="_blank">📅 13:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16139">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کانال ۱۶ اسرائیل :
«این توافق تنها زمانی محقق می‌شود که مرغ دندان داشته باشد»
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/16139" target="_blank">📅 13:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16138">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جزییات مراسم تشییع خامنه ای درتهران
استاندار تهران: مراسم وداع از ساعت ۶ صبح روز شنبه ۱۳ تیر در مصلای تهران آغاز می‌شود و تا روز بعد ادامه خواهد داشت
پیش‌بینی شده است نماز در ساعات ابتدایی روز دوم اقامه شود و پس از آن، مراسم وداع تا ساعت ۱۴ روز یکشنبه ۱۴ تیر ماه ادامه پیدا می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/16138" target="_blank">📅 12:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16137">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ارتش اسرائیل و شاباک: یک تروریست دیگر که در ربودن شهروندان در ۷ اکتبر نقش داشت، از بین رفت
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/16137" target="_blank">📅 12:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16136">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الان صدای انفجار‌ در شیراز (از قبل اعلام شده بود) مهمات عمل نکرده است
@withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/16136" target="_blank">📅 11:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16135">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMzJcRCGhHHkTFM8zMC-5DvmGXTBXc4os6C5wST4-N3YQuASlgTdpHNKidP6QxwcqAUNHJUaGs2SfLhX7kCu9OuIjJlrs-r3JHZ4Pr1GDxq0ucBAs3pojkjFIguhYCZ3Ru8NPBHS27XEbmryiYrlCBjQQXJl0kbDwAiFs4oPnw4FHo102wY6xFLez-vsYCPlnMB_0UdeXCXfdm07IxE704VA9EZr0E6XI2Ys23JZa6q_QOJ92WWqK64Zp6QBF0hl4Vu5B4t-zp_psw4vC1J7JrtzS7cHyazH4w74FPKBuYZGYCMQVukKP0D3fgw0GrBRqMEDH51EXgHsrRQV0GxUtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ستون دود اهواز بعد از شنیده شدن صدای انفجار
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/16135" target="_blank">📅 11:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16134">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">صدای انفجار اهواز
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/16134" target="_blank">📅 11:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16133">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور:
۶ میلیارد دلار از منابع مسدود شده ایران در قطر آزاد شد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/16133" target="_blank">📅 11:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16132">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رئیس‌جمهور روسیه، پوتین، دیروز برای اولین بار اعتراف کرد که روسیه به دلیل حملات اوکراین در خاک خود با کمبود و مشکلات سوخت مواجه است، اما ادعا کرد که نیروهایش به جنگ ادامه خواهند داد و حتی به تصرفات بیشتر در خاک اوکراین اشاره کرد. «این حملات به تأسیسات زیرساختی ما مشکلاتی ایجاد می‌کند، این واضح است»، او در مصاحبه با رسانه‌های محلی گفت و ادعا کرد که «کمبود بحرانی نیست»
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/16132" target="_blank">📅 10:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16131">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزیر کشاورزی آمریکا: محصولات کشاورزی آماده ارسال به ایران هستند
مجری: محصولاتی که قرار است به ایران بروند، احتمالاً قبلاً کاشته شده‌اند؟"
بروک رولینز: "دقیقاً درست است و آماده ارسال (به ایران) هستند.
@withyashar</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/16131" target="_blank">📅 10:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16130">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWxBLLhJBBPHK1cN834hIJG_RIpHkuOdrfsqzxcomzpiqnBZeQvaXIQF0fMGV9IBJJvaGiYaLbWpdX5gkTeTOdVhHldkNy6O-UBZK9qKzm88lFBwWWMekRS4VuFHVzQszYlp8WYKvJFLNLxJZM3WPbhz_j8rYJnoAmoVLWhexv_6irW_FF9JQ7ehnX_Eu1-Oz6RT4rNgx2FQPi1uh8engxMYXA0I0Y0XaTB5N_dXD4ckgZiGHJ-sS_0xm42QJeiIVu33_wIIwL5_paSlF6fx1qi4Rga2c15DUVACYPbM9frhZaHS2Yh3iIo3WPsFqdqmNCULWyaYMwENt1vdyXZd0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفر کاظم
دست کج
به عمان برای برگزاری نخستین نشست کمیته مشترک هرمز
این کمیته قرار است به‌صورت منظم برای هماهنگی‌های منطقه‌ای در حوزه امنیت و مدیریت تنگه فعالیت کند؛ اقدامی که می‌تواند نشانه‌ای از تقویت همکاری‌های تهران–مسقط در یکی از حساس‌ترین گذرگاه‌های انرژی جهان باشد.
@withyashar</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/16130" target="_blank">📅 09:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16129">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رسانه‌های افغانستان گزارش دادند پاکستان چند نقطه را در ولایت‌های کنر، پکتیا و پکتیکا هدف قرار داده است. هم‌زمان، پاکستان اعلام کرد مواضعی را در مناطق مرزی با افغانستان هدف گرفته است. @withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/16129" target="_blank">📅 09:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16128">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">جاسم البدیوی، دبیرکل شورای همکاری خلیج فارس:
در مورد بسته‌ی ۳۰۰ میلیارد دلاری، من چیزی ندیده‌ام. نه به من و نه به دیگران در کشورهای شورای همکاری مطلبی گفته نشده. ما چیزی در این مورد نمی‌دانیم
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/16128" target="_blank">📅 09:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16127">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فیلمی از حمله‌های سنگین آمریکا به مناطق جنوب
@withyashar
احتمال زیاد رادار سیریک</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/16127" target="_blank">📅 09:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16126">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124ea90741.mp4?token=GGfulK6UNDIX6TP4ekpSc_IXoE3kYtM0gIoOJYkvqZKwbgfkUfqgZtWJAIiFJV8IeZm4Bb9dIHo7yyg13kWGC7_Kwx4Pla6n3QAuqp8YPsKKW5X4PJYoEOLYQilzTE3F_fJgohtka_P_9QGtm1aiS4nP45qeOeuZ4tcEmiZb-u7oVuRP_EIMU3b31wDNY_01ivcn19aucpCBWUWZjnTJrUeDqSuw2NClrP5MDd7M-zGRqiShNhjVUKUfltZf02q3ifNVutE4skSejaV8Qw5Jxs1O1zzcLyi6JcRsXdcBA6J8EfJuKxWwv2nDO7LSUHPmgkWZ9oxRU7pjqXPkt5qweVBVvLrUQ39mPtpaED_Vuzo2jCNpsHDcmNqjMjZLIjs4YP1cCyrjEFHtGeyi6fK8_9Z4-FjSOxhrdNYZcTGqip7Ifb-5nkzEBgm_YBUxJdXAmfWDa_OqjXsS6r_6xthmiQ4xjcnsONbrUFxiRMnBqLCqCVxQyNO8UXh0qw4rKQcUFuUTlE95pmaWDeKwqDJ8HWtlVNnFXgPO2pyYF7xCW4e6E02YnPTZHvHRsdoWvIKJvCzeB9p1_F-GQ6A9-NIuqDKtYzO8VajCqL0mYJJ8Gng8YQBML1tjGDa41DNM6t4XJIUeMUfp56LyZrelGLRKxOlx3ct-PK73y_209SflohM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124ea90741.mp4?token=GGfulK6UNDIX6TP4ekpSc_IXoE3kYtM0gIoOJYkvqZKwbgfkUfqgZtWJAIiFJV8IeZm4Bb9dIHo7yyg13kWGC7_Kwx4Pla6n3QAuqp8YPsKKW5X4PJYoEOLYQilzTE3F_fJgohtka_P_9QGtm1aiS4nP45qeOeuZ4tcEmiZb-u7oVuRP_EIMU3b31wDNY_01ivcn19aucpCBWUWZjnTJrUeDqSuw2NClrP5MDd7M-zGRqiShNhjVUKUfltZf02q3ifNVutE4skSejaV8Qw5Jxs1O1zzcLyi6JcRsXdcBA6J8EfJuKxWwv2nDO7LSUHPmgkWZ9oxRU7pjqXPkt5qweVBVvLrUQ39mPtpaED_Vuzo2jCNpsHDcmNqjMjZLIjs4YP1cCyrjEFHtGeyi6fK8_9Z4-FjSOxhrdNYZcTGqip7Ifb-5nkzEBgm_YBUxJdXAmfWDa_OqjXsS6r_6xthmiQ4xjcnsONbrUFxiRMnBqLCqCVxQyNO8UXh0qw4rKQcUFuUTlE95pmaWDeKwqDJ8HWtlVNnFXgPO2pyYF7xCW4e6E02YnPTZHvHRsdoWvIKJvCzeB9p1_F-GQ6A9-NIuqDKtYzO8VajCqL0mYJJ8Gng8YQBML1tjGDa41DNM6t4XJIUeMUfp56LyZrelGLRKxOlx3ct-PK73y_209SflohM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلیل آخرینم باش…
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16126" target="_blank">📅 02:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16125">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سناتور جان کندی : ایران الان مثل یک پیرمرد خیلی پیر است که توانایی گرفتن سرماخوردگی را ندارد. ما آنها را به شدت تضعیف کرده‌ایم. نباید تسلیم شویم
برای من عدم توافق قابل قبول است؛ توافق بد قابل قبول نیست.
در پایان یک دوره زمانی معقول، ۶۰ روز یا هر چه که باشد، فکر می‌کنم باید دوباره وارد شویم و دوباره مثل گربه‌زن با آنها برخورد کنیم
باید آنها را بخوریم و استخوان‌ها را روی زمین تف کنیم
@withyashar
آخرش حرف منو میزنه منظورش اینه گربه گیرشون کنیم‌
😂
😂
😂</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16125" target="_blank">📅 01:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16124">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16124" target="_blank">📅 01:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16123">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">📩
درخواست همکاری  اگر علاقه‌مند به همکاری هستید برای کمک مسیج های قبلی پرید ، لطفاً اطلاعات زیر را از طریق تلگرام برای دوباره به این شکل ارسال کنید:  نام یا لغب نوع فعالیت / حوزه کاری: سابقه کاری: آدرس لینکدین: (خیلی خوبه باشه) آدرس اینستاگرام: (اختیاری) آیدی…</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16123" target="_blank">📅 01:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16122">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رسانه‌های افغانستان گزارش دادند پاکستان چند نقطه را در ولایت‌های کنر، پکتیا و پکتیکا هدف قرار داده است.
هم‌زمان، پاکستان اعلام کرد مواضعی را در مناطق مرزی با افغانستان هدف گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16122" target="_blank">📅 01:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16121">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c21113c23.mp4?token=srxW_vnz5IXs15bsf8u-peVDCr3GGDV-Vtqimak7DqqGTHi66UgNktkHSjsYbU7l-QAf1VQaPrxAZ3noKgZzBb1x0PTXl9yxx4SWgBDJDYN3-2NH78tOtJlvg2A9-TkMER5FHNjAQVykU3XR41VaFStBfBx4oWSncc-N_rAxSbmwvIiAjUIEnpXy0_9XavnWfEDEIdxyJn9cLrc7k09b6tg_Z9vYwNxbrRvkLo7Fpm4WGDqjHJxNhgqtyQF-1Ln3BxaqNBAaUEC-gXhAxutgkjTV27P0O9ihd82zUW5_VngcOORZZPDky-LRw8c5tF1lvwKiUKQ4TlV3upvRroeS1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c21113c23.mp4?token=srxW_vnz5IXs15bsf8u-peVDCr3GGDV-Vtqimak7DqqGTHi66UgNktkHSjsYbU7l-QAf1VQaPrxAZ3noKgZzBb1x0PTXl9yxx4SWgBDJDYN3-2NH78tOtJlvg2A9-TkMER5FHNjAQVykU3XR41VaFStBfBx4oWSncc-N_rAxSbmwvIiAjUIEnpXy0_9XavnWfEDEIdxyJn9cLrc7k09b6tg_Z9vYwNxbrRvkLo7Fpm4WGDqjHJxNhgqtyQF-1Ln3BxaqNBAaUEC-gXhAxutgkjTV27P0O9ihd82zUW5_VngcOORZZPDky-LRw8c5tF1lvwKiUKQ4TlV3upvRroeS1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل فیلمی از انفجار تونل در منطقه مجدل، جنوب لبنان، منتشر کرد. ارتش اسرائیل اعلام کرد که این نیروها تونلی را که در واقع یک مجتمع زیرزمینی ساخته شده با استفاده از دانش و فناوری رژیم ایران بود، منهدم کردند. در داخل تونل صدها سلاح و چهار سکوی پرتاب به سمت خاک اسرائیل وجود داشت.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16121" target="_blank">📅 00:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16120">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وزارت کشور بحرین: در پی حمله ایران، یک ساختمان مسکونی در منطقه المحرق آسیب دید، اما هیچ خسارت انسانی در پی نداشت.       @withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16120" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16119">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یک منبع آگاه از مذاکرات گفت که قرار بود مذاکرات سه‌شنبه در ابتدا در سوئیس برای رسیدگی به برنامه هسته‌ای ایران برگزار شود. تشدید تنش‌ها آنها را به مکان دیگری منتقل کرد و دوباره بر تنگه هرمز متمرکز شد.  به گفته یک مقام آمریکایی و یک منبع آگاه، انتظار می‌رود…</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16119" target="_blank">📅 00:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16118">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خبرگزاری اردن: سپاه به دنبال ترور یکی از فرماندهان سنتکام بود که موفق نشد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16118" target="_blank">📅 00:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16117">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">من مشکل جدی فیزیکی‌ برام پیش اومده کمک خواستم ! همین ! کلت زیر گلو کسی نزاشتم که ! جم کنید مسخره بازی رو</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/16117" target="_blank">📅 00:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16115">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اکسیوس: ایالات متحده و ایران توافق کردند حملات را متوقف کنند و در طول هفته آینده دیدار کنند، این را منابع آمریکایی به من اطلاع دادند. گزارش من در این موضوع @withyashar</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/16115" target="_blank">📅 00:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16114">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خبرنگار اسرائیلی: ایران تونل‌های عظیمی در جنوب لبنان ساخته است.
مقادیر مواد منفجره‌ای که ارتش اسرائیل به این منطقه پمپاژ می‌کند، بیشتر از هر چیزی است که در تمام جبهه‌های جنگ وجود داشته است
@withyashar</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/16114" target="_blank">📅 23:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16113">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اکسیوس: ایالات متحده و ایران توافق کردند حملات را متوقف کنند و در طول هفته آینده دیدار کنند، این را منابع آمریکایی به من اطلاع دادند. گزارش من در این موضوع
@withyashar</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/16113" target="_blank">📅 23:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16112">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📩
درخواست همکاری
اگر علاقه‌مند به همکاری هستید برای کمک مسیج های قبلی پرید ، لطفاً اطلاعات زیر را از طریق تلگرام برای دوباره به این شکل ارسال کنید:
نام یا لغب
نوع فعالیت / حوزه کاری:
سابقه کاری:
آدرس لینکدین:
(خیلی خوبه باشه)
آدرس اینستاگرام:
(اختیاری)
آیدی تلگرام:*
(الزامی)
توضیحات:
لطفاً تخصص‌ها، مهارت‌ها، سوابق و توانایی‌های خود را به‌صورت مختصر معرفی کنید.
لطفاً اطلاعات را فقط برای دایرکت همین چنل ارسال کنید
ادمین (خبری، بازار های مالی،گیم،موزیک، ورزشی)
برنامه نویس
و کسی که بتونه ویکیپدیا بیاره بالا
ویدیو ساز فقط با هوش مصنوعی
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/16112" target="_blank">📅 23:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16111">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اتاق جنگ با یاشار : الان جریان اینه که اسرائیل میخواد تونلهایی که حزبالله با کمک ایران ساخته رو منفجر کنه و برای این کار از دو برابر مواد منفجره معمول میخواد استفاده کنه که کاملاً نابود بشن. در نتیجه هشدار دادن به مردم شمال اسرائیل که شما ممکنه حتی یک زلزله…</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/16111" target="_blank">📅 23:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16110">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اتاق جنگ با یاشار : الان جریان اینه که اسرائیل میخواد تونلهایی که حزبالله با کمک ایران ساخته رو منفجر کنه و برای این کار از دو برابر مواد منفجره معمول میخواد استفاده کنه که کاملاً نابود بشن. در نتیجه هشدار دادن به مردم شمال اسرائیل که شما ممکنه حتی یک زلزله خفیف رو احساس کنید. از سمت دیگه حزب الله اخطار داده که با این کار تنشها تشدید خواهد شد. خواهیم دید چه میشود.
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/16110" target="_blank">📅 23:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16109">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نخست‌وزیر بنیامین نتانیاهو و وزیر دفاع اسرائیل کاتز در بیانیه‌ای مشترک: "در چارچوب عملیات «پایان جمله»، ارتش اسرائیل اکنون زیرساخت تروریسم زیرزمینی حزب‌الله را در منطقه روستای مجدل زون در جنوب لبنان نابود کرد. اسرائیل پیشاپیش آمریکا را مطلع کرده است"
@withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/16109" target="_blank">📅 23:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16108">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کانال ۱۴ ، جنجال در کابینه: به دیوید زینی، رئیس شین بت، دستور داده شد تا تحقیقات در مورد نشت عملیات «غرش شیران» به اخبار کانال ۱۲ را (علیرغم مخالفت مشاور حقوقی) پیش ببرد.
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/16108" target="_blank">📅 23:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16107">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فضائلی، عضو دفتر حفظ و نشر آثار آیت الله خامنه ای: امروز قرار بود مذاکرات فنی برگزار شود که ایران آن را لغو کرد و شرکت نکرد که دلیل این امر درگیری‌های این چند شب گذشته بود و دلیل دیگر این است که منتظر اجرای برخی شروط هستند که مثلا امکان برداشت پول‌های بلوکه شده است یا خیر
@withyashar</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/16107" target="_blank">📅 23:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16106">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گزارش ها از رهگیری چند موشک برفراز اردن
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/16106" target="_blank">📅 23:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16105">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وزارت خارجه اسرائیل :
شادی مردم ایران از حذف تیم جمهوری اسلامی یک چیز را نشان میدهد: انزجار و بیزاری مردم از چیزی که به رژیم مربوط میشود
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/16105" target="_blank">📅 23:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16104">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هم اکنون اسرائیل به شهرک‌های مفدون و نبطیه الفوقاء در جنوب لبنان حمله کرد.
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/16104" target="_blank">📅 22:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16103">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یک مقام ارشد دولت ترامپ امروز به رسانه‌ها اعلام کرد که مذاکرات میان آمریکا و ایران که قرار است آخر هفته جاری در سوئیس برگزار شود، همچنان طبق برنامه انجام خواهد شد
این اظهارات، گزارش پیشین روزنامه وال‌استریت ژورنال را رد می‌کند؛ گزارشی که مدعی شده بود این مذاکرات به دلیل دور جدید حملات متقابل ایران و آمریکا در منطقه خلیج فارس به تعویق افتاده است.
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16103" target="_blank">📅 22:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16102">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0003b579.mp4?token=p_lNwj5ZMknGwZdJHpe9iU7pXgJ8tUYzRWZaGsnnoB2EfNb6OuksAouX9Q7uO-fA8xp6xjadvMllWH6a4PU__huqwnP35igM7p3BGHJ_vOqLMAmpoMydvzlkooqQGKugOLe4RTOX-Kia8Kwg67LuxL5pM2iZjZ1m2WeitvfxHQQIBMWGI2g77zwq6Qyy5m3aeuH4g6nIP3KIpXacBWvaIVgKf3PiwJRW_InRwOoi3w2yBjQfrmEc_9mGumrM2n9ZdzHd5lUo-05Ri2NOtzCTTeaANMeGLakrw2hLB7QCvvLP63ELCG-lfW9CJM36FKr2uYfOHGgE-0PkGorSdxQRtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0003b579.mp4?token=p_lNwj5ZMknGwZdJHpe9iU7pXgJ8tUYzRWZaGsnnoB2EfNb6OuksAouX9Q7uO-fA8xp6xjadvMllWH6a4PU__huqwnP35igM7p3BGHJ_vOqLMAmpoMydvzlkooqQGKugOLe4RTOX-Kia8Kwg67LuxL5pM2iZjZ1m2WeitvfxHQQIBMWGI2g77zwq6Qyy5m3aeuH4g6nIP3KIpXacBWvaIVgKf3PiwJRW_InRwOoi3w2yBjQfrmEc_9mGumrM2n9ZdzHd5lUo-05Ri2NOtzCTTeaANMeGLakrw2hLB7QCvvLP63ELCG-lfW9CJM36FKr2uYfOHGgE-0PkGorSdxQRtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلار ۱۷۵،۰۰۰
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/16102" target="_blank">📅 22:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16100">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/16100" target="_blank">📅 22:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16099">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">والانیوز عبری
: اسرائیل در حال آماده شدن برای احتمال حمله مستقیم ایران است، پس از امضای توافق لبنان و اسرائیل
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/16099" target="_blank">📅 22:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16098">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">امروز تولد ۵۵ سالگی ایلان ماسک، ثروتمندترین فرد جهان هست
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/16098" target="_blank">📅 22:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16097">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دیدبان اتاق جنگ : هواپیمای c 130  هرکولس ارتش نشست مهرآباد
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16097" target="_blank">📅 22:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16096">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارشاتی از شلیک موشک‌ از ایران به سمت اردن @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/16096" target="_blank">📅 22:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16095">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گزارشاتی از شلیک موشک‌ از ایران به سمت اردن
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/16095" target="_blank">📅 21:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16094">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">افزایش حالت آماده‌باش در اسرائیل به دلیل نگرانی از پرتاب موشک از ایران
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/16094" target="_blank">📅 21:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16093">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/920d7be6f9.mp4?token=UtJJhygsQUR_MdBOgvk5e-Nzy3ooZFyTh80FHmglu9_R_4zHQDir0sINnX0sw5MU-XwTgzVSAkBWAhU8qydDTH-qW-4POGxIErAwacc1DdXaCS0dVUT6p96w7bLgLjXXIqMTdkhNCqr9-um-Ec7qlTB8oKulUW-xOi-_UBg2WZL4_yjxuNrQyqiumEYo9e6mSRu9CV4qs1iHTvY4ye_wJbI8vzcIr3ndDMErXIJfWlyQ_ixQ7Gf6Y8kqkmT4kmnIovr5eP2sikmssEvwHFUpikazqP048acLNSp1PRBMXw-YBw6jU40xrRQ68GK-TWxEXyZccKSwhiK6ajVfATtHdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/920d7be6f9.mp4?token=UtJJhygsQUR_MdBOgvk5e-Nzy3ooZFyTh80FHmglu9_R_4zHQDir0sINnX0sw5MU-XwTgzVSAkBWAhU8qydDTH-qW-4POGxIErAwacc1DdXaCS0dVUT6p96w7bLgLjXXIqMTdkhNCqr9-um-Ec7qlTB8oKulUW-xOi-_UBg2WZL4_yjxuNrQyqiumEYo9e6mSRu9CV4qs1iHTvY4ye_wJbI8vzcIr3ndDMErXIJfWlyQ_ixQ7Gf6Y8kqkmT4kmnIovr5eP2sikmssEvwHFUpikazqP048acLNSp1PRBMXw-YBw6jU40xrRQ68GK-TWxEXyZccKSwhiK6ajVfATtHdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک والتز، سفیر آمریکا در سازمان ملل:
اگر ایران فکر کنه ترامپ قراره در برابر ادامه حمله به کشتی‌های بین‌المللی دست روی دست بزاره، کاملاً در اشتباهه؛ چون همین چند شب اخیر نشون داد که این کارها رو بی‌پاسخ نمی‌ذاره.
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/16093" target="_blank">📅 21:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16092">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">به گزارش i24NEWS، ایران هر شب حداقل شش پهپاد را به سمت کشتی‌های تجاری در تنگه هرمز پرتاب می‌کند که برخی از این پهپادها توسط ارتش ایالات متحده رهگیری شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/16092" target="_blank">📅 21:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16091">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تایید خبر توسط ایران: مذاکرات به دلیل حمله آمریکا به ایران لغو شده است  @withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/16091" target="_blank">📅 20:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16090">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شبکه ۱۲ عبری:
توافق میان اسرائیل و لبنان که متن کامل آن، از جمله در وب‌سایت وزارت خارجه آمریکا، منتشر شده است، دارای یک
پیوست امنیتی محرمانه
نیز بوده که همچنان طبقه‌بندی‌شده باقی مانده است. دلیل اصلی محرمانه ماندن این پیوست، درخواست صریح دولت لبنان عنوان شده است.
هیچ‌گونه عقب‌نشینی خودکار و زمان‌بندی‌شده‌ای وجود نخواهد داشت
؛ بلکه هرگونه عقب‌نشینی یا اجرای تعهدات، بر اساس میزان موفقیت در میدان و ارزیابی نتایج عملی انجام خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/16090" target="_blank">📅 20:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16089">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وال استریت ژورنال: مذاکراتی که قرار بود این هفته بین واشنگتن و تهران در سوئیس برگزار شود، پس از تبادل حملات دیشب متوقف شد. @withyashar</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/16089" target="_blank">📅 20:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16088">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اکسیوس: اسرائیل و لبنان به این نتیجه رسیدن که برای جلوگیری از دخالت جمهوری اسلامی باید توافق کنن.
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/16088" target="_blank">📅 19:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16087">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">هم اکنون نیروهای زمینی سپاه مواضع گروه کرد در کردستان عراق را با توپخانه هدف قرار دادند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/16087" target="_blank">📅 19:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16086">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وال استریت ژورنال: مذاکراتی که قرار بود این هفته بین واشنگتن و تهران در سوئیس برگزار شود، پس از تبادل حملات دیشب متوقف شد.
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/16086" target="_blank">📅 19:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16085">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مسیر های دریایی عبور از تنگه هرمز  شماره ۱ : که ورودی از بالای جزیره لارک و خروجی از پایین آن عبور میکند  شماره ۲ : هم اکنون مین ریزی شده و به شدت خطرناک است شمار ۳: مسیر ایجاد شده توسط آمریکا که سپاه حملات اخیر را در این مسیر انجام داده @withyashar</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/16085" target="_blank">📅 19:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16084">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دلار و تتر ۱۷۲،۵۰۰
🚨
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/16084" target="_blank">📅 19:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16083">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">طالبان افزایش قیمت اینترنت را ممنوع کرد
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/16083" target="_blank">📅 19:12 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
