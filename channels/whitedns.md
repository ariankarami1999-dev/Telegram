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
<img src="https://cdn4.telesco.pe/file/Lf2Zh5d8QvMFFVyEOsSMYKftOnni1arq6x1P710Mkt8MNlaPn_lDOpXo4NqZDOy4eB3Y4jxzuocskAo_pIe8-kq0fhq4aKEih3oiZfsRo7X87At2RZcaC1adkbeTNCZ-JWASd1NvZ0_KSklAcbnkuef_16__edJ_SMpd8E1BIGwKRh2iHSyDVHG5TlzaIaRos-IdsV3yQzcVVuLWSVji9FlyDL2KEqZB2aQG2Je4yzUjWkyliWBvyLrgEWmlHjZjgOVLAIbzGZ6XiVOSms171PbXiO5n22C2Hi7gyu4RT-hydERh57q3XMtnYaZAg-jt3M4xSeE_DG6pKxuuWVv6lg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 108K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 17:38:33</div>
<hr>

<div class="tg-post" id="msg-1739">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دوستانی که علاقه به AI و برنامه‌نویسی دارید، من یه چنل شخصی 《پدی》 شروع کردم که اگر به اون موضوع علاقه دارید میتونید جوین بشید
❤️
https://t.me/iampediii/5</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/whitedns/1739" target="_blank">📅 13:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1738">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-poll">
<h4>📊 سرور های اختصاصی براتون وصل میشن؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/whitedns/1738" target="_blank">📅 11:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1737">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gS6DZgrjDnfGgPROAjYsjjRgO_nb7zn-FiM9ogCw5ZWVT4UuEPFxKotYJAOAH84JOg9jpNA6snPTaIMN_6nC__SI1R6QNQH8eR5_FjsH68N1ohrhhKpDgk8UhDYol0Rp7m5-eRf6rXcEDzNurbLV7Uc2Yq0QHMIWfc0qgGuAHm_ak4rhwsQAdgwJcULSSIJAdYCD9VlUAH1vNh78YahWWg6pYBLCVR7An0cyM5-ZLOFISYs8loC3Px6tKr0pUFeJoMtnOZ32YA8WfKZjtMsvntN0g2ghePuJuxU6BOLjvUNNT5UwZDVv7wg8GcMqq8W1wRElX87L2Rk6y2SJGcjHFA.jpg" alt="photo" loading="lazy"/></div>
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
💬
Support Bot:
@WhiteDnsResponder_bot
🔗
WhiteDnsChain
@WhiteDnsChainbot
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/whitedns/1737" target="_blank">📅 08:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1736">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">از دیروز تا حالا تعداد اتصال‌ها چند برابر شده؛ از کامنت‌هاتون هم معلومه که این تغییر رو حس کردید
🙌
جالبه بدونید ما با فقط ۱۰ تا سرور و ماهی ۱۵۰ دلار هزینه، داریم هر هفته به حدود ۵۰ هزار کاربر فعال داخل اپ WhiteVPN، رایگان سرویس می‌دیم!
این تازه بدون حساب کردن کاربرهای ویندوزه؛ با اون‌ها، آمار خیلی بیشتر هم می‌شه.
😑
آدم این عددها رو که می‌بینه، بیشتر حرص پول‌هایی رو می‌خوره که تا امروز به فیلترشکن‌فروش‌ها داده
واقعاً ممنون از انرژی مثبتی که بهمون می‌دین و وقتی که می‌ذارید تا تجربه‌هاتون رو زیر پست‌ها بنویسید. همین بازخوردها کمک می‌کنه بفهمیم کجا خوب پیش رفتیم و کجا هنوز باید بهتر بشیم.
به‌زودی WhiteVPN Desktop رو هم با سرورهای اختصاصی آپدیت می‌کنیم تا کاربرهای دسکتاپ هم از این اتصال‌ها استفاده کنن.
🎮
یه سورپرایز هم برای کاربرهای WhiteAesther و بچه‌هایی داریم که دنبال سرویس مخصوص گیمینگ بودن
ممنون که کنارمونید
🤍
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/whitedns/1736" target="_blank">📅 06:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1735">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ما سعی میکنیم هر ۲
یا
۳ روز سرور هارو عوض کنیم تا تا جای ممکن از فیلتر شدن آی‌پی ها جلوگیری کنیم
.
همچنین کشور های دیگه رو هم اضافه میکنیم تا آپشن های بیشتری داشته باشید
❤️
🛡
سرور های اختصاصی رایگان، امن و مدیریت شده توسط
تیم ما هستن.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/whitedns/1735" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1734">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🛡
انتشار نسخه جدید WhiteVPN 1.6.6
لطفا تست کنید و نتیجه رو با ما به اشتراک بگذارید. امیدوارم همه بتونید به سرور های اختصاصی وصل بشید.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/whitedns/1734" target="_blank">📅 14:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1729">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.6-arm64-v8a.apk</div>
  <div class="tg-doc-extra">36.1 MB</div>
</div>
<a href="https://t.me/whitedns/1729" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/whitedns/1729" target="_blank">📅 14:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1728">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMMAEUzTbM4PAGA7zKR92fTkXsVMV3TJVaCQOThLqkIx-Z2rJKFSomZs8wlscwvg2j1oVvTBDsks5o02FZhXyyfheg9nzaEGvw8-6R73RLInBYJcyXwhncA6R-d7jD-YX5Q88uc-068iAosguYox4s0bmD3iaDerPe9ZrYYxuzYV-8swEw0-xWFz6HP0NTCMJtU5r8C3G6-2LrFIR-h7lKFtujn4xp1qv5Fq4ShC-exxOmXQaB81J715K7FrMF1DJyP8bwaaDBN6KFl0e8_vfLEYUrJiz8wOYQjnNki3mAXRLXtCont2SmZhd1Klnx_8hgm8g_CerXN4ItWfbl_iXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
انتشار نسخه جدید WhiteVPN 1.6.6
🟢
توی این نسخه ما ۱۰سرور اختصاصی WhiteVPN گذاشتیم. همه داخل فنلاند هستند.  بعد از تست کردن سرور کشور های دیگه رو هم اضافه میکنیم.
در صورت فیلتر شدن سرویس ها، سرور هارو جایگزین میکنیم.
🟢
توی این ورژن، اپ اول سعی میکنه به سرور های اختصاصی WhiteVPN وصل بشه، در صورتی که امکان‌پذیر نبود بعد سرور های عمومی رو امتحان میکنیم.
📱
دانلود آخرین نسخه از گیتهاب
✍️
دوستانی که ورژنی که دقیقه هایی پیش فرستادیم رو گرفتن، دوباره دانلود و نصب کنید.
❤️
نتیجه اتصال رو برای ما بفرستید.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/whitedns/1728" target="_blank">📅 14:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1725">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✍️
یه زودی یک آپدیت جدید داریم برای WhiteVPN روی اندروید.
توی این ورژن سرور های اختصاصی WhiteVPN رو اضافه کردیم. برای شروع ۱۰تا سرور اختصاصی فنلاند به صورت آزمایشی اضافه کردیم.
اگر بازخورد ها خوب بود، سرور های کشور های مختلف رو اضافه میکنیم.
توی این ورژن جدید، اپ اپل سعی میکنه به سرور های اختصاصی ما وصل بشه، بعد میره روی سرور های عمومی.
خیلی زود برای دستکتاپ هم آماده میشه.
@WhiteDNS</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/whitedns/1725" target="_blank">📅 13:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1724">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚀
نسخه جدید WhiteDNS Clean IP Finder منتشر شد — v1.4.3
این آپدیت، قابلیت‌های جدید و اصلاحات مهم نسخه‌های v1.4.1 تا v1.4.3 را یک‌جا ارائه می‌دهد.
✨
مهم‌ترین تغییرات:
⚡️
اضافه شدن حالت اسکن سریع
Fast Scan Mode
🌐
اضافه شدن انتخابگر شبکه‌های Edge
Edge Network Picker
☁️
پشتیبانی از سرویس‌های مختلف از جمله:
Cloudflare • Cloudflare Pages • Vercel • Render • Railway •
Fly.io
• Netlify • Koyeb • Glitch
🎯
اسکن هوشمند بر اساس دامنه‌های اختصاصی هر پلتفرم، برای پیدا کردن IPهای واقعاً قابل استفاده
🔐
افزایش دقت در اسکن‌های Scoped با بررسی معتبرتر Certificate و پاسخ دامنه
🌍
اصلاح تشخیص روی Port 80 و جلوگیری از نتیجه‌های اشتباه مبتنی بر CDN Header
🚂
بازگشت دامنه
railway.app
به دامنه‌های شناسایی Railway
🛠
بهبود منطق اسکن، افزایش دقت نتایج و رفع چندین باگ
📱
💻
نسخه‌های منتشرشده برای:
Android • Windows • Linux • macOS • Termux
اگر هنوز از نسخه‌های قبلی استفاده می‌کنید، پیشنهاد می‌شود مستقیماً به v1.4.3 بروید.
🔗
دانلود آخرین نسخه:
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.4.3
@whitedns</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/whitedns/1724" target="_blank">📅 21:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1723">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب
https://youtu.be/h920xIQCMP4?si=gjpsrzgky62iOy25
@whitedns</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/whitedns/1723" target="_blank">📅 20:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1721">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">موقت :
دوستان گرامی ، اون کانفیگ هایی که ما توی ربات
@WhiteDnsChainbot
می‌دیم خدمت شما برای
"exit chain
" هست ,
توی v2ray و بقیه آپ ها میزنید و بعد پیام میدید چرا کار نمیکنه ؟ خوب معلومه نباید کار کنه
روزی ۱۰۰ - ۲۰۰ پیام اینجوری داریم میگیریم ،و نمیشه هی تکرار کرد ، خواهش میکنم قبل از استفاده از هر چیزی مطالب کانال را مطالعه کنید ،
پست زیر را بخونید خواهشاً ،
https://t.me/whitedns/1608
اگر موردی هست که سوال دارید و جوابتون را پیدا نکردید  از ربات پاسخگو بپرسید
@WhiteDnsResponder_bot
@whitedns</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/whitedns/1721" target="_blank">📅 13:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1718">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-text">📦
WhiteDNS Tools — Downloads
━━━━━━━━━━━━━━━━━━
📱
WhiteAesther
• Mobile:
https://github.com/WhiteDNS/WhiteAestherMobile/releases
• Desktop:
https://github.com/WhiteDNS/WhiteAesther/releases
━━━━━━━━━━━━━━━━━━
🛡
WhiteVPN
• Mobile:
https://github.com/WhiteDNS/WhiteVPN/releases
• Desktop:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases
━━━━━━━━━━━━━━━━━━
🌐
WhiteDNS — مناسب دوران قطعی
• Android:
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
• Desktop:
https://github.com/WhiteDNS/WhiteDNS-Desktop/releases
━━━━━━━━━━━━━━━━━━
🔎
WhiteDNS Clean IP + Resolver Finder
• Desktop & Mobile:
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases
━━━━━━━━━━━━━━━━━━
🍎
CoreForge VPN + DNS — iOS
• TestFlight:
https://testflight.apple.com/join/DRkT6zny
━━━━━━━━━━━━━━━━━━
🎓
آموزش‌ها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVPN
https://youtu.be/yx-jFqv9pYM
🛡
آموزش کامل WhiteVPN
https://www.youtube.com/watch?v=tm0ls3r4ppw
📱
آموزش کامل WhiteAesther
https://www.youtube.com/watch?v=cRfqxbDY1Dg&t=1s
🌐
آموزش کامل WhiteDNS
https://www.youtube.com/watch?v=tz8cj7HzHVI
🍎
آموزش کامل CoreForge
https://www.youtube.com/watch?v=filwdiPKN90
🔎
آموزش کامل اسکنر WhiteDNS
https://www.youtube.com/watch?v=N5hKuWXp37w
━━━━━━━━━━━━━━━━━━
@whitedns
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1718" target="_blank">📅 20:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1712">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cV12CD8eK-dpOv7Fa2L-skDGe6zBInpw33tG1DrgOcFjtNjvbGbeN5WmJ_2XJcy2H0Btlci0Tmfxn-jNRzWPJVqhtivG3fZn-PIu99fD3WJ1XNtCNLfzTn7h1QYYo1m_XFUcZmhzi3DAVObGZz82v7mxl7gf1zuobWbVogIkcJfkH_-d93B0q3KdfmYt1carzGGR4gWz2hNDHDJTCkHKbUTUZrjD7EzuQ04pdnHmtUkhHetnEhxn9MBKUOrZkyJzQzLv9DbAVTCICjSvOPKS9U5oWspKhKyvrSYtY5Z_ckz6FXEBMWWi-mQwOxomRikG0_ti91Gy2-cFyBX0As8qFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/whitedns/1712" target="_blank">📅 13:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1711">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/MZ5AJlfYu1umk81kOc9GgW50Ab8sKMNJ24Q2hV_-W22DDHmkRliM5lx8fJHWjpB0g_jFdwTPb5_K97N3r9i7UDn3trS03QUG-kbKsCTneJwd0paDKrGR6ZgiMuAT9UfAsFXMAHaUd49GVM_0Smbprmy9tceuREFeyvDOSUPXV1t7XRhhml2B8lxNQM1PkLa94tmY27YrIEPqgMU68ejRpTU0FW8sT5-1ImMwERzmZIn6XcXmDO0P0RvKk_iYUJr7NBUCado90BMblo4InUPk0Ho9n19SrcC6KMMbpLHVSTDibZCQpl_1pgf615QWyuvbtlo9t5unTAWcQ-J7RmmygA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
راهنمای کامل استفاده از ربات WhiteDnsChain
(کانفیگ هسته x-ray )
نکته : این ربات یک کانفیگ اضطراری برای شما ایجاد میکند تا در موارد خیلی خاص از ان استفاده کنید . کانفیگ های این ربات برای امکان exit chain در اپ های white ایجاد شده و هر گونه سواستفاده از آن مجاز نیست
🤖
آدرس ربات:
@WhiteDnsChainbot
برای دریافت و مدیریت اتصال اختصاصی خود مراحل زیر را انجام دهید:
1️⃣
شروع و انتخاب زبان
- وارد ربات شوید.
- دستور /start را ارسال کنید.
- گزینه «
🇮🇷
فارسی» را انتخاب کنید.
- برای تغییر زبان در آینده از گزینه «
🌐
تغییر زبان» استفاده کنید.
2️⃣
درخواست کانفیگ
- روی «
🔐
دریافت کانفیگ» بزنید یا دستور /config را ارسال کنید.
- درخواست شما برای مدیر فرستاده می‌شود.
- پس از تأیید، یک پیام اطلاع‌رسانی دریافت می‌کنید.
- دوباره /config را بزنید تا لینک اشتراک و QR اختصاصی شما نمایش داده شود.
3️⃣
اضافه‌کردن کانفیگ به برنامه
- یک برنامه سازگار با V2Ray/Xray روی دستگاه خود نصب کنید.
- لینک اشتراک را کپی کنید.
- در برنامه گزینه افزودن Subscription یا «افزودن اشتراک» را انتخاب کنید.
- لینک را وارد کرده و اشتراک را به‌روزرسانی کنید.
- یکی از سرورها را انتخاب کرده و اتصال را فعال کنید.
4️⃣
مشاهده وضعیت حساب
از گزینه «
👤
حساب من» یا دستور /account استفاده کنید تا موارد زیر را ببینید:
- وضعیت فعال یا غیرفعال
- تاریخ انقضا
- حجم مصرف‌شده
- حجم کل
- محدودیت تعداد دستگاه یا IP
5️⃣
دریافت دوباره کانفیگ
اگر پیام کانفیگ را پاک کردید، نگران نباشید. با /config همان کانفیگ اختصاصی دوباره نمایش داده می‌شود و کانفیگ جدیدی ساخته نخواهد شد.
6️⃣
پشتیبانی
- روی «
💬
پشتیبانی» بزنید یا /support را ارسال کنید.
- مشکل خود را در یک پیام کامل توضیح دهید.
- پیام مستقیماً برای مدیر ارسال می‌شود.
- پاسخ مدیر را داخل همین ربات دریافت خواهید کرد.
7️⃣
دستورات کاربردی
- /start — شروع و انتخاب زبان
- /config — دریافت کانفیگ
- /account — مشاهده وضعیت حساب
- /menu — نمایش منوی اصلی
- /support — ارتباط با پشتیبانی
- /help — نمایش راهنما
⚠️
نکات مهم
⚠️
-درخواست ها توسط ادمین دونه دونه بررسی و تایید میشود پس لطفا صبور باشید
- ادمین کاملا مختار است که به هر دلیل ممکن از ارایه کانفیگ به شما خودداری کند پس لطفا اعتراض نکنید
⚠️
-در حال حاظر کانفیگ ها با محدودیت 1 روزه و یک گیگ هست
- لینک و QR کاملاً اختصاصی است؛ آن را برای دیگران ارسال نکنید.
- هر حساب تلگرام فقط یک کانفیگ فعال دریافت می‌کند.
- ارسال چندباره /config کانفیگ تکراری ایجاد نمی‌کند.
- برای امنیت بیشتر، پس از دریافت کانفیگ می‌توانید پیام آن را با گزینه «
🗑
مخفی کردن» حذف کنید.
- در صورت پایان حجم یا اعتبار، از طریق پشتیبانی با مدیر ارتباط بگیرید.
@whitedns</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/whitedns/1711" target="_blank">📅 13:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1710">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">WhiteAesthe Desktop 1.7.1 — حالا کامل فارسی منتشر شد
🔥
🔥
از این نسخه، تمام برنامه فارسی است. نه فقط صفحهٔ اول — تمام تنظیمات پیشرفته، زنجیرهٔ خروج، جستجوگر دروازه و پیام‌های وضعیت.
اگر انگلیسی بلد نیستید، دیگر لازم نیست حدس بزنید کدام کلید چه کار می‌کند.
━━━━━━━━━━━━━━━━━━
🔤
چطور فارسی کنم؟
هیچ کاری لازم نیست.
اگر ویندوز یا سیستم شما فارسی است، برنامه خودش بالا می‌آید فارسی.
اگر می‌خواهید دستی عوض کنید: بالا سمت راست پنجره، کنار آیکون تنظیمات، دکمهٔ فا را بزنید. برای برگشت به انگلیسی همان‌جا EN را بزنید.
انتخاب شما ذخیره می‌شود و دفعهٔ بعد هم همان می‌ماند.
━━━━━━━━━━━━━━━━━━
📐
کل چیدمان راست‌به‌چپ شد
فقط کلمه‌ها ترجمه نشدند — منوی کناری، ردیف‌های تنظیمات، دکمه‌ها و نوارها همه به سمت راست منتقل شدند، همان‌طور که یک فارسی‌زبان انتظار دارد.
سه نکته که عمداً برعکس نشدند:
• نمودار تأخیر — زمان همیشه از چپ به راست می‌رود، هر زبانی که باشد. اگر آینه‌اش می‌کردیم، «اکنون» سر قدیمی‌ترین نقطه می‌افتاد. • اعداد لاتین ماندند — آی‌پی، پورت و میلی‌ثانیه با ارقام فارسی خواناتر نمی‌شوند، بدتر می‌شوند. ارقام فارسی فقط داخل متن‌ها استفاده شده‌اند. • اسم‌های فنی — MASQUE، WireGuard، DNS، TLS و مثل این‌ها دست‌نخورده ماندند. ترجمه‌شان فقط گیج‌کننده بود.
━━━━━━━━━━━━━━━━━━
🔍
جستجوی تنظیمات، هر دو زبان
Ctrl + K را بزنید و تایپ کنید.
فارسی تایپ کنید یا انگلیسی — هر دو کار می‌کند. اگر اسم انگلیسی یک تنظیم را از قبل بلدید یا در یک پست انجمن دیده‌اید، لازم نیست معادل فارسی‌اش را حدس بزنید.
مثال: هم «مسیرها» جواب می‌دهد، هم routes. هم «تونل کامل»، هم full tunnel.
━━━━━━━━━━━━━━━━━━
⚙️
موتور به Aether 1.8.0 ارتقا پیدا کرد
چهار مورد که مستقیماً به کار شما می‌آید:
۱. پروکسی بالادستی با یوزر و پسورد — اگر در تنظیمات «اتصال از طریق یک پروکسی محلی» را با نام کاربری و رمز پر کرده بودید، موتور در نسخهٔ قبل رمز را اصلاً نمی‌فرستاد. درست شد.
۲. تونل WireGuard بعد از یک خطای داخلی بالا نمی‌آمد و تا ری‌استارت کامل برنامه برنمی‌گشت. چون پیش‌فرض ما WireGuard است، این را احتمالاً دیده‌اید.
۳. حالت WARP in WARP کرش می‌کرد و بعدش دیگر وصل نمی‌شد.
۴. یک آسیب‌پذیری امنیتی شناخته‌شده در یکی از کتابخانه‌های رمزنگاری حذف شد.
━━━━━━━━━━━━━━━━━━
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases
ویندوز · لینوکس (deb / rpm / AppImage) · مک (اینتل و اپل سیلیکون)
از این نسخه به بعد، وقتی آپدیت جدید بیاید خود برنامه بالای صفحه به شما خبر می‌دهد.
━━━━━━━━━━━━━━━━━━
💬
اگر ترجمه‌ای به نظرتان نامفهوم یا اشتباه است، همین‌جا بگویید — عوضش می‌کنیم.
@whitedns</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/whitedns/1710" target="_blank">📅 18:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1709">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎉
نسخهٔ ۱٫۳٫۰ WhiteAesther android منتشر شد —
برنامه فارسی شد
بزرگ‌ترین تغییر از زمان انتشار .
🔥
رابط کاربری کامل فارسی
همهٔ برنامه، حدود ۴۵۰ عبارت — از صفحهٔ اول تا تنظیمات پیشرفته، اعلان‌ها، و کلید تنظیمات سریع.
زبان را خودتان انتخاب می‌کنید، نه گوشی. در تنظیمات ← زبان سه گزینه هست: سیستم، English، فارسی.
چرا مستقل از گوشی؟ چون این دو برای خیلی‌ها یکی نیست: گوشی‌ای که انگلیسی مانده چون همه‌جا همین‌طور فروخته می‌شود، ولی صاحبش فارسی می‌خواند — و برعکس، کسی که گوشی‌اش فارسی است ولی اصطلاحات انگلیسی را ترجیح می‌دهد.
🔤
فونت وزیر
متن فارسی با فونت وزیرمتن نمایش داده می‌شود، با فاصلهٔ سطر تنظیم‌شده برای خط فارسی.
فونت داخل خود برنامه است، نه اینکه هنگام اجرا از اینترنت گرفته شود. برنامه‌ای که کارش نفرستادن ردپا از شماست، نباید برای یک فونت درخواستی بفرستد که نام دستگاه شما را ببرد.
🔢
عددها
در متن، عدد فارسی. در مقادیر فنی — آدرس IP، پورت، سرعت، مدت اتصال — عدد لاتین.
آدرسی با رقم فارسی نه خوانا است و نه قابل کپی.
🐞
دو کرش وارپ‌در‌وارپ رفع شد
▫️
موقع قطع شدن: برنامه هنگام پایان نشست ناگهان بسته می‌شد.
▫️
موقع وصل شدن: همان موردی که در ۱٫۲٫۷ رفع شد و اینجا هم هست.
⚙️
هستهٔ Aether به ۱٫۸٫۰ رفت
کتابخانه‌های رمزنگاری به‌روز شدند و خواندن هدر پروکسی سریع‌تر شد.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases
▫️
arm64-v8a
— تقریباً همهٔ گوشی‌های ۲۰۱۷ به بعد
▫️
armeabi-v7a
— گوشی‌های قدیمی‌تر
▫️
universal
— اگر مطمئن نیستید
نیازی به حذف برنامه نیست؛ روی نسخهٔ قبلی نصب می‌شود و تنظیماتتان می‌ماند.
💬
اگر ترجمه‌ای به نظرتان نارسا بود یا جایی متن از کادر بیرون زد، همین‌جا بگویید. زبان چیزی است که فقط با استفادهٔ واقعی درست می‌شود.
@whitedns</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/whitedns/1709" target="_blank">📅 16:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1708">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxH35G82uhDRLbGBVf6f2N5lwXdZpVQgb2sBiaGhheio9lAoPCgDUF-IsyKrkG0TkoVaCu9xu8dQAB5AH4LLnitfn6uPBbx2n_lrmg58LqfvDbCIcqy0LbWYJ_UHtbppXxmyQiq0kuIF6Q4kMnHQN6VQv79_NoBmaKssKTDqxJrl9jpemqU1ClLV40DEBq3pGzFgRM7fJBuE_0bWWKV5n3jYfzHLAsws1iR8bUMH5GQa02lSGSvjtyVKcMCqiaXrjgicBInCvnFd_oZC0VA-4bjRboVu6crVApIVoLZpPSbL_TGn0d_l4hSxwnY6UVBMR0ZCui85OjD043zqUM4bfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
این هم یکی دیگه از تست‌های موفق ما بود؛ تستی که با همراهی و بازخوردهای شما، کنار هم مشکلاتش رو برطرف کردیم.
👑
بیش از ۶ ساعت اتصال پایدار و بدون قطعی
به‌زودی ظرفیت سرورهای اختصاصی WhiteVPN رو چند برابر می‌کنیم. این سرورها فقط از طریق خود اپلیکیشن در دسترس شما قرار می‌گیرن.
تیم WhiteDNS، یک تیم کوچک و با محصولاتی کاملاً رایگانه و هیچ درآمدی از کاربرانش نداره؛ تنها پشتوانه‌ی ما، حمایت شما از کانال یوتیوب و یوتیوب WhiteDNSـه.
❤️
ممنون که کنارمون هستید و کمک می‌کنید این مسیر رو ادامه بدیم.
به امید روزی که نیاز به هیچکدوم ازین ابزار ها نداشته باشیم.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/whitedns/1708" target="_blank">📅 16:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1697">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/whitedns/1697" target="_blank">📅 18:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1695">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خرید و فروش کانفیگ در کل گروه های whitedns ممنوع است
⚠️
بلافاصله بدون اخطار = ban</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/whitedns/1695" target="_blank">📅 17:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1694">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/616b32759e.mp4?token=OS2jOq8KwpKbOtTAgSm36yhm1xphDqQeP-oGjaHaKs37y9DoiNwRq_3OxqIxBb7Tf44wc8ViAiJKWSYhI8AU4DO7iB8OGjhXntCd9PXWyXm-na_dRYh8FtpbhD2xF09JrWkn_4OShfAO1F40xC9ibJ286cCuIy9BLpmx1b-EXecH478To7HCz6NialJR7ZaaJnpQ1qRTOX1I7BVl-mclMN5r1099qQUUVRAElkNvfC2GxuZgvPYPVKOT1riSqwSsqtgkRYwPcmtM1b1MAwqFru5HrA4La7iXW9Qx0c838s4cs53XPvSuY0Z7T1b6VVSOuJE76I4nKdCPTDidOHX8Rp-uJXCtTxjKHlQLucQpaC4sVJgivXvgMvlB86EG2MwfipuDyevvocWMAZAOwg1ynjP98yNWE2lGEEb4kjOTgw2cQYyGsSLGbyyKvKlMGGVNmCbNrx7nzXnjlcwnIPGOtCZub-zAGpUCgB8VB0pTFXAaMGtggNnc1f9kgRhFhlaTykrNAjzIa8G5SRnQ8hZBWpzeTyBgwvRjx-XpZLrqvM_T-zCE9y4-p13wZLCBRfKcxKzurj85_H9ATEJygJWrgch61-Wrxnz83Engu1QJCrPA2BZCufs_2XXLOIEQ2pxG9FxjXOmsNiBV3ume-yNfaNFcybVPg30UqE-LoLbfaaI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/616b32759e.mp4?token=OS2jOq8KwpKbOtTAgSm36yhm1xphDqQeP-oGjaHaKs37y9DoiNwRq_3OxqIxBb7Tf44wc8ViAiJKWSYhI8AU4DO7iB8OGjhXntCd9PXWyXm-na_dRYh8FtpbhD2xF09JrWkn_4OShfAO1F40xC9ibJ286cCuIy9BLpmx1b-EXecH478To7HCz6NialJR7ZaaJnpQ1qRTOX1I7BVl-mclMN5r1099qQUUVRAElkNvfC2GxuZgvPYPVKOT1riSqwSsqtgkRYwPcmtM1b1MAwqFru5HrA4La7iXW9Qx0c838s4cs53XPvSuY0Z7T1b6VVSOuJE76I4nKdCPTDidOHX8Rp-uJXCtTxjKHlQLucQpaC4sVJgivXvgMvlB86EG2MwfipuDyevvocWMAZAOwg1ynjP98yNWE2lGEEb4kjOTgw2cQYyGsSLGbyyKvKlMGGVNmCbNrx7nzXnjlcwnIPGOtCZub-zAGpUCgB8VB0pTFXAaMGtggNnc1f9kgRhFhlaTykrNAjzIa8G5SRnQ8hZBWpzeTyBgwvRjx-XpZLrqvM_T-zCE9y4-p13wZLCBRfKcxKzurj85_H9ATEJygJWrgch61-Wrxnz83Engu1QJCrPA2BZCufs_2XXLOIEQ2pxG9FxjXOmsNiBV3ume-yNfaNFcybVPg30UqE-LoLbfaaI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✍️
اگر WhiteVPN فقط با زدن دکمه 《اتصال》 براتو کار نمیکنه، میتوین کانکشن هارو دستی تست کنید و بعد وصل بشید.
⛏
این ویدیو ۱دقیقه بهتون یاد میده چطوری این کار رو انجام بدید.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/whitedns/1694" target="_blank">📅 15:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1693">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sn80DMGpDqxPOfVglfmFrGA-f69pv89Ckpg_YVtEM8t9i0EZMfZHwG4Ya7tlqLVn_AqdH-LJRT0PwCZ8zQLgHOjOiHnKDtwiLVtmDFE2r5gVpMCq8ugwKV1_rZJCNLJT8so2M3IXkJI4n5EL5YGbpGLvkBjBZJZN7JQynJ0w4OQkV7ixOjE-I8ojWsGM-merC-83YWj5tYYXBAv7xMDo4pudUUmhjtkUvp3Af301wMk4v4IHPCusPI02QgSHl3l95_ZV-i9e-MMzGVv4ygVg2YMwKJp1BHv61oI2kE6dN6TYMl19dFhA29Z10vv_ghz1hFBr-PPeJg4yuSev1Lzi-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
ما تصمیم گرفتیم محتوی متفاوت در زمینه تکنولوژی داخل
چنل یوتیوب WhiteDNS
بذاریم
این اولین ویدیو متفاوت از موضوع هایی هست که تا  امروز داشتیم و توی این ویدیو دایانا ۵ ابزار کاربردی
و
رایگان هوش مصنوعی برای تولید محتوی در موضوع های زیر معرفی میکنه.
🎙️
Speechma — تبدیل متن به گفتار و ساخت صدای AI به‌صورت آنلاین
🎨
Leonardo AI — تولید تصویر، آثار هنری و تصاویر خلاقانه با هوش مصنوعی
🧪
Google Labs — آشنایی با پروژه‌ها، ابزارها و آزمایش‌های جدید هوش مصنوعی گوگل
📸
Clipdrop — مجموعه ابزارهای هوش مصنوعی برای ادیت و ویرایش عکس
🎶
Suno AI — ساخت آهنگ باکلام و بی‌کلام با استفاده از هوش مصنوعی
📹
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/1693" target="_blank">📅 11:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1690">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/azejSrZym6qdDOZJ7640WkAIouNbBY_q3Pk0jzlw9zonBbSxgPRwRvhl23j3Fh4JD0Lo4lIzSW5C2mbxEKgWsyHDO80wBcH3kOLjIp7NvQwmVs9vrWE-uxbzZnIMIgIuR71CvplDxxPmarwwSPS06VV0nYg0YNPg1lFkSpCK1ym9Myff0GHTgj4XL_7fWjxgW6yZ6G0x8CLo08mba3yC2pHCTyp_NJXk8YFb-A0GskMSQ_OukHjrZ63UjYcOmXBNrLo_wm-UaQEdn2adfvtnZaXsoIGRd3X9pgLdP_IxhYoFxQnpO1xP1cVywRunwE_BSk2eJMY7EDKNwWftQ1INww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/whitedns/1690" target="_blank">📅 11:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1689">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⚠️
اصلاحیه
نسخهٔ ۱.۲.۷ منتشر شد
اگر نسخهٔ ۱.۲.۶ را نصب کرده‌اید، لطفاً به‌روزرسانی کنید.
🐞
مشکل چه بود
در نسخهٔ ۱٫۲٫۶، اگر پروتکل را روی وارپ‌در‌وارپ می‌گذاشتید و دکمهٔ اتصال را می‌زدید، برنامه بسته می‌شد.
بقیهٔ پروتکل‌ها سالم بودند. فقط وارپ‌در‌وارپ.
🔧
چرا این اتفاق افتاد
در نسخهٔ ۱٫۲٫۶ یک باگ قدیمی را رفع کردیم که باعث می‌شد روی وارپ‌در‌وارپ مرورگرها باز نشوند. برای آن رفع، اندازهٔ بسته‌ها را به عددی تغییر دادیم که این تونل واقعاً می‌تواند حمل کند.
ولی آن عدد از حداقلی که پروتکل IPv6 لازم دارد کمتر بود، و اندروید این حداقل را اجباری می‌کند. نتیجه‌اش این شد که ساختن تونل رد می‌شد و برنامه بسته می‌شد.
یعنی رفع ما مشکل بدتری ساخت: قبلش وصل می‌شد و مرورگر کار نمی‌کرد، بعدش اصلاً وصل نمی‌شد.
بابت این اشتباه عذرخواهی می‌کنیم.
✅
در نسخهٔ ۱٫۲٫۷
حالا وقتی تونل نتواند IPv6 را حمل کند، برنامه آن را روشن نمی‌کند به‌جای اینکه بسته شود.
نتیجهٔ عملی: وارپ‌در‌وارپ فقط با IPv4 کار می‌کند. این محدودیت واقعی این تونل است، نه چیزی که بشود دورش زد.
هم اتصال درست کار می‌کند و هم مرورگرها باز می‌شوند.
به‌جز این، هیچ چیز دیگری نسبت به ۱٫۲٫۶ عوض نشده. تمام قابلیت‌هایی که در پست قبلی گفتیم سر جایشان هستند.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
▫️
arm64-v8a
— تقریباً همهٔ گوشی‌های ۲۰۱۷ به بعد
▫️
armeabi-v7a
— گوشی‌های قدیمی‌تر
▫️
universal
— اگر مطمئن نیستید
نیازی به حذف برنامه نیست؛ روی نسخهٔ قبلی نصب می‌شود و تنظیماتتان می‌ماند.
@whitedns</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/whitedns/1689" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1687">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔗
نسخه جدید اندروید whiteaesther منتشر شد -
🔥
1.2.6
این نسخه یک باگ مهم را رفع می‌کند و بخش زنجیرهٔ خروج را برای فهرست‌های بزرگ بهینه می‌کند.
پایین همه‌چیز با آموزش آمده.
🐞
رفع باگ: مرورگرها روی حالت وارپ‌در‌وارپ باز نمی‌شدند
اگر روی پروتکل وارپ‌در‌وارپ وصل می‌شدید و همه‌چیز درست به نظر می‌رسید ولی هیچ سایتی بالا نمی‌آمد، این همان مشکل بود.
چه اتفاقی می‌افتاد: اپ به گوشی می‌گفت بسته‌های بزرگ‌تری بفرست از آن‌چه این تونل می‌توانست حمل کند. درخواست‌های کوچک رد می‌شدند و هر چیز بزرگ‌تر بی‌صدا می‌افتاد.
برای همین بعضی برنامه‌ها مثل تست سرعت کار می‌کردند ولی مرورگرها نه — مرورگر بسته‌های بزرگ می‌فرستد.
این باگ از نسخهٔ ۱٫۲٫۲ بود و حالا رفع شده.
⚡️
زنجیرهٔ خروج برای اشتراک‌های بزرگ
اگر اشتراک شما صدها یا هزاران کانفیگ دارد، این بخش عملاً غیرقابل استفاده بود. چهار مشکل داشت که همه رفع شدند.
۱) باز شدن صفحه گوشی را قفل می‌کرد
اپ همهٔ ردیف‌ها را یک‌جا می‌ساخت، حتی آن‌هایی که روی صفحه دیده نمی‌شدند. حالا فقط همان‌هایی ساخته می‌شوند که می‌بینید.
۲) دکمهٔ تست همه تمام نمی‌شد
روی هزار کانفیگ حدود شانزده دقیقه طول می‌کشید و هیچ نشانه‌ای از پیشرفت نمی‌داد. حالا دکمه می‌گوید چند تا تمام شده، و همان دکمه متوقفش می‌کند.
۳) فقط چند تای اول پینگ می‌گرفتند
همهٔ تست‌ها یک‌جا فرستاده می‌شدند، یعنی صدها درخواست هم‌زمان از یک تونل. تونل اشباع می‌شد و بقیه به نتیجه نمی‌رسیدند. حالا دسته‌دسته فرستاده می‌شوند.
۴) اتصال، لحظه‌ای گوشی را قفل می‌کرد
اپ کار سنگینی را روی رشتهٔ اصلی انجام می‌داد، دقیقاً وقتی تونل بالا می‌آمد.
🆕
قابلیت‌های جدید در زنجیرهٔ خروج
مسیر: تب Routes ← گزینهٔ Exit chain
🔍
جست‌وجوی کانفیگ
بالای فهرست یک کادر جست‌وجو هست. بخشی از نام را بنویسید تا فیلتر شود. روی فهرست هزارتایی، این تنها راه پیدا کردن یک کانفیگ خاص است.
✅
انتخاب چندتایی
کنار هر کانفیگ یک تیک هست. چند تا را انتخاب کنید تا روی همه‌شان کار کنید.
⚠️
تیک با انتخاب کانفیگ فعال فرق دارد. برای عوض کردن کانفیگی که ترافیک از آن می‌رود، روی خودِ ردیف بزنید نه روی تیک.
🗑
حذف از فهرست
بعد از تیک زدن، دکمهٔ حذف ظاهر می‌شود.
⚠️
نکتهٔ مهم: کانفیگ‌های اشتراک واقعاً پاک نمی‌شوند، چون اپ دفعهٔ بعد دوباره اشتراک را می‌گیرد. اپ فقط آن‌ها را از فهرست کنار می‌گذارد.
اپ تعدادشان را نشان می‌دهد و یک دکمهٔ بازگردانی دارد، تا کانفیگی که ناپدید شده با اشتراک خراب اشتباه نشود.
🏓
دو نوع تست
هر دو دکمه حالا بالای فهرست هستند، نه پایین آن.
▫️
Test all — همه را امتحان می‌کند. روی فهرست بزرگ چند دقیقه طول می‌کشد.
▫️
Test selected — فقط آن‌هایی که تیک زده‌اید.
راه عملی برای فهرست بزرگ: با جست‌وجو چند تا را پیدا کنید، تیک بزنید، و دومی را بزنید. خیلی سریع‌تر از امتحان کردن هزار تا.
📶
مرتب‌سازی خودکار
فهرست خودش مرتب می‌شود: سریع‌ترین‌ها اول، بعد آن‌هایی که هنوز تست نشده‌اند، و آخر آن‌هایی که این نسخه نمی‌تواند به آن‌ها وصل شود.
📺
اندروید تی‌وی
تیک‌های جدید با کنترل تلویزیون و دستهٔ بازی هم کار می‌کنند و حلقهٔ فوکوس دارند.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
▫️
arm64-v8a
— تقریباً همهٔ گوشی‌های ۲۰۱۷ به بعد. از این شروع کنید
▫️
armeabi-v7a
— گوشی‌های قدیمی‌تر
▫️
universal
— اگر مطمئن نیستید
اگر مشکلی داشتید، از مسیر
Settings
←
Diagnostics
گزارش بگیرید و بفرستید.
@whitedns</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/whitedns/1687" target="_blank">📅 21:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1683">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نسخه جدید
🎯
WhiteVPN Desktop  منتشر شد -v1.0.20
این نسخه بیشترین تغییرات کاربری چند وقت اخیر را دارد.
سایت‌های ایرانی دیگر از تونل رد نمی‌شوند
بزرگ‌ترین درخواست شما بود: لازم نباشد برای باز کردن بانک یا سامانه‌های دولتی، وی‌پی‌ان را قطع کنید و بعد یادتان برود دوباره روشنش کنید.
مسیر: تنظیمات ← سایت‌هایی که از تونل رد نمی‌شوند
سایت‌های انتخابی مستقیم از خود دستگاه شما خارج می‌شوند. سریع‌تر باز می‌شوند، و آن‌هایی که آدرس خارجی را قبول نمی‌کنند درست کار می‌کنند.
▪️
فهرست از قبل پر است. اولین مورد، کل دامنهٔ کشوری ایران را یکجا می‌گیرد
▪️
دیجی‌کالا، آپارات، ورزش سه، دیوار، اسنپ و شاپرک هم در فهرست هستند
▪️
هر کدام را می‌توانید حذف کنید و هرچه خواستید اضافه کنید
▪️
محدودهٔ آی‌پی هم می‌شود اضافه کرد، مثلاً برای شبکهٔ محل کار
▪️
چسباندن آدرس کامل اشکالی ندارد و بخش‌های اضافه خودکار حذف می‌شوند
پیش‌فرض خاموش است. آپدیت نباید بدون انتخاب خودتان مسیر ترافیکتان را عوض کند، پس اول سوئیچ بالای همان صفحه را روشن کنید.
⚠️
هر چیزی که در این فهرست باشد با آدرس واقعی شما خارج می‌شود، دقیقاً مثل وقتی که وی‌پی‌ان خاموش است. هدف همین است، ولی یعنی هرچه نمی‌خواهید دیده شود جایش در این فهرست نیست.
🪟
یک پنجره، هرچند بار که کلیک کنید
تا حالا هر بار اجرای برنامه یک آیکون تازه در نوار وظیفه می‌ساخت. دو بار، سه بار، و هر کدام یک موتور جداگانه که سر پورت با بقیه درگیر می‌شد.
حالا اجرای دوباره فقط همان پنجرهٔ موجود را جلو می‌آورد. مخصوصاً وقتی پنجره را بسته‌اید و برنامه کنار ساعت است، که از بیرون شبیه خاموش بودن به نظر می‌رسد.
🐧
حالت تونل روی لینوکس
تا حالا فقط روی ویندوز کار می‌کرد. حالا روی لینوکس هم هست و رمز را از طریق پولکیت می‌پرسد. اگر پولکیت نصب نباشد، گزینه اصلاً نشان داده نمی‌شود، به‌جای اینکه باشد و همیشه شکست بخورد.
🎨
رنگ آیکون کنار ساعت
حالا وضعیت اتصال را از رنگ آیکون می‌فهمید، بدون باز کردن پنجره:
🟢
متصل
🟠
در حال اتصال
🔴
ناموفق
⚪️
قطع
🔌
پورت اشتراک‌گذاری روی شبکه
وقتی اتصال را با گوشی یا تلویزیون به اشتراک می‌گذارید، حالا پورت را خودتان تعیین می‌کنید. قبلاً اگر پورت اشغال بود، برنامه بی‌صدا پورت دیگری برمی‌داشت و دستگاهی که تنظیمش کرده بودید به جای خالی وصل می‌ماند.
هر دو پروتکل روی همان یک پورت کار می‌کنند.
🧪
تست همهٔ اشتراک‌ها در یک اجرا
دانلود
ویندوز، مک و لینوکس، همه از این نشانی:
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/whitedns/1683" target="_blank">📅 21:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1680">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/N09pOnABCMlV1WmpK8PKNNE4iAnjtQO6LVGx3IsGHu2HV7fM2eM2xCE9UXl3PqAZt2xye36Z0gm3Sp6SSUnp7El-1Hu7_4dfC_1gvy1k34hYTdK_w0t4hX0VePjPA8gXUntRhHU6RE4AVmrC9f26q-dxWxNZcstcheVJN9Ls4c0tSkr6cvaAtgeeaAUw67yYXGL0axh-T2JXP38aXj48NL0wLnPnSHngF_BR_aZiFYxp3PKGKhG8P0Q3hw0oBDzQ2RaryY4wB6e5oj3YedFarIkDaTsn8jQ8L3_BJqCRCj2bPWTMZMYoOv0MY2wnXCh1Lm4wHPEZswHK-QDom7EU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
نسخه جدید WhiteDNS Clean IP Finder منتشر شد.
🔭
تغییرات اصلی:
🟢
پشتیبانی بهتر از IPv6
🟢
انتخاب IPv4، IPv6 یا هر دو در ASN Scanner
🟢
بهبود حالت‌های Fast و Thorough در DNS Scan
🟢
بهبود DoH / DoT و مدیریت Timeout
🟢
گزارش‌دهی و مرتب‌سازی بهتر نتایج
🟢
بهبود Nearby Discovery برای IPv4 و IPv6
🟢
بهبود نسخه‌های Android و Desktop
🟢
بدون نیاز به تغییر تنظیمات نسخه‌های قبلی
📱
دانلود آخرین نسخه از گیتهاب
📱
تماشا آموزش اسکنر WhiteDNS Clean IP Scanner
⭐️
اگر پروژه براتون مفیده، توی GitHub استارش کنید.
@whitedns</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/whitedns/1680" target="_blank">📅 09:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1679">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f216f892a.mp4?token=J6K-UN-N72HzSDMkqGBdvSFljWFEQ6nAQ3xWSyNEg6lCCfSbxCaBs5UMvEPcXSV6HIRtEsCDlTyBWvE7-InIE_LcOsukciojEcpvm-8L4ttsrHuzVVkskH0U1yL8xpgAwidVem4ZvTdBFhsB15CUBk2GE97czbWDz0CFuooWnYl9YiNF3qj2RRL7Pk9ZhfmK7HR2ewBtj7oo8LjYI2T_MZem7QsGmcA2TBkGEaaWfb2me0tPrONarlfwuZHeaduJ6sCBZOIosxBQPfzCoamoO4LszU0uIRtoeV0V_BKOfeziSLDW-5jrLPfkvtL1mAFhFNtt3OdS2mWDsMFUbYwgWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f216f892a.mp4?token=J6K-UN-N72HzSDMkqGBdvSFljWFEQ6nAQ3xWSyNEg6lCCfSbxCaBs5UMvEPcXSV6HIRtEsCDlTyBWvE7-InIE_LcOsukciojEcpvm-8L4ttsrHuzVVkskH0U1yL8xpgAwidVem4ZvTdBFhsB15CUBk2GE97czbWDz0CFuooWnYl9YiNF3qj2RRL7Pk9ZhfmK7HR2ewBtj7oo8LjYI2T_MZem7QsGmcA2TBkGEaaWfb2me0tPrONarlfwuZHeaduJ6sCBZOIosxBQPfzCoamoO4LszU0uIRtoeV0V_BKOfeziSLDW-5jrLPfkvtL1mAFhFNtt3OdS2mWDsMFUbYwgWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
اگر برای باز کردن اپلیکیشن های
x.com
یا اپلیکیشن های AI مشکل دارید، میتونید از داخل WhiteVPN مسیر زیر رو طی کنید
تنطیمات > اتصال ها > یکپارچگی TLS
Settings > Connections > TLS Integrity</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/whitedns/1679" target="_blank">📅 09:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1676">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خرید و فروش کانفیگ در کل گروه های whitedns ممنوع است
⚠️
بلافاصله بدون اخطار = ban</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/whitedns/1676" target="_blank">📅 10:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1675">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">💬
ورژن جدید WhiteVPN  1.6.4 برای گوشی های اندرویدی
🔼</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/whitedns/1675" target="_blank">📅 09:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1670">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/whitedns/1670" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/whitedns/1670" target="_blank">📅 09:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1669">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ID7DEzCJnKaTlzcSO2QCKttsrs3Bwy34L9kMt35bCsqTjryPePHAJxFP8lz95LbjshQBz5OAA0G-_68eO8j1RecSfEQV1w-nGUFTVBRmsg8d7Z5l5WOMuoEfm89Gb116M0n4GIdq-isLdQEJf-uUF7fpCsywAfctuEhYHyUxX3Y1_1zrMjreMzdsPkxO3hLOx2vgKiNVUkSnh0CZSVU8uekCwfj10oHymIWivefV9lUw-GjirieNKcYlTwTwJa1cYzvU7nA7RqQZXEC4jVMkhlOukbbgHCwH05TvyHHUHrRrpNz31X6miJuLJq9Pl4eP-qWB5BhiWtVmCdKuOS1Q5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
ورژن جدید WhiteVPN  1.6.4 برای گوشی های اندرویدی
تغییرات در این نسخه:
🎯
اتصال و قطع اتصال پایدارتر. رفع مشکل قطع اتصال.
🔒
بهبود امنیت با رفع مشکل لیک با IP V6
🔭
افزودن کانفیگ با QR Code یا Clipboard
🎨
نمایش واضح‌تر وضعیت اتصال و بهبود ظاهر برنامه
📱
دانلود آخرین نسخه از گیتهاب
نکته:
⚠️
در صورت دانلود نشدن از گیت هاب مرورگر خود را به فایرفاکس تغییر دهید</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/whitedns/1669" target="_blank">📅 09:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1665">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BYnPZEL9minZ1_mpBgsdGepxJuUyv2Gd4CDfRKrd9F_vXrFoMcaj9y8wDMlomp-7TPRkl1gcDgaxfZQSWw00QgPRzmN5KfyNplBrmp5UkKPjqYs0ab1g8Ap8IWl66O-PRsR4dOYWnVOMs5Dcot1wnYwCLvUl4J3bTMFEXtxW_1mJ8OXTFw7ZVoeQs35m9wHRdiM_qeSoRPlnT_IY98CivOI9hQT5oh3s8aoYv4y6BPipRnU-PnIziGF9rUrojlaKPDOemDy40AGXYy4UwT7K0SPaXMJ8CLEaO0Pz-26Qx_HSBSuHzEb8URWoGrEkRrnJce7xXhADfrEGovriUrRy2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه رسمی و شفاف‌سازی مجموعه WhiteDNS
دسترسی به اینترنت آزاد، پایدار و امن حق طبیعی هر کاربر است. مجموعه
WhiteDNS
با هدف تحقق این هدف و تسهیل ارتباطات، خدمات و زیرساخت‌های خود را در اختیار عموم قرار داده است.
بدین‌وسیله رسماً اعلام می‌گردد:
۱۰۰٪ رایگان بدون هیچ قید و شرط:
تمامی خدمات، سرورها، کانفیگ‌ها، دی‌ان‌اس‌ها و آموزش‌های ارائه‌شده در چنل رسمی
WhiteDNS
کاملاً رایگان بوده و خواهد بود.
عدم وجود هرگونه اشتراک پولی (VIP):
این مجموعه هیچ‌گونه اکانت ویژه، پولی، پلن VIP، یا سرویس اختصاصی فروشی ندارد.
ممنوعیت کامل خرید و فروش:
هرگونه خرید، فروش، واسطه‌گری یا سوءاستفاده مالی از نام، کانفیگ‌ها یا سرورهای
WhiteDNS
غیرقانونی، غیرانسانی و نقض صریح قوانین این پروژه است.
هشدار نسبت به کلاهبرداری:
اگر فرد یا گروهی تحت عنوان ادمین، نماینده یا پشتیبان
WhiteDNS
به شما پیشنهاد خرید سرویس، اکانت یا پرداخت هزینه داد، سریعاً او را مسدود (بلاک) کرده و موضوع را گزارش دهید.
تنها مرجع رسمی:
کلیه اطلاع‌رسانی‌ها و به‌روزرسانی‌ها صرفاً از طریق کانال تلگرامی ما منتشر می‌شود:
🔗
کانال رسمی تلگرام:
https://t.me/whitedns
❤️
حمایت شما تنها از طریق معرفی کانال به دوستانتان و اشتراک‌گذاری اینترنت آزاد با دیگران و تماشای ویدیوهای ما در
کانال یوتیوب
و دادن
⭐️
به پست های ما و همچنین boost کردن کانال و حمایت از
گبت هاب
ما  امکان پذیر است
کلیه خدمات  WhiteDNS همواره رایگان در کنار شما می‌ماند.
@whitedns</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1665" target="_blank">📅 06:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1663">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔥
درود دوستان عزیز :
با توجه به رای گیری که شد و نظر دوستان عزیز
مقدار حجم روزانه کانفیگ های ربات به
4 گیگ
تغییر کرد
❤️
اگر از این خدمت استفبال شود احتمالا به زودی سرورهای بیشتر با لوکیشن های بیشتر در اختیار شما عزیران قرار خواهد گرفت که هر چه بیشتر امکان دسترسی رایگان شما فراهم شود .
بازم تاکید میکنیم که این کانفیگ ها فقط و فقط برای استفاده در قابلیت " exit chain " در برنامه های whiteaesther و whitevpn است . متاسفانه هنوز یک تعداد زیادی پیام دریافت میکنیم که دوستان میگن چرا این کانفیگ های توی v2rayng , hiddify و .......... کار نمیکنه
.
⚠️
لطفا تمام مطالب پست زیر را با دقت کامل بخونید
https://t.me/whitedns/1608
لازم به ذکر کرد در صورت مشاهده هر گونه سواستفاده از این کانفیگ ها لطفا به ادمین ها گزارش دهید
درصورتی که مشاهده شود که کانفیگ ها توسط افراد سودجو  در حال فروش به دیگران است این خدمت به طور کل حذف خواهد شد - پس خواهشمندیم خودتون در حفظ این امکان کوشا باشید
ربات :
@WhiteDnsChainbot
ارادتمند
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/whitedns/1663" target="_blank">📅 05:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1658">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-poll">
<h4>📊 محدودیت حجم کانفیگ ربات را از 1 گیگ به چقدر تغییر بدیم که برای انجام کارهای روزمره کافی باشه ؟👀</h4>
<ul>
<li>✓ 1.5</li>
<li>✓ 2</li>
<li>✓ 3</li>
<li>✓ 4</li>
<li>✓ همین خوبه☺️</li>
</ul>
</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/whitedns/1658" target="_blank">📅 13:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1656">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/JSdZuqXCSKGivc3w3V4Z4BIuuyhe3K_P0t70Eq0W6BjC3NuztYmQTx-uAb5rGrbKrO3glLsgzevMDnqU5XEXxwUvJ5KOcyUFHt89pWoJPCcoGdENoJQqed4VPEPQY2aXqw7PNDpJ-P0340fTdY8QVx1EWOyFxMdD4Xki7rBMFA9oB5APYMXyxVDjZKhpGnY37wbqW08sgC1kjsA-U4Er3pRDuOl99IyxnAqM59a7tsu5lbqRqeEfRDaVZIkMEg3ca-kiDYjqNOPVpyyeXgNqqsID35UL-VkuyUkZdYaDqjViOoNxRyzFep7Iz741lEX2J8fVwUN0Mqgv3ly_61PkwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#آموزش
اگر WhiteAesther mobile با یک بار زدن دکمه اتصال وصل نشد، یعنی هنوز باید تنظیمات درست شبکه خودت را پیدا کنی.
📡
این راهنمای کامل را قدم‌به‌قدم بخوان:
📖
https://github.com/WhiteDNS/WhiteAestherMobile/blob/main/docs/GUIDE.fa.md
@whitedns</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/whitedns/1656" target="_blank">📅 09:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1654">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/IEpT4L-mKhYFmfTgeDiNjMnytb78Gu3W4bnpZGQm5M4skfe0GWksTTe8Y-Jy9kaQJhhj1l3rBzaF4TX7AOOaiOMAnJIrCus5ckyT48eMQcZgsMTMWYSCpcNNwwdyCq24knMbvdzX2yRwNGyuJhQ2m47p8uu25kv361DZp4wVPiTx8p3m8yCSOovhKSzfLJVRpK6PZ806typ4K_RiSs3boXrmq8HceRh6z6rWG5TzjwAtFkj1Q3hXrAbuiCamhOlDB8R9ez32tAU8tz3fRNL-kmPA4xeoUAdtHpWzpoUhCodvHVvooY7VvQGmSsuS8ytxULRYjB1VMzOITuhI0SBwDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود دوستان عزیز
👋
چند تا کانفیگ جدید به ربات اضافه کردیم  که شاید بهتر بتونید متصل بشید و برای سرویس های خارجی مشکلات کمتری داشته باشید . کانفیگ ها تست شده است و مشکلی نداره
✅
از حالا به بعد شما میتونید تا
3 کانفیگ
را انتخاب کنید
😃
❤️
لطفا برای اطلاعات بیشتر حتما پست زیر را مطالعه کنید
⚠️
⚠️
https://t.me/whitedns/1608
Bot
🤖
:
@WhiteDnsChainbot
@whitedns</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1654" target="_blank">📅 05:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1653">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZcV5YrmZ2P4zkA24Bo_vqw6xtS4rmx7CCZzKLrqc7m4DaA7h6CD4bHG5PM8jAmz0M_Dp4SBhvHvscQAydLZ50DP_p6QuLRTqkhySM_VLWD48-WeQpU5rngrP0nt-_tp1YYJj0ySQwKofhS_1y4WKbzWwpWI_ANRAHv7ASx0UYl0uZmGz6NO87geSWxThlCExnFOAkp3GKbEsQI36wKcBTrW2wDLjjmO9PuQG_7KKekVSDMWh9fDqqWSI3oCdMfD5ui0jB3Z2qJEQkaT_ThOqBIHmhXBbqwPvvcwUUVYoZ4tb29n5YC1TB8GYrs30glZZOj6zWhB5xVoA8KtjjWsOjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
راهنمای کامل استفاده از ربات WhiteDnsChain
(کانفیگ هسته x-ray )
نکته : این ربات یک کانفیگ اضطراری برای شما ایجاد میکند تا در موارد خیلی خاص از ان استفاده کنید . کانفیگ های این ربات برای امکان exit chain در اپ های white ایجاد شده و هر گونه سواستفاده از آن مجاز نیست
🤖
آدرس ربات:
@WhiteDnsChainbot
برای دریافت و مدیریت اتصال اختصاصی خود مراحل زیر را انجام دهید:
1️⃣
شروع و انتخاب زبان
- وارد ربات شوید.
- دستور /start را ارسال کنید.
- گزینه «
🇮🇷
فارسی» را انتخاب کنید.
- برای تغییر زبان در آینده از گزینه «
🌐
تغییر زبان» استفاده کنید.
2️⃣
درخواست کانفیگ
- روی «
🔐
دریافت کانفیگ» بزنید یا دستور /config را ارسال کنید.
- درخواست شما برای مدیر فرستاده می‌شود.
- پس از تأیید، یک پیام اطلاع‌رسانی دریافت می‌کنید.
- دوباره /config را بزنید تا لینک اشتراک و QR اختصاصی شما نمایش داده شود.
3️⃣
اضافه‌کردن کانفیگ به برنامه
- یک برنامه سازگار با V2Ray/Xray روی دستگاه خود نصب کنید.
- لینک اشتراک را کپی کنید.
- در برنامه گزینه افزودن Subscription یا «افزودن اشتراک» را انتخاب کنید.
- لینک را وارد کرده و اشتراک را به‌روزرسانی کنید.
- یکی از سرورها را انتخاب کرده و اتصال را فعال کنید.
4️⃣
مشاهده وضعیت حساب
از گزینه «
👤
حساب من» یا دستور /account استفاده کنید تا موارد زیر را ببینید:
- وضعیت فعال یا غیرفعال
- تاریخ انقضا
- حجم مصرف‌شده
- حجم کل
- محدودیت تعداد دستگاه یا IP
5️⃣
دریافت دوباره کانفیگ
اگر پیام کانفیگ را پاک کردید، نگران نباشید. با /config همان کانفیگ اختصاصی دوباره نمایش داده می‌شود و کانفیگ جدیدی ساخته نخواهد شد.
6️⃣
پشتیبانی
- روی «
💬
پشتیبانی» بزنید یا /support را ارسال کنید.
- مشکل خود را در یک پیام کامل توضیح دهید.
- پیام مستقیماً برای مدیر ارسال می‌شود.
- پاسخ مدیر را داخل همین ربات دریافت خواهید کرد.
7️⃣
دستورات کاربردی
- /start — شروع و انتخاب زبان
- /config — دریافت کانفیگ
- /account — مشاهده وضعیت حساب
- /menu — نمایش منوی اصلی
- /support — ارتباط با پشتیبانی
- /help — نمایش راهنما
⚠️
نکات مهم
⚠️
-درخواست ها توسط ادمین دونه دونه بررسی و تایید میشود پس لطفا صبور باشید
- ادمین کاملا مختار است که به هر دلیل ممکن از ارایه کانفیگ به شما خودداری کند پس لطفا اعتراض نکنید
⚠️
-در حال حاظر کانفیگ ها با محدودیت 1 روزه و یک گیگ هست
- لینک و QR کاملاً اختصاصی است؛ آن را برای دیگران ارسال نکنید.
- هر حساب تلگرام فقط یک کانفیگ فعال دریافت می‌کند.
- ارسال چندباره /config کانفیگ تکراری ایجاد نمی‌کند.
- برای امنیت بیشتر، پس از دریافت کانفیگ می‌توانید پیام آن را با گزینه «
🗑
مخفی کردن» حذف کنید.
- در صورت پایان حجم یا اعتبار، از طریق پشتیبانی با مدیر ارتباط بگیرید.
@whitedns</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/whitedns/1653" target="_blank">📅 05:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1652">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/D5Fo8UFReF3Nec8DPcvWTiWiYAEr7oN_4CgW-zSvVKGeuz6DnK_7LvcyaBuIETbx9q1D1ERVtukMPUHz2t_qmVRhPZhrCus77DLtTTHwBUDE3uPWXK7Y4-EXwQYi25PWKMBMejRC8L5guPNP5muIE6wOaf7JIr9jV9N9-HYxg4hlS20ce8AiczhxjrdUBbgzDS0GO3kvdb_Zw1sW8p2sivK_x7EorPy9NCqbqaGRJru9mWrkIsZaNhFMstJXXvX54EffciIg8p12VoScuVIbN0KPHFHRfoUdMdRsbZ65ThtpSlvCkGKOlv8sPyEY9gt62O7TW9pq_Me9LAfLsHNnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/whitedns/1652" target="_blank">📅 05:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1651">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/JvIdY6VGaOlhgdbsvvRdSaF2_h3QZarVSe7pbIHh0Hx4fQMc-hWE2DB4jKb6p2dLB3-BgPtYrpEnZ4aLzMl9A0TVzQnYHQvUbEG5yAm-8AN4IyJVZwABeaavlfnKk-cvH8altIKNZ5tK3QQf-H8mK3BoWzTfpCHsAfR8BLVZEgrpOSFjE1XjFLtTNkDYMWMrEYeFa-5OlSCRtfPif2mtZzKi7COZd9ZXqxDZyQpfTWgtH0GflM1VhdLjISjJcGQz71nHXHcALrFGi8PmxA88qG8TY9RV7J4ftkSeg_Q3ottuyP54LfrVmD1lhJOmidrvLrcitukDQlPAmXDm6_TflQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
آپدیت WhiteAesther — نسخه 1.2.5
🔥
⚠️
⚠️
⚠️
در این ورژن رفع باگ Android TV انجام شده است و دوستانی که روی گوشی استفاده میکنند لازم نیست اپدیت کنند
⚠️
⚠️
⚠️
مشکل کنترل با ریموت در Android TV برطرف شد. پیش از این، بعد از رسیدن به بخش «Connected for»، امکان حرکت به قسمت‌های پایین‌تر صفحه وجود نداشت.
حالا با دکمه‌های بالا و پایین کنترلر می‌توانید به‌راحتی بین تمام بخش‌های صفحه Home حرکت کنید و اطلاعاتی مثل آدرس، ترافیک مصرفی و جزئیات اتصال را ببینید.
این تغییر فقط مربوط به حالت Android TV است و عملکرد نسخه موبایل تغییری نکرده.
🔗
دانلود رسمی از گیت هاب
@whitedns</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/whitedns/1651" target="_blank">📅 16:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1650">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEPw6-0f-tnoqbN03DA2Tnzq07BDEnfCIW9Cury1eLoUuVbZbBw_iSdzfqZiV669L-XfhefYfK3epgsp75trVRmsOMICxUPwwxWP4yzPXI-y5q7lNQWIP8_syVkRHh5GBnc_wE130cZSeboxEX-MJF-8x-_GuZa0IQGbZKZE-7BI-7aZM7ZfwTwe-Ug5q4-Q2zWQa68UPCUNizMbC4bUy4cZju36RK96x12KfGjY_ihfUqAVGJAwVOmHQ1ecXT6g5reysd0aXNsdbWOseVYeLUvyOixUL_a0oGRH8AhK1D_SWlBEIpIz3_qBs6Ani_T1Z8PkyYCKXc2Dfa_RhzSBTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
نسخه Android TV و Google TV برنامه WhiteAesther منتشر شد
از نسخه v1.2.4 به بعد می‌توانید WhiteAesther را روی تلویزیون، TV Box و دستگاه‌های Google TV فقط با ریموت یا دستهٔ بازی کنترل کنید؛ بدون نیاز به صفحهٔ لمسی.
حداقل نسخه موردنیاز: Android 8
🔗
دانلود رسمی از گیتهاب
⚠️
برنامه را فقط از لینک رسمی بالا دانلود کنید.
🦢
🦢
🦢
🦢
🦢
🦢
📥
کدام فایل WhiteAesther را برای تلویزیون دانلود کنیم؟
برای بیشتر تلویزیون‌ها و TV Boxهای جدید:
"WhiteAestherMobile-1.2.4-arm64-v8a.apk"
اگر مدل پردازنده را نمی‌دانید یا فایل بالا نصب نشد:
"WhiteAestherMobile-1.2.4-universal.apk"
نسخه Universal روی دستگاه‌های بیشتری اجرا می‌شود، اما حجم بیشتری دارد.
گزینه‌های دیگر:
• نسخه "armeabi-v7a": مخصوص دستگاه‌های قدیمی ۳۲ بیتی
• نسخه "x86_64": بیشتر برای شبیه‌سازها و بعضی دستگاه‌های خاص
• فایل "AAB": برای نصب مستقیم مناسب نیست
🦢
🦢
🦢
🦢
🦢
🦢
🛠
نصب WhiteAesther مستقیماً روی Android TV
۱. مرورگر تلویزیون یا برنامه‌ای مثل Downloader را باز کنید.
۲. وارد صفحه رسمی انتشار شوید.
۳. فایل APK مناسب دستگاه را دانلود کنید.
۴. فایل را باز کرده و Install را بزنید.
اگر اجازه نصب داده نشد، گزینه Install unknown apps را برای مرورگر یا Downloader فعال کنید.
این تنظیم معمولاً در یکی از مسیرهای زیر قرار دارد:
Settings → Apps → Special app access → Install unknown apps
یا:
Settings → Security → Unknown sources
بعد از نصب، بهتر است این دسترسی را دوباره غیرفعال کنید.
🔗
دانلود نسخه رسمی از گیتهاب</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/whitedns/1650" target="_blank">📅 10:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1649">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnNrLV7zmcXxz6apTSEB7--BodrwXV5ZTMYu3xdPn3eEDhnbpITvc06hnZHiHmHYoVc3ipokMAiMGE1JzWeZHnsQYr6HkdUT00RF2hJIRI9lfD0t22uDs0Up_KOUaUpIhFEOJhWvJaZD3hyApc4DpQka1Jn9GqfVppuAKEWNNxVL0jIvluga_wvk1QRF_L50ZcxZ0R-aVZqhaYURAkkClkprvzEbndEKi5bQ-DEVlRBWmQAKZvHSJANUVTITvYrVlAQwS6tjFZErEvaF5ge7DBoHRnXFkACCFC_P9SQNtWxk-AEl3JEQJeoTniR_Lauy0bjc81dWxK5y9pEkNAf17A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
داریم تست های نهایی رو برای WhiteAesther روی AndroidTV  انجام میدی
م</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1649" target="_blank">📅 19:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1645">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/QFR90Ufsw2tdyVDYBJ-saDa5e-AcIDcIfrpbzaHmhanNT4vXRe3_SKgdpCWEC-XR1drRHXYmWkvKQ6xXKex9HJU3Iw_taHXyoWGHEQI5KrMthDpoFqgqY22GE88dV2KEb0PuFa7kDJ4dSvHWetn8tJ4uMWQSJzuK64gLtjA1zXUom7f4m39WJStqAw6jU_8RnQOtl4VMu78gi-pT97mvRD-cm879N84KSfy4AtZD_VTkWmjKjChZLfNAc9HyOyBCdVFGvrimAaNQOsIqOYfgKhWu9EGH4XuOgnV9WC8PhztdOeHEosB3CKNxT1k3hR_pf08ymO_XKgJC1zazn2gj9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/hoRnR9goGH7Rl6B7qsNCAIIZYEDfhBPVz4cEaHR3urMHIdZ_wnofsJVbi5ITuEZi7E7rZRqRxv2y2s3hJJUUhVNnBU3nXLHaV2E8jBcTLTWt92wPMK6XRxIY-PRzQFidQu6hiCm5hW1McRrcYB8CRX3HvyU-VcUgT67WXu1ubYKbab6sYeMflTL8eUZO6LflZnZeqHQAwTx8gQHX5aMePP9ivgmBEKeUahoxa2DeobttsY8mB4DcSnzx8gZ9D36oHZRQGtAw_LglcefnJbA3_5ZSWz4L5wjsbKvUqyLZyMzcJxXlc5gLpBXgP4fQmE_WcN8TNQhwAi9ZppKdzAK19w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/iMNnwfnokfbsGfAGCto-HBxyBDkMvDZhepuakeF6t3tX7cIfDW5bQ4O5oIVwTZpH2l6XZsVag2KUT2WSJP1r_tpvf9mKMegfD8-vZJ2GTTPvYC6JGvB_BpAnzDgHCGJs65WagzwkdRSpd-OT_0nZ9C6ykexYijEYiycVmuwsH8OFMHVA22L-ZNf5s1waTnzNrpEWA-9m0svplmKIk652r_g4C-a9Y2CXxIwtbvwu4BrGX-_THpG_F13MR72oykYUelEJznDUGnhFT3DmhlBjyEBXUqshxaHY46B8PppdTfaQUwLK7gy8i7UdtByXmi5rk3wlWFXM650mSFfMK8wEJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راهنمای زنجیر کردن  Psiphon Desktop
با
whiteaesther
Desktop
🔥
🔥
اول Psiphon را وصل کنید.
در تنظیمات Psiphon proxy محلی را پیدا کنید. و یکی از پورت های زیر را وارد کنید . توصیه میشود از ساکس استفاده کنید
SOCKS5:1080
HTTP:8080
WhiteAesther را باز کنید.
بروید به:
Advanced
→
Routes & transports
→
Anti-blocking
در فیلد
Dial through a local proxy
یکی از این‌ها را وارد کنید:
socks5://127.0.0.1:1080
یا:
http://127.0.0.1:8080
بعد
Save profile
را بزنید.
حالا Connect کنید. مسیر  می‌شود:
App traffic -> WhiteAesther local SOCKS -> Aether/WARP -> Psiphon local upstream -> Internet
اگر میخواهید که whiteaesther سیستم شما را تانل کند روی Full tunnel و اگر نه از پراکسی whiteaesther برای نرم افزارهای خاص خودتون استفاده کنید
نکته : قابلیت exit chain را توی تنظیمات خاموش کنید
⚠️
⚠️
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/whitedns/1645" target="_blank">📅 15:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1644">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG/PattN کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  پروژه های خوبی وجود دارند که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/whitedns/1644" target="_blank">📅 06:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1641">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مطالب اموزشی نسخه 1.6.0 دسکتاپ whiteaesther
🔥
🔥
خلاصه :
🔧
تغییرات و قابلیت‌های جدید
▫️
حالت
Full Tunnel
یک کارت شبکهٔ مجازی ایجاد می‌کند تا تمام ترافیک سیستم از تونل عبور کند؛ حتی برنامه‌هایی که تنظیمات Proxy را نادیده می‌گیرند.
▫️
خروج سایت‌های ایرانی از تونل
شامل ۲۹۰۶ رنج IP و ۴۱٬۷۲۹ دامنه ایرانی است که مستقیماً داخل خود برنامه قرار گرفته‌اند و نیازی به دانلود جداگانه ندارند.
▫️
دریافت خودکار دسترسی Administrator
هر زمان دسترسی ادمین لازم باشد، برنامه خودش پیام تأیید ویندوز را نمایش می‌دهد و با سطح دسترسی لازم دوباره اجرا می‌شود. دیگر نیازی به راست‌کلیک و انتخاب
Run as administrator
نیست.
▫️
اطلاع‌رسانی نسخه‌های جدید
در صورت انتشار نسخه جدید، یک نوار اطلاع‌رسانی بالای برنامه ظاهر می‌شود که با یک کلیک شما را به صفحه دانلود می‌برد.
▫️
چهار تنظیم جدید موتور
تنظیمات بیشتری برای موارد زیر اضافه شده است:
Local Proxy
Domain Sniffing
Identity Re-registration
Keepalive
مقدار پیش‌فرض
Keepalive
نیز از ۵ ثانیه به ۲۵ ثانیه تغییر کرده است.
▫️
عبور مستقیم ترافیک شبکه محلی
ترافیک دستگاه‌های داخل شبکه مثل Printer، Router و NAS دیگر به نود خروجی فرستاده نمی‌شود و مستقیماً در شبکه محلی باقی می‌ماند.
▫️
رفع مشکل آیکون‌های مرده در Taskbar
حالا در تمام حالت‌های خروج از برنامه، آیکون آن به‌درستی از Taskbar و System Tray حذف می‌شود.
▫️
حذف اتصال خودکار
برنامه دیگر بدون اجازه کاربر به‌صورت خودکار متصل نمی‌شود. زمان اتصال کاملاً در اختیار شماست.
▫️
باز شدن صحیح پنجره با کلیک روی آیکون برنامه
مشکلی که در حالت اجرای برنامه با دسترسی Administrator باعث می‌شد ویندوز فرمان باز شدن پنجره را مسدود کند، برطرف شده است.
🛡
۱. حالت Full Tunnel — جلوگیری کامل از DNS Leak
تا الان دو حالت داشتیم:
▫️
فقط همین برنامه
▫️
کل دستگاه
مشکل حالت دوم این بود که فقط برنامه‌هایی را پوشش می‌داد که از تنظیمات Proxy ویندوز استفاده می‌کنند.
خیلی از برنامه‌ها این تنظیمات را نادیده می‌گیرند و مستقیماً به اینترنت یا DNS وصل می‌شوند. در نتیجه ممکن بود بخشی از ترافیک خارج از تونل عبور کند.
حالت جدید
Full Tunnel
یک کارت شبکه مجازی ایجاد می‌کند و
تمام ترافیک سیستم
را از تونل عبور می‌دهد؛ حتی برنامه‌هایی که Proxy سیستم را نادیده می‌گیرند.
این حالت بهترین گزینه برای جلوگیری از DNS Leak است.
🔹
روش فعال‌سازی
۱. برنامه را باز کنید و متصل شوید.
۲. پایین صفحه اصلی سه حالت وجود دارد.
۳. گزینه سوم یعنی Full Tunnel را انتخاب کنید.
۴. ویندوز برای دسترسی لازم از شما اجازه می‌خواهد. گزینه Yes را بزنید.
۵. برنامه به‌صورت خودکار بسته و دوباره با دسترسی لازم اجرا می‌شود.
دیگر لازم نیست روی برنامه راست‌کلیک کرده و Run as administrator را انتخاب کنید.
✅
برای تست
بعد از اتصال، سایت زیر را باز کنید:
dnsleaktest.com
سپس گزینه Extended Test را اجرا کنید.
سرورهای نمایش‌داده‌شده باید مربوط به کشور نودی باشند که به آن متصل شده‌اید.
━━━━━━━━━━━━━━━━━━
🇮🇷
۲. خروج خودکار سایت‌های ایرانی از تونل
دیگر لازم نیست برای باز کردن بانک‌ها، دیجی‌کالا، آپارات و سرویس‌های داخلی، هر بار VPN را خاموش کنید.
سایت‌های داخلی معمولاً نیازی به عبور از تونل ندارند. عبور آنها از تونل فقط می‌تواند سرعت را کاهش دهد و پهنای باند نود را مصرف کند.
حالا می‌توانید کاری کنید که:
سایت‌های ایرانی مستقیم باز شوند و بقیه ترافیک از تونل عبور کند.
🔹
روش فعال‌سازی
به مسیر زیر بروید:
Advanced → Traffic & DNS → Routing Rules
سپس گزینه زیر را روشن کنید:
Iranian sites bypass the tunnel
لیست موردنیاز داخل خود برنامه قرار دارد و شامل:
▫️
۲۹۰۶ رنج IP ایران
▫️
۴۱٬۷۲۹ دامنه
است.
هیچ فایلی هنگام اتصال دانلود نمی‌شود؛ بنابراین این قابلیت حتی زمانی که دسترسی آزاد به اینترنت ندارید نیز قابل استفاده است.
━━━━━━━━━━━━━━━━━━
📱
۳. اشتراک اینترنت با گوشی، تلویزیون و دستگاه‌های دیگر
حالا می‌توانید کامپیوتر خود را به یک Proxy Server تبدیل کنید و دستگاه‌های دیگر را از طریق آن به اینترنت متصل کنید.
بدون نیاز به نصب WhiteAesther روی گوشی.
🔹
روش فعال‌سازی
به مسیر زیر بروید:
Advanced → Traffic & DNS
در بخش:
Share with other devices
گزینه اشتراک‌گذاری را روشن کنید.
برنامه یک آدرس مشابه این نمایش می‌دهد:
192.168.1.24:1080
بار اول ویندوز ممکن است از شما اجازه Firewall بخواهد.
گزینه:
Allow access
را انتخاب کنید.
اگر اجازه ندهید، Proxy فقط روی همان کامپیوتر قابل استفاده خواهد بود.
📱
در Android
وارد تنظیمات Wi-Fi شوید.
شبکه متصل را باز کنید و به بخش تنظیمات Proxy بروید.
حالت Proxy را روی Manual قرار دهید.
برای مثال:
Hostname:
192.168.1.24
Port: 1080
همان IP و پورتی را وارد کنید که WhiteAesther نمایش داده است.
🍎
در iPhone
به مسیر زیر بروید:
Settings → Wi-Fi
روی علامت (i) کنار شبکه بزنید.
سپس:
Configure Proxy → Manual
را انتخاب کرده و IP و Port نمایش‌داده‌شده در WhiteAesther را وارد کنید.
🔐
نکته امنیتی مهم
اگر Username و Password تعیین نکنید،
هر دستگاهی که به همان شبکه Wi-Fi متصل باشد می‌تواند از Proxy شما استفاده کند.
در شبکه خانگی شاید این موضوع مهم نباشد، اما در محل کار، دانشگاه، هتل یا کافه حتماً هر دو فیلد زیر را پر کنید:
Username
Password
خود برنامه نیز در صورت خالی بودن آنها با یک هشدار زرد به شما اطلاع می‌دهد.
یک Port برای هر دو پروتکل استفاده می‌شود:
HTTP
و
SOCKS5
بنابراین همان شماره Port را برای هرکدام که دستگاه شما پشتیبانی می‌کند وارد کنید.
━━━━━━━━━━━━━━━━━━
⚡️
۴. پشتیبانی بهتر از Hysteria2 و TUIC
اگر در Subscription شما نودهای Hysteria2 وجود داشتند و همیشه علامت — نمایش داده می‌شد، این مشکل اکنون برطرف شده است.
مشکل از اندازه Packet بود.
این پروتکل‌ها Packetهایی با اندازه حدود ۱۲۸۰ بایت ارسال می‌کنند، در حالی که تونل قبلی فقط ۱۲۵۲ بایت ظرفیت داشت.
در نتیجه حدود
۲۸ بایت کمبود ظرفیت
باعث می‌شد Packet قبل از ارسال حذف شود.
🔹
روش استفاده
به مسیر زیر بروید:
Advanced → Routes & Transports
سپس Protocol را روی:
WireGuard
قرار دهید.
برای این نودها از MASQUE استفاده نکنید.
در حالت MASQUE این محدودیت از سمت Cloudflare وجود دارد و برنامه نیز کنار نود توضیح می‌دهد که چرا قابل استفاده نیست.
━━━━━━━━━━━━━━━━━━
🔔
۵. اطلاع‌رسانی نسخه‌های جدید
از این نسخه به بعد، وقتی نسخه جدید WhiteAesther منتشر شود، خود برنامه به شما اطلاع می‌دهد.
یک نوار اطلاع‌رسانی در بالای برنامه نمایش داده می‌شود.
با زدن گزینه:
Get it
مستقیماً وارد صفحه دانلود نسخه جدید خواهید شد.
━━━━━━━━━━━━━━━━━━
🔧
سایر تغییرات
▫️
نودهای REALITY حالا با برچسب Not Supported مشخص می‌شوند.
موتور فعلی از آنها پشتیبانی نمی‌کند، بنابراین بهتر است وضعیت آنها واضح باشد تا اینکه نودی نمایش داده شود که هیچ‌وقت متصل نمی‌شود.
▫️
Subscriptionها کامل‌تر پردازش می‌شوند و مشکل جا افتادن بعضی نودها برطرف شده است.
▫️
مشکل باقی ماندن آیکون‌های قدیمی برنامه در Taskbar برطرف شده است.
▫️
برنامه دیگر به‌صورت خودکار متصل نمی‌شود. تصمیم برای اتصال کاملاً با کاربر است.
▫️
تنظیمات بیشتری برای Local Proxy، Keepalive و گزینه‌های پیشرفته اضافه شده است.
▫️
موتور برنامه به نسخه زیر ارتقا پیدا کرده است:
Aether 1.7.0
@WhiteDNS_Laurie</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/1641" target="_blank">📅 05:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1640">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CowXdm3H3Imt9ad1_Y5MeVRKQ9Pks_lhg7OLe1elQKBmyC06PHA7blpylhcnC_uaU010Ttd294KVFE1dQCJ7JFXjaAigO-1s08L-q78fwMCNIVIngfTWeBFMiiARTttrPVprEF1LOpyVBZwU2ES9eP8IhIpP4GXssEhAcKqZEWrOVXZVsr7lA7gvScPdllmir4rb-AJkvMXGQ-9xGFkml1HIT_-U8wegeOTkNZX_oxqWKMVQwF8htIXNe-LikCjDDNcF_LcEYG9jVWlcEoVxYWdPZTRzEr3eQwSCMYRBZMFcpfRCJ0xieaAd6XnCvgzHZTt1jnnOBCj4edWiXgunaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه 1.6.0 دسکتاپ  WhiteAesther منتشر شد
بزرگ‌ترین آپدیت WhiteAesther تا امروز.
حالا می‌توانید:
▫️
کل کامپیوتر را تونل کنید
▫️
سایت‌های ایرانی را از تونل خارج نگه دارید
▫️
اینترنت را با گوشی، تلویزیون و دستگاه‌های دیگر به اشتراک بگذارید
━━━━━━━━━━━━━━━━━
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases
نسخه‌های موجود:
▫️
Windows
▫️
Linux —
deb / rpm / AppImage
▫️
macOS Intel
▫️
macOS Apple Silicon
━━━━━━━━━━━━━━━━━━
⚠️
نکته مهم قبل از تست
اگر برنامه رسمی
Cloudflare WARP
روی سیستم شما نصب است، قبل از استفاده از WhiteAesther حتماً آن را کاملاً
Disconnect
کنید.
اجرای همزمان دو VPN روی مسیر شبکه می‌تواند باعث تداخل، قطع اتصال یا نتایج گیج‌کننده شود.
━━━━━━━━━━━━━━━━━━
💬
اگر سؤال یا مشکلی داشتید، همین‌جا مطرح کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/whitedns/1640" target="_blank">📅 05:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1636">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-text">آموزش تغییر لوکیشن با Exit Chain
داخل اپ‌های WhiteVPN و WhiteAesther
🔥
واسه gemini و بقیه AI هایی ک نیاز دارین عالیه
https://youtu.be/yx-jFqv9pYM?si=VuY0qqm5qbFUJOO6</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/whitedns/1636" target="_blank">📅 03:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1634">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔗
نسخه ۱.۲.۳ اندروید WhiteAesther منتشر
شد ......!
در نسخه جدید سه بخش مهم اضافه شده:
🛡
قفل ایمنی
🧭
قواعد مسیریابی
⚙️
چند تنظیم جدید برای موتور اتصال
پایین، همه موارد را همراه با آموزش توضیح داده‌ایم.
🛡
۱. قفل ایمنی — Kill Switch
چه مشکلی را حل می‌کند؟
تا الان اگر تونل بعد از چند بار تلاش وصل نمی‌شد، برنامه تسلیم می‌شد و گوشی بی‌صدا به اینترنت معمولی برمی‌گشت.
حالا می‌توانید مشخص کنید که در چنین شرایطی، به‌جای برگشت به اینترنت عادی،
تمام ترافیک اینترنت مسدود شود.
آموزش
۱) وارد بخش Traffic شوید.
۲) بخش Advanced را باز کنید.
۳) گزینه زیر را روشن کنید:
Block traffic if the tunnel fails
تمام! از این به بعد اگر تونل از کار بیفتد، هیچ ترافیکی از گوشی خارج نمی‌شود.
🔸
حالت سخت‌گیرانه‌تر
بعد از فعال کردن گزینه بالا، گزینه دیگری ظاهر می‌شود:
Keep blocking after you disconnect
اگر این گزینه را روشن کنید،
حتی زمانی که خودتان اتصال را دستی قطع می‌کنید، اینترنت همچنان مسدود می‌ماند
تا خودتان آن را آزاد کنید.
⚠️
توجه:
در این حالت گوشی واقعاً اینترنت نخواهد داشت. اگر فراموش کنید این گزینه فعال است، ممکن است فکر کنید اینترنت یا شبکه مشکل دارد.
برای برداشتن قفل دو راه دارید:
▫️
از نوتیفیکیشن Traffic is blocked
▫️
یا از صفحه اصلی برنامه و دکمه Lift the block
اگر دوباره به تونل متصل شوید، قفل به‌صورت خودکار برداشته می‌شود.
🧭
۲. قواعد مسیریابی — Routing Rules
چه مشکلی را حل می‌کند؟
بعضی سایت‌ها و اپلیکیشن‌ها با IP خارجی درست کار نمی‌کنند؛ مثل بعضی بانک‌ها، اپ‌های داخلی یا سرویس‌های ایرانی.
قبلاً برای استفاده از آنها مجبور بودید VPN را کاملاً خاموش کنید.
حالا می‌توانید مشخص کنید که
فقط بعضی سایت‌ها یا سرویس‌ها از تونل عبور نکنند
و بقیه ترافیک همچنان از تونل استفاده کند.
آموزش
۱) وارد بخش Routes شوید.
۲) در کارت اول، گزینه Routing rules را که زیر Exit chain قرار دارد انتخاب کنید.
۳) دو کادر خواهید دید:
🔹
کادر
Never connect
هر چیزی که اینجا قرار بگیرد، اصلاً اجازه اتصال نخواهد داشت.
مناسب برای مسدود کردن تبلیغات، ردیاب‌ها و دامنه‌های ناخواسته.
🔹
کادر
Skip the tunnel
هر چیزی که اینجا قرار بگیرد،
بدون تونل و با IP واقعی شما
باز می‌شود.
مناسب برای بانک‌ها، سایت‌ها و اپلیکیشن‌های داخلی.
هر قانون را در یک خط جداگانه بنویسید.
مثال:
bank.example.ir
digikala.com
snapp.ir
نوشتن یک دامنه، زیرمجموعه‌های آن را هم شامل می‌شود.
برای مثال:
digikala.com
شامل این مورد هم خواهد شد:
www.digikala.com
حالت‌های پیشرفته
▫️
فقط همان دامنه دقیق:
full:
example.com
▫️
هر آدرسی که یک کلمه خاص داخل آن باشد:
keyword:tracker
▫️
یک محدوده IP:
cidr:
10.0.0.0/8
▫️
یک پورت مشخص:
port:25
▫️
کل شبکه محلی:
private
▫️
هر خطی که با # شروع شود، به‌عنوان توضیح در نظر گرفته شده و اجرا نمی‌شود.
⚠️
مهم:
هر چیزی که داخل Skip the tunnel قرار دهید، با
IP واقعی شما
به اینترنت متصل می‌شود. بنابراین این لیست را فقط برای موارد ضروری استفاده کنید.
🔸
نکته مهم درباره دامنه‌ها
در مسیر زیر:
Traffic ← Advanced
گزینه‌ای وجود دارد با نام:
Match rules on domain names
این گزینه به‌صورت پیش‌فرض روشن است و بهتر است روشن بماند.
اگر آن را خاموش کنید، قوانینی که با نام دامنه نوشته شده‌اند ممکن است کار نکنند؛ چون برنامه در اندروید معمولاً ترافیک را در سطح IP دریافت می‌کند.
در صورت خاموش بودن این گزینه، خود صفحه Routing rules نیز هشدار خواهد داد.
⚙️
۳. تنظیمات جدید موتور
تمام این تنظیمات در مسیر زیر قرار دارند:
Traffic ← Advanced
🔹
تنظیم DNS داخل تونل
گزینه:
DNS inside the tunnel
می‌توانید DNS دلخواه خودتان را وارد کنید.
مثال:
8.8.8.8
,
1.1.1.1
اگر خالی بگذارید، DNS پیش‌فرض موتور استفاده می‌شود.
آدرس‌های نامعتبر نیز به‌صورت خودکار نادیده گرفته می‌شوند.
🔹
اتصال تونل از طریق یک پروکسی دیگر
گزینه:
Dial out through a proxy
این قابلیت یکی از مواردی بود که کاربران زیادی درخواست کرده بودند.
اگر ابزار دیگری روی گوشی شما در حالت پروکسی فعال است، مثلاً
Psiphon
، می‌توانید اتصال WhiteAesther را از داخل آن عبور دهید.
مسیر اتصال به این شکل می‌شود:
گوشی ← WhiteAesther ← Psiphon ← اینترنت
برای مثال اگر پروکسی SOCKS روی پورت ۱۰۸۰ فعال باشد، وارد کنید:
socks5://127.0.0.1:1080
پورت را باید با پورت واقعی برنامه پروکسی خودتان جایگزین کنید.
پروکسی HTTP نیز پشتیبانی می‌شود:
http://127.0.0.1:8080
🔹
تنظیم WireGuard Keepalive
این گزینه می‌تواند روی مصرف باتری تأثیر داشته باشد.
سه مقدار قابل انتخاب است:
▫️
۵ ثانیه
▫️
۱۵ ثانیه
▫️
۲۵ ثانیه
مقدار پیش‌فرض در نسخه جدید
۲۵ ثانیه
است. در نسخه‌های قبلی مقدار پیش‌فرض ۵ ثانیه بود.
هر بار که این زمان می‌گذرد، گوشی یک بسته کوچک ارسال می‌کند تا اتصال فعال بماند.
در حالت ۵ ثانیه، این کار بسیار بیشتر انجام می‌شود و مخصوصاً روی اینترنت موبایل می‌تواند باعث مصرف بیشتر باتری شود.
مقدار ۲۵ ثانیه نیز مقدار رایج استاندارد WireGuard است.
⚠️
اگر بعد از آپدیت متوجه شدید اتصال WireGuard بعد از چند دقیقه بی‌کاری قطع می‌شود، مقدار را دوباره روی
۵ ثانیه
قرار دهید.
🔹
جایگزینی هویت ردشده
گزینه:
Replace a refused identity
این گزینه به‌صورت پیش‌فرض روشن است.
اگر Cloudflare هویت ذخیره‌شده روی گوشی را دیگر قبول نکند، برنامه به‌صورت خودکار یک هویت جدید دریافت می‌کند.
بدون این قابلیت ممکن است تونل ظاهراً متصل شود، اما هیچ ترافیکی از آن عبور نکند.
📌
خلاصه محل تنظیمات
بخش
Routes
▫️
Protocol
— مثل قبل
▫️
Endpoint
— مثل قبل
▫️
Exit chain
— مثل قبل
▫️
Routing rules
—
جدید
بخش
Traffic ← Advanced
▫️
Obfuscation
— مثل قبل
▫️
Local proxy port
— مثل قبل
▫️
Share with this network
— مثل قبل
▫️
DNS inside the tunnel
—
جدید
▫️
Dial out through a proxy
—
جدید
▫️
WireGuard keepalive
—
جدید
▫️
Block traffic if the tunnel fails
—
جدید
▫️
Match rules on domain names
—
جدید
▫️
Replace a refused identity
—
جدید
⬇️
دانلود آخرین نسخه
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
▫️
arm64-v8a
— مناسب تقریباً همه گوشی‌های سال ۲۰۱۷ به بعد؛
اول این نسخه را امتحان کنید.
▫️
armeabi-v7a
— مخصوص گوشی‌های قدیمی‌تر
▫️
universal
— اگر مطمئن نیستید؛ حجم این نسخه تقریباً سه برابر است.
اگر با مشکلی مواجه شدید، از مسیر زیر گزارش بگیرید:
Settings ← Diagnostics
و برای ما ارسال کنید.
@whitedns</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/1634" target="_blank">📅 19:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1632">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RCXmLbY9q3eRH6kK_lyFVOoiOxxtDNy1skRih66vvCST2819mKOx-LCkkkIP-ss50tZRy3RT-8UXWn-ssYmcQXC-4_hUKpz1XDEjvXsSU4GTX7xIIwR7NQoqw2l2un8pxR6wVFHD5bkEkqhaFqedA2796SU3Dwi-y8Z_diltQMeOZlyTrPanMEZWkYRtvMgzlzXa6Fvt9ppWO2r3a6ISyWpDyQESQKDldsHp0eNW6xUkNVlnjn4EEkUlzMw0rNOLz5TbfUzY4EpZk-3JSlJphmLpp4lQ53xvcfRJtpu4brsWZK59oqzTggP8DnBuAs3g6ma5ttFKt2aVgfOCpzyjYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔜
به‌زودی:  WhiteAesther  اندروید نسخه ۱.۲.۳
🔥
🔥
🔥
▫️
قفل ایمنی (Kill switch) — اگه تونل بمیره، ترافیک بی‌صدا لو نمی‌ره
▫️
قواعد مسیریابی — بگین کدوم سایت‌ها بدون تونل باز بشن (بانک، اپ‌های داخلی)
▫️
اتصال یه پروکسی دیگه (مثل سایفون)
▫️
امکان DNS دلخواه داخل تونل (برای کاهش پینگ)
▫️
بهینه‌سازی مصرف باتری روی WireGuard
@whitedns</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/whitedns/1632" target="_blank">📅 16:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1631">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/p1Lnrd5FbDeI1nddNBJeBK5oLrk73_6FL0uU6EjRIEpsOVsxtz1f2GLWOY6-xat3vw84_NMvb1P_l8_yY7e-IbjJZf6nUMLK80UpL3Iw4-JS5wC-tn-Yd5f_Di_D45oCtBJWiSFsOmICstQTw1uarys_2zfBrKnv09aczGOUUFj_oGBM83WKvddfMLvblwP70zJYcama6V5eANghznibnvvlqIcXDymySQDHKN_EN5i0dmKnMBljWPT9ZY05CjdzzzSHWHDBOM7zIIpkl6sKjMIuQH_KZiOH2i8JWNtoZ72atsD1EpEwQsb7lEIaRMw40wll1l4lFQmbS0jpGWmO6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/whitedns/1631" target="_blank">📅 10:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1630">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Hf0N6S9c9TU4wrBY3x0hGZNnTjcDdfIzqM9bHjRM-Kj6l4Y4WZFgiGG_cTckGkSw57C4BZoLq5ObGwEbCFy7f4jgzIb77NlXxRKyA9kh29nqOun1wmDfU5fiNOicGsBZisOn-OezDQO41Mqpb0gD106ATqF0v8F6MVm3qioEL9liVuNrrN3LAmLqttkZvsypl-ga7Dh6Duk3CoKuPW2L6PK7C-Si768AqJnRZ460L3TqaF0FT2Tc68aMe5kcn9CPylCia9D189TlyZOv4EXVDX799SH11ipE26GIEExdZhzzsgNlOFOlMU2K18uMfKBlSutrkRTrgKbDUa_Ev2McOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی آزاد و امن به اینترنت با WhiteVPN (نسخه موبایل و دسکتاپ)
اگر به دنبال یک کلاینت یکپارچه، سبک و حرفه‌ای هستید، WhiteVPN با رابط کاربری مدرن در دسترس شماست!
⚙️
قدرت گرفته از هسته Mihomo:
این برنامه بر پایه هسته قدرتمند Mihomo (مشابه کلش و متا) توسعه یافته است که بالاترین سطح پایداری و سرعت را در دور زدن محدودیت‌ها برای شما فراهم می‌کند.
⚠️
توجه مهم:
این اپلیکیشن کاملاً سورس‌باز (Open-Source) است و در Google Play یا App Store منتشر نشده است. تنها منبع رسمی برای دانلود، مخزن گیت‌هاب پروژه است.
✨
ویژگی‌های کلیدی:
🔹
پشتیبانی همزمان از ویندوز، مک، لینوکس و اندروید
🔹
رابط کاربری ساده و اتصال تنها با یک کلیک
🔹
سیستم پراکسی جامع و تونلینگ کل سیستم (System-wide)
🔹
مدیریت پیشرفته سرورها و پایداری بالا در اتصالات
━━━━━━━━━━━━━━━━━━━━
📥
دانلود مستقیم آخرین نسخه از گیت‌هاب (رسمی):
📱
نسخه اندروید (Mobile):
🔗
https://github.com/WhiteDNS/WhiteVPN/releases/latest
💻
نسخه دسکتاپ (Windows / macOS / Linux):
🔗
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
برای دانلود، وارد لینک‌های بالا شده و از بخش "Assets" فایل متناسب با دستگاه خود (فایل apk برای اندروید و فایل‌های نصب برای ویندوز/مک) را دانلود کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/whitedns/1630" target="_blank">📅 10:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1627">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سابسکریپشن WhiteDNS برای اپ های WhiteVPN / Karing / Clash Mi / Clash Party / FLClash :
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
@whitedns</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/whitedns/1627" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1626">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Live stream finished (1 hour)</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1626" target="_blank">📅 18:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1618">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvPiLm9wHssChH43ZcNEcZEi0oE8Xnl1deRA0ioFxvkAKO_vIkAyE46bk8yKj-YMdt05tXKy3sRjuFrS__FPycgC1M70Ud-ScgwEDOj3TIueOlIpovid4MiYUbhb37_nCKFCb1b9yUpADV96lBchIRSMskJXP6z20cQmvpe5g-_aEzaakNFv_Dk01N5eFgXD_Z5OtExJxSPpc6niDu95WmRiVMga3q9u2226ZxcmQtl7kQcJBx6m1769uUOpu6Su_3P3dhjyCG7m2VD86bChCIftGxm6TLZaa5g7Kvev1ESGGYO2FSuMn0pNN7vas2TKIoLbRb0gSOgkN1CS7qFlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
یک پورت برای حکومت بر همه!
آموزش نصب و راه‌اندازی CottenRouter
🇺🇦
تماشا در یوتیوب
https://youtu.be/N725_-A_-B8
اگر روی یک سرور چند DNS Tunnel مختلف داشته باشید، خیلی زود به یک مشکل می‌خورید: همه‌شون پورت عمومی 53 رو می‌خوان.
سرویس CottenRouter دقیقاً برای حل همین مشکل ساخته شده. جلوی تمام سرویس‌ها قرار می‌گیره، دامنه هر درخواست رو تشخیص می‌ده و بدون دست‌کاری Packet، اون رو به Backend درست می‌فرسته.
یعنی می‌تونید CottenDNS، MasterDnsVPN، StormDNS، thefeed و سرویس‌های مدیریت‌شده با SlipGate رو هم‌زمان روی یک سرور و یک IP اجرا کنید؛ بدون جنگ بر سر پورت 53.
✍️
توی این ویدیو می‌بینیم:
• سرویس CottenRouter دقیقاً چه مشکلی رو حل می‌کنه
• مسیریابی درخواست‌ها بر اساس Domain چطور انجام می‌شه
• چطور چند DNS Tunnel روی یک IP اجرا می‌شن
• پشتیبانی از DNS، DoT و HTTPS
• تفاوت نصب مستقیم با Docker
• پنل مانیتورینگ، محدودسازی ترافیک و قابلیت‌های امنیتی
• نحوه نصب و اتصال Backendها
سرویس CottenRouter هیچ Label یا داده اضافه‌ای وارد Packet نمی‌کنه؛ پس فضای قابل استفاده Tunnel و MTU رو هم کاهش نمی‌ده.
🇺🇦
تماشا در یوتیوب
https://youtu.be/N725_-A_-B8
🔗
سورس‌کد و راهنمای نصب:
https://github.com/TaJirax/CottenRouter
اگر با DNS Tunnelها کار می‌کنید، این پروژه احتمالاً کلی دردسر از مدیریت سرورتون کم می‌کنه.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/whitedns/1618" target="_blank">📅 15:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1616">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔭
یک خبر خوب برای کاربران WhiteVPN
🟢
یک فیلتر جدید به سابسکریپشن
اپلیکیشن ‌های
WhiteVPN اضافه کردیم تا کانفیگ‌هایی که هنگام استفاده از ChatGPT و سرویس‌های OpenAI خطا ایجاد می‌کردند، به‌صورت خودکار از لیست حذف شوند.
🟢
از این به بعد، با تمام کانفیگ‌های موجود در سابسکریپشن باید بتوانید بدون دردسر به ChatGPT و سایر سرویس‌های OpenAI دسترسی داشته باشید.
🟢
برای دریافت لیست جدید، کافی است سابسکریپشن WhiteVPN را یک‌بار به‌روزرسانی کنید.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/1616" target="_blank">📅 11:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1610">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/E3N2cErLcXUWcPXzsblXEENPnDuFqdJsuHhHzscO9P1kLeV7B_aJpjGReSmrJTivojBqqR6macMXuXNQ4r5EtaCOolAPY7-sBfeSmhLWCnghkIUIS7kdzmtWZb85CTxuHWakeo5YE-i9Qihakn6Ky0WsUWhDa4CQ7o--SvIVFHAK9A0HmEo3MWp-TKOwH1w-nQ4aZlWebrG261z2uRa_fnWbMT5gOL9sdcQG40f5g1BU9ML5qg36gdpHFq_jONuZyxUjVsAFK602R9PejBGFCzIbSb3WMrcJVjL-paK6zzxZeGJz4p-aVRWZQzJf4Kc7aZNBm0yC9fuyN9Cx2OOPOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/whitedns/1610" target="_blank">📅 11:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1608">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">"exit chain "
⚠️
✍️
راهنمای استفاده از
#exit_chain
در اپ whitevpn# اندروید
ساب را وارد کن - برو تنظیمات - برو زنجیره اتصال - برو افزونه بعد - اشتراکی که وارد کردی را از اون بالا انتخاب کن - یک تست اتصال بگیر - یکی از کانفیگ ها را انتخاب کن - وصل شو -
تمام
✅
راهنمای استفاده از
#exit_chain
در اپ whiteaesther# اندروید
📱
برو route - گزینه exit chain را روشن کن - یا ساب و یا کانفیگ را وارد کن - برگرد صفحه اول و وصل شو -
تمام
✅
راهنمای استفاده از
#exit_chain
در اپ whiteaesther# دسکتاپ
برو advanced - برو exit chain - ساب و یا کانفیگ را وارد کن - برگرد simple - کانکت را بزن - تمام
✅
👨‍💻
این سه پست را مطالعه کنید :
https://t.me/whitedns/1601
https://t.me/c/3869114465/152008
https://t.me/c/3869114465/151806</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1608" target="_blank">📅 10:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1605">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/wByOU4yS_oTeXRaGpjFfabltc0GxuuniL5IfzofomnnHaPSJP12zgR8fCK89njlNtAWVBSDmA-E_2c2WcBJlH3G3SkgRX3UNXXTiRxD2PkRgmaOTXnYQcwbIaSIHHP_CXhIyO64Esws45cPLM7Ohk2zMXSfEYFzKP3tp2enSLtctWsUNflHL0LWAy-YlxPh_PxlYyS1D6EU7OSJ6p0e4CwoITi3tKJ1n1I_NwRiwhzqQS8mT36pTspTM8yNmgD86_luSnNAN_5Bfq092cPaKjARcvOQDRVPzyaVz-YlObcoo3FHv5-_gUK5zw0NwT92nsMgd_377b5PSwiZ5uebqnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
Wh
iteAesther
✍️
نسخه ۱.۲.۲  برای اندروید منتشر شد !
— موتور جدید و چند قابلیت
این آپدیت موتور تونل رو عوض می‌کنه و چند چیزی که کاربرها خواسته بودن اضافه می‌شه.
🟢
⚡️
موتور جدید (Aether 1.7.0)
▫️
مصرف حافظه محدود شد
— قبلاً هرچی اتصال طولانی‌تر می‌شد، حافظه‌ای که اپ می‌گرفت بیشتر می‌شد تا جایی که تونل می‌افتاد. حالا سقف داره.
▫️
WARP in WARP وقتی یک طرفش قطع بشه دوباره وصل می‌شه
به‌جای اینکه کلاً بمیره.
▫️
پیام خطای واقعی از Cloudflare
— اگه ثبت‌نام رد بشه، حالا می‌گه دلیلش چیه: آی‌پی علامت‌خورده، یا ثبت‌نام زیاد از این آدرس. قبلاً فقط می‌گفت شبکه مشکل داره.
✍️
نودهای hysteria2 و tuic توی Exit chain کار می‌کنن
اگه توی ساب‌تون نود hysteria2 یا tuic دارین و تا حالا هیچ‌وقت بالا نمی‌اومدن، دلیلش پیدا شد و درست شد.
✍️
ولی یک شرط داره:
باید پروتکل رو روی
WireGuard
بذارین (از
Routes ← Manual ← Protocol
).
روی MASQUE همچنان کار نمی‌کنه و این دست ما نیست — محدودیت خود Cloudflareست. اپ هم اگه ببینه روی MASQUE هستین بهتون می‌گه.
🟢
نودهای REALITY حالا مشخص می‌شن
اگه توی ساب‌تون نود REALITY دارین، قبلاً یا اصلاً نمی‌اومد یا می‌اومد و وصل نمی‌شد و معلوم نبود چرا. حالا با برچسب نارنجی
not supported
نشون داده می‌شه و قابل انتخاب نیست.
نود سالمه — موتور فعلی هنوز نمی‌تونه باهاش احراز هویت کنه. وقتی بتونه، خودبه‌خود دوباره کار می‌کنه.
🟢
اشتراک تونل با شبکه (LAN sharing)
می‌تونین تونل گوشی رو با بقیه دستگاه‌های همون وای‌فای به اشتراک بذارین — مثلاً لپ‌تاپ یا تلویزیون.
از
Traffic
حالت رو روی
Proxy
بذارین، بعد بخش Advanced رو باز کنین و
Share with this network
رو روشن کنین. اپ آدرسی که باید توی دستگاه دوم بزنین رو بهتون نشون می‌ده.
⚠️
رمز اختیاریه ولی حواستون باشه:
بدون رمز، هرکی روی اون وای‌فای باشه می‌تونه از تونل شما استفاده کنه و ترافیکش با هویت شما بیرون می‌ره. روی شبکه خونه خودتون مشکلی نیست؛ توی کافه و هتل و خوابگاه حتماً رمز بذارین.
🟢
صفحه اول: آی‌پی و مصرف
•
آی‌پی قبل و بعد از تونل
— که ببینین واقعاً عوض شده
•
سرعت لحظه‌ای دانلود و آپلود
و مجموع مصرف هر نشست
نکته: آی‌پی «بدون تونل» فقط وقتی خونده می‌شه که اپ باز باشه و وصل
نباشین
. اگه مستقیم بزنین connect، اون خونه خالی می‌مونه — این عمدیه، چون خوندنش وسط اتصال یعنی فرستادن آدرس واقعی‌تون از کنار همون تونلی که قراره مخفی‌ش کنه.
🟢
کلید روشن/خاموش توی پنل سریع
از
Settings
دکمه
Add a quick settings tile
رو بزنین. بعدش از پنل بالای گوشی بدون باز کردن اپ وصل و قطع می‌شین.
🟢
مشکل «Allow background running» که نمی‌رفت
روی بعضی گوشی‌ها (مخصوصاً شیائومی) هرچی اجازه می‌دادین، اون کارت باز هم می‌موند. دلیلش این بود که این گوشی‌ها تنظیم باتری خودشون رو دارن و اجازه رو فقط اونجا ثبت می‌کنن، ولی جواب استاندارد اندروید همچنان «نه» می‌مونه.
حالا اپ خودش می‌فهمه این اتفاق افتاده، شما رو می‌فرسته به تنظیمات درست گوشی، و یک دکمه
I've done this
داره که کارت رو ببنده.
📥
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
▫️
arm64-v8a
(۵۴ مگ) — تقریباً همه گوشی‌های ۲۰۱۷ به بعد. از این شروع کنین
▫️
armeabi-v7a
(۴۸ مگ) — گوشی‌های قدیمی‌تر
▫️
universal
(۱۵۷ مگ) — اگه مطمئن نیستین
اگه مشکلی خوردین، از
Settings ← Diagnostics
گزارش بگیرین و بفرستین.
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1605" target="_blank">📅 08:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1603">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/gIeNfgAVEd3TeJ0KbylnG5WvlUDUqy4fYKx-zu73yQVSr4XO4Gd6QhZ1iGQtShLjrVypTtq0BxKWOIT04-jnZMv1VE-jHQTR34sFU6EiKhP2bWVWddINSqaV_nusgaqLwnL-9VRSylFkBQjh8Dc1Nn4yM9iRxedoYEaUmDx3XD8N3AHBgA7XXNSGZ8k3DNSL3gajgHpn6nPHS4TA6I8-gjuix7Uma_wm02ntGlUvkyCfPDHif1Js7ey8VX6k_b3m0pisU8CKHYXa6KCoF6DXR22xaFCarvElfAow_VrZ7xbUQEH8Q0y2mICAjuHUw77CgLrxCgVF7UixWktgB8cIIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
آپ
دیت جدید وایت‌استر برای دسکتاپ (WhiteAesther) منتشر شد!
نسخه:
v1.5.4
در این نسخه تغییرات بسیار جذاب و کاربردی برای راحتی بیشتر شما به برنامه اضافه شده است.
🔭
تغییرات این نسخه:
🟢
اشتراک‌گذاری اتصال در شبکه داخلی (LAN Share)
از این پس می‌توانید اتصال VPN فعال روی سیستم خود را به راحتی با سایر دستگاه‌های متصل به مودم یا شبکه (مثل گوشی موبایل، تلویزیون هوشمند یا لپ‌تاپ‌های دیگر) به اشتراک بگذارید!
🟢
نمایش هوشمند وضعیت گره‌ها (پشتیبانی بهتر از Node ها)
مشکل عدم نمایش وضعیت یا کار نکردن بی‌دلیل گره‌ها برطرف شد. حالا گره‌هایی که برنامه به هر دلیلی نمی‌تواند از آن‌ها استفاده کند (مثلاً نیاز به WireGuard دارند یا از پروتکل REALITY پشتیبانی نمی‌کنند) با
رنگ نارنجی
مشخص می‌شوند. با نگه‌داشتن نشانگر موس روی آن‌ها، می‌توانید دلیل دقیق عدم پشتیبانی را ببینید.
🟢
بهبود مسیریابی کل سیستم (Whole Machine)
(تغییرات نسخه 1.5.3)
حالت System Proxy حالا به درستی ترافیک کل سیستم را از طریق مسیر زنجیره‌ای فعال (Active Chain) شما عبور می‌دهد.
🔭
راهنمای استفاده از قابلیت LAN Share (اشتراک اینترنت با گوشی و
تلویزیون):
۱. در برنامه به بخش
Settings
(تنظیمات) بروید و تب
Traffic & DNS
را باز کنید.
۲. گزینه
"Share this connection on my network"
را فعال کنید.
۳. برنامه به شما یک
آدرس (IP)
و یک
پورت
(مثلاً 1080) نمایش می‌دهد.
۴.
امنیت اتصال:
در همین بخش می‌توانید یک
نام کاربری (Username)
و
رمز عبور (Password)
تعیین کنید تا فقط خودتان بتوانید به آن وصل شوید.
(
⚠️
توجه: اگر این دو کادر را خالی بگذارید، هر دستگاهی در شبکه وای‌فای شما می‌تواند بدون رمز از اینترنت آزاد سیستم شما استفاده کند).
۴. حالا وارد تنظیمات پروکسی (HTTP یا SOCKS5) در گوشی، تلگرام یا تلویزیون خود شوید، آی‌پی و پورت نمایش داده شده را وارد کنید و روی اتصال ضربه بزنید.
(نکته: در اولین استفاده از این قابلیت، فایروال ویندوز از شما یک تاییدیه می‌خواهد که باید روی گزینه
Allow Access
کلیک کنید تا پورت شبکه باز شود).
✍️
هم‌اکنون می‌توانید برنامه خود را به آخرین نسخه به‌روزرسانی کنید.
https://github.com/WhiteDNS/WhiteAesther/releases/latest
#آپدیت
#وایت_استر
#WhiteAesther
#پروکسی
#تونل
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1603" target="_blank">📅 07:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1602">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Xm8sfsHcE7Z5-3QjnqZupUZUoNpebzm09h0Nw5_oLrNNo7wKcghzJ42174Iw8_N1xQAD3B2F12kBBK7IwIiAWqEdSi_xev06WVPuIMs9DyDU9kAS5ugAKchQZ_09cIITDLiieYR5gbc2Jy8C_Q47lElXw22E8kKYy0UckyLUgyxHoCTTGCsS9uskhebutliFXWiTw0cwHNYJ0zGYO7r-o4-NT1-i1obwmIXwO-GD0iD-GIKPYLGVmkH8D9mgiLVuUUfGdTa6-tDHDKvAW6DbqzOvYbzGV6OseHgstEhX3kW4t5DR4259L1I--5F3FCIfOV5tXsSfoBLrK0c-3Eiqog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
نسخه جدید موبایل و دسکتاپ به زودی منتشر می‌شود!
این نسخه‌ها شامل چه مواردی است؟
🟢
بهبود عملکرد اتصال برنامه
🟢
ارتقا موتور به ۱.۷.۰
🟢
اضافه کردن امکان LAN sharing
🟢
رفع باگ
🟢
در اندروید امکان اضافه شدن به Quick setting
🟢
استفاده از wireguard و hysteria exit chain برای داشتن حداکثر سرعت
ممنون
@WhiteDNS
🔥</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1602" target="_blank">📅 19:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1601">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Mv_yuWaLM9T61Fq-_Ge2Y7rWq7w6Z7H4MNYimvFYz8XQP3RfXOnIbw8hB5-ghitZwCwz-mVCGkuWa1_0q2iglGagKqQP3LvH3hYFXEk-QetxgUANvKPP-dip63AXpBlM4Vzyf8BkX6HVP-RPvfbEF4B_6kPc7TRkQCtGPfdrEu-CYNs0PzdyywOtU3dWVKp92zoPGxmmxGaAwWE2D5WdDQg_s9dXhmc-x_CI17RopalEF2b9lCZkB4gtUc9vdvLK5MfQTWmQ3xLGTdwxAz60RQgeKFiGvNQMGwU-XGdotaY_4MK0FdVR0SnlV6Cz5EQNdOiSwhxyf0PpQSYGUH5ACQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم
⚠️
⚠️
⚠️
⚠️
⚠️
دوستان :
پست  را با دقت مطالعه کنید
https://t.me/whitedns/1568
این کانفیگ های برای قابلیت "exit chain" توی اپ whiteaester و whitevpn هست - که ip شما را ثابت میکنه و یک لایه امنیت بیشتر به شما میده چون TLS هست
چون خیلی از دوستان کانفیگ نداشتن و یا نگران امنیتشون بودند ما این امکان را فراهم کردیم .
این کانفیگ ها برای استفاده مستقیم در اپ هایی مثل v2rayng و غیره نیست، اگر قصد استفاده مستقیم دارید لطفاً درخواست ارسال نفرمایید
تشکر
@whitedns</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/whitedns/1601" target="_blank">📅 17:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1600">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ODWr3DywiFIRbw8_0OdFd5ehRWd73kYF9LWuXKBNy5ZXiCDrJJN4YamH8paIZyR0K3i0DMJXRa02TGVwoiDYpABID52_3O-TCOjU1sx1UdPIoQBkIc16KDQpXVTt4MOdfg6Vz_mhAnsjo5xQbwAwkOHNGt_5WKkEwCu67Kh6pE0hiF6LB677CUDFXjkowdX9KfN32-qrgWvDVspkWHw_L3HYQHrBpvm9o0WPN_JpAfyM4f0I0I9M4uj8NPwKpgAkok-uL3oTGE2pf8WKhR7alm4xMQxvv3_-aaqovxTIaMdHDkbxSElZaxqqh29D3zKm1NaDyTaCTRJxtvs_sZmIRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
راهنمای کامل استفاده از ربات WhiteDnsChain
(کانفیگ هسته x-ray )
نکته : این ربات یک کانفیگ اضطراری برای شما ایجاد میکند تا در موارد خیلی خاص از ان استفاده کنید . کانفیگ های این ربات برای امکان exit chain در اپ های white ایجاد شده و هر گونه سواستفاده از آن مجاز نیست
🤖
آدرس ربات:
@WhiteDnsChainbot
برای دریافت و مدیریت اتصال اختصاصی خود مراحل زیر را انجام دهید:
1️⃣
شروع و انتخاب زبان
- وارد ربات شوید.
- دستور /start را ارسال کنید.
- گزینه «
🇮🇷
فارسی» را انتخاب کنید.
- برای تغییر زبان در آینده از گزینه «
🌐
تغییر زبان» استفاده کنید.
2️⃣
درخواست کانفیگ
- روی «
🔐
دریافت کانفیگ» بزنید یا دستور /config را ارسال کنید.
- درخواست شما برای مدیر فرستاده می‌شود.
- پس از تأیید، یک پیام اطلاع‌رسانی دریافت می‌کنید.
- دوباره /config را بزنید تا لینک اشتراک و QR اختصاصی شما نمایش داده شود.
3️⃣
اضافه‌کردن کانفیگ به برنامه
- یک برنامه سازگار با V2Ray/Xray روی دستگاه خود نصب کنید.
- لینک اشتراک را کپی کنید.
- در برنامه گزینه افزودن Subscription یا «افزودن اشتراک» را انتخاب کنید.
- لینک را وارد کرده و اشتراک را به‌روزرسانی کنید.
- یکی از سرورها را انتخاب کرده و اتصال را فعال کنید.
4️⃣
مشاهده وضعیت حساب
از گزینه «
👤
حساب من» یا دستور /account استفاده کنید تا موارد زیر را ببینید:
- وضعیت فعال یا غیرفعال
- تاریخ انقضا
- حجم مصرف‌شده
- حجم کل
- محدودیت تعداد دستگاه یا IP
5️⃣
دریافت دوباره کانفیگ
اگر پیام کانفیگ را پاک کردید، نگران نباشید. با /config همان کانفیگ اختصاصی دوباره نمایش داده می‌شود و کانفیگ جدیدی ساخته نخواهد شد.
6️⃣
پشتیبانی
- روی «
💬
پشتیبانی» بزنید یا /support را ارسال کنید.
- مشکل خود را در یک پیام کامل توضیح دهید.
- پیام مستقیماً برای مدیر ارسال می‌شود.
- پاسخ مدیر را داخل همین ربات دریافت خواهید کرد.
7️⃣
دستورات کاربردی
- /start — شروع و انتخاب زبان
- /config — دریافت کانفیگ
- /account — مشاهده وضعیت حساب
- /menu — نمایش منوی اصلی
- /support — ارتباط با پشتیبانی
- /help — نمایش راهنما
⚠️
نکات مهم
⚠️
-درخواست ها توسط ادمین دونه دونه بررسی و تایید میشود پس لطفا صبور باشید
- ادمین کاملا مختار است که به هر دلیل ممکن از ارایه کانفیگ به شما خودداری کند پس لطفا اعتراض نکنید
⚠️
-در حال حاظر کانفیگ ها با محدودیت 1 روزه و یک گیگ هست
- لینک و QR کاملاً اختصاصی است؛ آن را برای دیگران ارسال نکنید.
- هر حساب تلگرام فقط یک کانفیگ فعال دریافت می‌کند.
- ارسال چندباره /config کانفیگ تکراری ایجاد نمی‌کند.
- برای امنیت بیشتر، پس از دریافت کانفیگ می‌توانید پیام آن را با گزینه «
🗑
مخفی کردن» حذف کنید.
- در صورت پایان حجم یا اعتبار، از طریق پشتیبانی با مدیر ارتباط بگیرید.
@whitedns</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/whitedns/1600" target="_blank">📅 17:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1599">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMasterDnsVPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSg-pPpq9uTsLSycmMSFmbzGX0O0Bij_12PtlZ5z3yCItzuC-zk5_2mLx8EC875rLJFcrusy-67EorztvJ3UjUongSfEbYsJ0dlk8UEFZUY1c55Q3YLgRpedYNDZD0shIbR5hH30PZ11LP3enFM7PmSSp02ex74mhHU6ZSrzoPWg6Z2UkGCMw3R9YKZz2xeHcAImArF3wkzogaBRHxTqziYOli9Ikkt2mUshh8V1Ca-t8Bo0BkgjGfeu6HJHOH95uctPETpHTmOOrZ_RBehJxIquR9EWWeAzqyNjhSLn1dTeUYDLWKJEyp04_d0IDZIHPnusZ_07VklNTpsQG0x7CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👋
درود،
◀️
آموزش رفع مشکل خطای
Sign-in failed: failed to start login server: An attempt was made to access a socket in a way forbidden by its access permissions. (os error 10013)
مربوط به برنامه ChatGPT در ویندوز
◀️
ابتدا در منوی استارت خود کلمه cmd را سرچ کنید.
◀️
سپس روی آن راست کلیک و Run as Administrator را بزنید.
◀️
در نهایت دستورات زیر را وارد کنید و Enter بزنید.
net stop winnat
net start winnat
✅
مشکل شما رفع میشود.
❤️
پیروز و سربلند باشید.
🤨
با تشکر فراوان،
امین محمودی
🗓
3 شهریور ماه 1405
🛡
کانال:
@MasterDnsVPN
💬
گروه:
@MasterDnsVPNGroup
#chatgpt
#هوش_مصنوعی
#رفع_مشکل</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/whitedns/1599" target="_blank">📅 16:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1598">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMasterDnsVPN</strong></div>
<div class="tg-text">👋
درود،
⚠️
یک پروژه هست، دوستان معرفی کردن، من تایید یا رد نمیکنم، فقط منتشر میکنم، خوب بودن و نبودنش با خودتون، من خیلی چک نکردم.
◀️
پروژه واسه جمع کردن کانفیگ های v2ray هست.
👩‍💻
0xRadikal/Free-v2ray-Configs
◀️
تفاوت اصلی پروژه با بقیه ریپوهای کانفیگ رایگان اینه که صرفاً کانفیگ‌ها رو از منابع مختلف جمع نمی‌کنه. کانفیگ‌ها وارد یک pipeline چندمرحله‌ای می‌شن، duplicateها حذف می‌شن، ساختار و endpoint بررسی می‌شه، اتصال TCP تست می‌شه و در نهایت کانفیگ با یک درخواست HTTP واقعی از طریق proxy در ۳ دور مستقل تست می‌شه.
◀️
در حال حاضر پروژه از ۲۱ منبع تغذیه می‌شه و در آخرین اجرای ثبت‌شده:
🔴
۱۱٬۴۱۵ کانفیگ یکتا جمع‌آوری شده
🔴
۲٬۴۰۳ کانفیگ در هر ۳ دور تست موفق بودن و وارد بخش
verified
شدن
🔴
خروجی‌های
verified
،
fast
،
secure
و
top100
تولید می‌شه
🔴
خروجی برای V2Ray/Xray، Clash و sing-box ارائه می‌شه
🔴
کل سیستم هر ۱۵ دقیقه به‌صورت خودکار به‌روزرسانی می‌شه
✅
به گفته ناشر: هدف پروژه اینه که این پروژه تبدیل به یک منبع متن‌باز و قابل‌اعتماد برای کانفیگ‌های رایگان بشه، مخصوصاً برای کاربران ایرانی.
🔴
نمونه همینکار رو هم WhiteDns انجام داده، اینجا میتونین ببینین:
👩‍💻
WhiteDNS/subs-check
🔴
اگر از این پروژه خوشتون اومد میتونین با
⭐️
دادن داخل گیت هاب از ناشر این برنامه حمایت کنین.
⚠️
نکته تکمیلی از سمت خودم: اگر از Vless/Vmess و هر فیلترشکن رایگانی استفاده میکنین، اگر امنیت اطلاعاتتون مهمه، حتما از حالت Chain و ... استفاده کنین، یعنی به وسیله اون VPN به یه VPN دیگه به سرور خودتون وصل بشید و Vmess/Vless سرور خودتون رو داشته باشید، از سرورهای رایگان برای فیلتر نشدن و ... استفاده کنین (البته که من کلا پیشنهاد میدم، VPN رایگان تا حد امکان استفاده نکنین و سرور خودتون رو راه اندازی کنین، اما این سرویس ها ممکنه، برای بعضی ها کاربردی باشه)، اما برای امنیت بیشتر اینکار رو انجام بدید.
❤️
پیروز و سربلند باشید.
🤨
با تشکر فراوان،
امین محمودی
🗓
1 شهریور ماه 1405
🛡
کانال:
@MasterDnsVPN
💬
گروه:
@MasterDnsVPNGroup
#v2ray
#معرفی_پروژه
#اینترنت_آزاد
#فیلترشکن
#vless
#vmess</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1598" target="_blank">📅 09:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1597">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbUxXjO4fG2v492sK7-TFPA58xaZPBVhQC2QAU3BrkM0IPMfrMYTnV-k0lUAtpxl0aS0ePfF7Y9_M5WTTdNUq-4EiZTfF-9ixGJjAQwf1lC1317Y3w-LstV1UY50durVv_rULlAZEtWI1zillWqFGxny6mP-m93dsPKJ5IdOcfJ6j7zVZLQ-yQu57gC1exXnwoqAXB1t3CATwejsktUF4gZuTgK_kEi82H_9nu6qMRO_YymLQ_A1oKnH920jH5oXZgqyqjk5kYzZREndfnRGP-aUn7rimLlKsKe_UZ2CTwzu4vfvO4HYebwnNCZbgi8-fqxAjsdAdEI26jdrITCL0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
برای آیفون اپلیکیشن نداریم؟ چرا، داریم!
اگر از کاربران iOS هستید، می‌توانید از اپلیکیشن
Core Forge
استفاده کنید؛ یک اپلیکیشن کامل که سه قابلیت اصلی را یکجا در اختیارتان قرار می‌دهد:
🔹
اتصال VPN
🔹
استفاده از MasterDNS, CottonDNS
🔹
اتصال از طریق پروتکل Aesther
دیگر لازم نیست برای هرکدام از این قابلیت‌ها یک اپلیکیشن جدا نصب کنید؛ همه‌چیز داخل
Core Forge
در دسترس است.
📥
دریافت Core Forge برای iPhone
🎥
تماشا ویدیو آموزشی در یوتیوب
🔥
لینک ساب WhiteVPN برای استفاده در اپ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/whitedns/1597" target="_blank">📅 08:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1596">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">📹
آموزش اپلیکیشن WhiteVPN کامپیوتر و استفاده اپ داخل
🍏
آیفون برای کاربران IOS
https://youtu.be/tm0ls3r4ppw</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/1596" target="_blank">📅 01:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1594">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔭
در ۳۰ روز گذشته، بیش از ۷۰۰ هزار اتصال موفق در اپلیکیشن WhiteVPN ثبت شده.
خوشحالیم که در این مسیر کنار شما هستیم.
🕊️
به امید روزی که همه به اینترنت آزاد دسترسی داشته باشیم و از WhiteVPN فقط برای حفظ امنیت و حریم خصوصی استفاده کنید، نه برای عبور از فیلترینگ.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/whitedns/1594" target="_blank">📅 14:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1593">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🌎
انتشار نسخه ۱.۶.۲ WhiteDNS برای اندروید</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/whitedns/1593" target="_blank">📅 14:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1589">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.2-armeabi-v7a.apk</div>
  <div class="tg-doc-extra">34.2 MB</div>
</div>
<a href="https://t.me/whitedns/1589" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/whitedns/1589" target="_blank">📅 14:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1588">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5RhbFHpqp3xu656SUFrLVKP2euwSxGa08NbFO52LhJ3DQroFh2qm-5iozMcw9Zq9iDXuutPdGyJp6nP_GqC1KAlnkeNmQbmxDtbQOeMkC09JYFpYiJtUmXVFYMPPwsYSbCYq3a61KJ-WCCFiSuJcOtRBa2ui1A_1UM_GgprByVS_nKkdbwJ2O61JBq1_XuWuYBu3vLkIkrAn3b1SfJJeVa3WEV9_kANa9lN0HEP7h7GccssabED8kPpka-j1tXYizRughFwpT1Gvm_bbzWFrfxQy4VCXj6BheN1R3XS33apm1h-gCkPCA-1TuJTC0uXNl9zXEW4s_qxQnvmiHXwCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
WhiteVPN 1.6.2
✍️
این نسخه اتصال WhiteVPN را سریع‌تر و پایدارتر می‌کند و چند بهبود مهم برای سابسکریپشن‌ها، تنظیمات و Split Tunneling دارد.
✍️
تغییرات مهم
• اتصال مجدد خودکار، سریع‌تر و قابل‌اعتمادتر شده است.
• در صورت بروز مشکل در اتصال، برنامه بهتر و امن‌تر آن را بازیابی می‌کند.
• بررسی سلامت اتصال و مدیریت تغییرات شبکه بهبود یافته است.
• هنگام قطع اتصال، وضعیت واقعی عملیات نمایش داده می‌شود و برنامه تا توقف کامل اتصال در حالت «در حال قطع اتصال» باقی می‌ماند.
• مدیریت و ذخیره‌سازی سابسکریپشن‌ها پایدارتر شده است.
• فایل‌های خراب سابسکریپشن به‌صورت خودکار شناسایی و دوباره دریافت می‌شوند.
• آخرین نسخه سالم سابسکریپشن برای مواقعی که دریافت نسخه جدید ممکن نیست، حفظ می‌شود.
• پشتیبانی از لینک‌ها و کانفیگ‌های SOCKS و SOCKS5 اضافه شده است.
• تنظیمات سابسکریپشن، زبان و ظاهر برنامه به بخش جدید «تنظیمات برنامه» منتقل شده‌اند.
• گزینه «بازنشانی تنظیمات» اضافه شده است؛ بدون حذف سابسکریپشن‌ها، نتایج تست‌ها یا قطع اتصال فعال.
• در بخش Split Tunneling اکنون تمام برنامه‌های نصب‌شده، حتی برنامه‌های بدون آیکون، نمایش داده می‌شوند.
• اسکرول فهرست برنامه‌ها در Split Tunneling اصلاح شده است.
• ذخیره نتایج تست اتصال و به‌روزرسانی صفحه سریع‌تر و روان‌تر شده است.
• حجم نسخه نهایی با حذف منابع اضافی کاهش یافته است.
📱
دانلود از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.2</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/whitedns/1588" target="_blank">📅 14:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1587">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✍️
دوستان، فعلاً سرور ساب WhiteVPN با یک مشکل فنی روبه‌رو شده و بچه‌ها در حال بررسی و برطرف کردنش هستن.  به‌محض اینکه مشکل حل بشه، ساب رو آپدیت می‌کنیم و همین‌جا بهتون خبر می‌دیم.  ممنون که صبورید و شرمنده بابت اختلالی که ممکنه براتون ایجاد شده باشه
🙏
فعلا…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/whitedns/1587" target="_blank">📅 13:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1584">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/uBq5yDhHbigBdyal7C8iXMYY4-Kzk-ybr6VL5ChW9GjKHRMOHUZdTXaRmTRHwoEoRX9tkTeethWRYIJCBX65Lhj-G0VazM-J0IwaaE4s9uzW45K7QjuuiucDDTtR0h2yHNcEsd4dXXFrvHMFLrFuo9FrvSG1pKwIoziS2PrE8kUZu0B9WptPuT8JQ6YtzJUh5DBTtoDEKXcMXwEMGAbConIIH9EMA58TAVyM1XovFRLWxvNz25Le2vP-aQiHuoGx_x52BVxLVTq35Aoi8rnWJf6sGOBEUjC2EwfrlHVg6guYpsck1ZgtGvYgasJVSB7bflrRe2snn1illubyyRPTUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم
⚠️
⚠️
⚠️
⚠️
⚠️
دوستان :
پست  را با دقت مطالعه کنید
https://t.me/whitedns/1568
این کانفیگ های برای قابلیت "exit chain" توی اپ whiteaester و whitevpn هست - که ip شما را ثابت میکنه و یک لایه امنیت بیشتر به شما میده چون TLS هست
چون خیلی از دوستان کانفیگ نداشتن و یا نگران امنیتشون بودند ما این امکان را فراهم کردیم .
این کانفیگ ها برای استفاده مستقیم در اپ هایی مثل v2rayng و غیره نیست، اگر قصد استفاده مستقیم دارید لطفاً درخواست ارسال نفرمایید
تشکر
@whitedns</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/whitedns/1584" target="_blank">📅 11:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1582">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✍️
دوستان، فعلاً سرور ساب WhiteVPN با یک مشکل فنی روبه‌رو شده و بچه‌ها در حال بررسی و برطرف کردنش هستن.
به‌محض اینکه مشکل حل بشه، ساب رو آپدیت می‌کنیم و همین‌جا بهتون خبر می‌دیم.
ممنون که صبورید و شرمنده بابت اختلالی که ممکنه براتون ایجاد شده باشه
🙏
فعلا از ساب موقت استفاده کنید تا اون مشکل حل بشه
https://ns1.rmft.tech/top300/sub
https://raw.githubusercontent.com/paranoideveloper/CoreForge-Sub/main/subscription_base64.txt
ارادتمند
تیم وایت</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1582" target="_blank">📅 07:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1581">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/K63v9-icgU34hGghHC0MuLxSs4EMQCsPpj5Y-__NV3uEERR4Fhi0xLzUjHQtkJSmEvJUkkGTeTdiho1-oc_Vm0DeHpd2RSUitV9wMdkUhny1cFLFGcdfnJWnbx19qfae3mbjF4jR3zMRk_4w_i3syecJ7yk5Lol14DZhBEgd64G4uPAIRHeIdFLeMjQScYAsM-FRuS9axJdWuMJb4VwjaVNSDl3Ctqui6umbe9UVwa7rrLv9VCV54AMvNXEA9epYMu3F2jMrl3SQvdX6L0xpgM54t6xg-5saYh-OvX7e6MSBjrdRKowxxMV9N-1Q6AW0p5o3dPqR8NcyoAoHwLKpjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/whitedns/1581" target="_blank">📅 06:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1580">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/nOgCJl_QubgHfStLeL3cIb3TDKkV_iB12iKXejKMTo5yeHQlcqmgThFFUPuO8jmZcvvjj-Q9rnVZRqQy4y5_LB0SHvtxdi4juKZw0HqBhTv76IMesobnzG_N_wizHsHxFvN3rNkfWCSRiSuIenU-UV_huhNpt5uhEr5hCq3ifssNrgPBNapnmWlQqCeSnDB3OfQjTU6tSTio38VA2FYORWKGBLLtuPkhcsqd6WdpFGMPxKnwfiaiP0lJZaDhYfe4pQcFmfi0RBkVenHnxYMVtramGLES4VBtSdeKNKdbViwtdQMmphkSen0i30aVGFSn-Df02x8576f2rJnCI74Izg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی آزاد و امن به اینترنت با WhiteVPN (نسخه موبایل و دسکتاپ)
اگر به دنبال یک کلاینت یکپارچه، سبک و حرفه‌ای هستید، WhiteVPN با رابط کاربری مدرن در دسترس شماست!
⚙️
قدرت گرفته از هسته Mihomo:
این برنامه بر پایه هسته قدرتمند Mihomo (مشابه کلش و متا) توسعه یافته است که بالاترین سطح پایداری و سرعت را در دور زدن محدودیت‌ها برای شما فراهم می‌کند.
⚠️
توجه مهم:
این اپلیکیشن کاملاً سورس‌باز (Open-Source) است و در Google Play یا App Store منتشر نشده است. تنها منبع رسمی برای دانلود، مخزن گیت‌هاب پروژه است.
✨
ویژگی‌های کلیدی:
🔹
پشتیبانی همزمان از ویندوز، مک، لینوکس و اندروید
🔹
رابط کاربری ساده و اتصال تنها با یک کلیک
🔹
سیستم پراکسی جامع و تونلینگ کل سیستم (System-wide)
🔹
مدیریت پیشرفته سرورها و پایداری بالا در اتصالات
━━━━━━━━━━━━━━━━━━━━
📥
دانلود مستقیم آخرین نسخه از گیت‌هاب (رسمی):
📱
نسخه اندروید (Mobile):
🔗
https://github.com/WhiteDNS/WhiteVPN/releases/latest
💻
نسخه دسکتاپ (Windows / macOS / Linux):
🔗
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
برای دانلود، وارد لینک‌های بالا شده و از بخش "Assets" فایل متناسب با دستگاه خود (فایل apk برای اندروید و فایل‌های نصب برای ویندوز/مک) را دانلود کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/whitedns/1580" target="_blank">📅 06:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1579">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fj7QrXhVpYuJLTnVWkIenc040p_EEcdbcC70dDPUCmUFPTnQIt_1ersxjAoYxU2ceg6SpR1I7mAURJfVHSZ9wgvuDHhRBAf2GTxvM5Mbf3FyL0soA78wXCCVTGUeMjvXYQePI7kIp6CInVhpoc9Q5RMNJOEwHHpHI1phuaoqZtRKT-QjpSgJ3ygvYt9f81FvZ-PjWqhiEWNB-xLbjBKHGa4O9gZ4RKum8ikuCCmCQSC7OZyneyx8xHfh9Sz3LjuZ6RbN7K_uDrAH01jgACVUv0g0ZDXrPNaBj09LEHYB7pzfkZ606I6VDBY5zBvzeZSB80Fhf04dBU05FiUn4I1inQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم
⚠️
⚠️
⚠️
⚠️
⚠️
دوستان :
پست  را با دقت مطالعه کنید
https://t.me/whitedns/1568
این کانفیگ های برای قابلیت "exit chain" توی اپ whiteaester و whitevpn هست - که ip شما را ثابت میکنه و یک لایه امنیت بیشتر به شما میده چون TLS هست
چون خیلی از دوستان کانفیگ نداشتن و یا نگران امنیتشون بودند ما این امکان را فراهم کردیم .
این کانفیگ ها برای استفاده مستقیم در اپ هایی مثل v2rayng و غیره نیست، اگر قصد استفاده مستقیم دارید لطفاً درخواست ارسال نفرمایید
تشکر
@whitedns</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/whitedns/1579" target="_blank">📅 22:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1577">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">📹
آموزش اپلیکیشن WhiteVPN کامپیوتر و استفاده اپ داخل
🍏
آیفون برای کاربران IOS
https://youtu.be/tm0ls3r4ppw</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/whitedns/1577" target="_blank">📅 17:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1576">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLordofCinder</strong></div>
<div class="tg-text">🚀
بالاخره ‎CottenRouter‎ منتشر شد!
چیزی که خیلی‌هاتون بارها درخواست کرده بودید، بالاخره آماده شد.
🔥
اگه روی یک ‎VPS‎ چند ‎DNS Tunnel‎ دارید، دیگه لازم نیست برای ‎Port 53‎ بین سرویس‌ها درگیر باشید.
‎CottenRouter‎ امکان اجرای چند ‎Tunnel‎ روی
یک ‎IP‎ و یک ‎Port 53‎
رو فراهم می‌کنه و هر ‎Domain‎ رو به ‎Backend‎ مربوط به خودش هدایت می‌کنه.
⚡️
پشتیبانی از:
‎CottenDNS‎
‎MasterDnsVPN‎
‎StormDNS‎
‎thefeed‎
‎SlipGate‎
🛠
امکانات:
• ‎UDP / TCP‎
• ‎Multi-Domain‎ و ‎Multi-Backend‎
• ‎Port 53‎ بین چند ‎Tunnel‎
• ‎DoT‎، ‎DoH‎ و ‎HTTPS‎ بر اساس ‎SNI‎
• ‎TUI‎ و ‎Control Deck‎ برای مدیریت و مانیتورینگ
• نصب مستقیم روی ‎Linux‎
• پشتیبانی از ‎Docker‎
• ‎AMD64‎ و ‎ARM64‎
🛡
بدون دستکاری ترافیک ‎Tunnel‎
‎CottenRouter‎ چیزی به پکت ها و تانل اضافه نمیکنه
بنابراین قابلیت‌هایی مثل ‎ARQ‎، ‎FEC‎، ‎Compression‎، ‎MTU Discovery‎، ‎Record Channels‎، ‎SOCKS‎ و ‎TCP Forwarding‎ بدون تغییر باقی می‌مونن.
🔥
خلاصه:
یک ‎IP‎ + یک ‎Port 53‎ + چند ‎DNS Tunnel‎
🔗
‎GitHub‎:
https://github.com/TaJirax/CottenRouter</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/whitedns/1576" target="_blank">📅 15:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1570">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/sc55WzDnYZgnax7mHBQinrFlXd_xYpaPgqkWI50g0Z0VKAkjwmUox6bQ48-kC0WIEV3PuaEgnVXa2_PPfez8TyqWAF6wxxAIpbAICRKueJ--N3OQY-DFtIyhH2DBb0r5HPTBzBPQD2KFDaKLKYYEa8AWsjDqP9T3C_QmNZKnxiljodcaoUZrDxrExfm8QbFpRa8gE1oJRLZGONHrpXnwpy8NI5qTqrCTwPFWmVf3tKzyHB7LjM27dd-m5Gk10Fa21eeutSXgFt_b97aksfaZ7IEXVjhHO4dCs_kLsJxultmD6WE6IxiD7eYk-Lhczc1SqC55sEYdA00KZ9RvvTzd0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقت :
یک سوال خودمونی :
تا الان نزدیک 50 نفر کانفیگ دریافت کردن
چرا حتی به خودشون زحمت ندادند یک لایک کنند ؟
این فرهنگ عجیب از کجا اومده ؟
اون لایکی که شما میکنید یک انرژی برای این تیم هست که شما دریغ میکنید .
😏</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/whitedns/1570" target="_blank">📅 06:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1568">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Gtmu_9HP5-L7fRhow-2I3NqV7wlpuZzAeumaEJ8GNidw_kOZ5kEi5egCSYNkbQMSkwCV3QzeaWZqFpFjIg1IF5RHAfGfxHocu-l19FrzV9jocI-9jffaLd7-7_YXcb4jI_so-ftr0QQC8MtJK5shGDzzFgJUqYKrptqHf3sjv82KKVDA-hpsrWE4nj0IgffIfBSUhLBlhGti0vHXCBHkjnorXV9tT314QKxG6uZ-NOlqAnEuTI062Z0loAolFJdnAxbRhKkPZuomLjmJ4AbFXmztScRWZyqSjzazyLgnp0toLDVUYLAC6XFuUQb1hvlhAnXqfMfxW6rFEqndxqkV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
راهنمای کامل استفاده از ربات WhiteDnsChain
(کانفیگ هسته x-ray )
نکته : این ربات یک کانفیگ اضطراری برای شما ایجاد میکند تا در موارد خیلی خاص از ان استفاده کنید . کانفیگ های این ربات برای امکان exit chain در اپ های white ایجاد شده و هر گونه سواستفاده از آن مجاز نیست
🤖
آدرس ربات:
@WhiteDnsChainbot
برای دریافت و مدیریت اتصال اختصاصی خود مراحل زیر را انجام دهید:
1️⃣
شروع و انتخاب زبان
- وارد ربات شوید.
- دستور /start را ارسال کنید.
- گزینه «
🇮🇷
فارسی» را انتخاب کنید.
- برای تغییر زبان در آینده از گزینه «
🌐
تغییر زبان» استفاده کنید.
2️⃣
درخواست کانفیگ
- روی «
🔐
دریافت کانفیگ» بزنید یا دستور /config را ارسال کنید.
- درخواست شما برای مدیر فرستاده می‌شود.
- پس از تأیید، یک پیام اطلاع‌رسانی دریافت می‌کنید.
- دوباره /config را بزنید تا لینک اشتراک و QR اختصاصی شما نمایش داده شود.
3️⃣
اضافه‌کردن کانفیگ به برنامه
- یک برنامه سازگار با V2Ray/Xray روی دستگاه خود نصب کنید.
- لینک اشتراک را کپی کنید.
- در برنامه گزینه افزودن Subscription یا «افزودن اشتراک» را انتخاب کنید.
- لینک را وارد کرده و اشتراک را به‌روزرسانی کنید.
- یکی از سرورها را انتخاب کرده و اتصال را فعال کنید.
4️⃣
مشاهده وضعیت حساب
از گزینه «
👤
حساب من» یا دستور /account استفاده کنید تا موارد زیر را ببینید:
- وضعیت فعال یا غیرفعال
- تاریخ انقضا
- حجم مصرف‌شده
- حجم کل
- محدودیت تعداد دستگاه یا IP
5️⃣
دریافت دوباره کانفیگ
اگر پیام کانفیگ را پاک کردید، نگران نباشید. با /config همان کانفیگ اختصاصی دوباره نمایش داده می‌شود و کانفیگ جدیدی ساخته نخواهد شد.
6️⃣
پشتیبانی
- روی «
💬
پشتیبانی» بزنید یا /support را ارسال کنید.
- مشکل خود را در یک پیام کامل توضیح دهید.
- پیام مستقیماً برای مدیر ارسال می‌شود.
- پاسخ مدیر را داخل همین ربات دریافت خواهید کرد.
7️⃣
دستورات کاربردی
- /start — شروع و انتخاب زبان
- /config — دریافت کانفیگ
- /account — مشاهده وضعیت حساب
- /menu — نمایش منوی اصلی
- /support — ارتباط با پشتیبانی
- /help — نمایش راهنما
⚠️
نکات مهم
⚠️
-درخواست ها توسط ادمین دونه دونه بررسی و تایید میشود پس لطفا صبور باشید
- ادمین کاملا مختار است که به هر دلیل ممکن از ارایه کانفیگ به شما خودداری کند پس لطفا اعتراض نکنید
⚠️
-در حال حاظر کانفیگ ها با محدودیت 1 روزه و یک گیگ هست
- لینک و QR کاملاً اختصاصی است؛ آن را برای دیگران ارسال نکنید.
- هر حساب تلگرام فقط یک کانفیگ فعال دریافت می‌کند.
- ارسال چندباره /config کانفیگ تکراری ایجاد نمی‌کند.
- برای امنیت بیشتر، پس از دریافت کانفیگ می‌توانید پیام آن را با گزینه «
🗑
مخفی کردن» حذف کنید.
- در صورت پایان حجم یا اعتبار، از طریق پشتیبانی با مدیر ارتباط بگیرید.
@whitedns</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/whitedns/1568" target="_blank">📅 05:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1567">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد
PattNG
/
PattN
کرده و لذت ببرید !
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt
ساب هر ۲۴ ساعت آپدیت میشود.
///
توضیحات:
چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری و تست میکنند و سپس کانفیگهای سالم را فیلتر و در اختیار قرار میدهند پروژه‌ها‌ی
https://github.com/0xRadikal/Free-v2ray-Configs
و
https://github.com/itsyebekhe/PSG
و
https://github.com/Delta-Kronecker/V2ray-Config
هستند.
اما این پروژه‌ها دو مشکل اساسی دارند، اول اینکه تست کانفیگها باید از طریق اینترنت و فایروال ایران انجام شود ولی در حال حاضر تست کانفیگها در این پروژه‌ها از طریق گیتهاب انجام میشود، دوم اینکه روی نت‌های آپلود محدود (ایرانسل و ...) عملا اکثر کانفیگهای این پروژه‌ها آپلود محدود هستند و کیفیت بسیار پایینی دارند.
از آنجا که با روشهای زیادی میتوان محدودیت آپلود را روی کلودفلر دور زد، من در پروژه‌ی خودم اومدم کانفیگهای کلودفلر سالم را از پروژه‌ها‌ی اصلی جدا کردم و تغییراتی را برای دور زدن محدودیت آپلود (و همچنین دور زدن فیلتر دامنه) اعمال کردم (در حال حاضر متد fragment+fingerprint اعمال شده). بنابراین کانفیگهای نهایی سالم و با حداکثر سرعت در تمامی نتها قابل استفاده هستند.
برای دور زدن محدودیت آپلود در نتهای آپلود محدود در حال حاضر فقط باید از کلاینت
PattNG
/
PattN
استفاده کنید، بزودی در سایر کلاینتها نیز این مورد پشتیبانی میشود.
https://github.com/patterniha/Free-Configs</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/whitedns/1567" target="_blank">📅 03:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1566">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quk15MahgYwUVCROkUX0_5dhbMPq1SsxvAhk0g9b0oZuKnkqbzVbOEHP8J65adx8ITeAXmVXo32mT7NoJnuE56DzThdnUGAzIi-6DAuTFpc7AcJ5pU4RrQYgT-looVVPUYPvH1w8v69naM6rIRxH-tEGK6ufF82iaVpmCEdQAWnAhjERlAnPjbwvSSBAmCchu-bmogAKTE6NA6hK_Y7raKnSJFbVBsxWCqGJbivr2TOurYvszbpu2UhtY8VRUivVaoARKKsNc3F7zwiZwX0g2QNpK23BlZEQUMR0TekznSbf8tPIp49ejG82-jWzxCMUWecE5L7e_q1OTbQUef3kbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
WhiteDNS
مسیری که قبل از روزهای قطعی اینترنت شروع شد
تیم WhiteDNS از مدت‌ها قبل از قطعی‌ها و محدودیت‌های گسترده اینترنت فعالیت می‌کرد. از همان ابتدا تلاش کردیم ابزارها، سرویس‌ها و آموزش‌هایی بسازیم که رایگان و در دسترس همه باشند.
در این مدت افراد زیادی به این جمع پیوستند؛ بعضی ماندند و بعضی مسیرشان جدا شد، اما چیزی که ما را کنار هم آورد همچنان پابرجاست:
حرکتی جمعی برای دسترسی آزادتر به اینترنت.
تیم WhiteDNS تا امروز کاملاً مستقل و بدون هیچ منبع درآمدی اداره شده و تمام هزینه‌ها را خودمان پرداخت کرده‌ایم. با این حال، این مسیر را ادامه می‌دهیم و همچنان ابزارها و سرویس‌های رایگان بیشتری را با کمک همین جامعه خواهیم ساخت.
حالا تنها مسیر درآمدی ما کانال یوتیوب WhiteDNS است. اگر می‌خواهید از این حرکت حمایت کنید، کانال را سابسکرایب کنید و ویدیوها را ببینید. همین همراهی کمک می‌کند WhiteDNS مستقل، فعال و جامعه‌محور باقی بماند.
📺
https://www.youtube.com/@WhiteDNS
ممنون که بخشی از این مسیر هستید
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/whitedns/1566" target="_blank">📅 18:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1564">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/rNUmZQX07h6p8KHVwSEJLc-bezWOF34BN3dRQKH7FEKpf7aNWHuLMKitga47guOE5A5H00YlSTqu_ozK_Mun8lPvfYFuzQVo8z64DRchkwXZDvEiYJ4qeSFh9rfUU0BKfpA_g5p0_iW4h5EBRRG58gjXBFhkyBXPkTMJrduRC8Squ5zhVTgdq4fYHAK0JSAnnHMnXD1zs2h07jREIXPpbhq1fpAizC4tE2tYf2lCi2zA5YVHpUOeHKlWl4l8EHEnOI53fyj1upeIFw-FDUl3jNt0WQ-up0g8Z0cG9FnC9n_zwB_0jkeigCjYcOHrDShkTRnpvnHAi_P4SpJpi3_PGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/whitedns/1564" target="_blank">📅 17:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1563">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/776e6fda95.mp4?token=TYpXZ-45hAO8Vnybm_xjEzQ_GQ9nlv5d28-Eh3Zqw2c6klmFYFHIP6i2Ten4pfoOw7XT7oJHIImoU2s5pCwoNI77YFNrbAuZqa6vFInt5wmho78WtqqS2jd_ivs0V7yWB4slxv4Dfa9aU8-ezlnRXEqnVrExTxfvtn_WdrqojI3zp_7nW0JI0bo8d-zW2MqkifM_8avtza2Xa1p6H1_zXmyYuwMY0pGl1QEcDGHJZju7jd3gAxcm_F1dWAlJ0oES4wYDx8bBKEqwJbPGZ-9xgTU9eeXIYTPHiqvKTTXzPsvtSOj_bLPeoTM_6iS1MJhdjlrLaipgA5G7dNWrPOJ2mF6VKURh8i4b0rtvIDYlEgXhQxKqdaUPbX17v4u4k0pFIuTd5l2-zTd4tVe62DG6hO-t4rF-uWbsUZD7c-BYin-SXyXVR5fz5xo-huFY-iFE3vFTiQnEt4MqW5AOxT0mrhuEQI2NT5HrVi7Zo6QjLe10FAAfxVyT0cF3aRABdhvLU0gZ4ujv5tGtYlsJ5EbWJ3TAckTtgbtuXJgPjU0KY1B7UYCmEYa_WbDKMehHEXuW66Qufl5DyQh_uaJJ85K1I7DHB9IO-DMMPzED1Fu-fm178UJqQusL8coTO3NhFDZbuOo5VByneJopDhVXv2m4A30BjvemolB9PLrBBvbZiJs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/776e6fda95.mp4?token=TYpXZ-45hAO8Vnybm_xjEzQ_GQ9nlv5d28-Eh3Zqw2c6klmFYFHIP6i2Ten4pfoOw7XT7oJHIImoU2s5pCwoNI77YFNrbAuZqa6vFInt5wmho78WtqqS2jd_ivs0V7yWB4slxv4Dfa9aU8-ezlnRXEqnVrExTxfvtn_WdrqojI3zp_7nW0JI0bo8d-zW2MqkifM_8avtza2Xa1p6H1_zXmyYuwMY0pGl1QEcDGHJZju7jd3gAxcm_F1dWAlJ0oES4wYDx8bBKEqwJbPGZ-9xgTU9eeXIYTPHiqvKTTXzPsvtSOj_bLPeoTM_6iS1MJhdjlrLaipgA5G7dNWrPOJ2mF6VKURh8i4b0rtvIDYlEgXhQxKqdaUPbX17v4u4k0pFIuTd5l2-zTd4tVe62DG6hO-t4rF-uWbsUZD7c-BYin-SXyXVR5fz5xo-huFY-iFE3vFTiQnEt4MqW5AOxT0mrhuEQI2NT5HrVi7Zo6QjLe10FAAfxVyT0cF3aRABdhvLU0gZ4ujv5tGtYlsJ5EbWJ3TAckTtgbtuXJgPjU0KY1B7UYCmEYa_WbDKMehHEXuW66Qufl5DyQh_uaJJ85K1I7DHB9IO-DMMPzED1Fu-fm178UJqQusL8coTO3NhFDZbuOo5VByneJopDhVXv2m4A30BjvemolB9PLrBBvbZiJs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
یه آموزش خفن و کاملاً رایگان براتون داریم!
✨
اگه دوست دارید بدون هیچ هزینه‌ای با
پنل Netra
کانفیگ بسازید، این آموزش دقیقاً برای شماست!
💗
بدون هزینه
🎀
کاملاً رایگان
✨
آموزش مرحله‌به‌مرحله
🎥
آموزش کامل رو آماده کردیم و می‌تونید همین الان توی یوتیوب ببینید:
https://youtu.be/qluhGfGNbwk?si=oTLkVuC1z-5L03fy
💌
اگه آموزش براتون مفید بود، حتماً لایک کنید و برای دوستاتون هم بفرستید!
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/whitedns/1563" target="_blank">📅 15:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1560">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Fk2_hxAwelzgQtK8rZJE30qLjGs5Lbcu67YeZkN6sf-UBjoxRIM4GSuTey_nEFqtvfyKYNgN93PndyjGnhJqGFe9IrI5iXCsPAMCwsYySAiqn8daWwTxKHQpW2Rs5JTymdDulyCtcpDbJ8WVbcfr7ErxdeyaHgiImBIVV9W6wL9zquHYrBDKUgOsY4_cNAmpzriSEzA-Nlm_5-ncdMevBGJwyzucu2Czoj9vaiMRBxTDfVJBbr1zO0xBgtI1nsbIHxs4TgEyBGUHUP2uN8tsg1_Xbb9NLCPCjz-gHUAqv0akydmrpbh54RbZcjiYcxqJrJ_ytYFqYzz1DLh-vegtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteVPN Desktop v1.0.18
زنجیره کردن اتصال (Connection Chaining)
از این نسخه می‌توانید ترافیک را قبل از رسیدن به اینترنت از دو سرور رد کنید.
اتصالی که در صفحهٔ وی‌پی‌ان انتخاب کرده‌اید هاپ اول می‌شود، و سروری که در تنظیمات به‌عنوان هاپ دوم انتخاب می‌کنید جایی است که ترافیک از آن خارج می‌شود.
چطور فعالش کنم؟ تنظیمات ← زنجیره کردن اتصال ← هاپ دوم
پیش‌فرض روی «خاموش — یک هاپ» است و اگر دست نزنید، همه چیز دقیقاً مثل قبل کار می‌کند.
چند نکته که خودِ برنامه رعایت می‌کند:
▪️
سرور هاپ دوم از فهرست هاپ اول حذف می‌شود، تا هر دو سرِ زنجیره یک ماشین نباشند و بی‌دلیل هزینهٔ دو هاپ را ندهید.
▪️
اگر هاپ دوم WireGuard یا Hysteria2 (یا هر پروتکل روی QUIC) باشد، فقط سرورهایی به‌عنوان هاپ اول پیشنهاد می‌شوند که بتوانند UDP را حمل کنند. زنجیره‌ای که هاپ اولش فقط TCP باشد ساخته می‌شود و وصل هم می‌شود، ولی هیچ ترافیکی رد نمی‌کند.
▪️
حالت Automatic همچنان کار می‌کند. اگر هاپ اول قطع شود، خودِ گروه جایگزینش می‌کند و نیازی به اتصال دوباره نیست.
▪️
اگر سروری که به‌عنوان هاپ دوم انتخاب کرده‌اید بعد از به‌روزرسانی اشتراک حذف شود، همان‌جا در تنظیمات به شما گفته می‌شود — نه وقتی که دارید وصل می‌شوید.
⚠️
توجه: دو هاپ طبیعتاً کندتر از یکی است، چون هر سرور باید ترافیک سرور بعدی را هم حمل کند. اگر سرعت برایتان مهم‌تر از لایهٔ اضافه است، همان یک هاپ را نگه دارید.
دانلود: ویندوز (x64 / ARM64) · مک (Intel / Apple Silicon) · لینوکس (deb / rpm / AppImage / tar.gz)
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/whitedns/1560" target="_blank">📅 16:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1558">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/twihPMUVrkCGPSVT9p1hibEJ8fA10-cDISL6sUNa9HaXRx6Lr2ImJz-HSB0MpoRsrE2t-yi3N4wstcdHQiUVER0k-HNjSZQOiJAAXD0_-w7IH-tD5JBK6uRDEE-8aZYo6qPntYfolm2SyEzJqJ4G7Uxfd8hADBFj4PfS7UnrUxAcYgEiBfmLf31g6aLbLaOzhbQWEu2Pu0dQvzfULC5I0tVBVvETvU1IahGf5zwhZvndUoZKC63z4Z38sG7_dLfofdvov1HYW9e-_AmJFtrYbw5-BV6MGcrLyK174XWOMUa5UUSYejFJqDOVD4bKKHPyjsEh8gOLivA3r0X6ACkE4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther Android ورژن جدید
🔥
🔥
🔥
🔥
🔥
نسخه ۱.۲.۱ — رفع سه مشکل اتصال
این نسخه قابلیت بزرگ جدیدی نداره؛ سه تا مشکل رو رفع می‌کنه که باعث می‌شد اپ روی خیلی از گوشی‌ها اصلاً وصل نشه. اگه ۱.۲.۰ داری حتماً آپدیت کن.
🛠
چی رفع شد
1
.پروتکل های wireguard و warp in warp برای خیلی از دوستان اصلاً وصل نمی‌شدن
توی ۱.۲.۰ «ثبت‌نام مشترک بین پروتکل‌ها» رو به‌عنوان یک بهبود اعلام کردیم. اون کار اشتباه بود: وقتی MASQUE هویت رو ثبت می‌کرد، کلید WireGuard روی سرور Cloudflare پاک می‌شد. بعدش هیچ اندپوینتی جواب نمی‌داد و اپ می‌گفت شبکه بسته‌ست — در حالی که مشکل از هویت بود، نه از شبکه.
حالا هر پروتکل هویت خودش رو داره. اگه از ۱.۲.۰ آپدیت کنی حسابت از دست نمی‌ره.
⚠️
در عوض، اون کاهش سه‌برابری احتمال rate limit هم برگشت. اگه زیاد نصب و حذف می‌کنی، حتماً از
Settings ← Identity & access
یک بار بکاپ هویت بگیر.
۲
. عوض کردن پروتکل وسط اتصال، همه‌چیز رو خراب می‌کرد
اگه بدون قطع کردن اتصال پروتکل رو عوض می‌کردی، جستجوی اندپوینت از داخل همون تونل قبلی رد می‌شد — یعنی هزاران درخواست دقیقاً به جایی می‌رفت که قرار بود جایگزینش کنه. نتیجه: هیچی وصل نمی‌شد.
۳
. گیر کردن روی پروتکلی که شبکه‌ات بسته
پیش‌فرض قبلی H3 بود که روی UDP کار می‌کنه. اگه شبکه UDP رو بسته بود تلاش اول شکست می‌خورد و اپ دوباره همون رو امتحان می‌کرد. تا نوبت MASQUE H2 برسه چهار دقیقه و نیم گذشته بود، و عملاً هیچ‌کس این‌قدر صبر نمی‌کنه.
✨
چی جدیده
حالت Automatic — از
Routes ← Manual ← Protocol
گزینه اول حالا Automatic هست و پیش‌فرض هم شده. خودش سریع امتحان می‌کنه ببینه شبکه‌ات چی رو اجازه می‌ده، از H2 شروع می‌کنه (چون TCP روی پورت ۴۴۳ هست و شبیه HTTPS معمولی دیده می‌شه)، و هرچی جواب داد رو یادش می‌مونه تا دفعه بعد از همون شروع کنه.
روی نصب تازه: ۱۴ ثانیه تا اتصال، جایی که قبلاً چند دقیقه طول می‌کشید.
گزارش خطای واقعی — قبلاً اگه جستجو نتیجه نمی‌داد فقط می‌نوشت «اندپوینتی پیدا نشد». حالا می‌گه چرا: بسته‌ها از گوشی خارج شدن و جوابی نیومد (مشکل از شبکه‌ست)، یا اصلاً خارج نشدن (مشکل از مسیریابی خود گوشیه). لاگ خود موتور تونل هم از این نسخه داخل
Settings ← Diagnostics
هست — اگه مشکلی خوردی همون گزارش رو بفرست.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/whitedns/1558" target="_blank">📅 14:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1557">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/wBsthA23P0W73084HJpHvmX82NZyPHy6L7e-xql5QeGe0ukLMen4o1tYz_kKa9UblHzllBRo3yUCN0Ga4owkxmzfzrv9uaPQgsz61N59HepFC8f0DL2fTYfHBdhWlaPX8OSf-_IGiRQ246NYOerjmyHeoOC-KW1ZwELyUNiqrOI-GCna29AtgbqsCzF9HOeOpTJdMk4_RqlZTHBlWgDbQwcKfc1NK8oUmTFzgW4AP69fP80YGifbufEw3yYEuJsak7xEvmgFkC-dj-6ix7OGzAeQnuKSG7w8rH-JHl7YypR97gYX0Kn6RulXvE8wbACnCe6DI8kKNXlS0gEjEJf_Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/whitedns/1557" target="_blank">📅 14:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1556">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OFZ_BuoqO9j4tliMIxKBF1Mo19sAjZxm26KhTCCA29Xw9wQUca9AuZNNTSNQtEzzpuXBi8j4-oqptIFtBejt5okwB8_Yt12r3Bfng6_31wqZ3rpSxvFyDpPHTkzq11MyhW_U_jEaWTOjrK8cEiFiztHBSSfqJHk0QR6GJSQOmpXctu_rym9A24Onb8j_K8yVm3dt5p1kfCxTlX5uQNi_b5xKvLU_jEj9DZF88q2hmfMJSQ7apFzf3F2WbFqaHewMrPPk98cXMX4L57TZy-3e1PcuMjtS_-4pvbkAhon7ezAsuS2QGa7-RX3f4TtP-f7A7nM71pyQfwxSIokLUVzp9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی آزاد و امن به اینترنت با WhiteVPN (نسخه موبایل و دسکتاپ)
اگر به دنبال یک کلاینت یکپارچه، سبک و حرفه‌ای هستید، WhiteVPN با رابط کاربری مدرن در دسترس شماست!
⚙️
قدرت گرفته از هسته Mihomo:
این برنامه بر پایه هسته قدرتمند Mihomo (مشابه کلش و متا) توسعه یافته است که بالاترین سطح پایداری و سرعت را در دور زدن محدودیت‌ها برای شما فراهم می‌کند.
⚠️
توجه مهم:
این اپلیکیشن کاملاً سورس‌باز (Open-Source) است و در Google Play یا App Store منتشر نشده است. تنها منبع رسمی برای دانلود، مخزن گیت‌هاب پروژه است.
✨
ویژگی‌های کلیدی:
🔹
پشتیبانی همزمان از ویندوز، مک، لینوکس و اندروید
🔹
رابط کاربری ساده و اتصال تنها با یک کلیک
🔹
سیستم پراکسی جامع و تونلینگ کل سیستم (System-wide)
🔹
مدیریت پیشرفته سرورها و پایداری بالا در اتصالات
━━━━━━━━━━━━━━━━━━━━
📥
دانلود مستقیم آخرین نسخه از گیت‌هاب (رسمی):
📱
نسخه اندروید (Mobile):
🔗
https://github.com/WhiteDNS/WhiteVPN/releases/latest
💻
نسخه دسکتاپ (Windows / macOS / Linux):
🔗
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
برای دانلود، وارد لینک‌های بالا شده و از بخش "Assets" فایل متناسب با دستگاه خود (فایل apk برای اندروید و فایل‌های نصب برای ویندوز/مک) را دانلود کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/whitedns/1556" target="_blank">📅 14:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1555">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AikliaV7b_Xct0VFZiagc_v-KSXgBn4dq86U2rIYj2eeb3FULodfTcN3tppxXvpBvaXil8RtpeaInP8HQhX6aewVQPTID0V9rQRmUg64RP_wKppIppW1evjSGyhQhiem50Av2AooRXlgbi9wS3w2U5YqhVPm7MasQevzqlG5N-GaFVV4XlgGmH5AePDQLM3ykeL-3sVK5k3r4eLdb974jZ5GT-0SesQoOlEFgs9rMV-4JRAR5RPfr3ffPVzs3uI7ubVQMEQnVW26oKKURAPoPUQvw8EVvD9V5eO3zDQ_roZ2_IbR8RLc98c7HQk1psaitjOeGobsYkpzCXAtE78qpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
WhiteDNS
مسیری که قبل از روزهای قطعی اینترنت شروع شد
تیم WhiteDNS از مدت‌ها قبل از قطعی‌ها و محدودیت‌های گسترده اینترنت فعالیت می‌کرد. از همان ابتدا تلاش کردیم ابزارها، سرویس‌ها و آموزش‌هایی بسازیم که رایگان و در دسترس همه باشند.
در این مدت افراد زیادی به این جمع پیوستند؛ بعضی ماندند و بعضی مسیرشان جدا شد، اما چیزی که ما را کنار هم آورد همچنان پابرجاست:
حرکتی جمعی برای دسترسی آزادتر به اینترنت.
تیم WhiteDNS تا امروز کاملاً مستقل و بدون هیچ منبع درآمدی اداره شده و تمام هزینه‌ها را خودمان پرداخت کرده‌ایم. با این حال، این مسیر را ادامه می‌دهیم و همچنان ابزارها و سرویس‌های رایگان بیشتری را با کمک همین جامعه خواهیم ساخت.
حالا تنها مسیر درآمدی ما کانال یوتیوب WhiteDNS است. اگر می‌خواهید از این حرکت حمایت کنید، کانال را سابسکرایب کنید و ویدیوها را ببینید. همین همراهی کمک می‌کند WhiteDNS مستقل، فعال و جامعه‌محور باقی بماند.
📺
https://www.youtube.com/@WhiteDNS
ممنون که بخشی از این مسیر هستید
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/whitedns/1555" target="_blank">📅 10:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1553">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">WhiteAesther V1.2.0    دو پروتکل جدید، رفع مشکل قطعی، و مسیریابی اپ به اپ  از این آپدیت سه تا قابلیت جدید اضافه شده و سه تا مشکل قدیمی رفع شده. همه‌شون رو اینجا خلاصه کردم.
✅
چی اضافه شد  ۱. دو پروتکل جدید: WireGuard و WARP in WARP  تا الان فقط MASQUE (روی…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/whitedns/1553" target="_blank">📅 09:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1552">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fb57NQqspiAVOGVN075PfWyWavm1otxNtwlTLg64zMjZSyxHImpUzoHsaFF788dBUi3Q-xdEZOr_NNzDjaEfHuIsV3IPq2hnRwAWHaFEADdyeXoBkWTXvvSAdztXCrTRmrf_J9alc65vlCDJmvCAK7i8aTE4E0HZKskwFPYrzi48rj-U7d3MecXZxnUZxSJLzBSbwoL5MeHcEQbkxYfVCr1ti5x6chg8Z-BeI_mmvyPa-gfD4jmX2bZ0E5r6EVYR_7R8jQHFByVCTKWU60O7AUVGNVUqRu3BXar9XLZ8b16WzWeKQyz5z5SSgne7BPMRdfr9LFqvlvRxPj5KxMBRXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان عزیز
✍️
از دیروز گزارش های زیادی روی WhiteVPN روی گوشی های قدیمی گرفتیم که بهمون گفتید نصب نمیشه، یا نصب میشه ولی میزنید روی اتصال، اررور میگیرید.
ما سعی کردیم توی ورژن ۱.۶.۱ که از لینک زیر میتونید دانلود کنید این مورد رو حل کنیم.
حالا گوشی های اندروید قدیمی‌تر هم میتونن بدون دردسر وصل بشن.
همچنین مشکل کانکشن هایی که camouflage داشتند هم توی این ورژن حل شده.
تغییر دیگه،ای نداشتیم  جز این دو مورد.
دانلود آخرین نسخه
https://github.com/WhiteDNS/WhiteVPN/releases/latest
با تشکر
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/whitedns/1552" target="_blank">📅 06:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1550">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v6FrVZWEhNyCOWZ9HeMKpZJo0jjA5sRQBpNcXEUKCcv1ZxGxppc59tmVuhEUk_oNPJR15FGJ1IiZJ8DzS0ilhc-Yo_XlYtXCvfp4X-BgfKkWOVDOLWjCY5vtN64SBjDJwGuECmmP_tFVGfvFbspIergdcC0qtQqYrxhvgnr63_1PIs2nfxR2F8ITYds7FTRxtbODpdmdybjDCiR4YT61wFpA1Yw4TaqSCAZ1MLepBXV-wLkATsptDpmbuJTm2JcH9T2GQnzLJfdy8GyTkTCn2d3UotDsT177T3DvwmKkk_qvw-Gi1YyPK_g6mWKzzCfQ-FzDrnTk4G-oY3ATzsHWsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mgMtmAt1hRMWegI5vKQbtaGdwMaq6T4LM6xJY2b9ZDbnHpmqwWb4cm3I-scf4mAN9PijnN5EeSd4qIPJpNjdwahAJp5h2A5TixMPuSJumgrr6w1jZyUPTT2tI8I2w6bxybacJkzlwoARRObWTooV94tMWjqSkQLvADZIAfuzoqIJnL-IDiaHRyj4moFxe18b2Z2n9SijSrLuQMgvFfM_3DPESTBITkmZX70nXp70sScBakDle6BkZ76r7djyMfBD3GCkaxpCF_lnI3EgYTFGPueGxHE8krJDc9eEm4xq53wS3tWAnyLftrj8fBm57NBVAKcbrwraVGflJz0qbXmT7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان عزیز
لینک ساب رو باید بعد از کلیک کردن روی دکمه Raw مشابه به عکسی که گذاشتیم کپی کنید.
لینک
صحیح WhiteDNS Sub
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/whitedns/1550" target="_blank">📅 05:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1548">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCore Forge</strong></div>
<div class="tg-text">🚀
CoreForge Build آپدیت جدید منتشر شد
https://testflight.apple.com/join/DRkT6zny
این نسخه یکی از بزرگ‌ترین آپدیت‌های CoreForge تا امروز محسوب میشه.
از Build 90 تا Build 100 طی حدود ۲۰ روز:
• 214 Commit
• بیش از 411 فایل تغییر کرده
• بیش از 86,000 خط کد جدید اضافه شده
• چند Engine و Protocol جدید از پایه اضافه شده
• بخش بزرگی از سیستم Connection، Routing، Failover و Config Management بازطراحی شده
###
🧩
پروتکل‌ها و Engineهای جدید
🔹
OpenVPN
* پشتیبانی مستقیم از فایل‌های .ovpn
* UDP و TCP
* AES-GCM / AEAD
* AES-CBC برای بعضی سرویس‌های قدیمی‌تر
* TLS-Crypt
* Multi-Remote / Multi-Address
* Username / Password
* Client Certificate
* OpenVPN Subscription
* پشتیبانی بهتر از ProtonVPN، VPNGate، SoftEther و کانفیگ‌های مشابه
🔹
Tailscale
* اتصال مستقیم به Tailnet
* انتخاب Exit Node
* MagicDNS
* مدیریت Account داخل CoreForge
* امکان اتصال به Exit Node حتی بدون انتخاب Config معمولی
🔹
Cloudflare WARP / MASQUE
* WARP به‌عنوان یک Outbound واقعی
* MASQUE روی HTTP/2 و HTTP/3
* امکان استفاده داخل Chain
* WARP Endpoint Scanner برای پیدا کردن Endpoint بهتر
* تست Endpoint با handshake واقعی MASQUE، نه فقط TCP Ping
🔹
mKCP
* پشتیبانی از mKCP مربوط به Xray
* همه Header Typeهای اصلی
* قابل استفاده با VLESS و Trojan
🔹
ECH
Encrypted ClientHello حالا به صورت واقعی داخل CoreForge اجرا میشه و برای بعضی Transportها از جمله Hysteria2 هم اضافه شده.
###
⚡
Load Balancer و Failover
Load Balancer فقط اسم نیست و حالا Connectionها واقعاً بین Nodeهای انتخاب‌شده مدیریت میشن.
همچنین:
* Config فعال داخل برنامه نمایش داده میشه
* Exit IP بعد از تغییر Node آپدیت میشه
* Dead Server Detection سریع‌تر شده
* Backup Node از قبل آماده نگه داشته میشه
* اگر Config فعلی از کار بیفته، CoreForge می‌تونه بدون Disconnect کامل به Backup منتقل بشه
* Backup Pool بعد از Failover دوباره پر میشه
###
🌐
Routing
سیستم Routing هم تغییر زیادی کرده:
* Routing Profile شبیه Shadowrocket
* Rule Actions
* Iran Direct Preset
* Iran 2026 Rules
* category-ir
* Import کردن Routing Rules از فایل
* Fragment به‌عنوان Routing Target
###
📂
Configs و Subscriptionها
مدیریت Configها تقریباً کامل بازطراحی شده:
* Swipe برای Ping / Edit / Share / Delete
* Drag & Drop برای مرتب کردن Sectionها
* Groupهای Local
* Bulk Actions
* forge:// Chain Links
* Tap-to-Ping-and-Connect
* Import QR Code از داخل عکس
* Subscription Folder
* Rename / Reorder / Export
* Auto Update جداگانه برای هر Subscription
* Plan Status
* تقویم شمسی
مشکل فایل‌های OpenVPN بزرگ هم برطرف شده؛ برای مثال اگر یک فایل شامل ده‌ها یا صدها Profile باشه، دیگه همه‌ی اون‌ها به‌عنوان یک Config خراب Import نمیشن و Profileها جدا میشن.
###
🔧
Fixهای مهم
در این نسخه تعداد زیادی Bug مهم هم برطرف شده، از جمله:
* Crash روی تعداد زیاد Config
* مشکل Import بعضی لینک‌های VMessAEAD
* مشکل gRPC پشت Cloudflare
* مشکل XHTTP که Connect می‌شد ولی Traffic عبور نمی‌کرد
* مشکل REALITY و extra
* اصلاح UUIDهای VLESS
* Lag شدید Config List
* Writeهای اضافی Keychain
* آپدیت نشدن Connection Details بعد از Failover
* UDP برای VMess، Shadowsocks و SOCKS
* UDP Associate برای Trojan
* gRPC MultiMode
* pinnedPeerCertSha256
* PattNG Fragment / Cipher Suite / Unsafe Fingerprint
###
📱
iPad و UI
* پشتیبانی بهتر از Stage Manager
* Split View
* Resizable Window
* تغییرات Liquid Glass
* اصلاح Light Mode
* بهبود Tab Bar و Headerها
---
⚠️
نکته مهم درباره Build
این نسخه تغییرات خیلی زیادی داشته و طبیعتاً
۱۰۰٪ تضمین نمی‌کنیم که تمام قابلیت‌های جدید روی تمام Serverها، ISPها و Configها بدون مشکل کار کنند.
بعضی قابلیت‌ها هنوز در مرحله‌ی تست واقعی توسط کاربران هستن و ممکنه روی یک Server عالی کار کنن ولی روی Server یا Network دیگه Fail بشن.
به‌خصوص قابلیت‌های جدیدی مثل:
Tailscale / WARP / OpenVPN / ECH / Chainهای پیچیده / بعضی حالت‌های VLESS و REALITY
هنوز نیاز به تست گسترده روی Serverها و اینترنت‌های مختلف دارن.
پس اگر چیزی Connect نشد یا Connect شد ولی Traffic نداشت، حتماً گزارش کنید و در صورت امکان Config، Log و نوع اینترنت رو هم بفرستید.
Build بیشتر از اینکه «نسخه نهایی بدون باگ» باشه، یک جهش بزرگ برای CoreForge ـه و Feedback شما مستقیم روی Fixهای نسخه‌های بعدی تأثیر می‌ذاره.
🛠️
CoreForge Build
⚒️</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/whitedns/1548" target="_blank">📅 15:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1545">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/mNvVb3VAmSVzsJfICjbbRng9oNTH7aaSwjdQWj1hm_BO06-P1zKK9q5Xn7OCFCpOXMYQ8nIj7UQto2UY_R_EnAZtwO5rawf3pNJ-i5P0wscdg29EbgyXWLyTkemDyQ1C3sX_O_paoZ464lm8hxybjeq4eTri_w3n5_RBsP8zahpWQOpiUyAoefU5rmsflNo8dmYhQAS8dmvuuUZDmkl_Z9gx_JajrrlTapBn4l84qcCV2rkfCPLSHgsGjqE9-NbXpbL-MdRR3JsdDtPPX0sQy0ub-hw_I3J0N1v9ODthb7hymfTQYZQ3NDze8zQ9a1pW-H8LdlmJScZ9ZBfFo45Zcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther
V1.2.0
دو پروتکل جدید، رفع مشکل قطعی، و مسیریابی اپ به اپ
از این آپدیت سه تا قابلیت جدید اضافه شده و سه تا مشکل قدیمی رفع شده. همه‌شون رو اینجا خلاصه کردم.
✅
چی اضافه شد
۱. دو پروتکل جدید: WireGuard و WARP in WARP
تا الان فقط MASQUE (روی H3 یا H2) داشتیم. حالا از Routes ← Manual ← Protocol می‌تونی این دو تا رو هم انتخاب کنی:
▫️
WireGuard —
سریع‌تره، ولی روی UDP کار می‌کنه
▫️
WARP in WARP —
یک تونل داخل تونل دیگه، کندتر ولی شناسایی‌ش سخت‌تره
⚠️
هر دوی این‌ها UDP هستن. اگه شبکه‌ات UDP رو کامل بسته باشه (مثل همراه اول این چند وقت اخیر) اصلاً وصل نمی‌شن — اونجا MASQUE H2 که روی TCP کار می‌کنه انتخاب درسته.
۲. بکاپ هویت — راه‌حل قطعی مشکل «چند بار نصب کردم دیگه وصل نمی‌شه»
دلیل اون مشکل این بود که هر نصب، یک هویت تازه از Cloudflare می‌گرفت، و بعد از چند بار ثبت‌نام از یک آی‌پی، دیگه هویت جدید نمی‌داد. حالا می‌تونی هویتت رو قبل از حذف اپ ذخیره کنی و بعد از نصب مجدد برگردونی.
۳. Split tunnel — انتخاب اینکه کدوم اپ‌ها از تونل رد بشن
از Traffic ← Apps: همه اپ‌ها، فقط چندتا اپ خاص، یا همه به‌جز چندتا اپ خاص (مثلاً بانک یا اپ‌های داخلی).
🛠
چی رفع شد
▫️
ثبت‌نام مشترک بین پروتکل‌ها — امتحان کردن هر سه پروتکل قبلاً ۳ بار ثبت‌نام می‌خرید. حالا یکی مشترکه.
▫️
WireGuard و WARP in WARP دیگه روی "trying" گیر نمی‌کنن — از تا ۹ دقیقه بی‌نتیجه، به معمولاً چند ثانیه.
▫️
باگ ساب عوض‌شده که نودهای قدیمی رو نشون می‌داد — درست شد.
📌
آموزش: Split tunnel
۱) Traffic ← Apps
۲) یکی از سه حالت: All apps / Only these apps / All except these
۳) با سرچ اپ‌های موردنظر رو پیدا کن و سوییچشون رو بزن
برای بانک یا اپ داخلی: All except these بزن و همون یکی دو تا رو انتخاب کن.
📌
آموزش: بکاپ هویت
Settings ← Identity & access → Save a backup (قبل از حذف اپ) / Restore from a backup (بعد از نصب مجدد)
⚠️
این فایل مثل رمز عبوره، رمزگذاری نشده — جایی نگهش دار که رمز عبور نگه می‌داری.
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/1545" target="_blank">📅 12:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1535">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A84ybidWcWgmcFyv2OPChg_ZJr3idbBXAP74MiPNkmyUWfIilII7mSQIG1S91gvObNbHS0k0XDbZpz-BoivqUN9Ho5LsbFPoyOQ7DJT8dkB2k-DExkAsRxKk1sLbeBl9XMX_Ue8PjrPu73KVujdUjpKYsOCxhhpu73J_v-FZ7-AevTrAPqkLCmzwxJL5EB6QBbPqjW7YquCAiyKobY601M6cVsh6KkpNcE0BnQ0wMpxvWYVJ8WWph0Jc968Hz7pyEP7L9v61b4e5BpHoGDx8Uq9zhXegXmKKB2Ls1wqeSdryD_5fXBAJ9H5LuVVsVxs71rsAR8v-LAFlym5wrPQV3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN v1.6.0 منتشر شد
🚀
یکی از بزرگ‌ترین به‌روزرسانی‌های WhiteVPN آماده است؛ با امکاناتی که اتصال‌ها را قدرتمندتر، انعطاف‌پذیرتر و قابل‌کنترل‌تر می‌کند:
📺
پشتیبانی کامل از Android TV
🔗
زنجیره کردن دو اتصال برای امنیت و انعطاف بیشتر
🛡
پشتیبانی از
AmneziaWG v3
و تنظیمات پیشرفته WireGuard
📥
وارد کردن مستقیم لینک‌های
Hysteria2
و
WireGuard
⚡
تست اتصال‌ها از تمام سابسکریپشن‌ها
🌐
بهبود سازگاری، پایداری و رابط فارسی
اگر از WhiteVPN استفاده می‌کنید، همین حالا به نسخه
۱.۶.۰
به‌روزرسانی کنید.
این نسخه با کمک بازخوردهای شما ساخته شده است. اگر مشکلی دیدید یا پیشنهادی داشتید، حتماً در گروه با ما در میان بگذارید.
🤍
WhiteVPN v1.6.0 — دو مسیر، یک اتصال قدرتمندتر.
📥
Github Release
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.0</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/whitedns/1535" target="_blank">📅 09:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1534">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">از این به بعد کانفیگ های بیشتری داخل ساب ما خواهد بود.
هر ۳۰ دقیقه بیشتر از ۲۲۰هزار کانفیگ جدید تست میشن و خروجی اونها بین ۲۰۰۰ تا ۳۰۰۰ کانفیگ با کیفیت و سریع خواهد بود.
تعداد کانفیگ های حاضر: ۳۳۵۳
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1534" target="_blank">📅 07:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1531">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">https://github.com/iampedii/whitedns-sub
لینک ساب برای استفاده در برنامه های white</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/whitedns/1531" target="_blank">📅 18:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1528">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👆
whiteAesther  android V1.1.0
در این نسخه از اپ اندروید شما میتونید با  قرار دادن یک کانفیگ ای پی خودتون را ثابت کنید و احتمالا خیلی از مشکلات مربوط به Gemini , Chatgpt و بقیه هوش مصنوعی ها و وبسایت هایی که روی لوکیشن حساس هستند  حل خواهد شد
نکته  خیلی مهم برای نسخه اندروید :
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
بسته به نوع کانکشن و موارد دیگر ممکن هست 1-5 دقیفه بار اول طول بکشه که شما موفق به اتصال بشید . ولی در دفعات بعدی این موضوع خیلی سریع خواد بود .</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/whitedns/1528" target="_blank">📅 17:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1527">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">WhiteAesther
android V1.1.0
🔥
🔥
🔥
🔥
🔥
🔥
قابلیت Exit Chain
از این نسخه می‌تونی بعد از تونل، یک ایستگاه دوم اضافه کنی.
یعنی چی؟ تا الان ترافیک تو از سرورهای Cloudflare بیرون می‌رفت و سایت‌ها آی‌پی Cloudflare رو می‌دیدن. حالا می‌تونی سرور شخصی خودت (یا سابسکریپشنی که داری) رو آخر مسیر بذاری، و سایت‌ها آی‌پی اون سرور رو ببینن.
مسیر ترافیک این شکلی می‌شه:
گوشی ← تونل رمزنگاری‌شده ← سرور خودت ← اینترنت
به چه دردی می‌خوره؟
▫️
سایت‌هایی که آی‌پی‌های Cloudflare رو بلاک کردن (بانک‌ها، بعضی سرویس‌های خارجی، بعضی بازی‌ها)
▫️
وقتی به آی‌پی یک کشور مشخص احتیاج داری
▫️
و مهم‌تر از همه: اگه شبکه‌ات اصلاً تونل رو بلاک کرده، می‌تونی تونل رو دور بزنی و مستقیم از سرور خودت استفاده کنی
پروتکل‌های پشتیبانی‌شده: vless vmess trojan shadowsocks hysteria2 و بقیه — چه لینک سابسکریپشن، چه کانفیگ تکی که دستی می‌چسبونی.
📌
آموزش — ۵ قدم
۱) اپ رو به نسخه ۱.۱.۰ آپدیت کن.
۲) برو به تب Routes ← گزینه Exit chain.
۳) کلید Exit chain رو روشن کن.
۴) توی کادر Add a subscription لینک سابسکریپشنت رو بذار و Add رو بزن. اگه فقط چند کانفیگ تکی داری، از Paste nodes by hand استفاده کن — هر کانفیگ توی یک خط.
۵) برگرد به Home و وصل شو. تمام.
⚠️
سه نکته که حتماً باید بدونی
۱. لیست سرورها فقط بعد از وصل شدن میاد
قبل از اتصال قسمت Nodes خالیه و این ایراد نیست. سابسکریپشن تو از داخل تونل دانلود می‌شه تا شبکه‌ات نفهمه داری چی می‌گیری. پس اول وصل شو، بعد برگرد به Routes ← Exit chain تا لیست سرورها رو با پینگ‌شون ببینی.
انتخاب سرور قطع و وصل نمی‌خواد — روی همون اتصال جابه‌جا می‌شه.
۲. گزینه Dial nodes through the tunnel
پیش‌فرض روشنه و بهتره روشن بمونه: شبکه/اپراتور تو هیچ‌وقت آدرس سرورت رو نمی‌بینه، و سرورت هم آدرس واقعی تو رو نمی‌بینه.
🔸
ولی اگه اپ اصلاً وصل نمی‌شه یا خیلی طول می‌کشه، این گزینه رو خاموش کن. اون‌وقت WhiteAesther تونل رو کامل رد می‌کنه و مستقیم به سرور خودت وصل می‌شه — دقیقاً برای شبکه‌هایی مثل همراه اول که تونل رو می‌بندن، همین حالت جواب می‌ده و خیلی سریع‌تر هم وصل می‌شه.
۳. Coverage باید روی Whole device باشه
توی تب Traffic. اگه روی Proxy only باشه، Exit chain کار نمی‌کنه و اپ بهت تذکر می‌ده.
💾
حجم اپ بیشتر شده
از حدود ۸ مگابایت رسیده به ۴۷ تا ۵۷ مگابایت. دلیلش موتور جدیدیه که این قابلیت رو اجرا می‌کنه. اگه Exit chain رو روشن نکنی، اپ دقیقاً مثل قبل کار می‌کنه.
▫️
arm64-v8a — تقریباً همه گوشی‌های ۲۰۱۷ به بعد. از این شروع کن
▫️
armeabi-v7a — گوشی‌های قدیمی‌تر و اقتصادی
▫️
universal — اگه مطمئن نیستی (حجمش سه برابره)
⬇️
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
اگه مشکلی خوردی، از Settings ← Diagnostics گزارش بگیر و بفرست — از این نسخه لاگ موتور Exit chain هم داخلشه.
@whitedns</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/whitedns/1527" target="_blank">📅 17:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1526">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">📺
خبر خوب برای کاربرهای Android TV
در ورژن بعدی WhiteVPN پشتیبانی کامل از Android TV اضافه شده. تا فردا نسخه جدید اپ اندروید هم ریلیز میکنیم
❤️</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/whitedns/1526" target="_blank">📅 17:34 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
