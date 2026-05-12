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
<img src="https://cdn4.telesco.pe/file/ixB6tXTcshTlCqs4McarC_Rmhfddiydd0Q1juglucSNN_ydlp1lvI9kLiFTk4vcojOAuWMJETlaJhqCGB7hdeqFKybqyCIjGW43mBUrLqTndHWY_Gx3f-mMcAL1t6ldvJkd1gZAHvndG1qy5020J5vLXYmsH20B3tUGhsHhgUxEU3wc5w1KjDfXZu_ShhDuZMRmzXtqBODPGhqhE8d41r2D9Kw-Hv47I7xzue347dBqFt4HG_G5hPmIE5GNZIwAXMHCctSyhXUVflglbLcFkTOqwYaWGw_g21PVXrdASQnAeAj69g6BwvNGbk6KpT8Jwuw4st_DDsD24aQkR5KoMvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.9M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 21:28:40</div>
<hr>

<div class="tg-post" id="msg-651993">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ترامپ: از کسی در جنگ با ایران کمک نمی‌خواهم
🔹
هرگز توافقی را با ایران نخواهیم داشت مگر آنکه توافق خوبی باشد.
🔹
مذاکره طولانی با رئیس‌جمهور چین درباره جنگ علیه ایران خواهم داشت.
🔹
هیچ کمکی از کسی درباره ایران نمی‌خواهم و ما پیروز می‌شویم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 328 · <a href="https://t.me/akhbarefori/651993" target="_blank">📅 21:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651992">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تفویض اختیار به استانداران استان‌های مرزی جهت واردات اقلام اساسی
هادی تیزهوش تابان، رییس اتاق بازرگانی مشترک ایران و روسیه در
#گفتگو
با خبرفوری:
🔹
با توجه به تحولات اخیر، تغییر رویکرد از بنادر جنوبی به سمت بنادر شمالی و دیگر مناطق مرزی اجتناب‌ناپذیر شده است. به همین منظور اختیار واردات برخی اقلام اساسی به استانداران استان‌های مرزی واگذار شده است.
🔹
پیش‌بینی می‌شود واردات کالاهایی مانند غلات، روغن، حبوبات، دام زنده، کود، نهاده‌های تولید در حوزه فولاد و پتروشیمی و حتی دارو از مسیر کریدورهای تجاری شمال کشور، به‌ویژه کریدور شمال–جنوب، افزایش یابد. همچنین با توجه به ظرفیت کشورهای چین و روسیه، امکان تأمین این اقلام از طریق بنادر شمالی فراهم است.
@TV_Fori</div>
<div class="tg-footer">👁️ 662 · <a href="https://t.me/akhbarefori/651992" target="_blank">📅 21:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651991">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cROZm5KGidT0UjitskaOvOC-Ue_AHqdFLQrj-eMO2-jPFVqMHeaYpKpDXp8kiLgEPFFj3uejOYdU4VxgHpiYdVeGZcmggeIqOXBOD_fv3NkT9qX4Y9eqNCUyxtZe5Na-HyctQjHNp9H5wSgGl-aBOGYRKkuLy3wsmEs7UUxNT3dIXjr2vCjLGqkodCnqbt2zOm4w5vNQOFsavZl1jEsVS83o5zrzodzNBZLWiYoTW68B0rma85Ph8fiBNuN-5NwEoSCZHlIf20PidKcPKlVQAjyHIZqX6MyHbpn6pBzOkISVs0TiGSf1tehU0SgiozdQJ3XOHznXr_8kWOioiZmrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای بلومبرگ: امارات با هماهنگی اسرائیل دوبار به ایران حمله کرده است
🔹
بلومبرگ شامگاه سه‌شنبه گزارش داد که امارات دوبار با هماهنگی رژیم اسرائیل به ایران حمله کرده که یکی از این حملات پیش از آتش‌بس و دیگری پس از آتش‌بس روی داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 802 · <a href="https://t.me/akhbarefori/651991" target="_blank">📅 21:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651990">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ژنرال دن کین، رئیس ستاد مشترک ارتش آمریکا و پیت هگست، وزیر دفاع آمریکا، هر دو از اظهارنظر درباره گزارش‌هایی که ادعا می‌کنند تنها ۳۰ درصد از توان موشکی ایران نابود شده است، خودداری کردند
🔹
هگست گفت: من اطلاعات درز یافته‌ای را که ممکن است درست یا نادرست باشد، تایید نمی‌کنم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/akhbarefori/651990" target="_blank">📅 21:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651989">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQlH-5E3JPw7feUvVzOvFfeDJSPIlULiHSXl6AB43C0VSm7tVyeNfzwcwZw0WdgWgPXNbBjh72XtuNZpG_najdy3-plFiq3yRI2HRRiSfMbcz35deNXpkOAUXA2CrnlYzL3ofoV4_uIj6P-IkItq6ljNg23u6v4kpBXOUb6TlQst0OsmL_DmniUcvBBtghd1jOXpzwaiJIB6wV90jO3eSsvWb5J28D8Jp6088HpiyVhPT9uax2qZUX42kCGknTfQFC7PB_4pmDlNwPhkwHywdVRHj3stF3pxt6Ujjdfkv505nlE7NAEsqDE2BUvyK2-ZEklv59_KxXpgsMHv9DD7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طرح جدید مجلس: میانگین پرداختی کل دوره شغلی مبنای حقوق بازنشستگی می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/akhbarefori/651989" target="_blank">📅 21:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651988">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
لارنس ویگر سون، افسر بازنشسته ارتش آمریکا: در حال ورود به مرحله‌ای از این درگیری هستیم که دیگر راهی برای خروج‌از آن بدون تحمل تلفات انبوه وجود ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/akhbarefori/651988" target="_blank">📅 21:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651987">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O64A1YNkAIT2spwUHIUgyvQl4_S9vnzcxP4u7dapl4qiO7cIbWlH4vp8ZplMUInF_6rGi44MPejhTYh17IrJ4GB2a_RPgaCDydOaVQoTGXyu1emmxcAnqIGuuUH-nFFeezzEs-tI2gbQAZEXzUaD6dx1fDOU6ar8kqpotCJ4y3KFOYOSPfzv2QZ13SK846iyS1P50EyCwxUHojJZ4f5RgNoA2FqSb4lekyyVSB9at9vBbwzoPnGm4487N37GGi5zHnxkk66yzXtta6AttV0HYo7T0JPLf2pS9z7dalN-FhCHQ5CbM5dPm3fj7tOwHyc3xZd6KdSV1UtkATOZwwSJ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی: تاکید ایران بر اصولی روشن است: «توقف دائمی جنگ و عدم تکرار آن»، «جبران خسارات»، «رفع محاصره»، «رفع تحریم‌های غیرقانونی» و «احترام به حقوق ایران»
🔹
معاون وزیر امور خارجه: نمی‌توان هم‌زمان از آتش‌بس سخن گفت و محاصره را ادامه داد؛ از دیپلماسی گفت و تحریم را تشدید کرد؛ از ثبات منطقه‌ای حرف زد و به رژیمی که منشأ تجاوز و بی‌ثباتی است، پشتیبانی سیاسی و نظامی ارائه کرد. چنین رویکردی، مذاکره نیست؛ ادامه سیاست اجبار با واژگان دیپلماتیک است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/akhbarefori/651987" target="_blank">📅 21:02 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651986">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225fbab644.mp4?token=M0iOg7TzXr5Kbi91eLLDGxyyaD-CULLiV7pwr6NC3ZrkLVGMxVSKnilN2ayq6vobNTAU2Otjs2NOXIMjWZTDVaVai6v6lsh4M_dIm22mpQyhHgRy6ad10gMAZhZeA4x0YhfOlA4GYplLrgESJPcof60nOVn6cBRwDWBYRSZNMXAv6yue4WaCZrrBaYow2CXiS4ypm2S0yHsUXKyy10LJWxTmNi_SfgfE5aa6u779G_Kfm56TfDNwz-U7gtu1XrEYW0MWpg8oVbKQHU-S83g4KZF4LYkJzzy_Q6iJ-hNKtF2Zlcanxyztu9GLmKSRnDCap8N1HKTjXWQtOr20zNhvZx32hT17gJ2cQuB5wpfHmOAffAIHUlZV672AQhsSxZbzyRGo-mv2UvvhKHlTjSgjHxiMOFa__VaT9EApGld8byL88uy8hFtHxR8tcXTThUzSqPyxhVbT0HH6C8_1wAyA21fTVbsxRpF0Qx6jtUp4OsW_LdtB1jpPR8hywd3T-2f8sPyJSwONWiBPBVgcfKlgpyxe4A82ljqL5C2ofDnAbK7ENcsPzJ1dCvbW29gd0SzfT0aZBWWIFJC11eYd-RRFM7vtttRRwrWU2htETjzuvFbzFG86-m3guELDuG_v7KM6S6GaWMm0-SJxpq_iuxltCy5p-TqCYmj0eH70Sf0a-7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225fbab644.mp4?token=M0iOg7TzXr5Kbi91eLLDGxyyaD-CULLiV7pwr6NC3ZrkLVGMxVSKnilN2ayq6vobNTAU2Otjs2NOXIMjWZTDVaVai6v6lsh4M_dIm22mpQyhHgRy6ad10gMAZhZeA4x0YhfOlA4GYplLrgESJPcof60nOVn6cBRwDWBYRSZNMXAv6yue4WaCZrrBaYow2CXiS4ypm2S0yHsUXKyy10LJWxTmNi_SfgfE5aa6u779G_Kfm56TfDNwz-U7gtu1XrEYW0MWpg8oVbKQHU-S83g4KZF4LYkJzzy_Q6iJ-hNKtF2Zlcanxyztu9GLmKSRnDCap8N1HKTjXWQtOr20zNhvZx32hT17gJ2cQuB5wpfHmOAffAIHUlZV672AQhsSxZbzyRGo-mv2UvvhKHlTjSgjHxiMOFa__VaT9EApGld8byL88uy8hFtHxR8tcXTThUzSqPyxhVbT0HH6C8_1wAyA21fTVbsxRpF0Qx6jtUp4OsW_LdtB1jpPR8hywd3T-2f8sPyJSwONWiBPBVgcfKlgpyxe4A82ljqL5C2ofDnAbK7ENcsPzJ1dCvbW29gd0SzfT0aZBWWIFJC11eYd-RRFM7vtttRRwrWU2htETjzuvFbzFG86-m3guELDuG_v7KM6S6GaWMm0-SJxpq_iuxltCy5p-TqCYmj0eH70Sf0a-7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تهدید جالب شهید حاج محمد نظری به سربازان آمریکایی!
🔹
خاطره یکی از نیروهای نظامی از دستگیری نیروی دریایی متجاوز آمریکایی در خلیج فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/651986" target="_blank">📅 20:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651985">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
انگلیس از حضور خود در تنگه هرمز خبر داد
🔹
دولت بریتانیا اعلام کرد که با پهپاد جنگنده و ناو برای تامین امنیت تنگه هرمز مشارکت خواهد کرد.
🔹
لندن خاطر نشان کرد با تجهیزات خودکار برای شناسایی مین و جنگنده های تایفون و ناو جنگی در تنگه هرمز حضور خواهد یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/akhbarefori/651985" target="_blank">📅 20:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651984">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jevQdKXm2i8SHETHh-kc4KUGIZbLb-joJtLivNfmwdqQUONDX938RsY8UgznXr23DcZnYefkPWnjEa67C2_Bq-wR2fMfjOHmUrnbOv1-R8Jcm0derhXYbymJQwssybKWfdq-Rs-USFBJxKELW_Diib_86VO-UQKjtuYbx1Hfiaey2_K-QU9MCwn69yEarzE_SOUrgIkJs7VXLAaizWwFIVKR5d37moTYfCXVxoko7TwlKS1aD04jpjqzVOMaprQCz7GdRl4RNU4TLEyF6WxVmSI9JQv0iGmpN3r8Gtka7XYtNGktnZ6gRRGq5OdcAHGgYEsE9hB6bbA_qzRFvCC-CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمک نظامی اسرائیل به امارات در جنگ ایرات علنی شد
سایت رادیو ملی آمریکا:
🔹
اسرائیل در جریان جنگ ایران، برای کمک به دفاع از امارات، سامانه‌های ضدموشکی گنبد آهنین و نیروهای عملیاتی به این کشور اعزام کرده است.
🔹
هاکبی با اشاره به روابط دفاعی رو‌به‌ گسترش اسرائیل و امارات: «اسرائیل باتری‌های گنبد آهنین و پرسنلی برای راه‌اندازی آن‌ها به امارات فرستاده است.»
🔹
همچنین از امارات به‌عنوان نخستین عضو پیمان ابراهیم یاد کرد و این همکاری را از نتایج این توافق دانست. / خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/akhbarefori/651984" target="_blank">📅 20:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651982">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d58e4bba9.mp4?token=sJXglPxuiChWf8gZxQGLMmhrkJGoZP7Znj5NuKFUI1GddcixNUj56uN3waDpZ7dP3xOXK4OnPoYUSzdTJoy8YAIoX1Wpne8sQNgWvJn9t2dgI3Fsjp75erIfpgZnYTf6KcCjBIDIm-siuyqce75ZsmDkRZDqoKLHdxTjaBKRahSgDQzbdo6FodhFWrhbg-a-8xBYWPEu_-6ZSRSmQATk0XjNtJ-tiWH4LRah6JTAprMnUSKOdOnBAC2WZX2TRAlHAuxrnff4Fm_ZIDaBIZP4j4uRZnBY_kfObA6ZDMBjG72VaObXp1GCl106ABLun4VyxaOMKt6PknI3pe1-p_NICQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d58e4bba9.mp4?token=sJXglPxuiChWf8gZxQGLMmhrkJGoZP7Znj5NuKFUI1GddcixNUj56uN3waDpZ7dP3xOXK4OnPoYUSzdTJoy8YAIoX1Wpne8sQNgWvJn9t2dgI3Fsjp75erIfpgZnYTf6KcCjBIDIm-siuyqce75ZsmDkRZDqoKLHdxTjaBKRahSgDQzbdo6FodhFWrhbg-a-8xBYWPEu_-6ZSRSmQATk0XjNtJ-tiWH4LRah6JTAprMnUSKOdOnBAC2WZX2TRAlHAuxrnff4Fm_ZIDaBIZP4j4uRZnBY_kfObA6ZDMBjG72VaObXp1GCl106ABLun4VyxaOMKt6PknI3pe1-p_NICQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریس کونز، سناتور آمریکایی خطاب به وزیر جنگ آمریکا: شما در جنگ با ایران موفقیت‌های «تاکتیکی» دست یافته‌اید اما در آستانهٔ یک شکست «استراتژیک» هستید، چون ما اکنون درحال مذاکره هستیم تا فقط [تنگه باز شود]
🔹
وزیر جنگ آمریکا: این حرف خیلی احمقانه است!
🔹
کریس کونز: شما دارید به من حمله می‌کنید، من دشمن شما نیستم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/akhbarefori/651982" target="_blank">📅 20:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651981">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664ca9f2de.mp4?token=WbV9ff0OWunkuJ5f8Pc7JUQeuTRJs8-u-vzPtdbutOh_oXsPKAgoSbTfSiLL1W6ebq7F1zl_BiuNp8DJqDhxSFLw578ejoyaCR294BEnBrD3J6egbqJylt1BdcQwJJVVY4fE7-BsSDy8CWNBEbUa2bxHO0scg7Ifg3PgJdZBvdguh0Ayf0-T0r46HiTA6Z8g61_4Uuf1EJ3LJE8FvNKmGaMO8h2seqw9N59X-k9LJL2l1oIds7pf8xb_d82KIQdSlIqlGMpqbZkHuzbeafPQT637u7-11_CgX9xrRIAHml5fuy70EkCNnUu0gKUd_Na8wGWb1RhHODiv9iVF7GLJ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664ca9f2de.mp4?token=WbV9ff0OWunkuJ5f8Pc7JUQeuTRJs8-u-vzPtdbutOh_oXsPKAgoSbTfSiLL1W6ebq7F1zl_BiuNp8DJqDhxSFLw578ejoyaCR294BEnBrD3J6egbqJylt1BdcQwJJVVY4fE7-BsSDy8CWNBEbUa2bxHO0scg7Ifg3PgJdZBvdguh0Ayf0-T0r46HiTA6Z8g61_4Uuf1EJ3LJE8FvNKmGaMO8h2seqw9N59X-k9LJL2l1oIds7pf8xb_d82KIQdSlIqlGMpqbZkHuzbeafPQT637u7-11_CgX9xrRIAHml5fuy70EkCNnUu0gKUd_Na8wGWb1RhHODiv9iVF7GLJ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: خطاب به وزیر جنگ آمریکا: شما ادعا کنترل تنگهٔ هرمز را دارید اما مشخص است که تردد کشتی‌ها در دست ما نیست
🔹
کریس کونز: آقای وزیر، شما همین چند لحظه پیش گفتید که «ما کنترل تنگه را در دست داریم». اما کاملاً مشخص است که بازگشایی تنگه هرمز برای تردد تجاری همچنان از دسترس ما خارج است؛ و دلیل عمده‌اش این است که ایران ذخیره قابل‌توجهی از پهپادهای ارزان و مرگبار «شاهد» را حفظ کرده و رقبای ما نیز در حال کمک به آن‌ها برای بازسازی این ذخایر هستند. آقای وزیر، برنامه شما برای بازگشایی تنگه هرمز چیست؟
🔹
وزیر جنگ آمریکا: بخش عمده‌ای از سوال شما بسیار غیرمنصفانه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/akhbarefori/651981" target="_blank">📅 20:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651980">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
شکست «عملیات پروژه آزادی»
🔹
باز هم شکست خوردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/akhbarefori/651980" target="_blank">📅 20:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651979">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESIboz7DVYbUxT45ZKfkd6nyvaGRxt2Wif_2OI5rL-qDzqU4uRmBXEGkPallarUPFqWQKPYQd2mkAM6eKU2pugJGmTgnyWKhrKZ5EVJ-Xh3Fj9bSfD6VFL6zFvkXxN_c6mMmZ6kteejw_jHRCtZ8ct7wpXJaAyEOpWri_Ux_uVQqGUtZnO2XDd7QUjuymTl-6zv_Ren0cRriIbWMRl8PPHG0Y5G6alRBU5k5Jez1CfGzvaWtX1h5cZJAivlYgfIYYPu82ajoHSRWsbXulNCDfxExcs-RTdOXiu-EjD9wbmdQM2liQmt5qjuPuuwFOeL6MnxDaRPUWtRoPRuNcj1Oxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشینگتن پست: جنگ ایران رؤیای کشورهای خلیج [فارس] برای اقتصاد بدون نفت را با تهدید مواجه کرده است
🔹
این درگیری نه تنها درآمد نفتی کشورهای خلیج [فارس] را کاهش داده، بلکه تلاش‌های آنها برای گسترش اقتصاد پسانفتی را نیز تضعیف می‌کند.
🔹
جنگ ایران به آزمونی استرس‌زا برای آینده‌ اقتصادی کشورهای خلیج [فارس] فارس تبدیل شده؛ کشورهایی که برای خود شهرتی به‌عنوان مراکز مالی جهانی و قطب‌های گردشگری و فناوری ساخته بودند.
🔹
این احتمال که ایران بتواند تنگه هرمز را تا هر زمان که بخواهد مسدود نگه دارد، اعتماد سرمایه‌گذاران خارجی را متزلزل کرده و اعتبار کشورهای حاشیه خلیج [فارس] را به‌عنوان پناهگاهی امن برای کسب‌وکار از بین می‌برد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/akhbarefori/651979" target="_blank">📅 20:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651978">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d264a2ad4b.mp4?token=jtTE_yQMukKxT6IEeAx9UtAmxHxSv7eRklIS9JfUJyNL_u0WNvDfPVYeTJSRLWRuisImd2IHkb2zkLCUR_B-Ae0b0yo60PcVX8nttpWnGVuuHyjTILdniChPx3N1QxyM9X_m1ZMnDwLkChQHuE00RayY5J6alOp88OJo-NH5SsDYM4ZfON4oyS2nthoH-H2Am6yI03KskKogZH7hLU4oV6cpX-dBXqlGMubGVV-CPZhWUguaedgdGaXNWL6nnyQL9yIeIlsJA9Gq_22xsU6ShFsnVRwoUYB2hDi8hhgQFqMTkaz0ZodMj1_owCjB9X-TLrPzByCjfVOhddcL_d-20g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d264a2ad4b.mp4?token=jtTE_yQMukKxT6IEeAx9UtAmxHxSv7eRklIS9JfUJyNL_u0WNvDfPVYeTJSRLWRuisImd2IHkb2zkLCUR_B-Ae0b0yo60PcVX8nttpWnGVuuHyjTILdniChPx3N1QxyM9X_m1ZMnDwLkChQHuE00RayY5J6alOp88OJo-NH5SsDYM4ZfON4oyS2nthoH-H2Am6yI03KskKogZH7hLU4oV6cpX-dBXqlGMubGVV-CPZhWUguaedgdGaXNWL6nnyQL9yIeIlsJA9Gq_22xsU6ShFsnVRwoUYB2hDi8hhgQFqMTkaz0ZodMj1_owCjB9X-TLrPzByCjfVOhddcL_d-20g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهید محمد ناظری، بنیانگذار نیروی ویژه‌ دریایی سپاه بود، یک تیپ‌خیلی ویژه و جوان که مخصوص متوقف کردن کشتی‌های متجاوز در خلیج فارس هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/akhbarefori/651978" target="_blank">📅 20:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651977">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58948247ba.mp4?token=fGtZC_mMZhpvJF2SOMR4JCVF3dEvxSL4YUFrdkpCsT9AXZEfFUZkD03jfmFhu8ri_qWvd-uiP_ODrMfSHx_ZNAlx4wIUO0wYyC5QhO7ppSUpmpzDtL4HgbFfnyCAOztKkdfUrIgH7Sc3dxSWQNV6m2OUbEZgh0WWMCbH_4-S-8qNJL1ZZ1C-6Oi_r3TftgsgM7qajbbYB5Npsih3RIcUFClHySp_OehCJ8POK8IXLnGI7bx31u5yrSxLgZiWdPcsytTUAy7WDmZ0XHzqxCyI_KZ9XxyPx09fqDyZhhgKPJv9_mcpXNA0R0u2WZ3ymKrDk4JOn4Yg5WOaPfGQrG0ALw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58948247ba.mp4?token=fGtZC_mMZhpvJF2SOMR4JCVF3dEvxSL4YUFrdkpCsT9AXZEfFUZkD03jfmFhu8ri_qWvd-uiP_ODrMfSHx_ZNAlx4wIUO0wYyC5QhO7ppSUpmpzDtL4HgbFfnyCAOztKkdfUrIgH7Sc3dxSWQNV6m2OUbEZgh0WWMCbH_4-S-8qNJL1ZZ1C-6Oi_r3TftgsgM7qajbbYB5Npsih3RIcUFClHySp_OehCJ8POK8IXLnGI7bx31u5yrSxLgZiWdPcsytTUAy7WDmZ0XHzqxCyI_KZ9XxyPx09fqDyZhhgKPJv9_mcpXNA0R0u2WZ3ymKrDk4JOn4Yg5WOaPfGQrG0ALw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلجی، رئیس شورای اطلاع‌رسانی دولت سیزدهم: شهید امیرعبداللهیان یک‌تنه جریانی برای حمایت از غزه در جهان به وجود آورد که شاید دلیل شهادت ایشان هم همین باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/akhbarefori/651977" target="_blank">📅 20:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651976">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
روایت علی هاشم خبرنگار الجزیره از پنج شرط تیم مذاکره‌کننده ایرانی
🔹
به گفته یک منبع مطلع از روند مذاکرات میان ایران و ایالات متحده، دستورالعمل‌های سطح بالایی که به تیم مذاکره‌کننده ایرانی ابلاغ شده، شامل پنج شرط است که باید پیش از ورود به گفت‌وگو درباره پرونده هسته‌ای رعایت شود:
🔹
۱. پایان جنگ در همه جبهه‌ها
🔹
۲. لغو تمامی تحریم‌ها
🔹
۳. آزادسازی دارایی‌های مسدودشده
🔹
۴. جبران خسارت‌ها و زیان‌های ناشی از جنگ
🔹
۵. به رسمیت شناخته شدن حق حاکمیت ایران بر تنگه هرمز/انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/akhbarefori/651976" target="_blank">📅 20:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651975">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d18d73e58.mp4?token=s8bwT5-0By2C8Y6NMmVNkLfXUJGwPUBgWW6W2eb3AP-1t3-ekeZOMTMzdkB65EpW1_wsoKpNLKqfZotAL35WZMZuZbVfDyMDJ0VcwF7OkCe2vf6myydBGGInp3-3UCvQd3tpLcaKeDK69ygQXG495KrlGrWc_fKMnBf9CiUHLiqZHv1GSXK_-m6lisZfQ0araakfLkYvASIbLMyFofqqGtE2RC4ihQwXteRSgVSWX4R-hyhs4zpvxoLihS_4mZjm2iqs5T584jF6Dmugy2xg8gcFr-JJRueiJIAcZgivAGjl3KPjelcKmMXUKvwX2t5f1bdIBatZeX062VmrT8RdOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d18d73e58.mp4?token=s8bwT5-0By2C8Y6NMmVNkLfXUJGwPUBgWW6W2eb3AP-1t3-ekeZOMTMzdkB65EpW1_wsoKpNLKqfZotAL35WZMZuZbVfDyMDJ0VcwF7OkCe2vf6myydBGGInp3-3UCvQd3tpLcaKeDK69ygQXG495KrlGrWc_fKMnBf9CiUHLiqZHv1GSXK_-m6lisZfQ0araakfLkYvASIbLMyFofqqGtE2RC4ihQwXteRSgVSWX4R-hyhs4zpvxoLihS_4mZjm2iqs5T584jF6Dmugy2xg8gcFr-JJRueiJIAcZgivAGjl3KPjelcKmMXUKvwX2t5f1bdIBatZeX062VmrT8RdOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنتاگون: خسارات وارد شده به پایگاه‌های آمریکایی را برآورد نکرده‌ایم
🔹
پتی موری، سناتور آمریکایی: طبق گزارش‌ها ایران به حداقل ۲۲۸ ساختمان یا تجهیزات در پایگاه‌های نظامی آمریکا ضربه زده است. آیا می‌توانید بگویید هزینۀ خسارات وارد شده چقدر است؟
🔹
وزیر جنگ آمریکا: خب، فکر می‌کنم قبلا به وضوح توضیح داده‌شده که ما چه مواردی را نمی‌توانیم بگوییم.
🔹
پتی موری: هیچ برآورد هزینه‌ای ندارید؟
🔹
نماینده پنتاگون: در ر مورد آرایش نظامی آینده در خاورمیانه، ما هنوز نمی‌دانیم که وضعیت چگونه خواهد بود. در مورد ساخت‌وسازهای نظامی، فعلاً برآورد هزینه‌ای نداریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/akhbarefori/651975" target="_blank">📅 20:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651974">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
تخمین وزارت انرژی آمریکا درباره زمان بسته بودن تنگه هرمز
🔹
وزارت انرژی آمریکا گفته تصور می‌کند که تنگه هرمز تا اواخر ماه مه میلادی بسته خواهد ماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/akhbarefori/651974" target="_blank">📅 19:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651973">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH_nwoLqDAmvxRoZvQAoJ_M0TQRVP09iL5H-4Jobq_ojNJw9o3c0ckLIepAonzC0BDAqVImg3z4nc6FjEnYOkS4Pp0T26QsLbcqkrSwVLEw6SaUXq2D0O4-1AJGV51zYHgDIVLX3bqltYCMXbr07R1Ue_5GDJOXun56-Pnk1y_zUbKGWEHqgx8peAJNfhllUwaDuPEht1du3ihTcHPsMtYv4sRs9X4e5GAUmRL_jdK6yJxrYPQA0wbFCOSbUPsp-eUNV6bABg8ad0qbVqQwudjQGAru_pKgn-7L9rwrZYdllzPNy8pL-Poj3cXMoMjalDDZYUylJDHq3DgXIYbb-3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افرادی که وسط جنگ هم دست از افزایش قیمت خودرو برنمی‌دارند!
🔹
طاهری، عضو کمیسیون صنایع مجلس: ایران‌خودرو با مدیریت جدید نباید هر اقدامی را بدون توجه به سیاست‌های کلان انجام دهد.
🔹
پیش از این بارها هشدار داده بودیم که واگذاری‌ شرکت‌های خودروسازی از نظر ما با تعارض منافع همراه خواهد بود.
🔹
انتظار می‌رود قوه قضائیه به‌صورت جدی به این موضوع ورود کند زیرا تصمیمات مدیریتی در حوزه خودرو مستقیماً بر زندگی مردم اثر می‌گذارد.
🔹
الان کشور گرفتار افرادی است که وسط جنگ خودرو را گران می‌کنند.
🔹
حتی در دوره‌ای که مدیریت خودروسازان دولتی بود، اگرچه مردم از وضعیت خودرو رضایت کامل نداشتند، اما سیاست‌های کلان حاکمیت در حوزه قیمت‌گذاری رعایت می‌شد و کم‌تر شاهد تصمیماتی بودیم که در شرایط حساس کشور موجب افزایش قیمت‌ها شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/akhbarefori/651973" target="_blank">📅 19:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651972">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsYk0BieLVPHMIDxDr2XIDa9PhWqtjj9q1ArsZuL5MUkoUufNeP2-nDgaAzpBNG-QHdI-7_5y_tiQgZaAXL_I7RtbhrqlUunhaE7PfJkPu5aHmC9AxdvGi2oV-gv-V9RUMzm_0RauJ0nu56ISR8k2CUUQqu0Hprna9Yk_TLh_mGkfQRY42C6ZV7JtGfquO_DEnXyWoHjlNRQwdh-oBLn9rWmuEwLjbX1TQE2a8MUj2lfy-eHB1gWRWq6mDp9_uBH77NffX7Dqvi2T1j7qHLxTcaVXNjA-D1KaFRwyB2SdNNPu7AmfAtENy-rYWEIWTdk_EUywr0URjoQmshbbo-b8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتهام زدایی رییس دستگاه قضا از اپراتور ها با احضار مسئولین ذی ربط
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/akhbarefori/651972" target="_blank">📅 19:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651971">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8549a7b4e.mp4?token=JZhRI_FBQXbIaBUBL9zLWh6H4YM7S0D813mII-DVi_sKWAUZb8IDk3xvohvsLIhC5EMbGL68hi-XNOVynnt7_MHMAI_wTwcxLHdLqCE6_T-cN4PVRh3OcIODchCuZSsq1vg6CApc-cuUthF0Bc69V4HyMKXhPbRd3T_d0yX34o--0aRlbUbGBKepnZJ82ebTnWC15J27Q5jVXTvDtiv-96Oq8BWSUmo84UE3NDg2JlWbvnuFgWIi9YN9JtdmArINwR03v13i17J5Dl1o_OV7_y5D8XnAmmWNRui_GivyGsH3bnXHYvL8WmiVjZ28DWsY9EPZ4G6VrQ-f6B6luNV6Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8549a7b4e.mp4?token=JZhRI_FBQXbIaBUBL9zLWh6H4YM7S0D813mII-DVi_sKWAUZb8IDk3xvohvsLIhC5EMbGL68hi-XNOVynnt7_MHMAI_wTwcxLHdLqCE6_T-cN4PVRh3OcIODchCuZSsq1vg6CApc-cuUthF0Bc69V4HyMKXhPbRd3T_d0yX34o--0aRlbUbGBKepnZJ82ebTnWC15J27Q5jVXTvDtiv-96Oq8BWSUmo84UE3NDg2JlWbvnuFgWIi9YN9JtdmArINwR03v13i17J5Dl1o_OV7_y5D8XnAmmWNRui_GivyGsH3bnXHYvL8WmiVjZ28DWsY9EPZ4G6VrQ-f6B6luNV6Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معترضان ضدجنگ جلسه هگست در کنگره را مختل کردند
🔹
جلسه استماع سنای آمریکا درباره بودجه نظامی مرتبط با جنگ علیه ایران با اعتراض فعالان ضدجنگ مختل شد.
🔹
یک زن معترض پیش از انتقال از صحن سنا، مخالفت خود را با ادامه جنگ علیه ایران را فریاد زد.
🔹
معترضان خواستار توقف بودجه‌ریزی برای جنگ و مخالفت با افزایش هزینه‌های نظامی آمریکا شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/akhbarefori/651971" target="_blank">📅 19:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651970">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70bd3f20.mp4?token=rP3Om2p1EMiqxZYbkAKSUSo5W2-9bfJNOVVvIyAHsPwydz7fdx5UjrPI-sMtrnJrCtKVe-h55MxLqBniRzDSfhQjtMx02tgaEBwI4XcUxF3RvHT-VUlD8Lq7YwxVtExRXMdhPgzoYZA_Ggw6EmLNSFBt-FAT4ruE-p9Z9mMKkfKupwDbNcVP5R3otq6SjqwLRFT2Pfpffu3-Sl-MvrmEEYAe2btO7NJpsW58Idi98glXkBtqgBbg0Gsg579utggvg7U9lEkSzG2_Kcxw0vS-RKGZ9YFhvVH66vt4ALIwFuhyykJDWV2zRTOHWGY0VolBsCV5rUFhhRijdCs-APx9-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70bd3f20.mp4?token=rP3Om2p1EMiqxZYbkAKSUSo5W2-9bfJNOVVvIyAHsPwydz7fdx5UjrPI-sMtrnJrCtKVe-h55MxLqBniRzDSfhQjtMx02tgaEBwI4XcUxF3RvHT-VUlD8Lq7YwxVtExRXMdhPgzoYZA_Ggw6EmLNSFBt-FAT4ruE-p9Z9mMKkfKupwDbNcVP5R3otq6SjqwLRFT2Pfpffu3-Sl-MvrmEEYAe2btO7NJpsW58Idi98glXkBtqgBbg0Gsg579utggvg7U9lEkSzG2_Kcxw0vS-RKGZ9YFhvVH66vt4ALIwFuhyykJDWV2zRTOHWGY0VolBsCV5rUFhhRijdCs-APx9-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده کنگرهٔ آمریکا: طبق گزارش‌ها ما تا یک ماه پیش در جنگ با ایران ۳۹ هواگرد از دست داده‌ایم که برخی از آن‌ها جایگزین ندارد
🔹
اِد کِیس، نماینده کنگره: طبق گزارشی در پایگاه «وار زون»، ما حدود ۳۹ هواگرد از دست داده‌ایم، که البته آن گزارش قدیمی است. متعلق به تقریباً یک ماه پیش است. آیا هزینۀ جایگزینی تمام آن هواگردها را می‌دانید؟ با این فرض که برخی از آن هواپیماها قابل جایگزینی نیستند، اما قاعدتاً باید آن‌ها را با نوعی ظرفیت و توانمندی جایگزین کنید.
🔹
نماینده پنتاگون: هزینه‌هایی در این مورد وجود دارد، اما می‌خواهم جزئیات دقیق آن‌ها را به صورت مکتوب به شما ارائه دهم. چون همان‌طور که می‌توانید تصور کنید، محاسبه هزینهٔ تعمیرات هواپیما کار بسیار دشواری است. ما می‌خواهیم پیش از برآورد هزینه، یک عیب‌یابی کامل از هواپیماها انجام دهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/akhbarefori/651970" target="_blank">📅 19:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651968">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae403d377e.mp4?token=WLppBUj-GiKts0KYVtwTAprhMDi79EhngQdyOSv0_HY49RYzTBkrcDgPMP69Wj-2KXkbekuvqYCd141fF_7M-kZqlYHUoN8Wnc5oDYdZuB-NOE-F3S1RTNtPdlY89iV6ZJacwkB7k9YmhuV9YHC8F5JYN0doNUcWKvfZ9UL2FrvkhVLO7ATFeEBfiBC301sPhtxlgI57rCHJ7RGjs7BLLbb88ZwM3Lb6oYX0aYp5ReSmi6hOh7U4S68-j7PZCc7-dGtPVI8TplpLLe_4uWJXLMBAeKEaERzBsC1MpsxvybSv4Vsl3IcJddu-XxY3zRf8_8X80mNa0loucC0q-8VHNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae403d377e.mp4?token=WLppBUj-GiKts0KYVtwTAprhMDi79EhngQdyOSv0_HY49RYzTBkrcDgPMP69Wj-2KXkbekuvqYCd141fF_7M-kZqlYHUoN8Wnc5oDYdZuB-NOE-F3S1RTNtPdlY89iV6ZJacwkB7k9YmhuV9YHC8F5JYN0doNUcWKvfZ9UL2FrvkhVLO7ATFeEBfiBC301sPhtxlgI57rCHJ7RGjs7BLLbb88ZwM3Lb6oYX0aYp5ReSmi6hOh7U4S68-j7PZCc7-dGtPVI8TplpLLe_4uWJXLMBAeKEaERzBsC1MpsxvybSv4Vsl3IcJddu-XxY3zRf8_8X80mNa0loucC0q-8VHNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی دولت: اینترنت پرو مصوبه شورای عالی امنیت ملی برای کسب‌وکارها است که پزشکیان رئیس این شورای است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/akhbarefori/651968" target="_blank">📅 19:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651967">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مینو محرز: هانتا ویروس جهش پیدا نمی‌کند مگر اینکه آن را دستکاری کنند
مینو محرز،  استاد دانشگاه علوم پزشکی تهران در
#گفتگو
با خبرفوری:
🔹
ویروس هانتا سالهاست کشف شده و جهش پیدا نکرده است و از جوندگان به انسان منتقل می شود، نه انسان به انسان.
در آن کشتی کروز همه جمعیت حاضر در کشتی مبتلا نشدند و تنها عده کمی درگیر شدند.
🔹
این ویروس تاکنون جهش نیافته و  با علم امروز از انسان به انسان منتقل نمی شود.
🔹
بنابراین ویروس هانتا جهش پیدا نمی کند چون سالهاست که وجود دارد مگر اینکه آن را دستکاری کنند که البته بعید است چون خیلی از ویروس های دیگر نسبت به ویروس هانتا قابلیت بیشتری را برای این مسئله دارند.
@TV_Fori</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/akhbarefori/651967" target="_blank">📅 19:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651966">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dU0nOqiCWEaHvjD8wV90AOWDM_VlPi1vNwFP-JD3RGDIDGawgFA-YllQ0mPCHGPN9J5xFLmVn4cIYZ9W84CnyCu8e3Xz30jmLsdgT2nyFPLgE4cJqG5pZpVukl9cVz2J9dEOMFsg5Z5BcFmgpXDb0ZHMirk0z0KRByiEGYLg08jALzF9tR86HbPPVmKCRvM31wKb3LTbZOjWlGdg2V1kro8wSUpdu7CMy_j_JYkJQFFYPi87-di-gNZg3grS2VpfpK2Gu655sCCiqAEFhPOqOwZXhO-BWkEPMrLI2kVqXDJKZItH0MSBWyn5PC1u7c1T9fYQ708KhHsjgLxibq2mNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایش فیلم در دالان تاریک قطع اینترنت/ جنگ چه محدودیت‌هایی برای وی او دی‌ها به وجود آورد؟
🔹
وی او دی‌ها که قرار بود تحول ریشه‌ای عرضه محتوای آنلاین را بر عهده بگیرند این روزها در دالان تاریک قطعی اینترنت به دنبال حفظ کورسوی حیات خود هستند.
گزارش خبرفوری را ابنجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3212579</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/akhbarefori/651966" target="_blank">📅 19:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651965">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d499d05e5.mp4?token=GgV_FLf7dGgSaCxSzn6UcwWdWG5pggyA4OJv16EPU5jHdqrGU5LTso8HFuGXZyWFGEV0clDLIu3OFiNoBBf7mUselb2yhNz8zSxSwVZsVhVYvi071UOYOZ--ba-TeZzGO63gDi42BKWgQFGjq_WF64PbOzIk2RrnpC8jqdDxvNE5W-oxb3tsAf5uv-aJRVYN0RnkNgGIHT4NRuBXskqrFtCirzeRQ-zOSU1VB2YV8DSIV5CEEkuzlmCBgDJUCMHJ9aJVYkxeCSPKhxPh-6ZM698kLMogFY9pGXh-CCi4HecDQzlRjb8Yz06IRjOoQ_SvTS1c0MfBVTEb8tD7mfEY3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d499d05e5.mp4?token=GgV_FLf7dGgSaCxSzn6UcwWdWG5pggyA4OJv16EPU5jHdqrGU5LTso8HFuGXZyWFGEV0clDLIu3OFiNoBBf7mUselb2yhNz8zSxSwVZsVhVYvi071UOYOZ--ba-TeZzGO63gDi42BKWgQFGjq_WF64PbOzIk2RrnpC8jqdDxvNE5W-oxb3tsAf5uv-aJRVYN0RnkNgGIHT4NRuBXskqrFtCirzeRQ-zOSU1VB2YV8DSIV5CEEkuzlmCBgDJUCMHJ9aJVYkxeCSPKhxPh-6ZM698kLMogFY9pGXh-CCi4HecDQzlRjb8Yz06IRjOoQ_SvTS1c0MfBVTEb8tD7mfEY3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در پایگاه نظامی اسرائیل در شمال فلسطین اشغالی
🔹
منابع اسرائیلی گزارش داد این مقر در نزدیکی شهرک «مرگالیوت» قرار دارد و دچار آتش‌سوزی شده است.
🔹
این مسئله ناشی از حملات حزب‌الله به این شهرک اعلام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/akhbarefori/651965" target="_blank">📅 18:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651964">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIe3jHXt26xSHRFYVa9JZ8nkm43K2XskmP2WVOShkg4K2-yv9ovHMGX2d8LjJVKsJFtxlvqw3Bft8w2B8P3zJ9SmL77ps6jCnL95N7HOlIQc65YTD06tePKW8SPefUPHk8Kw1XbtFZ268lxvsZQHe3sIBWmMCscmWYIRNpjXUUWgwzYuuz8bU33afqC3NOzvpf0TN_k-Ww7FLOV4IFQRhEJGeNo0AUFKMM8D78g4E3JLCX6wtU_9t3fIfccJhapn8K5VL9Nk9JbzBHKYSmbE_o8nx2yWrX0Cwz4OjQBbT-gxSuC6_fB0th5lV40tB1ZBWC9xnZ_s_vfL0I3L7G5s9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات پیام تهران به پکن درباره تنگه هرمز
🔹
رحمانی فضلی، سفیر جمهوری اسلامی ایران در چین با اشاره به تلاش چین برای کاهش تنش در منطقه غرب آسیا در نتیجه جنگ تحمیل شده به ایران گفت: «پکن کوشید از طریق رایزنی با بازیگران مؤثر، ارایه ابتکار صلحی مشترک با پاکستان که زمینه ساز گفتگوهای اسلام آباد شد و نیز طح چهار ماده ای اقای شی جین پینگ مسیر بازگشت به گفت‌وگو را باز نگه دارد و تقویت کند.»
🔹
مسئله اصلی برای تهران این است که آیا طرف مقابل آماده شنیدن پیام واقعی ایران هست یا نه. پیام ایران روشن است: توقف دایمی جنگ، تثبیت آتش‌بس پایدار، رفع محاصره و احترام به حقوق مشروع ایران. چین می‌تواند این پیام را در سطح قدرت‌های بزرگ بازتاب دهد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/akhbarefori/651964" target="_blank">📅 18:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651963">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b4c0212b.mp4?token=FipgJtzp61IgNXrfka3WpEQrxamS6q12gU_TF-loft8vuPU_Kn1OaSy9mpFTJT3uPhtLDdAQj2dxoTwtYwNpLOe6CyPiztFC3D-sItFqPpKXavAY2OTXZWmlhVyRAZd8Ke3G9DUbtjbL1UO64mWODhLN1AIOzExjincMPJIlfXmbvFCl5MF6tOQGM3nunKxLCnSO4Z9vH1VFex_qo63-sjaQIiRGCfm5kIn-K3Dd67D7SaGKv64tl96zs56wsJtKP3V0nfsQonunh1yvKj6R35H0oFQ273Mgzz5u4zHdcCtoaOlYoQ57Wvpvyv5aklGv39jwJqwqb1YWlmw3ck_IqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b4c0212b.mp4?token=FipgJtzp61IgNXrfka3WpEQrxamS6q12gU_TF-loft8vuPU_Kn1OaSy9mpFTJT3uPhtLDdAQj2dxoTwtYwNpLOe6CyPiztFC3D-sItFqPpKXavAY2OTXZWmlhVyRAZd8Ke3G9DUbtjbL1UO64mWODhLN1AIOzExjincMPJIlfXmbvFCl5MF6tOQGM3nunKxLCnSO4Z9vH1VFex_qo63-sjaQIiRGCfm5kIn-K3Dd67D7SaGKv64tl96zs56wsJtKP3V0nfsQonunh1yvKj6R35H0oFQ273Mgzz5u4zHdcCtoaOlYoQ57Wvpvyv5aklGv39jwJqwqb1YWlmw3ck_IqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگترین اتاق فرار دنیا کجاست؟!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/akhbarefori/651963" target="_blank">📅 18:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651962">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOES2igykMhdwqX1oKq6G4WOPCeqWWGnmeT7grfvGaLjDAl-aEm-YG6o0JM6CEr3S2a5RM9Z9c477H8b0FyIEGJpkthes5Gp-yp4cGbyaWo_DWuMC4Mk8GVwEg9l7cEBo1sE1KgMYCr8bc74ZX1OgZ0VS6klx7xeknAERFiEEIy2R1TrCQMFNbn1A4LYO_HmF43no4lVoZV2sAQEtbhoGijspkBRBTo5_fGMmtQQ7PVFH7sviNzWFgoCrNUph4bStguxQHOFf7W6SxpFLd1dpoBHworIZT9oRT-5Xv_TpldHkrEYWswAF30WwWI1mSS87pAiBZ7TreQpPqiFvOvZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبیعت در بند پلاستیک
🔹
هر بطری، هر کیسه، هر انتخاب کوچک، می‌تواند حیوانی را آزاد کند. آینده‌ سبز از تصمیم‌های امروز ما شروع می‌شود.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/akhbarefori/651962" target="_blank">📅 18:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651961">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
کویت سفیر ایران را احضار کرد
🔹
وزارت خارجه کویت با ادعای ورود چند نیروی سپاه پاسداران به جزیره بوبیان، از احضار سفیر ایران خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/akhbarefori/651961" target="_blank">📅 18:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651960">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68eac19863.mp4?token=DZonB4Zj1R-Mv6JQ7iRtJvQMHOo0gRgbZM7KtwLl5RoOZusXKfdVr8zrnQAnpTpB5RCuug7EiX_rJBACI05dkYnGhVm38jtsLq6RcRkrNjmHPuLglR_NmAHT0fuBiFNrZtIYgMv_vz49tDMz0WAUipT6p1vlACMPlfSKrA4B2P_qVYfuhKsxOXRfimsshSaR1qE0Swz43L6y0uWA7KO5-Ui9boiAXi6LWfiMkM5OQfRj8Ec28xDu6fUpiG34fz4rguO4pWDU959UAdZvVd5nxs2_goYk13Ls04kiDmUuOqbWjWUZEV0gQOiP0OOch7VyzGfvnrfNlb9OXBVxiVCgyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68eac19863.mp4?token=DZonB4Zj1R-Mv6JQ7iRtJvQMHOo0gRgbZM7KtwLl5RoOZusXKfdVr8zrnQAnpTpB5RCuug7EiX_rJBACI05dkYnGhVm38jtsLq6RcRkrNjmHPuLglR_NmAHT0fuBiFNrZtIYgMv_vz49tDMz0WAUipT6p1vlACMPlfSKrA4B2P_qVYfuhKsxOXRfimsshSaR1qE0Swz43L6y0uWA7KO5-Ui9boiAXi6LWfiMkM5OQfRj8Ec28xDu6fUpiG34fz4rguO4pWDU959UAdZvVd5nxs2_goYk13Ls04kiDmUuOqbWjWUZEV0gQOiP0OOch7VyzGfvnrfNlb9OXBVxiVCgyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور آمریکایی: وزیر جنگ ترامپ گفته جایگزینی مهمات استفاده‌شده در جنگ ایران سال‌ها زمان می‌برد
🔹
دولت ترامپ حجم عظیمی از مهمات را در جنگ با ایران مصرف کرده است. بعد از ۱۵ هزار حمله، تنها چیزی که نصیبمان شد، ۱۳ کشتۀ آمریکایی، بسته‌شدن تنگۀ هرمز، بنزین ۴.۸ دلاری بود.
🔹
آن‌ها بدون هدف استراتژیک، بدون برنامه و بدون جدول زمانی وارد این ماجرا شدند. حالا هیچ راهبردی برای خروج ندارند و به دست‌وپازدن افتاده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/akhbarefori/651960" target="_blank">📅 18:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651959">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea6055463.mp4?token=UXS6gpL7EYPm4pIq9B4bP_fA5qJs_dhXWSAbbkzFnKol7E1uShyjSpi8o8Udo0efuiTy2S53BO9E2Fp8LE8J-n-r6bz3C7RMhbGoec7sAvqc_bzK3LWHJcqfzDQ_kH3e371iNeY5Wu3t7LYEMsPHWVLLuXbTP094Dy_I1nMFsB1YSB5ezq5gmSGaiLrCKZbyCyTLefDLOu_h6ktESmrlzch2tJ1d8jp-_yknDCIwNGyNVFHb_6wPPINRXupYdU2YBwHpmNsgMqKf7L_s6ftfqYk9r7aRv3N_ZRfAprUiRiM4TLeYRWoV97UM9CViiGychzBdWaGn4sFZTT6rTB3AYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea6055463.mp4?token=UXS6gpL7EYPm4pIq9B4bP_fA5qJs_dhXWSAbbkzFnKol7E1uShyjSpi8o8Udo0efuiTy2S53BO9E2Fp8LE8J-n-r6bz3C7RMhbGoec7sAvqc_bzK3LWHJcqfzDQ_kH3e371iNeY5Wu3t7LYEMsPHWVLLuXbTP094Dy_I1nMFsB1YSB5ezq5gmSGaiLrCKZbyCyTLefDLOu_h6ktESmrlzch2tJ1d8jp-_yknDCIwNGyNVFHb_6wPPINRXupYdU2YBwHpmNsgMqKf7L_s6ftfqYk9r7aRv3N_ZRfAprUiRiM4TLeYRWoV97UM9CViiGychzBdWaGn4sFZTT6rTB3AYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدف جنگ از زبان روبیو: بازگشت به زمان قبل از جنگ
🔹
مارکو روبیو گفت: «ترجیح ما این است که تنگه هرمز باز باشد، به همان شکلی که قرار است باز باشد و به همان شکلی برگردد که قبلاً بود.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/akhbarefori/651959" target="_blank">📅 17:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651958">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dz73ruePXJX2knM7W0yiQ--hrNcLyAtBxXCh6azCyQQYQpvBiDKaUc95KyQBIXNhwJA2HKzjVp8t15nEPHujZWiJjZHdEN98dIJJwpqgep8HILK7LkkFWpOQrlLiGr55Mw6V5QaYm38B_RD99HCk1TRh-hDMfA9CecQsXPpMh_EI72QNWbtXENlhf56I2zO80lNytqLZSHeIibVFUmYBb3xfJcMMXsO-xeWRGz6vAQOVswmjlHyb2JNPx25O3xtXmPfXHPvbrn6Z7akmgzJ9zXYZs9WBjWfW_m5qkJJOGu2PCGZCfc3SN7ajONhTbKDuh3cTF_PRVxT2xKzcsqTU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران و آمریکا دورتر از همیشه | مرحله اول جنگ؛ بازگشایی تنگه هرمز
🔹
آمریکا و ایران همچنان بر سر چارچوب یک توافق برای پایان دادن به جنگ و بازگشایی تنگه راهبردی هرمز اختلافات عمیقی دارند؛ موضوعی که به یکی از حساس‌ترین پرونده‌های دیپلماتیک سال تبدیل شده است.
در این‌باره بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3214220</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/akhbarefori/651958" target="_blank">📅 17:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651957">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdp2D6Rq9T73CUJ_P69z7Fwwd2XObWLZDcjOC2-zSSCyF4ETEqI5zVrdX2is24GD0wW5CfZk7ekI-emiGamE385zAmckZOmU5gMM4POz8E6KjVHaJJo-8Ny43qiJVfDShUdCfugL5uteRpYR8xnWYIM_9ijgxR9LRQ-3w2Ak5KmBBMo_rlOFp5HVFZkvBL7REf9yl8ZlBwIcdbj1uQrCgSXe2Rk_Mgy54HPWIZ0aMmYSK8ayMPK85TWuyWTTiiEaqMTaX8LvDgN8vqoD1B7SZr2jMJxm08hbxH6iFJKH7DqaEf1b5d3w-Y_Sq4cruQLDOpDbysPE2euRh_u_88Xpzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: «ما ۱۰۰٪ گرد و غبار هسته‌ای و کل ماجرا را از ایران خواهیم گرفت»
🔹
یک بار در عملیات شهرضا سرنوشت ماجرا جویی نیروهایش را دیده اگر هوس رقم زدن طبس ۳ را دارد در خدمتیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/651957" target="_blank">📅 17:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651956">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIuj6KQvZSOTnxzMiPijBxA7dBN99zZ02yr5jYA1pAe3VjsrtRKaWy89oGbgPJJ8cafWg7Nw5rycccJ4WqIeDbu-hHBrFQ7Ju2sFXPFosgN9qDuOIebG3jwTFxneKcfLVgiCESRv7KcgqSHP-k0rZzB5smZuU8RdVCVPTFJ9hUmYRK2kQFCRQHaD3yacoHUV73MU8yznLJUIEhpRY_QLpv2v1NJnersx0wTIvlO6aScI8C4klevt8k5uKuRMCF338TSRoeyU6el0075baJdzV-I122mEhkA08_CUxVUZ6llw-CoJDZoh4Pmz6rmOOn3HmSvRTSHFADQ2jibE0ccIog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگرداندن اولین نفتکش غیرایرانی از محاصره آمریکا
🔹
نفتکش حامل نفت عراق به دلیل اینکه با اجازه ایران از تنگه هرمز عبور کرده بود، توسط نیروی دریایی آمریکا بازگردانده شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/akhbarefori/651956" target="_blank">📅 17:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651955">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cbf8f3249.mov?token=Z1m7dfRERLG9LYOzOEfziDrCJ_whzdOsiVkHamC1Uv65m5_jRRyLQBsSjLxMMEbXhhRp-yHz2ZJvAFqkNPZSJ36V9okSfELNz1ZrvakJu_YnPYBNqvmKe9eJz13uHWh70hPBUbJV7oyCDGzbNnNAUc2VP_2bu84pavdKDfVf-dGFUMVe91-x5t5tt_zenAhvZXfpRhFB5OFNKHCPblU7_bVfUm4RoEKROkhmtZg2PPsEu8_Y2yo4r0NyVSGC-FiytuwMU3GaZNjNtBoeAxQBhIG-YATATCRwv-xjdSPVbmSus_1RcsJy654aj0shfumnldW2rXEaXSRahZiBUM4fIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cbf8f3249.mov?token=Z1m7dfRERLG9LYOzOEfziDrCJ_whzdOsiVkHamC1Uv65m5_jRRyLQBsSjLxMMEbXhhRp-yHz2ZJvAFqkNPZSJ36V9okSfELNz1ZrvakJu_YnPYBNqvmKe9eJz13uHWh70hPBUbJV7oyCDGzbNnNAUc2VP_2bu84pavdKDfVf-dGFUMVe91-x5t5tt_zenAhvZXfpRhFB5OFNKHCPblU7_bVfUm4RoEKROkhmtZg2PPsEu8_Y2yo4r0NyVSGC-FiytuwMU3GaZNjNtBoeAxQBhIG-YATATCRwv-xjdSPVbmSus_1RcsJy654aj0shfumnldW2rXEaXSRahZiBUM4fIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات و آمار آسیب به اورژانس و آمبولانس ها در جنگ رمضان
🔹
توکلی رئیس اورژانس استان تهران: در طول جنگ رمضان ۲۷ دستگاه آمبولانس، ۱۰ خودروی پشتیبان عملیات و یک فروند بالگرد به صورت کامل و ۲۷ پایگاه ما آسیب دیدند.
🔹
بعد از آغاز آتش بس تا به امروز همکاران ما ۲۴ ساعته آماده به خدمت هستند و هیچگونه تغییری ندادیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/akhbarefori/651955" target="_blank">📅 17:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651953">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9524ecb154.mp4?token=o-qrdmqejbLlz7woiPbYiON1OWXSJ4790AT6ZCmvIhUrryQ1EUGoTSfxvxUbxQyyvMsdXdZ9JeLKbX0c6A2dUwdSiDd7oW8vlSowlmgI_518i31kcBczBbCN0qx4I-7nzVau3GAJZQrGfkhHfJ22WFWSBP2D4hS-VMOeLBIiJHHhaToEeYrXnPagifTcK2RmpgFE_rQftqVWP-FqhtvTkTyMTHvUlv8t0-LSrTiJKXzM34HEpFUAFj3ip933L4XL14CrUzkzG_strIKpHWzB2k8zmzUiUB1g56gZmC4IE9AkNJ021xa8CYygybwi_B_lNf6eyOM11TaNQZZAr5xxFkdgQfjBJoKka4_JYfciSkb8Rh1fIBoybJkamD-CeAQXxlQZFkTYHS3VfRUBLt5nQfmJDJBzMQwibhabI0ZlsLi8qGGz9HlXzpVzZpnRaQDJpH1q3ydcZgQyAoQ4zoWYn178Wq4kGbkpRxjHyCrxUj71PKGPUsX1z_cdE8oFkUB2BCmRpz-iOGifPREstKPkbBtT5yr4A8zvYAsJtE1n6KKYcT5g9FUxW5YHr-husIGRlqpawRiEP2T2ur8LMnsoSK_BUJ5QbjvxAqjqp2Q-sGraxMpZHRA9f2hz4tep0oZZQCPEcDnNLEkp2k-dL9GNhP0ARW0kw8mpDSWbDxrPPEM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9524ecb154.mp4?token=o-qrdmqejbLlz7woiPbYiON1OWXSJ4790AT6ZCmvIhUrryQ1EUGoTSfxvxUbxQyyvMsdXdZ9JeLKbX0c6A2dUwdSiDd7oW8vlSowlmgI_518i31kcBczBbCN0qx4I-7nzVau3GAJZQrGfkhHfJ22WFWSBP2D4hS-VMOeLBIiJHHhaToEeYrXnPagifTcK2RmpgFE_rQftqVWP-FqhtvTkTyMTHvUlv8t0-LSrTiJKXzM34HEpFUAFj3ip933L4XL14CrUzkzG_strIKpHWzB2k8zmzUiUB1g56gZmC4IE9AkNJ021xa8CYygybwi_B_lNf6eyOM11TaNQZZAr5xxFkdgQfjBJoKka4_JYfciSkb8Rh1fIBoybJkamD-CeAQXxlQZFkTYHS3VfRUBLt5nQfmJDJBzMQwibhabI0ZlsLi8qGGz9HlXzpVzZpnRaQDJpH1q3ydcZgQyAoQ4zoWYn178Wq4kGbkpRxjHyCrxUj71PKGPUsX1z_cdE8oFkUB2BCmRpz-iOGifPREstKPkbBtT5yr4A8zvYAsJtE1n6KKYcT5g9FUxW5YHr-husIGRlqpawRiEP2T2ur8LMnsoSK_BUJ5QbjvxAqjqp2Q-sGraxMpZHRA9f2hz4tep0oZZQCPEcDnNLEkp2k-dL9GNhP0ARW0kw8mpDSWbDxrPPEM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روسیه از یک موشک عجیب و قدرتمند رونمایی می‌کند
🔹
روسیه می‌گوید که موشک جدید «Sarmat» با قابلیت حمل کلاهک هسته‌ای را با موفقیت آزمایش کرده و قصد دارد آن را تا پایان سال جاری در حالت آماده‌باش رزمی قرار دهد.
🔹
پوتین می‌گوید برد این موشک می‌تواند از ۳۵,۰۰۰ کیلومتر فراتر رود.
🔹
پوتین: «قدرت کل موشک سارمات بیش از چهار برابر هر نمونهٔ معادل غربی است.»
📲
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/akhbarefori/651953" target="_blank">📅 17:41 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651952">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70b4b75817.mov?token=o2tnb4pp6Y0TLikAZ0yTlhgg3P1a6XftX4G0J58ZJzaO9Rk5g8HWN45WN2Yl7sVufxIpuRoBzdmDJd9BxSJP-74YhgkGoMsDjOSLLdeW7OqyxYB0mhOnDUO85qRjJbD3zlWD6eZ8Jsk0okxf1_nAPvinT9cI9KO1Izbq62EIAy7Md1TzKJJFbF8h2BXxcNI2KiHoKUpZOMLGc3lsFHpPXOeh3BHtsAyxwggUIyvsPTiwyDkrUidWJEjuQYxW5GZMHHwYurKw-f7wAVf9gCoPgQOv6dew1Z9bUbOGpB-85bqYw2Z33ATLRQ-vTmJxDqBCRZ6knJrCfG-hggevHZfCeDJZ4Y1-yAvLqAN6xpA39WghNvTB-hxQFill_NKGJzROeEFgkJpgD1k1XMoU10nCSfiqWey6sHdvBsAL7nfotyfQvThOsMno_MeQVe1j8rL7EZl32zEi-rd3ED6JEuTXPkicDGz2jesoGc_oOuBIUiVaAV6R_7pO5fjFwSL5dbPe6eM9kGRqfA3GvLsiOZ41d1oMkKQuc3LLcGQCs-cglPWj9v0Q-Voxsw3swvuOgDtfUU15YbAosn4zLCoc4-Bsmxkw7K0QqW0n_dzB0Zl7sLWuOL3ARun6HYc_bWiwakrdsTIgOw0KKW0hRBXJ0r9vrrbrvNeEsWX0zbytVPqWOXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70b4b75817.mov?token=o2tnb4pp6Y0TLikAZ0yTlhgg3P1a6XftX4G0J58ZJzaO9Rk5g8HWN45WN2Yl7sVufxIpuRoBzdmDJd9BxSJP-74YhgkGoMsDjOSLLdeW7OqyxYB0mhOnDUO85qRjJbD3zlWD6eZ8Jsk0okxf1_nAPvinT9cI9KO1Izbq62EIAy7Md1TzKJJFbF8h2BXxcNI2KiHoKUpZOMLGc3lsFHpPXOeh3BHtsAyxwggUIyvsPTiwyDkrUidWJEjuQYxW5GZMHHwYurKw-f7wAVf9gCoPgQOv6dew1Z9bUbOGpB-85bqYw2Z33ATLRQ-vTmJxDqBCRZ6knJrCfG-hggevHZfCeDJZ4Y1-yAvLqAN6xpA39WghNvTB-hxQFill_NKGJzROeEFgkJpgD1k1XMoU10nCSfiqWey6sHdvBsAL7nfotyfQvThOsMno_MeQVe1j8rL7EZl32zEi-rd3ED6JEuTXPkicDGz2jesoGc_oOuBIUiVaAV6R_7pO5fjFwSL5dbPe6eM9kGRqfA3GvLsiOZ41d1oMkKQuc3LLcGQCs-cglPWj9v0Q-Voxsw3swvuOgDtfUU15YbAosn4zLCoc4-Bsmxkw7K0QqW0n_dzB0Zl7sLWuOL3ARun6HYc_bWiwakrdsTIgOw0KKW0hRBXJ0r9vrrbrvNeEsWX0zbytVPqWOXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار طلایی‌نیک سخنگوی وزارت دفاع: ایران در هردو حوزه دیپلماسی و میدان ظرفیت های دفاع از ملتش را نشان داده است؛ هرگونه تهدید و تعرض از سمت دشمن قطعا بی درنگ با واکنش پشیمان کننده از ما مواجه خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/akhbarefori/651952" target="_blank">📅 17:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651951">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTxonsZYUBK548AY2Z1Bcwg870KHqWXEiBmAFYop5g0s-0EwBUUDWllfI90cI8O413kW0xYllIB7Ykp6n8rNUk_ghQCaPOQx90sgSaIqd724jWKUdJt0VOBWjpG7sQQguJBxtZM9XT3SvPXD9T8pVcqovFgPdmYjDKfVYXgQx8FbUTnngAgUPEA3i2GSUHFatRBLpUcm_wA5TFVNAQJgi52ZGh4UU8oduCA1Tr9Nw7zAnegnri3gd-ZqVPy8-lctSfQPvgwmiz_Np0qwWZO9qQyzmWS33gEvr2O5Tbw1ztCpd8W7L14JbjTAav--9h3yU_9ujoN-_Iyw66Dw7OezXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ بازهم مدعی پیروزه شده است؛ آره  ۲ بار
🔹
ترامپ طبق معمول بعد از یک جنگ پر هزینه و بی‌نتیجه بازهم ادعای پیروزی کرده و گفته است:«ما در حال پیروزی هستیم؛ ما در هر جزئی از آنچه در این درگیری جنگیدیم، پیروز شده‌ایم.»
🔹
برای نابودی نیروی دریایی جنگیدند تنگه هرمز چند قفله شد.
🔹
برای اورانیوم جنگیدند شهرضا طبس شد
🔹
برای نابودی ایران جنگیدند همه ایران تبدیل به میدان انقلاب شد.
🔹
برای نفت جنگیدند جریان جهانی نفت متوقف شد.
🔹
ترامپ در ادامه هم باز تهدید کرده و گفته است:«نحوه حل این مسئله به شرایط ما، به شرایط رئیس‌جمهور ترامپ، بستگی خواهد داشت»
🔹
تا الان که ترامپ هر آتش روشن کرده ایران آن را مدیریت کرده از الان به بعد هم رئیس جمهور آمریکا اگر پیروزی می‌خواهد بیاید تا دوباره در خدمتش باشیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/akhbarefori/651951" target="_blank">📅 17:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651950">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a68529b33.mp4?token=uT79w0ouPXGN3Q6o5Z44ulhjK6OW1y62x_0-pNQT-R10O5p7CPtfP7BpTOH7Y_9OpWB7j3XPZ6aSaAMdEddk5dF2CGrGn_Xy_j9JqYoBDInsb8NFTBJKXmLbQx-31ooQ3jS5tOLXAD4AJh5Xogi3TFX6zcDPIWp6HK7fIKn71JKJuEovWKFIwGg47lju-6hYP_rOe0Wiwa48jTBix0xmrUeB5DiKtc88IS7X-1Z0GAZkkzAzoV7o__ZhpJBiziaL6rrZhs1tq4qfakVNsiFScQH6cmnnW09amZ_XfD-GmtEqtrdquIhnmXkiRs_XCIb0-oGOH5eb9vO6FYq8Yqw3qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a68529b33.mp4?token=uT79w0ouPXGN3Q6o5Z44ulhjK6OW1y62x_0-pNQT-R10O5p7CPtfP7BpTOH7Y_9OpWB7j3XPZ6aSaAMdEddk5dF2CGrGn_Xy_j9JqYoBDInsb8NFTBJKXmLbQx-31ooQ3jS5tOLXAD4AJh5Xogi3TFX6zcDPIWp6HK7fIKn71JKJuEovWKFIwGg47lju-6hYP_rOe0Wiwa48jTBix0xmrUeB5DiKtc88IS7X-1Z0GAZkkzAzoV7o__ZhpJBiziaL6rrZhs1tq4qfakVNsiFScQH6cmnnW09amZ_XfD-GmtEqtrdquIhnmXkiRs_XCIb0-oGOH5eb9vO6FYq8Yqw3qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عباس گلرو، عضو کمیسیون امنیت ملی مجلس: آمریکا ۲ خواسته دارد که برای ایران حیثیتی شده است و نمی‌تواند بپذیرد، اول توقف دائمی غنی‌سازی و دوم تحویل دادن اورانیوم غنی‌شده به آمریکا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/akhbarefori/651950" target="_blank">📅 17:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651949">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1645c3c85e.mp4?token=TjMjywt1hotS7AAxfOavCxZbtTgJG3y9E-r5UA6wHbLMWtxQBGRAmXcQ0gdCwZdDalMhUVHE770_vNefZKFZn1O7R5PfRyu6PBfb-_8ttbU1FVJGRXe1YR_H9GUKybUShqnDDkLbI5RV2JVoQRnZ9t-c_mFrUNFhT0m8M8ackDw1ssCUdjuuC3V0E0bwTEuXcpXEymdyoDWGR3vYTwRADcsSdMqx6qbhsX3Qch7Tgkspg7ESPExA6INBLeAJCZGwKALPtuwv0D-X0tp5EVuaAjLBNNV9Fz1LmLduMaAlPS8c5QEWwwZD4pI9ZRaNwLVhBBhoHMGuFCS2OzCd5UDoIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1645c3c85e.mp4?token=TjMjywt1hotS7AAxfOavCxZbtTgJG3y9E-r5UA6wHbLMWtxQBGRAmXcQ0gdCwZdDalMhUVHE770_vNefZKFZn1O7R5PfRyu6PBfb-_8ttbU1FVJGRXe1YR_H9GUKybUShqnDDkLbI5RV2JVoQRnZ9t-c_mFrUNFhT0m8M8ackDw1ssCUdjuuC3V0E0bwTEuXcpXEymdyoDWGR3vYTwRADcsSdMqx6qbhsX3Qch7Tgkspg7ESPExA6INBLeAJCZGwKALPtuwv0D-X0tp5EVuaAjLBNNV9Fz1LmLduMaAlPS8c5QEWwwZD4pI9ZRaNwLVhBBhoHMGuFCS2OzCd5UDoIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر بخشی از محموله‌های کشف شده سلاح از شبکه‌های قاچاق وابسته به رژیم صهیونی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/akhbarefori/651949" target="_blank">📅 17:12 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651948">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
جایزه ۱۵ میلیون دلاری آمریکا برای مختل کردن سیستم مالی ایران
🔹
وزارت خارجهٔ آمریکا از برنامهٔ «پاداش برای عدالت» خود برای پرداخت تا سقف ۱۵ میلیون دلار به افراد همکار با این کشور، با هدف اختلال در سازوکارهای مالی سپاه پاسداران خبر داد.
🔹
این اقدامات در ادامه کمپین موسوم به «خشم اقتصادی» دولت ترامپ علیه ایران انجام می‌شود در حالی که آمریکایی‌ها خود اذعان دارند چنین اقداماتی تاکنون نتوانسته اقتصاد ایران را از مسیر توسعه و تعامل با شرکای بین‌المللی خارج کند و بیشتر جنبه روانی و رسانه‌ای دارد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/akhbarefori/651948" target="_blank">📅 17:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651947">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0858d26d7.mp4?token=hP1tkWnWinhQ8-cgoEaUGsDf7MhDhikXLII6k57Dmxw7SdW-vebAvhDqd2feIR4WgZ-pRbMSBvRU3S92Z5FezxsPsDAse_ZjvuS0YYNwZ4uaSHwlIly03pI31v62CrB9hdBvYeYftMEtYcCh2XSKsCBGMXTgebsdSm4WaIdIfFV9A0kU9xp6AKypaTnmdXlv16ifzxizuBHlXzE7jmWRWDYHlvGE8wP66G2r_e2DO-yd9nZpfBfRpyGbDMRCJN0a6HEn3dTOB_2xpE8UAUXNbKeQrgV9e_W0Dr1P1LsPpz0HtykpoL_VJ06jFBKfZZyZd8_PAaQBrxD9lfCSeVEdDnStXcq9KhhBkvRwlr7arxNOpBTwlmIu35vD1hRSpXmUb3guMZ_0T6uJLgJpyZINAZ6t3g7DgVHH1tZRgVI4eBzBSgFXDyFAk5B_XllV53iZAMQrQK1zVC2-pXqiUYG1Qt6-WcJTn9YZ8YYkEmkzXIbxPke7xaYfdwBC371MQPb3H_4akqW5eOGIocH4EbqdpTvlDNxAKxA1lqnCT6Mi3fDi9UrTBzyYybf7Av3etd5GbuUSicDG4XR9NVEIpbb2VmkA7EdVmQhXH8avvyQ3ZteyTnqgN1_MjThzdueQMjfFdoUfagwIxcQSM0JxnkGl-M66UacwpdDdzAYXf7Gfc6k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0858d26d7.mp4?token=hP1tkWnWinhQ8-cgoEaUGsDf7MhDhikXLII6k57Dmxw7SdW-vebAvhDqd2feIR4WgZ-pRbMSBvRU3S92Z5FezxsPsDAse_ZjvuS0YYNwZ4uaSHwlIly03pI31v62CrB9hdBvYeYftMEtYcCh2XSKsCBGMXTgebsdSm4WaIdIfFV9A0kU9xp6AKypaTnmdXlv16ifzxizuBHlXzE7jmWRWDYHlvGE8wP66G2r_e2DO-yd9nZpfBfRpyGbDMRCJN0a6HEn3dTOB_2xpE8UAUXNbKeQrgV9e_W0Dr1P1LsPpz0HtykpoL_VJ06jFBKfZZyZd8_PAaQBrxD9lfCSeVEdDnStXcq9KhhBkvRwlr7arxNOpBTwlmIu35vD1hRSpXmUb3guMZ_0T6uJLgJpyZINAZ6t3g7DgVHH1tZRgVI4eBzBSgFXDyFAk5B_XllV53iZAMQrQK1zVC2-pXqiUYG1Qt6-WcJTn9YZ8YYkEmkzXIbxPke7xaYfdwBC371MQPb3H_4akqW5eOGIocH4EbqdpTvlDNxAKxA1lqnCT6Mi3fDi9UrTBzyYybf7Av3etd5GbuUSicDG4XR9NVEIpbb2VmkA7EdVmQhXH8avvyQ3ZteyTnqgN1_MjThzdueQMjfFdoUfagwIxcQSM0JxnkGl-M66UacwpdDdzAYXf7Gfc6k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پخش لحظه شکار سامانه چند ده میلیون دلاری گنبد آهنین به وسیله پهپاد ۲ هزار دلاری حزب‌الله از شبکه سه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/akhbarefori/651947" target="_blank">📅 16:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651946">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrfBliaH5gfuXHtsg21CcJUwUnJMxmAG5mEb1Z5YN78jCUzfDDBPC0HGFEQ_rhldjn_dRQkxoPGFV7FU1r-trULa75hfbAWucZxtI3rd7K3wQkIQcmDXYUj4kidKbXKTuaBCkMuRjDgy3hwB4kg3f2pXk1jvLQ4k6vzDW1f0P5daHLhIfi-QAiHkpcDiMi12igh0uw4d1zqgRmFhgMSqktw3hAv1oD8E7Gyl9HzrtZgx4sOEVg8oZBUnbGyxR7RyK_n_F3fzIAxVNKJV5xYsVbyoLBun2hhUcivuJtYf7RucBY6htmzYHRwRReT5R-jp6oqb6kkO4w7X7cZgN9s52g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه عبری: زندگی در شمال اسرائیل به جهنم تبدیل شده است
🔹
رسانه‌های اسرائیلی گزارش می‌دهند با ادامه حملات و تهدیدها از جنوب لبنان، «زندگی شهرک‌نشینان شمال به جهنم تبدیل شده است» و هیچ چشم‌اندازی برای خروج از این «کمین استراتژیک» وجود ندارد.
🔹
تصریح کرد: «ترکش‌هایی از موشک‌های رهگیر که از داخل اسرائیل به سمت لبنان شلیک شدند، به خانه‌ای در کریات شمونه برخورد کرد. این بخش خانه تقریباً به‌طور کامل ویران شد و این تنها چند دقیقه پیش از آن بود که سه کودکِ همین محله در راه مدرسه‌شان از آنجا عبور کنند».
🔹
وی سپس با طعنه پرسید: «آیا درباره این رخداد شنیدیم؟ اما تصور کنید اگر این اتفاق در کریات شمونه نمی‌افتاد و مثلاً در تل‌آویو رخ می‌داد؛ قطعاً تیتر اصلی در دستورکار تمام اسرائیل می‌ماند.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/akhbarefori/651946" target="_blank">📅 16:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651945">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8195f830.mp4?token=dMrAJuQp9hplmAOEqhIKddVdpXi-au1ggxxA4bbtmjxA45OmyA1shmO4IGlXHwEqQC30DD9oJK6ABOUyO_U-5J8LycwreX6zkixVFSFOHiv4UWJohULZ6QWHfmDh3c8CpmdHaZYlg9ASDJZP42Qlg6jJN0ZGCrcOjHWGsdeDkPeUO1xy3_9jKuPsMDXCjW8tE2BTA8xP1xAKTMmoDMg1uoQjDtw3PHN4PriC_Fnqg7vJAENoP16fiyI_oZUl23K_JJvOKB-clgElft1yds-qvBPMg8wLQeMaEwjAfxU8HSdB7VVzDgdP-aJJZEGZdLLYcEI7jqq7lkSXJDLl2sfYjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8195f830.mp4?token=dMrAJuQp9hplmAOEqhIKddVdpXi-au1ggxxA4bbtmjxA45OmyA1shmO4IGlXHwEqQC30DD9oJK6ABOUyO_U-5J8LycwreX6zkixVFSFOHiv4UWJohULZ6QWHfmDh3c8CpmdHaZYlg9ASDJZP42Qlg6jJN0ZGCrcOjHWGsdeDkPeUO1xy3_9jKuPsMDXCjW8tE2BTA8xP1xAKTMmoDMg1uoQjDtw3PHN4PriC_Fnqg7vJAENoP16fiyI_oZUl23K_JJvOKB-clgElft1yds-qvBPMg8wLQeMaEwjAfxU8HSdB7VVzDgdP-aJJZEGZdLLYcEI7jqq7lkSXJDLl2sfYjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر جنگ آمریکا: اگر لازم شد برای تشدید تنش با ایران طرح داریم
🔹
پیت هگزث در نشستی درباره بودجه دفاعی آمریکا در کنگره این کشور درباره جنگ علیه ایران گفت، ما در صورت لزوم، همانطور که طرحی برای کاهش تنش داریم، طرحی برای تشدید تنش علیه ایران نیز داریم که اگر لازم شد آن را اجرا می‌کنیم.
🔹
وی افزود، به دلیل جدیت ماموریتی که رئیس جمهور ترامپ بر عهده گرفته است و در راستای عدم دستیابی ایران به سلاح هسته‌ای، گام بعدی علیه ایران را فاش نخواهیم کرد.
🔹
اظهارات وزیر جنگ آمریکا در این باره درحالیست که بسیاری از ناظران سیاسی و تحلیلگران غربی استراتژی واشنگتن در جنگ ایران را یک شکست تمام عیار خوانده‌اند و می‌گویند که پنتاگون به هیچ یک از اهداف خود در جنگ دست نیافته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/akhbarefori/651945" target="_blank">📅 16:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651944">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
دستگیری عضو گروهک تروریستی منافقین در ازنا توسط سربازان گمنام امام زمان(عج)
🔹
سربازان گمنام امام زمان(عج) در اداره اطلاعات، یکی از عناصر عملیاتی گروهک تروریستی منافقین را در شهرستان ازنا شناسایی و دستگیر کردند.
🔹
این فرد به اتهام انجام اقدامات خرابکارانه در چند استان، ارتباط و همکاری با گروهک تروریستی منافقین و ارسال اخبار و اطلاعات برای مرتبطین خارج از کشور، تحت رصد و اشراف اطلاعاتی قرار داشت.
🔹
ماموران اداره اطلاعات با هماهنگی دستگاه قضایی و طی یک عملیات دقیق اطلاعاتی، متهم را در مخفیگاهش در شهرستان ازنا بازداشت کردند.
🔹
مجددا از مردم عزیز درخواست می شود هر گونه گزارش و اخبار ضد‌ امنیتی خود را از طریق شماره ۱۱۳ ستاد خبری وزارت اطلاعات اطلاع‌رسانی نمایند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/akhbarefori/651944" target="_blank">📅 16:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651943">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gejIWj7VO7_Oct2CKS2QmdRybEOkC6zYCloruIIeatu1xw9Mi7j9c3AO63LWp9aLPC88K4S81hlCMM9tb-DccET3jfo7CL1yPD257ETcWrSjthfSNiUIste_2bG_2b3WkP2e1x6Qx85sAlMI5i1PyH7_o2FrWPMYVgbv84MKsO3rsujjQQvHtxQMRGuge95hcLmEbLOdm58rk2_3Ss-nDbaZCeDrWsKTsPAD50q-GZDbxfOfrBTSLjNRv7SFXAwNgmEfnojqJaKrnqPOqxTuY83NjphFu6-Nj_qMub_5AFCdqeqW88IWgqIFh_A6ZHqwxXlJVontevpSF8je1LCYrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضربه سازمان اطلاعات سپاه به ۵ شبکه قاچاق سلاح و مهمات وابسته به رژیم صهیونی
🔹
سازمان اطلاعات سپاه استان تهران:
🔹
در ادامه اقدامات هدفمند اطلاعاتی و عملیاتی و اشراف نسبت به مسیرهای انتقال و جابجایی محموله‌های غیرمجاز سلاح و مهمات تعداد ۲۰ عنصر در قالب ۵ شبکه سازمان‌یافته ناامن‌ساز، وابسته به گروهک‌های تروریستی و قاچاقچیان سلاح و مهمات، شناسایی و منهدم شد.
🔹
از این افراد بیش از ۵۰ قبضه انواع سلاح گرم، ۷۰ کیلوگرم مواد منفجره، ۲۰۰۰ فشنگ و مهمات مرتبط کشف و ضبط شد.
🔹
امنیت و آرامش مردم خط قرمز دستگاه‌های امنیتی بوده و هرگونه تهدید علیه ثبات و امنیت کشور با پاسخ فوری و مقتدرانه مواجهه خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/akhbarefori/651943" target="_blank">📅 16:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651942">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmAGpjhOAebSP_UBC4O-Os5LROFr4BljraWk-es-V4mgtUZRpEApP7GPij13ZvGovtbXEBziCe25uZ6gN76lDxOzGyFtyV53bAHh-j89iSax0vUKBI49HcEoc2biTNUfCLpd1YwZp7HLbhF4NDLErGQkbtDY61CfTvAZocutPD3-rz0sDVHaJwz8v0s8uMgLSqJfeDlJGfMNr7UArBZlmfFKVVRQ6tvQtsUMsYSv3IqDb2XtG6SkHDjm8X1ktpliCF6Gd0RWVrx186nnAmLRRDAidh_9qB-qe9j6l9gAVurAF8TTI1eVfELJwP5vM4AUspQSsrcx1oNbiyNc06_USw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: یکی از گزینه‌های ایران در صورت حملهٔ مجدد می‌تواند غنی‌سازی ۹۰ درصد باشد. در مجلس بررسی می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/akhbarefori/651942" target="_blank">📅 16:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651941">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjEzVxNSB7WAFQA3e_ew1aqZo_CZ1zI8arsL7qrWpxVIcfUBekjy7OSXDvYstbKOvJKx9CgaisL_zEJ39gYnlux2anJZ9djkW0xzdOB8-NAEi9dz1fA_i7GM6gtPtVurtfdyDCJMdyW3KuE7qC7sEAqN64lr6dXg--0XpqWQGCSiJPDkUXx8RSjBabqxUbwpUMGDAwKMMl28zpgWJWkXleIRktaCZiINcJMp9ieP2gTVlDHWRQZ50huG8qnbdaF8X9KcliRPrKizrSV74Hc2Ytbexcu6T4fZ1XbES-mHUrWYlP2XD_YgcM9zd30nXckbVcYSDA0UKIjTaMlW3hLqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقام ارشد عراق: ایران در برابر دو ابرقدرت نظامی ایستاد
🔹
معاون نخست‌وزیر منطقه کردستان عراق قباد طالبانی به یک چهره رسانه‌ای انگلیس پیرز مورگان گفت: «ایران، بیشتر از هر زمان دیگری یکپارچه است و مردم، پشت سر حکومتشان هستند.»
🔹
طالبانی در این مصاحبه گفت: «واقعیت این است که ایران در برابر ضربات شدید دو تا از قوی‌ترین ارتش‌ها روی پای خودش ایستاده است. ایران کشوری است که دارای نهادهای مختلف است، نهادهای سیاسی، نهادهای حکومتی، نهادهای مذهبی و البته نهادهای نظامی و شبه نظامی. این نهادها قادر بوده‌اند که در برابر ضربات (و حملات) شدید حدودا دو ماهه (آمریکا و اسرائیل) مقاومت کنند. ما الان با تحول یک دوره آتش‌بس در جنگ مواجه هستیم که جهان می‌خواهد بازگشایی شود تا اقتصاد جهانی امکان بهبود یافتن داشته باشد.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/akhbarefori/651941" target="_blank">📅 16:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651940">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcc97e3f7b.mp4?token=rh-Qa6Nmt3z_Haa6U-fuJALeB-jd0Yr3tMI0KpSC2YRgqEC2g-uEk8DvIER9rMMztTTmkqvf-05pDAXGHd_EBe0jHyZNlMAweAzvvFtVKErm0KqfKzAVUOUMwpE35SvGPLPrj4D_v3aVntC6HsaievCJQY4ZCYdW9e0FJ9f93uj0bby7ySQ6UfhOyC9n8gRxFKGhdmOaRzWtH25MEG7Fl1vxBrC2MdOD_1NC3hoz9YjDzp_xd2gnkrvarCdUuB3ea_GgbpHcfC9B3ARm0WJia8jByaOj2vCuQ13fQOx2DatCHKhrfoz3tJuFJ0t3-8idMwearXjkjxh9lFGsJ8ZO0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcc97e3f7b.mp4?token=rh-Qa6Nmt3z_Haa6U-fuJALeB-jd0Yr3tMI0KpSC2YRgqEC2g-uEk8DvIER9rMMztTTmkqvf-05pDAXGHd_EBe0jHyZNlMAweAzvvFtVKErm0KqfKzAVUOUMwpE35SvGPLPrj4D_v3aVntC6HsaievCJQY4ZCYdW9e0FJ9f93uj0bby7ySQ6UfhOyC9n8gRxFKGhdmOaRzWtH25MEG7Fl1vxBrC2MdOD_1NC3hoz9YjDzp_xd2gnkrvarCdUuB3ea_GgbpHcfC9B3ARm0WJia8jByaOj2vCuQ13fQOx2DatCHKhrfoz3tJuFJ0t3-8idMwearXjkjxh9lFGsJ8ZO0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲۰۰ هزار میلیارد تومان خسارت وارده دشمن به قسمت هایی از خط تولیدها
🔹
مهدی طغیانی، عضو کمیسیون اقتصادی مجلس شورای اسلامی: در دو شهر اصفهان و تهران به جز دو واحد بزرگ تولیدی، بخشی از خسارت های وارد شده به واحدهای تولیدی شامل ۲۰۰ هزار میلیارد تومان می شود. البته این میزان خوداظهاری خود واحدهای تولیدی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/akhbarefori/651940" target="_blank">📅 16:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651939">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGcDlmOzgb8ypZT1ZT9zKStiYJl-grweK3gL95VNLExIZ0XEy_cyTXAYsyaGdsqsgTorGq0_DGlXs9_Y-L_QogXRRow-bUwCnM8NROEs7f5ruwgmI_jmLXtiNypoIxI0I1u3gQoxN67kHsBlzqwz8JXNM9TQ_QbnZQ1TjhXObE22hdoe5z3P4CYjlybgjZ7II0sjgnTxkz5tk7st_dZ7gbWZr52fI4gB_TY3KTarA1l0r1wa11RcuWWtj7uhN5qCARo10aJUzDF3I0trDxf5InOmlndnSeNiTVQDe69yJ4U9pFoPCqpRylXf2NnVmJ-z4Q5ZsFerSreuWB5EIOgl0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش خرقانی فعال فضای مجازی به اظهارات افشین: اینترنت رو به خاطر ترور قطع نکردن، به مردم آدرس غلط ندهید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/akhbarefori/651939" target="_blank">📅 15:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651937">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bF8aLUsPO4_QcargRSXyVmujm8G3dcGl8RNk2yB3R2UvDtNOlKMRA_qRVhgGrNTpSwP5-FmGpw8tUgnLDqkGeF2GbjOM3s6NFgV66ejumnYBMvy-B0jhfIoMuuK4K8XKwqzc4CAx-fXelSx2VG4cr7lQuMEW_F99_wGZkP27ml0PRzdPEgFn1ys0CgystxQDww0gtaOmrX0f2VKv5r4zGYYeBvIrKBU_tWfrOFu_cLQju2rbdAEr84aDAdn_lEAe4L-IJiuDvu8EN6moeVGKr2h5tlHMcQ82sCFqkTPt-c648gXCC_W8vODoa-Nx-jaos_msIZFVz0hIcushGl_6dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خودروهای ایرانی در ۸۰ روز گذشته چند درصد گران شدند؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/akhbarefori/651937" target="_blank">📅 15:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651936">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b42278bbb3.mp4?token=UkbotoXdIexRzJ80nIEdt-N2ctZBzb49TRCwMuNiI0lWGJEr3fZsbTFbWIg9Sv0InAhsRu18VOMb3UWTH9-UxDji_H_FoGUXbFweujpaJMtKdCivauhfcrSAR3p_WKhMUyxnd7de2k4PeDuWoYd6etDcObnFbNzv3cbS03TNitz_nTGLo2bPjCCaf5HJfWXyx-DbR1KooEya5qc8WmhH9_egsU_veI6nqojPfb4sJC4hrN_wqc1bYOdYyScL_3h85_pbEoSy3bBNQ6kmwdue5sLozjUfwr0LuH4MvVSDQdsp7PVHUD0V3n_myph-7dJgZV9U9yRzKK0uULxQjttTFXH6nyMp6glUc9GiAlrBbAmiVfU4oFEHOR-fwvNQAn3HvXfjSShtK-HONtXm11McMWOoKbzmpp_Qsv3_euqadsSOBu0RHFpkwHbtt2ZRrrrJji6BcklbBdag40EvyHwQvZT7lhobQpibN8J7V1dCZ_7IB9PMKAS9anciapWJBOskuT4PoSDBZ9SDaI6gBz5mTfgNo905E_DtqR2doJpxoxjsZvL1HjW1lxT-e339LbdLy0ghoIHgQqV0uCFmbhqStax9xD3lNvvy1V-0YOhu5aL-LY3bm7lcAU1C6GMdBBaOuOvWrz3-uj64YZ9OgJhlnDjCvh7NL-UgrYcv_jTJ2rM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b42278bbb3.mp4?token=UkbotoXdIexRzJ80nIEdt-N2ctZBzb49TRCwMuNiI0lWGJEr3fZsbTFbWIg9Sv0InAhsRu18VOMb3UWTH9-UxDji_H_FoGUXbFweujpaJMtKdCivauhfcrSAR3p_WKhMUyxnd7de2k4PeDuWoYd6etDcObnFbNzv3cbS03TNitz_nTGLo2bPjCCaf5HJfWXyx-DbR1KooEya5qc8WmhH9_egsU_veI6nqojPfb4sJC4hrN_wqc1bYOdYyScL_3h85_pbEoSy3bBNQ6kmwdue5sLozjUfwr0LuH4MvVSDQdsp7PVHUD0V3n_myph-7dJgZV9U9yRzKK0uULxQjttTFXH6nyMp6glUc9GiAlrBbAmiVfU4oFEHOR-fwvNQAn3HvXfjSShtK-HONtXm11McMWOoKbzmpp_Qsv3_euqadsSOBu0RHFpkwHbtt2ZRrrrJji6BcklbBdag40EvyHwQvZT7lhobQpibN8J7V1dCZ_7IB9PMKAS9anciapWJBOskuT4PoSDBZ9SDaI6gBz5mTfgNo905E_DtqR2doJpxoxjsZvL1HjW1lxT-e339LbdLy0ghoIHgQqV0uCFmbhqStax9xD3lNvvy1V-0YOhu5aL-LY3bm7lcAU1C6GMdBBaOuOvWrz3-uj64YZ9OgJhlnDjCvh7NL-UgrYcv_jTJ2rM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعداد واحدهای صنعتی آسیب دیده از حملات دشمن چقدر است؟
🔹
مهدی طغیانی، عضو کمیسیون اقتصادی مجلس شورای اسلامی: نزدیک به ۵۰۰ واحد صنعتی به صورت مستقیم مورد اصابت حملات دشمن قرار گرفته اند که دچار تخریب حدود ۸۰ درصدی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/akhbarefori/651936" target="_blank">📅 15:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651935">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
شکایت ایران از آمریکا به دیوان داوری لاهه
🔹
دولت جمهوری اسلامی ایران با طرح دعوی در دیوان داوری لاهه، از ایالات متحده آمریکا به‌دلیل «تجاوز نظامی به تأسیسات هسته‌ای ایران»، «اعمال تحریم‌های اقتصادی» و «تهدید به توسل به زور» شکایت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/akhbarefori/651935" target="_blank">📅 15:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651934">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78c1650433.mp4?token=dkWTZRmuPlv_eZL05ivW4IduVahUTNWSdihpRS6Sk6WHR07s6XFea8Vqh1MwCnZxT4uRbcehyLJR0YE3Us3Km4E6VAgheZnyuMZh8j_XuB6iiBuCJwXHY-mQq2Ulj9RczB28mJVS-XEo7LF89UEkeai0N0cKcGAhDk6MqFXwx2mz3wM8N5iFdYcQ5rnCtW7_jpBShTL-bQ-HdW4jEUsdbWLtPKA_cTN5qtB0qGw7iPm-_jCPGXZRRE5BZHw02L3H2H-7NwMBxSh4MFjOxsLxFZVWjW-kAwXcW1AMQ5pj59scfeftrphr7SYPVt1eUs22K9p8W9ybS8l9K7FGYayFTnTfWH2hkXS19kDBxHqEgAp00TuMq1eCtTLUlsH2evVvENZWZAzFA0bt9v7xYB7fk5xamgsQoYrKrBnStgEtqJ5-DSlyRXUMLjnI7jHCALXzUj2gKP1lMkHstSJPiuLZKAZRqTzYqsHFOOBlidfbYaYakqcEAmMFFfTRNR_fX-Hk6G7uQlEc0m1IPCShCIgKb7rcuW8BGlt6ARsxKmA8GZNfbl2fPXD6nTfrIMfFEvRxtgb4rO6Xb4ByJjroSDNq2OFyB0mJF6tvDH9NYXwb2av6ka3S-QPvKF6r8ktgCc1BucetTh5ct_-hv_xjPp2DPntLtqdIxm3fElcUxyuLuyE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78c1650433.mp4?token=dkWTZRmuPlv_eZL05ivW4IduVahUTNWSdihpRS6Sk6WHR07s6XFea8Vqh1MwCnZxT4uRbcehyLJR0YE3Us3Km4E6VAgheZnyuMZh8j_XuB6iiBuCJwXHY-mQq2Ulj9RczB28mJVS-XEo7LF89UEkeai0N0cKcGAhDk6MqFXwx2mz3wM8N5iFdYcQ5rnCtW7_jpBShTL-bQ-HdW4jEUsdbWLtPKA_cTN5qtB0qGw7iPm-_jCPGXZRRE5BZHw02L3H2H-7NwMBxSh4MFjOxsLxFZVWjW-kAwXcW1AMQ5pj59scfeftrphr7SYPVt1eUs22K9p8W9ybS8l9K7FGYayFTnTfWH2hkXS19kDBxHqEgAp00TuMq1eCtTLUlsH2evVvENZWZAzFA0bt9v7xYB7fk5xamgsQoYrKrBnStgEtqJ5-DSlyRXUMLjnI7jHCALXzUj2gKP1lMkHstSJPiuLZKAZRqTzYqsHFOOBlidfbYaYakqcEAmMFFfTRNR_fX-Hk6G7uQlEc0m1IPCShCIgKb7rcuW8BGlt6ARsxKmA8GZNfbl2fPXD6nTfrIMfFEvRxtgb4rO6Xb4ByJjroSDNq2OFyB0mJF6tvDH9NYXwb2av6ka3S-QPvKF6r8ktgCc1BucetTh5ct_-hv_xjPp2DPntLtqdIxm3fElcUxyuLuyE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هفتاد و دومین شب حماسه خیابان؛ عهد مردم برای شکست دشمن صهیونی-آمریکایی در جبهه اقتصادی
🔹
ایرانیان متحد دیشب ضمن حمایت از نیروهای مسلح، پیمان بستند با رعایت الگوی مصرف، در کنار کارگران و تولیدکنندگان، چرخ اقتصاد کشور را بچرخانند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/akhbarefori/651934" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651933">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7mWNX9sw7hwX9Cbi32-928JxPFIWKopjHRwXsbTb01rlKRJ18yWEblzow8IQz1Tlt55IJukCa7UqOXmnzPeQ17NcNJLfJ61A-G9GJlzfpO9WYp6mCD58UvZIAbM_x0CdRCjxZ7E8gClYiy_wly3Wz7-gdhv43A5fFnvnZWB35AL2lVC2tq7V2c3foKKoePadLihrZ9FOw63StUHxL5Q9LEqlqi2OowNE540dTb7Vz73SRDysKIqJXy8N_5Jdd96HUuyM8sLbWhqDhhriAaKcqFQ3qaIOziIKFE1AjfOAiHvskuZzSYrAhTbp6JTVYkMhTWVfrF2ZyOQqwljm0zAvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غنی‌سازی ۹۰ درصدی اورانیوم در مجلس بررسی خواهد شد
🔹
سخنگوی كميسيون امنيت ملی مجلس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/akhbarefori/651933" target="_blank">📅 15:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651932">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
معاون امنیتی وزیر کشور: حدود یک میلیون عراقی برای شرکت در مراسم تشییع رهبر شهید انقلاب اسلامی ثبت‌نام کرده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/akhbarefori/651932" target="_blank">📅 15:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651931">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBys-ee2hKNKSBhld6b-4xaoObZAEMvvu7r7-yafZvRsUdd71T8waJP8ZHAl55FHiLlUnDKUtH3aLbn3iEd2_dvgqYGYlIXS0oyU9oz_NedSbDC7BSN5v8WyAPKQP1Z9SBwBn9i3_7XNKL0ROLTyhns6kqYzT-LdiHhpXBw0pW8jnROihls1OAWzUTxNO7KF6Rx8vFMGGx6m6vUojhj9OqFxl7Ul4hasg3T9IMPwrswIxeD6PtV5SYDM88rvvVY-Ov7JzwzIvuUIer-0ITTqIQYO0fTpOrO91wyaRNihsVORE9-BB7IGr5rIE-i-jt8tOQLEaLiFl8uxcVOYjJZqCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درختی که زباله می‌رویاند
🔹
وقتی طبیعت به جای میوه، پلاستیک می‌رویاند، یعنی زمان تغییر رسیده است. هر بطری، هر کیسه، یک زخم بر تنه‌ زمین.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/akhbarefori/651931" target="_blank">📅 15:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651930">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEnc3IYd82k5xjoAE3M2AI-8dmPJ3x1ofX6LBAo97AAQPVrGH0uXD0ZiF-sRGrE4UZq4RcRTNmRldxKP2_jErsBk44xVd8DXFwab0H4WWcNcTAuvTimHLssZwT3pzbp35Vg1fALkhED9x-U-1BKlNzYZML-kpKX5CqD5hjYpOw0qdBzZ0i7g8hdXe7NAAhF2sxwnyE4H0cbT86gw4O8_Rz4v0L9T-4hpZnIxBRjYDYisZqr172F-bRQamR_fjt0SikukZYOxvRKtGkBge-g59Q3rJBrfiOFqWpkn08fNCh6Xf_sMtSPjx5-RpdwP1G2R_bqM2DBLmjNqisZBnJsrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برگزاری رزمایش قائد شهید سپاه حضرت محمد رسول الله تهران بزرگ
🔹
به گفته فرمانده سپاه محمد رسول الله تهران بزرگ در این رزمایش همه سناریوهای از پیش تمرین شده، تاکتیک‌ها و تکنیک‌های تیمی و فردی در مقابل دشمن تمرین شد و مورد ارزیابی قرار گرفت.
🔹
سردار «حسن حسن‌زاده» تاکید کرد: ارتقای توان رزمی برای مقابله با هرگونه تحرک دشمن آمریکایی - صهیونی، از اهداف و سناریوهای اجرای شده این رزمایش بود که با موفقیت انجام شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/akhbarefori/651930" target="_blank">📅 15:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651929">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
آرامش ۱۰۰ ساعته در تنگه هرمز؛ تردد شناورها زیر نظر سپاه ادامه دارد
🔹
از برقراری آرامش در تنگه هرمز حدود یکصد ساعت می‌گذرد. در این چهار روز درگیری گزارش نشده است.
🔹
نیروی دریایی سپاه با اقتدار امنیت آبراه را تأمین می‌کند. تردد شناورهای دارای مجوز ادامه دارد.
🔹
سازمان بنادر نیز به کشتی‌های متوقف شده در خلیج فارس خدمات می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/akhbarefori/651929" target="_blank">📅 15:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651928">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95bc07926d.mp4?token=EwHfm6FuVHZj1tXa2EF1qRxWTfsv6giaI_cIV50OSLE3jEAzKLITcdVCrJA5kpOLpOxjL8rxIVIZTeuXrynYH8GKgtwIHaSfrtlo0YnMmAsJPyCyHfZZMxDzmMbz3xlGarmpc-U68cJWQs4SD1Pc7IdFTyZcQhEqSmVmAEQu9NKekh1lul7nk8oDYt2NV9JVnl5ezrsS1qT8oRLKdYbJ9HENFqYpuI6nov2KqJEdTIV36APWHNtLAFiIcqCHatrXtREe3Gh89rNdXfBdklG_nSp99ON31BQMOQVYILCM0aJURvEcd_hKV4sOF-kFVqnM61QDHV5E_AmO4orxuON2kn7pt9Kcj13yHrStmZfgCy0EqRR9g-qvS-rZSMgpRtEJ-TOijW1P2I19OPyj8R4Uvnd_XFU812cHI16cc1pv1mzD4BlhMoxSBvcawx16c3adsawNQmheWgg9q-JCTputgX53x6GRFeNBzqpbaeW9OEk6GFUteDUOfd1mGZa_nyf40qifuefdvZSiIQxDM3a1WhBvvOSueFFSJiPdmgyBZBXWSFEm_S1sAQClUGmN0KFN54nEvJiRUUZLCFmhnhUaRawaTCo2808CgMQ3hKWSFdwtZP281dE9fi0Et22sZBN8d4gvXXTBcDqfa1jujqFKLBhkagIeuXFaabZGuQ1F1b0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95bc07926d.mp4?token=EwHfm6FuVHZj1tXa2EF1qRxWTfsv6giaI_cIV50OSLE3jEAzKLITcdVCrJA5kpOLpOxjL8rxIVIZTeuXrynYH8GKgtwIHaSfrtlo0YnMmAsJPyCyHfZZMxDzmMbz3xlGarmpc-U68cJWQs4SD1Pc7IdFTyZcQhEqSmVmAEQu9NKekh1lul7nk8oDYt2NV9JVnl5ezrsS1qT8oRLKdYbJ9HENFqYpuI6nov2KqJEdTIV36APWHNtLAFiIcqCHatrXtREe3Gh89rNdXfBdklG_nSp99ON31BQMOQVYILCM0aJURvEcd_hKV4sOF-kFVqnM61QDHV5E_AmO4orxuON2kn7pt9Kcj13yHrStmZfgCy0EqRR9g-qvS-rZSMgpRtEJ-TOijW1P2I19OPyj8R4Uvnd_XFU812cHI16cc1pv1mzD4BlhMoxSBvcawx16c3adsawNQmheWgg9q-JCTputgX53x6GRFeNBzqpbaeW9OEk6GFUteDUOfd1mGZa_nyf40qifuefdvZSiIQxDM3a1WhBvvOSueFFSJiPdmgyBZBXWSFEm_S1sAQClUGmN0KFN54nEvJiRUUZLCFmhnhUaRawaTCo2808CgMQ3hKWSFdwtZP281dE9fi0Et22sZBN8d4gvXXTBcDqfa1jujqFKLBhkagIeuXFaabZGuQ1F1b0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گلی گم کرده‌ام می‌جویم او را
🔹
ماجرای تشخیص پیکرهای تکه تکه شدن کودکان میناب توسط مادرانشان
🔹
مستندساز مدرسه میناب: برایم عجیب بود، مادری که بچه‌اش را از دست داده بود در مقابل دشمنان این مملکت مقتدرانه رجز می‌خواند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/akhbarefori/651928" target="_blank">📅 14:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651927">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZcQzvAUXqqvRFEh3H_pqWWw29vKG2GB1emmGAJp1tM2hvwB44aedxnQsjr9yTCTgP7BxjN8_6ZfvbuM4QVwERcds64h07SYmici9sXtHbSXsxxBwr0wKmwRBhtzW2xb7syJt2cOWzbjhgaUVzHUYefYnWzuEFi7_E03g9rVNZOyCbvWJnYCBirwl-TTKAxPEa-uIxc21c5TCMGWeuEhoOedQyZ-Z-RssBSW4xhwWQQoAT-56jKJ2PtLbNOFC-6k1ZBWCwlY4STbz5Wq89hCSR4aU6-qa2SZV0wc4fb1Hxw-pPg50jS4EyuhKB3m04fxpjNWrhuJekByNGAbUZhRFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسرائیل به دنبال سامانه‌های جدیدی برای مقابله با پهپادهای حزب‌الله
🔹
رادیوی ارتش اسرائیل گزارش داد که ارتش این رژیم با الهام از جنگ روسیه و اوکراین، شروع به وارد کردن سامانه‌های جدیدی کرده است که هدف آن‌ها مقابله با پهپادهای حزب‌الله است.
🔹
به گفته این رسانه، این سامانه‌ها بر پایه سیم‌های خاردار چرخشی طراحی شده‌اند که برای قطع کردن کابل‌های فیبر نوری به کار می‌روند؛ همان کابل‌هایی که در هدایت برخی از پهپادهای حزب‌الله استفاده می‌شود.
🔹
رادیوی ارتش اسرائیل همچنین افزود که همزمان ده‌ها هزار گلوله ترکشی برای توزیع میان نیروهای اسرائیلی در لبنان وارد شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/akhbarefori/651927" target="_blank">📅 14:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651926">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
تنگه هرمز محور تماس تلفنی «روبیو» با همتایان انگلیسی و استرالیایی
🔹
«مارکو روبیو» وزیر امورخارجه ایالات متحده در تماس تلفنی با همتایان بریتانیایی و استرالیایی در مورد موضوع ایران و تنگه هرمز گفت‌وگو کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/akhbarefori/651926" target="_blank">📅 14:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651925">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8dc45ad6.mp4?token=rDSCnYM8dTujUkyvNr3mQslX3BQe61u5_yeTCXWJMiWQQPn6Btoc8DTT8xqz8tiMBHfj7bqQkvaTRR-NZU_f0m8GqMlRQOvqfrb59m6w1oHCjhmllrulGPKtMmmLiP3h2cmobZn6Bmn05OyNdEmyVCgU9vUj1Vc8gIjU9DX8InN0jFry3FyGP_kUdLpOL1oVxOUXzTGgxT1kl77S5BZpBs-gBbqbTcikPJlA9ZtECYkCcfMDZQ_Zehb-has1p1bgYawp33_58O4C9r1LJa7drC7oqbDKudrmpw40-I2xk1Spa0wshxZlJQWQWILhaBkB4e0VxjhQqZYtATeRthxijw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8dc45ad6.mp4?token=rDSCnYM8dTujUkyvNr3mQslX3BQe61u5_yeTCXWJMiWQQPn6Btoc8DTT8xqz8tiMBHfj7bqQkvaTRR-NZU_f0m8GqMlRQOvqfrb59m6w1oHCjhmllrulGPKtMmmLiP3h2cmobZn6Bmn05OyNdEmyVCgU9vUj1Vc8gIjU9DX8InN0jFry3FyGP_kUdLpOL1oVxOUXzTGgxT1kl77S5BZpBs-gBbqbTcikPJlA9ZtECYkCcfMDZQ_Zehb-has1p1bgYawp33_58O4C9r1LJa7drC7oqbDKudrmpw40-I2xk1Spa0wshxZlJQWQWILhaBkB4e0VxjhQqZYtATeRthxijw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش صهیونیستی مدعی رهگیری یک پهپاد در جنوب سرزمین‌های اشغالی شد
🔹
ارتش صهیونیستی: برای اولین‌بار از آغاز آتش‌بس یک پهپاد را در ایلات رهگیری کردیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/akhbarefori/651925" target="_blank">📅 14:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651924">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSrui0eJX3Mi6u-J4_XZGx3bB8_1nV5m4GnWtcTdu_LFZqeXo42uf20cpHDcJYuNmAMWVO136qzjoSDpQ2STOd79G0MtRL86HKFGqR-vRHt6Gm25MdOI5Cq9Y0fsmmKhX3B0PZu_6rlFXMOpp7tG0u4p2dLcSYx-iDnkxhkreb3v6WgeMJ3E5iEEipt_3oASjER4-JsWnr68i-aow_mxcOFTD15EpNmO30-uaWiT4i8ynOT0qlPbqKXRcd0GZkiU1DlXeKnKMCQaWgn0XbS97LufzI-H1CA20vOBD6ydb_YBw_nrXIZbNHiqNNjs-Xz2zTOyGKBzSRvayUvtN8ev5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترس، شکست، خستگی: برداشت اسرائیلی‌ها از آخرین مصاحبه نتانیاهو
🔹
چهره‌های رسانه‌ای اسرائیلی، نتانیاهو را در آخرین مصاحبه خود، فردی خسته، نگران و شکست‌خورده توصیف کرده‌اند. این موضوع، در کنار اعتراف صریح او به شکست در تمام اهداف جنگی، به چشم می‌خورد.
🔹
نخست‌وزیر رژیم صهیونیستی در آخرین مصاحبه با شبکه سی‌بی‌اس آمریکا، اعتراف کرد که اسرائیل به هیچ‌کدام از اهداف جنگی خود نرسیده است. اهدافی که شامل نابودی توان موشکی و برنامه هسته‌ای ایران بود. همچنین باید هدف اصلی یعنی براندازی و تجزیه ایران را هم به آن اضافه کرد.
🔹
باراک راوید، در خصوص این مصاحبه به نقل از یوسی ورتر، نوشت: «نتانیاهو حتی از پشت لایه‌های گریم هم خسته و رنگ‌پریده به نظر می‌رسید. چشمانش بیرون زده بود و انگار کیسه‌های سنگینی زیر آن‌ها آویزان بود. او ضعیف صحبت می‌کرد، بدون آن پرحرفی‌های همیشگی‌اش؛ حتی وقتی سعی می‌کرد قدرت و تکبر را به نمایش بگذارد، بیشتر شکست و خستگی را منتقل می‌کرد.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/akhbarefori/651924" target="_blank">📅 14:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651923">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i816bLfGPc7zd0dIU6w7OtqZ1HqpSs6iHsFHt--CFF5zLhQ66DoXKp_y6Iwc7ZnKWpzh0YFl16G4WEB1TRvYGl4wfGpSrPX-EPrEtAu9fVMYA_DOGHoTymdAFoHD8PH8N26L-VmJNRDecD5jBJ5bj_6B7kvxBgS5JRlpPBUzrZDQMIGEISQQaLE4c_wstFMkbAXGuNrO5AYGT0j8NO3KMW9bVrsTNgPVJs2UTuhsxN3sKOE_fCjcpqMTfWisLrdNl_8wCwUiibsXfLcN7FTZQVt1TfiVVkn2Zq4p_JxOQ1p0KiYG_drE3HWISfbgWHUhzWzOHaTcX4kE73JyIZC3qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقف تعهدات درمانی بازنشستگان به ۱۰۰ میلیون تومان رسید
🔹
رئیس کانون عالی بازنشستگان تأمین اجتماعی از گسترش پوشش بیمه تکمیلی، افزایش سقف تعهدات درمانی و ادامه پیگیری‌ها برای تحقق درمان رایگان خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/akhbarefori/651923" target="_blank">📅 14:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651922">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEK16incyEQU9_mEL-ivA1xv6QO18m7uJ6wRbgx1lKbZ10GUaevROhOFrN1yN8Tb1fKKb4Vqg9jZ13m-qNUK1L8rdatiIepdjsFYnIy7w5xJfFhtpKKVz0fAHO2MXkwpL0WAPw6mbu-yXkxoSzFB2Hg9zQrrG3yaUr0ZMxdVmAA_lbJuhUzSJcvJpVSsj-BV_Xb-GFf5zqZDd9DRZPKJHDJrC_NnqFv663GfXEMgkgS5a_A-2vVYCpqZdcO4IoDxQCpoeiGOZ2cxGz9_8kT9eb1-lnsGAkP1_KmCQ7j3Lff9my6ugvIXcLjpIhQ2Cx4sLDgBCvfV3D9hdRCV7PqTfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر کیلوگرم گوشت مرغ ۳۸۰ تا ۴۰۰ هزار تومان به فروش می‌رسد
🔹
پایش بازار نشان می‌دهد اگرچه قیمت‌ اقلام بالا است اما کمبودی در بازار کالاهای اساسی مشاهده نمی‌شود
🔹
قیمت تخم‌مرغ در هفته سوم اردیبهشت ماه بین ۵۴۰ تا ۵۸۰ هزار تومان در هر شانه دو کیلوگرمی متغیر است
🔹
قیمت گوشت مرغ بدون بسته‌بندی در این هفته روند افزایشی داشته و هر کیلوگرم گوشت مرغ بین ۳۸۰ تا ۴۰۰ هزار تومان بسته به کیفیت گوشت تولیدی به فروش می‌رسد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/akhbarefori/651922" target="_blank">📅 14:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651921">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rX0lKgq1WIRNKeQC38NgzF3CYgy2pg9ZKn2d9_Sw9KtO_s3cidKxxUYLVTD08OwTuWLp6iHpzHIC8BIR0b5RexFtX7ES4H7cvv6ntYcGVsCUuhSmeOmUQXel5Y-ZvGZhTr44bwXv2G00pP8khZOmdu3AsBPPEMT7mx8kTotwD_9zcJM04o9wa0x1hr5vt9MXYRlCvbrk9B5xw3my1OYSzavjthmvLo8EQU5IBqgRwjuzR3CIPPSUW-b-iIihXagyHrjkEOSQkB5RBUDQYQvedx0-bYksQVL1cuS_maETp-RWRImasTrAfAiP2NfjkfdQU4gOy66iS1Gas49QilB5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دروغ بزرگ بحرین و افشای نقش واقعی آن در حمله به ایران
🔹
بحرین که تا دیروز خود را بی‌طرف و صرفاً هماهنگ‌کننده دفاعی در جریان حمله اخیر آمریکا و اسرائیل به ایران معرفی می‌کرد، حالا با انبوهی از اسناد نظامی و گزارش‌های غربی روبروست که او را به عنوان قلب تپنده عملیات جنگی آمریکا و اسرائیل علیه ایران معرفی می‌کنند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/akhbarefori/651921" target="_blank">📅 13:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651920">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8e8642e67.mp4?token=munvAKd-SZtTmWYYu0psCPa9FS-ksWN4BvbFLQ96chRfKBX_5IJ3Q8qMdu48DBe-16CehfTZ8tYqOvB1Bc5hy-ry7ITmaUDlgQygmzE1DqBgYIpjfpY4a1UztV1jIkYYp59FckoqCjIcFt26kEofPc4K7oB_0g1DOicC1U_aWtSYNRxG3UjT4yEOdB2ciHLJGKsssJAOFIfiNy6OJcKlbW4ooZgaopO-aBQfPH_uaZx2HyySDnmKyY_UDVI8tVzvSsPfSB_aqZ5bC7825mGbRO9qw89Udlh5nRZGj7iLOAYJEnHGUYoNHXFTE-qKdWqgMbyTnvn-Gc8cKTAAfIhPFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8e8642e67.mp4?token=munvAKd-SZtTmWYYu0psCPa9FS-ksWN4BvbFLQ96chRfKBX_5IJ3Q8qMdu48DBe-16CehfTZ8tYqOvB1Bc5hy-ry7ITmaUDlgQygmzE1DqBgYIpjfpY4a1UztV1jIkYYp59FckoqCjIcFt26kEofPc4K7oB_0g1DOicC1U_aWtSYNRxG3UjT4yEOdB2ciHLJGKsssJAOFIfiNy6OJcKlbW4ooZgaopO-aBQfPH_uaZx2HyySDnmKyY_UDVI8tVzvSsPfSB_aqZ5bC7825mGbRO9qw89Udlh5nRZGj7iLOAYJEnHGUYoNHXFTE-qKdWqgMbyTnvn-Gc8cKTAAfIhPFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس جمهور: دولت اجازه نخواهد داد عده‌ای با سوء استفاده از شرایط جنگی معیشت مردم را هدف قرار دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/akhbarefori/651920" target="_blank">📅 13:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651919">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oa-CZiPmz-y33jY8ytYG2zzTa6PY6rdVbitR-36AJ5rkKwyS_vqOECEhYTlEKfpA4LaecuGIHR9iitac2v99_YCqr-RHSq-EJrGhhQWKpxEBzMF3EdSTI873Z8179RjVculmT2sxrN6ofV1UNDVJ2qkSdB5-D84e-t3Z41B2Dg38QbvMyMMjrhrC4VPn0_Dp1gg57zJS6oxJFeZMpqKBhxTODqEyNFjdbt_gyRg5aVGVWaZDLxwUEFdLEpV7eZsZizTOcZ19SwHL1BYRj2zP6kbJaEjd93bU5q8HGpy2Uow6908XiZ3EIev13Fki8qnKF6NrAAXZUlPuDF-xBlPxQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توری که امارات برای ۲ بانک ایرانی پهن کرد
🔹
وابستگی ارزی و تجاری ایران به امارات به نقطهٔ حساسی رسیده و به گفتهٔ خاندوزی، وزیر اسبق اقتصاد، امارات با استفاده از شرکت‌های پوششی، صرافی‌ها و حتی شعب بانک‌های ملی و صادرات به مرکز اطلاعات مالی ایران تبدیل شده است.
🔹
وزیر خزانه‌داری آمریکا نیز اعلام کرده است کشورهای خلیج فارس اطلاعات مالی ایران را در اختیار واشنگتن گذاشته‌اند.
🔹
خاندوزی به بازداشت مقام بانکی ایران و محدودسازی حساب‌های درهمی اشاره کرد که برای فشار ارزی انجام شده بود.
🔹
اکنون با وجود اینکه بیشتر کالاهای وارداتی فقط از مسیر امارات عبور می‌کنند، نیمی از تسویهٔ تجارت ایران در این کشور انجام می‌شود.
🔹
کارشناسان علت این وابستگی را عادت تجار و سود ناشی از ارز چندنرخی می‌دانند و پیشنهاد می‌کنند ایران از مسیرهای جایگزین لجستیکی و شبکه‌های مالی چین، عمان، ترکیه و تهاتر استفاده کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/akhbarefori/651919" target="_blank">📅 13:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651918">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLudRp9EhhGstw4asvkCRSo1bWQ4SIGpzraSRNRyee3eBuQxK4snmu3TpFCknjNgNww50G1hFTx3DHt18P3xgoCN9Y3tRMwIEhjDysJtzZzqjzubWr3IJ8rdaamCGHnLx6NKQmYy1yVr9S018T4FySsO6bcktlW40WycbMGx-4ap_nyu2-cey37_0sPGSLj_p1I6VMcfwCcGvvkD93z5WBqVjmNEv_czuJMBNuR8abqUK9nGTYCc6F05hR1e8lAKZHfCWC18QRciCarvXmUMvPpOUugROefm7cq_HcLVQw-mfMBjIemShPP8S4WdoZUrA6KpOkToLGnoDlS9vp_UQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت صمت تأمین نشدن قطعات سایپا توسط کروز را تایید کرد
🔹
مفتح، قائم‌مقام وزیر صمت: زنجیرۀ تامین قطعات وابسته به شرکت ایران‌خودرو، باید براساس قراردادی که با سایپا دارد قطعات این خودروسازی را تامین کند، اما این موضوع انجام نشده است.
🔹
از بهمن پارسال هزاران خودروی کوئیک، اطلس و شاهین به‌دلیل عدم تامین قطعه در پارکینگ‌های سایپا مانده و قابل تحویل به مشتریان نیست. تعداد این خودروها آن قدر زیاد است که خودروساز دیگر جایی برای نگهداری آنها ندارد.
🔹
بخش زیادی از این قطعات به گفتۀ مسئولان سایپا قبلا توسط شرکت قطعه‌سازی کروز که حالا مدیریت ایران‌خودرو را برعهده دارد تامین می‌شد.
🔹
وزیر صمت پیگیر ماجراست و در صورت اجرا نشدن قراردادها از طریق مراجع قضایی عمل می‌کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/akhbarefori/651918" target="_blank">📅 13:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651917">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
واگذاری ۴۵۰۰ کودک بی‌سرپرست به خانواده‌ها طی جنگ
🔹
مدیرکل دفتر امور کودکان و نوجوانان سازمان بهزیستی کشور: تا پیش از آغاز جنگ، در مجموع حدود ۵۰۰ کودک در کشور در قالب طرح میزبان به خانواده‌ها سپرده شده بودند.
🔹
طی جنگ، بیش از ۴۰۰۰ کودک از میان حدود۱۰ هزار کودکِ مراکز شبانه‌روزی بهزیستی، وارد محیط خانواده شدند.
🔹
۱۲ شیرخوارگاه در ایام جنگ خالی از کودکان شد.
🔹
در ۳۰ روز ابتدایی جنگ، حدود ۸۱ مرکز بهزیستی به مکان‌های امن منتقل شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/akhbarefori/651917" target="_blank">📅 13:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651916">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLlW8vzemsQ7mhe8Vl_RNgoVn1ENWHMFSRZmdr_R-WwLF650edsTzZs-ZzBbmYF32lwVuOPDQHYGBDT1ktCuD5TzIkavXFBu4mSNgLlS51d0KVvAYvLI2kSIqdCiPhCjRm_IMOdivA5TPnlz-Wq8ZWybjClyhjK_6hQLlNTQ3cIA4IV7lHPMJRN8NmlhghA30HiKeKDfuyuZ-8npYLPO3Ucbtrm3Zv7RGAx5iy8NRArM76uSZ_6N3XSP9Kihip_-CiHXItX19U149xOXs-8A9mI613FpDrO89l3g-Bq1yeS2VTVa0aQHMW2rBaPie6KIqsYV6mfKaYT7dky_z7raGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیخ نعیم قاسم: با تجهیزات اندک مقابل گروهی وحشی و مجهز ایستادیم
🔹
پیام دبیرکل حزب الله: گفتند کار شما تمام است و شکست خواهید خورد! اما جهاد شما به اسطوره‌ای از پایداری تبدیل شده که جهان را شگفت‌زده کرد. از کجا آمده‌اید؟ چگونه خود را آماده کرده‌اید؟ تعداد شما چقدر است که پایانی ندارد؟
🔹
ریسمان شما تا آسمان امتداد دارد و پروردگارتان پاداشی بی‌پایان به شما عطا می‌کند. شما فرزندان پاک جنوبِ و دارای شرافت هستید و لبنانِ مستقل و دارای حاکمیت مورد حمایت جنوب است و انسانیت در آزادسازی جنوب تجلی می‌یابد.
🔹
ما با دشمن جنایتکار و وحشی «اسرائیلی» مقابله می‌کنیم که مورد حمایت مستبد خونریز آمریکایی است.
🔹
امروز جمعیتی زیاد با نیرویی عظیم و وحشیگری وحشتناک در مقابل گروهی کوچک، با تعداد، تجهیزات و حامیان اندک قرار گرفته است. اما این گروه کوچک پشتیبانش خداست و درنتیجه ما پیروز خواهیم شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/akhbarefori/651916" target="_blank">📅 12:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651915">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
دبیرکل حزب‌الله: هرگز تسلیم نخواهیم شد
🔹
ما با تجاوز اسرائیلی-آمریکایی روبه‌رو هستیم که می‌خواهد کشورمان لبنان را تسلیم کند تا بخشی از «اسرائیل بزرگ» باشد اما ما هرگز سر خم نخواهیم کرد و تسلیم نخواهیم شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/akhbarefori/651915" target="_blank">📅 12:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651913">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9rxYGJRhuG9bowtWihI8vBCKRiiok8X2_TV2wrrLoavqvZmVUvODLb8X4q4Be9n9NR0SmX5W3c1znghj5rBnAKdAYOiqNj8trnS5OADXC7PR7TYj2t230zYxVcOiVA_UDTTTOJFEF-2HC3DqDg-kGLEAj9z0035SToivV9ux5yNM__Gpy-rF3jbl7wDyKNsvMJyrc1kxu77E82_XlzGlHTpgVZo8iCzzhhiTOdd2gqTf60l29D5n4rco7WuD-gqGdUGEpbkDpQxx3N0HaxlMhSICNHxY75ed8NrCuTGtOunBCsE6fSb5wNjuOAti_6ZAY0eT0n82dChx5Ok8Zrtlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیخ نعیم قاسم: پهپادهای حزب الله اشغالگران اسرائیلی را خفه می‌کند
🔹
دبیرکل حزب‌الله لبنان در پیامی به فرماندهان و رزمندگان مقاومت اسلامی : پهپادهای شما زمین را در برگرفته و اشغالگران اسرائیلی را خفه می‌کنند.
🔹
پهپادهای شما، اشرار و ظالمان زمین را به وحشت می‌اندازد، موشک‌های شما زندگی آنها را متزلزل می‌کند و آنها را دچار اضطراب و بحران‌های روانی می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/akhbarefori/651913" target="_blank">📅 12:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651912">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upEHr19Qo3Z_oew2MYC560RZy5IyX8DR9IbH8AeRUbKSBPiyoHRqWwQkdvI6heAZh4Nt-XnlhDibYItvUyByW-IIIR4fiuFJmu9MdV6y89AGze9bkmCMGcBoM3MWo8kjweHcuwCUS7Qq0zOa6bMJI3D87P7akrG_ejwm1tkV5Wfp40uwYvTdMw3XCLRl8klXmufXphmRtQibfT33wVj1ZNMnk4YswjKa-TTru-m9bSzyqbAKX1mcvtjjQTorjAXirzOCFLe3haVeybccnPb2fJlQMZhRnCGNWrv07AlylEyLFeLyiT2QKdzKEI-tCVeVYlVxV58BNPJB3uXD8xjLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلوند، پرشور و ساختگی | طرفداران ترامپ که توسط هوش مصنوعی تولید شده‌اند
🔹
در آستانه انتخابات میان‌دوره‌ای آمریکا، موجی از تصاویر و ویدئوهای تولیدشده با هوش مصنوعی در شبکه‌های اجتماعی به چشم می‌خورد که زنانی جوان، بلوند و جذاب را در حال حمایت پرشور از دونالد ترامپ نشان می‌دهد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3214392</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/akhbarefori/651912" target="_blank">📅 12:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651911">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCYmoAhZCTIw07MllJ2cEHJlkdxAbCaeXPYEITAV0oGibQD1fcF5aCOX-v8MC8NzH1fiTL0YG-R7xclnFzKRWEpRXDWUzKKLWWfP1Q6gzsnaGFdu5K08D6ZM3vPcLHDFaizF4iFEU3fyzR8Kr0jORfAnxhKPAegBa_Eapn2ZoHo58XtwTqP12gD2XCQwY20cR2JVn8jM2XsXwz_hr132aA8fAgi3ir_CeP098KwPfxRYnDjvVyXybAVoYTApTUbzBN0SYctSLfDi10zSIM-QzXMckSJZTMOsuLPg_AdktQTaY1soKPNBavDDimqgq2WPso-lv15T_3DgmYKFEGFhpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابعاد تازه از آزار جنسی اسرای فلسطینی‌ به روایت خبرنگار ارشد آمریکایی
🔹
یک نویسنده آمریکایی در تحقیقات گسترده‌ای ابعاد تازه‌ای از شکنجه و آزار جنسی فلسطینی‌ها در زندان‌ها و همچنین از سوی شهرک‌نشینان فاش کرد.
🔹
نیکولاس کریستوف در مقاله خود در روزنامه نیویورک تایمز نوشت با ۱۴ فلسطینی گفت‌وگو کرده که تأکید داشته‌اند در جریان بازداشت توسط نیروهای اسرائیلی یا شهرک‌نشینان مورد تعرض جنسی قرار گرفته‌اند. او همچنین با وکلا، فعالان امدادی، بازجویان و اعضای خانواده قربانیان مصاحبه کرده تا برخی روایت‌ها را راستی‌آزمایی کند.
🔹
در میان شدیدترین روایت‌ها، شهادت خبرنگار فلسطینی سامی الساعی قرار دارد که در سال ۲۰۲۴ بازداشت شده است. او می‌گوید نگهبانان زندان او را برهنه کرده، مورد ضرب‌وشتم قرار داده و با ابزارهای مختلف و همراه با تمسخر و تحقیر به او تعرض کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/akhbarefori/651911" target="_blank">📅 12:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651910">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5P7QTkW_LTdOCFp0IyFnT4dueJ9jA6pJIPtO1reHXOvK9A-7JIclVEt38WfkFJXFHlXuuLbs1M9OMVYiw8nG2FSrfbPfYn6Co3xXpES7O5OGE1_0vP1bU_ccIQ2T3Vm1FlT4gpVSRTz9S38cEz7sglo8j7erKdZJCVEmU4tDtCXyPnosDBVjYhWplaoLqCDXJZGPjonU3B7RgvRMsHpZGJ87L9o8IyWRb2qnsCZlhhONH1J75WHRP0mND5TITx57c585_Z6IvEqoGOBqG0KH40BqsqiCgqacllH6uGtnTb8XmXWar9ZJcW8ayrQzlDqtk4devekx0JlHwWKqUmjVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لشکر «جان‌فدا برای ایران» از ۳۱ میلیون و ۵۰۰ هزار نفر فراتر رفت
🔹
تاکنون بیش از ۳۱ میلیون و ۵۰۴ هزار نفر از هموطنان با ثبت‌نام در پویش ملی «جان‌فدا» آمادگی خود را برای دفاع از تمامیت ارضی کشور در برابر تهدیدات دشمن آمریکایی- صهیونیستی اعلام کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/akhbarefori/651910" target="_blank">📅 12:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651909">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
سخنگوی دولت: دولت علاقه‌مند است تا هر چقدر مقدور باشد رقم کالابرگ را افزایش دهد؛ این موضوع همچنان در دست بررسی است؛ چنانچه به نتیجه برسد اعلام خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/akhbarefori/651909" target="_blank">📅 11:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651908">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXCWF0XVCj4eGrm4MiTLNLI-CnfgQYSSTllLjMkZP6gga-BJpYIpiwpDCE9zpuBX0wDP9qjKn57hkCziuYUUgIsY1YU1sqE-lz40_7Oqjysjz9mgAwAFs3HqaK7P6RfyfkoQ-zHb_GiQrEKnu5V1X-TcO7h6ZWYOKUyi2eSvAILVnREEWxAyBh5vBboeQhJav8x2YMIauBeR-_xj-sanL0DB-Clgw0jwwM6_E4RRws4aUken3dZOViwMNkrIdEbo8ZhVqdDm0YLCz_mH_bOctoj-VmAz6xkGZA9VXDnsV7Dx6xEo6hR9Y20jpZEfAKuj60Fl-jmDLT0KYjREamk5Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمین، قربانی مصرف ما
🔹
نجات زمین را از همین امروز و از انتخاب‌های ساده شروع کنیم  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/akhbarefori/651908" target="_blank">📅 11:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651905">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XaVI3IYNn8Z3X7zGE0RmOdm8pg8bX8EE11d1gsGWvS9XNeZIgFj13AHuBMs-L-2Y_cbHH7asI4sk-iUYd6MLwKhGOqijbro5UaTle-VpByW6EVFIbPd0MW__88IRy1kvYU-o03fn_OkvtqPPWpM9sygO9Eeaxt1rVGgc1ilF5PEFGiUDYL2Kg-KwHTcb6veQA6t5ajakERs7Dv04ZUWmNiNzSbO4J-T4Y2Ud5t3Ofq25noF56MeWDE8cc7NrQeJnjJNV1q58V9fJIgNP9A8fDoY0QWOce79RnVNJgwtgokwzIpec7jBo0nTC1_JDL-XJp7oHM-v8oFYm7sufOiROnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pRcfL5Lgrb1TdSihT0MfY9peZv7FeiQwDFpai7_xpWdFpwAooU7bpMbnKgw5i740uFbO7DfbZe02w7xeP-lMdoTXz_vaKJbCRHZ_gHNNmAgsHCyS80u1rkbMgKomdDNvodKqrGMCOXR0J5JN7DwfMobwx7MW6PRzBTuowDkpQbraSDybKfSpeys5rmgWmpfrHNkd28Vq4hKQV6ogXHEgN_pHPQ_zxFu1FJyBPtbtMsmGERwXD8MHOC2qQ9jlwFJUxwW_RlQ1v7Mw5yYLul_hkJ4JuQcd0ptVInDxXiI6b-Iy0i3zTvD10E9KlWaHglp9JNAVkXGqV9MdxziSuSzc7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33c24605de.mp4?token=t7N4VeR5DcmgiyzNWxn8xZF4LOid5s0nQ_ZIaHg7aH1fMwefpy3uvTcNAoF5RIJ2xOg1DO_bCLaUPpAFmDSpIYdqetkbQAezCAuOSa7yGZSfgMOvntFWRpNCufvhesY6l63ldu2ujIPRjsUjU3Jq_Rovy2DkmSJLHzXHaz1YdUUbXRm7KHJ6uEIkxjP6txzY2caSilqmmFl73TCqxLkrP7pFjqxy76MgngrL4TBEAL5OdRqJbt7N9g4xHTK7NkDPBRkppOBuCx-J9uG7CipT0fq84eq1LW00BFw863B7Zw4PWYFsfJx5p87549jUxJptlwJXiNnAFQIeCGGvs9ePow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33c24605de.mp4?token=t7N4VeR5DcmgiyzNWxn8xZF4LOid5s0nQ_ZIaHg7aH1fMwefpy3uvTcNAoF5RIJ2xOg1DO_bCLaUPpAFmDSpIYdqetkbQAezCAuOSa7yGZSfgMOvntFWRpNCufvhesY6l63ldu2ujIPRjsUjU3Jq_Rovy2DkmSJLHzXHaz1YdUUbXRm7KHJ6uEIkxjP6txzY2caSilqmmFl73TCqxLkrP7pFjqxy76MgngrL4TBEAL5OdRqJbt7N9g4xHTK7NkDPBRkppOBuCx-J9uG7CipT0fq84eq1LW00BFw863B7Zw4PWYFsfJx5p87549jUxJptlwJXiNnAFQIeCGGvs9ePow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر املاک توقیف‌شده خبرنگار اینترنشنال منتشر شد
🔹
مستندات املاک شناسایی‌شده فیروزه جابانی خبرنگار رسانه صهیونیستی فارسی‌زبان اینترنشنال که با دستور قضایی به نفع مردم توقیف شده است، منتشر شد.
🔹
مرکز رسانه قوه قضاییه: برخی افرادی که در همکاری با دولت‌های متخاصم موجبات ایجاد خسارات گسترده‌ای به کشور شده بودند با انجام اقداماتی سعی در اختفای املاک خود داشتند که با کار پیچیده حقوقی و اطلاعاتی و تلاش‎های سازمان ثبت اسناد و املاک کشور، در حال شناسایی است.
🔹
یکی از این خائنان به وطن که با حضور در شبکه اسرائیلی ایران‌اینترنشنال، در راستای اهداف دشمن صهیونی در تجاوز به کشور نقش فعال داشته ، فیروزه جابانی است.
🔹
با پیگیری‌ها و استعلامات صورت‌گرفته، دو واحد از یک آپارتمان درحال ساخت متعلق به خبرنگار اینترنشنال که تلاش برای اخفای آن کرده بود، شناسایی و به دستور قضایی به نفع مردم توقیف شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/akhbarefori/651905" target="_blank">📅 11:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651904">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34e4e31ae6.mp4?token=tdrPaJPZ5uPQ7OjUrCuCSkagmYnf2h2_IRPgBFJ1N9wwHWp6JKbDessnYuNqbr8MSD_W4YY5HAGG8WZDJ77lizfIevtccpi4UNq00I85NqfWAgfP-YDJmn7HuYVfRxTO2jc7twrzpgj3M9pwdsEHES5ScMDOa5W1vu_Dz_wnDvTM8LskGiswl39GO7ruRlIjEVmbkqn7eOSYyc3L6FkRrjzlN48vmmO1Ntk6HOe7L6y5tXswqO7nh-grUL7u_uAe_HOlVfurtXF5-5iMl9qEfdvBanWnZ55EwkOef2mblL1izbuK6IeGAv7IcmfB3-t7-KrjmqJp0Ya5Lo9EdqUc8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34e4e31ae6.mp4?token=tdrPaJPZ5uPQ7OjUrCuCSkagmYnf2h2_IRPgBFJ1N9wwHWp6JKbDessnYuNqbr8MSD_W4YY5HAGG8WZDJ77lizfIevtccpi4UNq00I85NqfWAgfP-YDJmn7HuYVfRxTO2jc7twrzpgj3M9pwdsEHES5ScMDOa5W1vu_Dz_wnDvTM8LskGiswl39GO7ruRlIjEVmbkqn7eOSYyc3L6FkRrjzlN48vmmO1Ntk6HOe7L6y5tXswqO7nh-grUL7u_uAe_HOlVfurtXF5-5iMl9qEfdvBanWnZ55EwkOef2mblL1izbuK6IeGAv7IcmfB3-t7-KrjmqJp0Ya5Lo9EdqUc8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احتمال انتقال سهمیه سوخت به کارت بانکی؛ مجلس دولت را مکلف کرد
🔹
نواز سخنگوی صنف جایگاه‌داران سوخت: انتقال سهمیه کار به کارت بانکی بارها مصوب شده و امسال نیز مجلس دولت را مکلف به اجرای آن کرده است. امید می‌رود این طرح بزودی اجرایی شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/akhbarefori/651904" target="_blank">📅 11:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651903">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsCz4KipmZ6I0sAkeAp5qhLG1EzsDqoHAgTGO0doZvxASwBJNnvp6ccd-EgqNX6L39-eZc0bxkxZ5AE4JjyiDVMkm8FA-zZzFj5z4dq8VoRoT5BL929dzCCQZVVKHdjLCeOvQAVqUWhvYD5KzJFbsSxatl1404v7LCWbGLJ361IzHnvHE7VLYCSnOMOxQGB0yjjLAVM1t0ZpE2xgde7-8ORVikPA1FwRQ_MNPK8DnD7QWSrZxnKfICGVqs9lKdmkdV6UTyeQnm7e3S6ZFvct3S25jDUFcGXtShZtbuMiDgYxsLhsjF2TY7PKiWTEfKCZgLDG1lAMX7XSFK6rT2Ef_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«ماندن به وقت جنگ»؛ روایتی از ۴۰ روز ایستادگی کادر سلامت در جزیره خارگ
🔹
در روز‌هایی که جزیره خارگ زیر شدیدترین حملات جنگ ۴۰ روزه تحمیلی قرار داشت و بسیاری از خانواده‌ها برای حفظ جان خود جزیره را ترک می‌کردند، نیرو‌های بهداشت و درمان همچنان در کنار مردم ماندند تا آرامش و خدمات درمانی قطع نشود.
🔹
«فهیمه زمانی» سرپرست مرکز با وجود فرزندان ۶ و ۸ ساله خارگ را که از بچگی در آن بزرگ شده بود را ترک نکرد، «زهرا کشوریان» بهیار مرکز با دو کودک خردسال یک و سه ساله روز که اول جنگ آنها را به بیرون از جزیره فرستاد و «سیروس حقیقی فرد» از کارکنان حراست مرکز که حدود ۳ ماه بود فرزند تازه متولد شده اش را ندیده بود، تصمیم گرفتند محل خدمتشان را ترک نکنند و در روز‌های جنگ در کنار مردم جزیره بمانند.
🔹
شب‌های بمباران، اضطراب مردم و ماندن در جزیره.
🔹
بهیار مرکز: کودکان خردسالم را همان روز اول جنگ به خارج از جزیره فرستادم.
🔹
نیروی حراست مرکز: فرزند پنج‌ماهه‌ام را سه ماه ندیدم؛ اما خارک را ترک نکردم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/651903" target="_blank">📅 11:40 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651902">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6254b500db.mp4?token=Uy4PZ3xujuSFQoZP0wYE-ddk7DMvXVftq_o7gxJyV3feE4Cb5wylfjpGm5MXBxbN4BymmEFpiDcHszR3VYt9v3mARkPFyL9i3AsnjP0A2eglzpSqlWjz4zkJMnMEcA5bmdvmJsFmaHr8v1f7jtkGo5POqKaCq1sgfcSNBOxCkKeuxSER4ZVnumxU_NF0zvOSj7dH-rSS_Bz5VOsmzTgwKv42klVz34fq279h2hhzuQ6MZMlmIghprGi6pZbRmMux45NOB8i_9RB0rPSloYbSwDO5WnV9dvNP6nYqCsh_9pIqLsZiD3OyNbgqre-6-1BJYwN1R90Hj1YBcTlHf1rVtkAhIptQZnIbykODyioO3_gitm8xnRp2yZ73nESXK1vFmv8G3oxcI7xGZbjZUC7w2wOF925DSGs_-IzA_odrW2XhCmKQVNX_7AgZhCyogNCvRyDKPXtV0gA5hr6oOB2FMYOoJJQX91Ik6PQwYJQXWZV6x3MvgzsQvkXRVFAz_WuJtiAcPksfJf7gLV_Fs-o08Em8lcGXa0RSXBTDkSkxQwzltUub3Gj4AhZ9KxQfMsEVZD6XJCEoAyQZ8YKykV3__r8pRsNQv9Ue3nW5xP0RF-ivhSzJXJDaSGN3AvJwWIVK4J9vCmQ8Y0plGGK6YuYab_lqbXPJ6XMoBzgy6KbRX4M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6254b500db.mp4?token=Uy4PZ3xujuSFQoZP0wYE-ddk7DMvXVftq_o7gxJyV3feE4Cb5wylfjpGm5MXBxbN4BymmEFpiDcHszR3VYt9v3mARkPFyL9i3AsnjP0A2eglzpSqlWjz4zkJMnMEcA5bmdvmJsFmaHr8v1f7jtkGo5POqKaCq1sgfcSNBOxCkKeuxSER4ZVnumxU_NF0zvOSj7dH-rSS_Bz5VOsmzTgwKv42klVz34fq279h2hhzuQ6MZMlmIghprGi6pZbRmMux45NOB8i_9RB0rPSloYbSwDO5WnV9dvNP6nYqCsh_9pIqLsZiD3OyNbgqre-6-1BJYwN1R90Hj1YBcTlHf1rVtkAhIptQZnIbykODyioO3_gitm8xnRp2yZ73nESXK1vFmv8G3oxcI7xGZbjZUC7w2wOF925DSGs_-IzA_odrW2XhCmKQVNX_7AgZhCyogNCvRyDKPXtV0gA5hr6oOB2FMYOoJJQX91Ik6PQwYJQXWZV6x3MvgzsQvkXRVFAz_WuJtiAcPksfJf7gLV_Fs-o08Em8lcGXa0RSXBTDkSkxQwzltUub3Gj4AhZ9KxQfMsEVZD6XJCEoAyQZ8YKykV3__r8pRsNQv9Ue3nW5xP0RF-ivhSzJXJDaSGN3AvJwWIVK4J9vCmQ8Y0plGGK6YuYab_lqbXPJ6XMoBzgy6KbRX4M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: دشمن در سال ۱۴۰۴ بیش از ۱۰ هزار ایرانی را به شهادت رساند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/akhbarefori/651902" target="_blank">📅 11:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651900">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe01028607.mp4?token=tt0D-gCADxchKAQ8FFAEvu5Oo23Dcdn3GlYBG5NLQTSUgN6cvm51NS45cXjv_moCVRS8MbcrnBDOjlwMhdFWoaE6Kxf2vWS-PuEqW3SqhPuiI1_7oiCuVKuzBeVexC4uXweJ5jYMhEIdHCUnL0S1aB_u8OhDPVuaAY4kcenCPkW8WYrLxaA7-3cD56TFp84HUMKILmqhJ_TjtFBCKCVyCJwGnc1wsQfp5d1nUiI90L0c5_sPkG30Oa1cKIPjPvclrF1ofvo7cVF3OGbCoX0z93SlC-PaaakuNCc4v24mrSfo96x_JRrSNLR_VfDhS_8EM6Vb_2wfcfhHGTC_W8mCFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe01028607.mp4?token=tt0D-gCADxchKAQ8FFAEvu5Oo23Dcdn3GlYBG5NLQTSUgN6cvm51NS45cXjv_moCVRS8MbcrnBDOjlwMhdFWoaE6Kxf2vWS-PuEqW3SqhPuiI1_7oiCuVKuzBeVexC4uXweJ5jYMhEIdHCUnL0S1aB_u8OhDPVuaAY4kcenCPkW8WYrLxaA7-3cD56TFp84HUMKILmqhJ_TjtFBCKCVyCJwGnc1wsQfp5d1nUiI90L0c5_sPkG30Oa1cKIPjPvclrF1ofvo7cVF3OGbCoX0z93SlC-PaaakuNCc4v24mrSfo96x_JRrSNLR_VfDhS_8EM6Vb_2wfcfhHGTC_W8mCFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهاجرانی: فشار اقتصادی ناشی از تحریم‌ها حق مردم را ضایع کرده است
🔹
سخنگوی دولت: فشارهای اقتصادی ناشی از تحریم‌ها بر مردم تأثیر منفی گذاشته و دولت در تلاش است با پرداخت کالا برگ، افزایش حقوق‌ها و حمایت از تولید، وضعیت را بهبود بخشد. بیکاری یکی از عوامل اصلی افزایش تورم است و حفظ اشتغال پایدار ضروری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/akhbarefori/651900" target="_blank">📅 11:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651899">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHMCyLE-sLZknGc6WbHNoRDikzvXKwXAjuNJxyuKhGrB7VRbbv4KcrnvIfQI4uS-zFFbXL26IsuMS_T0keA09a8HXObzs8tTzzwfnamvRP6HhiCGwGTf2OLqcwUXh_LyQJgM2AIfLvMzHp-2k5ukjO8ykIylhnqCyj4UVsCrlSFO-ISDnpU0YBcLRFG-_Q3euDUEpVsjGbDQSiCaxalrypbFH7nfLcfThLvzEDwS4UxBuQi8Afmi1G3o6rkt5OCMaCpxmaolLxjn-NJSNVb7mWoMx1Lf2GX2lU2fHVCZt4H1dDEg-1ITyVumcfWVb-WAFHjSjDulHdrY5tJYxp_HFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعایی درباره ساخت یک پایگاه توسط اسرائیل در عراق!
وال‌استریت‌ژورنال:
🔹
اسرائیل پیش از جنگ، با اطلاع آمریکا، پایگاهی مخفی در عراق برای پشتیبانی از عملیات علیه ایران ایجاد کرده بود؛ پایگاهی که پس از شناسایی توسط نیروهای عراقی، هدف حملات هوایی اسرائیل قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/akhbarefori/651899" target="_blank">📅 11:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651898">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsA8-hrfUr8C7XXZIevRd9IWvP_39kObBQ7ucvKo99_3d3WUbT6wLwO_KaIS3Qpy18XFyGwnlqpcXPDpXKMKMM73nBQ3lnLn_d1GY4Wm2adeTGlCcOzVx0zdMKjlp4MKqvsMFilCs1CmMPVqfEo-xoZHWMYaVSJ3PF15T2SA03PAhFTo2TNIxr27SDjB7vIQw65VLPTdT9n8gcVpqhya995BFJE6800WTPdV1r_yQP6FLHM0ThiOtMyz0eUTbNHpDCoYUAaHyfXND2tywsviL7v8G34A-28IfsNq0i-ocOT9khRkBGU-p6FCV-uYw3MS8bM6aDABA4x0yLjrs71p3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در ایام جنگ مردم بیشتر چه چیزی می‌خریدند؟
🔹
آمار یک فروشگاه اینترنتی نشان می‌دهد با نزدیک شدن تنش‌های جنگی، تعداد سفارش‌ها و ارزش سبد خرید افزایش یافته است.
🔹
تقاضا برای کالاهای ماندگار مثل آب معدنی، روغن و کنسرو بالا رفته و فروش تنقلات کاهش یافته؛ در عین حال فروش شمع ۸۶٪، کبریت ۳۹٪ و باتری ۲۶٪ رشد داشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/akhbarefori/651898" target="_blank">📅 11:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651897">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1GqwQmbBdLeL5hh12XXcGE3Z8KEfddgESRF2YOu-CPPxg5IBqR1O8690DE5VSNCkRLw_G8J9QUFCUPmtw9XVE_UutmzYC58u4_nm6eM3d0OVgDZS3bNrlmJQS6_H7D4Q3WATz9Ow01ysptXMdHhJUg0x_pfQHmthi1kyvZT7-A7fU5fveUgfd-h5k-r3tK6Su767kKMWTvcVj2vxHXu31lK1vi0iQZol5jQ0_j69FDJ00lC8yRAvDu7-mVYNhQYVwNdUM0Q5Zdzxmoa_d7ggYeYY1UrIe1witDw18w7egPGXkSIo1mZtQAH3VidMRTv_CLyFIXVUEfHt_XXxotX1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رپیس جمهور: اجازه سوءاستفاده از شرایط جنگی و فشار بر معیشت مردم را نمی دهیم
🔹
پزشکیان  در نشست بررسی الگوی مشارکت اصناف در فرآیند تولید، توزیع و تنظیم بازار: کنترل تقاضای القایی و مدیریت مصرف از سیاست‌های اساسی دولت است. صادرات ارزآور و دیپلماسی اقتصادی، به منظور تقویت تاب‌آوری اقتصاد کشور با جدیت پیگیری شود. یکی از سیاست‌های اساسی دولت در شرایط فعلی «کنترل مصرف و جلوگیری از شکل‌گیری تقاضای القایی و کاذب» است. ایجاد تقاضای غیرواقعی بدون تأمین متناسب کالا، منجر به نارضایتی عمومی و برهم‌خوردن تعادل بازار خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/akhbarefori/651897" target="_blank">📅 11:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651896">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f65082375b.mp4?token=KuVcA29l5M69oEDgFnkwJDNdkPzcR9xgsWhbUF8fC4AsbMagZp_KlBLikOG082VZ2Xb8omFhZXSthvV9QiXsdo6kyx5WlRRZA0XNq76C1eESNOk50q5SH33GcAP63h6xNqiIm990Vd9747iXJ9xuyRxBxvBDNtlqntV1AglYR2gi-f_YSTSkm_l9bSHxWtTcELGSxs5sIiuUBT_xgpgnUaUJo5gWdf_aeW2GYIES0la8cIP5ovXTTPysNZL9F2FE6gXf1fLzBjLK8uG6EnnSA8-g0LnozShoj2qMclzOYYje3Y2ScPnbY8d84xzRndTi9ynPBjYTStZFE2gVNVzDXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f65082375b.mp4?token=KuVcA29l5M69oEDgFnkwJDNdkPzcR9xgsWhbUF8fC4AsbMagZp_KlBLikOG082VZ2Xb8omFhZXSthvV9QiXsdo6kyx5WlRRZA0XNq76C1eESNOk50q5SH33GcAP63h6xNqiIm990Vd9747iXJ9xuyRxBxvBDNtlqntV1AglYR2gi-f_YSTSkm_l9bSHxWtTcELGSxs5sIiuUBT_xgpgnUaUJo5gWdf_aeW2GYIES0la8cIP5ovXTTPysNZL9F2FE6gXf1fLzBjLK8uG6EnnSA8-g0LnozShoj2qMclzOYYje3Y2ScPnbY8d84xzRndTi9ynPBjYTStZFE2gVNVzDXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهاجرانی: اعتراضات دی ماه حق مردم بود، اما تروریست‌ها آن را مصادره کردند
🔹
سخنگوی دولت با تأکید بر حقانیت اعتراضات دی ماه مردم، گفت: متأسفانه این اعتراضات توسط تروریست‌ها مصادره شد و منجر به شهادت بیش از ۳۰۰۰ نفر از هموطنانمان شد.
🔹
دولت در راستای حفظ سلامت مردم و رفع مشکلات اقتصادی، تصمیمات جدی از جمله حذف ارز ترجیحی را اتخاذ کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/akhbarefori/651896" target="_blank">📅 11:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651895">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGgchA9rT9w-8sWIjMJxfyBdVSiUj1OF1dHgs3lPQrDt2KhT9rsoIMhboQoFcaezLEIp3t7czLY6lDvqyif3aXYZiVWwYDI1Qux31-rRA4UuIAWjiy8Y4Y8hru11oO8X40PRiHg5XTMVlFiVkNUQRRAOD1EoyTisfmU8U99YSlLER3S001XRZMEjcpmj6CCqvABeYVtwG4ejJRpL7gBW-fO2ZUX1-k1wLaYgJwT1rQOz_c-4xaR-pJdfXnrv4vZO1zwChqjWvJh8B1sTlTnqbsKXuohb6-8boTTtMo_t-jjvQeCm9FrgjctoEKcXGntd99LZDJLIOIS_kh293w9X3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
متوسل شدن ارتش اسرائیل به تورهای ماهیگیری برای مقابله با پهپادهای حزب‌الله!
🔹
روزنامه عبری هاآرتص اعلام کرد که ارتش رژیم اشغالگر برای حفاظت از نظامیان خود در برابر پهپادهای مقاومت لبنان، به ابزارهای ابتدایی مانند تورهای ماهیگیری متوسل شده است؛ آن هم در شرایطی که از پیدا کردن راه‌حل‌های فناورانه ناتوان مانده است.
🔹
یک مقام ارشد در ساختار ذخیره نیروهای زمینی در مصاحبه با این روزنامه گفته است که به‌دلیل سیاست‌های نتانیاهو و ترامپ، «ارتش دست‌بسته مانده است» و در حال حاضر فعالیت موجود تنها به تخریب روستاها توسط پیمانکاران خصوصی محدود شده است. این مقام نظامی نسبت به کمبود شدید شمار سربازان و افسران هشدار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/akhbarefori/651895" target="_blank">📅 11:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651894">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3valQuxlodIyFX2fJ8y7RTDXj-38gCBVCJXROwCFWSCprv1PuLFJJgTQtINIUYxpSSOsiaj6dXaIld2NtQsIAyaWlICezTFduDBUMg4nYlqlnOy0IQdOXok2rIWP2HgIr5-9FHtE9kimcs8kWS-IxftG1vDxIvEIXSrcNeHpa3anHvZcRNdYO1QVJBuQWgknIa-fwY1a41kwAIFyO1VCjgqCO3RqhPzm0bfadoDc2Qxi87lp6U0K7Q3K7UuUmpzSQpop5YcjOwdnqfMUtagXJvPALSFK-l87GTn1-1eZxob4FUbBMOvSMF7FMlOrL4_h44kFMXacHjf1UWhxhSBJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خارج شدن موضوع هسته‌ای از اولویت مذاکرات ایران و آمریکا
🔹
در شرایطی که در گذشته، تلاش آمریکا برای محدود کردن برنامه هسته‌ای ایران اولویت مذاکرات بود، سفیر پاکستان اعلام کرد که بازگشایی تنگه هرمز مهمترین موضوع مذاکرات کنونی با تهران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/651894" target="_blank">📅 11:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651893">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVzAsAn9rCZOL1XE-94MPrnl7-OkL7zZ0SxUmqkBgpOfmAKvW0bTt5uorJYO4hpTZQrlEvui15qAdSlcfwvZOTD3cv5XOk4Uqse5uyBnbL6_BwvPHdKkIK0_WFpGU5OR0E53uZWze410P9AX3lo9HJZVaZukTwCNtEnomDTGMbpmiAfFUYh08ByLHySyVQPTf0JZyINELwuhfDUeG2RwTC9Yfv0pKsufXW3z88XhfUo8XEVe8Iti7XbLKEfyCVp3_vQRwfMj7uA9RbVxDHLLsYlGWt02_l7FOyj94vr1yk6VGu0qut_Cal3HcANFz6Nh7P6BpxgFR6Zy89ggJwfaWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارسال پیامک‌های تهدیدآمیز منتسب به ایران به شهروندان اسرائیلی
🔹
منابع اسرائیلی از یک حمله سایبری گسترده به اسرائیل، شامل ارسال پیامک‌های تهدید آمیز از سوی ایران، به شهروندان اراضی اشغالی خبر دادند.
🔹
طبق تصاویری که از این پیام در شبکه‌های اجتماعی منتشر شده است، در این پیامک آمده، «به شما قول داده بودیم که به زودی ستاره‌هایی را در آسمان شب خواهید دید که ستاره نیستند... به زودی خورشید را در آسمان شب خواهید دید، اما...» کاربران معتقدند که خورشید در آسمان شب اشاره به حملات موشکی و پهپادی ایران دارد.
🔹
براساس این گزارش، سازمان ملی سایبر اعلام کرده که در ساعات اخیر یک «حمله ادراکی» (جنگ روانی) گسترده شامل پیامک‌های تهدیدآمیز را شناسایی کرده است که تنها یک هدف دارند: برهم زدن آرامش روانی جمعی و ایجاد حس تعقیب دیجیتال. در تهران ظاهراً فکر می‌کنند اکنون زمان مناسبی برای برقراری یک رابطه نزدیک با شهروندان اسرائیلی است، حتی اگر این رابطه بر پایه تهدیدهای کلی باشد که از سیستم‌های ارسال انبوه فرستاده شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/akhbarefori/651893" target="_blank">📅 11:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651892">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6672cf69a8.mp4?token=lqLI1sezxdW-WA9ilvSpfvmj1SOmZ-IPVusb9Mh7EfjO5qEB9wrzqbmF86z-9zUiANffIOMA0hjxkoQ9bWlhbvayl5zrswcD7bQl9HWC0AgnedwpQlqO7fRfS-VOMcJMHqW11MdlM4L0_U2SwH9ata62tMYXuj2Ig5jFABF8OI0zyPVKAgOHvQK9NySFapQqdgfZJwkJYDExtS3WgdG9QQFhtq08vi0j7u21aiboEIp7wlyRADSGleWx9WEKtS3PXcXGhEnQFGfDA9s8vdO1MXqoN-5axWO2X_YTv3CkO03BeHN75_2Pw4hIylKb2Xsg4aT7KJfrt8x0QLFCWc3lgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6672cf69a8.mp4?token=lqLI1sezxdW-WA9ilvSpfvmj1SOmZ-IPVusb9Mh7EfjO5qEB9wrzqbmF86z-9zUiANffIOMA0hjxkoQ9bWlhbvayl5zrswcD7bQl9HWC0AgnedwpQlqO7fRfS-VOMcJMHqW11MdlM4L0_U2SwH9ata62tMYXuj2Ig5jFABF8OI0zyPVKAgOHvQK9NySFapQqdgfZJwkJYDExtS3WgdG9QQFhtq08vi0j7u21aiboEIp7wlyRADSGleWx9WEKtS3PXcXGhEnQFGfDA9s8vdO1MXqoN-5axWO2X_YTv3CkO03BeHN75_2Pw4hIylKb2Xsg4aT7KJfrt8x0QLFCWc3lgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: گزارش‌ گرانی ها به دقت به مسئولان می‌رسد
🔹
مهاجرانی در نشست خبری: افزایش قیمت‌ها در دو سطح بررسی می‌شود: کلان و خرد. دولت به دنبال کنترل تورم و مهار رشد نقدینگی است. گزارش‌ها به دقت به مسئولان می‌رسد و سیاست‌های حمایتی برای مدیریت معیشت مردم اجرا می‌شود. همچنین، توجه به تفکیک گرانی از گران‌فروشی و استفاده از نگاه‌های ارشادی مورد تأکید است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/akhbarefori/651892" target="_blank">📅 11:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651891">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سردار ‌جعفری؛ فرمانده قرارگاه بقیه الله (عج): تصمیم نظام در این شرایط حساس، همان پیش‌شرط‌های اساسی ۵‌گانه برای ورود به هر نوع مذاکره احتمالی است. یعنی تا زمانی که جنگ در همه جبهه‌ها پایان نیافته، تحریم‌ها برداشته نشده، پول‌های بلوکه‌شده آزاد نگشته، خسارت‌های ناشی از جنگ جبران نشده و حق حاکمیت ایران بر تنگه هرمز به رسمیت شناخته نشده باشد، هیچ مذاکره دیگری در کار نیست. این مطالبه مردم از تیم مذاکره‌کننده و پیام ملت ایران به دولت آمریکاست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/akhbarefori/651891" target="_blank">📅 11:01 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651890">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3875703205.mp4?token=ZW_WwHV5LgGgzmpa664wM20QdRGkOGvLJD7BewJchkmC1jpbNdXP7hsII_k_zaPbzsIpY4-r8cjyynY39hilrQqE6M1OeS1Xvwzz6nU1XUR2BAsincyJOU2ORTPIjYSKyyZxVa8wryYbec4nOcwofa_EjlQL6GfXoiD6e-ZGya3wNhU5eOcxuVy1-7V30Ta5FueqMzKlWx-ON2L1M1Ugu_8eWs99srqZ09-layIR9bemrBYQL73MNRVaCxyFmPKN_aPaWNztmiDR_jo9xj3xSZelArRzKw7vhJEJFOa3MmjDnE9fllVwZV72I_ukr2ginNv7Ey-eFvyTiw78iJ4Kqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3875703205.mp4?token=ZW_WwHV5LgGgzmpa664wM20QdRGkOGvLJD7BewJchkmC1jpbNdXP7hsII_k_zaPbzsIpY4-r8cjyynY39hilrQqE6M1OeS1Xvwzz6nU1XUR2BAsincyJOU2ORTPIjYSKyyZxVa8wryYbec4nOcwofa_EjlQL6GfXoiD6e-ZGya3wNhU5eOcxuVy1-7V30Ta5FueqMzKlWx-ON2L1M1Ugu_8eWs99srqZ09-layIR9bemrBYQL73MNRVaCxyFmPKN_aPaWNztmiDR_jo9xj3xSZelArRzKw7vhJEJFOa3MmjDnE9fllVwZV72I_ukr2ginNv7Ey-eFvyTiw78iJ4Kqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: انسجام ملی با پاسخگویی دولت و رفع حس تبعیض تقویت می‌شود
🔹
از مردم که بیش از ۷۵ شب خیابان را زنده و پر نگه داشتند قدردانی می‌کنم؛ این حضور امروز به یکی از اضلاع قدرت کشور در مذاکرات تبدیل شده و باید به‌عنوان شکل نوینی از مشارکت مورد توجه قرار گیرد.
🔹
برای حفظ انسجام ملی، دولت باید عملکرد مناسب و پاسخگو داشته باشد و به‌ویژه در حوزه معیشت، حفظ اشتغال و ثبات اقتصادی برنامه‌ریزی و پیگیری کند.
🔹
جلوگیری از شکل‌گیری حس تبعیض، تقویت نظارت مردمی از طریق سامانه «فؤاد»، به رسمیت شناختن احزاب و گفت‌وگو با نسل‌های مختلف نیز از محورهای مهم استمرار همبستگی ملی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/akhbarefori/651890" target="_blank">📅 11:01 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651889">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f77d4cec5.mp4?token=SYW-90RW-UNXd_O_6uuqTskwyEYxZg9w_adT1tZL9FKKSAMg_tupJ7sA6RqOfRG8Vbnm7L5L92skMWWu4yK_2QrveTb8mglLjWC2KIaOcUFLn9j6mQ7vePNbkx-3aBg4ACwaiBBGzCyEXoWx3llOYlZ0FJkOjpc95bq1hG9VUtPZZJ0ur7CN-HSBVy5qc4bVCNcIOCaxv5qKQdkOaYyvte1RdPzx7NFdtcPsBQ7yZmQkygnvdvs2ygubw_6j20A3dXu5zNtw1n0lBX1bxZzzUKxQcijDYTNi3YZt0Oi4rNOkNbcudth46-kMq5CFneFqG3sy5K3S2k_wuIj8f1lRrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f77d4cec5.mp4?token=SYW-90RW-UNXd_O_6uuqTskwyEYxZg9w_adT1tZL9FKKSAMg_tupJ7sA6RqOfRG8Vbnm7L5L92skMWWu4yK_2QrveTb8mglLjWC2KIaOcUFLn9j6mQ7vePNbkx-3aBg4ACwaiBBGzCyEXoWx3llOYlZ0FJkOjpc95bq1hG9VUtPZZJ0ur7CN-HSBVy5qc4bVCNcIOCaxv5qKQdkOaYyvte1RdPzx7NFdtcPsBQ7yZmQkygnvdvs2ygubw_6j20A3dXu5zNtw1n0lBX1bxZzzUKxQcijDYTNi3YZt0Oi4rNOkNbcudth46-kMq5CFneFqG3sy5K3S2k_wuIj8f1lRrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: کشور در جنگ است؛ بپذیریم که ویژگی جنگ امنیت مردم است
🔹
طبیعتاً رئیس‌جمهور، رئیس شعام هستند. بدیهی است که امضای ایشان برای همه ما معنادار دارد. تأکید می‌کنم که پیگیر حقوق مردم هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/akhbarefori/651889" target="_blank">📅 10:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651888">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/014db93225.mp4?token=viil-08vPRK2yhAbLbRSkkaYwFs21ezMKJ_PF3goFB3ImH7HR_MMQMe-3si4lg1ySG7YYuKBkMffKccNrzplMpMPK1xncBYLvQtALd1M3n2cljSNEL5mbpO89xHA-jRAeKXmb9GSVc-cRW_-trZXDO1oL9pp9EbzKV9DcoUjzyeVCpYycKOnfk1tosoEs2WqBHX9MJRSpIyL-5LxB3ihQUyktMJPkG-xGJM3woTSUYLiy-RHNEMjQa7QfAtZfeQbHDa_I9Xc4S95qdRwtGY33e8pnqDBdkS01fLLj1jtDa5YK8s_axYqzEgOYoOL-4Wk53QfGqinmh6ypL-Fd9C-xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/014db93225.mp4?token=viil-08vPRK2yhAbLbRSkkaYwFs21ezMKJ_PF3goFB3ImH7HR_MMQMe-3si4lg1ySG7YYuKBkMffKccNrzplMpMPK1xncBYLvQtALd1M3n2cljSNEL5mbpO89xHA-jRAeKXmb9GSVc-cRW_-trZXDO1oL9pp9EbzKV9DcoUjzyeVCpYycKOnfk1tosoEs2WqBHX9MJRSpIyL-5LxB3ihQUyktMJPkG-xGJM3woTSUYLiy-RHNEMjQa7QfAtZfeQbHDa_I9Xc4S95qdRwtGY33e8pnqDBdkS01fLLj1jtDa5YK8s_axYqzEgOYoOL-4Wk53QfGqinmh6ypL-Fd9C-xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: پس از دور شدن سایه جنگ وضعیت اینترنت به تدریج به حالت عادی تغییر می کند
🔹
اینترنت پرو مصوبه شورای عالی امنیت ملی را دارد که آقای رئیس‌جمهور رئیس آن هستند
🔹
آقای رئیس‌جمهور پیگیر حقوق مردم هستند و طبیعتاً پس از رفع مشکلات و پس از دور شدن سایه جنگ از کشورمان، وضعیت به تدریج به حالت عادی تغییر خواهد یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/akhbarefori/651888" target="_blank">📅 10:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651887">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2lnRMQ89xPRV7rXUe_2wPaKgaQUZeAkEc-NN9W3puAQRSjFG7kKCtWN4hxhpZpNOAzI8t9R9hdmQLSIAhyOhCAGfcjahYkWR7mrizm_RugMeEOnYvciQRpDDC0hoz3_0hb7Bawk211ZP5544Ni2a32uyzwIGiq4AGrqA06QnRtorYJQq94zFJk0vJ2uZMQ6WU911iFefx__BUWrQEKX5Eo-7fpTHQBZx-B1CiXLkBClTM4UgVEtmnQ1ISKkQ72Revs48LL_FjCqvCFd3-evvTK5yXKoAOzpfuxuM9mFQa_RMfmMioUctyxKIJMUBcvX0DWRvp3UPQ33Wq-YBTTmag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس قوه قضاییه: اگر خط سفید و اینترنت پرو موضوع درستی است آن را تبیین کنیم؛ اگر تخلف است برخورد قانونی شود
🔹
حجت‌الاسلام والمسلمین محسنی اژه‌ای: ما در قوه قضاییه پاسدار حقوق عامه مردم هستیم و به هیچ وجه، اجازه نخواهیم داد این احساس در مردم ایجاد شود که در جامعه ما، تبعیض حکمفرماست.
🔹
قضیه‌ی موسوم به خط‌های سفید و اینترنت‌پرو، در ذهن مردم مسئله ایجاد کرده است؛ این ذهنیت نیز یک شبه بوجود نیامده و اگر در باب آن برای مردم شفاف‌سازی نکنیم، موجبات بدبینی شهروندان فراهم می‌شود.
🔹
بارها اعلام کرده‌ایم که کسی تصور نکند چون شرایط جنگی است و اقتضائات خاصی حکمفرماست، می‌توان قانون را دور زد و یا عملی مغایر با قانون و شرع مرتکب شد و یا سوء‌استفاده‌ای از شرایط موجود کرد
🔹
در همین قضیه‌ی موسوم به خط‌های سفید و اینترنت‌پرو، گزارش‌هایی واصل می‌شود که فلان فرد با دریافت مبالغی هنگفت این خط یا خطوط را واگذار کرده است! توجه کنید که این قبیل مسائل بعضاً به حاکمیت نسبت داده می‌شود و سبب بدبینی، بی‌اعتمادی و شکل‌گیری احساس تبعیض در مردم می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/akhbarefori/651887" target="_blank">📅 10:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651886">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
معاون نیروی دریایی سپاه: تحرکات را با دقت زیرنظر داریم
🔹
در یکی از موارد اخیر، یک ناوچه آمریکایی قصد عبور از محدودهٔ تنگهٔ هرمز را داشت که با رصد دقیق نیروهای مسلح مواجه شد و پس از مشاهدهٔ برخی رفتارهای تحریک‌آمیز، نیروی دریایی ارتش با شلیک‌های هشداردهنده و هدفمند، پیام لازم را منتقل کرد و این شناور نیز بلافاصله مسیر خود را تغییر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/akhbarefori/651886" target="_blank">📅 10:43 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
