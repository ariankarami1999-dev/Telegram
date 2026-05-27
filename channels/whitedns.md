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
<img src="https://cdn4.telesco.pe/file/o6jWTmeaYBohZo9fGuxmbaXnOR2I8mdqfZVGImEnSO0gLDTVn8iv0IZ4TwnFxfdG6AkrY0HSXEhItdkNeX0-H72ECjQPF_myqm3XvIL2a_FrO32Ri--Bh_L0xsdQdgH6dliA19iiDrfdwj8thxamCVO3ZnM0Ap8yQTzkhU4PnQz7igxb7LK-tpCdCDj0oeJBrthGNscrveZLzqcfTqAI0yGu0QmBMGRjJSeHrgbWpnRcqvPbIUYWlngem55xMr9yp0cJjJiYSHpczNe8PMkAYr2X93lYMPUifLLqhHpZbvBgPzzaxCtURT2ztlFlWBjNwbYZxGV4WQbEQloAYLwTpA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 97.2K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhisperInHeaven</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 14:04:32</div>
<hr>

<div class="tg-post" id="msg-824">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔥
نسخه WhiteDNS Desktop V1.0.0-beta4  با کمی بازتر شدن شرایط فیلترینگ و قابل‌استفاده‌تر شدن روش‌های پایدارتر، تصمیم گرفتیم پشتیبانی از V2Ray را به نسخه کامپیوتر اضافه کنیم.  در این نسخه VLESS، VMess و Trojan پشتیبانی می‌شوند، امکان وارد کردن کانفیگ و Subscription…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/whitedns/824" target="_blank">📅 12:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-820">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta4-linux-arm64.rpm</div>
  <div class="tg-doc-extra">24.8 MB</div>
</div>
<a href="https://t.me/whitedns/820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
نسخه WhiteDNS Desktop V1.0.0-beta4  با کمی بازتر شدن شرایط فیلترینگ و قابل‌استفاده‌تر شدن روش‌های پایدارتر، تصمیم گرفتیم پشتیبانی از V2Ray را به نسخه کامپیوتر اضافه کنیم.  در این نسخه VLESS، VMess و Trojan پشتیبانی می‌شوند، امکان وارد کردن کانفیگ و Subscription…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/whitedns/820" target="_blank">📅 12:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-poll">
<h4>📊 کسی به نسخه جدید دسکتاپ با v2ray تونست وصل بشه؟#موقت</h4>
<ul>
<li>✓ وصل شد</li>
<li>✓ وصل نشد</li>
<li>✓ دانلود نکردم، اندروید دارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/whitedns/819" target="_blank">📅 12:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-818">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/818" target="_blank">📅 11:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-817">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستانی که از نسخه اندروید اپ WhiteDNS  استفاده میکنند.
برای بیشتر کردن سرعت و پایداری
، میتونید با وارد شدن به بخش ریزالور ها، یک پروفایل جدید با مقادیر زیر بسازید
1.1.1.1
1.0.0.1
8.8.8.8
8.8.4.4
9.9.9.9
149.112.112.112
208.67.222.222
208.67.220.220
94.140.14.14
94.140.15.15
برای کم کردن مصرف
، سپس وارد بخش تنظیمات و پیشرفته بشید و‌مقادیر زیر رو تغییر بدید.
Upload Dup = 1
Download Dup = 2
اگر سرعت شما قابل قبول نبود، دوباره مقادیر Dup رو بالا ببرید.
توجه کنید که این مقادیر فقط مناسب اینترنت پایدار هستش. در صورت بازگشت اینترنت به وضعیت قبلی، باید کانفیگ های متفاوتی اعمال کرد.
ممنون
تیم White DNS</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/whitedns/817" target="_blank">📅 11:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آموزش اتصال V2Ray در نسخه کامپیوتر
دریافت لیست کانفیگ ها برای ایمپورت کردن
https://t.me/whitedns/804
https://t.me/whitedns/805</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/whitedns/816" target="_blank">📅 11:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta4-release-windows-x64.zip</div>
  <div class="tg-doc-extra">23.8 MB</div>
</div>
<a href="https://t.me/whitedns/812" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/812" target="_blank">📅 11:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-811">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHIlkY5pBtMwpsSYRA2avTt7PewIDD0t3xWWt490_ndL9okgFVPSQf34Q6qwRUIs3SL-TfBGM8pPjBVKBFw3lbsgsuZQhUePHLKI9FtT13rrZtk5W-w5TpDciyjUDBI16P07WDi3Ywo6hiuC9dXlQ9cRXKD5ed7axuWwG-RtGxKKRPpwpZhoZXHOIm5SrBybdUmBp5qEE400mkQ0yUd3X6kMngBJrPKexUlTeJNk0iZ9_V49jQxu8XQHSKD94NXkIB-N_nWHgPiMaMPi1NEMbfteDDNZQrSOXaUJF4b33uvziH5W1s4AZcNBut4I0_bBZB9vfh3OprMU77t9VqRlsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نسخه WhiteDNS Desktop V1.0.0-beta4
با کمی بازتر شدن شرایط فیلترینگ و قابل‌استفاده‌تر شدن روش‌های پایدارتر، تصمیم گرفتیم پشتیبانی از V2Ray را به نسخه کامپیوتر اضافه کنیم.
در این نسخه VLESS، VMess و Trojan پشتیبانی می‌شوند، امکان وارد کردن کانفیگ و Subscription اضافه شده، و ابزارهای داخلی برای مسیر‌دهی هوشمند، مسدود کردن تبلیغات و عبور مستقیم ترافیک سایت‌های ایرانی از شبکه داخلی فراهم شده است.
اتصال MasterDNS هم پایدارتر و کم‌مصرف‌تر شده؛ درخواست‌های تکراری حذف شده‌اند و مصرف اینترنت حالا تقریباً شبیه یک VPN معمولی است.
✅
پشتیبانی از V2Ray اضافه شده است.
✅
پشتیبانی از VLESS، VMess و Trojan اضافه شده است.
✅
امکان وارد کردن کانفیگ و Subscription اضافه شده است.
✅
آدرس‌های خصوصی و داخلی مستقیم وصل می‌شوند و از مسیر V2Ray عبور نمی‌کنند.
✅
سایت‌ها و آی‌پی‌های ایرانی با geosite-ir و geoip-ir مستقیم از شبکه داخلی عبور می‌کنند.
✅
تبلیغات، بدافزارها، فیشینگ و ماینرها مسدود می‌شوند.
✅
همه ترافیک‌های دیگر از پروکسی V2Ray انتخاب‌شده عبور می‌کنند.
✅
کش داخلی sing-box برای لیست‌های قوانین آنلاین فعال شده است.
✅
MasterDNS پایدارتر و کم‌مصرف‌تر شده است.
✅
درخواست‌های تکراری حذف شده‌اند و مصرف اینترنت تقریباً شبیه یک VPN معمولی شده است.
✅
سرعت اتصال بهتر شده و Packet Loss کمتر شده است.
✅
ریزولورها به گزینه‌های بین‌المللی و قابل اعتماد مثل
1.1.1.1
و
8.8.8.8
تغییر کرده‌اند.
✅
حالت تاریک، Scanner جدید، بکاپ کامل و رفع باگ‌های زیاد هم اضافه شده‌اند.
@WhiteDNS</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/811" target="_blank">📅 11:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-810">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">Defyx VPN
🚀
یک اپلیکیشن VPN مدرن، هوشمند و متن‌باز که با Flutter ساخته شده و با تمرکز بر امنیت، حفظ حریم خصوصی و تجربه کاربری جدید، دسترسی آزاد و رایگان به اینترنت را فراهم می‌کند.
🌐
🔓
🔹
متن‌باز و قابل بررسی
📜
🔹
رابط کاربری مدرن و روان
💻
🔹
تمرکز بر حریم خصوصی و امنیت
🔒
🔹
مناسب برای دور زدن محدودیت‌های اینترنت
🕸
بروزرسانی جدید
⬇️
GitHub:
https://github.com/UnboundTechCo/defyxVPN
📂
@whitedns</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/whitedns/810" target="_blank">📅 10:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-809">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">Orbot for Android v17.9.4 BETA 2 (tor
0.9.4.8
)
بروزرسانی جدید
Orbot 17.9.4 (2.7.0) برای اندروید منتشر شد
📲
این بروزرسانی، موتور Tor را ارتقا داده، روش‌های اتصال جدید اضافه کرده و چند مشکل اتصال را برطرف می‌کند
🔒
🔧
.
✨
تغییرات مهم:
• ارتقا به Tor
0.4.9.8
برای پایداری و عملکرد بهتر
🚀
• اضافه شدن پشتیبانی از Shadowsocks داخل خود Orbot
🌐
• امکان استفاده همزمان با پل‌های obfs4 ،Meek و WebTunnel
🌉
• گزینه جدید «بدون پروکسی» برای خاموش کردن سریع پروکسی بدون حذف تنظیمات
⚙️
• بروزرسانی پل‌ها و ابزارهای دور زدن فیلترینگ
🛡
• بهبود DNSTT برای اتصال بهتر در اینترنت‌های محدودشده
📡
• رفع چند باگ و مشکل اتصال
🐛
📱
مناسب برای افرادی که از Tor برای دسترسی آزادتر و امن‌تر به اینترنت استفاده می‌کنند
🔐
🌍
.
دانلود
📥
https://github.com/guardianproject/orbot-android/releases/tag/17.9.4-BETA-2-tor-0.4.9.8
@whitedns</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/whitedns/809" target="_blank">📅 10:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-808">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دوستان سلام :
این یک مدت به همه سخت گذشت ، شاید شما اسم دو نفر را بیشتر شنیدید ولی بدونید یک تیم ۳۰ نفره بی نام و نشان پشت این کار بودند  توی بدترین شرایط از همه چیز زدند تا شاید یک روزنه کوچکی باز بمونه ،
ببخشید کم بود ، کافی نبود ،ولی در حد وسع خودمون تلاشمون را کردیم
یک تعداد زیادی از  دوستان پیام دادن ، تشکر کردند و گفتن ادامه بدیم ، خواهش کردند بمونیم
ما هستیم کنارتون ، مگه میشه این همه عشق و محبت را رها کرد
یکم استراحت کنیم ،همه با قدرت بر میگردیم
توی این مدت مراقب خودتون باشید
تیم whitedns
@whitedns</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/whitedns/808" target="_blank">📅 02:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-807">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLgIe4SvUoXJavrrQZv-Kh6c3xmaZxh3yq1qD6OjRI1pDcNDDs8DJRZxAlIdyAwVKoagLr0MvZPK4tNvypSpzuM8HDMU2bvsGLB9-Q6M_MHhf8mSfgbjhRXu8MeibuTCSWE_-oT6koKhwQUIV6BOpUdn85Sy6k3v6_c6YsTyM-cGghOd6MwwTzurOkCkPEkP0yhtsMRbMfEWPiJ1nKKnmpW5lgxTwowXr8mNShfF86ydzQzAT_l0tBX2VuaQxD8tRFho_coQWfhCGlqzAbBOZYk-0YwEr2whIqJGE0RjxStk-b2o97lzN_E3Rp4vSb5YI06ucLNcFWZMKjMiuMep9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#موقت
یادمون نره کسانی که از ظلم پول در آوردند.</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/whitedns/807" target="_blank">📅 19:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-806">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">برای استفاده از کانفیگ های بالا میتونید از اپ v2ray یا دیگر اپ های مشابه استفاده کنید
👆
👆
👆
اپ های قابل استفاده:
npv tunnel
happ
nekobox
MahsaNG
v2raytun
v2box
V2rayN</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/whitedns/806" target="_blank">📅 19:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-805">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2rayconfigs_with_WhiteDNS_2.txt</div>
  <div class="tg-doc-extra">30.2 KB</div>
</div>
<a href="https://t.me/whitedns/805" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">115 کانفیگ تست شده دیگه پینگ 100-200
ممنون ازعلی عزیز برای تست و پاکسازی لیست
@WhiteDNS</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/whitedns/805" target="_blank">📅 19:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-804">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2ray_configs_WhiteDNS.txt</div>
  <div class="tg-doc-extra">38.3 KB</div>
</div>
<a href="https://t.me/whitedns/804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">141 کانفیگ تست شده روی مخابرات پینگ 100-200
ممنون ازعلی عزیز برای تست و پاکسازی لیست
@WhiteDNS</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/whitedns/804" target="_blank">📅 18:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-802">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-BCSv3ed9v7Wswf64sBh9BIV8lKSPbB6jmxSGyLQihMzYr9IBz01AOZD6Z1U3bAwdzw19Oef-oTV2RWbWUqFMfYyW_EZSxi_mWTMSChvjLaro5yDESFNwfRpOJv6S10778FrRLk1o3Vh80Cbpy28jmwI_1dZxKeKY0kd18Adj0GnBLXdLGj6RQjGECBG3R09oslNfEnTjfpBUIDM5e9h54Lsy5NL1DfyTJBTXO7_vM7G2GWnQaiLL1Hi23DhLcgNjMD3YZJGvxgc0PkgdgHUWXwcHecPzhWmXDhQZjlhHyCKaFtrPh7QiokL9yZ_NO9uE_yyfdLH3bX0XsAlW_QmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hfb5IhA7jAan8L1iWm8u1ke3F-qJwVlav10Q92q9mvenPgXijnGgySzZSofms7ZJgZoCisb6mzUROcNO8ilM3sS9FfKOzlVD-AsnPs11gHqytf93RAkfD3TT4jaCZfjFLhCyJfDEZSYSHdG4kRMJvtZguZuUlcBqOIAoGrRQxxHKI3h4t0W45sCYJHl4LX5S4myOBjt4AQc6UzUVgcRz90zHfacqAbWajZ8ImmHU9MVEVs_BzMNx-h1MMfC_ERoBwWTPQxjNJRWnO3G0kV5nVrWlTQFM1tMdfAfquELlpx5yaMPUVRwZo07HDp3USDZEKtQeQ17L4oqu-iVPThLMmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این هم یک تست سرعت با ریزالور های درست و با اختلال کمتر
🤌</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/whitedns/802" target="_blank">📅 17:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-801">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">“}
سلام خدمت همه عزیزان
❤️
امیدواریم این روند ادامه‌دار باشه و اینترنت به‌زودی برای همه اپراتورها به حالت پایدار برگرده.
برای دوستانی که فعلاً به سرویس‌های دیگه دسترسی ندارن، می‌تونید از ریزالورهای زیر استفاده کنید:
1.1.1.1
8.8.8.8
همچنین بهتره مقدار
Duplicate
رو کمتر کنید تا مصرف اینترنت پایین‌تر بیاد و اتصال داخل اپ پایدارتر بمونه.
حتی در صورت برگشت کامل اینترنت، سرورهای WhiteDNS همچنان فعال می‌مونن و می‌تونید ازشون استفاده کنید.
یادمون نره، مارو از کمترین حقوق شهروندی محروم‌کرده بودند. فراموش نمیکنیم.
دم همگی گرم بابت همراهی و صبوری‌تون
🔥
@WhiteDNS</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/whitedns/801" target="_blank">📅 17:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-800">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">در طول ۳ روز گذشته، کاربر های ما ۱۰۰۰ سرور جدید اختصاصی با ربات WhiteDNS ساختن
🎉
@WhiteDNS_installer_bot</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/whitedns/800" target="_blank">📅 09:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-799">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دوستان گرامی :
ما هیچ گروه و کانال دیگری در هیچ پیام رسان خارجی و  داخلی نداریم
تنها گروه رسمی ما :
https://t.me/whitedns_group
تیم whitedns
@whitedns</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/whitedns/799" target="_blank">📅 03:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-797">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOpGxoPfjb9L4qN4aK0H4YpTPIY16AZJ138uOsjOrVHrhOQcpwCB9NmIfnHLVnFYmXSs_bDvv3kJis5Q77In1bJUmsSmrZXFic_Qu0lCrautPButE5VS4Ho9GqCOmQGUtiC3LSdxZUVGptzT1mcLjJML_Kbfzdv4_eYH1ChN3d2GbE4f7Hn4vFQvC-nR4Nl48yncN-Gumxajv3sn8uW-lbSrlJ7ZCZjq68_8Jd11ds0YIwgVLILnj6cq-WqVqPT8E5KuSFIL9N_Y82t0LUG-6ZLO1kGqyBrAd5dFKIJa1JZHUx-fxp1E7COsEBoPCo3SsEMTt5wX107YlfL_QslRHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کیه این تک دلقکو همیشه میزنه
😂
؟
به افتخارش نفری یدونه بزنید ببینه دلقک کیه
🤡</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/whitedns/797" target="_blank">📅 16:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-796">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaBShimecfrTOLtyMOSkgWv7U5cEWnJIL932oBsnepfSTfl64p5jvxMe-Du2FOlvr1Hk8a9AjyjhP1i1y07FOvUBMzSTy-pugyMFonEa5OqaDXwGKfU6lK5VbOn-0OK6F6zdaoPUrSI1YaaEzcgdSrtn26K5PIur8_0ccn_BIzHJr7zK9oX2Il-Qpeg5EcUDwMgRitDlCmOudlH1qRkXcjzrz9WpVc71ffnXX_LB-FyoppuK2TzDCFfh6WxD3dN03GhyxsNojzzGGjm-9OvSppkMgHfUSrG-tCFMi51WzNDLHPV9xYQLx3ihKha2q3AgM2M8Tz34Eo401nUcV52e6mgk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaBShimecfrTOLtyMOSkgWv7U5cEWnJIL932oBsnepfSTfl64p5jvxMe-Du2FOlvr1Hk8a9AjyjhP1i1y07FOvUBMzSTy-pugyMFonEa5OqaDXwGKfU6lK5VbOn-0OK6F6zdaoPUrSI1YaaEzcgdSrtn26K5PIur8_0ccn_BIzHJr7zK9oX2Il-Qpeg5EcUDwMgRitDlCmOudlH1qRkXcjzrz9WpVc71ffnXX_LB-FyoppuK2TzDCFfh6WxD3dN03GhyxsNojzzGGjm-9OvSppkMgHfUSrG-tCFMi51WzNDLHPV9xYQLx3ihKha2q3AgM2M8Tz34Eo401nUcV52e6mgk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/whitedns/796" target="_blank">📅 11:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-795">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESqFgllxjOUz599DErxQu_2NJXL-E2wmmXhFKL2IPJv5jqucrx75LKws4sJHoBcuu954q_18wKq1GBhbfrZligl88-90a2HPLJ9i9hy1iONWAeqH1iANtuvUuN-8ovs8PhKjQUycsWdt0-JJLsPmzVsrGgCEmlpPKxJ_vwWEzi2NNdeNL8JGkvR1bIPXxZIJzWmYAiWXPvIvnET4oKyDwzYER_GArCg2ehh9AYIS_rNGgm9TCJxw3V7AyzaHwezBH5Iv1UZbHGFQe39R1V5w7lHv3gkmmWAyIYjM8pHcMHWPyhAVUlqN0WIpQezYdZNCF1a0uxBIrb5W3KvIr0niAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حال حاضر مشغول تست نسخه جدید اپلیکیشن دسکتاپ WhiteDNS هستیم.
در این نسخه، علاوه بر اضافه شدن حالت دارک مود، تغییرات مهمی در عملکرد داخلی برنامه اعمال شده است.
یکی از تغییرات اصلی این نسخه، تغییر کلاینت داخلی اپ از StormDNS به MasterDNS است.
این تغییر به این معنی نیست که سرورهای StormDNS دیگر قابل استفاده نیستند یا وصل نمی‌شوند. سرورهای StormDNS همچنان قابل استفاده هستند.
اما تنظیمات داخلی برنامه در این نسخه بر اساس آخرین نسخه MasterDNS ساخته شده و در تست‌های اولیه، از نظر سرعت، پایداری و مصرف حجم، عملکرد بهتری نسبت به نسخه‌های قبلی نشان داده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/whitedns/795" target="_blank">📅 09:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-793">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">White DNS
pinned «
دوستان گزارش دادن که Hostinger پولشون رو بلوکه کرده و پشتیبانی جواب نمیده و... ترجیحا نخرید. نکته اینکه شما با دامنه .ir هم میتونید انجام بدید این متد رو اما خب توصیه نمیکنم به شخصه علتش هم واضحه. جای مطمئنی برای دامنه دیدم معرفی میکنم
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/793" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-792">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">دوستان گزارش دادن که Hostinger پولشون رو بلوکه کرده و پشتیبانی جواب نمیده و...
ترجیحا نخرید.
نکته اینکه شما با دامنه .ir هم میتونید انجام بدید این متد رو اما خب توصیه نمیکنم به شخصه علتش هم واضحه.
جای مطمئنی برای دامنه دیدم معرفی میکنم</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/whitedns/792" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-791">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سلام خدمت همه همراهان عزیز  ویدیو آموزش ساخت سرور شخصی که متین عزیز تهیه کردند دقیق همه مسایل رو ‌توضیح‌ میده.   تنها‌ نکته‌ای که باید اشاره کنم، متین از ترمینال برای وارد کردن دستورات و نصب MasterDNS استفاده کرده.   من پیشنهاد میکنم برای راحتی کار شما، بعد…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/whitedns/791" target="_blank">📅 16:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-789">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">💥
موقت
🚫
دوستان :
اگر سروری دارید از جایی  میگیرید که پورت ۲۲ نمیده اصلا خرید نکنید
ظاهراً یک عده دوباره دارند سر مردم کلاه میگذارند
داستان داریم به خدا
لطفا اگر توی گروه های ما کسی داره کلاهبرداری میکنه با ذکر ID گزارش کنید
@WhisperInHeaven
🚫</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/whitedns/789" target="_blank">📅 12:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-787">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سلام خدمت همه همراهان عزیز
ویدیو آموزش ساخت سرور شخصی که متین عزیز تهیه کردند دقیق همه مسایل رو ‌توضیح‌ میده.
تنها‌ نکته‌ای که باید اشاره کنم، متین از ترمینال برای وارد کردن دستورات و نصب MasterDNS استفاده کرده.
من پیشنهاد میکنم برای راحتی کار شما، بعد از خرید دامنه و اتصال DNS از ربات
@WhiteDNS_installer_bot
استفاده کنید.
اگر از این‌ ربات استفاده کنید، فقط با پروکسی کردن تلگرام‌ میتونید سرور خودتون رو مدیریت کنید و در شرایط بحرانی فقط از طریق تلگرام همه چیز رو مدیریت بکنید.
ممنون
@WhiteDNS</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/whitedns/787" target="_blank">📅 05:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-786">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو:
https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو:
https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- خرید دامنه و سرور ارزان با کریپتو(+آموزش)
2- تانل کردن ترمینال با Proxifier و ssh زدن با خود ترمینال
3- تنظیم دامنه در کلودفلر و راه‌اندازی ساده‌ی سرور MasterDNS
4- استفاده از سرور MasterDNS در کلاینت های ویندوز و اندروید WhiteDNS
5- توضیح استفاده از Parallel Testing در WhiteDNS
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز به خریداری یک عدد سرور لینوکسی و دامنه داره(مجموعا 5 دلار نزدیک به 800 هزار تومان) کافی برای اتصال نزدیک به 5 نفر
کانال مستر دی ان اس:
1-
https://t.me/masterdnsvpn
گروهشون:
2-
https://t.me/MasterDnsVPNGroup
کانال وایت دی ان اس:
1-
https://t.me/whitedns
گروهشون:
2-
https://t.me/whitedns_group
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/whitedns/786" target="_blank">📅 05:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-785">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SL_TC5IrYPD7Fuz7i1Ayah8upa8JXoEYUDXiDnXz8_WuHj-uedxdW8rYa6YjbcMEBsCrXJXMt0hlP-9xYWmOck7oQ6vuV27CWZ-S5uJZBTdkWEU5jgjDJ2tyc0icmkw3bSE1v1NC168TML2YZRc6l6_mZ4ow70TIk4qO5_5yhNCj__9eR1oXvVJJOiSHK9wk5lxRFPffoKVW8SXxfsAvO7T_uJw6eoQH7Lw5l7BIkJtY3AbmWBoYk1WCtUmdP4QxboeFakNTzMmVPKoWp1goNv8kb4hwWIrObP2porFhvObilB5YhQ1vF-M74ntDHLFItYLASVoVA7qIU0fwm2rzgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♨️
معرفی ربات جدید WhiteDNS برای راه‌اندازی و مدیریت سرور شخصی MasterDNS
♨️
ربات جدید WhiteDNS آماده استفاده است.
👉
@WhiteDNS_installer_bot
این ربات به شما کمک می‌کند بدون نیاز به درگیر شدن با مراحل پیچیده نصب، سرور شخصی MasterDNS خودتان را روی VPS راه‌اندازی و از طریق تلگرام مدیریت کنید.
✅
نصب خودکار MasterDNS روی VPS
✅
مدیریت سرور از داخل تلگرام
✅
دریافت اطلاعات اتصال و Encryption Key
✅
بررسی وضعیت سرور
✅
ری‌استارت و مدیریت سرویس
✅
مناسب برای استفاده شخصی، دوستان و خانواده
🔐
نکات امنیتی:
اطلاعات کاربر، اطلاعات ورود به سرور، رمز عبور، کلیدها و مشخصات VPS به هیچ عنوان ذخیره یا لاگ نمی‌شود.
اطلاعات فقط در همان لحظه برای اتصال به سرور و اجرای دستور مورد نیاز استفاده می‌شود و بعد از پایان نصب یا اجرای هر دستور، توسط ربات نگهداری نمی‌شود.
بعد از انجام عملیات، اطلاعات ورود و مشخصات سرور توسط هیچ‌کس قابل مشاهده یا دسترسی نیست.
به همین دلیل، کاربران همچنان مالک کامل سرور، دامنه و تنظیمات خودشان هستند.
این ربات فروشنده سرور یا دامنه نیست.
کاربران باید:
* دامنه خودشان را تهیه کنند
* سرور خودشان را تهیه کنند
* دی‌ان‌اس های لازم را روی دامنه تنظیم کنند
هدف ما این است که راه‌اندازی و مدیریت سرور شخصی برای کاربران ساده‌تر شود؛
نه این‌که همه وابسته به چند سرور عمومی و متمرکز بمانند. ما باور داریم کاربران سرعت و پایداری بیشتری با سرورهای شخصی و غیرمتمرکز خواهند داشت.
⚠️
این ربات در اولین نسخه عمومی منتشر می‌شود و ممکن است هنوز باگ یا مشکل داشته باشد.
لطفاً مشکلات و بازخوردها را برای ما ارسال کنید تا سریع‌تر بهترش کنیم.
ویدیو آموزشی خرید سرور و دامنه و تنظیم دی‌ان‌اس به زودی داخل چنل قرار خواهد گرفت.
@WhiteDNS</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/whitedns/785" target="_blank">📅 21:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-784">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7j5_kLM-Nr8nV5iiOxSqqJzx5_wpX3hqLVhDqkzYS2OfieIUCrN_EoPwDsUIM9dpSRm-_xeENztrOSle5ABu0tR6HAsqu-YZekgWEn9z2h4j0dYfcOXVitNU1t67B2NirGKVI-ViyJAECPdvQVrGOIBn3Rqy1h2RactTWXK7ZZ06s7H5FQVxmxnJg8dsuveA7TDgW-pDl3oBJtZ5cbMOM1hJW0hm-9BvLCqQ4xDC6sIdlkJ7zgxRX2vtseSMsnSMUPyJmcKeZXRSfqytBZZDZvxYJjr5VL_lwGjRlnZMJCwCYwzMiCREW1qLbI7pAu76BWrAaIDw0uZbL7-tRNYnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♨️
پروژه جدید WhiteDNS در حال آماده‌سازی است
♨️
تیم WhiteDNS بر روی سیستمی کار میکند که کاربران بتوانند فقط با داشتن یک VPS و یک دامنه، سرور شخصی MasterDNS خودشان را مستقیماً داخل تلگرام راه‌اندازی کنند.
هدف این پروژه این نیست که ما به کاربران سرور یا دامنه بفروشیم یا مدیریت کنیم.
هدف تنها ساده‌تر کردن فرآیندی است که امروز برای خیلی‌ها پیچیده، زمان‌بر و فنی محسوب می‌شود.
در این سیستم، کاربر فقط:
• VPS خودش را تهیه می‌کند
• دامنه خودش را تهیه می‌کند
• DNS Record ها را تنظیم می‌کند
و باقی مراحل توسط ربات و Mini App تلگرام به‌صورت خودکار انجام می‌شود.
سیستم به‌صورت اتوماتیک:
• وضعیت DNS Record ها را بررسی می‌کند
• اتصال دامنه به سرور را تست می‌کند
• MasterDNS را نصب و راه‌اندازی می‌کند
• اطلاعات نهایی مثل Domain و Encryption Key را به کاربر تحویل می‌دهد
در عمل، کاربران می‌توانند بدون درگیر شدن با دستورات پیچیده لینوکس و تنظیمات طولانی، سرور شخصی خودشان را راه‌اندازی و مدیریت کنند.
این پروژه متن‌باز خواهد بود تا همه بتوانند کد آن را بررسی کنند.
در حال حاضر پروژه در مراحل نهایی توسعه قرار دارد و طی روزهای آینده نسخه اولیه آن منتشر خواهد شد.
@WhiteDNS</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/whitedns/784" target="_blank">📅 09:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-783">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/783" target="_blank">📅 18:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-782">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8AmMmF-JDBUJF2RA3YsCnDo_m6yqr3OM9DfbVuNDV7XoJbm8VGFBQpvU1CFl6UJQ6BiM-rrFHKfJfZta9L5RNaYZcNSZBpat-KoVA3KvkxXE-CpfdIfWUltQjUPksMnMqQAYDZaq5reqivXWzbIAnfZbTLbvk5uk0oi6e4xC6J3D2wNWpifjLNkLuW4rqA5HH-VG_CA2xZ2CmPtrrBegLdYG-Ykp3F2OzKXwvxWxJitZkxa-IZB-EDL5jsBBjdUbE_tVLWdsGDEHLR08eVxLJDcFaVv_RKAUpUNolA7agrkZCUZfzL8a6Aj3CpXCnPdn5W--sLJ3evr5nDcf_brrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام دوستان
👋
چون سوالات خیلی تکراری و بی‌هدف شدن
🤔
ما یک گروه با تاپیک‌های مختلف درست کردیم
📂
لطفاً اونجا عضو بشید و توی تاپیک خودش سوال کنید
✅
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/whitedns/782" target="_blank">📅 18:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-781">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIqmSp9brMYv-9yuVZ99Ahiwtm-ctjHNN7DZhZEBCY7fWwUQVM1-4c16-B95z4LQ2-jinDUxFpk9VqmBRw4hrLXRpTzbrvZavipYHd8w5FoINHA_QbJpQ0vWIZ0s6-mCeenFv3XxWihFBNvMhWCau6CDGRbye_eHe293HLOgRSm5Yfi55eXX-FWoSSUZZ4DuF0hOXTxk5rOKFavZ-Gu5XDhZIeoe9W-XpwSRLHr6V7-jNKzD-JGuyzqCB_-pRjxXYBYDpVa_T4dj647FOmLKmwLu_HZQRA8djLhH5cJZFM2F7ef7Dn98FZOLapY4N50_SZOVaud_bxau2SbkZyzyVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش پروکسی و تانل کردن ویندوز
در این ویدیو نحوه پروکسی کردن فایرفاکس با نرم افزار WhiteDNS
پروکسی کردن کردن کروم ادج
و همینطور تانل کردن کل ویندوز با متود جدید آموزش داده شده است !
لینک دانلود ویدیو ( داخلی ) :
https://dl.toolschi.com/view.php?f=9f27edab8159500e.mp4
لینک دانلود نرم افزار  TunnelX ( داخلی ) :
https://uplod.ir/75m7wx9r6c17/TunnelX-v2.1.0__Whitedns.zip.htm
لینک گیت هاب TunnelX
:
https://github.com/MaxiFan/TunnelX/releases
امکان هست که آنتی ویروس  TunnelX رو حذف کند. در صورت نیاز اون رو به لیست نرم‌افزار های سفید آنتی ویروس خود اضافه کنید.
منبع تصویر کانال اینترنت آزاد
1️⃣
@WhiteDNS</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/whitedns/781" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-780">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">+۲۵۰ ریزالور جدید به ربات تلگرام WhiteDNS اضافه شده
برای دریافت وارد بات شوید
@dns_resolvers_bot
و بعد دستور زیر را اجرا کنید
/dns_master</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/whitedns/780" target="_blank">📅 16:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-779">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/779" target="_blank">📅 16:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-778">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">لینک داخلی آموزش ساخت سرور شخصی StormDNS & MasterDNS
https://guardts.ir/f/d68436b0fc33</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/whitedns/778" target="_blank">📅 10:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-774">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMKOjveSsTJGGQQN50vkSdA8h1SXJd77KeBcJHeZzbKeGMce7zYxKnzkcF6oMjuiO7ayg8YKunsJrVIYNvBPXsAvJR2wiyb7wC86NtxsR4dqhvWSfo-G7tmIsAWxu0W_h8X1FCLidXX2WtKOt59_fqWn8G5y-WH8qPE8hh4d4C6ktGnVqJ1TQ5D5eSO2FlDiLIL6sq3lONs8Yp9xQ0XdQUziEMdBFj95aNV7VlDUjLPX0jn8qMcTqGBK1G804oenYBOkCtYKj8QV0_ZfA_mV8VVhK7IcyiwZ7TXYfz6As605ip4ihRiJ1ogF-IE86r6-koIMgrpr-qbWtszp0yEn5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/akDEDTAcUj_jLmGwqqiUmII3sdnLoBS1wxR8xcI5c4pxfLIuYcrLVUBvsu9ffvnuNX5TpiWaeKHEgJV3tc073M0jT-CPv4gfdcduQkGvdzDcO-zCYMAOcYFzzMelXuGClwJWprFNJMGMlWcFjZaV4eXcK26Ac0oB_eO3G0RRtZ7ixV3f5d7sa4V-_KlYQD79YaVt5ruTHnIct00iWmtr5adlpDmHPyu3Fa2ksuCCibfVIKbbbaB8MT-y89z0N-LyHu2xDK5YBQgJqNqpkc4QwPfJjGqKwZwcnx4PwSUUhOxLv4CWAo-OBkFJs5L6L8mI7ue0h_UFFVE8Khjxh87o4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GkXr2T9C_qTmWyaw253mRpW4GrLk_vcrp47MX87It8vae6jfWKn6O5sVL6CxiUrPF_G8RStFBLLykbDjs0ZXMZaGlVH2CSYFwlRsPuQ8g9Oe7vmP606-y6A1UzC4K4jjSAWlV3LqwtVc_AaW3xPBtJCHpSdEhIrbfenuiU_hiLTXU5hOr2bXryjo2OwcTn3zzGsxiDmfh-bm-E-V31copau1EA_96Yyh90tnw8HgXGkwSAyYwoLj6oxVGox67SHgV45nquZyfuGCk1NROQoSwmGFMTzpC0Vz8com6sf9BwiZLRzNANjF6Fi3HTP67Fnu4SnSHZY1y4RenDtp8hoHQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">- برای پیدا کردن سرور برای وصل شدن به تاپیک سرور برید
- برای راه اندازی سرور شخصی به تاپیک سرور شخصی برید
- برای آموزش و یادگیری اولین شروع با این ابزار به تاپیک اولین شروع برید
🫡
لینک گروه اصلی
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/whitedns/774" target="_blank">📅 07:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-773">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جمع‌بندی نهایی
تیم WhiteDNS تمام نشده، رها نشده و قرار نیست فقط به چند سرور عمومی محدود بماند.
برعکس، هدف ما این است که استفاده از WhiteDNS از حالت وابسته به سرورهای عمومی خارج شود.
کاربران می‌توانند با آموزش، سرور شخصی یا گروهی خودشان را راه‌اندازی کنند و اتصال پایدارتر و اختصاصی‌تری داشته باشند.
این روش برای اتصال حیاتی، شرایط سخت و دسترسی ضروری طراحی شده است؛ نه برای مصرف سنگین، دانلود زیاد یا انتظار سرعت VPNهای تجاری.
تیم WhiteDNS همچنان کنار شماست.
فقط قرار است از این به بعد، به‌جای اینکه فقط ماهی بدهیم، بیشتر ماهی‌گیری یاد بدهیم.</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/whitedns/773" target="_blank">📅 07:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-772">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">هدف اصلی WhiteDNS
هدف WhiteDNS کمک به دسترسی آزادتر به اینترنت در شرایط سخت و محدود است.
WhiteDNS یک پروژه غیرانتفاعی است و تمرکز ما روی ساخت ابزار، آموزش و کمک به کاربران برای داشتن راه‌های پایدارتر اتصال است.
ما همچنان مسیر توسعه اپلیکیشن، بهبود کیفیت، آموزش و نگهداری زیرساخت‌های فعلی را ادامه می‌دهیم.
اما می‌خواهیم کاربران کمتر به سرورهای عمومی وابسته باشند و بیشتر بتوانند اتصال اختصاصی خودشان را بسازند.</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/whitedns/772" target="_blank">📅 07:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-771">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آیا دانش فنی زیادی لازم است؟
برای راه‌اندازی اولیه کمی دقت لازم است، اما آموزش‌ها طوری آماده می‌شوند که کاربران معمولی هم بتوانند مرحله‌به‌مرحله انجام دهند.
اگر هیچ تجربه‌ای با سرور نداشته باشید، شروع کار ممکن است کمی سخت به نظر برسد.
اما بعد از یک بار راه‌اندازی، استفاده از آن بسیار ساده‌تر خواهد بود.
هدف ما این است که این مسیر را تا حد ممکن ساده‌تر، قابل فهم‌تر و قابل انجام‌تر کنیم.</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/whitedns/771" target="_blank">📅 07:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-770">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آموزش‌ها کجاست؟
ویدیوها و آموزش‌های مربوط به نسخه اندروید، نسخه دسکتاپ و راه‌اندازی سرور شخصی داخل کانال قرار داده شده‌اند.
لطفاً قبل از پرسیدن سوال، داخل کانال سرچ کنید.
برای پیدا کردن آموزش‌ها می‌توانید این عبارت‌ها را جستجو کنید:
آموزش
سرور شخصی
دسکتاپ
اندروید
StormDNS
MasterDNS
Resolver
آموزش‌ها مرحله‌به‌مرحله منتشر شده‌اند و با کمی جستجو قابل پیدا کردن هستند.
همچنین داخل گروه اصلی تاپیک اولین شروع همه چیز رو توضیح داده
https://t.me/whitedns_group/32380/38590</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/whitedns/770" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-769">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اگر سرور کند بود، مشکل از اپلیکیشن است؟
نه لزوماً.
کندی یا قطعی می‌تواند دلایل مختلفی داشته باشد:
- شلوغ شدن سرور عمومی
- ضعیف بودن Resolverها
- اختلال یا محدودیت سمت اینترنت ایران
- کیفیت پایین مسیر شبکه
- تنظیمات نامناسب
- استفاده تعداد زیادی کاربر از یک سرور مشترک
کیفیت نهایی اتصال به سرور، Resolverها و شرایط شبکه هم بستگی دارد.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/whitedns/769" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-768">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">چه انتظاری نباید داشته باشید؟
از WhiteDNS نباید انتظار سرعت بالا برای مصرف سنگین داشته باشید.
ممکن است شبکه‌های اجتماعی باز شوند، اما همیشه سرعت عالی نخواهد بود.
برای مواردی مثل این‌ها مناسب نیست:
- دانلود زیاد
- ویدیو با کیفیت بالا
- وب‌گردی سنگین
- استفاده هم‌زمان چندین اپلیکیشن پرمصرف
- انتظار سرعت شبیه VPNهای تجاری
این روش بیشتر برای دسترسی ضروری طراحی شده، نه مصرف سنگین روزمره.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/whitedns/768" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-767">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">این روش برای چه کاری مناسب است؟
WhiteDNS و روش‌های مبتنی بر MasterDNS/StormDNS بیشتر برای شرایط سخت، محدود، ناپایدار و اضطراری ساخته شده‌اند.
این روش برای مواردی مثل این‌ها مناسب‌تر است:
- اتصال حیاتی
- پیام‌رسان‌ها
- دسترسی ضروری
- شرایط محدودیت شدید اینترنت
- استفاده سبک و کنترل‌شده
این روش جایگزین کامل VPNهای پرسرعت تجاری برای مصرف سنگین نیست.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/whitedns/767" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-766">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">استفاده گروهی با دوستان و آشناها
یکی از بهترین روش‌ها این است که چند نفر با هم یک سرور تهیه کنند.
اگر دوست، خانواده یا آشنایی خارج از ایران دارید، می‌تواند برای تهیه یا راه‌اندازی سرور کمک کند.
بعد از راه‌اندازی، اطلاعات اتصال داخل WhiteDNS وارد می‌شود و همان سرور به‌صورت اختصاصی‌تر برای شما یا گروه کوچک‌تان قابل استفاده خواهد بود.
این روش معمولاً از استفاده از سرورهای عمومی شلوغ پایدارتر است.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/whitedns/766" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-765">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">هزینه تقریبی سرور شخصی
هزینه راه‌اندازی سرور شخصی معمولاً خیلی بالا نیست.
به‌صورت تقریبی:
شروع کار: حدود 7 دلار
هزینه ماهانه بعدی: حدود 6 دلار
البته ممکن است سرورهای ارزان‌تر هم پیدا کنید.
یک سرور حدوداً 6 دلاری معمولاً می‌تواند برای حدود 5 تا 10 کاربر سبک و معمولی کافی باشد.
اگر چند نفر با هم هزینه را تقسیم کنند، هزینه ماهانه برای هر نفر بسیار کمتر از اکثر سرویس‌های VPN خواهد شد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/whitedns/765" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-764">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مزیت سرور شخصی
راه‌اندازی سرور شخصی یا گروهی چند مزیت مهم دارد:
- فشار کاربران عمومی روی سرور شما نیست
- پایداری معمولاً بهتر است
- در بعضی شرایط سرعت بهتری می‌گیرید
- احتمال پیدا کردن Resolverهای مناسب بیشتر می‌شود
- کنترل کامل‌تری روی تنظیمات دارید
- هزینه آن معمولاً از خرید VPN کمتر است
- می‌توانید با دوستان یا خانواده به‌صورت گروهی استفاده کنید
ابزار WhiteDNS برای همین ساخته شده که فقط محدود به چند سرور عمومی نباشد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/whitedns/764" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-763">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">چرا سرور عمومی جدید منتشر نمی‌کنیم؟
وقتی یک سرور عمومی در کانالی با ده‌ها هزار کاربر منتشر می‌شود، خیلی سریع زیر فشار زیاد قرار می‌گیرد.
در نتیجه:
- سرعت کم می‌شود
- اتصال ناپایدار می‌شود
- سرور گاهی از دسترس خارج می‌شود
- کاربران فکر می‌کنند مشکل از اپلیکیشن است
در حالی که مشکل اصلی معمولاً فشار زیاد روی سرور، محدودیت‌های شبکه، یا وضعیت Resolverهاست.
طبیعتاً یک سرور عمومی نمی‌تواند هم‌زمان برای هزاران نفر مثل VPN اختصاصی کار کند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/whitedns/763" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-762">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وضعیت سرورهای فعلی
سرورهایی که تا امروز توسط تیم WhiteDNS ارائه شده‌اند، همچنان نگهداری می‌شوند و تا جایی که امکان داشته باشد فعال خواهند ماند.
اما از این به بعد برنامه‌ای برای انتشار مداوم سرورهای عمومی جدید از طرف تیم نداریم.
اگر سروری متعلق به خود تیم WhiteDNS باشد، فقط داخل تاپیک «سرورها» اطلاع‌رسانی خواهد شد.
تمرکز اصلی ما از این به بعد آموزش، مستندات و کمک به کاربران برای راه‌اندازی سرور شخصی یا گروهی است.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/whitedns/762" target="_blank">📅 07:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-761">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تمرکز جدید کانال
از این به بعد تمرکز اصلی ما بیشتر روی این موارد خواهد بود:
- آموزش استفاده بهتر از WhiteDNS
- آموزش راه‌اندازی سرور شخصی MasterDNS و StormDNS
- آموزش نسخه اندروید و دسکتاپ
- آموزش پیدا کردن و تست Resolverها
- معرفی تنظیمات بهتر
- رفع اشکال و راهنمایی کاربران
- بهبود اپلیکیشن و اطلاع‌رسانی نسخه‌های جدید
هدف ما این است که کاربران فقط مصرف‌کننده چند سرور عمومی نباشند.
نرم‌افزار های ما طوری طراحی شده که بتوانید از سرورهای خودتان، سرورهای دوستان‌تان، یا هر سرور سازگار با MasterDNS و StormDNS استفاده کنید و اتصال پایدارتر و اختصاصی‌تر بسازید.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/whitedns/761" target="_blank">📅 07:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-760">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سلام به همه همراهان WhiteDNS
از امروز رویکرد ما در WhiteDNS کمی تغییر می‌کند.
WhiteDNS از ابتدا برای استفاده با سرورهای MasterDNS ساخته شده و همچنین از فورک StormDNS هم پشتیبانی می‌کند.
یعنی استفاده از WhiteDNS فقط محدود به سرورهایی نیست که از طرف کانال معرفی می‌شوند.
هر سرور MasterDNS و همچنین سرورهای سازگار با StormDNS می‌توانند داخل اپلیکیشن WhiteDNS استفاده شوند.
تا امروز، در کنار توسعه اپلیکیشن، تعدادی سرور آماده هم در اختیار کاربران قرار دادیم تا شروع استفاده برای همه راحت‌تر باشد.
👇
اما در ادامه یک سوءبرداشت ایجاد شد:
بعضی از کاربران فکر می‌کنند اگر سرورهای معرفی‌شده شلوغ شوند، کند شوند یا موقتاً در دسترس نباشند، یعنی خود اپلیکیشن WhiteDNS مشکل دارد یا قابل استفاده نیست.
در حالی که WhiteDNS فقط یک اپلیکیشن وابسته به چند سرور عمومی نیست.
قدرت اصلی WhiteDNS این است که هر کاربر یا هر گروه کوچک می‌تواند سرور MasterDNS یا StormDNS خودش را راه‌اندازی کند و از همین اپلیکیشن برای اتصال استفاده کند.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/whitedns/760" target="_blank">📅 07:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-759">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">White DNS
pinned «
سرور جدید WhiteDNS   Domain: v.wdn.best Encryption Key: bad99364093861634030e96f11fe3132 Encryption: XOR @WhiteDNS
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/759" target="_blank">📅 07:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-758">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.wdn.best
Encryption Key:
bad99364093861634030e96f11fe3132
Encryption: XOR
@WhiteDNS</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/whitedns/758" target="_blank">📅 06:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-754">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/754" target="_blank">📅 16:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-753">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bI8HQ8f9hJLnKHW1umwAa9di0JBuWF6jCa6fzREWiQaKGGbidgIReN00thhVqF9C9whFGmUKegV4QVNjlCcZVpYPRvftFT2blkBrDujt7okWWpDIx7GpdcqGmJTj2VO5NCY5U8YgJXoQjBYL3Kx6Ya3ZnTnMsa8Sd7fMk2iyMnCU4Qn546K4S66wr8Fh4HlZ5O1iDmpIRlqp5GLB5ZiZQWYtlChF0jt31CUjeJGx6LvJJ7khVXWz2-nnrbc6cNM29W5WJS3wT1yBfImb9mhgNNhS05N6D4AFyU_M7EDjmEzyWUrhL-sRCj_TZk0cIRDTPe42uNQQHbdMm_MqEW5__A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل گروه اصلی تاپیکی ساختیم به اسم «اولین شروع» که یک توضیح کامل از وایت دی ان اس هستش + یک سری رکورد صدا که آموزش و نحوه استفاده کلی از اپلیکیشن رو آموزش میده.
لینک گروه
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/whitedns/753" target="_blank">📅 15:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-752">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompythash</strong></div>
<div class="tg-text">سرور ها آپدیت شدن
دقت کنید هم رمز و هم دامنه تغییر کردن
سرور StormDNS اختصاصی چنل Pythash/پای هش
StormDNS Server Configs
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 1
@pythash
Domain:
v1.pythash.tr
Key:
Telegram-Channel------->@pythash
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 2
@pythash
Domain:
v2.pythash.tr
Key:
Telegram-Channel------->@pythash
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
نحوه اتصال:
windows , android:
https://t.me/pythash/74
linux:
https://t.me/pythash/81
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🌀
@pythash
🌀
@pythash</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/whitedns/752" target="_blank">📅 15:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-751">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/whitedns/751" target="_blank">📅 14:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-749">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/749" target="_blank">📅 14:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-748">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/oTQT-qskcFTO1E2CbtiX_11Z3bIOUGie1PRyOiA-nsPQsAPn7E5lBNkYYf9eY8ZDTjjJBtcagFSzp9Ig85OoE84SDwtYU_U18HfdtvvBOJ90D5brlCna8xouZXrlZ6kzp8NnGav8-wTpIQQU-3k_3UnoELiP_SpCu2Ik9QTuaEEREPQu_B_HDgPMSu_ZE-uixXivYlZm0WT9fMN_TMfYVbJXeV4FJjj2L8pmSnXP9XWxZc8Pfuq2nTrEzrcjsi416yHooXoirCmesUa0URbDMdwZcb2j3tQf_yEmtoyv9cqUJY1N-1CHr2QR4Ko4Cx_WOQYWmRvvsLLvgYDEbHFACQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/whitedns/748" target="_blank">📅 14:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-747">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-poll">
<h4>📊 🌷نظرتون در مورد نسخه جدید Whitedns windows چی هست ؟👀⚠️</h4>
<ul>
<li>✓ عالی</li>
<li>✓ خوب</li>
<li>✓ متوسط</li>
<li>✓ بد</li>
</ul>
</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/whitedns/747" target="_blank">📅 13:53 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-745">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LlKBFpYr5Q0oo1fQNjyAs1Yopyf405CbyANvF4tXcKcdMWrw2EFT98tUjtFPn9xxwblX64vEWhd6TBSMpZ8N0a0JueBTSWuezaEa4Q7enG3zrrJqAy2-trvY6BLJ0Rob3cGO6vqPq6IxjGAZHcM3fRVbRfDGVbpxTCLi2V27hKiCTl8MGTqLPke6CMFWfOZ3L-wDZtDp5mIIed7gwlPWhrOfxF9akeoQH5hGE00ObZT0lnkBSA4p1PJtIhgxvPqBa_HfnRAiDIsN9uAs9a9GZQo9LGqIFgQ0YUOIan2F7AGwx1zDLV_IPYV4_yL8Z6_q0zXzHd6iubZrt_gvjYMr1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LzgPp7B_lh_kOemPjpYFNsc8s5paVC6JsvNDiLdwnW0E0m-WqErk6c584BYESWcBvUVk30u-H9L6a-H_JDChxyPsl8MFd9_12VE-g7-03uhg2QmVHME_Z1nWC8xGlhP19l3C9b3rXrkoBRQaj2KGm_ovTs82f-6JhiRSga3MYnE2k-yOJXluiEuXcNt-LKDr6r8hVV3_sP0_B3yq47Ar3KiATeLMZHdD_FUtHHRBhn3KOwW45I9qg5zzoGFWJS1jJcvGb839s7ACsREsbFBNkZoJ4dDtN-0nw0MpA93AhtDFHsSWQfMN_U8fe_caPvGPK9jdy-a-Zi0nwQJnhO8-nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♨️
نسخه 1.0.0 Beta 3 ویندوز WhiteDNS منتشر شد
♨️
سلام به همراهان عزیز WhiteDNS   نسخه جدید ویندوز منتشر شده و در این آپدیت تمرکز اصلی روی بهتر شدن تجربه کاربری، تست سریع‌تر تنظیمات، مدیریت راحت‌تر سرورها و ریزالورها و رفع مشکلات گزارش‌شده بوده است.
🔅
قابلیت‌های…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/whitedns/745" target="_blank">📅 11:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-744">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👇
👇
👇
👇
👇
👇
این گروه توسط جمعی از فعالین این حوزه مدیریت می‌شود و هدف، دسترسی مردم به اینترنت آزاد است.
چت کردن، صحبتی به غیر از دسترسی به اینترنت، تبلیغ، سؤال راجب فروشنده‌های VPN = مستقیم بن
گروه اصلی:‌
https://t.me/Ir_Blackout
گروه کانفیگ:
https://t.me/Ir_Blackout_Config</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/whitedns/744" target="_blank">📅 10:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-743">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">لینک های داخلی برای دانلود اپلیکیشن های دستکتاپ
⬇️
Windows
|
Linux
|
Mac
1
.0.0 Beta3
باتشکر از چنل
@masir_sefid</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/whitedns/743" target="_blank">📅 09:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-741">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta3-linux-arm64.deb</div>
  <div class="tg-doc-extra">15.5 MB</div>
</div>
<a href="https://t.me/whitedns/741" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/whitedns/741" target="_blank">📅 09:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-735">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta3-linux-amd64.deb</div>
  <div class="tg-doc-extra">17.9 MB</div>
</div>
<a href="https://t.me/whitedns/735" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/whitedns/735" target="_blank">📅 09:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-734">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_IlFqqs52HcTw-Iv0vI6bAoZsYzfWAcEmsnDNIqCwxx7yQFxr7c61hVrB-nMVZE8Ipo_nWbYtN77nAb94vJmxgJuPd0uvrKG4Zt7Z_si_r44I4Mop5N2HBJO9cfHnK0W1eN0LuWIHYYTbBGGoc_R3VCMDG2DBkJGGuqPF_cfVV6fp5xa2G9qeJGN2ZKDWDzlEBjK1c0REf-dV5wAr_u1HXPRaluHuMo2jzO0OTBh1C9jehJh3vTziGeZ_mMljsQC512Qd3kVVVTGanN5vxDUeYM36DBrgjFIGJ8rgQWNZakGw1J1TnBSO5b9zcpXp7-07B1o3c9Y78ioPMVA81_qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♨️
نسخه
1.0.0 Beta 3
ویندوز WhiteDNS منتشر شد
♨️
سلام به همراهان عزیز WhiteDNS
نسخه جدید ویندوز منتشر شده و در این آپدیت تمرکز اصلی روی بهتر شدن تجربه کاربری، تست سریع‌تر تنظیمات، مدیریت راحت‌تر سرورها و ریزالورها و رفع مشکلات گزارش‌شده بوده است.
🔅
قابلیت‌های جدید
✅
اضافه شدن قابلیت
Parallel Test
برای پیدا کردن بهترین تنظیمات اتصال
✅
اضافه شدن دکمه‌های جدید برای حذف لاگ، کپی لاگ، خروجی گرفتن از سرورها، ایمپورت DNS، خروجی گرفتن و ایمپورت تنظیمات
✅
امکان انتخاب نتایج اسکنر و ساخت پروفایل جدید بعد از اسکن
✅
امکان کپی همه نتایج اسکن، انتخاب دستی نتایج و کپی موارد انتخاب‌شده
✅
اضافه شدن قابلیت مرتب‌سازی تنظیمات، سرورها و ریزالورها
✅
نمایش IP ویندوز برای اشتراک‌گذاری اینترنت با موبایل و سایر دستگاه‌ها
✅
اضافه شدن قابلیت ریست تنظیمات برنامه
🔅
بروزرسانی‌ها و بهبودها
✅
بازطراحی و رفع مشکلات تب داشبورد
✅
اضافه شدن اسکرول در بخش‌های سرورها، ریزالورها و تنظیمات
✅
بهبودهای مختلف بر اساس گزارش‌های کاربران
لطفاً نسخه جدید را تست کنید و اگر مشکلی دیدید، همراه با لاگ و توضیح دقیق در بخش مربوطه گزارش دهید تا سریع‌تر بررسی شود.
ممنون از همراهی و گزارش‌های ارزشمند شما
🙏
@WhiteDNS</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/whitedns/734" target="_blank">📅 08:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-732">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta2-linux-amd64.deb</div>
  <div class="tg-doc-extra">17.8 MB</div>
</div>
<a href="https://t.me/whitedns/732" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
دوستان عزیز Linux, اپ دسکتاپ WhiteDNS Beta2 برای لینوکس هم آماده کردیم و میتونید دانلود کنید.
این نسخه بتا هستش  و ما در روز های آینده دایما با فیکس ها و فیچر های بیشتر آپدیت میدیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/whitedns/732" target="_blank">📅 17:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-731">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOj9dONvDw3IPlkb7PHyKbsCu9ZX1-sYsI1RJuuWeMGvnHqfOtC6Jw7fw4LvOS1Ke52zPpU6-rPTQmjlesBqwNw9aoLj2E0Dfv7OJPuHdQAcdS_8eQLii2-GuqCclaTz5mmfJ2-9irxSIlBxQyrNWc5jAdBAK_kMCoixMjsC8j0TcHAhDUIjOeRfcYiEN_CL6yWgHpjQ7mY-CzO4ZZMdu5ZpNC1R8KVK1RoyvvqCodvt4nCHhSQ2ZgoVjqrIcWWecC-1CO6rvguQPVZDYbaTsM3vp5gangwUrHAaL92qNguDaZhFEgjSyd-vnoYzKco4Jpop3mKrpFCJvjOcF2F3lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل گروه اصلی تاپیکی ساختیم به اسم «اولین شروع» که یک توضیح کامل از وایت دی ان اس هستش + یک سری رکورد صدا که آموزش و نحوه استفاده کلی از اپلیکیشن رو آموزش میده.
لینک گروه
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/whitedns/731" target="_blank">📅 17:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-730">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">لیست ۱۰۰ ریزالور موقفی که در ۲۴ ساعت گذشته به سرور های WhiteDNS وصل شدن
80.75.7.2
31.214.169.244
185.208.183.29
62.60.144.87
93.115.127.9
5.160.128.142
109.230.89.90
185.142.158.162
134.255.206.205
185.53.142.174
94.232.173.28
185.88.178.196
2.188.21.58
46.245.80.82
62.60.144.85
185.255.91.60
185.109.61.27
2.188.21.70
74.63.24.210
185.208.174.167
185.141.105.139
185.51.201.58
217.66.203.211
2.188.21.46
85.185.157.181
5.202.252.30
172.64.32.0
173.245.58.0
93.118.127.118
108.162.192.0
78.39.234.140
178.252.128.66
158.58.184.147
37.191.95.70
164.138.17.122
185.50.37.52
46.32.31.30
185.53.141.230
92.246.87.191
93.118.109.213
5.160.140.16
2.188.21.146
2.188.21.138
2.188.21.62
5.160.227.78
5.160.2.55
5.160.137.130
109.72.197.1
74.80.77.246
80.210.40.53
74.80.77.247
80.210.40.50
207.211.215.145
185.191.79.210
74.80.77.244
81.16.121.151
78.157.41.60
217.218.59.18
45.135.241.33
194.61.120.143
74.80.77.245
217.219.76.102
85.185.1.10
185.129.170.75
46.209.44.74
43.226.5.169
87.107.9.233
79.175.172.101
2.188.21.78
172.253.228.147
185.213.11.85
@WhiteDNS</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/whitedns/730" target="_blank">📅 16:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-729">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سلام عزیزان، امیدوارم در این اوضاعِ به شدت خراب و زندگی در کشوری که توسط یک رژیم فاسد اداره میشه همچنان قویی باشید و حال دلتون عالی باشه. همونطور که میدونید ما
به شدت
با پروسه‌ی فروش
مخالف
بوده ایم و تمام فعالیت های ما برای
تمام
مردم ایران به صورت
کاملا
رایگان
بوده؛ اما جا داره که از تمام کسانی که چه با کریپتو و چه با استارز زدن به پست ها از ما حمایت میکنند تا فعالیت چنل و سرورها مداوم باشه، تشکر کنم. در این مدت دقت کردم که تمامی پست های چنل حداقل یک استارز خورده و بدونید که تمام این حمایت ها حتی یک استارزی که میزنید برای ما خیلی با ارزشه و از شما قدردانی میکنیم که در این راه دشوار و مبارزه با این حکومت خون‌خوار در کنار ما ایستاده اید!
❤️
- کوچیک شما Patrick.
WhiteDNS-Team
@WhiteDNS</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/whitedns/729" target="_blank">📅 14:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-728">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">لینک داخلی تمام پلتفرم های برنامه‌ی WhiteDNS Desktop:
Macos-amd64:
https://guardts.ir/f/736498ddfb14
Macos-arm64:
https://guardts.ir/f/4594c5008167
Windows-x64(amd64):
https://guardts.ir/f/2549b69980b3
Windows-arm64:
https://guardts.ir/f/05e3847a8a43
@WhiteDNS</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/whitedns/728" target="_blank">📅 13:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-727">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فیلم آموزش استفاده از نسخه WhiteDNS Desktop</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/whitedns/727" target="_blank">📅 13:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-726">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فیلم آموزش استفاده از نسخه WhiteDNS Desktop</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/whitedns/726" target="_blank">📅 11:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-725">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XISVdfcGOiivYkfNuNmroQVkZHPDx4aQ_1AM9_vwBHpvIxogYEcqAxwBPcE3qPBBb-1PZPtpuPbilqCCeYCDS8kU4S64CJYEbJzmDNO4cbXMwzVMqJLJ5wYbtnou1grpy2k2KSWn8gnhfEGUAG_UHVcYPMDvsr7GhxVXpR1NzfQwQW-mnt0WD8jeDeppczddGyQJwSGcH7MqLUmIWjwB3IbvVBdS7NJCEfpwmkOoeD-EE7nN1TUDTQ1WEeunC_4OEcu0LlXROKqPaeHFtMJlG5irVtvtN21q7u183SzZkXYdPaoltqT8rvqtMsTYIIO3i3LGvqEpKM-Sopc9d84HPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی مک، دوستانی که مشکل باز کردن اپ رو دارید، دستور زیر رو اجرا کنید
chmod +x "/Applications/WhiteDNS Desktop.app/Contents/MacOS/WhiteDNS Desktop"
xattr -dr com.apple.quarantine "/Applications/WhiteDNS Desktop.app"
open "/Applications/WhiteDNS Desktop.app"</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/whitedns/725" target="_blank">📅 11:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-721">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta2-macos-amd64.zip</div>
  <div class="tg-doc-extra">25.8 MB</div>
</div>
<a href="https://t.me/whitedns/721" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه WhiteDNS Desktop V1.0.0-beta2
✅
حل مشکل باز کردن در ورژن های قدیمی مک
✅
حل مشکل وصل نشدن و خطا بعد از ۴۵ ثانیه
✅
حل مشکل وارد کردن کانفیگ به صورت گروهی
✅
حل اضافه شدن دگه ذخیره برای ریزالور های سالم و. فعال به صورت جداگانه
✅
حل مشکل مشکی شدن صفحه در ویندوز
✅
اضافه شدن نسخه های لینوکس</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/whitedns/721" target="_blank">📅 10:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-717">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">macos-amd64.zip</div>
  <div class="tg-doc-extra">25.8 MB</div>
</div>
<a href="https://t.me/whitedns/717" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎉
WhiteDNS Desktop منتشر شد</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/whitedns/717" target="_blank">📅 08:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-716">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5WgQ35FotvjRjba__KW1CSnPym-cH2ckngu_zR-1rcRdudqDcrCdxhGccSOZz_GxQ7jBWGshpDG94dCyirdjAErHwdcn-LDlDaEj_bOrrgrDn9stW-0YJSnaljlQ2Di1iAd7fR5jYi5i3rN8idahKXjINOjXoktvO_Mq1RijC7bGsZoB-t7MHW8XBrLHjd0yLESoAGcd0933COsLxCHEOd5XBskfl92a82EWhPPzCH08ANxb6KMEARpf-1nUKd2hRjPGnvWdE2M5PO4ogHMIpsUOL85CJLBWS8Zjtk9q_ObPiEelqfXYEC8iqjpVL8MRgKupUTu2iCRd1zkb36J6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
WhiteDNS Desktop منتشر شد
نسخه دسکتاپ WhiteDNS حالا آماده استفاده است.
این برنامه برای کسانی ساخته شده که می‌خواهند اتصال‌های MasterDNS و StormDNS را روی کامپیوتر، ساده‌تر، سریع‌تر و بدون درگیر شدن با ترمینال و فایل‌های تنظیمات اجرا کنند.
با WhiteDNS Desktop می‌توانید پروفایل اتصال را وارد کنید، Resolverها را مدیریت کنید، اتصال را فقط با یک دکمه روشن یا خاموش کنید و وضعیت همه‌چیز را به‌صورت زنده ببینید.
✨
امکانات اصلی
✅
اتصال و قطع اتصال فقط با یک دکمه
✅
رابط گرافیکی ساده برای Windows و macOS
✅
پراکسی محلی آماده برای مرورگرها و برنامه‌های دیگر
✅
پشتیبانی از SOCKS و HTTP از طریق sing-box
✅
امکان فعال کردن System Proxy
✅
وارد کردن پروفایل‌های آماده با لینک‌های
stormdns://
✅
ساخت و مدیریت چند پروفایل اتصال
✅
ساخت و مدیریت چند لیست Resolver
✅
بررسی خودکار معتبر بودن Resolverها
✅
نمایش Resolverهای فعال، آماده‌باش و ردشده
✅
نمایش سرعت دانلود، سرعت آپلود و مصرف کل داده
✅
نمایش روند اتصال و درصد پیشرفت هنگام راه‌اندازی
✅
امکان توقف و ادامه دادن تست MTU هنگام اتصال
✅
خروجی گرفتن از تنظیمات به‌صورت
client_config.toml
✅
بخش لاگ و جست‌وجوی لاگ‌ها برای عیب‌یابی راحت‌تر
⚙️
تنظیمات پیشرفته برای شبکه‌های ضعیف و ناپایدار
برای کاربرانی که روی اینترنت‌های محدود، ضعیف یا ناپایدار هستند، تنظیمات پیشرفته هم داخل برنامه قرار داده شده است:
✅
انتخاب روش بالانس بین Resolverها
✅
تنظیم Packet Duplication برای پایداری بیشتر
✅
تنظیم فشرده‌سازی آپلود و دانلود
✅
تنظیم MTU، Timeout، Retry و تعداد تست هم‌زمان
✅
کنترل Workerها، Streamها و صف‌ها برای سیستم‌های مختلف
✅
وجود Watchdog برای بررسی زنده بودن اتصال
🔍
ابزار Scanner داخلی
در این نسخه، یک ابزار Scanner هم داخل برنامه اضافه شده است تا تست و بررسی Endpointها راحت‌تر شود:
✅
تست سریع یک Host با چند پورت
✅
اسکن گروهی از فایل‌های TXT، CSV یا JSON
✅
تست پروتکل‌های TCP، TLS، HTTP، WebSocket، UDP، QUIC/H3 و DNS
✅
نمایش Score، Grade، Latency، Jitter، Packet Loss و Stability
✅
بررسی اینکه Endpoint برای Tunnel آماده هست یا نه
✅
امکان دیدن و کپی کردن نتیجه کامل به‌صورت JSON
این نسخه برای کاربران عادی طراحی شده تا اتصال راحت‌تر و بدون دردسر انجام شود؛ اما برای کاربران حرفه‌ای هم تنظیمات دقیق‌تر در دسترس است تا بتوانند اتصال را با شرایط شبکه خودشان بهتر هماهنگ کنند.
⚠️
توجه: این نسخه هنوز بتا است.
اگر مشکلی مشاهده کردید، ارسال گزارش خطا، لاگ برنامه و توضیح شرایط شبکه شما کمک زیادی به بهتر شدن نسخه‌های بعدی می‌کند.
ممنون از همراهی شما با WhiteDNS
🤍</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/whitedns/716" target="_blank">📅 08:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-715">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ah91t7g92XjBQsD5yLe5WCVsASzcMd4bhAazS7BwX4EohDOCznT5l4sdA-RJkJxwGlLoKHrshAKqw8aCkqyEWBcyfJWoaxx9L1uXlBouqyv86sl8w4BoFPZtQa21Qo0ztOUylN7S2QlmU9MMiVxXENhprX0Ux-3_YS8FwwKwP--TUJYHtuJiLBCz6jtzOX6z37QrDRUyDse4DwvKdEfPXvrrVpssQOb5B3kBN-324G5pmhWi1OjuXt9pJxAY3belndnle696T0wOBFYC1GosAVcN2lYtLvcHIMy-FHefAMWgpW0-A9Nb53GT_rxd45fQtfiWiCRqPEbD5U4rkbqQZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همراهان عزیز،
بعد از بازخود هایی که ما از ورژن قبلی اپ ویندوز گرفتیم، تصمیم به بازنویسی این نرم‌افزار برای سیتم عامل های
مک ، ویندوز و لینوکس
گرفتیم.
تقریبا تمام امکانات اپلیکیشن اندروید در این اپ خلاصه شده اما با قدرت و منابع بیشتر.
سعی میکنیم هرچه زودتر اپ رو آماده و در اختیارتون قرار بدیم.
با تشکر
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/whitedns/715" target="_blank">📅 07:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-714">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2Ray Proxies with Khosrow</strong></div>
<div class="tg-text">خب این هم آموزش SNI Spoof برای مک.
فرآیندش برای ویندوز و لینوکس کاملاً مشابه هم هستش. فقط باید فایل اجرایی‌ای که برای sni spoof هستش رو مطابق سیستم‌عاملتون دانلود کنین.
فرقی هم نداره که از چه برنامه‌ای برای کانفیگ‌ها استفاده کنین.
لینک دانلود برنامه SNI Spoof برای مک و لینوکس
برنامه آپلود شده در تلگرام
لیست کانفیگای جمع آوری شده توسط متین عزیز.
کانفیگ JSON
لینک دانلود ویدئو بالا برای اینترنت ایران.
@khosrow_v2ray</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/whitedns/714" target="_blank">📅 02:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-713">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrfTHX7Ej9Ty9YIp2KRp-UCfAzLN-1IG_9X4zndZjY-DPARNJiZXrf5ydQi_6fzntRQ0UXBqiJwpbyJ4ymcES2whiT8w_qW91ETa2Nity-HToUbDEUE8vSph7T8xDNbTUjH1_RTBRJyFVGPbEHjfCNHbi3w3_QR0zpO7rzT1DiL8Fy3YpAOiz95o4pcrZPcnbQUD-c9C8hUTYlSbVrJWvU8n7bKr79E2UYj4cE5Tc-JUOsRD5zvVKFtnfbTXlwMsA4JwXpsamHbPrrfw5jzdwFaNtV7tWkU4GGNASP09gKNeKYNUs09tIBuNyZU2Vr7FB9Ty8xyFR_Lb9a08pl1PkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد میکنم تنظیمات موازی سازی MTU رو بین ۵۰ تا ۳۰۰ بسته به جدید قدرت گوشی همراهتون بذارید.</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/whitedns/713" target="_blank">📅 18:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-708">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/whitedns/708" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/whitedns/708" target="_blank">📅 18:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-707">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuWANTEi4sVg2GMuLJa8CT6ux--8hsWLe_X8l72Cx1m3UfTFZjsvhSy48FbctfaiVjRPZgm6puQDOriwn44ZlYMZiMqlzIAC-mLIK6RwMklDDIsfypLgnfqHnyGlGjVYUfxY5ysl6vazA1nCD8yWFwupr_Fyraj1eGCLtTTHVIP4Wb8l4sxU335502WFMlkqMTjf9YldGSN2XNW1xRaoi78tjpyrrBhkKr27ZRsnhvDCFMMM2xZ1PUrtvE2CMu49T0M7_seXS4RQg4qAgb9K2u_6nh1gw380sE8nNokTQrEyHumQA3XS8QI18HR05y2J8sO3_wu68AbB4vgEpc67_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همراهان عزیز
تغییر بزرگی در این ورژن انجام نشده. تمرکز در این نسخه روی
بهبود  تست موازی تنظیمات بوده. در این نسخه تنطیمات بیشتری و بهینه تری به این قابلیت اضافه شده.
✅
نسخه اپلیکیشن به 1.5.1 ارتقا پیدا کرده
✅
جدا شدن تنظیمات پر مصرف و بهینه در تست موازی.
✅
بعد از یک همه پرسی در کانال، حالا تنظیمات در ۱۰ دسته متفاوت تقسیم شده تا بهینه ترین تنظیمات بر اساس ریزالور های انتخاب شده برای شما استافده شود.
@WhiteDNS</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/whitedns/707" target="_blank">📅 18:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-705">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">برای باز کردن اینستاگرام در مرورگر گوشی (بدون اینکه وارد اپلیکیشن شوید)، می‌توانید این مراحل را دنبال کنید:
📱
💻
۱.
مرورگر خود را باز کنید:
🌐
وارد مرورگر گوشی خود (مثل Chrome در اندروید، Safari در آیفون، یا Firefox) شوید.
۲.
به سایت اینستاگرام بروید:
📍
در نوار آدرس بالای صفحه،
[www.instagram.com](https://www.instagram.com)
را تایپ کرده و جستجو کنید.
۳.
وارد حساب کاربری خود شوید (Log In):
🔐
در صفحه باز شده، روی گزینه
Log In
ضربه بزنید و نام کاربری (یا ایمیل/شماره موبایل) و رمز عبور خود را وارد کنید.
نکته مهم (جلوگیری از باز شدن خودکار اپلیکیشن):
⚠️
بسیاری از اوقات، وقتی آدرس اینستاگرام را در مرورگر وارد می‌کنید، گوشی به طور خودکار شما را به اپلیکیشن اینستاگرام (اگر نصب باشد) هدایت می‌کند. برای جلوگیری از این اتفاق، می‌توانید از ترفندهای زیر استفاده کنید:
راه حل اول (سریع‌ترین راه):
🚀
مرورگر خود را در حالت
ناشناس (Incognito یا Private)
باز کنید و سپس سایت اینستاگرام را در آن وارد کنید. در این حالت، لینک‌ها به اپلیکیشن منتقل نمی‌شوند.
راه حل دوم (تغییر تنظیمات در اندروید):
🤖
به تنظیمات گوشی (Settings) بروید.
بخش برنامه‌ها (Apps) را باز کنید و Instagram را پیدا کنید.
به بخش
Open by default
(باز شدن به‌طور پیش‌فرض) یا
Set as default
بروید.
گزینه باز کردن لینک‌های پشتیبانی‌شده (Open supported links) را خاموش کنید یا روی حالت "همیشه بپرس" (Ask every time) قرار دهید.
راه حل سوم (در سافاری آیفون):
🍎
در گوگل کلمه Instagram را جستجو کنید. روی لینک سایت اینستاگرام در نتایج جستجو
انگشت خود را نگه دارید
(Long press) و از منوی باز شده گزینه
Open in New Tab
را انتخاب کنید.
@whitedns
📡</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/whitedns/705" target="_blank">📅 07:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-704">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">WhiteDns-Windows-Setup.exe</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/whitedns/704" target="_blank">📅 07:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-703">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">11 MB</div>
</div>
<a href="https://t.me/whitedns/703" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">WhiteDns Windows 1.0.6
🖥
🔌
راهنمای اتصال هوشمند (Smart Connect)
🤖
قابلیت اتصال هوشمند به برنامه WhiteDns کمک می‌کند تا بهترین تنظیمات اتصال را به‌طور خودکار انتخاب کند. کاربران عادی نیازی به تغییر دستی تنظیماتی مانند MTU، Workers (تعداد پردازش‌گرها)، Packet Duplication (تکثیر بسته‌ها)، فشرده‌سازی (Compression) یا سایر تنظیمات در بخش پیشرفته (Advanced) ندارند.
✅
نحوه استفاده
📝
۱. برنامه
WhiteDns Windows
را باز کنید.
🪟
۲. به تب
Connect
(اتصال) بروید.
🔗
۳. مطمئن شوید که گزینه
Smart Connect
روی حالت روشن (
On
) قرار دارد.
🟢
۴. هدف اتصال خود را انتخاب کنید:
Stable (پایدار)
🛡
بهترین گزینه برای شبکه‌های ضعیف یا فیلترشده. این امن‌ترین و مطمئن‌ترین گزینه است.
Balanced (متعادل)
⚖️
برای اکثر کاربران توصیه می‌شود. این حالت تلاش می‌کند ضمن حفظ پایداری اتصال، سرعت خوبی نیز ارائه دهد.
Fast (سریع)
🚀
بهترین حالت برای زمانی که شبکه شما از قبل قوی است. ممکن است در این حالت از تنظیمات تهاجمی‌تری استفاده شود.
۵. موتور (Engine) را انتخاب کنید:
⚙️
MasterDNS
برای اکثر کاربران و اتصالات پایدار توصیه می‌شود.
StormDNS
در صورتی از این گزینه استفاده کنید که پروفایل/سرور شما برای StormDNS ساخته شده است یا می‌خواهید موتور سریع‌تر را آزمایش کنید.
⛈
۶. حالت پروکسی را انتخاب کنید:
🌐
System proxy (پروکسی سیستم)
برای وب‌گردی معمولی توصیه می‌شود. مرورگرها و بسیاری از برنامه‌های ویندوز به‌طور خودکار از WhiteDns استفاده خواهند کرد.
🖥
SOCKS5 only (فقط SOCKS5)
اگر می‌خواهید پروکسی را به‌صورت دستی در برنامه‌هایی مانند تلگرام تنظیم کنید، از این گزینه استفاده کنید.
📱
۷. روی
Connect
کلیک کنید.
👆
چه اتفاقاتی به‌طور خودکار رخ می‌دهد؟
🔄
وقتی اتصال هوشمند (Smart Connect) روشن است، WhiteDns کارهای زیر را انجام می‌دهد:
- استفاده از موتور انتخاب‌شده (MasterDNS یا StormDNS).
🛠
- بررسی تنظیمات موفق که در دفعات قبل جواب داده‌اند.
✔️
- انتخاب یک پیش‌تنظیم (Preset) مناسب بر اساس هدف شما.
🎯
- استفاده از بهترین تنظیمات شناخته‌شده برای تحلیلگر (Resolver).
📊
- امتحان کردن تنظیمات جایگزین امن‌تر (Fallback) در صورتی که تلاش اول ضعیف باشد.
🛡
- به خاطر سپردن تنظیمات موفق برای استفاده در دفعات بعدی.
💾
کدام هدف (Goal) را باید انتخاب کنم؟
🤔
ابتدا از
Balanced
استفاده کنید. این بهترین حالت پیش‌فرض برای اکثر کاربران است.
✅
در شرایط زیر از
Stable
استفاده کنید:
- اتصال مرتباً با شکست مواجه می‌شود.
❌
- اینترنت شما به شدت فیلتر است.
🚫
- تونل وصل می‌شود اما اتصال به سرعت قطع می‌گردد.
- سرعت برایتان نسبت به پایداری و اطمینان در درجه دوم اهمیت قرار دارد.
در شرایط زیر از
Fast
استفاده کنید:
- حالت Balanced در حال حاضر به خوبی کار می‌کند.
- سرعت بیشتری می‌خواهید.
⚡️
- شبکه یا سرور شما قوی است.
💪
تنظیمات پیشنهادی برای کاربران عادی
👥
اتصال هوشمند (Smart Connect):
On (روشن)
🟢
هدف (Goal):
Balanced
⚖️
موتور (Engine):
MasterDNS
🛠
پروکسی:
System proxy
🌐
سپس روی
Connect
کلیک کنید.
👆
اگر متصل نشد چه کار کنیم؟
🛠
این مراحل را به ترتیب امتحان کنید:
۱. هدف را به
Stable
تغییر دهید.
🛡
۲. گزینه Smart Connect را همچنان
On (روشن)
🟢
نگه دارید.
۳. دوباره روی
Connect
کلیک کنید.
۴. اگر باز هم متصل نشد، به بخش
Resolvers
بروید و یک اسکن اجرا کنید.
🔍
۵. بهترین نتایج Resolver را اعمال (Apply) کنید و سپس دوباره سعی کنید متصل شوید.
✅
برای کاربران تلگرام
💬
اگر از گزینه
SOCKS5 only
استفاده می‌کنید، پروکسی تلگرام دسکتاپ را به این شکل تنظیم کنید:
نوع (Type): SOCKS5
هاست (Host):
127.0.0.1
پورت (Port): 18000
نام کاربری/رمز عبور (Username/Password): خالی بگذارید
🔓
اگر از
System proxy
استفاده می‌کنید، مرورگرها معمولاً به‌طور خودکار متصل می‌شوند، اما تلگرام ممکن است همچنان به وارد کردن تنظیمات دستی SOCKS5 نیاز داشته باشد.
برای کاربران حرفه‌ای
🎓
اگر گزینه اتصال هوشمند را خاموش (
Off
) کنید، WhiteDns از پروفایل فعلی و تنظیمات پیشرفته‌ی (Advanced) شما دقیقاً همان‌طور که هستند استفاده خواهد کرد. این ویژگی برای زمانی که می‌خواهید کنترل کامل و دستی روی تنظیمات داشته باشید بسیار مفید است.
🔧
🚫
خیلی مهم :
به هیچ عنوان هیچ نرم افزار vpn دیگری مثل v2ray و یا ..... نباید روی سیستم شما باز باشد . مطمن شوید که حتی در پس زمینه هم بسته شوند
🚫
برای تست روی مرورگر ها حتما از گزینه New Private window یا New incognito window استفاده کنید
👍
@whitedns</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/whitedns/703" target="_blank">📅 07:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-702">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/GhW5e-46fesTzZxsSspav7hUS1ojoH7MKNwIGHNYfTD1Ps0wljNC8mya5-_7WQLxw9XGJMvg8dk0A6FbP2xVoujxmXozIgV9I9xuCO9-9MhDO9MScJJlpZ-ql7EB9RNa6DmSq6aUepexHcFdNYK4DKAgHyArHuGEOpAYWWDqvLefYi06WK73V23gECnl1EX8v3Wj3Snc8OAlgFAm3QoYu2qTUEf8jdlwPBoO_W1P1jogUuBTlk69iPrkg_bWalR7NhNNiNaKLyOK3iQYv7EzrFafIjiMRIZhHs4P7TyzSRTB-xxq6Huwl7WOpGIgssr5j5r1nFrHWM7PcSW2yIrYDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در نسخه ۱.۰.۶ -
WhiteDns Windows
🪟
قابلیت
«اتصال هوشمند» (Smart Connect)
اضافه شده است؛ یک حالت اتصال خودکار جدید که به کاربران کمک می‌کند بدون نیاز به تغییر دستی تنظیمات در تب پیشرفته (Advanced)، به تنظیماتی پایدار و مطمئن دست پیدا کنند.
🚀
اکنون قابلیت اتصال هوشمند می‌تواند اتصال را بر اساس موتور (Engine) انتخاب‌شده، سرور، کیفیت تحلیلگر (Resolver) و نتایج موفق قبلی تنظیم و بهینه‌سازی کند.
⚙️
کاربران می‌توانند یک هدف ساده را انتخاب کنند:
پایدار (Stable)
🛡
متعادل (Balanced)
⚖️
سریع (Fast)
⚡️
. سپس برنامه پیش از برقراری ارتباط، به‌طور خودکار تنظیمات انتقال و تحلیلگر امن‌تری را برای MasterDNS یا StormDNS انتخاب می‌کند.
همچنین این نسخه نتایج موفق اتصال هوشمند را به تفکیک هر سرور، موتور و شبکه به خاطر می‌سپارد؛ در نتیجه اتصالات بعدی می‌توانند با استفاده از تنظیماتی که پیش‌تر جواب داده‌اند، سریع‌تر برقرار شوند.
🧠
اگر مسیر اتصال ضعیف باشد، قابلیت اتصال هوشمند پیش از نمایش پیام خطا، تنظیمات جایگزین امن‌تری (Fallback) را امتحان می‌کند.
🔄
صفحه اتصال (Connect) با یک پنل کنترل جدیدِ اتصال هوشمند به‌روزرسانی شده است، در حالی که امکان اتصال دستی معمولی همچنان برای کاربران حرفه‌ای در دسترس قرار دارد.
🛠
@whitedns</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/whitedns/702" target="_blank">📅 07:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-701">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-poll">
<h4>📊 با اپلیکیشن های ما تونستید به اینترنت متصل بشید؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/whitedns/701" target="_blank">📅 05:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-700">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
پروفایل های وایت دی ان اس (WhiteDNS)
❤️
تاریخ بروزرسانی : ۲۸ اردیبهشت
👾
لینک دانلود
کلاینت :
1️⃣
WhiteDNS
1.5.0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jygxKSIsInNlcnZlciI6eyJkb21haW4iOiJ2MS5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jygyKSIsInNlcnZlciI6eyJkb21haW4iOiJ2Mi5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jygzKSIsInNlcnZlciI6eyJkb21haW4iOiJ2My5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg0KSIsInNlcnZlciI6eyJkb21haW4iOiJ2NC5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg1KSIsInNlcnZlciI6eyJkb21haW4iOiJ2NS5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg2KSIsInNlcnZlciI6eyJkb21haW4iOiJ2Ni5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg3KSIsInNlcnZlciI6eyJkb21haW4iOiJ2Ny5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg4KSIsInNlcnZlciI6eyJkb21haW4iOiJ2OC5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jyg5KSIsInNlcnZlciI6eyJkb21haW4iOiJ2OS5tYXNpci1zZWZpZC5teSIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViuKtkO-4jygxMCkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEwLm1hc2lyLXNlZmlkLm15IiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
⚡️
پک ریزالور
👍
تنظیمات مخصوص وایت دی ان اس
⬅️
نحوه ی اضافه کردن پروفایل ها
⬅️
فیلم اموزش وایت دی ان اس
👌
آموزش ترکیب با برنامه ی نکوباکس
👍
آموزش ترکیب با برنامه npv
(پیشنهادی)
✉️
Channel |
@Masir_Sefid
| کانال
✉️</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/whitedns/700" target="_blank">📅 20:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-699">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/whitedns/699" target="_blank">📅 18:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-698">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">راهنمای_جامع_استفاده_از_وایت_دی_ان_اس_ویندوز_.docx</div>
  <div class="tg-doc-extra">2.9 MB</div>
</div>
<a href="https://t.me/whitedns/698" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
راهنمای جامع وایت دی‌ان‌اس (WhiteDns) برای ویندوز منتشر شد!
🚀
کاربران عزیز، اگر برای اتصال و تنظیم برنامه WhiteDns در ویندوز با چالشی مواجه هستید، این راهنمای کامل دقیقا برای شما آماده شده است. برنامه WhiteDns یک ابزار قدرتمند دسکتاپ برای تونلینگ و ساخت پروکسی محلی است و با استفاده از این راهنما می‌توانید بالاترین سرعت و پایداری را تجربه کنید.
📌
خلاصه‌ای از آنچه در این راهنما یاد می‌گیرید:
🔹
شروع سریع و آسان:
آموزش قدم‌به‌قدم ایجاد پروفایل، وارد کردن دامنه، کلید رمزنگاری (Encryption Key) و اتصال اولیه.
🔹
انتخاب حالت پروکسی:
تفاوت بین حالت دستی (SOCKS5 only) و اعمال پروکسی روی کل سیستم (System proxy) برای مرورگرها.
🔹
ابزار قدرتمند اسکنر (Resolvers):
آموزش پیدا کردن سریع‌ترین و پایدارترین تحلیلگرهای DNS با استفاده از اسکنر داخلی برنامه (در حالت‌های سریع، عمیق و با دقت بالا).
🔹
تنظیمات پیشرفته و موتورها:
معرفی تفاوت‌های موتور MasterDNS و StormDNS و نحوه استفاده از پروفایل‌های آماده (Presets) مانند
Stable Iran
(برای بالاترین پایداری در شبکه‌های محدود) تا حالت‌های تهاجمی‌تر (Aggressive).
🔹
تنظیمات مخصوص برنامه‌ها:
راهنمای دقیق ست کردن پروکسی محلی (
127.0.0.1:18000
) روی تلگرام دسکتاپ، فایرفاکس، کروم و مرورگر اج.
🔹
رفع مشکلات (Troubleshooting):
راهکارهای عملی برای حل مشکلاتی مثل وصل نشدن مرورگر با وجود اتصال برنامه، قطع شدن مداوم، و یا رفع گیر کردن روی راه‌اندازی کند تونل.
💡
فرمول طلایی اتصال:
بهترین و امن‌ترین مسیر برای اکثر کاربران این است: وارد کردن اطلاعات تونل
⬅️
اسکن تحلیلگرها
⬅️
اعمال بهترین تحلیلگر
⬅️
انتخاب حالت Stable Iran
⬅️
اتصال!
برای استفاده حرفه‌ای از این نرم‌افزار و دور زدن قطعی‌ها، حتماً فایل راهنمای کامل را مطالعه کنید.
#اموزش_ویندوز_whitedns
@whitedns</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/whitedns/698" target="_blank">📅 18:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-697">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">11 MB</div>
</div>
<a href="https://t.me/whitedns/697" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تغییرات WhiteDns ویندوز نسخه 1.0.5
بازسازی رابط مدرن
بهبود جزئیات کوچک رابط کاربری و تراز کارت‌ها برای ظاهری تمیزتر و یکدست‌تر در دسکتاپ.
🖥
✨
اسکنر با دقت بالا :
یک اسکنر با دقت بالا برای شرایط سخت اضافه شد
طراحی شمارنده رزولور بهبود یافته
به‌روزرسانی استایل شمارنده رزولور تا با چیدمان کارت‌های اطراف هماهنگ‌تر شده و ظاهری مدرن‌تر داشته باشد.
🎨
پشتیبانی از سینی ویندوز بهبود یافته
رفتار سینی برنامه به‌روزرسانی شد تا در ویندوز طبیعی‌تر احساس شود و در پس‌زمینه در دسترس بماند.
🪟
🔌
فعالیت شبکه برای حالت SOCKS5 اصلاح شد
فعالیت شبکه اکنون ترافیک را زمانی که برنامه‌ها از پروکسی محلی SOCKS5 استفاده می‌کنند، ردیابی می‌کند، به جای نمایش فعالیت فقط از طریق مسیر HTTP/System Proxy.
🌐
🔍
سازگاری پورت SOCKS سفارشی
فعالیت شبکه اکنون هنگام تغییر پورت SOCKS در تب پیشرفته نیز به کار خود ادامه می‌دهد.
⚙️
حافظه اسکن رزولور اضافه شد
برنامه اکنون بهترین نتیجه اسکن رزولور را به خاطر می‌سپارد و اسکن‌های کامل تکراری را هنگام اتصال مجدد با مجموعه رزولور یکسان کاهش می‌دهد.
💾
🚀
تجربه اتصال مجدد سریع‌تر
اتصالات مجدد باید روان‌تر احساس شوند زیرا برنامه از اسکن مجدد غیرضروری رزولورها هنگام در دسترس بودن نتیجه معتبر قبلی خودداری می‌کند.
⚡️
وارد کردن دستی رزولور اضافه شد
گزینه وارد کردن .txt در کارت «وارد کردن / رزولورهای دستی» برای بارگذاری آسان‌تر لیست رزولورها اضافه شد.
📥
📝
نکات اتصال
از لیست رزولور باکیفیت و کوچک‌تر برای راه‌اندازی سریع‌تر استفاده کنید.
🚀
رزولورهای پایدارتر را در بالای لیست نگه دارید.
📌
هنگام آزمایش اتصال، ابتدا از حالت SOCKS5 استفاده کنید.
🧪
اگر حالت System Proxy با یک برنامه ناسازگار است، آن برنامه را به‌صورت دستی برای استفاده از
127.0.0.1
و پورت SOCKS نمایش داده شده در WhiteDns پیکربندی کنید.
⚙️
مگر در صورت نیاز، از تغییر مقادیر تونل پیشرفته خودداری کنید؛ مقادیر پیش‌فرض معمولاً پایدارترین هستند.
🛡
@whitedns</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/697" target="_blank">📅 18:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-696">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">برای اشتراک‌گذاری اتصال
WhiteDNS
روی وای‌فای با دستگاه‌های دیگر، کافی است داخل بخش تنظیمات، مقدار
Proxy Address
را از:
127.0.0.1
به این مقدار تغییر دهید:
0.0.0.0
بعد از انجام این تغییر، در بخش
Connection Info
یک آدرس IP جدید به شما نمایش داده می‌شود. از همان IP می‌توانید برای تنظیم پروکسی روی دستگاه‌های دیگری که به همان شبکه وای‌فای متصل هستند استفاده کنید.
لطفاً دقت کنید که برای اتصال دستگاه‌های دیگر، نباید از
127.0.0.1
استفاده کنید. باید حتماً از آدرس IP جدیدی که داخل
Connection Info
نمایش داده می‌شود استفاده شود.</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/whitedns/696" target="_blank">📅 18:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-695">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پروژه‌ی TheFeed که متعلق به Sarto هست و قبلا درموردش حرف زدیم برای ios هم عرضه شد! میتونید با نصب برنامه‌ی Testflight در Appstore و رفتن به لینک زیر برنامه رو دانلود کنید:
https://testflight.apple.com/join/J6bfxDdZ
لینک کانال TheFeed
@WhiteDNS</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/whitedns/695" target="_blank">📅 17:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-694">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجاوید نامان ایران(Bamdad)</strong></div>
<div class="tg-text">کانفیگ برای کلاینتهای وایت دی ان اس  بر روی اندروید، آی او اس، مک اوس، ویندوز و لینوکس
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDIiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5iYW1hay54eXoiLCJlbmNyeXB0aW9uX2tleSI6ImFhZjRiNi1ASmF2aWRuYW1hbklyYW4tYWFmNGI2ZmZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDMiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5pcmRtYy5jb20iLCJlbmNyeXB0aW9uX2tleSI6ImFhZjRiNi1ASmF2aWRuYW1hbklyYW4tYWFmNGI2ZmZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDQiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5qbmlyLm15IiwiZW5jcnlwdGlvbl9rZXkiOiJhYWY0YjYtQEphdmlkbmFtYW5JcmFuLWFhZjRiNmZmZiIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDUiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5pZ29paS5vcmciLCJlbmNyeXB0aW9uX2tleSI6ImFhZjRiNi1ASmF2aWRuYW1hbklyYW4tYWFmNGI2ZmZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDYiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5qYXZpZG5hbWFuLmNvbSIsImVuY3J5cHRpb25fa2V5IjoiYWFmNGI2LUBKYXZpZG5hbWFuSXJhbi1hYWY0YjZmZmYiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQEphdmlkbmFtYW5JcmFuIFphbDEiLCJzZXJ2ZXIiOnsiZG9tYWluIjoieC5uYW1hZC54eXoiLCJlbmNyeXB0aW9uX2tleSI6ImFhZjRiNi1ASmF2aWRuYW1hbklyYW4tYWFmNGI2ZmZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/whitedns/694" target="_blank">📅 16:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-693">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یه تشکر از کانال
https://t.me/Masir_Sefid
این دوستان عزیز از روز های اول شروع کردن به آموزش، تنظیمات و اشتراک گذاری سرور های رایگان برای اتصال رایگان.
اگر دوست دارید عضو چنلشون بشید و از آموزش، سرور و تنظیماتی که میذارن استفاده کنید.
ممنون از همه دوستانی که برای اتصال رایگان هموطن هامون تلاش میکنن
🫡
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/whitedns/693" target="_blank">📅 15:54 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-692">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">لیست ۱۰۰ ریزالور با بیشترین درخواست ها به سرور های WhiteDNS
185.94.98.34
185.142.158.162
5.160.128.142
2.189.44.68
93.115.127.9
109.230.89.90
217.219.162.200
94.232.173.28
134.255.206.205
80.75.7.2
185.208.174.167
185.37.55.30
185.51.201.58
185.53.142.174
185.255.91.60
185.88.178.196
164.138.17.122
78.157.41.60
5.202.252.30
31.214.169.244
185.109.61.27
2.188.21.58
185.213.11.85
178.252.128.66
2.188.21.70
185.105.101.1
2.189.44.98
109.107.159.86
77.238.123.179
2.188.21.46
172.64.32.0
173.245.58.0
151.232.36.4
108.162.192.0
185.208.175.228
185.137.25.146
185.208.183.29
207.211.215.145
185.50.37.52
2.188.21.138
109.230.206.175
2.189.44.14
85.185.1.10
46.32.31.30
109.72.197.1
2.189.44.84
2.189.44.82
80.191.163.249
2.189.44.86
2.189.44.83
2.189.44.85
78.39.234.140
85.185.157.181
37.191.95.70
185.191.79.210
185.141.105.139
74.80.77.247
78.38.174.2
74.63.24.210
74.63.24.211
2.189.44.93
185.53.141.230
2.189.44.94
74.80.77.246
2.189.44.91
2.189.44.92
2.189.44.90
2.188.21.146
172.253.228.147
74.63.24.205
172.253.12.151
172.253.12.155
172.253.228.150
172.253.228.145
172.253.12.16
172.253.13.147
172.253.13.146
172.253.13.156
172.253.13.154
172.253.13.152
172.253.13.149
172.253.228.156
78.38.114.66
172.253.12.221
172.253.12.150
172.253.13.157
172.253.12.154
172.253.12.210
172.253.13.145
172.253.13.148
172.253.12.212
172.253.13.151
172.253.12.216
172.253.228.148
@WhiteDNS</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/whitedns/692" target="_blank">📅 15:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-691">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">WhiteDNS-1.5.0-x86.apk</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/whitedns/691" target="_blank">📅 13:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-690">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دوستانی که تازه اضافه شدید، سوال دارید یا نمی‌دونید چطوری از WhiteDNS استفاده کنید، تمام مراحل زو اینجا براتون توضیح دادیم
https://t.me/whitedns_group/32380/32404</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/whitedns/690" target="_blank">📅 13:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-685">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/whitedns/685" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر از مطمین نیستید، ورژن یونیورسال رو دانلود بکنید.</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/whitedns/685" target="_blank">📅 13:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-683">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fAiCUI2xkW25f4fE12MZGrcreZKm5Lhao6Pn6A6ec-8lgccQa_jWkwd0ijB98ijSKLVvStVcNA9ieK2PFoezw1hOf2fJ9OLYG2CHbGui2nTRgP8txS1MPDExfVRCZGqGkpbJLEG_hHSogbSHLgVGoAHB4RGzkTEvxtUjpkeOw9LQRFirbC9eswOFBVdWGtdtkqqeCZUU01z4MtqIHXPxk-GHAlzJ8RnwYdXwgaWT4zvpAYxZ-yfR37tU3IqHBbw4PIQ7gBCLrX_boc3pp07wPqhV20o3vB9qbWsR5aGeKr6SnxdSEyl6syDEWC438OTETPDoYHHUN4MbEsZsfsoDZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gdy9COWuBG969Xa_UHQbcJara7y80up8ItPHNGJifq4VFzQBm4jKVS4cHss9uzK132Px_8nz8-OipmiBE1j7c7Z9G8xPOvTHzlqSvWnvCqb9oYa-P6LLgSBmLVVX-4hagRotwaRYqbS5m2X6dHAa6U_B_v4JoyEpQA381xSD6zga6lqSX_kjxrO0RPl-BLmIBs-k0iDHST0ng1rtXUaj3tLsKsevf27bw704g7LZdo1MvuptWZhs82smEHdCh4TKNfNpByq3nauHkLOPphQm7nCYXN8mAYyzEVuQyF1J9860-JF-ZE_glQCISY0KuP6NO35yGdieb5monZCg1gxCjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام خدمت همراهان عزیز،
تمرکز در این نسخه روی زبان فارسی، دسترسی پذیری برای افراد با مشکلات بینایی، تست گروهی سرور ها و خروجی از ریزالور ها بوده.
✅
نسخه اپلیکیشن به 1.5.0 ارتقا پیدا کرده
✅
تست سرورها اضافه شده و می‌توانید سرعت، Ping و وضعیت سلامت همه سرورها یا هر سرور جداگانه را بررسی کنید
✅
نتیجه تست کنار هر پروفایل سرور نمایش داده می‌شود تا تشخیص سرورهای بهتر یا مشکل‌دار راحت‌تر باشد
✅
زبان فارسی به اپ اضافه شده و می‌توانید از داخل تنظیمات بین فارسی و انگلیسی جابه‌جا شوید
✅
چیدمان فارسی راست‌به‌چپ شده و فونت Vazirmatn برای خوانایی بهتر اضافه شده
✅
بخش‌های اصلی اپ مثل اتصال، پروفایل‌ها، اسکن، لاگ‌ها و تنظیمات فارسی‌سازی شده‌اند
✅
دسترس‌پذیری اپ برای TalkBack و صفحه‌خوان‌ها بهتر شده و دکمه‌ها، تب‌ها، اسلایدرها و کارت‌ها توضیح واضح‌تری دارند
✅
وارد کردن پروفایل با QR راحت‌تر شده
✅
خروجی گرفتن همه Resolverهای ذخیره‌شده در یک فایل اضافه شده و Resolverهای تکراری حذف می‌شوند
✅
تنظیمات Parallel Test مرتب‌تر شده و تنظیمات پایدار به‌صورت پیش‌فرض استفاده می‌شوند
✅
تنظیمات تهاجمی‌تر Parallel Test جدا شده‌اند و فقط در صورت فعال کردن استفاده می‌شوند
✅
نتیجه اسکن Resolver پایدارتر بروزرسانی می‌شود و پروفایل Scanner Result فقط بعد از پایان اسکن تغییر می‌کند
✅
پروفایل Default Resolver دیگر اشتباهی به‌عنوان پروفایل دستی ذخیره نمی‌شود
✅
وضعیت تست سرورها هنگام قطع اتصال یا خطا بهتر پاک می‌شود
ممنون از دانی عزیز برای تغییرات مربوط به زبان و دسترسی پذیری
❤️
در این ورژن تنظیمات جدیدی برای تست موازی MTU اضافه شده. دوستان عزیز که ابتدا مشکل داغ شدن گوشی موبایل داشتن، این گزینه رو بیارن پایینتر. مقدار حدود ۳۰ میتونه خوب باشه. اگر همچنان این مشکل رو داشتید مقدار های کمتر رو امتحان کنید.
همنین دوستانی که گوشی های مدل بالاتر دارند، میتونند مقدار های بالاتر رو تست کنند.
@WhiteDNS</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/whitedns/683" target="_blank">📅 13:38 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
