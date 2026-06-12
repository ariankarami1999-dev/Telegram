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
<img src="https://cdn4.telesco.pe/file/lSx-xf32UMaYSPbSiP7rp5ogxtjNhgbRJknQtAdDXoW_PtxTgkVLmAJoVNHdAV5XfAM1oyVl1G2gWkd-9D7fTPADOOjkbPTySYjmiUYUFIY_4xniW5-xwKN9pFpmQFhfKPCioBOk_wNlz2ALQpzl7fimU9-L1zqyB7R9OaXOZDRcrh_hRHh_DO8yW45p2hLNrAxw7K3F-kZaPl050GyNpV60DNiYe7OavJk4A9zYVzBlt4FzfhzbsRyW6PvT8TDygmtTP30ocgVagm1OIeCvF7xhI1AES-BUkXIdfWE8T1kz6PucMRw_1W7gaz1fCSrDhJPQ_Q3bu9IOu6wm6wBkFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.61K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 20:15:04</div>
<hr>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">📢
جدیدترین قابلیت‌های
ربات وگا
را معرفی می‌کنیم:
🔗
قابلیت AI Agnet در گروه
🔸️
ادمین باید از پنل استارت ربات در گروه به بخش تنظیمات برود و قابلیت را خاموش یا روشن کند
🔹️
با این قابلیت ربات طبق اتمسفر گپ صحبت میکند
🔮
قابلیت خودمونی بودن در گروه
🔸️
ادمین از پنل استارت ربات در گروه به بخش تنظیمات برود و قابلیت را خاموش یا روشن کند
🔹️
با این قابلیت ربات بی سانسور و صمیمی جواب می‌دهد
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
⚡️
Vega Bot
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 457 · <a href="https://t.me/archivetell/6327" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
50GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 50 / 50
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 808 · <a href="https://t.me/archivetell/6326" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZlk8hyKeO4zVqUk-bXd_bjHz1WoyM7wiN9Q2DB8mzI0B_-xyN9637cGyIE_ZmE3w1yki0qUSmSAi83uJDjHzI08XY4yy9VC37UVUSzjB80MQ_YILSGDiSKktLM88wkO3B9OlDgIbBfIgfI-gXuSLzWaMZifiGA9xtE1E4a1vCIh2iRv28C-GxrhTHCqkswbuxzMXBaU-kiady0KlHtzRISfCXAw4LnJ5jc5ydGzWvcR-lZpd9LQSAZ2IKN3jYFDp5p2ID-_fk4lo9ApYn0ohV7aY1XtRZlRkJlA_9hJSvJBtwjTz13_HgaraJcK7R-yfLfUqmsNazUeRIn_6ye99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
تولید انیمیشن کوتاه از متن + عکس فقط با یک کلیک!
🎬
✨
✨
قابلیت‌ها:
•
🔹
حفظ ثبات شخصیت در تمام صحنه‌ها
•
⚡
پیوند صحنه‌های طولانی بدون قطع
•
🛠️
دوبله چندزبانه برای مخاطبان بین‌المللی
•
📦
رابط کاربری ساده و سریع
🔗
https://aianimation.video
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 906 · <a href="https://t.me/archivetell/6325" target="_blank">📅 17:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecEmRffVWT4Mz0O6dJAbrmgZ2z9udInXktbtOUDJIJe_Ib187zGMamD7VP5Ix7RPrs0axV4Y8MDd4OTXfYpbuPqHB58IhlNBRl1riyzZnr0w-QVkKXPYWDdael3yuxPp27ZTwJLfM4cyI-z2Ve26-1ocyMJneJypCuadN79iMsTX683IUGf48dDaQMFVIgsYderx0D56KxlTthyCsfZO7P7M2D1Ww8QkZfzkPHLURojqPjfy-y_e-YPwVI73v2xHqCqv-LbIYJFZaHCIu6pzEbKostWHbSyEq8pNm8ufHV7hG0uwiFbehXateHGGg4KaIrZ5ctTPQ8HSCz1PlN7yKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
تولید آهنگ فقط با توصیف متنی!
🎶
✨
✨
قابلیت‌ها:
•
🔹
نوشتن شعر، ملودی و تنظیم خودکار
•
⚡
ساخت موسیقی پس‌زمینه بدون حق کپی‌رایت
•
📦
خروجی با کیفیت حرفه‌ای
🔗
https://memotune.com
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/archivetell/6324" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTG0s6WVVKQhi5HiBqH_-BVfSHZawp3nfEBM67puw3TPNbvLgcCxMtEUJI2dVD7vqHi72mkVD2FyOn0Zvad0CRJRGs1lac0ALa9kPeqdUKw8pSpktPFby1CeOhO_h3Ru2uW-hjZOBcYd_wZYxDqBEXG7UWwrtUOKB3ks-IwNLeKIRbmWiKwCyxlvleF4r070iaEjuI8t_NaDcGuptEF_JJdUOm1xbiSb-kPOMw9e2RUiLljIqP79VBSg4KPfA4G7zH6TD5Q6RtIz5mQeKuKcE11yrRFNgKMHspz8KhmJMzS8g5mE0NpVUVHP4ZgXYLKAKCP3xOQ2gKVwNA3RoApw3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ویرایش تصویر آنلاین با هوش مصنوعی، بدون واترمارک و بدون نیاز به دانش طراحی!
🎨
🖼️
✨
قابلیت‌ها:
•
🔹
انتقال سبک و رنگ‌آمیزی عکس‌های قدیمی
•
⚡
برش تصویر و حذف پس‌زمینه با یک کلیک
•
🛠️
افزایش کیفیت و ویرایش دسته‌ای سریع
•
📦
خروجی با کیفیت بالا در مرورگر
🔗
https://stylizeimage.com
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/archivetell/6323" target="_blank">📅 16:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=FgMlXj0dS2h-ggTB_ON7Xt-wz7NV5Yhtf9a_r--zKN8y7SuNrgOaQmTrh_DhbXAaoJae6-ejix7Mc4IcFBPMi_4V0rRGFla00lC2iTKCTwa8yj8_VtN_S_bZYHpuvrh4n6MYTyhntBlsVIuPz97Lp-iJgF4kGNNwCegglq5WhF8I9XzI_75n4t5WAz2UH-On-7BG3XApqay59t08G6RYyrz-rqdCVAKGS2CLSb0ivxGPjta6CTBCbzk2Zkr_LevEmYUd4FxhXeHGUNn5NqfAL3vSadmYkBUS2OD7JxPdGElpT4qHDITfhiCcq_OHz2XDyDAVpP7dBtwSfbmLdGCD-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=FgMlXj0dS2h-ggTB_ON7Xt-wz7NV5Yhtf9a_r--zKN8y7SuNrgOaQmTrh_DhbXAaoJae6-ejix7Mc4IcFBPMi_4V0rRGFla00lC2iTKCTwa8yj8_VtN_S_bZYHpuvrh4n6MYTyhntBlsVIuPz97Lp-iJgF4kGNNwCegglq5WhF8I9XzI_75n4t5WAz2UH-On-7BG3XApqay59t08G6RYyrz-rqdCVAKGS2CLSb0ivxGPjta6CTBCbzk2Zkr_LevEmYUd4FxhXeHGUNn5NqfAL3vSadmYkBUS2OD7JxPdGElpT4qHDITfhiCcq_OHz2XDyDAVpP7dBtwSfbmLdGCD-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
افزونه GlifAI، سبک هر تصویر را با یک کلیک کپی می‌کند!
🎨
🖱️
✨
قابلیت‌ها:
•
🔹
کلیک راست → “Glif it” → دریافت نسخه‌ای با سبک مشابه
•
⚡
بازتولید هوش مصنوعی سبک نقاشی، عکس یا صحنه فیلم
•
🛠️
حفظ جزئیات قابل تشخیص در خروجی
•
📦
کاملاً رایگان
🔗
https://chrome.google.com/webstore/detail/glif-style-hunter/abfbooehhdjcgmbmcpkcebcmpfnlingo
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/archivetell/6322" target="_blank">📅 15:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lB9pQwJ0oyB1rqzGz2wujl-JegkiCJSL9A-Z7yGMfi_8LnOlW2PqEE9kpRz8ThvuXOVwL78xV1snH5S3Fk1HURjVj93m2ZlBSBa9TApybguTbdcNE-tI2eho1MscIicloR4pQ64BGg3IlQCVh4ia4lZ1pg2KedVjStS8twCiCN4Emgnu5U28xWKYoU8ufdhicm-MYNk0TsIOWZjd7x5ShKHFRHuA0nsmb7TBnLG5SMCCtZGvBaR64ejLhNRcCQ3ykN6eUSR51R5UewpJd_REKB77p4TrzTeZ3y_xKCiPNd9HEEdT8ULvGK5yR1I26yKNjSoCeQetCfG6_Z_uzpwjjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJacJNxbQQ52UgRAe7DNtbaVwm0LC0zB9nouSV66GpzmMldnQxDBWsNga-mrymKD4Gy4_2SaBxXZF9GdL9jRqm6xkPALFpPUeAtTtV6EBoAH-51bST7r-SMq5RoGLzIwRlkhdXwzrMZGGMZ9qV9d8UpWdwzHtRbK7QefkpXoJml8Smine9_eTtBXNrjEf8RNF26vlYS48BHU0nBk3U6I96o99GVBY0QQyOqbOW8a7DreD0Jzgk65Luu8iHvv32kUV2akDamh2guic8UMKRP7K2yv43F5h9Izpq9u27cPhTgvR-cpbaukggSfcmjF5lMOiVV3DHy4q7bQjO7xwtgm9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pf2Kn4TryTdYnyUfzbfeMdZK2xV-3siCmoaaoameMgrne6fFXuFkxRm8FFNaVsQjIkNxYpeWKTjxAsIzpmcmTUOsO1_SuWiKURKRCfAy4bRHo0XnL-nCOuGneXewGWLozGokeIusdnZuOa6nVYtv8Qo0UNOLdH7RvadB8EP1d_CSLIkBk27odn2BZrSdDY8D9EYod9IdwW31Ff3JHs-aAA4vYnaEIMmvC1rsh28d1gWx1nLYeZ4TvV1bqIoEqNfWQckmXPQ4PxFtNiWxVOjOdDtS7teLgliXsui1iS36si63q1Xl6I9L8jl7MU-whOn1TLc2_AXkv2YdyfBqEdHwdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد
شرکت Anthropic به‌تازگی مدل جدید
Claude Fable 5
را معرفی کرده؛ اولین مدل عمومی از کلاس جدید
Mythos
که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:
• عملکرد بسیار قوی در برنامه‌نویسی، تحلیل، تحقیق و اتوماسیون
• توانایی مدیریت پروژه‌های چندمرحله‌ای و بلندمدت
• پشتیبانی از وظایف پیچیده مهندسی نرم‌افزار و مهاجرت کدهای بزرگ
• استفاده از مکانیزم‌های ایمنی ویژه برای حوزه‌های حساس مانند امنیت سایبری و زیست‌شناسی
📌
طبق اعلام Anthropic، مدل Fable 5 تا 22 ژوئن در برخی پلن‌های اشتراکی در دسترس است و پس از آن استفاده از آن نیازمند اعتبار مصرفی خواهد بود.
این مدل به‌عنوان قدرتمندترین مدل عمومی Anthropic معرفی شده و تمرکز ویژه‌ای روی وظایف طولانی، استدلال پیشرفته و توسعه نرم‌افزار دارد.
با لینک زیر ۵ دلار اعتبار
🎁
نیاز به شماره مجازی
⚠️
(ایران رو چک نکردم ببینم داره یا نه
😂
)
🔗
https://v0.app/ref/94OS6T
🔵
@ArchiveTell
| Bachelor
⚡️
#Anthropic
#ClaudeFable5
#AI
#ArtificialIntelligence
#ArchiveTell</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/archivetell/6318" target="_blank">📅 13:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها رو یک جا در اختیار کاربر میده و دیگه لازم نیست درگیر دردسرهای مختلف بشید
🛠️
✨
✅
این بات به شبکه‌های ورزشی محدود نمیشه و حدود ۶۰ هزار شبکه فیلم،سریال،اخبار  و.. را نیز پشتیبانی می‌کنه
آیدی بات:
@Bear_Tvbot
🐻
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/archivetell/6317" target="_blank">📅 12:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxKx_OcXq9MG7l6ML0V0u6Wv9XJKwwaE8GnUz6CQYzDkGsZqn5jPNnYmtZJWnKio4fWg5owp8LE6rK1baIvYIiQBl0cccsLs0g4Hu1AUeWZzkpws73Is1YVcrakLchpnkHQXl0k1yNSe6FY-n1dXkJr8PgJBDXwOl0N6OPBG1ZMCyxrGtDc6NNgvINBrJ_rIr4IvdSgdZmwcYZBxrvLYebVn8CVXcVFD-Xj7zF3xcJiVE9GYlS5ondtCHyZFM-XkNFtrQHmsAFrZ7OJ6f_ZxDTwW-PpDrG3A_lkjUlG4hFZiy8G5jEkI4yIWWzXmegsX_jOMQOI1k7Tw6FgCbUqnWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مدل‌های پیشرفته‌ AI به‌صورت رایگان در Notion!
•
🔹
Claude Opus 4.8
•
⚡
Gemini 3.1 Pro
•
🛠️
GPT‑5.5
•
📦
DeepSeek V4
🔗
لینک:
https://app.notion.com/
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/archivetell/6316" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dr_e073ol3v_vSs4Y-A5nXIemDtUTHrmH9UKYvMfSDiFyA6rDpwz4J-Zd3YqDs-ya5K819s1pMMG-hB8qv0PHOFEeoYaVRywV7DBdxN5Z8A7UUoNKM6L0IxKKDIQ2UrYywByCs2S7xEElR4PLPZsUi4RktDyzCESGv02pS4SdX2pm8Amvcge3BPloChwL5lOAM5GUrUCPGP-fektuyGwkSFuKICxeTGJrcDa-KX-hBNw9Q0034cIQX581OOxo6Nj1M4_DqR3vnF4oXviiiKEbRDi4ijjwsPA8ZL2-QRPwaErOpK01l8DtH-hzBsdIbjErxY6XorwC8Rysf-MgloTbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dIDfg9x0SHP0Ol_nUN8B3vH_8ydG9rm10Rn9DYBUnnV_GrKKre4HeRcd13v6ORcYYDymoLhcqzH6YJeNU-2gbD4eOwGooVsDUBoHybf3QyHYmus6a6tGHuUwvE03KDi4cAITEd_3JMKvXOZYTbqICYnpsBKHftFCmRZ2DRSSPQd7na9R-kQ71TPqmuCtdaWd0PhG5blhRPr3jh4UFN1_EaZC6kCqdD6GTdXhGx_FbVCLuaBsaayOCSWLQMb-pk9FTeztK7zbLOt25L-YZjHQx4D5KiGYrKyR1JKljgSZeGQb_KDTGEXPbK9YFbBgJ7ZNuVcOMVFiKwPoGS8uvcEcKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=r5aRh9PVD3IVX-oNvnRWZqLdLUTT5DlR9-73DsGwNOM4nOrNuxZPdaLlSICX8BFe1Aij7QjxdE7BuMqwIbR3HsxVFcBglMk5nkc0KedJzzeYIlejNSOKymJMFpRfzqhEYLeGi-HDjS8nU7icMbnG3P8ZpTB5AbYgDCyIiufhhSY_VR-TKurBRPidZV2rvg2NqsG4vXu3cTMIcZiZJ_8wRYFpCBolqvykdW7ZPIPytdN0hpuf_JMhMGjacHkkh3boSlxLq2c0r6Pc9GBiHzkXiRI_RyrmygZosTVXwaWnHFlEL8xrMQ6r3TN-wjbtSr43UumQ-RpoUDXQALndul7aKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=r5aRh9PVD3IVX-oNvnRWZqLdLUTT5DlR9-73DsGwNOM4nOrNuxZPdaLlSICX8BFe1Aij7QjxdE7BuMqwIbR3HsxVFcBglMk5nkc0KedJzzeYIlejNSOKymJMFpRfzqhEYLeGi-HDjS8nU7icMbnG3P8ZpTB5AbYgDCyIiufhhSY_VR-TKurBRPidZV2rvg2NqsG4vXu3cTMIcZiZJ_8wRYFpCBolqvykdW7ZPIPytdN0hpuf_JMhMGjacHkkh3boSlxLq2c0r6Pc9GBiHzkXiRI_RyrmygZosTVXwaWnHFlEL8xrMQ6r3TN-wjbtSr43UumQ-RpoUDXQALndul7aKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تلگرام به‌روزرسانی شد: پشتیبانی کامل از Markdown و امکانات جدید
✨
قابلیت‌ها:
•
📱
دسترسی در تمام ساعت‌های اندرویدی
•
📝
قالب‌بندی نامحدود برای ربات‌ها (حداکثر ۳۲۷۶۸ کاراکتر)
•
🤖
ربات‌های هوش مصنوعی می‌توانند درخواست‌های عضویت در گروه‌ها را پردازش کنند
•
📊
امکان افزودن لینک به گزینه‌های نظرسنجی
•
🌐
باز کردن سریع لینک‌ها در مرورگر پیش‌فرض
#Telegram
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/6311" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3qSRtZ64J48TLSSVsUzWzsu4XYRCYUes_ikepryLdyoht6Cmg9GbVKljo8BQtWQ_W9Prr_6l1FQn8B-DV4KuS4MRGp-e3kI8mGELf4rynS1xb2t9RvwUsUdcYtL6PhdkIk-X6J0DVYmjgnkDVhmeU9vqqQHBi6IqQnEZo2UEprAZR7JYjdMWZQuls3PY8jiwD0Xxl4A764ahnzdfo6x1FuytiiDt93_DwuWkIxYb6GvnGTRXZVzKbu05QN8ocRtKcnsFmROBwFH7z1K_9MEhLYCwQMbsUkXL9WMx9pR-q2tbSdCvJ5o1-gmyYTts9B_jy7VFywISgCO7zM6GvVp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
MemeDepot
کتابخانه‌ای بزرگ از میم‌ها و گیف‌ها برای استفاده در شبکه‌های اجتماعی
✨
قابلیت‌ها:
•
🔹
جستجوی پیشرفته بر پایه دسته‌بندی و محبوبیت
•
⚡
فید و برچسب‌های خودکار برای میم‌های روز
•
🛠️
دانلود بدون واترمارک و ثبت‌نام
•
📦
به‌روزرسانی مداوم محتوا
🔗
لینک:
https://memedepot.com/
#Meme
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/archivetell/6310" target="_blank">📅 11:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔥
دامنه رایگان 1 ساله!
اگه دنبال یه دامنه رایگان هستی، از سایت زیر می‌تونی کاملاً رایگان برای 1 سال دامنه بگیری:
https://domain.stackryze.com/
✅
قابل اضافه کردن به Cloudflare
✅
امکان ست کردن نیم‌سرور دلخواه
✅
مناسب سایت، پنل و انواع پروژه‌ها
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6308" target="_blank">📅 02:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIWzH-x68xyFtzN4-lRIFjHMtlriawo0V-xQYEPH6pKBiAXwmS-_2cx31vt8k8b5G28eNcPrpQsIXuAl3VG-UPQLCY4WDxpaH1xMD1A8xHEB1EZeUPEJnLcPaSNWSp_8RKKJBF2QWC-ekwzV-gN9xx6Adz0cGJAbSkgiXz-mIheI5S6WdM2y5WUnakfDuPBclkjjkOfDX3Dmt73itVWci7v8HLFoBnK-AcXyFgmXhKjBkEL8wIipuMASjE0TGgQmzW-k67_SmnmWvuM-dxmQxJr6n2YG0OHdtRf132ie20dBX65NbmjyxI7qn1pcCSwK-fkxKmDSFv2lSQBqTl77Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕵️‍♂️
CloakBrowser | مرورگر ضد شناسایی برای اتوماسیون
مرورگر
CloakBrowser
یک مرورگر مبتنی بر Chromium است که برای کاهش شناسایی ابزارهای اتوماسیون طراحی شده و تلاش می‌کند وب‌سایت‌ها آن را مانند یک کاربر عادی تشخیص دهند.
✨
ویژگی‌ها:
• مبتنی بر Chromium با تغییرات در سطح کد منبع
• سازگار با Playwright و Puppeteer
• قابلیت اجرا روی سیستم محلی، Docker و سرور
• مناسب برای تست، اسکرپینگ و اتوماسیون وب
• کاهش احتمال شناسایی توسط سیستم‌های ضدربات
⚠️
توجه:
هیچ ابزاری تضمین نمی‌کند که همیشه از تمام مکانیزم‌های ضدبات عبور کند. استفاده از چنین پروژه‌هایی باید مطابق قوانین، شرایط استفاده سرویس‌ها و ملاحظات اخلاقی انجام شود.
🔗
GitHub: CloakBrowser
#OpenSource
#Chromium
#Playwright
#Puppeteer
#Automation
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6307" target="_blank">📅 01:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مرحله یک طهلیل من به واقعیت پیوست
😝</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUz1-np2DAfyP8zrWDvw3UGyoscPmMpYAtifLkhR-N--4BKOMb9C3DKpo6tIxQUc71HdApU9GEePW7zL9lcKkmYozT3vMP6cX7JtfjxqIwkBlYjpJf4yHyFWx-n31LUF1_DZTWbfVjIkHO_3L1EYCPAwiPJCeEtME5kPdTlERsnb0iwLGyT2zAUHGM7gybQtM8vmyL2lHO3aSpzeNANsjt35Pq3Hxn9W5kcf7MKpDSwG8USsWcNpgCjNZ9h0p4FcHhyWWu1BjeKzYCEJKEvy2E5VAZFGgk-i58gfTAc9vxlbNpdLp63abTNRZxaMvFsB4LSRMaUn8QLzF22A8HOMOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):
Aistudio.google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6304" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6303" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">📢
جدیدترین قابلیت‌های
ربات وگا
را معرفی می‌کنیم:
📚
حل سوالات درسی در پیوی
🔸️
در بخش سرویس های هوشمند
🔹
امکان ارسال عکس سوال
🔹
جستجو در منابع آنلاین
📝
خلاصه خودکار موضوعات گروه
🔹
هر شب ساعت 21:30 ارسال شدن خلاصه مهم‌ترین مباحث در تمامی گروه ها
🌐
بهبود سیستم جستجوی وب
🔹
نتایج بسیار دقیق‌تر و معتبرتر
🔹
دسترسی به اطلاعات به‌روز تر
📰
آخرین اخبار هوشمند
🔹
هر ۸ ساعت بروزرسانی می‌شود
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
⚡️
Vega Bot
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6302" target="_blank">📅 22:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEAdbwhkV9_wWrEzve7SAuc9r5bT8xMQSQEkoXqKPq7J8cXxJCqSpClphcC99I-ya4OU2mJZUdibDFKheSHiuQrVECsM42HL35h_2-dex9Td07ClRZRkGdIsMKSyV0WtGfbNB_EVSy9J8o6OmlRFsrOkYTiMMY4GyoTWXawS35ZJA4x9jXOLCqIM2lnPImJ1VwOi2roz5UPrickivQgjOfGdJHFnTKJmcizK4azVmakrU6dx4qGY1T9np0b7XQT5Cf3QDUAKx6haZp18mS4snN09iKnln_RTpXqo8gVqrbE3yccl7T0_lbbUR5tNnyehGDtQwVDeZ61OgDBro-tKow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
OpenAI برای برخی کاربران API Credits رایگان ارائه می‌کند
اگر از APIهای OpenAI استفاده می‌کنید، می‌توانید با فعال کردن اشتراک‌گذاری داده‌ها برای بهبود مدل‌ها، به سهمیه و اعتبار رایگان دسترسی پیدا کنید.
📌
مزایا:
• سهمیه روزانه برای GPT-5.5 و مدل‌های Mini
• اعتبار رایگان API برای حساب‌های واجد شرایط
• دسترسی مقرون‌به‌صرفه‌تر به مدل‌های هوش مصنوعی
⚠️
توجه:
با فعال‌سازی این گزینه، بخشی از داده‌های ارسالی شما ممکن است برای آموزش و بهبود مدل‌ها استفاده شود. برای پروژه‌های حساس یا حاوی اطلاعات محرمانه، قبل از فعال‌سازی شرایط را به‌دقت بررسی کنید.
مسیر فعال‌سازی:
OpenAI Platform → Data Controls → Sharing
#OpenAI
#API
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6299" target="_blank">📅 22:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/archivetell/6298" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=kQU7AO5Q8YwysAhk53oryUGpjJMM8dabgqEhXOPMGfJVppK_wYYAljSruhgSAp-ZIc4OotTyGw95QGVNgCNxwrna7fQDoUsfIFctOyV-J_GijRbwZFaoEn0PPzR77ptna1iVXGSywrjtcYREpeCVgD1d1qBJ8JrI723ZCuW0huqIQ9BnAgnzClWDMYG017a0uZhGGAh3c-XFS0bPa5XY26flfprV9pI8VH_Xv5LUSnEjOq42SX58Us3LzAE_udKjcgPWYc6s6k1Jfr4VUcRpcWB57gX5UqIly1Xnr1fXQ7kPCBwhtVeKdpfbGKKYdAqJrwn8m-WIoYGIlIc7q4Fizg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=kQU7AO5Q8YwysAhk53oryUGpjJMM8dabgqEhXOPMGfJVppK_wYYAljSruhgSAp-ZIc4OotTyGw95QGVNgCNxwrna7fQDoUsfIFctOyV-J_GijRbwZFaoEn0PPzR77ptna1iVXGSywrjtcYREpeCVgD1d1qBJ8JrI723ZCuW0huqIQ9BnAgnzClWDMYG017a0uZhGGAh3c-XFS0bPa5XY26flfprV9pI8VH_Xv5LUSnEjOq42SX58Us3LzAE_udKjcgPWYc6s6k1Jfr4VUcRpcWB57gX5UqIly1Xnr1fXQ7kPCBwhtVeKdpfbGKKYdAqJrwn8m-WIoYGIlIc7q4Fizg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم ملی ۱۹۷۸ ایران، فقط یک تیم فوتبال نبود؛ نماد غرور، اتحاد و جسارت یک ملت بود نسلی که برای اولین‌بار نام ایران را در جام جهانی طنین‌انداز کرد و نشان داد که می‌توان در برابر بزرگان ایستاد.
از ملبورن تا آرژانتین، از صعود تاریخی تا تساوی مقابل اسکاتلند، این تیم برای همیشه در قلب تاریخ فوتبال ایران جاودانه شد
❤️
یادگاری از دورانی که فوتبال، فراتر از بازی بود، یک رؤیای ملی
✨
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/archivetell/6297" target="_blank">📅 20:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EH3A0l3U_SETSB4ko11h_VSgiqDRlOBATGqkqZWPo1P20qjqf-0hd_WvzP71tRVzSL9P5aqhfqQEAhlCAtjJr7AhGnn__ZkX3NAFRqNyVeUCJeGeWccNgz8YqhORNgQLHyYf0ffAeGG21GhaF06eD7CVAEDGOnWeZ5byaDeX1FE9181PNvRw0SxmY8K3dn_MTq9y_h5y-v4c--SJVp95ZAabKOvmb1r5oHECLb473LGewR-SdbWEtbHaW5ZhnIPDg8a0rqc2phKWNSID1Yz_vLoNfvGenrOUcOmbWzqsRBfhtcxMFH-F7HLEIdY1svoI52okxBfYg5EGD4dvHfA8KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
RuView
با استفاده از سیگنال‌های وای فای، بدون دوربین یا حسگر، موقعیت و علائم حیاتی افراد را حتی پشت دیوارها تشخیص می‌دهد!
✨
قابلیت‌ها:
•
🔹
ردیابی ۱۷ نقطه از بدن انسان
•
⚡
خواندن تنفس (۶‑۳۰ نفس/دقیقه)
•
🛠️
اندازه‌گیری ضربان قلب از راه دور (۴۰‑۱۲۰ bpm)
•
📦
دیدن افراد تا ۵ متر پشت موانع و ردیابی همزمان چند نفر
🔗
لینک:
https://github.com/ruvnet/RuView
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6296" target="_blank">📅 19:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اگه میخواید به سرورتون وصل بشید ولی مشکل وی پی ان و این چیزا دارید و روی cmd و ترمینال و این چیزا وی پی ان سیستمتون کار نمیکنه میتونید از ssh آنلاین تو خود گوگل کروم استفاده کنید.
https://webssh.webhorizon.net/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/6295" target="_blank">📅 19:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🌐
Javid Mask | ابزار افزایش حریم خصوصی برای کاربران استارلینک
اگر از استارلینک استفاده می‌کنید و به دنبال راهی برای مدیریت بهتر ترافیک شبکه، فیلتر کردن دامنه‌های ناخواسته و افزایش حریم خصوصی هستید، پروژه متن‌باز
Javid Mask
می‌تواند گزینه جالبی باشد.
✨
امکانات اصلی:
• محافظت از حریم خصوصی و کاهش نشت اطلاعات شبکه
• فیلتر کردن دامنه‌ها و وب‌سایت‌های ناخواسته
• راه‌اندازی ساده روی سیستم‌های لینوکسی
• پشتیبانی از Raspberry Pi (از جمله Raspberry Pi 5)
• دریافت به‌روزرسانی‌های جدید از طریق پروژه متن‌باز
📋
پیش‌نیازها:
• سیستم‌عامل Linux
• حداقل ۵۱۲ مگابایت رم
• حدود ۱۰۰ مگابایت فضای خالی
⚙️
راه‌اندازی:
1️⃣
سورس پروژه را دریافت کنید:
git clone https://github.com/rowdy-ff/javid-mask.git
cd javid-mask
2️⃣
فایل‌ها را بررسی و دستورات نصب موجود در پروژه را اجرا کنید.
3️⃣
پس از نصب، تنظیمات موردنیاز را اعمال کرده و دامنه‌های دلخواه خود را برای فیلتر یا مدیریت شبکه مشخص کنید.
💡
این پروژه بیشتر برای کاربران استارلینک در ایران طراحی شده و هدف آن بهبود کنترل شبکه و افزایش حریم خصوصی است.
⭐
متن‌باز و رایگان
🔗
GitHub: rowdy-ff/javid-mask
#Starlink
#Privacy
#Linux
#OpenSource
#ArchiveTell
⚠️
قبل از پیاده سازی و نصب، لطفا کد منبع رو بررسی کنید.
چنل ما هیچ تعهدی در قبال این پروژه ندارد.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6293" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QHKVXIzEPKdI-4k1G4nnWQsGP9nP6aNbS4qkucDSSbn7yfdrxP43vtsz2s8nUJKKEcOuFjGHDB9P5DrwgKGsajnJ50ksb1KvWF34jLuG14u1Ilh6GLyKlCKgy6cOkB9afat3DA4uOH3kTAiLDe5s3uB7rPi-osqrnBBFG_z2TJNCpjzaXU9m3wewtOKfqBtv_4Yvn3ubh6DqMkC2txVJUBpa1_FGzMyprRhajt5Tbn3lgI2ZNA7W3PVuEBKkCFYi-M6qMNugT0LUM75rGuyZ9kztnSwCizSl9wn54Zw3BJKFJTK5gi8v8kl42ISCHS6veSiTxPDcgkCJ_nJOKmzYTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mQ1F3a2rFtRNrFnYNwYcIYuirmUC8X1yIhjW6_mI-Nd18R1_YvSmHH-lzqZ3qAVhGlCGmjSe171W7rQBi3HOGfyIHOOnMJ9869Qu0GxHJqCap5NHR49EaSdWNcUaQ-jZ3NEhaY-SBgpWOQYmbybIBjm1Z6R0p6bi9uW5jKcYSQqHUEMx5a-Rt3XPbv0ylCKRuCaYm1c1TId0agzVOU4IeFj4RQ1yptzs_FWB8bX4WqTEx_kVajBRZYFLaS1kePh5lKo5zALY0eyL39UGtBC_dvDkbxBclb8zYeaFRypIDJNRo-S8LgQFI1xjCLceoJIJwmPyNvq_04u3R0rixsc2RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JFSOedU0s_vUpmCMtc2Al6F1qBUgsOnXm-FDS7QC8zKU4W5DMfa5BLqYh2sLCMOC0--bYF-2FvmF0ih1JnTiKYDqZnssMTOTpjuwUP6cd2i5ITNRtelohrMeA54TdT2ni-nwIopt0JRab3bRKrjqYSr86YYPnXgEp3-lx5htwvQK1VZ2uj4-fTyzx7i_Vlk8hv8c-lmoxXNpyXd59ygG4-cJMj9lXtWCTiSdKyKrl3Lacj7f8HQhmAdZN2FpICPAWB2dMMVr0MC_QSg1StNh8mH3Toqm53CHVC3eICCC88yODOgggHXBZKbJwOcw4AeMZNfNogpL6GUDgu4FkomV9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
شیائومی MiMo Code: مدل جدید هوش مصنوعی برای برنامه‌نویسان، با هدف پیشی گرفتن از Claude Code.
✨
قابلیت‌ها:
•
🔹
کار با پروژه‌های میلیون‌ها خط کد بدون محدودیت
•
⚡
پردازش مخازن بزرگ بدون از دست دادن داده‌ها
•
🛠️
آموزش مجدد مدل در حین کار روی پروژه
•
📦
تمام این‌ها به‌صورت رایگان و متن‌باز
🔗
لینک:
https://mimo.xiaomi.com/coder
#OpenSource
#Xiaomi
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6290" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=NhVSZuUYScZt2oQk32OKNXCGpDscLAOQyXNOPpfGHfj4LdeYQfsHgzNBO7ppyo3BcC4is9FL36YaVj39izdTysMORlot4MjyRlKlxfhA6ZBfCCZ30x6UTtnR167IAJFhZQEHZBWdcHZTaplXAFDvg1_ztr3QHaXOfTybLo68-H5HESk3N0QLsYL22mGNF-Eazr5G3_ePVb3pXTxOFU1g-VPwqBgOIrco1PJJuFyLibVRFuRH3ypgtFjHe6buPiWXNZn9bqgei9RNvzPPIyUj8T_YsTqarXKCCyMKuK_Kdlc3PMuwPFqyAG-VJBOPNmrSC3LdjeZ7f0-4s10FgtNK3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=NhVSZuUYScZt2oQk32OKNXCGpDscLAOQyXNOPpfGHfj4LdeYQfsHgzNBO7ppyo3BcC4is9FL36YaVj39izdTysMORlot4MjyRlKlxfhA6ZBfCCZ30x6UTtnR167IAJFhZQEHZBWdcHZTaplXAFDvg1_ztr3QHaXOfTybLo68-H5HESk3N0QLsYL22mGNF-Eazr5G3_ePVb3pXTxOFU1g-VPwqBgOIrco1PJJuFyLibVRFuRH3ypgtFjHe6buPiWXNZn9bqgei9RNvzPPIyUj8T_YsTqarXKCCyMKuK_Kdlc3PMuwPFqyAG-VJBOPNmrSC3LdjeZ7f0-4s10FgtNK3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
Every‑PDF
ویرایشگر رایگان PDF با پردازش محلی و بدون ارسال به فضای ابری
✨
قابلیت‌ها:
•
🔹
افزودن متن، امضا، تصویر و واترمارک
•
⚡
تقسیم، ادغام و تغییر ترتیب صفحات
•
🛠️
رمزگذاری
•
📦
کار با فایل‌های بزرگ به‌سرعت
🔗
لینک:
https://github.com/DDULDDUCK/every-pdf
#OpenSource
#PDF
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6289" target="_blank">📅 16:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">📊
خلاصه یک سال فعالیت گیت‌هاب در چند ثانیه!
توسعه‌دهنده‌ای با نام
PankajKumardev
ابزار جالبی به نام
GitStory
ساخته که فعالیت‌های سالانه کاربران GitHub را به شکل کارت‌های آماری و قابل اشتراک‌گذاری نمایش می‌دهد.
🔹
کافی است نام کاربری GitHub را وارد کنید.
🔹
سرویس اطلاعات عمومی پروفایل را جمع‌آوری می‌کند.
🔹
سپس آمارهایی مثل تعداد کامیت‌ها، ریپازیتوری‌ها، مشارکت‌ها و فعالیت‌های سالانه را در قالب کارت‌های گرافیکی نمایش می‌دهد.
﻿
💡
اگر توسعه‌دهنده هستید یا می‌خواهید نگاهی سریع به عملکرد یک سال گذشته خود در گیت‌هاب داشته باشید، GitStory ابزار جالبی برای بررسی و اشتراک‌گذاری دستاوردهایتان است.
https://github.com/pankajkumardev/gitstory-2025
#GitHub
#Developers
#OpenSource
#Tools
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6288" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚀
دریافت ۲۵۰ دلار کریدیت رایگان برای API
اگر دنبال دسترسی رایگان به مدل‌های زیر هستید، می‌تونید با Agent Router API Key اختصاصی بگیرید
👇
🖋️
Claude Opus 4.6
🧠
Deepseek v4 pro
⚡
GLM 5.1
📌
مراحل فعال‌سازی:
1⃣
وارد سایت
Agent Router
شوید
2️⃣
اگر سایت به زبان چینی بود، از بالا سمت راست
🔝
زبان را به English تغییر دهید
🇺🇸
3️⃣
روی Sign up بزنید و با حساب GitHub وارد شوید
🐱
4️⃣
وارد بخش API KEYS شوید
🔑
5️⃣
یک API Key جدید بسازید
➕
6️⃣
طبق راهنمای این سایت، از کلید ساخته‌شده برای اتصال API استفاده کنید
⚙️
💡
با این API می‌توانید:
🤖
ربات تلگرام بسازید
🌐
وب‌سایت طراحی کنید
⚡
ابزارهای اتوماسیون ایجاد کنید
💻
پروژه‌های هوش مصنوعی توسعه دهید
🔥
فرصت عالی برای تست مدل‌ها بدون پرداخت هزینه
💰
﻿
@Archivetell
✨</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6287" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⚡️
سیم کارت رایگان همراه اول به خاطر جام جهانی (کد تخفیف + پست رایگان)
CUPSIM26
هر کد ملی تا ۳ تا میتونه بگیره (همه رو تو یک سبد بذارید)
لینک خرید
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/6286" target="_blank">📅 11:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=tWvOS5rewvhItWWkDL5iKkKjFrHCBOzeqoU6g5PueIJiR5cX4M8t3F51ZvssxtpNwAg1U4djI8PKeL6-plgnsUbZD8GNbnrfEqNdsox-uGzNI_GbRnIMiuhBmJm8UyOuHntEZ6Lhyl1AbYFEMYAF3dyVYmr6sS-jbbUUOBZ-7fOvnHBzDXJMXL0RXc3YE8zdNhTpnWBHY5CQDk4i_XS-HEJMrllPssIcOh6VmbRH6DHUKP1lQC418zIWplcb4e5gOLADK7DBsp4T425SmKQK60e8DJwhNwBBC4gwEBDiggksQHkL-_dD51L6po3EZg_iaoc0IJnCS9ZwQccr9fhOPg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=tWvOS5rewvhItWWkDL5iKkKjFrHCBOzeqoU6g5PueIJiR5cX4M8t3F51ZvssxtpNwAg1U4djI8PKeL6-plgnsUbZD8GNbnrfEqNdsox-uGzNI_GbRnIMiuhBmJm8UyOuHntEZ6Lhyl1AbYFEMYAF3dyVYmr6sS-jbbUUOBZ-7fOvnHBzDXJMXL0RXc3YE8zdNhTpnWBHY5CQDk4i_XS-HEJMrllPssIcOh6VmbRH6DHUKP1lQC418zIWplcb4e5gOLADK7DBsp4T425SmKQK60e8DJwhNwBBC4gwEBDiggksQHkL-_dD51L6po3EZg_iaoc0IJnCS9ZwQccr9fhOPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
OpenAI
تا ۵۰ هزار دلار اعتبار رایگان API میده!
🎉
•
🔹
۲۵۰ هزار توکن در روز برای GPT-5.5
•
⚡️
۲.۵ میلیون توکن در روز برای مینی‌مدل‌ها
•
🛠️
تا ۱۰ میلیون توکن در روز در سطوح ۳ تا ۵
•
💥
در عوض، داده‌های شما برای آموزش مدل‌ها استفاده خواهد شد.
📦
این ویژگی برای همه فعال نمی‌شود، اما ارزش امتحان کردن دارد — وارد OpenAI Platform شوید، Data Controls را باز کنید و به بخش Sharing بروید.
🔗
لینک:
https://platform.openai.com/
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6285" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prWKfKvZwcJ5LZagF1hy7W4SfjXoZa-vWHlEoUE8a3N12QP5x1XRifQHfsu-t6nDQJ-I80k74nS9fd-r24yM_vdpx_flvEtTIrJGu_nQ5ohH0FCLQppV5plyfMye1CCZL5B76NCKs6y7sKt_uDdlwpoCsN6OaSShcvfsNfkee4EjF-m8j7LeAZJyH6HNlKMljAhDqUrJW__stuvL2xX_u7S3TklZyZmyKSSZkQkPpD1kGCAb_jEFXpBDZvVs2HPje2F-A3g4KBb_FsUlL9pGq50sYXYVK8IezwcDa7z_QLC7Ho1eyGhCtIaIb4mf_8NQ5EsDj7kW9WV9FiVdsYgikQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
BrowseryTools
مرورگر خود را به یک جعبه‌ابزار قدرتمند تبدیل کنید! 136 ابزار رایگان برای فایل، رسانه و هوش مصنوعی، همه در سمت کلاینت.
✨
قابلیت‌ها:
•
🔹
ویرایش تصویر و ویدئو بدون نصب
•
⚡
مبدل‌های فایل سریع و آنلاین
•
🛠️
ابزارهای توسعه‌دهنده با Next.js + TypeScript
•
📦
هوش مصنوعی محلی: رونویسی، ترجمه، حذف پس‌زمینه با Transformers.js
•
🌐
متن‌باز و قابل میزبانی مستقل
🔗
لینک:
https://github.com/aghyad97/browserytools
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6284" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=TA26iAz69xvogJD0QGILA5_1wrILpNfMCXRo2NySfBVOyrXTc1tkriBhmT44bA3nTeiKIVzeneUVeWC7r0tLfeNLJZlHmGdtVNYNpzK0CKhEbCYv2iN40uXVZFjMcjyAaSLzRFQhZQWaZlV1Omkc8stOmKfa-oR4jMXLPoQayH2n7nSS4NgQTOZBvzZB6rWnzG-ImXcRSKrifHppNr21f74L8Fbt6WMUvHko_nPx_LBlEWYY1P2RHzHqlRWBq8C-ttJmtMixM6RWnmn4SsvaaT2_Xsm8FgMkugxqBFdPXK5YEa-LG_ykdMa_c1SEgkKmVijNsr0dtxl00TuyF1Jy_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=TA26iAz69xvogJD0QGILA5_1wrILpNfMCXRo2NySfBVOyrXTc1tkriBhmT44bA3nTeiKIVzeneUVeWC7r0tLfeNLJZlHmGdtVNYNpzK0CKhEbCYv2iN40uXVZFjMcjyAaSLzRFQhZQWaZlV1Omkc8stOmKfa-oR4jMXLPoQayH2n7nSS4NgQTOZBvzZB6rWnzG-ImXcRSKrifHppNr21f74L8Fbt6WMUvHko_nPx_LBlEWYY1P2RHzHqlRWBq8C-ttJmtMixM6RWnmn4SsvaaT2_Xsm8FgMkugxqBFdPXK5YEa-LG_ykdMa_c1SEgkKmVijNsr0dtxl00TuyF1Jy_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
افزونه ImageToPrompt تصویر شما را در چند ثانیه تحلیل می‌کنه و یک پرامپت آماده برای مدل‌های تولید تصویر می‌سازه.
✨
قابلیت‌ها:
•
🔹
تشخیص سبک، اشیاء، نورپردازی و ترکیب‌بندی
•
⚡
تولید پرامپت دقیق برای Stable Diffusion، DALL‑E و …
•
🛠️
بدون نیاز به ثبت‌نام یا حساب کاربری
🔗
لینک:
https://chromewebstore.google.com/detail/ImageToPrompt/pgabcjhpgdcgbflabemecpficpknnpfn
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6283" target="_blank">📅 09:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUWjl_LitXhEkO1_wbxp90lPnZHVcHSd-Q9Dm3oyUV4UtOEO9CGWIOVcgZTTgdtNTXsciFPl4zUjqRhL16IvVbpoA9bU8khNvacDZWoDbZQA85dWEJvNuaRs4BlIdxwUi3ScHZZtC58MX1V3J9EW8SPODtpG7K-Mg2u0RQxvS61_VXAZt7DhI-YBFcpvUndfRI7-T9114aSR0bVpON1RfxMbeVQ6zAPWnyipKbCdLzCpRgh3biBOmE3KVEBbn-krI9wonp34kR4jfLOGkCLXfTENfyNsB3KbeiytdH51mCZSdxDw-qB4bAbzvzJgE8AWxvMpRa9jyc9XwNiUN8e16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتقال فایل سریع و پایدار بین دستگاه‌ها با قابلیت ادامه‌دادن پس از قطع
✨
قابلیت‌ها:
•
🔹
انتقال همزمان بین چند دستگاه
•
⚡
ادامه‌دادن خودکار پس از قطع ارتباط
•
🛠️
سازگاری با شبکه‌های پیچیده و متغیر
•
📦
انتقال تطبیقی برای بهینه‌سازی سرعت
🔗
https://shrimpsend.com
دانلود فایل مخصوص ویندوز ، مک و اندروید :
https://github.com/shrimpsend/shrimpsend/releases
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6282" target="_blank">📅 08:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbRhsvHi6U0T_VEV7oba7bMPJYMqNeKpYaPc7Z00uzkS23bUY0ajAbWWBIQUS40SSx8kSs7Jpcx5hVXMdSxVr5cDQD_KREmK8SbrIkM2tv_x-f4j-rzc8ZgBjuphkzp30kUoNebblCEFSWpENofZZgpP7wSnxsPydPCfIxAUxCP8yTJulv6glq76yf6QUbYJExg8GgFSOCkuF9wbEf4qJVDjTEEo1joVV1YaeiIT5srnFQOwg0fG03G5y_lNDaZW0xzrMaclln-hX_1Z0dSJlTSjFIKGcQpJ9W6HNDsVRONqWbPdxl1WtvXWndDxM4KhoGtSw-SMMtN0KYC8vsnF6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوتاه اما جالب
❕
به این صورت داخل duckduckgo میتونین qrcode بسازید
🔗
🎁
@Archivetell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6280" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6279" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚀
راه‌اندازی خودکار 3x-ui با WhiteDNS؛ از صفر تا تحویل کانفیگ در چند دقیقه  اگر حوصله نصب دستی 3x-ui، تنظیم کلادفلر، گرفتن SSL و ساخت کانفیگ‌های Reality و VLESS رو ندارید، WhiteDNS تقریباً همه این مراحل رو به‌صورت خودکار انجام می‌ده.
📋
پیش‌نیازها  قبل از…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6278" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=da_GCeXrbTBSrxRauz1Qv9STajz5mr8ZspehKsXeSEwQcuQ-XGwzlhrIX7Fg-Tz0KbA49z-M7_vQslaVLvohtMQ2NFyUZg62TnL5sGZRXCHffIpJ2jKAK3WiLfrcZlzWIzPn13ZzzT8NIQutmH7cUFz3Gl_kNm3XAPoQcxf340BJ-Dh9iHFwyBwLog9KSgnVBchme0XczQsXvgiMTLoXu5iqGMqSBYLsihisQ7jRTNCHQZlUfhWvzWir1UIWM2mqOX3GMpSXCHtTGflLXl7StubX7h4iwmYrDVOcY63fW92JRMmQZJG-CQlBZNCOwsAtm9FgKYc-kU3R1-ob_BN3dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=da_GCeXrbTBSrxRauz1Qv9STajz5mr8ZspehKsXeSEwQcuQ-XGwzlhrIX7Fg-Tz0KbA49z-M7_vQslaVLvohtMQ2NFyUZg62TnL5sGZRXCHffIpJ2jKAK3WiLfrcZlzWIzPn13ZzzT8NIQutmH7cUFz3Gl_kNm3XAPoQcxf340BJ-Dh9iHFwyBwLog9KSgnVBchme0XczQsXvgiMTLoXu5iqGMqSBYLsihisQ7jRTNCHQZlUfhWvzWir1UIWM2mqOX3GMpSXCHtTGflLXl7StubX7h4iwmYrDVOcY63fW92JRMmQZJG-CQlBZNCOwsAtm9FgKYc-kU3R1-ob_BN3dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6277" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=XkYuh2wl3JUt5YBs6DQ-KDjfb-Et94eSR7fuMn65fqkencb3ZFTZGCBs0CdLgx5_AwL4XY6nWbCZFrtXyWuDvpocYEHyFrmob6KNtuLi_HQVpVzexza0x1BVhwczgpnfePWywWC71cbHXSyO6VJQm_HTYVl04ZVDsP2nV48d1SZrHDv8rFGD0eCtHhd8V1_vsGP_a9urH7dDeHHVwlpIptip78Rx4fvPnGl9lDxWBTYgJtsaEZ1AzK9qEtdPoCQdNoDUw-fPlvbNczQRlr32PV63g0807p2hkPmAlN1MMZhPa5WBUw9omw9-gDJgRiuSDhqqvMNthRB67Ho-9lKKDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=XkYuh2wl3JUt5YBs6DQ-KDjfb-Et94eSR7fuMn65fqkencb3ZFTZGCBs0CdLgx5_AwL4XY6nWbCZFrtXyWuDvpocYEHyFrmob6KNtuLi_HQVpVzexza0x1BVhwczgpnfePWywWC71cbHXSyO6VJQm_HTYVl04ZVDsP2nV48d1SZrHDv8rFGD0eCtHhd8V1_vsGP_a9urH7dDeHHVwlpIptip78Rx4fvPnGl9lDxWBTYgJtsaEZ1AzK9qEtdPoCQdNoDUw-fPlvbNczQRlr32PV63g0807p2hkPmAlN1MMZhPa5WBUw9omw9-gDJgRiuSDhqqvMNthRB67Ho-9lKKDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6276" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=F3X4N95_QOUjsDQwSOXJV8vIWkdHH0cMkRYFKIlplx3NqyTRX5RYOVQHJ04eN5xnUJGRyHGLo5s0JHu9O4yQ9lFrxiiiOGkxytN9kZckPdNiPKhJF3ewjva551wvOTkUFHEX1gUEvtyMBoVO-V0pqV_rsdTyFnG81NeGFn2IF8eBld_Alp3zEX17rL16P9mFzj8rtj3a-bQR02G1TsYpNiphi7qAe-tJ3PZRI02-fdTFXGfqVO3Yw9rl-JAXLHqkPah70d1X37oXS8BJU3hrNqkGOd9Om1o7Xj2bJIbVHXUcAPZ7CoOtvewyhQV-OL1m3aUJKIydm39WyOzoEMTlHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=F3X4N95_QOUjsDQwSOXJV8vIWkdHH0cMkRYFKIlplx3NqyTRX5RYOVQHJ04eN5xnUJGRyHGLo5s0JHu9O4yQ9lFrxiiiOGkxytN9kZckPdNiPKhJF3ewjva551wvOTkUFHEX1gUEvtyMBoVO-V0pqV_rsdTyFnG81NeGFn2IF8eBld_Alp3zEX17rL16P9mFzj8rtj3a-bQR02G1TsYpNiphi7qAe-tJ3PZRI02-fdTFXGfqVO3Yw9rl-JAXLHqkPah70d1X37oXS8BJU3hrNqkGOd9Om1o7Xj2bJIbVHXUcAPZ7CoOtvewyhQV-OL1m3aUJKIydm39WyOzoEMTlHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6275" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ادم خودشو باید برای هر سناریو اماده کنه و باید تو پیشگیری خوشبین باشه. چون شاید همون ی روش هم جواب داد</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6273" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">همین الاناس که ترامپ میاد میگه:
دقایقی قبل قرار بود دستور حمله رو صادر کنم، ولی آنها گفتند ما مذاکره میکنیم و من برای این حسن نیت آنها ۲ هفته حمله را به تعویق انداختم.
ممنون از توجه شما
دانلد جی ترامپ
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6272" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">برق قطع بشه با کبوتر میخوای پیام بزاری تو تلگرام؟ 🫪</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6271" target="_blank">📅 00:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6270" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6269" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6268" target="_blank">📅 00:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">📝
جنجال جدید در دنیای آفیس‌های متن‌باز
پروژه
Euro-Office
نسخه 1.0 خودش رو به‌عنوان یک جایگزین اروپایی و متن‌باز برای Microsoft Office منتشر کرده، اما این ادعا با واکنش تند تیم
LibreOffice
روبه‌رو شده است
😬
🔹
بنیاد LibreOffice می‌گوید Euro-Office خودش را «اولین مجموعه آفیس متن‌باز اروپایی» معرفی کرده، در حالی که LibreOffice سال‌هاست چنین جایگاهی دارد.
🔹
همچنین توسعه‌دهندگان LibreOffice معتقدند تمرکز Euro-Office روی سازگاری کامل با فرمت‌های مایکروسافت، عملاً آن را به یک «هم‌پیمان غیرمستقیم مایکروسافت» تبدیل کرده است.
⚡️
به نظر می‌رسد رقابت بین پروژه‌های متن‌باز برای جذب کاربران و سازمان‌های اروپایی وارد مرحله جدیدی شده است.
#OpenSource
#LibreOffice
#MicrosoftOffice
#EuroOffice
🐧
📄
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/6267" target="_blank">📅 21:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyrI2a8QNCODUtjAi9tC1N4CQHtg97sOz8mgLYOjzXqvkLxUrVlpCk8J1_duklsFxp3-HN07CcUC9yEnqY9GI82wcNNPnH_hGYjxKLtwfAWs1Ke6hn1YJ0OjkPURHKK0hIIeg9iaoZLYAVQ3fjs7MhMxn232esu0VkzPQBU6lA0rf4AuZ_uSeJzLI926WI_wj0Ms0vVZcJUwhVOAHaAAs_8qzwGECVVZ_z47pezsJeNUhOaVlItGgiMWVAOMAbjRY8OIlGgi-GiyJ3mbwAohppKdqyvcKwEBVlAYEorYawfbEH3axpPk2DYAI8wFQe7I-r5Pqtf2gUF8x_0JUKPtXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ZOOOP: همه ابزارهای خلاقیت هوش مصنوعی در یک پلتفرم!
🎨
🤖
✨
قابلیت‌ها:
•
🔹
تولید تصویر، ویدئو و صدا با یک کلیک
•
⚡
کلون حرکتی برای انیمیشن‌های دقیق
•
🛠️
قالب‌ها و مدل‌های محبوب پیش‌ساخته
•
📦
یکپارچه‌سازی ساده و سریع
🔗
لینک:
https://zooop.ai
#OpenSource
#AI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6266" target="_blank">📅 20:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKwqh9-06LeluLWs7-eUZTygNUi9COYNAS59pRdoreP_66LOgluET7JrSsKKU5BZeM4FGKmlhbeHgo7AlPLw9LJKolRaessgOwA0c_fT6lAQsrYEt1LEFUCtb_N2Zg-SgCU6uRpxsJYk2v7gUtAzjpvOEPJlfFvlnKVOIy4iBP-_DUVMzDnAKdPlzpNt64vtB7PhSrKc8Vu6XZ8uB4C8sjYcwRGOOqJhE4hfZpAQoSxsZZw3wLkjwB6cbH2AMaOptIb5OTvW7DOSmGNjcAKPGmkgKqYEJ48eHIBYx0fW7J7K207QYyuayjRk5CJ233wVCohVJQV7iFDAYnmWxkBu1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕵🏻‍♂️
با این ابزار می‌تونید فقط با وارد کردن یک نام کاربری، حضور احتمالی اون رو در سایت‌ها و پلتفرم‌های مختلف بررسی کنید.
✨
قابلیت‌ها:
• جست‌وجوی خودکار در صدها سایت
• بررسی شبکه‌های اجتماعی، انجمن‌ها، پلتفرم‌های بازی و سرویس‌های دیگر
• نمایش تطابق‌های پیدا شده در یک فهرست
• اجرا مستقیم داخل مرورگر، بدون نصب برنامه
• امکانات پایه رایگان
🔗
لینک:
https://whatsmynameapp.net/
#AI
#OSINT
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6265" target="_blank">📅 19:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6263">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581e875845.mp4?token=hmFqkemk7ACZXE3AJYuAZnAVJdMeb4vl6bUHf8YeI0iJtFvKNOVR8bfX00RWfGD3WpyMBwCTkZqXgbVikecSdIF6t6oTv01Ujc4iNIWIjtbl-V1gb6_wfqD7Y3PscDo0EweOV0fzMHfu_k8PrztLGDD6bchQBsXiI9saXBfrhS528xnXF07TsaN9Kbhgqfdroyzy5drBRyxipzWSyVvJfdB5wnPTwU7PxSVNHSMlVn3zBItcAgcQJ9ItFocp8G7EkBTsKX3g7rn5iUpUWxwuZzSCmBspoVXTWn7llDlI6KhUW2HZcgyEwGshV1oQ_h23iw60Oecg8d3pQFi2bKH8Jx342GpR2nIbWLK5E7S-WPTBjeAR3TSyIHKyg3MRfd4yyFe3ylnhv4dtIdPZi-naTMkM69CfmjD8LGPzFbvTJMrH43pVbScYlwRa_bTeIAUWKICAMLYRJ-mdXrG_rEs8uh6TKTmIuTZTh4H8kDFj4C41wGN_2FEek4YSHMO2TF2jWXkjC3NwnnxAszXNqgEzpkpmxaJy-8Rw9h_qMG00DADf2vtv1V1LwrrEFy_na0LPlSMPk4R4jOW_LOluuEL3kZC0NSVHZ1Bd1hOazgOVQxLpb17WboQE5xf8mxqMECHx0qn7y8B_fPLt59bJnIIPvKRIRGlgjg2J2RQwg-cWtkU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581e875845.mp4?token=hmFqkemk7ACZXE3AJYuAZnAVJdMeb4vl6bUHf8YeI0iJtFvKNOVR8bfX00RWfGD3WpyMBwCTkZqXgbVikecSdIF6t6oTv01Ujc4iNIWIjtbl-V1gb6_wfqD7Y3PscDo0EweOV0fzMHfu_k8PrztLGDD6bchQBsXiI9saXBfrhS528xnXF07TsaN9Kbhgqfdroyzy5drBRyxipzWSyVvJfdB5wnPTwU7PxSVNHSMlVn3zBItcAgcQJ9ItFocp8G7EkBTsKX3g7rn5iUpUWxwuZzSCmBspoVXTWn7llDlI6KhUW2HZcgyEwGshV1oQ_h23iw60Oecg8d3pQFi2bKH8Jx342GpR2nIbWLK5E7S-WPTBjeAR3TSyIHKyg3MRfd4yyFe3ylnhv4dtIdPZi-naTMkM69CfmjD8LGPzFbvTJMrH43pVbScYlwRa_bTeIAUWKICAMLYRJ-mdXrG_rEs8uh6TKTmIuTZTh4H8kDFj4C41wGN_2FEek4YSHMO2TF2jWXkjC3NwnnxAszXNqgEzpkpmxaJy-8Rw9h_qMG00DADf2vtv1V1LwrrEFy_na0LPlSMPk4R4jOW_LOluuEL3kZC0NSVHZ1Bd1hOazgOVQxLpb17WboQE5xf8mxqMECHx0qn7y8B_fPLt59bJnIIPvKRIRGlgjg2J2RQwg-cWtkU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تست رایگان Battlefield 6 در استیم شروع شد؛ تا ۱۵ ژوئن می‌توانید این شوتر را بدون پرداخت هزینه تجربه کنید.
✨
قابلیت‌ها:
•
🔹
دسترسی رایگان محدود تا ۱۵ ژوئن
•
⚡
شامل ۵ حالت بازی مختلف
•
🛠️
تجربه ۴ نقشه چندنفره
•
🗺️
بازگشت نقشه‌های کلاسیک مثل بازار قاهره از BF3 و جاده گولماد از BF4
🔗
لینک:
https://store.steampowered.com/app/3028330/Battlefield_REDSEC/
#Battlefield
#Gaming
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6263" target="_blank">📅 18:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سیستم جدیدی به
ربات
افزوده شد.
✨
از این پس، در بخش
سرویس‌های هوشمند >> آخرین اخبار
، امکان دریافت اخبار روز ایران و جهان فراهم شده است
📰
🌍
هر دو ساعت اخبار بروزرسانی خواهد شد
✅</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6262" target="_blank">📅 18:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🦀
Asterinas 0.18 منتشر شد
پروژه Asterinas یکی از جاه‌طلبانه‌ترین پروژه‌های متن‌باز دنیای سیستم‌عامل‌هاست؛ یک جایگزین مدرن برای لینوکس که تقریباً به‌طور کامل با Rust نوشته شده و روی امنیت حافظه، کارایی بالا و سازگاری با اکوسیستم لینوکس تمرکز دارد.
در نسخه 0.18 تمرکز ویژه‌ای روی اجرای Asterinas در محیط‌های کانتینری و مجازی‌سازی بوده و قابلیت‌هایی مانند Namespaces، cgroups و بهبودهای مختلف VirtIO به آن اضافه شده‌اند.
از دیگر تغییرات مهم:
🔹
درایور جدید NVMe
🔹
بازنویسی درایور فایل‌سیستم EXT2
🔹
پشتیبانی بهتر از نرم‌افزارهای لینوکسی
🔹
اجرای برنامه‌هایی مانند Firefox، QEMU و Codex
اگرچه Asterinas هنوز فاصله زیادی تا جایگزینی کامل لینوکس دارد، اما یکی از جدی‌ترین تلاش‌ها برای ساخت یک سیستم‌عامل مدرن، امن و سازگار با لینوکس بر پایه Rust محسوب می‌شود.
#Linux
#Rust
#OpenSource
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6261" target="_blank">📅 17:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کانفیگ ناب
🔥
trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/6260" target="_blank">📅 16:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vM2ltHOl7J1wFibPDTL7Br_4oIXVgysoWAy0OMVbMCicMCOc7M7Y9DjztOlPwS3BHcw_F7S16Xa28Q_Scfcyc3W5dTVx6IgH8kfNHth9WGpf4lfdrYMM-EtjBVkoAxfA-TgLXaEt75E6LaPLGgnd12354Fyj61aNb2qYnzC1xsRQA7pMSdpKp5fXzZBoS85JY8CKzacpy8nhw99CCChxTOZUqp1V8xlzlZXamekZfaC_eVGZcgZ1k1it_s3-ac5tU2i-Hm7i5uAkIhjdCUS4NpGNQJFbI8caF3JaXK2YXfY_0P0kT-GEUpwfjBncGlaFgj-Mj21n67HQ3hgDN9aZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
یک ویرایشگر ویدیوی رایگان که مستقیم داخل مرورگر اجرا می‌شود و فایل‌هایتان را روی کامپیوتر خودتان پردازش می‌کند؛ بدون آپلود در فضای ابری.
✨
قابلیت‌ها:
•
🔹
ویرایش چندمسیره ویدیو
•
📝
انیمیشن متن برای ساخت محتوای حرفه‌ای
•
🎧
افکت‌های صوتی کاربردی
•
🎨
تصحیح رنگ و بهبود تصویر
•
📦
خروجی با کیفیت 4K
•
🌐
اجرا در Chrome و Edge بدون نصب نرم‌افزار سنگین
🔗
لینک:
https://github.com/Augani/openreel-video
#VideoEditing
#Tools
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6259" target="_blank">📅 16:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=bKTfivq0Y1yuKxj3vRCLU2gyWpGWOG0CFeNXme4Cju294fdqtMelwLptHwooaRqS2lOut_oLBWg4t7Mxjs-IXGrSML0IhBff_wfH5j3cvhx32hBTpLT_b-0a7-Y4UNmfvVAzV7AM1gLBMriLbk6tzrYRfE1v6VgdaWPle1oqAGIyLE2BzXEBqz59QJteSyKPt9sFcVy2TMq2Qs71u0eyRSluIovRrnpRvsekyh2GzYbuPb0BqyJ23kQxJ3wmX_4j0J-aDUmLg2tWlvqRzMyqYimhKSDqnN1e2JU2uo4tAqfvnCrntZHK-Qf8bsPUCPA8zouZAL5tA1L-p9e7vGfE7zPl8rQa2WuGXryA7bIOQ_Jm9z2Nh-oMz2dvMWmoBNSdrwK7K6T9O1hnxXmgtqFaKVNe9SBE9AwaZ0HbPAmyFX8eM_CUiWnRujaMp-QGN1jQcqPdwRjA3bU0q-K4InXbTXwI9rcdpWoqE6Pz28qqzc0IxOZoyyjiTVqZqiEYal1LBjBV2LqC2PpVp4A_HPXUvQXdkQqmcxR-4xzXxFHWKXDS6tmfk-98VY6wEzkaCdJMdv9EHVoF1t_ttvSSLCSrrSiS-ahmajXMzwpGYkYNVwqO8NL5eN3yl7wJhwkIHG2gzP_ihnHInEx4-eBKpWNZxz79Vf_SFLxDyIJMOP_okUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=bKTfivq0Y1yuKxj3vRCLU2gyWpGWOG0CFeNXme4Cju294fdqtMelwLptHwooaRqS2lOut_oLBWg4t7Mxjs-IXGrSML0IhBff_wfH5j3cvhx32hBTpLT_b-0a7-Y4UNmfvVAzV7AM1gLBMriLbk6tzrYRfE1v6VgdaWPle1oqAGIyLE2BzXEBqz59QJteSyKPt9sFcVy2TMq2Qs71u0eyRSluIovRrnpRvsekyh2GzYbuPb0BqyJ23kQxJ3wmX_4j0J-aDUmLg2tWlvqRzMyqYimhKSDqnN1e2JU2uo4tAqfvnCrntZHK-Qf8bsPUCPA8zouZAL5tA1L-p9e7vGfE7zPl8rQa2WuGXryA7bIOQ_Jm9z2Nh-oMz2dvMWmoBNSdrwK7K6T9O1hnxXmgtqFaKVNe9SBE9AwaZ0HbPAmyFX8eM_CUiWnRujaMp-QGN1jQcqPdwRjA3bU0q-K4InXbTXwI9rcdpWoqE6Pz28qqzc0IxOZoyyjiTVqZqiEYal1LBjBV2LqC2PpVp4A_HPXUvQXdkQqmcxR-4xzXxFHWKXDS6tmfk-98VY6wEzkaCdJMdv9EHVoF1t_ttvSSLCSrrSiS-ahmajXMzwpGYkYNVwqO8NL5eN3yl7wJhwkIHG2gzP_ihnHInEx4-eBKpWNZxz79Vf_SFLxDyIJMOP_okUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
نسخه ۳.۲ مدل Ray از Luma منتشر شد؛ اما طبق تست‌های اولیه، هنوز با رقبایی مثل Seedance فاصله قابل‌توجهی دارد.
✨
نکات مهم:
•
🔹
پشتیبانی احتمالی از خروجی HDR با فرمت EXR 16-bit
•
⚡
تولید ویدیو تا ۱۰ ثانیه
•
🛠️
ساخت ویدیو بدون صدا
•
📦
ضعف در بافت‌ها، انسجام تصویر، دینامیک حرکت و درک پرامپت
🔗
لینک:
https://lumalabs.ai/ray3-2
#AI
#VideoGeneration
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/archivetell/6258" target="_blank">📅 15:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qPRsiSyZb5YElYRMVgItHMB2u0vwwEiO7Qu6GAnDFeVZNhRdl6ZFTja31idGNaE_WH8AKZmFVoX5Lr1E36bbWhfNyQ5TczsxJtFvf8PuziKOg--0q9-JenN0754HyyEz5RF73GGLQenXTuOsYBUqYaFHwwc1xYZnmc36S83GuKEbYtYEacHyz4_KXWnYno-qPBTHg7TmoYXjbZvju3BHtyqo6C5daXH8-pLNLT-VIEk1B7yfODdcxb12iNzkHok0RdKQwloIz7H8S2aiWVbI1yROlqGYqe6mPUTavxkS6kmlB2hYFe9BmCaq0XGRDDK001XonQtzakpAT55uClfZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CNIc9lq5fHJI5iLBkXyCMJhTm2Ia2yILRZHQfZop4LwsgY6tmdMUpKxCTb22IDfzg__dDXrQEiMVyHSsf5xv7-9uWvPGKDm3Hj-WrmQmDuxV9MzHgdXOXvkyGVqc9wK2PVFD7QqVanBtEOmz-BN52_UAVSzBcIY9BElxz7AIQ-kO1S2EiAVtiXECXY6Qj9LUmnfRIJ0M_4d9z57-DvK-aLZACwtklJD5_FCIYHSL1kEitHCqgxk6WpQZMTLeVWMm_DDTqnSmgeGPQ6NG42Tb-s0FE3N-C56TX9oBAyoz5656BprvP2IeJMX6Tzjjg0w8oSI4LUE3IgWg4nrShhw8HQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
CodeWhale
یک عامل ترمینال رایگان و متن‌باز برای کدنویسی با DeepSeek و مدل‌های محلی است.
✨
قابلیت‌ها:
•
🔹
خواندن و ویرایش فایل‌ها داخل ترمینال
•
⚡
اجرای دستورها و کار مستقیم با Git
•
🧠
حفظ زمینه بین جلسات کاری
•
🛠️
پشتیبانی از MCP، مهارت‌ها و ابزارهای اضافه
•
📦
اجرا با DeepSeek، OpenRouter یا Ollama
نصب سریع:
npm install -g codewhale
🔗
لینک:
https://github.com/Hmbown/CodeWhale
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/archivetell/6256" target="_blank">📅 15:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آپدیت جدید
ربات وگا
انجام شد
✨
- اضافه شدن GPT-5.4
🚀
- اضافه شدن Gemini 2.5
⚡️
- اضافه شدن Flux 2 Kelvin
🌡️
- جایگزینی Lucid Origin با Flux 2 در گروه ها
🔄
- حل مشکل هنگ کردن Gemini 3
✅
- رفع سایر مشکلات
🔧
>
آموزش گرفتن API رایگان GPT-5.5
<
ArchiveTel - VegaEnter</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6255" target="_blank">📅 13:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">💵
گوگل اشتراک AI Plus را ارزان‌تر کرد؛ حالا فقط ۴.۹۹ دلار در ماه با ۴۰۰ گیگابایت فضای ابری.
✨
قابلیت‌ها:
•
🔹
دسترسی پیشرفته به Gemini 3.1 Pro
•
🧠
Deep Research برای موضوعات حجیم
•
📒
NotebookLM برای تحلیل و ساخت پادکست
•
🎬
تولید ویدئو با Gemini و Flow
•
☁️
۴۰۰ گیگابایت برای Gmail، Drive و Photos
🔗
لینک:
https://gemini.google.com/app
#AI
#Google
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6254" target="_blank">📅 13:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">📱
اگه حافظه آیفونت زود پر میشه، iMole می‌تونه حسابی به کارت بیاد.
🔍
این ابزار فضای ذخیره‌سازی آیفون رو بررسی می‌کنه و دقیقاً نشون میده کدوم برنامه‌ها و فایل‌ها بیشترین فضا رو اشغال کرده‌اند.
☁️
از بکاپ‌گیری افزایشی هم پشتیبانی می‌کنه و می‌تونه داده‌ها رو با بیش از ۷۰ سرویس ابری مختلف همگام‌سازی کنه. بعد از اطمینان از سلامت بکاپ، فایل‌های اضافی رو هم پاک می‌کنه.
💻
روی ویندوز، لینوکس و مک اجرا میشه و خروجی JSON هم داره که برای ابزارهای هوش مصنوعی و اتوماسیون کاربردیه.
🛠️
پروژه کاملاً متن‌باز و مناسب کاربرهای حرفه‌ای و علاقه‌مندان به CLI است.
https://github.com/chenhg5/imole
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6253" target="_blank">📅 11:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚀
YPtun؛ یک کلاینت VPN متن‌باز جدید برای اندروید  اگر از محدود بودن کلاینت‌های معمولی خسته شدی، YPtun یه گزینه جالب و همه‌فن‌حریفه
👀
🔹
پشتیبانی از VLESS + Reality، XHTTP، Hysteria2 و AmneziaWG
🔹
استفاده از هسته‌های Xray و sing-box در یک اپلیکیشن
🔹
قابلیت…</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/6252" target="_blank">📅 10:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtVCTql04rigqRNMaxDzJU-GEpTfivtF-MSFG0_sPgjsF15MpxYYXNR0MEPKW_kuZ6pl24bNoPC-VYa4DnE4cP1-8vQ1UL1ukM_SeGyLMxD2E0FWeMpq8Jx7ZMrJVcon0LXFzPORi__9fAvNQvEw-RynGi4R5F1YVnw113OcgmV5sQMz9_haIl_A97K77w-v-IaztjVBpmF2No-uC5bisR1uRXibhP43R2FvmP50jagBX9MA30NrxtORsams7YbMsrzE21XWcmmCPoVGVelj1F5nEOdJ8L5WCPeZCHufJ8kj_iaV0ceM21u7058cObjnk-KhdbwRSzl3MGHSN-wgoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Unlimited hotspot shield vpn method! |  7 days trial
/gen 415464440062
trail→
https://get.hotspotshield.com/trial
zip → 1216
Browser any
Ip usa
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/6251" target="_blank">📅 10:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBO3_8jB-S6ZqrC81m6-pZHL-gN07VeQk18gaKe-xrMMsgVtTL4UH-GAilDTtNikQavqoNIg_JWr6xXfIbtNoPYNwPnuiQ5-L-J11l-2zMP4NiZQ_hdfCTNbwnLtzIPz-ZaFpTiVcjfop6HD6fk04j7Yyp9mmML2b712CThAHInhvULbSZeBs-V33Ac6GJ_XjtuQZDpVSFXo-ep3s8af21zuak70oxas0sHkAF3-2EH8Buv09-kdcSp1FOUyBQ1wSZWMvezz3oI3Wwv4VpZcgEYOoNj0UmuAk_MaTUxP4gJGEfUyzb7fZSC14oAx6Uobwt5IrJRhYp8_YOLT6ks4ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
با «تحقیقات عمیق محلی» می‌توانید پژوهش‌های محرمانه را روی سیستم خودتان انجام دهید؛ رایگان و متن‌باز.
✨
قابلیت‌ها:
•
🔹
جستجوی خودکار در وب و منابع علمی
•
⚡
پشتیبانی از arXiv و PubMed
•
🛠️
کار با مدل‌های زبانی مثل Ollama و GPT
•
📄
بررسی اسناد شخصی و محلی شما
•
📚
تولید گزارش نهایی همراه با ارجاعات
🔗
لینک:
https://github.com/LearningCircuit/local-deep-research
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6250" target="_blank">📅 10:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcRp_7gLZtMTRIrYCe4LVkI8i-IPRncqcPfdXEThe5RWjVGucCVmyqjRdf-8AAt1juFWjAGSxFyfypLAnWtoMS6Z6tRdAAE_fJleUstQpAgAuoCP8UbC42rySQMCDqMtl_F3jgIoob-29rZIt7l6z9fkw1VTQTkY6a37xu0HuHn7yEb_iAYO6Mg5--tyV4CgHcNnjrUGzNVZ-cxlQdAPQDKYtpE14zZE5Zw1nrF8g-VqKj3vnZwutDVfiZiUW7mFlO9KMiqP-HiR31UvL4xu27TT_XfkgHEtqhPpTrTn7F1WbiyfihC9zNO9sKoRSg1_vH3ODh3BuOkTtQX1Mq4bXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
YPtun؛ یک کلاینت VPN متن‌باز جدید برای اندروید
اگر از محدود بودن کلاینت‌های معمولی خسته شدی، YPtun یه گزینه جالب و همه‌فن‌حریفه
👀
🔹
پشتیبانی از VLESS + Reality، XHTTP، Hysteria2 و AmneziaWG
🔹
استفاده از هسته‌های Xray و sing-box در یک اپلیکیشن
🔹
قابلیت Split Tunnel برای انتخاب برنامه‌هایی که از VPN استفاده می‌کنن
🔹
پشتیبانی از پروفایل‌ها و سابسکریپشن‌ها
🔹
متن‌باز و رایگان
جذاب‌ترین بخشش اینه که از روش‌های پیشرفته عبور از فیلترینگ مثل Hysteria2، AmneziaWG و حتی olcRTC پشتیبانی می‌کنه؛ روشی که ترافیک رو شبیه تماس ویدیویی نشون می‌ده. همچنین توسعه‌دهنده‌ها اعلام کرده‌اند نسخه ویندوز و لینوکس هم در راهه.
⭐
برای کسایی که دنبال جایگزینی متفاوت برای v2rayNG، Exclave یا Hiddify هستن، ارزش یه تست رو داره.
🐱
GitHub:
https://github.com/yanisplugg/olcvpn-client
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6249" target="_blank">📅 10:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c54422014d.mp4?token=SeWCNAfZIJj3dSv5c1taWQwYQPdRjH6AfklejXFCOLzlhOY7uSbKbDXqHVAKFXAyihehktuIQu6tmpPa0ddoQMpT6ng_1pzqQh5Wt4h5Qqp4c5j46lTopmkMI_qpBG5UJ5612HKHHJGrc19DmCOSifYjdKnykDUzjMErUasYT6X_Iox6tqXZu_UsS3ES0JmVEii2t4QAycqHLzxX_k5m6jKBrPo63W9rkVj5zKNW646Pu0a7BJ-nvpuua9WG6l4h3Cp9Qee6Cxr2HSmOlLOZiwrGFOdct5tx8hSDXAIDBrJGsTxDZqIVvIF66zRcNRZHPF5Lq0QdpmOEeeqL7mG_0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c54422014d.mp4?token=SeWCNAfZIJj3dSv5c1taWQwYQPdRjH6AfklejXFCOLzlhOY7uSbKbDXqHVAKFXAyihehktuIQu6tmpPa0ddoQMpT6ng_1pzqQh5Wt4h5Qqp4c5j46lTopmkMI_qpBG5UJ5612HKHHJGrc19DmCOSifYjdKnykDUzjMErUasYT6X_Iox6tqXZu_UsS3ES0JmVEii2t4QAycqHLzxX_k5m6jKBrPo63W9rkVj5zKNW646Pu0a7BJ-nvpuua9WG6l4h3Cp9Qee6Cxr2HSmOlLOZiwrGFOdct5tx8hSDXAIDBrJGsTxDZqIVvIF66zRcNRZHPF5Lq0QdpmOEeeqL7mG_0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
تلگرام برای اپل واچ
تلگرام به طور رسمی اپلیکیشن خود را برای اپل واچ بازگرداند.
#Telegram
#AppleWatch
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/6248" target="_blank">📅 09:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eINQM3OpsgRVB9yFR-eHCNTGSRnYBnM5YoM3n6QIBAjQ9fqnHoFsk4hLl8DlR5PiWw3yvP6HdneK6utszbg904y_PK-vwY0QUU0RBG0UgqZhKbFYxTXx38QG1lcie_JvI4oiwGsu3UOm6myoaf-c_coYckruoxYfoy06s2x2EY6UqAqphZC1UFezk462IppAK8TOxvzRCKfTNT08MVtGvasKLru_6M5s5mIiSzG57R0vSw1q4LPlaD3HsmFMWujZRa2BZhBEMLFt-6SjsQiXWopoNvSnN0faiJsd2HRvDULGSe3EpGnCtZ0k_2Gzlf_X3FhFs18pLXq9uNTjkM-M3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک فهرست بزرگ از ابزارهای رایگان هوش مصنوعی برای تست، توسعه و اجرای مدل‌ها
🤖
✨
قابلیت‌ها:
•
🔹
مدل‌های متن‌باز؛ از مدل‌های سبک خانگی تا گزینه‌های قدرتمند
•
⚡
ارائه APIهای رایگان برای توسعه و آزمایش
•
🛠️
اجرای محلی مدل‌ها با تمرکز روی حریم خصوصی
•
💻
دستیارهای کدنویسی رایگان جایگزین Cursor و GitHub Copilot
•
📦
فریم‌ورک‌ها و دیتابیس‌های کاربردی برای ساخت سیستم‌های چندعامله
🔗
لینک:
https://github.com/12britz/awesome-free-models
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6247" target="_blank">📅 09:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">💻
NekoBox 5.11.18 برای ویندوز، لینوکس و مک منتشر شد
🔹
یک کلاینت متن‌باز و قدرتمند مبتنی بر Sing-box برای اتصال به انواع پروتکل‌های ضد فیلترینگ.
🔹
پشتیبانی از VLESS، VMess، Trojan، Shadowsocks، Hysteria، TUIC، WireGuard، SSH، Tor و...
⚡️
🔹
دارای حالت TUN برای هدایت کل ترافیک سیستم.
🔹
سبک، سریع، رایگان و بدون تبلیغات.
🔹
گزینه‌ای مناسب برای کاربران Clash Verge، Hiddify Desktop و v2rayN.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6246" target="_blank">📅 08:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">vless://5dcf2dbf-3e82-4456-8961-287cc732bb0f@85.198.20.217:12817?type=ws&encryption=none&path=%2F&host=Play.google.com&security=none#Germany%20Hetzner-.
10 گیگابایت تانل المان</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6245" target="_blank">📅 03:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pV1dex4jgb_-Jpa-1Ku1ZWH-ssfDh54U_BkIlykHeFxGoAbaZzzmG6k5ourFdBBlxdBAkuxHt68KmNVPF7XMLz16RPhLRfi9Cd1ume0x6UQwhszMOeCUIS0l8x09cpAtGl5uLxt81E4CzMv_vZ0xbtaL3qksubzr4fPCJjcpT81C0Bd3ajql9s63iHZkKT-Hsnwjr0IG-lsV75xDhX5mXbJO0gD1moyLX3FFnTdQl3ckTCLNOv0Hr1B6yPP_CbJdCQgQwrh95gn4RTZUFQfutm_y9Ge4lLpLf1cK_Lcm8G_qUt6444Ah7vxLtFcD9B3QTHBRqoCqkCK0ziQke2Px9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله
😱
💻
اگه با 3X-UI کار می‌کنید، یه پروژه جالب به اسم X-UI-PRO منتشر شده که کلی از تنظیمات REALITY و WebSocket رو خودش انجام میده و دردسر راه‌اندازی رو کمتر می‌کنه.
🚀
🔐
این نسخه Nginx رو هم کنار 3X-UI میاره، SSL رو خودکار تمدید می‌کنه، روی پورت 443 کار می‌کنه و حتی برای مخفی‌تر شدن ترافیک از بیش از ۱۵۰ قالب فیک استفاده می‌کنه.
👀
⚡
از Sing-box، Clash Meta و Cloudflare هم پشتیبانی می‌کنه و برای Ubuntu 24 و Debian 12 آماده شده.
🛠️
اگه دنبال یه پنل کم‌دردسرتر برای REALITY هستید، بد نیست یه نگاه بهش بندازید.
https://github.com/mozaroc/x-ui-pro
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6244" target="_blank">📅 03:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hala Hey _ Live In Concert</div>
  <div class="tg-doc-extra">Armin Zareei _2AFM_</div>
</div>
<a href="https://t.me/archivetell/6243" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">امشب رو با این معما بخوابین
شرکت در کنسرت این شخص، از نظر اخلاقی، غیراخلاقی هست؟
#Moral_Dillema</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6243" target="_blank">📅 02:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🫠</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6242" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6WTVSryWvgxx0sbMjkCs9LcMcqldloTmfNQYxedlO6VwntKde5nPu4dUIxpqlLTuNgewCF_KsW_a-f6ekbj7D3PdflVx-oK7U43eTCIi-2sr8lKyh6SQDWETazJlOm_F3-p3L15X5DrafaL2VyRhCoGprt42F3X8lJx0SU9tb5-fsqlKIhpgEd6y8QDWkdb0A35mGAAL2PexmFuMC5S-5KBJRiqV3hGk9Z1Z1p_UTUIBnv_KY_45ousevNA8HEAqUkJPaKE71uuSzg3WRrBYAWQdDvwZNg8hXh6mvqx4YWTyicUUTZzDME9Otpdx3ODxgOCF-OGz87hToU3wiNR8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
Gemma 4 بدون سانسور منتشر شد!
🔹
یه نسخه دستکاری‌شده از Gemma 4 اومده که تقریباً هیچ درخواستی رو رد نمی‌کنه.
🔹
روی سیستم‌های معمولی و حتی آیفون هم اجرا میشه.
📱
💻
🔹
حجمش کمه و با Ollama و LM Studio هم سازگاره.
🔹
جالب اینجاست که با وجود حذف محدودیت‌ها، کیفیت مدل تقریباً مثل نسخه اصلی مونده.
⚠️
طبیعتاً دیگه خبری از فیلترها و محدودیت‌های امنیتی نسخه اصلی نیست.
👀
🫠
..
#Gemma
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6241" target="_blank">📅 01:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
بی رفرال
🤐
🧭
شرط دریافت:
کاملاً رایگان (بدون دعوت)
👥
کاربران دریافت کننده: 140 / 140
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6240" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">https://t.me/ArchiveTellNews/212
🤨
🤔</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6239" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6238" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app
بخونید نظرتونو بگید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6237" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">StormDNS
a.cyntarix.com
25ffbc77bcfb23b2d4ee225eedcd2466
داشته باشید اگه نت قطع شد</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6236" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این پروژه پایتونی جالب هم برای تشخیص اشیاء توی ناحیه مشخص شده کاربرد داره مثلا طبق مثال خودش که با QWEN ادغامش کرده یه نفر با هودی اومده توی ناحیه مشخص شده تشخیصش داده و به گوشیش نوتیف فرستاده و گفته چه چیزی با چه اطلاعاتی اومده توی ناحیه.
برای دوربین مداربسته خوبه یه ناحیه رو مشخص میکنی هر چیزی اومد توش بهتون خبر میده،کد اصلیش با پایتون نوشته شده و از ابزارهایی مث ffmpeg برای مدیریت استریم‌های ویدیویی استفاده می‌‌کنه.
github.com/roryclear/clearcam
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6233" target="_blank">📅 00:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6232" target="_blank">📅 00:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هر کی 99 تا رفرال داشته باشه ی کانفیگ نپستر میدیم بش
😌
🔥</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6231" target="_blank">📅 00:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6230" target="_blank">📅 00:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
نپستر
😎
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6229" target="_blank">📅 00:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nus5mIcBsm-rBoy-nCfKW7h_psBr9Fu7Yth1lH6LTfncTR5yngACodxnb6g_YHYgvNzCTnVHnFSpgfoijRFUeM2KQ-JzGfsdt5Wt6JOQBrqu8ri1jI_8MK_Q5viE73nvl1kt3EVw1YhrLVqkdl43kbQrW78Zu7bt5pvRRH7IKzHON_YpbaviFAhMOlAzVXtcgZNEhvpX0xuxw7fC-Ddy-SSDGzoe0b1ULIpkr1RfmLWTfRsOGpr5aUVVRiIOjGJeGC53yOYMg-b3Q6kL43IP7GZTy3nxcx6XREetDYQWR5LwMJLSQR8_kgD0cfc1KY7SefcG7mG-OidZb2TuY2kyQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Gitdot؛ رقیب متن‌باز GitHub که با Rust ساخته شده
🔹
پروژه Gitdot توجه زیادی جلب کرده و به‌عنوان یک جایگزین مدرن برای GitHub معرفی شده است.
🔹
این پلتفرم از ساخت مخزن، Push/Pull، ریپوهای خصوصی و عمومی و مهاجرت از GitHub پشتیبانی می‌کند.
🔹
رابط کاربری آن با الهام از ابزارهای CLI مانند Vim و fzf طراحی شده و روی سرعت و ناوبری با کیبورد تمرکز دارد.
⚡️
🔹
قابلیت‌هایی مانند Pull Request، Issues و CI هنوز در دست توسعه هستند.
⚠️
با وجود استقبال کاربران، Gitdot هنوز در مراحل اولیه توسعه قرار دارد و فاصله زیادی تا رقابت کامل با GitHub دارد.
🔵
@ArchiveTell
| Bachelor
⚡️
https://gitdot.io/</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6227" target="_blank">📅 23:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🛑
پایان uBlock Origin در Chrome نزدیک است
🔹
گوگل آخرین راه‌های دور زدن محدودیت‌های uBlock Origin را مسدود کرد.
🔹
پشتیبانی از افزونه‌های Manifest V2 به‌طور کامل در حال حذف شدن است.
🔹
فلگ kExtensionManifestV2Disabled نیز از Chromium حذف شده است.
🔹
مرورگر‌ های Edge، Opera و سایر مرورگرهای مبتنی بر Chromium هم این مسیر را دنبال خواهند کرد.
⚠️
نتیجه: نسخه اصلی uBlock Origin به‌تدریج از دسترس کاربران خارج می‌شود و کاربران باید به uBlock Origin Lite مهاجرت کنند.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6226" target="_blank">📅 23:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=F0y89XX8VSVOUmSSdABEpLvOZOfx8zQSsib2WHky4uGgi7b9SKB2agrUQO2VAo-I1KnksIrWzJhVIzrVfkVtRnstLTrsOvaibEysNVqmLWGOfrKyNaCty62Ro613YrCfX_3vtn9F_3KUINKg0zwddW2qb_bC3FwtL6br0YObUW_IH3ekOSVLbaic_D9fsXZ3K2bXelXXRxUizQt7kisE0OIcWBGMJUAxe7yJicx12GqzdG6hAkl8dQni8Zl6b9uU51VeO57VN_mWaBCPZr-zwpSJhI2IenmlSvKaBau5cFqQDfes5jcvPTOmBajzPu5MZobDP-u2lrl6VjppkQolVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=F0y89XX8VSVOUmSSdABEpLvOZOfx8zQSsib2WHky4uGgi7b9SKB2agrUQO2VAo-I1KnksIrWzJhVIzrVfkVtRnstLTrsOvaibEysNVqmLWGOfrKyNaCty62Ro613YrCfX_3vtn9F_3KUINKg0zwddW2qb_bC3FwtL6br0YObUW_IH3ekOSVLbaic_D9fsXZ3K2bXelXXRxUizQt7kisE0OIcWBGMJUAxe7yJicx12GqzdG6hAkl8dQni8Zl6b9uU51VeO57VN_mWaBCPZr-zwpSJhI2IenmlSvKaBau5cFqQDfes5jcvPTOmBajzPu5MZobDP-u2lrl6VjppkQolVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6225" target="_blank">📅 22:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-W92hTGA_85w_SBXLW34ubtmFcHXtAGJk2PriHJ7c0W1MfWqKd8ST5T0FCB82z0S4PGR0rACCNFI8GrOP6WlL3DbbR7T3rjCO6KMLEqnSSK0n9hcDEs5quj-zBubPsjRDHF3nFWjR5hfho0M-QHraPexzACmG4zE7TIry_XSMYm3Mo3nrwsorIU9_n5CovLbAR9Ic3d9WSeGy_HXjr1qkmYFDPzv9zOja9AeJAMRn-3KMGd8SApceJlq_gCg8VLPro0uxg55lElAfDjFsd5kgCm7M48tlqSWODa3qZsSSLCFtBEtMAc-xgQBM1xnvyR9L0g1maMQ4g-sMbv2e2h0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یک ویرایشگر ویدیوی کامل که مستقیم داخل مرورگر اجرا می‌شود؛ بدون نیاز به Premiere Pro یا CapCut
🎥
✨
قابلیت‌ها:
•
🔹
پشتیبانی از چندین ترک ویدیو و صدا
•
⚡
رندر سریع با شتاب سخت‌افزاری GPU
•
🛠️
افکت‌ها، ترنزیشن‌ها و ابزارهای تدوین
•
📱
قابل استفاده روی کامپیوتر، تبلت و گوشی
•
🎬
عملکرد پایدار حتی در مرورگر معمولی
🔗
لینک:
https://tooscut.app/
#VideoEditing
#Tools
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6224" target="_blank">📅 22:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">طبق درخواست شما عزیزان
تمامی سرویس هایی که API رایگان هوش مصنوعی در اختیارتون میزارن رو مجدد قرار میدیم
✨
Freemodel.dev
🥇
developers.cloudflare.com
🥈
console.groq.com
🥉
aistudio.google.com
build.nvidia.com
cloud.cerebras.ai
openrouter.ai
console.mistral.ai
llm7.io</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6223" target="_blank">📅 21:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OX69lNPvxX8At11JhDG_Sk0t6aLLQCEHzBVMPK9jFcT3bAQ3n7VGV7IXr14pnafxbOLQINT_eY6XwjwglzC-lWchS1EbWPtXAAT8qwsttt80L8I2CyLPYKUe9-c0zSZx01iSaLl2c2BL2AO4oflnw_tyQJvUgXGqYX2mfXWGjgNytK1US2UNktyPRVnq5GnhK3qS-gp8q9ieVtRJFCYNG_zf566hDFZn9bIEiKX8einFd-2mb84p4zHzLVRBE6PAQ-XKsGW6BMoXC-fnEFvwmsenwTtx72vnchpe7SeY_zBL87BrlTeevqn2WtAQQbf3SKxaVR9pdAcSvCUVd9yjeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
کاهش بار اضافی روی حافظه در ویندوز ۱۱ — غیرفعال کردن فعالیت پس‌زمینه Edge
😎
این کار از طریق ویرایشگر رجیستری انجام می‌شود:
1️⃣
کلیدهای Win + R را فشار دهید → regedit. را وارد کنید.
2️⃣
به مسیر زیر بروید:
HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Edge
3️⃣
روی فضای خالی کلیک راست کنید → «ایجاد» → پارامتر DWORD → نام آن را «StartupBoostEnabled» بگذارید و مقدار آن را 0 انتخاب کنید.
4️⃣
کامپیوتر را ریستارت کنید.
پس از این کار، Edge دیگر در پس‌زمینه اجرا نمی‌شود و منابع را مصرف نمی‌کند.
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6222" target="_blank">📅 20:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">walf.zip</div>
  <div class="tg-doc-extra">12.9 MB</div>
</div>
<a href="https://t.me/archivetell/6221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ℹ️
فایل سرچ پروتکل و سرور ویندسکرایب
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6221" target="_blank">📅 19:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚀
برنامه WALF منتشر شد!
اسکنر خودکار سرورهای ویندسکرایب نسخه PC
اگر از عوض کردن دستی سرورها خسته شدی یا دنبال یه راه سریع برای دور زدن فیلترینگ میگردی، این برنامه دقیقا همون چیزیه که نیاز داری.
کار برنامه چیه؟
برنامه WALF کاملا خودکار و بدون اینکه نیاز باشه کاری کنی، تک تک سرورها، شهرها و لوکیشن های ویندسکرایب رو روی پروتکل ها و پورت های مختلف تست میکنه تا بهترین و سریع ترین اتصال رو برات پیدا کنه.
👇
چطور کار میکنه؟ خیلی ساده:
۱. فایل برنامه رو از لینک زیر دانلود کن و از حالت فشرده درش بیار.
۲. فایل walf.exe رو اجرا کن و دکمه Start رو بزن.
۳. تمام! خود برنامه اگر ویندسکرایب بسته باشه بازش میکنه و شروع میکنه به اسکن کردن کل شبکه تا بهترین اتصال رو برات ردیف کنه. (فقط مطمئن باش که قبلا توی ویندسکرایب اکانتت لاگین شده باشه).
لینک دانلود برنامه سرچ خودکار پروتکل پورت و سرور های ویندسکرایب در پست بعدی
⬇️
با تشکر از چنل
@CubicDreams
که زحمت کشیدن ساختن
🙌
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6220" target="_blank">📅 19:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خب یه پست اختصاصی دیگه داریم این فایل رو خیلی جاها میلیونی میفروختن در حالی که رایگان بودش یکم دیگه پابلیک میکنم
🔥</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6219" target="_blank">📅 18:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXFnJREewastSmHimtScUCLsHMpNqEIjpdT4IeCQiT07CFEjSfBHpEfmjTokCJhiFgF6-r9dw1fJoubWNUliBlUBhKEAs1a3Hm7CEndpU296MxUI9POJRtBLCsaqMRn5mXJC5vrB6LqYyfuP76RvGIeuzevXNtBufNeAQkolnZRrKXJbrMiB3GzWsY5vN3gs532Ttb5Ou3QbP9AA8a1OyxnEyPXtpldtPeWbBcsoimS2oqwWVnAihWu081j9bGXmESWK8ykpH44fBO8XebyEk4WLr5jquNMbS5NDynZwm-Vdiof0pTnNkdkt29TuWHEbQR6v5dzb2fSP72buKDaMIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دریافت API رایگان GPT-5.5 از Freemodel  اگر دنبال دسترسی رایگان به GPT-5.5 هستید، می‌توانید از Freemodel استفاده کنید و API Key اختصاصی دریافت کنید.
👇
📌
مراحل ثبت‌نام:
1️⃣
وارد سایت Freemodel شوید.
2️⃣
با حساب Gmail ثبت‌نام کنید.
3️⃣
پس از ورود، صفحه احراز…</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6218" target="_blank">📅 18:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⚠️
اطلاع رسانی برای افرادی که اشتراک ویندسکرایب پرو خریداری کرده‌اند:
پروتکل
ikev2
روی تمام لوکیشن ها (تقریبا) متصل میشه
✅️
با تست هایی که گرفته شده با فیبرنوری مخابرات  سرعت همه سرور ها دانلود ۲۰۰ مگابیت و اپلود حدود ۵ مگ فعلا قفل هست
(پیش‌بینی میشه پهنای باند ikev2 کم کم محدودیتش برداشته بشه و به قبل شرایط ۱۸ و ۱۹ دی ماه محدودیت شبکه برگرده)
سرعت کانکت شدن به سرور ها و امنیت ، این پروتکل خیلی بهتر از tcp هست حتما استفاده کنید
👌
@ArchiveTell
🔥</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6216" target="_blank">📅 18:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ArchiveTel
pinned «
ArchiveVPN | کانفیگ رایگان
📝
کمپین: نپستر
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/6215" target="_blank">📅 17:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚀
دریافت API رایگان GPT-5.5 از Freemodel
اگر دنبال دسترسی رایگان به GPT-5.5 هستید، می‌توانید از Freemodel استفاده کنید و API Key اختصاصی دریافت کنید.
👇
📌
مراحل ثبت‌نام:
1️⃣
وارد سایت
Freemodel
شوید.
2️⃣
با حساب Gmail ثبت‌نام کنید.
3️⃣
پس از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
بخش اول: احراز هویت با شماره تلفن
🔹
بخش دوم: احراز هویت با تلگرام
✅
گزینه احراز هویت با تلگرام را انتخاب کنید.  لینک ربات تلگرام برای شما نمایش داده می‌شود. وارد ربات شوید و استارت را بزنید
🎉
پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار  هر هفته: ۶۶ دلار اعتبار
💰
4️⃣
از منوی سایت وارد بخش API Keys
شوید و یک API Key جدید بسازید.
5️⃣
در بخش Docs می‌توانید مستندات کامل استفاده از API را مطالعه کنید.
🛠
تنظیمات نمونه:
model_provider = "freemodel" model = "gpt-5.5" model_reasoning_effort = "xhigh" disable_response_storage = true preferred_auth_method = "apikey" [model_providers.freemodel] name = "freemodel" base_url = "https://api.freemodel.dev" wire_api = "responses"
🤖
حالا API Key و مشخصات بالا را به هوش مصنوعی موردنظر خود بدهید و از آن بخواهید برایتان کد تولید کند:
✅
JavaScript
✅
HTML
✅
Python
✅
PHP
✅
Node.js
✅
و بسیاری زبان‌های دیگر...
💡
می‌توانید با آن:
🔹
ربات تلگرام بسازید
🔹
وب‌سایت طراحی کنید
🔹
ابزارهای اتوماسیون ایجاد کنید
🔹
پروژه‌های هوش مصنوعی توسعه دهید
🔥
فرصت خوبی برای تست GPT-5.5 بدون پرداخت هزینه است.
@Archivetell
✨</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/6214" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
نپستر
🔥
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 60 / 60
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/6213" target="_blank">📅 17:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کانفیگ ناب اهدایی
💎
hysteria2://5z15av99psrlhdqp@32.195.51.20:39150?alpn=h3%2Chttp%2F1.1%2Ch2&fm=%7B%22udp%22%3A%5B%7B%22settings%22%3A%7B%22password%22%3A%22dlxmzvxvcp3i6v0e%22%7D%2C%22type%22%3A%22salamander%22%7D%5D%7D&fp=chrome&obfs=salamander&obfs-password=dlxmzvxvcp3i6v0e&security=tls&sni=32.195.51.20#usa_hesteria-%40u2vpn-100.00GB%F0%9F%93%8A
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6212" target="_blank">📅 15:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پروکسی‌های اختصاصی آرشیوتل
😎
⚡️
پروکسی ۱
🚀
پروکسی ۲
💥
پروکسی۳
💡
روی لینک بزنید و گزینه Connect را انتخاب کنید.
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6211" target="_blank">📅 13:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqJ7sbu8SaCSunsudoFQifljjA_AZHvqfrEHQh_E1n6mVuG4tArGsU2C5KqDAKuUYmA8g-76B3X0Kb2RpTt86LnIaKigpZmOttMaXiDSNkC6DCCRDGRyYpFVj0YzUBOXB9JXolMhbThKuyTSiCHZM3SEnYQLA5dROz8qJJmx1TaxaarxnTEhr0lAbpCkjTJvif9U4bDVchUtE6pE8Ie5FJr8QDLbT0OgUa5CXUOFMHHW--DpP8NtlcWzVOeuSE2odmnXDjgxUpkgh_RwSqo9fIWcmPuGPoZhWrrbL7YLTJ7_wS6Nxu4LCKkgS_c1tncMtg0xYSVYASDA1MWXtdyqug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینداسکرایب یه روش مخصوص ایرانی‌ها اضافه کرده، رو همه اپراتورها عالی کانکت میشه:
Settings → Connection → Anti-Censorship
گزینه Protocol Tweaks رو روی Enable بذارید، بعد وارد Configuration بشید و یکی از دو گزینه آخر که ایران هست رو انتخاب کنید. گزینه Large TLS رو هم روشن کنید.
پروتکل های udp و tcp رو تست کنید
ایرانسل tcp 587 france
مخابرات همراه اول udp 80
با فیک میل اکانت بسازید
https://windscribe.com/signup
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6210" target="_blank">📅 13:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNq4S3PWUD_5WUEAwuK8Ba5w-OoumBeKQalurSfm70uImMAeV6Q00aprlJ83sCSJE7W1jzqgpBHu0tAU56yUPV7cbwta-EE7TwNYFAp3GVvoeiieTq46vUj2s8-LxCrq84LGtmQzG1jwJtRY73HWZocpECXACUIMUxgt4Le54B_s4_NeR4HY2OV-6qeWX_J8nTtoz2x9-gEIrKHCqoqwGe-hUmT5PHLakA23PVcYtJk5PK3lzKlb2X92wJbFE8V_7lej_aDjVgbM_5iqom4txx9sAz7b4ONEeAa-RUkvbZdmBuipbPZ61jPSDctZZmZD8_N5PQsYDlPjCRdEff0HMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
Impeccable
‏این ابزار به عامل های هوش مصنوعی کمک می‌کند تا وب‌سایت‌های منحصربفرد و بدون الگوهای استاندارد ایجاد کند
🔥
‏
✨
قابلیت‌ها:
‏•
🔹
آموزش عامل‌های هوش مصنوعی برای ایجاد طراحی‌های منحصربفرد
‏•
⚡
کار به عنوان منتقد، توسعه‌دهنده front-end و نویسنده UX
‏•
📊
آزمایش ماکت‌ها، برطرف کردن خطاها و بهبود طراحی
‏
‏
🔗
لینک:
https://github.com/pbakaus/impeccable
‏
#هوش_مصنوعی
#طراحی
#OpenSource
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6209" target="_blank">📅 13:00 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
