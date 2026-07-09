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
<img src="https://cdn4.telesco.pe/file/WuvOe_ROARy4Un11tfA3K0ZRjLbR8wnvU9aTHv09LoNotzlOTby_efvQixZY3gIB40ypKit5ak54Mpn2wZgiyezDxKFWZLRBFOeiAw--sDB1hYgVi3jr4Dx1HhjGZ-cEzOlTnkvFjecRHNhxzceyvOUVD9A0M6GjIw1oNx4Z1bMjaCUD-SnlfgzD6BXrPZ28aeNnyUGQDk1kTfWbx34NQMXxyKd6xly4HB3XrGZ8GxH7Bo3McFeUfvZzRG9PboKxRjr-XvRXc5SWoBxuHk6aw1mGuZ-sXqOB70zxa2APDgN4cu7fg63062vVfqKK9cx3pXDqA_9umvlPliU0XlFOgQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.82K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐https://www.youtube.com/@ArchiveTelll</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 22:35:41</div>
<hr>

<div class="tg-post" id="msg-6827">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">📱
💿
؛EtchDroid؛ ساخت فلش بوتیبل با گوشی اندروید
اگر کامپیوتر در دسترس ندارید، EtchDroid به شما اجازه می‌دهد فایل‌های ISO سیستم‌عامل‌های لینوکسی را مستقیماً از طریق گوشی روی فلش USB رایت کنید و یک فلش بوتیبل بسازید.
✨
ویژگی‌ها:
🔹
متن‌باز و رایگان
🔹
پشتیبانی از اکثر توزیع‌های لینوکس و Raspberry Pi
🔹
مناسب برای مواقعی که سیستم بالا نمی‌آید و فقط گوشی در دسترس است
⚠️
این برنامه از ISO رسمی ویندوز و فایل‌های DMG مک پشتیبانی نمی‌کند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 349 · <a href="https://t.me/ArchiveTell/6827" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6826">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🤖
Cogny | دستیار هوش مصنوعی بازاریابی
✨
یه ابزار فوق‌العاده که بازاریابی رو با هوش مصنوعی انجام میده! سئو، تبلیغات، تحلیل رقبا و کلی کار دیگه
🚀
⚡
ویژگی‌ها:
🎯
سئو و بهینه‌سازی محتوا
📊
تحلیل کمپین‌های تبلیغاتی
🔍
آنالیز رقبا و بازار
✍️
تولید متن تبلیغاتی
📈
اتصال به ۱۳ کانال بازاریابی
💻
کار با Claude، Cursor و Codex
💰
رایگان برای شروع · ۹ دلار برای استفاده نامحدود
🔗
https://cogny.com
#هوش_مصنوعی
#بازاریابی
#سئو
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 579 · <a href="https://t.me/ArchiveTell/6826" target="_blank">📅 21:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6825">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3OX-l-vy1uCVGHE1UFtaFKj4p1Zauszoz2-x3bEdPrkGq7PqY0hHxd__Es3lLVXRX3mAj1mNWeq4KjZDGKix7mo7bkcWeFENhIMknwQv0J-1HMud5bQg2J0ZfHIvB_E0hvdNHLm2IUOpHkRyLbpX6FeFfEcU1AQymmD5P6tFHhnXUcvcsqLpjMSStOX5jDTrgiFGl5LvXf3qnCz2OlSHvEvntzo_sB4iTK5qpsX56RuI1fAgHpmTssfGJxYlK-3Ei4r2lKSKlOLrMibLKfP6__FyqXXV5vIYQwZcoDnMcJJ4HNvBxrGDFTr9j0n_atHZ2QNtILS_BtB8wPg5tBQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 671 · <a href="https://t.me/ArchiveTell/6825" target="_blank">📅 20:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6824">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">104.17.14.0
104.25.49.102
ایپی تمیز کلودفلر
تست کنین
❤️
با لایک و دیسلایک و کامنت اعلام کنین
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 768 · <a href="https://t.me/ArchiveTell/6824" target="_blank">📅 20:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6821">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYIVaEA7uEksOqnJnP3um_M9FNGd4RNQ4GGErygoyAc7U4OtFmynJA65VsIdpt7c4u6HAZFdY5iUj8zneFQSF7oxWRSxHm0WgIUyP5Ck6l_wFq_bFFyMKN_6I7BUcXJ6FqvnmSDDrpyMch3UXXLPxuQytNK0w3mHnIMh5jweaDrv0I8EvARrUj6M6WYwll9tbKoYiagezBkn4QbVrsTcFZipq-U-1avFdYfXigALEMsccsFzYGXfK7OKseHr0SzZsC2U0QTZ236CDG5pnn8IGAq8BuhG9h9dkTvnQN2K6hnm2H8LDwv9cbd6I16uuLP_YBP8sExjpdu0azo6tRYdgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lNCdxAE2cK8bdCeZjPHcfVr5KoB35RpeJzFqNCKVSWg_yXkJIEKuXBHJMEDxLl3GhK13dc8SHizmY1O-VKtWqcHJBhYb0ZN6uSCbn6CRB_06kbwGPmXOaEmBHFGQfq1f2nWMRNzoGS4m94kQqtFx40mbTOy16buyK_FU6jsEr60jYnZyGNtJ3qLdYU2dAxhlqHjy_IgxXtwr3Ana0BhBJI7Dl5HWjLJjGTfDM4rxIONp9DUmQiZsYyXERMfJ6sQ8PDoOe1hZOPvLgzM9yv8AJZlaz7dfPZpUHTjZ3fNjdJ_DSOEZgeIiNhUGtSz6_1kxBFrUmcw3Aud6n3lAGqmfOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏‌
Imgfree⁩: ابزار رایگان تولید تصویر و ویدیو با هوش مصنوعی
🤖
‏
🌐
پلتفرمی که مدل‌های پیشرفته هوش مصنوعی مانند ‌‌Midjourney⁩، ‌GPT-Image⁩ ، ‌Kling⁩ ، Nano Banana و Flux را گرد هم آورده است
📈
‏
✨
تولید تصویر و ویدیو بدون نیاز به تنظیمات پیچیده
📺
‏
🔗
لینک: ‌
https://www.imgfree.co
⁩
‏
💻
دسترسی رایگان و نامحدود برای تولید محتوای با کیفیت
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 984 · <a href="https://t.me/ArchiveTell/6821" target="_blank">📅 19:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6820">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r76R3EKpQlVW75x6I13Ms17jjzXTNcOIHhnaiiKiyrrIsoeu4hcmhvc_OCyhEFlGfQ9-Y_ca7GcTdE41Cj8_wffuL7fZlSn7Gxhuvep_yyi0PQ64lE9H6w8ZKKxf3aFVEXq_Z1Fge4Bt3JN6tMpN8QLS_KanrfOKUMq8rfkWntkTvvQZ6jkpFwoAWTZsiM_blakcgjjoSxR3ZLGILTz7QuwmTjyoT5Q3u0wGki-L6CiUCWc-orcOzsDPyowV2D52oVltuTkFADew5-anynSXZGp5gkSLcP99sKxHwo7gkmGQ8BjwuvPu6O72rtVmcLHeyMjL9VNjHmfr81ywFVR2IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛
🎬
CapCut Web؛ ادیت ویدیو با هوش مصنوعی
اگر تولید محتوا می‌کنید یا برای شبکه‌های اجتماعی ویدیو می‌سازید،
CapCut Web
یکی از کامل‌ترین ابزارهای آنلاین برای تدوین سریع و حرفه‌ای است.
با قابلیت‌های هوش مصنوعی این پلتفرم می‌توانید:
•
🪄
حذف خودکار پس‌زمینه و نویز صدا
•
📝
ساخت زیرنویس خودکار (حتی برای فارسی)
•
✂️
تبدیل ویدیوهای طولانی به کلیپ‌های کوتاه مناسب ریلز و شورتز
•
🎨
استفاده از افکت‌ها، قالب‌ها و ابزارهای هوشمند ادیت
🔗
سایت:
https://www.capcut.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 976 · <a href="https://t.me/ArchiveTell/6820" target="_blank">📅 18:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6819">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🌐
دانلود کامل هر وب‌سایت با Website Downloader
اگر می‌خواهید یک وب‌سایت را برای استفاده آفلاین یا بررسی کدهای آن دانلود کنید(فرانت اند)،
Website Downloader
ابزار مناسبی است.
✨
قابلیت‌ها: •
📥
دانلود کامل
HTML، CSS، JavaScript، تصاویر و فونت‌ها
•
🔗
بازنویسی لینک‌ها برای اجرای آفلاین •
📦
خروجی به‌صورت فایل ZIP •
⚡
متن‌باز با لایسنس MIT
این ابزار برای
کلون کردن سایت‌ها، تهیه نسخه آفلاین و یادگیری ساختار پروژه‌های وب
بسیار کاربردی است.
🔗
GitHub
:
https://github.com/AhmadIbrahiim/Website-downloader
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/ArchiveTell/6819" target="_blank">📅 17:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6818">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b961c32eaa.mp4?token=FJl4w5ddL_FwQBu6qOf3OU1mjOBtZWPQ1t08o3s8MiRlqJcjmgIYYCaUGiwUcf-i98-e5wIh0RljBJgXUTo9XEzbi4h8g_-W-MLYap7BnJ5U0CgTgOwSpP3SCxGTpkIwkOftyBX1GMdzmmWrr06nQ-Fi4Cu8bb6ii3CJOQU0iQy4819B3B26SxUDpMn0qVSB-ORFYI_G2tPrUTTA3rdWDE3kQ2vPirqWBMEOJGJVGHjlI3iD2LYUFFApw7vwPrOzW2B2XDz-8gUxpLaVpgCUK6G-YnmhJLtaPv4i5SM4yRwd-Aou12O3I1e4ywp1VQquKHQrrDj8rNvLXoL72y5HgWy5_n4dJJQBcAC6OY3qFBeposCaloD-5IIivrMFLJ-pDe1fUNM2392tMlouloJohijQO_72P8osskpFVCotXjJ6Ae5L7QttoLdY2TeQaD8sAINxyJ0pQXhTwAXgCT_tGh0SwmeOZMz3jFigz2gNmSJZNKubIcmCKKub522ujY1b-PBkmvXaTB5-NWDZa_0uhOfW7XE4OhFcV16l96ZPaHj--UyixP-T2_G8PmGGlWlAletFQ5GBMfeIDkdG20RVYntq9GQCcxmsfbrKXMhKJr9_mvaplgqOr4Q3KCP4uDi6wkQwKjT-ShLGVq8o8jatklm6-DlhAqQqzDzpM5GpwfM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b961c32eaa.mp4?token=FJl4w5ddL_FwQBu6qOf3OU1mjOBtZWPQ1t08o3s8MiRlqJcjmgIYYCaUGiwUcf-i98-e5wIh0RljBJgXUTo9XEzbi4h8g_-W-MLYap7BnJ5U0CgTgOwSpP3SCxGTpkIwkOftyBX1GMdzmmWrr06nQ-Fi4Cu8bb6ii3CJOQU0iQy4819B3B26SxUDpMn0qVSB-ORFYI_G2tPrUTTA3rdWDE3kQ2vPirqWBMEOJGJVGHjlI3iD2LYUFFApw7vwPrOzW2B2XDz-8gUxpLaVpgCUK6G-YnmhJLtaPv4i5SM4yRwd-Aou12O3I1e4ywp1VQquKHQrrDj8rNvLXoL72y5HgWy5_n4dJJQBcAC6OY3qFBeposCaloD-5IIivrMFLJ-pDe1fUNM2392tMlouloJohijQO_72P8osskpFVCotXjJ6Ae5L7QttoLdY2TeQaD8sAINxyJ0pQXhTwAXgCT_tGh0SwmeOZMz3jFigz2gNmSJZNKubIcmCKKub522ujY1b-PBkmvXaTB5-NWDZa_0uhOfW7XE4OhFcV16l96ZPaHj--UyixP-T2_G8PmGGlWlAletFQ5GBMfeIDkdG20RVYntq9GQCcxmsfbrKXMhKJr9_mvaplgqOr4Q3KCP4uDi6wkQwKjT-ShLGVq8o8jatklm6-DlhAqQqzDzpM5GpwfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🌎
نقشه آینده زمین برای زندگی!
‏این پروژه خیلی جالب و مهمه! یه نقشه تعاملی به نام ‌Farmland Atlas⁩ ساخته شده که پیش‌بینی می‌کنه مناطق مختلف زمین چقدر برای زندگی مناسب خواهند بود تا سال ‌2100⁩.
🤔
‏این پلتفرم با تحلیل بیش از ‌5⁩ میلیون نقطه، چندین سناریو رو بررسی می‌کنه، از خوش‌بینانه تا بدبینانه. برای هر مکان، پیش‌بینی آب و هوا، ارزیابی کیفیت منابع آب، وضعیت خاک و خطرات اجتماعی رو هم در نظر می‌گیره.
🌟
🔗
https://farmlandatlas.com/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.25K · <a href="https://t.me/ArchiveTell/6818" target="_blank">📅 14:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6817">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">📊
معرفی ابزار CodexBar
اگر از
Claude Code، OpenAI Codex، Cursor، Gemini، OpenRouter، GitHub Copilot
یا سایر ابزارهای AI استفاده می‌کنید، احتمالاً بارها با محدودیت استفاده یا تمام شدن سهمیه مواجه شده‌اید.
؛
CodexBar
یک ابزار متن‌باز برای macOS است که تمام این اطلاعات را مستقیماً در نوار منو نمایش می‌دهد تا همیشه بدانید چقدر از سهمیه‌تان باقی مانده است.
ویژگی‌ها:
• نمایش میزان استفاده و سهمیه باقی‌مانده
• نمایش زمان دقیق ریست شدن محدودیت‌ها
• پشتیبانی از Claude، Codex، Cursor، Gemini، OpenRouter، GitHub Copilot، Groq، Deepgram، MiniMax،
z.ai
و ده‌ها سرویس دیگر
• نمایش هزینه، اعتبار و میزان مصرف API در سرویس‌های پشتیبانی‌شده
• نمایش وضعیت آنلاین سرویس‌ها و اختلالات احتمالی
• حالت تجمیعی برای مدیریت چندین سرویس از یک پنل
• بدون ذخیره رمز عبور؛ از نشست‌ها و لاگین‌های موجود شما استفاده می‌کند.
🔗
GitHub:
https://github.com/steipete/CodexBar
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/ArchiveTell/6817" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6816">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚀
چند ابزار متن‌باز و رایگان برای برنامه‌نویس‌ها و سازنده‌ها:
🎨
Text Effects
افکت‌های جذاب CSS برای طراحی متن و رابط وب.
📧
SESPulse
داشبورد متن‌باز برای مدیریت و بررسی ایمیل‌های Amazon SES.
🔎
API Finder
مخزن APIهای عمومی برای پیدا کردن سرویس‌های آماده.
🛡
Tirreno
فریم‌ورک امنیتی متن‌باز برای شناسایی رفتارهای مشکوک کاربران.
💻
OpenTUI
کتابخانه ساخت رابط‌های کاربری زیبا در ترمینال.
✨
ابزارهای کوچک، کاربردهای بزرگ برای ساخت سریع‌تر پروژه‌ها.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/6816" target="_blank">📅 13:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6815">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کانفیگ اهدایی
🔥
vless://ac7e7b41-0dc0-4bec-a285-3266ecbb87c8@ps.aramvpn.kdns.fr:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QFc4pPuYwGfyKeoSWnxUkPgaDdEPCPPb2ImpxI-njxI&security=reality&sid=0586e9d2d3a6d12d&sni=www.yahoo.com&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/ArchiveTell/6815" target="_blank">📅 13:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6814">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">📸
ساخت عکس پرسنلی ۳×۴ با هوش مصنوعی
اگر یک عکس معمولی از خودتان دارید، می‌توانید با پرامپت زیر آن را به یک
عکس پرسنلی رسمی
تبدیل کنید.
✨
ویژگی‌ها:
✅
پس‌زمینه سفید یا خاکستری ساده
✅
نورپردازی طبیعی و یکنواخت
✅
حذف اشیای اضافی و اکسسوری‌ها
✅
افزایش کیفیت و وضوح تصویر
✅
مناسب برای عکس پرسنلی و پاسپورت
📝
Prompt:
Convert this photo into a professional ID/passport photo.
- Neutral plain background (light gray or white, evenly lit, no texture).
- Centered face and shoulders visible, crop from top of head to chest.
- Natural skin tone, balanced lighting, no shadows.
- Neutral facial expression (slight smile allowed).
- Professional look, no accessories (remove hats, sunglasses, background objects).
- Enhance sharpness and clarity.
- High resolution, suitable for official use.
💡
برای بهترین نتیجه، یک عکس با نور مناسب و کیفیت خوب به مدل بدهید.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/6814" target="_blank">📅 11:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6813">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">📄
olmOCR | تبدیل هوشمند PDF به Markdown با هوش مصنوعی
یک ابزار متن‌باز برای تبدیل فایل‌های PDF، PNG و JPEG به متن و Markdown تمیز با حفظ ساختار اسناد؛ مناسب برای مقالات، کتاب‌ها و فایل‌های اسکن‌شده.
🚀
⚡
ویژگی‌ها:
📝
تبدیل PDF و تصاویر به Markdown خوانا
📊
پشتیبانی از جدول‌ها، فرمول‌ها، دست‌خط و قالب‌بندی‌های پیچیده
🧹
حذف خودکار هدر و فوتر صفحات
📚
حفظ ترتیب طبیعی متن حتی در اسناد چندستونه و دارای شکل
⚡
دقت بالا با پشتیبانی از پردازش محلی یا سرورهای vLLM
🔓
متن‌باز با لایسنس Apache 2.0
🔗
https://github.com/allenai/olmocr
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/ArchiveTell/6813" target="_blank">📅 10:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6812">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">؛
🛠️
OfficeCLI؛ هوش مصنوعی برای Word، Excel و PowerPoint
؛
OfficeCLI
یک ابزار متن‌باز جدید است که به دستیارهای هوش مصنوعی امکان کار مستقیم با فایل‌های
Word، Excel و PowerPoint
را می‌دهد.
✨
قابلیت‌ها: •
📄
ساخت و ویرایش اسناد Word •
📊
ایجاد و تحلیل فایل‌های Excel •
📽️
ساخت و ویرایش ارائه‌های PowerPoint •
✅
بررسی و اصلاح خودکار خروجی‌ها
نکته جالب اینکه
بدون نیاز به نصب Microsoft Office
کار می‌کند و از محیط‌هایی مثل
Claude Code، Cursor و Codex
نیز پشتیبانی می‌کند.
🔗
GitHub:
https://github.com/iOfficeAI/OfficeCLI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/ArchiveTell/6812" target="_blank">📅 09:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6809">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dae562e36c.mp4?token=hiUjlYluD3yE4t07Eic8GVsS_lM4SF6G1VslAUcLEl2QeY-NWXyWlHwli19WUSuTvKRVGInEPRs80H8JyGOfvJH-pOK8Bg1_mQV5z_xZumjjmRKGms_3dZpYQzCdmOPfE5fqXmws43QTigjQW6N0N-fh7X6q4AKS1x5wW-aGPkD-A4XLHQMjTzqSy3Dpl4y1wy7I9JMZAuCU7mfhT2NMq4Z4alDw_kOD7p04UPCU6ALxDBxg2lRur1AatkDAcMhk2I_saDvfncgaZgAF3fNZXrybdIV6juaTrF4J6NCRxLdcK_kzpeT8cB6yS5oWh_JwzT6Lqi5fQCa2k0Qx6-66EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dae562e36c.mp4?token=hiUjlYluD3yE4t07Eic8GVsS_lM4SF6G1VslAUcLEl2QeY-NWXyWlHwli19WUSuTvKRVGInEPRs80H8JyGOfvJH-pOK8Bg1_mQV5z_xZumjjmRKGms_3dZpYQzCdmOPfE5fqXmws43QTigjQW6N0N-fh7X6q4AKS1x5wW-aGPkD-A4XLHQMjTzqSy3Dpl4y1wy7I9JMZAuCU7mfhT2NMq4Z4alDw_kOD7p04UPCU6ALxDBxg2lRur1AatkDAcMhk2I_saDvfncgaZgAF3fNZXrybdIV6juaTrF4J6NCRxLdcK_kzpeT8cB6yS5oWh_JwzT6Lqi5fQCa2k0Qx6-66EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">؛‌OpenAI⁩ مدل جدید ‌GPT-Live-1⁩ رو معرفی کرده که مکالمات صوتی با هوش مصنوعی رو به سطح جدیدی می‌بره!
🎙️
‏این مدل میتونه تغییر لحن بده، بخنده و حتی وقتی که کاربر ناگهان حرفش رو قطع می‌کنه، طبیعی‌تر واکنش نشون بده
🗣️
‏و اما یه قابلیت خیلی جالب دیگه: میتونه به صورت آنی به حرف‌های کاربر واکنش نشون بده و حتی به عنوان مترجم همزمان کار کنه!
🌎
‏همین حالا از طریق ‌
ChatGPT Voice⁩
قابل دسترسه!
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/ArchiveTell/6809" target="_blank">📅 08:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6808">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎯
RankGrow | دستیار هوش مصنوعی برای سئو
ابزاری هوشمند که با اتصال به Google Search Console، مشکلات سئوی سایت را شناسایی کرده و لیستی از مهم‌ترین کارهایی که باید انجام دهید را ارائه می‌دهد.
🚀
⚡
ویژگی‌ها:
📊
اتصال مستقیم به Google Search Console
🤖
۷ دستیار تخصصی هوش مصنوعی برای سئو
📝
پیشنهاد بهبود محتوا، لینک‌سازی و سئوی فنی
🎯
لیست اولویت‌بندی‌شده از کارهای ضروری SEO
📈
تحلیل رقبا و کشف فرصت‌های رشد
🎁
۵ اعتبار رایگان برای شروع (بدون نیاز به کارت بانکی)
🔗
https://rankgrow.com
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/ArchiveTell/6808" target="_blank">📅 07:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6807">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کد نویسی رایگان با ابزار هوش مصنوعی FREEBUFF
💻
ابتدا به
سایت
بروید و اکانت بسازید سپس ابزار را اجرا کنید
🚀
— نصب آسان با دستور npm install -g freebuff
🛠️
— بدون نیاز به کلید، کارت یا اشتراک ماهانه
🆓
— مدل‌های پیشرفته از جمله DeepSeek V4 pro و Mimo 2.5 pro و Minimax M3
🧠
— دارای یک وب سایت برای تولید و استقرار برنامه‌ها به صورت رایگان
🌐
کد نویسی خود را با هوش مصنوعی و به صورت رایگان انجام دهید!
✨
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/6807" target="_blank">📅 04:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6806">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🎉
Claude Opus 4.8 رایگان در
Supercode (فقط یک روز)
به مناسبت لانچ Supercode در Product Hunt، این ابزار دسترسی رایگان یک‌روزه به مدل Claude Opus 4.8 را برای همه کاربران فراهم کرده است.
🚀
⚡
جزئیات:
🆓
دسترسی رایگان به Claude Opus 4.8 برای یک روز
🤖
استفاده از AI Agent در ترمینال
💻
مناسب برای کدنویسی، توسعه و مدیریت پروژه‌ها
📈
؛Supercode
تاکنون به بیش از ۹,۵۰۰ دانلود، ۸۲ ستاره GitHub و ۲۲۰ کاربر رسیده است.
اگر قصد دارید Supercode را امتحان کنید، امروز بهترین فرصت است.
🔗
https://supercode.sh
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6806" target="_blank">📅 02:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SlipNet-v2.5.5-full-release-arm64-v8a.apk</div>
  <div class="tg-doc-extra">25.7 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6798" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🕊
@SlipNet_app</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/6798" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6797">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اقا سرعتی slipnet رو اپدیت کنید
😁
😁</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/6797" target="_blank">📅 00:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🎬
FreeCut | تدوین ویدیو با هوش مصنوعی
یک ابزار متن‌باز که با کمک مدل‌های هوش مصنوعی، ویدیوهای خام را به‌صورت خودکار تدوین می‌کند؛ بدون نیاز به API پولی.
🚀
⚡
ویژگی‌ها:
✂️
حذف مکث‌ها، تپق‌ها و بخش‌های اضافی
🎨
اصلاح رنگ خودکار و افزودن زیرنویس
🎥
ساخت انیمیشن و افکت‌های تصویری
🧠
پشتیبانی از Whisper محلی (بدون API Key)
💻
سازگار با Claude Code، Codex و سایر AI Agentها
🔗
https://github.com/Moh4696/freecut
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/6796" target="_blank">📅 23:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">https://www.youtube.com/@localhost_ir</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/6795" target="_blank">📅 23:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromlocalhost(Yousef Taheri)</strong></div>
<div class="tg-text">https://www.youtube.com/@localhost_ir</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/6794" target="_blank">📅 23:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGsWzfiE0mq7_Tpx0hPYW8YsYQ2uJkHhPdwjuzyEZxnHGk81FPrbnUpBn9IjO4amJagz_n0btuQSO8s5HhVIrWclwdXp0UaEjHfoJiB4ZVtyXjtEOcLErk1ldIhsBxaFUVLIrHHi-2DP5lkGhfPRjS_mR1aV8fXkBC_QKcTrYCEpn30sLYc5_tmej-Mo9pAZ607-Sq007WPMX07dTLHTVeWMtd5GITQT-JmonI9ZGV3YS7fYpuBocyrVYi0CYYUTKsf_7-eA6MgwosZbWGSr-YXmDdJ3cXIa9V655HNAlf_S-M6lvPzlB06RnBujF2kM8ENx5KHlsdlI_YBMCyLNCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛Grok 4.5 منتشر شد
⚡️
این نسخه محصولی ویژه از ایلان ماسک است که به‌طور خاص برای برنامه‌نویسی و توسعه‌ی ربات‌ها طراحی شده است.
نکات مهم:
• این مدل به طور مشترک با شرکت Cursor توسعه داده شده و با استفاده از داده‌های واقعی میلیون‌ها برنامه‌نویس آموزش داده شده است.
• سرعت بسیار بالا: 80 توکن در ثانیه.
• قیمت بسیار مناسب: 4 برابر ارزان‌تر از Opus 4.8.
در حال حاضر، به صورت
رایگان
در Cursor و Grok Build در دسترس است.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6793" target="_blank">📅 22:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">#اختصاصی
شبیه‌سازهای پلی‌استیشن
🎮
PS1:
duckstation.org
PS2:
pcsx2.net
PS3:
rpcs3.net
PS4:
shadps4.net
PSP:
ppsspp.org
PSV:
vita3k.org
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/6791" target="_blank">📅 20:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کانفیگ اهدایی
🔥
vless://878fa338-f275-4bf6-93ea-ef47d8865f59@ps.aramvpn.kdns.fr:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QFc4pPuYwGfyKeoSWnxUkPgaDdEPCPPb2ImpxI-njxI&security=reality&sid=0586e9d2d3a6d12d&sni=www.yahoo.com&type=tcp#@ArchiveTell
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6790" target="_blank">📅 19:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d26e8a3688.mp4?token=kp98AKRH8I5ga4hcBwrgRAvfFC-jShXZvgyjh9AazYM1607JDaa12IspUZ5Nl6aWutrIstgWk2w4wM1ByXyxIIK9wKJ_lLopRsOWSwIeu2R4NDHE1h798PnWzEx9IgIVcnjvCBD9AOVtzPWXKDKnzKtV9Rr6Sf04mkdNiAPza3cv-HrjsX4vpmAZJFH9asTrcxpTQVl4dYQ8uzC0ACCv7ofUNDe8Xx75-XzTgTGU6LaVyKhToPFdBEGuPedjL6y71fN44TJLhR8LWTn2QoC1I088PA8-4dZWdFe0r796EHc-Tr5newK_SwBmI09cpAFjuxS5TAKU_Gnu9C7arNiifljBWu2_XXfcdzVjUpGFcw4viNta-JqG1QNEtBEwtT5uzpj8iQwBIRo0bVpffWW5alozkb-k9Br0gwA6NR9FFI3QgacyJ1DFCoDHxom0L_JznjbXcbZiw6LtT-bIGEVtwihVF5svw7HCwekDvj0CIoQU5P0IFGpTColPMj7pg8sbK9Pr_wnb-oMGD2gf9JQnna2QX9HeKIueqVtEwhwzgOCn7joYhIBWYUTih_2GAe_oHi63k45KgqtruXKNs2kmcfonCYC4KbtXZbqWYu6kbHPoMmSV8byjzw-TGz9CyZz64rF3u4rlnw50PcrjwaTJXQkpiW_oHocmGIn83jUwSkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d26e8a3688.mp4?token=kp98AKRH8I5ga4hcBwrgRAvfFC-jShXZvgyjh9AazYM1607JDaa12IspUZ5Nl6aWutrIstgWk2w4wM1ByXyxIIK9wKJ_lLopRsOWSwIeu2R4NDHE1h798PnWzEx9IgIVcnjvCBD9AOVtzPWXKDKnzKtV9Rr6Sf04mkdNiAPza3cv-HrjsX4vpmAZJFH9asTrcxpTQVl4dYQ8uzC0ACCv7ofUNDe8Xx75-XzTgTGU6LaVyKhToPFdBEGuPedjL6y71fN44TJLhR8LWTn2QoC1I088PA8-4dZWdFe0r796EHc-Tr5newK_SwBmI09cpAFjuxS5TAKU_Gnu9C7arNiifljBWu2_XXfcdzVjUpGFcw4viNta-JqG1QNEtBEwtT5uzpj8iQwBIRo0bVpffWW5alozkb-k9Br0gwA6NR9FFI3QgacyJ1DFCoDHxom0L_JznjbXcbZiw6LtT-bIGEVtwihVF5svw7HCwekDvj0CIoQU5P0IFGpTColPMj7pg8sbK9Pr_wnb-oMGD2gf9JQnna2QX9HeKIueqVtEwhwzgOCn7joYhIBWYUTih_2GAe_oHi63k45KgqtruXKNs2kmcfonCYC4KbtXZbqWYu6kbHPoMmSV8byjzw-TGz9CyZz64rF3u4rlnw50PcrjwaTJXQkpiW_oHocmGIn83jUwSkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چینی‌ها یک "غول" جدید برای تولید تصاویر معرفی کردند: Seedream 5.0 Pro.
ویژگی‌های این ابزار:
🔹
ویرایش لایه‌ای تصاویر
📦
‏
🔹
ترکیب چندین تصویر در یک طرح کلی
📚
‏
🔹
تنظیمات جداگانه برای سبک هر شیء
🎨
‏
🔹
ویرایش محلی مناطق انتخابی
🔍
‏
🔹
تغییر تصاویر بر اساس دستورات متنی
📝
‏
🔹
تطابق دقیق‌تر خروجی با درخواست
📊
‏
🔹
بهبود عملکرد در کار با متن داخل تصاویر
📚
‏
🔹
تولید اینفوگرافیک، نمودارها و سایر مواد بصری
📊
‏
نسخه ‌Lite⁩ رایگان در ‌
Higgsfield⁩
و ‌
Dreamina⁩
قابل آزمایشه
📦
👀
‏نسخه ‌Pro⁩ از طریق ‌API⁩ در دسترسه
🚀
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/6788" target="_blank">📅 19:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQ_F8aAwFAoKWPpGnddG_s_HCCZwigB8UoWrYGZVLIplhFzUbn3VaibT7vF90_KK7EzetzRCf9VSvg0CSli0vwNnviMCaX4QYMiPU35FOCJuABnEHb30L3zTYTxr12GTmi2pcT2A5aua83K9gDREOF1JFu3EkvV67jI_TBXhh52EZzI5vxRn-mVSeMbwtCvXtlF-3VpZaNv1qqJHBnAQmMEc7NOXiAv3M-p3PfHhVp15xht9rpPbZrzxl8oVNhgTo5SHdYk2R9-O6jOtENCunIKtB3xCVdSyzVqU0Bg9LLOwCQLGOtnXRuThTN8VgrYlDNzDpyx81F39w9z2WRuzrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرورگر
DuckDuckGo
در جدیدترین به‌روزرسانی خود قابلیتی اضافه کرده که امکان
حذف تبلیغات ویدیوهای یوتیوب
را فراهم می‌کند
🌐
این ویژگی با استفاده از فیلترهای
uBlock Origin
کار می‌کند. هرچند ممکن است در برخی مواقع
زمان بارگذاری
یا
بافر شدن
ویدیوها کمی بیشتر شود، اما در عوض می‌تواند تجربه‌ای بدون
تبلیغات
و روان‌تر هنگام تماشای ویدیوهای یوتیوب ارائه د
هد
😎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6787" target="_blank">📅 18:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎥
Recordly | ضبط و ویرایش حرفه‌ای صفحه‌نمایش
✨
یک نرم‌افزار متن‌باز برای ضبط صفحه نمایش که ابزارهای ویرایش را هم در خودش دارد؛ مناسب ساخت ویدیوهای آموزشی، دمو و معرفی محصول.
🚀
⚡
ویژگی‌ها:
🎬
ضبط صفحه، پنجره و صدا
🖱️
زوم خودکار، افکت‌های موس و حباب وب‌کم
✂️
تایم‌لاین ویرایش، برش و افزودن متن
📤
خروجی MP4 و GIF
💻
پشتیبانی از ویندوز، لینوکس و macOS
🔗
https://github.com/webadderallorg/Recordly
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/6786" target="_blank">📅 18:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6785">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🛡
Dangerzone | تبدیل فایل‌های خطرناک به PDF امن
یک ابزار متن‌باز برای باز کردن امن فایل‌های مشکوک مثل PDF، فایل‌های آفیس و تصاویر؛ بدون نیاز به اعتماد به فایل اصلی.
🛡
⚡️
نحوه کار:
🗂
فایل داخل یک محیط ایزوله (Sandbox) پردازش می‌شود
🖼
محتوا به پیکسل تبدیل شده و دوباره به PDF جدید ساخته می‌شود
🚫
کدهای مخفی و عناصر فعال فایل اصلی حذف می‌شوند
✨
پشتیبانی از:
📄
PDF
📝
Word / Excel / PowerPoint
🖼
فرمت‌های تصویری مختلف
💻
قابل استفاده در:
Windows | macOS | Linux
📎
https://github.com/freedomofpress/dangerzone
🐍
زبان: Python
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/6785" target="_blank">📅 17:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FB0Viu7jFbUY3YtjYJfpJLHGcLAQ_d-0d3N3yZc5ZZxr9lvEymhlkeZxwX_oHoiULmiGEOsUC3YTr-C28sd0f5Nnszex66p7Selo10HT0FeXmDjRHvg84BXDgsC7WFsZIDLMt7yE43eQTqAA-LOJ_nGNvgVdfVzryXzxXdEChX8TK8HM96MGy2y4f0tyg0pZFX-0In_-_TeyLi8ELknV9Oq7OPfmb5aUHhjC3nZKdkBrC90FEdoTKyaIjcjhRm4onVVMVntUmhfuy51Xd1VYRKlUOU2Sd0zkN5uVBYSRl-oyfBdQ1aELQgQo80jextvtosJkFczQDUkERbq_ar1KxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">SubFarsiPro v5.0
📹
این ابزار، یک دستیار حرفه‌ای، پرسرعت و متن‌باز برای استخراج زیرنویس از ویدیوها و ترجمه دقیق اون‌ها به زبان فارسی (با لحن طبیعی و محاوره‌ای) هست
GitHub
🐱
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6783" target="_blank">📅 15:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">📊
دنبال معتبرترین رتبه‌بندی مدل‌های هوش مصنوعی هستی؟
اگر می‌خواهی عملکرد واقعی مدل‌های هوش مصنوعی را مقایسه کنی، این دو سایت را از دست نده:
🌐
Artificial Analysis
📈
یکی از کامل‌ترین لیدربوردها برای مقایسه مدل‌ها از نظر کیفیت، سرعت، هزینه، کدنویسی و ده‌ها بنچمارک معتبر.
🔗
https://artificialanalysis.ai
💻
DeepSWE
🧑‍💻
یکی از بهترین بنچمارک‌ها برای سنجش توانایی برنامه‌نویسی مدل‌ها با استفاده از پروژه‌های واقعی و جدید، نه سؤالات قدیمی و حفظ‌شده.
🔗
https://deepswe.datacurve.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/6782" target="_blank">📅 15:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammad</strong></div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/6780" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ارسالی یکی از یوزرای گل
👇</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6779" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor لینک ویدیو آموزش:  https://youtu.be/pN3LxWzDtKI  خود پروژه:  https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell | Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6778" target="_blank">📅 13:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔥
دسترسی رایگان به هوش مصنوعی قدرتمند Fable 5
اگر دنبال تست مدل‌های پیشرفته هوش مصنوعی برای
برنامه‌نویسی، تحلیل و کارهای پیچیده
هستید، این روش می‌تواند جالب باشد.
🌐
پلتفرم
Tasklet.ai
امکان استفاده محدود رایگان از این مدل را فراهم کرده:
✅
۵۶۰۰ کردیت ماهانه
✅
۳۰۰ کردیت روزانه
✅
مناسب برای تست و استفاده‌های روزمره
📌
روش استفاده:
1️⃣
با ایمیل ثبت‌نام کنید
2️⃣
وارد پنل شوید
3️⃣
از بخش انتخاب مدل،
Fable 5
را انتخاب کنید
هر بار کردیتتون تموم شد میتونید اکانت جدید بزنید
🤝🏻
لینک
🔗
:
Tasklet.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6777" target="_blank">📅 13:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🗂
نام‌گذاری هوشمند فایل‌ها با هوش مصنوعی (
Renamer.ai
)
پایانی برای کابوس فایل‌های بی‌نام‌و‌نشان مثل
Scan_001.pdf
. این ابزار به جای تغییر ساده متنِ اسم فایل، محتوای متنی و تصویری داخل آن را آنالیز کرده و نام‌های دقیق و جستجوپذیر پیشنهاد می‌دهد.
🔥
ویژگی‌های مهم:
*
🧠
درک محتوای فایل:
استخراج فاکتورها، تاریخ‌ها، نام شرکت‌ها و موضوعات داخل اسناد، تصاویر، اکسل و PDF به کمک فناوری OCR.
*
📸
سیستم پیش‌نمایش:
امکان بررسی و تایید اسامی پیشنهادی قبل از اعمال نهایی روی سیستم برای جلوگیری از خطا.
*
📂
پوشه جادویی (Magic Folders):
مانیتور خودکار پوشه‌های انتخابی (مثل Downloads) و نام‌گذاری آنی و اتوماتیک فایل‌های جدید.
*
⚠️
نکته:
نسخه رایگان محدود به ۲۵ فایل در ماه است. همچنین به دلیل پردازش ابری، بهتر است برای اسناد فوق‌محرمانه و اطلاعات حساس مالی استفاده نشود.
🔗
لینک وب‌سایت ابزار
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/ArchiveTell/6776" target="_blank">📅 12:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🌐
وب‌گردی و انجام خودکار کارها با هوش مصنوعی (Browser Use)
یک فریم‌ورک اوپن‌سورس (پایتون) که مرورگر شما رو در اختیار مدل‌های هوش مصنوعی (مثل GPT و Claude) قرار میده تا کارهای اینترنتی رو دقیقاً مثل یک انسان براتون انجام بدن.
🔥
ویژگی‌های مهم:
🤖
اجرای خودکار وظایف:
کافیه با زبان طبیعی بهش دستور بدید (مثلاً "این فرم استخدام رو با اطلاعات رزومه من پر کن" یا "این لیست رو به سبد خریدم اضافه کن").
🧠
پشتیبانی از انواع LLMها:
کاملاً سازگار با مدل‌های معروف و حتی مدل‌های آفلاین/لوکال.
💻
ابزار CLI حرفه‌ای:
قابلیت اتصال مستقیم و راحت به ایجنت‌های کدنویسی.
⚡️
جایگزین مدرن:
بدون نیاز به درگیری با ابزارهای قدیمی مثل سلنیوم، خودش با المان‌های سایت تعامل می‌کنه.
🔗
لینک مخزن گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/6775" target="_blank">📅 11:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHx7jLDwkpkxG8a-aFiznNpzz_rNGIqB7RxPTguflRZlPQYP_B9wrb5lVX2iCES0NmN2SyMH3Gxj51b58h7qwnNt8DSlxTp1SrjYE33LHqJLFE7xvVJ7LF0olpVvvlQwfcMWjUBxzA5E26aN8pFL5N-ZMGRktsoGCkGnyEXx-abEcDKHYQ5nCkrT7acGt2cRKb_vZIiH5jwKYQe6bX6ki_HcKaNoKbLNKRoO4KUrg9r8fLfmOPts1HFkLngfZNNUWVWRuUMievXCMGwCJFz-T0RUz5I6O691c5RK5dqFb4LQJN4H6tvBV9KdsuhiViC686k9mEaa7sclCOYsq1AcYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
معرفی Google Flow
این سایت جدیدی نیست ولی خب بعضی دوستان دیدم نمیشناسنش گفتم معرفیش کنم
😁
اگه دنبال یه ابزار رایگان و قدرتمند برای ساخت تصویر با هوش مصنوعی هستی،
Google Flow
یکی از بهترین گزینه‌هاست.
ویژگی‌ها:
✨
تولید تصاویر با مدل‌های
NanoBanana 2
و
NanoBanana Pro
🖼️
ویرایش تصاویر (چه ساخته‌شده و چه آپلودی) با پرامپت
🪙
ساخت تصویر با
۰ سکه
(رایگان)
📚
امکان ساخت همزمان چند تصویر و ادامه ویرایش روی بهترین نتیجه
🎥
قابلیت تولید ویدیو (با محدودیت بیشتر)
📌
لینک:
https://labs.google/fx/tools/flow
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6774" target="_blank">📅 11:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6773">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JI3ZY6ZVgnkX9trS7Hm49baNaFv_MPsoP8z8HanDFLbG0eWkxbgZQsrvURz-bxco5aYsZw63n06XrIQHj_wsuvpptwJWLD1hyGBaxdsT3NAAJ_Rfv5VsJ62KKWiW_LmAHzIsEUTlc2NzMf4J22_StQTJcG269w8cd69QP4hjn6eCo9h_WpMhE783X--vv0yVM2FYSDzfXYanEC0AJHib6KP1oGl4A0FGvEqXs3eO5eUZbmYjtya-fw59-r6Ji7hl_ofGkk7MWn9ZDS7RZb-Pj9rv8LFSdvZP9I70EJYiNxOiDP-Bt1Q0FElKy-h_RXRQACdf4FhE5vA-ik1FynToOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
WLLPR | ژنراتور والپیپرهای مینیمال
اگه از والپیپرهای تکراری خسته شدی، با
WLLPR
می‌تونی توی چند ثانیه والپیپرهای مینیمال و جذاب بسازی؛ اونم دقیقاً با رنگ و استایلی که دوست داری.
🎨
⚡
ویژگی‌ها:
• ساخت والپیپر برای
📱
موبایل و
🖥
دسکتاپ (4K)
• انتخاب رنگ، طرح و استایل دلخواه
• تولید نامحدود والپیپر با یک کلیک
• هماهنگ شدن رنگ رابط کاربری گوشی با والپیپر در بسیاری از گوشی‌های اندرویدی
🌐
لینک سایت:
https://bypedroneres.github.io/ai/
➖
➖
➖
➖
➖
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/6773" target="_blank">📅 10:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6772">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPZHefVEcb6ZLejUycFIi8ykkBPXX5zV0NGa2345Xft6ay_UN4_UaZVrLO3ABwo96Bw7G1vWJk3aTZyh-LPR49mnw1m4ekk_PTfuIb7O5OoION-LuDANu_-oNgZf94375r5lqqAKvH8-1iQ7z5Ont25-NkHA6HYWK0ZI6ciq9omnthnqmEjTZz7WXOvOJUtdk_8EjrGmPaMF76PxxpubqYkJjI0rkxKOjs9OWKK9EF9Xw6KHAWdLw7SdFt3KvrsmQgU6Z54ydmFrXd60D5wEdsEJrD-1IKS_QiH3CFwu4fD1xM0UkQWZQNiTs6j9vqnM1pap-n2Q3J5o0nrf0qW7iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت OpenAI
نسخه‌ی GPT-5.6 را برای Sol، Terra و Luna از فردا راه‌اندازی می‌کند!
🚀
دسترسی زودهنگام از همین حالا برای کاربران در سراسر جهان فراهم شده، می‌توانید با خیال راحت وارد شوید و آن را بررسی کنید.
🌍
🔍
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/ArchiveTell/6772" target="_blank">📅 10:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAXUSZ8Hcdym-GbX8Ga_nmW4j50QrBzp4VMBMvxJgm2XPnP5qD08E2cIMw0UWI-65KFC7R1_CXKGOX1aq_nuJRSJ6ps0IBj7-KWfmLyRltsofl7wuoD6lNRt0VVfqSXCfhySk0uLInwQjsnB_4nmtNBefbXIwo7ENjblBL-PSm3-pBhDHiRoyzxamaJeK5tva8Yl3iIYIM4-6WjQZQRFsxyKDj0h9918-DjSz6BNymWB0obPclEkRf_pyKRwXEroruDTs9OqYUzuvPz---YSka1KBA4wwDQkx0iwA3Y7KXpuX-NfozlWRHaZZP3LKH5ylYAWgBe4SNnmoORUN5KoGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">؛Constrict ناجی شما در فشرده‌سازی ویدیو!
📹
- ویدیو را آپلود کنید و اندازه مورد نظر را انتخاب کنید.
- بدون نیاز به سرویس‌های آنلاین و دستکاری‌های پیچیده در کدگذاری.
ساده، سریع و کاربردی!
https://github.com/Wartybix/Constrict
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/ArchiveTell/6771" target="_blank">📅 08:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6xnvZ5qOC9jQvuupaKwnsYQC82uHQmQneWMX55qJr1n5d5Zsci9mckToofDUkaUL3jGF6PkUzupUCEInc7xjlGFPMqEwFzY7U2ZGjMnqYZryk_E5RQzYr5ybmeFItaH5tVQuUPc06QmGAf1yufRaO464dgSNQHtjtTrpQtfN7pDO4zeTiVK_bOf3RsTZrkW1Z82fhWEkx_z6pnG-12pUcvtGeoN4Dl1LDjZmJgfRYkaNVkyvye_zDbMzcXFtAsna8ITKc3FAVeKc8-um2unIrY5GVl_k0Uq0_fschvJgQbC4VnCkIgJXYphsxhE80kA7-RO09Yg4QfC6IlPun7lNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
تحلیل ویدیوهای یوتیوب، تیک‌تاک و فایل‌های محلی با هوش مصنوعی
؛
Claude Video
یک ابزار متن‌باز است که امکان تحلیل ویدیوها را برای دستیارهای هوش مصنوعی فراهم می‌کند. کافی است لینک یک ویدیو یا فایل محلی را به آن بدهید تا فریم‌های تصویر و متن گفتار را استخراج کرده و در اختیار مدل قرار دهد؛ سپس می‌توانید درباره محتوای ویدیو سؤال بپرسید یا خلاصه آن را دریافت کنید.
⚡️
ویژگی‌های کلیدی:
-
🎬
پشتیبانی از ویدیوهای
YouTube، TikTok، X، Instagram، Loom
و صدها وب‌سایت دیگر
-
📂
تحلیل فایل‌های محلی مانند
MP4، MOV، MKV
و
WebM
-
🖼
استخراج خودکار فریم‌های مهم و متن گفتار (Transcript)
-
🧠
امکان پرسش درباره بخش‌های خاص ویدیو، خلاصه‌سازی و تحلیل محتوای تصویری
-
🤖
سازگار با
Claude Code، Claude Web، Codex
و ابزارهای مشابه
-
🔓
متن‌باز با
لایسنس MIT
🔗
گیت‌هاب پروژه:
https://github.com/bradautomates/claude-video
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/ArchiveTell/6770" target="_blank">📅 08:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">#Android
#Gaming
🎮
MuMuPlayer 6.0 منتشر شد
نسخه جدید شبیه‌ساز اندروید MuMuPlayer با تمرکز بر عملکرد بهتر و سازگاری بیشتر برای اجرای بازی‌های اندرویدی عرضه شد.
ویژگی‌های جدید:
•
🤖
پشتیبانی هم‌زمان از Android 12 و Android 15
•
🚀
عملکرد روان‌تر و FPS بالاتر
•
🖥
بهبود اجرای چندین Instance
•
🎯
سازگاری بیشتر با بازی‌های جدید
•
⚡
ارتقا بدون از دست رفتن تنظیمات و Macroها
مناسب برای اجرای بازی‌هایی مانند Roblox، استفاده از چند حساب کاربری و تست برنامه‌ها روی نسخه‌های مختلف اندروید.
🔗
https://www.mumuplayer.com
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/6769" target="_blank">📅 05:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tl2RqkGcboJVjvgN2qcdMCFvys3UD4DbQOzgXjPN4HqV-ktN9WlhxEwGHLR5sngOW75FrfbZLxaEHDlNWpbxNR30lqv5f8Jvc89Jm6MUh7rLWtmLvb18j5tONF1fosqeg-f2pLR1JKxmc5ke4NevIKmLIYXK_ID6jhTSyuoMqbxsPjMGWMd8_sg8GD1V8B2qi_4Qrewdz5tIWknhevLyuakY5wxsaXYAS2BU_GqV7eT0f-tmdH2RjQ_UX-eNgk8ddCRaS_dg8JE5YqbQtoNA4g5mXbWSMvGZazNUgOpRC8SrmPISytsF1oePI1c38NA1yHBVatO-RIaEEOc218qfAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
یادگیری شخصی با هوش مصنوعی
موضوع رو بهش بده؛ بر اساس سطح و درک شما آموزش می‌سازه.
✅
آموزش مرحله‌به‌مرحله
✅
امکان پرسیدن سؤال حین آموزش
✅
مناسب هر سطحی
🔗
https://peras.app/
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6768" target="_blank">📅 01:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏
🎁
100 هزار توکن رایگان ( 3 روزه )
‏دسترسی به مدل‌های زیر و صدها مدل دیگر برای کدنویسی :
🔹
‌GLM-5.2⁩
🔹
‌Qwythos⁩
🔹
‌Deepseek 4 pro⁩
🔹
‌Kimi k2.7⁩
🔹
‌Minimax M3⁩
🔹
‌Mimo 2.5⁩
‏
💡
ویژگی خاص:
امکان استفاده از مدل‌های ترکیبی ساخته‌شده توسط کاربران (مثل ترکیب ‌Qwen + Fable)⁩
🔗
‌featherless.ai
⁩
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/6767" target="_blank">📅 01:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtZgg9shoYER6mt1-4D3S_60R8R4SK9E6wqfoHUIiCU2E8WeCRpmtjS2jBV3cPYuB9BxEY_vdFNJ3t1bJ4Y6SeNeXLEf3tRXVMNvIt8kDkNn8tLZT_RCt4sFl6swqoPHDt2Xs9fI4ygxsEIE_46FR4s1g8hflX7EsnFaBWXi-r2inIJYApxBrPU49eqt2RSgu_w88E-p0aBsOzqeDwF4IsFnXXRfP2bNsdtZt-bLYxw4kDCIi3C7K9YJugz6cZ9T1Fc_K9Isg-EU2k7skRVio0cjrFsgr8SsaGl0CjMqq2B2La0B888EV_zDFOLXQhTPA9bc481_Wr65aXvH6T6goQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
PixelRAG
یک پروژه متن‌باز برای Visual RAG که به‌جای متن، اسناد، صفحات وب و PDFها را به اسکرین‌شات تبدیل می‌کند و جستجو را بر اساس محتوای بصری انجام می‌دهد؛ بنابراین جدول‌ها، نمودارها و چیدمان صفحه حفظ می‌شوند.
ویژگی‌ها:
•
🖼
جستجوی مبتنی بر تصویر صفحات
•
📄
پشتیبانی از وب، PDF و تصاویر
•
🤖
سازگار با مدل‌های چندوجهی (Vision)
•
⚡
ابزار CLI برای ساخت و جستجوی ایندکس
•
🌍
API و نسخه دمو آماده استفاده
🔗
https://github.com/StarTrail-org/PixelRAG
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/6765" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔐
VoidAuth
یک سرویس متن‌باز برای
SSO
و مدیریت کاربران در محیط‌های Self-Hosted.
ویژگی‌ها:
•
🌐
OIDC Provider
•
📖
LDAP Server
•
👥
مدیریت کاربران و گروه‌ها
•
🔑
MFA
و
Passkeys
•
📨
دعوت و ثبت‌نام کاربران
•
🎨
شخصی‌سازی رابط کاربری
•
🔒
رمزنگاری داده‌ها (
PostgreSQL
/
SQLite
)
⚠️
هنوز Audit امنیتی نشده؛ برای Production با بررسی کافی استفاده کنید.
🔗
https://github.com/voidauth/voidauth
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/6764" target="_blank">📅 00:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🖼
جستجوی معکوس تصویر با TinEye
اگر می‌خواهید منبع اصلی یک تصویر را پیدا کنید، نسخه‌های باکیفیت‌تر آن را ببینید یا وب‌سایت‌هایی که از آن استفاده کرده‌اند را پیدا کنید،
TinEye
یکی از بهترین موتورهای جستجوی معکوس تصویر است.
⚡️
قابلیت‌ها:
-
🔍
جستجو با آپلود تصویر یا وارد کردن لینک آن
-
🌐
پیدا کردن صفحات وبی که تصویر در آن‌ها منتشر شده است
-
🖼
شناسایی نسخه‌های ویرایش‌شده، برش‌خورده یا تغییر اندازه‌یافته
-
📈
مرتب‌سازی نتایج بر اساس اولین انتشار، جدیدترین، بزرگ‌ترین یا بیشترین تغییر
-
🔒
حفظ حریم خصوصی؛ تصاویر آپلودشده ذخیره یا ایندکس نمی‌شوند. TTinEye+1
🔗
وب‌سایت:
https://tineye.com
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6763" target="_blank">📅 22:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6762">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVMESswR9Qka_vbXDyZ_ycaFit-fxsFMVBydEcmqcCLTSjPDj4K9qXo07nr3tbya99Rip4MAyZNXQVEtmUHE3K6M1rOgVxs_RW3N_Zrr-0_44fSf2JsSzH60jsiECXaMI4dqiWGA6WtkecQL7f1aZFvkuDJ21JLku4_jupQa3LZZCJtyd1JEmW16Z5CtW7uBH6eGDL4yp0CsoCD1x93ms4t1s8POvjsBNMb96ZOmmwocr6vnRuG1p1XKvcl9F5p3aKhSWunvYNtPh-RxxK62zICppC4tL33KodeZN2iAyLDLcufmt8PG8YZw9eyf4dlnozMvJJ0Yeq4jUNy_5wz-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
تولید صدا با Pocket TTS روی پردازنده معمولی (CPU)
این ابزار یک مدل
تبدیل متن به گفتار (TTS)
بسیار سبک با
۱۰۰ میلیون پارامتر
است که بدون نیاز به
GPU
، پرداخت هزینه
API
یا وابستگی به سرویس‌های ابری اجرا می‌شود.
⚡️
ویژگی‌های کلیدی:
-
🚀
تولید اولین بخش صدا در حدود
۲۰۰ میلی‌ثانیه
و تا
۶ برابر سریع‌تر از زمان واقعی
روی پردازنده‌های مک.
-
🎙
امکان
شبیه‌سازی صدا (Voice Cloning)
تنها با یک نمونه صدای
۵ ثانیه‌ای
.
-
🌍
پشتیبانی پیش‌فرض از
۶ زبان
: انگلیسی، فرانسوی، آلمانی، پرتغالی، ایتالیایی و اسپانیایی.
-
🔓
کاملاً
متن‌باز (Open Source)
با
لایسنس MIT
و آموزش‌دیده فقط با داده‌های عمومی.
🔗
لینک گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6762" target="_blank">📅 19:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCZ-iMgJOfR1UAFiPYNlXUR2hj2XY2aD2GCDD2Y0JSEyoDVTB6BxRNEkUWx7WXCslKGVCnG_R3kE8MXaygrwvA4xZ38hW4nJ6DgfcHkwp1FdfJgtud28Tq5fqMC1fHeAm33nhhOZejAJvAEBA1NJmb4PLSUpIa18zuFWixIJ5mZLf1c9yf9W46mOk2x0KooXwHycc1ik4_T3sOndkXttVVBSraTbhbwRGyuGG_FYO7KzwlcvXRAPlb-EC09v2nwuOjmEskhACT_sYSiF6DRdX6CLdI_hfpB-IT0ZL868QwJ-d1Q6wlPzO6lm2zosZvRw4eM3LSuusIiGn6TvpicNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه به دنیای تکنولوژی، لینوکس، شبکه، سرور و ابزارای خفن علاقه‌مندین، یه سر به کانال لوکال هاست بزنین
توی localhost کلی آموزش، نکته کاربردی و تجربه واقعی از کار با سیستم‌ها هست. خلاصه هر چی از دل پروژه‌ها درمیاد، باهاتون به اشتراک می‌ذاره!
🅰
t.me/localhost_ir</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6761" target="_blank">📅 19:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJZsk7iVLf8QJpcZgbDSuM5mvvQkmInIaT5KItTeF3yGz0KH1AJUl8G_wtOlwUX_y5r7VOFn2M3PjHhzngtSMslKoNnTN50cTyj1oxoTSmomhoqL5rOk6HASDCwhFk0er6UaHp3PrAD2GoSxPr0U90EDgguWT3z2yHGhnHBlsdjwUOfOMJEq8kfPTaOqaDmRTHSpNazyGeSsFbylLNnGcXYckyqMmIEmliQamhDyRo06iMaAE9XVVkcvtGqPaN3IEYmHzf7SchoZt1wEwINJrLO8T9K5woqbsv3PhaXWHm9xI8b7k7N5P-HZ-0YVHGfXp6YHGnVtc1Q2Hn-mjytJJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلود و مدیریت فایل‌های تلگرام با TDL
یک ابزار متن‌باز و قدرتمند برای دانلود و مدیریت محتوای تلگرام است که امکاناتی فراتر از یک دانلودر ساده ارائه می‌دهد. این برنامه با مصرف کم منابع، سرعت بالا و قابلیت اجرای مستقل، گزینه‌ای مناسب برای کاربران حرفه‌ای تلگرام محسوب می‌شود.
⚡️
ویژگی‌های کلیدی:
📦
اجرای برنامه به‌صورت تک‌فایل (بدون نیاز به نصب)
-
🚀
مصرف بسیار کم منابع سیستم و استفاده حداکثری از پهنای باند
-
⚡️
سرعت دانلود بالاتر از کلاینت رسمی تلگرام
-
🔒
دانلود فایل‌ها از چت‌های محافظت‌شده (Protected Chats)
-
🔄
فوروارد پیام‌ها با مسیریابی هوشمند و جایگزینی خودکار در صورت خطا
-
⬆️
امکان آپلود فایل به تلگرام
-
📄
خروجی گرفتن از پیام‌ها، اعضا و مشترکین در قالب JSON
-
🌐
متن‌باز با لایسنس AGPL-3.0
🔗
گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6760" target="_blank">📅 17:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVFcqhNA5KOIAxTi0WReKWX9sFeDg7CpmI7d7ZCdyL3DSyp1nQ0u6_FsC98p3HvogN4qThckG7x0nLEvAcvrvYE8pLWSUfdM-81_b_vy4MNXyHAUD90_sAqO5cl3w1OExQsyL5D8RYQV8HtOgcTKtqNct5hHr0IVCJikE2DhynO-w2jwcgsZbkC0utpnDiWVM7Qc6K8_t-dgFs0_wPdy6zgiqf5MFELU4f5IqOKxPV4_pWdcmdhcA3XI5P6fz2__9ADwsR55ncu5E2jVt-LNxtkTh5-musGgNKR3juBqVAJxPCbHCN3ZEeu79SN9jh1Wen-3NcjaX_i3MyAQ9gmUVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهبود کیفیت عکس‌ها تا رزولوشن 4K با استفاده از ChatGPT
عکس شما را بهبود می بخشد و جزئیات را تا حد امکان حفظ میکند.
😮
پرامپت :
Restore and enhance an old damaged photo. Remove scratches, stains, and noise. Reconstruct faded or torn areas while preserving original details. Slightly sharpen the image for better clarity, but keep it realistic. Apply natural and era-appropriate colors to skin, hair, and clothing. Use a soft, balanced background color without being too striking. The final result should look like an old photo that has been realistically restored and colorized, while respecting its original appearance.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/6759" target="_blank">📅 11:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k68GeEH2JA6dnLk1VZObtGK7FD47Jva6Lhgo3UhICY-3vLRbAXZV-Xi4x_TrBgPVFeq1zlScl0BP-TgQm8FrDzvBTxgoVO7KPaJanGLMsXsmLbjNOt6DC1Zj9nKuODAdJPW_dv2nAI-pYCdgR7wKFg1jHODtqUidaYWowLeNSoBHM50mONTxUKK4hMOa1g-HPh1_R-TeH9wTnuUq6Gox7ZE1IkiDTc0hedxuGffublX6QrauwNPouaik2yrid7DPsxvdfIU2VJVbKl0vPccsjtB1tUHIdGcfpWmFNPfqCRA_pyTdGWbX_tbAxsg3I16Sfkdr5dksaXn8G7wSRz75Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
اپ‌استور متن‌باز و جایگزین Appteka برای اندروید
یک مارکت رایگان برای دانلود، مدیریت و به اشتراک‌گذاری برنامه‌های اندرویدی که بر پایه مشارکت کاربران (Community-driven) فعالیت می‌کند.
🔥
ویژگی‌های مهم:
*
📦
استخراج APK:
خروجی گرفتن از برنامه‌های نصب‌شده (حتی برنامه‌های سیستمی) بدون نیاز به روت (Root).
*
💾
مدیریت فایل‌ها:
قابلیت بکاپ‌گیری، بازیابی و نصب مستقیم اپلیکیشن‌ها از داخل خود استور.
*
💬
تعامل کاربری:
دارای چت گروهی، سیستم نقد و بررسی، لیست علاقه‌مندی‌ها و دریافت نوتیفیکیشن آپدیت‌ها.
*
🔒
امنیت:
اسکن خودکار برنامه‌های آپلود شده (از آنجا که محتوا توسط کاربران قرار می‌گیرد، بررسی منبع قبل از نصب پیشنهاد می‌شود).
*مناسب برای توسعه‌دهندگانی که می‌خواهند برنامه‌هایشان را راحت منتشر کنند یا کاربرانی که به دنبال یک استور بدون محدودیت و ابزاری برای استخراج APK هستند.*
🔗
[لینک دانلود یا گیت‌هاب پروژه
]
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/6757" target="_blank">📅 10:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675041278d.mp4?token=O_7ddLJ7T85QtKSq73T0OQpQHEv5BIX2mx5VWX5yePZ3U1ilJGVsGpsJnuXROiu6vEoRUVqIcReAXqJ9-ddVHQvU4dJyH2B58gJ9wNY9ozHYs3XCYcuqZBPWEXBHkM7-Wf5SF0-jyg7ZJf2Uxh_eCerW_53SejaxNCe4fIt4POegpt6XG97s9ABe0V219r1fXQpNSEFyacutOFetz1PqP5pEriGR4weKvccE-LGDohyW9PTm28WkD35QMZqY9wRMKb_g_R4I6zQqLLtSv9Phm_0jKR3DooUQ0FKC916TjoqOdm1KdRQcD-G09rg9Wcb33FnC21DVg_iARs7HvwPMKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675041278d.mp4?token=O_7ddLJ7T85QtKSq73T0OQpQHEv5BIX2mx5VWX5yePZ3U1ilJGVsGpsJnuXROiu6vEoRUVqIcReAXqJ9-ddVHQvU4dJyH2B58gJ9wNY9ozHYs3XCYcuqZBPWEXBHkM7-Wf5SF0-jyg7ZJf2Uxh_eCerW_53SejaxNCe4fIt4POegpt6XG97s9ABe0V219r1fXQpNSEFyacutOFetz1PqP5pEriGR4weKvccE-LGDohyW9PTm28WkD35QMZqY9wRMKb_g_R4I6zQqLLtSv9Phm_0jKR3DooUQ0FKC916TjoqOdm1KdRQcD-G09rg9Wcb33FnC21DVg_iARs7HvwPMKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6756" target="_blank">📅 10:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">📱
تست خودکار رابط کاربری و اپلیکیشن‌ها با Maestro
یک فریم‌ورک متن‌باز فوق‌العاده برای تست End-to-End (E2E) در اندروید، iOS و وب. با این ابزار نیازی به کدهای پیچیده تست (مثل Appium یا Selenium) ندارید و سناریوها رو خیلی راحت با فرمت ساده و خوانای YAML می‌نویسید.
🔥
ویژگی‌های مهم:
*
📱
کراس‌پلتفرم:
پشتیبانی از برنامه‌های Native، فلاتر و React Native.
*
⚡️
اجرای هوشمند:
بدون نیاز به کامپایل فایل‌ها، همراه با سیستم کنترل تاخیر (Smart Waiting) برای جلوگیری از خطای لود نشدن المان‌ها.
*
🖥
ابزار بصری:
دارای یک محیط رایگان (Maestro Studio) برای ساخت و رکورد تست‌ها به صورت ویژوال و بدون نیاز به ترمینال.
🔗
لینک مخزن گیت‌هاب پروژه
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6755" target="_blank">📅 10:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚀
۳۰ سایت رایگان ساخت ویدیو با هوش مصنوعی
#اختصاصی
اگر دنبال
Veo 3، Sora 2، Kling
و سایر مدل‌های ساخت ویدیو هستید، این لیست را از دست ندهید.
⭐️
بهترین‌ها
VeoAIFree
→
https://veoaifree.com
(بدون ثبت‌نام و واترمارک)
Vixdo
→
https://vixdo.art
(۱۷۰ اعتبار رایگان + بدون ثبت‌نام)
Pollo AI
→
https://pollo.ai/m/google-veo-3
(چندین مدل در یک پلتفرم)
GlobalGPT
→
https://www.glbgpt.com
(Veo، Sora، Kling و Wan)
Leonardo AI
→
https://leonardo.ai
(اعتبار رایگان هفتگی)
🎁
بدون ثبت‌نام
VeoAIFree • TryVeo3 • AIVideoGenerator • Veo3Free • Videomaker
💰
اعتبار رایگان روزانه
VeoE • EaseMate •
Veo3.us
• AIEase • Aitubo • Pixnova • SeaArt
🧩
پلتفرم‌های چندمدلی
Veo3AI • Pollo AI • GlobalGPT •
Media.io
• Novi AI
🎬
ابزارهای تخصصی
Digen
→ Lip Sync
MindVideo
→ انتخاب نسبت تصویر
DomoAI
→ تبدیل تصویر به ویدیو
Klap
→ تبدیل ویدیوهای بلند به Shorts و Reels
Fal.ai
و
Eachlabs
→ مناسب توسعه‌دهندگان
💾
این پست را ذخیره کنید؛ احتمالاً بخشی از این سرویس‌ها در آینده پولی یا محدود خواهند شد.
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/ArchiveTell/6754" target="_blank">📅 09:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9xP_IcL-4LWyOsTU13u6mbEbaQn1XCahTudyYXOlatP-rDkFcTGL2B8vhClL4eEouFIWRQfb7Ei1_6CtuY121PHnqhfdZlLmTYy3bN8Rp4Z97iuMdmbWIc4o-I1qoANsHUPD95eI-dSTQ4SrVkgq1pu1S0KN3e4ndPsg-fh8MTn2TtP1fVp1Bg-2GBzk_r9lq5n8-EnpSIeWCgUUO9qsfI4GPChqs1Xvv4MINnD5ZkvRhtKuFxDmB5c3WPZs54SX3eDAm8Vsvo6NTFmwOu0lgraJyRoGce9VworgsL-ss-wV5qf3UVksCzKEm8T0DTp5KNhdOlSNbJm48xr7j307g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان بقول نیچه
در چنین گفت زرتشت
«من از خردِ خویش به جان آمده‌ام، چون زنبوری که انگبین [عسل] بسیار گرد آورده باشد. نیازمندِ دست‌هایی هستم که به سویم دراز شوند. می‌خواهم ارزانی دارم و بخش کنم...»
بیاین مثه نیچه باشین و این عسل و انگبین چنل رو به سوی دستان دراز بسپارید
نیاز داریم به حمایت شما
❤️‍🔥
https://t.me/ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6752" target="_blank">📅 01:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor لینک ویدیو آموزش:  https://youtu.be/pN3LxWzDtKI  خود پروژه:  https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell | Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6751" target="_blank">📅 00:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مدیریت سرور مجازی با هوش مصنوعی (بدون دانش لینوکس!) | آموزش VPS Supervisor
لینک ویدیو آموزش:
https://youtu.be/pN3LxWzDtKI
خود پروژه:
https://github.com/faithsaly5-stack/VPS_Supervisor
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6750" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نیاز داری سورس کد کامل یه سایت (به همراه تمام فایل‌ها، تصاویر و CSS) رو یکجا برای استفاده آفلاین دانلود کنی؟
💾
🕸
ابزار اوپن‌سورس Website-Downloader با استفاده از قدرت wget کل سایت رو میرور (Mirror) می‌کنه و یک فایل فشرده بهت تحویل میده.
🧵
👇
#توسعه_وب
#اوپن_سورس
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6749" target="_blank">📅 22:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlkF0NdGCboCl-HUYuaCuOviR_Mhc8BNgtruldn6mwdU9LzOM3CcpMJtKX9iFgmiHA_i3rpNjVIsuuMoN95HaZodW_woTRvlSpqc3nHtheJae_rLII0b3VonkqZwFVskohQGP9gYP2Upr6c1jRFmf_XqOFfEyd7auZI__Hm84qujdyFqDTpUSE6NQXTGH51THMHyAnXNUgiMF0rngl2aGlrU4408Y9jnruvIn9sylKMHJUHrs6NCJJsTf_IMBYJNOoWFzz6Og7oPErLqf-OF0Ug75KIP2_5MyLwOr3Xuowth3i72Ar9jhf4dqj7HGCGkNb5I0q2JtOci2zMeAZklfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/ArchiveTell/status/2074191361432035554</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6748" target="_blank">📅 21:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C11TcPuncUlYOpwvEh8a6sWz0P9KNbnvcLUt3JQ0ASOHp6sCnbACTqIMT6JkQonqRv67NjXHPNsDu-VVUcboaAC0IHmJDqO2eYGD2KSKQUJM8ltmKkd6_exmcRG2Fk14f-mcuf1ebY5GSxdUwzTGtoJe2fz0gkN3KDbudHMDM19qe1V3_M0peL36b6Y_BfwcUr2K37dFW1lIAXeLpQEIhkKfgOPSx3eDTIHjJSxxMvq-ikO4NqtQR2GtX9a06sY0fCUbbf5O-VxFhwciYjsseNmhcD8mq_tXOlmWdms2UppXGvxiDjWnA2I-DisnZ-UHKpTUk-zTwjv9BW-CF0Lr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🗣️
هوش مصنوعی‌ها دارن با هم «زبان راز» می‌سازن!
🤫
🤖
‏تا حالا فکر کردی اگه ‌AI⁩ها یه زبانی داشته باشن که ما متوجهش نشیم، چی میشه؟
🤔
‏پروژه جدید
‌GLOSSOPETRAE⁩
دقیقاً همین کار رو انجام میده:
🔹
تولید خودکار زبان‌های مصنوعی (از آواشناسی تا دستور زبان)
‏
🔹
ارتباطات غیرقابل‌فهم برای انسان
‏
🔹
کدنویسی خالص با جاوااسکریپت (بدون وابستگی خارجی)
🚫
📦
‏این فقط یه ابزار نیست؛ یه پنجره به دنیای ارتباطات پنهان ماشین‌هاست.
🔍
🧠
‏
🔗
لینک پروژه:
github.com/elder-plinius/GLOSSOPETRAE
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6747" target="_blank">📅 21:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twA7LMH8tSfkrpJj3wSvn9MZ7Xk4jgjovd-G4FQ4eJHAL2Gqq92YwKgLCCKnN7I70tSqVMwjIFJJ-B_5Q918R42leQMUyKLKRhyGUnJDa_8VEhDwBKxmrNg10gsEFAF0I55SxJfsaq96dU19NTIc9cue4UHNlg1-GxmWoaaMf3ST99fzEs2ZZIPFUQi0PzGIYcFLaDSd50NO3qqCG3nL40PRhwsYMuHuVk8ime1e7VCTySo_81pQBJPBVK0Vvo7s3ZXmE5Ksg4A-mA9M_P2Nmpzh1wSIWnP9_KLDW3tOoglfhumRXvYooNFeD67TAotkFr7cQh3eGsFYGM3aDkygtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🆓
دسترسی رایگان به غول‌های هوش مصنوعی!
🤖
‏‌یه گنجینه از ‌API⁩های رایگان روی ‌GitHub⁩
💎
🔹
مدل‌های قدرتمند: ‌Gemini Flash⁩، ‌Qwen3⁩، ‌DeepSeek⁩ و ‌gpt-oss⁩
‏
🔹
سرویس‌های متنوع: ‌Google AI Studio⁩، ‌OpenRouter⁩، ‌Cloudflare⁩ و ‌GitHub Models⁩
‏
🔹
یکپارچه‌سازی آسان: اتصال راحت به ‌Cursor⁩ برای کدنویسی سریع‌تر
🚀
‏فقط یادت باشه محدودیت تعداد درخواست (‌Rate Limit)⁩ رو رعایت کنی تا سرویس‌ها قطع نشن.
⚠️
⏳
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6746" target="_blank">📅 19:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnZsF-JFiIRpvqHNfawIxLdiL4aTRfcPrfRKFKZC23rBmo6J60zACDioKdPvrie4JgpA27oKdIWGhgjFfD87Z4jOgYydzmErMaEtziNSwW09Q8z0H3OhI7p1AQrLwi0SHkcvZ_JTEapVMFIkxHdZezgKkGS6Vn-_dpTtXGhZ1H_A3ihT1Jn52dt9ppqK4N45EnW7xM__KkQ4lbnDkUtGYUkPwYHDpydeuMwaZZsY2-W6zHMzRZwcujHCFtiwboccw0pgzJu9MEY5b3__RLG2JiAOX1G_D7lbKmoUg_vFUPMJ8AZnMa_Y81IQmKEwGrsyLiq-Yku-8_m65dbmH102Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎨
حذف پس‌زمینه با یک کلیک!
🖱️
‏این ابزار وب پس‌زمینه عکس‌ها رو با دقت بالا جدا می‌کنه و کیفیت اصلی رو حفظ می‌کنه.
✅
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6745" target="_blank">📅 18:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/910f222215.mp4?token=WY25y_QhqWYb3h9_t9q3RwFoSQNVB-Jo1vl90zrEEozJ1RWDrlBYg0FgS8YDMrNywYstxqNpB1sx2qCIcnKKC3bZl7DCezBGGlHo27wEgSv7Zxx1quVkPTNYDaQtn0IXLHzDnVhaYBxoLQDeFWLsreRcU-wribpwD4y2swdQD30_8mqUFiy7yQrcqF9ew-B3JqDA4KUfL0L4UteJPowfPRxfnS2rwq1Heaed0xl01ssRe7oEE-biv1CsCDXK5ZujyECBf2vnR1h0kVof9ETfelUXjst5jwgpuKsA3kBhmBk3wgdG0dHaE1p_lGH6MdB8DwY3h39vwvBQObUj-i-Jsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/910f222215.mp4?token=WY25y_QhqWYb3h9_t9q3RwFoSQNVB-Jo1vl90zrEEozJ1RWDrlBYg0FgS8YDMrNywYstxqNpB1sx2qCIcnKKC3bZl7DCezBGGlHo27wEgSv7Zxx1quVkPTNYDaQtn0IXLHzDnVhaYBxoLQDeFWLsreRcU-wribpwD4y2swdQD30_8mqUFiy7yQrcqF9ew-B3JqDA4KUfL0L4UteJPowfPRxfnS2rwq1Heaed0xl01ssRe7oEE-biv1CsCDXK5ZujyECBf2vnR1h0kVof9ETfelUXjst5jwgpuKsA3kBhmBk3wgdG0dHaE1p_lGH6MdB8DwY3h39vwvBQObUj-i-Jsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧰
کالکشن ۱۷۰ ابزار کاربردی و متن‌باز
تمام این ابزارها تحت وب هستند و نیازی به دانلود فایل یا ساخت اکانت ندارند:
🎬
مدیا: ویرایش حرفه‌ای ویدیو و صدا
🖼
تصویر: فشرده‌سازی، تغییر سایز و افکت
🔄
مبدل‌ها: تغییر سریع فرمت فایل‌ها
📄
اسناد: ادغام، جداسازی و ویرایش PDF
📰
داده: پارسرها و پنل‌های مانیتورینگ
🔗
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/6743" target="_blank">📅 16:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVq-Oyux_xvIZGa_QgT_Dy-cn-sa0ToosYG_LQpoDKXh-MD1jsiyEUuAi3b9tpMIYkIDvZpyKxISrA-m1zVrF50UPk3He8cI94zy1HHdUq9G62fwgQSMQEOYcvYhmDDlttvN882JA0l19oeL76-0y4wnqb3ko651yE80CL87UmqC9mI7T2UtNhSu-qBucDaOCWo4Hp492-xaz8CLDyuR9GihAM-r9N5cvBrTm1Delx4uF1lRiCn_7U8KLgiPG54Q4cVoOrdwvFqJ-BfwS4HLs3ASxBChc0EPWWFzLLlTucDQOK-kME8P_mSsULWPDdlA3XuhPxX0xJuR1JQ89qCdEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
راهکارهای اتصال پایدار و پرسرعت برای اینترنت آزاد
🔹
پشتیبانی از V2RayNG، WireGuard، SlipNet و ArgoVPN
🔹
ارائه اشتراک‌های عادی و گیمینگ متناسب با نیاز کاربران
🔹
انتشار کانفیگ‌های رایگان، آموزش و پشتیبانی
🔹
تست کیفیت اتصال قبل از استفاده
📢
TirexNet؛ همراه شما برای دسترسی بهتر به اینترنت
🤖
Bot:
@TirexNetBot
💬
Support:
@HRMP1386</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6742" target="_blank">📅 15:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏
🚀
دسترسی رایگان به غول‌های هوش مصنوعی!
‏اگر دنبال جایگزینی برای ‌Agent Router⁩ هستید،
سایت ‌
Bluesminds⁩
فوق‌العاده است. با ثبت‌نام، 100 دلار اعتبار اولیه هدیه بگیرید و با مدل‌های قدرتمندی مثل:
🔹
‌GLM 5.2
🔹
‌Qwen 3.6
🔹
‌Minimax M2.7⁩
🔹
‌Mimo 2.5
‏کار کنید. همین حالا امتحانش کنید و پروژه‌هاتون رو به سطح جدیدی ببرید!
✨
🔗
Docs
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/6741" target="_blank">📅 14:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دوستان خوشتون نیاد هر چیزی رو ببرین تو ai ها. حالا ی سری کمپانی ها روشون نظارت هست، سیاست policies دارن. تو اروپا gdpr هست. که اکثر شرکتها تو اروپا ملزم به رعایت کردنش هست. حالا در کل بماند که حریم خصوصی و پرایوسی، لول بندی داره. ی شرکت کل داده های مهمتون…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6740" target="_blank">📅 12:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دوستان خوشتون نیاد هر چیزی رو ببرین تو ai ها. حالا ی سری کمپانی ها روشون نظارت هست، سیاست policies دارن. تو اروپا gdpr هست. که اکثر شرکتها تو اروپا ملزم به رعایت کردنش هست. حالا در کل بماند که حریم خصوصی و پرایوسی، لول بندی داره. ی شرکت کل داده های مهمتون فضولی میکنه. یکی میفروشه به دلال های داده (مثه گوگل و مایکروسافت و...) یسریا هم که حریم خصوصی محورن.
الان هرمس اینا رو واقعا نمیدونم. هر چی بیشتر این مدلا رو بیشتر وارد چیزاتون میکنین، ریسکش بالاتر میره در کل. باز این شرکتا اروپایی نظارت بالاتر هست ولی نمیدونم طرف خوشش میاد از ی مدل میگه به به چ مدلی چقد قابلیت بذارم چنل، ملت کلی ویو میزنن استفاده میکنن. طرف به تلگرامش و... هم وصل میکنه بعد اخر بعد چند روز میگه ببخشید هرمس رو شخصی ران نزنید
اینو میخواستم چند روز پیش بذارم ولی گفتم ولش. ولی حس کردم بهتره بگم تا پیشگیری بشه بهرحال</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6739" target="_blank">📅 12:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gw_K1CVtjdPWSlT3ZRHRGAh0ClJ7twv0KENnM0gYG7SxrT3FTSdqSOxWOJiCQxJROwuIulvq25_8T_fCb135MP3lm5YRZHksG8RnvvDnuMKZVsHpaWFEbRlj_dJ8sbikXSZG7R_WMfm93_yypSkK4uA-AVJdG6ld5pMfjLs688OEYLnirUo8pUDl9u4eLGZZssA3uJDo5CjVjI5fbScz93TgjAEFuOeQ_BDTjddvHvu9UIlzMYv_AwsRvxIJGmgH_Nf1JDwhJ1tAeCwW_rYDQB3SKRXW_cSWSy40hsDLkRB3WPiNJ3giol5gp9JOc2skGLMOAJJsti94Zg-tRvHiHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/ArchiveTell/status/2074039784629014892?s=20</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6738" target="_blank">📅 11:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGnA1h6bMt1S67XCQINiOtj2pYjZmf6Mbx7I9Ja1mWl_Ghy-SO_8D1PZpVtPw23Epki3QKXsrKeYyeYXlaItc587xaKEQTO1eogbEnRYqQS2Cxdf8p8KjopwMMDYzuz8i80H7UIfeUAu9rAZbTQegkk3FCOH-QbQW-2WbeoZlbFcZfbjub4JrgfzY7iezDdw6Uka2AstRUAXiwfkkd_z11QREetlDYKi43sIUrORUUVfDChHJIv0AtfZ0dONgroHpt4Ycs94ELjgjtLqXR7ZXcNpnjVl7OkS0t7eq-6gt6nYQ3s6uZeOOhZJ_G-E9Fg1k0JqsRPazBBS22yJBvAdaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
اجرای هر بازی اندرویدی مستقیماً روی کامپیوتر
یک شبیه‌ساز رسمی از گوگل که واقعاً سریع است و به راحتی از رقبا پیشی می‌گیرد.
🔹
پشتیبانی کامل از اندروید 14، از همان ابتدا.
🔹
عملکرد از طریق Hyper-V — همه چیز پایدار و سریع است.
🔹
هر فایل APK را بدون هیچ مشکلی اجرا می‌کند.
🔹
بدون هیچ بنری یا تبلیغ مزاحم.
🔹
بازی‌ها بدون هیچ‌گونه کندی یا تأخیر اجرا می‌شوند.
دستورالعمل به زبان فارسی
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/ArchiveTell/6737" target="_blank">📅 10:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtlCaGYBKPTGFLNioOs7iJEMq715NxMYjaUAdxuF2oiIOMa1geaC0n-nogaEDHieWOsK7QH8ghCt2ayE14TuIWvI1d6wdrkHyOKFlX9XghpMdjK9i80Z8JCzQFexbng2HgDs3iwYPE_mqIkxXhG1tNnpb24FYq2y2iSk9YSHKHUALpf9wDeO_d-FO4rE2vgipXotMdJsgGBg2fHBDQ5Ah8XpPwraIxXJOS7J2OShWoS8hCoqSWU8DnkkMalBn8CkzlMDkMm_yGWeRCHgiWpQociGxg9IG3ZH6dQbEFadjPI2hlLXQjxpL4NZKrwtfghu_vk3iyiQUhTb80nPjHk-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
کپ‌کات رو فراموش کنید؛ این ابزار رایگان و بدون نیاز به نصب جادو می‌کند!
‏اگر برای ادیت ویدیوهای خود به دنبال یک ابزار سبک، همه‌فن‌حریف و کاملاً رایگان هستید، پروژه متن‌باز ‌OpenReel⁩ دقیقاً همان چیزی است که نیاز دارید. این ادیتور قدرتمند مستقیماً درون مرورگر شما اجرا می‌شود و نیازی به نصب هیچ برنامه‌ای ندارد.
‏
💡
چرا ‌OpenReel⁩ یک جایگزین بی‌نظیر است؟
‏
🔹
ادیت چند لایه حرفه‌ای: قابلیت ویرایش همزمان چندین لایه ویدیو و صدا همراه با پیش‌نمایش زنده و بدون افت سرعت.
‏
🔹
امکانات کامل کپ‌کات: دسترسی به افکت‌های متنوع، ترنزیشن‌ها، پرده سبز (‌Chroma Key)⁩، کنترل سرعت و فریم‌های کلیدی (‌Keyframes)⁩.
‏
🔹
ابزارهای جانبی کاربردی: قابلیت ضبط صفحه نمایش، کار با متن و زیرنویس، و خروجی گرفتن سریع با فرمت‌های ‌MP4⁩ و ‌WebM⁩.
‏
🔹
کاملاً رایگان و امن: بدون نیاز به ثبت‌نام‌های پیچیده، پرداخت درون‌برنامه‌ای یا واترمارک روی ویدیوها.
‏بدون درگیر کردن حافظه سیستم یا گوشی، همین حالا ادیت ویدیوهای خود را در سطح حرفه‌ای شروع کنید!
🔗
Site
|
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/6736" target="_blank">📅 10:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6735">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg80ghBJdUs6Vr6M2WblxZKJ2wKtalauK3w7bZkjzIzFcY3zXLafYDeJ7Bj9uQpNqu42fr04THpIwP7QcTVgQ9yUEmmKSYgtP-wwBIKNZQrlvoRRDLwlEsbmnuPUEnn-aJpxnssddI-u8t8JkDz_z-p126maag5vKuBFz7ijhzyrRbU6ZHJkh3qYeNn7v9pBUiImSepfSsOqKB0eyWxdCEfyB-h6-OKxCKC8svKkggMFHhZ9tvh1_TtPe4Og8u566lttN4nGY5gwbQdSM9fBOtNbh4CLEWFwdncZMQz9aYauCsiZLK3wtIKMzy_tThIOKIgh4TDMxTqCgYcMIuCS9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
تمام غول‌های هوش مصنوعی دنیا، زیر یک سقف!
‏دیگه نیازی نیست برای تولید متن، کد، ویدیو یا عکس، بین ده تا سایت مختلف چرخ بزنی و کلی اکانت پولی بخری. این پلتفرم همه‌چیز رو برات یک‌جا جمع کرده!
‏
✨
چرا این ابزار بازی رو عوض می‌کنه؟
🔹
تیم رویایی در یک پنجره:
به راحتی و با یک کلیک بین قوی‌ترین مدل‌های دنیا یعنی ‌ChatGPT⁩، ‌Claude⁩، ‌Gemini⁩، ‌Grok⁩ و ‌Kimi⁩ جابجا شو.
‏
🔹
تولید همه‌جانبه:
از نوشتن کدهای پیچیده و متن‌های خلاقانه تا خلق تصاویر و ویدیوهای جذاب، همه در یک محیط واحد.
‏
🔹
سهمیه رایگان روزانه:
هر روز کلی توکن رایگان بگیر و پروژه‌هات رو جلو ببر.
https://www.easemate.ai/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/6735" target="_blank">📅 10:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6734">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2FDb5MxGNGrU08l-zVmaxik8iSSm7i0D0LPPYzxUj0TDGExV6KL1bPPU2Jr1rJ_VpGB0s9T5KLirjiUCDOSJSnmTrvAKnsJaQSRZIT_PIZyKLIb8mnGjn8hiG7w3wr2NF_e_vaHVnwL9e4-R6_yllcbbG2pfD2b3iMGO2UnLOPDkM4fHpJOCA9GPD6vOraFnyn8SHJKjpo_wVwyfCn--hcavrMPweSNvdSo8dES2jRBTJU2Qq1cZzVakpoIANYhloU5kpoyX7mqmMJ2biKBhsngJuGqO8v1zq1RdHcyFQmVk-xy1-rj1etI1S0zQM3CaLnZE4qtJp-totz4KdBhWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
غول هوش مصنوعی، بالاخره رایگان و بی‌دردسر!
‏دیگه نیازی به خرید اکانت پرمیوم یا دردسرهای ست کردن ‌API⁩ نیست؛ از امروز می‌تونید به صورت کاملاً رایگان توی پلتفرم ‌Tabbit⁩ با شاهکار جدید ‌Anthropic⁩ یعنی Claude Sonnet 5 گفتگو کنید!
💻
✨
‏
💡
چرا این خبر بمبه؟
سونت ۵ در حال حاضر یکی از باهوش‌ترین و دقیق‌ترین مدل‌های دنیاست که حالا بدون هیچ محدودیتی در دسترستون قرار گرفته. فقط کافیه وارد سایت بشید و چت رو شروع کنید
https://tabbit.ai
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/6734" target="_blank">📅 09:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🗂
هیچ‌چیز رو دور ننداز! معرفی Karakeep؛ بهشتِ آرشیوکارها و خوره‌های اطلاعات
🧠
اگر شما هم از اون دسته‌اید که روزانه ده‌ها لینک، مقاله و ویدیو رو برای «بعداً خوندن» ذخیره می‌کنید و در نهایت بینشون گم می‌شید،
Karakeep
(با نام قبلی Hoarder) دقیقاً برای شما ساخته شده. این ابزار یک جایگزین فوق‌العاده، سلف‌هاست و متن‌باز برای برنامه‌هایی مثل Pocket هست که با جادوی هوش مصنوعی ترکیب شده!
🔥
چرا Karakeep بی‌نظیره؟
🤖
تگ‌گذاری خودکار با AI:
با استفاده از LLMها (حتی مدل‌های لوکال مثل Ollama)، محتوای شما رو بررسی کرده و به صورت خودکار تگ‌گذاری و خلاصه‌نویسی می‌کنه.
🗄
آرشیو ابدی صفحات و ویدیوها:
برای جلوگیری از حذف شدن لینک‌ها (Link rot)، کل صفحه وب رو به صورت آفلاین ذخیره می‌کنه و حتی ویدیوها رو به کمک yt-dlp دانلود و آرشیو می‌کنه!
🔎
جستجوی قدرتمند و OCR:
متن داخل عکس‌ها رو استخراج می‌کنه و می‌تونید در کل محتوای ذخیره‌شده (فول‌تکست) جستجو کنید.
📱
همه‌جا در دسترس:
دارای افزونه برای کروم، فایرفاکس و سافاری، به همراه اپلیکیشن اختصاصی برای iOS و اندروید.
🔌
تعامل با ایجنت‌ها:
کاملاً سازگار با ایجنت‌های هوش مصنوعی (مثل OpenClaw) برای مدیریت خودکار اطلاعات از طریق CLI.
اسم این برنامه از کلمه عربی «کراکيب» (Karakeeb) الهام گرفته شده؛ به معنی خرت‌و‌پرت‌هایی که شلوغ به نظر می‌رسن اما پر از ارزش و خاطره‌ان و نمیشه دور ریختشون!
🔗
لینک مخزن گیت‌هاب پروژه:
https://github.com/karakeep-app/karakeep
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝑒𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6733" target="_blank">📅 08:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یه پروژه مدیریت vps توسط ai زدم شب میفرستم.  اینطوریه که ازت آی‌پی و پس رو میگیره  بعدش تو دستور میدی. میگی مثلا ثنایی رو بالا بیار، تونل فلان نصب کن، رباتمو بالا بیار و ... خودش قشنگ انجام میده آخرش ازت تشکرم میکنه‌  دیگه نیاز نیست دستور های ترمینال رو بدونی…</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/ArchiveTell/6732" target="_blank">📅 04:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚀
آموزش نصب OpenCode و استفاده رایگان از مدل های هوش مصنوعی زیر :
🔸
Mimo 2.5
🔸
Deepseek 4 flash
🔸
Nemotron 3 Ultra
🔸
Big Pickle
🔸
North Mini Code
🔘
آموزش نصب در موبایل
1️⃣
نصب Termux
اگر روی موبایل هستی
اول Termux را نصب کن
📱
2️⃣
دستورات داخل Termux
1) آپدیت Termux
pkg update -y && pkg upgrade -y
2) نصب ابزارهای لازم
pkg install -y proot-distro nano
3) نصب Ubuntu
proot-distro install ubuntu
4) ورود به Ubuntu
proot-distro login ubuntu --user root
3️⃣
دستورات داخل Ubuntu
1) آپدیت Ubuntu
apt update && apt upgrade -y
2) نصب پیش‌نیازها
apt install -y curl bash ca-certificates wget git nano gnupg lsb-release software-properties-common build-essential python3 make g++
3) نصب OpenCode
npm i -g opencode-ai
4) اجرای OpenCode
در یک پوشه اجرا کنید
مثال :
cd /storage/emulated/0/Download
سپس‌ :
opencode
4️⃣
اگر خواستی بعداً دوباره وارد Ubuntu شوی
proot-distro login ubuntu
5️⃣
اگر OpenCode را نصب کرده‌ای و فقط می‌خواهی اجراش کنی ، قبلش وارد پوشت شو
opencode
🔘
داکیومنت رسمی برای نصب در جاهای دیگر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/6731" target="_blank">📅 02:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎬
تدوینگر اختصاصی شما داخل ترمینال! معرفی ابزار فوق‌العاده Video-Use
🚀
دوست دارید فقط با چت کردن با عامل‌های هوش مصنوعی (مثل Claude Code یا Codex) ویدیوهاتون رو ادیت کنید؟ پروژه اوپن‌سورس
video-use
دقیقاً همین کار رو می‌کنه. فقط کافیه ویدیوهای خام رو بریزید داخل یک پوشه و با زبان طبیعی بهش بگید چی می‌خواید تا یک فایل نهایی (
final.mp4
) ترتمیز بهتون تحویل بده
.
🔥
چرا این ابزار انقلابی و متفاوته؟
🧠
پردازش هوشمند و ارزان:
به جای اینکه کل ویدیو رو به خورد LLM بده (که به شدت گرون و پرخطاست)، فقط یک فایل متنی سبک از ترانسکریپت با تایم‌استمپ دقیق کلمات و در صورت نیاز اسکرین‌شات‌هایی از تایم‌لاین (شامل فرم تصویر و موج صدا) رو بررسی می‌کنه.
✂️
حذف اتوماتیک اضافات:
تپق‌ها، مکث‌های طولانی و کلمات اضافه رو به صورت خودکار تشخیص میده و هوشمندانه کات می‌زنه.
🎵
تدوین بی‌نقص:
روی تمام کات‌ها ۳۰ میلی‌ثانیه فید (Fade) صوتی میندازه تا هیچ‌وقت صدای پرش کات رو نشنوید.
🎨
زیرنویس و انیمیشن:
می‌تونه زیرنویس‌های کاستوم (مثلاً کلمات دوتایی بزرگ) روی ویدیو بندازه و با ابزارهایی مثل Manim ،Remotion و HyperFrames انیمیشن تولید کنه.
🤖
حلقه خودارزیابی (Self-Eval):
قبل از اینکه خروجی رو به شما نشون بده، خودش ویدیو رو بازبینی می‌کنه تا پرش‌های تصویری یا مشکلات صوتی رو پیدا و برطرف کنه.
این ابزار مثل این می‌مونه که یک کارگردان و یک تدوینگر رو همزمان داخل محیط کدنویسی خودتون داشته باشید که حتی پروژه‌ها رو ذخیره می‌کنه تا روزهای بعد بتونید ادیت رو ادامه بدید!
🔗
لینک گیت‌هاب پروژه برای نصب و راه‌اندازی
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6730" target="_blank">📅 01:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thefeed-android-v0.30.8-universal.apk</div>
  <div class="tg-doc-extra">25 MB</div>
</div>
<a href="https://t.me/ArchiveTell/6729" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
نسخه جدید
#TheFeed
(v.0.30.8)
🔹
بهبود مدیریت لینک ها در برنامه، اگر توی یک پست ای دی یک کانال دیگه و یا لینک یک پست از یک کانال دیگه باشه، وقتی روش بزنید میتونید به اون کانال و پست منتقل بشید، توی قسمت فید باید اون کانال حتما توی اون کانفیگ وجود داشته باشه، توی قسمت میرور خودکار اون کانال به لیستتون اضافه میشه.
📯
من نسخه اندروید
universal
که مناسب همه‌ی گوشی های اندروید هست رو توی این کانال میزارم. ولی اگر نسخه‌های دیگه رو میخواید باید از گیتهاب و یا کانال زیر دانلود کنید (
ویندوز
،
مک
،
لینوکس
،
بی‌اس‌دی
، اندروید‌های
قدیم
و
جدید
،
ترموکس
، و حتی
نسخه ipa
آیفون) و لینک دانلود نسخه آیفون از تست‌فلایت توی کانال پین شده، البته هنوز آپدیت نشده.
📢
کانال اصلی دفید:
@networkti
📦
کانال فایل‌های باینری/نصبی دفید:
@thefeedfile
⚙
کانال کانفیگ‌های دفید:
@thefeedconfig
🔗
گیتهاب پروژه:
https://github.com/sartoopjj/thefeed</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/6729" target="_blank">📅 00:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚀
معرفی CdnScanner؛ جامع‌ترین و قدرتمندترین اسکنر IP و CDN
🚀
✨
ویژگی‌های برجسته:
* پشتیبانی کامل از ۱۷ سرویس‌دهنده (CDN): شامل Cloudflare (و WARP/Workers)، AWS CloudFront، Google Cloud، Azure، ArvanCloud، Fastly، Vercel، Akamai، Gcore و...
💪
تست فوق‌دقیق بر اساس کانفیگ شما: در این ابزار IPها فقط زمانی تأیید می‌شوند که با کانفیگ V2Ray واقعی شما (شامل SNI، Host و Path) پاسخگو باشند (پشتیبانی از TCP connect + TLS Handshake + HTTP HEAD).
🫆 اسکنر اختصاصی HTTP: امکان وارد کردن مستقیم IP، دامنه یا رنج CIDR (مانند
1.1.1.0/24
) با قابلیت بازگشایی و اسکن خودکار کل رنج.
* تولید خودکار خروجی V2Ray: ساخت بی‌درنگ لینک‌های VLESS ،VMess و Trojan از IPهای سالم با قابلیت کپی و دانلود یک‌کلیکه!
* پینگ واقعی (ICMP): عملکرد دقیق روی Windows ،Linux و macOS (همراه با سیستم جایگزین TCP در صورت مسدود بودن پینگ).
* اسکن کامل و بدون نقص: بررسی جزء‌به‌جزء تمامی IPهای یک رنج مشخص، به جای اکتفا به نمونه‌های تصادفی.
* رابط کاربری مدرن و فارسی (RTL): داشبورد حرفه‌ای و چشم‌نواز همراه با نوار پیشرفت (Progress bar)، کارت‌های آماری، پیام‌های Toast و طراحی کاملاً راست‌چین.
📥
دریافت و نصب:
همین الان می‌توانید این ابزار قدرتمند و متن‌باز را از گیت‌هاب دریافت کنید. (اگر ابزار برایتان کاربردی بود، دادن ستاره
⭐️
به پروژه در گیت‌هاب فراموش نشود!)
🔗
لینک پروژه در گیت‌هاب:
https://github.com/ScannerVpn/CdnScanner
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6728" target="_blank">📅 21:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/6727" target="_blank">📅 19:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یه پروژه مدیریت vps توسط ai زدم شب میفرستم.
اینطوریه که ازت آی‌پی و پس رو میگیره
بعدش تو دستور میدی. میگی مثلا ثنایی رو بالا بیار، تونل فلان نصب کن، رباتمو بالا بیار و ...
خودش قشنگ انجام میده آخرش ازت تشکرم میکنه‌
دیگه نیاز نیست دستور های ترمینال رو بدونی یا حفظ کنی. تو فق به زبان فارسی بش میگی انجام میده</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/6726" target="_blank">📅 18:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">https://x.com/ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6723" target="_blank">📅 13:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دیده‌بان لیکفا منتشر شد
🆕
افزونه‌ای برای مرورگر کروم که هنگام بازدید از وب‌سایت‌ها، اگر آن سایت سابقه نشت اطلاعات داشته باشد، به‌صورت خودکار به شما هشدار می‌دهد. متن‌باز، رایگان، کاملا محلی و بدون ارسال اطلاعات به سرور
👍
Download
🛫
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/6722" target="_blank">📅 13:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqb-74CSBWTL3gNzssWCNt-jzuSyW8KGpL63gfkAX44iL1apgqELzSFCtd2JBt84cBiUFEhOa3Up0aRBZl3hJOqi463WYUZOQq3LD7zyc2yIXm_eDV8rbBDA3TZzj6ngUTLHQl3_yETNJJrVWawTdgQXdf4goFktYasprHW9KLjkVQElhLxhDUdUvZPuY2unVNtM9Crl8c_7A3xwqHnCafcsZg5R_ls_Gp-1h8osPV9RrNuHrlenrKNj4n9_dDw1JmkgkuIN-kyA6k4p1RxfEximCt1R8UIG5Jkr02lnYZZ0UTzXFV2dmwYcXgsn2tIhLwW6jOpWTPQ2P2Pdmz_EHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💻
سیستم‌عامل شخصی، مستقیم توی مرورگر!
‏یک پلتفرم متن‌باز و سبک که می‌تونی روی سیستم خودت بالا بیاریش (‌Self-host)⁩ و همه‌چیز رو کاملاً آفلاین و امن مدیریت کنی.
‏
✨
چرا جذابه؟
🔒
امنیت مطلق:
داده‌ها فقط روی هارد خودت ذخیره میشن.
‏
🛠
ابزارهای کاربردی:
ویرایشگر متن، ضبط صدا و پلیر داخلی در یک تب.
‏
🚀
فوق‌العاده سبک:
بدون نیاز به سخت‌افزار قوی، فقط با یک کلیک.
‏
⚡️
راه‌اندازی:
دریافت سورس از گیت‌هاب و اجرا با داکر.
🔗
لینک گیت‌هاب پروژه
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/6721" target="_blank">📅 12:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🐦‍🔥
اسکنر قدرتمند سیمرغ (SIMORGH Scanner v0.3.0) منتشر شد!
🚀
اگر برای کانفیگ‌های VLESS خودتون دنبال پیدا کردن IP تمیز کلودفلر هستید، اسکنر سیمرغ یکی از بهترین ابزارهاست. به تازگی نسخه 0.3.0 اون با یه رابط کاربری وب بسیار جذاب (نئونی-رترو) منتشر شده.
🔥
ویژگی‌های خفن این نسخه:
💻
پشتیبانی از ویندوز و اندروید:
نسخه ویندوز به صورت Standalone هست و بدون نیاز به اینترنت اولیه یا نصب پایتون، به راحتی با یک کلیک اجرا میشه. نسخه اندروید (APK) هم با بک‌اند بومی Go نوشته شده و کاملاً برای صفحه نمایش موبایل بهینه‌سازی شده.
🎯
تست همه‌جانبه:
می‌تونید تک IP، رنج‌های CIDR و لیست‌های ISP رو اسکن کنید. این ابزار دارای دسته‌بندی لیست‌های آماده ISP ایران و بین‌الملل هست و حتی می‌تونید لیست اختصاصی خودتون رو به صورت فایل txt وارد کنید.
⚡️
امکانات دقیق اسکن:
دارای قابلیت‌های نمایش پینگ (Latency)، بررسی مجدد (Re-check) و تست سرعت (Speed test) به صورت مجزا هست.
📁
خروجی حرفه‌ای:
در نهایت آی‌پی‌ها و کانفیگ‌های تمیز رو رتبه‌بندی می‌کنه و خروجی‌های مرتبی مثل best_configs.txt و clean_ips.txt بهتون تحویل میده.
🔗
لینک گیت‌هاب پروژه برای دانلود نسخه‌ها
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6720" target="_blank">📅 11:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb0268ad1.mp4?token=dxhcGIkld5TrkiqRvP7CQ7TxujiMJNoGO1mSJfhpPKwVB3YBNMWUtr9DKb-OtYziaRlreRbQbPTAKIyfCY7xv4XgyeoooJ2XwQosx5sCqv-MF38pwK_Gd79fkCK1w0GuiAcq4OXVNje79Jzu0Vn7QWGnp39Tln-acqc9r2aArsZ9wDdl6moe_BqVRZp_dw7NPGGGn78iMFsN0lGujNyFGHxlLilvjaVOSbGwrYcueunuXQGb3riBHr6l4QpxufiwaU8RGZeE-xG8gLd5LmWv4kkO-LOf3NaNJ9576fqxlowjzxLyjleHBroEX6KBMlwYXy-FtkctCdQ5cjXYW_IhbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb0268ad1.mp4?token=dxhcGIkld5TrkiqRvP7CQ7TxujiMJNoGO1mSJfhpPKwVB3YBNMWUtr9DKb-OtYziaRlreRbQbPTAKIyfCY7xv4XgyeoooJ2XwQosx5sCqv-MF38pwK_Gd79fkCK1w0GuiAcq4OXVNje79Jzu0Vn7QWGnp39Tln-acqc9r2aArsZ9wDdl6moe_BqVRZp_dw7NPGGGn78iMFsN0lGujNyFGHxlLilvjaVOSbGwrYcueunuXQGb3riBHr6l4QpxufiwaU8RGZeE-xG8gLd5LmWv4kkO-LOf3NaNJ9576fqxlowjzxLyjleHBroEX6KBMlwYXy-FtkctCdQ5cjXYW_IhbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
‌GitFut⁩:
رتبه‌بندی پروفایل ‌GitHub⁩ مثل بازیکنان فیفا!
⚡
‏هر توسعه‌دهنده‌ای تو دنیای کد یه ستاره‌ست!
🌟
‏این ابزار
رتبه ۰ تا ۹۹
رو بر اساس:
‏
🔹
تعداد
‌commit⁩ها
‏
🔹
ستاره‌های ریپو
‏
🔹
دنبال‌کنندگان
‏
🔹
زبان‌های برنامه‌نویسی
‏بهت میده!
‏
ببین به کدوم بازیکن فوتبال شباهت داری!
⚽
💻
‏
👉
امتحان کن
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6719" target="_blank">📅 10:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnjjEOE_ohR1CBOdBpZ26YIyBSqryZMnQPWIHh5EQoxSO4AyivzAxbD98HaKdaOBlD77mDzCXAOHY9ZtEDLWNiJF6CUNzrZbCOfL3STy_kurmvK35p8F62x3mFF1EV8XZqbulQoY5KE0Nr-X4PVAM2sVTheeLu1PIQdlNIsNdsY37bf56TXNw6OIOjW_P5VerZ1LzeLTcjf0sVTkcJZ9XvfH888YdthQlVrgVDHOCoeup8YwIB4O5QYfm8lfKNmw8BY9QZsH3XdMxdzAqUx9khnUDjgybpo2v22HrLDA8-ALc0sAbhvgBiKYuE4q3fVID7eHhNdPDHsjUUYDEYFLEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
‌scrcpy⁩
— کنترل کامل گوشی اندرویدی روی کامپیوتر!
📱
➡️
💻
‏
✅
بدون دردسر
: نیازی به روت یا نصب اپ روی گوشی نیست! فقط با ‌USB⁩ یا وایفای وصلش کن.
‏
⚡
سرعت بالا
: ۱۰۸۰‌p⁩+ با ۳۰ تا ۱۲۰ فریم بر ثانیه.
‏
🔊
صدا
: انتقال مستقیم صدا (اندروید ۱۱+).
‏
⌨️
کنترل کامل
: موس و کیبورد فیزیکی شبیه‌سازی میشه.
‏
🎥
ضبط صفحه
+ نمایشگر مجازی.
‏
🐧
سازگار
: ویندوز، مک، لینوکس (بدون نیاز به ‌snap)⁩.
‏
🔗
مخزن
:
‌GitHub⁩
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/6717" target="_blank">📅 10:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏
🚀
‌Arvix AI⁩ = جعبه‌ابزار کامل هوش مصنوعی تو
‏
🧠
متن:
‌GPT⁩, ‌Claude⁩, ‌Gemini⁩, ‌Grok⁩
‏
🎨
تصویر:
‌Midjourney⁩, ‌FLUX⁩, ‌Nano Banana⁩
‏
🎬
ویدیو:
‌Kling⁩, ‌Veo⁩, ‌Seedance 2⁩
‏
🎧
صدا:
‌Suno⁩, ‌ElevenLabs⁩
‏
🎁
توکن رایگان + دسترسی به همه مدل‌ها
https://arvixai.net/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/6716" target="_blank">📅 10:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏
🚀
آموزش دریافت ‌API⁩ رایگان ‌Nvidia⁩
🚀
‏‌
1⃣
ثبت‌نام اولیه:
‏وارد سایت
‌build.nvidia.com⁩
شو و یک حساب کاربری بساز
📧
2⃣
‏‌
شروع تایید هویت:
‏پس از ثبت‌نام، روی کادر زرد رنگ بالای صفحه کلیک کن تا پروسه وریفای آغاز شود.
⚠️
3⃣
‏‌
دریافت شماره مجازی:
‏به سایت
‌2nd-no.com⁩
برو و یک شماره مجازی موقت و رایگان دریافت کن.
📱
4⃣
‏‌
فعال‌سازی حساب:
‏شماره دریافتی را در سایت انویدیا وارد کرده و کد تایید را ثبت کن.
✅
5⃣
‏‌
ساخت کلید دسترسی:
‏به بخش ‌
API keys
⁩
برو و کلید اختصاصی خودت را بساز.
🔑
6⃣
‏‌
انتخاب مدل‌های رایگان:
‏به بخش
‌
Model⁩
برو و از گزینه‌های
‌Free Endpoint⁩
استفاده کن.
🤖
‏
🌟
برخی از بهترین مدل‌های در دسترس:
🔹
‌GLM 5.2⁩
🔹
‌Minimax M3⁩
🔹
‌Deepseek v4 pro⁩
🔹
‌Kimi k2.6⁩
🔹
‌Qwen 3.5⁩
‏
بدون محدودیت توکن
🔓
بدون لیمیت روزانه
‏
♾
40
درخواست در دقیقه
‏
⏱
🔵
@ArhiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6715" target="_blank">📅 03:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318f76cfea.mp4?token=AiLL5OVC2FLDmxVKkQb7IUp633dLelXxsv0OwsDS4j-XTIb6fenwlAJHQSqfteNLW8QriPw7a0-wySm5-mKT4JZjWTb5MoYAlI8va9r4snmygXPkzbI-dPfkEs4U0YfZQ2PD0_ZUPaJUUhenY-azIgVCPXHpBQh7AvLijdwFkro0vzA80tdTaWVq2cS0LpQQ0zdXl4nFdGb-iESc6dQohzEEUHrSyXV_hbVVrZMVJKS49ccg2mKyTUaqLLccBv0IsV1aSPEhJzlDBT-FuivQt_ZvmMgtN3BCtCLqhu18qGKLFChoGpcWINXRnWucBBS6VHYKpxBhE1Kf20olYwQ_JF0yW2wj9q0_4LG2bOn0IeUBZVGyBy7ughNh9b5Ll1I_0MJV22pEl_qWD-61lZckBxnAstAu168Xh45mYX0lyeZCJlh72R4x0b5wy49-jkcC-v7sQZBDcY7d7UWb3ArToyDUrM-3Vj1GtweJQfcZyLO3c8wnK9BsFHQUjMaTX8417vouYM54K1wvGA15k-7yxV2dtJMitEuwcKEPwaNnexT2mtktyYYYFx-foPqdUY9cYbNs6wCeDlV7GPunzBPh0QBZwvnVK3hR1frr2S1xEipv8-7PSsol_mLAcz5EuZPpHH0lEFlO-kypVKkMdY5aFohYzxdELM08-ABJ7snaLxU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318f76cfea.mp4?token=AiLL5OVC2FLDmxVKkQb7IUp633dLelXxsv0OwsDS4j-XTIb6fenwlAJHQSqfteNLW8QriPw7a0-wySm5-mKT4JZjWTb5MoYAlI8va9r4snmygXPkzbI-dPfkEs4U0YfZQ2PD0_ZUPaJUUhenY-azIgVCPXHpBQh7AvLijdwFkro0vzA80tdTaWVq2cS0LpQQ0zdXl4nFdGb-iESc6dQohzEEUHrSyXV_hbVVrZMVJKS49ccg2mKyTUaqLLccBv0IsV1aSPEhJzlDBT-FuivQt_ZvmMgtN3BCtCLqhu18qGKLFChoGpcWINXRnWucBBS6VHYKpxBhE1Kf20olYwQ_JF0yW2wj9q0_4LG2bOn0IeUBZVGyBy7ughNh9b5Ll1I_0MJV22pEl_qWD-61lZckBxnAstAu168Xh45mYX0lyeZCJlh72R4x0b5wy49-jkcC-v7sQZBDcY7d7UWb3ArToyDUrM-3Vj1GtweJQfcZyLO3c8wnK9BsFHQUjMaTX8417vouYM54K1wvGA15k-7yxV2dtJMitEuwcKEPwaNnexT2mtktyYYYFx-foPqdUY9cYbNs6wCeDlV7GPunzBPh0QBZwvnVK3hR1frr2S1xEipv8-7PSsol_mLAcz5EuZPpHH0lEFlO-kypVKkMdY5aFohYzxdELM08-ABJ7snaLxU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تبدیل ویس به متن تلگرام کاملاً رایگان! (بدون نیاز به پریمیوم) با هوش مصنوعی Cloudflare
https://youtu.be/Xq7e2k3qlqA</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6714" target="_blank">📅 02:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دوستان وقت بخیر و خسته نباشید
این چنل زاپاس آرشیوتل هستش
داشته باشین بهتره
❤️‍🔥
ی موقع اگ چیزی شد...
https://t.me/FOSSArchive</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6713" target="_blank">📅 22:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0691365cb.mp4?token=tfS4n796inm8BPhFLXJXgWK5FxP4Wk30vol-BEuMkgNsSWWRpm88LErrCWE9w0Lr2j3p9TiJ7d0wj8OGNhMpzeew93_oASkvgkVQ7Bx87zSuevQToa3mVv-XKux91XkYM3PotJ0D-Pb8oyx4STfd5FosWg8DknQAaFQSW0SHKSKA0sf3eTumKOwp_uo6kiK8IAkN034CEyBwPuBaHhd_7OEPCQkOEXolcR-AhwTjuPSbM914lmRQ-e9hYX_NRYDfgegO2-Uh4Fegc-m3S2tu6QgDXKshc2FOJdMB65_WfQYAsDM00kH7tF8kx15t_qGNsL4xa8r-KQGTcFGD1DRCBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0691365cb.mp4?token=tfS4n796inm8BPhFLXJXgWK5FxP4Wk30vol-BEuMkgNsSWWRpm88LErrCWE9w0Lr2j3p9TiJ7d0wj8OGNhMpzeew93_oASkvgkVQ7Bx87zSuevQToa3mVv-XKux91XkYM3PotJ0D-Pb8oyx4STfd5FosWg8DknQAaFQSW0SHKSKA0sf3eTumKOwp_uo6kiK8IAkN034CEyBwPuBaHhd_7OEPCQkOEXolcR-AhwTjuPSbM914lmRQ-e9hYX_NRYDfgegO2-Uh4Fegc-m3S2tu6QgDXKshc2FOJdMB65_WfQYAsDM00kH7tF8kx15t_qGNsL4xa8r-KQGTcFGD1DRCBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
ImageGlass
ابزار سبک و سریع برای مشاهده عکس ها در ویندوز با پشتیبانی از طیف گسترده ای از فرمت های فایل.
• پشتیبانی از بیش از 90 فرمت: WEBP, GIF, SVG, AVIF, JXL, HEIC
• رابط کاربری بصری با سرعت پردازش بالا
• مناسب برای کاربران عادی و طراحان
https://github.com/d2phap/ImageGlass
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/6712" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423195fff7.mp4?token=eBIiEUscBBNKl_DrjRnhxx4Ay3GyAjtIPVbVcymaRcZpZPzwFgwI7hZh1vi95uGJ10oHF3Sby17iWnEaUqv5yHdGUgrL1nLe4UCwPq89gf_dg2aBFq_3jnyKwPu1X1e4IrNG7XFGf0EEJmfycCChF-El1DWVykvO4YsmxDoyKnOl7JFmbrBH8ckwNpUQLRzfWy-fsYnCyY-iAuzaHo8rp0d_gWkSS3KIdk_iL_fT8BqHThpmuMOY6OE3wFmalfMTPwroI2XITh2AzNolk7rs1Nf2vIllWtsKNGNeJQK79ncT7s4RtJqNLPEcQVm_xPt7ZBCIdJ1FqJIYk5Glli7Wrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423195fff7.mp4?token=eBIiEUscBBNKl_DrjRnhxx4Ay3GyAjtIPVbVcymaRcZpZPzwFgwI7hZh1vi95uGJ10oHF3Sby17iWnEaUqv5yHdGUgrL1nLe4UCwPq89gf_dg2aBFq_3jnyKwPu1X1e4IrNG7XFGf0EEJmfycCChF-El1DWVykvO4YsmxDoyKnOl7JFmbrBH8ckwNpUQLRzfWy-fsYnCyY-iAuzaHo8rp0d_gWkSS3KIdk_iL_fT8BqHThpmuMOY6OE3wFmalfMTPwroI2XITh2AzNolk7rs1Nf2vIllWtsKNGNeJQK79ncT7s4RtJqNLPEcQVm_xPt7ZBCIdJ1FqJIYk5Glli7Wrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏کتابخانه‌ی معروف ‌Pad Shaders⁩ (منبع غنی گرادیان‌ها، پس‌زمینه‌ها و شیدرهای خفن) رایگان و متن‌باز شد!
🎨
✨
‏دیگه نگران لایسنس نباش؛ می‌تونی تمام پلاگین‌ها و ابزارهاش رو تو پروژه‌های شخصی و تجاری استفاده کنی.
https://shaders.paper.design/
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6711" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6710">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚀
دسترسی به قدرت هوش مصنوعی در سرور شخصی؛ آموزش API کلودفلر (Workers AI)
☁️
🤖
اگر برای پروژه‌هایتان به یک هوش مصنوعی قدرتمند (مثل Llama 3 یا Mistral) نیاز دارید، سرویس
Workers AI
کلودفلر یکی از بهترین و بهینه‌ترین گزینه‌هاست. برای استفاده از این سرویس، باید یک API Token اختصاصی بسازید.
🔥
مراحل دریافت API Token در کلودفلر:
1️⃣
ورود به بخش API:
وارد پنل شوید، روی آیکون پروفایل کلیک کرده و به مسیر
My Profile > API Tokens
بروید.
2️⃣
ساخت توکن:
روی
Create Token
کلیک کنید و سپس
Create Custom Token
را انتخاب کنید.
3️⃣
تنظیم مجوزها (بسیار مهم):
در بخش
Permissions
، گزینه
Account
را انتخاب کنید و دسترسی
Workers AI
را روی حالت
Edit
قرار دهید.
در بخش
Resources
، اکانت خود را انتخاب کنید تا دسترسی‌ها محدود به همان اکانت باشد.
4️⃣
نهایی‌سازی:
روی
Continue to summary
و سپس
Create Token
کلیک کنید.
⚠️
توجه:
کد نمایش داده شده را بلافاصله کپی و در جای امن ذخیره کنید؛ این کد دیگر نمایش داده نخواهد شد!
💡
نحوه استفاده:
شما علاوه بر توکن، به
Account ID
نیاز دارید که در صفحه اصلی
Workers & Pages
پنل کلودفلر قابل مشاهده است.
آدرس فراخوانی (Endpoint) شما به این صورت خواهد بود:
[https://api.cloudflare.com/client/v4/accounts/](https://api.cloudflare.com/client/v4/accounts/){ACCOUNT_ID}/ai/run/{MODEL_NAME}
✅
حالا می‌توانید با استفاده از این توکن، مدل‌های هوش مصنوعی کلودفلر را در کدهای خود (پایتون، Node.js و...) فراخوانی کنید.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/6710" target="_blank">📅 16:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFaJBzSINtRWug-x7T15IG9q6vlPrXxoM9UUffmcuZ8f0IPh-I3FGJNMUEebpAH-48J1hxUOxR48fAT-tfQuB8ugNlbJacxs1Y1FMyhWIjRMMEpxDruFFFxx1zB9lruDEw-j3bdhfZK42o44AHHvaQzebOiOA5RIZEOjHsP4TCQwyIVr2dlR1ZPWjBROe-xo9WT5KCJl_j0p4RU7DQakiPJpOXR4R9mZy15edoZfWXN4hi7y83zhRqFMkIrHfo3LUrgMGDj_YRs4UCirUgpuSkTbq-Gx0sAFpyNL4rjRiUmlFJBXxHjwzrdcpzhAi014Hd3NZBtk521p3y4nA8MkVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5
هوش مصنوعی رایگان و قدرتمند شرکت انتروپیک
10 دلار کردیت
با لینک زیر 20 دلار
https://v0.app/ref/94OS6T
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/6709" target="_blank">📅 15:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سایفون رو اپدیت کنین خوشگل شده
🔥
(نسخه بتا)</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/6708" target="_blank">📅 14:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/013ef6f73c.mp4?token=jhBKQFZRZrGFUamJ1ew0YG7pSXuv3K_kXl_fie1yYS4edobprO2O-iGcyWuyT7JTmJMiiTw3zq0JlF-81aG4SzTrxrQK7UcBH_bhyerXVqZC8GirDFivT6RSI2DMt9Kyj8jvT-5hb_nPlafbrb1BavzeFXF0Qn2ARQ5LEzYWvjdVhVHPEsTnt8rUX0USpH7eKdnyZhlcfb2-ysVTdwFQkacwS5eS4yOT0pHGi_WXr-5f_4Af45coxfkiVcfBvHtWS_KyRDAxQ48I2lqXSgDiRa1ZZzLMI38DLHDo92vtodo1gkmUbwlpMPMPajUXbq34xzJLU4rN3fbNqchNFKqAxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/013ef6f73c.mp4?token=jhBKQFZRZrGFUamJ1ew0YG7pSXuv3K_kXl_fie1yYS4edobprO2O-iGcyWuyT7JTmJMiiTw3zq0JlF-81aG4SzTrxrQK7UcBH_bhyerXVqZC8GirDFivT6RSI2DMt9Kyj8jvT-5hb_nPlafbrb1BavzeFXF0Qn2ARQ5LEzYWvjdVhVHPEsTnt8rUX0USpH7eKdnyZhlcfb2-ysVTdwFQkacwS5eS4yOT0pHGi_WXr-5f_4Af45coxfkiVcfBvHtWS_KyRDAxQ48I2lqXSgDiRa1ZZzLMI38DLHDo92vtodo1gkmUbwlpMPMPajUXbq34xzJLU4rN3fbNqchNFKqAxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت 10 تا ایمیل رایگان با ساختن یک ایمیل اتومیک (مولتی اکانت)
https://www.youtube.com/watch?v=XHJ3TwrwG-g</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/ArchiveTell/6707" target="_blank">📅 03:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoVfNuER14bf9xqqzbOkoaLJDW9bicgZoyyWDfGcLBM4JYMC_5Oew9JNSwKZK_mL6sfGU4xH5VZlpIdfQxsrYjQP4hLIJoRdI_cscWaDWiHkTfa9E-WVIcMS_PMXD1qbU9D3cpE4grk3Ut9u6Wj19txuU6Zmo8rZR2Gsqee31iO1RZ8yc8tbe7GCqDx-n4PKmP-KLKLha41Or52qLcJEDlvMtRhzC8v00c5bwjD0zyuagPTM_FEZ6Py7J5_CbCFQZw7k_y55FdhHfV2zr_XQ3BdZwO78-3t8GHqY6XFZ7hLmrlT8NgAJnjG_5l0YIy2z1Hq5N9y5IeOH4wV16zhJTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
قابلیت جدید «وگا کد» فعال شد!
💻
‏همین حالا وارد
‌Mini App⁩
ربات وگا شوید و از قدرت کدنویسی هوشمند لذت ببرید.
✨
‏
🛠
مشخصات فنی:
‏
🔹
پشتیبانی توسط مدل قدرتمند
‌GLM 5.2⁩
‏
🔹
سقف
۵ درخواست
در هر ساعت
⏳
‏
🔹
ورودی تا
۱۵ هزار توکن
📥
‏
🔹
خروجی تا
۱۶ هزار توکن
📤
‏همین الان تستش کنید!
🚀</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/6706" target="_blank">📅 02:43 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
