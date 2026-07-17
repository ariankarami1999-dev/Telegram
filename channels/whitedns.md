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
<img src="https://cdn4.telesco.pe/file/jOvhtuR5YhD28bqmrv2kGVrAwsXBuwHnQpVbytyhnRE_TFYke8C3Lw0zd6gJw_cDkX2MqfdKcEPFr6JP5BlMUjOKlEEzCGa9zZRtK07B86A-_z7-ZFr1Z3lHkjAe7znQfsk7cEIQa9u5aRBiBxzzGGEKYTmW7c3VDtpmdAa7Sj0o1z1QRCpwHXGUjFK9PGCg4Bf43JKQK8mcwlSNIF0xynBictIhrFJT734AzC4c-yzUklabMgdIeS4e7F3UXmmovdgvoN4GUaFXJH-QyciRaD72bBZVCJ_nlgzVEpFkqwT8cGBTEhpBeX07DAaAL7qhq1McONdMTvEquz1vf6tTiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 108K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 20:31:51</div>
<hr>

<div class="tg-post" id="msg-1195">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/eWe42sKpK5io-1ZBDwAWoVh7Acsu4M_02tzGTyJ69_G_fPtnhOBCvA6RYzsu2d8yAbkNbk23lCCn8hWUUZPj8RTXPIxvrCjCHLL4xZLiYTDflpUghlXM9Czae2N9GSEdaSt-B_HFC8va2f2m_FmvPB8BXNb5dp9FxfTK2uf6D_UR0SVQBR11Z1HSMAvp9_QFOJnkLKtf3OUJW0IOatMRZc1y3HfK62fz5xx1AQHXqAR_YsPIS5OQ5nk6D8KAo10iePCQTs7CFQnbJe7EBVTNSSc-9qBFUKpaVV0-CjzTD_1AAh2OYK86yBlzltuF6VHh_M4gIWkK5-F4d_xp1x1zgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
راهنمای جامع تنظیمات APN اپراتورهای ایرانی
📱
📥
۱. مراحل تنظیم در اندروید (Android):
1. وارد
تنظیمات (Settings)
شوید.
2. به بخش
اتصالات (Connections)
یا شبکه و اینترنت بروید.
3. بخش
شبکه‌های موبایل (Mobile Networks)
را باز کنید.
4. وارد گزینه
نام نقاط دسترسی (Access Point Names یا APN)
شوید.
5. روی
افزودن (Add / +)
بزنید تا APN جدید ساخته شود.
6. فیلدهای
Name
و
APN
را مطابق لیست زیر پر کنید (بقیه گزینه‌ها مثل پروکسی و پورت حتماً خالی باشند).
7. از منوی سه نقطه بالا گزینه
Save (ذخیره)
را بزنید و آن را فعال کنید.
🍏
۲. مراحل تنظیم در آیفون (iOS):
1. وارد
تنظیمات (Settings)
شوید.
2. به بخش
Cellular (تلفن همراه)
بروید.
3. گزینه
Cellular Data Network
را انتخاب کنید.
4. در بخش
Cellular Data
، روبه‌روی گزینه
APN
مقدار مربوط به اپراتور خود را (از لیست زیر) وارد کنید.
5. یک‌بار اینترنت گوشی یا حالت پرواز را خاموش و روشن کنید.
📋
لیست مقادیر APN اپراتورها (برای کپی آسان روی کلمه‌ها ضربه بزنید):
🔹
همراه اول (MCI)
* Name: MCCI Internet
* APN: mcinet
🔹
ایرانسل (Irancell)
* Name: Irancell-GPRS
* APN: mtnirancell
🔹
رایتل (RighTel)
* Name: RighTel
* APN: rightel
🔹
شاتل موبایل (Shatel Mobile)
* Name: Shatel Mobile
* APN: shatelmobile
🔹
سامانتل (Samantel)
* Name: Samantel
* APN: samantel
🔹
تالیه (Taliya)
* Name: Taliya GPRS
* APN: taliyagprs
⚠️
نکته بسیار مهم:
اگر در فیلدهای
Proxy (پروکسی)
یا
Port (پورت)
در تنظیمات گوشی شما هرگونه عدد، آدرس یا کلمه‌ای وارد شده باشد، سرعت اینترنت شما به شدت افت خواهد کرد یا کاملاً قطع می‌شود. حتماً بررسی کنید که این دو بخش کاملاً
خالی
یا روی
Not set
باشند.
@whitedns</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/whitedns/1195" target="_blank">📅 16:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1194">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1194" target="_blank">📅 13:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1192">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :   ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.    پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/whitedns/1192" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1191">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1191" target="_blank">📅 12:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1190">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/rGvBk6Wor2fIsqE3qDUFpEMsA1ECEiU8jCwgdUhNgru5p6Whe-Meo8dg2dnKHCruC78-YexlWe5xMIGrHbtHW2gaSlrzfW3DZepo-u_24h48sxZC8h2Fq1LbNsDtzBb4TtInLnwTEf3HEL0DfVU5RfQrR3RqUi1Jbfgort3oktjTg4ORUy-8eJzYSk6vkituGmiHvPxqTx56NlNoCFv3EV7YCtGt9NqmxUeh-nlHx6izm3FbQxLHVgs95PKuFC-dJy2DLBo0zb3e5QW4_bQ18_pav_P2R2sIQ9rvblVZ7eUDPOduugVP5NPWmM8b7TY5EBdExfl1Md9icTd4Qw3B4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/whitedns/1190" target="_blank">📅 12:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1188">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🛡
ورژن جدید WhiteDNS VPN
👆
👆</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/whitedns/1188" target="_blank">📅 11:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1183">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/whitedns/1183" target="_blank">📅 11:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1182">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGXnycNNSG2uXXN1r7YLxXkTORXK9JDsNOUFiWTae0TkBTVdMmj_L9bzuJGKWxptSRXay00xYuZBZtstxTCJSs0z5AFZC_808x1_2S-zbEqfw2Dn8V6O4o5ooTJVqttnH435Q8F8LiTYv8b_HTcRDw6zg2Axl_918V6YGMZtDFJGMmoqZMLCveowTRFND9d-R-jYTv_A8pR2ETS1lpzy_AdPnJdFp1f7eQSVHhf9ZZpBcsmS1VUWNAenR8GA3brpmU3voua6Sz4dhhcfXm3A8aLIg55xD-KpPBX7cZ9sRjd_QiFblztfZ9X3zFZuiTn-iH-PQLO4nlXgC1lHChwsOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/whitedns/1182" target="_blank">📅 11:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1181">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1181" target="_blank">📅 08:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1180">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LySHO13lUu2Z5JtJdAF_lhHuu-HlhV6JSghVE2gnGjtLMGsQS77YQk9phuHXVGWXwZjtnhDKFXilTdNRLpwJrHl9M23Gy1z1wxAUajlWFQdi9aqZlNJQ3LWQgSGc06gOGEG4s1zlJIEnXqCnXDy7q2uG9qGnAny9QCbwVcszWE2f3xnSrtU-kAGNM0Jm8TErs23JqV9RHj2tkCFBV2TvahVdr1ko3DBqrSA_tYIScUr4djo4EL37e9PG0hq4iUejyNRdvr0EEsQ9iTxsPD0azg1Oo35zukEDJA63OCY7ZogNhTSjI9Jp5EJsvtEYhY5d-Vq9ojhu3y0WGx1LA9psUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی کانال یوتوب WhiteDNS
🌐
اگر به دنبال آموزش‌های تخصصی و کاربردی برای دور زدن فیلترینگ، پیدا کردن آی‌پی‌های تمیز و ساخت سرورهای شخصی هستید، این کانال یکی از بهترین مراجع آموزشی است!
🎓
در این کانال می‌آموزید:
🔹
آموزش صفر تا صد V2Ray
و راه‌اندازی پنل‌های ثنایی (3x-ui)
🔹
پیدا کردن آی‌پی تمیز با
WhiteDNS Scanner
🔹
راه‌اندازی
پروکسی MTProto
برای اتصال بدون قطعی تلگرام
🔹
معرفی ابزارها و کلاینت‌های مختلف (مثل CoreForge برای iOS و FlClash برای اندروید)
🔹
راهکارهای ارتباطی برای زمان قطعی کامل اینترنت
📡
و .................................
برای یادگیری ساخت فیلترشکن‌های امن و پرسرعت، همین الان به این کانال سر بزنید و سابسکرایب کنید.
👇
🔗
https://www.youtube.com/@WhiteDNS</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/whitedns/1180" target="_blank">📅 08:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1179">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✍️
در مدتی که اینترنت وصل بود، تیم ما تلاش کرد ابزارها و روش‌های جدیدی آماده کند تا در صورت بروز قطعی شدید، بتوانیم بهتر از شما پشتیبانی کنیم.
متأسفانه بسیاری از این ابزارها را تا امروز منتشر نکرده‌ایم که برای این تصمیم دلایل منطقی و امنیتی وجود دارد.
در صورت شروع محدودیت یا قطعی گسترده، تلاش می‌کنیم این روش‌ها را به‌تدریج معرفی و در اختیار شما قرار دهیم.
برای شروع، تعدادی سرور MasterDNS نیز منتشر خواهیم کرد. با این حال، پیشنهاد می‌کنیم در صورت امکان، یک سرور تهیه کنید و با استفاده از ربات زیر آن را به‌سادگی کانفیگ کنید:
@WhiteDNS_installer_bot
❤️
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/whitedns/1179" target="_blank">📅 04:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1177">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/N1oB7yYw0KYbTxICbr-CKPTPjhjOUz7AjCzkpok7Fntw-oOjO5Zcz1457xWk6uWs9SjIdyDR-UuT6cDRQGXy426mlZikLAJuiTyUOOgHZWj3-1lcsoCmUkrDDBwBypG7hR6zCI3_xaPX4IDod4y8IURbk2UJcmlqJ1EXv-GDg3-24fbqNWPBt8kLG95d8GJhUTBlkVNdfOtcUbvQpIhihe_RjCB2cx7q-Jh4s2IY1XpJAMcwc6XqsMHJqOmNMy3MOuDESiAbOSGcJPCFfzAdHAwN4GrwGTaFwncwHyJYHeiYEDgyCA6877hTiMrIUHwcvZWZfDNEN3B5QrkDWwa8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند کانال WhiteDNS
👉
@WhiteDnsResponder_bot
✅
جواب سریع |
✅
۲۴ ساعته |
✅
رایگان
نحوه استفاده:
۱. روی لینک بزنید
۲. Start
۳. سوالتان را بنویسید
مثال: چطور فیلترشکن نصب کنم؟
/search عبارت — جستجوی مستقیم
/contact — ارتباط با ادمین
⚠️
ربات WhiteDNS در چه زمینه‌هایی جواب می‌دهد:
✅
فیلترشکن و VPN
✅
DNS و تنظیمات اینترنت
✅
آموزش نصب اپلیکیشن‌های WhiteDNS
✅
رفع مشکلات اتصال
✅
Warp و Cloudflare
✅
تنظیمات اندروید، آیفون، ویندوز، مک
✅
سوالات مربوط به قطعی اینترنت
❌
ربات قادر به پاسخ‌گویی به سوالات غیرمرتبط با موضوعات کانال نیست.
💡
نکته: اگر جواب دقیق نگرفتید، سوالتان را طور دیگری بنویسید یا از دکمه جستجو استفاده کنید.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1177" target="_blank">📅 17:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1176">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NU2y1Lcb7fqHY8CTm1uQI1A41FPTRwhcTukhzX4U20h1koYSdcGFS__TTsZlzOsdhr7mb2IEyz9vYmTj3_SLET3oVhbe9yNfxQu1O66ZC1-uSYdDMAaPlPrnNi9bhk-VXTOgb3znJ98v2CwxQLyLW-bRwVdCj507NkFb3TmIhfM8Ilzz3YKjZNc_s5f_zj8jxgRyZxY5bPiW6e6c75vLFcrIVRUUKysONup7UyxNkTDaGFQQQEflptO4tXR6w5UjxQEwODvoLcI-ipykwjjP9hVAlVR1LMernY1RxEZI7-teYUgXDfEAzCCymBO8XvMqV4lgYtvg4ehhEBHv_Zq3_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
OnionHop V3.7.2 - انتشار جدید: اتصال هوشمند و عیب‌یابی شفاف
آیا می‌خواهید ترافیک سیستم خود را بدون درگیری با تنظیمات پیچیده از شبکه Tor عبور دهید؟ OnionHop، ابزار متن‌باز، سبک و قدرتمند ویندوز، برای همین کار ساخته شده است. نسخه جدید 3.7.2 تمرکز ویژه‌ای بر پایداری در شبکه‌های سانسور شده و شفافیت عملکرد دارد.
✨
امکانات و قابلیت‌های کلیدی:
🛡
حفاظت دوگانه:
انتخاب بین حالت
پراکسی
(سبک) و
VPN
(سیستمی).
🌉
عبور از سانسور شدید:
پشتیبانی کامل از Bridgeهای Tor، شامل
obfs4
,
Snowflake
,
WebTunnel
,
meek
, and
dnstt
.
🌍
انتخاب کشور خروجی:
امکان انتخاب دقیق کشور نود خروجی (Exit Node) برای تغییر موقعیت جغرافیایی.
🔒
امنیت بالا:
شامل
Kill Switch
(قطع خودکار اینترنت در صورت قطعی Tor)،
DNS امن (DoH)
و پشتیبانی از
IPv6
.
🚦
تونل‌بندی هوشمند (Split Tunneling):
انتخاب کنید کدام برنامه‌ها از Tor عبور کنند و کدام‌یک مستقیماً متصل شوند.
🤖
اتصال هوشمند (Smart Connect):
قابلیت جدیدی که به طور خودکار بهترین استراتژی اتصال، موتور Tor و Bridge را برای شبکه شما انتخاب می‌کند.
📢
مهم‌ترین تغییرات نسخه v3.7.2:
۱. تشخیص و تأیید ۱۰۰٪ پل‌های WebTunnel
در نسخه‌های قبلی، برنامه فقط آنلاین بودن CDN را بررسی می‌کرد. در نسخه ۳.۷.۲، OnionHop یک
اتصال آزمایشی واقعی (Handshake)
با خود پل برقرار می‌کند تا مطمئن شود که آیا واقعاً ترافیک را عبور می‌دهد یا خیر. این یعنی دیگر پل‌های خراب به اشتباه «سالم» نمایش داده نمی‌شوند و شما زمان را برای تست اتصال‌های مرده تلف نمی‌کنید.
۲. عیب‌یابی شفاف با لاگ‌های دقیق
اگر یک Pluggable Transport (مثل obfs4 یا Snowflake) به هر دلیلی اجرا نشود، دیگر با پیام‌های مبهم مثل "status code 2" مواجه نمی‌شوید. OnionHop قبل از اجرا همه‌چیز را بررسی می‌کند و دلیل دقیق خطا را در لاگ‌ها نشان می‌دهد؛ مثلاً: فایل اجرایی خراب است، نسخه اشتباه پردازنده است، یا مجوز دسترسی وجود ندارد.
🛠
راهنمای قدم‌به‌قدم اتصال (How-To Connect Guide)
براساس اطلاعات مخزن گیت‌هاب، نحوه اتصال بسیار ساده است:
نصب و اجرا:
فایل نصبی (.exe) را از لینک زیر دانلود کرده و اجرا کنید.
اولین اجرا (انتخاب حالت):
Proxy Mode (پیشنهادی):
اگر فقط برای مرورگر یا برنامه‌های خاصی به Tor نیاز دارید، این حالت را انتخاب کنید. نیازی به دسترسی Administrator ندارد. باید تنظیمات پراکسی برنامه خود را روی
SOCKS5 127.0.0.1:9050
قرار دهید.
TUN/VPN Mode (دسترسی ادمین):
اگر می‌خواهید
تمام ترافیک ویندوز
(کل سیستم) از Tor عبور کند، این حالت را انتخاب کنید. این کار با استفاده از Wintun و sing-box انجام می‌شود.
انتخاب پل (در شبکه‌های فیلتر شده):
به بخش
Scanner
بروید. اگر در شبکه‌ای با محدودیت هستید،
Bridges
را فعال کنید و روی
Scan
کلیک کنید تا برنامه‌ها پل‌های سالم را برای شما پیدا کنند.
اتصال:
روی دکمه بزرگ
Connect
کلیک کنید.
Smart Connect:
برای راحتی بیشتر، می‌توانید Smart Connect را در حالت خودکار قرار دهید تا برنامه خودش بهترین تنظیمات را اعمال کند.
🔗
لینک‌های رسمی
🔗
متن‌باز و رایگان
#اوپن_سورس
🚀
دانلود مستقیم نسخه V3.7.2:
https://github.com/center2055/OnionHop/releases/tag/v3.7.2
🌐
وبسایت رسمی:
https://www.onionhop.de
@whitedns</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1176" target="_blank">📅 14:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1175">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns16.7.2026.txt</div>
  <div class="tg-doc-extra">18.3 KB</div>
</div>
<a href="https://t.me/whitedns/1175" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@whitedns
🔗</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/whitedns/1175" target="_blank">📅 12:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1174">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/kI-5d2Stt1a1Bz-aZmgrB69lijyO-hEteIkT4VRfojs5sv65BVmmglEX0bTJ_lu5mEmXRQtRs8vtXKYCLYFWz4_02mdtsuLY1LVszUoWSKOOpJHpMk-ssd9ETKQMIPMwekRb6wy8SkbjDwvL1PCsP6e_TnLAfzeZDjxSDX47DxTWNmv2Ht1rcwAYxhZVTthYd1eZqMATUsqhLixBhgPQ8rmeh4N0-v4zf_VF90uSzUrPgWHBH1it0E4X_82XmlSGTvTbzGBE1Rl2jLLxQxs-lB1_lBgQ-2OmoJe7HvM0lO9I_Az_wbxMSN3o0RoRAWcg7PuwZPH-dLEkLBI4k1H2jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">16.7.2026
فایل زیر را دانلود کنید
⬇️
1. کانفیگ‌های داخل فایل را کپی و در برنامه v2ray وارد کنید
📋
یا
2. خود فایل را از طریق گزینه import locally در برنامه v2ray وارد کنید
📥
@whitedns
🔗</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/whitedns/1174" target="_blank">📅 12:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1173">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1173" target="_blank">📅 12:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1172">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/PmYay6Rcl8S9oqRlKOq_j0ZL1iT_MAMUyGoBD-Uyt0ZtGyO-FQRCe-_T9b3-LdJqZXkXxhUvYqdCu6ya94bizNUVDZkwa86JuM8HHW_jt7Y8XP6BxFf1cWm28i2K7Aq1EH8VrdeN924Cd9LjwOveQBnO2czAMmxlnnkrdjJ-zBNOdDMssDfJ1PFirtTCAKsCFJuFlE-D0nGcJgO9GQUm5jfQ7BpLDWiocJZu_TdWcyOjcJTMH9a4EKVb0dgK93JtuVeLY2AEGKdwled_Ln33DX5hiw7STVy1WdmyEtrK1VZqj-UWuIFX0v1cPkg076WdfAcst9AVwxVbDL0vUOe5oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش جامع استفاده از
WhiteDNS VPN
و
WhiteDNS Scanner
برای اتصال امن و پرسرعت!
🚀
🛡
رایگان
در این ویدیو به بررسی تخصصی ابزارهای اختصاصی *WhiteDNS* پرداخته شده است که به شما کمک می‌کند بدون نیاز به دانش فنی پیچیده، به اینترنت آزاد متصل شوید.
🌐
🔓
خلاصه‌ای از مباحث آموزش داده شده:
📝
راه‌اندازی WhiteDNS VPN:
نحوه نصب اپلیکیشن و اتصال اولیه بدون آی‌پی تمیز (0:00 - 5:30)
⚙️
📲
*
اسکنر قدرتمند WhiteDNS:
آموزش کامل کار با بخش *IP Scanner* برای پیدا کردن آی‌پی‌های تمیز و پرسرعت (7:40 - 18:00)
🔍
⚡️
*
کاربردهای حرفه‌ای اسکنر:
بررسی قابلیت‌های پیشرفته مانند *SNI Scan*، *HTTP Proxy Scan* و *Config Maker* برای ساخت کانفیگ‌های شخصی‌سازی شده (20:30 - 27:30)
🛠
🔧
*
نکات طلایی:
نحوه استخراج آی‌پی‌های تمیز از دیتاسنترهای مختلف و استفاده از آن‌ها در برنامه‌هایی مثل *v2rayNG* و *Psiphon* (22:40 - 25:00)
💎
🌍
✅
این ابزارها با رابط کاربری ساده، برای همه کاربران (مبتدی تا حرفه‌ای) مناسب است.
👨‍💻
👩‍💻
📥
لینک‌های دانلود:
- دانلود اسکنر: [GitHub WhiteDNS]
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/1.3.5
- دانلود اپلیکیشن: [Telegram Channel]
(
https://t.me/whitedns/1072
)
💬
با تماشای این ویدیو، سرعت و پایداری اتصال خود را به شکل چشمگیری افزایش دهید!
📈
🚀
لینک ویدیو :
👇
https://www.youtube.com/watch?v=N5hKuWXp37w&t=57s
@whitedns</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1172" target="_blank">📅 11:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1171">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/lCa3wwlkc41lVDniWIlFvpQ3fCIcEZnoioLqpGA4FqGH-CQtsthBlkz3I_11Li4aDgcKeWUoLHcJ7Pkt3bpPHUb1iVmnVw6OyiDbNAtQ1MFAa-uD3cSKFDp1omtY_hENGlWiewEQBQBdl0MXtO4oWLkOqNy06YyLNbe1dQjZroo2jKXptCP5zKuq5lioerqcmFyuRSBWZKdlPF5QxSgrnAJadkbLF0nKnIW5Y6C7GVhyrvwvZaWLKCaC7oG__H9bVk6x72Yt2ptHe5pT4ufJxN4B_0YvXFVioOp7yPMJ7sEkWTKv9GeERVpXvAi2uWoHwPyj0AN-qYQkEHU7ASHZ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش کامل راه‌اندازی V2Ray با پنل قدرتمند 3x-ui از صفر تا صد!
🎓
اخیراً با کاهش محدودیت‌های اینترنت، روش‌های باکیفیت و پایدار دوباره فعال شده‌اند. در این ویدیو،
WhiteDNS
🛡
تمام مراحل راه‌اندازی سرور شخصی و فیلترشکن اختصاصی را به زبان ساده و کاربردی آموزش می‌دهد:
🔹
سرور و دامین:
نکات کلیدی برای انتخاب سرور خارج و ثبت دامین در کلادفلر
☁️
.
🔹
نصب پنل 3x-ui:
نحوه نصب این پنل کاربردی با استفاده از هسته Xray بر روی سرور
🛠
.
🔹
ساخت Inbound:
آموزش مرحله به مرحله ساخت اولین ورودی برای فیلترشکن
🔄
.
🔹
تنظیمات کلادفلر (Cloudflare):
نحوه ثبت DNS ریکوردها و تنظیمات امنیتی ضروری
🔒
.
🔹
استفاده از آی‌پی تمیز کلادفلر (Cloudflare Clean IP):
روشی برای بهبود سرعت و دور زدن فیلترینگ با جایگذاری آی‌پی‌های تمیز
🚀
.
🔹
ساخت کاربر و استفاده از کانفیگ:
نحوه اضافه کردن کاربر و دریافت کدهای تنظیمات برای استفاده در برنامه‌هایی مثل v2rayNG
📱
.
این ویدیو یک راهنمای کامل برای کسانی است که می‌خواهند فیلترشکن اختصاصی خود را با امنیت و سرعت بالا راه‌اندازی کنند. اگر هنوز شروع نکرده‌اید، این فرصت را از دست ندهید!
✨
برای دیدن آموزش کامل، روی لینک زیر کلیک کنید:
👇
🎥
https://www.youtube.com/watch?v=vVjqNQBUGIc
🆔
@WhiteDNS</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1171" target="_blank">📅 09:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1170">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i9DErcPdVjed0yJXyqlCRd8YXGRppsQfO61DEh_TpDwQnwK7aFznLC0oWQYHNYjlDGNztz7WKwTODjvnhpOD6MTsh_KvfeFmpfolM9E1Es1-kFYu6tFY6fHhx90cPDBnzP70__lbTqpXAR7bUSkAyNhXaO4sUY5n9Xo2D0M5vdumjwr3Ca9x93Z0ZwvnINSe3BJYMul7l8CCbco1PKiDS7ryq3KxB7SnRs2JbuWNB8D8kBE7JQPpDBbsYPzljb85TDtUkhg9NpYFyzlfEuRVrO3jrWc2SLVOXuXO-jEHHaMfs4Qe4MJdO_K8l_AkntShizi3bGC0krJO9I5Jnj3Vlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
اتصال رایگان و پرسرعت با پروژه Aether + پروتکل ویژه گیم Wireguard
⚡️
لینک پروژه‌ی اصلی:
https://github.com/CluvexStudio/Aether
لینک پروژه GUI من:
https://github.com/MatinSenPai/Aether-GUI
دستور نصب از ترموکس:
curl -fsSL https://raw.githubusercontent.com/CluvexStudio/aether/main/aether.sh -o aether.sh && chmod +x aether.sh && ./aether.sh install
دستور غیرفعال کردن محدودیت مصرف CPU و باتری:
termux-wake-lock
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره. حتی نیاز به اکانت کلودفلر هم نداره
😂
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/whitedns/1170" target="_blank">📅 13:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1169">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RGXDtrVzQNwqh7eq_WgJ8FccDSqLE-BvNkmLaNX8EIz_jIr986wuPOnUIlvIUv17QTcrWMtVDQX88iGEIcseOLetKIZThYHWvwdQGLz_Um58hrU5ofMgE0AHdAWfUtc_f4fg7P4mXY7Iu7NuuKxab5FO5OtJXAL2kSGr7ShwT1gU_dVRLvJf4NtPwsGPnV_wOwhKSBmmSFFwEoZvl6nKWGdmBLJ5T5WEkd1kb2PYq0DTJDnQM6fKJ_HSxZ1A9yEJGJ_PyfRkhFPedviss_AEh1-VES8H2_rKSh1FMrG6y4XrOgPoohaTzYYu_S1SHig3vmo21IUDgoiENBoCZ1W4SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر برای استفاده از سرویس‌های هوش مصنوعی (AI) مشکل دارید
🤖
این پراکسی را چک کنید
🔍
برنامه یک اپلیکیشنِ نوار منو (Menu bar)  و یک داشبورد محیط ترمینال است که به عنوان یک
مرکز کنترل و مانیتورینگ برای ایجنت‌های Claude Code
عمل می‌کند.
به طور خلاصه، این ابزار کارهای زیر را انجام می‌دهد:
نظارت یکپارچه بر ایجنت‌ها:
وضعیت تمام ایجنت‌های در حال اجرای Claude Code را در یک نگاه نشان می‌دهد؛ بنابراین دقیقا می‌دانید کدام ایجنت در حال کار است، کدام متوقف شده (خطا داده) و کدام منتظر تایید شماست.
بررسی وضعیت اینترنت و سرور:
به صورت مداوم وضعیت اتصال اینترنت شما و سرورهای Anthropic را چک می‌کند تا در صورت توقف کار ایجنت، دلیل واقعی آن (مثلاً کندی اینترنت یا مشکل خودِ Anthropic) را به شما بگوید.
حفظ لوکیشن (Location Fencing):
ایجنت‌های شما را روی یک کشور خاص قفل می‌کند. اگر VPN شما قطع شود، به جای اینکه ایجنت‌ها با خطای دسترسی (مانند خطای 403) از کار بیفتند، درخواست‌های آن‌ها را موقتاً متوقف نگه می‌دارد تا دوباره به اینترنتِ همان کشور متصل شوید و کارشان را از سر بگیرند.
ردیابی مصرف (Usage Tracking):
میزان مصرف واقعیِ محدودیت‌های اکانت شما را (با خواندن دیتای خود Claude) به طور دقیق نمایش می‌دهد.
https://ghhrmnzdh.github.io/tower/
🔗
@whitedns</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1169" target="_blank">📅 09:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1168">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns 15.7.2026.txt</div>
  <div class="tg-doc-extra">48.7 KB</div>
</div>
<a href="https://t.me/whitedns/1168" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/whitedns/1168" target="_blank">📅 09:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1167">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/A8XiKSdYWGu_75QmSSxTaHuZW9THlDF9EaBzeeOyVQafepYOPBXduY8ghVpHCk3w5KGjXZBGNHdR609S8dXqRDQ6LX_70zTPZjxXYJznHHDFsLWGSh13ebduRmIvijga-Y69O7TQYLNnP0t0kgFowAA8AnEydVkXD_y-YyIoSZTx37x55Z10HvwRPS30RntH6hXmI_PIowteqncJQ9lOLwiSCAKklFrBVKOjGB1javT2kzJXzEHP2rG9q38q-lIMiFNI8VUkgbe8jhu94aFUmI0ZoZ2vLWEbDWkZMFvY-aPnKrwRLLHDgiS8QI0vcE-FH_ht7pT0TcWFp3GsEepn8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">15.7.2025
📅
فایل زیر را دانلود کنید
⬇️
1. کانفیگ‌های داخل فایل را کپی و در برنامه v2ray وارد کنید
📋
یا
2. خود فایل را از طریق گزینه import locally در برنامه v2ray وارد کنید
📥
@whitedns
🔗</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/whitedns/1167" target="_blank">📅 09:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1166">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سلام به همه
👋
یک موضوع مهم که خیلی از کاربران VPN با آن آشنا نیستند، مسئله‌ی DNS Leak یا همان نشت DNS است.
شاید برای شما هم پیش آمده باشد که VPN روشن است و آی‌پی شما تغییر کرده، اما بعضی سایت‌ها یا سرویس‌ها همچنان شما را به‌عنوان کاربر ایرانی شناسایی می‌کنند یا دسترسی‌تان را محدود می‌کنند.
DNS نشت یعنی چه؟
وقتی وارد یک سایت می‌شوید، دستگاه شما ابتدا از یک سرویس DNS می‌پرسد آدرس واقعی آن سایت چیست. اگر این درخواست به‌جای عبور از داخل VPN، از طریق اینترنت اصلی یا شرکت ارائه‌دهنده اینترنت شما ارسال شود، به آن DNS Leak می‌گویند.
به زبان ساده، با اینکه VPN روشن است، بخشی از اطلاعات اتصال واقعی شما هنوز قابل مشاهده است.
چرا مهم است؟
DNS Leak ممکن است باعث شود:
• موقعیت یا کشور واقعی شما تشخیص داده شود
• بعضی سایت‌ها همچنان دسترسی شما را محدود کنند
• حریم خصوصی شما کاهش پیدا کند
• اتصال VPN شما آن‌طور که انتظار دارید کامل و امن نباشد
چطور تست کنیم؟
1. ابتدا VPN را روشن کنید
2. وارد سایت زیر شوید:
https://ipleak.net
3. چند ثانیه صبر کنید تا نتیجه نمایش داده شود
4. بخش DNS Addresses را بررسی کنید
اگر در نتیجه نام شرکت اینترنت شما، کشور واقعی شما یا DNSهای مربوط به اینترنت اصلی‌تان نمایش داده شد، احتمالاً VPN شما DNS Leak دارد.
پیشنهاد می‌کنیم همیشه از VPNهایی استفاده کنید که نشت DNS ندارند تا هم حریم خصوصی بهتری داشته باشید و هم سرویس‌ها کمتر بتوانند موقعیت واقعی شما را تشخیص دهند.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/whitedns/1166" target="_blank">📅 08:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1165">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Whitedns-14.7.2026.txt</div>
  <div class="tg-doc-extra">241.5 KB</div>
</div>
<a href="https://t.me/whitedns/1165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/whitedns/1165" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1164">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bCt_iYTMF1FvuS0xYPDO6hmGxXZ2wRFvmcSMqcylW5Z8nLDniYTmciHhgIM6jQLJXlzAg0G7RFPjwfVnKdw-kyA3irjbVo-fTeQka98ZvkhSkyBQFRSbdh07CqzgvErOn-jmRzdtLKX81svqR0L81nTF_LRW-RNkuVQYSb4B28gPcN-u7ExifD7IJDpGrpu4-C2Tna1_dJkVczzlALDH5uWKYXMV0CKQR2TvDIb4qacArzPKvfIE1AxSlyXuJLkpCZ93YZ_RtePntq7vmYS8eCXhV-127ZQmyCuSt4MKs4kQRgb2Zj2i6yDoqBL_2xNhB3vHN14dvY1M6UKVBj4HgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14.7.2026
فایل زیر را دانلود کنید
⬇️
1. کانفیگ‌های داخل فایل را کپی و در برنامه v2ray وارد کنید
📋
یا
2. خود فایل را از طریق گزینه import locally در برنامه v2ray وارد کنید
📥
@whitedns
🔗</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1164" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1163">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qu5wYmabiTyLOwOXx7YyKQkvpyKjhxSMOijJ39uizhrpVQ5WoCLRWEzZ214fk-PrmJCIR-Rw_W8kSNehd-GdKKMucKuBW8ADViLTMI6Hugww_p0_CC38tOi8g7mdnI-E2CuAe6hGVorVuJauShwKiRrVnB_swc1ABPG1zKrJ6dLYHUFP0UNMgUvA3A7Qrr7DysdaLsLWKS5Uk-DNMerPszD2T3_lrZdyia106oz5703dwN0cq4aPWZEv8onomqQEnWY8aVDIt4OfsROLw6dnsNCVIeV1G3BhCAzya4j4OCdX8hP96xlY1VRJ_rg9hvahB91R5lS_KkXl9XKtIJO6cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند کانال WhiteDNS
👉
@WhiteDnsResponder_bot
✅
جواب سریع |
✅
۲۴ ساعته |
✅
رایگان
نحوه استفاده:
۱. روی لینک بزنید
۲. Start
۳. سوالتان را بنویسید
مثال: چطور فیلترشکن نصب کنم؟
/search عبارت — جستجوی مستقیم
/contact — ارتباط با ادمین
⚠️
ربات WhiteDNS در چه زمینه‌هایی جواب می‌دهد:
✅
فیلترشکن و VPN
✅
DNS و تنظیمات اینترنت
✅
آموزش نصب اپلیکیشن‌های WhiteDNS
✅
رفع مشکلات اتصال
✅
Warp و Cloudflare
✅
تنظیمات اندروید، آیفون، ویندوز، مک
✅
سوالات مربوط به قطعی اینترنت
❌
ربات قادر به پاسخ‌گویی به سوالات غیرمرتبط با موضوعات کانال نیست.
💡
نکته: اگر جواب دقیق نگرفتید، سوالتان را طور دیگری بنویسید یا از دکمه جستجو استفاده کنید.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/whitedns/1163" target="_blank">📅 17:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1162">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">White DNS
pinned «
👆
⭕️
⭕️
⭕️
⭕️
موقت :   پرونده اتصال سریع و اسان برای افرادی که دانش و امکان درست کردن کانفیگ ندارند با چند پست بالا بسته شد   این مدل اتصال در صورت قطعی  سراسری کار نخواهد کرد
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1162" target="_blank">📅 17:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1161">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👆
⭕️
⭕️
⭕️
⭕️
موقت :
پرونده اتصال سریع و اسان برای افرادی که دانش و امکان درست کردن کانفیگ ندارند با چند پست بالا بسته شد
این مدل اتصال در صورت قطعی  سراسری کار نخواهد کرد
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1161" target="_blank">📅 17:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1156">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-IP-Scanner-x86_64-release.apk</div>
  <div class="tg-doc-extra">15.6 MB</div>
</div>
<a href="https://t.me/whitedns/1156" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر براتون سوال پیش اومده که لیست ipfronting ها را از کجا آوردیم . پاسخ خیلی ساده است
😊
👇
با استفاده از Whitedns Ip finder
🛠
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases
📂
@whitedns
📱</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/whitedns/1156" target="_blank">📅 17:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1155">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/kwzSYhmRLRcMl1o6noGRyvnXYmVwOU50tXrkGyMSMZNUuUKS2-EDH8PY9BlIrGUePf-mgrONhNeG8dXfyDo6SpyAFbLWM6PU8Ahjj2-HphjCUvc_DKgp_axzwwXfMId-SnIcUSW_IHovL7CMweAMaLYGUUcdsiPnZs7Ql8_GFiANjG5bjHMO2NCmixiyct_836aL5k9AZwWkWVmw7Wfr0cv-vTXubrC9qE3kKY_40kOwptXmeF7OOTdmCSrOLiW6vlPeqKOBMyoHrZcApJeNl1i7qtw0OxwBFDU63nYrT0UqG7qRsXI6hQqkSlSnWwUTHxSCCFJvaZtiu7BTaNeUgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/whitedns/1155" target="_blank">📅 17:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1154">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LzI6Y0G2TAKmCK8yBEI_BeFOFiOi1AstLosJGS8PSS2hQS1Mpytn7i407DvlIk_hkmPfwgHgGBCO0U41EBnHyKGD_1ZnwSMaj4y0x_ASrzDrE4rutUsSqtOWLTHBC6qrH-HFLjSjT_p2W-0QXnBwfWiwrE_k4rZtHoSq-iZ7B3HFtmQMZj4iY9IgOO4B0EAoFGkerPCK9epQy73M_JYVL0FM0TSJcHlYFI-bUL7ghg7yRcW7BkGXep8Q4UObgMYr5cg-qcn_UimkHB4QwSwdGyNJRT656C94MS6sC90lEvYF5de5XIJg6j4SUc3PTKGsYX9HLDCj_GSTuNY3SsPyJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان :
در صورتی که موفق نشدید با برنامه whitedns vpn وصل بشید
🙄
🔌
وارد قسمت advanced بشید و ای پی های زیر را دونه دونه امتحان کنید
👇
🛠
2.189.86.45
2.189.86.102
2.189.86.42
2.189.86.46
2.189.86.41
185.8.173.179
2.189.86.44
45.149.77.160
194.62.43.166
94.101.184.211
37.152.185.169
37.152.182.54
185.226.118.234
185.231.182.55
185.226.118.234
185.231.182.55
185.226.117.67
185.228.236.4
2.189.86.43
2.144.21.79
2.144.21.120
2.144.21.79
2.144.23.129
2.144.21.120</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/whitedns/1154" target="_blank">📅 17:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1152">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">White DNS
pinned «
دوستان :
👋
یک مورد کوچیک در مورد whitedns VPN بگم
📱
این اپلیکیشن بر اساس کانفیگ های متناسب با هسته x-ray یا سینگ باکس هست ، به طور مثال vless ,vmess, Trojan ,....
⚙️
اگر وصل شد حتما اول با مرورگر یک تست بگیرید
🌐
، اگر هیچی باز نشد ، دکمه refresh را بزنید…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1152" target="_blank">📅 16:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1151">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوستان :
👋
یک مورد کوچیک در مورد whitedns VPN بگم
📱
این اپلیکیشن بر اساس کانفیگ های متناسب با هسته x-ray یا سینگ باکس هست ، به طور مثال vless ,vmess, Trojan ,....
⚙️
اگر وصل شد حتما اول با مرورگر یک تست بگیرید
🌐
، اگر هیچی باز نشد ، دکمه refresh را بزنید
🔄
اینقدر این کار را تکرار کنید تا یک کانکشن پایدار متناسب با وضعیت شما براتون پیدا بشه و هر بار تست کنید روی مرورگر
🧪
✅
تیم whitedns
👥
@whitedns
📩</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/whitedns/1151" target="_blank">📅 16:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1146">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.8-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/whitedns/1146" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اپلیکیشن Whitedns vpn 0.0.8
📱
یک برنامه بر پایه هسته‌های x-ray و singbox است که بدون نیاز به وارد کردن اطلاعات و تنها با فشردن دکمه‌های Connect یا Refresh، به راحتی یک اتصال اینترنت مناسب ایجاد می‌کند
🚀
🌐
.
ٌ
@Whitedns</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/whitedns/1146" target="_blank">📅 16:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1145">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Hpx2QSeBBKoVVSyMy9W60kpoOvb9nq5dZogk78WKWfbyemLDi7Gbs4JdQJ_rPFdrPKg6sbEbybTaklLO_I4G5jkRxoALvJbfYRBbYdtN2ujdZfWIjRT8GJKeLVBNXFFIQi4oivGx2bamQXy5L-rbY0G_106j32yEq-prPzQa6_osGIqh2DrWVexTlpwEH5dwexQQIOIpBEWqgFuWakRYJ-TUcYbLdkIENDy3uwqqVfKaWQ08T1G0coQhE5WVQ5l9feh4OT1k9GWlTbnO5wqox2ddDl1f1sBt20p8GhmuZf1cmarRd2_Dz38F7l1N7LNqkK_bPZL6nObWiiVhvkk3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/whitedns/1145" target="_blank">📅 16:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1144">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">برای اینکه دوستان قاطی نکنند، ما دو نوع اپلیکیشن برای اتصال داریم
📱
:
۱
. اپلیکیشن بر پایه پروتکل‌های DNS محور مثل masterdns, stormdns, ...
🌐
مثل Whitedns 1.5.1
۲. اپلیکیشن بر پایه هسته‌های x-ray, singbox که پروتکل‌هایی مثل vless, vmess, ... دارند
⚙️
مثل  0.0.8 whitedns vpn</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1144" target="_blank">📅 16:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1136">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-poll">
<h4>📊 وضعیت اینترنت چطوره ؟</h4>
<ul>
<li>✓ ☺️مثل قبل هست  , وصلیم</li>
<li>✓ 😔اختلال داره ولی وصلیم</li>
<li>✓ 😡اختلال شدید ، به ندرت وصل میشیم</li>
</ul>
</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1136" target="_blank">📅 16:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1135">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🛡
مدتی پیش اپلیکیشنی برای اسکن Resolverهای متد DNS ساختیم که می‌توانید آخرین نسخه‌ی آن را از لینک زیر دانلود کنید:
https://github.com/WhiteDNS/IP-Range-Scout-Android/releases/tag/v0.1.2
اگر امکان اسکن Resolverها را ندارید، می‌توانید از ربات ما استفاده کنید:
@dns_resolvers_bot
همچنین اگر برای اولین‌بار از WhiteDNS استفاده می‌کنید، پیشنهاد می‌کنیم در گروه اصلی، تاپیک «اولین شروع» را مطالعه کنید.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/whitedns/1135" target="_blank">📅 03:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1134">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">درود به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه. با توجه به شرایط کنونی خاورمیانه، ترجیحا هم اپلیکیشن WhiteDNS را نصب/آپدیت کرده و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/whitedns/1134" target="_blank">📅 03:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1133">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">درود به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
با توجه به شرایط کنونی خاورمیانه، ترجیحا هم اپلیکیشن WhiteDNS را نصب/آپدیت کرده و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/whitedns/1133" target="_blank">📅 00:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1129">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwVY17-YGUG3q6k-AiReXwyA1IC2hOcV8BrpL2yjT47bJRvCseApyLWfATpQx_ly3psjbniyc63g3g7IiVz5OmDlwtED6svtoH2cCPZLLf5EgwljWG1PDyaySALwVHUz1etqzdoqD2NBS9lDT5EeLsbDX5IH1vK6XUPT8HOU7HiSk9wJPylZuDTTMiYY_Cp-VyVpEyvvYSBYIsGhAdU6mUAA5WE_Hmp2jHa1pb5KsVMi_uI4QONdLH345G0MC1lw4pPPuihfYguByhy1SkgWqwlJJJhaisZmcvf5lxmJkoG-ER0Uv1GJcdxVUe9oDKW19x3r1qR5PCVR8XK2VLgGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
جایگزین تلگرام برای قطعی کامل اینترنت
در این ویدیو، اپلیکیشن TheFeed را از صفر تا صد بررسی می‌کنیم؛ از اضافه‌کردن کانفیگ و پیدا کردن DNS و ریزالور سالم گرفته تا مشاهده کانال‌ها، دریافت محتوا و فعال‌سازی پیام‌رسان داخلی.
🇺🇦
تماشا آموزش در یوتیوب:
https://youtu.be/Jg0Utycz7DE
این اپ یک پلتفرم مبتنی بر DNS است که برای شبکه‌های محدود و شرایط اختلال یا قطعی اینترنت طراحی شده است. این اپلیکیشن علاوه بر دریافت محتوای کانال‌ها، امکان گفت‌وگوی امن بین کاربران را نیز فراهم می‌کند.
📦
دانلود فایل‌های اصلی TheFeed:
https://t.me/thefeedfile
⚙️
کانفیگ‌های عمومی TheFeed:
https://t.me/thefeedconfig
📢
کانال WhiteDNS:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/whitedns/1129" target="_blank">📅 17:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1127">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1127" target="_blank">📅 14:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1126">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cTdgD0vunV4RezfrSfbj4fryTYzF_zmuJfVUsE1ZA0X-QmPbYMkzAOLbjdGyfHEOmtmdiiotB0DQ82zCgv_83b_802hazsMAPtHxivCNOp8GLuSjY9LyhBmWHVR4LjQcMPpDCF52lRqkvJ9zxD0lqSrIH_8Bqa0483FrpHLAGXnXbCaXWwsg2HGmRFP_KHTn3sWUu4iIXvrHYgC96tdQnJLxnOooCXkipDthbIxH_73NzDLEZoBaKw2WSDNEHP6wXQ8SaCeaVIMcCKQFyd5nVsICPmp4NfeDp--yhA8Mo_JePdCKe3o40EXYZt2fgd5NyBAZnGA29ThDP84d6HQK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند کانال WhiteDNS
👉
@WhiteDnsResponder_bot
✅
جواب سریع |
✅
۲۴ ساعته |
✅
رایگان
نحوه استفاده:
۱. روی لینک بزنید
۲. Start
۳. سوالتان را بنویسید
مثال: چطور فیلترشکن نصب کنم؟
/search عبارت — جستجوی مستقیم
/contact — ارتباط با ادمین
⚠️
ربات WhiteDNS در چه زمینه‌هایی جواب می‌دهد:
✅
فیلترشکن و VPN
✅
DNS و تنظیمات اینترنت
✅
آموزش نصب اپلیکیشن‌های WhiteDNS
✅
رفع مشکلات اتصال
✅
Warp و Cloudflare
✅
تنظیمات اندروید، آیفون، ویندوز، مک
✅
سوالات مربوط به قطعی اینترنت
❌
ربات قادر به پاسخ‌گویی به سوالات غیرمرتبط با موضوعات کانال نیست.
💡
نکته: اگر جواب دقیق نگرفتید، سوالتان را طور دیگری بنویسید یا از دکمه جستجو استفاده کنید.</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/whitedns/1126" target="_blank">📅 13:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1125">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">White DNS
pinned «
⚠️
⚠️
⚠️
⚠️
اطلاعیه مهم  با بالا گرفتن تنش‌ها و با توجه به تجربه‌ای که از قطعی سراسری اینترنت داشتیم، پیشنهاد می‌کنم دوستانی که تازه به جمع ما اضافه شده‌اند، مطالب زیر را با دقت مطالعه کنند.  در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1125" target="_blank">📅 10:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1124">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🌎
آموزش کامل WhiteDNS Desktop براز مان قطعی اینترنت
لینک مشاهده ویدیو
https://www.youtube.com/watch?v=Mc--GlKw2wg</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/whitedns/1124" target="_blank">📅 05:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1123">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⚠️
⚠️
⚠️
⚠️
اطلاعیه مهم
با بالا گرفتن تنش‌ها و با توجه به تجربه‌ای که از قطعی سراسری اینترنت داشتیم، پیشنهاد می‌کنم دوستانی که تازه به جمع ما اضافه شده‌اند، مطالب زیر را با دقت مطالعه کنند.
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/whitedns/1123" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1122">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMasterDnsVPN</strong></div>
<div class="tg-text">👋
درود،
⬅️
ایران موشک بخوره یا موشک بزنه اعضای اینجا زیاد میشن، همه چیز آروم باشه اعضای اینجا کم میشه، تعداد ممبرای این کانال شده یه چیزی مثل «شاخص پیتزای پنتاگون»
😂
⬅️
ولی من واقعا دوست ندارم، اینترنت قطع بشه و شمارو دوباره سر همون موضوع قبلی اینجا ببینم
😕
امیدوارم وضعیت اینترنت جوری درست بشه که اعضای این کانال صفر بشن، ولی مارو یادتون نره
😁
❤️
پیروز و سربلند باشید.
🤨
با تشکر فراوان،
امین محمودی
🗓
18 تیر ماه 1405</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/whitedns/1122" target="_blank">📅 02:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1120">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge
https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/whitedns/1120" target="_blank">📅 10:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1119">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🛡
معرفی CoreForge برای iOS فیلترشکن ساده و قدرتمند مخصوص آیفون  دوستان عزیز،  اپلیکیشن CoreForge برای iOS آماده تست عمومی شده و می‌تونید از طریق TestFlight نصبش کنید.
📥
نصب CoreForge از TestFlight: https://testflight.apple.com/join/u1vfEHur   CoreForge برای…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/whitedns/1119" target="_blank">📅 10:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1118">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🛡
معرفی CoreForge برای iOS
فیلترشکن ساده و قدرتمند مخصوص آیفون
دوستان عزیز،
اپلیکیشن CoreForge برای iOS آماده تست عمومی شده و می‌تونید از طریق TestFlight نصبش کنید.
📥
نصب CoreForge از TestFlight:
https://testflight.apple.com/join/u1vfEHur
CoreForge برای شرایط سخت اینترنت طراحی شده؛ مخصوصاً زمان‌هایی که اختلال شدید داریم، خیلی از روش‌های معمول وصل نمی‌شن، یا حتی اینترنت به سمت حالت بسته و محدود می‌ره. خلاصه برای همان روزهایی که اینترنت تصمیم می‌گیرد انسانیت را ترک کند.
این اپ دو حالت اصلی دارد:
✍️
RelayForge
حالت پیشنهادی و روزمره برای استفاده عادی
مناسب وب‌گردی، اپلیکیشن‌ها، تماس، شبکه‌های اجتماعی و استفاده عمومی
✍️
DnsForge
حالت اضطراری برای زمان‌هایی که بیشتر روش‌ها بسته شده‌اند
این حالت از تونل DNS استفاده می‌کند و برای شرایط قطعی شدید یا اینترنت ملی می‌تواند کمک‌کننده باشد. سرعتش مثل VPN معمولی نیست، اما برای دسترسی اضطراری، پیام‌رسان، وب ساده و کارهای ضروری طراحی شده.
🛡
قابلیت‌های مهم CoreForge:
• مخصوص iPhone / iOS
• اتصال ساده و سریع
• پشتیبانی از کانفیگ و اشتراک
• تست و انتخاب بهترین مسیر اتصال
• حالت Full Tunnel
• حالت اضطراری DNS Tunnel
• مناسب دوران اختلال شدید و قطعی اینترنت
• طراحی شده برای استفاده ساده، حتی برای کاربران غیر فنی
📌
نکته مهم:
DnsForge آخرین راه‌حل است. یعنی اول از RelayForge استفاده کنید، اگر روش‌های معمول جواب ندادند، سراغ DnsForge برید. اینترنت خودش به اندازه کافی اذیت می‌کند، ما دیگر لازم نیست داوطلبانه سخت‌ترش کنیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/whitedns/1118" target="_blank">📅 10:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1117">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♨️
معرفی ربات جدید WhiteDNS برای راه‌اندازی و مدیریت سرور شخصی MasterDNS
♨️
ربات جدید WhiteDNS آماده استفاده است.
👉
@WhiteDNS_installer_bot   این ربات به شما کمک می‌کند بدون نیاز به درگیر شدن با مراحل پیچیده نصب، سرور شخصی MasterDNS خودتان را روی VPS راه‌اندازی…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/whitedns/1117" target="_blank">📅 06:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1116">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZxL3jInwBIQciymExysI2zGyBo665y_1Fa5LtF9N8e8ejjYuFxwcNmpNgwchLssB7ma7B5DgO814Tv6fWYDhOcWuOMEC5nzZ02Ml7j_nlqtCN3SuNMaNvB8a9y40aW0wGsLBjFDWhLdx3BNo00g-8phhE2Q4kiTLcdOi6SIxzFHmZpMVX9tTbDeennezuTiOEL2r-WQEt35YrPF8GyQIDwY4L2wFs22zsgd7c3Bd6U_A3Q8tOhmlRobL7wxDOOkRuR7TcqvwIYhNgzi-KxSCZfq1FKteCm-lTrPfa4Z7aX3-7bj1QilhHLv_Y3dsQ_R5E0JzOYyzubngdIuwdeCAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/whitedns/1116" target="_blank">📅 06:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1115">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✍️
دوستان :
آیدی ادمین که توی دیسکریپشن کانال گذاشته شده، برای حل مشکلات شخصی شما نیست. ممنون که لطف می‌کنید و درد دل‌های روزانه خودتون رو برای ما می‌فرستید، ولی متاسفانه قادر نیستیم پاسخگو باشیم چون تعداد پیام‌ها خیلی خیلی زیاد هست.
اینکه موبایل شما و یا کامپیوتر شما دچار مشکل شده، یا اینترنت شما کار نمی‌کنه، شرکت تامین‌کننده اینترنت شما کلاه سرتون  می‌گذاره، و یا اپلیکیشن‌هایی که ما گذاشتیم دچار فلان مشکل هست و غیره رو برای آی‌دی ادمین نفرستید، توی گروه مرتبط با خودش مطرح کنید.
آیدی ادمین فقط و فقط برای مواردی هست که شما قادر نیستید توی گروه های عمومی ما براش پاسخی پیدا کنید (که تقریبا غیر ممکن است )و یا گزارش و یا یک مورد خیلی فوری را میخواهید به دست تیم ما برسونید
در ضمن بازم تاکید می‌کنیم برای اون دسته از دوستان طلبکار و بی ادب  ، شما حقوق ما را نمی‌دید و ما هم از جایی بودجه نمی‌گیریم ، ما بدهی به شما نداریم ، بی ادبی شما جوابش فقط بلاک شدن و حذف شما از کانال و گروه های ماست ،
از امروز مواردی غیر مرتبط به هیچ عنوان پاسخ داده نمیشود
سپاس
❤️
تیم whitedns</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/whitedns/1115" target="_blank">📅 10:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1114">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا
اگر داخل پنل های نهان و bpb یا هر فیلترشکنی که دارید مشکل باز شدن یه سری اپلیکیشن ها رو دارید(تلگرام،یوتوب و...) طبق تنظیمات زیر داخل هر کلاینت برید این تنظیمات رو داره:
Dns:
💎
9.9.9.12
8.26.56.26
8.8.8.8
8.8.4.4
208.67.220.220
208.67.222.222
Fragment:
✅
Google.com
Length:10-20
Interval:10-20
Packets:1-1
💡
نکته:قسمت فرگمنت بیشتر برای مشکل آپلود یا باز نشدن اپ هاست لذومی نیست حتما روشن کنید.
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/whitedns/1114" target="_blank">📅 04:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1113">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/iaOHAqYDoVvKULy2NAuc0vFGdLNNVh3Ib-OraeuYj_yIx1rufOlHAUifSDeL7ZwfvO0aY2kQUvqTgCykhTDBsZPsbMOy772W0cXMubsBLocs-9dC-yXedeCUzZ3hQQZ-7t3JDlkLEsooXN43qGEWYZl86420Oyv6_n7rfOF03Bqy1EZ0f8N3o63-9wFLEyifNPfpje7sdN7lmNaxXFvoUvDeoYbnFGhElv5gsNYPCH42_SbheG62L0CMKEw6athmKsi7hqiIuw1Yn-2mODSJUY9NFEJKU1a70FrcKLQZsQpV5JSWSSjcwfSm76YNTYO-kx065HU_YVhOKtzzIJL4jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/whitedns/1113" target="_blank">📅 20:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1110">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhitednsProxyProfiler-Android-v1.0.7.apk</div>
  <div class="tg-doc-extra">55.4 MB</div>
</div>
<a href="https://t.me/whitedns/1110" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پروفایلر پروکسی WhiteDNS نسخه ۱.۰.۷
🛠
پروفایلر پروکسی WhiteDNS یک ابزار تشخیصی برای ویندوز و اندروید است که بهترین ترکیب‌های پروتکل پروکسی/VPN را در یک شبکه پیدا می‌کند. این ابزار می‌تواند هم بررسی‌های محلی بدون VPS و هم تأییدات عمیق‌تر مبتنی بر VPS را اجرا کند.
🌐
ویژگی‌های اصلی
اسکن شبکه محلی:
آزمایش سریع بدون نیاز به اعتبارنامه‌های VPS.
🏠
اسکن VPS:
تأیید از راه دور عمیق‌تر با استفاده از اعتبارنامه‌های VPS شما.
🖥
تست پروتکل‌های VLESS، VMess، Trojan، Shadowsocks، WireGuard، Hysteria و HTTP.
🚀
پشتیبانی از انتقال‌های TCP/RAW، WebSocket، gRPC، XHTTP، HTTPUpgrade و mKCP.
🔄
پشتیبانی از ترکیب‌های TLS، REALITY و بدون امنیت (در صورت معتبر بودن).
🔒
تشخیص دسترسی‌پذیری، فیلترینگ، پورت‌های مسدود شده، مشکلات SNI/TLS و رفتارهای شبیه DPI.
🔍
نمایش نتایج تشخیصی دقیق و اطمینان از شواهد محلی.
📊
کمک به شناسایی ترکیب‌های ایمن‌تر پروتکل، پورت، انتقال و امنیت.
🛡
نحوه استفاده
برای یک آزمایش سریع بدون VPS، گزینه
اسکن شبکه محلی
را انتخاب کنید.
⚡️
از
تنظیمات پیشرفته
برای تست پروتکل‌ها، پورت‌ها، مقادیر SNI، انتقال‌ها و انواع امنیتی بیشتر استفاده کنید.
⚙️
وقتی به شواهد قوی‌تر سمت سرور نیاز دارید، گزینه
اسکن VPS
را انتخاب کنید.
🌍
آی‌پی VPS، پورت SSH، نام کاربری و رمز عبور یا کلید SSH خود را وارد کنید.
🔑
اسکن را شروع کنید و پروفایل پیشنهادی کارآمد یا نتایج تشخیصی را بررسی کنید.
✅
نکته مهم
اسکن محلی نشان می‌دهد که شبکه فعلی شما به چه مواردی دسترسی دارد. اسکن VPS شواهد قوی‌تری ارائه می‌دهد زیرا هم سمت کلاینت و هم آنچه واقعاً به VPS می‌رسد را بررسی می‌کند.
🧐
نسخه:
۱.۰.۷
🏷
@WhiteDNS</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/whitedns/1110" target="_blank">📅 19:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1109">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سلام
❤️
توی این آموزش، تمام بخش‌های برنامه V2Ray را از مبتدی تا حرفه‌ای به‌صورت کامل بررسی کردیم؛ از اضافه کردن کانفیگ و Subscription گرفته تا تنظیمات پیشرفته، Routing، آپدیت برنامه و حالت‌های مختلف Tunnel.
🇺🇦
لینک آموزش در یوتیوب:
https://youtu.be/i1-XenoSalk?si=5jbQK3BrGAe4ctsu
اگر موضوع یا نرم‌افزار دیگری هست که دوست دارید آموزش کاملش را ببینید، داخل کامنت‌های یوتیوب یا گروه تلگرام پیشنهاد بدید تا برای آن هم آموزش تهیه کنیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/whitedns/1109" target="_blank">📅 18:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1108">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDr Alan(Dr . A)</strong></div>
<div class="tg-text">چجوری کانفیگ رایگان بسازم بدون دردسر؟
🤔
همه چیز با یک کلیک در WhiteDNS BPB
🚀
مرحله 1:
اول از همه برنامه رو نصب کنید و وارد برنامه بشید
📲
مرحله 2:
وقتی وارد برنامه شدید دکمه Connect CloudFlare رو بزنید
☁️
مرحله 3:
وقتی به مرورگر هدایت شدید، اطلاعات حساب Cloudflare خود را وارد کنید
🔐
مرحله 4:
بعد از وارد کردن اطلاعات به یک صفحه منتقل میشید که از شما میخواد اجازه استفاده WhiteDNS BPB رو از اکانت کلادفلر خودتون رو بدید. برای این کار به پایین صفحه اسکرول کنید و دکمه آبی رنگ Authorize رو بزنید
✅
مرحله 5:
دو حالت وجود دارد. یا شما میخواد یک برنامه رو انتخاب کنید که باید برنامه WhiteDNS BPB رو انتخاب کنید. یا به یک صفحه دیگه منتقل میشید در این حالت به برنامه WhiteDNS BPB برگردید و دکمه I Finished رو بزنید
🏁
﻿
مرحله 6:
بعد از اتصال حساب کلادفلر شما به برنامه، به تب(بخش) Bpb Deployment برید و دکمه eCreat Panel رو بزنید
⚙️
مرحله 7:
به یک صفحه منتقل میشید که میتونید تغییرش ندید و بزارید در حالت پیش فرض بمونه و دکمه آبی رنگ Create Panel رو بزنید
مرحله 8:
بعد از کمی صبر پنل شما با موفقیت ساخته میشه. دکمه Subscriptions رو بزنید و اولین ساب رو کپی کنید
📋
مرحله 9:
میتونید اون لینک ساب رو در برنامه های v2ray / v2box ... وارد کنید یا از داخل تب VPN در برنامه WhiteDNS BPB لینک رو وارد کنید و همونجا به کانفیگا وصل بشید
🌐
⚠️
توجه:
به هیچ وجه از ایمیل های فیک و رندوم استفاده نکنید
🚫
حتما باید اکانت کلادفلر شما Verify شده باشه در غیر این صورت با خطا مواجه میشید
❌
اگر از فیلترشکن استفاده می‌کنید، توجه داشته باشید که باید ایپی شما ثابت
باشه
🛡️
لینک دانلود نرم افزار:
https://t.me/whitedns/1018
@WhiteDNS
با تشکر
🙏</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/whitedns/1108" target="_blank">📅 04:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1106">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy
فیلترشکن قوی و پرسرعت برای تلگرام
https://www.youtube.com/watch?v=pyvB6VSPhwg
@WhiteDNS</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/whitedns/1106" target="_blank">📅 19:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1105">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا یکی از بچها زحمت کشید یه ویدیو کوتاه واسه این ابزار درست کن با کمی بهینه و میانبر واسه دریافت توکن که میتونید ببینید و واسه خودتون و خانوادتون فیلترشکن رایگان بسازید
✅
ویدیو یوتیوب:
📹
https://www.youtube.com/watch?v=e8FNffowfYo
بات دکی:
👑
@itsyebekhebot
نوا پروکسی دریافت توکن:
✅
https://novaproxy.online/install
داشبورد کلودفلر:
💎
https://dash.cloudflare.com
ایمیل فیک:
⚡️
@TempMail_org_bot
خلاصه: داخل ویدیو نحوه دریافت توکن آسون تر شده و این که یه سری بهینه سازی هم داخل ویدیو هست
❗️
@yebekhe
👑
@mehdisedighinasab
💎
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/whitedns/1105" target="_blank">📅 16:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1102">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">↗️
تعداد کانکشن های موفق WhiteDNS VPN در ۲ هفته به ۱۰۰هزار رسیده
.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/whitedns/1102" target="_blank">📅 15:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1101">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRh-YQt2CNxXLEjgWpYtXqyInI822ROy3B3-dkCvTJz9wb2-9CT6HPRHOwhbUQrtMa7OD0_93woBPOAAOlvPFX7pPYLROuSMM_mwJIbnqi7-uJrrX0Uc2NhRK1L12pYoZec34yiXpNMMKL8-baHMKa0A2rq3ned_aq1oGEfHgyoCS_BUBkJdvIm5Fq1iLYmmZfSU6XVu9NSSuxNL9WiKk5PnTyI305lXed0-28MtltHMfxPv3qXltVIqBzJFGlshQpPZzI32Ftlpdm5ywuN7vlq7QwVOOiS0VVY_Bb_alnt61Whn1Cc7nFAt1ZP5PajDbVedUHvLHliLDJa1OJg_fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📇
دوستانی که امکان اسکن ندارند، می‌توانند از تاپیک «IP تمیز» در گروه استفاده کنند. دوستان دیگر IPهای تمیز را آنجا به اشتراک گذاشته‌اند و می‌توانید از همان‌ها استفاده کنید.
لینک گروه
https://t.me/+-Uc2AHI2d8Q2MzA0
آموزش استفاده از IP سفید
https://youtu.be/N5hKuWXp37w?t=1092&si=mdL0Q8Q9H039IAiL</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/whitedns/1101" target="_blank">📅 08:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1100">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=aqu7Yxkj31nVNL9cOdqPexp5YAt_wneb56TUEL4aEdps60d6EavPVUqpTg7QAk4ViwgDA1o_ILX7NON1ZJ02CktNrBRIEmlPnlrmEXk41O-tUtmHF4iB36sPs1Wug0Jc0VdyRqBXT6anKAM1W9pmB57kPS4lhaV3eMa3wluomvoRyLGQGDEGNg6NJUUAjaNPGQWyfPDqG_qjOPKBVpbj8e2XHLrnpUIrjd5ctBdFXOct0Bfjdt0Q_2vxHiEVjPeibVzH0ZR6BydTZr92zGvSHUr0GhjUeNDjWiODOBqOhby9dDYvb3w7iLvENz0efaHEzYfxtk_Nf76n8ud2luhiRYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=aqu7Yxkj31nVNL9cOdqPexp5YAt_wneb56TUEL4aEdps60d6EavPVUqpTg7QAk4ViwgDA1o_ILX7NON1ZJ02CktNrBRIEmlPnlrmEXk41O-tUtmHF4iB36sPs1Wug0Jc0VdyRqBXT6anKAM1W9pmB57kPS4lhaV3eMa3wluomvoRyLGQGDEGNg6NJUUAjaNPGQWyfPDqG_qjOPKBVpbj8e2XHLrnpUIrjd5ctBdFXOct0Bfjdt0Q_2vxHiEVjPeibVzH0ZR6BydTZr92zGvSHUr0GhjUeNDjWiODOBqOhby9dDYvb3w7iLvENz0efaHEzYfxtk_Nf76n8ud2luhiRYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">https://www.youtube.com/watch?v=Z069VNFAgAc
ایجاد بی‌نهایت آدرس ایمیل با یک دامنه روی کلودفلر
📧
آیا می‌دانستید می‌توانید با استفاده از قابلیت Email Routing در ، بی‌نهایت ایمیل شخصی‌سازی‌شده برای دامنه خود بسازید و همه آن‌ها را در یک صندوق دریافت مدیریت کنید؟
در این ویدیو، نحوه راه‌اندازی این سیستم کاربردی را یاد می‌گیرید که برای مدیریت بهتر ایمیل‌ها و جلوگیری از اسپم عالی است.
@whitedns</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/whitedns/1100" target="_blank">📅 17:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1099">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🛡
ویدیو آموزش استفاده از WhiteDNS Scanner
+
WhiteDNS VPN
https://youtu.be/N5hKuWXp37w
با استفاده از اسکنر WhiteDNS می‌تونید آی‌پی‌های تمیز و مناسب Cloudflare رو پیدا کنید، تست سرعت بگیرید، خروجی دقیق بگیرید و بعد از آی‌پی‌های سالم برای اتصال بهتر داخل اپ WhiteDNS VPN استفاده کنید.
در این آموزش یاد می‌گیرید:
- دانلود و نصب WhiteDNS Scanner
- اسکن IP و CIDR
- پیدا کردن IPهای تمیز Cloudflare
- تست سرعت و کیفیت آی‌پی‌ها
- استفاده از خروجی اسکنر
- دانلود و راه‌اندازی WhiteDNS VPN
- اتصال رایگان با گوشی موبایل
- انتخاب IP مناسب برای اتصال پایدارتر
📹
ویدیو
https://youtu.be/N5hKuWXp37w
📥
دانلود WhiteDNS Scanner
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3.4
📱
دانلود اپ WhiteDNS VPN
https://t.me/whitedns/1072
📢
کانال تلگرام WhiteDNS
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/whitedns/1099" target="_blank">📅 15:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1098">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔭
برای دوستانی که می‌خوان سرور شخصی خودشون رو راه‌اندازی کنن، کیفیت VPSهای این سایت واقعاً خوبه:
https://yottasrc.com
چند نکته مهم:
* شماره و کشور ایران رو قبول می‌کنه
* پرداخت با ارز دیجیتال داره، روی شبکه‌های مختلف
* آی‌پی‌های سرورها کیفیت خیلی خوبی دارن
* پورت ۱۰ گیگابیت ارائه می‌ده، که برای سرعت و پایداری واقعاً مهمه
* لوکیشن‌های متنوعی هم داره
برای ساخت سرور شخصی، VPN، DNS یا تست‌های فنی، گزینه‌ی خیلی مناسبیه.
منبع
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/whitedns/1098" target="_blank">📅 11:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1097">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/whitedns/1097" target="_blank">📅 14:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1096">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iB9yF_IL5HEN37U_4-Nc7BF89rluexSieLeXw6gUzvgYYODRtYZ3cG3Ydb6xmHZjIX19dw6oMvSAhHJVAaY6iD-e2-YFLeuCtnP-0zC-U_9jW1Gyqw5MQkeJihsntAeS4zOGB7gu8AeRCfrAAQEcxtQtQdiLUsAqWlQCR7UI_yf_zxDyfJ7xGDqt4Ec7CQTkD4CLy2onLrd_ZWnovcZOZi1GZcp6Fxes82CjMDW-Z8RLk1ZE_F2QfLQDlEP4vm1AwSC52oHXNensWoYMTmK7sbz6nYYXuwks7E1SVjdWxe3SdhV6TCYrRFAchE8HEQdEyhOdrailiv_7ZF-rl1Sysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/whitedns/1096" target="_blank">📅 10:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1095">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/whitedns/1095" target="_blank">📅 05:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1094">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/whitedns/1094" target="_blank">📅 05:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1093">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.
نتیجه این تست، هر ۳۰دقیقه داخل این مخزن گیتهاب برای سرویس های متفاوت قابل دسترسی خواهد بود.
🌎
ساب مناسب اپ های V2Ray, V2rayNG & ...
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
🌎
ساب مناسب Clash Mi, Clash Party
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
🍏
IOS App
: Clash Mi, Karing
👾
Android App
: Clash Party, Karing
👍
Mac App
: Clash Party
📱
Windows App
: Clash Party
📱
Linux App
: Clash Party
@WhiteDNS</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/whitedns/1093" target="_blank">📅 05:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1088">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS Desktop  منتشر شد
👆
👆
👆
👆</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/whitedns/1088" target="_blank">📅 11:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1082">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta6-linux-amd64.deb</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/whitedns/1082" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/whitedns/1082" target="_blank">📅 11:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1081">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdJ7J6Gfg_TleTwYIztoit1Oa0hqaC_R3RFyn5rUJu7vgNMDCIVHbq2nzbJYpurN6J7Hn71z4wBSDuW_-BNsVmz1PX_n5dwk7-8U1w1Kh0NMm-Eh9JPNR3MAZ20onVOqk-Lemfy_V2CB5-td9jJijB4gPCQi92whPRMu2HSXqu0ucyOqb8Xl3e4OCmubHU9Q6bWpFKx34MnBDmi-pDXJEBDmAXBHLzvKCx_gqaMKkcLAZzSvDYVT8ZFjG8Vd47rt2-FUTQEtmGanNMDSOwNb8k5WGcgxqFK7LUGupvIG3Xw79dTY9MsVciyi9l6uWKyhz9S6XFW3oTH15s54d4bJRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS Desktop 1.0.0-beta6 منتشر شد
در این نسخه، ماژول جدید WhiteDNS VPN به WhiteDNS Desktop اضافه
شده.
امکانات این نسخه:
• اضافه شدن WhiteDNS VPN به اپ دستکتاپ
•  انتخاب هوشمند بهترین سرور
•  نمایش کشور و وضعیت سرورها
•  اتصال بدون نیاز به تنظیمات پیچیده
•  تجربه کاربری ساده و روان</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/whitedns/1081" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1080">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⚠️
⚠️
⚠️
⚠️
اطلاعیه مهم
با بالا گرفتن تنش‌ها و با توجه به تجربه‌ای که از قطعی سراسری اینترنت داشتیم، پیشنهاد می‌کنم دوستانی که تازه به جمع ما اضافه شده‌اند، مطالب زیر را با دقت مطالعه کنند.
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
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
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/whitedns/1080" target="_blank">📅 04:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1079">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVOfBCIjHRyB-zLIy_Nv23iu7fQSg15bQXmGXpB73jWzBRAiltsHn78xmZLR-X5NiVkJ0ZaL2bFGYWMerUqzYAKJgKjPHldwjnb9ARnaiw7TQn30gq1MyJ3qi89Wcw5ufoc42h0wjBsyvu2gms6ZEWk5LnTSawi_bBcWsCB-IuPT3ripJib9khKUwyxsgKTNUVIqlCQ7ltEcOMI9FCGZ9WdJww94hK00B0sJR9lnSsESefToCZSQtPyaGfMmZG-hZJzGFbb1dZDygD5haWGg96PQsrBO99I95wU7HhdGj0IiiQ2F8k3CtRUXONMKVO1HUvSeZ7YXWu16jqUk_unh2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
ورژن جدید WhiteDNS Desktop تقریبا آماده شده
در این ورژن همان وی‌پی‌ان داخل اپ اندروید
برای ویندوز، مک و لینوکس قابل دسترسی خواهد بود.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/whitedns/1079" target="_blank">📅 16:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1077">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚀
اسکنر WhiteDNS  اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن. https://github.com/WhiteDNS/WhiteDNS…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/whitedns/1077" target="_blank">📅 03:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1076">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5HyfpD2DRevx6u4XMMKIIj6Ubao9g3VhX5jQopjLUjH8RRXyO8PRb5l8eLgwQCmcOfLZHvQA5J-lzrNWgxRziKMjUB2ZdUKbY9-d6ob1QEwHWtMivlJDulQuFtPnYY6eLAIYTNR72XGFbXGSKGE0VZpE3V2ksAisXWt2MCUvdDz1w_goN5kQ28HSAD9sHOos6Ms3b1QDdeeEBaRA2UnVaQ4q9AwlMy5Od8ttiUEIFaUw0Nl_otSb33dBNtkv7IuZwmQCXK3oAQ5rrsdE81sGEzzYEmLIEOjkS9KVwf8uq7z0UemaeIAZzNJe-x5JAuCQsrHrjkRlyBxPjyq9SpUUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اسکنر WhiteDNS
اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ
مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3desktop
📱
نسخه اندروید
سبک، بهینه‌شده برای موبایل و قابل استفاده روی گوشی، با امکانات کاربردی نسخه دسکتاپ.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3.4
⛏
قابلیت‌ها:
• لیست آماده از ASNهای ایران و ASNهای معروف داخل اپ
• امکان وارد کردن لیست آی‌پی دلخواه
• Health Check برای توقف خودکار اسکن در زمان ناپایداری اینترنت و ادامه بعد از پایدار شدن اتصال
• ادیت یک کانفیگ و ساخت تعداد زیادی کانفیگ روی آی‌پی‌های تمیز با چند کلیک
• استخراج آی‌پی از داخل کانفیگ‌ها
• تست سرعت دانلود و آپلود آی‌پی‌های اسکن‌شده
• انتخاب پورت از لیست آماده یا وارد کردن پورت دلخواه
• لاگ پیشرفته برای بررسی لحظه‌ای روند اسکن
• خروجی کامل و دقیق از نتایج اسکن
متدهای اسکن:
⭐️
IP Scan
برای پیدا کردن آی‌پی‌های تمیز از دیتاسنترهای داخلی و خارجی و استفاده در کانفیگ‌ها.
⭐️
HTTP Scan
برای پیدا کردن آی‌پی‌هایی که امکان استفاده به عنوان پروکسی HTTP رو دارن.
⭐️
SOCKS5 Scan
برای شناسایی آی‌پی‌هایی که می‌تونن به عنوان پروکسی SOCKS5 استفاده بشن.
⭐️
SNI Scanner
برای اسکن دامنه‌های موردنظر روی لیست آی‌پی‌ها و پیدا کردن آی‌پی‌های مناسب برای SNI Spoofing.
⭐️
Speed Test
برای تست سرعت دانلود، آپلود و Packet Loss آی‌پی‌های اسکن‌شده، همراه با رتبه‌بندی خودکار.
این ابزار برای کاربرهایی ساخته شده که می‌خوان با دقت بیشتری آی‌پی‌ها رو بررسی کنن، خروجی تمیزتر بگیرن و زمان کمتری برای تست دستی تلف کنن.</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/whitedns/1076" target="_blank">📅 03:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1074">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1074" target="_blank">📅 17:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1073">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/os2gLq1YgqlmXl6vJglHKRIYTXmxznQmGxe9ysXzW6VcE9GGg5rOOP1LlOPog-1gOVzX9GUndSBdwTQnl5gp_rgl88BxW7iwBeiioDXbveO6bdESFsvVfdRDRopFlrylyLvFfFpORq7tE6ueQbFLXSYo9qLkGJjhh4JWmKjEqXyMYa6XdwgmDXFQ5YPw9rPmDqVYJmAchlZTKYX6qzKARLTawBg0LtvbKxLYHZb4-LD264i-dmqOKiJQxcZIReffU1K_yz03hIs_KEgZiwirZhbMQeaJ-PT8OyjF13ENOHk01uOqh2e4t3fd4GDDkf-RVeM8-Zz_HEy7SHixse9PrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا شد
😎
۷۰۰ اتصال موفق در ۳۰دقیقه گذشته.
ممنون از همه دوستان که کمک ما تست کردند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/whitedns/1073" target="_blank">📅 16:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1068">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.8-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/whitedns/1068" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⭐
نسخه جدید WhiteDNS VPN 0.0.8 منتشر شد
میدونم آپدیت کردن این سرعت یکم برای هم شما هم من سخته. اما تونستم دقیق مورد رو پیدا کنم و فیکسش کن
ی
م.
ممنون از تمام دوستانی که نسخه‌های قبلی رو تست کردند و مشکلات رو گزارش دادند.
⛏
در این نسخه، مشکل لود شدن بعضی سرویس‌ها مثل یوتیوب و اینستاگرام برطرف شده و اتصال‌ها پایدارتر شده‌اند.
✍️
از همه شما بابت اختلال‌ها و مشکلاتی که در اتصال داشتیم صمیمانه عذرخواهی می‌کنیم. ممنون که همراه ما هستید و با گزارش‌هاتون کمک می‌کنید WhiteDNS بهتر بشه.
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/whitedns/1068" target="_blank">📅 15:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1062">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS VPN 0.0.6 منتشر شد
👆</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/whitedns/1062" target="_blank">📅 13:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1057">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.6-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/whitedns/1057" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/whitedns/1057" target="_blank">📅 12:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1056">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4aqB0xTvPxZKGpgR7lxJkZYkm9SHeXhbc-E-cCcxmbIivQ8OCNYi2def2HTj6GWE1PlXp3EYdOPcYeOgwIooPidejPkbR4JWPOBnLEqpjtqkVapvaCy-25TmMX0NyaLbmczDkLKAAxV5pagEGjO12hrhMY6Ej6RPZQ5wzfaRb6dsmNuCp08mhtYWaLAbBRapq4opvCrVD4jSUmvHO4UryPHQmno6fbk-noSpClIGwzIKjevMaD5QFO5f6abIJMy_zuE6pXn8Ytp-IuVdHvrL-RbU-bnAwxqcBUnNdMH-UTZve_BEuz_iUncoeS1508EnDlgSJN29siwGoC4BNF1Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS VPN 0.0.6 منتشر شد
با مشکلاتی که دیروز برامون پیش اومد، فرصت این رو پیدا کردیم همزمان با درست کردن مشکل کردن اسکنر  ها، روی سرعت اتصال هارو هم بهتر کنیم و تا شاید کاربر های بیشتری بتونن بدوم IP Fronting وصل بشن.
🌈
در این ورژن، سرعت اتصال شما با اختلاف زیادی بهتر شده
🌈
اپ پایدار تر از همیشه هستش.
🌈
اپ از نظر ظاهری بهتر شده.
🌈
مشکل اتصال و نمایش کشور اشتباه حل شده.
نتیجه اتصال و سرعت خودتون رو زیر همین
پست بهمون بگید
ممنون از همراهی شما
@WhiteDNS</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/whitedns/1056" target="_blank">📅 12:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1055">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🛡
سلام به همه دوستان عزیز
بابت اختلالی که امروز توی سرویس WhiteDNS VPN پیش اومد واقعاً عذرخواهی می‌کنیم.
متأسفانه یه مشکل فنی برای سرورها ایجاد شده بود که باعث شد بعضی از اتصال‌ها درست کار نکنن. خوشبختانه مشکل برطرف شده و سرورها دوباره در دسترس هستن.
برای اینکه لیست جدید سرورها داخل اپ براتون آپدیت بشه، یکی از این کارها رو انجام بدید:
• یک‌بار دیتای اپ WhiteDNS VPN رو پاک کنید.
• یا اپ رو حذف و دوباره نصب کنید.
• یا حداکثر تا ۳ ساعت صبر کنید تا اپ خودش تنظیمات جدید رو از سرور بگیره.
شاید سرعت کانکت شدن کمی پایینتر آمده باشد اما به زودی اون مورد هم حل میکنیم.
ممنون از صبوری و همراهی‌تون
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/whitedns/1055" target="_blank">📅 08:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1054">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🌎
سلام به همراه عزیز WhiteDNS
تغییرات جدیدی روی سرویس WhiteDNS VPN اعمال شده که از همین حالا در دسترس هستند:
✅
تمام کانکشن‌ها با دقت بالا از نظر DNS Leak بررسی و اعتبارسنجی می‌شوند.
✅
قوانین جدید پراکسی اضافه شده تا سایت‌های داخلی ایران به صورت مستقیم باز شوند و دیگر نیازی نباشد برای دسترسی به آن‌ها VPN را قطع کنید.
✅
تبلیغات از بسیاری از وب‌سایت‌ها حذف می‌شوند تا تجربه بهتری داشته باشید.
برای استفاده از این قابلیت‌ها نیازی به آپدیت اپلیکیشن نیست. کافی است یکی از کارهای زیر را انجام دهید:
• یک‌بار دیتای اپ WhiteDNS VPN را پاک کنید.
• یا اپلیکیشن را مجدداً نصب کنید.
• یا حداکثر تا ۳ ساعت صبر کنید تا تنظیمات جدید به صورت خودکار از سرور دریافت شوند.
ممنون از همگی.
🙏
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/whitedns/1054" target="_blank">📅 13:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1052">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یکی از اولین آدم‌هایی که از این پروژه حمایت کرد،
ویکی‌تجربه
بود. زمانی که اینجا فقط حدود ۱۰۰۰ نفر بودیم.
شاید خودشون هیچ‌وقت ندونن، ولی با به اشتراک گذاشتن پروژه، یکی از کسایی بودن که به ما انگیزه دادن ادامه بدم. بعضی وقتا یه حمایت کوچیک، بیشتر از چیزی که فکر می‌کنیم روی مسیر یه نفر تاثیر می‌ذاره.
خیلی وقته دیگه خبری ازشون نیست. حتی دیدم دامنه سایتشون هم تمدید نشده.
کار درست انجام دادن توی ایران سخته. درست موندن و باوجدان زندگی کردن هم سخت‌تر.
من حتی این عزیز رو از نزدیک نمی‌شناسم و اسم واقعیشون رو هم نمی‌دونم، ولی همیشه قدردان لطفشون بودم.
امیدوارم هرجا هستن، سالم باشن و حال دلشون خوب باشه.
🥲</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/whitedns/1052" target="_blank">📅 16:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1051">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OZEiijNhifGLm54t4cOphWj2EOiqO95BadxsORx4vSwvpO6P9lTJ9OPY5_W_STGXqfJXJRQ8noEGm8tpl18dnfxrf_88ezXUIKfv-4P1PHaWlUOVcP483iN6WaGP9okgs1Ytrbce8HzpFQCQHx3SWS07NjGvGdfmTuakL8ZsoDsb0Ot9L0Swmf3ZZRyZkayHSF5s2rqRSWVKjNENGFbNsfIjm_iOoB5QD3C_IsxSwMYizKnc5YmOXdvnTABph02sVXn7f44ikGmV3CSV9Foo0zdD13tdu-zs8MSmuCaXEuxTUS9LJ9DTJJ7ajopH8jd2gzep7wSFyi-LSEWbsyi8og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویکی تجربه یکی از معدود گروه‌هایی بود که بدون هیچ وابستگی و فاند و رانتی، محیطی رو فراهم کرده بود که افراد نظر واقعیشون رو راجب شرکت‌های ایرانی بگن و نظر بدن.
سر همین خیلی از شرکت‌ها می‌گفتن که کامنت‌هایی که راجب ما گذاشتن رو پاک کن وگرنه شکایت می‌کنیم و فلانت می‌کنیم و... یا حتی می‌گفتن بهت پول میدیم، اما قبول نمی‌کرد.
و همینطور یکی از عواملی بودش که باعث شد آموزش‌های من به دست خیلیها برسن، چون همیشه مطالب رو share میکرد و با وجود هزینه‌های سرسام آور سرورهاش و شرایط سخت مالی، توی قطعی نت کنارمون بود.
و آخرین پست کانال تلگرامشون توی
تاریخ ۲۷ مارچ
(۹۰ روز پیش و اواسط جنگ) بود و همه نگران بودیم که نکنه اتفاقی واسه‌ی مالکش افتاده باشه یا دستگیر شده باشه.
و نتونسته دامنه
https://tajrobe.wiki
رو تمدید کنه. امروز دیدم که دامنه‌ی ویکی تجربه توسط ابرناک گرفته شده(احتمالا یکی از شرکت‌هایی که تهدیدش می‌کرد). و در عجبم از اینهمه بی‌شرفی، که میراث شخصی رو که مشخص نیست مرده یا زنده‌ست یا دستگیر شده یا... رو برداشته و اسم تمام اون پلتفرم رو گذاشته انتقام‌گیری.
امیدوارم که حال ویکی تجربه خوب باشه. دامنه و اینها کمترین اهمیت رو داره</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/whitedns/1051" target="_blank">📅 16:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1050">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">↗️
تعداد کانکشن ها موفق WhiteDNS VPN به ۱۰،۰۰۰ کانکشن روزانه رسیده .
✍️
در حال حاظر تمرکز اصلی ما روی اضافه کردن وی‌پی‌ان به نسخه ورژن ویندوز، مک و لینوکس هستش.
✍️
مواردی گزارش DNS Leak توی کانکشن‌ها داشتیم. درحال آماده کردن سیستمی هستیم که علاوه بر تست‌های سرعت، امنیت و پایداری، تست DNS Leak  هم از کانفیگ ها گرفته بشه.
ممنون از همگی
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/whitedns/1050" target="_blank">📅 10:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1049">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-poll">
<h4>📊 به ورژن جدید  WhiteDNS VPN تونستید وصل بشید؟</h4>
<ul>
<li>✓ آره</li>
<li>✓ نه</li>
<li>✓ ویندوز یا IOS استفاده میکنم</li>
</ul>
</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/whitedns/1049" target="_blank">📅 13:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1043">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-armeabi-v7a-release.apk</div>
  <div class="tg-doc-extra">33.1 MB</div>
</div>
<a href="https://t.me/whitedns/1043" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بیلد کامل اندروید SenPai Scanner، با تشکر از
Hidden-Node
عزیز</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/whitedns/1043" target="_blank">📅 02:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1042">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/whitedns/1042" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">به زودی نسخه یونیورسال هم ارسال میکنیم.</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/whitedns/1042" target="_blank">📅 18:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1041">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🛡
چطور آی‌پی اسکن بکنیم؟
یک آموزش براتون ساختیم تا بتونید با اپ SenPaiScanner روی گوشی اندرویدی خودتون آی‌پی های کلادفلر یا رنج های خودتون رو اسکن بکنید.</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/whitedns/1041" target="_blank">📅 18:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1039">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS VPN 0.0.5 منتشر شد
👆</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/whitedns/1039" target="_blank">📅 09:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1034">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.5-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/whitedns/1034" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/whitedns/1034" target="_blank">📅 08:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1033">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvdvS5Zhme54fxj70TBXPiJ9ZZNFfh8rmzADGnYKcc5J8DzEjL6bgoa8TMtbzPdPZsNZ3eTq0wKg0STtqi6dLFh8lkT8GWDrxCYMI_dInFa6N7o6XNIhYMjsVEIwBuq-5m5-kXSLBUHPGaLr0c72gb7TDDixVCTsxY7U08ckHwxtMF1aYNvnYDUyCiIuB7FNshfNuia_XKKD-xwFVIm_zmGSygfgWDyr_u6wkeIbiZkVpAD66Kk6-uQHcmOfelr-DVPTD_F9QWeEMIgOlE8PELXMRFDFUnSbRhmXuSS8x9KH5T0oaDf84hhEp2w4Yh9G20GRVNeZXfDCLLXs_dQu9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS VPN 0.0.5 منتشر شد
توی این نسخه چند تغییر مهم داشتیم تا اتصال راحت‌تر، سریع‌تر و قابل‌کنترل‌تر بشه:
• موتور اصلی اپ از XRay به Mihomo تغییر کرده
• تم دارک به اپ اضافه شده
• امکان اضافه کردن تا۵ آی‌پی تمی در بخش IP Fronting
• رفع مشکل «کانکت میشه ولی چیزی لود نمیکنه»
• اتصال سریع‌تر بعد از قطع شدن، با استفاده از کش
• اضافه شدن دکمه Refresh برای گرفتن کانکشن جدید و شاید بهتر
• نمایش سرعت دانلود و آپلود
• نمایش آی‌پی‌ای که در حال حاضر به آن متصل هستید
اگر برای اتصال مشکل دارید، احتمالاً باید برای خودتون آی‌پی تمیز اسکن کنید و داخل بخش IP Fronting قرار بدید.
تیم ما همچنان در حال تست و بهتر کردن اپه تا اتصال پایدارتر و ساده‌تری داشته باشید.
ممنون که همراه WhiteDNS هستید
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/whitedns/1033" target="_blank">📅 08:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1032">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دوستان
👋
بچه‌های تیم به صورت مداوم در حال اسکن و بررسی IPها هستن تا همیشه بهترین و تمیزترین IPها داخل اپ در دسترس باشه و شما کمتر درگیر اسکن کردن و پیدا کردن کانفیگ مناسب بشید.
هدف ما اینه که تا جای ممکن فقط اپ رو باز کنید، یک دکمه بزنید و متصل بشید.
اگر فکر می‌کنید قابلیت یا امکانی هست که می‌تونه تجربه استفاده از اپ رو بهتر کنه، حتماً زیر همین پست برامون بنویسید. اگر با مسیر و هدف کلی اپ هم‌خوانی داشته باشه، با کمال میل بررسی و به لیست توسعه اضافه می‌کنیم.
ممنون از همراهی همیشگی شما
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/whitedns/1032" target="_blank">📅 13:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1031">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1031" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1030">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سلام به همه همراهان عزیز،
متاسفانه یکی از اولین اعضای خوب خانواده WhiteDNS که از روزهای اول قطعی اینترنت خالصانه در کنار ما بود، به علت بیماری سرطان از میان ما رفت.
از طرف تیم WhiteDNS، این اتفاق دردناک رو به خانواده، دوستان و همه کسانی که دوستش داشتند تسلیت می‌گیم و آرزوی صبر و شکیبایی داریم.
یاد و خاطره‌اش همیشه در قلب ما می‌مونه.
🖤</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/whitedns/1030" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1029">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا...
پروژه نهان که قبلا متین معرفی کرد رو محصول داداشم دکی واسه دسترسی رایگان به اینترنت آزاد با روش ورکر رو بلدید دیگه؟
حالا میشه آسون تر حتی واسه کسایی که مبتدی و هیچ ایده ای ندارن هم ساخت با کمک ربات:
@itsyebekhebot
شما وارد ربات میشید ساخت پنل نهان رو میزنید وارد سایت کلودفلر میشید و طبق راهنمای کامل پیش میرید و ظرف دودقیقه حتی کمتر با کمترین اطلاع و دانش از ورکر یا هر چیز سخت دیگه ای فیلترشکن رایگان خودتون رو بسازید به صورت رایگان
❗️
نکته:از بات ایمیل فیک هم داخل کلودفلر میتونید استفاده کنید:
@TempMail_org_bot
هر جا هم گیر کردید بهتره که به من پیم بدید
😆
آموزش ساخت پنل نهان
@yebekhe
👑
@xsparvin
🍷
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/whitedns/1029" target="_blank">📅 13:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1027">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه • ظاهر اپلیکیشن تغییر کرده  • امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.  • پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.  • با کمک یکی از بچه های…</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/whitedns/1027" target="_blank">📅 15:33 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
