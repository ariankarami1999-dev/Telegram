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
<img src="https://cdn4.telesco.pe/file/a8Gneg2h8MS5mHT8WSppsmpYMn1pzODjySSmLD8Y4kvpjka9j3vp1vYA4Y6LKd81OSVFYO3jAC4E4IGJLB5axV7vyxlHpUom6EoAMFrfkE1H8XD23LxHNu1B-89T_wCp8nFvk-GUkPhEzbKep-4kuovWGybkC8kJrhqUYNiD3KnW7FlyF8YNEWMHznxuOLgwB08r7yXjOo5b8plT1Cs2BenLlgwwBYn-efV9VMsGxl_lon3mL8Ip2Ul4l95IHS5CH8jg7ik_ptTloTWLjmW-1mG96HmCoIIhh8SMBgzXwEuHju67WDhwD--YHyz0D26B5Rg8SWbuS3_wCsHO2Hp-Rg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 7.02K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 18:30:12</div>
<hr>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خودتون آیپی اسکن کنید با این روش ها..</div>
<div class="tg-footer">👁️ 830 · <a href="https://t.me/archivetell/4987" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4986">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel(𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣⚡️)</strong></div>
<div class="tg-text">اسکنر برای آی پی تمیز https://github.com/seramo/sni-scanner</div>
<div class="tg-footer">👁️ 174 · <a href="https://t.me/archivetell/4986" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4985">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">اسکنر برای آی پی تمیز
https://github.com/seramo/sni-scanner</div>
<div class="tg-footer">👁️ 143 · <a href="https://t.me/archivetell/4985" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4984">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">hosts.txt</div>
  <div class="tg-doc-extra">4.1 KB</div>
</div>
<a href="https://t.me/archivetell/4984" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اینا هم اسکن کنید..</div>
<div class="tg-footer">👁️ 107 · <a href="https://t.me/archivetell/4984" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">akamai-AS20940.json</div>
  <div class="tg-doc-extra">97.1 KB</div>
</div>
<a href="https://t.me/archivetell/4982" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">رنج آیپی akamai واسه اسکن</div>
<div class="tg-footer">👁️ 59 · <a href="https://t.me/archivetell/4982" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ping.py</div>
  <div class="tg-doc-extra">17.6 KB</div>
</div>
<a href="https://t.me/archivetell/4981" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکنر TCP رنج ایپی های Akamai
فایل hosts.txt رو کنارش بذارید و روی هر سیستم عاملی با پایتون اجراش کنید (ورودی ایپی تکی و ایپی رنج ساپورت میکنه)
- قابلیت تشخیص NAT از اتصال واقعی بر اساس پینگ
- سرعت ورکر رو میشه تنظیم کرد
- قابلیت بهینه سازی تایم اسکن
- خروجی رو توی فایل vali.txt میده.
بدون پیش نیاز...</div>
<div class="tg-footer">👁️ 112 · <a href="https://t.me/archivetell/4981" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Sni-radar.zip</div>
  <div class="tg-doc-extra">303.4 KB</div>
</div>
<a href="https://t.me/archivetell/4980" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔹
سورس اسکنر اختصاصی تیم پرشیا
❤️
🟢
این
سورس اسکنر sni و Cdn هست و با بهترین قابلیت ها نوشته شده است
☑️
💡
اموزش نصب در کامپیوتر:
🔹
اول فایل را دانلود کرده سپس استخراج کنید
🔹
سپس رو محل فایل کلیک کرده ترمینال را باز کرده و در ان این دستور را بنویسید:
pip install -r requirements.txt
🔹
سپس این دستور را بنویسید:
python sni_web.py
🔹
بعدش صفحه باز میشه و میتونید اسکن را شروع کنید
🟢
🟢
🟢
🟢
🟢
🟢
🟢
🟢
🟢
🟢
🟢
🟢
⏺️
اموزش نصب در گوشی با برنامه termux
🔹
اول وارد برنامه ترموکس شده و پکیچ های پایتون نصب کنید
🔹
سپس دستور زیر را وارد کنید
git clone https://github.com/DevMoEiN/SNI-Radar.git
🔹
سپس این دستور:
cd SNI-Radar
🟢
بعد این:
pip install flask
🔹
و در اخر این:
python sni_web.py
⏺️
سپس این را در کروم تایپ کنید:
http://127.0.0.1:10808</div>
<div class="tg-footer">👁️ 132 · <a href="https://t.me/archivetell/4980" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">📌
نحوه اسکن آیپی‌‌های Akamai در ترموکس :
1⃣
به یک فیلترشکن متصل بشید و ​ترموکس را باز کنید و این ۳ خط را کپی کنید و اینتر بزنید تا ابزارهای لازم نصب بشن :
pkg update && pkg upgrade -y
pkg install nmap -y
termux-setup-storage
اگر پیغامی برای دسترسی به فایل‌ها اومد، Allow را بزنید.
2⃣
​
حالا فیلترشکن رو خاموش کنید و دستور زیر رو بزنید
:
nmap -p 443 --open -T4 2.16.0.0/1
8
‼️
من در دستور از رنج آیپی
2.16.0.0/18
استفاده کردم و 4 آیپی وایتی که اسکن کرد رو براتون گذاشتم، شما میتونید اون رنج‌ رو پاک کنید و از این مخزن گیت‌هاب، سایر رنج‌ها رو در دستور جایگذاری کنید :
https://github.com/platformbuilds/Akamai-ASN-and-IPs-List
بعد از پایان اسکن، ​هر جا نوشته بود Nmap scan report for و زیرش نوشته بود 443/tcp open یعنی اون آیپی‌ وایته و باید کپیش کنید
.
بهتره رنج‌های کوچک رو اسکن کنید، اسکن رنج‌آیپی‌های بزرگ، ساعت‌ها زمان میبره</div>
<div class="tg-footer">👁️ 110 · <a href="https://t.me/archivetell/4979" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">جهت اسکن آیپی های fastly یا akami یا هر آیپی / رنجی که میخواین میتونید از ریپوی زیر استفاده کنید
https://github.com/penhandev/IP-Scanner</div>
<div class="tg-footer">👁️ 102 · <a href="https://t.me/archivetell/4978" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ip_scanner_gui.exe</div>
  <div class="tg-doc-extra">9.6 MB</div>
</div>
<a href="https://t.me/archivetell/4977" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکنر آیپی
قابلیت هاش:
1. چک کردن ایپی معمولی
2. چک کردن رنج ایپی Fastly و Akamai
3. بصورت دستی اضافه کردن ایپی یا رنج
4. بصورت فایل اضافه کردن .txt  و .json
5. ماکسیموم پینگ گذاشتن واسش مثلا زیر 180ms
6. ایپی های که داخل چنلا میزارن بندازید توش اسکن کنه
منبع : پای پکیج</div>
<div class="tg-footer">👁️ 117 · <a href="https://t.me/archivetell/4977" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Akamai-IP-Scanner.zip</div>
  <div class="tg-doc-extra">1.8 KB</div>
</div>
<a href="https://t.me/archivetell/4976" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">برنامه Akamai IP Scanner
۱. لیست رنج‌های هدف (با پشتیبانی از تمام فرمت‌ها مثل 16/ یا 24/) را در فایل ips.txt قرار دهید. (پیشفرض قرار داده شده)
۲. روی فایل scan.ps1 راست‌کلیک کرده و گزینه Run with PowerShell را برای شروع اسکن انتخاب کنید.
۳. بهترین آی‌پی‌ها به‌صورت لحظه‌ای در clean_ips.txt ذخیره می‌شوند (هر زمان مایل بودید می‌توانید اسکن را متوقف کنید).</div>
<div class="tg-footer">👁️ 106 · <a href="https://t.me/archivetell/4976" target="_blank">📅 17:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آپلودسنتر
https://files.bokhary.fun/dump/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/archivetell/4974" target="_blank">📅 17:21 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">لینک داخلی شیر و خورشید ، دو تا آپلودسنتر
دانلود
دانلود
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/archivetell/4973" target="_blank">📅 17:17 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">Telegram.apk</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/archivetell/4969" target="_blank">📅 16:34 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آیپی تمیز شیر و خورشید
2.21.134.89
2.19.204.217
96.16.122.149
172.237.127.6
96.16.53.158
23.55.163.135
2.19.205.64
23.73.2.148
2.17.147.11
2.19.204.240
184.51.252.36</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/4968" target="_blank">📅 16:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ایرانسل تست شده شیر و خورشید
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29
2.22.21.152
95.101.23.82
23.215.0.164
23.197.161.35
184.28.230.87
23.220.128.221
96.17.207.142
23.50.131.18
23.36.162.209
23.219.3.212
23.223.245.150
96.16.122.59
23.2.13.138
23.2.13.144
96.17.207.135
23.220.113.51
96.17.72.41
23.203.185.105
95.101.35.83
2.21.239.23
23.54.210.170
23.215.60.73
95.101.181.125
23.192.237.222
23.200.143.71
23.58.222.98
125.56.219.8
104.80.49.118
96.16.122.158
2.21.239.10
96.16.122.65
95.101.23.170
104.111.202.158
23.2.13.201
92.123.102.104
23.58.222.139
2.17.147.89
96.17.178.132
23.49.248.6
23.222.30.64
23.55.110.70
23.2.13.153
173.222.105.65
23.200.143.73
23.201.217.14
23.55.110.200
95.101.23.25
23.37.206.186
173.222.105.42
95.101.29.12
88.221.92.177
23.50.131.132
184.86.251.27
2.16.244.11
2.16.27.71
2.19.10.30
104.121.12.86
23.73.207.16
2.18.190.26
96.16.122.149
23.201.217.150
95.101.23.168
96.17.207.162
96.16.122.48
95.101.35.73
23.192.237.208
80.67.82.179
96.17.207.154
2.21.89.66
2.18.190.27
95.100.156.147
23.192.46.51
104.76.220.137
23.36.162.198
23.37.197.128
96.17.207.143
23.36.162.208
23.36.162.202
23.200.143.88
23.55.110.46
23.55.110.143
173.222.105.18
2.23.176.166
23.44.10.10
104.126.37.171
23.55.155.169
23.210.123.174
104.117.76.26
23.46.188.168
23.58.222.147
95.101.200.63
125.56.219.32
23.192.237.209
95.101.29.54
23.46.230.118
96.17.207.153
184.25.52.200
23.202.156.203
23.36.162.196
96.16.122.145
23.33.126.163
95.101.29.30
23.36.162.215
23.39.249.249
2.21.239.29
23.210.73.136
104.126.37.161
23.2.13.186
23.50.131.160
23.219.138.200
96.16.122.153
104.117.76.146
23.38.49.97
2.19.196.105
96.16.122.141
104.78.170.186
96.17.222.31
23.41.37.129
23.2.13.227
23.222.126.108
2.20.255.113
2.17.251.98
23.2.13.152
95.101.23.27
2.21.239.21
23.211.49.252
88.221.168.5
104.103.90.156
23.79.20.249
88.221.132.162
23.59.235.208
23.60.69.118
23.46.188.71
104.122.212.92
23.219.1.4
23.57.43.195
184.51.252.135
2.22.6.68
23.217.11.56
95.100.69.108
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29
23.40.63.69</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/archivetell/4967" target="_blank">📅 16:24 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTelegram APKs for Android</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Telegram.apk</div>
  <div class="tg-doc-extra">77.9 MB</div>
</div>
<a href="https://t.me/archivetell/4966" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">12.7.3 (6750)
Directly downloadable from
telegram.org/android</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/archivetell/4966" target="_blank">📅 16:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zr_bE0EBDQ2_OWtH6MFh5rAKww8qr_Gwi30naNkyV_rqvXHQd9_gDqK6Qe1d86Wmj4i_BVjZ3SSlB_B-oQGR_DmeP51br6Lfxxakh-qXkjVqIlcP4fnk2G9AJZM5Vcr85a4TKYObFpkxtuXD8HcQaOUtb5Q4RVkcridxhndxYxMtKki1fq0ckSjTdawdsU_a7QsextkLAdXEViJIVadDerKdU_ottsuwkx66ZzRWXh7kenPhuJ_vEhs76cL84_SNZf6RQW7HUYBZrPYyznArK_TuA3Hr4GYIIdoMsA_PnaHWXxiSiNaS1WXTTlm4Lb_DaS7cGFfe5TitttByi7zP1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساده ترین تلاش های یک ایرانی برای اتصال به نت بین المللی:</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/4965" target="_blank">📅 15:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شیرخورشید   CDN Edge IPs: 151.101.192.223 CDN SNI Hostname: python.org‎</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/archivetell/4964" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شیرخورشید
CDN Edge IPs:
151.101.192.223
CDN SNI Hostname:
python.org
‎</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/4963" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اسکنر برای آی پی تمیز https://github.com/seramo/sni-scanner</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/4961" target="_blank">📅 15:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اسکنر برای آی پی تمیز
https://github.com/seramo/sni-scanner</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/4960" target="_blank">📅 14:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">آپدیت ویندوز: من ادامه میدم تا وقتی نت هست اتشفشانو نمیشه با برف بست</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/4959" target="_blank">📅 14:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دستیار هوش مصنوعی تولید محتوا:
@Scriblastbot
- مقالات و پست‌های وبلاگی اصیل می‌نویسد.
- محتوا را برای هر پلتفرمی بازاستفاده می‌کند.
- متن‌های جذاب برای شبکه‌های اجتماعی می‌سازد.
- سئو را بهینه می‌کند و لحن/سبک‌های متنوعی را تنظیم می‌نماید.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/4958" target="_blank">📅 14:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">Windows.Update.Blocker.1.8.rar</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/4957" target="_blank">📅 14:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4956">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Windows.Update.Blocker.1.8.rar</div>
  <div class="tg-doc-extra">988.5 KB</div>
</div>
<a href="https://t.me/archivetell/4956" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">غیرفعال کردن اپدیت خودکار ویندوز 10 و 11
(تست کردم خودم)
با یه کلیک ساده اپدیت خودکار رو خاموش کنید و وقتی نیاز داشتی فعال کن .
منبع سافت 98
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/4956" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4955">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آقا واسه شیر کردن فیلترشکن با PdaNet رو کابل USB که از همه پایدارتره اینجوری پیش برین: ۱. اول فیلترشکن گوشیو روشن کنین. ۲. گوشیو با کابل وصل کنین به کامپیوتر. ۳. تو برنامه PdaNet گوشی، تیک USB Tether رو بزنین. (اگه پیام USB Debugging داد، always allow رو تیک…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/archivetell/4955" target="_blank">📅 14:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4954">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">PdaNet+ v5.32 (Premium).apk</div>
  <div class="tg-doc-extra">1.7 MB</div>
</div>
<a href="https://t.me/archivetell/4954" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">PdaNet+ v5.32 (Premium).apk
@archivetell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/archivetell/4954" target="_blank">📅 14:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شاید واستون سوال باشه که چرا پترنیها اینقدر تلاش میکنه واسه پیدا کردن این متد ها  چون حکومت نتونه وایت لیست  رو به راحتی اجرا کنه و فشار زیادی وارد بشه روی فیلترینگ</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/4952" target="_blank">📅 13:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تازه اسکن شده سرعت فضایی
💥
:
شیر و خورشید؛
84.26.13.91
23.54.210.170
23.44.201.206
23.220.163.205
23.209.46.33
23.10.34.11
23.39.185.35
23.32.152.106
23.218.232.181
23.206.188.212
2.21.2.89
23.208.222.120
23.48.203.248
23.44.201.136
23.44.201.151
23.44.201.149
2.21.2.58
23.3.90.48
23.44.201.41
2.19.204.184
23.218.232.188
23.44.201.12
23.212.253.227
23.201.31.155
23.220.163.203
23.44.201.185
23.52.116.66
23.44.201.17
23.62.54.24
23.218.239.132
23.39.149.69
23.52.40.147
23.58.95.144
2.16.244.58
23.212.253.137
2.17.106.176
23.62.54.137
2.17.106.5
23.203.134.233
23.212.253.232
23.206.188.197
23.44.201.170
23.54.127.39
23.214.170.83
23.52.40.89
23.55.176.73
23.202.229.140
23.215.56.61
2.17.106.166
23.222.126.108
184.25.85.224
23.1.241.123
23.3.90.43
بزنید عشق کنید ری اکشن هم یادتون نره
❤️</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/4951" target="_blank">📅 13:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شاید واستون سوال باشه که چرا پترنیها اینقدر تلاش میکنه واسه پیدا کردن این متد ها
چون حکومت نتونه وایت لیست  رو به راحتی اجرا کنه و فشار زیادی وارد بشه روی فیلترینگ</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/4950" target="_blank">📅 13:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p27f9A3B2LiVQrv4qf8tDCLRQBmhrapyLHPZR08SwdaLL8l80IJDeFHewUwjFZ1qKDj06SXsxPEChwybUdlSXDotyf30Cug_Wm3MMMmzqij9YbSF3lXevugvSemfOUfd0Wsja4gJmITenEjODrNgKLKLMCmobEoH5cFq0PYcP1fdadz3A32P8tFh_cWFcMxcOR4numXUAOwURUH47rPt41ss_L7A6G3jezLKUoyLuNHhRsGTWclGfJjWNPaZ73eZb-RROpjFuFspM45pR6QjT7pvFDT1Ip1_F7tb_MJUe-Ir2a0b6vszs7Uu9sUkIMsYPOW10m4lkl-oepr36jBryg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت.
حالا بیا جلو اینم بگیر
😎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/4949" target="_blank">📅 11:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نتلیفای بای بای
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/4948" target="_blank">📅 11:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">hosts.txt</div>
  <div class="tg-doc-extra">4.1 KB</div>
</div>
<a href="https://t.me/archivetell/4947" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اینا هم اسکن کنید..</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/4947" target="_blank">📅 10:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">akamai-AS20940.json</div>
  <div class="tg-doc-extra">97.1 KB</div>
</div>
<a href="https://t.me/archivetell/4945" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">رنج آیپی akamai واسه اسکن</div>
<div class="tg-footer">👁️ 960 · <a href="https://t.me/archivetell/4945" target="_blank">📅 10:15 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4944">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ping.py</div>
  <div class="tg-doc-extra">17.6 KB</div>
</div>
<a href="https://t.me/archivetell/4944" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکنر TCP رنج ایپی های Akamai
فایل hosts.txt رو کنارش بذارید و روی هر سیستم عاملی با پایتون اجراش کنید (ورودی ایپی تکی و ایپی رنج ساپورت میکنه)
- قابلیت تشخیص NAT از اتصال واقعی بر اساس پینگ
- سرعت ورکر رو میشه تنظیم کرد
- قابلیت بهینه سازی تایم اسکن
- خروجی رو توی فایل vali.txt میده.
بدون پیش نیاز...</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/4944" target="_blank">📅 10:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ایرانسل ، همراه اول و رایتل   شیر و خورشید تست کنید   185.200.232.40 185.200.232.43</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/4943" target="_blank">📅 10:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شیر و خورشید
151.101.0.223
151.101.128.223
151.101.192.223
65.109.34.234
151.101.64.223
142.54.178.211
2.16.53.50
2.16.53.11
95.101.133.82
95.101.133.42
104.103.65.50
2.23.168.47
104.103.64.7
2.23.168.254
2.23.168.144
2.23.169.249
2.23.169.42
2.23.170.80
104.103.65.5
95.101.133.131
104.103.65.74
2.16.20.51
23.221.28.57
23.221.29.29
23.221.28.5
2.23.169.111
2.23.168.96
2.23.169.12
2.23.168.174
2.23.168.7
184.84.221.34
2.23.41.22
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/4942" target="_blank">📅 10:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Sni-radar.zip</div>
  <div class="tg-doc-extra">303.4 KB</div>
</div>
<a href="https://t.me/archivetell/4941" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔹
سورس اسکنر اختصاصی تیم پرشیا
❤️
🟢
این
سورس اسکنر sni و Cdn هست و با بهترین قابلیت ها نوشته شده است
☑️
💡
اموزش نصب در کامپیوتر:
🔹
اول فایل را دانلود کرده سپس استخراج کنید
🔹
سپس رو محل فایل کلیک کرده ترمینال را باز کرده و در ان این دستور را بنویسید:
pip install -r requirements.txt
🔹
سپس این دستور را بنویسید:
python sni_web.py
🔹
بعدش صفحه باز میشه و میتونید اسکن را شروع کنید
🟢
🟢
🟢
🟢
🟢
🟢
🟢
🟢
🟢
🟢
🟢
🟢
⏺️
اموزش نصب در گوشی با برنامه termux
🔹
اول وارد برنامه ترموکس شده و پکیچ های پایتون نصب کنید
🔹
سپس دستور زیر را وارد کنید
git clone https://github.com/DevMoEiN/SNI-Radar.git
🔹
سپس این دستور:
cd SNI-Radar
🟢
بعد این:
pip install flask
🔹
و در اخر این:
python sni_web.py
⏺️
سپس این را در کروم تایپ کنید:
http://127.0.0.1:10808</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/4941" target="_blank">📅 09:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4940">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ایرانسل ، همراه اول و رایتل   شیر و خورشید تست کنید   185.200.232.40 185.200.232.43</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/4940" target="_blank">📅 09:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شیر و خورشید همه نتا
185.200.232.8
185.200.232.9
185.200.232.11
185.200.232.16
185.200.232.17
185.200.232.19
185.200.232.24
185.200.232.25
185.200.232.26
185.200.232.34
185.200.232.40
185.200.232.42
185.200.232.43
185.200.232.49
185.200.232.56
185.200.232.57
185.200.232.58
185.200.232.64
185.200.232.65
185.200.232.66
185.200.232.67</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/4939" target="_blank">📅 09:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سامانتل شیر و خورشید
184.24.77.42
184.24.77.32
184.24.77.5
184.24.77.7
184.24.77.16
184.24.77.36
184.24.77.21
184.24.77.11
23.48.23.186
23.48.23.133
23.48.23.195
23.48.23.178
184.24.77.29
185.200.232.49
185.200.232.50
185.200.232.42
185.200.232.41</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/4938" target="_blank">📅 09:47 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سایت های وایت لیست شده رو بستن تا بتونن جلوی این متد رو بگیرن..</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/4937" target="_blank">📅 09:16 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ایرانسل ، همراه اول و رایتل
شیر و خورشید تست کنید
185.200.232.40
185.200.232.43</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/4936" target="_blank">📅 09:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4935">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-text">🔥
متصل
https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR%20NETLIFY%20SUB</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/4935" target="_blank">📅 04:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=jucmCXmGRH0EJp1m4l7n6bcioPhk9oUJv893R9RjYGLBia9PkaMDKFG6jPKsEPG7k5zcyeWH751JoyFcG1udYJodULfuKbmHqYRflyTI2yLr-gqUEdeBSARdWrSzbp-lH7GA_01_N8nmsTFd9xETE0anhmWT9rJvu2OwgVlIiPxZsXKUUbmQHg0xsQWEfYM00d-yFCXcJnnNkTrsleG5JCShXwtJ88_V_a5UFoEFxTTqt5EzkCXa31vYlbnSZ3bjRHe7kLdbnjP4syBrIOBfaJU1VNp4YEIx5XyOIEBgnSkdy-JluvYBVwM8W1Wu2mWHTd92VbpR5itGleLy4ioFfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=jucmCXmGRH0EJp1m4l7n6bcioPhk9oUJv893R9RjYGLBia9PkaMDKFG6jPKsEPG7k5zcyeWH751JoyFcG1udYJodULfuKbmHqYRflyTI2yLr-gqUEdeBSARdWrSzbp-lH7GA_01_N8nmsTFd9xETE0anhmWT9rJvu2OwgVlIiPxZsXKUUbmQHg0xsQWEfYM00d-yFCXcJnnNkTrsleG5JCShXwtJ88_V_a5UFoEFxTTqt5EzkCXa31vYlbnSZ3bjRHe7kLdbnjP4syBrIOBfaJU1VNp4YEIx5XyOIEBgnSkdy-JluvYBVwM8W1Wu2mWHTd92VbpR5itGleLy4ioFfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/4933" target="_blank">📅 03:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">CDN Edge IPs:
151.101.0.223
151.101.128.223
151.101.192.223
65.109.34.234
151.101.64.223
142.54.178.211
2.16.53.50
2.16.53.11
95.101.133.82
95.101.133.42
104.103.65.50
2.23.168.47
104.103.64.7
2.23.168.254
2.23.168.144
2.23.169.249
2.23.169.42
2.23.170.80
104.103.65.5
95.101.133.131
104.103.65.74
2.16.20.51
23.221.28.57
23.221.29.29
23.221.28.5
2.23.169.111
2.23.168.96
2.23.169.12
2.23.168.174
2.23.168.7
184.84.221.34
2.23.41.22
CDN SNI Hostname:
python.org</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/archivetell/4931" target="_blank">📅 01:14 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⭐
184.50.87.44
🫥
SNI Hostname:
python.org</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/4930" target="_blank">📅 01:10 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4929">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MITM-DomainFronting-16.zip</div>
  <div class="tg-doc-extra">18.3 KB</div>
</div>
<a href="https://t.me/archivetell/4929" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ مستقیم MitM-DomainFronting-v16: https://github.com/patterniha/MITM-DomainFronting/releases/tag/v16  تغییرات: باز کردن موقت سایت github</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/4929" target="_blank">📅 01:07 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">CDN SNI Hostname:
pypi.org
Ip :
151.101.64.223
CDN SNI Hostname:
a.optnmstr.com
Ip :
84.17.46.53
CDN SNI Hostname:
docs.mapbox.com
Ip :
13.227.192.92</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/4928" target="_blank">📅 01:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کانفیگ مستقیم MitM-DomainFronting-v16:
https://github.com/patterniha/MITM-DomainFronting/releases/tag/v16
تغییرات:
باز کردن موقت سایت github</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/4927" target="_blank">📅 01:04 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4926">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">📌
نحوه اسکن آیپی‌‌های Akamai در ترموکس :
1⃣
به یک فیلترشکن متصل بشید و ​ترموکس را باز کنید و این ۳ خط را کپی کنید و اینتر بزنید تا ابزارهای لازم نصب بشن :
pkg update && pkg upgrade -y
pkg install nmap -y
termux-setup-storage
اگر پیغامی برای دسترسی به فایل‌ها اومد، Allow را بزنید.
2⃣
​
حالا فیلترشکن رو خاموش کنید و دستور زیر رو بزنید
:
nmap -p 443 --open -T4 2.16.0.0/1
8
‼️
من در دستور از رنج آیپی
2.16.0.0/18
استفاده کردم و 4 آیپی وایتی که اسکن کرد رو براتون گذاشتم، شما میتونید اون رنج‌ رو پاک کنید و از این مخزن گیت‌هاب، سایر رنج‌ها رو در دستور جایگذاری کنید :
https://github.com/platformbuilds/Akamai-ASN-and-IPs-List
بعد از پایان اسکن، ​هر جا نوشته بود Nmap scan report for و زیرش نوشته بود 443/tcp open یعنی اون آیپی‌ وایته و باید کپیش کنید
.
بهتره رنج‌های کوچک رو اسکن کنید، اسکن رنج‌آیپی‌های بزرگ، ساعت‌ها زمان میبره</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/4926" target="_blank">📅 01:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4925">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🌐
184.26.163.51
CDN SNI Hostname:
python.org</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/4925" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">CDN Edge IPs:
167.82.48.223
CDN SNI Hostname:
files.pythonhosted.org</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/4924" target="_blank">📅 00:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4923">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">CDN Edge IPs:
151.101.64.223
CDN SNI Hostname:
pypi.org</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/4923" target="_blank">📅 00:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">CDN edge IPs :
151.101.128.223
CDN SNI Hostname :
python.org</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/4922" target="_blank">📅 00:50 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">CDN edge IPs :
151.101.0.223
CDN SNI Hostname :
www.python.org</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/4921" target="_blank">📅 00:41 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تست شده شیر و خورشید   CDN Edge IPs: 151.101.192.223  CDN SNI Hostname: python.org</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/4920" target="_blank">📅 00:20 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">از این کانفیگ هایی که وقتی کلودفلر بازه کار میکنه بدید کامنت</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/4919" target="_blank">📅 00:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">می‌دونستید جعبه سیاه هواپیما اصلاً سیاه نیست؟
✈️
🟧
آره، در واقع یه نارنجیِ جیغ و زننده‌ست. این‌طوری رنگش کردن که وقتی هواپیما سقوط کرد، همه‌چیز سوخت و به خاکستر تبدیل شد، بتونن از بین اون‌همه سیاهی و ویرانی پیداش کنن تا بفهمن دقیقاً کدوم فاجعه و کدوم نقص باعث این سقوط شده. جعبه سیاه، راویِ صادقِ فاجعه‌ست.
اما حالا یه فکت دارک‌تر: می‌دونستید «سیم‌کارت سفید» در اصل قرمزه؟
🩸
📱
همین الان که نت کل کشور قطع شده و ما رو تو یه سیاه‌چال دیجیتال حبس کردن، یه عده از «ما بهتران» دارن با همین سیم‌کارت‌های به‌اصطلاح «سفید» تو اینترنت جهانی می‌چرخن و احتمالاً الان دارن چک می‌کنن ببینن سهامشون تو بورس نیویورک چقدر بالا پایین شده.
ولی چرا می‌گم قرمزه؟
چون این سفیدی فقط یه روکشه. این سیم‌کارت تو بی‌عدالتی و خفقان خیس خورده. رنگش قرمزه، به رنگ حقِ بدیهیِ ۸۰ میلیون آدم که سر بریده شده تا تو جیب یه اقلیت خاص جا بشه. به رنگ خط قرمزی که روی صدای یه ملت کشیدن.
تفاوتشون اینجاست:
جعبه «سیاه» که نارنجیه، بعد از سقوط به داد آدم می‌رسه تا حقیقت رو بگه.
اما سیم‌کارت «سفید» که قرمزه، خودش همون موتوریه که داره مارو به سمت سقوط می‌بره و حقیقت رو خفه می‌کنه.
خلاصه که گول اسم‌ها رو نخورید... تو سیستمی که سیاهی‌هاش نارنجیه، سفیدی‌هاش قطعاً بوی خون، تبعیض و قطعیِ نت میده.
#سیم_کارت_پرو
#قطعی_اینترنت
#تبعیض
#اینترنت_طبقاتی
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/4918" target="_blank">📅 00:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4917">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تست شده شیر و خورشید
CDN Edge IPs:
151.101.192.223
CDN SNI Hostname:
python.org</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/4917" target="_blank">📅 23:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4916">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚀
معرفی ابزار Pantegnos: رمزگشایی و استخراج کانفیگ‌های قفل‌شده!
---
رفقا سلام!
✋
خیلی وقتا پیش میاد که تو یه اپلیکیشن VPN خاص (مثل Netmod یا Slipnet) یه کانفیگ فوق‌العاده و پرسرعت پیدا می‌کنید، اما کانفیگ قفل و رمزنگاری شده و فرمت‌های عجیبی (مثل //:slipnet-enc یا //:nm-vless) داره. در نتیجه نمی‌تونید اطلاعات اصلی سرور (آی‌پی، پورت، SNI و...) رو بکشید بیرون تا تو برنامه‌های استاندارد خودتون مثل V2rayNG یا NekoBox ازش استفاده کنید.
امروز یه ابزار تازه‌نفس و خفن به اسم
Pantegnos
(نوشته شده با زبان قدرتمند Go) رو بهتون معرفی می‌کنیم که حلال همین مشکله!
این ابزار برای محققین شبکه و دور زدن فیلترینگ طراحی شده و کارش اینه که کانفیگ‌های اختصاصی و قفل‌شده‌ی کلاینت‌های مختلف رو می‌شکافه و دیتای اصلی رو براتون دیکریپت (رمزگشایی) می‌کنه.
🛠
کانفیگ‌های پشتیبانی‌شده تا این لحظه:
🔹
فرمت‌های Netmod (مثل کانفیگ‌هایی که با -nm شروع می‌شن)
🔹
فرمت‌های Slipnet
(توسعه‌دهنده گفته به زودی برنامه‌های بیشتری رو هم اضافه می‌کنه).
💻
نحوه استفاده:
کار با این ابزار خیلی سادست. اصلاً نیازی به بیلد کردن هم ندارید؛ فایل اجرایی آماده تو بخش Releases گیت‌هابش هست. کافیه کانفیگ‌های قفل‌شدتون رو بذارید داخل یه پوشه (مثلاً به اسم configs) و تو ترمینال سیستم این دستور رو بزنید تا فایل‌های استخراج‌شده رو تو پوشه خروجی تحویلتون بده:
./Pantegnos -input configs -output outputs
🔗
لینک پروژه و دانلود در گیت‌هاب:
https://github.com/FrontierTM/Pantegnos
📌
#رمزگشایی
#دیکریپت
#کانفیگ
#نت_مد
#VLESS
#ابزار
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/4916" target="_blank">📅 23:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ایرانسل تست شده
شیر و خورشید
CDN SNI hostname خالی بذار
CDN edge IPs :
2.16.20.51
2.16.53.11
2.16.53.50
2.16.19.136</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/4915" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">جهت اسکن آیپی های fastly یا akami یا هر آیپی / رنجی که میخواین میتونید از ریپوی زیر استفاده کنید
https://github.com/penhandev/IP-Scanner</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/4914" target="_blank">📅 23:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ip.txt</div>
  <div class="tg-doc-extra">145.8 KB</div>
</div>
<a href="https://t.me/archivetell/4913" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست آیپی تمیز</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/4913" target="_blank">📅 23:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خلاصه آموزش شیر و خورشید واسه اونا که تازه وارد کانال شدن
اول
شیر و خورشید
رو نصب کن
بعد از نصب اپلیکیشن ابتدا وارد (Options|گزینه ها) بشید و سپس (More Options|گزینه های بیشتر) رو انتخاب کنید.
در قسمت Connection Protocol، گزینه‌ی CDN Fronting رو انتخاب کنید cdn edgei ps آیپی وارد کن بعد هم بزن وصل</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/archivetell/4912" target="_blank">📅 23:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گیت هاب بسته شد..</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/4911" target="_blank">📅 22:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ایرانسل تست شده
شیر و خورشید
CDN SNI hostname خالی بذار
CDN edge IPs :
96.16.122.59
95.101.35.83
173.222.105.65
95.101.35.73
23.58.222.147</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/4910" target="_blank">📅 22:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گیت هاب بسته شد..</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/4909" target="_blank">📅 22:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شیر و خورشید
CDN SNI hostname خالی بذار
CDN edge IPs :
2.21.2.34
23.197.216.67
2.21.2.8
2.21.2.33
2.21.2.105
2.21.2.59
2.21.2.18
2.21.2.50</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/4908" target="_blank">📅 22:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">fastly-AS54113.json</div>
  <div class="tg-doc-extra">38.6 KB</div>
</div>
<a href="https://t.me/archivetell/4907" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">رنج فستلی واسه اسکن</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/archivetell/4907" target="_blank">📅 22:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ip_scanner_gui.exe</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/4905" target="_blank">📅 22:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">akamai-AS20940.json</div>
  <div class="tg-doc-extra">97.1 KB</div>
</div>
<a href="https://t.me/archivetell/4904" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">رنج آیپی akamai واسه اسکن</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/archivetell/4904" target="_blank">📅 22:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ip_scanner_gui.exe</div>
  <div class="tg-doc-extra">9.6 MB</div>
</div>
<a href="https://t.me/archivetell/4903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اسکنر آیپی
قابلیت هاش:
1. چک کردن ایپی معمولی
2. چک کردن رنج ایپی Fastly و Akamai
3. بصورت دستی اضافه کردن ایپی یا رنج
4. بصورت فایل اضافه کردن .txt  و .json
5. ماکسیموم پینگ گذاشتن واسش مثلا زیر 180ms
6. ایپی های که داخل چنلا میزارن بندازید توش اسکن کنه
منبع : پای پکیج</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/archivetell/4903" target="_blank">📅 22:27 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شیر و خورشید
CDN SNI hostname خالی بذار
CDN edge IPs :
2.22.21.152
95.101.23.82
23.215.0.164
23.197.161.35
184.28.230.87
23.220.128.221
96.17.207.142
23.50.131.18
23.36.162.209
23.219.3.212
23.223.245.150
96.16.122.59
23.2.13.138
23.2.13.144
96.17.207.135
23.220.113.51
96.17.72.41
23.203.185.105
95.101.35.83
2.21.239.23
23.54.210.170
23.215.60.73
95.101.181.125
23.192.237.222
23.200.143.71
23.58.222.98
125.56.219.8
104.80.49.118
96.16.122.158
2.21.239.10
96.16.122.65
95.101.23.170
104.111.202.158
23.2.13.201
92.123.102.104
23.58.222.139
2.17.147.89
96.17.178.132
23.49.248.6
23.222.30.64
23.55.110.70
23.2.13.153
173.222.105.65
23.200.143.73
23.201.217.14
23.55.110.200
95.101.23.25
23.37.206.186
173.222.105.42
95.101.29.12
88.221.92.177
23.50.131.132
184.86.251.27
2.16.244.11
2.16.27.71
2.19.10.30
104.121.12.86
23.73.207.16
2.18.190.26
96.16.122.149
23.201.217.150
95.101.23.168
96.17.207.162
96.16.122.48
95.101.35.73
23.192.237.208
80.67.82.179
96.17.207.154
2.21.89.66
2.18.190.27
95.100.156.147
23.192.46.51
104.76.220.137
23.36.162.198
23.37.197.128
96.17.207.143
23.36.162.208
23.36.162.202
23.200.143.88
23.55.110.46
23.55.110.143
173.222.105.18
2.23.176.166
23.44.10.10
104.126.37.171
23.55.155.169
23.210.123.174
104.117.76.26
23.46.188.168
23.58.222.147
95.101.200.63
125.56.219.32
23.192.237.209
95.101.29.54
23.46.230.118
96.17.207.153
184.25.52.200
23.202.156.203
23.36.162.196
96.16.122.145
23.33.126.163
95.101.29.30
23.36.162.215
23.39.249.249
2.21.239.29
23.210.73.136
104.126.37.161
23.2.13.186
23.50.131.160
23.219.138.200
96.16.122.153
104.117.76.146
23.38.49.97
2.19.196.105
96.16.122.141
104.78.170.186
96.17.222.31
23.41.37.129
23.2.13.227
23.222.126.108
2.20.255.113
2.17.251.98
23.2.13.152
95.101.23.27
2.21.239.21
23.211.49.252
88.221.168.5
104.103.90.156
23.79.20.249
88.221.132.162
23.59.235.208
23.60.69.118
23.46.188.71
104.122.212.92
23.219.1.4
23.57.43.195
184.51.252.135
2.22.6.68
23.217.11.56
95.100.69.108
23.40.63.69</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/4902" target="_blank">📅 22:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شیر و خورشید
CDN SNI hostname خالی بذار
CDN edge IPs :
23.221.28.5
23.44.201.206
23.220.163.205
23.209.46.33
23.10.34.11
23.39.185.35
23.32.152.106
23.218.232.181
23.206.188.212
2.21.2.89
23.208.222.120
23.48.203.248
23.44.201.136
23.44.201.151
23.44.201.149
2.21.2.58
23.3.90.48
23.44.201.41
2.19.204.184
23.218.232.188
23.44.201.12
23.212.253.227
23.201.31.155
23.220.163.203
23.44.201.185
23.52.116.66
23.44.201.17
23.62.54.24
23.218.239.132
23.39.149.69
23.52.40.147
23.58.95.144
2.16.244.58
23.212.253.137
2.17.106.176
23.62.54.137
2.17.106.5
23.203.134.233
23.212.253.232
23.206.188.197
23.44.201.170
23.54.127.39
23.214.170.83
23.52.40.89
23.55.176.73
23.202.229.140
23.215.56.61
2.17.106.166
23.222.126.108
184.25.85.224
23.1.241.123
23.3.90.43
184.26.13.91
23.54.210.170</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/4901" target="_blank">📅 22:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-text">🚀
ساب ها اپدیت شدن
🔺
ساب آزمایشی (دانلود سنگین دارید با این بزنید)
https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/test2_1.0.4.txt
🔺
ساب ثابت کانال
https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/IR_NETLIFY_SUB_new.txt
🔺
ساب متغیر (هر بار که باز کنید سرور و sni و ip رندوم میده)
https://sub.ir-netlify.workers.dev/</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/4900" target="_blank">📅 22:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این ساب آپدیت شده و اوکیه   https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/test2_1.0.4.txt</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/4899" target="_blank">📅 20:27 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-text">این ساب آپدیت شده و اوکیه
https://raw.githubusercontent.com/IR-NETLIFY/NETLIFY/refs/heads/main/test2_1.0.4.txt</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/4898" target="_blank">📅 20:27 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4897">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dr2XVY0Kh2QKfbG6nc2wcFA4FfK2JL0pbZdD8UP94zY8eb8nTW4al1S8RBLX98eQPm0JlTGf0mOF1dUnU2wG3Rrrq2aY_bj5HFJomzBrxWc2n3y2nx1YCifdPEauQ8vKyhiyf1kFlLjTjbRf6Jw9TdmUj64VQDU3W7j3l7W8h8Ar7zSTHXIlC9xEi81KzpSHN5uZWbYen7kpfV9nT0GFya-wBNLktn9ooEmgxyL_gLjcKOF-Ire-NWy75pM3sRTHSfDbodH7nCZNa4yzWhRMvu432QeIG418yKlEmTuZn9OEv8-hhnB8f7BiI64Wkhw-wuGvaBla7s4svyQYy882xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Iran network core:</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/4897" target="_blank">📅 20:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@ArchiveTell.txt</div>
  <div class="tg-doc-extra">74.2 KB</div>
</div>
<a href="https://t.me/archivetell/4896" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">شیر و خورشید
CDN SNI hostname خالی بذار
CDN edge IPs :
فایل رو باز کن و همه این آیپی ها رو جای گذاری کن</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/4896" target="_blank">📅 20:22 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ایرانسل تست شده   2.19.204.225</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/4895" target="_blank">📅 20:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ایرانسل تست شده
شیر و خورشید
CDN SNI hostname خالی بذار
CDN edge IPs :
23.221.28.5
23.44.201.206
23.220.163.205
23.209.46.33
23.10.34.11
23.39.185.35
23.32.152.106
23.218.232.181
23.206.188.212
2.21.2.89
23.208.222.120
23.48.203.248
23.44.201.136
23.44.201.151
23.44.201.149
2.21.2.58
23.3.90.48
23.44.201.41
2.19.204.184
23.218.232.188
23.44.201.12
23.212.253.227
23.201.31.155
23.220.163.203
23.44.201.185
23.52.116.66
23.44.201.17
23.62.54.24
23.218.239.132
23.39.149.69
23.52.40.147
23.58.95.144
2.16.244.58
23.212.253.137
2.17.106.176
23.62.54.137
2.17.106.5
23.203.134.233
23.212.253.232
23.206.188.197
23.44.201.170
23.54.127.39
23.214.170.83
23.52.40.89
23.55.176.73
23.202.229.140
23.215.56.61
2.17.106.166
23.222.126.108
184.25.85.224
23.1.241.123
23.3.90.43
184.26.13.91
23.54.210.170</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/archivetell/4894" target="_blank">📅 20:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4893">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ایرانسل تست شده
2.19.204.225</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/4893" target="_blank">📅 18:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Akamai-IP-Scanner.zip</div>
  <div class="tg-doc-extra">1.8 KB</div>
</div>
<a href="https://t.me/archivetell/4891" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">برنامه Akamai IP Scanner
۱. لیست رنج‌های هدف (با پشتیبانی از تمام فرمت‌ها مثل 16/ یا 24/) را در فایل ips.txt قرار دهید. (پیشفرض قرار داده شده)
۲. روی فایل scan.ps1 راست‌کلیک کرده و گزینه Run with PowerShell را برای شروع اسکن انتخاب کنید.
۳. بهترین آی‌پی‌ها به‌صورت لحظه‌ای در clean_ips.txt ذخیره می‌شوند (هر زمان مایل بودید می‌توانید اسکن را متوقف کنید).</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/archivetell/4891" target="_blank">📅 17:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ایرانسل تست شده
2.19.204.251</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/4890" target="_blank">📅 17:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">akamai-scanned-ip.txt</div>
  <div class="tg-doc-extra">71.6 KB</div>
</div>
<a href="https://t.me/archivetell/4889" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست چند هزار تایی ip تمیز akamai
شیر و خورشید
CDN SNI hostname خالی بذار
CDN edge IPs :
این آیپی ها رو بذار</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/archivetell/4889" target="_blank">📅 17:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">2.22.151.4
23.67.253.11
23.67.253.24
23.67.253.55
23.67.253.77
23.67.253.101
23.67.253.120
23.53.35.146
23.53.35.158
23.53.35.171
23.53.35.182
23.53.35.194
23.53.35.207
184.26.163.12
184.26.163.24
184.26.163.38
184.26.163.51
184.26.163.66
184.26.163.79
2.16.186.20
2.16.186.31
2.16.186.44
2.16.186.58
2.16.186.69
2.16.186.81
23.195.81.72
23.195.81.84
23.195.81.96
23.195.81.108
104.124.148.191
104.124.148.203
23.32.5.18
23.32.5.44
23.32.5.71
23.32.5.96
23.32.5.118
23.32.5.141
23.32.5.167
23.32.5.193
23.32.5.214
23.32.5.236
96.16.97.82
96.16.97.104
96.16.97.126
96.16.97.148
96.16.97.169
96.16.97.191
184.50.87.22
184.50.87.44
184.50.87.66
184.50.87.88
92.122.123.128
2.19.204.87
2.19.204.137
2.19.204.144
2.19.204.145
2.19.204.170
2.19.204.184
2.19.204.185
2.19.204.202
2.19.204.210
138.201.54.122
2.22.151.4
2.22.151.9
2.22.151.12
2.22.151.13
2.22.151.15
2.22.151.17
2.22.151.20
2.22.151.22
2.22.151.23
2.22.151.32
2.22.151.36
2.22.151.37
2.22.151.39
2.22.151.47
2.22.151.51
2.22.151.53
2.22.151.54
2.22.151.58
2.22.151.60
2.22.151.62
2.22.151.135
2.22.151.138
2.22.151.139
2.22.151.141
2.22.151.142
2.22.151.143
2.22.151.144
2.22.151.146
2.22.151.149
2.22.151.150
2.22.151.151
2.22.151.152
2.22.151.153
2.22.151.154
2.22.151.155
2.22.151.156
2.22.151.157
2.22.151.158
2.22.151.159
2.22.151.161
2.22.151.162
2.22.151.163
2.22.151.164
2.22.151.168
2.22.151.169
2.22.151.170
2.22.151.171
2.22.151.173
2.22.151.175
2.22.151.179
2.22.151.181
2.22.151.182
2.22.151.183
2.22.151.184
2.22.151.185
2.22.151.186
2.22.151.188
2.22.151.189
2.22.151.190
2.22.151.191
2.22.151.193
2.22.151.194
2.22.151.195
ایرانسل وصله ولی ضعیف</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/4888" target="_blank">📅 17:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4886">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شیر و خورشید   CDN SNI hostname خالی بذار   CDN edge IPs :   2.19.204.225 2.19.204.232 2.19.204.234 2.19.204.240 2.19.204.249 2.19.204.250 2.19.204.251 2.19.205.8 2.19.205.9 2.19.205.11 2.19.205.27 2.19.205.33 2.19.205.34 2.19.205.40 2.19.205.41 2.19.205.42…</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/4886" target="_blank">📅 17:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">میگن رو ایرانسل اکامی رو زدن ، وصلید؟</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/4884" target="_blank">📅 17:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4882">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rvtS_L5siSiYakD750rlBsoVWsZCZd7DOplFiyKCJWU111TCz-T3RHEnrDHjErXXQbqM2Bmn4YvvcQfqVQcSJ2k5lTLbakzekVeNcx0uY4jFO3vK3Z9U7899aEeATIsEgCkIEjFge-UyLJZCJ_Rgzw0mJibYhFZZI5XrWOONclxG322UEeW4PpMduT9sAetiyHx75ppnHenHaRwdxHqYZQU2k69aDxuq_qNJGwaEYIRUc0ump8r9QTpNUMypCFfuR9C8Si6LwBOkOiOgfihshShVAUnrqlLPnZfagHDEnY4moGLkQah6p2fno3UOSJlQUajxxsdEWeuze1NVmyxlxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/olHK_im_SwVFEKQC9MowcSe2lGFTExmVqmef5D-vQR8uodRLC2kPi5rCT3MZVAF4w03f8xgv_BfEOLGqNyoMi7ltarebmLa6vKa8A4QESdI0ENrxM54Owym6rYQiRMzLeu-6_p94iCWnqIQ4NT7y04apA27GTTMNqocMPdzVxH6xgxSVI7ym1QOQv4kGczp1KGctkzSWsYchZWyvcoaF5kcAJo8IYf4xLt_BVHaTQZLjnFVsCeejI5lKte_CjRCB0ynuRO6VDsBxe5LJe8molC2vqeWypElu1XY75UwRLBJUexnCbqFIlK70jqPIPWNRS03sl031VlxnT1Srb4YkYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شیر و خورشید   CDN SNI hostname خالی بذار   CDN edge IPs :   2.19.204.225 2.19.204.232 2.19.204.234 2.19.204.240 2.19.204.249 2.19.204.250 2.19.204.251 2.19.205.8 2.19.205.9 2.19.205.11 2.19.205.27 2.19.205.33 2.19.205.34 2.19.205.40 2.19.205.41 2.19.205.42…</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/archivetell/4882" target="_blank">📅 17:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4881">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شیر و خورشید   CDN SNI hostname خالی بذار   CDN edge IPs :  92.122.123.128 2.19.204.87 2.19.204.137 2.19.204.144 2.19.204.145 2.19.204.170 2.19.204.184 2.19.204.185 2.19.204.202 2.19.204.210 138.201.54.122</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/4881" target="_blank">📅 16:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4880">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فعلا در این کانال صرفا مطالب مهم و پین‌های گروه  @ProjectXHTTP   گذاشته می شود.  ///  اگر کارهای بنده باعث شده گره ای از مشکلات شما باز شود ممنون میشم حمایتی هم از اینجانب بکنید:  USDT (BEP20): 0x76a768B53Ca77B43086946315f0BDF21156bF424  USDT (TRC20): TU5…</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/4880" target="_blank">📅 16:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4879">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">فعلا در این کانال صرفا مطالب مهم و پین‌های گروه
@ProjectXHTTP
گذاشته می شود.
///
اگر کارهای بنده باعث شده گره ای از مشکلات شما باز شود ممنون میشم حمایتی هم از اینجانب بکنید:
USDT (BEP20): 0x76a768B53Ca77B43086946315f0BDF21156bF424
USDT (TRC20): TU5gKvKqcXPn8itp1DouBCwcqGHMemBm8o</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/4879" target="_blank">📅 16:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4878">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شیر و خورشید
CDN SNI hostname خالی بذار
CDN edge IPs :
92.122.123.128
2.19.204.87
2.19.204.137
2.19.204.144
2.19.204.145
2.19.204.170
2.19.204.184
2.19.204.185
2.19.204.202
2.19.204.210
138.201.54.122</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/4878" target="_blank">📅 16:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4876">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompatterniha</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">psiphon-helper-force-akamai.json</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/archivetell/4876" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سایفون میتواند هم از طریق akamai و هم از طریق fastly متصل شود.
این دو کانفیگ سایفون را مجبور میکند که از طریق akamai یا fastly متصل شود.
در کانفیگ akamai شما نیاز به یک ip سفید و در کانفیگ fastly نیاز به یک sni سفید دارید که میتوانید در صورت نیاز آن را در کانفیگ ها تغییر دهید.
گرچه دومین‌فرانتینگ های استفاده شده به اپ شیر و خورشید اضافه شده اما با استفاده از هسته Xray-core شما از ویژگی های متعددی مثل "فینگرپرینت کروم" و "happyEyeballs" و ... برخوردار هستید.
پروژه های دیگری در راه است حمایت فراموش نشه
@patterniha</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/4876" target="_blank">📅 16:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4874">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">منتظر ایران نتلیفای باشین، از معجزاتش زنده کردن مرده هاست
ایشالا که خبری بشه</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/4874" target="_blank">📅 16:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4873">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🎯
خلاصه و جمع‌بندی متدهای امروز (سایفون + دامین فرانتینگ)
---
رفقا سلام!
✋
امروز یه رگبار پیام تو کانال داشتیم درباره متد جدید و می‌دونم ممکنه با دیدن این همه فایل و ربات و کد، خیلیا گیج شده باشن که «بالاخره کدوم رو باید انجام بدیم؟!»
بیاین خیلی عامیانه و تروتمیز جمع‌بندی کنیم که دقیقاً بدونید باید چیکار کنید:
🔥
راحت‌ترین و سریع‌ترین راه (بدون هیچ دردسری!)
اگر حوصله درگیری با فایل و سرتیفیکیت و تنظیمات پیچیده رو ندارید، فقط نسخه آپدیت‌شده‌ی برنامه «شیر و خورشید» رو نصب کنید.
تو این آپدیت، فقط کافیه پروتکل اتصال رو بذارید روی "فرانتینگ cdn". تمام! برنامه خودش وصل می‌شه و نیازی به گرفتن سرتیفیکیت، برنامه V2ray و وارد کردن کانفیگ نیست.
📱
روش دستی برای اندروید (V2rayNG)
اگه دوست دارید خودتون متد رو دستی پیاده کنید:
۱. دریافت گواهینامه: باید دو تا کلید بگیرید (یا از سایت regery.com، یا ربات‌های تلگرامی مثل
@CrtGen7Bot
). در نهایت باید دو تا فایل به اسم‌های mycert.key و mycert.crt داشته باشید.
۲. نصب در گوشی: تو تنظیمات گوشی CA certificate رو سرچ کنید و فایل mycert.crt رو اونجا نصب کنید.
۳. تنظیمات V2rayNG: برید تو بخش assets files برنامه و اون دو تا فایل رو اضافه کنید. بعدش طبق آموزش قبلی، سایفون رو بهش متصل کنید.
💻
روش راحت برای ویندوز
برای ویندوز ابزار آماده PsiphonOverMITM کار رو راحت کرده:
۱. فایل زیپ پروژه رو از گیت‌هاب دانلود و اکسترکت کنید.
۲. روی فایل Run-PsiphonOverMITM.bat راست‌کلیک کرده و Run as Administrator رو بزنید.
۳. برنامه سایفون رو باز کنید، برید تو Settings و تو بخش Upstream Proxy این مشخصات رو وارد کنید:
Hostname:
127.0.0.1
Port: 20808
۴. تغییرات رو تایید کنید تا متصل بشه.
⚠️
اون آموزش طولانی SSL سرور ایران چی بود؟
پستی که درباره انتقال فایل‌های fullchain و privkey به سرور داخل بود، فقط و فقط مخصوص ادمین‌ها و کسانیه که سرور شخصی دارن. اگر شما یک کاربر عادی هستید، اون پست رو کاملاً نادیده بگیرید!
💡
نتیجه‌گیری: اولویت اول برای اینکه گیج نشید و سریع وصل بشید، همون دانلود نسخه جدید "شیر و خورشید" و گذاشتنش روی حالت "فرانتینگ cdn" هست. لذتش رو ببرید!
✌️
📌
#آموزش
#سایفون
#دامین_فرانتینگ
#نت_ملی
#تونل
#شیر_و_خورشید
ArchiveTell |</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/4873" target="_blank">📅 15:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4872">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚀
آموزش اتصال رایگان به اینترنت آزاد (ترکیب Psiphon + دامین فرانتینگ پترنیها)
---
رفقا سلام!
✋
امروز یه متد به‌شدت خفن، بدون پیش‌نیاز و کاملاً رایگان براتون داریم که با ترکیب کلاینت سایفون (شیر و خورشید) و کانفیگ‌های دامین فرانتینگِ پترنیها کار می‌کنه و اینترنت آزاد رو براتون میاره.
این روش برای وب‌گردی، اینستاگرام و تلگرام عالیه (البته برای گیم آنلاین پیشنهاد نمی‌شه). تمام فایل‌های مورد نیاز هم از قبل آماده شده و لینک‌هاش پایین پست هست!
👇
🖥
آموزش برای ویندوز (V2rayN)
1️⃣
نصب V2rayN: برنامه V2rayN رو باز کنید (اگه ارور داد، Runtime و Framework نسخه ۶ به بالا رو نصب کنید).
2️⃣
ساخت سرتیفیکیت: فایل Certificate Generator (موجود در فایل‌های دانلود) رو داخل پوشه bin تو مسیر V2rayN کپی و اجرا کنید تا دو فایل جدید ساخته بشه.
3️⃣
نصب سرتیفیکیت: روی فایل mycert راست‌کلیک کنید، Install Certificate رو بزنید. مسیر Local Machine و بعد Trusted Root Certification Authorities رو انتخاب کنید تا نصب بشه.
4️⃣
تنظیمات V2rayN:
🔸
برنامه رو باز کنید، از Configuration گزینه Add Custom Configuration رو بزنید. یه اسم بذارید، فایل Json پترنیها رو Browse کنید و Core type رو روی Xray بذارید.
🔸
تو مسیر Settings ➔ Option Settings، پورت Mux رو حتماً روی 10808 تنظیم کنید.
🔸
کانفیگ رو انتخاب، Enter بزنید و وضعیت سیستم رو روی Clear System Proxy بذارید.
5️⃣
تنظیمات کلاینت شیر و خورشید: برنامه رو باز کنید، برید تو Settings. قسمت Upstream Proxy، هاست رو
127.0.0.1
و پورت رو 10808 قرار بدید و استارت کنید.
📱
آموزش برای اندروید (V2rayNG)
1️⃣
پیش‌نیازها: نصب آخرین نسخه V2rayNG و کلاینت سایفون (شیر و خورشید).
2️⃣
نصب سرتیفیکیت: تو تنظیمات گوشی CA Certificate رو سرچ کنید و فایل mycert.crt (موجود در فایل‌های دانلود) رو نصب کنید.
3️⃣
تنظیمات V2rayNG:
🔸
فایل‌های سرتیفیکیت رو تو نرم‌افزار Add کنید.
🔸
فایل کانفیگ JSON رو با زدن دکمه + و Import from local وارد برنامه کنید.
🔸
تو تنظیمات، پورت (Local Proxy Port) رو روی 10808 و Mode رو روی Proxy Only قرار بدید و کانفیگ رو استارت بزنید.
4️⃣
تنظیمات کلاینت (شیر و خورشید):
🔸
وارد Options ➔ VPN Settings بشید، تیک Don't tunnel selected apps رو بزنید و V2rayNG رو از تونل خارج کنید.
🔸
تو بخش Proxy Settings، گزینه Connect through an HTTP Proxy رو انتخاب کنید. هاست رو
127.0.0.1
و پورت رو 10808 بذارید و استارت رو بزنید.
📥
لینک‌های دانلود و منابع مورد نیاز:
تمام فایل‌ها (V2rayN، V2rayNG، کلاینت شیر و خورشید، Certificate Generator و فایل Json پترنیها) رو می‌تونید از لینک‌های زیر بردارید:
🔗
لینک دانلود مستقیم فایل‌ها در تلگرام:
https://t.me/MatinSenPaii/3035
🔗
لینک پروژه اصلی در گیت‌هاب:
https://github.com/therealaleph/Maste
...
📺
ویدیوی آموزشی کامل در یوتیوب:
https://youtu.be/M3kZxw1M3vE
(اگر این روش براتون مفید بود، می‌تونید از توسعه‌دهنده این متد از طریق لینک
matinsenpai.pages.dev
حمایت کنید
☕️
)
📌
#آموزش
#سایفون
#دامین_فرانتینگ
#نت_ملی
#تونل
#رایگان
#Psiphon
#V2rayN
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/4872" target="_blank">📅 15:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4871">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">##
🚀
آموزش اشتراک‌گذاری اینترنت آزاد روی هات‌سپات (بدون نیاز به نصب برنامه‌ روی گوشی دوم!)
اگر می‌خواهید اینترنت فیلترشده را از لپ‌تاپ به گوشی یا دستگاه‌های دیگر منتقل کنید، به‌طوری که بقیه فقط با وصل شدن به وای‌فای شما به اینترنت بین‌الملل دسترسی داشته باشند، این روش بهترین گزینه است.
###
🛠
پیش‌نیازها:
1. لپ‌تاپ دارای کارت شبکه وای‌فای.
2. برنامه
v2rayN
(نسخه جدید).
3. فعال بودن یک کانفیگ سالم.
###
🟢
مرحله اول: تنظیمات v2rayN
ابتدا باید قابلیت عبور ترافیک از هسته برنامه را فعال کنید:
1. برنامه v2rayN را باز کنید.
2. از منوی پایین، روی آیکون برنامه راست کلیک کرده و
System Proxy
را روی حالت
Set System Proxy
قرار دهید (آیکون برنامه قرمز/رنگ روشن می‌شود).
3. گزینه
TUN Mode
را در قسمت پایین برنامه فعال کنید. این کار باعث می‌شود تمام ترافیک سیستم وارد تونل شود.
###
📡
مرحله دوم: فعال‌سازی Hotspot ویندوز
1. در ویندوز به بخش
Settings
و سپس
Network & Internet
بروید.
2. وارد قسمت
Mobile Hotspot
شوید و آن را
On
کنید.
3. نام (SSID) و رمز عبور را تنظیم کنید.
###
🔗
مرحله سوم: اشتراک‌گذاری آداپتور (مرحله طلایی)
حالا باید جادوی اصلی را انجام دهید تا اینترنتِ "تونل شده" به هات‌سپات منتقل شود:
1. به مسیر زیر در کنترل پنل بروید:
Control Panel > Network and Internet > Network Connections
2. در اینجا لیست کارت‌های شبکه را می‌بینید. کارتی را پیدا کنید که مربوط به v2ray است (معمولاً نامی مثل
nekoray-tun
یا
v2ray-tun
یا
Sing-box
دارد).
3. روی آن راست‌کلیک کرده و
Properties
را بزنید.
4. به تب
Sharing
بروید.
5. تیک گزینه اول یعنی Allow other network users to connect through... را بزنید.
6. در کادر پایین آن، نام آداپتور مربوط به هات‌سپات خود را انتخاب کنید (معمولاً با نامی شبیه Local Area Connection* X یا Microsoft Wi-Fi Direct Virtual Adapter ظاهر می‌شود).
7. روی
OK
کلیک کنید.
###
✅
نتیجه نهایی
حالا هر دستگاهی (گوشی، تلویزیون، کنسول) که به هات‌سپات لپ‌تاپ شما وصل شود،
بدون نیاز به هیچ اپلیکیشن اضافی یا تنظیم پروکسی
، مستقیماً به اینترنت آزاد متصل خواهد بود.
🌐
💡
نکته مهم:
اگر بعد از این کار اینترنت قطع شد، یک‌بار هات‌سپات و v2ray را خاموش و روشن کنید تا آی‌پی‌ها به‌درستی ست شوند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/4871" target="_blank">📅 15:25 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
