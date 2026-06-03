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
<img src="https://cdn4.telesco.pe/file/nnpY7BRf3Hm9cUfePARWX6ONWmJPvpepNk0bdhYhBgks2c-CHxns406aZ08A69SogirUKB4MeSNY9ohhSEIsUMKMrTp1AQnkUPmqSNQuY5GtOeT46i9Y82uupOtKh-HxNc_4UERWRgmqrxXmXVxPB2YeMux8gJnkpz9RYg6hWkxevnBO74WnvqVUS35YDPlLQQZK7y5rCKOpgfXLXW9c32Gw53Aw90emH0znoPor3iIfij0ERDHuM-K0GX7ucmVTJN4dpWRbMxv-oczQypeMhtzyKigwChlr5qx1gSpnISyz752JdW4QLPWIqc8WAHKWDCmF8ju55P4GGyKm2Nzpiw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.91K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 15:47:09</div>
<hr>

<div class="tg-post" id="msg-16909">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKF2jqFZ6y4dP9s9FVqCup1LydbJPuECQ42l7DFwxPaec6nsrrMshKcOhhKsEahROoa2dpO_FDG1Swmm-luCm6nnv1Bu01HG79NDcx_FTPFC7PLhUWbxXKsb9WKmmli0wfd9eyvesTTsBmr1Qvydcv8Fv0ULxG_Tan2sioi-hGtnxcXBCpV7-_4F7fBczmrQnrJ_ER0xF1-dInv_VU_yrKgb4njUdVKP7vCbQKb2frsi3EAj_Wz1G6-IrBuh6ZaZZ1XVMx7JD5OfHjFRYrCVzgXzcSg22Lm1QdEpFPMLtArkUgGpTMejmH4fdwKKoFNvGruxBil5Yei-a4uNZ5v1zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروه «مختار-007» ولی گفت که به شرط آتش بس در لبنان حاضر است سلاح های خود را تحویل دهد.</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SBoxxx/16909" target="_blank">📅 15:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16908">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شما ببینید وضعیت این منطقه گه گرفته چطوری است که پاکستانی که خودش در‌ همین مدت در غرب (بلوچستان)، شمال (وزیرستان) و شرق (هند) غرق در تنش و نکبت بوده حالا دارد برای ما میانجیگری می‌کند!  سبحان الله!</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/SBoxxx/16908" target="_blank">📅 14:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16907">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ایران ۶ موشک بالستیک به پایگاه آمریکایی در کویت شلیک کرد  سپاه پاسداران انقلاب اسلامی حداقل ۶ موشک به پایگاه هوایی علی السالم، محل استقرار نیروهای آمریکایی، شلیک کرد. تصاویر، صداهای انفجار و تلاش‌های رهگیری بر فراز کویت را نشان می‌دهد.  رسانه‌های ایرانی می‌گویند…</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/SBoxxx/16907" target="_blank">📅 14:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16906">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">در این پست و پستهای ریپلای شده اش گفته شد که هدف اصلی ترامپ «تحقیر» شدید جمهوری اسلامی است و این مسخره بازی امروزش هم که میخواهم رهبر ایران را ببینم و اینها هم در همان راستا است.  عجیب است که ولی عده ای مونگول کماکان تصور می‌کنند هدف ترامپ سرنگونی نیست و مثلا…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/SBoxxx/16906" target="_blank">📅 14:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16905">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OIwF6S4pTjA6HlpenJZy1HOHSxmpYAQ3iObUSkhibe50zrgDJZdvxpmjl3D9z1QkR-6gEuzTW7HhxMdpFAHVdaDsOcyEQHtbPUGUIvPrLpOadtbIaWeT-tknC84uSsEZtNjvr-kx4JbBNJ5VpVHoKCDtgyRT1dlS7aHI_tf0dxDnkE80MMRJGYaBALBSkFosRX3WmoHIeXGIAA5KILdotR_qR7RTyNTez69gZF_-YzRMt_eoMNd-E2KCahpGYUS8nxyKtecbK-DDMstoBGTfMFmJCYzJ1o95dJza_t7GNWq9ijs0gynqYxyPa6MaxEGa-ff7D5BjW0qfSauloFj_JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر کوتاه بود و دلخراش:
محمدرضا شهبازی
مورد تجاوز قرار گرفت
😄
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/SBoxxx/16905" target="_blank">📅 14:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16904">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینجا گفته بودم که هدف ترامپ تنها شکست ‌‌و تسلیم ایران نیست بلکه تحقیر جمهوری اسلامی نیز هست  به عنوان حکومتی که ۴۷ سال نمادهای قدرت و غرور آمریکایی را هدف قرار داده، جمهوری اسلامی از دید ترامپ بایستی پیش از شکست، شدیدا تحقیر بشود.  — تسخیر سفارت آمریکا و…</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/16904" target="_blank">📅 14:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16903">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ:
رهبر جمهوری اسلامی با مذاکرات موافقت کرده است.
اوضاع با ایران به سرعت در حال پیشرفت است و بسیار خوب خواهد شد.
ممکن است در مقطعی با او دیدار کنم.
ممکن است محاصره ایران تا روز کارگر برداشته شود</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/16903" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16902">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-VZSMKFWaVTfQ6N88lHnWJw54YnFKm0GD6Vw_ifM77xasuwp2nSFa-M6mwNCJHGpZDhNb2bqqOKVhCcFTrBOCsH9Buc6QpjZItz3-dIisIqOOEkN55Pk_Z-rWWmefvO0ujqzccKGOvGeiuwOvA2EygFhFZ4WswceuiY-SXoJBldeuq37rQGKtBj1XNyzRuwb6T0gznD7tAMd8ggd7AJW7sS9Eu22IRActcMgZ3kxdKb97HVOSpiS0rdTLNbUaazvjRm4rIMM5qeZ_Ib1MMEzlMFRSzEfGJk3yTCBoDCBa4S1BYZrXBlTjX3lW-m2yr5TQ24pa3f7SD1jPZQoidCWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تخریب ۱۱۰۰ مترمربع از آیینه کاری و گچ کاری کاخ گلستان در طی جنگ ۴۰ روزه</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SBoxxx/16902" target="_blank">📅 13:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16901">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اصحاب کهف با خلع سلاح گروه‌های مقاومت مخالفت کرد  گروه «اصحاب کهف» که از گروه‌های مقاومت عراقی وابسته به «مقاومت اسلامی» است، روز سه‌شنبه ۲ ژوئن با درخواست‌های سیاسی برای تحویل سلاح گروه‌های مسلح مخالفت کرد و تأکید نمود که استناد به حمایت مرجعیت از این روند،…</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/16901" target="_blank">📅 12:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16900">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇨🇳
پروژه نظارتی چین با هوش مصنوعی: شناسایی منتقدان دولت پیش از اقدام سیاسی
🔸
شرکت چینی Geedge Networks که در زمینه ساختن نرم‌افزارهای امنیتی فعالیت دارد، اکنون تمرکز خود را روی تحلیل رفتار شهروندان گذاشته است
🔺
طبق اسناد فاش‌شده‌، این شرکت درحال استفاده از مدل‌های هوش مصنوعی برای تحلیل داده‌های موقعیت مکانی، الگوهای استفاده از اینترنت، تماس‌های تلفنی و حتی تاریخچه تماشای فیلم و مطالعه کتاب شهروندان است
🔸
هدف نهایی این پردازش‌ها، ساخت پروفایل‌های رفتاری دقیق برای شناسایی «نیت» افراد است تا سیستم بتواند کسانی را که ممکن است در آینده به منتقدان دولت تبدیل شوند، شناسایی کند. براساس صورت‌جلسه یکی از نشست‌های این شرکت، تمرکز محققان روی «کشف اطلاعات مضر» است؛ حزب کمونیست چین معمولاً از این عبارت برای توصیف نارضایتی‌های سیاسی یا محتوای مخالف دولت استفاده می‌کند</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SBoxxx/16900" target="_blank">📅 12:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16899">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">قطعی برق خانه‌ها از اواخر حرداد شروع خواهد شد
آرش نجفی، رئیس کمیسیون انرژی اتاق بازرگانی، صنایع، معادن و کشاورزی ایران: پیش‌بینی می‌شود که این روند از اواخر خرداد یا اوایل تیرماه آغاز شود و مردم ایران احتمالاً به مدت سه ماه با این شرایط درگیر خواهند بود که در این مدت همراهی و همدلی همگانی ضروری است.</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SBoxxx/16899" target="_blank">📅 12:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16898">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آمریکا چهار صرافی ایرانی (نوبیتکس، بیت‌پین، رمزینکس و والکس) را تحریم کرد.
مراقب باشید که در این شرایط، ولت هایی هم که با این صرافی ها در تعامل بوده اند ممکن است بلاک شده و موجودی شان فریز بشود.
در این وضعیت، دپو کردن دلارها به صورت اسکناس و|یا در بروکرهای معتمد منطقی تر است. (یا خرید سکه|شمش و نگهداری اش به صورت فیزیکی)</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/16898" target="_blank">📅 11:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16897">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaGxteeRol5Hr1UlX-9cXnGv0U3lyt4xwybDSxucfVP4fmFf40Igjqxs7WbhjA9aLfv4CCpawv6eFi1FdlZiyMXZ4QXRT1wVlom_8cYe6TH7MBLKR8dZ86VlH-UryiWbsKMiRNfYa_WT8tszEQlrjvkQKc2z_IweVSVl--xeSmU-Kmo4AZJL82uNUY8g93zxpO64p2AMCyHWDBWnX5dNTQNrnzv49PKxkgCqIoZ-4cKEdX6DuCmFzCWKBBaCGm6kyNjuS3TB_vPdo0XYF59L6RXdqf9n6M4AojTK2JFX0vzwrCyAU4hukSLwZtk-g5yxda3wLPLCjXl_ZUqbqmcDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه به قول آقای رسایی، روبیکا حتی خودش اینستا هم داشت  (منظور مبارک امکان گذاشتن استوری بوده)</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/16897" target="_blank">📅 07:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16896">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESWLwdny9T7heu5jaL-uTK1zptn9supDjQ_LQwOkQYe8FkIk-DGn7H1TlOxZoINZKLoftxol8U6_pS2pxZxf1Mb-f4H2jwcpz7s5d0F7O08O3Xb7yX7BjsdGEwdWeqT1kVAx11GRv2a38I3ELvMBslZe0wLGcTWi3851aGg8R6tnIubtL_iayBekgmRvLLEGVwd_s8-2HCgeOuPDVwbRlD5NhVNFVqtVLaMeTdFtywjuwZeu7_L3FoIUgfquWjxuptF0pQXzQLTAY9aQmkNO7S97UlLX6zW495aFrpwOvdKsN4ScAGowGRr29-rOVxc0M_ZajVwtgPD3SjIrEL6wEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد ایرانی فاش کرده است که تهران فناوری پیشرفته چینی را برای قطع دائمی دسترسی به اینترنت جهانی وارد کرده است.
این افشاگری در بحبوحه خاموشی بی‌سابقه اینترنت در ایران صورت گرفت، جایی که مقامات پس از شروع جنگ با ایالات متحده و اسرائیل در ۲۸ فوریه، اینترنت را قطع کردند.
محمد سرافراز، عضو شورای عالی فضای مجازی ایران و رئیس سابق صدا و سیمای جمهوری اسلامی ایران، در ۲۳ مه به روزنامه آنلاین فراز گفت که سخت‌افزار چینی از قبل در کشور وجود دارد.
به گفته وی، هدف از این فناوری، زمینه‌سازی برای محدود کردن دائمی اینترنت در حالی است که فقط دسترسی تحت نظارت شدید برای کاربران منتخب در کشوری با حدود ۹۰ میلیون نفر جمعیت فراهم می‌شود.</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/16896" target="_blank">📅 07:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16895">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اطلاعیه سپاه درباره وقایع شب گذشته  و بامداد امروز   روابط عمومی سپاه پاسداران انقلاب اسلامی:  بسم الله القاصم الجبارین  فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ  در اواخر شب گذشته ارتش متجاوز آمریکا یک نفتکش ایرانی…</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SBoxxx/16895" target="_blank">📅 07:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16894">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اطلاعیه سپاه درباره وقایع شب گذشته  و بامداد امروز   روابط عمومی سپاه پاسداران انقلاب اسلامی:  بسم الله القاصم الجبارین  فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ  در اواخر شب گذشته ارتش متجاوز آمریکا یک نفتکش ایرانی…</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/16894" target="_blank">📅 06:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16893">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ایران ۶ موشک بالستیک به پایگاه آمریکایی در کویت شلیک کرد  سپاه پاسداران انقلاب اسلامی حداقل ۶ موشک به پایگاه هوایی علی السالم، محل استقرار نیروهای آمریکایی، شلیک کرد. تصاویر، صداهای انفجار و تلاش‌های رهگیری بر فراز کویت را نشان می‌دهد.  رسانه‌های ایرانی می‌گویند…</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SBoxxx/16893" target="_blank">📅 06:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16892">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حمله موشکی سپاه به کویت!</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/16892" target="_blank">📅 06:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16891">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رییس جدید موساد!  رومن گوفمن، سرلشکر متولد بلاروس و از نزدیک‌ترین چهره‌های مورد اعتماد بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از ۲ ژوئن ۲۰۲۶ ریاست موساد را بر عهده گرفته است.   گوفمن که پیش از این به‌عنوان منشی نظامی نتانیاهو فعالیت می‌کرد، اکنون در رأس مهم‌ترین…</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/16891" target="_blank">📅 01:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16890">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCjVEl5hZMgeuBv7BotPDBED-_o5EryAq-t82_NjiDX-hezr9clgJFhw_zLXHvZs-O-fLX6NVLXQvQp12QesXnJKgfbw1TCpzyjaEwgZedHlc-P_mTmuJx8uDKi12uxN9dmNxUcQMr_ZpToYXJZMGSNNN9VRjQMzW3LzXX9a6r859HOzNuq8tDBZFPGRE9kbeNd_G2jvKh64t15vBQ8_dwxMUoUwceRy-YZiNvr8RlAoFD58BrnKsZPOFxRQEk_iomdqXAlS-V4oGmyBVTJoqJ9n1Ld7-GCyDMwJSbn1Tri1BfM0v2D4jEO7oCbUAno_teeb46QoUe3CS2WU8I7JiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلا رفت برای این سناریو که عصر گفتیم…؟!</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/16890" target="_blank">📅 01:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16889">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حمله موشکی آمریکا به ابرنفتکش ایرانی!</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/16889" target="_blank">📅 01:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16888">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwJLQjYiD0mK4jnzDaxyGh9_8MgcxxbbVSe6dRXImz8uAMxkl3e7juBYSP98G_ogq6wIzpg_vKOfb4_iBVzKVEx88PtEMdN831lVjOl1y8Id22MwsXvXIf5rdhuJbO_e_73rUPjtMxdhMKlxozwr6-SF-4T11VD09f6sdWKjKY02lRyIp4O3woWhzxDZdQpROij_9RBDZNeFmDTSUm8CxViUG4-q60pYKGHKZ-MDHVTJPV3S9oMZmOFs6dBjoybm2n0crWxnehCUn2A3cemxPtnezpOd4u4W2vEVrGwsjr6y4wz9gbpAjda3-1cnm_kDxTbkFfsDlYuQKgKosbg82w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس جدید موساد!
رومن گوفمن، سرلشکر متولد بلاروس و از نزدیک‌ترین چهره‌های مورد اعتماد بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از ۲ ژوئن ۲۰۲۶ ریاست موساد را بر عهده گرفته است.
گوفمن که پیش از این به‌عنوان منشی نظامی نتانیاهو فعالیت می‌کرد، اکنون در رأس مهم‌ترین سازمان اطلاعاتی اسرائیل قرار گرفته؛ انتصابی که از سوی حامیان دولت با استقبال مواجه شده، اما هم‌زمان نگرانی‌هایی را در میان برخی کارشناسان و ناظران امنیتی برانگیخته است.
منتقدان این انتصاب معتقدند که پیشینه حرفه‌ای گوفمن عمدتاً در یگان‌های زرهی و مسئولیت‌های ستادی ارتش متمرکز بوده و او برخلاف بسیاری از رؤسای پیشین موساد، سابقه قابل توجهی در حوزه عملیات مخفی، اطلاعات انسانی یا مأموریت‌های برون‌مرزی نداشته است. از این منظر، برخی تحلیلگران انتصاب وی را بیش از آنکه ناشی از تجربه تخصصی اطلاعاتی بدانند، نتیجه نزدیکی سیاسی و شخصی او به نتانیاهو ارزیابی می‌کنند.
گوفمن در جریان مباحثات داخلی پیرامون جنگ غزه و ساختار حکمرانی این منطقه پس از پایان درگیری‌ها، به‌طور مستمر از مواضع سخت‌گیرانه و قاطع نخست‌وزیر حمایت کرده است. این همراهی موجب شد که او به یکی از اعضای اصلی حلقه تصمیم‌گیری نزدیک به نتانیاهو تبدیل شود و نفوذ قابل توجهی در روند تدوین سیاست‌های امنیتی پیدا کند.
از جمله موضوعاتی که نام گوفمن را در کانون توجه قرار داد، تدوین یک سند داخلی درباره آینده غزه بود که در آن از برقراری حکومت نظامی مستقیم اسرائیل بر این منطقه حمایت شده بود. این پیشنهاد با انتقادهایی در داخل نهادهای امنیتی اسرائیل مواجه شد و برخی محافل بین‌المللی نیز آن را گامی در جهت اشغال بلندمدت غزه تلقی کردند. بنا بر گزارش‌ها، حتی شماری از مقامات ارشد اسرائیلی این طرح را  «از نظر راهبردی خطرناک» و «بیش از حد سیاسی» توصیف کرده‌اند.
گوفمن همچنین در جریان عملیات نظامی اسرائیل در غزه طی سال‌های ۲۰۲۳ و ۲۰۲۴، به‌عنوان نزدیک‌ترین مشاور نظامی نتانیاهو در تمامی تصمیمات راهبردی مهم حضور داشت. منتقدان بر این باورند که این جایگاه، او را با جنجالی‌ترین و بحث‌برانگیزترین مراحل جنگ پیوند می‌دهد. برخی منابع آگاه نیز وی را شخصیتی توصیف می‌کنند که بیش از ارائه ارزیابی‌های مستقل راهبردی، تمایل دارد دیدگاه‌ها و ترجیحات نخست‌وزیر را تأیید و تقویت کند.
در نتیجه، برخی ناظران معتقدند که اهمیت انتصاب گوفمن نه در ایجاد تحول ساختاری در موساد، بلکه در تغییر جهت‌گیری و فضای حاکم بر این سازمان نهفته است. از نگاه آنان، حضور یک چهره کاملاً وفادار به نخست‌وزیر در رأس دستگاه اطلاعاتی اسرائیل می‌تواند به کاهش موانع و فیلترهای داخلی، افزایش نفوذ ملاحظات سیاسی در تصمیم‌گیری‌های اطلاعاتی و همسوتر شدن عملیات پنهان با اهداف و اولویت‌های سیاسی دولت منجر شود. بر اساس این ارزیابی، مأموریت اصلی گوفمن نه اصلاح موساد، بلکه هماهنگ‌سازی هرچه بیشتر فعالیت‌های اطلاعاتی و مخفی اسرائیل با راهبردها و جاه‌طلبی‌های سیاسی دولت نتانیاهو خواهد بود.</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/16888" target="_blank">📅 01:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16887">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFxkzQxRZtycoQJZGQGt2ZgDytknRa_NEbJF3zbOs8DgEAaqxLNRGEVJsSYII2IbxuY430Pr664itJyca-bmQfPlieGtzfI_F7CvPb3iKjYUZ4nFsUNtTQKbPJ_5bbaRwFdkLXzA8EORS-js-8Sq1S7I_BbO1AzOLro0d-ZQIFe1C0iejipoqtwGpG-BT-f60uyFg0OkYK1L6AiFV5ljErtn4Zt4_VSXLxBcxGjIExqUKdpdjZndRW68G2H3ar_cqMgJb_maFs224U0vjdA8mzsHG7Tyz9meXdz2jzbwiEKBIvOTwNWKS2nMst0Pjq_K4IkeJ0oIAYCwbLS04I5ZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلمش را هم به این سرعت بیرون دادند حرامزاده ها!  اینها ثروت ملت ایران است که دود می شود.</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SBoxxx/16887" target="_blank">📅 00:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16886">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/864d5386d4.mp4?token=I2gV-lxIFEsE83nJJBj5R1QkWF14r4tOOd_kYETk-LUHuh9XEOL-MvJcDTMxEwhw7fhbRm2z0rOdzMetnM4CXGOZxgTG-YR3Js8WHZW4gPw7T_1B6f6RJo5FFRfFFShLFXxPgVaT00YUjpmLW81HMueiYq4EZFe01fIaTBeA2w5J_KH1OVTAXRKNsZ-3KK-t1pX-ljDNeNABYkZHnJ8lEDY8loZNvNjt1GCVomofBCiwoSej1OlL1eD-N-n9Utkiszq82Vnrq5K4ZAdRYMXDGgzZK0QP-tqWFaIU9ltaSqcJ9SDim48TvkJoMWpLFUfSWxyxmNCsWia8tlUdmkTC9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/864d5386d4.mp4?token=I2gV-lxIFEsE83nJJBj5R1QkWF14r4tOOd_kYETk-LUHuh9XEOL-MvJcDTMxEwhw7fhbRm2z0rOdzMetnM4CXGOZxgTG-YR3Js8WHZW4gPw7T_1B6f6RJo5FFRfFFShLFXxPgVaT00YUjpmLW81HMueiYq4EZFe01fIaTBeA2w5J_KH1OVTAXRKNsZ-3KK-t1pX-ljDNeNABYkZHnJ8lEDY8loZNvNjt1GCVomofBCiwoSej1OlL1eD-N-n9Utkiszq82Vnrq5K4ZAdRYMXDGgzZK0QP-tqWFaIU9ltaSqcJ9SDim48TvkJoMWpLFUfSWxyxmNCsWia8tlUdmkTC9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران دارای یکی از بزرگترین ناوگان های نفتکش دنیا بود اما با این وضعیتی که پیش می رود باید از شوتی های زحمتکش مرزهای شرقی و جنوب شرقی کشور برای انتقال نفت بهره ببریم!</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/16886" target="_blank">📅 00:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16885">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgWA7NmBTr3kkpJGB2C4e01A5_B0P7hzYVRJae5nxXEJW3IBKzpoeUYCyhTchFrngj276gOIp0X99lg7Ly0FqQKOC5RcBv8KoOwN6MKq6ed3N3hx_8LCS0yE329BU1VaIRoGPD1MkBlXvCcpPlN__vRixaSOmk5UFqde0hujFgvSKGnJqIncbrlXTWarhOuR9ll1Bqbpp9xXh8jSmnlgMN4Vd_mFtCePE8j4EkE4KME4M35jMylXs-60knveZhrPSYAPwni7t2gVTbXo-1_x8Yk6Wd9S-HNoi919yGISPN1dZ-nzymQSf8hYtimyRz2aFPu7Z3KBF2fKzhJauSkAuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران دارای یکی از بزرگترین ناوگان های نفتکش دنیا بود اما با این وضعیتی که پیش می رود باید از شوتی های زحمتکش مرزهای شرقی و جنوب شرقی کشور برای انتقال نفت بهره ببریم!</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/16885" target="_blank">📅 00:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16884">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حمله موشکی آمریکا به ابرنفتکش ایرانی!</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/16884" target="_blank">📅 00:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16883">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حمله موشکی آمریکا به ابرنفتکش ایرانی!</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/16883" target="_blank">📅 00:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16882">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گروه «مریم مقدس» هم با خلع سلاح مخالفت کرد.</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/16882" target="_blank">📅 00:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16881">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گروه «مریم مقدس» هم با خلع سلاح مخالفت کرد.</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/16881" target="_blank">📅 00:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16880">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اصحاب کهف با خلع سلاح گروه‌های مقاومت مخالفت کرد  گروه «اصحاب کهف» که از گروه‌های مقاومت عراقی وابسته به «مقاومت اسلامی» است، روز سه‌شنبه ۲ ژوئن با درخواست‌های سیاسی برای تحویل سلاح گروه‌های مسلح مخالفت کرد و تأکید نمود که استناد به حمایت مرجعیت از این روند،…</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/16880" target="_blank">📅 00:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16879">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">همینطور کتائب امام علی.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/16879" target="_blank">📅 22:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16878">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شما ببینید وضعیت این منطقه گه گرفته چطوری است که پاکستانی که خودش در‌ همین مدت در غرب (بلوچستان)، شمال (وزیرستان) و شرق (هند) غرق در تنش و نکبت بوده حالا دارد برای ما میانجیگری می‌کند!
سبحان الله!</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/16878" target="_blank">📅 22:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16877">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خب گویا اینها هم لازم شده یک گوشمالی اساسی بشوند...  بعد از پیروزی شان در سیندور یکم، خیلی سیس عقاب برداشته بودند و این نمایشهایشان سازندگان سلاح های غربی مورد استفاده هند (خصوصاً جنگنده رافائل) را آزار داده و بیش از حد سلاح سازان چینی را نوازش می داد.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/16877" target="_blank">📅 22:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16876">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♨️
سقوط چشمگیر کاربران پیامرسانهای داخلی در طی هفته اخیر با بازگشایی نسبی دسترسی به اینترنت بین المللی
🩵
منبع : مجله فناوری گجت نیوز</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/16876" target="_blank">📅 20:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16875">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♨️
سقوط چشمگیر کاربران پیامرسانهای داخلی در طی هفته اخیر با بازگشایی نسبی دسترسی به اینترنت بین المللی
🩵
منبع : مجله فناوری گجت نیوز</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/16875" target="_blank">📅 20:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16874">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">فناوری_هوشمند،_جنگ_را_به_انتخابی_احمقانه‌تر_تبدیل_می‌کند.pdf</div>
  <div class="tg-doc-extra">476.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/16874" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">توهم خطرناک جنگ مدرن.pdf</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/16874" target="_blank">📅 19:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16873">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حشد الشعبی نیز به پایان خود نزدیک می شود...  بعد از گروه صدر (سرایا سلام)، امروز گروه عصائب اهل حق نیز اعلام انحلال کرد.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16873" target="_blank">📅 19:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16872">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گویا گروه‌های مسلح تجزیه طلب کردی با حزب الله طاق زده شده اند.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/16872" target="_blank">📅 19:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16871">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وزیر امور خارجه آمریکا، روبیو: ایران فقط به خاطر بازگشایی تنگه هرمز از تحریم‌ها معاف نخواهد شد.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/16871" target="_blank">📅 18:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16870">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇰🇵
رهبر کره شمالی برای خودکشی ( درصورت زنده ماندن فرد ) مجازات اعدام را قرار داد</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/16870" target="_blank">📅 17:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16869">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکاخ رسانه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc85d6917.mp4?token=BfJI5zKx4-5CTLdk49Uam0unfq7x9Sm5cT1bqLiHVWyHVsUQrxDj6VG0QHrvXQWMmptIG6bhqu6DnGw0B9j6_eycyme9ArSULGCmZHecY4oJhRJrfQGd9Ybwu14bCRrNtFijYywIXcpoHw8TtVStwzuzPDJtXv89UuvVxQ10Att01XZJTX-GbJ5bsb9JqQvSymXRBNc8Fek8vrbYq6wwZj15NJTuwd9nB2PJUH-0XnLj3CHYRaI6SeABA96LnQOALI11fxIWbV4buV_kG_D3qVY3AAxOiZ3m_Fpy8k6okNHkIxJ04Vcik-95_RYhd708BMqqnw3Jo9XNh9jkHj6HBXIbxD93n98iKLLfV9jVESIZyIS10YpjXWAqKOEIIOkMB7HwsNaa5-i0mVbBfoSl-yZBVpohtnPNNIDfaVHwDB8RtXWzRCAStg0HH16L77A9FUVnAr944tFBlF8lD-smEz2EfLCHj5OaPS4JLll9WFjGnAbgUFCQqrpPpwqOvoVlk83MNJM-UXjnF5fzFXWeXE6v2V9pDQMgThAp_9iovGaV9-c5UNmq3eUQ2kRkROuSOo35q1nSQIS0k7Ap5kUeFu-hN9-rGe12E6HI7qvvtpP6z9ibpRmN9MrFYLfUIDqZCYHuV3RvbdP6UrVOSCoQQ1b3uRTA0w1lcKS4IQktk2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc85d6917.mp4?token=BfJI5zKx4-5CTLdk49Uam0unfq7x9Sm5cT1bqLiHVWyHVsUQrxDj6VG0QHrvXQWMmptIG6bhqu6DnGw0B9j6_eycyme9ArSULGCmZHecY4oJhRJrfQGd9Ybwu14bCRrNtFijYywIXcpoHw8TtVStwzuzPDJtXv89UuvVxQ10Att01XZJTX-GbJ5bsb9JqQvSymXRBNc8Fek8vrbYq6wwZj15NJTuwd9nB2PJUH-0XnLj3CHYRaI6SeABA96LnQOALI11fxIWbV4buV_kG_D3qVY3AAxOiZ3m_Fpy8k6okNHkIxJ04Vcik-95_RYhd708BMqqnw3Jo9XNh9jkHj6HBXIbxD93n98iKLLfV9jVESIZyIS10YpjXWAqKOEIIOkMB7HwsNaa5-i0mVbBfoSl-yZBVpohtnPNNIDfaVHwDB8RtXWzRCAStg0HH16L77A9FUVnAr944tFBlF8lD-smEz2EfLCHj5OaPS4JLll9WFjGnAbgUFCQqrpPpwqOvoVlk83MNJM-UXjnF5fzFXWeXE6v2V9pDQMgThAp_9iovGaV9-c5UNmq3eUQ2kRkROuSOo35q1nSQIS0k7Ap5kUeFu-hN9-rGe12E6HI7qvvtpP6z9ibpRmN9MrFYLfUIDqZCYHuV3RvbdP6UrVOSCoQQ1b3uRTA0w1lcKS4IQktk2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۵ درصد از کل گاز تولیدی کشور در حملات آمریکا و اسرائیل از بین رفت
در صدا و سیما می‌گویند بعضی حقایق را نگویید
سردبیر خط انرژی
@kakhresaneh</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/16869" target="_blank">📅 15:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16868">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کرملین:  اگر زلنسکی دستور عقب‌نشینی نیروهای اوکراینی از مناطق روسیه را بدهد,جنگ «تا پایان روز» به پایان می‌رسد</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/16868" target="_blank">📅 14:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16867">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کرملین:
اگر زلنسکی دستور عقب‌نشینی نیروهای اوکراینی از مناطق روسیه را بدهد,جنگ «تا پایان روز» به پایان می‌رسد</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/16867" target="_blank">📅 14:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16866">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Faprl8yeV36ecObK9J5qC5cywnVxnvOD5RkM7KzORYToTlDFMrZgNiyN_WonWEy2v5ot_t9NOOsTq-8K32-yyijth4Q-FTftodGFRrFWK6c_2q0B96aRshJaX_t4MsOJqOrT9pQpjAHJKA8lgMtgxVJvFNnIICF1MjLUSrvQR7m-z_kjk5O0PpZCLqy69cCi6XaH9dt7uP3_2hlg7Cw29bYwqdrIuXjXjYPcB9l4BYGUxpmstMd72kT-MdiWQK2kR60eTjL68t0SMJnnrVcHQIENNeD6RFPKkCTyENHzAj5m_8oDTffG7zUHxrKUDuZL6rWqakyknNWfZNobvosWaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله!</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/16866" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16865">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بر اساس ارزیابی مؤسسه CTP-ISW، تعلیق مذاکرات ایران و آمریکا در ۱ ژوئن را می‌توان نشانه‌ای از ترجیح بخشی از حاکمیت ایران به تداوم وضعیت فعلی دانست؛ وضعیتی که نه به توافقی محدودکننده منجر شده و نه به رویارویی مستقیم و گسترده با آمریکا. اعلام این تصمیم از سوی…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/16865" target="_blank">📅 13:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16864">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خلاصه دیدگاه موسسه مطالعات جنگ درباره اهمیت راهبردی کنترل تنگه هرمز در دکترین جدید بازدارندگی جمهوری اسلامی:  مقامات ارشد ایرانی در ماه‌های اخیر بار دیگر بر اهمیت راهبردی تنگه هرمز به‌عنوان یکی از اصلی‌ترین ابزارهای قدرت و بازدارندگی جمهوری اسلامی تأکید کرده‌اند.…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/16864" target="_blank">📅 13:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16863">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فرستاده آمریکا باراک:   این بخش از جهان تنها زور را میپذیرد</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/16863" target="_blank">📅 12:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16862">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">این تصویر را ترامپ دیروز پست کرده بود.  کلمه discombobulator را پیشتر ترامپ در توصیف سلاح مخفی سری که آمریکا در جریان ربودن مادورو استفاده کرد به کار برده بود و دیروز دوباره گویا به این سلاح اشاره کرده است.  گویا این سلاح به نوعی در مختل کردن کلیه دستگاه های…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/16862" target="_blank">📅 11:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16861">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آکسیوس: مشاجره شدید ترامپ و نتانیاهو بر سر تشدید تنش‌ها در لبنان  اکسیوس گزارش داد که دونالد ترامپ در تماس تلفنی با بنیامین نتانیاهو به‌شدت از تشدید عملیات اسرائیل در لبنان انتقاد کرده است.  بر اساس این گزارش، ترامپ با لحنی تند به نتانیاهو گفته است:
▪️
«تو…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/16861" target="_blank">📅 07:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16860">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آکسیوس: مشاجره شدید ترامپ و نتانیاهو بر سر تشدید تنش‌ها در لبنان
اکسیوس گزارش داد که
دونالد ترامپ
در تماس تلفنی با
بنیامین نتانیاهو
به‌شدت از تشدید عملیات اسرائیل در لبنان انتقاد کرده است.
بر اساس این گزارش، ترامپ با لحنی تند به نتانیاهو گفته است:
▪️
«تو دیوانه شده‌ای. داری چه کار می‌کنی؟»
▪️
«اگر من نبودم الان در زندان بودی.»
▪️
«دارم تو را نجات می‌دهم.»
▪️
«الان همه از تو متنفرند.»
▪️
«به خاطر این اتفاقات، همه از اسرائیل متنفر شده‌اند.»
یک مقام آمریکایی به آکسیوس گفته این تماس یکی از
پرتنش‌ترین و تندترین گفت‌وگوها
میان دو رهبر بوده است.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/16860" target="_blank">📅 07:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16859">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from📣خبر فوری ایران💯</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11be99e5c8.mp4?token=FRI-MxwyVGNse2HDQ6GCVJ-0MfekNKQH7RIMW55Nj1N01nzlRGHPGTDW0DczbvXMtj610EXWuWZ82G1jwXkBBPXD9iFkphGzMO-UOw_CJfbv1qL_JAdnmR3og0JnjogMBwwVdeF8jhB2x5--EHNjb3g0OOGnKVOzPzEA8VCVFqUCkI0Fjz1ApFXqZGMwqRGhBjrXcxkMxYl4gihwU0QJHxA_cYuu72n91J16d8wXDO5tnFiCAlPfWjHd0ihBgqmW5gCX89aMkXRdcWyYgZxhA4ovutKEaorPgSTGaFiCs_-RrZqkfqWZ9Twp4ztq7ltAFomw6KT7xJxEbANVrKzCrzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11be99e5c8.mp4?token=FRI-MxwyVGNse2HDQ6GCVJ-0MfekNKQH7RIMW55Nj1N01nzlRGHPGTDW0DczbvXMtj610EXWuWZ82G1jwXkBBPXD9iFkphGzMO-UOw_CJfbv1qL_JAdnmR3og0JnjogMBwwVdeF8jhB2x5--EHNjb3g0OOGnKVOzPzEA8VCVFqUCkI0Fjz1ApFXqZGMwqRGhBjrXcxkMxYl4gihwU0QJHxA_cYuu72n91J16d8wXDO5tnFiCAlPfWjHd0ihBgqmW5gCX89aMkXRdcWyYgZxhA4ovutKEaorPgSTGaFiCs_-RrZqkfqWZ9Twp4ztq7ltAFomw6KT7xJxEbANVrKzCrzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه با یک خانم فرانسوی در میدان انقلاب تهران که در تجمعات انقلابی این شبها شرکت می کند
🆑
@kh_fouri
🇮🇷</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/16859" target="_blank">📅 00:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16858">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GO1MmS6wXv8BZmdwmA6Ls4W8_gNvNMV2ziabppXLCVChP3JyWZcTkI_SUBNaa6-JszfQWawUf3H9fwEibJ4xErI4Cm2hqHHn1F2yvpDpqxMOwGKf7HaRWg282g6Fq5tL79o7bJvkp93F6ZU8rXhecaXLj4NgCrPfEQo7q3zdnXOQvFNc8Fhk-940gGMwS7Y4wG1NtgZRwXlrCFHFFVa2zqU7e_Nq5BBoHWPsyKDJN3pfvlAhtBiqgoK_ha0lgWIfHs9D0n5C-rKxCLRxsfK5Vo1xM_R04yLRBAX5wo9MJo7-TCKpzKwug-E7Q7iYLETpxb8kdxTtM4oSZYrEdGu3sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
قالیباف در گفت‌وگو با رئیس مجلس لبنان: جان ما و شما یکی، و پیوند ایران و لبنان ناگسستنی است
💬
رئیس مجلس و رئیس هیات مذاکره کنندۀ ایران در گفت‌وگو با نبیه بری، رئیس مجلس لبنان:
🔻
حزب‌الله و امل امروز هم از سرزمین مادری‌شان و هم از امت اسلامی دفاع می‌کنند. از این جهت پیوند ایران و لبنان ناگسستنی است و جان ما و شما یکی است.
🔻
در ۲ روز گذشته با جدیت توقف حملات اسرائیل را دنبال کرده‌ایم و اگر جنایت‌ها ادامه پیدا کند نه‌تنها روند گفت‌وگوها را متوقف می‌کنیم بلکه جلوی رژیم‌صهیونیستی خواهیم ایستاد.
🔻
ما مصمم هستیم که آتش‌بس در همه‌جای لبنان و به‌ویژه در جنوب این کشور برقرار شود.
🔻
چنانچه توافقی برای پایان جنگ بین ایران و آمریکا شکل بگیرد شامل توقف حملات در همه جبهه‌ها به‌ویژه لبنان خواهد بود.
🔸
رئیس مجلس لبنان ضمن تقدیر از تلاش‌های جمهوری اسلامی ایران برای توقف جنایت‌های رژیم صهیونیستی گفت: لبنان هرگز مواضع مثبت ایران در این مرحلۀ حساس را فراموش نمی‌کند.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/16858" target="_blank">📅 00:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16857">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شما خونه تون مورچه داره؟!</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/16857" target="_blank">📅 00:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16856">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حزب الله پیشنهاد آتش بس را رد کرده و به سمت شمال اسرائیل حمله راکتی کرد!</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/16856" target="_blank">📅 00:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16855">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ادعای رسانه اسراییلی: تعویق حمله به ضاحیه بیروت در پی مداخله آمریکا  سازمان رادیو و تلویزیون اسراییل  گزارش داد که طرح حمله نظامی به ضاحیه جنوبی بیروت به دلیل دخالت‌های طرف آمریکایی به تعویق افتاده است.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/16855" target="_blank">📅 23:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16854">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نمیدانم منظور جناب ولایتی از اشاره به «ذات السلاسل» کدام جنگ است اما بد نیست بدانید که هر دو جنگ موسوم به این نام توسط سگ هایی رهبری شد که هم ضدایرانی بودند و هم ضدشیعی.   یکی توسط عمروعاص (دوست صمیمی رفیق بهزاد ف) ضد وحوش دیگر عرب و دیگری توسط خالد بن ولید…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/16854" target="_blank">📅 22:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16853">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نمیدانم منظور جناب ولایتی از اشاره به «ذات السلاسل» کدام جنگ است اما بد نیست بدانید که هر دو جنگ موسوم به این نام توسط سگ هایی رهبری شد که هم ضدایرانی بودند و هم ضدشیعی.
یکی توسط عمروعاص (دوست صمیمی رفیق بهزاد ف) ضد وحوش دیگر عرب و دیگری توسط
خالد بن ولید
حرامزاده ضد ایرانیان.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/16853" target="_blank">📅 22:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16852">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ولایتی:
بمباران ضاحیه ونقض آتش‌بس عجلۀ رژیم جعلی برای پایان دادن به تاریخ نحس خویش است.
🔹
شما آغاز کردید، اما برخلاف انفعال تماشاچیان منطقه، ایران و جبهه مقاومت تا آخر کنار مردم عزیز لبنان، از مسلمان تا مارونی ایستاده است.
🔹
تاریخ تکرار میشود و پاسخی از جنس «ذات‌السلاسل» در راه است تا زنجیرهای اسارت را بگسلد. «نقطه‌ی پایان این کتاب باماست».</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/16852" target="_blank">📅 22:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16851">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انتشار اخباری دال بر پرتاب موشک از کرج!</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/16851" target="_blank">📅 21:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16850">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انتشار اخباری دال بر پرتاب موشک از کرج!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/16850" target="_blank">📅 21:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16849">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqmAAxpyz6Kxw7AHRQSaqc88n7SHQU1QZajFYL9B5BHRmL-30aw_OY9cjLEWAOELT5DGVWkoa0ETn34PoZLJM0nS9uGrRvtsiIdMbgxg_u9rqr-YhsCLiPaaa7NaTQfQ9b1RIscFO6Ktv5c0zaG1_ZHiTTDCvOEt3DMUH4tCMZYWIsEXdRt617EVCUVmcUHY-Vhveia7Br6RlUtpfC9ZNnhMCvlmvduCLbMUQxP-xiGemPzVSWoxU4MuK4QG8vGstj52vuWxZNJ3xlxJppoPe19UzDSxaMcL5vpPMgzLMNM4_NMPi81tmLRTDn8w6x8TPk86dygO6cttqRkIA1Cm5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این جهش وحشتناک قیمت نفت در همین یکی دو ساعت، ترامپ مجبور به عقب نشینی است.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/16849" target="_blank">📅 21:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16848">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حزب الله از طریق ناهیب بري، رئیس پارلمان لبنان، به ایالات متحده اطلاع داده است که آماده پذیرش آتش‌بس کامل و فوری با اسرائیل است.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/16848" target="_blank">📅 20:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16847">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">با این جهش وحشتناک قیمت نفت در همین یکی دو ساعت، ترامپ مجبور به عقب نشینی است.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16847" target="_blank">📅 20:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16846">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ادعای رسانه اسراییلی: تعویق حمله به ضاحیه بیروت در پی مداخله آمریکا  سازمان رادیو و تلویزیون اسراییل  گزارش داد که طرح حمله نظامی به ضاحیه جنوبی بیروت به دلیل دخالت‌های طرف آمریکایی به تعویق افتاده است.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16846" target="_blank">📅 20:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16845">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">— رئیس‌جمهور آمریکا ترامپ و نخست‌وزیر اسرائیل نتانیاهو در حال حاضر در حال صحبت تلفنی هستند.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/16845" target="_blank">📅 20:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16844">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">چرا میخند؟</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/16844" target="_blank">📅 20:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16843">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">با دوستان مروت؛ با دشمنان مدارا</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/16843" target="_blank">📅 20:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16842">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">محسن رضایی: صبر ایران حدی دارد  تنگه هرمز تحت مدیریت ایران است. اجازه تداوم محاصره دریایی را نخواهیم داد و تشدید تنش در لبنان هم تحمل نخواهد شد. صبر نیروهای مسلح جمهوری اسلامی ایران حدی دارد.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/16842" target="_blank">📅 20:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16841">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">با این جهش وحشتناک قیمت نفت در همین یکی دو ساعت، ترامپ مجبور به عقب نشینی است.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/16841" target="_blank">📅 20:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16840">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ به ان‌بی‌سی: ما محاصره تنگه هرمز را حفظ خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/16840" target="_blank">📅 19:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16839">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ به ان‌بی‌سی: ما محاصره تنگه هرمز را حفظ خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/16839" target="_blank">📅 19:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16838">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حالا توجه کنید که در همین مدت که آمریکایی ها دهها کشتی تجاری را از تنگه هرمز عبور داده اند، محاصره دریایی شان را کماکان اعمال میکنند و این یعنی کارتی که ایران دارد (تنگه هرمز) در حال کم اثر شدن است اما کارتی که آنها دارند (محاصره دریایی) کماکان در دستشان باقی…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/16838" target="_blank">📅 19:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16837">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">محسن رضایی: صبر ایران حدی دارد
تنگه هرمز تحت مدیریت ایران است. اجازه تداوم محاصره دریایی را نخواهیم داد و تشدید تنش در لبنان هم تحمل نخواهد شد. صبر نیروهای مسلح جمهوری اسلامی ایران حدی دارد.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/16837" target="_blank">📅 19:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16836">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVLpOO_7TBluWXd6F6WTuAl4f0G0cUEC2NiPrq0t3TlpLQtvTEFmKRlFdsYh0Ihn1dSWxjslPt-6O6x3tNJYKRQRZ7dxVmLYbg0w9NGyAs3AzzsccK3wD5ycBY5lU7-d-iGeWqcUikS1cVAxwZBoKZSCCmLMWFtjnAkIcTJWkPK25iFl26MVbXZjpF0u92HcvJvhbiJ2IQ_t5nHd3Swe5UpRhQP6IvocgQbpOPjv5Jz_8YqUSQTk2mwrpkwQ-4oEjGk5Ste3qI9h2NaJZuYxNPXWPQN7D5iMDxb0L4riu_OSopCRfR0_4DRQ95NhSt_PPnJrQYoS8UDtN3gsQdSvdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایده خوبی است بسم الله!</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/16836" target="_blank">📅 18:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16835">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عراقچی: نقض آتش بس در یک جبهه، نقض آتش‌بس در تمام جبهه‌هاست  آتش‌بس میان ایران و  آمریکا، بدون هیچ ابهامی، آتش‌بسی در تمامی جبهه‌ها، از جمله لبنان، محسوب می‌شود.  نقض این آتش‌بس در هر یک از جبهه‌ها، به منزلۀ نقض آن در تمامی جبهه‌هاست.  آمریکا و اسرائیل مسئول…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/16835" target="_blank">📅 18:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16834">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">قیمت کنونی ۱۶۹</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/16834" target="_blank">📅 18:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16833">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">با این جهش وحشتناک قیمت نفت در همین یکی دو ساعت، ترامپ مجبور به عقب نشینی است.</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/16833" target="_blank">📅 17:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16832">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خواننده Secret Box از‌ همان روز توافق میدانست که اندوه لبنان خواهدکشت ما را.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/16832" target="_blank">📅 17:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16831">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خب در توافق بحث پایان جنگ در لبنان هم مطرح شده و لذا میتوان گفت این بندش هیچ وقت اجرا نخواهدشد.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/16831" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16830">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ایران اعلام کرد که آماده بستن کامل تنگه هرمز و تنگه باب‌المندب است اگر اسرائیل حملات به بیروت را متوقف نکند</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/16830" target="_blank">📅 17:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16829">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سخنگوی وزارت خارجه:
ما حق دفاع مشروع در برابر نقض آتش‌بس توسط آمریکا را داریم و امروز هم مبدأ تجاوز به خاک کشور را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/16829" target="_blank">📅 17:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16828">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">عراقچی: نقض آتش بس در یک جبهه، نقض آتش‌بس در تمام جبهه‌هاست
آتش‌بس میان ایران و  آمریکا، بدون هیچ ابهامی، آتش‌بسی در تمامی جبهه‌ها، از جمله لبنان، محسوب می‌شود.
نقض این آتش‌بس در هر یک از جبهه‌ها، به منزلۀ نقض آن در تمامی جبهه‌هاست.
آمریکا و اسرائیل مسئول پیامدهای هرگونه نقض این آتش‌بس خواهند بود.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/16828" target="_blank">📅 15:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16827">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">برکشایر هاتاوی اکنون بیش از هر زمان دیگری در تاریخ خود پول نقد در اختیار دارد</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/16827" target="_blank">📅 14:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16826">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بنیامین نتانیاهو به همراه وزیر دفاع اسرائیل دستور حمله به ضاحیه بیروت را اعلام کردند و گفته می شود ستونی طولانی و عظیم از خودروهای مردم به سمت مناطق شمالی بیروت و بیرون از آن در حرکت هستند.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/16826" target="_blank">📅 13:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16825">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">قالیباف:
محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش‌بس است و هر گزینه‌ای بهایی دارد که پرداخت خواهد شد.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/16825" target="_blank">📅 13:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16824">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بنیامین نتانیاهو به همراه وزیر دفاع اسرائیل دستور حمله به ضاحیه بیروت را اعلام کردند و گفته می شود ستونی طولانی و عظیم از خودروهای مردم به سمت مناطق شمالی بیروت و بیرون از آن در حرکت هستند.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/16824" target="_blank">📅 11:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16823">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">️صدای انفجارها در بندرعباس کنترل شده است
صدا‌هایی که دقایقی قبل مردم در سطح شهر بندرعباس شنیدند ناشی از امحای مهمات عمل نکرده است.
روابط عمومی استانداری هرمزگان اعلام کرد: انفجار‌های صورت گرفته کنترل شده است و تا ۷۲ ساعت ادامه دارد و مردم نگران نباشند.
این انفجارهای کنترل شده از دیروز آغاز شده است و تا فردا سه شنبه ادامه دارد.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/16823" target="_blank">📅 10:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16822">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">این جریان استعفاهای پزشکیان هم مثل خداحافظی های کریم باقری است.
سبحان الله!</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/16822" target="_blank">📅 09:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16821">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حالا توجه کنید که در همین مدت که آمریکایی ها دهها کشتی تجاری را از تنگه هرمز عبور داده اند،
محاصره دریایی شان را کماکان اعمال میکنند
و این یعنی کارتی که ایران دارد (تنگه هرمز) در حال کم اثر شدن است اما کارتی که آنها دارند (محاصره دریایی) کماکان در دستشان باقی است.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/16821" target="_blank">📅 09:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16820">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ارتش آمریکا به ۷۰ کشتی تجاری کمک کرده تا در ۳ هفته گذشته با خاموش کردن سیستم GPS خود از تنگه هرمز عبور کنند.  به نظرم این رادارهای ما را میزنند تا توان رهگیری اهداف متحرک از سپاه سلب بشود و سپس کشتی ها را خارج می‌کنند.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/16820" target="_blank">📅 09:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16819">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ:
ایران واقعاً می‌خواهد معامله‌ای انجام دهد و این معامله برای ایالات متحده آمریکا و کسانی که با ما هستند، بسیار خوب خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهان به ظاهر غیر میهن‌پرست درک نمی‌کنند که وقتی سیاستمداران فرصت‌طلب بارها و بارها با سطحی بی‌سابقه به صورت منفی «نق» می‌زنند و می‌گویند که من باید سریع‌تر حرکت کنم، یا کندتر، یا به جنگ بروم، یا به جنگ نروم، یا هر چیز دیگری، برای من بسیار دشوارتر است که به درستی شغلم را انجام دهم و مذاکره کنم؟
فقط بنشینید و آرام باشید، همه چیز در نهایت خوب پیش خواهد رفت - همیشه همینطور بوده است!
رئیس‌جمهور DJT</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/16819" target="_blank">📅 08:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16818">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIRg0UN0k1n8AjRCSfy8Q5aKAP_PocPUxj_JtZ9GlIvjeI1R8FsdNUD1s_sER90gjiVuOgTXnl8B-tbJU3hvhWd9_tAApgF6g7I1dski7sBMgpvwP27Uwx6FY5j81uBpgZwHddSgGcw6VpjPwPU3oYcNQXLDdazqxQ4QlXSz7niFQJkxJsTLFgkvBcwlRs44G_Qk8okxl5DbNPq3-1Z_lxG18QWmJqac3RyMkiYGwhQJKHLDs9HMJpNb77htY7xpysSdZvqLonXTSnYOeE2KfarXM7Wz074IWx2G-7QMT8xmuC9hK_Cz9WXkbl8GExKqRu1SEZjdZ62XMPoIyEZbEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات آمریکا به رادارهای ایرانی و پاسخ سپاه   مرکز فرماندهی مرکزی (CENTCOM) اعلام کرد که حملاتی را به عنوان «ضربه‌های دفاع از خود» علیه سایت‌های راداری و فرماندهی در گورک و جزیره قشم انجام داده است.  در پاسخ، نیروی هوافضای سپاه پاسداران پایگاه هوایی که حمله…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/16818" target="_blank">📅 08:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16817">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pm8SXdTxTihq6bZLx5aHd8wlJ2FV_bkHpsBdbGyEr8tklGUEl9gqbyX5AIAoUW96a1dJdmgtYU_dQWEFX-ROs_iYoj5tlkq2tNcBUTtEiCdk0zZNXO6h5N1Z9YUt2p53djn14IoKlJ9IM9JcbW05f5wVKZ9O2qa6pANq2o5qPLnjajyFddhJDOO5Htcp4ktQ9QGzUzKFoI4z2TxBxNx813rkXuJvXmTVXOZ7dmdj_CILAA0xRcab0rCV2unKoIiTCc4atcgjCnUpnX_vNSYKattqMCcuawrVRMhtjkTFaIRnaHvOdNnTNoMW4xXuxiM1pf94pI2RrsHardrSOX_mpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این وضعیت به نظرم دوشنبه نفت با گپ مثبت باز بشود</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/16817" target="_blank">📅 08:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16816">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حملات آمریکا به رادارهای ایرانی و پاسخ
سپاه
مرکز فرماندهی مرکزی (CENTCOM) اعلام کرد که حملاتی را به عنوان «ضربه‌های دفاع از خود» علیه سایت‌های راداری و فرماندهی در گورک و جزیره قشم انجام داده است.
در پاسخ، نیروی هوافضای سپاه پاسداران پایگاه هوایی که حمله آمریکا از آنجا آغاز شده بود را هدف قرار داد و گفت که «اهداف پیش‌بینی شده نابود شدند».
ارتش کویت نیز این وسط از فعالیت‌های پدافند هوایی در منطقه گزارش داد.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/16816" target="_blank">📅 08:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16815">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">دیسکامبوباتور.pdf</div>
  <div class="tg-doc-extra">200.8 KB</div>
</div>
<a href="https://t.me/SBoxxx/16815" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این تصویر را ترامپ دیروز پست کرده بود.  کلمه discombobulator را پیشتر ترامپ در توصیف سلاح مخفی سری که آمریکا در جریان ربودن مادورو استفاده کرد به کار برده بود و دیروز دوباره گویا به این سلاح اشاره کرده است.  گویا این سلاح به نوعی در مختل کردن کلیه دستگاه های…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/16815" target="_blank">📅 00:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16814">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kavpAiRSpPP72fa-PYtKCS3CWuclPhVZMdce6na8j0Ir0b_mu9yVsEO10glANnDnFFpnRZ1atvATb8C_YNhK7dpdlA7g1p2UlEC65RswAO7ZyLzE4FSwNWhxUJ9atY60nHy4vyrumfTOG7H8dOIAXn8Yiat82GhkWX3akOXglfxfHE7ugqR01aH4bZUvsqeDK4wk99FVB9uz79ynlCHyuHHYy2H_g4G5F2vj5nwl8A9Tul9zAL2c1glh6oOO62aLHl2EgxiuXq3oxl2gDHqp-jeqD0RBz0X8w90yK6Xg0thw-eiTntIqDfs9OzpzS-HVhePlIOa6AUq55GlGbx_zew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا در تهران نوعی خرابی وسایل برقی، نوسان جریان برق، ناپایداری نت حس می کنید؟  بله:
👍🏻
خیر:
👎🏻</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/16814" target="_blank">📅 23:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16813">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آیا در تهران نوعی خرابی وسایل برقی، نوسان جریان برق، ناپایداری نت حس می کنید؟
بله:
👍🏻
خیر:
👎🏻</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/16813" target="_blank">📅 23:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16812">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCccrh-xau3bbyfjszQt83HUX5hxnDkU7852sb42k4-tnz9xgFHffckVQ6an6n9Th2hD12y43vJuiKnuTzHrS0q1tAaXDCEeMGe8L7TWkrI0qLlhhqRQ6oQZu9Vcowq4qY7t2D2kHPuTXio16NGI0ewr7YA8HyHmqjVGCmBOKKLEd7d7FZ4ZiO9-6MjAfeGOovUGOolAqKwdZtxnORqoPSUQ9aZo2LxfJu22gedct8qVXcRjqgTJAfpszoNi8CTZ34Futn7eMeHVhcKU4xG7mFg7Zb0u2BZI5JopE9M7ayNMaHSMPCcmJJSu8JounzMYpt2hg7fWGYc57IxB8fdF_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت جنگ در جنوب لبنان!
منطقه بنفش تصرفات اخیر ارتش اسرائیل
منطقه سرخ محدوده بمباران ها و تنشهای نظامی</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/16812" target="_blank">📅 20:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16811">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بسیار کار خوبی است و باعث کاهش فشار روی سرورهای پورن هاب می شود.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/16811" target="_blank">📅 20:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16809">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکاخ رسانه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qw6cfn-VMVuBofhuvif6BO3m0WxDLvFKefU3C-EjD1-j3Bei6K7ic-0cfvaDh6pcLmlxVwbfhhgG0Uhb2mYu--gEinVtWpHoVG983OM3eV6Mf-bK9_5kbxw6PJJZKZ1MgJ8QXx9LC3y0YSbWX-BnxX8LxQCMmfMfiz794xuLk7ViSf4wjrMO7vaIrrDWEaCbF9swMqp8qVM8a0bJy2_SHjcLYsb1Pnuo8SGHufzWmgco-d1oBYWJfUcmGjNQOnDv9HgoROpV6yHOAY33lzih4K6fYH0_Ph269hyXIWp9er-HjYGhbQ3JX600i3FmiXS_KIUGzCjgdRGqLT6MDzPoag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l5shyTiKGTayJnsRxrJEtwiVOJm_9_QGmalfeaPp_LXJ44rVBG3PD4bNPFrKTiQdeOI1i0TN0nq_KwPusP5mJ5kzuWKLNHiOdEeFlRHCuqwGVcllaekgqBvD9PnbVcSamqnFHhVt2bRBuK3Q6Mr3BE3Fx9Zx5V1-r81e08nwVvX2oD5xsyIzfNWY17TrLwhAsS7c3mQqZKruV1VOcD5gz1TVlyRUnmATWYjtXKM0W4TWeLF-zZMQWdkdsTyk3HvoF_Lmzct5cW6iUZrUbGEyY_9R6L22lK5b2qufDett1TEbjSRp2bvtO0kVQjWqnpaCQ567AUVv9Vk1eOe8malI8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک کمپین عجیب در خبرگزاری فارس
گزینه «قطع داوطلبانه دسترسی به اینترنت بین‌الملل» را فعال کنید!
ایجاد کننده کمپین صالح اسکندری از موسسین حزب شریان است
@kakhresaneh</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/16809" target="_blank">📅 20:03 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
