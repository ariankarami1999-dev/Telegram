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
<img src="https://cdn4.telesco.pe/file/vqNeqp1PZYaEGBUuN1T9TxAN61XYEYIy-kTtLZI6okA7qNo1JNbbUfZd_fRA_W8jnnYl3wTTNuuYRykZK3yREXeDmkg3xweIVurJJKnpi1ZfB__qSNnPhtONemk3xYDTX1RpSBNBuybiQaL3Rlw7vVg1fR8VWqbQP_CDCO_VL1A6suAzfT43VNego_MwYnyk4furXUFqsV4Sha6NorSA2PrTLqvKH1VnCl3WfL9r8esiTacDphK3F4fX_w6g9cByVShI5nO2-G-DKkuMf4qKNkwn8MBBchWdN9mHvjxQelhM6LLvbM2fjr9ysl1HVNnaRb_n1AjAIH5aaeqOq2PS2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 965K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 17:08:24</div>
<hr>

<div class="tg-post" id="msg-125069">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/45c2d0b1d6.mp4?token=e9Cr3-NWIlpo3nr0MWX5bYC0wnANVoug-Q09QSD4SpVES_DE3gPzv-HYtdlc5kR72s1YW-2ZdOIfM8EFoAWkxaFxZOdDy5hUxhEZv6E4eGCLzfAAYIQclyJwN9ByU8X9bXIA8MZCNseHFgE2xOQ7HAVwQV0bIM4GzVr3jwG7QAB-eilYI0vKukvIJqZw7ASv5RNqAoQsDQZ51ktLONbwiNkv0-3VHXB7faIM6Ip3M1uhh65bT268p_6JK9DvnWYeFS1Eb_oImPIjeDsDu2pgYzJZoxbCofwMpdEEWRMMh_hE_9fQzAYpR236XS68JqjuEKBWqo2XvFoqlaA859H3cw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/45c2d0b1d6.mp4?token=e9Cr3-NWIlpo3nr0MWX5bYC0wnANVoug-Q09QSD4SpVES_DE3gPzv-HYtdlc5kR72s1YW-2ZdOIfM8EFoAWkxaFxZOdDy5hUxhEZv6E4eGCLzfAAYIQclyJwN9ByU8X9bXIA8MZCNseHFgE2xOQ7HAVwQV0bIM4GzVr3jwG7QAB-eilYI0vKukvIJqZw7ASv5RNqAoQsDQZ51ktLONbwiNkv0-3VHXB7faIM6Ip3M1uhh65bT268p_6JK9DvnWYeFS1Eb_oImPIjeDsDu2pgYzJZoxbCofwMpdEEWRMMh_hE_9fQzAYpR236XS68JqjuEKBWqo2XvFoqlaA859H3cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ماجرا و محتوای این پست بسیار دردناک و ناراحت کننده‌اس، اگه بیماری قلبی دارین به هیچ وجه نخونین.
توی سنندج یه زن و شوهر از هم طلاق میگیرن، بعدش مَرده حضانت بچه هارو به عهده میگیره و میره یه زن دیگه میگیره.
دیشب همسایه‌ها بعد از شنیدن صدای جیغ وارد این خونه میشن، می بینن دو تا دختر 7 و 15 ساله داخل دستشویی حبس شدن.
با اومدن پلیس و اورژانس معلوم میشه توی این مدت پدر و نامادری‌شون تا سر حد مرگ شکنجه‌شون میدادن!
یکیشون فکش ۳ ماه بود شکسته بود، اون یکی دست، پا و دنده‌اش، شکسته بود. رحمِ دختر بچه رو سوزونده بودن!
به بچه کوچیکه انقد غذا ندادن مثل چوب بستنی لاغر شده بود. انقد موهاشون رو کشیدن که مو روی سرشون نمونده!
کل بدنشون جای سوختگی بود. دکترا گفتن هر لحظه ممکنه بمیرن انقد عذاب کشیدن. پدر حرومزاده‌شون بهشون تجاوز کرده و برای اینکه معلوم نشه آبجوش ریخته روی واژن دختره!
این پدر و مادر امروز دستگیر شدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8 · <a href="https://t.me/alonews/125069" target="_blank">📅 17:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125068">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">امروز عراق با اسپانیا بازی دوستانه داره و جمهوری اسلامی با مالی
😐
@AloSport</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/alonews/125068" target="_blank">📅 17:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125067">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57af1916b1.mp4?token=k3TfXSyIa7kLv8L3N313tjUCpeC3eFPPiTN7ZOU1CbLHeFIXynXD_F9RXjrySixskKLI3Qg29kO2yuAY90B9efYG4ISS69ck2YSBUkz8vAoB9ubNVEsjuArAYU1tZxuVf4_Pl3_hb8xcXxFiVIkMtc0mkqq26Vx_bD9WCjb3DnRR5ivNIaYmntolHtuEhtmv11RH3ENCT5n5qBJXnahpJJR6pUWv5ipxqC0fYRFZyK27dhVuPKbZUcmeh4dXRgA9hA13zNpp_QJ1BaRIp_X5cTQ9TbRk-yRCcmkjcNELdwWINk2vHqofDCFxexH1s1HKhpASAmQCiTpgsnFOu6jF3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57af1916b1.mp4?token=k3TfXSyIa7kLv8L3N313tjUCpeC3eFPPiTN7ZOU1CbLHeFIXynXD_F9RXjrySixskKLI3Qg29kO2yuAY90B9efYG4ISS69ck2YSBUkz8vAoB9ubNVEsjuArAYU1tZxuVf4_Pl3_hb8xcXxFiVIkMtc0mkqq26Vx_bD9WCjb3DnRR5ivNIaYmntolHtuEhtmv11RH3ENCT5n5qBJXnahpJJR6pUWv5ipxqC0fYRFZyK27dhVuPKbZUcmeh4dXRgA9hA13zNpp_QJ1BaRIp_X5cTQ9TbRk-yRCcmkjcNELdwWINk2vHqofDCFxexH1s1HKhpASAmQCiTpgsnFOu6jF3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویرانی در تبنین، جنوب لبنان، پس از چندین حمله هوایی اسرائیلی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/125067" target="_blank">📅 17:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125066">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/alonews/125066" target="_blank">📅 16:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125065">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LCTg3RSJjPrdo1rlRcUJm8j7W3t5m3ujdVyHdv-aPK1hVn33_NgQ2u317YP_B7XSYbato3an0ZD85JCrLTHFkPG_dTMVZnwHySJtAZGusneq0QsEhFaizuWHc9u-dSXQ5kzRRFTQ_ewHmKeYzvZgN-_mzn7pq6XMuG1MvR73SXQeIqgqVadl3IrBqPAIjfhXZWhZu6aOQ5m2YNU4sNYFjhjPuskiqqHUrORjlTPaFoHR6aqG3FcnGfNXE5hJfZi_9YO0p0G18_IlzyUZ_gkJfNN_YCigXyGNgo3IwcJMmggDsRCoarJWB0ilvk3qvuQ8SK30eCFNeBg2NQYq1LepSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/alonews/125065" target="_blank">📅 16:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125064">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
الجزیره: قیمت نفت پس از توافق آتش‌بس لبنان و اسرائیل کاهش یافت
🔴
قیمت نفت پس از توافق آتش‌بس بین اسرائیل و لبنان کاهش یافت، زیرا امیدها برای توافقی گسترده‌تر برای پایان دادن به جنگ آمریکا و اسرائیل علیه ایران افزایش یافت که می‌تواند به بازگشایی تنگه هرمز منجر شود.
🔴
معاملات با احتیاط انجام شد و کاهش قیمت محدود بود. قیمت معاملات آتی برنت ۱.۱۴ دلار یا ۱.۲ درصد کاهش یافت و به ۹۶.۶۷ دلار در هر بشکه در ساعت ۱۰:۲۲ به وقت گرینویچ رسید، در حالی که نفت خام وست تگزاس اینترمدیت ۹۰ سنت یا ۰.۹ درصد کاهش یافت و به ۹۵.۱۲ دلار رسید.
🔴
دو قرارداد روز چهارشنبه حدود دو درصد افزایش یافته بودند، پس از آنکه خصومت‌های تازه در خاورمیانه، از جمله حملات ایران به کویت و حملات نظامیان آمریکایی در نزدیکی تنگه هرمز، روی داد.
🔴
جان ایوانز، تحلیلگر نفت پی‌وی‌ام، گفت: «ایران بر توقف تجاوز اسرائیل به لبنان، یعنی حزب‌الله، تأکید دارد و به نظر می‌رسد واقعاً پیشرفتی حاصل شده است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/125064" target="_blank">📅 16:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125063">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
رسانه اسرائیلی i24news : یکی از پیشنهادات مصالحه «صندوق کمک‌های بشردوستانه» برای ایران به مبلغ میلیاردها دلار (من شنیدم ۶ میلیارد دلار) بود تا دارو، غذا و مسائل بشردوستانه خریداری شود - تا کنون ایران این پیشنهاد را رد کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/125063" target="_blank">📅 16:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125062">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
کرایه حمل‌ونقل عمومی جاده‌ای از ۱۶ خرداد ۲۱ درصد افزایش می یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/125062" target="_blank">📅 16:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125061">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPMp4oIgC66a9qLuSGJj53PLwJeS5I61i7ZfcESGPIvs_gVYya5Tly4eslSJf8c4j5CBqyQvUU3Tb4eSdZ_SNIo_NricPei0Q3TQLopMN7z_p0cxbprHNmpkmaEOvDMW7hUfL0iEPTqQDiC0MG1DPxgtXZszco-bc4NQz_pmN3LAhVwfdprREk8QHsunZZ73cqvwJoFb3P_KGgDws-EcqPgGmFQ1kqCIKLhC-XnN6El1ZQETmCQeQrznWCApSL4xlhGCzeWiI3G03KXjFfK5wUPebyUDynuQx9z04vR5qO-ihDNP0cmAYvqBAVBPnAQfPxtjsxKxdex-Gp7ANC10Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مراکش در حال ساخت بزرگترین استادیوم فوتبال جهان، با ظرفیت ۱۱۵,۰۰۰ نفره
🔴
نام این ورزشگاه «گرند استاد دو کازابلانکا» هستش، با هزینه ۵۰۰ میلیون دلار قراره ساخته بشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/125061" target="_blank">📅 16:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125060">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
بریتانیا و فرانسه برنامه‌های نهایی برای رهبری عملیات چندملیتی پاک‌سازی مین‌ها در تنگه هرمز را تکمیل کرده‌اند که ممکن است ظرف چند روز پس از توافق آمریکا و ایران برای بازگشایی این مسیر آبی آغاز شود، گزارش بلومبرگ.
🔴
ائتلافی متشکل از ۱۵ کشور نیرو و تجهیزات برای این ماموریت اختصاص داده‌اند، اگرچه استقرار تنها پس از بازگشت حمل‌ونقل تجاری عادی از طریق تنگه آغاز خواهد شد.
🔴
مقامات بریتانیایی و فرانسوی معتقدند که تلاش پاک‌سازی مین باید توسط ائتلاف مدیریت شود نه ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/125060" target="_blank">📅 16:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125059">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
دبیرکل حزب‌الله: از ایران سپاسگزاریم که با وجود چالش‌های بزرگ خود، به ما برای بازپس‌گیری سرزمین و حق‌مان در مواجهه با تجاوزات اسرائیل و آمریکا کمک می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/125059" target="_blank">📅 16:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125058">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رهبر حزب‌الله، نعیم قاسم: مذاکرات با اسرائیل بی‌شرمانه است
🔴
تا زمانی که اسرائیل در لبنان حضور دارد مقاومت ادامه خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/125058" target="_blank">📅 15:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125057">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ادعای موساد به گفته کانال ۱۲ اسرائیل، سلاح‌ها و مهماتی را که از حماس و حزب‌الله گرفته بود، به کردها منتقل کرد تا بخشی از طرحی برای سرنگونی رژیم ایران باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125057" target="_blank">📅 15:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125056">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJfhLMk-1c3n_C2UyUixck1p0tbHUoPS1OIL8k5E0OcWuN7iEL1jKOkirZlxLfb2GZWt18gojV970xCmQbpAnboQx0uqXIJutV_gdTj-SRyRX9DDhsCs338683gYL0Mnz6Q1_isKw9ohn1hLVifFZyJRkkeYFYy6ttgs6TdHpQZfmeVibMItFxZo4q3FHnUlse5EqeSN36g7VJrTvQQhIjCKk5pH-IxvTzHXUroF_lmEo4LRxGDqTd51Py5PbhJcbRG9JC6B-2tHnD4fs0j4KWZb5HKJiajN_YyBIBR3sSfAjcDK3PsGB7eGu2NNmEn-cjV0N9Ic3iBNoEzyCofL8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بررسی دقیق کمک‌های مالی آمریکا در عملیات «خشم حماسی» توسط USAID
🔴
ون نگوین، بازرس کل موقت آژانس توسعه بین‌المللی آمریکا (USAID)، اعلام کرد که این نهاد برای تضمین «شفافیت و پاسخگویی دقیق»، هرگونه کمک مالی خارجی مرتبط با عملیات «خشم حماسی» را مورد بررسی قرار خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/125056" target="_blank">📅 15:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125055">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کاتز: توافق کردیم؛ اما با آزادی عمل کامل برای حمله به بیروت
👈
وزیر جنگ اسرائیل جزئیات تازه‌ای از توافق با دولت لبنان فاش کرد: ماندن ارتش اشغالگر در منطقه امنیتی تا «خط زرد»، ایجاد منطقه غیرنظامی در جنوب لیتانی و آزادی عمل برای حمله به بیروت با چراغ سبز آمریکا.
🔴
ارتش اسرائیل به هدف‌گیری زیرساخت‌های متعلق به حزب‌الله در لبنان ادامه خواهد داد.
🔴
وضعیتی که در لبنان تحمیل کرده‌ایم ممکن است در آینده به توافق صلح با این کشور منجر شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/125055" target="_blank">📅 15:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125054">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzBjo0ZVVuIvCtUlbNg0gqtx9v5KMY3Hly3BynlGlenJy6eniYOV05tJxngNGdDBdBXuAnkrJc2T7UkbvV80FQJON0s_dQAkQFcGRo9ft4BCH28AbH1gA-YCgFOt-dS1MKwoYBi4cVhLvMD2fLy-1MSULvlNHqfp9DIfN_9FYJ1TuREmb09wF49tkohqiMbp4ieElEHbpFhfUFOhMZjSQQwU501UfVPLjWoTZMtr6TgFOhWzIFeqEkWbSvsPXziKy6M_YuqY459aTCijFLrQAFmBs63Ir12qfgjfdJZ4r45Lm7txWrqOrAqs_Vu2kiOCH8hdeTZmGGTiagR6DBkVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال‌استریت ژورنال: کشورهای حاشیه خلیج فارس در حال سرمایه‌گذاری در خطوط لوله، راه‌آهن و تأسیسات ذخیره‌سازی هستند تا جریان نفت را حتی در صورت بسته بودن تنگه هرمز حفظ کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/125054" target="_blank">📅 15:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125053">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ درباره قطعنامه اختیارات جنگ: دیروز، در یک رأی‌گیری بی‌معنی، مجلس با ۴ جمهوری‌خواه بد و همه دموکرات‌ها، اختیارات جنگ من را محدود کرد، درست در میانه مذاکرات نهایی من برای پایان دادن به جنگ با جمهوری اسلامی ایران. چه کسی چنین کار غیرمیهن‌پرستانه‌ای انجام…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/125053" target="_blank">📅 15:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125052">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
قراردادهای آتی نفت خام برنت و نفت آمریکا با امید به پیشرفت در توافق صلح آمریکا و ایران، بیش از ۳٪ کاهش یافته و ضررهای خود را افزایش دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/125052" target="_blank">📅 15:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125051">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
نیروهای اوکراینی به یه شناور گشتی کلاس «Svetlyak» در کریمه حمله کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/125051" target="_blank">📅 15:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125050">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
۲ عضو شورای شهر ایلام با دستور مقام قضایی بازداشت شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125050" target="_blank">📅 15:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125049">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/No9ydGBaitVvaUIB3a3Ei75flpfSTM94Uze_ToGS0Lh-xjUw1ntGEiKGGXDqmounCTOT4ii5qGiBZ-yV4PYTMd0NRplyJgZBYxGaOJkxVM8GKXLrxMlazEW8yOQcPD_PaG50Pk9lWxVRhQ_x1XdlpQ0999TnQrXgbMkH_NmJ0SYk7gAGB8o0LLQdmsnZg42ksK0oSl9plbFYH3Cs_yIAP_vzybt0OfHreqL8QiaJKKHZ9jU5lqTRI1M08xrBd6InYvt9d5y6Z4Qxw3yO5x3teBXt9UEL3dJFu-VTBVCfbmmQjRCa0_syPe-DC-v4VHYX62tNPGj6D3ibp790Kny5lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ عکسی از نشان‌های پلیس و اصلاحات با نماد جمجمه به سبک ترامپ منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125049" target="_blank">📅 15:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125048">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a6b0ffdeb.mp4?token=L79IsKQHDJe9kXrkaeTsnqA1wlCb9BVrlA7n-H03BhX4LNaIX0zMPfwg25GAotW_YmCyNqd0dgJqV0A6UN2lr3XppbE73o4CH-7SIjpCm6TYiZ7L4a6d9daWkz758si9OqN86FT4ssUaG8704oMPehvjYKe0ngjOipfcorNJLqL-meF6s-MhbAKGBKH7ZNMmTfI_jorHcZO8TDjAokvXA48hgWTngUBdb3p_B5eDAK8DRWdjayEBobat4dpvpaezuZOrfUPIn2mmO7wkHpRj3jks8OOMoGyxFhsIR_Duqw3Q0EMlXFFapxNd5R3FEZ_SQDLIdEyQAJVEeq-dBdqKOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a6b0ffdeb.mp4?token=L79IsKQHDJe9kXrkaeTsnqA1wlCb9BVrlA7n-H03BhX4LNaIX0zMPfwg25GAotW_YmCyNqd0dgJqV0A6UN2lr3XppbE73o4CH-7SIjpCm6TYiZ7L4a6d9daWkz758si9OqN86FT4ssUaG8704oMPehvjYKe0ngjOipfcorNJLqL-meF6s-MhbAKGBKH7ZNMmTfI_jorHcZO8TDjAokvXA48hgWTngUBdb3p_B5eDAK8DRWdjayEBobat4dpvpaezuZOrfUPIn2mmO7wkHpRj3jks8OOMoGyxFhsIR_Duqw3Q0EMlXFFapxNd5R3FEZ_SQDLIdEyQAJVEeq-dBdqKOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در حال توضیح‌دادن این موضوع که طول استخر کاخ سفید (از پروژه‌های محبوب ترامپ) از ارتفاع آسمان‌خراش‌های معروف دنیا بیشتره!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125048" target="_blank">📅 15:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125046">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JrMVZIKv7XbulS_JFltFz6YV8XKJ1ljp6RUoRrh0bxzXRmA6Vi4SriM0gsribSu913UavXo_HcBguxkIcKX8Qhzj02Yn-S84BRmfGq3RUbx2I5KjNb6aQDnLSGbUNULKe88rB0b3ghkzHd7uzkOu3wRJgPCjGs7E23wCJGUR8urw3pggAv48Zy0l_BoRvNMF0jjt-kMLxj5s0fGCpk5LAVDHrBhrrJJG3udVaBPMhUFOqR2jZCCqfr090lnkvxeIJ1dNzPLPByyXgZm1876_4GS3N8_gUZDQcoYJjeE9I_Xl0EG0VG7qOAu9hsNG03h4tJcNPWpg306OngKbM-1lNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اولین بار پارک ویژه آقایان توی قزوین راه اندازی شد!!!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/125046" target="_blank">📅 15:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125045">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملات هوایی به ساختمان‌هایی در تبنین و حاروف در جنوب لبنان انجام دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125045" target="_blank">📅 15:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125044">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQvrHYQ0LEbL8zBJbUKVo80QHFVr0RNAnq8-5QW-ZMewqY9ZzGDfThf5wX9t-f0aQDTuFBNSjwg48poeATc_xwTv7gscWmoSy4-ffLjsVEHg2CKei1Jr2Pdv044Va4AzaDCBwpcDvZFfl7-ghCngyU_w2z2flv2JMpsQbENa1j6f-Q4vB-CrqiNc0HSb-4SPxlw4exBt8l3HSw7BXtFBzsQP-rjHQRC3kTf-PEzq8P1JX7jL0c0KBBZZJugaRjM3QfHzeAMu8r_5PufuUENxWeCAShZ8eyr39Sbwpe_KEe8E4MJDaOV05qweRnQCZpN5N1NT31iz7yj1L_rhrz9QdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش دکتر باز شد فقط با گیگی
8
فقط برای الو نیوزی ها با کد تخفیف
🔥
Alonews
همراه با لینک ساب
🔗
و مدت زمان 30 روزه
❌
بدون هیچ ضریبی
❌
⚠️
ظرفیت به شدت محدوده
⚠️
📥
جهت خرید سرویس کیلیک کنید
📥
🤖
@Xvpn021Bot
🤖
🤖
@Xvpn021Bot
🤖
🤖
@Xvpn021Bot
🤖
🤖
@Xvpn021Bot
🤖</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/alonews/125044" target="_blank">📅 15:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125043">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
فیفا در آستانه آغاز جام جهانی ۲۰۲۶، ورود بطری‌های آب چند بار مصرف را به‌تمامی ورزشگاه‌های این رقابت‌ها ممنوع کرد؛ این نهاد پیش‌تر اجازه ورود بطری‌های پلاستیکی شفاف و خالی را داده بود، اما با اصلاح آیین‌نامه ورزشگاه‌ها، این مجوز لغو شد.
🔴
دلیل این تصمیم مسائل امنیتی و جلوگیری از خطر آسیب‌دیدگی ناشی از پرتاب بطری‌ها و سایر اشیا به داخل زمین یا سکوها عنوان شده است. همچنین ورود اقلامی مانند قوطی، لیوان و شیشه نیز ممنوع خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/125043" target="_blank">📅 15:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125042">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
اسکای‌نیوز: حزب‌الله توافق آتش‌بس دولت لبنان و اسرائیل را رد کرد و نپذیرفت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125042" target="_blank">📅 14:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125041">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-2S7oYLpf3tG4IrbPINR_zHbZbQnMOnyhqQtp4AN7Y5zHGLtkewVnHH-l5jDRZ2tBE4kE4X5harYlBGePbsaZ1fnBtEWL7QS6Gx-pibF6Lff5Vqj_4hR8lHrqNo6nx4qx7PTSYmg7llPEHqo827-FbnA67iSn1QsP_3_s5gthwjgBNLEMxZXr7PAMsH_T5LrEyaQx0NyFWAo0OpmPCaYk99LpkoiYfzStlz61yVYIwxtRq-av4LIZTOZZ4hzcy1v-y1qdI6EMPj6jbdu21mhfLZvPd5bF4dJZWOFZ6RJYfhfnVdlNNDnDmKVj_7bG0vk-gEeLBtfGsdPQDEGfGaIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ درباره قطعنامه اختیارات جنگ:
دیروز، در یک رأی‌گیری بی‌معنی، مجلس با ۴ جمهوری‌خواه بد و همه دموکرات‌ها، اختیارات جنگ من را محدود کرد، درست در میانه مذاکرات نهایی من برای پایان دادن به جنگ با جمهوری اسلامی ایران. چه کسی چنین کار غیرمیهن‌پرستانه‌ای انجام می‌دهد؟
🔴
آنها می‌دانند مذاکرات در چه مرحله‌ای است. دموکرات‌ها با سندرم اختلال ترامپ سوخت‌رسانی می‌شوند. آنها ترجیح می‌دهند کشور ما شکست بخورد تا اینکه من یکی دیگر از پیروزی‌های متعددم را کسب کنم.
🔴
چهار جمهوری‌خواه، داستانی کاملاً متفاوت است - آنها فقط نمایش‌گر هستند! آنها باید از خودشان شرمنده باشند. ماگا!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125041" target="_blank">📅 14:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125040">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X52UjX8Uj8yMvhz47YeoPkXgOWMnEXks2wKz4lzOVkxzh0PWvr4owJTZJT8xmxyOOZd4wu-XgUY66aou9rIxpxO6ce2HwqNaLQ2FgzSjqdw8GG8ZWNZJm8WbwLJrJ1_us7AFrhhVbOirVYffBSVqoNGFdZo0ASLATJeHnUnW-iSdCvSTur-KjKkGZ70R6mkPJarYPCWFk3M8rNqaS3h3YrMhcKAVAC7X5Jw66XHUOOKoEP0sYEKf-FgDCMCiyrhvFtQo97gV4a2K6itW1Qj7yRC7U2ZaR4i1VdRk2X5niLdsoE_ENWIE0SCoWfRZloTQr_T2uig0TW918s24KBMI4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فارین پالیسی: جایگاه متمایز آمریکا، چین، روسیه و بریتانیا در صحنه جهانی
🔴
نشریه فارین پالیسی در تحلیلی به قلم برندن سیمز استدلال می‌کند که اگرچه ایالات متحده و چین از نظر اقتصادی و نظامی بسیار جلوتر از روسیه و بریتانیا هستند، اما هر چهار کشور دارای ویژگی‌هایی هستند که آنها را از رده بعدی بازیگران اصلی در صحنه جهانی متمایز می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125040" target="_blank">📅 14:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125039">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7vkqkslq4sD6OMKFExsWOLQpY_RE1Zf4RmEcVjtm2_GQ-Qb96W9HwUw3pG3MKSAT4MvHOPgWCNUjYlTFZcDpbCt22p6D9l5r404zdnrl3rOT8430OWQvcGtusMtLZUAmhtgHp_jpN8UGQ9eeR2toTt3rrDAKvcqOtnOFHP0h5Mktwt3J6vehoay2rgT403W_z624ukCVLoM4IqYh58jrEPFDHDrRKyUgNltZIzlLb6rP4Nnfvn6kxXqqIpHaFuBby4K-xZLUcf5fKUB0MV593c-ZA52UEYTlePvaXfwuC3izg-PgEej0PIMtaj8ubthFdLPOpqk5Ofi9Xz5MFku1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش نشنال اینترست: استفاده ایران از موشک چینی برای سرنگونی جنگنده آمریکایی
🔴
نشریه نشنال اینترست گزارش داده است که به نظر می‌رسد چین سخت‌افزار نظامی در اختیار ایران قرار داده و ایران در جریان عملیات «خشم حماسی» از یک موشک چینی برای سرنگونی یک فروند جنگنده F-15E Strike Eagle آمریکایی استفاده کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/125039" target="_blank">📅 14:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125038">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
چت جی‌پی‌تی، دیپ‌سیک و گراک بدون فیلترشکن در دسترس قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125038" target="_blank">📅 14:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125037">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
تسنیم: پرتاب پهپادهای هوافضای سپاه به سوی اهداف آمریکایی در کویت، در نیمه شب و اصابت هم در نیمه شب (و در تاریکی هوا) صورت گرفته است درحالی که در فیلم و عکسهای ادعایی که از پهپاد در فرودگاه منتشر شده، هوا کاملاً روشن و مربوط به روز است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125037" target="_blank">📅 14:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125036">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAXAqfSXSiV7_P0cM6USkak7U9FR0MKXAf6rzlWii5Mo9dfRoZ3SAiZ9Kd19KSYKeY758q79FJTMxwAjFQYgMH-Q6AX5DyMq63-7xtdqrn3Q-YCpe5YwguIQN7PyvoxKEUKT3rIUR6Ku9u-_LvdsqspoVlqNguZ81vYEusC5nUmyP9BZ-ITcQ9neygskY7rpU6X9nbpdQADuXPxqJdHxkUiaK7jTBVa6jH1368JbQAbiejcSU65oqgsp6_bT9qC2EOSp2ZwnWqp2ESl-gYyHv8nKnL5OJzo0YwFcvPGj0fo7_9XmM9qPK0vXoX_0mr8w7QEQdISk2Ungqp77gFwM0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125036" target="_blank">📅 14:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125035">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
نخست‌وزیر آلبانی، ادی راما، در برنامه CNN با ایسا سوارس درباره تنش‌های پروژه پیشنهادی جرد کوشنر برای یک مجتمع لوکس ۴ میلیارد دلاری در خط ساحلی محافظت‌شده آدریاتیک به شدت واکنش نشان داد و گفت «هنوز پروژه‌ای وجود ندارد»، و گزارش‌های منتشر شده را به عنوان اخبار جعلی رد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125035" target="_blank">📅 14:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125034">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDoB1RaRJgjtqvOgulExO6smSdgcoecMjA4Wz7hDUI7Ub_S-WQbwxwSIeH9kSAdS6TMw-SDHOpALrpy_DqUvzuLQ4Bhse6rWksXoJIyjtKhxpOXwMRnr_9P_Hwp34GP78mCDa_0JJdHI3DL5vy0x-lexrGNh2czzm0QwFBvN-2wBmhm8Ybye4-CHoGvZMp9oPM2daqNiIkSGQd0CFnBsQpIiKt-k5rhag6kaVC0OyIofdhtOzrd04PRDm87e1C1S3jlEh1N3rjiGVryKE3XJR6g6uZSvSPSPweGeitAiSoQ2G2t67DFuYFq2QCJQLx_zhBFcP6bxyL7Kbj0jI_x3EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار قاآنی: اسرائیل باید به نقطه قبل از شروع جنگ ۴۰ روزه عقب‌نشینی کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125034" target="_blank">📅 14:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125033">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
اکسیوس :  یک شکاف رو به رشد بین ترامپ و نتانیاهو در مورد آینده منطقه در حال شکل‌گیری است.
🔴
بر اساس گفته مقامات آمریکایی، ترامپ می‌خواهد تنش‌ها را کاهش دهد، درگیری‌های جاری را پایان دهد و به دنبال یک توافق دیپلماتیک با ایران باشد.
🔴
در مقابل، نتانیاهو به نظر می‌رسد تمایل بیشتری به حفظ فشار نظامی بر ایران و متحدانش، از جمله حزب‌الله، دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125033" target="_blank">📅 14:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125032">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=f349vRfxNl-pBZ8vOc5XrkZrpkH-uMAkqUpt2J7xa8gdVSFLfrBR74lFK10ln0U6i6CvnHIZnQLedBsK9JaZc4pShzPdSUTcQCJWuSh-jMcNCG84EDu5ATcMyWzrUovHTt-jKQWKSHOAjWCOeJQjhBT5I1ue8UY_SJxixmoh3qp3tgPMDokZ36wGKy0hzM01rycceJwlkMHxZvetp7HviEFHEQx0oDxN7k2Gn-E0Atz5QfBJDENLQ_RJLPZxPzxHZZb5HdPzP9bLkEewzyNSDZWh36Y3SNH-23y5HqYQEZrf8riXl3RFe-LJXorL0diEhS2i56kNfpSq8T81mqwUNzsP6VisQndWvzAjV1atJzW9Tbmj0WE_1MXFA38M4_PdiTgsuMOjr02lLNy0TUgsF34CeeZ8X3ctY1GsciZTOL0c4Hgv66VNP15Nyr1vufZ7acb_oQCpAhhyYOZMwzlRDrgsZ0fIiK7y9hzOv1btf9_AASbhYp6N_QAGCBt51O8ROrBEW0zUp8B6iciotqgccF_wS0TKm9CmzUJ3repO3bv9Nf35fTH98JAf-E6PgfdzC1Va7axXS5oM_sBtu-SuR9V78DHANFArMhIklo-UzfF32his7btab32Rrv2CP9PpW4ACaTtHnWcxDt2m96l6lz_3quWyS7L8ErH_JoUB8QY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fad04c34.mp4?token=f349vRfxNl-pBZ8vOc5XrkZrpkH-uMAkqUpt2J7xa8gdVSFLfrBR74lFK10ln0U6i6CvnHIZnQLedBsK9JaZc4pShzPdSUTcQCJWuSh-jMcNCG84EDu5ATcMyWzrUovHTt-jKQWKSHOAjWCOeJQjhBT5I1ue8UY_SJxixmoh3qp3tgPMDokZ36wGKy0hzM01rycceJwlkMHxZvetp7HviEFHEQx0oDxN7k2Gn-E0Atz5QfBJDENLQ_RJLPZxPzxHZZb5HdPzP9bLkEewzyNSDZWh36Y3SNH-23y5HqYQEZrf8riXl3RFe-LJXorL0diEhS2i56kNfpSq8T81mqwUNzsP6VisQndWvzAjV1atJzW9Tbmj0WE_1MXFA38M4_PdiTgsuMOjr02lLNy0TUgsF34CeeZ8X3ctY1GsciZTOL0c4Hgv66VNP15Nyr1vufZ7acb_oQCpAhhyYOZMwzlRDrgsZ0fIiK7y9hzOv1btf9_AASbhYp6N_QAGCBt51O8ROrBEW0zUp8B6iciotqgccF_wS0TKm9CmzUJ3repO3bv9Nf35fTH98JAf-E6PgfdzC1Va7axXS5oM_sBtu-SuR9V78DHANFArMhIklo-UzfF32his7btab32Rrv2CP9PpW4ACaTtHnWcxDt2m96l6lz_3quWyS7L8ErH_JoUB8QY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم جدیدی از حمله هوایی آمریکا و اسرائیل به پل B1 در کرج
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125032" target="_blank">📅 13:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125031">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
سفیر آمریکا در اسرائیل : لبنان و اسرائیل بر سر لزوم توقف کشتار اسرائیلی‌ها توسط حزب‌الله و عقب‌نشینی از جنوب این کشور به توافق رسیده‌اند.
🔴
لبنان و اسرائیل توافق کرده‌اند که ایران هیچ نقشی در تعیین آینده هیچ یک از طرفین ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/125031" target="_blank">📅 13:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125030">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
آموزش و پرورش: اعلام برنامه امتحانات نهایی کذب است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125030" target="_blank">📅 13:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125029">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
شبکه ۱۴ اسرائیل : کابینه امنیتی اسرائیل امشب جلسه تشکیل میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125029" target="_blank">📅 13:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125028">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
آکسیوس به نقل از دو مقام ارشد آمریکایی: در حالی که ترامپ می‌خواهد جنگ در لبنان را پایان دهد، به نظر می‌رسد نتانیاهو می‌خواهد آن را از سر بگیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125028" target="_blank">📅 13:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125027">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ادعای العربیه: مذاکرات پیرامون دستیابی به توافق برای آزادسازی بخشی از دارایی‌های مسدود شده ایران به مراحل پایانی خود نزدیک شده
🔴
رایزنی‌های فشرده درباره نحوه و سازوکار آزادشدن این دارایی‌ها همچنان ادامه دارد
🔴
اصلی‌ترین گره و مانع کنونی در مسیر مذاکرات، به سازوکار و چگونگی مدیریت و استفاده از این اموال آزاد شده بازمی‌گردد
🔴
پیشنهادی مبنی بر تشکیل یک «صندوق ویژه» جهت واریز و نگهداری دارایی‌های آزاد شده ایران تحت نظارت مشخص، روی میز مذاکره قرار گرفته و در حال بررسی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125027" target="_blank">📅 13:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125024">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BDlxd5-QetsSRM43O4Dh8eR4KVw6PmgA_bX1shr9Vr3L30R7nXIzmTY5u0unEUa7GJu_aiFKZgutv7cGf6CP9SW7A7_RPEB7-tHXVe6py6_y6tRiKNbu8xMlHvamRRiKPzPJapQLp6nPQfKBTWMkAmzJdSmXff79m8wW61RkGRbCrYuL2o2lgv7zUBHLPd4ry6DWSy05IjOf_6HqhV20pH-nMfGAKlxQNd0hWtiEyUUaeRXsmbx4WgdXbfSvXSRZvLBeTD6r5RZWLcWI7WPli0InxTZ1eBAY7e63k4zP9PKigJef_kLWIQJc6UL_0K5sbz3pfUl5xjcRqnymow4HFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P8KiavCvxTbMEWvtsi-HRJeDkl7ox3TFFe_su1gKYTg4OlJUDnyT8TdWS2oyIqBEQdJZohDzyL8z4SuhHnHiW3p-90uUIWDcY2A8EBBwT1pKETz-mCvlm3xPDYHSleSBEATLaG4SyCgVqByAMPNnQkgDq9tUyYYjCBPaUOfs9eXQrg17hrc5O7vQZJB6n-1khV0TKjUyhWBjbu4gCePA9KMGFsPO15RXOpuklaNhZeCnJCOfAh53e7Ff5wFLhhsDi5Z0bNyWR3E58gvUBUiOVqzzlLGunCHqoRQEwOPKSypx5BcR7js-oFcNF10y5BdzqrK0xtORxZiSkAmIppew1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WdXXqbbk0FOoeOUkaH8ub0kA3XtofTQ2-sn4nblswvR5qzx5ncjJn5lfdtKBhg62qrXaxkIrIS7DVmdZa1JAMIj7_o8Frt9tFd7RJM1S4thtcJCQr83wAjMyd54iBKGy_gVh0nynNCrKlJ2hfLJv2V2SysDYMJFEoWsOGxKgEAzudNRTSlNzrX6OSex16ObhBejaIWdlRW8s2jRDp2ts7s8qbbEFupQ6RTqyPJsf30In_U-v5-0hMnAPoI1_RJHQEp592DLaCvGC6nFhS2Q_A0s6xjraT2lwixOSOZ0hiR5I3kII8axbF92UVaVeciucOo_nf6Sp9x01esoZCEVPqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملات هوایی به تبنین و نبطیه الفوقا در جنوب لبنان انجام داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125024" target="_blank">📅 13:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125020">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75bd8285ce.mp4?token=MsP4i1xDKfa7JlWGh6R5svvM7TIFB9gOqIwGgDugeI1fiWWjptQth_yhktWak54fd-DB88SiHjCX1HOyQqpWoD2lUxpSxz6M2GCegbe7UI6nE08TIcH2NYQ7H0bVHw97TxGbCC0Qu34-IcPGh39ZWXWXxQAWlwsxqRKhU8gwWa0yrs7lUVynzvRDJCCWOqRIOy8jkELX8UJF6-x8ttTC7X8DKfnzIvMGKlmxngVqtqm4SXXaBd1UH_LsFP2bAdopsBTCTTmKwJUNmIngfx_eF3QtQAs8PmCuO2d5qAIVYhU1kUBluXVRY41Z3besJeYZEJyboP5_AEd8QdBySh9vGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75bd8285ce.mp4?token=MsP4i1xDKfa7JlWGh6R5svvM7TIFB9gOqIwGgDugeI1fiWWjptQth_yhktWak54fd-DB88SiHjCX1HOyQqpWoD2lUxpSxz6M2GCegbe7UI6nE08TIcH2NYQ7H0bVHw97TxGbCC0Qu34-IcPGh39ZWXWXxQAWlwsxqRKhU8gwWa0yrs7lUVynzvRDJCCWOqRIOy8jkELX8UJF6-x8ttTC7X8DKfnzIvMGKlmxngVqtqm4SXXaBd1UH_LsFP2bAdopsBTCTTmKwJUNmIngfx_eF3QtQAs8PmCuO2d5qAIVYhU1kUBluXVRY41Z3besJeYZEJyboP5_AEd8QdBySh9vGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری‌ها بین نیروهای دولت فدرال و واحدهای امنیتی وفادار به رئیس‌جمهور حسن شیخ محمود و نخست‌وزیر سابق حسن علی خیر در طول شب در موگادیشو، سومالی ادامه داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125020" target="_blank">📅 13:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125019">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
فارس: فعلا آقا رو دفن نمیکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125019" target="_blank">📅 12:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125018">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رادیوی ارتش اسرائیل: نتانیاهو دیروز یک جلسه امنیتی محدود برگزار کرد که در آن ارتش طرحی را برای یک عملیات نظامی گسترده در لبنان ارائه داد.
🔴
در حالی که کاتس و بن گویر از اجرای این عملیات حمایت کردند، نتانیاهو به دلیل فشارهای آمریکایی نسبت به آن محافظه‌کاری نشان داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125018" target="_blank">📅 12:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125016">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf769954a5.mp4?token=ajEQD1OXB9AirS1vStlU0VIwLOekEyB8caqrBYBeZX_twY6hufroyPMTZbotpVXmhSJA0XEggZPw5AiNacwaQkbDoSK8Nm19DwK6xpWw_0AA4Xjz90zJcS-_4qk2NUhc4mGIShQ2DQb9lJ3P3szdT26PcObT9OBiel3rIuE1ljs3meEYz5JhxbovlaI_JBaIlDm5HkIR2lYm59vHFShipWYg_IBuDHH0Ixiz-Kj23aiKFDhfwykPDwd3RgwZYHigmIVcB2Df9nwkPD7GwYtwhor1ods3KkCsYf71uNJNGoAtiVJyYslVSJ3eXCUXyo3dtCSro7srTzJeYZIHAPuRWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf769954a5.mp4?token=ajEQD1OXB9AirS1vStlU0VIwLOekEyB8caqrBYBeZX_twY6hufroyPMTZbotpVXmhSJA0XEggZPw5AiNacwaQkbDoSK8Nm19DwK6xpWw_0AA4Xjz90zJcS-_4qk2NUhc4mGIShQ2DQb9lJ3P3szdT26PcObT9OBiel3rIuE1ljs3meEYz5JhxbovlaI_JBaIlDm5HkIR2lYm59vHFShipWYg_IBuDHH0Ixiz-Kj23aiKFDhfwykPDwd3RgwZYHigmIVcB2Df9nwkPD7GwYtwhor1ods3KkCsYf71uNJNGoAtiVJyYslVSJ3eXCUXyo3dtCSro7srTzJeYZIHAPuRWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور جان فتترمن: من همیشه به هر چیزی که اسرائیل نیاز داشته باشد، چه نظامی، مالی یا اطلاعاتی، رای خواهم داد.
🔴
می‌دانید، آنها یک معجزه هستند و نمونه‌ای از دموکراسی و ارزش‌هایی هستند که ما در کشورمان و در کل آن منطقه زندگی می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125016" target="_blank">📅 12:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125015">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی اتمی (IAEA):
آژانس بین‌المللی انرژی اتمی توسط نیروگاه هسته‌ای زاپوریژژیا (ZNPP) مطلع شده است که نیروگاه حرارتی زاپوریژژیا (ZTPP) که سوییچ‌یارد آن به تأمین برق ZNPP کمک می‌کند، امروز صبح تحت حمله سنگینی قرار گرفته است.
🔴
تیم آژانس در ZNPP دود کم‌نوری را از سمت ZTPP مشاهده کرده و صدای فعالیت‌های نظامی را شنیده است.
🔴
فعلاً خط برق هنوز متصل است. کارکنان ZTPP به دلیل حمله در حال پناه‌گیری هستند، طبق اطلاعات موجود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125015" target="_blank">📅 12:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125012">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RBiaM53VIgtU8liz9VZrco4mz-akCZijg_sIMZDfCycWHiz5H6Zi-A_uy2495LDx5wh91ebOSSDaPhISJ_wADxzRj9-Ud7TLHiP-HcoLNmR467IjiATUKrecsgZL_kaskJ0NsjnM4ITUky-P1SFFeYqFwudnSWFohJUhu8kaQDUCLrngxmTvhC6KSGLcVqeiKYQllRBwzXenpBQLTH1VFqRr11USjCcan8Q1t-ZCmrQXE1N2I-3kBLpoR8k4m8oEzKO8hUHPh6QdRa0OsU7MxBWHjsGouW4F4cGS3TmmdhOPaOa00FP2zdxJUammqfVm0Nm1T7lWe1anKry3NtfzEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWL0JIPak0KVouGZKR7CV7Oiry9iLi8iq6avF9YQlzuSUNIf5WNTMLg_Z2KqPOiftkyxm_AxqnR6sTqFUMytSD5UsHxtHNND8vdF5JYt6xRf65PIv7O4DCskyZsj5ZxvQw-3y6gxZNYfX_M9aTc0Ol17_z1VLcHK2z5eyvg0YVpHmduuPzNrEyhiLKqoEbQG7XIafE5R4UYGNWQ0Csw13IXw8xcFVkzm-aa3k7wCrece13m4hFPo9sGEJwkZKuUV0iBFvNV9VthPHINSSA02eWzWra0VQk05dB2h6vvY4v-pV0v2dMW5IcVpr9ZfiNIbsU_j-b2i2V7Z0oxpLwic2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K1sfOwdarA1ux5tXkQh5Tg2RXsVZ_s_fa4ea7TTYbpBhWDkUN4ErK9bQLoAUM3b5RHNJ5AZaEkbzxfH2pibaoB0gyXE76itOeWOqWkLru3JdtxNXaNZerkNntekstMv09I8UYB-pH14k1Gn32hh_4LZIBIQukoqVZmHyUsT6mxOOjbPOWoYXDY5ADmpW5wlzL3pXVcTTH02AQLvVSedinlear0PEvXiVAoNDMChMa5AypiUZuq6QTnRDI-r8uFX0iRsBPgMPZwDUokWTlTnaOg8Shtn-i121zx-hvKPfBDZeGmbS9j9tl3ByiHJzLkD4zSGAM3DleEHMkya0wALL-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی همچنان جنوب لبنان را بمباران می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125012" target="_blank">📅 12:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125011">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
رادیوی ارتش اسرائیل: پهپادی که حزب‌الله پرتاب کرده بود، لحظاتی پس از پیاده شدن «رافی میلولو» فرمانده فرماندهی شمالی ارتش از خودرویش، در آن خودرو منفجر شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125011" target="_blank">📅 12:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125010">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
نیروهای دفاعی اسرائیل هشدار تخلیه خود را به همه ساکنان جنوب لبنان مجدداً اعلام کرده و از آنها خواسته‌اند که به شمال رودخانه زهرانی تخلیه کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125010" target="_blank">📅 12:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125009">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
گویا اسپاتیفای رفع فیلتر شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125009" target="_blank">📅 12:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125008">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
شبکه عبری کان: پهپاد حزب‌الله به خودروی فرمانده فرماندهی شمال ارتش اسرائیل اصابت زد
🔴
یک پهپاد حزب‌الله به خودروی فرمانده فرماندهی شمال ارتش در جنوب لبنان اصابت زده است بدون اینکه تلفاتی در پی داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125008" target="_blank">📅 12:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125007">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
منبع مطلع به العربیه:  ترامپ به واسطه‌ها اعلام کرده که پیش از امضای توافق، با آزادسازی پول‌ها به ایران مخالف است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125007" target="_blank">📅 12:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125006">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/alonews/125006" target="_blank">📅 12:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125005">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JCk3UngcX5CaWkWL1yTw7JMuCrYdOdOkobkPS6BvwgDBjNetFAUsnlcAx7dviIa00pEtGj45sGnGBVLFC-rFsRKLkflQpMKX2OlYhtEq2LNVxD2SR0Wkt7toSccQXLfr0EpwsL67ZWwrFzjKuBwH2B-SGolbEoeBiopIFsCVC2Ale5LzQGq8SL22w_DTBgH9W1ME6u5kcgSBHglwicdKPmvYuNREoP0zYS_j_SaK9mS2AS8POccvlgYxbp4mXet_DzNQYFRQvN6Vv5uZTjP_XqEWNyhnJVnV4lIXLk5xd0ob8nuKAgikQjqCYYd68vx6AV-ctyO24J6bYubwx94mbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤚
اینترنت مخصوص جنگ
🚀
💙
🔥
نامحدود فقط 690 تومن
🔥
⭐️
فقط گیگی 7 هزار تومان
😍
✅
بدون قطعی‌های آزاردهنده
✅
سرعت بالا حتی ساعات شلوغ
✅
مناسب تلگرام، اینستاگرام و یوتیوب
✅
همراه با ساب
✅
تعداد محدود با این قیمت
🤖
@NetAazaadBot
🤖
@NetAazaadBot</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/125005" target="_blank">📅 12:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125004">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euvh3u6zyyUikAvJcWesA--9RsbligheSXwke4_7Y__7JZa-goOCkyQX_kW5Ny8DXd_-9hXrY6OyLtzWLZB-Xoc4UGTr8L2OhBRlVvblhJJ1kqGhauxht8wmgpf8_Z1DFjNcZb2IeJqcMPwC1sbgMLA0gohYlAo6AIqvdqkoviMo2okssMZXjipDLIuMJBuV7la1YWwH6FLeDVxw02FXOLgMKZQpbXKSzoxOJLbYq0J0duUpVBLwSHNRqUL8tcDvlSd91lBF3E8tMT2WGqr_Ys8eungbNcLjRiMNCPimvY5WJp4gOHMkM-AH9AzzBYNcqW2FKUXmxtdRJ7uVpLBYnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره ای از ناوچه Boykiy نیروی دریایی روسیه پس از حمله پهپادی روز گذشته اوکراین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125004" target="_blank">📅 12:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125003">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIirYpRTz57dSgfGfUl96Mc-xD80A2eT5xH3TWNHBmIOGfrjJg8-qQUenz8CEAyrtBORLP8FfUmHPuKmZE5ZBD77jhAFtF0R6YzzfC8GtZ-q_-yi1am9UdTBUqkzU0BUDIFK7uW_j1_zOYYGgP1CaHywJUg4gSXY-tGIA4L868_sl88JxMU1erjagNm_MFjuuHsMEKIj5mybQw1-dq0RKQjXcXj4ta1X2B-6gCBUEHzJkBk6QjN-UZE4E7geJ13rETB1kP_WNr9173ORKxC0TvF8xZRmBzI8cG5rQZhi07-H0LEgXUJYDalfbSf_rkOWN3GOoO5jqddtw7qwIGUjLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جروزالم پست: سرهنگ دوم آویخای ادرعی می‌گوید ارتش اسرائیل اولین هشدار تخلیه در جنوب لبنان را از زمان اعلام آتش‌بس توسط ترامپ صادر کرده و تأسیسات حزب‌الله را هدف قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125003" target="_blank">📅 12:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125002">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ: ترجیح می‌دهم آتش‌بس در لبنان را از «مشکل بزرگ‌تر ایران» جدا کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/alonews/125002" target="_blank">📅 11:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125001">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
مجتبی خامنه ای :  نظام سلطه پایگاه نظامی به نام «اسرائیل» ایجاد کرد و ایران از موضع خود در قبال «اسرائیل» عقب‌نشینی نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/125001" target="_blank">📅 11:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125000">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jck4OhJvEl5UEOb8z4iAGwEoBHnBwXlw6Ool_3rTiaUpSSoWN8AmfW-4eRTvxwYjzak2-rBWwW1ikImUqS2axdWv6ZdKCnuI8B0wKwDorZ8uWRKkIWq76sVjJcVLl99VYdODlG6UVqlNPfLisImXNQcHYrCQNkaNqQIvm_FQ46FByDCAgNaMiQ1qUgz0ep8eR2lS-q6yyg9Czs9EUMUWoBtgCuekYjyWOWzUzrqjgmE6IYArIjfZHsgvu2M4f3qqpzl97PDGU7BwpxAUuqvNtQO-XFOdrN6GR4oyb9c8_QXmhlv6hZj5j3PmKLwGNl8cTBrONQW8o7xFsGZO-MmE-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۱۴ خرداد؛ سالگرد درگذشت روح‌الله خمینی، بنیان‌گذار جمهوری اسلامی هست
🔴
وی در اولین سخنرانی خود بعد انقلاب گفته بود که شما را به مقام انسانیت میرسانیم
نظرتون؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/125000" target="_blank">📅 11:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124998">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rDEpdY9jgdEbAduncMv2OidWOBfXTRVEsHVRnKZmtO40VbU0dB0YJzDRjsQciVQPsEicBu9-hkFGpe1VoATYWmvArziimqGc69UR23Bqo6LKDehpjsljzFoThemIqeLhOQcH-Tqy2TiwXqi_5QLFiVgsPEk1-yQSwuCZVO-9RcEs1Eetw-P_qHcDElicOwg6VUbwmBOqIMENgFypRRcptqeHBIGX-o6ADTUVcuZWwf7sozSM1R-TDJr3JWXGBLYJU40HukaaxhzTcOzr4-Z4zZLS_89SfaSo6YBjcSwAt5G34jVfU_AO-SmQnMeRIxT1g2NgPFJyJGZXpt40AWV76g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dSVpyLWa8Hpd8P70rpYsz8Md-CyaiKwLNoGgZ8fpqAPcDB7SYtLhDsjYrgLGGwgqSXduH0YkD_JtpTzv0_A7k8CzYQM9DDQQ6YYyoUDXhUkQUfO5qZCmptbGBg6tmn4A2kUCALPMAFqXDqPApW1mZ-qZl2Ms3C1emyIWwKJQcJD3ZNN-GriyNplMR4AoCCVB3klwIZAXOpMYOCeMJk1vwnPneGlBMyDHqaMJZ-wEN8LqSnNtrDftfKi8OEghlg56Qe5bCV_OjH3sSwLhjR_3LRhTcTOLmcM_ekhkYDrMVDT_Zb1n-CcTlERszSDdcwmZMKMH2ocpQjnzcpTqRqM_9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی به حملات هوایی در سراسر جنوب لبنان ادامه می‌دهند.
🔴
عکس‌ها از زواتر الشرقیه و المنصوریه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/124998" target="_blank">📅 11:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124997">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBvToZka2a8PWmPZOT9uDtgolXdh0RJP-HFbO5d3LOOz1DF8DSEzm7Wfu82ceS8n_PAArn4BNLNjeBPYDLsIObnclxdJsWZ8WgzOBz3R1vr7Y_g3i62M1tfBgwiHpOQuWEbGBRwSueLCzPOT5KerN6byswhnPxjF1nW5cTwBOzZ4TwTJv6hZvzk9h0RGVQwBrMhhTE2gKPAMYwmQlz0CX2BQSPcyj0F-RD5jR6cgtnv_dzM_ZuedjoDE1ZxP41b6NrFlG8a8Tb91ijvBVX68iHi9kLCiRFejrotog_lBie7mjf_D64wMBtGFxDHCdUrFEzC3MpdjHbc5reDdr3DOLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدیرعامل شرکت «ایران تک»، جمشید قمی ۶۳ ساله اهل نیوپورت بیچ، به اتهام تأمین تجهیزات آمریکایی برای تأسیسات هسته‌ای و نظامی ایران بازداشت شده است.
🔴
نخستین تصاویر مربوط به بازداشت او در آمریکا منتشر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/alonews/124997" target="_blank">📅 11:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124996">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزارت خارجه پاکستان: روند مذاکرات میان ایران و آمریکا ادامه دارد.
🔴
هرگونه افشای اطلاعات درباره ایران به آمریکا در سفر اخیر وزیر خارجه پاکستان به واشنگتن صحت ندارد.
🔴
در جریان این گفت‌و‌گو هیچ اطلاعاتی به اشتراک گذاشته نشده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/alonews/124996" target="_blank">📅 11:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124995">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
در ادامه موج بازداشت‌ها در شهرداری و شورای شهر سقز، یکی از اعضای شورا و یک کارمند شهرداری به اتهام فساد مالی دستگیر شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/124995" target="_blank">📅 11:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124994">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVhlaLqTH30gj8q66nxA5I-JMx7Wc8IFfHJWDrJ7e1g6GqiiitFnSf6nS9a9QTLTT95lgySeQyk18yBLhaVRZamwjA57JIHWO8RQ6RWKJ9115baD7Yy2MzaskGcnZ655oOwdsilx7sIydNDyV8KAmwE8pD0WfD0l1Dge5GwtrJB7Nm265T-SkRSf-FdiPSAYMUVv5OZiyj93DLoTN5NNcteWdvv0EzZqztR4WTF4lcwa9OmFvha_7NLiu4WspiQdxpJVfEns_HG-uidrnBpdzotiH6bNti_xAsOMskQXuhqgYn6y6qcGKlRXThdSiLLWv5llnz5ISoC_dAsDuFPi8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله به پزشکیان و قالیباف در تجمعات شبانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/alonews/124994" target="_blank">📅 11:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124993">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
کیم جونگ اون به رسانه‌های دولتی کره شمالی گفت که قصد دارد «نیروهای هسته‌ای کشورمان را با سرعتی تصاعدی تقویت کند» و اینکه آنها ظرفیت خود را برای تولید مواد هسته‌ای با درجه تسلیحاتی در پنج سال گذشته دو برابر کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/alonews/124993" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124992">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
مجتبی خامنه‌ای: هدف دشمن اینه فشار اقتصادی بیاره تا مردم ناامید بشن، مردم باید مقاومت کنن تا به قله برسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/124992" target="_blank">📅 11:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124991">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bedf43656.mp4?token=mIbtkaseYud48q3TWzh8GSEsxKpi9i-26aJYHdy66VEVnCchVkA061-KAS8dLWF_WIerQ3-UwrOP0P8NyEz_mjPp_KiH2V7-dS9OUKNIyLXYYLmaBxIqDhD0x3T7-2aNwQp1a6xGDBrKWeu2ppUiF16cbrbcsIqGn6GlFcZVr24ptUDdUUgiXcKgl2Wgcq3Swix3HopihpL2QSozgh_R3oZGLwDmqL8-MP_G1JZYcMddkHE-R3iChaxpcY3A2KkT1-FCYxEN6E3Yy6DR7m_L8omva9C6UC4cA3_64cl71DHg75Ur9mVag3kaEEVRrQFwKy4APU5Rf70c_assK8wP0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bedf43656.mp4?token=mIbtkaseYud48q3TWzh8GSEsxKpi9i-26aJYHdy66VEVnCchVkA061-KAS8dLWF_WIerQ3-UwrOP0P8NyEz_mjPp_KiH2V7-dS9OUKNIyLXYYLmaBxIqDhD0x3T7-2aNwQp1a6xGDBrKWeu2ppUiF16cbrbcsIqGn6GlFcZVr24ptUDdUUgiXcKgl2Wgcq3Swix3HopihpL2QSozgh_R3oZGLwDmqL8-MP_G1JZYcMddkHE-R3iChaxpcY3A2KkT1-FCYxEN6E3Yy6DR7m_L8omva9C6UC4cA3_64cl71DHg75Ur9mVag3kaEEVRrQFwKy4APU5Rf70c_assK8wP0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از پرواز پهپاد پنهانکار RA-01 اسرائیل در آسمان تهران
🔴
پهپاد RA-01 یک پهپاد شناسایی-رزمی پنهانکار اسرائیلی است که برای ماموریت‌های اطلاعاتی، نظارتی و حمله استفاده می‌شود.
🔴
ویدیو مربوط به زمان جنگ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/124991" target="_blank">📅 11:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124990">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ارتش اسرائیل می‌گوید درگیری‌ها در جنوب لبنان ادامه دارد و به ساکنان لبنانی هشدار می‌دهد که به سمت جنوب حرکت نکنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124990" target="_blank">📅 11:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124989">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVeYtYLz4Uvtf8xULmnUZXmHtBZ9DefXWMweA5W6URL97B5COZiXp69RRiVE6L6QLMb0dc75SDrFMMa-4HY8gdvfRmuIk5sO-GrsbWdym8FM6Lk51vSQSIx08hZdUy8X43x1YHh8ibQVezzoM8mi9K7zW05DSc4vBeuVZ2cbwFeg5vf3A9VB4LAy8qaonbBkRBZBoyh6Vkje9tk8VjEjwCIBvdpiCjMD_B5Fgr1y_8zY9wpgJIuzboBAapNys-dxwD-VyrCB62OUImBNoK-GUpKdGW13ReagUdh9ZnsvH4-EaFvrJSfLhFv_uZuwEuvNNqrhTCZAcnfEAoAGqd2a2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موتور پهپاد شاهدی که به فرودگاه کویت برخورد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/124989" target="_blank">📅 11:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124988">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WAAZ_eZmjcNKQoQmziatfuutV492ygKF7z31WJMalmzBcnFu44-V3vWnvPEPSErnoxSE3dvFo1uDtS_4gHib_6LME0cpJkYXVFsp-tfiZ_xKDUQQadRYKRVUzQSZygbSY51VPWwTThjGwWWitUIfdwON7kEaSPdX51EBTcKf_AbVPPCuGTbUintF28c5fO8bfmUvssEhtT-_5c9tLIrNO7hQkZv7CJmlNcsiL_DD93VeMSISDxxd5PsqCkmbGvhkU4Vz2a5-PM8u7SDZ57NA8_5J7CKCW6XUo2AAuWj1FDS_iGt1oHO2_Mehuhd68gk7Y5UyzFZi5Fm8tmyHlSMkZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای Falcon 900EX متعلق به دولت ایران در حال پرواز بر فراز دریای خزر به سمت روسیه است. این هواپیمای خاص توسط مقامات ارشد ایرانی استفاده می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/124988" target="_blank">📅 11:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124987">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca1e1a949.mp4?token=cZHgeXME5cNIjK0u0j30EhG0Wn0sxBEtBtJ86yy8ZlCBCPHzwNvxWUDYRVlvI7QbVhxILpdzZvUW3Cq0JTk8zvNLR2O9t8cMeQmOmNbnVZ0-3ZFcsrunaGWIQHpo6l50Bwv1v6CYw6AfyY9R5k33u6QUcmrOX2C2r6FRrQb1jl3DOJTsx-swNCMsS0xlpfGg_hjQnTSBa0DfkTkD60vXIJZvbaUhVPOXKWFWOr0Q3E6Eu45ZNlu5-3aSMP9P7OETWLfbjP0oJVGQiOgWMEqjXkiztNKgYCVbOJnvokAC2mX3iMceE6iiVRwdM5G4dyZiZYFP1pn_FrhyhnVos_q3UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca1e1a949.mp4?token=cZHgeXME5cNIjK0u0j30EhG0Wn0sxBEtBtJ86yy8ZlCBCPHzwNvxWUDYRVlvI7QbVhxILpdzZvUW3Cq0JTk8zvNLR2O9t8cMeQmOmNbnVZ0-3ZFcsrunaGWIQHpo6l50Bwv1v6CYw6AfyY9R5k33u6QUcmrOX2C2r6FRrQb1jl3DOJTsx-swNCMsS0xlpfGg_hjQnTSBa0DfkTkD60vXIJZvbaUhVPOXKWFWOr0Q3E6Eu45ZNlu5-3aSMP9P7OETWLfbjP0oJVGQiOgWMEqjXkiztNKgYCVbOJnvokAC2mX3iMceE6iiVRwdM5G4dyZiZYFP1pn_FrhyhnVos_q3UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی جدید از حمله آمریکا/اسرائیل به آزادراه بروجرد - خرم‌آباد در طول جنگ اخیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/124987" target="_blank">📅 11:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124986">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
هشدار هواشناسی برای مسافران شمال/ رگبار شدید و آبگرفتگی در جاده‌ها؛ باد شدید در شرق اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124986" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124985">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81d6e65b18.mp4?token=aWoIj67WRhr_BSdu4eadVRlTfyiojkNajjAUy2PSDEtz7jMp3ttu1rs7cVL0YP6N6fjS6bPrvLf9CF254kKi_fRShzQsxQAUwFIHwEzEw2WB26pfxLv45JTaJ1kxT1lCduTz-esPPp-O4wD4fHl9qgziIhutJbzVuhprATHGDnqle8YijqClWF7xCrPj0-dp5cfshkhJux5ffKiEwVBQ_Asxq6FsMnT5I-A9tUBWD4z5u3v6DU1NSx2Io_aR988JPsmNJnPTToGLV_egQ5FdcoXS1veJ_g5wPOB_lCRIXfzfWtKMD4rUS0flQcBlgcpPrBscOYZwKOMPVaNMFjs7WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81d6e65b18.mp4?token=aWoIj67WRhr_BSdu4eadVRlTfyiojkNajjAUy2PSDEtz7jMp3ttu1rs7cVL0YP6N6fjS6bPrvLf9CF254kKi_fRShzQsxQAUwFIHwEzEw2WB26pfxLv45JTaJ1kxT1lCduTz-esPPp-O4wD4fHl9qgziIhutJbzVuhprATHGDnqle8YijqClWF7xCrPj0-dp5cfshkhJux5ffKiEwVBQ_Asxq6FsMnT5I-A9tUBWD4z5u3v6DU1NSx2Io_aR988JPsmNJnPTToGLV_egQ5FdcoXS1veJ_g5wPOB_lCRIXfzfWtKMD4rUS0flQcBlgcpPrBscOYZwKOMPVaNMFjs7WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روز گذشته/بدشانسی عروس و داماد سنندجی و تصادف شدید با یک پراید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124985" target="_blank">📅 10:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124984">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی: از زمان اعلام آتش‌بس، حزب‌الله ۶موشک به سمت نیروهای ما که در جنوب لبنان فعالیت می‌کنند، شلیک کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124984" target="_blank">📅 10:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124983">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLtx5Dytxu8KHCk9Rtaccpe9aJbLlBbR_4eENn9Jo2zYKYW2ukuCymEumSSPnPO9w4OHVNd8WvOI0JzIkWlJfOgFwYgHPChOYKbMJf8GyHvu7mlC19UsjAO3a8vXw3U8W_3Fc5pDedx7eVj_o5UnRjRLKedrWXbjHbw6-RT3bLMo7qHyFHcJCBpYGwyx_-zI4VRqxIaFe7KQp2p-5p0wJ0InrjGbcjNWq0w96EMukooruFdQhaDW9JHemygsw0or4eAyGQp8qwrcNfcFGBJUuQSASFRrBmJ0kbdLun6MNHy9P1HqrXdYJnSyzGG0rqxPHjh3uBMx_ez1IJKVwyKKdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله مجدد اسرائیل به منطقه نبطیه لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124983" target="_blank">📅 10:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124982">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
شهبازی مجری محبوب صدا و سیما: من سالم هستم و خبر تجاوز گروپ به من کاملا کذبه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124982" target="_blank">📅 10:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124979">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mej4ygPZnQwpWTZW7K4nrqxdms3eIk-sZiGRSOAtdMQnvueE4_YADAKZKn-TL7UUzxj0SUCGsa9kwovIVAVqhvh7orcZMKVrvyAnDsvBBl210Y_pp9nugREMXKcP_P0gHAVzLY0KV9TM2S47aj9pj-c72AZEu5ceHivgomeeS1gQ4OVqtcOqCUFO11lWg2topSJ4Mg8It7m46zkv9oyexUZqSu-srAy3pmwobvjs4iEicnL52FRaKHNveC24FmBpMVYblCD6LS1EGF1dfQRll2mMJNhYfiETioIjJhpn9m5dY5vQz-jPPwlemv-W6EJLkEFzuRynD7jL_SPtpYeVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ip5Qi7gWxv8E1FX_Yydxy4JLMZwFnaMGTpI56_75UKaCInPEW6tbfJk0SfcziOxfCQ_GlSiE5iHzLUneJYDg6ujoE-GaudYc-b6YLTWXZLmXJ4SAtlY4VrdsxaLRU7xHwxC07aIFRmcemwmX9qz4N5xVPwJ2bq-MZOMi02QAoMrzbDjPLOE3revqZNBBQC70fINNqnYYa4L5gyF6Jv8CiH6tczOGJTSXIZUi-IlnI6I8gKiNhTm2vGI7uBLJRMzYssL1sPZujAHUHp5cI_CWQNke8szMr3kESCr1lsPvsoX5NhPCP8Xiq43Z2oxIazS1sCMce7LXutU6gFyuRs9JSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2724519f2.mp4?token=flKCjhizTmIXpEMI28SuRwsaYeuKPAEw3u05fHhq_uunLdRZwAoojTb-Z0TbQ18VXCHsQiGL4WSFR6HovdlWcuVbLU-gYswwDxe7MFw6zOi-SErRL8v1HeUb5awy9KH7ZnO-xcAlCKKCtxK_7GkpmtXcSOffxR56Fcq7jTALP-xKbgfq_tJQIraaMuxzSIcw66Juc-Y25o98ozz8k8HmXPkCAGLV1PGvWBcB8h8x3Am9Hl33cYrKVKfoxCNxvCxFljmpDL9LLnGf0MHBGTFYxzvM3NJejhKDN2XkSEgeSjfzjYaDmx7L1x6oxZo8WrmnjPmyZQ4685f2Qoz8S68A0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2724519f2.mp4?token=flKCjhizTmIXpEMI28SuRwsaYeuKPAEw3u05fHhq_uunLdRZwAoojTb-Z0TbQ18VXCHsQiGL4WSFR6HovdlWcuVbLU-gYswwDxe7MFw6zOi-SErRL8v1HeUb5awy9KH7ZnO-xcAlCKKCtxK_7GkpmtXcSOffxR56Fcq7jTALP-xKbgfq_tJQIraaMuxzSIcw66Juc-Y25o98ozz8k8HmXPkCAGLV1PGvWBcB8h8x3Am9Hl33cYrKVKfoxCNxvCxFljmpDL9LLnGf0MHBGTFYxzvM3NJejhKDN2XkSEgeSjfzjYaDmx7L1x6oxZo8WrmnjPmyZQ4685f2Qoz8S68A0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صور، جنوب
لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/124979" target="_blank">📅 10:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124978">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f6a25b81.mp4?token=URg8qbOYWOsLqqeg98N12u5cK7K8d3JZII6Lafx0HUOgUVlxl1wdzrxDtsYMNV-xQhWL5X64PlnCB06F6rkneBQfB8hEx_HryZDP3jIhHjCgYpulv6ayC4D20E1rEfiSYbHRBVSvS0yk4niH8XYCd6YVyU9cGcg7mfuByp6PleMJQAdkGcQf-jy5x0FMiPC37Acg4MOzq-5PRuuul_UZtFhq2COKnMm3LQShAkcKhmqjGGuivFMB964c0fhkuUm41rilGeIGBR1ajEhiVdIQvA1OkICXSPtP5ZbYz68JzsKW0PG9ijTVqJ6yU5T72-bcB1zn7nMnpIET2EH-Kor8fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f6a25b81.mp4?token=URg8qbOYWOsLqqeg98N12u5cK7K8d3JZII6Lafx0HUOgUVlxl1wdzrxDtsYMNV-xQhWL5X64PlnCB06F6rkneBQfB8hEx_HryZDP3jIhHjCgYpulv6ayC4D20E1rEfiSYbHRBVSvS0yk4niH8XYCd6YVyU9cGcg7mfuByp6PleMJQAdkGcQf-jy5x0FMiPC37Acg4MOzq-5PRuuul_UZtFhq2COKnMm3LQShAkcKhmqjGGuivFMB964c0fhkuUm41rilGeIGBR1ajEhiVdIQvA1OkICXSPtP5ZbYz68JzsKW0PG9ijTVqJ6yU5T72-bcB1zn7nMnpIET2EH-Kor8fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حمله به انبار نفت کرج (فردیس) در جنگ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/124978" target="_blank">📅 10:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124977">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4f5-G3thl5UjoJwOYcK966CVK0JtXMjBzziuMizChsb21Jr-dB-vmIB3BzHfPCBg4U17-lxe2KsCUL7SnTW4_7RBqsC2zsAQjGIRDRIS6bdMk5p6PBK6o5zuib97QZ6ZI1JhVWnCQDWH2zRDeN5qf7jqWGAhXsJidCXTI769n3UOnyT_e3YjtemY8d34cIsmFwXWuOsI-isZa0ttESvEJFy-94xNpxCcdA9krZYihyq7GR9l2EwlY9Jwxk3c0dTgAFGrC80R21FbZCNQG5inWDxOiznnudVfbhCUvjJEcvl2XF32qfFPiniDtNixt3FnuSDMJAzI9J0Ja70-wc6VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: دموکرات‌ها دوباره شروع کرده‌اند! آن‌ها در تلاش‌اند تا فرماندار کالیفرنیا و شهردار لس‌آنجلس را از دو کاندیدای بزرگ جمهوری‌خواه بدزدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124977" target="_blank">📅 10:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124976">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وال استریت ژورنال : ترامپ جمعه گذشته آخرین پیشنهاد ایران را رد کرد و به دستیارانش گفت که ایران باید از قبل امتیازات جدی بدهد، نه در یک دوره طولانی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124976" target="_blank">📅 10:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124975">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLPH1PiRzmwbfd3hBlxokzUTfvMz2Mlpr0S3PuNfNXwy5rSgdPrSG_gUafO9pwvO0anUCElU2_Y_EradtU1wof9w35RjliixC0_vmn_SPIaHdS84KJ3tzIswn0cEIr3Dqd7Xj_pcVH9oDlZrqNCDB2eJQvWmSlqb8BO6CCXwRx6O9AhmNS0OGF90WPVq9I2vbTEpR0cKgO0qBpEKmQ-Kw-6StolwNtlppNSeMfI2IegdiVMaPWf56j_FdnIc5c_JghzqUNBLu5gpB5vRhljRB86__uZ6haL9TikH-W6hnHoXevlYS1mIXqAfQ8cFKWWsimf6ByJ-Q2Qd631oc8bUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات هوایی اسرائیل شهر صور در جنوب لبنان را هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124975" target="_blank">📅 10:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124974">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_Ucv3rsq9G_l7EiCzxBdPHszAVHeb3HAqdB0yLfWASctbICBgziDxLJeMtC3jyoBt4W971hm_dwpwpt1KMmD_ntm5hRchDJpnVQ2RHvPOmmhFvMA7F68O5Eo7-xaLBhposerjf5ivuaNGLQYBRAlO-zcSTaqkWj0ggTHm7sR1-PpPY4YmxdoRdVGlOJud4DFV-bPkdfaVp4itULAXVv9HRxipAbG4C0hNYnTKqxZRyw68u6LKWKj1L8tPXYkp1e-NW2YAIXYEq8uMU8-udkI4dzvIdvg5cXdvXl8RDPuOUb0SxtdrzpV29EW3n9vlCjF5cVDZOIaGq2rRt3e9PoKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکا بیشتر از عربستان و روسیه روی هم نفت تولید می‌کند / ایران در رتبه هفتم
🔴
بر اساس آمار سال ۲۰۲۶، آمریکا با تولید روزانه ۱۳.۲۵ میلیون بشکه نفت، بزرگترین تولیدکننده نفت جهان است. این رقم بیشتر از مجموع تولید عربستان (۱۰.۱۱) و روسیه (۱۰.۰۳ میلیون بشکه) می‌باشد.
🔴
ده کشور برتر تولیدکننده نفت در سال ۲۰۲۶ (میلیون بشکه در روز):
🔴
۱. آمریکا: ۱۳.۲۵
🔴
۲. عربستان: ۱۰.۱۱
🔴
۳. روسیه: ۱۰.۰۳
🔴
۴. کانادا: ۵.۰۶
🔴
۵. چین: ۴.۴۲
🔴
۶. عراق: ۴.۳۹
🔴
۷. ایران: ۴.۰۳
🔴
۸. امارات: ۴.۰۱
🔴
۹. برزیل: ۳.۹۵
🔴
۱۰. کویت: ۲.۶۶
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/124974" target="_blank">📅 10:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124973">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
لیبرمن، وزیر جنگ سابق اسرائیل: آتش‌بس با لبنان چیزی جز مهلتی اضافی برای حزب‌الله نیست تا بتواند دوباره صف‌بندی کند و قدرت خود را تازه بازیابد.
🔴
این آتش‌بس نیست، بلکه بازگشت به همان رویکردی است که ما را به هفتم اکتبر کشاند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124973" target="_blank">📅 10:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124972">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b489036c24.mp4?token=hwFalb2ypknBGJUuRGedXrPnJfCWOdjvnjPs_AP5vbWnRjJ8t9N_QnjIgtOFvbgE-urgVKVj-yzn3O-zqh8QKo-Y4tlXHbNXbd-zTlw8D5Rj6lZgJE01RkzS-rQqFSYaQjCF335bR_0310ClDbDZYqrhGz3GY_HDo6E7sH0SjJWznggZ5IVwSxUpy36juED5CslDdwarZpzUbIMjUPKbzYt6ReqkfIjvgxUpmYnTWOV2-aCpopWtizPApoTQPKk7oxJJYwG7Haqr0B9XhjeEsle9MVmYsSv_su5jYzr5UAnqQsfAx20J9yKjiF-0Vb_M1hOwFKJZKDy-IhILAIJmhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b489036c24.mp4?token=hwFalb2ypknBGJUuRGedXrPnJfCWOdjvnjPs_AP5vbWnRjJ8t9N_QnjIgtOFvbgE-urgVKVj-yzn3O-zqh8QKo-Y4tlXHbNXbd-zTlw8D5Rj6lZgJE01RkzS-rQqFSYaQjCF335bR_0310ClDbDZYqrhGz3GY_HDo6E7sH0SjJWznggZ5IVwSxUpy36juED5CslDdwarZpzUbIMjUPKbzYt6ReqkfIjvgxUpmYnTWOV2-aCpopWtizPApoTQPKk7oxJJYwG7Haqr0B9XhjeEsle9MVmYsSv_su5jYzr5UAnqQsfAx20J9yKjiF-0Vb_M1hOwFKJZKDy-IhILAIJmhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی جنوبی ایالات متحده:
نیروهای آمریکایی به یک قایق مظنون به قاچاق مواد مخدر در شرق اقیانوس آرام حمله کردند و دو «تروریست مواد مخدر» را کشتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124972" target="_blank">📅 10:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124971">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd2ae2072e.mp4?token=XS5JKlMvZF_toY2qgEEiwwCNqBxtQmWepJouRXh0JVUSX_fk6SNvRrFc7LSt_eUivUz4jQeAoZID8Zp2rOEGzI1dHYOJBkE3RxueSxQny6dfSHLTZLBWcT6dbNyg9g39Xnv7Cz87NDX4tmlkdltpSFYUYSb5OrK8fkLnpzHn8TXlzDTJ1fjQOWvdSbRiRJlhR-ajS3ExGPG5flZQAL1VcWNOaQT262MmEcGnzsDPHrFuJXsWMzoVIXMO1F16p8boVBld-I2drlQ73t8So-YH3XkMAke4O5t2FOzHs-JAbhcdwNNjai0ZEWHDnHcQnNqYhBy7-W76Ctf0M9D6JH90_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd2ae2072e.mp4?token=XS5JKlMvZF_toY2qgEEiwwCNqBxtQmWepJouRXh0JVUSX_fk6SNvRrFc7LSt_eUivUz4jQeAoZID8Zp2rOEGzI1dHYOJBkE3RxueSxQny6dfSHLTZLBWcT6dbNyg9g39Xnv7Cz87NDX4tmlkdltpSFYUYSb5OrK8fkLnpzHn8TXlzDTJ1fjQOWvdSbRiRJlhR-ajS3ExGPG5flZQAL1VcWNOaQT262MmEcGnzsDPHrFuJXsWMzoVIXMO1F16p8boVBld-I2drlQ73t8So-YH3XkMAke4O5t2FOzHs-JAbhcdwNNjai0ZEWHDnHcQnNqYhBy7-W76Ctf0M9D6JH90_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مداحی به زبان چینی!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/124971" target="_blank">📅 09:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124970">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6mdBszGFUo0yD2iOyYpzBJDDJyCd1gVonxWG8kzNpKRKjD51BDIZXL-1kF6B2896Z-Bh1ddqlL01JuxRV-qcJYd6CFr9P2Nkxt8p0yLX_zWAyrDNGe4whyZLicNepARTBJgB27SaSTA-jxkU35ZySKzwi-0S5eIVD2gSyBTUcTsI9t2hc-hi1KpkKHrF3ky5nptyxPuIYJnw3h3oC4x-UdvAp6YJzLUd36fkH-plvKPzudOcyPSbhGOwbEHDRTCcgVej6CSy0BtQNHIspUR57dcgO1lCDoBWM8tQj4vj_FHM9CzlYQO1zeqfCRmY215druXxoFgYEwDRrBxrra1UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اپل برای رونمایی از نسل بعدی سیستم‌ عامل موبایل خود آماده می‌شود. بر اساس اعلام رسمی، iOS 27 کمتر از چهار روز دیگر در WWDC 2026 معرفی خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124970" target="_blank">📅 09:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124969">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
کاتز: اسرائیل این آزادی عمل را دارد که با حمایت آمریکا در پاسخ به هرگونه آتش‌سوزی به سمت شهرک‌ها یا اسرائیل، به بیروت حمله کند
🔴
حضور ارتش ما در منطقه امنیتی شامل منطقه قلعه بوفورت می‌شود و ساکنان از بازگشت به آنجا منع شده‌اند
🔴
یک منطقه غیرنظامی در جنوب رودخانه لیتانی ایجاد خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124969" target="_blank">📅 09:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124967">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bac082417.mp4?token=ssIXfjbUPdOsTBqVj_oUN4G2_zP4vd1zj4SKHU84hQgz4EilQ4ipgijADwTg16lK-JxUfB-WKTdNNJcRktLAPoH20ZnKfmYrNKkInkcf66g0iceQzka2en2pzxDTq17-uOP5_a_jxJ5ZfiFj9T3YBK7wbfYbOumPoQ-IeN62E0D2aZOtFx_6PFYw7IU4nrWHv0Hsq0IfqADnPQ3Ubg7E_1R927LpEFdS4zqRPfsZz_yJyQZInhiFg58UY7BvXH1TAvvFLurFnSKY4NbV7sWBxZ8aCdHK4whMy7mViP8fnd8S1jQZ-8bLR7My4ExqWn5jbtVwQyqBW1Kwd3amnRNXiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bac082417.mp4?token=ssIXfjbUPdOsTBqVj_oUN4G2_zP4vd1zj4SKHU84hQgz4EilQ4ipgijADwTg16lK-JxUfB-WKTdNNJcRktLAPoH20ZnKfmYrNKkInkcf66g0iceQzka2en2pzxDTq17-uOP5_a_jxJ5ZfiFj9T3YBK7wbfYbOumPoQ-IeN62E0D2aZOtFx_6PFYw7IU4nrWHv0Hsq0IfqADnPQ3Ubg7E_1R927LpEFdS4zqRPfsZz_yJyQZInhiFg58UY7BvXH1TAvvFLurFnSKY4NbV7sWBxZ8aCdHK4whMy7mViP8fnd8S1jQZ-8bLR7My4ExqWn5jbtVwQyqBW1Kwd3amnRNXiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیده شدن دونالد ترامپ در یکی از پارک های شیراز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124967" target="_blank">📅 09:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124966">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: به هدف قرار دادن زیرساخت های حزب الله در لبنان ادامه خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124966" target="_blank">📅 09:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124965">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
رافائل گروسی» مدیرکل آژانس بین‌المللی انرژی اتمی در سفر به ریاض با «عبدالعزیز بن سلمان» وزیر انرژی عربستان سعودی دیدار و در مورد پیشرفت این کشور در برنامه هسته‌ای غیرنظامی ریاض گفت‌و‌گو کرد.
🔴
گروسی در صفحه شخصی خود در شبکه اجتماعی ایکس نوشت: «برای من مهم است که در عربستان سعودی باشم، زیرا ریاض در حال پیشبرد برنامه هسته‌ای غیرنظامی خود است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124965" target="_blank">📅 09:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124964">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
کاهش قیمت نفت با امیدواری به آتش‌بس لبنان و اسرائیل و خوشبینی به پیشرفت مذاکرات ایران و امریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124964" target="_blank">📅 09:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124963">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزارت امور خارجه فرانسه با انتشار بیانیه‌ای همبستگی کامل پاریس را با کویت و بحرین اعلام کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124963" target="_blank">📅 09:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124961">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nNam5MYB4A3MsTo9hf711TF1VyUny12fOkE-fRywJObRG6I93bfrIFpBSK698RtXNtjTFuoLTzvaEq5Q4gYNht9aO0i6Qa41ho4cPwe11_mhTTMhQzIfbWaYxgKkncFCkGkfhme13hsVhl75rS7tWGAnc4YjUiqDthKS-r6ur4TMmtrsphybbwn7qovDK2qkTr2kaGOD6Hhink_gmX96PgcSLp_n4VbNyD3ONse7OXV5RwyTEwrbe6EiSUr-_8JLkN43tD6_Z8RGp2j4BMH0-kvD5MbZCMtmFcZDqkCYQVwnPeJjlzHuwxU7qsgsTNdI1KF5nCE1IPr8evezkwiEFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tT04e6Y_oQ2dabGFaz0FPFzpifyOoUrGIvrXpj17qNQ2cpM5v8d6IbYqFCSoX2y2f7y9_DT2IblpbyaVQYaNYHg70M35ANU7eQnMBQfZToaENJJ75RV-10EJgJCZoqb2ZZY8oprO2ceq7JAGOEjpQRprzahYwHY_0-9pFfAcuUdMx-Ng60WguZuSapswWNTW0_U-wPMOy2rduHQiHtz9Wr0HmMlsy5WQNnwU74JBfvd-nr1GUhcpTDA5lX9gYIMpx3VdboFf5z1RxPxQvUmPISRqSwaW0p0M370x7LaDJkcKYK4pUQhCI7djwqKEjBdy0Ye0vtxKG13OCu1tCo3_fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا به درخواست نماینده تگزاس، واکین کاسترو، برای پاسخ به این سوال که آیا اسرائیل سلاح هسته‌ای دارد یا خیر، پاسخ داد.
🔴
وزارت امور خارجه پاسخ داد: «ما شما را به دولت اسرائیل برای سوالاتتان درباره توانمندی‌های اسرائیل ارجاع می‌دهیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/124961" target="_blank">📅 09:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124960">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
محمود قماطی، نایب‌رئیس شورای سیاسی حزب‌الله: تمام تلاش‌های آمریکا و اسرائیل با شکست مواجه خواهد شد.
🔴
رویارویی ادامه دارد و مقاومت در برابر تجاوز اسرائیل همچنان پابرجاست.
🔴
آمریکا و اسرائیل هیچ حقی در مورد سلاح‌های مقاومت ندارند، زیرا این یک موضوع داخلی لبنان است که ما در مورد آن توافق داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124960" target="_blank">📅 09:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124959">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
بن گویر وزیر امنیت ملی اسرائیل:
آتش بس با لبنان یک اشتباه بزرگ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124959" target="_blank">📅 09:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124958">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOCGWscYodRyueAmHCckZLjoWy9kNuedZraRUlYKLSCmfbNxpWmQZEwqH_WX_S8mm4TjvLw_N93pQd0ixLvodv1PX8O3IsV6604W2rwAJ1TFljlYEFbb7vkWvqZSLprZ8KRsYv3eHtp-quAU_73iHzgTDyKCGZfoDJoVjcA4HNVzdZ0DmaeOxthrpmJ8fPN-RvqZPe3ot75TzXBnRY5h88dTX5bcddTC3Q4ELtuIXKsQ7krdxCDsAnRnBY_YRCYw6V1P342J5hZCTws4TDIk4YZSpZJNpLuSfZ3bbrbBv51EF_pBmXWv0bk1W--MgBOCxbi26eZcssXbzoLWZjJMnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکونومیست در مورد مذاکرات ایران و آمریکا: هر دو طرف به آرامی به سمت توافقی حرکت می‌کنند که ممکن است پایدار نباشد. آنها طوری رفتار می‌کنند که انگار این توافق دائمی خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124958" target="_blank">📅 09:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124957">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcCvgcqkCerVevqHvlbQ2ZNmJkGKznxMDICjzkE9sAFN6Z_1_F2VcgxVmBn1h4yZOsXRmw7mZbBkivlhORYNdQLXewtOZM8K329wWZF2z-YhINUmxTPCK-7beQIiqzdXXgUubajIYdS6K-Wa1AUcaZnkZGeWf_ioMKk5v4NbZpcmMDmj7rX4AnSg86uH0ZSdMpDDYDw90-WlzAc_1z6khNWIjAaUxqT6LOO-JbRvK3CQtOXJgPSB4bvQZ-nGaLr5H5snmH50eoYXMZ8yHgvd34k2lgkcWGHQhlGwqh2hjYSLfYcI91tAM5hSsWeHzyBRX9GQJ8gvovWqJICK9lMKtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فایننشال تایمز: همزمان با جنگ آمریکا علیه ایران و اختلال در عرضه انرژی، ذخایر نفت آمریکا به پایین‌ترین سطح از ۲۰۰۴ رسید و در صورت بسته ماندن تنگه هرمز، احتمال افزایش قیمت نفت تا ۲۰۰ دلار وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124957" target="_blank">📅 09:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124956">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-Jb0J9asQENI4ZFNfLbS1qNLf7wgz68jKWWh_PrVSAwS5zpBlTcOL2SVwVHyH6QxOTZeJA7ZsSse5eO9YTVn7DNxdrkHRxWnSb38mzzyI8gnU9XmXQQ-mzY0-ryCpMohAdFds8zYFJsfUgJcBKw02oHNnT-vdTk4N7r0-et9RdRVk_BKpolcB8lm9OiVzliWrbg61YjpH5mDMwfhQKUiRbXPLeNzpaxgP0X9sGuVw_PT87O9CPuNeg7RMLe8n1whC4BLs4KfN3TgkI-xuivZCx_d1ktNd7VHJtuVRMJC39DTW6tahAUIKC8dZtMkhbG1aNbVPDxCiIUvXITOTiyrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت کوین برای اولین بار از ۲۴ فوریه به زیر ۶۳٬۰۰۰ دلار سقوط کرده است
🔴
بیش از ۱.۱ میلیارد دلار موقعیت‌های اهرمی ارز دیجیتال در ۲۴ ساعت گذشته نقد شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124956" target="_blank">📅 09:15 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
