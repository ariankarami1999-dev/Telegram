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
<img src="https://cdn4.telesco.pe/file/fO3_Zq6f5qwUki1HWYhszG7e_vnyxyfDPZ0JiAlVHrtMghN9tgiZGAqpt8qRXFTRZI3rvcc6M4C3q1Dh1Oayykx9GvqX_rEVergUeIJKZC7VhPHOM7z0mNcDs4vxVrx745aM1JYUntq8grNzBH5ITb4qB5oDTz4PtRjB6Ii53ssrjXIxWFmqJK7nuLBCxl9-0pdMD3VF1X7s9Hq7KiNDvpZZ2JiZcqkb6yCpntZawaGwvkfH7RCo7BxcQ_IjiAw_T2_Tax51kbUImNG-Cne7AOEJ26JFCXikmEWpkdz1dNKTiJhPrVWg-jNjiqwH8lf7cInbgufnobYXnNC33r1e-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 40.6K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 13:09:42</div>
<hr>

<div class="tg-post" id="msg-8713">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 614 · <a href="https://t.me/IranProxyV2/8713" target="_blank">📅 12:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8712">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/IranProxyV2/8712" target="_blank">📅 10:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8711">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/IranProxyV2/8711" target="_blank">📅 09:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8709">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/IranProxyV2/8709" target="_blank">📅 09:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8708">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/IranProxyV2/8708" target="_blank">📅 08:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8707">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/IranProxyV2/8707" target="_blank">📅 08:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8706">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/IranProxyV2/8706" target="_blank">📅 08:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8705">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/IranProxyV2/8705" target="_blank">📅 07:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8704">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/IranProxyV2/8704" target="_blank">📅 07:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8703">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/IranProxyV2/8703" target="_blank">📅 02:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8702">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/IranProxyV2/8702" target="_blank">📅 02:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8701">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/8701" target="_blank">📅 00:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8700">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/IranProxyV2/8700" target="_blank">📅 00:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8699">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8699" target="_blank">📅 00:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8698">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تانل پرسرعت آیپی آلمان تو ربات موجود شده فقط گیگی 20 هزار
🇩🇪
⚡️
10GB=200T
⚠️
دوستان 200 تا تست ۱٠٠ مگابایتی ۱ روزه تو ربات موجود شده ، خواهشا تست محدوده اگه میخواین بخرید فقط تهیه کنید و سرعت تست کنید درصورت رضایت میتونید سفارشتتونو ثبت کنید
❤️
💥
@RUSSIAPROXYY_Bot…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/IranProxyV2/8698" target="_blank">📅 00:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8697">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تانل پرسرعت آیپی آلمان تو ربات موجود شده فقط گیگی 20 هزار
🇩🇪
⚡️
10GB=200T
⚠️
دوستان 200 تا تست ۱٠٠ مگابایتی ۱ روزه تو ربات موجود شده ، خواهشا تست محدوده اگه میخواین بخرید فقط تهیه کنید و سرعت تست کنید درصورت رضایت میتونید سفارشتتونو ثبت کنید
❤️
💥
@RUSSIAPROXYY_Bot…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/IranProxyV2/8697" target="_blank">📅 22:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8696">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/IranProxyV2/8696" target="_blank">📅 19:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8695">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
⚠️
اقتصاد نیوز : ایرانسل و همراه اول امکان خرید اقساطی بسته اینترنت رو فعال کردند.
اوج خوشبختی ایرانی خرید قسطی نت
😠
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/IranProxyV2/8695" target="_blank">📅 18:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8694">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/IranProxyV2/8694" target="_blank">📅 15:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8693">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/IranProxyV2/8693" target="_blank">📅 15:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8692">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یه سوپرایز دیگ هم واستون دارم، بزودی رونمایی خواهیم کرد
😁</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/IranProxyV2/8692" target="_blank">📅 14:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8691">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=40T
💥
توجه کنید پلن های 3 گیگ، 5 گیگ، 10 گیگ، 15 گیگ و 20 گیگ تو ربات موجوده با تخفیفففف
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت…</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/IranProxyV2/8691" target="_blank">📅 13:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8690">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYCBwY2eFkPZiRyak8XeJ5w_dnIqpZmbw4-7gAXa3wDxbuwt-DxRQjFN0vJeiVP2j-RavEdpj97mXHXK5SDGkNi2COtHRR3QyrKVuiL9HQLND0Ul9ZChS_ukHsgrtItPpz-VJjd2BcbtkdNveXU9iZAIsCNrDl7Z4ztKph7tLf0USj4EcyiIG9gpYq1-0xtd7zDIWzl8cX3SOxg1a0LmOyjruHZlHFvqsvoGCq5l1MvSU_BFqfUQE98zTG4L-IU4o5iwSoLxaqBXMUbwN3FLfkHv0dzbEz9_f4mPwn4HizealaZKV61UyUctYfgp0OqphWozG4kOWNcDqIMY1_q7Eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/IranProxyV2/8690" target="_blank">📅 07:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8686">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/IranProxyV2/8686" target="_blank">📅 01:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8681">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/IranProxyV2/8681" target="_blank">📅 00:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8679">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/IranProxyV2/8679" target="_blank">📅 00:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8678">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnEm8ShfchB0JXZNHpQmy_DuJOMtemdURKgZ7W8GH0ojZg8ap-fVdK5qDVRDCt1YgjOQDhd6i9RhIwC4u1VYLBMqghXktvmxiOE2OzqTSmy_sjHUZ9UsPR9GMR45ASEYS6DkS_QGDyXih4M6XcmgO-t45BF08D4PyWcqB6l5-37jWcwZPvlaLqhqFnfoYTkLHVBXJ1UiZcgOm8igU0Ut229GWOgQTpU8cCY7fkbZfCFjR07afgSeFka8ovrwhXvDHszF1s3tIrMWvYFp0Gd4riRA73jsXxdvTdamW4nxS2bWFMUt0_XrTAisEyoQ5ME9bm1bub88w3xSNdryut_dOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/IranProxyV2/8678" target="_blank">📅 23:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8677">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">vless://309f5aa1-2665-4ceb-9cc1-17eea907a927@185.143.235.201:8880?path=%2F&security=none&encryption=none&host=sublink2.ionosio.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
اختصاص کانال
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/IranProxyV2/8677" target="_blank">📅 22:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8676">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/IranProxyV2/8676" target="_blank">📅 20:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8675">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/IranProxyV2/8675" target="_blank">📅 19:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8674">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rrzyo2ou6Se9BHwFr6BeOvarwWRsq2mymlKDpYGpNaUi5njAcGV1H1jiIOjkOZa4wMOIlA1domyNgeZHcu6v14N3S62mZFV3i1IaXINuH0l82xmDmux-YbCBsrLj_KPzWYl1w05yE0u7zHCtAFikuZy9gm02N6O25l2aY53MYwxVGXhgUPjFZNB7bn4hSz3YrUzSf5K4hHhTvvQ-c19ZCrx85Ga2OyU5S9js-HGebXOAgwmi5vELTMqGWfcJmuP6S0lkzouNauaHjA8P-OURPgQ6O4RVzPtvOq53b-99BZKmgnnZMKTVvRzi83irlaRHy9sYNV7jmxbYYkDpYg3M8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/IranProxyV2/8674" target="_blank">📅 19:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8673">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/IranProxyV2/8673" target="_blank">📅 17:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8672">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">vless://dfd2bd8a-aedb-47d1-b87c-c22f18495592@f101001010.imsoon.org:80?encryption=none&host=play.google.com&path=%2Fsoon&security=none&type=ws#Xhttp80-iao93lhbdd-1000.00GB%F0%9F%93%8A
به غیر از همراه اول، مابقی اپراتورا وصله
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/IranProxyV2/8672" target="_blank">📅 17:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8671">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
مدیرعامل آروان کلاد(ابر آروان):
◀️
از نظر فنی همینطوری که میشه توی یه لحظه اینترنت رو قطع کرد؛ همینطوری میشه تو یه لحظه هم وصلش کرد. زمانبر بودن بهبود وضعیت اینترنت از نظر فنی فقط بهانه ست. وضعیت اینترنت در حال حاضر بسیار ناپایدار و ضعیفه و اصلا به شرایط قبل از جنگ برنگشته.
ببخشید که ما ریدیم تو نت دیگه تکرار نمیشه روانی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/IranProxyV2/8671" target="_blank">📅 17:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8670">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpYRW5aZWRwMm1rVGJUMXFD@4.168.201.246:443#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vmess://eyJhZGQiOiI1MS4xOTUuMjM1LjcxIiwiYWlkIjoiMCIsImFscG4iOiIiLCJmcCI6IiIsImhvc3QiOiIiLCJpZCI6IjU5ZTI4Zjc4LWMzMWItNDYxMy05ZDlmLTFlNjczMmEzMWY0NiIsImluc2VjdXJlIjoiMCIsIm5ldCI6InRjcCIsInBhdGgiOiIvIiwicG9ydCI6IjIwNTIiLCJwcyI6IkBSVVNTSUFQUk9YWVkg8J+Ht/Cfh7oiLCJzY3kiOiJhdXRvIiwic25pIjoiIiwidGxzIjoiIiwidHlwZSI6Imh0dHAiLCJ2IjoiMiJ9
vless://9ca41eeb-4b30-4271-a123-22021b1230d0@104.17.121.71:443?mode=auto&path=%2FTelegram-Zedmodeon&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=mano.tll-far.ir&fp=chrome&type=xhttp&allowInsecure=0&sni=mano.tll-far.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
trojan://f6d3aa07a52dbcedcb4731029e2fb6ae@18.163.128.27:2663?security=tls&insecure=0&headerType=none&type=tcp&allowInsecure=0&sni=www.nintendogames.net#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/IranProxyV2/8670" target="_blank">📅 13:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8669">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKvac1hXe_3AACKrS7ZIBEfvG6JOYmeAfFYMJRzszO6XbbAsWS9rkHhP6XtO2XBbg2cUq9IPbUjqG1lTxMfl7AZKPh8cq1Iu2FP5UV5T3zismHEcJKQ8x-7-02bsius82DZZNfqXfUqE2HLCx8-XXtj4uc6vfpMeQFA25RlWPtRc7NzOPsAc3NlP1G99u-NdUEzN9G0c6p0svVgC9fFJ2UJLDWdZsO_rbVVpv_oi2xyqbYdLXXPxg-Sb7E_PxaZDV_6KtHM5SsM1vPihRCnqQb9u0TDW-YZ_0Z3nNmFCHo1Rk_UoNgdRAOwDFB39XD2fC5MHYmVrl5i_KSkiHLY_GQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/IranProxyV2/8669" target="_blank">📅 13:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8668">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/IranProxyV2/8668" target="_blank">📅 09:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8667">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/IranProxyV2/8667" target="_blank">📅 08:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8666">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/IranProxyV2/8666" target="_blank">📅 08:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8665">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/IranProxyV2/8665" target="_blank">📅 07:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8663">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vP_G9xS4SpwDJ6q5JJcAXrQJjHi3y9YfWuces8rHPgLAl2lmlNnkfTyf-itSKhFes-bHObz72pj6Ht_wivDCJXGNFtN6viMDsqEN_Zmls0_8R5pA-5I4_3gNFl5PoYccqkBuBMEN_qRRLQ91Z_A1JVoehGu-OfE6JAsqCNcMhsjbeq9Pn15l6va9RJ8W0ivKbNXxf4IOR-0uRD4-wc8xzUmPXgHt1NUaqSBaddBeb6RFaKwLDSw9Y4b_KK2_7F_W1zstf9UJAky_MgOatnbbwRnT3inb6LFqRXTJX7WcxECE5mOx80_2t2HFtx_IYMtYTI4eIrold5j-m36Goc8rVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/IranProxyV2/8663" target="_blank">📅 01:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8659">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/IranProxyV2/8659" target="_blank">📅 21:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8658">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adC8AzqtbLZ47jVOee-ekgi2eBUKGW9ZFXGU2ZOkwIowWvnXNf9qqq-mptn7DnXoReTthCBkJa5KSh41dMSlLzn7d3geFDczYqgs-eZIPB_h3-8IIdZoGpti7QrO76Q2tOGmzIGRqbiyZadtylOaqExAH908mBr8zUfIKrrQq6OKGr4f5GQvwaqf-nIxy6Kn85L0b3s8glWga_YUlN49zaZJ26eyqVWMceF2vU2kSkut1n4er1BAqZfkDbOC7SVB1vDKk5Z6VEznpP7YNWnB0sAL10Ke7liX_WpLH9xYVFNCINPOJlEEoxz45XcHe8ekcYjsDCdJBiOL04upubdBdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/IranProxyV2/8658" target="_blank">📅 20:40 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8657">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQ2zvMxJzctOuQ0oRWL8qcnATQ59lmcV3gOL0elEFY-dIFE6M5NRdLJvy2xrWecuwMjgdJLsFwRhBXL-m9H-dNz_MMDt4zjyajjS1qYOiAzZpU-ObRXn_yseAOsCf42rjOY_hiHB-UOfBkcO8rlfDOeoVcrAhpwvHsPNbazzpKNlE1xOZ1bseO3EnX36STw8oZsK7Na8004WTBGUrWEt7MxE8YxeI2nJg7W1EGvVv46zpOt9oeCrExvZja91bPVQLHZiZH_JDFBXe3JZmykG367j-5JfdJayp5oMn1WnnzqrHZjoZYAlU0fU_vzLGLgiqVqt9tZ17XgAJ-CkTg1NMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😬
😬
😬
😬
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/IranProxyV2/8657" target="_blank">📅 20:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8655">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/IranProxyV2/8655" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8654">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/IranProxyV2/8654" target="_blank">📅 18:10 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8653">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqKrCAmkLPVZ54o1od3Ksc8slO_hKmY8czTiVADiK5UOQSc6lV_TnVXXXYtP4xyyv-x9tR5O6gtVsxUNUQMN_pGgbRLRUxM0a12uKAQlpBcM20pqKZr9jHllQpOyJlGlPQ2EVNZ2nlFXDgyaVfKQFO-mdq4Ngeh2GOi4_TNWwzspg7kDRd9Rb_pFgcOZNYjhccWE2JrXDMj1KKblFTWJxDNcbQixWJ8W1Xyy-GiYlHetccCkp0GYEQZnk-hXPs8U_E0fPGfaD0mQHpU0jOGs3jbMttWBKKeugi1CH1fQD0VgZQxVG7mXZJp59zuZ6xgMi5wQTyf7x5YP1tTid8sOiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مدل محتوا(دیتای کاملا جعلی و روایت ساختگی) که یسری از رسانه‌ها(دلقک‌های حکومتی) دارن منتشر میکنن فقط داره به قطع اینترنت و فیلترینگ مشروعیت میده و اصلا جنبه فان نداره!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/IranProxyV2/8653" target="_blank">📅 17:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8652">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/IranProxyV2/8652" target="_blank">📅 15:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8651">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/IranProxyV2/8651" target="_blank">📅 10:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8650">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">trojan://humanity@www.calmlunch.com:443?path=%2Fassignment&security=tls&insecure=1&host=www.calmlunch.com&type=ws&allowInsecure=1#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
vless://e258977b-e413-4718-a3af-02d75492c349@45.130.125.69:2096?path=%2FChannel----%40VPNCUSTOMIZE&security=tls&encryption=none&insecure=1&host=jp.aniua.qzz.io&type=ws&allowInsecure=1&sni=jp.aniua.qzz.io#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/IranProxyV2/8650" target="_blank">📅 08:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8649">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/IranProxyV2/8649" target="_blank">📅 06:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8648">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 10K · <a href="https://t.me/IranProxyV2/8648" target="_blank">📅 23:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8647">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/IranProxyV2/8647" target="_blank">📅 18:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8646">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">درحال بررسی و آپدیت جدیدی برای سرورا هستم، کمی طول میکشه ولی سوپرایزی در راهه
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/IranProxyV2/8646" target="_blank">📅 18:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8645">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/IranProxyV2/8645" target="_blank">📅 18:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8641">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
سنتکام: حمله ایران به کویت با موشک بالستیک نقض آشکار و فاحش آتش بس بود
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/IranProxyV2/8641" target="_blank">📅 14:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8634">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/IranProxyV2/8634" target="_blank">📅 14:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8633">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ایفونی های عزیز جامپ جامپ استفاده نکنید اپل ایدیم لاک شده سر این فیلتر فیلتر دیگ استفاده کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/IranProxyV2/8633" target="_blank">📅 13:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8630">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Openvpn.ovpn</div>
  <div class="tg-doc-extra">54.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8630" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟠
open vpn
🛜
برای ایرانسل رایتل مخابرات چک کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/IranProxyV2/8630" target="_blank">📅 13:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8629">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دیشب آمریکا به بندر عباس حمله کرد ایرانم در جواب به کویت حمله کرد اما هنوز اتش بس نقض نشده
به این میگن یه توافق درست حسابی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/IranProxyV2/8629" target="_blank">📅 13:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8628">
<div class="tg-post-header">📌 پیام #40</div>
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
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/IranProxyV2/8628" target="_blank">📅 13:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8627">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8UZgMdOtUc7M9cCVOqBL10PWti936R1xhUqnn_J17iFHmR4woEByxvqgRym6qYR4OCKh66hxl1sGyzF3FdGrR7r8mVdkR3qbtztYmb2GYaC3GKs36paefiMfWDGTY2JiiFWG-BAwprOmz_deRweeQbPDcs0iOWd6k6zjjYFFUO9e960OCs-vIz5RN9qG7KTYtwDnY15Lstr1NujBwim7d3atlGr_vKBcun65wkq2hTnaGa4OLyXM8q2vacJyK8gsV2PZGouxoAcU7BREs8l7a3xyGGpSbVPRb_8iMJdf3Qcx57REhqCRwd_INlgvn_N0oMGCqaf4oxoef6MAWMmig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آخرین آپدیت از وضعیت اتصال اپراتورها به اینترنت بین‌الملل!
+ طبق این لیست ، ایرانسل با 38 درصد بالاترین اتصال رو به نت بین‌الملل داره و باقی اپراتور ها و شرکت ها همگی زیر 30 درصد اتصال دارن!
++ یعنی اگه اینترنت رو مثل یه دریچه در نظر بگیریم ، الان فقط به اندازه رد شدن هوا این دریچه باز شده!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/IranProxyV2/8627" target="_blank">📅 12:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8626">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfFu_N0cIJLNJ_4a40ACvE9clitI5SVwDS91SsG1FoVB1qFuckIJDs5xg1Ljj_Y4ZzPHmio0dlhWq0XOHhOrrMUMG8Y9SqvhJNcV7st0XIcXP_O2Ob54xe10fJVb4pDbLnk_jTNAg2Cz74qEwx1NrMwbmZ7-7xVreD3FboxW2iARrwF6Tyw_T7WPZfsaC4IpYIDLxNIKpW30fkJKoTm_MWLRRchAAvkbckjv09zrwHmIyz-46LRZt2x2n4x1D2LuK12WbAErvjlW8BAJasSh-1wz58tjmOiu0ePTwhkoIbQYXANdCd7mNfXr1lKXMpqJwskkjwdK3XDuk8vlwSfpUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍽
فعلا درحال حاضر تونستم تانل جدیدی بزنم رو دیتاسنتر جدیدی که پیدا کردم و تهیه کردم براتون از خارج کشور پینگ میده، با قیمت مناسب و پینگ بینظیر، باز مجدد اگه سطح دسترسی ها افزایش یافت تانل های جدیدی با قیمت هایی پایینتری براتون موجود میکنم حتما،نگران هیچ موضوعی نباشید تا آخرین مگابایت مصرفیتون پشتیبانی انجام خواهد شد
👀
🔐
1GB
➡️
60T
💥
◀️
جهت ثبت سفارش میتونید از ربات اقدام کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/IranProxyV2/8626" target="_blank">📅 11:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8625">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🟢
پروکسی متصل با سرعت خوب
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ%3D%3D
https://t.me/proxy?server=tg.capycore.ru&port=443&secret=27ebe852539fb8ec5f327c73262bb721
https://t.me/proxy?server=87.248.129.129&port=15&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d
برای اتصال به پروکسی ها حدود 10 ثانیه صبر کنید
⚪️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/IranProxyV2/8625" target="_blank">📅 10:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8624">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">vless://f172c28c-14f7-408b-b41e-838f4f32a15f@185.143.234.122:2082?path=%2F&security=none&encryption=none&host=tl2.axepart.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
وصله دوستان استفاده کنید
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/IranProxyV2/8624" target="_blank">📅 09:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8623">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/IranProxyV2/8623" target="_blank">📅 09:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8622">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">❤️‍🔥VIP❤️‍🔥.npvt</div>
  <div class="tg-doc-extra">3.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8622" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/IranProxyV2/8622" target="_blank">📅 08:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8621">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺(3).ovpn</div>
  <div class="tg-doc-extra">5.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8621" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/IranProxyV2/8621" target="_blank">📅 03:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8620">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/IranProxyV2/8620" target="_blank">📅 03:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8618">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
یکی از دلایل اصلی اختلال و کندی شدید اینترنت، سقوط سهم IPv6 در شبکه ایرانه؛ سهمی که از حدود ۱۲٪ به فقط ۰.۱٪ رسیده.
این افت باعث شده فشار شدیدی روی IPv4 بیفته و نتیجه‌اش رو حالا کاربران به شکل اینترنت ناپایدار، اختلال VPNها، ضعف شبکه موبایل و لگ شدید در بازی‌های آنلاین می‌بینن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/IranProxyV2/8618" target="_blank">📅 02:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8617">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
⚠️
گزارش‌های اولیه حاکی از آن است که ایالات متحده یک عملیات دفاعی را در بندرعباس ایران انجام داده است
.
🔴
یک مقام آمریکایی گفت: «ایالات متحده برای حفاظت از منافع منطقه‌ای خود اقدام خواهد کرد و این بر آتش‌بس تأثیر نمی‌گذارد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/IranProxyV2/8617" target="_blank">📅 02:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8616">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⭕️
خبرگذاری فارس صدای انفجار رو تایید کرد
🔴
شنیده‌شدن صدای ۳ انفجار از شرق بندرعباس
🔹
حوالی ساعت ۱:۳۰ بامداد صدای ۳ انفجار از شرق شهر بندرعباس شنیده شد.
🔹
هنوز محل دقیق و منشأ این صداها مشخص نیست و پیگیری‌ها برای مشخص شدن آن ادامه دارد.
🔹
همزمان برای دقایقی پدافند شهر بندرعباس نیز فعال شد.
🔸
طی ۴ روز اخیر نیروهای مسلح کشورمان یک پهپاد آر کیو ۹ و یک پهپاد اوربیتر‌ دشمن آمریکایی صهیونی را در منطقۀ هرمزگان منهدم و همچنین سامانه‌های پدافندی نیز یک اف ۳۵ و یک پهپاد آر کیو ۴ را نیز رهگیری کردند.
📝
اخبار تکمیلی متعاقبا منتشر می‌شود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/IranProxyV2/8616" target="_blank">📅 02:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8615">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‼️
مث اینکه بندر عبارسو میگن زدن و صدای جنگنده میاد
🧐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/IranProxyV2/8615" target="_blank">📅 02:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8614">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‼️
مث اینکه بندر عبارسو میگن زدن و صدای جنگنده میاد
🧐
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/IranProxyV2/8614" target="_blank">📅 02:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8613">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/IranProxyV2/8613" target="_blank">📅 01:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8609">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کافه پروکسی💥.ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8609" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اوپن ویپن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/IranProxyV2/8609" target="_blank">📅 00:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8607">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Openvpn.ovpn</div>
  <div class="tg-doc-extra">5.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8607" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ open vpn
🎀
آموزش اتصال:
⬇️
کانفیگ رو وارد برنامه کنین
بزنین روی connect
بعدش ۲ تا گزینه میاد بزنین روی continue
عشق کنین
🍒
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/IranProxyV2/8607" target="_blank">📅 00:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8606">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awyD2rMI2qnPU93p4BqPirUo43tnz8Yjv95JqVYLZN7SppFnUeppaqS-xJCloLr5pUhitZO0RQF4sh3Odfyd9Dvbf4LaqjxUlKdUknpiD_Yy4ObQSsYlh4AXKIvX8UXMsHq5o3npRvGNQNIMEVdxMmwwidBeUZdUhaqGbC0DNWLoi9-BenjbN-z4CDYARSA3QCIP7Aoa7G8kyGWrvEkd4012jTeNhD3B89zIkOvO4T5HNbkSRp3m3HwX4da8_wiKhASK50KZWHC9BN3-MxFiWtvH2UEj7hEYzFOYG5YRhEYuLOLDzYrofTjvl6fP9BYxVPxS9Jkr2ProEYotue_SuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت :
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/IranProxyV2/8606" target="_blank">📅 23:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8605">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/IranProxyV2/8605" target="_blank">📅 23:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8604">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اپ استور هم رفع فیلتر شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/IranProxyV2/8604" target="_blank">📅 23:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8603">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
گویا گوگل پلی تو اکثر مناطق وصل شده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/IranProxyV2/8603" target="_blank">📅 23:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8602">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺(2).ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8602" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/IranProxyV2/8602" target="_blank">📅 23:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8601">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/IranProxyV2/8601" target="_blank">📅 22:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8600">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/IranProxyV2/8600" target="_blank">📅 21:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8599">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/IranProxyV2/8599" target="_blank">📅 21:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8598">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">💚
پروکسی های جدید و متصل
پروکسی
-
پروکسی
-
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/IranProxyV2/8598" target="_blank">📅 21:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8597">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@RUSSIAPROXYY🇷🇺(1).ovpn</div>
  <div class="tg-doc-extra">5.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/8597" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کانفیگ های جدید اختصاصی OpenVPN با حجم و اعتبار نامحدود
تست شده روی ایرانسل، رایتل، شاتل، سامانتل(برخی نقاط ممکنه متصل نشه)
بدون نیاز به یوزر پسورد
📍
آموزش اتصال تصویری
برای اتصال در تمام سیستم عامل ها کافیه روی کانفیگ کلیک کنید و برنامه OpenVPN را انتخاب کنید، یوزرنیم و پسورد را ست کنید و متصل شوید یا کانفیگ را سیو کنید و از داخل برنامه ایمپورت کنید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/IranProxyV2/8597" target="_blank">📅 20:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8592">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❤
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
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/IranProxyV2/8592" target="_blank">📅 19:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8591">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
ترامپ درباره ایران:
آنها می‌گویند که بسیار تمایل دارند که به توافق برسند.
تا کنون به آن نرسیده‌اند. ما از این وضعیت راضی نیستیم، اما یا راضی خواهیم شد، یا اینکه باید کار را تمام کنیم.
آنها در حال مذاکره با جدیت بسیار کم هستند.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/IranProxyV2/8591" target="_blank">📅 19:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8590">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
ترامپ: ایران حتی اگه اورانیوم های خودشو هم تحویل بده هیچ خبری از کاهش و لغو تحریم ها نیست
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/IranProxyV2/8590" target="_blank">📅 19:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8589">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پروکسی‌های متصل
♥️
https://t.me/proxy?server=49.13.35.164&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=mt.corph.ru&port=443&secret=dd2ed7517b077ef414e24b106e0729335d
https://t.me/proxy?server=free-mtproto.flexiblenet.org&port=443&secret=4da47f00c2291d55696fa3ae954ffd78
https://t.me/proxy?server=ams1.tlgfast.com&port=443&secret=083fe0c452e2407d835537872f097c54
https://t.me/proxy?server=91.107.182.200&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=176.65.131.45&port=25565&secret=79e344818749bd7ac519130220c25d09
https://t.me/proxy?server=91.107.174.85&port=8443&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/IranProxyV2/8589" target="_blank">📅 19:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8588">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">https://t.me/proxy?server=87.248.129.129&port=15&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d
پروکسی متصل سرعت قوی
❤️‍🔥
⚡️
👀
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/IranProxyV2/8588" target="_blank">📅 19:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8587">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اینترنت بین الملل در حال قطع؟
نت‌بلاکس: به نظر روند بازگشایی اینترنت ایران متوقف شده و در حال اعمال محدودیت‌های بیشتر برای جلوگیری از دانلود و استفاده از VPN ها هستند. کماکان هیچ اخباری مبنی بر اتصال کامل اینترنت دیتاسنترها وجود ندارد که مشخصاً برای جلوگیری از گسترش تانل‌ها و VPN ها می‌باشد.
تندروها کار خودشونو کردن واسه همینه خیلیا نمیتونن وصل شن یا سرعت افتضاحه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/IranProxyV2/8587" target="_blank">📅 19:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8586">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sL4qYd0l-8i1YK8t56P5YWf2VAuDMqg3xWg1i4oxdUzzFoSpwAMKikR04zwx-dyCuhSht6j1ezCowTL5WKwjNukMwAxFr05y05pWzEjIzC6r-_HfzgevJSmxEY5I_RwDUh8I9oEO9Y5rmJ_wFxTFFzqAnryCoRA10_6KbWiA1eqMxm2tB0sBaisdQDAsvJ5103Injxcw_owNk9FnzsCJrnZ76Y3qzZ-FSiLjWHx3EjGQlbMOHCjjc-pBeQXr2jCdAOqPTvIO9ZzfL2Tc2sq195KJ3M1Pac1SL5CQYK-THeKiohbsTMRrCCt9bgaYKmUz_8AJWvZ3onf6Wu45qmW5Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که سفارش ثبت کردید تو ربات، دارم یسری آپدیت رو سرورا میدم، صبور باشید، اوکی شد همینجا اطلاع میدم و سفارشتونم تایید میکنم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/IranProxyV2/8586" target="_blank">📅 18:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8585">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❤️
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
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/IranProxyV2/8585" target="_blank">📅 16:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8584">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">این لیست پروکسی اختصاصی رو داشته باشید باید با خیلی از اینترنت ها اوکی باشه
پروکسی اول
پروکسی دوم
پروکسی سوم
پروکسی چهارم
پروکسی پنجم
پروکسی ششم
پروکسی هفتم
پروکسی هشتم
پروکسی نهم
پروکسی دهم
پروکسی یازدهم
پروکسی دوازدهم
پروکسی سیزدهم
بفرستید برای دوستانی که نیاز دارند، وصل بشن
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/IranProxyV2/8584" target="_blank">📅 15:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8583">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">vless://406d8436-0eb9-4eb2-84fb-960e076ffba6@162.159.38.183:2083?mode=stream-one&path=%2Fde&security=tls&alpn=h2%2Chttp%2F1.1&encryption=none&insecure=0&host=de.lezzatzone.ir&fp=chrome&type=xhttp&allowInsecure=0&sni=de.lezzatzone.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
همراه اول تست زدم، اوکی بود، مابقی نت هارو خودتون تست بزنید
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/IranProxyV2/8583" target="_blank">📅 15:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8582">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XExlCcfVnvriYcpX4mYwck1HOcaSRRNJMVgDwlpMZf74dszw7GJmmTt_5bBltb67_axJj9DYbjn3AzTM40EpcqH8ppDrsqgOyiamtS8Aivi0DLjPPVP_iLjmM8Qd2NksGfsVb4jg5NB6qHdDRtKKZW8gb7FaCjDO-EE1cnDVvN-pITxPK1XB4_tqEmzU4UcS8zIoLDu0xjIGPQ83ZZPAw6M2POwofdSakiUPMsL0EJGkMihUYlnZ56MuV44MU8Xy-Xfd082bSB8B5Eexqp3ZebhVinuEutBD79dWwkrvLN3Nfj8snwk-5bl85D9a1QV43q3ifcH_bctHdXqDtqLzPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همراه اول بعد از اعتراض کسانی که اینترنت  پرو خریدن و گیگی 40 هزارتومن بابتش پول دادن اعلام کرد در صورت تمایل میتونن  اینترنت خودشونو به حالت قبل برگردونن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/IranProxyV2/8582" target="_blank">📅 15:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8581">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SK9wrsbJobmkKBigTke1DW0rMFwjgdcXN8g2aKrTK6iFMzX_OdXKIH0QDv4DAQdGEY_N63_YR-P5fO1wqHgey88y9ozT-qXvPJqCtHKhfw0ALal-i1cRYBQ6TeQd3WybHTE78JCdGi9A_OU6ZOgarzui4tE99LoIB-hd9l7nGunvXSMM5-Rb_4hNzysKHWUdr0wMVLASkxGyCKE1M7dXdCyneekNmE4ijNM6qHgZf0UX02KZLl-PN8PNyazcylcT64pUv5RtWdaXUD9d8221J_VvajRnwzOD08V6Y0DoG5LvFfr2BtrVkN1wKdFop73f7uxJp3G2AkbvidFXTWJrbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آخوند حمید رسایی: از وقتی اینترنت وصل شده قلبم درد گرفته، یه لحظه‌ام نتونستم بخوابم
.
وصل شدن اینترنت پایمال کردن خون رهبر شهیدمونه، با اینکار تن رهبری تو گور لرزید.
عوامل موساد باعث بازگشایی اینترنت شدن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/IranProxyV2/8581" target="_blank">📅 15:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8580">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">vless://406d8436-0eb9-4eb2-84fb-960e076ffba6@162.159.38.183:2083?encryption=none&type=xhttp&security=tls&path=%2Fde&host=de.lezzatzone.ir&mode=stream-one&sni=de.lezzatzone.ir&alpn=h2%2Chttp%2F1.1&fp=chrome&allowInsecure=0#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
رو همراه اول تست شده اوکیه
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/IranProxyV2/8580" target="_blank">📅 15:09 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
