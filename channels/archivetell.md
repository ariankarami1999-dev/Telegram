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
<img src="https://cdn4.telesco.pe/file/jc1kuLOHnH7CtxhYJt8QonIhPrYWYfpKqnjfGKWQMbcaBayuH2Yvoe_-56KGilW73mCg8upAhFQKOOW9WIui5pSnIL3JOP__BGpoBDQXKFa5zBIH5U1COmn-1Re6Dz8I3YudN-WW6JAMC3FT2s4lYRtuX-Mxxj5a1qzipGzW55VCgtpfWrgJe_Nkez1MvAIByOYTQXu545VnX1G3u9bFqTaXjgXb972Viq1bwS5JOuCDmFilsfe_cdEJDtGu5GhoU39AYJwu_xERIhB2otrxHRu27AJcYmH_N7lpT_Z20QiWBN2Ev24pAtoHSh-fsWV2xg64dvF46XDX_ASaS-yDUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.62K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 20:43:45</div>
<hr>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚀
فضای دیسک ویندوزت کمه؟
🤯
با غیرفعال کردن هیبرنیشن، تا 30 گیگابایت آزاد کن!
ویندوز 10 و 11 به طور پیش‌فرض حالت هیبرنیشن رو فعال دارن که با ذخیره رم روی دیسک (فایل
hiberfil.sys
)، کلی فضا اشغال می‌کنه. اگه ازش استفاده نمی‌کنی، وقتشه آزادش کنی!
✨
چطور فضای دیسک رو برگردونی؟
•
🔍
نمایش فایل‌های مخفی:
Win + R
->
control folders
-> تب
View
->
Show hidden files
رو فعال کن.
•
💾
بررسی فایل: در درایو
C:
دنبال
hiberfil.sys
بگرد. (اگه نبود، قبلاً غیرفعال شده).
•
⚡
غیرفعال‌سازی: ترمینال (CMD/PowerShell) رو به صورت Administrator باز کن و دستور
powercfg -h off
رو اجرا کن.
•
✅
نتیجه: 10 تا 30 گیگابایت فضای دیسک آزاد میشه و حالت "خواب" (Sleep) عادی همچنان کار می‌کنه!
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 52 · <a href="https://t.me/ArchiveTell/6572" target="_blank">📅 20:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=Uiw779kySIPIWjUv-RKVdjk0LaKIJz7KBrZwegoNGDhSIrLrOLdfSZarTX1_C0v7yrtlCAqq9-_wfA9VaPPKZCHWdDsHXgcx6fKAKUyDb9YZuE3sUcnhLDE1OcB2BAVQm3II3CifQiSsRlAvBiMsUpAaXeHJVjWmKrIzyaPl8QbP9gRDsJ9aoYTKhdA_WMmLP0KVpIpkEWCEzC7QQrbKycdWUoSpRqrfeLYD5zKzfYGHJW_7WKpB3DAADQyxUsQuCO2We8ikWdyTMCrlIH-qNF0Xk3GdD3OMU7pSH3bwHHqE3X5mmSPYUUzEUaltMnnI9BbaGxMnA99yeeC4Ybj7jlup3HPeBlvGziengiWGQ7IdC3e7oR7ZEErLMH2KlN8WysowY7bdGhPxLJ9_q1sGsch6m-sudbOJw3qqDh9XVTtjPnk0JZcCWrsn4cirsUegwPvELqUhUwHiStf-3jDnI_Jc18tO2QGHIXI3BDTWiYaLPXEf9C9K5xEs5PUu6RdP46gI5DsuBes0xGcIxg3w3dR6ueTiibatbWw1l-RV390ah-6GcW5wpPXXeJigYyFUYC9dqgB1h6SNOtqRHagzyGTdIzYkH8YLpGXJcp-LpivXzk2Q05BQHB1Eb2EhcSrs8AclL7diyaUE8zoFSbnpyzP5x5sMJkZ7_wV-vM3_H1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1ffe541d.mp4?token=Uiw779kySIPIWjUv-RKVdjk0LaKIJz7KBrZwegoNGDhSIrLrOLdfSZarTX1_C0v7yrtlCAqq9-_wfA9VaPPKZCHWdDsHXgcx6fKAKUyDb9YZuE3sUcnhLDE1OcB2BAVQm3II3CifQiSsRlAvBiMsUpAaXeHJVjWmKrIzyaPl8QbP9gRDsJ9aoYTKhdA_WMmLP0KVpIpkEWCEzC7QQrbKycdWUoSpRqrfeLYD5zKzfYGHJW_7WKpB3DAADQyxUsQuCO2We8ikWdyTMCrlIH-qNF0Xk3GdD3OMU7pSH3bwHHqE3X5mmSPYUUzEUaltMnnI9BbaGxMnA99yeeC4Ybj7jlup3HPeBlvGziengiWGQ7IdC3e7oR7ZEErLMH2KlN8WysowY7bdGhPxLJ9_q1sGsch6m-sudbOJw3qqDh9XVTtjPnk0JZcCWrsn4cirsUegwPvELqUhUwHiStf-3jDnI_Jc18tO2QGHIXI3BDTWiYaLPXEf9C9K5xEs5PUu6RdP46gI5DsuBes0xGcIxg3w3dR6ueTiibatbWw1l-RV390ah-6GcW5wpPXXeJigYyFUYC9dqgB1h6SNOtqRHagzyGTdIzYkH8YLpGXJcp-LpivXzk2Q05BQHB1Eb2EhcSrs8AclL7diyaUE8zoFSbnpyzP5x5sMJkZ7_wV-vM3_H1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو بخش انتخاب پنل ۴ تا انتخاب وجود داره
طبق تجربه نوا و زئوس پنل های خوبین</div>
<div class="tg-footer">👁️ 158 · <a href="https://t.me/ArchiveTell/6571" target="_blank">📅 20:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚀
معرفی Cloud WZA
با Cloud WZA مدیریت سرور و ساخت کانفیگ‌های کلود ساده‌تر از همیشه شده است!
🤖
یک ربات تلگرامی قدرتمند برای ساخت کانفیگ و مدیریت سرویس‌ها، با امکان دیپلوی سریع پنل‌های محبوب:
⚡
Nova
⚡
Zeus
⚡
BPB
⚡
Nahan
فقط با یک دکمه پنل موردنظر خودت را دیپلوی کن و بدون دردسر شروع به استفاده کن
✅
✨
امکانات Cloud WZA:
🔹
ساخت و مدیریت کانفیگ کلود
🔹
دیپلوی خودکار پنل‌ها
🔹
مشاهده میزان مصرف کاربران
🔹
ساخت کاربر جدید
🔹
مدیریت کاربران
🔹
تغییر رمز عبور
🔹
مدیریت آسان و سریع از داخل تلگرام
Cloud WZA؛ راهی ساده، سریع و هوشمند برای مدیریت سرویس‌های کلود
☁️
🚀
🤖
ربات:
@nova_wzabot
ــــــــــــــــــــــ
توسعه داده شده توسط AssA
✨</div>
<div class="tg-footer">👁️ 143 · <a href="https://t.me/ArchiveTell/6570" target="_blank">📅 20:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=Yz7fSgeo65wsH--YcIrjrZ8cQlVk5BK0J4j_Ryn7WPBiBBZAaeens52LHoCjt95kxQ15usMgIubhqJaazY0-kB3_a4D_uHIxcBTfMR1aGa5LEJNtpqFV9TFUqmj3PdFcpQjBzDP6hmYg9sD14BCieyfS-suJypyfrMwmE4iPfWOt89x8LDzgREvGr5CJQu0-xnStGEDuscg4rm0ziw_r5bnNbHEvRoyzONh-ahH91u5s32VIjznHXRmO3uRGW1wsVV2ZkNLqutWut5nZe48M4j8xUbNJcx81l18kC3e695Xmk3f2JBh-CQiSZoCEl8izFn9hNNMCLjkL0_ZSDPgDEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b5316c72.mp4?token=Yz7fSgeo65wsH--YcIrjrZ8cQlVk5BK0J4j_Ryn7WPBiBBZAaeens52LHoCjt95kxQ15usMgIubhqJaazY0-kB3_a4D_uHIxcBTfMR1aGa5LEJNtpqFV9TFUqmj3PdFcpQjBzDP6hmYg9sD14BCieyfS-suJypyfrMwmE4iPfWOt89x8LDzgREvGr5CJQu0-xnStGEDuscg4rm0ziw_r5bnNbHEvRoyzONh-ahH91u5s32VIjznHXRmO3uRGW1wsVV2ZkNLqutWut5nZe48M4j8xUbNJcx81l18kC3e695Xmk3f2JBh-CQiSZoCEl8izFn9hNNMCLjkL0_ZSDPgDEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">KREA.AI
Enhancer
تصاویر پیکسلی را تا 22K ارتقا دهید!
دیگر نگران کیفیت پایین عکس‌هایتان نباشید؛
KREA.AI
با ابزار قدرتمند Enhancer خود، تصاویر بی‌کیفیت را به وضوح خیره‌کننده تبدیل می‌کند.
🖼️
✨
✨
قابلیت‌ها:
•
🔹
ارتقاء کیفیت تصاویر تا وضوح 22K
📈
•
⚡
تبدیل پیکسل‌های بی‌کیفیت به جزئیات واضح و شارپ
🔍
•
🛠️
استفاده آسان و سریع برای نتایج حرفه‌ای
🚀
🌐
Site
#AI
#ImageEnhancement
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 396 · <a href="https://t.me/ArchiveTell/6569" target="_blank">📅 20:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxRifyTOfXnvkXMG8zFljjynpoGGq_yzvkuduTORaxOK-LU_hSsZucSKSa5zusf109Ad1ETq3p2xoTrFfwKYcYl4efrn4x6Jfvk0P9M5bDVrkJyFSa2xTMhiuCqh69ijOJHhRoC742BgL21mtXGFTbr8lqWXjX8BnjcBWsSUsBkZ7nAoeGHQplzyVPzC5cWJLexHrB1v00MlmTh9HVCtv4fbxH8e5xc3sPTi81YZZnvRq0gLu7g46vemS_-c_PTcxoAxG5izsnx60tHe9z5D6y-hhmBEOxzis_Y1f12ltW6o_j36CfggtjsJ4fhN5OmR8wa0qKFL9lTjWZgF-tFLWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1000 برنامه رایگان برتر برای آیفون و کل اکوسیستم اپل: یک دانشنامه واقعی از نرم‌افزارهای مفید در گیت‌هاب ساخته شده است!
🍏
در این مجموعه همه موارد ضروری پیدا خواهید کرد: از پیام‌رسان‌های امن گرفته تا ابزارهایی برای تماشای فیلم از طریق تورنت.
🎬
🔐
🌐
GitHub
#Apple
#iPhone
#FreeApps
#GitHub
#OpenSource
#Productivity
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 623 · <a href="https://t.me/ArchiveTell/6568" target="_blank">📅 19:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=PmEUMmvRpMVTDxN5LLLhnAdeq_3JZ1bJSyTGkpTV4BA6h7agIkS7H0DRAL72Nk_d89igNrRrxa3Xu7D_6_Fn4JUeM0bZ_sprX-9ueqpSVLyNL6RLuB7hq01AlZuoAIC-ui8_2mGzOlpW-R_0ctiJEnMIZ5Dcrvnxa7oxChW43BfaSw8bfvhXSkJzw1z2jngdWtsjv0_EV3Vdcrtw9NPd16lZ0hqSE5MMv70HYQRAVd13I4xn1DiJaStMduPauQE50k_xYUBux8pBFvKc8_29mhr_I0UdYEUBFUkYy37o3JVunp4ca5DWP87GBP_8GgWjbFWffVEmvjvOdsmdYMOWcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9395cb697.mp4?token=PmEUMmvRpMVTDxN5LLLhnAdeq_3JZ1bJSyTGkpTV4BA6h7agIkS7H0DRAL72Nk_d89igNrRrxa3Xu7D_6_Fn4JUeM0bZ_sprX-9ueqpSVLyNL6RLuB7hq01AlZuoAIC-ui8_2mGzOlpW-R_0ctiJEnMIZ5Dcrvnxa7oxChW43BfaSw8bfvhXSkJzw1z2jngdWtsjv0_EV3Vdcrtw9NPd16lZ0hqSE5MMv70HYQRAVd13I4xn1DiJaStMduPauQE50k_xYUBux8pBFvKc8_29mhr_I0UdYEUBFUkYy37o3JVunp4ca5DWP87GBP_8GgWjbFWffVEmvjvOdsmdYMOWcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک برنامه‌نویس جوان توانست با ترکیب علاقه و مهارتش، درختی که با پایتون کدنویسی کرده بود را به قیمت 8 هزار دلار بفروشد. این پروژه از 100 دلار شروع شد و در چند روز به این قیمت رسید
🤯
#Python
#Programming
#Business
#DigitalArt
#Success
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 846 · <a href="https://t.me/ArchiveTell/6567" target="_blank">📅 18:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚀
آموزش اجرای Opus 4.8 در ترمینال با Claude Code توسط Agentrouter
1️⃣
ثبت‌نام در Agentrouter
وارد سایت
Agentrouter
شوید
با حساب Github ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🎉
شما 125 دلار کریدیت گرفتید
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Token
یک API Key جدید بسازید و ذخیره کنید
3️⃣
نصب Termux (روی موبایل)
📱
اگر موبایل دارید، از Termux استفاده کنید
4️⃣
دستورات نصب در ترمینال ( به ترتیب وارد کنید )
1⃣
آپدیت Termux
pkg update && pkg upgrade -y
2⃣
نصب ابزارها
pkg install proot-distro nano -y
3⃣
نصب Ubuntu
proot-distro install ubuntu
4⃣
ورود به Ubuntu
proot-distro login ubuntu
5⃣
آپدیت Ubuntu
apt update && apt upgrade -y
6⃣
نصب ابزارهای ضروری
apt install -y sudo ca-certificates curl wget git nano gnupg lsb-release build-essential python3 make g++
apt install -y curl nano nodejs npm
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
7⃣
نصب Claude Code فیلترشکن بزن
npm install -g @anthropic-ai/claude-code@2.1.167
8⃣
تنظیمات Claude Code
mkdir -p ~/.claude
دستور زیر را برای باز کردن فایل تنظیمات بزنید:
nano ~/.claude/settings.json
کد زیر را داخل فایل پیست کنید (کلید خود را جایگزین کنید) و با زدن Ctrl + X و سپس y و در نهایت Enter ذخیره کنید:
{
"env": {
"ANTHROPIC_API_KEY": "کلیدت",
"ANTHROPIC_BASE_URL": "https://agentrouter.org/",
"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"
},
"permissions": {
"allow": [],
"deny": []
},
"apiKeyHelper": "echo 'کلیدت'"
}
▶️
اجرای Claude Code ( با فیلترشکن خوب وارد شوید )
claude
✨
حالا آماده استفاده است
🚀
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 955 · <a href="https://t.me/ArchiveTell/6566" target="_blank">📅 18:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚀
دسترسی رایگان به API غول‌های هوش مصنوعی!
با لینک زیر به جدیدترین مدل‌ها دسترسی پیدا کنید:
🔹
GPT 5.4
🔹
Claude Sonnet 4.6
✅
سازگار با همه پلتفرم‌ها:
ربات تلگرام ، وب‌سایت ، Codex و Claude Code
🔗
zyloo.io
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/ArchiveTell/6565" target="_blank">📅 17:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=isfPBAtoxgq1SwOjY1GGkYky1PmQwyNGrkqebc9OI7FNOlkiUreKU7DIzWU3dzVx1E-sB7bdgNrBmT7m4xRzcdwFH-QssWJmpixTD-f_0GbK5CMCoCShAwAH-ZIm1XGg34JfUZ3KwOmb2Xr2Uc3Qba_vKuTxP4ng1La7Y5epw1TkIKuh_82K0oZnZa4zycsiw6nT8K7XxJKlnhMUb3Jbw12doD1g2GTCTDdSoHiNbE0NbsVEL2SokAUKvRdVc4wIbMD2fBGs_MfXWpB5mIBY4tdmguDAvxa1jgAHYSJTws9TKJOoj-NfGZnVSaYhHKsdu19sQLDVGU0ys4l6S3Wkcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a86123e61.mp4?token=isfPBAtoxgq1SwOjY1GGkYky1PmQwyNGrkqebc9OI7FNOlkiUreKU7DIzWU3dzVx1E-sB7bdgNrBmT7m4xRzcdwFH-QssWJmpixTD-f_0GbK5CMCoCShAwAH-ZIm1XGg34JfUZ3KwOmb2Xr2Uc3Qba_vKuTxP4ng1La7Y5epw1TkIKuh_82K0oZnZa4zycsiw6nT8K7XxJKlnhMUb3Jbw12doD1g2GTCTDdSoHiNbE0NbsVEL2SokAUKvRdVc4wIbMD2fBGs_MfXWpB5mIBY4tdmguDAvxa1jgAHYSJTws9TKJOoj-NfGZnVSaYhHKsdu19sQLDVGU0ys4l6S3Wkcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮
Morflax Mesh — تصاویر سه‌بعدی در مرورگر
این سرویس امکان ساخت تصاویر سه‌بعدی را در چند ثانیه فراهم می‌کند. عناصر را بکشید و رها کنید، فرمت‌ها را تغییر دهید، رنگ‌ها و نورپردازی را تنظیم کنید — همه چیز مستقیماً در مرورگر کار می‌کند.
تعرفه پایه رایگان است و دانلودهای نامحدود دارد. با پرداخت ۸ دلار در ماه، به کتابخانه سه‌بعدی، خروجی با کیفیت بالا (.jpg و .png) و قالب‌های آماده دسترسی پیدا می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/6564" target="_blank">📅 16:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nC3w9LV5cvUXwOBMCnN6T0GV-NwnPKPM2tKyze4UBr3U-d-siOD7ROqPlPCuJhSIhuAGql5d8p2RFrpg5q4pHpOAJjdVgyvP8oTtGWN55DXWyXGCQ3zvtm3p4zjHg_7JLfl9i3-vAWquHk5OvTj9OaSuGBS6IL_XV8veoX8hegcR_jIV4JHa-9mKNvrviLdRrJq7KB1HJ6YIt-FqtUBXsIxxosvReZwyRqTm3rJlyyrhtHqLC_3Unyib9u7tb-EtjxD3SfjNI3nhG3GT2evhppftmgSf-UhF0hOgbrp5aIuwwLyrZu3g4QsqVlk_BJPL6ThP1be72HC60Rvpso5vCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
یه ترفند خفن برای چند برابر کردن سرعت گوشی‌های سامسونگ!
احتمالاً شما هم فکر می‌کنید هرچی مقدار RAM بیشتر باشه سرعت گوشی بالاتره، اما یه گزینه‌ای تو گوشی‌های سامسونگ هست به اسم RAM Plus که به صورت پیش‌فرض روی همه مدل‌ها فعاله و برخلاف اسمش، تو خیلی از مواقع باعث لگ و کندی اعصاب‌خردکن میشه!
🤦‍♂️
🧐
اما چرا این اتفاق میفته؟
قابلیت Ram Plus در واقع میاد بخشی از حافظه داخلی گوشی رو به عنوان «رم مجازی» اشغال می‌کنه تا برنامه‌های بیشتری تو پس‌زمینه باز بمونن. از اونجایی که سرعت حافظه داخلی به مراتب از رم فیزیکی (سخت‌افزاری) خود گوشی پایین‌تره، وقتی سیستم می‌خواد اطلاعات رو بین این دو جابجا کنه، پردازنده بی‌دلیل درگیر میشه و گوشی کُند میشه.
🛠
چطوری غیرفعالش کنیم تا گوشی پرواز کنه؟
کافیه وارد تنظیمات گوشی بشید و دقیقاً این مسیر رو برید:
⚙️
Settings > Device Care > Memory > RAM Plus
(اگر منوی گوشیتون فارسیه: تنظیمات > مراقبت از دستگاه > حافظه > رم پلاس)
گزینه بالای صفحه رو روی حالت Off (خاموش) قرار بدید.
بعد از این کار گوشی ازتون می‌خواد که یک بار ری‌استارت بشه)
✅
🆔
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/ArchiveTell/6563" target="_blank">📅 15:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚀
معرفی MinerU؛ استخراج جادویی و سریع متن از انواع فایل‌ها!
📄
✨
اگر برای پروژه‌های هوش مصنوعی (مثل RAG)، کارهای تحقیقاتی یا روزمره نیاز به استخراج متنِ تمیز از فایل‌های مختلف دارید، ابزار رایگان و متن‌باز
MinerU
یک شاهکار به تمام معناست!
🔥
ویژگی‌های شگفت‌انگیز این ابزار:
1️⃣
پشتیبانی همه‌جانبه:
تبدیل فایل‌های PDF، Word، Excel، PowerPoint و حتی اسناد اسکن‌شده به متن خالص و بدون به هم ریختگی.
2️⃣
سرعت پردازش خیره‌کننده:
می‌تواند یک فایل PDF دویست صفحه‌ای را در کمتر از ۱.۵ دقیقه پردازش کرده و متن آن را استخراج کند!
3️⃣
اجرای کاملاً محلی (Local):
بدون نیاز به اینترنت و سرورهای ابری روی کامپیوتر خودتان اجرا می‌شود که برای حفظ حریم خصوصی فایل‌های حساس بی‌نظیر است.
4️⃣
بهترین دوست هوش مصنوعی:
پشتیبانی از پردازش گروهی فایل‌ها (Batch) و قابلیت ادغام و همگام‌سازی بی‌نقص با ایجنت‌های هوش مصنوعی مانند
Claude
،
Cursor
و سایر LLMها.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#MinerU
#PDFExtractor
#OCR
#AI
#Claude
#Cursor
#OpenSource
#Github
#Tools
#RAG
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/ArchiveTell/6562" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1f4gX8ws72PSZ2oBp5mwbkZ9NU5re2-hovKllor0RKQmkgOdbkpKXDBaLlSL3YJQgIRbdmhoRETY_2_jmyxBbJX5XasX8TIk5Nw2rsGK-IDie6GMNkezdaNMeSXv9L9GkPWdQZw8j-dFo6H2Rbifonu4YgdM4xqkuoPS6WufdDunz9bMDNVEZ6venPNiQ0_acim-kLGG4RJ1aAK6jZogtbKST83Pl4HdMyhvopLIzC_b0mCBQyM0OjO98EfVdblPz29GCSViaC05wL4tB0VqxVzKfXpsQzFv9S2qUm1pF3SbSnYt4zs5Q1oZacjRTLzcM6SUP97PMazJFpfjSShIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Popit Music: ساخت موسیقی با هوش مصنوعی و مالکیت کامل اثر
🎵
✨
قابلیت‌ها:
•
🔹
انتخاب ژانر و حالت برای تولید سریع ترک
•
⚡
ورود خودکار به پلی‌لیست و رقابت با آثار دیگر
•
🛠️
مالکیت کامل حقوق موسیقی متعلق به شماست
•
📦
دو بار تولید رایگان برای شروع
🌐
Site
#AI
#Music
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/6561" target="_blank">📅 13:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚀
معرفی droidMirroring-mac؛ تجربه اکوسیستم اپل برای کاربران اندروید در مک!
📱
💻
✨
اگر از گوشی اندرویدی استفاده می‌کنید اما کامپیوتر شما Mac (سیستم‌عامل macOS) است، احتمالاً همیشه حسرت قابلیت یکپارچگی عمیق اکوسیستم اپل (مثل iPhone Mirroring و Handoff) را خورده‌اید. پروژه جدید و متن‌باز
droidMirroring-mac
دقیقاً برای حل همین مشکل و پر کردن این خلأ توسعه یافته است!
🔥
ویژگی‌های جذاب این ابزار:
1️⃣
انعکاس صفحه (Screen Mirroring):
مشاهده و کنترل کامل گوشی اندرویدی مستقیماً از روی صفحه نمایش مک (دقیقاً شبیه به قابلیت جذاب iPhone Mirroring در نسخه‌های جدید macOS).
2️⃣
کلیپ‌بورد مشترک (Universal Clipboard):
همگام‌سازی بی‌وقفه کلیپ‌بورد بین گوشی و مک؛ متنی را در اندروید کپی کنید و در مک Paste کنید (و بالعکس).
3️⃣
رایگان و متن‌باز:
این پروژه کاملاً Open-Source است و بدون نیاز به خرید اشتراک یا برنامه‌های تجاری گران‌قیمت، ارتباطی عمیق بین دو اکوسیستم متفاوت ایجاد می‌کند.
اگر به تازگی از آیفون به اندروید مهاجرت کرده‌اید ولی نمی‌خواهید راحتیِ کار با مک را از دست بدهید، این پروژه گیت‌هابی یک معجزه برای شماست!
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Android
#macOS
#ScreenMirroring
#Productivity
#OpenSource
#Github
#Tools
#Handoff
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/6560" target="_blank">📅 08:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6559">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY8zYupJdxq920eK5pAGv2UzQ6i5m2AupMOUDLS3AgB8ROHRxtCjY_EWjzLT6rFlLfDc3o6GD0Eyf-glUANN4b3EA8-_wVva3d4pb9TuIQpNkjqJfHyclw3NXLlPx0kiLIhmN0JO89dN6PvghfzvcpaST3NLnE5UgT4JDCiwICt07y3hLL8IEZ1S7LDi-pxRl1OqoHCgpb85e_4LqWh91cTjVVJrC4O34UTyQlQPp2VAbznJjiI6oFPYLgoHSstUfEGVfNZIp0sk5s5CvsXzBhCbq5566QoUBTD61mbKhrfKlHpuIT0fOGFGbEDtQg9-6WFOuQQuCAj9lrN3S-30Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">> توسعه‌دهنده‌ای با نام مستعار slqnt نسخه وب بازی افسانه‌ای Half-Life 2 را معرفی کرد.
اکنون می‌توانید این شوتر افسانه‌ای را مستقیماً در مرورگر اجرا کنید، بدون نیاز به نصب برنامه‌ها یا راه‌اندازها.
بازی پایداری شگفت‌انگیزی را نشان می‌دهد و کاربران در حال آزمایش پروژه‌هایی مانند
Ravenholm
و
City-17
در مرورگر هستند!
🌐
Site
#HalfLife2
#WebGame
#Gaming
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6559" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8491578554.mp4?token=cuBklSUfd9gedgYT2Ck9o1_FLRKFFFNvdJ3eylOK0Nd8v8IvxQK0PW6gJ9Q2L-MwTD41NOY5JoIIfayuhcvJsvrThXzd9NYZjP6RHjOQGI61RvXl2hC0LHNpxLjUpAv90hUgnk5dCry_JkEcaBAkSvrvvXDH9CC0Zi2uppKzczY4pKo-711ZEaizDYN8GQTdaJPH8FpJJxpps3BWsZ7f0Rg-ChoCGfS1KQoqlRlNehFf380IwcsR0jOR1q10Ml1hew9Yv--DOWhCH8H3XqSda68Hmar0EUzka_IvTjrOE2S4OLGpqY_f17OjjD7hnOOsGQcx9P__ryMI_H-OUO35iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8491578554.mp4?token=cuBklSUfd9gedgYT2Ck9o1_FLRKFFFNvdJ3eylOK0Nd8v8IvxQK0PW6gJ9Q2L-MwTD41NOY5JoIIfayuhcvJsvrThXzd9NYZjP6RHjOQGI61RvXl2hC0LHNpxLjUpAv90hUgnk5dCry_JkEcaBAkSvrvvXDH9CC0Zi2uppKzczY4pKo-711ZEaizDYN8GQTdaJPH8FpJJxpps3BWsZ7f0Rg-ChoCGfS1KQoqlRlNehFf380IwcsR0jOR1q10Ml1hew9Yv--DOWhCH8H3XqSda68Hmar0EUzka_IvTjrOE2S4OLGpqY_f17OjjD7hnOOsGQcx9P__ryMI_H-OUO35iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم Caveman دقیقاً برای شما ساخته شده است! این افزونه کاربردی با…</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/6557" target="_blank">📅 22:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6556">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚀
معرفی افزونه Caveman؛ ابزاری برای کاهش شدید مصرف توکن در هوش مصنوعی!
🧠
✨
اگر زیاد با چت‌بات‌های هوش مصنوعی کار می‌کنید و نگران محدودیت پیام‌ها (Limits) یا هزینه‌های مصرف توکن هستید، افزونه کروم
Caveman
دقیقاً برای شما ساخته شده است! این افزونه کاربردی با بهینه‌سازی کلمات، مصرف توکن را در سرویس‌هایی مثل
ChatGPT
،
Claude
،
Gemini
و سایر مدل‌ها به حداقل می‌رساند.
🔥
این افزونه چطور کار می‌کند و چه ویژگی‌هایی دارد؟
1️⃣
صرفه‌جویی تا ۷۵ درصد:
این ابزار پرامپت‌های شما و پاسخ‌های هوش مصنوعی را به صورت خودکار بازنویسی می‌کند و با حذف کلمات اضافه، مصرف توکن‌های خروجی را تا
۷۵٪
کاهش می‌دهد.
2️⃣
حفظ معنای اصلی:
با وجود کوتاه شدن جملات (شبیه به لحن انسان‌های اولیه!)، پیام اصلی و محتوای علمی/فنی به هیچ وجه از بین نمی‌رود.
3️⃣
پاسخ‌های بدون حاشیه:
به جای خواندن پاراگراف‌های طولانی و خسته‌کننده، هوش مصنوعی را مجبور می‌کند تا جواب‌هایی کاملاً خلاصه، سرراست و پرمحتوا به شما بدهد.
4️⃣
پشتیبانی گسترده:
این افزونه برای تمامی سرویس‌های معروف LLM قابل استفاده است.
💡
نکته کاربردی:
ای
ن ابزار مخصوصاً برای کاربران نسخه‌های رایگان Claude و ChatGPT که زود به سقف محدودیت پیام می‌رسند، یک ترفند طلایی محسوب می‌شود!
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#ChatGPT
#Claude
#Gemini
#ChromeExtension
#Caveman
#PromptEngineering
#Tools
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6556" target="_blank">📅 22:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=QXV047uVcgELxMLQgY7ucb0Rhqs-ORJXO3s-zlG8jOxJYP0rebMzgPkoMm0RNHq532ZzkWvDevi3ls5reSeDk5ff0HnV-pcBqufGuYD1D1iC_hffe2r-5qV0BQKDqJK3_Jaie1uysqQbidEXVySNwIJHvD-KnnKAYF32k55f7wRDintFj7gZeHZJVgDwaQMsg0yMRz6NWNiiyQ0Ukadk8BDIJ2cVBJTx--jpPNQz9ZAHOR-8mGaev2iECwg4LUsEi7Ew9i7ATYOVSTHzBoKvLNw5qws6f__JRkNG1HbQG_zmUe1za-XcxcV_W1JRRZA_azqKLR2BJJaFDNqki4DrlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c485a59e.mp4?token=QXV047uVcgELxMLQgY7ucb0Rhqs-ORJXO3s-zlG8jOxJYP0rebMzgPkoMm0RNHq532ZzkWvDevi3ls5reSeDk5ff0HnV-pcBqufGuYD1D1iC_hffe2r-5qV0BQKDqJK3_Jaie1uysqQbidEXVySNwIJHvD-KnnKAYF32k55f7wRDintFj7gZeHZJVgDwaQMsg0yMRz6NWNiiyQ0Ukadk8BDIJ2cVBJTx--jpPNQz9ZAHOR-8mGaev2iECwg4LUsEi7Ew9i7ATYOVSTHzBoKvLNw5qws6f__JRkNG1HbQG_zmUe1za-XcxcV_W1JRRZA_azqKLR2BJJaFDNqki4DrlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎓
ساخت دوره‌های آموزشی شخصی‌سازی شده با Gemini
🚀
✨
قابلیت‌ها:
•
🔹
طراحی مسیر یادگیری بر اساس هدف (مصاحبه، پروژه یا تحصیل)
•
⚡
تولید خودکار ساختار شامل سخنرانی، تصویر و کد نمونه
•
🛠️
شامل آزمون‌های سنجش یادگیری
•
📦
دسترسی رایگان و فوری برای همه کاربران
🌐
Site
#AI
#Education
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/6555" target="_blank">📅 21:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6554">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJ__2B3xA8cZHMbmUhdTqVRc28XE-TWThx5KgA4GX3dxXby6pzHFDPNxwwjdrdgYtB1zmEm2aQ7SqAyptI6v6lOAxs1-zYlV5MPP4O0W8HaYRjZs__TxjkIf1hf9nt_VtWyrijbV7XTyEkQNjKWqTFw2577fcRVLfL5YtDi9AnEAIYTFz0XMjXSoOrdaUC1jxho3QsKJ_HixkBipNSMgEx99IJeCFhbfdCigSrLOZkKVnUqVftn6VDR-YJn0ToiMqcXTaSEYtXKxMdIVhtSnNwxLVK-GU09wV7Gpx0o4ERUWMmgU4b-zookwuhxKhudShjV1RMK-wxtvuRJoZiyxfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
ویدیوهای یوتیوب را تا کیفیت 8K و بدون محدودیت دانلود کنید
🚀
✨
قابلیت‌ها:
•
🔹
دانلود ویدیوهای تکی و پلی‌لیست‌های کامل
•
⚡
پشتیبانی از کیفیت 144p تا 8K
•
🎧
خروجی MP4 و MP3
•
🛠️
ذخیره تنظیمات دلخواه کاربر
•
📦
دانلود دسته‌ای با سرعت کامل
🌐
GitHub
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/6554" target="_blank">📅 21:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚀
Vibe
ابزار آفلاین تبدیل صوت و ویدیو به متن
🎙
✨
وایب برنامه کراس‌پلتفرم مبتنی بر
OpenAI Whisper
برای پیاده‌سازی متن فایل‌های صوتی و ویدیویی به صورت کاملاً
آفلاین
و با حفظ حریم خصوصی است.
🔥
ویژگی‌ها:
1️⃣
پشتیبانی از زبان‌های متنوع با قابلیت ترجمه به انگلیسی.
2️⃣
خروجی‌های متنوع: زیرنویس (SRT, VTT)، متنی (DOCX, PDF, TXT)، HTML و JSON.
3️⃣
پردازش گروهی، استخراج متن از لینک‌ها و ضبط مستقیم صدا.
4️⃣
بهره‌گیری از GPU برای سرعت بالا و پشتیبانی از CLI.
﻿
⚡️
مشخصات:
* زبان: TypeScript / JavaScript
* پلتفرم: ویندوز، مک، لینوکس
🔗
لینک
🔵
@ArchiveTell
| Bachelor
⚡️
#Vibe
#AI
#OpenAI
#Transcription
#Privacy
─────────────────────────────</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/6553" target="_blank">📅 20:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپخش کانفیگ رایگان🔥</strong></div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
:
60GB
🧭
: حداقل 1 دعوت
👥
: 0/60
💾
: 60 GB
⏰
: 5 روز
🟢
فعال</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6552" target="_blank">📅 14:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🌐
دامنه رایگان
eu.cc
با GNAME! (فیلتر شده ظاهرا)
فرصتی عالی برای ثبت دامنه رایگان
eu.cc
که برای ساخت سایت‌های سبک، تست یا پروژه‌های شخصی عالیه!
✨
ویژگی‌ها:
•
🆓
ثبت دامنه رایگان
•
🔄
تمدید رایگان سالانه
•
☁️
پشتیبانی از میزبانی Cloudflare (CF)
•
🎯
هر کاربر تا ۳ دامنه می‌تواند ثبت کند
•
💡
مناسب برای سایت‌های سبک، تست و پروژه‌های کوچک
همین الان دامنه رایگان خودت رو ثبت کن!
👇
🌐
Site
#دامنه_رایگان
#GNAME
#Cloudflare
#وبسایت
#هاستینگ
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/ArchiveTell/6550" target="_blank">📅 14:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚀
معرفی 1Hosts؛ سپر دفاعی پیشرفته شما در برابر تبلیغات و ردیاب‌ها!
🛡
✨
اگر به دنبال یک لایه امنیتی قوی برای مسدودسازی تبلیغات مزاحم، ردیاب‌ها (Trackers) و بدافزارها هستید، پروژه متن‌باز
1Hosts
یکی از بهترین و بهینه‌ترین فیلترهای DNS و لیست‌های مسدودسازی (Blocklists) در گیت‌هاب است. این ابزار از سال ۲۰۱۷ به‌طور مداوم در حال توسعه بوده و با وجود حجم کم، عملکردی بسیار قدرتمندتر از جایگزین‌های سنگین‌تر دارد.
🔥
نسخه‌های موجود در این پروژه:
🟢
نسخه Lite (متعادل):
ایده‌آل برای استفاده روزمره. این نسخه با کمترین میزان خطای مسدودسازی (False Positives)، تجربه‌ای روان از وب‌گردی به شما می‌دهد (نصب کنید و فراموش کنید).
🔴
نسخه Xtra (تهاجمی / Beta):
طراحی‌شده برای کاربرانی که به بالاترین سطح حریم خصوصی نیاز دارند. این نسخه به شدت سخت‌گیر است و هرچند بالاترین سطح امنیت را فراهم می‌کند، اما ممکن است عملکرد برخی سایت‌ها را دچار اختلال کند.
⚙️
پشتیبانی و سازگاری گسترده:
شما می‌توانید لینک‌های 1Hosts را به راحتی در طیف وسیعی از نرم‌افزارها و سرویس‌ها اضافه کنید:
مرورگر و شبکه:
uBlock Origin, AdGuardHome, Pi-hole
اندروید و iOS:
AdAway, Blokada, InviZible Pro, DNSCloak
سرویس‌های DNS:
همگام‌سازی آسان با NextDNS, ControlD و RethinkDNS
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
──────────────────────────────</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/6549" target="_blank">📅 14:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بیایین با عاباس آشنا بشیم
❤️
دیس وگاس و عاباس
😝</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/6548" target="_blank">📅 13:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚀
ارتقای رتبه هر سایتی در نتایج جستجو با کمک هوش مصنوعی!
🔝
✨
ابزار جدید و متن‌بازی پیدا کردیم که وب‌سایت شما را به صورت دقیق آنالیز کرده و به شما کمک می‌کند تا جایگاه آن را در نتایج جستجوی گوگل (SEO) بهبود ببخشید. پروژه
open-seo
یک دستیار هوشمند و همه‌کاره برای کارهای سئو است.
🔥
قابلیت‌های کلیدی این ابزار:
1️⃣
**تحلیل خودکار:** سایت شما را بررسی کرده و توصیه‌ها و پیشنهادات عملی برای بهبود سئو ارائه می‌دهد.
2️⃣
**رصد دامنه و رتبه‌ها:** وضعیت سلامت دامنه را بررسی و جایگاه سایت شما را در کلمات کلیدی مختلف ردیابی می‌کند.
3️⃣
**نظارت بر منشن‌ها:** اشاره‌ها و منشن‌های نام برند شما را در موتورهای جستجو زیر نظر می‌گیرد.
4️⃣
**اتصال به ایجنت‌های هوش مصنوعی:** پشتیبانی کامل از اتصال به Claude Code، Codex و سایر ایجنت‌ها از طریق پروتکل **MCP** (Model Context Protocol).
5️⃣
**اتوماسیون سئو:** دارای سناریوهای آماده برای خودکارسازی کارهای تکراری و زمان‌بر سئو.
6️⃣
**راه‌اندازی سریع:** به سادگی و تنها در عرض چند دقیقه از طریق **Docker** اجرا می‌شود.
🔗
لینک مخزن گیت‌هاب برای دانلود و نصب
🔵
@ArchiveTell
| Bachelor
⚡️
#SEO
#AI
#OpenSource
#Docker
#WebDevelopment
#Github
#Tools
#MCP
#SEO_Automation</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6547" target="_blank">📅 12:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ظاهرا Claude Fable برگشته
🔥
❤️‍🔥</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/6546" target="_blank">📅 12:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دوستان دقت کنید
تو گیتهاب پروژه ها میتونن ویروسی باشن
بررسی کنید
متن باز هست ولی نیاز به بررسی دارن پروژه ها
ولی تلاش ما بر اینه که معتبر هارو بذاریم اکثرا</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6545" target="_blank">📅 10:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔥
🔥
ویژه
ساخت اکانت جیمیل بدون محدودیت سیم کارت، وریفای و ...
(تست نشده)
فقط روی ویندوز
github.com/ShadowHackrs/gmail-account-creator
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/6543" target="_blank">📅 09:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ویژه
🔥
🔥
🚀
تبدیل گوشی‌های قدیمی اندروید به سرور لینوکس یا هاب خانه هوشمند!
🐧
📱
اگه تو خونه یه گوشی اندرویدی قدیمی دارید که گوشه‌ای خاک می‌خوره، پروژه
Linux-Android
دقیقاً همون چیزیه که بهش نیاز دارید! این ابزار که به تازگی در گیت‌هاب ترند شده، یک اسکریپت ساده و قدرتمند است که بدون نیاز به روت (Root)، گوشی اندرویدی شما رو از طریق اپلیکیشن Termux به یک دسکتاپ کامل لینوکس یا سرور خانه هوشمند تبدیل می‌کنه.
🔥
امکانات و کاربردهای بی‌نظیر این پروژه:
1️⃣
نصب خودکار و بدون دردسر:
بدون نیاز به دانش فنی پیچیده، فقط با اجرای یک اسکریپت، لینوکس با محیط دسکتاپ دلخواه شما (مثل XFCE، KDE، MATE یا LXQt) نصب میشه.
2️⃣
تبدیل به سرور خانه هوشمند (Home Assistant):
می‌تونید گوشیتون رو به یک هاب مرکزی (Home Assistant Hub) تبدیل کنید تا وسایل هوشمند مثل لامپ‌ها و پریزهای وای‌فای رو کنترل کنه.
3️⃣
پشتیبانی از شتاب‌دهنده گرافیکی (GPU Acceleration):
با استفاده از درایورهای Turnip، گوشی‌های دارای پردازنده اسنپدراگون گرافیک بسیار روانی روی دسکتاپ لینوکس به شما میدن.
4️⃣
نصب ابزارهای کاربردی:
ابزارهایی مثل مرورگر دسکتاپ (Firefox)، پخش‌کننده ویدیو (VLC)، سرور SSH و حتی اجرای برنامه‌های ویندوزی با استفاده از Wine (به‌صورت اختیاری) قابل نصب هستن.
5️⃣
کاملاً ایمن و بدون نیاز به کلود:
تمام پردازش‌ها روی گوشی انجام میشه و نیازی به سرور ابری ندارید.
⚡️
این پروژه برای آموزش لینوکس، توسعه با پایتون و ساخت سرورهای خانگی فوق‌العاده است.
🔗
لینک مخزن گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#Linux
#Android
#Termux
#HomeAssistant
#OpenSource
#Github
#Python
#Tools
#TechHack</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/6542" target="_blank">📅 01:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚀
آموزش اجرای MiMo Code یک AI و ابزار کد نویسی کاملا رایگان و بی محدودیت
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
3) نصب MiMo Code
curl -fsSL https://mimo.xiaomi.com/install | bash
4) اجرای MiMo Code
در یک پوشه اجرا کنید
مثال :
cd /storage/emulated/0/Download
سپس :
mimo
4️⃣
اگر خواستی بعداً دوباره وارد Ubuntu شوی
proot-distro login ubuntu
5️⃣
اگر MiMo Code را نصب کرده‌ای و فقط می‌خواهی اجراش کنی ، قبلش وارد پوشت شو
mimo
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/6541" target="_blank">📅 23:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-_KdngRyILWwj54N6O38eckF-v7JJBJKidfT0AQe0mUA4M7z6-25tS5h7sapWkx0NP6sPqvfOwE_5qx6hJk0Zy1XYFXLSqiqkw5ZsIFB1Z2YLg7bs2tHrth-R-BU8HSMQGUZ9S5tH21WdDDbu237uUkEReW0Fq_wrpRZi2WS61OMWBm_Z9XxEIGqXL-tKJe5GGDnbtFrmtiebgQ6CKlSrOYMAiakfMbyojg96rTwvMZP6pmfvlEH27n5OqkK9WqEyky_YNZ2unaqmXBcsteLwdFtvMjIXlRXj3o7grcIpOXIPJ1hs7dth89V24B7TrCeq9ecO8f93XCmePU_X6v-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
کتابخونه‌ای به وسعت ۱۱ هزار کتاب!  هوشمندانه جستجو کن و دنیای جدیدی از کتاب‌ها رو کشف کن.
✨
قابلیت‌ها:
•
📖
دسترسی به ۱۱ هزار کتاب با رتبه‌بندی و توصیه‌ها
•
🧠
جستجوی معنایی: «کتابی برای توسعه فردی» یا «متا فیزیک»
•
🔄
مشاهده نسخه‌های مشابه برای هر کتاب
•
🌟
مجموعه‌های پیشنهادی از افراد مشهور
•
📊
جمع‌آوری داده‌ها از کتابخانه‌ها، شبکه‌های اجتماعی و رسانه‌ها
🌐
Site
#کتاب
#کتابخوانی
#معرفی_کتاب
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/6540" target="_blank">📅 21:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6536">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LI17QfOYp-qt0jjvMqolrTttltDgs-tDiZ8EayyN0BjpIyZe3nnpD3JcEIn32nP3NcHte7gsx2vIUOLmITwcUkSG8K1c4Ci2KywLeQ0fyjzdpS2XI44XbztbNN2HK_ZzbsY1Afp5oQlJDeKg4x0eQqrpHWlUMqWtA1xY9mdKRt615ZUaIgBQ4oZEORqZZt_h3X22eInm2MXIHklwTnKkhWebe_HlRUdNis_v7D5q1xV1DW5mjBZ9eF7Q5hp0Xrevn9J17kZcTYMAb3UabUuh7wzljlvVQ-XbcYHrgTxULPbWvNuGIUL6VYO1Ml4umJseBaTLmiacnf09LxGpXUtiaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nWM5WuJJsWeXHUfOPqDwUj7yXIUnKTtB1T8xDslJuhBcqMWI3RmFTQsXc7YbOZzFzwbABaGbSlo-Asjr3_kMxvfFXb4zXDx9Pkqnr0XLXCPGCSqkXwL5oWqE-IoLsYuvyCLxW3Q2M09CBupgamBWY56b1ouYGHMa4oRJj1Gnvd6FJEpsMfLoh1rX7EuBIIQlO5NufCcAn-eW4CDbUBamJWrNd2kGTLoBMLGHITwdVz768iUXtmuwn5UamzDWNhAhT8m3EeWdnJaw4I7COMvWZS0I5atVW1Bd_Pn6EO41zJzHbQgqwL3GyQU58ZFl0KdQ69xzVqlyMbwbWUYuztPG6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OtHrQRRn92QFT-BIzCGpBl4t28ENKBzYw0l9h8TstoiC_BdK-7z7M0xTexA9FtmcXLxkwYoiBlGh7sE59Nk3CI5gragT6y_zgdPqsC1kF8TSbVfg1fbHrgxgtmYAry4edJWhWLgi8fn7wQov1oNeBOPhdULEg-6yzdJXW3EKHeiXjaS5kSUHQqy0d2pNbHXNk9TT8awqk1cS7TfQwF3lu6FANqsxjugpLrOGZSpaeA96yBKp0ZIZAluBpCMuNGBza5AY3GgiYlHJwuK47pHX_fyRSAo_QOp3G_WY8MjtwqmjtcglxMJTMdBqndRnoq9BvbvG_AfV3Dpgte67ggsofQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mayhWx4XnfwcNCYLplqIB-Yxc-oesr79Vh3_--b7eEmsDN8iwcQd6Wy3SvyOe0f8KFwtD1bM4hVQFxjuM5L3SKGR32OgGb5EDThIl8Q-QpfmscLe-rsTjFA8VGvUWjjE-LpSdsEIn4f_NUbk1xbL3hVv4XzCt-WCH2dZCxy3EntwPJoqJTxiWp8iJ1jlig5HKFoTg6x292eTnBQq5ir2rxO2gZsxbhiUD7JU73JT002sM8-PDUIU8uYi7I-dQor5bXUjnrs8TyHUSAtq8YC9Oz9K_AO41jxdY3JGaLqKr4j1LjoPR9K9mCfyKu1iQaEVZEgvNezaf3xwQn39rcXJqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🍿
نتفلیکس خود را بسازید — یک برنامه رایگان و متن‌باز برای تماشای فیلم‌ها، سریال‌ها و انیمه بدون تبلیغات مزاحم پیدا کردیم.
🔹
بسیار سریع‌تر از اکثر سرویس‌های مرورگر کار می‌کند.
🔹
امکان دانلود محتوا مستقیماً روی دستگاه را فراهم می‌کند.
🔹
از زیرنویس‌های فارسی پشتیبانی می‌کند.
🔹
بر اساس علایق شما توصیه‌ها و مجموعه‌هایی را ایجاد می‌کند.
🔹
برای راه‌اندازی فقط به یک توکن رایگان
TMDB
نیاز دارید که در چند دقیقه تهیه می‌شود.
🌐
GitHub
#OpenSource
#Streaming
#Entertainment
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/6536" target="_blank">📅 20:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">worker.js</div>
  <div class="tg-doc-extra">23.5 KB</div>
</div>
<a href="https://t.me/ArchiveTell/6535" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سورس کد ربات تلگرامی برای چت با هوش مصنوعی بر بستر کلودفلر
🌐
ویژگی‌ها:
- گفتگو با مدل‌های GLM 5.2، Kimi k2.7، Gemma 4، GPT 4 و Llama
💬
- تولید تصویر با مدل‌های Lucid origin و Flux 2
🖼️
- تبدیل صدا و موزیک به متن با مدل whisper-large-v3-turbo
🎤
راهنمای اجرای این سورس در بخش کامنت های این پست ارائه شده است
👇
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/ArchiveTell/6535" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚀
معرفی Save to Yaps؛ ابزاری برای ذخیره هوشمند و خصوصی مطالب وب!
🌐
✨
اگر از آن دسته افرادی هستید که همیشه ده‌ها تب (Tab) باز در مرورگر خود دارید، یا لینک‌های مهم را برای خود ایمیل می‌کنید و دیگر هرگز سراغشان نمی‌روید، افزونه
Save to Yaps
دقیقاً همان راهکاری است که نیاز دارید!
این افزونه یک "Web Clipper" فوق‌العاده است که هر صفحه وب را به یک یادداشت Markdown تمیز و خصوصی در کامپیوتر شخصی شما تبدیل می‌کند.
🔥
چرا Save to Yaps متفاوت است؟
*
تبدیل هوشمند محتوا:
مقالات را از شر تبلیغات، منوها، بنرها و پاپ‌آپ‌ها پاکسازی کرده و فقط متن اصلی را به عنوان یک یادداشت تمیز ذخیره می‌کند.
*
ذخیره سریع تصاویر:
با قابلیت Hover-to-save (نگه داشتن موس روی تصویر)، می‌توانید عکس‌ها را به سادگی به یادداشت‌های خود اضافه کنید.
*
حریم خصوصی مطلق (Private by Design):
برخلاف سرویس‌هایی مثل Pocket یا Evernote، در این ابزار هیچ اطلاعاتی به سرورهای ابری ارسال نمی‌شود. همه چیز به صورت محلی (Local) روی کامپیوتر شما ذخیره می‌شود.
*
کارکرد آفلاین:
حتی زمانی که به اینترنت دسترسی ندارید، می‌توانید یادداشت‌های خود را ذخیره و مدیریت کنید.
*
سازگاری:
روی تمام مرورگرهای مبتنی بر کرومیوم از جمله کروم، اج، بریو و آرک قابل نصب است.
💡
نحوه استفاده:
برای شروع، کافی است اپلیکیشن دسکتاپ رایگان Yaps (برای مک یا ویندوز) را از
اینجا
دریافت کنید، افزونه را روی مرورگر نصب کرده و با یک کلیک، مطالب مهم را به "Second Brain" یا همان پایگاه دانش شخصی خود منتقل کنید.
🔵
@ArchiveTell
| Bachelor
⚡️
#Yaps
#WebClipper
#Privacy
#Productivity
#Markdown
#KnowledgeManagement
#TechTools</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/6534" target="_blank">📅 17:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6AlyIMgUq8MFKyhylutczxufZFhzsD_Whhz5yq8ne-5hJvZrUXIKnUwLiEJW6Jj3YOeH1oDcKhm8i_iKVDRFGy1rnvtoIcskRVgHmJzPNZVgzlG034QNIWfkYWqihkAGgY72mc6rgbAjOdoE2I9i8udcM2WAeikF-jpwBEu6nUGPr2TeYD24AbC7tan_8AjxClMVYKUPVfyj_3exH9u33MJ4OGc6HcuQMPSb6ay1dvCo0FZ9bbn0VKI0Ww9tsRsPhik5DmNn_jB3Cd_1_XxWOsHyKbP8M7iEiElueir36DvxUUN8vl7HUNpIWx7yFJw1O6RJhIMn5S5GTPfsQzeeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش در سطح MIT و هاروارد رو رایگان تجربه کن!
🎓
بیش از ۱۷۰۰ دوره از بهترین دانشگاه‌های جهان حالا در دسترس شماست.
✨
قابلیت‌ها:
•
🔹
دسترسی رایگان به دوره‌های برتر جهانی
•
📚
شامل برنامه‌نویسی، ریاضیات، طراحی، کسب‌وکار، فلسفه و علوم دیگر
•
📹
محتوای کامل: ویدئو، جزوه، تمرین و امتحان
•
💡
مناسب برای یادگیری از صفر تا پیشرفته
•
🔸
یکی از بزرگترین آرشیوهای باز آموزشی
🌐
Site
#Education
#FreeCourses
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/6533" target="_blank">📅 16:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ij10RZDLHUrkqMdNJPHcUxueRKLyy3PeBtnEmIqeMJTMuAtNKTuAu64m7afFcVg9tbFm8Aqrr7vVede-yzSfCdASRSLMVIPiNeMcmQfyKS6meSwMqtYr5xz3bx59CwWWbmEyAPrRbj_lg-VrbeYD1rqnp27btk57Mub7aYLvDYOVIz4bR7iaf47kVLzDgcJUhTOJFQ7xdqOT0A_HhA5TjcgLFZOC9wpWnnuvRx2VSAu4-X33mHSt-CIIrbqjt4Pr7cdHg4KNyk6mY_hByO75DqaKsht1GIDI3KxMe2rN4buCIooe9mR9QfmfEbQSv2aPsmdZGSGtQjc2fPjBwPIRrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FCThrpZEDuBXS81y_Exzmil4y8VIvuhZYR8EzEWngkFkR5m-WMuWR7sFC8TWlvCqkY03C-PcvieGAGezVD6-98MHtPB_bwPUaUClwlnviOhsJbR3sxt-JeemorfwZpTgG-_pZQpCp0-_7WOhMA9kd7o67UQXX-w8gIoungMj2gVSN8BCLzX74dDKQM2Im9UCvzcVt3BY5vuYQOla-rVi3neMsI6-1LYmnVOhNO5cpVSoP1YW_uGbB7bSF-iZ0W1DqMmtugMP-w6Rnm6FNdsBbo-FS6Te7LVITJ0wO8fVHf458Du0joqnZKFn7ugBziLT0dgVRCjGRQ68-33i-VePcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eVJHSj7YpIJvmi9rjhbWTd3gA_04ZnA2-fHRziqXSAnRYsajcA2quejwjf_dlKccBEX8LnU2f1CxHihTMfZsgk0tNbLO7kK9vG4gjJnwyJPg2o-5DXC7McU89BHWF9J2QMaTIC11_8AxdkOuvVQ1qVaHMDPXvwFnuEIDRqd0YlDHalObGw4RFs4ctOLvDA7-oq2Sj_vrm3i1NnrV0yTs2qUNmSQGK9DgT4seZJPnvYgW_NE-dFtI0nFD-a5bimdFBOE5cJ96oDmlYxvSk2XJaFYSHRW-cTtlukDf7FFu53RJGI8ku7_HkGeQigw7UPIycI7V4D-Qrz6y-LTpKf16Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hsRlKDKvD0nnbFEtbwoXMh-blDCBQVLXHS9t1LM4-MEA7xBeagmBcxouWxxzjJKVvtK6ffaGP6Bat-1pcGbkyQlHmgI0ZX8QVgVfReMH8DHI6yKoMfQKuyjr_CGfjKZYH9JRKoSw8QuP_FeF-HMCBYdYbkvmoKoPE8tMnnI8ohIG9MZT8r4yl_BO4HeKVOHqBxnwr_4W05F3Ov6CzkTrKf873VyYhAY5KWaEgZVDRBa7ZpXx_UlMjFTxL-27kZEddJDHgrs7Ko_AdLvglzI7Q4_S11N-XA9LUrdPk07hgix59yV_7pryGWho1mPLoJS9adiIvi_CiGrO2U-Q5rvRPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qEjQFGK0cCg-ypZn4roA3-ELlewthHd4aWi0KNQVlyIpb3YGmZyqSUTqNcsprDD8ApQtMCgb4cvueehkeaIo24TrmbH1eJluTHvgYAKJX8dFo_iNlkLG7v356UgOR68QvWVIRiOJDTIRaq2u-2AnUOwV2JrLOVt-xWELX9bbVqzzRvpratGHKNUMjblIg31v50AG9i1WO7nkWEi6pafnJkDiCeJZ14XX_FCuCKwTFaKOsc0JJKMRu0zJCGMoFTRAp6OWVmkUyeDaR9JWBTGRCQ2TyMBsZyKzyeDrkZVqiQyrnLtheVg81w0hdBnvJdp4lghta31mGwLZ-z63cEaC1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cq2JF3S-Gj09qyopPrSOdmeTn8hm10YnJG8aPDbvBOmSlzcWo_cSQH0mZwBdAsvccRWNlTW_EZU3hktxhSC-al1HwJGuaPaPTtoHx01prpQcd9vgbw1wEK8NMvhzJdtQ7WLiaTriUb3K5c1LeZKa6tUFo3frLLV3E3aNT3ikFyJ3q-xE31mQvLJDpFFnEO2cWAM2q3UaZdH6Gkbd2NWdZhqCgcaiXzpxuWH_H4cGZu4-PxXdD5MetNjaigOKWK6w77rsm5e8O7OWc23-XsfmmvRPrt0PxijX-dGDzt8GrIGIheSb3Z86y-8TBF_xwQ3Poy-pcTRmAT-u818zOR2NGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر منتشر شده از بازی GTA VI</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6527" target="_blank">📅 14:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6526">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dx3IxaHPShaPVF2YgiKkdT-OgKErA92KgLN3mpvPtAwsGGgaACzd_S9HaobgY_hlRLl3ifjUIjZvALd1Vsh5o6RVExEGcyr8Wgj36WFEKZA0qWcizFcdRIiKfgdvxCa7hvE1ll4amNjdrZ5bbrT-zDU3VmrHFqNFGTsGmt4PxiowghFJC4NiXVv2lebok5tjOkUl5PLfnvq1nZPMDjwYeevf-cxr3zI6PfBkToWLCOVXLfnINvCS-iEsgsVqDD4ZqmLLe0ZAulkoXf9NvphBXEOscqU0zmz0_F8pHM9XV261BodQBDlrOmvapTvFwEtC2obuLDXsM_N76KXvWEuy-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر تورنتی که بخوای رو پیدا کن!  با "EXT Torrents"، یک موتور جستجوی قدرتمند و رایگان، به دنیایی از محتوا دسترسی پیدا کنید.
✨
قابلیت‌ها:
•
🔹
آرشیو عظیمی از فیلم، سریال، انیمه، موسیقی، بازی و نرم‌افزار
•
⚡
جستجوی سریع و دقیق با کلمات کلیدی
•
📂
مرور دسته‌بندی شده و رتبه‌بندی محبوب
•
🔗
پشتیبانی از کپی مستقیم مگنت و دانلود فایل تورنت
•
🆓
رابط کاربری ساده و بدون نیاز به ثبت‌نام
🌐
Site
#Torrent
#SearchEngine
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6526" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6525">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚀
معرفی winpodx؛ اجرای اپلیکیشن‌های ویندوز در کانتینرهای لینوکس!
🐧
✨
اگر نیاز دارید برنامه‌های ویندوزی را در محیط لینوکس اجرا کنید اما نمی‌خواهید درگیر سنگینی و کندی ماشین‌های مجازی (VM) شوید،
winpodx
راه‌حل جایگزین و هوشمندانه شماست. این ابزار به شما اجازه می‌دهد برنامه‌های ویندوزی را درون کانتینرهای ایزوله در لینوکس اجرا کنید.
🔥
ویژگی‌های کلیدی:
*
بدون نیاز به ماشین مجازی:
اجرای مستقیم و ایزوله در کانتینر با عملکرد بسیار بالاتر.
*
پشتیبانی منعطف:
اجرای نسخه‌های مختلف ویندوز در محیط کانتینری.
*
توسعه‌یافته با Python:
ابزاری سبک و قابل سفارشی‌سازی برای سناریوهای مختلف.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#winpodx
#Linux
#Windows
#Docker
#Python
#Containers
#DevOps
#OpenSource</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6525" target="_blank">📅 11:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚀
معرفی AI Website Cloner Template
این پروژه یک قالب حرفه‌ای برای
تبدیل هر وب‌سایتی به کد مدرن (Next.js 16 + React 19 + Tailwind)
با کمک ایجنت‌های هوش مصنوعی است.
قابلیت‌ها:
*
مهندسی معکوس هوشمند:
تحلیل سایت، استخراج توکن‌های طراحی (رنگ، فونت) و ساخت کامپوننت‌های دقیق.
*
سازگاری بالا:
پشتیبانی از ایجنت‌های معروف مثل Claude Code، Cursor، Windsurf و Gemini.
*
تکنولوژی روز:
خروجی تمیز با Tailwind CSS v4 و استانداردهای strict TypeScript.
کاربرد:
بازسازی پروژه‌های قدیمی خود یا یادگیری نحوه ساخت کامپوننت‌های پیچیده وب‌سایت‌های حرفه‌ای.
🔗
مشاهده در گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6524" target="_blank">📅 07:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡 یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده. این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway  را فراهم می‌کند. از طریق خود ربات می‌توانید:
✅
پنل موردنظر…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6523" target="_blank">📅 00:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=UlMypHWOAA0zau4GyemyMhijybnpcpX1qqnTIuol6xejL5Tb6QsXaYkkJsT-ddmrmoJXbc_0QPnrQUMFycHnuP7JCZGmq_dviZ5k_BSqrqUWEFNbbweJeBJACTcFI7sRwg2V1BMhGQo4WI5L-C8ihE874Kv3IsGFSoS0gPfEje2lbuIfAMNZY8fxV0XHCsjzVTfzDiRbghbRr74IkFQdLRZnGOsRlXGHL_IcWyI1WRbw2sDhiohhpldZzKAPUC8xiDwx6GmoINxgteGoaeTc2IUnIqHFO_s7W_P6Lk8q92rrdaO9uYx8vcFQpzcp5pkHg90MLKhHtKYrwoAXsVpLkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fcd8ab3fc.mp4?token=UlMypHWOAA0zau4GyemyMhijybnpcpX1qqnTIuol6xejL5Tb6QsXaYkkJsT-ddmrmoJXbc_0QPnrQUMFycHnuP7JCZGmq_dviZ5k_BSqrqUWEFNbbweJeBJACTcFI7sRwg2V1BMhGQo4WI5L-C8ihE874Kv3IsGFSoS0gPfEje2lbuIfAMNZY8fxV0XHCsjzVTfzDiRbghbRr74IkFQdLRZnGOsRlXGHL_IcWyI1WRbw2sDhiohhpldZzKAPUC8xiDwx6GmoINxgteGoaeTc2IUnIqHFO_s7W_P6Lk8q92rrdaO9uYx8vcFQpzcp5pkHg90MLKhHtKYrwoAXsVpLkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش ثبت دامنه برای رندر
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6522" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚀
معرفی پروژه 𝗥𝗘𝗡
یک ربات ساخت خودکار پنل است که برای ساده‌تر کردن فرآیند ساخت و مدیریت پنل طراحی شده.
این ربات با استفاده از 𝗔𝗣𝗜 𝗧𝗼𝗸𝗲𝗻، امکان ساخت خودکار پنل روی سرویس‌های:
☁️
Render,
🚀
Railway
را فراهم می‌کند.
از طریق خود ربات می‌توانید:
✅
پنل موردنظر خود را بسازید
✅
مصرف و وضعیت منابع را مشاهده کنید
✅
دامنه شخصی خود را برای پروژه متصل کنید
✅
آی‌پی تمیز را مستقیماً از طریق ربات دریافت کنید
هدف 𝗥𝗘𝗡 ایجاد یک روند ساده‌تر و خودکار برای مدیریت پروژه‌ها و سرویس‌هاست.
🤖
ربات
💻
سورس پروژه
━━━━━━━━━━━━━━
👨‍💻
توسعه داده شده توسط 𝗔𝘀𝘀𝗔
دوستان اضافه کنم اگر رندر شما ساسپند شد اکانت رو حذف کنید و دوباره با همون ایمیل یا گیت هابی که داشتین ثبت نام کنین مصرفتون ریست میشه
برای حمایت از پروژه star بدین
❤️
(در گیتهاب ترجیحا
😂
)
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6521" target="_blank">📅 23:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AI5R6XYaBF5_s-lMrW-q4KWkaxFdSbebWO22Na_B3RR6Re-EM4MOtzihmXFNHMZtfH1zeZSBf1p2GJs5yvDRnqT3jzvcm_IKjafU1oALLELVzMuy3CAIC_v3N9nZS_KZ5FFl_gx-lMOqhV4SCX7SG1VdhEqgs-G8w4i3MvEp3R0pFLgV6lV7m6xGmyHcWhtqlfU36fktSu23lxsNdNanKtjcLCo8PjgwFO4v8Eo4TTCd0d8djCLF4dd8UFciLX42cbizgCW1ZlvEQUWAD_GqyVFcmOrfD-ojJGgGZWeVNac4U2NwrZUctN-VA5wBjYcBn2TKbAsONzE2aO6eZnd33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی shadPS4؛ سریع‌ترین شبیه‌ساز کنسول پلی‌استیشن ۴ برای کامپیوتر!
🎮
✨
اگر به دنبال اجرای بازی‌های PS4 روی سیستم خود هستید، پروژه
shadPS4
یکی از فعال‌ترین و سریع‌ترین پروژه‌های متن‌باز (Open-Source) در دنیای شبیه‌سازی است که با زبان C++ نوشته شده و با سرعت خیره‌کننده‌ای در حال پیشرفت است.
🔥
چرا shadPS4 در حال حاضر ترند شده است؟
1️⃣
توسعه روزانه:
این شبیه‌ساز تقریباً هر روز آپدیت می‌شود و بیلد‌های جدیدی برای سازگاری با بازی‌های بیشتر منتشر می‌کند.
2️⃣
پشتیبانی چندپلتفرمی:
به راحتی روی
ویندوز
،
لینوکس
و
macOS
اجرا می‌شود.
3️⃣
رشد سریع:
در تاریخ اخیر شبیه‌سازهای کنسول، shadPS4 سریع‌ترین روند بلوغ و افزایش سازگاری با بازی‌های بزرگ (Major Titles) را داشته است.
4️⃣
جامعه کاربری فعال:
با بیش از ۳۱ هزار ستاره در گیت‌هاب، این پروژه به یکی از محبوب‌ترین ابزارهای گیمینگ در اکوسیستم متن‌باز تبدیل شده است.
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#PS4
#Emulator
#Gaming
#OpenSource
#Github
#Cplusplus
#RetroGaming</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/6518" target="_blank">📅 21:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚀
معرفی OpenSERP؛ دسترسی رایگان به API موتورهای جستجو (جایگزین SerpAPI)!
🌐
✨
اگه برای پروژه‌های هوش مصنوعی، سئو (SEO) یا اتوماسیون خودتون به دیتای موتورهای جستجو نیاز دارید و نمی‌خواید هزینه‌های سنگین برای خرید API بپردازید، ابزار
OpenSERP
دقیقاً همون چیزیه که دنبالشید! این پروژه متن‌باز (Open-Source) دسترسی کاملاً رایگان به نتایج Google, Yandex, Bing, Baidu, DuckDuckGo و Ecosia رو از طریق API فراهم می‌کنه.
🔥
چرا این ابزار فوق‌العاده است؟
1️⃣
بهترین جایگزین سلف‌هاست:
یک جایگزین رایگان و قدرتمند (Self-Hosted) برای سرویس‌های پولی و معروفی مثل SerpAPI, DataForSEO و Tavily.
2️⃣
خروجی مارک‌داون (Markdown):
قابلیت استخراج دیتا از سایت‌ها و نمایش نتایج جستجو به فرمت Markdown (که برای پروژه‌های RAG، ایجنت‌های هوش مصنوعی و LLMها یک ویژگی طلایی محسوب می‌شه).
3️⃣
جستجوی ترکیبی (Megasearch):
این قابلیت به شما اجازه می‌ده تا یک کوئری رو به‌طور همزمان در تمام موتورهای جستجو سرچ کنید و نتایج تجمیع‌شده رو تحویل بگیرید.
4️⃣
کاربردی برای همه:
ابزاری بی‌نظیر برای متخصصین سئو، توسعه‌دهندگان، برنامه‌نویسان وب‌اسکریپینگ و فعالان حوزه هوش مصنوعی.
⚙️
این ابزار رو هم می‌تونید خودتون هاست کنید و هم از نسخه تحت وب و آماده‌ی اون استفاده کنید.
🔗
لینک مخزن گیت‌هاب
🔗
نسخه آماده و تحت وب
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenSERP
#API
#SEO
#WebScraping
#LLM
#RAG
#OpenSource
#Github
#Tools</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6516" target="_blank">📅 20:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6515">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚀
آموزش دریافت یک ماه اشتراک رایگان Duolingo Super!
🦉
✨
اگه از برنامه دولینگو برای یادگیری زبان استفاده می‌کنید، الان می‌تونید با یه ترفند خیلی ساده و جذاب، یک ماه اشتراک پریمیوم (Super) این برنامه رو کاملاً رایگان دریافت کنید و از شر تبلیغات و محدودیت‌های جون (Heart) خلاص بشید!
🔥
مراحل دریافت اشتراک:
1️⃣
نصب اپلیکیشن:
ابتدا
اپلیکیشن Webtoon
را دانلود کرده و یک اکانت جدید در آن بسازید.
2️⃣
جستجو:
در نوار جستجوی برنامه، عبارت
Duo Leveling
را سرچ کنید (این کمیک مشترک دولینگو و وبتون است).
3️⃣
اسکرول کردن:
سه قسمت (اپیزود) از این کمیک را باز کنید. (اصلاً نیازی به خواندن نیست، فقط کافیه صفحات را تا انتها به پایین اسکرول کنید!).
4️⃣
دریافت کد:
بلافاصله بعد از انجام این کار، یک کد فعال‌سازی رایگان Duolingo Super به شما داده می‌شود.
👏
5️⃣
فعال‌سازی:
حالا وارد لینک زیر بشید، وارد اکانت دولینگوی خودتون بشید و کد را وارد (Redeem) کنید:
🔗
ورود
🎉
تبریک! اشتراک یک‌ماهه شما فعال شد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Duolingo
#DuolingoSuper
#Webtoon
#FreeAccount
#LanguageLearning
#Tricks
#Education</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6515" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚀
تبدیل عکس شما به مینی‌فیگور واقعی لگو (LEGO) با هوش مصنوعی!
🧱
✨
دوست دارید بدانید اگر یک کاراکتر لگو بودید چه شکلی می‌شدید؟ با استفاده از تولیدکننده‌های تصویر هوش مصنوعی و یک پرامپت (دستور) مهندسی‌شده، می‌توانید هر عکسی را به یک رندر سه‌بعدی و فوق‌العاده جذاب از مینی‌فیگور لگو تبدیل کنید!
🔥
ویژگی‌های این استایل جذاب:
1️⃣
حفظ هویت و جزئیات:
لباس‌ها، مدل مو، رنگ مو، حالت چهره و حتی اکسسوری‌ها کاملاً شبیه عکس اصلی شما بازسازی می‌شوند.
2️⃣
رندر فوق‌واقع‌گرایانه (Photorealistic):
اعمال بافت پلاستیک براق لگو، درزهای قالب‌گیری و نورپردازی استودیویی که باعث می‌شود تصویر کاملاً شبیه یک اسباب‌بازی واقعی به نظر برسد.
3️⃣
رعایت دقیق تناسبات:
سر استوانه‌ای، دست‌های گیره‌ای کلاسیک و بدن بلوکی شکلِ استاندارد لگو.
👇
پرامپت (دستور) برای استفاده در Midjourney یا DALL-E 3:
کافی است عکس خود را در هوش مصنوعی آپلود کنید و دستور زیر را به آن بدهید:
>
Turn the person in the uploaded image into a realistic LEGO minifigure, preserving their individuality, clothing, hairstyle, hair color, facial expression, and accessories as much as possible. The character must match the proportions of a LEGO minifigure: a cylindrical head, simple facial features, a blocky torso with printed clothing details, standard LEGO arms and hands, and a molded plastic hairpiece. Use realistic LEGO plastic texture with a glossy sheen, molded seams, and studio lighting. Plain white background, full body photorealistic 3D render from head to toe.
💡
نکته کاربردی:
این ترفند برای ساخت عکس پروفایل‌های بامزه، آواتارهای تیمی و پست‌های خلاقانه شبکه‌های اجتماعی بی‌نظیر است!
🔵
@ArchiveTell
| Bachelor
⚡️
#LEGO
#AI
#Midjourney
#DALLE3
#Prompt
#PromptEngineering
#3DRender
#Avatar</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/6514" target="_blank">📅 18:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjMMONq8nk9hkV60hlT4xl8JYbju_WIPT6XKTjkTaYKW3B8l_lIupbsCUgUjTbRn5Qyr2GYoyJDMC7M4SnfTnSfmiGAls24rynTDtvpF5N7jSwDDdoWcf2o2Yw6Ike4X9AVzrMZgzBq7zW-0pSIP4OXie6oLkrCYCg7Z38ZkyKwJniRoDJgE_aSGYK9cc9Ue8dkbxNpdSRGtRKZ6WfUZKMUSzJeSr31gZiyKOYuZJqYos99Z6VH8iaHl4bAg0X0qStHuXr94KWvVijmyRUUCfR2N4WgFJSAqoahJ1hPvu3BlrvmrSYkyGnWnJyVMdkr21RKryzcni7Na6ubSEeVXeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل‌های هوش مصنوعی پریمیوم با مرورگر tabbit
🤯
ChatGPT 5.5 Pro
Gemini 3.5 Flash
Claude Opus 4.8
و بیشتر
در دسترس برای
macOS
و
ویندوز
مرورگر را نصب کنید و استفاده از جدیدترین مدل‌های هوش مصنوعی را به صورت رایگان شروع کنید!
🌐
Site
#Ai
#ChatGPT
#Gemini
#Claude
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/6513" target="_blank">📅 17:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8UxuS0MHr5rVLCCZsyFfaTdMLjOIuvxSguWr2xfvn3i5OC6QmRVhQ1YHRgOYP0b1ufV5GavzUxERa-9xKLwV9AWlPfANTCrhC0kQ_f1sd6a4EnrOjPQ-7q8yaZfkAI9NFDU_MieuZ9Zds1j2Tt-l43UWxkbE7WtmDODvLsjjxBlBt3uPLfJYdCtMbaK3QICfsG0UhHlMiFerZasRMs0WzT5Mb2EYneID1avlNPyXtfSMn2HzX98JlNF27xGYj5IJEuMdBgxVDNfFqX5FaC5Q2HzgjG81--CZQwhUCfxWIgpgBxS3kAx6bmyjeS73RFlY8V0O8ciQmP36szbxTWMgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چینی‌ها مدل Qwythos-9B-Claude-Mythos-5 را معرفی کردند که بر پایه Qwen3.5-9B است و قابلیت پردازش ۱ میلیون توکن را دارد!
🤯
✨
قابلیت‌ها:
•
🧠
تنظیم دقیق بر اساس ترکیبی از Claude Mythos و Claude Fable.
•
📚
پنجره متنی گسترده تا ۱,۰۰۰,۰۰۰ توکن!
•
🌐
انتشار کاملاً متن‌باز
•
✍️
همه‌کاره برای کار با متن، کد و اسناد طولانی.
🌐
Site
#OpenSource
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/6512" target="_blank">📅 17:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyybjzeZhkh7poUCfgQIrTdoW85zPUSHiq1ovvBGUXrF5X5XaLszfiT4i8q7tZ5oHZnlALIq29MEfmVA-buh_RlqhJ3hfvc0JsO4cjs8fx6SGnIYKtX6j03BlhwVJ9bSyEmXQhHlQfaixhaw5lfA1PfEp2xo4WbVK7fJw1T3ntGTOXKuJZXIuBXfLi3o3Y-zMunUsCFRVmi9LbbX1v-rhT-_OIrVjB4UwZRW7v4ckjsKxLDwLbl6M9jmncBh9KKVr7GQO36MYsuTFVHfj14jy01dBcxCwo95s-1FBrkSwTtPU_Gq7wmhLbIpbzKLvKCk1XinYb8mKWJ-eT_D27T-rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
Consensus — جستجو در مقالات علمی
موتور جستجویی برای ۲۰۰ میلیون مقاله علمی. سوال خود را وارد می‌کنید و مجموعه‌ای از تحقیقات مرتبط و خلاصه نتایج آن‌ها را دریافت می‌کنید.
🌐
Site
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/ArchiveTell/6511" target="_blank">📅 12:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=S2_vLBGkVuaPKme-gKeKxQiZ4QX0SxrUzVJqVqnQnoeEx3kveRN0BRqDJLizoxLGgRftgVI4e6U3GomsQ09IHrIc1eeAcPrUJwEvW709QSF_J2jMcHRFUiCukYy8bdN-I4xbv1zFNxplc3s72iW7QAdm5K_pcYr5AqoA5CBO8A57XeBCSf82qduXGNVcxldkeU2DO2k49MjH7WQDFlsxUoaClenbQZg4Tg6HxzOkHW79ryCYaDAR6N3lTjvtcDKmw3zPkp-iclQpGdOIOIo98Y_6EDAY2hAzAbWGHu6GfGeuQt8vxEWvNaChXiHTzuGlLEjxmg2DynIl_NZPd8epoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e892ec1f9d.mp4?token=S2_vLBGkVuaPKme-gKeKxQiZ4QX0SxrUzVJqVqnQnoeEx3kveRN0BRqDJLizoxLGgRftgVI4e6U3GomsQ09IHrIc1eeAcPrUJwEvW709QSF_J2jMcHRFUiCukYy8bdN-I4xbv1zFNxplc3s72iW7QAdm5K_pcYr5AqoA5CBO8A57XeBCSf82qduXGNVcxldkeU2DO2k49MjH7WQDFlsxUoaClenbQZg4Tg6HxzOkHW79ryCYaDAR6N3lTjvtcDKmw3zPkp-iclQpGdOIOIo98Y_6EDAY2hAzAbWGHu6GfGeuQt8vxEWvNaChXiHTzuGlLEjxmg2DynIl_NZPd8epoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗿
افزونه Caveman پرامپت‌ها و پاسخ‌های هوش مصنوعی را فشرده می‌کند
به‌طور خودکار کلمات اضافی را از درخواست‌ها و پاسخ‌ها حذف می‌کند و در عین حال معنی را حفظ می‌کند. با ChatGPT، Claude و Gemini کار می‌کند.
نویسنده ادعا می‌کند که این افزونه می‌تواند مصرف توکن‌ها را تا ۷۵٪ کاهش دهد. ایده ساده است: کلمات کمتر یعنی هزینه کمتر، و معنی باقی می‌ماند.
🌐
افزونه
#Caveman
#ChatGPT
#Gemini
#Claude
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/6510" target="_blank">📅 11:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚀
معرفی Firecrawl؛ قدرتمندترین API برای جستجو، استخراج و تعامل با وب در مقیاس بزرگ!
🔥
✨
اگه توسعه‌دهنده، محقق هوش مصنوعی یا دیتا ساینتیست هستید و نیاز دارید اطلاعات سایت‌ها (حتی سایت‌های پیچیده و مبتنی بر جاوا اسکریپت) رو برای مدل‌های زبانی (LLM) یا دیتابیس خودتون استخراج کنید، پروژه
Firecrawl
که اخیراً تو گیت‌هاب ترند شده رو از دست ندید!
🔥
امکانات بی‌نظیر این ابزار:
1️⃣
استخراج هوشمند (Scrape):
تبدیل هر URL به فرمت‌های تر و تمیز مثل Markdown، HTML، اسکرین‌شات یا JSON ساختاریافته در سریع‌ترین زمان ممکن (میانگین ۳.۴ ثانیه).
2️⃣
پوشش ۹۶ درصدی وب:
به راحتی از پس سایت‌های سنگین JS-heavy برمی‌آید.
3️⃣
خزش و نقشه‌برداری (Crawl & Map):
کشف آنی تمام لینک‌های یک سایت و استخراج کل صفحات آن فقط با یک درخواست (Single Request) یا به صورت گروهی (Batch).
4️⃣
عامل هوش مصنوعی (Agent & Interact):
فقط کافیه به زبان ساده توصیف کنید چه دیتایی نیاز دارید تا Agent این ابزار سایت رو بگرده، باهاش تعامل کنه و دیتای مورد نظر رو جمع‌آوری کنه.
5️⃣
متن‌باز و خوش‌ساخت:
هم به صورت سلف‌هاست (Open-Source) و هم سرویس ابری قابل استفاده است و پکیج‌های آماده برای Python و Node.js دارد.
🔗
لینک سایت رسمی:
🔗
لینک مخزن گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#Firecrawl
#WebScraping
#API
#AI
#OpenSource
#Github
#Python
#Nodejs
#DeveloperTools</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/6509" target="_blank">📅 09:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=hD9DYkhFBqwHERJOB3B1bRlGM56MCwLj_tMTlfNnXxqlrwgQoTSe7f0rOvOIs-hNREwI6dFYxc3HsKjxatyJZVxloUNRw66WNgL3RUIOXsYxPyUyQlzuBe2USkRBawamTNsYolEtSkiArthHRFWjCJFtMilfr-mUAqJ2lOHRebYh6VVZT4hGrXuCKDXvRxaj49fKhqvw0hlx65jxkl6jB-kJpFIDOR1A-KQ-KXtwqAWirmyMUcCvev1NlFAMz6fbXjZXAKgeREE_CVDSkeQ1_IzPKLIfRGRWT4YJHeIfnXbu2fzAVnaeb-2FVH8qEIJApSmcaRUut9nEcdYW5xNEVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c5a46767e.mp4?token=hD9DYkhFBqwHERJOB3B1bRlGM56MCwLj_tMTlfNnXxqlrwgQoTSe7f0rOvOIs-hNREwI6dFYxc3HsKjxatyJZVxloUNRw66WNgL3RUIOXsYxPyUyQlzuBe2USkRBawamTNsYolEtSkiArthHRFWjCJFtMilfr-mUAqJ2lOHRebYh6VVZT4hGrXuCKDXvRxaj49fKhqvw0hlx65jxkl6jB-kJpFIDOR1A-KQ-KXtwqAWirmyMUcCvev1NlFAMz6fbXjZXAKgeREE_CVDSkeQ1_IzPKLIfRGRWT4YJHeIfnXbu2fzAVnaeb-2FVH8qEIJApSmcaRUut9nEcdYW5xNEVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
معرفی KanaiAI؛ چیدمان مجازی مبلمان در خانه شما بدون نیاز به حدس و گمان!
🛋
✨
اگه از اندازه‌گیری‌های دستی و خسته‌کننده برای خرید مبل و وسایل دکوراسیون کلافه شدید،
KanaiAI
دقیقاً همون چیزیه که بهش نیاز دارید! این ابزار هوش مصنوعی به شما نشون می‌ده که هر وسیله‌ای دقیقاً چطور در فضای خانه شما قرار می‌گیره.
🔥
چرا این ابزار فوق‌العاده است؟
1️⃣
مدل‌سازی دقیق:
اسکنر هوشمند این سرویس، یک مدل کاملاً دقیق و سه‌بعدی از اتاق یا محیط خانه شما می‌سازد.
2️⃣
خداحافظی با متر و اندازه‌گیری:
دیگه نیازی به محاسبات و درگیری با ابعاد نیست؛ هوش مصنوعی خودش پارامترهای وسایل مورد نظرتون رو با فضای خالی اتاق تطبیق می‌ده.
3️⃣
تجسم واقعی پیش از خرید:
مبلمان و وسایل جدید را قبل از اینکه پولی بابتشان پرداخت کنید، مستقیماً در دکوراسیون منزل خود ببینید!
🔗
لینک ورود به سایت
🔵
@ArchiveTell
| Bachelor
⚡️
#KanaiAI
#AI
#InteriorDesign
#TechNews
#SmartHome
#Architecture</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6508" target="_blank">📅 09:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjqDO2cr8_vOhYaXHjDQp2rnfnrieIesTY8prDcOArEvZm0OXyVT4-e0iKqQnPTNFjtl6aZE3PCFaEIgWniHYctWr1wy7aFYhP1z4tM8ENgmL7BirySao8E7tetsUKh1neoRylya3WNsr2pY8MGl0z5A-0gITKn-4GGL0HB5sD9Qx-ul_FbsJCexIzg6NiScbdW2Okr_zYLFbKWL0tovRnfYGyw2_CEKhy_0SpqoE3QLdTdTFELkK74XW7kJNcjtUQhygl5M5ws5OAQz1CGsgNCpSaYq03MOx6OpVqnxv7ugLHKfc3dWjfNYXc6XD0cc8Ao5vickkAJabMhr7AVJZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎵
Navidrome — اسپاتیفای شخصی خودت رو بساز!
سرور موسیقی رایگان و متن‌باز که کامپیوترت رو به یک مرکز پخش موسیقی خصوصی تبدیل می‌کنه.
☁️
✨
چرا عالیه:
•
🏠
رایانه شخصی = مرکز موسیقی خصوصی
•
📱
دسترسی از هر دستگاه: اندروید، iOS، وب، پلیرها
•
☁️
پشتیبانی از فضای ابری — لازم نیست PC همیشه روشن باشه
•
🍓
اجرا روی سخت‌افزار ضعیف
•
🎚️
کنترل کامل — بدون سانسور، بدون محدودیت
•
💸
کاملاً رایگان — بدون اشتراک
🌐
Site
#Navidrome
#Music
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6506" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452211db9f.mp4?token=e-hqVlswZ-eU3mgLF-VaQdh2G8GUiSoBNPSHv234ZCGIq4uhbWtAJgGuk2xOTGwz9J4rGRMn7lZbE8zGbOQqaGRqwcxs1qoH2ueTnLxacfbk1WS5moqonpxLIzdQ3sSiAPqzXVJIQxLr1XIwvUSX65p8oQRAr12OdU0dqV67so3jxyV-uWfgwyrmk7ad6kpX4etoq06O33rPWgFrcjXbtlOqE50EU8cuzoyXrU3gypDeONBTDbVjVKjZ4uvmGFJlZMB4DyfK2wmtpTJf1lCTwT6vb3jXHnEjfdglS6sizP85tR9gChAJ3PkpWpwyZstP0dUFBd2vjxQtRNekh408-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452211db9f.mp4?token=e-hqVlswZ-eU3mgLF-VaQdh2G8GUiSoBNPSHv234ZCGIq4uhbWtAJgGuk2xOTGwz9J4rGRMn7lZbE8zGbOQqaGRqwcxs1qoH2ueTnLxacfbk1WS5moqonpxLIzdQ3sSiAPqzXVJIQxLr1XIwvUSX65p8oQRAr12OdU0dqV67so3jxyV-uWfgwyrmk7ad6kpX4etoq06O33rPWgFrcjXbtlOqE50EU8cuzoyXrU3gypDeONBTDbVjVKjZ4uvmGFJlZMB4DyfK2wmtpTJf1lCTwT6vb3jXHnEjfdglS6sizP85tR9gChAJ3PkpWpwyZstP0dUFBd2vjxQtRNekh408-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
OpenScreen — ضبط صفحه نمایش، سینمایی و حرفه‌ای
✨
قابلیت‌ها:
•
🖱
حرکت روان و طبیعی موس
•
🎨
پس‌زمینه شیک و حرفه‌ای
•
✏️
ویرایشگر داخلی: زوم، سایه، گرد کردن گوشه‌ها
•
💻
سازگار با ویندوز و مک‌اواس
•
💸
رایگان و متن‌باز — رقبا ماهی ۲۰$ می‌گیرند!
🌐
Site
#OpenScreen
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6505" target="_blank">📅 21:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9haP8aMR2JvvYnQC13awYrJ-4RVObur9slLKIuL42XE4v1GCA5wRbboFeM9FnXomTf53rnwfojmn3HlQ_LDtXVxUJB01xhW8OW7VXnzaWqPn1L5I8QgXLRLP7f-FMJ_v8j40wIIi-j2k1MYIPS3ig1TiijzIz3nt6Lt3c-FouJmUDP9rhQNYfobgJTR5h1v5kPhujnFmipFv41iKT-rcSOttDhmNKpZtnmzi3ivKk1tDwaPXe5gRpIb35SLy4bUsz1a9EHGlRPPpeGXdqQal2fDsGipTxyYoQilh8t6dlIuRm-BVfv61IozHMTKLqTjyv4lLwV3gb_WO_nQdwvTww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین سایت دزدی دریایی زنده شد — Bookracy در سال ۲۰۲۴ راه‌اندازی شد و به سرعت در شبکه محبوب شد، اما در سال ۲۰۲۵ سایت بسته شد و حالا دوباره بازگشته است.
• درون سایت تعداد زیادی کتاب، کمیک، مانگا و انواع دیگر محتوای چاپی وجود دارد.
• تمام محتوا بسیار سریع دانلود می‌شود. می‌توانید کتاب‌هایی پیدا کنید که حتی در کتابخانه‌ها هم نیستند.
• همچنین امکان ایجاد لیست شخصی برای مطالعه و افزودن هر چیزی که می‌خواهید وجود دارد.
🌐
Site
#Bookracy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/6504" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIFYV28Fbt6YDf4zMujCJl9kTlZJl6rJDv2DhL_WWe4izP2YMo6uUgr42Kb5LWJ9xY9CfZ94jjl66klq3eiX5PrP4zDYKpQfCFuihvczG2u7snocbzdkDvRyac1XIkPXDlif3SELo7iBjriS5yGj0M39VhUUJISFLKEaXH4Hc256AZs2qbKlhGFXTBoIcvBepPvCshvaXz3O_PnKHJ_y5vp_sPRPxYD5Qk2ZqTw4zxdzuqM8Jk0NCYhVGn0U95zhxrjaD6kJ-zX7rk8TMSEhdzOcFYk0c1iMP5uj_7VjcOXRRwnzppmrc6Zpu8XKb1-h1ICpNFQZ9rXUOvbu56PNug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗂
PostKeeper
این افزونه توییتر یا X را به آرشیو شخصی شما تبدیل می‌کند
✨
قابلیت‌ها:
•
🔹
خروجی پست‌ها، لایک‌ها، بوک‌مارک‌ها و لیست‌ها
•
📥
دانلود فایل‌های ساختاریافته برای پشتیبان و مرجع
•
🔒
آرشیو محلی و خصوصی روی دستگاه خودتان
•
🧭
جستجو و دسترسی آسان به تاریخچه حساب
•
🛠
متن‌باز با تمرکز بر حریم خصوصی
🌐
سایت
🌐
افزونه
#Twitter
#X
#OpenSource
#Privacy
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/6503" target="_blank">📅 19:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wvd_fHLSYc83YvgZelqbHM9hcT-DbQfTWMj41wxthi1Yc3UwDaebsGKRhX8NHZRFAEYjXzd-otaqeiHnaYuqSFLiuOGfXV-_vlc84s2zwgb4Au32Z3blpkeS8ObCcI4SuKwa8EfBhTKBOZgv31RCibXEpQi-y_eEdIXyzcl0dVGx3SaoNdvKnuAoadKVts4-TZ2jrtPa1isknTOmMC8YN74HrnGrY3miWnJB2qEZcnEmNDyvK2hzWUYlguYl4h6vbglAhx8fpO2SuRXsi7Z1V55MirFVnhDjkYgB0zefCyHTyOzeNHgP-7aF5ZjVUhFQmz_A6xuZHb_ajom2KvllPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
80 کریدیت رایگان برای دسترسی به برترین مدل‌های جهان مثل Opus، Fable و GPT
✨
همین حالا وارد سایت
kie.ai
شوید
📝
ثبت‌نام کنید و از امکانات فوق‌العاده آن لذت ببرید
🔑
همچنین می‌توانید API Key اختصاصی دریافت کنید
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6502" target="_blank">📅 17:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔗
tiny_computer
یک محیط دسکتاپ کامل لینوکس (Debian 12) رو فقط با نصب یک فایل APK روی گوشی اندروید بالا میاره!
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/6499" target="_blank">📅 16:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQ2El8Bj2cJbEwseIspSy2lSyojmivvYzDj8kXGjNfV7Ss7R_ydooCIo3u-SUp-nfzbhbStEQi_JXIkBGQUxGnvVaR9I06_bgjEoh3vDzL_5zmIQJut-tQdRfWN9UUwTepz9C6SKVJC6O9ib869C6BUTwqW7JfCedUfHZCJGLhLb36SKn8yVqzNfntp8GmZI-Jru4gWjHyROPF6vJTDb3gTcgsAUSmPn9SNDqilxwfjrVT_xULcs-JbjCHpi6Pt6Qo1lpQ3M7JmK00dryF8JCyrPz-jXinoT__yDaLt6CUzFdsMjbKAM1BIDeL6IS73QShrHgJ9nUvajA7CB75_JOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی ترسناک بقا که قوانین هر مرحله تغییر میکنه ، در تاریکی از Cobb فرار کن و از سیاه‌چال خارج شو.
🌐
Site
#Game
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/6498" target="_blank">📅 13:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=GMONxXo_ARVbkpNhdE0BwN4iZwT1qshnTtOm7I3PST7X2uLtILuSM7xyznIqD5QVH02IMmoGXdoTQnHo-FhJm_VMUFOfDP_xU-xRLaJLedLY1bprSL1P2c5BSJuWw4ZjUAq6Uo6dqwXQ18lJU6OY0dMQlsyfx9o0JbjAuj33P8wiDy5aEqG38FamYdmVQ87ZnCvxoEIIDv6XJV8Bjmf5EpdO7rlc7smCcnqFG8YV1z79p1xVrg4fByY4bmBPkMRCB6CkayD-TvGhnupHPuRajV3oXUqMCO5PmcY0-EmhdfKwC-01ZSIYVXQMwMVmL6PUnBI_ZQ3K_0t1sW7U4YJ1Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abeb4a003e.mp4?token=GMONxXo_ARVbkpNhdE0BwN4iZwT1qshnTtOm7I3PST7X2uLtILuSM7xyznIqD5QVH02IMmoGXdoTQnHo-FhJm_VMUFOfDP_xU-xRLaJLedLY1bprSL1P2c5BSJuWw4ZjUAq6Uo6dqwXQ18lJU6OY0dMQlsyfx9o0JbjAuj33P8wiDy5aEqG38FamYdmVQ87ZnCvxoEIIDv6XJV8Bjmf5EpdO7rlc7smCcnqFG8YV1z79p1xVrg4fByY4bmBPkMRCB6CkayD-TvGhnupHPuRajV3oXUqMCO5PmcY0-EmhdfKwC-01ZSIYVXQMwMVmL6PUnBI_ZQ3K_0t1sW7U4YJ1Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">MagicVideoAI
تبدیل متن به ویدیو
🔥
شرکت ByteDance (تیک‌تاک) ابزار جدیدی برای تبدیل متن به ویدیو ارائه کرده است .
این مدل از نظر پارامترها از Pika 1.0 و Stable Diffusion-XT پیشی گرفته و ویدیوهای فوق‌العاده‌ای بر اساس متن تولید می‌کند.
🌐
Site
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/6497" target="_blank">📅 12:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjVvBR9dCkvLFpD1YzWBC-fn_8-R_tbLq4WHrBPhup67IeGXTBl5DI3MieDhwA-sknlNsvKXr4NHEtOKAanU9hKGc3huG8jYin25WtuQ1TrKfEYVNDC66GJ9sUMVgzBp3qxoNdD_06LN1O0tzj2hnT59LaTcxWXOhnQ34sHMXi70ho7pW1ZBMuze5eHUk58vXH2y1lBicQSSpH9LeFcroqcTcnxpZzwUJD_IuYihnHS2_WGknEK3UyZfpNIugTIz1QLpcSzM2btNxs4V_ORolsnZI1mnXaSfOmCOHLKpPfF584UrfLcfe_2ZHgobMO3YWCWOwDEpFIBicKb_whDICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام Sakana Fugu رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک…</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6495" target="_blank">📅 10:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚀
معرفی Sakana Fugu؛ سیستم چندعاملی (Multi-Agent) که GPT-5.4 و Opus 4.6 را شکست داد!
🤖
✨
شرکت ژاپنی پیشرو در هوش مصنوعی یعنی Sakana AI، به‌تازگی از پرچمدار جدید و تجاری خود با نام
Sakana Fugu
رونمایی کرد و ثبت‌نام نسخه بتای آن را باز کرده است. این سیستم یک پلتفرم هماهنگ‌کننده چندعاملی (Multi-Agent) است که در قالب یک API واحد (سازگار با فرمت OpenAI) ارائه می‌شود.
🔥
ویژگی‌های شگفت‌انگیز این سیستم:
1️⃣
دو نسخه متفاوت:
نسخه
Fugu Mini
(با تمرکز بر تاخیر بسیار کم و سرعت بالا) و نسخه
Fugu Ultra
(برای پردازش تسک‌های فوق‌العاده سنگین و پیچیده).
2️⃣
معماری کاملاً پویا (Dynamic):
برخلاف سیستم‌های قبلی که نقش‌های ایجنت‌ها از پیش تعیین می‌شد، هسته Fugu یک مدل زبان سبک و خودران است که بسته به میزان سختی تسک، مدل‌های «کارگر» (Worker) را به‌طور خودکار فراخوانی کرده و کار را بین آن‌ها تقسیم می‌کند.
3️⃣
خوداصلاحی و Test-Time Scaling:
این سیستم قابلیت بازگشتی (Recursive) دارد؛ یعنی می‌تواند خروجی‌های قبلی خود را بخواند، اشتباهاتش را تشخیص دهد و یک گردش کار جدید برای اصلاح آن‌ها ایجاد کند.
4️⃣
پادشاهی در بنچمارک‌ها:
نسخه
Fugu Ultra
در تست‌های به‌شدت سخت استدلال و کدنویسی طوفان به پا کرده است! این مدل در تست‌های GPQAD (۹۵.۱)، LCBv6 (۹۳.۲) و SWEPro (۵۴.۲) توانسته مدل‌های پرچمداری مثل
GPT-5.4
،
Gemini 3.1
و
Claude Opus 4.6
را به‌طور کامل شکست دهد.
🔵
@ArchiveTell
| Bachelor
⚡️
#SakanaAI
#Fugu
#MultiAgent
#AI
#GPT
#Gemini
#Claude
#TechNews</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6494" target="_blank">📅 10:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚀
معرفی یک راهنمای جامع و فوق‌العاده برای یادگیری زبان انگلیسی!
🇬🇧
✨
اگه دنبال یه نقشه راه اصولی، متفاوت و البته رایگان برای تقویت زبان انگلیسی می‌گردید، ریپازیتوری
English-level-up-tips
که اخیراً تو گیت‌هاب ترند شده رو از دست ندید. این راهنما با یه رویکرد قدم‌به‌قدم، یادگیری زبان رو از یه غول ترسناک به یه پروسه لذت‌بخش و طبیعی تبدیل می‌کنه!
🔥
ویژگی‌های برجسته این راهنما:
1️⃣
پوشش تمامی مهارت‌ها:
از درک مطلب و دایره لغات گرفته تا لیسنینگ، ریدینگ، اسپیکینگ و رایتینگ؛ همه‌چیز در این آموزش گنجانده شده.
2️⃣
یادگیری با قدرت هوش مصنوعی:
یکی از جذاب‌ترین بخش‌های این راهنما، آموزش نحوه استفاده از ابزارهای هوش مصنوعی مثل
ChatGPT
و
Gemini
برای تسریع و بهبود فرآیند یادگیریه.
🤖
3️⃣
مناسب برای همه سطوح:
فرقی نمی‌کنه مبتدی هستید یا پیشرفته، دانشجو هستید یا یک متخصص؛ این مخزن ترفندهای جذابی برای همه داره.
4️⃣
جامعه کاربری پویا:
یک مسیر ساختاریافته که به شما یاد می‌ده یادگیری زبان یک مسیر پیوسته است، نه یک مقصد نهایی!
🔗
لینک مخزن در گیت‌هاب:
🔵
@ArchiveTell
| Bachelor
⚡️
#English
#Learning
#Github
#AI
#ChatGPT
#Gemini
#Roadmap
#Education</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6493" target="_blank">📅 10:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebzjP6LSsfyudoNO6dI5TX1gBLFTLRBf4VXULgUpX1SnG5su26Eg33JcXA05J79uhdfCbvE00L06MKIJIw-Qpc6FVbNh8DEH893BUutBpJb8Hs5_WlT2jJ_AJQqPi6oGHEheF6Cl7ED2PxvlXaoXRBGdPUu1-P_JfpEnNQVqFnTsrfQ6zx98UP5fJfhXWtzH574qbXAyoQ_AirbAVMPRvf0nsKiT1reO-5tK2MVtyzoyMQdBKxxN8NEcvgF9blKj0AunzyoyyxJ4MWTC9H6ZxSeQpFNKfia0RMRvoXjS4nSSXX58SjeFJWTwsXhhkSLQ715XgTER_itt9ZvUe7xI_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
ساخت آرشیو اینترنتی شخصی
ابزاری به نام Monolith می‌تواند کل سایت‌ها را در یک فایل HTML مستقل ذخیره کند.
دیگه نیازی نیست نگران باشید که مقاله، دستورالعمل یا مستندات مورد نیاز روزی ناپدید شوند.
✨
قابلیت‌ها:
•
🔹
ذخیره کل صفحه در یک فایل HTML مستقل
•
🖼
نگهداری تصاویر، استایل‌ها و منابع صفحه
•
⚡️
استفاده ساده بدون تنظیمات پیچیده
•
🛠
اجرا روی ویندوز، لینوکس و مک‌اواس
•
📦
رایگان و متن‌باز
🌐
GitHub
#OpenSource
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6492" target="_blank">📅 09:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚀
معرفی OpenPencil؛ رقیب متن‌باز و رایگان فیگما مجهز به هوش مصنوعی!
🎨
✨
اگه به دنبال یک ابزار طراحی جایگزین هستید که هزینه‌ای براتون نداشته باشه، با
OpenPencil
آشنا بشید! این ویرایشگر طراحیِ متن‌باز (Open-Source) با قابلیت‌های شگفت‌انگیز هوش مصنوعی منتشر شده و تمام ابزارهای پولی رو به چالش کشیده.
🔥
چه کارهایی می‌تونه انجام بده؟
1️⃣
پشتیبانی از فایل‌های فیگما:
می‌تونید فایل‌های با فرمت
.fig
رو مستقیماً توش باز و ویرایش کنید.
2️⃣
اجرای محلی (Local):
کاملاً آفلاین و روی سیستم شخصی شما اجرا می‌شه، بنابراین حریم خصوصی پروژه‌هاتون کاملاً حفظ می‌شه.
3️⃣
دستیار هوشمند (Agentic AI):
دارای قابلیت‌ها و ایجنت‌های هوش مصنوعی داخلی برای کمک به پروسه طراحی.
4️⃣
خروجی مستقیم کد (جادوی فرانت‌اند!):
طرح‌های شما رو با یک کلیک به کدهای تمیز و آماده‌ی
Tailwind
و
JSX
تبدیل می‌کنه!
⚛️
5️⃣
یکپارچگی عالی:
قابلیت اتصال و هماهنگی کامل با ابزارهای برنامه‌نویسی محبوبی مثل Claude Code و Cursor.
🔗
لینک دریافت پروژه:
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenPencil
#AI
#Figma
#Design
#OpenSource
#Tailwind
#JSX
#FrontEnd
#DeveloperTools</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6490" target="_blank">📅 04:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">📰
خلاصه اخبار مهم سایبری و تکنولوژی هفته:
🚨
✨
🔹
آمریکا و توقیف AI:
دولت آمریکا برای اولین بار در تاریخ، انتشار یک مدل هوش مصنوعی (
Claude Fable 5
) را به دلیل خطرات امنیت ملی ممنوع کرد.
🔹
هک بانکی در ایران:
یک حمله سایبری سنگین، سیستم ۴ بانک ایرانی را فلج کرد.
🔹
شنود تلگرام:
پاول دورف اپراتور بزرگ هندی (Reliance) را به رهگیری ترافیک کاربران تلگرام متهم کرد.
🔹
خطای مرگبار هوش مصنوعی:
یک سیستم AI در برزیل با رد درخواست بستری اورژانسی، باعث مرگ یک بیمار شد.
🔹
فریب موتورهای جستجو:
محققان ثابت کردند موتورهای جستجوی پیشرفته AI به‌راحتی با یک کامنت هدفمند در ردیت (Reddit) فریب می‌خورند!
🔹
ابطال گواهی‌های SSL:
شرکت GlobalSign به دلیل تحریم‌ها، گواهی امنیتی هزاران سایت روسی را باطل کرد.
🔵
@ArchiveTell
| Bachelor
⚡️
#CyberNews
#AI
#Telegram
#Security</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/6489" target="_blank">📅 23:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6488">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚀
معرفی Prompts.chat؛ خفن‌ترین و جامع‌ترین کتابخانه پرامپت برای هوش مصنوعی!
🤖
✨
اگه می‌خواید از مدل‌های هوش مصنوعی (مثل ChatGPT، Claude، Gemini، Llama، Mistral و...) خروجی‌های تخصصی و بی‌نقص بگیرید، سایت
Prompts.chat
کامل‌ترین مرجع برای شماست!
🔥
چه چیزهایی تو این سایت پیدا می‌شه؟
1️⃣
قالب‌های آماده و کاربردی:
نیاز به نوشتن یه رزومه‌ی حرفه‌ای دارید؟ یا می‌خواید یه قرارداد پیچیده رو تحلیل کنید؟ پرامپتِ آمادش دقیقاً همینجاست.
2️⃣
پوشش تمام نیازها:
از ایده‌پردازی برای کسب‌وکار و تولید محتوای مارکتینگ گرفته تا خلاصه‌نویسی دروس و برنامه‌ریزی تمرینات ورزشی.
3️⃣
خروجی‌های سطح متخصص:
با استفاده از این پرامپت‌های مهندسی‌شده، هوش مصنوعی طوری جواب می‌ده که انگار یه متخصص حرفه‌ای اون متن رو نوشته!
🏆
اعتبار این مجموعه چقدره؟
این فقط یه لیست ساده نیست! این دیتاسِت
رتبه اول بیشترین لایک در Hugging Face
رو داره، بیش از ۴۰ بار در مقالات علمی معتبر بهش ارجاع (Citation) داده شده و حتی در رسانه‌های بزرگی مثل Forbes و دانشگاه‌های تراز اولی مثل هاروارد و کلمبیا هم ازش نام برده شده!
🔗
لینک ورود به مرجع پرامپت‌ها
🔵
@ArchiveTell
| Bachelor
⚡️
#Prompts
#AI
#ChatGPT
#Claude
#Gemini
#HuggingFace
#Tools
#Productivity</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/6488" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚀
معرفی Upscayl؛ افزایش بی‌نظیر کیفیت تصاویر با قدرت هوش مصنوعی!
🖼
✨
اگه عکس‌های بی‌کیفیت، تار یا سایز کوچکی دارید و می‌خواید رزولوشن اون‌ها رو بدون افت کیفیت به شدت بالا ببرید،
Upscayl
دقیقاً همون ابزاریه که نیاز دارید! این نرم‌افزار کاملاً رایگان و متن‌باز (Open-Source) با استفاده از پیشرفته‌ترین مدل‌های هوش مصنوعی، معجزه می‌کنه.
🔥
ویژگی‌های کلیدی:
1️⃣
پردازش گروهی (Batch Processing):
می‌تونید یه پوشه پر از عکس رو بهش بدید تا همه رو با هم و به صورت خودکار باکیفیت کنه.
2️⃣
افزایش وضوح و شارپنس:
رفع تاری، نویز و پیکسلی بودن عکس‌ها به طبیعی‌ترین شکل ممکن.
3️⃣
مدل‌های سفارشی:
امکان اضافه کردن و استفاده از مدل‌های هوش مصنوعی دلخواه برای رسیدن به بهترین نتیجه ممکن.
4️⃣
پشتیبانی کامل:
سازگاری با سیستم‌عامل‌های ویندوز، لینوکس و مک‌اواس (macOS).
⚙️
نکات فنی:
* این برنامه با زبان قدرتمند TypeScript توسعه داده شده است.
* برای اجرای پردازش‌های این ابزار، سیستم شما به یک کارت گرافیک (GPU) سازگار با Vulkan 1.3 نیاز دارد.
🔗
لینک دریافت و گیت‌هاب پروژه:
🔵
@ArchiveTell
| Bachelor
⚡️
#Upscayl
#AI
#OpenSource
#ImageUpscaling
#Tools
#TypeScript
#Github</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/6487" target="_blank">📅 21:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMU-5StxannSqEvCqETNggvVQ7WRIkDMShcB5SYvmxWcfY6o4slo2lSAOeMDrGk-ZOOSYtuQO8tO8RtJ7_xgTYrS4tQH_kWgL8pqniayQNcyJw4Vi18QeqS81Izq7jRTC8Xc15TCM8d1ru5WXu1rZ4bOmjdNJoFnyj0tc_jOnmMB7chxXtnl9vKZ7Sq4a7o4vtqAodTDiQC5YM3uev5t6yZfdh7Z9EuphczMRxO6g9HvjmKsMoSnzJEsrTBhct3ZGJYDpSZk7qKElxN3h05hM1XVmx5k-8XuH0mr0wlt9frEl-Lp8yxrEjygGUmUgZcBLLEbLTKkZ5_puEkJrqEAXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت What Is This Movie کمک می‌کند با توجه به صحنه‌ها، دیالوگ‌ها، جزئیات داستان یا نشانه‌های بصری دامنه جستجو را محدود کنید و سریع‌تر فیلمی را که نامش را به یاد نمی‌آورید پیدا کنید.
🌐
Site
#Movie
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/6483" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViFdM8fYj903J96RyuEiAnEzu90NcqYnLrUuiSJoH5waSX6ZdfSthm7yVh4LmAORAbDG4J2wTYO-8S2DBYlj331XSdtrL3uS6GhSJKAttjYlJKcVxoTQ8Oa0ia8JKFuzh8yTrPyIfY8MwB9IsD2btGhpDVz8Xn_Pn8bkn-Sa0hLZ0EpGzB3XEtA2fjp96JvjKewtxDaMFgwry-u8POVQ7w2QbBAmYcm9FLiQXLiU5FbEhHzb1laVb0voGtLklDUTyYzyqVpWuTKDqifwMkyz_m0hzr2Ki0T1vB5qQjlSMoHGh_ISMtZtCMpP7eNlITAZMA9-YeZzJKy3yiU5o9Kycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف رایگان واترمارک Gemini آنلاین و بدون نیاز به ثبت نام
🌐
Site
#Gemini
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/6482" target="_blank">📅 17:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚀
معرفی Lift؛ هوش مصنوعی رایگان برای استخراج و پارس کردن فایل‌های PDF!
📄
✨
تیم Datalab به‌تازگی مدل هوش مصنوعی قدرتمندی به نام
Lift
رو منتشر کرده که می‌تونه داده‌ها و اطلاعات رو از فایل‌های PDF و تصاویر بخونه و در نهایت یک خروجی کاملاً ساختاریافته و تمیز با فرمت
JSON
بهتون تحویل بده.
🔥
ویژگی‌های کلیدی و برجسته:
1️⃣
دقت و کیفیت شگفت‌انگیز:
توسعه‌دهندگان این مدل ادعا می‌کنن که کیفیت خروجی Lift به‌شدت نزدیک به مدل قدرتمند Gemini Flash هست و از خیلی از مدل‌های متن‌باز (Open-Source) فعلی بهتر و دقیق‌تر عمل می‌کنه.
2️⃣
خروجی ساختاریافته (JSON):
این مدل دقیقاً خوراک برنامه‌نویس‌هاست! داده‌های خام، جداول و متن‌های به‌هم‌ریخته رو می‌گیره و یه دیتای مرتب و آماده‌ی استفاده تحویل می‌ده.
3️⃣
کاملاً رایگان و در دسترس:
این شبکه عصبی صددرصد رایگان و متن‌باز منتشر شده و می‌تونید بدون هیچ هزینه‌ای ازش تو پروژه‌هاتون استفاده کنید.
🔗
لینک‌های دسترسی و دانلود:
گیت‌هاب پروژه
مدل در هاگینگ‌فیس
🔵
@ArchiveTell
| Bachelor
⚡️
#Lift
#AI
#PDF
#JSON
#OpenSource
#DataExtraction
#DeveloperTools</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/6481" target="_blank">📅 16:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGpDBgRWHWKqvpQtLB41TDbV7_bDoSI--ohG0FM0MsPD5aEckhJ_rZL_MUfwW1IFXnCatDeGDYmVrw9ae1wi7ilSJSWUiJqHVVoXFC20VB5JtpwveMP0KPObRUgWP1ZzozaYO9zqZcc3aAdlNqMFj2I0clRpAu8thsE-YoC4oiTWW5X6Zh7bL0O-pEcT4kg-1I4oy_yN3YuEWjz6t7KhzLtvaLS-mscxmVIKjcZ97a8Nm8_Xlf28VcNfToQattV0mttkTFJ4S6FpCAke9bh82v3347YGdzID6r3rKaL2lV09Or4YouOzm5qJPMwqu1TAqqpdYyYQyrlpno8aMne-cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
مدل Gemini 3.5 Pro احتمالاً ۹ تیر (۳۰ ژوئن) منتشر می‌شود!
🚀
✨
🔹
شایعات داغ:
کاربران شبکه X پیش‌بینی می‌کنند که این مدل قدرتمند دقیقاً در آخرین روز از مهلت وعده داده‌شده توسط مدیرعامل گوگل (۳۰ ژوئن) منتشر شود.
🔹
سوتی عجیب گوگل:
در حین آماده‌سازی بک‌اند برای این آپدیت جدید، رابط کاربری تحت وب Gemini باگ داده و اشتباهاً پاپ‌آپ معرفی نسخه‌های قدیمی (2.0) رو برای کاربران نمایش داده!
🔹
نتیجه‌گیری:
این گاف فنی نشون داد که نسخه وب جمنای هنوز پر از کدهای قدیمی (Legacy) و باگ‌های پیش‌پاافتادست.
🔵
@ArchiveTell
| Bachelor
⚡️
#Gemini
#Google
#AI
#TechNews</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/6480" target="_blank">📅 15:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚀
معرفی WinScript؛ ابزار قدرتمند و متن‌باز برای شخصی‌سازی و بهینه‌سازی ویندوز!
🛠
✨
اگه دنبال یه ابزار سبک، ساده و متن‌باز (Open-Source) برای شخصی‌سازی، سبک‌سازی و افزایش سرعت ویندوزتون هستید،
WinScript
رو از دست ندید. این برنامه به شما اجازه می‌ده اسکریپت‌های اختصاصی خودتون رو برای ویندوز بسازید و روی هر سیستمی که دوست دارید اجرا کنید!
نحوه کار:
خیلی سادست! تو رابط کاربری برنامه، تیک قابلیت‌هایی که می‌خواید حذف یا بهینه‌سازی بشن رو می‌زنید، یه اسکریپت آماده تحویل می‌گیرید و هر زمان که خواستید اون رو روی سیستم خودتون یا هر سیستم دیگه‌ای اجرا می‌کنید.
🔥
امکانات و ویژگی‌های کلیدی:
1️⃣
حذف برنامه‌های اضافی (Debloat):
پاک کردن اپلیکیشن‌های پیش‌فرض و مزاحم ویندوز مثل Copilot، Edge، OneDrive و سایر نرم‌افزارهای غیرضروری (Bloatware).
2️⃣
حفظ حریم خصوصی:
غیرفعال کردن کامل تله‌متری (ردیابی اطلاعات) ویندوز و برنامه‌های شخص ثالث، و مسدود کردن دسترسی و جمع‌آوری داده‌ها.
3️⃣
بهینه‌سازی فوق‌العاده:
تغییر وضعیت سرویس‌های پس‌زمینه به حالت دستی (Manual) برای آزادسازی منابع سیستم، تنظیم DNS و پاک‌سازی فایل‌های موقت (Temp).
4️⃣
نصب سریع نرم‌افزارها:
امکان نصب گروهی و یک‌کلیکه‌ی تمام برنامه‌های مورد نیازتون با استفاده از ابزار قدرتمند Chocolatey.
⚠️
نکات مهم پیش از اجرا:
* اسکریپت تولیدشده حتماً باید با دسترسی ادمین (Run as Administrator) اجرا بشه.
* چون این ابزار تنظیمات ریشه‌ای سیستم رو تغییر می‌ده، ممکنه آنتی‌ویروس (Windows Defender) بهش گیر بده که این یک هشدار اشتباه (False Positive) است. با توجه به متن‌باز بودن پروژه، خیالتون از بابت امنیت راحت باشه.
⚙️
سازگاری:
ویندوز ۱۰ و ویندوز ۱۱ (کاملاً رایگان - لایسنس GPL-3.0)
🔗
لینک دانلود / گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️
#WinScript
#Windows
#Windows11
#Optimization
#Debloat
#Privacy
#OpenSource</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6479" target="_blank">📅 12:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHEbx1ag8LCf3PoiergbaXrjwk7W7cIr5iKiSuyeBCFL8hJ8VQiiq2PA7yEmedbeaSUglOUkeCBAuPJ2HWL7599X4WGWOFaQE_nHsp8mvI1NWHx2X-UndqOecar_Ii-icdkJAJ8WjulsrAwMED8BMVlyfXlCBbrYSLXEwYktdXTOcspwIx3jZAbhBKEt6-lF0mB8NcaVAGR_KJaRihnByXnUi1gCWgVd86v-9DBgIn5f7vQdlP0d9zhgikoah32jTHqr-EQ4205SY4Q4DLplX5-Usip3IZfwkxnpWgG8f0FLpQMTI3Dcd0XEabz-h7YPMLkNmMoKfXY5--qZWXvuIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
با GeoSpy AI می‌توانید محل احتمالی ثبت یک عکس را از روی جزئیات تصویر پیدا کنید.
•
🔹
تحلیل جزئیات عکس و مقایسه با تصاویر آنلاین
•
📍
ارائه مکان‌های احتمالی همراه با مختصات
•
🎯
مرتب‌سازی نتایج بر اساس احتمال تطابق
•
🏞
دقت بالاتر در مناظر طبیعی و معماری خاص
🔗
لینک:
Site
#AI
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/6478" target="_blank">📅 12:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fp9DzbTgYBtF4pT2W-DZRWCzMYbLNMWccOhz5cKsrIXXvQ8V_IdkMj5t_8JSAdGvcYHDg8wk2qOH8aKCCz59gOOrhhp4UKdCpmjhN1hnYaFkJsJeCy9nHOLcTiEkgGY-hut5LP0TzgW32TSwH4k6BesdDqvjeS11Mk89jiv9kkTK_SjqbxhlxGUNNJ_s4aWwU3b8QtRXxXfCCxbp-p0Kj2LxBcGd7lRaLS4UbpbEavb5B8xjQQ5eM3-1HibyNNmeZoORPW306LYui7F7t6orJwBzDNNVfQcJhOWdcAek9l1XXFltoHSZxl2Y5vS1-NiDIIWWqXrA_oXT-Zi_dQJsHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی کاملاً رایگان به مدل‌های هوش مصنوعی با Unlimited AI!
🤖
✨
اگه دنبال یه راه بی‌دردسر و مجانی برای استفاده از مدل‌های هوش مصنوعی هستید، سایت
Unlimited AI
دقیقاً همون چیزیه که نیاز دارید!
🔗
لینک‌های دسترسی سریع:
🌐
وب‌سایت اصلی:
🛠
اسکریپت واسط (Transfer API):
اگه برنامه‌نویس هستید و می‌خواید این سرویس رو به پروژه‌هاتون متصل کنید و ازش خروجی API بگیرید، این ریپازیتوری
گیت‌هاب
کارتون رو راه می‌اندازه
🔵
@ArchiveTell
| Bachelor
⚡️
#AI
#FreeAI
#API
#Tools
#Github</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/6477" target="_blank">📅 10:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6476">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=vEXU2i7e3C9T21f_tnKP1kxI1jr4gsb4HlLsSQiOZ45-pHrtr1YybsoO_rdcNfvWhux5XtCMdYSaMFcGiAS0zURGjJBZJR3EdvtVl6_a5pfKwd9b2Thpo1agwR1vqF3PNkVEYE7EOupecnBxkhj-kZBxPOxbbOI0G87ik8NXmYEEGXe9exyG80B1LXojGbzMpXkpLvM_4MehQxcDWIjF5gGN7I649R1KtiBuAaQ1r-aZdMIs2IeQ2-3WKUYefJNAAnXdU4L5ViFJRu0q8AfUdFqyM_s9HkYYYd8tI25Oh5K5dTQnOjdA4SrLrevWYVs-22s43Pz6oubOf_xTIhLP4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/165c1586b0.mkv?token=vEXU2i7e3C9T21f_tnKP1kxI1jr4gsb4HlLsSQiOZ45-pHrtr1YybsoO_rdcNfvWhux5XtCMdYSaMFcGiAS0zURGjJBZJR3EdvtVl6_a5pfKwd9b2Thpo1agwR1vqF3PNkVEYE7EOupecnBxkhj-kZBxPOxbbOI0G87ik8NXmYEEGXe9exyG80B1LXojGbzMpXkpLvM_4MehQxcDWIjF5gGN7I649R1KtiBuAaQ1r-aZdMIs2IeQ2-3WKUYefJNAAnXdU4L5ViFJRu0q8AfUdFqyM_s9HkYYYd8tI25Oh5K5dTQnOjdA4SrLrevWYVs-22s43Pz6oubOf_xTIhLP4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
گوشی‌تان را به کنسول رترو تبدیل کنید؛ صدها بازی کلاسیک مستقیم در مرورگر.
•
🕹
بازی‌های PS1، Game Boy، Sega و پلتفرم‌های نوستالژیک
•
⚡️
بدون نصب، حساب کاربری یا اشتراک
•
📱
💻
قابل اجرا روی موبایل و کامپیوتر
•
🎮
پشتیبانی از گیم‌پد
•
🆓
رایگان و آماده اجرا
🔗
لینک:
Site
#Gaming
#Retro
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/6476" target="_blank">📅 09:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWqnAJkqSDACOXKWPSDeRQLDjy67yK0YCRq3qLdYegjFJYUWQ7Qf8O4S2O83HqeDNZd_4SueSLhXq9AAfF6ikpqwpoc6RoW3hdYmSrNUIgDYx2UxYebIPbgQh3V_CGBARkTIw78uxRax3YrWi0hW8SrTRreppbaSV5oarGZFgmLffIeQhLQjIB4yn-UnVx-WOUsSYfDqX45gEKszFj1hssz5CBI0h9v9nqtw5dW9gbpb4SgIQLSxc01bripH1A7AuqkkiT8Xl_PNJiZLUpSYjZEaF2IeMZK_oE79ZYuDya7W6wELAEo613uHnnBLuj7CzIuMF0Ce3PMD4JNBnno_Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی رایگان به API مدل DeepSeek-V4-Flash تا ۲۸ ژوئن!
🤖
✨
یه فرصت بی‌نظیر! می‌تونید مدل جدید و فوق‌سریع DeepSeek رو تا ۲۸ ژوئن (۷ تیر) از طریق API کاملاً رایگان دریافت کنید و بدون پرداخت هیچ هزینه‌ای برای توکن‌ها، پروژه‌هاتون رو باهاش پیش ببرید.
🔥
چه کارهایی می‌تونه انجام بده؟
1️⃣
تولید کد و اتوماسیون:
ایده‌آل برای کدنویسی و سناریوهای عامل‌محور (Agentic).
2️⃣
تحلیل و تسک‌های فنی:
عملکرد عالی در تحلیل داده‌ها، تولید محتوای متنی و حل مسائل تکنیکال.
3️⃣
پروتوتایپینگ سریع:
تست سریع ایده‌ها و ساخت نمونه‌های اولیه بدون هیچ نگرانی بابت هزینه‌های API.
4️⃣
پروژه‌های خلاقانه:
خوراکِ آزمایش و پیاده‌سازی روی ربات‌ها، سرورهای بازی و سایر پروژه‌های خاص و غیرمعمول.
🔗
لینک دریافت رایگان
🔵
@ArchiveTell
| Bachelor
⚡️
#DeepSeek
#API
#AI
#Free
#DeveloperTools
#LLM</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6475" target="_blank">📅 01:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncPiX5fYQDc6ixasKFCRUzKGRIxQFcsiBhMjhy6kw-kDvee4k7WcqIwXKkAYx3G22tRQ9lY9DPoDunDj671PU7DZ1sqPEsvws0wjF_4oM1GWu5hvoor16FsonvbgSpvcjpoDbRdrk5uiAYrJ25l2ASlei2pB0RtffCV3a9osix3zQKVU9vl8A16j5h9Se_8ZVeNr865cV-sqABsKwUzGYrhYd3Q1uJz7TRETEVSkob_7vfWtDOeZRn_izMxP7GWLFaYJ3MXjzu25N-4txCpaAPDSfSRbaMmKACP_wmeS2VggjNteVKWGgtr5kLBT_z79v92RbEaKkGWfNH3pMfFTNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دریافت یک ماه اشتراک پلاس رایگان پلتفرم HotGen AI!
🤩
✨
اگه به دنبال استفاده از قوی‌ترین مدل‌های تولید عکس و ویدیوی هوش مصنوعی هستید، الان می‌تونید اکانت پلاس پلتفرم
HotGen
رو به مدت یک ماه کاملاً رایگان دریافت کنید!
🔥
مدل‌های قدرتمندی که براتون باز می‌شن:
>
🔹
Seedance 2.0
>
🔹
Kling 3.0
>
🔹
Google Veo 3.1
>
🔹
WAN
🛠
مراحل دریافت (بدون نیاز به شماره و کارت بانکی):
1️⃣
وارد سایت
https://hotgen.ai
بشید.
2️⃣
خیلی راحت با اکانت گوگل ثبت‌نام کنید.
3️⃣
توی داشبورد کاربری‌تون، بخش
Tasks
رو باز کنید.
4️⃣
هر ۶ تسک ساده رو انجام بدید (ساخت یک عکس، ساخت یک ویدیو، اشتراک‌گذاری و غیره).
تمام! اشتراک پلاس شما به‌صورت خودکار فعال می‌شه.
✅
🎁
با این اشتراک چی می‌گیرید؟
به مدت ۳۰ روز، سقف محدودیت‌های تولید ویدیو و تصویر برای شما به‌شدت افزایش پیدا می‌کنه و می‌تونید از بهترین مدل‌های روز دنیا با بالاترین ظرفیت استفاده کنید.
(البته جمع کردن توکن به این راحتی نیست. زاییده شدم
😂
، الان تست کردم)
🔵
@ArchiveTell
| Bachelor
⚡️
#HotGen
#AI
#Free
#Kling
#GoogleVeo
#VideoGeneration</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/6473" target="_blank">📅 00:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚀
معرفی Remnawave؛ پنل مدیریت پروکسی قدرتمند و مدرن مبتنی بر Xray-core!
🌊
✨
اگه دنبال یه ابزار حرفه‌ای برای مدیریت زیرساخت پروکسی می‌گردید،
Remnawave
با تمرکز روی سادگی و راحتی کاربر طراحی شده است. این پنل به شما اجازه می‌ده نودها، کاربران و اشتراک‌ها رو در یک رابط کاربری وب بسیار تمیز و به‌صورت یکپارچه مدیریت کنید.
تمام بخش‌های این پروژه (بک‌اند، فرانت‌اند و نود) کاملاً با TypeScript و با استفاده از فریم‌ورک‌های NestJS و React توسعه داده شده است.
🔥
ویژگی‌های کلیدی و پیشرفته:
1️⃣
معماری ماژولار و بهینه:
دیتابیس، پنل وب و صفحه اشتراک (Sub Page) کاملاً قابل تفکیک هستند. یکی از بهترین قابلیت‌ها اینه که حتی اگه پنل شما آفلاین بشه، نودها بدون مشکل به کارشون ادامه می‌دن!
2️⃣
مدیریت حرفه‌ای کاربران:
تعیین محدودیت ترافیک، فیلترها و قابلیت جذابِ محدود کردن اتصال به دستگاه‌های خاص از طریق شناسه سخت‌افزار (HWID).
3️⃣
مانیتورینگ و امنیت بالا:
مانیتورینگ لحظه‌ای ترافیک کاربران و نودها، پشتیبانی از ورود با اکانت تلگرام (OAuth)، احراز هویت دو مرحله‌ای (2FA) و هماهنگی کامل با Cloudflare Zero Trust.
4️⃣
امکانات ویژه:
تولید انواع فرمت اشتراک (مثل Mihomo و Sing-box)، پشتیبانی از وب‌هوک (Webhook) برای کاربران و نودها و ابزار داخلی برای اعتبارسنجی کانفیگ‌های Xray.
﻿
⚙️
حداقل سیستم مورد نیاز:
برای نصب این سیستم قدرتمند (از طریق داکر)، به
۲ گیگابایت رم
،
۲ هسته پردازنده
و
۲۰ گیگابایت فضای ذخیره‌سازی
نیاز دارید.
🔗
لینک‌های دسترسی سریع:
داکیومنت
گیت‌هاب
داکر هاب
کامیونیتی
🔵
@ArchiveTell
| Bachelor
⚡️
#Remnawave
#Xray
#Proxy
#VPN
#OpenSource
#TypeScript
#Tools</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/6472" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_4qVEN-GWfzjxVXdQjEjFvfKa6MWQyW8eNFlnfI1kH57chIlUiVJF-Fi-1WcAG0qSJhQHYsI2CN9k51DUr84WJxXhOHz8jhNBiS8t209kG2DOOk50KqVG7_c8IpT8xelMI9AZnLq6_qK-QN5LqINCxqQ-PFyBOysoFuI-7DOQoA4poYnlF3XX35D2-WXot2YV8uvofoDAkLwL-LQepQ_65jvCS-UpIB5SR2Lc3_XOnN5SguyQ-eHd1J94LXm6uGGLivLeANKfmLbCQIS0Jthaz1unuvQDD4WEuynm7wbqE6tV9StVCUVaqmOmmx5ddjyUDI_lATcPHrYgEZa9vxEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
یک کتابخانه رایگان از پرامپت‌های Nano Banana برای ساخت تصویر با
AI Studio
منتشر شده است.
✨
قابلیت‌ها:
•
🔹
پوشش سناریوهای متنوع برای تولید تصویر
•
⚡️
قابل استفاده رایگان در AI Studio
•
🗂
دسته‌بندی منظم و جستجوی سریع
•
🔄
به‌روزرسانی مداوم با پرامپت‌های جدید
🔗
لینک:
Site
#AI
#Prompts
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/6471" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚀
معرفی Ladder؛ عبور از پی‌وال‌ها و خواندن رایگان مقالات پولی با یک کلیک!
🔓
✨
🔥
🔥
🔥
اگه برای خوندن مقالات، اخبار یا کتاب‌های معتبر تو سایت‌های خارجی با درخواست خرید اشتراک و صفحه‌های پرداخت (Paywall) مواجه می‌شید، ابزار
Ladder
این مشکل رو برای همیشه حل کرده! این سرویس با شبیه‌سازی رفتار بات‌های موتور جستجو، بهتون اجازه می‌ده محدودیت‌های هزاران سایت رو دور بزنید.
🔥
ویژگی‌های جذاب و کاربردی:
1️⃣
دسترسی نامحدود:
باز کردن مقالات پولی و ویژه در سایت‌های معتبر علمی و خبری مثل WSJ, NYT, Bloomberg, The Atlantic, Nature, Science, The Lancet و کلی سایت دیگه.
2️⃣
وب‌گردی بدون مزاحم:
حذف خودکار تمامی تبلیغات، بنرهای پاپ‌آپ، ترکرها (ردیاب‌ها) و اسکریپت‌های اضافی، تا یک تجربه مطالعه تمیز و راحت داشته باشید.
3️⃣
نصب و اجرای منعطف:
می‌تونید این ابزار رو روی سرور شخصی خودتون (Self-hosted) یا حتی به‌صورت لوکال روی سیستم (PC) نصب و اجرا کنید.
🔗
لینک دریافت ابزار
🔵
@ArchiveTell
| Bachelor
⚡️
#Ladder
#Paywall
#Bypass
#Articles
#Tools
#OpenSource</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6470" target="_blank">📅 19:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUSsiNBbu6i9Ev8z8aMwa36iiuzMGs5G3nsLhHCyShi7LQPWgKU01U-KYHSnenybEkw26pI5OvxjvAzxpSVd__x96DEYziqTbQeZpaR0sWENkGpiy8FfyOMTbg9aPSwmaOKv_5c8npQQJ0gaG4H80MxSus8sZQik2CrJUUG5G9Y0KtlvdbPpU_6pfxjDoBJIFGxzHownhp_9zzG0RfL1n9He1BQAH0vNmH3jNgAJ3PzOSgLngQ5EKgU3X5MYHjPIK_8grjXMV6CxSxt_nyh9Swv8gciS_myfu_S5bSxfVgeBaF0-rXnWFX5I_sREpzSZpC34o1slfV-dRd_ClGomrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
بازی‌های کلاسیک کنسولی را مستقیم داخل مرورگر اجرا کنید؛ بدون نصب و دردسر.
✨
قابلیت‌ها:
•
🎮
شبیه‌سازی کنسول‌های Nintendo، Atari، Sega و دیگر پلتفرم‌های قدیمی
•
⚡
انتخاب بازی و اجرای سریع از داخل سایت
•
📦
امکان آپلود فایل ROM برای بازی‌های دلخواه
•
☁️
همگام‌سازی ذخیره‌ها با فضای ابری بین دستگاه‌ها
🔗
لینک:
Site
#Gaming
#RetroGames
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/6469" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🎬
معرفی OpenMontage؛ استودیوی شخصی و هوشمند شما برای ساخت ویدیو!
🚀
✨
اگه تدوین ویدیو بلد نیستید اما ایده‌های جذابی تو سرتون دارید، ابزار جدید و متن‌باز
OpenMontage
دقیقاً برای شماست! این هوش مصنوعی خفن، فقط با خوندن توضیحات ساده‌ی شما، یک ویدیوی کامل و حرفه‌ای تحویلتون می‌ده.
🔥
ویژگی‌های جذاب و کاربردی:
1️⃣
صفر تا صد اتوماتیک:
از ایده و سناریونویسی گرفته تا پیدا کردن متریال (عکس، ویدیو، موزیک)، صداگذاری و تدوین نهایی رو خودش انجام می‌ده.
2️⃣
الهام‌گیری از یوتیوب:
فقط کافیه لینک یه ویدیوی یوتیوب رو بهش بدید تا سبک، ریتم و حال‌وهوای اون رو تحلیل کنه و یه ویدیوی جدید با همون فرمون براتون بسازه!
3️⃣
اتصال به ابزارهای مختلف:
این سیستم به ده‌ها هوش مصنوعی دیگه (برای تولید عکس، صدا و موسیقی استوک) وصل می‌شه تا باکیفیت‌ترین خروجی رو بهتون بده.
این ابزار کار رو برای تولیدکنندگان محتوا، معلم‌ها و هرکسی که می‌خواد بدون دردسر ویدیو بسازه، به‌شدت راحت کرده!
🔗
لینک ابزار (گیت‌هاب)
🔵
@ArchiveTell
| Bachelor
⚡️
#OpenMontage
#Video
#AI
#ContentCreator
#Tools</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/6468" target="_blank">📅 17:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLhpa_xmBoYfRluQ6UBgO2K-ymQsu3LBA1LaIEUdTLQqqDDSNdoqTUwdUbC_oblw1A_Osv2qreVjQt7aub-hUfhT1xju9B-lFZqJyKrDS4q9D3kIwnzSOojldp23Lez1p8bfSL1D0ljvFnncaDrqalk1UHxT6KcXS_68_mtbcgTC17bDPT1h1xEDI-dbREPgiqaMFDjrDNAb8gDwaNeoixN1ymVtqtlAW65a4m1Iu3z0xRWEoiL27Ta3wnfkU9ek6utK-IWVv0MB_r_mF72NnN5fKliiyepc8x1JcMmhUqLizTfV4FIIS4O4r6XbJ5teIa6xRla5pL7j7r0A1xSaGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bR7jgyTCC1d50CzxQ4F1--ZEBWWPgVJHidt2y5IzjiX-6K3tygNWJ2Piz0JMXaiVKX9Bn_2TzQVyQbXLUVfJMNhjnC69VJUjRwzytUMtRyVlajm_vtL_sl8_McUNH5rX_D_ZE9IxyuvhForvPez3v6ua0UDiM-UvY_IUhPjULKqZMDMWgfyb9wswMdVy9jg0v7K8wDmZ1psrtlGqoyqgji1nEf7hyr0EKqmDqo_ga15tSd2QCNpiGSyomVijNdW5kf5P4SgjiLpOVk8o0I6pFY3-oYqSs0mYTv1Qa5tRd5jgaGLGx98r0t25K4_G1CGfvAtk4BxqAcRibxFdnGyd5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QeVODjX4JfyYZskJBWOQxWi3QkKJlOCNYlvQIWWehQzqYvlecxhtkyPZxRHvz46WTOCfaHyD8SKhzYL2v4ptbzvqCJ_sf7XLq7asAnopcrsm6bPSCPS-N8xrBwxggeRDBJDrH7X8hcatoa8UX3DED_wtd26zgTiG9LXtLchwwNBIhXAD8n8Oe86KaXB865gv9H-8yDwj3TBS6HWPEnQAgz_IQ4NYzd-UV6YX7p3Y5uc6h3UAcvDRpsQOQNaHIy_JVVU13UlTPLtpNB7jp1xFzOmUzr6H_wwUYkAWWC3pA5pYFbePlMU2-7S9ZfKlrLx3truC7pGk_KRt1Qr2Td7WCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lctnYBPhSg03D6RLepfh2NfDj4JQ_yPuzwRmi2IQSq-wDtFji8AwDJFFh2q4fFKAE92AugA4gKwojLzD3FJebC2nWCX1ZjLKQP44mAyx92FEuIT1jD25uHB6H-39E4qkOf9JRAY9FWqiXmO3ocVyVwnWtNiVj0IEfRI60RFCxPQzIK08aQ46B3AGpQ1fbu-wdLtkCWgl4fmekacjhsBdlaV7Jw-3xvXSpQsZSHMdnD6hKKNP_T6VjNJur1VyYZA5oQq6OiMPkRHfV09C_8vE6Iaq1-52UDkU0IDN5wg7XKj1QogP1Ww2ovp9qYEVI-5bHJQlCBGCoWbfg2WuJ3yb7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Splayer
پخش‌کننده موسیقی متن‌باز با قابلیت دانلود از یوتیوب و اتصال به اسپاتیفای
🎵
✨
قابلیت‌ها:
•
🔹
پخش فایل‌های محلی و مدیریت موسیقی‌ها
•
⚡
دانلود صوت و ویدئو از YouTube
•
🛠️
واردکردن پلی‌لیست‌های Spotify
•
🎧
متن همگام‌شده آهنگ‌ها، پادکست و کتاب صوتی
•
🎚️
اکولایزر پنج‌باند، ویژوالایزر و ویرایشگر صوتی
•
🎨
شخصی‌سازی تم و رابط کاربری
🔗
لینک:
GitHub
#OpenSource
#Music
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/6463" target="_blank">📅 16:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚀
🔥
ویژگی‌های کلیدی و پیشرفته:
1️⃣
تبدیل سایت به اپلیکیشن: هر سایتی که فکرش رو بکنید (مثل ChatGPT، یوتوب، ایکس/توییتر، اسپاتیفای، دیسکورد و...) رو به یک برنامه دسکتاپ مجزا تبدیل می‌کنه.
2️⃣
حجم فوق‌العاده کم: برنامه‌های ساخته‌شده با این ابزار تا ۲۰ برابر کمتر از اپلیکیشن‌های سنگین مبتنی بر Electron فضا اشغال می‌کنن.
3️⃣
سایز مینیاتوری: میانگین حجم هر اپلیکیشنی که باهاش می‌سازید فقط حدود ۱۰ مگابایته!
4️⃣
مصرف بهینه منابع: به لطف استفاده از قدرت زبان Rust و فریم‌ورک Tauri، مصرف رم سیستم به طرز چشمگیری کاهش پیدا می‌کنه.
5️⃣
پشتیبانی کامل: این ابزار کاملاً رایگانه و روی ویندوز، مک (macOS) و لینوکس بدون مشکل کار می‌کنه.</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/6462" target="_blank">📅 13:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBRdLnVok6Yfp3EhdWm3j8P4htlxybJVT8lm5yDLaSQMGFi5eilRK0xm2wvYXo0oAar6Y-zTywmR6R0i9FTDntVMlYTe6BsFLkAl6oKNIhTOdxIF7LWhFPqKwiMkTKxcbTRabqtCMOF_nxFPd6VFa7tsLlrtSZBvaEaatST9ojYiqKIFB56Vg3utNpEUGydEK2O6jAUKxV7rBJQl_fgMNWEs0eOUKgODUzW70hLnebJNhvmS9Ch8YCxoCWJZNqr9_9SsuNk5PMkvWxMS6uIxCdVYYAGs2_bPWfJ3iB6WykdP7zUM1CAcPp_9RgbzI5-bint_YzaZl5MT9TbZIxDGZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q8OabbRHkmg3kP0_2-3idZS7lCP5h0-XCVEmzXadOSfy55s6UDODV80sYgZgT5g8TGxnzIQeu-9gjcVg-o7LAWhmCKpZ2UlzxkgUkrvnO7wkZu0SFRg7itHx4lnhDlh_slbj2mEH-R7TKW6MmwYFGJzqdinavyAqFC_k69zMlPDvHNkuGmdHkHluFktCN8WAId-drwzTiaW0V_BhFyu4Oe8ySXYdkjzwL7Pa5LpsU0y82hXQXwhgga1WXjcD6lHhJSaDGKf7NkiXiCq3Yil1CkE9gnQy3cydzYHUp-PylVCm_Eda-DQQPC3TEMJMuKea29EQHG9bPbrOzPVqXHJRJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYCcGRQ3fQK_ljOx0NvekUJyQ-bH8-LJzNpUvQpKlHnUdwizJ3JwAHaOA5OAJztfOW4DGOXOR3tzn4cUo9qda6FeVE83E8mVQovIHFF0OujemOIAkoGh0C_2hC2bHvEqrx2tbqfO-9T8p8U7ZXKYD6a2MhfXPuyg1_9MzJHq8FMsdm6trBzJeTjhsyFl764NqonXGjCLDBdLqQJa8ttj07fPkGTNe_yr5pSG0Weq0PFgtMRzFVaMTUAo_zCdO4676C6hiPYL9PsNjkQJMqkxAqF0zvMV7Jr11uto8m--NlLUvZaiKuOpjOUvi2vIvU9Eqi5kkS6gPVaDdhSHOPC79Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VywtY1FmMcrb26uHVnG_oxq1I4fpqNM1N3jFvmXN01CvGVtM6hselWUiY6KirQcF-ZQ-c5_7zcS-zsxxzYvsVk3FHLC8cHS9BWcvm0WE1pmYl5f4l5AqkubJyiRE2I2J8lcI_kmBG7ETE7L51Sfzu7DGdFcTv8j1T4hb0GxKHmLDa1jlqlc_7M-h-FdqwMSN4AzEWCOdr0-1IoTe9zP212Sv0mFf5qXMYAi4arBu3uL5UsAvdHbh2PNsz4WRDyrWKTZ1qyOJRMQVlA6cyNkUczqF0Vhw1wI3Yac9QAIvHOSA6qsDE8O2TT4yjVc4b2jQ7Bf7PkgPzLawMfgLwbdimQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ded905356.mp4?token=BXYbzGlmuaVeIuIr7C0Ec_9IhsQGv5qyNz5o7Dd5ZtyyfgMV5unSD7PfvT5U4MIhzEh9niuyj5KdQcUuHlL9oHS-AwhOyMq_nyJ-yDGmd6yJKTOGGuZW5OeZL4GTLWpULJ46nHj_pdrcHrbY0TDUX3oOsAdvXoWMsTL0W16lUo2bFvV1j_g-pMGTh_qYl4XelhsUOyxXJJCuuzMRhkn3N9UqR0-EITpUuPns1tdwFoQLGDAfbLWesvtqJfenThfKevcFsq1ifL70-BnibutxASyjoBc0Ps-JChYxHz0ZiF16NxdiaTRV7eYCAHX30pde7L6eeeAGYb7lVnjomQ33uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ded905356.mp4?token=BXYbzGlmuaVeIuIr7C0Ec_9IhsQGv5qyNz5o7Dd5ZtyyfgMV5unSD7PfvT5U4MIhzEh9niuyj5KdQcUuHlL9oHS-AwhOyMq_nyJ-yDGmd6yJKTOGGuZW5OeZL4GTLWpULJ46nHj_pdrcHrbY0TDUX3oOsAdvXoWMsTL0W16lUo2bFvV1j_g-pMGTh_qYl4XelhsUOyxXJJCuuzMRhkn3N9UqR0-EITpUuPns1tdwFoQLGDAfbLWesvtqJfenThfKevcFsq1ifL70-BnibutxASyjoBc0Ps-JChYxHz0ZiF16NxdiaTRV7eYCAHX30pde7L6eeeAGYb7lVnjomQ33uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
با Pake هر وب‌سایتی را به برنامه دسکتاپ سبک تبدیل کنید
یک پروژه متن‌باز برای ساخت اپ دسکتاپ از سرویس‌های وب مثل ChatGPT، YouTube، Spotify و Discord و ... است.
✨
قابلیت‌ها:
•
🔹
تبدیل هر وب‌سایت به اپ جداگانه
•
⚡️
اجرای سریع‌تر و مصرف رم کمتر
•
🛠
ساخته‌شده با Rust و Tauri
•
📦
خروجی کم‌حجم، معمولاً چند مگابایت
•
💻
پشتیبانی از Windows، macOS و Linux
🔗
لینک:
GitHub
#OpenSource
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/6457" target="_blank">📅 12:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇸
ترامپ: شرکت Anthropic دیگه تهدید امنیت ملی نیست!
🤖
✨
به گزارش Axios، دونالد ترامپ بعد از دیدار با «داریو آمودی» (مدیرعامل شرکت Anthropic) در حاشیه اجلاس G7 اعلام کرد که دیگه این غول هوش مصنوعی (سازنده مدل‌های Claude) رو یک تهدید امنیتی برای آمریکا نمی‌دونه!
🔥
جزئیات و حواشی این توافق:
1️⃣
ریشه اختلاف:
قبلاً سر آسیب‌پذیری و باگ‌های خطرناک «جیلبریک» (Jailbreak) تو مدل‌های
Claude Fable 5
و
Claude Mythos 5
اختلاف شدیدی بین دولت آمریکا و این شرکت پیش اومده بود.
2️⃣
اقدامات قبلی دولت:
وزارت بازرگانی آمریکا تو ۱۲ ژوئن محدودیت‌های شدیدی اعمال کرده بود تا دسترسی تکنسین‌های خارجی به این مدل‌ها محدود بشه.
3️⃣
همکاری و چارچوب جدید:
الان Anthropic با درخواست‌های اصلاحی دولت کاملاً راه اومده و کاخ سفید به همراه چند نهاد امنیتی در حال تدوین یک چارچوب فنی دقیق برای ارزیابی خطرات مدل‌های هوش مصنوعی هستن.
﻿
⚙️
سیاست کلی آمریکا در قبال AI:
ترامپ تاکید کرده که هدف اصلی، حفظ برتری بی‌چون‌وچرای آمریکا تو رقابت هوش مصنوعی با چینه و اصلاً قصد نداره با بستن یا تصاحب شرکت‌های داخلی، جلوی رشد این صنعت رو بگیره. البته این رو هم اضافه کرده که در شرایط اضطراری، از استفاده از قوانین سخت‌گیرانه نظارتی (مثل قانون تولید دفاعی) چشم‌پوشی نخواهد کرد.
🔵
@ArchiveTell
| Bachelor
⚡️
#Anthropic
#Claude
#AI
#USA
#TechNews
#Security</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/6456" target="_blank">📅 10:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2SQwsMx_y9jlYBTN63E-q2JvKD99GkWw5nC9_DKYjYYhvT0HQ34YZH5L21rgAq-g1vRA8_mqFsVtzgAW_ZKkFrH8IPCeWToxii6s2KNBXRvpGHTlchFbQO621n7XJRCjcwdKQX7kX7HGupw8sEFvCGhkiTEAQQYisKtSrEIf7miedf2JGYplP2LyjrHu5yI55xg_JlP3bOeknlztONZ4KsJSJuBZwibvuPu17XAaI_stEEYnwvlPfpIAWwZWuuGfVBlGSqOymk_ccQVqTGCCdfm9O8NNc3W9IZ4DMZmXXl7bgdyygf066H8K1ESBtnnhciGGuzatukF0KU3hXuBLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">KillerPDF
جایگزین متن‌باز و سبک برای Adobe Acrobat
📄
✨
ویژگی‌ها:
•
🪶
مخصوص ویندوز 10/11 با حجم حدود ۶ مگابایت
•
✏️
ویرایش متن داخل PDF
•
🔗
ترکیب چند فایل PDF
•
📑
استخراج صفحات انتخابی
•
🖊️
نقاشی و افزودن امضا
•
🔒
اجرای کاملاً محلی، رایگان و بدون تبلیغات
🔗
لینک:
GitHub
#OpenSource
#PDF
#Windows
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/6455" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚀
مدل جدید Janus Pro از DeepSeek منتشر شد؛ پیشتازی در تولید تصویر!
🎨
✨
استارتاپ هوش مصنوعی چینی DeepSeek به‌تازگی گزارش فنی مدل متن‌باز جدیدش به نام
Janus-Pro-7B
رو منتشر کرده. بر اساس بنچمارک‌ها، این مدل در زمینه تبدیل متن به تصویر (Text-to-Image) تونسته عملکردی بهتر از رقبای قدرتمندی مثل DALL-E 3 (از OpenAI) و Stable Diffusion از خودش نشون بده!
این مدل در واقع نسخه ارتقایافته مدل Janus هست که اواخر سال گذشته معرفی شده بود.
🔥
ویژگی‌ها و بهبودهای کلیدی:
1️⃣
کیفیت و پایداری بالاتر:
با بهینه‌سازی فرآیند آموزش، ارتقای کیفیت داده‌ها و بزرگ‌تر شدن سایز مدل، جزئیات و پایداری تصاویر به‌شدت بهبود پیدا کرده.
2️⃣
تغذیه با داده‌های غنی:
در این نسخه از ۷۲ میلیون تصویر ساخته‌شده (Synthetic) باکیفیت در کنار داده‌های واقعی استفاده شده که خروجی‌ها بصری بسیار جذاب‌تری رو تولید می‌کنه.
3️⃣
مدل ۷ میلیارد پارامتری:
این مدل با ۷ میلیارد پارامتر، درک بسیار بهتری از دستورات (پرامپت‌ها) داره و سرعت و دقت تولید تصویر رو به سطح جدیدی رسونده.
📉
تاثیر دیپ‌سیک بر بازار تکنولوژی:
جالبه بدونید اپلیکیشن دستیار DeepSeek (مبتنی بر مدل قدرتمند V3) اخیراً رتبه اول اپلیکیشن‌های رایگان اپ‌استور آمریکا رو فتح کرده!
موفقیت‌های خیره‌کننده دیپ‌سیک و صدرنشینی مدل V3 تو جدول مدل‌های متن‌باز، حتی باعث شد تا سهام غول‌هایی مثل Nvidia و Oracle در روز دوشنبه با افت مواجه بشه. (شرکت‌های OpenAI و Stability AI هنوز به این خبر واکنشی نشون ندادن).
🔵
@ArchiveTell
| Bachelor
⚡️
#DeepSeek
#JanusPro
#AI
#DALL_E
#StableDiffusion
#TechNews</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/6454" target="_blank">📅 02:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fl5oHHnYxmLOhmdIB0ZdmzHAmz-3O12BF7xBLsnQXDDCWx97-IA8c51uyP69SNLtIAjwUH4HPc2GoqaOhzCUrWkbkFUhZrVGim7ViphLyLzp0Hx_wakZLDJ08n7Fd4cXckLaAYyTEEEmsBkrX5EmKUN8VhWgj9a5ug-wcgglsXNZnYpRlfY-z7SPqDRpv95HUtSsYbl0hPxX-o8JYOXX99WBorMbh_JMw6tO2j_qEIIHfJg8LmnBXw6nhKixn9mbnxoYlQKVARSpYXk3vDaq77MPan72vHEW99ObA9gZfEezUDPZS_wRm38FNv8N-zhqCN_ICv9GejiTdkKBOPrqoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g6pL4zP9f4_Ra6IgYpgZKrmLwVHolm6ztnvWE6Sw0ey_74YNxK1CB2JO9mx48iSLT4NT2PHtUjZ3kdH2pRkli4-cFp1qwc-MFsh-837MUYqV7CbrAiDJN4H1U9yGG4bvbzf5oRj7fEyo6uM-hoRtqx4xBpdQbBnpas3-uj23iA1RFHiCPOqsIc00qBgLVDvLrRRQkYf4Qol1dkDc2rO5DITK48FuD7qAuLOouBYTEQkGLFNixNY1VDeTDa4_Xy2MX-tcYnh4vdRl4JddjTSJEgaYIOx9GGT7dUwnLIsNs6HKNAlQJX0dawqMIwat6uSTWK2GfHTlyrYZVPx65uaMLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Product photography on a solid sky-blue background, soft studio lighting, no shadows.Product photography on a solid sky-blue background, soft studio lighting, no shadows.
Two thick, fluffy, plush terry towels are neatly folded and stacked one on top of the other, deep soft folds, thick looped pile texture. Top towel: white with thin blue stripes. Bottom towel: solid cream. [product from uploaded photo] rests nestled inside a deep fold of the white-striped towel, partially sunken into the fluffy fabric. [product from uploaded photo] lies diagonally inside a fold of the cream towel below.
Water droplets cover both products, fresh just-rinsed look. Top-down angle, empty blue space above for text. Photorealistic, high resolution, sharp focus, no text, no logos, no people.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/6452" target="_blank">📅 02:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCQRk6hNN6DSWe0lvmY_vauOTzo23TV4YDwYeBv_54A3oqyELjcJpIMgzUB32pahIzX82_VPodaum7EayqESxHUkNmk57fAyos0clBqx7AMBKpmZf6BIvpGWy6CwaRUivB9Le3fTVm6r8Dz1lLcSe2QsoQ6GZzw6Swu3TYLyRZ-qtS2soHHt8VXfVpGs89pavj6UNP5m8iKu7xBAo5v9pPTJtlhGauEtfyMgDqDrcQHbWetkfpo_TstI93ZxAqanWyOq_UUx5UpqE8D8BuAdjc30HoZQ8vqP-u2X-3sWABnUv_6UMd6pbHkFdkn8RSt1WSWnkfPHRRRJcAiGv9iSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی BleachBit؛ ابزار قدرتمند، رایگان و متن‌باز برای پاکسازی سیستم!
🧹
✨
اگه به دنبال یه ابزار امن و کاملاً رایگان برای بهینه‌سازی و پاکسازی سیستم‌عاملتون (چه ویندوز، چه لینوکس) هستید، BleachBit یکی از بهترین گزینه‌ها برای حفظ حریم خصوصی شماست!
این ابزار با حذف فایل‌های اضافی، کش مرورگرها، کوکی‌ها، فایل‌های موقت (Temp) و لاگ‌های سیستم، هم فضای هارد دیسک رو آزاد می‌کنه و هم ردپای دیجیتالیتون رو به حداقل می‌رسونه.
🔥
ویژگی‌های کلیدی و پیشرفته:
1️⃣
خرد کردن فایل‌ها (File Shredding):
حذف دائمی و غیرقابل بازیابی فایل‌های حساس.
2️⃣
پاکسازی فضای خالی (Wipe Free Space):
پاک کردن کامل فضای خالی دیسک برای جلوگیری از ریکاوری اطلاعات قدیمی.
3️⃣
بهینه‌سازی دیتابیس‌ها:
فشرده‌سازی دیتابیس برنامه‌ها برای افزایش سرعت و عملکرد سیستم.
4️⃣
امکانات حرفه‌ای:
پشتیبانی از خط فرمان (CLI) برای اتوماسیون، اجرای پرتابل (بدون نیاز به نصب) و امکان تعریف رول‌های (Rules) اختصاصی برای پاکسازی.
🔗
لینک وب‌سایت و دانلود
🔵
@ArchiveTell
| Bachelor
⚡️
#BleachBit
#OpenSource
#Linux
#Windows
#Privacy
#Tools</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/6451" target="_blank">📅 23:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🌐
ارتباطات آفلاین، امن و غیرمتمرکز با Nomad Network (نسخه ۱.۲.۰)
🔗
لینک گیت‌هاب
پلتفرم
Nomad Network
پلتفرمی برای ساخت شبکه‌های مش آفلاین با رمزنگاری قدرتمند، محرمانگی پیشرو و حریم خصوصی است.
✨
ویژگی‌ها:
>
🔹
کنترل ۱۰۰ درصدی:
بدون ثبت‌نام، قوانین یا وابستگی به سرورهای متمرکز.
>
🔹
تکنولوژی LXMF و Reticulum:
مسیریابی همتا‌به‌همتا (P2P) و زیرساخت مش رمزنگاری‌شده.
>
🔹
انعطاف‌پذیری بستر:
اجرا روی امواج رادیویی تا کابل‌های نوری.
مناسب برای دور زدن محدودیت‌ها و ساخت شبکه‌های محلی ایزوله.
🔵
@ArchiveTell
| Bachelor
⚡️
#LXMF
#P2P
#Reticulum
#NomadNetwork
#Mesh
#MeshNetwork</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/6450" target="_blank">📅 21:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6449">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTzrqwpj5GbbdQORsCmRjzNzQP6qL5JkuuNapcf8ooSmfHEkbyPGyF6h3QLfaP02l20-T2v6J40QdsE-Rywd6pcavTwsbn6YYPqif9LMuVDn42apBvP-QyMfv0Qyl4MfBPaXo1FjMtO6wmL5HXMj-9pf06DQfPGPVZOnc9r4RNJHuiTiI0S-mcblcEZKzL-8bPEjDO9bo5kzGeGUOm1KfI-j-Z71ZoAXQnig43wr0CR5RuRSqRcciH2YfJ-RbBXH77tn-Ru9opIK9CTAJNBi76XI8MzqiT4Ewy2CDI5vP_Kfri6fr-wt5qU_NT8DPX3GkwG-_FdidkgmazYgb9_0jWTo4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6745de7d1a.mp4?token=pIkn8fZyP0deDw-UsERhNiTD4UbJtNTpUFZsbdE8W7z_dEGG4jL_2lKulXl_dEt_bYAoZA5DP-lySjBvRcGxwxrnE7QytqVChldlE5lRjPzJq0EZL6KhfBmF84Kn9ODGfZt72mim3VIPvSTWtBI56HqD18rPeQC-Ii1ziUgbzdowOTjGa65g7mZwYBrflMPopuvSnPNXE0FntedTdc7ydboc4NihDrYudL7VhTkmVmO4ogEbLWw-uYGpeUiNGzt7i8D6uC5fNi4tIdJkaESOzSbxEKZ8JHScFnkluUUWinLEAMfFhUWBCG5X_D6p3MJolGk0mJKe7nevDBR0rPCTzrqwpj5GbbdQORsCmRjzNzQP6qL5JkuuNapcf8ooSmfHEkbyPGyF6h3QLfaP02l20-T2v6J40QdsE-Rywd6pcavTwsbn6YYPqif9LMuVDn42apBvP-QyMfv0Qyl4MfBPaXo1FjMtO6wmL5HXMj-9pf06DQfPGPVZOnc9r4RNJHuiTiI0S-mcblcEZKzL-8bPEjDO9bo5kzGeGUOm1KfI-j-Z71ZoAXQnig43wr0CR5RuRSqRcciH2YfJ-RbBXH77tn-Ru9opIK9CTAJNBi76XI8MzqiT4Ewy2CDI5vP_Kfri6fr-wt5qU_NT8DPX3GkwG-_FdidkgmazYgb9_0jWTo4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Palmier Pro
ویرایشگر ویدیو نوآورانه و رایگان که با هوش مصنوعی کنترل می‌شود
📹
•
🔹
اتصال مستقیم Claude، Cursor و Codex از طریق MCP
•
🔹
برش، تنظیم ریتم، صداگذاری و افکت‌گذاری خودکار
•
🔹
درک رابط کاربری توسط AI بدون تنظیمات اضافه
•
🔹
ابزارهای جانبی برای تولید تصویر و ویدیو
🌐
Site
#AI
#VideoEditing
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/6449" target="_blank">📅 19:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gA0z_ug9vh-Kddrh4zTJBIn9lZ518kT-ngiemgZQ8zp1D_5CDpvCG9orpZglrpJ7mJppGr8vla92H7ksbAOvJUd0ijW-qt1kYBJ_GT2FwdIiJ73GEvpVneKyBdrybeel1Rd4UupivUD82ifgDwufwm_rcNYAUckf_D7rV3YpW4EiOhVJNh9s8eUwnxjbzGWjMO8__9vhoxC0LqYzkPIIC9DVK01W0jGCXsIp5IBFutuhsDh6QvZgjAJmtNyQrPZfrfnEZFL1caMoM3ZirKdkfPhjoFkTkzxGc_-12EcRQ0N_RWF2slACZlVNc1S1gFwNaKpKjWex3yAYw-GfK1nBlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اگه حوصله داکیومنت خوندن ندارید و یا پروژه‌ای داکیومنت درست حسابی نداره، به جای این‌که سر خودتون رو درد بیارید، یه سر به سایت DeepWiki بزنید و با کمک هوش‌مصنوعی، جواب سوال‌های خودتون در مورد رپوهای گیت‌هاب رو پیدا کنید. اون خودش داکیومنت و کد بیس رو کامل مطالعه می‌کنه و کار شما خیلی راحت‌تر می‌شه.
🔗
deepwiki.com
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/6448" target="_blank">📅 18:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AavWWt7mBVXN3FfiRJxpIZ2XR3MIRyICaSAvvKbQPbVGwXEQ-sXx1SjACF8V6FhhTYcQckszFZ_wFT5xzDb8ySBt3RdN__4E5AFZWk6cU-rxNuUm1KciyYwu1q73Mssesf1f3_egklKYwi0oKmDibNpAkZvlRr9-OhRkopypbe2XeIwIP-UR7e1rGoA9bPvZcbI7fVWn6FcTpHwaDIP8wG3SqDir6PaeFTmLxF1trcHbVcQ1U-GcQKMifWzP3dnUiogBHrjHvDgRTvu8nHvURNGs-66oFN2SeZH7iubTEu80ocaBB3FL_TzcyuzBQAVhMc8LGznSz7wVLv42BmN3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساخت موزیک رایگان
🎧
https://freemusiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/6447" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6446">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚀
آموزش استفاده از مدل‌های قدرتمند GLM در ابزار Claude Code!
💻
✨
اگر از Claude Code (ابزار برنامه‌نویسی محبوب مبتنی بر ترمینال) استفاده می‌کنید، الان می‌تونید با اتصال به پلتفرم Z.AI، مدل‌های بی‌نظیر سری GLM (به‌ویژه نسخه جدید
GLM-5.2
با کانتکست خارق‌العاده ۱ میلیون توکنی) رو جایگزین مدل‌های پیش‌فرض کنید!
🛠
مراحل راه‌اندازی سریع:
1️⃣
نصب Claude Code:
(نیاز به نصب Node.js 18+)
تو ترمینال وارد کنید:
npm install -g @anthropic-ai/claude-code
2️⃣
تنظیم API و متغیرها:
تو سایت
Z.AI
ثبت‌نام کنید و کلید API بگیرید. برای سیستم‌عامل‌های مک و لینوکس فقط کافیه اسکریپت زیر رو اجرا کنید تا همه‌چیز خودکار تنظیم بشه:
curl -O "https://cdn.bigmodel.cn/install/claude_code_zai_env.sh" && bash ./claude_code_zai_env.sh
(برای ویندوز باید متغیرهای
ANTHROPIC_AUTH_TOKEN
و
ANTHROPIC_BASE_URL
رو دستی توی سیستم ست کنید).
🔥
ارتقا به مدل ۱ میلیون توکنی (GLM-5.2):
به‌طور پیش‌فرض کلود کد روی مدل
GLM-4.7
تنظیم می‌شه. اما برای استفاده از نسخه
GLM-5.2[1m]
، فایل
~/.claude/settings.json
رو باز کنید و این مقادیر رو به بخش
env
اضافه کنید:
"CLAUDE_CODE_AUTO_COMPACT_WINDOW": "1000000"
"ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5.2[1m]"
"ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5.2[1m]"
⚙️
نکته حرفه‌ای در مورد قدرت استدلال (Effort):
با دستور
/effort
داخل محیط کلود کد می‌تونید قدرت تفکر رو تعیین کنید. اگه این گزینه رو روی
max
یا
ultracode
بذارید، مستقیماً به استدلال سطح Max در مدل GLM-5.2 متصل می‌شه که برای حل باگ‌ها و تسک‌های پیچیده عالیه.
💰
هزینه‌ها چطوره؟
استفاده از مدل GLM-5.2 تو ساعات اوج ترافیک (۱۴:۰۰ تا ۱۸:۰۰ به وقت پکن / ۰۹:۳۰ تا ۱۳:۳۰ به وقت ایران) ضریب ۳ برابر داره، اما تو ساعات غیرپیک (به‌عنوان آفر ویژه تا آخر سپتامبر) فقط با ضریب ۱ محاسبه می‌شه!
🔵
@ArchiveTell
| Bachelor
⚡️
#Ai
#Claude
#GLM
──────────────────────────────</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/6446" target="_blank">📅 13:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPvoA0tUzb9NQEAQ7emQvJGLmt9MfwaebBrXYndvYkzsjT1hGIEN-uLpuRCJ1w_B3kyOtk_8P548KV71wJJlNP09OUQsvJQx7Q-Q6tF-BvdwalP-bcQxdvOnLDumQkx1BPkfYIUlBoqE3dni2lOHLwk2F6ujEi4MEqEuh-dQjTdYEhrCki9i6GoXDTQDv5LHGL0sx5OgvRwh_M4b5vhyh-kGGHDJF4_C9Eivy_-j7Tlp13lROCR49Vnr_4UCkRCwFbqdAxYhw0CaaoT7YfCfg4InnCdu5EBWlB6y51mjS99vlnPhDUBKwD34_CoERIb76wSufT2wEqAAg-D9f8QjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
۶۷ کلید ترکیبی پرکاربرد در لپ تاپ و کامپیوتر
⌨️
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/6445" target="_blank">📅 01:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🎯
پروژه Universal Android Debloater
📝
این ابزار یه رابط کاربری گرافیکی (GUI) کراس‌پلتفرمِ نوشته‌شده با زبان
Rust
هست که با استفاده از ADB به شما اجازه می‌ده گوشی‌های اندرویدی
روت‌نشده
رو دی‌بلوت کنید (برنامه‌های اضافی و پیش‌فرض سیستم رو حذف کنید). نتیجه این کار؟ بهبود چشمگیر حریم خصوصی، امنیت و افزایش عمر باتری دستگاه شما!
──────────────────────────────
این پروژه متن‌باز (Open-Source) در واقع فورکی از نسخه اصلی Universal Android Debloater است که با تمرکز ویژه روی افزایش امنیت، سرعت و بهینه‌سازی مصرف حافظه توسعه داده شده و با حذف اپلیکیشن‌های غیرضروری، سطح حمله (Attack Surface) رو به حداقل می‌رسونه.
✨
ویژگی‌های کلیدی:
🔹
رابط کاربری ساده، روان و کاربرپسند
🔹
دارای یک لیست جامع و کامل از پکیج‌های سیستمی
🔹
قابلیت دی‌بلوت کردن دستگاه (حتی بدون نیاز به کامپیوتر)
🔹
دارای ویکی (Wiki) و مستندات کامل شامل آموزش راه‌اندازی، راهنمای استفاده و نحوه بیلد گرفتن از سورس‌کد
🛠
از نگاه فنی:
این برنامه با استفاده از زبان Rust و کتابخانه گرافیکی Iced ساخته شده تا تجربه‌ای بدون لگ و یکپارچه رو ارائه بده. از نظر حریم خصوصی هم خیالتون راحت باشه؛ هیچ دیتا یا اطلاعات کاربری جمع‌آوری یا ارسال نمی‌شه و تنها ارتباط خارجی برنامه، درخواست‌های (GET) به گیت‌هاب برای دریافت لیست پکیج‌ها و بررسی آپدیت‌هاست.
چه کاربر مبتدی باشید چه یک متخصص فنی، اگه می‌خواید گوشی‌تون رو بهینه‌سازی کنید، این ابزار یکی از بهترین گزینه‌هاست.
💡
حرف آخر:
با این ابزار، کنترل کامل عملکرد و امنیت گوشی اندرویدی‌تون رو دوباره به دست بگیرید!
──────────────────────────────
🔵
@ArchiveTell
| Bachelor
⚡️
#Github</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/ArchiveTell/6444" target="_blank">📅 00:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KW5rXI7eli36KVP2E_bXjgEGljGtdw3tnFkr-JFTxDFcr9fbwgt3Nh6YiWlWPSukx1-8eU4MdHaDiY-0_d8ktk1tZ268GMZ9O0lEsNZD3PN5obO15cesv6aysJUSJYdhTqUPeLjNOw8FSKjfexFccA0NIy_JN50GAdNPznTuvAjG72YD6_smfgLBFRp2EXqF3tzrV653c8xf3nblOTgDvHfGV7pm6FSF4htNRZ1oGTcWLnpurVwHqiGHx2bV-JKth1UMvNJEzY7Ob8TQeYLzXiRXqBgBrZu31snHKv5UF0JRgOe5psuGKhN3Z7_lsUXx5ymIZLvF8JZubFBZD103tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دانلود کامل ویدیوهای یوتیوب + ویرایش فوری بدون افت کیفیت
🎬
یک توسعه‌دهنده دانلودر شخصی خودش را متن‌باز منتشر کرده؛ ابزاری ساده برای دانلود و ادیت سریع ویدیوها.
✨
قابلیت‌ها:
•
🔹
دانلود ویدیو با کیفیت اصلی
•
✂️
برش، چسباندن و تقسیم ویدیو داخل برنامه
•
💻
اجرای کاملاً محلی روی سیستم
•
🆓
رایگان و متن‌باز
•
🧩
رابط کاربری ساده و کاربرپسند
GitHub
#OpenSource
#YouTube
#Downloader
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/ArchiveTell/6441" target="_blank">📅 19:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚀
آموزش اجرای GPT 5.5 xhigh در Codex روی ترمینال (کاملاً رایگان)
1️⃣
ثبت‌نام در Freemodel
وارد سایت
Freemodel
شوید
با حساب Gmail ثبت‌نام کنید
بعد از ورود، صفحه احراز هویت نمایش داده می‌شود:
🔹
گزینه 1: احراز هویت با شماره تلفن
🔹
گزینه 2: احراز هویت با تلگرام
✅
گزینه
Telegram Verification
را انتخاب کنید
🔗
وارد ربات تلگرام شوید و Start را بزنید
🎉
در این مرحله پلن Pro برای شما فعال می‌شود:
هر ۵ ساعت: ۱۰ دلار اعتبار
💰
هر هفته: ۶۶ دلار اعتبار
💰
2️⃣
ساخت API Key
وارد سایت شوید
از منو بروید به بخش
API Keys
یک API Key جدید بسازید و ذخیره کنید
3️⃣
نصب Termux (روی موبایل)
📱
اگر موبایل دارید، از Termux استفاده کنید
4️⃣
دستورات نصب در ترمینال
(
به
ترتیب وارد کنید )
1⃣
آپدیت Termux
pkg update && pkg upgrade -y
2⃣
نصب ابزارها
pkg install proot-distro git curl wget nano tar -y
3⃣
دسترسی به حافظه
termux-setup-storage
4⃣
نصب Ubuntu
proot-distro install ubuntu
5⃣
ورود به Ubuntu
proot-distro login ubuntu
6⃣
آپدیت Ubuntu
apt update && apt upgrade -y
7⃣
نصب ابزارهای ضروری
apt install -y sudo ca-certificates curl wget git nano gnupg lsb-release build-essential python3 make g++
8⃣
نصب Node.js
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt install -y nodejs
9⃣
نصب Codex
npm install -g @openai/codex
🔟
تنظیمات Codex
mkdir -p ~/.codex
cat > ~/.codex/config.toml <<'EOF' model = "gpt-5.5" model_provider = "freemodel" preferred_auth_method = "apikey" model_reasoning_effort = "high" disable_response_storage = true
[model_providers.freemodel] name = "freemodel" base_url = "https://api.freemodel.dev" wire_api = "responses" env_key = "OPENAI_API_KEY" EOF
🔘
تنظیم API Key
echo 'export OPENAI_API_KEY="کلیدتو اینجا بزار"' >> ~/.bashrc source ~/.bashrc
▶️
اجرای Codex
( با فیلترشکن خوب وارد شوید )
codex
✨
حالا Codex روی ترمینال شما آماده استفاده است
🚀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/ArchiveTell/6440" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-QBkzNDKixhoe2LpOXSFvbfBonQAAwSoFXMIrZKH7fQVYD3tALa9EWLdwTDkk8QPPckkP4U9W2oT1B0Yy-al19no0u7izDBn85EnznCTNvwZ-HgxJ9pOTxY9a5omgLm5bGyh4uZJ7S0LYj17Gxl694WZSc8V2U32cfiNtyoQYBW3NMkxHSE3JfHUBZJCEwvpXGkrL5Q-FzlWofNCYuJ_xocQ3pbFCOVemO__qRq2KUl9y6TH8kFNP0mjNZxiW6Kxty_kWg0SyCl6c1whnbuBUAVqJOOyNbF9xnGNMfdJy8CKPYLNM3KwJbf76c9ZaHpe3tDtSWzpLqGqVkjeonTeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
راک‌استار از کاور رسمی GTA VI رونمایی کرد ، پیش‌سفارش این بازی افسانه‌ای از ۲۵ ژوئن ( ۴ تیر ) آغاز خواهد شد.
#GTA6
#GTA
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/6439" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
