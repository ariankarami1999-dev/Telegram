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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 18:08:14</div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/MatinSenPaii/3961" target="_blank">📅 14:58 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/MatinSenPaii/3960" target="_blank">📅 12:28 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/3959" target="_blank">📅 10:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3958">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وقتی اینترنت گوشی رو Share کرده بودم برای لپ تاپ، بدون VPN، بهم آپلود 0.02 مگابیت میداد. اما همین رو وقتی با کابل و PdaNet+ اینترنتش رو share کردم، سرعتش شد 2 مگابیت. یعنی صد برابر
امتحان کنید شما هم، شاید همین اتفاق واستون افتاده باشه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/3958" target="_blank">📅 09:18 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/3957" target="_blank">📅 08:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3956">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کافیه یه آیپی تمیز بذارید توی بخش Advanced, ip fronting
زیر ۲ ثانیه کانکت میشه</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/3956" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3955">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه • ظاهر اپلیکیشن تغییر کرده  • امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.  • پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.  • با کمک یکی از بچه های…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/3955" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/3950" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3949">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6rIa4rgFme5jjXBz1dKQn7Au3GxYOT8UTgWBUFvptiH72i8oLb8IbON9nZ_QtLgo3yqqpM6m1JspGOT07AIg2WZ5hPYRbagCOv5HvV1KXpd315D9u8EcVzJYQmXjn8p4FsGTEM0dnoN1hVMCH_umnthy_6Pb3iplmstE6E1rdV0xI5g6FSG-PjBUSQbGe9aZTiIq_fJbfZ14dExn6n7ImQ8u3muEHobZfSBG4fwr2NDHi7_N7PT63xH2oKtEqtWYv7es2qD0zaFLRrsxKseZK3pKOCfbov-2GNR7d22AmdyKEhDAkzFK03lDqpBynXs4IXmUpRNwKJArvdoK8ogmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/3949" target="_blank">📅 18:02 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/3948" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3947">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kmTL0sg_B-qSPZvQiTQrSmzyv0KNsSPAXZrbyV2x0PZ7fa6ntwNZUd4bHcLJIXffe5nEd3HU_-8i734coL8_TvC8nyMJZl9kX0YGRHof8B-3wpdHksPYCEK8KKZ2Hlz-vls2IOIOAfczwe3eW0EBx0m3QZSjoAImgdecf_1a0XfluShTrt6bbWK8NTCeu6A6QMcXuN7T-fDZhjYidX6KYycEzjTyHbwDNsri1iFOI9wLshZyb1zRR6trwOBamDumTdQ2SO6ZfaRcA1yc7k_9wM_yiHjXyF2cm9ylvQluLvbTWggpL8JKjdpbAktd71tv03srgfJjDOsYuGRzVhKcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از contributerهای پروژه‌ی senpaiscanner، دوست عزیزمون hidden-node، نسخه‌ی اندروید اسکنر رو توسعه دادن. طرز کارکردش دقیقا شبیه به اسکنر دسکتاپه. نصب کنید و یه تست بکنید
👇</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/3947" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/3946" target="_blank">📅 12:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3944">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KdwH0gg21gBOe7So8px4_QBoqE7RLazto4DX5tyOZUsRp5zENuZeUrq2UgjARTMMbQ5-fJAqwnHtHPC_hD1DU44qIdGHzf2MDP6wP3sXIaSDYTR2TUHdw7U_ERcrciv1GNK0hHQNWyBAkXLpUlvXSMAW__pwcrxdwidpBlqV71d3_ZFYvUnns-sFyAB31qGkl6mXWMsoNOfk8pMXryayBCUMiS5eQ3CUKz4lXEGgudsJEkJoC1bQthep9UPa7VN1zsRbJfhbceqj2ocKkfdlI4dzcW7YNNweg0Gff3mJ6iJa7-alHq5Xw4_-AX_hrKMY86oVqRVWEfuPvY137g5HdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S3fdlhfpqfnDdygmwb7Y3rEkz0x8EK1C-kT_Lm_ScdXEZ7hjbr7YEyFlUy0I4hgnM6WPSRjHrvb91DKliekyPohePdMG06v2gxj1AtkGgv3d2pAfFO8p5LoERNGPdPcpTQalAWnV0tis_4_0nZDLYiqbdnzLlte7zmxXCRrXunXrrFn3-s57TwgYFomISRqVTAFcarvrFbPREpEuzP-9-Tp7hJnhPqLYZ2-78Fx9LBWGwWEiqbt1FjWcuAfDCV--_TB3aHvxF5THqoMjAsP6uGyiEy8ybcvcqi6x8zm4hp3XF8Es3Iew67Ugnxtuavw8ubafBBzZFmXNnrvPubOhuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از بچه‌ها اینو واسم فرستاد و گفت گویا V2box، به صورت آزمایشی SNI-Spoof آورده. یه تست بکنید ببینم داستان چیه:)</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/3944" target="_blank">📅 00:48 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/3943" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3942">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">این پست سگاروی عزیز رو بخونید، و اگر دوست داشتید همکاری کنید:
https://t.me/AiSegaro/120</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/3942" target="_blank">📅 18:14 · 28 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/3941" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3940">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGWXhjG6MMxk6mmX9SRqPXEZuafmr4DfD-ahtADx-vwqadsYYUXd5eGCK_iLAGzMw3u8R7JnNaushwch8kMXLBc4xCRjmP0E7TYU-l_FEDOvgF3PZzW-ADkqK955xQ0unVV4LdMRsabPXznhY9sc4LByZmgZOb46kR75GEjg5qWVgAlmN9lvaAY55HhsTtVWREz_Gv1U8U3L7MWaDPU1jycVRxpdz-ObKHC1x_nMaThNDppJES-TlY-xJy1iQ-MmbBF7Jx-qG827ejFbzIPepqn5pI7-ywh0QBdgmI5KvhcT1aNYAUwSWMT9KH5MLgeIQNn_Y_a_BEySiBNKamX1cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/3940" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3939">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SAw8dIpnB-ladhUmST4lUt41JMoWS8-tWCtaAPaTNcp-vqkxp9ucIf-W2sEkhM--S_a9_4qmZeGOvjadEPUEpZxZ4Jwtu1AIE5K0V5hvG2eDz1R-UgGXS5eh9wY0phAaChSjD1j-dPqq9fghLbwLpJ-JR_shOEX4Wugq6d96dB-um8NA6mtA-HZGc2KwT2Lmdo5UQblF7mFMMOCovEkPRzOj7X3jwEgvj0GETD4dAG0yjxIQfeLSuvpnsA1bGudN9r6PrNa9wX_Y38tDB6LoL2a9zjXJzDnosaiHSg86zNBIj_f8jLoMsu9lbUFiHMHV7ulJ2-vBdwMpxvb9LEzx8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی از دوستان این مشکل رو داشتن که تلگرام واسشون باز می‌شد، هیچی دیگه باز نمی‌شد. یا یوتوب و ... باز نمی‌شد   مشکل احتمالا از کلاینتتونه و dns اش. باید تشریف ببرید توی تنظیمات v2rayng و Domestic DNSرو از چیزی که هست، به 9.9.9.9 و یا 9.9.9.12 تغییر بدید. همینطور…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/3939" target="_blank">📅 17:19 · 28 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/3938" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3937">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ویدئوش آخرای ادیتشه
🔋
می‌ذارم تا ظهر</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/3937" target="_blank">📅 10:03 · 28 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/3934" target="_blank">📅 23:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3933">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">میگن Cursor یه چیزی ساخته که SpaceX اومده 60 میلیارد دلار خریدتش
نمی‌دونم چقدر حقیقت داره این حرف اما سرمایه‌گذاری خوبی انجام داده. به زودی CLI کدنویسی grok رو شاهد باشیم احتمالا</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/3933" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/3931" target="_blank">📅 18:11 · 27 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/MatinSenPaii/3926" target="_blank">📅 18:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3925">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/3925" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/3922" target="_blank">📅 15:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3921">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">برق داره دوباره نوسان میکنه
اگه سیستم داشتم به جای لپ تاپ، از صبح تا الان 15 بار خاموش شده بود
فکر کنم باز می‌خوان قطع کنن اه</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/MatinSenPaii/3921" target="_blank">📅 15:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3920">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">😂
😂
😂</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/3920" target="_blank">📅 14:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3919">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aDqxgSPPmhZEiBDAj6se1agrd2Fa1LZ6vJMOOWgJ8ZBPdJpQCP1grQzbyu-MNSbDJ7ENto5oPkVDiEvSZRsXBxoWvQozTpwBdQA--QGJAPf_U5qg0zVz6KgLyZozfZpoQ4vUekJ-cLlLY8zglcbERvp3UqRv8hThZn5XCY7LSwdYAdhFz4w7DJ-0eyHcDJfE417Cy8pkgMExuKu8I7MbMrE7e_hPDA3puCOFZxphMGNA3E_l8NWR6AkVMnAaa94IvCYDKfX2wzlfvVUIhGA0-1BvNacXTUqAzWZ7wsGhkZM7B0xS_U9CzLyfzz58n1_8ZdnIOspGaK96Grf9mkaS2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/3919" target="_blank">📅 14:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3918">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ARzJF9CcdtMyjyT1Ax6lU7Vb_c94QlJe76KnSmjPNkQl1KWEgnq0DjXs_ovY0y3yxzpoEoKjscHs4IGFnHgvDW6M04jB3ad0SLsHnDYw7RR8JVH_Pkvf-5r-4-fIBeaVEger_pWjBftQIcpvJ5DdV80a82dPZ_TvuXq4ZfdBpfjTO7MRZV2BFDljJ1Nj1SfBGzWDH13wrj_M0QmCC94884WXhPIREjvpxGjlZMu4yUlhNPLKZkRa9fCPc4kayt7CJ69tUT-CcSh4uvaI8AVqxOZiPBBxaliuwjx6_h3gQtjdKyqWGR5KICTsqFDxiKVbVlazdsj9NDPuq1e7J1wlPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیدات کردم مهدی جان
🥳</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/3918" target="_blank">📅 14:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3917">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VgNq-vqO-vj-cmJaWIq1BnHY3c5EIXodG-12uB0KVNT-bqaOpqBzxXJXecDE1XrJ_Ro60UszK6IsqTMpAkXfjAZVyIT60P9RcoGy_kvku7K4hsMkkrExqLAsspLeQeqtXXHtOGEGreoBWBryH2bukSrKsQBKE6-z-O8h_e9pkfhhmeNnBujndFCDPjj8bZz3o5Zwj34ZBaIqsmQFHBdzmX46yjWEsFlLCADCVCfNwdpw-pAVKl0khh3DMDKsLLJGSjvPRqtRFtxyHUbg5jvZfQcxPx2bBk0tBYdKVslaBmvBuWTri65Xp02MG3GNcbFRVxwhafyNXhq2F2cQqofTGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندتا از بچه‌ها تفریحشون اینه برن وارد پنلی که من توی هر ویدئو میسازم بشن و پسووردش رو عوض کنن و برای خودشون لینک ساب بسازن استفاده کنن
😂</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/3917" target="_blank">📅 13:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3916">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/3916" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3915">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kHJD6MvUVsVbrlVKMVeFaBjE9hEk3RSsAuoeJGfIhy_MniHVP1NB8892Pxoc6larRCkUYkA9Gpvu7mJvTwZd-oW-UvkqOn-HUoRYLYswFYL_C6udQmJurGtJ4fZEN1h3wG9Qvmai5LijtW07ce5nuEgZVDyIxbJKkTYmjLekUMOOZvUJsuzWEPtebhuSBkZ1DiUJhdxejGiOAREkA_hLQzqReXqouvtsy-_DHCh50lHpdLapLsADOkLQV7IG6FcQeob5ydfNHESaYONbBRM95h_XmKjMfbYCI_o0EvvE_u34Dih0fOZoftLE6Qqn93O6YzRWw_nsm71cBKU9FMDtAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3915" target="_blank">📅 05:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3913">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/3913" target="_blank">📅 03:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3912">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">من که عددی نیستم والا نمیدونم وحید آنلاین و اینا چطوری هندل میکنن که آیدی خودشونم گذاشتن
😫</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/3912" target="_blank">📅 01:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3911">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3911" target="_blank">📅 00:59 · 27 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/3909" target="_blank">📅 00:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3908">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cI-j8lgsR5c-JAmtbJmEZIppCBehKLgdzkeQ3XO-W3_gJ9AFHoIq4vL06Bnqp1CA5YExm41AkXz5YpKC3DBxDDh1f0vB2C_sA0ax4Ir4TVeH_Kxzf6J7sWFWzhMswk1EZXt4Uss1Po2_-PRlI3nCRLNUEHL6wZPuL1VCmVsILN8KkzeJMj-D_qIjZ6Mt7o96MRQfRI4g4qYw2UJJijc6l1fmDcLKND7FPIXWBDalmiXeaoASOYVVmEOP93Kzxl7V8BYQltwSrUuqRyp4JPF0JGPg-tlyqWCi1q5zHhJbeJ9rM9oDElOnWvTe_SWoBUpOBPCg1xsAfVk5GyWoMHlgYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/3908" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3907">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">متشکرم از بچه‌هایی که دونیت می‌کنن. چه کسایی که استارز می‌زنید، چه کسایی که به ولت‌ها دونیت می‌کنید، همه باارزشه.
من دسترسیم به ولتم قطع شده بود و مجددا وصل شد الان، دیدم دوتا از دوستان 3 و 20 دلار بیت‌کوین دونیت کرده بودن. ممنونم ازتون
❤️</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/MatinSenPaii/3907" target="_blank">📅 20:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3906">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3906" target="_blank">📅 19:41 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/MatinSenPaii/3905" target="_blank">📅 19:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3904">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">داریم تستش می‌کنیم این رو، و خارق‌العادست. دم ویسپر و پدی و بچه‌ها گرم واقعا توی ۱ دقیقه پنل BPB ساخته شد واسم و الان دارم پیام میدم باهاش</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/3904" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/3903" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3902">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/3902" target="_blank">📅 17:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3901">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB
خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/3901" target="_blank">📅 17:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3900">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مقامات هند، تلگرام را تا 22 ژوئن در این کشور مسدود کردند.</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/MatinSenPaii/3900" target="_blank">📅 15:42 · 26 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/3897" target="_blank">📅 12:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3894">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ltlTOm6lujUn5VMMhRXXHpLmK0AYcKxKh4X78tUW09L49kGnYEdjLHbq_bhnqY2Okj0fznNg7rPUlAfr9VDQa2Wz5ZlOUstAtuSBomvBF49DplVocJdkTUI1WWws9i84-fQ1tf34iYObd0tKdtA0-Yt46Yr4nmB3IQLoyfBDrGUSD6wn-y9dwgtCLkIeg-FXoaG7wozrbCagzK50YquqIA-Jswkif4dv6HepOB8EFReDGob9xeaTLtJLwjTsprKrS5GULBZZXwKh5rJlCME-myHwFkPec_HVOuUCi_LXUv6mUzE7vutzRWw0NKHn44haoXI6-WxH6kvsAH7_CEuUCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZrAw1UDiz0XQfJlD755N4eKKXuRU_KvE5mb4SH2UcN5cp1EPyH9qI5CvkQ4X05OaPtz47BPIVDkviZmZ7DGzLL-gKXpVf7Br-nAuWCaKUgWAEQ0ZYJaNmTXlfOTfuT81KJjF_4D4TGwSHCuyWZ1JpuJDJXWcfGOLa5_cHpqAlMq-A0TymSfgfKATGOcVe9Ami1ns6UkfXFzanQj-n1t6o6hT6Wal2cK4BpCq-HC1Q_6s3PtLQvkTJ5kIKWJ9X-Non6LS-fhyC4oqUw51s1MdUY8yspILKBkmZR_UjT3s5IkUlSiv2yLxGlOyRERImipkk5SrqEyJLb9DwNoY3dZV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PztClkgAAJAVnRrR8te4SCsSORqmiR_PoTPhlDNRl99BHOWxsdJK4zWZTtbmEh776EOsiRw4Qb1SRpmPNH65tjFOqErczEFv6uPvn0yyuWqO6PQBErkiyXLQ-MRtyDtb2_luVbKDhmgMabevGd3qVOHnEiD6XXFpO7o97oSg1lMt_1MC8o-AKhaPwj8_gAhfRj5hDElo-io2PA5wkiI3CVp_5V3l3Rst9_9t6CgafTRw9Dx43Fu7wNZRNMWCOYXz1WtojqbYckYDE4FDVWiNSrVvfSBWAOFtEA0wn6-iyu_jtsnePGzYk6zaI8laLrC51aXxT1xCYfTcAcvbNSKnCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا با WhiteDNS BPB هر کاربر اندروید می‌تواند تنها با گوشی خودش، پنل اختصاصی خود را راه‌اندازی و استفاده کند.</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/3894" target="_blank">📅 11:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3893">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">از دو روز پیش، دیدم که سرعت آپلود کانفیگ‌های مستقیم پشت کلودفلر روی یه سری اپراتورا توی منطقه‌ی ما به شدت افت کرده.
و بعد که چک کردم، متوجه شدم سرعت آپلود خود اینترنت خام کمه و زیر 1 مگابیت، و مشکل از کانفیگا هم نیست.
پیر شدیم برای یه اینترنت خوب</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3893" target="_blank">📅 09:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3892">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شمع iced blueberry
🫐</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/MatinSenPaii/3892" target="_blank">📅 16:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3891">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iv49yU37kRihiZnXlO4mzgAILqIhVfkIeLIGhvFfOrAQrrKyGgHTX75sPocr_1htFSs8W7_Az3ONrVrRvbWRBMjpuYBmfVNhKMg0goEPr1oqbQFi-QgyveDHNfLeGSU2qd96MN_TBrzrQH3GFaXPYoE3llSd7GiLa33CsD8hcnq1WErX2BbY_euq6k7E9GbBRdamctyWVY3ssX2zMadKdD_f5eLISYUd8-7BjwiUALVDmw7jV3eE8Am4Id7IJnsc-Slm2nrTstfe1cRDhQ0zNGjMCvFxVOugABO9L_a4l0pr4Xzn6MRtTQ6GUJdiOXiNiMm2g4vGHU5gihaJakzrrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
جدا از همه چی رفقا این ابزار رو خودم قبلا ساختم این ابزار چیه؟
این ابزار کارش اینه که شما لینک ساب بدید کانفیگ میده با فرمت های مختلف و همچنین این که کانفیگ بدید بهتون ساب میده یه سری آپدیت ها براش میدم تا بتونید مستقیم تو اپلیکیشن ها استفاده کنید ولی فعلا داشته باشید و ازش استفاده کنید.
لینک ابزار:
✅
https://xsparvin.github.io/Abzar/
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/3891" target="_blank">📅 13:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3890">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bi5tpJfbGBqneoXL0d8Dxaz5mNhm1O4knzXz4yRQicHU8kWNH3lDKJ70_fiYrSHQGMLETsdjukGbvkyBdH9OlIM7j1FJIpgb1lbbUEvruoLYE3kCy7CsgT9L29LhOh9VpN5tmGqYYYn14puOjeIIGmvDt3vkkQHsUWS1LHJkcIgwo5Ufb1HfaiVeTdXy9G2i_yJ2PJoDHdo39L624j8fDcVkhKoU4GK60gaDJghuHFe08JCxopjHCJgPqkCcV3bu7KqwauAueP3__rXTEVorw_EBzin3Z3g6nLLn3L9B8NaOTPrNlF886ZcEtp7oqmqVoWVZw20PrDZbRhCJtWRSkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اول که ممنون از لطفتون و بازخورداتون، دوم اینکه اسکنر حجم زیادی میخوره حواستون به این نکته باشه
🧐</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/3890" target="_blank">📅 10:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3888">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TgG3Wx20qeiwK6EhV99rrVQjNf32sdTyMEsfm60upXa5mnrr-X51oYNmSKuQfYlv37Qjz80WlqIi4AJLhQw_SerTflms_KiZuBGu0iLIazjKe8ojbzAARMAy6tLie67CNsDpZDP8mLVC_z5moSxhgqDUI27JqHHAEq-pyVRiA9I_Thxfbfb2r1ugQtLFbvH9223PqQZOXvdd8al5iLJTVf07hi4MwNWVZ6C6WEQZIc87Sus0VBmhkufBNJzRQnLaiZWr6O_NAUpxMuj--UK2r5rlblnai2LdNXldwUMLlSqETfulOYB7d99rz7podymfFsLByyeIH-41fnbF8TgDSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gmPlCP193M0mrEFurUYErrBMZ2CM1zSO9KIeaHLlU93MarhjxZ-vNR_iRNNeL151k7vGIyM1dKq9H16BS6LBOQATVQ7e7j05Qq7Yh3sdmhM7pngvyCcHg5iffD09AsagaH90Etgl8wwaJTXuHCnTo0V0-p0w7TJTQB0KRx8bDneeLDcj_ZHu5ZDXP3sm_MVE2dWDFlDlF0IhE3dN8hHsS86zi1EEUdxK5X9xntoDBaZyCZaqX_DeWb0L7nFD4hVqks8tHXMpZGlJzbu60TX6Ubjol8iUJ08dhLgEN6Is1Q2_dJMZdTSncobPLCj-dJBaC0Hh9JEANxpbAhNkdeesKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور: @nahanproxyipbot</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/3888" target="_blank">📅 10:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3887">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qFj8_CRmfIVH2gDyn--h616J6y7Ra1MDsCStZW6jqVZOE8DBa3DDz-PU4aRYO8hdc3089w_CfDfjow0gwU4n3doHGVmkCdfddB6Su0OyXne9g6eDPKlYaQk5O5_VWGLNAgLyaMURHIYkFdczhvF8rXhw2-q8QjGUL9ym6pH3slNO3DQBzLVRmZ-p3Y1DPfJmpzVj-aU9HN2Fqaj0GGDAaJ3Sh4YGiQDASDwrKDfsq0iK0EBxb3qKNMMUJ3ltnbg2yorTUS6enV2DBzPk6hkKqewbKZ24nqULCj_cAUIVV6K0pN071GaoJesS52XXIl5Ghgek6ZxrAmUYBmHWqVFReA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور:
@nahanproxyipbot</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/3887" target="_blank">📅 10:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3886">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خب قیمت دلار اومده 165
انگار جدی جدی توافق(که نه، تفاهم) شده</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/MatinSenPaii/3886" target="_blank">📅 09:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3885">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vmn4IdrTTV8EDkNQ7uqm1pcMw5EMRENkhB9Q-XpdmQlUkWlq1gPTw--Z0iAPTp-2PLLTYHL-i6vqkMsVOWObEesg1cT0GjcgbNh7t-NNCSH-mAq_SsF944f_kmd6x0Ebz-yfLaPlQCuomOAwYKejayU8vi8Z7QUCX06Jt13mErNmdh-StRhk4MO2h7YesrUqLHUf7LxiyrRRpCDpBnr9GgozHMe_hBt55BpbkUsnYbThwiaQums67m3-8_ZeR52LVtlFBwCVgLHt4R782GShcR77x3UPwdwxaKQtWFV3ndkn-pemE6OMBpISzJGJj9vTSKfffumoD9CXkivmtWEC9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/3885" target="_blank">📅 08:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3884">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/MatinSenPaii/3884" target="_blank">📅 21:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3883">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/MatinSenPaii/3883" target="_blank">📅 19:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3882">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JKpLnt8OvRL8nZAr0IRMZktKWFuNSpj5Yvn7TtuwqdwExHCJcoIB-cVFCzs6dP7UVWfmrlknGBsrV5Xl4LAcctqB8HyClo3oUky9xJpgUTJ5ZaP7wBkpsIj_NGrwQqV0TVxIx98KT9tigvcuMUPTWekCeUtQkEJ6XpBlIVa_lO-aXFClMCKN8vgH5yphIBdgRe8Tgp5NqoYmCVOLYO5XCVShmkRmeoeLcdNNnAYcioQORq8JWs2dbJKzbgSJbabSk-BdLuEK7td-qeAJumjNKlHz5RPv1dUteXM73zOK4yGIsPSAn5o0fAH-AR-LyKc5nf_bTdXRPPmUKK8v3bNxQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو برای اسکنر یا هر پروژه‌ی دیگه‌ای می‌گیرید، ترموکس رو از گیتهاب نصب کنید؛ درست میشه
https://github.com/termux/termux-app/releases</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/MatinSenPaii/3882" target="_blank">📅 18:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3881">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L6IZQPYBu-a3pip960W_cFLazySEmfRhoIZ5mUApZgSM0AS1iGjrW3_mcW59CBY_dPFD8LkfNjbKxgIJDZXhnUBU19qzbfB0cXTkEkCG74PoLBEHVY_Y0cUnnzhUUvfR1ROjRPezvKbERhEnpGCsamudMwpaPz-oLrTvd-fuwyYq9QSMjskW27Gfcwp9GsUN-h4iD0iIzRyQB6h6kv18CGPjT9DKTljO1uIdwdbHW_BfEE3KmnNqHt7bTTDJlj9q_i9a-pHVsCWV7j0im8C6lbnsJdL_i1yzFTYXX0H3DeytZ6hH7PMCuagmvFM1zzd7bccdBUD-m15SwUllGwVNyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/MatinSenPaii/3875" target="_blank">📅 13:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3874">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خب دوستان به نظر من اشتباه کردم و فونت وزیر متن هستش. مسئله اینجا بود که از من پرسید، گفتش چه ترکیبی بزنم؟ چندتا داشت، یکیش فونت مربع+یکان‌بخ بود. منم زدم همین و بعد دیدم اصلا پولیه. اما الان انگار وزیر متن انتخاب کرده
نکته اینجاست که چرا اصلا فونت‌های پولی و غیررایگان باید بهشون اشاره کنه یا دروغ بگه
🤔</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/MatinSenPaii/3874" target="_blank">📅 12:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3872">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SUBE-GzXQcy33r7aFyRzSfUrVMfB1J_r3VJpRlURZziUrAQAOwBX4oYLaV14paLmLwlG1d9ruR7fZ4j9zQm6p1BOUIuvgv4RO89mCB9wNlXCmoMzhn1CueiJ2ARtAxmQPHDms-IUeTM_bQUa3uTuxAC7-z292uXSu_mLhhyllhbBaVgz71KVRcbkk07ffmx2qTd4Wg9kryas1Eu9R2SOGFaBWAx85Ya-Dek3zLBDFT53cDJA5pJCUB9DlJRP2ElyNyi1VhTGmRrT6e40diRoCaiGJ5v11H7EJ4APDHfK00M8qEujiG7ADApF-EAeQhTmxFY-KpV26LLylCDC-E2ULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YhjaMoB_ndU7P3RmOdm_ql22g6PNLxiJCvid1C74uD8N_X2WSOAldR8Wej7xX6PH0uOl4xK4KSbVa0VS1PUZfP8BxO9uOYhH-emm8j832sFP12FRyp7qnOUD8NzmTxLxbdFd1KKJUF8PxpCQ4y3jEG8HWl9EsBjZGEBJitxDviZ6NoeRoRUxfk_ewJ49aryseKJJKkYvfkNvYHCERpEkg75SUVsjMs-tyXsDtg0DE-wSmNhY5oDSbwCUN_bX18z_3W1a9vwYwL_zQhXbZyDhhZFYw9kySUz-x3I28o390S6yb20d-8h5ixAyPVirX_kDSNae7zcVAC8GXrAE_jZpIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم کپی‌رایت برای کلاد شوخی‌ای بیش نیست. اون از قابلیت اکستنشنش که کل UI و المنت‌های صفحه وب رو درجا کپی میکرد، اینم از این</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/3872" target="_blank">📅 11:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3871">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h8hPI_MVfsxLDrUBlU9VQHi7EkHPB71VKAes83I7FqxlVX1zaWx203GAAv1pydS6aoX9sCwr7KskTwi_0A3arwvZsrPuZ14Vewm7krkltONVGzfcOP_dfxU-ARiO0Ehrb1GyKrRFZtgADXm57sm_K6cSpOYa2tppLc9yUkxImsMifewWES0FKK7HKNFwL_I4W-N9e2p2ujVWedpRViSAfOJuFfptX2F8cM9Ou1MLv7SYFBacBoFZcycT20RZ-SmV0NCSXXMjK6fNZLl3Vkmqus-SfQZ36n1mNLa7p2Hd67tZJr9pjj-2PC20O9P6c5s7kZ976ArP4YEsskivqROjww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/3870" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/MatinSenPaii/3867" target="_blank">📅 08:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3866">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7ArP42mP2AewSroHyM8f54EmxLh8VADBVJf6o4UJdqLMmyQxY_jAvOD4kvPFNkQtQTxpIUHQuBQ6lC-vJvuzNZEZs75waKFOjdoRyKNL1CE-SvQm-Rr7UiSDyKPSjzk5fS3YjGcGg8GDBF847-YoaMoZOZojg1intFpXB2Sfc0LtQtZKOUMD1LhPIG0M49iqNcdTFiCGfnwHCJBv7RPLTgJ0Jm9LyvNyhFXiRbawW8kFB52mh-EmI3ULgNEhCs8in-KDxuS-4pGingfelj5ttIym_jlF3LRcBPo68EFAV9iosuBSU1PX20d-0CzXSxBkkP8rePk85tW01U0Ugj96A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/3866" target="_blank">📅 01:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3865">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JV175HDxxX20LzWa18CJEih1bXZV35GmLrLws5kIrv7PdoefKfAeLx4AL6BTki99whMMfQMZ4fLzRmEUECJ_cn_VxR8MdYpCI3WsRXUuumAnOPiVqFeLXh2ns1y5pjea_RnaAoLDkJPuBDKd2IjG_fnrxlEyOCIHPqZxht97DVPUe5VGEeMJNbrN6Hb9P6hPrBw2KZCPD9EDfxVJ-e1-J2OxUlskGVwWMCTNn_RfdLsNdR774PYKQ84DtlR7AOrdbHW8fzkkZn0-DMEZLaWHa0cUkyE7aR9SemAee7B3WmvWEiC6vLSoT3ndM1oDjzsOJoUyPQ2t4YHUVti2nTD8Wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dHhxOotW9yiuBDeXm4-Jg_b3zpWt0EtvUz1YmrG68fopmMcghKp1kBvWMaUPO45PmOHys1u9nBstcbRE4s9-T4m8KlqlV4OPkFlzu_a2CLOISG4cntOEPKYjR6RnPoqPBG7JSQXWSV6uq03ZB2t__g2xkF9noccX7k2Rt6LjNyGowXfyNDW6KOFAzTjCEx_Dc9xQQKyH6sA1kntbNaz2ISFvT091iilHW8h5LlEOhrYIduq2Hx0Zi6oQEW7fCR-UW5QsTdNMPPcHRyn_vg8Kc_3SRbFnli3HvoYDWc1D8vlM5UMu7puwDw7hAuXw2ooYjwBk0IpxB4fQ1A_yshQbKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jfJWnBH8-SbYhW3BhXRWJPwGkuWDAoxWKJOAdko5Q7Cvt0hF2wFOXruYE9iBSBVZ12z1OV-gXTDe3srrnKPLmSZPFJ3Q6GXFnyspV1kvsFWGJACZvnmuBRGPYYGD2hJZAS8x4cQtyjMoyFLB5S-UPctIurFxZ6wLfWRHBfA2fjcFf7Rfy70bbjLqJ_ltUacqjiCVhtkvD3l-Jk5tROf1lxTQDC-v6iKK1Gu9X-TDmEU4PWNqaFwlc2lqBSEUKJ8TkJUiSMLSUxpz8LNW35dskpsz0mmWcNP4nTYvqNvXnlBQITEwEIw1wD0VVk3v3HQS6vP9yA6KfAJGWdJBQhvD9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Wcn3yG3MSNzPfeDLV4H-GGQXOHzq3VwScadaiPyNJq3Ws01WVlxxXhjNdhI_2vvLM5tP1e8iUgtLdMWBEfyPEuSMvqcd1sNfdCpLngpj8CxHS7YxwDDyFHEuxdeEWPjvb8S1zHNQMDm_7PQhZBJ7l5qV5Bj-VDOdFkSlQ5EwU7O0PscKdr9xOqUm7-wlcskjunx8XmwGAbwzMR8mV-DoPDLMaOZCl0_64ZIqLtzZgwabxJOzmfg1vv1p1MtvOzIztS0Mo8mVvE_v6i9y7oyE0BS6qelK2GKGUbMFaSk2cMWpt_FbIaK0e_mb9hnZDv5gIbla9OYgMIsW0XWmjPvJxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WnvoZETjwUqFhmq6YNbS6fRm7mUb8JtHsky07Uw84oZ3AfQMYxUh9y3-EA6YXoJTlKOqYVESWOikBBuBA1TV2gEaVbWdOxz7g-EvT8L6Zn1fXi5GntVhBWCWWInIKZHQAfbBPf5n8UgzudGyIG2HSnniwbJERvNsLt96OkYt0VihKJmfJpflnX_TKGyISEWTDnG6mm6AwQXibAc-aAlpTpAYjZw0gq4pQQkEplad5sbHOpXIzSpxRxSZghNtRSG3BOK4r_YGJMpJlM9-EW4yC9F6542u5vFwgahBg31uf2EbWR8Oc7xfK5s3oeZ5N9cpWIajNP2p2bOt9PrXumR7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fahS5IGXHnqc25uP01aP3x-tjHRUB8rm3YU0EAYjGfpsH6a5b0037804gVy7BmQBd85LzYA3OZ_xikf3PCAOHTnN2cfhzZIbgZI7EnZV2v6SIAbjwz6fL5yYyYplK519fQoR9XnDZW3V2Gt5V_Fic5K7RnjyOiasmaFh9Ha-X_DaJyuqSnuCmIImnUpcx_KfogfhEjNxvDQE2l18zufYk8Z0sJltyV1h5B8hfZDwZ9d8mEskIMAAfq_jN72BaSvj6Ux2oBVde2DSQ_dy47KWOcu_pT9ULgeswnu07153TMAoGSnUf_d0ZP3HSgMECbn_QrtJENP8yUMO5NPTYNYs_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/3851" target="_blank">📅 11:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3850">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PlhY7LndlkFFrhQoEOtdRVcF0qi9qHJS00H9bSleyhRp5OPqsuG79f-vS-hoNJGnyo-sLGlRRl2dB29DhRZ7IZbKHxONigAFWKAwsBACMaPklcO7kiERoI8vZozKMFPR6qEOiavpEyQcu2NOG1itVx9t_pQfhfY66s8W_ZCJ8ywY__dE0G2o8zP5waXida0utEhhzwodA6RsvFvrHkNVNjpWSSc4m6vDnN-i748s18X7AFL6WbN4P0yfr_k--bOuJzUTMbHMwbFueSTv2xQtkbNhZhdAzFt3HOM_XTSViDuxBN1gL7OAfI6w8cvav8uMc8dF1tO0J1BPdZZk8SyI0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BWoTeZOT2Xs_I6BlCxhBcTxKhcZZVYq5eGsdjbGUNPQA2Gp2ype44xiGrMDU2EIdpanqDfukDE3Qj8li2RrCXSES6ldUeWV6w1jrjU9Y5BUsJc1iMkKJ_GrGKWNnYiSZtElmtObmzb0zJu3PvLPcUe2RavnQb7_Z9HFELk1XzwZRPj-ztWRqtQEMK_Cz7WRxvOT7Kti24yKvOaIXH5o7B-oVIGU8Ff21A9yyjea7NVXt8HjohVyechwLuzuXugKtNJfP_0mr92kMMUp_Mopmg9L-j58BT3gTNyJ_J2SIsfXcNdXSNik1IK2b2KS8B6cSkQtjXZq5T_zag5aE9tjCUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/3837" target="_blank">📅 10:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3836">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qO9mTyH7pwz36MmqjnUBsVW0muIwWTOG3ngpjDatVTCWYboytttnjlrzrV7aV0B6E8DDlBA1Dccuio6nQriFKH1hG5eNxwasS6aSC-jw8dq83MspJ7m3clUzxjXVYEhjCMVJZtisd7mrKcQLRcjX2B2_SDgQ3yhh9QKdPbBevS8dejYdbh3c3FwJ1kFu9UZFN8ws_GcHqBHsSvuwZuHlShb1M85QAKdjlhpAyvbZNkq6pgm8iNkEy_hN7L52YhTDBH3BCzcZTt__mzcJ7_4lSeMHFVcFmjc5R9Inq0pa_zIYfqgjgpURCj40eQl5xAuMMHQ9NNgVj0DNmRGO7qnaWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لپ تاپ اوکی شده الان اومدم تست کردم MiMo رو و خوشگله یه تست پرفورمنسی بریم باهاش روی SenPaiScanner</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/3836" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3835">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WGiWyPtnfbBC_5vm2IS70CGXagfuXBdVpQrjt39_rK6uHGPwdXyM9-v54T5YkBItMBhKzihbG4Sg5anmI7YXjnxqktbZ3tU1wLjXtTzIVbNgUFYjSTK2ng35zgmpDyXPQ0j34XUp71ajp8NxOxvzeWcDyvYNh-10BjFmJCUmK5PgMIFzJKxHnYbIvTxhg7vDDsr0J62EdM49d77508evlZDEB0xARmtD6cQznDAV80idWSefduVHSTbKp4wVY8zWTy7V5sR3m3ib0e9_5ziSQ9zBQpPnJ1HFZj6qnHs8-ruzYJVfNapTXgMi91pD_OFVR3Hb--mAj6bA5KlXcIcO4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rRahGwzoUH2GF6x8vHo1ZM2hwbh8hZ7HABxr12zCupjONMOZX8vUbwprrt1lybMoJOXxRUbQq-5WI2WLw3sGxjPHWqQ25bxq1OBoWXOUPBVKn4oEnkQBTpddYyAXWu1OIXvgaac1mKVUcPnQkN0kIdIHtWpzt2yUDSSP2kU8SWG4hlRInijPTmecHe9mcYFGfWxkrPcZNe4oRNoMZxmKnwp7v63qoLat1Cu-IO_umTe3pUd1YXzNpiULyiatetaZeDSCU-H0NVBME3Ef7_tXwWvKgqCpBPT6C87mf0It8k7nDMWMEKO8I7FOojXG4X7PMi9MKMfqP2auCEFg9nTGOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/3833" target="_blank">📅 09:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3832">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید http://l53.net/</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/3832" target="_blank">📅 02:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3831">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F57Da8nz7S9QdoTo51KANC-yBCwm96-QW5STeRQ54Vyu8N7BGMAAozuGf3SzNzq3tYV2ICZhe2IEQIMVyipHA27antKVAZ3bPu-QXiMHkJwg85CTsM_eBwVwYXzWUPFeGCCByHozN6cTU7aGyIvXhMDVy0wtjggXwxWCVIdPQefXYEfRw1LH_6hP6monVroa3QlQ6L407Mq1Ektm7FN4r1U96cKoc1IjdIFWitqw1WU4xeAd32v467zFc-f7konxSwkLgQBZ7sI54bY5ZSZYHv5U7T9Dtb9zVghOSk6HV8qK5RpPMo8CFXB3PcxR7foxdC3somlpehViTsuUuGUmBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید
http://l53.net/</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/3831" target="_blank">📅 01:55 · 23 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=lklz29O3gMB567A_NBOxrCE5xf8lS-_PX2OB65gjWWFpJiMzVUPd0j0GIRykxWBcElHSeJxKVDcVH5r0EDeCgKhrF5tdfZCKTb-isFkrg6EoOEkTJHUKEw83gI7H0i-88oz3IDCdmHj3Cxj1KHLB6PI1P38wZQRfvIprkmcxAs5HuuVLPSqf6CNhtzzLGLDh-8wEyHDpnngMEPYu_1hOAZyNr1osiRq2fEQt9cIYiocUPvSznU-uK303a0S7csHoa-nnJIom3WK9rrjqRPX-gy9cKw4W33-usJVEUR1VgmCfwKQAWY4aGVkCLbUstpV4pdCpPm5BVAQI_FKm87K81w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=lklz29O3gMB567A_NBOxrCE5xf8lS-_PX2OB65gjWWFpJiMzVUPd0j0GIRykxWBcElHSeJxKVDcVH5r0EDeCgKhrF5tdfZCKTb-isFkrg6EoOEkTJHUKEw83gI7H0i-88oz3IDCdmHj3Cxj1KHLB6PI1P38wZQRfvIprkmcxAs5HuuVLPSqf6CNhtzzLGLDh-8wEyHDpnngMEPYu_1hOAZyNr1osiRq2fEQt9cIYiocUPvSznU-uK303a0S7csHoa-nnJIom3WK9rrjqRPX-gy9cKw4W33-usJVEUR1VgmCfwKQAWY4aGVkCLbUstpV4pdCpPm5BVAQI_FKm87K81w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
