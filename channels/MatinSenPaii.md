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
<img src="https://cdn1.telesco.pe/file/cG-RrCSHSl5ymus4lt1C0L80nWj5gmnlCgfnpH84UicjwbDQ9ElBKqtqOjKzBQEQA5f0Js9cHmHLnqShO1pvSoJlIG50Df2slaJIgk6bJj3JDT6UYxn--L4a72y4jV7wKHqNVv8pgxQOpZMSVlaV2KJSDh-zy6JZKlFrizY9Zye_YXDKvD1i7hk_DgdK2YrpK7r81JWhbblcAOrR_WK57DfF89UUstPPBVjq6vy-biF13R9C1G4jN-z1UUnpLd-Q09cqUqk8gq_Ng1FqSBSvo-oFY1x3iqVLRMhy73NVO8IVd5lhRIfyFRt_IEMX9ZZDO3Q4D61-sp6aKQpV8-X-AA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 161K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 15:53:56</div>
<hr>

<div class="tg-post" id="msg-3961">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rJjQl8ibcwvKHeDkdwIfzpUf0VlDD2sXcIDQKPUdIyknPoWd5k_jWKIy9j3pur1Be7wR-97g6NHZ9yfbUXk64YFY0591Atn-ZvPmhRd9Sr_PjK5xOb02wQv2bFCEO173uf8JSalgrGTWFh4MCoYf9UB2Q-Pa-qQA-Wd-GrMoxNmwUz8HD6BH3H5TnP104qc1sOgNQbNXSn6g7QNhMCLGwlYH_z_ri6di5GE7zlSAzkE3IOxOMoQCEl-pmTr5rI3MIq0wEcSwQ7b95TPYf8AV7VLNIR8_SKmgIp64ZAtSl0tbWfHgc2e71mlyugYiF7-WnDfjYAeMVljQTK4Rj61DAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
✅
نسخه‌ ۲.۲.۱ BPB Wizard منتشر شد.
۱. قابلیت اضافه کردن چند اکانت کلادفلر به Wizard اضافه شد. این قابلیت برای بچه‌هایی که اهدا میکنن و تعداد زیادی اکانت دارن خیلی کاربردیه.
۲. اسکریپت نصب خودکار برای macOS هم از این به بعد قابل استفاده هست.
✍️
بیا پایین بچه
آموزش استفاده از ویزارد رو قبلا ضبط کردم:
https://youtu.be/uCRKnrQEQYU</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/MatinSenPaii/3961" target="_blank">📅 14:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3960">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/MatinSenPaii/3960" target="_blank">📅 12:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3959">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-text">اگه میخواین بدون VPN، به سایت
x.com
(یا توییتر سابق) دسترسی پیدا کنید، کافیه این گام‌ها رو طی کنید:
1️⃣
وارد این مسیر بشید:
C:\\Windows\\System32\\drivers\\etc
2️⃣
فایل
hosts
رو با Notepad باز کنید
3️⃣
انتهای فایل، این خطوط رو اضافه کنید:
104.19.229.21 abs.twimg.com
104.19.229.21 x.com
104.19.229.21 ads-api.x.com
104.19.229.21 pbs.twimg.com
104.19.229.21 api.x.com
میتونید بجای استفاده از 104.19.229.21، هر IP مربوط به cloudflare که تمیز هست، استفاده کنید
4️⃣
فایل رو ذخیره کنید
5️⃣
مرورگرهاتون رو ببندید و دوباره باز کنید و
x.com
رو جستجو کنید (بسته شرایط اینترنت‌تون، ممکنه مجبور بشید که چند بار صفحه رو reload کنید
⚠️
توجه داشته باشید که در این روش، ممکنه
x.com
(یا توییتر سابق)، شما رو با IP خودتون شناسایی کنه، چون که شما بدون سرور واسطه ممکنه متصل بشید (به
این دلیل
از کلمه‌ی "ممکنه" استفاده کردم).</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/3959" target="_blank">📅 10:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3958">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وقتی اینترنت گوشی رو Share کرده بودم برای لپ تاپ، بدون VPN، بهم آپلود 0.02 مگابیت میداد. اما همین رو وقتی با کابل و PdaNet+ اینترنتش رو share کردم، سرعتش شد 2 مگابیت. یعنی صد برابر
امتحان کنید شما هم، شاید همین اتفاق واستون افتاده باشه</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/3958" target="_blank">📅 09:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3957">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vQoFE51j4VVPmdf5eJ-Iu3vmPONB7cTx7dzmJ_NCDH0anKbQBjaHcMqZ4DJK7Vtg-TCQnjQpUaOUQLQb_IOQkZ8lcG5mO5sxLesw6T1c6TryzhPywEM3H8bf4H7tpX36DZpHPmWuLP4QandfAuA63H0qvNeUd8L2YqaVn7xp20kHtOCdb-ahFNQ8CvF3ZmsgJF0KdDvZ010BqQNo3RM2svh5elV2T5IeBKQ4g_vpNVZsFsykPqAM0lszw2eNzFXbpqv3LAw2GpgtbUl9aigV8IxjKbm4_PnqcRpQtKgvOzlVKEGRR-58EH6h1ZvhrNtxlUxAWj7y-hyFWDw5om4vQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل در حال آماده‌سازی یک «ارتقای مغزی» بزرگ برای هوش مصنوعی خود است.
تصور کنید یک کارمند بسیار باهوش دارید که گاهی در کارهای طولانی «تنبلی» می‌کند یا برخی جزئیات تصویری را خوب نمی‌بیند؛ حالا نسخه 3.5 قرار است مثل یک متخصص ارشد عمل کند که نه تنها چشمان تیزبینی دارد (درک بصری قوی)، بلکه می‌تواند مستقیماً نقشه‌های مهندسی و کدهای ظاهری وب‌سایت (SVG) را طراحی کند. این ابزار برای کسانی که می‌خواهند از یک ایده خام به یک محصول دیجیتال واقعی برسند، حیاتی است. اهمیت آن در این است که فاصله بین «فکر کردن» و «ساختن» را به حداقل می‌رساند، هرچند که احتمالاً برای این هوشِ برتر، باید هزینه بیشتری بپردازید و با قوانین سخت‌گیرانه‌تری (فیلترهای امنیتی) کنار بیایید.
نشانه‌های فنی در زیرساخت‌های گوگل تایید می‌کند که Gemini 3.5 Pro در یک قدمی عرضه جهانی قرار دارد.
این مدل که به عنوان پاسخی به نیاز بازار برای «هوش عملیاتی» شناخته می‌شود، بر سه محور اصلی متمرکز است:
تقویت بینایی ماشین
استدلال چندوجهی (درک همزمان متن، تصویر و صوت)
جهش در تولید کدهای گرافیکی مانند SVG (فرمت برداری برای طراحی وب)
گوگل در این نسخه، «دقت جراحی» را جایگزین «تنبلی مدل» (تمایل هوش مصنوعی به کوتاه کردن پاسخ‌ها در وظایف طولانی) کرده است.
با این حال، این پیشرفت بدون هزینه نیست؛ گزارش‌ها حاکی از آن است که کاربران با یک «قیمت گزاف» روبرو خواهند شد که این ابزار را از دسترس عموم به سمت بخش‌های تخصصی سوق می‌دهد.
همچنین، اعمال فیلترهای محتوایی شدیدتر، نشان‌دهنده هراس گوگل از سوءاستفاده‌های احتمالی است. در واقع، گوگل در حال بومی‌سازی مفهوم «شاگرد اولِ سخت‌گیر» در دنیای سیلیکون است؛ مدلی که همه چیز را می‌بیند و می‌سازد، اما تنها در چارچوبی که معمارانش تعیین کرده‌اند و با هزینه‌ای که هر کسی توان پرداختش را ندارد.
✍️
Gratomic AI Bot</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/3957" target="_blank">📅 08:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3956">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کافیه یه آیپی تمیز بذارید توی بخش Advanced, ip fronting
زیر ۲ ثانیه کانکت میشه</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/3956" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3955">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه • ظاهر اپلیکیشن تغییر کرده  • امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.  • پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.  • با کمک یکی از بچه های…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/3955" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3950">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3950" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/3950" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3949">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slNx6JgRZpHEAKei4DNkSNhpiAC1j4FEymFfJrBgyAf0DYI83MbEZBAnN-NoLpZFMR1CGY0xERG9QgZc2TQNr1k92o8VgolTX_3cj_YJXMz7ijoWunGBCJtaGvCVQGrzMxMqN5R0OkCHDAuaJUNLxEZxYgsr3ZpJnpjDfCmlIQPEg7MJqZ7il7GbzdD7L6XRjgOuwRmMYHFovjIGFN8Kem79gmVlbWNA9g8VulMldhOYs-Tl0atsgdmwLp9RG18oDwRsiRTKNDO5vtwE5qxlkC0qUu6veDcz-mufkm91jnNyywMuPMPRw8bxyB3Vn3B7E9_jE6_Qu3RkuDAvmoiyEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه
• ظاهر اپلیکیشن تغییر کرده
• امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.
• پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.
• با کمک یکی از بچه های گروه، یکسری از مشکلات امنیتی اپلیکین رفع شده.
💬
اگر براتون وصل نمیشه، فقط و فقط مشکل از شبکه شما هستش. آی پی تمیز پیدا کنید و داخل فیلد IP Fronting قرار بدید و براتون کار میوفته.
@WhiteDNS</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/3949" target="_blank">📅 18:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3948">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3948" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/3948" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3947">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kmTL0sg_B-qSPZvQiTQrSmzyv0KNsSPAXZrbyV2x0PZ7fa6ntwNZUd4bHcLJIXffe5nEd3HU_-8i734coL8_TvC8nyMJZl9kX0YGRHof8B-3wpdHksPYCEK8KKZ2Hlz-vls2IOIOAfczwe3eW0EBx0m3QZSjoAImgdecf_1a0XfluShTrt6bbWK8NTCeu6A6QMcXuN7T-fDZhjYidX6KYycEzjTyHbwDNsri1iFOI9wLshZyb1zRR6trwOBamDumTdQ2SO6ZfaRcA1yc7k_9wM_yiHjXyF2cm9ylvQluLvbTWggpL8JKjdpbAktd71tv03srgfJjDOsYuGRzVhKcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از contributerهای پروژه‌ی senpaiscanner، دوست عزیزمون hidden-node، نسخه‌ی اندروید اسکنر رو توسعه دادن. طرز کارکردش دقیقا شبیه به اسکنر دسکتاپه. نصب کنید و یه تست بکنید
👇</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/3947" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3946">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">✍️
دوستان برای جلوگیری از هرگونه سردرگمی، ما در حال حاضر سه اپلیکیشن مختلف داریم:
🛡
۱. WhiteDNS Application
این اپلیکیشن بر پایه‌ی MasterDNS ساخته شده و مخصوص زمان‌هایی است که فیلترینگ و اختلالات اینترنت خیلی شدید می‌شود.
در شرایط عادی فعلاً کاربرد خاصی برای استفاده روزمره ندارد.
🛡
۲. WhiteDNS VPN
این یک اپلیکیشن ساده‌ی VPN برای کاربران اندروید است.
اگر فقط می‌خواهید راحت وصل شوید، این گزینه برای شماست.
🛡
۳. WhiteDNS BPB
این اپلیکیشن برای ساخت و راه‌اندازی BPB روی گوشی اندروید است.
یعنی بیشتر برای کسانی است که می‌خواهند خودشان یک پنل BPB بسازند و مدیریت کنند.
🛡
۴. WhiteDNS Installer Bot
آیدی بات:
@WhiteDNS_installer_bot
در این بات می‌توانید کارهای زیر را انجام دهید:
• نصب MasterDNS Server
• دریافت لیست IPهای سفید Cloudflare
• دریافت کانفیگ رایگان VLESS
• تبدیل کانفیگ‌های خودتان به کانفیگ‌هایی که پشت IPهای سفید Cloudflare قرار می‌گیرند
🛡
۵. WhiteDNS Installer Wizard
لینک گیت‌هاب:
https://github.com/iampedii/WhiteDNS-Wizard
این ابزار برای کانفیگ خودکار سرور شخصی شما استفاده می‌شود.
با استفاده از آن می‌توانید سرور خودتان را همراه با پنل شخصی 3X-UI راه‌اندازی و تنظیم کنید.
❤️
یک نکته مهم:
اینکه اسم برند ما WhiteDNS است، به این معنی نیست که همه‌ی سرویس‌ها و اپلیکیشن‌هایی که می‌سازیم حتماً بر پایه DNS هستند.
ما از اسم WhiteDNS به عنوان نام برند استفاده می‌کنیم، اما راهکارهایی که ارائه می‌دهیم می‌توانند VPN، BPB، MasterDNS یا تکنولوژی‌های دیگر باشند.
@WhiteDNS
🌎</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/3946" target="_blank">📅 12:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3944">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KdwH0gg21gBOe7So8px4_QBoqE7RLazto4DX5tyOZUsRp5zENuZeUrq2UgjARTMMbQ5-fJAqwnHtHPC_hD1DU44qIdGHzf2MDP6wP3sXIaSDYTR2TUHdw7U_ERcrciv1GNK0hHQNWyBAkXLpUlvXSMAW__pwcrxdwidpBlqV71d3_ZFYvUnns-sFyAB31qGkl6mXWMsoNOfk8pMXryayBCUMiS5eQ3CUKz4lXEGgudsJEkJoC1bQthep9UPa7VN1zsRbJfhbceqj2ocKkfdlI4dzcW7YNNweg0Gff3mJ6iJa7-alHq5Xw4_-AX_hrKMY86oVqRVWEfuPvY137g5HdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S3fdlhfpqfnDdygmwb7Y3rEkz0x8EK1C-kT_Lm_ScdXEZ7hjbr7YEyFlUy0I4hgnM6WPSRjHrvb91DKliekyPohePdMG06v2gxj1AtkGgv3d2pAfFO8p5LoERNGPdPcpTQalAWnV0tis_4_0nZDLYiqbdnzLlte7zmxXCRrXunXrrFn3-s57TwgYFomISRqVTAFcarvrFbPREpEuzP-9-Tp7hJnhPqLYZ2-78Fx9LBWGwWEiqbt1FjWcuAfDCV--_TB3aHvxF5THqoMjAsP6uGyiEy8ybcvcqi6x8zm4hp3XF8Es3Iew67Ugnxtuavw8ubafBBzZFmXNnrvPubOhuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از بچه‌ها اینو واسم فرستاد و گفت گویا V2box، به صورت آزمایشی SNI-Spoof آورده. یه تست بکنید ببینم داستان چیه:)</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/3944" target="_blank">📅 00:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3943">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">دوستان عزیز
❤️
در چند روز گذشته متوجه شدیم که بعضی افراد و کانال‌ها، به جای همکاری و ساختن، مسیر تخریب و سوءاستفاده را انتخاب کرده‌اند.
این افراد که ظاهراً در فضای اینترنت آزاد و کانال‌های مشابه فعالیت می‌کنند، برای جذب مخاطب بیشتر حاضرند هر کاری انجام دهند؛ حتی اگر نتیجه‌ی کارشان آسیب‌زدن به پروژه‌هایی باشد که با زحمت و هدف کمک به کاربران ساخته شده‌اند.
چند روز پیش اپلیکیشن WhiteDNS VPN را معرفی کردیم؛ اپلیکیشنی که هدفش این است کاربران بدون نیاز به تنظیمات پیچیده، فقط با زدن یک دکمه به بهترین کانفیگ‌های آماده و تست‌شده‌ی ما وصل شوند.
اما متأسفانه برخی کانال‌ها شروع کرده‌اند به استخراج کانفیگ‌های داخل اپلیکیشن و انتشار آن‌ها خارج از برنامه.
دوست عزیز، اگر مسئله فقط بستن مسیر دسترسی شما بود، ما ده‌ها راه برای رمزنگاری، تغییر مدل درخواست‌ها و محدود کردن این رفتارها بلد بودیم. اما شرایط اینترنت آزاد و محدودیت‌هایی که کاربران با آن درگیرند باعث شده ما تا حد ممکن ساده، باز و قابل استفاده طراحی کنیم.
مشکل اینجاست که همین رفتارهای مخرب در گذشته به پروژه‌های خوب و ارزشمندی مثل Slipnet ضربه زد. وقتی هر ابزار مفیدی به جای حمایت، هدف استخراج، کپی و سوءاستفاده قرار بگیرد، در نهایت انگیزه و امکان ادامه دادن از بین می‌رود.
واقعاً هدف چیست؟ آن کانفیگی که با زحمت استخراج می‌کنید، همان چیزی است که بخش زیادی از آن در لینک‌های ساب ما هم وجود دارد. چیزی که روزانه هزاران نفر را متصل نگه می‌دارد فقط یک لیست کانفیگ نیست؛ پشت آن اسکنرها، تست سرعت، بررسی مداوم، فیلتر کردن کانفیگ‌های خراب و یک سیستم کامل قرار دارد.
ما این ابزارها را در مدت کوتاهی، با انرژی و فشار زیاد ساختیم تا به کاربران کمک کنیم. لطفاً به جای تخریب، کپی‌برداری و گرفتن انگیزه‌ی تیم، سازنده باشید.
ما از نقد، همکاری و حتی پیشنهادهای جدی استقبال می‌کنیم؛ اما سوءاستفاده از ابزارهایی که برای کمک عمومی ساخته شده‌اند، نه کمکی به اینترنت آزاد می‌کند و نه به کاربران.
اجازه بدهید این مسیر ادامه پیدا کند.
✍️
@WhiteDNS</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/3943" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3942">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">این پست سگاروی عزیز رو بخونید، و اگر دوست داشتید همکاری کنید:
https://t.me/AiSegaro/120</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/3942" target="_blank">📅 18:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3941">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-text">تیم داشته باشم، دوست دارم از خودِ شما کمک بگیرم. اگر دانشجو یا دانش‌آموز هستید و مهارت ترجمه دارید، این می‌تواند یک
کار نیمه‌وقت منعطف
برای شما باشد تا در ازای کمک به ترجمه و ادیت، درآمد کسب کنید. آیا این مدل همکاری برایتان جذاب است؟
هدف من این است:
سریع‌تر به محتوای آموزشی مورد نظرتان برسید.
هزینه‌ها برای هر نفر ناچیز باشد (پول یک قهوه!).
بالاترین کیفیتِ ممکن (ترجمه انسانی) را تحویل بگیرید.
یک زنجیره همکاری برای دوستانی که دنبال کار نیمه‌وقت هستند ایجاد کنیم.
هر پیشنهادی در مورد نحوه قیمت‌گذاری، فرمت‌ها و اجرای بهتر دارید، در کامنت‌ها بنویسید.
من تک‌تک نظرات شما را می‌خوانم تا بهترین مدل را برای شروع استارت بزنیم.
این فرصتی است که با هم یک کتابخانه آموزشیِ قدرتمند بسازیم!</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/3941" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3940">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1e7OiFXHrdJiBMhljyFZJ6KvEiozY1ed-06SNMQbb6LR-YroYaR5bHepeeV-sPvBsP1AV-av_c7Q7JslOc6B8NUZ95Q4M84fIq_DQzMQsK8sqs8kwJD5ZJo0M8G9rZAH7QQnQitk-dDnw7tWIPiLRwvZ8gFqToIvsrszKPBmD9JKWbRob1hlbG9UkEtnQogWjF-LXDphGvh8VulAYq2c6PC8iBM71wEVN_fAf9tteBtuxvZpMYX5KWCB86E6Ixzw92oTKxtk7PdV91E7pRL8xbkMemwzbKgc80ZVqNXDG9Sin6YEv4k9IEvR8Srk7OWJt0wE9S4KQdu1S2AQ_wIfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همگی، یک پیشنهاد ویژه برای دسترسی بهتر به محتوای آموزشی!
همان‌طور که می‌دانید، درخواست برای ترجمه و زیرنویس کردن ویدیوهای یوتیوب، یودمی و کورسرا زیاد است. از آنجایی که کیفیت و دقت برای من خط قرمز است، فرآیند آماده‌سازی ویدیوها (ساخت زیرنویس، ترجمه دقیق و ادیت) بسیار زمان‌بر است.
برای حل این چالش، قصد دارم یک
«کانال مستقل»
برای مدیریت درخواست‌های شما راه‌اندازی کنم تا با مدل
«مشارکت جمعی» (Crowdfunding)
، ویدیوها را به صورت عمومی و با کیفیت بالا آماده کنیم. در این مدل، به جای اینکه یک نفر هزینه کامل را بدهد، با مشارکت چند نفر، ویدیو برای همه آزاد می‌شود.
اما قبل از شروع، می‌خواهم «شما» تصمیم‌گیرنده باشید.
برای اینکه این سیستم عادلانه و دقیق باشد، دوست دارم در مورد جزئیات زیر در کامنت‌ها با هم صحبت کنیم:
مدل هزینه‌کرد:
به نظرتان چه مبلغی برای «مشارکت جمعی» منطقی است؟ (پیشنهاد شما برای ویدیوهای زیر یک ساعت و بالای یک ساعت چیست؟)
فرمت خروجی:
ترجیح می‌دهید فایل زیرنویس (SRT) را جداگانه دریافت کنید یا ویدیویِ چسبیده شده (Hardsub) که آماده پخش است؟
یک فرصت برای شما:
اگر تعداد درخواست‌ها زیاد شود و نیاز به</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/3940" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3939">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P0Wuefc7QwaNEheIsFKe8PCfv5KeL4JE5L0O3J3GiyJKwu9qpLM9J2yKwfpwgQ0eIObv50SKpHGKK_ZMFpRLnY3EQprg__vYxEXIzRXgbRQxNNeKm2sPnyyULsBB7sY4xL3Y3_rxLDrJ5E8roeXcJhO4zWpGFJ_AX5ihE5j7-kaj5upGljkpXzIe56u97J6tm4KGmQYKiWTsSiWKOfnqJKGCCb8kZOT1IVu4OZXuDZlaoxQNmLUpDRLEwH9bxANZePAQ4bAGPMviwUPydSgKZsr_soLu4bvHz50PHTiHxmxqT6flznn2acv9EPJNUxyixnaFukoerTxOd-c_hWCEvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی از دوستان این مشکل رو داشتن که تلگرام واسشون باز می‌شد، هیچی دیگه باز نمی‌شد. یا یوتوب و ... باز نمی‌شد   مشکل احتمالا از کلاینتتونه و dns اش. باید تشریف ببرید توی تنظیمات v2rayng و Domestic DNSرو از چیزی که هست، به 9.9.9.9 و یا 9.9.9.12 تغییر بدید. همینطور…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/3939" target="_blank">📅 17:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3938">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XX2UDc0OvlWTRBsWRiUuLJ15w3fYFbpf3TUDuwc6LzgPSCjP2YEPWfqL3IBjamsqXvbItnoF9UhkAXLcxhcbKv1_GoEOSHdVIaop9cNyrkp63X3MWEAH0wkSsEQNBuwt1HHYQy5wSBTokiB_tUTfqws_kT_4KzRAZrYld8D5Hen8xT181sAVOIvgsjFr35YShq4jQkjJ9F4KZNPQE_Nsm_nnrWdwAsG5N2ZR9YsImJz6a1N8WY1in2j7GhOntR4cYLlSq1ktEeLADH73mw_uZtOltpTqTssBeL9spMeaK1Z0Y9_uPj7s9nak1O9ch6AgMADeLXiAmYMnsn2s3MTJYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
بدون دانش برنامه‌نویسی و کاملا رایگان، اپلیکیشن اندروید بساز! (فعلا اپلیکیشن ساده
😁
)
⚡️
لینک‌های استفاده شده توی ویدئو:
1- خود AiStudio گوگل:
https://aistudio.google.com
2- پرامپت ساز ریک:
https://chatgpt.com/g/g-6a319e2a22648191836468df375a3763-prmpt-sz-ndrwyd
⭐️
توی این ویدئو:
1- بهتون نشون میدم که چطوری می‌تونید از یه پرامپت ساده، یه اپلیکیشن ساده با تم دلخواه تحویل بگیرید
📲
2- توی مرورگر، Emulator اندروید بالا میاریم و با اپلیکیشنمون کار می‌کنیم
🏆
3- و در نهایت، اپلیکیشن رو مستقیم روی گوشیمون نصب می‌کنیم!
📱
🤎
اسپانسر ویدئو:
خانه EB، خیریه حمایت از کودکان مبتلا به ای‌بی و بیماران پروانه‌ای:
https://ebhome.ngo
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/3938" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3937">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ویدئوش آخرای ادیتشه
🔋
می‌ذارم تا ظهر</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/3937" target="_blank">📅 10:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3934">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KcwsuP5Xy-hoBJhSg5kwsCF288jKBOD1Uk8NyuKeoZ_7yNO7EeHTG6VNcUsCe-mac3Hja8u5QfUkgTrdqvsDca7rxvFqAUUFHp2ZQzuwht9PdGWtURJ8CVziXWRZeUAiZ9HQArwj4YgqKC3kTLhu3w9x3Na7RXtfItSAynA3djM0JGfrI8tPcegCL98F-pgLrJpYPC9ZBvodq7p6VPmEWxZEsuN92YAosjqpIPFSHv6A9A8bQulNGfs3kYt_APAqomTZSeUBnvBggnqwhWNckKNGaiXliSHX8G2DRXkOkLfABMODnwXczCyJObn03HWGQuRT1oEiNyo-o9CjzKJzEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o_aCfDaOJSji3HwUyurY1EeCF4WrXu0yGpWb2W_3VrNThPTRXKoy8sSAXJUAIrmwLRbBrUVqdG78aqD4fZDncc8rSKxkwY_prlyMhv4PJ_mKZzDypBYBSEj6By8h0HV336CEWyBvfToAEgRbPRvLBSd5woWb1ECALHMwBmwDG2yh4X0Js_ZPlKmW2ENuit09bGa1fewS2SHgAYzl5jm7hw3TpyBupsOc1khXNkhtfs4Ch5xkUdJ9xYKGEfhIlycuAjWogNgLG3FQ7W84RbclJtgutMm0n0oWNAQOJ9-o0bf0NsgTd3jNeSWESTaHiJ-fCeTH4mzFNi84-nHLvTJEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Nr4o1kMACpGkidDFQnzBO_j2PtvEbZCvfyo43FnmFOg7iFyFEeBac_kzps76hAXSP0qee-QS5UDhwPh-j2C8CR2ngX30pc_ipzfqsAKLBE7mrMb7pbKEpPKj426k4eQp487refz4upySPg9nUv1W-f48XgfipdkKJ0FLzxStFVj8LXa_DZkHRHvPsrgOWNI-uIrKTZ92u_p-AxaBjIyCXicvw9TQ-7yr9NqvJTyFBgSyiNPBycPVBrXXbWP-eiZjcNJeqjIhQkCXsSdqLMBngblYWFScnhDFssuUR9EGGmkFNrJuGY4B4zpe6215sDz0N8olPN2UUIH-wAaemNts3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه اپلیکیشن مسخره‌ی اندروید با AI گوگل نوشتم مجانی، توی بیست دقیقه
ویدئوش رو ضبط کردم که به شما هم یاد بدم. اصلا چیز خفنی نیست اما خب بامزست</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/3934" target="_blank">📅 23:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3933">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">میگن Cursor یه چیزی ساخته که SpaceX اومده 60 میلیارد دلار خریدتش
نمی‌دونم چقدر حقیقت داره این حرف اما سرمایه‌گذاری خوبی انجام داده. به زودی CLI کدنویسی grok رو شاهد باشیم احتمالا</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/3933" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3932">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">آموزش کوتاه استفاده از :
WhiteDns BPB  1.1.0
📱
📡</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/3932" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3931">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ورژن 0.0.3 خیلی بهتر شده رفقا. حدودا بعد از 20 الی 30 ثانیه وصل میشه روی همه‌ی اپراتورها و سرعتش هم عالیه
منتها می‌تونید از خود Wizard استفاده کنید و بسازید برای خودتون</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/3931" target="_blank">📅 18:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3926">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.3-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3926" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/3926" target="_blank">📅 18:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3925">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/3925" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3922">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QK1E6qn_d55TfU8HK50gVrYQmVf7dVmnaD-B7FOKJrucmS1BIuxg4y5KQdm6JVM5UBchDbSEhJJcDfrs8NFeOPhW39CAaRzzV_b-pM8rNoOfHaQK7xPWVfpN7NItGO4fzn5HV_Nn7LMBDLb5sSx93iKC1kavXNCGp3C8rXxeDgaD2yy1joow-Sp57DnxEloIT4QYgyRiFQHid41Go60FkXASGXq201tnCcF8pdo7ZzA-LanaO3wFMILOu2-ILU2fDXGzZ_YzfeCnL-BLvRO6NoWPlI7AYrAihZa0siEh_3SDwqxOrBbf5wYkkQode8tFAiHTr6_hc0MWOA8VsZqoUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X5sRtEdia9GmjlNTiZQJluw9_KYlMXyN-aDVUOjpCpaoGXm_Bplt-vO0LIp4paLl_CjX9fhGpl4rjsbwo43KKV6eWRjpe7l3jdJ46H8IAGmhdRX9LMDVzqiczNCm9mPP42dgmry3VP9CaIDdNLEwXHfVtawNl1oYbghRFUAe0tbM0rEVno8x5bJXjV1PSsNtaaxOWLgwWQFUNP7OtG2948wc8-yY9VAZVQqrKE_FNKH3ESupZtGef5KAx1EC7jjZ9S74wrVxXNDNF-ftLNGt6Ujqb4Zp2r-Tztr9He1fF-l1neSatZIZvMlDa7Wnm9S9VSFGpwqIY66jDcdoN5LfWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SQvaAwV7S4vXk2Gqa-J7bfVQERVjV_Qirm8P_GrgJsuOXsKz0lZJqozCuOuL-5T9alQRMQLZszxjqY-Jf25LSKbqYiAUpakv2Fr4DUKWj4LkIHBjVEKbcA7HXHjaSM1A64riT1lIRWFh1oMRKEgfgKscdUS9uIL5HOHq7j01d3-ezekJkHMc9Hk7wMOwPzA_L2pSqmtoM5Qag8OIrRhbDf8DOjT3_miyJ9I7kRmFJlqF_H_y885-b48fNbfwPAdLdbWBlO5BFsbIXn673n_CxgLBzdhkYE7IfE5-42vGXdCEn6XHmHQGMYxsf1Rt6Vch7lI5cAmu-nnNtiI4KBuR6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بالاخره قابلیت ضبط صفحه نمایش به همراه دوربین سلفی، به اندروید 17 اضافه شد و دیگه نیازی نیست این کارو با نرم‌افزارهای مجزا یا تیک‌تاک و... انجام بدیم. کلی قابلیت باحال هم برای گوشی‌های تاشو اضافه شده؛ از جمله foldable gaming(که توی تصویر دوم می‌بینید) و ارتقای مولتی تسکینگ
اطلاعات کامل تغییرات:
https://blog.google/products-and-platforms/platforms/android/android-17-features/</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/3922" target="_blank">📅 15:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3921">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">برق داره دوباره نوسان میکنه
اگه سیستم داشتم به جای لپ تاپ، از صبح تا الان 15 بار خاموش شده بود
فکر کنم باز می‌خوان قطع کنن اه</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/3921" target="_blank">📅 15:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3920">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">😂
😂
😂</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/3920" target="_blank">📅 14:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3919">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aDqxgSPPmhZEiBDAj6se1agrd2Fa1LZ6vJMOOWgJ8ZBPdJpQCP1grQzbyu-MNSbDJ7ENto5oPkVDiEvSZRsXBxoWvQozTpwBdQA--QGJAPf_U5qg0zVz6KgLyZozfZpoQ4vUekJ-cLlLY8zglcbERvp3UqRv8hThZn5XCY7LSwdYAdhFz4w7DJ-0eyHcDJfE417Cy8pkgMExuKu8I7MbMrE7e_hPDA3puCOFZxphMGNA3E_l8NWR6AkVMnAaa94IvCYDKfX2wzlfvVUIhGA0-1BvNacXTUqAzWZ7wsGhkZM7B0xS_U9CzLyfzz58n1_8ZdnIOspGaK96Grf9mkaS2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/3919" target="_blank">📅 14:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3918">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ARzJF9CcdtMyjyT1Ax6lU7Vb_c94QlJe76KnSmjPNkQl1KWEgnq0DjXs_ovY0y3yxzpoEoKjscHs4IGFnHgvDW6M04jB3ad0SLsHnDYw7RR8JVH_Pkvf-5r-4-fIBeaVEger_pWjBftQIcpvJ5DdV80a82dPZ_TvuXq4ZfdBpfjTO7MRZV2BFDljJ1Nj1SfBGzWDH13wrj_M0QmCC94884WXhPIREjvpxGjlZMu4yUlhNPLKZkRa9fCPc4kayt7CJ69tUT-CcSh4uvaI8AVqxOZiPBBxaliuwjx6_h3gQtjdKyqWGR5KICTsqFDxiKVbVlazdsj9NDPuq1e7J1wlPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیدات کردم مهدی جان
🥳</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/3918" target="_blank">📅 14:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3917">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VgNq-vqO-vj-cmJaWIq1BnHY3c5EIXodG-12uB0KVNT-bqaOpqBzxXJXecDE1XrJ_Ro60UszK6IsqTMpAkXfjAZVyIT60P9RcoGy_kvku7K4hsMkkrExqLAsspLeQeqtXXHtOGEGreoBWBryH2bukSrKsQBKE6-z-O8h_e9pkfhhmeNnBujndFCDPjj8bZz3o5Zwj34ZBaIqsmQFHBdzmX46yjWEsFlLCADCVCfNwdpw-pAVKl0khh3DMDKsLLJGSjvPRqtRFtxyHUbg5jvZfQcxPx2bBk0tBYdKVslaBmvBuWTri65Xp02MG3GNcbFRVxwhafyNXhq2F2cQqofTGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندتا از بچه‌ها تفریحشون اینه برن وارد پنلی که من توی هر ویدئو میسازم بشن و پسووردش رو عوض کنن و برای خودشون لینک ساب بسازن استفاده کنن
😂</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/3917" target="_blank">📅 13:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3916">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/3916" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3915">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kHJD6MvUVsVbrlVKMVeFaBjE9hEk3RSsAuoeJGfIhy_MniHVP1NB8892Pxoc6larRCkUYkA9Gpvu7mJvTwZd-oW-UvkqOn-HUoRYLYswFYL_C6udQmJurGtJ4fZEN1h3wG9Qvmai5LijtW07ce5nuEgZVDyIxbJKkTYmjLekUMOOZvUJsuzWEPtebhuSBkZ1DiUJhdxejGiOAREkA_hLQzqReXqouvtsy-_DHCh50lHpdLapLsADOkLQV7IG6FcQeob5ydfNHESaYONbBRM95h_XmKjMfbYCI_o0EvvE_u34Dih0fOZoftLE6Qqn93O6YzRWw_nsm71cBKU9FMDtAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/MatinSenPaii/3915" target="_blank">📅 05:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3913">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/3913" target="_blank">📅 03:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3912">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">من که عددی نیستم والا نمیدونم وحید آنلاین و اینا چطوری هندل میکنن که آیدی خودشونم گذاشتن
😫</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/MatinSenPaii/3912" target="_blank">📅 01:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3911">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/MatinSenPaii/3911" target="_blank">📅 00:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3910">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3910" target="_blank">📅 00:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3909">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا من داخل این پست میخوام توضیح بدم این بکاپ ها و این ip به چه درد میخوره؟
ببینید قبلا یعنی تا چند روز پیش شما تو ایرانسل اسکن میزدید واسه ip اینا ۱۰۰ تا میداد برای مثال ولی الان هر  چی میزنید ۵ تا به زور بهتون میده و ip اصلی که
188.114.97.6
میشد که ملت روش وصل بودن رو بستن
❗️
یعنی ip ها کلا رفت تو دیوار کاملا خاکستری شد
اینجا (patterniha) بهش اشاره کرد:
https://t.me/patt_channel_x/68
بعد حالا همه ip ها واسه همه جواب نمیده باید ببرید پشت gpt با یه سری ip محدود برای sni spoof استفاده کنید.
جدا از اون میتونید تست کنید این لیست ip ها رو که واسه شما وایت باشن و مستقیم بتونید داخل پنل های bpb و نهان و... استفاده کنید
🫰
ip:
103.160.204.34
185.193.30.94
45.8.211.57
199.181.197.1
159.112.235.52
170.114.45.239
104.17.21.111
104.24.200.94
188.114.97.6
آموزش ساخت پنل bpb
آموزش sni spoof
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/3909" target="_blank">📅 00:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3908">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cI-j8lgsR5c-JAmtbJmEZIppCBehKLgdzkeQ3XO-W3_gJ9AFHoIq4vL06Bnqp1CA5YExm41AkXz5YpKC3DBxDDh1f0vB2C_sA0ax4Ir4TVeH_Kxzf6J7sWFWzhMswk1EZXt4Uss1Po2_-PRlI3nCRLNUEHL6wZPuL1VCmVsILN8KkzeJMj-D_qIjZ6Mt7o96MRQfRI4g4qYw2UJJijc6l1fmDcLKND7FPIXWBDalmiXeaoASOYVVmEOP93Kzxl7V8BYQltwSrUuqRyp4JPF0JGPg-tlyqWCi1q5zHhJbeJ9rM9oDElOnWvTe_SWoBUpOBPCg1xsAfVk5GyWoMHlgYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/3908" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3907">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">متشکرم از بچه‌هایی که دونیت می‌کنن. چه کسایی که استارز می‌زنید، چه کسایی که به ولت‌ها دونیت می‌کنید، همه باارزشه.
من دسترسیم به ولتم قطع شده بود و مجددا وصل شد الان، دیدم دوتا از دوستان 3 و 20 دلار بیت‌کوین دونیت کرده بودن. ممنونم ازتون
❤️</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/MatinSenPaii/3907" target="_blank">📅 20:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3906">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/MatinSenPaii/3906" target="_blank">📅 19:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3905">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر:
https://dash.cloudflare.com/
لینک پروژه‌ی نهان:
https://github.com/itsyebekhe/nahan
لینک اسکنر:
https://github.com/MatinSenPai/SenPaiScanner
لینک ربات ProxyIP یـ‌بـ‌خـ:
t.me/nahanproxyipbot
لینک ویدئوی اندروید:
https://youtu.be/2otJfXgNWCM
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش ساخت پنل نهان
2- اتصال به ربات تلگرام و api کلودفلر
3- ساخت کاربر و مدیریتشون
4- رفع مشکل وارد نشدن ساب در  V2rayNG و ارور 1031 و 1101
5- اسکن آیپی تمیز با اسکنر SenPaiScanner
6- پیدا کردن و تنظیم ProxyIP بر اساس کشور یا بر اساس سرعت اتصال(توی ویدئو نشون دادم چقدر سرعتم بالا رفت برای دانلود)
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره
با تشکر از
YeBeKHe
عزیز
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
(نسخه باکیفیت‌تر)
💰
دونیت</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/MatinSenPaii/3905" target="_blank">📅 19:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3904">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">داریم تستش می‌کنیم این رو، و خارق‌العادست. دم ویسپر و پدی و بچه‌ها گرم واقعا توی ۱ دقیقه پنل BPB ساخته شد واسم و الان دارم پیام میدم باهاش</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/3904" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3903">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-BPB-v1.1.0.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">معرفی نسخه اولیه WhiteDNS BPB
نسخه اولیه اپلیکیشن WhiteDNS BPB منتشر شد.
این برنامه برای کسانی ساخته شده که می‌خواهند پنل BPB خودشان را راحت‌تر روی Cloudflare راه‌اندازی و مدیریت کنند، بدون اینکه لازم باشد همه مراحل را دستی و پیچیده انجام بدهند.
با این اپ می‌توانید:
✅
به حساب Cloudflare خود وصل شوید
✅
پنل BPB جدید بسازید
✅
پنل‌های ساخته‌شده را داخل خود اپ ببینید و مدیریت کنید
✅
پنل BPB را با مرورگر داخلی اپ باز کنید
✅
لینک‌های سابسکریپشن مختلف پنل را ببینید
✅
سابسکریپشن‌ها را کپی یا مستقیم وارد بخش VPN کنید
✅
کانفیگ‌ها را تست کنید
✅
از داخل اپ به VPN وصل شوید
✅
لاگ‌ها و وضعیت اتصال را بررسی کنید
در این نسخه تلاش شده همه چیز ساده و مرحله‌به‌مرحله باشد؛ از اتصال Cloudflare گرفته تا ساخت پنل، گرفتن سابسکریپشن و اتصال VPN.
اپلیکیشن هنوز در نسخه اولیه است، پس ممکن است در بعضی دستگاه‌ها یا شرایط خاص نیاز به بهبود داشته باشد. اگر مشکلی دیدید یا پیشنهادی داشتید، خوشحال می‌شویم گزارش کنید تا نسخه‌های بعدی بهتر و کامل‌تر شوند.
WhiteDNS BPB v1.0.0
@WhiteDNS</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/3903" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3902">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/MatinSenPaii/3902" target="_blank">📅 17:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3901">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB
خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/3901" target="_blank">📅 17:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3900">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مقامات هند، تلگرام را تا 22 ژوئن در این کشور مسدود کردند.</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/3900" target="_blank">📅 15:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3897">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/G_TUh0A7rpKQVdwdf6gWspCA98KUrw0wsGkT0gJqBFaus95khxwmGSn0xTIizihvu6G1DX3WwVWgSRWRMH15tXw-UhOG37e1nuByeL-m8WD7YIwwS_F9bjBJg-q1bhC13DVadx5t3HLh6ksk52zImbG2bgBcB3BqG2Yb1PcD3Zu4g4HP018Irq1kJeGBqcLcZ6tcSBzOY47J0hLG3zAJiYxBdeWe5j1h-HUL3j56QiQvte3l4h5hfWWX8d3CJZCsF2OpLPhhCa-sTiE4kgVKd9wltEGTZuumd_uIgrz_3PvbJ-KM1Xb-zjfowyu-1ss4tODdJNW-oKC35owyM4xXWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nx9VX9rWWRLYYU7wbG4k9AIGZqjl7Qs3Tjs5oeydLOHjjG4lGZy53xsYvLYLI2c7kB6b9RRwBf0w8vK3UEvMmB4tG3T7AgW8mEbeGM_ibMnTP7GM6XCRc67ZoVU5an8W3_z6m_V2Xs33_pVPKpRNSY6nSvGGQj-kgHy-kW9DgIfcHZ67UVY4PeoUIYEw6CzfJipwnhkA0rRiuP1AjFtRG0osW6GO2R7WRecwtANM5j-vkLeUQjHt0SLfXqOt2UGoXi_P8UsUn_AEwdDVhxPMEOxkmMAYCJqexAlaylA7-_AQAj0DeI5cUiRWs_nttS-mrNabQyLqIneEMCJP7dte1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NvHcWNVsHrDNdzLYGvuwQdZpnL3XxMZYJxBCw53TAlLgUVCzA4e9rKBtYrfh5j-H2q0ZZ0LW8XKT3AHKHWPuyEkQr8NaCJw6zGMgIaw5KVI1Rq9lR1PIpRaYCvSJwdsmvBfEavwN5QWP_EZ1uamtShngR6eIBwpvFYASTXcqcEkqJxMuqZWoNRoR8YPw68YGcXdCCIlNHbUa1j65xGBj_U6_bLEU38m9E43CguiZOi6OFEinPGd2QYjd27-CHEHosCiEiMoVHHA8eGzSEChEHFXwh7bDGteA5RlrmRdmV3bOt74FSotlFX55brw7nwpV_WdZjsCIPZtCcy_JllAP0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد میگن چرا کامنت‌ها رو جواب نمیدی
چون 90 درصدشون جواب توی ویدئو هست، اما ویدئو رو کامل ندیدن
✉️
مثلا اینا کامنت‌های ویدئو BPB هست</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/MatinSenPaii/3897" target="_blank">📅 12:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3894">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iu-g1VJN93bHNRSE0VqnY_RgqkNv6yAqW5JINg3sQc73hdm9hY0k0Nm36jFuBYSuUaKYGfg99DP0_04PU5pBC6VRON75YiaT5JrMJNuEh8UcbEFFHqJWEtiyBlmJ007Og2S14x-Rn94yB7VD-z_PkUAUYPdTGnWnx8sCrrpTZBOrXu2x2lhH2fUg_EpM8viAPFz3u6kXhhv1hFj-hsJZOMwfOfMHUujYsDauXOu3BaTymkxyo1628QSgAKMWjLTGkxxgcZBXhhGYiP6-EloIeT3PPR0p6DMNI8SJ5qEygqHF3dtjLm2HLv53HrR9P6jOwSb3vudXhb1Rbq5Yk5awkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cgREXOKZgn8az52S0HvsmV5NW6rkOskuNaGS0bbESJ7BteMutD5NXael8hOXQfNhOgZU5FAC4nTOMlUelFw36Ghw5shPG6ZlAZjXjRkuVzbC2utBGS9mdyBqWU9OxBWxQwdMHa0sDuysf7CY57qB5fPH6p4hVa0kZL73WswyIW1lbKGU-86JlvAeoQYn-IVVsSjapXs-YeS1YEPdHn2qGtK-FSyJPQwr_AXWEcQErZJtO-7Cdfy_9xj1V0GfHHT5ECTh9A5pzoo-gZTjb77esn28ONJUOiV9T5sVb8vwO2x1KSrG9Dthnqc0ja3PqIVTzknXurXBQFyrHzElbSBMqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PztClkgAAJAVnRrR8te4SCsSORqmiR_PoTPhlDNRl99BHOWxsdJK4zWZTtbmEh776EOsiRw4Qb1SRpmPNH65tjFOqErczEFv6uPvn0yyuWqO6PQBErkiyXLQ-MRtyDtb2_luVbKDhmgMabevGd3qVOHnEiD6XXFpO7o97oSg1lMt_1MC8o-AKhaPwj8_gAhfRj5hDElo-io2PA5wkiI3CVp_5V3l3Rst9_9t6CgafTRw9Dx43Fu7wNZRNMWCOYXz1WtojqbYckYDE4FDVWiNSrVvfSBWAOFtEA0wn6-iyu_jtsnePGzYk6zaI8laLrC51aXxT1xCYfTcAcvbNSKnCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا با WhiteDNS BPB هر کاربر اندروید می‌تواند تنها با گوشی خودش، پنل اختصاصی خود را راه‌اندازی و استفاده کند.</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/3894" target="_blank">📅 11:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3893">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">از دو روز پیش، دیدم که سرعت آپلود کانفیگ‌های مستقیم پشت کلودفلر روی یه سری اپراتورا توی منطقه‌ی ما به شدت افت کرده.
و بعد که چک کردم، متوجه شدم سرعت آپلود خود اینترنت خام کمه و زیر 1 مگابیت، و مشکل از کانفیگا هم نیست.
پیر شدیم برای یه اینترنت خوب</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/MatinSenPaii/3893" target="_blank">📅 09:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3892">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شمع iced blueberry
🫐</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/3892" target="_blank">📅 16:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3891">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLaFeghNLOT0uMg0PjvkM7SXpMPJ-qi7y_0E6W7SmqZ3npeALu6TJFfbvWjrm89YPuhnHq4VXJWlLeSSAQoqtLRFvo60cDPmaDBlG9dcfeygt1B2bhqemS3D6VNdeo-xWvDDmMzj0wiK2I3P_cekX5-2aB2Pea3djIeG4T53tzOV1vL9usfX8_r_CjpK7fl846mpL6Dkyax8n5Za9puEYHZ2_zmT0urgSyZ9SpQw3Aahhsr-HFsV4W3BRvfVnjZH0LCWAWTDuhdBRhxq7yXSxKXD1FYeuxHe470p0Bn_KisLwZ3S2bKaxjx6j1tb70b9P2wLJTwNSNNOolDhB4liZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
جدا از همه چی رفقا این ابزار رو خودم قبلا ساختم این ابزار چیه؟
این ابزار کارش اینه که شما لینک ساب بدید کانفیگ میده با فرمت های مختلف و همچنین این که کانفیگ بدید بهتون ساب میده یه سری آپدیت ها براش میدم تا بتونید مستقیم تو اپلیکیشن ها استفاده کنید ولی فعلا داشته باشید و ازش استفاده کنید.
لینک ابزار:
✅
https://xsparvin.github.io/Abzar/
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/3891" target="_blank">📅 13:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3890">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bi5tpJfbGBqneoXL0d8Dxaz5mNhm1O4knzXz4yRQicHU8kWNH3lDKJ70_fiYrSHQGMLETsdjukGbvkyBdH9OlIM7j1FJIpgb1lbbUEvruoLYE3kCy7CsgT9L29LhOh9VpN5tmGqYYYn14puOjeIIGmvDt3vkkQHsUWS1LHJkcIgwo5Ufb1HfaiVeTdXy9G2i_yJ2PJoDHdo39L624j8fDcVkhKoU4GK60gaDJghuHFe08JCxopjHCJgPqkCcV3bu7KqwauAueP3__rXTEVorw_EBzin3Z3g6nLLn3L9B8NaOTPrNlF886ZcEtp7oqmqVoWVZw20PrDZbRhCJtWRSkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اول که ممنون از لطفتون و بازخورداتون، دوم اینکه اسکنر حجم زیادی میخوره حواستون به این نکته باشه
🧐</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/3890" target="_blank">📅 10:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3888">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/riKmiMVOty-EytC8bTnHk9v9PeVukZimtcqOGys8qb7OJT01eoHi0SpfB0fkP1AboWMXf7UXuUeG_KJ5eKo2tfv1rD1Y3HvJppDtrz5j_eEBi2dnbM4Hv4-VrEj6qB3XyzDadd3iUf4MI5kXO2GE-HPb88BzXfnTvR6dGGG3-uLO67nd0Ia2qgzWRhxdRDISpv3xyAfTJK1L2aBwwE5aX4jzMMVn2bim31NlcOEJ9JO9W8_RNjTgj1Rw_Y3KdL7OK0jIDFe6r8GzkCbafrjD0a558rUnWZucoLWbMm0TsQrCN6ZUF2v_7oYjQfxeHzS1Q9S-cLH-0Vg1dei6d-5fnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ta7GcH4rd9GLP5c8jsLnZ0Bpkgi0GCUHDIqZESyMD6_d8W7_fkUXvbbQaUm_4EPo7QQHs6VVr4TQERxrQ6jfABDN0lSyLFQ8lVNO-FR2bxYHBkz6JBTyjuuzqq-Ao6EacV1kLCrLAq44vspFLEq755l5A4T_MpB1i4A6u4OanPbQbN1wKrcUjVbGVEclPNkkfPF2CnoqKTRSGBFbYk_9xDRqwFBTrH68-7x-L6Ctl87yGvVKKxvoABklQF1MEwqNrzgkFS2CZxDzt801TCC16G9-C2wHlRpHcg-9tjmGqsOTjj9epX5cHI5XPlCIV9Ho-U_oGabPTEeOx2rWGIOLYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور: @nahanproxyipbot</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/3888" target="_blank">📅 10:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3887">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kf66nb1PjyVmTB-TcEtbP91xEOf80GRlaQR9xADddeOFX6S7wg-mI4vzaxQQIvtE4ujPq5QgGDnEmD06AQeGMLR1rVba7hOMJuZVj3pVQ41bsuDN_B9Pt9TwrazPNQgHN0bJOsdG280cF-yQDwPsZI3JxagvPiTIibuAxO4dwyhyzlo7hiIEX9MLwu5zgLUyDUvaDhTd7NcWiwGTh5_4NG47nOnV7yeDrI683WEtC-5l-2Qzr-ispIg-g3b5W5xBJbbrUFr7-sOb4c-_MJlYcEpfo0IBIFwqdej6AKVSk1C2qomN3l1JuJKzT8VdOoweZbA3E8fT3WtN2OCVNjuLMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور:
@nahanproxyipbot</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/3887" target="_blank">📅 10:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3886">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خب قیمت دلار اومده 165
انگار جدی جدی توافق(که نه، تفاهم) شده</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/3886" target="_blank">📅 09:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3885">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ud_pVSMLjVfNN-LC4jVcOIczA5qVMf-Kbj21xf8_ghHPNvqNt4pF4Ar1vAjddZG9CU9lqfX8ZIcFm0DROr-D_e_aHXfBrsLVObU1tZQryo4t5xt55fJbAQ3XhvWe70yESMXswPwI6cZdtRQeg3j-cVjzYo29JtXSVfOyHIAKn3qKZosCffdhKVRltL-CXX3rP0_Buk2JOqqQKWr_C09eroDudufMja045RCszHFNGLZCsVAudAI_yMqt862VgEzgL_0wQhONLElAoyx49YNklbXuDmM172epUb1CXjhdTo1-PjLaV6tKot-LvG4WQ5NP767r4_1jdFEtwLCB4pHmqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پروژه‌ی جالب دیدم به اسم SurfSense، که بهش می‌گن جایگزین اوپن سورس NotebookLM
📞
اگه از NotebookLM میاید، باید بگم که SurfSense همون کارو می‌کنه؛ صرفا با کنترل کامل دست خودتون. خلاصه بخوام بگم، یه agent تحقیقاتی اوپن‌سورس و با تمرکز روی حریم خصوصیه که شبیه به کار NotebookLM رو انجام میده.
👍
مزایا نسبت به NotebookLM:
• اتصال به ۲۵+ منبع: گوگل درایو، Notion، Slack، YouTube، GitHub و افزونه‌ی مرورگر برای ذخیره‌ی هر صفحه‌ای (حتی پشت لاگین)
• آزادی انتخاب مدل: ۱۰۰+ مدل از طریق LiteLLM، یا اجرای کاملاً لوکال با Ollama و vLLM
• بدون محدودیت داده: هیچ سقفی روی تعداد منبع و نوت‌بوک نیست، و دیتا روی سرور(یا سیستم) خودت می‌مونه
• جستجوی بهتر: RAG دومرحله‌ای در برابر سرچ تک‌مرحله‌ای NotebookLM
• قابلیت‌های تیمی جالب: به شما رول‌های Owner/Admin/Editor/Viewer میده + چت و کامنت و...
• تولید پادکستا بدون محدودیته
😭
معایب:
• نصبش هلو برو توی گلو نیست واقعا. رو اعصابه — باید با dependency، API key و فایل‌های Env کلنجار برید
• هنوز کاملاً production-ready نیست و در حال توسعه‌ی فعاله
• باید خودت میزبانی و نگهداری کنی؛ طبیعتا که راحتی NotebookLM رو نداره
#️⃣
جمع‌بندی:
صادقانه بگم، NotebookLM همچنان ساده‌تر و آماده‌تره ولی کاملاً بسته‌ست. SurfSense سخت‌تر راه میفته ولی دیتا و انتخاب مدل کاملاً دست خودته. اگه با self-hosting و سرور هم بخواید پیش برید، به درد بخورترینه.
🔗
ریپوی اصلی:
github.com/MODSetter/SurfSense
آدرس خود وبسایتش برای دانلود مستقیم نرم‌افزار:
https://www.surfsense.com/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/MatinSenPaii/3885" target="_blank">📅 08:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3884">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/MatinSenPaii/3884" target="_blank">📅 21:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3883">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/MatinSenPaii/3883" target="_blank">📅 19:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3882">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n9YIdxZ5bpt8hf66XQu8NjItwzkndsj_znj9kEKrgyXP-6xlWlXmmqgR9rW3gvZOpaqUAUgpY63Gza3A8jNEJj5deq42b6ZQvnqB7K3va7v8xRwoMOhAvCAhGCnrkR3T5Qb99OCrFW7ZGMkB_XV-mNQeyyW0d_n4Yjs38JHu8Cl3TPo6bBgBgeupvfTnxJqXND2mD-P0FBEgRFZA5MKi7H0v5MVCQUZbeuJP4ueROJjS8jo7xi9RSzCHEKVgKeDaDoeGH4WUAIvBJzfnY4KlWUpE-trJaSJHEu1pPS8ctIa7Uf6Ti0DiWZGUVq1XYdjRyC4HZS0ZEV9WqUvOX3kxuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو برای اسکنر یا هر پروژه‌ی دیگه‌ای می‌گیرید، ترموکس رو از گیتهاب نصب کنید؛ درست میشه
https://github.com/termux/termux-app/releases</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/MatinSenPaii/3882" target="_blank">📅 18:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3881">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HfYZlFoOIzOpgyFyGCGZccLoQ0l5GEnqcqarqH32xD8TOV10BycioYJ4CcEg4BCdVnxe33pUYZgbkdIvec3FjCofC4FhOsqDLhULWVLNjy_byEHB_sJBFAFhkfYXUtRYzkd8ECdTcjs7Rb_Rdv9-jTq2gUEW41u6IyEzsUR94ECB_qtqQy9-QwILrE_zBrKfjsL247VQDn7rbrvY0pvJsL2mtYol_zQ1AtwLB4_Ug2vIV2OEYx2BEU7Z-jdRwgU50-rLFTM_Gf8YZyQWyJx_DfYqaZrbDQeYOO6FOiKMc7pgMQxcyNRBQLsXJFf0xPAb4WpMpHxZDqwET2z1TqP5qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الان خودم با سرعت عالی وصلم روی ایرانسل. ۲۰ ثانیه طول کشید حدودا، منتها ممکنه تا چند دقیقه طول بکشه. ولی وقتی وصل بشه دیگه کانکت می‌مونه و قطعی نداره</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/MatinSenPaii/3881" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3876">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3876" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه جدید اپ WhiteDNS VPN آماده شده.
در این نسخه
• سرعت اتصال بهتر شده
• مشکل داغ شدن گوشی رفع شده
• اپ همانقدر ساده مانده و فقط شما باید دکمه اتصال رو بزنید
متاسفانه باید نسخه قدیم رو پاک کنید و این ورژن رو از اول نصب کنید. این مشکل از ورژن بعدی نخواهد بود.
ممنون
🔥
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/MatinSenPaii/3876" target="_blank">📅 15:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3875">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LcRx25JfwgW8SWtgioJpPu9zrcQwQ7nGPLFbzHNG7gw-SSN0zTHXWtFRMd2bt_xrPr8657of8ulxRd5pPxJjUo4nj5uRuIDloAVGw4i_i8VGx0lOqbkh7rcOB0ZdpmyzrCvVr8p4F3znI77BbUb867NaPDtjsby2k3SGWo0K9SVLKvvvm-aaPlhtwV01O8_gazVedL2P6SirGkWDt47RRX7tfCx-Y3BUGJWmkdBE6SmunxSk9hcSpslLKRnRm6aXuTEFgCmwcQHa4rxWlPYUZH3i-yyTzYTPxMIKqKr-9izytn-WDHCbKY9cqK0eSVzmR9C9g6zYtwgTDFvQuR7O6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکرشو نمی‌کردم یه روزی قالب وردپرس رو هم بگن بیاید اقساطی بخرید</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3875" target="_blank">📅 13:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3874">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خب دوستان به نظر من اشتباه کردم و فونت وزیر متن هستش. مسئله اینجا بود که از من پرسید، گفتش چه ترکیبی بزنم؟ چندتا داشت، یکیش فونت مربع+یکان‌بخ بود. منم زدم همین و بعد دیدم اصلا پولیه. اما الان انگار وزیر متن انتخاب کرده
نکته اینجاست که چرا اصلا فونت‌های پولی و غیررایگان باید بهشون اشاره کنه یا دروغ بگه
🤔</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3874" target="_blank">📅 12:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3872">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n_NdvFkfhmdumqrsXVSx_JSIpXVcGlFTXtqny2rx8rBq2DiaiOmUsSQYsSdgEyVHyhn_QNThS7LIVj1tfGKlNyfihHB743k4IQdHXdmnWRPHvefN__Gk09Qtmvz42uKSaXumJbKcNT6CZ-vSJKxCpBRDlhnmo9H74h694mU3GPcz4uk8CjuHjYJLvrcqGSujY8XrcM5V9VIkiS-JnYwW5in1mGBEPn5JKhyZqlTYTiM0dgxb_lubOg0Ifh9eq_Y2lP-_gJDX4TWlN0fh3Av7xrmKBQcDsQJ3NSrl3H2182iV9usp90W1B0X-8fr1hoegXHVM-aFaXSVYpvLyNeg2og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fZPqMDzFgz2ujY4qT4uzIy75aHOLF4-woCu8ZdvPuUNEeSJiwBBH_F5aXhwKpP0mkGFUdDi_WSag4P1481rk0-oAlDon9Q5WNrjQMj1tze54z_xYaYO8fuXPOgCab3cgOsqdTIc-7Xep-WFIa_R5dCWSHnPR6jXBTO8CVMcgNqVYe88xYjNyu2HMeHS8W2YErFJL3G81ZiuHj9BlBesPpNt9Pnm0pd_oUNaZ__xkTZjzYJPfhQYNvBj6ptoMH2d9OEBO4cOAkogtVmBVkZUOntxfleqiZ6vbR2xBmvWficFd9CQZ5bwYvd0KQxSfnxsSULjVPjY9RP1OgCnNtiVvPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم کپی‌رایت برای کلاد شوخی‌ای بیش نیست. اون از قابلیت اکستنشنش که کل UI و المنت‌های صفحه وب رو درجا کپی میکرد، اینم از این</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/MatinSenPaii/3872" target="_blank">📅 11:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3871">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GYwVp-jp-pwJqbgMygQw3ZFqYSwmDVoDelzLLoNpTT9HlOpKBv30eOLXz5fYNrN791-GdgFoxfohy-9uV6lLgmivUQODmRHSKP2fQQfJIjt-d17zYxKiCISJMv-_7pgt0TSzzNqYwCdzf0Tz_drd0AQczU3_zVfwAVpGNbENqABBcf4TnPSSlCXnNwSIZ3gXW123IHema2UCqbHeTWIy4FwlZFtM62iWnc2MA-8WaDqF2EIIsrRnqTeORYJbSzpHmdxpcSzCkkpLPrnHWyvqLvltEgB4Olvk0l4bniAfbRLnB_fKskyhCxOZeK-z6id_4v8Esdnj1i6M3PsAy2umdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/3871" target="_blank">📅 10:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3870">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/MatinSenPaii/3870" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3869">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/3869" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3868">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/3868" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3867">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏
بدافزارهایی که با ترساندن هوش مصنوعی پنهان می‌مانند!
تصور کنید یک سارق بعد از دزدی، یادداشتی آنقدر وحشتناک جلوی در خانه بگذارد که مامور پلیس بعد از خواندنش، با خود بگوید «بیخیال…» و اصلاً بازرسی را ادامه ندهد! پژوهشگران متوجه شده‌اند در موج تازه‌ای از حملات نرم‌افزاری، هکرها از ترفندی مشابه برای فریب دادن هوش مصنوعی استفاده می‌کنند؛ آن‌ها بدافزارهایی می‌سازند که بخشی از متن‌شان طوری نوشته شده که هوش مصنوعی از بررسی هرچه بیشتر صرف نظر می‌کند!
ابزارهای هوش مصنوعی کنونی، ترمزهایی از پیش تعریف‌شده دارند. برای مثال اگر از آن‌ها راجع به نحوه‌ی ساخت «بدافزار»، «تسلیحات شیمیایی» یا «تسلیحات اتمی» سوال کنید، فوراً ترمزشان کشیده می‌شود و از پاسخ دادن طفره می‌روند. حالا هکرها متوجه شده‌اند که با افزودن این نوع از متون ممنوعه به بدافزارها یا نرم‌افزارهای معتبری که آلوده شده‌اند، می‌توان فرایند بررسی امنیتی کدها از سوی هوش مصنوعی را هم مختل کرد.
به زبان ساده، مهاجم سعی دارد کاری کند که ابزار امنیتی وقتی به بدافزار می‌رسد، به‌جای بررسی دقیق کدها با خود بگوید: «من اصلاً اجازه ندارم این را تحلیل کنم» و از آن رد شود.
﻿
این نوع حمله نشانه‌ای است از ورود به مرحله تازه‌ای در امنیت سایبری؛ مهاجمان دیگر فقط انسان‌ها را فریب نمی‌دهند، بلکه رفتار هوش مصنوعی هم هدف قرار می‌گیرد و ترفندها در گذر زمان فقط پیچیده‌تر و خلاقانه‌تر خواهند شد.
✍️
NooshDaroo</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3867" target="_blank">📅 08:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3866">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8ltUHEcBjsqqTTztapGWvdYtD7vSqldVPw2UfbQ6gYQvyLSkoFvIUcJXxQKgiCSp6WRpzy3Hy1o0xTH62q_VzV1gkIl7_PFH03OU1nqq6Sp9D0HSbyaCnZYVhp2zPdtVkUBTPZmSU5s1ZRxGY25S_EOLoiZWOqk7vSUNixs7SAZaquebz3x5Gtrb2iqwE0VcFFnXEyW-TbiLmLcSp8YgbslCX9mMlgLqK3rRU1KD7RIBDH7oeXpBe99uSMQA9olMi0BtJa3uy2KCBjM-bgNSQ3yOOnvdgnFfnJFA1IN3FTSSrl1CkWygkbMHx_VKBf2XB_q4TyVyCl1K0bWLAoY1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید دفید قراره قابلیت چت با رمزنگاری e2e داشته باشه؛
باهاش میشه ارتباط امن با خارج و داخل ایران داشت.
کل این قابلیت با ریزالور ها کار‌ میکنه تا توی فیلترینگ و قطعی شدید هم وصل بمونه.
طبق تست های من یک‌ سرور متوسط با ۸ گیگ رم و ۴ کور سی‌پی‌یو میتونه تا ۵ هزار کاربر انلاین رو هندل کنه!
اینجوری کار میکنه که هر کاربر یک اکانت رندم واسش ساخته میشه که توی سرور های مختلف ادرس اکانتش ثابت هست؛
ادرس اکانت شامل ۲۰ حرف انگلیسیه که هرکی این رو داشه باشه میتونه بهتون پیام بده.
(سیستم اکانتینگش تقریبا شکل شبکه اتریوم هست، یعنی‌یک seed دارید که با اون یک اکانت ساخته میشه)
کلاینت هر ۱۵ ثانیه به سرور هایی که بهش وصل هست درخواست میده و پیام های جدید رو میگیره و تقریبا برای ارسال یک پیام چند کلمه ای باید حدود ۴‌ کوئری دی ان اس کوچیک‌به سرور بفرسته!
واسه اینکه به سرور ها فشار نیاد محدودیت های سختگیرانه گذاشتم، ولی همه این محدودیت ها توی سرور قابل تنظیم هست و اگر سرور شخصی راه بندازید میتونید محدودیت هارو کمتر کنید.
https://x.com/i/status/2065531715041239193</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/3866" target="_blank">📅 01:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3865">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ml3CM_9lfyggd8uQX7pN8-g5smCfZGoR_QRkUIFFydXoHjdfv_lhk7s1moDiIqFhTJLZbqJqQWCdaAoTC71I7ZnQSgahs7pCO1WibsKivn2Er-ELlOdiaf7-pOEgu8XaTcb-r8eAcKHel7mTSzadkb6gZU42CvhtelKOEMMbqtp3UtHGtWSVzBuzsy-edgbowQS6INpsuzNppgkO9Gp9WkkSpcfNv-XQRoyQayDRCdqyjCekitd2a3DScfestlVhCewGdpww3lmVSfL0M6H1W9Wey7Ev7X5EgSGDni2FTLK5TWPpT3MCZd8mBQ3C37HTvcvApkCrJZVFyBABDBk3jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا به هیچ وجه روی کانفیگ Websocket معمولی سرور شخصیتون نباید اسکنر ران کنید. فقط روی Workerهاتون انجام بدید که ارزشی ندارن و ابیوز هم نمی‌خورن</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/MatinSenPaii/3865" target="_blank">📅 19:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3864">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">برای اندروید و ترموکس، کسایی که مشکل دارن طبق این آموزش دوستمون برن</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/MatinSenPaii/3864" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3863">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">برقا باز شروع کردن به رفتن؟ خیلی دیدم امروز توییتر وسط کد و گیم و ادیت و... برقشون رفته بود</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/MatinSenPaii/3863" target="_blank">📅 17:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3862">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مرحله اول  همه بخش مرحله یک  رو کپی و توی ترموکس بذار
pkg update && pkg upgrade -y
pkg install golang git -y</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/3862" target="_blank">📅 15:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3861">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/3861" target="_blank">📅 14:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3860">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نمیدونم این کانالای تلگرامی چه گیری روی ری‌اکشن دارن
میگن ری‌اکشن بزنین انرژی بگیریم. انگار از ری‌اکشن برق تولید می‌کنن
عقل ندارن راحتن به خدا</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/MatinSenPaii/3860" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3859">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم
پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/MatinSenPaii/3859" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3856">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dpms0dH8RADxmK0Yx_4xZcM8lP6iq02v7YVnBr0tn_nP_Qx1u6c-W4sxhVhQujoWF2KTAZ7HnjBRzG9ofg0STsNr6Aw4id8hs5VVodgepuQR3ZjA1YeO7gGH_iigTMI9jv9kZP4IwL5EP2fwL5iEK9_iQUiuAxLfWI7QEDu4tkL3h29rbJ4_ZlKzkOcT0cBDsxBUKs8JTgiU_wrQ89ZGMuQVJIyUAQ-wojuGySkXgvHGlgjyDqcIi12GK4udauqi9kAqB7tKuNw9OOlK1TtksZKKFTrx9F-IbxvWr2HNVG4HhAff8SA45IqHTUpc91Yz16vaqF_Ja23ZL7ePjBReGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ldSYtWnB57M4VbsQmRFecjafEjqx2s05ta7Basm5LoAz9G37qIYRl8-w6ndsg8Y51xgRFHVuVXeLaHkV-FsBLunVOI5PTCzOOy1FbwDq1F1aUIIcNqyIrcfm6mlUrPeNWFyfgvgID3N_UB4_CILq8l1QY_nETECWHD2DYwboaDxq_RaIjFyvxRjSuYlObgOMIx1reCHh7BaJrvpURhR3gn-JK8HSyrmjz_X8v-nyCbb8AeuqtMzfM3XVPFwGW1FEKyfwojY8As7YTw-6BAEzm9ZD8yQumblVQ8WGVQdvQCUVeQ1BQDNZEMWcF03ogiGouOSzbnk1lf98iJt5BxuB2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P-gNupzwOWK9iF-7PnImZSLo1Hp65fEdsf0tRorsBlqOilnCvI8AFHZiV8t8xBwO3y1GdWW5BTdDktJgREiv3oHKtUvyGoWTskK3Bfvy5tEhOYwiClkxVaplJ1t0TAWTX7G9JylfnTIe36ZNbct9DzaHnEfAnUW4K_TdpxYEQ_6vIrhheUNjdF7RbW72dGK85GqEPTsk-fM6pEtBJGHpc_Kpehs5L0RdY0DMVORSyzLZR274wh2ztGPIgDiIEc-mdWTjevrVF4rVjGIVMVwzv_Ldhal6TL8OxDJWpOSBRA3ey5zi3uDESf3yKkY0nBBORawMXHUWFwgyi1VmInGd9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن 0.7.1 از SenPaiScanner منتشر شد
✉️
😏
پروتکل‌های جدید
: پشتیبانی از
Shadowsocks
و
VMess
اضافه شد — هر دو از فاز ۱ اسکن تا فاز ۲ xray کاملا کار می‌کنن.
🧮
خروجی چندفرمتی
: با زدن
e
بعد از فاز ۲ می‌تونید نتایج رو به سه فرمت صادر کنید:
1- لیست Subscription
2- Sing-Box JSON
3- Clash YAML
🔥
تنظیمات سرعت
: فیلتر حداقل سرعت، تست سرعت آپلود، آدرس سرعت‌سنج دلخواه، و سایز sample قابل تنظیم.
🤖
ذخیره تنظیمات
: تنظیمات اسکن ذخیره می‌شن و گزینه «retry last scan» هم اضافه شد.
📚
پشتیبانی از CIDR
: حالا می‌تونید توی
ips.txt
، مستقیم رنج‌های
/13
و... بنویسید.
📱
اولین نسخه پیش‌نمایش
اپ اندروید
با Kotlin و Jetpack Compose اضافه شد. معماری MVVM، تم‌بندی کامل، و ساخت خودکار APK از طریق CI/CD(هرچند CI/CD باید روش کار بشه هنوز).
لینک دانلود آخرین نسخه:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.7.1</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/MatinSenPaii/3856" target="_blank">📅 13:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3855">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دوستان، این شکلی میتونید به من پیام بدید:
https://t.me/MatinSenPaii?direct
اما از اونجایی که دایرکت به شدت شلوغه، و من پیامها رو اسکرول می‌کنم پایین، ممکنه گاهی اوقات زده باشه سین شده، اما من نخوندم در واقع</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/MatinSenPaii/3855" target="_blank">📅 12:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3854">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حقیقتا MiMo اگر پلن پولی بده، خودم اولین مشتریش هستم. توی تسک‌های متوسط Backend شاهکار کرد امروز
هم توی سرعت
هم توی دقت</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/MatinSenPaii/3854" target="_blank">📅 12:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3853">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">هم پشتیبانی از Trojan و Vmess و Shadowsocks اضافه شده
هم تشخیص ISP
هم تست آپلود و شخصی‌سازی تست دانلود
هم WebSocket(که بهتره On بذارید)
هم هسته رو به کلی بازنویسی کردم
و این به کوشش دوستان عزیز برنامه‌نویس دیگه هم بودش که اسمشون توی Release note میاد و contributer پروژه هستن. من شاید 20 درصد از این 10 هزار خط کد که اضافه شد توی این ورژن رو نوشته بودم</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/3853" target="_blank">📅 12:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3851">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dmxMz19FpVjy3ICCklx8YYUfSWZ8doGQFQZRldMfoL8gnbtfcx0k0f9RcCeULF93d6V5Oib_9y8xcSY822I-WvCesVPT_j_rCUMCpXiebEKPpoh97E4FJhE6UqCFD1xD7o7PeM59sYNt8wY1IakmS6-R_xNSRbawuYgFSSzujWp_96x3qHCsPh-raURfsaYL0jchmDBS_OYmLGnwtEG0177datzGLMsrxPSFJWMPep-uKjZ10kJ9a5YAFcwh8AI2oj1RSOMgCPhg_u1fk_LM7Q5U_NSMvU9KldvxofNOw27JupcMVYCNknfrqxWIxnuS3UW9sKGpAiqsYgrucwlJyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lbh2623ZhHeLkT5vvRPEVrdL10dhqxp6xj5SGjoIRutzrhoanK7Oexiq4_XscC6YkUiVbZHQce1elsIKenxl-j0OgZVdR68uGC1ECb3FfGEmJFfMBRAREn1wDKoMmIXFoFztAewDMkmTHP9AvyObgl7IOnhY6gkitwiIPU3OQmrpA-KMw76gLGc0seTfZ8TDC_HyWcR0znguVlOkAOZlHrV2YHkg6_LYXGxv09o__0cMMvqC7Sq1FWjLZCzk_JurfcCkv61nXDJavAWORSDRWluPVRXRxIbCx1sNf50HyUfeacbT6EEud9M7WyWvzz3jui3Y2uQYFyXNtLv3JqdG7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/3851" target="_blank">📅 11:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3850">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sAfLPG8JEvIlLWODCV_Um1vRI7gYAaE1DJWqlWPns98DJhkfWZ42CL1eboIUPPPsKEHDki_sS12-lkXEQ82GKHlzKpUGC59KpGYr-6whlcJ_IDTnzwuOk9nEG3bO-xVsJTeRhGE5oKoxplJt-D1wDydftksd5RvyYYQMhp3tp7-cyv1m5Ju0loMuzR6GyZxmaBUp-zh3OlD7BbydyuYp9nwgUP9BKuZTZ_6ue7oPNbejuNMt0PQfpZaa-_OrjEJ5LrC_H5pnwFZ5QNom2OOUTRz34yxUI6YMb1CgVnPy3kExTsdoDartAnp-K8UgQh20WlYV2on--ZJzreRxg0dsvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/3850" target="_blank">📅 11:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3849">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/3849" target="_blank">📅 11:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3848">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nNNji0tu7qyar7t1UtmLooFEIr5XIGA-bc_CvcReLwRE1dL76nQwz14vjphM2Vvzkx5rntj2Eakj2MX3fg-WT0cRA0uGR2hGTSeFfcApONUVfIEJg27DozCBDNsBSUXbDood8duaT8tSz09i2OInvR04yz6ov8aMSdQVzzGXYlIW73Q1EVIQZTabMViwNMMSJSq6L8u4enuRb268yoG0gqGAfqsU9u-gVYNXUYab-K5-UyQoV2A7xFGQLN_O3qyPoRwoc3VFnKimnVPIgZ6hz6leXLYX7rAjzxXS1N4ImIK0GeuaxLvst-3zkh5nRnWYkNNE4u56MFOZwKrllvO7iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان خوب، لطف کرد و هسته‌ی اندروید و تمام چیزی که برای ورژن اندروید نیاز داریم اد کرده، صرفا منتظرم که خود اسکنر عملکردش به بهترین سطح برسه، اون موقع نسخه‌ی اندروید هم بیلد میگیرم</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/3848" target="_blank">📅 11:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3847">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نکته‌ی خنده‌دار اینجاست که دولت آمریکا دستور داده دسترسی به این مدل‌ها برای هر فرد غیرآمریکایی (foreign national) — حتی داخل آمریکا و حتی کارکنان غیرآمریکایی آنتروپیک — مسدود بشه!!  آنتروپیک اعلام کرده که چک کردن ملیت کاربران به صورت عملی ممکن نیست، بنابراین…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/3847" target="_blank">📅 11:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3846">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/3846" target="_blank">📅 11:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3845">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/3845" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3838">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">32 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3838" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خب، دوستای من هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/3838" target="_blank">📅 11:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3837">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خب، دوستای من
هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/3837" target="_blank">📅 10:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3836">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pS55s8XOP26cT7aFclo3d8KWMh_9W-dHiad1PMpe8JLNKapA0ZJAZXVid9pYfgDfilNZdgzG5YkG5S2_U6kL38_aLWUHWUaEjUvgNiUV5I_BKldB4Z90gi2lA-D5GPxu3pxFi5sVOz66nFqlnsamvY_tHbXnUWxM0mG09NEUy1BLnT5Hh7GfvTeAQPMAKLTEqCXU86lJsuQyW02mQHcG0mcKX3_34I-u5fjBL3Az-rYzSjpvK6yHGNU4sXAEy3wAkIsjhZVqVsLNsZI9a15q93QILaABSXqofh8wY9uCZ7IG6x310nnzeP55kU0jPebKD89Bt_pMLjm3zMDzgpeO5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لپ تاپ اوکی شده الان اومدم تست کردم MiMo رو و خوشگله یه تست پرفورمنسی بریم باهاش روی SenPaiScanner</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/3836" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3835">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LN9lUGVhasXcVv_auSVO8cij8St8t9ESSE7oXQQoeGZGYpA_h1f7H9US4UD-Aukcw8H7TKtFR9EENpEC5_EH3c2XWzJGqsZ-RrKpR9S2k4gGUz2BVVotAVoS3yfFwx5-wY6yVkrYiT8iIk3kOAOOStrz39dcA6lgeVkGMAQV51rLpqb540ulzauNl3s6fWnWIn6giu5GMb8T2Q5-kwtHTHpWTipobcf1_xkEf62t8ytCBGbozbHbSCu2YqqUHoiOGqioqBXrw_wjxA_Mj-Fa7pt6lKTYLwtqW2gK4Xm55vkz8gnDQwdVc9x7ungQIfZjeU_Lcw-CkaoJfSIGHfphcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد  توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش فورک OpenCode هست!).  خلاصه‌ی ماجرا: تیم…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/3835" target="_blank">📅 10:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3834">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/3834" target="_blank">📅 09:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3833">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vohfBGvSd0EC2uDTPpnFtmaTQUC1SOt40TyvAu01p3QN0JgXvPb_JdX_0uVagEJ5WMHdRzG2XonWrHiV1Oo5sMYeX5BnbAcbeaWrcscgLp3XwhlLp4SrxhlcUEZTymt9fRlJvzb-klZn7dz5Fii_lPmeqU10iqSK-08QtJ2SCvugg0nwhKJSMTB7MmzX04IbQe7HicBnK_k6rE8A5YkwoJntq6X6ZGJ_-h0H6GsVK2XHM4Q3W6gBX4tZgVlk9O_3CaiuMkhTTFFlKrBUEDfFnalGB90Yt_NTN0WqfIrOmNi8G_qXrnw_-jJW6QJyGSZ9H6j8O3cbsvwzq8qjddHc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/3833" target="_blank">📅 09:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3832">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید http://l53.net/</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/MatinSenPaii/3832" target="_blank">📅 02:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3831">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t_Qs7yV2kYHThDnmkfMA2b12zk2MPb3ooS8kuuPK6CKXqoyBRJL3Jc2_pnFKr97fs1UYn5n3ZwfvzakSBuzfdwNfIbDdwmRm5dfTtLcLBhQlYKWKpFat9t3aQX2h-zdZNU-nBrd87WpVby7v_C6NyjjO6WcnMGvqXH7HRukpMBRx8CJch02EoS7yjo9ToySPVGPqCdP2pd_cUJopp65YBVcI-GgA7v4Cll4-Tgve1kDJ44rPpiZQTwEE3N_3HVxTQHI5JCYwfFAK_iI-OqMo3mVCPiIG7_qbSCAAm0aYsjhZovJJ09IAAmoPItXSBUpFPFec05y74_M_yXPpK7bmQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید
http://l53.net/</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/MatinSenPaii/3831" target="_blank">📅 01:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3830">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">من شرایط ضبط نداشتم دوستان. یه مشکلی هم برای لپ تاپم پیش اومده که باید بدم تعمیر و ممکنه کلا مادربوردش بسوزه اگه روشن کنم ترجیح میدم ریسک نکنم چون دیگه پول ندارم بخرم
😂
تعمیر شد، آموزش‌هایی که قول داده بودم رو ضبط می‌کنم</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/3830" target="_blank">📅 01:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3829">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWireguard Configᵛᵖⁿ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=TXImbmwQzFTwOgsaXNngahlak3Z0oKAGvrftj9qgLYWUA0qvAcKTh6H0vWqKGc8EhCyZfnwA-VViMLUlHNKicrN3gBntQsyEO2_InoZz6MN_p3XxMZdf6l06_prZ60W1ocBjKxjH241qi_XcU1p3wCJPSeYl2R1pkEsnbW8FwMkzVfBqxZG-qTO-YE2Wpdp5UvlJ2l0F0eGclVr2VhfgvQ6pvlyRPQ6ow92yuKVXBtsj6z7RsX9PEt25gCxiFDSm0bOuwlDbouDz2B4IVCo9xI4k6dkY2RfhDCUDGo5ob3rmzbgY9j8s9CEzsCA940Gut6yKeJr98mCHvgCU2Ik3ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=TXImbmwQzFTwOgsaXNngahlak3Z0oKAGvrftj9qgLYWUA0qvAcKTh6H0vWqKGc8EhCyZfnwA-VViMLUlHNKicrN3gBntQsyEO2_InoZz6MN_p3XxMZdf6l06_prZ60W1ocBjKxjH241qi_XcU1p3wCJPSeYl2R1pkEsnbW8FwMkzVfBqxZG-qTO-YE2Wpdp5UvlJ2l0F0eGclVr2VhfgvQ6pvlyRPQ6ow92yuKVXBtsj6z7RsX9PEt25gCxiFDSm0bOuwlDbouDz2B4IVCo9xI4k6dkY2RfhDCUDGo5ob3rmzbgY9j8s9CEzsCA940Gut6yKeJr98mCHvgCU2Ik3ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سا
خت کانفیگ Amnezia VPN
• صبرکنید ای پی ها رو لود کنه
• بعد یکی انتخاب کنید
• تیک فعال سازی پارامترهای امنزیا 1.5 حتما بزنید
• بزنید روی ساخت کانفیگ Amneziawg
• دانلود کنید وارد کنید داخل Amnezia VPN
• میتونیدم کانفیگو کپی کنید + بزنید بعد insert بزنید کانفیگ اضافه بشه
🟡
فعلا روی ایرانسل
💯
جوابه(همراه اول ،مخابرات،سامانعلی)
📍
ای پی جدید هم اضافه می‌کنم
https://darknessshade.github.io/Amnezia-VPN-Config/
@ConfigWireguard</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/MatinSenPaii/3829" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
