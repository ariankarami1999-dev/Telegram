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
<img src="https://cdn4.telesco.pe/file/Z2T89BQRusUv1VSU_bRwyVGnfPQesz229YDZPM6017IpEd_yz3sxcqcLhUk1CfYSgFeUBRjNueZJVfmDJDxCZmgODaLoKAYpQbIbX-1tvkXQiAHcmTsw1u4gK0zmnPo_XRxunVZnxzX1WfA7aY3qygFc5oLk-s0U5_wruffenDKVjhbTuubPMDW3XO7m2dqjPynwBXIYyOFEmNq-1-YhxPTcfMVLLxPCFhLfzXbNJvja7w3jk0Bn0PgA5fm8wPKFmXi6gRHbWgKDX-Q1gxkZEUgNZwjnU_IXJIkC7LVV046wYvYGFSyLfOt3fCzZkSbz2qyNv4Gx5ZUsoKN_othIAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 488K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 13:03:45</div>
<hr>

<div class="tg-post" id="msg-25082">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">به یاد قربانیان بی‌گناه حمله تروریستی ۷ اکتبر @WarRoom</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/withyashar/25082" target="_blank">📅 12:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25081">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d91c52f407.mp4?token=iV4kNfo0s8T9_HriXqdVNff3PQLOmh48F0DzImQq0rc8Mb685YQPgmHqABy_inio_Z9Q9YYeF5JOklDRPtHgDD-AQO6gHvG5jreHQp-vLEbYXgT0-W5pvhz4n2-iOmE-RPJfuf1_ndmxfSuDcBnTMp9IAQZ3tDRnPGMB9g9oEbYRPwcweyUuwCpE9M7Kxt5Qn9ZQO67AYIFM0Q9HrgLdId2r2RWN5XPYC_pb2BHBqDzoLZDpSQeYIzYdu0AtXdPTR1lAj4fX23MnVjx-FUBTfgqNmErZMEsx0aM-gEv6cSvEujsUjg_11UhOtDvlp7LX49YdvNCP56GP4ajKv8nswQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d91c52f407.mp4?token=iV4kNfo0s8T9_HriXqdVNff3PQLOmh48F0DzImQq0rc8Mb685YQPgmHqABy_inio_Z9Q9YYeF5JOklDRPtHgDD-AQO6gHvG5jreHQp-vLEbYXgT0-W5pvhz4n2-iOmE-RPJfuf1_ndmxfSuDcBnTMp9IAQZ3tDRnPGMB9g9oEbYRPwcweyUuwCpE9M7Kxt5Qn9ZQO67AYIFM0Q9HrgLdId2r2RWN5XPYC_pb2BHBqDzoLZDpSQeYIzYdu0AtXdPTR1lAj4fX23MnVjx-FUBTfgqNmErZMEsx0aM-gEv6cSvEujsUjg_11UhOtDvlp7LX49YdvNCP56GP4ajKv8nswQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روبیو، وزیر امورخارجه: اقتصاد ایران در آستانه رسیدن به وضعیتی قرار دارد که تعداد بسیار کمی از کشورهای جهان تاکنون از نظر شدت وخامت اقتصادی تجربه کرده‌اند آنها مردم ایران را در شرایطی قرار داده‌اند که اکنون در آن به سر می‌برند
@WarRoom</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/withyashar/25081" target="_blank">📅 12:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25080">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مارک لوین درباره خبر (نکشتن ده نفر برای اداره آیندهی ایران توسط سیا) : «نگرانم که سیا حتی بیش از حد محتاط و ریسک‌گریز باشد و همچنین با مسلح کردن مردم ایران مخالفت کند. این موضوع بسیار نگران‌کننده است.» @WarRoom.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/withyashar/25080" target="_blank">📅 12:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25079">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">العربیه: نیروی هوایی یمن بامداد چهارشنبه ۱۵ مهر، در پنج حمله
انبارهای موشک‌های بالستیک، پایگاه شلیک موشک و مخفیگاه‌های سلاح حوثی‌ها
را در اردوگاه ماس و اطراف آن در شمال مأرب هدف قرار داد. در منطقه مفرق الجوف نیز تجهیزات نظامی و یک نفربر حوثی‌ها که از صنعا برای تقویت جبهه‌های الجوف در حرکت بود، هدف قرار گرفت. هم‌زمان درگیری‌های شدیدی میان نیروهای دولتی یمن و حوثی‌ها در جنوب‌غرب تعز ادامه دارد و نیروهای دولتی چند ارتفاع راهبردی را تصرف کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/withyashar/25079" target="_blank">📅 12:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25078">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روبیو، وزیر خارجه آمریکا: ایران فرصت‌های متعددی برای توافق درباره برنامه هسته‌ای خود را از دست داده است. ایران هرگز به سلاح هسته‌ای دست نخواهد یافت و ترامپ اجازه نخواهد داد ایران با تلاش برای خروج نیروهای آمریکا از منطقه به این هدف برسد. نمی‌توان پذیرفت یک کشور به‌تنهایی کنترل یک مسیر مهم دریایی را در اختیار داشته باشد؛ باید منابع و مسیرهای متنوعی برای تأمین انرژی وجود داشته باشد. تنگه هرمز باز است و حجم نفت عبوری از آن اکنون دقیقاً برابر با میزان پیش از بسته‌شدن تنگه است.
@WarRoom</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/withyashar/25078" target="_blank">📅 12:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25077">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رویترز: بیت‌کوین امروز حدود ۱.۷۶ درصد کاهش یافت و به محدوده ۸۴ هزار دلار رسید؛ اتریوم نیز حدود ۳.۳ درصد افت کرد و به محدوده ۲۶۱۰ دلار رسید. تقویت دلار، افزایش بازده اوراق خزانه آمریکا و نگرانی‌های ناشی از تشدید تنش‌های ایران و خاورمیانه از عوامل فشار بر بازار رمزارزها هستند.
بیش از
۴۰۰ میلیون دلار موقعیت لانگ
در بازار کریپتو لیکویید شد و بیت‌کوین در فاصله حدود ۲۰ دقیقه نزدیک ۲ هزار دلار از ارزش خود را از دست داد. مجموع لیکوییدیشن‌های ۲۴ساعته بازار به بیش از
نیم میلیارد دلار
رسید.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/25077" target="_blank">📅 11:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25076">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pz-_LLwSTw4Ikx8pVXMrpS3-a9YN8h28vnsc42SgjM0O3iOXsD2B_I9u7oqvUGvHYDDawTmLUDgt5_Z66c-qeRK0Pw5nOo-hoxKivbWm2w1SDSXM_EjQzm9Vp6XBX8o20Pr1ARUJgLvwYvUfNOeuebnDFd_KXvJm3ROoDJbq8cN-e5t58e2WEqwZvwCeQSA7YYWiYSQvuVXlGXvPfqr3hgk1NJwYtUxR2z7qCArEHx3D64RyIshBJFXj_0qxJzZd345N-NOtULLD5kiZ_bGsuw-WFUdnvq--EModju3xvuuhHJ8T9SV2ik59L3YMcvyk6sghoud6nVsZ00HECY9Kuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جروزالم پست:
تصاویر ماهواره‌ای از سایت هسته‌ای «تأسیسات اتمی لویزان» (معروف به تأسیسات مژده) افزایش رفت‌وآمد و عملیات عمرانی را نشان می‌دهد؛ این سایت از سوی اسرائیل به فعالیت‌های مرتبط با
توسعه تسلیحات هسته‌ای ایران
مرتبط دانسته شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/withyashar/25076" target="_blank">📅 10:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25075">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">منابع هندی اعلام کردند یک کشتی تجاری با پرچم پاناما امروز، ۶ اکتبر, ۱۴ مهر هنگام عبور از نزدیکی تنگه هرمز و سواحل عمان هدف یک پرتابه ناشناس قرار گرفته و ۱۱ خدمه هندی زخمی شده‌اند. تاکنون هویت عامل حمله به‌طور رسمی اعلام نشده ولی این حمله به سپاه نسبت داده…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/25075" target="_blank">📅 10:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25074">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فایننشال تایمز:
به دلیل خطر عبور از تنگه هرمز، ناخدای نفتکش‌ها اکنون تا
۱۰۰ هزار دلار در ماه
و حدود ۵۰ هزار دلار پاداش برای هر عبور دریافت می‌کنند؛ نرخ بیمه خطر جنگ برای برخی نفتکش‌ها نیز به حدود
۲۰ میلیون دلار در هر سفر
رسیده است.
@WarRoom</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/25074" target="_blank">📅 10:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25073">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079c75e928.mp4?token=o1l3WHWpbE8c47Wzo7BW_Ah5eT6EB2vG3NH2FsCehL2Arv4NEMoqoa9HNbpUedHhhy6v0hgxg5E6VZVKlT2WAhCJEW5MWWgQXJ9rf_w-K7E8UDfVD5Xsx1tU3QEnW-v8EKZDAhutq7BNEl4TK2uEJnV_hjOgkk2ou97DVMNtssBALPx8fSy5DLVp38t5UJ9Lq046ilndEG5OmvCQ-kHzIXsW8M5NqkYfh6F5lld-X91EwunYaH111qzYs8Gu_JomFtwIA2TGVR4LxOqkil9RQmSqOqwbHBW24vxur8qt2YRM0azuxPf1hksILCTiXs503i16Y9wNBx8n2-OvpvB5xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079c75e928.mp4?token=o1l3WHWpbE8c47Wzo7BW_Ah5eT6EB2vG3NH2FsCehL2Arv4NEMoqoa9HNbpUedHhhy6v0hgxg5E6VZVKlT2WAhCJEW5MWWgQXJ9rf_w-K7E8UDfVD5Xsx1tU3QEnW-v8EKZDAhutq7BNEl4TK2uEJnV_hjOgkk2ou97DVMNtssBALPx8fSy5DLVp38t5UJ9Lq046ilndEG5OmvCQ-kHzIXsW8M5NqkYfh6F5lld-X91EwunYaH111qzYs8Gu_JomFtwIA2TGVR4LxOqkil9RQmSqOqwbHBW24vxur8qt2YRM0azuxPf1hksILCTiXs503i16Y9wNBx8n2-OvpvB5xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به یاد
قربانیان بی‌گناه حمله تروریستی ۷ اکتبر
@WarRoom</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/25073" target="_blank">📅 10:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25072">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بر اساس گزارش جدید منابع حقوق بشری، جمهوری اسلامی از زمان اعتراضات ژانویه(دی) به‌طور میانگین
نزدیک به دو نفر در هفته
را در پرونده‌های سیاسی و امنیتی اعدام کرده و ۱۹۴ نفر دیگر با حکم اعدام روبه‌رو هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/25072" target="_blank">📅 09:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25071">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ایرنا:
تهران به بحرین و دیگر کشورهای منطقه هشدار داد اجازه استفاده از خاک یا حریم هوایی خود برای حمله به ایران را ندهند؛ ایران تهدید کرده در صورت تکرار چنین اقدامی پاسخ خواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/25071" target="_blank">📅 09:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25070">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajL19rA0QuihplzpJz-d5m3qRHe_8vA6lbWaGWZ2SoXop6XrmXnZKuoU6v7jNhRS4bkAHTy_FKqugnf2ZGOxMYX85RPKzIUY_ocU3F3tQJy5A5aTKiW0bwAmp3xbhYkzaTEMxbP32Rxi79S6-RJ1bLOsbkChzdHk7jbaxFeHrN9LSuuR9QZw-xSSFtXAb4AaeQz0GNQdlw1FkjIgsyORCQi8m6NwvWpaPbTr97UXtT2Oeza64ad_ZwBiFUBlkQ653f1_HCkOohZvKhPLxc5VjSMf5qtv11dR9nvy86JyFKIk-nUj-5hPLduD817ioHLi97u0Gdf_ePnnBkdllz_AZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منابع نظامی اسرائیلی تأیید کرده‌اند که نیروی هوایی و فضایی اسرائیل یک رزمایش بر فراز ایران انجام داده است.
در این رزمایش، جنگنده‌های پنهانکار
F-35I آدیر
شرکت داشتند و یکی از تانکرهای سوخت‌رسان جدید
KC-46A
اسرائیل، در حریم هوایی عراق به آنها سوخت‌رسانی کرده است.
این نخستین گزارش از استفاده عملیاتی از تانکرهای جدید KC-46A اسرائیل برای پشتیبانی از F-35I در یک مأموریت دوربرد بر فراز ایران است. پیشتر رژیم حتی تایید کرده بود که جنگنده های دشمن تست ورود به ایران را انجام داده‌اند و پروازها هم کنسل شدند
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/25070" target="_blank">📅 09:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25069">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/25069" target="_blank">📅 09:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25068">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcWQWsoLfL_rAHGss21gX8aB7JUX1ppfx_2rviuf0AhBKENvKKhihpF0iIul4L826k2jSx6YSECW9kYUxDIs27BaLX5GCEecyd8eIwGB_9KPdW7Pi48oEJW8dxyvnCe5q8OYJ56T6UR1qLO6sl7EYTq4ZDzkbECblMQ5-3ciqp403x3pserRCELloPgfqa5t59MLsEvnJMY_j0EGMWU6ULZaHsbXwEO9fulz8_CZ7mT1v1kMi8IE85lugVb8Pe6oC5URcVEwFPayknzLP92T2XkmPvAKBAW1zd_OM0qLRpMcf_XtE1SQta1ZJNKlXqC63uxijCReUsbsxo9n1RInlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ اسرائیل : سازمان سیا فهرستی از حدود ده مقام ارشد ایرانی را که نباید هدف ترور قرار گیرند، به اسرائیل ارائه کرده ، چهره‌هایی که واشنگتن معتقد است «می‌توانند نقش‌های کلیدی در دولت آینده ایران ایفا کنند». @WarRoom</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/25068" target="_blank">📅 09:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25067">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رویترز:
جی‌دی ونس گفت برای پایان جنگ، ایران باید
کاهش معناداری در ظرفیت غنی‌سازی اورانیوم
ایجاد کند و صرفاً وعده کاهش در آینده کافی نیست. ونس همچنین گفت آمریکا درباره اینکه چه کسی در تهران تصمیم نهایی را می‌گیرد، اطمینان ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/25067" target="_blank">📅 09:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25066">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b33fbf02be.mp4?token=E1Sf63phinZTpRAfJvQH4S4sIqAfz4Ts87P_VhCvjHeO2KRksEwP6xKpIkU3aelBrmtQDeriNguP09qEGVBs4rXaIRp2FsC0dkNhC0GM-z8KiAJWiAjdLj9i98o8gPG8_IpAxllTk-2W7KmUO1JPWqht3FF88TbaK2uJYHJd0JRMj0KDjp31oyp0fFgp6hmNMJt1qCgRwAIT8IhZ8nWgk_gszqWN4yGjTS8vRpHySEP27HVWWVMFinHHS1hyxYuYBWeHChO6GP3KDKzPnk-8JcSsuedsbiseB8S52BebxTXyaq7N5nlY9RpSHpmCxmseWsKc70pE_o-wAF-uxbhDwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b33fbf02be.mp4?token=E1Sf63phinZTpRAfJvQH4S4sIqAfz4Ts87P_VhCvjHeO2KRksEwP6xKpIkU3aelBrmtQDeriNguP09qEGVBs4rXaIRp2FsC0dkNhC0GM-z8KiAJWiAjdLj9i98o8gPG8_IpAxllTk-2W7KmUO1JPWqht3FF88TbaK2uJYHJd0JRMj0KDjp31oyp0fFgp6hmNMJt1qCgRwAIT8IhZ8nWgk_gszqWN4yGjTS8vRpHySEP27HVWWVMFinHHS1hyxYuYBWeHChO6GP3KDKzPnk-8JcSsuedsbiseB8S52BebxTXyaq7N5nlY9RpSHpmCxmseWsKc70pE_o-wAF-uxbhDwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جانسون، رئیس مجلس نمایندگان آمریکا:«ایرانی‌ها، البته، شرکای قابل اعتمادی برای مذاکره نیستند.
بعضی از آنها دروغ می‌گویند و این کار را بخشی از مذهب خود می‌دانند.
آنها می‌توانند دروغ گفتن به کافران را با استناد به مذهب توجیه کنند.
آنها نمی‌خواهند این مسئله را حل کنند. جهادی‌ها در رأس قدرت هستند؛ کسانی که واقعاً تا پای مرگ می‌جنگند و تلاش می‌کنند هر کسی را که با آنها مخالف باشد، بکشند.»
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25066" target="_blank">📅 01:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25065">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aec2707327.mp4?token=i49O0sM97YEFL92iMmGyckqH5R7wsqOdOYNZl9ltsRm5WffTAl1tpuLvtf_rSPUqae-BA4DzuAYwrhcB_GXYAsf7TjmX-LkpZtqmRJxDclRLRc43ejq97wlCbTvU5ACQTDN70NHjUot1pZulNQiJGqpFmFtDOdOBk2ZlXd1NIFZfpYHrORfC4lCfXmmmMW2wv6V1L3PThMYr0H3n-iiWOYi9YSO9sgPw0Uv7hrn-OfC-Fl_9vB79mvFe1Mii69WZgU6CAdO1f9TQp2SlX1M5Pf60iZ3Dp8YSNopOmxUfKeObwxve28UEqLcbbeDEZoiyGP255nHtEneEKSeqr4BBlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aec2707327.mp4?token=i49O0sM97YEFL92iMmGyckqH5R7wsqOdOYNZl9ltsRm5WffTAl1tpuLvtf_rSPUqae-BA4DzuAYwrhcB_GXYAsf7TjmX-LkpZtqmRJxDclRLRc43ejq97wlCbTvU5ACQTDN70NHjUot1pZulNQiJGqpFmFtDOdOBk2ZlXd1NIFZfpYHrORfC4lCfXmmmMW2wv6V1L3PThMYr0H3n-iiWOYi9YSO9sgPw0Uv7hrn-OfC-Fl_9vB79mvFe1Mii69WZgU6CAdO1f9TQp2SlX1M5Pf60iZ3Dp8YSNopOmxUfKeObwxve28UEqLcbbeDEZoiyGP255nHtEneEKSeqr4BBlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ :
«ما داریم
پول مردم را که در دوره ریاست‌جمهوری اوباما از آنها کلاهبرداری شده بود، به خودشان برمی‌گردانیم.
»
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25065" target="_blank">📅 01:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25064">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c507c5c1b.mp4?token=u66D7JdUNRd97NTt1hlxNrXMZ8ciogMlkFTIqekK_7UF7v4qA-ArpbcnFyEW3awgAo_czTtgv9lWgAU7tn4pJ9Ol06TbiXyvhASAPSJsMcGL8RVELCOlF9BfnMbRsD8u4QcH2xy4uw67PC8gKBqHgHxEfqmtGw1gIb-c6el56FC3LyPGAw4uDW5mnmGMofy2dhDqS75YeiWTAcYB9P3obLIr5EMImKRlB3Cp1KC2m1a4UW98fzorR1e9lUeffVp577EY42etdQ3giY7DqlYOtmScvCIUj2621mpPBjDaiYZhx2LD8jStPtw2IUxywxkbwaG_yqZvESXGOE1tfFhINA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c507c5c1b.mp4?token=u66D7JdUNRd97NTt1hlxNrXMZ8ciogMlkFTIqekK_7UF7v4qA-ArpbcnFyEW3awgAo_czTtgv9lWgAU7tn4pJ9Ol06TbiXyvhASAPSJsMcGL8RVELCOlF9BfnMbRsD8u4QcH2xy4uw67PC8gKBqHgHxEfqmtGw1gIb-c6el56FC3LyPGAw4uDW5mnmGMofy2dhDqS75YeiWTAcYB9P3obLIr5EMImKRlB3Cp1KC2m1a4UW98fzorR1e9lUeffVp577EY42etdQ3giY7DqlYOtmScvCIUj2621mpPBjDaiYZhx2LD8jStPtw2IUxywxkbwaG_yqZvESXGOE1tfFhINA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز : موفقیت دونالد ترامپ در حمایت از نامزدها در انتخابات مقدماتی، نزدیک به
۱۰۰ درصد
است.
سنا:
۱۰۰٪
مجلس نمایندگان:
۹۸٪
مجموع:
۹۷٪
در سنا، برخی از این رقابت‌ها، انتخابات مقدماتی
سختی علیه نمایندگان مستقر و فعلی
بوده است.
«اگر ترامپ از آنها حمایت کند، آنها پیروز می‌شوند؛ آمار این را نشان می‌دهد.»
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25064" target="_blank">📅 00:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25063">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bb8248d01.mp4?token=I3LwMcBjfmg-am9hj-gvqGmDtg9S6UwHTPvFuzsVYKbScSxD_wzekTsqK1X_722Vkwu81TIMK38CKFc1RHpCxQOO9frSnbW03QFtoA7a-FGjlRbNeswk4GkVf8gVmYoO37z-N6HWtMYngC7Z03W5SNxxQ0DtphFwvpoTS0RJZdt3kv4-z0Rt-SRkyXJAKrM95AFDkVB3h7VbfIL1-KEf141R8XOhGxGhry4dsxmjSvpHM1VusFlKLx262Qq1skeqdgeyGknAt_KQyV0QraLIjyPH-sUm8-woyWjxKQhczfk_UP2SZ-LZ-LrFFHPoVi9zGCaSjVYkT4iG_bccKvDP0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bb8248d01.mp4?token=I3LwMcBjfmg-am9hj-gvqGmDtg9S6UwHTPvFuzsVYKbScSxD_wzekTsqK1X_722Vkwu81TIMK38CKFc1RHpCxQOO9frSnbW03QFtoA7a-FGjlRbNeswk4GkVf8gVmYoO37z-N6HWtMYngC7Z03W5SNxxQ0DtphFwvpoTS0RJZdt3kv4-z0Rt-SRkyXJAKrM95AFDkVB3h7VbfIL1-KEf141R8XOhGxGhry4dsxmjSvpHM1VusFlKLx262Qq1skeqdgeyGknAt_KQyV0QraLIjyPH-sUm8-woyWjxKQhczfk_UP2SZ-LZ-LrFFHPoVi9zGCaSjVYkT4iG_bccKvDP0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: «به لطف مردان و زنان نیروهای مسلح آمریکا، ده‌ها نفر از رهبران تروریست ایران از بین رفته و مستقیم راهی دروازه‌های جهنم شده‌اند.
رهبران آنها دیگر وجود ندارند. بزرگ‌ترین مشکلی که من دارم این است که هیچ‌کس نمی‌داند چه کسی کشور را اداره می‌کند. شاید این چیز خوبی باشد.
خمینی(خامنه ای) را یادتان هست؟ همه آنها از بین رفته‌اند.»
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25063" target="_blank">📅 00:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25062">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f3cfb9ad3.mp4?token=hCmyuwgkxpCXtn07vpDMtZ0LobPqNLLmwR0k82YZkFUWFoFpw3tUY9lRg9qkB-uNBI2nMbppetwilM8NR8LAH-uWHT2F_CxImVtkmS_tz6OaNLbh7PtTFOhS6NL3XqBmq0zG_UJTFfm-gl4kxOKLLLDQj53OHNW_buaCW4GXp9ta_e_NY8fuVORecWe0BIWUviWSPtwFox9-fbGklhfKhV6gpvqJlu80lNCON8W9-CNO6MWoHLlcL7GAkw0JFo7SvRtxDpeJYLtaBWMEn5zQWJMH-s4ZPJy6N9mSoZWWehydAp7fIzAgHZaZrzpMaSIUPtHsUyRtzBNwqbbnGBb8rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f3cfb9ad3.mp4?token=hCmyuwgkxpCXtn07vpDMtZ0LobPqNLLmwR0k82YZkFUWFoFpw3tUY9lRg9qkB-uNBI2nMbppetwilM8NR8LAH-uWHT2F_CxImVtkmS_tz6OaNLbh7PtTFOhS6NL3XqBmq0zG_UJTFfm-gl4kxOKLLLDQj53OHNW_buaCW4GXp9ta_e_NY8fuVORecWe0BIWUviWSPtwFox9-fbGklhfKhV6gpvqJlu80lNCON8W9-CNO6MWoHLlcL7GAkw0JFo7SvRtxDpeJYLtaBWMEn5zQWJMH-s4ZPJy6N9mSoZWWehydAp7fIzAgHZaZrzpMaSIUPtHsUyRtzBNwqbbnGBb8rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«جنگ ایران زمانی تمام شد که بمب‌افکن‌های بی-۲ آمریکا به تأسیسات هسته‌ای ایران حمله کردند؛ چون با آن حمله، برنامه هسته‌ای آنها پایان یافت و این دلیل اصلی انجام این عملیات بود؛ شاید ۹۵ درصد، و شاید هم ۱۰۰ درصد.»
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25062" target="_blank">📅 00:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25061">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a556b7c8f8.mp4?token=IMDk6X0bBpr2TsEvjGO91zRnso9_Cx4C8i7g2bKL-9Ll9fBj35durBGMHe2vuPu1B2i9-Yf42iFZ_9tLlaYqgI0qFF6FhhZ_4Zv0lMAeFOF2tI6Iz3tO4KAwn7MFmjIiOaJJfCTiCiW3j20z3zIawVi4GrXBu7KvRuWXHONJSu1k-UmKnRAAHn9ij4yxbB7Gfn7Ld2Bc4FK75GJDe8kNNN2Hsivwhls80T4WUWZhRPf1fnx3-o0eQrJFKGToPDSyVP8Lq22tt1ViCITlo5fLT6h95j0_hsrfRS-e41NX69d6drh6YDKAdapOkQfMmDeTHWNUSRXhA1zKuRNyFLprDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a556b7c8f8.mp4?token=IMDk6X0bBpr2TsEvjGO91zRnso9_Cx4C8i7g2bKL-9Ll9fBj35durBGMHe2vuPu1B2i9-Yf42iFZ_9tLlaYqgI0qFF6FhhZ_4Zv0lMAeFOF2tI6Iz3tO4KAwn7MFmjIiOaJJfCTiCiW3j20z3zIawVi4GrXBu7KvRuWXHONJSu1k-UmKnRAAHn9ij4yxbB7Gfn7Ld2Bc4FK75GJDe8kNNN2Hsivwhls80T4WUWZhRPf1fnx3-o0eQrJFKGToPDSyVP8Lq22tt1ViCITlo5fLT6h95j0_hsrfRS-e41NX69d6drh6YDKAdapOkQfMmDeTHWNUSRXhA1zKuRNyFLprDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
من مدام از رهبران جهان تلفن‌هایی دریافت می‌کنم که از من [به خاطر جنگ با ایران] بسیار تشکر می‌کنند.
من گفتم: "خیلی خوب. چه زمانی می‌خواهید برای آن هزینه را پرداخت کنید؟"
ما بارِ کل جهان را بر دوش خود حمل می‌کنیم. ما از انجام این کار لذت می‌بریم، زیرا ما قوی‌تر شده‌ایم و دیگران ضعیف‌تر.
آنها فقط ضعیف شده‌اند. آنها ناکارآمد شده‌اند. ما کارهایی را انجام می‌دهیم که هیچ کشور دیگری نمی‌توانست انجام دهد
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25061" target="_blank">📅 00:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25060">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13405144db.mp4?token=QcB60zYPFTjD0pqpRXNWGy3lF0NwI3ceMEuzq_gSAsLwtuoKar-iBuKHexaQVCLH1WIIsUqiPj2kPmvSDU0l6sqAyx-Tu2IIe6uxcHe1zC0zAdlbXqHvNx6oiigrKawh2H1rz3wWmcMTMX4CM7CeHQXeAEC1oCuRwhgZKDKq0IDSK9ayVCyBiQTHqFdCGW_ApWxwaIrgMtlLfI3mx0HgRqjJDQrv9KrlibLnBo8M8hXooJqLuRWRkbRrMA0Ull4UHSRMUTmA06jXlHBFqTarXE1pTheZmZ-mKzY_bBjJyM0nvfRz7Z5DLj73DZhDq5HGDADwEeyNAIELgZxlf_ed4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13405144db.mp4?token=QcB60zYPFTjD0pqpRXNWGy3lF0NwI3ceMEuzq_gSAsLwtuoKar-iBuKHexaQVCLH1WIIsUqiPj2kPmvSDU0l6sqAyx-Tu2IIe6uxcHe1zC0zAdlbXqHvNx6oiigrKawh2H1rz3wWmcMTMX4CM7CeHQXeAEC1oCuRwhgZKDKq0IDSK9ayVCyBiQTHqFdCGW_ApWxwaIrgMtlLfI3mx0HgRqjJDQrv9KrlibLnBo8M8hXooJqLuRWRkbRrMA0Ull4UHSRMUTmA06jXlHBFqTarXE1pTheZmZ-mKzY_bBjJyM0nvfRz7Z5DLj73DZhDq5HGDADwEeyNAIELgZxlf_ed4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : به هگست تبریک میگم بابت کار عالی‌ش ، ونزوئلا رو خیلی سریع یکسره کرد ، و ما فوق خوب عمل کردیم با جمهوری اسلامی ، اونا دیگه ارتشی و چیزی براشون نمونده
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25060" target="_blank">📅 23:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25059">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خواهر امیرحسین مقصودلو(تتلو) خبر از عفو برادرش داد  با شرط لیزر کردن کل تتو های بدنش @WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25059" target="_blank">📅 23:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25058">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd1d989f72.mp4?token=MBK_m-4-epcodiXcypVdRryaM1WYT23JXvEA8O7RZJu5pS54v9GwKoJRn_0300bLsp6SEjAmN2T3PTI4A8hyD3NxByercGrIlNLpNG646eI-swwAShDFb9WaHoFQYC3mPjJDolTDGUs-ZyfhOGXCA20kqZmIbBhClzzJKE2c78OcUz0UslfmiFmjAc7j7kZUz2mZqV_BE30k6kunygnJ1RsFRXEtQOxcp9zvZ4WJ3UQn5O7jzkdzghMyRvQYhSSw8vZbp7k2AhULCNE66dErtixBqPKhq3GiHgcicZLjC1e9fXv4zC1IrD6LUCtzHSw4uLD646ApcV3tU2kNjKacwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd1d989f72.mp4?token=MBK_m-4-epcodiXcypVdRryaM1WYT23JXvEA8O7RZJu5pS54v9GwKoJRn_0300bLsp6SEjAmN2T3PTI4A8hyD3NxByercGrIlNLpNG646eI-swwAShDFb9WaHoFQYC3mPjJDolTDGUs-ZyfhOGXCA20kqZmIbBhClzzJKE2c78OcUz0UslfmiFmjAc7j7kZUz2mZqV_BE30k6kunygnJ1RsFRXEtQOxcp9zvZ4WJ3UQn5O7jzkdzghMyRvQYhSSw8vZbp7k2AhULCNE66dErtixBqPKhq3GiHgcicZLjC1e9fXv4zC1IrD6LUCtzHSw4uLD646ApcV3tU2kNjKacwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ  : لات خاورمیانه دیگه لات‌بازی در نمیاره ، ولی باید کار را تمام کنیم و تنها مسئله این است که تصمیم بگیریم با روش خوب این کار را انجام دهیم یا روش نه‌چندان خوب. به‌زودی متوجه خواهید شد
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25058" target="_blank">📅 23:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25057">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نتانیاهو بار دیگر به شهروندان اسرائیلی هشدار داد: به شما هشدار می‌دهم، آنها قبل از انتخابات به ما حمله خواهند کرد , ما برای این موضوع آماده‌ایم؛ در وهله اول چنین تلاش‌هایی را خنثی خواهیم کرد و در هر صورت، اگر آنها مرتکب این اشتباه شوند، با
قدرتی عظیم
پاسخ خواهیم داد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25057" target="_blank">📅 23:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25056">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ادعای خبرنگار وال‌ استریت‌‌ ژورنال: سرویس مخفی آمریکا CIA یک لیست از ۵ الی ۱٠ نفر مسئولان ایرانی را به اسرائیل داده که این افراد را نباید ترور کرد چون قصد دارند در آینده، حکومت را به دست بگیرند تا ایران کشوری نرمال شود!!️ @WarRoom یاشار: این ادعا فقط در همین…</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25056" target="_blank">📅 23:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25055">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc3582730b.mp4?token=V-i35l2XnxyCgBq3QY2MuvaC9S7bu9Fr2jGi68XTgwXorhQ-ftGv2xZ_t9PNCieHc_MFoEYDBE3gc2OwNqxjd70S84LFX_mKSnKA23TN9KYzte4uf8_wgZ9P6uDNZj1c1Xc2GQ1dbNUCQFg9ltjrtMgp1RtoZcjuxXPHNOa46C2JBPsP2jEOWiAfJKwQclwr7aOfmGOZZIDCt-ruXhvq_4DXfP3PCY1E1ZaSlF-drxCfIRnVC0kwbUXOjNSoWpV8xbJUc4isWEQ6XPTZVD8JaQgqoknAAkdzfSL9EUh6lE-lnqI_DzEQXIMhZQkoLmSZwskOithzeYdER26Fl1Xvig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc3582730b.mp4?token=V-i35l2XnxyCgBq3QY2MuvaC9S7bu9Fr2jGi68XTgwXorhQ-ftGv2xZ_t9PNCieHc_MFoEYDBE3gc2OwNqxjd70S84LFX_mKSnKA23TN9KYzte4uf8_wgZ9P6uDNZj1c1Xc2GQ1dbNUCQFg9ltjrtMgp1RtoZcjuxXPHNOa46C2JBPsP2jEOWiAfJKwQclwr7aOfmGOZZIDCt-ruXhvq_4DXfP3PCY1E1ZaSlF-drxCfIRnVC0kwbUXOjNSoWpV8xbJUc4isWEQ6XPTZVD8JaQgqoknAAkdzfSL9EUh6lE-lnqI_DzEQXIMhZQkoLmSZwskOithzeYdER26Fl1Xvig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواهر امیرحسین مقصودلو(تتلو) خبر از عفو برادرش داد  با شرط لیزر کردن کل تتو های بدنش
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25055" target="_blank">📅 23:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25054">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25054" target="_blank">📅 23:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25053">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">چند پرتاب جدید از سیریک
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25053" target="_blank">📅 23:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25052">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فاکس‌نیوز : شما گفتید ایران یک
تهدید فوری
است، اما اخیراً هم گفتید جنگ با ایران باید تمام شود تا هزینه‌ها کاهش پیدا کند. پیش‌تر نیز گفته بودید: «بیایید این کار را انجام دهیم و درست انجامش دهیم.» بالاخره کدام‌یک درست است؟
مایک راجرز (نامزد جمهوری‌خواه مجلس سنای آمریکا از میشیگان):
همه این موارد درست هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25052" target="_blank">📅 23:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25051">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0986831e52.mp4?token=mC6BluQDgguRzLJkaANJYE3HuURoQIUzIPNx3bZeTwsi37aOpjuMVO-MtmyLZhknp27eB4s_XZU0uYtxDIF97n92dwLSVrtTzQDPrhGc3BtvoZFKPwJF17EKouD0Oq3g4-Qv3VpnlqgyHDxD4Cud0dUCIsQsIzTQMH2fBq1YHCOKaAf7b3RS31dWF72lGfTwc1iOmTXExct211WR3yATjN4N1_t7WguRUC0-gnXrPzFzwdnqom-7PT5oZ5C0SMv6uWL6habAJlSwYOEMXOKor5X2zbDbSer2DS9Mqcnb8OQREYb2-Y52pPuO5_TNkASXeLO01cEmrzcQ-i5j6nAkVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0986831e52.mp4?token=mC6BluQDgguRzLJkaANJYE3HuURoQIUzIPNx3bZeTwsi37aOpjuMVO-MtmyLZhknp27eB4s_XZU0uYtxDIF97n92dwLSVrtTzQDPrhGc3BtvoZFKPwJF17EKouD0Oq3g4-Qv3VpnlqgyHDxD4Cud0dUCIsQsIzTQMH2fBq1YHCOKaAf7b3RS31dWF72lGfTwc1iOmTXExct211WR3yATjN4N1_t7WguRUC0-gnXrPzFzwdnqom-7PT5oZ5C0SMv6uWL6habAJlSwYOEMXOKor5X2zbDbSer2DS9Mqcnb8OQREYb2-Y52pPuO5_TNkASXeLO01cEmrzcQ-i5j6nAkVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
وزیر نفت ایران به‌تازگی استعفا داده است.
او گفته: «ما هیچ اقتصادی نداریم، نفت نداریم، هیچ‌چیز نداریم.»
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25051" target="_blank">📅 22:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25050">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a708cc69cc.mp4?token=gTMKcCiuu6ST0vMx11P8tzA62_o_o0yqxbUag7bh2S319qif4QRDsiBL0fIzgOQa3GN8Sa1GRrCGcHEu4lwA2RNmmG-hdyL50-nS0RmqViaku7dpP8xkkdw3UUxQJKz8jU5JZx2ou3YdT122zuXcFV2YIFw-OP5B54_9GwYS48Fh1im09qbnrgJp3yoOUMlmuSAdsYM3aag55pHRAj_nVLj-dyU3LnpbjhJu-_X5zqqW4wtyuOzDUAi_CaODfFPVJtd0M3fUVAg52KMWeEPtg0wXntRvXkZwPYoZMZXptLy4-CUsKwGFNip_oqBbXoCbr3UY2fyrFJmejUUZ0LMfAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a708cc69cc.mp4?token=gTMKcCiuu6ST0vMx11P8tzA62_o_o0yqxbUag7bh2S319qif4QRDsiBL0fIzgOQa3GN8Sa1GRrCGcHEu4lwA2RNmmG-hdyL50-nS0RmqViaku7dpP8xkkdw3UUxQJKz8jU5JZx2ou3YdT122zuXcFV2YIFw-OP5B54_9GwYS48Fh1im09qbnrgJp3yoOUMlmuSAdsYM3aag55pHRAj_nVLj-dyU3LnpbjhJu-_X5zqqW4wtyuOzDUAi_CaODfFPVJtd0M3fUVAg52KMWeEPtg0wXntRvXkZwPYoZMZXptLy4-CUsKwGFNip_oqBbXoCbr3UY2fyrFJmejUUZ0LMfAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
در همین چند روز گذشته، میلیون‌ها بشکه نفت وارد بازار شده است. اکنون نفت با حجمی در حال عبور و انتقال است که به سطح قبل از جنگ رسیده و گاهی حتی از آن هم بیشتر شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25050" target="_blank">📅 22:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25049">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تنگه صدای زم زمه اسماعیل خطیب میاد
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25049" target="_blank">📅 22:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25048">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULK7NGggNU9WoidK4voLR-G4Y8qomOeu79ebxxoaTHZJxcgp7ITXdBeoTGnFXapbpEih37rrwFr5tX7k_mXT1Ra8Wc5KlDk_icv5cSQYwVfA3pWNILFfN2P7xlvOhdIng2SytWiuIqSZFyURKFtcvpJELJVb2wumpl87VgqctscKyRUY4oTRqf093LGBcDvXEj4_nR9dG8Zs08sowuD_JgePeviYdl5LPEXUfDnDjSIzV9aAy1nDy2NpBqYrO066Gh4L3wryf7D9QMYakG74mn7lB0Q3k9Ma0UR0jQH9QfKeTQwrYozzVp6oNiP9a9IVE6ZzM7vqaOJ0mboUiNnqkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصل خبر فاکس‌نیوز:
دو شناور مهم نظامی آمریکا، از جمله ناو هواپیمابر یواس‌اس جورج اچ. دبلیو. بوش، موقتاً خاورمیانه را ترک کرده‌اند و برای توقف بندری به تایلند رفته‌اند. در حال حاضر یواس‌اس جورج واشنگتن تنها ناو هواپیمابر آمریکایی در خاورمیانه است. با این حال، بوش قرار است طی چند هفته آینده دوباره به خاورمیانه بازگردد. در مجموع حدود ۱۷ شناور نظامی آمریکایی همچنان در منطقه حضور دارند و سه ناوشکن موشک‌انداز نیز در دریای سرخ مستقر هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25048" target="_blank">📅 22:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25047">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : ناو بوش بر میگردد
فاکس نیوز»: ناو هواپیمابر «بوش» خاورمیانه را ترک می‌کند و تنها ناو هواپیمابر «جورج واشینگتن» در منطقه خواهد ماند.
این خبر کانال های زرد فیک نیوز است
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25047" target="_blank">📅 22:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25046">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سیریک صدای انفجاررررر
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25046" target="_blank">📅 22:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25045">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه : جنگنده‌های آمریکایی در چند روز گذشته چندین بار تا نزدیک مرزهای ایران آمدند مانور انجام دادند و برگشتند
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25045" target="_blank">📅 22:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25044">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">چند پرتاب موشک کروز ضد کشتی از قشم به سمت تنگه انجام شده @WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25044" target="_blank">📅 21:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25043">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e04b0950.mp4?token=JzP-YTqxbwQKrlr2YuGWhgAOs8QzFL5H029w1kL2lhWLg1m4FjEW-FGbjKvLWw7-2hqZUU9Dh10wMcNqpcxfTBIu1GLG10i5YUz8P2aohfq3xIACs59wIbJyeE83el6dRdk7NnhZOvZ89gn0oswrTdHgbQJIt7rJpBnaNTnT8AEFdUwEY7ddvmagyGusuLwMLqwYTQ3v3rsJBsyrVjYfVqMYwjyMdmYQuKxYUorQER-PY2IiI7I9jG7oI-3a9gK24uLu-MkOeqVqa0oIcedICzmjXX9LhmSNfUFkTdgcmOx47Q6gkgBr933c7WaDHCKbXg0lnsEC2ARuxZWXSXRfxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e04b0950.mp4?token=JzP-YTqxbwQKrlr2YuGWhgAOs8QzFL5H029w1kL2lhWLg1m4FjEW-FGbjKvLWw7-2hqZUU9Dh10wMcNqpcxfTBIu1GLG10i5YUz8P2aohfq3xIACs59wIbJyeE83el6dRdk7NnhZOvZ89gn0oswrTdHgbQJIt7rJpBnaNTnT8AEFdUwEY7ddvmagyGusuLwMLqwYTQ3v3rsJBsyrVjYfVqMYwjyMdmYQuKxYUorQER-PY2IiI7I9jG7oI-3a9gK24uLu-MkOeqVqa0oIcedICzmjXX9LhmSNfUFkTdgcmOx47Q6gkgBr933c7WaDHCKbXg0lnsEC2ARuxZWXSXRfxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: «کدام قسمت استیک را بیشتر دوست دارید؟»
ترامپ: «راستش من
همه قسمت‌های استیک را دوست دارم
؛ برخلاف تالافریکو در تگزاس (جیمز تالاریکو، نامزد دموکرات مجلس سنا) که وگان است و حالا یک‌دفعه استیک می‌خورد، ولی از آن هم راضی نیست!
این آدم کاهو دوست دارد، نه استیک!
»
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25043" target="_blank">📅 21:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25042">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PU63fqfgpN7AO1Fn68sAAjy4LIL1b0Vf79fXYn_iZuk0tx4tHobhS-rTt6d4YBzSV3wixZFotzAdmDCyPnW36B2HMiJbjwBNeZG4sZMZTzdCh0PjS3hz9z6q3y0UF8RXf5tsJnGH2hWQVw68rzAnRIFnrtmD3Eeq86H5tsAT_1iygteGU9ycix2_jck874qLE46UPMAVOJD_luB7MuzK1s3N216x2zCfwyPNcvPkCm3IRvPSLp-hfqkBaavP7yi-ePZiOBEsMIw6HsKrHAKSzH7NRaASt1EegAkOQRKgJmfXBJ8hcBHdJK_FKDdBRcLcg9w7iJzEzZ8moaoudlRLWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پی۸ پوسایدون و ۵ سوخترسان هم‌اکنون در حال انجام مأموریت در منطقه هستند.تمرکز اکثر آنها بر روی تنگه هرمز میباشد. همچنین ترامپ دیشب گفته بود که موشکهایی که به سمت کشتی ها می‌آید، ما «بینگ بینگ» میزنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25042" target="_blank">📅 21:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25041">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گزارش های بسیار از صدای انفجار در قشم @WarRoom
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25041" target="_blank">📅 21:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25040">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دادستان‌های بریتانیا سه ایرانی را به جاسوسی برای جمهوری اسلامی متهم کردند. مصطفی سپهوند ۴۱ ساله، فرهاد جوادی‌منش ۴۶ ساله و شاپور قلعه‌علی‌خانی نوری ۵۷ ساله متهم‌اند بین اوت ۲۰۲۴ تا مارس ۲۰۲۵ فعالیت‌های روزنامه‌نگاران ایران اینترنشنال را زیر نظر گرفته و برای…</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25040" target="_blank">📅 21:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25039">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گزارش های بسیار از صدای انفجار در قشم
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/25039" target="_blank">📅 21:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25038">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرنگار کانال ۱۲ اسرائیل: نتانیاهو در هفته‌های پایانی انتخابات، به‌جای نظرسنجی کانال ۱۲ که
۵۳ کرسی برای بلوک او و ۵۴ کرسی برای مخالفان
نشان می‌دهد، ظاهراً روی کانال ۱۴ حساب کرده که
۶۳ کرسی برای بلوک نتانیاهو و ۴۵ کرسی برای مخالفان
پیش‌بینی کرده است. او دعوت گادی آیزنکوت برای مناظره را رد کرده و هم‌زمان کارزار علیه
اوفر وینتر، نامزد مستقل راست‌گرا
را تشدید کرده تا آرای راست پراکنده نشود. این رویکرد نشان می‌دهد لیکود تصور می‌کند برای تشکیل دولت به همه کرسی‌های جناح راست نیاز ندارد.
لیکود اکنون سه هفته پایانی را با این باور آغاز کرده که می‌تواند پیروز شود و حتی به اکثریت مطلق برسد
؛ هرچند این ارزیابی با بسیاری از نظرسنجی‌ها تفاوت دارد. نتیجه انتخابات برزیل نیز این اعتماد را تقویت کرده؛ جایی که بولسونارو
۲ تا ۳ درصد بهتر از نظرسنجی‌ها
عمل کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25038" target="_blank">📅 20:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25037">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpIVC18fNBIYN7bGFHpBtC3e3xEntfajShFEuHHDa_XHEoinIHStQhpLb0rlMTa01JO2XnKQMjdYTSS7jv1IOuMkPGrWCmJ3mlyr_cZOWnNA4oi33BjKBRl32AQ2bfT8dTZyF5C0W_ZE4M3KlO6yU6zDDYTrNN_uAgfauGhjfb6Eguq7FWVJn-sypzNAmsUf3_ayMlEVn0wDkCfK2mZnoaOrXj4OYnizqmBULY6CYOsX6NgAJBkNskpgxi1thqZM1yHfF-QlrBGWVbGK4cGGPNb6pA7aeZTqtn9be_riUS1kKh5bGYbs-XzU8Y_ByMcN62Dg4HFbc9DLabhLjiNLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: آلارم جنگی در بالاترین سطح؛ ورود ناو سوم آمریکا و «کد ۱۰۰» سپاه!
حقیقت‌یاب اتاق جنگ
:
پخش
خبر فیک و فوتوشاپ شده ، توسط کانال های زرد از قول سنتکام
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25037" target="_blank">📅 20:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25036">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فاکس نیوز :
شورش‌های گسترده در پاریس
؛ پرچم‌های فلسطین در خیابان‌ها به اهتزاز درآمده و نیروهای پلیس ضدشورش برای کنترل اوضاع با مشکل مواجه‌اند. گاز اشک‌آور نیز به کار گرفته شده است.
جنبش‌های مرتبط با حماس به‌طور فعال در شورش‌ها دخالت دارند
و معترضان در نقاط مختلف تحت تعقیب پلیس هستند.
بازداشت‌ها باید گسترده‌تر
شود «فرانسه در حال سقوط است.»
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/25036" target="_blank">📅 20:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25035">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رایتل ورشکسته شد !
شستا امروز آگهی مزایده
۱۰۰ درصد سهام رایتل
را منتشر کرد؛ قیمت پایه این واگذاری
۱۳۰ هزار میلیارد تومان (۱۳۰ همت)
تعیین شده و فروش به‌صورت
نقدی و یکجا
انجام می‌شود. مزایده قرار است
۲۳ مهر
برگزار شود. رایتل پیش‌تر نیز به‌دلیل مشکلات مالی و کاهش درآمد، اعلام کرده بود که در معرض ورشکستگی قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25035" target="_blank">📅 19:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25034">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMjIOt2fD01tCKevlyrgB5aZs89KEr6k8HwItsqM1yPtKfrVYL5b5lYB_4KQJhEfBk06MQ4w8JavaZ1koQ8qAvncM-3Zbf4e8fK1OiHhyAfwgfbDe8bg-4le4x-in0S0rGTol5P0LN3I_-ES0UOrqEG4E7ZhOsNTDmdYsqo403aKp53_IcD2wiiPmEVi8-bKrS6Xh_x3FfYAKIPqb2yxVa-UUlcq0V6g7I_B8bcDDfIPXoDbaeo-edCSyfQz7o3Rq7YZ_JW8opGGPNRyXxPCa-_wfZR2Jf-O2bXVbGByTRTgfoTyusJjEn_hGpyMtSMRuV5izOsEatsBMDU0AZUShg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث‌ : آنچه در فرانسه در حال رخ دادن است، چیزی کمتر از
مهاجرت گسترده و خارج از کنترل
نیست. این موضوع درباره مدارس نیست؛ موضوع این است که
اسلام می‌خواهد کنترل کشوری را که زمانی بزرگ بود، در دست بگیرد!
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25034" target="_blank">📅 19:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25033">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ادعای مرگ دوم بر اثر طاعون در روسیه
؛ رسانه‌های محلی روسیه مدعی شده‌اند فرد دومی در منطقه ایرکوتسک بر اثر ابتلا به طاعون جان باخته است؛ ادعایی که هنوز از سوی مقام‌های روسیه یا سازمان جهانی بهداشت تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25033" target="_blank">📅 18:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25032">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184e92d2f2.mp4?token=gB5_cZNdVtC1OZ5dqomCx6FBNxoieMKWZuFmb59jGlss3otFWciyFVn-lwaDssvSyb2VH8iDXy1YyTG5RSRtgqyZfrMq1fuT2IUOe1wAmx6YkWsBViiSjw_NYLzj6amLrnnW32VX7a0LKexXywtVSiwThnB7cvmbIJrEPmpMt8NM8oXTWwairKqZySajYMfbwmCIksuVlXILjd8dXUpuuxhs5VeRyatVAz0ClMOo1h_SubQIR_2M-vSRDH2dVnrl3Ueuh3rmwfZf5uFknW5tnFIuAWM28ZOS9qu3HG-EHfPA6vAAreJME4P393C2laXjGTHqzeGI-Y2IDvMk2NhEbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184e92d2f2.mp4?token=gB5_cZNdVtC1OZ5dqomCx6FBNxoieMKWZuFmb59jGlss3otFWciyFVn-lwaDssvSyb2VH8iDXy1YyTG5RSRtgqyZfrMq1fuT2IUOe1wAmx6YkWsBViiSjw_NYLzj6amLrnnW32VX7a0LKexXywtVSiwThnB7cvmbIJrEPmpMt8NM8oXTWwairKqZySajYMfbwmCIksuVlXILjd8dXUpuuxhs5VeRyatVAz0ClMOo1h_SubQIR_2M-vSRDH2dVnrl3Ueuh3rmwfZf5uFknW5tnFIuAWM28ZOS9qu3HG-EHfPA6vAAreJME4P393C2laXjGTHqzeGI-Y2IDvMk2NhEbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امان از دست جاده های باب المندب. هر دو قدم، یه دست انداز گذاشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/25032" target="_blank">📅 18:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25031">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کاتز ، وزیر دفاع اسرائیل : ۴ هزار نفر از تروریست‌های حماس که ۷ اکتبر وارد اسرائیل شدن، کشته شدن و ۲ هزار نفر دیگه باقی موندن.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25031" target="_blank">📅 18:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25030">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کانال ۱۴ اسرائیل: نیروهای امنیتی جمهوری اسلامی طی دو هفته گذشته به دست‌کم
پنج خانواده از معترضان کشته‌شده در اعتراضات ژانویه ۲۰۲۶
یورش برده‌اند. مأموران با ورود به خانه‌ها، وسایل شخصی قربانیان از جمله لباس، دفتر خاطرات، کتاب و حتی عروسک‌های دوران کودکی را ضبط کرده‌اند. به گفته خانواده‌ها، نیروهای امنیتی همچنین آنها را تهدید کرده‌اند که در صورت انتشار عکس یا ویدئو از فرزندانشان در شبکه‌های اجتماعی، وسایل بیشتری از اتاق‌های آنها برده خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25030" target="_blank">📅 18:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25029">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مدیرعامل آرامکو : حتی اگر بحران جنگ علیه ایران همین الان پایان یابد، امکان دارد جهان برای پر کردن دوباره ذخایر نفتی که در طول جنگ مصرف شده‌اند، تا ۲ سال به حدود ۲ میلیون بشکه نفت بیشتر در روز نیاز داشته باشد
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25029" target="_blank">📅 18:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25028">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏
کشتی حامل گاز طبیعی مایع "ال مافیار" متعلق به قطر، از طریق مسیر ایران وارد تنگه هرمز شد و در راه پاکستان قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25028" target="_blank">📅 17:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25027">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مهم‌ترین رویدادهای پیش‌روی بیت‌کوین به وقت و تاریخ ایران در‌ این ماه میلادی : ۱۵ مهر، ساعت ۲۱:۳۰ — صورت‌جلسه فدرال رزرو؛
۲۲ مهر، ساعت ۱۶:۰۰ — تورم آمریکا (CPI)
؛
۶ آبان، ساعت ۲۱:۳۰ — تصمیم نرخ بهره فدرال رزرو
؛ ۶ آبان، ساعت ۲۲:۰۰ — سخنرانی جروم پاول؛ ۸ آبان، ساعت ۱۶:۰۰ — شاخص تورمی PCE آمریکا.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25027" target="_blank">📅 17:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25026">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کوین‌دسک: بیت‌کوین امروز چند بار به محدوده
۸۷ هزار دلار
نزدیک شد اما برای سومین بار از ۲۳ سپتامبر در عبور پایدار از این سطح ناکام ماند و دوباره تا حوالی ۸۵۶۰۰ دلار عقب نشست. اتریوم نیز حوالی ۲۷۰۰ دلار معامله می‌شود. همزمان شاخص‌های سهام آمریکا در نزدیکی رکوردهای تاریخی قرار دارند و بازار کریپتو همچنان تحت تأثیر شرایط نقدینگی و نرخ بهره قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25026" target="_blank">📅 17:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25025">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7d0da0527.mp4?token=jpMR2e-N1gcsLa-vAhvu0LBIEP2dodKigjIf-9SK67HtzWWjtrff2hDgGpSe8LY9ZEgIO0U75_LmFiRdE595_oBnNbV6Mwd-rXK6IZ2BuA2K20a0B5-j0sLptJ6SV3lItozjv44FjFaAM4PL1jlWIQOTcW2ivxkXtRmn1XoaZBZ2LyNVU_oEF5yTk5m1w9uIFrtT3iRaMxOvR3Dyt83SykF4mFu4GTJYjd5rr_nMw4029_XRno5F4UMPK8tYM8LMr49Zd_jYLp2MkAEcNFMMP57Lg5ob22pXl62ZIjmdAliHRQAAa4-vLQTRf0mFEOoqjPgze_mn2rCCYFG9xSQs6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7d0da0527.mp4?token=jpMR2e-N1gcsLa-vAhvu0LBIEP2dodKigjIf-9SK67HtzWWjtrff2hDgGpSe8LY9ZEgIO0U75_LmFiRdE595_oBnNbV6Mwd-rXK6IZ2BuA2K20a0B5-j0sLptJ6SV3lItozjv44FjFaAM4PL1jlWIQOTcW2ivxkXtRmn1XoaZBZ2LyNVU_oEF5yTk5m1w9uIFrtT3iRaMxOvR3Dyt83SykF4mFu4GTJYjd5rr_nMw4029_XRno5F4UMPK8tYM8LMr49Zd_jYLp2MkAEcNFMMP57Lg5ob22pXl62ZIjmdAliHRQAAa4-vLQTRf0mFEOoqjPgze_mn2rCCYFG9xSQs6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو از روسیه خواست اطلاعات بیشتری درباره مرگ کارمند مؤسسه تحقیقات ضدطاعون در سیبری منتشر کند.
روبیو گفت آمریکا این موضوع را «ساعت‌به‌ساعت» زیر نظر دارد و در صورت جدی‌تر شدن وضعیت، واشنگتن اقداماتی برای کمک به روسیه در اختیار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25025" target="_blank">📅 17:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25023">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رویترز:
دست‌کم دو فلسطینی در حملات اسرائیل به غزه کشته شدند.
به گفته مقام‌های پزشکی، یکی در نزدیکی بیمارستان شفا در شهر غزه و دیگری در حمله‌ای جداگانه در همان منطقه کشته شده است. ارتش اسرائیل گفت این دو حمله، نیروهای مسلح تروریست را هدف قرار داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25023" target="_blank">📅 17:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25022">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رویترز:
صادرات نفت کشورهای خلیج فارس، بدون احتساب ایران، در سپتامبر به بیش از ۸۱ درصد سطح پیش از جنگ رسید.
صادرات نفت خام و میعانات به حدود ۹۱ درصد سطح قبل از جنگ برگشته، اما صادرات فرآورده‌هایی مانند گازوئیل و سوخت جت تنها حدود ۶۰ درصد سطح پیش از جنگ است. صادرات نفت ایران نیز به دلیل محاصره آمریکا تقریباً به صفر رسیده است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25022" target="_blank">📅 17:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25021">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SX-7C4-JiBT9sDYCvXyn6KsGcNdC_qgQv5-37f8FwSfFR2k5EzS3gZ053bMe-WKGDt4ykscabJmfzyiUxuEvlYEPKuLrQL4-ukKIGAWsGh1R_7F6qKazLvHZdwfCyFy5d59rhfaMbby5TrXOYJv_cx4rLbP-g4vY7rXkPf_OyXgLaug07RKx2A97OFlb0nQtsm1KKH-73yOmC9rZeswW_zDP5-ztHiwPk0XP8_9Gw99IKMWYbZxwK3L7wI_X5A7go-66TsUtP50wvH4Rc9HR6TnQET6_vA8CmX-q6RLDKApREjozgrfbhOL118YX2RjzBbamJ0ptqKV9IGpEpdo75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارت ایران روز فلج مغزی رو به ترامپ تبریک گفت
@WarRoom
البته باید به موشتبی این رو تبریک میگفت</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25021" target="_blank">📅 16:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25020">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سفارت بریتانیا در ریاض برای شهروندان خود هشدار امنیتی داد
سفارت بریتانیا در عربستان سعودی با صدور اطلاعیه‌ای از اتباع خود در این کشور خواست با توجه به شرایط فعلی، ضمن حفظ هوشیاری کامل، پروتکل‌های ایمنی را رعایت کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25020" target="_blank">📅 16:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25019">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پلیس بریتانیا یک مظنون دیگر را در پرونده پایگاه هوایی فیرفورد بازداشت کرد.
پلیس ضدتروریسم بریتانیا اعلام کرد یک
مرد ۲۲ ساله بریتانیایی
در وست‌مینستر لندن به ظن
آماده‌سازی برای انجام اقدامات تروریستی
در ارتباط با پرونده مرتبط با پایگاه هوایی
RAF Fairford
بازداشت شده است. در جریان این عملیات، یک ملک در وست‌مینستر نیز مورد بازرسی قرار گرفت. این فرد
هفتمین بازداشت
در این پرونده محسوب می‌شود؛ تحقیقات درباره طرح احتمالی مرتبط با پایگاه فیرفورد همچنان ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25019" target="_blank">📅 16:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25018">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlvRDhrc1gbhKReCaQb2qVLcI6HAXV4L-fKFW3P3BoZQiJxiEnfxzcyTpTZM9kxbGgTCgHk-w9ZeuIv4nStTdwLVnElYBw6pv_TQ8kw7WlbvXhicwwooR89oqiG0nml3M6zZgoPu1LgEmXldNHFKXetFS7230C0eSvyrv-XT4gZyXB8QKK1hswLftimMXWMabE8YN0la_KJyn3Hzm3t6-G8jAumRDsR9AvaNh2s_TChWEnBrOyF-8U-MJydqeeG0oMxhc4W7UP4m2bAqKndh6xNbpInkE3QZblrkQkqyyGmaGHLdq3aO18UjPS8xFdF9U8cyXUUpmavDDLopa6cGGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت یاب
سنتکام گزارش سقوط بالگرد آمریکایی در دریای سرخ را تکذیب کرد.
فرماندهی مرکزی آمریکا اعلام کرد گزارش‌های منتشرشده در
رسانه‌های دولتی ایران
درباره سقوط یک بالگرد
MH-60R نیروی دریایی آمریکا
پس از اعلام وضعیت اضطراری، صحت ندارد و
تمام هواگردها و نیروهای نظامی آمریکا در سراسر خاورمیانه سالم و در دسترس هستند.
این تکذیب پس از آن منتشر شد که بالگردی با همین مدل، دوشنبه شب هنگام پرواز در نزدیکی
ینبع عربستان
وضعیت اضطراری اعلام کرد و سپس از سامانه‌های ردیابی عمومی ناپدید شد. دلیل وضعیت اضطراری همچنان اعلام نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25018" target="_blank">📅 16:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25017">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دادستان‌های بریتانیا سه ایرانی را به جاسوسی برای جمهوری اسلامی متهم کردند.
مصطفی سپهوند ۴۱ ساله، فرهاد جوادی‌منش ۴۶ ساله و شاپور قلعه‌علی‌خانی نوری ۵۷ ساله
متهم‌اند بین
اوت ۲۰۲۴ تا مارس ۲۰۲۵
فعالیت‌های روزنامه‌نگاران ایران اینترنشنال را زیر نظر گرفته و برای
تدارک حمله خشونت‌آمیز
علیه دست‌کم دو روزنامه‌نگار، از آنها عکس و فیلم تهیه کرده‌اند. دادستان پرونده گفت هدف،
تلافی انتقاد از جمهوری اسلامی و ایجاد ارعاب
بوده است. هر سه نفر اتهامات را رد کرده‌اند؛ سپهوند مدعی است تحت فشار و تهدید عمل کرده و دو متهم دیگر می‌گویند از ارتباط اقداماتشان با سرویس اطلاعاتی ایران بی‌خبر بوده‌اند. دادگاه در
وولویچ کراون لندن
برگزار شده و رسیدگی به پرونده حدود
شش هفته
ادامه خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25017" target="_blank">📅 16:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25016">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L85P6BKXPzN9u9CNsdDC92a7YM4Wtzz6igbBJQFZv8ViFL8NN5jruryIeCXmc1BwposdOJeFMAZRi6Es82O_jnJe5ewvh7tugNHba0djfp3wk4zCj10kZ_-weTC8C1q5ygaI3hYYRuYkPF8RxrHAUGMJl_4dVnvKzDqG0LthwCGpAB4hoVz6cRCUQeGMP72EGld_qJh_cHjXSgrxscGD6nJhXc0vHhJQLdO6P-PN1RbrE-3PURjs04cY_oZkJqMNO3dmZhduiV4psetEr0uUb7n-DtkGVGQevfEB81rHvqp4StHjU3z4lc2rHwbBjIH-lCDwntzwystTVsv7VHEjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب یک دستگاه آبگرمکن گازوئیلی از بهبهان خوزستان
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25016" target="_blank">📅 15:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25015">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28d6cd9fcc.mp4?token=hdISkvT2cpJYQ_x9cCHcKbTDDTrdn7VrgXQzsvHpn0iru-bY4QxqTUCRjC5CUNfa54Tbx6y1GM35xNnax-jN-VR9-8mG16Kgs4QlZ4xsw7fK2nlUPO4bxpD5x2Hq1iKAerw814Tj7h2KGkL29uOIZIPCFOCQJ7HB3FX7Xv-KAXzG2fV_t0eVOQ5HVt5u55PqM4XauUAZ8CRJRiUwjJngpHuSJ0dc2-5NY2T3LYg_A09qX2iFXfmjHDoZ1YXkFjIDTzOlO73pQyELM2TYgZIPOg0RS88Uu-ncc_rEOAMuQkUj-qh3qyBuhKbIYO9XiQOqrN9I2PP5f160Y5zzuleg1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28d6cd9fcc.mp4?token=hdISkvT2cpJYQ_x9cCHcKbTDDTrdn7VrgXQzsvHpn0iru-bY4QxqTUCRjC5CUNfa54Tbx6y1GM35xNnax-jN-VR9-8mG16Kgs4QlZ4xsw7fK2nlUPO4bxpD5x2Hq1iKAerw814Tj7h2KGkL29uOIZIPCFOCQJ7HB3FX7Xv-KAXzG2fV_t0eVOQ5HVt5u55PqM4XauUAZ8CRJRiUwjJngpHuSJ0dc2-5NY2T3LYg_A09qX2iFXfmjHDoZ1YXkFjIDTzOlO73pQyELM2TYgZIPOg0RS88Uu-ncc_rEOAMuQkUj-qh3qyBuhKbIYO9XiQOqrN9I2PP5f160Y5zzuleg1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از ۱۰۰ موتورسوار که از حضور مسلملنان و صدای مسجد در منطقه کلافه شده بودند در روبروی مسجد آنها و در حال عبادتشان گرد هم آمدند تا موسیقی گروه «ای‌سی/دی‌سی» را با صدای بلند برای آن‌ها پخش کنند!
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/25015" target="_blank">📅 15:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25014">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سخنگوی وزارت امور خارجه قطر : تماس ها و بازدیدها در تلاش برای پیشرفت در مذاکرات بین واشنگتن و تهران ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25014" target="_blank">📅 15:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25013">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رویترز:
پالایشگاه‌های نفت چین، حجم خرید خود از نفت خام عراق را افزایش داده‌اند تا کمبود عرضه نفت ایران از طریق تنگه هرمز را جبران کنند. بر این اساس، حداقل ۱۲ میلیون بشکه نفت خام عراق و قطر خریداری شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/25013" target="_blank">📅 15:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25012">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b6a1530a7.mp4?token=cZ7bTICHGAjDI5clJwWUS2BsejWr3EJortKY5-nah9YdahUofY43-OHkUJ89apI_sUp40UDSFXzED_ivKsw9a5ghJQHcf8Dr3HSi9MqSpVj5Jbqdw6N7MPUUEjfREZMNGWWGwqnpLdDs23bZk31qjvqgGu6K53pXPXU7kWx5pbev7RrLDqJadbkjzQP6u3mp2JXYP7E6ALECFpCw7yC44Nj1a9kUp5h9yJi-3VDJcgULDQD6wm4GK1TkVNnTN6pf-0WYYYGKszmoUiZgdH3GNFjOGwVK6SaXWqJbb9nxWhtK6wlDfwNWle8wGk4uSOC2AYGY1Awz6ayxxB_W2uw3Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b6a1530a7.mp4?token=cZ7bTICHGAjDI5clJwWUS2BsejWr3EJortKY5-nah9YdahUofY43-OHkUJ89apI_sUp40UDSFXzED_ivKsw9a5ghJQHcf8Dr3HSi9MqSpVj5Jbqdw6N7MPUUEjfREZMNGWWGwqnpLdDs23bZk31qjvqgGu6K53pXPXU7kWx5pbev7RrLDqJadbkjzQP6u3mp2JXYP7E6ALECFpCw7yC44Nj1a9kUp5h9yJi-3VDJcgULDQD6wm4GK1TkVNnTN6pf-0WYYYGKszmoUiZgdH3GNFjOGwVK6SaXWqJbb9nxWhtK6wlDfwNWle8wGk4uSOC2AYGY1Awz6ayxxB_W2uw3Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای خبرنگار وال‌ استریت‌‌ ژورنال: سرویس مخفی آمریکا CIA یک لیست از ۵ الی ۱٠ نفر مسئولان ایرانی را به اسرائیل داده که این افراد را نباید ترور کرد چون قصد دارند در آینده، حکومت را به دست بگیرند تا ایران کشوری نرمال شود!!️
@WarRoom
یاشار: این ادعا فقط در همین ویدیو بیان شده و در وال استریت ژورنال یا رسانه دیگری منتشر نشده است</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/25012" target="_blank">📅 14:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25011">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">منابع هندی اعلام کردند یک
کشتی تجاری با پرچم پاناما
امروز،
۶ اکتبر, ۱۴ مهر
هنگام عبور از نزدیکی تنگه هرمز و سواحل عمان هدف یک
پرتابه ناشناس
قرار گرفته و
۱۱ خدمه هندی زخمی شده‌اند
. تاکنون هویت عامل حمله به‌طور رسمی اعلام نشده ولی این حمله به سپاه نسبت داده میشود.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25011" target="_blank">📅 14:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25010">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">عملیات کاگ‌ب برای ایجاد اختلاف میان شاه و آمریکا:
بر اساس اسناد
آرشیو میتروخین
و
اسناد رسمی وزارت خارجه آمریکا (FRUS)
، بخش «سرویس A» کاگ‌ب که مسئول عملیات فریب و اطلاعات نادرست بود،
نامه‌ای جعلی به نام جان فاستر دالس، وزیر خارجه آمریکا، خطاب به سفیر آمریکا در تهران جعل کرد
؛ نامه به‌گونه‌ای تنظیم شده بود که توانایی شاه را تحقیرآمیز جلوه دهد و این تصور را ایجاد کند که
آمریکا در حال بررسی کنار گذاشتن یا سرنگونی شاه است
. کاگ‌ب نامه را مستقیماً به شاه نداد؛ مأموران شوروی
نسخه‌هایی از آن را میان نمایندگان بانفوذ مجلس و سردبیران مطبوعات ایران پخش کردند
تا نامه از طریق محافل سیاسی به شاه برسد؛ طبق پرونده کاگ‌ب، این نقشه موفق شد و
شاه نامه را واقعی تصور کرد و دستور داد نسخه‌ای از آن برای سفارت آمریکا ارسال و درباره آن توضیح خواسته شود
. سفارت آمریکا اعلام کرد نامه جعلی است، اما طبق گزارش کاگ‌ب،
تکذیب آمریکا نیز در میان برخی محافل ایرانی و حتی شاه باور نشد
و محتوای تحقیرآمیز منتسب به دالس به موضوع گفت‌وگوهای پنهانی در میان نخبگان ایران تبدیل شد.
هدف اصلی عملیات، ضربه زدن به اعتماد شاه به آمریکا و تشدید شکاف میان تهران و واشنگتن بود.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25010" target="_blank">📅 14:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25009">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تلاش شنیده نشده نافرجام کاگ‌ب برای ترور شاه در تهران:
بر اساس اطلاعات
آرشیو میتروخین
، یک مأمور مخفی کاگ‌ب یک
فولکس‌واگن بیتل مملو از مواد منفجره
را در مسیر حرکت محمدرضا شاه به سمت
مجلس شورای ملی
پارک کرد. طبق روایت منتشرشده، این عملیات به دستور کاگ‌ب و با تأیید
نیکیتا خروشچف
انجام شده بود. هنگامی که کاروان شاه از کنار خودرو عبور کرد، مأمور کاگ‌ب با
کنترل از راه دور
اقدام به انفجار بمب کرد، اما
چاشنی عمل نکرد و انفجار رخ نداد
؛ در نتیجه شاه از این سوءقصد جان سالم به در برد. این گزارش در کتاب
«آرشیو میتروخین ۲: کاگ‌ب و جهان»
نوشته کریستوفر اندرو و واسیلی میتروخین آمده است. آرشیو میتروخین شامل یادداشت‌ها و رونوشت‌هایی است که یک آرشیویست ارشد کاگ‌ب از پرونده‌های محرمانه این سازمان تهیه کرده بود و اکنون در
مرکز آرشیو چرچیل دانشگاه کمبریج
نگهداری می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25009" target="_blank">📅 14:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25008">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اتاق جنگ با یاشار | حقیقت‌یاب: ماجرای موسوم به «طاعون روسی» پس از مرگ یک پژوهشگر ۲۸ ساله در مؤسسه تحقیقات ضدطاعون در ایرکوتسک روسیه مطرح شد؛ اما آزمایش‌های رسمی تاکنون ابتلای او به طاعون را تأیید نکرده‌اند و علت مرگ، ذات‌الریه با منشأ نامشخص اعلام شده است.…</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25008" target="_blank">📅 13:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25007">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhTkss1E9H2cG6ntmZD7V_qTqVk8fme6Twb0HWIetLVTQO8S6H3QVq3nbX64hGbBwqVWciAJ6lqYQwLHufZsaRjYxqka_k7orQSi0GCZSRiC82rQP9YnwXVtAdRUcYtKifucT9qw0N7XTjM3oyExRPngFHuyfBw2lzWed4f6KRk3LI-DOCt41aTfL5XFTWIvrA_I-Rr3I_zQ3cnsl1YOekPazQX0mwtgTwjK-8z_DF43Bxj_RFYYFHdSyysoEa9x3rXGxmFZQu0L2KspCaMRNV1dqooXRRaS3ULSGVdEKb0nuVZ1oY5FUqIwWE4qz3D_SoG4bHgMZpmooEXKMdoANg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران اعلام کرد در واکنش به اقدامات آمریکا علیه نفتکش‌ها و شناورهای ایرانی، نیروی هوافضای سپاه با موشک‌های بالستیک به دو ناوشکن آمریکایی  DDG119 - USS Delbert D. Black و  DDG53 - USS John Paul Jones  حمله کرده است. سپاه مدعی شده این دو ناوشکن که به…</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25007" target="_blank">📅 13:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25006">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/230bdf5772.mp4?token=aWeZoUBFsWVmsxFizrW39O3XqPIV5zoE5ThTh-umAJa29X_AP7X_cMA72NCWlUBkvUMLdgIDbGMU3yPchDD3ia9wcULeTlIvEoyKTkO2MY_wp1ZzbJcVRyT0cqp144sooNgNxaK9sZ8MW9Pt0jne6I2xMg9pIxemDqvGdE3urhoCeonCxxsQxYP0OnGHPrh22jzNj1BtVMUuVCp5H0oVnMyiO7cpRhcDmmVudIbQPtU5nDUwZhZgvis0GolV-hsvQ0HnLQMGTmzsgW2OQTs__SSW9ACXaU0VKnmtO9p90BSOZBSJu8ZdAUuWDxcDevjUTMzNrdSJMsNRv8oXQMG8QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/230bdf5772.mp4?token=aWeZoUBFsWVmsxFizrW39O3XqPIV5zoE5ThTh-umAJa29X_AP7X_cMA72NCWlUBkvUMLdgIDbGMU3yPchDD3ia9wcULeTlIvEoyKTkO2MY_wp1ZzbJcVRyT0cqp144sooNgNxaK9sZ8MW9Pt0jne6I2xMg9pIxemDqvGdE3urhoCeonCxxsQxYP0OnGHPrh22jzNj1BtVMUuVCp5H0oVnMyiO7cpRhcDmmVudIbQPtU5nDUwZhZgvis0GolV-hsvQ0HnLQMGTmzsgW2OQTs__SSW9ACXaU0VKnmtO9p90BSOZBSJu8ZdAUuWDxcDevjUTMzNrdSJMsNRv8oXQMG8QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو: «معجزه‌ای که امروز جهان شاهد آن است این است که حتی بعضی از کسانی که ما را محکوم می‌کنند، در دل خود می‌گویند: «وای، ادامه بدهید، ادامه بدهید!» چون خودشان چنین قدرتی ندارند.»
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25006" target="_blank">📅 12:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25005">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d6a47346f.mp4?token=c9Aq1liqKD_cy4bRK5s-fjVEzkfAmjDCCE5Zdv3Wq2NzY3-eZe4lL951mfzBJmwRJCIdCe0yMu6uMALQPlNMYbBp7RQ-x_r-s61hYJ4L0SfjZBmvlV6jAuqt_ZM6IpzGgO4XnrY1grqJvqNZ8pJqXlfXaNcLJGvSqLzasXoptOlOh-WBCLFLfFMQRUQEZ02Ws9WGBiqQHj3a7GF1GWK4RPUwIQTlV4I6Kz-RcVpa6viqs4q1FYFXh67ZnDV3zbl8O3wXz2Uzzwa55mFbvkswBq22BWdaKQtn6StAJeCfF2eme4j8u2Q93keDOz4jk9TLDH-ME_8NehlgUnnUKed8vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d6a47346f.mp4?token=c9Aq1liqKD_cy4bRK5s-fjVEzkfAmjDCCE5Zdv3Wq2NzY3-eZe4lL951mfzBJmwRJCIdCe0yMu6uMALQPlNMYbBp7RQ-x_r-s61hYJ4L0SfjZBmvlV6jAuqt_ZM6IpzGgO4XnrY1grqJvqNZ8pJqXlfXaNcLJGvSqLzasXoptOlOh-WBCLFLfFMQRUQEZ02Ws9WGBiqQHj3a7GF1GWK4RPUwIQTlV4I6Kz-RcVpa6viqs4q1FYFXh67ZnDV3zbl8O3wXz2Uzzwa55mFbvkswBq22BWdaKQtn6StAJeCfF2eme4j8u2Q93keDOz4jk9TLDH-ME_8NehlgUnnUKed8vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو: «در دنیای غرب امروز، در جوامع دموکراتیک، آنها هم انتخاب دیگری ندارند؛ اما نمی‌جنگند. ما هم انتخاب دیگری نداریم، اما
می‌جنگیم
.»
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25005" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25004">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نتانیاهو در اکس: «ما ایران را عقب راندیم؛ مأموریت را هم به پایان خواهیم رساند.»
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/25004" target="_blank">📅 12:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25003">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">استیضاح عراقچی در سامانه مجلس ثبت شد
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25003" target="_blank">📅 12:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25002">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزیر کشور رژیم جمهوری اسلامی , اسکندر مؤمنی برای شرکت در مذاکراتی وارد دوحه قطر شد هم زمان ۶ سوخترسان و جنگنده های آمریکای با تمرکز بر تنگه هرمز در حال اسکورت کشتی ها از مسیر جنوبی تنگه هستند @WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/25002" target="_blank">📅 12:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25001">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شبکه ۱۲ اسرائیل : همام الهمامی، کمک‌خلبان عمانی در بازجویی جدید گفته است او قصد داشت هواپیما را طبق روال عادی برای فرود هدایت کند و در ثانیه‌های پایانی، زمانی که دیگر امکان رهگیری وجود نداشته باشد، هواپیما را به ساختمان ترمینال فرودگاه بنگوریون بکوبد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25001" target="_blank">📅 11:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25000">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8573ef2225.mp4?token=bsNa-T6pdobIE7pUwYHrzLdmJv_ftBw0OLcb-XyvQjSEomaV5sjOulV80Ab_wyxbaQvIxW9AduybMmeSSUwlhGlR-hU6zeyLzh3jql7jT7xvKkvyTBEn7e39QDkl2lrQVWEle2N14R7FwSauQp8dIm5DKb0X-qgjRMYCl5GMbSD5uceBB960uWgGIiU8rRa7cEZ3g-PRiqYyqyd_C1x6fw2ky_3ufVatx5gB5zwg8F7s8h7VeEaaLqxDznw3BWIFJ8Xk0WGaJOtnY6gzVMa72i35liEBXrZn8TSxWGq4V6NQZNbbUbZuNAg5cXgmEe2GJXoQOTXM17ENTUtrWeBXGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8573ef2225.mp4?token=bsNa-T6pdobIE7pUwYHrzLdmJv_ftBw0OLcb-XyvQjSEomaV5sjOulV80Ab_wyxbaQvIxW9AduybMmeSSUwlhGlR-hU6zeyLzh3jql7jT7xvKkvyTBEn7e39QDkl2lrQVWEle2N14R7FwSauQp8dIm5DKb0X-qgjRMYCl5GMbSD5uceBB960uWgGIiU8rRa7cEZ3g-PRiqYyqyd_C1x6fw2ky_3ufVatx5gB5zwg8F7s8h7VeEaaLqxDznw3BWIFJ8Xk0WGaJOtnY6gzVMa72i35liEBXrZn8TSxWGq4V6NQZNbbUbZuNAg5cXgmEe2GJXoQOTXM17ENTUtrWeBXGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏سخنگوی ارتش اسرائیل: یک تونل به طول یک‌ونیم کیلومتر را در شمال نوار غزه منهدم کردیم. عملیات برای نابودی زیرساخت‌های زیرزمینی در این منطقه ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/25000" target="_blank">📅 11:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24999">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏اداره فدرال حفاظت از قانون اساسی آلمان : تلاش جمهوری اسلامی برای دستیابی به فناوری آلمانی مورد استفاده در ساخت موشک و سامانه‌های پرتاب افزایش یافته است. حکومت ایران برای بازسازی زرادخانه و تاسیسات آسیب‌دیده خود به دنبال فناوری‌های غربی است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24999" target="_blank">📅 11:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24998">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzPhXBBeqyODEN5W8dlHK7YNdMuozRfPpxFuvtZgFdt-9hZLGLRS_qofU-vJUusU2LV5QdOWHV6MBKmAycAJb7D3JUS5r-KJXzGAf7A8Hhw9BCuuPRXcNQrmRNMitQz8Cqjzgh_LpJ4xZXupBicRul76Ae1bVJQe-33Fvr94pXJgbf6q-Hk3e5rZ01VFVW4wnbl8I382-NbQsyEIz1eQ-QTEPS1ywY7haymaTqe3qRXlmwGVlrLMPSfUtUYWnJOXDMpThDxmoh3jZr9oLs-dZQkDgY6kCUTL2CpDUrqHZkV9FbsAkjd-QqWjVnoL0y8hZ4kdtXfrc-4xKJPM9_5Axw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت آموزش و پرورش ترکیه تو جلد کتاب درسی جدید خودش، تمام مناطق شمالی و شمال‌غربی ایران رو، جزو نقشه‌ی "دنیای ترک" قرار داده.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24998" target="_blank">📅 11:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24997">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بلومبرگ: دست‌کم
۵۰ نفتکش حامل نفت ایران
همچنان در نزدیکی سواحل ایران متوقف مانده‌اند و تعدادی نفتکش خالی نیز در نقاط مختلف اقیانوس هند و اطراف سریلانکا منتظر هستند و به سمت بنادر ایران حرکت نمی‌کنند. دست‌کم ۱۱ نفتکش حامل محموله در شرق جزیره خارک لنگر انداخته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24997" target="_blank">📅 11:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24996">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24996" target="_blank">📅 05:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24995">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24995" target="_blank">📅 05:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24994">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3258eb63.mp4?token=rEsQcknV2u-6UOToqNCKUWdPayi697b2zynHyjbI6Ta0blblRmguLP7RCwUSwtZuDuk0lptss3qLz_9mlE04rO6kIk6ACIjw8XdMky1Y2zk8gib-_ZQgmvhQLnZqaeRLY2eQVMDdMdKwdHYvOXeUb7r6r-XCzhkH8k2KQ2epW9prBCbklVvuzJjIYBSUqx2g69n88Sn48Hiw4ttPCmJGDMn6uwewV-MR66sLtdV04tLuR7xq5Q7NF4wAo1W7bPWylY0asj_hb-V4OycCMuNWdb7Um-DrOB45EZbTFhYHhw9JgnlY16oq_qRaOAwTUsfLUfFzMtL_5jIprpj_LXx3gGLML0V8cfO86auqGoREjJFl9rf3BWGyaU9rV-BFlm9rl2fOT6ngKDrC2h2Ql9DuiAeSreHSfYc1295gbEh3MVAXtgybx8Kfa6l6_MH8rp3uNGq0xFR82mDE0HJzEEsfMhBGPwPeiUpEgxoZlkgOpnfUyyniD74Sx38a0wuRu6mYz4j49Ik3y1TUcSr6XTv5OadVaPt063lxAu_5qfkmr19vPV_NV6fTFP2xCQkKjF78c_79FnkPzzpRaC9RweRXaMEzOdWwzstCsQGZ_GH4UAfh3g2-iJ5rvijynoERZ8BojQm8tpx7IEv94OS-xcrGaLjXm98g5dGy1t4l09LuH_8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3258eb63.mp4?token=rEsQcknV2u-6UOToqNCKUWdPayi697b2zynHyjbI6Ta0blblRmguLP7RCwUSwtZuDuk0lptss3qLz_9mlE04rO6kIk6ACIjw8XdMky1Y2zk8gib-_ZQgmvhQLnZqaeRLY2eQVMDdMdKwdHYvOXeUb7r6r-XCzhkH8k2KQ2epW9prBCbklVvuzJjIYBSUqx2g69n88Sn48Hiw4ttPCmJGDMn6uwewV-MR66sLtdV04tLuR7xq5Q7NF4wAo1W7bPWylY0asj_hb-V4OycCMuNWdb7Um-DrOB45EZbTFhYHhw9JgnlY16oq_qRaOAwTUsfLUfFzMtL_5jIprpj_LXx3gGLML0V8cfO86auqGoREjJFl9rf3BWGyaU9rV-BFlm9rl2fOT6ngKDrC2h2Ql9DuiAeSreHSfYc1295gbEh3MVAXtgybx8Kfa6l6_MH8rp3uNGq0xFR82mDE0HJzEEsfMhBGPwPeiUpEgxoZlkgOpnfUyyniD74Sx38a0wuRu6mYz4j49Ik3y1TUcSr6XTv5OadVaPt063lxAu_5qfkmr19vPV_NV6fTFP2xCQkKjF78c_79FnkPzzpRaC9RweRXaMEzOdWwzstCsQGZ_GH4UAfh3g2-iJ5rvijynoERZ8BojQm8tpx7IEv94OS-xcrGaLjXm98g5dGy1t4l09LuH_8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رقص و قر تمام کننده ترامپ
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24994" target="_blank">📅 05:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24993">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ca302cfb.mp4?token=BKK_jZ_NaeUzndfxBlUYw75ro9vbKv4lZVByksDkiaN4XFaH1P1JrBoAvTRCh7sM_qELQRTFyVxz69RvRMu1GHGGWURclNMbwNkW_09xvKjnq3xw00vlLfS_WkSAnrQ5MrGzvpvDjIhA5n8Fp4L8E0dAilCMZ_oWPkevf_5CCIiy8xLsFnaQScyH93ocBw41SBkWiUr6Rs-ZVhBxzvSTy9h3I4NopukPK0YjElA_bQ15aVvuV9uNPr2V6x3vpt8ZPvKRBztPIRI12w25t36w4hFOLNONT5oJICrUdM9Yg7oq18H90QZ9uL10ywPMngLxy_z_AbfvuA7-q9z7lVt8QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ca302cfb.mp4?token=BKK_jZ_NaeUzndfxBlUYw75ro9vbKv4lZVByksDkiaN4XFaH1P1JrBoAvTRCh7sM_qELQRTFyVxz69RvRMu1GHGGWURclNMbwNkW_09xvKjnq3xw00vlLfS_WkSAnrQ5MrGzvpvDjIhA5n8Fp4L8E0dAilCMZ_oWPkevf_5CCIiy8xLsFnaQScyH93ocBw41SBkWiUr6Rs-ZVhBxzvSTy9h3I4NopukPK0YjElA_bQ15aVvuV9uNPr2V6x3vpt8ZPvKRBztPIRI12w25t36w4hFOLNONT5oJICrUdM9Yg7oq18H90QZ9uL10ywPMngLxy_z_AbfvuA7-q9z7lVt8QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ: «فقط یادتان باشد، من دارم می‌دوم، باشه؟حقیقتأ به تمام معنا، واقعاً دارم می‌دوم.»
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24993" target="_blank">📅 05:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24992">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571e103bc9.mp4?token=h3_2Zqr6bzod3KSMN4kDY5oaYi9BMBccuyl6w5o5CUc0Mc4ZCSF-A__uWbIKuj5HHrPDJS0iBYw2sBqaITwuv9Z66r8MZExK8pJ_-dfy8M8x0owj_zC_P4okmCaFgfqbosWsDM1OudYmGHjqI-J0VPELvF93D65ZPsW30svyiZTuPd3HVcUmyG1tYyrcTJO1QhEpwly7JSb7zfmp2BUABcy8oGJx6t9ptcfhq8PguQLBuPny0vtA2O6xc6PPaTeGOSowDf0JUALwP8vI7lCm3YI0LuPTcOkc8eka3bqXiVBwI3-1-IGGH2IDOWJ115NCYxl7u45ohHjfZR7IzbZP3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571e103bc9.mp4?token=h3_2Zqr6bzod3KSMN4kDY5oaYi9BMBccuyl6w5o5CUc0Mc4ZCSF-A__uWbIKuj5HHrPDJS0iBYw2sBqaITwuv9Z66r8MZExK8pJ_-dfy8M8x0owj_zC_P4okmCaFgfqbosWsDM1OudYmGHjqI-J0VPELvF93D65ZPsW30svyiZTuPd3HVcUmyG1tYyrcTJO1QhEpwly7JSb7zfmp2BUABcy8oGJx6t9ptcfhq8PguQLBuPny0vtA2O6xc6PPaTeGOSowDf0JUALwP8vI7lCm3YI0LuPTcOkc8eka3bqXiVBwI3-1-IGGH2IDOWJ115NCYxl7u45ohHjfZR7IzbZP3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره احتمال حمله هسته‌ای ایران به یک شهر آمریکا: «میخواهید بگذارید این کار را بکنند؛ بگذارید لس‌آنجلس را از بین ببرند، بگذارید سن‌دیگو را از بین ببرند؟؛
این
گرانی بهای بسیار کوچکی است که باید پرداخت شود.
»
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24992" target="_blank">📅 05:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24991">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گزارش چند صدای انفجار بندر عباس ۱۰ دقیقه پیش
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24991" target="_blank">📅 05:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24990">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871cf2b90c.mp4?token=LNvH5bszJtu889zC-xo0tbQwJTHfpGvuzKkyoZ4BLi6scREXMK9AEvoWiBTW_hUKWasNhTajn9o89aN0fz2uUVle0ros7hi5CrL2felEfQa6nhtMBNo5VFes8ChuvEl3oarDEMTYf_TQTIS9DnXRyHGFOWY24Eq-_rHmiWJv1OkkGcq4Q1GuF3iEjttg3gddj0T6wDKgVJeADxQ-qBB7mdXm8XHbSQWiV9RqpRZ6gIzgGcjWFbMxVnY55uKL7N6wJGP4Uwkd6RLkcUYWikRD644RKGyvI5FuK0AfYJHDHxR37ub2SF3BTbw2_JHWnTU-jUYqE_GUsejIm7sMFoFdE4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871cf2b90c.mp4?token=LNvH5bszJtu889zC-xo0tbQwJTHfpGvuzKkyoZ4BLi6scREXMK9AEvoWiBTW_hUKWasNhTajn9o89aN0fz2uUVle0ros7hi5CrL2felEfQa6nhtMBNo5VFes8ChuvEl3oarDEMTYf_TQTIS9DnXRyHGFOWY24Eq-_rHmiWJv1OkkGcq4Q1GuF3iEjttg3gddj0T6wDKgVJeADxQ-qBB7mdXm8XHbSQWiV9RqpRZ6gIzgGcjWFbMxVnY55uKL7N6wJGP4Uwkd6RLkcUYWikRD644RKGyvI5FuK0AfYJHDHxR37ub2SF3BTbw2_JHWnTU-jUYqE_GUsejIm7sMFoFdE4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ درباره عبور کشتی‌های آمریکا از تنگه هرمز: «کار نیرودریای ما حرف نداره ، نفت از قبل هم بیشتر از تنگه عبور میکنه ، هر از گاهی آنها یک موشک کوچک شلیک می‌کنند. ما هم می‌گوییم «بینگ» و موشک را می‌زنیم و نابودش می‌کنیم. به شما می‌گویم، خیلی خفن است! موشک می‌آید، موشک می‌آید، موشک دیگر نیست. تمام. و کشتی‌ها هم به حرکت خودشان ادامه می‌دهند.»
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24990" target="_blank">📅 05:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24989">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دونالد ترامپ: «آنها شیاد هستند. دروغ می‌گویند. ما کاری جز پایین آوردن قیمت‌ها انجام نداده‌ایم و وقتی جنگ با ایران تمام شود، که خیلی زود خواهد بود، قیمت نفت به‌شدت سقوط خواهد کرد.آنها نمی‌توانند سلاح هسته‌ای داشته باشند، چون دیوانه‌اند. این کاری بود که رئیس‌جمهورهای دیگر یا کشورهای دیگر باید سال‌ها پیش انجام می‌دادند. ما همیشه مجبوریم کارهای سخت و کثیف را انجام دهیم، در حالی که این کار باید سال‌ها پیش انجام می‌شد. این وضعیت ۵۱ سال ادامه داشته است؛ زورگوی خاورمیانه دیگر چیزی ندارند همه چیزشان نابود شده است و تنها چیزی که دارد ، تورم ۳۱۰ درصدی است، کار را زود تمام میکنم احتمالا بعد از انتخابات میان دوره‌ای
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24989" target="_blank">📅 04:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24988">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9b95796cd.mp4?token=rUPjEoCGuQE5_hh1n_6-Cnb4rVJNWnHyQ8SPpxDT2mgWKaU_U6mXKsn-5tql1jQQI7V46C88peyZSbqLQwmOdPyXKU6E7ojjiZH4YNwNuf6QkTyKdLb2cfTHkvTRrdXHOSsxIS3uFBqBZPWl-c1inSAEG9v29uJsB4t3Gg_Rpn1rctLoRqCXWe0SUmvX0nd77KrMDWIh2rjWA6s_zLzc-jstgR3z2qEZ6U4ywFmBFPgvQBJ-PYhBCRpxBb2uATZO9-ZU80qivbXzmdZykEFQwyFtR4H_kr1ZZMcJtv6Cjkv0_qwaMa1jghSW5c6ttdFfrg16oNJoynxoRmcXibD2D4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9b95796cd.mp4?token=rUPjEoCGuQE5_hh1n_6-Cnb4rVJNWnHyQ8SPpxDT2mgWKaU_U6mXKsn-5tql1jQQI7V46C88peyZSbqLQwmOdPyXKU6E7ojjiZH4YNwNuf6QkTyKdLb2cfTHkvTRrdXHOSsxIS3uFBqBZPWl-c1inSAEG9v29uJsB4t3Gg_Rpn1rctLoRqCXWe0SUmvX0nd77KrMDWIh2rjWA6s_zLzc-jstgR3z2qEZ6U4ywFmBFPgvQBJ-PYhBCRpxBb2uATZO9-ZU80qivbXzmdZykEFQwyFtR4H_kr1ZZMcJtv6Cjkv0_qwaMa1jghSW5c6ttdFfrg16oNJoynxoRmcXibD2D4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ: راستی، ما داریم به ایران در کونی میزنیم ، اینو که می‌دونید، مگه نه؟
این ماجرا، به هر شکلی، به پایان خواهد رسید. خیلی زود تمام می‌شود و قیمت‌هایتان به‌شدت پایین خواهد آمد
ما خاورمیانه ، اسرائیل و جهان را نجات میدهیم, آنها هیچوقت سلاح هسته‌ای نخواهند داشت
@WarRoon</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24988" target="_blank">📅 04:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24987">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پزشکیان گزینه جدید وزارت دفاع را معرفی کرد.
مسعود پزشکیان،
مهرداد اخلاقی کتابچی
، از مدیران باسابقه صنایع موشکی و هوافضای وزارت دفاع را برای تصدی وزارت دفاع به مجلس معرفی کرد. او سابقه ریاست سازمان صنایع هوافضای وزارت دفاع و گروه صنعتی شهید باقری را دارد و نامش در فهرست تحریم‌های مرتبط با برنامه موشکی ایران نیز بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24987" target="_blank">📅 01:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24986">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">فرمانده سنتکام، دریاسالار برد کوپر: «ارتش آمریکا همچنان با تمرکز کامل بر این مأموریت فعالیت می‌کند و علیه هر کشتی که تلاش کند محاصره را دور بزند،
سریعاً اقدام خواهد کرد.
نیروهای ما آموزش‌دیده، حرفه‌ای و مرگبار هستند.» به تمامی دریانوردان توصیه شده هنگام تردد در
دریای عمان و مسیرهای منتهی به تنگه هرمز
، اطلاعیه‌های دریایی را پیگیری کنند و در صورت نیاز از طریق کانال ۱۶ ارتباط «کشتی به کشتی» با نیروهای دریایی آمریکا تماس بگیرند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24986" target="_blank">📅 00:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24985">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0A5BU8LSWefsDI4_mB9Us5l89-r-OVjRycX5fN5IV95b_ePmqEqS_B0aO04ezLyzwf-8SHghqaXUSSrFWD_SeSUf1s1D4n3MOJQZZTqA_a7nzIQpDmanACRmNiyVtXUaoV1cZs65Jw7LEi2bsZpSlqt4sxmPUPe25XLsGKwtQ_R4fn6kqFUbMcJjoIAv4vZr5PR038OTge96zxgzKAzpnesaUO_skCFyujJ4NlNMafeaITIW9mGjZNaEkKjRlMLnQonaGUGynGEQ8Kdi8zUoz-wuXVz9q3K5VlIfANW12RsyY2QkWtY37rxq2K0rMJregqH9QyvCR4SUlyC59aQyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام اعلام کرد نیروهای آمریکایی روز دوشنبه
صدوسی‌امین کشتی تجاری
را که قصد ورود یا خروج از بنادر ایران داشت، در چارچوب محاصره دریایی ایران، وادار به تغییر مسیر کردند. از زمان ازسرگیری محاصره در
۲۳ تیرماه
، نیروهای آمریکایی مدعی‌اند
۱۳۰ کشتی
را تغییر مسیر داده و
۳ کشتی
را که حاضر به تبعیت نبوده‌اند، از کار انداخته‌اند. همچنین به بیش از
۷۰ کشتی بشردوستانه
اجازه عبور داده شده است. سنتکام همچنین مدعی است طی ۱۲ هفته گذشته،
۱۳ کشتی تجاری
را که متهم به نقض محاصره یا فعالیت در شبکه چند میلیارد دلاری سایه سپاه پاسداران بوده‌اند، منهدم کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/24985" target="_blank">📅 00:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24984">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کانال 14 اسرائیل
: لحظاتی پیش نتانیاهو با روبیو، وزیر خارجه آمریکا یک تماس تلفنی اضطراری و ویژه برقرار کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24984" target="_blank">📅 00:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24983">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c54e4b572e.mp4?token=sw_vQFKaUuma11QyLUbEkmsSTe7gxQ3rsmQwX45CtuFCY4CFOBSC7JpvO_fIgP1u3HaQ6i7yKLHHEHKdiMr1SOI_D0Ilh0zsdesHhEmVY71JUhNxjWybUEIqpRFrUFzFaxPdDICE7X16m1knam7viY70h5N_Sfl2fsY2x2zcNOy9w-9xmhvKnvPibsogrxBGwVj8e5h_gm4PCmggimZ7XgsDfsHKNnGflVqnuUP5HvTLLojQjzn-jF2eSHTfuuleS03lmk0uNlPmo7R-jFSlTd8ifYyLhAqqlogL91eohysbho7B1zoZgDQIFelOqa2G4QLb6ED0PdJbVrwVPTn3BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c54e4b572e.mp4?token=sw_vQFKaUuma11QyLUbEkmsSTe7gxQ3rsmQwX45CtuFCY4CFOBSC7JpvO_fIgP1u3HaQ6i7yKLHHEHKdiMr1SOI_D0Ilh0zsdesHhEmVY71JUhNxjWybUEIqpRFrUFzFaxPdDICE7X16m1knam7viY70h5N_Sfl2fsY2x2zcNOy9w-9xmhvKnvPibsogrxBGwVj8e5h_gm4PCmggimZ7XgsDfsHKNnGflVqnuUP5HvTLLojQjzn-jF2eSHTfuuleS03lmk0uNlPmo7R-jFSlTd8ifYyLhAqqlogL91eohysbho7B1zoZgDQIFelOqa2G4QLb6ED0PdJbVrwVPTn3BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی‌های ترامپ: «این جمعیت از معمول بیشتره یا چی؟ دارم جذاب سکسی می‌شم؟ چه خبره اینجا؟ اینجا واقعاً آدم‌های زیادی هستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24983" target="_blank">📅 23:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24982">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dd3fb47f0.mp4?token=GZLdX23K0rVpCv6bHw-jZ6xLHxcBwtBYHPhvCw0aPE1HtPyRNFJ69tnFsdzWEhn4UVRoYnqhQ6wJHCvB2LRKkj7McdwoXKXhzXRBlsPHysPsbevMjaBWq2pKyYESYFGpikvvzZNoBfKqrOyhoDDVbG4JpfG6XTHRKumhVpJV0T5kv0G0NgTsZiijPCnSC1R2tgSRzYzcMc_aVSbzJlkcIIG8GAZ08SnpS75Q1jk7h_GpNwRkPklwgfzWe2U-ORjiJGLEa6yF78bD03bUtsaMdaMAceJ6W1oomOKZDLbrspK_3TPqzwGVFmPmDgaHTsDCTrQDYtGOdh-htlzzwITJoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dd3fb47f0.mp4?token=GZLdX23K0rVpCv6bHw-jZ6xLHxcBwtBYHPhvCw0aPE1HtPyRNFJ69tnFsdzWEhn4UVRoYnqhQ6wJHCvB2LRKkj7McdwoXKXhzXRBlsPHysPsbevMjaBWq2pKyYESYFGpikvvzZNoBfKqrOyhoDDVbG4JpfG6XTHRKumhVpJV0T5kv0G0NgTsZiijPCnSC1R2tgSRzYzcMc_aVSbzJlkcIIG8GAZ08SnpS75Q1jk7h_GpNwRkPklwgfzWe2U-ORjiJGLEa6yF78bD03bUtsaMdaMAceJ6W1oomOKZDLbrspK_3TPqzwGVFmPmDgaHTsDCTrQDYtGOdh-htlzzwITJoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لوکاس فاکس، خبرنگار فاکس‌نیوز: «درباره فلای‌دبی، آیا فکر می‌کنید ایران مسئول این حمله تروریستی بوده است؟»
ترامپ: «بله، شخصاً همین‌طور فکر می‌کنم.»
با این حال، بازرسان هنوز در حال بررسی هستند تا مشخص شود مظنون با
ایران یا یک طرف خارجی دیگر
ارتباط داشته است یا خیر.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24982" target="_blank">📅 23:20 · 13 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
