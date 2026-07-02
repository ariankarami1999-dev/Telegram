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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 15:33:43</div>
<hr>

<div class="tg-post" id="msg-16330">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏دبیر کل حزب دموکرات کردستان ایران ، مصطفی هجری گفته: ‏حمله زمینی به ⁧ ایران⁩ مطرح است اما پیشروی تا تهران در دستور کار  نیست، اگر شرایط مهیا شود تا ارومیه پیشروی خواهیم کرد @withyashar</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/withyashar/16330" target="_blank">📅 15:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16329">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏دبیر کل حزب دموکرات کردستان ایران ، مصطفی هجری گفته:
‏حمله زمینی به ⁧ ایران⁩ مطرح است اما پیشروی تا تهران در دستور کار  نیست، اگر شرایط مهیا شود تا ارومیه پیشروی خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/withyashar/16329" target="_blank">📅 15:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16328">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کانال ۱۴ : منابع مستقر در قطر گزارش می‌دهند که ایران در جریان مذاکرات غیرمستقیم و مهم این هفته با ایالات متحده در دوحه، تضمین‌های امنیتی محکمی دریافت کرده است و تضمین می‌دهد که مقامات و فرماندهان ارشد نظامی این کشور در مراسم تشییع جنازه آیت‌الله علی خامنه‌ای، رهبر فقید ایران، هدف قرار نگیرند.
@withyashar</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/withyashar/16328" target="_blank">📅 15:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16327">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الحدث : پس از ۱۲۵ روز از کشته شدنش.. ترتیبات استثنایی برای «تشییع جنازه خامنه‌ای»
@withyashat</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/withyashar/16327" target="_blank">📅 14:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16326">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">الحدث : دور بعدی مذاکرات هفته آینده با حضور عراقچی و قالیباف در  در بورگن اشتوک سوئیس براگزار خواهد شد
@withyashar
العربیه: دور بعدی مذاکرات آمریکا و ایران در ۱۸ ژوئیه برگزار خواهد شد</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/withyashar/16326" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16325">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16cdb8cfe8.mp4?token=XV1kvr5EjonYN7LvISLdC14YR8h3iWCBbHZn_inzmXGuIjFE_HDT3Nc0cbyHz3FnZmJ90Njd8qorI6-esSe9_IOg106yhsdP7S9BwOaViv83XlcsHDVnNJjd3iZZCyNPeWt-afcxTBI1kyrGwczzxLVMDjp5OSsgaVznMYU6XXjzeox4trZ1DL7iKIZY7g_xDTc9giFELxHZh1AiCWW-gP9TZlfl5kIjPkfrnxuv_PrQ1pAgQswOdU5LW2YuRrOLCRmUJf-benw-3fLAf_eRCPYJoERuLbRAPzi8QfuNp9-kOvv49lXsnqzzIDjbsd1KR2EzXorZEU1elsVJPdxBrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16cdb8cfe8.mp4?token=XV1kvr5EjonYN7LvISLdC14YR8h3iWCBbHZn_inzmXGuIjFE_HDT3Nc0cbyHz3FnZmJ90Njd8qorI6-esSe9_IOg106yhsdP7S9BwOaViv83XlcsHDVnNJjd3iZZCyNPeWt-afcxTBI1kyrGwczzxLVMDjp5OSsgaVznMYU6XXjzeox4trZ1DL7iKIZY7g_xDTc9giFELxHZh1AiCWW-gP9TZlfl5kIjPkfrnxuv_PrQ1pAgQswOdU5LW2YuRrOLCRmUJf-benw-3fLAf_eRCPYJoERuLbRAPzi8QfuNp9-kOvv49lXsnqzzIDjbsd1KR2EzXorZEU1elsVJPdxBrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : با توجه به داده ها به نظر میرسد کشتیهایی که از مسیر امن آمریکا در نزدیکی عمان رفت و آمد می کنند، نسبت به مسیری که جمهوری اسلامی تعیین کرده بیشتر است.
@withyashar</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/withyashar/16325" target="_blank">📅 13:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16324">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بلومبرگ:جمهوری اسلامی ایران کنترل مؤثر خود بر تنگه هرمز را از دست داده است.مقام آمریکایی اعلام کرد حمایت نظامی آمریکا و کمک به احیای جریان نفت و تجارت از تنگه هرمز در هفته‌های اخیر به بیش از ۱۰ میلیون بشکه در روز افزایش یافته است.
این افزایش ایران را غافلگیر کرده، توانایی آن برای کنترل ترافیک را محدود و به حملات اخیر اطراف تنگه کمک کرده است.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/withyashar/16324" target="_blank">📅 13:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16323">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">غضنفری نماینده مجلس :
یک کودتا علیه رهبری مجتبی خامنه ای در جریان هست
@withyashar</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/withyashar/16323" target="_blank">📅 13:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16322">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">امروز صبح، علی عبداللهی، فرمانده "خاتم‌الانبیای" (فرماندهی عملیات مشترک نیروهای مسلح ایران)، هشدار صریحی به اسرائیل و آمریکا داد و از "هرگونه محاسبات اشتباه" در طول مراسم عزاداری خبر داد. او گفت که این اقدام، "واکنش‌های شدید و ناخوشایندی" از سوی نیروهای امنیتی ایران به دنبال خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/16322" target="_blank">📅 13:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16321">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وقتی یک ماه پیش من گفتم در روابط عربستان و آمریکا تنش جدی ایجاد شده ، یک اینفلوئنسر تندرو سلطنت‌طلب که شبیه ته نون باگت است، حمله سختی به من کرد.</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/withyashar/16321" target="_blank">📅 12:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16320">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نیویورک پست: تنش در روابط عربستان و آمریکا بر سر ایران و نگرانی از جنگ و تهدید منافع نفتی با احتمال بسته شدن تنگه هرمز افزایش یافته است @withyashar</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/withyashar/16320" target="_blank">📅 12:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16319">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نیویورک پست: تنش در روابط عربستان و آمریکا بر سر ایران و نگرانی از جنگ و تهدید منافع نفتی با احتمال بسته شدن تنگه هرمز افزایش یافته است
@withyashar</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/withyashar/16319" target="_blank">📅 12:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16318">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یک منبع عبری : سقوط هلیکوپتر روز گذشته آمریکا توسط ایران بود
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/withyashar/16318" target="_blank">📅 12:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16317">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نتانیاهو: ممکن است جنگجویان کُرد ،حملات خود را به غرب و شمال غرب ایران امشب یا شب های بعد آغاز کنند.‌‌‌‌
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/withyashar/16317" target="_blank">📅 12:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16316">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بعد از حمله به بیت، اعلام کردن منصوره خجسته باقرزاده، همسر خامنه‌ای کشته شده.
اما بعد از اینکه مجتبی پیام تسلیت داد و یادش رفت اسم مادرشو بیاره، خبرگزاری‌ها تکذیب کردن و گفتن زندس!
الان دوباره گفتن کشته شده و قراره همزمان با علی خامنه‌ای، براش مراسم بگیرن.
@withyashar</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/withyashar/16316" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16315">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0gM4XpF9TiGgy7yLRI_cEF5XXi3s4dfedm48nx6tpw1tifDUDIr16WQqiomYb7EPky9glHfWnuvXkwFnxWpxp6Vb8ijNjhDvrWOu39yrYp6lK2A2pHhuAj0F-uWZPdKsJeOrx_ki2hNJ_5nYmRHOEXpca9TCHmqV0-96ryyMZLhaNpurgm8XxwfFKLOtahDgMwjHOFJN7NJQ0qjWhH1RqA1nncpicIDnKCJbaorH7U4G9osll5CF3veCZzYke3nxrqr5qA4HvhUTX--Tj5wk-ZVjSpm4XK8GxKQevUMzRCR15XQeY8SvMpn1RsfXH4TKVPqlGyyVnIZH0rpnHDtgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمودار سقوط دستمزد و ارزش پول ملی ایران از سال ۲۰۱۰ تاکنون
حالا اگه درامدت دلاری بوده این نمودار برعکس میشه
@withyashar</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/withyashar/16315" target="_blank">📅 12:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16314">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">فرمانده  خاتم الانبیا، گفت : «تنگه هرمز زمین بازی آمریکا نیست، بلکه قلمرو حاکمیتی تهران است. همه نفتکش‌ها و کشتی‌های تجاری موظفند فقط از مسیری که تعیین کرده عبور کنند.» آنها بعداً تهدید کردند که «هرگونه عدم رعایت پروتکل‌های ناوبری ایران در تنگه هرمز با واکنش فوری و قاطع نیروهای مسلح مواجه خواهد شد. ادامه حضور جنگنده‌های آمریکایی بر فراز تنگه هرمز، امنیت کل منطقه را به خطر می‌اندازد.»
@withyashar</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/withyashar/16314" target="_blank">📅 12:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16313">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">1$ Tether = 178,000 Toman
@withyashar</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/withyashar/16313" target="_blank">📅 12:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16312">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/16312" target="_blank">📅 11:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16311">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت
وزارت امور خارجه پاکستان اعلام کرد ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
طبق اعلام اسلام‌آباد، زمان برگزاری
نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر سابق ایران تعیین خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/withyashar/16311" target="_blank">📅 11:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16310">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یک منبع آگاه:حال روحی آیت الله مجتبی خامنه ای مناسب شرکت در مراسم رهبر انقلاب نیست
@withyashar</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/withyashar/16310" target="_blank">📅 11:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16309">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/withyashar/16309" target="_blank">📅 11:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16308">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d47807c6.mp4?token=XfyJzQFaRrMxWvdalgbofH8eubgpZsTszan_MSQTJ_1YvZA2sYjRTPrJey26v0Vn9nRN6YRZQTE2FFbZ6ozk-dFMN_TG2URRcOPw-seoLLDJJuijTOSxHVBZgX2rABHooWOKoOWbV9DDndnKLfaxJKp-dQ6WaVxvav9mUjLeQh_ZGNanrnysBlCajkop68OVX1eo4DnpTWJu8A8946-nsDN4uZaYL1Vvxc-6dfhoCFi3v1469uDB9NresM4s9n2GDt3zOddgYXh1-yL4IzkZdgwzl445Hlt6m1rikXEX6vW7D-eLoVkvYrDxdS_tcpWrK8QF26YOSScxoOrBtJOwwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d47807c6.mp4?token=XfyJzQFaRrMxWvdalgbofH8eubgpZsTszan_MSQTJ_1YvZA2sYjRTPrJey26v0Vn9nRN6YRZQTE2FFbZ6ozk-dFMN_TG2URRcOPw-seoLLDJJuijTOSxHVBZgX2rABHooWOKoOWbV9DDndnKLfaxJKp-dQ6WaVxvav9mUjLeQh_ZGNanrnysBlCajkop68OVX1eo4DnpTWJu8A8946-nsDN4uZaYL1Vvxc-6dfhoCFi3v1469uDB9NresM4s9n2GDt3zOddgYXh1-yL4IzkZdgwzl445Hlt6m1rikXEX6vW7D-eLoVkvYrDxdS_tcpWrK8QF26YOSScxoOrBtJOwwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره‌ای از سایت هسته‌ای اصفهان نشان میدهد ورودی‌ها همچنان مسدود هستند و هیچ نشانه‌ای از فعالیت جدید دیده نمی‌شود. گفته می‌شود بخشی از مواد هسته‌ای غنی‌شده ایران در این مکان نگهداری می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/16308" target="_blank">📅 10:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16307">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سایت The War Zone با استناد به گزارش‌های محلی اعلام کرده است که هر شش بمب‌افکن استراتژیک B-52H Stratofortress حاضر در پایگاه RAF Fairford در بریتانیا، پایگاه را ترک کرده‌اند و احتمالاً به ایالات متحده بازگشته‌اند.
دوازده بمب‌افکن استراتژیک B-1B Lancer همچنان در پایگاه باقی مانده‌اند که این تعداد نسبت به هجده بمب‌افکن استراتژیک قبلی کاهش یافته است
@withyashar</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/withyashar/16307" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16306">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سقوط قیمت نفت برنت به کانال ۷۰ دلار
بعد از افزایش عبور از تنگه هرمز، قیمت هر بشکه نفت WTI به ۶۷ و هر بشکه نفت برنت نیز به ۷۰ دلار کاهش پیدا کرد
@withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/16306" target="_blank">📅 10:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16305">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/16305" target="_blank">📅 02:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16304">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گروه
حزب آزادی کردستان ( پاک ) مستقر در منطقه کردستان عراق نیز در بیانیه‌ای اعلام کرد که دفتر مرکزی آن در استان اربیل هدف موشک بالستیک قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/16304" target="_blank">📅 01:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16303">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کانال 14 اسرائیل: مرکز فرماندهی منتسب به سپاه پاسداران در لبنان توسط ارتش اسرائیل (IDF) تصرف شد
@withyashar</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/16303" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16302">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رسانه های رژیم : در ساعات گذشته دو مقر گروهک های تجزیه طلب متعلق به گروه‌های تروریستی در اقلیم کردستان عراق هدف حمله قرار گرفته‌اند.
بر این اساس، یکی از حملات مقر گروهک تروریستی دمکرات در منطقه کویه را هدف قرار داده و حمله دیگر نیز مقر گروهک تروریستی پاک در منطقه بالکایتی را مورد اصابت قرار داده است.
‎
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/16302" target="_blank">📅 01:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16301">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سپاه: در پاسخ به اقدامات گروهک‌های کرد که منجر به کشته‌شدن سه نیروی فراجا شد، یکی از مقرهای این گروهک در منطقه دِیکله (شمال کردستان عراق) هدف حمله قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/16301" target="_blank">📅 01:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16300">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش هایی از ارسال تجهیزات گسترده ارتش جمهوری اسلامی به خصوص نیروی زمینی به منطقه غرب کشور
این حجم تجهیزات  بعد از زمان درگیری با داعش بی سابقه هست
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/16300" target="_blank">📅 01:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16299">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رویترز به نقل از منابع امنیتی عراق گزارش داد یک پهپاد حامل مواد منفجره به اردوگاه یک گروه مخالف کُرد ایرانی در شرق اربیل عراق برخورد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/16299" target="_blank">📅 01:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16298">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گزارش های زیاد از شلیک لانچر در ارومیه
🚨
@withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/16298" target="_blank">📅 00:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16297">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhW1uJ7BLvMiuc-rmas147Ew59s4Ie_CoCIxXAs6wbpebYp3Gyqt04MgyrCxroVpxN8VkxvjHnILEy5Vp_dluE5E6X2R56eY2bB4FGyTNurhRofTkWpe_D9XZ_s4-StwPtOBG6Tjs0zdW_oa_XN1dK3O2MR9CxDs54sslcoF0YD-qyTB5UwWO0JxwSN4Vq1gzVXQyw3THm5WMQwxcFBuJv8vb9YOZiP1KqGqEy-hoRXh_YnN9gIveIaaOVi9zo4-3pmWhLl_1WJxWo5pazq2KVZg712B6crASPrcLgTvQPcI0odtI9Gstn45nI2XfFBNNwuEhDWgv5EHt_tswFY1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق نظرسنجی شورای جهانی طلا از ۶۹ بانک مرکزی، رکورد ۹۰٪ از بانک‌های مرکزی عملکرد طلا در زمان‌های بحران را به عنوان عامل کلیدی در تصمیم خود برای نگهداری طلا ذکر کردند.
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/16297" target="_blank">📅 00:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16296">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc829af2ea.mp4?token=Zpnbk1J0oNTkNBdNO-SpFswUCQYoES72UEYyMPzFewKL3Wp4InEfcADC1jGbdtpHoXIp0iwu0ME_KNSZjZGQdEEoxyYhq3SIuvKnDT3Fzwfw-PT-xcL4s5SdfylVUaInvo07NrSNGAcvh4r1bFPh0kOacUf_bjjKVE_nwLQiOg_6sCxsdOHjrr0lYJFXhb3DTZVV6OSlH3FHQ-moBF0xO47ZC4sEmNubQDRQ9OfMxbVJNfpEtaOxetuUV6kyrR_CW907jG40botlMq7jJa8nMXcZ-rk-GQrz2rtvLtZOhNkLSK1Bs_IP1HCUGX8IEZT4JTEOmhzMLNWfmeHXW3ONRiAiSHEAf06X2GMBfneZAM5NFE9NOKqtFdwQo4ki5V7KcveB0NE9JGxtA0yUPsj-FGhW9PbqfDct0AFAYJZqR2prKrUjyNSItWYO9_wyDtrYF7j68YWdjhmeaHo21QtbTePToQA2sUw0Aq2mYyInwbWPdzhlRAHJhuYNiBtQwHFNat3ZsguolMfdBcSWqLvf1gVO6lZhwcQBCRDnDqDsFfCnj7TH46Yr5q65Xan1cIJGOagdffuI-7y86u1-6fSCuNW19pU7aSZytm2ie3U2z_0VATWQpSB8F_KMgX3DxTQVywuUcBBPS29MW7YxtbpOFhGGN0R_KfUwj74uN8XygUo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc829af2ea.mp4?token=Zpnbk1J0oNTkNBdNO-SpFswUCQYoES72UEYyMPzFewKL3Wp4InEfcADC1jGbdtpHoXIp0iwu0ME_KNSZjZGQdEEoxyYhq3SIuvKnDT3Fzwfw-PT-xcL4s5SdfylVUaInvo07NrSNGAcvh4r1bFPh0kOacUf_bjjKVE_nwLQiOg_6sCxsdOHjrr0lYJFXhb3DTZVV6OSlH3FHQ-moBF0xO47ZC4sEmNubQDRQ9OfMxbVJNfpEtaOxetuUV6kyrR_CW907jG40botlMq7jJa8nMXcZ-rk-GQrz2rtvLtZOhNkLSK1Bs_IP1HCUGX8IEZT4JTEOmhzMLNWfmeHXW3ONRiAiSHEAf06X2GMBfneZAM5NFE9NOKqtFdwQo4ki5V7KcveB0NE9JGxtA0yUPsj-FGhW9PbqfDct0AFAYJZqR2prKrUjyNSItWYO9_wyDtrYF7j68YWdjhmeaHo21QtbTePToQA2sUw0Aq2mYyInwbWPdzhlRAHJhuYNiBtQwHFNat3ZsguolMfdBcSWqLvf1gVO6lZhwcQBCRDnDqDsFfCnj7TH46Yr5q65Xan1cIJGOagdffuI-7y86u1-6fSCuNW19pU7aSZytm2ie3U2z_0VATWQpSB8F_KMgX3DxTQVywuUcBBPS29MW7YxtbpOFhGGN0R_KfUwj74uN8XygUo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش شبکه آی24: سیا و موساد در طرح استفاده از نیروهای کرد به عنوان بخشی از تلاش گسترده‌ علیه ایران نقش داشته‌اند
@withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/16296" target="_blank">📅 23:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16295">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/16295" target="_blank">📅 23:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16294">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گزارش های زیاد از شلیک لانچر در ارومیه
🚨
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/16294" target="_blank">📅 23:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16293">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b695ead9.mp4?token=ndutm7rdYJqBHQeTGkuImU9wkJWen8rWL-TiNO5Cnz5089mED99AbKrcDs4rATa8yv-Cjpra74UT4GZQPNJJt_dz5pi75oOVaMFL5IJrYGz2lL4wtCDBpEzBZqOh0jfb3G1R3iNs8L5qg8xJCbXOCOV2uyqygWmOpDFzORuwvRka440_VLbSLSfF-Rha9Gn0_R9QJLeZ9InFSapkOyUGt16ym_yFvB6hdZgk-TSMlUB0GNHVB-PBXWP6_J-KzebkNRKqjZmTPthudkbMv8O46gbpQNeX6OUPlhaDyTeF7q5WZhipCvBmJDsy4mfbHLX_SVSdBs2BBZaV5mC8mxpusg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b695ead9.mp4?token=ndutm7rdYJqBHQeTGkuImU9wkJWen8rWL-TiNO5Cnz5089mED99AbKrcDs4rATa8yv-Cjpra74UT4GZQPNJJt_dz5pi75oOVaMFL5IJrYGz2lL4wtCDBpEzBZqOh0jfb3G1R3iNs8L5qg8xJCbXOCOV2uyqygWmOpDFzORuwvRka440_VLbSLSfF-Rha9Gn0_R9QJLeZ9InFSapkOyUGt16ym_yFvB6hdZgk-TSMlUB0GNHVB-PBXWP6_J-KzebkNRKqjZmTPthudkbMv8O46gbpQNeX6OUPlhaDyTeF7q5WZhipCvBmJDsy4mfbHLX_SVSdBs2BBZaV5mC8mxpusg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحلیلگر ژئوپلیتیک چینی: امضای تفاهم توسط ترامپ، فقط برای عبور از گرمای تابستان منطقه است!
۶۰ هزار سرباز آمریکایی آماده حمله زمینی به ایران هستند.
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16293" target="_blank">📅 22:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16292">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/16292" target="_blank">📅 22:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16291">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تحقیق جدید نیویورک تایمز : بیش از دو میلیون سرباز روس و اوکراینی از ابتدای جنگ بین این دو کشور کشته یا زخمی شده‌اند. روسیه بیش از ۱.۴ میلیون سرباز از دست داده است که در میان آن‌ها حدود ۴۵۰ هزار کشته وجود دارد. اوکراین بین ۵۲۵ تا ۶۲۵ هزار سرباز از دست داده است که در میان آن‌ها ۱۲۵ تا ۱۵۰ هزار کشته وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/16291" target="_blank">📅 22:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16290">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD3ieVUjcDBU8HqBQEV-oYN3efw3gcd5l3nmI1OnK-qssmzlWYVzkUUEvibI35K2ogVDYNflk21KUsN34vxBtebsAB1xY2z1Pgf1_OmU3tk-keQ_SRzGVRhdXejpVRl0gsRrJgexWPHcLPTykopCa_BYO-vSeISgUZT9BXB8vA2XrdgUCc3SB1jZ_bCGsQlWCrnZgFFVAxtQ54IppwkwOa-cI8BkBesr6UvfXz4Iks4YL-DPv5Vwc7bAH70SrBHBYTcktr8RvRLEk10RgDH3bwE8mUNWMZEbkM1ZUk4xhoyAIcqrR-sYobTX7BxUU9gibyP1cs0anX7_oXvWBo9xEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو گروه از کشتی‌های نفتکش/کانتینربر تحت اسکورت هوایی و دریایی ایالات متحده از تنگه هرمز عبور می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/16290" target="_blank">📅 22:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16289">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سفیر آمریکا: «رابطه واشنگتن و تل‌آویو شبیه یک ازدواج ایده‌آل است که در آن جایی برای طلاق وجود ندارد»
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/16289" target="_blank">📅 22:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16288">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78447e35bd.mp4?token=XIt_XmYx1W4dLnXwOEBesJnWroJ4qEaWvfVRl0dVvPTbBRtUp79nILZpzRTH8JGUDObs2H3e8UNiQ2SOdLQolvtO-KxTrPpX-GyV1Oc8Y1DvD3xd8Z1wrTcsHiRL397vX8qntKI-_zx995Up-JcOrS6W73Bl-fKJi3hpJ2QgaWdUlWUmyrvH2YviJGaWbUVGfLFbU66YhA3T-vi_Y2rR5saYym2V3RsBwU9qs4o6q46tLDFwDZa2T-FqbGx8ufMim95p7WWjg2QhikhtpULCFHk3jcXPWliy6_UmWJkai3bh2QOureGDFth5oDRQQcb7_zO-i19l0kYYEwnJ11AFUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78447e35bd.mp4?token=XIt_XmYx1W4dLnXwOEBesJnWroJ4qEaWvfVRl0dVvPTbBRtUp79nILZpzRTH8JGUDObs2H3e8UNiQ2SOdLQolvtO-KxTrPpX-GyV1Oc8Y1DvD3xd8Z1wrTcsHiRL397vX8qntKI-_zx995Up-JcOrS6W73Bl-fKJi3hpJ2QgaWdUlWUmyrvH2YviJGaWbUVGfLFbU66YhA3T-vi_Y2rR5saYym2V3RsBwU9qs4o6q46tLDFwDZa2T-FqbGx8ufMim95p7WWjg2QhikhtpULCFHk3jcXPWliy6_UmWJkai3bh2QOureGDFth5oDRQQcb7_zO-i19l0kYYEwnJ11AFUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان پرزیدنت ترامپ توسط سوارکاران خشن (Rough Riders) تا کتابخانه ریاست‌جمهوری تئودور روزولت همراهی شد.
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/16288" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16287">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5fcb8e951.mp4?token=ZcTnGj15cg1e6Sl6hYhOURRSogywuK6v6zTc9JM-lpfUxYlvMQFZmpNMsRItIDIYIK4MfWNSuzYfK0Y_MLWK2u6rTIJ3Lj8cD2-cflkElk_tpv5WmsuZJQLSxZyPJNXKhUDSJFuoVqQhYe3cPnP1Kk7WBwu57rF81bERUUKGYwo16ENz6L4pvYQaFzDbugj1dhHqpbsE-TyolxYHhZdlujvWklJ9UpHr9MQXkvvU9b8FaN9ehcvq-HcOZ-LepC5FXFYVm2PxQY24VeWSJQ1BrTPRXCUHwP-T4mp4xkPM45eEdawfp5PTXFob4k9D4S_6fA8pb1r-Lk8hWjvCGnBQfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5fcb8e951.mp4?token=ZcTnGj15cg1e6Sl6hYhOURRSogywuK6v6zTc9JM-lpfUxYlvMQFZmpNMsRItIDIYIK4MfWNSuzYfK0Y_MLWK2u6rTIJ3Lj8cD2-cflkElk_tpv5WmsuZJQLSxZyPJNXKhUDSJFuoVqQhYe3cPnP1Kk7WBwu57rF81bERUUKGYwo16ENz6L4pvYQaFzDbugj1dhHqpbsE-TyolxYHhZdlujvWklJ9UpHr9MQXkvvU9b8FaN9ehcvq-HcOZ-LepC5FXFYVm2PxQY24VeWSJQ1BrTPRXCUHwP-T4mp4xkPM45eEdawfp5PTXFob4k9D4S_6fA8pb1r-Lk8hWjvCGnBQfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیروز کریمی روی آنتن زنده صداوسیما: قلعه نویی 5 سانت و 10 سانت رو تحمل کرد ولی 30 سانت رو میخواد کجاش بذاره؟!
@withyashar</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/16287" target="_blank">📅 21:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16286">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UncKG9TNBjJN_rS7PsMDdMR4qddWnyLtUKIJRu92TanXIT3Rf0GLZtfpKbHDQrv37eiabKroiZci4OgCOgY8FHlPxjd9K1T-a9ytHjvmvABKuG_-wNQ_8XwvwJ8EnDsefEhk3tal--5qaf7NWNq0JWBI3H2ROFPtkI9rAU9XPQtyX1IWysP71yXn4qW1aJQcd0tfXBP9p95oLZ3Xf7PMs_iOd1cQmJBxCF11_fQbqjWlWTyYVW4AtM5z5H2CvcY5EPnOtlxFyNegtrPjDzupmgCryvl4vazzWXGGnl6jueobFku2uw8nBO0jujXy0p6tb8M3lZBhNm0QeuVghg16mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیو ۳پا از به گل نشستن کشتی متخلف «خطر شب‌ ادراری
😂
⚠️
» @withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/16286" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16285">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جی دی ونس: نمی توانم متعهد شوم که در طول ۶۰ روز به ایران حمله نکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/16285" target="_blank">📅 21:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16284">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eba86lt_tPHGQg8E5OhaD75ZqqSfaP6C335OC5bPtUv2QdhrJQM-yz-9GUKx5NUOvG3NyGT00q6r9Uc9qafyfVUUQWPk7_EnG8vC-P7hF6VavYptisv9RIXao0Q4ZC6p-Od_uCLXniR1MI-lRltLTm1Pc9gmx6juJnLZ4vxhtenQeo1s1cu8_v3xRVQIFlOjWCsL7r3CEbD9V9O9MIm0SBRH1O8q7Ck_RZHptrX7X6vxfcsWjOVPP_ylMwpe1TfQ-U3Bds-bOAK37VL5ujpqrBWez2fp7DLP4PQuj5bhiVMFgno_Hk8Vuw1B8TKCOF4oZ6C0GmbpAASGpxWTTNomHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با رسیدن ناو آبی خاکی باکسر به محدوده فرماندهی سنتکام استعداد نیروی‌دریایی امریکا در خاورمیانه افزایش می‌یابد.
استقرار ناو آبی خاکی باکسر احتمال حمله زمینی امریکا به جزایر ایرانی و حتی نوار جنوبی کشور را چند برابر می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/16284" target="_blank">📅 21:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16283">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0fcb1fe97.mp4?token=ATeQUrWHRk8HZetkX-e5EAkeMr3bIQRlA4Z44x6Y_z_fFLv9XO0nLx0rDhMNUxJC69y3YwNT51miSNZLK2gp3vaH1B71cTBz-BqDsQDFMDPjKGLi3MfGLk8j6oyRjERgKGg4F_DLD6YA7T3OE4Q_WDJRh-ZVJ3q33bayEm_nCpjJSuZ21eJ7wLhITvHp9h2xq7KKzALRzYvHD3v5c2BNxXHge6Pqvs0dxkJ2KmF3JCkTEOSyOnJlostxEqGXXzhU4p76cyY_IQJqizGtU4TYUXpMzHX4R1QuaKuIst-RvPPt7QsnndhHvKuGz7D99wdJzVoAWEaXu69FLZIJZ3pJyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0fcb1fe97.mp4?token=ATeQUrWHRk8HZetkX-e5EAkeMr3bIQRlA4Z44x6Y_z_fFLv9XO0nLx0rDhMNUxJC69y3YwNT51miSNZLK2gp3vaH1B71cTBz-BqDsQDFMDPjKGLi3MfGLk8j6oyRjERgKGg4F_DLD6YA7T3OE4Q_WDJRh-ZVJ3q33bayEm_nCpjJSuZ21eJ7wLhITvHp9h2xq7KKzALRzYvHD3v5c2BNxXHge6Pqvs0dxkJ2KmF3JCkTEOSyOnJlostxEqGXXzhU4p76cyY_IQJqizGtU4TYUXpMzHX4R1QuaKuIst-RvPPt7QsnndhHvKuGz7D99wdJzVoAWEaXu69FLZIJZ3pJyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو ۳پا از به گل نشستن کشتی متخلف «خطر شب‌ ادراری
😂
⚠️
»
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/16283" target="_blank">📅 21:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16282">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گفت‌وگوها با واسطه‌های پاکستانی و قطری در دوحه به پایان رسید، سازوکاری برای جلوگیری از تنش‌ها بین دو کشور ایجاد خواهد شد. تصمیم گرفته شد که بخشی از ۶ میلیارد دلار دارایی‌های مسدود شده برای خرید کالا بر اساس نیازهای ایران استفاده شود
@withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/16282" target="_blank">📅 20:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16281">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/16281" target="_blank">📅 20:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16280">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گزارش ها از وقوع انفجار های شدید و تیراندازی گسترده میان ارتش اسرائیل و نیرو های حزب الله در جنوب لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/16280" target="_blank">📅 20:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16279">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وال استریت ژورنال: آمریکا در حال بررسی خروج نیروهای خود از عربستان است
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/16279" target="_blank">📅 20:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16278">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رسانه‌های سعودی درباره نشست دوحه:
ایران خواستار اجرای ۵ بند از یادداشت تفاهم قبل از پرداختن به پرونده‌های دیگر شد
ایران اسرائیل را به مانع‌تراشی در اجرای یادداشت تفاهم با ماندن در جنوب لبنان متهم کرد
ایران بر حاکمیت خود و عمان بر تنگه هرمز تأکید کرد و هرگونه مسیر حمل‌ونقل دریایی در تنگه هرمز بدون اجازه خود را رد کرد
ایران بر اجرای بندهای «دارایی‌های مسدود شده» تمرکز کرد
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/16278" target="_blank">📅 20:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16277">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ارتش آمریکا:
امروز ، ساعت ۳:۳۰ بامداد به وقت شرق آمریکا، خدمه یک بالگرد MH-60S Sea Hawk متعلق به ناو هواپیمابر USS George H.W. Bush در دریای عرب فرود اضطراری انجام دادند.
هیچ نشانه‌ای وجود ندارد که این حادثه ناشی از اقدام خصمانه بوده باشد.
سه نفر از چهار خدمه نجات یافته‌اند و در وضعیت پایدار روی عرشه ناو USS George H.W. Bush قرار دارند.
یگان‌های نیروی دریایی آمریکا در منطقه همچنان در حال جست‌وجو برای یافتن عضو مفقود باقی‌مانده هستند و علت حادثه در حال بررسی است.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/16277" target="_blank">📅 20:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16276">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اتاق جنگ با یاشار : در سیزن ۹ اپیزود ۵ کارتون سیپسون ها پخش در سال ۱۹۹۷ پیشبینی شده فینال یک جام جهانی بین مکزیک و پرتقال برگزار خواهد شد ! همه نظرشون اینه که این پیشبینی برای همین جام جهانی است !
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/16276" target="_blank">📅 19:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16275">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یک مقام آمریکایی به i24NEWS درباره ادعای آزادسازی ۳ میلیارد دلار از دارایی‌های ایران:
هیچ دارایی منجمد شده‌ای آزاد نشده است و هیچ دارایی‌ای آزاد نخواهد شد مگر اینکه ایران شرایط مندرج در یادداشت تفاهم را برآورده کند.
هر دارایی آزاد شده باید به تأیید آمریکا برسد و برای خرید محصولات کشاورزی آمریکایی برای مردم ایران استفاده شود.
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/16275" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16274">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">واشنگتن پست : وزارت جنگ آمریکا در حال آماده‌سازی برای اعزام نیروهای زمینی آمریکا به لبنان است.
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/16274" target="_blank">📅 19:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16273">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اینترنشنال: مجتبی خامنه‌ای میخواد اژه‌ای رو بعد از پایان دوره پنج ساله از ریاست قوه‌قضاییه کنار بذاره. @withyashar ( البته تجربه ثابت کرده هر چیزی که ترامپ و اینترنشنال بگن، جمهوری اسلامی لج میکنه و بدتر انجام نمیده.)</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/16273" target="_blank">📅 18:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16272">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">عراق به گروه‌های مسلح طرفدار ایران دستور داد تا ۳۰ سپتامبر خلع سلاح شوند
دولت عراق به گروه‌های مسلح طرفدار ایران دستور داده است تا ۳۰ سپتامبر، همزمان با پایان ماموریت ائتلاف ضد داعش به رهبری ایالات متحده، به طور کامل خلع سلاح شوند.
@withyashar</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/16272" target="_blank">📅 18:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16271">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/190c38d298.mp4?token=d7oYc-5DMyLNrGwpTM_2mC-6fZisXy-4RScJoAlAH24WjoX3VVuGfKn7_Rx1oan1LLuxbRw4kiu2Su2aQeBjEDoey5bVknqAmVmjUYTKErE5XCzLKTt9Dl01tp9Ej_QKCgvHYMuQ87_Sn3MQ1I4lAcydzR9r_LKL8U0fmKNj8lT3gjHvkly5O0ckGt9D1Qt6dfLelouYJZF-9SSROUA5xOY9hBN9qAAft-DWCHrKpDX3CVdCDr870EvtGxUSa2OKRLgKixz60vm4LSJw6KZsMj9HK0R_y0845gsoD2n4tHY9Qh66ZGdkNkH7j-On_EskA9L-SiHOsigvq6fUsdta7Gt5DUIj3tHJfuGLNZaYaIFTjkxSbxpbEin7Lla-ZeOjhO3q1qmuyotmkajOBdCJrgiJqSz8RVJinThsNsLCPyhciXJtHGcWXQMDnKvXYhz1K_iHbrYuMfNqw5JwDHeGnnbctf48tLmurX-qRGtMxYQgp0cyds4M9TmDMXHRUenu7jsSbGOSEsmTpxTTn32DUxsGDW2r6fO17YGhCWOYzFeXfJq5QbH638XJRjR5S4lIRx7yktdT3mhCIxyPTgIf5wdwtn005lVOFN1vhFzuzAZ5nv-O4-QdDg_0J9xKlH8aPmPbu_UaUxkcDF-IA6DMt2lvk89XaAWMh4JN9DLE3jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/190c38d298.mp4?token=d7oYc-5DMyLNrGwpTM_2mC-6fZisXy-4RScJoAlAH24WjoX3VVuGfKn7_Rx1oan1LLuxbRw4kiu2Su2aQeBjEDoey5bVknqAmVmjUYTKErE5XCzLKTt9Dl01tp9Ej_QKCgvHYMuQ87_Sn3MQ1I4lAcydzR9r_LKL8U0fmKNj8lT3gjHvkly5O0ckGt9D1Qt6dfLelouYJZF-9SSROUA5xOY9hBN9qAAft-DWCHrKpDX3CVdCDr870EvtGxUSa2OKRLgKixz60vm4LSJw6KZsMj9HK0R_y0845gsoD2n4tHY9Qh66ZGdkNkH7j-On_EskA9L-SiHOsigvq6fUsdta7Gt5DUIj3tHJfuGLNZaYaIFTjkxSbxpbEin7Lla-ZeOjhO3q1qmuyotmkajOBdCJrgiJqSz8RVJinThsNsLCPyhciXJtHGcWXQMDnKvXYhz1K_iHbrYuMfNqw5JwDHeGnnbctf48tLmurX-qRGtMxYQgp0cyds4M9TmDMXHRUenu7jsSbGOSEsmTpxTTn32DUxsGDW2r6fO17YGhCWOYzFeXfJq5QbH638XJRjR5S4lIRx7yktdT3mhCIxyPTgIf5wdwtn005lVOFN1vhFzuzAZ5nv-O4-QdDg_0J9xKlH8aPmPbu_UaUxkcDF-IA6DMt2lvk89XaAWMh4JN9DLE3jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : «لوفت‌وافه» وارد میشود
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/16271" target="_blank">📅 17:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16270">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">«جان رتکلیف» مدیر سازمان اطلاعات مرکزی آمریکا (سیا) ادعا کرد که جنگ آمریکا و اسرائیل علیه ایران اکنون جنگ فناوری است و گفت: «کشوری که بهتر بتواند از قدرت فناوری استفاده کند، آینده جهان را تعیین خواهد کرد.»
@withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/16270" target="_blank">📅 16:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16269">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">جی دی ونس: ترامپ به ما گفت با توافق با ایران فعلا تنگه هرمز رو باز کنیم و ذخایر انرژی جهان رو فول کنیم تا بعد ببینیم چی میشه‌.
@withyashar</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/16269" target="_blank">📅 16:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16268">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202c2c732d.mp4?token=DS0UWAh8v7GYxqLWdbXIPFZYyLuu-T1h4Rg_cvrI5hhCajWlB0nmkwZnrDH9kxM6H_m5brchyuPy6UqDUTKCUCIiikBL3pAmd-nFno3CluM6MBKUA66XC2rXwavHCYTmnqh2OgsenSJYR_h7q6q8x8V-2n-Cgu-OgG5-SsPrZ1Jd7x0WSQ4bix9B6-deiR_9yWQjsjVra-YEUVUMU3PdMu7RvDVo8-Uu7qHV0aEPFwOfHd24bJ0Oo5kQTKbPtmqnWm34NTuwyd82jxZ1JFxhGwzvgWMoGQuWfHxAiH2JflvUG_Jhh-Io5nuj53-D-RkYpIHZNGGiMJ9wQySPEqfN4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202c2c732d.mp4?token=DS0UWAh8v7GYxqLWdbXIPFZYyLuu-T1h4Rg_cvrI5hhCajWlB0nmkwZnrDH9kxM6H_m5brchyuPy6UqDUTKCUCIiikBL3pAmd-nFno3CluM6MBKUA66XC2rXwavHCYTmnqh2OgsenSJYR_h7q6q8x8V-2n-Cgu-OgG5-SsPrZ1Jd7x0WSQ4bix9B6-deiR_9yWQjsjVra-YEUVUMU3PdMu7RvDVo8-Uu7qHV0aEPFwOfHd24bJ0Oo5kQTKbPtmqnWm34NTuwyd82jxZ1JFxhGwzvgWMoGQuWfHxAiH2JflvUG_Jhh-Io5nuj53-D-RkYpIHZNGGiMJ9wQySPEqfN4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: منتقدان شما می‌گویند که از ریاست‌جمهوری سود می‌برید.
ترامپ: من سود می‌برم چون بازار بورس در حال رشد است. همه‌ی ما داریم سود می‌بریم.
وضعیت حساب بازنشستگی 401(k) شما چطور است؟ ۸۵ درصد رشد کرده. «متشکرم، رئیس‌جمهور ترامپ!»
من سود می‌برم چون پول زیادی دارم.
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/16268" target="_blank">📅 16:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16267">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ درباره ایران:
ما سه شب آنها را به شدت هدف قرار دادیم، اما اکنون رابطه ما بسیار خوب است.
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/16267" target="_blank">📅 16:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16266">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وال‌استریت ژورنال: یک کشمکش قدرت در داخل تهران، مذاکرات صلح آمریکا و ایران را به خطر انداخته است
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/16266" target="_blank">📅 15:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16265">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پوتین: به دلیل کمبود گسترده سوخت در روسیه،صادرات هرگونه سوخت ممنوع می‌شود،قابل توجه است که ایران از روسیه بنزین وارد می‌کند و صادرات سوخت به ایران نیز متوقف می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/16265" target="_blank">📅 14:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16264">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">غریب‌آبادی‌(کاظم دست کج)در راس هیئتی متشکل از وزارت خارجه، بانک مرکزی و وزارت کشاورزی به قطر سفر کرده است، صبح امروز با شیخ «محمد بن عبدالرحمن آل ثانی» وزیر امور خارجه دولت قطر، دیدار و گفت‌وگو کرد
پس از این دیدار،
نشست سه جانبه مذاکره کنندگان ارشد ایران، قطر و پاکستان برای بررسی روند اجرای یادداشت تفاهم برگزار شد
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/16264" target="_blank">📅 14:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16263">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGnFRB4hMWkTboyl46ajW-NkijkPCQZwydEEgVAA8lqZkPUm7prYMom7tAlq_iKYpifKLet4UXv97cOJkeGHQqIlEVLq3XbaSQ1s18F0s40xuLkd0xG0dx3yUkHYhPdtcfIyDQzjEqzYW_XzEQWMCGUqKhGjn2p0urzFhJ1rhcxj8wqOiV5cGCyki03zUXEOTUmp6fGOO_zA5ibNpfBrI_hGaXvREGk49Ra6xpvqIfjQ4R4HLURcwT2glPLoddm5XJq_cZxoozhkseNm51GF0VpzCl_UrkbOXpBBsAyG1RiNGVXtvLeMMmiyIrAJQAUDYS3FXtiGAyNegUFCDwJZXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این بین، جمهوری اسلامی هم بیکار ننشسته، یک هواپیمای ایلیوشین روسی تجهیزات را دیشب به تهران آورده و اکنون در حال برگشت است این در حالی است که خبرگزاری‌های عبری امروز صبح گفته بودند که ترامپ در پی یک حمله تمام عیار است
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/16263" target="_blank">📅 14:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16262">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyxJclMEPW2oOTH1Cur9VSgFo0lL39CTyi5Ix-qznCwcuoEzWLUc1AA5x1IXmDjDH308FBDjIndUlfhUBg4xn5aMAl9pWDLaw8WOUFNjaH_h-pzbRW4NTytCm7G8JEaVgcdMKxfVBaNUpisOlgYo_pGzIVCiPnumJS4XomTwWLmyqlQDatX8cirFVz1dUZbGcsaB-kykMlJN3cFsDiEiSNkUSLDHYq7YlKbVld_Lkt1CX9cjXjH3gUb_HmlkKWJzdrlphmdxxMvYuro0PKprUZSzuLTEnrPbmeV7edI-veHqD062F4xFF75FwGidEH-ksYgXA3TJ8k03laGGp0kEng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلا جهانی دوباره پایین زده و اومد زیر ۴۰۰۰ دلار
دلیل اصلیش اینه که پیش‌بینی‌ها از افزایش نرخ بهره آمریکا دوباره بالا رفته
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/16262" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16261">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1ssundTpRGsfxzxTkVUQFLKN7MG7--Lk2Akk6nAUQzhLMNdYUzNGkLVbPzRVhBNhehFaa-TjMZBH4KGKzaPj0baKE7BUTJ9vfbMu0lDYajtxOx1l1SHhAmJLZkyVWAtoGg1RnR_Yn9dO2bIUQKlbzmoj377bvo6jtn6YaQcVuSeXGrkXZtV6e4LkKvyiFh68YJ48w99kfYJGPv0O9tcpilIFIYXVX3bWO4hNfCpUsQiO43el3DUqf4P3ekgMD3Z74-HBoKjj_bFPhIUl5_pElomXA7RkqvQelsUfhqw3wIJPOdb4CJ5pa2U2NJvBh3U5cnN44RK1YEd1B8OtEepdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق داده‌های CryptoQuant، موجودی نهنگ‌های بیت‌کوین بزرگ‌ترین جهش تاریخش رو ثبت کرده و تا الان بیشتر از ۲۷۰ هزار بیت‌کوین (حدود ۱۶ میلیارد دلار) حوالی قیمت ۵۹ هزار دلار خریداری شده
و
در حال جمع کردن بیت‌کوین هستن
این به معنی رشد فوری قیمت نیست، اما ، نشونه مثبتی برای روند میان‌مدت و بلندمدت بازار محسوب میشه
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/16261" target="_blank">📅 13:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16260">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60dd03797.mp4?token=ghxZojYpoKrs-mAI6hXJ937LMgwvKFt_o4RfuubUIlF_Afp17Vv9ceYPdzZyUtC8ub9RRfA6L9lQ_fCIDfZukXhPGiJxqSQiK5ZLMFl-OorUa2keQBGIZTltvB9R93vR9C9TfD0JdkQXeZ0ZzcAhnFrJ2u4uxI2AJpGZNa_EZN1G6xjPHh8KLvH4_WT8xSjcs3rNSQaRZ2o0UsZHIdgAzDuGMwfF5nfzKaDPkOKcQGDl5wMTonsMe9I5Qmb65LncQAZ9weJXdnjV21NI4Pg8B0U1c700vuS4CAR80FgQLB8S5UaingYIlm0Lw_upoH0h1io-5Lu5xQPGS-HAuvf49LLZ1SfPGXF2pvAny2mWqjmrNfb_4CW5tmnCCRzy8RDHJw5HpuFciQVIRpzjI9o9ZN6jm0MkfZp_Ro925zUTWtNSDxeYFku57cR3YbRJLWRmW8URReV13M25To9fK4a4OMmG-of6PsskZh6CS8gKa1_oMl6YaeW9jcF8iXCFtN-5DHDU7-87eDPocM392hLcQI81ZeymouIpUACabNKFSbkOfTEG3HaNTL_03u_DtdeXEGTs0jYuRgcP16X5XRVojxpSZPJtr-Rqoz9GLRDpUgivbkDpbhutgIcqL-dc7QQ5EyVWanAbyr5hiIOUvRQbA6QrlciPEoXC93QTdTqhPrY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60dd03797.mp4?token=ghxZojYpoKrs-mAI6hXJ937LMgwvKFt_o4RfuubUIlF_Afp17Vv9ceYPdzZyUtC8ub9RRfA6L9lQ_fCIDfZukXhPGiJxqSQiK5ZLMFl-OorUa2keQBGIZTltvB9R93vR9C9TfD0JdkQXeZ0ZzcAhnFrJ2u4uxI2AJpGZNa_EZN1G6xjPHh8KLvH4_WT8xSjcs3rNSQaRZ2o0UsZHIdgAzDuGMwfF5nfzKaDPkOKcQGDl5wMTonsMe9I5Qmb65LncQAZ9weJXdnjV21NI4Pg8B0U1c700vuS4CAR80FgQLB8S5UaingYIlm0Lw_upoH0h1io-5Lu5xQPGS-HAuvf49LLZ1SfPGXF2pvAny2mWqjmrNfb_4CW5tmnCCRzy8RDHJw5HpuFciQVIRpzjI9o9ZN6jm0MkfZp_Ro925zUTWtNSDxeYFku57cR3YbRJLWRmW8URReV13M25To9fK4a4OMmG-of6PsskZh6CS8gKa1_oMl6YaeW9jcF8iXCFtN-5DHDU7-87eDPocM392hLcQI81ZeymouIpUACabNKFSbkOfTEG3HaNTL_03u_DtdeXEGTs0jYuRgcP16X5XRVojxpSZPJtr-Rqoz9GLRDpUgivbkDpbhutgIcqL-dc7QQ5EyVWanAbyr5hiIOUvRQbA6QrlciPEoXC93QTdTqhPrY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکورت و جابجایی دیدنی بی بی نتانیاهو
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/16260" target="_blank">📅 13:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16259">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXlVc7mAXq3x8_HuNNaJaCMlOv9_ebPHozG43ZagfZlG_wYZse2hVMJ366_qjCdQlFgeFK6YUj49ttU9K1YBzRIUQOu4gUrJL4OvOYoHYi3SxRlckR3iSPKe3c1gQw0UObqsZyZLvuBpONUiMedzgnogTyfyX01i36K05uo6Ltg1Cu9lpZtrmDnwjuDKdLtvZUKlMfOfujMDzGmp8zYxnPff2HyV9dLK7UL_wvVpAaQvzlkjrytW3icbqU5YMtJL2F4Z-cJsM9T80-NO9DizVGK--I7_lMe4qT4nPjRuK2FhuqzXVX60RZMJpjOsyKO6lbJE_R7ATUEbuDivFCDPWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت خدمات دریایی انگلیس:
یک حادثه دریایی در ۷۶ مایل دریایی جنوب بلحاف در یمن رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/16259" target="_blank">📅 12:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16258">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رویترز: مذاکرات فنی غیر مستقیم ایران و آمریکا، در دوحه با حضور مذاکره‌کنندگان ارشد و تیم‌های تخصصی در حال برگزاری است
ویتکاف و کوشنر، چارچوب و مبانی این مذاکرات را پایه‌گذاری کردند
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/16258" target="_blank">📅 12:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16257">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کانال ۱۴ اسرائیل : رئیس جمهور ترامپ برنامه‌های عملیات نظامی گسترده علیه ایران را متوقف کرده است تا مذاکرات دیپلماتیک با هدف محدود کردن برنامه هسته‌ای این کشور را در اولویت قرار دهد در‌ عوض از حملات تلافی‌جویانه هدفمند برای حفظ اهرم فشار استفاده می‌کند تا از بی‌ثباتی منطقه‌ای جلوگیری کند.
@withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/16257" target="_blank">📅 12:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16256">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فارس : استان هرمزگان بیشترین آسیب را از آلودگی نفتی ناشی از حمله آمریکا متحمل شده است. این آلودگی بخش‌هایی از سواحل بندرعباس، قشم، جاسک، سیریک، بندرلنگه، لاوان، بوموسی و تنب‌بزرگ را در بر گرفته و تاکنون بیش از ۲۵۰ کیلومتر از خط ساحلی این استان تحت تأثیر قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/16256" target="_blank">📅 12:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16255">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">1$ Tether = 175,000 Toman
📈
@withyashar</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/16255" target="_blank">📅 11:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16254">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKdbjY-twmEcreKIL5-PxEZ1qpuMB1ODbnMzVHjeXGU88eiUPUxMqM_yn7MJgUjF0oefg_G-m2UrVuhHTgEm1mI_epsfhtUicOaIyAnAy4ZTtaHpiUm6rVmdDfQsmdGW6q26b2OYIPD-8yzGOS08tUB89LqcvJkai6lUyOHpuXvwwLarZ-2c-ziQLUraYao5YNZnrMnRcI-qmFQed8V9NTLCFkX3GKbGGL3q519IcJiXUhzTU66mV4bK-11Mq1C4tBLQhSKn1M7cx8kPc8pAFabL34NgobkwTo5CxVJKlpCztcqJGyVXnasLIK20Y1sctw5d8iYBIbd7bd4wr46lYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون شیراز نابودسازی از پیش اعلام شده مهمات عمل نکرده.
@withyashar</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/16254" target="_blank">📅 11:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16253">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ygnr0snqT611pPVkvDGWxfLFM9t7zdPprMB2K8ztwXpKK7huPm1LKrwmwPKoFSIm7XTseobV9zK2tQLaDabCVs9_4UbFNVwf3c-uCMoiZxEfqs8-bRdWdO2eR6nM580OqwjfnMYwZOBTituxHSwur4Yq8kAl4YHbzITnztMUFpb2RnIaEO-w9kpjj4bixa-liWxA3YGpkwwaiVRZczhemKJAC0jjKqIIZ37ueeYH9tQx_RSjRfKKmnM8xP3c8Dr_HSst036tZQNPToKgSKJpwcxxw-DFM8a2ztapjLlIYIW56wORcuHsdOQkw21ldK9ecQG4g3swYkFxkHjiBdQy6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند کشتی باری که از مسیری غیر از مسیر تعیین شده ایران در تنگه هرمز، تردد می‌کرد به علت خطای ناوبری و آبخور، به گل نشست
@withyashar</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/16253" target="_blank">📅 11:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16252">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرگزاری های رژیم :
خبر تدفین رهبر انقلاب در نزدیکی ضریح امام رضا علیه السلام کذب است
به تازگی، برخی صفحات در فضای مجازی ادعا کرده‌اند که پیکر مطهر رهبر شهید انقلاب در روضه رضوان و در جوار ضریح ملکوتی امام رضا(ع) به خاک سپرده خواهد شد. این شایعه در پی آن مطرح شده که بخشی از روضه رضوان به دلیل مرمت سنگ‌فرش‌ها، داربست‌ کشی و با پارچه پوشیده شده است.
لازم به تأکید است که نظر و تأکید رهبر معظم انقلاب بر این بوده که مکان خاکسپاری پیکر رهبر شهید، به‌گونه‌ای انتخاب شود که خللی در زیارت حضرت ثامن‌ الحجج(ع) ایجاد نگردد؛ ازاین‌رو، پیکر مطهر ایشان در نزدیکی ضریح مطهر دفن نخواهد شد.
@withyashar
یاشار : امام رضا هم جواب کرد
😂</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/16252" target="_blank">📅 11:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16251">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سخنگوی ارتش فرانسه: ناو هواپیمابر «شارل دوگل» در خلیج عدن مستقر شد
@withyashar</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/16251" target="_blank">📅 11:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16250">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شرکت‌کنندگان مراسم تشییع از ساعت ۶ صبح روز ۱۲ تیر تا یک ساعت پس از تدفین، بیمه شدند
@withyashar
سه‌شنبه ۱۶ تیر نیز تهران تعطیل شد</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/16250" target="_blank">📅 10:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16249">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بی‌بی‌سی: ترامپ در سال گذشته بیش از یک میلیارد دلار از فعالیت‌های تجاری، به‌ویژه در حوزه رمزارزها، درآمد کسب کرده است
@withyashar</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/16249" target="_blank">📅 10:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16248">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وال‌استریت ژورنال: عربستان ابتدا دسترسی نظامی آمریکا به پایگاه‌ها و حریم هوایی خود را برای عملیات امنیت تنگه هرمز محدود کرد که با تهدید واشنگتن به تعلیق تحویل سامانه‌های دفاع هوایی همراه شد.
هرچند ریاض بعداً موضع خود را تعدیل کرد، اما این اختلافات و تنش‌های دیپلماتیک اخیر باعث شده آمریکا به کاهش حضور نظامی خود در عربستان فکر کند.
@withyashar</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/16248" target="_blank">📅 09:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16247">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وال استریت ژورنال به نقل از مقامات آمریکایی:
ترامپ در حال بحث درباره احتمال تجدید حملات نظامی گسترده به ایران با وزیر جنگ و رئیس ستاد مشترک ارتش است ، اما تصمیم گرفته است که مذاکرات دیپلماتیک را در حال حاضر ادامه دهد.
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/16247" target="_blank">📅 09:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16246">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f21403e97.mp4?token=XiAcSR6KF8Gwfv7VSaS39A8qnIWGwWyTKUXLzuZp8qMtwtYWOac5OZwq00Q4fb8jEv1Nd_fHwMzOWI_Lc3HtyCLhYL7-ThVaGdzXjJusGVcxMm1CzLKXyt_KhSiM4PkA2xRbgxzDw93Dk9Q0753gf47-aWyeGG3_hng3VDDXKTFx1YzQphnPuvBH_ZnxsHhoU4BrtFo4fNtDwqyXRs4_lBoUIcGUPqluPTd8HtfE3cKfLO4NzaAm_HI4cwqjqe0AMNTFgXAejU9eBA6XySclI4ftzynfgOg9rkXn4J00SLYw5-GJ_DzjIPFJN1Yuw3s-nz__zzfCtEslavq3lsa-HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f21403e97.mp4?token=XiAcSR6KF8Gwfv7VSaS39A8qnIWGwWyTKUXLzuZp8qMtwtYWOac5OZwq00Q4fb8jEv1Nd_fHwMzOWI_Lc3HtyCLhYL7-ThVaGdzXjJusGVcxMm1CzLKXyt_KhSiM4PkA2xRbgxzDw93Dk9Q0753gf47-aWyeGG3_hng3VDDXKTFx1YzQphnPuvBH_ZnxsHhoU4BrtFo4fNtDwqyXRs4_lBoUIcGUPqluPTd8HtfE3cKfLO4NzaAm_HI4cwqjqe0AMNTFgXAejU9eBA6XySclI4ftzynfgOg9rkXn4J00SLYw5-GJ_DzjIPFJN1Yuw3s-nz__zzfCtEslavq3lsa-HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها) , سپاه پاسداران که بیضه های این ارتش هم نمیشه
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16246" target="_blank">📅 02:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16245">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رویترز : مقام‌های فرانسوی تجمع بزرگ شورای ملی مقاومت ایران (مستقر در پاریس) را پس از آن ممنوع کردند که نهادهای امنیتی نسبت به افزایش تهدید از سوی فعالان سلطنت‌طلب رقیب هشدار دادند.
پلیس پاریس این تجمع را که قرار بود در ۲۰ ژوئن برگزار شود، تنها چند ساعت پیش از آغاز لغو کرد و دلیل آن را فضای به‌شدت متشنج داخلی و بین‌المللی و خطر بروز خشونت اعلام کرد.
تجمع‌های پیشین شورای ملی مقاومت ایران، که توسط بازوی سیاسی سازمان مجاهدین خلق ایران سازماندهی می‌شود و شرکت‌کنندگانی از سراسر اروپا و جهان را جذب می‌کند، معمولاً بدون حادثه برگزار شده است.
@withyashar</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/16245" target="_blank">📅 02:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16244">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rorgReJ_hL7WuprehxRwQNO9EWiBfXe-FGiimMl8YQTUjt8mqjFLTQtSMKC78sY6zcct8T-_8luzf7amIw0GgsrzeqrHp6QdJKU3bHu7HSoBAfbc8mxbqWPGQqBNTLH2qDSaEmGP_Ocu30QWHWzUV6Ge6fuZbpcWU-uuaZL98LCedlooQx8A6Tsb8VWmWSlrS0z7J7lpbQNbzwrS5NqpSbHPuskN1yTP22mnGVCRezQCk6-7o6L8N_7z4ExOfzN06zxBrfjWIlc7vKNK2BsS4SEE8aayLRs3dVwCr74KsK78mH4ZYCVl16IpsI2JQu-QotkgbwRz6vpY_lvs3rALvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون پنج فروند بوئینگ 777-268ER سابق سعودی به ماهان ایر، بزرگترین شرکت هواپیمایی ایران، تحویل شده. کاربر نهایی این هواپیماها، یک شرکت هواپیمایی مستقر در اصفهان متعلق به یک میلیاردر ایرانی است.
از پنج فروند، دو فروند در حال حاضر در فرودگاه بین‌المللی مهرآباد تهران هستند.
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/16244" target="_blank">📅 01:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16243">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نتانیاهو:
حزب‌الله چیزی شبیه به «پنتاگون» را در زیر زمین احداث کرده است
@withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/16243" target="_blank">📅 01:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16242">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAYhDp8S_pkxMvOocTPjUUQwSlsWGrIrOrulyjnlYDLir9uAOmR90Eq_mS4vpRjeH-Zb7zjD5-Ev0LB5ZKgs9ZQCexEKCusv0YkcvncYDTB_qie8SKaKhHZX88Ap3yuhAo7vRHrBElcDAozQifkjVVT_OMQi63JIZ4Mqtd1hpwpnCoEyWfKBQ0UN7dVkVqmV2z-RIOa352fT22HWez67XtriLnrksh6a82_bAI4JjMW54UrrEb5LxSkwrcnDbyekHu859hzfR1RVdixu0wMvtrjBXigkeEPDVRhSOFEaeGx04QymhHxc0kPK0yHEsER22bQCRYsMR0p-0AElQw7mww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : ناو آبی خاکی باکسر داره میاد ! ۴ ناو ۱ آرایش رو به جلو و آماده به سمت خاورمیانه  یو اس اس باکسر، یو اس اس پورتلند، یو اس اس جان ال. کنلی و یو اس ان اس پیلیلائو در آرایش جنگی در اقیانوس هند حرکت می‌کنند و تحرک و پایداری آبی-خاکی را در دریا…</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/16242" target="_blank">📅 01:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16241">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رسانه رسمی قالیباف بعد از اینکه صداوسیما مصاحبه‌ رو قطع کرد، اعلام کرد بخشیهایی که پخش نشد درباره این موضوعات بوده؛
پاسخ به ادعای بازرسی آژانس از سایت‌های ایران.
جزئیات پیگیری آزاد شدن پول‌های بلوکه‌شده ایران.
توضیح درباره اعتبار 300 میلیارد دلاری برای بازسازی که تو متن تفاهم اومده.
پاسخ به ادعاها و حرف‌های ترامپ.
توضیح درباره پیام راهبردی رهبر جمهوری اسلامی تو 28 خرداد.
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/16241" target="_blank">📅 01:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16239">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRfpTldG0SflBrixdwU-flz3F7VX4G1nuSWoo1SRyBKsWtToXwwCfq1MkB5jYarxDK2k7YErdHwoho0CeN5tGTOB8ylSl335_kN_9F3PzgT7CrQkjyNnisqUhCXrCtR9q1LNlWx4CM55Fnkg0vo_orJCxUrVcMkTVEGuDGW335ai5pB6_Zw6EX8oOsq8rgM8G6PH0J2RYxB5xFXMaTrQ3dicdhzPjiU6z8o7Z5-aid3UNKPbdnOAyuVwcAd-HvtYGkNAvXl1dnWerc9yVDXFHbHIjnOZk5WEgt_vY1yRpml3j9au_YvsvSbdMC1o47S6RUYGh2AcENlt-1kYyEURlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9663206797.mp4?token=eCOvsERV4W8i-3poNWdEkv54aEJ1Jr56mEF49Dw-fqwV0ikUoKVxw1S3Gc0SfG5Hz1VkKJ6yhqg6sQNwtOccp9Tub4fBHUWCbW9BT6oFCfhJra3CwXGme13arAXHlDVQOX3_ONDKmOKxptytI2E975VLwzuyGjHcb0K5aZrZ03WZdixaa5t1AoLWrcaKqr0GYgNn9E7MjEXssHyeKH1UrTrWozsBQQXjrqK4vKhahBSiagkju3adWQ4sbAZn4meKjJJRgd6GkILse8XRkPHAXTeLrYiRi_Aj2YywRFSc9uH_VmSYcI9WYNpMCuLBu_8u47dNlcAWLDDvtB3P5FKVyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9663206797.mp4?token=eCOvsERV4W8i-3poNWdEkv54aEJ1Jr56mEF49Dw-fqwV0ikUoKVxw1S3Gc0SfG5Hz1VkKJ6yhqg6sQNwtOccp9Tub4fBHUWCbW9BT6oFCfhJra3CwXGme13arAXHlDVQOX3_ONDKmOKxptytI2E975VLwzuyGjHcb0K5aZrZ03WZdixaa5t1AoLWrcaKqr0GYgNn9E7MjEXssHyeKH1UrTrWozsBQQXjrqK4vKhahBSiagkju3adWQ4sbAZn4meKjJJRgd6GkILse8XRkPHAXTeLrYiRi_Aj2YywRFSc9uH_VmSYcI9WYNpMCuLBu_8u47dNlcAWLDDvtB3P5FKVyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای افغان به مناطقی در بلوچستان پاکستان حمله کردند و درگیری‌های مرزی آغاز شد.
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/16239" target="_blank">📅 01:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16238">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdFpGElIXPRzdmNthEqGxsIS8rwse5m8MWzpd_5m6O8Kn_dJL1Ju05Gz3fQ-yDBMJoOZ2w-vuZo9lV8hHqgA-SkoXsoe1b8gJzyVC3lCSni0gnx3Gq5uu9sEHfY_279mNruBhKkmzzvNPLTINjSXnTtf4DkXLQEMxFX9FhpN-p2JUxH7iUMMbKzdsNMDJJP5egPUDIStBbfeziPZezwmn6qJktBzPRnijrAcEKddVdZLnSSYJ_PPWDVSHofhXBG_WahufyeeBZ28zq8P9IxI5YnfgGQilyhyXuqqFuj3rLlkuWYjsQkMH0zYr1BSESDLwpVfUNK0hsDTf1fbD1dEAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاروان‌های کامیونی پر از تابوت جدید از تروریست‌های حزب‌الله که توسط اسرائیل نابود شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/16238" target="_blank">📅 00:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16237">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وال استریت ژورنال: سپاه پاسداران این پیام را به واسطه‌های قطری منتقل کرد که اگر تضمینی مبنی بر کنترل انحصاری تنگه هرمز توسط ایران دریافت نکنند و اگر ایالات متحده و کشورهای غربی از برنامه‌های خود برای دریانوردی از مسیر جنوبی در این تنگه در نزدیکی سواحل عمان دست نکشند، دوباره تنگه هرمز را خواهند بست.
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/16237" target="_blank">📅 00:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16236">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2g09r2fKVYXn04mqAdoijacDhqu15H9AAmxFqSeXsRBmirA-kAokEa4cykMpssEAv5RqjOkwFMPKFxa9Tz5mg8-EvwUGG0GeNsg6VxotzHX8pZ3-LE1gpy4dsSAWMubYBz_Gw5MQiJJvq3B1uy3ObohAmj2t7-Kg4_cXQqBKUwDk2YV6Tio3arzJSi2woNrAm94LEtj74mPCbpC_URfKHoNvFpIbo4IDy1X9npLLIqF2Ljt0VtRlMxLb3ngaAYCJj6WLGraFRuBq0-g0rRom4wNWKx-GjSU4zrJL1_wuojvW7oZr04tFfBkdYl_zgwzUz62-Rj1cSIiDep4G5buOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین لرزه ای به بزرگی ۶.۲ ریشتر خلیج کالیفرنیا در سواحل مکزیک را لرزاند.
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/16236" target="_blank">📅 00:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16235">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">جی‌دی ونس: ایرانی ها یه تاکتیک عجیب برای مذاکره دارن. توی رسانه ها میگن مذاکره نمیکنیم ولی وقتی به ما زنگ میزنن برای مذاکره خواهش میکنن. خب این یعنی چی؟!
ترامپ مایل است بمب‌ها را رها کند، اما فقط اگر هدفی را پیش ببرد.
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/16235" target="_blank">📅 00:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16234">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اتاق جنگ با یاشار : چک افسری ! این ویدیو نکات ریز مهمی داره حتما دقت کنید! https://www.instagram.com/reel/DaOSvJUxDdL/?igsh=aGRkbWQyN2ozeTNs  کلیک کنید و کار های اداریشو انجام بدید</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/16234" target="_blank">📅 00:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16233">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کاور پست ، چقدر اینو خوشم اومد
😁
💥
@withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/16233" target="_blank">📅 00:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16232">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اینترنشنال: مجتبی خامنه‌ای میخواد اژه‌ای رو بعد از پایان دوره پنج ساله از ریاست قوه‌قضاییه کنار بذاره.
@withyashar
( البته تجربه ثابت کرده هر چیزی که ترامپ و اینترنشنال بگن، جمهوری اسلامی لج میکنه و بدتر انجام نمیده.)</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/16232" target="_blank">📅 23:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16231">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjusWThJWonl2PIavj_eZnwDayNORXudf5mozZ185Lb3PCTtLcfOHpoBSAnCSTZfJiDR5p1jMgyraT6fE9EaZZA7-g2sxdu5YbOqudhz-OLzFlRZb0ffBpx5w6IjbwACDXq85hO3KS9U1ZlYBbNN8YIuAYsfTKInhXbJpzYT1jECdF6T2545Q2rLKM1Eo2smlaoAcoCrbY4thWskiv1JXBLVIdq1bzyLB5nKnvC3PuEIHxLgYbv9udTmkia0veGTTlwU_i3Orjn631flKKJj-LL92CimPX3xANqbuXtn4KRw9vg98HGmW0Npv5-oFs59ntYwj5NoelofWas7cXQwKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور پست ، چقدر اینو خوشم اومد
😁
💥
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/16231" target="_blank">📅 23:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16230">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ec7f9b40f.mp4?token=Gcpvgz9D17FuBF07c6xRNeNal1imsnjvOvy7T5B6Nutzgne40szmRkBopWgKyEt4PseBDOHZP3z_nK97aWQQCIzKntdmFz1ASOuB2euiuAM539OFhLwh2Wi3VbZarLWEHwCEYIux1iOXqls4UEok0_3O_a6KM5y2v3NrV11U-AlH_8SpbTwgiX87wbb-Ws0tK3r_YgF3Ve1ex9zK57SiluSmCKzv7uCS56QoN7e8FByPlcyoKq93MfFGNjRFMQ1ngV0zov0okkmldDv29iVZPtVXotl8gKVjgAMmgHHVRLM6YbCPzE8Zlqdf5JqwMOsx_dWSYfiwXatctr7BJC9fmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ec7f9b40f.mp4?token=Gcpvgz9D17FuBF07c6xRNeNal1imsnjvOvy7T5B6Nutzgne40szmRkBopWgKyEt4PseBDOHZP3z_nK97aWQQCIzKntdmFz1ASOuB2euiuAM539OFhLwh2Wi3VbZarLWEHwCEYIux1iOXqls4UEok0_3O_a6KM5y2v3NrV11U-AlH_8SpbTwgiX87wbb-Ws0tK3r_YgF3Ve1ex9zK57SiluSmCKzv7uCS56QoN7e8FByPlcyoKq93MfFGNjRFMQ1ngV0zov0okkmldDv29iVZPtVXotl8gKVjgAMmgHHVRLM6YbCPzE8Zlqdf5JqwMOsx_dWSYfiwXatctr7BJC9fmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : اگه لازم باشه، برای بار سوم به ایران حمله میکنیم
@withyashar</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/16230" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
