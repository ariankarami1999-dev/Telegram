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
<img src="https://cdn4.telesco.pe/file/p67uOy8fGzkAFYvhsxwf8KLtK0_NvjN9yWGJei3OWeRO-iNQqbqHIAM9RzQngwvke9XbeO6cTDb-GVRI8ztQFieA6itJa62jmZ7kMjeWBi-e0s9-Xwt4WrMnCo_nlqhgw3Xr2LFxcuw0g_-2-PGeOSCr5C0Tg5VVIRJE8cQwsDEZPRzwW6n673nll8atJNTO1E6XJEjV1pq9pI0DCHYgwhSouebp-_7Bjscq1IU-EZlQOY8IUMM5GcUXRu4UlxQeWON6KEi0eTG6Vnf-k9rKmjPR-whZuDwNx_kkdCcXlkuzfmbSRxzxYJhLFj5VhunSeMTeYmqFGbbWIgXrIX-AeQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 8.7K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 16:36:06</div>
<hr>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎛
کالبدشکافی پنل سنایی (3x-ui)؛ نقشه راهنمای کامل برای بچه‌های آرشیوتل!  رفقای آرشیوتل سلام!
🌹
اگر به تازگی یه سرور خام گرفتید و پنل معروفِ سنایی (3x-ui) رو روش نصب کردید، احتمالاً همون اول با دیدن اون همه تب و منو یه مقدار گیج شدید. امروز اصلاً کاری به آموزش…</div>
<div class="tg-footer">👁️ 969 · <a href="https://t.me/archivetell/5732" target="_blank">📅 15:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚀
انتشار آپدیت بزرگ و جذاب پنل 3x-ui (نسخه v3.2.0)  ---  آپدیت جدید و پر از امکاناتِ پنل مدیریت سرور محبوب 3x-ui (نسخه سنایی) منتشر شد. این نسخه (v3.2.0) یکی از بزرگترین آپدیت‌های این پروژه است که تمرکز ویژه‌ای روی مدیریت گروهی کاربران، بهبود رابط کاربری و…</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/archivetell/5731" target="_blank">📅 14:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سایت خرید دامنه ارزون
👇
:
معرفی کنید دوستان
😂</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/5730" target="_blank">📅 13:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">RIP
⚰
Reality?</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/5729" target="_blank">📅 13:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzwP-4LoMr_aCwT_JHOWnPQ15rbZNa8N0yvO8i_9YE3WNx0ciRtOqsSaEAa8FPAurv8iOlQzTgSlj1oW5F-i4EXZQy3Oz-27Q_SJnPIUi8YN3lejzJWWnop29Eo68f7_2ype_XTTErT1IgyQSg7Zyh6nk_6k_EQBmQ7dY_MeXK90AZWvg3nh3qMPPrIQee0-2yHA0u6nG2zCQN58CDJhzJjIfxfjUnGaI8qwKAM27VSjOWlupB1eDT1q_YjWX2wJbbSnvdUjFCMfmokDI-ANvdXmt3tnTkOlw5fu2hio5hZkHCIGmczKTGOcvVl8XHBalUaguiaXYveXrcVuW39sEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">15 گیگ   vless://38a80d5e-0d9f-4bd6-b6ec-836fd07c8223@95.182.101.96:44535?encryption=none&fp=chrome&pbk=-0MP4KyHJ12AZ-z1YA5ITIjMOh8FUnGzSOSu2DFSgmI&security=reality&sid=be530c2769a1&sni=www.yahoo.com&spx=%2F9BvunqVqfGOOoPS&type=tcp#MOHRAZ-beeu61q6k5-15.00GB%F0%9F%93%8A…</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/5728" target="_blank">📅 12:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">15 گیگ
vless://38a80d5e-0d9f-4bd6-b6ec-836fd07c8223@95.182.101.96:44535?encryption=none&fp=chrome&pbk=-0MP4KyHJ12AZ-z1YA5ITIjMOh8FUnGzSOSu2DFSgmI&security=reality&sid=be530c2769a1&sni=www.yahoo.com&spx=%2F9BvunqVqfGOOoPS&type=tcp#MOHRAZ-beeu61q6k5-15.00GB%F0%9F%93%8A
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/5727" target="_blank">📅 12:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5720">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.7 MB</div>
</div>
<a href="https://t.me/archivetell/5720" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">V0.4.0</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/5720" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رفقا سلام!
✋
امروز یک ابزار فوق‌العاده کاربردی با رابط کاربری ترمینال (TUI) به نام
SenPai Scanner
(آپدیت جدید v0.4.0) را معرفی می‌کنیم. این برنامه ابزاری است برای پیدا کردن IPهای Cloudflare که واقعاً با کانفیگ VLESS یا Trojan شما کار می‌کنند. این اسکنر مخصوصاً برای شبکه‌هایی طراحی شده که در آن‌ها پینگ غیرقابل پیش‌بینی است و اتصالات به طور ناگهانی قطع می‌شوند.
🔥
ویژگی‌های اصلی و تغییرات نسخه 0.4.0:
*
روند اسکن دو مرحله‌ای (Two Phases):
*
فاز ۱:
بررسی اتصالات اولیه با استفاده از تنظیمات استخراج شده از لینک کانفیگ شما شامل SNI، Host، Path و پورت. برای کانفیگ‌های WebSocket، زنده ماندن اتصال از طریق DPI نیز بررسی می‌شود.
*
فاز ۲:
اعتبارسنجی نهایی با اجرای یک هسته Xray داخلی انجام می‌شود. در این فاز سرعت دانلود واقعی (Mbps) و میزان تاخیر (TTFB) اندازه‌گیری می‌شود.
*
پشتیبانی از پورت‌های متنوع:
امکان انتخاب چند پورت مختلف (شامل پورت خود کانفیگ، 443, 8443, 2053, 2083, 2087, 2096) برای تست وجود دارد.
*
منبع آی‌پی‌ها:
می‌توانید از رنج آی‌پی‌های تصادفی Cloudflare استفاده کنید و یا لیست سفارشی خود را از طریق فایل
ips.txt
به برنامه بدهید.
*
خروجی‌گرفتن سریع:
پس از پایان فاز ۲، با فشردن کلید
c
، ترکیب IP و پورت‌های سالم (Working Endpoints) در کلیپ‌بورد کپی شده و مستقیماً در فایل
ips.txt
ذخیره می‌شوند.
*
تمرکز روی یک هدف:
در این آپدیت، منوهای اضافی حذف شده‌اند و برنامه مستقیماً روی گزینه
Find Working IPs
برای تست کانفیگ‌های شما تمرکز دارد.
💻
نحوه استفاده:
* پس از اجرای برنامه، با کلیدهای جهت‌نما در منوی اصلی گزینه
Find Working IPs
را انتخاب کنید.
* لینک کانفیگ
vless://
یا
trojan://
خود را Paste کنید.
* تعداد آی‌پی‌ها برای تست (Count)، تعداد Workerها (به‌طور پیش‌فرض 50 که برای شبکه‌های محدودشده امن است) و مقدار Timeout را تنظیم کرده و با فشردن Enter اسکن را شروع کنید.
📥
دانلود و نصب:
* این ابزار به صورت فایل‌های کامپایل‌شده (Pre-built binary) برای سیستم‌عامل‌های ویندوز (x86_64)، لینوکس (ARM64 و x86_64) و مک (Intel و Apple Silicon) در دسترس است.
* برای دریافت، کافی است به صفحه Releases پروژه در گیت‌هاب (MatinSenPai/SenPaiScanner) مراجعه کنید.
* همچنین برای نصب سریع در لینوکس و مک می‌توانید از این اسکریپت استفاده کنید:
curl -fsSL [https://github.com/MatinSenPai/SenPaiScanner/raw/refs/heads/main/install.sh](https://github.com/MatinSenPai/SenPaiScanner/raw/refs/heads/main/install.sh) | bash
.
📌
#معرفی_ابزار
#اسکنر
#کلادفلر
#ویندوز
#لینوکس
#مک
#SenPaiScanner
#Cloudflare
#VLESS
#Trojan
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/5719" target="_blank">📅 10:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دوستان ببینید این کانفیگ واستون پینگ میده....
vless://c3e49c34-1177-42d1-8c7a-1b1fb2e269fe@45.130.125.76:443?path=%2Fproxyip%3D109.61.110.202&security=tls&encryption=none&insecure=0&host=javad-3yb.pages.dev&fp=chrome&type=ws&allowInsecure=0&sni=javad-3yb.pages.dev#CF%E5%AE%98%E6%96%B9%E4%BC%98%E9%80%8913
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/archivetell/5718" target="_blank">📅 10:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">vless://df1ad808-d628-4bdc-90ce-8f6465392207@91.107.243.68:80?path=%2F&security=none&encryption=none&host=play.google.com&type=ws#sadra-%20hetzner-500.00GB%F0%9F%93%8A
با ایرانسل آورد با ایرانسل تست کنید
500gb</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/5717" target="_blank">📅 10:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هوش مصنوعی برای دانشجوها
1.
perplexity.ai
➜ دستیار تحقیق
2.
hissab.io
➜ محاسبه هر چیزی
3.
otter.ai
➜ خودکارسازی یادداشت‌های سخنرانی
4.
stepwisemath.ai
➜ معلم ریاضی
5.
scholarcy.com
➜ خلاصه‌کننده مقاله
6.
caktus.ai
➜ ابزار مطالعه
7.
bookai.chat
➜ چت با کتاب‌ها
8.
chatdoc.com
➜ چت با اسناد
9.
textero.ai
➜ تولیدکننده مقاله
10.
jenni.ai
➜ نوشتن مقالات تحقیقاتی
11.
tome.app
➜ تولیدکننده ارائه
12.
plaito.ai
➜ معلم خصوصی
13.
heyscience.ai
➜ دستیار تحقیقات علمی
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/5716" target="_blank">📅 08:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">۲۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
😁
❤️
vless://99a7d8e7-f588-4d1f-a2c5-30cc94626c21@95.182.101.96:44535?encryption=none&fp=chrome&pbk=-0MP4KyHJ12AZ-z1YA5ITIjMOh8FUnGzSOSu2DFSgmI&security=reality&sid=de50a62ae9c03b&sni=www.yahoo.com&type=tcp#MOHRAZ-y28qfr8zv1-20.00GB%F0%9F%93%8A
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/5715" target="_blank">📅 08:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aigeo7nIGa696kompjS0MzujNgJ1CgCRXxphjceHjowIotFmzz_KB1C-Tbodp-DfA4aTkYtvIsJIgHlYBjS0Lbe1RbPwQLyiYkwMO0oFMGPRE2kIWyYN_nILPDSpUv8hVwlrJwFkZUi4BWNEwWzIqW1-766fvEA2QtQ5ZtvKm5UzMxasXj4Lh1DxlsveIWsMyCHBktlLIg_utRt-hQe1ozpmoW7xVMq3kaMOVp3f5zwUZg63p9ZQ3TPpR6xEb9pEQARakfs1_jlSy3qi95AycR1KVFaw6USV5Aiusfwa4AB9rLeFysYAaufbSh_0v2XCC2dkBhpNYCSFtlcDI0sZjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">SNI-Spofing----Plan B
coming soon
🔜
گویا پترنیها رو یک متود جدید کار می‌کنه که به راحتی میتونید فیلترینگ رو دور بزنید ..
اگه منتشر شد
آموزش رو واستون میزاریم...
❤️
@archivetell</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/5714" target="_blank">📅 04:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عه
رکب خوردی مشتی.....
🫵
😂
به جاش براتون آی‌پی تمیز کلود آوردم...
45.130.125.160
@archivetell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/5713" target="_blank">📅 04:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کانفیگ های
🇺🇸
🇳🇱
vless://4c5ec35b-d2aa-49be-a596-77c956aa40e9@31.57.63.70:12530?security=reality&encryption=none&pbk=odlIn9uuty8SSCafs7Dpka-jRTTUpiuJUuotikQU1i8&headerType=&fp=chrome&spx=%2FqlF7U3tRy88uURE&type=tcp&sni=www.yahoo.com&sid=dc6ed267aee4#5%DA%AF%DB%8C%DA%AF-5.00GB%F0%9F%93%8A
@archivetell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/5711" target="_blank">📅 02:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZKWL6QLS2mJY8AXKDUFXjn6CYvBtV0HRjcQmsr2vVget1Jobh4FmFnSJ_cDqyE76r1lRNKHSNsoUm8GG1wFDgJZWVcEX7yHRBYmsUemzX8NgI__Fxbkcl4eNd7WyA0p7tyMn2i6rPGJx7GLMeCsIgrCQa1RW7Vdl3b-FHaPjWpRHLR2OyNYGqjc8bVzHwOSBYsPrVvWYbfShgxr_KYybAh7B46KEUdcfZG-uigPCsBI8SwgehvMtVRiV_c3e4Y0-FdqaA8rLPFnaqPYSwBn4ZkR0S-BO4O5VckGtOvjgYUw8CE16X5qSSAHoXr880p4c2dINLVHu-fek8d34MEWDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به تازگی Vpn داخلی مرورگر Firefox در دسترس عموم قرارگرفته
📱
با آپدیت کردن این مرورگر روی سیستم خودتون میتونید از 50 گیگ ترافیک ماهانه استفاده کنین
⭐️
این قابلیت به تدریج برای همه کاربران فعال خواهد شد
😎
⬅️
@Archivetell</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/5709" target="_blank">📅 02:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚀
آموزش اتصال پایدار سایفون با دامنه‌های فستلی (Fastly)
---
رفقا
خبر خوب اینه که در حال حاضر روی شبکه فستلی (Fastly) خیلی از سایت‌ها باز شدن و می‌تونید از همین فرصت طلایی برای اتصال پایدار سایفون استفاده کنید!
این روش روی اپلیکیشن‌های
شیر و خورشید (ShiroKhorshid)
و
مهسا ان‌جی (MahsaNG)
در اندروید، و کلاینت
Se7en Pro
در ویندوز (یا کانفیگ‌های MitM+Psiphon) به خوبی جواب میده.
*(طبق تست‌های انجام شده، MahsaNG تو این متد اتصال بهتر و سریع‌تری نسبت به شیر و خورشید داره).*
###
🛠
آموزش تنظیمات:
۱. ابتدا یکی از دامنه‌های سفید زیر که پشت فستلی هستند رو انتخاب کنید (به عنوان SNI):
🔸
github.githubassets.com
🔸
docs.github.com
🔸
www.fastly.com
🔸
pypi.org
🔸
repo.almalinux.org
۲. حالا باید از دامنه‌ای که انتخاب کردید پینگ (Ping) بگیرید تا آی‌پی (IP) اون رو به دست بیارید.
⚠️
نکته بسیار مهم:
آی‌پی و SNI باید حتماً با هم مچ باشن! یعنی هر SNI که از لیست بالا انتخاب کردید، باید دقیقاً آی‌پیِ همون دامنه رو تو برنامه وارد کنید.
۳. تنظیمات برنامه رو دقیقاً روی این حالت‌ها قرار بدید:
🔹
Mode:
psiphon only
🔹
Protocol:
cdn_fronting
🔹
IP & SNI:
(آی‌پی و دامنه‌ای که در مراحل قبل پیدا کردید رو وارد کنید).
💡
وضعیت سرعت و پایداری:
به دلیل محدودیت‌های خود سایفون و تعداد بالای کاربران، سرعت این روش در حد متوسط (پخش یوتیوب با کیفیت 480p) هست؛ اما نقطه قوتش اینه که
کاملاً پایدار و بدون قطعی
کار می‌کنه و برای زمان‌های اختلال شدید، یه نجات‌دهنده عالیه.
📌
#فستلی
#Fastly
#سایفون
#مهسا_ان_جی
#MahsaNG
#شیر_و_خورشید
#Se7enPro
#CDN_Fronting
#آموزش
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/5708" target="_blank">📅 01:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5707">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">5 گیگ کانفیگ اهدایی از سرور آمریکا..
🇺🇸
vless://9a93ccb9-c010-417d-afec-b62ed1246ca7@31.57.63.70:12530?encryption=none&fp=chrome&pbk=odlIn9uuty8SSCafs7Dpka-jRTTUpiuJUuotikQU1i8&security=reality&sid=9a1fb502&sni=www.yahoo.com&spx=%2FoCtZeR0TiaFYTed&type=tcp#5%DA%AF%DB%8C%DA%AF-4.95GB%F0%9F%93%8A
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/5707" target="_blank">📅 01:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رفقا سلام!
✋
در این پست آموزش جامع راه‌اندازی اسکریپت بی‌نظیر CFnew (نسخه 2.9.8) رو براتون آماده کردیم. در این آپدیت، تمام باگ‌های یک ماه گذشته برطرف شده. این ابزار روی کلادفلر (Workers و Pages) اجرا میشه و یکی از کامل‌ترین پروژه‌هاست.
🔥
ویژگی‌های اصلی CFnew:
* پشتیبانی همزمان از پروتکل‌های VLESS، Trojan و xhttp.
* پنل گرافیکی قدرتمند: مدیریت کانفیگ‌ها تحت وب با دیتابیس KV (اعمال تغییرات در لحظه بدون نیاز به دیپلوی مجدد).
* Sub-converter داخلی: تولید کانفیگ کلاینت‌ها (Clash, Sing-box, V2rayNG و...) بدون نیاز به سرویس خارجی.
* پشتیبانی از ECH: دور زدن محدودیت‌های پیشرفته.
* تست پینگ داخلی: تست و انتخاب خودکار بهترین آی‌پی‌ها.
* پشتیبانی از رابط کاربری فارسی.
🛠
پیش‌نیازها:
یک اکانت کلادفلر + ساخت یک UUID معتبر از سایت
https://www.uuidgenerator.net
(این UUID رمز ورود شما به پنل خواهد بود).
💻
نصب روی Cloudflare Workers:
1. ساخت KV: در کلادفلر، از Storage ➔ KV یک Namespace جدید بسازید.
2. ایجاد Worker: در Workers & Pages یک ورکر جدید بسازید، کدهای قبلی را پاک و سورس CFnew را از گیت‌هاب پیست کنید (Deploy بزنید).
3. تنظیم متغیرها: در Settings ➔ Variables، متغیری با نام U (حرف بزرگ) بسازید و مقدارش را UUID خود قرار دهید.
4. اتصال KV: در Settings ➔ KV Bindings، دیتابیسی که ساختید را با نام C (حرف بزرگ) متصل (Bind) کنید.
5. تاریخ سازگاری: در Settings ➔ Runtime، گزینه Compatibility Date را روی 2026-01-20 تنظیم و ذخیره کنید.
6. اتصال دامنه: در Triggers ➔ Custom Domains، دامنه خود را متصل کنید.
🌐
نصب روی Cloudflare Pages:
1. آپلود فایل‌ها: در Workers & Pages یک Pages ایجاد کنید. با گزینه Direct Upload، فایل Zip پروژه را آپلود کنید.
2. تنظیمات: مشابه روش قبل، در Settings متغیر U (برای UUID) را ساخته و KV Bindings را با نام C متصل کنید.
3. تاریخ سازگاری: در Settings ➔ Runtime، تاریخ را روی 2026-01-20 تنظیم کنید.
4. دیپلوی مجدد (حیاتی): چون متغیرها فوراً اعمال نمیشن، به تب Deployments رفته، Create deployment را بزنید و همان فایل Zip را دوباره آپلود کنید تا پروژه از نو ساخته شود.
🔓
نحوه دسترسی به پنل مدیریت:
مرورگر را باز کرده و آدرس دامنه خود را به همراه UUID وارد کنید (مثال:
yourdomain.com/UUID
). در این پنل گرافیکی و فارسی، می‌توانید لینک‌های اتصال (Subs) بگیرید، ECH را مدیریت کنید و آی‌پی‌های تمیز وارد کنید.
🔄
نحوه آپدیت برای نسخه‌های بعدی:
* اگر از Worker استفاده می‌کنید: کدهای جدید را کپی، جایگزین کدهای قبلی کرده و Deploy کنید.
* اگر از Pages استفاده می‌کنید: در تب Deployments فایل Zip جدید را آپلود کنید (بدون نیاز به تنظیم مجدد).
📥
سورس کد و دانلود زیپ:
https://github.com/byJoey/cfnew
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/5704" target="_blank">📅 01:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">20 گیگ کانفیگ لوکیشن آمریکا...
🇺🇸
vless://d08a3998-d155-4541-9d46-85014b182ee8@45.39.230.25:42391?encryption=none&fp=chrome&pbk=vWLA2Hvig6fUErrisZvXBRs9ioeqegs_xmGkZf1uZ04&security=reality&sid=1608&sni=www.yahoo.com&spx=%2Fa91vwk8Tl6f5E3g&type=tcp#20%DA%AF%DB%8C%DA%AF-20.00GB%F0%9F%93%8A
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/5703" target="_blank">📅 23:47 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
❤️
vless://acd15093-fc20-418e-aeb6-e500d0509255@snapp.ir:8443?alpn=h2%2Chttp%2F1.1&encryption=none&host=shop.nex1shield.shop&path=%2F&security=tls&sni=shop.nex1shield.shop&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/5702" target="_blank">📅 23:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W29YqhAIc1YBXDYqQ-C9NryxSHCGpPi_wBRtesAajQIFHH_SpN1Q6Ns-42F8lP2IkVHf7Blnb_JplsHMoKVGVmwbDWVplmHueKPQ0H2XhY5YPcSHuQ38FN3Q2oHqXaGcb6UK0JGGxct1qwviGHfVcoxNZBerZLdxsWpLf82oLTRz02E0ne9quVJrwHOWMBTcqYr3-7nHB0rRkgu7k5WG5H9XXEDrTrsi8tkwGfF6pTw0EcUpP9RT8jPYiCZO_fMlmRF88m6KVbEX0plknyI69hxwNnUG8tcgch5NsvFWWyOazNPnN6qWbfrKQV9njX3yo7ikPDCR-HYzrAbhdg0NnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">SolveCaptcha
توسعه‌دهندگان راهی برای خودکار سازی عبور از کپچا پیدا کردند
چه چیزهایی پشتیبانی می‌شود:
🕤
reCAPTCHA v2/v3
🕤
Cloudflare Turnstile
🕤
FunCaptcha (Arkose Labs)
🕤
GeeTest و GeeTest v4
🕤
Amazon WAF و KeyCaptcha
🕤
Grid، Rotate، Canvas، ClickCaptcha
🕤
کپچاهای متنی، گرافیکی و صوتی معمولی
https://github.com/solvercaptcha/solvecaptcha-python
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/archivetell/5701" target="_blank">📅 22:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">output-addresses (11).txt</div>
  <div class="tg-doc-extra">18.4 KB</div>
</div>
<a href="https://t.me/archivetell/5700" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">۶۰ تا کانفیگ پشت کلودفلر
اهدایی یکی از ممبرای عزیز
❤️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/archivetell/5700" target="_blank">📅 21:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">۱۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
❤️
vless://2fd687a6-7b5f-491e-a7ff-a885da5504b1@se.sanaz.online:20609?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=2KojHs3QuIDI9X3HpOwIvEIhMy-54DLblBADeCuzlkU&security=reality&sid=0fe6d3442590&sni=www.yahoo.com&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/archivetell/5699" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5697">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دریافت هوش مصنوعی Anything — ۲۰ هزار اعتبار رایگان
🚀
دسترسی به برترین مدل‌های هوش مصنوعی در یک پلتفرم:
*
GPT-5.5
*
Claude Opus 4.7
*
Gemini 3.1 Pro
*
Kimi K2.6
نحوه دریافت:
* اینجا ثبت‌نام کنید:
Anything.com
* برای فعال‌سازی اعتبار رایگان خود از لینک زیر استفاده کنید
* دریافت از اینجا :
https://www.anything.com/signup?utmsource=promo&utmmedium=free-credit&utmcampaign=anythingplaystorelaunch&dubid=znvE3L0a0X3pl4Jz&promo=anythingplaystorelaunch
لذت ببرید
🎉
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/archivetell/5697" target="_blank">📅 19:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">۲۵ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
❤️
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo1REpYUnBtaTNpeXF4UTc5UGZLdjNC@195.93.253.240:14130#The%20Netherlands
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/archivetell/5694" target="_blank">📅 18:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">استفاده از Claude Opus 4.8 به صورت رایگان
👀
یک پلتفرم به نام Genspark AI به شما اجازه می‌دهد به بیش از ۱۵ مدل برتر هوش مصنوعی در یکجا دسترسی داشته باشید، از جمله
Claude Opus 4.8
GPT-5.5
Gemini 3.1 Pro
Grok 4
ثبت‌نام کنید، نیازی به کارت اعتباری نیست، روزانه ۱۰۰ اعتبار دریافت می‌کنید که هر ۲۴ ساعت تازه می‌شود.
فقط Claude Opus 4.8 در Anthropic ماهانه ۱۰۰ دلار هزینه دارد. اینجا آن را به همراه ۱۴ مدل دیگر رایگان دریافت می‌کنید.
واقعاً یکی از بهترین مجموعه‌های رایگان هوش مصنوعی موجود در حال حاضر است.
🔗
https://genspark.ai
@ArchiveTell
#AITools
#FreeAI</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/archivetell/5693" target="_blank">📅 18:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">۲۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
❤️
vless://b0785d2e-33cc-48b2-91d6-e1ed431fd849@panel.homan554.ir:45868?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=nyX6hzFp1vfyL5oPYp7Zpgn5jR5kZ_lTUN-wyx-YBG8&security=reality&sid=72&sni=github.com&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/5692" target="_blank">📅 18:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">به به حلوا و شیرینی
☕
🧁
ss://cmM0LW1kNToxNGZGUHJiZXpFM0hEWnpzTU9yNg@146.70.61.37:8080#ArchiveTell%20%F0%9F%87%AC%F0%9F%87%A7</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/archivetell/5691" target="_blank">📅 18:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">📌
فهرست جامع و راهنمای جستجوی مطالب کانال (آرشیو ابزارها و آموزش‌ها)
📱
۱. کلاینت‌ها، اپلیکیشن‌ها و ابزارهای اتصال
جدیدترین نسخه‌های برنامه‌های اتصال به همراه ابزارهای اختصاصی دور زدن نت ملی:
*
شیر و خورشید (ShiroKhorshid) / Se7enPro:
کلاینت‌های اختصاصی سایفون (اندروید و ویندوز) با قابلیت CDN Fronting. ➔
#شیر_و_خورشید
#Se7enPro
#سایفون
*
خانواده V2ray:
کلاینت‌های محبوب v2rayNG (نسخه‌های 2.1.7 و 2.1.8) برای اندروید و V2rayN برای ویندوز. ➔
#v2rayNG
#v2rayN
#v2ray
*
مهسا ان‌جی (MahsaNG):
نسخه v16 با قابلیت اتصال مستقل سایفون و دامین فرانتینگ. ➔
#MahsaNG
#مهسا_ان_جی
*
متد رله گوگل (mhrv-rs / MasterHttpRelayVPN):
کلاینت اتصال از طریق رله گوگل با زبان Rust و پایتون. ➔
#mhrv_rs
#MHRV
#رله_گوگل
*
اسکیرک (Skirk):
ابزار فوق‌العاده تونل کردن ترافیک از طریق Google Drive. ➔
#Skirk
#اسکیرک
#گوگل_درایو
*
زیرلن (Zyrln):
عبور از فیلترینگ با ترافیک ابری گوگل و کلادفلر ورکر. ➔
#Zyrln
#زیرلن
*
نوا پروکسی (NovaProxy):
پروکسی دسکتاپ با ترکیب Google Apps Script و Cloudflare. ➔
#نوا_پروکسی
#NovaProxy
*
بله وی‌پی‌ان (BaleVPN) و Whitelist Bypass:
تونل کردن اینترنت از طریق تماس صوتی/تصویری پیام‌رسان بله. ➔
#BaleVPN
#Whitelist_Bypass
#بله_میت
*
چشم عقاب (Eagle Eye):
دریافت آفلاین کانفیگ از طریق فرکانس شبکه‌های ماهواره‌ای. ➔
#چشم_عقاب
#Eagle_Eye
#آفلاین
*
کلاینت‌های iOS (آیفون):
برنامه‌های NexaTunnel و TheFeed (نسخه TestFlight). ➔
#NexaTunnel
#TheFeed
#آیفون
#iOS
*
سایر کلاینت‌ها و ابزارها:
NekoBox، V2box، Slipnet، MasterDns، OpenVPN، Happ، TunnelForge، HashemVasel و ابزار کلاینت لینوکسی XuiFactor. ➔ (اسم برنامه را سرچ کنید) یا
#کلاینت
#ابزار
🛠
۲. آموزش‌های طلایی و متدهای عبور از فیلترینگ
آموزش‌های قدم‌به‌قدم برای راه‌اندازی متدهای جدید:
*
متد SNI Spoofing:
آموزش دور زدن فیلترینگ با تزریق دامنه فیک (مثل hCaptcha) برای ویندوز (RM SNI Spoofer / Cloak)، لینوکس (FakeSNI)، و اندروید به همراه آموزش راه‌اندازی روی سرور ایران با پنل 3x-ui. ➔
#SNI_Spoofing
#FakeSNI
#اسپوف
#Cloak
*
آموزش‌های نتلیفای (Netlify) و ورسل (Vercel):
دیپلوی کانفیگ XHTTP، تغییر دامنه نتلیفای با کلادفلر ورکر برای رفع مسدودی، و اسکریپت XHTTP-Installer. ➔
#نتلیفای
#Netlify
#ورسل
#Vercel
#XHTTP
*
ترکیب سایفون و MitM:
آموزش متد Patterniha با گرفتن سرتیفیکیت (SSL) برای دور زدن DPI. ➔
#سایفون
#MitM
#سرتیفیکیت
*
اشتراک‌گذاری اینترنت آزاد (Hotspot/LAN):
آموزش انتقال اینترنت بدون فیلتر سیستم (V2ray یا SNI Spoof) به گوشی موبایل یا برعکس با برنامه‌های PdaNet+ و تنظیمات LAN/Proxy. ➔
#هات_اسپات
#LAN
#اشتراک_نت
#PdaNet
*
گیمینگ و پینگ پایین:
آموزش اتصال ویندسکرایب (Windscribe) روی SNI Spoofing برای کاهش پینگ در بازی‌ها. ➔
#گیمینگ
#پینگ
#Windscribe
#وینداسکرایب
*
لینوکس و ترمینال:
آموزش تونل کردن ترافیک ترمینال لینوکس با ابزار Proxychains4. ➔
#لینوکس
#Proxychains4
🔍
۳. اسکنرها و ابزارهای پیدا کردن آی‌پی (IP/SNI Scanners)
ابزارهای اختصاصی برای پیدا کردن آی‌پی‌های تمیز آکامای (Akamai) و فستلی (Fastly):
*
نتورک چکر (Network Checker):
اپلیکیشن همه‌کاره اندروید (v0.6.0) مجهز به اسکنر آکامای و کانفیگ‌ساز نتلیفای. ➔
#نتورک_چکر
#Network_Checker
*
اسکنرهای تحت وب و ویندوز:
CDN IP Finder (نسخه مرورگر)، AniScanner (داشبورد گرافیکی وب)، SNI-Radar و ابزارهای اسکن Akamai با PowerShell و Python. ➔
#اسکنر
#CDN_IP_Finder
#AniScanner
#اسکنر_آی_پی
*
لیست آی‌پی‌های آماده:
برای دسترسی به لیست‌های پینگ‌گرفته شده اپراتورها (ایرانسل، همراه اول، مخابرات، رایتل و سامانتل). ➔
#آی_پی_تمیز
#آکامای
#لیست_آی_پی
🤖
۴. ابزارها، اسکریپت‌ها و پروژه‌های خاص
ترفندها و ابزارهای کاربردی برای کارهای روزمره:
*
دانلودرها و ربات‌ها:
PlayDL (دانلود مستقیم از گوگل‌پلی)، MattDownloader (دانلودر با GitHub Actions) و ربات‌های هوش مصنوعی (Gemini, Claude, ChatGPT). ➔
#دانلودر
#PlayDL
#هوش_مصنوعی
#ربات
*
ایزی‌تل (EzyTel / Telemirror):
خواندن محتوای تلگرام به صورت آفلاین از طریق زیرساخت Google Translate. ➔
#ایزی_تل
#EzyTel
#تلگرام_آفلاین
*
سایر ترفندها:
ساخت شورت‌کات در Termux، مسدودساز آپدیت ویندوز (Windows Update Blocker)، ابزار Netlify obfuscator و مدیریت پروژه در VSCode. ➔
#ترموکس
#ترفند
#ویندوز</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/5688" target="_blank">📅 16:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚀
معرفی olcNG: فیلترشکن سریع، ساده و بهینه‌شده برای اندروید
---
رفقا سلام!
✋
امروز می‌خوایم یک اپلیکیشن بسیار جذاب و کاربردی به اسم
olcNG
رو بهتون معرفی کنیم. این برنامه در واقع یک نسخه (Fork) اوپن‌سورس و بهینه‌شده از اپلیکیشن محبوب
v2rayNG
هست که توسط تیم OpenLibreCommunity توسعه داده شده.
اگر از شلوغی و پیچیدگی‌های v2rayNG خسته شدید و دنبال یک جایگزین سریع‌تر، ساده‌تر و البته امن می‌گردید، olcNG دقیقاً همون چیزیه که بهش نیاز دارید!
###
✨
چرا olcNG رو پیشنهاد می‌کنیم؟
🔸
هسته (Core) فوق‌العاده قوی:
این اپلیکیشن برای مدیریت ترافیک و پردازش کانفیگ‌ها، از Xray-core و ماژول‌های قدرتمند
AndroidLibXrayLite
و
hev-socks5-tunnel
استفاده می‌کنه که باعث کاهش پینگ و افزایش چشمگیر سرعت اتصال میشه.
🔸
پشتیبانی کامل از تمامی پروتکل‌ها:
هر کانفیگی که در v2rayNG استفاده می‌کنید (مثل VLESS ،VMess ،Trojan و ShadowSocks)، بدون هیچ مشکلی در این برنامه قابل اجراست.
🔸
رابط کاربری (UI) بهینه‌شده:
برخلاف نسخه‌های اصلی که ممکنه برای کاربران عادی گیج‌کننده باشن، olcNG با یک طراحی بسیار ساده، سبک و کاربرپسند ارائه شده.
🔸
منبع باز و کاملاً رایگان (Open-Source):
این اپلیکیشن تحت لیسانس GPL-3.0 در گیت‌هاب منتشر شده که یعنی هیچ کد مخرب یا جاسوسی‌ای در اون وجود نداره و امنیتش تضمین شده است.
---
###
💻
دانلود و نصب:
نسخه جدید این اپلیکیشن (v4.2.1) به تازگی منتشر شده و با اندرویدهای جدید کاملاً سازگاری داره. برای دانلود مستقیم نسخه رسمی، می‌تونید از لینک گیت‌هاب پروژه استفاده کنید:
🔗
لینک دانلود مستقیم از گیت‌هاب:
🌐
https://github.com/openlibrecommunity/olcng/releases/tag/v4.2.1
*(در صفحه باز شده، روی فایلِ با پسوند
.apk
کلیک کنید تا دانلود شروع شود).*
🔗
سایت رسمی پروژه:
zarazaex.xyz
📌
#معرفی_اپلیکیشن
#اندروید
#فیلترشکن
#olcNG
#v2rayNG
#Xray
#VLESS
#Bypass
#Vpn
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/archivetell/5687" target="_blank">📅 16:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚀
این سایت یه معدن طلایِ هوش مصنوعیه: از ساخت حرفه‌ای‌ترین پرامپت‌ها تا ویرایش عکس و ساخت موزیک رایگان!
---
اگر از ChatGPT یا Claude استفاده می‌کنید اما خروجی‌های دقیقی نمی‌گیرید، یا دنبال ابزارهای رایگان برای تولید محتوا هستید، سایت
The Prompt Index
همون چیزیه که بهش نیاز دارید. این سایت فقط یک پرامپت‌ساز نیست، بلکه یک "جعبه‌ابزارِ دیوانه‌کننده" است که امکانات پولی ده‌ها سایت مختلف رو یکجا و رایگان جمع کرده!
کافیه یک
اکانت کاملاً
رایگان
(0$)
بسازید تا به این گنجینه دسترسی پیدا کنید:
📝
۱. ماشین جادویی پرامپت‌سازی (Prompt Generator)
با این ابزار، کیفیت جواب‌هایی که از هوش مصنوعی می‌گیرید ۱۰ برابر بهتر میشه!
🔸
دارای ۲۲۸ فریم‌ورک استاندارد در ۲۵ دسته‌بندی مختلف (از برنامه‌نویسی تا حل مسئله).
🔸
حالت مبتدی (Wizard):
فقط با جواب دادن به ۴ سوال ساده، حرفه‌ای‌ترین دستور رو براتون می‌نویسه.
🔸
حالت حرفه‌ای (Expert):
امکان ترکیب قالب‌ها برای کارهای فوق‌تخصصی.
🎁
۲. سوئیت ابزارهای رایگان (AI Toolbox)
🎵
موزیک و صدا:
ساخت ۲ ترک موسیقی در روز، ۵۰ دقیقه تغییر صدای هوش مصنوعی در ماه و ساخت ۱۰ افکت صوتی روزانه!
🖼
ویرایش تصویر حرفه‌ای:
افزایش کیفیت عکس (Upscaler)، حذف پس‌زمینه و واترمارک، ترمیم و گسترش ابعاد عکس (هر کدوم ۱ تا ۲ بار رایگان در روز).
📚
کتاب‌ساز و نویسندگی:
ابزار PromptBook برای ساخت یک کتاب کامل به همراه عکس جلد در ماه، ابزار Humanizer (انسانی‌سازی متن برای دور زدن ربات‌ها) و استخراج متن از PDF.
💡
نتیجه‌گیری:
پیدا کردن سایتی که مجموعه‌ای از بهترین ابزارهای موسیقی، تصویر، متن و پرامپت‌نویسی رو یکجا و رایگان در اختیارتون بذاره واقعاً غنیمته. حتماً سیوش کنید که به کارتون میاد!
🔗
لینک ورود و استفاده از ابزارها:
🌐
https://www.thepromptindex.com/
📌
#هوش_مصنوعی
#پرامپت
#ابزار_کاربردی
#تولید_محتوا
#ویرایش_عکس
#ساخت_موزیک
#کتاب_ساز
#AI
#رایگان
#پرامپت_نویسی
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/archivetell/5686" target="_blank">📅 14:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚀
آموزش ساخت امن‌ترین کانفیگ‌های VLESS REALITY (پروتکل غیرقابل فیلتر!)
---
رفقا سلام!
✋
خیلی‌هاتون پرسیدید این کانفیگ‌های قدرتمندی که براتون می‌ذاریم دقیقاً چطوری ساخته میشن؟
امروز می‌خوایم قدم‌به‌قدم بهتون یاد بدیم چطور روی پنل
سنایی (3x-ui)
دقیقاً همین کانفیگ‌های فوق‌امنیتی رو برای خودتون بسازید!
🛠
مراحل ساخت کانفیگ:
۱. تنظیمات پایه (Basic Settings):
بعد از ورود به پنل، یه Inbound جدید بسازید:
🔸
پروتکل (Protocol):
روی
vless
قرار بدید.
🔸
پورت (Port):
ترجیحاً
443
(یا پورت‌های آزاد سرورتون) باشه.
۲. تنظیمات شبکه (Network):
🔹
بخش
Network:
روی
tcp
باشه.
🔹
تیک
Reality
رو حتماً روشن کنید تا تنظیماتش باز بشه.
۳. تنظیمات استتار (Reality Settings) - مهم‌ترین بخش:
حالا باید ترافیکمون رو پشت یک سایت معروف مخفی کنیم:
🔸
در کادر
dest:
آدرس یک سایتِ بدون فیلتر رو با پورت ۴۴۳ بنویسید (مثلاً
www.microsoft.com:443
).
🔸
در کادر
serverNames:
همون سایت رو بدون پورت وارد کنید (مثلاً
www.microsoft.com
).
🔸
روی دکمه
Generate
کلیک کنید تا کلیدهای رمزنگاری (Private Key) و کدهای کوتاه (ShortIds) به صورت خودکار براتون ساخته بشن.
۴. ساخت کاربر و فعال‌سازی Vision:
حالا برید پایینِ صفحه تو بخش Clients و روی
+ Add
کلیک کنید:
🔹
ایمیل (ID):
یه اسم دلخواه برای کانفیگ بذارید.
🔹
⚠️
نکته طلایی:
در قسمت
Flow
، حتماً گزینه
xtls-rprx-vision
رو انتخاب کنید (این همون جادوییه که باعث دور زدن سیستم فیلترینگ و کاهش چشمگیر پینگ میشه).
✅
ذخیره و استفاده:
دکمه Save رو بزنید! تمام شد!
حالا روی آیکون QR Code کلیک کنید و لینک کانفیگتون رو کپی کنید. اگر به لینک دقت کنید، می‌بینید که دقیقاً همون ساختار حرفه‌ایِ Vless Reality رو داره. کانفیگ رو تو v2rayNG یا NekoBox کپی کنید و از اینترنت آزاد لذت ببرید!
✌️
📌
#آموزش
#فیلترشکن
#سرور
#پنل_سنایی
#VLESS
#Reality
#Vision
#کانفیگ
#تونل
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/archivetell/5685" target="_blank">📅 10:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚀
معرفی پنل PasarGuard: نسل جدید و قدرتمند مدیریت پروکسی و ضدسانسور
---
امروز قصد دارم یک پنل مدیریت سرورِ بسیار مدرن، جامع و قدرتمند به اسم
PasarGuard
رو بهتون معرفی کنم. این پنل با زبان‌های Python و React.js نوشته شده و با ترکیب Xray-core و WireGuard، یک رابط کاربری بی‌نظیر برای مدیریت صدها اکانت به صورت همزمان به شما میده.
اگر دنبال یک پنل حرفه‌ای با امکانات توزیع‌شده (Multi-Node) هستید، پاسارگارد یکی از بهترین انتخاب‌هاست!
✨
مهم‌ترین ویژگی‌های پنل PasarGuard:
🔸
پشتیبانی کامل از مدرن‌ترین پروتکل‌ها:
پشتیبانی از Vmess ،VLESS ،Trojan ،Shadowsocks ،WireGuard و Hysteria2 به همراه قابلیت‌های TLS و REALITY.
🔸
مدیریت پیشرفته کاربران:
امکان استفاده از یک کاربر برای چندین پروتکل، پشتیبانی از چند کاربر روی یک اینباند، و تعریف فال‌بک (Fallbacks).
🔸
محدودیت‌های هوشمند:
قابلیت تنظیم محدودیت حجم و زمان، و همچنین
محدودیت‌های دوره‌ای
(ریست شدن حجم به صورت روزانه، هفتگی و...).
🔸
سابسکریپشن استاندارد:
تولید لینک سابِ کاملاً سازگار با کلاینت‌های V2ray ،Clash و ClashMeta به همراه تولید خودکار QR Code.
🔸
امکانات جانبی قدرتمند:
دارای ربات تلگرامی اختصاصی، محیط خط فرمان (CLI)، دیتابیس‌های متنوع، API کامل و مانیتورینگ دقیق ترافیک.
---
💻
آموزش نصب سریع (روی لینوکس):
توسعه‌دهندگان، استفاده از دیتابیس
TimescaleDB
رو برای این پنل پیشنهاد دادن. کافیه به سرور متصل بشید و دستور زیر رو کپی و اجرا کنید:
curl -fsSL [https://github.com/PasarGuard/scripts/raw/main/pasarguard.sh](https://github.com/PasarGuard/scripts/raw/main/pasarguard.sh) -o /tmp/pg.sh \\
&& sudo bash /tmp/pg.sh install --database timescaledb
پس از پایان نصب، برای ساخت نام کاربری و رمز عبورِ مدیر (Admin)، دستور زیر رو وارد کنید (به جای
<username>
نام دلخواهتون رو بنویسید):
pasarguard cli admins --create <username>
🌐
نحوه ورود به پنل:
پنل روی پورت
8000
اجرا میشه و برای ورود به آدرس
https://YOUR_DOMAIN:8000/dashboard
نیاز دارید. *(نکته مهم: برای امنیت بیشتر، پنل پاسارگارد الزاماً به سرتیفیکیت SSL و اتصال HTTPS نیاز دارد).*
🔗
لینک گیت‌هاب پروژه برای اطلاعات بیشتر:
🌐
https://github.com/PasarGuard/panel
📌
#معرفی_ابزار
#پنل
#PasarGuard
#پاسارگارد
#فیلترشکن
#سرور
#Xray
#VLESS
#Hysteria2
#Wireguard
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/archivetell/5684" target="_blank">📅 03:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚀
انتشار آپدیت بزرگ و جذاب پنل 3x-ui (نسخه v3.2.0)
---
آپدیت جدید و پر از امکاناتِ پنل مدیریت سرور محبوب
3x-ui
(نسخه سنایی) منتشر شد. این نسخه (v3.2.0) یکی از بزرگترین آپدیت‌های این پروژه است که تمرکز ویژه‌ای روی مدیریت گروهی کاربران، بهبود رابط کاربری و ارتقای پروتکل‌های دور زدن فیلترینگ داشته.
###
✨
مهم‌ترین تغییرات و قابلیت‌های جدید:
🔸
مدیریت حرفه‌ای گروه‌ها:
اضافه شدن صفحه اختصاصی برای گروه‌بندی کلاینت‌ها (Client Groups) و امکان خروجی گرفتن لینک سابسکریپشن مجزا برای هر گروه.
🔸
پشتیبانی از XHTTP پیشرفته:
اضافه شدن تنظیمات حرفه‌ای XHTTP و پروکسی‌های خارجی TLS (قابلیت بسیار مهم برای شرایط فعلی فیلترینگ).
🔸
عملیات گروهی کلاینت‌ها (Bulk Actions):
امکان اضافه، حذف، انتقال و تخصیص گروه به کلاینت‌ها به صورت دسته‌جمعی.
🔸
فیلترهای پیشرفته:
اضافه شدن دراور (Drawer) فیلتر جدید برای پیدا کردن سریع کلاینت‌ها بر اساس حجم مصرفی، تاریخ انقضا، پروتکل و وضعیت اتصال.
🔸
امنیت و بهینه‌سازی دیتابیس:
اختصاص Role رندوم برای دیتابیس PostgreSQL جهت امنیت بیشتر و بهینه‌سازی استخر اتصالات (Pool Tuning) برای جلوگیری از افت منابع سرور.
🔸
ارتقای پروتکل‌ها:
اضافه شدن قابلیت Salamander auto-seed برای پروتکل Hysteria و قرار گرفتن فیلد Testseed برای VLESS Vision.
🔸
بهبود رابط کاربری:
بازنویسی و مدرن‌سازی کامل فرانت‌اند پنل با TypeScript و اضافه شدن داکیومنت‌های API به داخل خود پنل.
###
🛠
مهم‌ترین باگ‌های برطرف‌شده:
🔹
حل مشکل قرار نگرفتن SNI در لینک‌های اشتراک‌گذاری REALITY.
🔹
حفظ انکودینگ صحیحِ اطلاعات کاربران در لینک‌های Trojan، ShadowSocks و Hysteria.
🔹
رفع مشکل تداخل External-proxy با SNI در اتصال‌های TLS.
---
💻
نحوه آپدیت:
برای آپدیت به این نسخه، کافیه به سرورتون SSH بزنید، دستور
x-ui
رو در ترمینال وارد کنید و از منوی باز شده، گزینه آپدیت به آخرین نسخه رو انتخاب کنید.
🔗
مشاهده لیست کامل تغییرات در گیت‌هاب:
🌐
https://github.com/MHSanaei/3x-ui/releases/tag/v3.2.0
📌
#آپدیت
#پنل
#سنایی
#فیلترشکن
#سرور
#Xray
#VLESS
#XHTTP
#Hysteria
#مدیریت_سرور
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/archivetell/5683" target="_blank">📅 03:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚀
آموزش نصب سریع Hysteria 2 روی سرور اوبونتو (بدون قطعی)  ---  رفقا سلام!
✋
پروتکل Hysteria 2 به دلیل شبیه‌سازی ترافیک به HTTP/3، در حال حاضر یکی از مقاوم‌ترین روش‌ها برای عبور از سیستم‌های فیلترینگ (DPI) است. در این پست، نحوه نصب سریع و بهینه این پروتکل رو…</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/archivetell/5682" target="_blank">📅 02:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5681">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚀
آموزش نصب سریع Hysteria 2 روی سرور اوبونتو (بدون قطعی)
---
رفقا سلام!
✋
پروتکل Hysteria 2 به دلیل شبیه‌سازی ترافیک به HTTP/3، در حال حاضر یکی از مقاوم‌ترین روش‌ها برای عبور از سیستم‌های فیلترینگ (DPI) است. در این پست، نحوه نصب سریع و بهینه این پروتکل رو روی یک سرور مجازی (اوبونتو 22.04 یا 24.04) آموزش می‌دیم:
۱. آپدیت سرور و نصب پیش‌نیازها
ابتدا به سرور خود متصل شده و دستورات زیر را کپی و اجرا کنید:
sudo apt update && sudo apt upgrade -y
sudo apt install curl wget ufw fail2ban -y
۲. نصب Hysteria 2
با اجرای دستور زیر، پروتکل به صورت خودکار نصب می‌شود:
Bash
bash <(curl -fsSL [https://get.hy2.sh/](https://get.hy2.sh/))
۳. تنظیم کانفیگ سرور
دستور زیر را بزنید تا فایل تنظیمات باز شود:
Bash
nano /etc/hysteria/config.yaml
سپس کدهای زیر را کپی کرده و داخل آن قرار دهید:
(نکته: در بخش password، حتماً یک رمز قوی برای خودتان بنویسید)
YAML
listen: :443
auth:
type: password
password: "Your_Strong_Password_Here"
masquerade:
type: proxy
proxy:
mode: remote
addr: [https://www.apple.com](https://www.apple.com)
quic:
initStreamReceiveWindow: 8388608
maxStreamReceiveWindow: 16777216
initConnReceiveWindow: 8388608
maxConnReceiveWindow: 16777216
maxIdleTimeout: 30s
activeConnIdleTimeout: 30s
disablePathMTUDiscovery: false
bandwidth:
up: 100 Mbps
down: 100 Mbps
udpForwarding: true
برای ذخیره فایل، کلیدهای
Ctrl+X
سپس
Y
و در نهایت
Enter
را بزنید.
۴. باز کردن پورت‌ها در فایروال
برای عملکرد صحیح، باید پورت ۴۴۳ از نوع UDP را باز کنید:
Bash
sudo ufw allow 443/udp
sudo ufw enable
۵. راه‌اندازی و اجرای نهایی
Bash
sudo systemctl daemon-reload
sudo systemctl enable hysteria
sudo systemctl restart hysteria
📱
تنظیمات برای اتصال در گوشی یا ویندوز:
در برنامه‌هایی مثل NekoBox ،v2rayNG یا Exclave یک پروفایل جدید از نوع
Hysteria 2
بسازید و اطلاعات زیر را وارد کنید:
🔸
Server:
آی‌پی سرور شما
🔸
Port:
443
🔸
Password:
رمزی که در فایل کانفیگ تعیین کردید
🔸
SNI / Masquerade:
www.apple.com
🔸
Skip Cert Verify (Insecure):
True
(حتماً فعال شود)
✅
تمام! حالا یک کانکشن به شدت پایدار و پرسرعت دارید. اگر در مراحل نصب سوالی داشتید، توی کامنت‌ها بپرسید.
👇
📌
#آموزش
#سرور
#فیلترشکن
#Hysteria2
#Hy2
#اوبونتو
#V2ray
#تونل
#VPS
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/archivetell/5681" target="_blank">📅 02:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">https://t.me/boost/archivetell</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/archivetell/5680" target="_blank">📅 22:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⚠️
خدمت دوستان باید چند نکته مهم رو بگم:
هیچ تاثیری روی پروتکل های tcp , udp ,ikev2, wstunnel رو هر حالتی از سانسورشیب بزارید از کانفیگ A تا حتی H و I باشه هیچ تاثیری در وصل شدن سریعتر شما اصلا نداره! فقط این حالت برای وایرگارد قابل استفاده هست دقت کنید
نکته بعدی این هستش که شما حالت server routing رو هم حالت اتوماتیک بزارید چه حالت regular و حتی alternative هیچ تاثیری باز هم تو اتصال شما نداره فقط و فقط حالت اتوماتیک بزارید
مورد اخر گزینه large tls هم روشن بزارید چون به اتصال بهتر شما کمک میکنه وقتی خاموش باشه سخت تر وصل میشید در کل این ۳ مورد رو دوستمون دقت نکردن و نیاز بود این مورد حتما رو بگم که سرگردان تغییر کانفیگ های A,b,c نشید
❤️
#windscribe
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/archivetell/5679" target="_blank">📅 21:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">۱۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
❤️
vless://80fbb3e8-d705-4eca-a519-fd82fd6d319a@46.38.137.141:38554?type=tcp&encryption=none&security=none#%40IR_SI%20%2F%20100GB%20UAE%F0%9F%87%A6%F0%9F%87%AA-nubknlau-tpbvyzw1
http://46.38.137.141:2096/sub/eyovzx7b813yvs6g
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/archivetell/5678" target="_blank">📅 21:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کانفیگ های اهدایی یکی از ممبرای عزیز
❤️
حجم ۲۰۰ گیگ
vless://5de57aca-c66e-49c6-9bae-fb5eef64d832@sv2.vaslimgroup.ir:8880?encryption=none&host=vaslimgroup.ir&path=%2F&security=none&type=ws#vaslim%20economy-ArchiveTel%20vip-asli-200.00GB%F0%9F%93%8A
vless://5de57aca-c66e-49c6-9bae-fb5eef64d832@snapp.ir:8880?encryption=none&host=vaslimgroup.ir&path=%2F&security=none&type=ws#vaslim%20economy-ArchiveTel%20vip-%F0%9F%92%9Asnapp%F0%9F%92%9A-200.00GB%F0%9F%93%8A
vless://5de57aca-c66e-49c6-9bae-fb5eef64d832@tapsi.ir:8880?encryption=none&host=vaslimgroup.ir&path=%2F&security=none&type=ws#vaslim%20economy-ArchiveTel%20vip-%F0%9F%A9%B7tapsi%F0%9F%A9%B7-200.00GB%F0%9F%93%8A
vless://5de57aca-c66e-49c6-9bae-fb5eef64d832@anten.ir:8880?encryption=none&host=vaslimgroup.ir&path=%2F&security=none&type=ws#vaslim%20economy-ArchiveTel%20vip-%F0%9F%94%B1anten%F0%9F%94%B1-200.00GB%F0%9F%93%8A
هر ۷ تا رو اد کنید ، بعضی مناطق بعضی هاشون کار میده
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/archivetell/5677" target="_blank">📅 21:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پروکسی اهدایی یکی از ممبرای عزیز
❤️
https://t.me/proxy?server=hh87.salarjavidan.online&port=8991&secret=f41d30c2e0ca3895ca053b26d98af5b3
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/archivetell/5676" target="_blank">📅 21:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚀
معرفی فیلترشکن جدید و هوشمند Defyx VPN (نسخه v5.3.9)
---
امشب قصد دارم یک فیلترشکن متن‌باز (Open-Source) و بسیار قدرتمند به اسم
Defyx VPN
رو بهتون معرفی کنم که آپدیت جدیدش به تازگی در گیت‌هاب منتشر شده.
این اپلیکیشن رابط کاربری فوق‌العاده تمیز و ساده‌ای داره و بزرگترین مزیتش اینه که
نیازی به هیچ‌گونه تنظیمات دستی یا وارد کردن کانفیگ نداره!
✨
ویژگی‌های کلیدی Defyx:
🔸
هسته قدرتمند DXcore:
این برنامه در پس‌زمینه، ترکیبی از بهترین پروتکل‌های ضدسانسور دنیا یعنی
Xray, Warp, Psiphon, Outline
و
Warp-in-Warp
رو در خودش جا داده و به صورت هوشمند از اون‌ها استفاده می‌کنه.
🔸
اتصال تک‌کلیکی (One-Tap):
فقط کافیه دکمه اتصال رو بزنید تا خودش بگرده و بهترین مسیر رو برای دور زدن فیلترینگ پیدا کنه.
🔸
ابزار تست سرعت:
دارای اسپیدتست داخلی برای بررسی کیفیت و پینگ اینترنت شماست.
🔸
پشتیبانی کامل:
برای اندروید، آیفون، مک و ویندوز در دسترسه.
---
📥
لینک‌های دانلود رسمی:
🤖
برای اندروید:
🔗
[دانلود مستقیم از گوگل پلی](
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
)
🔗
[دانلود فایل APK از گیت‌هاب](
https://github.com/UnboundTechCo/defyxVPN/releases/download/v5.3.9/app-release.apk
)
🍎
برای آیفون، آیپد و مک (iOS/macOS):
🔗
[دانلود مستقیم از اپ استور](
https://apps.apple.com/us/app/defyx/id6746811872
)
💻
برای ویندوز:
🔗
[دانلود مستقیم نسخه پرتابل (بدون نیاز به نصب)](
https://github.com/UnboundTechCo/defyxVPN/releases/download/v5.3.9/windows-release.zip
)
📌
#فیلترشکن
#معرفی_اپلیکیشن
#اندروید
#آیفون
#ویندوز
#Xray
#Warp
#Psiphon
#DefyxVPN
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/archivetell/5675" target="_blank">📅 20:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آب را گل آلود کن و ماهی بگیر از این آب گل آلود...</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/archivetell/5674" target="_blank">📅 20:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwXilJi2XkuRX10XuotvW87mqdjpkrYYo2S4ShqOm-faQifC2UdjeEFWKxslXEH-jNHwIZSD8muRXHkZ4WDJhogb-ysi513jimwZeAmUjJZGzy05TNYGUXxFhI2z2zjtANmbMgf_Z0jE5zAl48k2lWTydq9LDjSDBE7jIQh8dZDYGfuhjm6jnhEUUV9AVmTdVAyexP3BncocivZlR76EAIDtclX5qCBdBFsJoTN1tUoKh72hxQt61jzhqsPOp_pB3yscQz5S9Q7MdnL40zw1QJoALGLrS-9EsGTI9o0MVgl9jgqQPIFUFbcQPoiCMjB5roLBZeSa25AQ3FPcVv8EaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به عامل کدنویسی هوش مصنوعی خود، یک سیستم طراحی در یک فایل markdown بدهید.
Awesome DESIGN .md
مجموعه‌ای از فایل‌های طراحی است که از وب‌سایت‌های واقعی متمرکز بر توسعه‌دهندگان الهام گرفته شده‌اند. شما یکی از آن‌ها را در پروژه خود قرار می‌دهید، به عامل هوش مصنوعی خود می‌گویید چه چیزی بسازد و از آن فایل به عنوان یک راهنمای سبک بصری استفاده می‌کند.
بدون خروجی Figma. بدون تنظیمات پیچیده. فقط markdown که به عامل می‌گوید رابط کاربری چگونه باید به نظر برسد و چه احساسی داشته باشد.
https://github.com/VoltAgent/awesome-design-md
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/archivetell/5673" target="_blank">📅 19:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نانوبنانا پرو رایگان می‌خوای؟
بفرمایید اینم یه ابزار خفن از گوگل:
https://labs.google/fx/tools/flow
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/archivetell/5669" target="_blank">📅 17:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مخابرات و همراه اول وصل
Windscribe
TCP, 443, Paris Seine
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/archivetell/5667" target="_blank">📅 17:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5666">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">اکسپرس برلین آلمان سوپر وصله</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/archivetell/5666" target="_blank">📅 17:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LulDMRx7ETlw7hpnfa5CC5_Yd5icoYCDcqyya9EtSjsIDB8qSiqHCeuhpUQqhB5xseNztG9IZMs5_tv4a5svomFtvMzmEQXKwwvObWHjx7EDXXoisBklf3UqniCVe2N4dDGOWYqRvTbrB3xlTxMpNL3zf-X_R01Pba4jVXMapP73LaADZMnEekXHPo5LVIq8FpSxYYYpVCwpyGnMcnPG7MgG_7dJvR9FiqlnwvO3c4CD1hXlYgrCWOZe5iazTJhLnwcC06EsNIaDcqxBSlEqNe6lhJGGy6flL_onxS6IArv7Yd33pHnJFAuRlveon7Du7hsHv1yvwg0VsJenWNjX1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HF3bmSvoQ0v-H0Ye4mx2dFO72JkjKwWKgVTp_lyZBHVgUQ0Q81KwB5FmU-HbbAUOlYZpcgVAXJtk8hgD7IZ4be0FqBif-oVQ49zJPYuiLz4zu3ksV6AqwIHvq_a1ObHL0C36yMnlclKGkmoqC0jr7gItnT6LAwvcJBDYxh3DRp2VoRZZ0ahd8urMy6kQUDrluzQMGERn31JA-6i8B1tpO62XMtpB00mvZRieuK_PZFI5DnJeDz0nltC6KVgD2FKF5fL_sBHmjE7L-9QePzU2sGj14JZrfRe3neILA1EugpKlRW5DzCIJSuE_QoHukrODyhnbOju1yQFN6fYMpqGfWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZDJBapfGnIEM4AAMgMB_QmR-5yjUve0ET9Nt8r6zmYVqBlkGCIjyanh0gOmA0Te-qWMfU2Xl6lkYS6elGYLk3H5kwWnCqpAMA0N2PpMZ5Gln5fxuLjaVPRKWiwd2PhTQ7iSjrhTn612LkNzS_68h8H4MDFVn0F2tx3AsR5x3VmbDB5QcNDD3Y1X1p2dM6bEPke5mAo8Zf12zo5mHMfekE_n0y9lmEvywroGnXbmZCAUQTg-g_v-4QDis8DF1DpebGSJ3gacxOXe4JCmKB3E1BOJpH2W5UTy7yDEvaXOnPibfIH5Acx8IEvahQxvlq864AvX05s9gm0UkfpNwU5E4yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر هنوز دسترسی به اینترنت جهانی براتون باز نشده و مجبورید از DNS Tunelling استفاده کنید:
با قابلیت جدید DNS Pool دیگه نیازی نیست دستی دنبال DNS بگردید یا اسکن کنید. می‌تونید تا ۱۰۰۰ تا DNS به برنامه بدید تا خودش قبل اتصال تستشون کنه و ۱۰ تا از بهترین‌ها رو خودکار براتون انتخاب کنه.
🕊
@slipnet_app</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/archivetell/5663" target="_blank">📅 17:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5662">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مسئله فقط اینترنت نبود
ما را از جهان در حال حرکت جا گذاشتند
صدا ها خاموش شد ، آدم ها فراموش شدند
و گل هایمان یکی یکی پر پر شدند
زخم این دوران هیچ وقت از دل ما پاک نمی شود..
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/archivetell/5662" target="_blank">📅 16:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">برای گرفتن 15 گیگ برای اکانت ویندتون باید اول ایمیلتون رو تایید کنین با اینکار 10 گیگ بهتون میده
🆓
برای 5 گیگ اضافه باید توی سایتش لاگین کنید Tweet 4 Data این گزینه رو پیدا کنین یه توییت بزنین براش منشن کنین و تمام 5 گیگ دیگه هم براتون فعال میشه
👑
👥
موقع ثبت نام، اینو بزنین ی گیگ اضافی هم به شما اضافه میشه
Declinedrice
⛈
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/archivetell/5661" target="_blank">📅 15:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gDNh8zTu5j7phsGpwOv37mu-x12ZIJejOFwCLKw_l88DiqjfJRsrjDEgp8S0oHAF7iGRdo0q57FAosEjNz61AYIvhXnEmh33pUMcL-aqz0ifnt5B16VlLNQvC5HtrviIYZy3zbN_zLhbthHdWm_hL9XD_lHI3h2Emzji7vjEGiSmiHq1esKIJVE-I3klJ8sUbpnKaxcOtP24abW0zi6IVzvyCMdx6q1GFL7Z_9GvRkaHI6Gv9sLKSKD4DhGrcljWaEtS6cT2HcNDXjOiHx47Ja9jxcaUoLdLR4e-lMHJdC3gNyCdqOhPmpw99zQB3P6pXpJS_h7W4QWHQNW_8QqTlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cvD__dSpIJYAI7EwIfTWhBCyjgSbG__QjjEhjU2i12ayMA5pgn0nnFRrxRFHKfkFceN3MLkhuCA5QtFNV1AxIj--I7ga8lcjAa7yAtLOpIIIyK6cfrHnAyo85Qss-n7APEYXdDBYop0O6s3JxYrkFmtuf39pg_dIqZyANvi6OzmIWz7-m_RZxr0VfDxJIpf6pq59pBpU65QGel4QGSj8OqhV2x1LTKP2r5Bvntr4hHmnb7gsYqDcKaj9e_NxzUaFPhqbEM9oB6HHShLVDLufJkIGHv3jqe0Cz7GsLVEeHB140qBPUfzjlS8qEW_Sru8rLZf2-b_zLJNrOIdzarCCMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وینداسکرایب روی همراه آخر روی Tcp پورت 443 وصله
🛜
از تنظیمات قسمت
connection
بخش
Anti censorship
باید
Protocol tweaks
رو
Enabled
کنین و یکی از گزینه های
iran experimental
رو انتخاب کنین
✅
تیک
Large Tls
رو هم بزنین
حالا کافیه روی tcp 443 رو هر کشوری که میخواید کانکت شید
🧬
✈️
@Archivetell</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/archivetell/5659" target="_blank">📅 14:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🛠
معرفی جعبه‌ابزار قدرتمند cfray: همه‌چیز برای VLESS و Cloudflare در یک فایل!  ---  رفقا سلام!
✋
امروز یک ابزار پایتونیِ به شدت کاربردی و جذاب به اسم cfray (ساخته‌شده توسط تیم SamNet) رو بهتون معرفی می‌کنیم.  این ابزار که قبلاً فقط یک اسکنر کانفیگ بود، حالا…</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/archivetell/5658" target="_blank">📅 14:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🛠
معرفی جعبه‌ابزار قدرتمند cfray: همه‌چیز برای VLESS و Cloudflare در یک فایل!
---
رفقا سلام!
✋
امروز یک ابزار پایتونیِ به شدت کاربردی و جذاب به اسم
cfray
(ساخته‌شده توسط تیم SamNet) رو بهتون معرفی می‌کنیم.
این ابزار که قبلاً فقط یک اسکنر کانفیگ بود، حالا در نسخه ۱.۱ تبدیل به یک "چاقوی سوئیسی" همه‌کاره برای دور زدن فیلترینگ و مدیریت سرورهای Xray شده.
💡
بهترین ویژگیش چیه؟
این برنامه هیچ پیش‌نیازی (Dependency) نداره! فقط پایتون 3.8 به بالا روی ویندوز یا لینوکس نیازه و تمام کارها رو با یک فایل
scanner.py
انجام میده.
✨
قابلیت‌های اصلی و جذاب cfray:
🔸
اسکنر کانفیگ و IP تمیز (Clean IP Finder):
دیگه نیازی نیست دنبال آی‌پی‌های تمیز بگردید. این ابزار می‌تونه کل رنج آی‌پی‌های کلادفلر (حدود ۱.۵ تا ۳ میلیون پروب) رو اسکن کنه، آی‌پی‌های سالم و با پینگ خوب رو پیدا کنه و مستقیماً روی کانفیگ‌های شما جایگزین (Swap) و تست سرعت کنه.
🔸
تست پایپلاین Xray (Xray Pipeline Test):
کانفیگتون وصل نمیشه یا توسط DPI مسدود شده؟ این قابلیت یه کانفیگ از شما می‌گیره و بهترین ترکیب از "آی‌پی تمیز + تنظیمات فرگمنت (Fragment) + دامنه‌های استتاری (SNI)" رو برای دور زدن فیلترینگ پیدا می‌کنه!
🔸
نصب و دیپلوی سرور Xray در ۲ دقیقه:
اگه یه سرور مجازی (VPS) خام دارید، کافیه این اسکریپت رو اجرا کنید. خودش Xray-core رو نصب می‌کنه، تنظیمات (TCP/WS/REALITY/TLS) رو انجام میده و کانفیگ آماده استفاده بهتون تحویل میده.
🔸
ساخت پروکسی ورکر (Worker Proxy):
اگه دامنه (SNI) کانفیگتون مسدود شده، این ابزار براتون یه اسکریپت Cloudflare Worker می‌سازه تا ترافیک رو از طریق دامنه‌های تمیزِ
workers.dev
به سرورتون منتقل کنید.
🔸
پنل مدیریت اتصالات (Connection Manager):
بدون نیاز به پنل‌های سنگین تحت وب، می‌تونید از طریق همین ابزار داخل محیط ترمینال، کاربر جدید بسازید، اینباند اضافه کنید یا کانفیگ‌ها رو مدیریت کنید.
---
💻
نحوه نصب و راه‌اندازی (بسیار ساده):
کافیه سورس برنامه رو از گیت‌هاب دانلود کرده و فایل پایتون رو اجرا کنید تا یک محیط گرافیکی و تعاملی (TUI) براتون باز بشه:
۱. دریافت از گیت‌هاب:
git clone https://github.com/SamNet-dev/cfray.git
cd cfray
۲. اجرای ابزار:
python3 scanner.py
✅
حالا منو براتون باز میشه و می‌تونید با فشردن کلیدهای میانبر، کارهایی مثل پیدا کردن آی‌پی تمیز (کلید F)، نصب سرور (کلید D) یا مدیریت کانفیگ‌ها (کلید C) رو انجام بدید.
🔗
لینک پروژه و آموزش کامل در گیت‌هاب:
🌐
https://github.com/SamNet-dev/cfray
📌
#آموزش
#معرفی_ابزار
#سرور
#کلادفلر
#Cloudflare
#Xray
#VLESS
#تونل
#اسکنر
#Bypass
#پایتون
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/archivetell/5657" target="_blank">📅 14:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ac73908c6d.mp4?token=BCt3r8WlJPtT4pGTnXlIIHkrDY6TztwlmPHozQ_nPGfH-mYCKLQW3BhrwBxDE4f9cj5FBig_VB4C6N3YoZkqGSi8N3xSdBYYXtfgFr_ILKrelG0b3Dz5UVCfYIAA2HdPifIYWYD5_iPJ1FLpwiw3E5LqkBxXcjuDoFsVch045FmLsZfT8RXqARUMx_Vm0GNgy2OmybP1IIh3emfSEQc0tJuvrWZadcbPwiwZzBWPTSCk-zWDzcSKRumnt-xZajarh8yiFwUsQpXu-RVQKytrzN0S4d443T-DboN5JE2AJijG2Luzts3b2dChgThzbwA2Fayr6Zfz4vozVrsja89wSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ac73908c6d.mp4?token=BCt3r8WlJPtT4pGTnXlIIHkrDY6TztwlmPHozQ_nPGfH-mYCKLQW3BhrwBxDE4f9cj5FBig_VB4C6N3YoZkqGSi8N3xSdBYYXtfgFr_ILKrelG0b3Dz5UVCfYIAA2HdPifIYWYD5_iPJ1FLpwiw3E5LqkBxXcjuDoFsVch045FmLsZfT8RXqARUMx_Vm0GNgy2OmybP1IIh3emfSEQc0tJuvrWZadcbPwiwZzBWPTSCk-zWDzcSKRumnt-xZajarh8yiFwUsQpXu-RVQKytrzN0S4d443T-DboN5JE2AJijG2Luzts3b2dChgThzbwA2Fayr6Zfz4vozVrsja89wSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧠
در GitHub پلاگینی به نام agentmemory محبوب شده است که به عوامل هوش مصنوعی حافظه «بی‌نهایت» اضافه می‌کند — این پلاگین تمام زمینه‌های جلسات، اقدامات و پروژه‌های شما را در یک پایگاه ذخیره می‌کند.
• به ۱۶ عامل هوش مصنوعی از جمله Claude Code، Codex و Cursor متصل می‌شود.
• تمام اقدامات آن‌ها را ذخیره می‌کند، به خاطرات فشرده تبدیل می‌کند و به‌طور خودکار در آینده آن‌ها را پیدا می‌کند.
• دیگر نیازی نیست هر بار زمینه را توضیح دهید — عامل همه جزئیات را به خاطر می‌سپارد.
در نتیجه، می‌توان تا ۹۵٪ از توکن‌هایی که معمولاً برای توضیح زمینه صرف می‌شوند را در هر جلسه صرفه‌جویی کرد.
https://github.com/rohitg00/agentmemory
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/archivetell/5651" target="_blank">📅 09:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کانفیگ اهدایی
تشکر از
@thee_LaShi
بابت این کانفیگای ناب
❤️
vless://9bc46020-c550-439a-86c5-38f64abc1ffd@tr-in.api.dznn.net:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=9F7JxyyP-TNLt0dY2xOB0_34I8W0xXIpFY7rZ7-L0Gg&security=reality&sid=19aa22f681923dc8&sni=tr-in.api.dznn.net&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/archivetell/5650" target="_blank">📅 08:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کانفیگ اهدایی
vless://9bc46020-c550-439a-86c5-38f64abc1ffd@ninka.api.dznn.net:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=9F7JxyyP-TNLt0dY2xOB0_34I8W0xXIpFY7rZ7-L0Gg&security=reality&sid=19aa22f681923dc8&sni=ninka.api.dznn.net&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/archivetell/5649" target="_blank">📅 08:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فیلترچی ری اکشن فیک بزن تا بسوزی
😁</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/archivetell/5648" target="_blank">📅 08:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5647">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پخش کنید بقیه هم وصل بشن
😁</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/archivetell/5647" target="_blank">📅 08:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کانفیگ اهدایی
vless://9bc46020-c550-439a-86c5-38f64abc1ffd@tr-in.api.dznn.net:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=9F7JxyyP-TNLt0dY2xOB0_34I8W0xXIpFY7rZ7-L0Gg&security=reality&sid=19aa22f681923dc8&sni=tr-in.api.dznn.net&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/archivetell/5646" target="_blank">📅 08:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5645">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کانفیگ اهدایی
vless://0468a043-e12c-466e-881c-7d685c1b3950@roz1r.skystreamgame.com:8443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QHkXBS2ENHV0khgY9VBYi8_9bpfqnUYDcfQN4cW5Qg0&security=reality&sid=4326&sni=roz1r.skystreamgame.com&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/archivetell/5645" target="_blank">📅 08:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کانفیگ اهدایی یکی از ممبرای عزیز
vless://9bc46020-c550-439a-86c5-38f64abc1ffd@fishsea.api.dznn.net:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=9F7JxyyP-TNLt0dY2xOB0_34I8W0xXIpFY7rZ7-L0Gg&security=reality&sid=0a6ba2716a409da6&sni=fishsea.api.dznn.net&type=tcp#@archivetell
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/archivetell/5644" target="_blank">📅 08:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کانفیگ اهدایی یکی از ممبرای عزیز
vless://9bc46020-c550-439a-86c5-38f64abc1ffd@fishsea.api.dznn.net:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=9F7JxyyP-TNLt0dY2xOB0_34I8W0xXIpFY7rZ7-L0Gg&security=reality&sid=0a6ba2716a409da6&sni=fishsea.api.dznn.net&type=tcp#@archivetell
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/archivetell/5643" target="_blank">📅 08:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">windscribe_auto_hand .zip</div>
  <div class="tg-doc-extra">12.4 MB</div>
</div>
<a href="https://t.me/archivetell/5642" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل اتوماتیک سازی فرایند جست‌وجو لوکیشن برنامه ویندسکرایب فقط نسخه ویندوز  با تشکر از چنل
@windscribe_auto_hand
که زحمت کشیدن کد نویسی این برنامه رو انجام دادن
❤️‍🔥
#windscribe
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/archivetell/5642" target="_blank">📅 02:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5641">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅️
خب از اونجایی که بعضی از پروتکل های ویندسکرایب باز شدن براتون یه اموزش و فایل رو میزارم که فقط مخصوص نسخه ویندوز هست
طبق این این اموزش جلو برید  و تک تک مراحل رو انجامش بدید :
کد exe اتوماتیک سازی فرایند جست‌وجو لوکیشن ویندسکرایب
مخصوص ویندوز
این کد به گونه ای نوشته شده که حتی موقعی که API وینداسکرایب کانکشن نمیده هم وصل بشه
⭕️
نحوه استفاده
اول وینداسکرایب رو باز میکنید
پروتکل و پورت مد نظرتون رو انتخاب کنید
بعد برنامه exe رو اجرا میکنید
وقتی اجرا کردید بلافاصله یه جایی رو windscribe کلیک کنید
حالا کد خودش شروع میکنه همه لوکشین هارو تست میکنه
اگر وصل شد توی پوشه logs تو فایل text مینویسه
تو این فرایند قهوه بنوشید و صبر کنید تا تموم بشه
امیدوارم به کارتون بیاد
❤️
با تشکر از چنل دوستمون
@windscribe_auto_hand
❤️‍🔥
که این اسکریپت رو واقعا زحمت کشیدن نوشتن و تو چنل قرار دادن اون زمان چون ایران اینترنتش اکسس بود قابل استفاده نبود ولی الان میتونید استفاده کنید
⚠️
نکته مهم : وینداسکرایب همچنان روی متد کار میکنن و باهاشون حرف زدم با اینکه اینترنت کمی محدودیت هاش رفته و باز کامل نیست
از پروژه دست نکشیدن و قراره نسخه نهایی رو یکدفعه release کنند که اگه یه زمان دوباره مشکلی پیش اومد همیشه این متد برای ایرانی ها قابل استفاده باشه
با تشکر از تیم ویندسکرایب که خیلی تلاش دارن میکنن نسخه نهایی رو بدون مشکل بسازن
🔥
🤌
#windscribe
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/archivetell/5641" target="_blank">📅 02:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">FileShare.exe</div>
  <div class="tg-doc-extra">48.6 MB</div>
</div>
<a href="https://t.me/archivetell/5638" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
انتشار نسخه جدید File Share v1.2
توی این آپدیت کلی تغییر و بهبود اضافه شده:
✅
امکان انتخاب پوشه اختصاصی برای اشتراک‌گذاری فایل
کاربر حالا می‌تونه هر پوشه‌ای رو برای اشتراک در شبکه محلی انتخاب کنه.
✅
اضافه شدن آیکون اختصاصی برنامه
از نسخه 1.2 برنامه ظاهر حرفه‌ای‌تری گرفته.
✅
جایگزینی پنل ویندوزی به جای محیط ترمینال
رابط کاربری ساده‌تر و کاربرپسندتر شده.
✅
رفع باگ‌ها و بهبود عملکرد
پایداری و سرعت برنامه بهتر شده.
📡
File Share یه ابزار انتقال فایل تحت شبکه محلیه که بدون اینترنت کار می‌کنه.
کافیه کاربر دوم IP سیستم رو داخل مرورگر وارد کنه تا از طریق محیط وب:
⬇️
دانلود فایل
⬆️
آپلود فایل
💬
تبادل پیام بین دستگاه‌ها
به‌صورت کاملاً آفلاین و داخل شبکه محلی انجام بشه.
🛠
همچنین پروژه روی GitHub قرار گرفته تا به‌صورت Open Source در دسترس همه باشه و سورس کدها برای توسعه، بررسی و مشارکت در اختیار همگان قرار بگیره.
لینک گیت هاب پروژه</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/archivetell/5638" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/b370928a6c.mp4?token=qrCALd_n3JQHzDyNVpx6ghKrHY2z5EzR-xMQW7y1URXoBtvnvu2d-F1shny8zuSluyUt0n65OY2AQODuF4x9gCchZ4qriZ9FOQI6hgh80_kAwNeg56krxNph0ZQ8CHbIkiuuFmpmNPxLxgYXouJC2PtGdZH0-WM0VvDb-bGlI08k95snqmlbPQbfN93YQErXbwAqDbmxXEkNsjgC-VlfymUEBwxYXTlOoyU4SVLQ6AM_zItOLR7XMd7-HHV_FECMWcwN2zyn8bRhyAOn1vE9BBmMXVlbRdKObcy7UArhSnjsTpLDwWxvuBVRxMqd82AJou6WnMOwnVCcu0jTocpAkw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/b370928a6c.mp4?token=qrCALd_n3JQHzDyNVpx6ghKrHY2z5EzR-xMQW7y1URXoBtvnvu2d-F1shny8zuSluyUt0n65OY2AQODuF4x9gCchZ4qriZ9FOQI6hgh80_kAwNeg56krxNph0ZQ8CHbIkiuuFmpmNPxLxgYXouJC2PtGdZH0-WM0VvDb-bGlI08k95snqmlbPQbfN93YQErXbwAqDbmxXEkNsjgC-VlfymUEBwxYXTlOoyU4SVLQ6AM_zItOLR7XMd7-HHV_FECMWcwN2zyn8bRhyAOn1vE9BBmMXVlbRdKObcy7UArhSnjsTpLDwWxvuBVRxMqd82AJou6WnMOwnVCcu0jTocpAkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاربران ChatGPT اکنون می‌توانند مستقیماً از طریق چت برنامه‌های واقعی بسازند
فروشگاه برنامه ChatGPT
به تازگی
AppDeploy
را اضافه کرده است و این قابلیت برای حساب‌های رایگان نیز فعال است.
توضیح دهید که چه چیزی می‌خواهید بسازید، ChatGPT کد را می‌نویسد، AppDeploy به طور خودکار در همان چت استقرار را انجام می‌دهد و بلافاصله یک لینک کارآمد به شما بازمی‌گرداند.
رایگان برای استفاده. نیاز به اشتراک یا کارت اعتباری نیست.
👉
نصب AppDeploy در ChatGPT
و راه‌اندازی اولین برنامه خود در چند دقیقه
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/archivetell/5637" target="_blank">📅 00:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گوگل پلی رفع فیلتر شده..</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/archivetell/5636" target="_blank">📅 23:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گوگل پلی رفع فیلتر شده..</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/archivetell/5635" target="_blank">📅 23:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ربات جدید تبدیل لینک به فایل
@url_uploder_nrbot
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/archivetell/5634" target="_blank">📅 23:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12fb4063f0.mp4?token=Q8yGPJ-M7zAAhE-11qwrXP50WktnH5fIva-QLr94byT6IJ7jPVuDfQwjJW3cFXQgm7SPnKSDXjCGD2GAGeg2hWNFx-vSWkpKBwnY7lgJlNnWcv34oFimT9GpRlZJGM8fnCeXAGoVb6xAgv_xvqS3ZA_Kxk3Xxhk-Y4NUIutUB8QQzXwo6q8N-7F5kIFxyDparm5gmSZWMOVm5YoLQCd9gQrAt6NcMaF2WlVFJ9qjgmzqDeHXUlBh7Ai1J-ra0tfBTScaaj3trQI28qyBOPsqCV02RFIqSpOiACDZp0L_PI3uW8SpRi_L3-aebKFCCPWK2UDiHx3qiltZY14LPsPCxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12fb4063f0.mp4?token=Q8yGPJ-M7zAAhE-11qwrXP50WktnH5fIva-QLr94byT6IJ7jPVuDfQwjJW3cFXQgm7SPnKSDXjCGD2GAGeg2hWNFx-vSWkpKBwnY7lgJlNnWcv34oFimT9GpRlZJGM8fnCeXAGoVb6xAgv_xvqS3ZA_Kxk3Xxhk-Y4NUIutUB8QQzXwo6q8N-7F5kIFxyDparm5gmSZWMOVm5YoLQCd9gQrAt6NcMaF2WlVFJ9qjgmzqDeHXUlBh7Ai1J-ra0tfBTScaaj3trQI28qyBOPsqCV02RFIqSpOiACDZp0L_PI3uW8SpRi_L3-aebKFCCPWK2UDiHx3qiltZY14LPsPCxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک مجموعه برتر از انیمیشن‌های رابط کاربری وب برای طراحان رابط کاربری که تمایلی به صرف زمان در ایجاد انیمیشن‌ها از پایه ندارند
https://transitions.dev/
این مجموعه شامل انیمیشن‌های آماده‌ای برای کارت‌ها، منوها، فهرست‌ها و کلیدهای تغییر وضعیت می‌باشد.
امکان بررسی مستقیم انیمیشن‌ها در وب‌سایت پیش از بهره‌برداری فراهم است.
ادغام در پروژه‌های فرانت‌اند واقعی به سادگی امکان‌پذیر است.
پشتیبانی از ادغام به عنوان یک قابلیت برای عوامل هوش مصنوعی ارائه می‌گردد.
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/archivetell/5633" target="_blank">📅 22:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/121da40c06.mp4?token=h4eDyvR5Gf1wEpkx9G5yC40TgVO7l8WZsZdgbRi7fQnXJTPCzwn9mU4QwHKsJ6Q4IAtsZoA01Qzv_AiXhkyEGjf1TNWzlO2zE21NxJ6lV_7Aw9lTCDgtJXqhK50MhaHLlgiPN49sYKydWIOFTuWoRpu0zEZwUZlqKMAY0cfPCEeUyv0hfRJsqbTGyjEyM7YoVHpSiPYhAENXOrhqmvKlZWN_iHVpLhpM58V_y7OxI0mKUB1XFINSJZWUFsQA0Vg_zWSkgCLRpXh6fX-V-lqlbc6QHEY9Xfnxpvfh7kdvvejgam4ACnevUW-gQvSP6YRUc81zp__PlCGCrDUmBxQHcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/121da40c06.mp4?token=h4eDyvR5Gf1wEpkx9G5yC40TgVO7l8WZsZdgbRi7fQnXJTPCzwn9mU4QwHKsJ6Q4IAtsZoA01Qzv_AiXhkyEGjf1TNWzlO2zE21NxJ6lV_7Aw9lTCDgtJXqhK50MhaHLlgiPN49sYKydWIOFTuWoRpu0zEZwUZlqKMAY0cfPCEeUyv0hfRJsqbTGyjEyM7YoVHpSiPYhAENXOrhqmvKlZWN_iHVpLhpM58V_y7OxI0mKUB1XFINSJZWUFsQA0Vg_zWSkgCLRpXh6fX-V-lqlbc6QHEY9Xfnxpvfh7kdvvejgam4ACnevUW-gQvSP6YRUc81zp__PlCGCrDUmBxQHcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎹
سونو را دور می‌اندازیم — ElevenLabs نسخه Music V2 را عرضه کرده است. توسعه‌دهندگان این را بزرگ‌ترین به‌روزرسانی شبکه عصبی موسیقی تا به امروز می‌نامند.
https://elevenlabs.io/music
🕤
تولید ووکال، ابزارها و آرنجمنت‌ها در همه ژانرها به طور قابل توجهی قدرتمندتر شده است.
🕤
سبک آهنگ را می‌توان در حین پخش تغییر داد.
🕤
هر بخش از آهنگ به طور جداگانه ویرایش می‌شود — ثانیه مورد نظر را انتخاب کرده و فقط آن را بازتولید می‌کنید.
🕤
پشتیبانی از رفرنس‌ها: می‌توانید صدا، متن، ژانر یا پرامپت معمولی بارگذاری کنید.
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/archivetell/5632" target="_blank">📅 22:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کانفیگ پرسرعت
ایپی استاتیک کره شمالی
جهت سفارش پی‌وی
🐱</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/archivetell/5631" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شما می‌توانید Llama 4، Qwen3، Gemma 4 را اجرا کنید — همه رایگان، همه خصوصی، روی لپ‌تاپ خودتان.
🖥️
⚡
این همان Ollama است.
🔗
ollama.com
این یک ابزار رایگان است که به شما اجازه می‌دهد مدل‌های قدرتمند هوش مصنوعی متن‌باز را به صورت محلی اجرا کنید — بدون نیاز به اینترنت، بدون هزینه API، بدون خروج داده‌ها از دستگاه شما.
فقط دانلود کنید، یک مدل بکشید و شروع به گفتگو کنید.
چرا مردم واقعاً از آن استفاده می‌کنند:
→ بدون هزینه‌های ابری
→ کاملاً خصوصی — داده‌های شما هرگز از دستگاهتان خارج نمی‌شود
→ به صورت آفلاین کار می‌کند
→ مدل‌هایی مانند DeepSeek-R1، Llama 4، Qwen3، Gemma 4 را اجرا می‌کند
نسخه ۲۰۲۶ اکنون شامل یک رابط کاربری دسکتاپ داخلی، شتاب‌دهی Apple Silicon از طریق MLX، و پشتیبانی ابری برای مدل‌های بزرگ‌تر است — همه در یک رابط کاربری تمیز.
اگر برای اشتراک‌های هوش مصنوعی هزینه می‌پردازید و هیچ کار حساسی با داده‌هایتان انجام نمی‌دهید... Ollama ارزش ۱۰ دقیقه وقت شما را دارد.
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/archivetell/5630" target="_blank">📅 20:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🎁
دریافت یک سال اشتراک پرمیوم RoboForm (رایگان)
---
رفقا سلام!
✋
یه آفر فوق‌العاده و محدود داریم. پسورد منیجرِ معروف، امن و پرطرفدار
RoboForm
، به کاربراش
۱۲ ماه اشتراک پرمیوم کاملاً رایگان
(به ارزش حدود ۳۰ دلار) میده.
اگر هنوز از یه ابزار مدیریت پسورد خوب برای ذخیره امنِ رمزها، قابلیت اتوفیل (Autofill) و همگام‌سازی بین گوشی و لپ‌تاپ استفاده نمی‌کنید، الان بهترین فرصته.
💻
مراحل دریافت اشتراک:
۱. وارد لینکِ آفر در پایین پست بشید.
۲. ایمیل خودتون رو وارد کنید و روی دکمه
Redeem Offer
کلیک کنید.
۳. مراحل ثبت‌نام و فعال‌سازی اکانت رو انجام بدید.
✅
تمام! اشتراک یک‌ساله پرمیوم به صورت خودکار روی اکانتتون فعال میشه.
⚠️
نکات مهم این آفر:
-
💳
بدون نیاز به کردیت کارت:
برای فعال‌سازی اصلاً نیازی به وارد کردن اطلاعات پرداخت یا کارت بانکی نیست.
-
🆕
کاربران جدید:
این آفر فقط برای اکانت‌ها و کاربرانی هست که تا حالا پرمیوم نبودن.
-
⏳
مهلت استفاده:
فقط تا
۳۱ می ۲۰۲۶
(۱۱ خرداد ۱۴۰۵) فرصت دارید این آفر رو دریافت کنید.
🔗
لینک دریافت آفر ویژه روبوفروم:
🌐
https://www.roboform.com/lp?frm=offer-ga
📌
#آفر
#رایگان
#RoboForm
#پسورد_منیجر
#امنیت
#پرمیوم
#کاربردی
#تخفیف
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/archivetell/5629" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">600 گیگ کانفیگ مستقیم متصل همه نتا
اهدایی یکی از ممبرای عزیز
❤️
vless://22768339-9096-48aa-9109-ff28141145b9@roz2r.skystreamgame.com:8443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QHkXBS2ENHV0khgY9VBYi8_9bpfqnUYDcfQN4cW5Qg0&security=reality&sid=4326&sni=roz2r.skystreamgame.com&type=tcp#Aqa.rza
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/archivetell/5628" target="_blank">📅 19:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">kiro.dev
یک ابزار کدنویسی هوش مصنوعی از AWS که فقط کد نمی‌نویسد.
این ابزار کل پروژه شما را از صفر برنامه‌ریزی، طراحی و می‌سازد.
⚡
Free trial with 500 credits
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/archivetell/5627" target="_blank">📅 19:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آیپی تمیز کلودفلر، تست شده روی ایرانسل 104.16.81.122 104.16.81.43 104.16.81.86 104.16.81.12 104.16.81.24 104.16.81.125 104.16.81.40 104.16.81.133 104.16.81.68 104.16.81.101 104.16.81.23 104.16.81.155 104.16.81.112 104.16.81.106 104.16.81.67 104.16.81.82 104.16.81.157…</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/archivetell/5625" target="_blank">📅 18:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">Defyx VPN  رایتل سرعت بالا  https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn  @ArchiveTell</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/archivetell/5624" target="_blank">📅 18:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آیپی تمیز کلودفلر، تست شده روی ایرانسل
104.16.81.122
104.16.81.43
104.16.81.86
104.16.81.12
104.16.81.24
104.16.81.125
104.16.81.40
104.16.81.133
104.16.81.68
104.16.81.101
104.16.81.23
104.16.81.155
104.16.81.112
104.16.81.106
104.16.81.67
104.16.81.82
104.16.81.157
104.16.81.6
104.16.81.1
104.16.81.110
104.16.81.72
104.16.81.10
104.16.81.16
104.16.81.126
104.16.81.75
104.16.81.53
104.16.81.134
104.16.81.119
104.16.81.156
104.16.81.2
104.16.81.91
104.16.81.45
104.16.81.21
104.16.81.77
104.16.81.73
104.16.81.66
104.16.81.19
104.16.81.32
104.16.81.88
104.16.81.132
104.16.81.74
104.16.81.8
104.16.81.18
104.16.81.121
104.16.81.48
104.16.81.145
104.16.81.51
104.16.81.13
104.16.81.104
104.16.81.80
104.16.81.42
104.16.81.144
104.16.81.111
104.16.81.105
104.16.81.118
104.16.81.117
104.16.81.26
104.16.81.78
104.16.81.159
104.16.81.57
104.16.81.25
104.16.81.60
104.16.81.54
104.16.81.149
104.16.81.136
104.16.81.97
104.16.81.38
104.16.81.90
104.16.81.137
104.16.81.140
104.16.81.59
104.16.81.22
104.16.81.41
104.16.81.150
104.16.81.64
104.16.81.31
104.16.81.33
104.16.81.61
104.16.81.76
104.16.81.69
104.16.81.46
104.16.81.49
104.16.81.35
104.16.81.50
104.16.81.79
104.16.81.34
104.16.81.93
104.16.81.102
104.16.81.129
104.16.81.71
104.16.81.115
104.16.81.92
104.16.81.5
104.16.81.99
104.16.81.84
104.16.81.130
104.16.81.128
104.16.81.47
104.16.81.36
104.16.81.96
104.16.81.9
104.16.81.37
104.16.81.4
104.16.81.124
104.16.81.58
104.16.81.52
104.16.81.55
104.16.81.113
104.16.81.44
104.16.81.65
104.16.81.138
104.16.81.95
104.16.81.29
104.16.81.135
104.16.81.56
104.16.81.108
104.16.81.103</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/archivetell/5623" target="_blank">📅 18:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
مدل بعدی Grok از xAI ممکن است ظرف ۲ تا ۳ هفته آینده عرضه شود
👀
⚡
گزارش‌ها حاکی از آن است که مدل جدید ممکن است از مدل پایه بسیار بزرگ‌تر ۱.۵ تریلیون پارامتری V9-Medium استفاده کند که جهش عظیمی نسبت به معماری ۰.۵ تریلیون پارامتری V8-Small در Grok 4.3 است.
جزئیات جالب دیگر:
گفته می‌شود داده‌های کدنویسی Cursor برای آموزش اضافی استفاده می‌شود.
Grok5؟
👀
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/archivetell/5622" target="_blank">📅 18:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">#اختصاصی
🌐
دامنه‌های رایگان برای هر پروژه‌ای
https://github.com/DigitalPlatDev/FreeDomain
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/archivetell/5621" target="_blank">📅 18:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPCXjYu2P7b4pk8RrpY-T41Gk355T8uZm7UigXH7p9N1MYBz0GlEYHTby6LIpQxzfCZoxyXz86sUStRksolOaIqXzadDiKEY00cF_r3lh4DksPAg_RuLHee6lXoQ6iQueZbM8DY1e1ZpeLqNeb7kfe5hbCns_fEtGdK2c1cK9by6I-5CiggOChcl-0Jtya-CcuzpHcFohEbASW14R1k110lHy-ESaUo29W9TnI0Y8XuV3PULDEepWLcVbnjVLd01tNkJRvoSbnUnCGn-mFxQD6_bp6l7gZzl4WP2WW7jhVx0UP39t6C_kZ2qsLV-lFsP3oQ4plxxsL4xT40UlzEsqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Defyx VPN  رایتل سرعت بالا  https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn  @ArchiveTell</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/archivetell/5620" target="_blank">📅 17:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">Defyx VPN
رایتل سرعت بالا
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/archivetell/5619" target="_blank">📅 17:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5618">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">configs.txt</div>
  <div class="tg-doc-extra">195.4 KB</div>
</div>
<a href="https://t.me/archivetell/5618" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دوستان میتونین با Hiddify روی سرور های رایگانش وصل بشید یا از گیت هاب بگردین دنبال ساب بندازین داخلش
👋
**میتونین داخل Github هم بگردین ساب های مختلف و وارد اپ کنین و تست بگیرید
👍
لینک دانلود داخلی Hiddify
👋
💀
@archivetell</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/archivetell/5618" target="_blank">📅 16:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5617">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfD1PH1ufp5oP9YtT3JHYCoEvmL-vMIzZG7VxH1Nu2uiT34NibU1gLq3s7WEzULzS66RsmU0F34_pWnDQ7d8O0iUdQGenUTei3bYlC4E4UQ4tavcUvsn_RxzaWChGII8jcCJ5WRQFauumFnoiLz_2SX7NkdJp9pakjA6TVV0XlTqYKC5DIdjjHw67Vcmf5LjuPHPx27H47zLzvc_hvYaRYbxdsb8VekTxjb_WF4qLDl9WR_ZU8GML6Y_ZyPKusXoHjiJ0B51N99XaAxAy-kn_dnJFzU5sx035e1P4nfpVltLg3uESiNxYX0XKGGAk9qY5KuEqCP3p3ydeXmdIeg9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان میتونین با Hiddify روی سرور های رایگانش وصل بشید یا از گیت هاب بگردین دنبال ساب بندازین داخلش
👋
**میتونین داخل Github هم بگردین ساب های مختلف و وارد اپ کنین و تست بگیرید
👍
لینک دانلود داخلی Hiddify
👋
💀
@archivetell</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/archivetell/5617" target="_blank">📅 16:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مقایسه سرور ها و خرید سرور مناسب و اقتصادی
جهت راه اندازی کانفیگ
https://t.me/archivetell/5282
https://t.me/archivetell/5308
https://t.me/archivetell/5309
https://t.me/archivetell/5310</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/archivetell/5616" target="_blank">📅 15:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHvAx-7fHk1TwL8jWxjhkhllmB6H8DFu4NtbG4Uu5O1Ioi4MZWmvK4SZPsPM_8Zdw1B1-S9jzCh_94RJEJ36jBgwta3I49CpKUiP8sSXSBtUTITwEYJbptJxe7p85wMvvwWyOrrK736BW12vJ_vGZ0PBhBHA-1DeNHS0pmmbmWAsl8R0EGTWvgtr8AQnqQ0Jg3e1ayDF1A0-rjyEsVoqkJPc2v5wKH3G1-MfFyXMcB1_DY0k7GEHrVB6-koIUCTbqt8g1JwX0_NySvBr9n0-xeHcUBCNQknkCN8mwWj0jFYH1rNZVYz2aWKpG_Of0zo9SZvomqbJ-_zcr5SOq2-fcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">162.159.192.1
162.159.193.3
162.159.195.1
برای وارپ وایرگارد با این آیپی وصل شدم.
پینگ می ده، لوکیش ایران می زنه
😂
ولی تلگرامم الا بالاس دارم باهاش پیام می دم.</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/archivetell/5615" target="_blank">📅 13:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">در کل این اپلیکیشن D-Tools خیلی خوبه ولی حیف توسعه داده نمی شه، وگرنه یه اسکنر Google CDN و Cloudflare CDN و Fastly CDN می‌آورد خیلی خوب می شد.</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/archivetell/5613" target="_blank">📅 13:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">در کل این اپلیکیشن D-Tools خیلی خوبه ولی حیف توسعه داده نمی شه، وگرنه یه اسکنر Google CDN و Cloudflare CDN و Fastly CDN می‌آورد خیلی خوب می شد.</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/archivetell/5612" target="_blank">📅 13:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCo8kv5xIZSj8a3pxwkdEw3K5kRv01IYjAvvDZRnHVaR0V3y4tUI2F5mfzsdHjlCG5UkAovgLeLxMTxPwmQJNfBcGayso25mLwk0wH5totQRkfsImhFUOV0MBlh10EkLk7Dm49R-nXH865KDBdgJTy-yle_xFq1j3PHSQWYF0TJX59aLikV6lldkH99YmOuK7I-lygNHZ-iojVgGjQIh7yCDd4wcBCfP5NTZ3G_v4FfCKaCaB6Ummm2IRUU0Pmhk9qk5U9bIOYo7AmUzow-JWSc--JXSaqS8NSWlf-0AdR-S9zMnVgh_l9j6XVKsNNSGGy5p_0fcfYwIg8dFY82QQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ساختن وارپ به این نیاز نیستا.  کانتریبیوتر v2ray، یک ریپو داره به اسم D-Tools. اپلیکیشن از پلی استور حذف شده ولی توی اینترنت پیدا می شه به شکل xapk. بدون سرور مجازی براتون کانفیگ warp می سازه.  {   "local_address": [     "172.16.0.2/32",     "2606:47…</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/archivetell/5611" target="_blank">📅 13:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">D-Tools_0.0.6_apkcombo.com.xapk</div>
  <div class="tg-doc-extra">31.7 MB</div>
</div>
<a href="https://t.me/archivetell/5610" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اینم فایل اپلیکیشنش.
😊
@archivetell</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/archivetell/5610" target="_blank">📅 13:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeuJ-gQvad_kLkcvW_WLSzMKLsB7zFO3bKtkzHpTOsAG62Hxv5Wuxx5IeUvxP30Rvk61YUwHezAbl2_ERYjdH3yx2tp3nGqGsBZBxGiKkrlK0-ZygZGd4CZvaFFqoF_ZaIkZJVHdCg7iYYoF54N2vxs87JzqMdh1e9434HH_bMF-ZBeKOVSyjkJTv4H6BKtllR10JAMAedFSFCuor6KQhDl74_eG3UmgEdyXBAVbjL-c0bHJjbCDnUBh7QxbXoPUUlCY_OUPa526lk0jw0JA2ImhweOBhsvoKvOkIDXIVWx-lzNBeZjLAzm5RqSD3ngdv000T2_tS8p4f7_NLU6f6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش ساخت کانفیگ وارپ (نیاز به سرور مجازی )  با استفاده از الگوهای زیر، کانفیگ اختصاصی خودتون رو بسازید :  کانفیگ‌های خام:  warp://licence@ip:port/?ifp=40-80&ifps=50-100&ifpd=2-4&ifpm=m4  warp://licences@ip:port/?ifp=30-60&ifps=50-100&ifpd=3-6&ifpm=m6 برای…</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/archivetell/5608" target="_blank">📅 13:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🌐
بات تست رایگان بدون رفرال (خرید نزنید)
@Cheap_v2ray_bot</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/archivetell/5607" target="_blank">📅 13:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آموزش ساخت کانفیگ وارپ (نیاز به سرور مجازی )
با استفاده از الگوهای زیر، کانفیگ اختصاصی خودتون رو بسازید :
کانفیگ‌های خام:
warp://licence@ip:port/?ifp=40-80&ifps=50-100&ifpd=2-4&ifpm=m4
warp://licences@ip:port/?ifp=30-60&ifps=50-100&ifpd=3-6&ifpm=m6
برای استخراج لایسنس، آی‌پی و پورت مورد نیاز، اسکریپت زیر رو اجرا و مقادیر رو در الگو جایگذاری کنید:
اسکریپت استخراج:
bash <(curl -fsSL https://raw.githubusercontent.com/Ptechgithub/warp/main/endip/install.sh)
☑️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/archivetell/5606" target="_blank">📅 12:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">همراه اول
Windscribe UDP 443 Censorship On Dallas BBQ
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/archivetell/5605" target="_blank">📅 12:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کسایی که سرور دارن.
اینباند:
Vless+xhttp+tls+Cloudflare clean ip
بزنین با آی‌پی تمیز کلادفلیر
عالی وصله‌
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/archivetell/5604" target="_blank">📅 12:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">همراه اول
Windscribe UDP 443 Censorship On Atlanta Peachtree
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/archivetell/5603" target="_blank">📅 12:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">و اینکه، نرم افزار Karing گزینه وارپش کار می کنه و پینگ داره و کار می‌کنه.
😊
@archivetell</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/archivetell/5602" target="_blank">📅 12:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">واقعا باورم نمی شه مردم چقدر می تونن عقده ای بشن.
📘
مگه ما فروشنده ها چیکارتون کردیم؟
😭
طرف با کانفیگ رایگان بعد ۹۰ روز وصل شده زنگ می زنه مسخره کنه. چه رویی دارین خدایی.
حالا من به وصل شدنشون می گم وصل، طرف فقط می تونه با کانفیگش پینگ بگیره
🤡
😊
@archivetell</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/archivetell/5601" target="_blank">📅 12:09 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
