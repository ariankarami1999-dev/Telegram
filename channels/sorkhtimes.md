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
<img src="https://cdn4.telesco.pe/file/mNuyzeQRvIOwgdkpl7Xncvf1VRMNLccEEpUt8IKaLHFrhAyhSX1gMDO5RpGnP54hAtcjVMAk0w_CgDbRFK0NV4wYJpo3h3qnbnMiyr9whD3UoGl4c9JVlYDJsU8O6w4M6eX5TW-rLzP3VVz_yyYr11jw-GtESw1CqTN8gbyKEjjPqlnEsd8YVh1MIYdnr0Vm6qPEl3p4r1ePMEQoCkELM3XGejpnV1_1A6CkEEPMhuYpxOCW_zA8ZdaSZW204ISZZtJpbR2ksxIc_G2o6CKk6lv9AxZ6mDua9a-C95I1O5AMZHiKyfKZAwMz6D7odCVm2rId4qN4TI-LQeFrNi1GrQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 05:55:29</div>
<hr>

<div class="tg-post" id="msg-140678">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O52zqxChJDLrhO8Cfee-8rvlPC3Nu0UGkngKHo53NwLnGnmPKNGTj0KSaLKZPEbGrycvdsbPr-NufQ0XyCtxJ2OcOm0W327d9mKj05IJV0UvsV2Lm2YkDVo9-Vya311HkBQlz5HO1Rr0-9uV_yiHAZGcn0XA7oWrphZRQwbraFF05hiAnvRbIzcXVheRTAE0LfZwTUS-RjjpeOpuiFWF-LkfHXSlK5ZBrtTjaZpDh9Gg5szkPN2SrbxDzfB_Socu-p1CkwtFEEqoE8z-aASRbrVpRxVwOKAJx7VhRWfp19GiT4VOgTnyMeenDHfjfY-wQcawBq0rn4D7WClZVNGPEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Russia -
🇮🇷
Iran
⏰
Tuesday 19:30
🏟
Ak Bars Arena
⚽️
روسیه با فرم هجومی بهتر وارد بازی می‌شود؛ ۳ برد در ۵ دیدار اخیر و میانگین گل‌زنی بالاتر، نقطه قوت اصلی این تیم است. ایران در مقابل تیمی است که در انتقال سریع و ضدحملات می‌تواند خطرساز شود. تقابل‌های اخیر دو تیم هم نزدیک بوده و در ۴ بازی آخر، هرکدام یک برد و ۲ تساوی ثبت کرده‌اند؛ بنابراین انتظار می‌رود بازی درگیرانه و کم‌فاصله دنبال شود و سناریوی گلزنی هر دو تیم دور از ذهن نباشد.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 909 · <a href="https://t.me/SorkhTimes/140678" target="_blank">📅 01:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140677">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
فرزین دبیری عضو هیات رییسه فدراسیون فوتبال: تراکتور، پرسپولیس و سپاهان مخالفت‌هایی با قهرمانی استقلال دارند
✔️
✔️
اینکه ما از الان مخالف قهرمانی استقلال هستیم، اشتباه است اما قطعا مخالفت‌هایی در مورد قهرمانی استقلال خواهد بود چرا که سپاهان، تراکتور و پرسپولیس…</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SorkhTimes/140677" target="_blank">📅 00:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140676">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🔴
افشاگری عادل فردوسی‌پور از ماجرای پول گرفتن ۷۵۰ هزار دلاری فدراسیون از باشگاه کیسه، قبل از اردوی ترکیه تیم ملی بزرگسالان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SorkhTimes/140676" target="_blank">📅 00:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140675">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♨️
🤩
🤩
افشاگری باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!
🔄
🔄
محمدحسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت…</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/SorkhTimes/140675" target="_blank">📅 00:24 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140674">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3190d23c56.mp4?token=u8Cz5L3WLzGTXoe5jGcO7OfWVH35cyb6W-2brJUna_Za8DRPpD_I2mpjgHrAmYBpCsXz0B2eln3W-NrrgFSMRnrObH4Y72uQUz6UNe1VICZLK6icG75NausslvzzbeNyeEnuwJ-YHusftlMSKRF5Djy4DsB6eF3RyyivSoCqGgdb6dWOnD7VbK1OWSLuLVf8YljvFWJn-guUr3JAFXDYeEIs2BTZpT09t4gLhtUsY9ffRcEb98HjXcDM5FJ_MlkmayQMyoB2X_S-ln75EZ-YezNOz7eilL3g0Ml6RPyfexNC2mO42c8osoG1xOIoJ4bDDlgvH1CKpWU3wE36mzbVNirR27S9xIIYizxV9nAT27gup5RFQS3wb7OJyXdi7M9wcMgOL61ZbAK0stfw2kfnsy9RgYMYibRlQ0p3E_VAOrek6vWR7NB43q4D2Ckb2QLt-tHJMNuJdNf4QYF41I8paRuBJTdaMjYAJ-VfAzozGcBNskvM_dpNX4HUax_x74HX_c6HJ7b5qqQrDQFLc8F5zloHeB6OErgRvNcIY_LW-qlxfoxfxmU8dez58wrJuCn5brsTaWPLl8HPkK6BYXcb7qtaY4D5NcRRd0Z5CUfp7GUDoy4uNh3dhPdbS__bbSYcdihwN-3LzDVzQmkhzZ7E9JO6vvbPRDhidf0zcZcrJdk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3190d23c56.mp4?token=u8Cz5L3WLzGTXoe5jGcO7OfWVH35cyb6W-2brJUna_Za8DRPpD_I2mpjgHrAmYBpCsXz0B2eln3W-NrrgFSMRnrObH4Y72uQUz6UNe1VICZLK6icG75NausslvzzbeNyeEnuwJ-YHusftlMSKRF5Djy4DsB6eF3RyyivSoCqGgdb6dWOnD7VbK1OWSLuLVf8YljvFWJn-guUr3JAFXDYeEIs2BTZpT09t4gLhtUsY9ffRcEb98HjXcDM5FJ_MlkmayQMyoB2X_S-ln75EZ-YezNOz7eilL3g0Ml6RPyfexNC2mO42c8osoG1xOIoJ4bDDlgvH1CKpWU3wE36mzbVNirR27S9xIIYizxV9nAT27gup5RFQS3wb7OJyXdi7M9wcMgOL61ZbAK0stfw2kfnsy9RgYMYibRlQ0p3E_VAOrek6vWR7NB43q4D2Ckb2QLt-tHJMNuJdNf4QYF41I8paRuBJTdaMjYAJ-VfAzozGcBNskvM_dpNX4HUax_x74HX_c6HJ7b5qqQrDQFLc8F5zloHeB6OErgRvNcIY_LW-qlxfoxfxmU8dez58wrJuCn5brsTaWPLl8HPkK6BYXcb7qtaY4D5NcRRd0Z5CUfp7GUDoy4uNh3dhPdbS__bbSYcdihwN-3LzDVzQmkhzZ7E9JO6vvbPRDhidf0zcZcrJdk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♨️
🤩
🤩
افشاگری باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!
🔄
🔄
محمدحسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت شکایت کرده است
🔄
🔄
در همین راستا این ایجنت قرار شده است مدارکی به پرسپولیس درباره فسخ آسانی بدهد و همچنین این بازیکن به پرسپولیس ملحق شود و مذاکرات حتی تا پیش قرارداد هم جلو رفته بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SorkhTimes/140674" target="_blank">📅 00:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140673">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
علیرضا بیرانوند: چون من تو یک تیم مدعی بازی می کنم این همه فشاره که به سربازی برم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SorkhTimes/140673" target="_blank">📅 00:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140672">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
باشگاه پرسپولیس در پرونده مهدی فراهانی و حمید مریخ برنده شد و این دو نفر باید سرجمع 220 هزار دلار آمریکا (51,216,000,000 تومان) و 12 هزار فرانک سوئیس (3,414,120,000 تومان) به باشگاه پرسپولیس پرداخت کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SorkhTimes/140672" target="_blank">📅 00:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140671">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNMIqvl7wO6Z8sJnJfl11C44I40yACdV8sChzW53cq7w-Dw4iT7lUCAJ_N4yVdBo6ZcLMXe3KRYsrWYce96PiJbGHW7S2sJIiXW7v5nL7mkE-CWD2YxwGP2e63-D8_afjGPTBeK3PQPGwdnzksuPXgwrfuGlmhKQEo-StqQnLiJXgUSgrh07k_POzFDQpFZxcBhwozaNfgphgJ8gf_Kja6tccyoXn_fFAWOUCn3JZ3wlkigzqihEm_7vGQWS3Sgsd5wfuHOOQF4UJASpG0kMxjAEm_Pisx8DfnuA3awFPW4M6HCXDxpsbPPyFnAtof3Hr9it6NbTLiAzVJZ17XFzTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
وارد فیفادی شدیم، شخصا از فیفادی نفرت دارم چون پرسپولیس لذت دیگه‌ای داره برام
❌
میشد که قبل از فیفادی یک برد دیگه و یک بازی دلچسب دیگه از تیم محبوبمون ببینیم اما کارشکنی‌ها جلوی برد دلچسبمون رو گرفت..
❌
دم تک تک بازیکنامون و کادر فنیمون گرم که کاری کردن وقتی بازی پرسپولیس رو نمیبینیم بجای اینکه خوشحال باشیم، حسرت میخوریم که چرا چرا چرا یه مدت نمیتونیم بازی تیم خوب و جنگنده‌مون رو ببینیم..
❌
بعد از فیفادی میبینمت پرسپولیسم؛ منتظر بازیهای هجومی‌تر از قبل و پر‌گل تر از قبل هستیم آقای تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SorkhTimes/140671" target="_blank">📅 23:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140670">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
یاسر آسانی: رامین رضاییان کسی بود یک دقیقه بعد تمرین تمام اتفاقات رو لو میداد و همه میفهمیدن و ساپینتو برای همین لج کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SorkhTimes/140670" target="_blank">📅 23:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140669">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
علیرضا بیرانوند: چون من تو یک تیم مدعی بازی می کنم این همه فشاره که به سربازی برم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SorkhTimes/140669" target="_blank">📅 23:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140668">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
✅
علیرضا بیرانوند دروازه‌بان تراکتور : من نردبونم و همه دارن ازم بالا میرن کینه‌ای که بعضیا از من دارن کینه نیست علاقه و دوست داشتنه.
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SorkhTimes/140668" target="_blank">📅 23:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140667">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
#فوری
🗣
خبرگزاری مهر : تعویق خدمت شامل بیرانوند نشده و او رسما از 1 مهر سرباز غایب محسوب شده و هر گونه بازی کردن او غیرمجاز است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SorkhTimes/140667" target="_blank">📅 23:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140666">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🤍
🇮🇷
سردار آزمون با بخشش 5 درصد اموالش به کمیته امداد خمینی به تیم ملی برگشت:))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/140666" target="_blank">📅 23:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140665">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇷
💙
💚
یاسر آسانی خطاب به عادل فردوسی‌پور: من میدونم که طرفدار پرسپولیس هستی
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SorkhTimes/140665" target="_blank">📅 23:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140664">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1981c5068c.mp4?token=XS_hJQ43kd0LXR0DjTI3qepFD4pYWqlrw-OZcG3xVmDa15eeDMHoFmznjOKDQkMoOMBHyyBh4so8P1G6SVECj9-lgs8AsGpAmp3GYToiGKv9KZmxzSKZ_iMhR13WnLj_xF711YSIsFwgoyd4mY0Ei1uxAx95x8aIR9m1e28qbRdFzsPgcvO-CJbbhMLKzaMMP3YGLbe8odtex9Sc59VVMhUt3z0gPH2lvrHMlgUeI2nQdqzLGpPhOk_S1uEAOh3HkB3zc8Bhro9J5vLnYCMqa43dEmQ4IysDE_5XjFhM-4g3w-8VUUhQb97AGjmUgqzS-er6J8-tD80dvh0yHxQNDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1981c5068c.mp4?token=XS_hJQ43kd0LXR0DjTI3qepFD4pYWqlrw-OZcG3xVmDa15eeDMHoFmznjOKDQkMoOMBHyyBh4so8P1G6SVECj9-lgs8AsGpAmp3GYToiGKv9KZmxzSKZ_iMhR13WnLj_xF711YSIsFwgoyd4mY0Ei1uxAx95x8aIR9m1e28qbRdFzsPgcvO-CJbbhMLKzaMMP3YGLbe8odtex9Sc59VVMhUt3z0gPH2lvrHMlgUeI2nQdqzLGpPhOk_S1uEAOh3HkB3zc8Bhro9J5vLnYCMqa43dEmQ4IysDE_5XjFhM-4g3w-8VUUhQb97AGjmUgqzS-er6J8-tD80dvh0yHxQNDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
💙
💚
یاسر آسانی خطاب به عادل فردوسی‌پور: من میدونم که طرفدار پرسپولیس هستی
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/140664" target="_blank">📅 23:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140663">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
یاسر اسانی: ابوالفضل جلالی بهم زنگ زد گفت نمیایی پرسپولیس؟ گفتم حاضرم از ایران برم ولی به پرسپولیس نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SorkhTimes/140663" target="_blank">📅 23:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140662">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
❌
ورزش‌سه: پرسپولیس به سند جدیدی تو پرونده یاسر آسانی دست پیدا کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SorkhTimes/140662" target="_blank">📅 23:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140661">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
پوریا لطیفی فر: از بچگی رویای پوشیدن پیراهن پرسپولیس را داشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/140661" target="_blank">📅 23:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140660">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🤍
🇮🇷
سردار آزمون با بخشش 5 درصد اموالش به کمیته امداد خمینی به تیم ملی برگشت:))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/140660" target="_blank">📅 22:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140659">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
خبرورزشی
❌
❌
باکیچ با وجود عملکرد خوبی که در فصل گذشته داشت، به اون صورت مورد علاقه تارتار واقع نشده و احتمال جداییش کم نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/140659" target="_blank">📅 22:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140658">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⚽
🤩
سپاهان باکیچ را می‌خواهد!
❌
گفته میشه سپاهان به‌دلیل عملکرد نه‌چندان خوب هافبک‌های فعلیش، دنبال جذب مارکو باکیچ در نیم‌فصل رفته و محرم نویدکیا هم تأکید زیادی روی جذب هافبک پرسپولیس داشته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/140658" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140657">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
تسنیم:
📰
جلسه امروز فدراسیون که به گفته رسانه‌ها برای تصمیم‌گیری برای جام فصل پیش بوده ؛ اصلا راجب به قهرمانی و اهدای جام به استقلال نبود و این موضوع در جلسات بعدی فدراسیون مطرح میشه!!
❌
احتمالا درباره مربی تیم ملی امید باشه
👀
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/140657" target="_blank">📅 22:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140656">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_xlo0PV4GSFw0GpuMWcQKkKkDlCW0cwRd6sWxTXQJjQhYzN8R6ki-XTCRulhGH-yExdbumNDrNA4gUtuhhR-S4TGmfJj3JGSdYkDD_7jgoz0cuZmdoCvNYQgmYy7noJAXMd5DgDeplzCYdavMV-DU-vYcAD67xRLl-O9YxgpLFkA30cMdfgap3OZRLgDxvO1Qj7WCq09hevW0dkuMNXNuEXYqZlFBX4PrtzBaoIuMCWwN8IoJi1ffVN8sfmI4O2TMObIikH7nD0KQgM8UWEvASN1cui_2GSKJQb5rBH5P5XrotI99nendnpD9SPk5U8zAm_zDGHCcfb-rU8pkg_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Belgium -
🇫🇷
France
⏰
Tonight 22:15
🏟
Roi Baudouin
🇪🇺
بلژیک در بازی اول با ۲ گل و ۱۹ شوت ایتالیا را برد، درحالی‌که فرانسه با برد ۱ - ۰ مقابل ترکیه وارد این مسابقه می‌شود. فرانسه در ۵ تقابل اخیر ۵ برد داشته و در این ۵ بازی فقط ۲ گل دریافت کرده؛ ضمن اینکه امشب بدون امباپه بازی می‌کند. از نظر روند، بلژیک در خانه ۶ بازی شکست‌ناپذیر است؛ بنابراین انتظار بازی نزدیک و کم‌فاصله از نظر موقعیت‌ها می‌رود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/140656" target="_blank">📅 21:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140655">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/140655" target="_blank">📅 21:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140654">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
پاسخ مثبت پرسپولیس به برگزاری جام حذفی بدون ملی‌پوشان
❌
باشگاه پرسپولیس با برگزاری رقابت‌های جام حذفی حتی در صورت غیبت بازیکنان ملی‌پوش موافقت کرده و خواهان برگزاری این مسابقات در فصل جاری است.
❌
با توجه به فشردگی برنامه مسابقات و حضور ملی‌پوشان در اردوهای…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/140654" target="_blank">📅 21:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140653">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CslaaZ-MQPwqq1UrGCPFZiYQmQPoqmjGYyAH_xzOPQydekiFd4T-Vt5-GHEeJOj8Svjc41FEs9t-iLbPFCj1FeE2cCtvsj_MyJTH2reK7oIYRFDwPNdvuEC7X963dpfXy0qRqu0PUEOtdctl8I6XC8h7qShXwbmcgkR3XHeg_NVjymb3lY5H2yN2U1BAAp4B8q89ZOZ_Du2qx4w3QcfZnx8C8B6yZ_rF0rxVXR1maCoC0axpZHfDOXtfBCRVWxNBhPCCnaqUvZzO3iN_g3MT2baCwnZzgGzx-5c9-tQPFpHY5jGsvlYo4uvsSCw37QoDddOqXZE_2uNH9wQwyVqhKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بازگشت دنیل گرا به تمرینات پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/140653" target="_blank">📅 21:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140652">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
رسمی:با استعفای حسین عبدی موافقت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/140652" target="_blank">📅 21:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140651">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
افشین قطبی نزدیک‌ترین گزینه به هدایت تیم امید است.
🤝
فوتبال ۳۶۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/140651" target="_blank">📅 21:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140650">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
✅
واکنش فدراسیون فوتبال به اظهارات تاجرنیا درباره جام قهرمانی فصل گذشته
❌
❌
اظهارات علی تاجرنیا، رئیس هیئت‌مدیره استقلال، درباره وعده اهدای جام قهرمانی فصل گذشته به این باشگاه، با واکنش جدی فدراسیون فوتبال مواجه شده است.
❌
❌
پس از موج واکنش‌های مجازی و اعتراض…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/140650" target="_blank">📅 21:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140649">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
همه هواداران پرسپولیس از مدیران باشگاه عاجزانه تقاضا دارن تا ماجرای یاسر آسانی رو تا ته تهش پیش برن.
🔺
آخرش اینه که یه پولی میخواییم بدیم و رای هم صادر نشه به نفعمون، این همه پرونده بوده که هزینه کردیم و باختیم، اینم روش
🔺
دقیقا از روزی که فهمیدن…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/140649" target="_blank">📅 19:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140648">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
پاسخ مثبت پرسپولیس به برگزاری جام حذفی بدون ملی‌پوشان
❌
باشگاه پرسپولیس با برگزاری رقابت‌های جام حذفی حتی در صورت غیبت بازیکنان ملی‌پوش موافقت کرده و خواهان برگزاری این مسابقات در فصل جاری است.
❌
با توجه به فشردگی برنامه مسابقات و حضور ملی‌پوشان در اردوهای…</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140648" target="_blank">📅 18:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140647">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✖️
گفته میشود باشگاه پرسپولیس برای تمدید قرارداد 5ساله با امیرحسین محمودی و 3ساله با پیام نیازمند به توافق رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140647" target="_blank">📅 18:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140646">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
✔️
✔️
✔️
❌
جواد عطایی، سامان نقیبی، ابوالفضل شیرازی، محمد حسین پژوهان،‌ پوریا آزاد رنجبر و محمدامین دهقانی بازیکنان تیم‌های جوانان و امید پرسپولیس بودند که امروز در ترکیب سرخپوشان به میدان رفتند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140646" target="_blank">📅 17:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140645">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ct_ou6uSFYOxNw3utQJqQnwrCQfUgbE-aItwlszDgNsyUBhPnmwzZm7V7NSThnxTG6NlgpObHI9nv1-DL8MTPsvOYv6LVvoLFcaqfgp_a2SljTZsdOkWcUM49EwVrPSqJHfFAXudXpAUQVkwZrmQTXQAvLmstDRcrvhLe3PIPyZ9kiN1jv3repO0cjX4dLNsGgF5b_QFQQTxoKbw2WbUE-_5a6U1URsU7UzK09i7RDVzinRDJjwu8j4ctVe3isHY6rmxAct5Vs2hSJ010plBeNQk2qOgdRVXuy5sRgDsOJXzjUQxRFFtV0Oe6wSKfzdTGvPyvdl11C_i5WfgHLDihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
آتزوری در برابر ترکیه؛ نبردِ کنترل و غافلگیری!
🔥
⚡️
[
ترکیه
🇹🇷
🆚
🇮🇹
ایتالیا
]
⚽️
تقابل دو سبک متفاوت؛ ترکیه با بازی مستقیم و انتقال‌های سریع می‌تواند دردسرساز شود، اما ایتالیا در کنترل توپ و سازماندهی دفاعی دست بالاتر را دارد. باتوجه به کیفیت دو خط دفاع، نیمه اول می‌تواند محتاطانه و کم‌گل دنبال شود و جزئیات کوچک روی نتیجه اثر بگذارد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140645" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140644">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
#رسمی؛ صابری عضو هیئت ‌مدیره پرسپولیس شد
⚪️
⚪️
با استعفای اردوبادی، حسین صابری به‌عنوان عضو جدید هیئت مدیره پرسپولیس معرفی شد. سمت دقیق اعضای هیئت ‌مدیره در جلسه آینده مشخص و بعد از نهایی شدن در کدال اعلام می‌شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/140644" target="_blank">📅 16:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140643">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
مدیران پرسپولیس آماده ارائه پیشنهاد تمدید قرارداد ۴ ساله به اوستون اورونوف هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/140643" target="_blank">📅 16:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140642">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
❌
فوری؛ بیژن مرتضوی که چند ماه پیش در فینال جام جهانی برنامه اجرا کرد، پس از چند دهه حضور در امریکا دقایقی پیش وارد ایران شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140642" target="_blank">📅 15:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140641">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
بیفوما با ساخت ۱۲ موقعیت گل، یکی از خلاق‌ترین بازیکنای این فصل لیگ بوده
🔥
🔴
اگه نصف موقعیت‌هایی که ساخته تبدیل به گل می‌شد، با اختلاف بهترین پاسور لیگ بود!   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140641" target="_blank">📅 15:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140640">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140640" target="_blank">📅 15:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140639">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
💢
💢
✔️
✔️
مدیران باشگاه پرسپولیس هفته گذشته‌ مذاکرات برای تمدید قرارداد پنج ستاره آغاز کردند
❌
پیام نیازمند
❌
محمدحسین کنعانی زادگان
❌
تیوی بیفوما
❌
اوستن اورنوف
❌
ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140639" target="_blank">📅 13:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140638">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
جلالی دوباره مصدوم شد
‼️
🔹
ابوالفضل جلالی در جریان تمرینات اخیر پرسپولیس بار دیگر دچار مصدومیت شد. البته شنیده می‌شود مصدومیت جلالی جدی نیست و بیشتر به گرفتگی عضلانی شباهت دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140638" target="_blank">📅 13:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140637">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140637" target="_blank">📅 11:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140636">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
اجرای بیژن مرتضوی در کنار ارکستر فیلارمونیک بین نیمه بازی فینال جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140636" target="_blank">📅 11:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140635">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccc2b8cd01.mp4?token=hBxUhR_ALVrs8uoDC_5mHI9ffOhYmmkA4RDDmGMe6WGtVtv-xbUwQP8UicXBkvqRY9niG3xiKWDa8ub5lJhqGnsKxza1kzsxVI8D39k6vYn2W8PrKF3mTKjnMqc02t8v7qUXgSQ0I6mnF9KvWGEOo4DlzQmR48FDu7OK-i4d1l9PLUlyOUrYNHeywjlI6rQ_Xk1li-tlYxiMtSnKE6UTT-Gda6JoRJSmOEAP19I6_ZWJfO5ojyJtSae7cntDEk9A3bL5nri4GUrvKEs6sPQSAn2ZTaIqsMSNFOXwARV8ZfTEWHgOR8vzVJmeTR35Pw9Kq_JPRrXbaMTbmjKC2WIbpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccc2b8cd01.mp4?token=hBxUhR_ALVrs8uoDC_5mHI9ffOhYmmkA4RDDmGMe6WGtVtv-xbUwQP8UicXBkvqRY9niG3xiKWDa8ub5lJhqGnsKxza1kzsxVI8D39k6vYn2W8PrKF3mTKjnMqc02t8v7qUXgSQ0I6mnF9KvWGEOo4DlzQmR48FDu7OK-i4d1l9PLUlyOUrYNHeywjlI6rQ_Xk1li-tlYxiMtSnKE6UTT-Gda6JoRJSmOEAP19I6_ZWJfO5ojyJtSae7cntDEk9A3bL5nri4GUrvKEs6sPQSAn2ZTaIqsMSNFOXwARV8ZfTEWHgOR8vzVJmeTR35Pw9Kq_JPRrXbaMTbmjKC2WIbpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دلداری خیابانی به بیرانوند قبل خدمت رفتن
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140635" target="_blank">📅 11:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140634">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
فوری؛ باشگاه پرسپولیس درخواست مدیر برنامه‌های یاسر آسانی از پرسپولیس، پس از فسخ قرارداد با استقلال را هم به مدارک خود اضافه کرده و خیلی امید دارد که سندی بر فسخ قرارداد آسانی باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140634" target="_blank">📅 11:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140633">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
رسمی:با استعفای حسین عبدی موافقت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140633" target="_blank">📅 11:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140632">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140632" target="_blank">📅 09:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140631">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
فوری؛ باشگاه پرسپولیس درخواست مدیر برنامه‌های یاسر آسانی از پرسپولیس، پس از فسخ قرارداد با استقلال را هم به مدارک خود اضافه کرده و خیلی امید دارد که سندی بر فسخ قرارداد آسانی باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140631" target="_blank">📅 09:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140630">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
❌
مدرک جدید پرسپولیس در پرونده آسانی، پیشنهاد رسمی اینجنت او به پرسپولیس بود.
❌
❌
بعد فسخ، این پیشنهاد ارائه شد با این مضمون که او با استقلال فسخ کرده و پرسپولیس می‌تواند برای جذبش اقدام کند.
❌
❌
مدرک از این معتبرتر ؟ / اگر باشگاه پرسپولیس با رقم عجیب و غریب…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140630" target="_blank">📅 09:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140629">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✖️
✖️
#فوروووووی
✅
سپاهان به جمع مشتری های ایرانی بشار رسن در نیم فصل اضافه شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140629" target="_blank">📅 09:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140628">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvSq_mvdfRA78ueLOeFRsCpv1Rj6JMzwaktRIxmwD6PlemTLbIPlyzrURw5X0UzkqFi4wrz0oOlQ5zTn2f1BFa14vZBAFnjvTljjUswI-3piHiNwVuTCWo-fYKz56Z6I6fEo-dYbw0NvXpkowAUrxIybGjaYr5mO7Y8z5Z2v4Bg2YKspRPXHHhNfYzYKa1_fN-jI8qMAwDMktooRBQDfX5AqdIZllCDqEntcrMCNxdJtmsXTg3ES6pZrMWxotfALso3a9RztlcF5ROEcWHN83DfXdLeRvhDUCtEJnhbEcOFicELEUAbrwbY8sgetD8-V_P0-WwNgh6XIKcoDYtn3sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140628" target="_blank">📅 08:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140627">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbT9XDrPdykOwiwb35n6IV1mCGZIRbnbT_iV8-4yXFpKv2LT2Q0Mqf-dc2oW8_pbDN6fkc-AzfQ6HTdVsg4ZItTjLkHnzPm3edTgATGD6Cs0lMWk34mX48Kg8b8UQ3tlzj5A6HHHX9qJBtGYlXmFZcU3lRCERdfDlB77RDKAvF3Tfb62v_wO9QN4-h_uYpiN_4kbER7jJDWMdajbJQB6tkpBeAStowdsFAudFUBrX-07Tj78KSPUg8tV1IjqKpkCkTs2FA9yWsEFbm3z6-zwSrR1wCdFln7agqedtXQ2irkypfuqRUd1i6H414eCTm0FI9WiO1rX_FRoE9ySzpPIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد جذاب خروس‌ها و شیاطین‌سرخ؛ جایی برای اشتباه نیست!
⚡️
[
بلژیک
🇧🇪
🆚
🇫🇷
فرانسه
]
⚽️
فرانسه در ۵ تقابل اخیر مقابل بلژیک شکست نخورده و هر دو تیم هم شروع خوبی در این دوره داشته‌اند؛ بلژیک ایتالیا را ۲-۰ برد و فرانسه ترکیه را ۱-۰ شکست داد. بازی در بروکسل است و بلژیک با فشار تماشاگران احتمالاً شروع تهاجمی‌تری خواهد داشت، اما فرانسه در انتقال سریع بسیار خطرناک است. با توجه به ۵ برد متوالی فرانسه در تقابل‌های اخیر، سناریوی بازی نزدیک و کم‌گل محتمل‌تر به نظر می‌رسد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140627" target="_blank">📅 01:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140626">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5ZSC9Mvqt7FXPfdwYFUWAOnrrCzmtbnIormnZ_R-o2R_JZ9nwSB8MIsM5UxLpyCMcLBz5LHkYGjZ9rWkRWQq5D7oJKPtntA-3urRivWazBi9cT-Jd0R3qrUsJ0LgfwrwonfF3tWmWvKeqGDNlg4-DIxZ98tIYb6XuRQpHUoZxbZHSs96H4I9ObWX0OzeHAwHq8iln9oDS-A2d9N_iM13TZGwaK7oAADceO84vOYvfArim7Xqq8R90wX0alopJWkI4ZiRcUy4pBXlQPFBVACtEKX7kcJCg9QEYl8MchdlyE0183TcCTof8dZZShrbXHdIFxfCuhmZUbffoTTRAOGXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️
🔴
با دستور پیمان حدادی، شورای هواداری تشکیل شد تا صدای هوادارا رو به باشگاه برسونه و پیگیر خواسته‌هاشون باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140626" target="_blank">📅 23:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140625">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYqkcPb9dCPTFBMGHBKaVWVewFkKCYOU6kYEmiElBq-xIwbMyFDqw0SHBn7ODH2jfS_-ZAbjINyG-sHKvKTfj8fXabOBBUqOXw34uXJGk3mFfubiMPPps7KGzEqPwaqu86WwTOFVOEINYTgfGeoKy9Ez9Usp61M4fJ-gnAguNwmqKkro8A_PLT5X5ukSyV22HZvB0s-Cc9xMxRuhY6n-f2e5f5NkrwrRzLpg0lxNpwSagz0oDrHaFWwY2SmWX8bTPlFa-qvBF0fGsG7LqMaPGsIy1-Q194q_pkv7jKhiD3dIPfasxRmqDDJTDt8_sjzTDYK2MrKXWmg6jxfNi3bbVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☑️
آقای فکت رسانه‌ای شما خواهشا از آسیا و سهمیه صحبت نکن که خودت با اون باخت ۷تا مقابل الوصل به اندازه کافی آبرو ریزی کردی بعدشم از سهمیه ای صحبت میکنی که بهتون هبه شده مثل پنالتی های معیشتی‌تون
❌
❌
شمایی که باشگاهت که با وجود ۶-۷ تا خوردن تو آسیا حرف از تخصص می‌زنین ، هنوز ۷-۸ هفته مونده به پایان لیگ خودتون قهرمان میدونین و دارین گدایی میکنین، جام ندیده های بدبخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140625" target="_blank">📅 23:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140624">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
❌
❌
❌
❌
❌
❌
❌
🚨
اورونوف در تعطیلات موفق شده ریکاوری خوبی رو پشت سر بگذاره و از نظر روحی و بدنی دیروز  آماده نشون داده
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140624" target="_blank">📅 23:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140623">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140623" target="_blank">📅 23:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140622">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfce03f041.mp4?token=Nh7SMRSxd-rNfOQYnoeiiUiWAb5eTIh6JDVyxS-fBNzwDNWFRNnwlTQkRQEkk66xk3cLA_PyinjZa_OBMijDX-OrOYbsG-X1kKx22Z63StUnwfUrNEqzBiQTGnhhO8FQJ7JRN5lU77QbSfnIsCX5qGQaGhFzihuVDFsU_cf6Sh3x73rPQ78ayFLAv8yjvYlinu2seMmDzZeQ7WaC4kMXkKfKQbInsomDD2uZI-ztt4drh3ce_m9lh7EOW7EUszhOfTGIyfmnhbx-nX9-4cSA1H4a5GC468hhL3XBmJSkOSSRSMlUB0vfgmyheG-Xpw1RKoECjmDrI3YqUiiXk_eGyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfce03f041.mp4?token=Nh7SMRSxd-rNfOQYnoeiiUiWAb5eTIh6JDVyxS-fBNzwDNWFRNnwlTQkRQEkk66xk3cLA_PyinjZa_OBMijDX-OrOYbsG-X1kKx22Z63StUnwfUrNEqzBiQTGnhhO8FQJ7JRN5lU77QbSfnIsCX5qGQaGhFzihuVDFsU_cf6Sh3x73rPQ78ayFLAv8yjvYlinu2seMmDzZeQ7WaC4kMXkKfKQbInsomDD2uZI-ztt4drh3ce_m9lh7EOW7EUszhOfTGIyfmnhbx-nX9-4cSA1H4a5GC468hhL3XBmJSkOSSRSMlUB0vfgmyheG-Xpw1RKoECjmDrI3YqUiiXk_eGyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
مدل موی عجیب و غریب یک بازیکن در کونکاکاف
▶️
#ویدیو
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140622" target="_blank">📅 22:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140621">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYZ1_UtSgb4tYyl_k3AWDPaG4wQS92V9JNXIqWsfytQy2tWd6IolX45mTQL8Do8M9L-itoLYRsuGf-BD7qxh_vEyHOAXYIdGCMK4oc6b6qCyeaQ_DhZJ_n5XIM9bdtz66cLuSQRo8RBnybxM_mGAEd-ChT3bcLBX8Nkq-4ZFEntOCvNh-ukM2zfEOWcdkU4T7YDBNQxjtWzLsuI12BW_LYkoPbNEtaSipJdriP4Cw-J0hGUe8cUCrU0pQRGq1nUFB8VlcWWr_BvSazvns_HJAYqaABHXH4jbSESe1W3S6ZZmH0P7VW28Thl5gZIge3M8nOG7L76bUu-xc59I3Zbkbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#
یادآوری
❌
وقتی قهرمانی پرسپولیس در کرونا درمیان بود‌، منطقِ اعتراض‌شون ٣٠ امتیاز باقی مونده و احتمالِ امتیاز از دست دادن پرسپولیس بود
🚨
حالا که پای قهرمانی خودشون درمیانه، ٢۴ امتیاز باقی‌مونده و احتمال امتیاز از دست دادن خوشون رو ندید میگیرن گدایی جام دارن‌. چرا آنقدر بی‌حیایید‌
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140621" target="_blank">📅 21:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140620">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
تیوی بیفوما:
✅
• سرعتم روی گل به ملوان ۳۷ کیلومتر بود/ سال گذشته اتحاد تیمی نبود و شرایط خوبی نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140620" target="_blank">📅 21:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140619">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⭕️
⭕️
ابوالفضل رزاق پور مدافع چپ تیم فولاد: از پرسپولیس آفر دریافت‌کرده‌ام‌اگه دو باشگاه به توافق کامل برسن درنیم‌فصل راهی این باشگاه خواهم شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140619" target="_blank">📅 21:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140618">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
🚨
هفت ورزشی؛  به استقلال خیانت شد؛ برگ برنده پرونده آسانی به دست پرسپولیس رسید!
🖍
ایجنتی که به باشگاه استقلال رفت و آمد دارد، مدرکی به دست باشگاه پرسپولیس رسانده که برگ برنده این باشگاه در ماجرای شکایت از یاسر آسانی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140618" target="_blank">📅 20:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140617">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRttS67JCp0mIN4hkrS5Grrkn8Iw7Jp8uXK7LBuQkfMaw8mnAbzuyhQ80cr4wgyC93fpU8NchdURUHkKH4JM7ZvWQ1VnfyddhljtvI0aDrK7su2-a0ywlmUROJjf3ZNcGtRNKZrKFjQSY4s1pFTrdo8CiWj_nyLbeAJscYZPLqtSIudnyHjSTuOE9G05_oIaWD5HGjLspOyNpoOrbNw9ULGKH6QHyu-gIGCZxHQnrFq9WcAT3SqlpTLeiay2PLJzBp1iPcr-QsGmJYQDwcPOYieycz-tAzdeQkId0P0A1uaFCUtzzjPEheGYm4ih0U6n3Hi51wrk-gHWNNjfTvjVmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد ستاره‌ها؛ شبی برای تماشای فوتبال در بالاترین سطح
⚡️
[
نروژ
🇳🇴
🆚
🇵🇹
پرتغال
]
⚽️
نروژ با تکیه بر قدرت هجومی و انتقال‌های سریع، می‌تواند بازی را به دوئلی فیزیکی و پرموقعیت تبدیل کند. پرتغال با مالکیت بیشتر و کیفیت بالاتر در یک‌سوم هجومی، به‌دنبال کنترل ریتم و استفاده از فضاهای پشت خط دفاع خواهد بود.
سناریوی محتمل: گلزنی هردو تیم بسیار بالا می‌باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140617" target="_blank">📅 20:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140616">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⭕️
⭕️
⭕️
دنیل گرا مدافع راست خارجی پرسپولیس به تهران بازگشته و اماده حضور در تمرینات گروهیه/قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140616" target="_blank">📅 19:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140615">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
بالاخره انتظارها به سر رسید و دنیل گرا پس از پایان مصدومیت، طی یک یا دو روز آینده به تمرینات گروهی تیم پرسپولیس اضافه خواهد شد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140615" target="_blank">📅 18:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140614">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
زنوزی علیه کیسه
❌
زنوزی: کیسه خیلی جام دوس داره بیان من پولش رو بدم  برن منیریه برای خودشون جام بخرن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140614" target="_blank">📅 18:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140613">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⭕️
⭕️
فارس: آرای هیأت رئیسه فدراسیون به قهرمانی استقلال ۷ رأی مخالف و ۴ رأی موافق داشته و به این ترتیب احتمالأ جام به این تیم اهدا نمیشه :)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140613" target="_blank">📅 18:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140612">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
✔️
فدراسیون به باشگاه گفته که مدرکتون برای یاسر آسانی کمه و اون مدرک اصلی و قوی که ما میخایم رو ندارید شما ، حالا باشگاه از طریق یکی از ایجنت های ایرانی یاسر آسانی یه مدرک فوق العاده قوی رو کرده که فسخ رسمی این بازیکن با استقلال رو نشون میده و فدراسیون هم…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140612" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140611">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140611" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140610">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🏅
تأکید مخالفت باشگاه تراکتور به اعلام نام استقلال به عنوان قهرمان فصل گذشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140610" target="_blank">📅 18:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140609">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6jNMb71sYKvKBuuLe5hJWs7EiVpTo4M-XnljBzIV1jHrulDbo9yP4nlc8ddFiUTJ6dL8MNxWYt6QvjKiELzukTBIdBHLy_3WfubKqtrf7Yasc84RgEReS9FvY0SMtUdBOwRM8EOtFatygfX38EVMRSIv3s1Af-EQoRrQWV8_kSGcoAz0KCZHGyhvIwNeB4ZHbT5D5isqRaNrcBJeHRVdBAREWTrOP8KVPqRNywJ9mD5ER1f-n_VEjF23X3cR_M68YCA2g2i7ssawCCzUHSaY5SjjczZ1hmWCn_y87o9cFw22Y_5YKL3y_jMGEAP-o-hBMSRHs62xMoxjKtN067qPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
تأکید مخالفت باشگاه تراکتور به اعلام نام استقلال به عنوان قهرمان فصل گذشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140609" target="_blank">📅 16:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140608">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
❌
علیرضا بیرانوند سربازه و معافیت نخورده و هر بازی که انجام بده غیر مجاز هستش / مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140608" target="_blank">📅 16:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140607">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EffrYfQEy0_Srcx7QvtIyTHJvmNe3TzwDUZehiJXgQOEPUsRXDMvTkXzrviSMMQZ_tBvwTyoM0Qosu9OX3f_9InkalaudWdCcWKJoritUk4qHIpvP86ChqX1WadzoGkZCBgGfkJQY2WdTPZuiCBbKmY2qhQRMga2YWyqXETpAM7PWF0fQ3Glu-lbH3HQPMOrAS8-bszzx-ogyUt4EHiAFanPu6_5VM6FgTbWFPUQQwtLcQWuPXvWrbJUpBHGRvHyjTPqDucFlPa8lSepNcGubhcPqPD4E-Xndmf0tvSsgrDDakhhiBPOOhjQagWDdxsQOPNEheBAcZUDK3RkqBrJiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Norway -
🇵🇹
Portugal
⏰
Tonight 22:15
🏟
Ullevaal Stadion
🇪🇺
نبردی بین فوتبال مستقیم و مالکیت هوشمند؛ جایی که هر اشتباه می‌تواند معادله بازی را عوض کند. پرتغال با تکنیک و کیفیت در یک‌سوم هجومی خطرناک‌تر است، اما نروژ روی انتقال سریع و قدرت خط حمله می‌تواند ضربه بزند. انتظار می‌رود بازی با ریتم بالا دنبال شود و جزئیات در محوطه جریمه، تعیین‌کننده برنده باشد.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140607" target="_blank">📅 16:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140606">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
سازمان لیگ مجددا کارت بازی علیرضا بیرانوند را به مدت یک ماه تا پایان مهر برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان می تواند  در بازی هفته هشتم با استقلال تیمش را  همراهی کند.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140606" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140605">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
باشگاه پرسپولیس با برگزاری رقابت‌های جام حذفی در تعطیلات جام ملت‌ها و بدون حضور ملی پوشان موافقت کرد/ورزش‌سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140605" target="_blank">📅 15:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140604">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
باشگاه پرسپولیس با برگزاری رقابت‌های جام حذفی در تعطیلات جام ملت‌ها و بدون حضور ملی پوشان موافقت کرد/ورزش‌سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140604" target="_blank">📅 15:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140603">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
❌
فووووووووری از ورزش سه
🚨
اولین خرید پرسپولیس در نیم فصل مهدی حسینی مدافع‌ وسط ۱۹ ساله شمس آذر خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140603" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140602">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🤝
🤝
مدیربرنامه‌های فرهان جعفری: فرهان اوایل دی‌ سربازی‌‌اش به‌پایان‌ میرسه و میخوایم توافقی که هم منافع او حفظ شود هم منافع باشگاه خوب ملوان حفظ شود از این تیم جدا شیم.
❌
❌
فرهان از دو باشگاه پرسپولیس و استقلال آفر دریافت کرده و در پنجره نیم فصل راهی یکی از…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140602" target="_blank">📅 15:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140601">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
طبق شنیده ها
❌
ابوالفضل جلالی مجدد دچار مصدومیت شده و بزودی مدت زمان دوری او از میادین مشخص خواهد شد
😰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140601" target="_blank">📅 11:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140600">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⚡️
⚡️
⚡️
رضا شکاری مجوز بازی نداره و صرفاً در لیست بازی قرار داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140600" target="_blank">📅 11:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140599">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
امسال جام حذفی برگزار نمیشه و تیم های اول تا چهارم سهمیه آسیا خواهند گرفت!///فوتبالی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140599" target="_blank">📅 09:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140598">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⚡️
⚡️
⚡️
رهایی کاپیتان سابق پرسپولیس از بیماری سرطان
⚡️
⚡️
سید محمد پنجعلی کاپیتان سال‌های دور پرسپولیس، مدتی را به دلیل درگیری با بیماری سرطان زیر نظر پزشکان بود.
⚡️
⚡️
خوشبختانه شماره ۵ پیشین سرخپوشان موفق به شکست بیماری سرطان شده است
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140598" target="_blank">📅 09:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140597">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">😰
محمد احمدزاده، سرمربی اسبق ملوان: یه مقام استقلال‌ به من زنگ زد و رشوه ۵۰ میلیونی به من دادن که به استقلال امتیاز بدم تا پرسپولیس قهرمان نشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140597" target="_blank">📅 09:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140596">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
✅
✅
مذاکرات پرسپولیس با بشار رسن در حد واسطه‌ها در جریان بوده و هنوز به مرحله مستقیم نرسیده است. / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140596" target="_blank">📅 09:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140595">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
✔️
بازگشت اورونوف به تمرینات پرسپولیس
✔️
با اعلام باشگاه پرسپولیس، اوستون اورونوف به تمرینات این تیم بازگشت. این وینگر ازبکستانی در فیفادی به اردوی تیم ملی کشورش دعوت نشد و کاناوارو ترجیح داد روی نام او قلم قرمز بکشد.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140595" target="_blank">📅 09:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140594">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_x16iTDvh6n1q-4RXPj3RN6OFCmRi203CkhD4za82iXj6NP0R0XV4npeHxX815FLVzXf4ROwbU2frwQKKvOZvRrwKNoZJ-YvUGvMRzuyG_2eO0VmqmRwyYDG_t595OJM7WKFVx37N5fCcbQv0VQRw8-0fGNUyTnw0xVylfte8P6B_bzMHY3QwC0SvVCoAQnZbTMbCRfV-k6WVTCGGSnC-Y8iRYXu6diiis-TBDpjbqlMk2ox-JBaEii6v4cOc8XSu4zgCqJubyC-gLwDvdo2Fvh8rzv7m2mfFy3qLb3MxTyI_MGs3HWwdIpg08a0bPMCI6mwnrX1vrHDoEXbToSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140594" target="_blank">📅 09:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140593">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGzpk0U1SUL59HqVyxO2lXx4OAkU1e4tLZispRaVXHDFGRW1d2Gk0kdNhggI2Xvvgj2Zi_FCUmFfq8LqvDKMas2FYKaAxtDvRVAh7nI_MY-_j6NNOJO-weJDrQvsBY_FNqF4RXcS3OuFsEOJtidsQeMK9eJuVEDCXWJcrK8dR8dqtiiAatUuVKADwN9a0yxDpEkGBYGYrocJ3Es2ZUs7Yk_uVkrT8xleOVoHI9VwW_TY3hX_nlVWfywWuc6Bv_WlCxkiq1YYVpuL1g-BYJIZBKruXwcfY41cjKSjy1a7aabL9DXJU3UJVd4JEm8BxS0j1RBKfZIGiJIg5y-u1As53g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
فرداشب لیگ ملت‌های اروپا پرهیجان دنبال خواهد شد؛ بازی‌هایی که روی کاغذ ساده‌ان، اما داخل زمین قطعا داستان فرق می‌کنه
🔥
⚡️
⚽️
فرداشب چند تقابل نزدیک و پرریسک روی میز داریم؛ از برتری‌های نسبتاً مشخص آلمان و اتریش تا نبرد کاملاً متعادل نروژ و پرتغال. در بازی‌های ساعت ۱۹:۳۰، هلند و دانمارک دست بالاتری دارند، اما صربستان و ولز می‌توانند معادلات را تغییر دهند. در ادامه، آلمان مقابل یونان و اتریش مقابل کوزوو از نظر اعداد شرایط بهتری دارند، در حالی‌که ایرلند با اسرائیل و نروژ با پرتغال نزدیک‌ترین دوئل‌های شب هستند. یک شب شلوغ با چند بازی که اختلاف روی کاغذ، لزوماً تضمین‌کننده نتیجه در زمین نیست.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار‌هارو رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140593" target="_blank">📅 02:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140592">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
✅
✅
فشار شدید امریکا علیه ایران
✔️
✔️
امارات، ترکمنستان و تاجیکستان ۳ کشور جدیدی هستند که حریم هوایی خودشون رو به روی هواپیماهای ایرانی تحریم کردند !
❌
مکزیک برزیل و بقیه کشور ها هم رسما تحریم کردند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/140592" target="_blank">📅 00:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140591">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⭕️
⭕️
قرار شده جام قهرمانی در ازای بدهی ۷۰۰ هزار دلاری فدراسیون به هلدینگ، به استقلال تحویل داده بشه!
✔️
✔️
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/140591" target="_blank">📅 00:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140590">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140590" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140589">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/140589" target="_blank">📅 23:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140588">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
تاجرنیا: از سازمان لیگ تقاضا دارم قهرمان فصل قبل لیگ برتر را اعلام کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/140588" target="_blank">📅 23:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140587">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
🔴
فارس:
⬇
بودجه پرسپولیس در فصل جاری ۳ هزار میلیارده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/140587" target="_blank">📅 22:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140586">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
✔️
✔️
بازگشت اورونوف به تمرینات پرسپولیس
✔️
با اعلام باشگاه پرسپولیس، اوستون اورونوف به تمرینات این تیم بازگشت. این وینگر ازبکستانی در فیفادی به اردوی تیم ملی کشورش دعوت نشد و کاناوارو ترجیح داد روی نام او قلم قرمز بکشد.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140586" target="_blank">📅 22:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140585">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
#فوری | ترامپ در سازمان ملل:
🔻
با تصمیمی بزرگ در مورد ایران روبه‌رو هستم؛ توافق یا نابودی کامل
‼️
🔻
آیا به توافقی دست یابیم که به این کشور اجازه دهد به ملتی بسیار بزرگ‌تر تبدیل شود، یا اینکه آن را به‌طور کامل نابود کنم
⁉️
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/140585" target="_blank">📅 21:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140584">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
‼️
🔴
ادعای جنجالی کریمی: خودسرانه برای بیرانوند دفترچه پست کردند؛ در تلاش‌ برای معافیت پزشکی او هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/140584" target="_blank">📅 21:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140583">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtjR8vhgGfLRKk8zB7FIS_EqFDhJNoxi5NsdJm0bfgXp6Kre2mibWnhtQLhNgp3yt9pKlMLNgma-EAIhUpFTGo4Xv9XPEJm2GwCq9apeW6J-TOGS2PfL44UIiBrFiy6wmG0eVo3cO2oQOwxg5iG3hwEnFqBqkVBaRUDamSzMxeejkqFMkKw7F0D5DdDqgtED-j4WuCf_gVyPL0_EtBJnWCpauZQWHZz7_hmVCM0f-34-aO_r0jPymE7QbRi_ay45TxVEhbl4XvyIt1XofAaQpzMdK2p3t9uwF5CpkCe4UrvLZE0-OVSHDqJsMhLCFOvHBzYa_j4NSMadxuD_20tvjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
❌
افشاگری فنونی‌زاده از قلعه‌نوعی‌‌:
‼️
من با سند‌ و مدرک به شما می‌گویم ۱۷ تا مربی در عرصه‌های مختلف ملی و باشگاهی که سابقه استقلالی دارند، توسط قلعه‌نویی به‌صورت مستقیم یا غیرمستقیم روی نیمکت تیم‌های مختلف ملی و باشگاهی نشسته‌اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140583" target="_blank">📅 21:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140582">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
❌
با دعوت احسان حاج‌صفی به اردوی تیم ملی این بازیکن در صورتی که مقابل ازبکستان و روسیه حتی یک دقیقه بازی کنه رکورددار بازی با پیراهن ایران خواهد بود و از علی دایی و جواد نکونام عبور خواهد کرد
✔️
جواد نکونام ـ 149 بازی ملی
✔️
علی دایی - 148 بازی ملی
✔️
احسان…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140582" target="_blank">📅 21:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140581">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140581" target="_blank">📅 21:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140580">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPtrhMb23ISSMAfjybqjOktj83PpbDMG4q7o6uB_ecrzIW2x4aOKB59tCEY9FVDo0V1NEtkp2ILWFg5gsXaiBzFI3yDtoqxx8BGNNBtp-2B1MK3vxHOr1R35ueo2LV6SceiAK20-EutACCehfw18XRrhGUEONjkOX6t30Rr8Nv1cNt-2kNIRKT3qsomC543O3aNCmtF-svv0pLSF7TsnhZ4fHGl1w3w1npZVXAa95gpyFeF8DdS0mmz8MsqVYbm5qj0sVfiz_-83v7OUszFCgUg0lC9FCw72CZVwS7YGvD7ncGrRLjsurlne2sI4vnHLPABAC8NKwPhXCzT1Krs7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
England -
🇪🇸
Spain
⏰
Tonight 22:15
🏟
Wembley
🇪🇺
اسپانیا با ثبات بیشتر در کنترل بازی و خط میانی منسجم‌تر وارد ومبلی می‌شود؛ در مقابل، انگلیس روی سرعت انتقال و کیفیت ساکا، بلینگام و کین حساب می‌کند. غیبت رایس، پالمر و چند مهره دیگر می‌تواند تعادل انگلیس را تحت‌تأثیر قرار دهد، در حالی که اسپانیا با هسته اصلی قهرمان جهان و اروپا حفظ شده است. از نظر فرم، اسپانیا در ۵ بازی اخیر ۵ برد داشته و انگلیس ۴ برد و یک شکست ثبت کرده؛ بنابراین انتظار یک بازی نزدیک با موقعیت‌های دو طرف منطقی است.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140580" target="_blank">📅 20:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140579">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
طرفداری: علی قلی‌زاده از پرسپولیس و تراکتور پیشنهاد دارد، ولی بازگشت‌ش به ایران منوط به این است که مشکل سربازی او حل می‌شود یا نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140579" target="_blank">📅 19:42 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
