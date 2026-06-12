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
<img src="https://cdn4.telesco.pe/file/hpJHV4FbLxK5oA0n3V80pXLqWaYOsBAkPnv4RMjswOtxNorokMWl98VkyFOs7inTkEwNQEchg0YZl7abUFBDBgDxgOdG-eppIokjlMhEhAbOWnwMCCWIZFzHiR9YQOYNy8ZMvXHRDq01W9XlrEuWmmRpsHrZf_4pbtv0SoaBN97CVNJGm5Vg_9UjHpFtTepqDOTEfslqELSlCCEpDyHK1FbRvP4KON7yTqlrY8AFfAx8jpqy7w1ULkNitJgi0G_Dr8pw9cFhEXp3Ma_dn47xbDFuG_2naoI_d9r28-e_Iq5iiFH4XzCqv3grRnOC73K2v5moZ3RmSYibUjAxr3_DbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 108K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhisperInHeaven</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 22:28:47</div>
<hr>

<div class="tg-post" id="msg-968">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gsam2ufvKyckVGymofWtIQNQ2Rs4dmaXQodQQ5aiCwlabghvEOJujPMuun5FoyEb3r1BbU-h1sj8kTc5GZlA7MUxI5gq2orjt9Vga9LawWFGRF8vpSAB9au3v6J1Mwva3RW9_pF-lIjHIaN75GHZG68HRzx16sh2CJo8MjIFXg_4nwuYBTJ80MHFewTL0Jp02Zsajgdva-WQVjak1dKhfXSxYji7XR-zY8SzRN-RRIqyK5oBHzEe5Ln2fZ5-XXxOAFMsAcpKwib92Aqd2hPgAjCm_B7qa4-LukoRO14F8vDxCO1mFvyfaUEJYZVeJAXPqtOFIAKVW-iIde5HXlOYvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/whitedns/968" target="_blank">📅 13:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-967">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">این دومین نسخه تست همگانی اپلیکیشن WhiteDNS VPN میباشد.
لطفا تجربه، سرعت و مشکلات خودتون رو زیر این پست برای ما بفرستید.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/whitedns/967" target="_blank">📅 13:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-963">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-vpn-arm64-v8a-v.0.0.1.apk</div>
  <div class="tg-doc-extra">30 MB</div>
</div>
<a href="https://t.me/whitedns/963" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
نسخه جدید اپ آماده شده
در این ورژن شاید اتصال شما کمی کندتر انجام شود.
ما در حال تلاش هستیم تا در ورژن های بعدی سرویس بهتری ارایه کنیم.
ممنون
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/whitedns/963" target="_blank">📅 13:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-962">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ما راه حل رو داریم، اپ مناسب رو هم ساختیم. حالا فقط باید باهم تست کنیم تا به نتیجه نهایی برسیم.
به زودی ورژن جدید رو منتشر خواهیم کرد
❤️
ممنون از همراهی شما</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/whitedns/962" target="_blank">📅 09:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-961">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">همراهان عزیز سلام
ممنون از تست شما. همونطور که بهتون گفتم این ورژن نسخه تست هستش و ما در حال حاضر به یک مشکل فنی برخوردیم.
به زودی اپ را آپدیت میکنیم.
ممنون از همکاری و گزارش های شما.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/whitedns/961" target="_blank">📅 09:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-960">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">چنل یوتیوب مارو سابسکرایب کنید که یکسری آموزش هارو از این به بعد اونجا به اشتراک میگذاریم
https://www.youtube.com/@WhiteDNS</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/whitedns/960" target="_blank">📅 08:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-959">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">این اولین ورژن اپ وی‌پی‌ان WhiteDNS هستش.
در ورژن های بعدی تغییرات بیشتری ایجاد خواهد شد اما سادگی اپ به همین شکل خواهد ماند.
پشت این سادگی پیچیدگی و تست های زیادی درحال انجام شدن هستش که همه پشت داکمه ساده اتصال پنهان شده.
لطفا توجه داشته باشید که در این ورژن شما محدودیت روزی ۱گیگابات استفاده را دارید.
ممنون
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/whitedns/959" target="_blank">📅 07:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-958">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">لطفا هر موفقیت در اتصال،‌ مشکل و یا نظری رو با ما به اشتراک بگذارید.
ممنون
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/whitedns/958" target="_blank">📅 07:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-954">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-vpn-arm64-v8a.apk</div>
  <div class="tg-doc-extra">30 MB</div>
</div>
<a href="https://t.me/whitedns/954" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/954" target="_blank">📅 07:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-953">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRb4WJM9XiwtrE1YM9dHqpCD5egj-hk6bUUomBEN93p88Aml6_TVGh6ckFaT6s5E_MttO1GgllXlpZy7sPSV1OQsKLNQ2q5L-QONNGQTqiShdM-j9qvqm_vnhpnBKKPVGcmBE8yWlf2x5eLBC5qmDLMffqyQ01d_FCDP6LJ_1djlDO9odLN5GOEEu99AKq3iz-3ZxK2AbGi7pDkDoQvrzZdTCh3otgZ3crc__OiGwtBiqTSTiHKOqXdGtr5PzUdl4j8Y-W4YiTFmvP5X0pDdkbaGbmQmrxaA-mHWtjKWBG8pq_-vXJ03DkVWHrq9g1Sk5usmOPu8sA88zdbPZqE0Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شروع تست پایلوت سرویس WhiteDNS VPN
نسخه تست عمومی اپلیکیشن whiteDNS VPN برای کاربران آماده است.
لطفا توجه داشته باشید که این مرحله صرفا برای تست جمعی است و سرویس ممکن است در هر زمان، بدون اطلاع قبلی، متوقف یا با اختلال مواجه شود.
هدف ما از این مرحله، بررسی عملکرد سرویس در شرایط واقعی، دریافت بازخورد کاربران و بهبود کیفیت نسخه‌های بعدی است.
در روزهای آینده نسخه‌های جدیدی منتشر خواهیم کرد و به‌روزرسانی‌ها به‌صورت مرحله‌ای در دسترس قرار می‌گیرند.
در این نسخه، محدودیت استفاده ۱گیگ  مصرف دانلود+آپلود در ۲۴ساعت اعمال شده است.
از همراهی، صبوری و بازخوردهای شما سپاسگزاریم.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/whitedns/953" target="_blank">📅 07:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-952">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آدرس جدید ساب WhiteDNS با بیش از ۲۵۰۰ کانفیگ تست شده و با سرعت بالا.
https://sub.whitedns.one/sub/mihomo.yaml
لینک های قبلی هم قابل استفاده هستند.
نرم‌افزار های پیشنهادی برای استفاده
iOS
:
Clash Mi
Android
:
FlClash
Desktop
:
Clash Party
|
FlClash
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/whitedns/952" target="_blank">📅 05:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-951">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سلام خدمت همه دوستان   پنل ثنایی در ورژن آخر تغییراتی انجام داده که باعث خراب شدن WhiteDNS Wizard شده.   بعد از گزارش های شما، ما این مشکل رو برطرف کردیم و ورژن جدید whiteDNS Wizard از گیت‌هاب ما قابل دسترسی میباشد.   https://github.com/iampedii/WhiteDNS-…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/whitedns/951" target="_blank">📅 04:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-949">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rlxg_qqp93gfh0dQyPXIcmEsAr8cqp-A_OXTL_dENPXIwdUgY1CEYLyg88Ce8GVWEsG-zgGTOxwQhZQD30hy9ZW79lQu7LanhszyRSvwtsAzdiWc2EUA4SqOj_NgzlkD3ATY1XC6byld3DSfW_V6TiHfoHtdUyj50TwznNC5iCKARw7oLqg1Pu2oGH9b69M_9EJNnM4FxWCGbcvuR_DdmC5X8_P9wwxmfnbtFi51xL5YAVPmzrutTrnHJmKvm5DxcGmasovfMO6DcM8bZui0Pv74j8S5ovt2IPvS7I5mjE1FMj8W9FyA5rGkBemNPeSlSpOvUHsVeb9II8vWE-iY5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان
پنل ثنایی در ورژن آخر تغییراتی انجام داده که باعث خراب شدن WhiteDNS Wizard شده.
بعد از گزارش های شما، ما این مشکل رو برطرف کردیم و ورژن جدید whiteDNS Wizard از گیت‌هاب ما قابل دسترسی میباشد.
https://github.com/iampedii/WhiteDNS-Wizard/releases/tag/v1.2.0</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/whitedns/949" target="_blank">📅 16:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-948">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⏯️
ویدیو آموزش استفاده از WhiteDNS Wizard و نصب و راه‌اندازی کامل و اتوماتیک پنل ثنایی
https://youtu.be/rxxlNXLcaqU</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/whitedns/948" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-947">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/whitedns/947" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-945">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یکی از کاربر های گروه لطف کرده یک ویدیو خیلی کامل و خودمونی از نحوه استفاده از اپ WhiteDNS  درست کرده.
پیشنهاد میکنم تا وضعیت مناسبه دانلودش کنید.
ممنون از همراهی شما
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/whitedns/945" target="_blank">📅 07:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-940">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/whitedns/940" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر از مطمین نیستید، ورژن یونیورسال رو دانلود بکنید.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/whitedns/940" target="_blank">📅 05:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-939">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجاوید نامان ایران(Bamdad)</strong></div>
<div class="tg-text">#کانفیگ
#دی_ان_اس
#وایت_دی_ان_اس
#مستر_دی_ان_اس
انکریپشن کی:
aaf4b6-@JavidnamanIran-aaf4b6fff
c.namad.xyz
c.irdmc.com
c.bamak.xyz
c.javidnaman.com
c.jnir.my
c.igoii.org</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/whitedns/939" target="_blank">📅 05:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ابزار WhiteDNS  برای ساده‌تر کردن راه‌اندازی و مدیریت سرورهای شخصی،  با نام  WhiteDNS Wizard آماده شده است.  هدف WhiteDNS این است که کاربران بتوانند بدون نیاز به دانش فنی درباره تنظیمات سرور، DNS، اینباندها، اوتباندها، گواهی‌ها و پنل‌های مدیریتی، سرور خود…</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/whitedns/938" target="_blank">📅 09:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سلام خدمت دوستان عزیز،  ما سرورها رو آپدیت کردیم و با همکاری جدیدی که شروع شده، از این به بعد ساب‌ها رو مرتب با کانکشن‌های جدید و تازه‌تر رفرش می‌کنیم تا کیفیت اتصال بهتر و پایدارتر بشه.  اگر این دامنه‌ها هم فیلتر بشن، لینک‌های جدید ساب رو براتون می‌سازیم…</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/whitedns/937" target="_blank">📅 09:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سلام به همه دوستان عزیز
در حال حاضر گروه ما هدف یک‌سری حملات از سوی ربات‌ها و برخی افراد مخرب قرار گرفته است. این حساب‌ها در حال ارسال تصاویر و ویدئوهای نامناسب و پورنوگرافی هستند.
تیم WhiteDNS به‌صورت مستمر در حال مانیتور کردن گروه، شناسایی و مسدودسازی این حساب‌ها و ربات‌ها است تا محیط گروه برای همه اعضا امن و مناسب باقی بماند.
از صبر و همکاری شما سپاسگزاریم.
با احترام
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/whitedns/936" target="_blank">📅 17:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سلام خدمت دوستان عزیز،  ما سرورها رو آپدیت کردیم و با همکاری جدیدی که شروع شده، از این به بعد ساب‌ها رو مرتب با کانکشن‌های جدید و تازه‌تر رفرش می‌کنیم تا کیفیت اتصال بهتر و پایدارتر بشه.  اگر این دامنه‌ها هم فیلتر بشن، لینک‌های جدید ساب رو براتون می‌سازیم…</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/whitedns/935" target="_blank">📅 08:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJfEzL0zVBC6dGxI48hl5RnQ6jRE14RqmoeGzn4LPoRMWpexw7UD-rZVMWKzE09U09g0mASEEVPjvCRuSsMrErSn-1gA3TK8qD2SYCbKINZcSJzhaYX6m4Io51-PVMVMOava849vYfd0VPxgCOd_4gQJvPsXcdYroMe80O0mPxhvmgLNCLWK9s4Vrr8laLcrO7-qu6LBG8y9nAatVAPuScPsTKSjE6YxeVz07T3jcjKijXlv8lWyAuyQR4v5RXrq2trWF32UqgbAV-v3sWW0Hdcf9tpYNcRsFKIE3yZdPx_sYlTlZTQvdjEuztgiKVOycQKp-BRvTqWJpomQ94lLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار WhiteDNS  برای ساده‌تر کردن راه‌اندازی و مدیریت سرورهای شخصی،  با نام  WhiteDNS Wizard آماده شده است.
هدف WhiteDNS این است که کاربران بتوانند بدون نیاز به دانش فنی درباره تنظیمات سرور، DNS، اینباندها، اوتباندها، گواهی‌ها و پنل‌های مدیریتی، سرور خود را به صورت خودکار و یکپارچه آماده استفاده کنند.
با این ابزار کافی است اطلاعات اولیه مثل دامنه، سرور و دسترسی Cloudflare را وارد کنید. WhiteDNS به صورت خودکار رکوردهای DNS را تنظیم می‌کند، ساختار مورد نیاز روی سرور را آماده می‌کند، اینباندها و اوتباندهای لازم را می‌سازد، گواهی‌های مورد نیاز را مدیریت می‌کند و در پایان لینک‌های اتصال آماده را در اختیار شما قرار می‌دهد.
تمام مراحل به شکلی طراحی شده‌اند که کاربر نیازی به درگیر شدن با جزئیات پیچیده کانفیگ سرور نداشته باشد. هدف ما این است که راه‌اندازی یک سرور شخصی، از مرحله اتصال دامنه تا دریافت کانفیگ‌های نهایی، تا حد ممکن ساده، سریع و قابل فهم شود.
WhiteDNS برای کسانی ساخته شده که می‌خواهند کنترل سرور خودشان را داشته باشند، اما نمی‌خواهند زمان زیادی صرف یادگیری تنظیمات فنی، خطاهای رایج، مدیریت DNS یا ساخت دستی کانفیگ‌ها کنند.
این پروژه قدمی دیگر در مسیر ما برای آسان‌تر کردن دسترسی به ابزارهای کاربردی، مستقل و قابل مدیریت برای کاربران است.
https://github.com/iampedii/WhiteDNS-Wizard/releases/tag/v1.0.0</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/whitedns/934" target="_blank">📅 19:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سلام خدمت دوستان عزیز،
ما سرورها رو آپدیت کردیم و با همکاری جدیدی که شروع شده، از این به بعد ساب‌ها رو مرتب با کانکشن‌های جدید و تازه‌تر رفرش می‌کنیم تا کیفیت اتصال بهتر و پایدارتر بشه.
اگر این دامنه‌ها هم فیلتر بشن، لینک‌های جدید ساب رو براتون می‌سازیم و منتشر می‌کنیم.
لطفاً این لینک‌ها رو تست کنید و نتیجه رو در کامنت‌ها بگید. اگر لینکی فیلتر بود یا مشکل داشت، اطلاع بدید تا جایگزین کنیم.
لینک ساب برای Clash Party / Mi Clash / FLClash:
https://sub.iampedi4.live/sub/mihomo.yaml
لینک ساب برای اپ‌های V2Ray:
https://sub.iampedi4.live/sub/base64.txt
آموزش استفاده از FlClash
آموزش استفاده از Clash Party
ممنون از همراهی شما
🤍
محتوای همه‌ی ساب‌ها یکی هست و فقط دامنه‌های جدید اضافه شده‌اند، چون دامنه‌ی قبلی فیلتر شده بود.
ساب گیتهاب فعلا آپدیت نخواهد شد.</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/whitedns/933" target="_blank">📅 18:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوستان عزیز WhiteDNS
🔥
اگر از WhiteDNS Sub استفاده می‌کنید و اخیراً احساس کردید کیفیت بعضی از کانکشن‌ها افت کرده، لطفاً بدونید که موضوع در حال پیگیریه.
ما در حال بررسی و بهبود وضعیت کانکشن‌ها هستیم و به‌زودی یک کانفیگ های بروز رو منتشر می‌کنیم.
خوشبختانه همکار هایی پیدا کردیم که می‌توانند در این مسیر کنار ما باشند و کمک کنند تا کیفیت و پایداری سرویس بهتر باشه.
به‌زودی آپدیت جدید روی Subscription قرار می‌گیره و اطلاع‌رسانی می‌کنیم.
ممنون از صبر، همراهی و حمایت همیشگی‌تون
🤍
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/whitedns/932" target="_blank">📅 14:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">در ادامه فیلتر شدن دامنه ما، دامنه جدید برای ساب آماده کردیم.
محتوی همه ساب ها یکی هستش، فقط دامنه جدید اضافه کردیم چون قبلی فیلتر شده.
تا فردا هم فیلتر کنن
(
🖕
)
ما لینک ساب جدید میسازیم  براتون
لطفا این رو تست کنید و نتیجه رو در کامنت ها بگید. اگر فیلتر بود یکی دیگه میسازیم.
🔥
لینک ساب جدید
https://sub.iampedi2.live/sub/mihomo.yaml
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/whitedns/931" target="_blank">📅 05:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دوستان و همراهان عزیز، سلام
🌺
لطفاً چند لحظه وقت بگذارید و این پیام مهم را در خصوص
نحوه ارتباط با ادمین‌ها
مطالعه کنید.
آیدی ادمین که در توضیحات (بایو) کانال قرار داده شده،
فقط و فقط
برای موارد خاص زیر است:
🔸
گزارش تخلفات
🔸
پیشنهادات همکاری در زمینه‌های مختلف
⚠️
لطفاً به این نکات توجه ویژه داشته باشید:
۱.
سوالات خود را در گروه بپرسید:
تمامی سوالات و مشکلات فنی باید فقط در
گروه‌های ما
مطرح شوند. لطفاً از ارسال پیام خصوصی (پی‌وی) به ادمین‌ها خودداری کنید. ما تیم پشتیبانی مجزایی نداریم که بتواند روزانه به صدها پیام خصوصی به‌صورت تک‌به‌تک پاسخ دهد.
۲.
توقع پاسخگویی در موارد نامربوط:
متاسفانه روزانه پیام‌های بی‌ربط زیادی دریافت می‌کنیم و در کمال تعجب، برخی از دوستان در صورت عدم دریافت پاسخ شاکی شده و حتی تهدید می‌کنند!
برای روشن شدن موضوع، به طور مثال
موارد زیر در تخصص ما نیست
و از پاسخگویی به آن‌ها در پیام خصوصی معذوریم:
❌
رفع مشکلات کامپیوتر، موبایل و یا خرابی مودم خانگی شما (برای این موارد به متخصصین شهر خود مراجعه کنید).
❌
مشاوره برای خرید تجهیزات سخت‌افزاری (مثل قطعی کابل شبکه و اینکه چه کابلی بخرید).
❌
آموزش خرید رمزارز و معرفی صرافی‌های مناسب.
❌
و هزاران مورد نامربوط دیگر که خارج از حوزه فعالیت ماست.
🙏
خواهشمندیم با رعایت این موارد، از ارسال پیام‌های خارج از موضوع به ادمین‌ها جداً خودداری فرمایید تا بتوانیم در موارد ضروری پاسخگوی شما عزیزان باشیم.
از درک و همراهی شما سپاسگزاریم
🌹</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/whitedns/929" target="_blank">📅 16:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⚠️
⚠️
⚠️
#موقت
⚠️
هر پیام اضافه، سؤال، بحث یا محتوایی غیر از نام سرور زیر این پست، باعث بن شدن خواهد شد.   سلام به همه دوستان عزیز  برای بررسی وضعیت اتصال، نیاز داریم یک تست همگانی انجام بدیم تا مشخص بشه در حال حاضر کدام متدها و سرورها برای شما وصل هستند. …</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/whitedns/927" target="_blank">📅 08:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⚠️
⚠️
⚠️
#موقت
⚠️
هر پیام اضافه، سؤال، بحث یا محتوایی غیر از نام سرور زیر این پست، باعث بن شدن خواهد شد.
سلام به همه دوستان عزیز
برای بررسی وضعیت اتصال، نیاز داریم یک تست همگانی انجام بدیم تا مشخص بشه در حال حاضر کدام متدها و سرورها برای شما وصل هستند.
لطفاً قبل از تست، ساب خودتون رو یک‌بار Refresh / Update کنید.
برای شرکت در این تست:
به سابسکریپشن WhiteDNS وصل باشید.
داخل اپلیکیشن موبایل یا کامپیوتر وارد بخش Logs / لاگ‌ها شوید.
نام سروری که به آن وصل شده‌اید را زیر همین پست برای ما ارسال کنید.
لطفاً فقط نام سرور را ارسال کنید.
اگر نمی‌دانید دقیقاً باید چه کاری انجام دهید، مشکلی نیست؛ می‌توانید در این تست شرکت نکنید.
ممنون از همکاری شما
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/whitedns/926" target="_blank">📅 07:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">لینک ساب ها درست شدند
😃
🔗
لینک ساب WhiteDNS برای FlClash:
https://sub.whitedns.one/sub/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://sub.whitedns.one/sub/base64.txt
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/whitedns/925" target="_blank">📅 04:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">متأسفانه سروری که برای اسکن و بررسی کانفیگ‌ها استفاده می‌کردیم، به‌دلیل حجم بالای اسکن‌ها، از سمت ارائه‌دهنده به‌عنوان رفتار مشکوک یا سوءاستفاده شناسایی شده و دسترسی آن محدود شده است
😣
در حال بررسی و رفع مشکل هستیم و تلاش می‌کنیم سرویس اسکن را هرچه زودتر دوباره پایدار کنیم.
تا زمانی که این مشکل برطرف شود، می‌توانید از ساب‌های GitHub استفاده کنید؛ اما فعلاً امکان ارسال آپدیت‌های جدید از سمت ما وجود ندارد.
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/whitedns/923" target="_blank">📅 17:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تیم WhiteDNS از ابتدا با هدف کمک به کاربران فعالیت کرده و تمام خدماتی که ارائه داده‌ایم، رایگان بوده و رایگان باقی خواهد ماند.
در این مسیر سخت، تعدادی از شما عزیزان با کمک‌های مالی خود از ما حمایت کرده‌اید. چه کمک‌های کوچک و چه مبالغ بزرگ‌تر، برای ما بسیار ارزشمند بوده و واقعاً دلگرم‌کننده است. همین حمایت‌ها نشان می‌دهد که این مسیر برای خیلی‌ها مهم است و ما بابت این همراهی صمیمانه از شما سپاسگزاریم.
مبلغ کل حمایت از ما تاحالا حدود ۵۰دلار بوده است.
متأسفانه اخیراً کیف پولی که برای دریافت کمک‌ها استفاده می‌کردیم، شروع به مسدود کردن یا محدود کردن تراکنش‌های مربوط به ایران کرده است.
به همین دلیل، از شما خواهش می‌کنیم تا زمانی که راه‌حل امن و مناسبی پیدا کنیم، فعلاً برای ارسال کمک مالی اقدام نکنید.
قدردان محبت، اعتماد و حمایت ارزشمند شما هستیم.
با سپاس فراوان
تیم whiteDNS</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/whitedns/921" target="_blank">📅 16:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔥
اگر محتوای WhiteDNS برای شما مفید بوده، با Subscribe کردن کانال یوتیوب ما می‌توانید از ادامه فعالیت‌های ما حمایت کنید
.
https://youtube.com/@whitedns</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/whitedns/920" target="_blank">📅 15:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-917">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/917" target="_blank">📅 11:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دوستان نگران نباشید، ما ۱۰۰۰ تا دامنه خریدیم این مدت برای سرویس های DNSTT & MasterDNS
تا فردا هم فیلتر کنن
(
🖕
)
ما لینک ساب جدید میسازیم  براتون
لطفا این رو تست کنید و نتیجه رو در کامنت ها بگید. اگر فیلتر بود یکی دیگه میسازیم.
لینک ساب جدید
http://sub.iampedi1.live/sub/mihomo.yaml
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
نکته، تمام آدرس های قبل کار خواهند کرد. ساب گیتهاب و تمام این ساب ها و ساب های آینده یک محتوی خواهند داشت.</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/whitedns/916" target="_blank">📅 11:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">📌
چند نکته کاربردی برای بهتر وصل شدن با FlClash در اندروید
یکی از کاربران WhiteDNS تجربه‌ی شخصی خودش را از کار با FlClash فرستاده که برای اتصال بهتر مؤثر بوده.
اگر با FlClash مشکل اتصال، آپدیت نشدن ساب، پینگ‌های عجیب یا ناپایداری دارید، این موارد را امتحان کنید.
━━━━━━━━━━━━━━
1️⃣
بعد از نصب، قبل از اضافه کردن ساب، Resourceها را آپدیت کنید
بعد از نصب FlClash، قبل از اینکه لینک سابسکریپشن را اضافه کنید، وارد این بخش شوید:
Tools → Resource
و تمام Resourceها را آپدیت کنید.
⚠️
نکته مهم:
طبق تجربه‌ی بعضی کاربران، اگر اول لینک ساب را اضافه کنید، ممکن است بعداً Resourceها درست آپدیت نشوند یا اپ رفتار عجیب نشان بدهد.
━━━━━━━━━━━━━━
2️⃣
تنظیمات Network
از بخش Network این موارد را بررسی کنید:
✅
گزینه‌ی DNS Hijack را فعال کنید.
❌
گزینه‌ی
Allow applications to bypass VPN
را غیرفعال کنید.
این کار کمک می‌کند برنامه‌ها ترافیک یا DNS را از بیرون VPN رد نکنند.
━━━━━━━━━━━━━━
3️⃣
تنظیمات دسترسی و اجرای پس‌زمینه
بعد از نصب وارد این مسیر شوید:
Tools → Advanced Configuration → On Demand
در این بخش، گزینه‌های مربوط به دسترسی‌ها را روی Authorized قرار دهید.
همچنین در تنظیمات باتری گوشی، برای FlClash حالت Battery Optimization را غیرفعال کنید تا اندروید برنامه را در پس‌زمینه نبندد.
━━━━━━━━━━━━━━
4️⃣
گوشی روی Power Saving نباشد
اگر گوشی روی حالت
Power Saving / Battery
Saver باشد، ممکن است اتصال ناپایدار شود یا برنامه در پس‌زمینه قطع شود.
برای استفاده بهتر از FlClash، هنگام اتصال، حالت Power Saving را خاموش کنید.
━━━━━━━━━━━━━━
5️⃣
تنظیمات DNS
از بخش DNS:
✅
گزینه‌ی Override DNS را فعال کنید.
🌍
گزینه‌ی GeoIP Code را روی IR قرار دهید.
بعد از این تغییرات، لینک ساب را اضافه کنید و تست پینگ بگیرید.
━━━━━━━━━━━━━━
6️⃣
اگر ساب آپدیت نمی‌شود، حذف و دوباره اضافه کنید
طبق تجربه‌ی بعضی کاربران، FlClash گاهی نشان می‌دهد که ساب آپدیت شده، اما در عمل لیست کانفیگ‌ها تغییر نکرده است.
اگر حس کردید ساب درست آپدیت نشده:
1. لینک ساب را حذف کنید.
2. دوباره همان لینک را اضافه کنید.
3. مجدد پینگ بگیرید و تست اتصال انجام دهید.
━━━━━━━━━━━━━━
7️⃣
در تب Auto کمی صبر کنید
طبق تجربه‌ی کاربر، بعد از حذف و اضافه کردن دوباره‌ی ساب و گرفتن پینگ در تب Auto، ممکن است اول فقط چند سرور پینگ بدهند و بقیه Timeout شوند.
اما بعد از اولین اتصال، FlClash ممکن است خودش شروع کند سرورها را دوباره بررسی کند و از بالای لیست Auto دونه‌دونه سرورها را تست کند تا به گزینه‌ی بهتر برسد.
یعنی ممکن است اول یک سرور اصلاً پینگ ندهد یا در لیست بالا نباشد، اما بعد از اولین اتصال، همان سرور یا سرورهای دیگر دوباره تست شوند و وصل شوند.
⏳
گاهی این روند کمی زمان می‌برد، پس اگر همان لحظه همه‌چیز Timeout بود، چند دقیقه صبر کنید و دوباره وضعیت را بررسی کنید.
━━━━━━━━━━━━━━
8️⃣
مرتب‌سازی سرورها بر اساس پینگ
برای اینکه سرورهایی که پینگ گرفته‌اند بالای لیست بیایند، روی سه‌نقطه بزنید و وارد این مسیر شوید:
⋮ → Settings → Sort → Delay
با این کار، سرورهایی که پینگ بهتری دارند بالاتر نمایش داده می‌شوند و انتخاب سرور راحت‌تر می‌شود.
━━━━━━━━━━━━━━
✅
ترتیب پیشنهادی بعد از نصب FlClash
1. نصب FlClash
2. آپدیت Resourceها از بخش Tools → Resource
3. فعال کردن DNS Hijack
4. غیرفعال کردن Allow applications to bypass VPN
5. فعال کردن Override DNS
6. تنظیم GeoIP Code روی IR
7. غیرفعال کردن Battery Optimization برای FlClash
8. خاموش بودن Power Saving گوشی
9. اضافه کردن لینک ساب
10. رفتن به تب Auto و گرفتن پینگ
11. تنظیم Sort روی Delay
12. اتصال و چند دقیقه صبر برای تست خودکار سرورها
━━━━━━━━━━━━━━
⚠️
این تنظیمات تضمینی نیست، چون شرایط اینترنت، اپراتور و گوشی‌ها متفاوت است؛ اما برای بعضی کاربران باعث اتصال بهتر و پایدارتر شده است.
🔗
لینک ساب WhiteDNS برای FlClash:
https://sub.whitedns.one/sub/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://sub.whitedns.one/sub/base64.txt
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/whitedns/915" target="_blank">📅 10:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69013b2789.mp4?token=XWzqlDJUfiYVKG-aFn3y9FdOLsGJuMaefjEbn27HQjBMCjxgIECYPLzvhoZI6ees7QX4H3gD7uf-bDLDbVkMtv5pYmGnxV141yFw-l9S45Aan2yXXz3jobE5pKQBGQnEsbxR0uCrCIDR1s_sLRL3RHdax2J44qKUuezNjjQXD8-nFqJajS5yJBEioEI2BTQj56oiR-8oB4j3sj5g3cxk0OwL6JHSxitTi21QuXv6keBrByTGjtCGPmCLeOuf5hDC1f8nRrFdrVcNtI1RFi2rOaPpnwpbvLcPXIZAqDcsNNRtpwLYr4vP2UNlidOrsMfJgeSxzZmob-OISd9sroQT9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69013b2789.mp4?token=XWzqlDJUfiYVKG-aFn3y9FdOLsGJuMaefjEbn27HQjBMCjxgIECYPLzvhoZI6ees7QX4H3gD7uf-bDLDbVkMtv5pYmGnxV141yFw-l9S45Aan2yXXz3jobE5pKQBGQnEsbxR0uCrCIDR1s_sLRL3RHdax2J44qKUuezNjjQXD8-nFqJajS5yJBEioEI2BTQj56oiR-8oB4j3sj5g3cxk0OwL6JHSxitTi21QuXv6keBrByTGjtCGPmCLeOuf5hDC1f8nRrFdrVcNtI1RFi2rOaPpnwpbvLcPXIZAqDcsNNRtpwLYr4vP2UNlidOrsMfJgeSxzZmob-OISd9sroQT9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو آموزشی فعال سازی Fragment در اپلیکیشن V2Ray در موبایل و دستکتاپ</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/whitedns/911" target="_blank">📅 02:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سلام خدمت همگی،
دوستانی که از همراه اول یا سایر اپراتورها استفاده می‌کنند و اخیراً با مشکل اتصال مواجه شده‌اند،
بر اساس تست‌های انجام‌شده، به نظر می‌رسد در روزهای اخیر روی برخی اپراتورها، از جمله همراه اول، DPI سنگین‌تری نسبت به قبل اعمال شده است.
به همین دلیل پیشنهاد می‌کنیم اگر با اتصال مشکل دارید، گزینه
Fragment
را در تنظیمات اپلیکیشن‌های زیر فعال کنید:
V2Ray
FlClash
Clash Party
Mi Clash
گزینه Fragment می‌تواند در بعضی شرایط به عبور از DPI و بهتر شدن اتصال کمک کند، مخصوصاً زمانی که اتصال روی برخی اپراتورها سخت‌تر شده یا کانفیگ‌ها دیر وصل می‌شوند.
اما توجه داشته باشید که فعال‌کردن Fragment همیشه به معنی افزایش سرعت نیست. در بعضی موارد ممکن است باعث کندتر شدن اتصال اولیه، افزایش جزئی پینگ، کاهش سرعت در بعضی کانفیگ‌ها، ناپایدار شدن برخی سرورها یا مصرف پردازشی و باتری کمی بیشتر در موبایل شود.
بنابراین پیشنهاد ما این است:
اگر اتصال شما مشکل دارد، کانفیگ‌ها وصل نمی‌شوند یا اتصال ناپایدار است، Fragment را فعال کنید و تست بگیرید.
اما اگر اتصال شما بدون مشکل و پایدار کار می‌کند، الزامی به فعال‌کردن Fragment نیست.
به‌زودی آموزش ویدیویی فعال‌سازی Fragment برای هرکدام از این اپلیکیشن ها ارسال میکنیم.
ممنون
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/whitedns/910" target="_blank">📅 02:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اپلیکیشن‌هایی مثل FlClash و Clash Mi چطور کار می‌کنند؟
اپلیکیشن‌هایی مثل
FlClash
در اندروید و
Clash Mi
در آیفون، برنامه‌هایی هستند که به شما کمک می‌کنند راحت‌تر به کانفیگ‌های مختلف وصل شوید.
فرق اصلی این برنامه‌ها با بعضی از اپلیکیشن‌های دیگر این است که لازم نیست تعداد زیادی کانفیگ را یکی‌یکی وارد کنید و هر بار دستی تست کنید کدام وصل می‌شود.
شما فقط یک لینک سابسکریپشن وارد می‌کنید. بعد از آن، برنامه خودش لیست کانفیگ‌ها را دریافت می‌کند، آن‌ها را بررسی می‌کند و بر اساس تنظیمات، بهترین گزینه را برای اتصال انتخاب می‌کند.
مثلاً وقتی شما لینک سابسکریپشن WhiteDNS را داخل برنامه وارد می‌کنید، برنامه یک لیست از کانفیگ‌های آماده را دریافت می‌کند. سپس می‌تواند از بین آن‌ها، کانفیگی را انتخاب کند که در آن لحظه بهتر کار می‌کند.
آیا این برنامه‌ها هم‌زمان به چند سرور وصل می‌شوند؟
معمولاً نه.
این برنامه‌ها معمولاً برای هر اتصال، یک کانفیگ یا یک سرور را انتخاب می‌کنند. یعنی سرعت اینترنت شما با وصل شدن هم‌زمان به چند سرور مختلف ترکیب نمی‌شود.
اما برنامه می‌تواند چند کار مهم انجام دهد:
کانفیگ‌های مختلف را تست کند
کانفیگ خراب را کنار بگذارد
بین کانفیگ‌های سالم، گزینه بهتر را انتخاب کند
اگر یک کانفیگ قطع شد، سراغ گزینه بعدی برود
مسیر بعضی سایت‌ها و برنامه‌ها را از پراکسی عبور دهد و بعضی‌ها را مستقیم باز کند
برای همین استفاده از این برنامه‌ها معمولاً راحت‌تر از وارد کردن دستی تعداد زیادی کانفیگ است.
فرق FlClash و Clash Mi با برنامه‌هایی مثل V2Ray چیست؟
در برنامه‌هایی مثل V2Ray، معمولاً شما یک کانفیگ را وارد می‌کنید، همان را انتخاب می‌کنید و به همان وصل می‌شوید.
اما در برنامه‌هایی مثل FlClash و Clash Mi، شما معمولاً یک لیست کامل از کانفیگ‌ها را وارد می‌کنید. بعد برنامه می‌تواند بین آن‌ها انتخاب کند و بر اساس قوانین مختلف، ترافیک اینترنت شما را مدیریت کند.
به زبان ساده:
V2Ray یعنی: این کانفیگ را بگیر و به آن وصل شو.
FlClash و Clash Mi یعنی: این لیست کانفیگ‌ها را بگیر، تست کن، بهترین گزینه را انتخاب کن و اینترنت را هوشمندتر مدیریت کن.
حالت‌های Direct، Global و Rule یعنی چه؟
در این برنامه‌ها معمولاً چند حالت اتصال وجود دارد:
Direct
یعنی اینترنت بدون پراکسی و مستقیم از اینترنت معمولی شما رد می‌شود.
Global
یعنی تقریباً همه ترافیک اینترنت از یک کانفیگ یا سرور عبور می‌کند.
Rule
یعنی برنامه خودش بر اساس قوانین تصمیم می‌گیرد کدام سایت یا برنامه از پراکسی رد شود و کدام مستقیم باز شود.
برای بیشتر کاربران، حالت
Rule
بهترین گزینه است، چون برنامه هوشمندتر رفتار می‌کند.
چرا استفاده از سابسکریپشن بهتر است؟
وقتی از سابسکریپشن استفاده می‌کنید، دیگر لازم نیست هر بار چندین کانفیگ را دستی کپی و وارد کنید.
کافی است یک لینک وارد کنید و بعد از آن، برنامه خودش لیست جدید را دریافت می‌کند.
اگر لیست به‌روزرسانی شود، برنامه هم می‌تواند کانفیگ‌های جدیدتر را دریافت کند.
این یعنی استفاده راحت‌تر، مدیریت بهتر و دردسر کمتر برای کاربر.
خلاصه خیلی ساده
اپلیکیشن‌هایی مثل FlClash و Clash Mi برای این ساخته شده‌اند که کاربر مجبور نباشد بین ده‌ها یا صدها کانفیگ سردرگم شود.
شما یک لینک سابسکریپشن وارد می‌کنید، برنامه لیست کانفیگ‌ها را می‌گیرد، آن‌ها را مدیریت می‌کند و کمک می‌کند راحت‌تر به گزینه مناسب وصل شوید.
این برنامه‌ها معمولاً چند سرور را با هم ترکیب نمی‌کنند تا سرعت چند برابر شود، اما می‌توانند اتوماتیک و یا در حین اتصال کانفیگ‌های خراب را کنار بگذارند و اتصال پایدارتری ایجاد کنند</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/whitedns/909" target="_blank">📅 17:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">📱
اگر لینک ساب WhiteDNS رو میخواید از گیتهاب داشته باشید، این ریپو هر ۴۰ دقیقه با بهترین سرور ها آپدیت میشه  https://github.com/iampedii/whitedns-sub   لینک ساب برای Clash Party & FLClash https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/whitedns/908" target="_blank">📅 17:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-907">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔥
اگر محتوای WhiteDNS برای شما مفید بوده، با Subscribe کردن کانال یوتیوب ما می‌توانید از ادامه فعالیت‌های ما حمایت کنید
.
https://youtube.com/@whitedns</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/whitedns/907" target="_blank">📅 14:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ما هر ۴۰ دقیقه ساب رو آپدیت میکنیم. شما هم یک آپدیت توی اپ بزنید تا بهترین کانفیگ هارو بگیرید.</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/whitedns/905" target="_blank">📅 13:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">📱
اگر لینک ساب WhiteDNS رو میخواید از گیتهاب داشته باشید، این ریپو هر ۴۰ دقیقه با بهترین سرور ها آپدیت میشه
https://github.com/iampedii/whitedns-sub
لینک ساب برای Clash Party & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
@WhiteDNS</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/whitedns/904" target="_blank">📅 13:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سلام خدمت همگی  از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:  اندروید: FlClash آیفون: Clash Mi  با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.  ما در سرورهای WhiteDNS بخشی از…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/whitedns/903" target="_blank">📅 13:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-901">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">😊
آموزش استفاده از Clash Party نسخه ویندوز در کانال یوتیوب WhiteDNS
🔥
کانال مارو Subscribe داشته باشید.
https://youtu.be/gMFH88yRghg</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/whitedns/901" target="_blank">📅 12:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آموزش استفاده از FLClash
ممنون از رضا عزیز
@WhiteDNS</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/whitedns/898" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⚠️
برای وارد کردن ساب باید به یک وی‌پی‌ان  متصل باشید</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/whitedns/897" target="_blank">📅 10:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سلام خدمت همگی  از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:  اندروید: FlClash آیفون: Clash Mi  با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.  ما در سرورهای WhiteDNS بخشی از…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/whitedns/896" target="_blank">📅 10:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-893">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvvlxdHYyhuoFQAd47D8D7TmWuGjZIDiE4V4HfAYvqR5ej64-j5ibPWVwlM9BmoT1Vr8aYMBrciJpc8oopkOV9XFawOfuCKGQKAsDZwbtCbtlfM-lxlJdJlCBVplzJGNyWeFlrDlk64J3YbOcWTf2GqnHR8tNZjhbeYmMurlRXRkDRzA7WuZyvoioJM6-3QqmyUIzObLmHzSQkgfw3ZZ0FT39bKZfP8WFyK9ncGt8BHoQxFcDTb5TnoXWdPRsDDwTL69waH_XN9F7_I088fu7tSYAih6XKHtScEb4KBsSlHulJvnPX_Fjzt_XGgPVBeEMdZwZTQAUv0EfYcuZLPVJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی
از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:
اندروید: FlClash
آیفون: Clash Mi
با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.
ما در سرورهای WhiteDNS بخشی از کانفیگ‌ها را بررسی و فیلتر می‌کنیم. سپس اپلیکیشن موبایل به‌صورت خودکار از بین کانفیگ‌های باقی‌مانده، بهترین گزینه‌ها را انتخاب کرده و به آن‌ها متصل می‌شود.
لینک WhiteDNS Sub برای استفاده در این اپلیکیشن‌ها:
http://sub.iampedi1.live/sub/mihomo.yaml
لیست سابسکریپشن ما هر ۱ ساعت یک‌بار به‌روزرسانی می‌شود.
دانلودFLClash برای اندروید، مک، لینوکس و ویندوز
https://flclash.cc/en/download
با تشکر
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/whitedns/893" target="_blank">📅 10:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89b2fd3cd.mp4?token=u8EJM5GcglBks8446QavKqHtvzJp125KqqNg6mkjY00u0gOVZZhVGuepHQoTkXAXeeqNekvZ4IoJjNlxgHTplW5Z5dePj4i8YgOWNfrH7SEwWB8oK76IR4jexZmo2ErFap8R_ITV2paXIMeTY4GagClHQZ2hRGMbqr3l-cyo3Ok3kbAegfrAPPc3JDRAGDuqt15yoEWd0NL2RBPKujOhV1bL0IQOK7ll4LpvsQhpDkYVBMmOpv_QfwBZNfPUD3s6S0oIpdiNvqQUF80BpIK6k9aUWPTGoRdItf7Zkny8Nv40GE5UbfU_XxeS_2reAAUie_y8Z2QoHNzKqBIGhI5_Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89b2fd3cd.mp4?token=u8EJM5GcglBks8446QavKqHtvzJp125KqqNg6mkjY00u0gOVZZhVGuepHQoTkXAXeeqNekvZ4IoJjNlxgHTplW5Z5dePj4i8YgOWNfrH7SEwWB8oK76IR4jexZmo2ErFap8R_ITV2paXIMeTY4GagClHQZ2hRGMbqr3l-cyo3Ok3kbAegfrAPPc3JDRAGDuqt15yoEWd0NL2RBPKujOhV1bL0IQOK7ll4LpvsQhpDkYVBMmOpv_QfwBZNfPUD3s6S0oIpdiNvqQUF80BpIK6k9aUWPTGoRdItf7Zkny8Nv40GE5UbfU_XxeS_2reAAUie_y8Z2QoHNzKqBIGhI5_Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همچنین کاربران نسخه دسکتاپ می‌توانند از قابلیت
تبدیل کانفیگ‌ها به IPهای سفید
به‌صورت مستقیم در داخل اپلیکیشن استفاده کنند.
🚀
Tools > V2Ray White IP Generator
@WhiteDNS
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور
🎬
کانال یوتیوب WhiteDNS</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/whitedns/885" target="_blank">📅 04:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsVj6i2KP5N7WFlVxPNrI6_f6qC_OUC-YU6DUj5mnHmJ5idWTwQtUasF5eBdz4cD94YPZCRwof0D9BYK9xBqRADpK9sJBrjRlerOy_AbKJ_ykNy2IkrGj1Q8omAN5D0HgRZ4nrS8K4jBxdvbiB5f3Uml9guSX_Hda85ysUQfbeTUXa8ozT1RkwLgBjgX_Qm0fjD05zhxDYLTLlkUE2sLjiyK6bTtMDk4bKnvbUxF1ikSbOCGrwq1INVIydMbVY2RyyiN-qMCudKoVoTcuntwVrtLEHYnwjPCWCIKugiQFNJMaGGM_9VKOcL5B8Bifv1BaiTIoXcNhJ-CxyWggVym6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش تبدیل کانفیگ به آی‌پی سفید
از این به بعد برای تبدیل کانفیگ، آی‌پی‌های خودتان استفاده می‌شود.
@WhiteDNS_Installer_bot
مراحل کار:
1. وارد ربات شوید.
2. روی گزینه «تبدیل کانفیگ با آی‌پی سفید» بزنید.
3. کانفیگ V2Ray خود را ارسال کنید.
فرمت‌های پشتیبانی‌شده:
VLESS
VMess
Trojan
بعد از تایید کانفیگ، ربات از شما لیست آی‌پی‌ها را می‌خواهد.
می‌توانید آی‌پی‌ها را به این شکل بفرستید:
8.8.8.8
104.18.1.1:8443
یا با کاما:
1.1.1.1, 8.8.8.8, 104.18.1.1:8443
نکته مهم:
اگر پورت وارد نکنید، پورت پیش‌فرض 443 استفاده می‌شود.
اگر آی‌پی را همراه پورت بفرستید، همان پورت استفاده می‌شود.
مثال:
1.1.1.1
→  پورت 443
1.1.1.1:2053
→  پورت 2053
در پایان، ربات فایل کانفیگ جدید را برای شما ارسال می‌کند که host و port آن با آی‌پی‌های ارسالی خودتان جایگزین شده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/whitedns/883" target="_blank">📅 03:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سلام خدمت همگی
❤️
الان تنها راه اتصال پایدار و بی‌دردسر اینه که شما یکبار اسکن کنید، آی‌پی مناسب پیدا کنید و بذارید جلوی کانفیگ‌هاتون.   متاسفانه فرمول یکسانی وجود نداره که برای همه کار کنه.   این روش رو میتونید برای کانفیگ‌های رایگانی که از ربات ما هم دریافت…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/whitedns/882" target="_blank">📅 02:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/whitedns/881" target="_blank">📅 02:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر:
https://t.me/MatinSenPaii/3598
پنل BPB روی گیتهاب:
https://github.com/bia-pain-bache/BPB-Worker-Panel
پروژه اسکنر روی گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner
پروژه رسول:
https://github.com/seramo/v2ray-config-modifier
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- ساخت پنل BPB ورژن جدید
2- رفع مشکل پینگ -1 کانفیگ‌های آپدیت جدید و درست کردن تنظیمات کلودفلر برای کار کردن پنل
3- استفاده از اسکنر SenPai Scanner برای اسکن آیپی تمیز کلودفلر با استفاده از کانفیگ‌های Worker
4- استفاده از پروژه رسول برای انداختن آیپی تمیز به تعداد بالا پشت کانفیگ
5- توضیح حجم مصرفی و استفاده از این روش روی کلاینت‌های متفاوت
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز هیچ سرور و دانش شبکه‌ای نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/whitedns/880" target="_blank">📅 02:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwVri8mpi2kxGWqRZ2fL7NkTXfPQ9VhG_vS1jMnCOF6-kVQ7joV_BaQVlw5QXAK4_vRWGeqPoQqPp9xJqlZZpEjHPK_l_DP8vKRrnrv9MeVrLmFqJAF4YwLHh6Rkx5p7-FXPGyIjIqZcqNmMrH8thxoP1Tw39EiOXoavDd9R4khI3SCJc04t7L1jz_ICtC8FWvRaevF1pu-4EJSsMJvC4sZdwBmqn7TpIePTg0GyyOCwrXwoW4PaholtRUERCspkmeYRJGVJlzI_optU402fAPRP8JLIC6oUXhjjmibORfv74ztQrCoVG4EWyy8MRhAb1yf29QEklVUrXYlip__jDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در شرایط سخت و روزهای «خاموشی دیجیتال»، تلاش کردیم با ساخت ابزارهای مختلف، آموزش‌های کاربردی و راهکارهای ساده‌، کنار مردم باشیم و کمک کنیم تا حداقل دسترسی آزاد به اینترنت حفظ شود.
اگر در تمام این مسیر فقط توانسته باشیم یک نفر را دوباره به اینترنت آزاد جهانی وصل کنیم، برای ما ارزشمند و افتخارآمیز است.
اولویت و هدف تیم WhiteDNS همیشه ساده‌تر کردن ابزارهای پیچیده و تسهیل در دسترسی به آموزش بوده تا به هموطنانمان کمک کند وابستگی به بازار سیاه، واسطه‌ها و مافیای VPN کمتر شود؛ با این نگاه که هر شخص قادر باشد ابزارها و اتصال‌های امن خود را بهتر شناخته، بسازد و مدیریت کند.
امیدواریم هرچه زودتر شرایط بهتر شود و حق اولیه و ساده‌ی دسترسی آزاد به اینترنت دوباره به همه‌ی مردم برگردد.
از تمام اعضای تیم WhiteDNS و تمام وطن‌دوستانی که در این روزهای سخت کنار مردمشان ایستادند، صمیمانه تشکر می‌کنیم.
دم همه‌تون گرم
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/whitedns/879" target="_blank">📅 15:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-878">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdD8R4pe7GT5CYr_0xgSbm9sj2k0CMohG4zR7IaPM7XD39nPR5QahKvZAmLOI563HffwvBOupjlNNnhQx8pn3kAxd0Rp3dV01HeeYcAbKL5kLD8TYNCprDctlOHiGh84bBz5HIeFhOx7-FHdYcKNrx_lxmw0Q13r3Vy8JtydKIa3Qo8_dITqtZCPCVayC9EQY3PTFX4G-qoBCnpqz_XqerLXMfO-e30hVVIm3jguCMVj6TytHPxhqJwlIhQeTJHr5b3n1zqfFhTXDraX8SFv5oM5DXF4VK-l3ufVWVYi7Dk23wHf-1WYXssDfwGwpCM725eqqX1CPB5QFyzi6iXIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😊
آموزش V2Ray از صفر تا صد | نصب پنل، ساخت Inbound و Cloudflare Clean IP روی سرور شخصی
در این ویدیو نحوه نصب و راه‌اندازی پنل V2Ray روی سرور را به صورت کامل آموزش می‌دهیم. همچنین با نحوه ایجاد Inbound، مدیریت کاربران، استفاده از IPهای تمیز Cloudflare و اتصال کانفیگ‌ها از طریق اپلیکیشن WhiteDNS آشنا خواهید شد.
سرفصل‌های آموزش:
✅
نصب و راه‌اندازی پنل V2Ray
✅
ایجاد و مدیریت Inboundها
✅
ساخت و مدیریت کاربران
✅
آشنایی با تنظیمات مهم پنل
✅
استفاده از IPهای تمیز Cloudflare
✅
آموزش پیدا کردن و تست Cloudflare Clean IP
✅
آموزش استفاده از اپلیکیشن WhiteDNS برای قرار دادن کانفیگ‌های V2Ray پشت IPهای Cloudflare
✅
افزایش پایداری و کیفیت اتصال با WhiteDNS
✅
تست و بررسی عملکرد کانکشن‌ها
✅
نکات امنیتی و بهینه‌سازی تنظیمات
😊
لینک تماشا در یوتیوب
https://www.youtube.com/watch?v=vVjqNQBUGIc&feature=youtu.be
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور
🎬
کانال یوتیوب WhiteDNS</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/whitedns/878" target="_blank">📅 11:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-877">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🤩
آمورش کامل استفاده از اپ WhiteDNS در نسخه کامپیوتر  - آموزش استفاده از کانفیگ های MasterDNS  / StormDNS و اسکن کردن - آموزش استفاده از V2Ray  - آموزش استافده از Scanner, Validator, White IP Generator
⭐️
دانلود از لینک داخلی  https://guardts.ir/f/6f56591f7b7a…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/whitedns/877" target="_blank">📅 10:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-875">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">#موقت
ارسال شده در تاپیک سرور ها
سرور اهدایی از بامداد عزیز برای MasterDNS  قابل استفاده در  اپ WhiteDNS
🔑
Encryption Key
aaf4b6-@JavidnamanIran-aaf4b6fff
💻
Domains
: جداگانه امتحان کنید
b.bamak.xyz
b.igoii.org
b.namad.xyz
b.jnir.my
b.irdmc.com
b.javidnaman.com
Encryption Method
: XOR
🎞️
🎞️
🎞️
🎞️
🎞️
🎞️
🎞️
🎞️
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/whitedns/875" target="_blank">📅 04:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/whitedns/873" target="_blank">📅 02:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🤩
آمورش کامل استفاده از اپ WhiteDNS در نسخه کامپیوتر
- آموزش استفاده از کانفیگ های MasterDNS  / StormDNS و اسکن کردن
- آموزش استفاده از V2Ray
- آموزش استافده از Scanner, Validator, White IP Generator
⭐️
دانلود از لینک داخلی
https://guardts.ir/f/6f56591f7b7a
https://up.theazizi.ir/download.php?t=ecabdec17d6cbb16f37a13fe28c724cdb591
😊
مشاهده از یوتیوب
@WhiteDNS</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/whitedns/872" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔥</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/whitedns/870" target="_blank">📅 16:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اگر در اجرای نسخه مک مشکل خوردید دستور زیر رو اجرا کنید
xattr -cr "/Applications/WhiteDNS Desktop.app"</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/whitedns/869" target="_blank">📅 12:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-linux-amd64.deb</div>
  <div class="tg-doc-extra">19 MB</div>
</div>
<a href="https://t.me/whitedns/865" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
نسخه لینوکس</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/whitedns/865" target="_blank">📅 11:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-macos-amd64.zip</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/whitedns/861" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/whitedns/861" target="_blank">📅 11:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUunBcMVV08_yZF9ZkfY2CA3ulQVEIN8MrKBy6M1vem2xz1R6RXOR-2Bl9qr9YFntXpUZLvEj5jn7HzRcwziofrriETk498JSLZ8uPrK63WuMbio_gxh8jVZ7QHGn_WqRfc4zmKUibbjgdUI1cfVUt7EVBQjPFnzyVl04EDGoUfxoV6aE_hm8pYm9Klvjb-ZKugMZzkypFrTRDzmZ9mIAoPG4SIVOPYkFWXSqCbt2cpubFZefPsLVBCzS-TFNdPm2ZxPVQrvTlgEFN6QCIV5FO2aamnSAoSsyHN6Tm0s4mMwYwpmiHnJqCfCrKS8vWsf9aIH2hwwqIhMnSrP0HNpeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
انتشار نسخه v1.0.0-beta5 اپیلیکشن کامپیوتر WhiteDNS
⚪️
تغییر هسته از Sing-box به Xray
🔴
اضافه شدن امکان اسکن آی‌پی‌های شرکت‌های زیرساخت ایرانی. با این قابلیت، اگر رکوردهای A+، A یا B پیدا شوند، می‌توانید از آن آی‌پی‌ها به‌عنوان سرور برای کانفیگ‌های خودتان استفاده کنید. شما همچنین میتونید لیست خودتون رو برای اسکن وارد برنامه کنید.
⚪️
بازطراحی بخش کانکشن‌های V2Ray. این بخش حالا برای مدیریت تعداد زیادی کانفیگ مناسب‌تر شده است.
⚪️
اضافه شدن امکان Speed Test برای کانفیگ‌ها.
⚪️
اضافه شدن پشتیبانی از پروتکل‌های VLESS، VMess، Trojan، Shadowsocks، Hysteria2، WireGuard، SOCKS و HTTP Proxy.
⚪️
اضافه شدن قابلیت سفیدسازی کانفیگ‌ها. ابزار جدیدی در بخش Tools اضافه شده که با وارد کردن کانفیگ V2Ray، آن را به کانفیگ‌هایی پشت آی‌پی‌های سفید سرویس‌های مختلف تبدیل می‌کند. همچنین می‌توانید لیست آی‌پی‌های سفید دلخواه خودتان را وارد کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/whitedns/860" target="_blank">📅 11:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aofns9pIavcOADpbj65Qd8fYvlO8cbt8_YT3c4e5vpatzqtUY8_hOG0xyUW-YzzWz7KUw9bnDSYciwYy1TbjvdIQfcuAg2Lzp7lMpbEqVZCHUlcdPjx4AN5V2rqnCm5-ydeOiZtzLy2wDefUUFJKSFxdNTtMPH71VF-D5frw3xKjZNK7YUd-mk94eYnwJb40y420t39gXBrfLTOw_HDJXfUcTBQhd-d-kELur4k3xgnClMMnaWITFL7aKiqtkLFhWWWvV6q8i12Xe4plf6283CxtDJdLhiRx1C4XjaAfI20lllYvH7SFgC9ldW7uVrMPckSTjebIFuFFi2iWFoWfUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.
@WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر بشه و پایداری بهتری داشته باشید.
بعد از عادی شدن شرایط، تعداد خروجی‌ها کمتر و بهینه‌تر میشه.
⏳
همچنین بعد از ۲۴ ساعت می‌تونید دوباره درخواست جدید ثبت کنید و کانفیگ جدید بگیرید.
ممنون از حمایتتون
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/whitedns/859" target="_blank">📅 04:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">7.3 MB</div>
</div>
<a href="https://t.me/whitedns/852" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">راهنمای ورژن‌ها
تغییرات و بهبود‌ها:
- رفع کامل LOSS% اشتباه روی شبکه‌های محدود و DPI (مشکل اصلی کاربران). حالا تایم‌اوت بین Dial، TLS و HTTP به‌درستی تقسیم می‌شه و پکت‌لاس فیک کاملاً برطرف شد.
- ذخیره خودکار IPهای سالم بعد از Quick Scan و کپی در کلیپ‌بورد با زدن دکمه C
- خروجی فقط شامل IPهای سالم (بدون IPهای مرده)
- فرمت txt حالا ساده: فقط یک IP در هر خط( از
https://t.me/MatinSenPaii/3543
برای بازنویسی کانفیگ استفاده کنید)
- پیش‌فرض‌های هوشمندتر برای شبکه‌های محدود (تایم‌اوت ۵ ثانیه، دانلود ۶۴KB)
- کاهش تخصیص حافظه و فشار GC
- حذف IPهای تکراری در اسکن
- اسکریپت نصب یک‌خطی (شامل آپدیت و Termux برای اندروید)
- بهینه‌سازی منو و تمیزکاری کد
ممنون از همه Contributorها:
ProArash
،
M-logique
،
Mralimoh
،
Hoot-Code
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/whitedns/852" target="_blank">📅 04:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">☠️
پروژه‌ی SenPai Scanner — اسکنر IPهای Cloudflare   چی کار می‌کنه؟   از شبکه‌ات چند هزار IP از محدوده‌های رسمی Cloudflare رو تست می‌کنه، سریع‌ترین و سالم‌ترین‌ها رو پیدا می‌کنه تا توی کانفیگ V2Ray / Xray / Trojan بذاری.  چطور اجرا می‌شه؟   فقط فایل مخصوص…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/whitedns/851" target="_blank">📅 03:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-850">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YIYGgoet5iuQIkbV3bbwqFHbO34jDAfZAxQoyKEChUOhY7PWKbBbi9rhQ7qpmJ0nLUzyMm9mow8vrohSzVZQn0tvgQomPJB-_zMBmatYChKghcP0mM7z_B_K1fdmeTF3ZgIUprGu1e_yC5palHDJXd6ObaP7IWxWHsl2CLbf1YjWN0TXTwj-bJ3OshoEt3f5pHTRwnWr9nHoUANFbTMI706zgtsaxangApM2x5AdZuFjFRWP-0JT5HGQ9MdUVR9EpfQNgJAfReWEyXJxdRLPzf_G2E9lM0qUzjp8I4MWtT-cK1G-rK65sEYw4iWXOIl31Qdufy4Fa8ayUszra0FFPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
پروژه‌ی
SenPai Scanner
— اسکنر IPهای Cloudflare
چی کار می‌کنه؟
از شبکه‌ات چند هزار IP از محدوده‌های رسمی Cloudflare رو تست می‌کنه، سریع‌ترین و سالم‌ترین‌ها رو پیدا می‌کنه تا توی کانفیگ V2Ray / Xray / Trojan بذاری.
چطور اجرا می‌شه؟
فقط فایل مخصوص سیستم عاملت رو دانلود کن و اجرا کن.
۴ حالت اصلی:
⚙️
Quick Scan
— سریع: تعداد IP، تعداد worker و timeout رو انتخاب می‌کنی و اسکن شروع می‌شه (پیش‌فرض: حالت HTTP + تست واقعی داده)
⚙️
Custom Scan
— کامل: تعداد IP، پورت، محدوده CIDR، فیلتر دیتاسنتر (مثل FRA)، حالت tcp/tls/http، خروجی CSV/JSON/TXT
⚙️
Test IPs
— لیست IPهای خودت رو از فایل
ips.txt
عمیق‌تر تست می‌کنه
⚙️
Discover Colos
— می‌فهمی از شبکه‌ات به کدوم دیتاسنترهای Cloudflare دسترسی داری
چی اندازه می‌گیره؟
- تأخیر (latency) و jitter
- درصد packet loss
- در حالت HTTP: تأیید Cloudflare + شناسایی colo (مثل FRA، AMS)
- یک نمونه دانلود کوچک — تا گول IPی که «وصل می‌شه ولی داده نمی‌ده» رو نخوریم
نکته مهم:
این یه ابزار
پروکسی نیست
— فقط IPهای خوب رو پیدا می‌کنه. تست نهایی هنوز با همون کانفیگ واقعی‌ات روی Xray/V2Ray هست.
---
🎄
پلتفرم‌ها:
Linux · macOS · Windows
🔗
لینک پروژه:
https://github.com/MatinSenPai/SenPaiScanner
دانلود فایل‌ها از گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner/releases
دانلود فایلها از تلگرام:
https://t.me/MatinSenPaii/3526</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/whitedns/850" target="_blank">📅 03:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8SQn7KC1zSqCca5SgBrED3AFDQEN1IQJSB51iXSjRyg4EApsFxDr6vM7aeeIbXd7pjB_9y_oMdFeA01GpJVdQ6Diu_NTBpgovJW8P8Ig3pG3AbEPF8h0hz_pp5AMEzMcVMrgjCIymRvCSIbJfXt3hpI170Gn3E9skCTKZX-MkjuzH6JTYvaNe8p2JDFCiYmezgSkOuMjGDRvj_zXTp7Xs9Gwuj5vWwRmwes8gNx50p_7FazengmqTWE0PsEak2HLQJ3sv39FcdGj1mbUEw9l98HzQ-9igHdT9qA_netLViRfTI1rgGiY0MnSb9twlEmb7DlQAuF0KWiQ4GOCM7lDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرایط امروز اینترنت، دسترسی به کانفیگ ها برای برخی اپراتور ها امکان پذیر است و برای برخی نه. ولی راه حلی هست که امکان داره کانفیگ هایی که سالم هستند ولی پینگ نمیدهند رو هم به کار بندازید.
با امکان جدید ربات
@Whitedns_Installer_bot
میتونید کانفیگ V2Ray خودتون رو ارسال کنید و اون رو تبدیل به کانفیگ هایی پشت آی‌پی های سفید بکنید.
وارد ربات بشید، روی «تبدیل کانفیگ با آی‌پی سفید» کلیک کنید و سپس کانفیگ V2Ray خودتون رو بفرستید.
تشکر
تیم WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/whitedns/848" target="_blank">📅 17:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.  @WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/whitedns/847" target="_blank">📅 14:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-841">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2rayNG_2.1.8-fdroid_universal (1).apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/whitedns/841" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آپدیت آخر V2rayNG fdroid
🔴
🔴
🔴
دوستان برای اتصال به کانفیگ های بات از این اپ استفاده کنید.
@WhiteDNS_Installer_Bot
@WhiteDNS</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/whitedns/841" target="_blank">📅 13:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/840" target="_blank">📅 13:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z1lyeQ8b_aI7PEGl_pbJFLt33_sPr9oduR2nLAHn8pY8wqJnzLDR69-mE4MbBDRBn6F2jlkFrQQj9eH0LE_OFTUTjZuC8Kk3onIriP4t3yYUClH0cC-XoQG5IZSQN_92EMDMsgOM1cRU2ybsYxOAXJX6-LbvpyO-v4mzHjyShWv2e1JA_tjVbrqYiuGC8nhzvI2TF9DRKQX6sqmcMuhlskaSXuXfwa5bO-a8cU4txNIJ3XE56TeGzPzDjHPzTVW1BZ_lm0yRSow-xsoky-EAYtvIIWheuOsQScZ1JNhEbmH1yVxu25AU5A-u2Yw_lOawVWrawFt2577ror6UPJjIkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QOkeewsRvHPV5mvhcliwZOooE8PpvqpXKjFykUMruFZg9OzmuauzvwPyztM1Jbmp6Cp2S4gDKO2BFY6jWowLTdrQfYyAEh3zB4YGpjo8X2N9W5vcTVsPQcaWP7TIGFRHlnooJAzCHEmxYIhNrvVTrJ24v-CpyjmEqNOAbS_CbMMtAFnDTDeRbvJRc6gOASCGqUlNrE5MCUtdHYtVgeWoEr4C2DzE3HTW7k9s-JK6wpKz-aCLb3PyMnlNKWNw0AlA_PYhTvTv-3fjNo9CbBiRfciAWRW6NFKbuK7bgOcWC29F_g3ruI7qG0x5aVYmGH_9NV4mQdYLSq0sm1rLPn9Cfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cA16Hins5OYH4txXNPxw-xi9xi6yCI9wyGJtSAumia_dZaETVSZ6wY2kNNFqO2azZjJ8s-4LopBfgG6GekgB1DdGAwTgoJM_NoBahP7lM35-jGxRlT0l6RbDARN-y-2et7J1FOJALEb6XfUsSi3236xbbYUtgwhM52eVV3ZLRiq3FnzIpbCDOgIbkZnDpItHrr_-gu9waKKX6FTdlSMIFfKG0LfZrwB5VPuoYzLadkOdWz6h-NpCmIiO2AXVhPiu2QqTBjWEjYjWOd9NMkelMOrlzPHnnvATPkORK9k92mh-7hJBq1qFC2t657zQa2Oh30tmc4j-0ySMctGjz60dCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nFMsdiuldZbh99E4QObQgYLFCC0NlYN_X5tdJGEmGHej3dS08a2uC1WIMtEb46gQaWFbKtnQKLaeRo57f4OmRQomfOGOnpNVryXWkpjuhjQJTigSGNiM2X7-eKhCSPncave0SjZaQV_FumCU0gaeb-eYgQijLDFc44pGDlcHo3w2JCLVSkHN2pn6X1InZU5t9XeBRyIxHc3kBKhCRSIPlbRQoO7eKtofxBh8AMXjQsFyaUkbJ3CGFwonNVd3T22cSVZUT7YDr9iygX-NkixBGDzBL3EydRlkztlCfpIraRt5HURtYqvlxIdb_0PTudb3R2qJsn9a0b7pFoihr7AoVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sKoqcPU0boH8iQ73rJs9svq-Hq0IJQkEY-sWHR_Guyw6IVzFQcnXZ1zv1L_qI45aAS3sMsLMUBXekEbyM58gdSfz-Vtb0sZO_6tHJlygSHsr3KSWBUwfri-glNY3LXa5BjTv1ClOldnbIsgCMCkCgp6kD32w0fEIXRhPoLv2qixQ3tghQzewWY5DubqsKk7XR23kN2oQlKz_y8fB2gLBG3scoKdbnv-rxRqgXh55Sdqae0BUuferbz0OSMHKRqeZad6GwvONz5d27OvbpjWOSpabh-RZ5N49VdiDqV1miPvW6r5II4rVU3Mk5isG_e-w1gM-u-lcHAflDP_OSNiIBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qNK5CjkgoYE36L0KCKEsWikjbA4PaMNBNs1nKv-EwV0nQmpYuMlC_vgfDBmZ8cTiENwi2Iwiz0rBoMC5VG67ha6txRMRiAlJhK4OY21mmrf9viJ9947L91MWkhfLDGWePLpymkJ--85_7DadaTKWvTuGy-RnWT_MssfoLBMujvV8wvTWv-totgOmOB2umFjOVWYLc8kBLjEcn3adJB02wt1IgIwQQ9sXHXk0RSS67lK1AjOpQ0fie7A8GdF9l3v5PVlrrnMNAyQ5RHiCzyY1tgyDpYR27cIYruTr1g8USlHjRtGSAgnsFAGDN0vKpq3KC0HeE65PP1czNCCuJW8w8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T-zaQ3jh3Kh027h0XvuKPr0AsEWLxxrbX76g1e13Ybop7AQ9wVZfeJTdmsBP6b0WRo6hxlLYP4gqQaTH6Zi443EhsmCDnfZwlvwzp356ALJpJc3n2ZcsbjAeRwSL6fr6Nob0Dru_nfCAfYTWfUORhEYvKX2dmCkh8qwcjUFu8J6tegpe-03lVDBN_DrwM15Q6EXeef1o_pNh8T2Z8xEbFOYv9hOpCqkIrlAmuTS8q2aIz9CxvEXvbaa4Tp-EktydNr_jmUr3d0STD8pd95XgqOD15vwbuiUvZTV-ndz5NmcOIxtDTMrc6JVb--K2bjuW1RaAot2BptvE_TyHbW2IMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UUoNGC5PcZsQiKEntlU4r1LNxLdREbSMzeqF7QonqfeIK3otQwEMuxctR8rIuSGcX2I0JoD91UGhL7ZD-bpuTA8pLYGgnRzCiGGTWqPJAwNwL92katGGTLEOOn4zTKgp_-HnwONLwdxyPVid3eYbdFeWywX4aZUc_zlRq-UHa_yP4J3pkqdSvCEDDeRBeQUa7-LCsgf_UW5Lezpvc7VTR3b15NY5GCUoodKpzfz4BYWzRClPjuBX3gY0iLXcgI_x7gZa85Yk5MRiOFId71mwn5LeItUsMvdmk57dNc54qQccJ6sAJz9LZqsSjK3rLRQb91DsW0Ib9WODJvUmMz-MDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CE6-OvZT13n6_UyZgHeGWedPDvDsvHOSFuUAvSAG2Msp7tskfPSQzQ3d6M9TOlq4YUO_Gjzw-tTq-3ABGaVTbfsmNPCPN70bCazyWqQM7eD4g4wDsd1yG-UL3-iQUzDGD3iO7rvtEmtA73Y0riYIdG2_6XC22IhyFfHp65GhaAEUd-Al8y2TgnqFJaJd13SoKh9G_pal_uNhI4Sb8AHQBDNrXRDJgNiwRSkfJOtys6-ecEanWV-XlhCuTK17CrqwUn8ERQx4uRsk-7MAg-99EAJ6h8oo84embfStZBKWoC4M_xOQeKn0YqvRxR12EqfR7_mYHX0A_PbWbSsXaGAXDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.  @WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر…</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/whitedns/831" target="_blank">📅 13:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WleIKZBW5Q0buzoCx_XRDSjMGIj0MU6hQcqBveqJ8sOWg2qRPEczM9DKGih3xpFMxlc5LpCIhfLH2yzmGcM8PQa_ORhX3L7jZNqSAfNX8EVgvGEzihfSZjZtUkwoZhLYEfQPfjA43ulPFHTk3rmBAM2mv1wQKR13MsuVWMjmJykxMsRj1LmpJ7mfceR7p4yUmYfV-93E3e9sz-KBxHjAu-c_RZ8_sVI3xokoSObLPcbKXiIVqk62q71yHWhTzOR_8HlC3J-IjH2A4UZfsnPu7bd58XMLrcZFwyLFn5lNg7QuAUJ5kT9Jy8CNbITAijE_tsOVRkt8nPhMJdLYy7ozDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.
@WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر بشه و پایداری بهتری داشته باشید.
بعد از عادی شدن شرایط، تعداد خروجی‌ها کمتر و بهینه‌تر میشه.
⏳
همچنین بعد از ۲۴ ساعت می‌تونید دوباره درخواست جدید ثبت کنید و کانفیگ جدید بگیرید.
ممنون از حمایتتون
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/whitedns/830" target="_blank">📅 12:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-824">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔥
نسخه WhiteDNS Desktop V1.0.0-beta4  با کمی بازتر شدن شرایط فیلترینگ و قابل‌استفاده‌تر شدن روش‌های پایدارتر، تصمیم گرفتیم پشتیبانی از V2Ray را به نسخه کامپیوتر اضافه کنیم.  در این نسخه VLESS، VMess و Trojan پشتیبانی می‌شوند، امکان وارد کردن کانفیگ و Subscription…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/whitedns/824" target="_blank">📅 12:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-820">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/whitedns/820" target="_blank">📅 12:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-818">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/818" target="_blank">📅 11:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-817">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/whitedns/817" target="_blank">📅 11:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آموزش اتصال V2Ray در نسخه کامپیوتر
دریافت لیست کانفیگ ها برای ایمپورت کردن
https://t.me/whitedns/804
https://t.me/whitedns/805</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/whitedns/816" target="_blank">📅 11:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta4-release-windows-x64.zip</div>
  <div class="tg-doc-extra">23.8 MB</div>
</div>
<a href="https://t.me/whitedns/812" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/whitedns/812" target="_blank">📅 11:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-811">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzaLWgShpDq1UWhJzUm6uSYVae-E-Of6D9oXbkuO1CQ4kq4PwOZLICWF7qneu1IfZSrO_tuJcy41mfDgEm9LezegfxBeTHSKqwHJTmD3QS57cNk6L784Y4nb_fxtEe8IcUNkSMdwpMSKVImH4JPrNq669Tsbb1LbTvODyxU08xLUK7ClhhP0E8doKL3Eh2of_NMHYfkh8P3Z-NR06gOrpgT3aS5Ki9GgRhBzcDa9IcT55AE-hpEhdwqDvsCu2BrnCuD9MHX3irUh9lrmfEsItinQlhRccoyB_FZ-ywue-bhh5Y79W8YqpeFGb_zRaZd8Q-4JWKYWNLfIfJgTQlDPVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/whitedns/811" target="_blank">📅 11:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-810">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/whitedns/810" target="_blank">📅 10:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-809">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/whitedns/809" target="_blank">📅 10:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-808">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دوستان سلام :
این یک مدت به همه سخت گذشت ، شاید شما اسم دو نفر را بیشتر شنیدید ولی بدونید یک تیم ۳۰ نفره بی نام و نشان پشت این کار بودند  توی بدترین شرایط از همه چیز زدند تا شاید یک روزنه کوچکی باز بمونه ،
ببخشید کم بود ، کافی نبود ،ولی در حد وسع خودمون تلاشمون را کردیم
یک تعداد زیادی از  دوستان پیام دادن ، تشکر کردند و گفتن ادامه بدیم ، خواهش کردند بمونیم
ما هستیم کنارتون ، مگه میشه این همه عشق و محبت را رها کرد
یکم استراحت کنیم ،همه با قدرت بر میگردیم
توی این مدت مراقب خودتون باشید
تیم whitedns
@whitedns</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/whitedns/808" target="_blank">📅 02:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-807">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvI7HUS35tqfHbwGcUamM8a3ub1baNaL9Aeg9OFivDfzd6QffNsIbXFUKXVU2lNpHmQQs0nLWmevapP6AMweLuSzVb_dvYZECkD7qU0LRjzcDm-EtXckqy7latUPU2N9x4zBb9I8M1Ik5dcQMJFGDgdZAP5Xti-GPCJstMBVni_LOHKM5QQIo6ce0tPlFCCEOdfKuIJEXuDiC2rVNPSAeaRvYx0BeYH1umL2woEWwJoy_cVu8vmRImehIV8rN158x5CQfqeWoAbKEg-qt_83467bUq9fN_tX_TdNIErJ4zr-GIGIkpbj_GCSo6SXIH9etigGxmPl8ja_DeDxcu9vVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#موقت
یادمون نره کسانی که از ظلم پول در آوردند.</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/whitedns/807" target="_blank">📅 19:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-806">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/whitedns/806" target="_blank">📅 19:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-805">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 62K · <a href="https://t.me/whitedns/805" target="_blank">📅 19:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-804">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/whitedns/804" target="_blank">📅 18:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-802">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QWwIYZjqh2bDLuhqCvIqsrNLxjPBY5zwJOhEpOUPxwFNVx9pFZLURGkFmdxiT27X2DhRmGw7CWSkDqu5ZVRSTBneJkY_J5S2fwnKl4u_08QpFFC1lalWCocsMVriraDS4wHJ5N4asf8z1JS9LB8SfIlKuSTdYpLhvaJSW1rIqsa4_EO7YNzfnLurA4fLs_Q8ZjvYZ3Z3nxu7LQdqBHRH_iAAK-tuBEm6RRR-6pZsjY6j3_TWYiLlWxb_sKThirw_60TQT6AdxSvYceFCs-0OaW7J-YiQ-ZNth9PXozRD3O9rQs7wTBOlD24uuI_EFheLlIE5ATp7Qu-fplEFL7V90Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/INGYZ-6cC-QELGgv9jkKxZcDIZ37wfwgwrZvQP_O-73mWhfyZhmLqxqkFtl8t7R5xpYmQBERYDIE3m2hCS5UboMdzSBg6ieq0WJc6-UCDsq8b1mGFF_C-Sq6FzfsLgbuhHezTNxOVJwPdcNig5gDsCQnM24awd1HwTVKiZCrnDq9GtC-zKo63lYbDLl8C2ZyVemlIloQ5H02iGqyYHPi00Hdh0mw7yCUmSxLj0vlS2L1_OJe7637x4uzhgqTWELHkZ4TRudU3U4HYlOdm-yS7GPYvhF6mlC-N5cgA6MGRVXZOTRvueYvmZBBbQMa_ZQ4p-4gLFD5yJZ-PpYAfccllA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این هم یک تست سرعت با ریزالور های درست و با اختلال کمتر
🤌</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/whitedns/802" target="_blank">📅 17:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-801">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/whitedns/801" target="_blank">📅 17:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-800">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">در طول ۳ روز گذشته، کاربر های ما ۱۰۰۰ سرور جدید اختصاصی با ربات WhiteDNS ساختن
🎉
@WhiteDNS_installer_bot</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/whitedns/800" target="_blank">📅 09:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-799">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دوستان گرامی :
ما هیچ گروه و کانال دیگری در هیچ پیام رسان خارجی و  داخلی نداریم
تنها گروه رسمی ما :
https://t.me/whitedns_group
تیم whitedns
@whitedns</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/whitedns/799" target="_blank">📅 03:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-797">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKo5xDOSDtg8gEQcQ-qAxAaBwRpKVl88figzcp87qu_vIr1S_r6A1Ew5Ek7YJG1j28Lz5IyWU0p5ZVPkiGl4TIrYtX639rRy-WGNEXnnL6eW1UDd-J3bCGumH_SAqaQRVyr4C7kDehR7nQFFZZHO3sf4NUhoTWIuhPkeE9UjQ1Msx6TJ_-KFQO3wUtRmyPadORXaOwIJ111F8UiTwU8hTOHJdIT9giShpKtyvWoKt7FjpHmM8wHFx_FuG8eZ6Yi0IhBkJ2jL8YI8IZ87cRqGrlxnn7FOddjE6XcYGiZdaU0-IT_C_xKqLS3ipuI3admV2bN1Ia5r3s-HtwUZ_2V6hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کیه این تک دلقکو همیشه میزنه
😂
؟
به افتخارش نفری یدونه بزنید ببینه دلقک کیه
🤡</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/whitedns/797" target="_blank">📅 16:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-796">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=lbckux_kNVdHzQJrRTuWyvWlcUzisTus8ph_d3wafB4m2jSKczV0PyKiij2OcrxQ5WkphyD4zgfNtfnW9PbPUgNdSmsIRLLI79JlVyIGBMJr_AXSbz1TX0-JVB-mXorQkF3W3sg4-QD5j8sx2XzdH4z9wywJMxPFtLkamuKOvrURm_dIiBxw_Rs9F5kq8dTb7UC5iylYgmfmPhUDzJG6ngjawf0W-KyHCtP7BZy-tr3dMBkE9sFTTotC-qiyJfoqvSwmMNN_TRmgOg43tQEoCL7_PrOkiYgRfOGlWW0Fjz-0EvNp0wNjgp1KRtm7q1Pg4NJHtdgHBz4zn5VZhinOG18DeX3XPcQ6f1U6qfmBVLCtcNKzR-dNBvGlFg2Dn_kcxcAdFIRooJRPvhp5GbToqit8sADRUt7WvopZaNNbqVnJW69fwSltb0BcV6_Nefq28KYpBC2wWtL83WkisQjR4g-ri5LCvNDnCJ2_kn611kMEectbSC_R32ApgtveCfPnxPKicXbbOzn17aHWfIJCjNGEXRva-mOvJi887O6s6B7cPuOw_tgVVUny3jx0cThz7ynkEKojgAbuG7F_tb5D0uHo5AG0RHX_9mGrwTfB9Yn_CJHVS3DFOSoiIYcK-nOEjvy7QIovzNlxo-mUD1L5Xv98JT05Dc0p8MJ8IifC9h8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=lbckux_kNVdHzQJrRTuWyvWlcUzisTus8ph_d3wafB4m2jSKczV0PyKiij2OcrxQ5WkphyD4zgfNtfnW9PbPUgNdSmsIRLLI79JlVyIGBMJr_AXSbz1TX0-JVB-mXorQkF3W3sg4-QD5j8sx2XzdH4z9wywJMxPFtLkamuKOvrURm_dIiBxw_Rs9F5kq8dTb7UC5iylYgmfmPhUDzJG6ngjawf0W-KyHCtP7BZy-tr3dMBkE9sFTTotC-qiyJfoqvSwmMNN_TRmgOg43tQEoCL7_PrOkiYgRfOGlWW0Fjz-0EvNp0wNjgp1KRtm7q1Pg4NJHtdgHBz4zn5VZhinOG18DeX3XPcQ6f1U6qfmBVLCtcNKzR-dNBvGlFg2Dn_kcxcAdFIRooJRPvhp5GbToqit8sADRUt7WvopZaNNbqVnJW69fwSltb0BcV6_Nefq28KYpBC2wWtL83WkisQjR4g-ri5LCvNDnCJ2_kn611kMEectbSC_R32ApgtveCfPnxPKicXbbOzn17aHWfIJCjNGEXRva-mOvJi887O6s6B7cPuOw_tgVVUny3jx0cThz7ynkEKojgAbuG7F_tb5D0uHo5AG0RHX_9mGrwTfB9Yn_CJHVS3DFOSoiIYcK-nOEjvy7QIovzNlxo-mUD1L5Xv98JT05Dc0p8MJ8IifC9h8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/whitedns/796" target="_blank">📅 11:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-795">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEBwE3YiHbyP7S3nGh9rbkHk58fY23-_6AGtcFIuKTv7na211ZNlastMk92JvKk7ayLfkZDrQdx80nG8UHHGUbKjQnB6WiT5WeO4CZvDsNb270lKBir9gSEP3mBOsCjdiioJ0Dm6DV7fTYODeqWgtJy_wk7h35akIadV0zbOKcpBshobfv_RntZ8SBt5VF2hM2NupGFpaVyvPqZ9s8z_eWR4kpevmxV5bYp-XxMP_QgNzudHlSsjrGTCApysM8FME0aZNWQ5IRsylpS4SCZp7ANnQLlTZRh6DhgYzKtyLXQwYYAN8szYUuPT2mbCYlH_KGRpuOMUhSsUNCmu1UrNnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حال حاضر مشغول تست نسخه جدید اپلیکیشن دسکتاپ WhiteDNS هستیم.
در این نسخه، علاوه بر اضافه شدن حالت دارک مود، تغییرات مهمی در عملکرد داخلی برنامه اعمال شده است.
یکی از تغییرات اصلی این نسخه، تغییر کلاینت داخلی اپ از StormDNS به MasterDNS است.
این تغییر به این معنی نیست که سرورهای StormDNS دیگر قابل استفاده نیستند یا وصل نمی‌شوند. سرورهای StormDNS همچنان قابل استفاده هستند.
اما تنظیمات داخلی برنامه در این نسخه بر اساس آخرین نسخه MasterDNS ساخته شده و در تست‌های اولیه، از نظر سرعت، پایداری و مصرف حجم، عملکرد بهتری نسبت به نسخه‌های قبلی نشان داده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/whitedns/795" target="_blank">📅 09:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-793">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">White DNS
pinned «
دوستان گزارش دادن که Hostinger پولشون رو بلوکه کرده و پشتیبانی جواب نمیده و... ترجیحا نخرید. نکته اینکه شما با دامنه .ir هم میتونید انجام بدید این متد رو اما خب توصیه نمیکنم به شخصه علتش هم واضحه. جای مطمئنی برای دامنه دیدم معرفی میکنم
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/793" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-792">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">دوستان گزارش دادن که Hostinger پولشون رو بلوکه کرده و پشتیبانی جواب نمیده و...
ترجیحا نخرید.
نکته اینکه شما با دامنه .ir هم میتونید انجام بدید این متد رو اما خب توصیه نمیکنم به شخصه علتش هم واضحه.
جای مطمئنی برای دامنه دیدم معرفی میکنم</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/whitedns/792" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-791">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سلام خدمت همه همراهان عزیز  ویدیو آموزش ساخت سرور شخصی که متین عزیز تهیه کردند دقیق همه مسایل رو ‌توضیح‌ میده.   تنها‌ نکته‌ای که باید اشاره کنم، متین از ترمینال برای وارد کردن دستورات و نصب MasterDNS استفاده کرده.   من پیشنهاد میکنم برای راحتی کار شما، بعد…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/whitedns/791" target="_blank">📅 16:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-789">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/whitedns/789" target="_blank">📅 12:41 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
