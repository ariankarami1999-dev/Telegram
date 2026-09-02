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
<img src="https://cdn4.telesco.pe/file/Mw51jRYg7_Ij66wchzLCKonqFMuLWzUkOdp-j4ijMrD036jxt2pzysbAu654XKR9DMQ18o815_P5LxpMeXcKv7ztWNoEItPF22WWUKQpD2Ob76yAIg0Xlkalwhqu7s-DstTr8BKhsc0OK3bJ76vzTL8HoXhCDlSpHMBB9Q2q3fg7y8Ey02OLY2jj4FTzDy8lL3pYreompPHv7zfmTgZSe5ExdAC7YgwHsxQnB2l9aXDKctbVBfCThOE7IRUT6OhDdS6URNysPwkuaPTatNxazQr1ulD1BkzZ_CTFiBTnpg9R2r2RDTGnh-tpeWTkNCu2zFht3PzYXs7nhe0E8hAx9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.43M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 10:41:44</div>
<hr>

<div class="tg-post" id="msg-686497">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
شهادت ۴ نفر از رزمندگان هوافضا در کرمانشاه
🔹
روابط عمومی سپاه استان کرمانشاه در اطلاعیه‌ای از شهادت ۴ نفر از رزمندگان جان‌برکف هوافضای سپاه استان کرمانشاه در حمله رژیم سفاک و تروریستی آمریکا خبر داد.
🔹
اسامی شهدا: شهید رضا محمدی، شهید شهرام جعفری، شهید علیرضا شکیبا و شهید جعفر کهریزی.
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/686497" target="_blank">📅 10:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686496">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyDJemRSpZtVxhtkO2ojoMi595lZxGfnwOjtfvhC9kNYR7Q-AiE7J-StV-ONbdkMEZCasRMtBF8Is1EO23p1Rqg0zXUR18T7sI4STIEVzNjxh5YLjJfynsf0jurZKTC0LvFoldyXHCoLrrAMHOv9gc2G2iP-o1-hXgCvDs01PNo3b8QCbMc6zPoithDvLtKfq6UapaDIXvZg0blD4zz8Kzlw6wuU4XKItbmBNdUUiPT3tpFJzG8_nrEgd4U4-jhKEtHOGrPHTz2HwnbTEcxjKRtQsQB5j6SSffCRQLM8OzzPnF2Qm3Jiu7ir6OtvGDKrCBc_Jywxi8OQrgbRK1Y8LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری رضا صادقی در واکنش به حمله ارتش تروریستی آمریکا به مراسم عروسی در سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/akhbarefori/686496" target="_blank">📅 10:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686495">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
۳ رزمنده بسیجی شهرستان دیر درجزیره لاوان به شهادت رسیدند
جانشین فرمانده سپاه سیدالشهدا(ع) شهرستان دیّر:
🔹
در این تهاجم ناجوانمردانه، شهیدان والامقام «مهدی بحرانی»، «حسین صالح‌نژاد» و «حسن مؤمنی» به فیض عظیم شهادت نائل آمده و تعدادی دیگر از نیروهای مدافع امنیت شهرستان دیّر نیز مجروح شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/akhbarefori/686495" target="_blank">📅 10:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686494">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19494596d8.mp4?token=kMw-oSYpFc0RkPI845haplHAaqZKLkqIkNSdFia9OOhfMvBf_rYm6SOnqBMh68MC9Ldr7eYl5LpOwsizIIPKHfEfkeUrWiuwpvOtq_6xQa74w2ig9442c8dxUtr51jf-yYs5wnfV-ShpQ7VHI2JqHAW4iSrwXivhNkRVh14yHVZ5E84rkhIsiSPYtx4O0qYB4lcrC_bCuextG1dZEL1tr91VadMqFJQ-G-oAO0CxrGzzxA8ykuEVHl0CmG5H9M1IZDTrxtT80rrhNDn7tdq-RIS6znhI3N8tEo44csaPoG-c0mCZ_UP_BFgwpSYRhUcwTSvWhPKTMq3h2K6px2Vlag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19494596d8.mp4?token=kMw-oSYpFc0RkPI845haplHAaqZKLkqIkNSdFia9OOhfMvBf_rYm6SOnqBMh68MC9Ldr7eYl5LpOwsizIIPKHfEfkeUrWiuwpvOtq_6xQa74w2ig9442c8dxUtr51jf-yYs5wnfV-ShpQ7VHI2JqHAW4iSrwXivhNkRVh14yHVZ5E84rkhIsiSPYtx4O0qYB4lcrC_bCuextG1dZEL1tr91VadMqFJQ-G-oAO0CxrGzzxA8ykuEVHl0CmG5H9M1IZDTrxtT80rrhNDn7tdq-RIS6znhI3N8tEo44csaPoG-c0mCZ_UP_BFgwpSYRhUcwTSvWhPKTMq3h2K6px2Vlag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گنده‌گویی جی‌.دی‌.ونس: در حال حاضر، سعی می‌کنم تا حد امکان بر انجام کار خدا تمرکز کنم و اگر این کار در نهایت به آخرالزمان منجر شود، اشکالی ندارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/akhbarefori/686494" target="_blank">📅 10:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686493">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رویترز: آمریکا جای چین و روسیه را در نفت ونزوئلا می‌گیرد
🔹
منابع خبری ترکیه: دو کشتی در دریای مرمره در سواحل استانبول با هم برخورد کردند و ۱۰ نفر مفقود شدند
🔹
سی‌بی‌اس نیوز: ذخایر نفت آمریکا به پایین‌ترین سطح در۴۴ سال گذشته رسید
🔹
استقرار گسترده نیروهای حشد شعبی در مناطق بیابانی غرب استان الانبار عراق برای مقابله با داعش
📲
⁣
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/akhbarefori/686493" target="_blank">📅 10:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686492">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaMxNy8K7OGYnzIAhD0sGIz3Zak_Ia12e2w2FFGH_wZx3KLZ6hjqaG7or2NP-lQVNqaLi5khivUz02EcVOmzhGTnSWSu7a9tkZH9dqgsqxCv6xdoB8axIL7ZWx4hFuqyqmGsEm6k9fsozLCrv-R3rQ8QvBi9jmmO8_a7s0KuSR-jQ3qjALQDGN58Gk2jYkhJRnqVKGW_Fk_2I3pVhLUamcLiRcBJvZGWTIs2pclFrNutBRxGKfr_hWmASe3KHugcabkwV0qctKqEtipHdyn7_lJr0koER_Vr91lq2LpdRoFYZy7ei8Q9ZOVQaqIMeqcBGROSh9n6TsygAVkeXPJFzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکاور بهمئی در عملیات مقابله با پهپاد متجاوز به شهادت رسید
معاون فرهنگی بنیاد شهید کهگیلویه‌وبویراحمد:
🔹
سید مالک موسوی‌تبار، متولد ۱۳۷۰ و از اهالی روستای تنگ‌گر بخش ممبی شهرستان بهمئی، صبح چهارشنبه ۱۱ شهریورماه در جریان انجام مأموریت و عملیات مقابله با تحرکات پهپاد متجاوز به شهادت رسید.
#اخبار_کهگیلویه_و_بویراحمد
در فضای مجازی
👇
@akhbar_kohgiluyevaboyerahmad</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/akhbarefori/686492" target="_blank">📅 10:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686491">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
واکنش قطر به درگیری‌های شب گذشته
ادعای وزارت خارجه قطر:
🔹
ما بر ضرورت توقف فوری و کامل تمامی عملیات نظامی و حملاتی که امنیت و ثبات منطقه را تهدید می‌کنند، تاکید می‌کنیم.
🔹
ما خواستار بازگشت جدی به مسیر گفتگو و مذاکره و پایبندی به توافقاتی هستیم که از طریق تلاش‌های دیپلماتیک به دست آمده است./ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/akhbarefori/686491" target="_blank">📅 10:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686490">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خبرفوری
pinned «
♦️
سپاه کدام پایگاه‌های آمریکایی را هدف قرار داد؟
🔹
کمپ تیتین در اردن
🔹
نوع حمله: سنگین با موشک‌های بالستیک
🔹
هدف: پادگان راهبردی تفنگداران و نیروهای واکنش سریع آمریکایی، تاسیسات و بالگردهای تهاجمی
🔹
نتیجه: کشته شدن تعداد زیادی از نیروهای آمریکایی؛ انهدام چند…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/686490" target="_blank">📅 10:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686489">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e4265d064.mp4?token=vgG76nqQlLObtiSn6_uyrMN0q6bRPrHEUmGxhgwKP0M5Spip1key9MJ-ZMaa_6gl05LYLiEoK_Ckn3P9Rhycv8-r12i-SKaogima-zB3NFhYCDhdGZDgo6txEPUcGoPsC_P5e41WKhCP93IOnf9FOoLE9RlpXwkfE6welGWznqt8x6AzQWiPWxvbspcIkVhikKnL0bv2_KAIh7NNpLm3a6iHKnNEYqPTFtsm1ZNkTIxYYjgwVV-ArTEUxA5oP7_y-Wy9JflJSxvny3iDI4Ulco5NHK9gYSjLI-_J3lkI5fewJ6iwjN0EOby2Gwtqys5QGl1A15Ikk_dE-vCcRCkAxKgSF-4aV_fzRbvoe6tXOD3xZdtn7YAEhrJ9IoWSIzB5nQmetnrxUNtN7qyY1q2CYFcYRJHB1VXVyeHSz4IqUsRFpknH62DbGsjPMdug5Tqyb1-jo8yxa-scRksreqqZZG99GPkcrNJFF7IcSuioUSP9C2NPiRHTEZIruPq9zDDIkDChSMK8FbxaQXp4fj26lmgRGFrdqELUIFTXITd6E4VZfusP439uLbWE9OCNV8vlPld0vKgs3E3ryxpXXPvRkyPcTg6wVnWC5H_4eX2UtvSQfrWMRLpasOt8g7K51VhPw4vTGq7MNFpTqQhzduAkMZ2MInKdyfndB5-nHRarRXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e4265d064.mp4?token=vgG76nqQlLObtiSn6_uyrMN0q6bRPrHEUmGxhgwKP0M5Spip1key9MJ-ZMaa_6gl05LYLiEoK_Ckn3P9Rhycv8-r12i-SKaogima-zB3NFhYCDhdGZDgo6txEPUcGoPsC_P5e41WKhCP93IOnf9FOoLE9RlpXwkfE6welGWznqt8x6AzQWiPWxvbspcIkVhikKnL0bv2_KAIh7NNpLm3a6iHKnNEYqPTFtsm1ZNkTIxYYjgwVV-ArTEUxA5oP7_y-Wy9JflJSxvny3iDI4Ulco5NHK9gYSjLI-_J3lkI5fewJ6iwjN0EOby2Gwtqys5QGl1A15Ikk_dE-vCcRCkAxKgSF-4aV_fzRbvoe6tXOD3xZdtn7YAEhrJ9IoWSIzB5nQmetnrxUNtN7qyY1q2CYFcYRJHB1VXVyeHSz4IqUsRFpknH62DbGsjPMdug5Tqyb1-jo8yxa-scRksreqqZZG99GPkcrNJFF7IcSuioUSP9C2NPiRHTEZIruPq9zDDIkDChSMK8FbxaQXp4fj26lmgRGFrdqELUIFTXITd6E4VZfusP439uLbWE9OCNV8vlPld0vKgs3E3ryxpXXPvRkyPcTg6wVnWC5H_4eX2UtvSQfrWMRLpasOt8g7K51VhPw4vTGq7MNFpTqQhzduAkMZ2MInKdyfndB5-nHRarRXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه فقط نیم‌ساعت وقت داری این غذا برای خودته   مواد لازم:
🔹
پیاز
🔹
سینه یا ران مرغ تکه شده
🔹
فلفل دلمه‌ای
🔹
زرشک
🔹
رب ‌گوجه #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/686489" target="_blank">📅 10:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686488">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
سپاه کدام پایگاه‌های آمریکایی را هدف قرار داد؟
🔹
کمپ تیتین در اردن
🔹
نوع حمله: سنگین با موشک‌های بالستیک
🔹
هدف: پادگان راهبردی تفنگداران و نیروهای واکنش سریع آمریکایی، تاسیسات و بالگردهای تهاجمی
🔹
نتیجه: کشته شدن تعداد زیادی از نیروهای آمریکایی؛ انهدام چند تاسیسات و چند بالگرد
🔹
پایگاه پرنس حسن در اردن
🔹
نوع حمله: حمله سنگین با موشک‌های بالستیک
🔹
هدف: آشیانه پهپادهای RQ-4 و MQ-9 و زیرساختهای فنی
🔹
نتیجه: انهدام پهپادهای آمریکایی؛ هلاکت تعدادی از خلبانان و خدمه فنی؛ آتش‌گرفتن زیرساخت‌های فنی
🔹
پایگاه‌های آمریکا در اربیل عراق
🔹
نوع حمله: حمله تلفیقی موشکی و پهپادی
🔹
هدف: مرکز تعمیراتی، انبار تجهیزات فنی، سامانه هدایت بالن جاسوسی و مخازن سوخت
🔹
نتیجه: انهدام مرکز تعمیراتی، انبارها و سامانه بالن؛ آتش‌گرفتن مخازن سوخت؛ کشته‌شدن تعدادی از نیروها
🔹
پایگاه علی‌السالم در کویت
🔹
نوع حمله: حمله تلفیقی موشکی و پهپادی
🔹
هدف: قرارگاه و محل اسکان فرمانده آمریکایی، آشیانه پهپادی و رمپ استقرار پهپادها
🔹
نتیجه: کشته‌شدن تعدادی از نیروهای آمریکایی؛ انهدام آشیانه و رمپ؛ انهدام تعدادی پهپاد
🔹
پایگاه نیروی دریایی آمریکا در بحرین
🔹
نوع حمله: تلفیقی موشکی-پهپادی
🔹
هدف: تاسیسات، تجهیزات و نیروهای آمریکایی
🔹
نتیجه: هنوز جزئیات کامل به صورت مجزا اطلاع رسانی نشده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/686488" target="_blank">📅 10:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686485">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f57450f310.mp4?token=l-jpTY5G-jT4ll9pLTZg3xygvBevot67kj3ZtGmLA0cH2kjgOD24eJ9RjE88fPvzcpO4s-iBxElU5WBc_4aSJ3_1STxFwGPx6aBxltaeoTC8DL439-lryYirAc_tJho6vea_mpiWIdAL0R0mm0tyvnb3lmVHDoNJkV-yf8lrV37L4ECK-lyCyllCYylbbq8eL_lfbHfR1fvbWrlLTueukWDV2DlqfUTENSA4UwWgU7ldhYNfB5bLw_IAp9pW6cQk9aFZY43oCeZRwj0wY5lQ_4r3PFooapIvERhDJm-V6zgRzli-RBsTbeAWIol2i359sfuLwhe11BKsPUNSYGXLPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f57450f310.mp4?token=l-jpTY5G-jT4ll9pLTZg3xygvBevot67kj3ZtGmLA0cH2kjgOD24eJ9RjE88fPvzcpO4s-iBxElU5WBc_4aSJ3_1STxFwGPx6aBxltaeoTC8DL439-lryYirAc_tJho6vea_mpiWIdAL0R0mm0tyvnb3lmVHDoNJkV-yf8lrV37L4ECK-lyCyllCYylbbq8eL_lfbHfR1fvbWrlLTueukWDV2DlqfUTENSA4UwWgU7ldhYNfB5bLw_IAp9pW6cQk9aFZY43oCeZRwj0wY5lQ_4r3PFooapIvERhDJm-V6zgRzli-RBsTbeAWIol2i359sfuLwhe11BKsPUNSYGXLPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظۀ اولیۀ حملۀ دشمن آمریکایی به محل برگزاری مراسم عروسی در بندر کوهستک سیریک
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/686485" target="_blank">📅 10:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686484">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c68a0f4c8.mp4?token=EDg0w_zbxDKGQB-1K2znJw53UrMHnq6riwZYxesg6QFdSXyeCnHR2GSze8_cGl2Hx3W04iTiYTRS0IqSkj_q_XtAp1tm5lTdkYOL5Rf5VJdyBjMlG6e7pjW-P5K9CO0R4ilUj8ncAku8SRwt4fwDpfxZQZwLs-xchiGGiss8VfoCN2TQN7GvzqYLMSyfW65zZ8Vu7PJQ3jFFRdYSiSiStCwywUiaZ8lda6CjkkBA4PenJdlbt93gZAF2Mt-7nMgmAb3y6GKymb8nfkFI1UFAwUnFWgkOojRxx2g8B3SCF3c4aDDXpph98gyAGJ3YEUwoUN5WFXki1IopNfgO3GptyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c68a0f4c8.mp4?token=EDg0w_zbxDKGQB-1K2znJw53UrMHnq6riwZYxesg6QFdSXyeCnHR2GSze8_cGl2Hx3W04iTiYTRS0IqSkj_q_XtAp1tm5lTdkYOL5Rf5VJdyBjMlG6e7pjW-P5K9CO0R4ilUj8ncAku8SRwt4fwDpfxZQZwLs-xchiGGiss8VfoCN2TQN7GvzqYLMSyfW65zZ8Vu7PJQ3jFFRdYSiSiStCwywUiaZ8lda6CjkkBA4PenJdlbt93gZAF2Mt-7nMgmAb3y6GKymb8nfkFI1UFAwUnFWgkOojRxx2g8B3SCF3c4aDDXpph98gyAGJ3YEUwoUN5WFXki1IopNfgO3GptyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسواک ۵۰۰ دلاری Dyson؛ هوش مصنوعی حالا داخل دهان‌تان را هم می‌بیند
🦷
🔹
این مسواک با دوربین ۱۰۰ هزار پیکسلی و هوش مصنوعی، داخل دهان را بررسی می‌کند، فاصله بین دندان‌ها را تشخیص می‌دهد و دهان‌شویه را دقیقاً همان‌جا می‌پاشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/686484" target="_blank">📅 10:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686483">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
جزئیاتی از حادثۀ خونین بلوار وکیل‌آباد مشهد  رئیس پلیس راهور خراسان‌رضوی:
🔹
این حادثه زمانی رخ داد که یک دستگاه خودروی هیوندا در مسیر غرب به شرق بلوار وکیل‌آباد با سرعت نسبتاً بالا و غیرمطمئن در حال حرکت بود.
🔹
این خودرو با یک دستگاه خودروی چانگان که در مسیر…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/686483" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686482">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlMA_0YoVpPmzR7H1glzuBrM2kGjgalhkE7VqtgEc8Wtv7rspMDYfcxH2MBhJTU5ORVF8X6WUbWjtFYeCp7iQaJq4RSY6lIJJFKRrBX92sY3oLDMKn1_LWWfxJFk_C8VpyMd68Iq0ibKTKj0qGmJIul4fnxoTKZ2wXd8DK5s8-6ZX4lpCxrHpdsu7AqvadIKbda59VJtCFtmpHoQdSlmA9uoFXh7ROLj4Cn2e6DR2iga0BqVI9TMS__9Ds-_0AIjaDMENCSDMJM0arpc8ZQABGLcODTcKDuDZvq42RopLsT4mV97E_Ba-wY_geAUWJLfnjIQjEkAKX547ecvfRxkzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک توسعه صادرات ایران؛ الگوی موفق در بانکداری اسلامی
🔹
بانک توسعه صادرات ایران بر اساس ارزیابی دبیرخانه شورای فقهی بانک مرکزی، در سی‌وششمین همایش بانکداری اسلامی به عنوان بانک پیشرو در اجرای بانکداری اسلامی در سال ۱۴۰۵ معرفی و مورد تقدیر قرار گرفت.
🔹
این تقدیر در پی عملکرد موفق بانک در رعایت موازین شرعی، تقویت سازوکارهای نظارت و تطبیق شرعی و اجرای صحیح عقود اسلامی در عملیات بانکی انجام شد.
🔹
لوح تقدیر با امضای رئیس کل بانک مرکزی و رئیس شورای فقهی این بانک به طور جداگانه به دکتر قاسمی سرپرست بانک توسعه صادرات ایران و رضا عبیدی مسئول نظارت و تطبیق شرعی بانک اهدا شد.
🔹
در این ارزیابی، شاخص‌هایی همچون نظارت بر رعایت مقررات شرعی، بررسی پرونده‌های تسهیلاتی، نظارت بر مصرف تسهیلات در چارچوب عقود اسلامی و آموزش بانکداری اسلامی مورد توجه قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/686482" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686481">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3db35ef4a5.mp4?token=kawZpKvmMMW8-yt2P1JLf0hl-_vSHKaLMwy1P_AELoiXbWeGeBGak6Dpp8JIa5F9km3Ueuru5C4t9dFJTPnd0j079Q4fIPg50taq6dptOqJTpVmuuw_w0oqXKSvdY0T0YPi-k86d9NeXdN5x5ZtDPX7-7xjOa053TLaCNWGpi7au7Lueq_FQUerP5CFT1W2ICrjIdepOwekDh44JWkSQwVjUgNj88poKnPBbIYEeyPnopXp7nmoGZXifM9hq_FDSOFlMNI2IDCskpJTIn2fL1jb0iyVD66mM1wztsJqXAaNtRzdJDOyUZ14og2fCE6es_KOIuQE6z8QnMhi6NBPmJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3db35ef4a5.mp4?token=kawZpKvmMMW8-yt2P1JLf0hl-_vSHKaLMwy1P_AELoiXbWeGeBGak6Dpp8JIa5F9km3Ueuru5C4t9dFJTPnd0j079Q4fIPg50taq6dptOqJTpVmuuw_w0oqXKSvdY0T0YPi-k86d9NeXdN5x5ZtDPX7-7xjOa053TLaCNWGpi7au7Lueq_FQUerP5CFT1W2ICrjIdepOwekDh44JWkSQwVjUgNj88poKnPBbIYEeyPnopXp7nmoGZXifM9hq_FDSOFlMNI2IDCskpJTIn2fL1jb0iyVD66mM1wztsJqXAaNtRzdJDOyUZ14og2fCE6es_KOIuQE6z8QnMhi6NBPmJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای تازه از اصابت موشک ایرانی به پایگاه هوایی آمریکایی الازرق اردن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/686481" target="_blank">📅 09:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686480">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b7195ceb1.mp4?token=t-yOjODlCPbuuPSCGA7owk27CoQn5V6RUHaynwrH-bmTBn8eZkSgG2V_QE2y-ACIISL1TPpDOD0eSCvPcrsOmIDOs2xgUhxWCS6GlbJMN20xMQRm1dGGtYwYrsN1lzuKyJh1SzT2kK3pDyYFXmXi_pMMqTYvHbUbTQdwHl-zY982JU-SPxATm8KaDEKz4h8Dn-RKgX0ynvjVsynQX8JdkK-Z92RIu-g1I28nNJcRTuLc6cyqK0c2FsshPweaAxOuYFGV7kgdpQbWQuEJyEwQx1DGd3EUew-C5DQIRW9l4Ua9chne_mtRoDWeb5ujYSQacLWoJWohxeKWXwYLaXhpkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b7195ceb1.mp4?token=t-yOjODlCPbuuPSCGA7owk27CoQn5V6RUHaynwrH-bmTBn8eZkSgG2V_QE2y-ACIISL1TPpDOD0eSCvPcrsOmIDOs2xgUhxWCS6GlbJMN20xMQRm1dGGtYwYrsN1lzuKyJh1SzT2kK3pDyYFXmXi_pMMqTYvHbUbTQdwHl-zY982JU-SPxATm8KaDEKz4h8Dn-RKgX0ynvjVsynQX8JdkK-Z92RIu-g1I28nNJcRTuLc6cyqK0c2FsshPweaAxOuYFGV7kgdpQbWQuEJyEwQx1DGd3EUew-C5DQIRW9l4Ua9chne_mtRoDWeb5ujYSQacLWoJWohxeKWXwYLaXhpkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سندی از جنایت آمریکا در حمله به مناطق مسکونی
🔹
وسعت حمله ارتش آمریکا به مراسم عروسی در سیریک
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/686480" target="_blank">📅 09:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686475">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lT68Lg-cmYR-tRZVOWVOJtmma4M9VQR5OZ3gDyp7Ko0dNxRglCoqi6JAzWYsyDcuEQVVi-o9UnxnBdBH7KSMwhNPkr8MiIwAML0lo6qVVC3enAG6jeGlbyIjPVLQBaBKk15wKD_kP9VEwEIXV1nbw-OKkkUJBOyuoQhIFwRq7qKjYZP_gS_ubr5ZmKuU-PNdLYPgFPu7DMzpuPm7TuImBBut1t8v-CllmWQkn2ZlXHph2kqXk4fXPQ_Mkonz8ZDnGQ_Pr0xNbTRvrbe4x-kCsE9zYtifE15qkjaEXTsz-ENyUETe3F1CzipKe_8W7BFpNmRghlrxeUTUKejOtNSw3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZdqTLXRrT76vJ5KpMk0jdpC1UI2J7L8vkdwv4u4WzfF4a8G9X-B-IoZTfK7M2h9_ZQK-fLDqjQjdmSfv7nlYmEhzqIyj02ttjs6ZcIMosBMunPaPPwJFLx4lKG9bqLWB8brglnbhQ-bUJw8bbph0wBmnjJ0PJpz7FJH5xugDCQEvNLMeL4CrqfUEEPI8WeRz4tLTVQ2x9LvkvRDE44jSwGKD6J-UJG1lsKuv4hfTykC7dXdudRHDp6HusRz_rwk57LLoRKT3CT6fX2ixVo_mNHUesxyU0nhigq130pwIe8_-x1O0f7TLQSdgoD7XXDAk715tZWJt-rZMQsyuGXXN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dHKyZpz_Z-IOwytitjwT6aGrQNRDEzD8v6sAm-dkKXnYOTB3kxTEy3j0fu9Kk9Cd0MqB8QrIO4QxlLBwQ9KNycff9V60htX6lsRenzkvehAAxBkntu00seEhfhbzGRq4Nk2HYUoCGzt0-ynYJxU1vVXd2vDpg5VXzuxbNbfyaJxVZAl_v9OUUilBsWSollLiWtRLel1099PX6r2DNrt2c-AqiTvpC12dsPZ_fVIDPTDUnaBWLFVovTTR2R8eGGm6Xygl3fLcMlIzrPpSZtqajtW2KtmnwzRURaZnM7EpbHGWv9iFH1FyjDxhTHie6MtSWs2XiZkczzMdTmcFkRI0EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HcOe1_H_qOFpEFQyvOAQnIq_wIqGixvp3tvDrQHX1at35OwNonK6d_xJ2bspZCVa9fIPKIJnWBTyUi_3PgZFcdfBAm01BezknFx7RbIVTz6PyX9dukWbmeoaUUdmEmO8lX7daBn3NVRLAPQPDz3paTuHrphQUtHkBAGj_ZDxI_wjgS7-bKNyM7jX38A7T1HX30bVgp182bAb5X1VCz25xbQZisaV75RSPf4-75shExdCSxX1DUSFWJAVXnGQHerfz-Zcqiu6Bs0TES7Q0t6uMT1W8HMdxGgdF6rXSC1nPT2C-bAc46k6GMbGAPK4U4ahwvmSCU1Vv80004slzd2hnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCI6d6d71TC6RwwJineYRuU8bzpcHz8S4UOCcx-f25hQAcftUXUs3RJvriRQL_ef3hZjeXxk5asesqxRiJHPnlkZe__nzeCy9ysTncInvCVdIPps5sxbNLOSX0BaXfbKIbFD8jef1ze1UlUKXy-B21-2fp40Aq5vrk-OvRaLEQQrqSmY5l7bcVdCT0_nyOiBbA0pkkeVtfNf6sJqoAykEhqkkGmtPVNEr4NbPygT9JegWR2TKw3zG6kzho88CmZyDcVdZXdLjg-Orpz4Sk95vOCNkJXWfmD-zdjizV6ZulaRBWkXq-sYoV9IoAFCll7fIAkhTyn-upM9a8924yWjHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
موشکی که به مراسم عروسی در منطقه کوهستک در جنوب ایران اصابت کرد و منجر به شهادت ۵ غیرنظامی (از جمله یک کودک) و زخمی شدن ۵۰ نفر دیگر شد، یک موشک آمریکایی به نام "SLAM-ER" بود
🔹
شرکت بوئینگ، سازنده این موشک کروز، ادعا می‌کند که این دقیق‌ترین سلاح در کل ناوگان…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/686475" target="_blank">📅 09:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686474">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
وضعیت مجروحان حادثه حمله آمریکا به جشن عروسی در بیمارستان میناب  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/686474" target="_blank">📅 09:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686472">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نایب رئیس کمیسیون اجتماعی مجلس، از واگذاری اختیار تعطیلی پنجشنبه‌ها به دولت خبر داد.
🔹
یک کارشناس رسمی دادگستری اردبیل حین دریافت رشوه دستگیر شد.
🔹
رژیم صهیونیستی در جولان اشغالی رزمایش برگزار می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/686472" target="_blank">📅 09:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686471">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
تکذیب حذف شارژ کالابرگ؛ زمان‌بندی جدید اعلام شد  معاون وزیر تعاون کار و رفاه اجتماعی:
🔹
زمانبندی شارژ کالابرگ از این پس به جای ۱۵، ۲۰ و ۲۵ هر ماه، در تاریخ‌های ۵، ۱۵ و ۲۵ ماه انجام می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/686471" target="_blank">📅 09:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686470">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4075e7990.mp4?token=JT3v7TaO6fM2k8EVWPgnHtETNMjwW02l5FuTAE3GVW7lUXU7b3MRSiyXLmMMQTBz0rXOOYU2kj_tElmnHgLiR0P08GxLwYV_2mutJifby5fDH07fapCkB3jDvUPC5lQzuBFe13T2_rF0Q_5NMe9H055ZGAFbnXKVShLPLRu97Ay_6ZB8SpjbItwaIxUCTzzIevmcxjkxvG0GgJMjXRFF_P38NgXyYoHfBiKi-l8boNlquQw5em_66GT8Cc5MAvkGn8SQudgkYLdOk5VIa4zXkHxGRaky5N_U9exYbs6U00__2SvhUyLh1huDAZP9wqAcaspQ_YJWrJalsVq5D4xuiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4075e7990.mp4?token=JT3v7TaO6fM2k8EVWPgnHtETNMjwW02l5FuTAE3GVW7lUXU7b3MRSiyXLmMMQTBz0rXOOYU2kj_tElmnHgLiR0P08GxLwYV_2mutJifby5fDH07fapCkB3jDvUPC5lQzuBFe13T2_rF0Q_5NMe9H055ZGAFbnXKVShLPLRu97Ay_6ZB8SpjbItwaIxUCTzzIevmcxjkxvG0GgJMjXRFF_P38NgXyYoHfBiKi-l8boNlquQw5em_66GT8Cc5MAvkGn8SQudgkYLdOk5VIa4zXkHxGRaky5N_U9exYbs6U00__2SvhUyLh1huDAZP9wqAcaspQ_YJWrJalsVq5D4xuiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکذیب حذف شارژ کالابرگ؛ زمان‌بندی جدید اعلام شد
معاون وزیر تعاون کار و رفاه اجتماعی:
🔹
زمانبندی شارژ کالابرگ از این پس به جای ۱۵، ۲۰ و ۲۵ هر ماه، در تاریخ‌های ۵، ۱۵ و ۲۵ ماه انجام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/686470" target="_blank">📅 09:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686469">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88e74c3ba.mp4?token=bMM6yDfeKdO6yKGAGxfuDuTtK9zwqhKG1n5hMueFi4_6Ku_6WAqD7jDo7_imK-u_S4W_DVvckST7FrqL43Ph4gVTEB-ZuWWA_zBK0hpm3wjoCLN75aE_Wt__V7QpLyLaOBOWN8NvhuDjachKgNwRMUDd8UOSzwe1IRplHFXcaE83YMsLkpm8n6UGc7Uq7-XT5FX8IGtppVqAjMxDWnxv39XW7OhGZy2JFOGIEbBEz7StBa_bhNRJ6Pj2fwbYTIO6tJmiasoAQS12xbnkUUil1nv2ZCJsn9kjioXpen3j2_4MbiMZicuq0CH6ZcBVrjamWHWQdkytkuRv3vGT_xvwwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88e74c3ba.mp4?token=bMM6yDfeKdO6yKGAGxfuDuTtK9zwqhKG1n5hMueFi4_6Ku_6WAqD7jDo7_imK-u_S4W_DVvckST7FrqL43Ph4gVTEB-ZuWWA_zBK0hpm3wjoCLN75aE_Wt__V7QpLyLaOBOWN8NvhuDjachKgNwRMUDd8UOSzwe1IRplHFXcaE83YMsLkpm8n6UGc7Uq7-XT5FX8IGtppVqAjMxDWnxv39XW7OhGZy2JFOGIEbBEz7StBa_bhNRJ6Pj2fwbYTIO6tJmiasoAQS12xbnkUUil1nv2ZCJsn9kjioXpen3j2_4MbiMZicuq0CH6ZcBVrjamWHWQdkytkuRv3vGT_xvwwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله سی‌ام عملیات صاعقه ارتش/ادامه حملات پهپادی ارتش به پایگاه‌های آمریکا در بحرین و امارات
روابط عمومی ارتش:
🔹
در سی‌امین مرحله از عملیات صاعقه و در پاسخ به هدف قرار دادن مردم بی‌گناه، از بامداد امروز، ده‌ها فروند پهپاد انهدامی ارتش، سامانه‌های راداری و محل‌ استقرار نیروهای آمریکا در پایگاه‌های الظفره و المنهاد امارات را مورد هدف قرار دادند.
🔹
همچنین، تاسیسات راداری و مراکز تجمع نیروهای تروریست آمریکایی در پایگاه شیخ عیسی بحرین، مجددا مورد هدف حملات پر حجم پهپادهای انهدامی آرش قرار گرفت.
🔹
پایگاه الظفره یکی از مراکز مهم عملیاتی آمریکای جنایتکار در منطقه است و از آن برای عملیات هوایی، شناسایی، مراقبت  و پشتیبانی استفاده می‌کند.
🔹
حمله به مناطق مسکونی و هدف قرار دادن مراسم عروسی از سوی دشمن، مصداق بارز جنایت جنگی و  آشکار کننده ماهیّت پلید «حقوق بشر آمریکایی»است و قطعا پاسخ رزمندگان ارتش به این جنایات دامنه دار و گسترده خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/686469" target="_blank">📅 08:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686468">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
بیانیه شماره ۶ سپاه پاسداران: زمان پایان سلطه رژیم منفور و وحشی آمریکا فرا رسیده است   بسم الله قاصم الجبارین  و لکم فی القصاص حیاه یا اولی الالباب  مردم مسلمان و شریف کردستان عراق
🔹
ارتش کودک کش آمریکا که تجاوز خود به ایران را با جنایت و کودک کشی در میناب…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/686468" target="_blank">📅 08:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686467">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH8SZ7CBg1Ii0dA3VXKxQVNNMEi6BHZU8cTfmMXMeV4fCGIePh08PrjwdH4W9nO9PY1O7KcbQutbQGept8XN5I73Ejkk6Vc5IuGIMMy0WBkWO1ojDhttUvkECxMYv_FNDSsQ-MHYk93Mx5TwFNbGZrWtNEi-URC7D-z9_S6BTSpbzGVnr5m7j_iHd0eNueDcVC-xqwliM51sXAPxBKE0jvCpmWkjCxLzpl1XhsdlNrovoFpnfBFwos1zXCqvE4iUGRXpQ_Jx4uLSrTOvZo9F0etQdVuXkbAXHI7w6gc7_nH42p3H7dBcolMI-sxinxCfPNn9pST1yUl6YK-Y90A2Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیش از ۲۰ مقام ارشد نظامی آمریکایی در طول دوره تصدی پیت هگست (وزیر جنگ آمریکا)، استعفا داده‌ یا اخراج شده‌اند
یک مقام آمریکایی:
🔹
"هگست تعداد بیشتری از ژنرال‌های آمریکایی را نسبت به ژنرال‌های ایرانی کنار گذاشته است"
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/686467" target="_blank">📅 08:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686466">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWMLaguUPJPCniO0dFytOy71OzspVImS-1yfjEX3ga1MOnBx3uArRJ1HcXZHoSog1RGFjWT2Loy3G8Hhos0pkE86FQDhjWJdbyPi4cPrfx_f60AKNNdjqhUU20DxIbivERqwRd2yKJQmvk-IIKzXWKn7KBF0Hbz4PiMwNccIf7gXKx-RQdXnpHVg6xCYlIpag929R2n_LLt4ih3iUXjl7d5JFrF7PlVUKuJ3aeIEM_N4hQAqiGkG6TKQwWhNfPowBjdiioyb_xKuJh8LxWnm8hJ0nUN9cDVa3Lf5bINCmK-Rzc6ALEcgx-l_Qi96auJtA3URDa9a8pP-zvugM7AaXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آکسیوس مدعی شد: ترامپ دستور حمله به نفتکش‌های ایرانی را صادر کرده است؛ دو نفتکش هدف قرار گرفتند
یک مقام آمریکایی:
🔹
این اقدام بخشی از سیاست جدید دولت ترامپ با عنوان «نفتکش در برابر نفتکش» است که با هدف افزایش فشار و بازدارندگی در برابر حملات ایران به نفتکش‌های عبوری از تنگه هرمز تصویب شده است
🔹
آمریکا نفتکش‌های ایرانی را به عنوان اقدامی تلافی‌جویانه در برابر حملات ایران به کشتی‌ها در تنگه هرمز هدف قرار می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/686466" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686465">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfP8QkblPMVJ2OmX6Xy-sFi0vya3pSTRNfMnvNKjbFA7-O-R5Ww0uxDMZJuKPB4TUvjOhUqFEx6mPYpI5giDmeOv8sDpJwSBI7OBVKI5G6uO4Ej_EGFjK2FmyLY2QkubohOAnui7p4_rCDTP8CMa7hu5dRGVkcfWDIuEouVBlFZO5bye2CUYuaT8rd08WSPyKjRA5vHiXGteNialyl6T4aUUbba9wMOGVzvXqmJ6v1bHitErrNJiuXRPZcc42LO3_kFx5dglGjEpcgsOy_5lmvNirYfppro-WVXKl-33K-IZKkwFrj_56BGKyk5RhQAYlnUD-x4VXRoGfNhIppJAwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار تصاویر از قطعات موشک‌های اصابت‌کرده به مراسم عروسی در کوهستک سیریک
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/686465" target="_blank">📅 08:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686464">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hi0at9Tt2VuOZENADrn0rsMV0ih2BdZHmWcOGR-IGsjQC-IcIARz5B7XztP83vhQ8GDlAnS875kcqJxz5rojLh7kV35fU3DxIkvt6agWLbBoVYi0tsIt1u4PBm51cs3ZjlMCA20gRmU3TOP8iJr0RV-aIutzhKbSkqs2lo7vXGNXRhBlnQwhUbVMn1ejKc8Cb7MAxvXNqgkbCmKVK0IHZ_Bi0vJRgCAKZ9y-am6efGOJ2SVl5Rqir5cEpJExmeF0MWpiy7gvDOklA50f1fBzry9AGPeA65CCzH8VfzmGNwESbgXvq2KGaRsrifxxX3acKv7vC2j88sNtnW5AK_Vx6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت ساعتی قبل از ۹۶ دلار هم عبور کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/686464" target="_blank">📅 08:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686463">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5534a77c.mp4?token=kHhYUxv1bEGCivze89F2oRq7nTzi1ZdOebmVnYK6nhSW89Xf4n5NTz4O3KmB-OupwvlLh7GX3EIFFWLUoHqvMbl9zJugKIlkroaxZJzEYGNffmg9phJeCzDKbKDt21jNpnp1FryfKhOXJfg0c2hT4l13giEwpValYHDQKdNGztJ_TbKfyqPazYzL4Jm_svod_gVSjGolb4Wx_cutLa-KuY-siO3ExOLSCKKUqleQWak7PjiR0kMSK6iRyd9SPXRxlT7s8eHx-KL2DX7x7kxmqhEluttTqRT9Sr-hAO-yKgHSYZE9xyoR01Wn2w3TvjMhhYtRZikMHi_L19Kh-5TloA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5534a77c.mp4?token=kHhYUxv1bEGCivze89F2oRq7nTzi1ZdOebmVnYK6nhSW89Xf4n5NTz4O3KmB-OupwvlLh7GX3EIFFWLUoHqvMbl9zJugKIlkroaxZJzEYGNffmg9phJeCzDKbKDt21jNpnp1FryfKhOXJfg0c2hT4l13giEwpValYHDQKdNGztJ_TbKfyqPazYzL4Jm_svod_gVSjGolb4Wx_cutLa-KuY-siO3ExOLSCKKUqleQWak7PjiR0kMSK6iRyd9SPXRxlT7s8eHx-KL2DX7x7kxmqhEluttTqRT9Sr-hAO-yKgHSYZE9xyoR01Wn2w3TvjMhhYtRZikMHi_L19Kh-5TloA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از حمله آمریکا به مدرسه میناب و ورزشگاه لامرد نوبت به عروسی در سیریک رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/686463" target="_blank">📅 08:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686462">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
هشدار دادستان تهران به افرادی که به تعهدات ارزی خود عمل نکرده‌اند
دادستان تهران:
🔹
کلیه اشخاصی که دارای تعهدات ارزی هستند در اسرع وقت نسبت به ایفا تعهدات خود اقدام کنند، در غیر این صورت مورد برخورد صریح، قاطع و قانونی دستگاه قضایی قرار خواهند گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/686462" target="_blank">📅 08:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686461">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
تیم‌های پرسپولیس و استقلال در صدوهفتمین شهرآورد از ساعت ۱۹:۳۰ به مصاف هم می‌روند.
🔹
پارلمان ونزوئلا قرارداد نفتی با آمریکا را تصویب کرد.
🔹
صدای انفجار کنترل شده در محدوده شهر میمه اصفهان شنیده می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/686461" target="_blank">📅 08:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686460">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
سوءاستفاده از جایگاه شورای امنیت؛ فرانسه در پی برگزاری نشستی درباره ایران
🔹
سفیر فرانسه در سازمان ملل متحد که کشورش به تازگی ریاست دوره ای شورای امنیت را در ماه جاری میلادی(سپتامبر) برعهده گرفته است، با سوءاستفاده از موقعیت خود، در پی برگزاری نشستی درباره ایران پیش از آغاز نشست سالانه سران مجمع عمومی سازمان ملل است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/686460" target="_blank">📅 08:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686459">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c623c5b1a8.mp4?token=fqqSKjQxdYfShm_boFC-hDPbtZ2aTq2336dG9Tj_ZeSbvb_X8NSvafSxr1x_1Od9PMwdxNPSfnHHbUozGyDycFNuX1uogSNGDuOevnZPFAUOqp778z13E0qmTCd12wNeMRYi7ODbck8p6Nueemp6LwAUMUMMX4w0oYMDn7HN6dmlCYnj3yGKjKxrbzbjv79kcJqg8ALvWbtm07ZlGLHKULKeDCAyni6KOlah84wVb8U80Tdar-iu5LvT3Kb2owYTUjTmuxECXWlttbQ7WccG_dKuwtyePjkTEYB-tsSIoLcaBygsVOB69jVObzu5IujNK1sxWcWG_6Wv4pavVyWemw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c623c5b1a8.mp4?token=fqqSKjQxdYfShm_boFC-hDPbtZ2aTq2336dG9Tj_ZeSbvb_X8NSvafSxr1x_1Od9PMwdxNPSfnHHbUozGyDycFNuX1uogSNGDuOevnZPFAUOqp778z13E0qmTCd12wNeMRYi7ODbck8p6Nueemp6LwAUMUMMX4w0oYMDn7HN6dmlCYnj3yGKjKxrbzbjv79kcJqg8ALvWbtm07ZlGLHKULKeDCAyni6KOlah84wVb8U80Tdar-iu5LvT3Kb2owYTUjTmuxECXWlttbQ7WccG_dKuwtyePjkTEYB-tsSIoLcaBygsVOB69jVObzu5IujNK1sxWcWG_6Wv4pavVyWemw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این تمرینات برای افرادی است که می‌خواهند بدنشان را بدون وزنه قوی کنند! #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/686459" target="_blank">📅 08:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686458">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91f8589ea7.mp4?token=YUyQplbAFd-7vL19QeisqW0o7h-w5bdZLrpd5xw4DCNSVhiZBJLIZxz7FZqQuO7vFWM3f6qzNVstzALiC4Ast4QGhX_HdJCrwuIuNTAbpAgS9pV8rOHdkraAkzvQNCZZ5aV3WbC-cyjD88Csb6lF1aeK3I-8wXY_7SPBfqxurG9HP6NMWAvJnrU_tLfQXhtw_fpAc7WvJL3_SbCDOGXX1tfgONRAAvsoa6-pnGgB-aIBVZgeCxyzmI_HRqxZ5T5l-rfy7jBoFs9vvPjbAB6xedWyuMe5HquXxTbRaznezpCky0MsviBv6o2r8NbjM8iVmbMbkmf8gBhCRe7BdD329zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91f8589ea7.mp4?token=YUyQplbAFd-7vL19QeisqW0o7h-w5bdZLrpd5xw4DCNSVhiZBJLIZxz7FZqQuO7vFWM3f6qzNVstzALiC4Ast4QGhX_HdJCrwuIuNTAbpAgS9pV8rOHdkraAkzvQNCZZ5aV3WbC-cyjD88Csb6lF1aeK3I-8wXY_7SPBfqxurG9HP6NMWAvJnrU_tLfQXhtw_fpAc7WvJL3_SbCDOGXX1tfgONRAAvsoa6-pnGgB-aIBVZgeCxyzmI_HRqxZ5T5l-rfy7jBoFs9vvPjbAB6xedWyuMe5HquXxTbRaznezpCky0MsviBv6o2r8NbjM8iVmbMbkmf8gBhCRe7BdD329zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرماندار شهرستان سیریک: ۵۰ نفر از ۶۳ نفر مجروح جنایت آمریکایی در کوهستک زن و کودک هستند
🔹
همه‌ی مجروحین به بیمارستان شهر میناب منتقل شدند و وضعیت مساعد دارند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/686458" target="_blank">📅 07:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686457">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1217f94e.mp4?token=SuZw22W_TeTCN9Y9h2JtRkcUf5aNKBDFUzFbv_qmD2kOekROhjmqEG2udnGqiKdie_2zQC0h8csejZHB_KO0yG5hjPqZYvCLchi3hJNGshyCqVB-zR64lFvlRSc4ilfgaHNvRPzU6BvYXNatLR1lD4sIlQv8IusGcflp_OtMm3aXrzD4Du0pjTA_2BU_xjsi3ZZNsrYh4xZohI80hwcbr39LYvwgPlqhwVQjdgN9Q70R80pvNbm3tFHuVeLGB89mhdkUZb3YrIcHcMvgQnYsfFiJPvLqzCrtBYZCrZDY93S58qdTdd0nC1tEp_BKKNhk9x5AIxE5sq_dymfSgjXAGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1217f94e.mp4?token=SuZw22W_TeTCN9Y9h2JtRkcUf5aNKBDFUzFbv_qmD2kOekROhjmqEG2udnGqiKdie_2zQC0h8csejZHB_KO0yG5hjPqZYvCLchi3hJNGshyCqVB-zR64lFvlRSc4ilfgaHNvRPzU6BvYXNatLR1lD4sIlQv8IusGcflp_OtMm3aXrzD4Du0pjTA_2BU_xjsi3ZZNsrYh4xZohI80hwcbr39LYvwgPlqhwVQjdgN9Q70R80pvNbm3tFHuVeLGB89mhdkUZb3YrIcHcMvgQnYsfFiJPvLqzCrtBYZCrZDY93S58qdTdd0nC1tEp_BKKNhk9x5AIxE5sq_dymfSgjXAGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار سخنگوی قرارگاه مرکزی خاتم‌الانبیا(ص) به کشورهای منطقه: با ارتش آمریکا همکاری کنید باید منتظر عواقب خطرناکش باشید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/686457" target="_blank">📅 07:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686456">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPKhANOlHe9mZMvc4HN_rsJCmnGyiag98yCmfi-5Z7qCbp00vfftdTp1wCazd9sKc8aFWkGEIC5qvLJVcCKllqLPbd7Gfqd5CovER3wK8ffYoTAJblYnoSR6dDtXZMdulawsc2XNQUnupCk4YXZJa2F4jNpjQMl7M2GfCDcZ4nwgtStAo4uJFNPu-_9i53p6iYpQlpGOrywWhZqouEJRRxz-lqAanIBN2o7VCte3akIoZI43bDuFYGYiuWiAfvRSXjPNbVRSxSBLxKUAvbP9tx1EBxkHTr3Kpg93xnHl749SmrFRxFQx3lJxcUvb86ezWt5EiJ7UXOo7EssOJWfXvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۱۱ شهریور ماه
۲۰ ربیع‌الأول ۱۴۴۸
۲ سپتامبر ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/686456" target="_blank">📅 07:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686455">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کشور «پِرو» در اقدامی همسو با آمریکا، روابط دیپلماتیکش با ایران را قطع کرد.
🔹
تانکر ترکرز: صادرات نفت عراق و کویت نسبت به قبل از جنگ ۳۶ درصد، قطر ۴۸ درصد و عربستان ۴۸ درصد کاهش یافته است.
🔹
بامداد امروز رئیس جمهور در پایان سفر دو روزه به قرقیزستان وارد تهران شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/686455" target="_blank">📅 07:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686454">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
الجزیره: رویارویی آمریکا و ایران احتمالاً به جنگ گسترده تبدیل نمی‌شود؛ پاسخ تهران ممکن است حساب‌شده اما همه‌جانبه باشد
نورالدین الدغیر، خبرنگار الجزیره:
🔹
این رویارویی احتمالاً به یک جنگ باز و گسترده تبدیل نخواهد شد و میانجی‌ها همچنان برای مهار تشدید درگیری تلاش خواهند کرد.
🔹
آمریکا با اقدامات اخیر خود به‌دنبال پایان دادن به بن‌بست دیپلماتیک و پیشگیری از واکنش احتمالی ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/686454" target="_blank">📅 07:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686453">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeU-bSppw5orz8TFT_hAr13vsMT5nV3HfNsVNINFTS-PE5-Q8oqMJ7_RTGTmSkuKvoHNcDeGHOjSeQ3b3gv8O2bk9XjpSi9g_CE46snwe9LqiWWyeBWaTI1KRooShbjf7lGw3fwBsyC6EPuDVQzX2wJCOfU3gp_Gaes8HfiYCggc1B2l1BregipQZ3JqwDaBt5G3qCrjG7c4EEQ7c81uXR1PMunkHZGORHuEZeOk0ayeOI6qhIZCTdU0MlcFgzudrOkvidOKvzmXhyC010uHet3eoMw74MPhAChlRriQJ6wEOItqefEItc7IpVPW43KfQq1VTKjce8IW7HsKA5kSUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزافه‌گویی‏ ‏ترامپ قمارباز: به هیچ وجه اهمیتی نمی‌دهم که آیا ایرانی‌ها توافقی را که از نظرشان بی‌ارزش است، امضا خواهند کرد یا خیر
🔹
‏من تلاشی برای اجبار ایران جهت حضور در میز مذاکره انجام نمی‌دهم.
🔹
ایالات متحده کنترل تقریباً کاملی بر تنگه هرمز دارد و این…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/686453" target="_blank">📅 07:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686452">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
بالگردهای تخلیه بر فراز اردن
🔹
این فیلم پس از تأیید بصری اصابت یک موشک بالستیک ایرانی به منطقه‌ای در نزدیکی کمپ تیتین، یک اردوگاه دورافتاده تفنگداران دریایی ایالات متحده واقع در خارج از عقبه، اردن، منتشر شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/686452" target="_blank">📅 07:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686451">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
حملهٔ موشکی آمریکا به اطراف شهر اهواز  معاون امنیتی استانداری خوزستان:
🔹
نقطه‌ای در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حمله موشکی قرار گرفت.
🔹
اخبار تکمیلی متعاقبا اعلام می‌شود.  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/686451" target="_blank">📅 07:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686450">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
تکمیلی/ گزارش‌ها از حمله پهپادی حزب‌الله
🔹
رسانه‌های صهیونیستی می‌گویند که جنبش مقاومت «حزب‌الله» با استفاده از پهپادهای انتحاری به شهرک‌های شمال فلسطین اشغالی حمله کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/686450" target="_blank">📅 05:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686448">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n26JbItzkPK_lLans_-ZHqdLtLwGrHXIhpiceyfxQhXeoXMdhaVnsEKp_lD_by6ve7mo4BCpdsvTuzRlyKz4M1sTohP97ueKpadNYU910-TAQxt00780pz7z7nN_lHtSLU3MN6gb3kCB-SMIn0QxJQsNlmoa4BtrBHfYtaEp6u_0CIXJkpMVGMIgmQf-uF6YuyghL2HkzFF2VRisfQEfgEETkPq6jZ10uNrN3XcHV5_WrsFz_taYEQ38cwzWQQ9Ygc2EwnPNWo1xEVO7dwbJP9LMkLc7CvZGBSaXYXWW0GaWm4no_IH2Szmg2rv5doui4ZSKiBoan1mysnMylfkQcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vP3iBXoDubig9xyUd2egoj62vdxCdqPFr0HM2-Pt9AqFFO76fh7UvsfdJFkPV3GyPnHqyhX7WTCn21BA_0sKWkurad-6pPZYSW8ul6Mc19dPHHY6cog0jk1LjHWF5gDbR_Ns0-KMt8leu1ycRLYXcrhf_Ft2BVpszpRJGESfo8EUKT3u_k9Oz8yTiA5PAcBpLWOAh07Sv7dTDCl1htwIZzNaIzV28EDqip_qF9uC1LUEyev8T1AKQQ0KH7KKXTS9rI3a8UvLt5RXZCdqxRb9az8A5VT7paI8LBBUI9BX6oTKmB2qrqcFOVmDWXIo7SS7JM4Y_u4abUkY_pd-T7urSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آژیر هشدار حمله هوایی در شمال فلسطین اشغالی
🔹
رسانه‌های صهیونیستی گزارش دادند که به دلیل شلیک موشک و پرتاب پهپاد از جنوب لبنان، آژیرهای خطر در شهرک‌های شمال فلسطین اشغالی فعال شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/686448" target="_blank">📅 05:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686447">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
گزافه‌گویی‏ ‏ترامپ قمارباز: به هیچ وجه اهمیتی نمی‌دهم که آیا ایرانی‌ها توافقی را که از نظرشان بی‌ارزش است، امضا خواهند کرد یا خیر
🔹
‏من تلاشی برای اجبار ایران جهت حضور در میز مذاکره انجام نمی‌دهم.
🔹
ایالات متحده کنترل تقریباً کاملی بر تنگه هرمز دارد و این در حالی است که اقتصاد ایران به طور کامل در حال فروپاشی است.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/686447" target="_blank">📅 04:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686446">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
رسانه‌های عربی: صدای انفجارهای شدید در سلیمانیه عراق شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/686446" target="_blank">📅 04:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686445">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
رسانه‌های عربی گزارش کردند که انفجارهای جدید کویت را لرزاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/686445" target="_blank">📅 03:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686444">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
سپاه: تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
🔹
پادگان تفنگداران آمریکایی در اردن هدف موشک های بالستیک قرار گرفت و تعداد زیادی از نیروهای آمریکایی به درک واصل شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/686444" target="_blank">📅 03:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686443">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
بیانیه شماره ۶ سپاه پاسداران: زمان پایان سلطه رژیم منفور و وحشی آمریکا فرا رسیده است
بسم الله قاصم الجبارین
و لکم فی القصاص حیاه یا اولی الالباب
مردم مسلمان و شریف کردستان عراق
🔹
ارتش کودک کش آمریکا که تجاوز خود به ایران را با جنایت و کودک کشی در میناب و لامرد و کشتار نزدیک به دویست کودک در این دو نقطه آغاز کرده بود شب گذشته با حمله وحشیانه به مراسم جشن عقد یک زوج پاک و جوان اهل تسنن در شهرستان سیریک با به خاک و خون کشیدن حدود ۷۰ نفر از مردم بی گناه پرونده نکبت بار خود را سیاه تر کرد در پی این جنایت تا کنون ۴ نفر از میهمانان این مراسم از جمله یک کودک به شهادت رسیده اند.
🔹
در انتقام این خون‌های پاک رزمندگان شجاع نیروی زمینی سپاه با حمله تلفیقی موشکی و پهپادی به پایگاههای آمریکایی در اربیل یک مرکز تعمیراتی و انبارهای تجهیزات فنی ارتش تروریست آمریکا را نابود کرده و سامانه هدایت بالون جاسوسی آمریکا در پایگاه را منهدم کردند. رزمندگان غیور نیروی زمینی همچنین مخازن سوخت این پایگاه را به آتش کشیده و تعدادی از متجاوزان را به هلاکت رساندند.
🔹
زمان پایان سلطه رژیم منفور و وحشی آمریکا فرا رسیده است سرزمین فرزندان فاتحان بیت المقدس جای استقرار و آتش افروزی کافران نیست.
🔹
اجازه ندهید سرزمین شما مبدا انجام چنین جنایات هولناکی باشد. این سرزمین پاک باید از لوث وجود نحس اشرار آمریکایی پاکسازی شود با این جنایتهای آشکار حجت بر همگان تمام است.
و ما النصر الا من عندالله العزیز الحکیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/686443" target="_blank">📅 03:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686442">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c675364dd8.mp4?token=p5vee3lh07Jq_mdNbs9T64VIgzA_SOK2b3IZc-LigPv427pAoDGJNBrMyZvbBllMS85dSgZKfbb12hPTS4VgufQJCoDaNlrBBhFpzSUfbqvoRGudAppwLLTpitcIZau7a40xGDuGSjoOFP2-J8ymXsEQieq9z85oi_BGMzclU2_DM3fAwQ4fbPwddGyF2sx4nkJEUiA0ve5LoPPWtJXHvWiQQL-vQQdkk4LQ54h1gyGI1mdNX0kY6VoL6Cy8-u_d2gTqsYRHfgYXtiR16RNes55dPwQJaSmB_gn3qVI3-FaPFmVQ_R1YvxfvlKr45Ji-k01LvgNHLokaZhnjVujCAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c675364dd8.mp4?token=p5vee3lh07Jq_mdNbs9T64VIgzA_SOK2b3IZc-LigPv427pAoDGJNBrMyZvbBllMS85dSgZKfbb12hPTS4VgufQJCoDaNlrBBhFpzSUfbqvoRGudAppwLLTpitcIZau7a40xGDuGSjoOFP2-J8ymXsEQieq9z85oi_BGMzclU2_DM3fAwQ4fbPwddGyF2sx4nkJEUiA0ve5LoPPWtJXHvWiQQL-vQQdkk4LQ54h1gyGI1mdNX0kY6VoL6Cy8-u_d2gTqsYRHfgYXtiR16RNes55dPwQJaSmB_gn3qVI3-FaPFmVQ_R1YvxfvlKr45Ji-k01LvgNHLokaZhnjVujCAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرماندار شهرستان سیریک: ۵۰ نفر از ۶۳ نفر مجروح جنایت آمریکایی در کوهستک زن و کودک هستند
🔹
همه‌ی مجروحین به بیمارستان شهر میناب منتقل شدند و وضعیت مساعد دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/686442" target="_blank">📅 03:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686441">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
انفجارهای پی در پی در بحرین
🔹
منابع عربی از حداقل ۴ انفجار در پی حملات ایران در بحرین خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/686441" target="_blank">📅 03:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686439">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
انفجارهای مهیب بحرین را لرزاند
🔹
منابع محلی بامداد چهارشنبه گزارش دادند که پایگاه‌ها و منافع آمریکا در بحرین هدف حملات موشکی و پهپادی گسترده ایران قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/686439" target="_blank">📅 02:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686438">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c94f0226.mp4?token=kFyqtiCBT2mvX8HMALopg6smj_fv8Cv9Txk-qEcs3eJTyiKG7kLXFr5svqVV5gsvF_7IX-2M4qmq_cNF-4CssvJzIWFWgWe8yrqELvkCvNLgPpmNdBl9nIWWjMaDtJAveuFB3SLcVac32S5nlfDyIfw4FY8xZGEZfxX4ojReXBL4ue_yFh7brE9hhD3AFbdD7HmT-6cPwzrSnpkYrgAlixHKoSYPPNaau1IQRua0Sx4qa_vuZnymeWYkUKSeAxMzSDsVyGYYODA6Yhsw8kb7TiIWql3DrRBL1DeUTXJ25qrjISPUVOBp1_SnNeRuxSHdjRfUcPoECwtugCAW1wv61w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c94f0226.mp4?token=kFyqtiCBT2mvX8HMALopg6smj_fv8Cv9Txk-qEcs3eJTyiKG7kLXFr5svqVV5gsvF_7IX-2M4qmq_cNF-4CssvJzIWFWgWe8yrqELvkCvNLgPpmNdBl9nIWWjMaDtJAveuFB3SLcVac32S5nlfDyIfw4FY8xZGEZfxX4ojReXBL4ue_yFh7brE9hhD3AFbdD7HmT-6cPwzrSnpkYrgAlixHKoSYPPNaau1IQRua0Sx4qa_vuZnymeWYkUKSeAxMzSDsVyGYYODA6Yhsw8kb7TiIWql3DrRBL1DeUTXJ25qrjISPUVOBp1_SnNeRuxSHdjRfUcPoECwtugCAW1wv61w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار تصاویر از قطعات موشک‌های اصابت‌کرده به مراسم عروسی در کوهستک سیریک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/686438" target="_blank">📅 02:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686436">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eClxYWejiSERhk7TaUeEaH3dvXa6CA4xVIJO-gqroXeD2UFG6vvWhJCIYi3O9UFr9JyZpEHVbExBRCykSilYgYCFlZK81cGtJj3Up9F63ogTcsdLyng6Wt9yfVEDBSUUuIkyCSp632NYQzu9heF-Dyp0rWcCXZk6qkvQ9gQkK8cNKXj3KRPoVz0txz0Z33yAQ9hkP3mGom5HFwQQ0UN4e4iiKbc8EEttzLZzijyFvMCP3UEEp2hvcbIB1j3ym8BZNv63bDC0JaKOXjbOYfNgxDP4qDY7_ffR1Pvo2e9TlzjzTHc5MVrV0QCzrMkW1TMtF65idvXmzHHzmGdGpr7jCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4220f97c5.mp4?token=AJx2j-DLMfHj50uit_Gex0kqSfxTlgsnhtcaoi6_wkqaHBqV5WrEndRdMpwfVGOy82Zjvf-aJU_6k-IecEVaJy-VQ_UlaYWhgF8NETW-ABABlFQo-QpRxVk_iNKAOtszsuhCmSZ8GP3i-Bb00TH07UH_2akvSC7YN0Wr0bKBfQgU1n3PfcZZTPDXWuBDJ4ow5zBTR_QGicJxDa03eoT4JRVagwXEpD4YA2SRTH4br-tKutw-mWdZu4z7vj3kayCWz0q44mW-wFhEzR9FqjwhJyt1Lbxg0AMgwJfabx4LHCrWsTmiyAR6Pmd63hdC7JDcYtREFjlgDc5eO59zQ447nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4220f97c5.mp4?token=AJx2j-DLMfHj50uit_Gex0kqSfxTlgsnhtcaoi6_wkqaHBqV5WrEndRdMpwfVGOy82Zjvf-aJU_6k-IecEVaJy-VQ_UlaYWhgF8NETW-ABABlFQo-QpRxVk_iNKAOtszsuhCmSZ8GP3i-Bb00TH07UH_2akvSC7YN0Wr0bKBfQgU1n3PfcZZTPDXWuBDJ4ow5zBTR_QGicJxDa03eoT4JRVagwXEpD4YA2SRTH4br-tKutw-mWdZu4z7vj3kayCWz0q44mW-wFhEzR9FqjwhJyt1Lbxg0AMgwJfabx4LHCrWsTmiyAR6Pmd63hdC7JDcYtREFjlgDc5eO59zQ447nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع انفجار در کنسولگری آمریکا در أربیل
🔹
رسانه عراقی با اشاره به حمله پهپادی به اهداف آمریکایی در اربیل، گزارش داد که انفجار بزرگی کنسولگری آمریکا در اربیل را لرزاند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/686436" target="_blank">📅 02:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686435">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی و سیاست خارجی مجلس: ایران محیط دفاعی و امنیتی خود را تعریف می‌کند؛ هر نقطه مبدأ تهدید باشد، مورد برخورد قرار می‌گیرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/686435" target="_blank">📅 02:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686434">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3618e31c3.mp4?token=qfYVE9CrtT6QaO-uEWbJW-4WwMDPTRFVw9hYynYouGLxMSjXhQUoqqfLAH-89xTQ_3g3kiaJ66YYfUrDWdZA1nuXtllHC70Af8gtMqM39H9hjCGfNL0ic0fJFcCmySXAcWiLrIOGnqW8no1c4F-9-wExBGXMclLNelkfffdz9ypPdb_HR4tlWn3gXF-aCpej-XHcRkI-iB2CH1OIraO-8C24zwRBoFpAHCK8rRAkrLwqKPXxBBlJipM89eQ_jdzMcmewCs9ollYjW0PfxMGhLQP2Ad-C_r_J6PxdRTsiyzEDKzjjf7fVcRYoelWnPpl2ys_6uzTdxOX3VfGS3iq5pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3618e31c3.mp4?token=qfYVE9CrtT6QaO-uEWbJW-4WwMDPTRFVw9hYynYouGLxMSjXhQUoqqfLAH-89xTQ_3g3kiaJ66YYfUrDWdZA1nuXtllHC70Af8gtMqM39H9hjCGfNL0ic0fJFcCmySXAcWiLrIOGnqW8no1c4F-9-wExBGXMclLNelkfffdz9ypPdb_HR4tlWn3gXF-aCpej-XHcRkI-iB2CH1OIraO-8C24zwRBoFpAHCK8rRAkrLwqKPXxBBlJipM89eQ_jdzMcmewCs9ollYjW0PfxMGhLQP2Ad-C_r_J6PxdRTsiyzEDKzjjf7fVcRYoelWnPpl2ys_6uzTdxOX3VfGS3iq5pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: پهپادهای دشمن با اینکه از چهار روش مخفی کاری استفاده می‌کنند اما همچنان توسط سامانه یکپارچه پدافندی شکار می‌شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/686434" target="_blank">📅 02:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686433">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
فعال شدن پدافند هوایی کویت
🔹
رسانه‌های خبری از فعال شدن پدافند هوایی کویت خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/686433" target="_blank">📅 02:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686432">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf136ebcb.mp4?token=oKHmSqHef1Qy79x3bwmnghcletBkkroR23D8_QI_q5z1LepQcf2OMya0D3GZeNhXxif7xzsAlYkJyL_Ei0FnP8LRntsW1gg0lSudUxYXK2q-fq_zvtqqvxoaWwEh6zoxeUWzZ-GenxDlkY2FRokVI_b6cN8d9l29lhXKpgZuuMS70XUwnugA-gPCzyr3LKRv_UzpThA6GnE2yS3EiJBVVfytTzXa_X4QABBkchh8e8Z-D2o4kwGxzY2T-bCqQ1syTKTbvgC0Bsf3u_rN96aD0WPfR0kRgwvJJtU5TnhnJ4eqTlX32uYsjUAmlZfaIFIB4qCelAZdjIukSQ_jh9cxVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf136ebcb.mp4?token=oKHmSqHef1Qy79x3bwmnghcletBkkroR23D8_QI_q5z1LepQcf2OMya0D3GZeNhXxif7xzsAlYkJyL_Ei0FnP8LRntsW1gg0lSudUxYXK2q-fq_zvtqqvxoaWwEh6zoxeUWzZ-GenxDlkY2FRokVI_b6cN8d9l29lhXKpgZuuMS70XUwnugA-gPCzyr3LKRv_UzpThA6GnE2yS3EiJBVVfytTzXa_X4QABBkchh8e8Z-D2o4kwGxzY2T-bCqQ1syTKTbvgC0Bsf3u_rN96aD0WPfR0kRgwvJJtU5TnhnJ4eqTlX32uYsjUAmlZfaIFIB4qCelAZdjIukSQ_jh9cxVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز پهپادهای انتحاری بر فراز اربیل
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/686432" target="_blank">📅 02:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686431">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
انفجارهای مهیب بحرین را لرزاند
🔹
منابع محلی بامداد چهارشنبه گزارش دادند که پایگاه‌ها و منافع آمریکا در بحرین هدف حملات موشکی و پهپادی گسترده ایران قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/686431" target="_blank">📅 02:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686430">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
بحرین اطلاعیه هشدار صادر کرد
🔹
همزمان با به صدا درآمدن آژیرهای هشدار در منانه، وزارت کشور بحرین نیز با صدور هشداری در تلفن‌های همراه، از مردم این کشور خواست به مکان‌های امن بروند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/686430" target="_blank">📅 02:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686429">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a36224e669.mp4?token=Zh83phRBxx8Pih7nF90x6fPdryd0cQJk4HzXBEJREKmR7fZbVnwrHMMdxDxYQqilFxTDggFeBcX6eUZ8TyVxk0KPmvyIBdyU4TmlOC4qscl5pKy4DGuFRrRmazzjXfH5bfhbPGpPMUwosRZQAqdny5f3tlrK4GoCWa0bZzuHBlHFOizrc1hQygDQ9IFCKn9doi9rYMiXfD7ySvrGZ3x84YC1ELUSbkXue8ZVb85AgoEbj_K4tyDFRKrEN7TRd_XWwhCpBoG5ovbNNqTwdFRM9AMfY1XHHi-8cShxOdD1DTMadjU8x0FobXpNy-rIvi_xZfuHZqOU6zGJ0vi1_9MI2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a36224e669.mp4?token=Zh83phRBxx8Pih7nF90x6fPdryd0cQJk4HzXBEJREKmR7fZbVnwrHMMdxDxYQqilFxTDggFeBcX6eUZ8TyVxk0KPmvyIBdyU4TmlOC4qscl5pKy4DGuFRrRmazzjXfH5bfhbPGpPMUwosRZQAqdny5f3tlrK4GoCWa0bZzuHBlHFOizrc1hQygDQ9IFCKn9doi9rYMiXfD7ySvrGZ3x84YC1ELUSbkXue8ZVb85AgoEbj_K4tyDFRKrEN7TRd_XWwhCpBoG5ovbNNqTwdFRM9AMfY1XHHi-8cShxOdD1DTMadjU8x0FobXpNy-rIvi_xZfuHZqOU6zGJ0vi1_9MI2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عضو هیئت رییسه مجلس: دیگر زمان مقابله چشم در مقابل چشم نیست، از این پس به در مقابل چشم، به سر حمله خواهیم کرد/ گزارش داده شده است که از امارات به ایران حمله شده است و اگر گزارش تایید شود، می‌دانند چه اقدامی انجام خواهیم داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/686429" target="_blank">📅 02:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686427">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
اطلاعیه شماره ۵/ حمله سنگین موشک‌های بالستیک به آشیانه‌ هواپیماهای بدون سرنشین دور پرواز آر کیو ۴ و ام کیو ۹ در پایگاه پرنس حسن/ تعدادی از پهپادها منهدم و تعدادی از خلبانان و خدمه فنی پروازی به هلاکت رسیدند
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
وَلَكُمْ فِي الْقِصَاصِ حَيَاةٌ يَا أُولِي الْأَلْبَابِ
🔹
مردم شریف و انقلابی اردن؛
یکبار دیگر دست شیطان از آستین ارتش کودک‌کش آمریکا به درآمد و با بمباران وحشیانه به مراسم جشن عقد یک زوج جوان اهل تسنن در منطقه سیریک هرمزگان، عمق کینه خود را به امت اسلام به نمایش گذاشت.
🔹
ارتش تروریستی شکست خورده آمریکا که از رویارویی مستقیم با رزمندگان اسلام عاجز است، با استیصال مردم مظلوم را به خاک و خون کشید و مراسم جشن عقد پاک مردم را به عزا تبدیل کرد.
🔹
ارتش جنایتکار آمریکا که در آغاز تجاوز خود به ایران اسلامی ۱۶۸ کودک دانش آموز را در مدرسه میناب و ۲۱ کودک ورزشکار را در ورزشگاه لامرد به شهادت رسانده بود، شب گذشته در این حمله ناجوانمردانه حدود ۷۰ نفر از مهمانان این مراسم را مورد اصابت قرار داد که ۴ نفر از آنان از جمله یک کودک خردسال به شهادت رسیده و حال تعدادی از مجروحان وخیم هست.
🔹
در قصاص این جنایت، رزمندگان نیروی هوافضای سپاه پاسداران انقلاب اسلامی در یک حمله سنگین با موشک‌های بالستیک، آشیانه‌های هواپیماهای بدون سرنشین دور پرواز آر کیو ۴ و ام کیو ۹ را در پایگاه هوایی آمریکا در اردن موسوم به پرنس حسن مورد حمله قراردادند که تعدادی از پهپادها منهدم و تعدادی از خلبانان و خدمه فنی پروازی به هلاکت رسیدند.
🔹
همچنین چندین زیر ساخت فنی آنها به آتش کشیده شد.
🔹
مردم شریف و پاکدل اردن،
اردن قدمگاه مقدس انبیاء الهی است، نباید جایگاه ولیدهای شیطان بماند. امروز با این جنایت های سبعانه، حجت بر همگان تمام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/686427" target="_blank">📅 02:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686426">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
حمله موشکی و پهپادی به کویت
🔹
ارتش کویت در بیانیه ای اعلام کرد که این کشور مورد حمله موشکی و پهپادی قرار گرفته است.
🔹
در این بیانیه آمده است که پدافند هوایی این کشور در حال مقابله با این حملات است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/686426" target="_blank">📅 02:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686425">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
معاون سیاسی سپاه خطاب به کشورهای منطقه: یا آمریکا را بیرون کنید یا پاسخ کوبنده بگیرید
سردار جوانی خطاب به کشورهای عربی:
🔹
بهتر است آمریکایی‌ها را از کشورهای خود بیرون کنید و پایگاه‌ها را پس بگیرید. در غیر اینصورت، نیروهای مسلح ایران ثابت کرده‌اند از هر نقطه‌ای در کویت، بحرین، اردن یا هر کشوری که به ایران تهاجم شود، با پاسخ‌های قاطع و کوبنده مواجه خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/686425" target="_blank">📅 02:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686424">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ارتش تروریستی آمریکا مدعی پایان حملاتش علیه ایران شد
🔹
ستاد فرماندهی مرکزی آمریکا ادعا کرد: ما با موفقیت موجی از حملات علیه اهداف نظامی ایران را به پایان رساندیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/686424" target="_blank">📅 02:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686423">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ارتش: در بیست و نهمین مرحله از عملیات صاعقه، تاسیسات راداری و مراکز تجمع نیروهای تروریست آمریکایی در پایگاه شیخ عیسی بحرین را هدف حملات پرحجم پهپادهای انهدامی قرار دادیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/686423" target="_blank">📅 01:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686422">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
وقوع انفجار در کنسولگری آمریکا در أربیل
🔹
رسانه عراقی با اشاره به حمله پهپادی به اهداف آمریکایی در اربیل، گزارش داد که انفجار بزرگی کنسولگری آمریکا در اربیل را لرزاند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/686422" target="_blank">📅 01:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686421">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
رسانه‌های عربی از اصابت موشک به پایگاه هوایی علی السالم در کویت خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/686421" target="_blank">📅 01:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686419">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6ae37b97.mp4?token=OXaaoiSSyUr0KKGkOBJRQENN-zJVRbuAEE90oA2qd3i9hbJMRkhEWZdTmwobZ_iphVLYQ-i6lNFvhaxIjbUWvjuXXgXny9A33VPpF6MMbDmjZX_dhiAtJkt6HahQq3U9sM_MZorixriJdWi2JQyHrVyFog0ro54xP-mJiqAgwvLP1r70qzFss3qu83Z94HMuQNLCGaDg1eLLTy2jWIP_2MXMiBQj5cz9bZFQoOOpx8opNZBxM_TUer6WY1a5WQtQc2KntnLjz_CDZvhVmnZhjjIDjyAcE1uZ98M0a4c49_e4vg_PkKWIADVTr3qPI1fe8oFw0Yqgr9JHPn5l8WI__A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6ae37b97.mp4?token=OXaaoiSSyUr0KKGkOBJRQENN-zJVRbuAEE90oA2qd3i9hbJMRkhEWZdTmwobZ_iphVLYQ-i6lNFvhaxIjbUWvjuXXgXny9A33VPpF6MMbDmjZX_dhiAtJkt6HahQq3U9sM_MZorixriJdWi2JQyHrVyFog0ro54xP-mJiqAgwvLP1r70qzFss3qu83Z94HMuQNLCGaDg1eLLTy2jWIP_2MXMiBQj5cz9bZFQoOOpx8opNZBxM_TUer6WY1a5WQtQc2KntnLjz_CDZvhVmnZhjjIDjyAcE1uZ98M0a4c49_e4vg_PkKWIADVTr3qPI1fe8oFw0Yqgr9JHPn5l8WI__A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحشت در سراسر کشور‌ کویت از ترس موشک ها و پهپادها، قطع پخش زنده شبکه های تلویزیون کویت و اعلان آژیر قرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/686419" target="_blank">📅 01:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686418">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
صدای انفجار در بحرین و اربیل
🔹
منابع عربی از چند انفجار در بحرین در پی حملات ایران خبر دادند.
🔹
همزمان پدافند هوایی در اربیل عراق نیز فعال شده و چندین انفجار گزارش شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/686418" target="_blank">📅 01:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686417">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
انفجارهای شدید در کویت
🔹
ارتش کویت اعلام کرد که پدافند هوایی این کشور در برابر حملات پهپادی ایران قعال شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/686417" target="_blank">📅 01:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686416">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
‏ارتش کویت: پدافند هوایی ما در حال حاضر در حال مقابله با حملات پهپادی در پی تهاجم ایران است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/686416" target="_blank">📅 01:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686415">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
صدای انفجار در بحرین و اربیل
🔹
منابع عربی از چند انفجار در بحرین در پی حملات ایران خبر دادند.
🔹
همزمان پدافند هوایی در اربیل عراق نیز فعال شده و چندین انفجار گزارش شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/686415" target="_blank">📅 01:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686414">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
پیام سخنگوی وزارت امور خارجه درباره جنایت جنگی آمریکا در حمله به جشن عروسی مردم در بندر کوهستک شهر سیریک: هر روز بر سیاهه جنایات آمریکا علیه مردم ایران افزوده می‌شود
اسماعیل بقائی در پیامی در شبکه ایکس:
🔹
فهرست جنایات آمریکا علیه ملت ایران اکنون کامل‌تر از همیشه شد: امشب یک منزل مسکونی در کوهستکِ سیریک، در حالی هدف حمله قرار گرفت که مردم در آن مشغول برگزاری جشن عروسی بودند. بیش از ۵۰ زن، مرد و کودک بی‌گناه شهید و مجروح شدند.
🔹
این قساوت را نمی‌توان از زنجیره حملاتی که پیش از آن در میناب، لامرد، قشم و دیگر نقاط رخ داده است، جدا کرد؛ همان‌طور که نمی‌توان آن را از حمله به اهداف نظامی جدا دانست؛ حملاتی که با برچسب‌ها و توجیهات فریبنده پوشانده شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/686414" target="_blank">📅 01:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686413">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
منابع عربی از شنیده شدن صدای انفجار در کویت خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/686413" target="_blank">📅 01:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686412">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff4f370421.mp4?token=ejXaCHIeHh7vsCMdFLVYkPr9vcgAuyYv134rbv8MrH0MkoBZOt6LLyNi5QBhKhhDaFVwzgfqFh4sON-HtixHitVa9dPC9nnPpo5kLMGtD6Kh-kBtC-dYbQGUNKYBEQBv0uAxWcPap0b4ooVInyX3TLckUbq65bDapWJf94rwGe1vjTfFOMaCqBGJ-S963w5FUS7-cOPCSqaoZsKcCPZGp2XEG2DIlU6p9G3O5zhVX-Z_EzUdaHPxrrx2-KEdTbc10Kijz5-V-js9u8FsUQ9bqcc12i7lxU_CJ8tftO-MQm4npIuTZc-R3DL7-L_BUWqP-fPsrS7uXvLZdlBvmyZEAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff4f370421.mp4?token=ejXaCHIeHh7vsCMdFLVYkPr9vcgAuyYv134rbv8MrH0MkoBZOt6LLyNi5QBhKhhDaFVwzgfqFh4sON-HtixHitVa9dPC9nnPpo5kLMGtD6Kh-kBtC-dYbQGUNKYBEQBv0uAxWcPap0b4ooVInyX3TLckUbq65bDapWJf94rwGe1vjTfFOMaCqBGJ-S963w5FUS7-cOPCSqaoZsKcCPZGp2XEG2DIlU6p9G3O5zhVX-Z_EzUdaHPxrrx2-KEdTbc10Kijz5-V-js9u8FsUQ9bqcc12i7lxU_CJ8tftO-MQm4npIuTZc-R3DL7-L_BUWqP-fPsrS7uXvLZdlBvmyZEAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری تلخ از عروسی که جنایتکاران مدعی حقوق بشر آن را به عزا تبدیل کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/686412" target="_blank">📅 01:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686411">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
منابع عربی از شنیده شدن صدای انفجار در کویت خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/686411" target="_blank">📅 01:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686410">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
المیادین: پاسخ امشب ایران، ویرانگر بود
منابع امنیتی ایرانی بامداد چهارشنبه در گفتگو با شبکه «المیادین»:
🔹
پاسخ امشب ایران علیه پایگاه‌ها و مراکز آمریکایی در منطقه قوی، دقیق و ویرانگر بود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/686410" target="_blank">📅 01:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686409">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2aac91e57.mp4?token=L83O5mCglK4BKZOmaGe3OyhkiyCHYgVE_7A9f0-Kpa-oUsi9Q30K1Vxu8Esq3UVJgq9ZtB_uuwmOxxSAJHfEjTsJ5omoH9xSNFzuXX07ru67PNMVDFgq8nXuWKyEfcbANkXir5hJ0egHIWJDhQKSmLtqyNtiDdduSf4UM880-fYB4CTJRhZ8z9DW3vgq2k_qWQM26xtmtmKz0mdhVfdGfechLIw_sNu71kvOdllRKk8A80SEsHjb8w6pBnmKKtrqA04dJhDpHjKll4GHEH5FyO3sPjWPoZbfAZBExqcvBCoxNNJB_5nMXAKp_xE3OSlyVsQvUcC-SXXyXlHncFcuZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2aac91e57.mp4?token=L83O5mCglK4BKZOmaGe3OyhkiyCHYgVE_7A9f0-Kpa-oUsi9Q30K1Vxu8Esq3UVJgq9ZtB_uuwmOxxSAJHfEjTsJ5omoH9xSNFzuXX07ru67PNMVDFgq8nXuWKyEfcbANkXir5hJ0egHIWJDhQKSmLtqyNtiDdduSf4UM880-fYB4CTJRhZ8z9DW3vgq2k_qWQM26xtmtmKz0mdhVfdGfechLIw_sNu71kvOdllRKk8A80SEsHjb8w6pBnmKKtrqA04dJhDpHjKll4GHEH5FyO3sPjWPoZbfAZBExqcvBCoxNNJB_5nMXAKp_xE3OSlyVsQvUcC-SXXyXlHncFcuZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عضو هیئت رییسه مجلس: هر کس در کشور به مذاکره دل ببندد و فکر کند که با این دشمن وحشی می‌شود مذاکره کرد و از ماجرا عبور کرد، دچار توهم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/686409" target="_blank">📅 01:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686408">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae470cfde6.mp4?token=iBjSTyg63jhJYKUH3S5pFaGMW46SQeBdt8b9kKMkQxLN53OwQwTYcAw8ZX2wtRMkMfvciEQvPupCbFEK6il_7x9c0mMYTfkciS2hueQ9VKfplFJqtplrAr3sivMWOCPfVRIVcqLKQHhQqQoC6xPyBN9_EOTmHJspu9dh_pX6OgfH8DPMgPmb25MzJDTlm3cXWt8QtJvtuAXWpS5l6u1_laoQSIt-at4v-SLTwTap8rdElkh8pxr79j8Zc5BCAk2y6AQBkJa07_aZJtwece1zdfoKrwP-mdr-JVbKtTBKE3x-9JsJBJC7upTBJ6d5PNJuulU5YN8SA05rSQ-7F4UoLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae470cfde6.mp4?token=iBjSTyg63jhJYKUH3S5pFaGMW46SQeBdt8b9kKMkQxLN53OwQwTYcAw8ZX2wtRMkMfvciEQvPupCbFEK6il_7x9c0mMYTfkciS2hueQ9VKfplFJqtplrAr3sivMWOCPfVRIVcqLKQHhQqQoC6xPyBN9_EOTmHJspu9dh_pX6OgfH8DPMgPmb25MzJDTlm3cXWt8QtJvtuAXWpS5l6u1_laoQSIt-at4v-SLTwTap8rdElkh8pxr79j8Zc5BCAk2y6AQBkJa07_aZJtwece1zdfoKrwP-mdr-JVbKtTBKE3x-9JsJBJC7upTBJ6d5PNJuulU5YN8SA05rSQ-7F4UoLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بالگردهای تخلیه بر فراز اردن
🔹
این فیلم پس از تأیید بصری اصابت یک موشک بالستیک ایرانی به منطقه‌ای در نزدیکی کمپ تیتین، یک اردوگاه دورافتاده تفنگداران دریایی ایالات متحده واقع در خارج از عقبه، اردن، منتشر شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/686408" target="_blank">📅 01:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686407">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
یو‌اس‌ای‌تودی رسانه آمریکایی: ایران با استفاده گسترده از موشک‌های پیشرفته «خیبرشکن»، حلقه پایگاه‌های آمریکا در منطقه را به‌شدت آسیب‌پذیر کرده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/686407" target="_blank">📅 01:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686406">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0CaJgIgKPFCn3o46Jj7-tp9sxU-75VuCirFgaG46YN-BsHlRUgE_vqi9onst5exlow6mQplsjWLKJJogWRIaqclHDKeAmG8l5zkF1h1Qw_Y1d1F1ItycK7iKcPBdIV4dcsahfgvL2onUtMlKk-o79kbxTApvewoSNdhNmoa2htRaQ6w560D9Z8lDNkGOeRAJoO_Ql16DNQarZJQXVyoEWVKOSwaljP6q_HSEssdlsTgaVSiiVpz0uUxtgjHxrlQd-DJItLJnorVlNjh-D1k4iCZotONG7ffsqsLi6qp41FSZepCBwRYZLINzzwA7UwZYLlDoJX0aIs3A4sU3Li__Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: هدف قراردادن یک عروسی و قتل‌عام مردم بی‌گناه در کوهستک، گواه نهایی استیصال مطلق مدافعان دروغین حقوق‌بشر و تکرار جنایات آن‌ها در میناب و لامرد است
🔹
این جنایات بدون مجازات نخواهند ماند. هیچ‌چیز آن‌ها را از ارادۀ کوبندۀ نیروهای مسلح ایران محافظت نخواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/686406" target="_blank">📅 01:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686405">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0acdf5c71a.mp4?token=lMGbTtMN5kd5DalL6ZxwogQGIRUM10NLUrfGepTrnoGyzf5wIogEieVXxRMeyyQnjxodioy_akAAyD_tnIP6apcbgMyLarSH4ECfAqBnEhKzz932DhwJouWMdPNcg1GKmQu7ma9lwZXAQdAndRK_hrFAEwIYPvr7w83JxRD8nqkXKMSsWGmiKUVqH-OkBZF7yuKruWpdqLmID8keZgfDitVVEWBO1MTlZk6a7B5aisrADLOdJ7xbj-EkrDOIVnc05K9tckVZDpCa_n9L-RS_Pv1vqbcN0ScBMKRfLf0--5092O3BvDY0FYCKSr5mc1GvUpQS3aslbySUKxIGwcKm-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0acdf5c71a.mp4?token=lMGbTtMN5kd5DalL6ZxwogQGIRUM10NLUrfGepTrnoGyzf5wIogEieVXxRMeyyQnjxodioy_akAAyD_tnIP6apcbgMyLarSH4ECfAqBnEhKzz932DhwJouWMdPNcg1GKmQu7ma9lwZXAQdAndRK_hrFAEwIYPvr7w83JxRD8nqkXKMSsWGmiKUVqH-OkBZF7yuKruWpdqLmID8keZgfDitVVEWBO1MTlZk6a7B5aisrADLOdJ7xbj-EkrDOIVnc05K9tckVZDpCa_n9L-RS_Pv1vqbcN0ScBMKRfLf0--5092O3BvDY0FYCKSr5mc1GvUpQS3aslbySUKxIGwcKm-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از شلیک دسته‌های پهپادی ارتش ایران به سمت پایگاه آمریکا در بحرین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/686405" target="_blank">📅 01:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686404">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار مشهد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e73625973f.mp4?token=KH5mqnvR_v0hbKdqZTntYa6lw50qx7rYZTgMMA54940E-DvCT3AWVL43sCdmCoJipM1ERd3a8BZC5gdWij0jykIFNZIjKoCcjXooyAH-s7ju39HivJ3KHqvx99ABIAsxymnwYhdYp5GUj1cm1clZo7qz1W881cD3UYhGh_IiKPshtD6NK41j8yhL-Fh6WcT5Qu6ZNVH91VRpWBxuRSRE0yRm30oq0GPy20HUVjE2kn6DqhRvJpHR6l3s7SHaoyfjh_GVwb1wBITB6hZ8lDlIf2_MXygNl9Gg2z2vIJFpKalY-MpZF7V3125Lg22APfbL_gsJ6LNED7J0GHK5DE9W9xoQzmh9xfIq7TTS790GR2Ix0czZBWBReW0IpU5us4NEbum3MReIgJtNfreex9MHfuswaDyrLb3j05VQGvWnyyvlq2P4ZSauFjBTFaJEzdy6rRHrzjc1bAUZH3gntXOgqNkZMciGVWmchXUKSsG_ywzx1g4nBuRjEWfUpNwOqtIa6btlGIVm32MSJab2iQJ79TvevZKmPXePsWqYy0wNVWoS4DsF80Fn4nXAsDhNLyTUcnS1xjX6D1JKXbD6YXGF3LiF_wVF1XnudmfO6f8aW7cYji6YlOzQF434Z6M3-feIT09z0kf9r2xVkrxtal327GOdvOE_wYRwRZ9CCLvw8kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e73625973f.mp4?token=KH5mqnvR_v0hbKdqZTntYa6lw50qx7rYZTgMMA54940E-DvCT3AWVL43sCdmCoJipM1ERd3a8BZC5gdWij0jykIFNZIjKoCcjXooyAH-s7ju39HivJ3KHqvx99ABIAsxymnwYhdYp5GUj1cm1clZo7qz1W881cD3UYhGh_IiKPshtD6NK41j8yhL-Fh6WcT5Qu6ZNVH91VRpWBxuRSRE0yRm30oq0GPy20HUVjE2kn6DqhRvJpHR6l3s7SHaoyfjh_GVwb1wBITB6hZ8lDlIf2_MXygNl9Gg2z2vIJFpKalY-MpZF7V3125Lg22APfbL_gsJ6LNED7J0GHK5DE9W9xoQzmh9xfIq7TTS790GR2Ix0czZBWBReW0IpU5us4NEbum3MReIgJtNfreex9MHfuswaDyrLb3j05VQGvWnyyvlq2P4ZSauFjBTFaJEzdy6rRHrzjc1bAUZH3gntXOgqNkZMciGVWmchXUKSsG_ywzx1g4nBuRjEWfUpNwOqtIa6btlGIVm32MSJab2iQJ79TvevZKmPXePsWqYy0wNVWoS4DsF80Fn4nXAsDhNLyTUcnS1xjX6D1JKXbD6YXGF3LiF_wVF1XnudmfO6f8aW7cYji6YlOzQF434Z6M3-feIT09z0kf9r2xVkrxtal327GOdvOE_wYRwRZ9CCLvw8kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حادثه مشهد صرفا ترافیکی بوده است
روایت «سرهنگ موسی آبادی» رئیس پلیس راهور خراسان رضوی از حادثه امشب
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/686404" target="_blank">📅 01:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686403">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
وزارت خارجه یمن: حملات ایران، مشروع است، کشورهایی که پایگاه‌‌های آمریکا را میزبانی می‌کنند باید بهای آن را بپردازند
🔹
وزارت امور خارجه یمن اعلام کرد که تداوم تجاوز آمریکا علیه جمهوری اسلامی ایران، اراده و ایستادگی این کشور را تضعیف نخواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/686403" target="_blank">📅 01:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686402">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
استاندار خراسان رضوی دستور پیگیری به حادثه بلوار وکیل‌آباد را صادر کرد
🔹
بنابر اعلام پلیس راهنمایی رانندگی مشهد، ساعتی قبل یک دستگاه خودروی جنسیس در بلوار وکیل‌آباد با سرعت بالا منحرف و پس از آن با تجمع‌کنندگان برخورد کرد.
🔹
در این حادثه ۴ نفر فوت و افزون…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/686402" target="_blank">📅 01:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686401">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9f02e16a.mp4?token=s9CJvsslTKdksADsONhsQGzh_7Lx80VWKueKc19kVIvmPoUviABtYR4S940M-c8FPJ-4wGFwPrFgv0k9axSC77AkQ-P38kd9j2HBb02U46s9Bv82vXy91Zn21TblvzEeRMMSn-0d05IslDazFMzdmhEBQadJWEetBzIwgw1SC9Kv-GiyfiuVOTWwxHdI2aVu_PWNwUOGVGILBs_n3yY4lGW-tDjBbdqTYmBLAXTTmbojTsSYUfbO43E_FJ7UmeLQYuBoURZgN2RwXKK66-0w0jXrnNDLnvTBGts2wRMMpA-xGaiF18o_7WBj0JgmWuULEJY7IpQQDtkz7Hv5jpX0VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9f02e16a.mp4?token=s9CJvsslTKdksADsONhsQGzh_7Lx80VWKueKc19kVIvmPoUviABtYR4S940M-c8FPJ-4wGFwPrFgv0k9axSC77AkQ-P38kd9j2HBb02U46s9Bv82vXy91Zn21TblvzEeRMMSn-0d05IslDazFMzdmhEBQadJWEetBzIwgw1SC9Kv-GiyfiuVOTWwxHdI2aVu_PWNwUOGVGILBs_n3yY4lGW-tDjBbdqTYmBLAXTTmbojTsSYUfbO43E_FJ7UmeLQYuBoURZgN2RwXKK66-0w0jXrnNDLnvTBGts2wRMMpA-xGaiF18o_7WBj0JgmWuULEJY7IpQQDtkz7Hv5jpX0VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برق مناطق آسیب‌دیده قشم پس از حملات دشمن متجاوز آمریکایی در شامگاه سه‌شنبه پایدار شد
🔹
فرماندار شهرستان قشم از رفع قطعی برق در مناطقی از این شهرستان که در پی حملات شامگاه سه‌شنبه آمریکا دچار خاموشی شده بود: جریان برق اکنون در تمامی نقاط قشم برقرار و پایدار…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/686401" target="_blank">📅 01:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686400">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
نیروهای مسلح اردن: شلیک ۱۳ موشک بالستیک به سمت اردن/انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/686400" target="_blank">📅 00:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686399">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
حمله دشمن به برخی زیرساخت‌های تلفن و اینترنت در بخش‌هایی از هرمزگان
اداره‌کل مخابرات استان هرمزگان:
🔹
در جریان حملات آمریکا به مناطق غیرنظامی و زیرساخت‌های خدماتی در بخش‌هایی از مناطق جنوبی کشور از جمله کوهستک در سیریک، به تعدادی از دکل‌ها و سایت‌های مخابراتی و اینترنتی هم خسارات جدی وارد شد. حملاتی که موجب قطع شبکه ارتباطی تلفن ثابت و همراه و همچنین اینترنت در بخش‌هایی از این محدوده شده است.
🔹
در همین راستا و علیرغم تداوم حملات دشمن، عملیات تیم‌های اضطراری برای رفع مشکلات پیش آمده و وصل مجدد شبکه مخابرات و اینترنت درحال انجام است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/686399" target="_blank">📅 00:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686398">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
شایعۀ حمله به کرمانشاه تکذیب شد
🔹
معاون استانداری کرمانشاه با رد شایعات مطرح‌شده؛ هیچ نقطه‌ای از استان کرمانشاه مورد اصابت دشمن قرار نگرفته و وضعیت در استان کاملاً عادی و تحت کنترل است.
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/686398" target="_blank">📅 00:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686397">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
سپاه امشب کدام پایگاه آمریکا را هدف قرار داد؟
🔹
سپاه در موج دوم عملیات «یا رسول‌الله(ص)» کمپ تیتین آمریکا در اردن را با موشک‌های بالستیک هدف قرار داد؛ مقری راهبردی در نزدیکی عقبه که محل استقرار و اعزام سریع تفنگداران دریایی آمریکاست.
🔹
اهمیت حمله در این است که آمریکا پس از اختلال مسیر هرمز بخشی از نیروهایش را به این نقطه منتقل کرده بود؛ حمله سپاه، نمایش اشراف اطلاعاتی و توان هدف‌گیری این جابه‌جایی بود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/686397" target="_blank">📅 00:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686396">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMSs3L92GFfOAreGgUqnwvRMEh3jyXY5l3SXKWOzBxcnxWEW1Z_HcMr7gO5C_HIeZ1uv-DKAC-RIyKqJ-Jq20XdoDUC19DnO5l3iiXc-kxTFOd0gQ27EbkvsPC2rDLJU6gkJvbWU5sOd4QWV-P_fvtnemc8FxaEEwxDoAcnvK6-Iabq-6nYQNRO2RksTs9hFtHkQk-jEXCXFCURj6C2VXhwsY0uCqpvwfCY0t2JnKqPtAy1wbwQd_VQId5Y6KNH8zQzQQjt71DEi8QXGdsgQuTnLJE1X8USP_iaC37GZEnOPkYTvZraVzGVvXLrnNoicU9M96Plxxbm017UIldRqFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویدئویی از مصدومان حمله ساعتی قبل آمریکا به یک مراسم عروسی در سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/686396" target="_blank">📅 00:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686395">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
چند نقطه از شبکه برق هرمزگان هدف حملات دشمن قرار گرفت؛ خاموشی تا کم‌تر از یک ساعت رفع می‌شود  مدیرعامل شرکت توانیر:
🔹
در ساعات گذشته، چند نقطه از شبکه برق در مناطقی از استان هرمزگان مورد اصابت دشمن قرار گرفته است.
🔹
در جزیره قشم و سیریک به علت اصابت و تخریب،…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/686395" target="_blank">📅 00:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686394">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
استاندار خراسان رضوی دستور پیگیری به حادثه بلوار وکیل‌آباد را صادر کرد
🔹
بنابر اعلام پلیس راهنمایی رانندگی مشهد، ساعتی قبل یک دستگاه خودروی جنسیس در بلوار وکیل‌آباد با سرعت بالا منحرف و پس از آن با تجمع‌کنندگان برخورد کرد.
🔹
در این حادثه ۴ نفر فوت و افزون بر ۱۰ نفر زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/686394" target="_blank">📅 00:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686391">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/face74d2d6.mp4?token=aRRpaqqtJ6WS_B6nuDWuE69XX0fHiOUZ-83Bhssntw6IZHA_woZM-7BWyJShYjLXklnzUCGR71G0TljV5HPPsnGo7sy9ziyDcVWSxZtzQFl5OIi0Rrek1OXL-KcKbKEpSdneEH7yenr3UJvB6p3yE_e4qOm2Hhfpm37L25zmfQgTrApmLBhv9IBMMH91oOOnrE_eWT_fvUZul_PhrIi9nI9-v6klKelmFUgR_e6WW8r5VuLQ0Xd6xI4wK74btJP0ItMd8_qHnni3a06C9ChSdLgWCh7d5ow1o2fi_Paj4Ofaxb0ee6R4pHDPZi8_L6YtEPA6AfqojFPSxQcwXpILYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/face74d2d6.mp4?token=aRRpaqqtJ6WS_B6nuDWuE69XX0fHiOUZ-83Bhssntw6IZHA_woZM-7BWyJShYjLXklnzUCGR71G0TljV5HPPsnGo7sy9ziyDcVWSxZtzQFl5OIi0Rrek1OXL-KcKbKEpSdneEH7yenr3UJvB6p3yE_e4qOm2Hhfpm37L25zmfQgTrApmLBhv9IBMMH91oOOnrE_eWT_fvUZul_PhrIi9nI9-v6klKelmFUgR_e6WW8r5VuLQ0Xd6xI4wK74btJP0ItMd8_qHnni3a06C9ChSdLgWCh7d5ow1o2fi_Paj4Ofaxb0ee6R4pHDPZi8_L6YtEPA6AfqojFPSxQcwXpILYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی پیش یک خودرو به تجمعات مردمی در اقبال لاهوری مشهد برخورد کرد و تعداد زیادی از مردم را زیر گرفت
جزئیات بیشتر
👇
khabarfoori.com/fa/tiny/news-3242100</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/686391" target="_blank">📅 00:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686390">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17d416a8f.mov?token=dATTF6_pd0eEqDIEhK-QmdJUtylKWhBibxziTOjEHClZHAVdLNDgzNNmPYjp2UU_iSrNyw0rdA6GhdKcWCOkmyfBn2vJfzdlkG6IlHG8Go_bwwkYGIg-7fhQq4YD8fWNbW164p3qtKmItgi2seM4fimlQxFojWgxWV198eRwZlgp1vatYCo5y4UnNIK9pJddZwJQvWyi5egxdy1myJ2GeMI8nCbOVf3A2GyjxfAtyBwgpljWmSOMX6IUwjIPeDdefJWLzgxO-P3plKaXLS-xqWAGt4uhHqZP5vTBCpQjBwe9xMISFJbC3NKPjMzMXJK16p9fv92RsPrL0r15AVlpMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17d416a8f.mov?token=dATTF6_pd0eEqDIEhK-QmdJUtylKWhBibxziTOjEHClZHAVdLNDgzNNmPYjp2UU_iSrNyw0rdA6GhdKcWCOkmyfBn2vJfzdlkG6IlHG8Go_bwwkYGIg-7fhQq4YD8fWNbW164p3qtKmItgi2seM4fimlQxFojWgxWV198eRwZlgp1vatYCo5y4UnNIK9pJddZwJQvWyi5egxdy1myJ2GeMI8nCbOVf3A2GyjxfAtyBwgpljWmSOMX6IUwjIPeDdefJWLzgxO-P3plKaXLS-xqWAGt4uhHqZP5vTBCpQjBwe9xMISFJbC3NKPjMzMXJK16p9fv92RsPrL0r15AVlpMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از مصدومان حمله ساعتی قبل آمریکا به یک مراسم عروسی در سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/686390" target="_blank">📅 00:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686388">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNAjOfHsQC7HHjdLxEuFmFyl5vQpp6H2Vmxt86EREdp65oEsybhEpCCAvzWONgPzVts7Fp4O-1wNKsn2dzgpzqhEmJu2PxGjvt9SyLZRCpU91w_11M7aWmd5-oduEz04hX7kfVHsi93UlxNJ2OXbEwBkBTn74XRZL0qdcFhtkuSJTt_TAzGaStHsHaYhN34_-zcuzk3S0pFJVURyE8s7Nq3kVy6CpAcNomqRzJDShQKPjAh0CULPjvUBf1pYcaVBEC15iKCV6uZn9NcULgD-vpYEwCFAMrvnYFFSQm4UlFotiMWacQSyit-cpo1Swhp_UwYkIn7OUqMUytR7Wscb6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توقف پروازها از فرودگاه نجف به ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/686388" target="_blank">📅 00:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686387">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e95424e8.mp4?token=vSfaKWvyBK0P-DkvlAqLzJ377qIX4AYU826Leif5xoAn_5J-yNAEREV1dXRyQvfAb_HZvkjpcVHWoxNqiDcDwjXqd-89AecXczdJ6zAHSTYcSR-2B3Va7ugTjIqUCyfFo8rNVemZZnw80Djz6A8P58QOXVvNcxGBpQ9hmy0O4r_A6P96SCDjMRZAAywKv-KhQAybSRiymVKFkZrRek-jvKd1_8bQHJtyIBENgQGX2zlYR_FZM3JsVW-QOa0gNUIG-WghCjKoq9QNcgYIa6b4IrxWYosNTkIoXUyPDi7Q96kE2lgrTOpatHcf0G3TxD3g3Y7_-rQqmewyF-HoPNtJRSGLIpj_fmYfaNA-USljHwWzhXpjhvFz4xCkA-2pLrI0f49SQkyyceaQmoPZJo2-23AuERTyFhIlEWSwHnzh9PwCOD47qvpIvLfgaWcuEQ1dT0A62Oyx9q-kNM-f0NAyb2KJDkP11OhiBjZ1pAsyWaOni6_IYJUcOt5zwAZtNcPIGeFSjZh9qXdgbmPC6q8LPwKm3sI9Bh2fmGgRgp1h-YPRBGcsUSupQWN-L0c66JOK2ITucDJdHMo1RcGPWSTuHy2I5BeHk-WQXtGmCgMl-D33qH6MIVYJAdQ63-gs8CUz4-zxkfXb5kjUuUDLD17JTfv7j0eB0ZIm1U7xg4p2sOM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e95424e8.mp4?token=vSfaKWvyBK0P-DkvlAqLzJ377qIX4AYU826Leif5xoAn_5J-yNAEREV1dXRyQvfAb_HZvkjpcVHWoxNqiDcDwjXqd-89AecXczdJ6zAHSTYcSR-2B3Va7ugTjIqUCyfFo8rNVemZZnw80Djz6A8P58QOXVvNcxGBpQ9hmy0O4r_A6P96SCDjMRZAAywKv-KhQAybSRiymVKFkZrRek-jvKd1_8bQHJtyIBENgQGX2zlYR_FZM3JsVW-QOa0gNUIG-WghCjKoq9QNcgYIa6b4IrxWYosNTkIoXUyPDi7Q96kE2lgrTOpatHcf0G3TxD3g3Y7_-rQqmewyF-HoPNtJRSGLIpj_fmYfaNA-USljHwWzhXpjhvFz4xCkA-2pLrI0f49SQkyyceaQmoPZJo2-23AuERTyFhIlEWSwHnzh9PwCOD47qvpIvLfgaWcuEQ1dT0A62Oyx9q-kNM-f0NAyb2KJDkP11OhiBjZ1pAsyWaOni6_IYJUcOt5zwAZtNcPIGeFSjZh9qXdgbmPC6q8LPwKm3sI9Bh2fmGgRgp1h-YPRBGcsUSupQWN-L0c66JOK2ITucDJdHMo1RcGPWSTuHy2I5BeHk-WQXtGmCgMl-D33qH6MIVYJAdQ63-gs8CUz4-zxkfXb5kjUuUDLD17JTfv7j0eB0ZIm1U7xg4p2sOM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستور پوتین برای حمله به تأسیسات انرژی اوکراین
🔹
رئیس‌جمهور روسیه گفت که دستور حملات گسترده به زیرساخت‌های انرژی اوکراین، در واکنش به حملات این کشور را صادر کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/686387" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686386">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b044a65a7a.mp4?token=WXE5USiv1J8CRg89982rhXE8y1hOCks9S0F_f033Imsy9fYDuk6DVSdK405wpTkrX8LqfRQb3SZfEn28JXfeAscWWRLyfjZqmnHL48fNrdHOElGMat-LME0CovGrOhlJRGfDvhYQcrVTWtxFxHkSkv4Vn7TAAs_j8U-bgwo70n84_ebGdZq_lULD7YQXdLqK2tqx2IotTq_P-XSxCnfm9FswMq_EtATXPJs0fQGNnJ9aRKegeCBYwotLhwFru8w1z_KFeaN5u_2oOqqEKVYIVkDNN5usUmTcPfcOIJXCinHemVXiTYagI92YVw97otzfy6fWTXJ6g5nT2xVPJnyPcg1l9Kx_LhVuSGJME88jG9QK1C6Uyy-qsmfUdrqnZ1wORRCsdx1zmEpeM3GivB3T1613viPA7KpoZzUN-_VAJIBZgjCM-bUo2VF6jo6xMluksJCNR70zalq21lhy6VQfVOGdKbCjoBq-MAyPkNSrFZaDuQ3eCT-J0ldnEfFvWT8FHfx2hfz_LdOW1_u017RtMRGqbZxQ6AUwHaDp2P3YBMnbL0lgVKWgTJ4P7-JaLbtp6wY5nsQXG2_z9yCp0kUp1r_m4knwc3e1QmHJjZ1OrvblFpSUVqJ35YgFFBbleZ51wiNCrvwMSwWHFF3tGKoCnCHmQCctcBcnxSwQ0R9PwkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b044a65a7a.mp4?token=WXE5USiv1J8CRg89982rhXE8y1hOCks9S0F_f033Imsy9fYDuk6DVSdK405wpTkrX8LqfRQb3SZfEn28JXfeAscWWRLyfjZqmnHL48fNrdHOElGMat-LME0CovGrOhlJRGfDvhYQcrVTWtxFxHkSkv4Vn7TAAs_j8U-bgwo70n84_ebGdZq_lULD7YQXdLqK2tqx2IotTq_P-XSxCnfm9FswMq_EtATXPJs0fQGNnJ9aRKegeCBYwotLhwFru8w1z_KFeaN5u_2oOqqEKVYIVkDNN5usUmTcPfcOIJXCinHemVXiTYagI92YVw97otzfy6fWTXJ6g5nT2xVPJnyPcg1l9Kx_LhVuSGJME88jG9QK1C6Uyy-qsmfUdrqnZ1wORRCsdx1zmEpeM3GivB3T1613viPA7KpoZzUN-_VAJIBZgjCM-bUo2VF6jo6xMluksJCNR70zalq21lhy6VQfVOGdKbCjoBq-MAyPkNSrFZaDuQ3eCT-J0ldnEfFvWT8FHfx2hfz_LdOW1_u017RtMRGqbZxQ6AUwHaDp2P3YBMnbL0lgVKWgTJ4P7-JaLbtp6wY5nsQXG2_z9yCp0kUp1r_m4knwc3e1QmHJjZ1OrvblFpSUVqJ35YgFFBbleZ51wiNCrvwMSwWHFF3tGKoCnCHmQCctcBcnxSwQ0R9PwkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حملات گسترده موشکی به اهداف آمریکایی در اردن در موج دوم عملیات تنبیه متجاوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/686386" target="_blank">📅 00:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686385">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c02b3ddf9.mp4?token=Y_LwUqIwMw-M9fmPdHaQxRdwS0EbNtCUA9hXkhXId9RKFvU5szkxWo2toFbI4ElwYLcQwa2epNDe_3MU02-mj-x6g9pFY-FqRykz0XlF8T3jn630MO-VpRwK4OoGeeRpMrHjFi2F_S4MAXK849ObIfPwSBdcn3mRuWQRCRri4atYGUtNXCXVGCJ2pqbIMwlh_PYr9XA8F29y_-m8p-rE_CfgX7vAZbjv3nq_eyyXTn93zN0BXyY6hLJdVXOi2IrI8OZOrru5Cf-bDxBmj5CNCPtmfw342T0sTUmXQp-7tJ5ZsSezLYVODE88PEFIT0eZXpVEQS8SPtZ-rceCXjmfbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c02b3ddf9.mp4?token=Y_LwUqIwMw-M9fmPdHaQxRdwS0EbNtCUA9hXkhXId9RKFvU5szkxWo2toFbI4ElwYLcQwa2epNDe_3MU02-mj-x6g9pFY-FqRykz0XlF8T3jn630MO-VpRwK4OoGeeRpMrHjFi2F_S4MAXK849ObIfPwSBdcn3mRuWQRCRri4atYGUtNXCXVGCJ2pqbIMwlh_PYr9XA8F29y_-m8p-rE_CfgX7vAZbjv3nq_eyyXTn93zN0BXyY6hLJdVXOi2IrI8OZOrru5Cf-bDxBmj5CNCPtmfw342T0sTUmXQp-7tJ5ZsSezLYVODE88PEFIT0eZXpVEQS8SPtZ-rceCXjmfbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری دردناک از کودکان مجروح حمله موشکی امریکا به سیریک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/686385" target="_blank">📅 00:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686384">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
تکذیب صدور نوتام برای بسته شدن فضای کشور
سخنگوی سازمان هواپیمایی کشوری:
🔹
نوتامی برای بسته شدن فضای کشور صادر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/686384" target="_blank">📅 00:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686383">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
سپاه: پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تبتین هدف موشک های بالستیک قرار گرفت
؛
تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
ملت قهرمان و بپاخاسته ایران اسلامی، ارتش تروریستی و شکست خورده آمریکا، عاجز از رویارویی مستقیم با رزمندگان اسلام با حمله وحشیانه به یک منزل مسکونی در سیریک، محل مجلس عقد دو جوان پاک را به خاک و خون کشیده و با به شهادت رساندن و مجروح کردن نزدیک به پنجاه نفر از مردم عزیزمان خاطره وحشیگری مدرسه میناب و ورزشگاه لامرد را زنده کرد.
🔹
رژیم کودک‌کش آمریکا در این حمله جنایتکارانه یک بار دیگر با به شهادت رساندن چندین نفر از جمله یک کودک، عمق کینه‌توزی و دشمنی خود با مردم ایران را آشکار کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/686383" target="_blank">📅 00:13 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
