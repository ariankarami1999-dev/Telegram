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
<img src="https://cdn4.telesco.pe/file/s-kMh1WxdDUrD8vqPeSH29xvxp4_6jJa6SflLutnQZmUf3lacxpeuiUCLxnqHkfUKL6j_d40LPUxYCmDl4ynSVr1wKRfthYFwCkvhvI-iiy76BS8GG2VvZHxQGHHIkCCNIJPKPGcgjwFuM8QjZ3yCsyQcTxio5lPz1iUifa3B4ri5Pk2L4rj2rM0_QsVGTF2CGZwMS2r7Gpia_G-hOPaSEH_PXeK5mGH24lTVr0MHuRAXgZqrY7ltnL-9FogPhJsfFP6VpwxeXgaAUzMWKd5Wi3c_HIM497unVL20ZUpeuRMAM3QuDC4L4AN2oqMqz8G8bpV8s1_qXXNSs8QnPkEFg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 8.25K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 23:51:20</div>
<hr>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">{
"_comment": {
"remark": "@ArchiveTell"
},
"log": {
"access": "",
"error": "",
"loglevel": "info",
"dnsLog": false
},
"inbounds": [
{
"tag": "in_proxy",
"port": 1080,
"protocol": "socks",
"listen": "0.0.0.0",
"settings": {
"auth": "noauth",
"udp": true,
"userLevel": 8
},
"sniffing": {
"enabled": false
}
},
{
"tag": "http-in",
"port": 10808,
"listen": "::",
"protocol": "http"
}
],
"outbounds": [
{
"tag": "proxy",
"protocol": "trojan",
"settings": {
"servers": [
{
"address": "188.114.96.3",
"method": "chacha20-poly1305",
"ota": false,
"password": "humanity",
"port": 443,
"level": 8,
"flow": ""
}
]
},
"streamSettings": {
"network": "ws",
"security": "tls",
"wsSettings": {
"path": "/assignment",
"headers": {
"Host": "www.calmloud.com"
}
},
"tlsSettings": {
"allowInsecure": true,
"serverName": "www.calmloud.com",
"alpn": [
"http/1.1"
],
"fingerprint": "ios",
"show": false
},
"sockopt": {
"dialerProxy": "fragment",
"tcpKeepAliveIdle": 100,
"tcpNoDelay": true
}
},
"mux": {
"enabled": false,
"concurrency": 8
}
},
{
"tag": "fragment",
"protocol": "freedom",
"settings": {
"domainStrategy": "AsIs",
"fragment": {
"packets": "tlshello",
"length": "100-200",
"interval": "10-20"
}
},
"streamSettings": {
"sockopt": {
"tcpKeepAliveIdle": 100,
"tcpNoDelay": true
}
}
},
{
"tag": "direct",
"protocol": "freedom",
"settings": {
"domainStrategy": "UseIp"
}
},
{
"tag": "blackhole",
"protocol": "blackhole",
"settings": {}
}
],
"dns": {
"servers": [
"8.8.8.8"
]
},
"routing": {
"domainStrategy": "UseIp",
"rules": [],
"balancers": []
}
}
ترکیبی سایفون یا شیر و خورشید با v2ray</div>
<div class="tg-footer">👁️ 146 · <a href="https://t.me/archivetell/5435" target="_blank">📅 23:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">{
"dns": {
"fallbackStrategy": "disabledIfAnyMatch",
"servers": [
{
"address": "tcp://1.1.1.1",
"fakedns": [
{
"ipPool": "198.18.0.0/15",
"poolSize": 65535
},
{
"ipPool": "fc00::/18",
"poolSize": 65535
}
],
"queryStrategy": "UseIP"
}
]
},
"inbounds": [
{
"listen": "127.0.0.1",
"port": 2080,
"protocol": "socks",
"settings": {
"auth": "noauth",
"udp": true
},
"sniffing": {
"destOverride": [
"fakedns",
"http",
"tls",
"quic"
],
"enabled": true,
"metadataOnly": false,
"routeOnly": true
},
"tag": "socks"
},
{
"listen": "127.0.0.1",
"port": 9080,
"protocol": "http",
"settings": {
"allowTransparent": true
},
"sniffing": {
"destOverride": [
"fakedns",
"http",
"tls"
],
"enabled": true,
"metadataOnly": false,
"routeOnly": true
},
"tag": "http"
}
],
"log": {
"loglevel": "warning"
},
"outbounds": [
{
"protocol": "trojan",
"settings": {
"servers": [
{
"address": "104.18.13.149",
"password": "humanity",
"port": 443
}
]
},
"streamSettings": {
"network": "ws",
"security": "tls",
"tlsSettings": {
"allowInsecure": true,
"alpn": [
"http/1.1"
],
"serverName": "www.calmloud.com"
},
"wsSettings": {
"headers": {},
"path": "/assignment"
}
},
"tag": "proxy-global-3669"
},
{
"protocol": "freedom",
"tag": "bypass"
},
{
"protocol": "blackhole",
"tag": "block"
},
{
"protocol": "dns",
"settings": {
"userLevel": 1
},
"tag": "dns-out"
}
],
"policy": {
"levels": {
"1": {
"connIdle": 30
}
},
"system": {
"statsOutboundDownlink": true,
"statsOutboundUplink": true
}
},
"routing": {
"domainStrategy": "AsIs",
"rules": [
{
"inboundTag": [
"dns-in"
],
"outboundTag": "dns-out",
"type": "field"
},
{
"ip": [
"geoip:private"
],
"outboundTag": "bypass",
"type": "field"
}
]
},
"stats": {}
}
ترکیبی سایفون و v2ray</div>
<div class="tg-footer">👁️ 554 · <a href="https://t.me/archivetell/5434" target="_blank">📅 23:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">این آیپی
شیر و خورشید روی آپتل وصله
142.54.178.211</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/archivetell/5433" target="_blank">📅 23:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5428">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/5428" target="_blank">📅 21:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نکوباکس رسمی نیست تا جایی میدونم
تست ویروس بودن هم چیزی تشخیص داده نشد
ولی بازم مسئولیتش با خودتون</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/5427" target="_blank">📅 21:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS.E. Virus Detect</strong></div>
<div class="tg-text">🔎
Findings:
❌
Detection: 0
⚠️
Suspicion: 0
✅
Not detected: 66
• File name:
NekoBoxPlus-1.4.2-28-universal.apk
• File format:
Android
• File size:
71.36 MB
• First analysis:
2026-05-25 21:09:17
• Last analysis:
2026-05-25 21:09:17
•
VirusTotal link</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/archivetell/5426" target="_blank">📅 21:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">NekoBoxPlus-1.4.2-28-universal.apk</div>
  <div class="tg-doc-extra">71.4 MB</div>
</div>
<a href="https://t.me/archivetell/5425" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔵
@ArchiveTell
https://4pda.to/forum/index.php?showtopic=1121122&st=680#entry143480923</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/5425" target="_blank">📅 21:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚀
آپدیت جدید NekoBox+ (نسخه 1.4.2-28)
---
رفقا سلام!
✋
یک نسخه جدید برای اپلیکیشن محبوب
NekoBox+
(نسخه بر پایه Starifly) منتشر شده که تمرکز اصلی‌اش روی بهبودِ پایداریِ روتینگ، آپدیت هسته و رفعِ باگ‌های عملکردی بوده.
###
✨
مهم‌ترین تغییرات این نسخه:
🔸
آپدیت هسته مرکزی:
- هسته
sing-box
به نسخه
v1.13.12
ارتقا پیدا کرد (بهبود پایداری کلی).
- رفع نشت حافظه (Memory Leak) و بهبود صفِ عملیات در
XHTTP
(طبق تغییرات Xray-core).
🔸
تغییرات مهم در روتینگ (Routing):
- قوانین (Rules) مربوط به
network_type
و وای‌فای (
SSID/BSSID
) و
source_port
که قبلاً در برخی شرایط نادیده گرفته می‌شدن، حالا به درستی پردازش میشن.
-
نکته:
برای اینکه روتینگ بر اساس وای‌فای درست کار کنه، برنامه حالا دسترسی
Location (موقعیت مکانی)
در پس‌زمینه رو درخواست می‌کنه تا SSID شبکه رو تشخیص بده.
🔸
تغییرات DNS (بسیار مهم):
- DNS پیش‌فرض Remote از
dns.google
به
8.8.8.8
(Google DNS over HTTPS) تغییر کرد.
- DNS پیش‌فرض Direct از حالت معمولی به
77.88.8.8
(Yandex DNS over HTTPS) تغییر کرد.
🔸
سایر اصلاحات:
- اضافه شدن پروتکل جدید
MasterDnsVpn
.
- رفع باگ نمایشِ ویرایشگرِ تم در تبلت‌ها.
- اصلاح اکسپورتِ کانفیگ‌های Trojan (اگر TLS غیرفعال باشه، پارامتر security=none به درستی اعمال میشه).
---
📥
دریافت نسخه جدید:
این نسخه برای معماری‌های مختلف اندروید (Arm64, Armeabi, x86) آماده شده. اگر از NekoBox+ استفاده می‌کنید، حتماً آپدیت کنید تا از آخرین بهبودهای sing-box بهره‌مند بشید.
📥
فایل‌های نصبی:
(پیشنهاد می‌شود فایل
universal.apk
را برای راحتی کار دانلود کنید)
🔗
📌
#آپدیت
#NekoBox
#singbox
#فیلترشکن
#اندروید
#DNS
#روتینگ
#آموزش
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/archivetell/5423" target="_blank">📅 21:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">#موقت
دوستان
با نسخه web وارد همراه من بشید
my.mci.ir
وقتی تو ماه هرچقدر صورتحسابتون باشه پرداخت کنید
برید تو قسمت تشویقی
بعد هدیه شتاب در پرداخت رو بزنید
۲ گیگ رو انتخاب کنید
و
تند‌تند روی فعالسازی تا قبل از نمایش پیام موفقیت سمت راست پایین ادامه بدید
چند لحظه ضبر کنید بعدش اینترنت براتون با حجم زیاد فعال میشه</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/5422" target="_blank">📅 21:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0283f0af06.mp4?token=jjX9zytgyxhFZf9N95kgRdW-hyS_vPh7sPXKAa6c4eOkjNS5E6OPNKZ5nJKukW6YohRYc55gthSsO_n2M8YTqM4Af5JOLxaEVP2Lmapb7lgvd3PGYCAIpvZx0FeLMT0ctd_whWK9uPA_HbD5Ty0hJwt1LM2j8S_RtcbH6N-dmRzMAAXI0deIBTga0Pp8pTcCuhbPvSaWSxq2Myuk-JmrrB8xkNI0gA7sfCvHeojT_eVCFn0LMUYFMAcPvLayPra2mN-4wrHM6gLjSPetpUXAvedZq7ZHAO34aVjYcAp5X0gSSQFJNNxstoJ79KHWCaXsuqBfkp8sFiad2wukPuwnKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0283f0af06.mp4?token=jjX9zytgyxhFZf9N95kgRdW-hyS_vPh7sPXKAa6c4eOkjNS5E6OPNKZ5nJKukW6YohRYc55gthSsO_n2M8YTqM4Af5JOLxaEVP2Lmapb7lgvd3PGYCAIpvZx0FeLMT0ctd_whWK9uPA_HbD5Ty0hJwt1LM2j8S_RtcbH6N-dmRzMAAXI0deIBTga0Pp8pTcCuhbPvSaWSxq2Myuk-JmrrB8xkNI0gA7sfCvHeojT_eVCFn0LMUYFMAcPvLayPra2mN-4wrHM6gLjSPetpUXAvedZq7ZHAO34aVjYcAp5X0gSSQFJNNxstoJ79KHWCaXsuqBfkp8sFiad2wukPuwnKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای یه سری ها این روش قطع شده داخل کانفیگ به جای اون ip این رو بزارید و مجدد لذت ببرید:)))
188.114.96.4
@xsfilterrnet
👑
@ArchiveTell
⚡️</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/archivetell/5420" target="_blank">📅 21:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9251555194.mp4?token=YdIwrEapotk5wnPu3htMNgzsy7T0k0WH2Hj8D8AYIDV8beI5-jEcuCexH-N8DRPxDJ95Ru5_IV5zKDexI_Jfm5HJwcCZYR3US8CW6-amCSVUMWmnysA5EGVxow7CyiIBoFoOltiXwpTIV18lDCwg9qO-pyyQIwsTJW2qO8WynCAo5DyTIDoPX_7rSRmNSHQbsxCej8GlqoBPn1wMtA2ynR7e5nyJs5bymIDY9o6gB4XSpigR5TpJrS5rwWaExFeQIJrPVfUEjO5AglujgyFDTCPBgsqbeS-U4Sv_A_S5sNb_4BKn2_wQdBrjRqUwFgC7rth29Ij8fQhjg3DmnIVLug7tA64mBqQcDCq5dJE0ql8JWw--KQeEuf9yFeR9peEIhVjTdOUu3iwriZzSBgkuBYqj7MkhDoGMcPBa1iNaIvcsawqjvURQPpI3db50yRpP76g7af7tRCFTOBA2gAuW3iZSgCE8VScvhNQ5dTKiXmc_s6yokThSDm_QfXEnKeZO0ajbOk0qQEnrO6-yZ-d-UXwmTA2mOJMEuWr2U-ZOwRw2h034I1r_9L6Uw46HAPFBlH_CdtFLQxUwwuTTOQQpfYc5ZMyFgyRvtP-pOi8nDKCXH0An0qtFaj8g3gi2xyUbnLbLHEtExseJ6lY785LDPm1eYX9Z_xPpWEX7daKNMHU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9251555194.mp4?token=YdIwrEapotk5wnPu3htMNgzsy7T0k0WH2Hj8D8AYIDV8beI5-jEcuCexH-N8DRPxDJ95Ru5_IV5zKDexI_Jfm5HJwcCZYR3US8CW6-amCSVUMWmnysA5EGVxow7CyiIBoFoOltiXwpTIV18lDCwg9qO-pyyQIwsTJW2qO8WynCAo5DyTIDoPX_7rSRmNSHQbsxCej8GlqoBPn1wMtA2ynR7e5nyJs5bymIDY9o6gB4XSpigR5TpJrS5rwWaExFeQIJrPVfUEjO5AglujgyFDTCPBgsqbeS-U4Sv_A_S5sNb_4BKn2_wQdBrjRqUwFgC7rth29Ij8fQhjg3DmnIVLug7tA64mBqQcDCq5dJE0ql8JWw--KQeEuf9yFeR9peEIhVjTdOUu3iwriZzSBgkuBYqj7MkhDoGMcPBa1iNaIvcsawqjvURQPpI3db50yRpP76g7af7tRCFTOBA2gAuW3iZSgCE8VScvhNQ5dTKiXmc_s6yokThSDm_QfXEnKeZO0ajbOk0qQEnrO6-yZ-d-UXwmTA2mOJMEuWr2U-ZOwRw2h034I1r_9L6Uw46HAPFBlH_CdtFLQxUwwuTTOQQpfYc5ZMyFgyRvtP-pOi8nDKCXH0An0qtFaj8g3gi2xyUbnLbLHEtExseJ6lY785LDPm1eYX9Z_xPpWEX7daKNMHU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
به نام یزدان گردان سپهر
درود دوستان، آموزش ساخت پنل cfnew و ملزومات
#کانفیگ
ترکیبی رو براتون ضبط کردم
تمامی مراحل در ویدیو مشخصه
😎
نکته های مهم که باید توجه شه بهشون
❗️
1-در صورتی که قصد آپلود با موبایل دارید باید فایل قبلی حذف و نام فایل به worker.js تغییر کنه
2-برای متغیر KV باید حرف C رو بزرگ (کپتال) بنویسید
3-برای ورود به پنل بعد از زدن روی visit site تنها اقدامی که لازمه اضافه کردن UUID هست که ست کردید
4-مثل من افکت صفحه رو خاموش کنید تا صفحه روان تر باشه
5-تیک تروجان رو فراموش نکنید همون اول کار بزنید (من خودم یادم رفت)
6-به پروژه حتما استار بدید
7-از کانفیگ کاستوم که بدست آوردید
پینگ نگیرید
و فقط ترکیب کنید
﻿
چیز هایی که باید تو این
کانفیگ
تغییر کنه :
servername
host
path
password
هست که توی ویدیو کاملا نشون دادم کدوم بخشه.
✅
لینک گیتهاب پروژه
✅
لینک دریافت UUID
😀
لینک ایمیل موقت
(توی ویدیو نمایش داده نشده ولی خب ساختش راحته)
دانلود فایل پروژه و ویدیو با لینک داخلی
👉
👉
Pass :
@hamedvpns
‌‌
@hamedvpns
💎
@xsfilterrnet
👑
@ArchiveTell
⚡️</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/archivetell/5419" target="_blank">📅 21:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">@ArchiveTell تون ماهی</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/5418" target="_blank">📅 21:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ساخت ویدئو های سینمایی که واقعا شبیه صحنه های فیلم به نظر میرسند
🎬
⚡
🌐
https://higgsfield.ai
@ArchiveTell
#VideoAI
#AITools</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/5417" target="_blank">📅 20:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5414">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDDKft--pfMspQI0i3hUXjluvJMC9GZaedKXokh3ET_I8h1u9o3uyI2ovnunMI2_VDSL6S84flZRvkgdoj0bYkEXp2Psxrp0nWVFMs7S1jH6eVPZVC_z1WYmIQZfGpHC30zdvAU_tLM2rXCDYcoX_VJtYhwD9YdGK_N9OCTpb8MYBnvaRz_XOPpH8nQfztZ8zyhEKHaUCMYQcuQvwk0aWrk-VFOMMM_VcZGYCjQUDWrg3ITboi9BfO2PlyyNAT3AilV0U1q0TqNS5l_bU2HPGu2ktriUzDYDC3TqWpKnPiE4BuU9omXzY9WY6bEfRVuSe8oSig2PMSVgME25VHo-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@ArchiveTell
تون ماهی</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/5414" target="_blank">📅 19:50 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMehrsan</strong></div>
<div class="tg-text">امیدوارم یه روز همه اینا چیزی جز یه خاطره ازشون نمونه و دیگه مجبور نباشیم بخاطر حقمون انقد زحمت بکشیم</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/5413" target="_blank">📅 19:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from❖Ƭʜᴇᴍᴀʜᴅɪ</strong></div>
<div class="tg-text">من که نت وصل بشه بازم به همین شیرخورشید وصل میشم
یا sni spoof میزنم برای خودم
رایگانه بدون تبلیغه سرعتشم بد نیست
کسخلم پول بدم؟</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/5412" target="_blank">📅 19:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromfanee .ir</strong></div>
<div class="tg-text">ملت اینقدر متدهای مختلف یاد گرفتن و تست کردن که IP گوگل باز بشه کسی دنبال خرید کانفیگ و VPN نمیره ...
به هفت روش سامورایی وصل میشن ...
الان یکسری از ایرانی ها واکسینه شدن نسبت به نت ملی ...
چه به روزمون آوردن ... دم همه اون هایی که این ۳ ماه پای کار مردم بودن گرم ، خیلی هاشون رو نمیشناسیم ولی کاری کردن که فیلترچی شب ها خواب نداشت و کابوس متد جدید میدید ... فیلترچی باختی بد هم باختی
👏
👏
👏
👏
👏</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/5411" target="_blank">📅 19:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شیر و خورشید همه نتا وصل  CDN edge IPs :  185.141.106.238 185.50.37.52 80.191.243.226 164.138.17.122 185.88.178.196 109.72.197.1 78.39.234.140 5.160.128.142  CDN SNI hostname: snapp.ir  Beast Mode : روشن   لینک داخلی شیر و خورشید   @ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/5410" target="_blank">📅 19:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3OWikqUPl3m1Ula-LSI03fr3b1YTbpz4fN9BCwZQJBcSERaR8WVwtTVvAxYFJrd2G3syeP7S8n2MRBLfgcw2OrXlHLOsfs3cTCzeWuIyDn0F0DOgcTnb5DV06cB65pEL_Eyq8Us6ItLvIgdoUYlcKRUF9PoyEoCO9NQE7QD9c_XTIF2oyTnPx0SJhhkcTy7Eh-0vCavx_BZCvePuh6m2Z5UpozDiHEyc-PdZDup5s5X8nTRzACC1nFMBFy6WN3fdDv0RK6f0elV0P-D4MPKb7mxO_vgf1EBReVbHn5ybCzWtT7W9jQZo6mbM5AtILADFYq_6rEi0136VmF8i1g1bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیر و خورشید همه نتا وصل  CDN edge IPs :  185.141.106.238 185.50.37.52 80.191.243.226 164.138.17.122 185.88.178.196 109.72.197.1 78.39.234.140 5.160.128.142  CDN SNI hostname: snapp.ir  Beast Mode : روشن   لینک داخلی شیر و خورشید   @ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/5409" target="_blank">📅 19:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شیر و خورشید همه نتا وصل
CDN edge IPs :
185.141.106.238
185.50.37.52
80.191.243.226
164.138.17.122
185.88.178.196
109.72.197.1
78.39.234.140
5.160.128.142
CDN SNI hostname:
snapp.ir
Beast Mode : روشن
لینک داخلی شیر و خورشید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/5408" target="_blank">📅 19:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترکیبی سایفون و v2ray
vless://aaaaaabb-4ddd-4eee-9fff-ffffffffffff@188.114.96.4:443?allowInsecure=1&alpn=http%2F1.1&encryption=none&path=%2F43.218.77.16%3D443&security=tls&sni=JoinProxyVPN11.afrcloud4.c01.kr&type=ws#@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/5407" target="_blank">📅 18:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترکیبی سایفون و v2ray
trojan://humanity@188.114.96.4:443?allowInsecure=1&alpn=http%2F1.1&path=%2Fassignment&sni=www.calmloud.com&type=ws#@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/5406" target="_blank">📅 17:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">لیست جدید و قوی برای روش cdn fronting
من با ایرانسل چک کردم بقیه نت هام تست کنید
🌸
اگر ای پی شما با ۲۶ شروع بشه احتمال اتصال بالاتر میره
بعد از زدن دکمه استارت حداقل یک دقیقه صبر کنید
۴/خرداد/۱۴۰۵
جای IP خالی باشه.
snapp.ir
varzesh3.com
digikala.com
telewebion.com
bmi.ir
aparat.com
divar.ir
namava.ir
python.org
yryirjrhqffsxwpg-a.akamaihd.net
a248.e.akamai.net
qpwn.com
bbdv.net
a.akamaihd-staging.net
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/5404" target="_blank">📅 16:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مخابرات وصل
vless://8c4604ef-749c-4b56-adf1-7da405002a21@2.144.4.154:40443?encryption=none&host=qyi.fqjd663.ggff.net&path=%2F&security=tls&sni=qyi.fqjd663.ggff.net&type=ws#@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/5403" target="_blank">📅 16:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">alain-de-botton-the-course-of-love.epub</div>
  <div class="tg-doc-extra">578.9 KB</div>
</div>
<a href="https://t.me/archivetell/5402" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">حالا که کتابخون تو چنل هست
این کتاب باحالیه
ترجمه فارسیشم موجوده
اشنایی دو نفر هست و میتونین مسیر و روند عشق این دونفر رو تجربه کنین در طول داستان
در کنار نظرورزی های الن دوباتن که به شما درباره عشق خیلی مطالب خوبیو یاد میده
از تب عشقی اول رابطه گرفته تا دردسر های بعدش
نقد عشق مدرن و اون چیزی که بیشتر تو رسانه از عشق دیده میشه
https://t.me/Alain_de_Bottonn/169</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/5402" target="_blank">📅 14:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نرم افزار دانلود از گوگل درایو
https://abrehamrahi.ir/o/public/W9uUu9PS/
لینک های درایو رو بردارین و داخلش پیست کنین و منتظر بشین تا دانلود تموم شه.
ربات های تبدیل فایل به لینک گوگل درایو:
@TheGdriveXBot
@File_linkerobot
@GDrive_Uploader_Robot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/5401" target="_blank">📅 14:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کرم کتاب داریم اینجا؟ Annas-Archive  خیلی طول میکشه تا PDF ازش دانلود بشه جایگزین چیزی هست؟ Libgen قدیم خوب بود</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/5400" target="_blank">📅 14:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کرم کتاب داریم اینجا؟
Annas-Archive
خیلی طول میکشه تا PDF ازش دانلود بشه
جایگزین چیزی هست؟
Libgen قدیم خوب بود</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/5399" target="_blank">📅 14:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5398">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد  اگر تازه با TheFeed آشنا شدید و نمی‌دانید از کجا باید شروع کنید، این ویدیو دقیقاً برای شماست.
👇
در این آموزش یاد می‌گیرید:
✅
اضافه کردن کانفیگ
✅
آشنایی با ریزالورها (DNS)
✅
پیدا کردن ریزالورهای سالم
✅
مشاهده کانال‌ها و دریافت…</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5398" target="_blank">📅 13:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOKElhkFJQsl4lDJJGy-a_zTh1ADRC49BstxQn42vMC4sAZYXe8dgi0TvJ0gBcb-b-CMjb3yUPeuUDVf4Mea6RBAAL25VRE1I1kuipjNKtVHNClV56YS99AYiQzdDMZA-pXcROTwuVT3LefgX4c8DZSEovNlhZvagSHjS_T_NeB3hC2U-Dnr6jSmaY30dD1wBUuSJVFY0AzKyhVAQ3cm6hTV3oh6BcMAmN-tKiOjtcCZnf86JSEJyN0EtpK-slsmiN7AsUEIgtIHNQnq51O-nMF84Xhe-VVIQl2czfFWlDPnI2-mZtaNokdPO-8W5gpNDC3pYdWJBNViDmUKPtPwHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
FileShare یه ابزار ساده برای اشتراک‌گذاری فایل توی شبکه محلیه. با این برنامه می‌تونی فایل‌ها رو روی سیستم خودت آپلود کنی و از یه دستگاه دیگه داخل همون شبکه، خیلی راحت دانلودشون کنی.
✅
کارش اینه: - فایل را می‌فرستی داخل ابزار - برنامه فایل را ذخیره می‌کند…</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/5397" target="_blank">📅 13:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سایت جدید film2media
film2media
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/5396" target="_blank">📅 12:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🦁
معرفی Lion VPN: یه رابط کاربری شیک برای متد Google Relay
---
رفقا خیلیا از متدِ "Google Relay" (که با پایتون اجرا می‌شه) برای عبور از فیلترینگ استفاده می‌کنید. مشکل همیشگی این روش، درگیری با اسکریپت‌ها و تنظیمات دستیِ پروکسی روی گوشیه.
پروژه
Lion VPN
(که تازه منتشر شده) اومده این مشکل رو حل کرده. این ابزار در واقع یه رابط گرافیکی (GUI) مدرن و زیباست که کدهایِ پایتونیِ اون متد رو توی خودش بسته (Bundle) کرده و یه تجربه کاربریِ "یک‌کلیکی" بهتون میده.
✨
چرا این ابزار رو پیشنهاد می‌کنم؟
-
رابط کاربری مدرن:
با استفاده از Compose Multiplatform ساخته شده و خیلی نرم و روونه (دارک‌مود هم داره).
-
پشتیبانی از Android VpnService:
این مهم‌ترین ویژگیه! دیگه لازم نیست توی تنظیماتِ وای‌فایِ گوشی، پروکسیِ دستی وارد کنید. خودش ترافیک رو می‌گیره و می‌فرسته توی تونل.
-
تولید خودکارِ گواهینامه:
برای باز کردن سایت‌های HTTPS، این برنامه خودش گواهینامه رو می‌سازه و نصبش رو براتون راحت می‌کنه.
-
نسخه دسکتاپ:
برای ویندوز، مک و لینوکس هم یه برنامه مستقل (Executable) میده که دیگه نیاز به نصب پایتون ندارید.
🛠
نحوه راه‌اندازی:
۱. همون روالِ قدیمیِ Deploy کردنِ اسکریپت روی
Google Apps Script
رو انجام بدید (فرقی نکرده).
۲. برنامه Lion VPN رو از گیت‌هاب دانلود و اجرا کنید.
۳. اطلاعاتِ مربوط به Deployment ID و کلیدِ امنیتی (Auth Key) رو داخل برنامه وارد کنید و دکمه Connect رو بزنید.
🔗
لینک گیت‌هاب پروژه:
🌐
https://github.com/dariushm2/CMP-GUI-MasterHttpRelayVPN
---
💡
نظرتون چیه؟
این پروژه در واقع یه fork از کارهای قبلیِ Google Relay هست که تمرکزش رو گذاشته روی ظاهر و راحتیِ کار با موبایل.
اگر کسی این رو تست کرده، بیاید توی کامنت‌ها بگید:
-
روی گوشی پایداریش چطوره؟
-
توی مصرف باتری اذیت می‌کنه یا نه؟
اگه تجربه یا مشکل خاصی باهاش داشتید بنویسید تا بقیه هم موقع نصب بدونن چی به چیه.
👇
📌
#معرفی_ابزار
#GoogleRelay
#LionVPN
#اندروید
#فیلترشکن
#رابط_کاربری
#آموزش
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/5395" target="_blank">📅 12:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مخابرات وصل
socks5://81.12.24.237:24845#(WIFI)</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/5394" target="_blank">📅 12:14 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🤖
Claude‌ رو هکر کن!
---
رفقا، یه پروژه خفن اومده به اسم
Claude-BugHunter
. قضیه چیه؟
این ابزار یه پکیج‌ه که می‌ریزید رو Claude Code و عملاً مغزش رو عوض می‌کنید! یعنی دیگه مثل یه چت‌باتِ معمولی جواب نمیده، تبدیل میشه به یه «هکرِ ارشد» که کلی تجربه (از ۵۰۰ تا باگِ واقعیِ HackerOne) تو مغزش داره.
خلاصه بگم چی‌کار می‌کنه:
•
هانتِ حرفه‌ای:
به‌جای حدس و گمان، قشنگ می‌دونه کجا رو باید بگردی.
•
فیلترِ باگ:
قبل از اینکه وقتت رو برای گزارشِ باگ‌های الکی (که ریجکت میشن) هدر بدی، خودش با یه فیلترِ هوشمند چکشون می‌کنه.
•
گزارش‌نویسی:
گزارشِ باگ رو قشنگ آماده می‌کنه که فقط کپیش کنی.
•
پوششِ عالی:
از باگ‌هایِ وب گرفته تا سرورهای سازمانی و حتی VPNها و سرویس‌های کلودی.
خلاصه اگه تو کارِ Bug Bounty یا تست‌نفوذ هستی، این ابزار خوراکِ خودته که Claude رو دستیارِ اولِ خودت کنی.
🔗
لینک گیت‌هاب:
https://github.com/elementalsouls/Claude-Bughunter
نصبش هم خیلی راحته، فقط کافیه اسکریپتش رو اجرا کنید. اگه کسی تستش کرد بگه واقعاً باگ‌خوره یا نه!
😉
📌
#ابزار
#امنیت
#هک
#Claude
#BugBounty
#هوش_مصنوعی
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/5393" target="_blank">📅 12:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCE-5gpJWHT30P2kgSPANIqzhxnSxENyCP4u4UdCb7kHe-2skv3F5tCnrNQu6hPRy7nptvz6Aid3uZjZ_GhIbJ5iclQPCCWwqZUm7X7X0SseznEk-0_nzqOjcVfsQS3MniKKcGRUh7ucgSUnZrWcqT4mM0HIEtjmziLfpjVKhlFBBpRgfTu-OpJk_Db5Qx13VemGajeDQq4JEULz4vy9op9OdKpBEc60HHcI-V08qCXR_PYl3TL11O06tqKTTGFQW0nBk7UZZKq6fA3B0UquGtrOoIVxDx2U6KxWV8a3Eguyj6PwDJBoxT69msSckpn298bbX9aoh8SWHDPcjJpO3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔬
برای Claude Code مجموعه‌ای از بیش از ۳۰ عامل هوش مصنوعی ساخته شده است که مقالات علمی می‌نویسند — آن‌ها ایده خام را به مقاله آماده، پروژه کلاسی، گزارش یا حتی پایان‌نامه تبدیل می‌کنند.
https://github.com/Imbad0202/academic-research-skills
این عوامل از طریق arXiv، Semantic Scholar و DBLP تحقیق عمیقی انجام می‌دهند، مقاله را مرحله به مرحله می‌نویسند، کیفیت را ارزیابی می‌کنند، صحت اطلاعات را بررسی می‌کنند و نتیجه را به فرمت‌های APA، IEEE، MLA و دیگر فرمت‌ها صادر می‌کنند.
@ArchiveTell
#Claude</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/5392" target="_blank">📅 11:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=T2tzBzBat38gCkRLA1vxIGFBNTIHA5ExIvhylWpJjr7nfN21km_iFwWYvH8-4yvALq8atsf7xdvRc6EzHIYM3xMI5MGMCa8x8GjUcvI3eRSOdvo8ht72_uCVmI4V8YKo2w23KdrYz9g__XSiEww0NCHmoGgMoRCVZFgENqzdRtBBmKiR8sbD_-p97CeWta7EyhTbHxLZDXx_9dEMKNcCal13FD645PXPYvUGdqZjI3z7zOcvKRD1unYi5k8OVJhph0hh9ZcIjvChCS5MFQaJvuj3AhsX2tAHJoHbiRugkHjSYaYmqTHOjog_JqWL-p8Q-Cq7tKyptAaPq5icmjkjZWULL3cs4N4DL5lU4yvCKFwYSn8Bdm9nhaxaQ5HX23fEPnAEbIQf7U-GjN7RxYoa_sNMD09YPQ065dVhiAwtms1nHrIgKsNZabYwf47oZT1_Q_C7hp_GhmMiN2rMHngJ793tURHRcMNCR28QLa4HA66rid99VlS7oOPYokP7ZcHqUDT7QyFXA9T7NH6uiln8-kwmh3NCqILKn2RBute-1siUtjI0pVpScEp22JZyzaWJzFOqAUKIBzxgdCDleTQ5ozFZ_AEqQHApoDnQXmvdsfJvtAVdapmIS5VktIVrMXvtjVWQPIAK0CSrH30khyH5NfgG-IiH4OMiWAo_u8xOr74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=T2tzBzBat38gCkRLA1vxIGFBNTIHA5ExIvhylWpJjr7nfN21km_iFwWYvH8-4yvALq8atsf7xdvRc6EzHIYM3xMI5MGMCa8x8GjUcvI3eRSOdvo8ht72_uCVmI4V8YKo2w23KdrYz9g__XSiEww0NCHmoGgMoRCVZFgENqzdRtBBmKiR8sbD_-p97CeWta7EyhTbHxLZDXx_9dEMKNcCal13FD645PXPYvUGdqZjI3z7zOcvKRD1unYi5k8OVJhph0hh9ZcIjvChCS5MFQaJvuj3AhsX2tAHJoHbiRugkHjSYaYmqTHOjog_JqWL-p8Q-Cq7tKyptAaPq5icmjkjZWULL3cs4N4DL5lU4yvCKFwYSn8Bdm9nhaxaQ5HX23fEPnAEbIQf7U-GjN7RxYoa_sNMD09YPQ065dVhiAwtms1nHrIgKsNZabYwf47oZT1_Q_C7hp_GhmMiN2rMHngJ793tURHRcMNCR28QLa4HA66rid99VlS7oOPYokP7ZcHqUDT7QyFXA9T7NH6uiln8-kwmh3NCqILKn2RBute-1siUtjI0pVpScEp22JZyzaWJzFOqAUKIBzxgdCDleTQ5ozFZ_AEqQHApoDnQXmvdsfJvtAVdapmIS5VktIVrMXvtjVWQPIAK0CSrH30khyH5NfgG-IiH4OMiWAo_u8xOr74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
اگر تازه با TheFeed آشنا شدید و نمی‌دانید از کجا باید شروع کنید، این ویدیو دقیقاً برای شماست.
👇
در این آموزش یاد می‌گیرید:
✅
اضافه کردن کانفیگ
✅
آشنایی با ریزالورها (DNS)
✅
پیدا کردن ریزالورهای سالم
✅
مشاهده کانال‌ها و دریافت محتوا
✅
آشنایی با بخش TeleMirror
✅
رفع مشکلات رایج کاربران
✅
نکات مهم برای استفاده بهتر از برنامه
دفید یک سیستم مبتنی بر DNS است که امکان دسترسی به محتوای کانال‌های تلگرام را حتی در شرایط محدودیت اینترنت فراهم می‌کند.
📢
کانال اصلی پروژه:
@networkti
📦
فایل‌های نصب:
@thefeedfile
⚙️
کانفیگ‌های عمومی:
@thefeedconfig
توضیحات متنی
👇
سلام. توی این ویدیو می‌خوام خیلی ساده و سریع نحوه کار با برنامه The Feed رو توضیح بدم.
بعد از نصب و باز کردن برنامه، اولین کاری که باید انجام بدید اضافه کردن یک کانفیگه. برای این کار از بالا روی علامت جمع بزنید و کانفیگ مورد نظرتون رو وارد کنید. کانفیگ‌های عمومی داخل کانال
@thefeedconfig
منتشر میشن و می‌تونید از اونجا دریافتشون کنید.
هر کانفیگ دارای تعدادی ریزالور پیش فرض هست که توسط سازنده کانفیگ داخل کانفیگ قرار میگیرن. بعد از اینکه کانفیگ رو اضافه کردید، برنامه شروع می‌کنه به بررسی ریزالورها. ریزالورها همون DNS هایی هستن که The Feed از طریق اون‌ها اطلاعات رو دریافت می‌کنه. این مرحله ممکنه چند دقیقه طول بکشه، پس اگر بلافاصله کانال‌ها نمایش داده نشدن نگران نباشید. بعد از پیدا شدن ریزالورهای سالم، لیست کانال‌ها دریافت میشه و می‌تونید وارد هر کانال بشید، پست‌ها رو ببینید و در صورت وجود، عکس‌ها، فایل‌ها، ویس‌ها و ویدیوها رو دانلود کنید.
اگر یه زمانی دیدید برنامه کند شده یا اطلاعات جدید دریافت نمی‌کنه، معمولاً مشکل از ریزالورهاست. برای همین داخل برنامه بخشی به اسم «پیدا کردن ریزالور» وجود داره. وارد این قسمت بشید و روی «بارگذاری لیست پیش‌فرض» بزنید. با این کار حدود ۵۸ هزار ریزالور برای اسکن آماده میشن.
اگه خودتون ریزالور خاصی دارید، می‌تونید به صورت دستی هم واردش کنید. علاوه بر این، ربات
@dns_resolvers_bot
هم می‌تونه برای پیدا کردن ریزالورهای جدید بهتون کمک کنه.
بعد دکمه «شروع اسکن» رو بزنید تا برنامه ریزالورهای سالمی که روی اینترنت شما کار می‌کنن رو پیدا کنه. وقتی چند تا ریزالور پیدا شد، می‌تونید اون‌ها رو به لیست فعال اضافه کنید. فقط یادتون باشه موقع اسکن بهتره VPN خاموش باشه تا نتیجه دقیق‌تری بگیرید.
داخل برنامه یه بخش دیگه هم به اسم Tele Mirror وجود داره. این قسمت با سیستم اصلی TheFeed فرق داره و برای نمایش کانال‌های عمومی تلگرام از سرویس‌های گوگل استفاده می‌کنه. با TeleMirror می‌تونید خیلی از کانال‌های عمومی دلخواهتون رو دنبال کنید، ولی محدودیت‌هایی هم داره؛ مثلاً امکان دانلود فایل یا پخش ویدیو توی این بخش وجود نداره. همچنین اگر سرویس‌های گوگل در دسترس نباشن، ممکنه Tele Mirror کار نکنه. البته این موضوع روی بخش اصلی TheFeed تأثیری نداره و سیستم اصلی برنامه همچنان از طریق DNS به کار خودش ادامه میده.
در نهایت اگر جایی به مشکل خوردید، اولین چیزی که باید بررسی کنید ریزالورها هستن. در اکثر مواقع با پیدا کردن چند ریزالور سالم، مشکل برنامه برطرف میشه. برای دریافت آخرین اخبار پروژه هم می‌تونید کانال
@networkti
رو دنبال کنید، فایل‌های نصب رو از
@thefeedfile
بگیرید و کانفیگ‌های عمومی رو از
@thefeedconfig
دریافت کنید.
ممنون که این ویدیو رو دیدید و امیدوارم از The Feed لذت ببرید.</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/5391" target="_blank">📅 11:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54f6977bbd.mp4?token=Zte2hG4C0Uid6pscguNo2JtPIii0Qcko6drP-AxEaDFmC4AxxGN15HooPew67JCJcOUuOKXtGT9zolZnNpPnHfwD_lMN4m-uW-ZPZgJV-B6Kw5FSx6hJO8tQB4xufK5x3eYWdrt92ivspXKsaNEeuhtq2RrotCo8yTUmj4BTD2Asuwgzq0dlJJr5sliFmWT-E8gM3MKSgMzIXWwy6RZo4_pi7Lsgw28DN6HL1KVzAj8BmpfCvAyau79rJYjMArFLlE5RItnu9A--PWukRhncCE8LAVcA21ld_hZs_gwq5Iu_A-0ZN32XhSLL1-U3EovaUumd-oE3IujbQdD80vHeaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54f6977bbd.mp4?token=Zte2hG4C0Uid6pscguNo2JtPIii0Qcko6drP-AxEaDFmC4AxxGN15HooPew67JCJcOUuOKXtGT9zolZnNpPnHfwD_lMN4m-uW-ZPZgJV-B6Kw5FSx6hJO8tQB4xufK5x3eYWdrt92ivspXKsaNEeuhtq2RrotCo8yTUmj4BTD2Asuwgzq0dlJJr5sliFmWT-E8gM3MKSgMzIXWwy6RZo4_pi7Lsgw28DN6HL1KVzAj8BmpfCvAyau79rJYjMArFLlE5RItnu9A--PWukRhncCE8LAVcA21ld_hZs_gwq5Iu_A-0ZN32XhSLL1-U3EovaUumd-oE3IujbQdD80vHeaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از وقتی اینترنت قطع شده انلاین شاپا دست به هرکاری میزنن بتونن جنساشونو بفروشن
😂
😂
😂
😂
😂
بابا اینترنتو وصل کنید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/5390" target="_blank">📅 11:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7HpoBSlBmmUTVpQC6GY8l23GnedeQPyPQMscRBnYE9uCjcL83jHJj6CwqQIpCOnh6-YHmVH8nSjtCWg5SNU_HW3I-32dorcF9YbkmvSGe7kCEiysyC8ptgdjefxBBtrf4gXdY4YPvXkUK_tzPUzyPujmM2TyCDDaJlgROgtIpGJnExubDM4xwl_i09uQrHFW45W4TTGnydaHXMd_F0w__DAFZE8SAdhBqbne5rG92XCO3jDMFgLyvMDPoZdpGfxHUunf_7PUgFWRnr3WSuSiYzUqpEnT8TyuPETYwKGvlcBHCs_Fm_zGWPZvLhfDykVXHEZnCezaI2StG7B_3KObw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@ilovepdfs_bot
خار و مادر ور رفتن با pdf
یسری قابلیتاش رایگانه
یسری هم پولیه
با رفرال میشه برای تایم محدود قابلیتاشو باز کرد</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/5389" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بررسی میزان تمیز بودن آیپی:   https://www.ipqualityscore.com/ip-reputation-check    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/5388" target="_blank">📅 10:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بررسی میزان تمیز بودن آیپی:
https://www.ipqualityscore.com/ip-reputation-check
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/5387" target="_blank">📅 10:50 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">علی‌بابا به تازگی یک مترجم هوش مصنوعی معرفی کرده که می‌تواند صدای شما را به صورت زنده شبیه‌سازی کند
🤯
⚡
https://qwenlm.github.io
برخلاف مترجمان معمولی، این مدل می‌تواند:
• صدای شما
• لحن
• سبک صحبت
• آهنگ طبیعی گفتار
را حفظ کند در حالی که به صورت زنده به زبان دیگری ترجمه می‌کند
👀
@ArchiveTell
#VoiceAI
#AITools</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/5386" target="_blank">📅 09:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مخابرات وصله
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@95.38.164.245:40443?allowInsecure=1&encryption=none&host=sni.111000.indevs.in&path=%2F%3FTelegram%D9%8B+%40ProxyVPN11&security=tls&sni=sni.111000.indevs.in&type=ws#@ArchiveTell</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/archivetell/5384" target="_blank">📅 07:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">95.38.164.245
40443
بزنید رو کانفیگای کلود
مخابرات وصله</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/archivetell/5383" target="_blank">📅 07:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-text">🥮
آپدیت پروژه IR NETLIFY RELAY
📌
v 1.1.2
📦
ورود به سایت و دریافت فایل پروژه
🔸
روی دکمه Generate & Download ZIP کلیک کنید
🔹
فایلی که دانلود میشه استخراج کنید
🔸
داخل پوشه Template Sites چند تا سایت فیک هست
🔹
این 3 سایت فیک رو با فاصله 1 دقیقه در نتلیفای دپلوی کنید (روی یک پروژه)
🔸
هر سایت رو که دپلوی میکنید آدرس پروژه رو باز کنید تا طبیعی بشه
🔹
پس از دپلوی آخرین سایت فیک، روی همون پروژه کل فایل زیپ رو دپلوی کنید (استخراج نکنید)
⚠️
خیلی نرم شروع کنید ترافیک رد کردن
🔺
اکانت نتلیفای تمیز بسازید
🔺
جیمیل تمیز
🔺
آیپی تمیز
🌐
گیتهاب پروژه
⚙️
کانفیگ ساز
🌟
انرژی بگیریم
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/5382" target="_blank">📅 00:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Code obfuscator.html</div>
  <div class="tg-doc-extra">11.8 KB</div>
</div>
<a href="https://t.me/archivetell/5381" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
ابزار  Netlify obfuscator
یه ابزار سبک و به شدت کاربردی برای کسایی که روی
Netlify
پراکسی ران می‌کنن!
🌐
این ابزار بهتون کمک می‌کنه کدهاتون رو با کمک هوش مصنوعی کاملاً Obfuscate کنید (تغییر نام متغیرها و فایل‌ها) تا شناسایی نشن، و در نهایت
مستقیم یه فایل ZIP با پوشه‌بندی دقیق و آماده دیپلوی
تحویل بگیرید.
⚙️
چطور کار می‌کنه؟
1️⃣
پرامپت آماده‌ی داخل ابزار رو کپی می‌کنید و به همراه کدهای اصلیتون به هوش مصنوعی می‌دید.
2️⃣
متن خروجی هوش مصنوعی رو داخل ابزار پیست می‌کنید.
3️⃣
با یه کلیک، فایل .zip آماده شامل netlify.toml و توابع Edge رو دانلود می‌کنید!
✅
مزایا:
*
اجرای لوکال و آفلاین:
کاملاً روی مرورگر خودتون کار می‌کنه و هیچ دیتایی جایی ارسال نمیشه (امنیت ۱۰۰٪).
*
ساخت خودکار ساختار پوشه‌ها:
دیگه نیازی به ساخت دستی فایل‌ها و پوشه‌ها نیست.
*
ساده و سریع:
مناسب برای دیپلوی‌های پشت سر هم.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/archivetell/5381" target="_blank">📅 00:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">trojan://humanity@127.0.0.1:40443?host=www.ignitelimit.com&path=%2Fassignment&sni=www.ignitelimit.com&type=ws#@ArchiveTell%201
trojan://humanity@127.0.0.1:40443?host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#@ArchiveTell%202
trojan://humanity@127.0.0.1:40443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#@ArchiveTell%203
trojan://humanity@127.0.0.1:40443?host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#@ArchiveTell%204
trojan://humanity@127.0.0.1:40443?alpn=http%2F1.1&host=www.calmloud.com&path=%2Fassignment&sni=www.calmloud.com&type=ws#@ArchiveTell%205
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#@ArchiveTell%206
trojan://humanity@127.0.0.1:40443?path=%2Fassignment&sni=www.multiplydose.com&type=ws#@ArchiveTell%207
این کانفیگا UDP ساپورتن
@ArchiveTell</div>
<div class="tg-footer">👁️ 886 · <a href="https://t.me/archivetell/5380" target="_blank">📅 23:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کانفیگ sni spoofing
vless://1b69417d-afc8-4f26-ab5d-fcf515e68492@127.0.0.1:40443?alpn=h2%2Chttp%2F1.1&encryption=none&extra=%7B%22mode%22%3A%22auto%22%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&mode=auto&path=%2F&security=tls&sni=infinityservers.space&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/5379" target="_blank">📅 22:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚀
معرفی ابزار RM SNI Spoofer: دور زدن فیلترینگ با رابط گرافیکی (GUI)
---
رفقا اگر یادتون باشه قبلاً در مورد ایده جذاب SNI Spoofing (فریب دادن سیستم فیلترینگ با ارسال SNI تقلبی) از بچه‌های تیم Patterniha صحبت کردیم. حالا یک توسعه‌دهنده (rm-rfd) اومده و این پروژه رو کامل‌تر کرده و براش یک
رابط گرافیکی دسکتاپ (GUI)
ساخته!
💡
این ابزار دقیقاً چیکار می‌کنه؟
این برنامه قبل از اینکه ترافیک واقعیِ شما رو بفرسته، یک بستهِ تقلبیِ TLS (با یک SNI فیک و شماره توالیِ اشتباه) برای سیستم DPI (فیلترینگ) می‌فرسته. فیلترینگ با دیدن این بسته گول می‌خوره و مسیر رو باز می‌ذاره، اما سرور مقصد اون رو نادیده می‌گیره و دیتای اصلی شما بدون مشکل عبور می‌کنه!
✨
ویژگی‌های فوق‌العاده این نسخه جدید:
🔸
رابط کاربری گرافیکی (GUI):
دیگه نیازی به درگیری با محیط کنسول سیاه و کدهای پیچیده نیست؛ همه چیز با چند تا کلیک مدیریت میشه.
🔸
هسته داخلی Xray:
این برنامه خودش هسته Xray رو همراهش داره! یعنی خودش کانفیگ شما رو می‌خونه و بهتون پورت SOCKS5 و HTTP میده (عملاً بی‌نیاز از اجرای همزمان v2rayN).
🔸
مدیریت پروفایل‌ها:
می‌تونید چندین لینک مستقیم
vless://
یا
trojan://
رو داخلش ذخیره کنید و هر کدوم رو که خواستید Active کنید.
🔸
تست سلامت کانفیگ (Delay Test):
دقیقاً مثل کلاینت‌های استاندارد، می‌تونید از کانفیگ‌هاتون تست پینگ بگیرید تا ببینید کدوم سالم و سریع‌تره.
⚠️
نکات مهم برای استفاده:
- این برنامه فعلاً
فقط مخصوص ویندوز
هست.
- برای اجرای درست و دستکاری پکت‌ها (WinDivert)، حتماً باید برنامه رو با دسترسی ادمین (
Run as Administrator
) باز کنید.
- فقط از پورت ۴۴۳ برای ریموت پشتیبانی می‌کنه.
📥
لینک دانلود و دریافت نسخه اجرایی از گیت‌هاب:
🌐
https://github.com/rm-rfd/sni-spoofing-gui
📌
#معرفی_ابزار
#ویندوز
#SNI_Spoofing
#فیلترشکن
#تونل
#رابط_گرافیکی
#Xray
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/archivetell/5377" target="_blank">📅 22:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚀
آموزش اختصاصی: حل قطعی مشکل لاگین نشدن در Windscribe
---
رفقا تو شرایط فعلی، خیلی وقتا سرورهای Windscribe سالمن و کار می‌کنن، اما API لاگینش فیلتر شده و اصلاً نمی‌تونید وارد اکانتتون بشید.
امروز یه ترفند اختصاصی و تضمینی داریم که با ترکیب
Proxifier
و
سایفون (یا WhiteDNS)
این محدودیت رو دور بزنیم و با موفقیت لاگین کنیم.
🛠
پیش‌نیازها:
۱. برنامه Proxifier (برای تونل کردن ترافیک)
۲. برنامه Psiphon یا WhiteDNS
###
💻
مراحل انجام کار (قدم‌به‌قدم):
مرحله اول: آماده‌سازی مسیر
۱. برنامه سایفون (یا WhiteDNS) رو باز کنید و متصل بشید.
💡
نکته مهم:
اگر از سایفون استفاده می‌کنید، ریجن (Region) رو روی
سوئد (Sweden)
یا کشوری بذارید که مطمئنید سایتِ اصلی Windscribe رو بدون مشکل باز می‌کنه.
مرحله دوم: تنظیمات Proxifier
۱. برنامه
Proxifier
رو باز کنید.
۲. از منوی بالا برید به
Profile ➔ Proxy Servers
.
۳. روی
Add
کلیک کنید و آی‌پی لوکال سیستم (معمولاً
127.0.0.1
) و
پورتِ
سایفون یا WhiteDNS رو وارد کنید (پروتکل رو روی SOCKS5 یا HTTPS بسته به خروجی برنامه‌تون تنظیم کنید) و OK رو بزنید.
مرحله سوم: ساخت رول (Rule) برای وینداسکرایب
۱. حالا تو همون Proxifier برید به مسیر
Profile ➔ Proxification Rules
.
۲. روی دکمه
Add
کلیک کنید تا یک Rule جدید بسازیم.
۳. در کادر
Applications
، روی Browse کلیک کنید و فایل اجرایی وینداسکرایب یعنی
windscribe.exe
رو انتخاب کنید.
۴. در پایین همون صفحه در بخش
Action
، منوی کشویی رو باز کنید و اون پروکسی سروری که تو مرحله قبل (مربوط به سایفون/WhiteDNS) ساختید رو انتخاب کنید.
۵. همه پنجره‌ها رو OK کنید تا تنظیمات ذخیره بشه.
✅
مرحله نهایی:
تمام! حالا برنامه Windscribe رو باز کنید. الان ترافیکِ لاگینِ وینداسکرایب داره از تونلِ سایفون عبور می‌کنه. یوزر و پسوردتون رو بزنید و به راحتی لاگین بشید.
⚠️
توجه:
بعد از اینکه با موفقیت لاگین کردید، می‌تونید Proxifier و سایفون رو کامل ببندید و از خودِ Windscribe (با پروتکل‌هایی مثل WStunnel یا Stealth) به صورت عادی استفاده کنید.
📌
#آموزش_اختصاصی
#وینداسکرایب
#Windscribe
#پروکسی_فایر
#سایفون
#Bypass
#آموزش_شبکه
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/5376" target="_blank">📅 22:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
104.19.229.21
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
hcaptcha.com
"
}
🔻
کانفیگ موردنیاز :
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@127.0.0.1:40443?allowInsecure=1&ed=2560&eh=Sec-WebSocket-Protocol&encryption=none&host=sni.jpmj.dev&path=%2F&security=tls&sni=sni.jpmj.dev&type=ws#@ArchiveTell
آموزش sni spoofing
لینک داخلی V2rayn ویندوز
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/5375" target="_blank">📅 22:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5374">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">برای تونل شدن بازی‌ها و… با متود SNI SPOOF
یه روش که خودم تست کردم الان هم خیلی پایدار تره هم پینگش خوبه، هم میتونید به هر لوکیشنی که خواستید وصل بشید:
بعد از ران کردن اسپوف میتونید با
Se7en Pro
ترکیبش کنید (تو ستینگ برنامه قسمت Upstream Proxy
127.0.0.1:10808
) و باز تیک Allow lan بزنید تو ستینگ برنامش و تو گوشی به ادرس ایپی لپتاپ و پورتی که بهتون میده وصل بشید!
@NET_SPOOF
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/5374" target="_blank">📅 22:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5373">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ربات های سرچ تلگرام
@MotherSearchBot
@en_SearchBot
@SearcheeBot
@argo
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/archivetell/5373" target="_blank">📅 21:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5372">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آموزش بازی های انلاین با پینگ خوب برروی ویندوز با استفاده از روش SNI Spoofing
موارد مورد نیاز:
1-اتصال به Sni Spoofing
2-کلاینت V2ray
3-نرم افزار Windscribe که از قبل توش اکانت داشتید حتی اکانت فری و از قبل بهش لاگین کردید .(الان نمیشه بهش لاگین کرد اگه کسی روشی داره بگه بهمون )
شروع:
فرض بر این میگیریم شما با sni وصل هستید به اینترنت ازاد
روی v2ray پروکسی رو بذارید روی Clear system proxy و اصلا نباید حالت TUN روشن باشه .
حالا باید توی تنظمیات وایندسکرایب این تنظیمات رو اعمال کنید :
1-در بخش Connection روی split tunneling بزنید و بذارید روی Exclusive و در بخش app همون صفحه روی دکمه + بزنید و برنامه SNI SPOOFING رو پیدا کنید و اضافه ش کنید و مطمین بشید تیکش سبز باشه .
2-برگردید به بخش Connection و در قسمت Proxy setting و در بخش پروکسی تغییرش بدید به HTTP و ادرس و پورت زیر رو بذارید
127.0.0.1
10808
3-دوباره برگردید به بخش connection و Firewall رو بذارید روی حالت Manual
4- بخش conncetion Mode رو بذارید روی حالت manual و پروتوکل TCP و پورت 443
دقت کنید فقط پروتوکل TCP رو میتونید با این روش بهش وصل بشید و پینگ خوبی بهتون میده اگه اینترنت نرمالی داشته باشید .
سرور هم میتونید از المان فرانکفورت یا فرانسه جاردین استفاده کنید.
با این روش اینترنت شما مستقیم از وایندسکرایب گرفته میشه که هم اینترنت تمیزی بهتون میده که همه سایت ها و اپلیکیشن ها باز میشن هم پینگ خوبی بهتون میده .مطمینم میشه همین اینترنتو روی گوشی هم شیر کرد تا بتونید با اینترنت کامپیوترتون روی گوشی گیم بزنید ولی نمیدونم چجوری .
ویندسکرایب با هر ایمیل که بتونید وریفای کنید ماهانه 10 گیگ بهتون میده واسه گیم زدن کافیه فک کنم.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/archivetell/5372" target="_blank">📅 21:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrGmREJ8iQFMphhE3uE59DxxKIClhlPgipjsdVeula6kZCJ46HE8HAcpxprnLiMPNiEFWAxAqtPQK5UwJlcois7XRb73iEYRkFEUnoRW0ENBbTcd3l4lrrlarMCwzQWUjUAUb15zRbM-bjUxq7BItBTv9h6gTaKDBNfM04VB3CphaoLB9R_aNbxaEMdslCVybbtFHJnJCB9nX1GJv8P1T7G9gQY7FDiF9Kl5NOaa3sNbQVcnPcubxNFeaHD9pEiRpF2GvvgQfXbuRUhl9AQRqtfT4kqp9xpUhMZLpI_MPv_QXVX6rsh7sjZDq7TF8B95-Hia9uzVDUlfyFiQREbNog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان واسه اینکه کلا ترافیک سیستم رو بتونید از داخل تانل فیلترشکن رد کنید و نیاز به غیر فعال کردن هم نداشته باشید برای شبکه داخلی یه راه حل خوب استفاده از
Throne
هست، همون نکوری هست ولی توسعه اش ادامه پیدا کرده و خیلی بهترش کردن
گزینه  Tun رو فعال کنید، بعدش پروفایل ایران رو دانلود کنید و بعدش هم فعال کنید، اینجوری شبکه ایران از داخل تانل فیلترشکن رد نمیشه
خیلی خیلی هم بهتر جواب میده از همه لحاظ این کلاینت</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/archivetell/5371" target="_blank">📅 20:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">معکوس کردن ویدیو و صدا برای ایجاد ویدیوهای جادویی
Reverse Video - Apps on Google Play
با برنامه Reverse Video، می‌توانید به‌راحتی ویدیو و صدا را معکوس یا به جلو پخش کنید تا افکت‌های سرگرم‌کننده، شگفت‌انگیز و جادویی ایجاد کنید. بخواهید کسی را طوری نشان دهید که به عقب می‌پرد، آب را دوباره به لیوان برگرداند یا به صورت معکوس صحبت کند — این برنامه انجام این کارها را آسان و خلاقانه می‌کند.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/archivetell/5370" target="_blank">📅 19:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5369">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">📡
اشتراک‌گذاری اینترنت PC با گوشی (بدون نیاز به کانفیگ مجدد)
---
💡
رفقا، اگه کانفیگ (مثل SNI-SPOOF یا هر روش دیگه‌ای) روی سیستم (PC) براتون وصله، دیگه نیازی نیست روی گوشی هم جداگانه درگیرِ دور زدن فیلترینگ بشید! کافیه با یه تنظیم ساده، همون اینترنتِ آزاد رو مستقیم به اندروید و آیفون منتقل کنید.
⚠️
پیش‌نیاز خیلی مهم:
لپ‌تاپ/سیستم و گوشیِ شما باید دقیقاً به
یک مودم یا شبکه Wi-Fi
وصل باشن.
---
🖥
مرحله اول: آماده‌سازی v2rayN روی سیستم
۱. برنامه v2rayN رو باز کنید.
۲. از منوی بالا به مسیر
Settings ➔ Core Settings
برید.
۳. تیک گزینه
Allow LAN connections
رو فعال کنید و OK رو بزنید.
۴. از پایینِ صفحه اصلی v2rayN، پورتِ نوشته شده جلوی
Mixed Port
رو یادداشت کنید (معمولاً
10808
یا
10809
هست).
۵. حالا
CMD
ویندوز رو باز کنید و بنویسید:
ipconfig
۶. در اطلاعاتی که میاره، عددِ جلوی
IPv4 Address
رو یادداشت کنید (مثلاً
192.168.1.5
).
---
🤖
مرحله دوم: تنظیمات گوشی اندروید (Android)
۱. برید به تنظیمات وای‌فای (
Settings ➔ Wi-Fi
).
۲. روی اسم وای‌فای خودتون نگه دارید (یا آیکون چرخ‌دنده
⚙️
رو بزنید).
۳. گزینه
Edit
و بعد
Advanced options
رو انتخاب کنید.
۴. بخش Proxy رو روی حالت
Manual (دستی)
بذارید.
۵. حالا این اطلاعات رو وارد کنید:
•
Proxy hostname:
همون آدرس IPv4 سیستم (مثلاً
192.168.1.5
)
•
Proxy port:
همون پورت v2rayN (مثلاً
10808
یا
10809
)
۶. ذخیره (Save) کنید.
✅
تمام! الان مرورگر و اکثر اپ‌های اندرویدتون آزاد شدن.
---
🍎
مرحله سوم: تنظیمات گوشی آیفون (iOS)
۱. برید به تنظیمات وای‌فای (
Settings ➔ Wi-Fi
).
۲. روی آیکون (i) کنار اسم وای‌فای ضربه بزنید.
۳. بیاید پایین و
Configure Proxy
رو بزنید.
۴. روی حالت
Manual
قرار بدید.
۵. این اطلاعات رو وارد کنید:
•
Server:
آدرس IPv4 سیستم (مثلاً
192.168.1.5
)
•
Port:
پورت v2rayN (مثلاً
10808
یا
10809
)
۶. ذخیره (Save) کنید.
✅
تمام! آیفونتون هم از فیلترشکن لپ‌تاپ استفاده می‌کنه.
---
✈️
مرحله چهارم: وصل کردن تلگرام (بسیار مهم)
تلگرام پروکسیِ وای‌فایِ سیستم رو نادیده می‌گیره و باید جداگانه بهش پروکسی بدید:
۱. توی تلگرام برید به
Settings ➔ Data and Storage ➔ Proxy Settings
۲. روی Add Proxy بزنید و نوعش رو روی
SOCKS5
بذارید.
۳. اطلاعات رو وارد کنید:
•
Server:
آدرس IPv4 سیستم (مثلاً
192.168.1.5
)
•
Port:
همون پورت v2rayN (مثلاً
10808
)
۴. تیک ذخیره رو بزنید و فعالش کنید. تلگرام هم وصل شد!
---
⚠️
یک نکته مهم:
این روش فقط ترافیک رو پروکسی می‌کنه و تونل کامل (Full Tunnel) نیست:
•
✅
برای وب‌گردی، اینستاگرام، یوتیوب و دانلود کاملاً جواب میده.
•
❌
اما بعضی از گیم‌ها و اپلیکیشن‌های خاص ممکنه کار نکنن؛ برای اون‌ها باید کلاینت و کانفیگ رو مستقیماً روی خود گوشی نصب کنید.
📌
#آموزش
#شبکه
#ویندوز
#اندروید
#آیفون
#اشتراک_گذاری
#v2rayN
#پروکسی
#LAN
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/archivetell/5369" target="_blank">📅 19:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5368">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آموزش اشتراک گذاری sni spoofing رو گوشی
برای اشتراک گذاری همین کانفیگی که روی ویندوز متصل شدید به دیگر دستگاه ها مثل موبایل کافیه مراحل زیر را انجام بدید
ابتدا cmd ویندوز را باز کنید و دستور زیر را وارد کنید و اینتر بزنید :
ipconfig
در کادر ipv4 address ایپی مورد نظر را کپی کنید (این ایپی متغیر هست و هردفعه که ویندوز را ریستارت میکنید ممکنه تغییر کنه)
سپس در هر برنامه ای که روی اندروید یا ایفون دارید یک پروکسی socks5 یا http با مشخصات زیر بسازید :
Ip : YOUR WINDOWS IPV4 ADRRESS
این همون ipv4 address هست که مرحله قبل با دستور ipconfig گرفتید .
Port :10808
متصل بشید و لذت ببرید
نکته مهم:
سیستم و گوشی های مد نظر همه باید به یک اینترنت متصل باشند .
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/5368" target="_blank">📅 17:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🛠
حل مشکل قطعی SNI Spoofing در حالت TUN (در v2rayN)
---
رفقا سلام!
✋
اگر موقع استفاده از روش SNI Spoofing، وقتی v2rayN رو روی حالت TUN (تونل کل سیستم) می‌ذارید اتصالتون قطع میشه، علاوه بر روشی که بچه‌های تیم Patterniha گفتن، یه راه حل خیلی ساده و تمیز هم از داخل خودِ تنظیمات v2rayN وجود داره!
فقط کافیه یک روتینگ (Routing) مستقیم (Direct) برای آی‌پیِ مربوطه اضافه کنیم تا ترافیکش به مشکل نخوره.
🖥
مراحل تنظیم روتینگ:
۱. برنامه v2rayN رو باز کنید و از منوی بالا به مسیر
Settings ➔ Routing setting
برید.
۲. روی دکمه
Add
کلیک کنید تا یک پروفایل جدید ساخته بشه.
۳. در کادر
Remarks
یک اسم دلخواه بنویسید (مثلاً
direct-4-snispoof
).
۴. حالا در همون صفحه، روی
Add rule
کلیک کنید.
۵. در پنجره‌ای که باز میشه،
Remarks
رو برای نظم بیشتر روی همون آی‌پی بذارید (مثلاً
104.19.229.21
).
۶. گزینه
Rule Type
رو روی
ALL
قرار بدید.
۷. گزینه
outboundTag
رو حتماً روی
direct
تنظیم کنید.
۸. در کادر
port
، پورتی که SNI Spoof استفاده می‌کنه رو بنویسید (اکثراً
443
هست).
۹. برای
protocol
و
inboundTag
تیکِ همه‌ی گزینه‌ها رو بزنید.
۱۰. برای گزینه
network
هر دو مورد
tcp
و
udp
رو انتخاب کنید.
۱۱. حالا تو کادر بزرگِ
IP or IP CIDR
، همون آی‌پی‌ای که با SNI Spoof بهش وصل میشید رو بنویسید (مثلاً برای الان
104.19.229.21
هست).
۱۲. تو کادر
Domain
هم آدرس
hcaptcha.com
رو وارد کنید.
۱۳. در نهایت تمام پنجره‌ها رو
Confirm
کنید تا ذخیره بشن.
✅
مرحله آخر (فعال‌سازی):
حالا برگردید به صفحه اصلی برنامه. از همون نوار پایین برنامه (کنار جایی که پروکسی سیستم رو تنظیم می‌کنید)، منوی کشویی Routing رو باز کنید و اون پروفایلی که الان ساختید (direct-4-snispoof) رو انتخاب کنید. تمام! اینترنت بدون مشکل تونل میشه.
📌
#آموزش
#ویندوز
#v2rayN
#روتینگ
#Routing
#SNI_Spoofing
#تونل
#حل_مشکل
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/5367" target="_blank">📅 17:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">چیه همش با روش های رایگان وصل میشین؟؟؟
کانفیگ فروشا زن و بچه ندارن؟ زندگی ندارن؟ نباید ۲ تومن بیاد سر سفرشون؟
#طنز
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/5366" target="_blank">📅 17:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">شیر و خورشید همراه اول و آپتل وصل
- SNI:
yryirjrhqffsxwpg-a.akamaihd.net
- IP:
63.141.252.203
لینک داخلی شیر و خورشید
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/archivetell/5365" target="_blank">📅 16:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">trojan://humanity@127.0.0.1:40443?host=www.ignitelimit.com&path=%2Fassignment&sni=www.ignitelimit.com&type=ws#@ArchiveTell%201
trojan://humanity@127.0.0.1:40443?host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#@ArchiveTell%202
trojan://humanity@127.0.0.1:40443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#@ArchiveTell%203
trojan://humanity@127.0.0.1:40443?host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#@ArchiveTell%204
trojan://humanity@127.0.0.1:40443?alpn=http%2F1.1&host=www.calmloud.com&path=%2Fassignment&sni=www.calmloud.com&type=ws#@ArchiveTell%205
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#@ArchiveTell%206
trojan://humanity@127.0.0.1:40443?path=%2Fassignment&sni=www.multiplydose.com&type=ws#@ArchiveTell%207
این کانفیگا UDP ساپورتن
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/archivetell/5364" target="_blank">📅 16:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آموزش sni spoofing
کانفیگ ها ۱
|
کانفیگ ها ۲
لینک داخلی V2rayn ویندوز
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/5363" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">برای مک از ازین ریپو هم میتونید استفاده کنید
https://github.com/selfishblackberry177/sni-spoof/releases/
1. فایل دانلودی رو با config.json داخل یه دایرکتوری بگذارید
2. داخل ترمینال cd بزنید و دایرکتوری رو بیارید
3. sudo ./sni-spoof-darwin-arm64 config.json</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/archivetell/5362" target="_blank">📅 15:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">🍷
ورژن Python برای SNI Spoofing:
https://github.com/patterniha/SNI-Spoofing
ورژن Rust برای SNI Spoofing:
https://github.com/therealaleph/sni-spoofing-rust
ورژن Go برای SNI Spoofing:
https://github.com/aleskxyz/SNI-Spoofing-Go
ورژن اپ مک برای Sni spoofing:
https://github.com/g3ntrix/Cloak
👑
@ArchiveTell
💎
@xsfilterrnet</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/5361" target="_blank">📅 15:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel(𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣⚡️)</strong></div>
<div class="tg-text">🚀
معرفی ابزار FakeSNI: دور زدن فیلترینگ با تزریق SNI فیک (مخصوص لینوکس)
---
رفقا سلام!
✋
در پیرو پست قبلی که درباره مستقیم شدن دامنه hCaptcha و روش SNI Spoofing صحبت کردیم، حالا وقتشه یه ابزار عالی برای پیاده‌سازی این متد روی سیستم‌عامل لینوکس معرفی کنیم.
پروژه
FakeSNI
یه نسخه بازنویسی‌شده، سریع و بسیار تمیز از پروژه معروف
patterniha
هست که با زبان Go نوشته شده.
🔥
این ابزار چطور فیلترینگ رو دور می‌زنه؟
این برنامه روی لینوکس یه پروکسی TCP می‌سازه. دقیقاً بعد از اینکه دست‌دادنِ اولیه (TCP Handshake) با سرور انجام شد، این ابزار یه بسته حاوی
ClientHello
با یک SNI فیک (همون دامنه‌ای که فیلتر نیست مثل
hcaptcha.com
) رو به بیرون تزریق می‌کنه.
چون شماره توالی (Sequence Number) این بسته عمداً دستکاری شده، سرورِ مقصد اون رو دور می‌ندازه؛ اما سیستم فیلترینگ (DPI) وسط راه گولِ همون بسته رو می‌خوره، فکر می‌کنه سایت مجازی رو باز کردید و مسیر رو برای دیتای اصلیِ شما باز می‌ذاره!
🤯
🛠
پیش‌نیازها برای اجرای ابزار:
🔸
سیستم‌عامل لینوکس (Ubuntu, Debian و غیره)
🔸
داشتن دسترسی روت (Root)
🔸
فعال بودن
iptables
روی سیستم (که معمولاً روی همه لینوکس‌ها هست).
💻
نحوه استفاده خیلی ساده:
۱. سورس برنامه رو از گیت‌هاب دانلود یا بیلد کنید.
۲. یه فایل به اسم
config.json
بسازید و دقیقاً مثل پست قبلی، تنظیمات آی‌پی و SNI فیک رو توش قرار بدید.
۳. ابزار رو با دسترسی روت و دستور زیر اجرا کنید:
sudo ./fakesni -config config.json
(نکته: این ابزار خودش به صورت خودکار رول‌های iptables رو تنظیم و بعد از بسته شدن پاک می‌کنه).
🔗
لینک سورس کد و توضیحات کامل در گیت‌هاب سازنده:
🌐
https://github.com/PechenyeRU/FakeSNI
📌
#معرفی_ابزار
#لینوکس
#فیلترینگ
#اسنیف
#FakeSNI
#SNI_Spoofing
#DPI
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/archivetell/5360" target="_blank">📅 15:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">لینک داخلی V2rayn ویندوز
دانلود
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/5359" target="_blank">📅 15:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش استفاده از tun موقع استفاده از sni spoofing:  خیلیها سوال داشتند که چطور کل سیستم رو موقع استفاده از sni-spoofing تونل کنیم تا بازی ها و ... هم بتونن تونل شن. دقت کنید در این روش دیگه نیازی به سایفون و وینداسکریب و ... برای tun کردن کل سیستم نیست و مستقیم…</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/5358" target="_blank">📅 15:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش استفاده از tun موقع استفاده از sni spoofing:
خیلیها سوال داشتند که چطور کل سیستم رو موقع استفاده از sni-spoofing تونل کنیم تا بازی ها و ... هم بتونن تونل شن.
دقت کنید در این روش دیگه نیازی به سایفون و وینداسکریب و ... برای tun کردن کل سیستم نیست و مستقیم کانفیگتون به کل سیستم تونل میشه.
همچنین میتونید tun رو به راحتی شیر کنید تا دستگاههای دیگه (مثل ps و xbox  و ...) بدون نیاز به v2ray مستقیم از کانفیگ لپتاپ شما استفاده کنند.
۱. برای اینکار cmd را با run as admin  قبل از قرار دادن v2rayN در حالت tun اجرا کنید و سپس دستور زیر را اجرا کنید:
netsh interface ipv4 add route 104.19.229.21/32 "Wi-Fi" 192.168.1.1 metric=1
دقت کنید بعضی پارامترها را نیاز دارید تغییر دهید:
اول ۱۰۴.۱۹.۲۲۹.۲۱ باید همان connect_ip شما در sni_spoofing_by_patterniha باشد،
دوم "Wi-Fi" باید اسم اینترفیسی باشد که از آن اینترنت میگیرید و در صورتی که با وایفای متصلین معمولا همین "Wi-Fi" هست، به هر حال میتوانید با دستور ipconfig اسم اینترفیس رو هم ببینید.
سوم default-gateway هست که اگر به وای فای خانه وصلین معمولا همین
192.168.1.1
است و اگر با گوشی اینترنت رو برای لپتاپ شیر کردید default-gateway برابر ip گوشی میباشد، به هر حال مقدار default-gateway را میتوانید با استفاده از دستور ipconfig مشاهده کنید.
۲. در تنظیمات dns-settings در نرم افزار v2rayN مقدار remote-dns را برابر
https://dns.google/dns-query
قرار دهید (چون بسیاری از ورکر استفاده میکنند و ممکنه dns کلودفلر براشون در دسترس نباشه)  و حالت tun را فعال و استفاده کنید.
///
دقت کنید با ری استارت کردن کامپیوتر route اضافه شده پاک میشود و باید دوباره دستور را وارد کنید. (میتوانید با  اضافه کردن  store=persistent به دستور route رو به طور دائمی اضافه کنید ولی پیشنهاد نمیشود چون ip ممکن است عوض شود)
///
اگه شرایط پایدار بمونه تو ورژن ۲ این دستور رو به صورت خودکار اضافه میکنم و log رو هم درست میکنم.</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/archivetell/5357" target="_blank">📅 15:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
پروفایل های وایت دی ان اس (WhiteDNS)
❤️
تاریخ بروزرسانی : ۲ خرداد
👾
لینک دانلود
کلاینت :
3️⃣
WhiteDNS
1.5.1
3️⃣
Windows
|
Linux
|
Mac
1
.0.0 Beta3
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViihWSVAtMSkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidmlwMS5tYXNpci1zZWZpZC50ZWNoIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViihDSVAtMSkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiY2lwMS5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViihDSVAtMikiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiY2lwMi5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViihDSVAtMykiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiY2lwMy5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViihDSVAtNCkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiY2lwNC5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViihDSVAtNSkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiY2lwNS5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
⚡️
پک ریزالور
⬅️
فیلم
اموزش
اندروید
|
دسکتاپ
👌
آموزش ترکیب با برنامه ی نکوباکس
👍
آموزش ترکیب با برنامه npv
✉️
Channel |
@Masir_Sefid
| کانال
✉️</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/5356" target="_blank">📅 15:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">sub2.txt</div>
  <div class="tg-doc-extra">87.9 KB</div>
</div>
<a href="https://t.me/archivetell/5355" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">حدود 400 کانفیگ spoof همش پینگ داد واسه من. با
104.19.229.21
تقدیم به همتون
💪</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/archivetell/5355" target="_blank">📅 14:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SNI-Spoofing_by_patterniha_v1.rar</div>
  <div class="tg-doc-extra">9.8 MB</div>
</div>
<a href="https://t.me/archivetell/5354" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل برنامه رو ران از ادمین کنید(همین)
وصل شید این کانفیگ
trojan://humanity@127.0.0.1:40443?security=tls&sni=www.creationlong.org&fp=chrome&insecure=1&allowInsecure=1&type=ws&host=www.creationlong.org&path=%2Fassignment#archivetell</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/archivetell/5354" target="_blank">📅 14:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5353">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تشکر از دوستانی که نبض بازار کانکت شدنو تو دایرکت بما میگن
اگه چیزی میدونین کار میده اینا دایرکت پیام بذارین، تو چنل بذاریم
https://t.me/archivetell?direct</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/archivetell/5353" target="_blank">📅 14:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5352">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فرانسه برگشت
😁</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/5352" target="_blank">📅 14:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5351">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اسپوف کامبک..</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/5351" target="_blank">📅 14:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5350">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اینارو تست کنید
hcaptcha.com
https://www.hcaptcha.com/cdn-cgi/trace
اگر براتون هر کدوم اومد بدونید میتونید استفاده کنید
اینم آیپی ها برای تست
85.198.12.209
2.144.19.238
185.236.38.44
95.38.177.31
46.38.137.156
81.12.32.136
104.19.229.21
🔥
104.19.230.21
🔥</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/archivetell/5350" target="_blank">📅 14:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5349">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کانفیگ اسپوف
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@127.0.0.1:40443?allowInsecure=1&encryption=none&host=sni.111000.indevs.in&path=%2F%3FTelegram%D9%8B+%40ProxyVPN11&security=tls&sni=sni.111000.indevs.in&type=ws#%DB%B1
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@127.0.0.1:40443?allowInsecure=1&encryption=none&host=sni.latonyamadeline.ndjp.net&path=%2F%3Fhttps%3A%2F%2Ft.me%2FProxyVPN11%F0%9F%87%A8%F0%9F%87%B3%3D&security=tls&sni=sni.latonyamadeline.ndjp.net&type=ws#%DB%B2
trojan://humanity@127.0.0.1:40443?host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#%DB%B3
trojan://1710442808@127.0.0.1:40443?allowInsecure=1&host=subb.nrshop198.workers.dev&path=%2F&sni=subb.nrshop198.workers.dev&type=ws#%DB%B4
trojan://humanity@127.0.0.1:40443?alpn=h2%2Chttp%2F1.1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#%DB%B5
trojan://humanity@0.0.0.0:40443?allowInsecure=1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#%DB%B6
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.multiplydose.com&path=%2Fassignment&sni=www.multiplydose.com&type=ws#%DB%B7
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.ignitelimit.com&path=%2Fassignment&sni=www.ignitelimit.com&type=ws#%DB%B8
trojan://humanity@127.0.0.1:40443?allowInsecure=1&path=%2Fassignment&sni=www.multiplydose.com&type=ws#%DB%B9
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#%DB%B1%DB%B0</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/5349" target="_blank">📅 14:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5348">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
104.19.229.21
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
hcaptcha.com
"
}
رایتل تست شده ، بقیه نتا تست کنید</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/5348" target="_blank">📅 14:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5347">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اسپوف کامبک..</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/5347" target="_blank">📅 14:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5346">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">چنل سطح مقاومت 8 هزار رو رد کرده و احتمالا این سطح نقش حمایت رو در اینده ایفا خواهد کرد.
در روز گذشته یکی دوبار به سمت 8 هزار پولبک زد
انتظار میره در روز های آینده چنل سقف های قبلی رو بشکنه</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/archivetell/5346" target="_blank">📅 14:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5345">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این داستان گروه های ۲۰۱۶ قدیمی اینا چیه داستانش؟
😐
همش واسم سوال بوده</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/5345" target="_blank">📅 13:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5343">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">92.123.106.90
Google.com
اینم رو مودم ایرانسل وصله</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/archivetell/5343" target="_blank">📅 12:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5342">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">142.54.178.211
jkiysqntxacscicm-a.akamaihd.net
همراه اول وصله</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/archivetell/5342" target="_blank">📅 12:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5341">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آپدیت جدید شیر و خورشید
نصب کنید
قسمت آیپی و sni خالی بذارید ، بزنید اتصال ، خودش اسکن میکنه و وصل میشه</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/archivetell/5341" target="_blank">📅 11:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5340">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مخابرات  اوووف وصله  yryirjrhqffsxwpg-a.akamaihd.net  142.54.178.211  تشکر از یکی از ممبرا @ArchiveTell</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/archivetell/5340" target="_blank">📅 11:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5339">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">😐
😂
😂
مخابرات ظاهرا خیلی بده اگه جواب گرفتین بگین رو چه اپراتوری بهتره</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/archivetell/5339" target="_blank">📅 11:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5338">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2_gcY657sZ1qJMk2iuSF7J7J-eKDRaLMC8VuewoSIpsdIaNgV-_H0QbTdEPTVTit9wYHkYHl-OpkfAjdSVQfSHFM4kPCp0cb-DPoMMan7RhK5sxJj5waGrC5S8oL8vIsb1G0I7IB1TkTofrwpogw5Y5X8qzzDKyhIBr8yQwjQWoI25DCb7KlffHUBXJxp5_Y5HPO9y5pjjbULlfIeDpS1HJQkki53dc9rfSFSeZEMHmyPp4RBnlSBoH6YtTA2HCJwb6vQ0VvevDnHAvDKnSHikxVN7FG3wfQuI5VBAzjW0MU__H2VtcTz7Q2BebTkF4nrA-mu-kE1HywDSiNCKbbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
😂
😂
مخابرات ظاهرا خیلی بده
اگه جواب گرفتین بگین رو چه اپراتوری بهتره</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/5338" target="_blank">📅 10:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5337">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">لینک داخلی آپدیت شیر و خورشید
https://punkpaste.ir/f/ShirOKhorshid-2026-0-03iy5e
https://dl.toolschi.com/view.php?f=43accc69841b6088.zip
https://punkpaste.ir/f/ShirOKhorshid-2026-0-03iy5e</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/archivetell/5337" target="_blank">📅 10:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5336">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7znZUcTQX5A3A5hfCL1Kt2d4o8eUxIhnKegck_jSUeyQbVHWZlvMGXeogzVf2uZ8Y-hKbNMYnmb9-Mst4UeF_3aCKJt6DFrBRR3LDC9jL7AF7nB2Y2dKNvszefSR5PRyg8SM0nRPwHEqdHPAVes0Ke7uYcFv3J8HaCPv2vxd5A9kIdeE6YrFMSpULvrb9xIal3QQj5Aqtuzpv851tbXCUrjzQ81tsNzzLEChKX2jBcH7Pl2HU7jmZkotpnlKEWAyNGaDJ7o3EPSbo2bwJRj7qs5M5RZlhX8520iHyF0d7GUDmhsW64hwNRMi5kxllsDYHLuIiBcn1K2rrACsaPmXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثه قبل start بزنین تا اسکن کنه
و قبلش تنظیمات قدیمیِ IP و SNI رو از قسمت Settings برنامه کاملاً پاک کنید (خالی بذارید)</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/5336" target="_blank">📅 10:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5335">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.24.apk</div>
  <div class="tg-doc-extra">25 MB</div>
</div>
<a href="https://t.me/archivetell/5335" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/archivetell/5335" target="_blank">📅 10:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5333">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚀
آپدیت جدید کلاینت "شیر و خورشید" برای اندروید (نسخه 2026.05.24)
---
رفقا سلام!
✋
نسخه جدید و جذاب کلاینتِ شیر و خورشید منتشر شد. توی این آپدیت، تمرکز اصلی روی پیدا کردنِ آی‌پی‌های سالم و بهبود اتصال روی CDN Fronting بوده.
✨
تغییرات و امکانات جدید این نسخه:
🔸
اسکنر قدرتمند آی‌پی (IP Scanner):
برنامه حالا یک لیستِ بسیار بزرگ از آی‌پی‌های ممکن رو در خودش جا داده.
💡
نکته مهم:
اگر در اتصال مشکل دارید، پیشنهاد میشه تنظیمات قدیمیِ IP و SNI رو از قسمت Settings برنامه کاملاً پاک کنید (خالی بذارید) و اجازه بدید خود برنامه اسکن رو انجام بده. *(دقت کنید اسکنِ بار اول ممکنه خیلی طول بکشه، حتی چند ساعت! پس صبور باشید).*
🔸
بهبود اتصالات (CDN Fronting):
پروتکل‌های بیشتری که با CDN Fronting کار می‌کنن به برنامه اضافه شده؛ در نتیجه احتمالِ وصل شدن و سرعت کلیِ شما باید بهتر از قبل باشه. قابلیت Beast Mode هم برای کارکرد درست روی این حالت آپدیت شده.
🔸
تنظیمات حرفه‌ای LAN Proxy:
حالا می‌تونید «پورت» دلخواه خودتون رو برای پروکسی کردنِ شبکه خانگی (LAN) تنظیم کنید. همچنین امکان تعیین Username و Password اضافه شده تا امنیت بالا بره و فقط کسانی که رمز رو دارن بتونن تو شبکه بهتون وصل بشن.
🔸
خاموش کردن تبلیغ سایفون:
بالاخره قابلیت غیرفعال کردنِ سایتی که بعد از اتصال سایفون به صورت خودکار باز میشه، اضافه شد!
🔸
آپدیت هسته:
هسته‌ی اصلی نرم‌افزار (سایفون) به آخرین نسخه ارتقا پیدا کرده.
---
📥
دریافت آپدیت:
می‌تونید فایل نصب (APK) رو مستقیماً از لینک گیت‌هابِ زیر دانلود کنید. اگر از این ابزار استفاده می‌کنید و براتون وصل میشه، پست رو برای بقیه هم بفرستید تا استفاده کنن.
👇
🔗
https://github.com/shirokhorshid/shirokhorshid-android/releases/tag/v2026.05.24-a3b91cf
📌
#آپدیت
#شیر_و_خورشید
#سایفون
#فیلترشکن
#اندروید
#تونل
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/archivetell/5333" target="_blank">📅 10:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5332">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b4dd5d5da.mp4?token=KAagNREWj_rzmu7dej8CN3lpxuxfbfGDoPOV7wyYkMqclazbInKTqV3vDk1vpd-_yg3Np0aGf_fr-u5AY3HyiSuKrz4uy-rsosvJtvK57_SU7f97NdzcWRQljUHMSG99FxLnwsLIejniZrb9D_UWF7X6t9SFyzh-nNo-IXQ9YZlFfujOIWOHwyuvRiJ5vYCr2CvItATGVd9rW73_08MEuOnGTO0imuKdCLmiFc_cZais8OoOvrb5XEhg2YKt_JfSLNpKSoEiYKLBI5eBq3RBJg6hfWCx-GhPpdqS2kBlbttpLyw7QcZcxlL_OwLt2kxM8O0RoKG1P-62gk9tpnZL5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b4dd5d5da.mp4?token=KAagNREWj_rzmu7dej8CN3lpxuxfbfGDoPOV7wyYkMqclazbInKTqV3vDk1vpd-_yg3Np0aGf_fr-u5AY3HyiSuKrz4uy-rsosvJtvK57_SU7f97NdzcWRQljUHMSG99FxLnwsLIejniZrb9D_UWF7X6t9SFyzh-nNo-IXQ9YZlFfujOIWOHwyuvRiJ5vYCr2CvItATGVd9rW73_08MEuOnGTO0imuKdCLmiFc_cZais8OoOvrb5XEhg2YKt_JfSLNpKSoEiYKLBI5eBq3RBJg6hfWCx-GhPpdqS2kBlbttpLyw7QcZcxlL_OwLt2kxM8O0RoKG1P-62gk9tpnZL5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چت‌جی‌پی‌تی به سمت شخصی‌سازی بیشتر پیش می‌رود.
نسخه چت‌جی‌پی‌تی پلاس اکنون قابلیت بهره‌گیری از خاطرات، گفتگوهای پیشین و فایل‌های متصل به کاربر را دارا می‌باشد تا پاسخ‌های هوشمندانه‌تری ارائه دهد، بدون آنکه نیاز باشد زمینه گفتگو در هر بار مجدداً تکرار شود.
شرکت OpenAI همچنین مکانیزم‌های کنترلی برای مدیریت، به‌روزرسانی یا حذف اطلاعاتی که چت‌جی‌پی‌تی ذخیره می‌کند، اضافه نموده است.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/5332" target="_blank">📅 09:09 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5331">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3aa3af6eac.mp4?token=PCD3TkLckYTk50c_AhYopGyyeZzK16KX1v5kmkfw5vDK8x1A-3hc0I7EV9u6nhxRLI0LKZEtGy__GxHOdPVwbDjDbEvA0TQnnkitbtmKeR7k2BSPQHfzygBvNFqRUZSb7Ec-q78HjJ5Yeko0qtwytCqxFVuDo78z0LnIaCB9C9tmDtcxNVc__Cs1yMQCoghbE3pAg6T86SoLc30ML9GZKz-Qrxc6OP2M2yuopVcaybpneDXbrZ7QhZtocpsRdWN4kSTc1WfhJg_TCIwTQpr0-V6qCuc1ucPFEDlop0zg1fry0dnD0o7oVQUHN674_aECHkzBe_KwXyMMWDWD8ZtsGw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3aa3af6eac.mp4?token=PCD3TkLckYTk50c_AhYopGyyeZzK16KX1v5kmkfw5vDK8x1A-3hc0I7EV9u6nhxRLI0LKZEtGy__GxHOdPVwbDjDbEvA0TQnnkitbtmKeR7k2BSPQHfzygBvNFqRUZSb7Ec-q78HjJ5Yeko0qtwytCqxFVuDo78z0LnIaCB9C9tmDtcxNVc__Cs1yMQCoghbE3pAg6T86SoLc30ML9GZKz-Qrxc6OP2M2yuopVcaybpneDXbrZ7QhZtocpsRdWN4kSTc1WfhJg_TCIwTQpr0-V6qCuc1ucPFEDlop0zg1fry0dnD0o7oVQUHN674_aECHkzBe_KwXyMMWDWD8ZtsGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
مایکروسافت AI Engineer Coach را به صورت اوپن‌سورس منتشر کرده است — افزونه‌ای برای VS Code، Cursor و Antigravity که کارایی عوامل هوش مصنوعی شما را به حداکثر می‌رساند.
https://github.com/microsoft/AI-Engineering-Coach
کارهایی که انجام می‌دهد:
• لاگ‌های محلی جلسات را از GitHub Copilot، Claude Code، Codex CLI، OpenCode و Xcode می‌خواند.
• جریان کاری شما را بر اساس ۵ پارامتر ارزیابی می‌کند، از جمله کیفیت پرامپت‌ها و مدیریت زمینه.
• بر اساس پایگاه داده‌ای شامل ۴۵ الگوی خطا بررسی می‌کند: مثلاً سوختن غیرضروری توکن‌ها یا جلسات خیلی طولانی.
• همه قوانین بررسی را در فایل‌های معمولی Markdown (.md) ذخیره می‌کند تا به راحتی قابل اصلاح باشند.
• الگوهای تکراری در پرامپت‌ها را پیدا کرده و آن‌ها را به مهارت‌هایی برای عوامل هوش مصنوعی تبدیل می‌کند.
در نهایت، سیستمی بهینه‌شده برای اتوماسیون هر پروژه‌ای از شما به دست می‌آید.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/5331" target="_blank">📅 09:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5330">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">trojan://humanity@45.89.221.111:443?path=%2Fassignment&sni=www.ignitelimit.com&type=ws#ArchiveTell%20
مخابرات و آسیاتک وصل</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/archivetell/5330" target="_blank">📅 02:27 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5329">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">قیمت لحظه ای‌ کریپتو های معروف در تلگرام  https://t.me/addlist/X6c9tOtZoLhkZTAy</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/archivetell/5329" target="_blank">📅 01:49 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5328">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4726a7517b.mp4?token=l1NVbRleMF3hWJOuI3K-5akUS0mhQqbgyRkT9J7wr-yJtGxcjxjxk_zusbCIj5HZtBzRfdfAaYU9bfOVSgjuTPx1NDW1S4HuxQwcHLMKeHIpQKBpiYJRaF9bz0S0TVcf2te4WbjyPfAZJ-LTsPK8L7VUVYJq0j3tms023XQ87EbzqmPKtId1CcPutxaS2pqupP9G111X1mzcbk7aTZeKU9fYza2nG-FnQpHQsmNsevCFsbuMYQ4sebmaXAhlRR0gQxY9bkCClxfbmEi0Gs92iVA32Wgf8sBwz1975DiAlEDLlHehrqwp8HXsW04FYDZHTNfID9oFUcyNcBDSKyH2MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4726a7517b.mp4?token=l1NVbRleMF3hWJOuI3K-5akUS0mhQqbgyRkT9J7wr-yJtGxcjxjxk_zusbCIj5HZtBzRfdfAaYU9bfOVSgjuTPx1NDW1S4HuxQwcHLMKeHIpQKBpiYJRaF9bz0S0TVcf2te4WbjyPfAZJ-LTsPK8L7VUVYJq0j3tms023XQ87EbzqmPKtId1CcPutxaS2pqupP9G111X1mzcbk7aTZeKU9fYza2nG-FnQpHQsmNsevCFsbuMYQ4sebmaXAhlRR0gQxY9bkCClxfbmEi0Gs92iVA32Wgf8sBwz1975DiAlEDLlHehrqwp8HXsW04FYDZHTNfID9oFUcyNcBDSKyH2MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نرخ تتر: 167,600 تومان ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ تاریخ: 1405/03/03 ساعت: 01:10</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/archivetell/5328" target="_blank">📅 01:42 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5327">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c57ee64b0.mp4?token=MULtvhp3pBy_kelxU483em3k1FxpOHTqdrL36INfivWhl74iKuCNm6jFuPElJUkqxAarsedQpf1n63gXtDZmupq1r6kN2nYQk37bFKaV7TOdJPf62cMYWlrLy3QS_karcs9lv29-HHBK6EmcY_8IU_NgOFV3RtdLBss9IBAcJu0JzYyo8349kUsHu2m2loq9DM8bezZUWl-YM1KKS9oRQCmbsA2yagD6992LS7fwlUReuXnFmq50b3W-zA9Mtr7J3cHuB5fhHRcGCWVdJjA83Jryw4yXxi_UdR2LJUHAnqJw5Q2qzMW1OW0eMBKTxGpTxgNjXejtIcERjQyxEdnzmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c57ee64b0.mp4?token=MULtvhp3pBy_kelxU483em3k1FxpOHTqdrL36INfivWhl74iKuCNm6jFuPElJUkqxAarsedQpf1n63gXtDZmupq1r6kN2nYQk37bFKaV7TOdJPf62cMYWlrLy3QS_karcs9lv29-HHBK6EmcY_8IU_NgOFV3RtdLBss9IBAcJu0JzYyo8349kUsHu2m2loq9DM8bezZUWl-YM1KKS9oRQCmbsA2yagD6992LS7fwlUReuXnFmq50b3W-zA9Mtr7J3cHuB5fhHRcGCWVdJjA83Jryw4yXxi_UdR2LJUHAnqJw5Q2qzMW1OW0eMBKTxGpTxgNjXejtIcERjQyxEdnzmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت الان :</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/archivetell/5327" target="_blank">📅 01:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5325">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نرخ تتر: 167,600 تومان
ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
تاریخ: 1405/03/03
ساعت: 01:10</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/archivetell/5325" target="_blank">📅 01:18 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5324">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e97817b2.mp4?token=RQz4pvJPmgocsrOtoyCiSGlo8xfYmdU-iSFL5G2x97yWQ2K0oW36OUFe_3pU4sV9J8Y_-vI48gIOwRYCCSJpgbitZQjwGeQ0sik6eS0XTN3rrfmTtVEfJRR_XNmOBrED1y_F9EtKEpS_fsnSPGUPZcfsLJNaeXg4Gb16AJrwodzknwDTRzpb0Tc4SfL0hXuUk-XHZna6Q9TX2vE60OJoFcjsFpjny6A_thTdO_hB1GvKvifrAbPtZ_7pVQxyovU-6dP31iGmfTiNjXosDWv0NY8UqLgIC0PdAtZiPGpLpPPOZqiVxzO_6NOPj4cqjHp9cccZo7ia7n1GkcJlZKGsNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e97817b2.mp4?token=RQz4pvJPmgocsrOtoyCiSGlo8xfYmdU-iSFL5G2x97yWQ2K0oW36OUFe_3pU4sV9J8Y_-vI48gIOwRYCCSJpgbitZQjwGeQ0sik6eS0XTN3rrfmTtVEfJRR_XNmOBrED1y_F9EtKEpS_fsnSPGUPZcfsLJNaeXg4Gb16AJrwodzknwDTRzpb0Tc4SfL0hXuUk-XHZna6Q9TX2vE60OJoFcjsFpjny6A_thTdO_hB1GvKvifrAbPtZ_7pVQxyovU-6dP31iGmfTiNjXosDWv0NY8UqLgIC0PdAtZiPGpLpPPOZqiVxzO_6NOPj4cqjHp9cccZo7ia7n1GkcJlZKGsNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب دوستان قراره سنگین بزنن</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/archivetell/5324" target="_blank">📅 01:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5323">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4024c3c872.mp4?token=NhOxMmyVvjrsEarNZ7Ix0twcTMOUepzubdY5E0c3xikU2u8lkNXlNbareGzBqliOD7aZbaHa6gfcDVjXZSWzvXulHAUiy1bOB-R_QdYl6lK0hYqK8gAhu4d_cHNza7PXUaUIWOt4COxgenQ_stPpwY-1npjBRlHFGaUrm3c5M4tWU_biXfu3mvWewhXuum_6TIx4cXurf9McDwV3v6Onmv93BeDgdWbre9IcLV7xX0HcuhLwDmATqnZ_Bdxjgi-LJtG1kixqeR1p6rpNZkq8KtTuJGoqMZXJdxM4bcKU1nr_ED8i4AFriPwb0Lb_f3VMAHcQg_F81Csf6t5tMrnvSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4024c3c872.mp4?token=NhOxMmyVvjrsEarNZ7Ix0twcTMOUepzubdY5E0c3xikU2u8lkNXlNbareGzBqliOD7aZbaHa6gfcDVjXZSWzvXulHAUiy1bOB-R_QdYl6lK0hYqK8gAhu4d_cHNza7PXUaUIWOt4COxgenQ_stPpwY-1npjBRlHFGaUrm3c5M4tWU_biXfu3mvWewhXuum_6TIx4cXurf9McDwV3v6Onmv93BeDgdWbre9IcLV7xX0HcuhLwDmATqnZ_Bdxjgi-LJtG1kixqeR1p6rpNZkq8KtTuJGoqMZXJdxM4bcKU1nr_ED8i4AFriPwb0Lb_f3VMAHcQg_F81Csf6t5tMrnvSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/archivetell/5323" target="_blank">📅 00:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5322">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خب دوستان قراره سنگین بزنن</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/archivetell/5322" target="_blank">📅 00:44 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
