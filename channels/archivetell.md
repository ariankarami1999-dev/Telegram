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
<img src="https://cdn4.telesco.pe/file/ZlvNSayFmyUq3nbI-_DAnmsh-csvexavMUm8QDpCDSyjKAhIvjT5M6S0nKIhENTrhNwxtHr8Jaqc7D8kCqxksM2ZNoVaQdzmNg1Gl5hZ3oK0Eu_r6ECn7LhSU1sNDxf5Kk1dUfsEGlXXxMfq3AnraEa4Q0LigM8fz6HMtd4tDR8G20wMhd6XSMEOTzExGUmdwslW9aMrvmBaMyxrcfewlYuuD74Wd8O7xjvhIFSmlT98JdNNVcAYEpYMmRfpWxHw87sybzZdsOcuNt_GJohrY-HUIxOi0iUy64Fy3vx7szULw1__rrad2O4fiwv70cQOL6iiUVHsXCBl-ksQ7qPFew.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 7.75K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 14:03:13</div>
<hr>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ArchiveTel
pinned «
ربات چنل راه اندازی شد
🔥
تضمینی ، سرعت بالا و پایدار  قیمت عالی  @ArchiveTellbot  آموزش ساده خرید تو پست بعدی..
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/5239" target="_blank">📅 11:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">صداهای ElevenLabs نامحدود و رایگان
صداهای زیاد دیگه‌ای مثل مایکروسافت ، هوش مصنوعی گوگل و موارد دیگه هم داره
https://teamsp.org/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/archivetell/5238" target="_blank">📅 09:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPrAUZiZsGFu4oUENd4ns1_4rE7JyfCM0NlVrFFXg2oOGiLkrw_5glLALgjJNDNEQmalc-VAPTxCGZlnF-IFERkV7q_n6WPrQQ5sAitOkhEWOVu58Q7MKr09LFrniD-0pLF-mZZFZmeq4vs81ZYuzSyO2Bbhh1BWwBmCNJlrXij1GnfVngIIILJDB6qy-UYxuD-QZsO-ef9NLshD80BaP5S6b7dfDjNNZK45LITfjed7oLc8aONZfgei0khtdlTXYfDDVSk36QM6NbL7MDqH97D5Wa9-eKllNaTjmYSqlhHXIS7iMPE2mBT4f4Ap8JDrnSJo1Z6ERGtTnGlYuMTaFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت هوشمندانه ‌تر کردن متن بدون اینکه شبیه به متن تولید شده توسط هوش مصنوعی به نظر برسد
Rewrite the text below so it sounds clearer, sharper, and more p
Improve the structure, remove weak wording, and make the message more confident without changing the original meaning.
Text: [paste here]
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/archivetell/5237" target="_blank">📅 09:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خواندن پست‌ها و نظرات Threads در تلگرام
@threadsreaderbot
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/5236" target="_blank">📅 08:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دانلود مدل های هوش مصنوعی از سرور ایران
Bitgraph.ir/iran-ai/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/archivetell/5235" target="_blank">📅 08:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جدا الان وقتشه کانفرینگ تنظیم بازار بیاد قیمتا بشکنه
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/5234" target="_blank">📅 01:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">📘
معرفی پروژه GateRelay
یک reverse relay سبک و حرفه‌ای با Go است که هدف اصلی آن تانل کردن لینک ساب پنل با یک http proxy است و نمی‌خواهید حتی یک درخواست غیرمجاز از proxy عبور کند.
با GateRelay می‌توانید یک دامنه داخلی/قابل‌دسترسی مثل:
https://example1.com/sub/...
را به یک upstream خارجی مثل:
https://example2.com/sub/...
وصل کنید؛ اما فقط بعد از اینکه درخواست از نظر دامنه، مسیر و متد کاملاً تأیید شد.
ویژگی‌ها:
• نوشته‌شده با Go
• پشتیبانی از authenticated HTTP proxy
• جلوگیری از open proxy شدن
• فیلتر سختگیرانه قبل از مصرف proxy
📱
GitHub:
https://github.com/YrustPd/GateRelay
😊
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/archivetell/5232" target="_blank">📅 22:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7238deb5ae.mp4?token=oYkOvbo8LTtf60IERJG5WrpLvgaiIMXwaOTgGdyHvcKMPQy778Rm90_ZtpnCs-BjEQa7YDm_htcjpX-qoRRdH-gAMLewYXVrOVU1GULA2_NR-x3OwWq8KoxfltjqfL4Z3yxCHRJXn80tpiAknGoCf-e7cUrtCFffFZGzgiZlyLxtHagY7ntM-smsm0s6QmiPULWkqxBE7XP2jCA68WaDTZc-1Vql1hMYSx6-9vjkA_YrJaUjLCDiSvZGLYeci44EnaGfzVoWGMlsU5sm0iqyHvD3LOVzgoa_ydY8NSJUszDtr8hDF9RDj8srLfwsJBnwFX2TG_qTdWze2E7s3o5u7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7238deb5ae.mp4?token=oYkOvbo8LTtf60IERJG5WrpLvgaiIMXwaOTgGdyHvcKMPQy778Rm90_ZtpnCs-BjEQa7YDm_htcjpX-qoRRdH-gAMLewYXVrOVU1GULA2_NR-x3OwWq8KoxfltjqfL4Z3yxCHRJXn80tpiAknGoCf-e7cUrtCFffFZGzgiZlyLxtHagY7ntM-smsm0s6QmiPULWkqxBE7XP2jCA68WaDTZc-1Vql1hMYSx6-9vjkA_YrJaUjLCDiSvZGLYeci44EnaGfzVoWGMlsU5sm0iqyHvD3LOVzgoa_ydY8NSJUszDtr8hDF9RDj8srLfwsJBnwFX2TG_qTdWze2E7s3o5u7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚰️
R.I.P?</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/archivetell/5231" target="_blank">📅 22:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⚰️
R.I.P?</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/5230" target="_blank">📅 22:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آموزش بازی های انلاین با پینگ خوب برروی ویندوز با استفاده از روش SNI Spoofing
موارد مورد نیاز:
اتصال به Sni Spoofing
v2rayng
نرم افزار Windscribe که از قبل توش اکانت داشتید حتی اکانت فری و از قبل بهش لاگین کردید .(الان نمیشه بهش لاگین کرد اگه کسی روشی داره بگه بهمون )
شروع:
فرض بر این میگیریم شما با sni وصل هستید به اینترنت ازاد
روی v2ray پروکسی رو بذارید روی Clear system proxy و اصلا نباید حالت TUN روشن باشه .
حالا باید توی تنظمیات وایندسکرایب این تنظیمات رو اعمال کنید :
1-در بخش CONECTION روی split tunneling بزنید و بذارید روی Exclusive و در بخش app همون صفحه روی دکمه + بزنید و برنامه SNI SPOOFING رو پیدا کنید و اضافه ش کنید و مطمین بشید تیکش سبز باشه .
2-برگردید به بخش CONECTION و در قسمت Proxy setting و در بخش پروکسی تغییرش بدید به HTTP و ادرس و پورت زیر رو بذارید
127.0.0.1
10808
3-دوباره برگردید به بخش connection و Firewall رو بذارید روی حالت Manual
4- بخش conncetion Mode رو بذارید روی حالت manual و پروتوکل TCP و پورت 443
دقت کنید فقط پروتوکل TCP رو میتونید با این روش بهش وصل بشید و پینگ خوبی بهتون میده اگه اینترنت نرمالی داشته باشید .
سرور هم میتونید از المان فرانکفورت یا فرانسه جاردین استفاده کنید.
با این روش اینترنت شما مستقیم از وایندسکرایب گرفته میشه که هم اینترنت تمیزی بهتون میده که همه سایت ها و اپلیکیشن ها باز میشن هم پینگ خوبی بهتون میده.</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/archivetell/5229" target="_blank">📅 22:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">sni spoofing
وصله
امنه ، راحت استفاده کنید ، به حرف اونا که میگن مشکل داره و ... گوش نکنید ، واسه سود خودشون اینارو میگن</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/5227" target="_blank">📅 21:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5226">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel</strong></div>
<div class="tg-text">https://seup.shop/f/nn3o5
از حالت فشرده خارج میکنید میرید توی فولدرش
بعد sni-spoof-rs.exe رو راست کلیک میکنید و administrator باز میکنید
بعد میرید داخل ویتوری به این کانفیگ وصل میشید و تمام
trojan://humanity@127.0.0.1:40443?security=tls&sni=www.creationlong.org&insecure=1&allowInsecure=1&type=ws&host=www.creationlong.org&path=%2Fassignment#Technologia%20%3A%20Poland
توی تلگرام با این پروکسی وصل شید
tg://socks?server=127.0.0.1&port=10808
با فایر فاکس هم میتونید برید پروکسی تنظیم کنید و استفاده کنید راحت
برای کروم باید foxyproxy داشته باشید یا مشابه این اکستنشن
1-اگه براتون وصل نشد نت گوشی رو شیر کنید و امتحان کنید
2-فایل config.json رو میتونید باز کنید وبجای ایپی
104.19.229.21
و ادرس
hcaptcha.com
چیز دیگری امتحان کنید
3- بجای کانفیگ هم میتونید کانفیگ دیگه پیدا کنید که اهدا شده
لینک داخلی v2ray ویندوز
https://seup.shop/f/zp9bi</div>
<div class="tg-footer">👁️ 687 · <a href="https://t.me/archivetell/5226" target="_blank">📅 21:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">لینک داخلی شیر و خورشید
دانلود</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/5224" target="_blank">📅 20:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">IP,SNI
185.141.106.238
,
a77.net.akamai.net
185.88.178.196
,
a184.net.akamai.net
185.141.106.238
,
ak.net.akamaized.net
185.50.37.52
,
a77.net.akamai.net
185.141.106.238
,
ds-aksb.akamaized.net
185.50.37.52
,
a104.net.akamai.net
185.88.178.196
,
ds-aksb.akamaized.net
185.141.106.238
,
a104.net.akamai.net
185.88.178.196
,
a77.net.akamai.net
185.50.37.52
,
a184.net.akamai.net
185.137.25.214
,
a248.e.akamai.net
185.88.178.196
,
a104.net.akamai.net
185.141.106.238
,
a184.net.akamai.net
185.88.178.196
,
a248.e.akamai.net
164.138.17.122
,
a184.net.akamai.net
185.88.178.196
,
ak.net.akamaized.net
185.50.37.52
,
ds-aksb.akamaized.net
185.137.25.214
,
a184.net.akamai.net
185.137.25.214
,
a104.net.akamai.net
185.141.106.238
,
a248.e.akamai.net
185.50.37.52
,
ak.net.akamaized.net
185.50.37.52
,
a248.e.akamai.net
185.137.25.214
,
ds-aksb.akamaized.net
185.137.25.214
,
a77.net.akamai.net
185.208.174.167
,
a77.net.akamai.net
185.208.174.167
,
a184.net.akamai.net
185.208.174.167
,
a248.e.akamai.net
185.137.25.214
,
ak.net.akamaized.net
185.208.174.167
,
a104.net.akamai.net
185.208.174.167
,
ak.net.akamaized.net
185.208.174.167
,
ds-aksb.akamaized.net
37.191.95.70
,
a248.e.akamai.net
37.191.95.70
,
ak.net.akamaized.net
37.191.95.70
,
a184.net.akamai.net
37.191.95.70
,
ds-aksb.akamaized.net
37.191.95.70
,
a104.net.akamai.net
37.191.95.70
,
a77.net.akamai.net
برای شیر خورشید
تست شده رو نت ایرانسل
Sni
a248.e.akamai.net
a77.net.akamai.net
a104.net.akamai.net
a184.net.akamai.net
ds-aksb.akamaized.net
ak.net.akamaized.net
Ip
185.88.178.196
185.50.37.52
185.141.106.238
185.137.25.214
164.138.17.122
185.208.175.228
185.208.174.167
5.160.13.85
5.160.13.85
37.191.95.70</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/archivetell/5223" target="_blank">📅 20:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">برای شیر و خورشید
IP,SNI
185.141.106.238
,
aparat.com
37.191.95.70
,
snapp.ir
78.39.234.140
,
snapp.ir
81.91.145.2
,
snapp.ir
185.141.106.238
,
telewebion.com
81.91.145.2
,
digikala.com
78.39.234.140
,
varzesh3.com
81.12.72.218
,
varzesh3.com
185.141.106.238
,
digikala.com
37.191.95.70
,
aparat.com
37.191.95.70
,
bmi.ir
185.137.25.214
,
aparat.com
37.191.95.70
,
digikala.com
80.191.243.226
,
aparat.com
80.191.243.226
,
bmi.ir
80.191.243.226
,
snapp.ir
185.137.25.214
,
telewebion.com
78.39.234.140
,
digikala.com
80.191.243.226
,
digikala.com
37.191.95.70
,
telewebion.com
78.39.234.140
,
bmi.ir
81.91.145.2
,
bmi.ir
109.72.197.1
,
varzesh3.com
109.72.197.1
,
telewebion.com
109.72.197.1
,
bmi.ir
185.137.25.214
,
varzesh3.com
109.72.197.1
,
aparat.com
185.141.106.238
,
varzesh3.com
81.91.145.2
,
telewebion.com
78.39.234.140
,
aparat.com
81.12.72.218
,
aparat.com
185.141.106.238
,
bmi.ir
109.72.197.1
,
snapp.ir
78.39.234.140
,
telewebion.com
81.91.145.2
,
aparat.com
5.160.128.142
,
telewebion.com
81.91.145.2
,
varzesh3.com
80.191.243.226
,
telewebion.com
81.12.72.218
,
telewebion.com
185.141.106.238
,
snapp.ir
81.12.72.218
,
digikala.com
5.160.128.142
,
bmi.ir
5.160.128.142
,
varzesh3.com
5.160.128.142
,
snapp.ir
5.160.128.142
,
aparat.com
185.137.25.214
,
snapp.ir
80.191.243.226
,
varzesh3.com
185.137.25.214
,
digikala.com
5.160.128.142
,
digikala.com
185.137.25.214
,
bmi.ir
81.12.72.218
,
snapp.ir
109.72.197.1
,
digikala.com
81.12.72.218
,
bmi.ir
37.191.95.70
,
varzesh3.com
iP
31.214.169.244
185.109.61.27
46.32.31.30
37.255.133.30
37.191.76.110
80.191.243.226
185.141.106.238
81.12.72.218
37.191.95.70
63.141.252.203
142.54.178.211
5.160.13.85
178.252.128.66
94.130.13.19
2.23.168.254
2.23.168.144
78.39.234.140
109.72.197.1
185.137.25.214
2.23.168.7
78.157.41.60
2.23.168.96
185.208.175.228
81.91.145.2
2.23.168.47
185.255.91.60
2.23.170.80
2.23.168.213
2.23.168.174
65.109.34.234
5.160.128.142
SNi
snapp.ir
varzesh3.com
digikala.com
telewebion.com
bmi.ir
aparat.com</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/5222" target="_blank">📅 20:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ArchiveTel
pinned «
ربات چنل راه اندازی شد
🔥
تضمینی ، سرعت بالا و پایدار  قیمت عالی  @ArchiveTellbot  آموزش ساده خرید تو پست بعدی..
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/5221" target="_blank">📅 19:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NkRY_Vc42XGfJI2qeUxSwQFEUQGu-DKRswWz9l0g5pvoB9KMVRe0e5bCQyo0zc4hYXensLLGxJGbO-4jwXdSR7KM9puiVJvyp1zMeg5jNua-mDYaqQODFWEVkimXHyUDyRDRab8Ots3aAtKkkU8_bKR7xpeY-yg73O9zFbHcDH0QcOPCklCFf_awY34DU2hDdZI5NHQG8GR35djZJ36rPU-ZOrdCbNbMZKAbG_AQYVp8lsoFH3t_UK3uJAjPNyhWvADgW3J7mtVKOjmHHqIoHHPOeAE-WGv0SA5ovQr4E0od84h3Jt-xTigZoakZMAob-9vGbND5iTfNTiWX9VqJmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnk29o457HngB6h8l_tRPdtwwYsLocr5fiupXeuF4DA3TaBjiGgkIWHv5ONCoLPtPFjB7iRxzqWKn_tpgZj-9aa-t-9P1NQ2qrnnyNkl5UsMJ-lFBA52YY2vogeHwKK_JjzOz9OYLQpDmvKZT0co-5Ts_I62GNXIda-ql3Do2p9KR8U48WEAYjfZt_Q9LhyrJoFbednugid5ZfDWdb27lDBQYPYdXtUvhd8ExkcfiEfAWkdLzpb0alTKdo-WJ-K7Mx7LuUdLBaN3n_79qiuLMcifmuRSWSsa3Bc93wOY0Sem23C5r7qRfljTKVHBicy438Z3pgHpo9KCanv74Ec75g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرامپت تبدیل تصویر معمولی به تصویری که انگار در یک کتاب کودکانه قدیمی اروپای شرقی دهه ۸۰ پیدا شده است
Turn this photo into a strange vintage Soviet children's book illustration with grotesque humorous cartoon energy. Use thin shaky black ink lines, awkward anatomy, elongated limbs, uncomfortable facial expressions, chaotic movement, weird proportions, sparse composition, and intentionally clumsy drawing style. Make the characters look slightly absurd, nervous, and ridiculous rather than cute. Use pale faded watercolor washes, dirty paper texture, uneven coloring, washed-out muted colors, lots of empty space, careless sketchy linework, and rough old-print illustration texture. Keep the background minimal and random, with small strange details and loose doodles. The mood should feel weird, humorous, slightly unsettling, and authentically like an old Eastern European children's book illustration from the 1980s. Do NOT make it polished, aesthetic, modern, cute, detailed, or realistic.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/5219" target="_blank">📅 18:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5218">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ربات های کاهش حجم فیلم رایگان
@AdaptiveVideoBot
@Compreseebot
@mediaEasyBot
@wecompress_bot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/archivetell/5218" target="_blank">📅 17:49 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚀
آپدیت حیاتی و بسیار مهم فیلترشکن محبوب mhrv-rs (نسخه v1.9.33) منتشر شد!
---
رفقا سلام!
✋
ابزار
mhrv-rs
(نسخه‌ی سریع و سبک فیلترشکن رله‌ی گوگل به زبان Rust) رو که یادتونه؟ همون متد خفنی که ترافیک شما رو پشت دامنه‌ی اصلی گوگل مخفی می‌کرد و کاملاً هم رایگان بود.
حالا یه آپدیت جدید براش اومده که دست روی بزرگترین باگِ این متد، یعنی
«هدر رفتن سهمیه روزانه جیمیل در زمان بیکاری»
گذاشته و اون رو کاملاً برطرف کرده!
🎯
تمرکز اصلی این آپدیت: جلوگیری از مصرف بی‌رویه‌ی سهمیه گوگل (Google Quota)
توی نسخه‌های قبلی، حتی وقتی در حال وب‌گردی نبودید و سیستم شما کاملاً بیکار (Idle) بود، کلاینت مدام درخواست‌های خالی (Empty Polls) به اکانت جیمیل‌تون می‌فرستاد تا اتصال رو زنده نگه داره. این کار باعث می‌شد سهمیه رایگانِ ۲۰ هزارتایی روزانه‌ی شما خیلی سریع و بیهوده تموم بشه.
⚡️
تغییرات و بهینه‌سازی‌های فنی نسخه v1.9.33:
🔸
سیستم هوشمند Keepalive Backoff:
در حالت Full Tunnel، وقتی اتصال شما کاملاً بیکار بشه، برنامه با یک مکانیزم هوشمند و سخت‌گیرانه‌تر، فرستادن پینگ‌های متوالی رو متوقف می‌کنه تا سهمیه‌تون الکی نسوزه.
🔸
کاهش چشمگیر لودِ سرور:
با این کار، بارِ ترافیکیِ درخواست‌ها روی «گوگل اپس اسکریپت» و
tunnel-node
در زمان‌های سکوتِ شبکه به شدت کاهش پیدا می‌کنه.
🔸
پشتیبانی از ناوگان‌های ترکیبی (Mixed Fleets):
اگر چند دیپلوی مختلفِ جیمیل داشته باشید و حداقل یکی از اونا قابلیت Long-poll سالم رو داشته باشه، کلاینت هوشمندانه ارتباط رو به صورت Round-robin حفظ می‌کنه تا دیتای برگشتی از سمت سرور قفل نشه و اتصالتون همیشه پایدار بمونه.
---
📥
لینک‌های دانلود مستقیم آخرین نسخه (v1.9.33):
📱
نسخه اندروید (Universal):
🔗
https://github.com/therealaleph/MasterHttpRelayVPN-RUST/releases/download/v1.9.33/mhrv-rs-android-universal-v1.9.33.apk
💻
نسخه ویندوز (Windows 64-bit):
🔗
https://github.com/therealaleph/MasterHttpRelayVPN-RUST/releases/download/v1.9.33/mhrv-rs-windows-amd64.zip
🌐
صفحه گیت‌هاب پروژه (جهت دسترسی به نسخه‌های مک، لینوکس و کدهای جدید):
🔗
https://github.com/therealaleph/MasterHttpRelayVPN-RUST
📌
#آپدیت
#گوگل_رله
#نت_ملی
#رایگان
#mhrv_rs
#Rust
#Google
#Bypass
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/5217" target="_blank">📅 17:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G4chACZ9tKl6wqJEzAN2GSi6UPBnp99fftmZq59Gj16tyIfL7Cvh0rBBdwGovOO7hWvxfYFV_eS08Y8eKByweo2VfYs7y9g9ZnG3cpnrJWbCWoaX0OAjoxTfjGtfPOaOCHrAf9vOpojsaxNCtLEScpt5r5L0HCjlY56yqsg6gfqNlWEJB356NKBBYRsMo8lVJQh_aPSVkibEmVO8Ne8Sad4u2sIcuygw9PUxYYuwmaTjGbl_E21eFLsrhFQISyPt15F2wlED_Bet_ONeWGqgu5ndBvnoJ4WFSqO8MsCFVEbcZnqDWXxez2LhbeVyZzoEoxuk2RNZ-Vkm-QzPPYPLnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qXGEKtiy6mJmkMMpHLVcr7joOKcpEcpp2ElI23fPhbN4pjMCHfixBXqcJ5rAhX3Y-WLWd9Sy0mqPLxnk8w3BmamQhDNkVETJsOzrGdKnuZ1ZXdcxaMAUSbG4Nq6Dx3uAMlmkRDP1TPokuHgTRbOR9_xvMfPW3EazlCQPBkPBO1BFwgW5mXaKqgWwq_AdorVFNbhGbq2EVDZsVUTqEPTlsYPezm-nfvAuARF-W9Di_tHyuk62z4Q61MULULPJ0aepTKPm9nB-mULB_qh2DQEzbo2GO-oEduzu_9eL3R9ZJzD7Hh_fKsDGtgTT1_5Vb6iX2fZvGg0loyk2_bAKt7JVvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
آپدیت بزرگ ابزار EzyTel (نسخه modified_r1): مرور کاملاً آزاد و بدون فیلتر تلگرام!  ---  رفقا حتماً با متد بی‌نظیرِ باز کردن و خواندن محتوای کانال‌های تلگرام از طریق زیرساخت گوگل ترنسلیت (مثل ابزار telemirror) آشنا هستید. حالا یکی از ممبرهای عزیز و هنرمند…</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/5215" target="_blank">📅 17:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ezytel-v2_modified-r1@ArchiveTell.zip</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/archivetell/5214" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آپدیت متد ezytel
باز کردن محتوای تلگرام با استفاده از گوگل ترنسلیت(یچیزی تو مایه های telemirror)
یکی از ممبرای عزیز ، ایزی تل رو ویرایش کرده و باگ هاشو برطرف کرده
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/5214" target="_blank">📅 17:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚀
آپدیت بزرگ ابزار EzyTel (نسخه modified_r1): مرور کاملاً آزاد و بدون فیلتر تلگرام!
---
رفقا حتماً با متد بی‌نظیرِ باز کردن و خواندن محتوای کانال‌های تلگرام از طریق زیرساخت گوگل ترنسلیت (مثل ابزار telemirror) آشنا هستید. حالا یکی از ممبرهای عزیز و هنرمند کانال، اسکریپت
EzyTel
رو کاملاً بهینه‌سازی کرده و یک نسخه‌ی Modified بدون باگ و همه‌کاره ازش داده بیرون.
✨
تغییرات و بهبودهای کلیدی در نسخه modified_r1:
🔸
تغییرات ظاهری و UI جدید:
• اضافه شدن دارک مود اختصاصی با رنگ‌بندی شیکِ Telegram Web.
• شیشه‌ای و شفاف شدن هِدِر کانال‌ها همراه با حذف آواتار و اسم فرستنده برای تمیزتر شدن ظاهر پست‌ها.
• امکان فول‌اسکرین، زوم و جابه‌جایی (Pan) روان با کلیک روی تصاویر کانال.
• رفع مشکل کامل هم‌ترازی (RTL) در متن‌های ترکیبی فارسی و انگلیسی.
• نمایش ارورها به‌صورت Toastهای نرم و محو شونده بجای پاپ‌آپ‌های (Alert) رو اعصاب!
🔸
امکانات کاربردی اضافه شده:
• قابلیت اضافه یا حذف کردن کانال‌ها مستقیماً از داخل محیط خود برنامه (دیگه نیازی به ادیت دستی فایل
channels.txt
نیست!).
• مرتب‌سازی خودکار و هوشمند لیست کانال‌ها بر اساس جدیدترین پیام ارسال شده.
• باز شدن کامل باکس Quoteها برای نمایش متون طولانی و امکان کپی شدن متن داخل کوت با کلیک روی آن.
• اضافه شدن دکمه اختصاصی COPY برای کپی کردن کل متن یک پست با یک کلیک.
🔸
ارتقای فنی و سیستم ضد بلاک (Anti-Block):
• حذف کامل دیتای اضافه و آشغال‌های گوگل ترنسلیت از لینک‌ها و باز شدن آن‌ها در تب جدید.
• استفاده پیش‌فرض ابزار از سیستم سورس
curl
روی پروتکل پرسرعت HTTP/2.
• اضافه شدن دامنه‌های بیشتر از سرورهای گوگل و تزریق Headerها و User-Agentهای کاملاً تصادفی برای دور زدن لیمیت‌ها.
---
⚠️
چطور باگ Rate Limit (خطای Something went wrong) گوگل رو دور بزنیم؟
گوگل روی حجم درخواست‌های پشت‌سرهم حساسه. برای اینکه لیمیت نشید:
1️⃣
خیلی سریع و رگباری روی کانال‌ها کلیک نکنید.
2️⃣
از لیست‌های بیش از حد سنگین و شلوغ استفاده نکنید.
✔️
راهکار رفع لیمیت:
اگر خطای Something went wrong گرفتید، کافیه ۲ الی ۳ دقیقه صبر کنید، یا اینکه یک‌بار حالت هواپیمای گوشی رو روشن/خاموش کنید (یا نت رو بین 4G و 3G سوییچ کنید) تا آی‌پیتون عوض بشه. (این ترفند روی آی‌پی ثابت وای‌فای خانگی جواب نمیده).
❌
محدودیت‌های دائمی:
عدم دانلود فایل‌ها و ویدیوها، کیفیت پایین تصویر و عدم نمایش ایموجی‌های پرمیوم تلگرام به دلیل محدودیت‌های خودِ ساختار گوگل ترنسلیت هستن و کاریش نمیشه کرد. این متد تا زمانی که گوگل در ایران باز باشه، تضمینی کار می‌کنه!
---
🛠️
راهنمای راه‌اندازی قدم‌به‌قدم روی ویندوز و اندروید:
💻
اجرا در ویندوز:
۱. برنامه معروف XAMPP رو دانلود و نصب کنید.
۲. پوشه
ezytel
رو داخل پوشه
htdocs
(محل نصب زامپ) کپی کنید.
۳. برنامه XAMPP Control Panel رو باز کنید و سرویس
Apache
رو استارت (Start) کنید.
۴. مرورگر رو باز کنید و آدرس
localhost/ezytel
یا
127.0.0.1/ezytel
رو بزنید. (اگر نیومد، پورت درج شده جلوی آپاچی رو ته آدرس بذارید، مثل
localhost:80/ezytel
).
🤖
اجرا در اندروید:
۱. برنامه KSWeb رو از استورها نصب و اجرا کنید.
۲. پوشه
ezytel
رو داخل پوشه
htdocs
که در حافظه داخلی گوشیتون ساخته شده کپی کنید.
۳. در برنامه KSWeb به تب APACHE و PHP برید و گزینه‌ی
Enable Server
رو روشن کنید.
۴. مرورگر گوشی رو باز کنید و آدرس
localhost:8000/ezytel
یا
127.0.0.1:8000/ezytel
رو وارد کنید. (ترجیحاً از آپاچی استفاده کنید نه Lighttpd).
📌
#آموزش
#ایزی_تل
#تلگرام_آفلاین
#نت_ملی
#گوگل_ترنسلیت
#EzyTel
#Bypass
#Telemirror
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/5213" target="_blank">📅 17:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
معرفی Cloak: مدیریت حرفه‌ای و ساده‌ی SNI Spoofing روی دسکتاپ!
---
رفقا سلام!
✋
خیلی‌هاتون درگیرِ تنظیماتِ پیچیده‌ی «اسنیفینگ» (SNI Spoofing) توی محیط ترمینال و کنسول بودید. امروز یه ابزار فوق‌العاده به اسم
Cloak
رو معرفی می‌کنیم که کار رو براتون گرافیکی و به‌شدت راحت کرده!
✨
چرا Cloak خاصه؟
این ابزار یه کلاینتِ دسکتاپ (مخصوص مک و ویندوز) هست که خودش همه کارهای پشت‌پرده مثل تزریق SNI فیک (Fake SNI) و مدیریت کانفیگ‌ها رو انجام میده. دیگه نیازی نیست درگیر دستورات پیچیده‌ی ترمینال بشید.
🛠
قابلیت‌های کلیدی:
🔸
مدیریت یکپارچه: وارد کردن فایل‌های کانفیگ V2Ray، Trojan و... با درگ اند دراپ (Drag & Drop).
🔸
تست پینگ و سلامت: تست هم‌زمانِ همه‌ی کانفیگ‌ها و انتخاب سریع‌ترین سرور.
🔸
سیستم پروکسی هوشمند: اشتراک‌گذاری کانکشن با دستگاه‌های دیگه توی شبکه (LAN) تنها با یک کلیک!
🔸
پایداری بالا: مدیریتِ عالیِ Tunnel ها و پایداریِ کانکشن.
💻
آموزش راه‌اندازی سریع:
1️⃣
برنامه رو از لینک گیت‌هاب دانلود و نصب کنید.
2️⃣
در بخش Settings، دکمه «Restore Default» رو بزنید تا کانفیگ اولیه (که شامل آی‌پی‌های تمیزِ پیش‌فرض هست) بارگذاری بشه و بعد Save کنید.
3️⃣
به بخش Profiles برید، روی دکمه Add بزنید و کانفیگ‌های V2Ray/Trojan که دارید رو وارد کنید.
4️⃣
بعد از اضافه شدن، روی کانفیگ کلیک کنید و دکمه Ping رو بزنید. اگر پینگ داد، یعنی کانفیگ سالمه.
5️⃣
دکمه Connect رو بزنید تا پروکسی فعال بشه. (برای اشتراک‌گذاری با گوشی، دکمه LAN رو توی تنظیمات فعال کنید و آی‌پی و پورتی که میده رو توی گوشی وارد کنید).
📥
دانلود برنامه (ویندوز و مک):
صفحه رسمی پروژه در گیت‌هاب:
🔗
https://github.com/PechenyeRU/FakeSNI
⚠️
نکته مهم: این ابزارها برای دور زدن محدودیت‌هاست، همیشه امنیت و رعایت حریم خصوصی رو در اولویت قرار بدید.
📌
#معرفی_ابزار
#Cloak
#SNI_Spoofing
#نت_ملی
#فیلترشکن
#ویندوز
#مک
#v2ray
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/5212" target="_blank">📅 17:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نتلیفای بای بای</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/archivetell/5210" target="_blank">📅 14:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚀
آموزش جامع و قدم‌به‌قدم دور زدن فیلترینگ با روش SNI Spoofing
روی سرور ایران (ترکیب با پنل 3x-ui)
در این آموزش قصد داریم با استفاده از یک ابزار بسیار سبک و قدرتمند (نوشته شده به زبان Rust)، سیستم SNI Spoofing را روی سرور ایران راه‌اندازی کنیم. این ابزار به ما کمک می‌کند با جعل نام دامنه (مثلاً استفاده از یک سایت تمیز مثل hcaptcha)، سیستم فیلترینگ (DPI) را فریب دهیم و ترافیک را با موفقیت به سرور خارج متصل کنیم.
###
🛠
مرحله اول: دانلود و انتقال ابزار به سرور ایران
ابتدا باید فایل اجرایی پروژه را روی سرور ایران خود قرار دهیم. برای این کار دو روش دارید:
روش اول (پیشنهادی - مستقیم از طریق ترمینال):
وارد ترمینال (SSH) سرور ایران شوید و دستور زیر را وارد کنید تا فایل مستقیماً از گیت‌هاب دانلود شود:
wget https://github.com/therealaleph/sni-spoofing-rust/releases/latest/download/sni-spoof-rs-linux-amd64
روش دوم (از طریق SFTP):
فایل sni-spoof-rs-linux-amd64 را از گیت‌هاب پروژه دانلود کرده و با نرم‌افزارهایی مثل WinSCP یا FileZilla، آن را در دایرکتوری روت (/root/) سرور ایران آپلود کنید.
###
⚙️
مرحله دوم: ساخت فایل کانفیگ (JSON)
حالا باید به برنامه بگوییم که روی چه پورتی گوش دهد و ترافیک را به کجا بفرستد.
۱. در ترمینال سرور، دستور زیر را بزنید تا یک فایل جدید باز شود:
sudo nano config.json
۲. کدهای زیر را دقیقاً در محیط باز شده کپی (Paste) کنید:
{
"graceful_shutdown_sec": 0,
"listeners": [
{
"listen": "127.0.0.1:40443",
"connect": "104.19.229.21:443",
"fake_sni": "hcaptcha.com"
}
]
}
💡
توضیح مقادیر مهم:
*
listen:
آدرس و پورتی است که برنامه روی سرور ایران منتظر دریافت ترافیک می‌ماند (اینجا روی لوکال‌هاست و پورت 40443 تنظیم شده).
*
connect:
آی‌پی سرور مقصد شماست. در این مثال از آی‌پی تمیز کلودفلر (
104.19.229.21
) با پورت 443 استفاده شده است.
*
fake_sni:
دامنه‌ای است که می‌خواهیم فیلترینگ را با آن فریب دهیم (در اینجا
hcaptcha.com
).
۳.
نحوه ذخیره فایل:
کلیدهای Ctrl + X را روی کیبورد بزنید. سپس حرف Y را تایپ کنید و در نهایت Enter بزنید تا فایل ذخیره شود.
###
🏃‍♂️
مرحله سوم: دسترسی دادن و اجرای دائمی برنامه
۱. ابتدا باید به فایلی که دانلود کردیم، اجازه اجرا (Execute) بدهیم:
sudo chmod +x sni-spoof-rs-linux-amd64
۲.
اجرای برنامه در پس‌زمینه:
اگر برنامه را عادی اجرا کنید، با بستن ترمینال برنامه متوقف می‌شود. برای اینکه برنامه همیشه روشن بماند، از ابزار Screen یا Tmux استفاده می‌کنیم. دستور زیر را بزنید تا یک سشن جدید باز شود:
screen -S spoofer
۳. حالا برنامه را با فایل کانفیگ اجرا کنید:
sudo ./sni-spoof-rs-linux-amd64 config.json
*(اگر اروری نداد، یعنی برنامه با موفقیت در حال کار است. حالا کلیدهای Ctrl + A و سپس D را بزنید تا برنامه در پس‌زمینه سرور در حال اجرا باقی بماند).*
###
🔗
مرحله چهارم: اتصال کانفیگ به پنل 3x-ui
حالا که Spoofer در پس‌زمینه سرور ایران کار می‌کند، باید پنل 3x-ui را طوری تنظیم کنیم که ترافیک کاربران را به این برنامه تحویل دهد.
۱. تنظیم اینباند (Inbound - ورودی):
وارد پنل 3x-ui سرور ایران شوید. یک کانفیگ ورودی (مثلاً VLESS یا Trojan) با پورت دلخواه بسازید و به کاربر بدهید. (این قسمت دقیقاً مثل ساخت کانفیگ‌های عادی شماست و تغییری ندارد).
۲. تنظیم اوتباند (Outbound - خروجی) - بخش اصلی:
حالا باید ترافیک را از ایران به خارج بفرستیم.
* در پنل 3x-ui به بخش
Outbounds
(یا Xray Config / Routing بسته به نسخه پنل) بروید.
* یک Outbound جدید ایجاد کنید.
* تنظیمات این Outbound باید
دقیقاً مشابه کانفیگ سرور خارج شما
باشد (همان کانفیگی که در نرم‌افزارهایی مثل v2rayN روی ویندوز وارد می‌کنید؛ با همان UUID، نوع شبکه، TLS و...).
*
تغییر کلیدی:
فقط دو فیلد زیر را تغییر دهید:
*
Address (آدرس):
را روی
127.0.0.1
تنظیم کنید.
*
Port (پورت):
را روی 40443 بگذارید.
۳. تنظیم مسیریابی (Routing):
در بخش تنظیمات Routing پنل، یک قانون (Rule) جدید اضافه کنید و بگویید هر ترافیکی که از Inbound (کانفیگ کاربر) وارد شد، به این Outbound (که ساختید) هدایت شود.
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/archivetell/5208" target="_blank">📅 13:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">https://seup.shop/f/nn3o5 از حالت فشرده خارج میکنید میرید توی فولدرش بعد sni-spoof-rs.exe رو راست کلیک میکنید و administrator باز میکنید بعد میرید داخل ویتوری به این کانفیگ وصل میشید و تمام  trojan://humanity@127.0.0.1:40443?security=tls&sni=www.creationl…</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/5207" target="_blank">📅 12:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
برگ‌ریزون‌ترین آپدیت جمینای؛ کلونِ دیجیتالیِ خودت رو بساز!
🚨
بچه‌ها، قضیه آواتار جدید جمنای (Gemini) خیلی دیوانه‌کننده‌تر از اون چیزیه که فکرشو می‌کردیم!
🤯
این بار گوگل رسماً مرزهای هوش مصنوعی رو جا به جا کرده. تو این آپدیت جدید، جمنای قابلیتی آورده که می‌تونید
دقیقاً با چهره و صدای خودتون
ویدیو تولید کنید!
🎬
🎙️
یعنی چی؟ یعنی کافیه عکس و صدای خودتون رو بهش بدید، تا یه آواتار فوق‌العاده طبیعی و واقعی ازتون بسازه. این آواتار می‌تونه هر متنی رو با لحن، صدا و میمیک صورت خودِ شما بخونه و یه ویدیوی کامل و بی‌نقص تحویلتون بده!
🔥
دیگه برای تولید محتوا حتی نیاز نیست جلوی دوربین بشینید؛ خودِ مجازی‌تون با بالاترین کیفیت همه کارا رو انجام میده! سرعت پیشرفت هوش مصنوعی هم به شدت جذابه، هم یه نمه ترسناک شده...
😨
فکر می‌کنید این تکنولوژی چقدر قراره کار یوتیوبرها و تولیدکننده‌های محتوا رو عوض کنه؟ شما حاضرین آواتار خودتون رو بسازین؟
🤔
👇
#Gemini
#هوش_مصنوعی
#آواتار
#تولید_محتوا
#تکنولوژی
#آپدیت_جدید
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/archivetell/5206" target="_blank">📅 12:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eup2GGaxki60bi-8Af2qUNuCqdoTbTjVLpBit3_HeXM2bhqpt3tbzDdBG6zjdoimF8svyoc_wyNT9bgkSeK7zIcbm9ndNhHCSHDKPxdDk2s62XewpJ8uBRagHAIQTJwN72cjWdI_YA-ugbmKPK9ilhkuAtAXr-Hhj6lUwcGiAq1pTY0u8cY7XkS90k77SVX1XaKKuwpJm5UYyJoR3f9dDDiFRO5j2KCQ3ZxnYiPlGB-z4u1Tz63R-b3SB5XdiphrjIG_Vw80pF1wnoorbp3BDGkEN80lAPLc9veqI0yGIjugza12TSHIoA8KZkk3M523Ea0rYvIjcyFECdWsiw2u_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمینای ۳.۵ اومد
پر قدرت تر از همیشه
+بنچمارک هاش
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/archivetell/5204" target="_blank">📅 11:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فقط باید داخل سرور اینو بزنید
ping
104.19.229.21
اگه پینگ بده میشه</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/archivetell/5203" target="_blank">📅 10:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">راه اندازی sni spoofing رو سرور ایران
کانفیگی که با این متد وصل هستید رو اوتباند کنید تو پنل و کانفیگ بسازید..
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/archivetell/5202" target="_blank">📅 10:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpb2to15uLHCCAFat81vO9rL293bxZcGlCpXO7UGThzuSxiOL6HwsdXefstIg5zD_poRM8BDWCS0Z1zHFGUcfLuLdUafNKSsOITM-NmBmQ6OpndUyUDNZaLjj-MXN09LxtcUIeeG3NThMLjwuVsYw4WfiGNLHdXHyli3TwDVdzDl7lklxPlANAugEn0kYqafkg0BQJavsbzXExn2MvXHeDM_uzNhyHLiANjF7yAuGm03Bm7xlMgeThvd7QN8WaBMcNY1rj7_bmNHFUjOWw1DGHRPp-3SIStC8Ub_I3-wtkrGqpBm1R5lrKfGLDehZ0fCQmFsz3xlRmvxfZwBNWWGFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Google I/O 2026
جمنای، جستجو، عینک‌های هوشمند
جدیدترین رویداد گوگل موجی از نوآوری‌های هیجان‌انگیز را به همراه داشته است!
🌟
از معرفی جمنای، تا به‌روزرسانی‌های پیشگامانه در جستجو که وعده نتایجی شخصی‌تر و کارآمدتر را می‌دهد، گوگل مرزها را بیش از همیشه گسترش می‌دهد. علاوه بر این، عینک‌های هوشمند گوگل بازگشته‌اند، اکنون با قابلیت‌های پیشرفته واقعیت افزوده و طراحی باریک‌تر، با هدف ادغام بی‌نقص دنیای مجازی با واقعیتی که روزانه در آن حرکت می‌کنیم.
🌐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/archivetell/5201" target="_blank">📅 09:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqk_lzP9Ls6MNFKaDSfXnwAds-sQatFmEVhaGecqMWyJWLDe-lJQX_GfNeDiUq0QyLFsfrPCqU-iNu-1P3_GwUYVQGwCGWNs2s53U7sO2SmqyN2wZNcOH5WzzXXt4hyfGok4VgjbBWoc_4cplUIBlKlObIv2RTwjJgV5AxGwGOnomfgP4QO2A_CPlLxF_5-N_eHWN0Kuut-iUUUS-xMZgDps1bEwzwP5MvGjULo1h0QPVjwV-kPtde5NGpk4xuzqz9vBVq2ZXjJDSZYi0YuQJiofQ2mf-bhtZ1LWe_ndb2JHzQlyIJMmlrya9PNy64EPUxP78Nr9a1uDOp354Tc30A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه Gemini 3.5 Flash منتشر شد
این نسخه به‌طور قابل توجهی قوی‌تر از Gemini 3.1 Pro است.
مهم‌ترین نکته این است که گوگل به مشکلات مربوط به عامل‌پذیری (agentness) به طور جدی پرداخته و به ویژه مدل را در این زمینه بهبود داده است. به عنوان مثال، نشان دادند که چگونه Gemini 3.5 Flash در ۱۲ ساعت یک سیستم عامل کوچک نوشت که می‌تواند Doom را اجرا کند. مدل Pro نیز وجود دارد و وعده داده شده که ماه آینده عرضه شود، قیمت‌های آن احتمالاً بسیار بالا خواهد بود.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/5200" target="_blank">📅 08:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e945b36d4.mp4?token=O182d73SXPgf74tWKphHBpI1BPtbpgHAQljPtnDNDjceNf8Zwvl6sTRH_WVRiLu5jQBD4xY1EaYIuUHJhZtwD7H0TCtjdccB-DT4sdE7rlXw__VD4YV9Ct0PiSl1aEGJL_AvjEVro14ctPhrlASkzEupoPeXZMo3gxcxTkPV2qThmF4z6Frox5VbKSU9sn3cyGwRcujVqVVbPZpOubg2DRNwmC4gOWAw5L_43GSqlJrMFZNtAM087fMp6sfBuPz7mJDuzkBbNnxG8eYmMXTFFGv1YI6zUiD29-7V96jj-pdh6B40cGz0cIykYXmAUrB2hk1-KcctfFw8bEQ6fM9WAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e945b36d4.mp4?token=O182d73SXPgf74tWKphHBpI1BPtbpgHAQljPtnDNDjceNf8Zwvl6sTRH_WVRiLu5jQBD4xY1EaYIuUHJhZtwD7H0TCtjdccB-DT4sdE7rlXw__VD4YV9Ct0PiSl1aEGJL_AvjEVro14ctPhrlASkzEupoPeXZMo3gxcxTkPV2qThmF4z6Frox5VbKSU9sn3cyGwRcujVqVVbPZpOubg2DRNwmC4gOWAw5L_43GSqlJrMFZNtAM087fMp6sfBuPz7mJDuzkBbNnxG8eYmMXTFFGv1YI6zUiD29-7V96jj-pdh6B40cGz0cIykYXmAUrB2hk1-KcctfFw8bEQ6fM9WAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو آپدیت جدید تلگرام ربات‌ها میتونن با همدیگه ارتباط برقرار کنن
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/5199" target="_blank">📅 08:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">https://seup.shop/f/nn3o5
از حالت فشرده خارج میکنید میرید توی فولدرش
بعد sni-spoof-rs.exe رو راست کلیک میکنید و administrator باز میکنید
بعد میرید داخل ویتوری به این کانفیگ وصل میشید و تمام
trojan://humanity@127.0.0.1:40443?security=tls&sni=www.creationlong.org&insecure=1&allowInsecure=1&type=ws&host=www.creationlong.org&path=%2Fassignment#Technologia%20%3A%20Poland
توی تلگرام با این پروکسی وصل شید
tg://socks?server=127.0.0.1&port=10808
با فایر فاکس هم میتونید برید پروکسی تنظیم کنید و استفاده کنید راحت
برای کروم باید foxyproxy داشته باشید یا مشابه این اکستنشن
1-اگه براتون وصل نشد نت گوشی رو شیر کنید و امتحان کنید
2-فایل config.json رو میتونید باز کنید وبجای ایپی
104.19.229.21
و ادرس
hcaptcha.com
چیز دیگری امتحان کنید
3- بجای کانفیگ هم میتونید کانفیگ دیگه پیدا کنید که اهدا شده
لینک داخلی v2ray ویندوز
https://seup.shop/f/zp9bi</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/archivetell/5198" target="_blank">📅 08:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">marzban_http_proxy_install_guide.md</div>
  <div class="tg-doc-extra">6.6 KB</div>
</div>
<a href="https://t.me/archivetell/5197" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🤔
راهنمای نصب Marzban روی سرور خام با HTTP Proxy.
در این فایل، مراحل نصب مرزبان روی سروری که دسترسی مستقیم به اینترنت بین‌الملل ندارد توضیح داده شده است.
قبل از اجرا، حتماً اطلاعات Proxy خودتان را جایگزین کنید و بعد از نصب، مرحله پاکسازی را انجام دهید.
‼️
﻿
توی این روش حد اقل به ۴۰۰ مگابایت پروکسی نیاز دارید.
💯
😊
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/archivetell/5197" target="_blank">📅 01:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚀
آپدیت فوری v2rayNG (نسخه v2.1.8) منتشر شد!
---
هنوز چند روزی از انتشار نسخه ۲.۱.۷ نگذشته بود که تیم توسعه‌دهنده نسخه
v2.1.8
رو برای رفع باگ‌های جزئی و بهبود عملکرد منتشر کرد.
✨
تغییرات مهم در نسخه v2.1.8:
🔸
پشتیبانی از SOCKS4/5: حالا می‌تونید لینک‌های اشتراک SOCKS4 و SOCKS5 رو هم مستقیماً وارد برنامه کنید.
🔸
بهبود نوتیفیکیشن سرعت: نمایش سرعت در نوار اعلان‌ها (Notification) حالا با ثبات و دقت بیشتری انجام می‌شه و از سیاست‌های جدیدِ نمایشِ وضعیت (مثل لیست گروه‌ها) هم پشتیبانی می‌کنه.
🔸
رفع باگ‌ها: مشکلات جزئی نسخه قبل برطرف شده تا پایداریِ اتصال بالاتر بره.
📥
لینک‌های دانلود مستقیم (نسخه 2.1.8):
📱
نسخه arm64-v8a (مخصوص اکثر گوشی‌های جدید - پیشنهاد اول):
🔗
https://github.com/2dust/v2rayNG/releases/download/2.1.8/v2rayNG_2.1.8_arm64-v8a.apk
📱
نسخه armeabi-v7a (مخصوص گوشی‌های قدیمی):
🔗
https://github.com/2dust/v2rayNG/releases/download/2.1.8/v2rayNG_2.1.8_armeabi-v7a.apk
📱
نسخه Universal (اگر پردازنده گوشیتون رو نمی‌دونید):
🔗
https://github.com/2dust/v2rayNG/releases/download/2.1.8/v2rayNG_2.1.8_universal.apk
📌
#آپدیت
#معرفی_ابزار
#اندروید
#فیلترشکن
#نت_ملی
#v2rayNG
#Xray
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/archivetell/5196" target="_blank">📅 00:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5195">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b104e89c3c.mp4?token=q6VuvyIqt8OkNdkHbW0WdcLuhB0H453SwKRUYjBF5kp02B0k0WMUDSLiU69jldfnOvRIKZDLMkCLe2ukgjt4NNRPXG90Cillm_RcFDTjNfXHka68Ttv5AZzDRAxUVNleoNYcsOU43cTj4u1q2iDkDL6wfaT82fcIEE-zlig17CKS_KPA75-iifGlbA1tQpfxKfMcS7IOH10sT4yw9BhuuzExoxl8kAYGetNQj_bIHU2SpP4U3D0LxOGFFQJdQwy-Wtf9KmWDFl3JybmIskXmi0k_gVwPTpVYsfJoHkyH-t_3He92n2SkiCZan7MYILQH2VnTsod8tmPFjH5er08eUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b104e89c3c.mp4?token=q6VuvyIqt8OkNdkHbW0WdcLuhB0H453SwKRUYjBF5kp02B0k0WMUDSLiU69jldfnOvRIKZDLMkCLe2ukgjt4NNRPXG90Cillm_RcFDTjNfXHka68Ttv5AZzDRAxUVNleoNYcsOU43cTj4u1q2iDkDL6wfaT82fcIEE-zlig17CKS_KPA75-iifGlbA1tQpfxKfMcS7IOH10sT4yw9BhuuzExoxl8kAYGetNQj_bIHU2SpP4U3D0LxOGFFQJdQwy-Wtf9KmWDFl3JybmIskXmi0k_gVwPTpVYsfJoHkyH-t_3He92n2SkiCZan7MYILQH2VnTsod8tmPFjH5er08eUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Sni spoof  ip : 104.19.229.21  sni : www.hcaptcha.com</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/archivetell/5195" target="_blank">📅 23:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاینترنت آزاد</strong></div>
<div class="tg-text">Sni spoof
ip :
104.19.229.21
sni :
www.hcaptcha.com</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/5194" target="_blank">📅 23:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">لیست SNI ها برای اینکه روی یه دامین همه نریزن.
three-cust.hcaptcha.com, stats.hcaptcha.com, www.hcaptcha.com,u.hcaptcha.com.
tg.hcaptcha.com, primary.haptcha.com, pat-internal.hcaptcha.com, jobs.hcaptcha.com,
hmt-lucid-neumann.hcaptcha.com, dashboard.hcaptcha.com, cached-queries.hcaptcha.com,
billing.hcaptcha.com, assets.hcaptcha.com, api.hcaptcha.com, analytics-beta.hcaptcha.com,
accounts.hcaptcha.com, a.hcaptcha.com, 47dilm9.mqwaa.dns.army, rel-I.top,
www-canary.hcaptcha.com,tractionrec.hcaptcha.com,tp.hcaptcha.com,
three-cust-imgs.hcaptcha.com, temple-gates.hcaptcha.com, styler.hcaptcha.com,
past-issuer.hcaptcha.com, _ health-check.hcaptcha.com, exchange.hcaptcha.com, email.hcaptcha.com,
abeling-masters.hcaptcha.com, pre.hcaptcha.com, fantasia-assets.hcaptcha.com,
proxy.hcaptcha.com, loader.hcaptcha.com, i2.hcaptcha.com, hmt-pensive-torvalds.hcaptcha.com
chunker.hcaptcha.com, analytics.hcaptcha.com, hcaptcha.com, newassets.hcaptcha.com,
charlie.hcaptcha.com, js.hcaptcha.com, imgs3.hcaptcha.com, challenge-tasks.hcaptcha.com,
serverless.hcaptcha.com, imgs2.hcaptcha.com, imgs.hcaptcha.com, factored-cognition.hcaptcha.com,
hiding.men, cf-3.payun.men,_mit.hcaptcha.com, risk-prod-srv.hcaptcha.com,
pst-sample.ncaptcha.com, sentry.ncaptcha.com, nmt-eloquent-mclaren.hcaptcha.com,
hmt-elegant-rosalind.hcaptcha.com, demo.hcaptcha.com</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/archivetell/5193" target="_blank">📅 22:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دانلود همه کلاینت ها با لینک داخلی
http://Files.en-javadian.ir
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/5192" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">لینک داخلی Happ ویندوز
دانلود</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/5190" target="_blank">📅 21:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMashaya</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2xIkv7apQq-MOqEsA3BbOxtYf-8MuQV2Gl4V5Ge6MxoJyetCHxpFtdXKzx4QrPD_8cjnkDX5l3fJxiUz7lDoz-Bi0Zomfevsopt1IuygkgL9Yaj2qxXWgKNZh4jjDWl2uhln3Yu2jmCwrR3Zm_Io3GvAW3SL8t-SaEyP-SRATU6o24c8D8ietn47RLIVRBdyWjqLyfMkT5X7mu-YnwV2B2UvA05qL-hopoFiUiSW-6K94n0MfXIpdGXfdqsZSvNw3iVq2HtG4FssG9y1y-Bn6rio3dB78ShzbTTrQSK2nM7biW-uRhJ757OBo8Sm2DFj9Ck_-mDBNoVqPMpHEfJnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Moyg1N6FyNZrllVOlvEM2c9cDFmr7tMJSFyMjw3H-4U9BBbKqSYxIj3ceLJ9Co-nyGV_O5Xir4R7KGfl6OzHxBMV4xu2cSuiofMQTitBzh_Pz7Z6X4G3aNt_Xgtgoxh2JlFBJXHsG3JW1JP4p0Exv_qRWyGtZwstFVhEN0-BE5IHRu1_Z9BYPmHZUUl_RhvogZEvllEL9RehANZDmA-z1Dau3UKvo7I1An4vowM5lPBVX1a-VLQ2zgr3LPvt9TqRZyqNJLFtoaSsMOeCYDUaJc_0WD6y-Geu14T0ij7PmNQJYKhoohNGrLY65pKstm9dMbXmzxXKdA224lra4ly4LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n5mFrEtZ0MaubSQzMfRBp9f_phTZCuh_A-LCAfG0KF5nkp96h-V9am7wB42Si4G2sqtudZbcxGkWOsmVfZimEJ1hbX_qfyTLGSctrhfzI_xNNywRU1VjyGHVBTpJek34-h0KmxsE2uA_rw2QVP4OdfCgx-JC5rsyN83Ivo1UddjUBIo0qbgK_JKBCNCBli9iSPkVQPaWCZI1uhsK3RN01l8det7kgdl1PXe3FggUBTE0-xdRVGHksnGbDwWs6jhk1Mbc5klnsxj-9STosNxABuzNb0LQW69Mo0-9fJxhweqVUTz3gITLk9_8Wnhcp4eOd_SqfokZVvi8E5CljYR9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KkluWeW2B2gd2UcInNzTSeo7BCqwWQaPrQaMss5EinbAWSEE9W1JbTCi86ke7E68tpWgO6gPvEfhLo62KkLFdeKpCEmYyQ39y55qlwAr0AynmWDa9EHIYYy18yCtmNPqzY6Irz51oz3jbFDoWO_EfTKuvkXsJQ_H8CEYYuIS9qHKLYYoRbVI0LlrVQ_JdUDJIrH2X4yC6Vige-mQ8AuN-y000R6jEHc6vcPUHCjd8qqoeUR7b5uqvySbaf7sjxbKxtAXLfbhu98zkAhRtJ9vp3Fo9ci5-CbcMg7zH2_q6olKa1CeSgLj3izdsS5sRz4jUTU0vj5nmdCuymUKhm2bBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ssQYVilInw4Oq0MQ5WnYA3k22p2d8HYJRSrReDrK9SFgriSXJYZ3S6Gr_beOoZC5fjO7UXGQJeNZEuKdynlmsIf8MH7i0A-cQC4uRWByC6Qki0M-7x-T5cBaOL4b_NA6sbtr8t7vUApNUkQuj_jUoxtEq-K-KhZM4CaAHdLmkIf4-grsGObHp79XVbCfNFNfisfCrmtfYpHH1jzgmEP3ZHK_wkEoxibCxP8MXVlBLytNwO66s1xLcbwWTaGlwGwuJ6vUf3RtsAWIIqIlrnhdSMDtT-sSPsKG0ffUKagy6kAZPAcNCxNBCeuQcxjVtLWHpmpFr9KSiypZWSJdn-bxWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من تونستم با sni ، گوشیمو به کامپیوتر وصل کنم (اصلا نمیتونستم با ویتوری وصل شم)
برای کمک کسایی که میخوان نت کامپیوترو به گوشی بدن
من از اینترنت ایرانسل استفاده کردم
برنامه ی happ به جای کلاینت v2ray توی کامپیوتر استفاده میکنم . هم توی ویندوز و هم توی گوشی بهش نیاز داریم
دقیقا مثل ویتوری ، کانفینگارو توی قسمت سرور ها اد می کنیم ، بعد از اینکه sni رو فعال می کنیم و پینگ میگیریم که ببینیم کدوم فعالن به بخش سیتینگ اپ هپ میریم
(عکس اول) اگه اسکرول کنید تا اخر میبینید یه گزینا نوشته allow connection from lan
اونو فعال می کنید
ای پی و پورت هاتونو که دقیق نوشته چیا هست
(عکس دوم) فقط باید دقت کنید توی قسمت ویدندزو فایروالتون حتما برنامه ی هم رو تعریف کرده باشید
مسیرش هم کنترل پلن ، سیستم و سکیورتی   ویندوز دیفندر فایروال و الود اپز
اول چینج سیتینگ رو می زنید بعد الو انادر اپ
و هپ رو اضافه می کنید
حتما حواستون باشه که دوتا تیکارو بزنید
(عکس سوم و چهارم) بعد اون میاید توی برنامه ی هپ گوشیتون
رو اون مثبت بالا سمت راست می زنید
منوال manual input
بعدش socks
(عکس پنجم) بعد یه صفحه براتون درست میکنه
اسم رو هرچی میخواید می زنید
اینجا نوشته server address
این سرور ادرس رو دقیقا همون ای پی ای که توی هپتون ، توی ویندوز براتون زده رو مینویسید
و port رو هم ، ببینید عددی که هپتون توی ویندوز نوشته جلوی SOCKSS proxy port چی هست . همونو می نویسید
و در اخر وصل می شید
✨</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/archivetell/5185" target="_blank">📅 21:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromㅤ</strong></div>
<div class="tg-text">هر ایرانی اندازه دو ترم راه اتصال به اینترنت رو تو این هشتاد روز پاس کردن</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/5184" target="_blank">📅 21:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHossein</strong></div>
<div class="tg-text">چقد سختش میکنید اول سیستمو متصل کنید بعدش برید تو cmd تایپ کنید ipconfig بعدش برید ipv4 رو کپی کنید  بعدش همون کانفیگی که رو لپ تاپ متصلید رو داخل v2rayng یا v2box کپی کنید گزینه ویرایش بزنید به جای 127.0.0.1 اون ipv4 رو پیست کنید تمام</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/5183" target="_blank">📅 21:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5182">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHossein</strong></div>
<div class="tg-text">چقد سختش میکنید اول سیستمو متصل کنید بعدش برید تو cmd تایپ کنید ipconfig بعدش برید ipv4 رو کپی کنید
بعدش همون کانفیگی که رو لپ تاپ متصلید رو داخل v2rayng یا v2box کپی کنید گزینه ویرایش بزنید به جای
127.0.0.1
اون ipv4 رو پیست کنید تمام</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/5182" target="_blank">📅 21:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5181">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آموزش اشتراک‌گذاری اینترنت آزاد (V2ray/SNI-Spoofing) از لپ‌تاپ به گوشی
اگ
ر روی لپ‌تاپ خود با ابزارهایی مثل SNI-Spoofer یا V2ray به اینترنت آزاد وصل هستید با این روش می‌توانید همان اینترنت بدون فیلتر را به گوشی خودتان برگردانید:
مرحله ۱: فعال کردن LAN در لپ‌تاپ
در برنامه v2rayN روی لپ‌تاپ، از پایین صفحه تیک گزینه
Allow connections from LAN
را بزنید. پورت SOCKS نوشته شده در پایین صفحه (معمولاً 10808 یا 10809) را به خاطر بسپارید.
مرحله ۲: پیدا کردن آی‌پی لپ‌تاپ
۱. در ویندوز برنامه
CMD
را باز کنید.
۲. عبارت ipconfig را تایپ کرده و اینتر بزنید.
۳. عدد روبروی
IPv4 Address
را یادداشت کنید.
مرحله ۳: باز کردن پورت در فایروال ویندوز
برای اینکه ویندوز جلوی اتصال گوشی را نگیرد:
۱. برنامه
PowerShell
را جستجو کنید، روی آن راست‌کلیک کرده و
Run as Administrator
را بزنید.
۲. دستور زیر را کپی و پیست کرده و اینتر بزنید (اگر پورت V2ray شما در مرحله اول چیز دیگری بود، عدد 10808 را در این کد تغییر دهید):
New-NetFirewallRule -DisplayName "V2Ray LAN" -Direction Inbound -LocalPort 10808 -Protocol TCP -Action Allow
مرحله ۴: اتصال در گوشی
۱. در گوشی خود برنامه
v2rayNG
را باز کنید.
۲. روی علامت
+
(بالا سمت راست) بزنید و
Type SOCKS
(یا Add a Socks profile) را انتخاب کنید.
۳. در قسمت
Address
: آی‌پی لپ‌تاپ (که در مرحله ۲ پیدا کردید) را وارد کنید.
۴. در قسمت
Port
: پورت لپ‌تاپ (مثلاً 10808) را وارد کنید.
۵. کانفیگ را ذخیره کنید و دکمه اتصال را بزنید.
@ArchiveTell
@NET_SPOOF</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/5181" target="_blank">📅 21:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5180">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3040ff2528.mp4?token=tdDtWWH-8fWj1VKb9_rxvqmxbpmRYqymv-4qHh8prPHcuXg8Rmc_V1B-_Oa7d4rVutf1A8J0--JUx1nHm8H5yJfOrtbLGHpToU0tl2-3MsPfAArnEAtJZc3DL4qp_2f5tqyBuzaq0cF2j1UFVSkqFr_S7P_ueqA2ESyGS3msikoOm0raXDxbitece1uZYDd4lrJPm5F9S7lC5MGVLJv3kevmjpeZ8DcG7vx1B9vx3vkFCg_iQpNFWzNDP727tz84rwz0M_QqaQ4AG80V4Cog4ElwM5rLiQJ72xZxzPCiOzfYcA8RxQXptXmTpEeQNDqPK5qdwo2LS_c5VkQwkcsGxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3040ff2528.mp4?token=tdDtWWH-8fWj1VKb9_rxvqmxbpmRYqymv-4qHh8prPHcuXg8Rmc_V1B-_Oa7d4rVutf1A8J0--JUx1nHm8H5yJfOrtbLGHpToU0tl2-3MsPfAArnEAtJZc3DL4qp_2f5tqyBuzaq0cF2j1UFVSkqFr_S7P_ueqA2ESyGS3msikoOm0raXDxbitece1uZYDd4lrJPm5F9S7lC5MGVLJv3kevmjpeZ8DcG7vx1B9vx3vkFCg_iQpNFWzNDP727tz84rwz0M_QqaQ4AG80V4Cog4ElwM5rLiQJ72xZxzPCiOzfYcA8RxQXptXmTpEeQNDqPK5qdwo2LS_c5VkQwkcsGxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">HashemVasel_2.0.0_x64_en-US.msi</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/5180" target="_blank">📅 20:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">HashemVasel_2.0.0_x64_en-US.msi</div>
  <div class="tg-doc-extra">86.5 MB</div>
</div>
<a href="https://t.me/archivetell/5179" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه جدید HashemVasel به‌صورت کامل بازسازی شده و حالا با رابط کاربری جدید، عملکرد پایدارتر و مدیریت اتصال دقیق‌تر ارائه می‌شود. در این نسخه قابلیت SNI Spoof اضافه شده تا اتصال‌ها بهتر و حرفه‌ای‌تر مدیریت شوند، وضعیت Core و اتصال واقعی شفاف‌تر نمایش داده می‌شود، کنترل سرویس‌ها و System Proxy بهبود پیدا کرده و بخش‌های داشبورد، تنظیمات، لاگ‌ها و صفحه درباره برنامه ساده‌تر و کاربردی‌تر شده‌اند. همچنین مشکلات نسخه‌های قبلی در اجرای سرویس‌ها، تشخیص وضعیت اتصال، بسته‌بندی برنامه و راه‌اندازی Core برطرف شده تا تجربه استفاده روان‌تر، مطمئن‌تر و قابل‌فهم‌تری داشته باشید.
- شب نسخه کامل شده رو میدم، امیدوار باشیم وصل بمونه.
لینک دانلود داخلی:
https://guardts.ir/f/058a7e797803</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/archivetell/5179" target="_blank">📅 20:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5177">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Er_MSlEgLX7JhNUVndwtSXiYSm4TZqxbrmkEYntTdEWq8N8PDrqLyQ_LGfNnDQnqjA9nRutrwkvK7x4ybxPUuhfbtZtzFVYGALLKoxRSEC_PiO34wHZagQeX0siLYzZYmu1Hvm0YxaPMRX1qNj72QuudZc3dd-92qE9-1eQUiL-mMv2v3C9Dm3C3A2o8dJh-avysXAyCGKZ8yI9rvPYeZ8_9gIOd0_MUM_K43MuHQYdd8G14j9cQnUt6uAVkXZ0nPMGLJIZ81Cu1kNYYaVsCw6sOLpMRoW6xh17p57rfJnWqMei3wG8suMw4UQeUoM-LOD0i29V0P3KRw1X2RNcBvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrDFeK3Wp3AWChU0gykYA8SEHGB12EUz2LCrR2llZe6uc86I7p7cTX_bp_67huMSxoF6pO960glpTcGuZ4GJzOyooVLv4eWMIZY733NT-6OagNHUwI1YTvG0uo_BsUNuLKaRR_lc8mSMOYtXaNsF0OhGeAIPIHlicKsiHhALR9jZ_R7w-fnhbqEcEnr8_yHJqlpyok83EfbNYSP5XMZArXH6hNERs67ZY9EUsRi70gcczE3pqfQ32mlOe15EJy6aArvvVl_JBxqooOGMj1E0R7WefBOUVolCYr1PqUmRjYG9fhao6BoNMOTQMCClL0xgq3R1pfip13VB0IboJyKdTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کیفیت کانفیگای چنل
موجودی محدود
تضمینی ، سرعت بالا و پایدار
قیمت عالی
@ArchiveTellbot
آموزش خرید</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/5177" target="_blank">📅 19:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚀
معرفی ابزار NexaTunnel: مدیریت هوشمند و مانیتورینگ کانفیگ‌ها در iOS
---
رفقا سلام!
✋
برای کسایی که توی آیفون/آیپد دنبال یک کلاینت تمیز، مدرن و حرفه‌ای برای مدیریت پروفایل‌های تونل (Tunnel) هستن، اپلیکیشن جدید
NexaTunnel
گزینه بسیار خوبیه.
این برنامه در واقع یک «داشبورد مانیتورینگ و مدیریت» هست که بهتون اجازه میده به‌راحتی کانفیگ‌های مختلف رو وارد و بین اون‌ها سوئیچ کنید.
✨
ویژگی‌های کلیدی NexaTunnel:
🔸
مدیریت حرفه‌ای کانفیگ‌ها: امکان وارد کردن (Import)، خروجی گرفتن (Export)، کپی کردن و سوییچ سریع بین چندین پروفایل.
🔸
مانیتورینگ زنده (Live Traffic): نمایش آنی سرعت آپلود/دانلود، پینگ لحظه‌ای، آی‌پی عمومی و وضعیت سلامت تونل.
🔸
تست هوشمند DNS: قابلیت تست و انتخاب بهترین ریزالور (DNS) برای شبکه فعلی شما.
🔸
امنیت و حریم خصوصی: تمام کانفیگ‌ها روی خودِ گوشی باقی می‌مونن و مقادیر حساس در لاگ‌ها ماسک می‌شن.
🔸
رابط کاربری مدرن: پشتیبانی از دارک‌مود/لایت‌مود و طراحی بسیار مینیمال و کاربرپسند.
⚠️
نکته مهم:
نکسا‌تونل خودش سرور یا سرویس VPN داخلی نداره! این برنامه فقط یک «کلاینت» هست و شما باید فایل کانفیگِ سازگار (که از قبل دارید) رو داخلش وارد کنید تا بتونید متصل بشید.
📥
لینک دانلود از اپ‌استور (مخصوص آیفون و آیپد):
🔗
https://apps.apple.com/us/app/nexatunnel/id6766783641
📌
#معرفی_ابزار
#آیفون
#آی_او_اس
#نت_ملی
#تونل
#NexaTunnel
#iOS
#VPN_Client
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/5176" target="_blank">📅 18:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سلام چن روزه نبودم
میگن نتفلای شاشبند میکنه راسته؟</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/5175" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">thefeed-android-v0.19.0-arm64-v8a.apk</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/archivetell/5174" target="_blank">📅 14:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thefeed-android-v0.19.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.9 MB</div>
</div>
<a href="https://t.me/archivetell/5173" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
نسخه جدید TheFeed (v0.19.0)
این نسخه چندتا تغییر داشته که انتظار میره سرعت برنامه بیشتر بشه
🔸
برنامه تلاش میکنه تا کوئری هایی که میفرسته سمت ریزالور ها رو جوری بسازه که شکل کوئری بقیه کاربرها که در همون لحظه دارن از برنامه استفاده میکنن بشه!، اینجوری اگر چند نفر هم زمان با یک کانفیگ‌ و ریزالور مشترک درحال گرفتن یک کانال یکسان باشن، سرعت چند برابر میشه، چون ریزالور یکبار دیتا رو از سرور میگیره و با سرعت زیاد به دست همه کاربر ها میرسونه! ،هنوز نمیدونم در عمل چقدر ممکنه این شرایط پیش بیاد که چند نفر با یک ریزالور یکسان یک کانال یکسان رو بگیرن! و البته اگر‌ بخواید میتونید این قابلیت رو از تنظیمات غیرفعال کنید
🔸
توی این نسخه جدید برنامه سعی میکنه بلاک های متادیتا رو بصورت هم زمان بگیره تا عملیات گرفتن پست های کانال ها سریع تر شروع بشه (اون مکس اولیه که قبل از شروع گرفتن پیام های کانال ها میبینید سریع تر میشه)
🔸
ظاهر تنظیمات بهتر شده و تنظیمات دسته بندی شده (یک سری از تنظیماتی که قبلا توی کانفیگ بود هم به این بخش منتقل شده، مثل تعداد هم زمانی کوئری ها و ...)
🔸
قابلیت فول اسکرین کردن ویدیو ها
🔸
نشون دادن هش فایل ها توی گیتلب
🦠
رفع باگ دکمه ریست امتیاز ریزالور ها
🦠
رفع مشکل تغییر سایز فونت در iOS ( نسخه جدید واسه iOS هنوز رلیز نشده و فعلا نمیتونید آپدیت کنید!)
📯
من نسخه اندروید arm8a رو توی این کانال میزارم و اگر نسخه های دیگه رو میخواید باید از گیتلب و یا کانال زیر دانلود کنید (ویندوز، مک، لینوکس، بی‌اس‌دی، اندروید arm7a و حتی ترموکس):
📦
@thefeedfile
🔗
https://gitlab.com/sartoopjj/thefeed
🔐
SHA256:
d2b10e3d16d3d07662c7010aa28495a2936e3a281b92c459b6d93efcaf95fb59
📢
کانال اصلی دفید:
@networkti
📦
کانال فایل های باینری/نصبی دفید:
@thefeedfile
⚙
کانال کانفیگ هایی دفید:
@thefeedconfig</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/5173" target="_blank">📅 14:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚀
ورژن آخر اپلیکیشن محبوب v2rayNG (نسخه 2.1.7)
---
یکی از بهترین و پرکاربردترین کلاینت‌های اندروید برای دور زدن فیلترینگ، یعنی v2rayNG، یه آپدیت جدید و پر از امکانات خفن داده بیرون که پیشنهاد می‌کنم حتماً نصبش کنید.
⚡️
مهم‌ترین تغییرات نسخه جدید (v2.1.7):
🔸
قابلیت Chain Proxy (پروکسی زنجیره‌ای): بالاخره این قابلیت جذاب اضافه شد تا بتونید ترافیک رو از چند سرور مختلف عبور بدید.
🔸
سیستم روتینگ پیشرفته برای پروسه‌ها: حالا می‌تونید (تو اندروید ۱۰ به بالا و با روشن بودن TUN) مشخص کنید که دقیقاً کدوم اپلیکیشن‌ها (از طریق نام پکیجشون) از VPN رد بشن یا نشن!
🔸
رمزگذاری روی SOCKS: اضافه شدن پشتیبانی از یوزرنیم و پسورد برای لوکال ساکس.
🔸
میانبرهای سریع (Shortcuts): اضافه شدن شورت‌کات به آیکون برنامه برای روشن/خاموش کردن سریعِ اتصال.
🔸
تنظیمات جدید برای IPv6 و SOCKS5 (مثل بستن UDP).
🔸
و البته آپدیت هسته Xray به آخرین نسخه (v26.5.9).
📥
دانلود مستقیم (از گیت‌هاب سازنده):
با توجه به نوع پردازنده گوشیتون یکی از فایل‌های زیر رو دانلود کنید (برای اکثر گوشی‌های جدید، نسخه اول یعنی
arm64-v8a
مناسبه):
📱
نسخه arm64-v8a (مخصوص اکثر گوشی‌های جدید):
🔗
https://github.com/2dust/v2rayNG/releases/download/2.1.7/v2rayNG_2.1.7_arm64-v8a.apk
📱
نسخه armeabi-v7a (مخصوص گوشی‌های قدیمی‌تر):
🔗
https://github.com/2dust/v2rayNG/releases/download/2.1.7/v2rayNG_2.1.7_armeabi-v7a.apk
📱
نسخه Universal (اگر نمی‌دونید پردازنده گوشیتون چیه، این نسخه روی همه نصب می‌شه - حجمش کمی بیشتره):
🔗
https://github.com/2dust/v2rayNG/releases/download/2.1.7/v2rayNG_2.1.7_universal.apk
📌
#آپدیت
#معرفی_ابزار
#اندروید
#فیلترشکن
#نت_ملی
#v2rayNG
#Xray
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/5172" target="_blank">📅 14:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اشتراک گذاری متد اسپوف از سیستم رو گوشی
تو سیستم ipv4 رو پیدا کن بزا جای آدرس کانفگیت بعدش کلیک راست کن روی کانفیگی که توی سیستم وصلی گزینه share بزن یه بارکد بهت میده با گوشی v2box یا بقیه کلاینت ها وصل شو</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/archivetell/5171" target="_blank">📅 14:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">لینک داخلی V2rayn ویندوز
دانلود</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/archivetell/5170" target="_blank">📅 13:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">برای مک از ازین ریپو هم میتونید استفاده کنید
https://github.com/selfishblackberry177/sni-spoof/releases/
1. فایل دانلودی رو با config.json داخل یه دایرکتوری بگذارید
2. داخل ترمینال cd بزنید و دایرکتوری رو بیارید
3. sudo ./sni-spoof-darwin-arm64 config.json</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/archivetell/5169" target="_blank">📅 13:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/archivetell/5168" target="_blank">📅 13:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5167">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/archivetell/5167" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5166">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تعدادی کانفیگ واسه متد sni
trojan://1710442808@127.0.0.1:40443?allowInsecure=1&host=subb.nrshop198.workers.dev&path=%2F&sni=subb.nrshop198.workers.dev&type=ws#1
trojan://humanity@127.0.0.1:40443?alpn=h2%2Chttp%2F1.1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#2
trojan://humanity@0.0.0.0:40443?allowInsecure=1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#3
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.multiplydose.com&path=%2Fassignment&sni=www.multiplydose.com&type=ws#4
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.ignitelimit.com&path=%2Fassignment&sni=www.ignitelimit.com&type=ws#5
trojan://humanity@127.0.0.1:40443?allowInsecure=1&path=%2Fassignment&sni=www.multiplydose.com&type=ws#6
trojan://humanity@127.0.0.1:40443?allowInsecure=1&host=www.creationlong.org&path=%2Fassignment&sni=www.creationlong.org&type=ws#7</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/archivetell/5166" target="_blank">📅 08:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5165">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">https://seup.shop/f/nn3o5
از حالت فشرده خارج میکنید میرید توی فولدرش
بعد sni-spoof-rs.exe رو راست کلیک میکنید و administrator باز میکنید
بعد میرید داخل ویتوری به این کانفیگ وصل میشید و تمام
trojan://humanity@127.0.0.1:40443?security=tls&sni=www.creationlong.org&insecure=1&allowInsecure=1&type=ws&host=www.creationlong.org&path=%2Fassignment#Technologia%20%3A%20Poland
توی تلگرام با این پروکسی وصل شید
tg://socks?server=127.0.0.1&port=10808
با فایر فاکس هم میتونید برید پروکسی تنظیم کنید و استفاده کنید راحت
برای کروم باید foxyproxy داشته باشید یا مشابه این اکستنشن
1-اگه براتون وصل نشد نت گوشی رو شیر کنید و امتحان کنید
2-فایل config.json رو میتونید باز کنید وبجای ایپی
104.19.229.21
و ادرس
hcaptcha.com
چیز دیگری امتحان کنید
3- بجای کانفیگ هم میتونید کانفیگ دیگه پیدا کنید که اهدا شده</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/archivetell/5165" target="_blank">📅 08:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خب hcaptcha رو مستقیم کردند، اگه: https://www.hcaptcha.com/cdn-cgi/trace  ایپی خودتونو داد یعنی رو نت شمام مستقیم کردن. {   "LISTEN_HOST": "0.0.0.0",   "LISTEN_PORT": 40443,   "CONNECT_IP": "104.19.229.21",    "CONNECT_PORT": 443,   "FAKE_SNI": "www.hcaptcha.com"…</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/archivetell/5164" target="_blank">📅 02:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این لینکو بدون وی پی ان باز کنید اگه باز میشه اسپوف هم وصل میشه
https://www.hcaptcha.com/cdn-cgi/trace</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/archivetell/5163" target="_blank">📅 02:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SNI-Spoofing.zip</div>
  <div class="tg-doc-extra">131.4 KB</div>
</div>
<a href="https://t.me/archivetell/5162" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">spoof
mac os</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/archivetell/5162" target="_blank">📅 02:36 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚀
آموزش جامع و قدم‌به‌قدم اسکریپت XHTTP-Installer (تونل نتلیفای و ورسل)
🤯
---  با محدودیت‌های شدید اخیر، اتصال مستقیم به سرورهای خارج خیلی سریع باعث فیلتر شدن آی‌پی می‌شه. اما با اسکریپت فوق‌العاده‌ و ایرانیِ XHTTP-Installer، ترافیک سرور شما پشت سرویس‌های…</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/archivetell/5161" target="_blank">📅 01:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚀
معرفی NovaProxy: عبور از فیلترینگ با ترکیب Google و Cloudflare
🤯
---
یه پروژه دسکتاپیِ به‌شدت خفن و مهندسی‌شده به اسم NovaProxy اومده که با استفاده از تکنیک Domain Fronting، ترافیک اینترنت شما رو دور از چشم فیلترینگ جابه‌جا می‌کنه.
🔥
این ابزار دقیقاً چیکار می‌کنه؟
وقتی NovaProxy رو روشن می‌کنید، سیستم فیلترینگ فقط می‌بینه که شما در حال تبادل دیتا با
www.google.com
هستید! اما در واقع، ترافیک شما از طریق سرورهای گوگل به یه اسکریپت (Apps Script) فرستاده می‌شه، از اونجا می‌ره تو کلادفلر ورکر (Worker)، و بعدش سایتِ فیلترشده‌ای که می‌خواید رو براتون باز می‌کنه.
این روش برای وب‌گردی عالیه و سایت‌هایی مثل تلگرام وب یا یوتیوب رو خیلی روون باز می‌کنه (البته تلگرامِ خود ویندوز فعلاً با این روش کار نمی‌کنه و این ابزار مخصوص مرورگرهاست).
🛠
آموزش راه‌اندازی (مرحله‌به‌مرحله):
1️⃣
مرحله اول: ساخت Cloudflare Worker
۱. برید تو سایت کلادفلر و بخش Workers & Pages. یه ورکر جدید (Hello World) بسازید.
۲. کد فایل
worker.js
(موجود در پوشه server گیت‌هاب) رو تو ورکری که ساختید پیست کنید.
۳. در کدها، خطی که نوشته
WORKER_URL
رو پیدا کنید و آدرس ورکری که خودتون ساختید رو به جاش بذارید و Deploy کنید.
2️⃣
مرحله دوم: ساخت Google Apps Script
۱. برید تو سایت
script.google.com
و روی New project کلیک کنید.
۲. کد فایل
Code.gs
رو اونجا پیست کنید.
۳. دو متغیر
AUTH_KEY
(یه رمز دلخواه قوی براش بذارید) و
WORKER_URL
(آدرس همون ورکر کلادفلری که تو مرحله قبل ساختید) رو تو کد جایگزین کنید.
۴. از بالا Deploy ➔ New deployment رو بزنید. نوعش رو روی Web app و دسترسی رو روی Anyone بذارید و دیپلوی کنید تا یه Deployment ID (شبیه AKfy...) بهتون بده.
3️⃣
مرحله سوم: راه‌اندازی نرم‌افزار NovaProxy
۱. برنامه
novaproxy.exe
رو دانلود و نصب کنید. تو همون مرحله اول یه پاپ‌آپ میاد که باید گواهی (Certificate) رو تایید و نصب کنید.
۲. تو تنظیمات، کشور رو روی Iran بذارید.
۳. برید تو بخش پروکسی و اون ۳ تا مقداری که ساختید (Auth Key، Script ID و Worker URL) رو وارد و ذخیره کنید.
۴. تو صفحه داشبورد، اول پروکسی و پروکسی سیستم رو روشن کنید، بعد کلید GSA رو فعال کنید تا وب‌گردی آزاد براتون استارت بخوره!
📥
دانلود برنامه و کدهای مورد نیاز:
کدهای مراحل اول و دوم، و همچنین فایل نصبی خود برنامه رو می‌تونید مستقیماً از صفحه رسمی گیت‌هابِ پروژه بردارید:
🔗
https://github.com/IRNova/Nova-Proxy-App
📌
#معرفی_ابزار
#نوا_پروکسی
#گوگل
#کلادفلر
#دامین_فرانتینگ
#نت_ملی
#NovaProxy
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/archivetell/5160" target="_blank">📅 00:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">config.json</div>
  <div class="tg-doc-extra">150 B</div>
</div>
<a href="https://t.me/archivetell/5159" class="tg-doc-link" target="_blank">دانلود</a>
</div>
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
www.hcaptcha.com
"
}</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/archivetell/5159" target="_blank">📅 00:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SNI-Spoofing_by_patterniha_v1.zip</div>
  <div class="tg-doc-extra">9.8 MB</div>
</div>
<a href="https://t.me/archivetell/5158" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل برنامه رو ران از ادمین کنید و در v2ray وصل بشید به این
trojan://humanity@127.0.0.1:40443?security=tls&sni=www.creationlong.org&fp=chrome&insecure=1&allowInsecure=1&type=ws&host=www.creationlong.org&path=%2Fassignment#ArchiveTel</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/archivetell/5158" target="_blank">📅 00:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5157">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompatterniha</strong></div>
<div class="tg-text">خب hcaptcha رو مستقیم کردند، اگه:
https://www.hcaptcha.com/cdn-cgi/trace
ایپی خودتونو داد یعنی رو نت شمام مستقیم کردن.
{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
104.19.229.21
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
www.hcaptcha.com
"
}
///
104.19.229.21
,
104.19.230.21
///
ولی sni-spoofing رو یه سری از نت ها کامل وصله، یکسری کنده و یکسری قطعه احتمالا بلایی سرش آوردن یا صرفا ip رو کند کردن. در حال بررسی هستم ...
///
خود سایتشم بسیار کند بالا میاد فعلا حالت عادیشم بسیار کند هستش.</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/archivetell/5157" target="_blank">📅 00:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5156">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5718e643c7.mp4?token=EMFxerORbgi6dLovThYf7WtvnEIzg68-mbP2dAftyQsSUD4oagDdCAQ9T3aMxY05-UImvKIR-ModD4hGD6QsKCKBC-INv8TTqZ_RZHhzs-s6remhswRRyojwHGk88fjyi745BDJCHoqxsZlQYJOyl90R4RuWPbDvPW61aNGcHhy5cgKlE0mE4KwUeyovozHhRNgy1eNaOfbxhUUf6phFVxzgwJMcJRAcWCloEdp9OiSSe---0xBWXm6JmpyZQd0Zp2StdLlD-xddtVclXckrRZhdw6TexYQ09aDm9H3y2HSJU7L6QgRjdqUWkMGFxkLZEga9dyZUFNVVNWtQ-UoAAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5718e643c7.mp4?token=EMFxerORbgi6dLovThYf7WtvnEIzg68-mbP2dAftyQsSUD4oagDdCAQ9T3aMxY05-UImvKIR-ModD4hGD6QsKCKBC-INv8TTqZ_RZHhzs-s6remhswRRyojwHGk88fjyi745BDJCHoqxsZlQYJOyl90R4RuWPbDvPW61aNGcHhy5cgKlE0mE4KwUeyovozHhRNgy1eNaOfbxhUUf6phFVxzgwJMcJRAcWCloEdp9OiSSe---0xBWXm6JmpyZQd0Zp2StdLlD-xddtVclXckrRZhdw6TexYQ09aDm9H3y2HSJU7L6QgRjdqUWkMGFxkLZEga9dyZUFNVVNWtQ-UoAAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
آموزش جامع و قدم‌به‌قدم اسکریپت XHTTP-Installer (تونل نتلیفای و ورسل)
🤯
---
با محدودیت‌های شدید اخیر، اتصال مستقیم به سرورهای خارج خیلی سریع باعث فیلتر شدن آی‌پی می‌شه. اما با اسکریپت فوق‌العاده‌ و ایرانیِ XHTTP-Installer، ترافیک سرور شما پشت سرویس‌های قدرتمندی مثل Netlify یا Vercel مخفی می‌شه!
🔥
با بررسی دقیق آموزش‌های ویدیویی این پروژه، راهنمای صفر تا صد اون رو براتون آماده کردیم:
🛠
مرحله ۱: تنظیمات دامنه (Cloudflare)
۱. وارد اکانت کلادفلر بشید و به بخش DNS برید.
۲. یه رکورد جدید از نوع A بسازید. در بخش Name یه اسم دلخواه (مثلاً test) بدید و در بخش IPv4، آی‌پی سرور مجازیتون رو وارد کنید.
۳.
⚠️
به‌شدت مهم: تیک پروکسی (ابر نارنجی) رو حتماً خاموش کنید تا خاکستری (DNS Only) بشه و Save رو بزنید. (یکی دو دقیقه صبر کنید تا ست بشه).
💻
مرحله ۲: اجرای اسکریپت در سرور
۱. به سرور لینوکسی خودتون SSH بزنید.
۲. کد زیر رو کپی و اجرا کنید:
bash <(curl -fsSL https://raw.githubusercontent.com/avacocloud/XHTTP-Installer/main/install.sh)
۳. اسکریپت می‌پرسه رو حالت screen اجرا بشه؟ (کلید n رو بزنید).
۴. حالا می‌پرسه رو کدوم پلتفرم می‌خواید دیپلوی کنید؟ عدد 1 (ورسل) یا 2 (نتلیفای) رو انتخاب کنید.
⚙️
مرحله ۳: پاسخ به سوالات اسکریپت
اسکریپت چندتا سوال می‌پرسه که باید این‌طوری جواب بدید:
🔸
دامین: همون ساب‌دامنه‌ای که تو کلادفلر ساختید رو کامل وارد کنید (مثلاً
test.yoursite.com
).
🔸
ایمیل: یه ایمیل معتبر وارد کنید.
🔸
پورت و مسیر (Path): دست نزنید و فقط Enter بزنید تا همون پیش‌فرض بمونه.
🔸
توکن (Token): توکنی که از پنل Vercel یا Netlify گرفتید رو اینجا Paste کنید.
🔸
اسم پروژه: Enter بزنید تا خودش رندوم بسازه. (برای ورسل ممکنه تنظیمات پرفورمنس هم بیاد که باز همون Enter رو بزنید).
در نهایت y بزنید و صبر کنید تا عملیات ساخت و تست کانفیگ تموم بشه و لینک vless رو بهتون بده.
📱
مرحله ۴: اتصال در کلاینت (ترفندهای طلایی)
🟢
برای کاربران ورسل (Vercel):
لینک رو تو کلاینت (مثل v2rayNG) وارد کنید. برای اینکه پینگ بده، فیلد Address (یا همون آی‌پی) رو پاک کنید و یکی از این دو آی‌پی وایت‌لیست و بدون فیلتر رو جاش بذارید:
198.169.2.1
198.169.2.65
🔵
برای کاربران نتلیفای (Netlify):
اگر کانفیگ خام پینگ نداد، برید تو ربات تلگرامی
@verceltoken_bot
، از بخش Config Builder گزینه Netlify و سپس Mix mode رو انتخاب کنید. کانفیگتون رو بهش بدید تا یه فایل متنی حاوی ده‌ها ترکیب SNI و IP بهتون بده. همه‌رو تو کلاینت تست پینگ بگیرید و هرکدوم وصل شد از همون استفاده کنید!
📥
ویدیوها و سورس کد اصلی:
▶️
ویدیو آموزش نتلیفای:
https://youtu.be/B-As6aZSiMA
▶️
ویدیو آموزش ورسل:
https://youtu.be/yz2gLxTeWGE
💻
سورس کد در گیت‌هاب:
https://github.com/avacocloud/XHTTP-Installer
(طراحی اسکریپت توسط
@avaco_cloud
و آموزش ویدیویی از AmirS
🤍
)
📌
#آموزش
#اسکریپت
#نتلیفای
#ورسل
#نت_ملی
#XHTTP
#Vercel
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/archivetell/5156" target="_blank">📅 00:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-text">vless://557ad0d8-5a72-48e4-9408-10c04f1c7347@198.169.2.1:443?encryption=none&security=tls&sni=relay-arb3pb5l.vercel.app&fp=chrome&alpn=h2%2Chttp%2F1.1&insecure=0&allowInsecure=0&type=xhttp&host=relay-arb3pb5l.vercel.app&path=%2Fapi&mode=auto&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D#%40IR_NETLIFY-XHTTP-vercel
vless://557ad0d8-5a72-48e4-9408-10c04f1c7347@198.169.2.65:443?encryption=none&security=tls&sni=relay-arb3pb5l.vercel.app&fp=chrome&alpn=h2%2Chttp%2F1.1&insecure=0&allowInsecure=0&type=xhttp&host=relay-arb3pb5l.vercel.app&path=%2Fapi&mode=auto&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D#%40IR_NETLIFY-XHTTP-vercel</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/5155" target="_blank">📅 00:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">😂
ورسل وصل شد</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/archivetell/5153" target="_blank">📅 00:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ربات Music Tool بهترین ربات برای مدیریت آسان فایل‌های موسیقی شماست!
🎵
✨
@MusicToolBot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/archivetell/5152" target="_blank">📅 23:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚀
آپدیت جدید جعبه‌ابزار Network Checker منتشر شد (نسخه v0.6.0)
---
اپلیکیشن همه‌کاره و فوق‌العاده‌ی Network Checker که قبلاً تو کانال معرفیش کرده بودیم، یه آپدیت داغ و به‌شدت کاربردی داده بیرون.
⚡️
تغییرات مهم این نسخه (v0.6.0):
🔸
اضافه شدن اسکنر اختصاصی آکامای: دیگه نیازی به اسکریپت یا برنامه‌های جانبی نیست؛ اسکنر آی‌پی آکامای (Akamai IP Scanner) مستقیماً به خود برنامه اضافه شده!
🔸
کانفیگ‌ساز Netlify: یه قابلیت جدید و خفن (Netlify Config Generator) برای ساخت کانفیگ به برنامه اضافه شده.
🔸
بهبود اسکنر دامنه (Domain Scanner): لیست دامنه‌های پیش‌فرض برای اسکن، آپدیت و بهینه‌سازی شدن تا خروجی‌های کاربردی‌تری بهتون بدن.
📥
لینک‌های دانلود مستقیم برای اندروید (نسخه 0.6.0):
📱
نسخه arm64-v8a (مخصوص اکثر گوشی‌های جدید - پیشنهاد اول):
🔗
https://github.com/mirarr-app/network-checker/releases/download/0.6.0/app-arm64-v8a-release.apk
📱
نسخه armeabi-v7a (مخصوص گوشی‌های قدیمی‌تر):
🔗
https://github.com/mirarr-app/network-checker/releases/download/0.6.0/app-armeabi-v7a-release.apk
📱
نسخه Universal (اگر نمی‌دونید پردازنده گوشیتون چیه، این نسخه روی همه نصب می‌شه):
🔗
https://github.com/mirarr-app/network-checker/releases/download/0.6.0/app-release.apk
(برای دانلود نسخه‌های آپدیت‌شده‌ی ویندوز و لینوکس می‌تونید به صفحه گیت‌هاب پروژه مراجعه کنید).
📌
#آپدیت
#معرفی_ابزار
#اسکنر
#نتورک_چکر
#آکامای
#نت_ملی
#Network_Checker
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/archivetell/5151" target="_blank">📅 22:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ArchiveTel
pinned «
ربات چنل راه اندازی شد
🔥
تضمینی ، سرعت بالا و پایدار  قیمت عالی  @ArchiveTellbot  آموزش ساده خرید تو پست بعدی..
»</div>
<div class="tg-footer"><a href="https://t.me/archivetell/5150" target="_blank">📅 19:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g69oKvrrcvryvACiJw9Cz5r4cmpkFNbe0EScV5LnX7Ij2JIG3v_QHgaR4XKB_4mJw7a8g0PAAdKxs9ZKOANxLr3a9gDtZ0ULKBiFy7c-9pb8TXlPKgxIW4_EoEYMY_vPpVYOe3-avNML0t2s9DuMszVYIG0sXhXV_bEuSQaKG0UzyThIDv8FdtQMvoPmfamWiFSroVT19PUkhlhKg2_3eS94OPNBuQMIoSAr5z9JRt1qo-TZq8aFG8Pl1d7YisXVJV95eNZF_iydfRnbgtVk1Cwxizg2NBZ863GYqruEQ_PCp2FYFTokvrVll-4Z6E3KWaXs0Ebibwo2udTMjbzJpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ulbLWRiRwdA1O9PwQv4lYRbv2mOfB7vFVLe6zkfvl-IvFzAg4JmlkaTiqc-0y6JOE6btXfPcHuxts5MrpxaEmI_yRIbpnkSN9kxsqVNNYTSadF1phzP6hWvdL6D1AR8X22_4gExdHAUCp7IW2wktgXp9TgA-7KQ0BtZxJlAIGde2qIQbKH14Bfzh-zI-AExS4Ol2KstMOfFpvl5Afxh_EYZStqbgBtoMvCWRkGkZAW33o8MeV1o4xYpQvbBZmJCNGdDVJbIbrwOst5t4AToIx4UQRM277jJWHiFriprIfet8CNzGSvXOm3EYwFtNfPGfkOG2d6C5vl3oSFk5LoTxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nLI3UySpjpWevlaNTB4K1WKQpZBARjDn-0yj_o2U9Esbn4-UIYX5eM1umor8JPI_D8vbBYvuF2syWy56EPU8eUAgs3wAWMBcLR1jzx7duK9T6mGMYCV7U4p_F133Epg7GqZuhnTKRdgoGATs4OkE1KPrfGy_piZEiBI90KRsIZDK0SpjFtT5InM_wTHQtynmbud9JBy7tFTU0yp-TtdC8RNyAkpDTwJ9ala_707BS2cpSHUYqsV8lfmNi3kSgEgoc9zz8YqiTGK2l-vTsm8G-u8Yf6nkpHZiTykXmv_q0Rsuuge03uuSzRqTlY4554Yv19R7h4HHpoUptJZH1Vy_jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KmeNOwTnsPH_rpjYSt1n68uMLbw60ekG5OsU_DarWKg0o0Ov04VHj9pbwXq2JO0ljx5yBEFJwKq-w7WlQvJWAirH9WwTVRjODrwomxCQu7Atq3vFlkMGHpjomrKYx8hIZYvp9wYrTRfONdW_Bo7oTWjwUi0RCRVDOUNyX2g04nQod3blG3QXFuqyj0dfdmemJ_cmMQ5t8j-Ktg1YVw2339BrAe2YZNO7qmxiwrrLTMhIRtDayRX7Q18wdF3CZG0w2rnHGXIZm4ZR5A2SIulUBHfzFG_MMIJyI1oKvhG1oIkTHXVJPDN0FRPDkuBeIFhK9T4KzYQYk2yqE7B5SahxXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S0vk7zB8HutQFgahms0ruHNAdb9h9H3fx38REgkEkyE7jovXRIbvj7qfrW0eeMfHAwMX2jKx8uuSG1zOPkxyrRJU6RvA1RASWq1VDBz0JmeM00XUJpYDXZd82DqJPNGRT9v1HExpN_jRKZe6DJ7qpUtWm3ep8FfucbN_Jk2ZJLsQFuV6Qu8uBfMnUXOXGxm93qKvmIb6LiPSe0-kWGox9xcl9o9jQlj5_L_FqHPoUgKgGt6fYJEG_2V9oi3adEyDpiZ8inDoCm9BG7A3Fh1aBPxSqrA7rXQpBWLKpgMcosq5l82NVtXg33soHJF-KBKSyKKkzDEtaZsO59QgGFVsvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-let2CXTTk9P2OJpin_dm8jVHAySDCSHz-KNqyQCOR1SZ-zAcefvCZ8grlk4Rq4zxHFeZALjF_Rchi0vYZ0IHojoGJT7z5xdbs8dYOCwSBoTfrjUOOUjuTX7jjksymMk51d7XluRPT8qt4lQmDwhT1PXwO8oBrzoS1ZTfHTfuH3eATrb15BgyYuHTjiFS8POMIqBgIG0Fon1ScQkLsRC621y9u6jAEXsrVWiwMdsv62Jp9E7DQL8LmFtzXcEINXNAT2RSFybgGPrgq3Jguult1xY4vw_3OV-bUnh5BPojgI4iVnBaHN738bUn_6Aolt2317afBHZhQJnrIamdu2QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/buRElvPwwun0l5S2hqQ3F9_5-oDBTUIAUmgRhU15WQzY2NeUUD39F_W3yIfGfSN2BfvNKcZ3_aQUdTC7EC8e1JEFEZoDWJ6LEmpEvMpH7aP-WJE_qgaq-H1_BDm8IttKnSKqhcWysjz-BDVeNj9L2ySwuLCWfhqbD1eP2DeOkGBOIx6cS3U-IVTmH-ANfnZGOPVX_R4JHJPjz5euMgMjcQovpcgeNPvrw493yHxv6BrGVcRgW9kIblQriJnQ3ADsn1Dv7iJBy2fzcAfN7z0ccYbsjqJhqOf6R6BxQoyaOXa0FZUPCVgYH2MdwnW43wJtbq0DPmXXB9Zy1BMjTgSI1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
آموزش تصویری خرید اشتراک ArchiveTell با سواپ‌ولت
1️⃣
-
ثبت‌نام و شارژ (زیر ۲ دقیقه):
وارد (
@SwapWalletBot
) شوید، به بخش
Wallet
بروید و با شماره موبایل و کدملی احراز هویت کنید. سپس حساب ریالی را شارژ کرده و ارز
🪙
تون (TON)
یا
🪙
ترون (TRX) بخرید
(توصیه ما TON است چون انتقالش کارمزد ندارد).
2️⃣
-
ثبت سفارش:
در ربات ما روی «
🔐
خرید اشتراک» بزنید و حجم دلخواهتان را انتخاب کنید.
3️⃣
-
پرداخت فاکتور (یکی از دو روش زیر):
🪙
روش TON  (بدون کارمزد):
مبلغ را از سواپ‌ولت به آدرس زیر انتقال دهید و حتماً رسید را به
☎️
پشتیبانی
بفرستید تا سرویس فعال شود:
👇
(برای کپی کلیک کنید)
UQBS9c1YqBaOI1oTcXo0n_khM6XxaJDInwHpr0u63JhgBrh-
🪙
روش TRX (تایید خودکار):
مبلغ دقیق ترون را به آدرسی که داخل فاکتور ربات نوشته شده واریز کنید تا سرویس کاملاً خودکار و بدون نیاز به رسید فعال شود.
✔️
در آخر، وارد بخش «
🛍
سرویس‌های من
» شوید و لینک اتصال خود را به راحتی دریافت کنید!
@ArchiveTellbot</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/archivetell/5143" target="_blank">📅 19:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ربات چنل راه اندازی شد
🔥
تضمینی ، سرعت بالا و پایدار
قیمت عالی
@ArchiveTellbot
آموزش ساده خرید تو پست بعدی..</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/archivetell/5142" target="_blank">📅 19:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚀
معرفی اپلیکیشن TheFeed برای کاربران iOS (آیفون/آیپد)
---
رفقای آیفون‌دار
می‌دونیم که پیدا کردن ابزارهای دور زدن فیلترینگ برای iOS همیشه سخت‌تر از اندرویده. امروز یه کلاینت جدید و جذاب به اسم TheFeed رو بهتون معرفی می‌کنیم که فعلاً تو مرحله تست (بتا) قرار داره و می‌تونید از طریق TestFlight اپل روی گوشیتون نصبش کنید.
🛠
آموزش نصب و راه‌اندازی (فقط در ۳ قدم):
1️⃣
قدم اول (نصب پیش‌نیاز): ابتدا باید برنامه رسمی TestFlight رو از App Store سرچ و روی گوشیتون نصب کنید (این برنامه مال خود اپله و برای نصب نسخه‌های آزمایشیِ برنامه‌ها استفاده می‌شه).
2️⃣
قدم دوم (نصب اپلیکیشن): روی لینک دعوتِ زیر کلیک کنید تا صفحه TheFeed تو برنامه تست‌فلایت براتون باز بشه. بعد روی دکمه Accept و سپس Install بزنید تا برنامه نصب بشه.
3️⃣
قدم سوم (دریافت کانفیگ): بعد از نصب، برنامه خالیه و برای اتصال نیاز به کانفیگ دارید. سازنده‌های این پروژه یه کانال تلگرامی مجزا زدن که کانفیگ‌های مخصوص TheFeed رو اونجا قرار می‌دن. کافیه کانفیگ‌ها رو از اونجا کپی و تو برنامه وارد کنید.
📥
لینک‌های مورد نیاز:
🔗
لینک دعوت و نصب TheFeed (از طریق TestFlight):
🌐
https://testflight.apple.com/join/J6bfxDdZ
⚙️
کانال دریافت کانفیگ‌های مخصوص برنامه:
🆔
@thefeedconfig
📢
کانال اصلی پروژه (برای پیگیری اخبار و آپدیت‌ها):
🆔
@networkti
📌
#معرفی_ابزار
#آیفون
#آی_او_اس
#نت_ملی
#فیلترشکن
#TheFeed
#iOS
#TestFlight
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/archivetell/5141" target="_blank">📅 14:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آپلودر بدون نیاز به ثبت نام
https://guardts.ir/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/5140" target="_blank">📅 13:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/archivetell/5139" target="_blank">📅 12:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCheshm E Oghab - چشم عقاب</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CheshmehOghab-Android.apk</div>
  <div class="tg-doc-extra">26.1 MB</div>
</div>
<a href="https://t.me/archivetell/5138" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دانلود مستقیم اپلیکیشن چشم عقاب
یا از طریق:
-
گوگل درایو
-
گیت‌هاب
-
گوگل پلی
میتونید این آدرس‌هارو با دوستان خود به اشتراک بگذارید از اونجایی که برخی از سرویس‌ها رو بعضی از آی‌اس‌پی ها باز هستند.
@CheshmehOghabApp</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/5138" target="_blank">📅 12:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚀
معرفی اپلیکیشن «چشم عقاب» (Eagle Eye): دریافت اخبار و کانفیگ VPN، کاملاً آفلاین و از طریق ماهواره!
📡
---  امروز با یه شاهکارِ تکنولوژی و انقلابی اومدیم که دقیقاً برای روزهای قطعیِ مطلق اینترنت (نت ملی) طراحی شده.   وقتی اینترنت کاملاً قطع می‌شه، اپلیکیشن…</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/5137" target="_blank">📅 12:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚀
معرفی اپلیکیشن «چشم عقاب» (Eagle Eye): دریافت اخبار و کانفیگ VPN، کاملاً آفلاین و از طریق ماهواره!
📡
---
امروز با یه شاهکارِ تکنولوژی و انقلابی اومدیم که دقیقاً برای روزهای قطعیِ مطلق اینترنت (نت ملی) طراحی شده.
وقتی اینترنت کاملاً قطع می‌شه، اپلیکیشن «چشم عقاب» بهتون اجازه می‌ده اخبار، توییت‌ها، پیام‌های تلگرامی و مهم‌تر از همه،
کانفیگ‌های تازه و سالمِ VPN
رو مستقیماً از طریق دیش ماهواره و بدون نیاز به سیم‌کارت یا حتی یک بایت اینترنت، روی گوشیتون دریافت کنید!
🤯
🔥
مکانیزم کار چطوره؟
خیلی ساده‌ست! شبکه مورد نظر به جای پخش فیلم، یک‌سری QR Code رو تند و پشت‌سرهم روی صفحه تلویزیون پخش می‌کنه. شما دوربین گوشی رو می‌گیرید سمت تلویزیون و تو کمتر از ۲۵ ثانیه، تمام اطلاعات به صورت آفلاین وارد گوشی شما می‌شه!
✨
ویژگی‌های بی‌نظیر این اپلیکیشن:
🔸
۱۰۰٪ آفلاین و امن: این برنامه اصلاً مجوز (Permission) دسترسی به اینترنت نداره و فقط به دوربین دسترسی داره. محاله بتونه دیتایی ارسال یا دریافت کنه.
🔸
کانفیگ‌های داغِ VPN: دریافت سرورهای V2Ray، Shadowsocks و WireGuard از ماهواره؛ تا به محض اینکه نت وصل شد، سریعاً فیلترینگ رو دور بزنید.
🔸
رمزنگاری و امضای دیجیتال: تمام محتواها با الگوریتم (Ed25519) تایید می‌شن تا کسی نتونه دیتای فیک یا مخرب به خوردتون بده. اطلاعات هم روی گوشی با AES-256 رمزنگاری می‌شن.
🔸
ضد اسکرین‌شات: برای امنیت بیشتر شما، امکان اسکرین‌شات و ضبط صفحه بسته شده.
🔸
دریافت با وجود خطا: حتی اگه ۳۰ درصد از QR کدها رو به خاطر پرش تصویر از دست بدید، باز هم اطلاعات به صورت کامل بازسازی می‌شن!
📡
مشخصات شبکه در ماهواره:
ماهواره: ترکمن‌عالم / یاهست (TurkmenÄlem 52°E)
فرکانس: 10762
پلاریزاسیون: عمودی (V)
سیمبول ریت: 27500
📥
لینک‌های دانلود برنامه:
📱
دانلود مستقیم از گوگل‌پلی:
🔗
https://play.google.com/store/apps/details?id=com.filtershekanha.cheshmoghab
🌐
دانلود مستقیم فایل APK (بدون نیاز به گوگل‌پلی/فیلترشکن):
🔗
https://cheshmehoghab.app
(همچنین کانال رسمی خود برنامه برای دریافت آپدیت‌ها:
@CheshmehOghabApp
)
📌
#معرفی_اپلیکیشن
#چشم_عقاب
#آفلاین
#بدون_اینترنت
#ماهواره
#نت_ملی
#کانفیگ
#VPN
#Eagle_Eye
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/archivetell/5136" target="_blank">📅 12:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یوتیوب داخلی
https://zintube.ir
همه ویدئو ها توش نیست ولی بهتر از هیچیه
ادمینایی که میخوان کلیپ آموزشی درست کنن ، به خاطر راحتی ممبرا از این استفاده کنن تو این شرایط
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/archivetell/5135" target="_blank">📅 12:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">لینک داخلی شیر و خورشید
دانلود
Pass :
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/5134" target="_blank">📅 11:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5133">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اگه نتونستید به تلگرام وصل بشید وارد سایت زیر بشید
https://market.qeshmyar.com/telegram/
بعد تو قسمت سرچ ، آیدی کانال مورد نظرتون رو بدون @ وارد کنید و بعد بارگذاری رو بزنید ، مطالب کانال رو میاره
مثلا کانال ما سرچ کنید
archivetell</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/5133" target="_blank">📅 11:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5132">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">لینک گروه بچه های قشنگ آرشیو تل
😁
https://t.me/+xes6CqzcVcwwODFk</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/5132" target="_blank">📅 11:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5131">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CDN_IP_Finder@ArchiveTell.html</div>
  <div class="tg-doc-extra">59.2 KB</div>
</div>
<a href="https://t.me/archivetell/5131" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/5131" target="_blank">📅 10:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚀
معرفی کامل‌ترین اسکنر تحت وب برای پیدا کردن آی‌پی‌های تمیز (CDN IP Finder)
---
پیدا کردن آی‌پیِ تمیز برای متد «دامین فرانتینگ» (مثل برنامه شیر و خورشید) همیشه یکی از بزرگترین دغدغه‌ها بوده. امروز می‌خوایم یه ابزار به‌شدت خفن، ایرانی و اوپن‌سورس به اسم CDN IP Finder رو معرفی کنیم که این کار رو به ساده‌ترین شکل ممکن براتون انجام می‌ده.
🔥
چرا این اسکنر شاهکاره؟
چون کلاً روی یه فایل HTML سوار شده! یعنی بدون نیاز به سرور، ترموکس، پایتون یا هر پیش‌نیاز دیگه‌ای، مستقیم تو مرورگر گوشیتون اجرا می‌شه. ازونجایی که تست‌ها با اینترنت خودتون انجام می‌شه، نتایج ۱۰۰٪ برای اپراتور شما (ایرانسل، همراه اول، شاتل و...) دقیق و شخص‌سازی‌شده است.
✨
ویژگی‌های بی‌نظیر این ابزار:
🔸
پشتیبانی از ۴ غول بزرگ: قابلیت اسکن آی‌پی‌های Akamai، Google CDN، Amazon CloudFront و Azure.
🔸
تشخیص خودکار اینترنت: خودش می‌فهمه از چه اپراتوری استفاده می‌کنید و بر همون اساس تست می‌گیره.
🔸
داشبورد حرفه‌ای: بهتون نمودار پینگ، تاریخچه اسکن‌های قبلی و حتی QR کد (برای انتقال سریع آی‌پی‌ها به یه گوشی دیگه) می‌ده.
🔸
پیشنهاد SNI: دقیقاً بهتون می‌گه برای هر شبکه‌ای که اسکن کردید (مثلاً آکامای)، چه SNI ای رو باید تو برنامه وارد کنید.
🛠
آموزش استفاده سریع (تست با مرورگر):
1️⃣
اینترنت گوشی رو (بدون فیلترشکن) روشن کنید.
2️⃣
لینک نسخه تحت وب اسکنر رو (که پایین پست گذاشتیم) تو مرورگر باز کنید. (یا می‌تونید فایل index.html رو از گیت‌هاب دانلود و تو گوشی باز کنید).
3️⃣
شبکه‌ای که می‌خواید (مثلاً Akamai) رو انتخاب کنید و دکمه اسکن رو بزنید.
4️⃣
بعد از اتمام، آی‌پی‌های سبزرنگ رو با یک کلیک کپی کنید.
5️⃣
برید داخل برنامه «شیر و خورشید» ➔ تنظیمات ➔ بخش CDN Fronting. آی‌پی‌ها و SNI مربوطه‌اش رو وارد کنید و استارت بزنید!
🎉
(توجه: تو صفحه گیت‌هابِ پروژه، چندتا اسکریپت خفن هم برای اسکن از طریق سرور مجازی / لینوکس قرار داده شده که خوراکِ بچه‌های حرفه‌ای‌تریه که سرور دارن).
🔗
لینک مستقیم نسخه تحت وب (باز کردن بدون فیلترشکن):
🌐
https://htmlpreview.github.io/?https://github.com/hossein8360/cdn-ip-finder/blob/main/index.html
🔗
لینک صفحه گیت‌هاب پروژه (برای دانلود فایل‌ها و اسکریپت‌ها):
🌐
https://github.com/hossein8360/cdn-ip-finder
📌
#معرفی_ابزار
#اسکنر
#آی_پی
#آکامای
#شیر_و_خورشید
#نت_ملی
#CDN
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/5130" target="_blank">📅 10:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚀
لیست داغ آی‌پی‌های تمیز آکامای (تست‌شده روی ایرانسل)
---
رفقا سلام!
✋
یکی از ممبرهای گل و فعال کانال دست‌پر اومده و یه لیست تازه از آی‌پی‌های اسکن‌شده و تمیزِ آکامای (Akamai) رو برامون فرستاده که همین الان روی نت ایرانسل عالی جواب دادن.
💡
نکته طلایی (آموزش استفاده):
به گفته‌ی این رفیقمون، نیازی به هیچ کار عجیب و غریبی نیست! فقط کافیه تو برنامه‌تون (مثل کلاینت شیر و خورشید):
۱. گزینه Protocol رو روی حالت
cdn fronting
قرار بدید.
۲. آی‌پی‌های زیر رو کپی کنید و تو بخش
cdn ips
(یا کادر مربوط به آی‌پی) وارد کنید و استارت بزنید.
👇
لیست آی‌پی‌ها برای کپی سریع:
23.44.201.149
23.212.253.227
23.44.201.185
23.44.201.17
23.62.54.24
23.58.95.144
104.83.198.44
92.123.102.153
184.51.252.134
23.53.40.147
184.51.252.176
2.18.64.212
172.104.251.198
2.18.79.101
23.216.77.181
92.123.102.89
23.216.77.80
96.16.53.132
23.53.40.139
23.48.165.70
2.21.20.143
23.43.85.155
23.48.23.184
23.207.210.83
23.209.125.169
23.48.23.172
2.21.240.22
23.55.110.82
23.216.77.35
23.58.95.138
23.33.40.149
23.48.23.146
23.209.125.145
92.123.102.130
23.53.40.121
23.48.23.11
23.201.248.171
23.209.125.27
23.48.23.176
23.207.210.86
23.55.161.151
92.123.103.89
2.23.7.34
23.207.210.80
23.48.23.165
23.48.23.173
23.48.23.156
23.55.110.74
173.222.107.202
23.213.161.140
23.48.23.134
23.204.152.160
2.23.97.120
(دمِ ممبر خوبمون گرم بابت اسکن و اشتراک‌گذاری این لیست
🤍
)
📌
#آی_پی
#آکامای
#ایرانسل
#دامین_فرانتینگ
#شیر_و_خورشید
#بدون_فیلتر
#Akamai
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/5129" target="_blank">📅 10:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ربات های جست و جو در تلگرام
@en_SearchBot
@argo
@tgdb_search_bot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/5128" target="_blank">📅 10:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کانفیگ من کجاییی ،
کانفیگ پینگ پاییییین ،</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/5127" target="_blank">📅 09:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👾
لیست دانلود برنامه ها با نت ملی
1️⃣
WhiteDNS
1.4.0
(نسخه ی رسمی)
1️⃣
WhiteDNS
(Windows)
1.0.3
4️⃣
NekoBox v8a
●
NekoBox v7a
1.4.2
7️⃣
The Feed
0.17.5
📱
Telegram
(گوگل پلی)
12.7.3
📱
Telegram
(رسمی)
12.7.3
📱
Telegram
(Windows)
12.7.2
💩
Whatsapp
2‌.26‌.17.‌72
💬
Instagram
v415.0.0.36.76
👑
ShiroKhorshid
2026.05.14
5️⃣
Mhrv Rs
v1.9.26
📱
MasterHttpRelayVPN
📱
TunnelX
v1.2.24
📶
Npv
123
📶
V2box
5.3.4
📶
V2rayTun
5.23.73
📶
V2ray Ng
2.18
📶
V2ray Ng
(Windows)
3️⃣
Am tunnle
(pro)
37
3️⃣
Am tunnle
(lite)
🕊
Slipnet
2.5.3
2️⃣
MasterDNS
HN 1.2.3
2️⃣
Masterdns
GG 1.1.0
📶
Windscribe
4.0
📶
Open vpn
3.71
📶
Open vpn
(Windows) 3.8.0.4528
8️⃣
Oghab
🤖
Happ
3.20.4
💻
Happ
(Windows)
📶
Psiphon
462
📶
Psiphon
(Windows)
8️⃣
Bd net
104
6️⃣
Mahsang
15
📶
http injector
6.5.0
📶
Wireguard
1.0.20260315</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/archivetell/5126" target="_blank">📅 09:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5125">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">#اختصاصی
​یک ماه اشتراک رایگان Duolingo Super
​لینک :
https://www.duolingo.com/redeem
​
​کد:
UBERMDAYSABUP6M
​از دسترسی پرمیوم بدون تبلیغات لذت ببرید.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/archivetell/5125" target="_blank">📅 09:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5124">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">لینک لیست پخش اسپاتیفای را ارسال کنید تا فایل فشرده ZIP شامل تمامی قطعات، تگ‌های شناسایی (ID3) و تصویر جلد آلبوم دریافت کنید
@SpotifyDownloaderExdbot
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/5124" target="_blank">📅 09:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIR NETLIFY</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rx1mihOCjo0a8hBbltDdRRrjL5wujtKEP8nz2vjj4gL7bXTkNTr7LHGgevWYJJv6HI5otS1t4hDdkPdjpyOK0YUd5UveQHmWujS3QjRmpT6_-ExM2n_xiIpsXJQ8Hlh0pwV4SYxf6YJZPcb6QRqp6ncNQmCkvb3Y6DlaLPmHERi13mBAq0Tj5bipxuXpxQ1_FD296EPlyNPi4eQ3A_2f4Fp_rDgFG_DIA8oQ4YvGCNnKADpcrbgTTS1GUHZ4HuEoGLPNDhm3B_JUJE6RXg7493O0OjZFyfgEhfJ9iDlt-HJmHEjayHKPCBxQb3WfrJbQP7Xy0yvfcGqfHCmxy2Qw3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txp5ZjX-F0YaXZnNGJDfiMTefR3F1p3-KFoijjDQ38HseAv4wYxps0OqGXEyAsTaHiuXmiAyVb4gjsyH42NJxl0KGiabMUwVEW7yCFkxoXL7h78bLsPGNztIsBq1aLQwu0Ktw2cqrY1xuuG6ofC3CJCvQoQVBLNbe1OqUim9gh8_HBq76tVI9Fyyo3-H9vUAsgANlLqxSSq6467huG3PM7Kid-kuUxEW0fA4zjMEhbUzcfp2pmD2lwZnSBAhbK6pmIF3zec1hmHhvHblue8ofKKeznNogmy6yGRDqGCGsGZ9hadAv3W98LUEsxmX7iUHY-jH5eIXphIJHfeemG1Qkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش اتصال بدون شکن با متود
🥒
🔹
مثل همیشه یه نتلیفای بسازید و پروژه رو دپلوی کنید
🔸
به جمینای این پرامپت رو بدید
Output exactly 25 raw domain names of old, obscure, and non-famous websites that are hosted on Amazon CDN (CloudFront), Cloudflare, or Netlify. Provide ONLY the list of domains, with each domain on a new line. Do not include any conversational filler, introductory text, numbers, or bullet points. Format the domains strictly without "http://", "https://", or "www." (e.g., example.com).
🔹
یه لیست میده بهتون یکیشو رندوم بردارید برید داخل دامنه پروژه نتلیفای ثبت کنید
🔸
نیاز به هیچ تاییدی نیست فقط باید ثبت بشه همین
🔺
اگه ارور
"
Another project is already using this domain
"
داد یعنی دامنه رو قبل شما یکی زده یه دامنه دیگه پیدا کنید
🔺
با این سایت
هم میتونید زیر دامنه های یه دامنه رو پیدا کنید اونا رو بزنید
🔹
وارد کانفیگ ساز بشید و با دامنه ای که ثبت کردید کانفیگ بسازید
🔸
اکثر سرور ها راه افتادن
🔹
در قسمت آیپی و sni هر دو این رو بزنید
104.198.14.52
🟢
کانفیگ بسازید و وصل
🔵
@IR_NETLIFY</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/5120" target="_blank">📅 03:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚀
معرفی ابزار Skirk: دور زدن فیلترینگ با پوششِ گوگل درایو!
🤯
---
رفقا سلام!
✋
امروز می‌خوایم یه ابزار خفنِ اوپن‌سورس و ایرانی رو معرفی کنیم که ایده‌اش واقعاً شاهکاره.
ابزار Skirk، ترافیک اینترنت شما رو می‌گیره، رمزش می‌کنه و به عنوان یه فایل ناشناس، می‌فرستتش داخل صندوق پستیِ Google Drive شما. بعد یه سرور که اون‌ور آب دارید، این فایل‌ها رو از گوگل درایو می‌خونه، به سایت اصلی وصل می‌شه و جواب رو دوباره از طریق گوگل درایو برمی‌گردونه به گوشی یا سیستم شما!
🔥
چرا این روش خیلی خفنه؟
چون سیستم فیلترینگ (DPI) فقط می‌بینه که شما دارید تو اکانت گوگل درایوتون یه سری فایل رو آپلود و دانلود می‌کنید (که کاملاً هم رمزنگاری شده است). این یعنی یه ارتباط صددرصد وایت‌لیست و امن با یکی از معتبرترین دامنه‌های دنیا!
🛠
نیازمندی‌های این روش (برای حرفه‌ای‌ها):
این روش به درد کاربرای عادی که دنبال یه دکمه اتصال می‌گردن نمی‌خوره. شما نیاز دارید به:
1️⃣
یک سرور مجازی (VPS) که نت آزاد داشته باشه (برای نصب بخشِ Exit سیستم).
2️⃣
یک اکانت گوگل معمولی (جیمیل).
3️⃣
نصب کلاینت روی گوشی یا لپ‌تاپ خودتون.
⚡️
تغییرات نسخه جدید (v0.1.45):
تو این آپدیتِ داغ، سازنده یه فایل نصبی پرتابل (Portable) برای ویندوز با رابط کاربری گرافیکی اضافه کرده که کار رو خیلی راحت می‌کنه.
📥
لینک‌های دانلود مستقیمِ کلاینت (نسخه v0.1.45):
(توجه: برای نصب سرور، به صفحه گیت‌هاب پروژه که پایین‌تر گذاشتیم مراجعه کنید).
📱
اندروید (APK):
🔗
https://github.com/ShahabSL/Skirk/releases/download/v0.1.45/skirk-android-arm64.apk
💻
ویندوز (نسخه پرتابل و گرافیکی با رابط کاربری):
🔗
https://github.com/ShahabSL/Skirk/releases/download/v0.1.45/Skirk_windows_x64_portable.zip
💻
ویندوز (نسخه فقط خط فرمان/CLI):
🔗
https://github.com/ShahabSL/Skirk/releases/download/v0.1.45/skirk-windows-amd64.zip
🐧
لینوکس:
🔗
https://github.com/ShahabSL/Skirk/releases/download/v0.1.45/skirk-linux-amd64.tar.gz
📖
لینک گیت‌هاب برای آموزش کاملِ نصب سرور (بخش Exit):
https://github.com/ShahabSL/Skirk
📌
#معرفی_ابزار
#گوگل_درایو
#اسکیرک
#نت_ملی
#تونل
#Skirk
#VPS
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/archivetell/5119" target="_blank">📅 01:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آنقدر سخت که عقل از قبولش سر باز زند و آنقدر زهر که زبان از بیانش تلخ گردد...</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/5118" target="_blank">📅 00:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚀
معرفی ابزار Whitelist Bypass: عبور از فیلترینگ با پوشش تماس تصویری «بله»!
🤯
---
رفقا سلام!
✋
امروز یه پروژه مهندسی‌معکوس‌شده‌ی به‌شدت فنی و خفن به اسم Whitelist Bypass رو معرفی می‌کنیم. این ابزار، ترافیک اینترنت شما رو مخفیانه داخل یک «تماس تصویری» در پلتفرم Bale Meet (بله) جا می‌ده و از سرورهای داخلی عبور می‌ده!
🔥
مکانیزم این ابزار چطوره؟
از دید سیستم فیلترینگ (DPI)، شما در حال یک تماس ویدیویی کاملاً عادی روی سرورهای وایت‌لیست‌شده‌ی «بله» هستید؛ اما در واقعیت، دیتای اینترنت آزاد داره از طریق تونل‌های ویدیویی (VP8) یا کانال‌های داده (DataChannel) بین دو دستگاه رد و بدل می‌شه!
این سیستم دو بخش داره:
1️⃣
Creator (سرور): دستگاهی که اینترنت آزاد داره و تماس رو «ایجاد» می‌کنه (معمولاً لپ‌تاپ یا سرور مجازی خارج از کشور).
2️⃣
Joiner (کلاینت): دستگاهی که نت ملی داره و به اون تماس «می‌پیونده» (مثل گوشی یا لپ‌تاپ داخل ایران).
💻
آموزش راه‌اندازی سریع:
🔸
تنظیم بخش Creator (روی دستگاهی که نت آزاد دارد):
۱. نسخه دسکتاپ Creator رو متناسب با سیستم‌عاملتون (از لینک‌های پایین) دانلود و نصب کنید.
۲. برنامه رو باز کنید، روی علامت + بزنید و تب Bale رو انتخاب کنید.
۳. با شماره بلهِ خودتون لاگین کنید. برنامه خودکار یه تماس می‌سازه.
۴. لینکِ اتصالی (Join Link) که بهتون می‌ده رو کپی کنید و برای گوشی/دستگاه کلاینت بفرستید.
📱
تنظیم بخش Joiner (روی دستگاهی که نت ملی دارد):
۱. نسخه Joiner رو (مثلاً فایل APK برای اندروید) دانلود و نصب کنید.
۲. لینک اتصالی که از مرحله قبل گرفتید رو تو برنامه پیست کنید.
۳. دکمه GO رو بزنید و دسترسی VPN رو بهش بدید. تمام! کل ترافیک گوشی از تماس ویدیویی بله عبور می‌کنه.
⚠️
نکات بسیار مهم:
🔹
امنیت: این تونل برای دسترسی به اینترنت آزاده، نه مخفی موندن هویت. بله می‌دونه شما کی هستید و به کجا وصل شدید. پس فقط برای کارهای روزمره و سایت‌های امن (HTTPS) استفاده کنید.
🔹
این ابزار یکم حرفه‌ای‌تر از نسخه‌های قبلیه و برای کسایی که سرور مجازی (VPS) دارن، بهترین گزینه برای ساخت تونل محسوب می‌شه.
📥
لینک‌های دانلود مستقیم (نسخه v0.1.0):
💻
فایل‌های بخش Creator (برای لپ‌تاپ/سرور دارای نت آزاد):
🔹
ویندوز:
🔗
https://github.com/kulikov0/whitelist-bypass-iran/releases/download/v0.1.0/Whitelist.Bypass.Creator-0.1.0-x64.exe
🔹
مک (پردازنده M1/M2):
🔗
https://github.com/kulikov0/whitelist-bypass-iran/releases/download/v0.1.0/Whitelist.Bypass.Creator-0.1.0-arm64.dmg
🔹
لینوکس:
🔗
https://github.com/kulikov0/whitelist-bypass-iran/releases/download/v0.1.0/Whitelist.Bypass.Creator-0.1.0.AppImage
📱
فایل‌های بخش Joiner (برای دستگاهِ دارای نت فیلترشده):
🔹
اندروید (APK):
🔗
https://github.com/kulikov0/whitelist-bypass-iran/releases/download/v0.1.0/whitelist-bypass.apk
🔹
آی‌او‌اس (IPA برای سایدلود):
🔗
https://github.com/kulikov0/whitelist-bypass-iran/releases/download/v0.1.0/whitelist-bypass-proxy.ipa
🔹
ویندوز (کلاینت):
🔗
https://github.com/kulikov0/whitelist-bypass-iran/releases/download/v0.1.0/WhitelistBypass.Joiner-0.1.0-x64.exe
📌
#معرفی_ابزار
#بله_میت
#نت_ملی
#تونل
#وایت_لیست
#Whitelist_Bypass
#P2P
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/archivetell/5117" target="_blank">📅 23:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚀
معرفی ابزار BaleVPN: تبدیل پیام‌رسان «بله» به تونل اینترنت آزاد!
🤯
---
رفقا سلام!
✋
امروز یه ابزار به‌شدت خلاقانه (P2P) رو معرفی می‌کنیم که ترافیک اینترنت رو از طریق زیرساخت «تماس صوتیِ پیام‌رسان بله» منتقل می‌کنه!
مکانیزم کار چطوره؟
🔸
یک گوشی نقش سرور رو داره: اینترنت سالم و آزاد خودش رو به اشتراک می‌ذاره.
🔸
گوشی دیگه نقش کلاینت رو داره: تمام اینترنتش رو از طریق سرور می‌گیره.
از دید سرورهای بله، این ارتباط فقط یک تماس صوتی طولانی بین دو مخاطبه! بدون نیاز به سرور خارجی، بدون ثبت‌نام جدید و پرداخت پول؛ فقط دو حساب بله که شماره همدیگه رو سیو داشته باشن.
📱
آموزش راه‌اندازی گام‌به‌گام (برای ۲ گوشی اندرویدی):
۱. پیش‌نیازها و نصب:
فایل APK رو از لینک‌های پایین دانلود و روی هر دو گوشی نصب کنید. (روی هر دو گوشی با شماره موبایلِ خودتون لاگین کنید؛ اگه شماره مجازی غیرایرانی بدید، کد تایید بله داخل تلگرامتون میاد!).
۲. تنظیم گوشی سرور (اونی که نت آزاد داره):
در صفحه اصلی برنامه، سوئیچ حالت رو روی Server (سرور) بذارید. سرویس خودکار شروع می‌شه و منتظر اتصال می‌مونه. (سرور همیشه باید روشن و برنامه در حال اجرا باشه. در اولین اتصال، روی گوشی سرور نوتیفیکیشن میاد که باید Allow/تایید رو بزنید).
۳. تنظیم گوشی کلاینت (اونی که نت فیلتر داره):
سوئیچ رو روی Client (کلاینت) بذارید. روی Peer Select (انتخاب مخاطب) بزنید و اکانتِ گوشیِ سرور رو انتخاب کنید. بعد روی VPN Start بزنید و دسترسی رو تایید کنید. تمام! اینترنت متصل شد.
⚠️
نکات به‌شدت مهم:
🔒
حریم خصوصی: ترافیک رمزنگاری می‌شه (DTLS)، اما این ابزار برای ناشناس موندن (Anonymity) نیست و سرورهای بله میانجی هستن. حتماً از سایت‌های امن (HTTPS) استفاده کنید و ترجیحاً اکانت بله رو با شماره مجازی بسازید.
⚖️
استفاده مسئولانه: فقط برای وب‌گردی، پیام دادن و کارهای روزمره خوبه. دانلود سنگین، استریم ویدیو یا تورنت اکیداً ممنوع! (چون ترافیک غیرعادیِ یک «تماس صوتی» سریعاً تو بله لو می‌ره و پروژه رو برای همه مسدود می‌کنن).
💡
دو فوت کوزه‌گری:
1️⃣
اتصال لپ‌تاپ: برای اینکه نتِ آزادِ گوشی کلاینت رو به لپ‌تاپ هم برسونید، اپلیکیشن EveryProxy رو روی کلاینت نصب کنید و هات‌اسپات بسازید.
2️⃣
نسخه فوق‌حرفه‌ای: اگر حرفه‌ای هستید، می‌تونید سرور Node.js رو روی لپ‌تاپ/سرورِ لینوکس یا macOS (با TUN واقعی و NAT هسته‌ای) ران کنید که سرعتش بی‌نظیره و گوشی اندرویدی رو به عنوان کلاینت بهش وصل کنید.
📥
لینک‌های دانلود مستقیم (نسخه 1.3.2):
(فایل اندروید رو به صورت فایل تو کانال هم براتون می‌ذاریم)
📱
نسخه اندروید:
🔗
https://github.com/kookoo1sabzy/BaleVPN/releases/download/v1.3.2/BaleVpn-1.3.2-release.apk
💻
نسخه ویندوز:
🔗
https://github.com/kookoo1sabzy/BaleVPN/releases/download/v1.3.2/balevpn-1.3.2-win-x64.exe
🐧
نسخه لینوکس:
🔗
https://github.com/kookoo1sabzy/BaleVPN/releases/download/v1.3.2/balevpn-1.3.2-linux-x64
🍏
نسخه مک (M1 و M2):
🔗
https://github.com/kookoo1sabzy/BaleVPN/releases/download/v1.3.2/balevpn-1.3.2-macos-arm64
🍏
نسخه مک (اینتل):
🔗
https://github.com/kookoo1sabzy/BaleVPN/releases/download/v1.3.2/balevpn-1.3.2-macos-x64
📌
#آموزش
#معرفی_ابزار
#بله_وی_پی_ان
#نت_ملی
#تونل
#BaleVPN
#P2P
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/archivetell/5116" target="_blank">📅 23:42 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
