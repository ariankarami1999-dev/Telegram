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
<img src="https://cdn1.telesco.pe/file/Wd2Ej-hwZEaZVZD1ZqCbQLy6xIRjKUk4378MwiF23eZDfGIBn93emmE4E0htqYSZMaOCGHaMsRWwzKiPL2l-o2c2zy6t5mEZGLg3fEC-thO6O5-ye5_spgEndsz5mQHp_va0ewvh9Z5bXjejuPo81ppDNzGRSlzIOOYhe_9p5SX71uhKlKwEZRrwSZRg5DWxPQh79Bk8zbL5Jh3NHpVKsthwFOpyMYRgDeHlqQxkpgzPf8119cfh5RpPEne155o8rlfVDHGrQnXFPzd1ntpLf57_DgDRGn6HQurqVLPeUPDalFapVRHOXtPUrmHNWpzA0aYgl-vEdFVGI0co5k5_UQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)ارتباط با من:https://linktr.ee/matinsenpai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 16:08:11</div>
<hr>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده.
توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل.
توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی وصل میشه ولی وقتی میرید جایی که پوشش شبکه وجود نداره، گوشی وصل میشه به استارلینک. یعنی همون اپراتور قبلی ولی با آنتهای فضایی. واسه همین اپراتور تلفن باید فضای فرکانسی خودش رو در اختیار استارلینک بذاره.
حالا در مورد ایران قطعا هیچ اپراتور ایرانی‌ای این کار رو نمیکنه ولی لزومی هم نداره حتما اپراتور ایرانی باشه، مثلا یه اپراتور امریکایی میتونه این کار رو به عهده بگیره. اون وقت شما وقتی دارید شبکه‌های موجود رو جستجو میکنید، اسم اون اپراتور رو میبینید در کنار ایرانسل و همراه اول و غیره.
یعنی از دید موبایل شما انگار یه اپراتور جدید داخل ایران فعال شده.
ولی مساله اصلی اینه که توان ارسال از موبایل به ماهواره خیلی محدود و ضعیفه و حکومت میتونه با ارسال پارازیت کاری کنه که ماهواره‌ها نتونن سیگنال کافی دریافت کنن. حتی توی مسیر ارسال از ماهواره به موبایل هم میشه پارازیت انداخت.
تفاوت این تکنولوژی با استارلینک اینه که توی استارلینک امواج رادیویی به صورت مستقیم ارسال و دریافت میشه واسه همین شناسایی و پارازیت انداختن روش سخته ولی امواج شبکه موبایل توی همه جهات پخش میشن و میشه راحت روش پارازیت انداخت.
من مخابرات بلد نیستم ولی اگه کسی تخصصش رو داره بهتر میتونه نظر بده که آیا روش عملی وجود داره که بشه سیگنال به نویز دریافتی و ارسالی رو بهتر کرد یا نه.
ولی میشه گفت توی مناطقی خالی از جمعیت که پوشش شبکه وجود نداره و در نتیجه پارازیت هم نیست، این روش جواب میده چون پارازیت پخش کردن توی همه نقاط ایران اقتصادی نیست.
✍️
aleskxyz</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/MatinSenPaii/5502" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">امروز روز آپدیت بود
دیگه تموم شد فعلا خدا رو شکر
🥸</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/MatinSenPaii/5501" target="_blank">📅 13:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FwVqWoJ5uOZzp5J5tfCZLV699dXQc2xQ6m-iRRmllo9NxJ5wDybX0fAjFAI14NTGQnnia8_CYtKIzEd5xoR13zM6625xUgjNAfPqyxbp5qP_VJZXVd76_f6r0zGrK0qym1YiqgHRJCLjyfJb2UaU43-sQDU4kEc1HuzQDYYuVn3iXvSoCUvVJpru2IW62Ay2uxgYVl8xu4GN7ex1leRI0vqFSlcZ1RvZnx75j-mI8byFTUuL7_dN7nY9nTYFmQTAR_dVxZBuqHqxd8I5MwgnvSwI28iz-wdKMDlXobdwLoy9SjnWakcaXwgd9oFi2xepBok6hmGrKshlpDoIuxbgzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه 0.8.0 از Aether-GUI منتشر شد
👋
- آپدیت هسته‌ی Aether به آخرین نسخه
- اضافه شدن شبکه‌های Psiphon و Tor
- اضافه شدن MASQUE-in-MASQUE
- افزوده شدن HTTP proxy، upstream proxy و exit-country
🐱
دانلود از گیتهاب:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.8.0</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/MatinSenPaii/5500" target="_blank">📅 13:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ELIJ5qOlI0U8Yd3DDhZ18bsRhXcRfieKc-hGF6pQRUbo8oFPO1m7wRmawZiAgiXa-MH5IKUFEghDcWTSgVLtUy4Ya6HD1cY0JF5H-0hnqwIXtY_mJc0jvJZInAYeAGLtzG5Is2IKIZHE9k2Lvce8Zxnc0zSap6nOx44UqKl4kE2YkL7Id_NoW0qdmSMUNXmsrQVKtgMZLr2lDFQBKJNepYy-yDODL8iNMPBayTx-2s12Ucz9KA0sc9ATRPjCf0HaI0WvL3p4HHH3PNUbx6qDayrmyTJPmJ5oT_-SazhLx6PesTPN2aPPWuRGmNPvI_8CWWdhQ6jdlvOYeU0ywP8OQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ری استریم رو هم اوکی کردم، به زودی میریم لایو، روی یوتوب
🤠</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/MatinSenPaii/5499" target="_blank">📅 13:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KzI9c54bm4OHgblLaWI8caOJHmaXEtojl909c7HQVSAVLBt_c5wHDNKyY-hMFYkQvPd_4zfkb-6FrNeHO6MX7jA_VrNwNnXiz8TfXLiUs-iBfvuW35PJFhZGeIY14Ovq4LPx4D8KhqUQ142EiG2oKQfPcM5qN6Sa9wHOmgvT0a-iyQIHg1sFSy2EEA0azsP4fyKzstuVHyxx5kzIlXcuJTh_DAI584ky9UZc2Oq1fY2dj-WHJgbHqgCOVD6n5qhHAZfBe-HMlIS9Sl-rJgWgMPsSpvFVHsQnwcZ9tMOx-zeTz4RcasTZxQjxsedC-wkLz0EoGVmgu5J6Gqkpb1_FEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه SenPai Scanner v1.1.1 منتشر شد
"برای اندروید، ورژن قبلی رو حذف و نسخه جدید رو نصب کنید"
• حالت متنی برای صفحه‌خوان (NVDA / JAWS) و افراد نابینا(ببخشید از اون سه عزیز نابینا که درخواست داده بودن و انقدر طول کشید. این آپدیت رو به خاطر شما خیلی زودتر دادم
❤️
)
• قابلیت Anti-DPI: ClientHello تکه‌تکه می‌شه، همون کاری که توی PattNG انجام میشه. مقادیرش هم قابل ویرایشه
• حالت Gentle برای اینترنت‌هایی که وسط اسکن قطع می‌شن
• Paste کردن IP / رنج / دامنه و شروع مستقیم از فاز ۲
• ذخیره و ادامه‌ی اسکن بعد از قطعی
• اندروید حالا همه‌ی قابلیت‌های دسکتاپ رو داره(برخلاف نسخه 1.1.0 که دیشب فراموش کرده بودم. این الان 1.1.1 هست
😂
)
• نسخه‌ی ۳۲ بیتی برای Termux
🛠
رفع باگ
• تست سرعت مستقیم همیشه fail می‌شد و الان نمیشه
• و Stop بعضی وقتا روی اندروید کار نمی‌کرد
📥
دانلود:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.1.1
این نسخه‌ها تماما روی گیتهاب بیلد گرفته شدن(مشکل اکانتم به لطف یکی از دوستان برطرف شد) و دیگه شبهه‌ای توی امنیتش نداره
👋
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/MatinSenPaii/5498" target="_blank">📅 12:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E7iUKNCqcb8Kz9O6h_DrYzx7HmH-YnM5rcAvBsxKbPBqaXgu2GpCrpTWMLL0IEy57EitKndZ1oE8yBqEGIkFRD7bV1YJ2N0wN9s0h64bVZBM-uT8K2u5qrzpKM5BkACNV7IWZ2G39fFi1ng-45nivr_OSo7Oktc_BiutVe3Gadqy21FVqc2ZhkkkKOAyTW4nqEbJEi5GP0Z13sZDMLxA3CMN61TuHFq0O7hOmtxCm0Y4e2cE_jWAxa53E6TvSPh1CwSNzYR0KeNSNlctFCESAQpNKJKfVeyMJJz3w6LvqfeSUVmJFUp4BSCyEEhncWE65DcYOBleBknFKdAaJZ4T7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایجنت گفت تمومه، دیتابیس قبول نداشت!
مایکروسافت با همکاری هاگینگ‌فیس بنچمارک ThinkingBox رو منتشر کرده که ایجنت‌های هوش مصنوعی رو نه از روی حرف‌هاشون، بلکه از روی ردپایی که تو دیتابیس و state نهایی می‌ذارن نمره می‌ده. مثالش بامزه‌ست: ایجنت ۹ تا تول‌کال تمیز می‌زنه ولی تیکت مشتری رو بدون حل واقعی می‌بنده. این بنچمارک ۵۰۷ ورک‌فلو واقعی کسب‌وکاری رو هر کدوم ۲۰ بار با مدل‌های مختلف اجرا می‌کنه تا معلوم بشه کدوم ایجنت واقعاً قابل اعتماده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/MatinSenPaii/5497" target="_blank">📅 11:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity https://github.com/MatinSenPai/Gemini-Config-Checker  " دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید: https://t.me/MatinSenPaii/2881 "  کانفیگ‌های…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/5496" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cfp2UmGrBrEzae8qNAviwDQ0w_1UJepJS6eF25N4vsArGogeAv1301aYInj53SgXaenyP4wulXp6JJkls-ZSshDW3CVcRV3fIQzazv4Sv0Qdvn52yk60hhz9KREB392_net4eVIX6zuyS5kaFqAuhVOfwOExI83OMYdHbnXbC-UMfQFVYj8SJv4j2jPcYZ3zi0UxJ5RnkYKwBHrDzEK2AAJelbE4xyTXq_vzpLfexY-SIDWQntWVFPtOF1gIqQUZGo0czpY5w-v0d6H_tI28xp0W9RjYtEi0p2Vl77--Q5W5TO5b8RQJUnTKNi_vwLsQUXCVS4ACVzfiqW7LG77a4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5495" target="_blank">📅 22:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/MatinSenPaii/5494" target="_blank">📅 22:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">وقتی یه مدل رایگان لوکال پیدا کردی و پروژه رو باهاش می‌بری جلو...
@Linuxor</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/MatinSenPaii/5493" target="_blank">📅 22:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CktH1JwO0eh0SzO2IVvl-vTEh_xmEwFR0j2RZstCPeH4qoB6ANMenqdZaT_9b0t9Apceydx3O38KDvd5F6UbQLyVMf3xzkuS4AgtJOo4iBz01Ah3063ma9Di1aWbzgkvvq7MQ_YCsqp5VBUYREh14E-V92ePbyD90BORwZVl2Ewa_032ZG-6CjNh4E1N-5Pt0dV9w5A4jLWAXOX1OgjUCR1fC7nWWXufmWjpNdKYFwAC9YmOk0fP7QErAY3mAJHllVylPg2qvi9dlHFhxEmyUcN1wq_RFMqaRgT8ZSTvvuLtenqWl5y_poSHYc0YROOUsnH5PlsFDluH2N42iKEjAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه دسکتاپ Cline برای لینوکس، منتشر شد
روی Cline می‌تونید از مدلهایی نظیر
Muse spark 1.3
Deepseek 4.1 flash
Mimo 2.6 flash
به رایگان برای کدنویسی استفاده کنید
https://cline.bot/desktop
ویندوز، مک و لینوکس
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/5492" target="_blank">📅 19:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=qqQZv-M42-tdJ01F8eikCg_hP7ezb69WeBdFHnq99_L9QhueZuCb2jQtGblksLJqRzJFKnL6WTp62deHvq07eX997sveFUp2yvteEd8vrvHBhWmRTGdny001tWAax55F-B_yH-chfX5e3fmbXFw2tkHmbmyHlVzPgSnvbnRxqaT-wnIl0gGU2LnUMu9caSoyrADrzGNFI6WUqLpqJj3mXmM3SXlEvmPu9jmAbEjQGMcvHfDDeVtVCdggANova1rFcN7rL1qtOvyEr8HvV3wTmumsKhAO1C9I-b75LbvwO8ZGAWW8goRxHoyoSf8mqSoDg0E4rl18r2ogkPkqkzQysA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=qqQZv-M42-tdJ01F8eikCg_hP7ezb69WeBdFHnq99_L9QhueZuCb2jQtGblksLJqRzJFKnL6WTp62deHvq07eX997sveFUp2yvteEd8vrvHBhWmRTGdny001tWAax55F-B_yH-chfX5e3fmbXFw2tkHmbmyHlVzPgSnvbnRxqaT-wnIl0gGU2LnUMu9caSoyrADrzGNFI6WUqLpqJj3mXmM3SXlEvmPu9jmAbEjQGMcvHfDDeVtVCdggANova1rFcN7rL1qtOvyEr8HvV3wTmumsKhAO1C9I-b75LbvwO8ZGAWW8goRxHoyoSf8mqSoDg0E4rl18r2ogkPkqkzQysA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم
سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5491" target="_blank">📅 19:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MyeC-TyLUxu5wVnZ96MHF3N-yFDmiuXZnXHQDsupq8n2oZyltZSziiUvD5Jm_0yFwhOFUOxM25zj8IohwFsyanhUBy0SCW1bSGzPoJnQtp4rTsTbbYZp6IfWakuplYFXS63jvT1TQDSL2GK37EQ4WhyAt9gfHILrWUlvsXqooaioN57pEboIiJ5jhyJINoDXppo4IFPdWaqzeGPeOUghg5WxFUiHxRroLUNNMpGZtW6CxxA2Ndw6DXXsdHRKfTrp5D-hjsdFMVVo1umVgRVZThN6dgxqFjDa3ZImSOBtX-ki9sM9xk9AfJ5rAR-jLOf963SbxkFdIx4cMU_kci_3OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/5490" target="_blank">📅 18:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ok5daQXPSiDgu2JqQEJxx3FxxBXvqOjwL8tkDxELqYoCDsMETiUetcID0JvUmW-rhyKBKaws2KvkA2vFSCp9QM-GyczD5s5htO6kP2vhxfiq9Tl2BeBsV3umGfDnQsVwXnPxfAgA2M2Oqh-W9eRNDflHP7ayGBWu0dExhS6i3mJNnNdJ30nyH5THKXnNWUWk5H1S012jA0uWSSaYzpfSZO9I3ibUmcZxMW9zbU5O3hsXEpVgu54wPiLznpz7zL6IJsqnJIKkRJHnCg_dovgCEq9suBT1KYRwFGc7mGmt2MSSiEcKfr-VI-rNOuOJPuD3o1jDZuwl0gnFb3MSlc6ZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n28PQJDTTgb0afKu4ES0jeg05No1CR_MEwSblTMRzLLM9w2_mBbWaePXqMvWtKMRDnVrQsZHWAB4u08IWcx7HXqrj_nQLtB-Hv1m6Iin7sD-rf2-JesjgyQFJnDD0xuYddX8uiHrsaehxYin5ZGmktRnzKG9JgAe1UBFL-h_SlRm8t2fJ4PVXp2Uegi1wXw_BvPAH2rTbLylcjEPwKa_7ovdUZiBUz5x0GnT5lnp8wHYjqVdC6xppqFrxYWoQl2z3dNMhQNSLp54QjYePmEZIHzrMOKjm55tGSGtVmfz8_9RjI-3_9LBtF_YwDXcgJDlUmysgicqIyvax5OTtQ2n1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/5488" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTaleo Comics | مانگا، مانهوا، ناول و کامیک</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X5qMmjQEEDz6a7Yjj46Epn_8cWkHsC47CiPYquzPWEWQrYa6AGsmd6eNeq-gbPkUsVOTxbGZLIrYTuRs5pjkXcIcqqyHqBI9B54TkzxhRganJZBykzAz60Nkm-s5aDWTI3Gl6lUhtLgZZLK6w3WeN9vUk9KUTYM7DKbNqDo7cKq2wbuBFOJXwOmZ2d1PnN8o4tljss8pspL-XV2w42xcYhHGFeBySxwD3_pxaN7QRQsxucaBUk2F1AJtOT6fHhiokXCNcb_9cnYVpu1dmoOWdFLjywsT2f8FXxaKO3oZnt03_P4uKWUpRRgGgYiDmSL-k7zOmWy2gTV1E_ewsBs_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔤
🔤
🔤
🔤
🔤
استخدام ادیتور مانگا و مانهوا در تیم تِیلو
😳
شرایط:
1- تسلط به Photoshop(برای ادیت با کامپیوتر) و یا ابزارهای مربوطه در گوشی موبایل
2- حداقل 3 ساعت تایم خالی در روز
3- مسئولیت‌پذیری
4- کار کلین(پاکسازی متن) و تایپ‌ست(جایگذاری متن)
به همراه یکدیگر
انجام می‌شود.
5-
استفاده از هر مدل AI برای بخش Clean، هیچ مانعی ندارد.
وقت شما برای ما ارزشمند است.
حداقل حقوق
به ازای هر چپتر مانگا/کامیک: 60 هزار تومان
حداقل حقوق
به ازای هر چپتر مانهوا/مانها: 40 هزار تومان
نکته‌ی مهم:  پس از استخدام، یک ToolKit کامل افزونه‌ی تایپ اختصاصی برنامه‌نویسی شده‌ی فتوشاپ + اپلیکیشن کلین با هوش مصنوعی در اختیار ادیتور قرار می‌گیرد تا کار، ساده‌تر شود
برای انجام تست اینجا کلیک کنید
🥺
t.me/TaleoCo</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5487" target="_blank">📅 14:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5486" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyvdP5-RUWX9IKFXfcXfDYnE_84jWivC9CX-UJuXMrPlHQaC3mSnWkUcmeGbk_e6hOmrI0MHwPdAogPVDOf0-IpoGsaj4Nfbtdnrv8brtmiwkBjiDMO2d4AVpPTyZnMh-3k1DhCONe8Pj71qGWEtfcubCyZ3DtUgEJOn29KWQsyhMAMs3T8A_-mK8wxHc2Ies8XIwHCWnNrZM1GoGPE2hAEDF3_JowOOcsaHi7FHx1CKGUKYxwMiS4z50tt2trQej3cz-6tEC6n6T0gPcncoExwKBAIDqtFKMezPKAXaB6KrdoAjKOalA35CMdTkw7SmO-GLoUsFJDS7KniMsUKd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان دوران بارکدهای سنتی و آغاز سلطه کدهای دوبعدی
بارکدهای تک‌بعدی خطی که ۵۰ سال پیش اولین بار روی آدامس ریگلی تست شدند، کم‌کم از بسته‌بندی‌ها حذف می‌شوند. طبق ابتکار Sunrise 2027 سازمان استانداردهای جهانی GS1، بارکدهای سنتی جایشان را به کدهای دوبعدی مانند QR Code می‌دهند که می‌توانند ۲۰۰ برابر دیتای بیشتری برای رهگیری زنجیره تامین، هشدارهای فراخوان سلامت و تاریخ انقضا در خود نگه دارند.
من هم قبلا یه ویدئوی کامل راجب داستان بارکد و اینکه چطور اختراع شد و سیستمش چطوری کار میکنه، ساختم توی یوتوب:
https://youtu.be/PAHA55mHLWs
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5485" target="_blank">📅 13:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pBZ_KMDHmi2cyKJvVnBNwQGintNxKU-mL1NtU6qFjicmtGnhB9MsiGQ4-pUgx-xhaa_bLk4MzpZj9k4caC-9fz0t9OaQ_Bo9Z8TLUoZOsZQlweY0Yw8KeEOVREZQhQWOBR3UgQY47z5bVW2iwe7AfRko85yacy90CavkUKQE28GhtWwkD4iKSU81_y6adXbNFI2vd-nUKtn5NViguos_wINFngjWgqf5842z7pG-aUW1H2IduTQ_YsQzz-2oSJloMm5vIdon3YtkQKVutXVBM9zeOIbXNcoBi7L2nRdCVb3vDbAs-9Hi8WS2yhT0M2B6NS-6vul92xnAoNhYLSSiqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/MatinSenPaii/5483" target="_blank">📅 10:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLFQYG1Jh_qNe4APCNkM45cPsjepEdC_T8XQKVdPkHNTQF4hVsoWDD4tlqGjJLJdSjUMRbBjTk6PYc4P63HuK-zIHuiD6Kd9fyNOzr40q9Trnx8H4lme1vDAMFAOFyAPfEmYcLSExtteCk_4OUDPr8rMRBwzLe0bEc80DfPx_VnCtleWjp9I3qzxQ2QJKjwmax5eAFVPDWv2RhWb2g6VywWcP1ihXrDyLGi5XnFGMv1NRXuTuCWkKqCvpa8Dy4iEqeIB2tzYWaaqKU1Eeif0EYdMED4Zx6_9dLyJrgy1Tt_hFgGF_TQyadBL7GPzZxL8E-324OZfdrcS4TCxCNcd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل رسماً سراغ سوئیفت سمت سرور رفت
گوگل کلاینت‌لایبرری‌های Google Cloud API برای سوئیفت را منتشر کرد؛ مخصوص سوئیفت ۶.۲ به بالا با SwiftNIO، مولتی‌پلکس HTTP/2، انتقال gRPC و ایمنی race در کامپایل‌تایم. گوگل می‌گوید با کانکارنسی سخت‌گیرانه سوئیفت ۶، این زبان با ایمنی شبه‌راست و پرفورمنس قابل‌پیش‌بینی ARC برای میکروسرویس با Hummingbird و Vapor و زیرساخت ابری ایده‌آل شده.
مبارک سوئیفتیا
🎨
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5482" target="_blank">📅 09:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/es1B1OFzfvTaFzeKRfZr2au8p1WM4oD9vXwFPBgJ7xhTXYCGk_d2KHDpfSv65cPCGCZwyJQ88Hl_6MUOYYhQh2B5WT43krWwQHlsMWHijct4rCaxTSdsukZWCtMh1YMBtPoD29dUK4KQ-0UPVlxpO9HKN9hehZTeG19XCyRiXUZJo3pcz9Vn6TBNiYbxiiTAo64AmDemZbJEmRzHRuHyYDuM1zPxQLDDJCHtCT_84dEhefuFBhCbOG5PGxq0kQZAgmp83ElpZyO0dKuDOI6qijKfkEy_LkTlNgqYY56Ux9fuRUe7eTM8U1o7GBuYpgt9KbbeUXJ-CF21iZxd9UBjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA  من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5481" target="_blank">📅 18:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VjOTNHGVtDwAo9vN7TC9Bll-Os0w2qkIbxLpQlhybXq8zGOQ6PD2dn0ltCaYqe1ZK5kiOyzxNaBEB3WUK3_9WxNCPIJJMd7vMEsvy-RQhfwr9PXASi1sHRkVbI4zRYPYyfGlCYKxqXWY3_aYTzSe7OxkAJJ9si9EN89UtZOqBicZ2Ys2ockGyEVKVBvmYEvofxvoflMFEfT_X2NzqvoVCtq3M6XtJoxM0XsC4gAQRH3Q9gBwBMrJLJTW06qI7UhmlONnypeKnZ2Q-DDPTFFniNaszsDeQEJ1TeIQatfNvMg3jJKZ_BvkwT4v1SJ97rJ1rl4-dFiGdr_LI06RH-9mBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fJUpxOn_rj-QPlhGJ_AzfFJGqxuNyyE61oV69FXwAbghwsf-v4KILIFOeREwNMPIHsnFEALyzN6FjtVg7hVtCFgK42kSvwzfBIrc0ert-UAAqQ4pLHtZe5rNOMTYO6UPiYz6QOU4r7LEkGRTipM232ODy9jC5PwXZUhyaLiYG9ZtNisk0D92uQHwYlEQo4IXBEBEwuO8o85ln-2UNKLHbc8i7wrLcsHEvgEFm8R_yXb9obvVOmh3HjPRsccvK_U_1wnrQ9hPlQ4PdNR5YSoEfqi_4XY5ENfZB0RZhzjnoFyE0pIaqjziwzmmvgjI_m2nQOihzADNsv-XcncrITRT9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5479" target="_blank">📅 18:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aNbioMwVxBro2a0OSOGFR01jdzlF0qAtAv2ktjkOnQEmy5Dh9FIqSBajMaisq11pNsJ1yUbNl8qDOEmARjM7xpSFSVLES1czikjhmCXrOoGSyR1Y1uLd6G7vQceI7C8wMiewz1tan4A_KfMJoLIuMZDBpiFEfN-h3yald4Yyr7ybWnhp20HvJ6UZvcvY0vWaTdW7QvEdbvQ_zXT3Dn-gUN5tF8fpZeBkMT4-I0DhQc_S4-TVmY2BHD_OfXL2IuQo8zxxSzCf4TYKXcRZVm3WhJ8o6ZU9RQLJgMIJvqzFlFk_nnXIh2tYZe_LDw2WijuUs62HA62_S8mYrOqtZOMNmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA
من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد دادم چه شکلی ازشون استفاده کنید و حتی با اینترنت ملی هم بتونید دانلودش کنید.
امیدوارم که مفید باشه واستون
❤️
دانلود Ollama:
https://ollama.com/download
📹
تماشا در یوتوب:
https://youtu.be/EAF-hMPUMYc</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5478" target="_blank">📅 18:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5477" target="_blank">📅 17:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxY5Mq3iBjQj7x6hRbSJhtHV3kmMT7f5rIEpJKq2lyxDPxAY3LYap74Mp63myAAMEjFFhZxNyB-7eZdTW3n0WKnIQ5JsVy9KfwlhNTZU5tNuAoO0YVAEgLtg4vP7-O7_7mfexgyEnUfl8ZMIf3ckB--IFvIbd13Dv6nfP6lHGL1FGBX3QdGqaQaUDByHWHnTgaKnDm6PAj03P8pOzGA0nHk-fkOAiTXtyi8hnu8NyPewHa6Rl9mKhV4xj6eeVTey39mKqFm01NPaXzQNClnK2OX3I8k8m0AktKBHvH0pLqDrvGidtaR3n77JblMG3lsUWZRESk3mD3VhA_0zrB-jgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5476" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">در کنار بلاک/فیلتر شدن دامین دریافت کلید وارپ، اومدن sni مسک (Masque) فعلا فقط h2 رو بلاک کردن :))</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5475" target="_blank">📅 13:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5474" target="_blank">📅 10:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">چطور فاصله‌ی بین Hermes و دستیارهای اختصاصی Dots و Grok رو پر کنیم؟
یکی از کاربرا توی یه راهنمای کاربردی از اکوسیستم هرمس توی ردیت، بررسی کرده که چطور می‌شه بدون نیاز به پلتفرم‌های بسته(مثل grok bot و dots و muse و...)، قابلیت‌های پیشرفته Dots و بات‌های گروک رو توی ستاپ Hermes پیاده کرد. راهکارهاش شامل لایه‌ی مسئولیت‌های موندگار (persistent responsibilities)، سیستم دیده‌بان پرواکتیو (Scout) برای وب و دیتا، مدیریت وضعیت تسک‌ها با SQLite، و تعیین سیاست‌های دسترسی قبل از اجرای ابزارهاست.
که البته خیلی از ۱۱-۱۲ تا قابلیتی که گفته همین الانش هم هست، صرفا دسترسی باید راحتتر بشه توی UX خود هرمس و به نظرم کم کم به اون سمت هم میره
👍
پستش رو توی ردیت بخونید، بد نیست:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5473" target="_blank">📅 09:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مهار دزدی و Distillation Attack مدل‌ها توسط OpenAI
شرکت OpenAI اعلام کرد یه کمپین گسترده و سازمان‌یافته برای استخراج و تقطیر (یا همون Distillation خودمون) قابلیت‌های استدلالی مدل‌های پیشرفته خودش رو متوقف کرده. گویا مهاجم‌ها با کوئری‌های پیچیده در صدد کپی‌برداری غیرمجاز از متدولوژی استدلال منطقی مدل‌ها بودن. اوپن‌ای‌آی دفاعیات و سپرهای نظارتی جدیدی رو برای شناسایی و خنثی‌سازی تریک‌های Adversarial Distillation مستقر کرده.
(ببخشید برادران چینی. راههای جدیدی پیدا کنید
😭
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5472" target="_blank">📅 01:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5471" target="_blank">📅 23:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آرنا توی این ویدئو، قدرت Gemini-4 Argon رو بیشتر توی زمینه‌ی 3D و قدرت پیاده‌سازی گیم‌ها و محیط‌های مختلف بررسی کرده
که خب کامل نیست و باید توی تسک‌های ایجنتیک و کدنویسی و بکند و... ببینیم
انگار که کلا قدرتش کمی پایینتر از GPT 6 sol هست که خب، ازم بپذیرید که قابل قبول نیست برای گوگل، اونم بعد از اینهمه غیبت کبری
توی دیزاینایی که نشون میده، قدرت Sonnet 5.5 هم می‌بینید
😂
خداست این مدل
https://www.youtube.com/watch?v=h5EL5zThKaI</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5470" target="_blank">📅 23:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CG-6gm7m9VE4hsxVJaCpGTlaBVChRR_TkyG3Wv9ARgAiVNeGaf5oW5Q0ZwrBY1ksklwIhI7xmTdD_t5oFmxltEy-z_YxucY4qECKOsh0dZog_kPn-AtAXaXPl_eVCQTXP-1jt1tT9vzgRLOJ1zp8f-bnG0uOA-3okxOb4aJgWHOVuA1kbus_7iwt9C75gf4ZAUWNv2myxl0B_jlisHRP5z_okF2QLBvpyXnkZAePbe085ldRiVRRGeXMbmCVDNI-PxPXiCGW1OMtJfyW1_UBerrBPCmCD8cXM_0iN4a9e2bvcuQYX7ug9zMUtaiosLc-kd3A_jXqLzsQFNDtAScgYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)
1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا
https://github.com/patterniha/PattNG/releases
)
یا نرم‌افزار PattN(برای ویندوز از اینجا
https://github.com/patterniha/PattN/releases
)
دانلود کنید.
2- کانفیگ V2ray خودتون که با Worker کلودفلر ساختید(آموزش ساخت کانفیگ رایگانش اینجاست:
https://youtu.be/iAbYpjXyLpY
) رو وارد اپلیکیشن(PattNG یا PattN) کنید
3- توی اپلیکیشن اندروید، روی مداد سمت راست کانفیگ و توی اپلیکیشن ویندوز، دوبار روی کانفیگِ وارد شده کلیک کنید تا پنجره‌ی تغییر تنظیماتش باز بشه
4- توی بخش Finalmask raw json، این مقدار رو وارد کنید:
{"tcp": [{"type": "fragment", "settings": {"packets": "tlshello", "lengths": ["0", "104", "1"], "delays": ["0"], "maxSplit": "0"}},{"type": "fragment", "settings": {"packets": "1-1", "lengths": ["114", "1"], "delays": ["1"], "maxSplit": "11"}}]}
5- توی بخش Fingerprint، مقدار رو روی
Unsafe
تنظیم کنید.
6- مقدار Alpn رو روی http/1.1 تنظیم کنید
7- توی بخش Cipher Suits، این مقدار رو کپی پیست کنید:
TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
8- کانفیگ رو ذخیره کنید و پینگ بگیرید. دقت کنید تمام موارد رو انجام بدید. آیپی تمیز
188.114.97.6
عموما کار می‌کنه. اگر کار نکرد، از اسکنر
https://github.com/MatinSenPai/SenPaiScanner/releases
که هم نسخه اندروید داره هم ویندوز و مک و لینوکس، استفاده کنید و آیپی تمیز پیدا کنید.
مقادیر ممکنه عوض بشن، مقادیر جدید رو می‌ذارم خدمتتون.
موفق باشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5469" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzgvcr4dUXBLpYDHyMzKyYBy54Z4HDXHBJXrfdMdvVer_s9JwMITIIo-68C2lBKfvtYRDLTRS3uO8r3NLhTP9-YFcpVD5XKIBQCdlelGNOZ51dPFplJEensxeWkUnCCCu70Zm8M8nxCQVj3HEghDr7apMs-Vff6Uj2tF0IR4nYk7eo_GSwNNlmMGjHWwiOFO_n3KqbH2F38__mdE7Aps1_D9yrOUl53VSGmyOitzDCiA9VAaq36ka6823QFVAtB9WumfWbWaI6zmI02VB86PU12T16K05msuFftqGGe5ZSZR7JwPgJAo11SFsDPH0wfZ3fRXcOo9WCB_hcNNpyuvkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل Airbnb: ایجنت‌های هوش مصنوعی به سیستم‌عامل اختصاصی نیاز دارن
برایان چسکی، مدیرعامل Airbnb، توی گفتگوی جدیدش تأکید کرده که
پارادایم اپلیکیشن‌های فعلی پاسخگوی نیاز ایجنت‌های خودمختار نیست و دنیای هوش مصنوعی نیازمند سیستم‌عاملی مستقل و AI-Native هست تا هماهنگی بین ایجنت‌ها و خدمات به شکلی پایدار صورت بگیره.
خب مشتی یه کاری بکن. ما هم میدونیم
😂
طرح نیاز که خیلی وقته شده
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5468" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بزرگترین مزیتی که ایجنت‌های شرکتی(Muse, Grokbot و Dots) دارن اینه که با مدل خود کمپانی یکپارچه هستن
برای هرمس، یه کم چون دستمون توی انتخاب مدل بازه ممکنه گاهی اوقات گیج بزنه یا دو نفر با کار یکسان، تجربه‌ی متفاوتی داشته باشن
اما همچنان هرمس رو ترجیحش میدم</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5467" target="_blank">📅 19:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">قراره با هم یه اپلیکیشن تمرین زبان با روش Shadowing بسازیم.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5466" target="_blank">📅 18:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gsSzKAYOuE6FoRaGEmnsWxhQ-_z4UKF8r4RVAhrGekMog6l6RtjlOSxNzXlSEkRJpBQjDFv2d7-kAsyWsBkaBHc4cvjF28dd0e6MnxPX4FJGijItE_jYYy6KMOzqrIjTlpkbBrAbfVuV0bzS40QnrKIOT1pblmxoJ3EINygRoBqst1iw3i6Mo1YgotlREhkMPeFfLbcrC3sPdpodQJ0WjAO_n0_aCAkfgV2WBp5m1J8iMGh50YfozUFY1gUjbTPM7X67hUKyaWXFK4qkW6ZotyM0-26TPL6Lxhsgnk7wtO9KeRS7Tyn9oMULn27J-Czb-W53DvdPETtFZuUYXmP3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردیت فیدهای RSS را متوقف و دسترسی عمومی به API را مسدود می‌کند
ردیت اعلام کرد که به دلیل اسکرپ گسترده داده‌ها توسط بات‌های هوش مصنوعی، پشتیبانی از تمامی فیدهای RSS را از ۱۳ نوامبر به پایان می‌رساند. این شرکت همچنین تاریخ توقف کامل دسترسی به API عمومی را مارس ۲۰۲۷ تعیین کرده است. این تصمیم در شرایطی گرفته می‌شود که فروش داده‌های کاربران به غول‌های هوش مصنوعی به بخش پرسودی از درآمدهای ردیت تبدیل شده و این پلتفرم دسترسی رایگان را کاملا محدود می‌کند.
که خبر بدیه برای ما
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5465" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">امروز زیاد ازش استفاده کردم
گفتم یه توضیحی راجبش بدم</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5464" target="_blank">📅 18:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یکی از قابلیت‌های بامزه‌ی یوتوب، Hide user from channel هست
این شکلی که وقتی کسی کامنت دری‌وری می‌ذاره، زمانی که هاید میشه، هنوز می‌تونه کامنت بذاره، اما کامنت‌هاش رو فقط خودش می‌بینه
نه من می‌بینم
نه بقیه
اصلا هم متوجه نمیشه که هاید شده
😂</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5463" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FoMyQFCenFsG9thDMo6an9jOgnCO61Iqe0cbHnD0-kVxo9hKsgkU6VsC_G5ldOEsbVscyLLTDHcNV9GDoUHDZ5lZZ5F-zU8zro9a6446SDe2FuTSDNsY_40Xl3WlIXB-B9dFJQtPVB3-cfMoj6Oexc18J64gYseJy_v7ZXuR6M4P02c_Ac4hHOcdPMJU9hm3-91PqnIi0UbEAoXKU0E7zb7RqNu1-jMuxlwJN6lRXHetjJ0BmczhE55F7P5Wi-VJTExJoQSsVqhbmZEuLm96ky7BGoIeJ3uzRoZHlzIoK09X3THB3chHCfCB2DtLc94rWICyPIMRhV3coaXHSagk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5462" target="_blank">📅 18:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wk9rGK8Y3tCmfStrC-MRSd-SRbRYPLfygP2IutXM4ONUz2qAbv2iMph1bS6vDRgKuJnHf_0f4s6_HyP14vKw89WGL0v4DgoE518nKFDJYOEvEw7q8qOArN1RSBKbUAdWIvygb1OY30RBuEST7phB81T8kMyxPJln8FH6HkRGUGRNzxf4ks5OPQWthZ948Y5JyNZFdfO4tzQcExQQd9vOq143zIwcTrvhF0reC5Bt3QNtp7Bn9TVe4dEums0Zs-Vx0gQ9GAvZRbty2VATKv7q0013bMgHR9BWUpu0uNB1R0fk-3rmvbt1hEUNFeDPIQzuV2lzCf1-nVgXqqFWS2C07Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Decisions API توسط OpenAI برای اتوماسیون فوق‌سریع تصمیم‌گیری در ایجنت‌ها
سم آلتمن از عرضه قابلیت جدیدی به نام Decisions API خبر داد که ساختاری مشابه مدل سریع Jev از استارتاپ TypeSafe دارد. این رابط برنامه‌نویسی به توسعه‌دهندگان اجازه می‌دهد مجموعه‌ای مشخص از گزینه‌ها را به مدل Luna بدهند تا با سرعت بسیار بالا و هزینه بسیار ناچیز، به صورت احتمالی بهترین تصمیم یا اکشن را انتخاب کند. این رویکرد به ویژه برای کنترل ازدحام ایجنت‌ها و اتوماسیون لحظه‌ای نرم‌افزارها کاربرد دارد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5461" target="_blank">📅 17:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SHZ3FqTIWUO0IZvddg9MahH0WdTENMkXcaRUzVtPdqR2M11azgsnZnpP41aoIhXs12q5aiAWg_-m8p5KpExq76kQRcM6MFK6E3frxi0NYolv5BO7jseqSOvIuZRb99to-UM1e4BjerrrTIukny24nocS6xTooCBInUvJIJXFN2asuP6hmtm6rsdeRMiPf1KZZ4VGXPyhw0A91msb5UrmvZr7hYsX_oYgPxwc61Wjc8DV8oDoWhr_eqnOXPYDXah-cZ5QZ1HV4izDjun4V87Kg-sjpNC-EAhyvC24HKgodulK0JFtRz4wc5GuZmV0HSddg3_DyZQz_OPAVfzabDFUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به قول Theo، چرا واقعا OpenAI هنوز داره از GPT-5.6 Sol استفاده میکنه توی چتش:))
نه تنها 6 sol اومد، بلکه 6.1 sol رو هم دادن و چت هنوز روی 5.6 گیر کرده
اولین باریه همچین چیزی رو میبینم حقیقتا بین کمپانیا</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5460" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M_iTkNdXiMMhRXrd1yEcepJHA0V5p7Fmu8QjVsGYO4oznx5A35LImQc8zrk4FaFblr_CFDTjzUr6xrwfod3H_sJs7MPuWFAM5bqqKIdmFbS8Cw_MlnHMlznhnZOgczWIelrmgb0H0b94_Fdk0NLfFdKz_o8sUgcfq8nFhDWorr8y37Wbo7IlBQrr3oo9tYdhElY2uEmSARvIvtuq5YtVvuIGQZK7RitoNs-nVbBBU4cE2CWKKlxNr3L_ld44qkGxnx-DMC7PPfQpVzVeSOQFas77DpSzbMzsh-41gv4BA2PUyQaG9J1Z63EmO2ihGKlfSwdw4sLypMeuIYiscZbCRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله ما نسل Z هستیم
😂</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5459" target="_blank">📅 12:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CoidRt_bWX8prlYgXToYAop2LeMzzb5Ukmg3eDTesbQAX27GWkxVcjcc5kkTEu5lBwLaOg64MWwkLzl-zEaY1--6FXVkGtE1mMZ-b_aR6MPZUfLmMtAg0nwRL0BeLx0IULofPE3CSh4ZjAZk1jccd9dorUywBYno-yKRmHJ_e9UzMl4bBukUrPhG9nspk29irdJFAxFrhMKAnVsmpztVSFroldt22-zCOx8Gvg9uDwcdGxkOzkS5hintxl037CGANPc9KEu7_96r8LIiJ_x2jc9_0C3DmhhCcrFrrCSnQ8o4ZuqexakEEMy3zRHdlQL8eaRfYlPjHdpIjUkHyOEw-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate
توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب:
https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5458" target="_blank">📅 12:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شدیدا حس میکنم مدلهای چینی اوایل که اومدن غول بودن، بعد از عرضه یهو ضعیف شدن
مثلا هممون به Ox Alpha دسترسی داشتیم، بعدش که glm 5.3 flash معرفی شد اصلا اون هوش رو نداشت.
یا من به Qwen 3.8 preview دسترسی داشتم و خارق‌العاده بود. سرچ کنید توی چنل نوشتم از تجربیاتم. اما الان Qwen 3.8 max وقتی ریلیز شد هم از مدلهای Frontier خیلی عقبت‌تره هم توی بنچمارک و هم توی عمل</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5457" target="_blank">📅 11:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/foQdDorZObcEaHf0JsT3l5Zd3PC8nj0Lgg6rhRq5aNO59RwgBa90sKjOAM2P_3aGQ3gTtCngMjSo9W-fS1p31-399Zzj5uS5QdZ80V--hfW1Y2Pz6jtnd81dmKC8VIWaVyEboi-_fm8r7fTlIae7q0A_9iMfTaC3mmO1PzOmUOAn_upcFh3Cyeb3xKmRJS8Wu8ff5bJiiz5msqHE_-EO7Aere1nY-sSqj_9TRXq-PlC08K_GWGaWJ0oGU5xkCP52DuKitnuXwc7jlCl6PRVKqvnQwE3TktH3sXh5eEE-v-c1zUpR_fT_FSmzdVZvMf5eGraQMNgM_1Dn9MIbWhnZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم به نوبه‌ی خودش عالیه
Hallucination یعنی توهم زدن ai
که این یعنی جمنای 4 به ندرت از خودش یه چیزی رو در میاره</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5456" target="_blank">📅 08:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کلا هر مدلی که میاد
این قضیه‌ی Benchmaxxing پیش میاد
نگران نباشید
میگن توی کدنویسی اونقدر هم خوب نیست انگار و باید منتظر موند و دید تا فردا پس‌فردا که شایعات و تست‌ها به کجا می‌بره ما رو</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5455" target="_blank">📅 07:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qr-eXW0PvRJ7qYGzmrHL9FWFaIW2qq8JpZnsc3JiQtgCJ1_3d67lsTsw-a3m3fUkoTBdxQz3KHqxnBb-a5M1YEWpHVAJpsuKv2_yKz1XyFVeYqYvz5-CzX10s2J0UeRzBdiiP2kWJxapNxGkQStDBmAlvKiP-0VO-O0ZFYfNxaRTo6glzXJ4Ra41bP13t6RwvqR9aU9U_OdcaRrNXPhSSn-Po9R6tZAY3OTS-dDEGDeKMuTW7Gd7WTpU2EhZqbWQUPKPYZVMZfneF--ZiNH8eQJfRgeBud7QEd3o3jOpqoGciNA5Clg-KR09_5VY64LWzKWkHsm7f00IHD0LBYRQnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uJLru7fdQbDPnLNIPFdyRCz7bGAVgHP3_j0YO0rP2yEqbfIY6B67IateaH-r3YKkOgG-ORTEsGjriqyKG187WpgZ1VvSNCKjRR-dmzph73rJAYYTetpNqwtKEuH2HyZgjfGkEqLp_p1B1ZVOUQP2v6YeSyVWOwMJUIsqqWPJSfLXa-fMdDAgHIvmCIinFoZksATX5yHcvlruuWj4dWOLBpzg3ZzDbO1LQVEqklkKicXR2q0_qN22Bq42HTpW3HDIkto0byHpQpBl5cGigGz3UEsKmBgIx1uLrSck23odYN_w5GUwZ7nMYydyLowHtBwVleDaex4-EcOiwYpM6jBdow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tG8NhSU2M20mCxv7nRq7h4zhgvkl_z9UJoNmXc-0U5lzxHx8S_V5PWKRBGZUsB7l5A2seYJhA8yAJp8WNTUV57RAlHTawIKzUrSU5h-83uf-5JInUdWfrqlSPOTluTkmL5z587kqCjOJvxf-xZSz0KJ8xqeFVsGG7gWRqcvkeInmbRoYOxmcwgU-m2wIg1aGl0NmJklsMWF98r63kVTcw7iSaFI0rmsLOz6K8oJCQ2OGrzHjzDxawj1rYHVyTnom02hXL7hZxwu0Qv91D3YW1X38HoOtmyunw_m4EwWGyyrKWxH1r4X4e2C9sT9WLhzss2D13NLmxYBjessCsgA0YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o3e7K7omlublrwT3Hhtpas4-b6SGfldYgiqCrIyFoxup9O5iuG5fvXLvRxupfO5G4AD8m77SQMPM7BTymX6yVPICMKDcfdjMpnd-bDx9K2iMnfCgkJer6VIi7Hh2yL9NNK0Dw6XlrdVMQ2TBngUeWLczA8dvANCCONGlA0pb9-Bix1pq3_RzNWR5jXSy_mcO8hDvw3hkNsLzceiEoXhlhjcNRmQtc4ZZXYkC9Qo-Hp1JKBerZzZIfar0VAVPbkqjByx2mpzEZviDYsxhZq8rsPlNq7DBzmBCdokYyaPRCJj7w1D-oxFU2ffo4eBd8GKvcuVoKwD9F8CWy0ay735O_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری  گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5451" target="_blank">📅 01:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=odhMFU7fJLC0TUqUsp8v7mJtcFULOzyqxsqDzUAlxtGf6mAE76noIXYwSD2lUyBuQwSIv8bs03f3_eEYL8L6Jkb60O1rm_XCt_0_l4qQXYn7cElqdOWUrWRAbDpn6UEpstuvL3c_44ymfxFemH0qGZGVlyY8W0LmsC8OFY4jebkMJLfdVLmN0TaR1tjfKGoyqSCYMLRQT9x9qU0PMnXNYEhCyrbLpS51wawZjw87nnxsg45kdSvoQB_fJkRQUokNrjDkEHMo4Ov1XiOq5uoSqopIzGPH1widK6l7tgK4Tyyep4WR3VAzfmjZSR0wO1UUCwl5lBUIQbppv9fiDXzjaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=odhMFU7fJLC0TUqUsp8v7mJtcFULOzyqxsqDzUAlxtGf6mAE76noIXYwSD2lUyBuQwSIv8bs03f3_eEYL8L6Jkb60O1rm_XCt_0_l4qQXYn7cElqdOWUrWRAbDpn6UEpstuvL3c_44ymfxFemH0qGZGVlyY8W0LmsC8OFY4jebkMJLfdVLmN0TaR1tjfKGoyqSCYMLRQT9x9qU0PMnXNYEhCyrbLpS51wawZjw87nnxsg45kdSvoQB_fJkRQUokNrjDkEHMo4Ov1XiOq5uoSqopIzGPH1widK6l7tgK4Tyyep4WR3VAzfmjZSR0wO1UUCwl5lBUIQbppv9fiDXzjaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5450" target="_blank">📅 01:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/goHt8_BTMuNmIWUZxApVazPxJJhxuSMFOoCSa5VGvNu12j6uSqRUIOxCcI_HwtEAJJUolks3MQibSQ-DT7lPWQZZHe0uD1K-gsr2owroznn3iFQdwGhQ6R4lVn0Ahx4PN22OrdGArkTUZWsiM1uItBaICp0qw85UJPEBd35-OrbMaSst9Kxy68k34-rIgVk_ddQnJfoU3Htdfngm-U8SYf5IiiM4F83JCMPpKOx4t0S1xeK07AYUp0Xfs18KjLDa5M6569_bs8SljAydVv3_vsgcjaqPuBY4nXvkExebOc9vug2yz1k-Jwkywp_Jrc5d12DuOqD1cqw6F6L4Szy65Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری
گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای اکثر مدلا) تولید می‌کنه و توی بنچمارک‌های مهندسی نرم‌افزار (امتیاز ۷۷.۹٪ در DeepSWE v1.1) و امنیت سایبری پیشتاز شده که به زودی می‌ذارمش. آرگون با هدف کارهای سنگین کدنویسی، تحلیل دیتابیس‌های حجیم و کشف خودکار آسیب‌پذیری‌های امنیتی طراحی شده.
هزینه‌اش برای دوره معرفی، قیمت خیره‌کننده‌ی
2$/10$
و بعد از اون،
4$/20$
اعلام شده. با 0.1$(بعدش 0.2$) برای هر یک میلیون Cache ورودی
دقیقا هم‌قیمت با Opus 5.5
باید فردا ببرمش زیر تست ببینم گوگل واقعا پرقدرت برگشت یا هایپ الکیه:)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5449" target="_blank">📅 01:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بیدار شید بیدار شید
جمنای 4 اومدد</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5448" target="_blank">📅 00:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BXZ-9vZ7gB7xIWW5-JyBb43SuCFMs5wB53qEyaiwBdwkh6W-aM7Y-ISIYIZ09JbxecRaozIX0WIJBLzEkX06wxWMyZTLa6osuw3KydzX01pMylV2vkViT5rFy7MbZ_sRegeXLj5DI1Ad-Zfwm_b5Ez_oKztqPDhQi3ZMf3FcKTCqtL94GG5kmOZXXRiqevxKC_xqDiozP4lGP1G_U2NbF9fQ6yApnjCVJ3fxkViM12yXiHwl_MXYhMjJEAO1AW5p7b0rboBs3duxQdlSbjVRyZjTkMazOSWUYgDt0eP4MEyW0rC63XZMgXXRsAY-cbbvVDiFdyXj2bCSmdYk1NU8sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش هزینه‌های هوش‌مصنوعی با Auto Router در Cloudflare
کلودفلر قابلیت جدید Auto Router رو به سرویس AI Gateway اضافه کرده. این سیستم توی لبه شبکه (Edge) پیچیدگی هر درخواست رو می‌سنجه و به‌صورت خودکار بهینه‌ترین مدل رو انتخاب می‌کنه؛ یعنی برای پرامپت‌های ساده مدل‌های سبک و ارزون‌تر رو صدا می‌زنه و فقط کارهای پیچیده رو به مدل‌های گرون می‌سپاره تا بدون افت کیفیت، هزینه‌های پردازش به‌شدت کم بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5447" target="_blank">📅 23:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">من معتقدم با مدلهای رایگان، مدلهای چینی و ابزارهای رایگان هم میشه به خوبی کد نوشت و ابزار ساخت
و به زودی برای اثباتش، یه سری کار انجام میدم
چون میبینم دور و اطرافم کسایی رو که هیچ کاری نمی‌کنن، تلاشی نمی‌کنن، به بهونه‌ی اینکه من اشتراک Claude یا GPT plus ندارم و...
و این کارو انجام خواهم داد که شاید انگیزه‌ای بشه، و شاید ترغیب بشن یه سری افراد که شروع کنن ایده‌هاشون رو بسازن</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5446" target="_blank">📅 21:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ویژگی‌ای که Dots و Cues و Grok Bot دارن نسبت به هرمس اینه که اومدن قابلیت‌ها رو محدود کردن!
بله درست شنیدین
همین محدود کردن قابلیت‌ها خودش فیچر خوبی بوده(برای اکثر مردم و برای مارکتینگ خودشون) و باعث شده کارهایی که میشه باهاش انجام داد ساده‌تر به نظر بیاد و سرراست تر بشه. از اون طرف، چون با LLM خودشون سازگاری صد درصد داره، به 99 درصد ارورهای مدل‌ها و api و... بر نمی‌خورید. VPS هم که نیاز ندارید دیگه
اونور قضیه، هرمس به شما "کنترل" و "هزینه صفر(روی لوکال)" میده که اون هم ارزشمنده برای قشر عظیمی</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5445" target="_blank">📅 16:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بچه‌ها ما قراره استریم داشته باشیم راجب دانشگاه و انتخاب رشته
اگر سؤالی دارید، می‌تونید به ایمیل matinsdungeon@gmail.com سؤالتون رو بفرستید با Subject استریم
روی استریم می‌خونیم سؤالاتتون و جواب می‌دیم با مهمونای گل</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5444" target="_blank">📅 14:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uOUjpDbwQtEBiq9C456Uq8pBJziKohH_qmsZaPreHUcszV22DhOq-IKmzQ_AlGPOwpah-8lR0zzkfNqOaHFNj716yq984PaIkh3Qy161bCLnILXiT8qH0_6zGHCaUtEyDRe2aaRWL--sqXK4RZ_fpKS9sGdTWu5XOkevOy_m9maFGTbQqqRExkkR6valIV3krhlSDH9NrAzncV9oM0fTNoAyUGOSAb_JnkQ_zIIlQKmOXaeLhjuA43U0P2ZR0H9I0te7x2exwN8qdgH0UzFWU3fQlXJygsd6ga_-5H7bOs8CFCmljPKvlSnwD3SwqIeVZpaI-w1Xjpxidd7N5-JQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری رسمی OpenAI با پلتفرم Hermes
در اعلامیه‌ای جدید، همکاری رسمی OpenAI با اکوسیستم ایجنت هوشمند Hermes(Nous Research) تأیید شده است تا قابلیت‌های مدل‌های جدید و ابزارهای کدکس به شکلی منسجم‌تر در اختیار کاربران و توسعه‌دهندگان این پلتفرم قرار گیرد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5443" target="_blank">📅 14:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بچه‌ها پدی 2500 دلار کردیت OpenAI داره که میخواد باهاش یه اپ بنویسه به انتخاب شما
رأی من زمین بازی سیستم دیزاینه
😂
❤️</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5442" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5441">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-poll">
<h4>📊 کدوم ایده رو با هم بسازیم؟</h4>
<ul>
<li>✓ تمرین انگلیسی با Shadowing</li>
<li>✓ زمین بازی سیستم‌دیزاین</li>
<li>✓ تبدیل کانال تلگرام به وب‌سایت</li>
<li>✓ ایده‌ی خودت رو بگو💡</li>
</ul>
</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5441" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dbYl5UtefEUzz-uiaBbz8k8jrvZMGgGywejPrGO1WjqlVmqSd9TueNOUZ9cEMDm9UKiXYuKzaGWIkEsoa8e-oh-guB1YbpLi7ryA1yf6AKbJpZXdOGMtOIctzPPGlRkk09htcTlTpZVBBAlnUPYY_dNCU6JjR8zu6tm4sn5C652nYeg0D7y64hzSdDyM4lVn12MAs81pI0YjYFbK7l-Q9y8cARJLyYfN-ypi_rjbW2Dog8UfYsYfqE0n3KVia-568_2f5xcOY9RBngu_LKjHjdh8zW5NZ-yziB4UFzsW9mvwYK1hXgiRPIFPcH4fhTCJliapN-q10wUQ_CmyEE27Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E7Wp5sGt1uAH3E6aaYJIphXSQ9ID0DVQhZsG9ny_kI7EcbhsTfBRpepKmGBxkY9nReQHCRj8_x2m_R5pm5pBwHTEFHFd2EftY9NMif71UmsEeQDWMdj-UMZWPCvyNZY_rzwZQ7PbEE7-HvPhmEbeh5doQRxeGK4eWvaSSZM2L5K8imJEDWGri8Xf1mRtarFLuXJyw6e_tU13Gayyv3u1NP0DmU0q8mDgOJwKjxfTvw6rggqDDG0IbwlTI6v37_3-GFQ-BqHekZTxoML1R3j-QRDd4r9nXa2zDWVyVImZQPFyUz-SNyKeVIu96cMaSPyuEXCHc3yw3GikhFiSfHISUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قبلا برای این کار شاید 20 دقیقه زمان می‌ذاشتیم.
پیشرفت ai واقعا عالیه</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5439" target="_blank">📅 14:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5437">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OWEZamrVVLyQcoQSrIQo7hrpb39yu3JUnLzzj9im-PxrMR0wM6Q-HjoKiu46nnxsiSbPzVFLtuUbndrOzUsGlz-FMxKEIgz3paF4-QydEjFQmcOjkrJ5WMvgONwYpH93sdGe4mKFvR3OPXWXS29oB1rfkp1gc48puJH9Z1v-N_8ok8MhKRfR9BDIl-k6Ip38DiJQ4A-Gvs7JsHnN1PkCfI_yOaolTG7gewIKRJPOtZvMN6M4Z0QkE_H2rTnDeyORq9HPMASXMhjQt0ONN_ytKOSA7-brtCmFvE2yoAUXIiL-SprIMbnEb7AYxePL75bDvCpV1F1EVQP1arkMGmScSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ksxjXNooxSnqEkPNDoHUnKicWpjJqp0j8h0lhxTVJPWpFHHdRDkdhTAmNs2gFWp6tF94qt_iVbpU_2A9ojgHFKD427vmxbvzLqD3j1e3e5mkau0YlLbG1ixei5OcqFr-eWWfmFJiC1I1-hoqKhFj090-ylIlLlBvW5YL7Ak5uE5Rikd4V7DLUIF6IIYvfU1ozi6Obve7-nqVZXdbXctXFgXjPbQzY6LnC3NEysxt5oRhvaGw7KpeNwo-4GephHCyFpvHsFYlY1jsNNDAPc4q_lZN5W8rpFS5sNkGvINYG90sDBBb_9_p2Co--1XHW6_c2JaZ6QjbsRyOBu6MTHeYEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز Manus پلتفرم Cues رو رونمایی کرد
چند ساعت بعدش، OpenAI از Dots
و طراحی بصری ساب ایجنت‌های بامزشون خیلی شبیه هم دیگه‌ست
😂
نمیدونم چه توطئه‌ای در کاره</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5437" target="_blank">📅 12:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گویا همه روی GPT 6.1 Sol مصرف توکن کمتر + قدرت بیشتر تجربه کردن</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5436" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عرضه نسخه ابری OpenAI Codex در رویداد DevDay
اوپن‌ای‌آی بالاخره بعد از شیشصد سال که رقیبش آنتروپیک این قابلیت رو آورده بود، توی رویداد DevDay بالاخره مدل Codex رو به فضای ابری آورد تا توسعه‌دهنده‌ها محدود به اجرای محلی روی سیستم خودشون نباشن و بتونن از راه دور با گوشی یا هر دستگاه دیگه‌ای ازش استفاده کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5435" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=D_I_zQMVsyqMV6i-kVFQCZUl8uskJuu876-bL5kmQ2IyLz40pp72-s2lYvS8nf3yugNtlpUhZZMZqX6qK-Vmf2l3nubThhFYTZd59dIW_hF5CE0DQs784vOrZH0W928qPr4sPDWYt8GT0lLLHAsaok7Mt9y06nMw6AI0iW1dqTGKaZ2kllM687ao862wjv3AlZzi9jFXkDp1DLx0gQbKqHHQbyf1JxgCTvWbqtRX5kw0qnEAxIQvyNJa0vQTUWG-9nlBapLSS7lWj29MSaMSq1HutWNAp0xR0km7_Tg0VPnGFjpCVaX2T9qJMCVGuaDLW-c4p6OuMs3KFvadD40OxA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=D_I_zQMVsyqMV6i-kVFQCZUl8uskJuu876-bL5kmQ2IyLz40pp72-s2lYvS8nf3yugNtlpUhZZMZqX6qK-Vmf2l3nubThhFYTZd59dIW_hF5CE0DQs784vOrZH0W928qPr4sPDWYt8GT0lLLHAsaok7Mt9y06nMw6AI0iW1dqTGKaZ2kllM687ao862wjv3AlZzi9jFXkDp1DLx0gQbKqHHQbyf1JxgCTvWbqtRX5kw0qnEAxIQvyNJa0vQTUWG-9nlBapLSS7lWj29MSaMSq1HutWNAp0xR0km7_Tg0VPnGFjpCVaX2T9qJMCVGuaDLW-c4p6OuMs3KFvadD40OxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5434" target="_blank">📅 08:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حس می‌کنم یه رقابت خیلی سخت بین سرعت ریلیز مدلهای جدید AI و بالا رفتن قیمت دلار شکل گرفته</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5433" target="_blank">📅 08:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5432" target="_blank">📅 00:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مدل Ember-1 از Fireworks: کارایی Kimi K3 با 40% توکن کمتر
تیم تحقیقاتی Fireworks مدل استدلالی Ember-1 رو بر پایه‌ی Kimi K3 منتشر کرد. تمرکز اصلی روی حل مشکل بزرگ مدل‌های reasoning بوده: تکرار بیش‌ازحد مسیر فکر توی خروجی که گاهی بخش اعظم هزینه‌ی توکن‌ها رو می‌بلعید.
چیزی که من خودمم توی ویدئوی کلاد رایگان، سر اون بازی سه بعدی تجربه‌اش کردم و واقعا افتضاح بود. مدل توی thinking خودش گیر میکرد ده‌ها دقیقه.
امبر با بیش از ۵۰ آزمایش و ۲۰۰ ارزیابی جوری آموزش دیده که شاخه‌های غیرضروری استدلال رو حذف کنه و بدون افت کیفیت و دقت کدنویسی، همون نتایج بنچمارک‌ها رو با حدود ۴۰ درصد توکن کمتر تحویل بده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5431" target="_blank">📅 00:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5430" target="_blank">📅 22:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن
به اسم Dots
تقریبا شبیه Muse، یا Grok Bot
https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5429" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5428">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AjztZgfE3zNQ6sWxKCaa2xJz37ZhpqjeinTPxLFZNbZsE8Vcj7ARNv6OcizDZ3jVDP-8k2rOIRZf7HKBz5r0Gw_HBprW0hRGicB_Y63u44UonHq8rt00bvxWjKLysmMjpnfmaBDBlmvZpnc-9rauCYHrxlo7GdhfVkY9f4LdU_0eWKyKPHoUm631PcaOrkVRa-IP4bs4SCdxqY0gPO3hahAkQMZjy8JAB9K-fd5eFqPWY2tMP8d_mhKu93UqeLeswiwiIsoEd9KvTQGvseu2h-VciWLTS1xhIXK8e4CYV0Kh0U71I_fka_MSdz0urFFlD9nV6ri3raNGQ9f-RIHiZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی خندیدم
توییتر OpenAI کلی گفته بود که امروز به مناسبت Dev Day قراره یه چیز خیلیییی خفن بیاد.
کلی توییت زده بودن
هایپ کرده بودن
حالا حدس بزنین چی دادن؟
GPT 6.1 Sol
😂
😂
😂</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5428" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mDMQDy1HU9TsCdHLeAFe6QQIMlbjBlAK2aCFAWp82pEKIjn1V8Ocw6WVgbo_52iDEZ5oFYqCVuZtdtFALJEE1ISEb9HuUt9ar2PPn5AZB07_zjgsKVwKUJ3fq20Qb9ByJBIEfZj27gvTGeqE-LT82n6C55QosWJsJBIAPMQK3DWYqYDX2U6GiGkbALr64ALMG32mmdfXvOaGqh2WydRKWP-3-ynnPc4cJzOGDEaMBDEZRddZRU5U6wyy97270cscjhwjPP2L3e09IFIuns10rg8SZ0JEERfNjIamlLl-o-AtZMEUmo0STrtpLyg2bM1akvK6qQBaQ0-_Q9Pyo37zBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qIShtDFrXdaAvazv-vKcpKbCN5VXvvdF_m3c63eF_Grz1dj_K6NUopaeAenc6yffdF7TkRQz9x6vGfyu-_JLkbAGKxrrTwdAzVjNHsPp5mDBqZ5B2bGwvnqNKfaUfg5a5POMi-ECi4B91AsXqFBteiVmpcqQsB5Vu0LzlBz-PvVM0sxQ_pLOgNgzLhrDtv2chv-pA2jvLKuHrlV2yTdp2IFWqGQ_6-nmHgAH-MJ9-f2PRl6C17ZngxvEulIcfiql7kvC8VMEGTVezSV_bWmgOP7EX7rMcGbKKJ0pYOoQSuCDo3-kyaap5z_5hWb7uDDJ-h9_96vHk_igZhoDGlRuCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کلی ارتقاش دادم از دیروز که الان داره با یه مدل خیلی ارزون، کارایی انجام میده که Astra نتونسته بود. یه پنل تحت وب نوشتم براش که اینونتوری رو ببینم، یه مدل سوپروایزر براش گذاشتم که بالای سر پلنر باشه و تصمیماتش رو هدایت کنه، بهش حمله کردن و دفاع کردن مقابل…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5426" target="_blank">📅 19:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Aq8IFChWo8Wu3YDbBJCZ6ea8cqL6ziWNN_bHI9XiI9Y_DT-WXF7zzO3tOnpsCi0pZBUljwpVDSVYCX49G2oMU3tE_vEwL3mOmUdI70Ls6urlDFUD08aCi2JP33Wgh909Dk3HsqjJv4jdV9i2a8r1z75m6j4qnEuJ7JchOV1fQgc8s_Sb2lJK7COcfRDNK78J1treqpfpC51OgwmPIuqyQQ--kW_7LCiMr0NmL4yyWxY_bsRPuzo0ROuqofdJ-n696XgPFIm7_2NM_oFJPgWEMrg7qiEkL-k9yrn2trmecGQ5tb2s1dflc_mm6S6vdouz-em_QhxdiTmO9rQISxGScw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستیار جدید ماریسا مایر فقط از روی عکس‌های گوشیت می‌فهمه کی هستی
ماریسا مایر، مدیرعامل سابق یاهو، بعد از راند ۸ میلیون دلاریِ seed بالاخره Dazzle رو معرفی کرد:
یه دستیار AI که برخلاف Muse و Instinct، نه خبرنامه‌ات رو می‌خونه نه تقویمت رو؛ کل context از Camera Roll می‌آد. از روی عکس‌ها می‌فهمه چی دوست داری، آخرین سفرت کجا بوده و بچه‌هات به چی علاقه‌مندن.
مثلاً از عکس‌های خود مایر فهمیده خانواده‌اش escape room دوست دارن و چند جایی که نمی‌شناخته پیشنهاد داده
😂
😂
کمی ترسناکه حقیقتا
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5425" target="_blank">📅 18:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ایده بیزنس: یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال" قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط بعدش از…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5424" target="_blank">📅 17:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ایده بیزنس:
یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال"
قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار
هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط
بعدش از سودت برای تبلیغات توی کل شهر استفاده کن و دوباره پول در بیار
سرمایه‌ات که رفت بالا و بالاتر و مردم اعتماد کردن، یهو پول رو بردار و دفترات رو هم جمع کن و فرار کن، همه چیز رو هم بنداز گردن بانک مرکزی و فرار کن د برو که رفتیم</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5423" target="_blank">📅 17:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">در مورد آزمون تورینگ و مقاله‌ی Computing Machinery and Intelligence سرچ کنید و بخونید. جالبه. با اینکه انتقادهای بسیاری بهش وارده که دوست دارم یه روز بشینیم با هم صحبت کنیم راجبش
و دقیقا پرسشیه که اوایل سریال West world مطرح میشه.
"If you can't say I'm human or robot, does it even matter anymore to ask this?"</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5422" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یه جورایی حس مور مور میده ویدئو
از شدت پیشرفت علم کامپیوتر، اینترنت، ai و...</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5421" target="_blank">📅 14:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=GauyU0fpQYHhFKBTbpxmJOL2vtKgBOUETS56O2pdHdzGWb7ig98eCm7zNdrBX3Gi2jeXCW_d_YuBVkp2TTXD9O4LUy5gbZ3QXcVL_sUhTiKZxno5d0edq-dKP9uopCvb_L2rnrpMZTRrhfVVlj00TxS00dJOxNtGLf-kqCEbw2AXb4nvRVv8JH9NyWMJ_Hvd7S0zqmSzBZUt6yVSjvHc2uzhEzMsV2Av3-uv9mWLmvuqStgvwDr61IY6rDyQeDL3yObLO1uEBFdyQi-vKSY5JuQwvzpJAryYpvFCcZzZw0d-PJgXzUPTjXWWER8TNwU2USQCbfMi2NaplmmIgJdeLw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=GauyU0fpQYHhFKBTbpxmJOL2vtKgBOUETS56O2pdHdzGWb7ig98eCm7zNdrBX3Gi2jeXCW_d_YuBVkp2TTXD9O4LUy5gbZ3QXcVL_sUhTiKZxno5d0edq-dKP9uopCvb_L2rnrpMZTRrhfVVlj00TxS00dJOxNtGLf-kqCEbw2AXb4nvRVv8JH9NyWMJ_Hvd7S0zqmSzBZUt6yVSjvHc2uzhEzMsV2Av3-uv9mWLmvuqStgvwDr61IY6rDyQeDL3yObLO1uEBFdyQi-vKSY5JuQwvzpJAryYpvFCcZzZw0d-PJgXzUPTjXWWER8TNwU2USQCbfMi2NaplmmIgJdeLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«کلاد ساننت 5.5 این رو ساخت. فقط با کد»
این داداشمون
این ویدئو رو توییت کرده و اینطور گفته
ویدئو در مورد پرسشیه که آلن تورینگ، پدر علوم کامپیوتر مدرن و هوش مصنوعی چهار سال قبل از مرگش مطرح کرد:
- آیا ماشین‌ها می‌تونن «فکر» کنن؟
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5420" target="_blank">📅 13:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=pneEHFCXjCS3cVQuHm0VdX18kLL8aZNiPyOUVO2QY3O62VAX13fI7okhpGpP0NwMKnc4znNXplnAwKuj5HRQvnAo-jXV-9fRhMo6kDWc3ZV1dcz4pZFiQhGmVlyJSKSqpXbQabGyFutYZx5sLVA96jXP7RelAtGCy-DVYzv7zps_BbKP6fqu-pB85UAqzCAxLJ5_n_yhKSmouab5dyz5d326kIXXlZozZi9tqsPvJBXfpNP_tAHtha8iEri6SXjn45ePb90CS-lSySwtP5f5zOFfxMXAasjfSDTrLNd6ElEUiWu4xsMK1PgJNm1-jIUB7YXeH0r_wm8r8i-lfxQ1KA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=pneEHFCXjCS3cVQuHm0VdX18kLL8aZNiPyOUVO2QY3O62VAX13fI7okhpGpP0NwMKnc4znNXplnAwKuj5HRQvnAo-jXV-9fRhMo6kDWc3ZV1dcz4pZFiQhGmVlyJSKSqpXbQabGyFutYZx5sLVA96jXP7RelAtGCy-DVYzv7zps_BbKP6fqu-pB85UAqzCAxLJ5_n_yhKSmouab5dyz5d326kIXXlZozZi9tqsPvJBXfpNP_tAHtha8iEri6SXjn45ePb90CS-lSySwtP5f5zOFfxMXAasjfSDTrLNd6ElEUiWu4xsMK1PgJNm1-jIUB7YXeH0r_wm8r8i-lfxQ1KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Claude sonnet ۵.۵ توی بنچمارک Terminal-Bench 4.0 نمره‌ی ۷۰.۶٪ گرفت.
بعد این پرامپت معروف بهش داده شد:
«یه کد به HTML بنویس که یه انیمیشن دوبعدی از یه پلیکان سوار دوچرخه رو با گرافیک SVG نمایش بده. نیازی به تست اضافی نیست.»
توی حالت xhigh: یه SVG سالم توی ۴۱ ثانیه، به قیمت ۰.۰۵۷ دلار.
اما توی حالت max: تمام ۱۲۸ هزار توکن خروجی کاملا خرجِ فکر کردن شد، ۱.۲۸ دلار سوخت، و SVG‌ای هم در نیومد.
گاهی سطح Effort/Reasoning بیشتر، فقط یعنی «شکست» با هزینه‌ی بیشتر.
پس الکی درجه‌ی Effort رو بالا نذارید. برای مدلهایی مثل sonnet، همون High-medium کافیه واقعا
🔗
‌
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5419" target="_blank">📅 12:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qJVwfeqLUGVT4VUMKpjntuQclYShv7eR5C0QgHm93PYitNzY7mAlO_sm_knWZMeGGm3fNP9hIEoH8HZ4jVCVtZgBYlR7swNcTUvdW5UvfcfNDE7FAw2hbjnJQGSsEQ-Gf4J4kUkUak_EjHvn9ODOAkLZdwMbC-tjTFOoNraFJ4hqc52K_d7CyncFWYS9SeoE4NEFW2SkN7NUsFd-XHPcrgLZQpOgObMH5qo8yKJRCeEnbSzeAnYL9maUiUUSHtta1UfCOJSDgh8EjdqUQChd76VTrRKIEqvdT-_kSiXvxfNT5mQRA_irGc8sAb7ukmtHwL88bUqnSpWJzkWAGqyCqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RrMvRmybsUcKniLTJCneCXtYZ3jHIEFNsTWkHNINuDyoiug7XbqpRqgr1mW5KHfY00COLqco83T-MjqcCorJiVFFggpWu9DYdj8LlKh1usq7z-eaJQ96qYRHsel2qngEQWOKbjVlG0v2mxE41cOrruf3lLJdE4EX95ZpbX5HrUAcT5ImQacCTTVNAFK6iULBxeKJB4r_zGiWMNNx-yMA-yYU7dvCzgD__34lPCmXpP3iJnRvIWYsSVLCX2BuCPfBeVgTLm0x5RnJ1Jjul4zuLQCtUO4We9yV-tJ564nUCinmmBrU09EF7hQ6wsYNd-o5GPb_9gYXxxu1jAtZCrmRMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این نسخه از WhiteVPN می‌تونید مشکل فیلترینگ ورکر رو دور بزنید</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5417" target="_blank">📅 10:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5414">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5414" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ryNfuO1PROzf9cecyJ9YjYDajFYXz7VixFvuXz3AfdkgfiB2I5ovEmhOIonVziWb5XWQrv6_Ua532XKFf8liCA59T09Wq4Bkl6etQYF6HoUOj-0rE7okFoj0JhjXAhPIFF0CMWJ5PcfmMUHlmL7bFFtcKYQYWc77wCA_Zm79CFsM5ssF5vnFAuEACIgaQzW7XpVAaSF-F0Ro358ZdSkph6iJv_hzedrE9uG71PVpqY6usFu6m_FcguGfdYszv4oeERhzGjUKRO6ai-7Y2eSmLIuq-QEnHR5jZYd_GqTJ8O1t2DKz4vMmtsUBCQvDUFueZqzr234c5tvDQUgrJwMlhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5413" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jZZFUwdi-kSEqVHTZOOP9ZhVtzEhO9VCOsEiGpb6M4TJHJ2EsX-bNbI266X-KSGSWAp8rZ6j_dqukSlU8UcJDeDdcRXIUX1UF7u38Fo49vIR3neSkdNy-x9u8-PXdk6HAZcZ56-l7fNU0YeZAya4Lxa8xcliF_vD1ovB5Wr8mGxGB9gGhs6xyWY6l0m4s518JkRD1BukgmSzkNEhSf7VOzrLDOMxLqK0os-l0ouf9BNzyDzemi3cUNnWLm3QWu5xgovq1L7i-jL4I9Dh7EB4Ks5_UEZzlP02KYmAg78LhzZKkaSn5C2_JpHbtNJOuv2Ap8CmJvMkQZUDSMVozRRfOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10
اسکیل برتر OpenCode
جامعه کاربری OpenCode فهرستی از ۱۰ ریپوی برتر Skillها برای ایجنت‌های کدنویسی جمع کردن که شامل پکیج‌های اتوماسیون تست، دیباگ خودکار و سینک شدن با دیتابیس که کار روزمره دولوپرها رو خیلی سریع‌تر و روون‌تر می‌کنه.
(حواستون به SuperPowers باشه که خیلی توکن می‌بره)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5412" target="_blank">📅 07:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">Matin SenPai
pinned «
اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید: https://youtu.be/dQKfkXnThCE  به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5411" target="_blank">📅 03:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LGO4ljrqank1_oPcr6S4EomFEVPvIJr1XYVeRw5GH98oW_HgMGUoNf8AkzfoivGwNJkvbc6zO-F4b70CoJucs03KMlY2yIIMp5Ckp9B-67CkkbdC1jSHNM4x5Ipg60Qs2Q3BJhhGhEkxOgWReKOHk1IyTs3FScVM1ev3yyvudA9s6_Huzi2kgo0DTNrAIlj0rETREjod2aCm8-tA0pTNt_MVR9cf7ahB787nVRHfynrCLfqN-RK8x9h98sQhLUazZHmIM3-Y_QbzfYxbUVz3kCsxznvAYpBsXavIYJyjSfu5Rph2i5Swzig63AVUkTxQNJFPOGkzwSjy9XoNE_aX6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5410" target="_blank">📅 03:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tv8XxVMfjAbC81ZFTi_1bBuMGUF7EAhfC07Xmdnbx4JR7S5Bma-zMLVwZlib5_ak-Di1wIca4LzPPOw2jWEAv9gBxYEYKwvBNAm16o4jdKhFuJJYVIeIH-5k7w1QCSPLXxP0PYSc6YftEPU15epGAuYn46EE53OH8GgagmUAPcUF3UtvQhXuq39MnsZzAHvMnTa1d2xx7-AANjiJIdDZdbQ2lVpqIDzcBXGSy1Uc8Ex_nDRxA3PDUOr58TGZgTL1P-hBsK_WDeuu55p-PzRF7I81Z_0TcxS-xVW-WRNK4yTVLy0ZnXJDO1CBKLOUWaGaycMkCcBN_Dwyc65BBB_gIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5409" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">هرمس خوبیش اینه که سمجه. اگر از ترکیب هرمس + مدل رایگان(مثل mimo) استفاده کنید، واقعا غصه‌ی توکن سوزی یا انجام کارهای سختتون رو ندارید</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5408" target="_blank">📅 23:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مدل Claude Sonnet 5.5 معرفی شد. هم قیمت با GPT-6 Sol، اما به شدت قدرتمندتر! نزدیک به Opus 5.5  • $2/M input • $10/M output • $0.20/M cache reads 1M context + 128K max output
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5407" target="_blank">📅 23:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NaXBchIBwT2MshxVGRvyer_xtkHi8xpz4JVkvI-gYE554KWLahN9NCFUZS2sc7bw2NV6uh4Zvp85PMU57bbj5NZrSSQmPTSi9Uh72Om58hxPSDLj8gqIphhgjgcARoXI6nIwJZJtsjm5b1s6ssGWQhy7RmjP2j4fKNho70Zu2XeMjOPAPzR0tp9dlx9kO1vwKmsC4_SLJQPtTodWGlu8EdE-GNEHRH_AYZFxQRH7nAru5RfttPbo4Lp876it--ktd51_70H5diwdpjgTiY-n1f2lql4My_vRFhi1ChY5MpDIMZ4KnchtW8UNVJT_QWpba5XHu87Dy4A4Q0CnMmDzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RHV1izdeLb1NWABpscDvT08BGcl4PXDG-2yg-wdbje2uRLwdaik7MNwtjOb27-3fD0MLvvfp2uZLI0O2or6gdJ2zh9a7r1sl1eCouhI7iqqa2_T-Qd7slrFZLiEMY-yZES1SBkO8roJ-VqknXjUH67YaM8q4qMEdoWEmAy36QvNwpPACF8HCu1BKnHSKCbZEU8y9UAJHJeOUIcrQ4L5Xuy5PIHrzvQMqpM5_9zYfFRp_zXurPJCGVr1ZCMW_1HoQdx-3tEUNUUTNkgA2vMlv87nsFxv1RuvM8uqXm8cs2yiZhcxOPYadXJgLe_GK-PJB4mPCluZeEcRfkouo1FE3KQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5405" target="_blank">📅 22:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5  از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.  هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید. https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5404" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82410567b8.mp4?token=PaAFN-8yxFHDrXD-XH6HLuJXVYuZQiFc0Jx2V269Al52hthVf8cEO6Mn6XOufwaAO5wf5HSHG0YSEVavCno4bZuC7qjSDILMBB7UQduiLg6Q0PLCFQ-uI_eqWlPWQKOLGTDUaP9JLdkVDEXwMJEMGgh946NKVVdCXs4l23sOCYrMyAsNovux4DCJL-HO2dhfv8QnF1nrgv9yfnjFu0QpQSOrpZs1myp8QpRYcD3Br5atlsdeILkDcoSG3uvNQlcO4WhbhQWFuD_BUA6ClUKL9f_WJ7hEoHNUC367lZ6lELa42SWipeeR03_decAcZyly3jR7Lt2bWGYEmBLsLYQHrg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82410567b8.mp4?token=PaAFN-8yxFHDrXD-XH6HLuJXVYuZQiFc0Jx2V269Al52hthVf8cEO6Mn6XOufwaAO5wf5HSHG0YSEVavCno4bZuC7qjSDILMBB7UQduiLg6Q0PLCFQ-uI_eqWlPWQKOLGTDUaP9JLdkVDEXwMJEMGgh946NKVVdCXs4l23sOCYrMyAsNovux4DCJL-HO2dhfv8QnF1nrgv9yfnjFu0QpQSOrpZs1myp8QpRYcD3Br5atlsdeILkDcoSG3uvNQlcO4WhbhQWFuD_BUA6ClUKL9f_WJ7hEoHNUC367lZ6lELa42SWipeeR03_decAcZyly3jR7Lt2bWGYEmBLsLYQHrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5
از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.
هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید.
https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5403" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید:
https://youtu.be/dQKfkXnThCE
به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5402" target="_blank">📅 19:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fV1_1DiBQFVBgSY7RsqPMy1J6xqpuLvHtyld9dkMu-zJqVkzM4k0K-e9LxwB9X1UuzY89w8xY7wst_5RuYRI20pjoY7zlqQbDUdA3JaONtp_biuSyOx6-p-GIbi9kHu1GyIcJwXYIzrmgtKnEiApTdUWkcQ4CgoBHkTkDi6VU1GcBotVTBirPPQM0mpCPO_pUr7wcJ_TZErMzj7lxNvQdNpkRNDwOS_PWcLle4ePN-LWYY2lIKI5jh0AWlCghqCkNY9c0uwf9cebVz287R-R_Ei4yD0BmilPhnIaMwIdLHNADkO5Z3xSqjlmmqn55Vpuc18lW_fd1WaZxsdKY7Mo9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه‌ی Hermes: از
MEMORY.md
متنی تا گراف دانش
نویسنده این پست ردیت گفته بودش که مثل خیلی‌ها به دیوار
MEMORY.md
دو هزار و دویست کاراکتری خورده بود (۹۹٪ پر و مدام درگیر نوشته‌های کهنه‌ی توی کانتکست). پس برای همین تصمیم گرفت plugin مربوط به ارائه‌دهنده‌ی حافظه‌ی Hindsight رو توی یه کانتینر Docker جدا راه بندازه؛ بعد از کلی تنظیمات مختلف، اولین اجرا و تجمیع گراف تموم شد.
که این باعث میشه:
1- دیگه محدودیت
Memory.md
رو نداشته باشیم
2- سرعت خوندن از حافظه وحشتناک بالا بره
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5401" target="_blank">📅 19:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EEvsNUgJAI71IKA6lbhCJMXhYXFkF3hTAUmY_8ZWU86CHl_UguMDewCrF-bduTpEfEetnZzD9yYZsZdwR70dvfDxgCbZ5T6lEElSkWqq9bm1K8Cn_c1q5Ek-dPs3zg3GrAOsKQYFp2u8jmX6oDqK5GwNpYqohtW6dpb-0rDltbdej7mrFHMTwaTvfANcYVXYwrfs_sKAa4UaCXv4PehQnTai7l8CeJeujLi0tq3N6ZAIGINHG8vleLdcFcVqYK3YwQKBtdngaI1X03pDjH42xb_lNXjEhwP09XiffqsHkfp214PyMtzD2jqZeS--H9axjbEnqHL6oPNwtz5pWrVuVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر کنم گوگل چند صد میلیارد توکن از نسخه 4.6 ساننت و اوپوس خریده برای Antigravity و نمیدونه باید باهاش چیکار کنه
😂
مشتی 5.5 اومد 6 هم به زودی میاد ولمون کن دیگه</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5400" target="_blank">📅 18:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pgme-Dp9fMEP0tvcfdJldf1R2BW6rwpm-gd0T4DonQljLifX2PB4Ffh1oWokiUIk08cnZNyjRbf2n_uCF0z9ShTyTVVGmnYiTqx5TyZY3KXqxCxC9Ie-YUwLgX18jS5ZQvD9_cs6sjZEu_M85nVgCGbqk-1jxLkFoj97OWJScxzyguoX6LdsTU9C9Dho8Ntj0S218KDbrri0Nkuhb8U4d0BSdMuCnqDQEjVLA_lizpH1527Ix5KoAmyp69v1olnEaV_uG44D3OcTHWwJYmI8rZB63vaT5A4gxFisHyBSrL9xusLNChI1-Fs0GDekyoQNR4sFJL6X4O-AXufPL_ZVJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی ساخت نرم‌افزار رو آسون کرد، دیده شدن رو سخت‌تر
قبل از AI برای ساختن به توسعه‌دهنده نیاز بود؛ حالا آدم‌های بیشتری همون چیز رو راحت می‌سازن. ولی تعداد کسایی که حاضرن پول بدن، یهو چند برابر نشده. نتیجه: وقتی ساختن برای همه ارزون می‌شه، مزیت واقعی از ساختن می‌ره سمت توزیع، ایده و شناخت مشتری.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5399" target="_blank">📅 17:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kDMbwQ6rC6AXdMtWwKymCw8Zxh_9znkBbTOTfKhy5eySW1WjtCyA87wSkSM-Bue87uw0ySGgTsCpbSUXKyZR34IfunCGPmM_BR6t31AbOhQ-h-ouYiYJGs0ShUJoOLIS80yBrH93137kMerie2PAniRph2a_KDatFrVUg2rUHuazIsAkpI-UZiOlLz974ijiXGreDK70IpZuSiNVk5DAArWzmBulYStOR5s91G9px3QyP8VDjLa2VZZuivR3Vm0rFIgpu2gr94xSMazyYbDRh6yzB63LyACB-DqnOy1V0pHEpT1nOog3-EByc_ghWkGDiXE0_OjHh_dmYFwX0XA-mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lpCZ2IKBJ_Qz5y-ThihULDTcJk91TiyO430XFS_LtZWTMdpg0FiAzl4A1yX5n355ozvREkksqwNQkdsCb2E5xj_neGm_7UzadbAj5p5244EOWwme8p82Hhi3YpNomYsKAK0WGD2MbIAgeRFkxFfyxkKI74mGRlrU7eE9lcr55bgRQq_0qyUZclps54-totYHuvzTB6wxcF2IoRD6w8S1odDxWVUTjVPSl-Vo4XbsQGOLCsNVgnkMo2OZ6Fw6hNGpDK9RWiaox6QRR79d4g2ZHUNXpR5AXR8v7rnU7rDTV1ZUEx8TgoD2lrdRSisUpRoXMPBlKC43FsczIvJZMAE2lQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این فتوشاپ اوپن سورس که مسخره‌اش کردن یه دوره، سازندش اومد توی ردیت درآمدشو از دونیت‌هاش گذاشت و گفت محصولم خیلی پرطرفدار شده
😂
لینک این فتوشاپ اوپن سورس که اسمش Photon هست:
https://tenzen.studio/photon
لینک پست ردیت:
https://www.reddit.com/r/SaaS/comments/1wsac6d/i_replaced_adobe_photoshop_with_a_free_better/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5397" target="_blank">📅 17:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست
با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5396" target="_blank">📅 16:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/MatinSenPaii/5395" target="_blank">📅 16:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rgr4Ez9JNN9a5fBfqFKBv69ophaXevJ5PSfkJVuvY9UriR6PUnK-RTnmfBWCjztVwmc08TmH2YEYexyJv1Rjd5rKwWG6tGQPTZowXW3GisM4zwxZIIShtriGsPrVa6jorD1vNJ37Y6HZhBemBTSbtUVjrO_PJ7p3W3ftCoDIIwKJnGIPayH3Lp5K8YL2yopuTZQL7_TJSpTUQ3izIS9zd9sQOP_wEr_ooNFFIoVZOmPe9dYocFKDeHFtzaJZtuOY2tJVN7gfmDDjJ18veK9toHEZw7ohOc7rvjizRnsgng15WWAOdB2srqrNmKM3d53pAjjwcTW8QZyZxfi7cLCD6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5394" target="_blank">📅 15:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xffn4j_syiwcAzXoY3AVKXLGzwjQ0mqoWB2CqSyti8FOxWXn5sfpyfgOjLRQYcA61NGnB7e3yje1--pJywYFOspYCVvVEG-tAnr2F1hzdoh58N7OaWBDe3vmS8RSQ3svX2VRig5zkUiZaLcjskXkZOgJzHaFVGBIOrRxADSn_quOnAS9YuUeYtYfuPiA46_kCEZQytD_uw1_7zwEWRKkzVxVxLfD0sYPxgitv1hHHdo0CZGyH3xodLApcGVjpICe9s12mbLQx75JilOPlRGQQJU9GINRdbOoZLuWIR4OdWMBPmqdszGDF669TOr93f9CT9XFoEdeB_9MnqcrZ0KTeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک خسته‌کننده نمی‌خواید؟ بشینید جنگ مدلها رو ببینید
🤣
سایت TinyAIArena یه صفحه‌ی ۸×۸ هست که چهار مدل توش دارن واقعی با هم می‌جنگن؛ نه یه جدول امتیاز خشک و خالی. روی هر مچ کلیک کنی می‌تونی تماشاشون کنی و ببینی بالاخره کدوم‌شون باهوش‌تره. کل پروژه هم روی GitHub عمومیه. البته این صرفا سرگرمیه و جدی نیست، اما همچنان برای دیدن اینکه مدل‌ها توی یه محیط محدود چیکار می‌کنن بامزست.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5393" target="_blank">📅 07:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">قضیه‌ی «انسان در حلقه» خودش داره از دور خارج میشه
مارگارت مچل و همکاراش توی یه مقاله استدلال می‌کنن که راه‌حل «انسان رو نگه داریم وسط کار» توی عصر AI، اون‌قدرها هم ساده نیست:
هم طراحی فعلی ایجنت‌ها نظارت مؤثر رو سخت می‌کنه، هم استفاده‌ی طولانی مدت از همین ابزارها، توانایی‌های شناختی خودِ ناظر انسانی رو هم کم‌کم از کار می‌اندازه. پیشنهادشون اینه که نیازهای ناظر رو به‌اندازه‌ی توانایی خودِ ایجنت جدی بگیریم؛ تا هم توی طراحی محصول و هم قضاوت انتقادی تمرین کنه، و هم توی سازمان‌ها با پروتکل‌هایی که اثر اتوماسیون رو جبران کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5392" target="_blank">📅 23:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5391" target="_blank">📅 23:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سندباکس‌های ابری Docker برای ایجنت‌های کدنویسی
داکر سرویس Cloud Sandboxes رو منتشر کرده: محیط‌های اجرای امن و میزبانی‌شده روی زیرساخت خودش، با ایزوله‌سازی microVM توی سطح سخت‌افزار. با یه دستور میشه سندباکس رو بین لپ‌تاپ و سرور جابه‌جا کنیم طوری که فایل‌سیستمش هم منتقل بشه؛ یعنی کار رو محلی شروع کنیم و قبل از خاموش کردن لپ‌تاپ بسپاریمش به کلود. هدف، ایجنت‌هاییه که ساعت‌ها کار می‌کنن و می‌خوایم چندتاشون موازی پیش برن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5390" target="_blank">📅 22:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5389" target="_blank">📅 16:40 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
