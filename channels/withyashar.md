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
<img src="https://cdn4.telesco.pe/file/fHPZHJZtUXiINapr0PgZLJZIbrSzzD-MoaifJm43THw8FArR_M5Qyl_ud3JLhGyoGRnJEEZqnYuYcjomCESd-HE8MlE_gz_F_LupMoq2exmF85qflGwbIyBGKlDVM3GF7Jt9PRthbiMs_V-tWA_AZcz0w9iabsvPmKs1TX6KaY4dcSFYn8lZJCBC9B3Fp8YocUP_HfpOMsshc4GDmu2KPunbNsXXJCeAgsWz_--tEhOiRHpupkenLXoJXIxf_VpZGM2GUuXObAXtQS4nVHRHiSxgJq4h4Sy4XYPs1VlBmc6ulghQ8K0ba0C-UGotMfVRM_T-Fp9I5AEUBE4LdqtvwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 306K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 13:59:26</div>
<hr>

<div class="tg-post" id="msg-14111">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ادعای ترامپ درباره ایران:
اگر برویم و بمباران کنیم، که اگر بخواهیم خیلی آسان می‌توانیم این کار را انجام دهیم.
اما تنگه برای ماه‌ها باز نخواهد بود. اگر بمباران کنیم، می‌دانید، افراد زیادی کشته خواهند شد. چه کسی می‌خواهد این کار را بکند؟ من نمی‌خواهم.
@withyashar</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/withyashar/14111" target="_blank">📅 13:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14110">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-poll">
<h4>📊 آیا شما از تیم ملی جمهوری اسلامی در جام جهانی ۲۰۲۶ حمایت می‌کنید؟</h4>
<ul>
<li>✓ خیر ، بر زدشونم هر کاری باشه میکنم</li>
<li>✓ خنثی ، فقط دنبال میکنم و میبینم</li>
<li>✓ بله ، تمام قد پشت تیم ملی هستم</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/withyashar/14110" target="_blank">📅 13:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14109">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رسانه‌های ایران می‌گویند دو تن از اعضای «نیروی پدافند هوایی ارتش» در حمله دیروز اسرائیل کشته شدند و امروز تشییع می‌شوند.
تاکنون در حملات دوشنبه و سه‌شنبه اسرائیل کشته‌ای گزارش نشده بود و ۱۵ زخمی اعلام شده بود.
@withyashar</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/withyashar/14109" target="_blank">📅 13:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14108">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7566ed8ca7.mp4?token=kOkf5h6bPAs_YqrDKkDIdc9v1opDhUzGDIvZaUrklDUyiOfltrQehtYV5LL0Gf_5Gs-XDksb-PZtCjQ259ol2ja1RIkJ8cjujIfrQKZEdt_hEHcrm_PI3toTF1yJrr4HriEE5DLGxYEI-U-QhaCi1rI9JNoLy0E-Q8xyUIk4E1Yu-Qseht0QP13mdY7PuNP7hAeGRrrr3ghCR0LliRAZIhR9Xp5fwfkRRCWNgjHDh4XCFplWcM_ZvabhxzFPNCTLeNH2FoGsYaIkOqKTUjD-SSRvCzUoFVhtZoMlcNL3JvOJMvghXz9iGijgnj8__-x6AAE5AJN23xJv0-ET1LOHJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7566ed8ca7.mp4?token=kOkf5h6bPAs_YqrDKkDIdc9v1opDhUzGDIvZaUrklDUyiOfltrQehtYV5LL0Gf_5Gs-XDksb-PZtCjQ259ol2ja1RIkJ8cjujIfrQKZEdt_hEHcrm_PI3toTF1yJrr4HriEE5DLGxYEI-U-QhaCi1rI9JNoLy0E-Q8xyUIk4E1Yu-Qseht0QP13mdY7PuNP7hAeGRrrr3ghCR0LliRAZIhR9Xp5fwfkRRCWNgjHDh4XCFplWcM_ZvabhxzFPNCTLeNH2FoGsYaIkOqKTUjD-SSRvCzUoFVhtZoMlcNL3JvOJMvghXz9iGijgnj8__-x6AAE5AJN23xJv0-ET1LOHJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار و آتش سوزی پادگان سپاه کنار کوه صفه اصفهان
پیشتر رژیم اعلام کرده بود امروز اصفهان خنثی سازی مهمات عمل نکرده انجام میشود
@withyashar</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/withyashar/14108" target="_blank">📅 13:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14107">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یوتیوب رفع فیلتر می‌شود
مصطفی پوردهقان، نماینده مجلس:
وزیر ارتباطات در کمیسیون قول دادند که فضا را به شرایط عادی برگردانند و بعد از رفع فیلتر واتساپ، رفع فیلتر یوتیوب هم در دستور کار بود.
@withyashar</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/withyashar/14107" target="_blank">📅 12:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14106">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/withyashar/14106" target="_blank">📅 12:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14105">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سهمیه بلیت تماشاگران ایران در جام جهانی حذف شد
@withyashar</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/14105" target="_blank">📅 12:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14104">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3559129ca.mp4?token=Kf8V7GKQbgVfxDWwc-8FQKOOFDxIVyDrr6YRsKas_g3zjeWkK_ijWiV96k7MQxp8sj3ycFzpEEyx8m9v8wNOe2sFkkoBDGcYKj8DYwioy9RXuWPg7roJlPeFyBhx1r6oQ8RwqFxIy1oWomYtwnbcDojg2eSccYlnkoDsUZXzHo9nsP6zFSXnewTpUikJ4JF_cNObbytd7_v2wOSw8WM24D5HNz1y_zIGa6MOc-80irlVwoWE3iPv44AQ_kciW3Zo4hLR6xm_l1PZFvNWoVfId-uTJyuIPxflWxibB24EKBLWNc8euVWmm3xAT3uRp4p_0XzBTeWDl_lmS7RtLe01GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3559129ca.mp4?token=Kf8V7GKQbgVfxDWwc-8FQKOOFDxIVyDrr6YRsKas_g3zjeWkK_ijWiV96k7MQxp8sj3ycFzpEEyx8m9v8wNOe2sFkkoBDGcYKj8DYwioy9RXuWPg7roJlPeFyBhx1r6oQ8RwqFxIy1oWomYtwnbcDojg2eSccYlnkoDsUZXzHo9nsP6zFSXnewTpUikJ4JF_cNObbytd7_v2wOSw8WM24D5HNz1y_zIGa6MOc-80irlVwoWE3iPv44AQ_kciW3Zo4hLR6xm_l1PZFvNWoVfId-uTJyuIPxflWxibB24EKBLWNc8euVWmm3xAT3uRp4p_0XzBTeWDl_lmS7RtLe01GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور اتباع کشورهای مختلف در تجمعات شبانه حکومتی
@withyashar
🥴</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/14104" target="_blank">📅 11:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14103">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شبکه cnn: ترامپ ۳۷ بار توافق با ایران را «قریب‌الوقوع» اعلام کرده، اما هنوز هیچ توافقی حاصل نشده!
@withyashar</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/14103" target="_blank">📅 11:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14102">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وزیر ارتباطات: ترافیک اینترنت بین‌الملل قبل از ۴ خرداد با ترافیکی که از مسیر استارلینک از شبکه‌های مرزی خارج می‌شد، برابری می‌کرد
@withyashar</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/14102" target="_blank">📅 11:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14101">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رسانه های رژیم :
هلیکوپتر تهاجمی آپاچی AH-64، بعد از عدم توجه به هشدارها توسط نیروی دریایی سپاه پاسداران و بوسیله شلیک یکی از قایق های بسیج، ساقط شده است.
این در حالیست که با توجه به قریب‌الوقوع بودن اعلام متن تفاهم مشترک، اسقاط این هلیکوپتر به نقص فنی مرتبط شده است.
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/14101" target="_blank">📅 10:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14100">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ درباره نتانیاهو:
به نتانیاهو حمله شد و او هم متقابلاً پاسخ داد و من نمی‌توانم او را به خاطر این موضوع سرزنش کنم، آنها را هدف قرار دادند. آنهاهم متقابلاً پاسخ دادن و حالا درگیری را تمام کرده‌اند.
بنابراین، آنها قرار است فقط برای یک هفته دیگر یا چیزی حدود آن، یکدیگر را به حال خود رها کنند.
این وضعیت خاورمیانه مدت زیادی است که ادامه دارد. اگر واقعاً بخواهید بگویید حدود ۳۰۰۰ سال اما مطمئناً ۴۷ سال است که اینگونه ادامه دارد.
@withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/14100" target="_blank">📅 10:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14099">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ گفت خلبانان بالگرد آپاچی که در تنگه هرمز سقوط کرد، سالم هستند. او گفت آمریکا امروز گزارشی درباره این حادثه منتشر خواهد کرد.
@withyashar
این حادثه در دست بررسی است و هنوز مشخص نیست که آیا این بالگرد با شلیک نیروهای جمهوری اسلامی سرنگون شده، دچار نقص فنی شده یا با مشکل دیگری مواجه شده است.</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/14099" target="_blank">📅 10:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14098">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حملات سنگین اسراییل به صور لبنان
رادیو ارتش اسرائیل: ما محدودیت‌هایی برای حمله به بیروت داریم اما برای عملیات در جنوب لبنان محدودیتی نداریم
@withyashar</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/14098" target="_blank">📅 10:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14097">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فارس: تجهیزات هدایت و پشتیبانی جنگنده‌های اسرائیلی در جنگل‌های تنکابن(شهسوار) کشف شد
خبرگزاری فارس گزارش داد مجموعه‌ای از تجهیزات فنی و سامانه‌های زمین‌پایه که گفته می‌شود برای پشتیبانی و هدایت جنگنده‌های مهاجم مورد استفاده قرار می‌گرفته، در ارتفاعات جنگلی شهرستان تنکابن در استان مازندران کشف و جمع‌آوری شده است.
بر اساس این گزارش، این تجهیزات در یکی از مسیرهای اصلی ورود جنگنده‌ها به حریم هوایی تهران مستقر بوده‌اند.
فارس مدعی شده منطقه مورد نظر در جریان «جنگ رمضان» یکی از کریدورهای اصلی ورود جنگنده‌های اسرائیلی برای اجرای حملات علیه تهران و مناطق شمالی کشور محسوب می‌شده است.
﻿
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/14097" target="_blank">📅 10:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14096">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حزب دمکرات کردستان ایران کمی پیش  امروز سشنبه در شبکه ایکس خبر داد یکی از کمپ‌های این حزب بار دیگر هدف حمله پهپادی جمهوری اسلامی قرار گرفت.
بر اساس این گزارش در این حمله دو فروند پهپاد به سمت "کمپ آزادی" شلیک شده‌اند.
کمپ آزادی محل اسکان خانواده‌های اعضای حزب دمکرات است و از آغاز درگیری‌های اخیر تا کنون بارها هدف حملات جمهوری اسلامی قرار گرفت. این حزب تا کنون گزارشی درباره تلفات جانی یا زخمی‌ها ارائه نکرده است.
بر اساس این گزارش، جمهوری اسلامی ایران از زمان آغاز درگیری‌ها با آمریکا و اسرائیل تا کنون با شلیک بیش از ۱۳۴ فروند موشک و پهپاد، کمپ‌های حزب دمکرات کردستان ایران و همچنین مراکز درمانی و آموزشی این حزب را هدف قرار داده است.
@withyashar</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/14096" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14095">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af93d53bde.mp4?token=DYaSGmbRi6nXlwTyQ5n_LszwKygtLaFfUrypwxTyutfl3LSEVYPpbipcBQUDpsLCojWpannBqp9aPb1hZuH5yAyBGvBwY5mjlv9eUAeqQ-6ZlvQHs62X5ctUV08FMOp6q-ERiy_FyENMXKb4q0OJFg3CP1MAFoKWzbdOTdEl_stl8iKT7C995JngdnqolBOUb7DRQyCSK2ZgRgazSa0jXDzy3FPsMA7ZdE_Bt8RDEqEf7M2o5yOkGS5ZShs6pDM6FQuWSOQt5Fjgg9vC_-W3cempI0Wq9nl6Et8Bv4wzqL6-Iy1knrK9tIV_Kj2RxnRU-kuYudny9zS6ehYaHWy10w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af93d53bde.mp4?token=DYaSGmbRi6nXlwTyQ5n_LszwKygtLaFfUrypwxTyutfl3LSEVYPpbipcBQUDpsLCojWpannBqp9aPb1hZuH5yAyBGvBwY5mjlv9eUAeqQ-6ZlvQHs62X5ctUV08FMOp6q-ERiy_FyENMXKb4q0OJFg3CP1MAFoKWzbdOTdEl_stl8iKT7C995JngdnqolBOUb7DRQyCSK2ZgRgazSa0jXDzy3FPsMA7ZdE_Bt8RDEqEf7M2o5yOkGS5ZShs6pDM6FQuWSOQt5Fjgg9vC_-W3cempI0Wq9nl6Et8Bv4wzqL6-Iy1knrK9tIV_Kj2RxnRU-kuYudny9zS6ehYaHWy10w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهواز همین الان
@withyashar
گویا دود فلر ‌نفتیه</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/14095" target="_blank">📅 09:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14094">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58ec6b7e1.mp4?token=KMYiQF46dhpZzgtt1XUm3zJDUlUv0NCj7H5MMPmsdWp4YUnm3abPoO-j7Ohc38nWioybYuIUXudAGRAWt-_FREMdUbL5Hi_PQ80lXqWfqQfGJ9MOlxF1mrpUiob3KsnbIXgsf05uzvvILQP1rTOEZJPLAPfAY4crVI6_6iMJoJeM0cbDak1VZ1NZiYZQi1QaVedhya1ADkX9ihzPzozZetEVEtx-VL3Dkl6Z-lVRfOlCHFSDdZXgptmqc2l4n8WJHS_qCvU2xroWzFrZ2eN0mk8_DkidYa0iLDS_1UQqoLUULdYXocbU06dIHU87Sq53DQq77WvdEQOs0FqOsBrX2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58ec6b7e1.mp4?token=KMYiQF46dhpZzgtt1XUm3zJDUlUv0NCj7H5MMPmsdWp4YUnm3abPoO-j7Ohc38nWioybYuIUXudAGRAWt-_FREMdUbL5Hi_PQ80lXqWfqQfGJ9MOlxF1mrpUiob3KsnbIXgsf05uzvvILQP1rTOEZJPLAPfAY4crVI6_6iMJoJeM0cbDak1VZ1NZiYZQi1QaVedhya1ADkX9ihzPzozZetEVEtx-VL3Dkl6Z-lVRfOlCHFSDdZXgptmqc2l4n8WJHS_qCvU2xroWzFrZ2eN0mk8_DkidYa0iLDS_1UQqoLUULdYXocbU06dIHU87Sq53DQq77WvdEQOs0FqOsBrX2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ان‌بی‌سی نیوز : وقتی رئیس جمهور ترامپ در بازی سوم فینال NBA هنگام پخش سرود ملی روی جایگاه تماشاگران در مدیسون اسکوئر گاردن ظاهر شد، توسط جمعیت (BOOE) هو شد.
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/14094" target="_blank">📅 09:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14093">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پنتاگون شرکت‌های BYD، Alibaba و Baidu را به فهرست شرکت‌های متهم به همکاری با ارتش چین اضافه کرد.
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/14093" target="_blank">📅 09:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14092">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نیویورک تایمز:  یک فروند بالگرد نظامی آمریکا دیروز دوشنبه در نزدیکی تنگه هرمز سقوط کرد و خدمه آن به سلامت نجات یافتند.
هنوز مشخص نیست که آیا این بالگرد توسط آتش‌ ایران سرنگون شده یا دچار نقص فنی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/14092" target="_blank">📅 09:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14091">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره لیندزی گراهام:
او برجسته است. مدت‌ها در کنار من بوده است.
ما ابتدا مدت‌ها پیش بر سر موضوع کاندیداتوری با هم مبارزه کردیم. او کاندیدا بود و من هم کاندیدا بودم، و ما مبارزه کردیم، و من شروع کردم به این که بفهمم او فردی بسیار بااستعداد است.
بعد از آن مبارزه، ما بهترین دوستان شدیم و او به من به اندازه هر کسی در سنا کمک کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14091" target="_blank">📅 02:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14090">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ: در دو هفته آینده "پیروزی کامل" را بر ایران اعلام خواهم کردم!
رئیس جمهور ایالات متحده: من فکر می‌کنم که ما در آن نبرد پیروز می‌شویم، اما شما واقعاً در دو هفته آینده که پیروزی کامل را اعلام می‌کنیم، پیروز خواهید شد.
این یک پیروزی کامل خواهد بود. خیلی زود این اتفاق می افتد و قیمت نفت پایین می آید.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14090" target="_blank">📅 01:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14089">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کن کلیپنشتاین، روزنامه‌نگار آمریکایی، مدعی شده اسناد محرمانه‌ای را دیده که نشان می‌دهد بخشی از نیروهای لشکر ۸۲ هوابرد آمریکا در آوریل ۲۰۲۶ به‌طور مخفیانه به اسرائیل اعزام شده‌اند. به ادعای او، این نیروها در چارچوب برنامه‌ریزی مشترک آمریکا و اسرائیل برای سناریوهایی از جمله تصرف جزیره خارگ ایران و ایجاد یک منطقه ساحلی در داخل خاک ایران آماده شده بودند. این ادعا تاکنون از سوی پنتاگون یا دولت آمریکا به‌صورت رسمی تأیید نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14089" target="_blank">📅 01:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14088">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ به اسکای نیوز:
من فکر نمی کنم اسرائیل به جنگ با ایران بازگردد. همه چیز خیلی خوب پیش می رود.
ایران کاری را که باید انجام دهد انجام می دهد. من فکر نمی کنم این اتفاق بیفتد، اوکی؟
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14088" target="_blank">📅 01:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14087">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">زلزله شدید بندرعباس الان @withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14087" target="_blank">📅 01:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14086">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یک منبع جمهوری اسلامی به الجزیره: آمریکا تغییرات غیرقابل قبولی در پیش‌نویس یادداشت تفاهم ایجاد کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14086" target="_blank">📅 00:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14085">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">جنگنده غرب تهران
قشنگ دیده میشد
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14085" target="_blank">📅 00:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14084">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">زلزله شدید بندرعباس الان
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14084" target="_blank">📅 00:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14083">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">صدا جنگنده در آسمان تهران
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14083" target="_blank">📅 00:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14082">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حمله پهپادی حزب‌الله به اسرائیل
🚨
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14082" target="_blank">📅 00:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14081">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش صدای انفجار از‌ دروازه دولت
🚨
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14081" target="_blank">📅 00:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14080">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارش از وقوع انفجار مهیب در محدوده گیشا تهران؛ لرزش شدید ساختمان‌ها و شیشه‌ها.
هجوم شهروندان به خیابان‌ها در پی شنیده شدن صدای انفجار و ایجاد رعب و وحشت.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14080" target="_blank">📅 00:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14079">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یک پهپاد از لبنان به شمال اسرائیل نفوذ کرد و آژیرها به صدا درآمدند
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14079" target="_blank">📅 00:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14078">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">جروزالم پست :  هشدار نفوذ پهپادها گالیلای علیا و جولان (1 مکان). در حال به‌روزرسانی...
وارد اتاق امن شوید و تا اطلاع ثانوی در آن بمانید
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14078" target="_blank">📅 00:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14077">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArad</strong></div>
<div class="tg-text">گیشا یک صدایی شد پنجره لرزید و مردم چند نفر ریختند بیرون</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/14077" target="_blank">📅 00:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14076">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمکران</strong></div>
<div class="tg-text">صدای انفجار اومد سیریک ولی دور بود</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14076" target="_blank">📅 00:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14075">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAli</strong></div>
<div class="tg-text">فکر کنم گیشا رو زدن</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14075" target="_blank">📅 00:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14074">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وزیر دادگستری لبنان: حزب‌الله باید سلاح خود را به دولت لبنان تحویل دهد تا موضع مذاکراتی ما تقویت شود. مذاکره جایگزینی جز گرداب جنگ‌ها و ویرانی ندارد. جنگ به اشغال شدن بخش بزرگی از جنوب لبنان منجر شده است.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14074" target="_blank">📅 00:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14073">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فارس:
جنگنده‌های اسرائیلی
در  عملیات‌های شب گذشته
بدون ورود به آسمان ایران
و از خارج از مرزهای کشور اقدام به شلیک تسلیحات دورایستا کرده‌اند.
این تغییر الگو نشانه‌ای از افزایش ریسک ورود مستقیم جنگنده‌های دشمن به حریم هوایی ایران بود
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14073" target="_blank">📅 00:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14072">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مقام ایرانی به الجزیره: توافق فقط به شرط آزادی دارایی‌های ایران حاصل می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14072" target="_blank">📅 23:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14071">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یک مقام آمریکایی به Axios گفت:
بی بی برای زنده ماندن سیاسی در اسرائیل نیاز دارد که جنگ ادامه یابد، و ترامپ برای زنده ماندن سیاسی در آمریکا نیاز دارد که جنگ پایان یابد.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14071" target="_blank">📅 23:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14070">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">@withyashar
جنگ مخفی</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14070" target="_blank">📅 23:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14069">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سامانه های پدافندی آمریکا در اقلیم کردستان، عراق در حال فعالیت می‌باشند.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14069" target="_blank">📅 23:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14068">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">جنگنده های آمریکایی در شمال عراق به پرواز درآمدند.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14068" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14067">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e393b6e499.mp4?token=dEvym4isFW47mwGWlkQFzcZLxl23Mx_NC6E3k1apoQq_zw_XEvum-iHM6fNARV8iGToKepa5nP7rGB-EuW2BDPME9EzjFMBcp69GQvS5btuyMMxYjPVxKHFVbYrovAfwFFBua8wnYn4E85KoeN0A3LCOmQgY19CUDlMecC-yb8tydnMbPQZZgCf0V23asBd0_g1JDNAjW2c2xwSUwB4MdWSLC9TRbj0pxjtBQHUmDlEXebU6kLeoMKJ7mQ69CIjnSx4k4xHDhDOpxFKAaeORLh3d0aFBdgutYNAec50MQbovY3UG5qh3IhgM0VDN6DGePqrKZaRGEyCLJ6os2o5lNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e393b6e499.mp4?token=dEvym4isFW47mwGWlkQFzcZLxl23Mx_NC6E3k1apoQq_zw_XEvum-iHM6fNARV8iGToKepa5nP7rGB-EuW2BDPME9EzjFMBcp69GQvS5btuyMMxYjPVxKHFVbYrovAfwFFBua8wnYn4E85KoeN0A3LCOmQgY19CUDlMecC-yb8tydnMbPQZZgCf0V23asBd0_g1JDNAjW2c2xwSUwB4MdWSLC9TRbj0pxjtBQHUmDlEXebU6kLeoMKJ7mQ69CIjnSx4k4xHDhDOpxFKAaeORLh3d0aFBdgutYNAec50MQbovY3UG5qh3IhgM0VDN6DGePqrKZaRGEyCLJ6os2o5lNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو از رهگیری موشک یا پهپاد های جمهوری اسلامی توسط امریکا همکنون در عراق
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14067" target="_blank">📅 23:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14066">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">واقعا یه خبرایی ‌هست
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/14066" target="_blank">📅 23:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14065">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">هم اکنون گزارش‌های تایید نشده از عراق، حاکی از حمله پهپادی گسترده ایران به پایگاه‌های آمریکا / کرد ها در شمال عراق است.
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14065" target="_blank">📅 23:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14064">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هم اکنون گزارش‌های تایید نشده از عراق، حاکی از حمله پهپادی گسترده ایران به پایگاه‌های آمریکا / کرد ها در شمال عراق است.
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14064" target="_blank">📅 23:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14063">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وزارت خارجه آمریکا: آزادی اموال بلوکه شده، مادامی که ایران به تعهدات خود پایبند نشود، رخ نخواهد داد
محاصره دریایی اعمال شده علیه ایران تا دست‌یابی به توافق پابرجا خواهد ماند
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14063" target="_blank">📅 23:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14062">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کاور @withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14062" target="_blank">📅 22:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14061">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">برم اتاق جنگ رو پست کنم</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14061" target="_blank">📅 22:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14060">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">استان یزد فردا تعطیل شد
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14060" target="_blank">📅 21:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14059">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ: جمهوری اسلامی از ما خواست تا اسرائیل حملاتش به ایران را متوقف کند
@withyashar
جمهوری اسلامی هم میگه آمریکا خواست
🤣</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14059" target="_blank">📅 21:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14058">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14058" target="_blank">📅 21:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14057">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14057" target="_blank">📅 21:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14056">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">صدا های مشکوک به انفجار‌ همکنون تهران
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14056" target="_blank">📅 21:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14055">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14055" target="_blank">📅 21:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14054">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14054" target="_blank">📅 21:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14053">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐀𝐥𝐢 🇺🇸𝐬𝐡𝐚𝐤𝐮𝐫</strong></div>
<div class="tg-text">درود سرباز شاه پیام که برای رضا پهلوی (شاهزاده ) فرستادی پاک کنین ، دشمن دنبال همین پیام ها هستن ، همه میدونیم ادمین کسی دیگس</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14053" target="_blank">📅 21:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14052">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14052" target="_blank">📅 21:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14051">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from:)</strong></div>
<div class="tg-text">یاشار دادا فکر کنم اون گز اجیلی که از چهارماه پیش برای روبیو  و ونس بردن تازه داره دعا جادوش  عمل میکنه جنس ایرانیه  دووم  نداره دیر کار شروع میشه زودم تموم میشه
اینا تموم شدن. اینم مثل جنگ ۱۲ روزه یه تست بود که بییین اینا چقدر داستان دارن که فهمیدن فقط بوق کرناس هیچی ندارن
✌🏻
دمتم گرم خسته نباشید
❤️</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14051" target="_blank">📅 21:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14050">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ به کانال 12 اسرائیل:
به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کنه، اونو تنها خواهم گذاشت.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14050" target="_blank">📅 20:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14049">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ : اسرائیلی‌ها وقتی جنگنده‌هاشون تو مسیر ایران بودن، به ما خبر دادن
من هم سریع وارد عمل شدم و تلاش کردم ابعاد حمله محدودتر بشه
همچنین پنج کشور منطقه با من تماس گرفتن و خواستن روی نتانیاهو فشار بیارم که حمله نکنه
من هم با نتانیاهو صحبت کردم و اون در نهایت موافقت کرد
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14049" target="_blank">📅 20:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14048">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اولین تصاویر از حمله به یک کشتی باری با پرچم پالائو با ۲۴ خدمه هندی در نزدیکی تنگه هرمز ساعتی پیش , بر اساس این گزارش‌ها، در این حمله موتورخانه کشتی هدف قرار گرفته است. @withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14048" target="_blank">📅 20:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14047">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14047" target="_blank">📅 20:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14043">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فرماندهی مرکزی آمریکا (CENTCOM) اعلام کرد نفتکش
Marivex
با پرچم کشور پالائو را در حالی که از آب‌های بین‌المللی دریای عمان
به سمت ایران در حرکت بود
، هدف قرار داده است.
پس از آنکه خدمه کشتی از اجرای دستورات نیروهای آمریکایی خودداری کردند، یک فروند جنگنده
F/A-18 سوپر هورنت
مستقر بر روی ناو هواپیمابر
آبراهام لینکلن (CVN-72)
یک مهمات هدایت‌شونده دقیق را به بخش موتورخانه و سامانه هدایت کشتی شلیک کرد
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14043" target="_blank">📅 20:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14042">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حریم هوایی ایران در حال باز‌ شدن است
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14042" target="_blank">📅 20:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14041">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وزارت دفاع عربستان سعودی اعلام کرد که یک موشک بالستیک که صبح زود از یمن شلیک شد، دچار نقص فنی شد، از مسیر برنامه‌ریزی شده منحرف گردید و در نهایت در منطقه‌ای غیرمسکونی نزدیک مرز عربستان و یمن سقوط کرد.
این موشک توسط حوثی‌ها (انصارالله) شلیک شده بود.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14041" target="_blank">📅 19:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14040">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نتانیاهو: همانطور که به دوست خودم ترامپ میگم: ما اسرائیل رو با عزم و هوشمندی دفاع خواهیم کرد و با هم امنیت رو به شمال اسرائیل بازخواهیم گرداند. @withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14040" target="_blank">📅 19:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14039">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: حملات موشکی ما تا برقراری آتش‌بس در لبنان ادامه داره
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14039" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14038">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نتانیاهو: ایران و حزب‌الله امروز از هر زمان دیگه‌ای ضعیف‌ترن و اسرائیل از همیشه قوی‌تره، اما کارزار ما علیه اون‌ها هنوز تموم نشده. تو 24 ساعت گذشته، ایران و حزب‌الله سعی کردن قواعد جدیدی به ما تحمیل کنن، اما من این موضوع رو نمی‌پذیرم. همون‌طور که سال‌هاست انجام دادم، روی حق اسرائیل برای پاسخ دادن به این حملات پافشاری می‌کنم.
و اگه ایران دوباره اشتباه کنه و حملاتش رو از سر بگیره، با قدرت بهش پاسخ خواهیم داد، اسرائیل حق دفاع از خودش رو داره و این حق رو حفظ خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14038" target="_blank">📅 19:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14037">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نتانیاهو: همانطور که به دوست خودم ترامپ میگم: ما اسرائیل رو با عزم و هوشمندی دفاع خواهیم کرد و با هم امنیت رو به شمال اسرائیل بازخواهیم گرداند.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14037" target="_blank">📅 19:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14036">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نتانیاهو: ایران نمیتونه معادلات رو به ما تحمیل کنه. من این موضع رو تأیید میکنم. پس از اینکه حزب‌الله به اسرائیل شلیک کرد، ما به بیروت حمله کردیم. و پس از اینکه ایران به اسرائیل حمله کرد، ما به مناطق دیگری در ایران حمله کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14036" target="_blank">📅 18:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14035">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نتانیاهو: در حال حاضر آتش در جبهه ایران محصور است، زیرا پس از اینکه رژیم تروریستی در تهران آماده شد، دیگر به ما حمله نکرد. اگر دوباره به ما حمله کند - با قدرت پاسخ خواهیم داد
@withyashar</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/14035" target="_blank">📅 18:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14034">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c95feb74.mp4?token=l54uqQq3xep-w5Kv4zxdsaRH7-lydub4bYG9RQQ3WwQgtZKcXxE0VAAbjTLvvlV8HYASVH1ljzp-bzeYtqivsc6gxyEZVge71ad4hEiYotjwzWYiY0_YVedbcoUL50BfzzVCcjf46vMmGr9FmwhIHlXl6YzE-b753lDxVKXqfh0XkHrMBXXpyK1zf5uj70-jh1_hFjlk4x6_HDg3Xba9GeNuToxplWGbezI1ChNrDp1b9FPTQCieiI0nJPebuV1HQUWmDeWsy2ijTmMiCdcrC5fGajqlcM9DV5d-DYck72O-6byH06-RMfmVWfBJ0iesdSk32auElcpDAxZtD9L1QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c95feb74.mp4?token=l54uqQq3xep-w5Kv4zxdsaRH7-lydub4bYG9RQQ3WwQgtZKcXxE0VAAbjTLvvlV8HYASVH1ljzp-bzeYtqivsc6gxyEZVge71ad4hEiYotjwzWYiY0_YVedbcoUL50BfzzVCcjf46vMmGr9FmwhIHlXl6YzE-b753lDxVKXqfh0XkHrMBXXpyK1zf5uj70-jh1_hFjlk4x6_HDg3Xba9GeNuToxplWGbezI1ChNrDp1b9FPTQCieiI0nJPebuV1HQUWmDeWsy2ijTmMiCdcrC5fGajqlcM9DV5d-DYck72O-6byH06-RMfmVWfBJ0iesdSk32auElcpDAxZtD9L1QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
اگر رژیم جمهوری اسلامی اشتباه کند و حملات خود را علیه ما از سر بگیرد، ما به شدت پاسخ خواهیم داد، زیرا اسرائیل حق دفاع از خود را دارد و ما این حق را حفظ خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14034" target="_blank">📅 18:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14033">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رئیس جدید موساد، رومن گوفمن : مردم ایران را مسلح کنید , بازی را تغییر دهید
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14033" target="_blank">📅 18:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14032">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اسرائیل هیوم: درگیری 24 ساعت اخیر نشان داد قدرت نظامی ایران حتی نزدیک به شرایط قبل از جنگ هم نیست.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14032" target="_blank">📅 18:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14031">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">قالیباف: معادله آتش‌‌بس روی کاغذ و نقض مکرر آن در میدان رو به هم زدیم. تا زمانی که ارادهٔ واقعی برای اعتمادسازی نداشته باشید، پاسخ ایران همین خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14031" target="_blank">📅 18:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14030">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رسانه I24News: اسرائیل به پمپی که مواد را در کارخانه بزرگ پتروشیمی در ایران حمل می‌کند حمله کرد. حمله‌ای به یک قطعه حیاتی (و گران‌قیمت) با هدف از کار انداختن کارخانه‌ها.
﻿
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14030" target="_blank">📅 18:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14029">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نتانیاهو دقایقی دیگه صحبت میکنه</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14029" target="_blank">📅 18:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14028">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">لغو تمام پروازهای کشور تا اطلاع ثانوی
شرکت فرودگاه‌ها و ناوبری هوایی ایران:‌
در پی صدور اطلاعیه رسمی هوانوردی (NOTAM) توسط سازمان هواپیمایی کشوری مبنی بر بسته‌شدن فضای پروازی غرب کشور، تمامی پروازهای فرودگاه‌های سراسر کشور تا اطلاع ثانوی لغو شده و انجام نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14028" target="_blank">📅 16:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14027">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906b9a08b0.mp4?token=ahemgY3ZDc-wf-Ohal8nJQi2oCbWwnERf2BpEss-hAJo0wDs7vUaK_7o1bNwoQkcl2k70VooTKZpuBlsaTEdUJ7TACfSLQhFeD_7Nf5fXE56MR5ai3nEwx-9eEjYKKMYi1FqKckyX28WOnFxeV004UnXT9bHHMY9GBwkem86FlCxD9TO_355q5sisaC4uiE5dDoFiU5bX0rhIfn9BqTRvy5mKo6z5Tt1uoJv44_kML5XBFzPEIrZ2N7c8LJBCdLvcIZDX-SFX0UbDWASMHj49Cmrrg4r6KiZc84lSM8BVr-VBqLvNJi_wNI_ZarD9jRhKRwSOCsR1zzGYO84TfooHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906b9a08b0.mp4?token=ahemgY3ZDc-wf-Ohal8nJQi2oCbWwnERf2BpEss-hAJo0wDs7vUaK_7o1bNwoQkcl2k70VooTKZpuBlsaTEdUJ7TACfSLQhFeD_7Nf5fXE56MR5ai3nEwx-9eEjYKKMYi1FqKckyX28WOnFxeV004UnXT9bHHMY9GBwkem86FlCxD9TO_355q5sisaC4uiE5dDoFiU5bX0rhIfn9BqTRvy5mKo6z5Tt1uoJv44_kML5XBFzPEIrZ2N7c8LJBCdLvcIZDX-SFX0UbDWASMHj49Cmrrg4r6KiZc84lSM8BVr-VBqLvNJi_wNI_ZarD9jRhKRwSOCsR1zzGYO84TfooHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خطر
⚠️
اگه ناراحتی قلبی دارید نبینید
🤣
بی اختیاری ادرار میاره
این ویدئو رو صدا و سیما خودشون پخش کرد!
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی برای تنگه هرکز
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14027" target="_blank">📅 16:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14026">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بریتانیا هشدار تخلیه به شهروندانش از اسراییل رو صادر کرد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14026" target="_blank">📅 16:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14025">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRH4nEDCT2utMH3ssORjd38ko9cX-obCx8jFCa4tp0Y6Jaw37k4i-4i0rdD5cY1AXpc9oceyh6nbegqetbDREUb4XKx5qRNlglPDaXWmlZjF891M27cDqH2spWfLWCnZgo3S-Bzwefy15RSJ1yAOsPovGGnmgR5AwwXjPwweuY2ocTiILoQu3ovZtzE6e3zMUK0eKTrc88O4KymOXKGPJxf_jtvt0r8I6fkNtLZEXGcZz3_zVf_N_x_kfcenv9CxKkMirfTV0C6nfbr_ZqgCUvwiBbw4oP3OxP43hd8p0ATTH0Gsiv_IFA18jd8rY9-Ln4W18kmWaQ6ZXMqHGqklcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل هم داره جنوب لبنان رو خیلی شیک و مجلسی هوایی میزنه.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14025" target="_blank">📅 16:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14024">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14024" target="_blank">📅 16:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14023">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترافیک سنگین در محورهای چالوس و هراز
@withyashar
خوش بگذره به هم وطنام
❤️‍🩹
جای‌منو خالی کنید</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14023" target="_blank">📅 16:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14022">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14022" target="_blank">📅 16:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14021">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVr2J7k4WS92Pj5TPKH8X_XqKoYRduJvjTENgsrf1lsXE2YgQBH0NH7jAksVS7jgpUZL4VHNOU0p08aiKcnc90JtvDm8GEL4ZDpjPITU2cpzrH6wwYfgfHtuQSCj2s4aMsUMqMifPrY8DIEHaSyV0f_tzRbn_hD26ByZli49hC4olf-tRyJ5JQUKkyIhkWFFMkiQymU_xeJ_9dKqeUd9U0uZreKVvUGlphhPuZAGS8ZYm89uyEgutYOxlbZyYQx036EuW3PWcYyUVtJSS3INtGoUFILTCQknV_QgADpmj85KRWR-5gdNJWEGx_mKwliXyZnbU60GkHv8aQ9N2lCyFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14021" target="_blank">📅 16:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14020">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14020" target="_blank">📅 16:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14019">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حزب‌الله هم حمله موشکی کرد به سمت اسرائیل و آژیرها فعال شد.
اسرائیل : 5 موشک رهگیری شد.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14019" target="_blank">📅 15:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14018">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یک مقام آمریکایی به آکسیوس:
تماس تلفنی ترامپ با نتانیاهو «مودبانه» بوده، اما نتانیاهو با درخواست ترامپ برای توقف اقدامات بیشتر مخالفت کرده.
به نتانیاهو صراحتا گفته شد که این چرخه باید پایان یابد. آمریکا با این حملات موافقت نکرد و از آنها حمایت نکرد.
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14018" target="_blank">📅 15:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14017">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">عراق از بازگشایی حریم هوایی خود خبر داد
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14017" target="_blank">📅 15:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14016">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کانال 12 اسرائیل: ترامپ و نتانیاهو دقایقی پیش صحبت کردن.
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14016" target="_blank">📅 15:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14015">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">هم اکنون اسرائیل به لبنان حملهِ کرد
@withyashar
😁</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/14015" target="_blank">📅 15:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14014">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">صدا و سیما:جنگ پس از شکست دشمن به پایان رسید و زندگی به روال عادی بازگشت
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14014" target="_blank">📅 15:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14013">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تحلیل کمی دیگه در‌اینستاگرام پست میشه</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14013" target="_blank">📅 15:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14012">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ به نیوزنیشن: یک جنگ دیگر را پایان دادم
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14012" target="_blank">📅 15:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14011">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=fMsT7szlNTyIyzHrJplNgERZZKaE7swnrBnc5wlDexv2cfuvHfJF4CDu9odrhg5pxwmEh_a2IEKrHA8DHHqLyftb-59pKmABeo97yfZXLozKOkQI42nNxBCjeGgGffPeWhRgMFqZWeKnVlrqIrpdSCIEHFJT2mYgD1BoDxRQYEkbkfDqh81wT65aFZBy8f39G_c1J94-sAfQ5IJzwi0XHXIaUEuzPl5u4bMfd0BVAfR55chqSET3gmyJRszt0BAhhQk_UgHkf9kPEoq7e6cr8sZDjTReqBSQVQ2ik7elHEHFyJysf7TsySUzo7UrVoSkltJvuiiwESlu7EYU7tczQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=fMsT7szlNTyIyzHrJplNgERZZKaE7swnrBnc5wlDexv2cfuvHfJF4CDu9odrhg5pxwmEh_a2IEKrHA8DHHqLyftb-59pKmABeo97yfZXLozKOkQI42nNxBCjeGgGffPeWhRgMFqZWeKnVlrqIrpdSCIEHFJT2mYgD1BoDxRQYEkbkfDqh81wT65aFZBy8f39G_c1J94-sAfQ5IJzwi0XHXIaUEuzPl5u4bMfd0BVAfR55chqSET3gmyJRszt0BAhhQk_UgHkf9kPEoq7e6cr8sZDjTReqBSQVQ2ik7elHEHFyJysf7TsySUzo7UrVoSkltJvuiiwESlu7EYU7tczQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14011" target="_blank">📅 15:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14010">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌: توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما در صورت تداوم حملات، از جمله در جنوب لبنان، اقدامات شدیدتر در راه خواهد بود @withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14010" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14009">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌: توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما در صورت تداوم حملات، از جمله در جنوب لبنان، اقدامات شدیدتر در راه خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14009" target="_blank">📅 14:53 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
