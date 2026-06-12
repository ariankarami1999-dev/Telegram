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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 00:32:11</div>
<hr>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=aDySov2OK5vZ-2nQgaKflGUcEfEq4Q6J7TBpUgAX8qQUlda64fr2MCuCZuN4VEmLI-dBmqUQD8OuJ_SjKV7svMLhQsQaC7TpnCu5unfQ0mW3YN63AMim6GRJ_J5bGPke6FeUiARXeHkChU8gYrRNTadpNckON7yuicxTmQOW6bxa0BNZhQFFsYnq1VQv5c_fDVlOzdEOeYVKnkYrCm0ru24_FVcV2GQli5r_8zglbWE31wXfXvUQXsy9dfWpMIGor-swkQFZlsGKt-EQLoNHr__GSFx1CTP9Pq-slkWCBhOJWXe8Q6wz4ZUq7a_4In2Q1zhA5Lsgpkc08VE1UGYJug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=aDySov2OK5vZ-2nQgaKflGUcEfEq4Q6J7TBpUgAX8qQUlda64fr2MCuCZuN4VEmLI-dBmqUQD8OuJ_SjKV7svMLhQsQaC7TpnCu5unfQ0mW3YN63AMim6GRJ_J5bGPke6FeUiARXeHkChU8gYrRNTadpNckON7yuicxTmQOW6bxa0BNZhQFFsYnq1VQv5c_fDVlOzdEOeYVKnkYrCm0ru24_FVcV2GQli5r_8zglbWE31wXfXvUQXsy9dfWpMIGor-swkQFZlsGKt-EQLoNHr__GSFx1CTP9Pq-slkWCBhOJWXe8Q6wz4ZUq7a_4In2Q1zhA5Lsgpkc08VE1UGYJug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
ClaimCircle
با یک کلیک، خبرهای جعلی را شناسایی کنید
✨
قابلیت‌ها:
•
🔹
تشخیص خودکار متن، پست یا تصویر فقط با کشیدن دایره
•
⚡
تجزیه و تحلیل لحظه‌ای محتوا و نمایش نتیجه در همان صفحه
•
🛡️
حفظ حریم‌خصوصی: پردازش در مرورگر، بدون ارسال داده به سرورهای خارجی
•
📚
پشتیبانی از چندین منبع اعتبارسنجی برای نتایج دقیق
🔗
لینک:
https://chromewebstore.google.com/detail/claimcircle/ominadfbilailbklmclcmdbpmckckdad
#claimcircle
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 702 · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 755 · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQMAncRMh-an4B5UuT-AOpJNtGkGQvQL4QTZOM0CBQbh7CmH2IIP3Cn1vVgJng1COt6N0vwHo6tFYQP_6kFWrr9D13JCd-50PsGcj3Vd4zx_B3apjgokQlvOZG34XzGLnsjWSc7_kRLhqsvlCcIqu9OLdsu07qycoOv4jA3Xh9siyBftmf_KnbejVzWzy9A9iszPk3b2Rby3X71rnfGmNX50ElwJ9lREliYR44rveCpNa2zqQxEbI4Jf2lkVi8DORnrFGwZoCgX3QdVZ_rZYeDdOJyHSGWNUM7nw-35fwn3S91sO92JO1_tHKVSaQVAD7kQUuHzr8qxTiCXjL7-L-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
پخش FLAC با کیفیت lossless بدون محدودیت!
✨
قابلیت‌ها:
•
🔹
دسترسی به کاتالوگ گسترده موسیقی از تمام ژانرها
•
⚡
دانلود همزمان چندین ترک با سرعت بالا
•
🛠️
ذخیره فایل‌ها با وضوح اصلی بدون فشرده‌سازی مجدد
•
📦
پخش مستقیم بدون نیاز به سرویس‌های استریمینگ
🔗
لینک:
https://flac.music.hi.cn/
#Music
#Flac
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/archivetell/6327" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/archivetell/6326" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/archivetell/6325" target="_blank">📅 17:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/archivetell/6324" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/archivetell/6323" target="_blank">📅 16:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/archivetell/6322" target="_blank">📅 15:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lB9pQwJ0oyB1rqzGz2wujl-JegkiCJSL9A-Z7yGMfi_8LnOlW2PqEE9kpRz8ThvuXOVwL78xV1snH5S3Fk1HURjVj93m2ZlBSBa9TApybguTbdcNE-tI2eho1MscIicloR4pQ64BGg3IlQCVh4ia4lZ1pg2KedVjStS8twCiCN4Emgnu5U28xWKYoU8ufdhicm-MYNk0TsIOWZjd7x5ShKHFRHuA0nsmb7TBnLG5SMCCtZGvBaR64ejLhNRcCQ3ykN6eUSR51R5UewpJd_REKB77p4TrzTeZ3y_xKCiPNd9HEEdT8ULvGK5yR1I26yKNjSoCeQetCfG6_Z_uzpwjjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJacJNxbQQ52UgRAe7DNtbaVwm0LC0zB9nouSV66GpzmMldnQxDBWsNga-mrymKD4Gy4_2SaBxXZF9GdL9jRqm6xkPALFpPUeAtTtV6EBoAH-51bST7r-SMq5RoGLzIwRlkhdXwzrMZGGMZ9qV9d8UpWdwzHtRbK7QefkpXoJml8Smine9_eTtBXNrjEf8RNF26vlYS48BHU0nBk3U6I96o99GVBY0QQyOqbOW8a7DreD0Jzgk65Luu8iHvv32kUV2akDamh2guic8UMKRP7K2yv43F5h9Izpq9u27cPhTgvR-cpbaukggSfcmjF5lMOiVV3DHy4q7bQjO7xwtgm9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pf2Kn4TryTdYnyUfzbfeMdZK2xV-3siCmoaaoameMgrne6fFXuFkxRm8FFNaVsQjIkNxYpeWKTjxAsIzpmcmTUOsO1_SuWiKURKRCfAy4bRHo0XnL-nCOuGneXewGWLozGokeIusdnZuOa6nVYtv8Qo0UNOLdH7RvadB8EP1d_CSLIkBk27odn2BZrSdDY8D9EYod9IdwW31Ff3JHs-aAA4vYnaEIMmvC1rsh28d1gWx1nLYeZ4TvV1bqIoEqNfWQckmXPQ4PxFtNiWxVOjOdDtS7teLgliXsui1iS36si63q1Xl6I9L8jl7MU-whOn1TLc2_AXkv2YdyfBqEdHwdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/6318" target="_blank">📅 13:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6317" target="_blank">📅 12:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6316" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/6311" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6310" target="_blank">📅 11:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/6308" target="_blank">📅 02:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgR-kNqpgAsyyYdDMS8WDr6RFjqR7YTIUlDIhNrsCe7Rk3K0WyhbZP_Fv2uiZcJHKxo59k6wywu7Yt-lNgwK38bk55LwdnS0ItyqOYgR4C93C-wqMJ2A3ts3jlGvtbXIj16w4dXuk66sHR8han8aRO2n_r4CHOr2r9zzoV8rCZVL8997CKVLYReR3ZgIdHbMF0aRIdXdHBssTL9QZfaoim9Oj5FvZhB4QAF1WQQC7hVAxih9EIyNS7S0eeHXg4b3-duNwsRLW-NY4jPwodEgKpM4P1dCcRE846QSVBhhxnQQYnwimzkoaAbAdgykGFWH9az23orWbBPwCWDkkIm8Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6307" target="_blank">📅 01:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مرحله یک طهلیل من به واقعیت پیوست
😝</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cua1end67Tt-w7Q3UpMvhWHQwUCOXap1DeU7kxBAE5AawEDYQlqV_GUJOl7X0L9BMCPDjYeEOEsEBQDwdn4nnzcCg5peLX0DcaZBkuqcssm8jQiAjLC8A-M0DRTgIfwgB_HZV7F7JWzlM3EU6o4mNnX2xVKG-gp1nhXEOSzvYvu6p9QJoWjvgdBDmvEEmJPaA6YddH0byTPVhj9oTihwpfyaeppccxKHrzG-LbNiHMaGil3ziAHMu9tu7xSeZwCayCgm5rZwiYrmV3n_mVo13X3oOU4BSnoHlkRCTtDPd72EyuZ85DQlr6jHHIXaNguHHeW0Uj0BZPXF_CDbwBPALQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):
Aistudio.google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6304" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6303" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6302" target="_blank">📅 22:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUMZRigz88JN-rE7fjcOFUyYkzj3ra0HmmIWFdP38V88PWY76-4sdTO2Hs_A6S82iD0tStkpe8TamxxzyyNHOUqiZVSXmAjuX2LJ1x571p2d1_uRtNF5j7sHO-Kioz1OEP-cqZIap83QhD-634HlluZKOHaCyFEYzMfZj4tbU-DSih-veXMQcYAs7dJpOiD4udAlopifC4lp8okxd1CaW-4g3V4bcn8JDrRoGJ8CFmnSp79WPi8II3gniiSXRurwa_B-mOqJReAsGHi7Rd2pDl_NlOwo5jq4Nh5FbC_fL741Us1Kz-5nDRcT5u3Kvs_dR8wEcerQJAaCV8gHS2uafA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6299" target="_blank">📅 22:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/archivetell/6298" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=jBaUPT9jLUrmq5EztHAnPXjOp2AEKanKP0YU5NrjZxna1NGbCJzWQK8g3ce0iEtSl92_UNXKCB9DJULfW2-8TX00_ieufWqQFgWWCPASxbLeo8dbv7iJqBDQDTuXo0x_6D_FJxT-1AiCMw52XYp52ZTtZhetuHwLbWzuBI5pm5XldRT2WKcAFYIv7V9-subpTsQJtL3QqrJ4k13n9O91waSfZtw11G7oRekmZ8TJFBr1tGLAsMc38GYasp0klRfmOzR09_tgCNp8NvmnYuE6b2J69_qbyf-4AQmgGqOzsx_bB0rmXzCOsJKKIUtAlPSMwE2Eci__IXYvJRQJnMWe9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=jBaUPT9jLUrmq5EztHAnPXjOp2AEKanKP0YU5NrjZxna1NGbCJzWQK8g3ce0iEtSl92_UNXKCB9DJULfW2-8TX00_ieufWqQFgWWCPASxbLeo8dbv7iJqBDQDTuXo0x_6D_FJxT-1AiCMw52XYp52ZTtZhetuHwLbWzuBI5pm5XldRT2WKcAFYIv7V9-subpTsQJtL3QqrJ4k13n9O91waSfZtw11G7oRekmZ8TJFBr1tGLAsMc38GYasp0klRfmOzR09_tgCNp8NvmnYuE6b2J69_qbyf-4AQmgGqOzsx_bB0rmXzCOsJKKIUtAlPSMwE2Eci__IXYvJRQJnMWe9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم ملی ۱۹۷۸ ایران، فقط یک تیم فوتبال نبود؛ نماد غرور، اتحاد و جسارت یک ملت بود نسلی که برای اولین‌بار نام ایران را در جام جهانی طنین‌انداز کرد و نشان داد که می‌توان در برابر بزرگان ایستاد.
از ملبورن تا آرژانتین، از صعود تاریخی تا تساوی مقابل اسکاتلند، این تیم برای همیشه در قلب تاریخ فوتبال ایران جاودانه شد
❤️
یادگاری از دورانی که فوتبال، فراتر از بازی بود، یک رؤیای ملی
✨
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/6297" target="_blank">📅 20:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmhCZdBUoFG_ap0GPfaUzHMisWIJPZBoT5G1dCS99IRS_ziBdj5UioEBsvPfM1ecxAmoiU6dtKp3Oj-8CtSBbTUGh5td0eb5_v0orDzzDbjv1MBPFzRbbuDdHCf-5AuL1_o6FW_oyUFlrFmdrwCb6Yqy3RnTw8qSSM-lTIvCrH9KXjz6HxM7KrVKHHhBE1QrW7vubz3xEamkmBsW6NIH49TNbHiFzQ6-dJXS8btRyBSzQWQUNnPJJVyy33fcr3zOqihLdnb3taTdSJCFmnireqxjuq5Qy64lYlcQ34I13FexK9jkIfrWvEEe0rNsF6xdmjgwRxnBAm_VzCJxyRJvpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6296" target="_blank">📅 19:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اگه میخواید به سرورتون وصل بشید ولی مشکل وی پی ان و این چیزا دارید و روی cmd و ترمینال و این چیزا وی پی ان سیستمتون کار نمیکنه میتونید از ssh آنلاین تو خود گوگل کروم استفاده کنید.
https://webssh.webhorizon.net/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6295" target="_blank">📅 19:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/6293" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbgFtk4dvl9uKPUSt26dbngm2Dy0T8kcIOnX8FSB6H8VAGK1YEXEf570h0X07ew0a-o1MpYmDwK986ERxTgN0epg3VupUmVVHAZs5H9qL5QRgZVEd4CZKAE5_F1AjLeE9IlLkrdtBmao9Xoim-OYaXYPH7nYiLfdVDRFNmTM7ukzAkBxPUEieAeSa3OeBwYkEEsaQbYWhW0WLH-mtNlM2K47bTBtNqtQdO9NPcBUcBjL4E-5oaHF5khro5Wj1ZHhw4UtL1W_rbpNdZPFzx_1l9S98t7kM3zApgVbqudDuENYCz3RUwAfQ_F7Skc4yVteCl9AmRS-SCbQ0NIMnB9mNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ch5B85JC3Ttb8mLOQnAsT9wSLKj_cKYv3vFbI-Krr-R8AHA2Xf8_kpe1bf2d35EFh5pUS_uBzDrx5telroYvrEtXggl9fjnfLlYMIf2349phWPml19VJ90hVINDhLZKpFGX4GzeSMI5gJp581ZpCVUO-4qYDQGsGbI8hH3Ty7HBuQ4KVUfNAGzepXeLcAUWy5zZwC_onGBE891n8Fo1SWaINzYXPnwSrUGztI5d7MANfIN_c70r9vOcMH6Gjt1Jo1PhkLs2yYT3AkYwjNK2jvq-tbpNT4_2WdjvDbreYIk7BUFiDEer9txUj_3WutJ74YCwxW1VvQqIu3WUV1YCEeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rhFN03W48tj83dDWr9UHOelgQ6GeeXYX3qqeeBKCFr_SEcxkeFrBitc33njA15RRDz4j_BfZA9qxZ1nxE_sYigQWWyaGnAfKD70YM3VOBXEKVDBXgmPwwJozK3H7apNHR9b5CaCtEqo1ic4RpuQycjZcASTidJHfUp32hJkk7GQary0TOBKtrcUyogvvgVgkSypggr5GXGntbPMCJ23l7zol_uhvZLLlwMR3Ct0snZOHLE4Y8RGiBtmGWqtchT2Z-eMPK0yBxZGsBAf0OLHdD86ZQUBgWOfobD1zjgTvCPsG1ziXY1bSUiPXzGnv5ZJ1fm2vMGqZZwhYN6u6x7Genw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6290" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=dWwQ6Fx9ud-htRnDc-2Xm08QffkGHzJcnK3rdJOwMbiiw8qLzKSh0MVcRAJAMCW3jaP54Bx-O7gM2uV7nwisJ84OtoCEYlJObZF31y38dzmkmnIXdb3SWoFM5hn9YgQIVAKEEgpMTd_nZe_P98F5q3T8rLakbRFMZqsCFPNKzE8f2jfY8h0imDWpMV1k0CEXxAuJx4QTFsuBl4Csk85hFRrcWZiyttXAy9h5Lf3UAV5isptfAeDe_giyEi9SbyOieM4_N1quow3h6oloHEFOSG5JWJXMDKypsdCy0GThERbOK9p4O3fIpHSGV2GM7lVf3Y3B2xKARm4c11ZPGWX_gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=dWwQ6Fx9ud-htRnDc-2Xm08QffkGHzJcnK3rdJOwMbiiw8qLzKSh0MVcRAJAMCW3jaP54Bx-O7gM2uV7nwisJ84OtoCEYlJObZF31y38dzmkmnIXdb3SWoFM5hn9YgQIVAKEEgpMTd_nZe_P98F5q3T8rLakbRFMZqsCFPNKzE8f2jfY8h0imDWpMV1k0CEXxAuJx4QTFsuBl4Csk85hFRrcWZiyttXAy9h5Lf3UAV5isptfAeDe_giyEi9SbyOieM4_N1quow3h6oloHEFOSG5JWJXMDKypsdCy0GThERbOK9p4O3fIpHSGV2GM7lVf3Y3B2xKARm4c11ZPGWX_gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6289" target="_blank">📅 16:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/6288" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6287" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⚡️
سیم کارت رایگان همراه اول به خاطر جام جهانی (کد تخفیف + پست رایگان)
CUPSIM26
هر کد ملی تا ۳ تا میتونه بگیره (همه رو تو یک سبد بذارید)
لینک خرید
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/6286" target="_blank">📅 11:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=Ge2ekIaxfd9OYaqn2cA3Uf4P3tBcTJe2_eKnRCtapuBVDqac3g13ZCHyiJ1Dj1hBz83KH8Nnk9IpCEauiNCHTJe_6bPygtmtOc1Ee1zCtxOBYcwPJsZXhZwweIEqcpMEqVAaT6I6kMaoha1njs6f3IhFJVhy0k7EGjy_LWiqHSOXvnecEzOCKDaGAuJJkliEIxVkXvPE-vtUSJENJj-ZHgqpSXS87urtrS-WYbFfrlfVruZDgAKvX3ULU8KglO1vZS3PuQIYlSRyxBqnxBA6ddRQ_pzzVTdRBIFXkGGXEMM3xNJzhUfkGuGLsO5uh0OyKeqO0VsYfMdiOM8YojMdqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=Ge2ekIaxfd9OYaqn2cA3Uf4P3tBcTJe2_eKnRCtapuBVDqac3g13ZCHyiJ1Dj1hBz83KH8Nnk9IpCEauiNCHTJe_6bPygtmtOc1Ee1zCtxOBYcwPJsZXhZwweIEqcpMEqVAaT6I6kMaoha1njs6f3IhFJVhy0k7EGjy_LWiqHSOXvnecEzOCKDaGAuJJkliEIxVkXvPE-vtUSJENJj-ZHgqpSXS87urtrS-WYbFfrlfVruZDgAKvX3ULU8KglO1vZS3PuQIYlSRyxBqnxBA6ddRQ_pzzVTdRBIFXkGGXEMM3xNJzhUfkGuGLsO5uh0OyKeqO0VsYfMdiOM8YojMdqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6285" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNHA-3MO0ycGtvcRTER4sZc2st1E8O7k7z_X-OX7UVDZjDzdGeX--503YxAtyy4DMIzCfxA0oQh_mziezubigYqE8MBzXBF3_GOD08VnDQqzWAAEGv-2uJRvHHI84qXfPQfKqIv-P1G0CDIxtXi68OG0NlE_wep03MqandSP6iY3FueXMP-hBSeOGWMd3YO0jU9FzRMcPPXMplJScJpQ19hPBNhaUxyQ9xM1tBQ6WSWVzKd5FM_l2vfZND9-Wz8i6VAILyYryAvIA2uI8jj9P5WoTdl8iY6j9jFn47aAsvBuxk54yxImvt01kJRHpaBeBMOSpH8ATRvirUGO58ulng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6284" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=QbbvZQk550zgMhUX4B1ytVI9bC2WvD1sP_doF8PCm-mFXWm4koN4W354645SjjrhzsrX9uJPcav_oUeLUyU5l5M5suoNfr7cbYSVzR73oNgyvlxPDtY2E29RCw56-wShJAGcGlXTChDlm4UvTUpXeW5_9ifMIVnK-GGHMV5V96OseEMR58KowWXsEA7u07JdeXWAMzKWPadeHQB_vNWHeNl93ER8EKpzx2T-kP2Qj05m48Izz_-EGUao-N7b-tdulbUgLklDZjIY2Dm8A3ufdFkLoqzfYn1qYuBznKDrLFBgRN0V2UOzzPgiKioef_5lwnxnD4NmJStu1XjsbYZ8pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=QbbvZQk550zgMhUX4B1ytVI9bC2WvD1sP_doF8PCm-mFXWm4koN4W354645SjjrhzsrX9uJPcav_oUeLUyU5l5M5suoNfr7cbYSVzR73oNgyvlxPDtY2E29RCw56-wShJAGcGlXTChDlm4UvTUpXeW5_9ifMIVnK-GGHMV5V96OseEMR58KowWXsEA7u07JdeXWAMzKWPadeHQB_vNWHeNl93ER8EKpzx2T-kP2Qj05m48Izz_-EGUao-N7b-tdulbUgLklDZjIY2Dm8A3ufdFkLoqzfYn1qYuBznKDrLFBgRN0V2UOzzPgiKioef_5lwnxnD4NmJStu1XjsbYZ8pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVsFIBZNdXbOh_jBkCpzAOWcO7woOTuPSIl4U6g4MoJTLKcKyEWnzP3glUkgy1CbqXvsLTFiR_-9rWYLrnZr8SDGKFAK3Dz-iRcd26P3B7Z4wW_HXVTD2JkeI_JUz5dJznsOLaDO-D00olLNNX3FZqKmuHUSMW8KYvuFb9eBM_cQ9CJw2o7onzklTmZReNzRxbg5iO6OFkmTRv0Ib5ZfdnDzA33zsjbI1rUhdPTL_XDJ2IEBbfna2n9KxAIwhBR0D7f9ZFjnhPVDWbSttWBKgCW47ZNwCl5BdIZ0_v87DToIAp8eVxhteGQ1ttoIwA605EUTAnapgJPnFNdh4fJhYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6282" target="_blank">📅 08:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqAKtyaCR_g0pUzytOapbU1ZNSy_ATwZ_POkD7eptkRg6ykvysOmeQGpvd5CK6bhDROt5VFV7QV2ATtd9fu1_hdOyQPSuV0PW675yUAth7fxN7NGHuVgiUPUvpoxsfuMMvk6ezyjfKv0ssN1RlIx2YJSpwN6CCvNc86IsNg3TgXkkF76QxgpT7ux3EXTnxAyo69no8N48qf7Im1mYSBCnoiRh2l0D3lPH33T_C_88_cLSeXmvA9umIFWCbI115FcyQEgvlsSnN6mrd3R1iyIXeD3Xh1jcNM_z5vkUl-513WN5eJx6KrkTw20dADyFx7iSPGjXlp7DmY_B0DoBNidPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوتاه اما جالب
❕
به این صورت داخل duckduckgo میتونین qrcode بسازید
🔗
🎁
@Archivetell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6280" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6279" target="_blank">📅 01:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚀
راه‌اندازی خودکار 3x-ui با WhiteDNS؛ از صفر تا تحویل کانفیگ در چند دقیقه  اگر حوصله نصب دستی 3x-ui، تنظیم کلادفلر، گرفتن SSL و ساخت کانفیگ‌های Reality و VLESS رو ندارید، WhiteDNS تقریباً همه این مراحل رو به‌صورت خودکار انجام می‌ده.
📋
پیش‌نیازها  قبل از…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6278" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=t501xWW8bn0rNGyFRwx28U19i-UVp5NCMQo1nqe3CcyXE2MmK8vH-fU0Ebuer_mbHEozcitQhBU8Q5YOLRDtChpGMQIxrlwqNag0Ank-SyRIxMSu-y-brKUCmZVxj59vZvivZnCQzyiR3PZKyt05doszaB7BS5FHeDSg5ZbPeNAuUALHHUNknxIt-ldWMJdXjcAMMIWrKwxfZKUrgdCQz73ashkjJRS7Pl4WXqO2OTgBHuw0etN9Oh0yo5CNtY95gioQ6SWkhYmorjn8aPPfw1W_4Fd3uaXfYXY0LyQBDsVIRuFmKuIpWfO0Qe90_jhT7kfJBGRrzhm-zimYVn1RiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d877e423a.mp4?token=t501xWW8bn0rNGyFRwx28U19i-UVp5NCMQo1nqe3CcyXE2MmK8vH-fU0Ebuer_mbHEozcitQhBU8Q5YOLRDtChpGMQIxrlwqNag0Ank-SyRIxMSu-y-brKUCmZVxj59vZvivZnCQzyiR3PZKyt05doszaB7BS5FHeDSg5ZbPeNAuUALHHUNknxIt-ldWMJdXjcAMMIWrKwxfZKUrgdCQz73ashkjJRS7Pl4WXqO2OTgBHuw0etN9Oh0yo5CNtY95gioQ6SWkhYmorjn8aPPfw1W_4Fd3uaXfYXY0LyQBDsVIRuFmKuIpWfO0Qe90_jhT7kfJBGRrzhm-zimYVn1RiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6277" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=hCi0l3pfJHQee29wbYBvTwT-4b7_0YXG4Yx4EFNRTPCHiWkRpv1iGPYbacm8uyGlF0yIgLn-LFCXVJ23fwnx6QPtsHBxYnVWX8JSZwbFhGNEgrreedbJG0_Q_qvE4ic70WgbXnGz6I625_763nqHzwloApUQWX_RQAqdc22IrVY_QXaeshht49cRFgoe92HqgmNbblRxzI2NZmpB9oD4Ox1M2JRnx5IphPw1nBDZGiOkWAeYBri1AAiRNrEuwGOphIR9XvPfmIZtrJUA0lf0wtTYdi_a4BWcRyeaK2NJhg3VXP2gX9ceokt_cXnRqIBKcgZohszN4m1cOkOWr4Wy7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=hCi0l3pfJHQee29wbYBvTwT-4b7_0YXG4Yx4EFNRTPCHiWkRpv1iGPYbacm8uyGlF0yIgLn-LFCXVJ23fwnx6QPtsHBxYnVWX8JSZwbFhGNEgrreedbJG0_Q_qvE4ic70WgbXnGz6I625_763nqHzwloApUQWX_RQAqdc22IrVY_QXaeshht49cRFgoe92HqgmNbblRxzI2NZmpB9oD4Ox1M2JRnx5IphPw1nBDZGiOkWAeYBri1AAiRNrEuwGOphIR9XvPfmIZtrJUA0lf0wtTYdi_a4BWcRyeaK2NJhg3VXP2gX9ceokt_cXnRqIBKcgZohszN4m1cOkOWr4Wy7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6276" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=T9kdV1WSqL5n5H2Gq4yWpo65sKiqpu0r84I2RU4ydsQhs1hVbx6T1XOfUF_Jwzo1XQQYZNJ_ltX3vvc2tM5ZtfspF2xOHXDkIFW47gxGidJSn00wjOx9vdM_rwxiHmZhcF9hBYj_ag58GY_Y5GQhJq4FdqLbMXgp6gzt87Ml-kpBCxIzMBrLs9-b3fxLqjnQmb7o2IF1vpi7xrVUJGl-yzW0RNUxbhuurDCXBp7kcjq6c9l0S-uCpacd-MCEHRLOfyo0872CNT2m1uvOV7TC_U7whH5UQ3mKr22t6At4xtUULJgVnfsYA1kQlnKw9i5cA8vmIlvlzEL986XzeOoONg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beef8b9c33.mp4?token=T9kdV1WSqL5n5H2Gq4yWpo65sKiqpu0r84I2RU4ydsQhs1hVbx6T1XOfUF_Jwzo1XQQYZNJ_ltX3vvc2tM5ZtfspF2xOHXDkIFW47gxGidJSn00wjOx9vdM_rwxiHmZhcF9hBYj_ag58GY_Y5GQhJq4FdqLbMXgp6gzt87Ml-kpBCxIzMBrLs9-b3fxLqjnQmb7o2IF1vpi7xrVUJGl-yzW0RNUxbhuurDCXBp7kcjq6c9l0S-uCpacd-MCEHRLOfyo0872CNT2m1uvOV7TC_U7whH5UQ3mKr22t6At4xtUULJgVnfsYA1kQlnKw9i5cA8vmIlvlzEL986XzeOoONg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6275" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ادم خودشو باید برای هر سناریو اماده کنه و باید تو پیشگیری خوشبین باشه. چون شاید همون ی روش هم جواب داد</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6273" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">همین الاناس که ترامپ میاد میگه:
دقایقی قبل قرار بود دستور حمله رو صادر کنم، ولی آنها گفتند ما مذاکره میکنیم و من برای این حسن نیت آنها ۲ هفته حمله را به تعویق انداختم.
ممنون از توجه شما
دانلد جی ترامپ
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/6272" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">برق قطع بشه با کبوتر میخوای پیام بزاری تو تلگرام؟ 🫪</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6271" target="_blank">📅 00:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تونل های DNS رو چرب کنین که داره میاد
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6270" target="_blank">📅 00:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6269" target="_blank">📅 00:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خب بریم ی چنتا آموزش کاربردی بذاریم تو این شرایط
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6268" target="_blank">📅 00:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6267" target="_blank">📅 21:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3YpX8YulO0RBUssr7qvWel0GbS8D8rg98EV93z2uXQqe_ZFb71Cv390-OI06BUOXNNE4v6HtUmFgutFbxYONnvky-obF325p6ITrSnT6IXvatnw2o_GxDZQ1jg8ArlwxzXOV5POy4bzzorvO3I5uJPVSAElMqMo9h2hFcE5MRB48znkj9toQt8SKmaw2GAGcc1r6zAnuCCqfpW8lfYyMaSjdY-Pl3rHXaruWVUjDiGEOS-pkp0kE3TPqdLQqK0xFP-G0gagI2pflZnZ8rwKRf1PaVcXLn6HG8rp67mceDzy4OIWHvv3E4y7SegTma6Qg-N6tnyedjMhU5-ANNHKmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHoafrqhm869t2rdOfGP4OukIIVsRu9TlmpZZcQJmaGz4RKffNOfL9NqeXW2Ls1HFbAJIXFfVf_S2Ro-d2fKG5ccDVec0_9lydRYf9gDnyyiwbUXeoQ7uurHPo5dPMFcWkn_YGuLl-O5UpnYVwSC40UfhdmHVs161yEr9layOCrPn3AIDsRlu_W1LTY3mgXJEkEFhdDDu4jRiEdoVFyVdmGHEscV3LzHpIlxiMtqCthXjy_LDRw8ZQYc5w3zxbcpze4ugA6yhVZUk4xGhqN3tOpNTYLekLNC7E_mNyHadBsvSUtNy4ch70fHAAVjFicEKir60GoBKDGGaI195_91kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6265" target="_blank">📅 19:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6263">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581e875845.mp4?token=PXtqRIG7xHHdNPR9cvmLOby0eIINb4JZaPjvdL5nFiA1pSC5COWK_-pKYzxvMiV44sKrGwQCENhQqaEtEwkkpNK9OUjyFELhVxzlXps-3A5jUtonzlT2jOUEpRyGGdWDaMn_e6V0RMKlF4L-xov2ZLZNtqCWtGyNNYFrvGrBbb1Us47dl1iEyCP-9nnba_qomhd9gmH01k7aFEB50GVqc6lpDuZ6TYcbgtCLEJ9tlzNm13scafyO9KJzNWJ3BZmLkJJWBoQQnyBrT2oSRkuDRVNr7E4QMkvA5MOxdJwIY0eCrfga-rUxRb91CYoU1WCLNBwW_vasIh45QJ7-K4BJU6mjJc-cyRsZJpL2MgErNlOsoEvepVZANALGT0MskU-jp-w9fbDuv2hsTYynHSQ1_0T6r_3n-b9gRB2gJwvqllg9hN8cX-92JHOyDciUOEr6kXHbnKGawGpx3dUEFmIV6KuXGX_Xh4YhIn211pT4PZ-PluxsK1ZXqDP0g1eDQ3pVipRCTAwLsBPL-avDh7cFP9RWLqX9EPevzDXbmsfcrsKcqjZEeHV_DIVSxN3n3nKlnnRU7gkucaA9t6zdbto8-MrnoYMR7t_6PbqEJF48XMDKVYd2Qshlu61bfKlf_G4jiG-1kONWNdGttdRUC3XGRHx4Z3M_tnWfqNGRbwahzYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581e875845.mp4?token=PXtqRIG7xHHdNPR9cvmLOby0eIINb4JZaPjvdL5nFiA1pSC5COWK_-pKYzxvMiV44sKrGwQCENhQqaEtEwkkpNK9OUjyFELhVxzlXps-3A5jUtonzlT2jOUEpRyGGdWDaMn_e6V0RMKlF4L-xov2ZLZNtqCWtGyNNYFrvGrBbb1Us47dl1iEyCP-9nnba_qomhd9gmH01k7aFEB50GVqc6lpDuZ6TYcbgtCLEJ9tlzNm13scafyO9KJzNWJ3BZmLkJJWBoQQnyBrT2oSRkuDRVNr7E4QMkvA5MOxdJwIY0eCrfga-rUxRb91CYoU1WCLNBwW_vasIh45QJ7-K4BJU6mjJc-cyRsZJpL2MgErNlOsoEvepVZANALGT0MskU-jp-w9fbDuv2hsTYynHSQ1_0T6r_3n-b9gRB2gJwvqllg9hN8cX-92JHOyDciUOEr6kXHbnKGawGpx3dUEFmIV6KuXGX_Xh4YhIn211pT4PZ-PluxsK1ZXqDP0g1eDQ3pVipRCTAwLsBPL-avDh7cFP9RWLqX9EPevzDXbmsfcrsKcqjZEeHV_DIVSxN3n3nKlnnRU7gkucaA9t6zdbto8-MrnoYMR7t_6PbqEJF48XMDKVYd2Qshlu61bfKlf_G4jiG-1kONWNdGttdRUC3XGRHx4Z3M_tnWfqNGRbwahzYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6261" target="_blank">📅 17:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کانفیگ ناب
🔥
trojan://humanity@104.17.121.43:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#%F0%9F%92%8E%20@ArchiveTell
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/6260" target="_blank">📅 16:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D823_ZDzwA8I7oqbeo0v5nz85tFLZ8IzBgOHRhM4nk6evOST1tkUpGjn_mcJ1ZX7mgcq4T2FQKjG8gWArQBuFeYgyYoJJWyZk7A1acHLluxhcZ446gXvO2TBmt4-eMpD42ybsHQTbC3kVUO-c5JFUC7ut8EGCD3346h-olY8CmlIW_syfG3dy2iU5ZXRPC3H6vVCXA-X-d4p5V4wRjKr1vZr_1N3SUHX6i9Vq77o14s83fi-MYIleOe96tKTzTKKvheRZcSzLhC1Qwtwq4OtXGtvhhv6T7f-vN_iW9wLUu3l_dgO7loBcbSjaY2MnqYa-TRg3BqDvoA6AEuBGmTepg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6259" target="_blank">📅 16:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=DeDSoPoth9JG8NelgtoU5qKZdhLa99GVvj3CENcz57g0jtIhGGG_XVm3S6jlPo0cAgxNZo-kM4rkTGvgLf3GbxHXv6rladIJvDCqr2TOvPQ_gc6Qtt0Ry8oDF_8XPJXeWNWWjx0vsq6tqS8gaZikpVY_53RxVHpaqFI6qpEGLEs1hyxQ46eQTMTs2ATlSmHGOkDb43sE5W547uuO0kKRIJBvqmmZjnYfJFU8UAi91SveAXOWLvlUTbwkiohK8V_lxo81Ki9hHCEU_hv0HZJJ1F4qZnN-lYCSGPu1xKQN1G40OIvyPswY8VULKNQ6mE0d4myI7x4btC1ua-DE1zOKnnYO8zG8U4ZvL0_cGYyoTryYRmusT0_q--grwFxQIdUvfELFm2i2-WX7fCz8RZdlY8HY38Yvcsr4kP-pK7nh3HED3lsJFvFKVfxlaBcjcmJ2QPYl4Lj4NhoOL5U7z83QnYsYuEwXQkUaFdQBHf1i4KBGZMMsS7KFSGGaTWeXI6AZuaosXU0lY7ldtr2BW2itVIEAAHfTNUIRzrq5MRP23Mu_E6BQwvQF4H7VjrG3FAfm3loK7RAHs7iDG2kDEpSR67CnRza3_NO5ijNu9XQiC1U0VlLvsUGEq88-9q8QxLkfbHhXJjK8bGdfPerYxedQEG30ZkcT2TZ24GJfvt782zY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4933b3906.mp4?token=DeDSoPoth9JG8NelgtoU5qKZdhLa99GVvj3CENcz57g0jtIhGGG_XVm3S6jlPo0cAgxNZo-kM4rkTGvgLf3GbxHXv6rladIJvDCqr2TOvPQ_gc6Qtt0Ry8oDF_8XPJXeWNWWjx0vsq6tqS8gaZikpVY_53RxVHpaqFI6qpEGLEs1hyxQ46eQTMTs2ATlSmHGOkDb43sE5W547uuO0kKRIJBvqmmZjnYfJFU8UAi91SveAXOWLvlUTbwkiohK8V_lxo81Ki9hHCEU_hv0HZJJ1F4qZnN-lYCSGPu1xKQN1G40OIvyPswY8VULKNQ6mE0d4myI7x4btC1ua-DE1zOKnnYO8zG8U4ZvL0_cGYyoTryYRmusT0_q--grwFxQIdUvfELFm2i2-WX7fCz8RZdlY8HY38Yvcsr4kP-pK7nh3HED3lsJFvFKVfxlaBcjcmJ2QPYl4Lj4NhoOL5U7z83QnYsYuEwXQkUaFdQBHf1i4KBGZMMsS7KFSGGaTWeXI6AZuaosXU0lY7ldtr2BW2itVIEAAHfTNUIRzrq5MRP23Mu_E6BQwvQF4H7VjrG3FAfm3loK7RAHs7iDG2kDEpSR67CnRza3_NO5ijNu9XQiC1U0VlLvsUGEq88-9q8QxLkfbHhXJjK8bGdfPerYxedQEG30ZkcT2TZ24GJfvt782zY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XPGjBfFbe6PuQXt-TcmjBvVSxPvFVsj67pEog3ocIN9bTn50hKSmNFO-CzFHdSwPG2LijcP8QjLRqTgR8xHpuulB9WqgwbkQhnuSXa2pu_1rHg8aGA0g0vVn-2RJKmdpHZn9RDvTcCoq4NXpdljgXc5GTD56BjZbHFMC-krpHE4sberf-d0FYVpJZtW4T7QBY7F-lx5TIIWApceRBrMPR3RPSAWXzy7iIjz9iJxqbBJ0sp28HqAn66zcZIsNXo13LwXO2DgkGZRUto4-nAlzud1scOd9wdrLhSHVeXkE1Wys1gIivGN0Wg81HGDN9yLaoilakvtyIx1cPI5jVj6Rvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdvImJtnyXNSy7blZPtYTkVu1VBaucj-CWXMv6tkCghOWTVIqxtFkTLmar8aEGYfe7l09dBH-rPOWmKzSWydaIn21cjMDsLXdvVIfqNL1tw8OvYMNcAwd9cEa7fI6_vRCYFeAxPgEOKncrR1UOk4owzSAdNShWFzzEaM7slDfNTB3DXaK-_H61gA4yHSegWoWC_g_f56E2O9MntaM0Uj_7EOZJaMD2612fO33T3woevwtOZH7UV7CDSK29rNhfkUCceSEVxfNjFvxcFAAakNH0kqLgObPvtWEuvx2kMJdMeONayi6OTo9OAYR05Kq2KR1jm4QUG2B-SvWg96fCdibg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6256" target="_blank">📅 15:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6253" target="_blank">📅 11:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚀
YPtun؛ یک کلاینت VPN متن‌باز جدید برای اندروید  اگر از محدود بودن کلاینت‌های معمولی خسته شدی، YPtun یه گزینه جالب و همه‌فن‌حریفه
👀
🔹
پشتیبانی از VLESS + Reality، XHTTP، Hysteria2 و AmneziaWG
🔹
استفاده از هسته‌های Xray و sing-box در یک اپلیکیشن
🔹
قابلیت…</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/6252" target="_blank">📅 10:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdMQ2fIhAVBpSQVGdf8Vpk9VPjdr408Z_iGq6cU66ZFj7tDpyiNCJJRrgFMKcxAUOn-f1x6hrleI0wLqf48O4_B-PNr0qNu3rtpZ7v3SxoP7X_2eau3QWzqpMX2zdOiSjv1YptA96_R9OSel9i0xFUuA5MJE2qlooczrzItf2Bss-tuEzI2KcvsY7OkkamaiQLl_9JnfFqU-jz2X98SHjhfbNJSXbLPukcjS8x--2XEzJJi-Rcg6sQHLF1TqTCTQaZHHiYm5gDd3ZRC55MUMGctaFUQv6XCuEpB27MMV0TuSzxyYjgt2jxgLNECDd3mGRvcQ8D2ylkm4WgDza-RpAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SO_Vj7gUikVDapTFFowKwKv8g7ABprnj92I49Ps46acqnkKbwwFGj8t_AUivESeqqC9DANh-1D_-icPjwcDbIlZ0pDqfJt7Ns7polunMXEGfdEKPF38tLbTO3osr8ugI6uHKJ7wj0LcCXj-q7lrkkVGb2mzXTskTdEk0WQf4dLu-g5j9jRSN9FSalfV96Ay7OJ7RtvH5pb3tYm2l9JJA_PziceVASj7ghBupX6EAKkYCGcVYEK-nwqMmRSLe6hDx4mv9YM-H6pWLxoEcbRSSyMrvP3mxUApt8RzZbUwTcTy-mOtVivImpkiEyJFQ64EAhviP4UlhH3A7ZNTCUS0-tA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c02KdjoMRKrDYjwE_EIyKZH9JGH4JfdNNiR4z6JDnU1HwkPxhVpcEHIl4eIHO9b8datq2qUlvi9aHt0UCU4KSHoNzeBdGpAytfs2RqJ18QcyFEt3tctYrxTZdsafdsMQTPpOD5UtDQBH6p93AocjqHewLBc1XjKAZzee7HD0hcLG21rdIuNhmfkrKhQoIfojHr1rtMjqUKXqWvKzzKDyVQxkd0oYAQk_BZ5mQAKq3pRy-ETHyRqrpHx5cfKpcGQG0kFYYsjNyl1mK8hnmNw6yRSVg_4YwJHQzauC3gjL2dr8YlrhTQMQhS2-gYRP3lKp2BLel73wzpJylMRXb2eF8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c54422014d.mp4?token=PshG09alsS23ACp-cYRumuQwVXDJ2npkqFLkmoXPmwCBnUQSKoYaUS1oyz-0rmSfep1FnL7s4Ai_-5f41RRbczMYfBdtz6S5snYMzZtd-ox2AmeZuucQhIRMIw5YntFR8esTtdhL2OnNF2zd1j_XeQfCtabJxAO9en4UQPTJhMBcLjo_27YQ6whqDZNHj1NNq18EbHq8pK_VoeZP6ZjLiicG3b4pHupdP-x3_D3l7ZJE9DhrQiHrmckX27rgiDolLlYreoUHyxIN0N39Sdl7u-0K2SF01KlKESPpdthzag4yUSebmYmoXvreKCrMkzNMM4mjL6gAgQTnmJvbZ6gTDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c54422014d.mp4?token=PshG09alsS23ACp-cYRumuQwVXDJ2npkqFLkmoXPmwCBnUQSKoYaUS1oyz-0rmSfep1FnL7s4Ai_-5f41RRbczMYfBdtz6S5snYMzZtd-ox2AmeZuucQhIRMIw5YntFR8esTtdhL2OnNF2zd1j_XeQfCtabJxAO9en4UQPTJhMBcLjo_27YQ6whqDZNHj1NNq18EbHq8pK_VoeZP6ZjLiicG3b4pHupdP-x3_D3l7ZJE9DhrQiHrmckX27rgiDolLlYreoUHyxIN0N39Sdl7u-0K2SF01KlKESPpdthzag4yUSebmYmoXvreKCrMkzNMM4mjL6gAgQTnmJvbZ6gTDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
تلگرام برای اپل واچ
تلگرام به طور رسمی اپلیکیشن خود را برای اپل واچ بازگرداند.
#Telegram
#AppleWatch
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/6248" target="_blank">📅 09:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaTd3_rGDmwk0kv6d29k7VV7nkxO4z0dv7FLbAOOTbHQkxaptFSpF1YNQWZtcU9MUZqDls6sAx2Naqn_6lXOVvbTuH_quN6xObHccGcoZUhZBLZ5VOAWhrTR1Gh_jG3hj4_dOSOlsNEWzCx_1D6IZ-aIQUY5uTA0oJ-zQOnzVVyj4csi78JjvNVAvd7ZiGA4ii1eJSo4_FFqsvZwDJUbsaw1XTeg3gmuJjeFDw3xiqs6xQKTboGn-YGMAxYLNzDWHRf4X3n0cmbuvJuxZ8WgphcKPT3AXK_iN3KSff1RQM4PZ8risE-Ks9-UoRidyQcsH6wE6Rei_i149MLP6cPRyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6247" target="_blank">📅 09:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6246" target="_blank">📅 08:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">vless://5dcf2dbf-3e82-4456-8961-287cc732bb0f@85.198.20.217:12817?type=ws&encryption=none&path=%2F&host=Play.google.com&security=none#Germany%20Hetzner-.
10 گیگابایت تانل المان</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6245" target="_blank">📅 03:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtoc9IC09jDCiahWo32K2--qksuk5f7A3k1ddyeCiHxAzu_avg_v0L7WvvJRIiwM9O2yK3ROS5rdYonfYP7c3VccJu4tRf7s4rPd_-Ak3-lionPf8dWfvMOSxd2Sj_JusTgIa6wBTHmCV9mRRqa_Cv_ICXLU8n1udOklyeEj-mC1CDlo36gUgBg9-A8T5nQBQTJCCxbGLjLQ4PZApmFSgdsaj1Y_JUr-adtWY25ffSo5hroQ6uDDkLSVHhwfKJ01SllnvdaS5lR_Z7gCVC-iZZ_A05t4xq-CVmzd4k0XYIGVUqV6WwZCOie97vO1EyoUNELmGWofTw12wV6wF9L9HQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6244" target="_blank">📅 03:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🫠</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6242" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYj2UWOyJr75Tyj2tp4DIvBmm2XhKxt-Sa6WcE0HhPn6U6zT7jNzXBs3FDmRz17-m3kPxJ3RjMxMxUXX4ANbHWhkCKYcH8OAY3-2NchO1jSCUsmxN6mwQxBerV6-cQQjVxq8WYbXfHJ6jZObigI1GoA0tualSSVzC1K0_KIoprybZSjobaeO7R99YRGrasR_iXut8cPsooPrz8PcEn7VqynvnJvi4eTpzykXaeZiVuLgTy4uC-CHiq_iQxOwD6yeg6goGwJHXUs36B2JbTDlfAdf8CA41ISH25xQiylkWr0fS-iV4CBjIwy-M7ntTXbU4L517U6PN_-yB6HNfbiHRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">https://t.me/ArchiveTellNews/212
🤨
🤔</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6239" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6238" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app
بخونید نظرتونو بگید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/6237" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">StormDNS
a.cyntarix.com
25ffbc77bcfb23b2d4ee225eedcd2466
داشته باشید اگه نت قطع شد</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6236" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">این پروژه پایتونی جالب هم برای تشخیص اشیاء توی ناحیه مشخص شده کاربرد داره مثلا طبق مثال خودش که با QWEN ادغامش کرده یه نفر با هودی اومده توی ناحیه مشخص شده تشخیصش داده و به گوشیش نوتیف فرستاده و گفته چه چیزی با چه اطلاعاتی اومده توی ناحیه.
برای دوربین مداربسته خوبه یه ناحیه رو مشخص میکنی هر چیزی اومد توش بهتون خبر میده،کد اصلیش با پایتون نوشته شده و از ابزارهایی مث ffmpeg برای مدیریت استریم‌های ویدیویی استفاده می‌‌کنه.
github.com/roryclear/clearcam
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6233" target="_blank">📅 00:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">هر کی 99 تا رفرال داشته باشه ی کانفیگ نپستر میدیم بش
😌
🔥</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6231" target="_blank">📅 00:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6230" target="_blank">📅 00:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6229" target="_blank">📅 00:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVkClTkEJE0VI5fpuPbmqF6ZIOklY8mkub6HTzMYMq7a2SR6YBPJs2Z35StZigEnHikr_2SNY89LUPnHDZh6ieQfwsFHwf4Qp1ScP7JWTw1safrifLs5j12ve1zBlYUbHbgZg8y_-QkuKBVifCChhuktPZ2Dx5E1NWQ-utoqpW8fOhpIKM1tRckiei8Z0G-0_Bct5dKi7r9s2BWF0Lq11zkMlFjfVjncy3sP2UYWp38Sq60HekwwDybdTc6rdEcd_yPdxl-QXGqm-uOs2PS3EQuLQJ4g53gqjpsYQr8E2U_k4IqcGRPKiUBkhK700duPLmzqoky8ciZyWY6g86f7iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=tkSx1tjMVVDwESalVLaunXP3DKL1CEbXf1o-GRKnLkMhAMgyat47kTaffHNAOf6vKVqOXlGyS08xX8XMSdWbD9x6gMwEBGrpHviCJm_sLY6rt-Sr1NpRuTah7ENeIXHIvOIaGBMKB-if9UhhMu2VrIGvyKHlwkmJkO2nd3ZDdZbgF6SxU1KX-KvM6y9Sl5SVfpQfL7LsSmeO_nCqPg3mss3zSHa6Q0piIw5FBnOWfs1cFl7oh5pT0uuhi9Whj5tr9SJY35xiDwBItFnDFgB9Kh8m7VNQZBOTDQA4n4Jiz868Rvcn70noxps2vWfQDatXPTyLfXJjgha-uuc7CRtJPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8c59be67.mp4?token=tkSx1tjMVVDwESalVLaunXP3DKL1CEbXf1o-GRKnLkMhAMgyat47kTaffHNAOf6vKVqOXlGyS08xX8XMSdWbD9x6gMwEBGrpHviCJm_sLY6rt-Sr1NpRuTah7ENeIXHIvOIaGBMKB-if9UhhMu2VrIGvyKHlwkmJkO2nd3ZDdZbgF6SxU1KX-KvM6y9Sl5SVfpQfL7LsSmeO_nCqPg3mss3zSHa6Q0piIw5FBnOWfs1cFl7oh5pT0uuhi9Whj5tr9SJY35xiDwBItFnDFgB9Kh8m7VNQZBOTDQA4n4Jiz868Rvcn70noxps2vWfQDatXPTyLfXJjgha-uuc7CRtJPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6225" target="_blank">📅 22:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXOwEyLbeKdM9YVVZVKaQakEkLZDa0R8eEWSXfSlfdz8YyFhHq1kDxmp0371r-POoGyGrahsSrUoZgnNaBTDWGFxcjHACivQMe4ncd196FnDMVtbWZihgIpsU44WJU6hvwSrvTTpf1rMu3Aa6syYQ1r3nfSfX1T00w-Ja3yLGm6PB-7xQ2k_Qdcp5yqpU0bYNyrT0xgb_-fg5O6PnyC8wsDFUnxrT4fjFBEhwcuCLXizorUNNLBtjyTv22YLn24OYtNfQjCYjR1GdH-cc7pC5id-u5nF5f7rGhneNe4cAJ34woP5LlZHVqoY-AE_8ckfdJsEdddmqlOaM0tO5txSwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/6224" target="_blank">📅 22:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6223" target="_blank">📅 21:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clKLW2tDqEk5Ar5y3L1Kc5tWZgUZHoMDvXhaTrCnkORwE7ZAO3KVOMXtNJGqFakjO5Y3N9j_OzI60G67JEaeuo40fLtEVx_4MkQMH7U7oIr8Nsyo6d-a9kfVgzDPd4_oPk4uKZJn4R-gNHJyDQ0jMyknOsDTQ0P7OV0iNXwni8zzVd-sHoZFnb5xsU74XYrPGWKKsobmxbZ05DkWMzvPdtRJhwKWEaRJGfK223QUEe_Qp3VosaMYXplFK1hrRaXOfFhgQ4YqLwhp5WcC-UY6v3N95YMcyTlLZ_KzWNgWZMuB4F2YHQD7j4d_Pqbfz9ZBYLTqa5XYqo9eNNOyQIje6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6222" target="_blank">📅 20:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6221" target="_blank">📅 19:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/6220" target="_blank">📅 19:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خب یه پست اختصاصی دیگه داریم این فایل رو خیلی جاها میلیونی میفروختن در حالی که رایگان بودش یکم دیگه پابلیک میکنم
🔥</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6219" target="_blank">📅 18:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNr-xMUVIYRAoI1E_IZnlvloQwZV9PSCGg2gnOHAf2k7vNAB1OTbgsa7YsdWtoHA1wZbUnB92HhVFjIx3tqC91_hx1VesVZ_1qC2sFgxc7BYHJt72lXBOMiLSlnjh26mRsz4b7_UJLwYpLZQdaGmSdSNbFuWo-R04WT69hab09LhQiLS8MRd336vWRx13RSz_pXr9LdBBhWvfUCE_nxEmjFgHjru0rb8r7JKYg1FULIXYC2TXcOFOBHfETB0CSiNP9TdC5gKJJL0lev6csZfYZq6OXWsoG3Phie9zLRcEvsTa_ZJJJJiTq73AoRJc-695koazqxbBNu6NR0v5dK7hA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6216" target="_blank">📅 18:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/6214" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6213" target="_blank">📅 17:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانفیگ ناب اهدایی
💎
hysteria2://5z15av99psrlhdqp@32.195.51.20:39150?alpn=h3%2Chttp%2F1.1%2Ch2&fm=%7B%22udp%22%3A%5B%7B%22settings%22%3A%7B%22password%22%3A%22dlxmzvxvcp3i6v0e%22%7D%2C%22type%22%3A%22salamander%22%7D%5D%7D&fp=chrome&obfs=salamander&obfs-password=dlxmzvxvcp3i6v0e&security=tls&sni=32.195.51.20#usa_hesteria-%40u2vpn-100.00GB%F0%9F%93%8A
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/6212" target="_blank">📅 15:52 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
