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
<img src="https://cdn4.telesco.pe/file/sp59gkS8GmXTpqldZREMAlg2VMthzNaj0TLcoaId7OXbYBbbOdb6Z2KV-KEUzZx-GxBTqIAJ7qF5TmrPpRFP8IMgajoEpS3FSTaoEIiSuE7xFASzrf9puvA6ueu8TB6plQrUOMoXZKzspt8Y3px5rVbLESeSVtJqQWfIdVZ-ClDk2iTrfi6wxlyZAnlyh7Qc-jFARnR6IDWF7LGC7SNt404RzPqF1TxbC5DJoOOUGcDnq-ED0Iw4ntXAh9SKtbAa45gUje3zsc6gjSE0lJbtzPLASAaKiq_o_drqvT_mhT9ZghDUulcGkmQ1Xpn-gwE4bwucgMglSv6dKIRfOE3AEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 8.67K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 10:08:38</div>
<hr>

<div class="tg-post" id="msg-5684">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/archivetell/5684" target="_blank">📅 03:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5683">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/archivetell/5683" target="_blank">📅 03:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5682">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚀
آموزش نصب سریع Hysteria 2 روی سرور اوبونتو (بدون قطعی)  ---  رفقا سلام!
✋
پروتکل Hysteria 2 به دلیل شبیه‌سازی ترافیک به HTTP/3، در حال حاضر یکی از مقاوم‌ترین روش‌ها برای عبور از سیستم‌های فیلترینگ (DPI) است. در این پست، نحوه نصب سریع و بهینه این پروتکل رو…</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/5682" target="_blank">📅 02:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5681">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/5681" target="_blank">📅 02:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5680">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">https://t.me/boost/archivetell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/5680" target="_blank">📅 22:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5679">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⚠️
خدمت دوستان باید چند نکته مهم رو بگم:
هیچ تاثیری روی پروتکل های tcp , udp ,ikev2, wstunnel رو هر حالتی از سانسورشیب بزارید از کانفیگ A تا حتی H و I باشه هیچ تاثیری در وصل شدن سریعتر شما اصلا نداره! فقط این حالت برای وایرگارد قابل استفاده هست دقت کنید
نکته بعدی این هستش که شما حالت server routing رو هم حالت اتوماتیک بزارید چه حالت regular و حتی alternative هیچ تاثیری باز هم تو اتصال شما نداره فقط و فقط حالت اتوماتیک بزارید
مورد اخر گزینه large tls هم روشن بزارید چون به اتصال بهتر شما کمک میکنه وقتی خاموش باشه سخت تر وصل میشید در کل این ۳ مورد رو دوستمون دقت نکردن و نیاز بود این مورد حتما رو بگم که سرگردان تغییر کانفیگ های A,b,c نشید
❤️
#windscribe
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/5679" target="_blank">📅 21:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5678">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">۱۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
❤️
vless://80fbb3e8-d705-4eca-a519-fd82fd6d319a@46.38.137.141:38554?type=tcp&encryption=none&security=none#%40IR_SI%20%2F%20100GB%20UAE%F0%9F%87%A6%F0%9F%87%AA-nubknlau-tpbvyzw1
http://46.38.137.141:2096/sub/eyovzx7b813yvs6g
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/5678" target="_blank">📅 21:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5677">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کانفیگ های اهدایی یکی از ممبرای عزیز
❤️
حجم ۲۰۰ گیگ
vless://5de57aca-c66e-49c6-9bae-fb5eef64d832@sv2.vaslimgroup.ir:8880?encryption=none&host=vaslimgroup.ir&path=%2F&security=none&type=ws#vaslim%20economy-ArchiveTel%20vip-asli-200.00GB%F0%9F%93%8A
vless://5de57aca-c66e-49c6-9bae-fb5eef64d832@snapp.ir:8880?encryption=none&host=vaslimgroup.ir&path=%2F&security=none&type=ws#vaslim%20economy-ArchiveTel%20vip-%F0%9F%92%9Asnapp%F0%9F%92%9A-200.00GB%F0%9F%93%8A
vless://5de57aca-c66e-49c6-9bae-fb5eef64d832@tapsi.ir:8880?encryption=none&host=vaslimgroup.ir&path=%2F&security=none&type=ws#vaslim%20economy-ArchiveTel%20vip-%F0%9F%A9%B7tapsi%F0%9F%A9%B7-200.00GB%F0%9F%93%8A
vless://5de57aca-c66e-49c6-9bae-fb5eef64d832@anten.ir:8880?encryption=none&host=vaslimgroup.ir&path=%2F&security=none&type=ws#vaslim%20economy-ArchiveTel%20vip-%F0%9F%94%B1anten%F0%9F%94%B1-200.00GB%F0%9F%93%8A
هر ۷ تا رو اد کنید ، بعضی مناطق بعضی هاشون کار میده
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/archivetell/5677" target="_blank">📅 21:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5676">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پروکسی اهدایی یکی از ممبرای عزیز
❤️
https://t.me/proxy?server=hh87.salarjavidan.online&port=8991&secret=f41d30c2e0ca3895ca053b26d98af5b3
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/5676" target="_blank">📅 21:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5675">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/archivetell/5675" target="_blank">📅 20:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5674">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آب را گل آلود کن و ماهی بگیر از این آب گل آلود...</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5674" target="_blank">📅 20:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqBuNx7TK-QT4T48oBEwLOiptmNU5RV8pcg0p7WjhflbhaWlLxDOPOHVgudwfTciOBByTgAnXVRU7d3sq2ECkKalfOy5NcZpBXEErFkdyhPx59BSrjue2a2La2h3bx7QDHG1yz1TVVRzScknB-HVLg_nax3WOc6QNZi9ABNB4XdMUEVzyjbveiapKRu8ArPttAXQ5wthiriV_MtGJrCN1oyGsp93bz99ioOF-jsybcsJJluzdgCANZReWmnatZBSZxFKhCy2a8AXDMYUoeyEeOPD_qcMy0XzVXl7V00LzGVMcUDon9gFyqEGOkTm1ETxp6itvYBGmyraSQ0uktYosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به عامل کدنویسی هوش مصنوعی خود، یک سیستم طراحی در یک فایل markdown بدهید.
Awesome DESIGN .md
مجموعه‌ای از فایل‌های طراحی است که از وب‌سایت‌های واقعی متمرکز بر توسعه‌دهندگان الهام گرفته شده‌اند. شما یکی از آن‌ها را در پروژه خود قرار می‌دهید، به عامل هوش مصنوعی خود می‌گویید چه چیزی بسازد و از آن فایل به عنوان یک راهنمای سبک بصری استفاده می‌کند.
بدون خروجی Figma. بدون تنظیمات پیچیده. فقط markdown که به عامل می‌گوید رابط کاربری چگونه باید به نظر برسد و چه احساسی داشته باشد.
https://github.com/VoltAgent/awesome-design-md
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/5673" target="_blank">📅 19:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نانوبنانا پرو رایگان می‌خوای؟
بفرمایید اینم یه ابزار خفن از گوگل:
https://labs.google/fx/tools/flow
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/5669" target="_blank">📅 17:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مخابرات و همراه اول وصل
Windscribe
TCP, 443, Paris Seine
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/archivetell/5667" target="_blank">📅 17:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5666">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">اکسپرس برلین آلمان سوپر وصله</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/5666" target="_blank">📅 17:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EtNggBCIB_e72MZpwZBnOauSO7T1ka60hOFTGLPEekoCN3FBDyqYVc4rDs2UBZfAyNMgLeRNO8TadBN-FIIVd0rpUeaIdWl3MzFfzK5iakXjjRWT3xvkxfcTNRzNO0Wsj3dh40xPzICjp92d32TzUtX0ac7mehZDL7_aZpku4oKSPA673qsJMtwUrE-2_pCsen3TgbJWOyUOXNnf8hGZIe3jQ9hPj1UYWSWWpW010dN3TusvJ1f9sjZuaK5F3It_lGn9s_uljzHAumhWqDDEXW_ZOs3Iou7U3q3w7Ycxu4bVnmx2jL295bD-l2ytz3FL9q4-JdEah-x7JKGUMs-xRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IABYS_EzCogK62__a5J_3zr-cQZOyjawv_oMvkinOuLK-XGPvQ7AGe6k4edWisCYOXHm4iDx6JkM3H1ouCTsLu1Oq7YHY0VQ0B2ep33TU00lULgOlx1vB_mNacWT9xmllqoVKsN23GwlsyO0X9nolBq6W2r1PqGi2e0uzMT__eh4TEWBM47mCrb3W-lvi2CxSx_dDycm2eqoXXk4V2ErZyKPI8OIEgGZ2rwy7c8fkpvgZxoaAiicNKrZmTeSr9YiRJjQgJI8Fa8ZyuWE35dlOmvneujLA5NA8B8yCLIhkBuHj9Mt-T1HlTxGiwu1OvXcHCBJgHCjbY4TrlsA4t3zqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHxnSxg7KUcR7_PQaCVYOgf478Cu1ZG-npka-I2SjIzVuQIzL-sk4_aDz9KGmg-5xtMmNxGTaEU_SH7RBgBVLVChgwbXxCPrDdgCNhf9sZWLNmGNAR01S9TuW8A9LBx5jj9xbDPK4qUqLH2G62GRCz8KcR0eMP9UPkudCJehKPsakbq-IuPfHXEfMWyCeklxVR8RV19tPuS6U9qFlO1Cu9GBFPnW20GD8t5SXuVlOxICdIX7b27dcCTv3RG1SaH3toiiIRc5dH6qkP5EwbOza3Yy-2iLxeS-H0SoB0xyHzd3AmBrIubHnaMhpyFl41kwKALCgNZjVpxLz_kY-q97Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر هنوز دسترسی به اینترنت جهانی براتون باز نشده و مجبورید از DNS Tunelling استفاده کنید:
با قابلیت جدید DNS Pool دیگه نیازی نیست دستی دنبال DNS بگردید یا اسکن کنید. می‌تونید تا ۱۰۰۰ تا DNS به برنامه بدید تا خودش قبل اتصال تستشون کنه و ۱۰ تا از بهترین‌ها رو خودکار براتون انتخاب کنه.
🕊
@slipnet_app</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/5663" target="_blank">📅 17:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5662">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مسئله فقط اینترنت نبود
ما را از جهان در حال حرکت جا گذاشتند
صدا ها خاموش شد ، آدم ها فراموش شدند
و گل هایمان یکی یکی پر پر شدند
زخم این دوران هیچ وقت از دل ما پاک نمی شود..
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/archivetell/5662" target="_blank">📅 16:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">برای گرفتن 15 گیگ برای اکانت ویندتون باید اول ایمیلتون رو تایید کنین با اینکار 10 گیگ بهتون میده
🆓
برای 5 گیگ اضافه باید توی سایتش لاگین کنید Tweet 4 Data این گزینه رو پیدا کنین یه توییت بزنین براش منشن کنین و تمام 5 گیگ دیگه هم براتون فعال میشه
👑
👥
موقع ثبت نام، اینو بزنین ی گیگ اضافی هم به شما اضافه میشه
Declinedrice
⛈
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/archivetell/5661" target="_blank">📅 15:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-4SPLZV4UfW_o0V_ca33SFt2p70NAgNMe_wyZ9jCEluzxbdDxh1-Nz0T9IWErP_-WJRtfa2zL9W6FNI9fYrVx-sJqxnlsNSEENpWUsyyILjH90RA9B9OQDmZbyfRUhXYJJKrjlBGItz47KXFylMPUWZkwa1c9fiQ6aB2f2IOn8GI3dSC8wt2CxVcpUmOyrklW9yWH2KmtTwFg19gQ7KeNm762w8Xpe-rnfExK-Mv-ph-B0g5Srr4kQ3Lx_VplHZxrxWt8WKz7Mjvqw2gihhf-qDPGCEtEyK0VWck534FNChd3Il3_eK2R2TWbvpmp3VfGmdJKkz_Goa3n8PhynsGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nhEubznBsTAjs8DyK7tfuIV8c_vAAehs8d0fkttYXVoeCzfX5YNlwgDsDTn97FRm35qzv5hbBoUTd6U9-BFiEYevM_TPykwuXe62Eb6viJ0WnEI_YSQq1s_KNA2XDRBOzA4RQKBz3lNdwhhikf_ETIhtE89OgUnNMeM4StILSnGAg9eXfqfNeFGT8fRQ-yLZ4GwVpuclolNG4PdWUeTrscyJyrL-Yv0PopnRkqi9HA2SB2583PbezwV5Th6lkkvg32ILOpNDEFm12ypPwLMSn_w1Xb6r1NoIaluLxbWL7tD45A4EtKNNxdRfAOz8tGTc0Whn9Gp0ihGa2DL18ptR6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/archivetell/5659" target="_blank">📅 14:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🛠
معرفی جعبه‌ابزار قدرتمند cfray: همه‌چیز برای VLESS و Cloudflare در یک فایل!  ---  رفقا سلام!
✋
امروز یک ابزار پایتونیِ به شدت کاربردی و جذاب به اسم cfray (ساخته‌شده توسط تیم SamNet) رو بهتون معرفی می‌کنیم.  این ابزار که قبلاً فقط یک اسکنر کانفیگ بود، حالا…</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/5658" target="_blank">📅 14:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/5657" target="_blank">📅 14:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ac73908c6d.mp4?token=rHyJmytMPWEdLCBptJ5lV8mTVek0Dvb3dv9ViHuokOfDHfCjEuGgUD8s-LCpLZucN1wlS5Fbv4RRJ215xV_W-Omk3fNL5NjpsFe9xwqWpDuwXALVw2W8L0ul2OHmKM0z_N_vH2xE_T60PHyxJ6YPNZhYy576tlKdKwO8ZoHFtzYIrN1RdSwYVRlswJ7rk5kgwTPyu5m7oE-Sg5RqpU8I0rJSX6hIDhkN3SK4YoIJM605vurY8bLao6FkoEGFe7bzJwr1hmdK-9xtHBl9rbcYmr10jc9sTUCuRpvMkCO3iBWa5-tuz-QzHOT5QKyTDAaZ7dq56gPqtIL7f8W8UMzEUA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ac73908c6d.mp4?token=rHyJmytMPWEdLCBptJ5lV8mTVek0Dvb3dv9ViHuokOfDHfCjEuGgUD8s-LCpLZucN1wlS5Fbv4RRJ215xV_W-Omk3fNL5NjpsFe9xwqWpDuwXALVw2W8L0ul2OHmKM0z_N_vH2xE_T60PHyxJ6YPNZhYy576tlKdKwO8ZoHFtzYIrN1RdSwYVRlswJ7rk5kgwTPyu5m7oE-Sg5RqpU8I0rJSX6hIDhkN3SK4YoIJM605vurY8bLao6FkoEGFe7bzJwr1hmdK-9xtHBl9rbcYmr10jc9sTUCuRpvMkCO3iBWa5-tuz-QzHOT5QKyTDAaZ7dq56gPqtIL7f8W8UMzEUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧠
در GitHub پلاگینی به نام agentmemory محبوب شده است که به عوامل هوش مصنوعی حافظه «بی‌نهایت» اضافه می‌کند — این پلاگین تمام زمینه‌های جلسات، اقدامات و پروژه‌های شما را در یک پایگاه ذخیره می‌کند.
• به ۱۶ عامل هوش مصنوعی از جمله Claude Code، Codex و Cursor متصل می‌شود.
• تمام اقدامات آن‌ها را ذخیره می‌کند، به خاطرات فشرده تبدیل می‌کند و به‌طور خودکار در آینده آن‌ها را پیدا می‌کند.
• دیگر نیازی نیست هر بار زمینه را توضیح دهید — عامل همه جزئیات را به خاطر می‌سپارد.
در نتیجه، می‌توان تا ۹۵٪ از توکن‌هایی که معمولاً برای توضیح زمینه صرف می‌شوند را در هر جلسه صرفه‌جویی کرد.
https://github.com/rohitg00/agentmemory
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/archivetell/5651" target="_blank">📅 09:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کانفیگ اهدایی
تشکر از
@thee_LaShi
بابت این کانفیگای ناب
❤️
vless://9bc46020-c550-439a-86c5-38f64abc1ffd@tr-in.api.dznn.net:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=9F7JxyyP-TNLt0dY2xOB0_34I8W0xXIpFY7rZ7-L0Gg&security=reality&sid=19aa22f681923dc8&sni=tr-in.api.dznn.net&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/archivetell/5650" target="_blank">📅 08:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کانفیگ اهدایی
vless://9bc46020-c550-439a-86c5-38f64abc1ffd@ninka.api.dznn.net:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=9F7JxyyP-TNLt0dY2xOB0_34I8W0xXIpFY7rZ7-L0Gg&security=reality&sid=19aa22f681923dc8&sni=ninka.api.dznn.net&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/5649" target="_blank">📅 08:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فیلترچی ری اکشن فیک بزن تا بسوزی
😁</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/5648" target="_blank">📅 08:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5647">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پخش کنید بقیه هم وصل بشن
😁</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/5647" target="_blank">📅 08:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کانفیگ اهدایی
vless://9bc46020-c550-439a-86c5-38f64abc1ffd@tr-in.api.dznn.net:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=9F7JxyyP-TNLt0dY2xOB0_34I8W0xXIpFY7rZ7-L0Gg&security=reality&sid=19aa22f681923dc8&sni=tr-in.api.dznn.net&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/archivetell/5646" target="_blank">📅 08:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5645">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کانفیگ اهدایی
vless://0468a043-e12c-466e-881c-7d685c1b3950@roz1r.skystreamgame.com:8443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QHkXBS2ENHV0khgY9VBYi8_9bpfqnUYDcfQN4cW5Qg0&security=reality&sid=4326&sni=roz1r.skystreamgame.com&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/archivetell/5645" target="_blank">📅 08:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کانفیگ اهدایی یکی از ممبرای عزیز
vless://9bc46020-c550-439a-86c5-38f64abc1ffd@fishsea.api.dznn.net:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=9F7JxyyP-TNLt0dY2xOB0_34I8W0xXIpFY7rZ7-L0Gg&security=reality&sid=0a6ba2716a409da6&sni=fishsea.api.dznn.net&type=tcp#@archivetell
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/archivetell/5644" target="_blank">📅 08:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کانفیگ اهدایی یکی از ممبرای عزیز
vless://9bc46020-c550-439a-86c5-38f64abc1ffd@fishsea.api.dznn.net:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=9F7JxyyP-TNLt0dY2xOB0_34I8W0xXIpFY7rZ7-L0Gg&security=reality&sid=0a6ba2716a409da6&sni=fishsea.api.dznn.net&type=tcp#@archivetell
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/archivetell/5643" target="_blank">📅 08:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/archivetell/5642" target="_blank">📅 02:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5641">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/archivetell/5641" target="_blank">📅 02:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/archivetell/5638" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/b370928a6c.mp4?token=HL1qiLwb74U3WtteKFks9NCd-63mvs_2uxXp-AUqQZPUflMy-PvxUqdjf7_0W71vM4TJYR4zTc4LFIHNFapv7ZpqOHIogrQlQSliNP8YxXWDfeSAcoNdOrRNmXlZ7D8rErhpGQZNuhqkWaFzfQ2K-t4nQCvV3ExOMSZBPec_EPGNH3SO7k4CyzXKtRZgkNPK24PJ1hCAazGfV1vy9VNKJKSC0z62z18qzNH36DlR0xHhhQH2RCpBjfM4wkk0iiHkWdWiHsqVLJO4WS1cCxm4TcKZYt0vqMrJ1_0YiImtxRbvSFKe4I0JAAXRUzXi4jobGVV6rY-D01mytWQqrug4Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/b370928a6c.mp4?token=HL1qiLwb74U3WtteKFks9NCd-63mvs_2uxXp-AUqQZPUflMy-PvxUqdjf7_0W71vM4TJYR4zTc4LFIHNFapv7ZpqOHIogrQlQSliNP8YxXWDfeSAcoNdOrRNmXlZ7D8rErhpGQZNuhqkWaFzfQ2K-t4nQCvV3ExOMSZBPec_EPGNH3SO7k4CyzXKtRZgkNPK24PJ1hCAazGfV1vy9VNKJKSC0z62z18qzNH36DlR0xHhhQH2RCpBjfM4wkk0iiHkWdWiHsqVLJO4WS1cCxm4TcKZYt0vqMrJ1_0YiImtxRbvSFKe4I0JAAXRUzXi4jobGVV6rY-D01mytWQqrug4Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/archivetell/5637" target="_blank">📅 00:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گوگل پلی رفع فیلتر شده..</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/archivetell/5636" target="_blank">📅 23:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گوگل پلی رفع فیلتر شده..</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/archivetell/5635" target="_blank">📅 23:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ربات جدید تبدیل لینک به فایل
@url_uploder_nrbot
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/archivetell/5634" target="_blank">📅 23:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12fb4063f0.mp4?token=IASTqfWyKbYJL16hZbGcukbWsB0pLc96-4tvTC2cRJb7ygpWPHXQOcBdhFxMbyPwTv9RtnBc1Swp1uavC4egyAR2GHMs3pYc_3Olnp_CPZc2NitsCPw1rk0KpTPN73OGCVL-vlzbqEBA2YT0aKsdu4ntJ2Xf7To3bW6_tjJ4FrfBycCUHW-x5sK3rHC5RND3_gb3-NKOn00Zcw51SFzEtUAelUt8T8bZN7EaiiVCoTjQr0jhvXNkjk-clj1iYxBMVgFbeeemL_ecn5ql2lmnsp8qWZTSQtGcTHzvudD6jMFm_-9Pk17_qfDVfGNbpPx5vsHuLGFdvyezle9z_QJp3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12fb4063f0.mp4?token=IASTqfWyKbYJL16hZbGcukbWsB0pLc96-4tvTC2cRJb7ygpWPHXQOcBdhFxMbyPwTv9RtnBc1Swp1uavC4egyAR2GHMs3pYc_3Olnp_CPZc2NitsCPw1rk0KpTPN73OGCVL-vlzbqEBA2YT0aKsdu4ntJ2Xf7To3bW6_tjJ4FrfBycCUHW-x5sK3rHC5RND3_gb3-NKOn00Zcw51SFzEtUAelUt8T8bZN7EaiiVCoTjQr0jhvXNkjk-clj1iYxBMVgFbeeemL_ecn5ql2lmnsp8qWZTSQtGcTHzvudD6jMFm_-9Pk17_qfDVfGNbpPx5vsHuLGFdvyezle9z_QJp3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک مجموعه برتر از انیمیشن‌های رابط کاربری وب برای طراحان رابط کاربری که تمایلی به صرف زمان در ایجاد انیمیشن‌ها از پایه ندارند
https://transitions.dev/
این مجموعه شامل انیمیشن‌های آماده‌ای برای کارت‌ها، منوها، فهرست‌ها و کلیدهای تغییر وضعیت می‌باشد.
امکان بررسی مستقیم انیمیشن‌ها در وب‌سایت پیش از بهره‌برداری فراهم است.
ادغام در پروژه‌های فرانت‌اند واقعی به سادگی امکان‌پذیر است.
پشتیبانی از ادغام به عنوان یک قابلیت برای عوامل هوش مصنوعی ارائه می‌گردد.
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/archivetell/5633" target="_blank">📅 22:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/121da40c06.mp4?token=NEe-VstTyVV2L1JVGlXWwR2lStbv1JYfzTESZaoGr29rodpbcMPcOqxnTPv2JUBs9oaSG-HhhIGbbulpXJflj7zXbkj00tZJ9HV5a1seJdnnbC9d-4rEHag-ZqP3mCbSe59pi-83BDOJmhnUUdcwNYXz6odhiZo1VqbX_MGp-uYfLOWrKrAur5-7wCeO0BfDEPpOiZbNLqZemE-x1VvFmKjJMOQQEun8rB8q4lQ10wC2XEzJRJPMK0ze8sdY4otEUppkpxCQ2m0wRut-4dkqAAh3M9oEmUCCUkfsOZO7ROS24qX-hJWK0LdtNSTfaAlrEBIGHyE4JECrjLJU7orOEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/121da40c06.mp4?token=NEe-VstTyVV2L1JVGlXWwR2lStbv1JYfzTESZaoGr29rodpbcMPcOqxnTPv2JUBs9oaSG-HhhIGbbulpXJflj7zXbkj00tZJ9HV5a1seJdnnbC9d-4rEHag-ZqP3mCbSe59pi-83BDOJmhnUUdcwNYXz6odhiZo1VqbX_MGp-uYfLOWrKrAur5-7wCeO0BfDEPpOiZbNLqZemE-x1VvFmKjJMOQQEun8rB8q4lQ10wC2XEzJRJPMK0ze8sdY4otEUppkpxCQ2m0wRut-4dkqAAh3M9oEmUCCUkfsOZO7ROS24qX-hJWK0LdtNSTfaAlrEBIGHyE4JECrjLJU7orOEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/archivetell/5632" target="_blank">📅 22:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کانفیگ پرسرعت
ایپی استاتیک کره شمالی
جهت سفارش پی‌وی
🐱</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/archivetell/5631" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/archivetell/5630" target="_blank">📅 20:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/archivetell/5629" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">600 گیگ کانفیگ مستقیم متصل همه نتا
اهدایی یکی از ممبرای عزیز
❤️
vless://22768339-9096-48aa-9109-ff28141145b9@roz2r.skystreamgame.com:8443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=QHkXBS2ENHV0khgY9VBYi8_9bpfqnUYDcfQN4cW5Qg0&security=reality&sid=4326&sni=roz2r.skystreamgame.com&type=tcp#Aqa.rza
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/archivetell/5628" target="_blank">📅 19:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">kiro.dev
یک ابزار کدنویسی هوش مصنوعی از AWS که فقط کد نمی‌نویسد.
این ابزار کل پروژه شما را از صفر برنامه‌ریزی، طراحی و می‌سازد.
⚡
Free trial with 500 credits
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/archivetell/5627" target="_blank">📅 19:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آیپی تمیز کلودفلر، تست شده روی ایرانسل 104.16.81.122 104.16.81.43 104.16.81.86 104.16.81.12 104.16.81.24 104.16.81.125 104.16.81.40 104.16.81.133 104.16.81.68 104.16.81.101 104.16.81.23 104.16.81.155 104.16.81.112 104.16.81.106 104.16.81.67 104.16.81.82 104.16.81.157…</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/archivetell/5625" target="_blank">📅 18:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">Defyx VPN  رایتل سرعت بالا  https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn  @ArchiveTell</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/archivetell/5624" target="_blank">📅 18:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/5623" target="_blank">📅 18:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/5622" target="_blank">📅 18:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">#اختصاصی
🌐
دامنه‌های رایگان برای هر پروژه‌ای
https://github.com/DigitalPlatDev/FreeDomain
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/archivetell/5621" target="_blank">📅 18:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ua8DlO613BTbMVeCw4QaPpYal9LJBY2H-Bjs3XuxHvMNsDIXYitGdu0J4Dcj33DaS_cURXJKe4jwS_HhNUltEhPSwknmSJ5chmNxEhAJekGAOi6ZCfzTwpFUeXc3KixmVhCEjO0P_BvMTojFZhi3kl-QyVf6nvmni3PLKZ62A5MMNLLfh3yo-qxpK6b2xbgM8v6LmUoxpR4WgS-5vKYGg5_T9zMBnHyJoFnO2I13EuFJ7KxkNtXWo51NgF2rqTzIHjIzlyfYjA_asXrlUKc7TbQi1vSa4zGUjo1Hg8TjPxzj8FgT1wtfOw2exRYWkHgGs9EgKSgyNoNYoIq4q4Ip2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Defyx VPN  رایتل سرعت بالا  https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn  @ArchiveTell</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/archivetell/5620" target="_blank">📅 17:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">Defyx VPN
رایتل سرعت بالا
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/archivetell/5619" target="_blank">📅 17:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5618">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/archivetell/5618" target="_blank">📅 16:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5617">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cP-x1a5JsX__9gbQpPhRcYuTSBTo7pbsCYbQ8jLYi3-UjbM3o4iDLYM2xvHtyryYRM9lpGrhP3-ZmzuU4HmHFxcG-Mafi4eHbkGgtul7lZYxZA0ZB4V50s_J9JOwXTqrxUDSkui43u8TGMk53golcnzBqqJTK8RbJ-KzENsNnOM7MD77Yojm-aalSs8d4bKcjzrlJvtKR6OaZ-t6D3fBYpUgkVXeU0JmnKfBoeZYEHrDLeNR2T8EbmnKY0myfFlIb7BG_gHCquVH3nOGTzjhWkuUacI3NkByI_76u66OIGG3HtJCrWQTflSG1u-tV3Qi8Nj7Ra_IVuP0paDe-IJjLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان میتونین با Hiddify روی سرور های رایگانش وصل بشید یا از گیت هاب بگردین دنبال ساب بندازین داخلش
👋
**میتونین داخل Github هم بگردین ساب های مختلف و وارد اپ کنین و تست بگیرید
👍
لینک دانلود داخلی Hiddify
👋
💀
@archivetell</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/archivetell/5617" target="_blank">📅 16:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مقایسه سرور ها و خرید سرور مناسب و اقتصادی
جهت راه اندازی کانفیگ
https://t.me/archivetell/5282
https://t.me/archivetell/5308
https://t.me/archivetell/5309
https://t.me/archivetell/5310</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/archivetell/5616" target="_blank">📅 15:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uADKu438IexKhjcIi52sgymQaqjdvWqOpHsIpe_6csUmRXZPrImvcYfzHNB0pDH_5_S0hRNlgYMtREzCUntyzadBqa0purD6rrtpOtlzemJqiNUHlQ7MYeTzz7KQ9p5QsIJxiXMzfvM44VEIANRJC0Aga2eloYqSYA9yLfeYJawaKfrbCCtrXdoqyEpx3HvHFJ60dT1TF95ii4TJeVYN_e2fU75Sqb-1r34x3v76WQLRF_dYWumK7vCD1uAzqjiDQUaB5E1oAhLGKtscR0Z-yVNfgP7h_D6da-7wGrne0jeZAzEF00mUTPb8Cubq7-sfuLlGIG-U53brqvghvHOm4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">162.159.192.1
162.159.193.3
162.159.195.1
برای وارپ وایرگارد با این آیپی وصل شدم.
پینگ می ده، لوکیش ایران می زنه
😂
ولی تلگرامم الا بالاس دارم باهاش پیام می دم.</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/archivetell/5615" target="_blank">📅 13:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">در کل این اپلیکیشن D-Tools خیلی خوبه ولی حیف توسعه داده نمی شه، وگرنه یه اسکنر Google CDN و Cloudflare CDN و Fastly CDN می‌آورد خیلی خوب می شد.</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/archivetell/5613" target="_blank">📅 13:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">در کل این اپلیکیشن D-Tools خیلی خوبه ولی حیف توسعه داده نمی شه، وگرنه یه اسکنر Google CDN و Cloudflare CDN و Fastly CDN می‌آورد خیلی خوب می شد.</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/archivetell/5612" target="_blank">📅 13:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu6qjcIqp47tBE-6XwNziihFCV01_F_mvPSGzYXgv-ByMdwBhkrQ6IJ4qf7bo6NFHyZYeVILbEZwvGG3uBJKTB0yzECBRJ4BxNFV0SzOKqr96vbB2EIUVUxzIhXsULDTk2Oyo1QtE7EURcVZZ5OjYf-CVfIK7lCBoji9UD_F2Ac9E4Aes5y_4-8lx3MPV-1K4gNGlAALw2bRlbg299IkW9qVTOZzqhTDJnITAsKOHLXcvjB-CwY7OyYErJgVzf9EWxTw9LEjcBhvD4BtUGTwD0f2tTUvunTT5LvzZgfCrAhgR8QfSugwx2gq_MgiMnRBiolAaBk121x9gz0rLM2Uxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ساختن وارپ به این نیاز نیستا.  کانتریبیوتر v2ray، یک ریپو داره به اسم D-Tools. اپلیکیشن از پلی استور حذف شده ولی توی اینترنت پیدا می شه به شکل xapk. بدون سرور مجازی براتون کانفیگ warp می سازه.  {   "local_address": [     "172.16.0.2/32",     "2606:47…</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/archivetell/5611" target="_blank">📅 13:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/archivetell/5610" target="_blank">📅 13:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_JOd5LnMzqiN4zkFUObujEgdtSKtVXr8GJPhIA9saokDqBhSFmySW5cysG6WoI8PRl95rMuyNr_yNUglNjdQ-JXpGvEm7boywgGfSzGEdhJZnUiLdcNlaJ-n4FRZYjt3OMgZSd8xaBq4tj_1enIHGfRnMb_QIDSgYl9lIv8hIHMEX5KGwHzGecIR7MiVsBPB0QQrhkGSkzQnx2UryYmGJbD1OIl6-JfLbYueN-aGwzL08HXd9wr0P8swH3HQX7N8XI3z9rs3NJJ023mOhPRP5ayQ6soiLJANPam-1OMkdj3yfHf7lLDk4cx-hcqBFbh8NabW60pNC8BOl3mvaiDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش ساخت کانفیگ وارپ (نیاز به سرور مجازی )  با استفاده از الگوهای زیر، کانفیگ اختصاصی خودتون رو بسازید :  کانفیگ‌های خام:  warp://licence@ip:port/?ifp=40-80&ifps=50-100&ifpd=2-4&ifpm=m4  warp://licences@ip:port/?ifp=30-60&ifps=50-100&ifpd=3-6&ifpm=m6 برای…</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/archivetell/5608" target="_blank">📅 13:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🌐
بات تست رایگان بدون رفرال (خرید نزنید)
@Cheap_v2ray_bot</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/archivetell/5607" target="_blank">📅 13:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/archivetell/5606" target="_blank">📅 12:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">همراه اول
Windscribe UDP 443 Censorship On Dallas BBQ
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/archivetell/5605" target="_blank">📅 12:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کسایی که سرور دارن.
اینباند:
Vless+xhttp+tls+Cloudflare clean ip
بزنین با آی‌پی تمیز کلادفلیر
عالی وصله‌
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/archivetell/5604" target="_blank">📅 12:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">همراه اول
Windscribe UDP 443 Censorship On Atlanta Peachtree
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/archivetell/5603" target="_blank">📅 12:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">و اینکه، نرم افزار Karing گزینه وارپش کار می کنه و پینگ داره و کار می‌کنه.
😊
@archivetell</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/archivetell/5602" target="_blank">📅 12:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">واقعا باورم نمی شه مردم چقدر می تونن عقده ای بشن.
📘
مگه ما فروشنده ها چیکارتون کردیم؟
😭
طرف با کانفیگ رایگان بعد ۹۰ روز وصل شده زنگ می زنه مسخره کنه. چه رویی دارین خدایی.
حالا من به وصل شدنشون می گم وصل، طرف فقط می تونه با کانفیگش پینگ بگیره
🤡
😊
@archivetell</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/archivetell/5601" target="_blank">📅 12:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">لینک داخلی
Am tunnle
(pro)
Am tunnle
(lite)
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/archivetell/5600" target="_blank">📅 11:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">AM TUNNEL
سرور ۱۶ fast dns روی ایرانسل و همراه اول سرعتش خیلی بالاست
https://play.google.com/store/apps/details?id=app.vpn.amtunnelpro
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/archivetell/5598" target="_blank">📅 11:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEQ38B2YSMBaEYXWRG7vU_HvFxuENSlTC8nPJBa5NksbBHoOJEuKo4khFC7O--_ZiO0toSGerUq3jW6GIi5wSY-ypEhI_knwE6QHOifm9rZplSGJls9QiWzFjXuOPKrHDZHkyy33jwknyfU17a2GbDzLX0vvfz7f3aQdpPm5Q_WrnhraH4lEyKcTBA7OWmeTCnrUWvQsQfz_hc5stD1UWIwggUmYHhX47jq3rDqV9w7ybTW2acyMd9Xh8YyPpaGBHaf5ElxmXZ4wrOnMOxna2kroTqp_3bNK8jEDBAAXF6ke8vTE65DO41c9RtcS9CtXa313VgVyn4VROORJi6rTNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Optimize-Windows
اسکریپت‌های بهینه‌سازی و ساده‌سازی نصب ویندوز
https://github.com/ShivamXD6/Optimize-Windows
@ArchiveTell</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/archivetell/5597" target="_blank">📅 10:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcxBZqP7FN024eGD4hInMlHgEueq9Wopd95oqba4fsxtVszz8LhAK7FuI2TOg3R2G_HGt3gQwjrqiQZTfXLyr4CI9wGDhju7zUa0w3kMl1BI6WZ66GovqnbRjSJ_QRs29mgjJfuRmyzUBXtGPm6P_w63zMubi1mCxNILiUD9T8Jw0CRravfcP2vkTzbfuR6s3-3WucaWfMaP7I6jVfCe19s8CBXjYuLMmEAuTNM0fiRtOgh5hslEt72hX_PKH6nn4na9rtN1A9m8RYksGf8YxjeArDiQ6I5NEqWPP2Mq8Buv5P6vYh3rO0ObTETwIvZV-08G9zjOrxo0WE1ZcIMFxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hYgn9Xkd6BhY0VcC644evdOXKNyTQRGX76d6bkZjYSIFTLKqRgI4H0NyvXgoxPp6wsRleOPlgqc7wSwjnDY0WMdKxyLzPOpE7ZxpQQsVqmG_2-JYJdONrC60vE2ugHLa-Uvz3aVymB6wIVNUllIhi0VEV9X2Gs7r9b687p5ckrFZsjhi48yNJTnHevPhIiLQ_l6l7GPgFIzo5I0GhsbNI5teSuOcz5Kh2aWKyNgE8I36gMWPlvzyhCydwi3tpqPtfSlAa7YGlUN0lXCv_CMUSsuAOqIs2MBLcXFG-eQJjOs3FeiUWIxtGhpDbYRUyunYaAz3-KUHSPyFllB0cjFn3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V84wnPtpATmEskma-ejy7VBDPHD3VxMf6Aj8F9CAjKVr7oEv3lg0yhFXAXVpEpVH_hrxudYDSTNVrUuyAPHOrMNt0jnwOkHPp2410m63J5pVx86jAp9vsnvfhd_hXa8pW_dQipEI_bDZNrCyhq_64onfxnZpk7y_EZBQ4ylqZ5zQ2UFaWWaOFGlbCcLWxM3sZnH-VUx-v9A3LfZADL54YLwFOoHCaIkR8wWCFAFhF9gnaoDQDN1W_0n7PRJ0DDJ1_OUOyPPFK-09q-VzwM_-6P1uZJdHScfT2kMnQIpV-K0mlX44elavQfT94YajDiTzIDinmOgenvKxslXI-P9LOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnIM9lcIZ37UAYPv7ujxCTIal9pH7OCwjGWUhZiMkqxYf-JxS0rxkLKv2pICd4VSsHfoKeS6B1HdPuH8TC-fgscpRRK6Y0HkqMF-ojN4w9C1zY2YbnyV_GcvXqxQaP1lnEFew6VRR3KSUGh0oJ53OJg--P9O2FYhIv5Mf8MufXOgKR3rCLCZ-mz75X7QdQHaA4YuJO_pj6PSBONSav99U85vlA7MJROcPUm0kLkh3KxiHvToDbDK-GAkRONFrH72zabnvSTjKNTmJx5MIkQA7qm80vXa29VqY8-zxDFm5rlk5PskkdueMGPnPRFYurBntM442amKWUV-oLbON7EXbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rKd6s6qfPCH9YdKPMq3nclLf3TI0Jo1653M6bR11cXdz9M4Bcot4LzKmOxvgfoyZ09dnH7xu2Wrn3RfF3pNde7sgM80ZnSqp6p6HZ1haktUJ9ZJRoXVMXLfIr2sMTAO6V71WtRvyU8yigRjhWu0z4MR5yHQRxjooq3jZKQU2snWocf96rToNkFGSA3eeY_d6-KHC7oH-315Yza4n1VtyK_tZg5vBAjva5IEzfdhdi7_7g_aPkvlU9C1Ff53aLuXiLTevk7T5nafoEAX5BCsPKU6-64aUqEcvjU7L8IzoK6QhotyIr0WbXsVeE7AF1Me_AMl9lTgxijtU1cuQy0RU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTtjc_CkhS1N26TOQQrruqRLtorKuk3hF65GfBhLJvueS96T96T3WJeCAeGpeaIQh-7B0zwW0jvQen6UDSF2EcHIm15-nPE3WDIM-pIZAjjsakXB9iaAZCdHymMngSolBfguzCsq61fWjrXRsJpILpNc1w4i9aRs2HZQpIV3hEXOGR9PDvhKCxP3-VOsMgEIJwp9Vrz1E6blIS6tZiAdt428QafaSEFi7CfEIhlbyEv55vN-5qbm92YmcJNETOcZYzUUyqZj4DWQ4Im4uO5szzXYyQjYFUjWSPKwnEKYkP1ChgLZL6SDR5gW9YNT-s00MQC7DeV8t1RP-JhIav26MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ltnbJ0l3CP1mQPCe0hphjEK4IewYVvVK8VmJ70i-DNQkuK_3YPWF98JjyeSd4izI-vIqG4Xn3WoPfpgcje6iCJUqdLB72OIBJa8RKWIrtymanGpdsLi9mNBsBz98BgmRVwvfRgbjKeMeQSfw_oNj__uFIYNoiNIxg8b-ZxzEHCIcj5R5nRxfZk8g5i1Z_IoAzsZ-quNdJeNTC148X09XrZI2b28CTAuudwMMr9uHMSEf8p0PFjEvCPorp1ozYDIzJaUQRyC2xjtwsKejVwMmXwNp6eHnSL7XSpGt2ZUoGJvlHZdjrFNRdYD8VI89HKSJQ5eiTOP2p4hEG6qBXy9ktQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ربات دریافت پل تور
@GetBridgesBot
پل webtunnel سامانتل و ایرانسل وصله
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/archivetell/5590" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Invizible_Pro__beta_ver.2.6.9.apk</div>
  <div class="tg-doc-extra">38.1 MB</div>
</div>
<a href="https://t.me/archivetell/5588" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">InviZible Pro beta 2.6.9
* Updated Tor to version 4.9.8.</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/5588" target="_blank">📅 10:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQbUc3ypxCrCR0mW_rQwilw-GcfwFbReppv1mW531jO_t5UBJCJxUTglIsU1PIrEdQz-q6MDU7GuWdCzbPou7j6ZWshMFzlJUOJlwKYcpDQMXLU_UXLnez2fxOYGDVDVFou9Ky_B5eeQ2yHQYYE07bx76mNmd5e3N7L7z2c3Iec5csBQQlg7nLCdDXvf4yixFTztZpZuPYYdLiAN8R1_u0AyAb1b5mn78xk4FzKIvY0QOaSRYmpfUJzBPNCLLl5mwvD0efiYwSycmPaNDyArVLhhTmH_Xtj9kLrbYVVZrz3pwvrrbBVR6V4Vz8yoI7MQwphAVxuMqsJdZNtH0C-xkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش invizible pro به زودی..</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/archivetell/5587" target="_blank">📅 09:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">MetaMask یا Trust Wallet?
🤔
👇</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/5586" target="_blank">📅 09:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">BD NET VPN
مخابرات، متصل
سرور BCCF 01
@ArchiveTell
https://play.google.com/store/apps/details?id=dastan.prince.bdfreevpn&hl=en-US</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/archivetell/5585" target="_blank">📅 09:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شیر و خورشید بدون آیپی
مخابرات ، همراه اول و ایرانسل وصله
تنظیمات رو به حالت اولیه برگردون ( کلیر دیتا ) و پروتکل رو بذار رو CDN ، متصل میشی ( کمی صبر نیازه )
﻿
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/archivetell/5584" target="_blank">📅 09:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آیپی تمیز کلودفلر سامانتل
208.103.161.170
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/archivetell/5583" target="_blank">📅 08:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">📱
صد گیگ کانفیگ اوتلاین به همراه شادوساکس بهتون میده
✅
( پروکسی ام میتونین انتخاب کنین )
@OutlineKeysRobot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/archivetell/5582" target="_blank">📅 05:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کلا tor برای وبگردیه فقط، هیچکدوم سرعت خاصی ندارن.  وقتی وصل شدین برین یکم تو این سایت وبگردی کنین
😊
https://tor.taxi/
اونایی که می دونن
🔫
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/archivetell/5578" target="_blank">📅 02:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDFqNtx4Jasm_YJf5BC4_Q-iSwDTiG-EFSH59iMEJYLYxBz69fG2p899LVauIoh1nDUE1GHrmYEXJq0I2OMmbrg0HocRQKYRVPydW1da3511CmmrrJRtL9e4Fkd4SgZ_TguqXNN1wOU3IhT5BVx6uflg8gbbK44FKHMw3NTF_wVBCTXQouxthHF5oC_MGs9jWL3OvAv1bxt_w9k13eB0ELqygd-NLGwyynroy2uUlL6wnP-xQrnCWewBlfa6C1DILuNyyTiWzs7oQUkvNj-z2kOyTcwYiqrQ3lT_1nIoxayadRUmcQD_mPqPbwzxOSB_XyivMsy617yXycGRy7bAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان کلا از نظر سرعت بخوایم مقایسه کنیم ظاهرا به ترتیب Obfs4/WebTunnel Meek Azure Snowflake اگه اشتباه نکنم</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/archivetell/5577" target="_blank">📅 02:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5576">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">octohide VPN
ایرانسل سرعت عالی
لینک گوگل پلی
از ربات
@octohide_bot
کد ۳ ماهشو بگیرین فعال کنین
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/archivetell/5576" target="_blank">📅 02:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🟢
نسخه جدید Argo VPN (اندروید)
🔺
بخش Network type رو روی Public Network قرار بدید و متصل بشید
اگه ارور داد یکبار برنامه رو ببندید و دوباره وارد بشید
https://dl.toolschi.com/view.php?f=ac33499153243a31.zip
(لینک دانلودداخلی)</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/archivetell/5575" target="_blank">📅 02:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کلا tor برای وبگردیه فقط، هیچکدوم سرعت خاصی ندارن.  وقتی وصل شدین برین یکم تو این سایت وبگردی کنین
😊
https://tor.taxi/
اونایی که می دونن
🔫
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/archivetell/5574" target="_blank">📅 02:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uV5nosy567f4CtYjxr26LTrFriFdpZ_BWeqngevIukr-dYkCg91qLjdR1Gjd8q_5gXzECzMamV2PtIve6km0EkBcgdaZFTQSsbEHwxNedRx87ZBAp4E_rTHNMMTLA8463yI7Htyn2VlD8_Ul3gqTpdfEkW88OitHeXuP6Y-bY0MaE4wpKfRsNlfykNQaXPPAjaUImLzFQWHg2CfCq2-8UcnbCxOm2YjOAlCF3GDVzp6t6hhJVtfUSz8lDY8JVMi6gdtjA59AkjrCenvAnS_JXDlhtcAgd4N6HGsnjirH6mWKM4U-6Q6_YP2eHwK5sFYz_q9lxacNByU6VqIzJYN56g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلا tor برای وبگردیه فقط، هیچکدوم سرعت خاصی ندارن.  وقتی وصل شدین برین یکم تو این سایت وبگردی کنین
😊
https://tor.taxi/
اونایی که می دونن
🔫
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/archivetell/5573" target="_blank">📅 02:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5572">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دوستان کلا از نظر سرعت بخوایم مقایسه کنیم ظاهرا به ترتیب Obfs4/WebTunnel Meek Azure Snowflake اگه اشتباه نکنم</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/archivetell/5572" target="_blank">📅 02:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دوستان کلا از نظر سرعت بخوایم مقایسه کنیم ظاهرا به ترتیب
Obfs4/WebTunnel
Meek Azure
Snowflake
اگه اشتباه نکنم</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/archivetell/5571" target="_blank">📅 00:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5570">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کلاینت های Exclave, SlipNet از ssh پشتیبانی میکنن
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/archivetell/5570" target="_blank">📅 00:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NzjnHDPQttfB0bue3wSTxIDwr3OpXBZD8VkwYJ1ad7g0NWHVDGtyg-7abp7ZYl_if89kk28BCp_6pHCeiYEmb9NtuhxyK4TCHeFDGB1ZDIOGlYg_XvvypljIamGpkPUQvtsJIwuQYjRMnQlAxb6qTRjUTz-IJA04s3ddxLVXxNfMQtqUwYIWCAOHPCv87G_R20P82K9YR_i2CSDoXFO14LASdb23LeYgGT0Wib_18w6a2VhRJjuGSbfDHHzDEWsvf5r4dPc9DcRd-99t-vPih2Z3igPcBAgcDU1rtm7ceDayPHaCScHqd1MeS7pakmUpcO7_h_f7w1NJX6d-gWzTSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxrS6CMktmFYby_BYeJOsmZT5ZWYMXnf8sIVOlC-85F4-5p-YO2LBemzl9T9G6yEtMAWIzaGDkveGP4jWSPE7o9djfwOvhkoIikfgOm2UG9teOTJ9hRb91BG4Uv7ibZwfpdtQyXohoAFtc9ZtnyoYb1d_hL_u1vJ9PS5tacGxo_H1tI5sg2X2q8JZodoxTdvvTqLmN_nB0Xlr36UztZIH-xDRlojRRV1HdalmIw50rfmjxHo9TtSm-nVc9-WVUz3AIKMq0pIi8f_LXlnOSAi57UqLdvYdaqFbm39mEAiDgukq6sQBloC76JBf3r82y-nYnM76ZM_Qp2o7tg1euEpNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QmTjiApJYiRaObJakQdNFWGXWstg6wgjPdEbrOhquACGIoSh0C2UFWV22hT37GEQu8eDZJnzk8rEW6rZJeHNLWp6VJQLI0_vT479hZj954NuLKWHbHftzhamB4FlBzNRluJO3ifm6M1ZFPifQYgdvCsLVD3DSdkEfh-jqxFp8SzKjdLshDKHmTyHSepl4nPJeuNqwy4xN7Rpe6dz_jUg8R18Hi2ML8McKXNjDkpoFCZmPCWSDnr4-20HZMlPiGeKM2FbhnUSq_rR8jbaqLzm519KM1p1_ieIXuYwtrS7F7qNqvB0FAGTZktr73uKJUaxJSKX1bxjEvA9ww6LHbEtyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bsYCgugeSovEwkHMjP_c_zEcuqxsNKf61vuekcguQbyksesY8BH74w9zU61RnYJcr-_xUNtNe82mEJCULlYf5L6SvdlVmjVIc4hrBMgQJ0jMrZbm4ySpoV2p-OrKDIsjoelKeVlcoGRFKVoPBQirnkuMHPJnZg1AiBVbHrLw8EdnqyuSnXOAqfLPSIUF2y4Cqt9mIX4Lss7aQDUMpizSb9i12PiIzlgR-3QgDZOiGA2B4RPOtS1GzB2WRrmuWZGEMA1fk1gjj1voxoIJS4_w1DnF-nWRoAbAY_u7bvg6UDsJ0fqBGaZFZ5TA852z3r_CbApGNvgPER0J-miv_m9t1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LizGCK1crToPasZAlaWhZ-SWOj_xr8DyHy-OJ8AMTrYg6J8vd0QszNXPQR3_SlPyqM1Vwqjfi7jnfezHekhxJTpH7bog8Yj-bBsP_dDFi5E5YxNfYScj2dvY3zLYU38uhC5OKVAZTYtnWLc9EHYJic7M4pyZ1L5zM7HOWMPtqNmgkQvsRJoFNMlGiIyTBzgBp5070HqoRSB4-e1d5CKwiKOlMabMklziq-E_d4FGyWU828buvEvDQc9dpnQd3lRaAcW6VcLhVpU4YsNq3keXrAfNdzXOpXGL0Ejvh8hnFUsnSAPoBc5GLIkew0wXBQFrR1ln-ymzuMXD7dNr-HVt4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vlLS69ORuZ-D_fM_ISwRW1WujyJHnEXRKB9MFl9dSxpM6ZhWyv1j2k6blbiv04t4t4PgdOV2oAduyJDEDqSU4edz4Gmsmftb6ufNx7XBxO-jJqPyT3m9F5gA76_PH802Ud4QrSfJAtLUltXWkPcRsB-IUkk-HwYlpBHllWf6s2HQx3TVUXIHKCAwlIPcitHEJWLY4df6YxFXdDXKnyBWrCWj-VLFY80CMDZ335vNTSCPZE_aBe0E2F92LZW4jyVu7WvMM3OKIml-N8agENjxCWxVzoUltkQpX889E0oHs96_f8cCNaIheVM0LIbMshPt9h_wPxqAuXyrkb4b_kppXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از بالا چپ به راست
اتصال Tor با برنامه اسلیپ نت
پل Obfs4
بقیه هم میتونید تست کنید
Snowflake, Meek Azure
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/archivetell/5564" target="_blank">📅 00:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پاکت هدیه
🎁</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/archivetell/5563" target="_blank">📅 00:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سوپرایز anonvector
❤️
🚀
آپدیت جدید و هوشمند کلاینت SlipNet (نسخه v2.5.5)
---
نسخه جدید اپلیکیشن
SlipNet
منتشر شد. توی این آپدیت، سازنده تمرکز اصلیش رو روی هوشمندسازیِ فرآیند اتصال و تنظیمات DNS گذاشته تا کانکشن‌ها خیلی سریع‌تر و پایدارتر بشن.
✨
مهم‌ترین قابلیت‌های این نسخه:
🔸
تنظیم خودکار شبکه (DNS Auto-Tune):
برنامه حالا می‌تونه به صورت کاملاً هوشمند، پارامترهای حساس مثل
Query Length
و
Rate Limit
رو بر اساس وضعیتِ فعلیِ اینترنت شما (برای کانفیگ‌های DNSTT، NoizDNS و VayDNS) تشخیص بده و موقع اتصال تنظیم کنه.
🔸
انتخاب خودکارِ بهترین دی‌ان‌اس (DNS Pool):
اگه این قابلیت رو از تنظیمات فعال کنید، برنامه قبل از هر اتصال لیست DNSها رو اسکن می‌کنه و ۱۰ تا از سریع‌ترین‌ها (با کمترین پینگ) رو برای کانفیگ شما ست می‌کنه. *(دو حالت اسکن سریع ۱۰ ثانیه‌ای و اسکن دقیق ۱۸ ثانیه‌ای هم داره).*
🔸
اسکنر و مدیریت پیشرفته DNS:
حالا می‌تونید آی‌پی‌های سالمی که اسکن کردید رو در قالب یک گروه یا استخر (Pool) ذخیره کنید و هر زمان که خواستید با یک دکمه فوراً لودشون کنید.
🔸
بهبودهای ظاهری و امنیتی (UI):
- منوی اضافه کردن کانفیگ جمع‌وجورتر شده.
- می‌تونید برای باز کردنِ باندل‌ها و قفل کردنِ پروفایل‌ها، پسوردهای کاملاً مجزا و مستقل تعیین کنید.
---
📥
دریافت آپدیت:
می‌تونید فایل نصبی این نسخه رو مستقیماً از لینک گیت‌هاب زیر (بخش Releases) دانلود و نصب کنید:
🔗
https://github.com/anonvector/SlipNet/releases/tag/v2.5.5
📌
#آپدیت
#SlipNet
#فیلترشکن
#اندروید
#DNS
#تونل
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/archivetell/5562" target="_blank">📅 23:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SlipNet-v2.5.5-full-release-arm64-v8a.apk</div>
  <div class="tg-doc-extra">25.7 MB</div>
</div>
<a href="https://t.me/archivetell/5554" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🕊
@SlipNet_app</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/5554" target="_blank">📅 23:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSlipNet</strong></div>
<div class="tg-text">v2.5.5 Changelog
🌐
DNS Pool (New)
•
Auto-Scan:
Automatically picks the top 10 lowest-latency resolvers at connect.
•
Verification Toggle:
Faster scans by default (10s timeout); optional full HTTP/SSH verification (18s timeout).
⚡️
DNS Auto-Tune (New)
• Auto-tunes query length and rate limits for DNSTT, NoizDNS, and VayDNS profiles at connect.
🔍
DNS Scanner
• Save working IPs as named pools and load them instantly via a new button.
🎨
UI Improvements
• Replaced the "add-profile" bottom sheet with a compact 3-column grid.
• Moved DNS section above Network in Settings.
• Independently set bundle-decrypt and per-profile lock passwords.
———————
✨
قابلیت‌های اصلی جدید این نسخه:
قابلیت Auto Tune: تشخیص و تنظیم خودکار و هوشمند پارامترهای Query Length و Rate Limit بر اساس وضعیت شبکه.
قابلیت DNS Pool (قابل فعال‌سازی در تنظیمات): اسکن خودکار و سریع لیست DNSها قبل از هر اتصال، و ست کردن بهترین و سریع‌ترین Resolver روی کانفیگ.
بهود رابط کاربری و رفع باگ
دانلود از گیت هاب:
https://github.com/anonvector/SlipNet/releases/tag/v2.5.5
🕊
@SlipNet_app</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/5553" target="_blank">📅 23:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkTuSL2QL3bqhUl6aizMskuQx6P70OfyNMm_ao4ib_DqRGLkqvmIgmLHJLleiGSJQ-z_NQu-sPdAqRT1RGxlPY3ThZF8MGvNyC2vCbCXx0APgVW3o-MoTgk4F1GenLs33ZMIFa5kNIb9Ekq4IINWwujz9UE8yIctAji2NlHxn67frXyBW9gY9FtezXDCHHzzyYqw_YhorqD954vxAXc1VU9PyMdFI22s2YkYF7KwhNIOGfDyzHdt5vJVOUowQ0_Of02OjmpGsmBuXBwu34XiiZH5gYlHXl4-YV6NuaSyF6cIUGA-ENF9Fzqnen_WwI5MigCMF_UG_J0dOW3updP3lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله  یکم لایک و انرژی بدین اپ تر و تمیز که رو ایرانسل کانکت میشه یافتم
🙊
🙈
❤️</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/archivetell/5552" target="_blank">📅 23:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5551">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سبحان الله  یکم لایک و انرژی بدین اپ تر و تمیز که رو ایرانسل کانکت میشه یافتم
🙊
🙈
❤️</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/archivetell/5551" target="_blank">📅 23:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سبحان الله
یکم لایک و انرژی بدین
اپ تر و تمیز که رو ایرانسل کانکت میشه یافتم
🙊
🙈
❤️</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/archivetell/5550" target="_blank">📅 23:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نت شخمی نشده؟
کانفیگا پولی هم بد وصله
😐
😂</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/archivetell/5549" target="_blank">📅 23:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ایرانسل پر سرعت وصل
Windscribe UDP 443 Censorship On
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/archivetell/5548" target="_blank">📅 22:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">همراه اول تست شده
vless://06ef598c-1555-4887-b3f9-08214a2f6792@104.16.7.70:443?encryption=none&host=2026.hhhhh.eu.org&path=%2F222.167.202.31%3A7443&security=tls&sni=2026.hhhhh.eu.org&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/archivetell/5547" target="_blank">📅 22:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سامانتل بدون فیلتره اینستا
😁</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/archivetell/5546" target="_blank">📅 22:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سامانتل بدون فیلتره اینستا
😁</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/archivetell/5545" target="_blank">📅 22:13 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
