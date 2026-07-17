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
<img src="https://cdn4.telesco.pe/file/hRA-yy2z1xsttE8UfTRsPNNhCW3YCxXMZQuS3SYYZpDill1UePDIYG85tICv4xY5fKsob1EErIml2n055lz98Q_WSnKvpJWn8QgtzG3tDYSfq5CQxMPwN4ErpXZ175Ahs88t_U2Y3JNH9cWSYSJcVjbHKv36HB_eK-wYBEY1QH4agsE0-Tpx0AyXaFaxOOs2bAFbUu53YjWUYLfpCP3RS0xdZEgXslzzYb-DEpyZWBIK0FdUHV-4451j5z6L8cT_sLzWulUHHsflCVnfjX_8pVRtGqCJjz0n7wcrGmImVLmnJYGoAQG8mSdh76zIgLdRI7pQ8F8_qBEnJCA6bANSWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 04:27:25</div>
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
<div class="tg-footer">👁️ 112 · <a href="https://t.me/danialtaherifar/944" target="_blank">📅 01:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-943">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_FAkdHvNreoZ9wY9xvqudm3hgHBk9ARvXa_VuhvYhmxx1YVQED0j1lQDkBXXTEN3rR9OzxsMhjmi3tGtx5jUDT4-DFL794lU3PskwY_-sT-n5x14y62Ots0o2P0XUttBCqYhjoQbTP6vIIVo8q3IwLagG8WdBQ8sncKNXsEK6g_Oc_XM_-_WJFKZALbXneMecoyXe-kU06poiTJHvjGo7l6z1-v39tK18DesQe4D46gIkktNvnJxgKHu3ldvCdsmJeeNFlj-GgvzNdSgMEVMFT8mtzWYGjoKiCKd2QKaUxRnWobly-frwXB1PHdCegS4EA0iH0WsC5zoIuxHAZ0bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از ظهر امروز اوضاع نت اصلا خوب نیست و رو به بدتر رفتن هم رفته
کارای مهمتون رو انجام بدین، احتمال هر شرایطی هست مجددا
@danialtaherifar</div>
<div class="tg-footer">👁️ 184 · <a href="https://t.me/danialtaherifar/943" target="_blank">📅 00:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-942">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">باز بریم بک آپ سایت هارو بگیریم :/
@danialtaherifar</div>
<div class="tg-footer">👁️ 393 · <a href="https://t.me/danialtaherifar/942" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 446 · <a href="https://t.me/danialtaherifar/941" target="_blank">📅 10:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
اگر از claude استفاده می کنید و اشتراک تهیه کردید، موارد امنیتی رو تا حد ممکن رعایت کنید
بن شدن اکانت ها شروع شده.
پ.ن: اکانت اصلی خودم پرپر شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 626 · <a href="https://t.me/danialtaherifar/939" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_Eka-TBoJRzCXRCYNY1PHRILnE3zwyUSSMP9ZsHp379kW7EXdgT3NbUpuQoy4hLrmqJ8D_LTRRbjW53OcUPkpgcupJPcbRZTtzZQRh60IOhqlEtU8sNpPLmjWVJg091l5L6IwQn4SlztCCjA2Wbb3pW8sHDDhWSYNBaIMdA_dayG433PUFTMPo9RKYBTWU_napum9U-rhaLCe03dCBlJkOqKGAiAUOyrK1kJJVF7lI2pRctEj-jIojfXNSgeplmaJBSJGr6Ii2ytIgPAXhg5b_iWBZHhdYK1V6qvI4rbFWFaRqvL_eAY-eAu577s9DrVQZwVnjcN7G_mBvKgqsFcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 819 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 922 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 946 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 940 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=CBdbyZRZgi036F3QBogMrXeOp0f97CEFHuo-i8CBpzuBzcvBtO65wQTUHYAAW54_D4u6DsOs9c4eswa25CJ14A2eLG143BWYO2IQSt2qsObO0OsfyfnkHYCMxE16nODTmjRZa7zWuvVTG4THu-KxswjoYaU9mJOknEjDbKC5s9aIhfGvE1y76YEmErmaYp-O9xPWWhYUDl64ENAjMwewvu_uyisScHu8LB4_YULi62MtCwe1qkbNvS1O8Oo5ZQLM5DSr7KX8hUGq5P0u9Vcg0hLG4EbBNZnnN5kqoDXzX52YirVnh61pLyZImagv1EuDdUINaEFtKaUHy_UW-c7oOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=CBdbyZRZgi036F3QBogMrXeOp0f97CEFHuo-i8CBpzuBzcvBtO65wQTUHYAAW54_D4u6DsOs9c4eswa25CJ14A2eLG143BWYO2IQSt2qsObO0OsfyfnkHYCMxE16nODTmjRZa7zWuvVTG4THu-KxswjoYaU9mJOknEjDbKC5s9aIhfGvE1y76YEmErmaYp-O9xPWWhYUDl64ENAjMwewvu_uyisScHu8LB4_YULi62MtCwe1qkbNvS1O8Oo5ZQLM5DSr7KX8hUGq5P0u9Vcg0hLG4EbBNZnnN5kqoDXzX52YirVnh61pLyZImagv1EuDdUINaEFtKaUHy_UW-c7oOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 934 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hT3blrJMO6GCYzYJPSkLTuIOMEph-FhYsSfXeTRDfUGzvIMSs4GJVpMqd9UrKNNT0BKaLHE7fwoj861xPxfAfbR-VO-Swbp2rbBum3SuWGXRhQ0D07d4oaoi920M-G-hWv_tT2i_63aMos0_iGjgnbVtTVAZrFe8rPNaPh3EECIodfyHWn3Fzk1AQNmsdlzAKOh_fV6E4gPSBPqTEMm-Nl9TzKIKzsyv-K3xIc76jj_M3CpwIyD1KOsyQnnCaDILsYTD30ZUkpD0-jOpxwRO6XEWB0y3sF9SDRk17JpJNRiYVOSvDqV9BRvv3mfEMG5kXQBN-CJ-R0BLztNtmWOx2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 753 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 763 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 922 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOZSVo5y1cIAabMUJCfZaKvCj_t20Sa5-zzmrtabsCBSEq7Kb5LajnthHlYcOMV4Dx9tLRG3u2ipaLy0oZ2RHH4AD_gQNwW6Tmh4x0su9htZt30ThF4CDwAMkvcvDcF5wdVpzFVvpkP6EpAfYypQ9ZDoOkWXf6upvZ6A2MSCb3slPjATlePEVwSke993GTnLtxRyvZ6qKbm2DRq3ji_n4s-8FMLs3rL3q0wsYxyXCFrhDSiJdzKjUwPtKzABoXXxQLXEu3JewVqUIELgNHaQg7p00e0b5enTaQxercwmNn1x_MYZ76xL1_a23L8Bn-HmZGQAmDsqjTuF-oofr_mLEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omKI1CkP4M722DKHDvF8yAjdaVKTyc39ZUJ5BAgpCo3joHOs3_00KH9UoDf7i1WA9EzD7zKGVxvIg4mt-iLFmxLbWou_jty9fHYDF7iJGDJDSQBIqXST0MqnDQLcoyizJbHnLMkjKgy3xezHVS7QigstlfQ7cZFdIl9TsJYlaXVug7eFTtAipx0wCwzcRljmz-Em60WWfzuGrBxFlWW3b4O2hbEaDpH4WK0Iajupj96A3Y2laK6PzHNx70lknmvyc2DO0NCSeUiJTPgyZU5xVJMNUNGX1dnyCVuyzMf1evqFTHXwZDRmi0cc7L3KHRtNfaC-PVVGliSjyR_NuaLmAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZl8CvjHbCGy8wza4OWkN6nw45QYOhVFu5wL47UaQypBcx7-V07seKTOkv86GTPi5F0wnr25KeLOdP2jdveTQUHRj0W6HIbL775wsnSX9s4LLRssRQ0MYbQn0nWL7u7O6Loz5qZOPMqdt6ExY5cbq3J8MYIc9alAju6wGz2RUhM1BGYvc5iXcrzaXg90_HHiGmz4Fgskzy5KqNdHnYr4npsXt95uLPX5KROgLPNlLwMx5uXDxdaZUj_36Ph4Ge8FgHoCOdZFOSWhNkf1OIkCfE6ZHBrkDshBjnj_u1Fb-1CrFY9lYi2QuHLwsBxymGWdTfyaqDnAfYIozzx2vctHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gp74IViH0Ah34d_4qi7_SOS2FyDF2R4jFIUaLX_9AQLVaMYwabSlg6KkFALubM1mqZIyj-CYSSPSyOqN26LdhA5M29yMbht-Vll19UEaEUt9odsemYBHpZP_OI3fygQ6EoN364OMWxgBoKhQHnpfVKDcDC0w5qsI_iGkdfcwt1vHXNJerhciCqyASGrUqGCR3EFJp3zhnuYQjimKVDZ6qe_yY1BJAJ1pIfGYYf6VHCWSnnCC6yr7UUzTvEKfbVC2_5ePUgR1wYQNA4VU1VaykHtQSs35C2sWr72wFwF9zhLclfJa-zUulfb75J4pdcY3L7EnzRoK6ACjesjREF6ObA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOwBweF-mbqxeVK9UtIwENhSTrn1r-91_99-fAkB1AIKTzuxXXFmf1R1bAayRh0Og1xnLdduxZF0iMz4RIOzBpsP3T9irgTuEVEGpIgB8SK4Ti-6WWi88inSi3Zc72yLJwicdgSo9dXYhWa3K6LbVHjsudKilwRm9ilAHhsJDiYgh92NkAns2HARjP7M-kB78b6daxal4pUxc1a_8OQLKLXNJ_0VSdPH0zZq_VVShs-CVrA__LTHSfAqclnowcoKblhPGjdDWhJLP_HYslMn5qtULtDgiw7C5XRg824wSHUUjb7t5RKjJ5DYsReq49qkDeWyhiLWgIfMkPbNfSFhWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-footer">👁️ 925 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 984 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2Hu7DfMwXC5Ahobzv_pk3rEvX2KAY-ofyPdwNTBa0lBV-dB7FIgvuwz5wCJ55EPPXUbnJ6Ss7_dxKgIwGjtEuYL0tpjHD8mTYmsoM--ewGHdwy3H6r5GpFIxiusVwP1t38fkdJVPDj6mR4tRRq7ZTonra7IIO70Qylbj2ViLn6YuRIc_fu-Ta1K4S6JOXjx4JCprxLWeg8Ghs1XGsaY3kBLCADPEJxHXLL7leH_mQjSm-oDmqfGKfdsCtmdjwKSPhBt5qq7yQ-z4VDW9uV81767-IZDhfKUv870Py6uwhpQ26B1mshZDTVvv0JUXoB5oSEqnyjVcEqes1sJrrbvhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GPHXy3qVB9AvtUzeGgZ8P7NZC5VdVscAfLxAtGB8eG5LuqHc_37XXMJf1bXR6QZQBkH9GLI1IQGP7LUh6vgqzsA2UZ8S7D6GDh5d3tugutsn8SgFx73taX3JrtiwR8TU1D-OiO74Hb1fI7OzC_tKFjBPEZ12hQB8mhNuW2_TkVRfsMZRY--49ISrL3rK-ucgk-MwOMfz716vwyNI_e-x-36PH426h_Cpw2lrJseAMlnaYCWvEbUxMpU5BgyeuHEVlp5l3dGVDsDNseoi2YRmxschf9OoBN_Wq93k49Hg9ShwA0n1a9JveDAjh0Ty_l7NKhM6YCoQLy8gAWfWhkC8YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UgfULH2ycuImZfixYuPoB-RcMVSivYlLVpwXv_xOt6mBpVwrbcpjVeo8zsZEbHNtV1KmahoZHz8YnCd61mkQ-wX4RMyWiaDGG0ip4P2wRFeDb1ctKBhEjvHBChIHZxT6CdB5vo5FYwrEQgd6N6nd0NWk3O0157fKNnxS1Zx9TnYuha2TamqIqm2m-_SaHVRouXfKltfpP4acCq-NutIGifyYT_bKUjfAc34EJ1inQ4_MErQcv0xrrdRJhEZRmRq_851YYpNZu_CQqFGWwBySmUg9WYyDqGh6pgVQ4d0YkJ_EG9TWCOajjmRf-afir0m5-UkvnTVkiP39gvfWZMjyFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rP7WgN5sB0buwMLaqsXNTL-up9q230qc-63gsrK2uYOum_VW7G_bHXss7Rtrh_knyIzld24_xRGn70gBjq2bg2xvZfQ22yykoAQ0OcQQ3y-I-Ht0mHXoeBKYQTiB7MjGFJ38eKfbmj46c5OlqUqK291wEyKXOS4yfOTTMKifrhQS-lgeNSboH8auiCWOkuIjKWIsGqbRR61M_iSs_TU5UkwhkvjZg1OtdR07ErjfEmkw9krfCcsteltSFz6eRXhHhkeehumygV6MNvoS1OB4ehHqcTXb7HP2P6TsnVy4GZe_Yb3ePLkzxQaUuImiIHI23cf0eh80BcXAAbqdAClS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 897 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
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
<div class="tg-footer">👁️ 977 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 850 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 692 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 918 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0gf5ZuSU-GJHLtGgHKDIKwVMCJQqgLix0SJLbT3tQngQWY7Oo4XbfRDC7du8lEwQYKtfoVHNMcYGccQjh7ATMEuEjlGUmZP-eyQxwFxQFeKpZhbME608g_IXYHxsmauiJr2dVkqx543Gmr5p2-yADEuA07tUAYCJ6xBMGn4--N3TyjnsSkDx6bS13MyHvdqbXKqV15Y8wQLo7m3FT9wudmYsVf4ZPJqCgpRavkKQsFEAxFfpnvwVcE7AupjGpvb1zsVpjKSWv8QozfdaZrg1a1eWIbTb3bvqgYMYxMVBE4uZudEjM0bqo31v1IVMioOhO9aRnxtIDVaKCUey6xEwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVyXjC8ucSckvQIBi08BBdC8R2cGAJWg0pA5AjVbcyYlgz5q2McXR1RChZS7dwfsjUtjK_gwRVaVphM4kRBhPFW_ixkbNg4B68e_aqcVRHH2xFN6aHnARF_nVi7Q9sXOy_DfwWIiw3HNIKyK5s2YYZEGzp8ycFSOZqLsrwLDUhJem7A4LIJTSDbijPRRyvH-SBqr1655etudYMudt7hcoL33r8q93Q66-79JOQNfbAhQCPsQHZqAEebqb-463Ge_BPKi2vV_8Cc2v9Yi9N1wrKeVwiC2OuSOxbz7t2SjcqXnuNwp0xwbUTRJsWhFkmI8L6q24jmVACYW694K5lmtmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5sOOt5uygU3hwJDW9Q0vXgvlvw9pDoiLowTRyX7UD66TkV_za7UAvtofJoZsxR47iTfD_0CDhMubkMu-EZCi7aWrrd4yzxwi8GKky2mbgJ2xsOJp_r1iBR4q_YWRrkE9aPdF8mh0-7_RulOSsBYM2XWW3uHV_oDQv4tWXaA2kGTOmbMnex4zJDPbyccMgOpyIsh0tn4Iti6mU1HU-o7iNJRpjbAeduE4QDUWmHEJ5LS-z9tCz4pcrZy_-Eldf01-4Wb5nwcIu50wfE-hQbsHcoK-In3St3d5sDqQjUMCADm3iHcD6W8ov6RlHfBLmAYNqY8aLfYAJzPuCIbF6d6vA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FEI5sKWPzSzWbhpd1j30TbvlNokALH6zIUhLPIdhq0ce8kfHP4PnnpZN7QAYo0NMD3YUtCmuD8meetVAHOkf3RKcsUT3f4JL-7uTzd48iF5BlA58gLlVZjitg798Yx0GzwY6x1otApyiQZBpup0aJupnlaqhOmdcz4jDviDJuOHVY9CDYNvvYnS5k4XjLVuJ13UR6g4_eDtzVUFnSTIEPbZENGMyQ8W-oFyPeBSiCej_jIN74rSQrSI5O9cp4C03eDWwNKnGGWds4x4ut7o9DYe80iIANvSwfaNP7KsAt0F-QvjAv6RG0nqbnrG1pUQ8L1c6DZAWXoNpdMGjC0JMpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kFWsSIzO4obGidnflRI81rxnbqwEQql2oVzWIU5VEKGuUvsGrjzYrv8zjgC0kKqPRYxM5SJO3pskFCWd1j4WDAr9ou2ysP9na-4YcmzKpMuTxzw_9EpBOcT0gOY_yZfLdwscE4wvooxxmLK3FvbPUoagqDQT26DOZHuz9h_3TbuQ4WfMd8fg7_w9lLbN5Ki-0sl-ivJ4ZXNLdEySR72TxTibOET9Qp9vL4cSlO3BewNtfTjLMYZc0j76Y91dXrYZu3vWY8KkfCEA1jYy7Edb_pzNgOQyRqdSfY7yA7eRtlu7gQHQ3_A5fJeFAM2_B63FgVTL0hWmN2pFzLsYfKzVMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lnf1vaAClR_VK7qB0eW2bh07DNr47XtGmaZzJslz7D13WT9hZUH45cr8yDI8cxbdWg2TQFBygbdUA_0n22U9KG3zQ7KuEWLTXeGhxyGb8Dg1iHVQ7picbvzlrxGtJ4a82ECD03uNlvUDuTg8mxPsQ2PycehUjmgarte0h07VHM56iUptFXnMNXLnfHcXIUZk6Uzh0KHqu49afXsDOBt4Qb9zUYRIeVH7dX_IMZWBr7TQYTidNfDTA3EL9wwPzuhk86vRLE_bTzbk1cm8Mo74OLUCgNRkJRjHLJFmRZ5U6QEQmFOrtcARihadMgk3N9HIIl04B3mLnhOw0aHlR5yGpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MU3syCVu4j-5HUo_wydfXg2Ra5-AiR9insCvUNIt5eC7yKMmPDLjj_X0HJ7-sOvYM3A_bx3RAK1qiWoN8kSm1DJll_2sKUQmHc4cbfaO9UgP5ZXjmJaeCkRf8HGH1v27xIVXzUGD_GRyDnPT_4lWU75S02bpSj-2tlQR5wLNDDEsKKzQKF0y6Gj58ocNkLSRnnr1bM0rlaXLCD0PuYdBGbkfC7O-Rqxv9mVBF1NXREvkDMwY6VA4F7k2wonoJz389qQJ2zfKSDHbeop3JDG-_S8vjRdeRhoPs4VeJD7_515mcx10RSTxnlwiiXgfr9fI8tESTDoIzfBIcrDNdYBDgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ms7SORQXXINesXqqm7fh4W755d0PeVKStF05LER4JC-ri4KlBiDdmsC-kQHe8r5S3Zm6emvDBVOLMZElVejaRBOd5FNrFcpXfoy895GXMU_-PWXkWQiyjEOX-HNHnWAwcBxCexU7Gm0rFMY1lOC-zM9b2OHXiRVm4gKVicMDmeLQE3NbcHOm8FtfdXtt-AC5K3COUDhgJBZ6jcvTZ5AiqdcXr1YsItFoNdsWamZB67MTgBDmSPVZqhXhC48sxJYy9jHKTLXg5ncS7cfdts659xHcnhWQuTFW3ukQ5EdUc-ByLFD5k2wHVjLpt1tDVyM1hI9OH_qUtTD9AsvLmpX1Bg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=UHRF9f-3E9SP6YFB72mHDTYoxr0CrKHS5cW6GlnXbgmCtdN8RwpUfvFNzCPFBhj81bBTkH8tNIgnIoX782GJ_jqZShP5whN8zwJbgJVFbsKdpeCTCrBpnHqWFPSXNPfPs5sltLP-alxklprwdBjmOgzn8Z1xUs6Njb7uG8gqpOZwZJ5ZrbwSD4ec-jlRtcMflmL47LbQpp8u1Xn_rzLAYE7vc5sV6by6nZ3ZojqCmc5Q94wqgmXq6m3QpiAOiAFXgCfzhg-9MoJcnqQULwcpVqa3-xE-2T216ozJwVy1Vve_kRhe9v0DTSjs8OidbIhnyVsv8vePl4YQKCk8_dlvXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=UHRF9f-3E9SP6YFB72mHDTYoxr0CrKHS5cW6GlnXbgmCtdN8RwpUfvFNzCPFBhj81bBTkH8tNIgnIoX782GJ_jqZShP5whN8zwJbgJVFbsKdpeCTCrBpnHqWFPSXNPfPs5sltLP-alxklprwdBjmOgzn8Z1xUs6Njb7uG8gqpOZwZJ5ZrbwSD4ec-jlRtcMflmL47LbQpp8u1Xn_rzLAYE7vc5sV6by6nZ3ZojqCmc5Q94wqgmXq6m3QpiAOiAFXgCfzhg-9MoJcnqQULwcpVqa3-xE-2T216ozJwVy1Vve_kRhe9v0DTSjs8OidbIhnyVsv8vePl4YQKCk8_dlvXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mX1ql9yOw7CI_UElda7MRN-GnYydQ8prw3ym7yEh0GBLSNxwRzwF6AjfqDoQ-kyH06ExmM9JE9hGyoLo3cYT1d8GxXDUx0JTdSkgfChIm__HlizT66eq8D5R-sWYkoMp2Uuo27r4J2n9sS5BG-a4plLmCyaPK9gMLBOo8AXOnCL-hN_soFUi8cGV-5zyH-ymeMKAxDTeUfuRxBzYehuXAdjcFhXsKSzMu_H2gsMqz9P6nv-IUhK16fPtg7XKOcAyQOZOAiix3jd1EbpwNig0ayIWaoZ1-c18KZRuld3VSExIVCaBrgOXnDLo2o_nyhzMMYyHhEiQtvp0JwMFHeOsaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RK3CYfYvU6OgAV9REm5o9UpOgiJ7p73Hjud1i54vHrAdIZtBBc_BAI3aCUbvcZQaizQIjBlu2mOZ68oEIIUAuApnxicPIiF9p4n_qqgAvZbXLY7RN_0oZ7y1eQFzgDgrOra4vFCefH0o56Bfiop43FHTBbXjx4uNqQk6DWHAD-1-vJZKwRmNEGWQ2ytUgOut6_KglqZCzZsh8D75Fa5pgQVykTbfPPxQZEYc9oOlcaeC6-Lc2H_O2WqxFVXH302MGWsI6bj81tlAKnboLTjtb7TEnQG_M8JPXcqnVZ0a5pGbwMPvGB3h3YOf4lpPY35FpbQTil_8XibSpMZnJ9nq6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGjybH092NZpGl26grXOaAMQbL3ienW759JCF4ZlHEA8JBTvuF1nIhFZcORx2DkPWzUwLAezRLcczqCPp38wCboklV0ttAn6aKeYhEKjtk_K6G9-El-zjXvXh4e-KLObDOZ2-BD6rX5QvFxJBrwixHQubngnkF343qzvUNPs-9glqcgiT6ATMzT9bLuN1mbGkK8fnMXhD4a7ZLue5t-TRShvwxp-GO_32BKltD1YfYoCEe8PWCf2ovNaDATcEV9BqNQ7tt_lNTWWXj70Uvb3t5d2FYQVCLucdgh09duuxUoNxVBBcUBIfnXYXUj4q5q2K-pl_WTXYGUnUtyhBoR22Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_QzD5GqSCU_hINzzcdVEH0It-IOX8grYnqHnUAImMiD1oURm8UR9yuKxN9BXGAJuFbFFuGO6VuWh6YVF3MTL-NIvtMBRij7giLhuNGqWIupxCV3LtRDale_1_agXR71swjkVxHeoahydj-cjcEsGofoHgyfS7_PlBnvhV2QTAIetaHwwWq8TRY-Eyvg-ONBOiPeb3i0hnetA67B14l2yXF7z6ApuQJmkVjk9MC3pz1Q5GeHYCIrWjR3ywoim2fUirIzlz3ivKAGvz0IjZaX8YAhvj1BohdFFTghGG23h_bx0opwhMoM7TPQQO9OdKGij9sww4PSpReV8M9mvcRE8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 805 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fytpeirKXE9eas9GcmIDad1C_WCTY65m6VEdztXEk1FC3FiXucFXxg-WwFJTf88z-pc5d2jHXnmvsG_1bA4o-M8ZteZzQ9KBvsJ4zVwQf_n2k4mophaG95mYx_tqCxtRQbM5rYRaFPRzxYINewIsHTd1HVD-Veraah-baWMM6b_ZRxKOKwh4kP-sRz0HyCbWhehoj3aS0ZbQuZH7Kh9_EcTrYg6SDA1uWeO8gL3Xsd3QYg_CO9UEy5xrEchN4Lo4GIz26kojhjbYsj1mILhOBWkaK7bm3tavGn8Twz7SA6kF1YNI2x3AXoByjox_YH507WUGkGWQZ9mumhrRL8Z8yg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Maa9JHqq-VYP86TtWsWvb9zB8bPSoeCT3V5xVllUXcgy8LrXO2H3PkomuY0QqRt-uS2HHjdx5q46ljH5_ttMUFtLhtrfQy7dAlRJ8CWkTccYpThMxYD1UPjamQPjcOtYeHJdz_ueU4dZez0MkdsBqq0c6WImAhUCv0vW-r-wSsCjhECpblaOsXKKMwO4sxcK0EWbXUtjlRRakmJPdgH8RPoOGqExekbnKeFal2mBlAPpXZw1Tcs6OKLRm8U5273m2mwiK4RQMNQEY24uqvSHNlHilVRS4n8D78BDyW4uhEP3yNMeVGyFh4oq1XLWeChuUtptvLSFpdRxOFgsXckCSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ks0ulSifHL-U9iXAYuie9HnshfQv0RxkTDMe8wIFkd85ytUn-SMuadaA-P6qwDSCL2q1Qvgv6AjK5Tt3sLpWuHie-bmWZURKgqJAx39k_yc2q6GWMKPLp74YHmFa11OML6iJjbpH0wO_eS0CgPDmQ9z54LIuJVW2XdO_3R2LEq0p1IbKxyZlsMmBeDrbHuZwDE1-Hr3QEg6yW3khEXrB79xX6p4CJGXMuCob97frTpw5JKYmyj8Ln2Je6utHKGRVB_VZgJEM-N-MmopyKji19NmJO-fW0LVBNy5L2Z76ePDXMqzVGm2KcpVC7UezYZFTJkFW0Z2w5E3x0F0XjWvqzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/goOLc1MBSIUzv4TQfvVH-orXe6tfgQ-aStxby_Ruk4P1ZGJxTGntsQs4tttGqisL6omcreuA9ShL3UlR6LRESuBAF5EPYwDTPro0D5n2EKS3dftTT-t26ge7Luw0WMkwsITWqADQZaOriCe2raAqLvqoeIA8Q1E3TDE2GmNpkkQHbyj8POSiCXWtkZs7M7cHy3lB6rm56TlsSGn_t-ze0gfV6m08S6CAO6nyTulWwGvSIUgGs0p8Y1XD5BxL_b0LzKvVfRXUesGgwgFwSpjhd0CvD1xkOOjoALIxoJtpVaXHIS4xHn-Z4hwiCFpACM1cFcrPZxLZqv6-Py5J2Pi4Kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhMB5TDwIz3De1XuZsEJV-Omy1JqbW-QHVMUmMFvQqOWwIXrWx_9Y225ae0kKlBKLCC0KfGPR_b9fS0_57zDfTwigXwiWceTn3t9Lj8SUGPb4EySGiFXiDbfohLSG7OjJ7uRS_55iNzmB6aAZl-cBn2MvmwgUQyCMs81BXMDfk-KmoHfj_bmDVSpAxKel4JafUf0qAWIiUugpoRCNOnotkMmUM12OmVBFsn8Wa9OyaTEpI73LYD9wWyPALjw4Co0BQoLBvKkBNwn55fvzynAa-jU_d6QDvyOBGYoPJUdZBFve1TOTbYT6TxluOWnnb7GlW2BbBRBzClKlZ8P-1hDhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLVoeyV-UYbD4TvPKuR85I8eUmUWW-9R_OKMbqtTarYN0dMhQ337tnBEaBFQn_niTIKsK2AoVMCuQdYF1YeJPpJLZnsjaeSCSkdT4YwPBcSVVH2uOr3BOhzDzBCCjhgmz_evDVoeD6eY0P7Nzl4v7Lt4SileIWEPsB5CnWtKdlgsABg8L2f5MpIDW4_XjTQCvExmWYe7c56bZLREHYwQ7U96Tv0Uo3_drQJZf1Yoxnh0TT_3T1-MNvciX4Y2OI9uHhVtONjrr49nBY-ab0BFxBWSZPzJka-dgZG1xa6D8woz9RgYk_SP-82OlTliWW2BM5owUdU3IqhGFPT7R3Wopg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INmP_OPMQMLHOwNZCtPL5kReMVz6OqSh_4_nLNKzCruE0vJprD0cmf2h8HyOGVQIO7CFDIxOLsGTFDSjgbg5VD7-UwRow-ZpigQqCkdnx76LLd3ApmL-FQC8VATTiaMt3HyeWHV91eVa2MA-54OBCCCMNStMlLPgdpzU2cAMvD-6zofRqU4Kk2rwZ8D4KK6c8C_oWq8w5M2TJY827my0775S8jHtleAtLq3SK7pw_8z99MY1Q9oHsUOLyAG4Tj0XbinYvR_oc0G_suNWNJNvt6G_tABUin9TmJ7r2REzt9QPDgOshP1K5ESi4G37GEV-4I6VJifSO9L8r4vYD3Uj5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRJw069gmVPUKCu7UzHB2bzWGiBx3y3Rs9zIMb9Yicrh5xL61V24FwRAkWFnAqFC7-6rPgpXMtYYE_Pu65h1FBeyStdfGxzANk1e3vxnkkEHjhU_j0lKV7ky8oLXSIoRMMuY8k7fe0oJhKUFPBspjdITE0_leV7bzdjoF7jsd9xfpZYiqcA64BI8SviOU7xMyu3HjMkiFR9p6I2MTLmFXzVgeqaK5EF89CyaPeRLYT3FRLRMYelC8nVR1SKHV3sc8aAtOM0D10l4pJTRRZbORQaleWGNyKSyDG3gyBKanliT1_0sMeuDDUhKHSAac-y22o4r6Q8kEYo-XbKqjqXQpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 643 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lUmVfdJ_uTbZV3WHQVzZApJx087NwaiKHhp2uE0_b3NXXvm2aVvYGO_H-B1Hm2umlZgYCZzF9j7GlobJn21yQcmwgpShg0qmUQ8bqi2wxZdPlFWytyZNihb6Nfz323p9I1bs8NmqIEnY2Ppyzf64lPH12MyiasJGzkLBEfoHwtUZVNLJsxU0TpJBe1MuK5n0uexNCeBMfAE9u0NiU4ig9By7HqVmYaBuOwjeKmt50Q1ijkaoAPyNX4eh-31XfK-UePhl7kl7XdNHwymQxHiuQWQCn88jROlO1DSnmqekZSIJturC8jWSL2-DXLbVr-65huXfRFp6QQOLyB6x2plpdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CmW6m14WnOLT16SPmAmd67dphVRp_Z9O2iZjfeFHWy4zLGJYsOYVZ6P-ruM_ONiP50d-E3oN5Zq6iC3WrWtOhARQnWzJ2QGCcUdBWCKoMHtKZntbazRAOYQskwHsJ3eTmPhDc-cACtT8yyooXQKSqSOfoh8yUrQurAKZsZpECaT0xslxbnbYF4SRZEh5ZfjpC2vPDpZZGGCLN6cU18uGQ3ICRKIAdUBjeB9nKkuPW0S8AZK_GGEx0UTdwB3HI7RtjOLeDB-_QkF1D1XNShRMwB93MzJ_Id4SXh2m37nU72gKOSmyEAAI8yUy6uJ7rE1seGPdgPCkOC1cE9kjKIjjpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dHYlRB1AE9yIrBmj_j8skqYHiWVFOparx4IoCCLGLODhB_vSqmixuBYYzsXxMC-ekPGDfPTBQAIcfUClPaL8y61iSy16UBR7CYqY8iHgsR4mw1gpYDDIFgHAlx6PaGLtch7EL-Ufie-zc63LcrUpstI6ziW9d1BwDL8GmFyLrfn1wWBQe1ibqvGfHJNDuGKTLd31lTOpFTrFrsfI6e6PNTC4n1f5JXcAuR8GrFYtcNWAOFKpMwvE-O4CEBrlIMFyu-T9S_1HvL6ZpVKrHaCtyKphDJ1gbf5nYD4vso59oVUkiSOMk8S48e9M6TJQzdIFSHwPUG03ohsSbJrIQd8gsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FEX52ONr1d_xhGnoZJN0607OTem8LeboSaZT_PLziB9cfPZRu7_rsYEzfnI_2EoU8wrym3tflkL-iBoQS9ADPkqIeOIfeA9kSUtm7Pmch_spe_pJRrAqRIfsMIYCYFaG0uz0PtYUeBhz1Vetore_U4NMbQhPP6s2iUijjB_K_kK0IF5p-mfGPk1Z78tNnEPKpyODG1kzP5MasE2Jdkm64M_YbtQhHHmWFjtAutOdsid_DeTHJOqVoGDv4GnGVW3OphKwyi03qemMazdl8-KEeDkR9rTt_1Y2yTrSNQfxpy-V_eZgbIdOVPrsFxN_ls_nrrgNX5KEdiWuHSyjMw38dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a4xbs0M4ME0m39Zj9gcCOaGwrwOUwoucfGQht-EiA-kBEhTV8NjlH19W-67-4GQsxMJYmqqq9Bks2TENZTWgvyaTpFLiX09S6U3RDClCeBV0ZTnJbYMFp_BTi15yNJHvD2LcLmxwhx1P0BRX6ce78WL-t9lfT5rvE27JqWRanST_EErEoJLluz_2RYr7th0iaF-TN7fG17IrE8mEeO8lE21Fd6XZkDnj2qOjHZheTDumuJLafOj8M3DTjNy9JCdu4N4ijszAZFniwWKybkvVtufqs18od6Z_jNU2uqZKwMSFOPLcc2Ao39xsjU_SNPjmV1lX1iU4TsV_2lC3jR227Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 788 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwcYU0nLLT3_QiXu9pJWk64k_2JpfIt8iA7XEVx_aWTKQYmh_qNqEbJxBsICXE3H73YXKp5HgoSeHxfWo-OE28GZkr-rBQscyZ1fjDUrnJ2q8bW4RPicAXRPqiyg1uA4Goxk5radF3aXhqk04sDJVoCRn2GpXZyMqWbvzEyx89D_gTXV3tsJtd-yuZmJolaS7OVttig8YKR3JTM2fH-yMEEa5pCFZP4nSHaOvhp4x0N4zmmKSCblYrgLYWvYUghvox4NE8PYmdwJFIChtZAJ0CAlqkTVHULDFbJl-91MIzPT0AVohopaqbLg3Xe-AKfYM6qbxT9VFDYSHMNTaioQPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxrmLsJIGLVvYIgZRbAMeqGw4tjT6HFEXNkZP6AcMDKPCOIIHDvVQeARGlo0vmEq3KuWUgmUiwPbyINU8aNAf6X8tU-Qn5QkSwZfz-_bCzAt9iBiDMI1wr2LCLQmmgq6j_g0zrTs8cerMpVWsUMZHFhUUIw5pAl4z7MiBbD_r6YzLZvkZrNrXArzOHhNrRA9RxMW0MXBQC12whylL8KpgYj0NqLvczSab_90a4mNvz_F0q3HDiFNLSShpWVAWn6pDbc82GuFzHBCNpWgbr5gEIGiz6aZjPxN0hRzxHUZx0zfGcS87lr1ytmjjdH4t-vJaxujNGExaDbyX2MjGCdmrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrKKbgpLLUzzHS_aDwb41YyyoNGSPAsxOW4O8bGegIHMWxvl75N-oyU2rzoihaFq6wLsDookOvAOb9TqiWjJFA5mxmPsdY8S8fmjcLQ2MnnlR0cSJkrf3Ny7icIDz3vxGm9j2S7zV2ftHR7VVwshdtgq5uYhOOPSBeL43vihMSFazDZJ3Y-P6B9DwPhJjYtgnxBNTic7T7-Bi7Ypt15ZmsmSh8T4LRjErGvi_z3EykmXTpf5owm6WynJteHRvEM4EWIn2xqRfJRtTD18XZJH0GF1u1LmVeR3xbmM352hLhsrdFzYXl8c78KS47p7M1zs3p2BSlNLlLNicU7MVClW5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtlYkwiU27-lE6spsw7iDvxuPnL2TzStAOQYFe9h96omK6EkaeoSie2nuPdpGzZS-5meHjK88XfmV2Q__vLHKqkWVebumi7WQM_ojXuqapqwJPo3amH1JAMjU6DpV-ZBkBa04QgGMRLPtIMc7dvbGIcQb1JPbBIQNHwTkMDIjAwspfs-a0-oLfyMdbW2SM_qbbUoImQlunGyAHMEzgfH7OjkjqG7YP_eJ2yxjjCeis1K8EARES8lhj0HtcVEJWfRN93tXbTC2FZpfCiBqcuLiWRB7_Mpp1HxZiylJSFPywSllFFYuJfbCXyAnbyKsNLm2uyzXObeptyNvaiVQYX1Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WH2mJxwa5NGs-LugcoQpA1hHxMq1pU4PcLwycAbdkIiHTcum0bwWLQPaj0RAnS9MOkpPsEO8rUIRTnOdvCmEycO06vcPANsTKVRA4F98gy7_pC54Y6yxxXbfBhpk-Z1oIBw_seeeY_PQ_nqvvxdUs41KOV6l-f5omadB2iqsaLP1ZCq7YN747n8cLOvyVdN5KhtPQujTVASf96H0VEsOflGqW0G5TfS9ApWR588RZCHhVWr2rdpp7Gm1cpnz5FjmuXtOtpWba4YfrDSr-KJtOo2NsNkjut6V53G1nxQc-oT04Qem7xFHpOxIKpzulzoRNtFhTUu7kBWc_9kA2uNHKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBiCUu5cs8dKrYezhUaW1ZuSZXnyfnSbymXN1lyrDO45_SHQWswRDKWmDbbl415p-TvT-x1bzWmYEx2CBUI7I1kX7rY3bGJvAbgLG97SVZ2796Oeo3ricjkGGqNSi5ZAXSoDAQE2DtLn8c6bLpj_sBgmWKSFXyoioeAHhH1CVHJW2Ixpz86jky8wlsvCp7nIzeZD1vGwuhDvkC4nM23n6wL1iA0PmVO3zshtRijpfiVmbdLOQQcLeB4Xrc3b0VYnYsCbF6TtkXL2MxbH5jy1L0FkiJex8LWAffC_lvARSA-y3yUN6O_6jvXdRNWgEMWgT4XFIXCllWFa0oMiIzxcag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9X0Y5iyHeJFprVdLq5PT1q_1ITYOtYwz10RvpAEHs5hSdgA5a59l-4if3-_G3pBM5t7pFRSkaJxetLhKJqEGSsJJ6a9-N3G87phcElA61KzNvA-Aa-l80jL-3D5R7gislf7APjFVdkvrMG-xHcbaALQjZidpabHVxz4NDniSlrNsufX67T3NwwED-2rb3SXPgBt2RcBzhXSJSof67sjabU9dUOW85OhlGH0WroPfYx4YLYTeCeAfkURwBX_XxqYlzaDZm_p6sTaAxooRMehorAAO7OZ08t7tFCu5_AM2tb9FKaVhzaU3BZbcBFsjAtk3dxbMrZiy3ONrMhdDv_IZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hEiq_fSYh-MYQu1AK7UHfdPPYxVTVaN94nSwwTZN_bTb0YsGs4QYrS68qZvjrEcF2giHhnswESpEdpEszvSdD9Oov5gipa71Vwh0Udbvt8i-0ErYqUKbfY8C0aO6eoEN-rImtY8zkVCH1ZgSqTQfA6Mm5lxPQNBXyGwo362ZYiiT-IfRqCfrQpWlpEhaUlC5tXv_ryKYb8wRXcnm8BhWaf9IuXSiHmEjvkqrbAzoYuxngzJqFRFq_aZNOzz2lQFZqQO8fNzi9NQynIoEUropQWK98Q7VxIIheVmoA2z1XWX5lVlg0eBrM_zdngRkiT3O920QuRMFA7cL2p-cRs07PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lGi1qkK9-Ex-jJ8A_yepqb7O-0ymohgq33-zxnL3QSS_uVSD9yFTl67E4X-jAR0IQEITzDsUq9MSRCMKb_4Qyysl_FK2bUK1SYEcP0b2PJe7iXgzzbG39YP9R_1Prx2yVRIJp4s1f6DEF2NDWwODTq56mMFU87yWzrHlUEGxCTmyf4Lq1wl3VcfEUi5Bs21WJAra9URAAQAnDyQrptEz5V7-vsT9wIYm3hegtT1JOuhz5VdPOH-ooBy-VjW74L-BRPVA0eoNGVEZh4e_ZzFuat9vLsWmzRsQMz9L2g2THS9WEBznbCiObojh7MHSPfazK1CaMNaqBEWPp3pZgvpYyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXe_n9hR7kutLSQ0DFXnGqLiEH8EhE01rjqEBKQ9lZvnlKiIZgqzrAE2iOdYVhvTPYK4T7zS2oRXKD_501noNZTv3VA0IIMoARTt4KLdqyP1dTOmKp-RVfrV_Qyu1d0rKQ8aEy5ZuPHJpnZNhQn1eK-3vRR-uCcmbshb5E1rGEycUvfLPw1qbS9vZYenLG1Wn6GdU8dmTENYmsjg1R5yxgrFhel-IZIeZC73eXITXvEWLkNOQ08ithF4EKKLqe7ha83AWsyIffBoQjnNSSVDJTzIqYWfOpMoqocz7p_WjBDJWYa00dMNi1CsX-weiVUDrNQcxV94cWEzYrAXzVYx1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpOp0aRmQ_uGR80OPegkov3Ct0A9fZvFnceTzqIr0HH24PUVQlR-kNjkKL9kCe9Hf0HkpIhL1Sds8K1sMv61PxTJD6c5B2YXOGIUQEVBFIf6Te3KbYocgXb-yzjrtgyew4_16acQ4y7jbZuoREj8WFGUDPh7-Oid1PSYuqeGzZkQx9PFb-8ygPXF0_hikc3oBySkceG_CQIZJzpY-lS9NLKonIyK0nzxhU0KS6cxbFqYJzld3Lkm3ECKChUWoLs9TYJBwfozSJSwfUssSqkErCHvDyNx-Pw3vd3XlJNQfL2YBzGnuW8gogBXtcFy4wdymxeSd2eI5js81IgwTe6GoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfPktPxWkpxoC_WXoDVXC9FTnyiEMcGs7Gpr8hOrN9qovTNZcWR6aEMVA_ZS87OOzFQkHrbjA-xE79zkg_dXn99s-cDaXgF2Jzrwoqxj7IdbGpWKhXvTCzzgPPYeTWkM5EluOBIurZysnZ08ovDsdUrTrWw9h-NfB1Bu4NIQW_a0QFVGDDTjUMhhO6FHrqeeiQ0AFpcMJsIm26fIgHLNFv2268A7Vi3tEL_WrmnRUdGHARYd2AST4QgDcyOaYVQpN4qRM2rW54L0gEI6LxpRZrLRazeq0bx9AR2RZOl-7HEQwg6fAKd1OvzivJtvbXtYwSalQjC28CumT4zUsUiy-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ie9ERLOC1YTwZ-Z_uaQlUpXeegTdz0koUFF1jz5408rRapF4Dtf5Jb6IcW6ZPbc-72yyEPbglrs0JsvJ6pYMc_LWSv31bz8FZ3Mg_M0PkYjz0vPk6PiNwqLdcY3IzTkYYcVpJsVtcTn6KI3Wnx62G_zJp2rp3Dj7rhJbDPmdF-kANv4BuF9CdlUR649I_QJ1Klq4op2onpqEAC0sTkJH4rFoNn93fxaI3Bf9Tw7FNHVIdouDTtz10qIaOqhE8arBeoy06uIm3h1bvLU8fHSb6I69epqlg41t8Oa8dtfaNp_92gWcM9068y3PxSuXFJuFY6Rw_cetmqUK_9lC9OBtLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mzha-LUJr347SyxWSmqhEDqSuWmz0tqQPxVWh8NeRl03hhLXdQLomE4thmaDXzaQQ9osRIBVBKFOEBSQhqcdgUXkf9aaop_jV999_Hen3evH44a_hgnz2o7UzuuHoZvg79T0FRt-fXOagkoHSJ8ECN-2XMgcHJSg__gCetpgYcvt7KMaJq9iEvoeWjF8OrU-LRKS4cVbUwgmFT08IdJkv_Z8QbgMDw-sw-kxrpKkGwWeu3HgYQjHHHWftAk0xTaK2CgpYkFcRRN5PbrBRns1GTdWCWrTO8cnxo7w2sOep8lzW-tHaDxEUrJoOagDy227Oiy-QJshec-gZwCL5GU4rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkpAWtAsnCT83CFDKPwPbU0Xz8Jp1L3ril1jfG7yquFkkXU8C6AgtlH9quor6ThFDjeCuEXmD_OjDkLwWz4ofzlAXehSf28ODTnn_odMu2iipR4Np5u0Kncgt4kk3ic9cU9jIgLzZJriT0RC7yIEAybkEOAR8nwoBC8GGPIgBTBkMqrfAC0aI4PRO8INtdkDwmtD0kNUCZIsH4mDni5MWE61_E5cJVJrUS6vbHUVb4xm3tSjJnA9o1a__EikmlHXiwwhY_fgsIdOz_5EiDx2R63m7Ww09E1cnKkfFlNpOF6QaBjOQbJghMSANJxGNRNpdGj6e__-pfyuNhZMcxOKbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EN5i6Mzi4DB9YtEbrL_Lb9R8AdPYh5DJQOJqvkRLTiHFa1Lk_UelaWzWu8rfJaDmB7y872rWrMUcdev0zchvjG32eyS5nyXZiW7RVWfZPNRFu3jNsHQ8pIa9eu9L86_h-oLaFM-8Z5spnbqmxJCb4cXrzQ2ba-ujuwyLqQXQX40rItThWlSo_NMmHZoh8Eq1ngnoB-lhSeWp_nS1vG8GNhCRfYeooT1KI4PiHFbcOXfuzRGDAdBGaAZREBhAHEOrDUh8Z15c6Gx6YTcTM1OhUqq3SBm3ZVtaCuW9QhCXTX1q1YNjKQVejrkQzi25mHSzp0t_FHgSw2ise4-whqhVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/INWr9Z1GOLRhBYJaP2_WoWXKLQgo5Cl_PpMSsQSg-ZYGfu1zPiKnbqkErx2nu2o1KAscoutInHsM69hKoH2taI_QAzV-7c9zl1UfvzQAvvKlKb9q7bH19ZBPaGIi3a9xUDD9GIm6Df01p_WR7OTj3HTEGROSJLKkIyW2UpcnpQZxY84vdr3sbEGc6RSqD_JCrOqRhmPPgDAevr-2F9kaAso26RN0n1Cj3p0IGlZ5mgkLtVZWX7VPYNlG2PlunsP4_t6NleT7HboweeIBCHyotnl-tfYjCGkwUpR5hwy5VSpKpAj4aYhk-E6Ug7caWYVfg4E-wMzMdVWLFQBRstnTmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drjXMUxFuIEhsSFfrC1k0yXXGHGEJI3HHdOGOv3_OZj6NOUH06-aVlVqW1LnaCf3zxilX5_c58l6z5q508otams7waCqEYERyiZk0_GqhHZkai19ctlQCR3UAJlKMnVaBRA6KBCxf0tYc7saL8C3_RguGOw2Lykum0nLsWKIq1i6zulbwhTLNfGVLGjXDMA5zHH-APWkMxy38tPSKAZFjPLB8rFbS2_0EDlYU9bXFyU6ZX80o6JJPdcq8d8NnvK4j5tRruDUerOk_PRFc0tuY61N2wuyArGM6E3RnpcwKR9FJeJpuWXIkPyGJYzmCplj9M59fJX0Ous6wQOlfTC_mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QK9dXtaHx2H-b2vuIRpaFgasZhwvbW5vWbxfdNvgkwvC2D86pTm0Uaioo6VM-J4eR7N92fqe-IWqEztN-j-EY1546vWngrLEQY5DY18kiz_idFryyncnxRjIdGZSQwLqxWxwJzc4kZjj737PfFa5l7rMMs6w7SLBt5q3jZjKH4CnsieNjVBBPK2PQospi0bsqqNMEGnHYe6Qj-E5KDNUYfvY0bpqkbQXRZT0DjnnUQhqAN-fsX4qTHjxRgjfqZYlDapXqxtKY_sZzc7A2jJ7smtQ8_e8sZ86mz4xKO9XX8IVjWmaxmo3vWGRC-O1wIqa2ZJXH6gkobtCPn6B0eGIvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EVrM9ab5LjQwgryGVaVyQvrRdEnjrnXoYx0v5ZcQRfL-x9OktYuEMr-0AiB1X6BZiER5oJru3NYS3XH-TgQ1BfKeDuAHSwJY5OpvTq6BSK_cWIHzI523cyzx__zQtjnobqYDVDfWcBX2Xh6956pWaefQAO70hftMY_Ep6a2t-HWQTdCjStaRsJ2hfm27MSdLMvP6fyz8n5-p2giOA5or6u3zqt5bzGPjcqb73AtMsdha91wxlJz8vZrPMjMZTLohkTeevUTUeZlYmZBpfkdIb6NFD92Km4eRaBVPRbyNOLfW7QVxptqDMKbvKhiZ7ym60ghOAy6p_9Zd3SKgcj3Mnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsmW7oZ976QPxMTeuTEx-jA6wnxKZcdgJcmZE2yUo1TgjbWqWaplx5IyZGgvNkIEyNg3fjDOqtTjiPTQpkqMPZ-Ut-oYClUA7LB5SohWS55bgN108J2qp_-xoa6bD9FDumplD4psC-PuU2K4XGw9n-NdZfZLjsU02QUa9MFm-YOXiKBB9AFwsnt76zsiJ4Vtu8I27ShtzYqzkZUKflS4ZawVU8V1EjJ4G-gSZPP22lnRIcKJ03lOYHJzUCrymC9V_2SQlfOMITbOH8FjIamdpND0T5xZVZC4BNae1kmAK5VAfmzo3RmHJA2OU6wuuWVLd_2gZFwIjzf59kOQoZQG0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qml0Ie-EAKvq7JVQdwE2Lt1eLBBM3XLen9jx4VBtyM1Rbq9kpHE8meyslV2RSHTclPXMDWs3Jr4-9nDSaSqBgrvT75AwI60C5ACqmxAFwpRDTadDEW4ZaZfWpwn7sBZTkAYnDx7KLNU0pmAzrwRwD0QJkyrNV6DEqfTUCzEfiHPf4Fvwr0GhrHe8StUzGnumgSjjO7HMNh_Zw4BPy1-_k--mcukzXu3DROikGB8IfEqEcRAVq242qQEWgUAyzC-RuTS-lTtuHEZC0Yq2H-K7ylXnuqrFO2i4FS7446U8sie7dsTk42LPVgmgkm6cHG4htGFM5KnXHHAfOxyDBj_jQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhHBOSDhIJczT5apzXCeJb98ZMsDTxHKGVuvAfqaCF-iRXGGeDL2OrhQm6dW8llV5ow6XWki860Z8x3B1R4skrKoDnP1N2ZdbS2tU9myQ_wt95kr_W14IG4GWSUBOOAWz96CWJ6rN-PKNIRCgYZGJg1LyAAFdG0M7D7ippqPGCHjNgohqvnVgZzniNvnVc1t2l6LJxMo2yajqoGOHpiXW8i8ItLY6vnl9ZZoMuWiILLF78YBIAsHwSMpMCnsBWL1yiS3RLOdxhlSzKyc07xZ__PbOdkgYF0FJFq7BFfRLJ0IAvz4Kc1BM4f6LjhbjWJFCu4_eHi2P3DHboC_lHqDKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/diUBV1ZHnEUVxImoAiqJhzzEAJ2p35FPB8LIofHJn9oMtNKHCRrrtfdUwANeY6xh5ajnuS4rfpMSUwJ5fjdYUXa1sMcPIjaHEdq5uvLO2c1LixoNu-KbDqkyvPndPwMcT8l_0sS9HmxPRMX7eTT-DlOLFwT5VarzWTsoaOYgc9I58ceyRTXgHpR39Z9vEfA2ApPnr2_IeBXd6XXqK8hjcXXvoSiInmcGhgVojL7DUv89vXthOB2-tm6loeIgKc7ttZBy6eLvEgtSa8FkIzISZyJfrdzHUB7H2dH2cI5_S5jwj0K2flvvQ-DighgXWQNllNTHY9vR-BFMs00QnX1G6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sp2X_24cxwZmT4ObhxeWfZkyNvN4gVkmCW4Xg3379i6E9p8LnLRS8AjaLMWdkMpnAPuN6Y9uMdCAydgdxnQ1qRYw1ug7IxQVnf6vLCuNyyOQkD9lvTbLV28JS7AhF9KWHUwOOv2d0XzE-xnse0t9hWcBoPRZCUjgfyqbhsfvYivYHzrb6VDnglWWgw_hstwATqcpIvQhbqvLngB7sl-0FZqtewfHsOQqe8SbsnFz2OBOJCixv5B4EXwQJf1kOYcQ-71MzciXQDeVE6yxU-FG-gU6mkDlH3jRH9-UUty7XQ_0Q8nso9zVCaDVJ8E7ieTHDAX3jHNXKHKKGUoN0Rue9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMko633QU__uJfwzYzBODV86814cicygZSGWc8xVQ89rwturiIdQ6f5YbmPMaBJkLuInROSxXKjx8zLnlnPIhxuaAdGMDryDdJPqMilPuIsuqCubWGYgrTXvy-mjvJUL3bBgsnV-_NG6mkJc50dy_c1qnByFfLdTggD_h9jtk4K-tLe3euw0L-t7gJxkQQX2lAF0OUo-_jA4MOv0MF511j-0Ky_NTsWjP40nf82EI5BAyYB059sRzyZ597z3OKHvqSFqehNHO7-SecPLXFMI4fh8-tT_OYeO8ieB60My10LSHcIyJaahP776WEQKViJXT4ytf-EFHcnTqFebAwUTFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPzpqV5lx1A18KNlPjzAj38HLYqaZdD5GcnZER4FmyVJquKuPci8l5vhky69OZuz9QBslzqRWT9hv2qe_kGKXeFysXdFOpXvGtX2EqwWAfgs_lzYf6LC5YHg17xqAGAqNgW0GbqB_w8vmVRZXnAxkvHDtDYYfGclKNe9HmhVVct02EtAOarGxgx33_fA7oKwgWJgcdjtlpcOuzWfKo-bZU6ZRH_GZaCGn-hpRVuSyO6dMZtDiknPI3YexogXOFF9XUxz4vuzTOUJvEnUFwZ1j07RBOr5Qz5BhSDhulZjU6OF2IDyh1TVRBCuLy6k0a6B3cZAmNtMQX-qZ-yFPeBsyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWkeJMTJ8jD3yodv2fAkFyOUcxpbM62JcCpw8-8bLH5ML4i2fduRQZKFf81e6zx4T_5-dOfSXkK3fCwWWUb8n55ZmAXUL20E9cAkY514NQADgb8QO8ptfniqp2j160GIXMptAzzjcoOSOlG-oNQpbap_pSzfvqMDL8klK2046dAAI-P_4eQk3P3aM0-MV7sJWdlIQdFH3tHdKVoAFgasFMIp01vRUSPSz-soAtrXV-LCLqAKoAH6mtYhA_EDL4BjjpjuMziPhXt8K_xXMhIxrOZzqoKeogqscmF90bjy7MLNxSY62hcT1yLkEqE6XrGR_VOHeOTdOWUEqjuAVlngEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igLRf0fPsf2Q9eBFLYcEBFyqd1zinZxujlspjj6gCHztPlJ6J8K4kScyhhE1nsgVsdRJMF31e_1ihNeZbfvCRdyek8UFqTrLVCY5C131f7TwvVOb-suo-4V5kXy4OgspxYI6bSmC9xosYPPYZTA_KJBfuMJareRdXE7Zt2qCuDwAQ35nI9gRAPpMKxqbQ4F-c87nBru-lr7slpbenAhIbLsVqUJlbZKp39U3Ndrc9c2eP7Vxgz5lfl2obHK1CjOt8w5SzwDV82MwfbPXTsiWRyRCJZHTHDTc2N2qG55eqrIaOMxhQ2dfZoCx-r2k4h-_sbTCpH1ZjKc75cUUij5Ixg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=HTl5qeJjsnB-PUM6RyfcfJrW0AGJRRsJD78UmYkW9z9ykZkU8WEESowxo1ReaGt-q3InOhSfeln2bY1NJ4zchj7XBTj7s0-hcVO26qAafyUMalyR4fLHun0uaOCKOxswRuPCvQ99-vngZbuXdMHv2Vuvyk7C-W6Rqz6PhzWqKn09Ie9l2gKKUKeaodbX67VvhnzHl9QDUy9duqN9zFOoZmAMzwORbJjwMFX8A6DvKyRb0LuhzWgaizvnyTeqmHA0SXOnWrWwwQj3f_DBk-zkaJo_A4Dpdf_mpZnGq8l5KtZZKfxpc2oy_LWro6Nj2MQr5h4Mw-shBB_ZPeWf967Z2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=HTl5qeJjsnB-PUM6RyfcfJrW0AGJRRsJD78UmYkW9z9ykZkU8WEESowxo1ReaGt-q3InOhSfeln2bY1NJ4zchj7XBTj7s0-hcVO26qAafyUMalyR4fLHun0uaOCKOxswRuPCvQ99-vngZbuXdMHv2Vuvyk7C-W6Rqz6PhzWqKn09Ie9l2gKKUKeaodbX67VvhnzHl9QDUy9duqN9zFOoZmAMzwORbJjwMFX8A6DvKyRb0LuhzWgaizvnyTeqmHA0SXOnWrWwwQj3f_DBk-zkaJo_A4Dpdf_mpZnGq8l5KtZZKfxpc2oy_LWro6Nj2MQr5h4Mw-shBB_ZPeWf967Z2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RB4g0qvL_12LiXgxQgEPThp_3GMe-boAA_PfspwKoHXgubJPFI3Xj7PjIWCvwnd5wOof_VO7TVA9WwAPW6EcoSk-Qqow-TQnocmxnoWpWXzLBjafbglAPeS8KKRga6B7D70uPpwDXb_du-f0hXheMA8KcZLKVCbAFiQKA3jPgtSJJk5XWV3o13cgLiTC6aPZ0GHce-LMzgIVo3M91u-E0EBw76IA-iZ0TclIUJwTL5XJkgc5sgL9iDUGSUq4ch6q_uTnqRqOOLQZaRztcWh7g95Ojf7_leKtl9p3ra_TNA3UEj2fIFqHnxV0JW-l5psvGsUWkdlCZ2uxcsWhjxmCtg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_zQpq-7N57zUHkPmWoXAczIRgz7YJu7VElyu4uQoMnHCEDT01XKv1Bne6hx5kXR6nFbZuLYJbWgPas0f9uWm-eIoi0VR_ZmE2nXh42s-1PuukHBy0WNg3hxRrfts1hQhz4bMkzXIypf4xDEQ-FabdxM0pcKbHlaS6WEviZB8zZmumVuLiX76-_Bv2Nbr5b-tJMqeUuHCHUicqM2RMCCw6_fhPe1HGdOEyKSw9IOikPZGgEOkIsX2OcAnDbFMDUDOIoxorRMwN9V7eRirwyTFn4v0BpKvjWuDGpqjJC1ZUbnDldy7pEwrZYJ7i-HYDOfkKC-ICFVtoKSDxDg6xVr5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WIvzJhdG0y4_n3r3yU3LP_N5mnJVrNZKMwVZq09DmGgTPUHhYJyMLR0tdD3ZR86TKXGPuwBd0TGsqfzFOB2pHzafeOUrMC-A2H_FSTMr71wZ4ac-92JAano4fRYtoIvnKsIbNhRR07SclJbM1hN60Y6owIJpgaZ32QvZv3ArD2EVTEyUwj1l4WWE_OjtPpmQAoUsbmLX2Q1nkcBlzNiuOip2wjvlEOhBDn_fJn2XbFogf2lIMh5NRt5Cbu0GD-0SxZV5BqZI8kPBNqvwLK7q_dtrd3Bh7-6z7-2LCmFn2dUbjN2rjBozyOwlnNnvaJsI2nf8fQXZ2Hy6S49wXBkIFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MHLbBcnvcqKIu93SRrM6OOjvrniqCD5Hv6Q8SaFVJomfXvV4IktJRagHtpIp4z798Fsv4tXEicu1-KVrp6ANxQAYQq4lQOHMBl0yFdBpdyenTeqLYgxLx5OBhfPkHwljkdyYVGs6IIVffMF6L5PKzxuOnIplG6OE4UUxpaFa_TC_UfrSqEU2wdhiyUM63WVjfJj8hZ3E_f8KRD7w8NYhbDQUAvMCzb3DypC4TapjSDaif3S3njq0eaN9Y6qM65-KBUN8YF9yHhQcZL2LQ9bkrXMegh0Thk0oNyY-VB_wKhAQOeqCKikFXviLc47IRqSlE_7xDDpwReCM6UsvTU-8Gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WT1xaOweMJR7AiKencUwKEvJktg1D6NIizvldBP5TBQhcluzxIVYTWzWJhBDdNxNRGwGwQRvW18BGQDflKsk4NdUNp5ZI3MzOKaMWHYOLt2zzuLLwODn0RLCXhrTwUWl6svWKtQnAb1jKa89B0G0fmXtIbjn1QD07ABV3ei8n0qL1gaJdn9FcVWNjcPfQ52Dn4HcZXuurRZrwpEkhUA1MCiqzooKfklysJ-X3f1-35pxaTcRQIYXJu3QgOYST4TeTtByjYGwQ0ZrF3OKYe2q-TZNV7HqdABB-diCzNTixnwW0IJRUtNG3nuOzH5DcPuFpHqy8GuAb0svHzW8bWmqPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H05F_8rQGt3psdZ19nTgBodfpVrUTYCU-obgSIWc3TrANeu-AbTRp484MxAEpvY64oTYe9sbSZov84uX1W8G5b97SVOkP3-Gar09cI7InCG8BByH-I7nzIIdHcrq6b5tmJW8Di7C-M1eszxtCTH7VCFbegsQpeEJQGqhTHJDo8R3S5bG2MJC3O-OhuwtDK__KO4vouhk9QnOOHFqUTib7Wz1X6_zJs_Lh3k2fEpWIhugSwS2H1Y3ZB3PcadI1_ytUpswnx9JgufTdS8d-btye0bElzXnoN0i6n-vEkhN-TpE63z8EE4NDNGgEe3WdqnMeSmU_2avIKGr0lzP2j9pxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eAxWJOiw87nhHVe5krFXke4eVYuzmHzO1lNJxM4u-qsRwge_nqn-DnKnOUKhP5NFYWs7ozYC4pZF32aDgXKnv8hMbTbyJINukxMnK5yY6n0k8_wOQiQQ6p7hDvq4tYf1pF3BIviVczL6VLACtd7ke0Je9oFFSamxGj2fu4kDPZuaCMKPqRuiZMj_p1JreVn2PcwKQLDNNhWUhub_pNfqL5ZZGZzpQA9Imp_ppg75XEs6EsnCXnQJxrjmSf3pM6nmsK9HgBW04QWIqqq7gTBQ2uyDTumogUqBSieDowbnVvp4fkXPYQ8eQ1PXlgdDBOT2f6beDaWu1MF4YwThwf9r9g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=vBnC_fFsyLSAz1TmoCe3X3r14Xrkxmj8Rd13nRJi8aEE5lUSFtdvC83nbCZhANU1vUfC0dFNMFhyZNrjqVWnZR0ki-OyGXSX7gt0_4xHDuD72l8oRHip7CClETYSG6rbF65X4kg9EONWyAu_QDLyfoB1XQl-xchPIaDnE7Gjv2roqlGzhKInau32jruhjvx_REJWjBtvvXANCfiQceT7Tqks8h2B6PWewbxxZarJmMLCqmOa6Yik3h1AEq09QMNNvPzlcyvfmLYIU8A3hxtsT8hH-jhizQ5SEaAM6iyghxzitgOF6nblzCSTxQDfY9Fu3dK8cEKDmPd3hlsbvOqBSiqrWhx5eFXswRHNiqyErQNWX9G56tFka1KUCnHHJw-VtIjPNmURp1pWRSvHLEXJ54B0OwQhWlaAgRY1knOfN3Zoqnw9IV3e1xPsVXJRSW4MzWm3V7eL30VLF_-7pU3rvTnPxcbZbAk_TPtR5HiArcHbeiRHlpF-wE34yrSVDTgphm5ll8rEtHOi9DQCJYZyYez0Az395Pybnlp6jzPe1a1BPYsE9Vjo6i7VbF8iG72upFTKyKn6WYTfN9Bu8jI_ZXrQHRR4Dl6N1efTWPMmjZQtlCAvgSm4w9FYamwpItCitfo2gQIFBUs5R587gzSgmzc6sZhc78y8YZUfbAx2L5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=vBnC_fFsyLSAz1TmoCe3X3r14Xrkxmj8Rd13nRJi8aEE5lUSFtdvC83nbCZhANU1vUfC0dFNMFhyZNrjqVWnZR0ki-OyGXSX7gt0_4xHDuD72l8oRHip7CClETYSG6rbF65X4kg9EONWyAu_QDLyfoB1XQl-xchPIaDnE7Gjv2roqlGzhKInau32jruhjvx_REJWjBtvvXANCfiQceT7Tqks8h2B6PWewbxxZarJmMLCqmOa6Yik3h1AEq09QMNNvPzlcyvfmLYIU8A3hxtsT8hH-jhizQ5SEaAM6iyghxzitgOF6nblzCSTxQDfY9Fu3dK8cEKDmPd3hlsbvOqBSiqrWhx5eFXswRHNiqyErQNWX9G56tFka1KUCnHHJw-VtIjPNmURp1pWRSvHLEXJ54B0OwQhWlaAgRY1knOfN3Zoqnw9IV3e1xPsVXJRSW4MzWm3V7eL30VLF_-7pU3rvTnPxcbZbAk_TPtR5HiArcHbeiRHlpF-wE34yrSVDTgphm5ll8rEtHOi9DQCJYZyYez0Az395Pybnlp6jzPe1a1BPYsE9Vjo6i7VbF8iG72upFTKyKn6WYTfN9Bu8jI_ZXrQHRR4Dl6N1efTWPMmjZQtlCAvgSm4w9FYamwpItCitfo2gQIFBUs5R587gzSgmzc6sZhc78y8YZUfbAx2L5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
