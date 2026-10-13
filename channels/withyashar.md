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
<img src="https://cdn4.telesco.pe/file/PXznIYUHZoaZWtgQuzOdHqslrEOf_xc3VF3Q1IySwxylmHyt8eUkTbO3I-yo0pHlACR5-64Q1IqITS7r78lWniQL7Upiqu6Y9BrOc3BCxT1sZ6lAOzQyguAja5e1dRhg6zAlqOcj0tluKKaZLDzm1xXb5miOj596zuDyOa5IMpsdF1iJFvFOCy6-N4GhOkeeIoH9YWKL-4peh8zxvQUNZwJ3ATgQDeh_FpZXoIof3YMZ68Rt6wYAMvtu101LA6BB6OzUrTAfQ7qRtajf7RFEZq96qk3UkrjY0DdXiylGwWOSy_uNYaCEdHWoRNFd0zgxAoGWAmkecDTrg3N5ug0M5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 496K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 02:50:38</div>
<hr>

<div class="tg-post" id="msg-25588">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پدافند شرق تهران با یه پهپاد شناسای درگیر شده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/withyashar/25588" target="_blank">📅 01:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25587">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : بوش بابا بعد از ریکاوری در پاتایا داره بر میگرده و موقعیت ناو روزولت و …. سوال ها رو کامنت کنید، همشو  تلگرام جوایب میدم لینک چنل تلگرام در بابیو⁩  https://www.instagram.com/reel/Decq0BfRPmP/?exln=MWh5Z2hqOXdjaXR5eA==  کارای اداری رو…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/withyashar/25587" target="_blank">📅 01:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25586">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حقیقت یاب
سنتکام:
ادعا:
فرمانده نیروی دریایی سپاه پاسداران امروز مدعی شد که تنگه هرمز تحت کنترل سپاه است و هر ناو جنگی آمریکایی که نزدیک شود، «غرق خواهد شد».
واقعیت:
فرمانده نیروی دریایی سپاه، نیروی دریایی‌ای در اختیار ندارد. نیروهای آمریکا و شرکای منطقه‌ای آن کنترل تنگه هرمز را در دست دارند. همین دیروز، نیروهای آمریکایی به کشورهای منطقه خلیج فارس کمک کردند بیش از
۱۹ میلیون بشکه نفت خام
از طریق این تنگه منتقل شود.
@WarRoom</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/withyashar/25586" target="_blank">📅 01:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25585">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آکسیوس : پیت هگست، وزیر جنگ آمریکا، و فرماندهان ارشد سنتکام از حامیان اصلی ازسرگیری حملات نظامی علیه ایران هستند؛ اما بخش زیادی از مشاوران ترامپ ترجیح می‌دهند فعلاً فشار اقتصادی و تحریم‌ ادامه پیدا کند
@WarRoom</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/withyashar/25585" target="_blank">📅 01:19 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25584">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دقایقی پیش جزیره کیش صداهای ناله ابل رحیم موسوی از دریا شنیده شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/withyashar/25584" target="_blank">📅 01:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25583">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس:
نتانیاهو در جلسات اخیر با مقام‌های ارشد امنیتی اسرائیل مدعی شده که این ترامپ بود، نه او، که بحث حمله به ایران پیش از انتخابات را مطرح کرد. به گفته یک مقام ارشد اسرائیلی، ترامپ از نتانیاهو پرسیده است که آیا اسرائیل نیز به این عملیات خواهد پیوست. یک مقام آمریکایی نیز گفته
ترامپ به نتانیاهو گفته است: «آماده شو»
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/25583" target="_blank">📅 00:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25582">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/25582" target="_blank">📅 00:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25581">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMBHKYoWqlVO_B59soK3Eh0rimTNaoF9VoP_SIwB68JiBCJgg8IBan8mLR6hDiq_U8u-lr2Ho8upBuZObo0ykS7LEXCJHdfpPdgifn2gvHx2SHMu8Ok0F9Qa5W9gJjOHuD3LGdg8wwXaquzL63f_iNG85pd7AWmOdrPGpkcjHWjPucQYgonh5NJEw73DsXlBdaKGSvSNnlwKLp7a5I8nwcZdJg1RwYiSSGyppnpGaKbkLlT7zCgTbsdZF2I3QWqPgRSY9H4NNVe7YHWzNpVyBCmG3ht2TiO0cSjaLuNuRkI3vqJkt-MhKuuGCny0P5FjNcDjtYH327gYmqqsXNrL-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : بوش بابا بعد از ریکاوری در پاتایا داره بر میگرده و موقعیت ناو روزولت و …. سوال ها رو کامنت کنید، همشو  تلگرام جوایب میدم
لینک چنل تلگرام در بابیو⁩
https://www.instagram.com/reel/Decq0BfRPmP/?exln=MWh5Z2hqOXdjaXR5eA==
کارای اداری رو یادت نره</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/25581" target="_blank">📅 00:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25580">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/25580" target="_blank">📅 23:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25579">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبراییه
😁</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25579" target="_blank">📅 22:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25578">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2uFHDbczqgT8ECgxvhvwBeJVCgQ2rlqHbv7J4fKEh-_LJ4qQPbyVnD-EDEOJO7e12Z-hjQTndDkDGT4P82_Lo4HSvSZXVq1dNGA8NEDCOmGdRWksXb9YAqT0yZy9XxSfbNXCnpPzpSvCqpWmcBA3rywF7oasDhmuT93GrDrk0civCKXqSYTMfBx6NFQ8v1WUOOFmW4T6GlRcMFrP8SgDAjG9LNSU8mgQvwNwhCFXVF9AJCbJUL1d7we4UvOoL17UNnOk-WZHGvPg6c_0ewezlDX9XRrb9h___T2L8Uwxpby5GwOi_WMKWZ8yL1BnSB3XX2JmfO-oQ7YEKr1-Oxc2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی مبنی بر وقوع حادثه‌ای در تنگه هرمز دریافت کرده است. یک منبع موثق گزارش داده است که یک کشتی کانتینربر هدف اصابت پرتابه‌ای ناشناس قرار گرفته است. مقامات در حال بررسی موضوع هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25578" target="_blank">📅 22:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25577">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سخنگوی ائتلاف: رهگیری موفق و انهدام دو موشک بالستیک که توسط شبه‌نظامیان حوثی به سمت شهر الجبیره و منطقه حرض شلیک شده بودند انجام شد . قطعاتی از شلیک‌های دفاعی در یک منطقه مسکونی در الجبیره سقوط کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25577" target="_blank">📅 22:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25576">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏ حملات جنگنده های عربستانی به مخازن نفت صنعا در یمن  @WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25576" target="_blank">📅 22:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25575">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کانال ۱۴ اسراییل : اسرائیل بعد از دو حمله غافلگیرکننده، خود را برای احتمال حمله نخست ایران آماده می‌کند
در پی احتمال فزاینده مبنی بر اینکه رژیم ایران که پیش‌تر دو بار در جریان عملیات‌های اسرائیل غافلگیر شده است ممکن است با اجرای یک حمله غافلگیرکننده و گسترده متقابل درصدد تغییر موازنه برآید، نهادهای امنیتی اسرائیل در بالاترین سطح هشدار قرار گرفته‌اند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25575" target="_blank">📅 22:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25574">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f8d98845.mp4?token=Ns0lzwa80Rr4PkTcN86J8gLEbwF6kQAihba0ouvOLc-f-WT6u0ABRWalVQF8zUBpRW4bwOWvMbgGtTtplRMalPaIP0IhCsnbBkUeijvcygDsKJrUVhDfTOQh7rl_1y86XrqLEMuBvHYen7EZBJeh4tVyzgJlCQss4lZW_4OveGl_pCk_rjV2Y8tql3c_TOW4E_eFZkxLPlnE4H4ZEQNN3zuqbHtuofFxEsjbXVOOYH352ndCaEiokTidvfxTkiWyYDx3bAKsSYlOvL0XjXA1PuVyLzyOVdFiMO-PQ-xI_nRQWcONP6ElJsc8ZRCO5sug3uPDegdm8uSx5AXgca2K5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f8d98845.mp4?token=Ns0lzwa80Rr4PkTcN86J8gLEbwF6kQAihba0ouvOLc-f-WT6u0ABRWalVQF8zUBpRW4bwOWvMbgGtTtplRMalPaIP0IhCsnbBkUeijvcygDsKJrUVhDfTOQh7rl_1y86XrqLEMuBvHYen7EZBJeh4tVyzgJlCQss4lZW_4OveGl_pCk_rjV2Y8tql3c_TOW4E_eFZkxLPlnE4H4ZEQNN3zuqbHtuofFxEsjbXVOOYH352ndCaEiokTidvfxTkiWyYDx3bAKsSYlOvL0XjXA1PuVyLzyOVdFiMO-PQ-xI_nRQWcONP6ElJsc8ZRCO5sug3uPDegdm8uSx5AXgca2K5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی ذغال‌فروش ، فرمانده نیروی دریایی سپاه: امروز آمریکا با 7 ناوگان خود به قاچاقچی سوخت تبدیل شده.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25574" target="_blank">📅 22:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25573">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دفتر نتانیاهو : نخست‌وزیر، ترامپ را تشویق نمی‌کند که قبل از انتخابات، ایران را مورد حمله قرار دهد، بلکه با او و مقاماتش در حال گفتگو است.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25573" target="_blank">📅 21:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25572">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">وزارت امور خارجه ایران امروز سفیر بریتانیا را احضار کرد به دلیل اتهامات مربوط به ارتباط تهران با حمله به پایگاه  نیروی هوایی فیرفورد بریتانیا.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25572" target="_blank">📅 21:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25571">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مقام آمریکایی در گفت‌وگو با شبکه ۱۲ اسرائیل: ما به افزایش فشار ادامه می‌دهیم و معتقدیم که در نهایت، افراد منطقی‌تر در ایران دست بالا را پیدا خواهند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25571" target="_blank">📅 21:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25570">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نتانیاهو و ایسرائل کاتس، وزیر دفاع اسرائیل، امشب هشدار دادند که ایران و نیروهای وابسته به آن در تلاش‌اند با انجام عملیات تروریستی علیه اسرائیل، بر نتایج انتخابات تأثیر بگذارند. این اظهارات در پی مجموعه‌ای از هشدارها و تهدیدهای این دو مقام ارشد امنیتی مطرح شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25570" target="_blank">📅 21:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25569">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یک مقام ارشد آمریکایی مدعی شده است که دونالد ترامپ در تماس تلفنی به بنیامین نتانیاهو گفته برای اقدام علیه ایران در هر لحظه آماده باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25569" target="_blank">📅 21:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25568">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">باراک راوید ، خبرنگار ‌آکسیوس :
نخست‌وزیر نتانیاهو هفته گذشته با رئیس‌جمهور ترامپ درباره احتمال از سرگیری جنگ علیه ایران گفتگو کرد. مقامات آمریکایی به من گفتند که تحت تأثیر قرار گرفته‌اند از این که نتانیاهو تمایل داشته است قبل از انتخابات، حملات به ایران را از سر بگیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25568" target="_blank">📅 21:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25567">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آویگدور لیبرمن (رهبر حزب «اسرائیل خانه ما» و وزیر دفاع پیشین اسرائیل):
نتانیاهو پیش از انتخابات کنست به‌دنبال آغاز جنگ است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/25567" target="_blank">📅 20:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25566">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rk8BVo6hN6pfAjY3AtiygHTvUXaPaZ74ADjOFuH70_eml6XXZinDn6RfT-sjF9O0mzBmN7s9QCyMZt-r3aiu29X4ZKrbYg1VT73dmj3zMuQ0uUDCrvMcCawUpXpSeFYzdWBbXwXykRowgJkSUqHn-H5xvRjwGoVxVY0I59j8f1xgy5_xGPI4MjiQuT8YmYQadN1qhZ0JpZugluepxW5qWQ9D-AlJg3JcV3NUDlMWjrEvlOM99oCnn7NdJ2yuP3Jjv_Ji__T79YSsFmzsYaN9_AhyBqp5eUkM9cyBTPEAVsh0WYkTObwBoI5aU9HIAWcvC_vY_OVbmM5GT5yc8FUEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :
حوثی‌ها رفتار بسیار بدی دارند. فکر می‌کردم یک سال پیش، وقتی آنها را به‌شدت بمباران کردیم و به درخواست خودشان حملات را متوقف کردیم، درسشان را گرفته باشند. آنها برای مدت طولانی سکوت کرده بودند، اما حالا دوباره ظاهر شده‌اند؛ احتمالاً به دستور ایران، که کشوری در حال شکست است، نیروی دریایی ندارد، نیروی هوایی ندارد، بدترین اقتصاد جهان را دارد و نرخ تورمش ۳۰۱ درصد است. آنها به شکلی بسیار زننده به عربستان سعودی حمله می‌کنند و عمداً تلاش می‌کنند قیمت نفت را بالا ببرند؛ احتمالاً در آستانه انتخابات آمریکا
این کار پسندیده‌ای نیست.
باید کسی برای آنها توضیح دهد که من در انتخابات شرکت نمی‌کنم؛ من قبلاً با
اختلافی بسیار قاطع و گسترده
پیروز شده‌ام، اما بعد از انتخابات به سراغشان خواهم آمد و
هرگز فراموش نخواهم کرد!
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25566" target="_blank">📅 20:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25565">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b7293e68.mp4?token=fDvl7LcnIsUo2eloL4dAmXTcCytkEd5dfM0uzIxsii-RMcTU-HOy1SuilZCFHvj_kn0kdWJJz0Q6QVID3cU-Yvuq4x5R69b-Z6mQh-4a9Ue6U2or71kS57gXzdi1pR-kbFSGZwXGLgcJyc127D8P-8X871fF87W-IWbSFy1mzfUNDgUykAUAZM4iJWi5AXBRcK0cx98QHvYEDmuEym9LKNeCkiBs9eAGFvRMTVMTugRZefU6Os4JZc7uDMrI8r5aKTui-jLbfxy_n344P5Pw0grFQ3n2KJqg5K72fOqoDNggvyS5CUQ9dtLgTbhclyzQij-_JIhGqgz7hD6rBwZPtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b7293e68.mp4?token=fDvl7LcnIsUo2eloL4dAmXTcCytkEd5dfM0uzIxsii-RMcTU-HOy1SuilZCFHvj_kn0kdWJJz0Q6QVID3cU-Yvuq4x5R69b-Z6mQh-4a9Ue6U2or71kS57gXzdi1pR-kbFSGZwXGLgcJyc127D8P-8X871fF87W-IWbSFy1mzfUNDgUykAUAZM4iJWi5AXBRcK0cx98QHvYEDmuEym9LKNeCkiBs9eAGFvRMTVMTugRZefU6Os4JZc7uDMrI8r5aKTui-jLbfxy_n344P5Pw0grFQ3n2KJqg5K72fOqoDNggvyS5CUQ9dtLgTbhclyzQij-_JIhGqgz7hD6rBwZPtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی‌ رژیم سقوط کنه
🐷
💅🏻
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/25565" target="_blank">📅 20:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25564">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ee2cOZCC8mZ-5P5SXkB1cHYxQ2dgOR4mlDuWNoaovAGJY8sNPWLabuUD8LA5TB4QeA2j5PqzSORqB_c_nGnD4hA6H_GuB4HIqTO3BOUx7m02Vn-5aEZURM9Bu52ECZMLYLRX0_W5KkjEZAQ2tUxQaFoKsQ-eklNI-GlxXpAji_SQEoP8JZJxBP4EWl2FfZllqIwWVmOOgupknu9CspnPSm0QLmMOxq9jZBLz7T7uYAVmVUmd74p9ktZ9NH854fHrRTyif7ArDDOk1feZbGkJULRDPWOnjXxAt3xOBztaSm-A0ISz9_RNxf42WVptkNecOwaHOxPs5bR--t6MSUosSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ: تولد نیروی دریایی ایالات متحده را تبریک می‌گویم! اکنون ۲۵۱ سال از پیروزی‌های قدیم و جدید آن می‌گذرد.
کاری که آنها با ایجاد «
دیوار فولادی نفوذناپذیر
» (از آن با عنوان محاصره یاد می‌شود) در
تنگه هرمز
انجام داده‌اند، دستاورد
تاریخی دیگری است
؛ یکی از دستاوردهای تاریخی متعدد این نیرو.
تولدت مبارک، نیروی دریایی ایالات متحده!
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25564" target="_blank">📅 19:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25563">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb45a9bacf.mp4?token=VCiCGY0FJsp0AFcFiveYAb10I4U-8F7EGruYVSuQqdFFBGLEu8Y93ES5d20HbaDdrobQ1NzMuTzxSBXzaRryn-e9G-FsyaFhKQyTXx_rKanQmGRqj0TqzcwmI0HrTpfqczsDXyE_Y-qSuqG5yzvQCGRNnCp1VbmuP4PAsZFGlQiea-2qGHymP9fBUv1WzM5O5Zo1_XVWHpfm7Bep_aMU40X6N90hjf0koEAJJ7gHuzj715JJa7BXFgqr-lQklz0UEBE1HPUlX1kxtE4spM3XLGXemWdy6zYZxYgMBL8-BdPXdkhdD8a2NWjF165n0vwq3mJO0PO1x7VwSly2_sZ4ITzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb45a9bacf.mp4?token=VCiCGY0FJsp0AFcFiveYAb10I4U-8F7EGruYVSuQqdFFBGLEu8Y93ES5d20HbaDdrobQ1NzMuTzxSBXzaRryn-e9G-FsyaFhKQyTXx_rKanQmGRqj0TqzcwmI0HrTpfqczsDXyE_Y-qSuqG5yzvQCGRNnCp1VbmuP4PAsZFGlQiea-2qGHymP9fBUv1WzM5O5Zo1_XVWHpfm7Bep_aMU40X6N90hjf0koEAJJ7gHuzj715JJa7BXFgqr-lQklz0UEBE1HPUlX1kxtE4spM3XLGXemWdy6zYZxYgMBL8-BdPXdkhdD8a2NWjF165n0vwq3mJO0PO1x7VwSly2_sZ4ITzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:آقای رئیس جمهور ، آقای  رئیس جمهور ، آیا شما امیدوارید که ….؟
ترامپ :  این همیشه سوأل از ایران داره ، بگو …
خبرنگار : گام بعدی شما در قبال ایران چه خواهد بود؟
دونالد ترامپ:
زکی‌، نگفتم
😂
ایران کشوری شکست‌خورده است. آنها هیچ اقتصادی ندارند. نرخ تورم آنها ۳۰۰ درصد است. آنها هیچ پولی ندارند. آنها حقوق نیروهای نظامی‌شان را پرداخت نمی‌کنند. حقوق هیچ‌کس را پرداخت نمی‌کنند. ما خیلی زود درباره ایران تصمیم‌گیری خواهیم کرد. ما تنگه هرمز را در اختیار داریم و کنترل می‌کنیم و مقدار زیادی نفت از تنگه هرمز خارج می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25563" target="_blank">📅 19:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25562">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0a13f22d.mp4?token=AmaUdyP1Cu6ga6TJoGLG6ZJyiTtpnLAZjCHNFHrk5FIz5SIH0SWurGBpGv3OR6ToKAaZpKg5wyNosErtXRtl7MAidk4PgV_feGy7OLlCR236lLXWRJoqX74om7i2olWdTa9eWqKaGDI9-Cu3Aip31SQq7noO4lKA3v2NrpecfrSSyPgHTE97T9H2rE0_OiqM_TpD6SR5_9QnGaEBu2z0ydDZzshSdB4SUsKdZC0YAhLVabjzXeJmBtm0qYuVF8lPyxKlQs4XEtU6PV0BsmDf4PkzfsW7PDNpS3VCqLpYNV8q79HH7QdVbAeH5MMsxXD-PaU3pLfxrXf4kWrB0AFLWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0a13f22d.mp4?token=AmaUdyP1Cu6ga6TJoGLG6ZJyiTtpnLAZjCHNFHrk5FIz5SIH0SWurGBpGv3OR6ToKAaZpKg5wyNosErtXRtl7MAidk4PgV_feGy7OLlCR236lLXWRJoqX74om7i2olWdTa9eWqKaGDI9-Cu3Aip31SQq7noO4lKA3v2NrpecfrSSyPgHTE97T9H2rE0_OiqM_TpD6SR5_9QnGaEBu2z0ydDZzshSdB4SUsKdZC0YAhLVabjzXeJmBtm0qYuVF8lPyxKlQs4XEtU6PV0BsmDf4PkzfsW7PDNpS3VCqLpYNV8q79HH7QdVbAeH5MMsxXD-PaU3pLfxrXf4kWrB0AFLWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
حملات جنگنده های عربستانی به مخازن نفت صنعا در یمن
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25562" target="_blank">📅 19:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25561">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ درباره ایران: خیلی زود در مورد ایران تصمیم خواهیم گرفت.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/25561" target="_blank">📅 19:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25560">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دادستان کرمانشاه: در بازرسی از یک تریلی در مرز پرویزخان، ۹۹ سلاح کمری، ۱۰ کلاشینکف، ۱۷۰۰ فشنگ و ۱۹۸ خشاب کمری کشف شد که در بخش‌های مختلف خودرو جاسازی شده بودند. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/25560" target="_blank">📅 19:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25559">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d491aff496.mp4?token=qbyZwMDPFel3QBFsi4TsOqJJuiBhAMHs_Ren8bwexL2mohg8UGQl8ef8BDsnEgZKgXBXKZZoweDsCwv7KBNchUE_RKe2aA2qj7yFrtYx_Dv6I3WNkY8vrRVRRjEdLeTKIKAJPFm5Wte-pX5hBGXiEkW2xDXisM6zRO0MFFhJJHYV47cPzv0Mji7YjeitBhaBm3Fai-f_5krpD_5JJwWN3-yo_cS3nyPE1atOYxJlmWQSUZQz_GrzGteTZ6U1Z8hlr2ceOQNvSZzaUEFcU3CGpIAC9r_Ktc8Q6KBWEy8TnjSelsRtCSyc9uTKeQr3HPXudJIrOwdqqCEMSPJ16qf-rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d491aff496.mp4?token=qbyZwMDPFel3QBFsi4TsOqJJuiBhAMHs_Ren8bwexL2mohg8UGQl8ef8BDsnEgZKgXBXKZZoweDsCwv7KBNchUE_RKe2aA2qj7yFrtYx_Dv6I3WNkY8vrRVRRjEdLeTKIKAJPFm5Wte-pX5hBGXiEkW2xDXisM6zRO0MFFhJJHYV47cPzv0Mji7YjeitBhaBm3Fai-f_5krpD_5JJwWN3-yo_cS3nyPE1atOYxJlmWQSUZQz_GrzGteTZ6U1Z8hlr2ceOQNvSZzaUEFcU3CGpIAC9r_Ktc8Q6KBWEy8TnjSelsRtCSyc9uTKeQr3HPXudJIrOwdqqCEMSPJ16qf-rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادستان کرمانشاه: در بازرسی از یک تریلی در مرز پرویزخان، ۹۹ سلاح کمری، ۱۰ کلاشینکف، ۱۷۰۰ فشنگ و ۱۹۸ خشاب کمری کشف شد که در بخش‌های مختلف خودرو جاسازی شده بودند.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25559" target="_blank">📅 18:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25558">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تداوم درگیری‌ها در استان سیستان‌و بلوچستان؛ منابع از «انفجار مهیب» و «تلفات سنگین» خبر می‌دهند
رسانه های محلی استان سیستان‌و بلوچستان امروز اعلام کردند در ادامه درگیری‌ها میان نیروهای حکومتی و افراد مسلح، مناطق «پیرسوران» در بخش کورین زاهدان و ارتفاعات «چاه‌احمد» شهرستان تفتان صحنه برخوردهایی سنگین بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25558" target="_blank">📅 18:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25557">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فارس گزارش داد بانک مرکزی محدودیت‌های بانکی و برداشت ریالی سه صرافی رمزارزی نوبیتکس، بیت‌پین و ارزینجا را پس از انجام اصلاحات موردنظر و رفع تخلفات اعلام‌شده لغو کرده است. این محدودیت‌ها روز دوشنبه ۲۰ مهر برای پنج پلتفرم رمزارزی اعمال شده بود؛ طبق گزارش‌های منتشرشده، محدودیت دو پلتفرم دیگر همچنان برقرار است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25557" target="_blank">📅 18:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25556">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xrswoa-NUMe_nQZLmczZqpThEJIXjHj79MIwGaHk0Wsy-OV6Ylf-S62YdraHgX16FaQYu_gSQ8V3ufrJZxx1F0eg-HHG0ROr3DTPNMk6v8tnUlSguaI5BffPItTnyeLjHGFQCiKVqHiMxUxvooEY65O9sXcOIsgqzRkhIH0yhQxOuqsBfZ4Wsdn_dphPrLqTMoKr16SPakgEu1ghj5XVtHrIlwRHRyICapt1w1vO3KP27yLfpWPLLFbqurMBUpBzhaEozmqWGvwLR3VkvxfyChISiKIO4Zin9DtyScNzDuL2KsGZBe3oi3XhL6BKJd5blrOYGXlmWuFn35rCliqgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه گاردین:
دست‌کم هفت کابل مهم داده و اینترنت زیردریایی از تنگه هرمز عبور می‌کنن
یکی از مهم‌ترین آن‌ها کابل AAE-1 است؛ سامانه‌ای حدود 25 هزار کیلومتری که جنوب‌شرق آسیا را از مسیر خاورمیانه و آفریقا به اروپا متصل میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/25556" target="_blank">📅 18:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25555">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fd8bd8128.mp4?token=gEoi8kqBNkNFy_ZXAblJFFzn2DqUlDvN0Dye9hNE-5NYTfzLYpgRAl1j8GbdL9on23FNItBE6GlhnOTjg2EcuKiCrA7L6nyiOOIPR-QhgjabdcvvL8cL8cKA7q68jGJj8uI1ZH1L4JYshphNxupyAp-Y5VGeRxo9FlJnOsovfEPyHCeyom7_w29fW_4AMGIeBnUEH3D4f6MsvaKTT75TOMF00OINxVJHdRf9-t_Jiq5Gc2575yf4gJyASNJD5WwfwVq7x4S3htC8ZAXVYqkGi-oBGizqNktooONOzplvIKtjMgVqmfXemd6DCsg4_6BRLMdA_b6uOq3MfI7orLidZLISdcnkEFLW4xv-Sqb2iDJS2su8QZnhqykk707FargoY4am5-sQ43doelspc76mo-uCYDxgJQLi1LZG-EB-qc-UWNm-4Wtu52ytBK-hIyA79mgrdUV3k0iX2tdT4T0yggBGUGC3TWBTLt23paYwFp6c8ijPBQ9VmpmA3b2mfheXNBnNc1y4I-QXT_fPWDuMxeGXigJ_SwY73eP9Vdq_usvIKeT2WmMqa8lZswBe2MhgQdonsFYw4gv2pPx25i-u4FP2JhVQo3r3h2wQ5ZE6FF2b-ib1AA_rOG1Tonx5m90gy6nP8Zoqp6MVBwLFbybYblqwpZdVLViKXGyzCsZRdG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fd8bd8128.mp4?token=gEoi8kqBNkNFy_ZXAblJFFzn2DqUlDvN0Dye9hNE-5NYTfzLYpgRAl1j8GbdL9on23FNItBE6GlhnOTjg2EcuKiCrA7L6nyiOOIPR-QhgjabdcvvL8cL8cKA7q68jGJj8uI1ZH1L4JYshphNxupyAp-Y5VGeRxo9FlJnOsovfEPyHCeyom7_w29fW_4AMGIeBnUEH3D4f6MsvaKTT75TOMF00OINxVJHdRf9-t_Jiq5Gc2575yf4gJyASNJD5WwfwVq7x4S3htC8ZAXVYqkGi-oBGizqNktooONOzplvIKtjMgVqmfXemd6DCsg4_6BRLMdA_b6uOq3MfI7orLidZLISdcnkEFLW4xv-Sqb2iDJS2su8QZnhqykk707FargoY4am5-sQ43doelspc76mo-uCYDxgJQLi1LZG-EB-qc-UWNm-4Wtu52ytBK-hIyA79mgrdUV3k0iX2tdT4T0yggBGUGC3TWBTLt23paYwFp6c8ijPBQ9VmpmA3b2mfheXNBnNc1y4I-QXT_fPWDuMxeGXigJ_SwY73eP9Vdq_usvIKeT2WmMqa8lZswBe2MhgQdonsFYw4gv2pPx25i-u4FP2JhVQo3r3h2wQ5ZE6FF2b-ib1AA_rOG1Tonx5m90gy6nP8Zoqp6MVBwLFbybYblqwpZdVLViKXGyzCsZRdG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی ارتش
تصاویری از یک تانکر نفتی در حال سوختن در تنگه هرمز شرقی منتشر کرد و اعلام نمود که نیروهای جدیدی را در دریای عرب، خلیج عمان و تنگه هرمز شرقی مستقر کرده است تا از تردد کشتی‌ها نظارت به عمل آورد.
@WarRoom</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/25555" target="_blank">📅 18:05 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25554">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6cda2498.mp4?token=KpRuokrZuOKaHq9ToR3sdBTC8emO5MnHdo20HauKgHnBAkUd0I6wkS_fOeWkC2LKYe_sKfNKya4qkHRGVxpksqpzQIUEzvAyeJ2j3UIFZTz1vgTC7Lf12S8BYqXE2ZfCDjMeCf6eKTLRvx2QLJFyrEEsNxM5SNEwHSihJVAHR3PUg0_yygMnCmZFW6Mo1ASkpP0ROAXMeaW7J568ALZSfnwRWxUzGzQ29gUyxzSaibpHe577v7YcZk8d_VXO6mxGaKhQl3DUJag9gsnHIt27CFz4_1nmXohYoUPr34UuAJgkS9pAFpsGC2BLtSDjpjkfd9HBBunA2XS8NccySvlUvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6cda2498.mp4?token=KpRuokrZuOKaHq9ToR3sdBTC8emO5MnHdo20HauKgHnBAkUd0I6wkS_fOeWkC2LKYe_sKfNKya4qkHRGVxpksqpzQIUEzvAyeJ2j3UIFZTz1vgTC7Lf12S8BYqXE2ZfCDjMeCf6eKTLRvx2QLJFyrEEsNxM5SNEwHSihJVAHR3PUg0_yygMnCmZFW6Mo1ASkpP0ROAXMeaW7J568ALZSfnwRWxUzGzQ29gUyxzSaibpHe577v7YcZk8d_VXO6mxGaKhQl3DUJag9gsnHIt27CFz4_1nmXohYoUPr34UuAJgkS9pAFpsGC2BLtSDjpjkfd9HBBunA2XS8NccySvlUvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کتی زاخاریا، سخنگوی جدید کاخ سفید:
دونالد ترامپ در حال عمل به تمام وعده‌های خود است.
دونالد ترامپ دوستانه‌ترین رئیس‌جمهور برای خانواده‌ها در تاریخ ماست.
@WarRoom</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/25554" target="_blank">📅 18:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25553">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvwFHk1VrcmDPPtX3AYJdJSzzpgpQ-B7q05fU5Naz6tp1KkP1LfnjJ2aaZj6WIMMMg09wT9uiP5oiEiZVrHsAcBFvJT4EVEI9EhqP_qp0C-OQgHHyJGVXVA_d7rJ7XfsBFcSMknbHkoK8gFmms-Yo8tzB_93dDW3ctGhmv6G3i_LjCjbycDSqmzI9AdQt_B9lWWS5Y_FCMoWXvNpLCpGNzuY3UqvcHbodMurvTpwF90ln6qNtZcR04VPRmMqPPQgTe5UVj8aBjTBmmxwxPcbmgImaThIcMj5PdBqbyBqVVBz7uQiibfqMUmvm1hnTaF6f9_yUEhwoo9OKYmCdL0omg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاطی سخنگوی دولت: دولت قطر در مورد خلبانان ایرانی قول مساعد داده.
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/25553" target="_blank">📅 17:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25552">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گزارش‌ها حاکی است که هم‌زمان با حملات هوایی در صنعا، جنگنده‌های نیروی هوایی عربستان سعودی مناطقی در استان حدیده در غرب یمن، تحت کنترل حوثی‌ها، را نیز هدف قرار دادند. در این حملات، چندین حمله هوایی بندر نفتی رأس عیسی و تأسیسات نفتی آن را هدف گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/25552" target="_blank">📅 17:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25551">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">عربستان تأسیسات شرکت نفت در غرب صنعا را بمباران کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/25551" target="_blank">📅 17:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25550">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آکسیوس :
صندوق بین‌المللی پول هشدار داد اقتصاد جهان به محدودیت تاب‌آوری در برابر شوک‌های جدید نزدیک می‌شود.
جنگ خاورمیانه، کاهش ذخایر انرژی، بدهی دولت‌ها و وابستگی بازارها به رونق هوش مصنوعی از عوامل اصلی نگرانی هستند. طبق سناریوی صندوق، اگر سرمایه‌گذاری هوش مصنوعی سقوط کند و دستاوردهای بهره‌وری محقق نشوند، تولید ناخالص داخلی جهان ممکن است تا سال ۲۰۲۸ حدود ۱٫۱ درصد پایین‌تر از پیش‌بینی پایه قرار گیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/25550" target="_blank">📅 17:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25549">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حمله افراد مسلح به پاسگاه مورتان در بخش پارود شهرستان راسک و درگیری شدید با نیروهای مستقر در پاسگاه گزارش شده است. بر اساس اطلاعات اولیه، درگیری از دقایقی پیش آغاز شده و دو طرف به تبادل آتش پرداخته‌اند؛ تاکنون جزئیاتی درباره تلفات احتمالی یا وضعیت نیروهای…</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/25549" target="_blank">📅 16:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25548">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رئیس ام‌آی۵ بریتانیا هشدار داد فعالیت‌های ایران و روسیه برای تهدید اهداف حساس در بریتانیا افزایش یافته است. او گفت تلاش‌های منتسب به ایران بیش از گذشته بر اهداف سخت‌تر، از جمله مراکز نظامی، متمرکز شده‌اند. تحقیقات درباره ماجرای پایگاه فرفورد ادامه دارد و رئیس ام‌آی۵ از اظهارنظر درباره جزئیات پرونده خودداری کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25548" target="_blank">📅 16:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25547">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">محمد البخیتی، از اعضای دفتر سیاسی حوثی‌ها، هشدار داد اگر آمریکا مستقیماً وارد عملیات نظامی عربستان علیه این گروه شود، واشنگتن و منافع آمریکا در منطقه با پاسخ سریع و شدید روبه‌رو خواهند شد. او همچنین به کارکنان تأسیسات نفتی و فرودگاه‌های عربستان هشدار داد که از این مراکز فاصله بگیرند
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25547" target="_blank">📅 16:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25546">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1032f22b5.mp4?token=Dzon2oLw_l2Y0O6iuxv-jtSJE_HlX19tJVLqRtHpOxVyoVs3xcoO4ilvF34cDPIMcan-CcIu9cBW-rABlgaLd81EQ78GbNHzZyv-lKgbrzxmgcFgp_mtnwGBt-m9-D4vfXeq5srmzf0oa4-GX6adwIqcCO9_4YfUHEwQMDJ7KNkxCIGYyi6Vs9M1bALSYa1rMZWQlJLzQWTCG_UJ7RpkpMFSVao9trCgmB30uFFWzGkV1IzUWZJAdoEoBosIGCNJ6BSyL5wvbfWVjaXHmVlkhsKMjRavaJMdB5fQC140scl2IcPc3aFqX7vjlUaCZ6OqIzgbckRRs9XdCSqq-BcPWH9jP26UTfqPSTTX5dc-i1Z_diCoQnsnh1zAlYd6GNFA7F2Z5lWxm567g6Ij_2-9EsoakGEURLqiRJTtscwk1uDehnouOybRNImBnHnfiBhMsrcsOQuuC2yl1igxbe4kbDUEQ4csWB7JNORyMop0tqMVo0-It8xJCBcjDiag4rzDDJjACitkyQN8o6bDzNsXI969SQ9W5XFQw_5FmzImXkAPyJt5OaZG_ZIHKtyFnAYbtpMtwyH5JxS4lDwyvgMJIf8kZjDnaMkGn3xo_73ODnXASoumvMxr7noMQIp_ZrMhrCLLkICD6gq0QjH0e5T6DKFc7pgAh_egyu7GSi5rEN4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1032f22b5.mp4?token=Dzon2oLw_l2Y0O6iuxv-jtSJE_HlX19tJVLqRtHpOxVyoVs3xcoO4ilvF34cDPIMcan-CcIu9cBW-rABlgaLd81EQ78GbNHzZyv-lKgbrzxmgcFgp_mtnwGBt-m9-D4vfXeq5srmzf0oa4-GX6adwIqcCO9_4YfUHEwQMDJ7KNkxCIGYyi6Vs9M1bALSYa1rMZWQlJLzQWTCG_UJ7RpkpMFSVao9trCgmB30uFFWzGkV1IzUWZJAdoEoBosIGCNJ6BSyL5wvbfWVjaXHmVlkhsKMjRavaJMdB5fQC140scl2IcPc3aFqX7vjlUaCZ6OqIzgbckRRs9XdCSqq-BcPWH9jP26UTfqPSTTX5dc-i1Z_diCoQnsnh1zAlYd6GNFA7F2Z5lWxm567g6Ij_2-9EsoakGEURLqiRJTtscwk1uDehnouOybRNImBnHnfiBhMsrcsOQuuC2yl1igxbe4kbDUEQ4csWB7JNORyMop0tqMVo0-It8xJCBcjDiag4rzDDJjACitkyQN8o6bDzNsXI969SQ9W5XFQw_5FmzImXkAPyJt5OaZG_ZIHKtyFnAYbtpMtwyH5JxS4lDwyvgMJIf8kZjDnaMkGn3xo_73ODnXASoumvMxr7noMQIp_ZrMhrCLLkICD6gq0QjH0e5T6DKFc7pgAh_egyu7GSi5rEN4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس هلال احمر : برای هر سناریو از جمله حملات هسته‌ای و شیمیایی آماده‌ایم!
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25546" target="_blank">📅 15:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25545">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نائب رئیس کمیسیون آموزش مجلس:
هنوز علت مسمومیت ۶۰ دانشجوی دانشگاه بوعلی همدان مشخص نشده
پس از دریافت نتایج آزمایش آب و غذا، می‌توان اظهار نظر کرد
شرایط در خوابگاه‌های مختلف یکسان نبوده؛ حتی در برخی خوابگاه‌ها افرادی که غذا مصرف نکرده بودند نیز دچار مسمومیت شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25545" target="_blank">📅 15:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25544">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رضا سپه‌وند، سخنگوی کمیسیون انرژی مجلس:  آمریکا رمزارزهای متعلق به اشخاص، نهادها و دولت ایران را در چند مورد هک یا توقیف کرده و بخشی از آن‌ها را برداشت کرده است. او توقیف این دارایی‌ها را «دزدی» توصیف کرد و گفت نام شبکه‌های واسطه‌ای دور زدن تحریم‌ها نباید افشا شود.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/25544" target="_blank">📅 15:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25543">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رسانه‌های کره جنوبی گزارش داده‌اند آمریکا، کره جنوبی و ژاپن رزمایش نظامی مشترک پنج‌روزه‌ای را برای تقویت هماهنگی عملیاتی و پاسخ مشترک در حوزه‌های مختلف  از دیروز آغاز کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25543" target="_blank">📅 14:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25542">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ایلان ماسک هشدار داد که فشار شدید در فرایند آموزش هوش مصنوعی ممکن است پیامدهای پیش‌بینی‌نشده‌ای داشته باشد. او با اشاره به ردپاهای استدلال مدل‌های گروک در مرحله یادگیری تقویتی گفت برخی از آن‌ها شبیه وضعیت فردی زیر شکنجه به نظر می‌رسند و افزود: «شکنجه یک ابرهوش احتمالاً ایده خوبی نیست؛ ممکن است بخواهد انتقام بگیرد.» این اظهارات در پی تصمیم آنتروپیک برای ممنوع‌کردن آزار مکرر و بی‌دلیل مدل کلود مطرح شد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25542" target="_blank">📅 13:46 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25541">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3oexgx9x5wnNyWA9xEQsVxW_AQBmbmJbU4n_Q_y2__R-n9nXTpHYGEuSh4pxIzdzQGWMS8WUp7tCFB0cJUrm402FHHFWLCVR0PmkCN_pQgco0q762eHyyS3poNX0h95N-pWZ4zHYkFQBOOZZuE957GwB0BkhjxeXYnU-4flZJc3rCDt0grH24eSCBQWKURpEVtX0gQS7WDldBLosGHRqHYhmItgTR-NHPEkd1JPKWnPRwaUiKrlXmnrOnX0b3zF5zA5nHCbCNMpFzTdudGUNBLz1aK_UvkOaWGu7oGaCOC4AuPY49-bTSChXSYJmrcsU-sbzpkthw_0_O86cNN-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای جاسوسی مخوف U-2S با شناسه «ZMBEFLT» و شماره سریال 80-1099(کد فرستنده AE096B)هم‌اکنون پس از برخاستن از پایگاه RAF فیرفورد (EGVA)،
در حال اوج‌گیری و حرکت به سمت شمال است. این هواپیما آخرین فروند از مدل U-2S است که تاکنون ساخته شده و در سال جاری، تنها یک بار پیش از این  ردیابی شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25541" target="_blank">📅 13:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25540">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آسوشیتدپرس : لبنان درباره محموله بزرگ مواد منفجره تحقیق می‌کند:
مقام‌های لبنانی هفته جاری از توقیف کامیونی حامل حدود ۷۸۰ کیلوگرم مواد منفجره، از جمله تی‌ان‌تی و سی‌۴، خبر داده‌اند. احتمال ارتباط محموله با حزب‌الله و ایران مطرح شده
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/25540" target="_blank">📅 13:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25539">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کی‌یف ایندیپندنت :
ستاد کل ارتش اوکراین مدعی شد روسیه از آغاز تهاجم تمام‌عیار در فوریه ۲۰۲۲ تاکنون حدود
یک میلیون و ۵۵۵ هزار و ۷۰۰
نیروی نظامی را از دست داده است؛ این رقم برآورد طرف اوکراینی است و مستقلاً تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/25539" target="_blank">📅 13:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25537">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZaUTAen2mOkJXpwYiatvMMVc84bjtITzCEQIrkBPudUqx29xzGZOqNeiBQakfsybdUf1tc3z_VSVRSZjDzwqhAABcx2SsR6KmI6iC78RSZaX6D0DsojBpHb0AfVNMyPtESkktlEchRDqMZAfrkWiL-s6XUur_ICmHTwwUrq5JairjmU1V8rB4FzYQbh5Ke-s9Obl7taPC4_5TcYlwYRnHEZJnEoiAsJavNuGg8UHURzaLK48DXuZDK8c8cRc-rS_cIdIuO58utDOH-yBxngcl_-bHXaDeHBTygxB2j9eTfZSc-4lxM1K-toig7Qz_JrQYHwz-kcWohQoGg0DjPCB2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOvejZkZJsF8lP0-T7oy2kyFuxW6y67lhckL1wobBde1c0zYpd3u29yaB4CTqEFue93Uiy4G9xz1XaXKP8mPmHcRUQDUNIySb84TWrdAimu6lm_PBsEDa6GkB0_cvjc1LOSQX6vNGyDmqYF0PQdYsrug9Y5HXquHth59rEzkvkkmmLxl8-2Xk2WI8xS5RzeTvqYuMhVX5FyjkMWM9V3NasU2x2OO8xBs_zRz_EZ-SRm8rNtCjvUVIg7FyDv43PPHCMMc8nzX1aCS0_98NnHyRVLaWfsGsN_jg8ARv1cBtUpYEagZpY5BsqMvdaKxi6xmHkG5iwQNNKRH2mZ1R8noBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تمرین پرتاب آبگرمکن از اطراف : سمنان ، یزد و اصفهان
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/25537" target="_blank">📅 12:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25536">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INAznlwlPFeXvmRsGU_dXHzKUJ-lQqlmrn0PPjZJe1VqOr-QCfX5m8r_VA6dUKjYvlsviOLZUzjM6UbiwXXIL_GzaWfHGJR76iFDDl_6t93cfI1y8MOUMf3gjTYzKaoclr7r2cdgNwTfBAFruAJlCAZV7FJvak9Ymqs5_oLuRyJT0y97rT0dPcTgZipM6_L8XdnDGtUsx3FMo6kM-OVAjLdAXU3U23u8BMGCPN4QV1He8_nTSQhrl35KLTy1W8QK72qfDqDdyzGpBFaW0jJOeZn8QnwlbazqMMBeJ5599B6M3AxtmCgLhGnxC0GrTOz_Q1n1_ZJZ63a8QZ3z8HSm-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طول 6 روز (از 5 تا 11 اکتبر)، اعلام شد که 14 کشتی در تنگه هرمز مورد هدف قرار گرفته‌اند. این بالاترین تعداد کشتی‌هایی است که در کوتاه‌ترین بازه زمانی از ماه آگوست به بعد، مورد هدف قرار گرفته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25536" target="_blank">📅 12:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25535">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نرخ ارز، طلا و سکه | سه‌شنبه ۲۱ مهر ۱۴۰۵، ساعت ۱۲ ظهر تهران
دلار: ۲۵۹,۹۰۰ تومان | تتر: ۲۵۶,۵۳۲ تومان | یورو: ۲۹۰,۸۸۰ تومان | پوند: ۳۴۳,۳۵۰ تومان | درهم: ۷۰,۸۲۱ تومان | انس جهانی طلا: ۴,۱۸۹ دلار | طلای ۱۸ عیار: ۲۵,۸۳۸,۴۰۰ تومان | مثقال طلا: ۱۱۱,۵۱۸,۰۰۰ تومان | سکه امامی: ۲۶۲,۰۴۰,۰۰۰ تومان | نیم‌سکه: ۱۳۹,۱۳۰,۰۰۰ تومان | ربع‌سکه: ۷۳,۵۲۰,۰۰۰ تومان | سکه گرمی: ۳۶,۰۰۰,۰۰۰ تومان
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25535" target="_blank">📅 12:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25534">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تمیم بن حمد آل‌ثانی، امیر قطر، در سخنرانی خود در پارلمان این کشور اعلام کرد جمهوری اسلامی به‌طور آشکار حاکمیت قطر را نقض کرده است. او تأکید کرد که پایبندی دوحه به گفت‌وگو و راه‌حل‌های مسالمت‌آمیز به معنای کوتاه‌آمدن در دفاع از کشور نیست و امنیت و حاکمیت کشورهای عضو شورای همکاری خلیج فارس قابل مذاکره نیست.
امیر قطر همچنین گفت بسته‌شدن تنگه هرمز و خسارت‌های واردشده به تأسیسات گاز طبیعی مایع (LNG) در راس لفان، صادرات قطر را به‌شدت مختل کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/25534" target="_blank">📅 12:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25533">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از افراد مطلع گزارش داد که ایران به کشورهای عربی منطقه هشدار داده است در صورت آغاز جنگی تازه، احتمال گسترش عملیات نظامی به خاک کشورهای همسایه و حمله به تأسیسات نفتی عربستان سعودی وجود دارد. بر اساس این گزارش، تهران همچنین تهدید کرده…</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/25533" target="_blank">📅 11:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25532">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از افراد مطلع گزارش داد که ایران به کشورهای عربی منطقه هشدار داده است در صورت آغاز جنگی تازه، احتمال گسترش عملیات نظامی به خاک کشورهای همسایه و حمله به تأسیسات نفتی عربستان سعودی وجود دارد. بر اساس این گزارش، تهران همچنین تهدید کرده است حملات علیه نیروهای آمریکایی را تشدید کند و شناورهای نیروی دریایی آمریکا را هدف قرار دهد؛ از جمله با هدف غرق‌کردن آن‌ها و کشتن ملوانان. این گزارش درباره تهدیدها و سناریوهای احتمالی ایران است و به معنای تأیید اجرای عملیات زمینی نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/25532" target="_blank">📅 11:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25531">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گزارش‌ها از آغاز درگیری سنگین میان نیروهای نظامی جمهوری اسلامی و افراد مسلح در ارتفاعات منطقه چاه‌احمد شهرستان تفتان، در محدوده کوه لوپ و ارزن‌تاک، از ساعت ۶ صبح امروز حکایت دارند. گفته می‌شود در این درگیری از سلاح‌های سبک، نیمه‌سنگین و سنگین استفاده شده و نیروهای کمکی نیز به منطقه اعزام شده‌اند. تاکنون جزئیات مستقلی درباره تلفات احتمالی منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25531" target="_blank">📅 11:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25530">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyeJxICS3YkJV4tb00-BLdwhVIV5R7FcuT9gqY7tW8KJuxvc4Krh0bHpTU1mVUJTmGj9MwdL1lstIHmM8ErAWejGD1G1y63scL38PNaocI6kexQOfGAr1X5HWNF6j-mDubn_TksT-NZRIQkdCjErW1SCyFgmKAlylZwhc6VAf_GkQOyd_8kN65gHiGzwKbDgzdxvBXLcsuEqsVw0ZaaqoZpV_aBJNLoilTauPkNyFtgyhc7kBwo7-sxf2iOVIk3uqTy3VKG6Te7xU2sqalvWyrBObrQkuq50xQdmofSxz0AOQzxcAvdio1xL14quN2HX_IA6SSoWLUB6p9hPQjH7rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث : می‌بینم چپ‌گرایان افراطی ادعا می‌کنند چین و روسیه به جمهوری اسلامی ایران کمک می‌کنند. اگر چنین کمکی وجود داشته باشد، بسیار محدود است؛ اما من اصلاً باور ندارم که آن‌ها به ایران کمک می‌کنند. چین و روسیه چیزهای زیادی برای از دست دادن دارند و اگر چنین کاری انجام دهند، ما خیلی سریع از آن مطلع خواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/25530" target="_blank">📅 11:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25529">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c4df0d1ee.mp4?token=e5mtgncAXfEdLqF5Sf8LT-AXBHKW9mYCrBRK1u7amB5e9yk8nha_sevKddLY4N7uxC-n6oCf_TNN0Yuf7-jTifsOBOgAPdeawnpg0zMIdBXNhH4wlQUQO_8pvFPehmgCBf1Pl19jSIzOA_M2o4M2JvUsd2nByoDxNyyE8aR4hq-usoPpuGFb-yh8niQscReE1bAGu3c3VajaHr2NKq-K-homkJBAlCWlseLFUSE-O5zBm2azzj2rBVO8rUgKGc3nrpOOIPcwimzYjfsWWN0ue0PuXFFXI-zxiQtBhm_ikAiIHGMEHTmgKzcZtCbCZYvrgrGlmfE_wx1BYwO-LOJ6bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c4df0d1ee.mp4?token=e5mtgncAXfEdLqF5Sf8LT-AXBHKW9mYCrBRK1u7amB5e9yk8nha_sevKddLY4N7uxC-n6oCf_TNN0Yuf7-jTifsOBOgAPdeawnpg0zMIdBXNhH4wlQUQO_8pvFPehmgCBf1Pl19jSIzOA_M2o4M2JvUsd2nByoDxNyyE8aR4hq-usoPpuGFb-yh8niQscReE1bAGu3c3VajaHr2NKq-K-homkJBAlCWlseLFUSE-O5zBm2azzj2rBVO8rUgKGc3nrpOOIPcwimzYjfsWWN0ue0PuXFFXI-zxiQtBhm_ikAiIHGMEHTmgKzcZtCbCZYvrgrGlmfE_wx1BYwO-LOJ6bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره جمهوری اسلامی:
«شاید در برخورد با رهبران بیش از حد پیش رفته باشیم، چون دیگر نمی‌دانیم دقیقاً با چه کسانی طرف هستیم.
راستش را بخواهید، برایمان دشوار شده که بفهمیم باید با چه کسی مذاکره کنیم. فکر می‌کنم زیاده‌روی کردیم.
می‌توانستیم در سطح یک متوقف شویم. رفتن به سطح دو و دو و نیم احتمالاً زیاده‌روی بود.»
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/25529" target="_blank">📅 11:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25528">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کانال ۱۲ اسرائیل: پس از دریافت تهدید ناشناس درباره وجود بمب در هواپیمای شرکت دلتا که از نیویورک در فرودگاه بن‌گوریون فرود آمد، مسافران به‌سرعت تخلیه و هواپیما به محل دورافتاده‌ای منتقل شد. نیروهای امنیتی هواپیما را بازرسی کردند؛ اما گزارشی از کشف بمب منتشر نشد و احتمال کاذب‌بودن تهدید مطرح شد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/25528" target="_blank">📅 11:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25526">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f888102f5.mp4?token=ao7vZ3foHZRq-Bnd9J7T4We8jgydMmXZPULr9lv3-xQP1ljF8BhbAGUGVFuq_JfishpMKunyIbnJ2uUx97DWKsXO-pa0HsuyvT9nLUaRSLM1pjv3ul1yrvS99bvDPCGkGTbumviQxhwQ7T4g6l9KQMEN-zRJwW-SMq0uZEDXh674zdqC8IZsdDcj6kOmeWkFrYtini3yrWpn5zQskJMeIVzyx6QfoNotLGlktO7gYkVB_BqFPuouhfgv39wD8WYv25o3Bfk4gMYfIU442MF_6YoP81gkBbRodILicsUqUxkJ25p5bTffSIOxjE42Osipspo-2-Lz3yx60uADHFh2DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f888102f5.mp4?token=ao7vZ3foHZRq-Bnd9J7T4We8jgydMmXZPULr9lv3-xQP1ljF8BhbAGUGVFuq_JfishpMKunyIbnJ2uUx97DWKsXO-pa0HsuyvT9nLUaRSLM1pjv3ul1yrvS99bvDPCGkGTbumviQxhwQ7T4g6l9KQMEN-zRJwW-SMq0uZEDXh674zdqC8IZsdDcj6kOmeWkFrYtini3yrWpn5zQskJMeIVzyx6QfoNotLGlktO7gYkVB_BqFPuouhfgv39wD8WYv25o3Bfk4gMYfIU442MF_6YoP81gkBbRodILicsUqUxkJ25p5bTffSIOxjE42Osipspo-2-Lz3yx60uADHFh2DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: شعار موردعلاقه‌ام«گی‌ها حامی فلسطین هستند!» می‌دانید اگر گی باشید، آنجا چه بلایی سرتان می‌آورند؟ شما را از بالای ساختمان به پایین پرت می‌کنند. شما را به بالای بلندترین ساختمانی که دارند می‌برند ــ البته ساختمان چندان بلندی هم نیست ــ و از آنجا به پایین پرتتان می‌کنند. بااین‌حال، مدام می‌بینم گی‌ها از فلسطین حمایت می‌کنند!»
او در ادامه با لحنی کنایه‌آمیز پرسید: «زنان حامی فلسطین چه بلایی سرشان می‌آید؟»
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25526" target="_blank">📅 09:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25525">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏شبکه دویچه‌وله آلمان بعد از ماه ها راستی آزمایی مستندی را از مصاحبه با برخی ماموران جدا شده از جمهوری اسلامی منتشر کرد.  مصاحبه‌شوندگان در این مستند تاکید کردند که جمهوری اسلامی برای نجات خود از سقوط، به هر ابزاری متوسل می‌شود.
@WarRoom
یاشار : فردا براتون قرار میدم</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/25525" target="_blank">📅 03:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25524">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/819b1a2d7e.mp4?token=GL1xOkNbqm16mAsjhtvkEylcKubQO4rjmbB4e3GXIX0cYXsE3EngO-_9ZKLqNqHkh2PFjGxEXpI_UnlF-rLL0vqmDFMpp0eaKaXK07ZjnfWVdeg4ph4l-WwYEuek74ezmECmGUNorRmxJLb3-RIOeYVB8yzXFV6zn-3Bm2J0NOVeKvEW4oIcKVUEYAAYXZPg6Z1IICiAa9FHl1wHp8_2Bt5gogFzmv-RFGR88Zu-UTwRnxUGORgsRgjeTndFnsdW8U0-2SIIvQQnXl1-r0UF3KKUt8cIIcE5YPxMEwGukirII3K9YOvNZQ5MqQnQ2GnJaTywZMm6EHsLiIa77YSSx5Y_--kJaNWt5QA0DALrZD_HJ4wHfYOjCryXI9Qs5QPAr4t8PnmVni8u8Y03vkxpZeZ7XAAfqI4E-1GVu9OTq2Fnkz2LaQ3Us-bdsE2aALX5cfFhxVWkks4_0VcbMzKxaStDotXtgs6zwcRuy55KaGex927nlsS42477c9oEzdl0ciJo2h6yJL0dQVuxcJvarWtIkovXy504kHC4-yZbVinkei3vSrlCS9QRkKG9L_Ub0n-9qXxpQE8n_rEATGG5o7d1dkgfNwPX3XEhCJd16utTGJXXKuH2K4oefI6NkrAuIphPVAIbWeqmcdr_FnzdrQ2TpTkkDSiBJacTEAMoJ4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/819b1a2d7e.mp4?token=GL1xOkNbqm16mAsjhtvkEylcKubQO4rjmbB4e3GXIX0cYXsE3EngO-_9ZKLqNqHkh2PFjGxEXpI_UnlF-rLL0vqmDFMpp0eaKaXK07ZjnfWVdeg4ph4l-WwYEuek74ezmECmGUNorRmxJLb3-RIOeYVB8yzXFV6zn-3Bm2J0NOVeKvEW4oIcKVUEYAAYXZPg6Z1IICiAa9FHl1wHp8_2Bt5gogFzmv-RFGR88Zu-UTwRnxUGORgsRgjeTndFnsdW8U0-2SIIvQQnXl1-r0UF3KKUt8cIIcE5YPxMEwGukirII3K9YOvNZQ5MqQnQ2GnJaTywZMm6EHsLiIa77YSSx5Y_--kJaNWt5QA0DALrZD_HJ4wHfYOjCryXI9Qs5QPAr4t8PnmVni8u8Y03vkxpZeZ7XAAfqI4E-1GVu9OTq2Fnkz2LaQ3Us-bdsE2aALX5cfFhxVWkks4_0VcbMzKxaStDotXtgs6zwcRuy55KaGex927nlsS42477c9oEzdl0ciJo2h6yJL0dQVuxcJvarWtIkovXy504kHC4-yZbVinkei3vSrlCS9QRkKG9L_Ub0n-9qXxpQE8n_rEATGG5o7d1dkgfNwPX3XEhCJd16utTGJXXKuH2K4oefI6NkrAuIphPVAIbWeqmcdr_FnzdrQ2TpTkkDSiBJacTEAMoJ4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در‌ تبلیغ سناتور اوهایو ، جان هاستد : «من خیلی به‌ندرت با مردها این کار را می‌کنم؛ شروع کردم به بررسی بدنش! از بالا تا پایین نگاهش کردم، به باسنش نگاه کردم، تمام بدنش را برانداز کردم و به دست‌هایش نگاه کردم؛ درست مثل چنگال! همان‌جا فهمیدم که تو یک ورزشکار فوق‌العاده‌ای! این را نمی‌دانستم؛ تبریک می‌گویم!»
@WarRoom
😂</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/25524" target="_blank">📅 03:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25522">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JP9om6pdHwarBjgFEqky7LR5u1WK6OuNcW5o6CnFZFGdxqWelR43IqkDrLAx5XvrRLALEuRZgfKT7KCrxTnKl8QLnT3h25eklUf7Snpgeft1SXKcKwdIF2_SqutaXQZZ-9_lYcnGWR6sb6vJ30B5hUTDBbWUddWMTQdqbsXY_gV33x6tMUd8G0fk9PNlKEcYCJcGJ0O98hrIXPI8jiRH-NImaXxbHxL1w1mpkPyg0LAbrkeyg8rQ6RO_iGZowqYFgUsC-XSuHifnSk9i3oWJ31H2y3ukdQy_LMohYg2eD1eKZd-KahhiShrCERxwGpnKu_S2kPYVL0AxCMFAAFJphw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون پرتاب آبگرمکن گازوئیلی از «حاجی آباد» هرمزگان به سمت تنگه.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/25522" target="_blank">📅 01:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25521">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aae1a1ab56.mp4?token=bDcxdQBwMe2wslPBguwfhlQUypPgdnJo_iYb9hXX2dbPt7_Srodiu5Y8t4yVJN577olL4F4HoErrv4bKQaRMFBrBqNy2MNenRZ1f_C_RNrjShHmfl6b30Q7UKWfXU-WRZW-4tdB_7IKXIM0TyLIbILGLzH5_PTKPlDHFEMtz61StkpJPonWCfQpt2HhBKMbeYPLvJCwrNT0fCOMHh4XhSc-HnP1_O-0aUxZRww_EMkE12GJxR-qrHrVjjxEsEU5GzwOMe3PJsFGCIf63TWK5l7Vd8paBcFnPQAEgTBtl6HLn73NiOBPNP1Btc1xRGpkgVMr9waTQSxS-V0O_A5hVWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aae1a1ab56.mp4?token=bDcxdQBwMe2wslPBguwfhlQUypPgdnJo_iYb9hXX2dbPt7_Srodiu5Y8t4yVJN577olL4F4HoErrv4bKQaRMFBrBqNy2MNenRZ1f_C_RNrjShHmfl6b30Q7UKWfXU-WRZW-4tdB_7IKXIM0TyLIbILGLzH5_PTKPlDHFEMtz61StkpJPonWCfQpt2HhBKMbeYPLvJCwrNT0fCOMHh4XhSc-HnP1_O-0aUxZRww_EMkE12GJxR-qrHrVjjxEsEU5GzwOMe3PJsFGCIf63TWK5l7Vd8paBcFnPQAEgTBtl6HLn73NiOBPNP1Btc1xRGpkgVMr9waTQSxS-V0O_A5hVWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: قیمت‌ها در حال کاهش است و به‌محض پایان جنگ با ایران، که خیلی زود اتفاق خواهد افتاد، قیمت نفت به‌شدت سقوط خواهد کرد. این جنگ خیلی زود تمام می‌شود.
خبرنگار
: با توجه به اینکه متحدان ناتو، ایران را به بریتانیا مرتبط دانسته‌اند، آیا اقدامی علیه ایران انجام خواهد شد؟
دونالد ترامپ
: خواهیم دید ! اقدامات زیادی در پیش خواهد بود.
خبرنگار
: منظورتان چه اقداماتی علیه ایران است؟
دونالد ترامپ
: اقدام علیه‌شان ؟! آن‌ها نیروی دریایی ندارند، نیروی هوایی ندارند و نرخ تورمشان اکنون به ۳۰۱ درصد رسیده است.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/25521" target="_blank">📅 01:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25520">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دونالد ترامپ درباره انتخابات میان‌دوره‌ای آمریکا:
فکر می‌کنم گردهمایی‌های انتخاباتی تأثیر بسیار بزرگی داشته‌اند. هر بار که در یک گردهمایی شرکت می‌کنم، آمارها بهتر می‌شوند؛ حتی تأثیر آن‌ها فراتر از همان منطقه است. تمام این گردهمایی‌ها با استقبال گسترده روبه‌رو شده‌اند و هزاران نفر بیرون محل برگزاری می‌مانند، چون نمی‌توانند وارد شوند. به همین دلیل، نمایشگرهای بزرگ تلویزیونی در بیرون ساختمان‌ها نصب می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/25520" target="_blank">📅 00:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25519">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ: روسیه و اوکراین می‌خواهند به توافقی برسند، اما نمی‌دانند چگونه این کار را انجام دهند.فقط این ماه ۳۲،۰۰۰ نفر کشته شدند
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25519" target="_blank">📅 00:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25518">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ: با ولیعهد سعودی صحبت کردم و حوثی‌ها رفتارهای بسیار نامناسبی دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25518" target="_blank">📅 00:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25517">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فرانسه نفتکش DF Peak را در اقیانوس هند، در جنوب جزیره رئونیون، توقیف کرد. شواهد نشان می‌دهد این نفتکش بخشی از
ناوگان سایه روسیه
است که برای انتقال نفت و فرآورده‌های نفتی و دور زدن تحریم‌های غرب فعالیت می‌کند. این کشتی با پرچم بنین حرکت می‌کرد و به استفاده از پرچم غیرقانونی و حمل‌ونقل غیرقانونی سوخت مظنون است. نفتکش در فهرست تحریم‌های اتحادیه اروپا قرار دارد. تاکنون ارتباط مستقیمی میان این کشتی و صادرات نفت ایران تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/25517" target="_blank">📅 23:58 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25516">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هاآرتص: نتانیاهو در تلاش است با جلب موافقت عربستان، زمینه حملات گسترده اسرائیل برای نابودی حوثی‌های یمن را فراهم کند. به گزارش این روزنامه، محمد بن سلمان، ولیعهد عربستان، فعلاً با این اقدام مخالفت کرده و نگران پیامدهای سیاسی و واکنش افکار عمومی عربستان به مشارکت اسرائیل در جنگ یمن است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25516" target="_blank">📅 23:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25515">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مسابقات دختر شایسته جهان عمدتاً در چهار رقابت شناخته‌شده با عنوان «Big Four» شامل Miss Universe، Miss World، Miss International و Miss Earth دسته‌بندی می‌شوند. در میان آن‌ها، میس یونیورس و میس ورلد از قدیمی‌ترین و شناخته‌شده‌ترین رقابت‌های بین‌المللی هستند. دونالد ترامپ از سال ۱۹۹۶ تا ۲۰۱۵ مالک سازمان میس یونیورس بود؛ ابتدا به‌صورت مشترک با شبکه NBC و سپس به‌طور کامل. او در سپتامبر ۲۰۱۵ این سازمان را فروخت و دیگر مالک آن نیست.
دیگر مسابقات صرفاً با تبلیغات، جذب اسپانسر یا پرداخت هزینه شرکت‌کنندگان تعیین می‌شود؛ مسابقات خارج از بیگ فور اعتبار منطقه‌ای یا تخصصی ندارند.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25515" target="_blank">📅 23:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25514">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اتاق جنگ با یاشار : ترابری نظامی آمریکا همچنان با شدت ادامه دارد… از ۲۴ ساعت گذشته تا همین دقایقی پیش! ترامپ حرفه‌ای بارها تاکیید کرده که زمان به نفع او است !
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25514" target="_blank">📅 23:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25511">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RaWe2GyPp-wpJm-kan9KI9sF1dl5eP7omEe1P5zfBbGuvb5rLmj79fG8jaP2rzhbOOANjqEj4mDaztNalnH3Eq932cFQoIHO2ZwaRiLYWtB_XtwakFicDqgHMfP4qZV7ikBvkjfLXsINXRrcvjHDfYnK0-NP-gcoBJahdVHNwO-XpDMe_TekfdxER1SF6P_Ge9DIymTg1DvCgGn9KBthkVfX0UK7vpCv5-IkdfTOXBXupjAewZmarYcPg0ByvlA4O8xDdIH9-011CS7RjXR1QDv6etqQnOihSUcaJd_Bn5n1JP8dFYf4ZJtvYqD8GpdKyUdfDh7lPuK4v12JClb6Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q80rZ5673BQoIQh-0dIKgo33Rb5Q0Ljd7dSoUs-_VBVFp5vKmaO8HZUncVZIfCOCwiXJcLFH4fVO0vX3OilZDJld28982CBoCkTLJCPeQEq1MGCsq6hRo5ffxNMN2wQjtBGqUBf82xO3_krYaDDGx9tnsZQig5vYOX825RTGmyuv8qC7kZVM2ArrtDQ_XK-N_2aQTYtqWau467j6qI8XEu3b9PfKqr3fI97jlMGwgEf0748C7mkF-HIHpgLG0G3kUkX5lCDfGYQfrNTjFrW9frag5_ziiUC34cxD9bcmsiloHPkSd0qqcZ50yjWMkBtUoT_tOhHc-IMAgt4p0m9lRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MG49yRjennbCkjC4CZUi2W1zuJNUIVNnVvqwcMfJqFKm1KziDB5VR2c1EQFynReagL2KavkyE7TvEzMiN21BiScqCarEz431rrwgJMJ5f1eYWJ6en2po-JFN9ROd8kclrHLQpvKCNNziPvw6IWT1vwhSsqddxPx8jm-malx9XfQ08TbCcf1xXG8C_OWg64uv5jYPGYsD6XU5Lzk22E5W7NdRvX3Y5rxYF_jOTSOXdlyXTqhwtxSM0QZkcdnA0k_hYd4kO58eZt5PhITE1yWlXG0b5xssYegkR_OBP5WwZgJ57QYGPfdtHNcyY7ruSLFQKIsMdCMz46SOj51-zn8IQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا در سومین گزارش پی در پی اعلام کرد یک نفتکش حامل نفت خام هنگام خروج از تنگه هرمز، هدف پرتابه‌ای ناشناس قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25511" target="_blank">📅 22:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25510">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">العربیه: نیرو های امنیتی بخاطر حمله حوثی ها، بازی را متوقف کردند و سریعا رونالدو رو نیز از ورزشگاه خارج و به یک جای امن منتقل کردن
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/25510" target="_blank">📅 22:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25509">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caBuwpkyanPvxEoX2GNf5xv8-DeHxgmXvwtUTm5XgZgC-cf9FmP-NHXovoNZpVC4E-UaNFg93RFXlpI7pX6-ZpMnHjzY0JpfBxYlgDUenLpR0LQfSx4BMt2lJCe6AaHiZXRyWVIIdnG-fcC5rgCX-EwcIU4VzWFw83xm-w2b8nU5_gWmQxibG88kk8NtUDwIkaQxzoHyjHI6aHa3qF7Fub_A0A7_g2WdOzzddGo2cu02jVjjp3jRZugEWocMAkTpW61sAnkrde-qHSsfC2XpgTx2u495EcfJ8Leq2UtWyt1C1XHwVnEeW-t2V35bQ6MLAhdyQToKwYNciG-RNOslTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظرسنجی کانال ۱۲ : ایزنکوت حذب یاشار فاصله خود را با نتانیاهو حذب لیکود افزایش داد.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/25509" target="_blank">📅 22:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25508">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO): گزارشی با تأخیر از وقوع حادثه‌ای در داخل تنگه هرمز دریافت شده است. بر اساس گزارش یک منبع تأییدشده، یک نفتکش حامل فرآورده‌های نفتی هنگام عبور از تنگه هرمز به سمت خروجی، با پرتابه‌ای ناشناس هدف قرار گرفته است. مقام‌های مسئول در حال بررسی این حادثه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25508" target="_blank">📅 21:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25507">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO): گزارشی با تأخیر زمانی از یک منبع تأییدشده دریافت شده که بر اساس آن، یک کشتی کانتینری هنگام ورود از تنگه هرمز با پرتابه‌ای ناشناس هدف قرار گرفته است. مقام‌های مسئول در حال بررسی این حادثه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25507" target="_blank">📅 21:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25506">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc43053e1a.mp4?token=UxKh5ovqWVaD0pKCVJe4vyU9lhh1Fm6622iMypwXwlXHZmKu_v_CPXymDTtt76FgY5CQ26ZAwuMeGDdWiy4KxR8d1guQD6hAS-inRxHkspWqh3LM0yVih6-xmmOKtomMTvD8RTk05-vVqvTIQSDp_ivyqpeurtaDuPWu3vP_iZ2zoGWDptR3hdDs0tOQPGggs_KVz7AwEfzbI6JDSHR3qNpFRUo61hzOEys6t7ZTIbW_7NlBIaNp7u3UGbSGS-nutB4TosItqTapE43mhcdVFBtWbuCtenHY_MntHuvFUwms7QOYHOiq9JWotNVWdRERdmqy5aFbqJy-IP8J6KnrTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc43053e1a.mp4?token=UxKh5ovqWVaD0pKCVJe4vyU9lhh1Fm6622iMypwXwlXHZmKu_v_CPXymDTtt76FgY5CQ26ZAwuMeGDdWiy4KxR8d1guQD6hAS-inRxHkspWqh3LM0yVih6-xmmOKtomMTvD8RTk05-vVqvTIQSDp_ivyqpeurtaDuPWu3vP_iZ2zoGWDptR3hdDs0tOQPGggs_KVz7AwEfzbI6JDSHR3qNpFRUo61hzOEys6t7ZTIbW_7NlBIaNp7u3UGbSGS-nutB4TosItqTapE43mhcdVFBtWbuCtenHY_MntHuvFUwms7QOYHOiq9JWotNVWdRERdmqy5aFbqJy-IP8J6KnrTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیست دانش‌آموز کوهنورد بر اثر انفجار یک مهمات عمل‌نکرده در نزدیکی مرز شمالی اسرائیل مجروح شدند. به گفته سازمان «مگن دیوید آدوم»، یک کشته و حال دو نفر دیگر نیز وخیم گزارش شده است. پدر یکی از کودکان مجروح چنین روایت کرد: «این گروه کوهنوردی مربوط به دانش‌آموزان…</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25506" target="_blank">📅 21:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25505">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">صداوسیما لحظاتی از شلیک موشک‌های کروز در تنگه هرمز تا عملیات مین‌ریزی را منتشر کرد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25505" target="_blank">📅 21:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25504">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رویترز: ۶۰ کشور در بیانیه‌ای مشترک بر آزادی کشتیرانی در تنگه هرمز تأکید کردند و با وضع عوارض عبور کشتی‌ها، دریافت هزینه‌های غیرقانونی و الزام به اخذ مجوز قبلی برای عبور مخالفت کردند. بریتانیا، ژاپن، استرالیا و کشورهای اتحادیه اروپا از حامیان این بیانیه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25504" target="_blank">📅 21:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25503">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">جت‌های جنگنده اسرائیل بر فراز چندین شهر و منطقه در لبنان، از جمله صیدا، منطقه بقاع، کوه لبنان و شمال این کشور، پرواز کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25503" target="_blank">📅 21:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25502">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ممکن است آمریکا در تلاش باشد ایران را به حمله اول تحریک کند
آلن ایر، عضو سابق تیم مذاکره کننده آمریکا نوشت: ممکن است آمریکا در تلاش باشد ایران را به حمله اول تحریک کند. احتمال انجام دور دیگری از حملات آمریکا علیه ایران بسیار زیاد است‌. با انتقال تجهیزات و نیروهای نظامی بیشتر آمریکا به منطقه و انتشار گزارش‌هایی درباره فعالیت هواپیماهای اسرائیلی در نزدیکی حریم هوایی عراق، این احتمال وجود دارد که  واشنگتن عمداً در حال آزمودن آستانه تحمل تهران باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25502" target="_blank">📅 20:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25501">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">امانی ، سفیر پیشین رژیم در لبنان : قرار بود پیجرها بررسی شود و برای همین عملیات را زودتر اجرا کردند
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25501" target="_blank">📅 20:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25500">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeYy-8zG4bLzay3vkJzyjCxXDLB2TROsgFOoiRYP2Vgillc_ZzdMbMqg-Im2MRnFwVQIj18gJLXpHUYbwaUGmBygu-LtnuFxpoZqY1YJqn7h2mhh4Zfgau3BhKXCgmZMfTi84_80nm7mRZ_3MRHj7hX8sWYJxSU2CJJyg-9vQdlpaQ5jbEJtJlA6qPkfmVRXV0cpMxXp6Hau4zA98HDoxa-e9-KLj9-RInKlmla5EZ00UikbgV8BcdaViBIjs6lI4FpGNnW9a-RZb8M3MIxou0AnqzgkR9ZMZXuXWDNptso_9vZnveUDn1N8Ts4kFERWj7pu6vHIahg5dcaKyuzLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث، وضعیت ۱۵۹ کشتی نیروی دریایی جمهوری اسلامی. در زمان ترامپ : کف دریا در زمان دیگر رئیس‌جمهورها: روی آب.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25500" target="_blank">📅 20:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25499">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بریتانیا، روح‌الله بازقندی (رئیس پیشین اداره ضدجاسوسی سازمان اطلاعات سپاه پاسداران) و شهرام علیرضا تمرزاده جکی را به دلیل اتهامات مربوط به مشارکت در فعالیت‌های اطلاعاتی سپاه پاسداران انقلاب اسلامی و توطئه‌هایی که افراد یا دارایی‌ها در بریتانیا و سایر کشورها را هدف قرار داده‌اند، تحریم کرد.
‌اندی برنهام در سخنرانی خود در مجلس عوام بریتانیا راسمأ اعلام کرد ارزیابی‌ها نشان می‌دهد که حمله به پایگاه هوایی فیرفورد به در ایران هماهنگ شده و هدایت آن به طور قطع توسط سپاه صورت گرفته است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25499" target="_blank">📅 19:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25498">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بیانیه ۲۹ کشور از جمله انگلیس و آمریکا: ما یافته‌ های بریتانیا را درباره دست داشتن ایران در حادثه پایگاه فیرفورد تأیید می‌کنیم. حملات ایران، حملات سایبری و فعالیت‌ های ترکیبی آن را محکوم می‌کنیم. واقعه فیرفورد آمادگی سپاه پاسداران را برای انجام حملات فرامرزی نشان می‌دهد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25498" target="_blank">📅 19:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25497">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وزیر امور خارجه بریتانیا: ما دو شهروند ایرانی را در فهرست تحریم‌ها قرار دادیم، زیرا آن‌ها در فعالیت‌های خصمانه به نمایندگی از رژیم [ایران] نقش داشته‌اند.تلاش‌های ایران برای تضعیف امنیت بریتانیا و متحدانش از طریق شبکه‌های جنایی و گروه‌های خود، غیرقابل قبول است. ما با هیچ تهدیدی علیه خاک خود مدارا نخواهیم کرد و سفیر ایران را احضار کردیم تا این پیام را به او منتقل کنیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25497" target="_blank">📅 18:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25496">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آسوشیتدپرس: رسانه‌های وابسته به حوثی‌ها مدعی شدند حملات هوایی به دو منطقه در صنعا، پایتخت یمن، یک کشته و ۱۲ زخمی بر جا گذاشته است؛ از جمله در یک کارخانه نمک و یک منطقه مسکونی. حوثی‌ها عربستان را مسئول این حملات معرفی کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25496" target="_blank">📅 18:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25495">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز، درباره حادثه امنیتی در مرز لبنان :
«در غم سنگین خانواده پسری که در جریان یک گردش در نزدیکی مرز شمالی، بر اثر انفجار جان خود را از دست داد، شریک هستم و برای همه مجروحان آرزوی بهبودی سریع و کامل دارم.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25495" target="_blank">📅 18:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25494">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تتر و دلار ۲۶۱،۰۰۰ تومان
🔻
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/25494" target="_blank">📅 18:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25493">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5f3a421c.mp4?token=OaWwdiZws8_iMtsJZ7iXeAOsRETjrEgmfcRUEPEB55QxRCzDvXHs3wFQsK3DtSa46eDp19qujbVsJnsKAqCDS8tLAsgk8srymqCkRUmNmATezi1l2JwZuQjBD5PXjfUxnUZK37J_E3ztusHOYfnlsQ0HKW6uay6_XGqYwzi2iG_Cw06TzHQXQFaPUHlxg33nFC-MscYK4RGodhFVztkVcOKX-BXjqQ5LQMtX_iqK7KG-sSl9DF07eiGgddaY51DsFBZVxTA9mYeuAISQVzonKLRvdz5gfExFKw0hWTbHEAOjPhJrDhFShhMMU3h-TClHCRC44yTPboMlQxK34ouzKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5f3a421c.mp4?token=OaWwdiZws8_iMtsJZ7iXeAOsRETjrEgmfcRUEPEB55QxRCzDvXHs3wFQsK3DtSa46eDp19qujbVsJnsKAqCDS8tLAsgk8srymqCkRUmNmATezi1l2JwZuQjBD5PXjfUxnUZK37J_E3ztusHOYfnlsQ0HKW6uay6_XGqYwzi2iG_Cw06TzHQXQFaPUHlxg33nFC-MscYK4RGodhFVztkVcOKX-BXjqQ5LQMtX_iqK7KG-sSl9DF07eiGgddaY51DsFBZVxTA9mYeuAISQVzonKLRvdz5gfExFKw0hWTbHEAOjPhJrDhFShhMMU3h-TClHCRC44yTPboMlQxK34ouzKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی تروریستی سپاه اعلام کرد طی دو روز گذشته، سومین نفتکش بزرگ را در تنگه هرمز هدف قرار داده که در پی آن، کشتی دچار آتش‌سوزی شده است.، این نفتکش هنگام تلاش برای خروج غیرمجاز از تنگه هرمز، سامانه ناوبری خود را خاموش کرده و با وجود چندین بار هشدار، به مسیرش ادامه داده است
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/25493" target="_blank">📅 17:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25492">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">چندین پرتاب موشک بالستیک از شهر های : یزد، اصفهان و کرمانشاه گزارش شده است. به نظر میرسد تمرینی و برای بازدارندکی و رخ نمایی توان باشد
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/25492" target="_blank">📅 17:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25491">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d4c1ebf1.mp4?token=mDiVFahHJjdhRvvh-oMbwhc40MnbvekDFJuzANoS9Kw0GxelFc35dElN4SmTklqwJymAEKlMR3Av4VN-kzF2-Q9_6O1YyRYnLJavL-xmh9Jgtf9e06MsqUlG_nIIQocZ70hNNDNfkt7NrI1dH5Kv6O6pJHHHQDuFyqUxoj8oQVMQAtnbSmKa3A4VzRgibZygN7QqAcY51ywwdv--pcqNV0V1QpRpeTu0OiOIH4kpGgWVpBPgSiciAxkhtKlN_4JtEpD6KRlnfnxq5L3mWAeZkltkoS74JkS8oXq54oXMHVGvfQV0zVFTotzGg1b9HR2TnDgyy0bnUJiTwUQh8Oa0Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d4c1ebf1.mp4?token=mDiVFahHJjdhRvvh-oMbwhc40MnbvekDFJuzANoS9Kw0GxelFc35dElN4SmTklqwJymAEKlMR3Av4VN-kzF2-Q9_6O1YyRYnLJavL-xmh9Jgtf9e06MsqUlG_nIIQocZ70hNNDNfkt7NrI1dH5Kv6O6pJHHHQDuFyqUxoj8oQVMQAtnbSmKa3A4VzRgibZygN7QqAcY51ywwdv--pcqNV0V1QpRpeTu0OiOIH4kpGgWVpBPgSiciAxkhtKlN_4JtEpD6KRlnfnxq5L3mWAeZkltkoS74JkS8oXq54oXMHVGvfQV0zVFTotzGg1b9HR2TnDgyy0bnUJiTwUQh8Oa0Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک جانسون: همه منتظر نتیجه انتخابات آمریکا هستند
حاکمان ایرانی‌ها این دوره انتخاباتی را زیر نظر دارند و می‌خواهند به رئیس‌جمهور و چهره سیاسی او آسیب بزنند و فکر می‌کنم این موضوع عامل مهمی در ماجراست.
پس از انتخابات، فکر می‌کنم وارد مرحله‌ای کاملاً متفاوت خواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/25491" target="_blank">📅 17:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25490">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
ایران برای دست‌یابی به سلاح هسته‌ای تلاش می‌کند، اما ما رژیم حاکم بر ایران را سرنگون خواهیم کرد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25490" target="_blank">📅 16:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25489">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بیست دانش‌آموز کوهنورد بر اثر انفجار یک مهمات عمل‌نکرده در نزدیکی مرز شمالی اسرائیل مجروح شدند. به گفته سازمان «مگن دیوید آدوم»، یک کشته و حال دو نفر دیگر نیز وخیم گزارش شده است. پدر یکی از کودکان مجروح چنین روایت کرد: «این گروه کوهنوردی مربوط به دانش‌آموزان مقطع راهنمایی بود و بچه‌ها آسیب دیدند. لطفاً برایشان دعا کنید؛ این مهم‌ترین مسئله است. این اردو برنامه‌ریزی و تأیید شده بود و همه هماهنگی‌ها انجام گرفته بود؛ تمام والدین فرم‌های مربوطه را امضا کرده بودند. متأسفانه مهمات عمل‌نکرده‌ای در منطقه وجود دارد و به نظر می‌رسد فردی به‌طور تصادفی با یکی از آن‌ها تماس پیدا کرده است.»
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/25489" target="_blank">📅 16:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25488">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حیوانات باغ‌وحش دزفول دزدیده شدند ,
فرمانده انتظامی دزفول از دستگیری چهار سارق و دو مالخر در کمتر از ۴۸ ساعت خبر داد.
این افراد چند رأس بز کوهی کمیاب را از باغ‌وحش دز سرقت کرده بودند.
در بازرسی از مخفیگاه متهمان، ۶ رأس بز کوهی کشف شد که یکی از آن‌ها سلاخی شده بود. پنج رأس بز کوهی نیز به باغ‌وحش بازگردانده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25488" target="_blank">📅 16:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DekF6cuGoWDrrMMeG7B3Cemq8cG3lY2WVAS_t7xzBOCEn7LA813TUeOnA4LFo4b3p_QoWQe4fZB2ybq44ZD2Qt6cfxkNoj0TRoKB2XZM9fSogxLhrU4mQ811bSb_wXMS-aMbuOsKVgBupl8iohAoba6FqvV2udBHrNSKjLIV7tnBPuOZb2fI0w-qqaQ7KXxh4SIJ5I8WkFJEK2qbzNsPVMuDo_H7LC9vTq-AhTkMmUft7UBN7OJ4w_jO-dRu4Fy5jVyu0_QZ0QYwEVW5rwXQBtnyWbRsXG0YtAwW0dpq3B4COEPqDMlOoQDuJ1JX1lRzUP4oC0Wm-P2ItpfRd2gRZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ چینی نشان می‌دهند که ناو آبی‌ـ‌خاکی
یواس‌اس میکین آیلند (LHD-8)
در کنار یک ناو ترابری آبی‌ـ‌خاکی از کلاس سن‌آنتونیو، در پایگاه مشترک پرل هاربر–هیکم در هاوایی پهلو گرفته
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25486" target="_blank">📅 15:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25485">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHDTc3KPgywOx6ze7NtP1DaGQgK_Xfv3ZCMRDBFYpSR9heOCc7sq6OqEKx1ScTmossZVnSLkC_Co2njwoO1kdPe6_4BwH03VxugMgUDDNtHSdtRhqPo1fobIrEtlJsgD5Ap_mxF0knqSBbKJd38F7JpJJa4Wn5SZfh4eIxt3p1lQC9SqIZu1V8R6qKKTESYn3apPC2DB_Uh-xp2ASYwrxtlLrTgsiEh0J4rc3A431saVB9Uux-dfa3eP-q0bhwzCF25QcK_jeW8UEes4-vsU0oXYkJqzjoAj0KORrgd3Bn-A_2WykIUKh-CURAMdR22A-OHaO8t4bQ30Dbt3FLYhug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ فروند پی۸ پوسایدون در حال حرکت و انجام مأموریت در ابتدای دریای عمان نشانه‌ای از جابه‌جایی یا تغییر موقعیت یکی از دو گروه نظامی:
گروه آبی ـ خاکی آبی‌خاکی (ARG) یا گروه ضربت ناو هواپیمابر (CSG)
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/25485" target="_blank">📅 15:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oi9yxpwlYgEzaRAxLZ2MTzqSg9BUJeeVMNxu8zsYkwn3tenPOfRzMWn91YgbSSymYnhR2Z_jkLU1995AkUb5bwLk6eMK3hKi4XZN56PU7ktFcqX6_D2YkYFnKR927ZXcVWsdms1fWXIBMO3Chla2V9YHvBQlB2rgjvT1FzKtOR3WFW7nxX6_b5z4TjRRulPp3Zo6jVkbiTC89Uuu6WSvqRvPjJn-ztRn0kOEmMPQ69deVNDJCB8yoKuP0OHYy6BngV8zlT0IMPfoHtk7XGnr7IrBHAqTCcYKDNEzuPb8jVAinWAdth_KF0ZTuREutH2H4Te4tN_6VkQjf8NqQcfSHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین تصویر از مهرداد اخلاقی کتابچی، وزیر پیشنهادی دفاع و پشتیبانی نیروهای مسلح
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/25484" target="_blank">📅 15:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خبرگزاری معاریو: برآورد نهادهای امنیتی نشون میده اگر ایران [به اسرائیل] حمله نکنه رویارویی به بعد از انتخابات موکول خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/25483" target="_blank">📅 14:59 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
