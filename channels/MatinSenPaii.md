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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 01:30:28</div>
<hr>

<div class="tg-post" id="msg-3963">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یه مصاحبه‌ی کوتاه 13 دقیقه‌ای جالب، با آندرس هلسبرگ، طراح و یکی از خالقین C# و Typescript، که هم در مورد برنامه‌نویسی و داستانِ ساختنِ این دو زبان صحبت کرد، هم راجب اینکه آیا AI قراره جای ما رو بگیره؟ و نظرش در مورد Vibe Coding و چیزای دیگه:  https://yout…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/MatinSenPaii/3963" target="_blank">📅 20:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3962">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یه مصاحبه‌ی کوتاه 13 دقیقه‌ای جالب، با آندرس هلسبرگ، طراح و یکی از خالقین C# و Typescript، که هم در مورد برنامه‌نویسی و داستانِ ساختنِ این دو زبان صحبت کرد، هم راجب اینکه آیا AI قراره جای ما رو بگیره؟ و نظرش در مورد Vibe Coding و چیزای دیگه:
https://youtu.be/CPrePbvbbic</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/MatinSenPaii/3962" target="_blank">📅 20:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3961">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/3961" target="_blank">📅 14:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3960">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/3960" target="_blank">📅 12:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3959">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/3959" target="_blank">📅 10:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3958">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وقتی اینترنت گوشی رو Share کرده بودم برای لپ تاپ، بدون VPN، بهم آپلود 0.02 مگابیت میداد. اما همین رو وقتی با کابل و PdaNet+ اینترنتش رو share کردم، سرعتش شد 2 مگابیت. یعنی صد برابر
امتحان کنید شما هم، شاید همین اتفاق واستون افتاده باشه</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/3958" target="_blank">📅 09:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3957">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/3957" target="_blank">📅 08:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3956">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کافیه یه آیپی تمیز بذارید توی بخش Advanced, ip fronting
زیر ۲ ثانیه کانکت میشه</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/3956" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3955">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه • ظاهر اپلیکیشن تغییر کرده  • امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.  • پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.  • با کمک یکی از بچه های…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/3955" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3950">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3950" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/3950" target="_blank">📅 18:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3949">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/3949" target="_blank">📅 18:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3948">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3948" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/3948" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3947">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kmTL0sg_B-qSPZvQiTQrSmzyv0KNsSPAXZrbyV2x0PZ7fa6ntwNZUd4bHcLJIXffe5nEd3HU_-8i734coL8_TvC8nyMJZl9kX0YGRHof8B-3wpdHksPYCEK8KKZ2Hlz-vls2IOIOAfczwe3eW0EBx0m3QZSjoAImgdecf_1a0XfluShTrt6bbWK8NTCeu6A6QMcXuN7T-fDZhjYidX6KYycEzjTyHbwDNsri1iFOI9wLshZyb1zRR6trwOBamDumTdQ2SO6ZfaRcA1yc7k_9wM_yiHjXyF2cm9ylvQluLvbTWggpL8JKjdpbAktd71tv03srgfJjDOsYuGRzVhKcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از contributerهای پروژه‌ی senpaiscanner، دوست عزیزمون hidden-node، نسخه‌ی اندروید اسکنر رو توسعه دادن. طرز کارکردش دقیقا شبیه به اسکنر دسکتاپه. نصب کنید و یه تست بکنید
👇</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/3947" target="_blank">📅 14:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3946">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/3946" target="_blank">📅 12:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3944">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Fsq62HCVkbSQTYtVdgLNbjW9DmXo50dBTC1nNQDazljCJWXEGfvo_O70A4FCjNQonDuAxmhPyAcAmuiAEAcr0YYiMg71gKRTrIl_X_Qf_ddjS2BsmSGPZjuyFDB8vF0fPaaA9Rkf5qRmYtRBJmeMm9v8aPcmYDBj4yC-6s65jyCGyQwPwJ_FEesxGJHHveCfqh-IB-nGiyggvduaCrCyU3bv2-WLpEIDXZcVzUb_wrNF21TlRUfy5cO-wFXzgk0qGnI-J4yUkuNXUi9yrTP61xwNe4twCnwIQnnrAXSHSBhYv-ozTTGcJEzS9_YWo9yIlnTshg6IJ85izfLtXJHyrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ewz0xeskOM418mHuhRWiRNnUM4JOQqb5CrmJqUlIrUzkssoqaam0r2W8gwg6oUIIYptwU3PpfwQDvcloEkkAL8WZ9gBK46YROcfsYB6tnhDq3nIc_PlAj4V5Ooazpn5k95NncUgw6kpwZVx7ahJCZvWn2jjsL5lQRdJzYV41hqkc5qKZAszgM2HLkdCpGEajg_NukMgDuietw7beiB8u24KaW3fwaDXgKl9lAOi7asMewGTwnKqAvU3y6T9w5hKGw8u4j-uDjBhyTU2OerLomj0J1uZhF-UUuIUYAgvi10K3rJctJc8J4H6olHa1JJAZAlK5ju1x9e0W9JpGgkCaJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از بچه‌ها اینو واسم فرستاد و گفت گویا V2box، به صورت آزمایشی SNI-Spoof آورده. یه تست بکنید ببینم داستان چیه:)</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/3944" target="_blank">📅 00:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3943">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/3943" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3942">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این پست سگاروی عزیز رو بخونید، و اگر دوست داشتید همکاری کنید:
https://t.me/AiSegaro/120</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/3942" target="_blank">📅 18:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3941">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/3941" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3940">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/3940" target="_blank">📅 18:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3939">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SAw8dIpnB-ladhUmST4lUt41JMoWS8-tWCtaAPaTNcp-vqkxp9ucIf-W2sEkhM--S_a9_4qmZeGOvjadEPUEpZxZ4Jwtu1AIE5K0V5hvG2eDz1R-UgGXS5eh9wY0phAaChSjD1j-dPqq9fghLbwLpJ-JR_shOEX4Wugq6d96dB-um8NA6mtA-HZGc2KwT2Lmdo5UQblF7mFMMOCovEkPRzOj7X3jwEgvj0GETD4dAG0yjxIQfeLSuvpnsA1bGudN9r6PrNa9wX_Y38tDB6LoL2a9zjXJzDnosaiHSg86zNBIj_f8jLoMsu9lbUFiHMHV7ulJ2-vBdwMpxvb9LEzx8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی از دوستان این مشکل رو داشتن که تلگرام واسشون باز می‌شد، هیچی دیگه باز نمی‌شد. یا یوتوب و ... باز نمی‌شد   مشکل احتمالا از کلاینتتونه و dns اش. باید تشریف ببرید توی تنظیمات v2rayng و Domestic DNSرو از چیزی که هست، به 9.9.9.9 و یا 9.9.9.12 تغییر بدید. همینطور…</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/3939" target="_blank">📅 17:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3938">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/3938" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3937">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ویدئوش آخرای ادیتشه
🔋
می‌ذارم تا ظهر</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/3937" target="_blank">📅 10:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3934">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rn36iciUG_1x3Bv0ZatJAnL8ssEIYWcrepFSET44DWASEw09OoqdD2TbVYW6UExllS8ELxff-JeWTLwzUl0RuYHVVoucDZwPDz4ItwfzHYVD-xVKx--Ya4yentQkqf0F8YlW3CZO2-82HkZ6z078GuELTgojcPxKumje5p0xbV--iYoBbZZa4DCw76RKjx_LH1T68OYK4dqa0AA8VzPxVFQCGLhdmjzL0CqYuYNhXZ-T0HX1X0f1iWIkBQKrnCKpQwUsFwjtLBCwGZyw6AC8MqaEeU18C1tOdt1SpW5lYakyx067B1yJ0_voCsG51ibSUBfiirQVH-_-Q_WQquZdnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F18nSMTvBWysFZdNXP5BmBoXu6HrT2C9OBwjkNXQPR6uL8aCbqZxF8wyKsxuqrFGsdr0XJ0GCsY7U2297l1nBgyMtfataYE0snCsg5O-r0PesEo50HcwRpQm7IEM9EpsClw09-3iGneZXgL08yyfBZEee_UMxf6jv9AY039oj5TcJ8SPsX6slMZXQy9_FhQfZBA47LCO6VTwxqbdZiNfhfjxPmL9R5YChoFQm4yxbNKhmGGv_vHKtT9s5uYijokpJRot-o0JTh-2NVs1uhNbUH3t7ccCv63bKaYuicftW-4KAjCHG4Uut8Prb3n6o0h2Z6E9sSVvwpEcCEz-p2JOgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HQybawzkwmVsxmFhn7vRXmoSvrZaWPhI7JA61udv6lux8pYhq_T7TsrPzsYHL47x7uQuNqI-2w1q2RhRP6GDONqcIGihLDLcEvGl1RWTs3HW0BC-s26_H3xj3ifG3IAiQuNvI95VZDD_lmEDLldGlDDrp8WIaq3yjxkcNGs87WpjbUqI3_nEULI5JqZTU9O81WfC2wC7DfLaSCaoREc-RmIB9SlOx63vklXjudlVHAvEjOcvXCnuzd1mBeMsaiu5BzCnxEpgeEACIetXdL0d19p1fcwflQ-qUwzoMV1A62mJ47FWAQUudOx9_plkoa_NmEWb6d4HH4W7isVTPFtg2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه اپلیکیشن مسخره‌ی اندروید با AI گوگل نوشتم مجانی، توی بیست دقیقه
ویدئوش رو ضبط کردم که به شما هم یاد بدم. اصلا چیز خفنی نیست اما خب بامزست</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/3934" target="_blank">📅 23:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3933">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">میگن Cursor یه چیزی ساخته که SpaceX اومده 60 میلیارد دلار خریدتش
نمی‌دونم چقدر حقیقت داره این حرف اما سرمایه‌گذاری خوبی انجام داده. به زودی CLI کدنویسی grok رو شاهد باشیم احتمالا</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/3933" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3932">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آموزش کوتاه استفاده از :
WhiteDns BPB  1.1.0
📱
📡</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/3932" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3931">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ورژن 0.0.3 خیلی بهتر شده رفقا. حدودا بعد از 20 الی 30 ثانیه وصل میشه روی همه‌ی اپراتورها و سرعتش هم عالیه
منتها می‌تونید از خود Wizard استفاده کنید و بسازید برای خودتون</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/3931" target="_blank">📅 18:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3926">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.3-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3926" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/3926" target="_blank">📅 18:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3925">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/3925" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3922">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QK1E6qn_d55TfU8HK50gVrYQmVf7dVmnaD-B7FOKJrucmS1BIuxg4y5KQdm6JVM5UBchDbSEhJJcDfrs8NFeOPhW39CAaRzzV_b-pM8rNoOfHaQK7xPWVfpN7NItGO4fzn5HV_Nn7LMBDLb5sSx93iKC1kavXNCGp3C8rXxeDgaD2yy1joow-Sp57DnxEloIT4QYgyRiFQHid41Go60FkXASGXq201tnCcF8pdo7ZzA-LanaO3wFMILOu2-ILU2fDXGzZ_YzfeCnL-BLvRO6NoWPlI7AYrAihZa0siEh_3SDwqxOrBbf5wYkkQode8tFAiHTr6_hc0MWOA8VsZqoUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X5sRtEdia9GmjlNTiZQJluw9_KYlMXyN-aDVUOjpCpaoGXm_Bplt-vO0LIp4paLl_CjX9fhGpl4rjsbwo43KKV6eWRjpe7l3jdJ46H8IAGmhdRX9LMDVzqiczNCm9mPP42dgmry3VP9CaIDdNLEwXHfVtawNl1oYbghRFUAe0tbM0rEVno8x5bJXjV1PSsNtaaxOWLgwWQFUNP7OtG2948wc8-yY9VAZVQqrKE_FNKH3ESupZtGef5KAx1EC7jjZ9S74wrVxXNDNF-ftLNGt6Ujqb4Zp2r-Tztr9He1fF-l1neSatZIZvMlDa7Wnm9S9VSFGpwqIY66jDcdoN5LfWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SQvaAwV7S4vXk2Gqa-J7bfVQERVjV_Qirm8P_GrgJsuOXsKz0lZJqozCuOuL-5T9alQRMQLZszxjqY-Jf25LSKbqYiAUpakv2Fr4DUKWj4LkIHBjVEKbcA7HXHjaSM1A64riT1lIRWFh1oMRKEgfgKscdUS9uIL5HOHq7j01d3-ezekJkHMc9Hk7wMOwPzA_L2pSqmtoM5Qag8OIrRhbDf8DOjT3_miyJ9I7kRmFJlqF_H_y885-b48fNbfwPAdLdbWBlO5BFsbIXn673n_CxgLBzdhkYE7IfE5-42vGXdCEn6XHmHQGMYxsf1Rt6Vch7lI5cAmu-nnNtiI4KBuR6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بالاخره قابلیت ضبط صفحه نمایش به همراه دوربین سلفی، به اندروید 17 اضافه شد و دیگه نیازی نیست این کارو با نرم‌افزارهای مجزا یا تیک‌تاک و... انجام بدیم. کلی قابلیت باحال هم برای گوشی‌های تاشو اضافه شده؛ از جمله foldable gaming(که توی تصویر دوم می‌بینید) و ارتقای مولتی تسکینگ
اطلاعات کامل تغییرات:
https://blog.google/products-and-platforms/platforms/android/android-17-features/</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/3922" target="_blank">📅 15:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3921">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">برق داره دوباره نوسان میکنه
اگه سیستم داشتم به جای لپ تاپ، از صبح تا الان 15 بار خاموش شده بود
فکر کنم باز می‌خوان قطع کنن اه</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/3921" target="_blank">📅 15:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3920">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">😂
😂
😂</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/MatinSenPaii/3920" target="_blank">📅 14:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3919">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aDqxgSPPmhZEiBDAj6se1agrd2Fa1LZ6vJMOOWgJ8ZBPdJpQCP1grQzbyu-MNSbDJ7ENto5oPkVDiEvSZRsXBxoWvQozTpwBdQA--QGJAPf_U5qg0zVz6KgLyZozfZpoQ4vUekJ-cLlLY8zglcbERvp3UqRv8hThZn5XCY7LSwdYAdhFz4w7DJ-0eyHcDJfE417Cy8pkgMExuKu8I7MbMrE7e_hPDA3puCOFZxphMGNA3E_l8NWR6AkVMnAaa94IvCYDKfX2wzlfvVUIhGA0-1BvNacXTUqAzWZ7wsGhkZM7B0xS_U9CzLyfzz58n1_8ZdnIOspGaK96Grf9mkaS2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/3919" target="_blank">📅 14:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3918">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ARzJF9CcdtMyjyT1Ax6lU7Vb_c94QlJe76KnSmjPNkQl1KWEgnq0DjXs_ovY0y3yxzpoEoKjscHs4IGFnHgvDW6M04jB3ad0SLsHnDYw7RR8JVH_Pkvf-5r-4-fIBeaVEger_pWjBftQIcpvJ5DdV80a82dPZ_TvuXq4ZfdBpfjTO7MRZV2BFDljJ1Nj1SfBGzWDH13wrj_M0QmCC94884WXhPIREjvpxGjlZMu4yUlhNPLKZkRa9fCPc4kayt7CJ69tUT-CcSh4uvaI8AVqxOZiPBBxaliuwjx6_h3gQtjdKyqWGR5KICTsqFDxiKVbVlazdsj9NDPuq1e7J1wlPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیدات کردم مهدی جان
🥳</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/3918" target="_blank">📅 14:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3917">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VgNq-vqO-vj-cmJaWIq1BnHY3c5EIXodG-12uB0KVNT-bqaOpqBzxXJXecDE1XrJ_Ro60UszK6IsqTMpAkXfjAZVyIT60P9RcoGy_kvku7K4hsMkkrExqLAsspLeQeqtXXHtOGEGreoBWBryH2bukSrKsQBKE6-z-O8h_e9pkfhhmeNnBujndFCDPjj8bZz3o5Zwj34ZBaIqsmQFHBdzmX46yjWEsFlLCADCVCfNwdpw-pAVKl0khh3DMDKsLLJGSjvPRqtRFtxyHUbg5jvZfQcxPx2bBk0tBYdKVslaBmvBuWTri65Xp02MG3GNcbFRVxwhafyNXhq2F2cQqofTGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندتا از بچه‌ها تفریحشون اینه برن وارد پنلی که من توی هر ویدئو میسازم بشن و پسووردش رو عوض کنن و برای خودشون لینک ساب بسازن استفاده کنن
😂</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/3917" target="_blank">📅 13:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3916">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/3916" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3915">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kHJD6MvUVsVbrlVKMVeFaBjE9hEk3RSsAuoeJGfIhy_MniHVP1NB8892Pxoc6larRCkUYkA9Gpvu7mJvTwZd-oW-UvkqOn-HUoRYLYswFYL_C6udQmJurGtJ4fZEN1h3wG9Qvmai5LijtW07ce5nuEgZVDyIxbJKkTYmjLekUMOOZvUJsuzWEPtebhuSBkZ1DiUJhdxejGiOAREkA_hLQzqReXqouvtsy-_DHCh50lHpdLapLsADOkLQV7IG6FcQeob5ydfNHESaYONbBRM95h_XmKjMfbYCI_o0EvvE_u34Dih0fOZoftLE6Qqn93O6YzRWw_nsm71cBKU9FMDtAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/3915" target="_blank">📅 05:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3913">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/3913" target="_blank">📅 03:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3912">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">من که عددی نیستم والا نمیدونم وحید آنلاین و اینا چطوری هندل میکنن که آیدی خودشونم گذاشتن
😫</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/3912" target="_blank">📅 01:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3911">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/MatinSenPaii/3911" target="_blank">📅 00:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3910">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3910" target="_blank">📅 00:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3909">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/3909" target="_blank">📅 00:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3908">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DnF39VnbdQhOKqg_qBf7rS5QhQ9EcwTX1kOk_IAcyBYw3_LUKgegyoR7EgTwaaooNIKZOmkBWu2kxOINbGe5OLLq_xJ5w09pmDkB1ho6X2MozCRoM6SmF6qwcXiBrppVmfubC7BjEYfw7lnNpPw9RQFpbz3x3rAuLx-B9JzeqSLrZ2iZh4clI9Cegk1DqJiGxMLGg135BWyGp5_xICXs4pubeuVg00ncnl4cDax3tcQFDnqNj5M8MYd-UxcGHO0YQspecWqwOkRi_k_iJePvrhMJPPRjUXVy7LSpqwGqwrSrypC7tpE1XsXw2NRfrd5NDhdV3fVRdaQKSp_01tvtGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/3908" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3907">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">متشکرم از بچه‌هایی که دونیت می‌کنن. چه کسایی که استارز می‌زنید، چه کسایی که به ولت‌ها دونیت می‌کنید، همه باارزشه.
من دسترسیم به ولتم قطع شده بود و مجددا وصل شد الان، دیدم دوتا از دوستان 3 و 20 دلار بیت‌کوین دونیت کرده بودن. ممنونم ازتون
❤️</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/3907" target="_blank">📅 20:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3906">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">☠️
ساخت VPN شخصی رایگان با پنل نهان + تنظیم لوکیشن دلخواه و آیپی تمیز
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی نهان: https://github.com/itsyebekhe/nahan لینک اسکنر: https://github.com/MatinSenPai/SenPaiScanner لینک ربات ProxyIP یـ‌بـ‌خـ:…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/MatinSenPaii/3906" target="_blank">📅 19:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3905">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 61K · <a href="https://t.me/MatinSenPaii/3905" target="_blank">📅 19:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3904">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">داریم تستش می‌کنیم این رو، و خارق‌العادست. دم ویسپر و پدی و بچه‌ها گرم واقعا توی ۱ دقیقه پنل BPB ساخته شد واسم و الان دارم پیام میدم باهاش</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/3904" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3903">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/3903" target="_blank">📅 19:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3902">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/MatinSenPaii/3902" target="_blank">📅 17:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3901">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">توی NPV tunnel هیچکدوم از مشکلاتی که داخل MahsaNG داشتم رو ندارم. احتمالا به خاطر dns‌هاش هست اما خود V2rayNG و Mahsa و V2rayN خیلی اذیت کردن این چند وقت سر BPB
خلاصه یه تست بکنید</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/3901" target="_blank">📅 17:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3900">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مقامات هند، تلگرام را تا 22 ژوئن در این کشور مسدود کردند.</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/MatinSenPaii/3900" target="_blank">📅 15:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3897">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H1JofueyEsYML2UTMGtYHIrkGoOs-B7HKlYhH0PJ4mX9h8QIlY0FgSM_j_Sb3a077XOKsn92SiENoKbWgNQDyHPPjH5IovzKOD7U0B_JQLGxEgqtAR7DXRw-Hgoc3D6Icl70zcrsSdNTDTYaRCiRL6-9btyfKkaqT_X-_lYKXg8l3pBPDHW0GbzJxYTf2fB5NFtIdGzJpyrRAHCHNh-2eJL0koKFHUrAxpT_f3F-eDIydQzWstHFBjQVV18rwWTmND5dEohzURoxr_kKhsYLA4STSPYiFUkMfrSd3e2jYsMfRP31dQ_gCB-2ZQxsvxloU5JW7PnLbfoTxDr4PKOkzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SjbMysQOb_jst6AWcPQhtY62XY3FJGmL_p_hkGJKtq6TozYIunvvjP0iC7v0JGvELF--sBvXWXaNnQZkLDH_D0S8YY9TgcLBcTCHCYwHRRnEcZKVLte6luSFTlHTZ62URI92oIwadX4qBJF5zJQQho9S-js3cMsqKgTKYdPBXN8ikdSr-HHgpvioJofedNSEC-zvEPnFBmsrWvHIgxt_Qj3t8wILo7qGiDZEmepgHTseUzf4HJQ6PXZW-gCdBqAdYtm8gJbOpoE2MLHKYUcAf4u0PpOnpRwoItKyKXj4SFKrGZdWEX5W4hzOzsfZAQl3i_EZieqUiSkznIfV9R3XwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eFjU5QRzkfYmZFrqioyzatjeePhbiQIBWKk7TYqh1DqrvnAVIslizDj64gFW0GxlkkWwObWEwDYha8drBMpbu7emEisXi-BeTDhOQAMhgZn57lGt7W0jGYdevfQhnNsJq4pBPwbjyiX7BGzK5F5epi4QWrR-7PpJm8s_iSBU3ceicmYVhfjNMk4Avd4gnkCyT3F9XIbsN0_p_1yh9n65BKxtK-UsDbGXdYJ7Cfgz1sAx-CaxzKOtKaB5Y--vC-n0AE11lsf4OSyUbxyK3DCyYa0dxCU6Dn5SoFJ-ekQ1y3yK2lL0YMcofxER7mUJjSFqTc3fZqskHy_P3S6MkdckzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بعد میگن چرا کامنت‌ها رو جواب نمیدی
چون 90 درصدشون جواب توی ویدئو هست، اما ویدئو رو کامل ندیدن
✉️
مثلا اینا کامنت‌های ویدئو BPB هست</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/MatinSenPaii/3897" target="_blank">📅 12:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3894">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UMsmRVo9U2uig79VCx-ZqiCGpd74t66YKP--BII4UmmnTLPNkkbbHM8imsFVQAhzQqgjBhT2hKcZ0f9fbQ9Jp3BlBKC4z_tKu2nyM7_SEGj72o_OgM9J9cY3WoWKJMhW53hvL2NKtby8qouC_D8crV1YfOVJNW4cwUMjk4fiZZnuwwddWnXIZSr5i-1bZXfGLtT0xk7J_K0yX9eOyz7IvlMhZlHoXhBx-RF2VHnNxHI43KRypvU7ez9xE4f08cAPncyz3z6i4qne9lgWgfyH4s4d_wGPO9FOtdYAwPKkr1HnZ0uvnwXEp9ai0YUrOjCjhEfwyJMfuFhIbYW_QRTGeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k1bq4p3chR3SsShh5GZxTEedgVQg-rnzK_3MU4fBmBbHYcdvCQ8GOFZUfcz-BQyUGiYXn0m1lsYnsskc9_LNWFujkEmr8rcXRL4TeaFyhfZD3ojl_14Q2aHEQgWu05c3e5oVoQS5UIEIiOCUXlAGibCguMy0n63hZEqxDGc_jO4AgWlIxBZEeLMEguXOXcW_9Xa5iwoywgtkhHxNJvE5k9V3JMcQ32BMLEj-dZxPJ8M2BqI5i_OuNFvoDiNcnvlY6khrXBhZJEGPfll7uXukaioZm8Ax-g91AsHk5Hv_Zqtu1xXKsigcQrko2DNv4O-caWeNuZLPWWpbkW0MdJdN_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mtNvbqpZh6cq1B2gNe3GgFZ18XeFo-4PCRI9tQhjFAYQm_10yIF6krTwmp4aVQPCgVoi533qaMIrNNrMR12pYpcbzxSjmbBNlfIzvV1xFRTzNIsw2ooSWr6vpJjUlIoRliRQu1a3rlbJa_nCpvqV6r2i7gqaqBKbNVcS6qdhyKCyjGsohW0DxakyzYCRcUHH9cDKEqDbQvNYjLeJsxv408h9txruVAa_PCEQXEeqjYNSzYBNsGNbcaWVYgcD8FXaljuQUzZUD49FgsRTxVkHk_yL8qZfnJmEtrVvfJzGTLJNAIIm8IGCw0oB3W44kx0iYz-GUBsRkcSQKppSysWlVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا با WhiteDNS BPB هر کاربر اندروید می‌تواند تنها با گوشی خودش، پنل اختصاصی خود را راه‌اندازی و استفاده کند.</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/3894" target="_blank">📅 11:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3893">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">از دو روز پیش، دیدم که سرعت آپلود کانفیگ‌های مستقیم پشت کلودفلر روی یه سری اپراتورا توی منطقه‌ی ما به شدت افت کرده.
و بعد که چک کردم، متوجه شدم سرعت آپلود خود اینترنت خام کمه و زیر 1 مگابیت، و مشکل از کانفیگا هم نیست.
پیر شدیم برای یه اینترنت خوب</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/MatinSenPaii/3893" target="_blank">📅 09:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3892">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">شمع iced blueberry
🫐</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/3892" target="_blank">📅 16:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3891">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoVfxTP_0u0IgMb4krAw8k12jJ5qAloGM52jUyOS03PQiu-Eo-Ocvw6_eUEfZ2nC31S7Vw2-UC4VKHWLSgJWdi6dr-O8-f1EZGPh1y1XpztPBoeccLrzssGCBqStBlaP2w6PzAIpJQX4V5hhXAR_bijpW1t6feo3t_xyfNX14JNpL4KbR48PbRBgiMlLKlOwuYv0nDfVf675gYbejVgtIjDN7RFLAXALm-MJxViRmOHVhjIF6CJceGvIQCeYNM3DEHvQdGQdHx1dzgGshRR6Jba85SCuvcflUHEiMBIvpEsazQuBTewaqXojmKBRZFMsQsuDvebHdOHfi9ejTzw3EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
جدا از همه چی رفقا این ابزار رو خودم قبلا ساختم این ابزار چیه؟
این ابزار کارش اینه که شما لینک ساب بدید کانفیگ میده با فرمت های مختلف و همچنین این که کانفیگ بدید بهتون ساب میده یه سری آپدیت ها براش میدم تا بتونید مستقیم تو اپلیکیشن ها استفاده کنید ولی فعلا داشته باشید و ازش استفاده کنید.
لینک ابزار:
✅
https://xsparvin.github.io/Abzar/
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/3891" target="_blank">📅 13:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3890">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lmwEpw2nc_24Z-Ol6SSCVeSQ2vU2VD3mD23NZMXAFBz0w1YSwFx72idSTtUquToUyaQeVME4StRno15hlkTBccxO_7jVKgP6bNGHgAmmGgmBBlw01EeTyIzPJ1a6XEYIY6wSMlA2Qmc5OVzN3WSPfXCq6Jct7LTLMJwMYFQhCCJtmQls3CjYnLRmSl6RY1L8BOv_shkk7vZZMVjL0qiOXp5_k_7dzgGJUDON4-_mRWkTPky8GYHf0EJxp2lrjCaP4q1r5kYz0-FyUBMEF9HBQ1ZajXmtqsVdy_mjjGFDV62zu3x-DAin-JD6AoNAlRNmYkE1itoX-xFpyJrRWb2Otg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اول که ممنون از لطفتون و بازخورداتون، دوم اینکه اسکنر حجم زیادی میخوره حواستون به این نکته باشه
🧐</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/3890" target="_blank">📅 10:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3888">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aK_tslTGzvsIfCBiUDEaXHRFcdKDqqBOXR1a6w6aibV-BEnMf23kpWbeEYbiOre90hdfk7Kc2p3iUw-rJehefELHbYZvxhvG6sUC6xn5bE3pHwmjav9x5FngOhrBEgS6Mr50oYZDVVI27FpEOHnPcbTKCn33vLgG0e99M3cOwPT5wI1EOjo18Sf_J0ewF1gSvAMwlUv7cxo13ZdXVAdRW-dACy1QRKTnQfAv0Uss-2sHGU7bq5trDcNYCIFvH8b3YS8x5Q75r71mCzQrnVWXyJrW64PGrSjVpNIAl1nwqOgMUu3iRrKYh5Lv6shDSIXjDnbrfmQm2_Hq2Qqj7KGLYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UVl8z6pfTRQll-9EkKLM8waTYR-WIu1yBEKmWqjTNvXod7HnPXev16WhXdnChfOKmuJcDNEJbCcT09ZRuJ3SesSwDcCakjz220i5a9x2gE060BqHxfe_MK6JitYEMgcPAXDhyHDuR1nWK_o_0sQ_hvQHTGXhBCu8H6edc_uk4574uCS7zrRPuNBMv58E9amgsUKfn1pDMhSPsWkuhPzmDK6QbiWBLy1EwpPFa14T62oHD0Qx8R4sCDZUwMZaxpS81YkvXMiAE7VPnDgaA3ytmLQsxXLmNxSRdAzPiicLFzs7aIeFLOenbsUDMmZkcix7LQDyFnx_Dx7jVJe5RknzhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور: @nahanproxyipbot</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/3888" target="_blank">📅 10:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3887">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T9hIOPNu2ZkTdCNFoL8XV0vs1XPLLipLzPG4tbsY_hukokBOWM9-HsFaI5b3Ey-DNZ7dSuF3B7eBlgSNYcWpYSGRSg_ULQrwRUVq2Dftbjj_t06Zwf1SAfSNuvneVW6lJVO9LfMj3DeOkcAiWsJeye3a6Lw7jF6O-u9QiE4aAPsbBavO8SLnPie8OhmRwA6QzNgPm7JGscr6tj1GrYIiBh60xB8cZiaxU-BWcAmhwFP_eTeZUhoYeCsA7uqB0wKmwdcG9lSZL5k4RpPCTeaeBHk3JlletKRMaztdHD6XiJ4EooSZvL4zR9PSe4LHhJCoIs28Vs-mbvFcVolJmqNYPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از این ربات یـ‌بـ‌خـ استفاده کنید برای ست کردن پروکسی ip بر اساس کشور:
@nahanproxyipbot</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/3887" target="_blank">📅 10:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3886">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خب قیمت دلار اومده 165
انگار جدی جدی توافق(که نه، تفاهم) شده</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/3886" target="_blank">📅 09:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3885">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bJ6PgmVYpPb5-VcWjFy-8zex1EOHP4dRjXp_du72KDsXLGh_P1tprHSbyvB_ouF6_yOGvCVq2hh3RteGuj_lvsiSJUg8uvQuXaMx0dolvb7_Tlce_I45LCG1qFGr0481mnQE5U3Fk-XivxoyDgEYg1iS4nWyuQIj_dTRZSoHpavuaES5HR6OXX4teyUYRY9i08LQUk6zWlUE5XhUYn14SmONNKTC7KBcgPSErKzuTZ3bwuWTrxXiOxRqD1BgsjX8mwaasT9VwUMJa2QeICu8DAdmGMuKKVtBJl0VBPih6oIQ4MAYKe4xVN7JvtQDk3MfF_niZ9MIfN6ke8SM9nKPGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/MatinSenPaii/3885" target="_blank">📅 08:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3884">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/MatinSenPaii/3884" target="_blank">📅 21:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3883">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رفقا من تبلیغ VPN و سرور مجازی و... انجام نمی‌دم. همونطور که توی دوران قطعی و از ابتدای فعالیتم این کار رو نکردم. هرچقدر هم رقم رو بالا ببرید فایده نداره. ممنون میشم واسه‌ی این پیام ندید
🙏</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/MatinSenPaii/3883" target="_blank">📅 19:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3882">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qvFYocVicmIrMxhCj96SIt_5lhK_dTAyjPk59N_hqy6uSNO1e1I1_RlmbEmezmCguD2yYnK7MqSxhBBrD-ZcDEkc_PM-jsgbACMEMkwyK4SW1-XSwgTJ0mBC7IT-MDi6fJPsnilI-UyV-8cgX-Sii42lmvr0cbfeXihJW7ZeD331H0RZDyrvpjnRxvmDIX7tVzBPpHZHI5W_pTJGUNE6rNdORbueeg4tsWU0WoV8ueo056uQuW86fIHql6T1QGcceL98JtPyeoRqhopJT2OB-nYAN8RaFWWs0g5gP_g9LIfY-bqITGq5OLRNYf25px_32wqh4i0yeAWkYvrpiykZjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو برای اسکنر یا هر پروژه‌ی دیگه‌ای می‌گیرید، ترموکس رو از گیتهاب نصب کنید؛ درست میشه
https://github.com/termux/termux-app/releases</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/MatinSenPaii/3882" target="_blank">📅 18:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3881">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g7ijPw32vyEXKme19zTyKad3dmPwrzSUf8qYOMouTs-cV_L8jPDy5pkCiDQi8ya1SCcHANPi2skaof-gkmdCW9tokYBW8VC2jjK0QACThT75SktlV6g21JczAco4XprilI57zL1awKbSq8cvicVuIdq6AxcwijIoLZcKFWYCzUvfx2JHXiAwn-BLt37y9zd1MX3axeo_k49r2OTfk9ekJftHGDZdEyYwkiy1ecdDHRFfBNM-VL32z86-l1RSzDuFGNqOzIlXsJWtSriwHrvOT278LwDqAWTIFJGS_Qcidw2m9InodL12aVdZ2MA3JC7dcw83dYEhKfBlrbB413BVkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الان خودم با سرعت عالی وصلم روی ایرانسل. ۲۰ ثانیه طول کشید حدودا، منتها ممکنه تا چند دقیقه طول بکشه. ولی وقتی وصل بشه دیگه کانکت می‌مونه و قطعی نداره</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/MatinSenPaii/3881" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3876">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/3876" target="_blank">📅 15:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3875">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iPK2oeCpe8akwcsbLadIOE2LINxAo90o48GmJFfva8KKqgfH_FVvoVpHVgB0L0cfhwNonfoXQEu5et3Xn8tBzN01Daeqb7iEUMZBLcJL5RFi61BEH-zHGZN8L7GZfA7FMoXJsnaj62jBPecIQDv0kFaXRMRKu8TJyD0L9D44jP4QGNrjMzxabmFI3HJaUvS7jCAGEHEeVroJVcbEulDhsuJPBY31HUThgaYuqL3jlFdCJrOCI_1Ps2AfCcFrIATXx7XtWJDxurxV9F11Z4rL8ehF4BGckwapbySJqIUgaLVDi9GTRjqeSOoeSQnMD1J2YarQq6UzS6K6dlcfCa3ibA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکرشو نمی‌کردم یه روزی قالب وردپرس رو هم بگن بیاید اقساطی بخرید</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/MatinSenPaii/3875" target="_blank">📅 13:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3874">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خب دوستان به نظر من اشتباه کردم و فونت وزیر متن هستش. مسئله اینجا بود که از من پرسید، گفتش چه ترکیبی بزنم؟ چندتا داشت، یکیش فونت مربع+یکان‌بخ بود. منم زدم همین و بعد دیدم اصلا پولیه. اما الان انگار وزیر متن انتخاب کرده
نکته اینجاست که چرا اصلا فونت‌های پولی و غیررایگان باید بهشون اشاره کنه یا دروغ بگه
🤔</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/MatinSenPaii/3874" target="_blank">📅 12:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3872">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bsK3xxAJRKjBNfM1P6-isa4ZlbbkjQc0BtMPuTWtk93qfs9vhgy9TkvNDDnSvYm3wF0wNKfb-juEb3hiKZcXmO0DBwxisQMqwEl3OJUX-KFBijfa4dvEc0QlT6Qgs6-CZOpwIU0d5q-7_Yn42zc8_l5G1vfaljTR4hyoEVPYw-VsW2sMBUHdwlZNIMTy7k7Se8mgIqOus-GuTMYFnruFvKbT-2x9PGgNQ5tuTMz59LLhavngdog05xFeovXDvd_kWVxjUJdaNIKTJNYFSsb-FVM5AX2Sj84rU5Dp-inJyCZlPGIIVaOyvZBeeMU6IEMpTpMEBzBYLo6kTmZMRsSZpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aHfx2_FuTDe3JoIhDwiOrZuk08EScIP6wbb-tnE9oxgRMWYDhzFuEqC4W-4AQZRwUxuxjumTnyq0RLReuRVFsmhjkzlUd5Tj-xfnahl97iPlTZGtYnKh-oxAip_gjUDY2DSUFuknTA33fGi42dkKjg9HvNkqYSI9n9MVZqiNPVgKqE3wlnCG9ld8jBZ-hd7owdLhMJFweHmHqf5mK6ygnZ59pSI8aXkYB0BMGDpaYg-1ZHZFh2gSxdGexZ7-T1xY1T3y1wfyX2DIbX4RvJyEt7TItZ4NM7uGcEAIccSRqt-KluNvcRuJUMJ7D4g0KCTKQxUNfUhH6lDMcNKB7HVUsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکر کنم کپی‌رایت برای کلاد شوخی‌ای بیش نیست. اون از قابلیت اکستنشنش که کل UI و المنت‌های صفحه وب رو درجا کپی میکرد، اینم از این</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/MatinSenPaii/3872" target="_blank">📅 11:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3871">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v0GUYoocfa1711shrBcD9SJUta7TAORs0_3zyRCJUNcUfSvTHoVFzHejqoTqYEz9Ckhb20hid4-_SykUxzoWjcxMYxqJvsEpiqJT-JAQ9C4UEUS5oYZ1_e9UQ9cb_a2DHLxDZQcTSyp0w2ndYUvWrOSVJqB_ONitJpbKyrty1-W8PQZ_mGPrPifMTSsQbvtfu8QlCEJCyor6-0NZumL8VFXR5D8EYAep6pyqs7BS4rJnA7zGEBUwHqM5DLCxLd27QauwNazV-WzrAW3Ka2jZPS6uG3NV0448ozUVvDcuEZDOcH2mbmY0mD6opQ8zxXQ3WcOa1KCz7-eyEdtXudCo5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/3871" target="_blank">📅 10:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3870">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">در این حد بگم که رفت فونت پولی ۵۹۹ هزار تومنی رو نمی‌دونم از کجا پیدا کرد و گذاشت توی پروژه
🤣
🤣
🤣
اصلا یه کار عجیبی کرد</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/3870" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3869">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/3869" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3868">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">من منتظرم که شرایطم استیبل بشه، حدودا ۶-۷ تا ایده‌ی خوب یادداشت کردم هم راجب AI و برنامه‌نویسی هم واسه اینترنت آزاد که واستون ویدئوش رو بسازم</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/MatinSenPaii/3868" target="_blank">📅 10:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3867">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏
بدافزارهایی که با ترساندن هوش مصنوعی پنهان می‌مانند!
تصور کنید یک سارق بعد از دزدی، یادداشتی آنقدر وحشتناک جلوی در خانه بگذارد که مامور پلیس بعد از خواندنش، با خود بگوید «بیخیال…» و اصلاً بازرسی را ادامه ندهد! پژوهشگران متوجه شده‌اند در موج تازه‌ای از حملات نرم‌افزاری، هکرها از ترفندی مشابه برای فریب دادن هوش مصنوعی استفاده می‌کنند؛ آن‌ها بدافزارهایی می‌سازند که بخشی از متن‌شان طوری نوشته شده که هوش مصنوعی از بررسی هرچه بیشتر صرف نظر می‌کند!
ابزارهای هوش مصنوعی کنونی، ترمزهایی از پیش تعریف‌شده دارند. برای مثال اگر از آن‌ها راجع به نحوه‌ی ساخت «بدافزار»، «تسلیحات شیمیایی» یا «تسلیحات اتمی» سوال کنید، فوراً ترمزشان کشیده می‌شود و از پاسخ دادن طفره می‌روند. حالا هکرها متوجه شده‌اند که با افزودن این نوع از متون ممنوعه به بدافزارها یا نرم‌افزارهای معتبری که آلوده شده‌اند، می‌توان فرایند بررسی امنیتی کدها از سوی هوش مصنوعی را هم مختل کرد.
به زبان ساده، مهاجم سعی دارد کاری کند که ابزار امنیتی وقتی به بدافزار می‌رسد، به‌جای بررسی دقیق کدها با خود بگوید: «من اصلاً اجازه ندارم این را تحلیل کنم» و از آن رد شود.
﻿
این نوع حمله نشانه‌ای است از ورود به مرحله تازه‌ای در امنیت سایبری؛ مهاجمان دیگر فقط انسان‌ها را فریب نمی‌دهند، بلکه رفتار هوش مصنوعی هم هدف قرار می‌گیرد و ترفندها در گذر زمان فقط پیچیده‌تر و خلاقانه‌تر خواهند شد.
✍️
NooshDaroo</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/MatinSenPaii/3867" target="_blank">📅 08:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3866">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jl1LJea7jf_OCEO7p5lFdj88jiGcywugcxrgSYAjXVnqIEVC3c97XrCCCo8zItYRoLyC8KTO8yIp9lCfawmMbIVV5D-jaDGAZEpp_oSWRfFnHlbSpNVnDfUGKzKJgQ-gtGJ3-n-Q2Cdy_A7biAsXnaJevd3I203qEMGoD5hK8CjHV2h9TXkzgCdVy1COc-dMhTnetEAxdKj27_TtAuoWMPhyziu5ccrsfzFfeOarlbc-y50XqhhsoHWBiDVFKkqhTUKKIqTTJOCkkaKntmlP8VIgFwPrtGhYqgZHyWU8RdODr7YsNesxmvPSLj4OcYszGvD9TjT6eLbRh4WVTAMZ2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/3866" target="_blank">📅 01:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3865">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ub4cYYHWWtE85JW7W0S5_duBleG-q1kSRKhXWZdW0ejHVLuUlpx89aln4HISqTmKKRqNSY2Sgt7osfoLKMVmRmaIuFat_Qtqtu25vXEw5donKtaORs8WNTktrm4qFNzyCmHtY_ux2DPIAMRsuDlnGAEqWPZxbLBAfZvitIoDTT9Kex3HfM5US447E_EoseSlhzYOM8HJ1UDjbtxcFX6BS8YuvWKxpCE334Z5OCIAtN_HrVsZ3UDNFUfNcQqdWbYRRUbvXwZQJe8WsxHn9a4LsNnSIH2KMoHqtDt8-uKgSas4Uff4Shrko3k0_11ps9CkO_kQ4AWGUtD9H7oPIhmf-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا به هیچ وجه روی کانفیگ Websocket معمولی سرور شخصیتون نباید اسکنر ران کنید. فقط روی Workerهاتون انجام بدید که ارزشی ندارن و ابیوز هم نمی‌خورن</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/MatinSenPaii/3865" target="_blank">📅 19:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3864">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">برای اندروید و ترموکس، کسایی که مشکل دارن طبق این آموزش دوستمون برن</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/MatinSenPaii/3864" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3863">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">برقا باز شروع کردن به رفتن؟ خیلی دیدم امروز توییتر وسط کد و گیم و ادیت و... برقشون رفته بود</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/3863" target="_blank">📅 17:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3862">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مرحله اول  همه بخش مرحله یک  رو کپی و توی ترموکس بذار
pkg update && pkg upgrade -y
pkg install golang git -y</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/MatinSenPaii/3862" target="_blank">📅 15:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3861">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/MatinSenPaii/3861" target="_blank">📅 14:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3860">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نمیدونم این کانالای تلگرامی چه گیری روی ری‌اکشن دارن
میگن ری‌اکشن بزنین انرژی بگیریم. انگار از ری‌اکشن برق تولید می‌کنن
عقل ندارن راحتن به خدا</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3860" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3859">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم
پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/MatinSenPaii/3859" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3856">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/m7euJNtWSIWCsQ0HhCZ2lmzHLT9J_YE6z5NccVOiUM3wnUis06Co_RqE9Pr5bhyM6tevKAKteuxyPndVai1g0ZXrzRwA0d9wQA46kr05-5o2129YJ62PDTU5SwpAtSsic3fTzUx-38S9ygefxniFQKXYda0ULq1tiX2zwZWeGcICfTvoWed9l6ky6JBJyfxdhFvH-xQImefUwgSiBxE2AAkrJDMkK-fKSYnGjoPaMsRgalsPwEkAeOd7mCCWW61YxLdFdsRx0o6PdlhqPixScdgomLcACva9slsHLhP3xyXUwuSKCUSixiOXOz8OO5TwAjtbwZDfoe0dMjtPRV0PtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HLmB4ryPCfNATiSW4oBY5Xy_vWl60hu4yfopA0eMUZds-45ukShxxZQE4oilp6paiyIUnxcb63sAsJ33BKt-VDd4RnbP9sqJqbRfbV2hbEyHmXoRpg4E0M7zyCWByjUKwmy0DIpfnTNG6R-V8oO-Dz1ZtvYEW46cuXOqQBjz20RMUbN_xTbsCC56YKYc8jPaGaHcl3rdhGDjSFcl90aG3dn982NiUt4v00zz3s0GkJtMKrthddokMX4IfChxe3hHiElGiNgzUvexKbHMthP_EJ7YrXI6D1LBJHYz_fss7r1NxKnoReH_WVoxV1JZrS5UmNNPfsIy4hiYFXtbzC4_7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AM83-eb3qOj3ruVSPjX3s4Iaz8W8s7BBKjNhuE-reuPvGAXm6BQqy8-5YpsRW_LmtWQzSoqK2kDaYHufYvaiDQohS3jUVnZMW7JyFdyfvrKSacmgDTtU2NLr7xhxfWWIG7UGP3Rj19x3xLY5bHHVMnDsQMHVyNgxR0wPqaCGXaTY0YtgjJsbZaVpwNuggz_aj1SQndPVvTDh48YRnMEqCXUh8VHYKIHglO4FrTFUtSlAPnfWoXSHsTjm2GKTCwRMmQosn0T1m-kPLX_PLFJTz5XCpaLX3ZLjMPRuN8oZcz4g4PbZQ_lobrYCl7eAw-HQwKzKUJjffa0rBTIi1l7Ofg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/MatinSenPaii/3856" target="_blank">📅 13:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3855">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دوستان، این شکلی میتونید به من پیام بدید:
https://t.me/MatinSenPaii?direct
اما از اونجایی که دایرکت به شدت شلوغه، و من پیامها رو اسکرول می‌کنم پایین، ممکنه گاهی اوقات زده باشه سین شده، اما من نخوندم در واقع</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/MatinSenPaii/3855" target="_blank">📅 12:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3854">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حقیقتا MiMo اگر پلن پولی بده، خودم اولین مشتریش هستم. توی تسک‌های متوسط Backend شاهکار کرد امروز
هم توی سرعت
هم توی دقت</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/MatinSenPaii/3854" target="_blank">📅 12:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3853">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هم پشتیبانی از Trojan و Vmess و Shadowsocks اضافه شده
هم تشخیص ISP
هم تست آپلود و شخصی‌سازی تست دانلود
هم WebSocket(که بهتره On بذارید)
هم هسته رو به کلی بازنویسی کردم
و این به کوشش دوستان عزیز برنامه‌نویس دیگه هم بودش که اسمشون توی Release note میاد و contributer پروژه هستن. من شاید 20 درصد از این 10 هزار خط کد که اضافه شد توی این ورژن رو نوشته بودم</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/MatinSenPaii/3853" target="_blank">📅 12:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3851">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vH0pluT-WLUdboYdLm7XGtrEfXIxw0ABgLslW5CHtrgbw9P4XoVMkRVg3jirY-EvlJ2tl7Sbx7UZg9Qtgc3fDWGaSK0r4Qh-901G7gEeXS9mT8wbSnH4hpch40OxdpUOXoXEeXIov0PUEe_YnAEhYQdgp1H-hEtOm2YrO0-6X0UrekyxUj-2S-kLls3wony6oxcrQiyn8D-H2NFZra_G0SacJa1PtRWM2f6pDhlSaL3BN7tQErFB2PwJNYuA5JclBlXNmulhtTDNXwOfOj18hG6cH4ZuVcySi_PmL4Qcy37QUyFeCpV0stbHL5Elbi9cQEGR3LYG7Nw3JvXIRQm10Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GlFwRN_G_JLsh4D-Nt1Vd65to3KwHleOnR-EBTuxF_kQCNsIWWfU-PPWXE3Thd9LgBHnkgRShqP5NL8F1A9LBIFdrj246Sz3RhsdrgJHRnhEXqlGvcy4Okq2119EGZ1irr2bNIzEbh0k68UaQFT3Rj-F7g_k7_woxTbWTgKR_8aH4Kny8F-P8j-r18OuD7D4orTq-v6GNddaqJ2yU1cGtsNyQLedOsFTiZZd8M9IYcozQjBYk3BlhsRbeQitj3vggTb59EB9THzdMvCuF2YDBkbwYytJhvHT5gADNc176wbxjjSMgDm7uOoBSkMTZUQUEUNlCIx1j0JPpDbWCeBjfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/3851" target="_blank">📅 11:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3850">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b7aLJErIq20k9106VuhHY8GLapw-FNVo85KSwqQ8BPxEUIg1K4X9LUWTEk-X94dWZmFwo-sE5w6HMiX3VeuKhy3b8G_49ngd35OFohZ3DDFsTveEwPcMFFJHr1slIB5s-y6y5hb7Ahw3Ry7xzdz2HMdnxBcEhnYoCbDXJ8PzEvuv9r4LnLSU7OVVAgei6Wf74ezJ7k5fsMZkhnPeREyGa8b4Vb4XwO5w2qa-Mx-Zfq32OWwxpBUBFQfpW3sOffrSGHNjd0er934Ax-Tm_rg90MhmewD0vHQYC91-c7_6jKWoWVl77IBWiCtsDIonpcwGJlwofLDOFRkn3JdKxIExEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/3850" target="_blank">📅 11:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3849">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/3849" target="_blank">📅 11:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3848">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v3kY6w7LMeqp-SF9-s1ScLRB2W-MgtmS0SYNwKaseJgQIyrLHEEo74LsAr9saNGU0TqEwpgLiFcTdUYD3hfpExisA3A5p82PXHMguv2NLRnmuznqyH2qpGP1KV5dWbDU3mpkFn324kU4wxM8kHGFijanDI_h-MFs7tLUC_axc9cIZTEFHxjZEYliVna2MLzkLtk7oBs_VURe7Yu6Z-5m0pRDycOQ5ty0zHTFsg5ZYsvVJ99dAENDFkUQwdTEx2WMOW3yltFsJhndzahAdieiq_vEerCBCox1I-KSIEmypTrsrso1rngNvylzyOybEHfcDlqTLpcvv2TvU5_55dbK8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان خوب، لطف کرد و هسته‌ی اندروید و تمام چیزی که برای ورژن اندروید نیاز داریم اد کرده، صرفا منتظرم که خود اسکنر عملکردش به بهترین سطح برسه، اون موقع نسخه‌ی اندروید هم بیلد میگیرم</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/3848" target="_blank">📅 11:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3847">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نکته‌ی خنده‌دار اینجاست که دولت آمریکا دستور داده دسترسی به این مدل‌ها برای هر فرد غیرآمریکایی (foreign national) — حتی داخل آمریکا و حتی کارکنان غیرآمریکایی آنتروپیک — مسدود بشه!!  آنتروپیک اعلام کرده که چک کردن ملیت کاربران به صورت عملی ممکن نیست، بنابراین…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/3847" target="_blank">📅 11:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3846">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/3846" target="_blank">📅 11:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3845">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/3845" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3838">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">32 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3838" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خب، دوستای من هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3838" target="_blank">📅 11:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3837">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خب، دوستای من
هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/3837" target="_blank">📅 10:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3836">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Enyhm9n_mVDSYOeJjFPj4zN-Hsr7KP_8sldOo3dwcm_TB2jlRrcW2m6MFkGTO7noUeWeWPboELdLIApDVvfAI49j4B9x7IxuuY7d8_exLGOb4NQLdJ0J7OPLKhpgWLEF7epoTebES9sxYco9lmWCx08iYBnqycuqyjWYMMxFGT5b55tSMIMLT5cVNy0of9qXrVK8z6zkbBRuEEmHyvcdU0zNJyAKaZ2nImLSkmFo5NbpwTYoRSxr_DFLk9eltnqafZOp8IAXQTo2T_YnW9txX3leiP5aCnbIrlbfH9ZJil1SJgudPfMd84EG9-pkJjJjxy_IAV6a9ZjlE3ixUkuGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لپ تاپ اوکی شده الان اومدم تست کردم MiMo رو و خوشگله یه تست پرفورمنسی بریم باهاش روی SenPaiScanner</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/3836" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3835">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VlMFVxLCwFqqYf_Y__3mHz32j3x9jmJpSdoROdWgo9CP11Zn6nsfLXlqUxBtxJSYJmtwpeEknx7NhK8BM6I1RDlQ3WvwbYVeY5-Lv2OT1TtE_W1x3qP1xyzBJPBtpTxqckEOYjx6TWMoikThgwlGYUIQuekWMq-64iRC84VXeiSyol85wPykOPopF6E6qOgaRznhIRwUyPoIFATWnMqfw0Pt260rOep4Xi3t68WTJhfN7WFAdBjJfUsdvgW5iVskpuZwWDGErjZQW_7uGReC6HFDnuBImnvW_XNkov56C-vi1i6G_oPDG27_qxDcriV_2oXdE685gXPjSyJiVB4hLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد  توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش فورک OpenCode هست!).  خلاصه‌ی ماجرا: تیم…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/3835" target="_blank">📅 10:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3834">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/MatinSenPaii/3834" target="_blank">📅 09:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3833">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mi8RtFnKa5tmt_KOFJpqcK0y56gRAgaWhIqkfyoOKYg35PHYPx9y2KBYYMtQo2B3839cfoaD2WtUp_mWRQRcdpYzKLvRlTK1dJ3XqeKfnr35M6ybk3Qj37Ve9DtvkghBOCLow_bAOkxVP5iEHy7xoOGTZZlEj-340NfWr5bbZnoujc9UtIjik7213xsv7gd-fRBe_b2a7zV9stR4buqGiw-kPkgcrRK-bpP3lrPD-YbF_ltOjfdlFPFFbudFxPH2Mn7HMXmPwAHJQhmjC_CEfpUDUUjWDrNJvLDTa1RmQN02m-8dtn1fscTbp4KaValdUGGBJml5IRbJ50NO-FOiPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/3833" target="_blank">📅 09:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3832">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید http://l53.net/</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/MatinSenPaii/3832" target="_blank">📅 02:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3831">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/goG1rwoy99H9Bm2Z3vYDEWDyomZ3OLXbuaD_92WMM4M1Vhy06iAhSo3KG0Ih2s97uVZuLeix3kmz9y4Zh2EdI8XMrhdTTiRbuGAX0KbwvVZvPhSrvoETdiPMIDIfl0ecREGU_7_tPdc8TT8JitRZ20jE7ls2AVZCg_IBWiMuRCmdQHb_491rJ38iRDk_uUB1ClkE7t-b__MKmMp3Igy-i12gRmaPufb1PuBSNnRrnT2IQ6ExJQZraNYsSgRHRzjJypaRI4rEAYFtb4wQAMoGRs3CnIAbRVW2k0hQxp0ekqsymfEpLUvdl0fWtLNc51uRerNRuyaCL-s2BE38Xcmcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید
http://l53.net/</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/MatinSenPaii/3831" target="_blank">📅 01:55 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
