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
<img src="https://cdn1.telesco.pe/file/uAj2DTXDjAe4pRFL24yBkLMkxRmUc2UWoYthDhPYXSFTZcAJTe3Zb1HcmiLJHYAkIJLXZxRCpL0u0oLzeAdfi6iJ-vrnfB6atwwWWwI5A0c2wda5HqcEPcCa8VPqgrzirRZQL4CS7fwjTm3C9f_2DeR7Fp7BZbRJJVEG6CgUlEoEg0QGnbbL2CiwAEYJ2916EdZ2RqRM2L0mNzw5X83ExOKqSSNJ-uk09hnrUpm9TruHAtDQBc6EpRFhl5BwxHUD2bFXAknvgsilxJ1ryZ_c45TDVa9_TMts_V1TqUFudfhmdFvCb6tZd9IHFJMtVcx2YbierMI6Nj_htRbkF80Jfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)ارتباط با من:https://linktr.ee/matinsenpai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 02:51:37</div>
<hr>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اگر سیمکارت همراه اول دارید هرچه سریعتر از پنجره بندازیدش بیرون. اعصابمو به هم ریخت دیگه فیلترینگ روی همراه اول</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/MatinSenPaii/5509" target="_blank">📅 01:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سه تا ویدئو ضبط کردم واسه AI اما اصلا حتی دلم نمی‌خواد بفرستمش برای ادیتور. خیلی وضعیت نت زده توی ذوقم
الان اینطوریم که خب من آموزش بدم، کی می‌تونه اجرا کنه اصلا</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/MatinSenPaii/5508" target="_blank">📅 00:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">متد یوسف قبادی</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/MatinSenPaii/5507" target="_blank">📅 20:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">Fragment
🪦</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/MatinSenPaii/5506" target="_blank">📅 20:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حساب رسمی مایکروسافت در ایکس با بیش از ۱۳ میلیون دنبال‌کننده هک شد</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/5505" target="_blank">📅 18:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c5F28ZiOTnrq6c6WpAm3TCPk30QpeQaVqLuZFvj8g4BKO2O-0RswpJE-WtuKgb_YtlGy8WuIQbsK2v7NnJe5MQDVkA0u_tO6006y-92xAgTUY18v_vsxjs8cvhj_20mt1ekl8bsDk7nUEUhoIwNzjxsbFla-QBudmqKFHrxcXuha8z-24nrPGNr5EnDO6jrwbkKPnuL0xJ2N14HE6TG01TbAx6sq5fcqHDtoFgWbbmiKHKNAchPCOmKyuC_Hpb64hoAMILXpkveSUXxFZ0M4Whh_BJJzeinwmihn9T4ECuZ3vro_XseE5RPbsDn97gHkS39cdOYreVW6KobAZvzC4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Ling 3.1 Flash روی Cline تا ده روزِ آینده رایگانه</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5504" target="_blank">📅 16:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">استارلینک توی ایتالیا با کمک اپراتور fastweb سرویس direct to cell رو تست کرده. توی سرویس direct to cell شما میتونید با یه گوشی معمولی نسل ۴ به استارلینک وصل بشید. مثل یه اپراتور معمولی موبایل. توی حالت عادی وقتی آنتن موبایل وجود داره، گوشی به همون شبکه زمینی…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5503" target="_blank">📅 16:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5502" target="_blank">📅 15:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">امروز روز آپدیت بود
دیگه تموم شد فعلا خدا رو شکر
🥸</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5501" target="_blank">📅 13:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5500" target="_blank">📅 13:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ELIJ5qOlI0U8Yd3DDhZ18bsRhXcRfieKc-hGF6pQRUbo8oFPO1m7wRmawZiAgiXa-MH5IKUFEghDcWTSgVLtUy4Ya6HD1cY0JF5H-0hnqwIXtY_mJc0jvJZInAYeAGLtzG5Is2IKIZHE9k2Lvce8Zxnc0zSap6nOx44UqKl4kE2YkL7Id_NoW0qdmSMUNXmsrQVKtgMZLr2lDFQBKJNepYy-yDODL8iNMPBayTx-2s12Ucz9KA0sc9ATRPjCf0HaI0WvL3p4HHH3PNUbx6qDayrmyTJPmJ5oT_-SazhLx6PesTPN2aPPWuRGmNPvI_8CWWdhQ6jdlvOYeU0ywP8OQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ری استریم رو هم اوکی کردم، به زودی میریم لایو، روی یوتوب
🤠</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/5499" target="_blank">📅 13:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5498" target="_blank">📅 12:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E7iUKNCqcb8Kz9O6h_DrYzx7HmH-YnM5rcAvBsxKbPBqaXgu2GpCrpTWMLL0IEy57EitKndZ1oE8yBqEGIkFRD7bV1YJ2N0wN9s0h64bVZBM-uT8K2u5qrzpKM5BkACNV7IWZ2G39fFi1ng-45nivr_OSo7Oktc_BiutVe3Gadqy21FVqc2ZhkkkKOAyTW4nqEbJEi5GP0Z13sZDMLxA3CMN61TuHFq0O7hOmtxCm0Y4e2cE_jWAxa53E6TvSPh1CwSNzYR0KeNSNlctFCESAQpNKJKfVeyMJJz3w6LvqfeSUVmJFUp4BSCyEEhncWE65DcYOBleBknFKdAaJZ4T7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایجنت گفت تمومه، دیتابیس قبول نداشت!
مایکروسافت با همکاری هاگینگ‌فیس بنچمارک ThinkingBox رو منتشر کرده که ایجنت‌های هوش مصنوعی رو نه از روی حرف‌هاشون، بلکه از روی ردپایی که تو دیتابیس و state نهایی می‌ذارن نمره می‌ده. مثالش بامزه‌ست: ایجنت ۹ تا تول‌کال تمیز می‌زنه ولی تیکت مشتری رو بدون حل واقعی می‌بنده. این بنچمارک ۵۰۷ ورک‌فلو واقعی کسب‌وکاری رو هر کدوم ۲۰ بار با مدل‌های مختلف اجرا می‌کنه تا معلوم بشه کدوم ایجنت واقعاً قابل اعتماده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5497" target="_blank">📅 11:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity https://github.com/MatinSenPai/Gemini-Config-Checker  " دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید: https://t.me/MatinSenPaii/2881 "  کانفیگ‌های…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5496" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pLNTP3CLimk4P4AcYkafJI_TqOP0BgvaKVYhZqTmXeK9bZZMRldyfY0WVx4Vhb9hSs5Zy0lOW5tiyqRFMLFdxmqDg6DQZ1q-mtkzeho8PrT9TgyQeweeKkRgLKtaPhC5ZfsvX_eqyv_TXFGBMSMhYjEPnuysUQB6sW_71_1ya81G3YXPKIozYVgik-z3f1Ov5Ylm2dDg9qoHJU3hMxHm83xGy1Wd3BrFoczIFi6mnxWUMMvBmgBs7OEdhwQyR-qd_ofNgGOR8InnMuHyzBQC4RCiXEOQ-WgTO5ucfJ543ZQmCciWj39hWG8AhcSDCuGBmraCMTw7sbsr3d96Sk4cWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5495" target="_blank">📅 22:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5494" target="_blank">📅 22:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">وقتی یه مدل رایگان لوکال پیدا کردی و پروژه رو باهاش می‌بری جلو...
@Linuxor</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/5493" target="_blank">📅 22:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/exSOSKOqie6fSaCdhgcWZPyp_linVUmVCACLDmEs4XrFQKEbryJJAGUEfBcwwhDAmJL28fy_Rxt7MkoRPauiozb5fM2OjKZpJjCy1BgnPHASu6O3bP8ERynczqkm2Gm3AzIqBDcOOIoHkPBvYTSS6wi1SujPq3smhFBN7ops68nChhT_SXJ9XLhqfWv_v-ePn-7dr6Vk2PcAhmFJSZ91AFSJoSOzyB2MT-MHFJXUO_TyIKjTQAJljC_VW7-knB0Qdx1MinJwyzRtYq0Yww6cHP2WXlBAjam5lvx6RhVlEel4jZraWyPDGxvjve3paOxMdaUPRbXMKbzyuDt7NQz3Zw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5492" target="_blank">📅 19:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=LxOOzPTDgpkFcatdWyRXFxONRpww8JHZ6djtTyLcO6swUnY0UhdPONj425rdHte7A7RAB_y_AOwaUoPvc4oHTm9dfoWt3ZTHHq5IZt5yP_Fyepd_Pv6aOSl7-69f5BRi9F3hLd2pJ4copyZi18Jc9J8-Jf9lhN2J0E2mkadyCFFZ8zD3PKfqrNPyoRCJi4mjWkCSTL8xi_xJ7HhQRz7a7ilkRbVFbLXmY62y3_LucIauPEDuY4a81lEjOGoiNe1tqxRRJrgKeHzdtGTzCEmaqRJVX-Kvp2282eGtyemUyEgfp3RISSXPvXHDqdjmMzNU0GpiSFbfkNBwIcNzS7z-1g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=LxOOzPTDgpkFcatdWyRXFxONRpww8JHZ6djtTyLcO6swUnY0UhdPONj425rdHte7A7RAB_y_AOwaUoPvc4oHTm9dfoWt3ZTHHq5IZt5yP_Fyepd_Pv6aOSl7-69f5BRi9F3hLd2pJ4copyZi18Jc9J8-Jf9lhN2J0E2mkadyCFFZ8zD3PKfqrNPyoRCJi4mjWkCSTL8xi_xJ7HhQRz7a7ilkRbVFbLXmY62y3_LucIauPEDuY4a81lEjOGoiNe1tqxRRJrgKeHzdtGTzCEmaqRJVX-Kvp2282eGtyemUyEgfp3RISSXPvXHDqdjmMzNU0GpiSFbfkNBwIcNzS7z-1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم
سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5491" target="_blank">📅 19:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uZb8AU-rwcFEtAsIcgot_c0dfnUGBKjris347I0Of3p_29Hp0j4gmCVdH6EdzMHV_kuLbdsDju5ddY79kO6iG694D8dJK0nlgSyfzoX1FvOhp27KMZpc8d-gPZTVbNc06WwiGXSHCPRatZPglWcDOJQcSGD-a9DcUvEVUb2zmImiCYVmUkS5HMgtLtDOESRIoMOi7bRv_sJsjyMvyc9o0fb2YaBqUnkp6otG773Yjpj8Sw3SeoEbpfr1anZLNCm1BeUVNaGVCDfTUPF2dcxBVxnQm5z0QxFC1IFGbGpfoSHFtex1ZvWK5x2qsBfjK79WPQmxT0osvOR_kYOfZDlFEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/5490" target="_blank">📅 18:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ok5daQXPSiDgu2JqQEJxx3FxxBXvqOjwL8tkDxELqYoCDsMETiUetcID0JvUmW-rhyKBKaws2KvkA2vFSCp9QM-GyczD5s5htO6kP2vhxfiq9Tl2BeBsV3umGfDnQsVwXnPxfAgA2M2Oqh-W9eRNDflHP7ayGBWu0dExhS6i3mJNnNdJ30nyH5THKXnNWUWk5H1S012jA0uWSSaYzpfSZO9I3ibUmcZxMW9zbU5O3hsXEpVgu54wPiLznpz7zL6IJsqnJIKkRJHnCg_dovgCEq9suBT1KYRwFGc7mGmt2MSSiEcKfr-VI-rNOuOJPuD3o1jDZuwl0gnFb3MSlc6ZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n28PQJDTTgb0afKu4ES0jeg05No1CR_MEwSblTMRzLLM9w2_mBbWaePXqMvWtKMRDnVrQsZHWAB4u08IWcx7HXqrj_nQLtB-Hv1m6Iin7sD-rf2-JesjgyQFJnDD0xuYddX8uiHrsaehxYin5ZGmktRnzKG9JgAe1UBFL-h_SlRm8t2fJ4PVXp2Uegi1wXw_BvPAH2rTbLylcjEPwKa_7ovdUZiBUz5x0GnT5lnp8wHYjqVdC6xppqFrxYWoQl2z3dNMhQNSLp54QjYePmEZIHzrMOKjm55tGSGtVmfz8_9RjI-3_9LBtF_YwDXcgJDlUmysgicqIyvax5OTtQ2n1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5488" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5487" target="_blank">📅 14:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5486" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyvdP5-RUWX9IKFXfcXfDYnE_84jWivC9CX-UJuXMrPlHQaC3mSnWkUcmeGbk_e6hOmrI0MHwPdAogPVDOf0-IpoGsaj4Nfbtdnrv8brtmiwkBjiDMO2d4AVpPTyZnMh-3k1DhCONe8Pj71qGWEtfcubCyZ3DtUgEJOn29KWQsyhMAMs3T8A_-mK8wxHc2Ies8XIwHCWnNrZM1GoGPE2hAEDF3_JowOOcsaHi7FHx1CKGUKYxwMiS4z50tt2trQej3cz-6tEC6n6T0gPcncoExwKBAIDqtFKMezPKAXaB6KrdoAjKOalA35CMdTkw7SmO-GLoUsFJDS7KniMsUKd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان دوران بارکدهای سنتی و آغاز سلطه کدهای دوبعدی
بارکدهای تک‌بعدی خطی که ۵۰ سال پیش اولین بار روی آدامس ریگلی تست شدند، کم‌کم از بسته‌بندی‌ها حذف می‌شوند. طبق ابتکار Sunrise 2027 سازمان استانداردهای جهانی GS1، بارکدهای سنتی جایشان را به کدهای دوبعدی مانند QR Code می‌دهند که می‌توانند ۲۰۰ برابر دیتای بیشتری برای رهگیری زنجیره تامین، هشدارهای فراخوان سلامت و تاریخ انقضا در خود نگه دارند.
من هم قبلا یه ویدئوی کامل راجب داستان بارکد و اینکه چطور اختراع شد و سیستمش چطوری کار میکنه، ساختم توی یوتوب:
https://youtu.be/PAHA55mHLWs
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5485" target="_blank">📅 13:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/5483" target="_blank">📅 10:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLFQYG1Jh_qNe4APCNkM45cPsjepEdC_T8XQKVdPkHNTQF4hVsoWDD4tlqGjJLJdSjUMRbBjTk6PYc4P63HuK-zIHuiD6Kd9fyNOzr40q9Trnx8H4lme1vDAMFAOFyAPfEmYcLSExtteCk_4OUDPr8rMRBwzLe0bEc80DfPx_VnCtleWjp9I3qzxQ2QJKjwmax5eAFVPDWv2RhWb2g6VywWcP1ihXrDyLGi5XnFGMv1NRXuTuCWkKqCvpa8Dy4iEqeIB2tzYWaaqKU1Eeif0EYdMED4Zx6_9dLyJrgy1Tt_hFgGF_TQyadBL7GPzZxL8E-324OZfdrcS4TCxCNcd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل رسماً سراغ سوئیفت سمت سرور رفت
گوگل کلاینت‌لایبرری‌های Google Cloud API برای سوئیفت را منتشر کرد؛ مخصوص سوئیفت ۶.۲ به بالا با SwiftNIO، مولتی‌پلکس HTTP/2، انتقال gRPC و ایمنی race در کامپایل‌تایم. گوگل می‌گوید با کانکارنسی سخت‌گیرانه سوئیفت ۶، این زبان با ایمنی شبه‌راست و پرفورمنس قابل‌پیش‌بینی ARC برای میکروسرویس با Hummingbird و Vapor و زیرساخت ابری ایده‌آل شده.
مبارک سوئیفتیا
🎨
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5482" target="_blank">📅 09:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v6Ixo_qidMJxdgpZ_evJsfQRqMG0O8hcGnQ10qgEBnjebg-A7cPF1cb_Sm8WQv1o1YdlHLX-StXj4rUQdR3vujL5JMtZH3f82DLveHj_nWU_3M1PrGpTF2fAeh1efFZZt7CG_CsdgNlXiadypCbspX5jmjZCLmIBtOV2l8I77D6muqUUSqWDp66XQY3a7aM32X9kJVIG3JI6_d4ak97LhC0fExNv1sKtu3Mj8BH1Hz4VfVcTvWaUlawno6zx7XcLKpSCgqvinYfK5wKQJd6k81tfpQj21clZzdJb0_AV4yCQPipDMzSJiVfO1xs0hLFi1jm6NE2RzqvZoMLuaLaYCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA  من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5481" target="_blank">📅 18:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AcDkTZvRndHFv3rhUXSXKYPbEpOJte09yZ3GmT4EUwc7nbRP8PLZrazoYlVmoqtFwbOVXRkaQ75AZIuc_vYv8Ukq6_rAR4WOhysz8P2MADzbDT5FbFh_lPfyNDxJowRWE1EfD7yild4UF9mRp347-XyS0rnJam97u60VvzxUz1TQgBB9P55n8mYfmEWsBYAJnbSK7IdQmIZ1KqHFzpeheRgCcd2VovWUzXvVefhqO3D_2TaXGR4CxbQAOw3_tPib0mVL6QE8An_tvswntIaur_XjB9WQkQSFsvD03cI60hlVT3YkRSRuEC7vlVBSRnWb1Qr2zuX7YN5kkZvcv7GAnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uhtTGV80qkWpRZj1bthQvGqu2KrHZn7njStF6AGxl1ruX-Gfp1onGO6s_XEHSJcC63as8ZZVew1P6BoiEbwzjag_L1HTJjJvcqzMXU13TaSBz7S6AD-6-XxgBPIvkj383gMbIUEMIEfGt3V8Dh0TxLbZuyK_KdpyQmnM_O1EnNPAiNHA-mLxMBbZ5Byx3b_DDjCFKSRkrTPhyFcph5eWi6UJRiCnyj0Z67Lom1ucCXVCSHmyzjQk-MYYD6fJfNlSceIE_xNrr_j_CnV914znqvfoVZZRNLN29rrk8DlRfBUemAI-0hTxYGG7zYpOOuFTnLj9uRuU2Z3bB6UR71mMyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5479" target="_blank">📅 18:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dQwGIKSYGW60RoPmrp2FxdBq3ZSpGlHSFo4fguFecBsWKe96v4Pjm5GPrtJLsOj65172BUw7MNakAZB8Dz4HK-DIfIUH9eCy6BH4D4Cz9XEdgaA5OUNYwQShNb6ex-ksQ7bT493ec5VqL8oiOMzaxGkwcY3Uwk5oP7KqQrigAXgIe9mz4JhcI9wmuGUk1IfiNoAEZ2W0SoTO3TwK9E2wscVuipbYeyNs4oEs-mfu23dzAymiPQuWtkYiXwEY1VKMwfjCdWNlR-Hd-QDFIglw15AVjWXivC_s7Xc2tC0rVZzyGFMES0GB02XT9aWT0oDyq2xIuxhHAUw0lLp53OrLlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA
من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد دادم چه شکلی ازشون استفاده کنید و حتی با اینترنت ملی هم بتونید دانلودش کنید.
امیدوارم که مفید باشه واستون
❤️
دانلود Ollama:
https://ollama.com/download
📹
تماشا در یوتوب:
https://youtu.be/EAF-hMPUMYc</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5478" target="_blank">📅 18:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5477" target="_blank">📅 17:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5476" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">در کنار بلاک/فیلتر شدن دامین دریافت کلید وارپ، اومدن sni مسک (Masque) فعلا فقط h2 رو بلاک کردن :))</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5475" target="_blank">📅 13:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5474" target="_blank">📅 10:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">چطور فاصله‌ی بین Hermes و دستیارهای اختصاصی Dots و Grok رو پر کنیم؟
یکی از کاربرا توی یه راهنمای کاربردی از اکوسیستم هرمس توی ردیت، بررسی کرده که چطور می‌شه بدون نیاز به پلتفرم‌های بسته(مثل grok bot و dots و muse و...)، قابلیت‌های پیشرفته Dots و بات‌های گروک رو توی ستاپ Hermes پیاده کرد. راهکارهاش شامل لایه‌ی مسئولیت‌های موندگار (persistent responsibilities)، سیستم دیده‌بان پرواکتیو (Scout) برای وب و دیتا، مدیریت وضعیت تسک‌ها با SQLite، و تعیین سیاست‌های دسترسی قبل از اجرای ابزارهاست.
که البته خیلی از ۱۱-۱۲ تا قابلیتی که گفته همین الانش هم هست، صرفا دسترسی باید راحتتر بشه توی UX خود هرمس و به نظرم کم کم به اون سمت هم میره
👍
پستش رو توی ردیت بخونید، بد نیست:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5473" target="_blank">📅 09:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مهار دزدی و Distillation Attack مدل‌ها توسط OpenAI
شرکت OpenAI اعلام کرد یه کمپین گسترده و سازمان‌یافته برای استخراج و تقطیر (یا همون Distillation خودمون) قابلیت‌های استدلالی مدل‌های پیشرفته خودش رو متوقف کرده. گویا مهاجم‌ها با کوئری‌های پیچیده در صدد کپی‌برداری غیرمجاز از متدولوژی استدلال منطقی مدل‌ها بودن. اوپن‌ای‌آی دفاعیات و سپرهای نظارتی جدیدی رو برای شناسایی و خنثی‌سازی تریک‌های Adversarial Distillation مستقر کرده.
(ببخشید برادران چینی. راههای جدیدی پیدا کنید
😭
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5472" target="_blank">📅 01:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5471" target="_blank">📅 23:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آرنا توی این ویدئو، قدرت Gemini-4 Argon رو بیشتر توی زمینه‌ی 3D و قدرت پیاده‌سازی گیم‌ها و محیط‌های مختلف بررسی کرده
که خب کامل نیست و باید توی تسک‌های ایجنتیک و کدنویسی و بکند و... ببینیم
انگار که کلا قدرتش کمی پایینتر از GPT 6 sol هست که خب، ازم بپذیرید که قابل قبول نیست برای گوگل، اونم بعد از اینهمه غیبت کبری
توی دیزاینایی که نشون میده، قدرت Sonnet 5.5 هم می‌بینید
😂
خداست این مدل
https://www.youtube.com/watch?v=h5EL5zThKaI</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5470" target="_blank">📅 23:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jYg4MPYLR1haws8Drp7bYjVraFfRrUY6SN-LYE6I0yojczCcRT-N4gDX5ZbCp8Xz2_qNWB0WksloO1IFyYL0kpbbffGQ5o67F9EckovprLI7EQ5ItFnkcBUR4BimtsqSDggk7ctfbhQarX3RN3iLiF1Vq5REmBkr3Vae4LO8m6sVVY9hIjvnHpwo_01RFoqpxuoWTICnlnP8sCtzIS9ew7N28ny-iXQrKVVeZoaqNmX5QbtL-VWfvaeUWRtOEew_7_G2Aj1FozBuxg-p9UXWQfP3YZmj6XqXNcgFIv5nAJNYKVDZjdCU-CnYsn6aJR-cJkvjv_ZmbCZR3lPLt-jJcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5469" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2spUqyTpXt4Tfg-bZ-rXNtVKqpj51V0VeoTwbbderHQIEhxaT7H_abGxVBglOD8tRH2cv3y7GkFyaGJud3uANZhyOSU8k2g_5R43pa5hgpwT_s9DU0UqEMopfaQ7MIvH1hXUBaHZF77q2rYW45iCmUDyuxWiZ63lNcQnbZ-4EJ7z0Zs7vrUPZt-uGWVTy5mWfr0o7LJQa9GQ-gVaW5R4gL4JZFZmsuBs0pCOXsAg_0s3PDaWyi0E3c5xPQ9tcbTWhBCjPyz7suuuq0yrZIYYUYIDxzvxv0n2e0SRWgDbQvUwADzDQqaQKbvZQsXMQpl_VTHk2_FOHRU0a8GMzWRfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5468" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بزرگترین مزیتی که ایجنت‌های شرکتی(Muse, Grokbot و Dots) دارن اینه که با مدل خود کمپانی یکپارچه هستن
برای هرمس، یه کم چون دستمون توی انتخاب مدل بازه ممکنه گاهی اوقات گیج بزنه یا دو نفر با کار یکسان، تجربه‌ی متفاوتی داشته باشن
اما همچنان هرمس رو ترجیحش میدم</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5467" target="_blank">📅 19:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قراره با هم یه اپلیکیشن تمرین زبان با روش Shadowing بسازیم.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5466" target="_blank">📅 18:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/wBMQpDbLjoTrPSj8ADYMfRjp73ijKrX-gEmPHtGelACHxlbYqOEgihVZN5vcVaJteLq_oYiCCL3PtexPvociczbRN6jjB-cFNDmTE6Dcn13K6fmotorP7HWZDHd7-6pKYOvib8M0jlyWdBZ5BoLAfW_Q8Y4OoY9K7_zeaIn0ajaguZcbXGJdRe6eefIecuA0QZ1HDBWX6XmzsjRgDYV7ta7OmeaPe9HOjqTj1dlyYDjMzfdgmHOR3Omu0l4sQg8VyZjYttyuDU1zHv0MAel61Tl_p9KUnYmRjou1PZomguH5Ttdb_eAHPPtSwJkV0lYtLkEUwCPAAleYGlZnJQwmdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردیت فیدهای RSS را متوقف و دسترسی عمومی به API را مسدود می‌کند
ردیت اعلام کرد که به دلیل اسکرپ گسترده داده‌ها توسط بات‌های هوش مصنوعی، پشتیبانی از تمامی فیدهای RSS را از ۱۳ نوامبر به پایان می‌رساند. این شرکت همچنین تاریخ توقف کامل دسترسی به API عمومی را مارس ۲۰۲۷ تعیین کرده است. این تصمیم در شرایطی گرفته می‌شود که فروش داده‌های کاربران به غول‌های هوش مصنوعی به بخش پرسودی از درآمدهای ردیت تبدیل شده و این پلتفرم دسترسی رایگان را کاملا محدود می‌کند.
که خبر بدیه برای ما
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5465" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">امروز زیاد ازش استفاده کردم
گفتم یه توضیحی راجبش بدم</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5464" target="_blank">📅 18:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یکی از قابلیت‌های بامزه‌ی یوتوب، Hide user from channel هست
این شکلی که وقتی کسی کامنت دری‌وری می‌ذاره، زمانی که هاید میشه، هنوز می‌تونه کامنت بذاره، اما کامنت‌هاش رو فقط خودش می‌بینه
نه من می‌بینم
نه بقیه
اصلا هم متوجه نمیشه که هاید شده
😂</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5463" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SA1LTLvfO7E3TSBEnio7Hmwd4KK2uJU1xpATegLcxIwd8KF37PXq5wwBl0JyhHji_w2Dmp5LQKcSu1xvUwu9LDo4JjIzl_JLNkTQUnD1rozpeCn4_huXyfhJ-D3G0AsBa7mTSglZf0cwofSwzFygmwqBQUPDcsGp2EQQgbZqfIVcVMd05WGD0l8kPAoD8WxsQ5ryKRqGdgMvZqyVzts0rIQKcC6J4fBnz0YBvkV7m0gaxDSa8-d4QhRVv_nBbOLkChEFUkkAhsRWbkgyGn7cDWUyxZG7vlqwbi_4zX-klf1ZzSBMiPYxG4esn_64CY_hHkdXeQWo-P4dBElm5FuDiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5462" target="_blank">📅 18:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L1eONgDJiTrkZuxTLz8wSYRqXx0MovW9h5YaJVHLnOH3QeQEwht2V_y_-Q9x6WVArd8dAxhfElKOkucp3u8DUxlFnquEa_Z0ODYnHXj2DuC7H5OMIPhAde5ZHUGaO5qnXkePkl702fx4D4zN6X5KtFuO3e2FyeK341g7GAjJ2AmekK-NrthapCVnQw-FNVVJ1CDEz5Fg5cO4iiP7N22r_sYdBx8DHUjWyvKlzV3LOD_tiXfJNP-tOvUw4vfZm_dIQ4iHgmc-dOYQ-iuXlY9RY9n_i_wYaR-7XjSk8j1kYqQ04Em30U4WbuHizSYSPaYg_EztpQ-lFl47Y4236Wx9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Decisions API توسط OpenAI برای اتوماسیون فوق‌سریع تصمیم‌گیری در ایجنت‌ها
سم آلتمن از عرضه قابلیت جدیدی به نام Decisions API خبر داد که ساختاری مشابه مدل سریع Jev از استارتاپ TypeSafe دارد. این رابط برنامه‌نویسی به توسعه‌دهندگان اجازه می‌دهد مجموعه‌ای مشخص از گزینه‌ها را به مدل Luna بدهند تا با سرعت بسیار بالا و هزینه بسیار ناچیز، به صورت احتمالی بهترین تصمیم یا اکشن را انتخاب کند. این رویکرد به ویژه برای کنترل ازدحام ایجنت‌ها و اتوماسیون لحظه‌ای نرم‌افزارها کاربرد دارد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5461" target="_blank">📅 17:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vHuuYsfpD9KhDOo1KlDTENjlJ8v21lrE8BCcCGrHgu4Tou7ppm615Ib0MCtaGieWVZ16bBi64FAsKdDUTTQVqaHpvbaR8Z5Ou2s2rDyvQ-vpXBVLgkz0m1Dwn7MozrsxClIZC-jh_a5iXIWszNRVHocRhnreJQhES9MpkpIvel1Zob1IVu-2Esh0ftzhHhyrUXgMmiIJwkMsZBmjf4JkKagi2DXh6e80iBf3bPKOnhq83Ea6_dHPHZXY2Wv5i3k6iSS_WdCxea2uYWoKICf2V9tbdvkY0pep2rJE1DfVEFLwRaJ2Cs8VcsGPdXqTnzX2VswS0GHg34gR8ePXM3hNVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به قول Theo، چرا واقعا OpenAI هنوز داره از GPT-5.6 Sol استفاده میکنه توی چتش:))
نه تنها 6 sol اومد، بلکه 6.1 sol رو هم دادن و چت هنوز روی 5.6 گیر کرده
اولین باریه همچین چیزی رو میبینم حقیقتا بین کمپانیا</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5460" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M_iTkNdXiMMhRXrd1yEcepJHA0V5p7Fmu8QjVsGYO4oznx5A35LImQc8zrk4FaFblr_CFDTjzUr6xrwfod3H_sJs7MPuWFAM5bqqKIdmFbS8Cw_MlnHMlznhnZOgczWIelrmgb0H0b94_Fdk0NLfFdKz_o8sUgcfq8nFhDWorr8y37Wbo7IlBQrr3oo9tYdhElY2uEmSARvIvtuq5YtVvuIGQZK7RitoNs-nVbBBU4cE2CWKKlxNr3L_ld44qkGxnx-DMC7PPfQpVzVeSOQFas77DpSzbMzsh-41gv4BA2PUyQaG9J1Z63EmO2ihGKlfSwdw4sLypMeuIYiscZbCRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله ما نسل Z هستیم
😂</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5459" target="_blank">📅 12:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bfHcSf8oVsxYZuyGDsZ128QOdQMK46LxjvhqnMe3HkOXz8dII42s_yw-Mk5ztMVjKuOER4sh4MN63THwIruO3mxjusdl4sxToB7mb3JMSqolLUMR0pVjKsr4VM2ekyMf0ijNRPtQ3HMgy9kspN4-BP6VOsLz53AUbT6k9qGMhI6ao9cB8VLmX_9o5REG86ar7j1JSr2Bg_coIgBnH8A4Y7CDaOA_NqQP2mXzvsBFmKRhnzdr4ZHWvMdYvpM5D1A8FAHy-ZbvRTUsncO9vB5DAlxZHIBCC8_eNgJ-RMHRyRKpuYQ0Hm06QsZjeYJjHX_f8AQqPSVNSNsyN9weP9stbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate
توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب:
https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5458" target="_blank">📅 12:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شدیدا حس میکنم مدلهای چینی اوایل که اومدن غول بودن، بعد از عرضه یهو ضعیف شدن
مثلا هممون به Ox Alpha دسترسی داشتیم، بعدش که glm 5.3 flash معرفی شد اصلا اون هوش رو نداشت.
یا من به Qwen 3.8 preview دسترسی داشتم و خارق‌العاده بود. سرچ کنید توی چنل نوشتم از تجربیاتم. اما الان Qwen 3.8 max وقتی ریلیز شد هم از مدلهای Frontier خیلی عقبت‌تره هم توی بنچمارک و هم توی عمل</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5457" target="_blank">📅 11:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n0axfSVaEs3aCuJQ494Rbf6MmmckR4iN-h79dInHVdKug0eNq2S3nI6Fl1rbTuPxs0N4UrX6kEZ65b4o23V-8u3s9i1ndjx9xZIQnXdbc9zFKh0qt8JYiLJ42VBx-FkL95EenGKyZpda7Rh3TJCgwLciPtg_4uN8TvNVQhtnXUFf99AQyt72WITK8tllTyUVbra9Wx2U9K7WH34NyaqZ53DAu9VFtZQK321TZmNdm6eiSFMAE9QKbDD0VemE1qBh_ldGp2DOBQRXLKz3xtJ2IMkCOB0uk2rPfxxqni3ElL8iFVWfbw8wHTsHY95LPNoT9Wr3N7gJTxSjqhvHriZLiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم به نوبه‌ی خودش عالیه
Hallucination یعنی توهم زدن ai
که این یعنی جمنای 4 به ندرت از خودش یه چیزی رو در میاره</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5456" target="_blank">📅 08:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کلا هر مدلی که میاد
این قضیه‌ی Benchmaxxing پیش میاد
نگران نباشید
میگن توی کدنویسی اونقدر هم خوب نیست انگار و باید منتظر موند و دید تا فردا پس‌فردا که شایعات و تست‌ها به کجا می‌بره ما رو</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5455" target="_blank">📅 07:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YGAIfId3LAwqa5PTYbbdj_7_tgr36Q9IWbNvjTogaVBiP_yfztnj-UQuPg76thgG73EZo-sucqh5nNxbnvl0bMuKRuvII1rms2R6rAzL1SC7gvNoKj36-12dfqADVCRUbSSP6XDwUo76jm96y4JRURkGAxXlf6LOYlTZ6gb68OEzn6Dh2cLqBoLeo47mBONt6B0atNRp_xOpXOsFWGsZ-MHxJMhgF1iaM1fORl9-zf4n3TVt0ZuBZ1W-XPBsPCwWMchB7hes3kIUvCOZEdwd3Hf3VPyCvtJPi-rOT9O0wvvJN7zHT8hn3X4LI67-bpLMoyhnB8qBrbsNMxs5jYhukA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EtZi4pGlrixDdKCLDUzHqAfNPVHkQmgiFKu4NnK89IBMuJ4w7UYYm_w-c2YDKYAcTCKG4Z6CDVQi_N90O6z9wG4sDwoMcSL72nO4--_oy-cwIGwEALjy9dxzL0z-vlIypUvp3_OJ17EKTkPxzLYzI2Fg3v1otNzKLQUnedSywE9KGxcHH9glnjKFmgiIGJ4Ty8WdGgDk-u9fuJNb8dbmm7NZJ9IQaNEHRnqlhoqX5ASTGJmZzAlWuTqzA3B47xtBszEc-mBbaXl677kHaQ7Pq2EwcT2JW6btYkRBr5eNTmnUsaD82_yYEZM-VHaZeGkt7n6yuq-y7U4ueoyDPsxMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SWsio9Lg3dYErEvSPja6229BOZ4ctAW_aH9N1uPumS2LYSC8jmUIW9rsK7OvBC-t2QvfL0ulny5M0OxVKdyqL7yaeTAt0kFwFonfTWU0uz3x3N-F-KO_SgLmaqEsfvPuK5JLGYuPllZeSXjWLwf26giO_VBTGov-Ah7FhbopvuQpAEeEnJIhKxxUYPrjzsQUY-1Y4JzZmxtNz1K1ZnqnT37QZ9IFsxLv_7t2MMH42h5rvU7pE-v8XpSE7SEM53ztrlhUxEkyMbfptLr_xZ5bzQWsEE4UIYTH1MIFwr054X5bW3D6s3Y4t5htVA5Qy24NKKV9WicazUjWGEDHMVYbxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RyWyeyFhQlBVdRZ3Mo3yW-q74puup1T7aEt0iDuo7HzAAUccOm_-X0Y6hv_ZJnVCb8uVpqX1fqcDLrxpOadJKcCi-pq_k9dl53w6xzr5WX8hpTUadg5JCaf_ffag_VVQHPB-fRjPTjxzDfvlxHJ0yB8vu7R0ZvJYYFr5AaFoifeFZswAUyhztGZ0cuT1_bcSHRF3GeJLsuaJPBXtqXPo9DmcLyodbsikpPBWBEO2XEG8H61vvdIw4WvNZC3OqNyuu8dYUPhmdj9HWaA2OoUPNJxGpRYZYlbFVoCEeDrNW_538B0CvzgP2yynGz4MjFJhkPacMC3WsRSihauHAprfHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری  گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5451" target="_blank">📅 01:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=FgJvuyH5UM3idb9ikty_okS4eBQoPk2JPEhgZQBKzoiy-14neNNNzpaY4OYL-ix0dKee2D7VpdolyUwPxk9BALiRV_pCoYQiT1eau5h_Ek1LNOJQrpaA5KyReprxSp_o0da4jGexmr5wnkDfpngf1V0EZIC7zuyyOShJ6d7dFraogUJ6pb2afHnzHpjLA-HdE7Cj3XTmwsnY6x-fWkwXhbs2Dpd7W1Cy9Fhjxk7qtvrV6yyZk1FKmG0XlP2hKcohU_wdoGnSr5Vu1428v17J_rSIkVo_6-PcHBmIHqtL4fY0D3ZZCPgKtUL_LbmmBwYPm9QaPvMZDB2JHvyok6NxNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=FgJvuyH5UM3idb9ikty_okS4eBQoPk2JPEhgZQBKzoiy-14neNNNzpaY4OYL-ix0dKee2D7VpdolyUwPxk9BALiRV_pCoYQiT1eau5h_Ek1LNOJQrpaA5KyReprxSp_o0da4jGexmr5wnkDfpngf1V0EZIC7zuyyOShJ6d7dFraogUJ6pb2afHnzHpjLA-HdE7Cj3XTmwsnY6x-fWkwXhbs2Dpd7W1Cy9Fhjxk7qtvrV6yyZk1FKmG0XlP2hKcohU_wdoGnSr5Vu1428v17J_rSIkVo_6-PcHBmIHqtL4fY0D3ZZCPgKtUL_LbmmBwYPm9QaPvMZDB2JHvyok6NxNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5450" target="_blank">📅 01:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T2roRE_yD9WVoyswdz7BzWETWBA4hHMHpAV8jrXH1rLALuKK_uItKCLL13UC4jNPAm4jvTD5sVYjrv43NpNpZICcSezGeEsTzwZsJZtifKCWeND3xgmgvLFeeMykWxCBTIAsQogRiZxDU9eJGzkrmVJYSN-eXVBSKHmN4NDQLpl2bjcKqHJeW_PD20zpBy0tgTDlXMbpTD7bbXf0LgHKy3fl3QJ6Eqg2dUA5Cm58j3bf-sZRMmqcJA7H8pvuG-iw0ChDvl3HbQna8O6xtm2mTQ9TJES43oiNZusKB0lniE7ekSpmNTIrrrz2BC25-eatEsuLvspI_YxTAV9mVRzyuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5449" target="_blank">📅 01:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بیدار شید بیدار شید
جمنای 4 اومدد</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5448" target="_blank">📅 00:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CHh8QC5IH_DWrm3MKvfPj3ljYihubzfPnzU9AoRiCvXrIGeMgAsqcsFWeuLTNr9oXWjrf-4wZPPxLd2qnkIem_e5k9Oil57mqiH9Ze2X2IDffuqXhMQBCphFGcX1nd77XgtEPLZYTN5_DWTWTXGPLuhJXQJNghPBapGCntgt97BzemrlKYytW6dOo5gPG2Ch_Ooi7AvmLx8vnWtzqw3zbZJrVmpqB19EW8rScvLzdHsaLnfSnt_B77fUQlRzbzvpyMQgPPptcW9w-k1fXBEkpqWtn7d-fCr5aqPDAChbT3FCsChP-nUFVZhoyyPRCTXfZt5952x2sDY1V1y18AquEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش هزینه‌های هوش‌مصنوعی با Auto Router در Cloudflare
کلودفلر قابلیت جدید Auto Router رو به سرویس AI Gateway اضافه کرده. این سیستم توی لبه شبکه (Edge) پیچیدگی هر درخواست رو می‌سنجه و به‌صورت خودکار بهینه‌ترین مدل رو انتخاب می‌کنه؛ یعنی برای پرامپت‌های ساده مدل‌های سبک و ارزون‌تر رو صدا می‌زنه و فقط کارهای پیچیده رو به مدل‌های گرون می‌سپاره تا بدون افت کیفیت، هزینه‌های پردازش به‌شدت کم بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5447" target="_blank">📅 23:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">من معتقدم با مدلهای رایگان، مدلهای چینی و ابزارهای رایگان هم میشه به خوبی کد نوشت و ابزار ساخت
و به زودی برای اثباتش، یه سری کار انجام میدم
چون میبینم دور و اطرافم کسایی رو که هیچ کاری نمی‌کنن، تلاشی نمی‌کنن، به بهونه‌ی اینکه من اشتراک Claude یا GPT plus ندارم و...
و این کارو انجام خواهم داد که شاید انگیزه‌ای بشه، و شاید ترغیب بشن یه سری افراد که شروع کنن ایده‌هاشون رو بسازن</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5446" target="_blank">📅 21:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ویژگی‌ای که Dots و Cues و Grok Bot دارن نسبت به هرمس اینه که اومدن قابلیت‌ها رو محدود کردن!
بله درست شنیدین
همین محدود کردن قابلیت‌ها خودش فیچر خوبی بوده(برای اکثر مردم و برای مارکتینگ خودشون) و باعث شده کارهایی که میشه باهاش انجام داد ساده‌تر به نظر بیاد و سرراست تر بشه. از اون طرف، چون با LLM خودشون سازگاری صد درصد داره، به 99 درصد ارورهای مدل‌ها و api و... بر نمی‌خورید. VPS هم که نیاز ندارید دیگه
اونور قضیه، هرمس به شما "کنترل" و "هزینه صفر(روی لوکال)" میده که اون هم ارزشمنده برای قشر عظیمی</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5445" target="_blank">📅 16:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بچه‌ها ما قراره استریم داشته باشیم راجب دانشگاه و انتخاب رشته
اگر سؤالی دارید، می‌تونید به ایمیل matinsdungeon@gmail.com سؤالتون رو بفرستید با Subject استریم
روی استریم می‌خونیم سؤالاتتون و جواب می‌دیم با مهمونای گل</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5444" target="_blank">📅 14:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uOUjpDbwQtEBiq9C456Uq8pBJziKohH_qmsZaPreHUcszV22DhOq-IKmzQ_AlGPOwpah-8lR0zzkfNqOaHFNj716yq984PaIkh3Qy161bCLnILXiT8qH0_6zGHCaUtEyDRe2aaRWL--sqXK4RZ_fpKS9sGdTWu5XOkevOy_m9maFGTbQqqRExkkR6valIV3krhlSDH9NrAzncV9oM0fTNoAyUGOSAb_JnkQ_zIIlQKmOXaeLhjuA43U0P2ZR0H9I0te7x2exwN8qdgH0UzFWU3fQlXJygsd6ga_-5H7bOs8CFCmljPKvlSnwD3SwqIeVZpaI-w1Xjpxidd7N5-JQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری رسمی OpenAI با پلتفرم Hermes
در اعلامیه‌ای جدید، همکاری رسمی OpenAI با اکوسیستم ایجنت هوشمند Hermes(Nous Research) تأیید شده است تا قابلیت‌های مدل‌های جدید و ابزارهای کدکس به شکلی منسجم‌تر در اختیار کاربران و توسعه‌دهندگان این پلتفرم قرار گیرد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5443" target="_blank">📅 14:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بچه‌ها پدی 2500 دلار کردیت OpenAI داره که میخواد باهاش یه اپ بنویسه به انتخاب شما
رأی من زمین بازی سیستم دیزاینه
😂
❤️</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5442" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5441">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5441" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N7VeKhiybrmqnRng5wYosOL06OGIOY9-NN7gKQvBmeMUXL4NKP793wVZWqQotODlDLvA2PqgvmlAHnUmwCbZD1csonET4w5o57w4eqsJ5wro4GcD2IPxDmGmlvOp1NQ4r7mEeIVqwgxtacJFKtqtHgguvwJ4IzRB2aahf7Xf8ZjltMDlYVPwdDCz8mQVxhV3JeA_IYC7kc5xO3MaX8VsRzLkXU31EKWrM9WPC6b2ogMF0Ixq5Uk60Df40sRgEy-Eyycb_YD5xEEgbhmGYHi3lsLq7plUXhBRqSvk9rEoJsSRqE-EKe7re98Rn2kAYYPU_Z2Wv4BoWe2lN-rcLjNzcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/E7Wp5sGt1uAH3E6aaYJIphXSQ9ID0DVQhZsG9ny_kI7EcbhsTfBRpepKmGBxkY9nReQHCRj8_x2m_R5pm5pBwHTEFHFd2EftY9NMif71UmsEeQDWMdj-UMZWPCvyNZY_rzwZQ7PbEE7-HvPhmEbeh5doQRxeGK4eWvaSSZM2L5K8imJEDWGri8Xf1mRtarFLuXJyw6e_tU13Gayyv3u1NP0DmU0q8mDgOJwKjxfTvw6rggqDDG0IbwlTI6v37_3-GFQ-BqHekZTxoML1R3j-QRDd4r9nXa2zDWVyVImZQPFyUz-SNyKeVIu96cMaSPyuEXCHc3yw3GikhFiSfHISUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قبلا برای این کار شاید 20 دقیقه زمان می‌ذاشتیم.
پیشرفت ai واقعا عالیه</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5439" target="_blank">📅 14:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5437">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OWEZamrVVLyQcoQSrIQo7hrpb39yu3JUnLzzj9im-PxrMR0wM6Q-HjoKiu46nnxsiSbPzVFLtuUbndrOzUsGlz-FMxKEIgz3paF4-QydEjFQmcOjkrJ5WMvgONwYpH93sdGe4mKFvR3OPXWXS29oB1rfkp1gc48puJH9Z1v-N_8ok8MhKRfR9BDIl-k6Ip38DiJQ4A-Gvs7JsHnN1PkCfI_yOaolTG7gewIKRJPOtZvMN6M4Z0QkE_H2rTnDeyORq9HPMASXMhjQt0ONN_ytKOSA7-brtCmFvE2yoAUXIiL-SprIMbnEb7AYxePL75bDvCpV1F1EVQP1arkMGmScSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AkhsNLU2TJGzVMe7WgIdDE8neO7wRwPnDZwRrI5_uCl9ddtBLJgyHNrfL6lw-bDQ4uZ7VHP_F4Pb71ra8a8y1Tet6c2uCt9p6gk-GTaDutHs-jlLPBEK-EZjOss9LwNnw-cpyC4IQ2Uz0RLvTWyuKo_HdCj3gEmIn2Z_BW0wv4UjBIeR8EsLVWL4k72kUv9YhXlqUn43DCJCr2_78N5MNKKzqA-k3-XDXsRyUBFrl6fRSGPzrR0U3_-g63XqxOmXXFJdauQsOMGMumQ7jOpaxsxSxQE1S9bBbw96H8o7l8x_ztoOnrFwqkuHih6UH_agNR7xXrVkMy95UWCQWQ5uYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز Manus پلتفرم Cues رو رونمایی کرد
چند ساعت بعدش، OpenAI از Dots
و طراحی بصری ساب ایجنت‌های بامزشون خیلی شبیه هم دیگه‌ست
😂
نمیدونم چه توطئه‌ای در کاره</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5437" target="_blank">📅 12:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گویا همه روی GPT 6.1 Sol مصرف توکن کمتر + قدرت بیشتر تجربه کردن</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5436" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عرضه نسخه ابری OpenAI Codex در رویداد DevDay
اوپن‌ای‌آی بالاخره بعد از شیشصد سال که رقیبش آنتروپیک این قابلیت رو آورده بود، توی رویداد DevDay بالاخره مدل Codex رو به فضای ابری آورد تا توسعه‌دهنده‌ها محدود به اجرای محلی روی سیستم خودشون نباشن و بتونن از راه دور با گوشی یا هر دستگاه دیگه‌ای ازش استفاده کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5435" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=BQxsUp3URtC1QdybWUhperpPRXF6HPlFv08EQ78P77lWwF8NZJg8K-Eze1qo2-O7cMsumuicZvSn6kQp4qNfdLFI1cV3_i5zMJLSlGk2UZgNPL_KA32ffXQSzB144J7BTX9rTWYlHZqtRzJU3uoTA66f-_iykFJoSAIh09Ra_-xFOkP-aUuuJxyhN26dLgqaTiBdBhi92Xg2epH5NudOKGIgaBj_wFW_PevqQ0iS8EiyYuL1XLtTcRZZkuhJgmmT-61citWLrQpt89JwITowvdJfvPCrdZ3yic1j312t2WAl1ctY_K2mLeHlGZrHVG8sRqWpwgrVPagPRKbgF3FKbw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=BQxsUp3URtC1QdybWUhperpPRXF6HPlFv08EQ78P77lWwF8NZJg8K-Eze1qo2-O7cMsumuicZvSn6kQp4qNfdLFI1cV3_i5zMJLSlGk2UZgNPL_KA32ffXQSzB144J7BTX9rTWYlHZqtRzJU3uoTA66f-_iykFJoSAIh09Ra_-xFOkP-aUuuJxyhN26dLgqaTiBdBhi92Xg2epH5NudOKGIgaBj_wFW_PevqQ0iS8EiyYuL1XLtTcRZZkuhJgmmT-61citWLrQpt89JwITowvdJfvPCrdZ3yic1j312t2WAl1ctY_K2mLeHlGZrHVG8sRqWpwgrVPagPRKbgF3FKbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5434" target="_blank">📅 08:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حس می‌کنم یه رقابت خیلی سخت بین سرعت ریلیز مدلهای جدید AI و بالا رفتن قیمت دلار شکل گرفته</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5433" target="_blank">📅 08:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5432" target="_blank">📅 00:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مدل Ember-1 از Fireworks: کارایی Kimi K3 با 40% توکن کمتر
تیم تحقیقاتی Fireworks مدل استدلالی Ember-1 رو بر پایه‌ی Kimi K3 منتشر کرد. تمرکز اصلی روی حل مشکل بزرگ مدل‌های reasoning بوده: تکرار بیش‌ازحد مسیر فکر توی خروجی که گاهی بخش اعظم هزینه‌ی توکن‌ها رو می‌بلعید.
چیزی که من خودمم توی ویدئوی کلاد رایگان، سر اون بازی سه بعدی تجربه‌اش کردم و واقعا افتضاح بود. مدل توی thinking خودش گیر میکرد ده‌ها دقیقه.
امبر با بیش از ۵۰ آزمایش و ۲۰۰ ارزیابی جوری آموزش دیده که شاخه‌های غیرضروری استدلال رو حذف کنه و بدون افت کیفیت و دقت کدنویسی، همون نتایج بنچمارک‌ها رو با حدود ۴۰ درصد توکن کمتر تحویل بده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5431" target="_blank">📅 00:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5430" target="_blank">📅 22:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن
به اسم Dots
تقریبا شبیه Muse، یا Grok Bot
https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5429" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5428">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QVlbKYq0zW4F0xgMS0psZtt-94CcD8bkKhjlDcLD1fOY2Mgw_l9AqSeOKQGwnqz3n4jpQXMKfNH4D_EH-x5285kqCIkJ2vXOnUrdfTcq07F7vTQTS-AG9qCebeJmw8TmOOuSXMiafcrPG-oAgiwZj6vlQ-SXHbj8-DU-HW1h3L-KPAfliObNwk-NQgiRiWn6behdV_sJRusKOPwOWg4oO4DTJCLFTDAN9Cpv2NFIM5xPsxDvN9H3xXx40kgDkU7jufzGq1Q-Zhaz6C5g-KjQNWhouzK6a_0piZX5-6vayPP29gg_FcTNbG6adHz0zGoI-XNU4CZ_BdcgXFw3GNORJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی خندیدم
توییتر OpenAI کلی گفته بود که امروز به مناسبت Dev Day قراره یه چیز خیلیییی خفن بیاد.
کلی توییت زده بودن
هایپ کرده بودن
حالا حدس بزنین چی دادن؟
GPT 6.1 Sol
😂
😂
😂</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5428" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gbl4HZqU4ZaTPJeGCGMNKDvSLYEaPG_Kq0FLFcQ9_Hjk8w1sPWpZdcQjzRolOc2BwNcgEhKWNXujmVrEtD0U92FXOKm7KtuTLZbl4fP6MIIuyhmCf8FXv5gSKPyS81AyXI2hKq0Z2VHqfN0r2XYPjgBgDiusOELAuytWprpQ1P5VRuWF8tT5_W8ckLJxToCGlUesXKNFoNRYvbdAnL_4y2TltEkws35DAaxP4Q8ZD6rdtdqlPA1HsYNDucgHxA0pKdnlskoXTZnjfYWQDpkBVEcmqEy0hyP7ERGloR6v2it3bn_-b6X5BYdCdWo6xmNPKwdmMJfWhl2gKJNmeWkbuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TcRpv4goNYvzg2ECxw1Ge43otSQOabPwaqcWvq6qE71DKd8TrcK4lgStJ9Zn_a7Q-JseuUltLC7C8R8_8XxE17WxmmoYH65VWsZpHvuSc7IP5xIX_oSUdqWiW4K58cO7G4ygBeBWH95atiKhfJZLtpL_GsPRAFItNs97IKXEQqJnjRoO3CLCHjcpyuSJLa43ZslZxcofliNt2q52oRs5cTeb2JipdZO2tZMgLlQxFcFVFdNfM3Jp_fFXOR84xSTKV-nb9offFQQHs4zTZ2bfhZ3epFv6k6qvrzxfSsZoE8CNO819X0sl6u7L1-Ks5aISkmEHDR-XhqNnBWi-MaSe3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کلی ارتقاش دادم از دیروز که الان داره با یه مدل خیلی ارزون، کارایی انجام میده که Astra نتونسته بود. یه پنل تحت وب نوشتم براش که اینونتوری رو ببینم، یه مدل سوپروایزر براش گذاشتم که بالای سر پلنر باشه و تصمیماتش رو هدایت کنه، بهش حمله کردن و دفاع کردن مقابل…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5426" target="_blank">📅 19:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vCEBGnPsdX_IJtXZABjhjXV0aYRueoSgvKzN7OkiOurI_dSIHNQqQstrQWrVg_IAarKTqQYrpSY2fefBR4D--gWKPsbrND3zdBnELuYlXvwZCuGvI8xk1nNXwxyaL3Qck7IvO14GtRGrfuAqQ-pTI--rhCGIBosXyktK-vn-LzMjtGvzPykXKyC_2iCfryHK0IjoQ5J-PfV0Gsae148Thud-U2xt_8iQe7gFlv-EGm80535FPizOMeqVzVuMYA9iEDwKYud89CS2uVGMu8zGKidM3ReroQdxIScZtS-mLdstt6qeIiCBp6FrBVAd19qorUeR5I70jS12x0uIXgYg6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5425" target="_blank">📅 18:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ایده بیزنس: یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال" قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط بعدش از…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5424" target="_blank">📅 17:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ایده بیزنس:
یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال"
قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار
هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط
بعدش از سودت برای تبلیغات توی کل شهر استفاده کن و دوباره پول در بیار
سرمایه‌ات که رفت بالا و بالاتر و مردم اعتماد کردن، یهو پول رو بردار و دفترات رو هم جمع کن و فرار کن، همه چیز رو هم بنداز گردن بانک مرکزی و فرار کن د برو که رفتیم</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5423" target="_blank">📅 17:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">در مورد آزمون تورینگ و مقاله‌ی Computing Machinery and Intelligence سرچ کنید و بخونید. جالبه. با اینکه انتقادهای بسیاری بهش وارده که دوست دارم یه روز بشینیم با هم صحبت کنیم راجبش
و دقیقا پرسشیه که اوایل سریال West world مطرح میشه.
"If you can't say I'm human or robot, does it even matter anymore to ask this?"</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5422" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یه جورایی حس مور مور میده ویدئو
از شدت پیشرفت علم کامپیوتر، اینترنت، ai و...</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5421" target="_blank">📅 14:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=Ry8aMHGd5wNK77m_CKLky971u0_y8Ve6MYzs4fZXFvCxCEAHwmnQJG88ds9no5H1kXRjmo4zHSBtlEks7Es1JfswAa164AEeaIZT_M5RKS-LMiV68pAFLwaBVLEyMuVIvIm6SLep9SsVZ-xyVt-qFAaeDD2Mu4KwoH-jLTWTmLNL0Fxh8PIwcVI0NSUX5WLkifuMPHnNhxHroPatAbj9U4Y4utyFzZxBS6y_bP7Foi2HnfhzoXRDWUONMvzflRacb2eaLzTw1oNdVp5UnvJM0Y3xKD0PkaRC39qkOUmaQ2k-kiF7L83rEXx1Zxo_K-0Xs-XZuDuNOCwiLLeMDmGMBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=Ry8aMHGd5wNK77m_CKLky971u0_y8Ve6MYzs4fZXFvCxCEAHwmnQJG88ds9no5H1kXRjmo4zHSBtlEks7Es1JfswAa164AEeaIZT_M5RKS-LMiV68pAFLwaBVLEyMuVIvIm6SLep9SsVZ-xyVt-qFAaeDD2Mu4KwoH-jLTWTmLNL0Fxh8PIwcVI0NSUX5WLkifuMPHnNhxHroPatAbj9U4Y4utyFzZxBS6y_bP7Foi2HnfhzoXRDWUONMvzflRacb2eaLzTw1oNdVp5UnvJM0Y3xKD0PkaRC39qkOUmaQ2k-kiF7L83rEXx1Zxo_K-0Xs-XZuDuNOCwiLLeMDmGMBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«کلاد ساننت 5.5 این رو ساخت. فقط با کد»
این داداشمون
این ویدئو رو توییت کرده و اینطور گفته
ویدئو در مورد پرسشیه که آلن تورینگ، پدر علوم کامپیوتر مدرن و هوش مصنوعی چهار سال قبل از مرگش مطرح کرد:
- آیا ماشین‌ها می‌تونن «فکر» کنن؟
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5420" target="_blank">📅 13:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=D3Rbk5v1V0ppZsdUcHOopyLiT7KEMI422mft7owZgCggcEfViidEY3SrRCXsDEYVNcoZcF9ispCiBcuSquqTPoo1jKKqHZ4QqIH8ru31hpz-T9uiv49oI50QD2y4W7S24Ppkg3DxuLPXq4iBAvQXhNRZw2Qiix5W3TYVDGhGgnlfEiDFwE1F5HnWeNt_mkdWUgjTFvwMo4E1Jbjf398awy9DdeudtoRSfI0HL7CBhG2xbJcglR_AOnPGpJWpIX6i5ArT4nuhuiM5oLglmGmrxtYJsyRkE_DY8n2VMF4jbMU39TWaqv221ibsHYJE4pljKWiVGWRk9NSnQAIfN2qyJw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=D3Rbk5v1V0ppZsdUcHOopyLiT7KEMI422mft7owZgCggcEfViidEY3SrRCXsDEYVNcoZcF9ispCiBcuSquqTPoo1jKKqHZ4QqIH8ru31hpz-T9uiv49oI50QD2y4W7S24Ppkg3DxuLPXq4iBAvQXhNRZw2Qiix5W3TYVDGhGgnlfEiDFwE1F5HnWeNt_mkdWUgjTFvwMo4E1Jbjf398awy9DdeudtoRSfI0HL7CBhG2xbJcglR_AOnPGpJWpIX6i5ArT4nuhuiM5oLglmGmrxtYJsyRkE_DY8n2VMF4jbMU39TWaqv221ibsHYJE4pljKWiVGWRk9NSnQAIfN2qyJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5419" target="_blank">📅 12:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SvUfspfFfmV5HhwNW8UaEhwYMPKEM61A1AxJUVcp-sJGSDVOqIy29WzM6V1u3ljqC-u-WVcbQJMvucNRuyXLjBUbHzMuejaxVYs5_zcNzSa5qFColMWbrGsMgXtnvnMMQDdlbskZ3FDhvOu2iLuLRFsUvrR0ugnVcY2i4Tw-8Dv9AU-pWhQFbpO5VsPZiIloLaWVW34Xqt3IGoea_0pJDVQAT3ofCcfXG_F7SUP878c7ZnyRIYpW3qXE_Hpk5KGGa4rk5AQ37obzGhfYbA7Edq3Zou2uVL9GgsdpOgdgVtoUlIC_GccJs60uP_oKBRrD06DFOlRl3LvKbkkyrfVDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RrMvRmybsUcKniLTJCneCXtYZ3jHIEFNsTWkHNINuDyoiug7XbqpRqgr1mW5KHfY00COLqco83T-MjqcCorJiVFFggpWu9DYdj8LlKh1usq7z-eaJQ96qYRHsel2qngEQWOKbjVlG0v2mxE41cOrruf3lLJdE4EX95ZpbX5HrUAcT5ImQacCTTVNAFK6iULBxeKJB4r_zGiWMNNx-yMA-yYU7dvCzgD__34lPCmXpP3iJnRvIWYsSVLCX2BuCPfBeVgTLm0x5RnJ1Jjul4zuLQCtUO4We9yV-tJ564nUCinmmBrU09EF7hQ6wsYNd-o5GPb_9gYXxxu1jAtZCrmRMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این نسخه از WhiteVPN می‌تونید مشکل فیلترینگ ورکر رو دور بزنید</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5417" target="_blank">📅 10:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5414">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5414" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZC-t2y0oCTee5NhDGUVLPqoHFU6PTRccXb53-R-JID4Ir0-3DpRi3Mb92kejX18m5LNoBfh0JcWokfoOmHj-HWecFPqvi1HBmUgW7HAnDfF677fSmGd6LtmfZLHnpR4wR8LBi3r74dqv7WFxVDY4CjBJinHBIVHrHWfAWK-P21IRC8tuV2IKLyi8kRtOmHYsNNd-Q-7vdwn-H0dxiHf6r0lwmw_0BgFGloJpa0jzvbEB8b9RleZMVu5syEFn3MHui1rZEmJiHDpxHHYkJgYTS_Dk2--N-64a-FoppiY23ICfubUwAwTtgxxdpMa8jHuCn2it6331XCaT0iFAKZEMbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5413" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N_M9rma4avZbBCd8Aw239YYRnk-bLvueMxibmoDEWh999nqLftHEJ2pIC70XuTy3qgWONOg6osVmIn0qamPtKgwdByWN2I666yTfPJ2HfMTVHbp2NgaGv6YyaXWhIsKgjQAo-ZxGBdwMwMUJR9HEYIfbZNqGZTVF03tynGE_b7Sv-kp4QABTsyGABTvgj3DHm3x-Rm0rIBVZvw_6ABMlt_rzunMWZOyfwY8SnH6VHhB-zOAhUpqcy1j37qTFFF1nr6WI0Djus8UCJF6C7c0EUTfalx7ARep3fdLXGLtmh-4XLb1pVSBJuibJa8GqcWeoRi4eQ0aLTiJJyz2as4RTMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10
اسکیل برتر OpenCode
جامعه کاربری OpenCode فهرستی از ۱۰ ریپوی برتر Skillها برای ایجنت‌های کدنویسی جمع کردن که شامل پکیج‌های اتوماسیون تست، دیباگ خودکار و سینک شدن با دیتابیس که کار روزمره دولوپرها رو خیلی سریع‌تر و روون‌تر می‌کنه.
(حواستون به SuperPowers باشه که خیلی توکن می‌بره)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5412" target="_blank">📅 07:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">Matin SenPai
pinned «
اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید: https://youtu.be/dQKfkXnThCE  به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5411" target="_blank">📅 03:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e-7KTUk5Wsx4WUtaTEUE0kgwzF3fxVgomzgH3XNIkCFpyRZiZZVKDL-magDHDHFY8WejPc3P21za9d2i2_bHceeDLpRCFaU3-YCoCFDZ14Ejp9V1EgxAWSvr5JjK-SGqkPqfk-ldwtc7Nnni2OBaEtUwjWGwRLFNvB60HeFcXwNTAZHMdAuBOjaBtRWohP7UFjrAvpoNy05jI2FAQ8THN1z70pdHXMktOkZkTpnkvwyxZ_NGq3379_RbBMjPyohpLU8to530BfxyYCWHAIcMJHOaVoSCuEYGDmsi5VNuMQUZk_nbWUidfYoj__J70bQMQXzqCcQHu1x2wyOnsJr3sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5410" target="_blank">📅 03:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J1-N-vPqcHdSXh-zIbIwEelUybzGc783yineH4AewlSX-k1Dehh_SE_UkhJZaCH-zhSaXGV-FlcRm_pgfL_sNI5vLZWoDTSgh-_iKns4UCN4-qxfKpzSE7oNYbW4fam-99A5qTaJwdMhL1MRXNjcgjLlKyGl5JiN1MgFyxZprL_Zzohdf6pbnOEbwC7kZcqaA9VeBbCtjQ28zCgojqwqmXIrbM_GyiIu_BbLc1l8AJCxwNwsBUiQQjy01Wg5Rj-SApqEwhFRp62LCHSDqVNbV_Fq6818ammL6Jv1299Tf4QipdksRkyfM5h3G4sIPxY4OVbOcfuWlL_HaGdpKzNh_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5409" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">هرمس خوبیش اینه که سمجه. اگر از ترکیب هرمس + مدل رایگان(مثل mimo) استفاده کنید، واقعا غصه‌ی توکن سوزی یا انجام کارهای سختتون رو ندارید</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5408" target="_blank">📅 23:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مدل Claude Sonnet 5.5 معرفی شد. هم قیمت با GPT-6 Sol، اما به شدت قدرتمندتر! نزدیک به Opus 5.5  • $2/M input • $10/M output • $0.20/M cache reads 1M context + 128K max output
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5407" target="_blank">📅 23:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aibKNxOEVh7qN8LWg2K_7BjVxhX2kuC6Ro8h6SqTpwGGD_OeDruvkysWeGKtKn-F4dsNj2LQwoMxRpmGyECeojqpfZo6RqcEA4McefCvMofCextsoIiei8nFfLA57geMd_Y7yLfz3-vi4a5d8feU4kXUAOmM4HxIRjG0SyhMJGSYdpROyRgQ4dziuhH1ffmfMo3EbT7UOOG-px_bzl8hY4WH9ZSo-FJg8gOjWaOmsWyA5wOnlPl0BM4x6TWjQuu_jBfo1bALZ_Sl9th04laVQcB86ABnVWceZlai0d25YouO12g7gHUSEUBiVql-E6ZE3BGSf3fnbczLRB82Bi6glg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i2X5SHehX3UTDxoU3DXLWmwc3vJexsadRBqzUuCU-BvejNhWAoYxmvIhsy1njOSFeVr5VhYE5k_su7UXJdcEq1mOEyIZQD6fWiKcYlIftTqqRjRnffOQckhmFKKNVKJ9CtU_L_aU6pWlaJ12r1G5xf9fouYxMcQsD-HyXrdBxqqGJtApHh43OPWTAkOi0WBMedHr79YoU0jSVpNrbL5Au5TE26ojkgL1V39tg71pfmyEkMnY10NRu1EChfIkBfZgwxbIUD3sL4_gdTYqFXKn2ZAA_z5sdkGZgaGfM2VzVaOGkm9BdV2QdkT7fBaRs6M8CQ2kX1ewd5B_xBvBrfNNgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5405" target="_blank">📅 22:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5  از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.  هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید. https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5404" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82410567b8.mp4?token=V63x6Gv4MoNrtoVOm_VtTGAkrp76IEGEr7ckqxRDZQ-HXTKhOp-6pSXSXLsDdcARbJ7KblchENUXulYbDo65ZUAhzpSEFJvAvm30KZ-XX0Zb9VjxOYTVJt8dKo6HIVUJktbC0o1l-FbgM-uYLqKfUWCMvGiDDTr7BoCK6BDKs6g1acP_0zW4kjNX5C018Zy90jrBJ43k4BuklxWmDdTc8kq4AiOfBIftXP0NeFs6hopvJEvkNPWPAdRZZr_-s-68tKU207NrrRRCQH6VJFWXe130rUkq0NNrwa7FeOoynVjljfr6IolYD4cX6SIjfPslsq1SKTCCp_9Fba4gjqJ36Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82410567b8.mp4?token=V63x6Gv4MoNrtoVOm_VtTGAkrp76IEGEr7ckqxRDZQ-HXTKhOp-6pSXSXLsDdcARbJ7KblchENUXulYbDo65ZUAhzpSEFJvAvm30KZ-XX0Zb9VjxOYTVJt8dKo6HIVUJktbC0o1l-FbgM-uYLqKfUWCMvGiDDTr7BoCK6BDKs6g1acP_0zW4kjNX5C018Zy90jrBJ43k4BuklxWmDdTc8kq4AiOfBIftXP0NeFs6hopvJEvkNPWPAdRZZr_-s-68tKU207NrrRRCQH6VJFWXe130rUkq0NNrwa7FeOoynVjljfr6IolYD4cX6SIjfPslsq1SKTCCp_9Fba4gjqJ36Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5
از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.
هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید.
https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5403" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید:
https://youtu.be/dQKfkXnThCE
به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5402" target="_blank">📅 19:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pm1OJBZ2NFSMvs5fihtEP0mW73JBKd5EwoSokPHs0y8nklECjYtuSE5-IL-yopVB2UDKrwmJJbo7EGr7MgjzW9yiKozQLkNxjyUsuPGa2jy-D-XgOyjNmQCvskUDBGlckAuDzyhyX4Ib9w99ESYA0oB3zJbqAHESRPteU_T-F0lSQNYy506omb2SWKaNoc42d3UdYr_R5boquM5sW0O70PPChl2ZaEvgA_KtbuyZrsAxJ-CWLA0fZR6m7XDLymOUJRkiuVcOW3A2eizBgrYdhgiC2lkHIBBJ-rD0F37zib1zT3BJCNJz7GN9Y75f6hqg9_4SgUOFdsPFWLMbAST8Tg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5401" target="_blank">📅 19:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LVUWiA00fuen5CMe_oi3X6EzHdUpkSzZwrkRGgV05emx0h6jKhmiEvOhoNVRNX2g80uIZA3OfELU6EhNVd607OdG3kRBKiv4VE6udB-oXZ4Fb_Js5pP2sx3mTVOpKtP9kTBWfjyi2CjjHv2V6Wr7JEe5uDlUhXoWlfR1wyosHZkJ85Q5qVJkQWENFM9kl4cVxyuCtqsS9y3hrDzp6r2bF9juVKBJV00JoWLALP3jIMo51F4utRMOpnYEYUq5fGsRJQ9grnZMKDISv1NUuQH0Y0zb-2YwVS6WYs2XdlkG0bUhldQE58O2m9lne8z872eE-ys5WOlUOkcSl85WaE1zXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر کنم گوگل چند صد میلیارد توکن از نسخه 4.6 ساننت و اوپوس خریده برای Antigravity و نمیدونه باید باهاش چیکار کنه
😂
مشتی 5.5 اومد 6 هم به زودی میاد ولمون کن دیگه</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5400" target="_blank">📅 18:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/celJ99mxzXlkOzKDPlJJMk6peFWp-gwtktJFN2YC1_vhPjol3J0y0d7dUuSYSn8JEpDDF8XDmRXp8xy1bAE8Hmzfab0KQtOqcJnGkH3zMzrfHhoZSkrO2PuhrC_O2FqruRoWDF4r_sA7o8tZsAeArDGvJen9qCY_RIAWnnlPom7cRP4XcuECaLEFJePCIfZmtG-uSsz4TnYSe638FMoLNYeHoR32NJGbCiXWvZDquonmnp-kbwT1_cRJEugthVqlboNMd4t8tn9chIZrEqzcVILOu1we-YlP0VUjxspqG0UtAx8CmEuE_HO2Twkt4lNj-jSqvaJUIpuIjYtbVe2ZVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی ساخت نرم‌افزار رو آسون کرد، دیده شدن رو سخت‌تر
قبل از AI برای ساختن به توسعه‌دهنده نیاز بود؛ حالا آدم‌های بیشتری همون چیز رو راحت می‌سازن. ولی تعداد کسایی که حاضرن پول بدن، یهو چند برابر نشده. نتیجه: وقتی ساختن برای همه ارزون می‌شه، مزیت واقعی از ساختن می‌ره سمت توزیع، ایده و شناخت مشتری.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5399" target="_blank">📅 17:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XN09jUD-4I_a87W_UWthx2B6woVezVwzGjZLIP28oxY8U3CzrRgjQ8JLL0k4tUNbxgQoEKq0sRRw8eFKxRpL2Oo-MKngrrw4JGEI2tjyOIj4oIJKD3T8gTRMkpx3xtyMvKiUgOCXhmxLKlda7gu8KQuY58yR8H6J5OJm6dPDuMJ9r_xirRqCqPhBazINXjH5E-NYK8kOfbqnHfQJRCeEk1LLJaadeSr1pi0p9WxCj6xjNg70BA_7Y420scpFDw3iot_u5tiVbXJ3PNkZ38VcGr-T2tOlg91V0B-1DyyglLSMS0zsfYI3IMa2UmUr-yl8UZkhzza8XkGqjJDT5NJRNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aoHOvlzfQTB67kQ7W3M99-wjuIU4esmgGJXU7KIsKdr9rjUpfk9sNZ_brD-r33QZq-aBUJdVCz-GL9GsNa9F4tieB3s6Vty9omCmO9J2TsZK6wX1x79pKg1bRlUtg8rErxyxerFeHQAQd5ewlh564Qc-F8eULafEwoiyw72GSKwIYQw2zWyE667B41NGuuLgEjPWK3hD8rcVavdACNPQt9BE0v7DlXM1Uj9tFeC8u27YIG5ZK7p2PUhZiSdu5xQKOZEcv546WBjA0qogtlNAqe2AZgF_3d4Dk0aEMM_yxWd8nwdLEm9f89XVAhnDvjGKE1Gsi67COGp-gRBkYz7_xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این فتوشاپ اوپن سورس که مسخره‌اش کردن یه دوره، سازندش اومد توی ردیت درآمدشو از دونیت‌هاش گذاشت و گفت محصولم خیلی پرطرفدار شده
😂
لینک این فتوشاپ اوپن سورس که اسمش Photon هست:
https://tenzen.studio/photon
لینک پست ردیت:
https://www.reddit.com/r/SaaS/comments/1wsac6d/i_replaced_adobe_photoshop_with_a_free_better/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5397" target="_blank">📅 17:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست
با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5396" target="_blank">📅 16:38 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
