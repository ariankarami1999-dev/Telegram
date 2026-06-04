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
<img src="https://cdn4.telesco.pe/file/SEWLG2cllgDptZDZ_wAmwmNBHi0fU5Xs0HD_i2TttWIBiOG-7FY5YKZjYIRZ3ZH5S6HaofAu0vl6oxJVuEOwncF5lboa2TejPwPMnmdPNeiBTMujOIFiPxVDzcbaSirYB51j4a-bgW6b6j_O5dOTROx9xvm52u8qZXot_FAQ8ydEMLyjchKD6tIhA3q1MBg8rZ1P1rNj6Oec6eeOdM3ttq-521ciBiTDCxS26BfI8DwzsB1Nfu50AmRjuJPR_bzkT8G8tSnRpHUYbs_gv6-Hqon1Kgjz-k8MKgGzkh-W0HVsU6XEDv5Y8aCJhFYAhuxzdy1Otg9Oa0BM17TyE9iRgw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 17:08:24</div>
<hr>

<div class="tg-post" id="msg-6012">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: آزمایشی
🧭
نوع کمپین: عادی
👥
کاربران دریافت کننده: 0 / 50
💾
حجم تخصیص یافته به هر اکانت: 1 GB
⏰
مدت اعتبار اکانت ها: 1 روز
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 102 · <a href="https://t.me/archivetell/6012" target="_blank">📅 17:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6011">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
آزمایشی
🧭
نوع کمپین: عادی
👥
کاربران دریافت کننده: 0 / 50
💾
حجم تخصیص یافته به هر اکانت: 1 GB
⏰
مدت اعتبار اکانت ها: 1 روز
🟢
وضعیت: فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 162 · <a href="https://t.me/archivetell/6011" target="_blank">📅 17:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6010">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">💦
💦
سرور اختصاصی 1000 گیگابایت    اهدایی ادمین چنل
🔥
vless://75700dda-3aa7-4f8e-b978-2237516f84db@45.130.125.66:443?mode=auto&path=%2F476T682e67a4f84a3c838ca94R86273&security=tls&alpn=h2&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%…</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/archivetell/6010" target="_blank">📅 13:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6006">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/im7TP5zgpZKcxgOsTvezDdl1Kxh5rCFbHhKMxuxY_aUENsTc6yr5pjQ4sqFnUbDK_1EMzWjzkiTkuaEFBdkkMi4pUYjT4Jv9Fsn8iM3DrgqO8Lc_EMJ_ftcqSqOUgmbobSsc2j3aGa3Eynr--nMkfhjBDOJPk3WY_vjMmG6MojOqOAL4P5rUg97wTLu0viAxD3P2gbuF8oeWPrLBBecq-K3VJaBtpgpqiia9eOCvJ2emM3so9MjKxoMWVlnv97pmcLF7qiHn7tbhOhEs1AO1aT6YtuH9sx6mFSdsymJemvsUvg2_cORW8khtboFBgYk3s1FzaMAsG9StoXSxa9xDAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXqZw0SSNy4v5uNcvGvt9bv9Bgag67l0K4wuZ0NhhYhsz2Xir-_1n0sIRFqFU1Eohpl2pDbERnc5OwV4Tx_VzNcAwNGkPb35ewCpkslS2zhqL_0wa4WDjrFX5zesJ6TEUmizU4vw9gChnzg8gBLUgGft8uVNruqDcZNb7wL0WNnIFFWzsgIrGEen3cghM22w5g6ZlIollSLe6cGM7kHyJE0niDJvq04dQl4wl1Sgkhl5V_avg5WoaLihGURk06CcnnoypWVw-FIK_uaid3OIzD2mBHpF20P6HUesLanwE1L4Ud_Diq-wBO5_vNEsW0jACEHgXI7QHVVZTCrF3qOGkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CJXUKABpWo6V9hkUD7ObYc15067MrswMALjkuft0LEFFOE-TyX_nyOJsFWtifW1tUvqWPiQ-NFQuAQZl1RJJjdCUe552I4zxb2r6C53YxpobRcuyRDwHLK35PNhAhQwenKakBDZ6546YN3viUX7Fbf_JxbTtU3ZkreqXkbwA5LvXz1olW4173u-ZyaTTr3gowKBxbgIrYC5U7xab4iKGR_C77ilBaBQaznQFRL1X34tZVTqV7ZOsvAl_Erb56U9LFVXWaflrL3xVGQITJn-7BMianiaIkKmE0lqLmSzk-JwwEKIn3zdseRnkh8QbLneJpKe1OQUrAJOCDbVstAD97g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Nano
🍌
²
Faithfully restore this image with high fidelity to modern photograph quality, in full color, upscale to 4K
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/6006" target="_blank">📅 12:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6005">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">عملکرد بی نظیر جنریت عکس
Reve 2.0
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/6005" target="_blank">📅 12:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6004">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎓
اکانت Cursor Pro رایگان برای دانشجویان  دانشجوها می‌تونن ۱۲ ماه اشتراک Cursor Pro (به ارزش ۲۴۰ دلار) رو رایگان دریافت کنن و به مدل‌های GPT، Claude و Gemini دسترسی داشته باشن.
✅
بدون نیاز به کارت بانکی
📌
مراحل دریافت:  1. وارد سایت cursor.com/students شوید.…</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/archivetell/6004" target="_blank">📅 12:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6003">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🎓
اکانت Cursor Pro رایگان برای دانشجویان  دانشجوها می‌تونن ۱۲ ماه اشتراک Cursor Pro (به ارزش ۲۴۰ دلار) رو رایگان دریافت کنن و به مدل‌های GPT، Claude و Gemini دسترسی داشته باشن.
✅
بدون نیاز به کارت بانکی
📌
مراحل دریافت:  1. وارد سایت cursor.com/students شوید.…</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/6003" target="_blank">📅 12:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6002">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚀
ابزار V2RayEz — ابزار متن‌باز عبور از فیلترینگ مبتنی بر DPI
ابزار V2RayEz یک پنل وب محلی و تک‌فایلی است که مجموعه‌ای از ابزارهای شبکه را در یک رابط کاربری مدرن ارائه می‌کند. کافی است فایل اجرایی را اجرا کنید تا داشبورد مدیریتی در مرورگر باز شود.
✨
امکانات کلیدی:
• پشتیبانی از Xray و Sing-box
• تونل SNI با قابلیت‌های ضد DPI
• دامین-فرانتینگ سمت کلاینت
• کتابخانه مدیریت کانفیگ‌های V2Ray
• اسکنرهای CDN، SNI و IP
• پشتیبانی از Psiphon و Cloudflare Worker
• رابط کاربری فارسی و انگلیسی
• بدون نصب‌کننده و بدون تله‌متری
🔧
فناوری‌ها:
• توسعه‌یافته با Go
• پنل وب داخلی
• قابل اجرا روی Windows، Linux و macOS
• متن‌باز تحت مجوز MIT
گیت هابش:
https://github.com/macan-dev/EasySNI
آموزشش تو یوتیوب:
https://www.youtube.com/watch?v=Y3tVfMqgys4&t=28s
#OpenSource
#GoLang
#V2Ray
#Xray
#SingBox
#Networking
#GitHub
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/6002" target="_blank">📅 11:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6000">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎓
اکانت Cursor Pro رایگان برای دانشجویان
دانشجوها می‌تونن ۱۲ ماه اشتراک Cursor Pro (به ارزش ۲۴۰ دلار) رو رایگان دریافت کنن و به مدل‌های GPT، Claude و Gemini دسترسی داشته باشن.
✅
بدون نیاز به کارت بانکی
📌
مراحل دریافت:
1. وارد سایت
cursor.com/students
شوید.
2. با ایمیل دانشگاهی (.edu) ثبت‌نام کنید.
3. فرایند تأیید دانشجویی را تکمیل کنید.
4. اشتراک Cursor Pro برای شما فعال می‌شود.
⚠️
داشتن ایمیل دانشگاهی (.edu) الزامی است.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/6000" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5999">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کانفیگ اهدایی نامحدود از ممبر عزیزمون.....
🇩🇪
vless://6d3c8903-86c1-46e7-a5dc-b45823dec9a7@fmmgkzjac48e.dxdx5.com:9023?security=&encryption=none&type=grpc#gum0fyg1
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/5999" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5998">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دوستان کانفیگ رو آف کردم   یکم استراحت کنید  بعداً دوباره فعال میکنم  به بزرگی خودتون ببخشید...  @Sina_1090</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/archivetell/5998" target="_blank">📅 10:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5997">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کانفیگ اهدایی نامحدود.....
🇳🇱
vless://f29fb004-34cc-424d-96bf-af70190e6e3d@nert.96s.ir:80?encryption=none&extra=%7B%22headers%22%3A%7B%22obito%22%3A%22obito%22%7D%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPadd…</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/archivetell/5997" target="_blank">📅 10:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5996">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-obito.conf</div>
  <div class="tg-doc-extra">532 B</div>
</div>
<a href="https://t.me/archivetell/5996" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وایرگارد...
@Sina_1090</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/5996" target="_blank">📅 09:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5995">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">40 گیگ کانفیگ سرور ترکیه..
🇹🇷
vless://8df1328a-9ba8-4135-9b6e-b00f0b7455de@obito.96s.ir:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&host=obito.96s.ir&mode=auto&path=%2Fobito&pbk=qYkuXrr6eqa8zJz6r_AWFaJCFjMF6fe4_8yl7Vo9-AY&security=reality&sid=54bd5de0&sni=www.yahoo.com&spx=%2FUicYvHKFefj2yqr&type=xhttp&x_padding_bytes=100-1000#OBITO-.obito-40.00GB%F0%9F%93%8A
تست کنید رو همراه و ایرانسل وصله واسم...
@Sina_1090</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/5995" target="_blank">📅 09:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5994">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کانفیگ اهدایی نامحدود.....
🇳🇱
vless://f29fb004-34cc-424d-96bf-af70190e6e3d@nert.96s.ir:80?encryption=none&extra=%7B%22headers%22%3A%7B%22obito%22%3A%22obito%22%7D%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPadd…</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/5994" target="_blank">📅 09:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5991">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knrBAAmXBkZKBvel6aNT-ACP_EaYOhmop__fFOv1kUHiTgkZCfuOTi_HYUS1PYkVZhjl20rGO999fMfN696i4YqNz-gzk4Hq7rUJUgOYc-6yBqCtOsuAe6BT1Ih1OfB3jG7EhgIje726UyWxZPr1A1SwO_3rS3IdBpUYXTR_RthMhwJd-sAf_RHgh4dQB6cTYVS6pQCQKA11RPX98RulrzSouYp_7JLpPwZu3xPjfkT8IKZkzL8tcJyQ3AApNS112ohYirOjimuhOqpPnR6GtvWEZJfhX9G6UIDW6sA6Byf7RkOioA9Jyaco31lDiEsEMZz4TEjlvzTyH4s6QYuaiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RUvSEVIx6ONYQtOQtGoMwRvF36o1Qb2LM36jJCYNhWdxMX3kv3zGjgQWfphkhNJR1laESHxeY1703gNi7Ef0M15655EGRBGclmol2gOUHWOcRdesjiryDeCVEF6iyCQDf3aiwKhl3WwECgP2bw1QmbUoY6aRkpQJlu0Gcmx5GrWPagj-quhKm-w3T5PYYaRSr4BQc4MFfnO4vVhSOXhAD5nw2dfcw6OYGIXrTGQsnK7Gt0xcfLTkOflu6vcoC-ZGEBgHT1RiW9fxTpJHfGuS-PiHNAvuTDeL5Yu1ggy1hk0n4M5esxAaCWF9rKtz06xdpUXPA5E690tgcKuk_AXahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L2GVQudLlMZGjyrYEbceFQr3pKpfRwWNZvYQsBg9MJKzoxiDPrjEVYIEJqCoE2n9zeIPco5eoyqZweXSvYhIxbsL-Z7dPO74iN8fQrDmjvx9XIqOx8dMqXxiy34De4CEpG87tnq_weXrT0qAnRcPVHSLePA2c1mZEW5y0hE7-rwDbIHzHrCcWV36VtIRmoHaoLuCGgF6kxeLUjiXsQfG6GQrhU2MdZyl3KgukhV-YeXkXTtGl8-YatWDws_haIIGRvyotDiU55oN4JL_geantLFG7Q4tL4_Omc5F5m49KIvo1vYlBUJ13c5A2u7Hz_ThhqH-v29tJO7BLp9BeTLYaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Ideogram 4
منتشر شد
https://ideogram.ai/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/5991" target="_blank">📅 08:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5989">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یک استارتاپ به تازگی ابزاری برای تصویرسازی با هوش مصنوعی ساخته است که در جهان رتبه دوم را کسب کرده است - بالاتر از گوگل و Midjourney.
👀
🎨
نام آن Reve 2.0 است و همین حالا منتشر شده.
آنچه این ابزار را واقعاً متفاوت می‌کند، نحوه عملکرد آن در پشت صحنه است. هر تصویر به صورت کد نمایش داده می‌شود - به این معنی که هر عنصر به طور کامل قابل ویرایش، قابل دسترسی و تحت کنترل شماست.
بهترین دقت متن روی تصویر در میان تمام ابزارهای هوش مصنوعی فعلی.
رایگان با محدودیت های روزانه
این ابزار در رتبه دوم جدول رده‌بندی Image Arena قرار گرفته و از Nano Banana 2 گوگل پیشی گرفته است -
🔗
https://reve.art
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/archivetell/5989" target="_blank">📅 08:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5987">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پروکسی متصل .
https://t.me/proxy?server=87.120.186.57&port=1337&secret=77806a58288a20e94ae9424dc0a4eb60
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/5987" target="_blank">📅 08:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5986">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@archivetell.npvt</div>
  <div class="tg-doc-extra">7.6 KB</div>
</div>
<a href="https://t.me/archivetell/5986" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پخشش با شما
❤️‍🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/archivetell/5986" target="_blank">📅 06:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5985">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کانفیگ اهدایی نامحدود.....
🇳🇱
vless://f29fb004-34cc-424d-96bf-af70190e6e3d@nert.96s.ir:80?encryption=none&extra=%7B%22headers%22%3A%7B%22obito%22%3A%22obito%22%7D%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&host=nert.96s.ir&mode=auto&path=%2Fobito&pbk=bPC70WXyPEUh8l4LSTdbACXer6Fhpw4tVwoMYLD_oxc&security=reality&sid=9d7b90df3283d95a&sni=www.yahoo.com&spx=%2Fy8WnnkZfDsyXZ8T&type=xhttp&x_padding_bytes=100-1000#Obito
همراه متصل
با نت های دیگه هم تست کنید...
@Sina_1090</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/5985" target="_blank">📅 04:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5984">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کانفیگ اهدایی نامحدود از دوست عزیزمون....
vless://d2ae2b13-2532-4e95-90bf-8b94e856b51b@testhol.shompolexy.shop:443?type=tcp&encryption=none&path=%2F&host=www.speedtest.net&headerType=http&security=reality&pbk=7ucgFrVZ0LjQV554F0ogN9sKlt2yuqiTinH1ptSdkk0&fp=chrome&sni=www.samsung.com&sid=d7002a619306ab3d&spx=%2F#MOHRAZ-kxl1tmid
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/archivetell/5984" target="_blank">📅 03:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5983">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">صبح واستون سرور ترکیه،
و وایرگارد می‌زارم عشق کنید...
@Sina_1090</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/5983" target="_blank">📅 02:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5982">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">100 گیگ کانفیگ اهدایی ....
🇩🇪
vless://5bcaed47-9082-4e34-ada4-1d7d17066f70@obito.homan554.ir:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&host=obito.homan554.ir&mode=auto&path=%2Fmarg&pbk=Fdp4TeOj4ZdzucCR4dEoxNWtyS2gWnUg0q819GYENQU&security=reality&sid=798210477fa214fd&sni=www.yahoo.com&spx=%2Fa93dgM4XpaaJ2IB&type=xhttp&x_padding_bytes=100-1000#Obito-100.00GB%F0%9F%93%8A
https://obito.homan554.ir:2096/sub/8y88zn5phoxy4lhe
@Sina_1090</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/5982" target="_blank">📅 02:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5981">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">@MohrazServerBot
دریافت 1 گیگ کانفیگ رایگان (از بخش تست)
ظرفیت‌محدود
🥳</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/archivetell/5981" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5980">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/331520d70a.mp4?token=bauSIi_YgXvC1tFkp5d0HGKs-2w9Jv-TmDXKgglbJtcyi0gmxN4af6KGqpZnYrB6jUNqwUmvy0TCJLId9camgQrMfx_v5gTu35G13mh8WqbojKwVIHeHlRacFlWI_p7ZHDsvqX4isi-3hyYEqnYbwABTBWOXhRbD_Jm7hxgNwWgDAmwet5kveT_LXt2sU8fjTxQI7z-AgyD2npvWkww16M41aqpRqa8bkJF2HTTikq-DaYZHW6cbtijU7fysNd4tvUFVFJR-msEFl55AAae8ZBf-owY6b7acExLEnI6d9RDR9GIVGBhEt39NYwZRsot5qH00h93I2477Xu0sUp-6_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/331520d70a.mp4?token=bauSIi_YgXvC1tFkp5d0HGKs-2w9Jv-TmDXKgglbJtcyi0gmxN4af6KGqpZnYrB6jUNqwUmvy0TCJLId9camgQrMfx_v5gTu35G13mh8WqbojKwVIHeHlRacFlWI_p7ZHDsvqX4isi-3hyYEqnYbwABTBWOXhRbD_Jm7hxgNwWgDAmwet5kveT_LXt2sU8fjTxQI7z-AgyD2npvWkww16M41aqpRqa8bkJF2HTTikq-DaYZHW6cbtijU7fysNd4tvUFVFJR-msEFl55AAae8ZBf-owY6b7acExLEnI6d9RDR9GIVGBhEt39NYwZRsot5qH00h93I2477Xu0sUp-6_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
اجرای مستقیم بازی‌های کلاسیک و نوستالژیک در مرورگر
اگر به بازی‌های قدیمی کنسول‌هایی مثل سگا، پلی‌استیشن ۱، گیم‌بوی و NES علاقه دارید، وب‌سایت
gam.onl
یک آرشیو کامل و کاربردی برای شماست.
مزیت اصلی این سرویس این است که برای اجرای بازی‌ها نیازی به دانلود فایل، نصب شبیه‌ساز (Emulator) یا درگیری با تنظیمات پیچیده ندارید؛ همه‌چیز مستقیماً روی مرورگر شما پردازش و اجرا می‌شود.
📌
ویژگی‌های این وب‌سایت:
*
بدون نیاز به نصب:
اجرای سریع بازی‌ها در خود مرورگر.
*
آرشیو جامع:
پشتیبانی از کنسول‌های نوستالژیک و پرطرفدار قدیمی.
*
سازگاری بالا:
قابل اجرا روی مرورگرهای موبایل، تبلت و دسکتاپ.
*
کاربری ساده:
فقط کافیست وارد سایت شوید، کنسول مورد نظر را انتخاب کرده و بازی را شروع کنید.
🌐
لینک سایت:
https://gam.onl
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/5980" target="_blank">📅 01:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5979">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy0ubqZ-ODCwYTdpKD9-H1o0azFJLW83Wkx2DzVoJfnUkSlhhzqSjvQaD51q21LhvVJN3s2_uY7Mrh0snGeAMKSNbFIKCwcOjO9ycCi0VBAuqPL7CsToLEHXExq8d5CyWd7lomPzJRPlqkLS2WsrORnpJqsdZr9dact76DNA_WgbgcMPnZJVlNODUrYKauI4Eeay2ui5IzXCs3AM4paIrahwP5GwLdxTWbf0W4eQ2UTVi4FCDTRSOcYLhqpZezNBeWpf-CmwPU_33NtDMs-VWwfbRj-3zAblSMTWowZsgXEQ8xMg-jv3lZwNFc1gF0vdGOKMTVM94AfEpldzp_4Dow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
در حالی که اکثر افراد به صورت دستی گیت‌هاب را زیر نظر دارند، Trendshift به طور خودکار پروژه‌هایی را که همین حالا در حال محبوب شدن هستند، شناسایی می‌کند.
1️⃣
رتبه‌بندی مخازن ترند در بازه‌های روزانه، هفتگی و ماهانه.
2️⃣
جریان انتشارها از توسعه‌دهندگان و سازندگان پروژه‌ها.
3️⃣
جستجوی هوشمند بر اساس حوزه‌های فناوری و دسته‌بندی‌ها.
4️⃣
فهرست‌های جداگانه بهترین عوامل هوش مصنوعی، دستیارهای کد و سایر راه‌حل‌های محبوب.
یک روش عالی برای دست داشتن بر نبض گیت‌هاب و از دست ندادن نسخه‌های واقعاً جالب.
https://trendshift.io/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/5979" target="_blank">📅 23:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5978">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">معرفی ابزار AutoWorker؛ راه‌اندازی خودکار پروکسی روی کلادفلر
سلام دوستان
🌹
همان‌طور که می‌دانید، پیکربندی پروکسی‌های مبتنی بر کلادفلر ورکر (مانند پروژه‌های خانواده Nova) معمولاً نیازمند طی کردن مراحل مختلفی به صورت دستی است؛ مراحلی مثل ساخت فضاهای KV، جایگذاری کدها، پیدا کردن Proxy IP سالم و تنظیم پنل.
ابزار
AutoWorker
توسعه داده شده تا تمام این فرآیندها را ساده و کاملاً خودکار (Automated) کند.
📌
قابلیت‌های اصلی AutoWorker:
*
بدون نیاز به پیش‌نیاز:
برای اجرای این ابزار نیازی به نصب Node.js، پایتون یا محیط‌های برنامه‌نویسی ندارید.
*
روند کاملاً خودکار:
از ساخت ورکر تا اعمال تنظیمات پنل و دریافت آی‌پی تمیز، بدون نیاز به دخالت کاربر انجام می‌شود.
*
حفظ امنیت اکانت:
این ابزار پسورد شما را دریافت نمی‌کند، بلکه از طریق پروتکل OAuth 2.0 یک توکن دسترسی موقت برای اعمال تغییرات می‌گیرد.
*
پشتیبانی از پلتفرم‌ها:
فایل اجرایی مستقل برای ویندوز، لینوکس و مک در دسترس است.
🛠
نحوه استفاده:
۱. فایل برنامه را متناسب با سیستم‌عامل خود از گیت‌هاب دانلود کنید.
۲.
نکته بسیار مهم:
پیش از اجرای برنامه،
فیلترشکن خود را کاملاً خاموش کنید.
روشن بودن فیلترشکن در روند اسکن و دریافت Proxy IP اختلال ایجاد می‌کند.
۳. برنامه را اجرا کنید. مرورگر شما باز می‌شود تا ورود به اکانت کلادفلر را تایید کنید.
۴. پس از تایید، به ترمینال (محیط برنامه) برگردید و منتظر بمانید تا مراحل تکمیل شود. در نهایت، اطلاعات ورود به پنل و
لینک سابسکریپشن (Sub)
برای استفاده در کلاینت (مثل v2rayNG) به شما نمایش داده می‌شود.
📥
لینک دانلود فایل‌های اجرایی از گیت‌هاب رسمی پروژه:
[لینک صفحه Releases در گیت‌هاب AutoWorker]
https://github.com/marketnoobtrader/autoworker
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/5978" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5977">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN-Z1SRaS5671cIoFkx-vUx7ryhb1M18r73t6TEw6X6lFHxmDWmt2khCchx-sJQUVb6gL1T6jX9hb3sKrdU_F7QqBd7U5fVDznWiwgUYYztK3zjzynUrTiroBxntRODel3TCKsCo3gbgNW5IYqOacUggI3YTSksDiOOvDAFawc6jGFeXRm-It8pn-Rfv2We9CUnbrhu8LU0SznXFe-o0zIIG-7J7TgeczDwLqOXztptecdKyKQ3PSR37dMgX9EoU7KILDWnluJoG9P4UfgkV-SToYBuGD-s-2Pg2D5DXAm0rX02uTp2qg0hNkyC3fjPxgvWf7i1t53MgFX5OLKOTyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
متن‌های هوش مصنوعی را کمتر کلیشه‌ای و طبیعی‌تر می‌کنیم — اپلیکیشن AI-Text-Humanizer نوشته‌های شبکه عصبی را به سبکی زنده‌تر و خواناتر تبدیل می‌کند.
🕤
افزودن انتقال‌ها و ارتباطات بین افکار، با حفظ معنا و ساختار.
🕤
جایگزینی کلمات ساده با کلمات تخصصی‌تر.
🕤
کمک به دور زدن شناسایی‌کننده‌ها و بررسی‌های هوش مصنوعی.
🕤
نصب با چند دستور ساده — بدون نیاز به برنامه‌ها و اشتراک‌های اضافی.
https://github.com/DadaNanjesha/AI-Text-Humanizer-App
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/5977" target="_blank">📅 21:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5976">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/486b42ea05.mp4?token=rDmtGtFrbTj3pf-Vn5kWTLmg3XzyZQGwEGA0dEsjD1M7jweSAOuRC5uMY7mCCc-Lk6wYfuZ1z6T8ig57Yy5Lbf32BAVdcbYJlaw4epmM8lPnMSkVDysdteA4DJ5tvjHHidHWzXz_kW0q4_iVHyfzZCS9CSi4MUqHe2ReYyChwXxKMUdvgWfg2-RfZjLkDtUBeSlcwaWf5W1lwUK49d6cog2zgMmFGjbSENajXuY-uEC1BTwBniyXmOqpdpzFNHgq8pQ-pLEbfedIZIII7G_MyQBippd_N6Lk2l32ATFvUW1X2vC7WK_AxQhZvExTZpEnl8ENlJX0AusKDfOOyBHJJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/486b42ea05.mp4?token=rDmtGtFrbTj3pf-Vn5kWTLmg3XzyZQGwEGA0dEsjD1M7jweSAOuRC5uMY7mCCc-Lk6wYfuZ1z6T8ig57Yy5Lbf32BAVdcbYJlaw4epmM8lPnMSkVDysdteA4DJ5tvjHHidHWzXz_kW0q4_iVHyfzZCS9CSi4MUqHe2ReYyChwXxKMUdvgWfg2-RfZjLkDtUBeSlcwaWf5W1lwUK49d6cog2zgMmFGjbSENajXuY-uEC1BTwBniyXmOqpdpzFNHgq8pQ-pLEbfedIZIII7G_MyQBippd_N6Lk2l32ATFvUW1X2vC7WK_AxQhZvExTZpEnl8ENlJX0AusKDfOOyBHJJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
Perplexity به ویندوز می‌آید
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/5976" target="_blank">📅 21:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5975">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXWIBNg6ESpgGhdrBs1heS7UJDO65UV6leHrSVa1jQD8lPtS8uuvDtNrUCyM0xOOCGLVbZiAksNqmp2C1ezVo2WFQ1Y-I-G48wMBnI8RraI7Gb5etZcDy6Xs6vIj8sYrR9GLHsnZm3oPJy6gmtAr4bFa5CZjuJgT3KPf8_TifoMekIkn8icr3zEbyVdskccZzbmcelT6Fq8MzoYNV5tR6tfJ-SRbINJlMvKXWobcK2AfOZmRLKoYEmxvfZD6nwOtK3vyBwqbdm3jWHgKSWKvf9KNsnOjqL5kYti3TBgU6vT0HSwc95CbkZmvXLC_AZtSbz0xO0hIvsp_sOWe2L3mYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکنون می‌توان افراد را از طریق وای‌فای با دقت تقریباً ۱۰۰٪ شناسایی کرد.
محققان
سیستمی به نام BFID توسعه داده‌اند که افراد را بر اساس ویژگی‌های بدن و الگوهای حرکتی آنها با استفاده از سیگنال‌های معمولی وای‌فای تشخیص می‌دهد. نیازی به دوربین یا سخت‌افزار خاصی نیست.
قسمت ترسناک ماجرا چیست؟ این سیگنال‌ها را تقریباً هر دستگاه مدرنی در نزدیکی می‌تواند دریافت کند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/5975" target="_blank">📅 21:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5974">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">trojan://humanity@104.19.229.21:443?allowInsecure=1&alpn=http%2F1.1&host=www.calmloud.com&path=%2Fassignment&sni=www.calmloud.com&type=ws#Cloudflare%20
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/5974" target="_blank">📅 21:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5972">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🎬
🔥
ساخت ویدیو با هوش مصنوعی Seedance 2.0 رایگان شد!
مدل جدید Seedance 2.0 که توسط ByteDance توسعه داده شده، حالا از طریق Dreamina در دسترس قرار گرفته و امکانات جالبی برای تولید ویدیو ارائه می‌دهد.
🤖
✨
🚀
قابلیت‌ها:
🎥
تبدیل متن، عکس و ویدیو به کلیپ‌های 1080p
🖼
پشتیبانی همزمان از چندین تصویر، ویدیو و فایل صوتی
🎭
حفظ چهره و شخصیت در تمام صحنه‌ها
🎙
پشتیبانی از صدا، دوبله و لیپ‌سینک
🎬
انتقال استایل و افکت‌های سینمایی به ویدیوهای جدید
📱
مناسب برای ساخت محتوا، تبلیغات، انیمیشن و شبکه‌های اجتماعی
💡
فقط کافیست متن یا تصاویر مرجع را وارد کنید تا AI بقیه کار را انجام دهد.
🌐
لینک:
https://dreamina.capcut.com
@ArchiveTell
🍷
Bachelor</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/5972" target="_blank">📅 20:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5971">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">💦
💦
سرور اختصاصی 1000 گیگابایت
اهدایی ادمین چنل
🔥
vless://75700dda-3aa7-4f8e-b978-2237516f84db@45.130.125.66:443?mode=auto&path=%2F476T682e67a4f84a3c838ca94R86273&security=tls&alpn=h2&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%2210-50%22%2C%22xPaddingHeader%22%3A%22apinode%22%2C%22xPaddingKey%22%3A%22domow%22%2C%22xPaddingObfsMode%22%3Atrue%7D&insecure=0&host=ticket.fibernet1.qzz.io&fp=chrome&type=xhttp&allowInsecure=0#ArchiveFast
مخصوص همراه اول و مخابرات
💦
💦
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/5971" target="_blank">📅 20:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5969">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b91beb31b.mp4?token=fFq_jvovYLCp7EFAXuFRJTkw8ABGTEkteac0Dgq6eUX2rcJeuplezBcuFfhG2wpjlHvMjWVmYVEAZ36w38k0yIjVLDJ1tRHSk7faaILKAj7Svqf68i9FdHaaizn1uFAST25volMsdcQAupl5F4WEj9MzKMi9-1N5bhpe2oafrnMWczhSx2A0WHDJNUkagoHCCISf0SzQbvXvgTckmtr98bQYEwmAqcC_F_d2sNHMw1U3OcdsBvXzSccvNGk1TrrRdUeQ4084Yn90oH6LDoZW3a65WJSNXoDp4Bw2vsbLwrVr8h7VKVA5-QIBg0P83yMpZsr9twdOHFuPCMYY6T44qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b91beb31b.mp4?token=fFq_jvovYLCp7EFAXuFRJTkw8ABGTEkteac0Dgq6eUX2rcJeuplezBcuFfhG2wpjlHvMjWVmYVEAZ36w38k0yIjVLDJ1tRHSk7faaILKAj7Svqf68i9FdHaaizn1uFAST25volMsdcQAupl5F4WEj9MzKMi9-1N5bhpe2oafrnMWczhSx2A0WHDJNUkagoHCCISf0SzQbvXvgTckmtr98bQYEwmAqcC_F_d2sNHMw1U3OcdsBvXzSccvNGk1TrrRdUeQ4084Yn90oH6LDoZW3a65WJSNXoDp4Bw2vsbLwrVr8h7VKVA5-QIBg0P83yMpZsr9twdOHFuPCMYY6T44qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔎
افزونه SwitchSearch — جابه‌جایی بین موتورهای جستجو با یک کلیک
اگر از محدود شدن به یک موتور جستجو خسته شده‌اید، SwitchSearch یک افزونه متن‌باز مرورگر است که امکان جستجوی سریع در چندین موتور مختلف را فراهم می‌کند.
✨
امکانات:
• پشتیبانی از Google، Brave، DuckDuckGo، Perplexity، ChatGPT، Wiby، Marginalia و Yandex
• امکان افزودن موتورهای جستجوی دلخواه
• جستجوی معکوس تصویر با Google و Yandex از طریق منوی راست‌کلیک
• باز کردن نتایج در تب جدید یا چند موتور به‌صورت هم‌زمان
• کاملاً متن‌باز و قابل شخصی‌سازی
🎯
مناسب برای:
• پژوهشگران و دانشجویان
• کاربران علاقه‌مند به حریم خصوصی
• افرادی که می‌خواهند از «حباب اطلاعاتی» موتورهای جستجو خارج شوند
• جستجو در منابع کمتر شناخته‌شده وب
https://github.com/thedmdim/switchsearch
#OpenSource
#SearchEngine
#BrowserExtension
#Privacy
#GitHub
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/5969" target="_blank">📅 19:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5967">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4hp6OU1g20xygIoouDoczVerw08yoGsCkBu9hQeKznJBgAPCOgcVUYsviDmk7790oyR5o7j64HrIXLLIReFebO1G0m59Z5DBujrULRmUI9RnZ8fCeOkBoJ8NDZyJoMg7xrZHOANoa9BF4YNIOL4JHsKlQGNCn7RMtnxzqY-9uB4h3ivB3jX27tmcsQmF0cwrUB06M0YaJwhVtnelkG3OsMPkvUAdfSZO-RBNJp0eRdjB1NAlgXThHeMK_Onn2aMuLAYiijblU5DJN-eyRPG3ZrbvZU0-VB4cPOPZSC2ajPVXwb4MCeWB5wMBky1zNSgwD-rH4CkxcN00XPm6YbxMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش جامع ساخت فیلترشکن شخصی و رایگان با پنل BPB (بدون نیاز به سرور!)  ---  امروز می‌خوام یکی از بهترین، پایدارترین و بی‌دردسرترین روش‌ها رو برای داشتن یک VPN دائمی و کاملاً رایگان بهتون آموزش بدم.   توی این روش که به کمک پنل BPB (Bypass Panel) انجام میشه،…</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/5967" target="_blank">📅 19:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5966">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚀
آموزش جامع ساخت فیلترشکن شخصی و رایگان با پنل BPB (بدون نیاز به سرور!)  ---  امروز می‌خوام یکی از بهترین، پایدارترین و بی‌دردسرترین روش‌ها رو برای داشتن یک VPN دائمی و کاملاً رایگان بهتون آموزش بدم.   توی این روش که به کمک پنل BPB (Bypass Panel) انجام میشه،…</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/5966" target="_blank">📅 18:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5965">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">طبق گزارشات محدودیت ۶ پکت هم اکنون رو بیشتر isp ها برداشته شده.  کلودفلر کلا باز شده</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/5965" target="_blank">📅 18:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5964">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">طبق گزارشات محدودیت ۶ پکت هم اکنون رو بیشتر isp ها برداشته شده.
کلودفلر کلا باز شده</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/5964" target="_blank">📅 18:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5961">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">vless://c2b6a323-19ec-4e4f-a95c-8b0e99aa7660@109.120.138.95:443?security=none&encryption=none&headerType=none&type=tcp#%40archivetell
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo0YTRjYjU3NS0xNWJkLTQ2NjQtYjk0ZC0yZTZhNmI0Y2NkYTg%3D@109.120.138.95:28655#%40archivetell
عشقا تست بزنید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/5961" target="_blank">📅 18:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5960">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CD_75rOM9B7VjDMops6sfYj-ivRSlFeQpZoV3XTxVLCzKF9TzSfy3h4RTb4dz5gAhI0635H_vc27SZSgM2iEaq5uByix4hF5VnKr2D_7_Tq-rZjkCElTRaY9Zi5WeaMBHZ-HnyWZgTsTCbKny6vR8-xCFjUlLe08ImxqZn1O4dLvCDkadat4TulYnk_uVpkbxDE3uhoyNYXU5Aoq1RWc48s8IjwfomcHlrWcjyvMNthx_iBoecQKxparkJpwmtpu6kUCCZjVcKM07ixcfTxHBvHhQFIXKo93jVVJCzfZ7O74wCTjHhhykVDfV9IhBG1E4vY_lTLiIHmxWoCnHiDOhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
اجرای شبکه‌های عصبی عظیم روی سخت‌افزار قدیمی — کتابخانه AirLLM اجازه می‌دهد مدل‌های سنگین حتی روی کارت‌های گرافیک با ۴ گیگابایت حافظه اجرا شوند.
🕤
به جای فشرده‌سازی ساده فایل‌ها، پارامترهای مدل را بهینه می‌کند و به طور چشمگیری نیازهای سخت‌افزاری را کاهش می‌دهد.
🕤
می‌تواند حتی در جایی که کارت گرافیک قدرتمندی وجود ندارد کار کند.
🕤
از بارگذاری مدل‌ها مستقیماً از Hugging Face پشتیبانی می‌کند.
🕤
سازگار با LLMهای محبوب: مدل‌های OCR، تولیدکننده‌های تصویر و سایر ابزارهای هوش مصنوعی.
https://github.com/lyogavin/airllm
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/5960" target="_blank">📅 17:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5958">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHaWaFldqljHKHK59gz5iAEG-2sbXek6WL9qOT0tkTGV5CWYosjY2GTFBKTLHZ92QG8N-UrpcbkQW8XbfBhM20YMzCsLmYqLn0rlK3Ajwlh8dMkL4w53DMcgIFECaxPUcL9ZetOPooedKxESyhe_r-8U6Q1mfHJqZnwz0RSesbsbuK2YWFDlheRuCQQJJelxgA1NDXsUXCP0cTrOIXskGYYllmRjawaf6gyaHNGNItQhhrdq97sdRyGDR-3voCp3BCAtdlgvAciZCdLd5KPGYBs3Uf5_OKi5-llrr8HuXrczQvmlk5E3RCTqbVUt2kTULup-YxxZ3UlFC5cQ02zkXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت عکس نامحدود و رایگان
پشتیبانی از مدل‌های GPT Image، Gemini، Qwen و غیره، بدون نیاز به ثبت‌نام، کاملاً رایگان، بدون واترمارک.
https://freemake.cc
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/5958" target="_blank">📅 15:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5957">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujBhP8nZ6O8AXn2uB1GHxTVykBewpxIl9jCPbl_G-S5iLx0hQvOzsXRq1lGPF4QJ6RZei3bXDE-PqsXZk_XvElh5jd6-B0WBraAtqP9r_qnk_f4fs1Hmgr35l6Oqr0HH-TL4BZrc1M_g_yP6HECekS3V9HIb9uEUCS-0Fc4BXZ5Brfd-FL-7ad8DAWoKnI8V9LkYkYq0dsEcoW5j_VYcWiULYeBg9MjRLKKAsKpnhTHxOP-nnxOcQA5R0ykX4mIaspVXNH80RMs_GtGBXQsVKpBQa2gKeAzpqCMvy7gLiuB2Emg9GH1npQamRETIbF90urcBgHRVzRxBvNzt8Kjtbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۱۰۴ ابزار هوش مصنوعی و ۶۲۴ پروژه متن‌باز
https://ai999999.top/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/5957" target="_blank">📅 15:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5956">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8404d116e.mp4?token=YQx7pHMdzTJhQB8UJQUYR2EVPSMLtGzLAQnFfGkzv4GwQ6AoIms5Ttzv5VXbrKQyvHQs8GsYs_Yd9YN1oIpTWY6p-P12DG0a5UYYeJTwxlwnsE8LKdI5MnaVBpgSrSj-BSHbFw41azsLtvTSKkrimwzpA4s7oOqR6c8yArhqAB7nJK1A5xVHJUylcVChd_5_vBRrzE5wKwtshAaw5yJ_4HeDWcj0NmU2vLl6WnSIxB-Tjh77sTm5GSMZ6gRsMDA2rsmw5YO7LB5Maewb7Cz_KjzmhwtXxkllb_OCx-JKhcRuIFYgi6kfLWj5p_-6hny36N4HW_HxsH01VcKHqjgBvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8404d116e.mp4?token=YQx7pHMdzTJhQB8UJQUYR2EVPSMLtGzLAQnFfGkzv4GwQ6AoIms5Ttzv5VXbrKQyvHQs8GsYs_Yd9YN1oIpTWY6p-P12DG0a5UYYeJTwxlwnsE8LKdI5MnaVBpgSrSj-BSHbFw41azsLtvTSKkrimwzpA4s7oOqR6c8yArhqAB7nJK1A5xVHJUylcVChd_5_vBRrzE5wKwtshAaw5yJ_4HeDWcj0NmU2vLl6WnSIxB-Tjh77sTm5GSMZ6gRsMDA2rsmw5YO7LB5Maewb7Cz_KjzmhwtXxkllb_OCx-JKhcRuIFYgi6kfLWj5p_-6hny36N4HW_HxsH01VcKHqjgBvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏰
WakeUpBroo — ساعت زنگ‌دار که شما را مجبور به بیدار شدن می‌کند
برنامه‌ای منتشر شده است بدون دکمه‌های «تعویق» و «خاموش کردن». برای قطع صدا باید کدی را از سایت وارد کنید — تا زمانی که به کامپیوتر برسید، خواب کاملاً از بین می‌رود.
چگونه کار می‌کند:
🔹
هیچ مصالحه‌ای وجود ندارد — فقط بلند می‌شوید و به سمت کامپیوتر می‌روید
🔹
کد برای قطع صدا در سایت تولید می‌شود — گوشی هوشمند کمکی نمی‌کند.
عالی برای کسانی که همیشه ساعت زنگ‌دار را عقب می‌اندازند.
لینک:
https://www.wakeupbroo.com/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/5956" target="_blank">📅 15:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5955">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b20169ea80.mp4?token=njL0wbDsI3_PdCc7Brvc_r70gIzulJ9OyhrJOq8lEU9cqJ1aCYwfJxQnD4lpuo9nUoI2aEd0cjt6J6luNPDnq3kQAzQ6YZNZC4KYG2uxEzeXo0ohprxgflw7tm2WSvbEQBPFdSSBubwsciInwfUR6JQnMnlQ-8qKmhjmMc8hIpmnb84oGW34n-95-VRQPblzlxawVzpimeZit6oSJNBlrLF68ycos6yaErEd-IvZdfP6oakqX9Kmyy7mHlGXA6O8ow9GpOVQfLOJg4SJVjz4WPSYYJmLt3etu3vHCRIq56yHWP3QHB9JASOqhePTyIqc9sOh9dPXt5-Hbocvn9tKDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b20169ea80.mp4?token=njL0wbDsI3_PdCc7Brvc_r70gIzulJ9OyhrJOq8lEU9cqJ1aCYwfJxQnD4lpuo9nUoI2aEd0cjt6J6luNPDnq3kQAzQ6YZNZC4KYG2uxEzeXo0ohprxgflw7tm2WSvbEQBPFdSSBubwsciInwfUR6JQnMnlQ-8qKmhjmMc8hIpmnb84oGW34n-95-VRQPblzlxawVzpimeZit6oSJNBlrLF68ycos6yaErEd-IvZdfP6oakqX9Kmyy7mHlGXA6O8ow9GpOVQfLOJg4SJVjz4WPSYYJmLt3etu3vHCRIq56yHWP3QHB9JASOqhePTyIqc9sOh9dPXt5-Hbocvn9tKDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه عوامل کدنویسی سلاح بودن
😁
Claude Opus 4.8 Ultracode
💀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/5955" target="_blank">📅 15:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5954">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ArchiveTel
pinned «
سرور اختصاصی 1000 گیگ اهدایی ادمین چنل:  vless://75700dda-3aa7-4f8e-b978-2237516f84db@45.130.125.66:443?mode=auto&path=%2F476T682e67a4f84a3c838ca94R86273&security=tls&alpn=h2&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPost…
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/5954" target="_blank">📅 12:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5953">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سرور اختصاصی 1000 گیگ اهدایی ادمین چنل:  vless://75700dda-3aa7-4f8e-b978-2237516f84db@45.130.125.66:443?mode=auto&path=%2F476T682e67a4f84a3c838ca94R86273&security=tls&alpn=h2&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPost…</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/5953" target="_blank">📅 12:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5952">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCd-fg0CKvdxzlnTAXEkMJXNFQvvIHemtFQ29pD3GOjXhu6P1kwdHtaX3ZDUjgWG8EVoo9nd4qWN7U3Q0B7GU572EAFTscphwaoaO_JvotoJwcj_QjinB9SkbUrsdkrRvxI6nUCQRhlkuCgcZyacQfjfBQ6jhedY-2ZFC3_XQ7l0UA3WLWxNAj6FzPZKHVBu4gooV5wGp1FQc-WUhur_jHjzb8LYmWUB_yCVo4UzHrPO6WT71yVNSzVfd9u3_bYEwcsMWFK9JGBisEStj5HSpSdOFdcktA8zQY1-ZwWbw2erBb6SSNAoau-tUR7UNAf6VRMK52bCohqPIQrrbun5bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🪗
می‌توانید اسپاتیفای را فراموش کنید — پلیر موبایل رایگان Metrolist را پیدا کرده‌ایم که دسترسی به موسیقی را بدون اشتراک و بدون تبلیغات فراهم می‌کند.
Metrolist چه کارهایی انجام می‌دهد:
🕤
موسیقی و کلیپ‌ را با کیفیت خوب پخش می‌کند.
🕤
موسیقی و لیست‌های پخش را برای گوش دادن بدون اینترنت ذخیره می‌کند.
🕤
بدون نیاز به احراز هویت اجباری کار می‌کند.
🕤
متن آهنگ‌ها را مستقیماً داخل برنامه ترجمه می‌کند.
🕤
امکان گوش دادن به موسیقی همراه با دوستان را فراهم می‌کند.
https://metrolist.cc/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/5952" target="_blank">📅 12:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5951">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سرور اختصاصی 1000 گیگ اهدایی ادمین چنل:
vless://75700dda-3aa7-4f8e-b978-2237516f84db@45.130.125.66:443?mode=auto&path=%2F476T682e67a4f84a3c838ca94R86273&security=tls&alpn=h2&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%2210-50%22%2C%22xPaddingHeader%22%3A%22apinode%22%2C%22xPaddingKey%22%3A%22domow%22%2C%22xPaddingObfsMode%22%3Atrue%7D&insecure=0&host=ticket.fibernet1.qzz.io&fp=chrome&type=xhttp&allowInsecure=0#ArchiveFast
به عشق اسما
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/5951" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5949">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">۱۵ گیگ کانفیگ اهدایی
⚡️
❤️
vless://4497c7f4-f6ac-4608-aa26-6948586470c3@94.183.157.63:2086?encryption=none&path=%2F&security=none&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/5949" target="_blank">📅 11:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5948">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">۱۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
ss://YWVzLTI1Ni1nY206WmpnM05URXdaVGMwWmpRMU16ZzBNVE0wWVdNMk4yWXpOak00T0RZeg@37.32.13.159:10112#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/5948" target="_blank">📅 11:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5947">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">potato vpn آیفون
همراه اول
✅
https://apps.apple.com/us/app/vpn-free-vpn-potato/id1473774730
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/5947" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5945">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gtOQhlNP6Vz3nqNf83QLfnWBMpXS0tMJMRsjRBDfNXe2PUifpx_4F9WZLwKV53xn3rWCAQZxP7ZS4MXpPJia87u1nGZNqMibJAbAQTX5JrYD-0bY4gL6fSJ1OsjDj6_7LG2r9yHVo4zeSLJThbyZBtpfaShF83LzF2Nb3wN8VneM2SAS384hvxBvSfgEYLeYTc4TXcxWkeYv2_epsvAiiYwGJpa0sJtpTpmG-wn83IZGbANPTzxyMhwnrDGf9YQ76eoNUMv4iC5HKj24Zd0vT0u7Mn3oQG2SjIkxUPZejZ7x1ELn7FSWkpGQkQq1Rm0uFMoEpUUTgYCUyo5aJbgfeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJV91RN7RKS0eoUPjTs4W1ey9CNU6Fe-z_aJjRX2WVHDu2uZAfSaoXzrA_bYYGGtVHuH00GVsjjskpDPN1-_7E5y3h_ZQRfmrtdVwzw7SX2JrS3g7QQ4CKKhMuyMdDLIJk90LGRaA_XekmveWv0GuSmuVkQXHKwJ5aDEe4wjMtRvOw7pgnb0I3DS94BN8VVcNggRdJ4hcdygy-4LYy4EaD03pSa4q_cPq_2eHDst9UXbuJwaq6MXNIPgG2fynw321_9kdICq7_RfXdm4MW9xAlCdmR6yUkC-6ZnXUzrIjwuahTgHPBtDwiX_gmDM7tiXUmmqxQltn8dRWG47AXNlrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Fair vpn
ایرانسل
✅
اگه سرور پرسرعت خواستین پینگ حتما زیر ۳۰۰ باشه .( اتصال به سرور دیگر) رو بزنین تا پینگ خوب رو پیدا کنین
✅
https://play.google.com/store/apps/details?id=fair.freevpn.vpnfair.fairvpn.fastvpn.proxy.vpn
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/5945" target="_blank">📅 11:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5944">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">GoFly VPN
سامانتل و آپتل
✅
(اول با vpn برید سرورها بیان بالا )
https://play.google.com/store/apps/details?id=com.ambrose.overwall
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/5944" target="_blank">📅 11:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5943">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یه کانفیگ از اینجا بگیرید. warp-generator.github.io/warp/‎ فرقی نداره کدومش باشه از Amnezia باشه فقط.  اندپوینتشو تغییر بدید به این 188.114.97.6:7281 بزنش داخل Amnezia WG با همراه و ایرانسل و مخابرات وصله.  @ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/5943" target="_blank">📅 11:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5942">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeU47K69yATnOJQ9d8M43masUoKQDw5ybv_wuJf-oRR-tWZgFWTfHu8evNM0Yx7d9tJFs6L0oZcG1qZi55mWMZ4JV8WUOYyAJD9wWzah7qgV1NNIb7ZXoF67xy-aCENptnK4kH3YRUu44IiLdDTYkNUs9RMkb1d-_FBacUXLYLISucl-w3hMN9wKfYcq1i6BdBPUfpzg5ZzpzyYefvznF5QuP80ErI4FJHZo0HQcBUr9L1RId8IDo3nrDLdSH2nC_TS_UPbxzRQLB5wjwKL2erzWpil70nGdck7rx_ShLqDj4A1hWBIv4bsJ148sN_bP3yQSA0UxEQzfvTlwxOKxjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Cybear vpn
ایرانسل
✅
https://play.google.com/store/apps/details?id=com.bear.vpn.super.fast.unlimited.connect
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/5942" target="_blank">📅 10:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5941">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQ3YzCqWPMnd61pyQC-kpfNl-sBh4BKEH9s8MC0z3vdNSor4_Qu2y0ilscKnaPbsaOMrYpFLEqPl_cJXLDhq9J8Zf8Y97w3vZqQa5PLzkbUX_mebCUI_C9VbITpRAmaP_OAN9YRnEcY9igl4nq3GAqX4jQJUkzOMqvLs5QatQcsn57MfMRtx2ZXm58bI1ow0NXMgMpkIpHBccC6DHvab_Vs4L7gVefyfYmd-1fJDJHRQLdOLQYGMea4kN5IQps9MrVfNSOyaJ6dPhGvC7Gaqmbtjla7HPMgyqbkUyDMb4RaFldvzTZCLPM4_tjYg8oIXJWrLvfsDSy5PB5MBFAfr9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Soren vpn
ایرانسل
✅
https://play.google.com/store/apps/details?id=com.provpn.soren
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/5941" target="_blank">📅 10:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5940">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQVEuxRcDDiaKNAltnoYNE77GKpWhZhrEoViRMCA_w-QSdIizC1bQZrAzVkY1aGHp0__SNRnC2VPPFmth4ZpQvdmCQ5WCkCWniFU-dxXQomfSj1XhmID0aewdEHdDPpZPbI3HXYel4jmzlT6Uz_pC5ScIyTSEo4Ra3_C5vNSdIdu-9wbL40s50ifUqAJeU8IHwbmMsl7HpPx3LdjmFMxbWeRi8_AkOjIypcTCoXYhpwULR4TR9MyVz7H1MoGj0EwPb4Odw7INRezPm1L0-EPbp3tX0Tny1Mjm97l1wJGkhjj4AsqITLUx8B6USJjPMPJ78WK6FWiKk0cFbB3ftni4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥷
۱۳۸۷ تجزیه‌گر OSINT جمع‌آوری شده‌اند - یک کتابخانه جهانی برای تشخیص نشت، تجزیه و تحلیل شبکه و دستکاری داده‌ها.
🕤
شبکه‌های اجتماعی ، تلگرام و فراداده‌ ها.
🕤
جستجوی داخلی ابزارها.
🕤
به‌روزرسانی‌های مداوم.
🕤
دسترسی رایگان.
OSINT Tools
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/5940" target="_blank">📅 09:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5939">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">https://hjfisher.github.io/SNISPF-HJ-Configurator/
انتشار configurator مخصوص SNISPF-HJ
تمامی تنظیمات رو می تونید اعمال کنید بدون هیچ سختی و خروجی بگیرید و استفاده کنید توی برنامه
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/5939" target="_blank">📅 08:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5938">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🛡
معرفی SNISPF-HJ — نسخه پیشرفته‌تر SNISPF
🔗
لینک پروژه:
https://github.com/hjfisher/SNISPF-HJ
━━━━━━━━━━━━━━━━━━━━
⚡️
چه چیزی اضافه شده؟
━━━━━━━━━━━━━━━━━━━━
✅
پشتیبانی از چندین IP و چندین SNI به‌صورت همزمان
در نسخه اصلی فقط یه IP و یه SNI ثابت می‌شد تعریف کرد. اینجا می‌تونید لیست کامل بدید تا ابزار خودش بهترین ترکیب رو پیدا کنه.
✅
Health Check خودکار
هر ۳۰ ثانیه تمام ترکیب‌های (IP, SNI) تست می‌شن و اگه یه مسیر ضعیف یا مرده شد، اتوماتیک جایگزین می‌شه — بدون قطعی.
✅
انتخاب هوشمند مسیر (Weighted-Random)
به جای انتخاب تصادفی، ترکیب‌هایی که packet loss کمتری دارن شانس بیشتری برای انتخاب دارن.
✅
Graceful Rotation
وقتی یه مسیر ضعیف می‌شه، کانکشن‌های فعال قطع نمی‌شن — اول کارشون تموم می‌شه، بعد مسیر عوض می‌شه.
✅
همه قابلیت‌های نسخه اصلی حفظ شده
Fragment، Fake SNI، Combined، TTL Trick و Domain Checker همه دست‌نخورده‌ان.
━━━━━━━━━━━━━━━━━━━━
💻
نصب روی ویندوز
━━━━━━━━━━━━━━━━━━━━
۱. Python 3.8 یا بالاتر نصب کنید:
https://python.org/downloads
(تیک «Add Python to PATH» رو حتماً بزنید)
۲. در CMD یا PowerShell:
pip install git+https://github.com/hjfisher/SNISPF-HJ.git
۳. اجرا با کانفیگ پیش‌فرض:
snispf-hj --config config.json
یا برای دانلود کامل سورس:
git clone
https://github.com/hjfisher/SNISPF-HJ.git
cd SNISPF-HJ
pip install .
snispf-hj --info
━━━━━━━━━━━━━━━━━━━━
📌
نکته
بعد از اجرا، آدرس
127.0.0.1:40443
رو به عنوان پروکسی در v2ray، Xray یا هر کلاینت دیگه‌ای تنظیم کنید.
⭐️
اگه مفید بود، به پروژه ستاره بدید!
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/5938" target="_blank">📅 08:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5937">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://2ddbde64-5bed-4209-b0bf-6a3f090d198c@se.sanaz.online:20609?encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%2C%22scMaxEachPostBytes%22%3A%221000000%22%7D&fp=chrome&host=se.sanaz.online&mode=stream-one&path=%2Fstream&pbk=aVfj7ITwEFsWQP4YjFuM-FBb8PWmfBYOwKu_Ag8dVVI&security=reality&sid=d675939d&sni=www.yahoo.com&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/5937" target="_blank">📅 08:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5936">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromℳ𝓊ℎ𝒶𝓂𝓂𝒶𝒹</strong></div>
<div class="tg-text">ترامپ فردا:
من در کاخ سفید داشتم قدم میزدم ناگهان یک ایرانی از 300 متری به من سلام داد پس من تصمیم گرفتم به ایران 2 هفته مهلت بدهم
آنها آدم های فوق العاده باهوشی هستند ولی نباید سلاح هسته ای داشته باشند زیرا به محض تولید آن را بلافاصله به سوی اسرائیل شلیک خواهند کرد، فکر میکنم آنها میخواهند توافق کنند، به پاپ بگویید خاک تو سرت</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/5936" target="_blank">📅 02:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5935">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85efdead3b.mp4?token=HhjYW3vp-D4MJQh33vDxZYGAASPtcOKBcwPvJ01MvFzcNww0OqEbLnEvM8F1f16WfmtKwh-gD4M-l2hw6hwtTXarCAWf7DFmsCn4XrvDJxnPt_iDm6poV77h14Hpi6nC9MuJf5SG1JoqFzxWVwQxz8O7hL9d1blClTuhndWCjBK2U-89JD4eEYF2u1Igc3j27MOsEbM_4TRS0Tw8n60qm23585mKsTzAAAvmoolkahTZsU-ScsL7_bWh3Xf6qk7ipeDCt5fjlpPDJpsRMB_ROYH3fIUTy_mzuLTpXfDt1-t9PQ5BzP5xfUge1eDX7crQK2vHrI6s707KRz1lBhzGtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85efdead3b.mp4?token=HhjYW3vp-D4MJQh33vDxZYGAASPtcOKBcwPvJ01MvFzcNww0OqEbLnEvM8F1f16WfmtKwh-gD4M-l2hw6hwtTXarCAWf7DFmsCn4XrvDJxnPt_iDm6poV77h14Hpi6nC9MuJf5SG1JoqFzxWVwQxz8O7hL9d1blClTuhndWCjBK2U-89JD4eEYF2u1Igc3j27MOsEbM_4TRS0Tw8n60qm23585mKsTzAAAvmoolkahTZsU-ScsL7_bWh3Xf6qk7ipeDCt5fjlpPDJpsRMB_ROYH3fIUTy_mzuLTpXfDt1-t9PQ5BzP5xfUge1eDX7crQK2vHrI6s707KRz1lBhzGtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/5935" target="_blank">📅 02:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5934">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وضعیت الان کانفیگ فروشا:</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/archivetell/5934" target="_blank">📅 02:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5933">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">امشب شب طولانیه🫪</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/5933" target="_blank">📅 02:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5932">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cc42fd82.mp4?token=THstpLlOpbpZMixuvsi0PudKaji7mTaa8otGrx3tt6eoWaj3S3NX04TXvKuGRfkpV166ztjWCqYgTBCce7pxkgDaw3-t--KiPG4DXcmCTDzRS9fLkoF-UyPM80uPUXbkIHcMraLt02Qtidps82Tp0wKzSyoeRpM6RZOz2crR5yrLnyMJTy3jmwqfk-FWpcSlRYM8HEB2CTAGMOVrwjF-qQtIaZ-qT5Nh4_8_iIuJAUlm13--LDNgaKpEsmu77NugzYqdo1WDHkGQMHANQvCzwcRBkmCoccAWZ8blc3cKUCpUtBPINaGaJxXnu9v814bxJ9VLxzowIlOxr5yr04mLRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cc42fd82.mp4?token=THstpLlOpbpZMixuvsi0PudKaji7mTaa8otGrx3tt6eoWaj3S3NX04TXvKuGRfkpV166ztjWCqYgTBCce7pxkgDaw3-t--KiPG4DXcmCTDzRS9fLkoF-UyPM80uPUXbkIHcMraLt02Qtidps82Tp0wKzSyoeRpM6RZOz2crR5yrLnyMJTy3jmwqfk-FWpcSlRYM8HEB2CTAGMOVrwjF-qQtIaZ-qT5Nh4_8_iIuJAUlm13--LDNgaKpEsmu77NugzYqdo1WDHkGQMHANQvCzwcRBkmCoccAWZ8blc3cKUCpUtBPINaGaJxXnu9v814bxJ9VLxzowIlOxr5yr04mLRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/5932" target="_blank">📅 02:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5931">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985e567cda.mp4?token=Nja3NC7CXcTBK8w_6nz7MH5-ahvdGr_O58MdbenEbbmboHtEOp1PA_JKosADBEONnEv1qP9hcGI_j3aE-nq4oI5OceIbcnGFbxfe8ffyDrcmUrKIErYA_yeyBP6P7dVznb9P2SMNqZBFmk_v4sPxN8X5-v4rkOk7Ndzxar14aOGuZ8Sq3CvnUmfeaB5gvm7RleDvub59Loo3x_BAIm2BxNqry-m6BHWSMqx0p3oIOhoQMgwdzi3Z3xfk9qU-AFRxeFbrjF2JjctxCmKdCaMKJgpIE678qPuiPtdkXVxVPyXafqezsdcfnOp4h47l_V25jKE-VuPe09UfWvBLM8C8FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985e567cda.mp4?token=Nja3NC7CXcTBK8w_6nz7MH5-ahvdGr_O58MdbenEbbmboHtEOp1PA_JKosADBEONnEv1qP9hcGI_j3aE-nq4oI5OceIbcnGFbxfe8ffyDrcmUrKIErYA_yeyBP6P7dVznb9P2SMNqZBFmk_v4sPxN8X5-v4rkOk7Ndzxar14aOGuZ8Sq3CvnUmfeaB5gvm7RleDvub59Loo3x_BAIm2BxNqry-m6BHWSMqx0p3oIOhoQMgwdzi3Z3xfk9qU-AFRxeFbrjF2JjctxCmKdCaMKJgpIE678qPuiPtdkXVxVPyXafqezsdcfnOp4h47l_V25jKE-VuPe09UfWvBLM8C8FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/5931" target="_blank">📅 02:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5930">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یه بالستیک که این حرفا رو نداره...  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/5930" target="_blank">📅 02:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5929">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یه بالستیک که این حرفا رو نداره...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/5929" target="_blank">📅 01:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5928">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">IObit Uninstaller Pro 15
License type: 6-month
Platform: Windows
License code:
2F93C-7EB9A-0BFB7-0B6TE
146D0-5E924-04007-088TE
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/5928" target="_blank">📅 01:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5926">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">100 گیگ مولتی لوکیشن
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@greblox.forum:443?mode=gun&security=reality&encryption=none&authority=greblox.forum&pbk=Tb21e9Z3rtr5NoprXQQtcqLLRZOgIVyIbuZmqPJkGXM&fp=firefox&type=grpc&serviceName=grpc&sni=greblox.forum&sid=c4cb37f029af5828#%F0%9F%87%B3%F0%9F%87%B1%20Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@crope.top:443?security=reality&encryption=none&pbk=Xgq8hNKvlfsBVHeJtXwjytbB5Fv2Tnu7vXJdZOgS8ig&headerType=none&fp=chrome&type=tcp&flow=xtls-rprx-vision&sni=crope.top&sid=b5af336756f77990#%F0%9F%87%B3%F0%9F%87%B1%20Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@birch.gouher.one:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=y_1jLoCup4gdKlQHsw6rj0FiPX0Mt6cyg2w1bIR9ris&host=stream.greenfield.lol&fp=random&type=xhttp&sni=birch.gouher.one&sid=28e92c6d545c9c26#%F0%9F%87%B3%F0%9F%87%B1Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@meadow.pinevalley.top:443?security=reality&encryption=none&pbk=JfUgtIVRM26EKkksroAENXLWNJp9n28mSG-z-8CDAHc&headerType=none&fp=chrome&type=tcp&flow=xtls-rprx-vision&sni=meadow.pinevalley.top&sid=e86995a2ccab9364#%F0%9F%87%BA%F0%9F%87%B8%20USA
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@rouze.click:443?mode=gun&security=reality&encryption=none&authority=rouze.click&pbk=PqunTCzbpHjmqH97ZpXHL0RBMyHaFzjJAO8i3uHr-XE&fp=chrome&type=grpc&serviceName=grpc&sni=rouze.click&sid=7fcb3d98608f93b6#%F0%9F%87%B3%F0%9F%87%B1%20Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@berry.riverpath.live:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=y_1jLoCup4gdKlQHsw6rj0FiPX0Mt6cyg2w1bIR9ris&fp=qq&type=xhttp&sni=berry.riverpath.live&sid=bdf09e70262b409c#%F0%9F%87%A7%F0%9F%87%AABelgium
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@road.oakvalley.digital:443?security=reality&encryption=none&pbk=rkgs3hpc8oIb2gCtzdy0AnD2AD2LkhtArGzTDDjcPnU&headerType=none&fp=qq&type=tcp&flow=xtls-rprx-vision&sni=road.oakvalley.digital&sid=54aafe829679e92f#%F0%9F%87%B5%F0%9F%87%B1Poland
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@stone.quietgrove.forum:443?mode=gun&security=reality&encryption=none&authority=stone.quietgrove.forum&pbk=MchbHn3bpJaqAX-oqnNXYiXrbUTN0n-K203T8YGr8D4&fp=chrome&type=grpc&serviceName=grpc&sni=stone.quietgrove.forum&sid=0ae20b3e5e2c0bc2#%F0%9F%87%BA%F0%9F%87%B8%20USA
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@flame.quietgarden.live:443?mode=gun&security=reality&encryption=none&pbk=fzbtjP1MtR9JYN-pKDJQTWB9I-V_EPEgdteL76Ed5yA&fp=random&type=grpc&serviceName=grpc&sni=flame.quietgarden.live&sid=06d7e21ecb57367a#%F0%9F%87%A9%F0%9F%87%AAGermany
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@ember.quietgarden.live:443?mode=gun&security=reality&encryption=none&pbk=fzbtjP1MtR9JYN-pKDJQTWB9I-V_EPEgdteL76Ed5yA&fp=random&type=grpc&serviceName=grpc&sni=ember.quietgarden.live&sid=fd488ee90cc0b9eb#%F0%9F%87%B3%F0%9F%87%B1Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@valley.syrniki-iz-samokata.live:443?mode=gun&security=reality&encryption=none&pbk=euMfJzUx3qAGiaXwcvAXqXiqglBQKPOqxkTdSqwnqEw&fp=qq&type=grpc&serviceName=grpc&sni=valley.syrniki-iz-samokata.live&sid=c6046d150f597d04#%F0%9F%87%B5%F0%9F%87%B1Poland
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@field.wildgarden.digital:443?mode=gun&security=reality&encryption=none&pbk=dtxZ0lFLHE0IGfg45g2t1t7WwHWHuDW4xbfww3zKhDQ&fp=random&type=grpc&serviceName=grpc-bridge&sni=field.wildgarden.digital&sid=bbbbe9607d343bb6#%F0%9F%87%B3%F0%9F%87%B1%20Netherlands
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@bridge.oakvalley.digital:443?security=reality&encryption=none&pbk=rkgs3hpc8oIb2gCtzdy0AnD2AD2LkhtArGzTDDjcPnU&headerType=none&fp=chrome&type=tcp&flow=xtls-rprx-vision&sni=bridge.oakvalley.digital&sid=5278abf8d6d75483#%F0%9F%87%B9%F0%9F%87%B7Turkey
vless://d9aff7cc-4e0f-4cd6-bb30-40f083974874@eveningwalk.sunnyside.city:443?security=reality&encryption=none&pbk=rkgs3hpc8oIb2gCtzdy0AnD2AD2LkhtArGzTDDjcPnU&headerType=none&fp=qq&type=tcp&flow=xtls-rprx-vision&sni=eveningwalk.sunnyside.city&sid=54aafe829679e92f#%F0%9F%87%BA%F0%9F%87%B8USA</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/5926" target="_blank">📅 00:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5925">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">10 گیگ مولتی لوکیشن (حتما ساب کپی کرده و وارد کنید)
https://cdn-biz.ru/sub/1/0588b70e-0b61-4e10-8d34-e83e8968cfd5
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/5925" target="_blank">📅 00:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5924">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
لوکیشن ترکیه ، همراه اول هم وصله..
vless://b9dccdab-0f77-4fb7-8949-4d378e92df5c@cdn4.greewebservices.ir:2095?encryption=none&host=turpanel2cdn.consolegamenet.ir&path=%2F&security=none&type=httpupgrade#@ArchiveTell%20%F0%9F%87%B9%F0%9F%87%B7
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/5924" target="_blank">📅 00:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5923">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
فوری؛ آمریکا چهار صرافی بزرگ ایرانی نوبیتکس، بیت‌پین، رمزینکس و والکس رو تحریم کرد.</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/5923" target="_blank">📅 00:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5922">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
فوری؛ آمریکا چهار صرافی بزرگ ایرانی نوبیتکس، بیت‌پین، رمزینکس و والکس رو تحریم کرد.</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/5922" target="_blank">📅 23:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5921">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://b9dccdab-0f77-4fb7-8949-4d378e92df5c@areal1.greewebservices.ir:2425?encryption=none&fp=chrome&pbk=xQnXh5EfPDhcEBB7rRiLca33GYrMEeUa35domLL_yA8&security=reality&sid=9b60d3&sni=yahoo.com&type=tcp#@ArchiveTell%20%F0%9F%87%A9%F0%9F%87%AA
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/5921" target="_blank">📅 23:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5920">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کدام مدل‌های هوش مصنوعی روی دستگاه شما قابل اجرا هستند؟
یک ابزار آنلاین که به کاربران کمک می‌کند بر اساس مدل GPU به سرعت بررسی کنند کدام مدل‌های هوش مصنوعی را می‌توانند به صورت محلی اجرا کنند.
https://www.canirun.ai/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/5920" target="_blank">📅 22:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5919">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">۲۰ گیگ
⚡️
vless://2ddbde64-5bed-4209-b0bf-6a3f090d198c@se.sanaz.online:20609?encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%2C%22scMaxEachPostBytes%22%3A%221000000%22%7D&fp=chrome&host=se.sanaz.online&mode=stream-one&path=%2Fstream&pbk=aVfj7ITwEFsWQP4YjFuM-FBb8PWmfBYOwKu_Ag8dVVI&security=reality&sid=d675939d&sni=www.yahoo.com&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/5919" target="_blank">📅 22:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5917">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRAnTs3ZbNoOamnOXYkmXpBAOzTHLfazGW9mgiN1pVhLV_QJE7euejChNEyOptu2WsYWtls69QaTA0x7KdpaqYY3sGkEMeFbhRB3XzDjji6P3L7TjHe4X5g9t8GT6tCyWSr7lxzghCn1d2ntGyAKB7bZrUjoLr32FWFplpToMgo_Gz7-rTh61_z2QnGxryUOHVvxVSoBeCJZnnE3zJ8zkoFFhwGJHPbEET5Jm5DMwxjNU4fINgGxs9oYFNc7CAy3WmDAF_9S_6kS5TwX5DNg6Mw_qJ8touR0zKV8ZQ1UDtr58Dx4JCN6Fm8AYDub3DRoZhrKSz6jwOeF8q7kBgYxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚒️
۱۳۰ ابزار که جایگزین تمام نرم‌افزارهای اداری می‌شوند: آفیس، ورد و پاورپوینت. همه چیز مستقیماً در مرورگر کار می‌کند، بدون نیاز به نصب و محدودیت.
در مجموعه:
🕤
ویرایشگرهای تصاویر.
🕤
ابزارهایی برای PDF، ZIP، CSV، Excel و فرمت‌های دیگر.
🕤
تبدیل فایل‌ها بین ده‌ها پسوند.
🕤
فشرده‌سازی تصاویر.
🕤
فرمت‌بندی و پردازش کد.
🕤
کار با صدا و فایل‌های صوتی.
🕤
ضبط صفحه نمایش.
🕤
ابزارهای متنی.
🕤
برنامه‌ها و چت‌های هوش مصنوعی.
🕤
ابزارهای ریاضی، فنی و داده‌ای.
https://github.com/aghyad97/browserytools#-features
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/5917" target="_blank">📅 21:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5915">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">VideoNote: ابزار یادداشت‌برداری و قالب‌بندی محتوای ویدئویی
یک ابزار یادداشت‌برداری ویدئویی کاملاً محلی که می‌تواند محتوای ویدئو را خلاصه کرده و یادداشت‌ها را قالب‌بندی کند.
https://github.com/xiaokeaijqx/VideoNote
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/5915" target="_blank">📅 20:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5913">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jd4gavrWQN5IHNKNTCKV4Ppvd6ZbqoUa5fyCEV4NZcUU_kHFvfa3QCWG50qhzqwvnMcWBmVpPfRl7geoTUlnEEiaxW1ZBWUrGl65nVbMLnSMD-qVFjG4WCVHQV-C-JlzWMHfVoiCkjnA7IUP3Uj5gMnSP08CJ88JYjby3_ay-8l8P6ou3h5TMy0ylgemPb-_gnl06NUYCzQXoZVyMBg8OPpENUhIo15jbrRYHIEG7hEVpa3oZrCK72SjJi0Z8mm1EXN7jEswYIIwLPsDK_oBfkCUqtfTkHwduhUMQSKJygvnumZ8kD6FuBJ24wmpIYrwNM6B8DnEknfqiVjcinhBqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvmrQDDPtpewQ3GSlfH9v45gco3-HQJ3ivtIwvpkjA6-0vDr7gFTgNA4V34wiDAA3zaWi7b2BDFJf6WUNpzgmn1pLj3lQGtrAd9q1Am0m3A1sr4_YTi15Xh9vWq7kKpM-3lNHa5vmvbuQXXBUWwD1jipw9xBgYZImiFuL7ODHe-LXGJQDpT8sSsRaLboCOC48xrba9ATr--JYuxk1REIyfP210IfbgsWntkk0OT69QfvyOgq4UWij2hInjdhQ6SFsH4-RPcs_zFCfUrdZVqaUR3zommLVa4wJ5FXFAANqK_nf07f1J_zsWZqEDX_7QXubdo81O5LJe3ga7vCIME5BA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنریت عکس و ویدئو رایگان
https://www.mindvideo.ai/creative-studio/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/5913" target="_blank">📅 20:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5912">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پروکسی اهدایی یکی از ممبرای عزیز کانال
😎
❤️
https://t.me/proxy?server=47.86.102.135&port=443&secret=dd887aa96cd9b760d42f62217afdcc6bc5
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/5912" target="_blank">📅 19:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5911">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7cytreFtVWrDwdJvF10ITpo6wm5ZD5DcZTDJf-coTRSkhbQKt2xKR21umDIrGEJ2eFHiqw-OfTR_VhZZEyQWLRnlQenFas7zdCuW9aftnui2zcYdXpu_7Ne82kz2U-eSZTNZ9SBKlkaaRablwWQ1HXLE4-vodLIa-5sl8vZaHYY9Ul_s8wWZYJClr8SnRGml74rv2fQzoc3OLd6P4Yr2Ml0gI-5CpBAx3sxem42jwkQKpGij0WIK92CY6QtGYlXoE1hQ0GGorFWxT7kgdSZMXZe1VKYjnSFrhEFCHk_C-Ejbsu7ksz4NmbDvEgkYutLtgsmCjIu-4-MCrAfULBTAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
ویندوز 11 را تا حداکثر توان ارتقا می‌دهیم
1️⃣
بهترین نسخه‌های ویندوز 11.
🕤
Flibustier 25H2
ایده‌آل برای استفاده روزمره.
🕤
Revision Group 25H2
حداکثر FPS ، مناسب گیم.
🕤
Ghost Spectre 25H2
فوق‌العاده سبک که حداکثر بهره را از سخت‌افزار می‌گیرد.
2️⃣
حذف زباله‌ها و قابلیت‌های اضافی.
🕤
Remove Windows AI
حذف هوش مصنوعی که منابع را مصرف می‌کند.
🕤
Win11 Debloat
حذف برنامه‌های پیش‌فرض.
🕤
Ultimate Tweaker
بیشتر از ۲۰۰ تغییر در یک ابزار کوچک.
🕤
Open Hardware Monitor
کنترل کامل بر سخت‌افزار
3️⃣
نرم‌افزاری که بدون آن ویندوز 11 دردسر است
🕤
WizTree
— بالاخره می‌بینیم فضای دیسک کجا می‌رود.
🕤
Revo Uninstaller
— برنامه‌ها را بدون باقی‌ماندن رد حذف می‌کند.
🕤
TaskExplorer
— مدیر وظیفه با قدرت بیشتر.
🕤
Explorer++
— مرورگری که واقعاً راحت است.
4️⃣
ظاهر و راحتی استفاده
🕤
Windhawk
—
مدهایی برای بازی ها
🕤
Jax Core
— پک‌های بصری و ویجت‌ها.
🕤
Seelen UI
— سفارشی‌سازی عمیق  رابط کاربری.
🕤
Cursor Mania
— هزاران نشانگر موس برای هر سلیقه.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/5911" target="_blank">📅 19:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5910">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ارائه‌دهنده سرویس‌های پرسرعت، امن و بدون قطعی اینترنت
🚀
| خرید و تحویل آنی | پشتیبانی اختصاصی
🛡
کانال: @ArchiveTell https://t.me/ArchiveTellbot</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/5910" target="_blank">📅 18:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5909">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ارائه‌دهنده سرویس‌های پرسرعت، امن و بدون قطعی اینترنت
🚀
| خرید و تحویل آنی | پشتیبانی اختصاصی
🛡
کانال:
@ArchiveTell
https://t.me/ArchiveTellbot</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/5909" target="_blank">📅 18:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://3617290e-f2e0-4eb5-9576-a610aa6f2c95@104.167.199.23:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fp=chrome&host=104.167.199.23&mode=auto&path=%2Fmohraz&pbk=wtVFe9j0FtOMtxUBKJqjd7NZs9-47lsjbnUlWq_MGEs&security=reality&sid=26a4&sni=www.samsung.com&type=xhttp#@ArchiveTell
https://104.167.199.23:2096/sub/ugqvbxg55h1u87rw
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/5907" target="_blank">📅 18:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuJ8VqD2dQ0CQly1pzo2zFAzQaFZcViclTcq2ZbU2hHIp2Ra7Ii99KTY2N2t92V1GIrBm6qnNsmXgugpVrtDX1JcKg8GjMMsdVgCi0MS6HRXHilzo0cHyetWST1WCskRzIlZc2QyTDRtMxHiR3xxC9Osl_JYXnGKuqNm6EeDQnaNWJ9z6puOWnE96jNxlv8Y8xijoTi_--BbZAuYEVQDqj9anDZKzy9uJgV2FHkRokRvi4ntXp0B7qRr6Bha4CZHv2TyABPM2BchaZCnkTmJCm5eh9iF7gU83ImU-AJpu6Xig1txI_6gceO0cmh5lI5e73KEhGw7OIc5QAAb_NKvWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نابغه ها قبلا ی چاره دیگری هم اندیشیده بودن پرایوسی سکسی</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/5904" target="_blank">📅 18:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">https://obito.96s.ir:2096/sub/cqx44nj2vnu1mebr
لینک ساب 50 گیگ ...
@Sina_1090</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/5903" target="_blank">📅 18:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🖥
ویندوز ۱۱ از تمام برنامه‌های غیرضروری پاک شده است - نابغه‌ها یک نسخه رایگان از این سیستم عامل را ایجاد کرده‌اند که ۲.۳ گیگابایت حجم دارد.  آنها موارد زیر را حذف کرده‌اند:
🕤
Xbox Center.
🕤
Windows Update.
🕤
Windows Defender.
🕤
Weather، Office، Solitaire و سایر…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5902" target="_blank">📅 18:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyE2Uc9h8zuBuEUpXis4yc3x_1kRKNtzFKaqxYhHDQDXgWDgB_LqTT7lwHHerAslAOv6UdfQpQaQvCHg0sZl6TYznBC05vLljIYy617kW1TPIpOKIR7f3_EgDBcZQKcwWW4hif3t2ISZoddmxwW_Sy7Xlwps2ZhSpyQp5DVZEIt0lxlB-zpq3VkKSU5m9xSq2QGZCvwwjr1DM5SLZlUEkukuOeRJxmU6RmDUKyGGk-lCeTbA2xx0CjrDNZX7dwj4zA9W8hpfp3lFDqBZb1DYmjv_jYPqrdFKouYA9zsbJM0UU6zmEtXq_NWCPLfDkWsSej2TV-mGdQDfkMaUTjSQFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
ویندوز ۱۱ از تمام برنامه‌های غیرضروری پاک شده است - نابغه‌ها یک نسخه رایگان از این سیستم عامل را ایجاد کرده‌اند که ۲.۳ گیگابایت حجم دارد.
آنها موارد زیر را حذف کرده‌اند:
🕤
Xbox Center.
🕤
Windows Update.
🕤
Windows Defender.
🕤
Weather، Office، Solitaire و سایر برنامه‌های داخلی.
🕤
اکثر درایورها (فقط ضروری‌ترین آنها باقی مانده‌اند).
🕤
Microsoft Edge و Internet Explorer.
http://github.com/ntdevlabs/nano11
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/5901" target="_blank">📅 18:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تولیدکننده ویدئوی تصویری هوش مصنوعی
ابزار آنلاین برای تبدیل تصاویر محصول، پرتره، پوستر و سایر تصاویر ثابت به ویدئوهای کوتاه، پشتیبانی از چندین جریان کاری و کنترل دوربین، مناسب برای صفحات محصول، تبلیغات و تولید محتوای شبکه‌های اجتماعی.
https://image-to-video-ai.best/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/archivetell/5900" target="_blank">📅 17:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">https://185.211.101.214:2096/sub/2f6ve5e7v0qim80w
سابلینک 50 گیگ ....
با نت های مختلف تست کنید...
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/5899" target="_blank">📅 17:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EoViVvq_Kb7nCA1z31GmHHLTLJ1fGDwQdHHDbkupXewG0vvQniBDnxWY551LqaZSSbTfrSWaDIg1ZxCU5zJuTpobQZtBB_jQM8C9HGeTuDVhGxXVkTTm9l6i7KCBZndb-tiueVzrtlpEmzplwUsXgV2yQMKpt_tMj6HV8PZ7kU6f_r6dv1BsgHbNT-C01INaGYxh4m580x1DN2oglg9NIbIYt24o7Qp0ahGhAzU3G9v0r4SAte2pEbjGe2Hnf0cTa-vWdIES7tugvvd-pYRBeWynoWliVDpoKSTkw8rYEkL3qGpFHOvtswK0gt_s1odO_0_XhMzoKqjZMxd825pE0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JOjbT4heu1vjAb7gLFV9t27GCeXaSPN3xbtPm257H3Tv2wYJQUAi8TGUfE_e0ZdPz0vj2chZD5YlVIyV-O4Pk7l6N0n8g7u0X0omyJldUhKEsRuTUT9leEX-J09HuBFHV-ixLfvfebKHlsNNEVuRmt1CQs2X3rc8bQ_ew4I65qg1WjDdNA6CEtO_oB16KTsYyDgon3u9-SESAZ5IDOshgNxBiehogrhmRSi7zZ3EVCt6UXCBKH6RZYtSs2WTGdYslbqlCdNL8PWQsaX49xCWFGzt9LztVzn1OvAzltuNx5xsPH421j2qPnzvcgvs2AgnmauiLAbKia8q8BmakWGbYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">https://khan.shompolexy.shop:2096/sub/tvhnms3g1zjuotay
سابلینک ۱۰۰ گیگ اینترنت
با همراه اول هم وصله..
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/5897" target="_blank">📅 17:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">Gemini Omni تولیدکننده ویدئوی هوش مصنوعی رایگان
پشتیبانی از ورودی متن، تصویر، صدا و ویدئو، قابلیت تولید کلیپ‌های ویدئویی با کیفیت سینمایی
https://omniaipro.app/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/archivetell/5894" target="_blank">📅 17:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuzKVaiNJj4I1ED0bhSMfkBEz7lNoG59PdpPYihbBbcKG6_OUkthG8ZYh-q2N8IOSBmpdF8qF5c2mYq0NEA-YiXFSv8nWUjAg4wafWvvAlanl5zOzXArrwQm1nFJIdVRVp7T_Xk0HhFJOmkvuN9Il0vWX161609hl_X3_sw01FWaH1aY1IGJudw_x_lO0rQampn64ghgKlSWSuveZrp1Q99vASAnNTa55_Pb--sXoRlT6PUSpChaj5CtC0rnLS9yvW7-aDYYdawSsmv71Emqru3iRMWhMh0JDSla3VpI7rQyLNpuqILHCYf_MzU9WtPSWoNwNwf_74rromEnRoq9Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">slipnet-enc://AVYDFT1SX5QRahOVGapvCIQOi5iX+F+Ayz7d82kXBzKUgbDFGOsXcyY12oASii0n3Ye5Fj9LOHfyxzQpTH6aZzsHCccHQuHa78SADfbTQRNENnLD6CeHOuPxRffHOjkB+5tHdtQ89Kfk8TzpeVOxfFMxXDMxDhTuX7D/hrMsm9KchoxYpj3l1HNlOSDSMkO6td9WttjNX/TrOGk9jSX3n+bBnR1t64wJs9TYIUUycW/wKH9ntwehzsQ0l7MkpkxjVGD4Qqx8G/AGiOGcqy0OHxb4WsNfWIvP+mR1UcoObW2qJCMqPvMmimZQGTCI0cHIbpH1Kx0GLVXI9USz59N6D+2py/TLS4sGIKK40X2xohmjXthNyo3zcIw20FmuSnV8Dez5RVaSAbUhuCY8Iqa5G/B9U2PmqAMcZSVUh+yr4IoK/7Uelbj4rUAT6SfYQlZiliDE6Wkx7eM5dd8rR2Zxmtjl/Lr1X/qtrMeQgbJ5w5QAlxmAltcolUJt3BH58ZOqpwTe</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/5893" target="_blank">📅 17:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">OBITO.conf</div>
  <div class="tg-doc-extra">530 B</div>
</div>
<a href="https://t.me/archivetell/5892" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@Sina_1090</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/archivetell/5892" target="_blank">📅 17:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-obito.conf</div>
  <div class="tg-doc-extra">532 B</div>
</div>
<a href="https://t.me/archivetell/5891" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@Sina_1090</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/5891" target="_blank">📅 17:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">هر کی دلش وایرگارد میخواد
دست بالا کنه....؟!
@Sina_1090</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/5890" target="_blank">📅 16:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">100GB مولتی لوکیشن
vless://d49eb175-facd-4c33-b1be-32c746701184@maple.cloudureld.com:443?security=reality&encryption=none&pbk=-VM1_ol58XU8fQHPvCnllupmpqyI6E1_bp6vpD6hD0w&headerType=none&fp=qq&type=tcp&flow=xtls-rprx-vision&sni=maple.cloudureld.com&sid=7e52de801e7c71de#%F0%9F%87%A8%F0%9F%87%A6%40ArchiveTell
vless://d49eb175-facd-4c33-b1be-32c746701184@island.cloudureld.com:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=U-aI9goYn0iGJ31emKZ1ltON45Ry0LjCl15MnumMD2c&fp=qq&type=xhttp&sni=island.cloudureld.com&sid=a7f9e69f037466b1#%F0%9F%87%AC%F0%9F%87%A7%40ArchiveTell
vless://d49eb175-facd-4c33-b1be-32c746701184@greblox.forum:443?mode=gun&security=reality&encryption=none&authority=greblox.forum&pbk=Tb21e9Z3rtr5NoprXQQtcqLLRZOgIVyIbuZmqPJkGXM&fp=firefox&type=grpc&serviceName=grpc&sni=greblox.forum&sid=9e327f04ce93c187#%F0%9F%87%B3%F0%9F%87%B1%20%40ArchiveTell
vless://d49eb175-facd-4c33-b1be-32c746701184@developer.projectauths.com:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=U-aI9goYn0iGJ31emKZ1ltON45Ry0LjCl15MnumMD2c&host=developer.projectauths.com&fp=random&type=xhttp&sni=developer.projectauths.com&sid=68d14e7adba07698#%F0%9F%87%B3%F0%9F%87%B1%40ArchiveTell
vless://d49eb175-facd-4c33-b1be-32c746701184@dev.projectauths.com:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=U-aI9goYn0iGJ31emKZ1ltON45Ry0LjCl15MnumMD2c&host=dev.projectauths.com&fp=random&type=xhttp&sni=dev.projectauths.com&sid=8a9d1d8916227e5b#%F0%9F%87%A9%F0%9F%87%AA%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/5889" target="_blank">📅 16:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oa3lZ2y_YfOeBPdWyWvKx7r7ukeDgcHYmHgZ54CIq0EMGEqajwBzCX9hNQfEY0kDEDiCboRjy6O-BHYV3n0KxuCYNd34d_WkYc-86RHQOH9_FUck9HeNuABDVCrxDU3inhSvC02UBHVNxCL2JCVbbCVE6TNFs3LENvCioiSSpOshk_gqUqponf-d65nDE83tWe8e7Vt5SlNWRCNmq6GQNIGnaT5O2njBOIFkWTq131ZUJ40TubBeEc6Y_muYEDvWvrCeSgEOxDQxHoSH5D_ruzk-5t8W6fKHhTGexiij92aS1FkLjwJzLNsOvECOmquKUw8aACheiaEux30gEqO_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطوری اندپوینت endpoint برای
کانفیگای وارپ
اسکن کنیم
داخل لینوکس یا ترموکس این رو بزنید
pkg update -y && pkg upgrade -y && pkg install curl -y
bash <(curl -fsSL https://raw.githubusercontent.com/bia-pain-bache/BPB-Warp-Scanner/main/install.sh)
به سوالاتی که میپرسه جواب بدین میگه چندتا اسکن کنم یا سریع باشه یا نرمال. ipv4 رو انتخاب کنید
دقت کنید که اسکن باید بدون فیلتر انجام بشه. اگه فایلش واستون دانلود نمیشه فقط قسمت دانلود فایل رو با فیلترشکن انجام بدین بعد قطع کنید و اسکن کنید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/5888" target="_blank">📅 15:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">۱۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://3617290e-f2e0-4eb5-9576-a610aa6f2c95@104.167.199.23:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fp=chrome&host=104.167.199.23&mode=auto&path=%2Fmohraz&pbk=wtVFe9j0FtOMtxUBKJqjd7NZs9-47lsjbnUlWq_MGEs&security=reality&sid=a99c6c05&sni=www.samsung.com&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/5887" target="_blank">📅 14:57 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
