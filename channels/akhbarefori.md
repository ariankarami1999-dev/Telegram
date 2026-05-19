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
<img src="https://cdn4.telesco.pe/file/OsukagpIGai8Ajici7wprlwD7dyb6FmmNS6axFuLB-H6oMu2cVTq-pn6XUSKSlE2am1prydjYOSVIk8vRWl3zKMZw48OuHE56MvNKk_tY6eMwZeCiw-yrFX2EvxFUsNJuAKCwRfnnLH12NpHM-XIJRKRCyd0nf_KLQLBd0kRM1cjYl3jVFmHOZjiTA1pAOGEtjVh3MMOcM72Khbz2RvYvH3SKxi1e-DOVqABNeA6MsIfokP7HE6wF7unCtTZ_cyUWfqVYntz_XDHup1ktPrwpGLhfSlmHz8Q-p8dMxml8ehwc0wtOYM6TbqlGtx8MuoC6O4Cb33OHFg1r_dRVzl14g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.99M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 14:16:55</div>
<hr>

<div class="tg-post" id="msg-653022">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc03414cab.mp4?token=n1LFgLGQfuaL15LRwacFrEs3fRW7ma4DmjtRwj7sT52trqt_sXPmkzTGaxvMgb-FJjUcjvXWJpQ9-2Ij1RpOAhrrLv9_CqP-kceezTL8QwFCgjmlqdRisq0jJxzdBCSq5Oybggaz8G2j22BpPrs6J1N4INr1QlZjmx9dvEE97AJsKnViezWbDkKbgslpSX-VmLBgIrBO4yOk-JvigZGwb4pUIuiKrtLOL3T5MMAQwg4Ymj6PGr8meoBJlesF4OTzHtHACc8vKE24z2b_T-dAL9CtiPYpKh78TFLf4v3pqEQtor-up4oeNTf2yRP84SrP35CXaPvDqoKjXyPDWDShTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc03414cab.mp4?token=n1LFgLGQfuaL15LRwacFrEs3fRW7ma4DmjtRwj7sT52trqt_sXPmkzTGaxvMgb-FJjUcjvXWJpQ9-2Ij1RpOAhrrLv9_CqP-kceezTL8QwFCgjmlqdRisq0jJxzdBCSq5Oybggaz8G2j22BpPrs6J1N4INr1QlZjmx9dvEE97AJsKnViezWbDkKbgslpSX-VmLBgIrBO4yOk-JvigZGwb4pUIuiKrtLOL3T5MMAQwg4Ymj6PGr8meoBJlesF4OTzHtHACc8vKE24z2b_T-dAL9CtiPYpKh78TFLf4v3pqEQtor-up4oeNTf2yRP84SrP35CXaPvDqoKjXyPDWDShTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صید یک بولدوزر دیگر توسط حزب‌الله
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/653022" target="_blank">📅 14:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653021">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
مجروح شدن ۴ شهروند اندیمشکی به دلیل سقوط پرتابه
🔹
معاون استاندار خوزستان: صدای شلیک های امروز در آسمان اندیمشک به دلیل تست پدافند هوایی است لذا مردم نگران نباشند.
🔹
به دلیل سقوط پرتابه در منطقه مسکونی، چهار شهروند مجروح شدند، که خوشبختانه در شرایط مناسب و پایدار قرار دارند و هم اکنون در مراکز درمانی به وضعیت آنان رسیدگی می شود.
🔹
با هوشیاری نیروهای مسلح و مدیریت استان، شرایط کاملا تحت کنترل و موضوعات ضروری در زمان لازم اطلاع رسانی خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 454 · <a href="https://t.me/akhbarefori/653021" target="_blank">📅 14:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653020">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
خنثی‌سازی مهمات عمل‌نکرده دشمن در پایگاه دریایی بوشهر
🔹
فرماندار بوشهر: اجرای عملیات تخصصی خنثی‌سازی و انهدام تعدادی از مهمات عمل‌نکرده متعلق به حملات جنایتکارانه آمریکای صهیونی، از تاریخ ۲۹ اردیبهشت‌ماه تا ۳۱ اردیبهشت‌ماه در محدوده پایگاه دریایی بوشهر خبر داد و انفجارها در این بازه زمانی کنترل‌شده بوده و جای نگرانی نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 489 · <a href="https://t.me/akhbarefori/653020" target="_blank">📅 14:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653019">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
انجام اقدامات حقوقی برای آزادسازی شهروندان ایرانی در کویت
علیرضا سلیمی، عضو هیئت رییسه مجلس در
#گفتگو
با خبرفوری:
🔹
چهار نفر از نیروهای ایرانی حین گشت‌زنی دریایی در کویت بازداشت شده‌اند. این موضوع ناشی از اشتباهات ناوگانی است. اقدامات حقوقی لازم برای آزادی آنان در حال پیگیری است و این اتفاق مورد خاصی نیست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/akhbarefori/653019" target="_blank">📅 14:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653018">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
سخنگوی ارتش: دشمنان دوباره حماقت کنند، جبهه‌های جدیدی باز می‌کنیم
🔹
ایران محاصره‌پذیر و قابل شکست نیست. اگر دشمن حماقت کند و مجدداً در دام صهیونیست‌ها گرفتار شود و دست به تجاوزی دیگر به ایران عزیز ما بزند، با ابزارها و شیوه‌های جدید جبهه‌های جدیدی را علیه آنها خواهیم گشود.
🔹
با توجه به اشراف نیرو‌های مسلح به تنگۀ هرمز و غیرقابل بازگشت‌بودن وضعیت تنگه به گذشته، تنها راه دشمن احترام به ملت ایران و رعایت حقوق حَقۀ ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/akhbarefori/653018" target="_blank">📅 13:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653017">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b81e83a5f.mp4?token=nHPZBfP-3ZKqJYDX7xmT0FNaB7yAAl77HNw5edmlCF8-pNgswIM_W_fRRB50tysozKTcPg5LiH4FW3Fezj_M6r7pOKHgNInSAOnrXBoxKx2YRHJwVbUv8yc5QI9MZg7aK8T0sYFtNMZXz7UX7bWhX2c1DPOAsPx6htvJklK1yHPV_Ui-WkBdo2kNFMkrW19xxfsFHSd_Kg08V7XrKynFKUKslQ4h1A3z_JvIMupDyG2wbkxPLIrTgojysjaenqqhQobFeIWM8NGWYwQ0bnGo3rv0RDn0ptJCJpKDZ32Jtkl1d8dA7AVt2FLh4Wyw3Qu7b3FiLlrc22_-3TcXmpDwOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b81e83a5f.mp4?token=nHPZBfP-3ZKqJYDX7xmT0FNaB7yAAl77HNw5edmlCF8-pNgswIM_W_fRRB50tysozKTcPg5LiH4FW3Fezj_M6r7pOKHgNInSAOnrXBoxKx2YRHJwVbUv8yc5QI9MZg7aK8T0sYFtNMZXz7UX7bWhX2c1DPOAsPx6htvJklK1yHPV_Ui-WkBdo2kNFMkrW19xxfsFHSd_Kg08V7XrKynFKUKslQ4h1A3z_JvIMupDyG2wbkxPLIrTgojysjaenqqhQobFeIWM8NGWYwQ0bnGo3rv0RDn0ptJCJpKDZ32Jtkl1d8dA7AVt2FLh4Wyw3Qu7b3FiLlrc22_-3TcXmpDwOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر دارایی رژیم صهیونیستی: من اینجا به طور قاطع می‌گویم: اگر حزب‌الله تسلیم نشود، ما بخش‌های بیشتری از جنوب لبان را تصرف خواهیم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/akhbarefori/653017" target="_blank">📅 13:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653016">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibMjr2MLhb1oEtRoTTSmSzJAJbf_321rlTNaHseU5f4XcjOgTCKQE26F3trXN3lf_CkSdPx_KfS-mKydnvSFSAiadlv7_d4CG-LPSuz0kieEi39ZlBmOyeS9D_s_syfJJ1ETk2SeSOYt1KyJlOaM7i_OV56gIMUCNXpneAzhIHlqpgOye0yo9rdGo-MCb0Gq2hs3n3VCGzlNIQTB02nZwjZCrPv_Na7g244VToYoyHuoYLtJr01yRz2DPg2nrlZ8JLc7POZ-wqeStzgw-32DlQGfN10UeVtfh7Pw6GK4VuWaMy6jEyLHNwCD_v-DwoGe-2Qmc8-7FTr2XAYogqT3ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر صهیونیست، مزد خوش‌خدمتی‌های محمود عباس را داد
🔹
وزیر دارایی رژیم صهیونیستی ضمن حمله به تشکیلات خودگردان فلسطین و رئیس آن، تأکید کرد که با این نهاد، وارد جنگ خواهد شد.
🔹
بزالل اسموتریچ همچنین هشدار داد که هر هدف اقتصادی یا غیر اقتصادی تشکیلات خودگردان را که بتوانن هدف قرار دهد، مورد حمله قرار خواهد داد.
🔹
وی ضمن تحقیر تشکیلات خودگردان، در توصیف آن گفت: این نهاد یک موجودیت حقیری است که از توافق اسلو منتج شد و الان قصد دارد به مسئولان دولتی ما اهانت کند.
🔹
اسموتریچ دیوان کیفری بین‌المللی را «یهودستیز» دانست و گفت این دیوان «قصد دارد حکم بازداشت من را صادر کند».
🔹
اسموتریچ که یکی از جنایتکاران جنگی در غزه است، در این زمینه مدعی شد: «صدور حکم بازداشت مقامات اسرائیلی، به منزله اعلان جنگ است و ما هم با اعلان جنگ، به آن پاسخ خواهیم داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/akhbarefori/653016" target="_blank">📅 13:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653015">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgV9fFMnstI_yjkZJPKoTnJmEC-lDKSTLfMgxnN72N8lhabFrR3Xysf371QBtpM3J4DQgtbJTkn6cRlW0CDIuIL0hQXo9ilo_cc-pRvKWmzLRPoupniiPKf2ZOn8Xc4fZBr01Y-W1kez0HJtfdWBQDu9BCqhOx2uwB_mmL17nrsQspfqjI2o2mDN5k7u_LcBa1R-eMA-Hf5TiFplaj6nOKxPdiMcHLldcFtGLMZi9hck-fwN8iGC0JTGYhT-907MPrc-UkeUNX3mgv8us-tf6lHL2YclVCDnAb7r03yaCII0llObzElCmpZ-NLsNbTQ3lhlmKMM8jAWW0R8z5nGAmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان افزایش قیمت‌های جهانی پس از جنگ با ایران
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/akhbarefori/653015" target="_blank">📅 13:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653014">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f7bc38532.mp4?token=WouopwpyxfYNldnaX8TGzdWqAbWNjBKYwsTIzN4ThJCIEfTHLjAIBAohRA4f3q7w5Emxs9pZ4RwpPYpxOLbNLxhSzpfI-C4-OVWosrzl6KKOVZboGMjdvNUQstWpu1Ry1kSmCGIHYBgHZv2pVxjAc8TestxSxWKV8PoeupQQrJ66Ukt-uSxtENv0x_RVRHH3fQAQYoL1EBSkGpg0zZlDALO04noxyRk2d_OrTCAQrTV_xth_qjH3xzXCEMdyWE2bue009kAw5yp1i6DoeBeuVTf51a5sxZn8ZkvOIbCez7mjS3OhfP29pi6r8d9rR5hZhLO5Uh9aQ53r6g2sUIuAgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f7bc38532.mp4?token=WouopwpyxfYNldnaX8TGzdWqAbWNjBKYwsTIzN4ThJCIEfTHLjAIBAohRA4f3q7w5Emxs9pZ4RwpPYpxOLbNLxhSzpfI-C4-OVWosrzl6KKOVZboGMjdvNUQstWpu1Ry1kSmCGIHYBgHZv2pVxjAc8TestxSxWKV8PoeupQQrJ66Ukt-uSxtENv0x_RVRHH3fQAQYoL1EBSkGpg0zZlDALO04noxyRk2d_OrTCAQrTV_xth_qjH3xzXCEMdyWE2bue009kAw5yp1i6DoeBeuVTf51a5sxZn8ZkvOIbCez7mjS3OhfP29pi6r8d9rR5hZhLO5Uh9aQ53r6g2sUIuAgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نظام‌الدین موسوی: بحث‌هایی درباره گران‌سازی انرژی در این شرایط مطرح شده است، این اقدام باید متوقف شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/akhbarefori/653014" target="_blank">📅 13:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653013">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOwhciD0LHU77rvYnYSbv_NtFTw_-0lZh26Rk9zM4ZA3FTLCrGd_leq2cjjWnp2T3lz-n7ubh-Yr2Y0ABkRWre3jnDFcVm5CxQCwwAQSVskMBWX6B-FxKr0Qfi-bJTjwYjc-vpebb2lXXem4Oc3PXvL6qN-F9K1hBh9K4QThUCpJEsnUmRq53CuYddVYcNJ0_B5DPMG8z2S1ottbJOdENIwGbeFIPApP-1Pmn-_CaWvJjsbkJmozpVTzypQvumRPYP5i4a2QBq3y938xCX8O3bFTaACyvxL4CNJTY_IY0pGnUG03ONIZXAnC6LlJRJYwHynH2nvlwYSzfcde_eRrHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آرایش جنگی بانک مرکزی و نظام بانکی با هدف حفاظت از منافع مردم
بانک مرکزی با همراهی دولت و شبکه بانکی، همزمان برای مهار تورم، حمایت از تولید و کاهش فشار اقتصادی بر مردم وارد میدان شده است.
افزایش سقف تسهیلات سرمایه در گردش تولیدکنندگان، پرداخت گسترده منابع به بنگاه‌ها، بخشودگی جریمه دیرکرد و تعلیق محدودیت‌های چک‌های برگشتی، بخشی از اقدامات حمایتی اخیر بوده است.
در بازار سرمایه هم بسته‌های حمایتی برای کاهش فشار فروش و حمایت از سهامداران خرد طراحی شده و در حوزه ارزی نیز سیاست «تسریع ورود ارز، حفظ ذخایر و تخصیص هدفمند» در دستور کار قرار گرفته است.
مشروح گزارش را در لینک زیر بخوانید:
http://www.ibena.ir/000lfP</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/akhbarefori/653013" target="_blank">📅 13:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653012">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
داوید میدان، مقام سابق موساد: حتی اگر یک حمله استثنایی علیه ایران انجام شود، می‌ترسم به همان وضعیتی برسیم که در پایان دور قبل بودیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/akhbarefori/653012" target="_blank">📅 13:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653011">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4hejRaip4gzWiJFzkJnRrwkWr6yoravicoNA3wbQ2Uid59hp2fQO8tZLnuFt9N1ug-5vYK-cTLMVyszE91PQOhFIlxzhhIylknPPWI_WhrUFjkOOnV7Ghex8q3pk1Ajj-swEix1KUajjuliytjoCYNqXJgXUmiSHLarjtrlRUElk0-pUjmKZKcasXvy-sjGU88H6yLJNtqhFv4etcOA55Vu2DHAmHBR4vhcrnyL-yEAonETHXA2tbkQ4q_QNm2tlU5o-bowIN7izn7qiBNa8KFN_kIjJuECa_LeVn6t-E4Mt7D--rgSE_6Mg7hclYzdm4ObWMvFmRY98Q41fERi9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چین با نفت ذخیره‌شده‌اش چقدر می‌تواند از جنگ ایران جان سالم به در ببرد؟
🔹
​مقاله نیوزویک بررسی می‌کند که اگر جنگ ایران و اختلال در صادرات نفت خاورمیانه ادامه پیدا کند، چین تا چه مدت می‌تواند با تکیه بر ذخایر عظیم نفتی خود دوام بیاورد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3216220</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/akhbarefori/653011" target="_blank">📅 13:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653010">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4321c709ea.mp4?token=ryjlfUce4FeN2yUtURDD_xivbX0Ohj8djtNZ8tjRkEoMclylg6pG6BuGhfMIy7LUwNyTisXsUoy0MPR1VLfL8vSD4O9I2O-dKEYik37qwW1CEspXzFqfiWu2nraoD8_lq3qLT9rCG9hoIhY0nNPV_YW2J1c08Ov81aVkXwMJF20mSbwEHDf58dawUKBO8Cn68g2_DduGZrkJZTqtuJgw9Wo-BwBUn4cyvA4u8xJ98bbm2XB9-eADZN1hJjZ3Pd9xjOTVIPDKoANXydi9KiLWKcFMlo2nwvzP0nptgT5eNQa0xeUI5E70s3QrVSm6FwnyA-Fl3Knf7ploE7JZILFkvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4321c709ea.mp4?token=ryjlfUce4FeN2yUtURDD_xivbX0Ohj8djtNZ8tjRkEoMclylg6pG6BuGhfMIy7LUwNyTisXsUoy0MPR1VLfL8vSD4O9I2O-dKEYik37qwW1CEspXzFqfiWu2nraoD8_lq3qLT9rCG9hoIhY0nNPV_YW2J1c08Ov81aVkXwMJF20mSbwEHDf58dawUKBO8Cn68g2_DduGZrkJZTqtuJgw9Wo-BwBUn4cyvA4u8xJ98bbm2XB9-eADZN1hJjZ3Pd9xjOTVIPDKoANXydi9KiLWKcFMlo2nwvzP0nptgT5eNQa0xeUI5E70s3QrVSm6FwnyA-Fl3Knf7ploE7JZILFkvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یادواره بچه های شهید مدرسه شجره طیبه میناب در کلن آلمان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/akhbarefori/653010" target="_blank">📅 13:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653009">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7qxL5iEDCcJSIuYOO1nQQucsR4zKWgOldvcfyFQEjXE44BmCYKKPaawn5Q8OkxcpP4zDzHSnV7B0Ywy5rXrNbF49XawC_S2Sx-YVBcWiTcQcqGhlTNYNrrvLoy7SF4p9Th4JzI8iAZLXmjw1i3935n3F96MCvOFv4IPPHWZx_l4_8l25L80itXjoAHtgfii1LglB29Cl1M11VevCWJTWn-E1Fh4MnRwhqnO5Vo-ue8dDs7TZNNBLpwhCZoYb7T6vJFxMAWQ4F8ZDqtM7xocphkR4j_ihaoz2fejEwU6TdHz6ZBlabsdZPY4euQ9MJCMrNjuA9J67vSsUzyzH-D6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعایی درباره جایزه ۵۸ میلیون دلاری ایران برای ترور ترامپ
ادعای شبکه خبری NDTV هند:
🔹
ایران در حال بررسی لایحه‌ای با عنوان «اقدام متقابل نیروهای نظامی و امنیتی جمهوری اسلامی» است. لایحه پیشنهادی پرداخت ۵۰ میلیون یورو، معادل حدود ۵۸ میلیون دلار، برای هر فرد یا نهادی که ترامپ یا نتانیاهو را ترور کند، رسمی می‌کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/akhbarefori/653009" target="_blank">📅 12:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653008">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgd3DxAL7BctwDMy82JYdW44L59UgM7_OsX3okNwNFxAekfVMhMENCU94i0u-rTnub0mqw5MLW8ROutzJekJSoBo4Wres6XiKWzKo8bAO1yOP4hYnaqh-_9QDJgQgn-mLEqew6ZhpS1nXukFh-ea4160WRs-QS7Z7dU4IG-FEWivcDAdnKs1PmnQ_T8cTzj01j16gjbKM7-IACzbhRHaipiqGs8lzEZMka52ZAZ5hRDaN_BvPbYLKHEIPmW6pQxfxFhw0m260uInwGUBNliSerVe3y2-lWp_ZyDAe4t9FQDbMSSBthZ_LStMDuZd-p7aRTplEzye1kUoIBRxP8XNsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محورها و چارچوب‌های پیشنهادات اخیر ایران
🔹
تأکید بر حق غنی سازی، خاتمه جنگ در تمامی جبهه‌ها از جمله لبنان، رفع محاصره دریایی، آزادسازی اموال ایران، تأمین خسارت‌های وارد شده در جنگ، خاتمه همه تحریم‌های یکجانبه و قطعنامه‌های شورای امنیت و خروج نیروهای آمریکایی از محیط پیرامونی ایران از جمله محورها و چارچوب‌هایی است که در پیشنهادات اخیر ایران مطرح شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/akhbarefori/653008" target="_blank">📅 12:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653007">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9QfJ1LHKt3-2jn4zV-DyOBXUm7Kvb4EuPOISUVqEJyibsAgYnrDSARLDZkMN8mcG3VBQtPOmcbB3mTUJqcoHsCmiiqa68ocs8d-ijudXgFZFbvqremKaiHD94_CM1TQk8DR0qjForTNM6S05VEsvjUH3Q_BclCBQsFcay7TMIMW3popt0Xd8IvyI6wWweqC2uEB0gzfIY5aeLEgvhXbqw5DlppuOtgGZmlOje_8htZv4n7JSEOd-ciSocj_UGgglwZ8Fwf0uwrMmHwaaaAWo7l_gToAw7DrDKZ5QZTzxTucf9LcYV23xC80BNNG7CQI5STABJuKEaeigI4LDh8k9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دادستان‌ها با قیمت‌سازی و احتکار کالا‌های اساسی برخورد کنند
🔹
رئیس کل دادگستری استان تهران: پرونده‌هایی که مصداق اخلال در مایحتاج عمومی هستند، باید به‌صورت ویژه و قاطع رسیدگی شوند.
🔹
دشمن پس از شکست در حوزه‌های امنیتی، معیشت و سفره مردم را هدف قرار داده است و دادستان‌ها موظفند به عنوان مدعی‌العموم و در راستای صیانت از حقوق عامه، نظارت میدانی و مستمری بر بازار داشته باشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/akhbarefori/653007" target="_blank">📅 12:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653006">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3d550e05.mp4?token=fMjCuyHHpqlv8cROKjIv-G5wmmQTsDRnWRyNyUw2P6J8dLpQE7dlspTnSUQgYlqGIDpPk4R2vu1DEIApDIyxCuZKCE_voF5U2rTOWlehTYk-uYYhJB2hjQpvCvkEjMtpBJJ4Ne_K_W7NTYxTX91hdx8g87WDon7aPrjt69mKFPTQsTKkXzQFx6RoMsj8kZ1b-lJ-wrnl11RxT6V0fSJ9xzxqGSzIU74gK7bsSDaP6wLHb4ARnFNWgvwlTfv0xoIdHuAfTqzYdNkAEFRcdAwjje__W0GtOSOEerChNJ3fG10IJ_0QfH0PfHOHVijSjbYtHW3lE_oLNPb-D4Pd_rVbYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3d550e05.mp4?token=fMjCuyHHpqlv8cROKjIv-G5wmmQTsDRnWRyNyUw2P6J8dLpQE7dlspTnSUQgYlqGIDpPk4R2vu1DEIApDIyxCuZKCE_voF5U2rTOWlehTYk-uYYhJB2hjQpvCvkEjMtpBJJ4Ne_K_W7NTYxTX91hdx8g87WDon7aPrjt69mKFPTQsTKkXzQFx6RoMsj8kZ1b-lJ-wrnl11RxT6V0fSJ9xzxqGSzIU74gK7bsSDaP6wLHb4ARnFNWgvwlTfv0xoIdHuAfTqzYdNkAEFRcdAwjje__W0GtOSOEerChNJ3fG10IJ_0QfH0PfHOHVijSjbYtHW3lE_oLNPb-D4Pd_rVbYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ته‌مانده خاندان منحوس پهلوی بعد از به شهادت رسیدن ۴۵۰۰ نفر از مردم ایران از جمله کودکان بی‌گناه در دو جنگ اخیر: جنگ آمریکا و اسرائیل برای ما یک عامل نجات‌بخش است و نه یک تعرض جنگی!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/akhbarefori/653006" target="_blank">📅 12:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653005">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/663e6a181f.mp4?token=kfK5gvqpxdRSbzCSy5yW2KpHYxK97RYlrEe_XjyiMSzkKYpSKsa8jKimQApSkkbboE01IEskaiDohpIeTMDbNjRDujDC-wVXBriQ5VY6FcHdRembbOj_hmb1_GQIKWTxPNg3x0mAHXV-sBGxqNMCBMBfdQpKiXXCymRVvURQ3IYyCwz5c7gOtcUBFRejot4SkrfwufUaz4giqcDIYOuC73iGUGaNPgxMBFv6nPv0vlU-FRfEc3hFRrITKg_pDEPT6h0Trk31NI8byejLPUlJ0cm5v1YtFT4fQl2aU8f51e7cqGoeWH4qnGCazNkZmOxBoqmsLDkOwxyfXg1m8PbLcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/663e6a181f.mp4?token=kfK5gvqpxdRSbzCSy5yW2KpHYxK97RYlrEe_XjyiMSzkKYpSKsa8jKimQApSkkbboE01IEskaiDohpIeTMDbNjRDujDC-wVXBriQ5VY6FcHdRembbOj_hmb1_GQIKWTxPNg3x0mAHXV-sBGxqNMCBMBfdQpKiXXCymRVvURQ3IYyCwz5c7gOtcUBFRejot4SkrfwufUaz4giqcDIYOuC73iGUGaNPgxMBFv6nPv0vlU-FRfEc3hFRrITKg_pDEPT6h0Trk31NI8byejLPUlJ0cm5v1YtFT4fQl2aU8f51e7cqGoeWH4qnGCazNkZmOxBoqmsLDkOwxyfXg1m8PbLcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آذری جهرمی: اینکه خیال کنند با مداخله نظامی می توانند تنگه را باز کنند خیالی باطل است
🔹
بستن تنگه هرمز یک اقدام واکنشی در مقابل تحریم هاست/ رهبر شهید انقلاب گفته بودند زمانی خواهد رسید که ما آنها را تحریم کنیم؛ آن زمان اکنون رسیده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/akhbarefori/653005" target="_blank">📅 12:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653004">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Po4aBoB4wqd6LcL-38nNLFrV5LOU5eRO1lXUE1Z7h_FnIQLhwRi_v10POl75MdulVbUZ_vlRQHXxiJnf78yIrls6SwDq0owngsaW7nrCylwgQuFPQuZ0OmDOwXtj1Ueo8SnhtnNJwbJe8XbWkunIc4ruM8ktTkFS8_U4vFmw-AA5TeJspjLkljZbheQlQpQstp1dGYcTaG-r6V98qHgrqaXUPbNH8mZD1VxpFjjG7vRWMxRsCXnEpUrMSV3Gxv9-rtzapL7HBdKEbmZDtV_-lTbKV7F8JFu6a8GungUMgf4ep-2k2UdvdmKaK2h59ub01uZ8KkzDwreoDd_0v7u0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: حفظ منابع آب و انرژی بخشی از امنیت ملی و تاب‌آوری کشور است
🔹
رئیس‌جمهور در نشست تخصصی با مدیران وزارت نیرو، ضمن بررسی آخرین وضعیت منابع آبی، ذخایر سدها، شبکه تولید و توزیع برق و پروژه‌های انرژی‌های تجدیدپذیر، بر ضرورت مدیریت مصرف، حفاظت از منابع راهبردی آب، برخورد قاطع با برداشت‌های غیرمجاز و توسعه زیرساخت‌های هوشمند برای افزایش تاب‌آوری کشور در حوزه آب و انرژی تأکید کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/akhbarefori/653004" target="_blank">📅 12:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653003">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
اعمال محدودیت مشترکان پرمصرف برق در تهران از ابتدای خرداد
🔹
ناظریان، مدیرعامل برق پایتخت: بیش از ۷۰ درصد مشترکان تهرانی الگوی مصرف برق را رعایت می‌کنند.
🔹
برای مشترکان بسیار پرمصرف از ابتدای خرداد سال جاری محدودیت اعمال خواهد شد.
🔹
ادارات در صورت عدم رعایت ابلاغیه هیات وزیران با قطع برق مواجه می‌شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/akhbarefori/653003" target="_blank">📅 12:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653002">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pw_9Tf4js7ECKJepnJMQjdIcTkUKvK9wln7BhjdUNbrSn-QOmnMBkyqK2sVFTIF-T5pZgl4Gm80mgPgYHPpYYe9daMTubGbJEi0x7SFipp6AloUJ6HPaTiQaPkpcsZ1BS2aK0fhfrnnx_DgJVlgPToyFqBFk8fH0o89T9JFGg3xZ4r5-220dJw0UDvDjRNGz9P-e8A6kcTPvNAaP31WZz2j9hpCEVquXMJdT2QuydLphqlYZ-fQcP7clUP6D1XSszm45WotY9tn_5dT0mbhJHatu21slLOJkPYSUGaql2PxY1hEefmfUZL2Wp9jh2lCZZJfvV5mzIXsMuIsI3AF7vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تخم‌مرغ ریخت، مرغ پرید
🔹
بررسی میدانی نشان می‌دهد قیمت تخم‌مرغ که تا هفته‌های اخیر به کانون التهاب قیمتی تبدیل شده بود، پس از ثبت رکورد شانه‌ای ۵۵۰ هزار تومانی، امروز به زیر ۴۰۰ هزار تومان سقوط کرده است.
🔹
اما در سمت دیگر مرغ گرم از کیلویی ۳۸۰ هزار تومان هفتۀ گذشته به ۴۵۰ هزار تومان افزایش یافته است.
🔹
کارشناسان صنعت طیور دلیل اصلی افزایش قیمت مرغ را کمبود و گرانی نهاده‌های دامی، افزایش چندبرابری هزینه‌های تولید و کاهش جوجه‌ریزی در ماه‌های گذشته عنوان می‌کنند.
🔹
اتحادیۀ مرغداران هشدار داده که هزینه‌های تأمین خوراک، دارو و واکسن نسبت به سال گذشته تا ۵ برابر افزایش یافته و ادامۀ این روند بدون تزریق نهاده با قیمت مصوب، بازار مرغ را با شوک تازه‌ای مواجه خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/akhbarefori/653002" target="_blank">📅 12:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653001">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3030431a7c.mp4?token=iv9Bru0_YzNVpwB6hKu5OZDXIPOQycRPlCwGioXxgCf8hmgJCt4txyi9Mh5VQiToWZVAbPHOkNeZFM1uDr3RmSdueBaxnajcVqQGd17f4KUzqICn3Ld27EieIDn3vM8dGuz0RwQcfVmY2KvkDNRfyv_JmCz0DkJSHub3AvQcO6oa0M6quW9Ux4dccC3ZdIoPmvrvZzvXxUo_CG-UvvP6TEQHde3kGs7TyjpbVqt_b8KPUxe6F6Wt7w3UmEoN1V9TTTv45Iw3EJk83S4ut9GxTtCJEeptaumMGkfRAqbZ0rFOtcBq293GREfbQS3sgBbtTJB8ykf_FHsVV5Fb_iEh1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3030431a7c.mp4?token=iv9Bru0_YzNVpwB6hKu5OZDXIPOQycRPlCwGioXxgCf8hmgJCt4txyi9Mh5VQiToWZVAbPHOkNeZFM1uDr3RmSdueBaxnajcVqQGd17f4KUzqICn3Ld27EieIDn3vM8dGuz0RwQcfVmY2KvkDNRfyv_JmCz0DkJSHub3AvQcO6oa0M6quW9Ux4dccC3ZdIoPmvrvZzvXxUo_CG-UvvP6TEQHde3kGs7TyjpbVqt_b8KPUxe6F6Wt7w3UmEoN1V9TTTv45Iw3EJk83S4ut9GxTtCJEeptaumMGkfRAqbZ0rFOtcBq293GREfbQS3sgBbtTJB8ykf_FHsVV5Fb_iEh1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انهدام چهار هسته تروریست‌‌های تکفیری در جنوب‌شرق ایران
🔹
وزارت اطلاعات جمهوری اسلامی ایران:
🔹
سربازان گمنام امام زمان (عج) در اداره‌کل اطلاعات استان سیستان و بلوچستان موفق شدند ۱۹ تروریست عضو این چهار هسته را که تحت هدایت مستقیم دشمن آمریکایی - صهیونی بودند پیش از انجام هرگونه اقدام شناسایی و بازداشت کنند.
🔹
از محل اختفا و خانه‌ی به ظاهر امن مزدوران مقادیر قابل توجهی از انواع سلاح‌های سبک و نیمه‌سنگین جنگی از جمله یک قبضه دوشکا، دو قبضه آرپی جی ۷ به همراه ۷ قبضه موشک مربوطه، یک قبضه سلاح آمریکایی‌ ام۴، ۵ قبضه کلاشینکوف، ۶ قبضه کلت کمری، دو عدد دوربین نظامی و حجم زیادی مهمات کشف و ضبط شده.
🔹
بیشتر مزدوران بازداشت شده از اتباع بیگانه بودند که پس از جذب و عضویت در گروهک‌های تروریستی تکفیری و گذراندن آموزش‌های نظامی، وارد کشور شده بودند.
🔹
وزارت اطلاعات از مردم خواسته هرگونه موارد مشکوک را به ستاد خبری وزارت اطلاعات به شماره ۱۱۳ یا درگاه‌های رسمی ستادخبری این وزارت‌خانه در پیام رسان‌های ایتا، بله، روبیکا و سروش‌پلاس به آدرس vaja۱۱۳@ با تیک آبی گزارش کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/akhbarefori/653001" target="_blank">📅 12:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653000">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
پرواز هواپیمای دولتی رژیم صهیونیستی به سمت امارات
🔹
رسانه‌های صهیونیستی اعلام کردند یک هواپیمای دولتی اسرائیل لحظاتی پیش به سمت ابوظبی پرواز کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/akhbarefori/653000" target="_blank">📅 11:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652994">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T36g6XJWdHyzPBuNafso5U5ReWzHuPv8a8eO2ez1V2Uz-JfSdGKGkR8byD07c4_YtEsW6HxWbDPSGpCQd4mPhnZqIQP7_4juSDaucGKu3STrCops1NZTI1noLMcMXbZentjEoINgxZBzL1Gig80Fd2PyAxxWvRVKVWjQxWT9QdCz-6PoMx2x_ZOaFYGVulGZ_g2aeUotCEV5Tyhlt9KjgUukPSNrSuaBkzPwBAPnFy8iDcx5KGEciiXicrWryHeEI43Ferk5720vkRNzqbyVLqWtMN9T7DRAs8OZ-mDxZ0Ii5XUnVOh_dHqEX6VAxmEGSJet3tmCBh1cnz-GJEbqCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fxgNHH5U-mbknBVbkEzdFR44BavTPV2oxTQu9jNntQXtgn68wgOq9Ba_zkdd8_pM6DIPkJ6epyIZMPqfPnmvSx1_JijfLnFpdAZfUe2V08tCIJu8fNT2boGzuA2Ng6VNyzGy39Z8LxfR41IZlGJvRU1ExXr5zank-4ctI35YlNjPmG4dtZs7h8gCy3Ow2F7SLiSvTk26XzR_1OBS4C_TudJeuBxt6WjK-FI0j5kYaLl6athNoVWphaO7JCALgrf8UCACwTDkyxJk0Pww-KBfEJle7UHy9gHNt2kao34hLUxmOCzrLgN-9ZNvQRGTuTzS0Qpj7ANipj8Z7ZNKeGtxBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XWBW26SQ7YeEaGF2YpJEFzi8wsi2exRCTBs4GXXnZlBoHgplsTVMFxfmmPlqUZYcDlYZnDofQrYUqBDNHJeWMk6GY748jkNQ44kJ-0G9IVLnf8pHyA-a7h_8t3uOur856BblIl5vMVHfHqjuto6eyI3OVIcMbb2LfW-S6w58-kGCQLGK87grGbYvL7cLC7V9FcWrBIS1p779M6VrwFKlKT77GDQg8-3ULLf6VDeP4VTU4mlVSfVbLjTqxVRBrgysN-LYnf8gLQ1kLl17rUjVd4p--7D9mD5vuXAp5Nyfl3cBA89cpd03Itzl1jor_GRN9qyBcc3bClDe2u5g-NQ3GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iNp_i0vQblLpC1CvsgGBgai6y5Xyzhl6GT3lza_66w6xCnzAolPj-GjcHsVpnHc8zuM-9-2G7JdKJzLa7xvUCXfQOu2P6nAlvWgVbFH-kNZ3OHSoyVfC2YQdMih2PPFz0k4YSXr50IjYpi0MOXaidpFrWACRqJvegaVIgyHM2RRMpQoMUAge1d7B6FP3Ph0mSqdxUHpWOHTL5sLsOA0zOipwTXTMVx1yAdaWQ8TrS1BCzxwvdxMjIURVOB_HHhFX1MMJ1kK5kKJGjqnM1ViJPS3QBtTlUsZYdJ1dT8YbE1w6y4dSShbP5U2abyexm49M1Cr6oF7VPn_CkOzkO2OLrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QN655_2GxcVhXBn5rYIn5xangjTdnQIIn9cOz55ROX7iyBMomkuwaZcgLfaKcR5ZOBLNqWofLmtphtXbW1lVTpRJEfh6YEEQS9G0AE2UMVkO41kqoU5HD4y6_sCdGA9_cHOOluCqAwTPmr8hy3eA92wZ_-CLk_6jrXWYIqOc7HFTpXAnsTJoLXfxATX4tYi2dnTrn6iSSnaBLdUqfUXqYpqjXj4eT9H_tHWXbTyxXKv2UtT4O4eYrPqhLoUGjXvEj6JSdD6KcQ4KvRJZc4eFB3PVUJMRnO38v977n3Hf0PKInDLQfs592ywuBXaRKEahPhr3cAOo2Pojnfda52UFlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMarbP6KefT54UQk89M-I7y6Zmx0LgNHsLoxwWxtrmLWJ-ma9fFVdb7KXm1F7MDfcyFfrXXgv9fDKpUViQ28gz-DqMjnT9XIYOtR1a34xblyDe_D49EXWdd4lgoNBPwypaN-cFwtHItMeRLYlc5LH75J0NvLE2TltSQC1wAVA0cvnMzCFUw5P6Z7t5MaoM-MBftb7ajSO0qpdV54-cJuxh6fXvhI8_00-NEumbigcfTwkGLx0B_P6MVk8MWS2ZZPlGZX2EaeNsbxZoOtK-C-ENfCrSs4V1xEL0-quMJAkfpxh6cStJL91wIvA5abJOeG6FkeJKsKxxjFp1ReSt5FmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
یک کلیک، یک شلیک؛ صرفه‌جویی موشکی است که قلب دشمن را هدف می‌گیرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/akhbarefori/652994" target="_blank">📅 11:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652993">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
۸۲ درصد مردم طلای خود را در جنگ نفروختند!
🔹
گزارش یکی از پلتفرم‌های خریدوفروش طلای آب‌‌شده نشان می‌دهد بازار طلا در اسفند و فروردین، با وجود تنش‌های سیاسی و اقتصادی، بدون توقف به فعالیت خود ادامه داده است.
🔹
بر اساس این گزارش، ۸۲ درصد کاربران در این بازه دارایی خود را حفظ کرده‌اند و رفتار سرمایه‌گذاران بیشتر مبتنی بر مدیریت ریسک و تصمیم‌گیری منطقی بوده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/akhbarefori/652993" target="_blank">📅 11:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652992">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ایرانی‌ام؛ صدای مردم زیر بمباران تهران
🔹
این تصاویر برای اولین بار از جنگ تحمیلی سوم منتشر می شود
🔹
از صوت تماس‌های مردمی در زیر بمباران با مرکز ارتباطات ۱۱۵ اورژانس استان تهران و احیای قلبی-تنفسی وسط خیابان تا دستور متفاوت فرمانده به نیروهای عملیاتی!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/akhbarefori/652992" target="_blank">📅 11:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652991">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/771831b805.mp4?token=QvTAarAj25aza8_nO6gGRSydRhhbhbsY5RfWuZOychMAQBEk8k8A2NbAlRVzRDeeDeifgG5TJp7jhYOCZUNtUoAKc9D1UWVAO-v2rKde6mK29jx48wQA1ebFuIB_ZiF5j9axM7LwwFTNUcfHceyyIhLYphnvWmS3oaOxafX24eetlfSrqDkegt45M_6zYdLNI5BQPVXQLCeDydZlCjagh1sCfP-5nyGUM5XLC8kUAEXxDZaa7Ez1-VqEHPwpS4DxeOWlyB-elQ9HvtPXgh2RqiUC284wkXoLOqyFGgxC8232iMxNw6-Au1wosWGFhvdLmzXOTLMcql8qa1DmN9cKpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/771831b805.mp4?token=QvTAarAj25aza8_nO6gGRSydRhhbhbsY5RfWuZOychMAQBEk8k8A2NbAlRVzRDeeDeifgG5TJp7jhYOCZUNtUoAKc9D1UWVAO-v2rKde6mK29jx48wQA1ebFuIB_ZiF5j9axM7LwwFTNUcfHceyyIhLYphnvWmS3oaOxafX24eetlfSrqDkegt45M_6zYdLNI5BQPVXQLCeDydZlCjagh1sCfP-5nyGUM5XLC8kUAEXxDZaa7Ez1-VqEHPwpS4DxeOWlyB-elQ9HvtPXgh2RqiUC284wkXoLOqyFGgxC8232iMxNw6-Au1wosWGFhvdLmzXOTLMcql8qa1DmN9cKpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون بهداشت وزارت بهداشت: با سقط غیرقانونی جنین به شدت برخورد می‌کنیم و هیچ ملاحظه ای نداریم/ سقط جنین عمدتا در خانه‌ها انجام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/akhbarefori/652991" target="_blank">📅 11:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652990">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JO9B8nTw61VtFt6YPPHUNEcT2sCHfqdLysy9DfS_jrqqV-bfw-hHxZDg9FhSPnvwOsCnlKVfz3No6IGqd5tEgo5R-g026CwZY8YHnI3k7O9ec7CzjqheZ91euB8vWzC9tHtANW-Mu8K9UMvFwuMa3tRJ8Gq9AN20JbtuXisJvnlHSVDbm6KhuQ3e45KiE6irh7VgH8ZODG3gov1X4GbDaqVtuAKWAVdoDiyCP4GzB68gv9riOB2VuhdqmCfLHkg1B1y0fZvTi7f-r5Lrnn6RY-cG0mA9iZZBAC7pW_13ApEdmg1YLgTi08864UPym4pekpdHN9KOzg6UNlJQjtOV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه عبری معاریو گزارش داد، «نیروهای ذخیره اسرائیلی ناچار شده‌اند به مناطق اشغالی که مزارع پرورش ماهی دارند بروند تا تورهای ماهیگیری را جمع‌آوری کنند و بدین وسیله، از خود در برابر پهپادهای حزب‌الله محافظت نمایند.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/652990" target="_blank">📅 11:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652989">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWPqCV_Xed5xK4DfSnqa0NITwS0vwGQ8ANDmDNHYkjvUtrKvwDHzrT7JMpGGrgM5rWkfsYwhQSljyC6ymPAixOewBUTC62dYd1tukz2n9z1rslQC_7WkEO5dYLAzfsSYhd6upzzryw6_yDdVRdTgie7J3VEcSejQ9S0-MkWhI5UMBcRsymybdZ1xwJ0o25_VgVvwQ7HRM37E2pp0O5bhkofPGvhaksvVgjBcCs_W27WySbmpUhTnDsPWc9eDCWlC9AbaAzTATYStYoai86TYhJ1D7T6FyFRAm2bBTDiUxIkB6sg1MqkHlTd_utwM80JluZHGK7y-RMzPrTICpNjAVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ورود ۱۴۰۰ میلیارد تومانی پول حقیقی به بورس
🔹
امروز ۱۴۰۰ میلیارد تومان پول حقیقی به بورس وارد شد؛ صنایع غذایی، دارویی، سیمانی و زراعت با تکیه بر تورم و گزارش‌های مناسب، بیشترین تقاضا را جذب کردند. حقوقی‌ها عمدتاً از نمادهای بزرگ حمایت کردند.
🔹
در همین حال، منابع صندوق‌ها بیشتر صرف حمایت از نمادهای لیدر و بزرگ بازار شد که در صورت تداوم تحولات مثبت سیاسی، احتمال رونق سایر صنایع ریالی نیز وجود دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/akhbarefori/652989" target="_blank">📅 11:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652984">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aYE8ER167q5bFNTSqvvXNGgm5nXqu5xQuizhoiOfiB6gzZY760BSnIbZWseIziHtYTXznfbj2vQSN9TbQpVH3FvGXciwb5zBDaxE3GliaCLgkuW46OA_kR7TiBtgXwVypdeO1V27IJPAeuLuBoY6hy4gFD3Z7fy43QzdQ4kgfDikd41wd4lu_gdvxLdEDq-AJg6KbqjspH_hL9VZ6BWF4XVGNEwx-tzMa5rFHpG-D-R6WLIu5uxPxswbSVctFPLOzHxQAszmuULpE_m7rQnPcZPE6U15NnX318aPnMR5HJHxOqXuWGMZ-hMndRy7Ppq902Ro7Bb_rbUmhAp2Iov_pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rvkthz9eUhTr4laRP8fVle-o3rC0h4x7YzzAczh-fRPNM3bCEqGFqObU84nVrodnmVPZoYeDBgYMJ7Bb3Cqn7dL8GVhqaPgxJbdYhEdc-qRS_5cAstzWYegEeEF7sbh9-OEospp93j2d0Gxf18Ntn88692nLb6NKmAODcjaY5FHr1VEBR7EVQGePLx8wY8nS7I6AIvkC4WdLPLhzbdo9Ha7PX1xE9ofQZ4mFZ27FwhbnXKRKerbJMtbsuQaUoxkMW_ib-bqzDPJGcKVWMvG0wbNsLS98nXfrso_whmmYKEJqhNVinwphovGSsfmXGFhbwISYganFQwoVGQDHt61kBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iZainwJ9X5fP4t6joy3Dzoh609NDpdGNYcofm5ZF-p8h2F29xjUFXuk88EBr_eYh1ibJsTJrqIbnZ043WnpiPxHU1_X4u-0zYQFWRRINrKMU81jv4v7-H6XTAMvrlZtBFQ8pf6RqPbqvqGeVVyWDxckjGGYniKl37v68XETfYALYHB5_tJEOJ5hvDZDIgxCAbkekwz1mw5w-1cz3zzYuYn3UnPyULRYe6oBsKwpjfCwVhQsLcKofJHXDdF9LcjqezxDOgIGPU67FoKkHhfOG5Vq8LfTNUzclHRXNoCVw5LnPl_PEQp3N7fBEO-VNCaBpIM0kNy1_N4JS5apD7jh4gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gI0HRVEHx5qfVrQP9vZZxNhxSDwwwZ5wzbR6SBTN4Zukcxlwq01yPneeGzEnwthHDFapeg3WpjAjb5ogMFB5i5OQT17pybrHNj34wYwtH4eusWuWT3B5dOsubHdkSDRflI0xPH4vOSB5kxqzQcgMwmEkheocpAjKpI0TCLUM_Kw0lkK4_6dzJXzOl6GJMLP8K4gPp-G3-36-0SH-vo4JlmPw7g5M6luN0kwrk87Vt3K0xSWCIiiGy_swMxCBoLBLeSxDFecR7nwSUudVGIyzvCliOzTp2T3mtG1U9xgOvGJ8j9BUhfE8r7eroBiW9bXwlOQxQx_4JyDr25k3cfO45A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ojU7qWmtpYlRPTyX6ecuGy0EjBIS1R5oRVsLzlKh8123zjXY24ddDpMN7OZ_8f4GECMoJdStzMh2KvlhLG-DnKlmNuWqRsgSBJ9S_TT-DLqy1zz7VtpwypOpS2KnMGXR5JAZ3ei7bt1aNEl1evYRL97hV7_8hilltdwb2Zq-V1JvoSKwHeUMnO3INhUykVpEhP-0EyWMS2jmE2XreJYJZUJMpwHccWb8Lncsr2PvfvIaBmI2Uzi9TpGalyKOAKZk81nZnTQbyKxnd-f66c02dL96ftShoglPcwOQeE6yRLXp31vCU1lC3tj9AErHtOlF1z8TJzBWceSBq-KuAI7sKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
‌‌
پویش مردمی نه به پلاستیک
🔹
مخاطبین عزیز خبرفوری، همراهی شما در این مسیر می‌تواند گامی موثر و ارزشمند در کاهش مصرف پلاستیک و حفاظت از محیط زیست برای امروز و آینده کشورمان باشد.
شماهم به این پویش بپیوندید
👇
#نه_به_پلاستیک
@na_be_pelastic
@Alo_fori</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/akhbarefori/652984" target="_blank">📅 11:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652983">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOW-sOdtganvNQaoERHooLEriieWB2vP82zIfrNc-Tk149EAIs8LnJydnlcyOOzAS3JNPZBCVyOio9SQ0L-N9lrMIrRxw86JQe9ldbco5kW8MlsXX06N1SxqOUpE7_9nIdjXKiXd4iJERhd1mgUknDxOv1Dm1eqNZnTCaLxmfKh65joDCKZBtcdKBQ1dqOvyYF1JNBfjxMzBJpkSLYc1vjhJT68lOOyENHau2gzD6NDpQbaPlrginUhRV81ShCFdy_IBNZMslrgfUvswG2-J2Jh10smDzTEDobodaSFEiENjQ1sbPN1MDnb6ym_GNPp7ajOYahvHG-X4Zw2-SxejhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت الان بورس؛ بازار سهام فراتر از پیش‌بینی‌ها بود
🔹
بازار سهام امروز پس از ۸۰ روز وقفه، با وجود شروع پرفروش، با ورود ۱.۵ همتی نقدینگی حقیقی و ارزش معاملات خرد ۸ همتی، به روند مثبت بازگشت؛ به‌طوری‌که در حال حاضر ۵۰٪ نمادها مثبت و ۰٪ منفی هستند و گروه‌های فلزات اساسی، نفتی و سیمانی پیشتاز جذب نقدینگی‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/akhbarefori/652983" target="_blank">📅 11:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652982">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fv0rLgYYSIAybL3lzxPe0aSdLbPhYVcCTOCSAPbAZ_XCEji-Ii8xu9PiKTxxlhYvMXHKoq9yUylB3qq4Amk0b9qbMw_YhiAREgVZYnmd50C0wU-_gEjZ0lirWM1YjqhW06vyQIaVfA1t7BaH5oEC30BruIZUb1D1lWgICoWDo_GS3TS-SHbhjhJtwM3Y85gb0T_rj-_viRHlbMn9yj6KmlLrH1RD8C95QHnfkYT1LjUcqQl685VFmKkevl-VsqLCSTduuzOuPAm1ExU7aBYl2Klri_DNebdAXf9DKtqr9V1eQlTaVIsnKBDnCOLVoPIDGg9VuYGGGC1VuCUnolCxdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هزینه جنگ برای آمریکا از ۸۵ میلیارد هم عبور کرد
🔹
دونالد ترامپ بر خلاف ادعاهای انتخاباتی خود، نه تنها وضع مردم آمریکا را بهتر نکرده بلکه با به راه انداختن جنگ ایران، بیش از ۸۵ میلیارد دلار از محل مالیات این مردم را نیز صرف یک «جنگ انتخابی» کرده است.
🔹
سایت «Iran War Cost Tracker» پس از ۸۰ روز، هزینه جنگ ایران و حضور گسترده تجهیزات و نیروهای آمریکایی در منطقه را بالغ بر ۸۵ میلیارد و ۳۹۶ میلیون دلار برآورد کرده است.
🔹
این در حالی است که پیش‌تر جوئل هرست، یکی از مسئولان مالی پنتاگون در ۲۲ اردیبهشت، هزینه این جنگ را حدود ۲۹ میلیارد دلار تخمین زده بود. به اذعان سی‌ان‌ان، وزارت جنگ آمریکا از بیم انتقادات، رقم دقیق این هزینه‌ها را اعلام نمی‌کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/akhbarefori/652982" target="_blank">📅 11:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652981">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
۱۲ میلیون جوان در سن ازدواج
🔹
رئیسی، معاون بهداشت وزارت بهداشت: تعداد جوان‌های در سن ازدواج ۱۲ میلیون نفر است. برای این‌ افراد باید تسهیلاتی برای ازدواج در نظر گرفته شود نه صرفا فقط مالی یا اقتصادی.
🔹
کاهش نرخ باروری را اگر صرفا تقلیل بدهیم به اقتصاد، اشتباه استراتژیک است. خیلی از کشور‌های دنیا که وضعیت اقتصادی آنها مناسب است اما رشد جمعیتی پایینی دارند.
🔹
در کشور خودمان قسمت‌هایی که از نظر اقتصادی مشکلی ندارد کم فرزند هستند. بنابراین فقط اقتصاد نیست اقتصاد شرط لازم است اما کافی نه!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/akhbarefori/652981" target="_blank">📅 11:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652980">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5YJy-tR1xiplqFRWwoy4ijxCqQfb3uWPmrRnNPIANQ-CfJG8Wl6ZJkx75ZKJKYN-0GFHV2-vSOndchOd06yzpXp2VLoaLpRHlXLje8AjUzY3LKizopaJua2sfdjkA34uH7CTXaZx_KswGds6JOGnujq2SKiotDpNLxLXIjEdqvepTfB9f0FbWre1sdF0-vLq2hvRn6gQevPBsi1zL-1FHoGqilC7MT2TaAhSnb2MMtvEb13BFPItGxnJCMyRNKpk3yczLrKnapXdKnTKrxAVxWCSWYCR6vY0I_HqUKLhNLL_t9dFRaGczo7QxRQLVax6Pe29jGzMBRX4M1TsTOXVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توقف ۲۰ روزه کامیون‌ها در مرز بازرگان؛هزینه توقف ماهانه ۱۰ میلیون دلار
🔹
احسان ملک‌زاده،عضو انجمن شرکت‌های حمل‌ونقل بین‌المللی ایران با اشاره به توقف‌های طولانی، گفت: ایستایی کامیون‌ها در مرز بازرگان به ۲۰ روز رسیده و هزینه توقف ماهانه آنها ۱۰ میلیون دلار برآورد شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/akhbarefori/652980" target="_blank">📅 11:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652979">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7KUNBkxV7795NtLvx4nHMVGjxEcXiiR0O60mpRbe13j2DiEKOglX5A8zNz6ILsw-hXnF7EsY6ihdGbTZht5w8fzjbwquBcW-U8uixZSGvj_4ybuWsuOnB8PTXqupNWPJ88UVcvRyBq_z8LcBj0g_o7Ouvw72uyO-UhBUdySTQAp5d88NWQ_9T7CLBFp0gpXdEwHtguUV0PI1ObSmt4c2R9DX4reYf42fr6gUsihTrlxMChdx1KJu0McnRgA4YX8lMJQMHUgKRu4BsCaXGE7zzBHo1p8YeRc85MsILo5LJ4M3fh-DU1SWhUll0I1K0NAFZKVR5MTXQbTp0ztfkEw7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جشن بزرگ خانوادگی ازدواج حضرت علی (ع) و حضرت زهرا (س)
امروز؛ سه شنبه ۲۹ اردیبهشت از ساعت ۱۷
ورزشگاه شهید شیرودی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/akhbarefori/652979" target="_blank">📅 11:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652978">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zzm74eqatTFf4S3L8p6z-1CM0R7LQZYIBmGN4G4wD0v68ONNemNOVU44Ui9t1fSoTN1mKpaGxn5FMcF8evj5fBQPVN_Qt8R_n3NgyxuIs_6gN4HOrCWUeVNlY3DzL46v_NL28zcjxCat8FmV3CEoIZIGLIKlAMqK9NWshM-hqhzOfd9Tes7spiJ5oDetQJBDtNa1VfYLEcpXwDVEa8US_ZuC0x7UBc1CmGrqMYpHE4NrcexOeLdrKjiCO1sJqK-R8WqdssGOgAX5yKx_TUzgibO5A7qmrfxDBGspw-mdAxxDYgnPNkDz1f8UxCjHsvm_N367RHA5QjhcORUQId7huA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پتروشیمی خارک در سخت‌ترین شرایط عملیاتی به سود ۵ همتی رسید
شرکت پتروشیمی خارک در سال ۱۴۰۴، با وجود شرایط پیچیده ناشی از جنگ ۱۲ روزه، جنگ رمضان، کاهش خوراک، توقف حدود یک‌ماهه تولید و کاهش ظرفیت عملیاتی، موفق به ثبت حدود ۵ همت سود شد.
این عملکرد در حالی به ثبت رسید که شرایط خاص جغرافیایی و ژئوپلتیک جزیره خارک و همچنین تهدیدات دشمن با هدف تضعیف روحیه کارکنان، فشار مضاعفی بر روند فعالیت‌های عملیاتی شرکت وارد آورده بود.
با این حال، تلاش منسجم مدیران و کارکنان این شرکت موجب شد پتروشیمی خارک از این دوره دشوار با سربلندی عبور کرده و کارنامه‌ای درخشان را در سال ۱۴۰۴ از خود بجای گذارد.
ble.ir/join/4TiHhasUNE</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/akhbarefori/652978" target="_blank">📅 11:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652977">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntFcB8Ck8HreVrq-h4JhqIiYZ-cGMEdcL4jcyn9tbMgoCAoLZHyNsC0Z55UWl0vH4QPYj_-SvN2wEHvgRGbpCc39bnUCMLZpzfYBSJa53YXIM5uAmw-1ZOU5OiFsi_hpOEv-5lI9ggtqcxSBdR1fEWsUwpNiVml2qWE5prTTsuUwaagbk5QhjzDN9QYJc91LxOacyveKGvLRyb6UEkVaiJasszCGQRy-xoucs97GYqZ2DVG6kTY2mDFiw0vQJ_Yhv1-ty-MCjctqJIdGn24NwSvULUO9ml1VeiVuBE5kjDeQJGg2P2AgmVO1EiRyxDctkhNk1BmrEtQJ7_2texzCrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاید امروز بی‌خطر به نظر برسد، اما اثرش سال‌ها در زمین باقی می‌ماند
🔹
کمتر پلاستیک مصرف کنیم قبل از اینکه دیر شود.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/akhbarefori/652977" target="_blank">📅 11:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652976">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
کاهش نرخ باروری در کشور
🔹
رئیسی، معاون بهداشت وزارت بهداشت: نرخ باروری که در دهه‌های گذشته حدود ۶.۵ فرزند به ازای هر زن بود، در سال ۱۴۰۲ به ۱.۶ و در سال ۱۴۰۳ به ۱.۳۵ رسیده است؛ در حالی که نرخ جانشینی جمعیت در دنیا حدود ۲.۱ تعریف می‌شود.
🔹
در سال ۱۴۰۴ تعداد تولدها به ۸۹۲ هزار و ۲۶۸ مورد کاهش یافت و برای نخستین‌بار تعداد موالید به زیر ۹۰۰ هزار نفر رسید.
🔹
حدود ۶۰ درصد زایمان‌ها در کشور به روش سزارین انجام می‌شود و ۳۸.۵ درصد از این موارد مربوط به نخستین زایمان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/akhbarefori/652976" target="_blank">📅 10:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652975">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0kepPPBpkgLPDFLoZX4-oitoJn2uR2ZoxJ6Ea3uX79K006j671bNJdUipBK3h-YdgGG9Zz_mXsrwjrjxma5woJv4NiOfYOu8rOSoC8qLrC4K1n9dGqcAO3cgdKaPNTMvueiSHxzF4YzIdaM4G8AFySU59cInCwJK9ASOPddgTs4Yg7zFCgkNFj6tetVpPDpaP0e_E3_YzkxY2dOovYKmjN3ORtO-sOX03j_vlt0bhBPseKLh1_h2tiLsES1YrkSwaarQ3Gu_wG0_EKJkLjSYOHg6V3EJORUztXwteTZYojjUjrTsoGwtZvA8TVDhAo2mSijF0UWjdmtrXdwDDZTfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش حقوق بازنشستگان از خرداد ماه لحاظ می شود
🔹
شهریاری رییس کمیسیون بهداشت و درمان محلس: بازنشستگان درباره موضوع پرداخت و افزایش حقوق دغدغه هایی دارند که قرار است از خرداد افزایش حقوق بازنشستگان لحاظ شود ولی این موضوع به صورت درست اطلاع رسانی نشده بود.
🔹
مشکلات قیمت دارو وجود دارد که بعضی افزایش قیمت داروها غیرمنطقی است که بطور حتم در جلسه ای با سازمان غذا و دارو این موضوع را پیگیری خواهیم کرد
🔹
بیماران سرطانی و صعب العلاج در حوزه درمان و خرید دارو تحت فشار هستند که باید مشکلات آن ها حل و فصل شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/akhbarefori/652975" target="_blank">📅 10:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652974">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiGlx0TWmy1cyKzw4MyOfgAkRl1zK8nSPKm-eJJWGx8OjB3oeDWGOrtiAd0qY0FH3FrNvEQe6jhhGUQDO5jxxU0CBSHEvcgFmNJegbuoBQP7zERofVn6ZaGbFggKk-19RXgfDZjsT0gXmKfGMb5sEDsg5AFqIkkgbzICuvKmklsQoh6sNLkEJ2Vy3t-cxeOT0Uuvx3p2B6lUnULm57hUeOg_Uoki261UtcC8IBgd3tIrixUXWA9ND2WuXVeL4W7cm4QCPhnJatiHtV8qFYamWZ3BGvf3sz0i80E-1S5noqNaLlHRsX3DYHI_NpsQmpsU22KahBbYuGsVImfegM910Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸۵ درصد از ساختمان‌ها و زیرساخت‌های غزه ویران شده است
🔹
شورای موسوم به «صلح غزه» به شورای امنیت سازمان ملل: حدود ۸۵ درصد از ساختمان ها و زیرساخت های نوار غزه ویران شده و یا آسیب دیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/akhbarefori/652974" target="_blank">📅 10:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652973">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuAAccQV3V3zS6sprQ5AWvXwM8-HXuRzHFtV-v_Mt0zZAdeOBLAyOnHbJJnIiPFqog-54GHl5ATZCL0ULp8yrHwsTOIVMNWxujGiolckhb5Dzdz1dXW5HaSNatOetib9S5GfxnoeiYuK6t8P6GfFrC0L_0j0yXpDQVafIkXPKgyAuCLE_KYv9m58AkPmB-W6fQ2iSLYH-fXpKGR0stwQ7EENJ_GuRUcuCahcPh-CTibYIqYrW64E_onOlY9XnFlzD-WELer54Ode6IF34sdfMgyvpn_8zTEVGmoLY1Pt1rIqw8BthYHragrEn3odCrtsuRwYzAEQIl9qgpvm0eU89Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هزار کیلومتر مربع اشغالگری جدید از اکتبر ۲۰۲۳
🔹
روزنامه فایننشال تایمز گزارش داد که اسرائیل از عملیات طوفان الاقصی تاکنون هزار کیلومتر مربع به اشغالگری خود اضافه کرده است.
🔹
ارتش اسرائیل مناطقی را در نوار غزه، جنوب لبنان و سوریه تصرف کرده است. این میزان حدود ۵ درصد از مساحت اسرائیل در مرزهای سال ۱۹۴۹ آن است.
🔹
تقریباً نیمی از این مناطق اشغال شده در جنوب لبنان قرار دارد، جایی که نظامیان اسرائیلی به بهانه مقابله با حزب‌الله، یک منطقه امنیتی ایجاد کرده‌اند. بقیه این مناطق در نوار غزه و سوریه هستند.
🔹
به گفته این روزنامه انگلیسی، نیروهای اسرائیلی کنترل بیش از نیمی از نوار غزه را در دست دارند و مناطق حائل اضافی ایجاد کرده‌اند. در نتیجه، تقریباً دو میلیون نفر از ساکنان غزه اکنون تنها در ۴۰ درصد از قلمرو پیش از جنگ این منطقه فلسطینی زندگی می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/akhbarefori/652973" target="_blank">📅 10:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652972">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ایران ۸۶ میلیون نفری شد
🔹
رئیسی، معاون بهداشت وزارت بهداشت: بر اساس آخرین سرشماری، جمعیت کشور ۸۶ میلیون و ۵۶۴ هزار نفر است.
🔹
از این تعداد، ۴۳ میلیون و ۶۵۸ هزار نفر را مردان و ۴۲ میلیون و ۹۰۶ هزار نفر را زنان تشکیل می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/akhbarefori/652972" target="_blank">📅 10:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652971">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQ_LJsYjsCwbCn9u2ef-h04SdeoxNjV_MklOg8lkBnlUZSgZ4xfWGSOzQSUpmhxL4jiNn-bSYmyuqqqSkrhvN_GTmHRjpIJEOqFB-CQjZkETuudQ1W4-RliiVpWI8x7kdBoR99u3tK4UtXVbo_mjncUrS6Xsq2h7llbu82RXK5mOv3X9kG0mYfYLnlFAkHi2ECgF89GffNWEF0x_9bzM8mQwzcwlSvSa4g8EkbLDEkINBUW4nD16mcxIeCUNd5PWmUDkiyQHj-e9KK9eCp-C0NI_-lQMTM_nyVvVMDhVfCZ746G5VVTEeet4FxTR5Tdh1cbdqldiy9B5SyBlAGK4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مطالبات گندمکاران به زودی پرداخت می شود
🔹
وزیر جهاد کشاورزی: طبق مصوبه شورای هماهنگی اقتصادی دولت حداقل ۵۰ درصد مطالبات باید به‌زودی پرداخت شود.
🔹
کمبودی در تأمین نهاده‌ها وجود ندارد و حدود ۱.۵ میلیون تن نهاده برای عرضه در بازار موجود است.
🔹
حتی بخشی از چالش فعلی، مازاد عرضه نسبت به تقاضا است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/akhbarefori/652971" target="_blank">📅 10:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652970">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
دستگیری ۲ عنصر نفوذی در تهران در پوشش خبرنگار
🔹
فرماندهی انتظامی تهران: ماموران پلیس اطلاعات فاتب موفق به شناسایی و دستگیری ۲ عنصر نفوذی شدند که در غرب و شمال تهران فعالیت می‌کردند و خود را در پوشش خبرنگار معرفی می‌کردند.
🔹
این افراد با سوءاستفاده از پوشش رسانه‌ای، اقدام به جمع‌آوری و ارسال اطلاعات طبقه‌بندی‌شده مرتبط با مراکز حیاتی و حساس نظامی و اطلاعاتی کشور به شبکه‌های معاند نظام می‌کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/akhbarefori/652970" target="_blank">📅 10:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652969">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
پزشکیان: حمایت‌های معیشتی باید هدفمند و مبتنی بر افزایش قدرت خرید باشد
🔹
رئیس جمهور: حمایت‌های معیشتی باید هدفمند و مبتنی بر افزایش قدرت خرید دهک‌های پایین باشد.
🔹
اشتغال پایدار باید جایگزین سیاست صرف پرداخت بیمه بیکاری شود.
🔹
عبور از تبعات اقتصادی جنگ نیازمند برنامه‌ریزی ساختاری و بلندمدت است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/akhbarefori/652969" target="_blank">📅 10:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652968">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL2g2pIyUVGQGgneDCeqdtDAGwOXVbXCifAQhHvUAkHd5SXly5tLnevx954iZ2CXSJ-9AkLPk6Ckz8pFMSiL-Dma4Qnumd-kL2-Y20xOGXh2Z0R4XdHM6vdzkQpYHGoMa-iJHg0V_Xq5rlal5kmKqcOSyCm_bS0jmAVGS4TW0MZnMA1NMfrVIJj7sQjNgR36eJrwM-fFzvgOQxH_RrKlshkh7z-XSfaO2-LdUPvV6U2Dn94LsaIc3BRJqjrO72GIJS-qtCtwmlBF8ZBa8SGDB4oG5U4qoYhR81ju_Iz6KZAgEsO5ZsekZ63FqBHCzsL3-v17mPXeKJofsNkeoLwDOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دست‌هایی که زمین را خفه می‌کنند
🔹
پلاستیک فقط زباله نیست؛ زنجیری‌ست که به دست‌های ما بسته شده  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/akhbarefori/652968" target="_blank">📅 09:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652967">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mO1D_edofiMMGDxNDg7GKlR-cSFgMJdZFU-DrouzwvF3zL6Oxh_WZtsDX5M9qkrEh5DNdYenVzuJ231V06L-O7y2S-EFqgABSw308sj9tImBdHNbuzn81DyQxYx7m0Q1hbK7GgvVWtY88jM3BonNck_TTGqAAYxN2GIlUeYw42957_rPjr6l3IL8mTPh2vWrC19zND5McHUwsZ9XHQHhAsbQi6vVHGpTdRzo_Awxk36HoUoMbTSdLPqp9P8L_BHn8kqwpdvmqaIgIYBx1vjO2BfOSeYS65UO88sutNDP4famexnm7tNjy76FijxVWm2BPMNWKjz9iZmDT0Wym8W4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شورای آمریکایی «صلح در غزه»، بازسازی را به خلع سلاح حماس گره زد
🔹
آمریکا نهادی به نام شورای صلح در غزه راه‌اندازی کرد؛ نهادی که تا به امروز مجری اوامر صهیونیستها بوده و در راستای اجرای توطئه‌های آنان گام برداشته است.
🔹
این نهاد امروز گزارشی به شورای امنیت ارائه کرد و هیچ اشاره‌ یا انتقادی از تجاوزات اسرائیل در غزه نکرد.
🔹
شورای آمریکایی صلح با بیان اینکه بازسازی غزه نمی‌تواند قبل از خلع سلاح کامل با نظارت بین‌المللی آغاز شود، تصریح کرد: تعهداتی به ارزش ۱۷ میلیارد دلار برای بازسازی غزه دریافت کرده‌ایم.
🔹
در بیانیه این شورا بدون اشاره به نقض چند صد باره توافق آتش‌بس از سوی اسرائیل، گزارش داد: علی‌رغم چالش‌های مداوم، آتش‌بس در غزه به مدت ۷ ماه پابرجا مانده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/akhbarefori/652967" target="_blank">📅 09:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652966">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
پایان صف انتظار کارت ملی؛ صدور کارت‌های جدید تا آخر پاییز
🔹
رئیس سازمان ثبت احوال کشور: با برنامه ریزی و پیگیری های صورت گرفته، مصمم هستیم تا پایان پاییز ۱۴۰۵ معوقات کارت هوشمند ملی جبران گردد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/652966" target="_blank">📅 08:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652964">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPkbrTlgZ_iXr2lJDE6YVrdmnQ7hj-WTOYfV4Zay2tZvpHXv1oVhyzJC0XzVOPZ8rJ7gh2d2ihizPU6mOGkqeE4OJWx17Kh5VeoA1kUc_gQwP2JiuNzq2ftkpdv9vDVC0MesiorGbsUfpGC7jVDmEoIhcLLfPXWW0IUn8ENLqjSeLQXdb6tgROIoJ3XPBaYP7jk3e1XhfLyopy_AnMR9ip7Ym1VxQHCeWcXEOBaLVlNpICk94lPtRsWK-f9qr0tSrz615EZusHoUD2czGGGPfVAephcCBEYff45z8WlXAAQZ2SuPImwPOfPnly7HA9G2p3_C-AkUNdLGbiUl8CNChg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت بیان نشده از مذاکرات غیرمستقیم ایران و آمریکا در دولت شهید رئیسی توسط سخنگوی دولت سیزدهم
🔹
بهادری جهرمی: پس از حوادث سال ۱۴۰۱ امریکایی ها گفتند "وضعیت تغییر کرده".
🔹
در زمان های گذشته آمریکایی‌ها همیشه وضعیت داخلی ایران را می‌سنجیدند؛ وقتی خیابان به نفعشان بود، امتیاز بیشتری می‌خواستند.
🔹
امروز اما میدان و خیابان در وحدت حول محور ایران عزیز است. شرایط کاملاً متفاوت شده و قدرت ملی مردم ایران افزایش یافته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/akhbarefori/652964" target="_blank">📅 08:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652963">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
وصول بیش از ۱۳۹ همت مالیات معوق و مطالبات دولتی
🔹
صالحی، دادستان تهران: بیش از ۱۳۹ هزار میلیارد تومان مالیات معوق و مطالبات دولتی شامل سود سهم خزانه، عوارض ارزش افزوده، عوارض سبز و معوقات مالیاتی با نظارت این دادستانی وصول شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/akhbarefori/652963" target="_blank">📅 08:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652962">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس : هرگونه تجاوز جدید علیه ایران با پاسخ قوی‌تر مواجه خواهد شد و ترامپ را شرمسارتر خواهد کرد
🔹
ابراهیم رضایی : هرگونه تجاوزی علیه ایران با پاسخی قوی‌تر مواجه خواهد شد و ما برای همه سناریوها آماده‌ایم
🔹
آمریکایی‌ها یا باید تسلیم دیپلماسی و شرایط ما شوند یا تسلیم قدرت موشک‌های ما.
🔹
تاریخ تنگه هرمز هرگز به حالت سابق خود باز نخواهد گشت و هیچ قدرتی نمی‌تواند آن را بدون رضایت ما باز کند
🔹
ما در حال اجرای یک چارچوب قانونی جدید هستیم که توسط مجلس تصویب خواهد شد تا تنگه هرمز را مدیریت کند تحت این چارچوب، کشتی‌های دشمن اجازه عبور از آن را نخواهند داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/akhbarefori/652962" target="_blank">📅 07:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652961">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">قسمت بیست‌و‌دوم - پادکست کافئین</div>
  <div class="tg-doc-extra">بابک خرّمدین</div>
</div>
<a href="https://t.me/akhbarefori/652961" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
بابک خرمدین
🗓
در لحظه‌یِ ورشکستگی و شکستِ قطعی، چطور «برندِ شخصی» و غرورِ حرفه‌ایمان را حفظ کنیم تا رقیب رنگ‌باختنِ ما را نبیند؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/akhbarefori/652961" target="_blank">📅 07:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652960">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69594ee11e.mp4?token=AT53pbk_2_UAFYBTCWaOd3Q1za7fdQLTLkeEkdbQjOqBMubxbYykxqsTE8SjrnHHK4FK3NepDEM_igKkTXFH9POXGk7LbaFAB_79cr320_o_bcjUFvH01bBjDHS6OjIeMG0VpH2ZBQZTe-7qfaLMhKEfqB_prvmW7t43Tf6YH_6yUc3EuBSmsVVJ--oT3qSdLWRq4e-szORRYnU6Wg4i-RpJbcDOCquRsOKxxFE6tJVhyNm8OWEocvPiU-t-7I2J0IOfx4L4be06ZLsILGpmVlI0L0ORKEY686unHSs7Ow7na2_NQyz3NAgIdR59vwgzlEGaKKpezn1Y5HP_chGNeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69594ee11e.mp4?token=AT53pbk_2_UAFYBTCWaOd3Q1za7fdQLTLkeEkdbQjOqBMubxbYykxqsTE8SjrnHHK4FK3NepDEM_igKkTXFH9POXGk7LbaFAB_79cr320_o_bcjUFvH01bBjDHS6OjIeMG0VpH2ZBQZTe-7qfaLMhKEfqB_prvmW7t43Tf6YH_6yUc3EuBSmsVVJ--oT3qSdLWRq4e-szORRYnU6Wg4i-RpJbcDOCquRsOKxxFE6tJVhyNm8OWEocvPiU-t-7I2J0IOfx4L4be06ZLsILGpmVlI0L0ORKEY686unHSs7Ow7na2_NQyz3NAgIdR59vwgzlEGaKKpezn1Y5HP_chGNeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بابک خُرّمدین، رهبر سُرخ جامگان
#پادکست_کافئین
| قسمت بیست‌و‌دوم
☕️
در این اپیزود به سراغِ مردی رفتیم که ۲۲ سال تمام، ماشینِ جنگیِ یکی از بزرگترین امپراتوریِ جهان (خلافت عباسی) را زمین‌گیر کرد. بابک خرمدین بودجه و ارتش کلاسیک نداشت، اما «معمارِ جنگِ نامتقارن» بود.
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtube.com/@caffeinepodcast2025?si=CNnq-Y7JNjOTm0Z_
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/akhbarefori/652960" target="_blank">📅 07:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652959">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUpplu9mx0c9yHPyI53SRHK3Pp1MGOkCs4UjzoQnlCHvGImIfvVtaGEBeL8cOHbggAv6rYqdlf_hB_wiEpbGk_D8FfOyI7-UEvuZjmdob4LLgDxf8PXV0ZPaPUGCt2VGLTkauqfcrj3AaN-_QWc7l6zau58YtA6CSAx3v9R7HHv7eko1i-1s_pWms-GImwBRTns6rBOF5XFuuWE8vFhRXU_VwY48b1iRYJM8dLJVFToKu6A1MRQxvWjhvNOlhNqe1LkgM8uLAhWseH1BP8p5IxB9cdzxP9GWYjODfdtKnSO539xeYKPVRzf82-NvbG_vIrO5X1NdTP549nXQOs6JSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۲۹ اردیبهشت ماه
۲ ذی‌الحجه ‌۱۴۴۷
۱۹ می ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/akhbarefori/652959" target="_blank">📅 07:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652958">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlRtDB2sAPCrhTQJ2cvPcCxNRPlP4VEZakHwSOtGqFi91tCkswIgDBkuqAW5MDtcQBK87Q2ehjzccHxCV7RtY7VKnR17oMyAXtRLfnXRpAteasBYAmbzn7FTJ7Q_HwdtkTIhFbKy1oJuEvDyWL8XbY3LROAAL8tt0NlImy05i5-q8HujL4CJlKxMrUQt61mtPFEcaeVs9pHkAYrs98gopmubbIaK2QaDmRNoX8AFP97F-Woqsd9Y5tTYO41rQJo_35QW0ZhjhfNFZKdon5ug1uB5tGvm818PL01C_BqHOik4ZZ79I9lvEN__CiUmD2fHdoSFmxDz0BEXgkeYfNaSJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: رفتارها و زیاده‌خواهی آمریکا مانع جدی در مسیر دیپلماسی است
🔹
وزیر امور خارجه در دیدار وزیر کشور پاکستان رفتارها و مواضع متناقض و زیاده‌خواهانه آمریکا را مانعی جدی در مسیر دیپلماسی خواند و گفت: در عین جدیت برای دیپلماسی، از هیچ اقدامی برای ارتقای آمادگی‌های خود جهت دفاع از امنیت و منافع ملی ایران فروگذار نخواهیم کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/akhbarefori/652958" target="_blank">📅 06:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652957">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
آماده‌باش اضطراری ۸۰ کشور جهان در پی بحران انرژی ناشی از جنگ علیه ایران
🔹
روزنامه فاینشنال تایمز:
🔹
در حالی که جهان به دلیل جنگ علیه ایران با مرحله بسیار خطرناکی از بحران انرژی روبرو می‌شود، نزدیک به ۸۰ کشور برای حفظ اقتصاد خود، دست به اقدامات اضطراری زده‌اند.
🔹
کارشناسان هشدار می‌دهند در صورت ادامه توقف و اختلال در صادرات نفت از طریق تنگه هرمز، بهای نفت جهش شدید و بی‌سابقه دیگری را تجربه خواهد کرد.
🔹
به ‌نقل از اقتصاددان ارشد شرکت سرمایه‌گذاری «آبردین» نوشت: ما در حال بررسی و تحلیل سناریویی هستیم که در آن قیمت نفت خام برنت به ۱۸۰ دلار در هر بشکه می‌رسد؛ اتفاقی که می‌تواند صعود شدید تورم و رکود سنگین را در کشورهای مختلف به همراه داشته باشد.
🔹
از زمان آغاز جنگ علیه ایران، ذخایر راهبردی نفت در جهان نزدیک به ۳۸۰ میلیون بشکه کاهش یافته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/akhbarefori/652957" target="_blank">📅 06:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652956">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
مقامات صهیونیست در صف صدور حکم بازداشت دادگاه لاهه به اتهام جنایت جنگی
🔹
کانال ۱۲ تلویزیون رژیم صهیونیستی فاش کرد که پیش بینی می شود دیوان کیفری بین‌المللی در لاهه به زودی احکام جلب و بازداشت جدیدی را علیه مقامات کلیدی کابینه رژیم صهیونیستی صادر کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/akhbarefori/652956" target="_blank">📅 06:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652955">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AouiEGUiwIDD539lUd0WCq0FzFpenPuPFzeAJXiBln2wy0LaQBXveq0KjcVcGjBFyWAmriGj1odCmKnvsomtZXzr6M-x_yRnj5HMX06t9_Rjbrw76NGWAr1POgQevyESa6kSuZdauHbttkK-sgcqbzpyNmSmBkkJwEd3b8fEouQeANadgZgZLx4Jrja2al61bQpub_dZlMYFjZW2wqFn0EteMymS1sAMbtn87BROolgtGkqeStVc5riCcFFBeWqDQTGmY78tcwRwC8oSgna_3J0A8hAao2kTYsjRvmoascEtkvsCM3HqzNLAxlCNcAE8LOm_te55c2ZBhEjEyQCvUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصر دست اسرائیل را از دریای سرخ کوتاه کرد
🔹
طرح اسرائیل برای تسلط بر دریای سرخ با کریدور زمینی مصر نقش بر آب شد. قاهره با همکاری اریتره، مسیر لجستیکی از مدیترانه به شرق آفریقا ایجاد کرد و نفوذ تل‌آویو در منطقه را شکست.
🔹
این پروژه که بنادر اسکندریه و سوئز را از طریق خاک سودان به بنادر اریتره متصل می‌سازد، عملاً حلقۀ محاصرۀ اقتصادی و لجستیکی اسرائیل در شرق آفریقا را تکمیل کرده و طرح‌های تل‌آویو برای تسلط بر کریدورهای تجاری دریای سرخ را برای همیشه خنثی می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/akhbarefori/652955" target="_blank">📅 05:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652954">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIdHLK4KvKnNMtJbAaNAtDoCBLVhFwySPMmYnskeDHdJFjZXeJ0spKiL7BgkHo-2TwgXZ8X77SaPtOepxFjVN0fhaejNXPe4zQLrc2OyMzcYDb6L02NSKrB5NlYoL3ctwDPZUyHBKn3dzdOpfYMJdGzJ45ZXbB1kLte_JzMofjzAKGBIVVHydoZifcqMRf4kS6uftoPEg3d96bycQeJXpoWwvXVaByTl1sIIi9_wGkrfMU_Bfr_ZMlLn7z_sLkCvzt6FQOk7PUIfZz7XYTk21SfO9NJvMZQwdFoZntYwZ01PTTsRe_KxlC3MtuqqxwdgUsEwm-3VB-rc1QQ4uSIS4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر کشور پاکستان حامل پیام تهدید و اولتیماتوم ۴۸ساعته ترامپ بود. او عصر دوشنبه از ایران خارج و احتمال جنگ تشدید شد اما ترامپ مجدداً عقب‌نشینی کرد و این‌بار تاکو به اسم سران سعودی، قطر و امارات فاکتور شد
🔹
البته در ایران هیچ اعتمادی به حرف جنایتکار نیست و دستها روی ماشه است.
🔹
احسان صالحی، کارشناس مسائل سیاسی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/akhbarefori/652954" target="_blank">📅 05:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652953">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
واشنگتن: توافق با ایران از مذاکرات لبنان جدا است
🔹
«تامی پیگوت» معاون سخنگوی وزارت خارجه آمریکا شامگاه دوشنبه در مصاحبه با شبکه «الجزیره» گفت که واشنگتن توافقی می‌خواهد که ذیل آن ایران سلاح هسته‌ای نداشته باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/652953" target="_blank">📅 04:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652952">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHL0A-rmYQk40CkxubsqbHVsYoiidEH1w0COwGz-Tv4Miwov_0ZU4t8kya8ssp2m57hYORBtPbNHzUDAopP1nNKW2c8DbU7hAzZVy_u_c5Ou6BSZ2Vs4ioaUr6EqodM8PjJoXlOZxGHsuSgCU4_GndtRarD3U_J2k2qWf-NQjJ2uc6IZRuFKfcVvCCCzKsYHFRXpCEOHICeTb03znFUxDzORCZODZyrQMpwvLwRWnQ3-IpaNpiYBG0bnaImb1Oavd94nDCM29NnRN0dZe8-u7qQK_xUk_zIdsCc9X6Aosj3SMcUmKfdZnn0QEIBKjxQwkJM3qHzyjEfLHWNYTZAlHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقام پاکستانی: ایران می‌خواهد ابتدا جنگ پایان یابد
🔹
روزنامه «واشنگتن‌پست» بامداد سه‌شنبه نوشت که ایران می‌خواهد قبل از توافق هسته‌ای با آمریکا، پایان جنگ اعلام شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/akhbarefori/652952" target="_blank">📅 03:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652951">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85aaf7da50.mp4?token=H06ewTxjWNP9YB4mx8mZql0VC74Bc2MYC2nSlI6fOHBuLLpz0Wlx6pW1F9OdrQYEWde4vy9rcs-Ol4UNjGSTeZ68mdo_KuSXbllR5dPUgHy1_rzUz-OzH8E6-_A7MAY-ERQLIL7Kba78JXe-tB_P3lYKZINaxPiZVymhI2Qi_BdzRvT4_RK9dz0Xp2u7cYeHDrNa48suFH94TEzYAHLlb6pLiJ0vP-4F3I50F3yJG7SR1JAtMiqhZIMNSwkm52-nABuu3fmEm3HD0ZGSwgKCoMEHJ8-2UNvP7a8EBKJYmS4otKMrsKyco7BpmTLovDlu_s49UN-5dz-ODDOe153hLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85aaf7da50.mp4?token=H06ewTxjWNP9YB4mx8mZql0VC74Bc2MYC2nSlI6fOHBuLLpz0Wlx6pW1F9OdrQYEWde4vy9rcs-Ol4UNjGSTeZ68mdo_KuSXbllR5dPUgHy1_rzUz-OzH8E6-_A7MAY-ERQLIL7Kba78JXe-tB_P3lYKZINaxPiZVymhI2Qi_BdzRvT4_RK9dz0Xp2u7cYeHDrNa48suFH94TEzYAHLlb6pLiJ0vP-4F3I50F3yJG7SR1JAtMiqhZIMNSwkm52-nABuu3fmEm3HD0ZGSwgKCoMEHJ8-2UNvP7a8EBKJYmS4otKMrsKyco7BpmTLovDlu_s49UN-5dz-ODDOe153hLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اسکات بسنت، وزیر خزانه‌داری آمریکا در جریان نشست گروه هفت در پاریس از اعضا درخواست کرد که با پیوستن به تحریم‌ها، منابع مالی ایران را از بین ببرند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/akhbarefori/652951" target="_blank">📅 03:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652950">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2879a3ef4e.mp4?token=ZkqD48aOHnAdeBRQnz3BdR7kKjVrG146jRX-UiT7zWmjCno5YcCk-GWM7a90PuDYNvE9ychSi-sxInJXgOBP6y2yDXoFFBq_dO5cYTykyeljfx690GFhvbTKqe9gok2uq7EVD8H4N_lyILco9TpWH0yEPhpGLRWoiZ_z-cAcTFi9jIDfwzdzWs7nry7h5rJKElSz22JaTykTFRM-EWpJaF_PAMeOMZgiQ06O9OL0GqRWKbPtHHd2yo6am0ChBjbucvSuTN20dd5XgUcrxojKOLRXksrUMIVQlkZB1PjkDiZ1rPD3Vk1EyDDKXM3xyXVZrMfbFQAMdxOdP7xHtOliSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2879a3ef4e.mp4?token=ZkqD48aOHnAdeBRQnz3BdR7kKjVrG146jRX-UiT7zWmjCno5YcCk-GWM7a90PuDYNvE9ychSi-sxInJXgOBP6y2yDXoFFBq_dO5cYTykyeljfx690GFhvbTKqe9gok2uq7EVD8H4N_lyILco9TpWH0yEPhpGLRWoiZ_z-cAcTFi9jIDfwzdzWs7nry7h5rJKElSz22JaTykTFRM-EWpJaF_PAMeOMZgiQ06O9OL0GqRWKbPtHHd2yo6am0ChBjbucvSuTN20dd5XgUcrxojKOLRXksrUMIVQlkZB1PjkDiZ1rPD3Vk1EyDDKXM3xyXVZrMfbFQAMdxOdP7xHtOliSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه‌هایی از بمباران مجتمع مسکونی در منطقه «المعشوق»، صور (جنوب لبنان)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/akhbarefori/652950" target="_blank">📅 02:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652949">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNmICAig8JSaLoIox_Jp4UlQ1hcIFzFZZlIxZZNCdTk0tSAVJb17MNRhz-IHHFJmtKYotUEc-eoMowbBQ-8nW56sGDH5FnB3jiQZ7INz8sgbOaM6am3xOsfKMuEScVV4XQQMTwWC0rNfCTW4f4ZRs7l7I1y8YBa5bhVx11xNJxAaYQWOvS7Rgq75zdwHoFyb30c6CwP7zFTanEK0nOT64D7LphjabCdGG7mwv2f5vdJCyGcfUWVzXtkkfThkOm8-CK5bCB2IcSGRujQJShjQJTV2kgRI10TTSbzNVLsL9vkNpvcy34X7V4QKHNKZwXmq47fEtNF8C1w5HsQ6eS82fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میدل‌ایست مانیتور: شکست‌نخوردن ایران در جنگ، واقعیتی است که آمریکا و اسرائیل نمی‌توانند آن را تغییر دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/akhbarefori/652949" target="_blank">📅 02:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652948">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
اردوغان: جنگ علیه ایران منطقه را در لبه پرتگاه هرج و مرج قرار داده است
🔹
رجب طیب اردوغان، رئیس‌جمهور ترکیه، پس از پایان نشست هیئت دولت در کاخ ریاست‌جمهوری در آنکارا، تأکید کرد: جنگ ۲۸ فوریه (۹ اسفندماه) آمریکا و اسرائیل علیه ایران، منطقه را در لبه پرتگاه و آستانه یک هرج‌ومرج و نابسامانی مطلق قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/652948" target="_blank">📅 01:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652947">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXtIKk5inqg8JSdEqGt3cjeh54naP-ITGufpRKIc8RA9yJiKVFNhFwwiqzWLqx4rj5c-W0LSEsQphBgCvhSMqL_3nQwuWOGC0SsqcFFbYBs5qa8DxciJspIjL2KqdYt8NOxoQfHlIlPosfjtq4rKqshWqLDKxFnQszHlR_uY0vJp7046YDD_u6VLwF4hnS7-kDdiBbEpQDEYJ7Gp5DBnnAjnrAJQGxfEY1Yb62o5BB1l-8s_kjaRKgGgDLCXkFRRruUOs8_ftREkeD2eoYdalWRlCExK0YU9-lBKqbwkHsjSq2QH2R_k_6UFsjBxi1PkoU-3Ltt5CpwdWXn6RBwR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ گزینه نظامی خوبی برای تمام‌کردن کار در ایران ندارد
🔹
ارزیابی کلی این است که هیچ یک از گزینه‌های نظامی موجود چه حمله گسترده، چه هدف‌گیری رهبران و چه عملیات زمینی یا دریایی، راه‌حل قابل‌ اعتماد و کم‌ هزینه‌ای ارائه نمی‌دهد و مسیر منطقی‌تر، حرکت به سمت توافق و کاهش تنش است، زیرا در غیر این صورت خطر ورود به سناریویی بسیار پرهزینه و غیرقابل کنترل برای همه طرف‌ها وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/652947" target="_blank">📅 01:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652946">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
هشدار فرمانده قرارگاه خاتم الانبیا به آمریکا و هم‌پیمانان در صورت مرتکب شدن دوباره اشتباه راهبردی درباره ایران
🔹
سرلشکر عبداللهی: به آمریکا و هم‌پیمانان آن اعلام می‌کنیم دوباره مرتکب اشتباه راهبردی و خطای محاسباتی نشوند
🔹
آن‌ها باید بدانند ایران اسلامی و نیروهای مسلح آن نسبت به گذشته آماده‌تر و قوی‌تر، دست بر ماشه هستند و هرگونه تعرض و تجاوز مجددی از سوی دشمنان سرزمین و ملت سربلند را سریع، قاطع، پرقدرت و گسترده پاسخ خواهند داد.
🔹
دشمنان آمریکایی-صهیونیستی بارها ملت شجاع ایران و نیروهای مسلح مقتدر آن را آزموده‌اند.
🔹
ما با عزم و اراده الهی ثابت کرده‌ایم که اقتدار و توانایی خود را در میدان عمل به دشمنان نشان می‌دهیم و چنانچه خطای دیگری از سوی دشمنانمان سر بزند با قدرت و توانایی به مراتب بالاتر از جنگ تحمیلی رمضان با آن برخورد خواهیم نمود و با تمام توان از حقوق ملت ایران دفاع می‌کنیم و دست هر متجاوزی را قطع می‌کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/652946" target="_blank">📅 01:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652945">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHo-c9g7RlsI_N1HYFx_Yhpu1WKh3TrNB6Gu7RAmgq48v5bREvizR65LvvwMboIZwk2LDPdi0VpEfpO54TG5XXbkt_OlteJR1OmCAoLsVCeBwOxKNY5wB4rtN6lCcaPDz6CrVGtNeZfCEStsicuuh4v8872zRMi4jTzpaHaStiS_MjfK66igBaT6EwdWoZTIimsz1RXy8YJSzhFOZKmBDKOODwwTy054rlusdZw7aGFD5T2T5hVORm9z-q2zGuHh71ksrkbEecI6NFxEmjfJ6KgWfQx0rBE2trwDKDLrGxJ4izP--AEo9gvYN9QeAGD0Mul_Qqes9zoIwGl-lIUjPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صدور حکم بازداشت وزیر صهیونیست توسط دادگاه لاهه
🔹
دادگاه کیفری بین‌المللی شامگاه دوشنبه حکم بازداشت «بتزلل اسموتریچ» وزیر دارایی رژیم صهیونیستی را به دلیل جنایات علیه بشریت، جنایات جنگی و جنایت نژادپرستی صادر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/652945" target="_blank">📅 00:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652944">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
خبرنگار صهیونیستِ مورد علاقهٔ ترامپ می‌گوید عقب‌نشینی‌های ترامپ، «دستکم ۶ مرتبه» بوده!
🔹
باراک راوید، جاسوس‌‌خبرنگار مورد علاقه ترامپ در وبسایت آکسیوس نوشت: ترامپ از زمان شروع جنگ حداقل ۱۲ بار ضرب الاجل‌ها را تمدید کرده و حملات برنامه‌ریزی شده به ایران را به تعویق انداخته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/akhbarefori/652944" target="_blank">📅 00:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652943">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApBFTe6-oK2hWCf0wJak1H1zc9YR7KgERsyk0hC11RJPICA18ErWkZEJSveUMVS2WrrCghji0smPWSN-D-3uGAQAIYF3dFFvmthQqMmIUGmdOJUYYNTjdN-RAFyGvFzpqEzXhFYPo_WV8ZGpjtVb6Og2xrZiH22Tp0mRrNmJR3vvmzS0nUWdazaIRQxuEBSji9NU64mux0reOHJ0eVTrz7_SPCZGuMthlTZ29tTBaGnctCY5n8DqMRd-s59iz4R8R_jx8nuvAJEmewmN7bno4Q_a3KxdJHNEgs-Vyu1_Wiwg1S2QBR9iJtoVzONXeFfiHFhajs4Kj39FRQlwePq2ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حقه کثیف ترامپ در اعلام تعلیق حمله به ایران/ این عدد همه چیز را لو می دهد!
🔹
بسیاری معتقدند خبر ترامپ درباره تعلیق حمله قریب الوقوع به ایران حقه ای است برای کاهش قیمت نفت.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3216090</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/652943" target="_blank">📅 00:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652942">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
حمله مسلحانه به مرکز اسلامی در آمریکا؛ ۵نفر کشته شدند
🔹
رسانه‌های آمریکایی از وقوع یک حمله مسلحانه به مرکز اسلامی شهر سان‌دیه‌گو در ایالت کالیفرنیا و کشته شدن ۵ نفر از جمله دو فرد مظنون در این حادثه خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/akhbarefori/652942" target="_blank">📅 00:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652941">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2iEfSzyVdu6b-CPqIp7AfOPkDZ2BXjKlsVScssSurOcziPKy4BJL8xaqNsGPJmf2a-LNOnmaFgvyY9Sx-b0FGm-6VmTNlaS0zwJ5BkR1td0tDvsYOUIUikxqmyRhoxjreXTgqa7jeTNKkR58n1be4Cw_-XaJCBw4K1xEkeYRlwf2Aq6KZszMmKnij2FDe8H-jmngW5p-QszFhcAPcJuW3RWHe_rxE7mbX34-CqkQDn0j6fwb3kTh0_P0RGDz92O-Vr0p3eXqM1hU5nerBcmGUshrZRPom68NA_yWW03hMsdaVHYD3abpDM-vzIGoCEn2NgeBIR1thHi2FshXkSEkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان مدعی شد: پلیس معتقد است دو مردی که در نزدیکی مرکز اسلامی سن دیگو پیدا شده و ظاهراً بر اثر شلیک گلوله خودکشی کرده‌اند، از مظنونان حمله بوده‌اند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/652941" target="_blank">📅 00:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652940">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
الجزیره به نقل از یکی از مقامات تروریست‌های کومله: مقر ما در استان سلیمانیه با ۴ موشک ایرانی مورد حمله قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/652940" target="_blank">📅 00:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652939">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-text">♦️
خیام را با صدای شما روایت می‌کنیم...
🔹
در روز بزرگداشت خیام ، صدای همراهان خبرفوری را می‌شنویم؛ روایت‌هایی کوتاه از خاطره، شعر و نگاه به زندگی از دریچه رباعیات خیام.
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/652939" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652937">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔹
از خبرها و تحلیل‌های جنجالی امروز غافل نمانید
🔹
🔹
حمله دشمن به قشم| پدافند جزیره فعال شد
👇
khabarfoori.com/fa/tiny/news-3216073
🔹
ترامپ بازهم عقب‌نشینی کرد؛ حمله برنامه‌ریزی شده فردا به ایران را عقب انداختم!
👇
khabarfoori.com/fa/tiny/news-3216054
🔹
جزئیات تازه دو پایگاه مخفی اسرائیل در عراق | چوپانی که پایگاه را کشف کرد و کشته شد | عراق واقعا از حضور اسرائیل بی‌خبر بوده؟
👇
khabarfoori.com/fa/tiny/news-3215932
🔹
چرا مردان در محل کار زنان را مورد آزار جنسی قرار می‌دهند؟ | علم دو توضیح ارائه می‌دهد
👇
khabarfoori.com/fa/tiny/news-3216010
🔹
پیشنهاد تازه تهران چرا واشنگتن را راضی نکرد؟
👇
khabarfoori.com/fa/tiny/news-3216058
🔹
در آپارات خبرفوری، ویدئوهای خبرساز را ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/652937" target="_blank">📅 23:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652936">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fedf38b8c.mp4?token=HJlqQwWM6iDyoZ9sSgNQ_rQ42XHyFLkyTtHzyd7vB08BQ7Uhtr7wv_cwAtwjDZP-N_9xGhOp9ErztvdcdTGjt4l838vZz_IjTIK7ZldDT5yparo5i9HHrDBAPA77W0Nt0tJyA86V5JdzR4u87m1rENVmKLAaOTXFAMrsINIIiEiukRohg_Yhdjbl7Foz6cexQNdU6TS_4DYF2t7lU-6V38XQ8ES3CmKzoPb62hW9GMwQaBTrv5wTU3uePORJaDOsBWqqFEBUqczb1-TfGhprapmtnJIVZ1fI2OdvOwmtkRdXtSdbSywMoym1EIh9ND37lWvaf7KdJoo4x0DThHm5WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fedf38b8c.mp4?token=HJlqQwWM6iDyoZ9sSgNQ_rQ42XHyFLkyTtHzyd7vB08BQ7Uhtr7wv_cwAtwjDZP-N_9xGhOp9ErztvdcdTGjt4l838vZz_IjTIK7ZldDT5yparo5i9HHrDBAPA77W0Nt0tJyA86V5JdzR4u87m1rENVmKLAaOTXFAMrsINIIiEiukRohg_Yhdjbl7Foz6cexQNdU6TS_4DYF2t7lU-6V38XQ8ES3CmKzoPb62hW9GMwQaBTrv5wTU3uePORJaDOsBWqqFEBUqczb1-TfGhprapmtnJIVZ1fI2OdvOwmtkRdXtSdbSywMoym1EIh9ND37lWvaf7KdJoo4x0DThHm5WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محدودسازی هوشمند جایگزین خاموشی برق خانگی می‌شود
🔹
وزیر نیرو: سیاست وزارت نیرو، مدیریت هوشمند مصرف و افزایش ظرفیت تولید برق است تا تابستان امسال با کمترین دشواری و بدون خاموشی گسترده سپری شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/akhbarefori/652936" target="_blank">📅 23:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652935">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1aWMnHjaTxWxKmv7ZbcijbenTjGxYFHM7_pJE7sTaM4FFe23m1ypAnOkL0R-_MCWUK4AmZ1v6QcYCA28MtOiETKAj9jrQnnIoHFy-BkCdU-w4gpYVVBXIvgrlqshz_F0-rqOY44wQjX6izjbKbzqyxyqeBjPqf7OpYLhgPL3eU6t-DJxkEK18Z9iFKjWNyMsLpdMFLlqd2MxEhdZmDlzFcLA5xPgSAcNVASPUHDToamhgMpW4YER4CRUgc0QZ38RSZiiQ22jJw9umcY3iIKk902AI6ifPh6IHvJAoIWmdV9vDOIdi_2sOQnY8oRgXN6iCc0HWBQhSfJ43sahxt8LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اردوغان: جنگ علیه ایران موجب افزایش تورم کشورهای جهان شده است
🔹
رئیس‌جمهور ترکیه: پس‌لرزه‌های بحرانی که با حملات به ایران آغاز شد، در بسیاری از مناطق ادامه دارد.
🔹
ما با یک عدم قطعیت چندوجهی روبرو هستیم، قیمت سوخت هنوز ناپایدار است، تورم در بسیاری از کشورهای جهان افزایش یافته، اختلالات زنجیره تامین هنوز ترمیم نیافته و انسداد تنگه هرمز هنوز برطرف نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/652935" target="_blank">📅 23:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652934">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHnzbspP-sh4F6SYGLQIIEnEPyoptm9B1WxRi7zlKEMJQFsa-0iU_K6c8XEJW3YujwAF3vzALhYA5bpQhqurLjhb3A9yFqRqcM0ev-LO_Eb6jc7Xoyma1X_sKOfHbNGTUkQUmFKQR556HGjeMDaUu6LwsS-_jy9Q3EuFM4BBSxotn0iWjnAtT9cYtHagm8FGw6JBkO6oJVaGOnvvVKhrIdhzCeEqlSKurFVveFD7n5vgSfcTBDRH8HPDiWauI0Y0hNpbm_rPkvcmo87iNp3AkdJFFNsZdyzILRiSl5KNZQcDy2amBZNBFO3lYEysPa5kuVFozu_vB1UIK33SNAkLKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خفگی با قلاده و تکه‌تکه کردن پیکر | همه‌چیز درباره قتل وحشیانه زن ایرانی در ترکیه | فرخنده قائم مقامی چرا و چگونه کشته شد؟
🔹
رسانه‌های ترکیه از کشف یک جنایت هولناک در استانبول خبر داده‌اند که قربانی آن زنی ۶۸ ساله ایرانی به نام فرخنده قائم‌مقامی بوده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3215954</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/akhbarefori/652934" target="_blank">📅 23:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652933">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a10808b7f4.mp4?token=Xf3eQw_8IZWl6KhKWog_s4ZmiO6fyFQs9iv-fiSYYo62s8SQogpA-FhNA2kpSRJtRakbc_KWgAmgOm3H1xwJnpJ_8nW3qAHBSCDcKdIawlO6eF-1ZtFL1mce0n2ZudnleAyq0YaFqUvvWk7-_Yr27gCLo8u8gXILNz1YVsV8UGw7C7v5ApYDhEXFk-MtLNaBZ80cEJE1BPVhB7twZRSWMowsYONr2G8FFZKqirtBVDf84ObL66A0VdGVpwg34NTHi38oF5yja22ivJZo6jGu7UOo4UsweJFNCentQacLGBe2z1X16vDKmILW-tfCBOdd2-A9bX509WiUdtZxeKLg2WUfudAmugOxPTZEHIxt8Wv1wMhQdH3hJUOiuw_oUHVcHU1JwTCRP8lJIMnpVDfFkj-xi26kSVasx6i5_0E3QB36D6tID3hDTC6ZB6K1rcL_UDxFyZUdX4wnYHiYEupGt1ykSNhVSf0RcMgwVofb63un9njE6A8XoS7BOmKYHLOQVONH5LQXZ3yl5QUTJ7cEDOekjK8kuryeQze-lEYcqmcBI4aGTXXmNMQ8s5IWzoXdB8Wcc5Mn_92Bg-9c5Y3riWkfpy0zupxJkl3921zcCKOLi8ZDhP3lHdzXiEfrVdjkqvzMXieHIOcwzBhUOGAdgbPXqPTrUEnJ7YxrljIPjms" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a10808b7f4.mp4?token=Xf3eQw_8IZWl6KhKWog_s4ZmiO6fyFQs9iv-fiSYYo62s8SQogpA-FhNA2kpSRJtRakbc_KWgAmgOm3H1xwJnpJ_8nW3qAHBSCDcKdIawlO6eF-1ZtFL1mce0n2ZudnleAyq0YaFqUvvWk7-_Yr27gCLo8u8gXILNz1YVsV8UGw7C7v5ApYDhEXFk-MtLNaBZ80cEJE1BPVhB7twZRSWMowsYONr2G8FFZKqirtBVDf84ObL66A0VdGVpwg34NTHi38oF5yja22ivJZo6jGu7UOo4UsweJFNCentQacLGBe2z1X16vDKmILW-tfCBOdd2-A9bX509WiUdtZxeKLg2WUfudAmugOxPTZEHIxt8Wv1wMhQdH3hJUOiuw_oUHVcHU1JwTCRP8lJIMnpVDfFkj-xi26kSVasx6i5_0E3QB36D6tID3hDTC6ZB6K1rcL_UDxFyZUdX4wnYHiYEupGt1ykSNhVSf0RcMgwVofb63un9njE6A8XoS7BOmKYHLOQVONH5LQXZ3yl5QUTJ7cEDOekjK8kuryeQze-lEYcqmcBI4aGTXXmNMQ8s5IWzoXdB8Wcc5Mn_92Bg-9c5Y3riWkfpy0zupxJkl3921zcCKOLi8ZDhP3lHdzXiEfrVdjkqvzMXieHIOcwzBhUOGAdgbPXqPTrUEnJ7YxrljIPjms" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس پیشین سازمان سیا: ایرانی‌ها قرار نیست تسلیم بشوند
🔹
جان برنان، رئیس پیشین سازمان سیا: ایرانی‌ها قرار نیست تسلیم بشوند؛ حتی اگر دوباره شروع به بمباران بکنیم، آن‌ها تاب‌آوری بسیار بالایی دارند. دونالد ترامپ به‌طرز استثنایی لجباز است و حاضر نیست بگوید که این جنگ یک اشتباه بوده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/652933" target="_blank">📅 23:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652932">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95a490a6b7.mp4?token=JvO_jroVNwk0ESBmCmtXe9f_PNU7mCFXMHPtnjSaKEJUqJg1IAG4vRW8kdmLLMeDYvVgObEk-YIuOI4jASceaQeb0V1j6XLOaMoki1JMd52l318tcZAfGHbiZ8sZROsCusSNx9PgyVgv8msDTvfdnCpZP-vq7XNOR2LdIBTwwd08c0Aty0gzeZDRJEvcFG7YizKB6jIBmQG4ZV4qBnU7VEMaOKlFgK7zm5WWNkMHoR2o2Xat33km3gUDi_j1Uj9fRiK-uHhw3BWxsu_WSJfDmPPBsBDaYYAZNF-Ir5wB0vPiwCqgBZjkAZiZnd7vLLMkXeYhOPTmdr6LrtBCj1xF0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95a490a6b7.mp4?token=JvO_jroVNwk0ESBmCmtXe9f_PNU7mCFXMHPtnjSaKEJUqJg1IAG4vRW8kdmLLMeDYvVgObEk-YIuOI4jASceaQeb0V1j6XLOaMoki1JMd52l318tcZAfGHbiZ8sZROsCusSNx9PgyVgv8msDTvfdnCpZP-vq7XNOR2LdIBTwwd08c0Aty0gzeZDRJEvcFG7YizKB6jIBmQG4ZV4qBnU7VEMaOKlFgK7zm5WWNkMHoR2o2Xat33km3gUDi_j1Uj9fRiK-uHhw3BWxsu_WSJfDmPPBsBDaYYAZNF-Ir5wB0vPiwCqgBZjkAZiZnd7vLLMkXeYhOPTmdr6LrtBCj1xF0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ای‌بی‌سی: نزدیک به شصت خودرو پلیس در محل حادثه حضور دارد و بالگرد پلیس در منطقه تیراندازی گشت‌زنی می‌کند
🔹
خودروهای آتش‌نشانی و آمبولانس نیز به محل حادثه اعزام شده‌اند.
🔹
به نظر می‌رسد که این یک حادثه بسیار جدی باشد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/akhbarefori/652932" target="_blank">📅 23:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652931">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q82qZn83NeW9E-XszOv4fkZSlVrxjCEzfK8Gs_WxpstBPa-CORO7dp8Nw09f6FW62024kSDEzrb1LYWeB1YwWvOEdvJsYrRRNCAQVlI3oZefzfsUOtbVa4RL-ccm-s3-PtTAyOUSha9Fr0sibUbBAISCQUo-hUAyWxcFOWiEDUPiAjlhAPsamTAFmENsL5Q6_b_1dfyFJi-67Jr3wxy_ofq5OrUTLS7hdueJyZdyyFiy70RpSIbjbdW8uQy386dMSmo6gZ1W8EOmHEtUUDK4wIyKfhwSiWS8ENFwsb7GVoYTZ6TJJDTMCrL7cpsFmzyChbp6gIYk_OgnY37h-IxVuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش رئیس‌جمهور ایرلند به ربوده‌شدن خواهرش توسط رژیم صهیونیستی
🔹
رئیس‌جمهور ایرلند: ربوده‌شدن خواهرم توسط رژیم صهیونیستی بسیار ناراحت‌کننده است.
🔹
من بسیار نگران او و همچنین نگران همراهانش در کشتی هستم.
🔹
«دکتر مارگارت کانولی» خواهر رئیس‌جمهور ایرلند، جزو شش شهروند ایرلندی است که از ناوگان جهانی پایداری ربوده شده‌اند.
🔹
دکتر کانولی در ویدئوی خود: اگر این ویدیو را تماشا می‌کنید، به این معنی است که من توسط نیروهای اشغالگر اسرائیلی از قایقم در ناوگان ربوده شده‌ام.
🔹
من اکنون به‌طور غیرقانونی در زندان اسرائیل نگهداری می‌شوم.
🔹
من بسیار مفتخرم که در ناوگان پایداری شرکت می‌کنم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/652931" target="_blank">📅 23:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652930">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
حمله پهپادی علیه گروه تروریستی پژاک در شمال عراق
🔹
مقر گروه‌ تروریستی پژاک در استان سلیمانیه عراق با چندین فروند پهپاد مورد حمله قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/akhbarefori/652930" target="_blank">📅 23:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652929">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9TCX9jjAVAEM0QLIACapM4ADCPNdyHpbCvH7tz4uhQfv5Yhe_2DWJ96vaznLAZm3_sop-VzulPV4v1EwR1k4juoMPDDMhT9oUHXIctq1mTerg97sG5zTurlI9xOePPFWghKPs2utwEiFQOO2OtEAwDGhk2FnehrlRhGDk8LUirP2hMYzmD_LX5BQFT-n1_wd18c7tmAwiY_gXfjHciINDJaJ4gO-JHVmn_wviP_SsWHnkG55K6C4Y_0tOVcn3kypmP-YvhOptY_jsvoJ0_GaIEZP2Ok5vnrLBPUyYsw6CHubjjQM0bGEauPzgKLNssEeTmfTrMAwpC1ffpUN8Ozxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه خبر| کارشناسان: علت فرار مجدد ترامپ، ترس از پاسخ قاطع ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/akhbarefori/652929" target="_blank">📅 23:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652928">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSnvd1ohFw5oEaBJgsfyjovIrUzv3ZnJBEkYDPLi1Vbc9r_YyWN3ob_JlwE6xdO2ONDsTEhgtBVm0X7lmR37aek7YJ2LxCzG0DATHrlrtYEwdngu307FJpcni6kk3OSuc26n6rnyMZs5h4TyAB6KSUf_jeK_uydff4xqRwE_3GYI7EEIq85fijSGNGCWqN-30GGBMcuGLqU0Kb0nnc3R4Z2p16Ac_Gibq_rlR-b9c-nvwbdgY7qH_K1vSizSFksGk_djmnzHZLIVcY8ydXfI69ca8SWZ_P_JuZ2z4IHLzX4M2nVQBvZAYtf1bH52ub6F6gIF33VLv1WeIlwXOzdBnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش فوری ویلا جنگلی در نوشهر (نخ شمال )
-برای قیمت و اطلاعات بیشتر و ارتباط با ما وارد لینک زیر شوید :
https://ble.ir/vila_aghsat
🏕️
ویلا مدرن لاکچری
داخل شهرک معروف
🔥
✅
متراژ زمین ۱۰۰۰متر
✅
متراژ بنا ۷۰۰متر
✅
۵خوابه (مستر)
✅
استخر چهارفصل،آسانسور
✅
معاوضه با خودرو ،طلا،دلار و...
✅️
دارای سند تکبرگ
✅️
⭐
اقساط بدون بهره
⭐
-برای قیمت و اطلاعات بیشتر و ارتباط با ما وارد لینک زیر شوید :
https://ble.ir/vila_aghsat</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/652928" target="_blank">📅 23:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652926">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
استانداری هرمزگان: صدایی که ساعاتی پیش در جزیره قشم شنیده شد، ناشی از فعال شدن سامانه‌های پدافندی بود
🔹
وضعیت کاملاً تحت کنترل است و شرایط جزیره قشم کاملا پایدار است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/akhbarefori/652926" target="_blank">📅 22:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652925">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j488fvwpCVTowj7OGlYLAm5sGcv6prE2R79hHeNVYZmnLbpahdwiXlglG9iBTV_sfXBkxgcankWUG8hsKrF4mzlfMiFtKALV7eZI3AHRAm4qYvKTbtND7ELqLPN1Qid7I69zuaKofXhXlhRT7mvkZtZRc5jUx7-qWHJ2_7u5U9t1XAf2silD7SmQ-cD_Nc2FbSFif-_zmxf7a6GSLbqXOW3gJOfu-YoMfb5R_1LbZbsyFxbWT4DCIndb8v6azfgH2-f8VI8-f4sWEGHFaHCmI-dgZC_V7UkD-yVFmbaP3x1QihvcqCu_C055mSh54KF7syXm--goPBuIa0FWxKI2ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پهپادهای FPV حزب‌الله مانع اساسی پیش روی صهیونیست‌ها
🔹
یک شبکه عبری گزارش داد که ارزیابی‌ها در ارتش این رژیم حکایت از آن دارد که ریزپرنده‌های انفجاری حزب‌الله مانع از حدود ۷۰ درصد از آزادی عمل ارتش در جنوب لبنان شده است.
🔹
شبکه دولتی «کان» اسرائیل اعلام کرد که بخشی از برنامه‌ها، عملیات‌ها و مأموریت‌های تهاجمی ارتش این رژیم که قرار بود انجام شوند، به دلیل تهدید کوادکوپترهای انفجاری حزب‌الله یا لغو می‌شوند یا به تعویق می‌افتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/652925" target="_blank">📅 22:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652924">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
بهم ریختگی بازارهای مالی آمریکا، وضعیت قیمت نفت و ایستادگی ایران، دوباره پدوفیلی را مجبور به عقب‌نشینی کرد
🔹
ترامپ دقایقی پیش نوشت: «از سوی امیر قطر، ولیعهد عربستان سعودی و رئیس امارات متحده عربی، از من خواسته شد حمله نظامی برنامه‌ریزی‌شده علیه ایران را که قرار بود فردا انجام شود، به تعویق بیندازم؛ زیرا مذاکرات جدی در حال انجام است و به اعتقاد آنان، به‌عنوان رهبران و متحدان بزرگ، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همچنین تمام کشورهای خاورمیانه و فراتر از آن بسیار قابل قبول خواهد بود. این توافق، نکته‌ای بسیار مهم را نیز در بر خواهد داشت: ایران نباید سلاح هسته‌ای داشته باشد.»
🔹
او در ادامه دوباره منتی بر سر حکومت‌های میزبان پایگاه‌هایش گذاشته و نوشته: «بر اساس احترامی که برای رهبران نام‌برده قائلم، به وزیر جنگ، پیت هگست، رئیس ستاد مشترک ارتش، ژنرال دنیل کین، و نیروهای نظامی ایالات متحده دستور داده‌ام که حمله برنامه‌ریزی‌شده علیه ایران را فردا انجام ندهند.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/akhbarefori/652924" target="_blank">📅 22:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652923">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
علت فعال شدن پدافند جزیره قشم مقابله با ریزپرنده‌های دشمن بود
🔹
معاون استاندار هرمزگان: صدایی که ساعاتی پیش در جزیره قشم شنیده شده است، ناشی از فعال شدن سامانه‌های پدافندی و درگیری با پرنده‌های دشمن بوده است .
🔹
وضعیت کاملاً تحت کنترل است و شرایط جزیره قشم کاملا پایدار است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/akhbarefori/652923" target="_blank">📅 22:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652922">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
باج‌خواهی آمریکا از شرکت هندی به دلیل دور زدن ادعایی تحریم‌های ایران
🔹
وزارت خزانه‌داری آمریکا مدعی شد با شرکت هندی «آدانی اینترپرایزز» بر سر ۳۲ مورد ادعایی نقض تحریم‌های آمریکا علیه ایران به توافق ۲۷۵ میلیون دلاری رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/652922" target="_blank">📅 22:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652921">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ترامپ باز هم عقب‌نشینی کرد
🔹
رئیس‌جمهور آمریکا در شبکه تروث‌سوشال نوشت که حمله نظامی به ایران را بنا به درخواست ولیعهد عربستان سعودی، رئیس امارات و امیر قطر متوقف کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/652921" target="_blank">📅 22:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652920">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
فوری/ ادعای ترامپ: حمله به ایران را که قرار بود فردا انجام دهم به تعویق انداختم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/652920" target="_blank">📅 22:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652919">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ylb1fCL_y3TYDEEzsLF0i4tlidJJYPlUSg4gTiGmiWEvXGgHCXwNqmLfqxnKcHKzPazoye_QRFTRHtyxT-IheqRoTB1WelQdCBY_cPaB4B9tpVP-hQFWCcIEAmJDFPhoiyfRGsDpOuwFdc6Py6IvCvj-U89_HRE_uyPxi0D3zUXdUg0AQ1TVb1s_kyqnzNXtbHtf-YO8miol7zDdVZtdOIu-ENwFrxPRzG-HfjNWsB83EIdLip4BsvX6w7vfPluobYnJo6CMebNTEQWleemB6_reQUffYbdmNlUFZmY8A-D1HNYlaUn0RBjGsl8l4GuSt4AWyX2fP3sE9-w0oOx_xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سالانه ۱.۵ میلیون تُن میکروپلاستیک وارد اقیانوس‌ها می‌شود
🔹
تغییر از انتخاب‌های کوچک ما شروع می‌شود.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/652919" target="_blank">📅 22:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652918">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7953d92b1.mp4?token=RPmfedyYbP0uLmhZtt2bQdPofKO-urTu034l3jFcShcIyfhgv-_z3xohY_goyqwlQDQFnLihdSmqTxAjAeeprIdHHaAee2qKP2q9iPLfVqOUKKzIZ1KuS9Xcl22Hf0ujO5p3WML4btpXnylkMwcpKgtCBB1WWvE-ehQSxEaqqjQ9Cf8m_vTuExPq22LtF-jkfUUzz5i86W1p0XWl7GL2_hYXpCp30-WfxW6-8Q5FytBLMgI1u1XvDOhY7ofu0go3brn73HQ3DSR5unebzjIUYf-e3SAeI0QJCQXHxuEOxBfLWMae41o7gDjgQTS-6lm2rdTjtyf4iGA-3YcVe-v90Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7953d92b1.mp4?token=RPmfedyYbP0uLmhZtt2bQdPofKO-urTu034l3jFcShcIyfhgv-_z3xohY_goyqwlQDQFnLihdSmqTxAjAeeprIdHHaAee2qKP2q9iPLfVqOUKKzIZ1KuS9Xcl22Hf0ujO5p3WML4btpXnylkMwcpKgtCBB1WWvE-ehQSxEaqqjQ9Cf8m_vTuExPq22LtF-jkfUUzz5i86W1p0XWl7GL2_hYXpCp30-WfxW6-8Q5FytBLMgI1u1XvDOhY7ofu0go3brn73HQ3DSR5unebzjIUYf-e3SAeI0QJCQXHxuEOxBfLWMae41o7gDjgQTS-6lm2rdTjtyf4iGA-3YcVe-v90Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خضریان، عضو کمیسیون امنیت ملی مجلس: خیلی از مسئولان ارشد نظام معتقد دارند که باید در مقابل اقدام محاصره نظامی آمریکا، پاسخ نظامی به دشمن بدهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/akhbarefori/652918" target="_blank">📅 22:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652917">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgAk5OV_XOEvcwZzt5_yCBGYzc7UJCiUrTRkZxtWemjAUuxmzq6Ayxl4WIKsMuREE5nwZmm4AYy9NZOWWAGguzgSpIXbUnjkwB7pYHT67tm8iwYMkU3hMhrgnWJhP7Keh3RKIn9ak-SmvbomErUKbRF5r6hsxhirk5pPzrxlT_f9mvF7VRi6-vsCJjZf_bWERW7mb3xMbqq2AhyG1CReyX-zw1gBB8myoyYn2PAk7on8eoxuk7XcTO591L8YRB9I4PcBwJqzAapviTZrAgiLP0sCiMrbdu5u27zHd2-YalDpjRw9JN424dAn4P9cN69-OyDiDpF3LpGg7GxLKWigxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برهه حساس کنونی
🔹
در شرایط حساس کنونی که تنش نظامی با آمریکا تحریم های فلج کننده و محاصره اقتصادی معیشت مردم را با دشواری بی سابقه ای رو به رو کرده انتظار می رود نهادهای ثروتمند حاکمیتی و دولتی پای کار آیند. این نهادها با تزریق سرمایه خود در اولویت های کلیدی اقتصاد کشور، نه هزینه، بلکه سرمایه گذاری راهبردی برای عبور از بحران و پایه ریزی شکوفایی پایدار انجام دهند؛ ورود به موقع این نهادها، ضمن حفظ آرامش بازار و کاهش فشار بر اقشار آسیب پذیر زمینه ساز اقتصادی مقاوم و خودکفا خواهد بود. چنین عزم جمعی هم به نفع مردم و هم تضمین کننده امنیت ملی و استقلال اقتصادی کشور است
🔹
هفتصدوپنجاه‌وسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/akhbarefori/652917" target="_blank">📅 22:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652916">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
پدافند هوایی جزیره قشم فعال شد
🔹
شامگاه دوشنبه پدافند هوایی جزیره قشم فعال شد.
🔹
هنوز مسئولان توضیحی در رابطه با چرایی فعالیت پدافند جزیره قشم ارائه نکرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/akhbarefori/652916" target="_blank">📅 22:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652915">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671233beec.mp4?token=JQ4WIcdsmAQxTQ3Y88XkLQA6dfaXpaDFIpNp3U8xj3dI5ZBkEcmytH7LO7cjvbW2zqOuC8azsJVHwNyTBz6rmM--iEFOX56p8JK6BqbYyAW7wM067_VXtcu27AJ7K3ocE_Rbb9M2mqi5IJ9-Q93VSF9NuvBYJeWKgxnMkjlnEgQwENWyk79xq6DYRM5_zomc5N8o9Q2VZLw-Xkoq7WeBBbAIqo_BsR4GuzTW39fhGPgHXofGJXNfpaJxTCgh0OA7KNMUJynJVKtxUdmuGrxeXLqrepBtMJEXrwIT5cUjdVDModeoG0R4ruz87lK6lQYEIJ01EfUOKDS080DmCPlZmjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671233beec.mp4?token=JQ4WIcdsmAQxTQ3Y88XkLQA6dfaXpaDFIpNp3U8xj3dI5ZBkEcmytH7LO7cjvbW2zqOuC8azsJVHwNyTBz6rmM--iEFOX56p8JK6BqbYyAW7wM067_VXtcu27AJ7K3ocE_Rbb9M2mqi5IJ9-Q93VSF9NuvBYJeWKgxnMkjlnEgQwENWyk79xq6DYRM5_zomc5N8o9Q2VZLw-Xkoq7WeBBbAIqo_BsR4GuzTW39fhGPgHXofGJXNfpaJxTCgh0OA7KNMUJynJVKtxUdmuGrxeXLqrepBtMJEXrwIT5cUjdVDModeoG0R4ruz87lK6lQYEIJ01EfUOKDS080DmCPlZmjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: خیلی از مسئولان ارشد نظام معتقد دارند که باید در مقابل اقدام محاصره نظامی آمریکا، پاسخ نظامی به دشمن بدهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/akhbarefori/652915" target="_blank">📅 22:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652914">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4a8639f1.mp4?token=YaTtUv2rp9ez81lca5XSvPcIm-RtUZmpY_c7IBLEORFLflyHkXqn4-H7JGDrIfMtdqrFaEh3pHAOaTjOPe8bkxfOty6jVStV8lrtPnwHX7apCa3MtroYZb4HzP7Bc7TKBP-0ztbgdGeDMnlmzXlC5ubExddlj0MKyFmzFlVNNWSjlsQCRhtqgElb3pbPrjNdDyeDCQdLsK997BHeN9i_c0O-L5lKTbOlS6G13pVEMlBRjIbv_2wujUqBLgu0ROzg2uMiMmI0hOPYWZ0droG2LRLj-paihLIF40i2NJZrJMbR2C_VwvGSymr5zLqzT_HLxvz3Ut-sOGU8AbH2dAryE33rQS-Q1NPhkOsa_roTKGQuE3uD41XkacnBQmMryF9SJbgZSs6fIPuO40Bn2hmbWUAzRxXjUGG3kXxJVWSbJGGn-VTHugknZYVwmoqO1QqlvXDWoQ9CAjr9NPgTang7mdCuXksf6Xo89M_uFx31dZuIfo37hbrrV4XX5nDlfo8wLMR8LjIzsR6er_XboX_Nt18q-6KriLoM3voDMtmu0Kb9V7b2lqNG5G8YBiMM673P8WPA_t0VuATRz9kUQztP4QX1RxsYFfEZTKKlM4WuU-4loHkKmNauRw3YQb_A-Ozm6GBTIdhCmZ47mC01BJAGeLqPy4aQenHzBq7nbR2SrIk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4a8639f1.mp4?token=YaTtUv2rp9ez81lca5XSvPcIm-RtUZmpY_c7IBLEORFLflyHkXqn4-H7JGDrIfMtdqrFaEh3pHAOaTjOPe8bkxfOty6jVStV8lrtPnwHX7apCa3MtroYZb4HzP7Bc7TKBP-0ztbgdGeDMnlmzXlC5ubExddlj0MKyFmzFlVNNWSjlsQCRhtqgElb3pbPrjNdDyeDCQdLsK997BHeN9i_c0O-L5lKTbOlS6G13pVEMlBRjIbv_2wujUqBLgu0ROzg2uMiMmI0hOPYWZ0droG2LRLj-paihLIF40i2NJZrJMbR2C_VwvGSymr5zLqzT_HLxvz3Ut-sOGU8AbH2dAryE33rQS-Q1NPhkOsa_roTKGQuE3uD41XkacnBQmMryF9SJbgZSs6fIPuO40Bn2hmbWUAzRxXjUGG3kXxJVWSbJGGn-VTHugknZYVwmoqO1QqlvXDWoQ9CAjr9NPgTang7mdCuXksf6Xo89M_uFx31dZuIfo37hbrrV4XX5nDlfo8wLMR8LjIzsR6er_XboX_Nt18q-6KriLoM3voDMtmu0Kb9V7b2lqNG5G8YBiMM673P8WPA_t0VuATRz9kUQztP4QX1RxsYFfEZTKKlM4WuU-4loHkKmNauRw3YQb_A-Ozm6GBTIdhCmZ47mC01BJAGeLqPy4aQenHzBq7nbR2SrIk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خضریان، عضو کمیسیون امنیت ملی مجلس: اگر تنگه هرمز باز شود جنگ بعدی با شدت بیشتری شروع می‌شود/ اگر اورانیوم از ایران خارج شود دشمن احتمال دارد با بمب اتمی تاکتیکی به ایران حمله کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/akhbarefori/652914" target="_blank">📅 22:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652913">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 50</div>
</div>
<a href="https://t.me/akhbarefori/652913" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه پنجاهم
رائفی‌پور:
🔹
0:07:50 چرا ائمه را واسطه بخشش گناهان قرار میدهیم؟
🔹
0:17:30 گریه سند محبت به اهل بیت است
🔹
0:22:30 ارزش قلب انسان ها برای خداوند
🔹
0:31:20 جایگاه بهشتیانی که به مقام رضایت رسیده اند
🔹
0:43:30 سنت خداوند برای مؤمنین
🔹
0:48:00 طولانی‌تر شدن عمر با انجام مستحبات
🔹
1:07:00 تحلیل اختلاف نظرات در شیعه و اهل سنت
#دعای_ندبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/akhbarefori/652913" target="_blank">📅 22:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652911">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9755b4156.mp4?token=N0oqNqWV-7sJ_SuNkmZuDfWUO5buISp4T2j-lgD1_JJAlm2nfVi0_7-K2yzqr_mRcDWEXnAVI2UU4Xk8efpBAgvqVeA7zpMk9Edz4rI5J_it-8b6hQApGTtcUuewaTlrEx_fQ_X7ZNCqxzKl5Tito8cvva5iZ0IaA-jIDSgHj94nPew15Uh2kdvwNBCsLMozF_HKUGc12LZJyZkR_WI5j-e5BE3FOj-AbQeNoNqe1GQ1mi1V9DziymUn6EfaAakp-oWddFnzOr6qK_DW63nMAayIUrmMvcrLpQ4OHXTE96cNiK85PqzLtZu283aC4MNLpV0c1ws448YK6Ku8VlTOf12uYnO907nUZ5HkNxsM6fZaf859jCanL4lpLMJwxA8UW6g82Dg34oW5PRd4xeulWF0xL1ZreYh8pfyJoDbF6QRz6nZWISiw60pHIZETmSBidruIvtHn3EOGzYNKwe8Nwa0AxW9YfcRZdQxFciCtu59bDggdNPGOgLYvIZZyQfLv2MHT3R8iZU-S7uxnkTORX7Aw7DFe0VGQOSWB3adAxDAumLuUxWE1zGUxS7kCDOw701jg2EykvT6uRHvx8wi0H14fl13DmRgXU0mWuPBmRhUMP9p7D7wZIG4ZkEi9UVC00e4luvPqjQ9geuk4o6jN9ViEsTg50pRPJe4mWKPgCXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9755b4156.mp4?token=N0oqNqWV-7sJ_SuNkmZuDfWUO5buISp4T2j-lgD1_JJAlm2nfVi0_7-K2yzqr_mRcDWEXnAVI2UU4Xk8efpBAgvqVeA7zpMk9Edz4rI5J_it-8b6hQApGTtcUuewaTlrEx_fQ_X7ZNCqxzKl5Tito8cvva5iZ0IaA-jIDSgHj94nPew15Uh2kdvwNBCsLMozF_HKUGc12LZJyZkR_WI5j-e5BE3FOj-AbQeNoNqe1GQ1mi1V9DziymUn6EfaAakp-oWddFnzOr6qK_DW63nMAayIUrmMvcrLpQ4OHXTE96cNiK85PqzLtZu283aC4MNLpV0c1ws448YK6Ku8VlTOf12uYnO907nUZ5HkNxsM6fZaf859jCanL4lpLMJwxA8UW6g82Dg34oW5PRd4xeulWF0xL1ZreYh8pfyJoDbF6QRz6nZWISiw60pHIZETmSBidruIvtHn3EOGzYNKwe8Nwa0AxW9YfcRZdQxFciCtu59bDggdNPGOgLYvIZZyQfLv2MHT3R8iZU-S7uxnkTORX7Aw7DFe0VGQOSWB3adAxDAumLuUxWE1zGUxS7kCDOw701jg2EykvT6uRHvx8wi0H14fl13DmRgXU0mWuPBmRhUMP9p7D7wZIG4ZkEi9UVC00e4luvPqjQ9geuk4o6jN9ViEsTg50pRPJe4mWKPgCXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: اگر تنگه هرمز باز شود جنگ بعدی با شدت بیشتری شروع می‌شود/ اگر اورانیوم از ایران خارج شود دشمن احتمال دارد با بمب اتمی تاکتیکی به ایران حمله کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/akhbarefori/652911" target="_blank">📅 22:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652910">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDdZ92QK19UF28YB38ltT27qdlczpPPMmo7Uyv2jNJtZmS6imGbSeq4K_yvwhMgzHL3zO-5TteHRh3uGobSvs9XHIsWR8gE6D3XsyXDQCY4falxHdpAYL_fUhRq0ua_38XNVbmCdXcmmlP7L_VuljgAl0BhaQPHlNCKQ0TuSedR3CfO-I--WMfY30sUrxTlJTkqU13W2bFqrAfcQq8bqiQ9nnuGZrZEhb-Nwg4pdlLEXwh5VlC9a21iw05bE1we3v4HTi7vk67JvtLdwvlU3g8bjZGBVM6eTNFdaePdgwrCwnkdbz1A8fBaihZwKy9V-GUr9sSCjOqkD_KCds3I7gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: جمهوری اسلامی ایران با عزت، اقتدار و حفظ حقوق ملت وارد گفت‌وگو می‌شود
🔹
رئیس‌جمهور: گفت‌وگو به معنای تسلیم نیست. جمهوری اسلامی ایران با عزت، اقتدار و حفظ حقوق ملت وارد گفت‌وگو می‌شود و به هیچ عنوان از حقوق قانونی مردم و کشور عقب‌نشینی نمی‌کند. ما با منطق و با تمام توان، تا پای جان، در خدمت مردم و حافظ منافع و عزت ایران خواهیم بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/akhbarefori/652910" target="_blank">📅 22:05 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
