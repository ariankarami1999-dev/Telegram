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
<p>@archivetell • 👥 8.49K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 17:41:59</div>
<hr>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">vless://478cc26d-16b3-4fdd-be64-60d5a58c1622@162.159.36.5:80?encryption=none&host=tt.andishehparenting.com&path=%2F&security=none&type=ws#@ArchiveTell
مخابرات ، آسیاتک و شاتل
@ArchiveTell</div>
<div class="tg-footer">👁️ 679 · <a href="https://t.me/archivetell/5492" target="_blank">📅 17:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">trojan://8r%3C%5B9%27l6hAO%238ZQi@95.85.28.102:2053?host=Koma-YT.PAGeS.Dev&path=%2FtrTelegram%F0%9F%87%A8%F0%9F%87%B3%2B%40WangCai2&sni=Koma-YT.PAGeS.Dev&type=ws#@ArchiveTell%201
trojan://8r%3C%5B9%27l6hAO%238ZQi@57.129.47.56:2053?host=Koma-YT.PAGeS.Dev&path=%2FtrTelegram%F0%9F%87%A8%F0%9F%87%B3%2B%40WangCai2&sni=Koma-YT.PAGeS.Dev&type=ws#@ArchiveTell%202
trojan://8r%3C%5B9%27l6hAO%238ZQi@95.85.11.18:2087?host=Koma-YT.PAGeS.Dev&path=%2FtrTelegram%F0%9F%87%A8%F0%9F%87%B3%2B%40WangCai2&sni=Koma-YT.PAGeS.Dev&type=ws#@ArchiveTell%203
مخابرات ، آسیاتک و شاتل
@ArchiveTell</div>
<div class="tg-footer">👁️ 769 · <a href="https://t.me/archivetell/5491" target="_blank">📅 17:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سامانتل کجایی که ببینی مخابرات و آسیاتک وصل شده
😁</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/archivetell/5490" target="_blank">📅 17:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دایرکت کانال چند نفر گفتن فیبر نوری ایرانسل هم وصل شده..</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/archivetell/5489" target="_blank">📅 17:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oAq5xE7ib_CXvGCqsS3OE2jG_bwWy8SBdHHZdW7igEkguP05dFq4Pv8vKoU-xEWGJI9p-5SocQMJ4jd9xpkwHGAo6vMUUPex8Qoh7HEAHh8pa5-_azkjlQiMSru9TZrZNLK7UNsoWn9rHap3lp-a7szvdoHS1f6BvKF7DhieqDiEvijdnIGAfwyu2TT1uZEY0wluGfXj7anXIUMO5q_pIANFOmPmPJO_oIGSy3KnsjtPJe9-6TqbnDWlVvUE1b189FasqQWtaVC3C3skR6IA5wOpKV9CB3gd99dVXGYQe6Bk-cc8rA9g8SdqSz2EbNpp-dNxzk56Bjs8Wf8P64eXlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخابرات توییتر بدون فیلتر میاره..
آیپی ایران انداخته
😁</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/5488" target="_blank">📅 16:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مخابرات یوتیوب بدون فیلتر میاره..</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/5487" target="_blank">📅 16:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آسیاتک و مخابرات
trojan://8r%3C%5B9%27l6hAO%238ZQi@104.21.7.21:2096?allowInsecure=1&host=Koma-YT.PAGeS.Dev&path=%2Ftr&sni=Koma-YT.PAGeS.Dev&type=ws#%F0%9F%87%A8%F0%9F%87%A6%20Canada%20(CA)%20-%20Toronto%20@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/5486" target="_blank">📅 16:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سایفون رو اینترنت مخابرات وصل شد ...</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/5485" target="_blank">📅 16:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مخابرات و آسیاتک
trojan://8r%3C%5B9%27l6hAO%238ZQi@speedtest.net:2096?allowInsecure=1&host=Koma-YT.PAGeS.Dev&path=%2Ftr&sni=Koma-YT.PAGeS.Dev&type=ws#%F0%9F%87%A8%F0%9F%87%A6%20Canada%20(CA)%20-%20Toronto%20@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/5484" target="_blank">📅 16:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مخابرات و آسیاتک
trojan://8r%3C%5B9%27l6hAO%238ZQi@172.66.47.69:2096?allowInsecure=1&host=Koma-YT.PAGeS.Dev&path=%2Ftr&sni=Koma-YT.PAGeS.Dev&type=ws#%F0%9F%87%A8%F0%9F%87%A6%20Canada%20(CA)%20-%20Toronto%20@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/5481" target="_blank">📅 16:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انگار آسیاتک و مخابرات وصل شدن بعضی فیلترا..</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5480" target="_blank">📅 16:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">صدای انفجار در نزدیکی مجتمع Config Sellers
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/archivetell/5479" target="_blank">📅 15:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اپ استور رفع فیلتر شده..
پ.ن: بسته شد</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5478" target="_blank">📅 15:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #87</div>
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
"address": "104.18.20.213",
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
ترکیبی سایفون یا شیر و خورشید با v2ray
آموزش
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/5477" target="_blank">📅 15:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdc6654627.mp4?token=jP1dj20s9A6ILEON6trJZptUehwPK-0bkjDVsuD_KGlnupMkcjdGctFx81r8og1e4Qk4-PGBrYIkO16icppbEz1vRIcLSPeTWwX3RtVnMOxotjjL4YT4_-1UiN-ecOIhZGtgD5ujSP2wSlbB2K_8dxl7qmDrRTbJYk2Iu4-avEWo1svyrrP-jLHAKG-3nxrvclxk03QD09xyQTd2KlEwM_QfKgDflyVPBQ79WpRcabPlVXB30ShxgBo-SmFc7uKf4XMSbU53_ux5e0wWthFC10vtNiFziNQcELzirs6Rd70Q1nZEmLwfyDxS0-vxjrqx1XuBVwgiNnlxwv80bD5oeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdc6654627.mp4?token=jP1dj20s9A6ILEON6trJZptUehwPK-0bkjDVsuD_KGlnupMkcjdGctFx81r8og1e4Qk4-PGBrYIkO16icppbEz1vRIcLSPeTWwX3RtVnMOxotjjL4YT4_-1UiN-ecOIhZGtgD5ujSP2wSlbB2K_8dxl7qmDrRTbJYk2Iu4-avEWo1svyrrP-jLHAKG-3nxrvclxk03QD09xyQTd2KlEwM_QfKgDflyVPBQ79WpRcabPlVXB30ShxgBo-SmFc7uKf4XMSbU53_ux5e0wWthFC10vtNiFziNQcELzirs6Rd70Q1nZEmLwfyDxS0-vxjrqx1XuBVwgiNnlxwv80bD5oeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/archivetell/5476" target="_blank">📅 15:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKMUVJknxq-q-uVUX4Vk4V5uKPOW8Ycd0wT603QvAvPYGcV3epqM52Q9N5j5rlN1HqigDuIRGX-woSrySBy6L4z4_TaFrZE6E81D6EbSVkeHQ3d8EleaL1TPziHNe9W8E1E4M0wYQKcKK_FWquysxOWR0MHp8ixfwCMtYIxVdsJ26HegqYso1wUAP1n-Ef_edxynEA8QG2kI5fsX5ABEDcXuquGZItC3_CBAyyDDvKtMh5_MJjbIpPTYELiUvSgjAs4VMtRoqUdOUnB-0rK7MZRTZMmyp7g1M3HLQ9FoN46Pse6xpVaMk1OTi4bELchUZTUGpIQp4R4NJKYeRXeMxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالله
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/5475" target="_blank">📅 15:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ی چهارتا سوراخو فقط باز میکنن هیچ چیز به عقب برنمیگرده نظر من</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/archivetell/5474" target="_blank">📅 15:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">{ "_comment": { "remark": "@ArchiveTell" }, "log": { "access": "", "error": "", "loglevel": "info", "dnsLog": false }, "inbounds": [ { "tag": "in_proxy", "port": 1080, "protocol": "socks", "listen": "0.0.0.0", "settings": { "auth": "noauth", "udp": true, "userLevel":…</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/archivetell/5473" target="_blank">📅 15:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">{
"_comment": {
"remark": "
@ArchiveTell
"
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
"listen": "
0.0.0.0
",
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
"address": "
104.18.12.149
",
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
"Host": "
www.calmloud.com
"
}
},
"tlsSettings": {
"allowInsecure": true,
"serverName": "
www.calmloud.com
",
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
"
8.8.8.8
"
]
},
"routing": {
"domainStrategy": "UseIp",
"rules": [],
"balancers": []
}
}
این وصله</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/archivetell/5472" target="_blank">📅 15:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">@SHADOW_CONFBOT  کانفیگ رایگان کلادفلر و باقی سی دی ان ها، فایل هارو بگیرید و آیپی تمیز رو جایگزین کنین  برخی کانفیگ ها شاید تموم شده باشن پس تست بزنید و آیپی جایگذاری کنین</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/5471" target="_blank">📅 15:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">@SHADOW_CONFBOT
کانفیگ رایگان کلادفلر و باقی سی دی ان ها، فایل هارو بگیرید و آیپی تمیز رو جایگزین کنین
برخی کانفیگ ها شاید تموم شده باشن پس تست بزنید و آیپی جایگذاری کنین</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/5470" target="_blank">📅 15:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">چند دقیقه وصل کردن تا حرف پزشکیان رو هوا نمونه
😁</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/5469" target="_blank">📅 15:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">قطع شد..</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/5468" target="_blank">📅 15:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">همه نتا وصله
trojan://8r%3C%5B9%27l6hAO%238ZQi@104.16.89.120:2096?host=Koma-YT.PAGeS.Dev&path=%2Ftr&sni=Koma-YT.PAGeS.Dev&type=ws#
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/5467" target="_blank">📅 15:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">همه نتا وصله
trojan://humanity@104.16.89.120:443?host=www.multiplydose.com&path=%2Fassignment&sni=www.multiplydose.com&type=ws#
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/5466" target="_blank">📅 15:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اونایی که ورکر دارن ، این آیپی استفاده کنن
104.16.7.70
اپیوس و ...</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/5465" target="_blank">📅 15:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">trojan://humanity@104.16.7.70:443?host=www.multiplydose.com&path=%2Fassignment&sni=www.multiplydose.com&type=ws#
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/5464" target="_blank">📅 15:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">trojan://8r%3C%5B9%27l6hAO%238ZQi@104.16.7.70:2096?allowInsecure=1&host=Koma-YT.PAGeS.Dev&path=%2Ftr&sni=Koma-YT.PAGeS.Dev&type=ws#%F0%9F%87%A8%F0%9F%87%A6%20Canada%20(CA)%20-%20Toronto%20@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/5463" target="_blank">📅 15:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">vless://388a6c57-87e7-420b-afe2-b3eb670fd7da@104.16.7.70:80?encryption=none&host=vip.yaml7.ggff.net&path=%2F+%40ProxyVPN11&security=none&type=ws#
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/5462" target="_blank">📅 15:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">vless://06ef598c-1555-4887-b3f9-08214a2f6792@104.16.7.70:443?encryption=none&host=2026.hhhhh.eu.org&path=%2F222.167.202.31%3A7443&security=tls&sni=2026.hhhhh.eu.org&type=ws#
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/5461" target="_blank">📅 15:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.7.70:8443?allowInsecure=1&encryption=none&host=sni.111000.dynv6.net&path=%2F%3FTelegram%F0%9F%87%A8%F0%9F%87%B3%2B%40WangCai2&security=tls&sni=sni.111000.dynv6.net&type=ws#
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/5460" target="_blank">📅 15:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">trojan://humanity@104.18.139.67:443?allowInsecure=1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/5459" target="_blank">📅 14:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ایرانسل ، رایتل و مخابرات وصله..</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/5458" target="_blank">📅 14:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">trojan://humanity@104.18.139.67:443?allowInsecure=1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/5457" target="_blank">📅 14:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وای فای وصله   trojan://humanity@104.16.7.70:443?allowInsecure=1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/5456" target="_blank">📅 14:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وای فای وصله
trojan://humanity@104.16.7.70:443?allowInsecure=1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/5455" target="_blank">📅 14:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کانفیگ SNI Spoofing با لوکیشن های مختلف
Finland:
vless://cbf524f0-4d7c-4173-aafb-e9f0608b3192@127.0.0.1:40443?alpn=h2%2Chttp%2F1.1%2Ch3&encryption=none&host=focalin.yhbj.store&mode=auto&path=%2FGoorbeh&security=tls&sni=focalin.yhbj.store&type=xhttp#@ArchiveTell%20Finland
Germany:
vless://a01daac7-1e65-4645-854d-b47d226f6b08@127.0.0.1:40443?encryption=none&host=y6-3cj.PAgES.DEV&path=%2F&security=tls&sni=y6-3cj.PAgES.DEV&type=ws#@ArchiveTell%20Germany%20
France:
trojan://humanity@127.0.0.1:40443?path=%2Fassignment&sni=www.ignitelimit.com&type=ws#@ArchiveTell%20France%20
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/5454" target="_blank">📅 13:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #63</div>
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
"address": "172.64.152.23",
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
ترکیبی سایفون یا شیر و خورشید با v2ray
آموزش
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/5453" target="_blank">📅 11:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ی چهارتا سوراخو فقط باز میکنن
هیچ چیز به عقب برنمیگرده
نظر من</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/5452" target="_blank">📅 11:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔥
آموزش اجرای روش جدید SNI-Spoofing (ابزار ZeroDPI) برای ویندوز و اندروید
---
رفقا سلام!
✋
ابزار جدید و فوق‌العاده‌ای به اسم
ZeroDPI
منتشر شده که به زبان قدرتمند Rust نوشته شده و می‌تونه محدودیت‌های فیلترینگ (مثل مسدود بودن کانفیگ‌های مستقیم) رو به زیبایی و شفافیتِ تمام دور بزنه.
این ابزار با روش‌های پیشرفته‌ای مثل (TLS SNI Spoofing) بستهِ فیلترینگ رو فریب میده و اینترنت آزاد رو در اختیارتون می‌ذاره. سرعت بالا و پایداری از مهم‌ترین ویژگی‌های این روشه.
💻
مرحله اول: دانلود و راه‌اندازی ZeroDPI روی ویندوز
۱. کلاینت ZeroDPI (نسخه ویندوز) رو مستقیماً از گیت‌هاب دانلود و اکسترکت کنید:
🔗
https://github.com/nullroute1970/ZeroDPI/releases/download/v0.1.0-20260525T092918Z-bd03a3d79aa4/zerodpi-windows-x86_64.zip
۲. فایل
config.toml
رو باز کنید و مقادیر زیر رو دقیقاً به این شکل تغییر بدید و سیو کنید:
LISTEN_HOST = "0.0.0.0"
LISTEN_PORT = 40443
SCAN_TIMEOUT_SECS = 20
۳. فایل
zerodpi.exe
رو کلیک راست کرده و حتماً با
Run as administrator
اجرا کنید. صبر کنید تا تست اولیه تموم بشه و لیست SNIها بالا بیاد؛ روی همون گزینه اول اِنتر (Enter) بزنید. حالا ZeroDPI آماده‌ست!
---
📥
مرحله دوم: پیدا کردن کانفیگ‌های سالم
۱. وارد این مخزن کالکتور بشید:
🔗
https://github.com/Delta-Kronecker/V2ray-Config
۲. از جدول اول، یکی از گروه‌های ۵۰۰ تایی رو باز کنید. کانفیگ‌ها رو کپی کنید و داخل برنامه
v2rayN
پیست (Paste) کنید.
۳.
تنظیم تست سرعت:
تو v2rayN برید به
Settings ➔ Option Settings ➔ v2rayN settings
و آدرس
Speed test URL
رو برابر مقدار زیر قرار بدید:
https://cachefly.cachefly.net/1mb.test
۴. حالا کانفیگ‌ها رو تو دسته‌های ۱۰۰ تایی انتخاب کنید و کلید
Ctrl+T
(یا کلیک راست و Real ping) رو بزنید. بر اساس پینگ مرتب‌شون کنید.
۵. اونایی که پینگ دادن رو انتخاب کنید و کلید
Ctrl+D
(تست دانلود) رو بزنید. هر کدوم که عددِ دانلود رو نشون داد، یعنی وصل میشه. روش دابل کلیک کنید تا فعال بشه.
⚠️
نکته بسیار مهم:
حتماً روی حالت
System Proxy
بذارید و حالت TUN رو خاموش کنید!
---
📱
مرحله سوم: اشتراک‌گذاری اینترنت آزاد به اندروید (بدون نیاز به کانفیگ روی گوشی)
اگر می‌خواید گوشی‌تون هم بدون دردسر وصل بشه (دقت کنید گوشی و لپ‌تاپ باید به یک وای‌فای وصل باشن):
۱. تو ویندوز،
CMD
رو باز کنید و بنویسید
ipconfig
. عددِ جلوی
IPv4 Address
رو یادداشت کنید.
۲. برگردید تو v2rayN؛ روی همون کانفیگی که الان بهش وصلید، دابل‌کلیک کنید تا ادیت بشه.
۳. مقدارِ
Address
رو از
127.0.0.1
پاک کنید و اون آدرس IPv4 (مرحله ۱) رو جاش بنویسید و ذخیره کنید.
۴. حالا روی همون کانفیگ کلیک راست کنید و گزینه
Share
رو بزنید.
۵. بارکدی (QR Code) که میده رو با برنامه v2rayNG گوشیتون اسکن کنید و بهش وصل بشید!
✅
تمام.
اگه جایی به مشکل خوردید، تو کامنت‌ها بنویسید.
👇
📌
#آموزش
#ویندوز
#اندروید
#SNI_Spoofing
#تونل
#فیلترشکن
#ZeroDPI
#v2rayN
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/5451" target="_blank">📅 10:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">trojan://humanity@127.0.0.1:40443?host=www.ignitelimit.com&path=%2Fassignment&sni=www.ignitelimit.com&type=ws#@ArchiveTell%201
trojan://humanity@127.0.0.1:40443?host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#@ArchiveTell%202
trojan://humanity@127.0.0.1:40443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#@ArchiveTell%203
trojan://humanity@127.0.0.1:40443?host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#@ArchiveTell%204
trojan://humanity@127.0.0.1:40443?alpn=http%2F1.1&host=www.calmloud.com&path=%2Fassignment&sni=www.calmloud.com&type=ws#@ArchiveTell%205
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#@ArchiveTell%206
trojan://humanity@127.0.0.1:40443?path=%2Fassignment&sni=www.multiplydose.com&type=ws#@ArchiveTell%207
کانفیگ های UDP واسه SNI Spoofing
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/archivetell/5450" target="_blank">📅 09:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">لینک داخلی
سایفون اندروید
سایفون ویندوز
شیر و خورشید
Mahsang
تلگرام ویندوز
تلگرام اندروید نسخه سایت
تلگرام اندروید نسخه گوگل پلی</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/5449" target="_blank">📅 08:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #58</div>
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
"address": "172.64.152.23",
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
ترکیبی سایفون یا شیر و خورشید با v2ray
آموزش
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/5448" target="_blank">📅 08:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #57</div>
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
"address": "104.18.12.149",
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
ترکیبی سایفون یا شیر و خورشید با v2ray
آموزش
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/archivetell/5447" target="_blank">📅 08:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">لینک داخلی Mahsang
دانلود</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/5446" target="_blank">📅 08:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">با سایفون ِ داخلی‌ش سر و کله نزنید. روش سنتی و راحت:
برید داخل Settings مهسا و Mode رو بذارید رو Proxy only،
داخل اپ سایفون / شیر و خورشید اپ مهسا رو اکسکلود کنید (که مشمول وی‌پی‌ان نباشه)،
هاست و پورت رو هم بدید:
127.0.0.1
10809
حالا اول یکی از دو کانفیگ مذکور رو داخل مهسا ران کنید (با دکمه‌ی M پایین برنامه)، و بعدش سایفون / شیر و خورشید رو. والسلام</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/5445" target="_blank">📅 08:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXTp9D6-mCjLhbQs5HBgzYfbShYfpoVjj72u0UvcIhnZHvD0hLULFeT2VtQ3cyB1dRfjg115OYS9oC-XUvVyFlPxA-b9hkAliq3uUVtkG3ULYVri6P6uvJE83GkfYAyA278GyFXu9xvfML9xA0hnCDJc_r7rZvDuu3Mw6zSOXI7aVaUr9Pb4OGqNLoGECm29ZYB7VMyIdhI4WTEsUwSdRpQadOeYJ4sJn22PDi2DaRzbDI_g7M_O4jtKRAoqcuLUlhlOvNyegIxaWJQrjRfFLet4j6L4D3Om9exW4iyNGJiAYS-H1Xu06iRrwg5tSC2oBLdO61yROoNML8zQxfBdbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VeyL-NQp5a0TusFodU6aCFHZuylZUh9o3R8P-WCT1WXTyDYM_hNvcy0q5qbf-XC93fIlrC8UXZf4TTkvJzUPAUdK5NmMW2sabhdZNj3S_Wv7acN4lrRSG8h_bD6BIn_Mrkd-EjhckrfYaWjMSDtOLLxiJrsQt7OP9ue5ewFWqGt-IY6RsxBCxNtj0KxlCaKE78kZTZOG-u0uEmpaMJDyf3iNgOA-AMj8XjvpUO2VV1tLxQ8RgSLM89DZCwfDMKUIekLVUsFnHSLwStGZSgPHppHaqLbxphZt4x_4_tZyMSEJePY-YBZ9ioDZxRG3KPQd_d8W6QTjQYXSP1WOK6zKew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این روش رو تست کردم فوق العاده است بذارید کانال
اگر کلاینت MahsaNG رو دارید انجام بدید وصل میشه
لینک داخلی
اگر سایت گیتهاب براتون باز هست:
از منوی برنامه مهسا ان جی، اورژانسی EMS، کانفیگ دریافت کنید
دو عدد کانفیگ ترکیبی مشاهده میکنید یکی رو انتخاب کنید
در تنظیمات سایفون Protocol رو روی Auto بذارید و Aggressive رو ON کنید و Save بزنید
دکمه psiphon-after از منوی F رو روشن کنید و Save بزنید
نیازی به روشن کردن فرگمنت از منوی F نیست
دکمه M رو روشن کنید و 30 ثانیه صبر کنید تا سایفون متصل بشه. پینگ بگیرید و از کانفیگ رایگان لذت ببرید
زحمت ایت این آموزش رو این عزیز کشیده
@Khode3ilent</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/5443" target="_blank">📅 08:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">داداش درسته که قبلا هم چند جا نوشتن ولی باز بنویسی و یادآوری کنی بد نیست.  اینکه حتما pass key بذارن رو اکانتشون تا اگه تلگرام انداخت بیرون بتونن باهاش دوباره لاگین کنن. چون ممکنه اس ام اسش نیاد و نتونن مجدد وارد اکانتشون بشن.</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/5442" target="_blank">📅 03:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5441">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑯𝑶3𝑬𝑰𝑵 . 𝑹</strong></div>
<div class="tg-text">داداش درسته که قبلا هم چند جا نوشتن ولی باز بنویسی و یادآوری کنی بد نیست.
اینکه حتما pass key بذارن رو اکانتشون تا اگه تلگرام انداخت بیرون بتونن باهاش دوباره لاگین کنن. چون ممکنه اس ام اسش نیاد و نتونن مجدد وارد اکانتشون بشن.</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/archivetell/5441" target="_blank">📅 03:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5440">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ظاهرا انقد ایپیای بیگ کور کثیف و لجنه (در واقع شده) که تلگرام پرت میکنه بیرون
لاگ اوت
—-
اکانت نمیپره
منظورم اونایی با روش اسپوفینگ ایپی وصلن یا کانفیگشو دارن</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/archivetell/5440" target="_blank">📅 01:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">در مورد کانفیگ humanity
این کانفیگ رو اولین بار آقا فرید کانال
@appxa
گذاشت ، از ایشون باید تشکر کنید بابت این کانفیگ ، بعد همه جا پخش شد
یه عده فاز برداشتن که انگار مال خودشونه
😁
تذکر میدم که حد خودتون رو بدونید.</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/archivetell/5439" target="_blank">📅 00:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5438">
<div class="tg-post-header">📌 پیام #49</div>
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
"address": "104.16.80.73",
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
ترکیبی سایفون یا شیر و خورشید با v2ray
آموزش</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/archivetell/5438" target="_blank">📅 00:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_qSY9la52yDGwYRIhotm8YZL6XVo6ZU4-mlqUKZ3a62NlvuojxK-350N0yg-VMUKWv_IvOiezDmzJv-chXI2NKa7xweikjBKmY3hkvaz8gHXhSC3_sFN1XR6EHAGxhpKshpc6lH-omvBtLV-CssSe3SH1dg2qIneGr0GNNrZkOveveJU216HMHnHw3X_eSZajVrEYI3w9adiv_Mds8b6MuvfjKq3AMv13WvxS0VkSO70FunfiB38KoZr2leL8ZBBdISeX21AuKJbD3UShmB3urzFBnWVgjXw7qCJnmKAkvZq6PZVgki9ZjhWwMZp_UDbwoufjlmEa9ukvZfTKWubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tbQ3e_9CMGiiZcGttzLEEF6fIazyMDOS3L2lj3BR1t0Zb6n7hbQ-6eHVeBRHYtV23At3BTb0Y_3P-nBZzS--miihjMU4x2RRydZ6hzlGWDxu2q8mub8M_w3DWlzEBqPjcUMYHz3a03R3siWr10ZdzQDkFPtNbI4ZIHvfYxjgYXUyadnW7eNAeLcQoDqYL7dKUTL_wJLIChGWuv-pAaoTWL_oY6WsCkOx5CJCbeb73adku9RruUS2peh3exGLbT8PK3QKU5L55SWPtGcJX1-SwY8-0VE1Ee5tZazKyfeLFydEdDF2620dk_nP4XkEYpB9iym-B8nsKwHSXekiTKlKpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اتصال ترکیبی ویتوری + شیر و خورشید.
برنامه رو بزارید رو حالت Auto
1. هر چی ip و sni گذاشتید حذف کنید.
2. از تنظیمات پروکسی http رو بزارید روی
127.0.0.1
10808
3. برید به قسمت don't tunnel selected apps و برنامه ویتوری رو تیک بزنید.
4. برنامه ویتوری رو بزارید رو حالت پروکسی مود و به
کانفیگ مخصوص
وصل بشید
5. حالا برید شیر و خورشید رو استارت کنید. زیر ۳۰ ثانیه وصله
@APPXA
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/5436" target="_blank">📅 23:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/5435" target="_blank">📅 23:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/archivetell/5434" target="_blank">📅 23:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">این آیپی
شیر و خورشید روی آپتل وصله
142.54.178.211</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/5433" target="_blank">📅 23:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5428">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/5428" target="_blank">📅 21:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نکوباکس رسمی نیست تا جایی میدونم
تست ویروس بودن هم چیزی تشخیص داده نشد
ولی بازم مسئولیتش با خودتون</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/archivetell/5427" target="_blank">📅 21:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/archivetell/5426" target="_blank">📅 21:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5425" target="_blank">📅 21:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/5423" target="_blank">📅 21:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/archivetell/5422" target="_blank">📅 21:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5420" target="_blank">📅 21:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/5419" target="_blank">📅 21:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">@ArchiveTell تون ماهی</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/5418" target="_blank">📅 21:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ساخت ویدئو های سینمایی که واقعا شبیه صحنه های فیلم به نظر میرسند
🎬
⚡
🌐
https://higgsfield.ai
@ArchiveTell
#VideoAI
#AITools</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/5417" target="_blank">📅 20:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5414">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDDKft--pfMspQI0i3hUXjluvJMC9GZaedKXokh3ET_I8h1u9o3uyI2ovnunMI2_VDSL6S84flZRvkgdoj0bYkEXp2Psxrp0nWVFMs7S1jH6eVPZVC_z1WYmIQZfGpHC30zdvAU_tLM2rXCDYcoX_VJtYhwD9YdGK_N9OCTpb8MYBnvaRz_XOPpH8nQfztZ8zyhEKHaUCMYQcuQvwk0aWrk-VFOMMM_VcZGYCjQUDWrg3ITboi9BfO2PlyyNAT3AilV0U1q0TqNS5l_bU2HPGu2ktriUzDYDC3TqWpKnPiE4BuU9omXzY9WY6bEfRVuSe8oSig2PMSVgME25VHo-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@ArchiveTell
تون ماهی</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/archivetell/5414" target="_blank">📅 19:50 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMehrsan</strong></div>
<div class="tg-text">امیدوارم یه روز همه اینا چیزی جز یه خاطره ازشون نمونه و دیگه مجبور نباشیم بخاطر حقمون انقد زحمت بکشیم</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/archivetell/5413" target="_blank">📅 19:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from❖Ƭʜᴇᴍᴀʜᴅɪ</strong></div>
<div class="tg-text">من که نت وصل بشه بازم به همین شیرخورشید وصل میشم
یا sni spoof میزنم برای خودم
رایگانه بدون تبلیغه سرعتشم بد نیست
کسخلم پول بدم؟</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/archivetell/5412" target="_blank">📅 19:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/5411" target="_blank">📅 19:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شیر و خورشید همه نتا وصل  CDN edge IPs :  185.141.106.238 185.50.37.52 80.191.243.226 164.138.17.122 185.88.178.196 109.72.197.1 78.39.234.140 5.160.128.142  CDN SNI hostname: snapp.ir  Beast Mode : روشن   لینک داخلی شیر و خورشید   @ArchiveTell</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/5410" target="_blank">📅 19:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3OWikqUPl3m1Ula-LSI03fr3b1YTbpz4fN9BCwZQJBcSERaR8WVwtTVvAxYFJrd2G3syeP7S8n2MRBLfgcw2OrXlHLOsfs3cTCzeWuIyDn0F0DOgcTnb5DV06cB65pEL_Eyq8Us6ItLvIgdoUYlcKRUF9PoyEoCO9NQE7QD9c_XTIF2oyTnPx0SJhhkcTy7Eh-0vCavx_BZCvePuh6m2Z5UpozDiHEyc-PdZDup5s5X8nTRzACC1nFMBFy6WN3fdDv0RK6f0elV0P-D4MPKb7mxO_vgf1EBReVbHn5ybCzWtT7W9jQZo6mbM5AtILADFYq_6rEi0136VmF8i1g1bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیر و خورشید همه نتا وصل  CDN edge IPs :  185.141.106.238 185.50.37.52 80.191.243.226 164.138.17.122 185.88.178.196 109.72.197.1 78.39.234.140 5.160.128.142  CDN SNI hostname: snapp.ir  Beast Mode : روشن   لینک داخلی شیر و خورشید   @ArchiveTell</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/archivetell/5409" target="_blank">📅 19:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/archivetell/5408" target="_blank">📅 19:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترکیبی سایفون و v2ray
vless://aaaaaabb-4ddd-4eee-9fff-ffffffffffff@188.114.96.4:443?allowInsecure=1&alpn=http%2F1.1&encryption=none&path=%2F43.218.77.16%3D443&security=tls&sni=JoinProxyVPN11.afrcloud4.c01.kr&type=ws#@ArchiveTell</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/5407" target="_blank">📅 18:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترکیبی سایفون و v2ray
trojan://humanity@188.114.96.4:443?allowInsecure=1&alpn=http%2F1.1&path=%2Fassignment&sni=www.calmloud.com&type=ws#@ArchiveTell</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/5406" target="_blank">📅 17:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/archivetell/5404" target="_blank">📅 16:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مخابرات وصل
vless://8c4604ef-749c-4b56-adf1-7da405002a21@2.144.4.154:40443?encryption=none&host=qyi.fqjd663.ggff.net&path=%2F&security=tls&sni=qyi.fqjd663.ggff.net&type=ws#@ArchiveTell</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/archivetell/5403" target="_blank">📅 16:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/archivetell/5402" target="_blank">📅 14:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نرم افزار دانلود از گوگل درایو
https://abrehamrahi.ir/o/public/W9uUu9PS/
لینک های درایو رو بردارین و داخلش پیست کنین و منتظر بشین تا دانلود تموم شه.
ربات های تبدیل فایل به لینک گوگل درایو:
@TheGdriveXBot
@File_linkerobot
@GDrive_Uploader_Robot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/archivetell/5401" target="_blank">📅 14:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کرم کتاب داریم اینجا؟ Annas-Archive  خیلی طول میکشه تا PDF ازش دانلود بشه جایگزین چیزی هست؟ Libgen قدیم خوب بود</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/archivetell/5400" target="_blank">📅 14:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کرم کتاب داریم اینجا؟
Annas-Archive
خیلی طول میکشه تا PDF ازش دانلود بشه
جایگزین چیزی هست؟
Libgen قدیم خوب بود</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/5399" target="_blank">📅 14:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5398">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/archivetell/5398" target="_blank">📅 13:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nrp9WH-VGuKw7O_4LChfGRoDMin729qxseemZAnqBBAech6LF7by0Sw5nFuGBmJD1BqQa5zoj6j2aNq1B8lloF4IMt4lzEAOnMqDLkVtGGPRWdgobRCNIBeKa79JfNF3BSpVvddOXX-RPjODR6MzdY9g95Slyqm2x0DvHsQg6WZaBOTpQvv7AR7WI0eq8iNaRVwxYU9Tcqe_pkNec3ouojLURAyyl1y6bZ8vEAU7UjQ9XrdvWBRx-Bx85LjJ-9B2OrhsbY3Jj6hZWwoFBo3dSla08203pfmpWBgFTnlelfFwb6NShkgcj-S1LtxszOmnFXiPC0czYyx7ByvktVam3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
FileShare یه ابزار ساده برای اشتراک‌گذاری فایل توی شبکه محلیه. با این برنامه می‌تونی فایل‌ها رو روی سیستم خودت آپلود کنی و از یه دستگاه دیگه داخل همون شبکه، خیلی راحت دانلودشون کنی.
✅
کارش اینه: - فایل را می‌فرستی داخل ابزار - برنامه فایل را ذخیره می‌کند…</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/5397" target="_blank">📅 13:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سایت جدید film2media
film2media
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/archivetell/5396" target="_blank">📅 12:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/5395" target="_blank">📅 12:31 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مخابرات وصل
socks5://81.12.24.237:24845#(WIFI)</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/5394" target="_blank">📅 12:14 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/archivetell/5393" target="_blank">📅 12:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYE5D5r3DLFcpxWONXpSWcFZqHjdY7sc3H_ufVE9ohYTqBxLwwNAmDvQp1WbuHRDFkGhReqZc5n7DVpPfcBhhr-NSbnZrDW8FR9Wa5XEYVNZJrruFrmeii0PdJDAAEQvK_2W9U07TVqx5nrkDrIMMSCD7C-WXA9HhElLKqYjs10lJ55JbMngOgzI4pHaFHx9y97eIbxIp6yACF4eb93XgED9-24_O0igbwH3lQ4YHrI_gBrqUOadGEqPBuU-71Ws_vvyViz20AEox36kMJoXMoMXRGakTTaj7F2ZPv8UonEr1smv5F1N-ExQJ4vJ8YPg--_F5SWZ5ZS-hMDYr6l1bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔬
برای Claude Code مجموعه‌ای از بیش از ۳۰ عامل هوش مصنوعی ساخته شده است که مقالات علمی می‌نویسند — آن‌ها ایده خام را به مقاله آماده، پروژه کلاسی، گزارش یا حتی پایان‌نامه تبدیل می‌کنند.
https://github.com/Imbad0202/academic-research-skills
این عوامل از طریق arXiv، Semantic Scholar و DBLP تحقیق عمیقی انجام می‌دهند، مقاله را مرحله به مرحله می‌نویسند، کیفیت را ارزیابی می‌کنند، صحت اطلاعات را بررسی می‌کنند و نتیجه را به فرمت‌های APA، IEEE، MLA و دیگر فرمت‌ها صادر می‌کنند.
@ArchiveTell
#Claude</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/5392" target="_blank">📅 11:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaBmFqVPVvWmNbeCQavS0qE8-y7e8OBSDBu5_ibbCe71Rkxj2mOLCiUoyG4lj0a5z5K70-98vOnJ-A2xmQZ_nSFpeSk-WKxfCXdjJWwLmT9MaD39pT83NqBFQ_LQjWm7vuFu3qi2-a7GPSU-UqUDFvbgPISrORnTCvzWVCffEhDAXS92OWskab6m8LBmucCWY45QQ87pPzL3LdQoq_zwyiCqZ7I4OQsScNFoFVhTn5p7ewU1g-oBEXhxXRPzkYysYWr2mTusF_ssDpyXnW9yPooCxgGQewn_QBs8M3_YqVGrzYEAuEDTF2pi5TBVCtgXGRWBmPn7a8eSR6FZ2KdJXKuY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaBmFqVPVvWmNbeCQavS0qE8-y7e8OBSDBu5_ibbCe71Rkxj2mOLCiUoyG4lj0a5z5K70-98vOnJ-A2xmQZ_nSFpeSk-WKxfCXdjJWwLmT9MaD39pT83NqBFQ_LQjWm7vuFu3qi2-a7GPSU-UqUDFvbgPISrORnTCvzWVCffEhDAXS92OWskab6m8LBmucCWY45QQ87pPzL3LdQoq_zwyiCqZ7I4OQsScNFoFVhTn5p7ewU1g-oBEXhxXRPzkYysYWr2mTusF_ssDpyXnW9yPooCxgGQewn_QBs8M3_YqVGrzYEAuEDTF2pi5TBVCtgXGRWBmPn7a8eSR6FZ2KdJXKuY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/archivetell/5391" target="_blank">📅 11:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54f6977bbd.mp4?token=VNXHPnUD9LqxwJ1fxl2VRfg41J5jtzK3YJxEP5GvbOz5Jm3c4IskLxOF5ejIV8RGv4ELfmmYDCdQMvSwtK45JZXAsMjFyT0hvoc3gOnSVclgPQtSx8TW-8XQCf6ztLfPyweyUr5gEGs9eJ5rReubttpS0ajGAmVNQDzADlu7yaVS7mmkNgQSE0wD7ugAsPrvjkJnjrqiw5RVT6cJjQ-QUAKllBDEOIfHnIvynaf5AB8mubzj2_YpG8EbJGoXaebINNLLYZDR0qu7AoRFzuA5wSKFHLbdcpJzQ-jCW6tiVMQYdkkDZeb-8DQAP1Tj_lkuKACfypaJ2a-gwGkntPNqkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54f6977bbd.mp4?token=VNXHPnUD9LqxwJ1fxl2VRfg41J5jtzK3YJxEP5GvbOz5Jm3c4IskLxOF5ejIV8RGv4ELfmmYDCdQMvSwtK45JZXAsMjFyT0hvoc3gOnSVclgPQtSx8TW-8XQCf6ztLfPyweyUr5gEGs9eJ5rReubttpS0ajGAmVNQDzADlu7yaVS7mmkNgQSE0wD7ugAsPrvjkJnjrqiw5RVT6cJjQ-QUAKllBDEOIfHnIvynaf5AB8mubzj2_YpG8EbJGoXaebINNLLYZDR0qu7AoRFzuA5wSKFHLbdcpJzQ-jCW6tiVMQYdkkDZeb-8DQAP1Tj_lkuKACfypaJ2a-gwGkntPNqkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از وقتی اینترنت قطع شده انلاین شاپا دست به هرکاری میزنن بتونن جنساشونو بفروشن
😂
😂
😂
😂
😂
بابا اینترنتو وصل کنید
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/5390" target="_blank">📅 11:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANyhkUs1rgbZBk2aISNGpSz_AmY3F-HnjIJpV_FO1dfSEkEKtvu2YtmBaCd5LfUPiKN22E_kinHfLUMu917yA6QAF8zrw1X9A6-WG9qFmvNhcFpG7ZVa22iHN8VOz9g0yVBXIGk1JpMUXmzjJLIZ8EVwny0mC70d9TOjU-Yq5UAjMDPdLUfvtW4SCaXvEILWrSEKUMMC-FnGfxNDE4VVkGl1gWpFbzLWTBblNAJalIkCmEppxW8ftc_CgJFV5epO_vM_UTAFozu2hRfRgAtg9ol9OySaaRUNWpRNUPz3C-4MECA4H6gYPdU6I5Bwx6Ic9diSpb8bKaBmtzzpnaEqWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@ilovepdfs_bot
خار و مادر ور رفتن با pdf
یسری قابلیتاش رایگانه
یسری هم پولیه
با رفرال میشه برای تایم محدود قابلیتاشو باز کرد</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/5389" target="_blank">📅 11:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بررسی میزان تمیز بودن آیپی:   https://www.ipqualityscore.com/ip-reputation-check    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/5388" target="_blank">📅 10:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بررسی میزان تمیز بودن آیپی:
https://www.ipqualityscore.com/ip-reputation-check
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/archivetell/5387" target="_blank">📅 10:50 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/archivetell/5386" target="_blank">📅 09:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مخابرات وصله
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@95.38.164.245:40443?allowInsecure=1&encryption=none&host=sni.111000.indevs.in&path=%2F%3FTelegram%D9%8B+%40ProxyVPN11&security=tls&sni=sni.111000.indevs.in&type=ws#@ArchiveTell</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/archivetell/5384" target="_blank">📅 07:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">95.38.164.245
40443
بزنید رو کانفیگای کلود
مخابرات وصله</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/archivetell/5383" target="_blank">📅 07:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/5382" target="_blank">📅 00:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/archivetell/5381" target="_blank">📅 00:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 946 · <a href="https://t.me/archivetell/5380" target="_blank">📅 23:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانفیگ sni spoofing
vless://1b69417d-afc8-4f26-ab5d-fcf515e68492@127.0.0.1:40443?alpn=h2%2Chttp%2F1.1&encryption=none&extra=%7B%22mode%22%3A%22auto%22%2C%22scMaxEachPostBytes%22%3A%221000000%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&mode=auto&path=%2F&security=tls&sni=infinityservers.space&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/archivetell/5379" target="_blank">📅 22:59 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
