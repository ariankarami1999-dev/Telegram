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
<img src="https://cdn4.telesco.pe/file/HIiTTgNODJgdgDCjd92rHMri5swFFzSE9yB8-obzknmdngr2V6dL50FItWQhBg1r13MrhQ43LhQ7lGWGr1REjyZiQ1Hmf5joZ83Xn9IciWSGcivDFE5uC0LkOLwIYdspZVQGk4iTNa-VOMuEibeEhfOy2qkbcWsMnT-FykkB0lA1LSqPDsFtdFq-1tRQFMBaDURC-G7619ayCzRXmlIELtR9ulc9i_tFby-WrfW_nJ-4PWM_IeXU7HeVfpokXG9qnwVX_8-nDyACpDxRS-J4sAlW9jN0MgQELrMU5g8PMM0PCdFWG6BXlZYnhpNfloMHvrlNa9nM1Xrl2PolzYfwMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 444K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 13:43:39</div>
<hr>

<div class="tg-post" id="msg-21012">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خبرنگار الجزیره: ۳ حمله هوایی اسرائیل بامداد امروز، مناطق اطراف شهر النبطیه الفوقا و حومه شهر انصار در منطقه النبطیه را هدف قرار داد. @WarRoom</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/withyashar/21012" target="_blank">📅 12:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21011">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKnmYm7G1La0rFvKjC-efuh_o1To-1kwsHIJ-jCZFqalVGGwP1oHOFgqFRxR3HApwkcCLDicikkCbB4gmmUNEGcRkwroamesWKXzMGWMFq2Uk45-UC5m8N3qYsws84GxF6bXLqCJVjujXZoJYxVXxWdbVW9I6GrgeS5wxBI00ruETKnpgsZzhMfu5QsP3WCDgVJNWquUuqNh_zg62wDI_xJ-l5pBwllnLIM7mh7b5u29XtE0JzOkrJhn_HfAgTRNAbNdoMo7mkLAYEuMoM9xP0Nn0zDfY0K2onpREUvNhghhF_8Htz_BP8FbgxW4EE-5PZk69-xMDQvotm2IUWp3Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : دیوار فولادی، محاصره
@WarRoom</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/withyashar/21011" target="_blank">📅 11:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21010">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFzEjA_J7lPQXbFyotLq7Gwvnsy8HK-LeiYRWbCMoHxKUKxYk_-jPbQ17DoCUtorLI3FcEpDIu2wuarg9_lDHCT-rb2c4BIbnK8QNQG3GqNVGwiGCjb603wHPcSDNpJM1ambiI_flCgQCUK2pXjUr9aIQo16ellOfG_ERonkE8ivWosMnRy_dcJfUzRNO9YaKM04jJlUMGq6U1YGc1CLVfo18RoKF5o-K5XNKNcxrLpwlnulPymr0lnXalIe7Z05oWA4HeqRSUGobVXjnj5hQ6CycHes0z4uiZQlW5qcKprKeLXO8qDdYx4mN7B3V8FY0-_17c_laIbYX4POqrUJtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۲ : تصاویر ماهواره‌ای منتشر شده توسط رویترز: دو لکه نفتی در نزدیکی جزایر قشم و سیری ایران در خلیج فارس مشاهده شد، در حالی که حملات مکرر به کشتی‌ها در این منطقه ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/21010" target="_blank">📅 11:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21009">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مستند دیدنی
«جاسوس ۲»
از کانال ۱۴ اسرائیل ، که در آن با مأموران سپاه مصاحبه میشود !
با زیرنویس فارسی
، پیش تر قسمت اول را برای شما قرار داده بودم… از دست ندید…
🌐
@WarRoom
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/withyashar/21009" target="_blank">📅 11:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21008">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7Pp1tfGgqRKfFX0vxdwsUcFBZjJePniOvjU7mTLhfotOgyxN2xcYq6KCyPSSxnqO8AsZLNnID4WhszhKI7j4MEV_TQCqVUSqGrF9fW7-Ube2IA77k3ykhvHdXurN-rTsf0R4ma2-LkzVDfeZuHF272ukyZQRLBHtKHi4ORWSNEIuPNfkcBulHEbLUv5eknyhKh2ZvCIT5Y-omWijwK3-0Rg8Uv5ssPIGBE988AI5xHExipX8G-6hYKcmIP0bzAg_kOMioTgOc9px_l-qgPt6BLuJm2Zgq-MPOgZ8MQA7FBPXjXa8_baesRKO19Bx6q1PDr9wEsdeB8u2Gv4uvFoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : خط جدید ترابری لاجستیکی نظامی آمریکا و کد عملیات «مووسی MOOSE» نشان میدهد در جنگ بعدی پایان دهنده کار، آمریکا بر روی پایگاه خود در قاهره حسابی ویژه ای باز کرده و مرکز پشتیبانی عملیات خواهد بود هم نزدیکی به منطقه هم فاصله دورتری نسبت به کشورهای حاشیه خلیج فارس…
سفر قاهره تازه شروع شده…
@WarRoom</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/21008" target="_blank">📅 10:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21007">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خبرنگار الجزیره: ۳ حمله هوایی اسرائیل بامداد امروز، مناطق اطراف شهر النبطیه الفوقا و حومه شهر انصار در منطقه النبطیه را هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/21007" target="_blank">📅 10:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21006">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-mmll4d4qs6u8woeRNAtk35ZKaYT8KxCTsb-eaKuzb9OGA00xYyKClT0F4yqMZitOj1E_fTyG5BLfqYtZ0UkpbIURFHjWjrYlBolgV6y5uMFcXWyI7IKV5rfLPO6u9IFIsCFckpK6MA8gupooUfDUVf_dTERueWn_eC5xtAQ0RlPftX4smRwTY3S5PXk_qNbUIiyC00nvVnDxFZZTETpzaL9Pjq6WelX40WYWYIomJS3RBx17-sKj-obTowM_t21nHaqpH6Ua8O2U9oFHY9BNP2jOZP1sheg_pcU8-sW3eduyS1WBEbFa1nXKqItxGbGns4k6DeIGPu74GIBWGKXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏UKMTO گزارش تأیید شده‌ای مبنی بر برخورد یک پرتابه ناشناخته به بدنه یک کشتی فله‌بر دریافت کرده است. خدمه در سلامت گزارش شده‌اند، هیچ ارزیابی خسارتی گزارش نشده است و در حال حاضر تأثیر زیست‌محیطی آن مشخص نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/21006" target="_blank">📅 09:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21005">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ادعای نیویورک‌تایمز: مشکل تأمین و تدارکات ناو آبراهام لینکلن پس از آن آغاز شد که ایران، به پایگاه نیروی دریایی آمریکا در بحرین آسیب شدیدی وارد کرد و یک مرکز لجستیکی مهم را از کار انداخت
سپس پنتاگون مرکز تأمین و پشتیبانی منطقه‌ای خود را به دیه‌گو گارسیا منتقل کرد که ۳۵۴۰ کیلومتر از ناو‌های آمریکایی فعال در دریای عمان، فاصله دارد
@WarRoom</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/21005" target="_blank">📅 09:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21004">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKXQ1wp3jljlmO4cQip8nFGtL_OiUGT9FAunEoUeDV-H3AtbF25zvSBx0obbDnWTvtV0aO9M3SLCGus6hgnVtRjNGgT2GJr5FwmOVOKd_dtaXWplJorjWpq1mIYWeh0nMbO2shCgZwPqdo64Kdo0hlHIzCu76yjjvcICrWpVSRTNKjcGHJ88itud8IgaiS2kjVxrm8KEzhBAIYkm2rKrsnt4ksDN8RJBqONsnRdPWaeCmDe8G7tH5fujTNMQLZnTBrLa04BK01XljdKrww8UkrV_328pVMLgs1KsQPCm7G6HKoAV_sscF37ez-OZAX2uvGs_MvaV1tXu3MpNIcvxmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس نیوز : آقای معاون رئیس‌جمهور، یک لحظه به توافق نزدیک هستیم، لحظه بعد می‌گوییم قرار است حسابی آنها را بمباران کنیم. یک لحظه تنگه هرمز باز است، لحظه بعد بسته است. مطمئنم این نگرانی و سرخوردگی داخل کاخ سفید هم وجود دارد. می‌دانم پیش‌بینی کردن دشوار است،…</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21004" target="_blank">📅 03:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21003">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ در مورد ایران: به زودی تنگه هرمز را جزو قلمرو ایالات متحده اعلام خواهم کرد.  ایران به شدت شکست خورده است. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21003" target="_blank">📅 03:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21002">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoVtBQpIVPxlLcgHPNmEWel-R35iAGEGsSqHyu8fz8R_UVwApdoBk0BXmVkESwUsE02tvsE1DpcdzdQKZ97DSDXTIDkTYpYs_x1EwEDlm5WycuPwAPHkqLsQk1J0JGmGp5ZmEkrl7-hW2nxBHfkpUWIHUsBlwTMUq8f1JkbArEwBE5xbsJIeLA3lVql804rPW0TtgmB0AiuN0-ZbNbO7bDf3m-EptW3geW-WEPvCQaych8az8ds6ShNzlcvcuVa9nED8yJEUNZG_uySSMggY1xpVKiSpVcFvDGWDjMD-DUKFXU12kbV8FtTK2Gd3yZKAZoQ5o88rWKVWhO7Oe9VcFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهار هواپیمای C130 سوپر هرکولس از آمریکا به انگلستان و یک C5Mسوپر گالاکسی، یک راست از آمریکا به خاورمیانه میآیند.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21002" target="_blank">📅 02:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21001">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وقوع زمین‌لرزه ۷.۴ ریشتری در اندونزی!
دو زمین‌لرزه جدید با قدرت های ۶.۱ و ۶.۶ ریشتر نیز دقایقی بعد رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21001" target="_blank">📅 02:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21000">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzaAKXIJme48RyEgdX00f_qcbAhAlyFHZTcBevzHaxOyw49VSf8KjlBz51DUBVVGmVgtLCEt5woMSkCqb9413DyemwK7SgkCDOvE31LVC6vaQLjha0Qsr1CXCulF72Aw83ZqjhPNORDAnPhhj_WEGmsYH3pNKLwPS8mSiV5Y1l8ZOtuRcXcCnYhVrsRzNGys_T6UovRrMzz5oGwzEp0kTldFHrjeWdIqxnDUaP_Si3a8FN7Qtf5VHzUhfYPws5jQ2F4jAIZEgMAj84-Bz4nt_qgh8hhk5hmKxFtQKHTO9vPjESSuU9c9Gk7FrrPrjy3lFuMgyb4x8KAzc17LN1DOhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هشدار زودهنگام E3B-Sentry با رادار AWACS هم راه با ۴ سوخترسان هم اکنون در منطقه خلیج فارس انجام مأموریت میکنند
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21000" target="_blank">📅 01:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20999">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">@WarRoom
مسیر من</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/20999" target="_blank">📅 01:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20998">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from………..</strong></div>
<div class="tg-text">درود یاشار
شما بیشتر خرف های جاوید نام روح الله زم رو بیشتر قبول دارین یا استاد مانوک خدایخشیان؟
ممنون میشم جواب بدی</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20998" target="_blank">📅 01:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20997">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">@WarRoom
مسیر ما</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20997" target="_blank">📅 01:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20996">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">@WarRoom
مقدمه</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20996" target="_blank">📅 00:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20995">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ: تمام کشورهای منطقه در شرایطی شبیه به محاصره قرار دارند، زیرا ایران به عنوان یک کشور زورگو در خاورمیانه شناخته می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20995" target="_blank">📅 00:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20994">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d76eba2226.mp4?token=hF7gjn8kubqGimFwlnR8fUeZIy1WTvU1HmLv07r-TqNFJffOKlS3Bi8BRk8csYu4fL0_i3Rvd6KB7m4IvWdGXBDaV4slUHYWjmi_frOpFmr-6fMqwE1a6IJv5fSW9D59xLAvS-ccUtzMjUb-U_NaVsdq6EpOMotETAreo4bemvvXcNTRCu0dqPiFPPnfge1GGj95yNIprZRnGbHut5ztVyDS9kGd9vgQoopMh_RN5lhHcn8us0utOXdwxu1BgjFPg_uMp21iSqRd5AXDadxpPqViRNWUuel7sXQhgoEG_bclFje2Z60FjORY7BHW0xZirLnMPWYqp3ezjsOcnabFRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d76eba2226.mp4?token=hF7gjn8kubqGimFwlnR8fUeZIy1WTvU1HmLv07r-TqNFJffOKlS3Bi8BRk8csYu4fL0_i3Rvd6KB7m4IvWdGXBDaV4slUHYWjmi_frOpFmr-6fMqwE1a6IJv5fSW9D59xLAvS-ccUtzMjUb-U_NaVsdq6EpOMotETAreo4bemvvXcNTRCu0dqPiFPPnfge1GGj95yNIprZRnGbHut5ztVyDS9kGd9vgQoopMh_RN5lhHcn8us0utOXdwxu1BgjFPg_uMp21iSqRd5AXDadxpPqViRNWUuel7sXQhgoEG_bclFje2Z60FjORY7BHW0xZirLnMPWYqp3ezjsOcnabFRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20994" target="_blank">📅 00:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20993">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L12DAMe7kg2ITn4Qk2yRemNOGwoQO9hRMHM55Py0KXWaQuUVLkUVdFjMB-X2H7KbygclDTH8XjsVyhUTfinoC5ultWzrP6rEgdIuN-ByFmbzFoS2zLzxQDTLB0Ghf2pH1QGmfpIYkciE_qXL1pPdTPVHnRQfl6xRe3V_FgSCZZl1rgn0X5El5OGCJ00ON_TK_qbnmOOHW5JeC6w-MS1_HkobdQVNNlyaFJoGt9d16e3B6AMcJEXvxsDys0n3nKJsS1KkBKurBk9DH4iPYSnnLfNpGzoNvUPaMAtZXFTWLZx227V-yqBuGcbFOrcJnI_1SBiGjl0pztYYcdwaM7nckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست در اتاق جنگ  در حال شنیدن گزارش نیروهای مستقر در خط مقدم فرماندهی مرکزی آمریکا (سنتکام) در حوزه‌های هوایی، زمینی و دریایی، از جمله ناو هواپیمابر
USS Abraham Lincoln
، هستم.آمریکایی‌های شگفت‌انگیزی که در حال انجام یک مأموریت تاریخی هستند.
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20993" target="_blank">📅 00:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20992">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e4825bc3.mp4?token=t_JZZlArmjcfSCc8HbMXFZ5kQvtY754_BwOJzNyOzaiTf-lf2C6IAyQfFXZuiMh7ykYI7rZBt-S0fvx_EKrBK-erBJbWZ0e88xeLj8qbK2gxpEfLjVGGTohjC_BG-GySta6g0zjgXa3PHuYhArmgRVNmbq9qz6mWoKGRW1rXEoq0rdiZzLVkMCfPDUS7d70WjiBn92P_fRwdgZ-NTh-J03vrJl_BDBlKnWsuJyDAbqOxVMfE7H5k6jJA9VfrMqN1uc-8ElskNNfPfOexWp6QH9qOn8FIw6ZebQmyYryfUAgFjZ011iLfDBwtOST6SdNtkaHy7xIX8Tttz2UrYA_a1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e4825bc3.mp4?token=t_JZZlArmjcfSCc8HbMXFZ5kQvtY754_BwOJzNyOzaiTf-lf2C6IAyQfFXZuiMh7ykYI7rZBt-S0fvx_EKrBK-erBJbWZ0e88xeLj8qbK2gxpEfLjVGGTohjC_BG-GySta6g0zjgXa3PHuYhArmgRVNmbq9qz6mWoKGRW1rXEoq0rdiZzLVkMCfPDUS7d70WjiBn92P_fRwdgZ-NTh-J03vrJl_BDBlKnWsuJyDAbqOxVMfE7H5k6jJA9VfrMqN1uc-8ElskNNfPfOexWp6QH9qOn8FIw6ZebQmyYryfUAgFjZ011iLfDBwtOST6SdNtkaHy7xIX8Tttz2UrYA_a1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ما قادر به نابودی کل کشور هستیم. ما نمی‌خواهیم این کار را انجام دهیم.
ما تحریم‌های اقتصادی علیه آنها داریم که هیچ کس قبلاً نداشته است.
اگر آنها حمله کنند، ما ۱۰۰ برابر سخت‌تر پاسخ خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20992" target="_blank">📅 00:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20991">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ: ایران همچنان موشک‌هایی دارد، اما این بخش کوچکی از موشک‌هایی است که قبلاً در اختیارش بود.
تولید موشک‌ها در ایران 82 درصد کاهش یافته و توانایی‌های تولیدی آن‌ها تا حد زیادی از بین رفته است.
نرخ تورم در ایران به 350 درصد رسیده و ارزش پول آنها هیچ است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/20991" target="_blank">📅 00:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20990">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ: آن‌ها رهبری ندارند. ما رده‌های اول، دوم و سوم آن‌ها را از بین برده‌ایم. این یکی از مشکلات من است، زیرا کسی وجود ندارد که بتوان با او مذاکره کرد.
ما رادارها و تمام تجهیزات اطلاعاتی پیشرفته و مدرن ایران را نابود کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/20990" target="_blank">📅 00:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20989">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ در مورد ایران:
آنها ۲۱۲ هواپیمای بسیار خوب داشتند که برخی از آنها به طرز درخشانی از طریق اوباما از ایالات متحده خریداری شده بودند.
همه هواپیماهای آنها از بین رفته‌اند.
یکی از مشکلات ایران این است که کسی برای مذاکره وجود ندارد. این یک مشکل است.
این تنها کشور در جهان است که هیچ کس نمی‌خواهد رئیس جمهور شود.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/20989" target="_blank">📅 23:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20988">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ: هیچ کس نمی‌داند که ما در ایران تا چه حد موفق بوده‌ایم.
می‌دانید چه کسی می‌داند که ما در ایران تا چه حد موفق بوده‌ایم؟ خود ایران.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/20988" target="_blank">📅 23:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20987">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ : به همکارانم گفتم: «ما باید سفری به خاورمیانه داشته باشیم، زیرا باید از یک فاجعه بالقوه، یک آتش بسیار بزرگ که مثل آن را قبلاً ندیده‌اید، جلوگیری کنیم.»
وقتی مجبورید برای بنزین خود کمی بیشتر هزینه کنید، من هرگز عذرخواهی نخواهم کرد. من کار درستی انجام دادم.
یک کشور بسیار بد، نباید سلاح هسته‌ای داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/20987" target="_blank">📅 23:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20986">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ درباره ایران:
جنگ با ایران، خدمت بزرگی به جهان است و ما کار فوق‌العاده‌ای انجام می‌دهیم.
من هرگز عذرخواهی نخواهم کرد، من کار درستی انجام میدهم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/20986" target="_blank">📅 23:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20985">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ: اگر ایران به ما حمله کند، ما با صد برابر قدرت بیشتر پاسخ خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/20985" target="_blank">📅 23:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20984">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ: ما نمی‌توانیم اجازه دهیم که ایران به مسیر فعلی خود ادامه دهد. اگر ما آن‌ها را با بمب‌افکن‌های B-2 مورد حمله قرار نمی‌دادیم، آن‌ها سلاح هسته‌ای به دست می‌آوردند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/20984" target="_blank">📅 23:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20983">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ درباره ایران: من هرگز عذرخواهی نخواهم کرد، من کار درستی انجام دادم.
ایران، بدترین حامی تروریسم در جهان است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/20983" target="_blank">📅 23:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20982">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ در مورد ایران: آمریکا قرار است زین پس هزینه بسیار کمی برای بنزین بپردازد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/20982" target="_blank">📅 23:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20981">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ درباره ایران: محاصره اقتصادی، دیواری فولادی است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20981" target="_blank">📅 23:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20980">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acb3349271.mp4?token=kgaEp44PRHPCMfczfnzAzu3xtzr7MPe9sK_qFWZ0_CkLw8XKwhu8JCv8P53ljN7ASNMiyTvuFQf1SghK400Wl90ENblGRLEJPwAUoDL_Njd0E1lNoFTkAhQd7EgaKjhmd8sVKPovuhPNMvA1qRgLP7Bczsy4vBAoX22S8YrdFjzFaSmguEbUxjXJEqXrt2km_4Jadd_gA8F7ebWUh8vM88_hMgCYcb0rxX4DxaxJ0ZvCEy4w-Op4Ct95iIcu-waNMT0H5hALYXFdXcvPMFvHnFua2Sxi4tBBaiCr4KZz8kvSn6TVe-Bh4A6OM3JBlL-_maNy-U6C-Vv313jXUx8S-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acb3349271.mp4?token=kgaEp44PRHPCMfczfnzAzu3xtzr7MPe9sK_qFWZ0_CkLw8XKwhu8JCv8P53ljN7ASNMiyTvuFQf1SghK400Wl90ENblGRLEJPwAUoDL_Njd0E1lNoFTkAhQd7EgaKjhmd8sVKPovuhPNMvA1qRgLP7Bczsy4vBAoX22S8YrdFjzFaSmguEbUxjXJEqXrt2km_4Jadd_gA8F7ebWUh8vM88_hMgCYcb0rxX4DxaxJ0ZvCEy4w-Op4Ct95iIcu-waNMT0H5hALYXFdXcvPMFvHnFua2Sxi4tBBaiCr4KZz8kvSn6TVe-Bh4A6OM3JBlL-_maNy-U6C-Vv313jXUx8S-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران: به زودی تنگه هرمز را جزو قلمرو ایالات متحده اعلام خواهم کرد.
ایران به شدت شکست خورده است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20980" target="_blank">📅 23:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20979">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">لحظاتی پیش حمله هوایی اسرائیل به المنصوری در جنوب لبنان انجام شد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/20979" target="_blank">📅 23:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20978">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کاخ سفید: به مجازات ایران و فلج کردن اقتصاد آن ادامه می‌دهیم. ابزارهای بیشتری برای اعمال فشار علیه ایران در اختیار داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20978" target="_blank">📅 22:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20977">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آنا کلی، معاون سخنگوی کاخ سفید، درباره ناو هواپیمابر لینکلن:
رئیس جمهور ترامپ بیش از هر کسی به سربازان اهمیت می‌دهد.
به یاد داشته باشید که جو بایدن تمرکز را از جنگجویان به سیاست‌های حمایت از نیروهای دفاعی تغییر داد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20977" target="_blank">📅 22:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20976">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">به گزارش کانال 13 اسرائیل، اسرائیل قصد داشته به مواضع ترکیه در سوریه حمله کند، اما ترامپ مداخله کرده و مانع آن حمله شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20976" target="_blank">📅 22:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20975">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ced329bda.mp4?token=orOmB8WRICkVQczY9tyV9bxLkab3pJfavYvfLN_nec6g64-DECiiUBNnYE70TW_P_M14MocVFM0RTpMddkn84MIEVlqohO-MZh3cSmblt3k8uYOoE6cHBBc5k2FMt3sGe2oWEtqxzbupAgVEU_T9XISLHx4jZlgoX7QV3S2kPbaRuIrP2HBo5n-Pqg8ewh91DJ68bGwlL4vbviQpsq2rAGUYbgBIW1bAeZqK5zwTcLxDUCsLYkLVd8SIc8qIuft2YKEVgWrqkJamix83CMsmOB8wz6VDyJxAQ2CkGxAnk62bF1c6TryFSDdZXhuqx4dyDaULRI3Y1D0srEe05NN3qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ced329bda.mp4?token=orOmB8WRICkVQczY9tyV9bxLkab3pJfavYvfLN_nec6g64-DECiiUBNnYE70TW_P_M14MocVFM0RTpMddkn84MIEVlqohO-MZh3cSmblt3k8uYOoE6cHBBc5k2FMt3sGe2oWEtqxzbupAgVEU_T9XISLHx4jZlgoX7QV3S2kPbaRuIrP2HBo5n-Pqg8ewh91DJ68bGwlL4vbviQpsq2rAGUYbgBIW1bAeZqK5zwTcLxDUCsLYkLVd8SIc8qIuft2YKEVgWrqkJamix83CMsmOB8wz6VDyJxAQ2CkGxAnk62bF1c6TryFSDdZXhuqx4dyDaULRI3Y1D0srEe05NN3qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های اسرائیلی با انتشار این ویدیو می‌گویند برخلاف تصور رایج، بخش زیادی از پرواز جنگنده‌های اسرائیلی بر فراز ایران نه پرتنش و پیچیده، بلکه شبیه یک پرواز عادی است. به ادعای آن‌ها، اطلاعات لحظه‌ای از موقعیت سامانه‌های پدافندی در اختیار خلبانان قرار می‌گیرد؛ تا جایی که این تصاویر از آسمان تهران، بیشتر به یک پرواز معمولی شباهت دارد تا مأموریتی در دل خاک دشمن
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20975" target="_blank">📅 21:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20974">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">امشب تا صبح بیدارم
🙌🏾
روال هر هفته</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20974" target="_blank">📅 21:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20973">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سیریک گزارش صدای انفجار/پرتاب موشک/پهپاد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20973" target="_blank">📅 21:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20972">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1310e64db.mp4?token=oAImxmd-ECaDsuKtBSj6hjW4o-pAzby35RXi10Oo6k1r9EBjMZxgH8cVzSvlhbO-jh-sy8E7-W8wbLaR3P1hnyjwf7VAmcdwnzI56ZkjaAEHnP48uzDAlNfFgSw7vERfLNKef-6NFZqh416XVcWEj72K6rC_tmnP-6vmidqB3i8gvJfWCuSsyZH0jmbgPyUHw2AC9BIpM7SRkpgv_DzA-t9r-sr0Xgdk89LMgiA8Tn5l6XVvowWKAoL4aLIUTu6XjF8DJVCRQouHuEfVq0DwGUWzzRmJfQKtJeLGJQc3JiEVOdxJdOcV5ZlmQOPLxen0PCAoxxo-kqMDiQb01Ia0SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1310e64db.mp4?token=oAImxmd-ECaDsuKtBSj6hjW4o-pAzby35RXi10Oo6k1r9EBjMZxgH8cVzSvlhbO-jh-sy8E7-W8wbLaR3P1hnyjwf7VAmcdwnzI56ZkjaAEHnP48uzDAlNfFgSw7vERfLNKef-6NFZqh416XVcWEj72K6rC_tmnP-6vmidqB3i8gvJfWCuSsyZH0jmbgPyUHw2AC9BIpM7SRkpgv_DzA-t9r-sr0Xgdk89LMgiA8Tn5l6XVvowWKAoL4aLIUTu6XjF8DJVCRQouHuEfVq0DwGUWzzRmJfQKtJeLGJQc3JiEVOdxJdOcV5ZlmQOPLxen0PCAoxxo-kqMDiQb01Ia0SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : این کشتی با یک کشتی یکسان (جرج واشنگتن) جایگزین میشود
خبرنگار: خانواده‌های نظامیان نگرانند از شرایط ناو لینکلن
ترامپ : «نه، آن‌ها نگران نیستند.»
خبرنگار: آیا این استقرار نظامی بیش از حد طولانی شده است؟
ترامپ: «نه، نه، نه؛ حتی نزدیک به آن هم نیست که بگوییم بیش از حد طولانی شده است.»
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20972" target="_blank">📅 21:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20971">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfefd33ebd.mp4?token=IkCW6mTavH37uvC5-V1-HGI9MMwONEWdssZ9K8KttuUcug8obAe4FH2ET8WvnLmTXvfbuqWJ_d9InyxRN8qMDweLZaW34H-Sm5F9-nJJYqOuwYiWbZlYG6Bc8mK6XA6Xq_GPjGjx5Xad1ZzhJXzNs3-5aapEcTRn5CcN2nilVcR8ep1r3F5rK-MQKV8IMQHBGDJLytqf-7FPM8C_krbU_moRbTUXZHcqUrY6cBlh7TGIdGYLqS_TFpC827xGssYyS47GWYEXUfynNPpzZH6t3kSx4kAIEPjj6O_rrSfWHk92IKQKT3wkQmXOnZQU7wPR_5Ky8SN7eiyxy4ssfrXl7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfefd33ebd.mp4?token=IkCW6mTavH37uvC5-V1-HGI9MMwONEWdssZ9K8KttuUcug8obAe4FH2ET8WvnLmTXvfbuqWJ_d9InyxRN8qMDweLZaW34H-Sm5F9-nJJYqOuwYiWbZlYG6Bc8mK6XA6Xq_GPjGjx5Xad1ZzhJXzNs3-5aapEcTRn5CcN2nilVcR8ep1r3F5rK-MQKV8IMQHBGDJLytqf-7FPM8C_krbU_moRbTUXZHcqUrY6cBlh7TGIdGYLqS_TFpC827xGssYyS47GWYEXUfynNPpzZH6t3kSx4kAIEPjj6O_rrSfWHk92IKQKT3wkQmXOnZQU7wPR_5Ky8SN7eiyxy4ssfrXl7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه های رژیم : دود مشاهده شده تو جنوب تهران مربوط به آتش زدن ضایعات پلاستیکیه ( عمو پلاستیکیاهو )
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20971" target="_blank">📅 21:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20970">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">داعش شروع به تهدید علیه اسپانیا کرد
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20970" target="_blank">📅 20:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20969">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79dd6977b1.mp4?token=KviXypy9zVwAQy8y8nSZob3a4Z4ETgrbSX6b3IMlwAfNP5KngPDfqs3Smu_dLO4ooTFg3ezdl0bNj022whbCuqxBvsH47ssxslZVYAB_3QblkTrIIk7CR2G6_0ffyONIXRr72D0KPkIUaAXRur32893sQhH8c6n0r2Anup69jPkgiDnAS25ONMtpDRRhjjF2I4jHkuicFLs8c-QU6D5qWQtE52KcT1xzmDuNM1j0ZWomGcYvEJZhxxvgXVHmLd6m5NmnShEJWVVYZLoCM8lwbqHzgDCb4rEX9qUmyojXze-PeR8sJqBAgWKdZfzM9Thy3fBRrdu9vUl7vNEZzZYgiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79dd6977b1.mp4?token=KviXypy9zVwAQy8y8nSZob3a4Z4ETgrbSX6b3IMlwAfNP5KngPDfqs3Smu_dLO4ooTFg3ezdl0bNj022whbCuqxBvsH47ssxslZVYAB_3QblkTrIIk7CR2G6_0ffyONIXRr72D0KPkIUaAXRur32893sQhH8c6n0r2Anup69jPkgiDnAS25ONMtpDRRhjjF2I4jHkuicFLs8c-QU6D5qWQtE52KcT1xzmDuNM1j0ZWomGcYvEJZhxxvgXVHmLd6m5NmnShEJWVVYZLoCM8lwbqHzgDCb4rEX9qUmyojXze-PeR8sJqBAgWKdZfzM9Thy3fBRrdu9vUl7vNEZzZYgiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیوزمکس: وقتی یک دموکرات می‌گوید «ایران هیچ‌وقت قوی‌تر از این نبوده»، واکنش شما چیست؟
وزیر خزانه‌داری بسنت: آنها بی‌اطلاع، دیوانه و فاقد هرگونه درک از چیزی هستند که درباره آن صحبت می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20969" target="_blank">📅 17:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20968">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">واشنگتن‌پست: ترامپ حتی در برابر کنگره نیز دست بالا را دارد
واشنگتن‌پست در تحلیلی می‌نویسد قدرت رئیس‌جمهور آمریکا در تصمیم‌گیری درباره جنگ، طی دهه‌ها افزایش یافته و کنگره عملاً ابزار محدودی برای متوقف کردن رئیس‌جمهور دارد. حتی اگر در آینده هر دو مجلس کنگره علیه جنگ رأی دهند، رئیس‌جمهور می‌تواند در برابر چنین تصمیم‌هایی مقاومت کند و در صورت تبدیل شدن آن به قانون، از
حق وتو
استفاده کند؛ وتویی که تنها با رأی دوسوم هر دو مجلس قابل لغو است.
این تحلیل در عمل نشان می‌دهد که
نتیجه انتخابات میان‌دوره‌ای به‌تنهایی لزوماً اختیار ترامپ برای ادامه یا پایان دادن به جنگ را از بین نمی‌برد
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20968" target="_blank">📅 16:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20967">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وزارت جنگ ایالات متحده با شرکت‌های "بوئینگ" و "آر‌تی‌اکس" قرارداد بست تا تولید قطعات یدکی موشک‌های SM-3 را افزایش دهد.
این موشک‌ها برای رهگیری موشک‌های بالیستیک در خارج از جو زمین طراحی شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20967" target="_blank">📅 16:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20966">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPfMxpMXul2jJCNHfGzxs1fH0JoyHtcFt4LumCGzhDK3fU2GrE7-HMEtvI8OdPAdtZY2U9hHPyApo4BzHeX2LcbxkotoYCKw38HvWggi5T7kWMh30_xzAuG8pUu2H2IPxf5CQxaiehUH8VxVs5OUpHD7Ih2nfXlnDoYffjC2KZay6NydAn74OJBLhj2bCW2vnuVPhQpM9bGcQ38hgWToSdBpXERYXWbimqmum2qswMz590tfw9j6atAcOnfQbz9Oq-LYfoWZEdgKeBmOa_m5Ttnz6-wGJnmgMdGGCJ4O0uexPNjJ1X3J631X7-j4VvJWc-2SeWCJY2pipNNBQZgT1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ در تروث :
نیوزمکس : ایالات متحده با انزوای اقتصادی بی‌سابقه‌ای به ایران ضربه خواهد زد
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20966" target="_blank">📅 15:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20965">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ادعای وال‌استریت‌ژورنال:
ایران و عمان در حال نهایی کردن پیش‌نویس توافقی برای بازگشایی تنگه هرمز بودند که به تهران اجازه نظارت بر کشتی‌هایی که وارد خلیج فارس می‌شوند را می‌دهد، اما اجازه نمی‌دهد عوارض یا هزینه‌های خدمات دریافت کند.
طرفین در مورد نکات اصلی پیش‌نویس که یک خط ورودی در نزدیکی ایران و یک خط خروجی در نزدیکی عمان ایجاد می‌کند  توافق کرده‌اند و آن را با آمریکا، کشورهای منطقه و رهبران ارشد ایران به اشتراک گذاشته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20965" target="_blank">📅 15:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20964">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اکسیوس : به گفته دو نفری که اخیراً با ترامپ درباره نتانیاهو گفت‌وگو کرده‌اند، ترامپ گفته است: “بی‌بی بزرگ‌ترین دشمن خودش است.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20964" target="_blank">📅 15:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20963">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اکسیوس : دونالد ترامپ با وجود درخواست‌های مکرر، هنوز از حمایت رسمی بنیامین نتانیاهو در آستانه انتخابات ۲۷ اکتبر اسرائیل خودداری کرده است. در حالی که نظرسنجی‌ها نشان می‌دهد ائتلاف نتانیاهو از اکثریت لازم برای تشکیل دولت فاصله دارد و رقبای او پیشتاز هستند، اختلافات واشنگتن و تل‌آویو بر سر ایران، غزه، لبنان و سیاست‌های منطقه‌ای افزایش یافته است. مقام‌های آمریکایی می‌گویند ترامپ از برخی تصمیم‌های نتانیاهو ناراضی است و ضعف او در نظرسنجی‌ها نیز تمایل رئیس‌جمهور آمریکا برای ورود به رقابت انتخاباتی اسرائیل را کاهش داده است. با این حال، کاخ سفید همچنان امیدوار است دولت اسرائیل در اجرای طرح صلح غزه، مذاکرات منطقه‌ای و برنامه‌های آمریکا برای توافق احتمالی میان اسرائیل و عربستان همکاری کند
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20963" target="_blank">📅 15:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20962">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e612920df0.mp4?token=qZx1z-eFgm9_H-dC0odqGyQtyA0sEaVJxejRASuMxTsuoECrJRJnY6RfalxB9lLXLaw2CayirUpKctoJLebq55BnARm3vKf3_GmEjNnWVWjP-MDYXIImGX9yd4TTK3ISJxHD_RwUFK_L34ZCVtpNIoBmoMzwyCK06w9INlj8Q2plZhOrOj-mSxFn-5-Iy3nL4Xwg44QIStJR1-rS8Rv18asEhHl7jANrEExLoVxx3IY8xUDobC_R8kunApBEFkzA9VFd0VW9iyvE8JB4y2nuc3-GO63qFJnCFvhIS-MzzK9Iwhe3ZYET4CYf-v7T64lIELJ696FCUQrjuKZUl3tN5hZf99Pr76dj-H8TlKe7KiZa2KHbc5pT6GztbrK4_P6LsSXIBwwA7EX8fW4PUohHqzxfKP2UXBNpNDxgsAk8-B7w0QB0yg1QcjPYEKyhYK_BScEasG02f-t4ugnD5M8cBWtyPzs97X3WY23hCc21yY8yCg78He6DNl8SX1Jo3kPszXslRYi9CXYlMyc6rpDTeGuuaG2BBpFgDOQLv-gStiM7SxReqAxKGftr7C9JS03Zebm0HqbL8huhtlgODkmXIGZI3B901G2KN0FYcLMOKaPwWUmyqxiB3Wy73IHccHd_ZOVE20YrGlTdTuEWLewuaEfDdQNCSC76U6Ql-r2VNVc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e612920df0.mp4?token=qZx1z-eFgm9_H-dC0odqGyQtyA0sEaVJxejRASuMxTsuoECrJRJnY6RfalxB9lLXLaw2CayirUpKctoJLebq55BnARm3vKf3_GmEjNnWVWjP-MDYXIImGX9yd4TTK3ISJxHD_RwUFK_L34ZCVtpNIoBmoMzwyCK06w9INlj8Q2plZhOrOj-mSxFn-5-Iy3nL4Xwg44QIStJR1-rS8Rv18asEhHl7jANrEExLoVxx3IY8xUDobC_R8kunApBEFkzA9VFd0VW9iyvE8JB4y2nuc3-GO63qFJnCFvhIS-MzzK9Iwhe3ZYET4CYf-v7T64lIELJ696FCUQrjuKZUl3tN5hZf99Pr76dj-H8TlKe7KiZa2KHbc5pT6GztbrK4_P6LsSXIBwwA7EX8fW4PUohHqzxfKP2UXBNpNDxgsAk8-B7w0QB0yg1QcjPYEKyhYK_BScEasG02f-t4ugnD5M8cBWtyPzs97X3WY23hCc21yY8yCg78He6DNl8SX1Jo3kPszXslRYi9CXYlMyc6rpDTeGuuaG2BBpFgDOQLv-gStiM7SxReqAxKGftr7C9JS03Zebm0HqbL8huhtlgODkmXIGZI3B901G2KN0FYcLMOKaPwWUmyqxiB3Wy73IHccHd_ZOVE20YrGlTdTuEWLewuaEfDdQNCSC76U6Ql-r2VNVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیپلر
: ترافیک دریایی از تنگه هرمز در ۱۳ اوت افزایش یافت و ۱۳ عبور تایید شده ثبت شد که نشان‌دهنده رشد ۴۴ درصدی نسبت به روز قبل (۹ عبور) است. نه کشتی از طرح یک‌جانبه ایران استفاده کردند، هیچ عبوری در سیستم جداسازی ترافیک هرمز تایید نشد و چهار مسیر نامشخص باقی ماند.
فعالیت در باب‌المندب پایدارتر بود و ۲۹ عبور تایید شده ثبت شد که ۴ درصد بیشتر از ۲۸ عبور روز قبل است. هجده کشتی وارد دریای سرخ شدند و ۱۱ کشتی از آن خارج شدند، در حالی که دو عبور تاریک ثبت شد. در طول روز هیچ حمله جدید تایید شده‌ای به کشتی‌ها گزارش نشد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20962" target="_blank">📅 14:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20961">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f327dcc92.mp4?token=e0n1UwfKTznR2sGqPWSCL26VU8aULS2sLsMcjtVgKq9hYUX4cMTwRQ2rxK-fSXFsJ_hwF5ntN5i25_-6qmh-CHRB9e0xWdPyNugyc-hCxedsMYiwWQ-OLZDZNb9YICp0rkOiJy08SgFcNwSJSDiH1lDQFOb1KW0oicVMO_t0UpfOAWCt7NRxRnkqTcbF0NaJSGgW7NN66WbyJLlr8q3wZTEXFiqELoVBafyGDE82TKYvmpOuBVuIoFSR1lxGN58j6urJRizv8hQeQ_fDamao58mgeRx4h7m52wqPW5tSCaQYc_N-q9ngzJCVlLmRVibZT2slsWg86RvmwYEEsTbbdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f327dcc92.mp4?token=e0n1UwfKTznR2sGqPWSCL26VU8aULS2sLsMcjtVgKq9hYUX4cMTwRQ2rxK-fSXFsJ_hwF5ntN5i25_-6qmh-CHRB9e0xWdPyNugyc-hCxedsMYiwWQ-OLZDZNb9YICp0rkOiJy08SgFcNwSJSDiH1lDQFOb1KW0oicVMO_t0UpfOAWCt7NRxRnkqTcbF0NaJSGgW7NN66WbyJLlr8q3wZTEXFiqELoVBafyGDE82TKYvmpOuBVuIoFSR1lxGN58j6urJRizv8hQeQ_fDamao58mgeRx4h7m52wqPW5tSCaQYc_N-q9ngzJCVlLmRVibZT2slsWg86RvmwYEEsTbbdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش اسرائیل در حال انفجار ساختمان‌ها در منطقه روستای شیعه‌نشین مرکبا در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20961" target="_blank">📅 13:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20960">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">از امشب ۳ شب مست میکنم
😂
🙌🏾</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20960" target="_blank">📅 12:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20959">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBoYTSDbmM-zhvNkadVnRZEgSQAlsv_GKxhjlmMl5xWULa10V1WBMeqPMTdAAJcOOiQTJopNgeGTKS0t0aHD2kG95EvGCk43P1o7wefI6CdhzROK5sxbyyn7OV8ePArxQ5BVbhiTZpCWDYUmOhqfg0F9DI9Gs0NecNhRxpaVk_KARv-x_YdyhlIdH0VNKPztlN-9lRQZR7iQ3AWMKCgNJ8QsXbu52WqsnM81TLPQ0Pqp702kDtVD8h0fjlYNXPxcj5bgFhHW9ugqEIFmrlFRQ0pq_vKNViez6FZwPEOyIbxaUGO1dUlqxR5G_4AwheXRUhUf5edXEhTBiI4s-D_RAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
بر اساس گزارش‌های دریافتی این سازمان از مراجع نظامی، یک نفتکش هنگام عبور خروجی از تنگه هرمز هدف یک پهپاد (UAV) قرار گرفته است. این شناور دچار خسارت جزئی شده، اما تمامی اعضای خدمه در سلامت هستند و حضور همه آن‌ها تأیید شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20959" target="_blank">📅 11:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20958">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‎ اتاق جنگ با یاشار : فلورا جون سر گردنه
هم مسیر شدن ناو هواپیمابر جورج
واشنگتن با یک کشتی کارگو ایرانی به نام «فلورا»که بسیار زیاد شبیه به عکس کاور مجله اکونومیک ۲۰۲۶ است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20958" target="_blank">📅 11:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20957">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5efb82e574.mp4?token=TI06CWZB9XD5V4c6tGDQrMx-4Fc74PQlR1iHtX-yNACNut7Gs-WkDsB-jvgsQHehvTNmpEO6UR3ZDbnVKwUuEw9Dttq87kqollmK9GsKdXrYo4x6RROHqOZniCv-4z2XU0igtx0m0RlDBxOhIDnSt_kLcN-AEPJW4FdGkaDCrY9lEOhuCm1bqatcEJrjgzCVG2j-junaRB5LO6sI6641Sc8qpeFpwtS3dmh0e_g-POD2If5K0Bbfg9kNz8AYMohsS5OXyxAiDODVtK2YE41tnr3EJZGDYYypI4npGeu1K0JCt4NNyg7jH7nCpYNUcp_HQV740LCJJKf3aFTDtmK6xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5efb82e574.mp4?token=TI06CWZB9XD5V4c6tGDQrMx-4Fc74PQlR1iHtX-yNACNut7Gs-WkDsB-jvgsQHehvTNmpEO6UR3ZDbnVKwUuEw9Dttq87kqollmK9GsKdXrYo4x6RROHqOZniCv-4z2XU0igtx0m0RlDBxOhIDnSt_kLcN-AEPJW4FdGkaDCrY9lEOhuCm1bqatcEJrjgzCVG2j-junaRB5LO6sI6641Sc8qpeFpwtS3dmh0e_g-POD2If5K0Bbfg9kNz8AYMohsS5OXyxAiDODVtK2YE41tnr3EJZGDYYypI4npGeu1K0JCt4NNyg7jH7nCpYNUcp_HQV740LCJJKf3aFTDtmK6xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویکتور دیویس هنسون
تاریخ‌دان، نویسنده و تحلیلگر سیاسی محافظه‌کار آمریکایی و پژوهشگر ارشد مؤسسه هوور است. او از حامیان شناخته‌شده دونالد ترامپ به شمار می‌رود، کتابی در دفاع از ترامپ نوشته و دیدگاه‌هایش در رسانه‌های محافظه‌کار آمریکا بازتاب گسترده‌ای دارد, وی پیشنهاد کرده است ترامپ از شاهزاده رضا پهلوی حمایت کند و زمینه تشکیل یک دولت ایرانی در تبعید تحت رهبری ایشان و با مشارکت ایرانیان را برای جایگزینی رژیم جمهوری اسلامی را فراهم سازد.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20957" target="_blank">📅 09:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20956">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هشدار خزانه‌داری آمریکا: تحریم‌های «بی‌سابقه» علیه ایران از هفته آینده
اسکات بسنت، وزیر خزانه‌داری آمریکا، اعلام کرد دولت ترامپ هفته آینده از بسته‌ای جدید از تحریم‌ها و اقدامات اقتصادی علیه ایران رونمایی می‌کند که به گفته او «در تاریخ بی‌سابقه» خواهد بود. جزئیات این اقدامات قرار است هفته آینده به‌صورت رسمی منتشر شود. این بسته بخشی از تشدید سیاست «فشار حداکثری» واشنگتن است و انتظار می‌رود بر مسدود کردن مسیرهای دور زدن تحریم‌ها، ناوگان سایه و کانال‌های مالی و ارزی ایران تمرکز داشته باشد؛ اقدامی که با هدف افزایش فشار اقتصادی بر تهران پیش از هر تحول دیپلماتیک یا نظامی دنبال می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20956" target="_blank">📅 09:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20955">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حقیقت یاب سنتکام در جواب به رسانه های رژیم :  ناو هواپیمابر «یو‌اس‌اس آبراهام لینکلن» همچنان یکی از بالاترین نرخ‌های تمدید خدمت خدمه را در میان تمام ناوهای هواپیمابر نیروی دریایی ایالات متحده دارد؛ این نرخ ۸۴.۴ درصد است. ملوانان و تفنگداران دریایی گروه رزمی ناو هواپیمابر آبراهام لینکلن، پس از بیش از ۲۶۰ روز حضور در دریا، انجام ۱۰ هزار پرواز و مصرف ۱.۵ میلیون پوند مهمات، همچنان مقاوم و مصمم باقی مانده‌اند. هیچ‌یک از نیروهای نظامی حاضر در این ناو هواپیمابر جان خود را از دست نداده‌اند و تنها ملوانی که در ۳ اوت به دریا افتاد، به‌سرعت و در سلامت کامل پیدا و نجات داده شد. گزارش‌های گسترده و نادرست درباره مأموریت تاریخی آبراهام لینکلن، در حق زنان و مردان نظامی ما و خانواده‌هایشان بی‌انصافی است
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20955" target="_blank">📅 03:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20954">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">هم اکنون حملات شدید پهپادی جمهوری اسلامی به مواضع گروه های کورد در اربیل عراق
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20954" target="_blank">📅 03:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20953">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">چند گزارش داشتم از صدای تیر اندازی سمت غرب (محدوده آزادی)
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20953" target="_blank">📅 02:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20952">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ به فاکس نیوز ‌: محاصره دریایی ایالات متحده در تنگه هرمز کاملاً برقرار است و «یک دیوار فولادی» است.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20952" target="_blank">📅 02:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20951">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGGldxYsVTUGTQo8ItRmI61XZexT3LvaG6YG6cCDg2Qn--fzzob1jUCPz0FZ_S2OWGosaqIF1zXd8GwrJxemTFnZQEbQV7aYzarQuO35to3GlGqEhq-dR64s81-kAehLT_FRE8-Dn6yiK4fgahPF6igjcmEZLwqrGVYcgRhQX_RwKyrbkplWkgT6cG7sUSBqVRNNknt6fxjCLCJR2BRZZXVwCX1d_jAJw3PeSKRgbNk4yl6A7u9UBpoCeF-i1q3a-La_1ArSQsvMkWkPhoSl0MAypK878-C04LkaFfRcHRrGbQt_Xi0U5oDAi3ZSWlZ9rK-0z7O3nIV8H6W8fzEHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای F/A-18C هورنت معمولی نسل اول برای تفنگداران دریایی آمریکا، از سمت تنگه هرمز با ترانسپوندر روشن( فعال بودن سیستم شناسایی و ارسال اطلاعات موقعیت ) با یک چرخش در ابوظبی فرود آمد.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20951" target="_blank">📅 02:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20950">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بعد از مدتها حتی‌ اطراف تنگه هم سوخترسان دیده نمیشه عجیبه…</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20950" target="_blank">📅 01:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20949">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50455ef10.mp4?token=hyJsDvQXe5EQbTh7YgdC5ynk2u3tmsy0EyrsydgGmtPS4P9477yPIBjvBnCIsNPF-xd4xbtIqWWiSHz-WxdVMqtM4PQMh5VTLI0z_e8JgxYesKcyF-ltuJF_mhF1jgipdWJwdiV2xp93_mgfVhQOpSBw5TQVNQbULqJodtKIOxHNO9cGy73gofX1693KzGU35fnZucphqJ8ziDt_AdFKSM4xBBUgXCTE0a_7dmxD7ytnULp6MFB456oLvYDSCtZxpRkPu1waNYtg_GfdToQtUa5EYd2lPQLzPAaDAJ1ctonazNJgSQzr98dhc3Ni9f5MZcV9SevGt5NcuObfy9M-bAjRy017Ge6Nnu6WUQaVI5Z5nuQw171v9XuOJNBgPOWamtbhAsaqea660EPRJ9VHLFksVNFS9R_7mPqXJFS1WfG-LNdY_zPhBK6YhXTMxFWdgZAWX0wyehW2No6Z-9PuWAysDi-MzPQ_-5FSbuwQjTVh2crHw0pF3kZKkPuq6HBiAAQSME1V85kcyrYN5w3TgUW5hqnInbDQlz47elqHOWheBdKIpjx6THA3QrXSxacyVQNXmI3CaEC5Pi4ZcU2arNMz9MTZ5tS2nxObuZUrp-no_t1g07Fg-RI-tjSyQ3LlP05HukG4X5PigCbJuBE_K4FtxrxwZ2Uw8t9pF2bTRVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50455ef10.mp4?token=hyJsDvQXe5EQbTh7YgdC5ynk2u3tmsy0EyrsydgGmtPS4P9477yPIBjvBnCIsNPF-xd4xbtIqWWiSHz-WxdVMqtM4PQMh5VTLI0z_e8JgxYesKcyF-ltuJF_mhF1jgipdWJwdiV2xp93_mgfVhQOpSBw5TQVNQbULqJodtKIOxHNO9cGy73gofX1693KzGU35fnZucphqJ8ziDt_AdFKSM4xBBUgXCTE0a_7dmxD7ytnULp6MFB456oLvYDSCtZxpRkPu1waNYtg_GfdToQtUa5EYd2lPQLzPAaDAJ1ctonazNJgSQzr98dhc3Ni9f5MZcV9SevGt5NcuObfy9M-bAjRy017Ge6Nnu6WUQaVI5Z5nuQw171v9XuOJNBgPOWamtbhAsaqea660EPRJ9VHLFksVNFS9R_7mPqXJFS1WfG-LNdY_zPhBK6YhXTMxFWdgZAWX0wyehW2No6Z-9PuWAysDi-MzPQ_-5FSbuwQjTVh2crHw0pF3kZKkPuq6HBiAAQSME1V85kcyrYN5w3TgUW5hqnInbDQlz47elqHOWheBdKIpjx6THA3QrXSxacyVQNXmI3CaEC5Pi4ZcU2arNMz9MTZ5tS2nxObuZUrp-no_t1g07Fg-RI-tjSyQ3LlP05HukG4X5PigCbJuBE_K4FtxrxwZ2Uw8t9pF2bTRVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز : آقای معاون رئیس‌جمهور، یک لحظه به توافق نزدیک هستیم، لحظه بعد می‌گوییم قرار است حسابی آنها را بمباران کنیم. یک لحظه تنگه هرمز باز است، لحظه بعد بسته است. مطمئنم این نگرانی و سرخوردگی داخل کاخ سفید هم وجود دارد. می‌دانم پیش‌بینی کردن دشوار است، اما اجازه دهید بپرسم:
این ماجرا چگونه تمام می‌شود؟ اگر و زمانی که مسئله ایران تمام شود، وضعیت چگونه خواهد بود؟
جی‌دی ونس:
خب ویل، چیزی که با اطمینان می‌توانم بگویم این است که فکر می‌کنم این ماجرا با
قرار گرفتن ایالات متحده در موضعی قدرتمندتر
پایان خواهد یافت؛ در شرایطی که ایران
سلاح هسته‌ای نداشته باشد
و
تنگه هرمز دوباره به وضعیتی بازگردد که قیمت نفت و گاز برای مردم آمریکا باثبات باشد
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20949" target="_blank">📅 00:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20948">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ونس، معاون رئیس جمهور آمریکا: آمریکا ابزارهای زیادی برای مقابله با ایران در اختیار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20948" target="_blank">📅 00:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20947">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اکسیوس : جرد کوشنر، فرستاده ویژه رئیس جمهور ترامپ، قرار است هفته آینده به اسرائیل سفر کند و با نتانیاهو دیدار کند
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20947" target="_blank">📅 23:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20946">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رویترز : ترامپ در آستانه یک جنگ پیچیده‌تر قرار دارد و به نظر نمی‌رسد که این مسئله او را رها کند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20946" target="_blank">📅 22:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20945">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گزارش صدای انفجار‌ سیریک ، پرتاب موشک/پهپاد به سمت تنگه هرمز @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20945" target="_blank">📅 22:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20944">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اصفهانی معاون پزشکیان:
تغییر قیمت بنزین در کرمان به‌دلیل برخی بی‌تدبیری‌ها متوقف شد.
۱۴ میلیون لیتر بنزین در هر روز کم داریم
دولت برای بنزین برنامه دارد و روزهای آخر تصمیم‌گیری در مورد آن است.
ما ۳ برنامۀ جدی داریم و هرکدام از آن‌ها نهایی شود، قبل از اجرا آن را به مردم توضیح می‌دهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20944" target="_blank">📅 22:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20943">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/737fe5f83b.mp4?token=k4OEt0DslRr0V2jkphH7TldeiYFLlvWwftdrQPkGsY7sYXmB4CzmKmqP43zk6IBhxyxc9D1qSILNSfkCgUzhwPBgkG5kMpmfG2HCUfcYRs5QIIiPEJ-8Qecvh1AEet5U-t5FR7xB-dxqGgmAOmp_VAUNpMIHCQm91stkBOjyrxYw7uWEDykTLjfqMCTp1OFpHcOCoWjCzQ96rCnk2n1-dz45_VqM9jChz_d7k9JUoP5S8WTgdYOmllSnrXFXPqxuW13O9G473hX0KJcleBjwi6OU38uAGwWdePa3XC6SluNgoXvCCtLxc69nHT4xFNto7btLDDfVboj0CtHliDYxOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/737fe5f83b.mp4?token=k4OEt0DslRr0V2jkphH7TldeiYFLlvWwftdrQPkGsY7sYXmB4CzmKmqP43zk6IBhxyxc9D1qSILNSfkCgUzhwPBgkG5kMpmfG2HCUfcYRs5QIIiPEJ-8Qecvh1AEet5U-t5FR7xB-dxqGgmAOmp_VAUNpMIHCQm91stkBOjyrxYw7uWEDykTLjfqMCTp1OFpHcOCoWjCzQ96rCnk2n1-dz45_VqM9jChz_d7k9JUoP5S8WTgdYOmllSnrXFXPqxuW13O9G473hX0KJcleBjwi6OU38uAGwWdePa3XC6SluNgoXvCCtLxc69nHT4xFNto7btLDDfVboj0CtHliDYxOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست به نیوز مکس : گزارش‌های مربوط به تخریب شرایط در ناو هواپیمابر ابراهام لینکلن کاملاً تحریف‌شده است و  هیچ کم و کسری وجود ندارد
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20943" target="_blank">📅 21:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20942">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سی‌بی‌اس: فقط یک ملوان در پی حادثه از عرشه هواپیمابر آمریکایی "یو‌اس‌اس لینکلن" در اوایل ماه آگوست(۲هفته پیش) به داخل دریا سقوط کرد. این ملوان توسط یک بالگرد جستجو و نجات نجات یافت و پس از دریافت درمان توسط بخش پزشکی، از کشتی منتقل شد تا مراقبت‌های پزشکی بیشتری دریافت کند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20942" target="_blank">📅 21:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20941">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dESio2k5oCX-XMllH1wuPkLaDqZQqR3tLp7jzx9Jz20a3Pd269oIRA3COuoo3mZ4FGi8XUFIfEwGZpgk4AJB1iIlQ3Ao5Y1RF5JBzTeu7MHv1Dw979HUhWqdNUewfpxYftGI-UvP9-XBpYkjtlYhAThU6tJaQy2kD0vJx99rr1DKHmPzwpbKWpW27iuryQNXVrKFEECGobnaYJC8Mr7NWEfTEhRsY8dt539f1YlixGwR42gdaXbG1-wbt_98K_7IbGV0MsabuZAffGbqUCr_G-x7tjQGaOsUKKA9PNgagos_SWRF-UbUdhoJIhRaOKHWreh6FX0vU1UQ6SQ7E3YuQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ با ارسال این عکس نوشت برایم، من در منطقه ای زندگی می‌کنم که همه عرزشی هستند. دقایقی پیش در کرج رعد و برق مهیبی زد. بلافاصله اکثر این ساختمان ها برقهایشان را از ترس حمله هوایی خاموش کردند. اینها از ترس شب و روز ندارند. خودشان هم میدانند به زودی کارشان تمام است. به مردم بگو ناآمید نشوند ، پیروزی نزدیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20941" target="_blank">📅 21:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20940">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یک منبع دیپلماتیک به شبکه خبری ام تی وی لبنان اعلام کرد که مقامات رسمی در بیروت، اطلاعیه مهمی دریافت کرده‌اند مبنی بر اینکه مقامات سیاسی اسرائیل، به ارتش اسرائیل اجازه داده‌اند تا منطقه علی طاهر در ارتفاعات نبطیه را کاملا منفجر کند (گفته میشود در این منطقه صدها نفر از نیروهای حزب‌الله و سپاه پاسداران در تونل‌هایی به دام افتاده‌اند)، انتظار می‌رود به زودی این انفجارها رخ دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20940" target="_blank">📅 21:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20939">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کانال ۱۳ اسرائیل : فرمانده سنتکام، برد کوپر به مقامات اسرائیلی گفته که در تلاشه تا جنگ علیه ایران رو از سر بگیرن چون معتقد است که این جنگ موضع ایران رو در مذاکرات هم تغییر میدهد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20939" target="_blank">📅 20:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20938">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سنتکام قصد دارد یک نیروی جدید پهپادی به نام
«فالکون استرایک»
تشکیل دهد؛ نیرویی چندملیتی که نیروهای آمریکایی و کشورهای منطقه را در یک ساختار مشترک کنار هم قرار می‌دهد. هدف این نیرو استفاده از
پهپادهای تهاجمی یک‌طرفه
(پهپادهایی که پس از حمله به هدف خود نیز از بین می‌روند و شبیه مهمات سرگردان یا «پهپاد انتحاری» هستند) در سه حوزه
هوا، سطح دریا و زیر آب
است. این طرح زیر نظر فرماندهی عملیات ویژه آمریکا شکل می‌گیرد و بر تجربه گروه
«اسکورپیون استرایک»
ساخته می‌شود؛ گروهی که طبق این گزارش، پهپادهای آن پیش‌تر در عملیات علیه ایران استفاده شده‌اند. سنتکام اکنون از کشورهای منطقه دعوت کرده به «فالکون استرایک» بپیوندند تا یک
توان مشترک و یکپارچه پهپادی در سراسر خاورمیانه
برا عملیات ایجاد کنند
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20938" target="_blank">📅 20:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20937">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">از تنگه صدای پول های بلوکه شده میاد
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20937" target="_blank">📅 20:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20936">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گزارش صدای انفجار‌ سیریک ، پرتاب موشک/پهپاد به سمت تنگه هرمز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20936" target="_blank">📅 20:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20935">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW7fPeADpavdwufebjTeGo-NPCFjjMvxvx2eyJoeTg_BvMYhE7e1oGZN2LTw7xbnd83_lL81XkSydj_uvhQu_zxEgfWnk1JEoiMxY103aCGVHUeqX1uIsIgrgCXKlRedRQTSGSnf_JhREkKchxlpeq_10lBp0Pss-N12JysenJBPo-FCO8Q0tdWe5wdaGrppfwekCciWaRaqm4WloAPkYO6bGy9Q1ABchDIUWTdkqJxAzmtwGwqw2Rm1BWAR2JJwLs4ShIfErKLsiBSQ2Oeaw3s4QiKiVitrmRA6tGWwFl56WIERhQKwtJmA1V0t2L5kKKY47J07qM6Bv_yJG7Yjvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هگست وزیر جنگ ، امروز در پاناما و پس از دیدار با خدمه ناوشکن USS Gridley گفت :
محاصره وابسته به حضور یک ناو یا یگان خاص نیست؛ نیروها می‌توانند یکی‌یکی تعویض و جایگزین شوند و بنابراین از نظر نظامی آمریکا می‌تواند آن را برای مدت نامحدود ادامه دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20935" target="_blank">📅 20:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20934">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خبرگزاری حوثی‌ها «سبا» به نقل از یک منبع نظامی گزارش داد که حوثی‌ها با استفاده از دو پهپاد به پالایشگاه شرکت آرامکو در منطقه جیزان عربستان سعودی حمله کردند. همچنین اعلام شد: «این حمله در پاسخ به نقض حریم هوایی یمن توسط سعودی در مناطق صعده و حجه انجام شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20934" target="_blank">📅 19:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20933">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کانال ۱۴ اسرائیل:  رئیس ستاد کل نیروهای مسلح اسرائیل ، ایال زمیر، به وزرای کابینه اعلام کرد که محاصره دریایی ایران بسیار موثر بوده است. طبق ارزیابی‌های اولیه ایالات متحده، مقامات ارشد اکنون بر این باورند که تداوم این فشار شدید اقتصادی هم‌زمان با وخامت سریع بحران مالی داخلی در تهران ،مؤثرترین راهبرد برای وادار کردن رژیم به تسلیم یا زمینه‌سازی برای فروپاشی آن است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20933" target="_blank">📅 19:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20932">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">@WarRoom
بالون</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20932" target="_blank">📅 19:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20931">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee29e07a01.mp4?token=B6eJzY8tTSE0YROviR1boWk4Rw1HghrVdRDzoLUPO1l9zJZqDSUnhbrE_w2PnZ-o9Fa1lnje6dMw68zwQCTN_MGMuC7Q35_R5_NPS2AlgZog8K6u4iHknOYxvXZGvHqsZvvWzfIKjjSKhd6Kv126JkX60_thfS58Bx4zMe_YFgMYwHvAenk_PE-SqXQeunL7CxTGlKo9pnBRPXgeo7HYNsQMml0ToOgCqZtZhibSPcTrwB6bS-jNUbAFyy1bScoUKJ-JIofb0zi1_BVMsrIlPV-OHdPq6MLHphzkXEfqd4cA4yiN8Iw-mHr4d_opqPEIvjb8EySwaS3fqwcP1c5IQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee29e07a01.mp4?token=B6eJzY8tTSE0YROviR1boWk4Rw1HghrVdRDzoLUPO1l9zJZqDSUnhbrE_w2PnZ-o9Fa1lnje6dMw68zwQCTN_MGMuC7Q35_R5_NPS2AlgZog8K6u4iHknOYxvXZGvHqsZvvWzfIKjjSKhd6Kv126JkX60_thfS58Bx4zMe_YFgMYwHvAenk_PE-SqXQeunL7CxTGlKo9pnBRPXgeo7HYNsQMml0ToOgCqZtZhibSPcTrwB6bS-jNUbAFyy1bScoUKJ-JIofb0zi1_BVMsrIlPV-OHdPq6MLHphzkXEfqd4cA4yiN8Iw-mHr4d_opqPEIvjb8EySwaS3fqwcP1c5IQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20931" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20929">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : جوجی‌جون ، ناو هواپیمابر جورج واشنگتون و اسکورتش به سمت منطقه می آیند
🚨
🚨
🚨
کارهای اداری یادتون نره⁩ https://www.instagram.com/reel/Db-HXkWoJz-/?igsh=NHNmZ3ZhYnhhdDJi</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20929" target="_blank">📅 19:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20928">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وال استریت ژورنال : ایالات متحده در بحبوحه تنش‌های جنگ با ایران، ناو هواپیمابر جورج واشنگتون را به خاورمیانه می‌فرستد
@WarRoom
یاشار : خیلی عقبید
😁</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20928" target="_blank">📅 19:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20927">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a73c9be9f.mp4?token=FEp42VJUVY5ui8TTdN9HyLXitPNXyv6_0W-zNbgUNZUCQwmToU9wcr0QTWZf3HxJw3t0TyxvpZyikvZ9UI_GnpnKkEen8nUUOrRZY-VINaJmuqCu9d13YKp1ps_9A9X0Z4rluTbySmZiDshZWzgMYO-JojGXPuvBTHSKgy_wIjd_1Tia3aKPKwYjSPyjmLeKBYjP8LRwNwYLWECWTfHNS350GADd6cxbClmRqLe5oKoLJpY3BJO3qAbMYRNICUErgKLbIg40ke9VBuAbbDXeGBjw2tbRoTJvFa7U73YBbW9MwtiRen-vgZgxlJadxzEAK5mmKl_I2-C_y6CHk5dVcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a73c9be9f.mp4?token=FEp42VJUVY5ui8TTdN9HyLXitPNXyv6_0W-zNbgUNZUCQwmToU9wcr0QTWZf3HxJw3t0TyxvpZyikvZ9UI_GnpnKkEen8nUUOrRZY-VINaJmuqCu9d13YKp1ps_9A9X0Z4rluTbySmZiDshZWzgMYO-JojGXPuvBTHSKgy_wIjd_1Tia3aKPKwYjSPyjmLeKBYjP8LRwNwYLWECWTfHNS350GADd6cxbClmRqLe5oKoLJpY3BJO3qAbMYRNICUErgKLbIg40ke9VBuAbbDXeGBjw2tbRoTJvFa7U73YBbW9MwtiRen-vgZgxlJadxzEAK5mmKl_I2-C_y6CHk5dVcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رابرت اف کندی جونیور:
دانا وایت گفته که او هیچ‌وقت ندیده ترامپ آب بنوشد. او فقط نوشابه رژیمی دایت‌کُک می‌نوشد.
او از هر آدم دیگری که تا حالا دیده‌ام، انرژی بیشتری دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20927" target="_blank">📅 18:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20926">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جمهوری اسلامی از طریق ترکیه به سوریه اطلاع داد که در صورت دخالت ارتش سوریه در لبنان علیه حزب‌الله، صدها نقطه در سراسر سوریه، از جمله کاخ ریاست‌جمهوری، با پهپادها و موشک‌ها مورد هدف قرار خواهند گرفت.
یک تحلیل اخیر هم صراحتاً می‌گوید ترکیه واشنگتن را متقاعد کرده که از دولت احمد الشرع(پیش‌تر با نام ابومحمد الجولانی)در رویارویی با حزب‌الله در لبنان استفاده نکند.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20926" target="_blank">📅 18:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20925">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏اوپک: افزایش تولید نفت کشورهای منطقه در حالی که ایران درجا می‌زند
‏گزارش جدید اوپک نشان می‌دهد تولید روزانه نفت عربستان سعودی، کویت و عراق در مجموع طی ماه گذشته نسبت به ژوئن حدود ۱ میلیون و ۶۴۰ هزار بشکه افزایش یافته، در حالی که افزایش تولید نفت ایران تنها ۲۶ هزار بشکه بوده است. پیش از انسداد تنگه هرمز حدود یک پنجم نفت مصرفی جهان از این آبراه عبور می‌کرد، اما کشورهای عربی حوزه خلیج فارس اکنون با استفاده از مسیرهای جایگزین در دریای عمان و دریای سرخ و روش‌های دیگر، صادرات نفت خود را ادامه می‌دهند. در حالی که همسایگان ایران ظرفیت تولید و مسیرهای صادراتی خود را گسترش می‌دهند، صنعت نفت ایران زیر حاکمیت رژیم جمهوری اسلامی عملاً از این رقابت منطقه‌ای عقب مانده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20925" target="_blank">📅 18:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20924">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYCk_eD3C2ZvvjkMuMX6zFjYJfeMx3RSVHJr-M6ykgfas14aoPgA9xKf34xpNhgNuN7xqgCdd_5wbdMkWc6BALnqYhA166EDKPUFbVVdlALz7LYPaZem7w-wy73zNFDikzGZcYt320t3-Zy8HwB_rG9H22ROfFuaVLCUGFrTq0Q7zWqlBb3_adXl7i3PJlJQC6ds7LnJ50JLS29Z-ksWNs1YvdrVWHhePxJl18XNOlSjPo4yfSKTkVF_ZLyDQtba6fB6J1UVPKf-Rb34lex_PekWXLUOaaSDT8rxV-EiFx_hDRpr1mIY0KhcfAzTwMqsmxbfYopktn_vmlc9h4b5Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : جوجی‌جون ، ناو هواپیمابر جورج واشنگتون و اسکورتش به سمت منطقه می آیند
🚨
🚨
🚨
کارهای اداری یادتون نره⁩ https://www.instagram.com/reel/Db-HXkWoJz-/?igsh=NHNmZ3ZhYnhhdDJi</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20924" target="_blank">📅 18:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20923">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwxxnGJQtpoOkyjzDlBpBLa0o0E_PKg-bqh0IyHrFyeRBBxXxovEeot4Ixa3-HYaCKHVUrnsBtCAyFsyXl7my23MM2cTGQ8pOhanlFTvJ0O98OlXYtc9Brn458BCqBNRK5fhl3s3eMzDHBR4rZTBkvl4s80LDjq-oaKOUaxE6t8lah6dNvusILREPcU2Gt_50WZwWBIXLDHZeD3EkDC9odasJpTlut-mwY7neVsgopghiGMXy5mYT6Lag4qRaUCVOvBFNQagEIAWLtW3gAQsX5MVJswcbjhORUNZF36ikFTbvfPNEFrxOiuY-hU0rdkgJUFkRKfSbMs2ZPEamzajOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عروس معصومه ابتکار(شامپانزه دیوار سفارت) که اقامت دائمش در آمریکا لغو شده، وکیلی حرفه‌ای گرفته و از دولت آمریکا شکایت کرده، به این امید که اقامتش برگردد و غرامتش را از اموال بلوکه‌شده بگیرد. او نامه‌ای خطاب به مردم آمریکا نوشته: «من عاشق آمریکا هستم، فرزندم فارسی بلد نیست و مادربزرگم در اشغال سفارت آمریکا فقط مترجم بود.» استدلال نامه و وکیل ایشان این است که فرزندان نباید به‌جای والدین مجازات شوند
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20923" target="_blank">📅 17:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20922">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8PnWuFhx73pb_rcPybBoi82h-mA3gt380tJKfmxGA7bZVJOnFMtuJwJNXJ88OsH-FinzpIoECNGmlakluhZIvDOn8OKSMxeh7e3vqsurrW-FL4IhkOA5zOUP2ZB-QGFUBpygc-VqYPOFszIQXT5eCHIzYFSdBUwzXmgRNFgbplQyZ0Dkijx5XFKSJcxAb1DibW-YpY5eKaZUCb6DvmFdes5C1blFgvvpd5njgiiZDrrf5Mn2eoAU_noLKgXExFtS7Ur5bf1wkiDHk6TLW7n1GJpogc2PqHzpK9o6y7p-moDKt9En62Nnxx5l2NlJAH3IL96WrT7_rmpgxh8iRtAOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواب بودم ، پیج روزدن
دیر برگردوندم
🙌🏾
😂
instagram.com/yashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20922" target="_blank">📅 17:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20921">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c76aaa280.mp4?token=FotA-24OhZ79a6lrMPsSu-GZrtUtQUCtj4yN5pUnBTI3z6f4yWGLDGgV62vP3F-TZJJYOy1be96ngs6YaZXNLEGNYEr63oG9oje6cTFAaGame7zs9m_iZevIoLMuo7xAUhOcRPBc_lsLDE6TtX27yysnhaVD6Mg5Lh4awAUCmf33v6c44ivFa40hTkQ7PmJIXsMg72y0tgNWeORzqWQR5Q13oOplDX1ZE5lzaBWUQWpbqcglI7eRoMPhzF7iU3xBEHoA66y52hKS937LI5sxqvKdBzq9NLPgCS7VbSt7alXn5Wt5cak3MrUNJ562wKWaA_H41nDUnMMdAiFe_kakWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c76aaa280.mp4?token=FotA-24OhZ79a6lrMPsSu-GZrtUtQUCtj4yN5pUnBTI3z6f4yWGLDGgV62vP3F-TZJJYOy1be96ngs6YaZXNLEGNYEr63oG9oje6cTFAaGame7zs9m_iZevIoLMuo7xAUhOcRPBc_lsLDE6TtX27yysnhaVD6Mg5Lh4awAUCmf33v6c44ivFa40hTkQ7PmJIXsMg72y0tgNWeORzqWQR5Q13oOplDX1ZE5lzaBWUQWpbqcglI7eRoMPhzF7iU3xBEHoA66y52hKS937LI5sxqvKdBzq9NLPgCS7VbSt7alXn5Wt5cak3MrUNJ562wKWaA_H41nDUnMMdAiFe_kakWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: شاید بتوانید بریتانیا را «جمهوری اسلامی بریتانیا» نامید
یک نفر گفت که اولین جمهوری اسلامیِ دارای سلاح هسته‌ای، جمهوری اسلامی بریتانیا خواهد بود.
ما داریم مطمئن می‌شیم که یه مورد دیگه مثل این، یعنی ایران، نداشته باشیم
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20921" target="_blank">📅 17:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20920">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1jeOz3XT3ILs-89od2hxCw4on1KZYiezXj6seEq12lQ4WHbkbeqxmP4g4BJ_1N8qB-JJMMAyh0vzHb0LrQRbvth_z8l1ovFdL0kVjB7ZhsIDmPYB5HGanImFCVaclG_z3CPq4VXKL327w7UDn-mf0hW9qiyA3j3moPmU7newwHIR3eoOB_t0zQg9z3b-qnBH3X-axu8QMjsWcIcH1yaQYzXXhYeAd8wCzMNbVNoiVMsjaUH0RPhWF1ey74s_b57hCCKPveE5QqasL1qu-FhTxlMicwCmML46ingBKHpNJZxmdb5o12zWk6j70nSXQowlLNBmWfYC5_q_K2BIZXm3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گفته کنعانی، مدیرکل حفاظت محیط زیست ایران، سطح آب دریای کاسپین به پایین‌ترین حد خود در نزدیک به ۲۰۰ سال گذشته رسیده است.
کارشناسان می‌گویند یکی از عوامل اصلی، روسیه است که با ساخت بیش از ۴۰ سد عظیم، رودخانه ولگا - شریان حیاتی اصلی دریا - را مسدود می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20920" target="_blank">📅 14:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20919">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjS5pxK4nE3br6wk4dYe7tAG7a9kfdkpLV6veMI3JQPxgvXklm7DjLJqPIpyNZoRjpoErtBTfm7zQfq_i76SHivJzVVCqsqE-4e4tN_cu75YnkHN6Irq_WmLr-wMUqIKLsmku7bePYo_1hquQXqnqKetGVocb9Z8soBe44VTgwmJDMDLgUCP-u4zBi0IHuJ3t_z3Wcgraea0kgh9KVIkAp4GYd4by6wKrKgyTgzBhptf9BHfidtVO921gyq1EVjAaQl6ujcRFAcBou6-VoaZxjwTsH1-eliyPLpZRVj3OxmGOLQRNlCM_Hf5kfsLqXT3Mg4rdmxNDRHuXE-_1lsnxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرگرد ابوالفضل حیدری، نیروی هوافضای سپاه ، امروز در یک سوء قصد با موتورسیکلت در زابل، استان سیستان و بلوچستان، به شدت زخمی شد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20919" target="_blank">📅 14:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20918">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b96bba2676.mp4?token=nuzocsq1yuxhm7WbGNe8OlqIDbs6baPsUYAKaIBpgn_iOi9hpwqYzpnehYHh2e--uDXjlGr0rF6WlfDI7pmbiacsMy6mgKZndqTmBiYQMcIsGTgeYGSzWDlzIGI8En6VeGFLP5i9lkiC_E8qtrxh0zAYKDECOzLPx1pyrNv0fmoksHdXHSV4vhtFxUBURmkH2lmJspFRGlTjE20fVgjNLUIP2WkVK3ZTwcHrnF3f7qMlZRMRTTEgDkAYcJvZ-A11xjrJJt4P4LKupoBqbBnLnD90Yz049iL5qsbVePk5ip5RmQA7s4S7yg2ltCap6qnFD8nemey0gUawhvtGmMCK-TH9KSZ2sUokHhPiBwWLZOR6R0DdtMB272P0uh7nKmR1fmDYZetRt4gm9xVJGrz0tdzAaiyCoKh2QnZ1XYwTt0WZQPz5IlT5iZMcx2kpc57228ETkYGGP57VDFkNCOvUhdK5vJZd06_prXwVoVeLo6jJroGUNVVd_v-EEvrDbx5vHT5hhgSIO-dsVIsLZe4sFINLvxdK1MUW8iftgu4Tqt89NZ_kISTbI--zekDZFnPAnpnKyPx4RQolstW-9EEeVxLJba0RbUWVH0aOfJnC9PrpT6YD9zc2V-9sTDm8BYPw-1p1RtV3E8Ifu9FxkHKYcFgns86W1FHdeGeIe77ATmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b96bba2676.mp4?token=nuzocsq1yuxhm7WbGNe8OlqIDbs6baPsUYAKaIBpgn_iOi9hpwqYzpnehYHh2e--uDXjlGr0rF6WlfDI7pmbiacsMy6mgKZndqTmBiYQMcIsGTgeYGSzWDlzIGI8En6VeGFLP5i9lkiC_E8qtrxh0zAYKDECOzLPx1pyrNv0fmoksHdXHSV4vhtFxUBURmkH2lmJspFRGlTjE20fVgjNLUIP2WkVK3ZTwcHrnF3f7qMlZRMRTTEgDkAYcJvZ-A11xjrJJt4P4LKupoBqbBnLnD90Yz049iL5qsbVePk5ip5RmQA7s4S7yg2ltCap6qnFD8nemey0gUawhvtGmMCK-TH9KSZ2sUokHhPiBwWLZOR6R0DdtMB272P0uh7nKmR1fmDYZetRt4gm9xVJGrz0tdzAaiyCoKh2QnZ1XYwTt0WZQPz5IlT5iZMcx2kpc57228ETkYGGP57VDFkNCOvUhdK5vJZd06_prXwVoVeLo6jJroGUNVVd_v-EEvrDbx5vHT5hhgSIO-dsVIsLZe4sFINLvxdK1MUW8iftgu4Tqt89NZ_kISTbI--zekDZFnPAnpnKyPx4RQolstW-9EEeVxLJba0RbUWVH0aOfJnC9PrpT6YD9zc2V-9sTDm8BYPw-1p1RtV3E8Ifu9FxkHKYcFgns86W1FHdeGeIe77ATmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏اظهارات کم‌سابقه سناتور تام کاتن درباره راز وقایع مرداد ۱۳۳۲ در برنامه هفتگی پربیننده مارک لوین در شبکه فاکس‌نیوز
‏«اوباما ادعا کرد که ما نخست‌وزیر منتخب دموکراتیک ایران را در ۱۳۳۲ سرنگون کردیم. این یک افسانه کامل است. او (مصدق) نخست‌وزیر دموکراتیک نبود. او اساسا سرنگون نشد...
..(برعکس)، مصدق کسی بود که سعی کرد قدرت را تصاحب و به طور غیرقانونی حفظ کند. ولی باراک اوباما با مغز استخوانش باور داشت و بارها درباره آن نوشت و سخنرانی کرد که آمریکا برای دهه‌ها تنش با ایران سزاوار سرزنش است و برای همین هم به دنبال توافق بهتری نبود.»
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20918" target="_blank">📅 12:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20917">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فرمانده ستاد کل نیروهای دفاعی اسرائیل، ایل زمیر، به وزرای کابینه در مورد وضعیت اقتصادی ایران گفت: تحریم‌ها علیه ایران بسیار موثر بوده است. بحران اقتصادی در آنجا رو به وخامت است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20917" target="_blank">📅 12:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20916">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سناتورهای دموکرات کنگره آمریکا خواستار بررسی شرایط ناو یواس‌اس آبراهام لینکلن شدند؛ این درخواست پس از گزارش‌هایی درباره کمبود غذا، خرابی لوله‌کشی و بحران‌های سلامت روان در طولانی‌ترین مأموریت تاریخ ناو مطرح شد.
سناتور روبن گایگو نیز خواستار بازدید رسمی و نظارتی یک هیئت دوحزبی سنا از ناو برای بررسی شرایط گزارش‌شده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20916" target="_blank">📅 11:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20915">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20915" target="_blank">📅 11:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20914">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEx7hRJYM7g_AZfVBpQYMS6IScT3zJaMFVjB3YnjxCGH3CQQV7Ptz1EiggbLupTJZGBLZRa8RI3ILXBb5BJfAE2yO-nvlpHjMZMFvSP4BmrY1GOA135jZNhZXVpoXj4S_INDiVl2033ZTNX5ftqSIjyV1oos1h9H7ug_ntLKWZh5p6kuZDQOPFSINxcTjZ34pnTQX48P3m_uFNYsr4yzo2QCysjgCJ4g_4zHQc4tCKxlCyjOlqt8IhWHssMLYvb2qxgQ_Cq7APYIApaj4HuAYPEYcoqg8O9UDR9seMlALJQhn5QfAk18Qmmf1HCQ3nIyI1KjS28RQhnE89eRCQAfXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : جوجی‌جون ، ناو هواپیمابر جورج واشنگتون و اسکورتش به سمت منطقه می آیند
🚨
🚨
🚨
کارهای اداری یادتون نره⁩
https://www.instagram.com/reel/Db-HXkWoJz-/?igsh=NHNmZ3ZhYnhhdDJi</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20914" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20913">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20913" target="_blank">📅 09:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20912">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20912" target="_blank">📅 09:46 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
