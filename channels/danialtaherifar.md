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
<img src="https://cdn4.telesco.pe/file/SvQvnffA8e_rNhiD34RoBBlFDLCuOcfgIA9h3MkUa9szJKA_GrdjsDW_B3XTNsWL24MCWKrnBKx0ZMbTk0lcg8bcqiE0b9zP23warrksRtovsp9M2KMrqAdpTL3tKQm_3m9pzRwSbtYQO6z2Oe_1FWherBG3H87LakIZFDR2NS8NV9yPb-SEFy3Fei6YZINBFJlGr86aGo5g64c9iPq01DxOOsoqm211C-xP4Ow0AMw7Cugpt0SRPIbpZVzU7h4cCbObWsD4f8Q-vojXwkS_-MlD_Gpomdy_sTIiGTUiOmNUlcYxbgu_StQvutgDLyEHxdRcNb8PvNSLqpfE2iFxvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.53K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 14:08:44</div>
<hr>

<div class="tg-post" id="msg-944">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tH1izn4uscUogmPjzajujkEE016nFVWAKpKOBI-_UkG9rsSeV3vkQc8GOYfbZKCkl75EXO8qOtqMOL6SxVYwBxZaBH003wpp_YWzwt-m3QU3G1vnhw4UX6sSQuDK7e0u7EiLNjHvEsy1plXe0DP12DxDJHfLLVbCalIEdLN0wt0mo8qJxVcElt_-wK0FeXMq2aDwLUZzitGUDy1hzYS5YjyDcGa-xn-03UgDp1nu2crnAbfMvQOj4-c7XpHQ8LiDzeEoPquRtU7UAmCFvJraijoKwMQTrRXiR_NlM1JDZ_zTzg3Ls0Twmj6ACdW3MKtgFg4wZS2Fg8uAUbfMCN8hlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d93f82da84.mp4?token=iYU4rUvONR2Mp6wqnwU-OjKIWG1NwHU2laVtlv7_TWUc8jiGuUnP2crKXnB8ODXk6MTGpODhdraYMjONRvHqN_qpSn0Z8kRL3JrIKedCAjPxTWHTEU0CQB1FXxD7dDNhYX9UaaO1G0AaUA7Icis3UMtpwPj008rZZ8INNi3qRAchfhUDX-QfhQr1OwYbYufW3KHRGmRs5vviwMQbR96IxfQbF1g9h5gr93YXOyHJw9sDd3IBXiESGQB0-AoKqlu_rzSCfo39kjtYJZC_sIMIycVSp0mYsyYhMe96rZGnX6h-OwjGHFW2Bt8gn8ysJ4ss9eApm_F-E760S3OCK7vUJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d93f82da84.mp4?token=iYU4rUvONR2Mp6wqnwU-OjKIWG1NwHU2laVtlv7_TWUc8jiGuUnP2crKXnB8ODXk6MTGpODhdraYMjONRvHqN_qpSn0Z8kRL3JrIKedCAjPxTWHTEU0CQB1FXxD7dDNhYX9UaaO1G0AaUA7Icis3UMtpwPj008rZZ8INNi3qRAchfhUDX-QfhQr1OwYbYufW3KHRGmRs5vviwMQbR96IxfQbF1g9h5gr93YXOyHJw9sDd3IBXiESGQB0-AoKqlu_rzSCfo39kjtYJZC_sIMIycVSp0mYsyYhMe96rZGnX6h-OwjGHFW2Bt8gn8ysJ4ss9eApm_F-E760S3OCK7vUJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این وسط با kimi3 هم آشنا بشید!
یک مدل هوش مصنوعی با 2.8 تریلیون پارامتر! و کانتکست ۱ میلیونی که عملکرد فوق العاده ای داشته و در سطحی نزدیک به Fable 5 , gpt5.6 ظاهر شده.
این اتفاق بسیار بزرگی هست برای مدل های چینی و ما تحریم شده‌ها از امکانات دنیای غرب.
من تجربه کار با GLM 5.2 رو بعد از بسته شدن اکانت آنتروپیک داشتم که اونم سطح بسیار خوبی داشت، اما قابل اتکا نبود برای تصمیم گیری ها، و الان امیدوارم فرصتش بشه که kimi 3 هم تجربه کنم (اگر خاورمیانه بذاره).
@danialtaherifar</div>
<div class="tg-footer">👁️ 181 · <a href="https://t.me/danialtaherifar/944" target="_blank">📅 01:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-943">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_FAkdHvNreoZ9wY9xvqudm3hgHBk9ARvXa_VuhvYhmxx1YVQED0j1lQDkBXXTEN3rR9OzxsMhjmi3tGtx5jUDT4-DFL794lU3PskwY_-sT-n5x14y62Ots0o2P0XUttBCqYhjoQbTP6vIIVo8q3IwLagG8WdBQ8sncKNXsEK6g_Oc_XM_-_WJFKZALbXneMecoyXe-kU06poiTJHvjGo7l6z1-v39tK18DesQe4D46gIkktNvnJxgKHu3ldvCdsmJeeNFlj-GgvzNdSgMEVMFT8mtzWYGjoKiCKd2QKaUxRnWobly-frwXB1PHdCegS4EA0iH0WsC5zoIuxHAZ0bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از ظهر امروز اوضاع نت اصلا خوب نیست و رو به بدتر رفتن هم رفته
کارای مهمتون رو انجام بدین، احتمال هر شرایطی هست مجددا
@danialtaherifar</div>
<div class="tg-footer">👁️ 239 · <a href="https://t.me/danialtaherifar/943" target="_blank">📅 00:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-942">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">باز بریم بک آپ سایت هارو بگیریم :/
@danialtaherifar</div>
<div class="tg-footer">👁️ 421 · <a href="https://t.me/danialtaherifar/942" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-941">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">📚
۷ ایده از Phil Chen درباره آینده کسب‌وکار در عصر هوش مصنوعی
چند روز پیش رشته‌توییتی از Phil Chen، از اعضای سابق OpenAI، DeepMind و Scale AI، خواندم که به نظرم یکی از ارزشمندترین مطالبی بود که اخیراً درباره آینده کار و کسب‌وکار منتشر شده است.
خلاصه مهم‌ترین ایده‌های آن:
۱.
هر کاری که خروجی آن قابل ارزیابی باشد، دیر یا زود خودکار می‌شود.
بنابراین ارزش انسان به سمت قضاوت، خلاقیت، تصمیم‌گیری در ابهام و اعتمادسازی حرکت می‌کند.
۲.
کمیاب‌ترین منابع آینده پول نیستند.
زمان، اعتبار و روابط واقعی، دارایی‌هایی هستند که به‌سادگی قابل کپی شدن نیستند.
۳.
مهم‌ترین مهارت، انتخاب مسئله درست است.
وقتی هوش مصنوعی می‌تواند بسیاری از مسائل را حل کند، مزیت رقابتی در انتخاب مسئله‌ای است که ارزش حل شدن دارد.
۴.
به‌جای ساخت راه‌حل‌های موقت، سیستم‌های مقیاس‌پذیر بسازید.
هوش مصنوعی سرعت ساخت را بالا برده؛ بنابراین مزیت پایدار از سیستم‌ها به دست می‌آید، نه از ترفندها.
۵.
تمایز واقعی در «آخرین ۱۰ درصد» ساخته می‌شود.
AI پیش‌نویس خوبی تولید می‌کند، اما کیفیت نهایی، سلیقه، جزئیات و استاندارد اجرا همان چیزی است که برند شما را می‌سازد.
۶.
هم فرصت بسازید، هم از فرصت استفاده کنید.
برندسازی، شبکه‌سازی و قرار گرفتن در محیط مناسب، کیفیت فرصت‌ها را افزایش می‌دهد؛ اما اجرای درست است که آن فرصت را به نتیجه تبدیل می‌کند.
۷.
هوش مصنوعی فقط یک ابزار نیست؛ یک طرز فکر است.
هدف صرفاً سریع‌تر کار کردن نیست؛ بلکه ساختن سیستم‌هایی است که بدون وابستگی کامل به شما نیز بتوانند رشد کنند.
جمع‌بندی:
به‌نظر من مهم‌ترین پیام این نوشته این است:
مزیت رقابتی آینده از «کار بیشتر» به دست نمی‌آید؛ از «
اهرم بهتر
» به دست می‌آید.
هوش مصنوعی دیگر یک ابزار جانبی نیست؛ بخشی از معماری هر کسب‌وکار مدرن است.
📖
منبع: رشته‌توییت Phil Chen در X
https://x.com/philhchen/status/2072793818945167475
@danialtaherifar</div>
<div class="tg-footer">👁️ 475 · <a href="https://t.me/danialtaherifar/941" target="_blank">📅 10:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl7RymQ0E2kUM-BU_JbHOOLzgbCjf3tPXSCHqgI6m3wyd3pxAHGHbpsyc3ShHdXAeR9aA6WcOnPr4ElQGI0Y2rQ-zPryTOIGRBVkP3w1mlOS-YWlegNWruFkBRjIYxi5uzJxid5dZvg7DDUfAYkzaNzCftYycE6-2s7Lk5-j6YDBHLF8YSffu9IBLWryLw-kjRfh9tep8tchdUifB04gEZO3wZ7azu_pRrZAKEa1Tc5Sx-QZj0TY87U9awNXpwgehGELBMkaZ1ArYSHlQ9LJMuk9tHL2A8Kn59sklBwjTEb23HLA4sHtaPHw3xUFmPIp9jwDnp6VkvGCUzdCklNylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 831 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست
دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل
Fable 5
و
Mythos 5
قطع شود.
نتیجه: آنتروپیک مجبور شد این دو مدل رو
برای همه‌ی کاربرها
غیرفعال کنه تا با دستور هماهنگ بمونه.
📌
نکات مهم:
• مدل‌های ضعیف‌تر مثل
Claude Opus 4.8
دست‌نخورده موندن و کار می‌کنن.
• دستور از طرف وزیر بازرگانی (Howard Lutnick) و دفتر BIS صادر شد.
• دلیل دولت: کشف یک تکنیک دور زدن safeguardهای Fable 5.
• آنتروپیک می‌گه این jailbreak
محدود
بوده — فقط یک قابلیت خاص امنیت سایبری Mythos رو باز می‌کرده، نه شکست کامل تمام محافظ‌ها.
یعنی عملاً قوی‌ترین مدل‌های هوش مصنوعی آنتروپیک حالا فقط در دسترس آمریکایی‌هاست.
🇺🇸
@danialtaherifar</div>
<div class="tg-footer">👁️ 929 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 953 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 949 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=d8RpRKbXVrcHYv8WSMjjJ_6EJ5jrR3io8WJBhbkE377hZFrhsvzTYYrscKK2xV-iCus6sYx-UwJAjCyKxK3l2MZzELYi-5FnjigwG9q3kVCvp-vQpzpacSRkpE3InbbvValjTxuvmE8SsfhH5XTqtdyA0aDDlW7-jbkPF6lcRukPegwFHqsoN8LFygwjZ4N8HJuEWoWEgI9mfR8CGnOZEIDw6cO0YfOfkfsyHdR019Shc6diPpKyMlv0OYjByv_FtNRgh77by126cBxiBhJPN0cebFIaPT7LtK6cw6sLxow8N8xP0ZQWeW49kLyPTr7KSpB6zecbyUzqP97JooXS2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=d8RpRKbXVrcHYv8WSMjjJ_6EJ5jrR3io8WJBhbkE377hZFrhsvzTYYrscKK2xV-iCus6sYx-UwJAjCyKxK3l2MZzELYi-5FnjigwG9q3kVCvp-vQpzpacSRkpE3InbbvValjTxuvmE8SsfhH5XTqtdyA0aDDlW7-jbkPF6lcRukPegwFHqsoN8LFygwjZ4N8HJuEWoWEgI9mfR8CGnOZEIDw6cO0YfOfkfsyHdR019Shc6diPpKyMlv0OYjByv_FtNRgh77by126cBxiBhJPN0cebFIaPT7LtK6cw6sLxow8N8xP0ZQWeW49kLyPTr7KSpB6zecbyUzqP97JooXS2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گوگل از قابلیت جدید «Search Profiles» برای ناشران و تولیدکنندگان محتوا رونمایی کرد
🔍
گوگل قابلیت جدیدی با نام
Search Profiles
را معرفی کرده است؛ ویژگی‌ای که به ناشران، رسانه‌ها و تولیدکنندگان محتوا اجازه می‌دهد حضور خود را در نتایج جستجوی گوگل بهتر مدیریت کرده و محتوای خود را در یک صفحه اختصاصی به نمایش بگذارند.
📌
این پروفایل‌ها به‌عنوان یک هاب مرکزی عمل می‌کنند و آخرین مقالات، ویدئوها، پست‌های شبکه‌های اجتماعی و لینک‌های مهم یک ناشر یا کریتور را در یک مکان جمع‌آوری می‌کنند. کاربران نیز می‌توانند از طریق دکمه
Follow on Google
آن‌ها را دنبال کنند و محتوای بیشتری از آن‌ها را در بخش
Google Discover
مشاهده کنند.
👥
در فاز نخست، این قابلیت برای ناشران و تولیدکنندگانی فعال می‌شود که در حداقل یکی از شبکه‌های اجتماعی اصلی دنبال‌کنندگان قابل‌توجهی داشته باشند. طبق اطلاعات منتشرشده، حداقل شرایط شامل 100 هزار دنبال‌کننده در YouTube، Instagram یا X یا 300 هزار دنبال‌کننده در  TikTok است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 944 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSD5UXEfCdWRctwf5H8wYuai21mNrk2OV8iNxWkYmuKty91sM26edoY9besy4obLE5DIazpIKV5TvwVxSq976DQ3qtKq8kwcZmNYrXLHirxpDgmzYlH4WHoQJEoy0G8OK8QZSKnWXJIOlGgNZ_RT6P_BAi7kh0H1eY3HId6dRJpQp1JHFVjCix2N4hSCtF7m5mVdLJRW6jb3fhXYJpBFCZJZnrLUWL7UvWQex6mk06pEYLvQwTjKeMjz-uUBTrRIldxKrFalK1CXEJAyuPSCng9ljed0ThwZfzRLksoRHDa7gJ8IK53X2V9CDsiWxl6vViN5F2OfRLvX3xf5koCJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل گزارش عملکرد AI را به سرچ کنسول اضافه کرد!
گوگل رسماً از قابلیت جدیدی در Google Search Console رونمایی کرده که به مدیران سایت‌ها و متخصصان سئو اجازه می‌دهد عملکرد محتوای خود را در نتایج مبتنی بر هوش مصنوعی گوگل بررسی کنند.
📊
این گزارش جدید اطلاعات زیر را نمایش می‌دهد:
✅
تعداد Impression صفحات در AI Overviews
✅
میزان نمایش صفحات در AI Mode
✅
حضور محتوا در قابلیت‌های هوش مصنوعی Google Discover
✅
صفحاتی که در پاسخ‌های هوش مصنوعی گوگل نمایش داده شده‌اند
✅
آمار تفکیک‌شده بر اساس کشور
✅
آمار تفکیک‌شده بر اساس دستگاه (موبایل، دسکتاپ و تبلت)
✅
داده‌های ساعتی، روزانه، هفتگی و ماهانه
🔍
نکته مهم:
این داده‌ها علاوه بر گزارش اختصاصی AI، همچنان در گزارش کلی Performance سرچ کنسول نیز لحاظ خواهند شد تا تصویر کامل‌تری از وضعیت سایت ارائه شود.
⚠️
فعلاً این قابلیت فقط برای گروه محدودی از وب‌سایت‌ها فعال شده و گوگل قصد دارد پس از دریافت بازخورد و انجام تست‌های بیشتر، آن را به‌صورت گسترده منتشر کند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 759 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 765 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 932 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBTdd1W7EeJ7lHjkGVPUecaFU5ZMJF8yAdeRl6e1R2myyGUcPcCHsMfJqae2dANfXsS8jDvhimLUORHoSduwdXapVY1wuolypa8hwpndWjrw5R8tVJ_6fmiBIla0GSfKKI7ZG4EL1IcnBojzvGHj6wM0jeOGyXxyKG9wysxe0S-MaBSFp9pJ-x14bVPtgsXQzEZ_Eqd8SwakkvK1F6wggBWG3pvWlSU60F-EXMgLUvy7NvBmCeXUVOVB7HxILb38sDYEO-NoUz83E0tRm_twlrVc9QfRK2T8pTFSKq9Z4mx8aPbyI_cjmN1ZnifjP9FIrLlFQWcPA4E_2QrIUW3hFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3R-Nuix9KOj3LDXPn0ZhTm2gLBq1QnGpWFuL4-o0-aazqK9ILq9utP3lsy1MGJpaIlF1uLqVASHhUnGFigib_-DrUbyaQgpOCrKX5kSbWua8Ddv2AZqToBe6iYeOUzhbT6BaNcajR3Nf5hfeznqO-QSjs9JhcwYd-CnFuhxegto8yz9hhZVtdsix6a39kdaAQD0bXcsJ-IMSX1yZcrSdqmcUR7uEBT44kPaoSImlkE7c0SzDoxhz0ChICh3joFCGVSyHy0z3lx4d8KcPgo1rCZ2Nx2OuMjloopyJlGH4_tfVoVlKJFZ8XMIgyWRKOv43G1gCmf7duhmpsdeaeuKDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHamcPTHs-WtFTPReW9emljWsITD3-Tj_cD4BIdxaAGhk1Ur2pvdTo1P3ymM9dnGzp9wWKB2jQKKMKEZa1h85sP01EaxUYTcfRwI__emnd7FNDxTsKHeVkyoAsCCPlDKqMpCXqPCCV54-ToA6wbvBigLGerDlCVINRYesaCIicNHbKa0ogmdz3VblKYV2FtgEM01S5ATPDmXswzZShpPw_lBuNQgpPn5eQiilvv4Oq-fyhGgu-H0WJB6Xtg9ZkWOcGpyOBZ_eX8BIvZH5gcdyJ2q7saSwE7B3enolwKG9bc36YmIrwK5WFbTYIDS9VXcL093ym2ufzyuc5iUtneGFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2cNy1eEN7npN0HosvkiaMGIiZq-Hso8WdGn2IiCctLgT3ShQsAzadBDZ6u-ZqBLsAjJmjyWitouvuQKKTiatxMuCx6lF4Fm8Jnqcvk8konLFNoCRMR-uOysU2Z01_9JBebD8RU65fPRnvSbo4R2X4gDGD6MV10VEGHO_G13OF37dczzKHavX4O_39YM1C7OY6gvI2jNf5raIG2ehkq3I5R-rSBSDSDpymgjsc_NtrsKz1m0-Q1HVUo-kIDn8Z-k8D74blTJbyM0sbBiCnhEi51QJXROnqxANT5lI8MGbweMdpjj585zX9bbIQfNye86iLM2dJBPiVAQjyZwn-Sm5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل ضربان قلب کسب‌وکارهای اینترنتی به یک «خط صاف» صفر...
💔
ما کسانی هستیم که زندگی‌مان، تخصص‌مان و آرزوهایمان به این «ریسمان نازک» وصل بود.
این فقط یک نمودار نیست ... این، فریاد خاموشِ میلیاردها تومان سرمایه، هزاران ساعت کار و تلاش و امیدِ صدها نفری است که در این مدت، نابود شده‌اند.
ما یاد گرفته بودیم با الگوریتم‌های گوگل بجنگیم، با رقبا رقابت کنیم، با «محدودیت‌های فنی» دست‌وپنجه نرم کنیم؛ اما هیچ‌وقت یاد نگرفتیم چطور با «قطع شدن» نفس بکشیم.
بیش از یک ماه گذشت...
یک ماه از روزی که «دسترسی آزاد» به اینترنت، تبدیل به یک «رویای شیرین» شد.
آقایان مسئول! این اینترنت، برای ما «تفریح» نیست؛ «نفس» است. برای کسب و کارها، برای فروشگاه‌ها، برای خدماتی‌ها... برای همه ما.
#قطع_اینترنت
#سئو
#دیجیتال_مارکتینگ
#سرچ_کنسول
#کسب_و_کار_اینترنتی
#ایران
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdWYHFgHKzKPeTJN3wGuQXZRZEwEu76NnJtchwUGlM9_LfUSHuWH2ch3xmGwXIiC0Ih64KJXtHWr1WSMA5o_XIYqNf8mAozWREOs0zCREZ7D5Cj4tskJW9ocOK6dQXOAKJHKhuYeyvUPFi6ActogedsX9I8io8T3DSo4E83O-uDZdi7rfhRsJljSf4_-2O4159pZ6LdQrxt2_J7laK_nT0DNDog95S2VT_LJEG1lcw0uczhPTREnnIrIhDfOWsdYSNh8o81dhOkBtrxEnw5j8QMEoarTq6AS82v2iDHGtfOPSFv9bpjLw4aOrijSoDbu6liwRe3RGsxSBocw6Xe0GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 966 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 926 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 985 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRITgvcY4xkmqK1DZIr_PT2Z1ZdLJxYs_C5tsufi8a901ahX3zgsu-NrbFaHTuR1BcBSaY_TBpjplR3mq1vmiZU_4AE1AJFhr1muKOg2trHSgBb9AAEFyQ8TsylrVamWxRpaYes_rWwlNHje_nbril_cuN2gsHeI_APsgPTJVmZrMjsflkLiLnyvT3Q5ETCQiJIuBMZQYsAUnPFPsydiJwbvyB4L4mNLvmkv18dr7tJLG8rGa_iFgb05mXB8nbg--zTy7BhjOCBb3r16Eap1VHz2__tk8o25xoBMYaiuJLOrCJgdIF339DIN-GiFTcTjGvDH9cqwfPdJWDPUl8LfBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FRV_To00ea_DryIB3dFNWj1vL5SEgNS1LOZezNpNaFCc2jrh2XOPogWlQU2TX3hY_YSrytn6GSJDkkELOXiXELZBE_8NrsZ7IcAaSTfCrztHXHw-YM2Fm7F8qL-km1Ph4zpT-tfX5VqmvToE97xYlVT2YrC8VcoezioHBxsmBi83J-XhlfQWRf0Q8EE7BTAsB5WME2YIeekNdf30DUjDwnNgNFYT3uLh561KtMNpfCqhCl553vJ1pBGRUs0qfn9H6Ku_psmQ_RpkSjt4axeDqrcXbO8bLvh6IBLyHjUpJkEvXy8eVsRLmove4MzakWZ9jKfa4GC_YubY_w0pseRlLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R9Sdg0xt7bVxwgirpwF-Ry7ezQLdP7p9bXaqztc05XPj2h8F_vTLZcnrLVSqLeXwYPirpWpCZWZZSxvNOvaOqhx04Y_lNB1yaAS8UhETxlFM1y_uqq5I0huOKvT9BZeCZOvqBEjBYqysm_tFEVqFtHVuiZb0GBETN4tME58ah2nDifzJA2km827_vY7ZFVBihSq6NB-I8WlG2C2Tt9wt57oQdDHNcgTbJDVKx48WX1DI6qjyoDFyj4dqSqkAUIFtvg4vjyfwveHAb6OzO-mn__xXjlifkDEL8vjq65PoSUyvpISfctmzKGMkSb5P03XHxDi0KBtclOerv0R-ou9Oig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4K6PNh9k6Nevpj0IcBvEKG1-331NMAvCvbNJbo0COOGFTxM6DwTUi1Wocwyxqqh_xMrkj0jzOW0XRxUAQkP_FXS0fGvksdVe1vs_5YVrHNHE-W1W0Vom3k_9xIWuTNUGuNkAekZCIwapwVsnLUR9B9Hvp1_3_9E8CevXHqXoUoOJnqHN3iFHsDcgLmuna8_2K1Ma3YRJqjyW-8cB2uPoUU-in_u479I1KVOTavpj7zHiahJXRFkzbR5f2EavlYD_AydGf3EvPA-DDdFEmlv6TAR3KEDBKWHk4P5sk23Nh2WuNw9odmnjzPZmgrlFvbr-xuzLeyZMlMfV7HkMWGXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 898 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 978 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 851 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 693 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 919 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjwAU5-sN_nVBAgbCNCM5Nztl4bu5K9nRY4cSB-BpOtoz0tdP9KeVi1PVShZOsSHohjtWwvzlljCKJy8y0-QtncbH8nG16HxDI7VyJlnZ4fxR1GhUId_j0qLWaCxUqtwvFNzDxN_X5irEqOVy1eWGhkDM447vqK6UxwLiCvXOpZ3jgkDOqyon-zOXFhBASTM0vR-XmF8OhOJInK0VIZeKofv-Bw179cgSi0KO2crSaypx2pNtmS0u4adevlPW1DW1sWqhlo-sH4-5rZd4oVF2x30Ld-0QCDMnIF3g_7Zf9C0BBF5izFd9nFFSGv9uj6mh7lRyBr0CpJEDE8mtB9SIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 901 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🟢
راهکارهای رفع مشکل سایت‌هایی که داخل ایران میزبانی می‌شدند و از نتایج گوگل حذف شده‌اند
برای این موضوع چند راه‌حل وجود دارد، اما رایج‌ترین و عملی‌ترین آن‌ها عبارت‌اند از:
1️⃣
راهکار سازمانی (Enterprise)
استفاده از CDNهای Whitelist‌شده که معمولاً فقط به اشخاص حقوقی و شرکت‌ها ارائه می‌شوند.
2️⃣
ایجاد Mirror از سایت
ساخت یک کپی کامل از وب‌سایت روی هاست خارج از ایران، به‌منظور دسترسی بدون محدودیت گوگل.
در این روش DNS به‌صورت هوشمند تنظیم می‌شود
ترافیک داخل و خارج کشور از هم تفکیک می‌گردد
⚠️
به‌دلیل اختلال در ارتباط مستقیم بین سرورهای داخل و خارج، معمولاً امکان سینک دائمی وجود ندارد یا این کار از نظر فنی زمان‌بر و پرهزینه است.
برای اجرای این روش، با پشتیبانی هاستینگ خود تماس بگیرید و درخواست سرویس GeoDNS بدهید.
3️⃣
(در صورت دریافت مجوز از سرویس‌دهنده، اعلام خواهد شد)
❌
نکته مهم:
در حال حاضر برخی سرویس‌دهنده‌ها در حال بازگشت به دسترس هستند؛ بنابراین پیشنهاد می‌شود از انجام تصمیم‌های عجولانه خودداری کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 841 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 782 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
رفع مشکل کندی پنل وردپرس در زمان قطعی اینترنت
اگر از سیستم مدیریت محتوای وردپرس در وبسایتتون استفاده می کنید، در شرایط قطع اینترنت به دلیل داشتن درخواست‌هایی به سایت های خارجی احتمالا کندی پنل به صورت بسیار اعصاب خورد کن رو تجربه می کنید.
دو تا راه حل واسه این موضوع هست:
۱- مسدود کردن ریکوئست های خارجی در مرورگر با زدن کلید f12، رفرش کردن صفحه، انتخاب درخواست های خاجی(از جمله فونت های گوگل و yoast و ...)، راست کلیک کنید و زدن گزینه block request  (محیط dev tools باید باز بمونه)‌
۲- از طریق فایل wp-config.php کافیه که کد زیر رو در کانفیگ قرار بدین تا تمام درخواست های خروجی رو متوقف کنید:
define('WP_HTTP_BLOCK_EXTERNAL', true);
و اگر دامنه بخصوصی رو نیاز دارید که در ایران میزبانی میشه و در دسترس هست، دامنه را در کد زیر جایگزین کنید و بعد از خط بالا قرار بدین:
define('WP_ACCESSIBLE_HOSTS', 'torob.com,*.danialtaherifar.ir');
با آرزوی موفقیت
❤️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5JaD43KpTLXtR3dgwE8PxIF4i2hHgi-J571O1JjYU0mBQFq8k657SEiAziQjy2hejI6cDCn2jz0Om7oLp2jhTlVKRxjj2LC4debQEb2zwLrLFxQD93v43smbLw6rcQdqe_ASRpaWOOlQrMJup_ndQ1oUQZTxiQP6JFgFufR379fue0dIsYElhvKP5EjvW4uF0aFdque-4CtSrD97vhR52-lbCoa2QFiqLEmPMzo-fGxAAHimIOFnzmgOwztNBE6M5KWbMhckBmezgZaiZOucMMwJni99yAkZw8t-NNN9G7-b5AmWIhPuXgeIijs6VVBiGv22UvNCPWPjrwMs0N1pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 859 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 693 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sp-MeX1eICABj_sYtBy--nZAPpQJACqA6Urulzwj0Z1lZttsR1hbQAU7CeTptQ0ihk2W3GNPqaYTVhTWbhcrLsA2eALojwfyAdYvh5m8jIR2GPvfqCF30b6UfFLrjxeF0TLn9fzgN-GVeT2sWoaO_CeXSnd7G0L6s9-vfIem0FpIagTSQIYUHxvi34HuwXrcD0sGhzm0ZkVHkL9EYrPkRb847xsET1XhU3F0C4IVz6xbbcH6cGRYFv41Dh0I0nT_gGfGhfCgwuQEl-YG9j5oMJZd8zY8EQuC-_xt3W0WeMV5kzadpKXJTJ0l9TQrG5b3vxG542VqEPfaX1iHNfTCag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 894 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jg2a3UKwtRYnNmqC2lGcK4nvdrvwIwZKhw0sb1fG0izsu8SnUpvZu9vP9PdGgolL2cjGevcDMSS_dnCiBePsV9AkfARMsVkAaMHZ5FIcHDrPNXOaIaGYhtmHUzfZkl2cVoCU_tdcHthUZZxVtKlKGjHz6dCSVlZzL4Awcstf8LnqmKALdIC3S59Zm6Aa2nvvWQkbTw-4aSX8l5wsvHGfW7Ne-ggAwmJlprOdG50t7rHH2tTIJLgtT2Qw-SCIInyhRb4qbCQtmTLc7F4OoE-PjwcX5t5fEiprdQXwjSXCQnXm0eD3TCLC_jqdYLqV7_Ynneg-VXy9WseE-OrDTtDc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mnXhHc7OtmESjnO-nlzbCGP7pdUAJY4DWviN3Eb2YtRg0jDufggYH8Deba3-bwwUkJsrd5Cx4aMPf-70503lykni-U3cbQn4Y7sZU-nOmEnVWCAdjIViOfeslkNZMWgMy5poZGU5o1FBm9JqkNgI_R22nl1yvEpcTJ1frJbGXbMIV9-fVwBcEBrbWmtxd4nYxl0MF4aq0_11W-GsHSc0GkHfONh00uR_oevTpsmt9B238zvY0t2bjkaotfyLWcLPIFKouqEJycWL-6fhkhg0hBjGGDc4mz8jrtoEA1-DlVlWgKn8WKkJSXFKnm8mF5lCDWJ8pjvX4FoIkXEIvANDxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMLCtS0kaOMcqieeXlHtX6JwXC05-qFVc7q8yseUdF1X80moCnTtG4inLkosBKqMo_X2OZR-1TjTPzOjOPehkYmT9GpzidA3bwGi0YNeMbjf9iSFF-dIzOQpqLXQDd2GfGfJfRwPH-iUdgVHIYFN2DEXP4zNMiITde0sDu0Vg0rGY6A8qOtsZs2sLxWWrT4HciB-hIJpJ4eaIls0OmNbPzPll-TJwP4B_69Qf1XEo4nb8Dt5YeHgrlFQSbAKubCc3n12j9B3CbLKqhaiW8a-wKM6wGmZgr7dKSfUzTAy8Fw8-WfRv_Hf2zPwSKYsXzTGMxycc_Ppkh1nAb0t5ytgrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xmw-FNn7JbpGagm0wiBntmw_a6XyyM-X--558y8kpKn6D1M74rze-SUbTDMThJrZKhgpayKOpWfeBGHt9PIJUIHa8QUV52hnv_3H8n8V_tCc2RRJFvUpXOsC31w6Wv-mRFzGfghpV2k0ReRCb9yFJkmceeNuM-b8rC-ZLyo6-YSD4XLusqkfOtSSSnXPw68JpgMcjQMvsBDnijsEOzDCsowhbpPaaOnUpy7Mt9fhLbIozHCZZs5w1vDcB-Rtc9lhIM1k81YMEz4NZwhEh206OPc6w9pGL5YrVQv8RNUnDYP9VqpzZ2v7LtdxaNHh2u1TEC6FMRlfeTp6Gjifa7n2xQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 985 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YE7IUylxfdmz8MXcevsGdgoA39Qt7-0rRFVI0hO2sKqPTI6XU4TKd_FXj_m6ZjSJqjAnTVTpZXAXrqhtSG0_-Vf8zjf_waC9nEJYJ6KFs-avl808TZF80qnB7lkNe1Se_FgqA93cQ5pY0-fC67lQqhcAlANNUXBRZvT-ZrUS2Bj3VhkevEJKjclcRj2zSUZDr1bbT5TnPmGfb5LmxX9fd0lm80_shngi6SfkGIncnIl0-sn3LDNWIVrAZZ0nwt43N6mqU7l8cYJJ8pxHM9UX0XcNNtndoO9wIasFhhMTsO9meYDY5Z-OZrRYtD3SPm7zUJrjcOBd385-_BBb-ytJBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 891 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=R-Y-0TFfdbLO8srN5VJUtaFPdNSHVcWYJNTqm4QER-zu95xLDUvZha5av5wQHsHKzza2nx3yDpVq72HF5b5OoiSZGuTh9NEQCwYbJm70w0Sif8UFTHvYi9Rf_S7AjPb99qZbmGRgjTyExDYs62ciL78st4eLBxj1QTfJJmhn-Efb-99iV367Tc64vU8-ohNK7VRfXx2v8LwXZSRzF00KDsSNLBRSf12S6BIYMY0FVDtgyizBxHGAr-kASStnIbU7SnaW6XWSImmA-74VL9uzfRB2oL3fenqBdXkSgqD2PNJPGNznfihac4IGrwMnaOx2Ab6lx9VglC_eCmBVdmw7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=R-Y-0TFfdbLO8srN5VJUtaFPdNSHVcWYJNTqm4QER-zu95xLDUvZha5av5wQHsHKzza2nx3yDpVq72HF5b5OoiSZGuTh9NEQCwYbJm70w0Sif8UFTHvYi9Rf_S7AjPb99qZbmGRgjTyExDYs62ciL78st4eLBxj1QTfJJmhn-Efb-99iV367Tc64vU8-ohNK7VRfXx2v8LwXZSRzF00KDsSNLBRSf12S6BIYMY0FVDtgyizBxHGAr-kASStnIbU7SnaW6XWSImmA-74VL9uzfRB2oL3fenqBdXkSgqD2PNJPGNznfihac4IGrwMnaOx2Ab6lx9VglC_eCmBVdmw7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCxBbCu8Wq9cgyCsBTQqHzarNEZ9EKp5ru-HSqCo9NizKMhQf8pfJKZzQz6xVIsP9MHlE4xmf0f5P9oScwv55bvVQ_QrfcsLFrHabcXCwlkzbMAZGuo4S0NCUe7qiQ2KRUv3OpSk__-Nbax1zLmbOMe3hS5IMgG4cpdnciKvEI5yCX2_9tFNItCevvENgy3R04xsyM9fEzRCInWY7hmeXz7-LrChH02_9mE9sEAe0hhTvJ8YzkYlklYOQlGQ6yzD6Fcvh8r97cVpMmkhVuYjV0FmHKsX65EC7-FFZ1_xXV1NdcI4oWFpbo3xcWNYGQIFHDbG48s83JXQQBfC6nTtuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
برای دیده شدن در AI Overviews چی کار کنیم ؟
برای حضور در پاسخ‌های خلاصه ‌شده هوشمند (AI Overviews) نیازی به AEO یا GEO نیست! فقط همون سئو کلاسیک کافیه.
📈
سئو معمولی = سئو AI
گوگل تأکید کرده که AI Overviews و حالت AI Mode هم با همان ساختار سئو سنتی کار می‌کنن
🧠
کیفیت محتوا مهمه، نه منبع
محتوای تولیدشده توسط هوش مصنوعی یا انسان، فرقی نداره؛ مهم اینه که «کیفی و قابل اعتماد» باشه
🔄
هوش مصنوعی در همه مراحل سئو دخیل شده
از کرال شدن با گوگل ‌بات تا رتبه‌دهی با RankBrain و MUM، AI به‌طور عمیق در فرایند نقش داره
✅
ویژگی‌های AI Overviews مخصوصه ولی پایه‌ها یکیه
فرآیندهایی مثل "query fan‑out" و "grounding" برای دقت پاسخ‌ها استفاده می‌شن، اما تم همه‌شون سئو سنتی هست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">😧
یک نکته مهم قبل از خرید بک لینک های سایدبار که باید بدونید
✌️
زمانی که بک لینک سایدبار در کل صفحات داخلی یک رسانه رو خریداری می‌کنید، اگر اون سایت فرضا 100 هزار صفحه ایندکس شده داشته باشه، بعد از حداقل 3 ماه با ابزار های مختلف مثل اچرفس و سمراش و ... متوجه میشید که احتمالا بین 20 تا 30 هزار بکلینک رو دریافت کردید (ممکنه این عدد کمتر یا بیشتر باشه)، حالا چرا بک لینک های کمتری رو دریافت کردیم در صورتی که اون سایت 100 هزار صفحه ایندکس شده داره ؟
به غیر از موارد تکنیکالی مثل نرخ کراول و ... ممکنه زمان ببره بک لینک ها در ابزار ها و سرچ کنسول ثبت بشه، متاسفانه برخی رسانه ها با روش های مختلف و به کمک
جاوااسکریپت
بک لینک شما رو فقط در یکسری صفحات سایت به
صورت رندوم
نمایش میدن !
برای مثال شما بک لینک
دانلود فیلم جدید
رو ماهانه از یک رسانه با قیمت 5 میلیون تومان خریداری کردید، برای تست وارد یکی از صفحات خبر میشید و میبینید بک لینک شما وجود داره، اما اگر
رندوم
وارد صفحات دیگه بشید، بک لینک شما دیگه نمایش داده نمیشه :)
رسانه ها برای اینکه تاثیر منفی کمتری با فروش بک لینک های سایدبار یا سایت‌واید روی سایت خودشون داشته باشند از این روش استفاده میکنند.
اسم رسانه خاصی رو نمیبرم، اما در خرید این مدل بک لینک ها حتما دقت کنید، بابت هزینه ای که می‌کنید ضرر نکنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 937 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHgWxpNaN4_90URQYTVNuzFV_oYok-9ltvUxXIakAirNniK0gRK5Y840hmVm7KsElIpPurLMsR-OhDRDwbwa-_3D_zvhs4vWzRFpcJbll-5L-oGWGxWL4So34bNMHNTSWlFLfgEIUaiExaq1Mv56tTDUBbiqNB8VAMK57W66ajxkyQyZZHmyUGTz5K9pNX-73U4jXlFS1GTzMGwOPfCyscxU9NzLwlEZB3bFNwUx07hYjLEc0fle7uZ-EKfKWnf1M3t7k4XGkO1qRXUX0oEr4P3q8mIuq_-zyE2RTRrm2dh4bbw2ZicIYzCHv3KG-lmLEqw9rr4c7oXbs7BXYZhSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بررسی آپدیت ژوئن ۲۰۲۵ گوگل: چه اتفاقی افتاد؟
✅
گوگل آپدیت اصلی رتبه ‌دهی خود را بین ۳۰ ژوئن تا ۱۷ ژوئیه ۲۰۲۵ منتشر کرده است. یک تغییر گسترده برای نمایش محتوای مرتبط‌تر و با کیفیت‌.
🔍
چه چیزی در این آپدیت متفاوت بود؟
طبق تحلیل‌ها، این آپدیت برخلاف موارد قبلی، ترکیبی از چند فناوری پیشرفته مثل:
✅
MUVERA (مدل‌های ارتقاء‌یافته بازیابی اطلاعات)
✅
GFM (مدل گراف-محور برای ارزیابی اعتبار محتوا)
رو در الگوریتم گنجانده تا گوگل بتونه:
🔸
محتواهای مفید و مبتنی بر تخصص رو بهتر تشخیص بده
🔸
ارتباط معنایی عمیق‌تری بین کوئری و محتوا برقرار کنه
🔸
تولیدکنندگان محتوا با درک عمیق‌تر از موضوع، ارتقاء پیدا کنن
📌
چی باید بدونی ؟
اگه افت داشتی، محتوای بی‌کیفیت یا قدیمی رو بررسی کن
الگوریتم روی «مفید بودن» و «رضایت کاربر» تمرکز کرده
توی سرچ کنسول دنبال نوسان ترافیک باش
واکنش سریع نکن! اول تحلیل کن بعد اقدام
@danialtaherifar</div>
<div class="tg-footer">👁️ 784 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pEsZCnRdSTcXpW50km8fp9zuFVtodB8IghodaBs5mV01BvsAMIEALT8MGnQVY_5kEfAo32TIWjnjz-uVGTDvTSj5gvhgh8bya47iM6corHAS1LPpZB_jqUkVZzuVXq2xNrDayyo4tLSJ9sKyUk2el0FG0KXm5oNWs-EaH1tFUzFdqspVtZ7K8uI_SA9waL0jF6Oyf4ksgsRnEJTXCl8W-u-AzJ-ZC9H3oUxo7tOyhlqyqnCVuiTCcQcBTTlMymY9nS_ye2Ua4iFFNiHGxa9OV87xI7Fc3s5mls-OFJL-LGfbNXrT4MkhdQ-We-uknSdU-amtzGYSfEp9NcylES-pCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/trNuHXW5zOoFOGkDdzLSkKy-Nc512IopxcwIwdSZ_52B5G80PjpG1n0g7sF7LWFXgjmLqvxnP9mOk60H4tvdyjaZ0xdHnlCn1Jho2SBLfckNiw0hSRIqf4iXcMwTIvg6oN7ZdGhL31YhQwR3n3N771gI-iQzaqCsWC7e0tVhRi-rtxqbA8eyYBWR6k0BbFdcePTbYBz2csE_N7NArTI8u8j6Kfx8lacNYD1vQwwX7OV6IFmQgeCo6dtwK3qIZuEtfVPHwmtrwJKFZ4BQ4Ve_KqwsPuxqKewVGM9RI5qsGJPaBIABWsCF-PVQ19Mt65bRTMuS5E-S8V1T_c3EcppKbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن بخش Insights  در سرچ کنسول گوگل
🔍
گوگل به ‌تازگی از نسخه جدید گزارش Insights در کنسول جستجوی گوگل رونمایی کرده است. این گزارش که پیش‌تر به‌صورت آزمایشی ارائه شده بود، اکنون به‌طور کامل در داشبورد اصلی GSC ادغام شده است.
❗️
چه اطلاعاتی در این گزارش ارائه می‌شود؟
1. عملکرد کلی سایت
2. پربازدیدترین صفحات
3. کلمات کلیدی برتر
4. دستاوردهای محتوایی
5. تاپ کشور های بازدید کننده
6. ترافیک سورس های مختلف
🕐
این ویژگی به ‌صورت تدریجی برای تمام کاربران در حال فعال ‌سازی است. اگر هنوز آن را در پنل خود نمی‌بینید، طی روزهای آینده دوباره بررسی کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 806 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">📌
چطور "اعتماد کاربران" روی رتبه سایت ‌ها اثر می‌گذاره؟
یه پتنت جدید از گوگل منتشر شده که داخلش یه نکته خیلی مهم گفته شده:
«
👀
گوگل داره رفتار واقعی کاربران رو دنبال می‌کنه تا بفهمه به کدوم سایت‌ها اعتماد دارن!»
یعنی چی؟ یعنی دیگه فقط محتوا و بک ‌لینک و سرعت سایت مهم نیست...
✅
اینکه کاربرا واقعاً به سایت شما اعتماد کنن و اون رو به بقیه پیشنهاد بدن، یه سیگنال رتبه‌بندی قدرتمنده!
💡
چطور کاربر، سئو رو تعیین می‌کنه؟
📌
گوگل از مفهومی به‌اسم Trust Signal استفاده می‌کنه، یعنی سیگنال اعتماد. این سیگنال‌ها از کجا میان؟ از رفتار واقعی کاربران توی نتایج جستجو! مثلاً:
🔸
روی کدوم سایت کلیک می‌کنن؟
🔸
چقدر زمان تو اون سایت می‌مونن؟
🔸
آیا اون سایتو به بقیه لینک یا پیشنهاد می‌دن؟
🛠
ایده خفن گوگل: دکمه اعتماد!
توی این پتنت اومده یه دکمه فرضی به اسم Trust Button طراحی شده که کاربر می‌تونه با زدن اون بگه:
👌
«من به این سایت برای فلان موضوع اعتماد دارم!»
گوگل این اعتمادها رو جمع می‌کنه و ازش یه "رتبه اعتماد" برای هر سایت می‌سازه.
سایت ‌هایی که بیشتر مورد اعتماد قرار بگیرن، در نتایج بالاتر می‌رن!
🔝
📈
یاد بگیر چطور اعتماد بسازی!
✅
محتواهای واقعی، کاربردی و انسانی بنویس
✅
کاری کن کاربر حس کنه که وقتش تو سایتت تلف نمی‌شه
✅
با جلب رضایت کاربر، اون رو به یه طرفدار وفادار تبدیل کن
✅
کاربران خوشحال = سیگنال اعتماد قوی = رشد رتبه در گوگل
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 994 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Na_to8uQsMR1YStv_4JH4EifPBnGlVk3Mh6FRl2g9WEbSzqMgwc--DXZ7acSndsvan5V6kTCgoVUtFD7HqO00g_F_P-m5DvsWI8ilFn8XdqoPYCIKkcBFbDyspwlMjyC08f_u39FbeTfFj9Z62UDknyKZdAojS5gg5Bj-sMZqN219gtH9C4ZfuBAdlGTXoaBaLycA1aW7pdmOWqxHDqYAaouhXqbaQQTMOx5e8OgskO53lnDGvfPnykSMhYlVkGJccZMDRWNO11kyokCinQxprnaB_8w7PVPcIhm_IQp2Xx-faii38z87JlhVGa66s3MhOcEeJsaZLGML5DsgNHrEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گوگل: ترجمه خودکار رو دیگه با robots.txt نبند!
📰
گوگل به ‌تازگی بخش‌هایی از مستندات robots.txt خود را حذف کرده که قبلاً توصیه می‌کردند برای جلوگیری از ایندکس صفحات ترجمه ‌شده خودکار، از robots.txt استفاده شود. این تغییر باعث هم‌خوانی بیشتر مستندات فنی گوگل با سیاست‌های مبارزه با اسپم شده است.
❓
چرا چنین توصیه‌ای قبلاً وجود داشت؟
هدف اولیه این بود که سایت‌ها بتوانند صفحات ترجمه‌شده (اغلب توسط ابزارهای اتوماتیک) را از دسترس ربات‌ها خارج کنند تا از ایندکس محتوای مشابه جلوگیری شود.
اما اکنون گوگل این راهنما را حذف کرده، چرا که ترجمه خودکار همیشه نشانه محتوای اسپم نیست و نباید به‌صورت پیش‌فرض توسط robots.txt بلاک شود.
گوگل حالا تاکید دارد که تضمین کیفیت ترجمه (کیفیت انسانی یا پس از ویرایش) اولویت دارد، نه محدودیت‌های فنی.
استفاده از متاتگ <meta name="robots" content="noindex"> برای کنترل ایندکس
یا استفاده از attribute هایی مانند notranslate برای جلوگیری از ترجمه خودکار و کاهش اشتباهات ایندکسینگ.
@danialtaherifar</div>
<div class="tg-footer">👁️ 930 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTsBw1oPOgJV0m9Md4SgfnFb3VuXNqU-pPlMTxpfNQrcA9NhJKItsqiIt33tj5RuE0URP6VICbAKW5tVgkn8s3zQ1LZXPpBGBTsqqQdHuBFBY6cD5pIkvV5oMMxmCzrwTVD5KOuIxW9c0mn5b6j1A-32c3cOy6np8wR3Uohcz0tHu0faFyOr47ejR3Rrbz2U42VnEwagDpcjruFlTCzxysX2oBUdyBoa3t0QZ9MV4AsrDxJJ6pziNGneulAAY9_BDH7Rrtd3GDQf2ZWC-z70iMFWmw6_JsfDEkLxuniwQgk8ZoNHz3_koyQMpWwUgJfgNqgV8KzOjMInBWe7JMHvWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 750 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n5Ojt-qU7Zod6q79Tw6a-lp8fi694sH7zxzArpOQuuvYSW_C-R0wDHuvLoThKqdY3hq06ShjoqtvlMvcAVx4BmJpjKswmtjcpMFEpJbXq_ZkrtV_Ah-9ZYxJyk86KaEn96HCk2xBmBa6oWOaAMvJM7SCjkLBjpdtEJoK3VSoZ3jqPJUF3D5dmOf3HeVd7KHiPDn5oll8_kZME0CglAEzaYWe-QE0iqjRmtan69FAglwdQcvg_zxSR1h5FhhWq4bPgL_EBrKMM08btWmmMQPHnsvTQscsQouyP-1vF7h3zPQbqG0AXRxBghrVsw61uc4aLjBQPCOODfmB8eEZ7TT0ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LSNM-JjAhjOybE1iX3EnS8MNzT3wVPdPaXdSaeLDPRzZqOtVQ9AKuDaNccyfD8JIZBK0kH-DLH3Fc7v9EncMCK_gux9_Pye4FrXZOQkQnrbalDepUTuDZHUDGBO1301_aJux_yAxV4HmPXGCd9u7d7hjV09gWgRsuC4cK4YbkG3v3D5mHza8tR9dKbLFprNssbdLlPVk-K9LUF_HGmjhfhH73tOyOtyB8MLqGsNq2g3JRYNMaxKvAOd8SqyjnhlLyZnIyl4MmbzFixSPSzL4asy4RgDWwvYZmzb7RfbNgnGk_eUQD9wYpAbJSEc4WmRJzZBQ7Cu_G6Ki0dYVxLKs5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📢
آپدیت جدید گوگل برای داده‌های ساختاریافته Event و Recipe
گوگل به ‌تازگی مستندات Structured Data یا همون داده‌های ساختاریافته رو برای دو بخش مهم یعنی رویداد (Event) و دستور پخت (Recipe) به‌روزرسانی کرده، تغییراتی که می‌تونه روی نمایش سایتت توی نتایج گوگل اثرگذار باشه.
👇
🔸
تغییرات در داده‌های ساختاریافته رویداد (Event)
✅
گوگل حالا به‌طور دقیق‌تر توضیح داده که چه نوع رویدادهایی می‌تونن در rich result بخش "Events" نمایش داده بشن.
❌
مهم‌ترین تغییر: ویژگی‌های مربوط به «رویدادهای آنلاین» دیگه پشتیبانی نمی‌شن!
📍
فقط رویدادهایی که در محل فیزیکی برگزار می‌شن و قابل رزرو برای عموم مردم هستن، شانس نمایش در نتایج Google Events رو دارن.
🔸
تغییرات در داده‌های ساختاریافته دستور پخت (Recipe)
📌
گوگل رسماً اعلام کرده که ویژگی image داخل داده‌ی ساختاریافته Recipe،
هیچ نقشی در انتخاب تصویر نهایی در نتایج جستجو نداره
😮
🔍
اگه میخوای تصویرت توی نتایج نمایش داده بشه، باید:
✔️
تصاویر با کیفیت، سبک و بهینه داشته باشی
✔️
باید alt-text و context مناسب برای تصویر قرار بدی
@danialtaherifar</div>
<div class="tg-footer">👁️ 761 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEq4NHAXv7y8fyrs_9xHpjuB0vrbffcqGfNyf8d9o-gXn1o_Jq0DascLZ7wQCQCXBZ35iYBZNJjDwCjIOuBjwAwMEAc2ab7HlXNcwRkrMD_5rs2GUfwp6aQdbkMM6Gy_hNHDN2Fytp0phoY8LCkAOE3rnBMDYNk5KRKdY9I5-ilbBMSA-FXKrUatU0rRr2i5W8-ibiNnKKjUc5hguK_tCM2vnJTbQbmTDvmMnXbK77dVgV51IjXVxQ3VzcanlxirZhTajU-tTnOLraHatut856M1dRdy1bAIEPI-SybiZofTfXJis6rpJGl-Kqgj5JFG6CzjrxWgN4fQ7TPWsEEdkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل سیگنال‌ های زمینه‌ای رو به نتایج جستجو اضافه می‌کنه
📌
‌ پتنت جدید گوگل نشون میده که قراره جستجوها خیلی دقیق‌تر و هوشمندتر بشن! دیگه فقط کلمات کلیدی مهم نیستن، گوگل حالا به شرایط و رفتار کاربر هم توجه می‌کنه!
📍
گوگل به موقعیت و زمان هم توجه می‌کنه!
فرض کن شب جمعه ساعت ۸، سرچ می‌کنی "پیتزا"
🍕
گوگل ممکنه بفهمه دنبال سفارش آنلاین پیتزا نزدیک خودتی، نه تاریخچه پیتزا!
😳
یا اگه بلیط یه فیلم رو خریدی و بعد اسمش رو سرچ کردی، احتمالاً دنبال تریلر یا نقدشی، نه یه بلیط دیگه!
🔁
بازنویسی هوشمند کوئری‌ها
🧠
گوگل با استفاده از داده‌های مختلف (مثل مکان، زمان، سابقه سرچ‌هات) می‌تونه کوئری‌ تو بهتر بفهمه و حتی یه نسخه دقیق‌تر ازش بسازه تا نتایج بهتری بهت بده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 675 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔍
جستجویی که می‌فروشد!
🤔
تا حالا فکر کردی چرا بعضی از سایت‌ ها با اینکه رتبه‌ی خوبی تو گوگل دارن، باز هم فروششون تعریفی نداره؟ یا برعکس، یه سایت شاید رتبه اول نباشه ولی همیشه مشتری داره!
🧠
واقعیت اینه که رتبه بالا فقط یه تکه از پازل موفقیت در سئوئه!
📌
این 4 تا نکته بهت کمک میکنه که بیشتر بفروشی
:
👇
1️⃣
هدف جستجوگر رو بشناس!
فقط به کلمات کلیدی نگاه نکن، بفهم چرا کاربر اون عبارت رو سرچ کرده. مثلا "کفش مردانه" یه جستجوی کلیه ولی "خرید کفش مردانه راحتی" یعنی آمادگی برای خرید!
👟
🛒
2️⃣
محتوایی بساز که بفروشه!
یعنی چی؟ یعنی محتوا باید مخاطب رو به قدم بعدی هدایت کنه:
ثبت‌ نام
📩
، خرید
🛍
، یا تماس
📞
. نه اینکه فقط اطلاعات بده و ول کنه بره!
3️⃣
داده‌ها رو جدی بگیر!
با Google Analytics و ابزارهای سئو بررسی کن که کدوم صفحات بیشتر تبدیل دارن. شاید یه مقاله تو رتبه ۳ باشه ولی دو برابر بیشتر بفروشه از رتبه ۱!
4️⃣
تجربه کاربری = کلید تبدیل
!
🔑
سرعت سایت، طراحی زیبا، دکمه‌های فراخوان (CTA) واضح… همه اینا کمک می‌کنن بازدیدکننده‌ها تبدیل به مشتری بشن.
🧭
🎯
فرمول طلایی موفقیت در سئو:
رتبه خوب + محتوای هدفمند + بهینه‌سازی تبدیل = فروش بیشتر
💸
🗣
پس دفعه بعدی که داشتی رتبه‌ات رو چک می‌کردی، این سؤال رو هم بپرس:
"این رتبه داره برام پول می‌سازه یا فقط دلمو خوش کرده؟"
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 817 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔍
نگاهی به سیستم‌ های رتبه‌ بندی گوگل
👇
این اطلاعات نگاهی نادر به نحوه ارزیابی کیفیت صفحات، سیگنال‌ های محبوبیت و نقش داده‌های مرورگر Chrome در رتبه‌ بندی نتایج جستجو ارائه می‌دهد.
🛠
سیگنال‌ های ABC: پایه‌های رتبه‌بندی
گوگل از سه نوع سیگنال اصلی برای تعیین ارتباط محتوا با جستجوی کاربر استفاده می‌کند:
A – Anchors
: لینک‌هایی که به صفحه هدف اشاره دارند.
B – Body
: وجود کلمات کلیدی مرتبط در متن صفحه.
C – Clicks
: رفتار کاربر، مانند مدت زمانی که در صفحه می‌ماند قبل از بازگشت به نتایج جستجو.
🔹
این سیگنال‌ها به صورت دستی تنظیم می‌شوند تا الگوریتم‌های رتبه‌بندی قابل فهم و قابل کنترل باقی بمانند.
📄
کیفیت صفحه: معیاری ثابت و مستقل از جستجو
کیفیت یک صفحه، که نشان‌دهنده میزان اعتماد و اعتبار آن است، به طور کلی مستقل از جستجوی خاصی است. این معیار به صورت ایستا در نظر گرفته می‌شود و برای همه جستجوهای مرتبط اعمال می‌شود. با این حال، در برخی موارد، اطلاعات مرتبط با جستجو نیز می‌تواند در ارزیابی کیفیت صفحه تأثیرگذار باشد.
🤖
سیستم eDeepRank: استفاده از مدل‌ های زبانی بزرگ
سیستم eDeepRank از مدل‌های زبانی بزرگ مانند BERT برای تحلیل محتوا استفاده می‌کند. هدف این سیستم، تجزیه سیگنال‌های پیچیده به اجزای قابل فهم‌تر است تا مهندسان گوگل بتوانند دلایل رتبه‌بندی صفحات را بهتر درک کنند.
🔍
سیگنال محبوبیت مبتنی بر داده‌های Chrome
یکی از سیگنال‌های رتبه‌بندی، که نام آن در اسناد محرمانه باقی مانده، از داده‌های مرورگر Chrome برای ارزیابی محبوبیت صفحات استفاده می‌کند. اگرچه جزئیات این سیگنال مشخص نیست، اما وجود آن نشان می‌دهد که رفتار کاربران در مرورگر می‌تواند بر رتبه‌بندی نتایج جستجو تأثیرگذار باشد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 824 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/danialtaherifar/883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
پتنت Site Quality Score چیه؟
🧠
پتنت شماره
US9031929B1
یکی از روش‌های گوگل برای سنجش کیفیت کلی یک سایت در نتایج جستجوئه!
💡
تو این پتنت، گوگل با استفاده از نسبت بین:
🔍
تعداد جستجوهایی که به یه سایت ختم میشن (مثلاً سرچ "ویکی پدیا")
👆
و تعداد کلیک‌هایی که روی اون سایت تو نتایج زده میشه، یک امتیاز کیفیت سایت (Site Quality Score) محاسبه می‌کنه!
✅
نتیجه ؟
افزایش جستجوی برند + نرخ کلیک بالا = امتیاز کیفیت بالاتر = رتبه بهتر تو گوگل!
@danialtaherifar</div>
<div class="tg-footer">👁️ 722 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRvH0ueHID_IeWaX74HZLN7ncooyjOhPN9YneabxKekfo4a8_mHFnJ8RuA5qRIHTiBg1TSUF4-OC8HAucebOIB5oTkJsK4DFFoMuk99MhAWn4mewX9sR5MsdH3vYg0xvUW-qCwjwspuJ020Ce2BRE-AEMB3niyZIPeLKWLYqUec8BkayCLJ8YT2W9GxvXnQOWF67gstuf53QZwRY-EhFiWuftritGLbHjfGB62OL2LdNJZKH1B4yFIt6z9knv7Zv2WOPplvltf33yHRSOCfr7gk7Ssmxm9mfv93RlT7v2SaJd3GsdE7A5yO0h_eP-mncUJxlMPE1nufc7Vyhzs4oZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رتبه‌ی یکسان برای همه لینک‌ها در بخش AI گوگل
📈
گوگل بالاخره تایید کرد که لینک‌هایی که توی بخش پاسخ هوشمند (همون AI Overview) در نتایج جستجو نمایش داده می‌شن، همگی با هم یک موقعیت یا رتبه در کنسول جستجو ثبت می‌شن!
🤔
یعنی چی؟
یعنی اگه توی یه AI Overview چند تا لینک از سایت‌های مختلف نشون داده بشه، همشون با هم یک Position حساب می‌شن. فرقی نمی‌کنه لینک اول باشه یا سوم؛ گوگل بهشون یه رتبه‌ی مشترک می‌ده.
🔍
چرا این مهمه؟
📉
ممکنه باعث بشه نرخ کلیک (CTR) سایتت بیاد پایین! چون:
خیلی از کاربرا جوابشون رو همون توی AI Overview می‌گیرن،
و دیگه روی لینک‌ها کلیک نمی‌کنن!
😕
📌
گوگل چی میگه؟
الان هیچ دیتای جداگونه‌ای برای AI Overview توی Search Console نشون نمیدن.
همه لینک‌ها با همدیگه یه رتبه دارن.
فعلاً هم برنامه‌ای برای تغییرش ندارن
😬
@danialtaherifar</div>
<div class="tg-footer">👁️ 823 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOONmVaJJumhrJ_zEszLxhB0l2g8fxcxC2f_4wq6hillc7Jjas56CJNkdiN6TwqzSIvnpT8LbKihOryqiGBIN6xOFxRsq7y5KjvXcZuDogSFZnFGpHL8xPBIwm1AFTY6J0kzc1M8YcRlncNP7dhCMQHq7gZ-wgpdo4Zy7WjHhZJE5gXSy4q6MJNEkcmLsExoEQNkzxQXdrDFTSlwrwoAdM2eNx_en9qDN2-LoYHPlkTIMVvfdWHhwMIRMgU7BDmMpRT4OGsAtQ6ysRtuQTfyMeKy6lZlxMuHpNuf_6Q_WFgv2aj7i50b2xXWjKk7-TxdcdTdP619_bESmVEULaQEdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل: Navboost یک سیستم یادگیری ماشین نیست!
در تازه‌ترین افشاگری‌ها پیرامون سیستم‌های رتبه‌بندی گوگل، یک نکته بسیار مهم روشن شد:
سیستمی به نام Navboost که تصور می‌شد یک الگوریتم هوشمند باشد، در واقع هیچ ربطی به یادگیری ماشین (Machine Learning) ندارد!
🔍
اما Navboost دقیقاً چیه؟
👨‍💻
به گفته‌ی دکتر اریک لِهمن، از مهندسان سابق گوگل:
بیشتر شبیه به یک جدول عظیم از داده‌های کلیکی کاربران برای کوئری‌های مختلفه؛ اطلاعاتی مثل تعداد کلیک‌ها، امتیازات و چند فاکتور ساده‌ی دیگه.»
🔸
یعنی به‌جای اینکه تصمیمات بر اساس هوش مصنوعی گرفته بشن، این سیستم صرفاً داده‌هایی مثل "چه کسی روی چه لینکی کلیک کرده" رو جمع‌آوری و نگهداری می‌کنه.
🧠
سیگنال‌ های رتبه‌بندی؛ دستی نه هوشمند!
🧩
بسیاری از سیگنال‌هایی که در رتبه‌بندی نتایج جستجوی گوگل تأثیر دارن، به‌صورت دستی توسط مهندسان تنظیم شده‌اند.
گوگل از توابع ریاضی مثل sigmoid و مقادیر آستانه برای ساخت این سیگنال‌ها استفاده می‌کنه؛ نه از مدل‌های پیچیده‌ی هوش مصنوعی (جز در مواردی مثل RankBrain و DeepRank).
@danialtaherifar</div>
<div class="tg-footer">👁️ 607 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGdeN_LlgR__FUpKjX1mVRAvvQ_48xXvQd-80I1Mn-AHTcLgo3J4TOQnQJnf8V_2EGR1MGt3786fnGKPi0U4-80PX6nP5RlUF0mlbJG7jSaA5XcIM85M0oGRFPH_nBDabXUGVMFzFD73KDJukchwlXinmx3jt2pgsND8o65Ns8hRy0N0tJ-fRRiXjpuiG0KWXBE7FMXf0gq00-tsRWFufbomIfjCtdfQ7V5erxLBhh8PaMtRma7y3IhzOKK_OkK3DhBt47rUaxZvGgLFug9KxyqA6fhv91CPLr00_eraOInyiIzxLD6QePdNGCiC7195Ka5n6ruNPzJoK_mjqFlu4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
چطور توی Google Discover بیشتر دیده بشیم؟
🔹
۱. محتوای با کیفیت بنویس
📌
فقط نوشتن کلمات کلیدی کافی نیست، محتوات باید واقعا مفید، مرتبط و جذاب باشه تا گوگل بهش توجه کنه.
🔹
۲. از عکس‌های باکیفیت استفاده کن
🖼
عکس با عرض ۱۲۰۰ پیکسل یا بیشتر؟ عالیه! چون باعث میشه کارت تو Discover بهتر دیده بشه و نرخ کلیکت بیشتر شه.
🔹
۳. موبایل فرندلی باش
📱
بیشتر کاربران از موبایل استفاده می‌کنن. پس سایتت باید سبک، سریع و بدون مشکل تو گوشی لود بشه.
🔹
۴. داده‌های ساختاریافته فراموش نشه
🧩
با استفاده از
Schema.org
به گوگل کمک کن بفهمه محتوات در مورد چیه. همین یک کار ساده باعث رشد دیده‌شدن میشه.
🔹
۵. حتما E-E-A-T رو جدی بگیر
🏅
هر چی اعتبار سایت و نویسنده‌ت بیشتر باشه، گوگل بیشتر بهت بها میده.
🔹
۶. سراغ ترندها برو
📈
محتواهای داغ و به‌روز توی گوگل دیسکاور شانس بیشتری دارن. اگه خبری یا موضوع جدیدی هست، سریع پوشش بده!
اگه می‌خوای تو Google Discover بدرخشی
💥
باید محتوای فوق‌ العاده جذاب و تجربه کاربری عالی داشته باشی.
@danialtaherifar</div>
<div class="tg-footer">👁️ 700 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔎
چارچوب Triple P در دنیای جست‌وجوی هوش مصنوعی؛ حضور، ادراک و عملکرد برندها
🌐
✨
📌
در دنیای دیجیتال امروز، موتورهای جست‌وجو با کمک هوش مصنوعی به سطحی رسیده‌اند که فقط نمایش لینک نیستند، بلکه تجربه‌ای هوشمندانه و تعاملی را برای کاربر خلق می‌کنند. حالا دیگه وقتشه برندها با رویکرد جدیدی به سئو و دیده‌شدن نگاه کنن!
👀
اینجاست که چارچوب Triple P وارد می‌شه:
✅
1. Presence (حضور)
🔹
آیا برندت تو نتایج جست‌وجوی هوش مصنوعی حضور داره؟
🔹
تو مدل‌های جدید AI مثل Gemini یا ChatGPT، دیده می‌شی یا نه؟
📍
حضور برندت تو پاسخ‌های تعاملی خیلی مهم‌تر از قبل شده. دیگه فقط لینک اول گوگل کافی نیست!
🧠
2. Perception (ادراک برند)
🔹
چطور مخاطب وقتی اسم برندتو تو پاسخ‌های AI می‌شنوه، نسبت بهش حس پیدا می‌کنه؟
🔹
آیا برندت قابل‌اعتماد، معتبر و پاسخ‌گو جلوه می‌کنه؟
📢
هوش مصنوعی بر اساس داده‌هایی که از برندت داره، درباره‌ات نظر می‌ده! پس محتوای درست و دقیق تولید کن.
🚀
3. Performance (عملکرد)
🔹
آیا حضور و تصویر ذهنی برندت در نهایت باعث کلیک، خرید یا تعامل می‌شه؟
🔹
چقدر از پاسخ‌های AI به سود واقعی برندت منجر می‌شن؟
📊
حالا دیگه اندازه‌گیری عملکرد تو جست‌وجوی AI فقط به کلیک محدود نیست، باید ببینی خروجی چیه!
✨
چرا چارچوب Triple P مهمه؟
چون در عصر هوش مصنوعی، برندهایی که فقط به سئو کلاسیک تکیه می‌کنن، عقب می‌مونن. برندهایی برنده‌ن که در جست‌وجوهای هوشمند هم دیده بشن، درست فهمیده بشن و نتیجه بگیرن!
📣
اگه هنوز به‌روزرسانی استراتژی سئوت رو با تمرکز روی AI Search شروع نکردی، الآن بهترین زمانشه!
@danialtaherifar</div>
<div class="tg-footer">👁️ 644 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XvDcV1fuHBKuCFE9IAScVMT8DNUJW-2pixEGcILJgD9-kWsQiSZsXqKxL9iiBVLDquEYMU71SSlM37XNA-OhhUtX5ZkSTG9a00Xnde-w7xwJ6hD42bn9ref9AC_8WOLQFvAwiBdBt7Yxdy8-AXlwOpOxmlIYjfz6CHhjDU9XtzOQoCMFK5FjG1pmxbSt8EbuhO-ZtOsFk4-3sjBZTtXVn2vK-28HVu6mY_fhGezB7WONzyPXInpHosNAwPzeupzAA-9RV3cjFCL-7Yh7yHEMQaSeDycXmaYoTEekfz444P7r5v5Qg3RoFA4fF1AcSrZ9CTB4xvGJUIUvGp825Vt7oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XfeZ2MY_1P4FmtFmMSjtkiu2fVbDim9HoLD1PY9TXfIG-6oXnecLcyRmG5yFfpNs87UAD7kPLs0rN3OdjDJFxyIWmTnH8JF2Urg0-UtyHvkwfuOd339liwfNsSSMt88lLRAvb8BY44KmlOM_wEkPvCIRmha_BwRnm5imvngXaHdfRpA7RbxjBsG_v0MaD_pEjCHwNT7hTtCSzwVdHHFk7kV3RLe9CXhQvssdd7WJ8AS38zMk_AdVpDxQkJt1Ddb35Lo8rhqWbI5wOBBySJFIC857arsnuIwgTwDHWgtA2Wz_1iBBAz1O7p39pXjsgwOnLAEHj6hRkCHFemXusHsd5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ALM6IhrOB54ITn9xP2iek9_1PmZ0EeTqq-XuEyXqa80CufwDsLsE9LhHkVpC8h3vjp9k4qUi8UBVN5aY_RDnlBW4TmiGCFETPkXRKHEAeFufs4z1CD2Eg_RlEA2T37WxaWkd8fF_c8O2Dar-OYd-sOV4cAQ4t9EeRQeVXDz-_GyLokU84gzhBVNgWI61N3DDJ-ejgtHGqYBQlWXkP0y4odaa3ES1NwcDnjXshMsofWxBNrfPJzkwU9-5AsyTNOtZxp2gbfEnwXeOKY5o1aKvPTzF1G79AmGHdtH5TEAoJnZQSPx9Rb8F9CcKJb_Yfhg3BXCvapSAgLx09k_RC1gC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GMXRpcGrNmvsjr0U1-Lw8xqYiy8swrFO2q2WHinxeho3V2zvEPtgl57maAnfxS1-n_aq4SpNpV2zhfbmYBjBCu_j_HGiIWILh6-DJZM8g5a35OXby0-X-CxethxNBSvVlLj7bscfgGYP2zCTpRK2viB5m0lp639AJDt1uLHrJpdetPPd5VUrp-RDjIXl1KT8Jl1jMBSMeEeF4w-HcyrzVqdJepBaerM4bCgWxFG08ChXSaBIq6rczz2JS1Q254Ti8YUomZFQhHoIvqe3t5UfWJaMZOI0zHbI7uUaSRbeamGcsltUix1H7Lkj3YNCFVgO3liFRaoBAnylWlmE0Fm8Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MjgHg6ZmmSA28RNq0Wtr0LVpXEwJ8yJ_YnBK6HHizAU9waK9PUIQEHYFl4v8eAs6UthnjAMQuKo2y5BQLDmJpz93uRYOr6WQoLuTC778Nt8m21627ox6Z4gZwiosM1Cbdr4-gmfqBq9zXHiipm3_oJFFv6WmImZjfkvRwSX-ALK3ZVosA_b1xdF_6B4HmjmKcGoYpJ88hUuB19OTsqjcl1N6j9IEUdXZ4g5wdICRPdZ60WhSDMVIdCzLoijO9zG--9lD38bnQZUtbIsAxuk8Q2Ocgo5NfRTt6YPmS7PuMAQ5AxIO1YOORzMystTPESfJRvr2_2QUlxozOtwYmtmFRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 788 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsnZ2pQU3G2uMKBEA7noykNwNBt9c_TW8xp5AlF7DHcR_LaRlZvCkdM7srCLcn0YX4X2ptiWjpyOQ0Eoj5htk8Pw0zYIPeISNI0Z4aDGdV8TAkT6o-YZPs_BbIo_k23-uCLlhdqjXKJ2rwMkauSbnSry2AAiG1Vq-Gk3rcJJUv8jv8IOOR2heKszm6qzfxoUsa-JRT7OOGT0xGga0izdCAyiM6dU7UeS8W9vx6z6bhFUJo7nUrZg5LMfkrrUfJ9Ohf0J96pWon1u1p5cGn9xG5HYAIry9L1MUAM6e3yV3yJYpB8RRfCST8ftD50zCgtMT8MSf_Vj8JAMPlJodGaUOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:
1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.
2. تعداد جستجوهای نام برندهای رقیب را نیز جمع‌آوری کنید.
3. مجموع جستجوهای برند خود را بر مجموع کل جستجوهای برندها تقسیم کرده و در 100 ضرب کنید.
🎯
مثال: اگر برند شما ۲۰٬۰۰۰ جستجو و سه رقیب اصلی به ترتیب ۱۵٬۰۰۰، ۱۰٬۰۰۰ و ۵٬۰۰۰ جستجو داشته باشند، سهم جستجوی شما:
20,000 ÷ (20,000 + 15,000 + 10,000 + 5,000) × 100 = 40%
💡
چرا باید بهش اهمیت بدیم؟
🧠
بهت کمک می‌کنه بفهمی جایگاه برندت تو ذهن مخاطبا کجاست.
📈
یه شاخص عالی برای پیش‌ بینی رشد یا افت بازار در آینده‌ است.
🔧
می‌تونی استراتژی‌های سئوت رو بهینه‌تر کنی و رقبا رو پشت سر بذاری!
@danialtaherifar</div>
<div class="tg-footer">👁️ 583 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blkyoAmb5z0KgsCREuSnrNSljbIqDhiMju51se3Jgk4kRb_1GVuqE0RIAJCNXKgMHqmvh7iSUHntgQnb7a3JhPoZ0Ue39DqS4ddVfl-As0lUkRnpsWN6ATx1BWON83N7ARvTOq5i_LeAGGiV0tpIEgV53FSUnZ2glzBj8fQaaD80800oiYezye38LqMQRHgtqHWIRa59NelTvMo-r3Jg8d26Lbvcstp9lkKeJx8haXjSGQ-zKON3gBCw2Yc9J0yKYNKR-IrxFiZBLcoKk66a85wO5eaq-PjTULmoyi9oYfjmQNLUzLN13gI57WD2bJp0u-U5wqhc-9sezGJ50hDsAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نحوه استفاده از پارامترهای زبان و کشور در جستجوی گوگل
اگر به دنبال راهی هستید تا نتایج جستجوی گوگل را بر اساس زبان یا کشور خاصی مشاهده کنید (مثلاً فقط نتایج فارسی برای ایران)، گوگل راهکاری ساده اما بسیار کاربردی در اختیارتان گذاشته است. کافی‌ست از دو پارامتر ویژه در انتهای لینک جستجو استفاده کنید.
🛠
تنظیم زبان و کشور در URL جستجو
&hl=کد_زبان → مشخص‌کننده زبان رابط کاربری (مثال: &hl=fa برای زبان فارسی)
&gl=کد_کشور → مشخص‌کننده کشور هدف (مثال: &gl=IR برای ایران)
💡
مثال کاربردی:
https://www.google.com/search?q=دانلود+فیلم&hl=fa&gl=IR
🎯
مزایای استفاده از این قابلیت
✔️
مناسب برای تحلیل سئو بین‌المللی و بررسی نتایج در کشورهای مختلف
✔️
مشاهده دقیق‌تر نتایج کاربران در زبان‌ها و مناطق متفاوت
✔️
قابل استفاده برای تولیدکنندگان محتوا، بازاریابان و متخصصان دیجیتال مارکتینگ
✔️
بدون نیاز به تغییر تنظیمات مرورگر یا حساب کاربری گوگل
@danialtaherifar</div>
<div class="tg-footer">👁️ 595 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-Hoc3VA58rONl8VRx2RNYcCDwsE-sZIg1DYpNUZkRbr2Zq-lbjOZwDDSgVCI43kFR_5wEnU2dRnjPeFOCYNJW4n9vvIsyWCcxCtrid68_fKq8EtCDrQ5MKTAT0nOnBoo_VSYhUzWsHTDWxdLabsm8fHNoEKtKxNG13YPmDIyGmjtlg2sOC4dPKXt1l8jHX2hq4DYOTdOigwLGeN6bxXWcdkbvLlF8kZ9jYrgBseXuku1U2mLbb8S6QufW9n4c8W0jmVrlh2D_ycFq7VX4pmlHwcEMMF3qJZF10_siABRPf1pEGrp8jHrspZ_MlzbFn8kLmot1A6-LIUO-Iceard6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل علیه محتوای فیک E-E-A-T وارد عمل شد!
گوگل توی آخرین آپدیت دستورالعمل‌های ارزیاب‌هاش، تمرکز ویژه‌ای روی مقابله با محتوای تقلبی و مخصوصاً محتوایی که به‌دروغ نشون میده تجربه یا تخصص داره (E-E-A-T) گذاشته!
🧠
چه چیزایی تغییر کرده؟
🔹
محتوای دارای تجربه واقعی اولویت داره
🔹
اعتماد مهم‌ترین عامل برای رتبه‌بندیه
🔹
تولید محتوا با هوش مصنوعی بدون بررسی انسانی = خطر سقوط توی سرچ!
📌
نکته مهم برای سئوکارها و نویسنده‌ها:
اگر تجربه واقعی، منابع معتبر و شفافیت نداشته باشی، گوگل دیگه باهات شوخی نداره!
😅
@danialtaherifar</div>
<div class="tg-footer">👁️ 704 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMpgCkfeSWgTNdf0LqlA6Lx3FhPWBQwlW4Iyr5hO6lQawn9hb7gGfA-0p64ljtzvqGoC5SELfUClqW1BBaFCDapui06M7yyIXwE1oeB9rIWjMX-pmr1KnAejVb0VJsE9G9IcQ35u0dxsdntEvKx_5PQf_npNRsNa9Ng5lfT4zOq8kLk3C-N6sU31kRmSCVDqd9xn5bDhmyt0swr6iIinzgASO6f9bdToDfvRvGoLo04_H2JEDOEoxAALph2esCcPEAfo1DBIjp8EjayM7vCgWSmLccrbN8ebw2w4ael4dLKdKIh2FMM8c2cTHbiZ2WFGMcKfchKX4J4M3LLCttCA5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
رندرینگ سمت سرور در مقابل سمت کلاینت: توصیه‌ های گوگل
👨‍💻
رندرینگ سمت سرور (SSR) چیست؟
در SSR، محتوای صفحات وب در سرور تولید شده و به‌صورت HTML کامل به مرورگر ارسال می‌شود. این روش به موتورهای جستجو امکان می‌دهد تا محتوا را به‌راحتی ایندکس کنند، زیرا نیازی به اجرای جاوااسکریپت در مرورگر نیست.
🧑‍💻
رندرینگ سمت کلاینت (CSR) چیست؟
در CSR، مرورگر ابتدا یک HTML ساده دریافت می‌کند و سپس با اجرای جاوااسکریپت، محتوا را تولید و نمایش می‌دهد. این روش برای برنامه‌های وب تعاملی مناسب است، اما ممکن است موتورهای جستجو در ایندکس کردن محتوا با مشکل مواجه شوند.
📈
توصیه‌های گوگل:
گوگل اعلام کرده است که هیچ مزیت خاصی از نظر سئو برای SSR یا CSR وجود ندارد. مهم‌ترین نکته این است که محتوای سایت به‌گونه‌ای باشد که موتورهای جستجو بتوانند آن را به‌درستی ایندکس کنند.
🔹
اگر سئو برای شما اولویت دارد، SSR می‌تواند گزینه مناسبی باشد.
🔹
اگر به دنبال تجربه کاربری تعاملی هستید، CSR را در نظر بگیرید.
🔹
در برخی موارد، ترکیبی از هر دو روش (رندرینگ ترکیبی) می‌تواند بهترین نتیجه را ارائه دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 648 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MF1CXvmCWDN1PcaDRSNxqLOkrIprsgfPvczaZtU5pvBNv2-VHiCyCEwoIQIQyvDCeFvABp6qhqzererdbEppBRKOg77erZAqEqNehVbIO-eCOdif_LunK1-puwh98H8E4ja2klwnByCOHBASaqao5QdR-1dN02yPMdJtqPzOzL3_gKyw0gSgdEE6yS3EgqlC6QpH-wDHEdnR8bO9NVPQPGANH0QhPFs0XfiNHRFMUc_214hofSjWeSjzjIQKcqehWvHa22Jbxrk9JC3zf8n0PeFxqjDoTVorFZSOatETsOP4BI2AF7SwaFpGEl_QQ8blBqnCflHN53lLKtQ36WVedQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
ابزار NotebookLM گوگل حالا در بیش از ۵۰ زبان در دسترس است!
📢
گوگل قابلیت «خلاصه‌های صوتی» (Audio Overviews) را در ابزار هوش مصنوعی NotebookLM گسترش داده و اکنون این ویژگی در بیش از ۵۰ زبان مختلف، از جمله فارسی، اسپانیایی، پرتغالی، فرانسوی، هندی، ترکی، کره‌ای و چینی، در دسترس کاربران است. ​
🎙
این ابزار با تبدیل منابع متنی به گفتگوهای صوتی شبیه به پادکست، به کاربران امکان می‌دهد تا اطلاعات را به‌صورت شنیداری و تعاملی دریافت کنند. با استفاده از پشتیبانی صوتی بومی Gemini، کاربران می‌توانند خلاصه‌های صوتی را به زبان دلخواه خود بشنوند.​
🌐
برای تغییر زبان خروجی، کافی است به تنظیمات NotebookLM رفته و زبان مورد نظر را انتخاب کنید. این قابلیت از سال گذشته در بیش از ۲۰۰ کشور راه‌اندازی شده و گوگل قصد دارد با دریافت بازخورد کاربران، آن را بهبود بخشد.​
✅
همچنین، گوگل این ویژگی را به چت‌بات Gemini و Google Docs نیز اضافه کرده است، تا کاربران بتوانند انواع بیشتری از محتوای نوشتاری را به صورت صوتی دریافت کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 717 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwCstqRo8US1_BmTGdfqH_ExSvL25L_s4XMG5mSD6MJT5nrny4tsmqukhW22LfSVtxMDMGvrTKR1Lf8ktf9ml_AifQe8lGcEmoiI1aox-ODR55C6yk6fH455Uho45jb1OKpa39tg1qoYD3Q25KxvevMcY3uCbAahFsmmJBqxvO4oIwSy1j4S8QHAAOTwXH-aAIGjZkrbDQFCtvNuqUwknIx0hgMUu4gxcvkyGbFt3wkLjNKNbW6Oy0v_LzGxVEo7Fi0ko6-GRChwMetJiWnoXluEDoo-pMRzBoLwEzrhuaVxuqksuJDXihhGNu8z0TiDRjwxCL8BtZWw5D1Jij78cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
جان مولر: آپدیت تاریخ XML Sitemap تأثیری روی سئو ندارد !
🗣
جان مولر، تحلیل‌گر ارشد گوگل، اخیراً تأکید کرده که تغییر خودکار تاریخ‌ها در نقشه‌ سایت XML (تگ <lastmod>) بدون تغییر واقعی در محتوا، نه تنها به بهبود سئو کمک نمی‌کند، بلکه ممکن است فرآیند شناسایی به‌روزرسانی‌های واقعی را برای گوگل دشوارتر کند.​
❌
کارهایی که نباید انجام بدید:
فقط تاریخ‌ها رو آپدیت نکنید اگه محتوا تغییر نکرده.
ابزارهایی که اتوماتیک تاریخ‌ها رو عوض می‌کنن، فایده‌ای ندارن.
گوگل می‌فهمه که محتوا واقعاً تغییر نکرده!
✅
چی کار کنیم؟
فقط وقتی که محتوا، لینک‌ها یا دیتاهای صفحه تغییر کردن، تاریخ رو عوض کنید.
نقشه سایت رو با تغییرات واقعی همگام کنید، نه مصنوعی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 615 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ua1GuTar2NRmldiCUbTNeitBrGP9hTXScDqxhYoj8MhudcvG9nnW6PWVkuNyBaTqHvpZvzCScL83zz3l-JAfwjofDuxx-RlKqbDXPAdR4j97MsIlwuKWmBw6s0RbLleTyfIXyKTePo6QiIcKs_vJ3tldl0GD6oMy2AU4xtj3tR15wCCTrX7VZDTUC_eLJACASkIdt2EFQPTSjuq8dLUWStYKL-QNAtCRidGouaTlArvn58sxQuAVqo_Y2RsQ3gCOOz4YgoxAJM4SETH3SwlZ8XEMypuCHzHipC9gBdQzSJT5lAOYaOX5YI5Kqf1zN67qlJ1rYf68EtSweY_HpYdRQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل مستندات Google-Extended را آپدیت کرد: کنترل بیشتر روی داده‌های آموزش AI!
🌐
این به‌روزرسانی به ناشران کمک می‌کنه دقیق‌تر تصمیم بگیرن که آیا داده‌های سایت‌شون برای آموزش مدل‌های آینده Gemini و Vertex AI استفاده بشه یا نه.
✍️
گوگل اکستندر یک user agent است که به وب‌سایت‌ها امکان می‌دهد تعیین کنند آیا محتوای‌شان می‌تواند برای آموزش مدل‌های Gemini و Vertex AI استفاده شود یا خیر.
با مسدود کردن این agent از طریق فایل robots.txt می‌توان جلوی استفاده از داده‌ها را گرفت.
🔹
نکته مهم: Google-Extended تاثیری روی رتبه‌بندی جستجو یا ایندکس شدن سایت شما نداره.
@danialtaherifar</div>
<div class="tg-footer">👁️ 641 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEYXjoaKVdGx-rqR4NkmoawyNMGWzf-H8vPmWsJGzSBiHmCuV4E44lRHrK_b24o2E798a7SgbKyY6o8VFWGS6rYyQK618JE7tol8OAHgwn1ATu6lasUhSp0d5gVQo6hRdwXs2pdnpgTHsovz1acykEKOPfj3QbCRseg97Cr4Mo2Byw8yy09TnYRvImdxke0MB2oPh_CtxdpSFVFMUt6NR4yqi5HuBQpkxcRvsOXYnW7Gp7UYcVDdmKTaE5hPxp1jkkf-3-5-EEk5BpG3AXtsAJ7Hd3qPKmyr6RTzfcHz9-GKNrhzIMSxrovAL3hGefAbQ_bw5V2N_aO-KtajKCYauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n1o2xsir-G31VfS6rF3qRAr40fCA8ah9kZ12Bk_rKC1VlZXVKRTy4LNq60HcbX3oyLvmyZ3xxQ4CyI4rZZ-wCzt9qjhkkQD3Trjh03ZWOiRa-PhcXwD0LoXRdWxbNu7diMtURSgW7vtHwETcp6y3Xs4hDPKinprnphf-tljfNBQcbufckRNI0ydfd98pesbhyWfSwnYPYKYy4ne4lDbi3o6yv7j2hfYCIytrQ6bdXwUg3agrueKiRy3IbMnEaG40UiqnJgM0sUw3RcpdgCas7u76SCklaYDKKT6t-01vIm2CeLv6ezXAuxC6ztNYlJpp5y3CuarHjGrHEz67hjMHIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
نوسانات شدید رتبه‌ بندی گوگل در چند روز گذشته !
📈
طبق گزارش‌های جدید، دوباره شاهد نوسانات چشمگیر رتبه‌بندی در نتایج جستجوی گوگل بودیم! این تغییرات درست بعد از نوسانات هفته‌ی قبل (۲۲ و ۲۳ آوریل) رخ داد و باعث شد خیلی از وب‌سایت‌ها افزایش یا افت چشمگیری در ترافیکشون تجربه کنن.
😵‍💫
🔍
ابزارهای مختلف مثل Semrush، MozCast و SimilarWeb هم این جهش ناگهانی رو تایید کردن. حتی بعضی از مدیران سایت‌ها از کاهش ۷۰٪ بازدیدکنندگانشون خبر دادن!
😬
👀
در حالی که به‌طور معمول هر هفته نوسانات کوچیکی داریم، این بار دو بار در یک هفته چنین شدت نوسانی خیلی غیرمعمول بوده.
💬
بعضی‌ها در انجمن‌های تخصصی گفتن که سایت‌هاشون از گوگل دیسکاور حذف شدن یا ترافیکشون افت وحشتناکی داشته؛ در مقابل بعضی‌ها هم رشد خوبی تجربه کردن.
📅
نکته مهم: هنوز خبری از آپدیت رسمی جدید گوگل در سال ۲۰۲۵ نیست (به غیر از آپدیت اصلی مارچ ۲۰۲۵).
📌
اگر سایتتون تغییرات عجیبی داشته، بدونید تنها نیستید! این نوسانات بخشی از بازی گوگله.
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 667 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVT_NUpQQEyFw3b9gHMmnoAvUkL-2g9CI2GATUV_jqMKskGzZTeXKnNbthd4HfY5fzW3GtQzjUUfr_x83eQvtRwOAa9mGxaR8KDzGUI-8PKFTDzY3R5-TgUlR7H2pFnBWhTEWjki0YBVejgXV4FL_Qqr1V8SnYctUBMc2dAp6-FZIMbgFORmobiWIdRCc42p7j7Id-EhLmtejFuDYuFVYQqy2JTwEI5n9RIsVspNGzuQp4ddsq-L0stm4lBRP-WDhbpau-R7gy6lTJFk3JDAtgnZPy2X_MTSECBcBPjjnKIbO21GzGDLoAj8j3o6_s2mtCfcCeiy4TuQ5SCZxwIgnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گوگل در حال تست URL آبی در نتایج جستجو است!
🔍
گوگل اخیراً در حال آزمایش تغییرات ظاهری در نتایج جستجوی موبایل است؛ به طور خاص، رنگ URLها که معمولاً خاکستری یا سبز بودند، حالا به رنگ آبی تغییر کرده‌اند!
👀
بعضی کاربران متوجه شده‌اند که در برخی جستجوها، آدرس سایت (URL) به رنگ آبی و در کنار عنوان لینک نمایش داده می‌شود، چیزی که پیش از این رایج نبوده.
🧪
این تغییر همراه با جابجایی محل نمایش URL و نام سایت انجام شده:
در بعضی موارد، نام سایت در بالا و آدرس URL در پایین نمایش داده می‌شود.
در برخی موارد دیگر، URL درست زیر عنوان لینک می‌آید، و نام سایت حذف شده.
📱
این تست‌ها فقط در نسخه موبایل گوگل دیده شده و هنوز مشخص نیست آیا به صورت دائمی اعمال می‌شود یا خیر.
📢
هدف گوگل از این تغییرات احتمالا افزایش خوانایی نتایج و بهبود تجربه کاربری است. البته هنوز بازخورد رسمی یا اطلاعیه‌ای از سوی گوگل در این باره منتشر نشده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 547 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feEZ1_GB-U_3j-Ynkgtrhpc0Yg8wPSKXobuMllzVwp4oMWfyUZ_xEgEzUa-DAV2wr3UV5DO-IG8laD3f4CdL-HcPN9jyXRJP7Mg7ZskvRcFb4ozFYzNZ4U_9WbFxiKhuG_Kpguj39p5c2eBc8fEx1EPTT8cVKKO2aF6UgX2kIodETaJhUneL0u_JX9QO3eTJlT_akWoTjQtEoic6Hyv-kWExErtTCV-VVHDgxFZock_kSxPVNCi8G6lfCLIUk41XZg2A_4MWF-n_CF4mnB1W59XchwtjsRK0Phlp2Bpj_E0Sl0n4pO4aPn_IBySAKCghQCyYKGFJrnCe32li4G4aNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
گوگل: استریم تصاویر برای سئو مناسب نیست!
🔍
جان مولر از گوگل توضیح داد که استفاده از تکنیک‌های استریم تصاویر (مثل قرار دادن عکس‌ها از طریق کد Embed به جای آپلود مستقیم) می‌تواند باعث شود تصاویرتون در نتایج جستجو ایندکس نشوند.
👨‍💻
در واقع وقتی تصاویر رو به این سبک بارگذاری می‌کنید (مثل ویدئوهای یوتیوب)، گوگل نمی‌تونه اون‌ها رو شناسایی کنه و در نتایج نمایش بده.
➖
نتیجه؟ کلی ترافیک احتمالی از دست میره!
🚫
📉
✅
اگر براتون مهمه تصاویرتون توی گوگل دیده بشه، بهتره روش سنتی آپلود مستقیم (JPEG, PNG و...) رو استفاده کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 546 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmD5RrgI7uO24QdAtuPV9yym78pZeBA-BkwrbWH_fSCVNRZroz3ThnxacypYmbbWGnaYnV0RmDju7BwPrBAHZmzW-zus76DE9s-MUYVKAuaiXA4VyLiLlXiYOjwtivBrvm5UfQcSNsOoGIx_WWETQLwg9FSNcG6fayvHnC9a3_T-DNvTh07lR7Zz7RTAB7OYEtLc6h57ccPHhMgel3aPHF9KTJ2ZSzH_XyQY7s8XkBhq124Y3c8TbyJbMiZcGBto63zKqAM6qDjZtbJEQvA0oMtS__Y9A4EyL_W6d0NRxM6zRsWdlC08KZy38Eqek1NkqN0J-g2D-z2JVGyXm_YZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گوگل تأیید کرد: داده‌های ساختاریافته باعث بهبود رتبه سایت نمی‌شوند​
📢
در تازه‌ترین اظهارنظر، جان مولر از گوگل اعلام کرد که استفاده از داده‌های ساختاریافته (Structured Data) به تنهایی تأثیری در بهبود رتبه‌بندی سایت‌ها در نتایج جستجو ندارد.​
🧠
داده‌های ساختاریافته چه کاربردی دارند؟
داده‌های ساختاریافته به گوگل کمک می‌کنند تا محتوای صفحات را بهتر درک کند و در صورت تطابق با معیارهای خاص، امکان نمایش آن‌ها در قالب نتایج غنی (Rich Results) مانند کاروسل‌ها، بررسی‌ها و دستور پخت‌ها فراهم شود. ​
⚠️
نکات مهم:
استفاده از داده‌های ساختاریافته تضمینی برای نمایش در نتایج غنی نیست؛ فقط امکان آن را فراهم می‌کند.
استفاده از انواع غیرمستند داده‌های ساختاریافته تأثیری در بهینه‌سازی جستجو ندارد؛ زیرا گوگل تنها حدود ۳۰ نوع از آن‌ها را در نظر می‌گیرد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 671 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiuWdjIxK4_Z82rQWZ9RECHq8xulEmZE5Wq5kFpcWsy0JUoidcJcqYAC98LUaSnhwegPt0fN7CZPeQgnUdV6PcScDEs3UVVmHBrlxerKNYABtG2QGleFKAgDECEmij41gHHgroX48hNIgJWioN3quY7y2hR0DA9fHJS1Fv0FfzFE1_Dd3COVKueCgGRHFNM_JS_Cuj4UTiRcjMmWSsKFjTtaPvTUumpO6wrc6Ld54SnuhUV75FZEAHnqKO3RHpoC94HBr106mZBgc4AxPKfrJkno1H3NC6npb5f1ziFUdTD_4Qo_lhqe_2QTsIPi4LWbmDJDO1FzDnmcJUtEVoFvKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
گوگل: فایل LLMs.txt به اندازه تگ متا کیورد بی‌فایده است!​
📄
جان مولر از گوگل اعلام کرد که فایل LLMs.txt، که به‌عنوان راهی برای هدایت خزنده‌های هوش مصنوعی پیشنهاد شده بود، در عمل بی‌فایده است و آن را با تگ متا کیورد مقایسه کرد که سال‌هاست توسط موتورهای جستجو نادیده گرفته می‌شود.​
🔍
فایل LLMs.txt چی بود اصلاً؟
یه سری از متخصصا و کمپانی‌ها پیشنهاد دادن که ما بیایم یه فایل به اسم llms.txt روی روت سایت بذاریم، تا مشخص کنیم چه مدل‌های زبانی (مثل OpenAI یا Anthropic) اجازه دارن محتوای ما رو بخونن یا نه. در واقع، یه چیزی مثل robots.txt ولی مخصوص هوش مصنوعی‌ !
🤖
📌
فایل LLMs.txt  به‌عنوان استانداردی برای کنترل دسترسی مدل‌های زبان بزرگ (LLMs) به محتوای وب پیشنهاد شده بود.​
📌
جان مولر اظهار داشت که این فایل توسط خزنده‌های هوش مصنوعی بررسی نمی‌شود و تأثیری در سئو یا کنترل محتوا ندارد.​
📌
تجربیات کاربران نیز نشان می‌دهد که پس از افزودن این فایل به سایت‌هایشان، هیچ تغییری در رفتار خزنده‌ها مشاهده نکرده‌اند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 685 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 693 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🎯
اخطار
گوگل: محتوای تولید شده با هوش مصنوعی در پایین‌ ترین رتبه قرار میگیرد
🔍
📢
در یک به‌ روزرسانی مهم، گوگل اعلام کرده ارزیابان کیفیت موتور جستجویش (Quality Raters) موظف شده‌اند تا محتواهای تولیدشده توسط ابزارهای هوش مصنوعی را نیز بررسی کنند و اگر این محتواها کم‌ ارزش، بدون تلاش انسانی یا فاقد اصالت باشند، باید پایین‌ترین رتبه ممکن را دریافت کنند!
🧾
تعریف رسمی گوگل از هوش مصنوعی مولد
"هوش مصنوعی مولد (Generative AI) مدل‌هایی هستند که می‌توانند براساس داده‌هایی که آموزش دیده‌اند، محتوای جدیدی مانند متن، تصویر، موسیقی و کد تولید کنند."
گوگل تأکید کرده که این ابزارها می‌توانند مفید باشند، اما در صورت استفاده نادرست، به‌ راحتی منجر به تولید انبوه محتوای بی‌کیفیت می‌شوند.
🛑
تمرکز جدید گوگل روی محتواهای کم‌ ارزش
💥
گوگل ساختار بخش‌های مربوط به محتوای خودکار را بازنویسی کرده و به‌شکل جدی با محتواهایی که:
تنها برای جذب ترافیک تولید شده‌اند
فاقد ارزش افزوده برای کاربر هستند
فقط ترکیبی از اطلاعات تکراری‌اند
مقابله خواهد کرد.
📌
حتی اگر چنین محتواهایی توسط انسان بازنویسی شده باشند ولی نشانه‌ای از تلاش واقعی، تجربه تخصصی یا هدف مفید برای مخاطب در آن‌ها نباشد، باز هم امتیاز پایینی خواهند گرفت.
📍
جمع‌ بندی مهم برای تولیدکنندگان محتوا، سئوکارها و مدیران سایت‌ ها
🟢
استفاده از هوش مصنوعی ممنوع نیست!
🔴
اما اگر بدون دقت، بازبینی و بدون ارزش واقعی باشه، رتبه سایتتون در خطره!
🛠
پس: هوش مصنوعی + تجربه انسانی = محتوای موفق
💡
@danialtaherifar</div>
<div class="tg-footer">👁️ 877 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGnpuLmKkgJnQYci3nFQM_iE_NiL1-HuePt9kPN8Q91LWs0k43-SUcBjOOnZOHTM_KoEEm_NiQHGn0abhGKY5XlQ9QBkU-tkvhbixeDyIqxfKAHPS0i0LcITUNClwfTW7gUHZY3aU3P2RA8NEwI_b2cuAZdlt9CeQ-R8aVQTjB0aBGiTl-QIe9hBOkxNn3SCdfD86EXnw0hXwN-LFdOzBW47dnexnv4jzh4vIUdDMqKvAVZE9JyC2E6Ql_h-vTTg9zZLrJAmnjmx_cWubSlBstqhgCd60px2TJ1MKw_bJd_NzWW2TI32JH-RkXFC1oxLgHD5DDEv3NWURq3SWpNvBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FmSIvMMb1xxGFUoxVjW6gdNBMOos49a4PFP9UP9PnIQ1Aj_IDlcWUSGJz0MmfnRxOVjkB_7dZJgHpDRFEPtKhyNLI4MvYCYB8N3aiqz7dNTZ6cEKRVMyY-nkGTgq1RG-OQOMv0V4T-HvDxjy4KpN8smDRC-VTbqWYUgiOCq00rypTDFMnXsp8XhFcC9vPRL4uzjet3MZJQ5CPmjzna7XeASEYXFpa7SfXRegvSxFMzgzY92dVzFGccoBrxCzl3KMIMcOdvQ6VjnB2XTKakjkNTflMytHQRwRK0XOlGC5Xf7lZ7GLI0YjutjMnPTue5DJRWUklFMOOKroRM3dlCnScg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
دسترسی به داده‌های ساعتی در API سرچ کنسول گوگل برای ۱۰ روز گذشته فعال شد!​
گوگل به‌ تازگی قابلیت دریافت داده‌های ساعتی را در API سرچ کنسول خود فعال کرده است. این ویژگی به کاربران امکان می‌دهد تا اطلاعات عملکرد جستجوی وب‌سایت خود را با جزئیات ساعتی برای ۱۰ روز گذشته دریافت کنند.​
🆕
چه چیزی تغییر کرده است؟
پیش‌تر، گزارش‌های عملکرد در سرچ کنسول فقط داده‌های ساعتی ۲۴ ساعت گذشته را نمایش می‌دادند.​
اکنون، از طریق API، می‌توان داده‌های ساعتی را برای ۱۰ روز گذشته دریافت کرد.​
برای استفاده از این قابلیت، باید از بُعد جدیدی به نام HOUR در درخواست‌های API استفاده کرد.​
همچنین، مقدار جدیدی به نام HOURLY_ALL به پارامتر dataState اضافه شده است که نشان‌دهنده داده‌های ساعتی (که ممکن است ناقص باشند) است.​
💡
چرا این ویژگی مهم است؟
این قابلیت به مدیران وب‌سایت و متخصصان سئو امکان می‌دهد تا نوسانات ترافیک و عملکرد سایت خود را با دقت بیشتری بررسی کنند و در صورت بروز مشکلات، سریع‌تر واکنش نشان دهند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 817 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S8w3ih4kaDhDkAFKwIRSXHhfmCKq8qM0uZOD6fhhB_pyGaqwtnp-w0-8ljnAW399Rz4aQraKpjdJXCzLN7towpn11Mpfy5urTY1DkZxO1CeAL-eacOXlf7p1MVi5s0l6BZRkWfXfSsKfP1IiLiWtM7lcwuVW0sD9aLe8k7GWSXzD-Z5WDSlIssYXgIWLRWSSoj73STBfaHYQjf5Twooqr4dkE-vl0kAhK1mmSjeNHXqYdrJ9e7cwUEmLWKf_pPLOe3taKC4DVS15H_5pkxdHbmAChD5tpBhzNZHiX2W1_WzFf8IXTwdbWaXpIrDSy2JkSkNCROn6Lu5WSHGvF7k0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jdsUARG3jVqioO1ejeQvx0AIeekItGmivW67yNr67ld7KGxopHJ0Dx6jikuFj_Dm4c1MFrrM15xTZv_VrFAMmyTa6QBT_e2u7bXwABKOP4rXDe_2uDeu_fqjg2iHBTXd9Voi6sY9anwmNPAiLN68mcd3UL2XBisrUSYf2vHR7AAa3ZD3qfsUMFlM9aqD4xwOr5kCC64PThd7Tca_UV2M-uiQcpZpl_JR4AmXjmyn4S2xnfPMPF3Zv2SgLizlpJkf-X_sXH-7gafMClzSW8dExpVWx7x8M7_gfq8aJV_k9oRWM4eUdJ1sNYT8SGyRlnfV7hPOAl4fmHw83dIaXM1rFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 808 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFKajy2u8uDpEVH23faNZQ6K4QQGvcOoXnbeUl6OEqfoMQw56lt2eTpvKDPPlKSw2WMsSkgyD4a4_3xSD8SzaLT1u4wxmbhUwARlicGYx6yy4lYI7JfHDOADkrjbnKWdEnj1XuBF8gFmwSuiFjW6GDBiOrKFaP1pK-KGdL3wSuK8gOb4mxiwq0HF0sdtJVbfH1GYJzN80y_ihWUS9VQBovwurqzbJTWXrNsqO2AQGIrgVMJ-5-XoPjl9lhfaFJmYrUqpmzl6aKJ2DtkrGzs4_tIygWW0tZ0KNfG7jV-hu_FaFkhdogbTNI2GH8ilB0Suq_-UeI1vRzZjOQlB2S57Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🔍
گوگل دیسکاور به دسکتاپ می‌آید: تغییر بزرگ در صفحه اصلی گوگل
🔔
گوگل اعلام کرده است که پس از سال‌ها آزمایش، قصد دارد گوگل دیسکاور (Google Discover) را به نسخه دسکتاپ صفحه اصلی خود اضافه کند. این خبر در رویداد Search Central Live در مادرید به صورت رسمی اعلام شده است.
📱
گوگل دیسکاور یک فید محتوایی شخصی‌سازی‌شده است که تاکنون فقط در دستگاه‌های موبایل در دسترس بود و به کاربران کمک می‌کرد محتوای جدید و مرتبط با علایقشان را کشف کنند. حالا این تجربه به دسکتاپ هم می‌آید.
👀
در هفته گذشته، برخی کاربران در ایالات متحده مشاهده کردند که گوگل در حال آزمایش نمایش فید دیسکاور در صفحه اصلی دسکتاپ خود است. این نشان می‌دهد که گوگل به دنبال ارائه تجربه‌ای یکپارچه در تمام دستگاه‌هاست.
📊
این تغییر می‌تواند تأثیر قابل‌توجهی بر استراتژی‌های محتوایی ناشران و سایت‌ها داشته باشد، چون دیسکاور یکی از منابع مهم ترافیک برای آن‌ها شده است.
🎯
با این به‌روزرسانی، کاربران دسکتاپ هم می‌توانند به‌راحتی به محتوای تازه و شخصی‌سازی‌شده دسترسی داشته باشند و لذت تجربه‌ای مشابه موبایل را ببرند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 588 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">📊
✨
چطور گزارش سئو بنویسیم که مدیر بازاریابی (CMO) عاشقش بشه؟
نوشتن گزارش سئو فقط نمایش اعداد نیست، بلکه باید داستانی بسازید که نشون بده سئو چطور به رشد کسب‌وکار کمک می‌کند. در ادامه به چند نکته مهم برای گزارش نویسی اشاره می‌کنم.
1.
🚀
نتایج تجاری، نه فقط داده‌ های فنی
مدیر ارشد بازاریابی (CMO) معمولاً با واژه‌هایی مثل "ترافیک"، "لینک‌ سازی"، یا "موقعیت کلمات کلیدی" ارتباط برقرار نمی‌کنن. اون‌ها می‌خوان بدونن این عددها چه تأثیری روی درآمد، برند و رشد کلی شرکت دارن.
✅
به جای این‌ که فقط بگید "افزایش ترافیک داشتیم"، بگید:
«ترافیک ارگانیک باعث افزایش ۲۵٪ سرنخ‌های فروش شد که منجر به ۱۵۰ هزار دلار درآمد شد.»
2.
💵
از ارزش مالی صحبت کن
باید نشون بدید که سئو به لحاظ مالی چقدر به صرفه‌ست. مثلاً:
🔸
هزینه جذب هر مشتری از طریق تبلیغات = ۱۲۰ دلار
🔸
هزینه جذب از طریق سئو = ۲۵ دلار
🔍
اینجوری نشون می‌دید سئو باعث صرفه‌جویی واقعی در هزینه‌ها میشه.
3.
📈
تمرکز روی محتوای برتر
به‌جای ارائه لیستی از تمام محتواها، فقط چند محتوای موفق رو هایلایت کنین. بگید:
«این مقاله وبلاگ ۳۵۰ سرنخ ایجاد کرد، به رتبه اول در گوگل رسید و در شبکه‌های اجتماعی ۵۰۰ بار به اشتراک گذاشته شد.»
4.
🧠
از زبان CMO استفاده کن، نه زبان سئوکارها
🔴
نگید: «Domain Authority این سایت ۷۰ بود.»
🟢
بگید: «ما از یک سایت معتبر لینک گرفتیم که باعث رشد رتبه ما در نتایج شد.»
زبان ساده، قابل فهم، و متمرکز بر نتیجه = موفقیت گزارش شما.
5.
📅
تغییرات را در بازه زمانی مقایسه‌ای نشون بده
مثلاً بگید:
«در مقایسه با ماه گذشته، ترافیک ارگانیک ۲۰٪ افزایش یافته و نرخ تبدیل از ۲٪ به ۳.۵٪ رسیده.»
نمودار و ویژوال هم خیلی کمک می‌کنه!
6.
📌
پیشنهادات عملی ارائه بده
فقط گزارش نده، بگو چه قدم‌هایی باید برداشته بشه. مثلاً:
✅
«اگر بودجه لینک‌سازی ۳۰٪ افزایش پیدا کنه، می‌تونیم تا سه‌ماه آینده ۵ رتبه در نتایج گوگل صعود کنیم.»
جمع‌ بندی
🎯
مدیران بازاریابی به دنبال تأثیر واقعی سئو روی رشد شرکت است. گزارش شما باید نشان دهد:
🔹
سئو چطور به درآمد کمک می‌کند
🔹
چه نتایج قابل اندازه‌گیری‌ای به دست آمده
🔹
قدم بعدی برای پیشرفت چیست
با این سبک گزارش‌نویسی، نه‌ تنها توجه CMO رو جلب می‌کنید، بلکه اعتبار تیم سئو رو هم بالا می‌برید
💪
@danialtaherifar</div>
<div class="tg-footer">👁️ 587 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZoWQHCQSrQgjE9wEseIhuzlXgtoQIhy3kmvsjxOMX1mRpdgybtTHOxF-f4aobSR8ymM2FmS7LTS9bjdz4BixtEQdnnQGqIGS54pQGmNz-kCprbX21mKrNDjY1QJdA7uiVyA7E1H1Oo3tIqBqZEYiYZsJIzuVqBZtxwR4sPv_1s6SyO17umQCaSC-Rjpnx4N-f4io1FebA-VnHQdoNMF32A23emMtQ2Pyb-uuSMABXnEAZ9o09yc241uT-FNzKjzS9PEv3Zf_UNVa2yWi3R0_gRbc0GaeeYpQSb3VJ5wV61TttMAj76J786AYLR8jj_0P2JVo7FuB_9zn7ezUGWkb-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DViuc-I3xLGaveluiBnKqpdYrCxXpS70ADlA1WY2Xd-CRJBD06FznGGTU_HwW9kd6m3qydn22rNXSvJT-t5NwO8Qt02uIpiVnjwBhl2sRxXuFVqUMhViLqniUgRk7bE4_8qOlJGaBGw1EjpwyEQejoO37_CGlOUTWFmUhHYgn4QBpyL7yanHQ94X5Bih6NANMf-UQf9epC6aLvwymvqM1u3PsDw6glC_il9dR-Iopo47oMNXe2gNbRaPTCnFB7MbqIhfTUsLfExUXwI79qvE3oKYil1AtTB8ZxFOOeaMmM0ntRmZYN74JXI1MEtqediFP6CMN3BJMchHL-CIYzzibQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
ویژگی جدید گوگل: نمایش موضوعات مرتبط در جستجو!
🔍
📚
✨
🔎
گوگل در حال آزمایش قابلیتی جدید به نام "Relevant Topics" یا "موضوعات مرتبط" است که در پایین برخی نتایج جستجو نمایش داده می‌شود. این قابلیت کاربران را تشویق می‌کند که فراتر از جستجوی اولیه‌شان، موضوعات مرتبط بیشتری را بررسی کنند.
📱
سچین پاتل (Sachin Patel) یکی از کاربران شبکه اجتماعی X (توییتر سابق)، اولین کسی بود که این ویژگی را مشاهده کرد و اسکرین‌شاتی از آن منتشر کرد.
🔍
وقتی او عبارت "SEO" را جستجو کرد، در پایین صفحه نتایج، بخشی با عنوان "Relevant Topics" ظاهر شد که لیستی از موضوعات مرتبط با سئو را نشان می‌داد.
📂
در کنار این لیست، گزینه‌ای با عنوان "Show more" یا "نمایش بیشتر" وجود داشت که با کلیک روی آن، موضوعات بیشتری نمایش داده می‌شد.
🛠
این بخش می‌تواند به سئوکاران و تولیدکنندگان محتوا کمک کند تا متوجه شوند گوگل چه موضوعاتی را به عنوان مکمل جستجوی اصلی در نظر می‌گیرد.
💬
فعلاً گوگل این قابلیت رو به‌صورت محدود و آزمایشی نمایش می‌ده و هنوز معلوم نیست چه زمانی به‌صورت رسمی برای همه کاربران فعال خواهد شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 676 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔥
گوگل به‌ روزرسانی هسته‌ مارس ۲۰۲۵ را تکمیل کرد!
🚀
🔍
📢
پس از ۱۴ روز به‌روزرسانی Core Update مارس ۲۰۲۵ گوگل، چند روز پیش به پایان رسید! این به‌روزرسانی که در ۱۳ مارس ۲۰۲۵ آغاز شد و در ۲۷ مارس ۲۰۲۵ تکمیل گردید که تغییرات مهمی در الگوریتم‌های جستجو ایجاد کرده است. اگر شما هم در این مدت تغییراتی در ترافیک سایت خود مشاهده کرده‌اید، این به‌روزرسانی می‌تواند دلیل آن باشد.
🧐
🔄
🔎
جزئیات کامل به‌روزرسانی Core Update مارس ۲۰۲۵
🔹
تاریخ شروع: ۱۳ مارس ۲۰۲۵
🔹
تاریخ اتمام: ۲۷ مارس ۲۰۲۵
🔹
مدت زمان اجرا: ۱۴ روز
🔹
هدف: بهبود نمایش نتایج جستجو با تمرکز بر کیفیت محتوا
🔹
نوع: این به‌روزرسانی به‌عنوان جریمه عمل نمی‌کند، بلکه صفحات وب باکیفیت را ارتقا می‌دهد.
🔹
گستره: یک به‌روزرسانی جهانی است و بر تمام زبان‌ها و مناطق تأثیر می‌گذارد.
🔹
تأثیر: برخی از سایت‌ها تغییرات چشمگیری در رتبه‌بندی تجربه کرده‌اند.
📌
تأثیرات این به‌روزرسانی بر وب‌سایت‌ها
🔥
برندگان:
✅
سایت‌هایی که محتوای باکیفیت و اورجینال دارند، شاهد بهبود رتبه‌بندی شدند.
✅
وب‌سایت‌هایی که تجربه کاربری (UX) بهتری ارائه می‌دهند، افزایش ترافیک داشتند.
✅
سایت‌هایی که از محتوای تولیدشده توسط کاربران (UGC) به‌درستی استفاده می‌کنند، امتیاز بهتری گرفتند.
⚠️
بازندگان:
❌
سایت‌هایی که محتوای کم‌کیفیت یا کپی‌شده دارند، کاهش رتبه داشته‌اند.
❗️
📉
❌
صفحات دارای تبلیغات بیش‌ازحد یا تجربه کاربری ضعیف، تأثیر منفی دیده‌اند.
❌
وب‌سایت‌هایی که از روش‌های قدیمی سئو (مانند تکرار بیش‌ازحد کلمات کلیدی) استفاده می‌کردند، ضربه خورده‌اند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 903 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔍
تحول به سمت جستجوهای بدون کلیک
📉
بر اساس تحقیقات اخیر، بیش از ۶۰٪ از جستجوها بدون کلیک خاتمه می‌یابند. این یعنی کاربران دیگر نیازی به ورود به وب‌سایت‌ها برای یافتن اطلاعات ندارند، زیرا پاسخ‌های خود را از بخش‌های مختلف SERP مانند (Featured Snippets)، (Knowledge Panels) و (Instant Answers) دریافت می‌کنند. این موضوع باعث کاهش چشمگیر ترافیک ورودی به سایت‌ها شده است.
🔎
چگونه گوگل ترافیک را درون خود نگه می‌دارد ؟
گوگل با توسعه قابلیت‌هایی مانند:
✅
نمایش پاسخ‌های مستقیم در نتایج جستجو
📌
✅
پیشنهاد‌ های Google Suggest
⌨️
✅
باکس‌ های نالج گراف (Knowledge Boxes)
📚
✅
نمایش اطلاعات کسب‌وکارها در گوگل مپ
📍
✅
و حتی قابلیت خرید مستقیم در نتایج جستجو
🛒
در تلاش است تا کاربران را درون پلتفرم خود نگه دارد و از خروج آن‌ها به وب‌سایت‌های دیگر جلوگیری کند.
🚀
استراتژی‌های مقابله با کاهش کلیک‌ها
1️⃣
بهینه‌سازی برای (Featured Snippets)
با ارائه پاسخ‌های دقیق، خلاصه و ساختاریافته به سوالات کاربران، می‌توانید شانس نمایش سایت خود را در باکس‌های ویژه گوگل افزایش دهید.
🔝
2️⃣
تمرکز بر برندینگ و ایجاد آگاهی از برند
اگر کاربران شما را به عنوان یک مرجع قابل اعتماد بشناسند، مستقیماً به سایت شما مراجعه خواهند کرد. حضور پررنگ در شبکه‌های اجتماعی و تولید محتوای ارزشمند می‌تواند به شما کمک کند.
💡
3️⃣
استفاده از داده‌های ساختاریافته (Structured Data)
با اضافه کردن اسکیما مارکاپ (Schema Markup) به صفحات خود، گوگل را قادر می‌سازید تا اطلاعات وب‌سایت شما را بهتر درک کند و در نتایج جستجو نمایش دهد.
🛠
4️⃣
ایجاد صفحات تعاملی و کاربردی
اگر کاربران پس از ورود به سایت شما تعامل بیشتری داشته باشند (مانند مشاهده ویدیو، خواندن محتوای کامل)، گوگل این را یک سیگنال مثبت در نظر گرفته و سایت شما را در رتبه‌بندی بهتر قرار خواهد داد.
📈
5️⃣
تنوع‌بخشی به منابع ترافیک
به جای تمرکز صرف بر ترافیک ارگانیک، از روش‌های دیگر مانند بازاریابی ایمیلی، تبلیغات پولی، فعالیت در شبکه‌های اجتماعی و استراتژی‌های محتوایی ویدئویی استفاده کنید.
🎯
🌟
با پذیرش این تغییرات و تطبیق با روندهای جدید، کسب‌وکارها می‌توانند در دنیای جستجوهای بدون کلیک نیز موفق باشند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 884 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔹
🚀
گوگل قوانین جدیدی برای استراکچر دیتا و بازگشت کالا اعلام کرد!
🔍
گوگل اخیراً الزامات داده‌های ساختاریافته (Structured Data) برای سیاست‌های بازگشت کالا را بروزرسانی کرده است. این تغییرات بر نحوه نمایش اطلاعات در نتایج جستجو تأثیر می‌گذارد و فروشگاه‌های آنلاین باید سریعاً اقدام کنند!
🛒
📊
💡
چه چیزهایی تغییر کرده است؟
✅
شفافیت بیشتر در نمایش اطلاعات بازگشت کالا
🔄
🔍
✅
ضرورت استفاده از استراکچر دیتا برای سیاست‌های بازگشت
📌
📊
✅
نیاز به مشخص کردن مدت زمان بازگشت، شرایط و هزینه‌ها
⏳
💰
نمونه به‌ روز شده از JSON-LD برای داده‌های ساختاریافته سیاست بازگشت کالا که دقیقاً مطابق با مشخصات جدید گوگل است:
"hasMerchantReturnPolicy": {
"
@type
": "MerchantReturnPolicy",
"applicableCountry": "CH",
"returnPolicyCountry": "CH",
"returnPolicyCategory": "
https://schema.org/MerchantReturnFiniteReturnWindow
",
"merchantReturnDays": 30,
"returnMethod": "
https://schema.org/ReturnByMail
",
"returnFees": "
https://schema.org/FreeReturn
"
}
🔹
بخش merchantReturnDays: حداکثر تعداد روزهایی که مشتری می‌تواند محصول را بازگرداند (در اینجا 30 روز).
🔹
بخش returnFees: مشخص می‌کند که آیا بازگشت کالا رایگان است یا هزینه دارد (در اینجا Free یعنی رایگان).
🔹
بخش returnMethod: نحوه بازگشت کالا (در اینجا Mail یعنی ارسال پستی، می‌تواند "InStore" هم باشد).
🔹
بخش returnShippingFeesAmount: هزینه ارسال برای بازگشت کالا (0 دلار یعنی رایگان).
📢
این استراکچر دیتا باعث می‌شود گوگل بتواند سیاست‌های بازگشت کالا را به‌درستی در نتایج جستجو نمایش دهد و تجربه بهتری برای کاربران ایجاد شود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 973 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jubiQ6KHLK3MlzV1X1B7tw-yG6FUcYShbyKuYsOkfO9dYWZLfkXXU857vsc1PTSifet7G8pF_FlalikjVasE0JYNJrWv9G3ngIL7kGHxIjlJ6j6Rh2oZENd4318vk1XSo_xIeBXNnT59tgFALJAD82Xybs9GRxXnaXZG8G8crJrkdsYgfUsZTfPIk9cbzkoxv-JfPRz4W9Ltwk2aRH-TldZ2Hqv5q7uaZZolud_IJ5lFMVyX6WJ4VPBjsrkBNDl3ivsGhC5kZ9QfIZhuvs6WKCgM3cCOgKRZp6iZ63I_EDg6ImFOt9HFFd3L9Xf5vXBaPMj5-uEr_zaSgjHR5FfW7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 718 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMe9JRy0BylwoiKjVmxPVOtL-HxD9yf9QE-OIl-Zyzd8NkG14d8DSEJW0M0mPIIzpzl5WRqdU_AJ2ZorSzGY84m4T6EIch0I9QE3x5bHGW2F0G9rQvfEA43N4jBa5pEaux0zU1UWjOShL_y8lBG0qcnZYKvkVm20I0V8U9miyem49OCk0u2kz6DWxDqiatbRA9pHBD51IzAkTfJQ7OudmWeKZF50zE3DN1vr38MRJ8ProbNgFX4PFETI7Q5v4I6EAoT6Pfd-4FYCU9rh4w4KTvLrdPPuxlQ0vymrK6uNiqUbq-a1-E4SuAAWx4he51PRjeh4rpDK_vVgriAluqxrXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚫
ریدایرکت کردن صفحات 404 به صفحه اصلی کار درستی نیست!
📢
مارتین اسپلیت
، یکی از کارشناسان گوگل، به تازگی در مورد یه اشتباه رایج سئو صحبت کرده: ریدایرکت کردن صفحاتی که خطای 404 (صفحه پیدا نشد) دارن به صفحه اصلی سایت.
💬
به گفته‌ی اسپلیت، این کار نه‌ تنها کمکی به تجربه کاربری نمی‌کنه، بلکه می‌تونه برای سئو هم دردسرساز بشه! وقتی یه صفحه خطای 404 داره, بهتره به جای ریدایرکت به صفحه اصلی، یه صفحه اختصاصی 404 طراحی کنید، که کاربر رو راهنمایی کنه یا اون رو به یه صفحه مرتبط بفرستید.
❓
چرا این موضوع مهمه ؟ چون گوگل می‌خواد بفهمه محتوای سایتتون چیه و
ریدایرکت بی‌منطق
می‌تونه سیگنال‌های اشتباه به موتور جستجو بفرسته. این کار ممکنه باعث بشه صفحات ارزشمند شما ایندکس نشن و سایتتون دچار مشکل بشه!
🚧
@danialtaherifar</div>
<div class="tg-footer">👁️ 775 · <a href="https://t.me/danialtaherifar/843" target="_blank">📅 13:33 · 19 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCrSI9K9wHoNUlXtm-3CmzMN1HAjRTz7GcJtTZ8U6jR7FWUzetsbcOZphaCFJTIV70XwEfRlfTbujorWaMxP7oqi8CLXYkUhdWgtouP0qoI2TIzQ5EYMkkaxhiqbjIOb9XwQR7Gd31yv6q6dKsoxiuLLtDM7ots6JyKYZuQ7RrCrS47bAHcFXc3FbZcvjYnNjLJfntlEMlpSKnOGI-EL7QrgKZdNqhpNLS_2YMoelo1lrAsWk-Ne3DSXKbQ3wazdTHWJJgh84R5Ce0TUZOSh3OqCf7wln2MdbFk45JiX70mB9Ss3YvjwN9FCx4R3nmsvTsoFD-BfvhbBfBxrYuZ76g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
هوش مصنوعی AI Overviews گوگل، دشمن جدید سئوکاران؟!
🔍
تحقیقات اخیر نشان می‌دهد که با افزایش استفاده گوگل از
هوش مصنوعی (AI Overviews)
در نتایج جستجو،
نرخ کلیک (CTR)
وبسایت ها به‌ طور قابل‌ توجهی کاهش یافته است. این تغییرات می‌توانند تأثیرات مهمی بر استراتژی‌های سئو و بازاریابی دیجیتال داشته باشند.
🔹
نتیجه؟ کاهش ترافیک سایت‌ها و چالش جدید برای سئوکاران!
🚨
💡
چگونه در این رقابت حضور داشته باشیم ؟
✅
محتوای ارزشمند و تعاملی تولید کنید
✍️
🔥
✅
بهینه‌ سازی برای AI Overviews را جدی بگیرید
⚙️
🤖
✅
از داده‌های ساختاریافته (Schema) استفاده کنید
📊
🔗
🌐
با توجه به تغییرات اخیر در نتایج جستجوی گوگل و افزایش استفاده از هوش مصنوعی، ضروری است که کسب‌ و کارها و وب‌ سایت‌ها استراتژی‌ های خود را متناسب با این تغییرات تنظیم کرده و به
بهبود تجربه کاربری
و
ارائه محتوای با کیفیت
تمرکز کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 772 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OH_z4Jq7mLLSC7_5sJXWyaz8oSx891WhoMrEsqAt4ZPi_DfKBE0d47PCxZbKRgK7UZQRdB5xfbq-1BAQh_fJlSp_FMRbPbXMi8SyxXNCBv5gaQCDEZBWGNBME96J9PUli8pRw7tv5uC5aErbwiiQMUNZc5FQazttxasDh1-U4RtDUPeRuoEucSZFo8S8jY-I_MP296gEwd7ZSMiV354cJj5485Wkte_eh1ekarpi-0YMSAFoxWXNRD6N76P8o02Sp6WaMveOBKS9MudQlYY958xmzqzbRn5kljYSR4Ynxm6IsflApwqlUQ00je0DXJvRzO_ErEezSHQWzQjDpXvjWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/irv1owoOunESugNceubGGpAYSkNUFSCre-tr2NfeEUzP3nmZPFaAK2bYJIE0YBSs4TMYFr7bavBh6whI1LYmM42BmngJR-mol5f9_c2zEgq8o_9LJGk59udzjTK01VM3ZqDp_G5ML1wvEc7APCCluz2mLthynIL7Eqv_9FP7JmNChq-ZXr6stzr6d5msFL6dk1lXGP0D6HSh_l_K21gXIYcw8PKF7BX0aG19nLtTBtiUCsEqfsoHANnmIC16HsNVudwmx3jFlEVzYKxOr3BQPW2MFmCpNJc22G2nzwQpslfdKCDO-vCGDLs42sHsWGsxCUyS0QkNtoMHr2MIaSHRPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
گوگل مستندات تگ متا ربات‌ها را برای اضافه کردن "AI Mode" به‌روزرسانی کرد!
🔹
گوگل اخیراً مستندات مربوط به تگ متا ربات‌ها را به‌روزرسانی کرده و حالت جدیدی به نام "AI Mode" را معرفی کرده است! این ویژگی با بهره‌گیری از هوش مصنوعی، تجربه جستجو را پیشرفته‌تر و دقیق‌تر از قبل می‌کند.
✨
این قابلیت از مدل هوش مصنوعی Gemini 2.0 استفاده می‌کند و توانایی ارائه پاسخ‌های تحلیلی، دقیق و چندوجهی را دارد.
📌
کاربران از طریق یک تب اختصاصی در صفحه جستجو به این حالت دسترسی دارند و می‌توانند اطلاعات گسترده‌تری دریافت کنند.
🔍
چه کسانی می‌توانند از AI Mode استفاده کنند؟
🔹
این ویژگی فعلاً برای مشترکین Google One AI Premium و برخی کاربران منتخب در آمریکا از طریق Search Labs فعال شده است که از این قابلیت برای ارائه اطلاعات خرید نیز استفاده می‌کند تا تجربه کاربران را بهبود بخشد.
🌐
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#directives
@danialtaherifar</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvcgVClS8clKaq58hnH7wSlRtzkqmM-oV2WKRvjsoVq2WnXc2vJN-s8d445AT45yoFDVs-A2C-kYr9VpB4jAzyHivfAJoCBNwO1-IOYNb2-RtjpKh2xwe8NiYN77Z6Ffn6pNwTlVNV4D4mQMhENJz7TF74qnYAj-D8pxwWtQe5ENIdt0aLK-v6k1wikuufsu1QbmmmZwKzFAoT56eIHlQJK4aZB00RW-4HFQZKKUY-ClyK6nCX5IwX_R2_nAFUhmOMqnqu43DSSsRKfidqXAoiVFfA8GaMmqSqCLMEiGwWxL3NcmrPakc-FXcHFfAqugMmIuphEniTeERGrpBZhf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل اکنون سالانه بیش از ۵ تریلیون جستجو را پردازش می‌کند!
🚀
🔍
افزایش چشمگیر جستجوها:
بر اساس داده‌های داخلی گوگل تا ژانویه ۲۰۲۵، این شرکت اکنون بیش از ۵ تریلیون جستجو در سال را مدیریت می‌کند.
📈
رشد قابل‌ توجه:
در سال ۲۰۱۶، گوگل اعلام کرد که سالانه ۲ تریلیون جستجو را پردازش می‌کند. این افزایش به بیش از ۵ تریلیون نشان‌دهنده رشد مداوم و قابل‌توجه در حجم جستجوهای گوگل است.
🤖
نقش هوش مصنوعی:
گوگل با استفاده از فناوری‌های هوش مصنوعی، تجربه‌های جستجوی غنی و چندرسانه‌ای مانند AI Overviews، Circle to Search و Lens را ارائه داده است. این ابزارها به کاربران امکان می‌دهند تا به‌صورت طبیعی‌تر و دقیق‌تر آنچه را که می‌خواهند بیان کنند.
🛍
افزایش جستجوهای تجاری:
با معرفی AI Overviews، حجم جستجوهای تجاری افزایش یافته است که فرصت‌های بیشتری برای کسب‌وکارها فراهم می‌کند تا با مصرف‌کنندگان ارتباط برقرار کنند.
این دستاورد گوگل نشان‌ دهنده تعهد مداوم این شرکت به
بهبود تجربه جستجوی کاربران
و
پاسخگویی به نیازهای متغیر جامعه دیجیتال
است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 623 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhqHdOiIac29ax__CQ7GUNv7S1CbaVkUWA8sPFqNrhoLEFuJG5ccUk3SZluY7ih1Jb6ScV_9dFzppviyQkVQV2auvVqLf-HXpySCIYvRSDSbUNia0CcOGLxYn9lc_BCDfI9jKdNlW3eieoZy2Y_UNfhNo_vMOiSTgTZeHQ8QxyvkpAh6WaUl4piPsZuZkE0huKP66maSBrLG9K4I2KAXGimOrxUwqV_tfB9x-AgMdhYMtJhVxghMO0khuDaIyw4uoo64e25HYFuUoxDZvSu1iWXUE6BPy2bLlPaF4JBZJPRY11FAqDIx-HGtOG4E9IZ-YvPGX1b5b8X1FWJS7TmyJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل در برابر محتوای کم‌ کیفیت اما خوش ظاهر سختگیر می‌شود!
🚨
🔎
بسیاری از سایت‌ها با استفاده از
محتوای تولید شده توسط هوش مصنوعی
،
بازنویسی‌ های سطحی
و
اطلاعات عمومی
سعی می‌کنند رتبه خوبی در گوگل بگیرند. این نوع محتوا معمولاً ظاهری حرفه‌ای دارد اما در عمق خود،
چیزی جدیدی به کاربر اضافه
نمی‌کند. گوگل با استفاده از الگوریتم‌های پیشرفته، این محتوا را شناسایی و رتبه آن را کاهش می‌دهد.
📉
⚠️
محتوای ضعیف چه ویژگی‌ هایی دارد ؟
❌
استفاده از جملات کلی و بدون اطلاعات دقیق
❌
تکرار مطالب عمومی که در سایت‌های دیگر وجود دارد
❌
عدم ارائه پاسخ‌های عمیق و مفید به سوالات کاربران
❌
استفاده بیش از حد از هوش مصنوعی بدون ویرایش انسانی
❌
هدف‌ گذاری فقط روی کلمات کلیدی بدون در نظر گرفتن نیاز کاربر
✅
اگر می‌خواهید در رتبه‌های برتر گوگل بمانید، محتوای شما باید
ارزشمند
،
کاربردی
و
واقعی
باشد، نه فقط
پر زرق‌ و برق
!
✍️
📚
@danialtaherifar</div>
<div class="tg-footer">👁️ 663 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">📢
تحول بزرگ در سئو: حرکت به‌ سوی سئوی معنایی و وکتورها !
🚀
🔍
🔥
گوگل دیگر فقط به کلمات کلیدی توجه نمی‌کند! با پیشرفت سئوی معنایی، موتورهای جستجو از وکتورها برای درک ارتباط مفهومی بین کلمات استفاده می‌کنند.
🧠
🔎
وکتورها: راز درک هوش مصنوعی
🤖
وکتورها ابزاری ریاضی هستند که هوش مصنوعی برای درک و سازمان‌ دهی اطلاعات فراتر از متن ساده استفاده می‌کند. به جای تکیه بر تطابق دقیق کلمات کلیدی، موتورهای جستجو اکنون از vector embeddings استفاده می‌کنند که کلمات، عبارات و حتی تصاویر را بر اساس معنای آن‌ها و روابط‌شان در فضایی چندبعدی ترسیم می‌کند.
🌐
🔗
🎯
به این صورت فکر کنید: اگر یک تصویر ارزش هزار کلمه را داشته باشد، وکتورها نحوه ترجمه این کلمات به الگوهایی هستند که هوش مصنوعی می‌تواند آن‌ ها را تحلیل کند.
🖼
➡️
🧠
💡
برای متخصصان سئو، این‌گونه می‌توان تشبیه کرد: وکتورها برای هوش مصنوعی همانند داده‌های ساختاریافته برای موتورهای جستجو هستند، روشی برای ارائه زمینه و معنای عمیق‌ تر.
📊
🌐
چگونه وکتورها جستجو را تغییر می‌دهند؟
🔄
با استفاده از
semantic relationships
,
embeddings
و
neural networks
جستجوی مبتنی بر وکتور به هوش مصنوعی این امکان را می‌دهد که هدف کاربر را به جای صرفاً کلمات کلیدی تفسیر کند.
🧠
💬
🔑
به این معناست که موتورهای جستجو می‌توانند نتایج مرتبط را حتی زمانی که یک کوئری شامل کلمات دقیق از یک صفحه وب نباشد، نمایش دهند. برای مثال، جستجو "کدام لپ‌تاپ برای بازی بهترین است؟" ممکن است نتایجی را نشان دهد که برای "لپ‌تاپ‌های با عملکرد بالا" بهینه شده‌اند، زیرا هوش مصنوعی ارتباط مفهومی این کلمات را درک می‌کند.
💻
🎮
📸
وکتورها چگونه به هوش مصنوعی کمک می‌کنند که محتواهای غیرمتنی را تفسیر کند؟
عبارات عامیانه (مثلاً "دندان روی جگر گذاشتن" در مقابل "تصمیم سخت گرفتن")
💬
تصاویر و محتوای بصری
🖼
ویدئوهای کوتاه و وبینارها
🎥
پرسش‌های جستجوی صوتی و زبان محاوره‌ای
🎙
📌
خلاصه: وکتورها در حال انقلاب در نحوه درک و رتبه‌بندی محتوا توسط موتورهای جستجو هستند و نتایج جستجو را مرتبط‌تر می‌سازند، حتی زمانی که کلمات دقیقاً تطابق ندارند!
🔍
✨
آیا برای این تغییرات در نتایج جستجو آماده‌ هستید؟
🤔
👇
@danialtaherifar</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔍
اهمیت Customer-Centric:  راز موفقیت در سئو
💡
✨
در Customer-Centric SEO به جای اینکه صرفاً بر الگوریتم‌ های موتور جستجو تمرکز کنیم، تلاش می‌کنیم
نیازها
و
انتظارات واقعی کاربران
را در اولویت قرار دهیم. با بهینه‌ سازی تجربه کاربری، ارائه محتوای ارزشمند و تحلیل مداوم رفتار مشتریان، می‌توان
ترافیک پایدارتر
،
تعامل بالاتر
و
نرخ تبدیل بهتری
کسب کرد. در ادامه، مهم ترین رویکرد های تجربه سئوی مشتری‌ محور رو بررسی می‌کنیم:
1️⃣
تحقیق عمیق درباره کاربران و سفر مشتری
🎯
✅
درک نیازها، مشکلات و سوالات کاربران قبل از تولید محتوا
✅
بررسی پرسوناهای مشتری و تحلیل داده‌های جستجو برای یافتن موضوعات پرتقاضا
✅
استفاده از ابزارهایی مانند Google Analytics، Google Search Console و ابزارهای سئو مانند SEMrush و Ahrefs برای تحلیل رفتار کاربران
2️⃣
ایجاد محتوای ارزشمند، کاربردی و مرتبط
📝
✅
تولید محتوا با تمرکز بر نیازهای واقعی کاربران نه صرفاً برای رتبه گرفتن
✅
استفاده از فرمت‌های مختلف محتوا مثل متن، ویدیو، اینفوگرافیک، پادکست و محتوای تعاملی
✅
ارائه راهنماهای جامع، پاسخ‌های دقیق به سوالات کاربران و محتوای همیشه سبز
3️⃣
بهینه‌ سازی تجربه کاربری (UX) و رابط کاربری (UI)
🖥
✅
ناوبری ساده و کاربرپسند برای یافتن سریع اطلاعات موردنیاز
✅
دسته‌بندی شفاف محتوا و استفاده از CTA (دکمه‌های دعوت به اقدام) بهینه‌شده
✅
ایجاد تجربه‌ای یکپارچه در همه دستگاه‌ها و توجه به دسترس‌پذیری (Accessibility)
4️⃣
بهبود سرعت سایت و بهینه‌سازی عملکرد فنی
⚡️
✅
افزایش سرعت بارگذاری صفحات برای کاهش نرخ پرش (Bounce Rate)
✅
استفاده از فرمت‌های سبک‌تر تصاویر (WebP) و فشرده‌سازی کدهای CSS و JavaScript
✅
بهینه‌سازی کش سایت و استفاده از شبکه تحویل محتوا (CDN)
5️⃣
تمرکز بر بهینه‌سازی موبایل (Mobile-First SEO)
📱
✅
طراحی سایت به‌صورت Mobile-First با رعایت اصول ریسپانسیو
✅
حذف عناصر اضافی که باعث کاهش سرعت در موبایل می‌شوند
✅
تست سایت در ابزار Google Mobile-Friendly Test
6️⃣
اعتمادسازی و افزایش اعتبار سایت (E-E-A-T)
🔒
✅
نمایش نظرات مشتریان، گواهینامه‌ ها و نشان‌ های امنیتی
✅
ایجاد صفحات درباره ما و تماس با ما برای افزایش اعتبار
✅
استفاده از لینک‌ سازی داخلی و خارجی معتبر برای تقویت سیگنال‌های E-E-A-T (تجربه، تخصص، اعتبار و اعتماد)
7️⃣
سازماندهی و ساده‌ سازی محتوا برای اسکن سریع
🔍
✅
استفاده از تیترهای مناسب (H1، H2، H3) برای ساختاردهی بهتر محتوا
✅
استفاده از لیست‌های شماره‌دار و بولت پوینت‌ها برای خوانایی بهتر
✅
ایجاد بخش FAQ (سوالات متداول) و خلاصه‌های کلیدی برای کاربرانی که سریع اسکن می‌کنند
8️⃣
بهینه‌ سازی نرخ تبدیل (CRO) برای CTAها
🎯
✅
طراحی دکمه‌های دعوت به اقدام (CTA) واضح، برجسته و ترغیب‌کننده
✅
تست A/B برای بهینه‌سازی نرخ تبدیل و بهبود مسیر کاربر
✅
ایجاد صفحات فرود (Landing Pages) جذاب و کاربردی
9️⃣
استفاده از داده‌ها و تحلیل مستمر برای بهبود عملکرد
📊
✅
بررسی رفتار کاربران با ابزارهای تحلیلی و شناسایی نقاط ضعف
✅
آزمایش و بهینه‌ سازی مداوم بر اساس داده‌ های به‌دست‌آمده
🔟
استفاده از مدیا و گرافیک‌ های جذاب برای تعامل بیشتر
🎨
✅
ترکیب متن با تصاویر، ویدیوها، اینفوگرافیک‌ها و نمودارها
✅
استفاده از تصاویر سبک و جذاب برای بهبود تجربه کاربری
✅
بهینه‌ سازی ویدیو ها با قابلیت نمایش سریع و کم‌حجم
⚡️
با اجرای این رویکرد، نه‌ تنها سایت شما برای کاربران مفیدتر خواهد شد، بلکه گوگل نیز به دلیل ارائه تجربه بهتر به کاربران، وبسایت شما را در رتبه‌ های بالاتر نمایش می‌دهد.
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 674 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">📢
هشدار گوگل درباره خطای "Noindex Detected" در سرچ کنسول!
🔍
گوگل اخیراً درباره خطای "Noindex Detected" در گزارش پوشش ایندکس سرچ کنسول توضیحاتی ارائه کرده است. این خطا نشان می‌دهد که گوگل یک صفحه را شناسایی کرده اما به دلیل وجود تگ noindex، آن را ایندکس نکرده است.
⚠️
چرا این اتفاق می‌افتد؟
🔹
اگر این تگ عمداً برای جلوگیری از ایندکس شدن صفحات خاص اعمال شده باشد، جای نگرانی نیست.
🔹
اما اگر ناخواسته اضافه شده باشد، ممکن است باعث حذف صفحات مهم از نتایج جستجو شود.
✅
راه‌حل‌ها برای رفع این مشکل:
1️⃣
بررسی سرچ کنسول: از ابزار URL Inspection استفاده کنید تا ببینید آیا صفحه موردنظر دارای تگ noindex است یا خیر.
2️⃣
حذف تگ noindex: اگر صفحه باید ایندکس شود، تگ noindex را از بخش هد (head) HTML حذف کنید.
3️⃣
بررسی فایل robots.txt: از آنجایی که گوگل دیگر از دستور noindex در فایل robots.txt پشتیبانی نمی‌کند، نباید از این روش برای جلوگیری از ایندکس استفاده کنید.
4️⃣
کنترل متا تگ‌ها و هدرهای HTTP: برخی مواقع، دستور noindex در هدرهای HTTP تنظیم شده است. مطمئن شوید که این تگ به‌طور تصادفی در تنظیمات سرور اعمال نشده باشد.
5️⃣
بررسی دستورات جاوااسکریپت: برخی اسکریپت‌های جاوااسکریپت می‌توانند به‌طور دینامیکی تگ noindex را به صفحه اضافه کنند. بررسی کنید که کدهای جاوااسکریپت باعث این مشکل نشده باشند.
6️⃣
بررسی تنظیمات سیستم مدیریت محتوا (CMS): برخی CMSها مانند وردپرس، جوملا و دروپال ممکن است گزینه‌هایی برای جلوگیری از ایندکس شدن صفحات داشته باشند. این تنظیمات را چک کنید.
7️⃣
بررسی تأثیر CDNها مانند Cloudflare: برخی شبکه‌های تحویل محتوا (CDN) مانند Cloudflare ممکن است بر نحوه ایندکس شدن صفحات تأثیر بگذارند. پیشنهاد شده است که موارد زیر بررسی شوند:
🔸
بررسی Transform Rules: ممکن است تنظیماتی وجود داشته باشد که محتوای صفحه را برای گوگل تغییر دهد.
🔸
بررسی (Response Headers): بررسی کنید که Cloudflare تگ noindex را در هدرهای HTTP اعمال نکرده باشد.
🔸
بررسی کش (Cache): گاهی اوقات کش Cloudflare نسخه‌ای از صفحه را به گوگل نمایش می‌دهد که دارای noindex است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 675 · <a href="https://t.me/danialtaherifar/834" target="_blank">📅 14:38 · 11 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpyZqb87kbKSTpQF8XnnLMod9WUL3O9MjNPSorRlvRLcdJ_RZIw9fNVuT2d7nsZL6SRoFRjaxiFmxiRAQ-33Bucuq6PH__AoB3xN2pRUKwD8bxiUMMvZdbMpPUkVjqY69pzNeGRvZbG1LE05c_VpKbDKTWms1uRHtbOcEfR6VO9p2aFreJszxdSIIc49W28dvWNCc0JMeKOcQqRaJ_GhDLjGc46Z-_QFuiWYzz4nl_FLCRFxDUn9ZjH5S6f1nQlZW1mz9vKIKlJ_IXMt_IvGlyhNe5usBmvWyg_C9gACx07dYq4KQxgsvM2be5rj9_KIsOvfFcbh3SjYmDZLcs2j0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نرخ‌ ایندکس شدن صفحات در گوگل بهبود یافته است!
🚀
📈
داده‌های جدید نشان می‌دهد که گوگل در حال ایندکس کردن صفحات بیشتری است.
این تحقیق که بر روی بیش از ۱۶ میلیون صفحه وب انجام شده، نشان می‌دهد که نرخ ایندکس شدن گوگل بهبود یافته، اما هنوز بسیاری از صفحات ایندکس نمی‌شوند و بیش از ۲۰٪ از صفحات نهایتاً از ایندکس خارج می‌شوند.
🔍
آیا صفحات شما ایندکس نمی‌شوند؟
اگر صفحات شما در مدت ۶ ماه ایندکس نشده‌اند، احتمالاً دیگر ایندکس نخواهند شد.
🔧
ابزار IndexCheckr
که برای نظارت بر وضعیت ایندکس صفحات طراحی شده، به وب‌سایت‌ها این امکان را می‌دهد که به‌روزرسانی‌های مربوط به ایندکس صفحات خود را دریافت کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 660 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rX09quW4WpA384plKtI-Xe2JVixvXHYd8q0bw0b3k3n_KK6bObSLsd8KE_O064cSzTaOKgjC7DuHR48d222Ep1UDN3K0d0jSx2M1vwb6va3KhtagV_2hL1CugYdNeUui8fRcUAlHGt039ezU5W6EegGEoEwWqOCNKpS4NHrWYo5n7C4izYt6fwV2P-N6lFPVb8BrNbUmAMR_rxRVuTr7G7eM_S_ZAKWnjh39wDsY6PPtAgcn2B9eromHFK6LfrkaHnKUwfAJDIGpcHWBgFVkXZuj3vaEvbnI-RGwYfErVdFM0kGdqWqMeD1yJPzbnzlpoWWVBwqL8Im3ALkhw--Ysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل نسخه جدید Google Ads API v19 را منتشر کرد!
🚀
🔹
ویژگی‌ های جدید و تغییرات مهم:
👇
✅
🎥
تولید خودکار ویدیوهای بهبودیافته برای کمپین‌های Performance Max – ایجاد ویدیوهای با کیفیت بالا به‌صورت خودکار
🎬
✅
🗑
حذف موجودیت‌های مرتبط با فید – استفاده از دارایی‌ ها (assets) به‌جای Feed، FeedMapping و FeedService
📂
✅
🖼
پشتیبانی از تصاویر پرتره ۹:۱۶ در تبلیغات Demand Gen – نمایش بهتر تبلیغات در فرمت عمودی
📱
✅
🔗
بهبود DataLinkService – امکان به‌روزرسانی و حذف لینک‌های داده‌ای یوتیوب
🎥
✅
✈️
هدف‌گذاری برای جستجوهای سفر در همان روز – جذب کاربران برنامه‌ریز لحظه آخری!
⏳
✅
🚫
حذف پشتیبانی از VIDEO_OUTSTREAM – این نوع تبلیغ دیگر در API موجود نیست
❌
✅
🎨
به‌روزرسانی دستورالعمل‌های برند در Performance Max – قابلیت تنظیم رنگ‌ها، فونت‌ها و سایر ویژگی‌های برندینگ
🎭
✅
💬
پشتیبانی از message assets – بهبود تجربه کاربران در تعاملات پیام‌ رسانی
📩
✨
این تغییرات به تبلیغ‌کنندگان و توسعه‌دهندگان کمک می‌کند تا کمپین‌های مؤثرتری اجرا کنند و نتایج بهتری بگیرند!
🚀
💰
@danialtaherifar</div>
<div class="tg-footer">👁️ 703 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=r0rgrXgehpT7DcJgwmAzajEBBnVPaFSZKaAVgrVNM3RHq6KAyW6g6mliKcxTS5Xgz2pZ3f3X-AloPVxEjpD8dFKz86tOmAoXNtozLI8b9oJDIVjn_5-2puSAjJhC8rAdILSNcJ7jJWFnTwsgE66qRZSDVdQLA81HzujfERgT7qXJQ94Chz-0i4XppmGxHm8euC6XYGUWN89t5giKMRCrl6gVDyIGtn_3x9T6Fq4jyrhQOs807TU0_59_AC5zFTUZKh_9ZgdyfnQXPuB9gs8QSGfedMV_symLOgLA2itIpxzYt_C53-dRV8NqSNu_aKemDaMY0UdFTWFjw1n9acohDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=r0rgrXgehpT7DcJgwmAzajEBBnVPaFSZKaAVgrVNM3RHq6KAyW6g6mliKcxTS5Xgz2pZ3f3X-AloPVxEjpD8dFKz86tOmAoXNtozLI8b9oJDIVjn_5-2puSAjJhC8rAdILSNcJ7jJWFnTwsgE66qRZSDVdQLA81HzujfERgT7qXJQ94Chz-0i4XppmGxHm8euC6XYGUWN89t5giKMRCrl6gVDyIGtn_3x9T6Fq4jyrhQOs807TU0_59_AC5zFTUZKh_9ZgdyfnQXPuB9gs8QSGfedMV_symLOgLA2itIpxzYt_C53-dRV8NqSNu_aKemDaMY0UdFTWFjw1n9acohDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
گوگل با ۶۰ لینک در AI Overview!  آیا کسی روی لینک های پیشنهادی کلیک می‌کند؟
چند هفته پیش گزارش شد که گوگل در حال آزمایش AI Overviews جدیدی است که با Gemini 2.0 تقویت شده و شامل بیش از ۶۰ لینک می‌باشد!
😱
در روزهای اخیر، کاربران بیشتری این تغییر را مشاهده کرده‌اند، اما سؤال مهم اینجاست:
📌
آیا کسی حاضر است روی این ده‌ ها لینک کلیک کند؟
📢
وقتی AI Overview فقط ۳ تا ۵ لینک دارد، ممکن است کاربران یکی از آن‌ ها را باز کنند، اما وقتی تعداد لینک‌ ها ۴۰، ۵۰ یا حتی ۶۰ عدد باشد، تعداد کلیک بر روی لینک های پیشنهادی ممکن است به صفر برسد !
🤔
به نظر شما این تغییر به نفع سئو است یا به ضرر آن !
@danialtaherifar</div>
<div class="tg-footer">👁️ 834 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP1YWY_vYIgXQjN_e-Ofe0bgCLGGHynN7i7uCob3Ung2MhMB0bFUX7MMG5nQ-sauLrq6vZjdwvpeehPYfa7PXGblMhJDOrgqRESu4yLElQakzxiEVNksL3mjA6JvKFgC0jisHdQzr07PkZcYvRJpaaNSV2bLLCIuNtgpIpC-bilnm4I16GwXqTuSsHCsGzNSu2Xm_kFY02AZfwoD7RKhSYQFsQOhvgCI29VFB1lKsvEirfAPOEb-7PQFFcWFwaYqdBsDcPInSbvgAYBbb9PtoWMkNU2NNU4NuPE8fHCOY3_u8AkVnQYyuLQik2akRToOWfnipKGHDLiDr_G49LHAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زلزله در نتایج جستجوی گوگل ! تغییرات جدید در رتبه‌ بندی
🔥
📢
نشانه‌هایی از یک آپدیت جدید در الگوریتم گوگل!
🔎
ابزارهای مانند Semrush، Mozcast و Advanced Web Rankings تغییرات شدیدی در رتبه‌بندی‌ها را گزارش کرده‌اند.
📉
برخی از وبمسترها از افت ناگهانی ترافیک شکایت دارند، در حالی که برخی دیگر شاهد افزایش ایمپرشن اما کاهش کلیک‌ ها هستند!
👀
هنوز تایید رسمی وجود ندارد، اما همه چیز نشان می‌دهد که گوگل دوباره دست به تغییرات اساسی زده است.
📌
شما هم تغییراتی در سایت خود داشتید ؟
@danialtaherifar</div>
<div class="tg-footer">👁️ 877 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
چطور محتوای خودمون رو برای گوگل دیسکاور بهینه کنیم؟
گوگل دیسکاور ماهانه بیش از ۸۰۰ میلیون کاربر فعال داره! حالا تصور کن اگر وب‌سایتت توی دیسکاور نمایش داده بشه، چه حجم ترافیکی می‌تونه جذب کنه!
😍
اما چالش اینجاست که هیچ راه قطعی و تضمینی برای ورود به Google Discover وجود نداره. با این حال، گوگل یه سری نکات رو معرفی کرده که می‌تونن شانس نمایش محتوای شما توی دیسکاور رو افزایش بدن. بیاید ببینیم این نکات چی هستن
👇
🔹
۱. تجربه کاربری (UX) رو جدی بگیر!
متأسفانه توی خیلی از سایت‌های ایرانی به UI و UX اهمیت زیادی داده نمیشه، درحالی‌که گوگل عاشق سایت‌هایی با تجربه کاربری خوبه! پس حتماً روی طراحی و کاربرپسند بودن سایتت وقت بذار.
🔹
۲. از تصاویر باکیفیت استفاده کن
محتواهای تصویری جذاب و باکیفیت، شانس ورودت به دیسکاور رو بالا می‌برن. یه تصویر خوب می‌تونه بیشتر از هزار کلمه حرف بزنه!
📸
🔹
۳. قوانین محتوای Google Discover رو رعایت کن
گوگل دوست نداره محتواهای غیرشفاف، گول‌زننده یا پر از تبلیغات باشن. پس رعایت این موارد ضروریه:
✔️
شفافیت محتوا (Transparency)
✔️
بدون کلیک‌بیت (No Clickbait)
✔️
بدون تبلیغات بیش‌ازحد (No Excessive Ads)
✔️
بدون اطلاعات نادرست (No Misinformation)
✔️
بدون محتوای نامناسب یا جنسی (No Sexually Explicit Content)
✔️
بدون الفاظ رکیک و توهین‌آمیز (No Profanity)
🔹
۴. امنیت سایتت رو تأمین کن
🔒
سایتی که امنیتش تأیید شده باشه (مثلاً با SSL)، امتیاز بیشتری از سمت گوگل می‌گیره و اعتماد کاربران رو هم افزایش میده.
🔹
۵. سیگنال‌ های EEAT رو تقویت کن
اگر گوگل حس کنه محتوای سایتت حرفه‌ای، معتبر و قابل‌اعتماد هست، احتمال دیده شدنش توی دیسکاور خیلی بیشتر میشه.
با رعایت این نکات، می‌تونی شانس ورود محتوای سایتت به گوگل دیسکاور رو افزایش بدی و از این منبع قدرتمند، کلی ترافیک رایگان جذب کنی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/danialtaherifar/829" target="_blank">📅 11:08 · 01 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8jkTRUITB1mqeMvzkpz1nzYwEJ-SKsoqY7x2SZiTSy8OC0wS_FaQ1EHvDi1Ej_QYlupVqER2CtcnzXOVVogiXj0QzDv0mLwB3Tr7qaseibfaZwX2QoIgzzM0zn7SYfkkRuchlqiG0ef5hpwHUJTenuqyorgB_QbBqObrJ3xxvXk_ZRjLD7RXwv76oMkTgor3QsidtcEkEz9cq5Ud0l-dPS1Xct66I0l6B0qZ4n7yMiCwmSdzcBYu7fohxVhTh2aHd6vvwqNpKbHj-2oBsxJMMvgynl2vx2MwiYQ6CTTAC4kjTPmLJsaa2pxI3dZvIiAbANoMHeel8P7WNLpRxmYqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مسدود شدن اکانت آنالیتیکس سایت های ایرانی
⚠️
اطلاعیه رسمی گوگل؛
‼️
اخیراً فعالیت نامناسبی در ارتباط با حساب Google Analytics شما شناسایی کرده‌ایم. بنابراین، ما دسترسی به اکانت‌های شما را به حالت تعلیق درآورده‌ایم، و همانطور که در بخش 14 شرایط خدمات Google Analytics بیان شده است، خاتمه سرویس Google Analytics و شرایط مربوط به اکانت‌های شما را آغاز کرده‌ایم.
⛔️
نکته؛ اگر اکانت دیگر سایت های شما مسدود نشده، در تنظیمات اکانت تایم زون رو روی کشورهای همسایه قرار بدید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/828" target="_blank">📅 23:54 · 20 Dey 1403</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GoogleBot-ips.json</div>
  <div class="tg-doc-extra">16.2 KB</div>
</div>
<a href="https://t.me/danialtaherifar/827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
لیست آیپی های گوگل بات، آپدیت 8 اکتبر
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/danialtaherifar/827" target="_blank">📅 12:50 · 22 Mehr 1403</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzF87yVV3cOYcLQhSxgAsqwmtYygf50SokaB7XQDqIj6RxVHweH7SShq3P1mVwmpjRwPq4uZJwygCLHFuMDEvZ2svteIUw51Q8xQIE7Z8rXRqzCweciFetK-NoA01MgUkLtsX4EJDdnMMt6sEMRC5KGvbwDxf5wd6F0qDRvtskRamKNPWJJjUBgEdlUKk-Gc0emVe3CIlCjriD_kvI7uaHUVtcxJ2JJsfTyEIa-lEEhtmbGr2ib7nLmtkXwjuzW0OSxIKArC3qdnLNDqv6lM78P2MstEGRdl4gp9fi1rnBKjAZ3zRCpoB-RzJIijSEhArS1WhrEhydMEEwnIK1isLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HtG04UObm2IlSD5qFM-izh32EFISCTu-y3wut_kSiDT9Ppr0a9ghuaXNqieZe0bbtG2219tIxDSIoI-ILL5X6sZrHM1-FrmkXHls5lFRLd8G3jdPysjrHPv6-z33NwUQkX3E4K0YzQVK3Jt3IQm-CFlbB5B81eAX_Qp5m50QGoHG2ps27L6OiGWCw79Qd_mt1RPTW6wu7X666k_w_tEUMdLt1UgUG1b5lB2NR4hDRJlRyyR9NGWwE_uv_glOm4hbUOP-7ZH5zHhZq_fSLG4OKffv0WOdSBb-64FOQfs8kxAqby7IQYdy0J8AdvJO5NZcP7AZgox1AJlFkHQmQRp-TQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
گوگل در حال تست نمایش قالب ویدیویی جدید در نتایج جستجو است
♨️
در این تست گوگل، باکس ویدیو ها و تصاویر آن کوچک تر نمایش داده میشود.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/danialtaherifar/825" target="_blank">📅 11:21 · 23 Tir 1403</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Et-SCNMwsM7o__WESIUoRO2V8nFlilbiyDjHT_Xyk0R3TP3DTcgWGgjyggh_InpnLVNI9ncbJyih0NbknG0lrfnrByp_AP-BSPuQiE8HiLpxV1qN2hwM8fW3xbUWU4ePb075HINPgoydHIsm9W7DGtxIpPURa-KoZQ0La4Y3OcLH3RvCB0cg1Yw896ly_wcDTdCTihlIwVPntfQAVHJFiEQtuVlpNHvIPwRjZJhp-51N-7XLy6YU3CGtIXR9Y4LnwjOGNVH0OS5CBEjMmvRv36jsNsP4_bl766jUxlQuexj8IOl7ksb152dzx_xIQVE44CumdArqkq8BkWXYh4RaYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GvAKuCJOPRCUDAArJYBgT_OiYkh0_d7udZPYBTOqPVm8M8HxNT7EO8lhB0vOqmz3dD_ghX6_fInwnb0KtChw2Kz7CKrsff9EAYPKIH_5WMytA_QYEjRaNuHLY5ux0RoEJ0Sctg_sKF41ijI618qI_4Sc9kXP8zLUEfRZIJnKrj9mCsFA6SXfQGT6QyIYpD5tKDeER2IFj1YzaduO6MMDVI5AZVEdeWFsRnHySj20pQ2MFCgEs8VZxUamCVKPC2s4wTRRfOLCU-30kxPFYKH9WOdq7Tiu6ekdjeVeGHrgGozPp4v-oxA-XXbd3R4mNCrpDbGpfUUvC8mUhWJgIeprAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rfITugn4JH7B3DUhVxYpZZymLTdIBZqVZwiPHsGHkeGHnTkW5N6MwB7FSVohPbZpdb7m_NdHSAx6E-rRxWi8luzfv6QdrunLRo6GImyIbK297Jfkab9_O2N4Ygu3wA5Jwl8qfz8G8k3kpJ1YXh9tG_79NUWJr3fs0syP5MIc6zqnz0bVFUMBHNmesXUolhLMd2EHYUWoHk4NZNXlnaVNiQvy4OL_folKm9aXdNVJiA3Su5H3BNn-jzu-2NA8Z0qVmTl8KY_QeCk12HGO5_kO5d0StxDFI_mfkx7ozjxrH3HafqekNMINMTU6iPPQ2d4OqJh_jrSR4jVqOsnwUYrkSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=R6xtkX6ehh4KFnOpPi2fekWUPuN6obNkrq_6IXDgXb7AdJldesJ-1OIaTVMCpffjSNwd0cX4XS-IgE4YCBIqqpLz2PWUHtUqhIv2nCxWw60IDDE8T7vB3bFJHOkvjDeedsi7XtLCSsxQApY8kyUaGPE75EgT-bHguNU2VgA15YhbIO2RR5mwDXhdMSOOJ5GrcGnbRvicJq6j2YiluRqZrUBr90T-HZVedlhENwl6jimYBRV9gj956muzZqEgr7fGHpX-1m2jTtsyZOuQmViGgf5zuv1r7Tuub0sUPrjMkt3CpAbVZ2Mk80i_TePjRjdwIvkJ_CqsMiO583GI5Qpw70YRPfIPGuI4f_Z0PPm_dZAbsmXxDWdzLrs5fySx7UWrJwJq_9IBQKSCaRKUHYN7-YlbiCeFZ9gzwxF-bWUohhT6auARyx8oZV8ojVz0GorvOUVUu1zD6LrPPatFX3y1mjc8hDNBPJ3SU1gaPxKAQeDRsdbbOFyhziwHOHfVzT_EsTeBsjqgVLm8bGVKhHRHRWMDpScPOKN2aDwXek3MlYL2PE9MQUcAuN-CpJJoCiRWc4VJ4tlmEw5Z-7e0rEQ2c-xXLzMsiC5AcaOFEsS14aJRDVXVmTgH4xNmgX9VLs1xgjgX3zveHWHFdBLLiI-VAFYAMT3ilQ2FuHvsXeWq3QY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=R6xtkX6ehh4KFnOpPi2fekWUPuN6obNkrq_6IXDgXb7AdJldesJ-1OIaTVMCpffjSNwd0cX4XS-IgE4YCBIqqpLz2PWUHtUqhIv2nCxWw60IDDE8T7vB3bFJHOkvjDeedsi7XtLCSsxQApY8kyUaGPE75EgT-bHguNU2VgA15YhbIO2RR5mwDXhdMSOOJ5GrcGnbRvicJq6j2YiluRqZrUBr90T-HZVedlhENwl6jimYBRV9gj956muzZqEgr7fGHpX-1m2jTtsyZOuQmViGgf5zuv1r7Tuub0sUPrjMkt3CpAbVZ2Mk80i_TePjRjdwIvkJ_CqsMiO583GI5Qpw70YRPfIPGuI4f_Z0PPm_dZAbsmXxDWdzLrs5fySx7UWrJwJq_9IBQKSCaRKUHYN7-YlbiCeFZ9gzwxF-bWUohhT6auARyx8oZV8ojVz0GorvOUVUu1zD6LrPPatFX3y1mjc8hDNBPJ3SU1gaPxKAQeDRsdbbOFyhziwHOHfVzT_EsTeBsjqgVLm8bGVKhHRHRWMDpScPOKN2aDwXek3MlYL2PE9MQUcAuN-CpJJoCiRWc4VJ4tlmEw5Z-7e0rEQ2c-xXLzMsiC5AcaOFEsS14aJRDVXVmTgH4xNmgX9VLs1xgjgX3zveHWHFdBLLiI-VAFYAMT3ilQ2FuHvsXeWq3QY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
فاکتور های رتبه بندی گوگل لو رفت !
🗣️
این فاکتور های رتبه بندی توسط یک فرد ناشناس در گیت هاب منتشر شده است و میتوان به نحوه عملکرد الگوریتم های گوگل از طریق API های منتشر شده به آن دسترسی داشت.
⚠️
بسیاری از موارد لو رفته جز فاکتورهای رتبه بندی هستند و برخی نیز اهمیت چندانی ندارند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/danialtaherifar/821" target="_blank">📅 11:48 · 09 Khordad 1403</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
