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
<img src="https://cdn4.telesco.pe/file/YN5dSGrgn0AFOgOhTqYhjotqu1Shrj9vDoyrF1FbTrIcMiygQk4FA9R-Gz5_oxmnXD_QJjvuKK9q3NjqcLTKw836_PETiz7awpsvsYv2jRjPBezkZFiuKcKcvycZzJt43y2wvwKSdm4V8tV84-PUpuu5FS9RwtNAMVYAppBd6Nsb6mUWXtXMT2c6ihzS4AAOlOYkB1pWW94gYOFhjz1y4yqpHsX7e6QNdEr6lmRfWkd8vZFZzq297_lxVkkwsy5rVpyarQ7gTTXHATa2KJ-7qebidp5hpYBLYfK6SdR7TlsEkJH9OwFlIDOieE1oLQdOffQ-qrH8a1mI5OlhhEYs3w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.4M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 19:38:12</div>
<hr>

<div class="tg-post" id="msg-671049">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
دیدار نخست وزیر عراق با ترامپ
🔹
علی الزیدی، نخست وزیر عراق که به واشنگتن سفر کرده، در کاخ سفید مورد استقبال ترامپ قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/akhbarefori/671049" target="_blank">📅 19:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671048">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
صدای انفجار در قشم
🔹
صدای دست کم ۵ انفجار در جزیرهٔ قشم حوالی ساعت ۱۸:۴۵ شنیده شد. ماهیت انفجارها مشخص نیست.  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/akhbarefori/671048" target="_blank">📅 19:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671047">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i07g4P0Dy27NfslIgvpaAmLwaNqR95Dxpbsb_9GhrnSdy_7g_KbudiZOEul7Qkj-x5wU-qQazIql40LuqvM42NPupg7Xcnmv9Hztx1CChihrG7wyCdXeoMfIB9ftlxCIpcr5t0BkKj-xvgZ8yukYlaN53opDcFCdstG9f8rb9Jtjbd58YP1n2-lC7aK6tuTZiaprsUcHaMNnuBkd1EFWD4MXA7iEKkyTZN5TLSFuiVzYWDHEiDCRiMuJvGw8qjIq86dVjpXfgYRl-F79nqiSqMo9i2tQkj4UkpqdRmdQgR31-m-bjk5tPeKR6MUbw38G4p5rOutZf-w5LxN-lQocCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رامین رضاییان با کیف لوکس Hermès Birkin ۴٠ دیده شد
🔹
قیمت رسمی این کیف در بوتیک‌های هرمس حدود ۲۰,۵۰۰ دلار است و با نرخ فعلی ارز، ارزشی نزدیک به ۳ میلیارد و ۷۰۰ میلیون تومان دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/671047" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671046">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c82c869464.mp4?token=DfCrcpkfketfUE1IQtMUttQ0O3A8iJz7Ul-FhntU0GKy8EPny4_92RD0dKlOIeVkAiTCeVI8Md0VwZd0JRDtLO14s8YnUcGOBZkch2mDeBZjaOyZVswoK0Hzb4RF9Kol4TA9NQr7yLHRvrOUnSpkRnDryCnctuGQ2_TNIJuEKzgmNyO5WRyK_S0N0UiuTOne-6xXzYtNzL06Dk_xNUsSW9ujuwI49wNOaQdFL2Zbft7px7XrTWR1a75p4pM9hY7GGncDEPGohU1-6n7m8v0PQvZePXNkaLjRBw_Ou3qMsfOsxQ-b5JQAItc2-FkOcbGvxbVHQdnQdMSKaAuqW8o_P7v-OPc6DzsuU8sbqXzWD5tzs7F6WQUNgfiWlZs4lpf6YA0m5oTtkBw_TksYfOQMzJIcjeyeaVwL-xcrKMPOYDosqGZ7Nf_ptU0YZeLnoSNX1ExHgU_tQSlyR8nXPxaZ7q8VorqNeMr1GbG-SOZStWI3wYlBrfkFcOrul0X4gtXb_TOtsrozGVvmvbzq_RButWR-hoB8vOIEw6ES3bdOS5cRzS1GlxErBu39SgQruN3wHq0ojdfS-mRSBRVyqqAUxbGBAmzS_sEBiXy6E8ETjjzzjY5jiTMIZ-NQtS7g7fp5SwddopV9ddmhTQPNnYwG9SyGvbLIrNAzzIE78wH6ffg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c82c869464.mp4?token=DfCrcpkfketfUE1IQtMUttQ0O3A8iJz7Ul-FhntU0GKy8EPny4_92RD0dKlOIeVkAiTCeVI8Md0VwZd0JRDtLO14s8YnUcGOBZkch2mDeBZjaOyZVswoK0Hzb4RF9Kol4TA9NQr7yLHRvrOUnSpkRnDryCnctuGQ2_TNIJuEKzgmNyO5WRyK_S0N0UiuTOne-6xXzYtNzL06Dk_xNUsSW9ujuwI49wNOaQdFL2Zbft7px7XrTWR1a75p4pM9hY7GGncDEPGohU1-6n7m8v0PQvZePXNkaLjRBw_Ou3qMsfOsxQ-b5JQAItc2-FkOcbGvxbVHQdnQdMSKaAuqW8o_P7v-OPc6DzsuU8sbqXzWD5tzs7F6WQUNgfiWlZs4lpf6YA0m5oTtkBw_TksYfOQMzJIcjeyeaVwL-xcrKMPOYDosqGZ7Nf_ptU0YZeLnoSNX1ExHgU_tQSlyR8nXPxaZ7q8VorqNeMr1GbG-SOZStWI3wYlBrfkFcOrul0X4gtXb_TOtsrozGVvmvbzq_RButWR-hoB8vOIEw6ES3bdOS5cRzS1GlxErBu39SgQruN3wHq0ojdfS-mRSBRVyqqAUxbGBAmzS_sEBiXy6E8ETjjzzjY5jiTMIZ-NQtS7g7fp5SwddopV9ddmhTQPNnYwG9SyGvbLIrNAzzIE78wH6ffg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیت‌الله سیدمصطفی خامنه‌ای: صبر در این مصیبت بزرگ هیچ منافاتی با انتقام و برخورد با اشرار عالم که در این جنایتهای بزرگ دست داشتند نخواهد داشت
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/671046" target="_blank">📅 19:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671045">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHbRcXEGitrx7heEKdaPsK1Z1gAljSmSj3IFaYFAxo4gGA10UAxBFIt6EEv-YxAKG33h_XYE-QBRXK2Ih6ahRDXepOdAoMaskrwqrFs2n-DLEa0bFQg_N7o1VWTweg6K7tJOCvmj_XPEKAIFLAA8rBGCL6SaabajkwvUtQB12QJnPGN3GVOTtMuIS4nGboSIQTlP7Ot_o0sHEUYgRwGB-LF9S2KrrzcWqh3lIsCRMorV8-6f95JoTW1E4x-kRGcYztOP2ylZPlwflRPQOTSDicIRpqHAaRt8yIZ8raR6xFWZLOwlUXdFkzCidGv6U_AG1NCrAAYqpCeoqY9F2O4wtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
خريد و فروش طلا
صندوق بانك گردشگري
صندوق اندوخته آميتيس
صندوق درخشان آميتيس
‎روبیس با دریافت مجوزهای لازم بستری امن و قابل اعتماد برای سرمایه‌گذاری فراهم کرده است.‌
https://rubisinvest.ir</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/akhbarefori/671045" target="_blank">📅 19:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671043">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971cb6b758.mp4?token=iNEEOrTYgdW1c7jafq3m9RMq_-ASRCtA9CtCxtdlzxdkNppQwYetw8Zon0j3Ws-5aIKOxW4F2A3kV-HyOaV_TYK7vIB_cD_Jxt72FoRhI1n_GDPwJY7Sb9Zo0Ct9gWBwPXwVEhrx3nGKE4nUrGoTEqd1C3ukpkvw7hlg4xbG7_4p_fxJajOtcwXw9Wmit9JMci3_KgnrSwb5Aw-3eqNtQu08196lvc-vymfWFXgoZg0jBObI4IsjU4V4Is5v0xUBTf1xuYYcIyR7UsLmRe3Yw6JGqwnDC4Oqxzh9jPxn08QeBpEmc4r1Azph62aHhC0cSj7-sAvTGfpOxopbnrNDVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971cb6b758.mp4?token=iNEEOrTYgdW1c7jafq3m9RMq_-ASRCtA9CtCxtdlzxdkNppQwYetw8Zon0j3Ws-5aIKOxW4F2A3kV-HyOaV_TYK7vIB_cD_Jxt72FoRhI1n_GDPwJY7Sb9Zo0Ct9gWBwPXwVEhrx3nGKE4nUrGoTEqd1C3ukpkvw7hlg4xbG7_4p_fxJajOtcwXw9Wmit9JMci3_KgnrSwb5Aw-3eqNtQu08196lvc-vymfWFXgoZg0jBObI4IsjU4V4Is5v0xUBTf1xuYYcIyR7UsLmRe3Yw6JGqwnDC4Oqxzh9jPxn08QeBpEmc4r1Azph62aHhC0cSj7-sAvTGfpOxopbnrNDVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سردار قاآنی در مراسم بزرگداشت رهبر شهید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/671043" target="_blank">📅 19:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671042">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
آسیب به تأسیسات برق کیش در پی انفجار پرتابه‌ها؛ احتمال خاموشی موقت
شرکت آب و برق کیش:
🔹
در پی انفجار پرتابه‌ها در نزدیکی نیروگاه برق جزیره، برخی تجهیزات فنی آسیب دیده و در حال بررسی است.
🔹
ممکن است برای انجام تعمیرات، تعدادی از واحدهای تولید برق از مدار خارج شوند که در این صورت خاموشی‌های موقت و زمان‌بندی‌شده اعمال خواهد شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/671042" target="_blank">📅 19:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671041">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
اطلاعیه دولت: مراسم بزرگداشت امام شهید انقلاب که مقرر بود روز چهارشنبه از سوی دولت جمهوری اسلامی ایران برگزار شود، به روز یکشنبه ۲۸ تیرماه، ساعت ۱۰ صبح موکول شد
🔹
این مراسم به میزبانی قوای سه‌گانه کشور در مصلای بزرگ امام خمینی (ره) تهران برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/671041" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671040">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
فعال شدن آژیرهای هشدار در کویت
🔹
منابع رسانه‌‌ای از حمله موشکی به اهداف آمریکایی در کویت و شنیده شدن صدای انفجارهای پی در پی خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/671040" target="_blank">📅 19:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671039">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
فعال شدن آژیرهای هشدار در کویت
🔹
منابع رسانه‌‌ای از حمله موشکی به اهداف آمریکایی در کویت و شنیده شدن صدای انفجارهای پی در پی خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/671039" target="_blank">📅 19:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671038">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
صدای انفجار در قشم
🔹
صدای دست کم ۵ انفجار در جزیرهٔ قشم حوالی ساعت ۱۸:۴۵ شنیده شد. ماهیت انفجارها مشخص نیست.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/671038" target="_blank">📅 19:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671037">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYuM30mASMz2XDniZLrvk4waHekZUuRyFaCKF1Xztm16nYLjPI3jP3npQpwB1OsOpGljorVmalJk-SDmxqTMsKz-bpthh6aKik8ea6twRPF1el92LA2HfeAGK3HnqNt0RLwcVaoO8nMuKYnzv-SSh3mKmN2f_aXzh1XOf3ehd6BSitB2fApBkYfEPmC47kjPK5ICqgtm3AZWqBOvYkO8waN7SlgAI14o29ymazITsmB7cP99zaONJFpy6VuAe4bRlelqVIxYlL9o6qMVNv6x5xBUoFlGusM4p4ypw2RV61D3HvyswklMc6lKUHkLJAakEcKjh96JObCA3SRx6TIEWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/671037" target="_blank">📅 19:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671036">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
خبرهایی درباره حمله به نفتکش اماراتی در سواحل عمان
🔹
این منابع گفتند نفتکش «البهیه» امارات در ساحل عمان هدف قرار گرفت و نهاد امنیت دریایی این کشور خبر داد سه نفر از سرنشینان این نفتکش مفقود شده‌اند.
🔹
در حمله بعدی هم یک نفتکش مستقر در امارات متحده عربی با پرچم لیبریا هدف قرار گرفته است.
🔹
امنیت دریایی عمان خبر داد که ۲۱ نفر از سرنشینان این نفتکش هم موفق به خروج از آن شده‌ و نجات یافته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/671036" target="_blank">📅 19:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671035">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4cv5DCJ-B0JoTXq0TQP42fFgkuMHCU7ccV2RIGVvomd04cUZxpBCgGNIC6q8CJDjQ50v_plVNovo_KO0G5b-DVSgKm6Gm8967ZMuucEW0DzktBJvRp84gidMdoRuvgsx64uUtIlOXzGBo0dukIJOjVZwIXdx4hB7OVul23Sj5Ml_Q_cmkIKwLEqg7_QzU5QSmIwEzR9LxeD7t6T5U4ZY-28Y5S_2RQiHKVIxc5uhz9fA-YNe7sQP2qauGLDVEzbdykPzO_EGuxw-NbKRybF0Oxz5lD3SfSNANI6Pr9HnjFo3_q4LFM2WoOfWbu9demuT4QR2uoLGjArdFdpjMaeGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: در تاریخ، جنوب ایران همواره نماد مقاومت در برابر استعمار و پاسداری از استقلال بوده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/671035" target="_blank">📅 18:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671034">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abecbc4c7d.mp4?token=OiB2Mxv2WUTAgy9n5C_g-muhsPZjREp0p4RrqePs8iAdsxUEzA_JAhg8X6_Och1guKC3mro4CUUF6QjKfCflY9Ok6LSvBkm49NLFcLaBzid_Upuy2gqs0zZNpbfAeUKwyGBf9JvmOXuXVtrWQ-mY5uyWuyuSLGGfrdZ2hCqIbTHQnr19EZeDnOu7Ta5DJ90VJez_5oGMST-TjKFtMWASwqMa_7J40cmQdjFeetGQ1yxdW7Sv8XkzakIDDWP-5QtJeK5qY7-NeAWfj8RY68nOdWNGoae-ShFNH2XMbmRlRIVCKaMm2Y9lGyYdwDQw66lhj1I2llg_raLjVeXWes88mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abecbc4c7d.mp4?token=OiB2Mxv2WUTAgy9n5C_g-muhsPZjREp0p4RrqePs8iAdsxUEzA_JAhg8X6_Och1guKC3mro4CUUF6QjKfCflY9Ok6LSvBkm49NLFcLaBzid_Upuy2gqs0zZNpbfAeUKwyGBf9JvmOXuXVtrWQ-mY5uyWuyuSLGGfrdZ2hCqIbTHQnr19EZeDnOu7Ta5DJ90VJez_5oGMST-TjKFtMWASwqMa_7J40cmQdjFeetGQ1yxdW7Sv8XkzakIDDWP-5QtJeK5qY7-NeAWfj8RY68nOdWNGoae-ShFNH2XMbmRlRIVCKaMm2Y9lGyYdwDQw66lhj1I2llg_raLjVeXWes88mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار نخست وزیر عراق با ترامپ
🔹
علی الزیدی، نخست وزیر عراق که به واشنگتن سفر کرده، در کاخ سفید مورد استقبال ترامپ قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/671034" target="_blank">📅 18:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671033">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
پلیس فتا: احراز هویت خریداران در معاملات آنلاین الزامی است
پلیس فتا:
🔹
در هنگام ثبت آگهی در سایت‌های فروشگاهی و یا انجام هرگونه معاملات آنلاین، احراز هویت خریداران و واریز کنندگان وجوهات از سوی فروشندگان و یا ارائه دهنگان کالا و خدمات الزامی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/671033" target="_blank">📅 18:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671032">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a05e1e5a.mp4?token=LjGBogCv-YbWUPOSVg-zfiPtWUP3yoIrundI3284BBpgrm6b6-63Rdr2gMzFh5RFoIy-M3peYrJk6ond28AHXfaio0w9DPJvDOU9fWCZzv-gRcspF1HfB8his6Gg8_XoTsGZKcu1UE6nd2m2PdhiEo7muh_nmzPiAOX208LiJdcs3Ir7S1_gOep5DOtoV7LLGtJIadoS0ABSG2UgvV-RADel_QDIKG2WSfasfqGpxnvblBw-vc9rGiDJ5WQeIBA5GunVsQp_c4W0Iqnw9fY9rnek-czRfVyRCWhF7q0hx1UKkrG3Y-qZxsAmSKJkybX_oWZ-la0smYoJgpvEJJc8yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a05e1e5a.mp4?token=LjGBogCv-YbWUPOSVg-zfiPtWUP3yoIrundI3284BBpgrm6b6-63Rdr2gMzFh5RFoIy-M3peYrJk6ond28AHXfaio0w9DPJvDOU9fWCZzv-gRcspF1HfB8his6Gg8_XoTsGZKcu1UE6nd2m2PdhiEo7muh_nmzPiAOX208LiJdcs3Ir7S1_gOep5DOtoV7LLGtJIadoS0ABSG2UgvV-RADel_QDIKG2WSfasfqGpxnvblBw-vc9rGiDJ5WQeIBA5GunVsQp_c4W0Iqnw9fY9rnek-czRfVyRCWhF7q0hx1UKkrG3Y-qZxsAmSKJkybX_oWZ-la0smYoJgpvEJJc8yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«فکت‌چک» برنامه تلویزیون اینترنتی مدار برای کشف حقیقت از میان شایعات روز
🔹
تلویزیون اینترنتی مدار در روزهایی که اخبار و اطلاعات با سرعتی بی‌سابقه منتشر می‌شوند، با ساخت و پخش برنامه "فکت چک" راهی برای تشخیص واقعیت از شایعه باز کرده است.
🔹
«فکت‌چک» برنامه‌ای است برای بررسی و راستی‌آزمایی ادعاها، خبرها و روایت‌های مطرح شده در رسانه‌ها و فضای مجازی که در تلویزیون اینترنتی مدار تولید و پخش می‌شود.
🔹
در هر قسمت، با تکیه بر منابع معتبر، اسناد و شواهد، به دنبال کشف حقیقت و روشن شدن واقعیت‌های پشت پرده خواهیم بود.
اینجا مدار را تماشا کنید
👇
www.aparat.com/MADAAR_TV
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/671032" target="_blank">📅 18:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671031">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NceZuCnELZSvy6IFSDoLH0NzBrtdRr6ckqYQAGX8QU14idUhTEIy6v7mbx5TgFz3IDYOKnL81HUpktYaivCPqVY8hm2JCLw1ahlzSfAXLB3VBSQ_x-ZH7vUpDX89gH04qInc_xYxTCWrmYGf00tU80H8huV3cKNb-1w3DJv1MM3GS__OhPM8Df1DxCGf-xITpBblEIVsup76rilvcX1Ym1RWcb8jW-ORjXI0k9CQ7v-wSDxZjuZI7-p-oPDOi1sRsPdRP5uNmuXJRywQCjo5ymBdNdP44v6ocamtJOeUpLLJnX9-XUxTP21g9XRn5srz5fiqr2NIOgzWpRtnhEtTkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوک هار از عوارض ۲۰% تنگه هرمز عقب نشینی کرد
🔹
«تصمیم گرفته‌ام که هزینهٔ ۲۰ درصدی بازپرداخت ایالات متحده را با قراردادهای تجاری و سرمایه‌گذاری جایگزین کنم که کشورهای مختلف حوزهٔ خلیج [فارس] در ایالات متحده انجام خواهند داد. آن سرمایه‌گذاری‌ها بسیار کلان (عظیم) خواهند بود.»
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/671031" target="_blank">📅 18:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671029">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np0LMYcl7o1vrOTjtHiv-YJxQyrY9kms9SoDwqVTzWU426oIS0eWrVWUdLhJv4GK89VpG229k8DQrxx3ytaVpAxJHsbsC5VodWfrwsGMIdjn82pHrMpdHxVryLIvvQobt1Pqa0MJp0VD7kSk58WHoAqhO4Uo31hZrp0cAgcBT5LCjjT6ARnSSmuvFnpqWppYDpK0Uw1ji3bG8DUViZBLG0czR5Ff0SO6-Bnt79gNYX4rv5VdZcmiAozQqNTuSR4DKVKJLQd18tU_-LkMlM4EO7iTBw5foKilkesHwsxSY5RLmWdVCBNTHWe-fmXNwcq6hgKBSvs3SyGMHG_pIEO6iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاش خواهر زیدان، ایتالیا را ببخشد | نیمه‌نهایی؛ جایی که همه پیش‌بینی‌ها می‌میرند | فوتبال عادلانه نیست؛ راز جذابیتش هم همین است | فینال آرژانتین و فرانسه؛ تنها پایانی که جام را نجات می‌دهد | همه چیز درباره نیمه‌نهایی
🔹
حرف زدن از فوتبال آن هم در این‌ شب‌های داغ جام جهانی همصحبت خوب می‌خواهد. کسی که هم خاطره بصری بلندمدتی داشته باشد و هم پای ثابت فوتبال باشد و البته که فوتبال برایش فقط محدود به فوتبال نباشد!
در خبرفوری بخوانید و ببینید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3230294</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/671029" target="_blank">📅 18:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671028">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81e4352e2e.mp4?token=ifYine3JH5FMA2gOzAQLcUj708y7wF-OEqYYxqvKHBGMEOlbWFPIraNAldsr8OaSTxJo0h0ldm8Kg9TQl2XXDSHfZZ9-I-uzSD14BPXimjjSHFVFP5iMoEPI0Yhi3BxtEPJy9Q5ZwdZlqMX-77IFXRt_hO83qg040JWkIMp4KAoZgajT7E0MbF1MWMNhevG66-du3fkB5z9lCBLI1IDJc-kfIr7g__G1mDRewIf0qFBGIBcr8-pOG-10VZTg1Y-5Mkx5V4Kns5QCmu1NKe25vHdwwopWL7hfj01g8pp1pZGomyb6K4WkMtNOGAu0XNYjoZQS9krgp3fvQYtcCKUp5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81e4352e2e.mp4?token=ifYine3JH5FMA2gOzAQLcUj708y7wF-OEqYYxqvKHBGMEOlbWFPIraNAldsr8OaSTxJo0h0ldm8Kg9TQl2XXDSHfZZ9-I-uzSD14BPXimjjSHFVFP5iMoEPI0Yhi3BxtEPJy9Q5ZwdZlqMX-77IFXRt_hO83qg040JWkIMp4KAoZgajT7E0MbF1MWMNhevG66-du3fkB5z9lCBLI1IDJc-kfIr7g__G1mDRewIf0qFBGIBcr8-pOG-10VZTg1Y-5Mkx5V4Kns5QCmu1NKe25vHdwwopWL7hfj01g8pp1pZGomyb6K4WkMtNOGAu0XNYjoZQS9krgp3fvQYtcCKUp5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عارف قزوینی؛ شاعر وطن‌پرست دوره مشروطه
🔹
عارف قزوینی فقط یک شاعر یا خواننده نبود؛ صدای خشم، وطن‌پرستی و آزادی یک نسل بود. با تصنیف «از خون جوانان وطن» نامش در حافظه ایران ماندگار شد. هنرمندی سرکش و میهن‌دوست که با شعر و موسیقی علیه استبداد شاهنشاهی؛ از…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/671028" target="_blank">📅 18:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671027">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzx-UfkXroPRnd9DhxZyHp8gLwd4SJteQymfHMhPNtpmOWzVzyHNvmjzUEsQ98PgDNK8KNEr4LpCsdBBxW3XL48O-TsiinE5D0t4Y09i42KhGxHC2Wzq6PHeC-BIFvLs7Rd9BWOjqcMzBnmgMVIGSeDyKvvgTSCZkUL7KpdsYe4v0pjdCs4rpdWgjBZVQeL_xmD4EpP8K6xzXk_nK0R1m2TIZBFkR6-YSpKtcgP1QjCWsdVSS4CjGbH9oGsrOgwuDAqUfyDf2xmkGvFaiNWM7sG8Leg2pLBqpOL_o9VdGwiwBouVcxsU6k7iiztRHAWGpmgzJXfZPmbwsIUXTnXo3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصطلاحاتی که بهتره وقتی میری کافه بدونی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/671027" target="_blank">📅 18:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671026">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
امکان تغییر محل آزمون پزشکی داوطلبان اهواز، بوشهر و بندرعباس
وزارت بهداشت:
🔹
داوطلبان حوزه‌های امتحانی اهواز، بوشهر و بندرعباس در صورت تمایل می‌توانند از ساعت ۱۴ روز سه‌شنبه ۲۳ تیرماه ۱۴۰۵ تا ساعت ۱۰ صبح روز چهارشنبه ۲۴ تیرماه، حوزه امتحانی خود را صرفا به شرحی که در ادامه آمده است تغییر دهند:
🔹
حوزه اهواز به لرستان
🔹
حوزه بوشهر به شیراز
🔹
حوزه بندرعباس به کرمان
🔹
آزمون فوق در حوزه‌های اهواز، بوشهر و بندرعباس همچنان برگزار خواهد شد و  این مهلت قابل تمدید نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/671026" target="_blank">📅 18:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671025">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
پاداش ورزشکاران مدال‌آور در بازی‌های آسیایی اعلام شد
کمیته ملی المپیک، پاداش پای سکوی ورزشکاران مدال‌آور در بیستمین دوره بازی‌های آسیایی را به این شرح اعلام کرد:
🔹
مدال طلا: ۳ میلیارد تومان
🔹
مدال نقره: یک میلیارد تومان
🔹
مدال برنز: ۴۰۰ میلیون تومان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/671025" target="_blank">📅 18:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671024">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c0d02ae7.mp4?token=bunkqoLZlFwWRLHoc7lg2lkVfgSSnPScjVqS53ZJVpwMwo1YOhrLNSdJk1aJpT_wahUTn3S9e_evJWQIp00m-BAsmMWjhGhp2_tqCmJYIPhi3ZqVPAqGve9q3EeJ8WXSu3xRnr43l_6M6D_irtlkfxRnc2pelK47pHY-h-VIdI93EpEtjDQH0jlW4kRJxggZ_WDkdtXotmKRrkUVLjaQDQhdV77oE6qTX9YR3lYjMQLFten76pTQYgrI42euhzJnAEgg06x_FHOMZmDd4Lq6HmwqFDJuteVgT51GO1n2-9AlcLsuZQuURQ-gFxjnU7sKe52wbdB8_zNp8y1flGQULw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c0d02ae7.mp4?token=bunkqoLZlFwWRLHoc7lg2lkVfgSSnPScjVqS53ZJVpwMwo1YOhrLNSdJk1aJpT_wahUTn3S9e_evJWQIp00m-BAsmMWjhGhp2_tqCmJYIPhi3ZqVPAqGve9q3EeJ8WXSu3xRnr43l_6M6D_irtlkfxRnc2pelK47pHY-h-VIdI93EpEtjDQH0jlW4kRJxggZ_WDkdtXotmKRrkUVLjaQDQhdV77oE6qTX9YR3lYjMQLFten76pTQYgrI42euhzJnAEgg06x_FHOMZmDd4Lq6HmwqFDJuteVgT51GO1n2-9AlcLsuZQuURQ-gFxjnU7sKe52wbdB8_zNp8y1flGQULw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سفرای کشورهای خارجی در مراسم گرامیداشت رهبر شهید در مصلی امام خمینی(ره)
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/671024" target="_blank">📅 18:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671023">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MM-xJCq3T84lv9tOpIM8mkRZgsNT4yEeWoNzcrBbOwBf9CCJVMLInyseneC2-RDBMstog_So6M6NQayxYrT10SYWdptaXAwe1oA6IVM7_6-jvTPZdH4g8bqMh1FueEP9vPNg0ekj8hTYULqmPge6xBJeUDTiHzJH28lW8q9hw6QCE0VP69BNWJFC4gO9VLuFxD0wpoNLaXXitkYL1GbHHLAdQMf1Uxn4AEMz6V9_UkoRXy-QGSYdXu49BI0nJptqakepHTmSFEpwVdXyM4ufyD1NFWfTKYz7bDtl_H-N-sBY_VDPP_TKTatATQSzK5a8p5YbzX7YQRUt1P3TS63TfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا تنظیم‌گری بازار آنلاین طلا به سرانجام نمی‌رسد؟
🔹
خبرگزاری فارس نوشت: ماه‌هاست مقررات این بازار میان دولت و بانک مرکزی در رفت‌وآمد است. تازه‌ترین اختلاف نیز به تفاوت میان مصوبه هیئت وزیران و ضوابط اجرایی بانک مرکزی درباره نحوه نگهداری طلای کاربران بازمی‌گردد.
🔹
بازاری که میلیون‌ها ایرانی در آن سرمایه‌گذاری کرده‌اند، بیش از هر چیز به مقرراتی شفاف، پایدار و قابل پیش‌بینی نیاز دارد؛ نه ابهام و تغییرات مکرر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/671023" target="_blank">📅 18:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671022">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hl5yNTT7o9ZKJPwZCTLrTBmQg5t7rUJiGz8hcOyfs9t--xNhxpZfclvb_Ou_bJfc5AuuDR8FKBFq3EOtlFy4zzilT5DXRRvBVFITxl2ZNQfQ2K3nwo-lCQrutd74EcygLerABDNcxKhcyvwIS54_kgvYubuEsJOoyeP89vLBJFGlJ69TN8kmUG-YAzKE6MrS268blQV4EJY_D4zzmjYBn1AzRupWCRM3qJMSoeBf1-uaZLLzAWllGTnTex-AvqFjlm515Zi_LFWR-NmkWvoX0H3Osp2ZHQOKf967pe5f7Q-PUO3L5b-Hs871LSi9nGzTt-c0L0cMvIo7PIJAFyr5fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوک زرد ری‌پست کرد: جزیره خارک رو تسخیر کنید!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/671022" target="_blank">📅 18:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671021">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
بریتانیا طرح ترامپ برای دریافت عوارض از تنگه هرمز را رد کرد
🔹
دولت بریتانیا پس از ادعای ترامپ مبنی بر کنترل تنگه هرمز و دریافت عوارض از آن، امروز اعلام کرد موضع خود را مبنی بر اینکه تنگه هرمز باید «بدون عوارض یا هزینه» بازگشایی شود، تکرار کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/671021" target="_blank">📅 18:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671020">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b03e544f40.mp4?token=cjUxx2_DZaQYG8jzSwVWsGNkxuNR8YuPujaAWwBYIsPFyLjGRvsxH-e_h7M30Lh_M3lzND1sAZ7Tz7klemkV8W-31iMgTLRRvm3UDX6HQXDsmzFvsC3EJ1CedqEHQQptlY8xMY67o3rKSzsPzfXk7Y1evnudPmnaQ92-9ZqCxZgictisz2eunJw5pR3ntqB0UaUP0tvjSH4a0ZkYf6TINgk0CeM3YpRPy4psl3tFQFvoWfDGfiRZsVDmw_nnQHSjwwnsvsOv3cLH-kIJZnD8xCVI8vwuLp3xL5-Au13gNEWWkqUOIcTy6WVeOBaoaX5I3ZoQFLALRCRQfxqZ3N-qZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b03e544f40.mp4?token=cjUxx2_DZaQYG8jzSwVWsGNkxuNR8YuPujaAWwBYIsPFyLjGRvsxH-e_h7M30Lh_M3lzND1sAZ7Tz7klemkV8W-31iMgTLRRvm3UDX6HQXDsmzFvsC3EJ1CedqEHQQptlY8xMY67o3rKSzsPzfXk7Y1evnudPmnaQ92-9ZqCxZgictisz2eunJw5pR3ntqB0UaUP0tvjSH4a0ZkYf6TINgk0CeM3YpRPy4psl3tFQFvoWfDGfiRZsVDmw_nnQHSjwwnsvsOv3cLH-kIJZnD8xCVI8vwuLp3xL5-Au13gNEWWkqUOIcTy6WVeOBaoaX5I3ZoQFLALRCRQfxqZ3N-qZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهادت سه عضو خانواده یک محیط‌بان هرمزگانی در حمله آمریکا به دکل محیط‌بانی حاجی‌آباد
🔹
صبح امروز در پی حمله آمریکا به دکل محیط‌بانی منطقه حاجی‌آباد در استان هرمزگان، سه عضو خانواده یکی از محیط‌بانان این منطقه به شهادت رسیدند.
🔹
بر اساس گزارش‌های منتشرشده، دو فرزند پسر این محیط‌بان به همراه عروس خانواده در جریان این حمله جان خود را از دست دادند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/671020" target="_blank">📅 18:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671019">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
سازمان بازرسی آثار حمله سایبری به چهار بانک کشور را بررسی کرد
معاون نظارت و بازرسی امور اقتصادی سازمان بازرسی:
🔹
هدف اصلی سازمان در شرایط کنونی، کمک به بازگشت هرچه سریع‌تر ثبات به شبکه بانکی، رفع مشکلات ایجادشده برای مردم و پیشگیری از تکرار اختلالات ناشی از حمله سایبری است./ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/671019" target="_blank">📅 18:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671018">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f592965c1.mp4?token=QteRQtzTLKZLlcH159ZZhanrwBUOGbDAeIdcDi_QBzqwjVzx1CV_RVNv8rlF4apRJo5EXDh_xmsBbL_lhJdvM22eR0qS_2mhdaR01DqH9ZY2xGedJglxVNGYK7qDCqYY8O75j3sbVRWpGdz9O8EuogeC23V1fjdG0fmhqiLozDxa8jRMtoLXrDU1y1ZDNc9-Y2MU872qtwHBH7N_fKi-9pnvM7vvd63p7EAkOL05Hh88jGC0YvaENRZyRUqcX1rM-XJIqDthEVAxId1Iw0lr3L1x4s7kCHorPCXKUAlS3TWWhSzfCI42zg1HHlsjzOUP8IbIysegp-4mQVBMtEHyvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f592965c1.mp4?token=QteRQtzTLKZLlcH159ZZhanrwBUOGbDAeIdcDi_QBzqwjVzx1CV_RVNv8rlF4apRJo5EXDh_xmsBbL_lhJdvM22eR0qS_2mhdaR01DqH9ZY2xGedJglxVNGYK7qDCqYY8O75j3sbVRWpGdz9O8EuogeC23V1fjdG0fmhqiLozDxa8jRMtoLXrDU1y1ZDNc9-Y2MU872qtwHBH7N_fKi-9pnvM7vvd63p7EAkOL05Hh88jGC0YvaENRZyRUqcX1rM-XJIqDthEVAxId1Iw0lr3L1x4s7kCHorPCXKUAlS3TWWhSzfCI42zg1HHlsjzOUP8IbIysegp-4mQVBMtEHyvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
قطعی برق؟ تاریکی دیگه دردسر نیست!
🔦
چراغ شارژی خورشیدی
تاشو با طراحی کاربردی، مناسب برای خانه، سفر، کمپینگ و مواقع اضطراری.
✨
ویژگی‌ها:
✅
شارژ با نور خورشید و USB
✅
طراحی تاشو و کم‌جا
✅
نوردهی قوی
✅
مناسب برای قطعی برق، خودرو، ویلا و طبیعت‌گردی
🔥
قیمت قبلی: 1,598,000 تومان
❌
💰
قیمت ویژه: 1,098,000 تومان
✅
⏳
این تخفیف برای مدت محدود فعال است.
🛒
برای مشاهده مشخصات و ثبت سفارش، روی لینک زیر کلیک کنید:
👇
👇
👇
https://memarket24.ir/product/brief/47540/180124/</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/671018" target="_blank">📅 18:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671017">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e44ec578b.mp4?token=LtxX-xfjnmhHNyrvHcQhubmsL9WsTjy_Zk_H2JsELfB9xRv0R1v3Yxlbcui2ak5ifkXECRwmNhN133C93zlbX1T7nMv7t119G_QX_J0yDcQRcb7pkzYh-Zvd5GH6KcE3IeMRyLaA70yqxQT_GYjJEOdpuVKkEpvGi2ETVkAJYmiBd64km3Q9NbhjwZaSqFF1a-r_r8xami7AXt1VuSG0x9r2UFkybJOPlhxCDu3OYvANTbVuBjgxl9ElQuYZ0BCcuD9AhIN2LhucIXDF0ryb3hKwdyAV_kxQty3ezq3eHx-y1Luoe86PGwZ9wQNEH-lujLfP-PY8xS59ZPLdnvbl9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e44ec578b.mp4?token=LtxX-xfjnmhHNyrvHcQhubmsL9WsTjy_Zk_H2JsELfB9xRv0R1v3Yxlbcui2ak5ifkXECRwmNhN133C93zlbX1T7nMv7t119G_QX_J0yDcQRcb7pkzYh-Zvd5GH6KcE3IeMRyLaA70yqxQT_GYjJEOdpuVKkEpvGi2ETVkAJYmiBd64km3Q9NbhjwZaSqFF1a-r_r8xami7AXt1VuSG0x9r2UFkybJOPlhxCDu3OYvANTbVuBjgxl9ElQuYZ0BCcuD9AhIN2LhucIXDF0ryb3hKwdyAV_kxQty3ezq3eHx-y1Luoe86PGwZ9wQNEH-lujLfP-PY8xS59ZPLdnvbl9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد متخاصم با آتش پدافندی نداجا در بندرعباس
روابط عمومی ارتش:
🔹
بامداد امروز، یک فروند پهپاد متخاصم دشمن متجاوز آمریکایی، با رهگیری و شلیک موفق سامانه های پدافندی دلیرمردان نیروی دریایی ارتش، تحت شبکه یکپارچه پدافند هوایی کشور در بندرعباس، مورد اصابت قرار گرفت و منهدم شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/671017" target="_blank">📅 17:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671016">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a8ddd9019.mp4?token=VepxiCCcaNMefKjZfJXME8r3tbfKu1ed2W9j4Vht2IDm9_Egn_RiWV6Y6TK4EDHAD4NMp6ASgjwi4egkY0iwxph7_hbYYsqvtbGW31TnfosxwjfWq6qmC29wFDIYpzbWu6X-Krv4s8kv3R92tD9Y_0xDHWob9KNDeRIXnXziTdm2QHlIqgkgrYiOBDojq0FoWRibLnbUqyCcWtWcND2Kuf23QhHWlGT4KBZQBHwjT0wV0MKOrlbYnZYrznRTibYg87AR7RXscWGisb6OQ5jlF7RT_V0kaVLRpKKK_eyUbSuVggrEmZbVJI999Tn_26VLnbyCJWk4qxPl2uAeoj5hTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a8ddd9019.mp4?token=VepxiCCcaNMefKjZfJXME8r3tbfKu1ed2W9j4Vht2IDm9_Egn_RiWV6Y6TK4EDHAD4NMp6ASgjwi4egkY0iwxph7_hbYYsqvtbGW31TnfosxwjfWq6qmC29wFDIYpzbWu6X-Krv4s8kv3R92tD9Y_0xDHWob9KNDeRIXnXziTdm2QHlIqgkgrYiOBDojq0FoWRibLnbUqyCcWtWcND2Kuf23QhHWlGT4KBZQBHwjT0wV0MKOrlbYnZYrznRTibYg87AR7RXscWGisb6OQ5jlF7RT_V0kaVLRpKKK_eyUbSuVggrEmZbVJI999Tn_26VLnbyCJWk4qxPl2uAeoj5hTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، تحلیلگر حوزۀ مقاومت: استراتژی چشم در برابر چشم دشمن را متوقف نخواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/671016" target="_blank">📅 17:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671015">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c90c845ea.mp4?token=eCU_JYlDp8IFPBRC8gqssNg0Sd3j-qXXWl0UG6bidrYnlja2nZTAiW82Qfd2pdKKwfW-Qtxu-E_k8lipLkszzSA6OPjBvUjeUhaTwczmutvZx7C5RMvwsjcCNd26Ga8Sq68iowpTnUKjpL9v470mjYLk9jSnespc3XJcaMRdZqesuuZv-xarhwaj6PUlBkiCAUW9IULgB1Tvh0tDnw163RwM3Bu3LSCjgyiKi4NDDX0NRiMrLZPrtL6sQ1Dnf4USo315dLKVs5pvBsVTEPIskAUh5Z2EijT0cNCddGgOBZk1aAI-xkzTMsvAlE0EXh1gI1Gd_qPgPLnZzT-yc8L6wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c90c845ea.mp4?token=eCU_JYlDp8IFPBRC8gqssNg0Sd3j-qXXWl0UG6bidrYnlja2nZTAiW82Qfd2pdKKwfW-Qtxu-E_k8lipLkszzSA6OPjBvUjeUhaTwczmutvZx7C5RMvwsjcCNd26Ga8Sq68iowpTnUKjpL9v470mjYLk9jSnespc3XJcaMRdZqesuuZv-xarhwaj6PUlBkiCAUW9IULgB1Tvh0tDnw163RwM3Bu3LSCjgyiKi4NDDX0NRiMrLZPrtL6sQ1Dnf4USo315dLKVs5pvBsVTEPIskAUh5Z2EijT0cNCddGgOBZk1aAI-xkzTMsvAlE0EXh1gI1Gd_qPgPLnZzT-yc8L6wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسگر موجود در توپ جام جهانی ۲٠۲۶ چطور کار می‌کند؟
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/671015" target="_blank">📅 17:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671014">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJIHQ6-yJdExoCDx4fq9_7DY3UgHvp04mYZnAJK75ZyhdNvigCeMKkyrhP2cSXRy_2zAEtkVT2AupIDsrEHe-W7V1HNOY3ZP7DZdHdrCl9gl99VGc10fH2OGsLP-6m_qh6fv-vo_Lb7I3BZOqjW7-v4AkUXQnvknhkns4JqyTwTJylmxjvOeX1oqeRcH_dguvkMqmpw5HW6erye99GsB3G9DItD5l-fNQrsLUAPRDQAJw1-icaxgUExoRgLbhqDbDv2z3GJckvb7DpYSsOSF9wiheQxckfvEVhaF4-IYUb7Yrxc7_is0ud7HH7YMwM3ONymIYpozSpnDepCttryuCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز پروژه تولید محتوای انگلیسی و عربی درباره ایران با امضای تفاهم‌نامه همکاری تلویزیون اینترنتی مدار و مؤسسه افق نو
🔹
تفاهم‌نامه همکاری فرهنگی و رسانه ای تلویزیون اینترنتی مدار و مؤسسه فرهنگی-هنری افق نو، امروز سه‌شنبه ۲۳ تیرماه برای آغاز پروژه تولید محتوای انگلیسی و عربی درباره ایران به امضا رسید. این تفاهم نامه برای ارائه تصویر بدون سانسور و واقعی از رویدادها، ظرفیت‌ها و نقش ایران در فضای بین‌المللی منعقد شده و در این همکاری چهره‌های فرهنگی اجتماعی اروپایی و آمریکایی در فرایند تولید محتوا مشارکت خواهند داشت.
مدار را اینجا دنبال کنید
👇
www.aparat.com/MADAAR_TV
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/671014" target="_blank">📅 17:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671013">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbYP5LBcb6kKkEonOM44GRX1If-QVhq-byR9RiLdyRZG7xxsiHiMLQMteWaUOYEY3wE37dMZF1z-EvPD2vD6iWscAslT2agqQxvA4bPwduzwGVdX-n7IsbwlFtXmxdWDpxFa8EsuS422FychrNrN0aXG1jhHWrH7anM7Qw6dTajbq57auHYVLIaB0R9W_EWTXhcTVSKrTdOaV3FDej6RpMvgQBekuBeAvRkrXK697PMzGsECxb3eDSh1LDpbvsXXeix5G0GS88DneZh04yS8BeZ9NxxzgvcXF8_A9GthaEGM7zlf1-kIQr5hfc_zkvLQRXY34TDX7aR7xLMiLwNHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خونخواهی رهبر شهید انقلاب یک مطالبه ملی است، نه شعاری مقطعی. انتظار می‌رود قوه قضاییه و همه دستگاه‌های مسئول، پیگیری حقوقی و قضایی جنایات آمریکا و رژیم صهیونیستی را با جدیت تا تحقق عدالت دنبال کنند.
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/671013" target="_blank">📅 17:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671012">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دادستان تهران: احکام پرونده‌های جنگ‌های تحمیلی و اغتشاشات دی ماه صادر شد
.
🔹
کاپوتاژ خودرو به کشور عراق از ۲۵ تیرماه ممنوع است.
🔹
فراجا: برای برگزاری مراسم سفر اربعین آمادگی صد در صدی داریم.
🔹
دادگاه عالی جنایی استانبول حکم جلب نتانیاهو را صادر کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/671012" target="_blank">📅 17:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671011">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02bf47cb4.mp4?token=Nw5E2aQk4mhpfAPiQicdNgiPDQrgnSs4dc6ahYgKRJ9aL8nRT4F_waAx7ATf46-xzwp4Tf8qCNYmB6pgRvukueWORVJC9M_YQdR5p3pHs_Gy06N7YbwWk_-BvZOl15fN_Z15pYjn-X8HvmMmiDdbBZEg-zC5ad3CLE3uuyJ9kg_uxQ4wpSE334np4H44em7uU5r3EXobqR_MmYiuzHU48-jPmBVqkDj9nifucktoy8KuwwgqzKOop8AN2JSHaYXo47DGg25O2bppj8Sby64eBNufe3kGNDGaJVmJ3Qu_gptg-jl7sGsnXbNC-oV90K0IealLlVsgwgmsPGYAyhjDRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02bf47cb4.mp4?token=Nw5E2aQk4mhpfAPiQicdNgiPDQrgnSs4dc6ahYgKRJ9aL8nRT4F_waAx7ATf46-xzwp4Tf8qCNYmB6pgRvukueWORVJC9M_YQdR5p3pHs_Gy06N7YbwWk_-BvZOl15fN_Z15pYjn-X8HvmMmiDdbBZEg-zC5ad3CLE3uuyJ9kg_uxQ4wpSE334np4H44em7uU5r3EXobqR_MmYiuzHU48-jPmBVqkDj9nifucktoy8KuwwgqzKOop8AN2JSHaYXo47DGg25O2bppj8Sby64eBNufe3kGNDGaJVmJ3Qu_gptg-jl7sGsnXbNC-oV90K0IealLlVsgwgmsPGYAyhjDRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سه فرزند رهبر شهید انقلاب در مراسم بزرگداشت ایشان در مصلای تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/671011" target="_blank">📅 17:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671010">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07330a77b.mp4?token=ji2LM2vYzL89wAAWmI517WKWQtdsWaG7SeCLhAL7SfQi_O-KDC1Oe617WytcyEz8TWEjUuAxgyZv2jAYYVN9HcyQaR9HA3Z-pxqIw2rJGI8euwGhoQ_5xMzRxg8suhJASw8W2K3UwJHeKrS6VYsqUNDZcrZkZJyu3sUljiyGN6tQxWrXHDx0yR6HLw38noOJghSmCK3iD_ERt9gxIVRKyEwgb7xNYbVchpGjod9-uxq5fKeEL3MYZ76I54ZxmaK6HfEuL07KOYc_whVCukAM5we0XWt4xIBeaKmSZV_o_81kpMhvlsKlU61qfdn9tycZCnjo5RDo4ekBid-SvTzY_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07330a77b.mp4?token=ji2LM2vYzL89wAAWmI517WKWQtdsWaG7SeCLhAL7SfQi_O-KDC1Oe617WytcyEz8TWEjUuAxgyZv2jAYYVN9HcyQaR9HA3Z-pxqIw2rJGI8euwGhoQ_5xMzRxg8suhJASw8W2K3UwJHeKrS6VYsqUNDZcrZkZJyu3sUljiyGN6tQxWrXHDx0yR6HLw38noOJghSmCK3iD_ERt9gxIVRKyEwgb7xNYbVchpGjod9-uxq5fKeEL3MYZ76I54ZxmaK6HfEuL07KOYc_whVCukAM5we0XWt4xIBeaKmSZV_o_81kpMhvlsKlU61qfdn9tycZCnjo5RDo4ekBid-SvTzY_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل ویرانگر در روسیه؛ ۵۰۰ خانه زیر آب رفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/671010" target="_blank">📅 17:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671008">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
هشدار یمن به شرکت‌های هواپیمایی بین‌المللی
🔹
رسانه جنگی یمن، نسبت به عبور هواپیماهای بین‌المللی از حریم هوایی عربستان سعودی هشدار دادند.
🔹
تمامی شرکت‌های هواپیمایی از عبور پروازهای خود از آسمان عربستان خودداری کنند.
🔹
این هشدار تا زمان رفع محاصره فرودگاه بین‌المللی صنعا پابرجا خواهد بود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/671008" target="_blank">📅 17:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671007">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Re9sJ8pF9hRKnFIqWdn1mwtKNACktU_v_bhrvLLTKYAYd_xxIwGNX4yo3v6yDDYJ_n2HM77eHKiliKxqsF7ppwGefkom7qouc_cR5jMgdYzopUGYmUyVCL5nEBe30wnEUfKvj5x2YszgLVk46j-Tb0I0tBDU68YiKDJbYbsRRebBPIl96-CNmd3NJXMQgFf8wnyNym6PkxVK7nuuGuf1THO5BlopcwUHIXuz-SIgoMfhDu8706AhVGf96J-4_2SlVU1PvJ6C9lVAPWVEVr3FF7QvjB61aRQacG6U8K0UEyriUc33iFhkCJUg4nkHbntaBNL2WJtkkDi6ssFOWPOKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | قطعی برق خارج از زمان مقرر
🔹
اگر در محل زندگی یا محل کار شما برق خارج از جدول و زمان‌بندی اعلام‌شده قطع شده است، تجربه خود را برای ما ارسال کنید.
🔹
برای پیگیری این موضوع، لطفاً اطلاعات زیر را برای الو بنویسید:
• نام استان و شهر
• محله یا خیابان
• تاریخ و ساعت قطعی برق
• مدت زمان قطعی
• اگر از زمان اعلام‌شده متفاوت بوده، ساعت مقرر را نیز ذکر کنید.
🔸
گزارش‌های شما پس از بررسی، مبنای پیگیری و انعکاس این موضوع از سوی خبرفوری خواهد بود.
🔸
اطلاعات خود را از طریق شناسه زیر برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/671007" target="_blank">📅 17:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671006">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
تجاوز مجدد رژیم صهیونیستی به جنوب لبنان
🔹
منابع خبری گزارش دادند توپخانه ارتش رژیم صهیونیستی اطراف شهرک شبعا در جنوب لبنان را هدف قرار داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/671006" target="_blank">📅 17:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671005">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
پاسخ یمن به حمله به فرودگاه صنعا؛ فرودگاه «ابها» عربستان هدف قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/671005" target="_blank">📅 16:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671003">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AephBRiwDLP2RI8QxMHQm6NnWL-z1I0I7ik25OnIQy0LAI8wUARZnUy0_aT84qNbgXfibI71WD8W68CFSD7Zs3EupjXjvaYJonFKkycTw8fh12dzNR3jeaLybZxFx4YIELh4Ps9kL5-T-8pTV-geq1xaJRj2u5E_W-Pf4ORDK8kl3ZCnxcqYlw7DRmInzr4NAsWREl3GAj6H3sqQN57x1wzFVtk9iCvGVVYJ89kLujpBBJEQN5gN7wSvnph8xOPM0nJW3OUozi7SoggOHVJN_nlx9hbAcDnOwTF143SkBt79tZjEsJWKFo9zVm2FTK2jup7ofimGD0mI4vcRbzuiOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امید به زندگی ایرانیان در ۵۰ سال اخیر چه تغییری داشته است؟
🔹
امید به زندگی در ایران از ۴۳.۳ سال در ۱۳۳۹ به ۷۷.۹ سال در ۱۴۰۳ رسیده؛ یعنی طی بسش از ۶ دهه حدود ۳۴.۶ سال افزایش داشته است.
🔹
این شاخص میانگین سال‌هایی را نشان می‌دهد که انتظار می‌رود یک نوزاد، با فرض تداوم شرایط فعلی سلامت و مرگ‌ومیر، زندگی کند.
🔹
توسعه خدمات بهداشتی، واکسیناسیون و بهبود مراقبت‌های پزشکی از مهم‌ترین عوامل افزایش امید به زندگی در ایران بوده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/671003" target="_blank">📅 16:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671002">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OM_GVZ2T2JCaUnb4TGnzVoF3ECLh7RiWvOvRqtlSYjfsrpwH5WNc20CnNeYvHuJIa_UcFISiLHJpt7N7zu7S8YEeh3t8Kh2V2j7V-uL7Y-RhM6TeerxLhDjfdjrRaWEQQ7zLJJYV1euspkvEMqFK92-xhSWX4T5WxeRyH4wi5CCwj_xs729wWfD29AaTM15u0NA_bawjSrnF8v4hM3XTDcCJpdnI3DyOljPR0QtDaRntMm40dT_ladV0HEjm4ljekJFJ6xCKVnOmNFjdtdUN7ZZZgyVQNprJA48eeFGOh5bbjk_tkfT4OIBZoySys08e3SfSjrBRsgJVPP7lhtDmMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قلعه بابک، آذربایجان شرقی
🇮🇷
#ایران_زیبا
#اخبار_اذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/671002" target="_blank">📅 16:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671001">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzjlEJj2SbFqVuokdqOkTKFZ2_UIuX_4zcYsfVv2fEjDuXw1Z6kFiZ8FFQIpKhO3mxUqPoDgztorOLfXxwgaEtKn9YH7LDpQhY1fMzAH8pJ4xzDt9Kjz28S2r97T0wRgUQvqyhd0g6inh9Lu66UHu6PAfAyG7QNOeRry3AvXbAgjx_HAKzOTFPuVqDneIEseijTzw7O3Gxynlq-uBkB3a4m8vp-i1_I7c4eO_1VA7DVOtnvJg2hMurq3Lqdw1w9HMBagE5ULELryZh9hteEJtCFp3KB_1bFPvpB1t480Hzg_ij9rFLFG5q3qpRBQw7ekcOqj2yrJWnC_fqEKupzlXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا در صندوق طلای «رز ترنج» سرمایه‌گذاری کنیم؟
🟢
خرید با حداقل ۱۰۰ هزار تومان
🟢
سرمایه‌گذاری امن در طلا با پشتوانه طلای فیزیکی
🟢
بدون پرداخت اجرت ساخت و مالیات
🟢
بدون دغدغه نگهداری، سرقت و تشخیص اصالت طلا
🟢
خرید و فروش آنلاین از تمام کارگزاری‌ها با جستجوی نماد «رز ترنج»
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/671001" target="_blank">📅 16:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670996">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIAk2n1vxixcxLDKhujqQajA7tRN58dtAABrXMolcNiULzzT80T-UgN0vXLZNADxZYUUJj75JiTSwKcWVqn15xAIMnuqBM1LXVeJQZIoZnfV4knnHtWQEO_Bg7umplf0Y-EVWxSRJyKOspfTCWzz1i6NU1egSgJpIn9JM7v9ib7NKKVhA7rqw7T3AGd3RkfhMsV88F8kd8VfRriRQfC3U2MO7vIZ4t9lTT1pf8JjWLjmxtnDflPsy86I6zs-_K5tSE6PZre7d7ZnbJVuDewa8CeQBikOXlQ_FnOU0RCWBab02PQpxbOzWYNfFtOOluNI1x5xX1gFCX0-q5Ox2wmxTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوه کلنگ که ترامپ تهدید به حمله به آن کرد، کجاست؟ / تاسیسات مرموز ایران در قلب زاگرس
🔹
رئیس جمهور آمریکا در صحبت های اخیر خود به حمله به کوه کلنگ اشاره کرده است. اما این کوه کجاست و اهمیت آن در چیست؟
دراین‌باره بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3230219</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/670996" target="_blank">📅 16:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670991">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiM_sIKuXubF0UGOIuzDqdHsDxvfrI51UxyNT7JeZKNi1RftUf7Lg9V0QmbUgM9Pj1dqNEuMcTch6dg3UYiR4XfeOvHsnLjW55Z_G5bzFJKHPh5dV3vbMBVwMbeulnjsbtvPn1A26OeMvysk4-cQdWt25s6fsBwOvgHycSlSqFieutiUffgmSIZ_l9ciR8AfBN24ePumUA-NSmli37il8mZialnn_DUFAtXn2GovhAvnXVEBMLBFFMmfVA17QTrt8HpBejrMHruwp_kvytu8Ke7s8AmJYWWeC6iA-4aSm_rBUu0iShPjGFcEcVXwKQrl0ixG5vYdkEj0nUJrVPFlbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRCJPi1WtAt_G4VauOROIZM7X8xdR2hAzRnhTxA-ZSziNyLPsQwoAmmlwAlzdyUawpKClsdygVFJWBP7-sLV4aJ-GH4VKV82HEy4LoIP7qvEwEewO4oRAB2qwfdwvJcjY_a3qAdd1GylIWhLeZUSoXfukTvqMTZCx0UNG6P22XBjn5J1TS5xccnY-m7uG6iyZhDzRX_U4YdOy6RkwJD1_wo26HWEy0WrgYy51SXHObB4hMk19G2qg2N1EfsS8MZgWZ-Y0eo5VJBKV-TgIN029x6AaweWAjEwkwA9UYoRrbxjeg5vwq_C_KMj98MwQ7Xph_yg50NvJv9bo3pvyoSUWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ks3Qv8IjX7BOikmBY2mJ4cD2dWBYevzW1zqRThTAPgfQWSHhI4ETOmAXS_pwxU-Bf7jJIj_BGQRgYyEC2hiA-3QB6x9skLHeBVsENGD67GrtYfQfwAenUu9tmZCEYuxedDqnpki7Ffl0jOqt7EfAAn9JYNJeva9n4Bi2ON7blPREkaHREIGHJeVHCruMBfLbaBcbce0uVoG_Xxo3dBXSH5z8saoQyquEWXBZXHPnXI1wJKY8-7Xa9590TAhXwxg5dnnapBVZq1hStPEhseNIoD_tiNqxwk51abTGqR7h8U4R1poYKfkqDIvf5n3p71naKx2ij10g8ghH9Fl0iLPfvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kwApLXuYZDSgWTQq1Q51w3yV5quvhdiB0pUAiS8OfNK1aKMgk7fZiejzsyiWFOICwwHC8ep1oQU9abOknszoN45d3qTnm85o600hUYM0aU73EJzF3lARmM9nOgEIAYMMpQtpVNEsxSGmmS21TeJ6qe-jgKqplWarl7mmd-qOEYSi-5-lXwrc4RigKLnsP7nISXXKdAlQgZSHzBLqicnGsNP68MiyP1ulBBF8N0qOhUlcviYlS-qy2dP2Bli3PJ9b4I-5QdPXMWqqqQo7yGV7YNLUn4u7-N11nhRJ3VxIfrmADiiw9z62QRnlB6ArUht5b1t9psFOsrN9aXMcGIOX-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHmHMXXyQ5AYr6v060CeoF24-gpNh-3vVVNnSV6XyOA59d9609DfOdx5tFZxdGsCgOdH0zOJd_kYzbyqFb8Me8_QkaAAuEkAMIJd3txpoN1M8BWys6bPSCJjFGNCrL96yUMlOiNYqzyKr9ZGZQr0-CVbCIdDR4pv-lduyF1javcVvuAVW15vPWmzp04DDIp47Fd0hRXTiBrVSixw4PvrCVgBPQLUU9u0ttG-WFOQCO5QkJIxtA8h-jWqprTT7vX21UcJmkujPuE25D65m38p-ZU4cMOt9mh_0xsxbKfCNCwgkV5pKZOTnxgz0_Wl5YANf5QkbwWjbtDY1RG0xlhrrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند اصل کلیدی پس‌انداز رو یاد بگیر تا پولت رو‌ هوشمندانه  ذخیره کنی
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/670991" target="_blank">📅 16:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670988">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_kkVK15tWZuSin8vWYd2VLUz6ZpSXNHD1m2lwvQ0h1dBWuihOSwUZwhMEvzB4Iu8-f7R_a-6KmfS4bf803S88eif9IFUgbeBG3-eK6T8Pk5uW17QtGrv2GjrCvYAMNFkHodBinhXtjqVhtGHvFcGolYdO-MleosuPdUw2C_nrJDLCRqejuz0u5v5918tQBsFENyz8HVmpDUkhuA7g8B10eR_iQ1pnXV-SLlKAre2aVfKyNHYgANIMG8L8T-6Xr0nsSdGBnFPquL9D8reSennG7eLRZtjPSHUSMbW0vfqpAxdjxpR_IoVP6WQzTxaoS32CBU_-pCHuOd_YUPljbSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
آخرین وضعیت ارائه خدمات بانک ملی ایران؛ از واریز سود سپرده‌ها تا وصول چک
🔹
با ادامه روند بازگشت خدمات بانک ملی ایران، بخش عمده‌ای از خدمات بانکی از جمله واریز سود سپرده، خدمات چک، پرداخت اقساط تسهیلات، انتقال وجه، خدمات کارت و مدیریت پرداخت‌ها به پایداری رسیده است. متخصصان بانک نیز همزمان در حال تثبیت پایداری سامانه‌ها و تکمیل بازگشت سایر خدمات هستند.
🔗
مشروح خبر...
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/670988" target="_blank">📅 16:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670987">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
چهار نقطه شهر بوشهر مورد اصابت پرتابه دشمن قرار گرفت  استانداری بوشهر:
🔹
در ادامه نقض آتش بس و تفاهم از سوی دشمن امریکایی ظهر امروز چهار نقطه شهر بوشهر مورد اصابت پرتابه های دشمن قرار گرفت./ ایرنا  #اخبار_بوشهر در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/670987" target="_blank">📅 16:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670984">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
داریوش فرضیایی به سوگ مادر نشست
🔹
«داریوش فرضیایی» مجری و برنامه‌ساز شناخته‌شده تلویزیون که سال‌ها با نام «عمو پورنگ» در میان مخاطبان شناخته می‌شود، در غم از دست دادن مادر خود عزادار شد./تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/670984" target="_blank">📅 15:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670983">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJSoSgTcWXnExsh8iDi6PkSoqqh1o44AYyZuN0FKkB94H6iFSFitTcfXkY_axrXnZVupWWRuXKekeGCm7OV6yrJw8CLWaD7zQKiPGlMEboMUnPx3iyGk242Shk9LwCGr4RxDDMGjEuarLRs52IdEe601bp-Md3VVnl_9qGkX-iz7YrOwk43F0D1mG-IX0Bp63PUid0eMNeZOGvBnmTXe6HG38HZPL6uFXRkgePPX5A6chLWrBXQ8Mm0dyXqM5HA4RXestSucWNize2qXhGqM9uqeJvyAEYX8JCHBJxnhB1R5lER7vxLfmuNc1k7_BqOrUvxnrqwRSUYzlqYD35385A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمپین بزرگ اسنپ‌مارکت با جایزه ۵ میلیاردی
🔹
اسنپ‌مارکت کمپین تابستانی خود را با جایزه نقدی ۵ میلیارد تومان برای یک نفر آغاز کرده و به ازای هر خرید، یک شانس در قرعه‌کشی نهایی به کاربران می‌دهد.
🔹
این کمپین با هدف قدردانی از همراهی کاربران طراحی شده تا خریدهای روزمره را به تجربه‌ای هیجان‌انگیزتر تبدیل کند؛ یعنی هرچه خرید بیشتر، شانس برنده شدن هم بیشتر.
🔹
به گفته اسنپ‌مارکت، فرآیند انتخاب برنده نهایی با رعایت ضوابط و در چارچوبی شفاف، طی مراسمی با پوشش سراسری برگزار و نتیجه آن به‌صورت رسمی اعلام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/670983" target="_blank">📅 15:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670980">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
آزادی ۵۵ صیاد ایرانی از بازداشتگاه‌های امارات
سفارت ایران در ابوظبی:
🔹
۵۵ صیاد اهل سیستان و بلوچستان و هرمزگان که به دلیل اختلال در سامانه‌های ردیابی توسط گارد ساحلی امارات بازداشت شده بودند، پس از حدود دو ماه آزاد شدند و در حال بازگشت به کشور هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/670980" target="_blank">📅 15:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670977">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EzzYJMjm-6jKFEK6xThVQvjKvZ2jmzVMVZ9TAzXnBMFyH83CnMa7Oy8kqd16OyqDL7TITxUTOukplI3e0lh4i7TBCpYNamB_nw5vWULdYx-4oQbZXxV_XPQFAfeWC4eWQBqej6-paOfFXPeqwtRcs522pPZKl7Gfh5hJ-OD3ekStIvW1zAbsLYsFf1B3Y1nY_cLg7uaYZC1oW3WityME9snLzFoE9oDF_jf19svwAcRkLcmdd1En7BdLwIkeVKWU7d1hGOGOBaVTNW4iDwynqf-lSh_UpcyUnpMLQGz_cNIcyPpzs0nX-5ljontyFFgSxHcpS9GjGBSmN6QxTgSprw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J7oaha0Sk3G6zvbMvo04LIQ2rJnbeqI1WLzCFvw_SyMXyMqBJP4qUj4lPn_fYTZ7zr9QdPHROnf_syv-GCCwHgXWd_oEG8jmeRxcvnBACkzCHjrdYX63HnW57WPE7jACN5ngZp_lugTwk5CB-YKoIsvp4Bf-30k9ba_fCxva_KWSzslw6WSjMkSXUX2lOWc_pbUMaf_lIkG-gBNAb49F2k9wvYhrNXoFNmierKMTwCID0kcuagdCGmuLTN9zHT8Xy_9sczeoHBDBjwb5l4NpxRt6C3NYCQOAOLbX6dwVAjIRN0m42IISgLQynNNjxSDtgd65-F_n3gcS4een5Rnghw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iytoFO1O7vWk4i3j74K9ExrIQCIz8cydNVyrnNHaV7X_KJsF5ubEz-gTytIRLXsyOjZjt6Kl9XMTbSwuljFWu5AbkVTwmukr78tdY7A2qNoF8kbDkiTvr-8JRfb9dATMDSNNvJEEZg2v-HJsotk_uTtfSnQEn2Gxw-4PjDUdL_tdcFsT_E3SBVPIrP2qS80HOu_rj0nwO0jD6RTV4g5hGO8_pNWV3GKe54_qg6i9VcpNM4pyNud0mQIXMGBMzRLvDzIc8kM5X4t49T5J9esvIeRIudK-WCB4AXUcfZLSAp0HjXUnDsPDGCVfN3vuAkvid7bvxNymc_zVLyJhFFWl7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ظهور نقص فنی در نمایشگر گلکسی S26 اولترا
🔹
سامسونگ در پی گزارش‌های کاربران مبنی بر مشاهده هاله قرمز در مرکز نمایشگر گلکسی S26 اولترا، تحقیقات گسترده‌ای را آغاز کرده است.
🔹
کارشناسان احتمال می‌دهند این مشکل ناشی از نقص سخت‌افزاری در فناوری جدید «نمایشگر حریم خصوصی» باشد که با تنظیمات نرم‌افزاری قابل رفع نیست و می‌تواند منجر به تعویض قطعات شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/670977" target="_blank">📅 15:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670975">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
افسر ارتش صدام: روزی نبود که خبر ترور کسی را در خانه‎اش نشنویم؛ ایران بعد از جنگ هیچ‌کدام از فرماندهان و خلبانان بعثی زمان جنگ را رها نکرد و همه را حذف کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/670975" target="_blank">📅 15:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670972">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZF1WbLeTI1OR2QfhiX9uU-_jaDgOkXJAN4-vijbjjsqJ__pucTujDpXACCx-iLOXfVCCLd9ZVgMEao-0DZ_v-eyszk0o6jE7g9NSVVl3V7Ixj66c5JKAB4eEFL3CUk1h75gIszVbRjpPfvsG_dQkzZebKyNRjntpZxUl0mghizGBOq8KleHsKTR_VP6JeS-2QlEexZbXHOouT4u_cFbb3VjQPBe5rznhpwxmXOJ6m6U4VKfN4oMk0M1Yf5KPwrHAh1W9BAZGXDPgDMuJ-xbKHUk0XDZ0wJPF454nqyt7kRvfzZXL2-ACqIcfWk7IqCR9NFs6EfHa0cVAiN8qP9lcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احمدی‌نژاد با دوستان و همکارانش دیدار کرد
🔹
این اقدام پس‌از شایعه نیویورک‌تایمز مبنی بر حصر خانگی محمود احمدی‌نژاد صورت گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/670972" target="_blank">📅 15:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670969">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
روایت سرلشکر صفوی از بینش رهبر شهید انقلاب به مسائل منطقه‌ای و نظامی
سرلشکر پاسدار رحیم صفوی:
🔹
در سال ۷۶، ما ۲هزار موشک داشتیم، حضرت آقا در آن زمان فرمودند ۲هزار موشک کم است و باید به چند ۱۰ هزار موشک برای چندین ماه جنگ برسد.
🔹
۱۵ سال قبل حضرت آقا به بستن تنگه هرمز به عنوان یک ابزار نگاه می‌کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/670969" target="_blank">📅 14:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670967">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1XUmTm5ak3YVpWAXl6gQHqk7S-bjMBlpGZfqnxQ1ORgw-nBhEHRw9cPpFuwXdJdrRxVv_H96KkAA3RaYmA0CmTzdFG20-oQs99VwnzSURR8LG9Af3XTV4csFEPhM6SYmC-3md0Z52FZ-yCcnSRYkONgZECVorY3XZVhNnmOAiUIoUGssSBCr6Y7Ntqfi5Cg_f3TOo7ewloCbqgf0bou7aAGPbtXcH6I-8vNKodjSjj5OCK1GMZJzVNyUMUv1FrqayvK9LZs4Vgk1Lnve-UPS8kUMZBCq8sMhQVgjXB936evll06zqqYFEZRfD7bzzmfq5zwB1aPzxgBbrhxjVRyyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار بیمه‌ای؛ چالش بزرگ تأمین اجتماعی
🔸
برآوردها نشان می‌دهد سالانه حدود ۴۳۰ هزار میلیارد تومان فرار بیمه‌ای در کشور رخ می‌دهد.
🔸
بازگشت بخشی از منابع ناشی از فرار بیمه‌ای می‌تواند به تقویت منابع سازمان تأمین اجتماعی و بهبود مستمری بازنشستگان کمک کند.
@amarfact</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/670967" target="_blank">📅 14:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670964">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
اصابت چند پرتابه دشمن به غرب بندرعباس تأیید شد
🔹
استانداری هرمزگان برخورد این پرتابه‌ها را در حدود ساعت ۱۳ امروز تایید و اعلام کرد که اخبار تکمیلی در این خصوص به زودی اطلاع‌رسانی می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/670964" target="_blank">📅 14:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670963">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c662d108c6.mp4?token=ZmggD7SCf8hZeos6MNR1etkf72_gc6GMQ631WsfZFPbE6paQNPwVl_oPOj_VEB1Yg9LKgwoAN7JlVAkHe0JLqAFY9Y1Se0EgZsUIYKhvCploCgf_kk9rihOIy2uP9D6x5ieOHCSdE73oizCfaUeZktSQ5l_O2_rVMR881ncTH5_FpAqPxZie4KPMYxdBEcye3gDdopaaOTsETrvP7fs-HjzOh4xsrHibkAZKIsFdyjv3uB-v3dm3x6Lg9TJmjScocnuAjSsNeds308gHyQAhVfXZ3Bg9avPU173i2LEzqeQzSf4FdInZE_0UMBhooOs_z_fWjWOTzsXz0ZK_KZcQ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c662d108c6.mp4?token=ZmggD7SCf8hZeos6MNR1etkf72_gc6GMQ631WsfZFPbE6paQNPwVl_oPOj_VEB1Yg9LKgwoAN7JlVAkHe0JLqAFY9Y1Se0EgZsUIYKhvCploCgf_kk9rihOIy2uP9D6x5ieOHCSdE73oizCfaUeZktSQ5l_O2_rVMR881ncTH5_FpAqPxZie4KPMYxdBEcye3gDdopaaOTsETrvP7fs-HjzOh4xsrHibkAZKIsFdyjv3uB-v3dm3x6Lg9TJmjScocnuAjSsNeds308gHyQAhVfXZ3Bg9avPU173i2LEzqeQzSf4FdInZE_0UMBhooOs_z_fWjWOTzsXz0ZK_KZcQ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار ویدئوی قتل مهاجر کلمبیایی به دست مأموران اداره مهاجرت آمریکا
🔹
تصاویر دوربین مداربسته، لحظات منتهی به تیراندازی مرگبار مأموران اداره مهاجرت و گمرک آمریکا (ICE) به یک مرد ۲۶ ساله کلمبیایی را در شهر «بیدفورد» ایالت مین به ثبت کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/670963" target="_blank">📅 14:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670961">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8e2326267.mp4?token=vfJhOjHOaLqYIsmPXlE9XFXD3Kkzjw2kstVm37AyUdpsvczitwxeS2-7_K6Le8EeWkdAbKDVMUW05yvl0Lhw_4H_F6lMLSGXhUkNNMzh3nUpNHPUedllukrW-j49--KdwyrJZtUMNEEJaptAmqJFVanbp9I5jr_kF6t5mg_nL-zZjBfLW2shF4oKxp4mFYSx5awdd7psshrkTO-bao3EIZhGZE7J1ge8jkzvUdPEi3mDw0IeTtj5qJYZd8kTntnhcnKOQ2zk00xfXpr9jQU7oyMbbOXeqB-qubGIKg8u8iKHRhHC6Ii696CTfx7xGowv5Kz9q67Y1pCMIJtvty9xzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8e2326267.mp4?token=vfJhOjHOaLqYIsmPXlE9XFXD3Kkzjw2kstVm37AyUdpsvczitwxeS2-7_K6Le8EeWkdAbKDVMUW05yvl0Lhw_4H_F6lMLSGXhUkNNMzh3nUpNHPUedllukrW-j49--KdwyrJZtUMNEEJaptAmqJFVanbp9I5jr_kF6t5mg_nL-zZjBfLW2shF4oKxp4mFYSx5awdd7psshrkTO-bao3EIZhGZE7J1ge8jkzvUdPEi3mDw0IeTtj5qJYZd8kTntnhcnKOQ2zk00xfXpr9jQU7oyMbbOXeqB-qubGIKg8u8iKHRhHC6Ii696CTfx7xGowv5Kz9q67Y1pCMIJtvty9xzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصویر از آمبولانسی که در حمله به لار مورد اصابت قرار گرفت
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/670961" target="_blank">📅 14:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670959">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_9GFSslilqQnLBTu1sUrBzVa17VvTlGlypYEhttqR-_i_JH9pc2y1fiI8lCQdnL7rH1qr43cG5LrDD0O0oNKJDIQq34Ebnw2RItFH3gsksBDJvXLZyqnmTRVR0XOXDBX1-inqQvKhX6jjciLfEeu3r7jW_G5pRS8_xOLOf9JMRcDtLn_hjet6QE4v-qFWTDXQxPGNMq-ZF3KVdHwOp5U7KYgip6qHwD8WLr8XHl79eKiozjZBsYQ9QkyWkX_CvFIYpQejB4LQ937YORIc3XfJALVaeKC0TSQPJ0_QWHDCaWd5VvpLBtKYuchET_yWAWq8FPekMzF_lGPsNiD5Uyiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۳ تیر ۱۴۰۵؛ ساعت ۱۲:۳۰
🔹
دلار امروز با ادامه روند صعودی به حدود ۱۸۳ هزار تومان رسید و نسبت به روز گذشته افزایش قیمت را ثبت کرد.
🔹
در بازار طلا و سکه هم سکه بهار آزادی با رشد روزانه، به حدود ۱۷۵ میلیون تومان صعود کرد.
🔹
روند امروز بازار ارز و طلا نشان می‌دهد که فشار افزایشی همچنان بر معاملات این دو بازار سایه انداخته است./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/670959" target="_blank">📅 14:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670958">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
اصابت پرتابه به آبادان و حوالی ماهشهر
معاون امنیتی و انتظامی استانداری خوزستان:
🔹
امروز سه‌شنبه ۲۳ تیرماه، در ساعت ۱۳:۲۵ نقطه‌ای در شهرستان آبادان و در ساعت ۱۳:۳۰ نیز نقطه‌ای در حوالی ماهشهر هدف اصابت پرتابه قرار گرفت.
🔹
حادثه دوم به دو انفجار شدید منجر شده و جزئیات تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/670958" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670957">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_cS6QaVO0b4lqK4EEBWUL70RQiQ7qRuF4VtEi39walfY_TlNO2QJ3aIpRRT4l7trLxFYZqNexQGbmFI9p9ojImmgBQVTepU0F0RhRRcTLO_D0pNJhUkCMFwBz85g0H8-Htyt7cNJmLdB3Zy55kFkMSyOMI3W0BLsA1Yhk-hiiDTqkPlDH1H5vOyfhURwrbSo6kJqZu4pKeC7_JT_VTCf9jnA8y-RZHnvBlZNMuazYMbLX1CS70AkKazG87E8VraU667ln9gs7fsWvwWTekDOV8PG7jFTCEgxQ0ALTXkxhLQmQUqWiKMP5nVYls4ZqLaSA2ATuapIuoZ4WM4ziLbXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت همچنان صعودی است؛ ۸۷.۲۳ دلار به ازای هر بشکه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/670957" target="_blank">📅 14:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670956">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
تیزر قسمت اول از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای سعید اعمی که به دلیل پیدایش غده‌ای در بدن و عمل جراحی برای رفع آن، روح از جسم ایشان جدا شده و در عالم برزخ، عذاب و ثوابی که با مرور تمام امور زندگی از جمله اذیت فروشنده پیر در ۵ سالگی تا کمک به جوان در راه مانده در بزرگسالی را درک می‌کند؛ نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سعید اعمی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/670956" target="_blank">📅 14:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670950">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XJLlvolTGoEFYCoHiI-wHocNhcX3PHv8QjKkBgo4G6S22Aj2Hgit_LMAZMaZrJjcK_AQTvwjQNRv6ONyZutrGqSKXc4OTQOnIDI6Q-DvblORoW4Osb4m6WQJhmywKs6eIFDTzOsHtlVZmNzipuX-CspyGlBc84-4vwtgKGZFrpmeX0f0m-x4bkk6I-U-68nlYnxRJje5ZMPrN0KMjlf4usMEd-ET7KShy5d0eHkFwQzt-IWfg3xv9JYEGTaDc9bQGP9swaFzEb0EhBQG9xGGDlgY533uZvA3HYI5c5tT1yBKTGCkWjm6xrfUNjr1ZNZ2OT5cC1dK5K0mxO8GaSC1Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZdJxXQ8BE3dI5MFyVvrSjGDDRpix526If7AqysUwR8Zel1FUOHNj-E9ruCCRjp2EQt1ohZHOs6FgTF2fnbhGRW1sOGcN_9NicTnc5ZLLC0ug8tche5iszqu52EGTa80lODDdokADzgO1OMKBuvpsL02R8RamRt6TTBs4jim0jZVsrY9PxVMycDQOltEfK7nqINeDb3Nk6oULGmZCWNyWVh1QTKslLo25YeaORoMCnfAr9GUlmW0UqjCce7zKguy_XCP9bO1RseQ0HQO92qoouk21rJPcTAilgQD-54NsL6r_A9gP3WMPvny9Y4Q53mmE_lC9wz8XDCh9QnsWshcbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fm_i6fEcupuFa4elB9VI_1ZUKN2itEKnITlECNaJpk88rnfO_jE6KHICrOpRzBF9NtEKM-X-yFyhHOQbCk5Y-8Kb0r7-rTcO9_XUVg08AHkMqjBVNuNYbmQ_L53MIIWx7cmSS_-F5fmkgAT88EYmClqu8W56cyUlm25GavT_Q94raGoR_NRopjyl_v_thC3256fyP4EaF03XGEnycxTmSjlphCfEHqI0nL5_94nygJvilToodISV9gd3k1aCzk3bIMZXicM8bVhU5IsX1r-GvjMt3bWg6-66rlA3g7ne6e17v-BOnSE-RXieJvwaTivOuNdW7OKD1zhpSQ4oulpzHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qEKQ3tSasZ_3YxmvUgGs7bGzARoAHXNOaQSQ-hmnaC4OnxnG5NR-i33l8JJiLSLmf0CYK4S4rsUgrnROIPtjMKWpuLSZRX1vJRvup70qUYk4rkQtFrEAa66eRGGJmTW6YIfmxHcHmsQB6grpraK2vWZOcsS8XJZeEGbOl3brywRLs7rY5LmwjHNwH9IHxCNObVaw-HXrKTakg4btrUe9OlO-sR97QmmG8vZRc7YYY6xWITflMlOs5eV87kn4SIgDL76MeOCcPF1ACuP2JdZXkkidkheu9rOZnSTqUnPQpHD8Sbuko3HFRRnfaApjuBkQaugoZ0diqm4mHgnW4iIvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7Xn9vc1NTwTeW2aTsIaRw3ft0FRgz_Cu-qj5DrDVDDLrIggJS6OlaGRRbDFKrqJD5b4O-1bVixcx8OseoV6CLdYeJ5tuftqaokdlPaxRkNg_IZSCJ1mbl7BokZrVv0e8Z2YKVB0ZNgT7DkLKJDTR32jQyP_uxiSAe7JUpLck7u0sSbVi8HalJYZuVRjVIWP3sr_Ym5-DDNl22ARV89j5hOaI-F1mXKZAcN5V1CEFY4THzrJhLmFe1wyUsAv2tvdZBCA40L3PzFJbgnsn-g3ArS8_wfWSKfbve1IEbbUtz3oU_jIzC7YJ5bTK4fUWAEALGCtd9hUwn3JlkYLz3biaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUe887w_E-JCl0vgDlxIKM9lFFqcIw8ZhoXbhqYCQK0KbtIJ6-7MWfZ2DUrEPbMVmqHFezZHZzJyyZ-_iBKc4L3uihv43zZdUew3fjFxKC38-eGrpK8gREeQfmNl9p0OpAb7hHmL6fZpBekJC8GIWXX_7npNoLHqNuSZq0Ipm6Y5p1Ha5U-D7i2u5sRvaUHO27KjyP9ASlsPV6rPrCaXMhk89XfZgJMF0LOLDBuFMl3AdVQQk-BSfhk5EGqLLl8FumFCFCCYDaHuYUHgtYnJ9vCy7iFCvbJZ49ZQgltMMrC1MSv3Z7uKCFs54InoUfpCxhB3rNinlr2MSQAiay5hbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شال مناسب هر رنگ لباس؛ این ترکیب‌ها استایل‌تان را چند برابر جذاب می‌کند
😍
#فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/670950" target="_blank">📅 14:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670949">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6bd01cff0.mp4?token=lit6Nn3yjGh2TSs_qBKGnPUr96DNEA7U6kvQrCm3DgtK_nDyauTHddiJop2ZVaaU-_94GBkTMNDQqoxvqx79zzV2cyCBSDmP8DVcJCWLcWAEKhhEIrt_J-QNOks-ClFKqINzjUy4cDRPhLUEAJCBWT1SyxZx-Sm3y9VikO7qQrzGM7A7DsODLu-R6FcsX1wavzOcIfeBIbv22aWWcAth6OF8ta5euplBYVqz5B5L0yFJZUzoxUDiSn-Wvb7FQdzEbPNkxpaLoAWUSz8UG-5rBSB9uJ60kmALWdgsYKoC0aEIIItywAiXpI805JAj8y2ydVKOc17PowzMnkySMRtjiAf7rh7L7jZdLJsEqLcxTxY8jukaK7IQ1guQFV4YMf6JCFZi6x4iSvhCaQIf2ZCpeexG_m1hBzMwhkIaxQANwwq0nJjqa97Qe2kpI5vU50IkkaF-Gfs81SXeIXKVV7WD2bmdSruHjLVdRj7F5YABMsFG9M7mdfsjRsGfJgLzvuTrXC0-0d-nrmlKnFNPTT4CXkJTkhdAgRScgTgpL4DFq-SC0FwFeJ-vK0tXYzMj8QR1liHjghATMMedXCG-_4oMeTqqBHJm6OWwztolVnBdYz71L5JdUUKuHO9ExBnujrD3rrOkhy8IuoKUZT8DjFz5fbs7UsIdSxG-iyeuDcZURe0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6bd01cff0.mp4?token=lit6Nn3yjGh2TSs_qBKGnPUr96DNEA7U6kvQrCm3DgtK_nDyauTHddiJop2ZVaaU-_94GBkTMNDQqoxvqx79zzV2cyCBSDmP8DVcJCWLcWAEKhhEIrt_J-QNOks-ClFKqINzjUy4cDRPhLUEAJCBWT1SyxZx-Sm3y9VikO7qQrzGM7A7DsODLu-R6FcsX1wavzOcIfeBIbv22aWWcAth6OF8ta5euplBYVqz5B5L0yFJZUzoxUDiSn-Wvb7FQdzEbPNkxpaLoAWUSz8UG-5rBSB9uJ60kmALWdgsYKoC0aEIIItywAiXpI805JAj8y2ydVKOc17PowzMnkySMRtjiAf7rh7L7jZdLJsEqLcxTxY8jukaK7IQ1guQFV4YMf6JCFZi6x4iSvhCaQIf2ZCpeexG_m1hBzMwhkIaxQANwwq0nJjqa97Qe2kpI5vU50IkkaF-Gfs81SXeIXKVV7WD2bmdSruHjLVdRj7F5YABMsFG9M7mdfsjRsGfJgLzvuTrXC0-0d-nrmlKnFNPTT4CXkJTkhdAgRScgTgpL4DFq-SC0FwFeJ-vK0tXYzMj8QR1liHjghATMMedXCG-_4oMeTqqBHJm6OWwztolVnBdYz71L5JdUUKuHO9ExBnujrD3rrOkhy8IuoKUZT8DjFz5fbs7UsIdSxG-iyeuDcZURe0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری شبکه عربی: کسی به ایران خرده نگیرد که ایران حق همسایگی را رعایت نمی‌کند، کدام حق همسایگی..!؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/670949" target="_blank">📅 13:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670947">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLxixDbOlNE2pH_GTwV9xDetX5vhspo0yIO_fZIKIF9QgMnB6PlP0Pc0RXaVeAitgI4ZLmqwFHUpuVRdJtudoo7x7LDX3YHs5a6iCN7Tr9dK-miect-t4WVxbxoMNMX7it6SusiHyoa53KWVlKirtJ4j1s_N_2JGgHna8leEV1Lfk42E4f1O8GSfyG8SbNdyrGyo43PbqP_fAJFTHvQNW__K6dlKEey-XhvVQjTOkDl-kuu-41AUumid-pzOEwq64WVOawSfiFdQTN4zQ_CcErPN6fhLamg18OFt-iFnbBq8pfkNF6YgoAoluJyZlphU39GrZAbE0yaTKbsQTuQaIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
تنها ۲ روز تا پایان مهلت ارسال آثار به سوگواره رسانه‌ای «بدرقه یار» باقی مانده است.
▪️
سوگواره «بدرقه یار» فرصتی برای ثبت و ماندگار کردن روایت‌های مردمی و آثار رسانه‌ای مرتبط با تشییع رهبر شهید انقلاب است. از تمامی هنرمندان، عکاسان، خبرنگاران، فعالان رسانه و تولیدکنندگان محتوا دعوت می‌شود آثار خود را به دبیرخانه این سوگواره ارسال کنند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگوتایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (پوستر و انیمیشن)
📌
هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش به دبیرخانه سوگواره ارسال کند.
🏆
به برگزیدگان هر بخش، جوایز ارزنده و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت نهایی ارسال آثار:
۲۵ تیرماه ۱۴۰۵
📩
لینک ثبت آثار:
https://survey.porsline.ir/s/aU5VZuaW
📨
همچنین می‌توانید آثار خود را از طریق شناسه زیر در تمامی پیام‌رسان‌ها ارسال کنید:
@Badraghe_yar
برای اطلاع از آخرین اخبار و جزئیات سوگواره، کانال رسمی «بدرقه یار» را دنبال کنید
👇
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/670947" target="_blank">📅 13:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670946">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
رویترز: ۸۰ درصد آمریکایی‌ها جنگ با ایران را طولانی می‌دانند
🔹
طبق نظرسنجی رویترز/ایپسوس از هر پنج آمریکایی، چهار نفر انتظار دارند جنگ آمریکا با ایران برای مدت طولانی ادامه یابد.
🔹
این نظرسنجی نشان داد که ۷۹ درصد از پاسخ‌دهندگان فکر می‌کنند دخالت نظامی آمریکا در ایران «برای مدت طولانی ادامه خواهد یافت»، که نسبت به ۶۵ درصد در اواخر ماه مارس افزایش یافته است.
🔹
تنها ۱۸ درصد از پاسخ‌دهندگان گفتند که فکر می‌کنند جنگ «خیلی سریع و ظرف چند هفته پایان می‌یابد.»/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/670946" target="_blank">📅 13:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670945">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
اصابت چند پرتابه دشمن به غرب بندرعباس تأیید شد
🔹
استانداری هرمزگان برخورد این پرتابه‌ها را در حدود ساعت ۱۳ امروز تایید و اعلام کرد که اخبار تکمیلی در این خصوص به زودی اطلاع‌رسانی می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/670945" target="_blank">📅 13:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670943">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
چهار نقطه شهر بوشهر مورد اصابت پرتابه دشمن قرار گرفت
استانداری بوشهر:
🔹
در ادامه نقض آتش بس و تفاهم از سوی دشمن امریکایی ظهر امروز چهار نقطه شهر بوشهر مورد اصابت پرتابه های دشمن قرار گرفت./ ایرنا
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/670943" target="_blank">📅 13:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670942">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21c16fb8d.mp4?token=evx-7OhzBx1vHrAo21LHnOvCSo_VLHzF2_rziTMh7RQD6lZoyvvD1iso2-YbHqgMVNc90xTkj-Bw3N19RxFEofC4eSy008UxAWQaOrqyLCImeFbRpxXLKtcee7ljF6J-GaBKpO5RaFI6fAQ8IGo-ZDMnWwiMY9J6LMvyCpD1S0e7p9pEP7jjwlxy9XbWPk3ZVrIBzPUDOXygGAXeolyu7eIa_XJiQ1jFbhRRJ7utxGmIsSMntWLfl4mRBE67ptqzbyc7sxPvI6Uk41DyetWIuOsJj8_jJFbwajiQKKUuo51KlH0NcwQO-jp9ruaDMUiVuOVep0s00Hh0kW7_G367SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21c16fb8d.mp4?token=evx-7OhzBx1vHrAo21LHnOvCSo_VLHzF2_rziTMh7RQD6lZoyvvD1iso2-YbHqgMVNc90xTkj-Bw3N19RxFEofC4eSy008UxAWQaOrqyLCImeFbRpxXLKtcee7ljF6J-GaBKpO5RaFI6fAQ8IGo-ZDMnWwiMY9J6LMvyCpD1S0e7p9pEP7jjwlxy9XbWPk3ZVrIBzPUDOXygGAXeolyu7eIa_XJiQ1jFbhRRJ7utxGmIsSMntWLfl4mRBE67ptqzbyc7sxPvI6Uk41DyetWIuOsJj8_jJFbwajiQKKUuo51KlH0NcwQO-jp9ruaDMUiVuOVep0s00Hh0kW7_G367SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله هوایی آمریکا به ساختمان سازمان تنظیم مقررات و ارتباطات رادیویی در بندرعباس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/670942" target="_blank">📅 13:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670939">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAchlLvfjand9vxvgwZYkPWuwp_sLKEuoeUKXTyyX8qi0IH-_xQSEaF9whIFmnTwMv8dLx22hijjG0M1U_o3N2mWW45Hidb2rjzFI-Bq9_0R4UL3cZ0jh69cpijbCB5cIEqkx4Nl572McynoUy5igA4ofY1RkSQMmED_54LwO2m5btxr2hq7A1PZ5SSNLzVnrwLoJ9u0-TecBeoDCBwaJyQMNVaTH5ld9z8nkz1I38TmTvESNrh7CBNsoWfbZURqaqXJQmqcgkQUjahIMTPuWoTXzFP7jwg5mFulzADbrZr7EQ_Z8QFj_6zSQ1gGD6zImsYNL1D0dLRoVk2CgaSltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام رهبر انقلاب به کشورهای عربی بر روی موشک خیبرشکن آماده پرتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/670939" target="_blank">📅 13:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670938">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5fde6ff9.mp4?token=kyx9KeDExrmxY-2Z4f43TglS-xZcL763sKLsQNy98UYBecb5BAsFLed818gJALBhysGWqNz0Ufqtd0sbR02xy1kKqjbxM2bWDbF2hG3r_KxBEBu8V1umAED61MhZrObt2YtwpD-mm5oEZv5RxugTSRW_1A4RJFh7FwxO3EhUjzWk8Z0zTAQSz0T2ehPSq2ef1yksn876FqrU9puiBxIxnZHfJSTu-U9_kGkud8Q39Xyc1Uj5httSEfdJsK65PBQU84FolI7YWPcB8c_2K_svw7lBFQ8zfJqv7AXPK4BbjrpDUsMvyKdK8ITH5HsI3S33Ma-UQEHItRknENzG3K1iVohlzyFDi2_f-Ur7spnTOsiGZjGC6lcoc67qx2zAh57k-7Q-HGiAsiWj6lTtQeHsmh5vBWfsWQhlJmikEVEnpcvKn2kLKxBlsSQccCE7GH8C5yGQpFbwcl6_Yiw6R-zi29lj95e6mmWgUHO4-N5m8cjzALYN-0FsD_FUNQv5uGHxc7zPqEE5J9C-YDDLNaqUOKWwE7Om57qF0Czn1xQlyWL0eIUxTESuviQXpqf7jxJs7eur30n1PaA8mPabqy_1FCK6sv9DrMr-7i29ygrJJlcF9qH5NLdRLudyc6EOMmqCd3qzbUfh7gvZHEMD-wXThgVeZartsVuTf0-z7XuhfD0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fde6ff9.mp4?token=kyx9KeDExrmxY-2Z4f43TglS-xZcL763sKLsQNy98UYBecb5BAsFLed818gJALBhysGWqNz0Ufqtd0sbR02xy1kKqjbxM2bWDbF2hG3r_KxBEBu8V1umAED61MhZrObt2YtwpD-mm5oEZv5RxugTSRW_1A4RJFh7FwxO3EhUjzWk8Z0zTAQSz0T2ehPSq2ef1yksn876FqrU9puiBxIxnZHfJSTu-U9_kGkud8Q39Xyc1Uj5httSEfdJsK65PBQU84FolI7YWPcB8c_2K_svw7lBFQ8zfJqv7AXPK4BbjrpDUsMvyKdK8ITH5HsI3S33Ma-UQEHItRknENzG3K1iVohlzyFDi2_f-Ur7spnTOsiGZjGC6lcoc67qx2zAh57k-7Q-HGiAsiWj6lTtQeHsmh5vBWfsWQhlJmikEVEnpcvKn2kLKxBlsSQccCE7GH8C5yGQpFbwcl6_Yiw6R-zi29lj95e6mmWgUHO4-N5m8cjzALYN-0FsD_FUNQv5uGHxc7zPqEE5J9C-YDDLNaqUOKWwE7Om57qF0Czn1xQlyWL0eIUxTESuviQXpqf7jxJs7eur30n1PaA8mPabqy_1FCK6sv9DrMr-7i29ygrJJlcF9qH5NLdRLudyc6EOMmqCd3qzbUfh7gvZHEMD-wXThgVeZartsVuTf0-z7XuhfD0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین وضعیت پرونده «امیرتتلو» از زبان‌ یکی‌ از وکلایش
🔹
توبه موکلم از سوی دادگاه احراز شده و این موضوع می‌تواند در بررسی درخواست‌های مطرح‌شده مورد توجه قرار گیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/670938" target="_blank">📅 13:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670937">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
هشدار سازمان مالیاتی به بانک‌ها: املاک را نفروشید، سال بعد مالیاتش را می‌دهید
رئیس سازمان امور مالیاتی:
🔹
اگر تا پایان امسال املاک، مستغلات و سهام مازاد را واگذار نکنند باید سال آینده، مالیات عایدی املاک مازاد همه سال‌های گذشته را یکجا پرداخت کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/670937" target="_blank">📅 13:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670933">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qB6_sxk6yrK39ZL-aVvnc9GGsXajyCXXwWfbXeh8gT6JCDMfW8Hc3W1q-YbxMkDI1ENFKrxcLiOOPOLZdm9KQaZR66jF6iTTCng3mNmIcJZqwfRRBfE__qfu4OPi-ps87uzUfN0_SpY-CbgEdRhw86h-d2wE_R72vD8SkMzQafUOjwq_1dwSv1DYzqM7LOUB_Wg7LQwbbZnNaMFqIj4GAsLlcjDKRQ84FsjRR7Tk2kRcSXLQcGSjJtQnKhp3F9TK-mfC3nyXtRnnHppJOBs86jn0wY4xafeqcu0vPWKBqFg48IKmEPBp19ZZTeQBgcDOVWPhn3YJtVOlia_774aPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QGRsps6dJMcDx61TNVwPVTQBciZzhF0dg-1n6zDZq6PMK_qvbETCICDUc7ww6E-fYnungVrLDr5GrWysywCABvw74vUYVk97zda0Sv_--iOiOBboUm-foLhVyoUd-m-NipTONj7nuG7JoH95VrWOMA7oG76xWSTulW0H212Axr9wRYMBbjP2ZM59VCPv6t1uEo-7DnuSBqnCqcu-vJpEok_HVz7jmNfZhFaEmXESfp24IQy8PiX2GNjWAxiOrfMIvXwTcaVtR2Uv-jrWSkR5YpC_J4FodPeatUxNHRnkqRxWGyNUgXwfnvP-g2Zauc-uW4Tc-WEB_Qsz24VoQwlI2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BmkJSiAJGzD16xMsRbde072YuUEdudMalOQ1yxXiJcSsRWPQJM4Y5seJvnma5jkuttQNjdEXHEhv35giJaOh4fzp0C9Qg7ktIgA5eLPjzQ_atwa_zStb58LkwYWaPkO8p15gF_wfljpiyK4d2HPRnrJJS_lhtuszwy-2tt3Ojr9reEI720qI2FGrcCaGykXIip-aqUz3G6MgZshg8NjjTiGouS-GrtwkAAjpGrL-WxFUNxLT5s5Tb_3st6c7dBJpwwlaYiWcnDkOeIrqjvVWj9qiYC2Gfx_0xvD4qPenMygPgWt8QVpp91GdVoDEI_0p5dblJMh-sj9z5qmsyQ5XiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YksAwWrKESU_mY-TJAzmJSy8XLxvJGBiZaBKZ9yb3kkq0in4E1yEm9UaWU7YIRTt5sYlwdb47iGZjBgDvlHaKUabBk6JG1UUW7vktXlumu-dTRr4WytuIJjLx5OE9ge_gTo7ckYyB7u_sHna36526TTM58olJ2_XRAJrnfm5W5gjUZVc5hLpFAg5hhsPPUQ6EEiNK4OzcU8it0dWG1LgwEoLE0ug4bgJ16unkXh1TXscWQwqOtwoTdhKSJN_q71QkwGUUYfap15zaK5e47JV4JJxjJsppw2JDYzSe0TUZ9Ai2KX2HdPMPkBmA-FAlzJ7Ky2vqTrxwT6zp2V7YHrf6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
راهنمای تغذیه ۹ ماه بارداری
🔹
در هر ماه از دوره بارداری باید تغذیه به چه شکلی باشد؛ در این اسلایدها ببینید
@Tv_Fori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/670933" target="_blank">📅 13:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670932">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HwKC0uNIZOBZJGHEiG-eKELlxliJBF6yInjauS0rVt0brNCS2eBcHvvkO9sHOWhCqGu2eg7lSICXTJsmIBSDsvA92X2K-lMirIUYuDkznTFuLOGIbNEwm66Yvb48xHN_sffohHOrSuuBWp4x8P1j9ktOQ3Bs8YsUqtfdL4ud4r1CWk7n9I4ql5hqj_dk0jUdA13B7_FNe3sTGJc-TVvQKdHNoGvIBnMVSBBkWCVh4RniuyBDcd8dd-wC4KgL1Pt1sxzzMKQ_jQWyZWRibzze1Sa1YqzHXGMuJT1NlmSN8wKfvloJoZXRLF4_ftqrcvoVb7sjNoWIPv9fuk7nLlE16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تماشای «فراموشخانه» در تالار حافظ
🔹
اگر اهل تجربه‌های متفاوت در تئاتر هستید، «فراموشخانه» روی صحنه است. این نمایش، فرصتی است برای دیدن یک اثرِ دغدغه‌مند و زنده در تالار حافظ.
🔹
با استفاده از کد تخفیف sahab15 می‌توانید بلیت خود را با ۱۵٪ تخفیف تهیه کنید و به تماشای این نمایش بنشینید.
🔹
همراهی شما، انرژی اصلی گروه برای ادامه این مسیر است.
📍
مکان: تالار حافظ
🎫
تهیه بلیت از سایت تیوال
https://www.tiwall.com/p/faramooshkhaneh2</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/670932" target="_blank">📅 13:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670930">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
بغض تماشاگران خردسال برنامه محفل ستاره‌ها با مداحی احساسی برای رهبر شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/670930" target="_blank">📅 12:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670925">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
محاکمه مهندس ایرانی در آمریکا
رویترز:
🔹
یک مهندس ایرانی‌تبار به اتهام صادرات غیرقانونی فناوری با کاربرد بالقوه در پهپادهای نظامی به شرکتی در ایران که یکی از مشتریانش سپاه بوده، مجرم شناخته شد.
🔹
دادستان‌ها مهدی صادقی را به همراه یک تاجر ایرانی متهم کردند که سیستم ناوبری مورد استفاده در پهپادهای نظامی ایران را ساخته‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/670925" target="_blank">📅 12:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670915">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKyPzEMA8XAWZPJpxErIzqIcKFQCWeYt2wSfLj3_AWhs11WdVAwH5kOd2x2B3KporC9UsmyyYLMwH00JEaXN9nNrgveAPUuAeG71XdrD7Bm5W-5pvjOH2LdlV4hMqhE2vy4xfcFuATrZYr_zCzbDPGO-gWFZ_fKyPf49YO81L7PLFw94RySvxF_hVHRZQ0qJgO-yyaekz5syJGffdPer7U_vGnNa3OwVHq56iKGT4VXt16C-2Z_PkAhM5R8LpxAbqwgD2fCnzeDN3uYAyw5vVT_otZaeE3QTm7IJG9OieKfK8WsstKjpDjSqsvkWpleaIHqtWcmLfo0tvQFRR6IaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWHiTI0by8i4FvV6itajlGL0vvALVRxbfXtW24apoJUDboo1bc34qyPw-XorIeK8hW8R3xVzG72wCOIBuc4V5tc6rSsd4FyFzhShgN9_Cmauj_zm6ZrhGzpdYHS7rc4C-OH1wbFVLof72_H2UrcvynL9RnnC6V55V7GhS8WqLzO17gXEf8-5Xb8jhvgue0vb5gZsZaFymHpdquA9Cmvv9X9WQTTOyguR75xmdRvZtfw5gwtWzDNn0mTXa9v0xUKl1Mla9w1SdWoaBTnYLml4j9pkMez_S5BKRqIEiwBRp9WMT9mZZcCYv5D1rr9axieShQ03GChBOVvq0wq5-d-PtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0HXspN8FwExu5H_FhjsNpyl1tPjk2TQi374MgQBsnSDmAMqv20t4MIjUHZn4-y-4KwZc-wQ55e8USj9FS6D38MxmF25jxNyqk2zSYL7cbV9PIljyssagyKDZ-quZc7F4RVlJQZySo-cGOO3tXklGzB9gmEWrKEBwG1jQzsNtFZiGZlOKSYtOF8WwXliTU8yZLB91NWsK_rFX5QPg9tgjnXNXmozRYk3d2LCRTzIXGVRGPguxGiWZSAABsxycVYLi59TG2_IRkeNh05bZd0qMdmCn6IMJLEIfLf97shOI-415gmKzkuHe5cR0cUi4ueNH0Xv95dO9KcNlyfs0Lm6dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tkMil8wRfB15YSCZo7hGT9DjYbcJ6_94J_u4zvoX1BlD6mW1SPav6Tff6S4qKzmRW7sgtcxAgGQQUF0ec6L5fCX4g-1N0p3YpxWptpD1_YqGQhehg3mahUGdtTw6kDIZuoP-eX8zsMYEMFG4fqx2aazyYX7AR9Fp1IqQgtD5iCoFzSxQmLgTp0BJSvwlWOAB0fajTJ--x4H2It3vlKqDInl2dggF8W51Lzxi2hTBC8vXJZRZZekPzeetsFz7EJ_RXsz6DG4yYEGSjXJsKgK600R7HX2GD4aMnFlwtfgvWaCfPa5FYeSvrlqmC-BRqEXwtb0PGs2sNBHw5YP04HbxDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-ZeOhUQJu0HtEVZsJZvdYzTdCQWDKOHHJepwejB3AmkDDkcUiKD94Tt_AT2XVuvOboiXIjVZNJv-hINqqrz4Y3jLHGShU2l5oWwgkacWJahGH41jsuGvutfLeFwvgZx0SuyajkMH_qKPcB_6svfCfwN-TzkvQqB8FXXZjtCKhtLaG7C6WCXLuguFghh1eSn5nqyA-bgkAGKzruDIgOGK5ud35v_DyB7A1U5VnkRUV87vhER_VpehrCTsbZnFu43aNlciRYGFFWzVhz2l3OLC23IB8n1NGOdRWV4RPKxFxXclgauqVeHYvYtn8dpT19axXtQx_wjTlZXV6q0UVMvog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGCgP3_ASl10ZHo7lX-A5Ve3EHMiVnz2lpqWPW9LAyLtPnLZlpUGzUV0QkWht6sywjxBi1bJKKi_ns5DxX2HT9UWZumxg7DvknBxGh6YEOibrRNMBwegSyM1KsTX0mrCB3vzJAMPzBKudAhk9tnVs902NXAGDEl0vtebjXM3TQQfK3Y6VffOmuO4NYGHBPm8vxiacVt82AP2qvAjvbxvavfdokbSDfrZJ3fGyQGDO3QWPkXvUqV7O5SEKCasIpkZ9VAoJTY_0deZkb1G_JBvSJfAq5hnBcoBsk87Ra0uEPDdEHeC_bgcvNTXr-kuvHxb7ZkmNc2bpVO_YY6COes8Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OVZPyfnXAFua5eu2B8qK_4gfVuciYFbZ1icc8n7-R5StA39-Iy8YSrG9plNgkC4On5JP6qc9wZcBDWZgiQFjcQLQCr-YltLPWAlAlZnDwNZ2yFrp02savz7zSQsp_fQr8rl313CGZnr-AKuH3LtN9DmILV-oVnFwcPYN989OgxAG36tjROnvZFEJ1Y_RcwFEpoBiWHZNhaZJVJMvBfoApIk1cNEbgVGUSR_tFiZPRszIjUf3cAypD9RMGccXNU1zKv48IFFb1l7La-eSy7tsg8ab9dnuts2fJuA1mjXoTqsbfcUaD6kzE2_97sdQ-n3u6SUsOr-i_SW4u3vbRQv4fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WeRCfyZAW-eBFSCVP0I4RMCPyXRhkS_iyT-Fo_MA7XBxkQn1Iim-naEvSgW-YJHNFLFiQWaXMbRblBa5-EeL8IT2gXa8ZORRTqsv7oyQtuXbrzet6xglm-xKS0__kpvoVgafZyYiwhPqKY8WGGmp8Cs1yD90F4hwqe8T8e7Ujs9foOwVE0JXqXH-AeueZjFIGMdcPIrqnAp0Bc2JaVexht0LxiobwJvbUEO3vYvu8JMRv5viPFp_7qCELOQIyLQSXnCCNTpJLFtiSuXKMldLxjrrDr4rdojy_1BPFyYc5rmGfpLEHI2KuWNhi1JQaQfg0v9CYPX20TB07BBFOpoMRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bp5W9KeRYTwhPur2fi7w4es61TCRTHwuyk8ek2FYHAmGV-dfpjzcogE7QLppNNUhXkjKZFMenzcav9E2rVgcXcXRNRk0e9l4pQW5X9ALmx8nyyHuDKDavmbUDMupVJB-bxC05mlnoe-Hgx4A98V7g_GDE3PBYHvjOeHa3DXrac9nRciHGkTdjJtM7mdIW_EQpckmDQJiVoBPgIBwoyy1RbBlP9O1YpLiHsctDCjCZcG3E6mzOnw57im4i4pkrB8kD-dPWTV9toXrQwwXDg21_2qohNU7G-ccacaRJFs4S423A5xuT035660428q5czI-t9Cvz_oA4zc1xPOeDAaIyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xjb97J5xRyLfeHPhtA8AeWD-9quh1JQiHzqB2qzgU2FAeedCqdhIgCpxbxtG22ophnFRByR9EvwLHjVaHT9QzGhFwJtZbRlAG2f2qCC0uHa6ytsI-2alxzDoqZ6KqWbzqIBpM2-Y-y-PNM21lzzd2fGDqrudzX08SnL88Pe1dwUQSuJhL75XQgKtbPDZNzLBXX048zcGs4oaTLYJS3MhlN3V6hyE9yaD3rnE6qh02H6USqFND0N4WLHsEnySbFEV6tU7rQkScJSrx-OnFhi2ylEaqp1PHwz0OwS0tTWfsbyo-Cbcl0kDn-L_4XdhfLt-ty0m9jM8zSbd7aJ5Di4DNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از فاکس‌نیوز تا نیویورک‌‌پست و تایمز اسرائیل
‌
🔹
غوغای رسانه ای اَبَر پرده‌های تهیه و نصب شده توسط کارگروه فضا آرايی معاونت فرهنگی و اجتماعی شهرداری مشهد، در آئین بدرقه آقای شهید ایران، در رسانه های بین‌المللی دنیا/ایران رسانه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/670915" target="_blank">📅 12:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670892">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCAzlArCtKkcO2o-7dlq-t3h4OT-mIjD4fIb1JQHWHW96pW7BKpErfVkxRqjU7dbytYwEAua7wuhkUoLnbNrXcVrPIG8k8eMBXEh3ZLd8Pg5__AmSq8hjTYBUZc3G4kHop6V_3g0mnnRWq-28Pui9TQ1pTb9V2715-Sjl2DvGPGEauFNWk1UZT0E3_cPq2H4QMTXozONg8Dy0y7bVw3dX3ozwdpYIXS0flE0j1sPmIrN8ueyU88zXuJKnpb8INz83GxSPk-a8sSUl5Zx9t7B8_XTJD2Z1aTx64TEMPr5Atfor-EqsX0JG5gars4_8_0bKE5uiw0UTIQCDn-DpuFT6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زندگی ما به تصمیم‌های خرد هم گره خورده است
🔹
نیاز به کار عجیبی نیست، قوی‌تر کردن دست اقتصادمان از همین تغییرات ساده شروع می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/670892" target="_blank">📅 12:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670890">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2ae27004.mp4?token=Q3XTaiXtG-2cVy4m9JLbdGc9k-49r9OisFgVrVJMYep6nnBWJxRMbo1nf6WPcIYjy0MVqI7P7iEyUmzmJygPDZcRqe8cMqg40wGxz0L7bmr7YBOON5Nyf5UCdPROuiO5x_5jNDM8ljh9aDrXmYVOQJJL0ds4Mi_NzgH_ueFY5xBdEbhL96_b4NJREQXhqWt63C78deRXmXLSNgzfqCU5Azd_shfGGk14VGpo3LRK90u3O6oYsMS8x0DQX_8Fmzj5BV1ZPAKi1TbJwHs9GB7ny5HMU4xu9Ka3CORQOM9TiSz_4-sC2r7jDXvEyOJhbjWaNuq48UvfwrSFCQyyLxfQWyKn-kxDWBjNx0tBlTH7nH2FGRY7MxKk_vjXDumrH3zjRXEvhaFLxw8KkoeXIbXmbeJWDubBx2EvjzaVILu2MsKDEEDFivUxR_ZGUg3jGhSaZxYXKGAvEvMfEvmbn7b8Jug85Fri_1oEFwXr_ulBU7ZfGuelWOC6tDRQQBjbiLff9l5sf6PkipubPbO0-yaZB1Cbod9wlWfXOcuDA6IbFPO03jXoxqUqjdbl3zwL3xO8ZDKh4kcmbgVKXMp8o8Iz7BnMeisLylz-YSYVRqAdZ4lf5MEFLhY0xhDZBboYNslz4jCJZeofQG_sDlIfL2NlmOkcwb59qZpl3QMtCktwbRY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2ae27004.mp4?token=Q3XTaiXtG-2cVy4m9JLbdGc9k-49r9OisFgVrVJMYep6nnBWJxRMbo1nf6WPcIYjy0MVqI7P7iEyUmzmJygPDZcRqe8cMqg40wGxz0L7bmr7YBOON5Nyf5UCdPROuiO5x_5jNDM8ljh9aDrXmYVOQJJL0ds4Mi_NzgH_ueFY5xBdEbhL96_b4NJREQXhqWt63C78deRXmXLSNgzfqCU5Azd_shfGGk14VGpo3LRK90u3O6oYsMS8x0DQX_8Fmzj5BV1ZPAKi1TbJwHs9GB7ny5HMU4xu9Ka3CORQOM9TiSz_4-sC2r7jDXvEyOJhbjWaNuq48UvfwrSFCQyyLxfQWyKn-kxDWBjNx0tBlTH7nH2FGRY7MxKk_vjXDumrH3zjRXEvhaFLxw8KkoeXIbXmbeJWDubBx2EvjzaVILu2MsKDEEDFivUxR_ZGUg3jGhSaZxYXKGAvEvMfEvmbn7b8Jug85Fri_1oEFwXr_ulBU7ZfGuelWOC6tDRQQBjbiLff9l5sf6PkipubPbO0-yaZB1Cbod9wlWfXOcuDA6IbFPO03jXoxqUqjdbl3zwL3xO8ZDKh4kcmbgVKXMp8o8Iz7BnMeisLylz-YSYVRqAdZ4lf5MEFLhY0xhDZBboYNslz4jCJZeofQG_sDlIfL2NlmOkcwb59qZpl3QMtCktwbRY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجربه تاریخ؛ با تورم موجود کجا سرمایه‌گذاری کنیم؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/670890" target="_blank">📅 12:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670888">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqQZJXu9kq2sMmEuIgbxR9N4giIbg89tf6XUq8aWyuUBRY3ePPpHo3FLiar_KZ6q0rUD-o-D_Fle0p5yLA6orbjyD1wqwIitH9cziaunedOTgyVVSOVyp3FBkfu7G2Pw5fZSrtLNea9xtC0QtRvsWDK816H_SS94JcJdtmve-KspGjJLArKNbeRlLYpFAK6WrJLnd3mlzqc7moNGFzNoiH490rUihs3Z3XUF0OiGNtgywWN36A8G0SWBmQ1Yqwt9Hu4Vcuu8szWXzPvV4kG58Q3cpUdYGcVcfDL_tSKB4Je-3M3E3uYEiTcALhmPLfQLzxKlu1Zf109-w8OocXTxyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داریوش فرضیایی به سوگ مادر نشست
🔹
«داریوش فرضیایی» مجری و برنامه‌ساز شناخته‌شده تلویزیون که سال‌ها با نام «عمو پورنگ» در میان مخاطبان شناخته می‌شود، در غم از دست دادن مادر خود عزادار شد./تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/670888" target="_blank">📅 12:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670886">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUyXeOeJFZeQYr3s-B5Ku2uUkvXnZ1hkHDlAEmgEWIAVqrbZEmqxi_FoDaUNKFIHj02WtwAx8MykYmwLh7WY-Kp06h_Ggf86K04NMHJbzbZEIjPnphkYyx470284AR0uTFSUap5wyWeH1cVLT7nJzvQQgzEpPPD4Pqk57OBBwLBhX3OIOfw3qPObILqJM-gRnqr9Zo5FA1OINX0IcTbnh6klJrRAIOYe7kBeKKFhp2ob_X4fANZy1XpYj1ABeojHUDrDUZtEfn1SyWXM4y4bzTNafZIbOX7SCd-qW-Jd0-NGESKg_nHkyZi2y0hQR2r_q1c6npbxVDQSEwwE9xVIhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشانه‌های تروما‌های حل نشده چیه؟
#سلامت_روان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/670886" target="_blank">📅 12:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670885">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0R9Gl1BRXenMDy4kFBkTa2bhJYhDdoawMm5_R1XvQfhrC_xXE5iWCbkRkOGyLMOlGopQwOUKWqz9J9gPFir_RbIaxtynmLKBgcWgK4tKWCLciePFJ3h5OaBr1YseSqQRaaW4Dgb-VTtgQivvnQ1YlQm-SwUjv8Z-js7RVSdEV6y0IUc6XSkkxErH6_AXRw9MqfD7mRU9gFM59qoUaT-c-0XAmsEYSUzi8UDFFhr3mERu-2XZcpGFh-nRAciP02Lrv0Dn1geLGFSGA5mPlLapfomlsSCKV1Gwj3QT1xuSdqRsoXpj0zsGwDnagcqLqrqj7yHv0olg-IsaR2qAtJkiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خواهر لیندسی گراهام با حمایت رئیس جمهور فاسد آمریکا به عضویت سنای آمریکا درآمد
🔹
به دنبال حمایت رئیس جمهور فاسد آمریکا، فرماندار کارولینای جنوبی خواهر لیندسی گراهام را برای تصدی کرسی سنای آمریکا که پیش‌تر در اختیار برادر او بود، منصوب کرد./ایسنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/670885" target="_blank">📅 11:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670884">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
قسمت اول آموزش سلاح جنگی کلاشینکف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/670884" target="_blank">📅 11:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670878">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
گرانی دینار در بازار آزاد؛ اثر نرخ دولتی ارز اربعین
🔹
به‌دنبال تعیین نرخ رسمی ارز اربعین (هر هزار دینار حدود ۱۲۹ هزار تومان)، قیمت دینار در بازار آزاد با ۱۰ درصد افزایش به ۱۲۰ هزار تومان رسید.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/670878" target="_blank">📅 11:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670874">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
امارات: دو اوکراینی در حمله ایران زخمی شدند
ایندیپندنت کیف:
🔹
وزارت دفاع امارات مدعی شد که موشک‌های کروز ایران که به دو نفتکش اماراتی در تنگه هرمز حمله کردند منجر به کشته شدن یک خدمه و زخمی شدن هشت نفر، از جمله دو اوکراینی شد./ خبر فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/670874" target="_blank">📅 11:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670872">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
رئیس‌جمهور برزیل: اگر آمریکا بر کشتی‌های عبوری از تنگه هرمز مالیات وضع کند، مانند «دزدان دریایی» رفتار کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/670872" target="_blank">📅 11:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670871">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 نگاه شما به پلتفرم‌های جدید خرید اقساطی چیست؟</h4>
<ul>
<li>✓ راهکاری عالی برای مدیریت هزینه‌ها و خرید کالاهای ضروری است</li>
<li>✓ به دلیل سود پنهان یا کارمزدها، اقتصادی نیست و ترجیح نمی‌دهم</li>
<li>✓ باعث ایجاد بدهی‌های غیرضروری و مصرف‌گرایی می‌شود</li>
<li>✓ کارآمد است اما سقف اعتباری آن‌ها برای خریدهای مهم کم است</li>
</ul>
</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/670871" target="_blank">📅 11:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670868">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb05813815.mp4?token=KMvkd76jyn1mjLuvqn5Rgo0pdYaGlKjMTUrt27XVhYZjfU4jVKW9cZKDGKdPJy0eSLrR17QTxUpuikoNd3sitsbVEirP1BUqVU0ksfopOLLlUd_dxTfrzoPu8Q3SivJ3KttEePNWDOYeWIkmiAhQ2Kirh2B_Tifv-I3EcMegf4Nu1VYAuMYTO1xL7q09443vdMuf-K2CHjg09xX3u82VchR-WxX1fK4fk1Ujc4K4hLKbGERdgGiRJtSqsze8-YDO8wecXOYme8iNHis-cBAN0gv6tyArKhCL7EejvbtDSFN_BD0UDV5f2G53izdCX2saMuIaDoz-D4qo-xviKaLAVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb05813815.mp4?token=KMvkd76jyn1mjLuvqn5Rgo0pdYaGlKjMTUrt27XVhYZjfU4jVKW9cZKDGKdPJy0eSLrR17QTxUpuikoNd3sitsbVEirP1BUqVU0ksfopOLLlUd_dxTfrzoPu8Q3SivJ3KttEePNWDOYeWIkmiAhQ2Kirh2B_Tifv-I3EcMegf4Nu1VYAuMYTO1xL7q09443vdMuf-K2CHjg09xX3u82VchR-WxX1fK4fk1Ujc4K4hLKbGERdgGiRJtSqsze8-YDO8wecXOYme8iNHis-cBAN0gv6tyArKhCL7EejvbtDSFN_BD0UDV5f2G53izdCX2saMuIaDoz-D4qo-xviKaLAVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنک اویگور، فعال سیاسی آمریکایی: امیدوارم که هیچ‌کس هرگز ویدئوهایی را که از غزه، لبنان یا ایران منتشر می‌شود، نبیند
🔹
اگر مردم آنها را ببینند، خواهند فهمید که همه افراد در رسانه‌های ما گروهی دروغگو هستند که برای اسرائیل کار می‌کنند. این امید بزرگ آنهاست. اما این امید اکنون در حال از بین رفتن است، زیرا دیوارها فرو ریخته‌اند. افراد از جناح‌های چپ، راست و میانه سیاسی می‌گویند: «من چشم دارم. من آن مراسم تشییع را دیدم. می‌دانم مردم ایران در کدام سمت ایستاده‌اند. شما گروهی دروغگو هستید.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/670868" target="_blank">📅 10:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670863">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6d1aa412e.mp4?token=v6C9xLNugMS_NHEocbobJMgwDymnJ6LJB6SvJCwmWC1WwU-FFsshBXbv3cXw0xQNzmKBW9OjEUwnKskUuf7YXCrKAefJJR5pL0_sTbZwEFTVzI3A1HefxCTp553Qa8C662DWfGSsCYxIFEWduoIbAxxdEfnfsHghRJtHeteFjpL3XjUzvBHE5rUmEG2cv3fmgbZYxPEegM_40rzECoymAP52IGsPtg0MBWHZmj7MYOlN8Pye2BV-lR7ye2EKUB_6c4-wWB4elQDiEfOdY05k6IdvoGOx48M1QZDpR1y3tNyXbxX6pYDMG6qIaZ6c9xvUUDmOd4uLlN826jNWZDC0bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6d1aa412e.mp4?token=v6C9xLNugMS_NHEocbobJMgwDymnJ6LJB6SvJCwmWC1WwU-FFsshBXbv3cXw0xQNzmKBW9OjEUwnKskUuf7YXCrKAefJJR5pL0_sTbZwEFTVzI3A1HefxCTp553Qa8C662DWfGSsCYxIFEWduoIbAxxdEfnfsHghRJtHeteFjpL3XjUzvBHE5rUmEG2cv3fmgbZYxPEegM_40rzECoymAP52IGsPtg0MBWHZmj7MYOlN8Pye2BV-lR7ye2EKUB_6c4-wWB4elQDiEfOdY05k6IdvoGOx48M1QZDpR1y3tNyXbxX6pYDMG6qIaZ6c9xvUUDmOd4uLlN826jNWZDC0bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی ساده‌ترین چیزها بهترین خاطرات را می‌ساختند؛ از والپیپر ماهی تا CS کلاسیک
🥹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/670863" target="_blank">📅 10:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670862">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dw6J6f24KWyEeB50eCGm7gbOn-_f38Pm7XeXK6b8UV09F8NRHOpFrNinpPcsKQFOJz1ZBOKbJIOowMb_FXlFAA-eYtS5AIY2V0MrzakLQCxQM_oW7i91QU_47TEIuhi8GW5Op17jKnXbEd1nReKqnEkaIyZ8IfRydqVZpjeEPhpArL5Ta6Zko4w7VzdQYMKzJd27qRFD3j7oFMyz1tDNIve-JxJex4ChgLgBAeYdNRD9N4zlllCDJrTQ45F-z4yJELpPouseeOjDd0PfJYpeKv-9GQoeK1OhslriPi1Y09S83lpzToAkyM2RShXygsyKSE4IBg0WFI3q7Ta8mBG7vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ شهر از ۱۰ شهر گرم جهان در ایران؛ دهلران با ۵۲.۱ درجه سانتی‌گراد در صدر ایستاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/670862" target="_blank">📅 10:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670860">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae914f0128.mp4?token=rr8GEXKxnkKwNDpyS2RX38WF5i6e83qObfwtip_m59IhsLmdmU9tDFdBNBirRchxMiTpT_LVkAsRigPXwe4HyjKX9ZcB8yRJkHi6vf27vgL_j61mh8PZFDkPdBCehWek6BHBAH4qGn-qbHpoQ-evhIv92_19DKTH1lCdDFtF4qSfMbhexCfnFKs5zVn3CUH3WiRr5oV-Z1qMmMtB5J5nk7AIlEgB4jYznoe_0LIf6089bEodzs5hpJKJrySe3Pcdxy85EP1RnOZA3JeajqWMIkqaHdwnXxWLUbrHJM5hq42leyvoaavda2H7ttUKRjX6jmz_O3Am-9L6KfJncnOkZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae914f0128.mp4?token=rr8GEXKxnkKwNDpyS2RX38WF5i6e83qObfwtip_m59IhsLmdmU9tDFdBNBirRchxMiTpT_LVkAsRigPXwe4HyjKX9ZcB8yRJkHi6vf27vgL_j61mh8PZFDkPdBCehWek6BHBAH4qGn-qbHpoQ-evhIv92_19DKTH1lCdDFtF4qSfMbhexCfnFKs5zVn3CUH3WiRr5oV-Z1qMmMtB5J5nk7AIlEgB4jYznoe_0LIf6089bEodzs5hpJKJrySe3Pcdxy85EP1RnOZA3JeajqWMIkqaHdwnXxWLUbrHJM5hq42leyvoaavda2H7ttUKRjX6jmz_O3Am-9L6KfJncnOkZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش یامال به تصویر نوزادی‌اش در آغوش مسی: فکر می‌کنم کمی بزرگ شدم! لئو هم همینطور، امیدوارم در فینال جام‌جهانی با مسی روبرو شوم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/670860" target="_blank">📅 10:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670856">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGmy3-bxUs37GU-Rn0XhYOwdsds_rGWtT9u8vV7xLNwwTAQjtSrxuiGjxTM7RC6vPjXJxhW4HO0ZqiDuB4MJGbXKSKzxO8zWJRA6s--QJv4Z-Uj27PVcE9Tj-DOaAxUWl6w2NbzLza6DaQ-aoF0M09qFnWa9F9_9AThrRBsdu7Cp_3oRii-8odzIVfxioUgT2y_1TkmaExa2uS8bKwAitcYJa-MoOBe80TUTvMtxj0QmKUIurbE2eMHRtCaWMq25MG5Emih0Bb1i_vvH2sm0RxqyeqFsffbaVY7U7FghnUEDxwcZIt_OB-JbfU6rIneg0wDhbwLLa70VpJKd1AX20w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ نیمه‌نهایی اخیر جام جهانی در یک قاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/670856" target="_blank">📅 10:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670852">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYi4qXD3QXX29JhYBAMl4Dq4gDFstr45i-QKnBXm9yKfsZNy1aXxN614H7cRskYd0Y_iWmyOJMJ7tv_ntTlErZ-_9aDVBy8t4FNvA8hKQQUxJvco76S1GGcwHWiIdGMEir6VuruYZKyAbmWJUA1ZlNA2dcG2iHiFs20CTDMDt1n34-l2cn1P23Mehzm13_ZWQYT1lZEqWp_MO5adu9OAWwQue8BHHYlWA89Qo7qEoiK5cEW1bcG0QCvJSJKDcMW3x8DX2uZdKkYAvUcwJch6kgqKmkY_-K0Iwa-PLVl6YoDuRDoEzO0rK3FE_TXEJh7xGLoqgb85TySygnBjTA8BEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3CcW0_pqvrLxL6HK1frGib0EAo2xmdl1Fk9cm2eOd_5XxlsrooXRCYFDW81HlqvjA927n9ckhVgbhUFBapbK5nd2CzYRv6PK_EkfgxsPLgPdWOLt5FeAvtpVcWlVUhHZYdHNLpNAS6yAoThE3LhgH5lOOmXxgv4V3hQxJXbUKbRcrPHMtwRqXIklLSuideZbwHsP_26N9tqdoeRHxduCpEXbozcvIQjUeQwpq1WJYwmYBeqxC7a3ok7JAvtMPrb45GP2gFzhobLiTy6q-J8nGPrRi6aqx9s5ZeJawPhFvhyrIuB11aykwiVJtZBnL0Idqb1PbvsWkc3yXkODPQmuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LzfxjZyXlpvXWusLS_HURPk_Me4xbZFDFHiC5ns8TFngsWuGeBvBTAdov8Fc31Us796cnl6c8KcFwo-TurYsCNi7-Hw0aMDaFYGx_zC90SaWvQr4PDFkxRQDS_CkCqIOulzlVlxZaUfZqLD70FmubFz54YpKJ4UF2B9EeZ8tbIaxKHzO6GH7_c6As7m7k5mmSDe3e81jqtsBqhr3h3mdIjkennKjwwObAPF-ef11zw6F_jeaIg1g15oPy9AQBwNYrtIolpF0H0xu9Stt3k-ElYnKXVt6lORrIYKo1q709adi19SVMwvj3yxurrSAgqKsSDIzFK5Ot2LCBGBXym98tQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مرغ رو به این روش درست کن
😁
مواد لازم:
🔹
ران مرغ: ۴عدد
🔹
رب گوجه: ۲قاشق غذاخوری
🔹
فلفل دلمه ای: ۱عدد
🔹
پیاز: ۱ عدد #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/670852" target="_blank">📅 10:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670851">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDNdQMHefcEX4P5wss5rXyAPEWbzIdpsvIC27GZ-1glmNAwW_3MC5coatZoHy_Fzpcz65P9KoV1vaonjUGsdigWNN7TDnjyeOvoAmKU7W7XgsXrb1OYBKITWbxL6L13CCPd6HWNP1HBGZVQRBge7BkdEg1Cr6VgKj-htbYCm1_QimlTDI8VUDUFdD-Quk4HXDqOjy_hXBUHoWghF_ZezM5ETUPiGXefWwrm4iBpPbRT5sor1OoK4ifART8di3irabh8rMNXrM4l5Bw2kJ-l9SKWEMADNBxO0cWziT6IH21QBtwSv0Jua9Qn8UGkOCp2-fycIM4j9YJc2Z7qMxvuNew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چطور باید به توییت‌ها و اظهارات تند ترامپ پاسخ داد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/670851" target="_blank">📅 09:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670850">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌
♦️
جزئیات حملهٔ دیشب آمریکا به بوشهر و چغادک
فرماندار بوشهر:
🔹
در ادامهٔ نقض تفاهم از سوی دشمن آمریکایی، دیشب در ۳ نوبت، ۲ نقطه در این شهرستان هدف حمله قرار گرفت؛ براساس ارزیابی‌های اولیه، این حوادث تاکنون هیچ‌گونه آسیب جانی یا مجروحی نداشته است.
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/670850" target="_blank">📅 09:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670849">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/habPmGo8xTK_WR5xhBWYCZ5gIl_JnWl59WcZpeiRMkOhoHKHWvDKpysThTwh_DsQ3FMKPuLyUaYKcm1U7Y3c-9_PiMEFvYrvJOg1F12P6pjuteUZsSPbMZxGu17h1EDWVdRDNXR5GQLamwoVUn57q8kqakPjv41vnePWeTJanJorO--TqPn_BXwni8z5r9IM9fiJlwcZh1DW6iYslHrgPazS03EsDHq5tyS8FqsPMAJMVeOW6BEv9Q4YXmbj73eibW3bDaGteLTFYq6PM1YPhM5sptnr_yierhMJxOpQCWCj0M32WWa2baOKbslN0asILFy_c2j9I1J22c--71ODyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیرعامل سایپا: مجوز افزایش قیمت نگرفته‌ایم
🔹
در صورت صدور مجوز افزایش قیمت، موضوع از طریق سامانه کدال به اطلاع خواهد رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/670849" target="_blank">📅 09:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670842">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d31aa2ae1.mp4?token=lg3KirunHL3ZHIs03MA4dOs0qvy19xW1O8i5awO3f1D2UCVwW5suOn3i1XbRN9KsequHhc1ytger2SaW4agpkJvwKZuxRf_D_HZ3fQVFA8TOO5PG1_8EVBdcjfHDy-bP39xRKE3-ZbZS1hHpwKh7gc_TuCdy__C8DStD_yvLRkT6KAypHHwFLrP02wrArPsRx0De9Naz_su9e1MCkkno_90EfMNLsD7IbORKScVrAPn7cUXLU_ARJ7MGSuIOpYps_sg5ir5iQ-_mCxPS8c_LuwEvAFZFOPLJFIbSO0HpETmhqL1eY41IZcRVtqOuNlPwmTJgZ6_aNF90RRQzp8ePxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d31aa2ae1.mp4?token=lg3KirunHL3ZHIs03MA4dOs0qvy19xW1O8i5awO3f1D2UCVwW5suOn3i1XbRN9KsequHhc1ytger2SaW4agpkJvwKZuxRf_D_HZ3fQVFA8TOO5PG1_8EVBdcjfHDy-bP39xRKE3-ZbZS1hHpwKh7gc_TuCdy__C8DStD_yvLRkT6KAypHHwFLrP02wrArPsRx0De9Naz_su9e1MCkkno_90EfMNLsD7IbORKScVrAPn7cUXLU_ARJ7MGSuIOpYps_sg5ir5iQ-_mCxPS8c_LuwEvAFZFOPLJFIbSO0HpETmhqL1eY41IZcRVtqOuNlPwmTJgZ6_aNF90RRQzp8ePxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنایه تند محمدعلی ابطحی به مدیران عالی کشور!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/670842" target="_blank">📅 09:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670841">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1XT9U7DMIZlq5Apk6ItVXrUS8fxqAaXu8p_UWv4_7GEfVJPnHnAGCmIS_0GyU8MLZfqvcFDaSs87wjQsDbA-_v-uGQBHP7NVHLobB7fKEU1hUFf4gFXRfnbEQTo4seH3F6yXktqbW4emfH-d2wIDWOSe0_FSyVLlQzzxW30XZxl62lIOFFcJNcPEUsNLrVEm25s7GUIgbY2NyI81R4C3rH7ykKYLCv4qBiqF1wn1NI5mWUzUfhOZOf8e9tKJAbEEGP4NH5fxfwuuS9WMQpV27LsQ-jgIKJ2MTU2AYGcl9rCMZDtKe3mNyz-Z1O2L66cfpr6lAuwPIjxjh4sHNm8SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاتز: تماشای ویرانی غزه، حس خوبی دارد
🔹
وزیر جنگ رژیم صهیونیستی در جریان بازدید از شمال نوار غزه، با افتخار درباره ویرانی‌های به بار آمده با جنایات این رژیم صحبت کرد و آن را «نتیجه سیاستی حساب‌شده» خواند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/670841" target="_blank">📅 09:07 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
