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
<img src="https://cdn4.telesco.pe/file/DFN3zjzegJRYJQTqQITtl-7IbdKBt3p3RGAscBf4bl0I3Xh-rZa1HsG3fw29RN55Q_ElXe5D20bv2HXT2l2tW13n_SfvKfnrkEBJdHTk7g5MMyIbFj88IwGhiAcsg1dwfT_yeJ-yGZOjGDLJUVoWWj4WvtajsMEmdaCu6fCXjc5dvl_AfHo2dmL0yLwPPGxjBXHCd3Mezc-UDhG3aX6fZUmGn4tP53cjpxijuhnmjKAZMBrhdRL4c8lQDSXgbgg4k-1NGYPR6DfAKQvtYfZl_oexlXpbHFdxZsCPDEwRLlpswqNnC-eZeCj439onztPCDQ4NVMokxtQei6D_btZTfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 107K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 20:10:43</div>
<hr>

<div class="tg-post" id="msg-1931">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Sqi_02uZJvcKHQSWud5PCa3A63OZYq73em0uvjquvYfa1A3bHHmuZo8uEuGlWDQq8RDNmuFU9RqV8j1hvxEm8hlTotCS0zVjS5mF5gGhqqaA1jFRLD9uwmTzKiay2YyHB5P9dxrFvgvJ1sPnyrobGDbz1t_vfvTP9_Xytclco0AYEQ4pf-m9rhgLb-SA-Ggp0ENDR5-H92B0WNzJI5BpC26VDL9Huheu4M2Gcu-SKa-aw1wodVSupKCLOuQmVIiZE3XfuNIM_Ea67wUW8v89d6AZQWrKc-_fBp3LHqPKNg3sMWts1gSJKzKtObdvjQ9hue-6iNcXOYkKgBo0hbMEJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dVXuSgjXB3PD_CMlcF5LSXbPUKnPiknFHMg9CSr6z-0RgRMEGY7agSbLvFU5KFz4fKMi2nK5Ge5OJYCD4IU0w6UI0JECVBuvgFB0BLe8DL6s3fMm9XpOy7MGUcK25fCJXwjmvAY8fRI8PwH_ELPm-4czoaZ_hkfG5J5fUFE3zKxzIvTU0XHGoe30vbLZqL_9EQxo2hiTaXk1hnK71UqecTMfjhQuiFcNQJjwI1ohHR7p53Us8IvSRYn96lX1DdqzQl2rvozeN6il6Abo2HFSMs2dpTMJW02aW7SKIRJZjUF_DBL_FLlFU0xudyBVw7EpLeynXbpdbwwOAwwNaEq3xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این تصاویر هم مربوط به تغییراتی هستش که باید در کلاینت MahsaNG ایجاد کنید دوستان گرامی</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/whitedns/1931" target="_blank">📅 17:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">درود بر همگی دوستان عزیز
😊
یک راهکاری را یکی از بچه های کانال پیشنهاد داده
اسمش رو نمیشه «متد» گذاشت، ولی راهکار خوبی هست.
میتونید امتحان کنید امیدوارم برای شما هم کار کنه
مرحله ۱ — آماده سازی کانفیگ
ابتدا یک کانفیگ از هر پنلی که میخواید (مثلاً BPB و ...) بگیرید و متد Fragment + Fingerprint رو روی اون اعمال کنید. برای این کار، نصب کلاینت PattNG لازمه:
🔗
https://github.com/patterniha/PattNG
مرحله ۲ — آموزش اعمال متد
۱. کانفیگی که از پنل گرفتید رو در کلاینت وارد کنید.
۲. روی آیکون ویرایش (مداد) کانفیگ بزنید و مقادیر زیر رو اعمال کنید:
address:
188.114.97.6
(or any clean ip)
finalMask: tlshello-0-len
fingerprint: unsafe
cipherSuites: semi-python
۳. بعد از اعمال، یک تست بگیرید و سرعت رو بررسی کنید.
⚠️
نکته: من به تازگی متوجه شدم سرعت متد افت کرده — و به نظر «فیلترچی» عاملش هست، بگذریم!
😅
برای افزایش سرعت این متد، دو راهکار داریم:
راهکار اول — ساخت کانفیگ ترکیبی (Chain)
۱. یک کانفیگ «اتر» با قابلیت سایفون روشن و پروتکل WireGuard بسازید (نوع پروتکل برای هر اپراتور فرق داره، نوع اتصال سایفون هم خودکار).
۲. کانفیگ ساخته شده رو در کلاینت، از بخش «افزودن کانفیگ»، گزینه یChain Proxy رو انتخاب کنید.
۳. دو کادر خالی ظاهر میشه:
- یک اسم دلخواه بذارید (پیشنهاد من: «فیلترچی احوال مادر گرامی چطوره؟»
😄
)
- در کادر اول: کانفیگ BPB که متد روش اعمال شده
- در کادر دوم: کانفیگ اتر
- بعد دکمهی Save رو بزنید.
۴. حالا سرعت رو روی منطقهی خودتون تست کنید. اگه کارتون رو راه انداخت که عالیه؛ اگه سرعت ضعیف بود، برید سراغ راهکار دوم.
راهکار دوم — کلاینت مهسا NG
۱. کلاینت MahsaNG رو از گوگل پلی دانلود کنید:
🔗
https://play.google.com/store/apps/details?id=com.MahsaNet.MahsaNG
۲. همون کانفیگ BPB که متد روش اعمال شده رو کپی و در مهسا NG وارد کنید.
۳. نحوهی انجام کار رو به صورت تصویری براتون میگذاریم
موفق باشید!
🚀
به امید آزادی
🫡
@whitedns</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/whitedns/1930" target="_blank">📅 17:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
ForgeCore برای macOS تأیید شد!  نسخهٔ مک ForgeCore از ریویو اپل گذشت و حالا روی TestFlight در دسترسه.
🚀
📥
دانلود و نصب: https://testflight.apple.com/join/Z4rvxEwk
⚠️
اگه قبلاً نسخهٔ مک رو نصب کرده بودید: اول اپ رو کامل پاک کنید، بعد از لینک بالا دوباره…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/whitedns/1929" target="_blank">📅 08:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1926">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCoreForge</strong></div>
<div class="tg-text">✅
ForgeCore برای macOS تأیید شد!
نسخهٔ مک
ForgeCore
از ریویو اپل گذشت و حالا روی
TestFlight
در دسترسه.
🚀
📥
دانلود و نصب:
https://testflight.apple.com/join/Z4rvxEwk
⚠️
اگه قبلاً نسخهٔ مک رو نصب کرده بودید:
اول اپ رو کامل
پاک کنید
، بعد از لینک بالا دوباره نصبش کنید. بدون این کار ممکنه نسخهٔ جدید درست بالا نیاد.
ForgeCore چیه؟
یه کلاینت شبکه برای وصل شدن به سرورها و کانفیگ‌های پروکسی/VPN خودتون:
- افزودن کانفیگ با
لینک اشتراک
،
QR کد
یا
لینک تکی
- تست
پینگ و در دسترس بودن
همهٔ کانفیگ‌ها
- پشتیبانی از پروتکل‌های متنوع
- اشتراک‌گذاری اتصال روی
شبکهٔ محلی و Personal Hotspot
برای نصب کافیه اپ
TestFlight
رو از App Store بگیرید و لینک بالا رو باز کنید.
🐞
اگه کرش یا مشکلی تو اتصال دیدید، همین‌جا بگید تا سریع درست بشه.</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/whitedns/1926" target="_blank">📅 00:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1925">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlA0yo5CHFJcikMV2T0ZSyZrNRRSOHyBsJRS2oXTdUVD4p2DBUFRP8G5POVZpCCNN-gSkg4DSTcZ1pXl7I2g9fUIVi5rAcAh6dB-v868gAtLa8VVcEH5kZANXs5O1DAEtmasKfu8fAnylk8hSld1hoMFCczin-c-wylW7QcZ5AZKwviezX_rIYH0rwcTQE5P9EMTqJAVxDhKNZjjER4NoQ8UT70AOszPtGfGSGOiL0p85r_XnS264WDDgWCHMaF1N1oFrE1p4wiVAWjJBBeoo-5CTkBTgyk77xaih-MWg7MzSm5jBAeDqndVZI1Yf0ik_MF_e1tSzJTtq9YleboYPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
درود به همه رفقا...
بعد از محدودیت های اخیر در فیلترنت و محدود شدن بیشتر پروتوکل ها و روش های رایگان مربوط به کلودفلر و...
تصمیم بر این گرفتم تست های مختلف طی چند روز انجام بدم و بهتون بگم چه روش هایی/اپلیکیشن هایی متصل هستند تا کمکی به شما رفقا باشه.
بهترین اپلیکیشم اتصال برای همه
دیوایس ها(ios,android,windows) از نظر بنده:
📱
اپلیکیشن defyx vpn: هست،اپلیکیشن کامل و متن باز که از نظر من جای بدافزار هایی مثل جامپ جامپ که روی همه گوشیا نصبه باید از defyx استفاده کنید ویژگی xray و بروز بودن این اپ در
#فیلترینگ
کمک بزرگی میکنه
😍
لینک دانلود بر اساس سیستم عامل متفاوت:
👽
android:
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
🛍️
ios:
https://apps.apple.com/pk/app/defyx/id6746811872
💻
windows :
https://github.com/UnboundTechCo/defyxVPN/releases
🤝
اپلیکیشن بعدی Mahsang:
بهترین روش برای اتصال به مهسا روش هایی مثل سایفون داخل اپ هست که کاملا متصله روی همه نتا فقط نیاز که برنامه رو بریزید و از بالا گزینه P و روی حالت سایفون بزارید تا متصل شید اگر اون حالت جواب نده
#کانفیگ
های EMS در سخت فیلترینگ هم وصله.
🛒
دانلود اپلکیشن Mahsang:
https://play.google.com/store/apps/details?id=com.MahsaNet.MahsaNG
🔥
اپلیکیشن white vpn:
اپلیکیشن بروز با هسته های بسیار خوب و داشتن ساب پیشفرض در برنامه برای وصل شدن در شرایط سخت
#فیلترنت
این اپلیکیشن هم کلاینت و هم روشی برای دور زدن محدودیت ها بر مبنا dns هست:
💻
گیتهاب پروژه:
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🙂
روش های کلودفلر و پترینها:
1️⃣
روش اول:
داخل پنل های کلودفلر(bpb) خود گزینه ECH رو فعال کنید مشکل وصل نشدن حله میشه مهم ترین پیدا کردن ip تمیز بر اساس نت هست بهترین اسکنر از نظر من:
https://github.com/ashanews9776-eng/asha_scanner/releases/tag/v0.8.3
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.1.1
2️⃣
روش دوم:(استفاده از ساب رایگان پترنیها)
پیشنهاد میشه این لینک ساب یا هر کانفیگی از نوع پروتوکل رو داخل اپ های خود پترنیها یعنی
pattng
/
pattn
بزنید اگر هم بلد نیستید میتونید از
ویدیو آموزش استفاده کنید
.
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt#Patterniha-F
💡
توجه:ممکنه بسیاری از روش های دیگه مثل وارپ(AETHER) یا حتی SERVER LESS رو نت شما کار کنه اما این بیشتر بستگی به محدودیت های اینترنت و منطقه شما داره این روش ها رو داخل این پست اشاره نکردم زیرا روی همه نتا متصل نیست و منتظر آپدیت جدید از CluvexStudio و patterniha برای هسته Aether و همچنین sni spoof میمونم و بعد از رفع مشکل معرفی میکنم.
@xsfilterrnet
🙂</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/whitedns/1925" target="_blank">📅 00:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1924">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔥
آپدیت مهم WhiteDNS
فایروال جدید، ترافیک DNS بالاتر از حدود ۶ کوئری در ثانیه را محدود می‌کند و همین موضوع باعث قطع شدن بسیاری از تونل‌ها شده است.
برای اتصال پایدارتر، برنامه را به آخرین نسخه آپدیت کنید
👇
📱
دانلود نسخه اندروید 1.6.4
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.4
💻
دانلود نسخه دسکتاپ 1.2.4
https://github.com/WhiteDNS/WhiteDNS-Desktop/releases/tag/desktop-v1.2.4
⭐️
تغییرات و تنظیمات پیشنهادی
🔹
محدودیت نرخ ارسال کوئری
در تنظیمات پروفایل CottenDNS، گزینه Query Rate Limit را روی ۳ کوئری در ثانیه قرار دهید. ممکن است سرعت کمی کاهش پیدا کند، اما اتصال پایدارتر خواهد بود.
اگر با اضافه کردن Resolverهای بیشتر سرعت بهتر شد، گزینه Rate Limit Counts را روی Per Resolver قرار دهید.
🔹
تصادفی‌سازی زمان ارسال کوئری‌ها
گزینه Timing Mask را روی Light یا Strong تنظیم کنید تا زمان ارسال کوئری‌ها تصادفی شود و ترافیک شما ریتم ثابت و قابل تشخیص نداشته باشد.
🔹
تعویض خودکار دامنه
اگر دامنه سرور مسدود شود، برنامه به‌صورت خودکار به یکی از دامنه‌های جایگزین دریافت‌شده از سرور سوییچ می‌کند؛ بدون نیاز به ساخت پروفایل جدید.
🔹
اتصال پایدارتر
پاسخ‌های جعلی Domain Does Not Exist یا NXDOMAIN که فایروال ایجاد می‌کند، دیگر باعث حذف Resolverهای سالم هنگام برقراری اتصال نمی‌شوند.
👀
محدودیت نرخ ارسال کوئری و تصادفی‌سازی زمان ارسال به‌صورت پیش‌فرض خاموش‌اند. برای استفاده از آن‌ها، تنظیمات بالا را فعال کنید.
🖥
برای مدیران سرور
ابتدا نسخه سرور CottenDNS را به آخرین نسخه آپدیت کنید:
https://github.com/WhiteDNS/CottenDNS/releases/latest
• برای استفاده از Domain Rotation، دامنه‌های جایگزین را در ADVERTISE_DOMAINS قرار دهید
• مقدار ZONE_NS را روی Nameserverهای خود تنظیم کنید تا سرور به کوئری‌های نوع NS مانند یک DNS Server عادی پاسخ دهد</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/whitedns/1924" target="_blank">📅 14:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1923">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مادر بزرگ ۷۰ساله من برای اینکه بتونه با بچش ۱۰دقیقه در روز صحبت کنه VPN استفاده کردن باید یاد بگیره.
باید استرس بکشه که الان قطع میشه، همراه خوبه یا سامانتل، باید بدونه سابسکرسپشن چیه، سرور چیه و ۱۰تا روش امتحان کنه تا به گوش من برسونه که 《مامان VPN من بازم قطع شده》
😭
لعنت بهتون که به دل کوچیک و بزرگ حسرت گذاشتید.
ببخشید یکم شخصیش کردم و میدونم این وضعیت دردسر هممونه و نه فقط من. شاید این در مقابل دردسر خیلی ها حتی چیزی هم نباشه.
خیلی از این متد ها مناسب افراد مسن تر با دانش کم نیست. تا جایی که میتونید هواشون رو داشته باشید
🥲</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/whitedns/1923" target="_blank">📅 13:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1921">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-GUI_0.8.0_x64-setup.exe</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/whitedns/1921" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/whitedns/1921" target="_blank">📅 13:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1920">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u9V2MR17R4Ft852FJIprugorQAt5eTmtqnue_hlV6SXswZh3diXbDuak6eoqU0Jz71uH-QTHMhDS2zuY0yORUHdaOCcY3nBgal5J_sqiq0AmzOzS0gXLOu7JQnxeGHpsQ-gL7Ay5-EmNH42kxqRjW8KK2VudnNcunwgNpgvheJcX6wWfJTgEGH4XZtsZ65Y8-7dSVxzPVhGlugAZo7u6kniTukmGe0b2QWeYIgUvrT81rYb-iosnql5GHuPWgHAgC77DjjuHzCEL4g83WfuSX-ORjO1rsDxGw5zTltXwt04ZNjVIMgdkD3ouPJ6ZH44030L0sTOXjPB0Z8oqWr6MNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه 0.8.0 از Aether-GUI منتشر شد
👋
- آپدیت هسته‌ی Aether به آخرین نسخه
- اضافه شدن شبکه‌های Psiphon و Tor
- اضافه شدن MASQUE-in-MASQUE
- افزوده شدن HTTP proxy، upstream proxy و exit-country
🐱
دانلود از گیتهاب:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.8.0</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/whitedns/1920" target="_blank">📅 13:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1918">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/jAd7dmD5CP59gjB-rcf1hGU_bpPSnGfK9WSAx8vTBp5vbqnqdhxVAxy_ayzcToiBwl9UOdVavrRfPSpHzdCxGVblD8rRxTFx5aN7S--ESxOcmTiijcxXDwlnNiELD9-Oo_2ehZrwWX0X90totauZ12XIO53ekjsHOuFtUTbJgJntIyIdpzSwq32ZLP7cPuyNlNYKyE6oCJ1qRFo8ntLg43kggzfepXjn13GU72Wy_KMjKskWLiDkO0ngnQ7N7AxMEgBBbjrbnng3z-m6QiYJqVmLGiodosT6AiJiPXuQOItdaDgPOB88i6kCX35dmDLfV-4rlZpnMVMQdMQX30N96A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/NzWdGE7qB-1UhTbESgJJSsJgt6t1lhFYmSn6MCkNhrROeGgYXoUOCZ-w2_kl_oirnwRWLulmR0gIBPj2wlNH-t-oB098WThMZUm4qidMWquXZ72yIcKkC_3eY4YxECwVGE4xTcN-EPrp0hGJHXJ59VVggdByssH6QCl4K18LZ7T1Re9SsBQM5qcSEBGh470kMrEJ-51c0GQgjwbw5WZSvFR9awnjG5V2kp_iuBieLktwjpIuUFXsHkEjH7_K1btRaRJF05Bo1NDpdC7y5cwtaG5gTsvRxhc_OzLm8MtwgmRP2nPGW9km5jjxaMldcr4oqvNLeYzgHcqaSDypkU6XYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان
🙋‍♂️
در نرم افزار
whiteaesther
اگر برای اتصال مستقیم با aether مشکل دارید، این احتمال وجود دارد که دستگاه شما به هر دلیلی روی اپراتور کنونی نمی‌تواند هویت WARP/MASQUE ثبت کند
📡
برای حل این مشکل برید routes  و اولی را روی تور  یا سایفون و دومی را روی aether بگذارید و دکمه اتصال را بزنید
⚡️
. صبر کنید تا سبز شود
✅
حالا شما هویت masque خودتان را دارید و می‌توانید از aether به تنهایی یا ترکیبی استفاده کنید
🚀
@whitedns</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/whitedns/1918" target="_blank">📅 13:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1917">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/SE_RCKxf4LCi5LPgHYyNCje20Dj1VYcgHQHKRB1dqYnJxbPpXentWlcXdOUgk8iTTSUSDQQOp1J8QOm4CW2081p7sHGfBFU8POjCA5xu3K1I95elaJ43oiONEsC23t4Lya10zgL6l6ekE-MNTLe14rKCWeMvaWm07tzPi-wTEIzm4Tkd84_Wjr3PjMebV9GGWmZtl8t2qaTsZasZg9CpS_Q7h4fsBnUpJTIZOTDnWTbt0JWvGmHeSH-gR5g3XlWhJOY12-a6ZH_D_V-OjV3zgkXEnYf83i8NrzD0-sGaplfSR6Ix_Fv7bTZO_alpk-kLzrreoVxeS0hZUcLmbsZl1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
اگر WARP محدود شد، چطور از WhiteAesther استفاده کنیم؟
⚠️
طبق گزارش‌های دریافتی، ارتباط UDP با IPهای کلودفلر روی همراه اول محدود شده است. احتمال گسترش این محدودیت به اپراتورهای دیگر وجود دارد، اما هنوز نمی‌توان آن را قطعی دانست.
این محدودیت می‌تواند اتصال
WireGuard و MASQUE H3
را مختل کند؛ با این حال، WhiteAesther مسیرهای دیگری هم دارد.
۱️⃣ ابتدا حالت خودکار را امتحان کنید
در تنظیمات برنامه:
🔹
Traffic → Coverage:
گزینهٔ «کل دستگاه»
🔹
Routes → Carrier:
گزینهٔ «خودکار»
در نسخه‌های دارای این قابلیت، برنامه مسیرهای Aether، Psiphon و Tor را بررسی می‌کند.
⚠️
اولین اتصال روی شبکهٔ محدود ممکن است چند دقیقه( تا پنج دقیقه ) زمان ببرد.
⚠️
۲️⃣ برای اتصال مستقیم، MASQUE H2 را امتحان کنید
از مسیر زیر پروتکل را تغییر دهید:
🔹
Routes → Advanced → Preferred transport → MASQUE H2
H2 روی
TCP
کار می‌کند؛ بنابراین بسته‌شدن UDP به‌تنهایی آن را از کار نمی‌اندازد. البته اگر مسیر TCP هم فیلتر باشد، اتصال برقرار نمی‌شود.
۳️⃣ امکان استفاده از IPv6 را حفظ کنید
🔹
Traffic → Addresses → IPv4 + IPv6
اگر IPv6 روی اینترنت شما قابل‌دسترسی باشد، ممکن است مسیر اتصال باقی مانده باشد. انتخاب این گزینه داخل برنامه، به‌تنهایی روی خط فاقد IPv6 دسترسی ایجاد نمی‌کند.
۴️⃣ تکه‌تکه‌کردن دست‌دهی TLS را امتحان کنید
🔹
Traffic → Advanced → Split the TLS handshake → روشن
این گزینه ممکن است در برابر بعضی روش‌های فیلترینگ کمک کند، اما مسدودشدن کامل IP یا TCP را برطرف نمی‌کند.
۵️⃣ اگر اتصال مستقیم جواب نداد، حامل را تغییر دهید
در
Routes → Carrier
حالت دستی را انتخاب کرده و
Psiphon
را امتحان کنید. گزینهٔ دیگر،
Tor با پل خصوصی obfs4
است؛ معمولاً کندتر است و ترافیک UDP را حمل نمی‌کند.
نام و محل گزینه‌ها ممکن است در نسخه‌های مختلف متفاوت باشد.
⚠️
هیچ‌کدام از این روش‌ها اتصال را تضمین نمی‌کند. بسته‌شدن WARP لزوماً به معنی ازکارافتادن کل WhiteAesther نیست؛ نتیجه به مسیرهای باز روی اینترنت شما بستگی دارد.
تشکر ویژه از
@patt_channel_x
@whitedns</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/whitedns/1917" target="_blank">📅 09:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1916">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">پروتوکل UDP هم به طور کامل روی ip های کلودفلر بسته شد (فعلا فقط روی فایروال همراه اول)
در نتیجه امکان اتصال به warp از طریق پروتوکل wireguard و یا masque-h3 دیگر امکان پذیر نمیباشد.
برای پروتوکل masque-h2 نیز، امکان استفاده از ECH از سمت خود کلودفلر بسته است، بنابراین در حال حاضر فقط با استفاده از IPv6 میتوان از این پروتوکل استفاده کرد.
روشهای جدیدی که بزودی منتشر خواهد شد امکان اتصال کانکشنهای TCP را به کلودفلر فراهم میکنند، در نتیجه، میتوان از آنها برای masque-h2، کانفیگهای ورکر، cdn و به طور کلی تمام اتصالات TCP روی کلودفلر استفاده کرد.
حمایت فراموش نشه
🙏</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/whitedns/1916" target="_blank">📅 09:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1915">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">PattNG v2.3.10-P59
منتشر شد.
امکانات اضافه شده
:
۱. مقادیر متد فرگمنت+فینگرپرینت اکنون به صورت آپشن تو خود اپ اضافه شده، بنابراین برای اجرای متد فرگمنت+فینگرپرینت کافیست:
address:
188.114.97.6
(or any clean ip)
finalMask: tlshello-0-len
fingerprint: unsafe
cipherSuites: semi-python
را انتخاب کنید، و دیگر نیاز به کپی پیست ندارید.
برای اجرای این متد روی کانفیگ‌های اتر نیز کافیست:
finalMask: tlshello-0-len
fingerprint: semi-python
را قرار دهید.
۲. اکنون امکان chain کردن کانفیگ‌های psiphon/tor/warp با هر کانفیگ دلخواهی به صورت
دو طرفه
برقرار شده.
به طور مثال برای chain کردن سایفون با یک کانفیگ دلخواه ابتدا باید یک کانفیگ psiphon-only بسازید و سپس از قسمت Add Proxy chain میتوانید آن را با هر کانفیگ دلخواهی به صورت
دو طرفه
chain کنید.
همچنان برای chain کردن سایفون با خود warp باید از همان منوی aether اقدام کنید (warp -> psiphon/psiphon -> warp)
۳. با توجه به فیلتر شدن دامنه دریافت کلید وارپ، اکنون میتوانید از طریق متد فرگمنت+فینگرپرینت (finalMask+semi-python) و یا حتی ech این محدودیت را دور بزنید و بدون نیاز به فیلترشکن مجزا کلید وارپ را دریافت کنید.
۴. به طور مشابه با توجه به فیلتر شدن دامنه masque-h2, اکنون میتوانید از طریق متد فرگمنت+فینگرپرینت (finalMask+semi-python) این محدودیت را دور بزنید و به پروتکل masque-h2 نیز متصل شوید.
امیدوارم حمایت فراموش نشه
🙏</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/whitedns/1915" target="_blank">📅 04:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1914">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v0_m8V9wlCBqgxG1gMX9ISS0SgRh9mVeyVklko6kyzwW196aWami_KSXIOV1yzzYs7oubvfBbIJItbowNvLX0N36cgBvopX_VkEhWtersTRYKUf9L7NSAgL7dM97ou1kfeFOltiemu4wkYJQJ6QiGVQqzos04BJBzlDV4Ku0DRTDJWIj_Vaae2qnjg2KpPnkLU-bo9EXLSS8S1b85VKAsRfgCJFpP2m2XQj4kuInL-TlQNtsqDVFbIj38J6nrND2ndJnhJz-o8LR9MvkGlc9K4SxEni0fEsp7kYih_NOFMk7Wk1gcBCsRtAos5WJNu6qxLpAlPoCvdObiwZbx2R7PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity
https://github.com/MatinSenPai/Gemini-Config-Checker
" دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید:
https://t.me/MatinSenPaii/2881
"
کانفیگ‌های رایگان زیاد هست، ولی کدومشون واقعا Gemini و AI Studio رو برای جیمیل خودت باز می‌کنه؟
این ابزار هر کانفیگ رو همون‌طوری تست می‌کنه که یه آدم استفاده می‌کنه: با حساب Google واقعی خودت، توی مرورگر خودت، از مسیری که واقعاً ازش وصل می‌شی. چون Google ریجن رو فقط برای حساب واردشده و بعد از لود شدن صفحه تعیین می‌کنه، تست‌های ساده‌ی «پینگ و API» همیشه همه‌چیز رو سالم نشون می‌دن و دروغ می‌گن.
🔹
دو حالت ساده و پیشرفته برای انواع شرایط
• ساده: کانفیگ‌های خودت یا لیست کانفیگ‌های رایگان (لینک، ساب، base64) مستقیم و بدون زنجیره تست می‌شن
• پیشرفته: کانفیگ‌های رایگان از پشت کانفیگ پایه‌ی خودت تست می‌شن (تو ← کانفیگ پایه ← کانفیگ رایگان ← Google)
🔹
تست واقعی ریجن
• ورود با حساب Google کاملاً لوکال، با Chrome / Edge / Brave خودت؛ نشست فقط داخل حافظه‌ی برنامه می‌مونه، چیزی جایی ارسال نمی‌شه
• AI Studio و Gemini جدا بررسی می‌شن و می‌تونی انتخاب کنی «سالم» یعنی کدوم‌ها
• اول اتصال سنجیده می‌شه تا کانفیگ‌های مرده زود حذف بشن، بعد فقط بقیه به مرورگر می‌رسن
🔹
پروفایل ضد فیلتر
• Finalmask (fragment)، Fingerprint، ALPN، Cipher suites و IP تمیز
• مقدارها رو از خود کانفیگ یا لینک می‌خونه؛ کپی‌پیست کن و تمام
🔹
خروجی
• «کپی با Chain»: کانفیگ کامل و مستقل، آماده‌ی PattN / v2rayN و Xray استاندارد
• خروجی لینک، JSON، و ذخیره در فایل
• انتخاب کانفیگ‌ها، مرتب‌سازی بر اساس تأخیر، و چک‌کردن دوباره
🔹
همه‌جا اجرا می‌شه
• ویندوز، مک، لینوکس: اپ دسکتاپ و نسخه‌ی وب (برای سرور)
• اندروید (APK): فقط تست اتصال؛ اندروید اجازه نمی‌ده برنامه مرورگر رو کنترل کنه، پس بررسی ریجن واقعی رو روی کامپیوتر انجام بده
• رابط فارسی با تم تیره و روشن
• متن‌باز، با موتور Xray-core داخل خود برنامه
این پروژه، به لطف این پروژه‌ها و آدم‌ها ساخته شد (حتما اگر دوست داشتید استار بدید):
• patterniha: PattN / PattNG و مقدارهای ضد فیلتر (Finalmask)
• 0xRadikal/Free-v2ray-Configs: لیست‌های کانفیگ رایگان
• bia-pain-bache/BPB-Worker-Panel
📥
دانلود و راهنمای کامل (فارسی و انگلیسی):
https://github.com/MatinSenPai/Gemini-Config-Checker
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/whitedns/1914" target="_blank">📅 01:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1913">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👆
این کانفیگ ها را هم برای amneziawg روی آپ whitevpn امتحان کنید
یکی از دوستان خوب زحمت کشیدند این کانفیگ ها را بازنویسی کردند
❤️</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1913" target="_blank">📅 19:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1908">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-mx-free-5.conf</div>
  <div class="tg-doc-extra">1.5 KB</div>
</div>
<a href="https://t.me/whitedns/1908" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/whitedns/1908" target="_blank">📅 19:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1907">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دوستان عزیز:
به جز خود سرورهای whitevpn , الان ۶ موتور اضافه شده است که هر کدوم روی یک نوع اپراتور و یا منطقه کار میده
شما باید خودتون موردی که الان کار میده را پیدا کنید .
فیلترینگ مثل سالهای گذشته یک الگوی ثابت نداره و نمیشه یک نوع خاص از فیلترشکن را به شما داد که روی همه چیز کار کنه
ارادتمند
تیم وایت
❤️</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/whitedns/1907" target="_blank">📅 19:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1906">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitevpn3.10.2026.conf</div>
  <div class="tg-doc-extra">2.8 KB</div>
</div>
<a href="https://t.me/whitedns/1906" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/whitedns/1906" target="_blank">📅 19:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1905">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-MX-FREE-13.conf</div>
  <div class="tg-doc-extra">340 B</div>
</div>
<a href="https://t.me/whitedns/1905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/whitedns/1905" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1904">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-MX-FREE-5.conf</div>
  <div class="tg-doc-extra">342 B</div>
</div>
<a href="https://t.me/whitedns/1904" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/whitedns/1904" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1903">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-poll">
<h4>📊 دوستانلطف کنید اول این فایل ها را ذخیره کنید بعد از قسمت پروفابل - افزودن- amneziaWG  -وارد کردن فایل پیکربندی این فایل را وارد کنید و امتحان کنید که ایا وصل میشید یا نه</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/whitedns/1903" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1902">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-poll">
<h4>📊 کدام پروتکل(های) زیر روی شبکه شما کار میکند ؟</h4>
<ul>
<li>✓ سایفون</li>
<li>✓ تور</li>
<li>✓ Ssh</li>
<li>✓ امنزیا amnezia wg v3</li>
<li>✓ IKEV2</li>
<li>✓ سرورهای عمومی whitevpn</li>
<li>✓ سرورهای اختصاصی whitevpn</li>
<li>✓ اتر whiteaesther</li>
</ul>
</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1902" target="_blank">📅 15:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1901">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pVgIuAMMqaG7NzwE3h63srhYKtC_hd011PpG73yGHR6zUsouFye0kEf_RBQvZbcJkL5zOJ8VGZy3OQpVaOdZCzpwIMOkT3UEHbYmY-3TM8RSKBy120MDfwFTbc7M-hc33HhW5GB4LMiPPM3b2sknF95M29HmEySz4pR6lPhz8nfaoWOKYtK9M_H5wVR4ioIRZhC93Oe5DS8xkVh6Y8Gqd93eDwgdgAToVREYmNxKxawt8Kpw4odLu14ICXUvCbGdTUK2XAPLFDLGNsSaPPeC0XmwPpWotsVJk4A6w8sxkTJm4ZykqkwzyG6K6yqInfr0TyVM7mcIQ_jWGwTXt8wahQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای دسترسی به امکانات جدید نسخهٔ آزمایشی WhiteVPN 1.7.0-beta.1 میتونید با مراجعه به تب "پروفایل" - "افزودن" آنها را مشاهده کنید
@whitevpn</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/whitedns/1901" target="_blank">📅 14:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1898">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.7.0-beta.1-universal.apk</div>
  <div class="tg-doc-extra">203.4 MB</div>
</div>
<a href="https://t.me/whitedns/1898" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی WhiteVPN 1.7.0-beta.1 منتشر شد!</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/whitedns/1898" target="_blank">📅 14:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1897">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Xcb_m5eTJkFwOoORQyeHJ1hmtang5zmE9EHoFcokbwQLqGQ17VVOW4QSEbihiY4os1g3jmcMA0lnFCfX01MzK1eUBJftAN_7fxcn3VH94OUJBOOBkxJr-6psEmXqeI7kUY6EWcknp0EN7FNMIfqCyxMjea5cb4pmR6_S5lnW7bqriY-01Y9mJ4LW48Hq8lCbIl5pvl3SZQHtc0LRRBrejmaXrK_4G2dWKD-27Eo-ytKU4_pvq7kWNaVzILh8cWn49nhCaFMl51Y6n6MtUydZEESl5NiWd5Y89Ix9JSPyHrupe2UD1qahH5i0K-WRfsO6J5DB8icRQuFWh0xsxREeOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧪
نسخهٔ آزمایشی WhiteVPN 1.7.0-beta.1 منتشر شد!
⚠️
🔥
در این نسخه، شش موتور اتصال در دسترس هستند:
Psiphon، Tor، SSH، DNS Tunnels، IKEv2 و AmneziaWG
✨
تغییرات اصلی:
• صفحهٔ یکپارچهٔ «پروفایل‌ها» برای مدیریت اشتراک‌ها و اتصال‌ها
• واردکردن کانفیگ AmneziaWG از فایل یا لینک
vpn://
• انتخاب کشور سایفون از فهرست
• هماهنگ‌سازی فرم‌های فارسی و انگلیسی و اصلاح نمایش گذرواژه‌های طولانی
• بهبود پایداری اتصال و قطع سایفون و نمایش ترافیک
⚠️
این نسخه
آزمایشی
است؛ بررسی کامل همهٔ موتورها روی دستگاه‌های مختلف هنوز ادامه دارد. برخی موتورها به سرور و کانفیگ سازگار نیاز دارند. نسخهٔ پایدار
1.6.10
همچنان در دسترس است.
⚠️
📥
دانلود نسخهٔ آزمایشی
اگر مشکلی دیدید، همراه با نام موتور، مدل گوشی و نسخهٔ اندروید گزارش کنید.
@whitedns</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/whitedns/1897" target="_blank">📅 14:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1896">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I9WglfsN_JlhQBVo6MeHGWtChzE59hasDx6_9UHVkWDpD6BvlekhjZQNBiRUW0Dfo211ymU22qGdzfefbj0sc_NGg52PBElhtRWgSxqLrBcYww6h717Icu3rmzwxMTGfZOJEEJWOIWy4so11ZJvAqTY6-Z6Wwohlk_jqtGgOzQ0sGSqj0QueEliuiRsRQv02nCmD4RGCUCQxccd1hj4dNVXb53JJsELXS0yMnJfFChGVoTjB1xVM2X1_CvzuIkiDCMhsjCX23RIXFMPWeRgwYD1lrjimbxsMiTsyZocNCe5t_nS0OArauFGw5yjcpiX8QnF0jDgd0BwaIEj3QX9_GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
عزیزانی که با WhiteAether سخت وصل میشن یا مدام قطع و وصل دارید، این روش رو حتماً تست کنید.
به‌دلیل اختلالات شبکه، ممکنه Endpoint انتخاب‌شده مرتب قطع بشه و Fallback به‌صورت خودکار Endpoint دیگه‌ای رو انتخاب کنه؛ همین سوییچ‌ها می‌تونه باعث کندی و ناپایداری اتصال بشه.
🛠
برای رفع این موضوع :
1️⃣
وارد بخش Routes بشید و از پایین صفحه وارد Endpoint بشید.
2️⃣
اسکن Endpoint رو انجام بدید.
3️⃣
بهترین Endpoint از نظر Ping رو انتخاب کنید و روی اون بزنید تا Pin بشه.
4️⃣
گزینه Fallback رو خاموش کنید.
🚀
حالا دوباره Connect کنید و نتیجه رو تست کنید.
چند نفر با همین تغییر مشکلشون برطرف شده؛ ممکنه برای شما هم در شرایط فعلی شبکه بهتر جواب بده.
@whitedns</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/whitedns/1896" target="_blank">📅 19:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1895">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VUud9rdzEsL_0yQd43c64BybplxBcwOyaK7pSl0hsvRMB8P1H2SWPyMUERlhCEfaDbX5unV9t6OIXkkDtH8EkR89rxuGtuF77IXH6wblcnotRocZKZJXZCkP-8whqY5L18ORkdmC89ZoarX_IxgBybLUX3l-sCEHUF3uhWxrzQnPPiTlWDcV5bn_rU5QoXihECQ1nBiZNKS0ab-ZsxGkQDX1ad2keQkK6MeLkGtDD4fe1Ew9_AEf8yBMs_TzJN3VutMjvUlcVzTqEFPnkPUmmyCgZCidRCkhzeMYxYqVb4i9YGHobpueAPNWK0xPFL2KkYseLuhCHPZ9-5U93mn1qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری (مستر دی ان اس )
⚠️
⚠️
whitedns app config bot/ masterdns config   :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/whitedns/1895" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1894">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-F6NAwUbBwrVwchh89-g8rOoImAhNTR2KvuaLtwxAhRWKNUeBTu6FWCqIEDpW55MmgOs71nLsyc_kjax0ejyvOP1S77ned6oLzIsbnTc6igI4KzKr8stqZdYYNlqzuBxhWVn6Ht_XuyHASv6AFOv9WRTQ3uaZOAyPlmv21JbnB_IqA42SE1oBOjhMQFVKJbBQmjt65x9NPVZZZrZalKGfmoGI1loFTggi36tP1-rZR4R5PpP_2aHnWyT8mBbwS98dIIz0Ofws_g5O9mvUrgZgdgVD32EjvG7VEmg4qspu6qIInck4RfuvJH8QBoFwXbZRhWewZ2njMfGEtlJwHACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به جای توضیح دادن «اون دکمه رو می‌گم»، روش کلیک کن
👀
اگه با Codex یا Claude Code رابط کاربری می‌سازین، احتمالا پیش اومده نصف پرامپتتون صرف توضیح دادن این بشه که دقیقا کدوم قسمت صفحه باید تغییر کنه
😅
ابزار Agentation یه نوار ابزار به پروژه اضافه می‌کنه؛ روی المان موردنظر کلیک می‌کنین و می‌نویسین چه تغییری می‌خواین.
مثلا:
«فاصله این دکمه از عنوان، ۱۶ پیکسل باشه و توی حالت loading عرضش تغییر نکنه.»
⭐️
نکته کاربردیش اینه که بازخورد رو همراه selector و اطلاعات المان به agent می‌رسونه. می‌تونین خروجی Markdown رو کپی کنین یا با تنظیم MCP، کامنت‌ها رو مستقیم در اختیار agent بذارین.
برای Claude Code یه skill راه‌اندازی هم داره:
npx skills add benjitaylor/agentation
بعد داخل Claude Code دستور /agentation رو اجرا می‌کنین.
فعلا به React 18+ و مرورگر دسکتاپ نیاز داره و بهتره فقط توی محیط توسعه فعال باشه. تغییر کد رو agent انجام می‌ده؛ نتیجه رو هم همچنان باید بررسی کنین.
برای رفت‌وبرگشت‌های ریز طراحی، ایده کاربردی‌ایه
🔥
معرفی و دمو
·
راهنمای نصب</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/whitedns/1894" target="_blank">📅 17:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1893">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommmahdi_sz</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJZIkmpI4xO8MEOoIFeXsYjbtJaWy4dHwgM57lX7p4Wh6BWlEuZKfmKrjfeChs1yBdXE6eifaey_rxnRl7zYpxxRPSq-SjVKkirdmMJ44nLgZ7pnKOY7kcZ_KLgrkLWiPk3b_O6QwH_kiCkO-IjaniibwSksq3gUA5RvfPWzCWVzCQAhrgtPtQL1PPEzwuM-cRjw96fn7f-5re1vEtsb0n5mkUcwa5wzYEYwH1KhCcBgHYAsAydm0dpL-IBzY1IKORo0XM-R3TnAreQ0NK9EUOA9VZ460t4ArBgu4SQUuTGcY3sudmVrGs6u3HHrzaqffI64dhoOXc_oIgQ88G0NJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ArasClient | کلاینت قدرتمند اندروید
یک کلاینت مدرن و متن‌باز برای مدیریت کانفیگ‌ها، Subscriptionها و اتصال‌های مختلف، با امکانات پیشرفته برای تست و مدیریت سرورها.
➿
➿
➿
➿
➿
➿
➿
➿
➿
⚡️
Smart Connect
تست هم‌زمان کانفیگ‌ها و مرتب‌سازی بر اساس Latency برای پیدا کردن سریع‌تر گزینه مناسب.
📡
Subscription Management
مدیریت چند Subscription، بروزرسانی کانفیگ‌ها، نمایش حجم مصرفی و زمان باقی‌مانده و امکانات بیشتر برای مدیریت سرورها.
.arasc
فرمت اختصاصی ArasClient برای Import / Export و اشتراک‌گذاری کانفیگ‌ها با حالت Protected.
🔐
Per-App & Routing
پشتیبانی از Per-App، Routing، Proxy Chain و Policy Group در بخش‌های پشتیبانی‌شده.
🔥
پروتکل‌های پشتیبانی‌شده
VLESS • VMess • Trojan
Shadowsocks • Hysteria • Hysteria2
WireGuard • AnyTLS • AmneziaWG
MASQUE • Mieru • SOCKS • HTTP
➿
➿
➿
➿
➿
➿
➿
➿
➿
🌐
Aether / WARP
پشتیبانی از پروفایل‌های Aether و قابلیت‌هایی مثل:
• WireGuard / MASQUE
• ECH و Fragmentation
• Endpoint Scanner
• WARP Key
• Psiphon و Tor
📊
امکانات بیشتر
• تست و مرتب‌سازی جهانی کانفیگ‌ها
• نمایش اطلاعات اتصال و مصرف ترافیک
• تشخیص کشور سرور بر اساس IP
• Backup & Restore
• Dark / Light Theme
• Logcat و ابزارهای عیب‌یابی
• تنظیمات پیشرفته Core و شبکه
➿
➿
➿
➿
➿
➿
➿
➿
➿
😎
Open Source • Android
👩‍💻
GitHub:
https://github.com/ArasTey/ArasClient
🖼️
Telegram :
https://t.me/imArasTey
📥
Releases:
https://github.com/ArasTey/ArasClient/releases</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/whitedns/1893" target="_blank">📅 17:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1892">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مشکل ربات
@WhiteDNS_installer_bot
حل شد
با این ربات میتتونید ازطریق تلگرام روی سرور خودتون MasterDNS نصب و سرور خدتون رو مدیریت کنید.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/whitedns/1892" target="_blank">📅 09:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1891">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSaaGSIiOpQQCeiu8iXWE9AzxbQws_96kY8RbLyKez6_Tpw_OjeVwe86mH_OSo0_I7lUci3p8OCCntbj_G3LQm0hDTJvuIdDcMWScu3nMrt-yv3uyiD-aiVYu15XXCRjSV2um_MmfOo4GH_5MU6SISozHHZtBQsAnCqRGfAsnW1Zfq8OqQdEZd7H1Yl_PbxK5_1sWBkMebosh8xY7k_U3V6-dre0gcaRdV-9pkeAW07NwbQK-okJQFFWdjrsbhNITMhMYLLkcwkzUxSCqrtq5DI84d_vrXIl_unPHkWFlp0d2Qm2WYDxAiGNhKtBOcAfnHXzsTnxJ5vPOjtaJ3fikQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
آموزش جدید رسید!
🥹
✨
اسکن آیپی تمیز با WhiteDNS Scanner و استفاده ازش توی کانفیگ
🔥
💗
از نصب اپ تا تست نهایی، همه‌چیز مرحله‌به‌مرحله توی ویدیو هست
🎀
🎬
ببینینش:
https://youtu.be/GDo6p_z3CAw
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/whitedns/1891" target="_blank">📅 19:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1889">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوست عزیز :
خرید ، فروش ، درخواست خرید ، آگهی فروش هر چیزی که توش پول رد و بدل بشه ممنوعه
🚫
بلافاصله بن میشید</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/1889" target="_blank">📅 15:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1888">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/whitedns/1888" target="_blank">📅 13:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1887">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/whitedns/1887" target="_blank">📅 13:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1886">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/whitedns/1886" target="_blank">📅 13:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1883">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/whitedns/1883" target="_blank">📅 13:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1882">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Blue Knight Panel WispByte.rar</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/whitedns/1882" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/whitedns/1882" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1881">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkVZ_MtK_VMwljsnvYkotNmxyPnfbNbK26TmHXpQ4iqJMsMap1URTWqx0ZNLIIqOLGEhPQK6iJmqTiatWNn-SmUSHozj2OhOfOvupMXmXkeXJj4e4bsIMvR5ORznE-uLigBNUC0zCYFxGfLC5w5pdb2vPo5pVwUEeU8KQeqLijrlUCB1M3_EzL4QvdlN0jkBiDqwSS1MUcttcZhlItC0jQ_mr2tKCVoKkk-V5ArJG5opQCIyl09scyHmlzJL9oAMtmh4ooUs5MXCIqpH6DBCGKzMTDNJGzqWk6qVCM5_mYb-YzWhHkS5n5T-4Cm8zVRwqE3Hnx7PrLMxknuNUwM_bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎀
بچه‌هااا یه آموزش خفن و کاربردی جدید دارم براتون!
🥹
💗
می‌خواین هاست رایگان بسازین و ازش کانفیگ V2Ray رایگان بگیرین؟
👀
✨
توی این ویدیو با Blue Knight Panel همه‌چیز رو از صفر باهم ساختیم و آخرش هم کانفیگ رو تست کردیم
😍
🔥
اگه این چیزا برات جالبه، حتماً یه سر به ویدیو بزن؛ قول میدم ارزش دیدن داره
🫶🏻
🎬
ویدیوی جدید رو ببین:
https://youtu.be/TmHM_yBPOUU
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/whitedns/1881" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1880">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">💬
تعدادی سرور اختصاصی جدید اضافه شد!
دوستان عزیز، برای استفاده از سرورهای جدید، لطفاً از مسیر زیر سابسکریپشن اختصاصی رو تازه‌سازی کنید:
✨
بخش سابسکریپشن
✨
سابسکریپشن اختصاصی
✨
دکمهٔ تازه‌سازی
🔄
فکر می‌کنیم ظرفیت فعلی برای همهٔ کاربران کافی باشه، ولی اگر نیاز به ظرفیت بیشتری باشه، حتماً سرورهای بیشتری اضافه می‌کنیم.
آی‌پی‌های این سرورها اختصاصی هستن و انتظار داریم باهاشون بتونید به‌راحتی به شبکه‌های اجتماعی و تمام ابزارهای هوش مصنوعی دسترسی داشته باشید
❤️</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/whitedns/1880" target="_blank">📅 11:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1879">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-poll">
<h4>📊 الان با چی وصلین ؟</h4>
<ul>
<li>✓ whitevpn</li>
<li>✓ whiteaesther</li>
</ul>
</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/whitedns/1879" target="_blank">📅 11:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1878">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚀
۵۰ سرور اختصاصی اضافه شد!
دوستان عزیز، لطفاً تست کنید و نتیجه رو به من بگید. موقع فرستادن نتیجه، اسم اپراتورتون رو هم بنویسید تا بهتر بتونیم وضعیت اتصال رو بررسی کنیم
🙏</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/whitedns/1878" target="_blank">📅 07:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1877">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🌎
سرور IPهای اختصاصی ری‌استارت شدن
🔭
برای دریافت آخرین تغییرات، برید به:
سابسکریپشن ← سرور اختصاصی ← دکمه تازه‌سازی
بعد از به‌روزرسانی، دوباره وصل بشید.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/whitedns/1877" target="_blank">📅 03:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1875">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⚠️
دوستانی که از نرم افزار whiteasther استفاده میکنند و مشکل ورود به وبسایت ها و یا سرویس های  تحریمی دارند
:
🔥
با یک سری تغییرات که روی سرور exit chain  یا همان زنجیره خروج  دادیم . احتمالا مشکل خیلی از دوستان حل خواهد شد
🛠
برای این منظور کارهای زیر را انجام دهید :
1. وارد ربات
@WhiteDnsChainbot
شوید و کانفیگ(های) مورد نظر خود را انتخاب و دریافت کنید
📥
2.در تنظیمات اپ whiteaesther به مسیرها-زنجیره خروج و در نسخه دسکتاپ به قسمت پیشرفته - زنجیره خروج  بروید و ادرس ساب خودتون را وارد کنید
⚙️
3.کانکت شوید
🚀
موفق باشید
🙏
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/whitedns/1875" target="_blank">📅 17:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1874">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">محدودیت آپلود
۶
پکت رو دوباره دارن اعمال میکنن.
از چند روز پیش برخی سرورهای شخصی دچار این محدودیت شدن.
از دیشب وبسوکتِ (alpn/1.1) کلودفلر هم برای برخی دامنه ها مثل
workers.dev
.* دچار همین محدودیت ۶ پکت شده.
در نتیجه کانفیگ‌های ورکر کلودفلر به صورت عادی در دسترس نیستند.
با ech ,
fragment+fingerprint
و چندین روش دیگه میشه این محدودیت رو بر روی کلودفلر دور زد.
فعلا تغییری در وضعیت warp هم مشاهده نشده.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/whitedns/1874" target="_blank">📅 13:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1873">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">💬
با از کار افتادن سرویس های BPB فشار بیشتری روی سرور های اختصاصی هستش (شاید براتون کار کنه و شاید درست بشه).
ما سعی میکنیم کیفیت سرویس های عمومی رو بیشتر مدیریت کنیم و از شما هم میخوام اگر مایل هستید به ما کمک کنید.
❤️
تنها راه کمک به ما سرویس Patreon هستش و فقط برای ساکنین خارج از ایران قابل دسترسی هستش.
🗺
امروز به ما ماهی ۲۲دلار بهمون کمک میشه اما ماه ها بوده که هزینه های ما بیشتر از ۱۰برابر این هستشو همش از هزینه شخصی پرداخت شده و تا جایی که بتونیم ادامه میدیم.
https://www.patreon.com/cw/WhiteDNS
یک سرور آمریکا
🇺🇲
جدید اضافه کردیم و سرور هایی که براتون کار نمیکرد رو حذف کردیم.
برای دسترسی به سرور جدید، به بخش سابسکریپشن برید و ساب اختصاصی رو بروزرسانس کنید.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/whitedns/1873" target="_blank">📅 13:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1872">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👀
یه تغییر آزمایشی روی
سرورهای اختصاصی
دادیم
فعلاً تعداد سرورها به
۴ سرور
در این کشورها کاهش پیدا کرده:
🇺🇸
آمریکا |
🇸🇬
سنگاپور |
🇫🇮
فنلاند |
🇩🇪
آلمان
آی‌پی این سرورها
هر ۲۴ ساعت یک‌بار تغییر می‌کنه
تا احتمال فیلتر شدن کمتر بشه.
قبل از تست، حتماً اشتراک رو به‌روزرسانی کنید:
بخش اشتراک‌ها → اشتراک اختصاصی → گزینه «تازه سازی»
بعد از به‌روزرسانی، سرورها رو تست کنید و نتیجه رو بهمون بگید
🙌</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/whitedns/1872" target="_blank">📅 06:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1870">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دوستان سلام :
ما برای کانفیگ whitedns ربات داریم
@MasterDnsManager_bot
این کانفیگ ها یک روزه هست ، با حجم محدود
⚠️
به درد افرادی میخوره که هیچی براشون کار نمیده و با یک سرعت خیلی خیلی پایین فقط می‌خوان یک وبسایت چک کنند و یا تلگرام اخبار بخوانند و یا پیام متنی بدهند
این روش سرعتش در بهترین حالت ممکن شاید به ۵۰۰ کیلوبایت برسه
عده ای از دوستان درخواست میفرستند که برای روز مبادا می‌خوایم ، که درخواست رد میشه ، توضیح دادیم که دوستان دلخور نشن
ارادتمند
تیم وایت</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/whitedns/1870" target="_blank">📅 14:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1869">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ImIQNZOX7GMB-3NZuGdsr1ctNtv4fg-raeBAN0j1uS52QoXevBiJ6dc9AuOqCGvfckcpOkwZaj_oMJ3jcRO1sI06r9W3gXCf1YucXIOgK8akcVpPM4uKTx-KSaelmKhTQhG8mznBHwNUIj6BbHRIGTdo9dTTGHZOmueTgVID8NOwD3egXfBPwJA_gEHmZwd2CN2pwELEEo070Djq67OcDDqTmJAvcd8z7nlsSvBqhcUNDUdhRxfmdcg9CfxFzTHbIbQ75oDzVj6gHDzDEkhY5OBLF3raNrJCHwOmFhpyN9FHM0NJvCN7sDQUvked8ixtR7-MZ1Ir0IfaoCdAQtSsAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
اطلاعیه پایان فعالیت ربات
@WhiteDnsResponder_bot
کاربران و همراهان عزیز،
به اطلاع می‌رسانیم که فعالیت این ربات و خدمات مرتبط با آن از امروز به‌طور کامل متوقف می‌شود و پس از این، هیچ‌گونه سرویس، پاسخ‌گویی یا پشتیبانی از طریق این ربات ارائه نخواهد شد.
از اعتماد، همراهی و بازخوردهای ارزشمند شما در تمام این مدت صمیمانه سپاسگزاریم. حضور شما نقش مهمی در مسیر فعالیت این پروژه داشت.
با آرزوی بهترین‌ها برای همه شما
🌹
تیم WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/whitedns/1869" target="_blank">📅 19:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1868">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مهم "
⚠️
⚠️
⚠️
📢
راهنمای تست اتصال WhiteVPN نسخه 1.6.10
لاگ‌های ارسال‌شده از چند دستگاه، نسخهٔ مختلف اندروید، وای‌فای و اینترنت همراه بررسی شدند. در بسیاری از موارد، کاربران فقط چند ثانیه بعد از زدن دکمهٔ اتصال، آن را دستی قطع کرده‌اند؛ درحالی‌که برنامه هنوز مشغول بررسی سرورها بوده است.
در نسخهٔ 1.6.10 برنامه ابتدا سرورهای اختصاصی را آزمایش می‌کند و اگر آن‌ها پاسخ ندهند، سراغ مسیرهای جایگزین می‌رود. این فرایند در شرایط فعلی اینترنت ایران ممکن است
تا دو یا سه دقیقه
طول بکشد.
لطفاً برای تست دقیق، مراحل زیر را به‌ترتیب انجام دهید:
مطمئن شوید نسخهٔ نصب‌شده
WhiteVPN 1.6.10 (85)
است.
وارد تنظیمات برنامه شوید و گزینهٔ
تعمیر اتصال / Repair connection
را اجرا کنید.
بخش
Split Tunneling
را موقتاً خاموش کنید.
در بخش انتخاب موقعیت، گزینهٔ
Automatic / خودکار
را انتخاب کنید.
اگر امکان انتخاب سابسکریپشن دارید، فعلاً
سابسکریپشن عمومی WhiteDNS
را انتخاب کنید.
دکمهٔ اتصال را بزنید و تا
سه دقیقه کامل
برنامه را قطع نکنید.
هنگام اتصال، بین وای‌فای و اینترنت همراه جابه‌جا نشوید و برنامه را از Recent Apps نبندید.
اگر پیام «متصل» نمایش داده شد، حداقل ۳۰ ثانیه صبر کنید و سپس موارد زیر را آزمایش کنید:
بازکردن یک سایت در مرورگر
ارسال یک پیام در تلگرام
بازکردن یک سایت خارجی دیگر
⚠️
اگر برنامه متصل شد ولی اینترنت یا تلگرام کار نکرد:
لطفاً اتصال را بلافاصله قطع نکنید. در همان وضعیت متصل:
اگر برنامه «متصل» شد ولی اینترنت کار نکرد، اتصال را قطع نکنید. در همان وضعیت، از همان گزینه‌ای که قبلاً برای
کپی و ارسال گزارش اتصال
استفاده کرده‌اید، لاگ را کپی و برای ما ارسال کنید. سپس نوع اینترنت، نام اپراتور، مدل گوشی، نسخهٔ اندروید و اینکه سابسکریپشن خصوصی یا عمومی انتخاب شده را بنویسید.
آیا هیچ سایتی باز نمی‌شود یا فقط تلگرام مشکل دارد؟
آیا حالت Always-on VPN یا «مسدودکردن اتصال بدون VPN» فعال است؟
اتصال با سابسکریپشن خصوصی انجام شده یا عمومی؟
اگر برنامه بیشتر از سه دقیقه روی «در حال اتصال» ماند، باز هم ابتدا گزارش را کپی کنید و سپس اتصال را قطع کنید. گزارش‌هایی که بعد از قطع اتصال گرفته می‌شوند ممکن است بخشی از اطلاعات اصلی خطا را نداشته باشند.
بررسی‌های فعلی نشان می‌دهد تعدادی از مسیرهای اختصاصی
AnyTLS
داخل ایران پاسخ پایدار ندارند. در چند آزمایش، سرورهای اختصاصی شکست خورده‌اند ولی برنامه پس از انتقال به سابسکریپشن عمومی با موفقیت متصل شده است. به همین دلیل تا زمان اصلاح مسیرهای اختصاصی، استفاده از
سابسکریپشن عمومی
پیشنهاد می‌شود.
همچنین اگر از نسخهٔ 1.6.9 استفاده می‌کنید و برنامه «متصل» نشان می‌دهد ولی دیتا ردوبدل نمی‌شود، حتماً به نسخهٔ
1.6.10
به‌روزرسانی کنید. نسخهٔ 1.6.9 در بعضی شرایط ممکن بود اتصال ناموفق را به‌اشتباه متصل نمایش دهد.
از ارسال گزارش‌های دقیق شما ممنونیم. این گزارش‌ها مستقیماً برای شناسایی اپراتورها و مسیرهای مسدودشده استفاده می‌شوند.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/whitedns/1868" target="_blank">📅 14:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1866">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⚠️
🔥
تعدادی از دوستان به خاطر فیلترینگ شدید توی منطقه ای که زندگی میکنند توی نسخه 1.6.9 دچار مشکل شده بودند .
کانکشن برقرار میشد ولی ترافیک نداشتند .توی نسخه 1.6.10 این مشکل به طور کامل رفع شده است و احتمالا خیلی از کاربران مثل نسخه های گذشته به راحتی متصل خواهند شد
دوستان تا ما مشکل سرورهای اختصاصی را حل کنیم فعلا از سرورهای عمومی استفاده کنید
⚠️
دوستان چنانچه هنوز برای اتصال مشکل دارید لطفا با نگه داشتن انگشتتون روی دکمه اتصال لاگ برنامه را کپی و برای ایدی ادمین که توی بایو هست بفرستید
ارادتمند
تیم وایت</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/whitedns/1866" target="_blank">📅 11:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1863">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/whitedns/1863" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/whitedns/1863" target="_blank">📅 11:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1862">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/WN8q0IqGMd08OisCohHgJD9CGXweODGLOs8QZ_LC4q2sHDJapZWx5KHdys6TZ-Fiwnvxv_OUtXcaChfbfALZesZuFviTh4GS4W4NLijqJEK9Z6xPWT0LWk8tcBZtFeW-qun0mASs7Nj_TXHt7f-B7Mt8GoBRimVaYc05rWV-G9JntXUujhaER8uaEnSc2G0zgUqwAQnaXkK1Ybwg0922kOfAttL4pdzGQEleSi7pIFLAUefDrOEewVIp6me89v8FX9QvTpcaS6P79W4Mga9R90q33Vb06BM_368FnejueY4XDmouJANNZx0Q83P9cZq1TYfsAjarNJQxxpqL8eQ7hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید WhiteVPN منتشر شد (نسخه 1.6.10)
در این نسخه، مشکل نمایش وضعیت «متصل» در شرایطی که ترافیک در شبکه‌های دارای فیلترینگ شدید از تونل عبور نمی‌کرد، به‌طور کامل برطرف شده است.
تغییرات و بهبودهای این نسخه:
تأیید واقعی اتصال:
وضعیت اتصال تنها پس از تأیید نهایی دسترسی به اینترنت آزاد و پایدار ثبت می‌شود.
سوئیچ خودکار هوشمند:
در صورتی که سرور تنها پراکسی محلی ایجاد کند اما دسترسی واقعی به اینترنت نداشته باشد، برنامه بدون وقفه به سرور پایدار بعدی سوئیچ می‌کند.
بازیابی خودکار اتصال:
بررسی‌های ناموفق مداوم پس از اتصال، مستقیماً وارد چرخه بازیابی و اتصال مجدد خودکار می‌شوند.
ثبات سیستم امنیتی:
حفظ و پایداری رفتارهای قبلی در بازیابی آفلاین و مدیریت خطاهای گواهی (Certificate).
افزایش امنیت اشتراک:
الزام و اعتبارسنجی دقیق لینک‌های اشتراک خصوصی در بیلد‌های رسمی برنامه.
📥
هم‌اکنون می‌توانید نسخه 1.6.10 را دانلود یا به‌روزرسانی کنید.
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🆔
@Whitedns</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/whitedns/1862" target="_blank">📅 11:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1860">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/oj0OehOxqg5ick8XpqqHw5QKxj1099SWpRLtZLhdKUDzUHQr8JVL-qN133nKqT99lmPREtzsD6V_YSN1WTCm_nINFOUwSUaJJ3f9wxGE4OR5qQG1ZLvg3JP-rnxE09kdRs2T-scOfTRpVBUG4Zk0HcG11pyy-N1wRzACb2NWN81JaiABWRbA0cCqdEjRDCHiOuU6W0WUoW5sXabzQJ2Kp6oHzZewlRI8oDKkkccm04SS4ttk3N2l6WKW54J0ws6uD_YWgolOx7RsatVpTf2n_rHLVmkUm8DuAWSyxobhC-PN_9Uc0VLXJDGlpK7rCCrqAt9rDemlZ86Ms_xXg6i_vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات پاسحگو
💬
Support Bot:
@WhiteDnsResponder_bot
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری
⚠️
⚠️
whitedns app config bot  :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/whitedns/1860" target="_blank">📅 18:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1855">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteAestherMobile-1.10.0-universal.apk</div>
  <div class="tg-doc-extra">134.8 MB</div>
</div>
<a href="https://t.me/whitedns/1855" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/whitedns/1855" target="_blank">📅 11:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1854">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/iSu5PP2zPSDQLF1Akz8YTIjcHBcOjvDYrHg0bA7CDBkc_XKquQZCh7G4zrVCCkzHvsmFIoU0iJVLGflVnK6bVnzB1_5ZBj8iBf1tBsru4oJyMpIrkvdayKVtTGUzFtp9ZMHRw4p9jApgAntpJ2VKZd17e8uWuqNePDuc_KPj4KQLcMDaiozk0HGwB6atBPIXyG0GVIfRBAahpN4av7iJj10x8J6HJGf-n6wEd-r5gK_gr7Ef_DWDk8uEM1oX928QHOjbRwqtXtaYCe_BcijvT6rM0uSr2RftUWpVjeKc2YS87SxNksg6UuNezywC6ZM1fn_T2NMmFexy69anBQrjCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Whiteaesther mobile v 1.10.0
حالت خودکار حالا جست‌وجوی مسیر را ادامه می‌دهد و مسیر موفق هر شبکه را به خاطر می‌سپارد
🧠
پایداری اتصال بهتر شده و سرعت دانلود و آپلود در اعلان برنامه دیده می‌شود.
📶
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.10.0
@whitedns</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/whitedns/1854" target="_blank">📅 11:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1852">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-poll">
<h4>📊 الان با چی وصل هستید ؟</h4>
<ul>
<li>✓ اخرین نسخه whitevpn</li>
<li>✓ اخرین نسخه whiteaesther</li>
<li>✓ اخرین نسخه whitedns/coreforge</li>
<li>✓ هیچ کدام</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/whitedns/1852" target="_blank">📅 18:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1851">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آمار اتصال ها داره برمیگرده به حالت عادی
❤️</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/whitedns/1851" target="_blank">📅 13:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1850">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✨
آپدیت WhiteVPN 1.6.9 منتشر شد
❓
بعد از دریافت و بررسی گزارش‌های زیادی که درباره مشکل اتصال برامون فرستادید، چند تغییر توی برنامه انجام دادیم. امیدواریم این تغییرها اتصال رو برای همه‌تون بهتر و پایدارتر کنه.  لطفاً WhiteVPN رو از داخل خود برنامه آپدیت کنید.…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/whitedns/1850" target="_blank">📅 12:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1848">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7N6fnMRfmYZkpiv_09PSGSRQm9TbsByx1pKnJgDjE4aBNYrR2unNKHepQmMUVHIWmyzSKhwTn0Z4lwNp5zFK8WQVjqojHv8um6rAUF0FJg6NWSou05ggDue-HBZxgboiMqcGwphu1cVRaDeRYO699VWyGgSX95uMsRUPpsZGmiw80H8Z9wdMbPDd00oplWj1EaVTl8oVhYXlO_BYzo7pF59VFQI96aZfmCFshYpgCAQupZgG_5TEUJac2GmRrIHHplJPCDmnE02E7euKQNORiUTGGD5uXdv_4I4476sEmNNC2f6RNbOMHJejiFc_fKVf6L6y6a-xTC-SBDO535zPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آپدیت WhiteVPN 1.6.9 منتشر شد
❓
بعد از دریافت و بررسی گزارش‌های زیادی که درباره مشکل اتصال برامون فرستادید، چند تغییر توی برنامه انجام دادیم. امیدواریم این تغییرها اتصال رو برای همه‌تون بهتر و پایدارتر کنه.
لطفاً WhiteVPN رو از داخل خود برنامه آپدیت کنید. نسخه جدید رو می‌تونید از صفحه GitHub ما هم دانلود کنید:
🛡
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.9
💬
بعد از نصب نسخه جدید، اگر هنوز مشکلی داشتید لطفاً بهمون خبر بدید. گزارش‌هاتون کمک می‌کنه مشکل‌های باقی‌مونده رو دقیق‌تر پیدا کنیم.
ممنون که با گزارش‌هاتون کمکمون می‌کنید
🤍</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/whitedns/1848" target="_blank">📅 12:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1847">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/WNC9sW1TpdbjO0xjNlwX8XISeS6Cn63_ZEe-ABs8gRnEwBrHVxValCK1d0JoKRApSieJI_AQavnf1oUuIHoCCVuyAp-KIGxXjdbpwC64ytoZAe3FPhRLfQA6e4zwJEjDc5JJPTSVOUP9qJGg9Z3Reg40NhSQwij7UaVUHoQMlrhfaoONnsUz5LfwHfNT-NFsehsMcKL_T0QsddkAtaEmu06Mt7YkzB0X9DlEtIsETjlNFk1BJ_wgdvIYNsmhECPqLYcMdUor_ZKL_91zfGUv9S73Rh5ghNQHxSX244G766z-pwQuZtTgEsZHWIf4v_FYWVP3KP4Hah0mxZI6hiBRiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧪
نسخهٔ آزمایشی whiteaesther desktop 1.9.7 pre-release
⚡️
اتصال باید خیلی سریع‌تر شود
کلادفلر در همان جواب ثبت‌نام، آدرس دقیقی را که به دستگاه شما داده اعلام می‌کند. موتور آن را می‌خواند، ذخیره می‌کرد، و بعد نادیده می‌گرفت — و به‌جایش حدود ۲۵۰۰ آدرس را یکی‌یکی امتحان می‌کرد تا یکی جواب بدهد.
🔑
و مشکل «دیگر نمی‌توانم ثبت‌نام کنم»
اگر تا حالا پیش آمده که بعد از چند بار نصب مجدد یا اتصال ناموفق، برنامه اصلاً نتوانسته شناسه بگیرد — این همان بود.
ثبت‌نام همان لحظه‌ای که سرور جواب می‌داد خرج می‌شد، ولی تا چند مرحله بعد روی دیسک ذخیره نمی‌شد. اگر وسطش چیزی قطع می‌شد، ثبت‌نام رفته بود ولی شمرده شده بود. و چون سهمیهٔ کلادفلر روی آی‌پی است، همین می‌توانست گوشی روی همان وای‌فای را هم از کار بیندازد.
حالا اول ذخیره می‌شود، بعد بقیهٔ کارها.
🛡
و یک حالت خراب که دیگر ممکن نیست
قبلاً اگر با وایرگارد وصل بودید و MASQUE را امتحان می‌کردید، هیچ‌کدام دیگر کار نمی‌کرد. ساختار جدید طوری است که این وضعیت اصلاً قابل ساختن نیست.
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.7
⚠️
نسخهٔ آزمایشی است — در فهرست به‌عنوان آخرین نسخه نشان داده نمی‌شود و برنامه خودکار پیشنهادش نمی‌دهد.
شناسهٔ فعلی‌تان خودش منتقل می‌شود؛ کاری لازم نیست بکنید و چیزی پاک نمی‌شود.
💬
اگر اتصال سریع‌تر نشد، یا هر چیز عجیبی دیدید، بگویید.
@whitedns</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/whitedns/1847" target="_blank">📅 12:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1845">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/TCSgPsG-94wrOsmrmxBXzbddIOZgm9pO9tXXDtjqYq0qFMRzhobV5_F0XG5a0ZENRT7mFBR_G2J06vzbZAX1QdcfVr3m-y4plsVc-Z83Y_uUJUohWUEExR-HYlAQ12p3z3FIJ8dTcbnHRFSTKxKttn_0ngb-XlrqEh4w8p_q0ir-6yc8OUR7vyxq-RPYpzhc8he558N3SlVVUItQOMYYbat3vu-4O6PiS6z6QnDbaKaovHbYDNw-oyi10BpWKVpMx2GrUXQPewWr2KwWXwDc_IYK664p9WbS2uMfjRX62qS5X1B7CfxrVzGfmJQNWvNdpQ3z1K8cMvMsKf42T_3btg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/N4N6itAUo9fL5eFfe5-efLC_9hAFBs5WFjgqHjVfnTMh_nfcIsaJepmgXMNJNLQM3sJ3UxekAKeFpKp1ygcIbG7__pinGnNuVVI3t253NrCqxL0ZOvUuaFfZvC6eIKNAdmaL7IWABZEn3wU7xrQ-w-UAXYAwFSFcVgbLhgbWX_ivUtbcFkU6M2Ah-fRYn_9tOINQfoovE2HobTGITIzcu2UeoilfStp3sPp5GXqaowrScjcCYcfT_8wZAyygwsHfOcxNjTrVT3anwTPLlP2_n94Qvo9ae6l5xt2hkJ8M1Bm09nCzfiKygILmB5oiInmxaLXtqHlYdV6gcdXiNQD71w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚠️
یک امکانی که توی اخرین نسخه ازمایشی whiteaesther موبایل و دسکتاپ تقویت و بهینه سازی شد - امکان ست کردن dns بود که تقریبا هیچ کس بهش توجه نکرد جز یک گروه خیلی کوچک به نام گیمرهای عزیز
😁
😃
از این امکان استفاده کنید حتما خیلی از مشکلات شما را حل میکنه
🤓
لیست dns های عمومی :
۱. DNSهای عمومی و معمولی
Google
8.8.8.8
8.8.4.4
Cloudflare
1.1.1.1
1.0.0.1
Yandex
77.88.8.8
77.88.8.1
Quad9
9.9.9.9
149.112.112.112
OpenDNS
208.67.222.222
208.67.220.220
AdGuard Unfiltered
94.140.14.140
94.140.14.141
Control D
76.76.2.0
76.76.10.0
DNS.WATCH
84.200.69.80
84.200.70.40
DNS.SB
185.222.222.222
45.11.45.11
AliDNS
223.5.5.5
223.6.6.6
DNSPod
119.29.29.29
—
Hurricane Electric
74.82.42.42
—
Comodo Secure DNS
8.26.56.26
8.20.247.20
Neustar UltraDNS
156.154.70.1
156.154.71.1
LibreDNS
88.198.92.222
—
360 Secure DNS
101.226.4.6
218.30.118.6
OneDNS
117.50.10.10
52.80.52.52
Quad9 Unfiltered
9.9.9.10
149.112.112.10
DNS4EU Unfiltered
86.54.11.100
86.54.11.200
۲. DNSهای امنیتی، ضدتبلیغات و خانوادگی
Yandex Family
77.88.8.7
77.88.8.3
Cloudflare Security
1.1.1.2
1.0.0.2
Cloudflare Family
1.1.1.3
1.0.0.3
AdGuard Default
94.140.14.14
94.140.15.15
AdGuard Family
94.140.14.15
94.140.15.16
OpenDNS FamilyShield
208.67.222.123
208.67.220.123
CleanBrowsing Security
185.228.168.9
185.228.169.9
CleanBrowsing Adult
185.228.168.10
185.228.169.11
CleanBrowsing Family
185.228.168.168
185.228.169.168
Control D Malware
76.76.2.1
76.76.10.1
Control D Ads
76.76.2.2
76.76.10.2
Control D Family
76.76.2.4
76.76.10.4
DNS4EU Protective
86.54.11.1
86.54.11.201
۳. DNSهای رمزگذاری‌شده (DoH و DoT)
Google
https://dns.google/dns-query
Cloudflare
https://cloudflare-dns.com/dns-query
Quad9
https://dns.quad9.net/dns-query
AdGuard
https://dns.adguard-dns.com/dns-query
Control D
https://freedns.controld.com/p0
NextDNS
https://dns.nextdns.io
Mullvad
https://dns.mullvad.net/dns-query
DNS.SB
https://doh.dns.sb/dns-query
AliDNS
https://dns.alidns.com/dns-query
DNSPod
https://dns.pub/dns-query
OpenDNS
https://doh.opendns.com/dns-query</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1845" target="_blank">📅 11:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1844">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">💬
کاربران WhiteVPN روی اندروید
اگر اخیراً داخل برنامه با مشکل اتصال یا اختلال مواجه شدید، لطفاً برای کمک به تست و بررسی مشکل این مراحل رو انجام بدید:
1. ابتدا گوشی رو یک‌بار
Restart
کنید.
2. وارد تنظیمات گوشی بشید و برای WhiteVPN گزینه
Force Stop / توقف اجباری
رو بزنید.
3. سپس
Clear Data / پاک کردن داده‌های برنامه
رو انجام بدید.
4. برنامه رو دوباره باز کنید و اتصال رو تست کنید.
در اکثر موارد بعد از انجام این مراحل مشکل برطرف میشه.
اگر بعد از انجام این مراحل همچنان مشکل داشتید، لطفاً نتیجه رو به ما گزارش بدید تا بتونیم دقیق‌تر بررسی کنیم.
ممنون که با تست و گزارش‌هاتون به بهتر شدن WhiteVPN کمک می‌کنید
🤍</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/whitedns/1844" target="_blank">📅 09:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1843">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tTEr1R666mqL458DhLs1RcTZQLUXh_oGmrU3Ft98F3Im2VYyblTvTOIH3OEJPlJNWF6w_y2EU0tNkRm_9yr9h8_5mtNXzliuc_PuDv3jC_DWEqNc5OdrcVdPi9lfaaca-JsNBAk1jsW60xQmvM7YcGn3DB2xVgDJOoY3Cqoc0sk_tFdvGg8P5q6AJ5PyVMFtEUfUHlimv72JAJm4Yta39OuPmkg8AWEzhJAMGZK411_L6qtTDLArWorI57ii-lor3mE59GEelXh-73lSP_cAYGJR5mn42aD4-twgQeVD9InTc0vjFI6My1lVbqjQLO9pT9DXTl3xSeb92oPZd-ixLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ازمایشی whitevpn desktop1.0.23 pre-release
🧪
این نسخه آزمایشی است، نه انتشار رسمی. برنامه خودش آن را پیشنهاد نمی‌دهد. اگر نسخه پایدار می‌خواهید، روی ۱.۰.۲۲ بمانید.
چه چیزی تازه است:
- فایل نصبی
.msi
برای ویندوز — نصب در Program Files، میانبر منوی Start، و حذف از تنظیمات ویندوز. نسخه zip هم هست.
📦
- گزینه «همه سرورها» — اگر چند سابسکریپشن دارید، از میان سرورهای همه آن‌ها انتخاب می‌کند.
🌐
- پروکسی سیستم و حالت تونل حالا در منوی آیکون کنار ساعت هستند.
⏰
بیشتر از همه به تست فایل نصبی نیاز داریم، چون اولین بار است ساخته می‌شود. اگر ۱.۰.۲۲ را دارید، این را رویش نصب کنید و ببینید درست جایگزین می‌شود.
اگر مشکلی دیدید گزارش بدهید — اگر بتوانید محتوای صفحه Logs را هم بفرستید کمک بزرگی است.
📝
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.23-rc1
@whitedns</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/whitedns/1843" target="_blank">📅 06:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1839">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-poll">
<h4>📊 خیلی از دوستان میگن الان یکی دو روزه اختلال شدید دارند و برنامه های white براشون کار نمیکنه . شما چطور؟</h4>
<ul>
<li>✓ هیچی کار نمیکنه</li>
<li>✓ همه کار میکنند</li>
<li>✓ فقط whitevpn کار میکنه</li>
<li>✓ فقط whiteaesther کار میکنه</li>
</ul>
</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/whitedns/1839" target="_blank">📅 15:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1838">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YDDKUMx2eN6WhDkNBbiVMEhcW-y6Ie1TQAXvdqWH_pXsmOJqfZHX0VXDMPXOBPTRdfac5PlHSWmlxV3u3H7VCW_VUutVHNdD5wYFMrXpHCHd9F0V8Spfk70YIqLwhlYcfaMiqpTwmNbYLwmX8dKQtkXq1NydhlomQ34j90DBkOzM_OErCxFDQYgytCrftOndlZPMqqBfA2gsu0ZjbIRw4ZKKX9SkcKy74IeEYQT-wHQlIYyBjDpHdd1NhK7jYiw-VgoIYBy7sSJ6beFOgFc6Xs4BfdRnAcHjteNL-MsoItDbrQXGHEKndnGZss3mhZM2WecBIHaQlM0bTwKCZDBnNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther mobile V1.9.4
pre-release
الان DNS inside the tunnel روی همه حالت ها اعمال میشود - قبلا این امکان فقط برای حالت proxy بود.
🌐
چی درست شد
▫️
فیلد «DNS inside the tunnel» بالاخره کار می‌کند.
✅
تا حالا هر چی وارد می‌کردید نادیده گرفته می‌شد و همیشه از
1.1.1.1
استفاده می‌شد. اگه با سایت‌های تست DNS چک کرده بودید و جواب عوض نمی‌شد، دلیلش همین بود.
اگه خالی بگذارید مثل قبل
1.1.1.1
می‌ماند. در حالت chain اعمال نمی‌شود، چون آنجا نام‌ها رمزگذاری‌شده و از سمت خروجی پرسیده می‌شوند.
🔒
و بهینه سازی موتور و routing , ......................
نصب:
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.9.4
@whitedns</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/whitedns/1838" target="_blank">📅 15:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1837">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fKeQy4YzWDV4ytEt_d-smHIfFoXpqH8iMX9zv9vkg75Z38qI9Ob4wemgmp7ihjVr3vNx_Mf4wyjBM5mmbEkKuWzwcKGNFjtMinH3S6GggY2isRmUW2OwHmpxUzdyLmRP25OfTGJZMmJqsYnFpe40ujG4PA-bCzBaaYih5RYTmvd-rlKgpcs5lOmy0hx-Mtpy8qfNrV8ZhRoksUxKLhgXCXfa_Jv20QEMIkCzvGYbOkGT2QhSMm0eXWLnwX4WqF8geD8i3pnT7Fqofx6rzVefgrB9vketqOjz0MN69sVdyKPzDlcXO6axneZEZPvMIjhTh3gXLvhzp_FG6ZhJ9zstOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخهٔ آزمایشی whiteaesther desktop 1.9.5  — رفع باگ پورت و یک سری بهینه‌سازی روی موتور و .........
🚀
اگر بعد از هر بار اتصال، پورت پراکسی محلی عوض می‌شد و تنظیماتتان به هم می‌ریخت، این نسخه همان را درست می‌کند.
✅
پورت دوباره ۱۸۱۹ می‌ماند — هر کریری که وصل شود.
🔒
این باگ از نسخهٔ ۱.۹.۲ به بعد دیده می‌شد، از وقتی دکمهٔ اتصال شروع کرد خودش راه خروج را پیدا کند و سایفون یا تور بیشتر برنده می‌شدند.
🕵️‍♂️
📥
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.5
⚠️
نسخهٔ آزمایشی است — در فهرست دانلودها به‌عنوان آخرین نسخه نشان داده نمی‌شود و برنامه خودکار پیشنهادش نمی‌دهد. با همین لینک بگیریدش.
اگر پورت باز هم جابه‌جا شد، حتماً بگویید.
📢
@whitedns</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/1837" target="_blank">📅 14:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1836">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎮
معرفی اپلیکیشن WhiteGame | پینگ و آنالیز سرورهای گیمینگ در یک بستر
🚀
برنامه WhiteGame یک ابزار کارآمد آنالیز و ارزیابی کیفیت اتصال گیمینگ (Network Pr MA) برای سیستم‌عامل اندروید است (که به‌زودی برای سایر پلتفرم‌ها نیز منتشر می‌شود)
📱
. این برنامه به‌طور…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/whitedns/1836" target="_blank">📅 09:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1835">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/af5w_cTR2DOxnymbRSKkG7HfgBJ856b6mRBXgPU5X_vq4AtVLfA2QUQ7MTMhh13VJwtjiIso750mNcXDDCvtG2EAvIXfPVS1-tJ64gG6pa9oIaLK30_T2zMpaMDxI75Bc2u56aZuC5eFj33UkOSawrkeXp2QawwjJE2OE2Semc893JeD_wFzWl6WwJsbrBeduQhWmQvh2XSOhebxQ1xWeOlihv19gA7lE49p9bWfQVajHvqxGRH_6Y1s9OOQW8o6TwVAPxCJ7ZpUp_rZcs6slTC_ftpd3lM4zcZSJXGrHKcmHVIyhlHjDItNVtSIr5atkmj8yoRN9NMK7_GBxtT_LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
معرفی اپلیکیشن WhiteGame | پینگ و آنالیز سرورهای گیمینگ در یک بستر
🚀
برنامه
WhiteGame
یک ابزار کارآمد آنالیز و ارزیابی کیفیت اتصال گیمینگ (Network Pr MA) برای سیستم‌عامل اندروید است (که به‌زودی برای سایر پلتفرم‌ها نیز منتشر می‌شود)
📱
. این برنامه به‌طور ویژه برای بهینه‌سازی پینگ، سنجش کیفیت اتصال (QoS) و رفع چالش‌ها و محدودیت‌های ارتباط با سرورهای بازی طراحی شده است.
📊
این ابزار با شبیه‌سازی پروپ‌های شبکه‌ای و سنجش شاخص‌های کلیدی و نوسانات پکت‌ها تحت وب، به گیمرها این امکان را می‌دهد که وضعیت زیرساخت اتصال خود را پیش از ورود به بازی ارزیابی کنند. جای دارد گفته شود که تمرکز ما روی
UDP
است، همچنین قابلیت
Test Real Path
در اپلیکیشن، پینگ واقعی و دقیق شما را در زمان Matchmaking و InGame نمایش می‌دهد .
🔐
پروتکل‌های پشتیبانی‌شده:
Warp | WireGuard | Amnezia | Xray
✨
ویژگی‌های برجسته:
• Packet Loss Injector
• Jitter Plus
• Gaming DNS Spy
• Optimizer Warp و WireGuard
⚙️
علاوه بر این، ابزارهایی برای ساخت و مدیریت کانفیگ در اختیار شماست؛ با استفاده از بخش Generation برنامه، تنها کافی است Public Key سرور خود را قرار دهید تا خروجی موردنظر به‌صورت خودکار تولید شود .
📉
همچنین در مرحله تست آزمایشی (Beta)، حدود ۳۰۰ نفر از کاربران با استفاده از ترکیب Warp و پنل BpB توانستند میزان Packet Loss خود را در شرایط ناپایدار کنونی به نزدیک ۰٪ برسانند.
🤝
امیدواریم با بازخوردها و پیشنهادات شما، این پروژه را روزبه‌روز بهبود ببخشیم.
https://github.com/TaJirax/WhiteGame
@Whitedns</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/whitedns/1835" target="_blank">📅 06:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1834">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pDrtI2gSlwG16RiDunCuM5ooVXUXyadUEEdY9E_GvWxaiqhiF0h-SqCeL1_9591M7G7JtRo-6YTGtQ_5Q0pjVIsdOZLJi2t-0KnGX8QsOS7RIfx8ZBWCDfV_xkJ8CGEwb0Twf4SpUfUioGvxiqCp0CQ6zc0pe4Co1XJktuaFuV2OXW7EH8VRaDhfNFVdPMioesMV_WsZNa5IzvWaSJqfipe3cSWtiLj9UI82HB3Tn0y4SrFL4vlfYm30EXc_L6hM5j7piQNriuJbLcQmH5R_IrXA-b3A1vKWFqPZB_kPjQJnt1faRxvBt84CTCa3dS5zUfSGnRTV6zhKZxS1MCTSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا در گروه whitedns عضو بشید
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/1834" target="_blank">📅 20:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1833">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bShQKUHOT6TFWHnC0cZIKGOhnO-iPTGp5Oiy_vnyG98ue1IGbwQ5IE3RKf7Lh3mQcELsnFTl-y3oZfoF6jkTrXX6mM0PfmONPdirSLasRFFGzXvpHG0Eg72Gpu0-mgGIq4O6Hg9XeUTUB0PMXRuuSXMajGbEqCsQve_uKw00Kkw3tO-t-eZczapT7KCmmLFbyPaXkW0t3m3S9lFa7Bdms4vjufmeRf1DbRifJ6kVMF2IpV-L7SOQfh10bpVfMEkNaR5WPton49T23rqM87Pnk6jfusBjDsijSYAYgrQonI8jtdHrx50AtK-494Okazr4zO0VisEluIXzh6u4ESkz-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات پاسحگو
💬
Support Bot:
@WhiteDnsResponder_bot
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری
⚠️
⚠️
whitedns app config bot  :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/whitedns/1833" target="_blank">📅 17:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1830">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Blue Knight Panel (Orihost).rar</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/whitedns/1830" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/whitedns/1830" target="_blank">📅 02:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1829">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhjkjY8JCb6Nfe2Lln4wyieYFAS6vsvSMoenUnkbtUmNmwMopdGIQNTg6OUIWrblm8RGkEOpbIdYsgvTCOdDxWZhjL28GCyMjMDvh4alX856Wr4Ujby6E8aLUsHa0cbN8dMZxDiiDvNiQiJGLQI8v4Ec_M-itVOsz-Bjr65YpyvKUjXTejQrRWHi20Z-ZglVtaQ3f6PwiuJunWnobWtZ7P8nn3Atm9O_l3R3zaZW_Wy7qg-PrTauZiethAzhVx-m1-a6q7WFdZMTQqQvvPsLelddQXk9aEopiLXOi7yw004qLgd_vIihGwUvWt1CgYbazE81i7tPkD_1LlCNEEvHOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
بچه‌هااا یه آموزش جدید آپلود کردم
🥹
✨
اگه Gemini خطای 403 میده یا Google Flow براتون باز نمیشه، این ویدیو رو از دست ندین
👀
💗
توی ویدیو از صفر Blue Knight Panel رو می‌سازیم و آخرش با کانفیگ‌هاش Gemini و Google Flow رو تست می‌کنیم
😭
🔥
🎀
تماشای ویدیو:
https://youtu.be/GK2PGDzkbh4</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/whitedns/1829" target="_blank">📅 02:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1823">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteAestherMobile-1.9.3-universal.apk</div>
  <div class="tg-doc-extra">134.8 MB</div>
</div>
<a href="https://t.me/whitedns/1823" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/whitedns/1823" target="_blank">📅 14:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1822">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/TT21Lwxam--eMFIwbV1zmMDw8lQdJJUWZ3mMfbM8Wbct5pPRz7fr1CkliauTy9sUNIz4R8mbe6VjoFN7vqM85nNZoM8hVfp-Va4d59w19GdiK2ABvibDslLhKZMBOZW2XN7j5nw1QglrqwZ63REpAiBOABpW3p-XJcTImSjHV1bninjv2-MLqaXgl75jkGiP0eesTMz_9kg-av5NvzDwuNJKBVq6HsR2kmnHv7NEYRiNA9rPBt-5m69PJJJwvOy-LnLDmuK42A3CA9wsZDHey7pzR6yqtEDOjry11m2ind64lv8PNg9QFtwusc-TtZpI4fViJp1tpVDn6c5fprMWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther
Mobile 1.9.3 — نسخه پایدار
🔥
نسخه پایدار 1.9.3 منتشر شد. برای به‌روزرسانی می‌توانید از قابلیت جدید داخل اپ استفاده کنید یا فایل را مستقیماً روی نسخه فعلی نصب کنید.
برنامه را حذف نکنید تا هویت و تنظیماتتان حفظ شوند.
قابلیت‌های جدید
آپدیت مستقیم از داخل اپ
کارت «نسخه جدید منتشر شده» حالا می‌تواند فایل به‌روزرسانی را دانلود و نصب کند.
این قابلیت فقط زمانی فعال است که:
پوشش اتصال روی «کل دستگاه» باشد.
فایل با همان کلید نسخه نصب‌شده امضا شده باشد.
ابزارک صفحه اصلی
بدون باز کردن برنامه، اتصال را برقرار یا قطع کنید. برای افزودن ابزارک، در Settings دکمه Add را بزنید.
هنگام جست‌وجوی مسیر نیز دکمه قطع اتصال در دسترس خواهد بود.
مشکلات رفع‌شده
مشکل نسخه 1.8.0 که ممکن بود برای یک هویت دو رکورد نگه دارد، برطرف شده است. اگر نصب شما در این وضعیت گیر کرده باشد، با اولین اتصال خودکار اصلاح می‌شود.
جست‌وجوی طولانی finding a working route اکنون محدودیت زمانی دارد. این فرایند قبلاً روی شبکه‌های دشوار ممکن بود تا ۲۷ دقیقه طول بکشد.
هنگام جابه‌جایی بین وای‌فای و دیتای موبایل، تونل تا جای ممکن به شبکه جدید منتقل می‌شود و از ابتدا ساخته نخواهد شد.
اتصال MASQUE in MASQUE اصلاح شده است. اگر روش اول برای هاپ داخلی پاسخ ندهد، روش دوم نیز آزمایش می‌شود.
تمام اصلاح‌های نسخه 1.8.1 نیز در این نسخه قرار دارند.
روش نصب دستی
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.9.3
فایل مناسب معماری گوشی را دانلود کنید.
اگر نمی‌دانید کدام فایل مناسب است، نسخه universal را بگیرید و آن را روی نسخه فعلی نصب کنید.
در صورت مشاهده مشکل، از مسیر Settings ← Diagnostics گزینه Send diagnostics را بزنید و گزارش را ارسال کنید.
⚠️
@whitedns</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/whitedns/1822" target="_blank">📅 14:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1821">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/HxDcZ3gLYS6Ch1WC9rb95KpK-wQeyjB_rrgq_pdv2r0bnaXS-jMrhKVcPaRD08qlPhavv90larQOy3ERGlInEXXLxxdwxvSuu6LRoprodwbQTWqOM0PevgxuZ7SvpxT4AMZ2yZyXIuKoi0OWBLBPTD32MJXRbHz8A0dCsEm8nMZTgYOpy2Y5YxKlyi9Pvaey1ak6gpH7tPFEsS96BQZvtXRY8mP61GyzVIFMVDPpPGEXtebtNPM-ltCkk-6ehX8fel2cD_4SIZEAuDxhlkJMgxqerH47-XClLg8bXTE3ctHZBq9AiZjWCRWd8D8ZGfMQPlwsuG7RMp5K_NiZpwcA7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
;کاتن روتر
چیست؟
کاتن روتر یک ابزار سبک برای مدیریت چند سرویس DNS Tunnel روی یک سرور است.
خیلی ساده بخواهیم بگوییم:
فرض کنید چند سرویس مختلف دارید، اما فقط یک سرور و یک IP در اختیار دارید. CottenRouter درخواست‌ها را دریافت می‌کند و بر اساس دامنه، هر درخواست را به سرویس مربوطه می‌فرستد.
یعنی چند سرویس می‌توانند از یک IP و پورت عمومی ۵۳ استفاده کنند.
⚠️
توجه: CottenRouter خودش VPN یا تونل ایجاد نمی‌کند؛ بلکه سرویس‌های تونلی موجود مانند CottenDNS، MasterDnsVPN، StormDNS و SlipGate را مدیریت و مسیریابی می‌کند.
🔗
لینک پروژه:
https://github.com/TaJirax/CottenRouter
پیش‌نیازها
برای نصب به این موارد نیاز دارید:
یک سرور Linux با IP عمومی
دسترسی SSH و root یا sudo
دامنه یا زیردامنه
سیستم‌عامل پیشنهادی: Ubuntu 20.04 به بالا یا Debian 11 به بالا
روی ویندوز مستقیماً نصب نمی‌شود؛ باید روی سرور Linux نصب شود.
نصب آسان
ابتدا با SSH به سرور وصل شوید:
ssh root@IP-SERVER
سپس دستور زیر را اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
بعد از نصب، پنل مدیریت را باز کنید:
sudo cottenrouter tui
استفاده خیلی ساده
در پنل بازشده:
با کلید Space سرویس موردنظر را انتخاب کنید.
با کلید i نصب هدایت‌شده را شروع کنید.
با کلیدهای Enter یا e دامنه و پورت سرویس را تنظیم کنید.
با کلید s یک سرویس را Restart کنید.
با کلید v اطلاعات اتصال و مسیر رمزها را ببینید.
با کلید x یک سرویس را حذف کنید.
تنظیم دامنه
برای هر سرویس یک زیردامنه جدا بسازید و همه را به IP سرور متصل کنید:
cotten.example.com
→ CottenDNS
master.example.com
→ MasterDnsVPN
storm.example.com
→ StormDNS
feed.example.com
→ thefeed
در پنل، همین دامنه‌ها را برای سرویس‌های مربوطه وارد کنید.
بررسی وضعیت سرویس
برای دیدن وضعیت CottenRouter:
sudo systemctl status cottenrouter
برای بررسی سلامت:
sudo cottenrouter healthz -config /etc/cottenrouter/config.json
برای دیدن لاگ‌ها:
sudo journalctl -u cottenrouter -f
به‌روزرسانی
برای نصب آخرین نسخه، همان دستور نصب را دوباره اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
نصاب تنظیمات قبلی را نگه می‌دارد و در صورت بروز خطا امکان بازگشت خودکار دارد.
📌
برای اطلاعات کامل‌تر، راهنمای فارسی پروژه را ببینید:
https://github.com/TaJirax/CottenRouter/blob/main/README.fa.md
اطلاعات این متن بر اساس راهنمای فعلی مخزن نوشته شده است.
@whitedns</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/whitedns/1821" target="_blank">📅 17:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1820">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/gC08ewNSvBx_R9UqwGpanB7H4E5t1gnrI-j-i1DGLCR0dRFvkvqWfwmoxFI50GRAtTQR30-qysQvxOuRUTO0tKB-uVu0aS04u6QzKpCwrNhPpqLZVr98_32UiH104pZQtSJ-c_f8X8m08qIuw5F2uzi30NSdqk1nlOP9_Fyt7yU0KaSufb3MOdA0XAU7U0cNzl3Qh3sURR-veFRXv62WaHPdWnA_LeEhW8GY434F8crJMcP60b5JyEyK4llyM-Sn21gyEDq0kLbyheI6oz4T9e90oWTQhhplIWKZAvBKy0V27xgHGURrtGMcAgu5CaiQRZkbqgPdXqa5IRwHRgMmQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه
CottenRouter v1.2.13
منتشر شد!
سریع‌تر، پایدارتر و آماده برای ترافیک سنگین
⚡️
• رفع مشکلات نصب
SlipGate
روی سرورهای تازه
• جلوگیری از Down شدن Router هنگام قطع نصب یا SSH
• رفع تداخل Domain و Port بین Backendها
• امنیت بهتر
CottenDNS
و
StormDNS
0
٪ Query Loss
در تست ۵۱۲ کلاینت همزمان
• پردازش بیش از
۲۲K Query/s
• بهبود TUI، خطاها و سیستم Purge
✅
آپدیت مستقیم بدون حذف Routeها، Backendها و تنظیمات قبلی
💻
GitHub
https://github.com/TaJirax/CottenRouter
📋
لیست کامل تغییرات
v1.2.13
https://github.com/TaJirax/CottenRouter/blob/main/docs/releases/v1.2.13.md
@whitedns</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/whitedns/1820" target="_blank">📅 16:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1819">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/okU7soh9nWUlzOYGowfcqNSbRjjozPQEiY-NJ7IJF-N-ijM76tkRPH2UfJeIOc64-Sj3pRAuF-sX5AWJeeU_x5I72YXz7Q4p6Zt0H473cKL-rq70-fIUyoou3cgBHHLKYLW0G7hIcN4ApqM56i2Fzd8uwDhPjy0Q1sUjTkyOJBq02L0CUmqj1CmAA3h6yhfmgzzeBEk3W4j9dQ4OByTZ6S-aOqfxpUH-FZkWSfMvB7jmHVJUTIYvvvvBLY6IjXmSjP0M7paEPbwnSQ8FiGXqvPsHYla9vyj54FYr7zxl_LmCtYWXbQwekeOrl5F1-9tWmHaj-0jH_1Oc1TQtaVvg-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whiteaesther moblie pre-release 1.8.1
⚠️
این نسخه برای کاربرانی هست که توی چند روز گذشته اختلال شدید گزارش کردند و نسخه آخر هم مشکل انها را حل نکرد
برخلاف باور غلط عمومی ورژن ها در حال بدتر شدن نیستند بلکه امکانات بیشتری در حال اضافه شدن است - اما به دلیل گستردگی کاربران ما مجبوریم حداکثر بومی سازی را انجام بدهیم که این کار گاها زمان بر خواهد بود .
اگر روی ورژن قبلی مشکلی ندارید فعلا اپدیت نکنید !!!!
⚠️
⚠️
⚠️
دو اصلاح، هر دو روی حساب زنده اندازه‌گیری شده:
MASQUE دیگر دنبال آدرس نمی‌گردد. Cloudflare در هر پاسخ ثبت‌نام آدرس اختصاصی دستگاه را می‌دهد و موتور نادیده‌اش می‌گرفت
ثبت‌نام‌های Cloudflare دیگر دور ریخته نمی‌شوند. هویت بلافاصله پس از ثبت‌نام و پیش از هر کار دیگری ذخیره می‌شود؛ مسیر مستقیم یک بار امتحان می‌شود نه پنج بار؛ و نصبی که enrolment مربوط به MASQUE کلید WireGuard‌
اش را باطل کرده بود، در اولین اتصال خودش را تعمیر می‌کند.
این نسخه به‌صورت خودکار به کسی پیشنهاد نمی‌شود.
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.8.1
@whitedns</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/whitedns/1819" target="_blank">📅 12:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1818">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">😎
دیگه لازم نیست برای آپدیت از اپ خارج بشید.
اپ اتوماتیک ورژن جدید رو دانلود و نصب میکنه.
این به کسایی که اطلاعات فنی هم ندارن کمک میکنه.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/whitedns/1818" target="_blank">📅 11:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1817">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3YiPsspmHocu68qbVLqSNIdDdmpJGWyJOyf6Kh8RDRDNmRO5XVmf6s-Yj10c8_xNmmbbAIDrT-kq2HYPQgh67KjgaM2lapPUGyjGnYKeRyCjxvgglk1MLyaPsHE3yIrtxtDJKe-ccYebGB45PF1zAa67ZGkyNna69GlcRPWUROosEKqGX7BdeEIDXgUN8YZ9sGav27uoraj7Iw6Jp7aSg0TO2uhoiEa23dnK4aH82EppPMhPbsz8RbOL2txA9WcKYBj4wuXZtycQED9Earku3kluOy36A8RUKBZLKhyPgQXYFKqunVIa56S49-bEdccQONE4bxAiubRuLCg_kSUlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
انتشار نسخه جدید WhiteVPN 1.6.8
تغییرات نسخه جدید:
🟢
ویجت صفحهٔ اصلی برای اتصال، قطع اتصال و نمایش وضعیت VPN
🟢
به‌روزرسانی از داخل برنامه، با نمایش پیشرفت دانلود، امکان رد کردن یک نسخه و بررسی صحت فایل و امضا پیش از نصب
🟢
اجرای Real Delay Test و تست سرعت در پس‌زمینه و هنگام خاموش بودن صفحه
📱
دانلود از گیتهاب</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/whitedns/1817" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1815">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⭐️
چطور API رایگان DeepSeek V4.1 Flash بگیریم؟
توی این ویدیو، قدم‌به‌قدم نشون می‌دم چطور به API این مدل دسترسی رایگان بگیرید؛
اگه با API آشنا نیستید، خیلی ساده یعنی به‌جای اینکه فقط توی سایت با هوش مصنوعی چت کنید، بتونید ازش داخل برنامه‌ها و ابزارهای خودتون استفاده کنید.
چه بخواید ایده‌ای رو تست کنید، چه روی یک پروژهٔ شخصی کار کنید یا تازه کار با API رو یاد بگیرید، این آموزش می‌تونه نقطهٔ شروع خوبی باشه.
📹
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/whitedns/1815" target="_blank">📅 22:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1812">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✍️
موقت
دوستان هم نسخه مبایل و هم دسکتاپ برای کارایی بهتر اول ورژن قدیمی را uninstall کنید و بعد نسخه جدید را نصب کنید
در نسخه ویندوز موقع uninstall کردن حتما گزینه delete app data را بزنید
ممنون</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/whitedns/1812" target="_blank">📅 16:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1811">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pypnlcUnAccPkNxjCQNvwplyOl8IlLeLDxszulyHw5U2CEiTmu-iHRH2oqJ1oH_DMXigCXuVwES51KQCeGgPMkhJgvwKOl5Xu3hrmp7nd9kcnq5RLoOzIzBRb0UkgCtFy5T1kMaBFLHeQoEntGkW9j-XCZW6PTfnIcRoyJRtt61vwI4jt07AgnJfbAKuV1Usjs-EvJRdvbpTyfLYYw6N-iaD4rhL5IpxfBpMC1W7kcvtOzRS3s2XeM-jphIGcERMk9TsO9SqsvZFl_aZk8esf6UN65OZ7Kr6HX_qAxLq0mw1ygbfe217OSrdAe6gu3SaRwMMftqiQUIBmkAx1tD99A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
WhiteAesther Mobile ۱.۸.۰ نسخهٔ پایدار
این نسخه دو کار را با هم می‌آورد: هرچه در نسخهٔ آزمایشی ۱.۷.۰ بود، به‌علاوهٔ یک راه خروج تازه. اگر روی ۱.۶.۱ هستید، هر دو را یک‌جا می‌گیرید.
⚡️
اتصال روی شبکه‌هایی که تا حالا جواب نمی‌دادند
حالت خودکار حالا واقعاً خودکار است. از همان لحظهٔ زدن دکمه، اتر و سایفون و تور را هم‌زمان می‌فرستد و هرکدام زودتر ترافیک را رد کرد همان می‌ماند. تشخیص اینکه کدام مسیر واقعاً کار می‌کند هم دقیق‌تر شده — دیگر یک مسیر سالم را به اشتباه کنار نمی‌گذارد.
این حالت از این نسخه پیش‌فرض روشن است. اگر خودتان قبلاً حاملی انتخاب کرده‌اید، انتخابتان دست‌نخورده می‌ماند.
🧅
ماسک در ماسک — راه تازه
یک پروتکل جدید برای شبکه‌ای که یاد گرفته یک تونل ماسک تنها را بشناسد. دو پرش تودرتو: پرش داخلی از دل بیرونی دست می‌دهد، پس چیزی که شبکه می‌بیند یک تونل است که محتوای مبهم حمل می‌کند، نه الگویی که آموزش دیده دنبالش بگردد.
هم در فهرست پروتکل‌ها هست، هم آخرین چیزی که حالت خودکار امتحان می‌کند — و بخش دوم مهم‌تر است: شبکه‌ای که این برایش ساخته شده همان جایی است که بقیهٔ راه‌ها شکست خورده‌اند، و کسی سراغ تنظیمات پیشرفته نمی‌رود. پس خودکار خودش به آن می‌رسد، بعد از اینکه راه‌های سریع‌تر نوبتشان را گرفتند.
از یک پرش کندتر است و عمداً آخر است. جایی که یک پرش کار می‌کند، چیزی برای شما عوض نمی‌شود.
🧠
موتور اتر ۲.۰
هستهٔ برنامه یک نسخهٔ کامل جلو رفت: سرعت عبور ترافیک روی تونل‌های TCP بیشتر شده، یک لایهٔ تازهٔ دور زدن تشخیص پیش از دست‌دهی اضافه شده، و پایداری تونل‌های تودرتو بهتر شده است.
🌍
کشور خروج روان‌تر
فهرست کشورها بلافاصله به‌روز می‌شود، «بهترین گزینهٔ موجود» همیشه در دسترس است، و اگر کشوری که انتخاب کرده‌اید در دسترس نباشد برنامه صریح می‌گوید به‌جای اینکه بی‌صدا تلاش کند.
🛡
پایدارتر
اتصال مجدد بعد از قطعی، حفظ تنظیمات محافظتی پس از راه‌اندازی دوبارهٔ سیستم، و رفتار دقیق‌تر هنگام جابه‌جایی بین وای‌فای و دیتا.
━━━━━━━━━━
📥
دریافت
برنامه خودش این نسخه را به شما پیشنهاد می‌دهد. اگر می‌خواهید همین حالا بگیرید:
برای تقریباً همهٔ گوشی‌های امروزی:
WhiteAestherMobile-1.8.0-arm64-v8a.apk (۴۵ مگابایت)
اگر نصب نشد، فایل universal را بگیرید — روی هر گوشی کار می‌کند ولی حجمش بیشتر است.
🔗
github.com/WhiteDNS/WhiteAestherMobile/releases/latest
روی نسخهٔ فعلی نصب می‌شود و تنظیماتتان می‌ماند.
#WhiteAesther
#v1_8_0
@whitedns</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/whitedns/1811" target="_blank">📅 16:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1810">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/n79AlASBmA0uCJHqP9ApKeuDjPNXYwUFZUNaDBgRYBUd6TqMgppmDLXfxdSYKn2vNdepm1pJaeN83sK8tQJoKKvQrqYXhMDPZsSf1FUU0SUIYsAiZwAnO-PuCDl37P0FVzJTgZJVhVY4x6-GvPEp8ccio2RF5JDlcg8syRCeQBTgi8l4wX2zyLC9jZN0_NcttWTayf9kIGDkzIQ9LB_lkwakXboIaZCjjbputFA3QzEt6cXXRJpxSxawM6eBeWFupswj_7Q1ObFBeHLUYCa73fF9v28otXKTpwNZtaFvyf74doFkePwszHwfNWejukGMncQBjjEKyyC3x9HQ3HhtnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
WhiteAesther Desktop 1.9.4 — نسخهٔ پایدار
بزرگ‌ترین تغییر از زمان ۱.۹.۱، و دقیقاً همان چیزی است که بیشتر کاربرها لازم داشتند.
دیگر لازم نیست بدانید کدام راه کار می‌کند
تا امروز اگر وصل نمی‌شدید، باید می‌رفتید در تنظیمات پیشرفته و بین Aether و سایفون و تور یکی را انتخاب می‌کردید. بیشتر مردم اصلاً نمی‌دانستند این گزینه‌ها وجود دارند و فقط فکر می‌کردند برنامه کار نمی‌کند.
حالا فقط اتصال را بزنید. برنامه هر پنج راه خروج را هم‌زمان امتحان می‌کند و اولی که واقعاً ترافیک حمل کند نگه می‌دارد.
قبلاً یکی‌یکی امتحان می‌شدند: اگر Aether بیرون نمی‌رفت، باید سه دقیقه صبر می‌کردید تا نوبت سایفون برسد. حالا همه با هم شروع می‌شوند و معمولاً چند ثانیه‌ای تمام است.
🆕
یک راه خروج تازه: MASQUE در MASQUE
بعضی شبکه‌ها یاد گرفته‌اند یک تونل MASQUE را بشناسند و ببندند. این حالت دو تونل تودرتو می‌سازد که از داخل هم رد می‌شوند.
لازم نیست انتخابش کنید — جزو همان پنج راهی است که خودکار امتحان می‌شود. روی شبکه‌ای که بقیه بسته‌اند، ممکن است تنها راهی باشد که باز می‌شود.
⚡️
موتور به نسخهٔ ۲ رفت
هستهٔ Aether از ۱.۸ به ۲.۰ ارتقا یافت. محسوس‌ترین اثرش سرعت است: بسته‌های بزرگ‌تر روی MASQUE H2 و دست‌دادن سریع‌تر.
🔒
حالا مطمئن می‌شویم چه کسی جواب می‌دهد
قبلاً برنامه یک مسیر را «کارکن» حساب می‌کرد اگر چیزی از آن برمی‌گشت. ولی روی شبکه‌ای که ترافیک را شنود می‌کند، خودِ شنودکننده هم جواب می‌دهد — یعنی ممکن بود همان مسیری انتخاب شود که در حال خوانده شدن است.
حالا از سایتی که به آن وصل می‌شود می‌خواهد هویتش را با گواهی ثابت کند؛ چیزی که فقط سایت واقعی می‌تواند ارائه دهد.
🐧
و برای کاربران لینوکس
پیام خطای «تونل کامل» دیگر شما را دنبال دکمه‌ای که روی لینوکس وجود ندارد نمی‌فرستد. حالا می‌گوید واقعاً چه کاری از دستتان برمی‌آید.
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/1810" target="_blank">📅 16:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1807">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">💬
تقریبا ۵۰۰۰ هزار کاربر فعال از کشور روسیه داریم که روانه دارن از WhiteVPN استفاده میکنند.
اونا هم اندازه ما دردسر فیلتر دارن، اما با توجه به «چراغی که به خانه رواست ...» از ورژن بعدی دسترسی کشور های دیگرو به اپ میبندیم.
• از ورژن بعدی میتونید اپ رو ببندید و پشت صحنه اسکن انجام میشه.
• آپدیت داخلی و اتومیاتیک به اپ اضافه شده
• بکسری تغییرات کوچیک دیگه
💬
اگر مشکلی داشتید که به ما گزارش دادید و ما فیکس نکردیم، لطفا برامون بفرستید.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/whitedns/1807" target="_blank">📅 09:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1805">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">💬
دوستان ما هرشب سرور های اختصاصی رو روی WhiteVPN بروز میکنیم تا از فیلتر شدن سرور ها جلوگیری کنیم.
متاسفانه این‌چند روز سرور سنگاپور رو نداریم ، توی یک شب ۳۰ ترابایت مصرف شد و هزینه زیادی داشت. وقتی خاموشش کردیم، دیگه سرور سنگاپور ارایه نمیداد.
باید دوباره موجود بشه و براتون یکی به زودی میسازیم.
🔒
اگر براتون مستقیم وصل نمیشه، به یک سرور عمومی وصل بشید و اختصاصی رو زنجیر Chain بکنید تا آی‌پی ثابت بگیرید.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/whitedns/1805" target="_blank">📅 02:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1793">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Y5JZIg4JajVG2-arIqaLl53ZdoyV9Hgk0Nj5ijGk5wZG51SQvVCa3AWtQreoSWq9e8YPiwyqvigQQAM1BsPEJZfLGEmnZCxzeV9Mp2DCw7OB-0-vJs-qlTppZStfjIilCGHKSrtLsOOCfZgXrAtfCKHR39WydSilMtB5jWTRtcPgbvleeFrpAsCqwTUdYg5eSHVgWXy2q-MQLx2d5wPzSQT0WARGUHiySwRUGMInMHriDVR46VAdGyteTn5erebCYDjfDI02rIu8EDc6gnDoN1MhUm0CTpyQ7TdRPIdnBWZVtNAyRaQT8P_cZ0VBLBSix_oUU-yDRWYvDSdeX0_oAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
اگر به هر دلیلی نیاز به کانفیگ (cottondns,masterdns,stromdns) برای اپ
WhiteDNS
دارید از ربات زیر میتونید با محدودیت حجم و روزانه کانفیگ بگیرید.
⚠️
این کانفیگ 1 روزه و با حجم 0.5 گیگ هست
در حال حاضر تعداد کانفیگی که میتونیم بدیم خیلی محدود است و فقط با تاییدیه ادمین برای شما ارسال میشه
⛔️
لطفا اگر اشنایی ندارید و کنکجاوید و یا میخواید ازمایش کنید و... درخواست ندید
@MasterDnsManager_bot
WhiteDNSاپلیکیشن
دانلود اندروید
•
دانلود دسکتاپ
@whitedns</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/whitedns/1793" target="_blank">📅 09:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1790">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bfo9PjWmKZl_Fe0zLxebPGVN_zgEmMNsne7qoOUJwOLFVgKfpI7CuPUpWGcaXMyq_G7l66lUIdhITXQ89NlxPekooHbY3_1uGHNCAV4nUlO0CTy3yt2MkozSBA94AmD9ExJKXzRQoC3OrzgJXVZOfBty9Tuw7U0V-VOy_BbV10CcmzK2oxZayS8Lsg3TLkLEoDt-OgmykdvoALGe4EFBjYOGyoehm0WuLL3aoTPFQF9VplD_TvIuIMH5gTgyH2n4kjiKq21a4DIQzEdMlK_KOpd1Gzt5GhMECxpqSrTHnFjCvb9IzWjG7O5o6FqnAtgz7lnnKro7JjNkWIqheEliZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
🤖
قابلیت جدید : (نسخه ازمایشی )
⚠️
⚠️
⚠️
گفت‌وگو با هوش مصنوعی در ربات
🔥
WhiteDNSResponder V.5
نسخه ازمایشی حتما باگ هایی دارد  و  دچار اشکالاتی خواهد شد که با پشنهادات و کمک شما هر روز بهبود خواهد یافت
👀
از این پس می‌توانید مستقیماً داخل ربات با هوش مصنوعی گفت‌وگو کنید، سؤال بپرسید، متن تولید یا ترجمه کنید و درباره موضوعات مختلف توضیح بگیرید.
این امکان جدید به صورت محدود و با درخواست کاربر فعال میشود.
⚠️
@WhiteDnsResponder_bot
🔐
نحوه درخواست دسترسی
1️⃣
وارد گفت‌وگوی خصوصی ربات شوید.
2️⃣
از منوی ربات گزینه /airequest را انتخاب کنید.
3️⃣
درخواست شما برای مدیر ارسال می‌شود.
4️⃣
پس از تأیید، دسترسی به‌صورت خودکار فعال شده و نتیجه از طریق ربات به شما اعلام می‌شود.
نیازی به پیدا کردن یا ارسال شناسه عددی تلگرام نیست.
🔹
روش استفاده
پس از فعال‌شدن دسترسی، سؤال خود را بعد از دستور /ai بنویسید:
/ai تفاوت DNS و VPN چیست؟
یا:
/ai یک متن رسمی برای درخواست همکاری بنویس
🔹
دستورات کاربردی
/ai سوال شما
شروع یا ادامه گفت‌وگو با هوش مصنوعی
/ainew
پاک‌کردن گفت‌وگوی قبلی و شروع مکالمه‌ای تازه
/aistatus
مشاهده سهمیه روزانه، میزان مصرف و تعداد درخواست‌های باقی‌مانده
📊
محدودیت‌های فعلی
• سهمیه روزانه براساس تأیید مدیر: ۵ یا ۱۰ پیام
• حداکثر ۳ درخواست در هر ۵ دقیقه
• حداکثر ۲۰۰۰ نویسه برای هر پیام
• نگهداری موقت چهار بخش قبلی مکالمه برای ادامه بهتر گفتگو
• قابل استفاده فقط در گفت‌وگوی خصوصی با ربات
• سهمیه روزانه در نیمه‌شب به وقت UTC تمدید می‌شود
🔒
امنیت و حریم خصوصی
• هوش مصنوعی به سرور، فایل‌ها، دستورات سیستمی یا اطلاعات خصوصی تلگرام شما دسترسی ندارد.
• متن مکالمات توسط این قابلیت در پایگاه داده ذخیره نمی‌شود.
• تنها شناسه کاربر، وضعیت دسترسی و میزان مصرف سهمیه ثبت می‌شود.
• لطفاً رمز عبور، اطلاعات بانکی، کلید API یا اطلاعات محرمانه ارسال نکنید.
⚠️
این قابلیت فعلاً به‌صورت محدود و آزمایشی ارائه می‌شود. درخواست‌های تکراری ارسال نخواهند شد و در صورت استفاده نادرست یا ارسال خودکار پیام‌ها، دسترسی کاربر ممکن است غیرفعال شود.
🤍
WhiteDNS — دسترسی ساده‌تر به ابزارهای کاربردی هوش مصنوعی</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/whitedns/1790" target="_blank">📅 15:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1789">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✍️
موقت
اگر روی ویندوز و یا اندروید نسخه قدیمی دارید
⚠️
⚠️
ویندوز :
گزینه reset app data را بزنید و بعد uninstall کنید و جدیدترین نسخه را نصب کنید
اندروید :
حتما ورژن قدیمی را uninstall کنید و ورژن جدید را نصب کنید
@whitedns</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/whitedns/1789" target="_blank">📅 04:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1787">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✍️
موقت
برای جمینای و بقیه هوش مصنوعی ها بر اساس تستی که کردیم روی سایفون و تور راحت باز میشه - اگر تور و سایفون مستقیم وصل نمیشه اول با اتر وصل بشید و بعد خروجی را روی سایفون و یا تور تنظیم کنید.
در ضمن اگر روی یک اپراتور جواب نمیگیرید حتما حداقل یک اپراتور دیگه را هم تست کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/whitedns/1787" target="_blank">📅 19:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1785">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-poll">
<h4>📊 امشب ساعت 8 به وقت ایران لایو بگذاریم جواب سوالات را بدیم ؟</h4>
<ul>
<li>✓ بله😍</li>
<li>✓ خیر😢</li>
</ul>
</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/whitedns/1785" target="_blank">📅 14:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1784">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CKbXVbh9-JPd2zuEbeVU15Xm8EoRHLMDUBev0IIQeSaFXqKRQHZXmnLrNooZ124_ysd79XDg6LOAlu8N6ZhpE3PcV6oJxMLkl0v-Qn6T2rccvGp_JM6PS23JHatUYzs0sFtWkJXlCFSPxhRFf2kOc_s73yTZOczRGyC_-fyrJg9ECy6HBRuHaKfy0qqIho0ORTzxmqrnfyoLfWcMELMtVyjyfd7I-yq0HUox5KMr-cy12QalTUM41rDdnPJ4xs1GOnKsphJ0m5Z3HyX2FpD-cWKltXz7tdjUR7ZJQojUb42u5uPrxIaH-KSWYnVGSkqaKQ0orHOHzI8Keuy3bcuZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات پاسحگو
💬
Support Bot:
@WhiteDnsResponder_bot
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری
⚠️
⚠️
whitedns app config bot  :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/whitedns/1784" target="_blank">📅 14:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1778">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/JBh6d1ES6F6b0f_z3nyNbK_G9nd0eZg5BDOdjHaj5frPTDL89vZL-CaZ-GvviwOuAfKDcv97aZBMXMn9lvvqkRGru1-RcpQoXGM8vGCfffBlxZ5DXO4nDYPC435bZCu99bIicQJFibRAaJx8k_tKqv1i0eIVBHzzaSrQ9X9XpFIW6_uVjrhJ9fUHZDoa5lKNl1GusI87_7qJjj5Ean8pEbicF7zkVJilQ9L2UfTlLweX8SwNoS7d9hI7ZTgdBRnpYkiY0zn8-wFi4DHOBa70Z1NMWaO3kyIKXL1fcKQ5k9YiqqWBn84fS64YffMDD6wB2oZUbST98kBQSl8gu0YiCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
WhiteAesther mobile 1.6.1 (stable)
دوستانی که منتظر اپدیت بودند الان میتونند اپدیت کنند
⚠️
✨
چه چیزی جدید است؟
🔗
زنجیره کردن دو حامل
حالا می‌توانید دو حامل از بین اتر، سایفون و تور را پشت سر هم وصل کنید، به هر ترتیبی. حامل اول چیزی است که شبکهٔ شما می‌بیند و حامل دوم چیزی است که سایت‌ها می‌بینند.
مسیرها ← حامل ← «خودم انتخاب می‌کنم»
⚡️
سایفون بهتر
سایفون به سرورهای بیشتری دسترسی دارد و زمان بیشتری برای پیدا کردن راه خروج می‌گذارد، پس روی شبکه‌هایی که قبلاً وصل نمی‌شد شانس بیشتری دارد.
🤖
حالت خودکار (آزمایشی)
اگر روشنش کنید، برنامه خودش اتر، سایفون و تور را هم‌زمان امتحان می‌کند و راهی را انتخاب می‌کند که واقعاً اینترنت از آن رد شود. راهی که روی هر شبکه کار کرد را هم یادش می‌ماند و دفعهٔ بعد سریع‌تر وصل می‌شود.
فعلاً پیش‌فرض خاموش است تا بیشتر امتحان شود. برای روشن کردن: مسیرها ← حامل ← «خودکار (آزمایشی)»
🛠
اگر نسخهٔ آزمایشی ۱.۶.۰ را نصب کرده بودید و وصل نمی‌شدید، این نسخه آن مشکل را برطرف می‌کند.
💡
نکته
اگر اتر روی اینترنت شما وصل نشد، سایفون را امتحان کنید:
مسیرها ← حامل ← «خودم انتخاب می‌کنم» ← سایفون
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.6.1
• بیشتر گوشی‌ها: WhiteAestherMobile-1.6.1-arm64-v8a.apk
• اگر مطمئن نیستید: WhiteAestherMobile-1.6.1-universal.apk
روی نسخهٔ فعلی به‌روزرسانی می‌شود و تنظیمات شما می‌ماند.
🐞
اگر مشکلی دیدید: تنظیمات ← تشخیص ← «ارسال برای توسعه‌دهنده»، و بنویسید چه اینترنتی دارید (همراه اول، ایرانسل، وای‌فای خانگی و…).
@whitedns</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/1778" target="_blank">📅 14:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1777">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hovKisOLs_D6HE8_kgdUyDF4hhieQrpTRWTSoe5KaclnYecshPzuIiMC4yYKn96x66xzQ5iP6kBRFwYNXRyLxMmcei1M-NdbHY_vt0XRzSt2mpzrKesv0ZA4yFtsbCab_aqCqlxkhu971_5TtPGNnmI_PqvxMHpWPqKmhIsgtCpKnSPNnTYkXRwWJh9TMg0I_gcE-BdooC7rxchq1VxKzq3sikPS_LXuB_k7sPoXsaf2muXKclXzXhN6hHOinWySSkM5tr1UgnbNKmvFYt1cJVtpcY9ZEHxPP-JJtA7Zpqg5vN_r8Bkx8dx4siMXuzeQrOffvgE3jQcXB9G46f21_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther desktop  1.9.1 (stable)
🔥
دوستانی که منتظر اپدیت بودند الان دیگه میتونند اپدیت کنند
⚠️
پنج ایراد درست شد که سه‌تایشان را فقط وقتی می‌دیدید که شبکه سخت می‌شد.
دکمهٔ «یکی که کار می‌کند را پیدا کن» حالا واقعاً می‌گردد
تا امروز، جست‌وجو روی همان گزینهٔ اول می‌ایستاد و می‌گفت وصل شد — حتی وقتی نشده بود. هیچ‌وقت به سایفون، تور و شش ترکیب زنجیره‌ای نمی‌رسید. حالا هر راه را تا آخر امتحان می‌کند، و یکی را فقط وقتی قبول می‌کند که یک درخواست واقعی از آن رد شده و برگشته باشد.
⚠️
یک نشتی در حالت زنجیره‌ای بسته شد
اگر پروتکل را روی WireGuard یا MASQUE H3 گذاشته بودید و بعد سایفون یا تور را جلویش می‌گذاشتید، Aether از کنار آن کریر بیرون می‌رفت — یعنی از همان آدرسی که زنجیره برای پنهان کردنش وجود داشت. حالا پشت هر کریری خودکار روی MASQUE H2 قفل می‌شود.
به هر کریر همان‌قدر وقت داده می‌شود که لازم دارد
جست‌وجو قبلاً هر تلاش را سر ۹۰ ثانیه می‌برید، در حالی که سایفون در اولین اتصال روی شبکهٔ سخت تا ۵ دقیقه وقت می‌خواهد. نتیجه‌اش این بود که روی سخت‌ترین شبکه‌ها — دقیقاً جایی که این دکمه برای آن ساخته شده — هیچ‌وقت جواب نمی‌داد.
و چند چیز کوچک‌تر
• جست‌وجو ساعت نشان می‌دهد و از اول می‌گوید چقدر ممکن است طول بکشد
• سایفون می‌گوید اولین اتصالش روی شبکهٔ سخت چند دقیقه است، تا فکر نکنید هنگ کرده
• عمق جست‌وجو (از turbo تا thorough)
حالا واقعاً رعایت می‌شود
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.1
ویندوز → .exe
مک (اپل سیلیکون) → macos_arm64.dmg
مک (اینتل) → macos_x86_64.dmg
لینوکس → .AppImage یا .deb / .rpm
@whitedns</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/whitedns/1777" target="_blank">📅 14:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1776">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/K4nVRkmVyynDA6RcymAnfC0kJONlIjS9p0NbGEJxF6wCMwKy95AmbC686qaTiHMoQY0VY215W7Xsy48cNsBFHUcHvjXyI4IGHQqoO1bTjtfT_go9yqNTHXAIRmpbxMLYEek63vLEuuTuwvmqpPxzi-7bxH0gJwPQ1zqKdSl3jkIr2J3FlTk47ldX8VYscJCMc2lTxe8yzmMnJe0zPDgq7LpMFWaa1JQ0xNNXiznv78S_qhpKAameSTeAhwDilEAwqRymNns06GY1dLS9dz_Aif3RRpqk9_kvpi4IfnCBHggNfvE7lfxlt8YvXN_h_Lih0o4gcVM8BrTdBi-5hGTRXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه پایدار WhiteAesther به‌زودی منتشر می‌شود!
🚀
تجربه‌ای سریع‌تر، امن‌تر و مطمئن‌تر در دسکتاپ و موبایل. منتظر باشید
💚
@whiteaesther</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/whitedns/1776" target="_blank">📅 13:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1772">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/mg1jWoVJp2xBRQboxEQZ1aE9d0zIJPAvRB1guah5VT1EnSuppP3a-ltCa1wZMReU_9lhm6KEhzpQlLbEgAW1EqWDBSHS26UwlEI2abM5EiSV_MKeNH5VQX42mecORm2caK5F1TsG5z_B72U0RRB6qE4_EzTMFsQn9JTKg8fXaUxe1baJ4yYO8vXg-5YPe2BjvtFjz5D9qWnp0bzUwnj15fnGwU9MAWV8iep9tron_gOz5OTS20S6jwrUPef-VxqqzJ_boNd2YtbBJonm9Lji1JRDqK4jZgTRU7p4MW0GdS_Y7rK_djTSRArRrv4bUTOLAnySDVLElnnoiwcl36WMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتیم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://www.patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/whitedns/1772" target="_blank">📅 16:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1771">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دوستان :
⚠️
⚠️
اگر پست ها را کامل نخوندید . لطفا توی گروه ها پیام ندید . چون کاملا مشخص هست خیلی از دوستان حتی 10 ثانیه هم وقت نگذاشتند . این مدل پیام دادن فقط باعث گمراهی بقیه میشه . لطفا کاملا پست ها را مطالعه کنید .برنامه را کاملا بررسی کنید . تنظیمات متفاوت را انجام دهید وفقط با توجه به روشی که توی پست های بالا گفته شده گزارش کنید
سپاس</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/whitedns/1771" target="_blank">📅 16:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1770">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/N8s3UCsNP6CShSSZnZ7khfmS1g-FIrzsLnnagULInl2drGoWkTfteRhSIgbcmIWOXndR0ij1-gobNRDsLoCCD--jSbn9PwG7TR17LtRtPXXT0JBcez5vdgciAPtC8WPGBS2z1eUdGDHbVIpkto2c7wjummAcRAvc1sGZCx0nwFrsBDXd8EbSn6kQIaING-8oUMw2kvDJx551qx36n-mjZW5vt1hN0-VOc6aIp0qklOIXFBg9Mc4bFKSkR9vMiU1iZsO_VkKlVEOph0bwQqyq-Pj_GCZdsIsMfEJySW7pFWt9qJO9ZmUZUQn4uQY3PqtqI3AsWLdI5Shb8c87CU2osA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا توی نسخه اندروید هم شما حالت اتوماتیک دارید ، خودش می‌گرده و بهترین حالت را انتخاب می‌کنه و وصل میشه
#WhiteAesther_Mobile_1
.6.0</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/whitedns/1770" target="_blank">📅 15:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1769">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی WhiteAesther Mobile  1.6.0
حالت خودکار: فقط دکمهٔ اتصال را بزنید
🔥
🔥
🔥
🔥
⚠️
این نسخه آزمایشی است و ممکن است باگ داشته باشد. داخل برنامه اعلان به‌روزرسانی برایش نمی‌آید و فقط از لینک پایین نصب می‌شود.
✨
چه چیزی جدید است؟
دیگر لازم نیست بدانید اتر، سایفون یا تور کدام روی اینترنت شما کار می‌کند. در حالت «خودکار» برنامه خودش اول اتر را امتحان می‌کند و اگر نشد سایفون و تور را، و راهی را انتخاب می‌کند که واقعاً اینترنت از آن رد شود.
راهی را هم که روی هر شبکه کار کرد یادش می‌ماند؛ دفعهٔ بعد روی همان وای‌فای یا همان سیم‌کارت خیلی سریع‌تر وصل می‌شود.
📱
استفاده
برای بیشتر کاربران خودکار از قبل روشن است؛ فقط دکمهٔ اتصال را بزنید.
اگر قبلاً حامل را دستی انتخاب کرده‌اید: تب «مسیرها» ← کارت «حامل» ← «خودکار (پیشنهادی)».
⏳
اولین بار روی یک اینترنت سخت ممکن است چند دقیقه طول بکشد؛ لطفاً صبر کنید. روی صفحه نوشته می‌شود الان کدام راه را امتحان می‌کند.
🐞
اگر مشکلی دیدید: تنظیمات ← تشخیص ← «ارسال برای توسعه‌دهنده»، و بنویسید چه اینترنتی دارید.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.6.0
• بیشتر گوشی‌ها: WhiteAestherMobile-1.6.0-arm64-v8a.apk
• اگر مطمئن نیستید: WhiteAestherMobile-1.6.0-universal.ap
@whitedns</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/whitedns/1769" target="_blank">📅 15:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1768">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/HD_XFGg5LuuhDMbYO861LRClDUtHBKRhrrsWIKhq7jisa_XgGhjxW_8XDwCI5WhJVQFtJ9TQMUXDIt4MAJKh13RmPbzuxBch-8YraETVRdvpHNCaHVQmmAzURThkEohQCbjvf97gFOcJG3ephQaWGjOH2jbXnJvaoRqR7UvZahvTrwR3hHXPH4lOmjHt9JLUPxH9IHtZsT9op27giIVEH5aWJuGkuwBB9kI9Pk5szHRjEexVrjQCf-jX1wGQglpotuDhebpqAKBeKpoVU7IhBnYtknpUmZrvmeyVjN_T5cdFwrQbmlQwWgZShV-1nnYjcnt2xqAJ6Zv-iLU_y_RTwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی نسحه دسکتاپ یک گزینه اتوماتیک ما داریم . که خودش بهترین کانکشن را براتون پیدا میکنه
#
WhiteAesther_desktop_1
.9.0</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/whitedns/1768" target="_blank">📅 14:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1767">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دوستان :
اموزش هایی که ما توی پست های کانال میگذاریم به خدا برای شماست - والا ما خودمون بلدیم !
خواهشا وقت بگذارید مطالعه کنید</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/whitedns/1767" target="_blank">📅 14:45 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
