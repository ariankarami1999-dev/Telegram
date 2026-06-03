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
<img src="https://cdn4.telesco.pe/file/mvMcJRyrS2eTv0jnQLnXqZ9NihBjieK3Y8hXWZ-wpEeBoWLuMc78r_1wZ91yPzmtIqF7LH4MiDwOXOAiADI3d7F5cpNynmQMmWF3uyPtp4kpyAw-PzvRNKwnjhZgVujUSmjNqzHFoTrZNt80pN0YNK1CwnolrYJr71Nxk17dZX36rpPwC0t0QkoxmJNdI4vA02ERKme-48yiHCNKi51o4Hmad56xGg3BPMGuM3v-78EaBqsKSrdD2FSX9eB5k-tTV4Dad0xihOZMvSLLe2mymL2_DvdREfRdlRTkPuSAazET_1iy3AYdIEleMtfj8bE_4ANL2xUtzrmJFwmmeu9Z6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 40.4K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 10:49:23</div>
<hr>

<div class="tg-post" id="msg-8766">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دوستانی که مشکل داشتند تمام پیام های پیوی پشتیبانی دستم خورد پاک شد، خواهشا اگه مشکلی داشتین مجدد پیام بدین مشکلتونو برطرف کنم، شرمنده از طریق پشتیبانی ربات اقدام کنید حتما
❤️</div>
<div class="tg-footer">👁️ 487 · <a href="https://t.me/IranProxyV2/8766" target="_blank">📅 10:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8765">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldeON9dKCihOCCs8yOZQ2CxK0TiiVXKLNvkfzoVeO7hGtJlbwE6FeMLeN4r8VYJMYn4jAaKqsU0bN36qGSY5aaCoUddbGRDeBkkC7TkVU_puF4GngIZeUoIA2R7e8ptT0JDXXJRT2_Dh1cyhhUaFQ--BLQyrjmYBTGbgE5Nhn19djjJI1YlNsrhxV8OhdKbeN3qOA2Kuq17tqJuWL_tCOc_e2LaRLb54w6WWPfnvwpUdPmPOs1QgDELa6WtCKT7zxmnFY_Tn9m0kNvJdFS38wI1TwaKnbIjBe22V-XWa8ZhtzkU1p--2j1KR-eWmVqLX-9c-LzApeBBf-qAmUWGP5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانل پرسرعت آیپی آلمان تو ربات موجود شده فقط گیگی 20 هزار
🇩🇪
⚡️
10GB=200T
⚠️
دوستان 50 تا تست ۱٠٠ مگابایتی ۱ روزه تو ربات موجود شده ، سرعت تست کنید درصورت رضایت میتونید سفارشتتونو ثبت کنید
❤️
💥
@RUSSIAPROXYY_Bot
💎
آیدی ربات جهت ثبت سفارش
👆🏻</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/IranProxyV2/8765" target="_blank">📅 08:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8764">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">‎⁨متصل و‌مناسب📮⁩.npvt</div>
  <div class="tg-doc-extra">2.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8764" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
🦁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/IranProxyV2/8764" target="_blank">📅 08:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8763">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">Telegram Proxy
tg://proxy?server=204.168.152.124&port=8443&secret=dd104462821249bd7ac519130220c25d09
tg://proxy?server=95.216.149.83&port=155&secret=FgMBAgABAAH8AxOG4kw63Q
tg://proxy?server=37.27.192.10&port=8443&secret=dd104462821249bd7ac519130220c25d09
tg://proxy?server=95.216.191.201&port=443&secret=dd104462821249bd7ac519130220c25d09
tg://proxy?server=66.163.127.176&port=8443&secret=ee20215347364b59b09c1ab722bcc1d0d36d656469612e737465616d706f77657265642e636f6d
tg://proxy?server=166.0.122.22&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=87.248.129.12&port=15&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
https://t.me/proxy?server=ams1.tlgfast.com&port=443&secret=083fe0c452e2407d835537872f097c54
https://t.me/proxy?server=proxy.speedbreaker.info&port=25565&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
tg://proxy?server=166.0.122.22&port=4515&secret=eee9a4f23b1d768c04a8d7f39120ca5b6e626973636f7474692e79656b74616e65742e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/IranProxyV2/8763" target="_blank">📅 08:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8762">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">eblis.npvt</div>
  <div class="tg-doc-extra">11.8 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8762" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
💎
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/IranProxyV2/8762" target="_blank">📅 08:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8761">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صدای توافق💥🚀.npvt</div>
  <div class="tg-doc-extra">25.1 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8761" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
🏅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/IranProxyV2/8761" target="_blank">📅 07:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8760">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">حجم بالا♥️.npvt</div>
  <div class="tg-doc-extra">18.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8760" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
🌟
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/IranProxyV2/8760" target="_blank">📅 07:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8759">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Tunnel3🎖️.npvt</div>
  <div class="tg-doc-extra">52.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8759" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
💦
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/IranProxyV2/8759" target="_blank">📅 07:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8758">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🇩🇪.npvt</div>
  <div class="tg-doc-extra">5.1 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8758" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
🌿
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/IranProxyV2/8758" target="_blank">📅 07:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8757">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1ترابایت.npvt</div>
  <div class="tg-doc-extra">1.5 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8757" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
🩶
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/IranProxyV2/8757" target="_blank">📅 06:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8756">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPDeqEpPAvwiWWBiA_3D8SkfTPZFrWO-n3vRA4wFzscDizjjmhMmodV-OYNlmwtoYhvmwjT5fMhyxR905xjGNR19L-DFoq3EHZX_rmFpVggW_TR7ApnO0aaNfXPXye1hPtXMFd6U0exJqt2kF5qPpDBPi-G9O5uWhVgExjIfNm3hxvdOnn3e_8BRo8H0ydnC2UUDxcKus8cL0FXDlcbj0HNeF6biHxyS9fWj4uQCuqIFEyZcML2HsByJH5cFC-1EPqQpDtHFkPgM5T9YEfHRE5wCb_FCUXDq29r_L_XOhtkvcsca7CuHOI0Dc7FGmCWVbAv1qOAOcduFgn3BnxSJAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانل پرسرعت آیپی آلمان تو ربات موجود شده فقط گیگی 20 هزار
🇩🇪
⚡️
10GB=200T
⚠️
دوستان 50 تا تست ۱٠٠ مگابایتی ۱ روزه تو ربات موجود شده ، خواهشا تست محدوده اگه میخواین بخرید فقط تهیه کنید و سرعت تست کنید درصورت رضایت میتونید سفارشتتونو ثبت کنید
❤️
💥
@RUSSIAPROXYY_Bot
💎
آیدی ربات جهت ثبت سفارش
👆🏻</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/IranProxyV2/8756" target="_blank">📅 20:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8755">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">⛄️200 گیگ.npvt</div>
  <div class="tg-doc-extra">7.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8755" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
🤍
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8755" target="_blank">📅 20:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8754">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes📷.npvt</div>
  <div class="tg-doc-extra">1.5 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8754" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
💵
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/IranProxyV2/8754" target="_blank">📅 20:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8753">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🔥⚡️.npvt</div>
  <div class="tg-doc-extra">1.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8753" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/IranProxyV2/8753" target="_blank">📅 20:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8752">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">‎⁨بادکنک پرسرعت🎈⁩.npvt</div>
  <div class="tg-doc-extra">2.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8752" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
❤
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/IranProxyV2/8752" target="_blank">📅 20:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8751">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">متصل سرعتی⚡.npvt</div>
  <div class="tg-doc-extra">2.1 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8751" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
🛜
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/IranProxyV2/8751" target="_blank">📅 20:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8750">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🔥🤝.npvt</div>
  <div class="tg-doc-extra">20.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8750" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
🇹🇷
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/IranProxyV2/8750" target="_blank">📅 20:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8749">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Sshموشک.npvt</div>
  <div class="tg-doc-extra">1.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8749" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
💎
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/IranProxyV2/8749" target="_blank">📅 19:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8748">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jomDGQnjtDs1iRF8ER58I-a7dSNiu-kiv7UDnZBZpBu1H4zDSsZVLrbCbylP8bJx9TRx7Hkg5VDYBr92P6F99eUMPKdP7KHiyTmpx-NNbnQcwepeMgvkNHbikoi8-t6Stp9D1V8qkQhZph8q5jrfHBhwqPuFjXSiS86Tk0k7fiz9O6JlJU0tH_Uqbm14O3-c37vKFsw1kxKuTeoB1lB9XIgyUsnrm2uHLl7FpykMN0XVYyVpzbV-n85kSbOWu6fF2IV4FfYn0ldv6IjRJf9eZk-Pv61WDc8vjZtKIyXDLo8wnreX1dfG_ZtEEFRehb2XKHbbRowjQaO0ZRT270yk4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانل پرسرعت آیپی آلمان تو ربات موجود شده فقط گیگی 20 هزار
🇩🇪
⚡️
10GB=200T
⚠️
دوستان 50 تا تست ۱٠٠ مگابایتی ۱ روزه تو ربات موجود شده ، خواهشا تست محدوده اگه میخواین بخرید فقط تهیه کنید و سرعت تست کنید درصورت رضایت میتونید سفارشتتونو ثبت کنید
❤️
💥
@RUSSIAPROXYY_Bot
💎
آیدی ربات جهت ثبت سفارش
👆🏻</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/IranProxyV2/8748" target="_blank">📅 13:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8747">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">مخصوص❤️🔥.npvt</div>
  <div class="tg-doc-extra">2.8 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8747" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
💯
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/IranProxyV2/8747" target="_blank">📅 13:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8746">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">میوه‌جات🍒🍓.npvt</div>
  <div class="tg-doc-extra">2.5 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8746" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/IranProxyV2/8746" target="_blank">📅 13:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8745">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جنگی🚀.npvt</div>
  <div class="tg-doc-extra">2.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8745" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
👑
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/IranProxyV2/8745" target="_blank">📅 12:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8744">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meYLkCNG48WsNvF-d9ZWkG5hDfyXUMHnJlxhE5tQr_rX54oQgn0qrl1YP5xOnfEfEVg77M8I68MOOGQfzWVv0mUQC0NiHF7kevnOKORiFs958avHELZkApIaSJOE_vdKBdS1-8PpW20XD9wVrwBZcmRbHpGJIxKKt8pirgqgN1cdwf7_sd0kl7sDR-XVZupNgh6SRhlSoeTtq9fL-Tls1GYmn5Bi35nyvSstRmu2FRTiqYphgWfLLJMERxvjq5fm28w-H-h6CZv-oRmgiMF9fIHz0DvHt618mEC-SRjpttCETpN7gSsxaNsF9fiXeinas86U28Z6xtRIj8707ZiqVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیتی رو سرورا انجام دادم، جهت افزایش سرعت و پینگ، لذت ببرید، شرمنده بابت چنددقیقه اختلال
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/IranProxyV2/8744" target="_blank">📅 12:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8743">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBgdxfayoPDPh9fDVa33r94YeAXH_-oO7rmfniaFABKJhO7Fdgtxtvp0fg-DtNGpREafBkiMA7fTSsiAnv3CS-rZlHRMx1v52AvmWye4GllkZeoSmKefmpBJxu8oxqR7lsAPpX0tMf3qeOIbb5toWwjXEZvp4dcD6LUqTPWAErkgPLIhly3CxEz-EK6Z2SdeZrCjTrvAMTDFvM6U2JZ2a1VE0AZ5YMYYR_UXS-ec3-j4OqUwTSNjpMa3nPjSmVBGTWZRQ0-XLVwoVCeNtWf7DM391-M7o4RYwmsYMqycxK6vm15d15yoRfE-EVlL6Te7i8CuesFzSVZ_WhMKZobyXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانل پرسرعت آیپی آلمان تو ربات موجود شده فقط گیگی 20 هزار
🇩🇪
⚡️
10GB=200T
⚠️
دوستان 50 تا تست ۱٠٠ مگابایتی ۱ روزه تو ربات موجود شده ، خواهشا تست محدوده اگه میخواین بخرید فقط تهیه کنید و سرعت تست کنید درصورت رضایت میتونید سفارشتتونو ثبت کنید
❤️
💥
@RUSSIAPROXYY_Bot
💎
آیدی ربات جهت ثبت سفارش
👆🏻</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/IranProxyV2/8743" target="_blank">📅 10:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8742">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🟢
لینکِ دانلودِ مستقیمِ داخلی (بدونِ فیلتر) وی‌پی‌ان‌ها و کلاینت‌های اندروید که این چند روز کارآمد و متصل بودن:
⚪️
Psiphon
[ v 453 ] :
https://guardts.ir/f/93e64280865c
⚪️
Psiphon ( Mod )
[ v 462 ] :
https://guardts.ir/f/4c112039f3dd
⚪️
V2RayNG
[ v 2.1.7 ] :
https://guardts.ir/f/c897cf6ab459
⚪️
V2RayN
(
Windows
) [ v 7.20.4 ] :
https://guardts.ir/f/6453ca38d2f5
⚪️
NapsternetV
[ v 123.1 ] :
https://guardts.ir/f/0e6130b96bd1
⚪️
SlipNet
[ v 2.5.3 ] :
https://guardts.ir/f/c3d4e2a2f7f5
⚪️
SlipStream
(
Windows
) :
https://guardts.ir/f/fc816aa4cf4a
⚪️
V2Box
[ v 5.0.3 ] :
https://guardts.ir/f/3b27ca8e489a
⚪️
Happ
[ v 3.18.1 ] :
https://guardts.ir/f/482047bab8e9
⚪️
MahsaNG
[ v 16 ] :
https://guardts.ir/f/bd0a0a134a07
⚪️
OpenVPN
[ v 3.3.2 ] :
https://guardts.ir/f/d0d45fa4119e
⚪️
HTTP Injector
[ v 6.5.0 ] :
https://guardts.ir/f/42d52a95c27b
⚪️
NetMod
[ v 3.2.8 ] :
https://guardts.ir/f/70f45198bf5a
⚪️
ShirOKhorshid
[ v 2026.5.24 ] :
https://guardts.ir/f/f32060f78b4b
⚪️
AM Tunnel
Pro
[ v 28.0 ] :
https://guardts.ir/f/7148653eb96c
⚪️
AM Tunnel Lite
: [ v 2.0 ] :
https://guardts.ir/f/4c38f9637164
⚪️
MasterDNS
[ v 1.0.9 ] :
https://guardts.ir/f/d2bf0d7588a7
⚪️
WireGuard
[ v 1.0.20 ] :
https://guardts.ir/f/df98ced89296
⚪️
WhiteDNS
[ v 1.5.1 ] :
https://guardts.ir/f/ca2c5508f4a9
⚪️
Every Proxy
[ v 12.7 ] :
https://guardts.ir/f/777372a7d691
⚪️
NetShare
[ v 2.5.50 ] :
https://guardts.ir/f/6ffdbd5f4b75
🔴
مهم؛ حتما لینک رو کپی کنید و در مرورگر Chrome جایگذاری کنید و دانلود کنید ؛ لینک ها با همه ی اینترنت ها بدونِ نیاز به وی پی ان کار می‌کنند .
+
اعتبارِ لینک هایِ دانلود: ۲۴ ساعت
[ لینک ها آپدیت میشه ]
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/IranProxyV2/8742" target="_blank">📅 10:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8741">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">vless://8ecccb71-95ec-4a12-cbc5-ffc32c4d5ded@3.71.187.131:443?security=none&encryption=none&headerType=none&type=tcp#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو همراه اول واسه من وصله با پینگ 152 مابقی اپراتور ها رو خودتون تست بزنید
🙂
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/IranProxyV2/8741" target="_blank">📅 09:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8740">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">vless://96103268-ee66-4245-b911-747857d26d8f@coco.mayagallery.shop:80?encryption=none&security=none&sni=fastly.com&fp=chrome&type=xhttp&host=Bartviloon.com&path=%2Fsteam&mode=auto&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
وصله سرعت بالا پینگ 125
🍾
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/IranProxyV2/8740" target="_blank">📅 09:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8739">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🇺🇲قوی (1).npvt</div>
  <div class="tg-doc-extra">2.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8739" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
👍
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/IranProxyV2/8739" target="_blank">📅 08:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8735">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺¹¹.ovpn</div>
  <div class="tg-doc-extra">35.8 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8735" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ مخصوص OpenVPN
📱
سرعتش خوبه، نامحدوده
🔝
- اگه ارور داد چند بار بزنید روی Retry متصل میشه
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/IranProxyV2/8735" target="_blank">📅 08:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8734">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CIVAX🦭.npvt</div>
  <div class="tg-doc-extra">3.1 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8734" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
🍽
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/IranProxyV2/8734" target="_blank">📅 07:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8733">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CIVAX🦄.npvt</div>
  <div class="tg-doc-extra">3.1 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8733" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/IranProxyV2/8733" target="_blank">📅 07:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8732">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">vless://96103268-ee66-4245-b911-747857d26d8f@coco.mayagallery.shop:80?encryption=none&security=none&sni=fastly.com&fp=chrome&type=xhttp&host=Bartviloon.com&path=%2Fsteam&mode=auto&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
تست کنید سر صبح بفرمایید ویتامین
🍊
👆
سرور آلمان
🇩🇪
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/IranProxyV2/8732" target="_blank">📅 06:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8731">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M41TmOtPUzNDlHbt81mzZUXzN6Fwb-Ynbhw8IU7B-rmotyc4K3nLXsb8NbW8Gt7ANMbE7o4EUYdCgT0pjQCS4fW75TSO2osjJz4LcAxu2P0-LF5XOU8MmjrtN1-5h9IuGVxa08T1Gq7bYb92OHj-EgDeTONyRL3RR3uCdmy-Cv_kn917H-E3OS_DYnb97NnkB9jaFD6z0zvOr-JsQIIsQv9HyYf9UIqAV-aRjXjWI08veWKInGjrS9FEwGp8Li12nbUFTLN2brbx-K3wPQUPsXZ4jlZZvBuutXAcfqJkrCVUAO7X4utIi_xJ3nh_tnKTKO85GYQ9pgKmxMUMnIRn7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانل پرسرعت آیپی آلمان تو ربات موجود شده فقط گیگی 20 هزار
🇩🇪
⚡️
10GB=200T
⚠️
دوستان 50 تا تست ۱٠٠ مگابایتی ۱ روزه تو ربات موجود شده ، خواهشا تست محدوده اگه میخواین بخرید فقط تهیه کنید و سرعت تست کنید درصورت رضایت میتونید سفارشتتونو ثبت کنید
❤️
💥
@RUSSIAPROXYY_Bot
💎
آیدی ربات جهت ثبت سفارش
👆🏻</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/IranProxyV2/8731" target="_blank">📅 19:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8730">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">⚡♥️💥.npvt</div>
  <div class="tg-doc-extra">17.2 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8730" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/IranProxyV2/8730" target="_blank">📅 19:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8729">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">از لحاظ روحی نیاز دارم شانس درِ خونم رو از جا بکَنه.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/IranProxyV2/8729" target="_blank">📅 18:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8728">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUeyRtbG39hAT4oI8rD01QqLE0lZV0lB-KyZB6OplTlQ-LnIgqQboUrxXdtM-G8UbwUyVpXz4dUeqtS6SFpdca3z7x30BDB4fzQTO1mcqobZin4GGk8O91c_QGuI-quW_3XDHF955oSOauLsDyYiPVSacG14_G5q8fLhoLH9KXV5UtpD-041bX_FFHU3HCBYk9_v2JoPEMxelvvIr84x8_NfM0lRDJ43aDUpT7sHNLQIupaG-eWSAFUschUmFFHYji7ydRtH1rUquiz0UImFObnUHwcHFdSm1AqoMPSRF7yeKFntsU9agzGnR26UGzH35lYuebI5iPN_RNlrpfQPXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانل پرسرعت آیپی آلمان تو ربات موجود شده فقط گیگی 20 هزار
🇩🇪
⚡️
10GB=200T
💥
@RUSSIAPROXYY_Bot
💎
آیدی ربات جهت ثبت سفارش
👆🏻</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/IranProxyV2/8728" target="_blank">📅 15:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8726">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سرعت جت🔥.npvt</div>
  <div class="tg-doc-extra">2.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8726" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/IranProxyV2/8726" target="_blank">📅 15:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8725">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/IranProxyV2/8725" target="_blank">📅 14:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8724">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پر سرعت❤️‍🔥.npvt</div>
  <div class="tg-doc-extra">2.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8724" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
💙
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/IranProxyV2/8724" target="_blank">📅 14:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8723">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">XV2RAY -🦖.npvt</div>
  <div class="tg-doc-extra">19.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8723" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
🏅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/IranProxyV2/8723" target="_blank">📅 13:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8719">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺⁷.ovpn</div>
  <div class="tg-doc-extra">5.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8719" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ مخصوص OpenVPN
📱
سرعتش خوبه
🔝
- اگه ارور داد چند بار بزنید روی Retry متصل میشه
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/IranProxyV2/8719" target="_blank">📅 13:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8716">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺⁴.ovpn</div>
  <div class="tg-doc-extra">5.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8716" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ مخصوص OpenVPN
📱
سرعتش خوبه
🔝
- اگه ارور داد چند بار بزنید روی Retry متصل میشه
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/IranProxyV2/8716" target="_blank">📅 13:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8713">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺¹.ovpn</div>
  <div class="tg-doc-extra">5.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8713" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ مخصوص OpenVPN
📱
سرعتش خوبه
🔝
- اگه ارور داد چند بار بزنید روی Retry متصل میشه
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/IranProxyV2/8713" target="_blank">📅 12:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8712">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تانل پرسرعت آیپی آلمان تو ربات موجود شده فقط گیگی 20 هزار
🇩🇪
⚡️
10GB=200T
⚠️
دوستان 200 تا تست ۱٠٠ مگابایتی ۱ روزه تو ربات موجود شده ، خواهشا تست محدوده اگه میخواین بخرید فقط تهیه کنید و سرعت تست کنید درصورت رضایت میتونید سفارشتتونو ثبت کنید
❤️
💥
@RUSSIAPROXYY_Bot
💎
آیدی ربات جهت ثبت سفارش
👆🏻</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/IranProxyV2/8712" target="_blank">📅 10:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8711">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صبح بخیر‌.npvt</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8711" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
🤩
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/IranProxyV2/8711" target="_blank">📅 09:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8709">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">عسله لامصب.ovpn</div>
  <div class="tg-doc-extra">5.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8709" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ مخصوص OpenVPN
📱
سرعتش خوبه
🔝
- اگه ارور داد چند بار بزنید روی Retry متصل میشه
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/IranProxyV2/8709" target="_blank">📅 09:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8708">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/IranProxyV2/8708" target="_blank">📅 08:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8707">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پر سرعت (1).npvt</div>
  <div class="tg-doc-extra">4.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8707" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
😯
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/IranProxyV2/8707" target="_blank">📅 08:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8706">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">موشک موقت⌚️.npvt</div>
  <div class="tg-doc-extra">9.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8706" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
🔝
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/IranProxyV2/8706" target="_blank">📅 08:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8705">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🔹️همراه اول🔹️(1).npvt</div>
  <div class="tg-doc-extra">7.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8705" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
🥂
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/IranProxyV2/8705" target="_blank">📅 07:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8704">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">💥𝗡𝗜𝗧𝗥𝗨 𝗩𝗜𝗣💥.npvt</div>
  <div class="tg-doc-extra">10.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
💯
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/IranProxyV2/8704" target="_blank">📅 07:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8703">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نت ملی شکن⚡️.npvt</div>
  <div class="tg-doc-extra">29.8 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8703" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
☄️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/IranProxyV2/8703" target="_blank">📅 02:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8702">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ایرانسل50ترابایت نوش جونتون.npvt</div>
  <div class="tg-doc-extra">4.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8702" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
💥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/IranProxyV2/8702" target="_blank">📅 02:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8701">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ایرانسل.npvt</div>
  <div class="tg-doc-extra">4.2 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8701" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel
🛜
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/IranProxyV2/8701" target="_blank">📅 00:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8700">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">100ترابایت♥️.npvt</div>
  <div class="tg-doc-extra">4.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8700" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/IranProxyV2/8700" target="_blank">📅 00:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8699">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برق تک فاز.npvt</div>
  <div class="tg-doc-extra">1.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8699" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/IranProxyV2/8699" target="_blank">📅 00:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8698">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تانل پرسرعت آیپی آلمان تو ربات موجود شده فقط گیگی 20 هزار
🇩🇪
⚡️
10GB=200T
⚠️
دوستان 200 تا تست ۱٠٠ مگابایتی ۱ روزه تو ربات موجود شده ، خواهشا تست محدوده اگه میخواین بخرید فقط تهیه کنید و سرعت تست کنید درصورت رضایت میتونید سفارشتتونو ثبت کنید
❤️
💥
@RUSSIAPROXYY_Bot…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/IranProxyV2/8698" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8697">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تانل پرسرعت آیپی آلمان تو ربات موجود شده فقط گیگی 20 هزار
🇩🇪
⚡️
10GB=200T
⚠️
دوستان 200 تا تست ۱٠٠ مگابایتی ۱ روزه تو ربات موجود شده ، خواهشا تست محدوده اگه میخواین بخرید فقط تهیه کنید و سرعت تست کنید درصورت رضایت میتونید سفارشتتونو ثبت کنید
❤️
💥
@RUSSIAPROXYY_Bot…</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/IranProxyV2/8697" target="_blank">📅 22:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8696">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تانل پرسرعت آیپی آلمان تو ربات موجود شده فقط گیگی 20 هزار
🇩🇪
⚡️
10GB=200T
⚠️
دوستان 200 تا تست ۱٠٠ مگابایتی ۱ روزه تو ربات موجود شده ، خواهشا تست محدوده اگه میخواین بخرید فقط تهیه کنید و سرعت تست کنید درصورت رضایت میتونید سفارشتتونو ثبت کنید
❤️
💥
@RUSSIAPROXYY_Bot
💎
آیدی ربات جهت ثبت سفارش
👆🏻</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/IranProxyV2/8696" target="_blank">📅 19:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8695">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
⚠️
اقتصاد نیوز : ایرانسل و همراه اول امکان خرید اقساطی بسته اینترنت رو فعال کردند.
اوج خوشبختی ایرانی خرید قسطی نت
😠
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/IranProxyV2/8695" target="_blank">📅 18:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8694">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/IranProxyV2/8694" target="_blank">📅 15:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8693">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ALL NET 8 (1).npvt</div>
  <div class="tg-doc-extra">5.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8693" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ نپستر نامحدود
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/IranProxyV2/8693" target="_blank">📅 15:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8692">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یه سوپرایز دیگ هم واستون دارم، بزودی رونمایی خواهیم کرد
😁</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/IranProxyV2/8692" target="_blank">📅 14:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8691">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=40T
💥
توجه کنید پلن های 3 گیگ، 5 گیگ، 10 گیگ، 15 گیگ و 20 گیگ تو ربات موجوده با تخفیفففف
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت…</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/IranProxyV2/8691" target="_blank">📅 13:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8690">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCoVdI5dS8GfgcB5YX1PlQNDkDW6fuaLZoU2OVsGiIjAra443dVYt1LSBez0kfzrzA63_GbAD_8LiVpir398SzE7QTR0BG7xXyP5YjYKXSIK5GtQ2SZ2-5R0OfUkm26Csza4d8kQzPaGJpgNyxzKhhlw0Jx0GntEWkakTnXqESSOLb2Nrh2I6Fb3gL5Ha6Y3RhKxPspovZGx7zKCLsXz4R8rQSCQc2dPRQ4nuSHIhpXhK6Q4_lriK30poB_VH3czbucMQs62xVYRLEN3rwye1Sik-QkI6ro-ngSov21NMfDsUJ_DtKF10OvYH9ZB28dfM9ZeOiTYlloGnCFTKDMQGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=40T
💥
توجه کنید پلن های 3 گیگ، 5 گیگ، 10 گیگ، 15 گیگ و 20 گیگ تو ربات موجوده با تخفیفففف
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot
📌
دوستان دقت کنید اشتراک های که تهیه میکنید، مثل چنلای دیگه تانل نیستن، قطعی بعد دو سه روز ندارند و به همین خاطر قیمت ها متفاوته
، پشتیبانی تا آخرین مگ مصرفی شما انجام خواهد شد.</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/IranProxyV2/8690" target="_blank">📅 07:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8686">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@russiaproxyy🇷🇺(4).ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8686" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ های جدید اختصاصی OpenVPN
با حجم و اعتبار نامحدود
تست شده روی ایرانسل، رایتل، شاتل، سامانتل(برخی نقاط ممکنه متصل نشه)
بدون نیاز به یوزر پسورد
برای اتصال در تمام سیستم عامل ها کافیه روی کانفیگ کلیک کنید و برنامه OpenVPN را انتخاب کنید، یوزرنیم و پسورد را ست کنید و متصل شوید یا کانفیگ را سیو کنید و از داخل برنامه ایمپورت کنید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/IranProxyV2/8686" target="_blank">📅 01:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8681">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">دیگه به آخرش رسیدم.npvt</div>
  <div class="tg-doc-extra">13.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8681" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/IranProxyV2/8681" target="_blank">📅 00:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8679">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Openvpn.ovpn</div>
  <div class="tg-doc-extra">36.8 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8679" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ open vpn
آموزش اتصال:
کانفیگ رو وارد برنامه کنین
بزنین روی connect
بعدش ۲ تا گزینه میاد بزنین روی continue
عشق کنین
💥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/IranProxyV2/8679" target="_blank">📅 00:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8678">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYAX3t1R2hpvj2xZSEVvBv17JRfqSPMODTlDhuFUaf2kyJvbaVCQHiq-LMguTBoAhPfDOyfuOhd7SjxOiR6AzI7sVEzfSCdDGDJhvtlQUg6Wbn3wmT5TvVyBkuYQaWQytEIyUNARca4rm8SQSCZBqWdSu1CyZ6BVJvxqSvsJzxJabZ6R9Z69DNicgB6N83E8TgVCFGYQK8dm5q4vVR8EWwYTxokaCgs_j8UjHY9jQpNeldf7Z0npWqPMV8C3y00rQfPXfxiB5YYirEQiXGnRJnMG5tRfOtnFnzahfqd573NLHVmuN0DlICJlLpmb6n-jWd6tuYMU7ohsPqolb_V2vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بررسی وضعیت اینترنت ایران نشون میده که پزشکیان هنوزم نتونسته اینترنت رو وصل کنه.
▪️
اینترنت دیتاسنترها قطعه.
▪️
اینترنت خانگی به شکل وایت‌لیستی کار می‌کنه.
▪️
پروتکل‌های IPv6 و HTTP3 مسدوده؛ SSH و UDP پر اختلاله.
به خاطر کاهش پهنای باند شبکه هم بسیاری از کانفیگ های پولی که در دوران قطعی اینترنت کار میکردن؛ از کار افتادن.
خلاصه میشه گفت اینترنت وصله ولی فقط به ظاهر
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/IranProxyV2/8678" target="_blank">📅 23:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8677">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">vless://309f5aa1-2665-4ceb-9cc1-17eea907a927@185.143.235.201:8880?path=%2F&security=none&encryption=none&host=sublink2.ionosio.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
اختصاص کانال
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/IranProxyV2/8677" target="_blank">📅 22:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8676">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🦕.npvt</div>
  <div class="tg-doc-extra">1.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8676" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وصلللللللللل پرسرعتتتتت پخش کنید
❤️‍🔥
👀
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/IranProxyV2/8676" target="_blank">📅 20:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8675">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">باطری نیم قلم (1).npvt</div>
  <div class="tg-doc-extra">1.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8675" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وصلههههههه پرسرعتتتت نامحدوددد فوررر کنیددد
❤️‍🔥
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/IranProxyV2/8675" target="_blank">📅 19:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8674">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWR7ihqUFYoZ3Km8pDVNZeFXtgiwe5fg4nOhda81JFa4g8_gYgc-NGqSxRR-ZFdtH4x1afCLwBJDL_Kfd6q_eK8PvvvTwTsfO5GSARes9b5CAr2pDJbhpTCPq9ILnsZhwg0BGtwAjqHX84NPGVqmQmZhMqcCvp0bZxgfmW-k-dUuntk-Zu0o72K6Afg4l_NNUq6c6tnjCnadmjOcNYKTc0zBxA0BhB7pdN03QRDeGuNzZkP2ggmV2XLQywC7a2mVGlplGtHTqwlUBipaDbuJvlAsETtrQ3IkGN7ayoVncVBiSwhllGUM7oH6XBqaYlVYwLpWmQavnDkPXLqH2CATSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دوستان عزیز متاسفانه دامنه قبلی ما فیلتر شد توسط آروان به علت عبور ترافیک زیاد و دسترسی به ساب هاتون امکان پذیر نیست، درحال حاضر ولی ما حل کردیم مشکلو، برای رفع مشکل دامنه جدید جایگزین شد که باید لینک ساب هاتون مطابق تصویر تغییر بدین یا اگه ساب رو وارد v2rayNG کردین نیازه فقط یه اپدیت بزنید مشکل حل میشه.
◀️
لینک سابتونو بردارین، حتما دامنه جدید رو از قسمتی که نوشته rezaz7ziranisa به
russiaproxyy
تغییر بدید و وارد ساب لینکتون بشید سرور جدید رو بردارین
✅
دوستانی که لینک ساب رو وارد v2rayNG کردین، فقط نیازه یه اپدیت بزنید از منوی سه نقطه بالای برنامتون همین تنها
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/IranProxyV2/8674" target="_blank">📅 19:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8673">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Ajex موشک متصل.npvt</div>
  <div class="tg-doc-extra">12.9 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8673" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ـ NPV حجم نامحدود
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/IranProxyV2/8673" target="_blank">📅 17:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8672">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">vless://dfd2bd8a-aedb-47d1-b87c-c22f18495592@f101001010.imsoon.org:80?encryption=none&host=play.google.com&path=%2Fsoon&security=none&type=ws#Xhttp80-iao93lhbdd-1000.00GB%F0%9F%93%8A
به غیر از همراه اول، مابقی اپراتورا وصله
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/IranProxyV2/8672" target="_blank">📅 17:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8671">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
مدیرعامل آروان کلاد(ابر آروان):
◀️
از نظر فنی همینطوری که میشه توی یه لحظه اینترنت رو قطع کرد؛ همینطوری میشه تو یه لحظه هم وصلش کرد. زمانبر بودن بهبود وضعیت اینترنت از نظر فنی فقط بهانه ست. وضعیت اینترنت در حال حاضر بسیار ناپایدار و ضعیفه و اصلا به شرایط قبل از جنگ برنگشته.
ببخشید که ما ریدیم تو نت دیگه تکرار نمیشه روانی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/IranProxyV2/8671" target="_blank">📅 17:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8670">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpYRW5aZWRwMm1rVGJUMXFD@4.168.201.246:443#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vmess://eyJhZGQiOiI1MS4xOTUuMjM1LjcxIiwiYWlkIjoiMCIsImFscG4iOiIiLCJmcCI6IiIsImhvc3QiOiIiLCJpZCI6IjU5ZTI4Zjc4LWMzMWItNDYxMy05ZDlmLTFlNjczMmEzMWY0NiIsImluc2VjdXJlIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwicG9ydCI6IjIwNTIiLCJwcyI6IkBSVVNTSUFQUk9YWVkg8J+Ht/Cfh7oiLCJzY3kiOiJhdXRvIiwic25pIjoiIiwidGxzIjoiIiwidHlwZSI6Imh0dHAiLCJ2IjoiMiJ9
vless://9ca41eeb-4b30-4271-a123-22021b1230d0@104.17.121.71:443?mode=auto&path=%2FTelegram-Zedmodeon&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=mano.tll-far.ir&fp=chrome&type=xhttp&allowInsecure=0&sni=mano.tll-far.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
trojan://f6d3aa07a52dbcedcb4731029e2fb6ae@18.163.128.27:2663?security=tls&insecure=0&headerType=none&type=tcp&allowInsecure=0&sni=www.nintendogames.net#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/IranProxyV2/8670" target="_blank">📅 13:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8669">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzxE68EIfMBt9jr6YIFYGGlEDu3qgkLKvfXMFYnyR2ufOVXfgEkhMj5W2QPr7SOD8XGXI8ELGUj5jF-2GryZqEvnYj4DfqIHh3Fq-GZoF89nNnV_QzJ7zXZCol2ypE5w0Hywfr1zGhsXz78ZyPThsVZq38bpI6Lti39KE2C-iZ3XSnE4u5i8yAwLFZmKWAQMDXQyVI5fRiRhqsHy5OLBgxoQ0IYJCc1TM9p47nKbH5jBzSio0UaSMeeaUkozQROd2VrzZUhdmBo7wsFcIPDOIfSStLiM2hvRhgKn3b6fqXJ5rqvp3U_6_MsykO4Jq824b3olDTB85JFM14v3VZHRrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این روزا سر به سر مردم شریف ایران نزارید
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
|
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/IranProxyV2/8669" target="_blank">📅 13:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8668">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺(2).npvt</div>
  <div class="tg-doc-extra">19 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8668" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ پرسرعت نپستر مناسب تمام‌ اپراتورها ، مخصوص دانلود و وبگردی برای اندروید و آیفون
👀
💯
ترافیک 12 ترابایت، زمان نامحدود
⚡️
❤️‍🔥
مخصوص شرایط نت ملی و فیلترینگ شدید
☄️
✔️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/IranProxyV2/8668" target="_blank">📅 09:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8667">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Moshak.ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8667" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اوپن ویپن، اگه ارور retry داد، چند بار پشت سرهم بزنید وصل میشه سرعت موشک داره
👀
☄️
Fast
💯
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/IranProxyV2/8667" target="_blank">📅 08:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8666">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺.npvt</div>
  <div class="tg-doc-extra">4.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8666" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ پرسرعت نپستر مناسب تمام‌ اپراتورها ، مخصوص دانلود و وبگردی برای اندروید و آیفون
👀
💯
ترافیک و زمان نامحدود
⚡️
❤️‍🔥
مخصوص شرایط نت ملی و فیلترینگ شدید
☄️
✔️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/IranProxyV2/8666" target="_blank">📅 08:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8665">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/IranProxyV2/8665" target="_blank">📅 07:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8663">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmvxqm0gQY5YctsN5ySQVTRhSJ6HEjNug290uksmQK7jIoF6t0obqoIrsIAillhG1VjW10TJS-pxXeVfjWLbxGoJD8IxbursYniX5VVt1KVmS6SwL-57qVAdCcD08VoBFY8_UHBXcA8RFd-TYRflznZAlnKY17HQw3hw-rPWBR5EzVnXcxZC9tfVUNIk2fngDQ9VQgol71KquUMPWh14AjNTFs5UvDoTmpMLfjt7_oO461HGbPdsp-Z7XJEph_JBNrTHGA3gxSgoEDnOEG7ftJSlYzBOAp6EHrJnT-37BkPME0RCXW67EEfh9JpcK5lroN5xQKKrMQ0gZFvK6fFXxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دوستان عزیز متاسفانه دامنه قبلی ما فیلتر شد توسط آروان به علت عبور ترافیک زیاد و دسترسی به ساب هاتون امکان پذیر نیست، درحال حاضر ولی ما حل کردیم مشکلو، برای رفع مشکل دامنه جدید جایگزین شد که باید لینک ساب هاتون مطابق تصویر تغییر بدین یا اگه ساب رو وارد v2rayNG کردین نیازه فقط یه اپدیت بزنید مشکل حل میشه.
◀️
لینک سابتونو بردارین، حتما دامنه جدید رو از قسمتی که نوشته rezaz7ziranisa به
russiaproxyy
تغییر بدید و وارد ساب لینکتون بشید سرور جدید رو بردارین
✅
دوستانی که لینک ساب رو وارد v2rayNG کردین، فقط نیازه یه اپدیت بزنید از منوی سه نقطه بالای برنامتون همین تنها
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/IranProxyV2/8663" target="_blank">📅 01:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8659">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Openvpn.ovpn</div>
  <div class="tg-doc-extra">108.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8659" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خطا retry داد ۴ الی ۵ بزنید روی retry وصل میشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/IranProxyV2/8659" target="_blank">📅 21:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8658">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b45uVvjHFWfOeW3oQMW1iJ7wzYA5QcJF5L-Qe2QVTW43275JDxbzBEkpljvKvTu1MCZcej6P_3VlBiIXzH5UytDodWJTHD6gyPHFvEI20l1IaHzhYZHPJlvkwMyDRpN_qETNUn0J7nyjwQSZythd_YnG4Cdy2THy9WwL76EVi84SUIeG_MYmjodVxVNI6nEUs3tXU_T-9IIr9wmZOgG5aMeeFU0bBp61PQvHuIB6Bm1_6yKj81yk8Q1bMY9VrqIXhhQB_MBW4sTHnyOUhCz3Sp9grECNED4FBF1MTVjIkvCaLVkmin6wV9UZJM-vPey-ojBfFg2TBDAwBPYILrbhXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سیتنا:
علت کندی اینترنت ایران اینه که IPv4 بازگشت کامل داشته ولی IPv6 هنوزم بسته ست.
پروکسی
|
پروکسی
|
پروکسی
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/IranProxyV2/8658" target="_blank">📅 20:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8657">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkdNzguXOjBOIsJq-5bOdwqxKW_bpJi-AxFsbTIzRhmQ6rns2zomWjG3bxC18YHMofnmXjFlG4QqJFviWOsQ1XzM_5YliQT1LNGBnkq3bgFGYsscgu7v22Uo50jbQrgLaokdPUz-76OCiZpNKq0JGwT8XIREKtAzOq0v_hZA_4L2Rshl-wOaL-Rf-jlxP6ewYD66_k-tjkLOsrEEcDXlgu1n-VUflE2kChT32M-lHyV-xD4wToy6BhUiYXZwjC46Qt11eGvHXQmGAqU4yBbv8a-aD0wcX1QF_AY0eedLeEspr47zHR3aDMNUJMFud7MrWKDvKbPdvACcSvdriideJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😬
😬
😬
😬
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/IranProxyV2/8657" target="_blank">📅 20:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8655">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@iDeathBirth🐰.npvt</div>
  <div class="tg-doc-extra">4.1 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8655" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اختصاصی نامحدود.
بفرستید بقیه‌ام وصل شن
🤍
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/IranProxyV2/8655" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8654">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">PRO71💎.npvt</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8654" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
کانفیگ نپسترنت ، Npv Tununel
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/IranProxyV2/8654" target="_blank">📅 18:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8653">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWGCjMS9N0LrmLhmwA8CfFW5Rt-3zEhWoUVdMlQjIIaZWD76oxiYuOoi63MXDN-blno0SUNQZ4FkrfwIsXuEbczSr1FQP-_sT3mFcoZied7Pe3UQ2uwBRc-ceL6CghdUcrXVG7mLkA_IPukKuOnQw7FV-1C2BT1zvvoRzJCeePlSxEa9eefHSI4I5c4huNCwNrseLs4dj33ZZCpSfpUk4KKY8uW8B8_GcQdxpsTHZW2sru4H6wtJP3fjDOHjqzIHCB6yiEGCi8EermhlReQVchsWDDe3FLtAy5F-rQovelQSinMzZDhNSQ3Ln7Uc4PSzECxB6rfFRj5j2eaWf5umIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مدل محتوا(دیتای کاملا جعلی و روایت ساختگی) که یسری از رسانه‌ها(دلقک‌های حکومتی) دارن منتشر میکنن فقط داره به قطع اینترنت و فیلترینگ مشروعیت میده و اصلا جنبه فان نداره!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/IranProxyV2/8653" target="_blank">📅 17:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8652">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/IranProxyV2/8652" target="_blank">📅 15:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8651">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">گلچین گل های غربت⁵⁰.npvt</div>
  <div class="tg-doc-extra">9.1 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8651" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
کانفیگ نپسترنت ، Npv Tununel
▫️
6 تا سرور (پینگ بگیرید) نامحدود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/IranProxyV2/8651" target="_blank">📅 10:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8650">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">trojan://humanity@www.calmlunch.com:443?path=%2Fassignment&security=tls&insecure=1&host=www.calmlunch.com&type=ws&allowInsecure=1#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://e258977b-e413-4718-a3af-02d75492c349@45.130.125.69:2096?path=%2FChannel----%40VPNCUSTOMIZE&security=tls&encryption=none&insecure=1&host=jp.aniua.qzz.io&type=ws&allowInsecure=1&sni=jp.aniua.qzz.io#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/IranProxyV2/8650" target="_blank">📅 08:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8649">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺(5).ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8649" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
کانفیگ های جدید اختصاصی OpenVPN
با حجم و اعتبار نامحدود
🏅
تست شده روی ایرانسل، رایتل، شاتل، سامانتل(برخی نقاط ممکنه متصل نشه)
💥
بدون نیاز به یوزر پسورد
برای اتصال در تمام سیستم عامل ها کافیه روی کانفیگ کلیک کنید و برنامه OpenVPN را انتخاب کنید، یوزرنیم و پسورد را ست کنید و متصل شوید یا کانفیگ را سیو کنید و از داخل برنامه ایمپورت کنید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/IranProxyV2/8649" target="_blank">📅 06:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8648">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/IranProxyV2/8648" target="_blank">📅 23:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8647">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺(4).ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8647" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👑
کانفیگ OpenVPN-VIP
🌐
📶
آیپی ثابت بدون نشتی DNS
🇵🇪
🛡
متصل برای مخابرات و یکسری وای‌فای‌ها(منطقه‌ای)
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/IranProxyV2/8647" target="_blank">📅 18:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8646">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">درحال بررسی و آپدیت جدیدی برای سرورا هستم، کمی طول میکشه ولی سوپرایزی در راهه
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/IranProxyV2/8646" target="_blank">📅 18:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8645">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/IranProxyV2/8645" target="_blank">📅 18:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8641">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
سنتکام: حمله ایران به کویت با موشک بالستیک نقض آشکار و فاحش آتش بس بود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/IranProxyV2/8641" target="_blank">📅 14:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8634">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Openvpn.ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8634" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📍
کانفیگ برنامه Open VPN Connect
Password:
@KurdConfing
🌐
تمامی نت‌ها
📲
اندروید و ios
❗️
اگه وصل نشد چندبار retry بزنید حل میشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/IranProxyV2/8634" target="_blank">📅 14:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8633">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ایفونی های عزیز جامپ جامپ استفاده نکنید اپل ایدیم لاک شده سر این فیلتر فیلتر دیگ استفاده کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/IranProxyV2/8633" target="_blank">📅 13:47 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
