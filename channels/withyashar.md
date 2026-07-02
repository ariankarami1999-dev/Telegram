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
<img src="https://cdn4.telesco.pe/file/itHaiWTdT-1XahCcpvQx1PKObiRfl8PodXuHeXFzckzdv9l4L01SFYJayHqweelnjKMYb6lPbNC5rz3ZRiyOMEYXJlLBOsuVp4y7m_7u2tPtM5EBFjRD_5UdE-fxqaeIwqgVJsh1_jUfg5N48pUBPtLgp2j-XLqbF8eHncQX5Zgi72qqCld-7A7f2iWO7HGWS23J9NUMe7DvT9_ZbenGlDCXPHgV_MJUPKpmcHoEdcsTLQx5z1QEsAPdGdfKWLkMRS2buIy6PJo8UJw23Nm-ZpEoMQCWagyhidA4i9yFimjlUdulkSXKjngt-7wq_svcp37Jsdtn8TN_qawL8pDDmg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 333K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 18:05:51</div>
<hr>

<div class="tg-post" id="msg-16338">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید
@withyashar</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/withyashar/16338" target="_blank">📅 17:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16337">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/withyashar/16337" target="_blank">📅 17:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16336">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آبدانان</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/withyashar/16336" target="_blank">📅 17:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16335">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کامنت جدیدم برای ترامپ. حتماً فقط همین کامنت را لایک و ریپلای کنید. میتوانید با اد استوری ( با نگهداشتن روی  کامنت)، انتشار بیشتری دهید.
https://www.instagram.com/reel/DaSrqH3NjVK/?comment_id=18333946015271080
ترجمه :
آقای رئیس‌جمهور،
بسیاری از ایرانیان بر این باورند که صلح و ثبات پایدار تنها پس از پایان حکومت کنونی امکان‌پذیر خواهد بود. از شما با احترام درخواست می‌کنیم هنگام تصمیم‌گیری، این چند نکته را در نظر داشته باشید:
مردم ایران
گرسنه نیستند
(لطفاً به ویدئوی آبادان مراجعه کنید).
بسیاری از ایرانیان از شاهزاده رضا پهلوی به‌عنوان شخصیتی وحدت‌بخش برای یک دوران گذار مسالمت‌آمیز حمایت می‌کنند.
مهم‌ترین اولویت ملی ما، ایرانی آزاد، دموکراتیک و با تمامیت ارضی کامل است. حتی یک سانتی‌متر از خاک میهن ما نباید مورد خدشه قرار گیرد.
لطفاً با آزادسازی منابع مالی یا توافق‌هایی که موجب تقویت این رژیم شود، به آن کمک نکنید.
از توجه مستمر شما به مردم ایران سپاسگزاریم. ما به آینده‌ای بهتر امیدواریم و از تلاش‌ها و حمایت‌های شما قدردانی می‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/withyashar/16335" target="_blank">📅 17:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16334">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وال‌استریت ژورنال: در یک تغییر راهبردی مهم، فرماندهی مرکزی ایالات متحده (CENTCOM) در حال بررسی جدی انتقال بخشی از سامانه‌ها و زیرساخت‌های عملیاتی نظامی خود از برخی کشورهای حوزه خلیج فارس به اسرائیل است.
بر اساس این گزارش، منطقه صحرای نقب  به‌عنوان گزینه اصلی برای استقرار این سامانه‌ها در نظر گرفته شده است.
@withyashar</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/withyashar/16334" target="_blank">📅 16:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16333">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">استاندار تهران: تمام تلاش ما اینه که مراسم تشییع رهبر بدون تلفات به پایان برسه.
@withyashar
😐</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/withyashar/16333" target="_blank">📅 16:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16332">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ در تروث : ایالات متحده بیشتر از هر کشور دیگری برای ناتو هزینه می‌کند، و این هزینه بسیار زیاد است، بدون اینکه هیچ سودی از آن ببرد:
آمریکا - ۹۹۹ میلیارد دلار، بریتانیا - ۹۰.۵ میلیارد دلار، فرانسه - ۶۶.۵ میلیارد دلار، ایتالیا - ۴۸.۸ میلیارد دلار، لهستان - ۴۴.۳ میلیارد دلار. سایر کشورها، از جمله آلمان، بسیار کمتر هستند. (۲۰۱۴–۲۰۲۵) مضحک است!
@withyashar</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/withyashar/16332" target="_blank">📅 15:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16331">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دریاسالار برد کوپر(فرمانده سنتکام): امروز، با افتخار از سربازان و ملوانان آمریکایی که به یک واحد مشترک ضد پهپاد (C-UAS) در بحرین منصوب شده بودند، به خاطر عملکرد استثنایی آنها در سرنگونی ۱۴ پهپاد تهاجمی یک طرفه جمهوری اسلامی در چند هفته گذشته، قدردانی کردم.
@withyashar</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/withyashar/16331" target="_blank">📅 15:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16330">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏دبیر کل حزب دموکرات کردستان ایران ، مصطفی هجری گفته: ‏حمله زمینی به ⁧ ایران⁩ مطرح است اما پیشروی تا تهران در دستور کار  نیست، اگر شرایط مهیا شود تا ارومیه پیشروی خواهیم کرد @withyashar</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/withyashar/16330" target="_blank">📅 15:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16329">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏دبیر کل حزب دموکرات کردستان ایران ، مصطفی هجری گفته:
‏حمله زمینی به ⁧ ایران⁩ مطرح است اما پیشروی تا تهران در دستور کار  نیست، اگر شرایط مهیا شود تا ارومیه پیشروی خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/16329" target="_blank">📅 15:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16328">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کانال ۱۴ : منابع مستقر در قطر گزارش می‌دهند که ایران در جریان مذاکرات غیرمستقیم و مهم این هفته با ایالات متحده در دوحه، تضمین‌های امنیتی محکمی دریافت کرده است و تضمین می‌دهد که مقامات و فرماندهان ارشد نظامی این کشور در مراسم تشییع جنازه آیت‌الله علی خامنه‌ای، رهبر فقید ایران، هدف قرار نگیرند.
@withyashar</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/withyashar/16328" target="_blank">📅 15:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16327">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الحدث : پس از ۱۲۵ روز از کشته شدنش.. ترتیبات استثنایی برای «تشییع جنازه خامنه‌ای»
@withyashat</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/withyashar/16327" target="_blank">📅 14:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16326">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">الحدث : دور بعدی مذاکرات هفته آینده با حضور عراقچی و قالیباف در  در بورگن اشتوک سوئیس براگزار خواهد شد
@withyashar
العربیه: دور بعدی مذاکرات آمریکا و ایران در ۱۸ ژوئیه برگزار خواهد شد</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/16326" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16325">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16cdb8cfe8.mp4?token=XV1kvr5EjonYN7LvISLdC14YR8h3iWCBbHZn_inzmXGuIjFE_HDT3Nc0cbyHz3FnZmJ90Njd8qorI6-esSe9_IOg106yhsdP7S9BwOaViv83XlcsHDVnNJjd3iZZCyNPeWt-afcxTBI1kyrGwczzxLVMDjp5OSsgaVznMYU6XXjzeox4trZ1DL7iKIZY7g_xDTc9giFELxHZh1AiCWW-gP9TZlfl5kIjPkfrnxuv_PrQ1pAgQswOdU5LW2YuRrOLCRmUJf-benw-3fLAf_eRCPYJoERuLbRAPzi8QfuNp9-kOvv49lXsnqzzIDjbsd1KR2EzXorZEU1elsVJPdxBrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16cdb8cfe8.mp4?token=XV1kvr5EjonYN7LvISLdC14YR8h3iWCBbHZn_inzmXGuIjFE_HDT3Nc0cbyHz3FnZmJ90Njd8qorI6-esSe9_IOg106yhsdP7S9BwOaViv83XlcsHDVnNJjd3iZZCyNPeWt-afcxTBI1kyrGwczzxLVMDjp5OSsgaVznMYU6XXjzeox4trZ1DL7iKIZY7g_xDTc9giFELxHZh1AiCWW-gP9TZlfl5kIjPkfrnxuv_PrQ1pAgQswOdU5LW2YuRrOLCRmUJf-benw-3fLAf_eRCPYJoERuLbRAPzi8QfuNp9-kOvv49lXsnqzzIDjbsd1KR2EzXorZEU1elsVJPdxBrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : با توجه به داده ها به نظر میرسد کشتیهایی که از مسیر امن آمریکا در نزدیکی عمان رفت و آمد می کنند، نسبت به مسیری که جمهوری اسلامی تعیین کرده بیشتر است.
@withyashar</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/withyashar/16325" target="_blank">📅 13:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16324">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بلومبرگ:جمهوری اسلامی ایران کنترل مؤثر خود بر تنگه هرمز را از دست داده است.مقام آمریکایی اعلام کرد حمایت نظامی آمریکا و کمک به احیای جریان نفت و تجارت از تنگه هرمز در هفته‌های اخیر به بیش از ۱۰ میلیون بشکه در روز افزایش یافته است.
این افزایش ایران را غافلگیر کرده، توانایی آن برای کنترل ترافیک را محدود و به حملات اخیر اطراف تنگه کمک کرده است.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/16324" target="_blank">📅 13:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16323">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">غضنفری نماینده مجلس :
یک کودتا علیه رهبری مجتبی خامنه ای در جریان هست
@withyashar</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/16323" target="_blank">📅 13:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16322">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">امروز صبح، علی عبداللهی، فرمانده "خاتم‌الانبیای" (فرماندهی عملیات مشترک نیروهای مسلح ایران)، هشدار صریحی به اسرائیل و آمریکا داد و از "هرگونه محاسبات اشتباه" در طول مراسم عزاداری خبر داد. او گفت که این اقدام، "واکنش‌های شدید و ناخوشایندی" از سوی نیروهای امنیتی ایران به دنبال خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/16322" target="_blank">📅 13:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16321">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وقتی یک ماه پیش من گفتم در روابط عربستان و آمریکا تنش جدی ایجاد شده ، یک اینفلوئنسر تندرو سلطنت‌طلب که شبیه ته نون باگت است، حمله سختی به من کرد.</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/16321" target="_blank">📅 12:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16320">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نیویورک پست: تنش در روابط عربستان و آمریکا بر سر ایران و نگرانی از جنگ و تهدید منافع نفتی با احتمال بسته شدن تنگه هرمز افزایش یافته است @withyashar</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/16320" target="_blank">📅 12:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16319">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نیویورک پست: تنش در روابط عربستان و آمریکا بر سر ایران و نگرانی از جنگ و تهدید منافع نفتی با احتمال بسته شدن تنگه هرمز افزایش یافته است
@withyashar</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/16319" target="_blank">📅 12:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16318">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یک منبع عبری : سقوط هلیکوپتر روز گذشته آمریکا توسط ایران بود
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/16318" target="_blank">📅 12:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16317">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نتانیاهو: ممکن است جنگجویان کُرد ،حملات خود را به غرب و شمال غرب ایران امشب یا شب های بعد آغاز کنند.‌‌‌‌
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/16317" target="_blank">📅 12:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16316">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بعد از حمله به بیت، اعلام کردن منصوره خجسته باقرزاده، همسر خامنه‌ای کشته شده.
اما بعد از اینکه مجتبی پیام تسلیت داد و یادش رفت اسم مادرشو بیاره، خبرگزاری‌ها تکذیب کردن و گفتن زندس!
الان دوباره گفتن کشته شده و قراره همزمان با علی خامنه‌ای، براش مراسم بگیرن.
@withyashar</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/16316" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16315">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0gM4XpF9TiGgy7yLRI_cEF5XXi3s4dfedm48nx6tpw1tifDUDIr16WQqiomYb7EPky9glHfWnuvXkwFnxWpxp6Vb8ijNjhDvrWOu39yrYp6lK2A2pHhuAj0F-uWZPdKsJeOrx_ki2hNJ_5nYmRHOEXpca9TCHmqV0-96ryyMZLhaNpurgm8XxwfFKLOtahDgMwjHOFJN7NJQ0qjWhH1RqA1nncpicIDnKCJbaorH7U4G9osll5CF3veCZzYke3nxrqr5qA4HvhUTX--Tj5wk-ZVjSpm4XK8GxKQevUMzRCR15XQeY8SvMpn1RsfXH4TKVPqlGyyVnIZH0rpnHDtgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمودار سقوط دستمزد و ارزش پول ملی ایران از سال ۲۰۱۰ تاکنون
حالا اگه درامدت دلاری بوده این نمودار برعکس میشه
@withyashar</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/16315" target="_blank">📅 12:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16314">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فرمانده  خاتم الانبیا، گفت : «تنگه هرمز زمین بازی آمریکا نیست، بلکه قلمرو حاکمیتی تهران است. همه نفتکش‌ها و کشتی‌های تجاری موظفند فقط از مسیری که تعیین کرده عبور کنند.» آنها بعداً تهدید کردند که «هرگونه عدم رعایت پروتکل‌های ناوبری ایران در تنگه هرمز با واکنش فوری و قاطع نیروهای مسلح مواجه خواهد شد. ادامه حضور جنگنده‌های آمریکایی بر فراز تنگه هرمز، امنیت کل منطقه را به خطر می‌اندازد.»
@withyashar</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/16314" target="_blank">📅 12:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16313">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">1$ Tether = 178,000 Toman
@withyashar</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/16313" target="_blank">📅 12:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16312">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/071529db45.mp4?token=aLCQe9DCWIQ1DMn5O_trBSxg-fzlLxXJDRM4gIdMsL_urSVaVQcWymLWztxjCY6uCp8Fk-BqSgzfszzLexAlvpHhhQurVVrM-Q6aQ4s1x3Rpmhg3XayYWf76BVLOna0jbWH6axAO1pdnk_0tTSx-KkD3YlLbeRxcMfR1X92B-CGG7NzpdWtamPTunDovkxjr6fpfxfUsedutxV0Dou9Wj_29zU8p4qx-vxZ7raIls1JqvdmgElh0T5YOqLOuwqbVdJnP_85lNJREIgAaPwetwEy3716a5I7msKtGCVEyuiip9OYK2P7e2V5nujbrOToomSQB0fkIn3xkX11bUXiftg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/071529db45.mp4?token=aLCQe9DCWIQ1DMn5O_trBSxg-fzlLxXJDRM4gIdMsL_urSVaVQcWymLWztxjCY6uCp8Fk-BqSgzfszzLexAlvpHhhQurVVrM-Q6aQ4s1x3Rpmhg3XayYWf76BVLOna0jbWH6axAO1pdnk_0tTSx-KkD3YlLbeRxcMfR1X92B-CGG7NzpdWtamPTunDovkxjr6fpfxfUsedutxV0Dou9Wj_29zU8p4qx-vxZ7raIls1JqvdmgElh0T5YOqLOuwqbVdJnP_85lNJREIgAaPwetwEy3716a5I7msKtGCVEyuiip9OYK2P7e2V5nujbrOToomSQB0fkIn3xkX11bUXiftg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از خودروی حمل خامنه ای رونمایی شد
رئیس ستاد تشییع، وداع و نماز رهبر انقلاب در تهران: شکل کلی خودرو شبیه ضریح حرم امام رضا(ع) است.
@withyashar</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/16312" target="_blank">📅 11:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16311">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت
وزارت امور خارجه پاکستان اعلام کرد ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
طبق اعلام اسلام‌آباد، زمان برگزاری
نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر سابق ایران تعیین خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/16311" target="_blank">📅 11:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16310">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یک منبع آگاه:حال روحی آیت الله مجتبی خامنه ای مناسب شرکت در مراسم رهبر انقلاب نیست
@withyashar</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/16310" target="_blank">📅 11:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16309">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634f71e520.mp4?token=i6vdfl2us4lrBspXZ98IMzIRw4qcdVOXMaekOPOLkjExeDtS0ZwI-kiFDM8wQScz9AOmYIivVQMyF_QqxG9D2frlWjTzb3YqegXu7V_Ib_MKH5iKGSMtDf74COl9BFR8AQomTjL-g6U6tG6y4MGPfFGwaBJgg58ONyKVusFEwo6PFdAxdLDMi44t-s8UNVMv5GIKHlOo4Eg3-4hsDIIwhTXwT004UZT8LAsyr1yQ6H_5chgQfTPI3xiUiHy1HM8W-wi-to2qjVj-G_kQeK4DIV5U2R7Yqb6WUvzS2kpF9jRYVJus7TtVpvweo1oyI9edRQ3_TU7Jtc_yWCr1WOC-cIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634f71e520.mp4?token=i6vdfl2us4lrBspXZ98IMzIRw4qcdVOXMaekOPOLkjExeDtS0ZwI-kiFDM8wQScz9AOmYIivVQMyF_QqxG9D2frlWjTzb3YqegXu7V_Ib_MKH5iKGSMtDf74COl9BFR8AQomTjL-g6U6tG6y4MGPfFGwaBJgg58ONyKVusFEwo6PFdAxdLDMi44t-s8UNVMv5GIKHlOo4Eg3-4hsDIIwhTXwT004UZT8LAsyr1yQ6H_5chgQfTPI3xiUiHy1HM8W-wi-to2qjVj-G_kQeK4DIV5U2R7Yqb6WUvzS2kpF9jRYVJus7TtVpvweo1oyI9edRQ3_TU7Jtc_yWCr1WOC-cIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در‌ پست جدید تروث ساخته شده با هوشمصنوعی دکتر می‌شود و بیماران مبتلا به «سندرم اختلال روانی ترامپ» را درمان می‌کند از جمله بیماران وی رابرت دنیرو نشان داده میشود
@withyashar
😂</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/16309" target="_blank">📅 11:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16308">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d47807c6.mp4?token=XfyJzQFaRrMxWvdalgbofH8eubgpZsTszan_MSQTJ_1YvZA2sYjRTPrJey26v0Vn9nRN6YRZQTE2FFbZ6ozk-dFMN_TG2URRcOPw-seoLLDJJuijTOSxHVBZgX2rABHooWOKoOWbV9DDndnKLfaxJKp-dQ6WaVxvav9mUjLeQh_ZGNanrnysBlCajkop68OVX1eo4DnpTWJu8A8946-nsDN4uZaYL1Vvxc-6dfhoCFi3v1469uDB9NresM4s9n2GDt3zOddgYXh1-yL4IzkZdgwzl445Hlt6m1rikXEX6vW7D-eLoVkvYrDxdS_tcpWrK8QF26YOSScxoOrBtJOwwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d47807c6.mp4?token=XfyJzQFaRrMxWvdalgbofH8eubgpZsTszan_MSQTJ_1YvZA2sYjRTPrJey26v0Vn9nRN6YRZQTE2FFbZ6ozk-dFMN_TG2URRcOPw-seoLLDJJuijTOSxHVBZgX2rABHooWOKoOWbV9DDndnKLfaxJKp-dQ6WaVxvav9mUjLeQh_ZGNanrnysBlCajkop68OVX1eo4DnpTWJu8A8946-nsDN4uZaYL1Vvxc-6dfhoCFi3v1469uDB9NresM4s9n2GDt3zOddgYXh1-yL4IzkZdgwzl445Hlt6m1rikXEX6vW7D-eLoVkvYrDxdS_tcpWrK8QF26YOSScxoOrBtJOwwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره‌ای از سایت هسته‌ای اصفهان نشان میدهد ورودی‌ها همچنان مسدود هستند و هیچ نشانه‌ای از فعالیت جدید دیده نمی‌شود. گفته می‌شود بخشی از مواد هسته‌ای غنی‌شده ایران در این مکان نگهداری می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/withyashar/16308" target="_blank">📅 10:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16307">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سایت The War Zone با استناد به گزارش‌های محلی اعلام کرده است که هر شش بمب‌افکن استراتژیک B-52H Stratofortress حاضر در پایگاه RAF Fairford در بریتانیا، پایگاه را ترک کرده‌اند و احتمالاً به ایالات متحده بازگشته‌اند.
دوازده بمب‌افکن استراتژیک B-1B Lancer همچنان در پایگاه باقی مانده‌اند که این تعداد نسبت به هجده بمب‌افکن استراتژیک قبلی کاهش یافته است
@withyashar</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/16307" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16306">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سقوط قیمت نفت برنت به کانال ۷۰ دلار
بعد از افزایش عبور از تنگه هرمز، قیمت هر بشکه نفت WTI به ۶۷ و هر بشکه نفت برنت نیز به ۷۰ دلار کاهش پیدا کرد
@withyashar</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/16306" target="_blank">📅 10:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16305">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/16305" target="_blank">📅 02:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16304">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گروه
حزب آزادی کردستان ( پاک ) مستقر در منطقه کردستان عراق نیز در بیانیه‌ای اعلام کرد که دفتر مرکزی آن در استان اربیل هدف موشک بالستیک قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/16304" target="_blank">📅 01:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16303">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کانال 14 اسرائیل: مرکز فرماندهی منتسب به سپاه پاسداران در لبنان توسط ارتش اسرائیل (IDF) تصرف شد
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/16303" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16302">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رسانه های رژیم : در ساعات گذشته دو مقر گروهک های تجزیه طلب متعلق به گروه‌های تروریستی در اقلیم کردستان عراق هدف حمله قرار گرفته‌اند.
بر این اساس، یکی از حملات مقر گروهک تروریستی دمکرات در منطقه کویه را هدف قرار داده و حمله دیگر نیز مقر گروهک تروریستی پاک در منطقه بالکایتی را مورد اصابت قرار داده است.
‎
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/16302" target="_blank">📅 01:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16301">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سپاه: در پاسخ به اقدامات گروهک‌های کرد که منجر به کشته‌شدن سه نیروی فراجا شد، یکی از مقرهای این گروهک در منطقه دِیکله (شمال کردستان عراق) هدف حمله قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/16301" target="_blank">📅 01:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16300">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گزارش هایی از ارسال تجهیزات گسترده ارتش جمهوری اسلامی به خصوص نیروی زمینی به منطقه غرب کشور
این حجم تجهیزات  بعد از زمان درگیری با داعش بی سابقه هست
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/16300" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16299">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رویترز به نقل از منابع امنیتی عراق گزارش داد یک پهپاد حامل مواد منفجره به اردوگاه یک گروه مخالف کُرد ایرانی در شرق اربیل عراق برخورد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/16299" target="_blank">📅 01:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16298">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گزارش های زیاد از شلیک لانچر در ارومیه
🚨
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/16298" target="_blank">📅 00:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16297">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhW1uJ7BLvMiuc-rmas147Ew59s4Ie_CoCIxXAs6wbpebYp3Gyqt04MgyrCxroVpxN8VkxvjHnILEy5Vp_dluE5E6X2R56eY2bB4FGyTNurhRofTkWpe_D9XZ_s4-StwPtOBG6Tjs0zdW_oa_XN1dK3O2MR9CxDs54sslcoF0YD-qyTB5UwWO0JxwSN4Vq1gzVXQyw3THm5WMQwxcFBuJv8vb9YOZiP1KqGqEy-hoRXh_YnN9gIveIaaOVi9zo4-3pmWhLl_1WJxWo5pazq2KVZg712B6crASPrcLgTvQPcI0odtI9Gstn45nI2XfFBNNwuEhDWgv5EHt_tswFY1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق نظرسنجی شورای جهانی طلا از ۶۹ بانک مرکزی، رکورد ۹۰٪ از بانک‌های مرکزی عملکرد طلا در زمان‌های بحران را به عنوان عامل کلیدی در تصمیم خود برای نگهداری طلا ذکر کردند.
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/16297" target="_blank">📅 00:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16296">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc829af2ea.mp4?token=Zpnbk1J0oNTkNBdNO-SpFswUCQYoES72UEYyMPzFewKL3Wp4InEfcADC1jGbdtpHoXIp0iwu0ME_KNSZjZGQdEEoxyYhq3SIuvKnDT3Fzwfw-PT-xcL4s5SdfylVUaInvo07NrSNGAcvh4r1bFPh0kOacUf_bjjKVE_nwLQiOg_6sCxsdOHjrr0lYJFXhb3DTZVV6OSlH3FHQ-moBF0xO47ZC4sEmNubQDRQ9OfMxbVJNfpEtaOxetuUV6kyrR_CW907jG40botlMq7jJa8nMXcZ-rk-GQrz2rtvLtZOhNkLSK1Bs_IP1HCUGX8IEZT4JTEOmhzMLNWfmeHXW3ONRiAiSHEAf06X2GMBfneZAM5NFE9NOKqtFdwQo4ki5V7KcveB0NE9JGxtA0yUPsj-FGhW9PbqfDct0AFAYJZqR2prKrUjyNSItWYO9_wyDtrYF7j68YWdjhmeaHo21QtbTePToQA2sUw0Aq2mYyInwbWPdzhlRAHJhuYNiBtQwHFNat3ZsguolMfdBcSWqLvf1gVO6lZhwcQBCRDnDqDsFfCnj7TH46Yr5q65Xan1cIJGOagdffuI-7y86u1-6fSCuNW19pU7aSZytm2ie3U2z_0VATWQpSB8F_KMgX3DxTQVywuUcBBPS29MW7YxtbpOFhGGN0R_KfUwj74uN8XygUo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc829af2ea.mp4?token=Zpnbk1J0oNTkNBdNO-SpFswUCQYoES72UEYyMPzFewKL3Wp4InEfcADC1jGbdtpHoXIp0iwu0ME_KNSZjZGQdEEoxyYhq3SIuvKnDT3Fzwfw-PT-xcL4s5SdfylVUaInvo07NrSNGAcvh4r1bFPh0kOacUf_bjjKVE_nwLQiOg_6sCxsdOHjrr0lYJFXhb3DTZVV6OSlH3FHQ-moBF0xO47ZC4sEmNubQDRQ9OfMxbVJNfpEtaOxetuUV6kyrR_CW907jG40botlMq7jJa8nMXcZ-rk-GQrz2rtvLtZOhNkLSK1Bs_IP1HCUGX8IEZT4JTEOmhzMLNWfmeHXW3ONRiAiSHEAf06X2GMBfneZAM5NFE9NOKqtFdwQo4ki5V7KcveB0NE9JGxtA0yUPsj-FGhW9PbqfDct0AFAYJZqR2prKrUjyNSItWYO9_wyDtrYF7j68YWdjhmeaHo21QtbTePToQA2sUw0Aq2mYyInwbWPdzhlRAHJhuYNiBtQwHFNat3ZsguolMfdBcSWqLvf1gVO6lZhwcQBCRDnDqDsFfCnj7TH46Yr5q65Xan1cIJGOagdffuI-7y86u1-6fSCuNW19pU7aSZytm2ie3U2z_0VATWQpSB8F_KMgX3DxTQVywuUcBBPS29MW7YxtbpOFhGGN0R_KfUwj74uN8XygUo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش شبکه آی24: سیا و موساد در طرح استفاده از نیروهای کرد به عنوان بخشی از تلاش گسترده‌ علیه ایران نقش داشته‌اند
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/16296" target="_blank">📅 23:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16295">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed15951ba.mp4?token=fkRZVc5QOW7QnCpnuZyBFTldLxeUnIh5dFWyqWPHiyEjnX4Ri0wcw1cQShs5s-Pra-KkJL3nzrtumLylZ82cvgS-AmUXl-K8E1weaOafAovhJIes4JDUk3-awlIHm-R8cAycaagL4BbMoypcxigieM2dL-wgzKouqFmz14PtQxVtCxnNx-vZ6g_seEvvh9cILbEK9-jvxvgjp52Z0Z4v5csvvejnHl1_KfXzpf7ODSGEcz26dmkp29It4WUrn5NHVoI7DqPSMwaNucMGrm6tHBo-dKWwz2iPTV-cAyXsDbx0QygMwmS4IFxbT3sTor5V_ru9-dH3yhNxiWr8bu3TKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed15951ba.mp4?token=fkRZVc5QOW7QnCpnuZyBFTldLxeUnIh5dFWyqWPHiyEjnX4Ri0wcw1cQShs5s-Pra-KkJL3nzrtumLylZ82cvgS-AmUXl-K8E1weaOafAovhJIes4JDUk3-awlIHm-R8cAycaagL4BbMoypcxigieM2dL-wgzKouqFmz14PtQxVtCxnNx-vZ6g_seEvvh9cILbEK9-jvxvgjp52Z0Z4v5csvvejnHl1_KfXzpf7ODSGEcz26dmkp29It4WUrn5NHVoI7DqPSMwaNucMGrm6tHBo-dKWwz2iPTV-cAyXsDbx0QygMwmS4IFxbT3sTor5V_ru9-dH3yhNxiWr8bu3TKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: کانال پاناما گران‌ترین چیزی بود که تا به حال ساختیم و همچنین سودآورترین چیزی بود که تا به حال ساختیم. این ترکیب خوبی است.
کمی شبیه ونزوئلا. ما در واقع با جمهوری اسلامی ایران هم به همان اندازه خوب پیش می‌رویم. شاید شنیده باشید؟
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/16295" target="_blank">📅 23:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16294">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گزارش های زیاد از شلیک لانچر در ارومیه
🚨
@withyashar</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/16294" target="_blank">📅 23:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16293">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b695ead9.mp4?token=EXLJHOO2tfr0gUfb0N6TRU75gnudc73j9R-p2hFRbjQxSoBy8hKXmvGu0IVnfA3ncjaz7Z6FEdn49f8RSayC4aPrJmdI5SA91Po-dQUFcOBcCrBdkb1O9EaVds5zRFBVdREF7yj1oAEkpSrs3VuXME5rntTB6f2-9oi20eM2IydARESJG_SziaolNbbHQ3Ykl8YUa0-R3omrWBz7DrP7_K9YNIH9cqjY5TL-qdyMK6UzAYWT3ys8sjWRmPfm89t_E3Q8YEnrO57-QAguQgA2vVF8vIC16PwTnjewi46cPBmiZ0j9OHZPxJOrN4N1TQb1Ts6BECwRq5p2n_XwGlllOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b695ead9.mp4?token=EXLJHOO2tfr0gUfb0N6TRU75gnudc73j9R-p2hFRbjQxSoBy8hKXmvGu0IVnfA3ncjaz7Z6FEdn49f8RSayC4aPrJmdI5SA91Po-dQUFcOBcCrBdkb1O9EaVds5zRFBVdREF7yj1oAEkpSrs3VuXME5rntTB6f2-9oi20eM2IydARESJG_SziaolNbbHQ3Ykl8YUa0-R3omrWBz7DrP7_K9YNIH9cqjY5TL-qdyMK6UzAYWT3ys8sjWRmPfm89t_E3Q8YEnrO57-QAguQgA2vVF8vIC16PwTnjewi46cPBmiZ0j9OHZPxJOrN4N1TQb1Ts6BECwRq5p2n_XwGlllOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیلگر ژئوپلیتیک چینی: امضای تفاهم توسط ترامپ، فقط برای عبور از گرمای تابستان منطقه است!
۶۰ هزار سرباز آمریکایی آماده حمله زمینی به ایران هستند.
@withyashar</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/16293" target="_blank">📅 22:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16292">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/16292" target="_blank">📅 22:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16291">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تحقیق جدید نیویورک تایمز : بیش از دو میلیون سرباز روس و اوکراینی از ابتدای جنگ بین این دو کشور کشته یا زخمی شده‌اند. روسیه بیش از ۱.۴ میلیون سرباز از دست داده است که در میان آن‌ها حدود ۴۵۰ هزار کشته وجود دارد. اوکراین بین ۵۲۵ تا ۶۲۵ هزار سرباز از دست داده است که در میان آن‌ها ۱۲۵ تا ۱۵۰ هزار کشته وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/16291" target="_blank">📅 22:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16290">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPFC8CSAk3iuXOsrbu7586VAXKACL3wy7lx3vE4EBRikgNrXtIkUYBrHZ0WPoIhY68vLOlJLZDAdLU3yU0o3Q8nTSJuEG8tnJb7xj_UAMV5zBmvsXa80f32Qcek9A1xRartgV3tUBfJ3__xEnQYq3NZuO0941ewPWGP-6-Jfs4NN4qiYRe8xMcGUzEteUOnibIE5Zsmtm40ioAmShCXtkYfP2qL0Z8Y-g7nqZItntcv8nqdzlaUBtwpt8qmuam0nwB3CihuWz77AAK15x5YlakluAyNXgk2kcNLmMDeWIha1JiuWzZdlzxIGDUmhtyJEtx5f1AxzCThfnGUFdmvFGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو گروه از کشتی‌های نفتکش/کانتینربر تحت اسکورت هوایی و دریایی ایالات متحده از تنگه هرمز عبور می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/16290" target="_blank">📅 22:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16289">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سفیر آمریکا: «رابطه واشنگتن و تل‌آویو شبیه یک ازدواج ایده‌آل است که در آن جایی برای طلاق وجود ندارد»
@withyashar</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/16289" target="_blank">📅 22:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16288">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78447e35bd.mp4?token=W7nlINap6JRe4fCKtNsbM7VaYaFYe6WNCz8Ucl7LLdoi1pYZH_CN1RkU4x37CuKdVbuXXk6HZvMtWh8mHRcWqFOGylMkmchuqlgoT7kEBfYhAe_-Vk8dX-LI-MWurDjFFN7izMsvgktZSAp-Bv3WVBNHZgkiihbAnAoeivpawSM0eakaOVL5bN8zSr4KyPxKUwhGqX63karjdgbQiDyQ5xQo3yQIkT1qNp6wJROiD4Cx9w9LNvGtxliK9w1DdQCKDoQDVxMb4t7KHwoVEwKX5maRUR3Lg04SFIGRi3REFScG2EAhgPtXeigmLwrKjN_H496bIerXO9fYjO55Bzw_qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78447e35bd.mp4?token=W7nlINap6JRe4fCKtNsbM7VaYaFYe6WNCz8Ucl7LLdoi1pYZH_CN1RkU4x37CuKdVbuXXk6HZvMtWh8mHRcWqFOGylMkmchuqlgoT7kEBfYhAe_-Vk8dX-LI-MWurDjFFN7izMsvgktZSAp-Bv3WVBNHZgkiihbAnAoeivpawSM0eakaOVL5bN8zSr4KyPxKUwhGqX63karjdgbQiDyQ5xQo3yQIkT1qNp6wJROiD4Cx9w9LNvGtxliK9w1DdQCKDoQDVxMb4t7KHwoVEwKX5maRUR3Lg04SFIGRi3REFScG2EAhgPtXeigmLwrKjN_H496bIerXO9fYjO55Bzw_qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان پرزیدنت ترامپ توسط سوارکاران خشن (Rough Riders) تا کتابخانه ریاست‌جمهوری تئودور روزولت همراهی شد.
@withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/16288" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16287">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5fcb8e951.mp4?token=DtlEXViQqREchH0sb5w0WSGdrI46GUNOF9mEuehLMEJRidoqIJ9B73AbBRykOr7kwylaDMlPfLDIyl7A_CHLy6C6UFIlXLv-52OZ3LEl-9MOblr4U_TTtOQlDD0cFRTd_P7DGENYV6eSEE5H5imoYtOqDWtkDAjJRsdqK2bYwz7BIMz8Wl-dOyrLIa0GSzJ6NM6fGxEs68AwryYEW216mKzaPHVC78gHjRIxQ54Psc5DZea6RrsxOHuRkC7drlVLl-L3QZKC3tuSLSXCBLF3UhYui4PjarCscENpYfsIudn2yGRgIicGD5Ym9Je0XBWsNskdPrkNUIcxEV-8hFjkMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5fcb8e951.mp4?token=DtlEXViQqREchH0sb5w0WSGdrI46GUNOF9mEuehLMEJRidoqIJ9B73AbBRykOr7kwylaDMlPfLDIyl7A_CHLy6C6UFIlXLv-52OZ3LEl-9MOblr4U_TTtOQlDD0cFRTd_P7DGENYV6eSEE5H5imoYtOqDWtkDAjJRsdqK2bYwz7BIMz8Wl-dOyrLIa0GSzJ6NM6fGxEs68AwryYEW216mKzaPHVC78gHjRIxQ54Psc5DZea6RrsxOHuRkC7drlVLl-L3QZKC3tuSLSXCBLF3UhYui4PjarCscENpYfsIudn2yGRgIicGD5Ym9Je0XBWsNskdPrkNUIcxEV-8hFjkMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیروز کریمی روی آنتن زنده صداوسیما: قلعه نویی 5 سانت و 10 سانت رو تحمل کرد ولی 30 سانت رو میخواد کجاش بذاره؟!
@withyashar</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/16287" target="_blank">📅 21:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16286">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJP2l7pOMCj7x7cbsiUNhGPEOnkMbbiAO1xcmzsEjG5OLgNN4JdhaEU5aRQO6hBj9IVJTIabVswGfYfgDt1Nmqd56fP1QP2YCYSCic9y9bFljDOp-alk-ylhL2v7uj4j4EyLynPF2nqtLPXvy88adJKA1ZGYdEgadk8vP19LqHcOHapRC1aGoIuA7iuqynh_oGo3GP4BOw5bJQAPffAjV8d9L_rdhmLXP2VNV_esWTM8BBETMofVjSqs__wayzyzwTEMNX5CSGn6aTqumPDGBtnX2efAn-byjTbU9F6PV1QXZjOspYX9Q0OQkxbCbWUwO-dQQY1PoJgz6j9SjIdb8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیو ۳پا از به گل نشستن کشتی متخلف «خطر شب‌ ادراری
😂
⚠️
» @withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/16286" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16285">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">جی دی ونس: نمی توانم متعهد شوم که در طول ۶۰ روز به ایران حمله نکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/16285" target="_blank">📅 21:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16284">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_Rr-dRpJf6IGZcsPwgeXIL7-dKIJEiR5BslpiS9BY-fjU6WjJE5jui4Ub4SZ4yUvPNgi-08YfT1n8b6WUI-S6s8CqfYjhyATZuY_gGYzn-F9oh--SmnBfJuj5j0tZDlMRdt26265FF-dDUPr8DqDy238O9byXDwQu8chp0Q5fliuu8bhKztwqu6Sa8LlxufN5Dw892u8RDInItkdzkNAHNPq_SAASJ2MhTMmgs6FcEEJ0IEuXr8SFZPecrJYHjIO07NmL1JoepLFdxMNC_ONHragbD4DL9m_X799FCMbrjGX-cowC5aajtSr9srs5onripsYrbld-7gkj9KAcF-sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با رسیدن ناو آبی خاکی باکسر به محدوده فرماندهی سنتکام استعداد نیروی‌دریایی امریکا در خاورمیانه افزایش می‌یابد.
استقرار ناو آبی خاکی باکسر احتمال حمله زمینی امریکا به جزایر ایرانی و حتی نوار جنوبی کشور را چند برابر می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/16284" target="_blank">📅 21:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16283">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0fcb1fe97.mp4?token=Jocy3JhNLjRZWiongahqi0rz5lNCZH2SUYIzEQe9j9wN9mSvA8_m9XEDGpYo8MIl5Y5zkewD3pmT-R7NoZ19pmKcIDf_yOdduIDgdzLGP9NChAaUQGwsvis8GGE9XgIZt8MVawUz0C6KnLmfH1ngEHlbnKfFfVZ9GJlLWtqQApZVmU1re_Kd5NgMpYmfHeNYSbj_hVx2xNUS-smh8xrk44vzcYOEqepRVxKTxbpOCsXuchY730SWKMCpiAA8qtjpCX0skiqdnB_0YB99Ki4ore9-Bdx_ECR8M6m5kLpDiK4BlQoGB_hdgvPgXqvnUd06EeGEVtwr1MC1mZrm-_Ya_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0fcb1fe97.mp4?token=Jocy3JhNLjRZWiongahqi0rz5lNCZH2SUYIzEQe9j9wN9mSvA8_m9XEDGpYo8MIl5Y5zkewD3pmT-R7NoZ19pmKcIDf_yOdduIDgdzLGP9NChAaUQGwsvis8GGE9XgIZt8MVawUz0C6KnLmfH1ngEHlbnKfFfVZ9GJlLWtqQApZVmU1re_Kd5NgMpYmfHeNYSbj_hVx2xNUS-smh8xrk44vzcYOEqepRVxKTxbpOCsXuchY730SWKMCpiAA8qtjpCX0skiqdnB_0YB99Ki4ore9-Bdx_ECR8M6m5kLpDiK4BlQoGB_hdgvPgXqvnUd06EeGEVtwr1MC1mZrm-_Ya_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو ۳پا از به گل نشستن کشتی متخلف «خطر شب‌ ادراری
😂
⚠️
»
@withyashar</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/16283" target="_blank">📅 21:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16282">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گفت‌وگوها با واسطه‌های پاکستانی و قطری در دوحه به پایان رسید، سازوکاری برای جلوگیری از تنش‌ها بین دو کشور ایجاد خواهد شد. تصمیم گرفته شد که بخشی از ۶ میلیارد دلار دارایی‌های مسدود شده برای خرید کالا بر اساس نیازهای ایران استفاده شود
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/16282" target="_blank">📅 20:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16281">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/16281" target="_blank">📅 20:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16280">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گزارش ها از وقوع انفجار های شدید و تیراندازی گسترده میان ارتش اسرائیل و نیرو های حزب الله در جنوب لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/16280" target="_blank">📅 20:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16279">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وال استریت ژورنال: آمریکا در حال بررسی خروج نیروهای خود از عربستان است
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/16279" target="_blank">📅 20:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16278">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رسانه‌های سعودی درباره نشست دوحه:
ایران خواستار اجرای ۵ بند از یادداشت تفاهم قبل از پرداختن به پرونده‌های دیگر شد
ایران اسرائیل را به مانع‌تراشی در اجرای یادداشت تفاهم با ماندن در جنوب لبنان متهم کرد
ایران بر حاکمیت خود و عمان بر تنگه هرمز تأکید کرد و هرگونه مسیر حمل‌ونقل دریایی در تنگه هرمز بدون اجازه خود را رد کرد
ایران بر اجرای بندهای «دارایی‌های مسدود شده» تمرکز کرد
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/16278" target="_blank">📅 20:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16277">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ارتش آمریکا:
امروز ، ساعت ۳:۳۰ بامداد به وقت شرق آمریکا، خدمه یک بالگرد MH-60S Sea Hawk متعلق به ناو هواپیمابر USS George H.W. Bush در دریای عرب فرود اضطراری انجام دادند.
هیچ نشانه‌ای وجود ندارد که این حادثه ناشی از اقدام خصمانه بوده باشد.
سه نفر از چهار خدمه نجات یافته‌اند و در وضعیت پایدار روی عرشه ناو USS George H.W. Bush قرار دارند.
یگان‌های نیروی دریایی آمریکا در منطقه همچنان در حال جست‌وجو برای یافتن عضو مفقود باقی‌مانده هستند و علت حادثه در حال بررسی است.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/16277" target="_blank">📅 20:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16276">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اتاق جنگ با یاشار : در سیزن ۹ اپیزود ۵ کارتون سیپسون ها پخش در سال ۱۹۹۷ پیشبینی شده فینال یک جام جهانی بین مکزیک و پرتقال برگزار خواهد شد ! همه نظرشون اینه که این پیشبینی برای همین جام جهانی است !
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/16276" target="_blank">📅 19:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16275">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یک مقام آمریکایی به i24NEWS درباره ادعای آزادسازی ۳ میلیارد دلار از دارایی‌های ایران:
هیچ دارایی منجمد شده‌ای آزاد نشده است و هیچ دارایی‌ای آزاد نخواهد شد مگر اینکه ایران شرایط مندرج در یادداشت تفاهم را برآورده کند.
هر دارایی آزاد شده باید به تأیید آمریکا برسد و برای خرید محصولات کشاورزی آمریکایی برای مردم ایران استفاده شود.
@withyashar</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/16275" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16274">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">واشنگتن پست : وزارت جنگ آمریکا در حال آماده‌سازی برای اعزام نیروهای زمینی آمریکا به لبنان است.
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/16274" target="_blank">📅 19:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16273">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اینترنشنال: مجتبی خامنه‌ای میخواد اژه‌ای رو بعد از پایان دوره پنج ساله از ریاست قوه‌قضاییه کنار بذاره. @withyashar ( البته تجربه ثابت کرده هر چیزی که ترامپ و اینترنشنال بگن، جمهوری اسلامی لج میکنه و بدتر انجام نمیده.)</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/16273" target="_blank">📅 18:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16272">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عراق به گروه‌های مسلح طرفدار ایران دستور داد تا ۳۰ سپتامبر خلع سلاح شوند
دولت عراق به گروه‌های مسلح طرفدار ایران دستور داده است تا ۳۰ سپتامبر، همزمان با پایان ماموریت ائتلاف ضد داعش به رهبری ایالات متحده، به طور کامل خلع سلاح شوند.
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/16272" target="_blank">📅 18:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16271">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/190c38d298.mp4?token=d7oYc-5DMyLNrGwpTM_2mC-6fZisXy-4RScJoAlAH24WjoX3VVuGfKn7_Rx1oan1LLuxbRw4kiu2Su2aQeBjEDoey5bVknqAmVmjUYTKErE5XCzLKTt9Dl01tp9Ej_QKCgvHYMuQ87_Sn3MQ1I4lAcydzR9r_LKL8U0fmKNj8lT3gjHvkly5O0ckGt9D1Qt6dfLelouYJZF-9SSROUA5xOY9hBN9qAAft-DWCHrKpDX3CVdCDr870EvtGxUSa2OKRLgKixz60vm4LSJw6KZsMj9HK0R_y0845gsoD2n4tHY9Qh66ZGdkNkH7j-On_EskA9L-SiHOsigvq6fUsdta7Eez9-Y5kihOy30mM80h1nLFhikHIkqwlQnRD1FIJxi5UQs7SrOUmNCiUjPuxVgrZWQmDeOWFgZWcRcfc0oeZUuPHQybD04HOnRor3XolyYIt8k6dNMhscge-u_3hDlwSPFEIIJX1d3nCy78Ip0KjPMPRx4U3IbZFpCtXSaBgqf3H7t77Cs5E6mpCI1e2kkI5SoYa3dS375OpzE1AUiAP3puMJU5DYxHHLi4EHb--LtjDTwFuEr15KRV90kDKO5mm4karpN0q99gwSKEBrOnXvYF85VBcOg-p6jvYqibMRe93T-83ou_r3xRN_qJK4JrBSpweqv57sTquTBsXZfawL4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/190c38d298.mp4?token=d7oYc-5DMyLNrGwpTM_2mC-6fZisXy-4RScJoAlAH24WjoX3VVuGfKn7_Rx1oan1LLuxbRw4kiu2Su2aQeBjEDoey5bVknqAmVmjUYTKErE5XCzLKTt9Dl01tp9Ej_QKCgvHYMuQ87_Sn3MQ1I4lAcydzR9r_LKL8U0fmKNj8lT3gjHvkly5O0ckGt9D1Qt6dfLelouYJZF-9SSROUA5xOY9hBN9qAAft-DWCHrKpDX3CVdCDr870EvtGxUSa2OKRLgKixz60vm4LSJw6KZsMj9HK0R_y0845gsoD2n4tHY9Qh66ZGdkNkH7j-On_EskA9L-SiHOsigvq6fUsdta7Eez9-Y5kihOy30mM80h1nLFhikHIkqwlQnRD1FIJxi5UQs7SrOUmNCiUjPuxVgrZWQmDeOWFgZWcRcfc0oeZUuPHQybD04HOnRor3XolyYIt8k6dNMhscge-u_3hDlwSPFEIIJX1d3nCy78Ip0KjPMPRx4U3IbZFpCtXSaBgqf3H7t77Cs5E6mpCI1e2kkI5SoYa3dS375OpzE1AUiAP3puMJU5DYxHHLi4EHb--LtjDTwFuEr15KRV90kDKO5mm4karpN0q99gwSKEBrOnXvYF85VBcOg-p6jvYqibMRe93T-83ou_r3xRN_qJK4JrBSpweqv57sTquTBsXZfawL4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : «لوفت‌وافه» وارد میشود
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/16271" target="_blank">📅 17:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16270">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">«جان رتکلیف» مدیر سازمان اطلاعات مرکزی آمریکا (سیا) ادعا کرد که جنگ آمریکا و اسرائیل علیه ایران اکنون جنگ فناوری است و گفت: «کشوری که بهتر بتواند از قدرت فناوری استفاده کند، آینده جهان را تعیین خواهد کرد.»
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/16270" target="_blank">📅 16:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16269">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جی دی ونس: ترامپ به ما گفت با توافق با ایران فعلا تنگه هرمز رو باز کنیم و ذخایر انرژی جهان رو فول کنیم تا بعد ببینیم چی میشه‌.
@withyashar</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/16269" target="_blank">📅 16:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16268">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202c2c732d.mp4?token=Ws9VvFfBQJPHYoGnC-dN5BGA5F-q36ENBKHMJGyaXIYlDdHjPXPXdp-wxOSTIuRPRt1G4WmtCLVbif2Og9d5Ge5Cj_6akiBtPFAq0Q_UHaBIJgsw9TyBvY81Rs-PguTxiEEhMOlnzXq7-_aWvE4QxlvomKgz7TrO741fV0q-n43WZU2XQtFQOSTAjlcBHNjumUzMeh-s3uRDQJjOsSnBWdvEJV9GWYkPRlmmf4Wwv76Cu2ElGgnElXhttaAA1PpDYqqKPNLq9z47L2YRBr7b25rBP56iGNtqNLhSiO5BZzIXvHlLtQAg4xtZ5KEz4F0bsgQ0ND6ZNKgsliLSZGcm1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202c2c732d.mp4?token=Ws9VvFfBQJPHYoGnC-dN5BGA5F-q36ENBKHMJGyaXIYlDdHjPXPXdp-wxOSTIuRPRt1G4WmtCLVbif2Og9d5Ge5Cj_6akiBtPFAq0Q_UHaBIJgsw9TyBvY81Rs-PguTxiEEhMOlnzXq7-_aWvE4QxlvomKgz7TrO741fV0q-n43WZU2XQtFQOSTAjlcBHNjumUzMeh-s3uRDQJjOsSnBWdvEJV9GWYkPRlmmf4Wwv76Cu2ElGgnElXhttaAA1PpDYqqKPNLq9z47L2YRBr7b25rBP56iGNtqNLhSiO5BZzIXvHlLtQAg4xtZ5KEz4F0bsgQ0ND6ZNKgsliLSZGcm1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: منتقدان شما می‌گویند که از ریاست‌جمهوری سود می‌برید.
ترامپ: من سود می‌برم چون بازار بورس در حال رشد است. همه‌ی ما داریم سود می‌بریم.
وضعیت حساب بازنشستگی 401(k) شما چطور است؟ ۸۵ درصد رشد کرده. «متشکرم، رئیس‌جمهور ترامپ!»
من سود می‌برم چون پول زیادی دارم.
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/16268" target="_blank">📅 16:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16267">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ درباره ایران:
ما سه شب آنها را به شدت هدف قرار دادیم، اما اکنون رابطه ما بسیار خوب است.
@withyashar</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/16267" target="_blank">📅 16:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16266">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وال‌استریت ژورنال: یک کشمکش قدرت در داخل تهران، مذاکرات صلح آمریکا و ایران را به خطر انداخته است
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/16266" target="_blank">📅 15:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16265">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پوتین: به دلیل کمبود گسترده سوخت در روسیه،صادرات هرگونه سوخت ممنوع می‌شود،قابل توجه است که ایران از روسیه بنزین وارد می‌کند و صادرات سوخت به ایران نیز متوقف می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/16265" target="_blank">📅 14:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16264">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">غریب‌آبادی‌(کاظم دست کج)در راس هیئتی متشکل از وزارت خارجه، بانک مرکزی و وزارت کشاورزی به قطر سفر کرده است، صبح امروز با شیخ «محمد بن عبدالرحمن آل ثانی» وزیر امور خارجه دولت قطر، دیدار و گفت‌وگو کرد
پس از این دیدار،
نشست سه جانبه مذاکره کنندگان ارشد ایران، قطر و پاکستان برای بررسی روند اجرای یادداشت تفاهم برگزار شد
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/16264" target="_blank">📅 14:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16263">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/va-jMfi1HQFRXbNTEQdwLDCvh10ym1EEw4bhQ2OgIgLt_rSpptS4q7ZlJM3rUN8s-40dcj8rxcavINp2IczoWCOF9SEcNv5lQTpcbBdxfwwPxrj4OY0sWqjN0nt3z8yUFskb7XsByxpRgc6KXMjc1twbB5kV5QW6SOFUCvvY3plQiYtPUE6r1kcy3VRRAEvnISfmUGpWTyCnC0vt3l8PgaZGkvr92ODlZ-OYFh5FMCt2hWRTxDcYrYs-LqCo3AAKV8C4xhYFTf9NC8DRHJYMbKowkJf3dxqYcD5CiFpK9Ij5g6N0fguBaH8v4G3UOZF4ReWNfvL3tNo2ca-9scwNJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این بین، جمهوری اسلامی هم بیکار ننشسته، یک هواپیمای ایلیوشین روسی تجهیزات را دیشب به تهران آورده و اکنون در حال برگشت است این در حالی است که خبرگزاری‌های عبری امروز صبح گفته بودند که ترامپ در پی یک حمله تمام عیار است
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/16263" target="_blank">📅 14:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16262">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JosvduYO2Lya9mc8MTUk0aBm9kxmYti71yXotac-jhESdz3Ho-J7Uvqm235fQNWS0w8U0gDDkCLKCZxOwn09PBTOsV4hk7Rb9VHqbKzyTksFuXJNZDj0M2Fsa4xG9J3sVszujmkFfXKFf6PL10_v9gzXTLEiWFgI40yyNWX5cL5ueZftBkZqFnB6X_BhY3WD_-EM7Gqjp-WwTKO5pb3WNrC8iORvVpkNPa_p-3dChWtZ41hP6YSMUVoueGlv_9_SdOnZn9rFhbSekNL_ZQ9y-rS9yS4oYVbvlUBTKyGxcFDeW54nF2Ob87A9JY2Wz_FVMMgdbiTUzpY-fEI75rhPeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلا جهانی دوباره پایین زده و اومد زیر ۴۰۰۰ دلار
دلیل اصلیش اینه که پیش‌بینی‌ها از افزایش نرخ بهره آمریکا دوباره بالا رفته
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/16262" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16261">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIvO0RROtr4Rghh1WplXmUb488TddVUGgO3t9hC53vn9OJArKCQFXcWwhx2c8d2df7516CBi_PhHqocAE6tKwuEmXX_YJrj-aCnVHPjjO2dJl0UFLnC3tfLpi3LkPdPMfz3g_78JE8Dw9kMqfb8n5d7WlF-q5PsoqGXrduOvqnqRBraWz7fD8UTgXBCqv9QNiozHliyquGzCZ--eU2NQsUvF929DE3svf515sgdDCz74ZCGFnK7oSY2-5sFb1HVnPd0_KsIJ9u85CbXpKeqmrq1luYdOllggbZBN6sjQNdPC_hPn57U5mFmdwrvfTLPJjLRFXdS4QRMyLS5r3lQfvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق داده‌های CryptoQuant، موجودی نهنگ‌های بیت‌کوین بزرگ‌ترین جهش تاریخش رو ثبت کرده و تا الان بیشتر از ۲۷۰ هزار بیت‌کوین (حدود ۱۶ میلیارد دلار) حوالی قیمت ۵۹ هزار دلار خریداری شده
و
در حال جمع کردن بیت‌کوین هستن
این به معنی رشد فوری قیمت نیست، اما ، نشونه مثبتی برای روند میان‌مدت و بلندمدت بازار محسوب میشه
@withyashar</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/16261" target="_blank">📅 13:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16260">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60dd03797.mp4?token=Brx-Iwtgw0DL4ZfeegVEEhY40JzI3eOeqNfBVGDSIILm-0eB6yp_DUkRutM0KRfvuzHmn0QN92ADB3xoce2Ddf9V0OZ8Vtd1THr7-0DwkAKIcrtHwG-owCwMLRznJX2AnsrwwKIfq29W8JkfcHakkV67zaNn8G1Mb2epSjGRjx1XMXdgJWA0X-vB7A4aRsSPR9-XoY3ONrUQIf7L65F9STTMiOKb9WO-l44LEL6NVQKj4XfSesDqCa5D45DAjPLwm9tlgJOIup0SJvz0iFh6PQhTsJD2RGVdmXMBfKLk68SALr366e5uAew64sYJHA7dYIWtaHHDZxidrOj1HdNy9jvs6jPp9smR5hbYcjLI_4GsjsA56PfwJCO7vNzPwDBTQXsXGTwSWrTVbmouAwh41dTr92-8oCWIRtjEXadZfAkQ_2R--IBjcb8NTHYD9kdP-ZjEfE9sNDQyIREjE41yrFAUcFMLV0Wm9tjK6MnJxugdeL-hgvUrKTblqXfI3xz1E9_VIP-g3dE29tzuj7yotQWTXwXwUZmgJ9z0goAdAWJXwxmZnBFVqZaNB3vKvoIjY1k8mFoUEOrvGzHiqTRFalikhnHagSOPjSgLwebZSyVoPqMuioUP21_PAPxLaScrqz-KJiaEOipRyDat4K_eA3UBwVmIftzOuqisvJFte4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60dd03797.mp4?token=Brx-Iwtgw0DL4ZfeegVEEhY40JzI3eOeqNfBVGDSIILm-0eB6yp_DUkRutM0KRfvuzHmn0QN92ADB3xoce2Ddf9V0OZ8Vtd1THr7-0DwkAKIcrtHwG-owCwMLRznJX2AnsrwwKIfq29W8JkfcHakkV67zaNn8G1Mb2epSjGRjx1XMXdgJWA0X-vB7A4aRsSPR9-XoY3ONrUQIf7L65F9STTMiOKb9WO-l44LEL6NVQKj4XfSesDqCa5D45DAjPLwm9tlgJOIup0SJvz0iFh6PQhTsJD2RGVdmXMBfKLk68SALr366e5uAew64sYJHA7dYIWtaHHDZxidrOj1HdNy9jvs6jPp9smR5hbYcjLI_4GsjsA56PfwJCO7vNzPwDBTQXsXGTwSWrTVbmouAwh41dTr92-8oCWIRtjEXadZfAkQ_2R--IBjcb8NTHYD9kdP-ZjEfE9sNDQyIREjE41yrFAUcFMLV0Wm9tjK6MnJxugdeL-hgvUrKTblqXfI3xz1E9_VIP-g3dE29tzuj7yotQWTXwXwUZmgJ9z0goAdAWJXwxmZnBFVqZaNB3vKvoIjY1k8mFoUEOrvGzHiqTRFalikhnHagSOPjSgLwebZSyVoPqMuioUP21_PAPxLaScrqz-KJiaEOipRyDat4K_eA3UBwVmIftzOuqisvJFte4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکورت و جابجایی دیدنی بی بی نتانیاهو
@withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/16260" target="_blank">📅 13:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16259">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYqhgZ8Oh_BcXxWGP9aCZcydCzbe3JYiXjt3d9hu7Jm6G_HKL6DmwAcmqWojeLw6YyZqTpZn5zUR2Qy8xayLqc0Wz9v5QBq-V7va6tsdlXtL09XnSnnpO1VzMsl0OdFqiVas6fjnd7R9pYBPGQG4brNnjg1tV2x4c7rDv4ijtDhdo3owl8lle7kVl37p8N4vPMwi3avj0FI6AAh-qPGpVEU04bXMJuo3LwkbJAii1aD1frTxWDu5ATpQ3uk08wVGkOunTIWO4UCZHN63ttHtNFZbDiKxa1nHZg2NG4esF4Ntz1Y-BviU9qrMf7wyfQDVleg3msdVTT_21N5DfBM8bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت خدمات دریایی انگلیس:
یک حادثه دریایی در ۷۶ مایل دریایی جنوب بلحاف در یمن رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/16259" target="_blank">📅 12:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16258">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رویترز: مذاکرات فنی غیر مستقیم ایران و آمریکا، در دوحه با حضور مذاکره‌کنندگان ارشد و تیم‌های تخصصی در حال برگزاری است
ویتکاف و کوشنر، چارچوب و مبانی این مذاکرات را پایه‌گذاری کردند
@withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/16258" target="_blank">📅 12:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16257">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کانال ۱۴ اسرائیل : رئیس جمهور ترامپ برنامه‌های عملیات نظامی گسترده علیه ایران را متوقف کرده است تا مذاکرات دیپلماتیک با هدف محدود کردن برنامه هسته‌ای این کشور را در اولویت قرار دهد در‌ عوض از حملات تلافی‌جویانه هدفمند برای حفظ اهرم فشار استفاده می‌کند تا از بی‌ثباتی منطقه‌ای جلوگیری کند.
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/16257" target="_blank">📅 12:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16256">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فارس : استان هرمزگان بیشترین آسیب را از آلودگی نفتی ناشی از حمله آمریکا متحمل شده است. این آلودگی بخش‌هایی از سواحل بندرعباس، قشم، جاسک، سیریک، بندرلنگه، لاوان، بوموسی و تنب‌بزرگ را در بر گرفته و تاکنون بیش از ۲۵۰ کیلومتر از خط ساحلی این استان تحت تأثیر قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/16256" target="_blank">📅 12:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16255">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">1$ Tether = 175,000 Toman
📈
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/16255" target="_blank">📅 11:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16254">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYpElLuQXywE6VuRQOcPPDlnrwdTbTAEo7eODHe7Shsf3Cs0gh_4WwTUCj_Ht_Xld70U_YhtGVpHyhu5ZynG2iwwmHa3amBiq3YFCgorX91y5tkhd6urEz6xo8JAlnW2haNVDIXf3c7KX0WDRMVzV-A760cjvZYinF5IrYU46Wh8cJlaEY-PjovplFe6ZzA8d6q2h5PKveoK-a3z1RG-hFNnwXj0oWL9VDiVznPvFOnAbtcYIdtTMksMvdymxZB67sdAoX_OXNj4ya_umVvN_4fPEH8u95Hgx2ft-VbyONm01-RYuv0uKpbgLvah41kVeYaX4HZ9Xvk1tfEfzNM66w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون شیراز نابودسازی از پیش اعلام شده مهمات عمل نکرده.
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/16254" target="_blank">📅 11:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16253">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaRuk4JnDd1n4uVm9uEpKQ3SHuzUO2neO4Mboz-sVPp6rBF3RsC4AQaCiXWdlhCVrh_2Afgiaf2lypxAHbnScYbW5k2LD2vv7rlIccqqqn00-7WiaDiQeC9B84kdi24QLSRwdP_zhcT245rH_YYCe5GOQVIfQcC0TPEh1YaUZ2WuIxS_jl5Owg63umYHaOsmLjjQmfJaHgaf_5GzUkITjqG8jtv0lh01HQBtk-DOa6jcWvUYS8t5GG4NA2ZS82m__CcU71XKEpNdsFUrnczODM5fosUltPT43IN_leOPjHuTK2iL8pC6aixaDYnTzq38MPmXLSAFKctkHHIk7Cnajw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند کشتی باری که از مسیری غیر از مسیر تعیین شده ایران در تنگه هرمز، تردد می‌کرد به علت خطای ناوبری و آبخور، به گل نشست
@withyashar</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/16253" target="_blank">📅 11:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16252">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خبرگزاری های رژیم :
خبر تدفین رهبر انقلاب در نزدیکی ضریح امام رضا علیه السلام کذب است
به تازگی، برخی صفحات در فضای مجازی ادعا کرده‌اند که پیکر مطهر رهبر شهید انقلاب در روضه رضوان و در جوار ضریح ملکوتی امام رضا(ع) به خاک سپرده خواهد شد. این شایعه در پی آن مطرح شده که بخشی از روضه رضوان به دلیل مرمت سنگ‌فرش‌ها، داربست‌ کشی و با پارچه پوشیده شده است.
لازم به تأکید است که نظر و تأکید رهبر معظم انقلاب بر این بوده که مکان خاکسپاری پیکر رهبر شهید، به‌گونه‌ای انتخاب شود که خللی در زیارت حضرت ثامن‌ الحجج(ع) ایجاد نگردد؛ ازاین‌رو، پیکر مطهر ایشان در نزدیکی ضریح مطهر دفن نخواهد شد.
@withyashar
یاشار : امام رضا هم جواب کرد
😂</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/16252" target="_blank">📅 11:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16251">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سخنگوی ارتش فرانسه: ناو هواپیمابر «شارل دوگل» در خلیج عدن مستقر شد
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/16251" target="_blank">📅 11:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16250">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شرکت‌کنندگان مراسم تشییع از ساعت ۶ صبح روز ۱۲ تیر تا یک ساعت پس از تدفین، بیمه شدند
@withyashar
سه‌شنبه ۱۶ تیر نیز تهران تعطیل شد</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/16250" target="_blank">📅 10:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16249">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بی‌بی‌سی: ترامپ در سال گذشته بیش از یک میلیارد دلار از فعالیت‌های تجاری، به‌ویژه در حوزه رمزارزها، درآمد کسب کرده است
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/16249" target="_blank">📅 10:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16248">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وال‌استریت ژورنال: عربستان ابتدا دسترسی نظامی آمریکا به پایگاه‌ها و حریم هوایی خود را برای عملیات امنیت تنگه هرمز محدود کرد که با تهدید واشنگتن به تعلیق تحویل سامانه‌های دفاع هوایی همراه شد.
هرچند ریاض بعداً موضع خود را تعدیل کرد، اما این اختلافات و تنش‌های دیپلماتیک اخیر باعث شده آمریکا به کاهش حضور نظامی خود در عربستان فکر کند.
@withyashar</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/16248" target="_blank">📅 09:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16247">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وال استریت ژورنال به نقل از مقامات آمریکایی:
ترامپ در حال بحث درباره احتمال تجدید حملات نظامی گسترده به ایران با وزیر جنگ و رئیس ستاد مشترک ارتش است ، اما تصمیم گرفته است که مذاکرات دیپلماتیک را در حال حاضر ادامه دهد.
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/16247" target="_blank">📅 09:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16246">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f21403e97.mp4?token=MEbEdpraB9mieaYpefEyGC8rlkDqiSPRe8NyFjaSPf5LIYfOoVewJsJS5nbp8dBg_cbrCywZuG2KZBifupqybaIotX3kYzYMd76iY_3S5IVk8Bga7PJnkT_R33FCJETE_0kdEzY2Z9yARhe9Z57PP6I4t5UcLO7SwSIL5UGVy7tkI2VXclr688jdVfYWwf5IlwBH4NJkLuds-hIoxweD3QbYiMNIGc6bAc9HZj1iWMFickuEqazVA92y3fpjkFG-BzPsbkIdhHqswq7-iYB--sVQ9X2Gm0ShbUT9k4vHiRmPUgZrCoFAhX7dTGlwykgVXTJbJUwXW3eMxkOx7uX5qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f21403e97.mp4?token=MEbEdpraB9mieaYpefEyGC8rlkDqiSPRe8NyFjaSPf5LIYfOoVewJsJS5nbp8dBg_cbrCywZuG2KZBifupqybaIotX3kYzYMd76iY_3S5IVk8Bga7PJnkT_R33FCJETE_0kdEzY2Z9yARhe9Z57PP6I4t5UcLO7SwSIL5UGVy7tkI2VXclr688jdVfYWwf5IlwBH4NJkLuds-hIoxweD3QbYiMNIGc6bAc9HZj1iWMFickuEqazVA92y3fpjkFG-BzPsbkIdhHqswq7-iYB--sVQ9X2Gm0ShbUT9k4vHiRmPUgZrCoFAhX7dTGlwykgVXTJbJUwXW3eMxkOx7uX5qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها) , سپاه پاسداران که بیضه های این ارتش هم نمیشه
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16246" target="_blank">📅 02:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16245">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رویترز : مقام‌های فرانسوی تجمع بزرگ شورای ملی مقاومت ایران (مستقر در پاریس) را پس از آن ممنوع کردند که نهادهای امنیتی نسبت به افزایش تهدید از سوی فعالان سلطنت‌طلب رقیب هشدار دادند.
پلیس پاریس این تجمع را که قرار بود در ۲۰ ژوئن برگزار شود، تنها چند ساعت پیش از آغاز لغو کرد و دلیل آن را فضای به‌شدت متشنج داخلی و بین‌المللی و خطر بروز خشونت اعلام کرد.
تجمع‌های پیشین شورای ملی مقاومت ایران، که توسط بازوی سیاسی سازمان مجاهدین خلق ایران سازماندهی می‌شود و شرکت‌کنندگانی از سراسر اروپا و جهان را جذب می‌کند، معمولاً بدون حادثه برگزار شده است.
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/16245" target="_blank">📅 02:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16244">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_Wy_3blAwlr7U3_VPugosxhUvZPLKlnLUKMITvSel9Daqm9hkBMeweuZagTIw8BFu2d1LSNSuqEXlhtXu9bza9XSEyevtO-wnOTZWuzwG49DihL-R2fp8A8suNNWx0YFglLln7xkfw_mnYe8m_VzhLLk8ZMeffNK6AI4EtspjkgcC8FntRU7IcEMn_Ug7_lF3JVFwxvoCJsOo9kuXdy57Ksmtd5MU8Gg4P26-yXQAfUPc_yqH439fSu39-N_DhjlOdcD3891LCExBlbHCxhzfIFF2ubFZbj82YCFJIWpUg-HPrhsOasU0a-f1WCzQO5VUuDBoMfz90tRRhYiDrDpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون پنج فروند بوئینگ 777-268ER سابق سعودی به ماهان ایر، بزرگترین شرکت هواپیمایی ایران، تحویل شده. کاربر نهایی این هواپیماها، یک شرکت هواپیمایی مستقر در اصفهان متعلق به یک میلیاردر ایرانی است.
از پنج فروند، دو فروند در حال حاضر در فرودگاه بین‌المللی مهرآباد تهران هستند.
@withyashar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/16244" target="_blank">📅 01:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16243">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نتانیاهو:
حزب‌الله چیزی شبیه به «پنتاگون» را در زیر زمین احداث کرده است
@withyashar</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/16243" target="_blank">📅 01:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16242">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BS7CNkb9Q814GhZ4TsAHBJDKoXjq8QrwmCIEbqku51DR6uhvjKVYCbcGNWzHh9qd_DD7uO9dqDKjR9IeY0390ywyiGIaCp7en7IW2lS9DTdfL5BA5ewYRC4FXo8uU54QH0VARsqMvIqUhcKLIdLAPu1ToWD2mDHI_D633cWhUm3fgOto85YIh7ka3t6bbT3ypBZEpcISg38K95nQUP1bliIYhcRDFweCnexg6AImARq9-sVQHblmNmuW6-rNLxDsPgMQdARSgoA-AOlMPSSl3v0_khpgfjQJTeQpUtpW1jRvB6P718d9z23Af_47LhJgYDw3trCQTAWW7jho4oncPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : ناو آبی خاکی باکسر داره میاد ! ۴ ناو ۱ آرایش رو به جلو و آماده به سمت خاورمیانه  یو اس اس باکسر، یو اس اس پورتلند، یو اس اس جان ال. کنلی و یو اس ان اس پیلیلائو در آرایش جنگی در اقیانوس هند حرکت می‌کنند و تحرک و پایداری آبی-خاکی را در دریا…</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/16242" target="_blank">📅 01:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16241">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رسانه رسمی قالیباف بعد از اینکه صداوسیما مصاحبه‌ رو قطع کرد، اعلام کرد بخشیهایی که پخش نشد درباره این موضوعات بوده؛
پاسخ به ادعای بازرسی آژانس از سایت‌های ایران.
جزئیات پیگیری آزاد شدن پول‌های بلوکه‌شده ایران.
توضیح درباره اعتبار 300 میلیارد دلاری برای بازسازی که تو متن تفاهم اومده.
پاسخ به ادعاها و حرف‌های ترامپ.
توضیح درباره پیام راهبردی رهبر جمهوری اسلامی تو 28 خرداد.
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/16241" target="_blank">📅 01:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16239">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prbl_yiQ6LRk2rZ2ymOM2LRpWiULPzmEo7zO4_I-AhaMnqng7Ddp13HavupVVpGqACC86JUYSGgp2agVq3cTORa0PnesjXaa4CXh_ERoPQn2qhyC8IqasHgzAbvaBydYsPIsw5-Ox9tJ0vLjq_SyeY1Q9r7qoL9Ud5DX1ks_J6wQ1IIPT6NVzpmCxjhFh5MngAEBX0qw-7BJL5edR5Re1o85NpJ608semEx9Bh83cUuB4-wqYgKjyoTA0kySBIy3T2JePyN0vqP9yDD83Egap2mOnw4gHF7kAaMjvSA8YqAELCXO3JOeBJ3aUPKHETqk2wZ6A6Nni3P8cNcCMKYUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9663206797.mp4?token=QdjyPUcgUt84psNIku08cRXiRLYmYAQmdwFpX3dprEM8MfXatKArMki8l6oYT_8P-809McmjqPFrbcZWh4ZI_XarU_mwwHjczqVewtq206JcFB8pe6eagcEztwv_Af-_kZpxDb8vc2Tb0B-4zYQnRY_aSYbcV8BO0GqfRP30q-VYmgac2hcrgZEtPzLcooCKpTyXS14X6LrhXUHxqCBQVBCuoz6X0rFqDD5bTsI26mXahRu2ABbq0O_m3NjvXc1RwL6X0zcAnlUiSHRJQAinhYs2e3o7eME0sC8-H0gcWxjuJH4AC2_q5Y1z5Q6mIQNZU_WkSRn43DqE8OcfiFQkSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9663206797.mp4?token=QdjyPUcgUt84psNIku08cRXiRLYmYAQmdwFpX3dprEM8MfXatKArMki8l6oYT_8P-809McmjqPFrbcZWh4ZI_XarU_mwwHjczqVewtq206JcFB8pe6eagcEztwv_Af-_kZpxDb8vc2Tb0B-4zYQnRY_aSYbcV8BO0GqfRP30q-VYmgac2hcrgZEtPzLcooCKpTyXS14X6LrhXUHxqCBQVBCuoz6X0rFqDD5bTsI26mXahRu2ABbq0O_m3NjvXc1RwL6X0zcAnlUiSHRJQAinhYs2e3o7eME0sC8-H0gcWxjuJH4AC2_q5Y1z5Q6mIQNZU_WkSRn43DqE8OcfiFQkSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای افغان به مناطقی در بلوچستان پاکستان حمله کردند و درگیری‌های مرزی آغاز شد.
@withyashar</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/16239" target="_blank">📅 01:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16238">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKE-a-ZfKcUWxqqODyDhg0NmlOTryWfqCZTS8xChNANGsdrApq51IRqKpISROyYaVL6P4_m0uOE37DxopDjL20-yHJqgu5ZlPa0dcTUcDSFFsSf84V8H_Jy5Vj4t0aHL4EW2TWSTyEk0kZjxng-Cb6B61TofI6hbRZQAIVnuqOxETAak59YEkGqQ1TBdfXwWEuf0opWcY2onhxxBH6lJiGWhA3r0r99L2HRHzYM3PZBznWnQXDE5y4IVZ-rZ-JgdayszPOa8s-kPQagpcYYZ1p8kHLxg55ySwzbe5pT2xxigC35UwloCw-PAGP6wEPqr0s-V7jRdP9DqD4Ozcf-lWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاروان‌های کامیونی پر از تابوت جدید از تروریست‌های حزب‌الله که توسط اسرائیل نابود شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/16238" target="_blank">📅 00:59 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
