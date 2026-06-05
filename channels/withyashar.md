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
<img src="https://cdn4.telesco.pe/file/p3vWM1xK7feOaqLbHVAzHegouR5ECJzbnjlpbFbuaYsOusk_oRrLiYUxXju_4Picg_KzHbUtLaLztJ3f4ecdwsxYzVHhVXdwj2w9RSYIGvZc0Gj_l-JJppKWHOvlWzTatzchZZ03Twi4uGikmqj8Go-zkRFr09F4FyljjX-D2h881hjlOgjOOZ6lExzoq04pghcGu6EaWifYXR1fAbU-iTJmsk15KKksncSYMUSFq2WYpsBVrI-2vq905xrN14ZziKZypvosKvC8f6MpETHZYO59JzDjeADgXAiWfCYzQ3uehdPXCE8mzzvYJG3rEYGyNJd2rzi01ofxZRXpTbkxRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 289K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 15:12:48</div>
<hr>

<div class="tg-post" id="msg-13546">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">العربیه: ایران بطور رسمی به پاکستان ابلاغ کرده که با انتقال بخشی از ذخایر اورانیوم خودش به یک کشور ثالث مورد توافق طرفین، موافقه. @withyashar</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/withyashar/13546" target="_blank">📅 15:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13545">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فیفا: نقص سایت باعث صدور بلیت‌های رایگان شد
‏فیفا تأیید کرد که نقصی در وب‌سایتش باعث شد ده‌ها هوادار بلیت‌های رایگان جام جهانی دریافت کنند!
@withyashar</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/withyashar/13545" target="_blank">📅 14:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13544">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">العربیه: ایران بطور رسمی به پاکستان ابلاغ کرده که با انتقال بخشی از ذخایر اورانیوم خودش به یک کشور ثالث مورد توافق طرفین، موافقه.
@withyashar</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/withyashar/13544" target="_blank">📅 13:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13543">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سی‌ان‌ان: اسرائیل پرسنل نظامی و اطلاعاتی خود را به‌صورت پنهانی در طول درگیری با ایران به جمهوری آذربایجان اعزام کرده
@withyashar</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/withyashar/13543" target="_blank">📅 12:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13542">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سازمان ملل از حزب‌الله خواست به تصمیمات حاکمیتی دولت مرکزی بیروت پایبند باشد، به حاکمیت کشور احترام بگذارد و روند انحصار سلاح در دست دولت را بپذیرد و از اسرائیل نیز متقابلاً خواست نیروهای نظامی خود را به طور کامل از خاک لبنان خارج کرده و به حاکمیت این کشور احترام بگذارد.
@withyashar</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/withyashar/13542" target="_blank">📅 10:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13541">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c45ee52c.mp4?token=gBQCSJ1MlsKyUm9Fmt_xt1cqwLgxJ7HjdloJeRC5nXwPpCamKh46hA7jJ40k9B5J4YdlQRDaB6il_LDf6DA2P5geWkHLJp_0RgRD0jEZhj99mh6NFAyRuvTicc8O-eeef8k0wKdjOAtq0bEdYADlfx4o2xOFfI2Yzdsrbtb6G7Ye9LQh4T9ojDeM7ep48wpPM6iMrXU8OdUGkGrrtJwYBuXhAFwURa4RoPSmp6W0mngf4_HWgKcdFxaSCGaRNWVA5H3g7ZrADlVT9gpcHaun1lY2QW-sEuC-L71SEDKGQiI-H58FV5rnt5Tqd_vG7AxcQ4C-wB4tTHivQsHKY_b1Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c45ee52c.mp4?token=gBQCSJ1MlsKyUm9Fmt_xt1cqwLgxJ7HjdloJeRC5nXwPpCamKh46hA7jJ40k9B5J4YdlQRDaB6il_LDf6DA2P5geWkHLJp_0RgRD0jEZhj99mh6NFAyRuvTicc8O-eeef8k0wKdjOAtq0bEdYADlfx4o2xOFfI2Yzdsrbtb6G7Ye9LQh4T9ojDeM7ep48wpPM6iMrXU8OdUGkGrrtJwYBuXhAFwURa4RoPSmp6W0mngf4_HWgKcdFxaSCGaRNWVA5H3g7ZrADlVT9gpcHaun1lY2QW-sEuC-L71SEDKGQiI-H58FV5rnt5Tqd_vG7AxcQ4C-wB4tTHivQsHKY_b1Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو اصابت یک پهپاد به تاسیسات بندر الفحل عمان که موجب توقف بارگیری نفت در این بندر شده است
@withyashar</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/13541" target="_blank">📅 10:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13540">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یدیعوت آحارونوت: کابینه امنیتی اسرائیل شب گذشته به قطعنامه آتش بس در لبنان رای نداد
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/13540" target="_blank">📅 09:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13539">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">طبق روال هر روز صبح حمله سنگین اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/13539" target="_blank">📅 09:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13538">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HL00r_x6xF_ubztutT7lNj5gMEknldpN9ykUQzd0dFmpAOJ7haN-FZqcXY-uFBJLrhJXwC59CLxGNrxu3At6R4qmXoh_tsfPbxKC01pFEOdW2uYwLdVJlTNRhEGVSiuYVb9xi6Qvd_aBXic7GBTtMmFd85PtLk0kkZDUruS3QODRMcmT47Gi7nVWiWMu8RhWwTNXiI2dOA3BTzz_AvQE56GfSF1fmy7un58bltKrb0vNpinHF2lXk01mWBT-I2Az0gK_y1_8H6Y-CeEvxcXjbcowNxTydVzx4uEBpbYq45L7IAqT5zguZ7r8QzZRvpaVS-_-sOps7KAolj7TPbcJwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارشهای زیادی برایم فرستادید که از پدافند سنگین ۳-۴ صبح و چندین انفجار در تهران ولی مدرکی نیست… فقط چندین عکس از اینجا برایم آمده.
آزاد راه پردیس به تهران
@withyashar</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/withyashar/13538" target="_blank">📅 09:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13537">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">امشب بیداریم ، ردبولم میزنیم
🤣
💥</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/13537" target="_blank">📅 09:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13536">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رویترز: بامداد جمعه انفجاری پهپادی در بندر الفحل عمان رخ داد.
@withyashar</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/13536" target="_blank">📅 08:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13535">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نورالدین الدغیر خبرنگار الجزیره در تهران:یادداشت تفاهم در مرحله نهایی خود قرار دارد
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/13535" target="_blank">📅 08:44 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13534">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fcaccf1cd.mp4?token=Ode9Qj1oCrfcDMfwoePAk2sJClCrQw_Tg-TEXMWNiRAdTip_3IyN27I6K6XUJWD0_uYgZjcoKzfjzpw-bzlJN6e_KRUVtOdGqNVjl-AxAV-Bn8-IwGi0GeYURmFyYJ-IMDGnRATE9CiNN7KZkr8QOZ1zazQuHfr0ASMNHO38Ib4l8INb6rVrVW5OOOs4yHKNK-G_N8dRvUJWPl33pnEg-2_cyxDc9D8I1wUgbp5QCaD9ZQ0KniXAzq8JXGqlvk7KSgh5w6Za9mPvAs7KEbyQ7DIg9qzmObMao4BtbXSrZbP-tR9UbYGsglytY8A0-3MLaelFGHZoaM0a6lBr1bMNAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fcaccf1cd.mp4?token=Ode9Qj1oCrfcDMfwoePAk2sJClCrQw_Tg-TEXMWNiRAdTip_3IyN27I6K6XUJWD0_uYgZjcoKzfjzpw-bzlJN6e_KRUVtOdGqNVjl-AxAV-Bn8-IwGi0GeYURmFyYJ-IMDGnRATE9CiNN7KZkr8QOZ1zazQuHfr0ASMNHO38Ib4l8INb6rVrVW5OOOs4yHKNK-G_N8dRvUJWPl33pnEg-2_cyxDc9D8I1wUgbp5QCaD9ZQ0KniXAzq8JXGqlvk7KSgh5w6Za9mPvAs7KEbyQ7DIg9qzmObMao4BtbXSrZbP-tR9UbYGsglytY8A0-3MLaelFGHZoaM0a6lBr1bMNAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر اختصاصی جدید CNN خسارت ناشی از آتش‌سوزی در ناو هواپیمابر USS Gerald R. Ford (CVN-78) را نشان می‌دهد؛ آتش‌سوزی‌ای که در بخش لباسشویی کشتی رخ داده و در زمان استقرار آن در دریای سرخ و در چارچوب عملیات آمریکا علیه ایران گزارش شده است.
این حادثه در ماه مارس حین جنگ با ایران  رخ داد و نیروی دریایی آمریکا فوری اعلام کردن آتش «مهار شده»، دو ملوان با جراحات غیرمرگبار درمان شده‌اند و ناو همچنان «کاملاً عملیاتی» است.
اما ویدیوی جدید CNN نشان می‌دهد خسارت بسیار شدیدتر از گزارش اولیه بوده است و منابع به CNN گفته‌اند سامانه اطفای حریق ناو از کار افتاده بود.
یکی از ملوانان گفته است خدمه حدود ۳۰ ساعت به‌صورت دستی با آتش مقابله کرده‌اند و حتی نگرانی درباره احتمال از دست رفتن ناو وجود داشته است.
مقامات تأیید کرده‌اند این آتش‌سوزی به‌طور موقت عملیات را مختل کرده، پرواز جنگنده‌ها را دو روز به تأخیر انداخته و باعث شده ناو برای تعمیرات اضطراری در یونان پهلو بگیرد
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/13534" target="_blank">📅 01:55 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13533">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ می‌گوید دولتش بررسی کرده بود که نیروهایی را برای تصرف اورانیوم ایران بفرستد، اما در نهایت این ایده را رد کرد چون خیلی پرخطر بود و می‌توانست به تلفات آمریکایی‌ها منجر شود، و این موضوع را با مأموریت ناموفق نجات گروگان‌های کارتر مقایسه کرد.
@withyashar</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/13533" target="_blank">📅 01:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13532">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ ۲۵ بهمن ۱۴۰۴: میخوام با آیت الله علی خامنه ای دیدار کنم.
۹ اسفند بخارش‌ کرد.
ترامپ ۱۴ خرداد ۱۴۰۵: میخوام با آیت الله مجتبی خامنه ای دیدار کنم.
چه تاریخی بخار میشه؟!
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/13532" target="_blank">📅 00:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13531">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ: ما به ایران رسیدگی خواهیم کرد، و به‌محض اینکه کارمان با آن تمام شد، در مسیر بازگشت، برای مدت کوتاهی توقف می‌کنیم و به کوبا رسیدگی خواهیم کرد… باید از شر این نظام خلاص شویم
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/13531" target="_blank">📅 00:18 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13530">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ: برنده این جنگ ما هستیم حالا چه روی کاغذ چه با قدرت نظامی
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/13530" target="_blank">📅 00:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13529">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ: جابجایی مواد هسته‌ای ایران مستلزم حضور یک یا دو هفته‌ای در منطقه درگیری بود، بنابراین ما این کار را انجام ندادیم
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/13529" target="_blank">📅 00:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13528">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ : من دنبال عملیات مخفی برای گرفتن اورانیوم ایران نیستم اون اورانیوم عملاً دفن شده و از بین رفته
اعزام نیروهای نظامی برای تصاحب ذخایر اورانیوم ایران؟ نه من نمی‌خوام جیمی کارتر باشم
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/13528" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13527">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ:
راستش نمی‌خوام با آیت‌الله دیدار کنم، ولی اگه ببینمش، برام افتخاره. با احترام هم باهاش رفتار می‌کنم.
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/13527" target="_blank">📅 00:02 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13526">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSiamak</strong></div>
<div class="tg-text">عمو یاشار اتاق جنگ نمیری امشب؟</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/13526" target="_blank">📅 23:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13525">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ:
من در امور امنیت ملی خیلی تجربه زیادی نداشتم، اما فکر می‌کنم واقعاً کار خیلی خوبی در این زمینه انجام داده‌ام.
@withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/13525" target="_blank">📅 23:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13524">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">منابع عربی:ظاهرا چراغ سبز برای بمباران حومه شهر بیروت گرفته شده است
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/13524" target="_blank">📅 23:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13523">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">من از ۶ سال پیش استوری کردم، به دوستای نزدیک و بچه‌های پیجم گفتم! از اتاق جنگم ۴-۵ بار گفتم، بازم میگم ما تا آخر ۲۰۲۸ تو جنگیم و درگیریم! حالا بقیشو من روحیه میدم تا بکشین تا تهش
🙌🏾
پس دیگه تکرار نمی‌کنم، هر کاری می‌کنید توشه راه رو داشته باشید. حتی فردا صبح هم اینا برن، طول می‌کشه. این زندگی واقعی هست و رؤیا و خیال‌بافی و وعده‌وعید نیست! حتی مانوک هم گفت بعد از مذاکرات تازه بازی شروع میشه، پس ما اولش هم نیستیم.
ولی با من این مسیر رو راحت‌تر از تمام حالات طی می‌کنید
❤️‍🩹
🙌🏾
ما بقی بازی سیاست و خبرگزاری‌ها و مارکت هست که ما هم به ناچار توشیم و انتشار می‌دیم! ولی این اخبار به هیچ وجه نه حرفه منه، نه کلاً تأیید می‌کنم؛ چاره‌ای هم نیست، این مسیر باید طی بشه!
از توجه شما به این مطلب ممنونم.
دوستدار شما یاشار</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/13523" target="_blank">📅 23:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13522">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فقط‌منننن خیلی‌رک میگم عمو ترامپ ۴۰ تا ملغ میزنه اخرم نمیگه
😁</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/13522" target="_blank">📅 23:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13521">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ: شما اجازه ندارید کلمه زغال را بگویید مگر اینکه قبل از آن کلمات زیبا و پاک آمده باشد @withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/13521" target="_blank">📅 23:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13520">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4113f62c.mp4?token=qYYK2z6XnP_FHBl0ok0_y4cn9U2OgIZb408zju6anDlUnwwy10C8cHJ-hpqjAxlkigxqhU24izp6yOwysVyhDVnOxTWzMY8XRrFaYAEDeV8Lk7QIZIGmiZfXzoTSuff7BGXOYVs4AMVbkfehoZIF8XvizDr3G8EBKkt6cqYfD5JD21mHqCJj_nltt1TExeKEAWNmFQx_Fg2_ZVGpGZuQ-BsbNJrJWS_XGSw-YzDZ-oP6ZWxYe1xPF5EDpht5QjScX1CSHutnUjYrRjTpLuiBvr-PFnyc_z6l7z1hxgQQIAmvsYuHqbqJ6zq-bEk7DiaaQKydMDHA2Wykxx8sGCUBMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4113f62c.mp4?token=qYYK2z6XnP_FHBl0ok0_y4cn9U2OgIZb408zju6anDlUnwwy10C8cHJ-hpqjAxlkigxqhU24izp6yOwysVyhDVnOxTWzMY8XRrFaYAEDeV8Lk7QIZIGmiZfXzoTSuff7BGXOYVs4AMVbkfehoZIF8XvizDr3G8EBKkt6cqYfD5JD21mHqCJj_nltt1TExeKEAWNmFQx_Fg2_ZVGpGZuQ-BsbNJrJWS_XGSw-YzDZ-oP6ZWxYe1xPF5EDpht5QjScX1CSHutnUjYrRjTpLuiBvr-PFnyc_z6l7z1hxgQQIAmvsYuHqbqJ6zq-bEk7DiaaQKydMDHA2Wykxx8sGCUBMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: شما اجازه ندارید کلمه زغال را بگویید مگر اینکه قبل از آن کلمات زیبا و پاک آمده باشد
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/13520" target="_blank">📅 23:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13519">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ببخشید درود و ادب خسته نباشی</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/13519" target="_blank">📅 23:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13518">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM H</strong></div>
<div class="tg-text">ببخشید درود و ادب خسته نباشی</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/13518" target="_blank">📅 23:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13517">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM H</strong></div>
<div class="tg-text">پدافند سمت وزارت کشور فعال شد الان</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/13517" target="_blank">📅 23:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13516">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">منظورشان 3روز دیگست یا 10 روز</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/13516" target="_blank">📅 23:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13515">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAMIR</strong></div>
<div class="tg-text">منظورشان 3روز دیگست یا 10 روز</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/13515" target="_blank">📅 23:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13514">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کانال 12 اسرائیل:
مذاکرات به نتیجه نرسید، آمریکا تا آخر هفته پاسخ میخواهد و با ایران اعلام کرده یا توافق می‌کند و یا درگیری از سر گرفته می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/13514" target="_blank">📅 22:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13513">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXtOoFEIlw75hucdyyiEm6kGI19CVUYKWOrL2S5SLROItKQqB4G2X9yfSDbRBSNNVk4bHTt_T3rhwAXmOmq4BsmmqkmzpIQ_aGZ4GPZwRCCawssAdUkkyWOCc__8w84T1q1a5sw2AnAImCY1iM77nVaE_zAu3zdBNTcG7bbb6UyhVc4srpnTUcDxH13-VHsoMwOGqkQxtAd3mzDmNKutk5oCfSHM4KapNfsJ2cX4poHD5l10DXG2G-C61VFMTB479lJG0CmYr9_t4kcCYPtrqqIST3Y4R7rd0tr2fIhThiNB5FOMQ8SJ4-1uBgAnTRpYq88WPL7zkIfznn20R4Y9OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه ایالات متحده هشدار امنیتی برای تمام کشورهای خاورمیانه صادر کرد
دلیل این هشدار محتمل بودن درگیری اعلام شده و از همه شهروندان آمریکایی خواسته شده که نزدیک‌ترین پناهگاه را پیدا کنند
@withyashar</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/13513" target="_blank">📅 22:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13512">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBYCDYzUqszgmFF9qw0WiIZeq0QSwMgDCViq5m53ntyoiR2OXZBw81jg6Cl5392NZDYVzU8vt2Dg6_uENbr7UjB2ipyPyvbQ4m2QNSHq3dG8Lrdqx09Lpw9M7ZeRncFo84dYHrzCLD2tj6TfpVBPCg1Tnax3Qjir9MOka9AG7O3bl3SErnXHdyIp0iV67RVe7tAKL4YvBdWtugA-dsZ9LlWNYp38Hu6LS9udKUKBU-y6ehc_7-3SPfdMCxyhXULR9mjhHul6Shl5sdLYFgh4y658KnZaR-fzZYt1HU5s-yErcwfzlfGy96cA-iHcPdN8fZrdgpYB-bmnZWTCpucVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زرشکیان و دخترش کشمش
🥴
@withyashar</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/withyashar/13512" target="_blank">📅 22:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13511">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">عراقچی: ایران و عمان مدیریت تنگهٔ هرمز را براساس معیارهای حقوق بین‌الملل تنظیم خواهند کرد
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/13511" target="_blank">📅 22:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13510">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سفارت ایالات متحده در اورشلیم هشدار عدم سفر جدیدی برای اسرائیل منتشر می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/13510" target="_blank">📅 22:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13509">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سی‌ان‌ان: ایران می‌گوید در تنگه هرمز هزینه خدمات دریافت خواهد کرد، نه عوارض
ایران می‌گوید به دنبال دریافت هزینه خدمات برای کشتی‌هایی است که از تنگه هرمز عبور می‌کنند، در ازای تضمین امنیت کشتی‌ها، به جای عوارض ترانزیت.
این کشور به دنبال جبران خسارت برای خدماتی است که در کنار عمان انجام می‌دهد، از جمله کمک‌های ناوبری، جست‌وجو و نجات، خدمات امنیتی و ایمنی و خدمات پاکسازی محیط زیست در صورت آلودگی.
@withyashar</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/13509" target="_blank">📅 21:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13508">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ادعای رویترز بر اساس داده‌های حمل و نقل: صادرات نفت ایران به پایین‌ترین سطح خود در حداقل ۶ سال گذشته رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/13508" target="_blank">📅 21:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13507">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کانال ۱۲ اسرائیل: واشنگتن به تهران گفته مراسم امضای توافق با آنها در سوئیس برگزار خواهد شد!
@withyashar</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/13507" target="_blank">📅 21:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13506">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQzGecdJbhMC-BwdwqrUay42iamrM0YzRIV7O7anEKBR85s-_QyKt--Uhe5c-qm-KVNSx6_xmQqUEDfCIJrg_w5ukWsinnm9GabQuLDWkq06JOpZIqU0gXF4MR75DeaboIr5Qf_1MkgIFTFpazl_jNiBQ-dgEG8C9165UZ65B2fRvYuymSje4ISP1DrQw0AMk61Wos22ds8wJ7gPiVTnGpojkdo-9iHkZfPUDJgmE2D4EH8qgab_926TChLcCvh41od9tHLHkEjw3Gw7M7wGy_aOhDQzf91CmlCe3z7u9Fc4Pfe33OLZtbV74BoQT_IAcl3aKC9T-7RiOowFS2zoLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل :
اعضای ارشد امنیت حماس را ب درک واصل کردیم
این اعضا وظیفه شون حفظ امنیت سران حماس بود ولی خودشون حتی نتونستن امنیت خودشونو تامین کنن
@withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/13506" target="_blank">📅 21:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13505">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خوانندگی قیصر برای کودکان میناب در میدان امام حسین
@withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/13505" target="_blank">📅 20:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13504">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twUhrCpnoFrSjceIt2YVxmve4wWMIeuTIbFoVKbD5s5qSAnOXjLyULeRjH0Ri7fPGQJ2Dhq5PF9mZZFVn-XbOFu61VVmun4rGYxxVE_AltEiUlO3z3onelTo8TJRAkUlSj84AunDuFAY66njvAY0McPMTSPU8qJMdNyj8hH41GF0pJIVUH9cJ2n_v__HJlXY_ZvpoHYe_vMikt0x4eGvfhLlNZ7u5Ti8mbbsfCy0ugK-RWiqpjXmiPjjOQUBoPHA6HCK5GG4FNexUbhqD3fHSpGYe0rQlOmr4gYNucjPm-fAEx7ZpOilcwswAt-S1JjWstBSGdTBLy9_e6gqE2aPyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها سردار سپاهی که امروز تو مراسم سالمرگ خمینی حضور داشته:
محسن رضایی
@withyashar
🥴</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/13504" target="_blank">📅 20:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13503">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">@withyashar
قیصر</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/13503" target="_blank">📅 20:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13502">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efc791eac1.mp4?token=G1g6g5YzJl4I0Aw3v-xdeg7BZ7xvs7d0-VlLX0W74DDhpcx9OXL6HMVt_bPlkhvXpo1hqbAT0elHMWx_omNjzDqlT1GtnMMbPP7o9W9xYxe1f_kC1veeklozPG1BVRuN0868iTdsorauKGkD4eRDBFDDdfcbduY0aKJ_lV0i53vVWK-5NvsOt9xsTkqK9lrPNRUFf4yxISvxrMggGv6FlddgrW0AJLUacef_CxH0pn0EwG6mlirXY08oZwRg8g833lE2VWDDfTAPqFlXJzb1Wl5ja-QqLun5QyXwk9zDZJSkvvhTrjNrVFR-gMDKDEbX1-Qe0d5bWm4r7Po7XXAGBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efc791eac1.mp4?token=G1g6g5YzJl4I0Aw3v-xdeg7BZ7xvs7d0-VlLX0W74DDhpcx9OXL6HMVt_bPlkhvXpo1hqbAT0elHMWx_omNjzDqlT1GtnMMbPP7o9W9xYxe1f_kC1veeklozPG1BVRuN0868iTdsorauKGkD4eRDBFDDdfcbduY0aKJ_lV0i53vVWK-5NvsOt9xsTkqK9lrPNRUFf4yxISvxrMggGv6FlddgrW0AJLUacef_CxH0pn0EwG6mlirXY08oZwRg8g833lE2VWDDfTAPqFlXJzb1Wl5ja-QqLun5QyXwk9zDZJSkvvhTrjNrVFR-gMDKDEbX1-Qe0d5bWm4r7Po7XXAGBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حظور قیصر خواننده
لس آنجلسی در جشن غدیر
🥴
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/13502" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13501">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/withyashar/13501" target="_blank">📅 19:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13500">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">داداش این خاننده دوزاری لس انجلسی که اوردن ایران پشت پردشو تو باید بدونی دستت تو موزیکه
پتشو بریز بیرون این عرزشیا عر عر نکنن</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/13500" target="_blank">📅 19:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13499">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرنگار بین المللی امور خاورمیانه:
من کاملاً مطمئنم که اسرائیل در مقطعی به بیروت حمله خواهد کرد،
زودتر از آنچه فکر می‌کنیم،
سپس ایران پاسخ خواهد داد و آتش‌بس پایان خواهد یافت.
@withyashar</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/withyashar/13499" target="_blank">📅 19:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13498">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حزب‌الله پیشنهاد آتش‌بس با اسرائیل را رد کرد
شبکه المنار حزب‌الله ،گزارش داد که دبیرکل حزب‌الله لبنان گفته است که این گروه از جنوب لبنان عقب‌نشینی نخواهد کرد.
نعیم قاسم در این بیانیه گفته است درخواست این توافق مبنی بر خروج نیروهای حزب‌الله از جنوب لبنان، در شرایطی که این منطقه زیر آتش قرار دارد، به معنای "تسلیم شدن، شکست و تحقق اهداف دشمن" خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/13498" target="_blank">📅 19:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13497">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وای‌نت: موساد در اقدامی با هدف سرنگونی جمهوری اسلامی، سلاح‌های ضبط شده از حماس و حزب‌الله رو به کردهای مخالف جمهوری اسلامی داده بود.
سازمان اطلاعات مرکزی آمریکا، سیا هم در طرح استفاده از نیروهای کرد به‌عنوان بخشی از تلاش گسترده‌تر علیه حکومت ایران مشارکت داشته. این طرح در نهایت پس از فشار رجب طیب اردوغان، رییس‌جمهوری ترکیه، و در پی هشدارها درباره خطر گسترش درگیری منطقه‌ای، از سوی دونالد ترامپ لغو شد.
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/13497" target="_blank">📅 18:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13496">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOac7SHQQC2HG1rGGYFseQpbNTYrxu6Riq852KB3GsKdSn_zWyuGeshGRvOWyZWn9yBnjC9yGW4OsbtTpivAjwxIhd6CjMrLbXZjwPuF9yuY_x3JlDZRTFHTQZh6vBdgHyekZc0SOKJuo5xTBPFOjzHtgwyvHRomYWghGyi_1NSY1w0LOkMYov3kAtDQ2S7Fk_WLngGI5zWyR111JbRsz2Fhy0OGEI2hSdvCYBKctpGvwgA50eGoVvksmi1q4mLFP_CQxuG0k6d2I76d64jZZr4qqQYAU00YIwSHuqii8r-oGQqjPJBWI6TAVibLpk_kP6kAhZoUo-Kbfec80lx0Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلیسای کاتولیک یک جن‌گیر را پس از ارتباط دادن مشاهده‌های یوفو با فعالیت‌های شیطانی برکنار کرد،.
جن‌گیر مشهور و قدیمی کاتولیک، استیون روزتی، گفت به باور شخصی او بسیاری از مشاهده‌های یوفو ممکن است ماهیتی شیطانی داشته باشند ! وی علاوه بر آن روان‌شناس نیز هست. به همین دلیل وقتی او درباره یوفوها صحبت می‌کند، سخنانش بیشتر از یک فرد عادی مورد توجه قرار می‌گیرد
اسقف‌نشین کاتولیک واشینگتن این اظهارات را مغایر با رویکرد رسمی کلیسا دانست و روزتی از سمت جن‌گیر رسمی برکنار شد و همکاری کلیسا با مرکز معنوی او نیز قطع گردید.
روزتی بعداً عذرخواهی کرد و بر تبعیت از آموزه‌های رسمی کلیسا تأکید نمود.
این ماجرا بحث قدیمی درباره ارتباط احتمالی یوفوها، موجودات فرازمینی و پدیده‌های ماورایی را دوباره مطرح کرده است
@withyashar</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/13496" target="_blank">📅 18:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13495">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxHEo7_yvdkGQn3Xh1a43yh4Nh-9fc64Jxym8wgFavbF2GzZ_phYCsucmVCrskHS5ujM6aqReT4ZWcV08j4_HVdU0HQA8pbpXgBD09p6hrV5PeOyDjfPGfdYivpFF6cRTuBixfB6bEUbEO8stbnf4r0Xg5TAq83RJjSZszUkeu95NfvxTwXjAvb1UYvrZ4KHe9qH5EG2jDT-9jL5ets7AYVrUGEStdarBnO0UgAO7qaHGUDLrln-bbLTLUfX0Tt_wU0bC7JMvZqmABvwLjpCm-NiA5uceAiTtWWUh-da1snM7zc9sAk4SEu6ErkffPSYLdO8CsxDq2K5OcbQdVImHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورانیوم رو بردن تحویل بدن
🤣
@withyashar</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/13495" target="_blank">📅 17:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13494">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سپاه: اسرائیل فورا حملات خود را متوقف و از مرزهای اشغال‌شده لبنان عقب‌نشینی کند
هیچ آرامشی در منطقه بدون عقب‌نشینی از مناطق اشغالی لبنان برقرار نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/13494" target="_blank">📅 17:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13493">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اصلا جان بر کف و جان فدا برای ما بود اونا گرفتن
😃
🤣
اون عرزشی ها کپی‌کارن زبان فارسی‌هم میراث ما هست نه اونا ، شاهنشاهی هم میراث ما هست لغت شاه هم کل دنیابگین میگن شاه ایران !</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/13493" target="_blank">📅 17:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13492">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مردم به ایلان ماسکم دیسلاک دادن موشک هوا کرد
😁
شما توجه نکنید پیشنهادم به بعضی ها اینه که یک جعبه شیرنی‌بگیرن و با خودشون آشتی کنند</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/13492" target="_blank">📅 17:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13491">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyxylpkVSqDgGMYvOpB7enCA2moolcTEfml_UqYlSwzT4jR6Jo0WPaz7xt1WZ39u5M47NlQu7dt1choxOb6igeuRlt1NOUXuDRh-bRrPJKjX0mT7fkEnj9QHCG_UrAie7UWdgIlDIxRcunTw4-1xyfMG2RsUaNwo2QmATjzpCSPYdfMmH1DDNQT0TLcrcfITuIjuRl7wAjLL8xIDgP-9uvy5DMMp_su-aAPck_B525bUQnXPBBqd1emjdmUNEEKwrMVXQnoa4_CBxwz_BxBdAlYjL3N3PMOLA9zh0vmJRWAOMC0EfeYFjpLoS7hATHub95tOKzEOTIGyWFeK1_x3bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا شاهزاده گفته جانفدا!!! جاویدنامان باید میگفت</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/13491" target="_blank">📅 17:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13490">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🌹</strong></div>
<div class="tg-text">چرا شاهزاده گفته جانفدا!!! جاویدنامان باید میگفت</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/13490" target="_blank">📅 17:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13489">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bf81edef.mp4?token=GGJvGvwt3sTNi2na63_ZIxpxndbRiAd3a17wgfy81486HaNciGRH_qWd1WaAZrGvo61ZZfl9-SFAWCL3p3fQ63OWd5G1OHnW2clWqdBgzncOlZO2t1ms1TOZEBx-bUNOwTAzQlPfZylG3VG5sLiaMrcxK1pytgE3pouapIpQr6qF_CjMqxcVwy9IV_Vl6lJBSNEvu9JKBYbEfcooZQmMLUePyAcm74kmuOqFATsxWtcPCh3SyCL3B-_vggloRuaZ-9cFE7c_AZr-1CQkgjulzm1rSd0awYoolHYb052wML_IGrU5hAfQiPcA77XpXtvJqE1eP82KFtnxrs0X3bESWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bf81edef.mp4?token=GGJvGvwt3sTNi2na63_ZIxpxndbRiAd3a17wgfy81486HaNciGRH_qWd1WaAZrGvo61ZZfl9-SFAWCL3p3fQ63OWd5G1OHnW2clWqdBgzncOlZO2t1ms1TOZEBx-bUNOwTAzQlPfZylG3VG5sLiaMrcxK1pytgE3pouapIpQr6qF_CjMqxcVwy9IV_Vl6lJBSNEvu9JKBYbEfcooZQmMLUePyAcm74kmuOqFATsxWtcPCh3SyCL3B-_vggloRuaZ-9cFE7c_AZr-1CQkgjulzm1rSd0awYoolHYb052wML_IGrU5hAfQiPcA77XpXtvJqE1eP82KFtnxrs0X3bESWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضایت شهبازی از کار
😂
@withyashar</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/13489" target="_blank">📅 17:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13488">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohamad Jalilzadeh</strong></div>
<div class="tg-text">اقا ری اکشن کوچکترین تمرین هست برای پذیرش دموکراسی
وقتی یه عده همه ش دنبال کم و زیاد کردن ری اکشن هستن و دنبال اینن که کی چه ری اکشنی زده در آینده ی ایران چطور میخوایم همدیگه رو تحمل بکنیم و باهمدیگه حرف بزنیم؟
همه ری اکشنا باید باز باشه و کاملا مخفی</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/13488" target="_blank">📅 16:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13487">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">شاهزاده رضا پهلوی : مسابقات جام جهانی فوتبال فرصتی کم‌نظیر برای رساندن صدای ملت ایران به جهانیان فراهم می‌کند. از این فرصت تاریخی بهره بگیریم؛ پرچم شیر و خورشید را در ورزشگاه‌ها، خیابان‌ها و میدان‌های شهرها به اهتزاز درآوریم و تصاویر جان‌فداییان راه آزادی…</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/13487" target="_blank">📅 16:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13486">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">چند گزارش ساعت ۱۵:۵۴ دقیقه محدوده شمال شرق تهران همچنین نیاوران صدا پدافند شنیده شد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/13486" target="_blank">📅 16:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13485">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شاهزاده رضا پهلوی : مسابقات جام جهانی فوتبال فرصتی کم‌نظیر برای رساندن صدای ملت ایران به جهانیان فراهم می‌کند. از این فرصت تاریخی بهره بگیریم؛ پرچم شیر و خورشید را در ورزشگاه‌ها، خیابان‌ها و میدان‌های شهرها به اهتزاز درآوریم و تصاویر جان‌فداییان راه آزادی را در برابر چشم جهانیان قرار دهیم.
@withyashar
وی به این موضوع که ورود پرچم ما به ورزشگاه ممنوع است و چه راهکاری باید داشته باشیم اشاره نکرد.</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/13485" target="_blank">📅 16:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13484">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0ULlsJUdFLhmnf1beUCVS6unJfCe52rtcRQCTq-0-t8GWEiiSod4cHMxKCawXzTwl0J97NshGZF-EdktS4H7Ces8pRofngGZ6MQ4wmh3Ip5MCSF8KLI0Tj1TB5jOzb-eeludH4IsfZKFVPVBtcqAH8U1xOfnsKU4ozEL_bJTBCevsbAUfiVSp75ATp9_5H-VNlZ3jKkUJPTuj0wxSKfpQZIiC2cxlg2ffprMUgRlmwZ3JWFkkD1ox7B7Js38535MYkO7uhqm049EDgS4feKMTQcH7QCiwx6QR1MlLIMytK7bzjgIJv_WCO6wpQQtjNgcBDVHCMT52GAt11TIssQAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل : سازمان تروریستی حزب‌الله گلوله‌های خمپاره‌ای شلیک کرده که به یک موقعیت نیروهای سازمان ملل اصابت کرده و در نتیجه یک نفر از کارکنان سازمان ملل در جنوب لبنان کشته شده است
شلیک‌های حزب‌الله نیروهای بین‌المللی را در معرض خطر قرار می‌دهد و به کارکنان سازمان ملل که در منطقه فعالیت می‌کنند آسیب می‌زند
@withyashar</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/13484" target="_blank">📅 16:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13483">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نعیم قاسم، رهبر حزب الله: نتیجه مذاکرات دولت لبنان با اسرائیل شرم آور و پوچ است و اونو بطور کامل مردود اعلام میکنم.
تا زمانی که تجاوز ادامه داره به هر جایی که تصمیم بگیریم و بتونیم حمله می‌کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/13483" target="_blank">📅 16:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13482">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ: در وسط مذاکرات پایانی برای پایان دادن به جنگ هستیم
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/13482" target="_blank">📅 15:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13481">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPU6REk0RMnl6eU39YshBMkEhBGF168a2n3v9DYX2z7klur-z0hOok5UnJQWgFi-EF0tf2h8ihBhj0AdB1Zx-A7gno7tVtoGt1x9QXQKEBfZJxlDYfl8Nzp8lISeiEYp6YN0tD8FWSRT-DPjw1MxoeNvfKjXbWfhLNqeO964_9J_pXE2_66P6jhGlmILdPAGGG7k4zFq1S3APD3UWnaZ4uCLaZZJQhsZKMjaCvvlhQWS9pN6xWkR65v3AE-ABFEHU3peUd-5HZvzvRwsntTnmn0LgdeT8b6NNI98ZbSFZhJTgotA-LLOIx6LYHYQEPtonu2Hy6GAsvPhLhUuzVm9DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ عکسی از نشان‌هایی با نماد جمجمه به سبک ترامپ منتشر کرد
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/13481" target="_blank">📅 15:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13480">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1oLTtF2ytkz6hWEdyUIrpkSj5TZgCEUjd24lC_IQeojiPmhfu6e1SObXwAiQNIaZahmmvB_1PKPkdVyKkOYPaNKcCKJhOPkaUR3oqD1V38R8TexEr9kHF57hOsiBE5J-4yV3yLfzOVT1d-R7HQ4ORkqsWDihGt9vPfLj-BW0SqaBgtnluxsVwjjh7PRmsXnnhiKDPIuoiduLNW7hKhOCk6RtS8bMPgs3FrITZsv9Sq9eNruDnRaQjt1KKTlCT-2Xr1e5jx4vLcPw0GRf-_nbcYMR8MvVOYBATWHJxZWZpDHQSHdmN4SryXB6A20f-lWNQ5w0AKtq00evGeoM2-TJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : دیروز، در یک رأی‌گیری بی‌اهمیت، مجلس نمایندگان با رأی ۴ جمهوری‌خواه بد و همه دموکرات‌ها، تلاش کرد اختیارات جنگی من را محدود کند؛ درست در میانه آخرین مذاکرات من برای پایان دادن به جنگ با جمهوری اسلامی ایران. چه کسی چنین کار غیرمیهن‌پرستانه‌ای انجام می‌دهد؟ آن‌ها می‌دانند وضعیت مذاکرات در چه مرحله‌ای است. دموکرات‌ها با چیزی به نام «سندروم جنون ترامپ» هدایت می‌شوند. آن‌ها ترجیح می‌دهند کشور ما شکست بخورد تا اینکه من یک پیروزی دیگر از میان پیروزی‌های بسیارم به دست بیاورم. آن چهار جمهوری‌خواه، ماجرای دیگری دارند آن‌ها اهل خودنمایی هستند! باید از کار خود شرمنده باشند.
MAGA!!!
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/13480" target="_blank">📅 14:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13479">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوربین‌های مداربسته لحظه‌ای را ثبت کردند که یک پهپاد کامیکازه شاهد-۱۳۶ ایرانی، اوایل صبح چهارشنبه به ترمینال ۱ فرودگاه بین‌المللی کویت حمله کرد. @withyashar
😟</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/13479" target="_blank">📅 14:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13478">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اکسیوس :  یک شکاف رو به رشد بین ترامپ و نتانیاهو در مورد آینده منطقه در حال شکل‌گیری است.
بر اساس گفته مقامات آمریکایی، ترامپ می‌خواهد تنش‌ها را کاهش دهد، درگیری‌های جاری را پایان دهد و به دنبال یک توافق دیپلماتیک با ایران باشد.
در مقابل، نتانیاهو به نظر می‌رسد تمایل بیشتری به حفظ فشار نظامی بر ایران و متحدانش، از جمله حزب‌الله، دارد.
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/13478" target="_blank">📅 14:06 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13477">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فیلم جدیدی که حمله هوایی آمریکا به پل B1 در کرج، ایران، را در طول جنگ نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/13477" target="_blank">📅 13:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13476">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کانال ۱۳ اسرائیل: «کابینه امنیتی اسرائیل امشب ساعت ۱۷:۰۰ تشکیل جلسه خواهد داد»
@withyashar</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/13476" target="_blank">📅 13:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13475">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وال‌استریت ژورنال : آخرین پیشنهاد ارائه‌شده از سوی ایران نتوانسته رضایت کامل دولت ترامپ را جلب کند و هنوز اختلافات اساسی بر سر برنامه هسته‌ای، سرنوشت اورانیوم غنی‌شده، رفع تحریم‌ها و آزادسازی دارایی‌های ایران باقی مانده است.
وال‌استریت ژورنال تأکید می‌کند که تماس‌ها و تلاش‌های دیپلماتیک همچنان ادامه دارد ، ترامپ همچنان به دنبال توافقی است که از دید او برنامه هسته‌ای ایران را به‌طور مؤثر محدود یا برچیده کند. در مقابل، ایران خواهان امتیازهایی مانند آزاد شدن بخشی از دارایی‌های مسدودشده و کاهش فشارهای اقتصادی پیش از پذیرش محدودیت‌های گسترده‌تر است.
اما مذاکرات هنوز زنده است و کانال‌های ارتباطی بسته نشده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/13475" target="_blank">📅 12:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13474">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وال استریت ژورنال:
«ترامپ به مشاورانش گفته است که جنگ تمام‌عیار با ایران را از سر نخواهد گرفت، مگر اینکه نیروهای نظامی آمریکا کشته شوند.»
مقام‌ها می‌گویند حملات مکرر ایران فشار بر رئیس‌جمهور را افزایش داده و تردیدهایی درباره دوام بلندمدت آتش‌بس ایجاد کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/13474" target="_blank">📅 12:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13473">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انتقاد مارک لوین از تصمیمات جدید ترامپ:
جمهوری اسلامی شاید نیروی دریایی و نیروی هوایی قابل ‌اعتنایی نداشته باشد، اما همچنان سپاه پاسداران و یک رژیم ایدئولوژیک دارد که شکست نخورده است؛ ما ملت ایران را برای سرنگونی رژیم مسلح نکرده‌ایم. رژیم کماکان در حال شلیک موشک های بالستیک و پهپاد ها است و هنوز مشخص نیست این تبادل آتش بخشی از مذاکرات است یا نه؛ هرچند در نهایت، چنین مواردی قابل راستی‌آزمایی نخواهد بود.
به نظر میرسد ما از نابود شدن سازمان حزب‌الله لبنان ممانعت می‌کنیم؛ حزب‌الله، قدرتمندترین نیروی نیابتی رژیم ایران میباشد که در 40 سال گذشته آمریکایی‌ها را کشته است؛ همچنین حماس به جای خلع سلاح، در حال تجدید قوا است.
این وضعیت برای آینده و پس از پایان دولت ترامپ، نشانه خوبی نیست. من فکر نمی‌کنم چین کمونیست که بزرگترین تهدید برای ما است، تحت تأثیر قرار گرفته باشد.
@withyashar</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/13473" target="_blank">📅 12:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13472">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9960590f00.mp4?token=rCppgY0BU_hu7G79KjKxkK3YMd6VM72kgPeDJBtH7gpLx45sCEBVlnLjQ7GggWYz4Dbp4AKxR_b-88hPm6DXu5-7dwcjrp4Uesty64nkbvWuHgQOszFbLBYG5A4AJSyqjKF0OjA3NGAcGUpMUZ9rNBvgHA_zvHUrUwkl3uN2vvTz-XwiXHQO_Cn7I7AP9esE6WIUENKEMto-9OyKyBSN77GS4XxhN603WjOd5Jmaq5quHC062icAKn-agFYNRLA481fFSq-ePTeLUUFVziiJrfNPukgg26cVj0zjSR-3207-Megi89fosO8b-xg5-eTH8XUn0ZwPO7nPOKhBAs5Whw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9960590f00.mp4?token=rCppgY0BU_hu7G79KjKxkK3YMd6VM72kgPeDJBtH7gpLx45sCEBVlnLjQ7GggWYz4Dbp4AKxR_b-88hPm6DXu5-7dwcjrp4Uesty64nkbvWuHgQOszFbLBYG5A4AJSyqjKF0OjA3NGAcGUpMUZ9rNBvgHA_zvHUrUwkl3uN2vvTz-XwiXHQO_Cn7I7AP9esE6WIUENKEMto-9OyKyBSN77GS4XxhN603WjOd5Jmaq5quHC062icAKn-agFYNRLA481fFSq-ePTeLUUFVziiJrfNPukgg26cVj0zjSR-3207-Megi89fosO8b-xg5-eTH8XUn0ZwPO7nPOKhBAs5Whw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری نیویورک پست
: آیا آیت‌الله (مجتبی خامنه‌ای) همجنسگرا است
ترامپ: بله.
مجری
: واقعا
دونالد ترامپ: بله، و فکر میکنم خیلی احترام براش قائل هستند.
@withyashar</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/13472" target="_blank">📅 12:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13471">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">در مراسم سی‌وهفتمین سال به درک رفتن روح‌الله خمینی، پیام کتبی منتسب به مجتبی خامنه‌ای خوانده شد. در این پیام آمده است «نظام سلطه پادگانی به نام اسرائیل از هر اقدامی برای جلوگیری از پیشرفت ایران کوتاهی نمی‌کند.»
@withyashar</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/withyashar/13471" target="_blank">📅 11:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13470">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الحدث گزارش داد آمریکا و جمهوری اسلامی به توافقی چهار مرحله‌ای نزدیک شده‌اند که با کاهش تنش‌ها آغاز می‌شود و به پرونده هسته‌ای و ترتیبات امنیتی منطقه ختم خواهد شد و انتقال از هر مرحله به مرحله بعدی، پس از «اجرای تعهدات» انجام می‌شود.
طبق این گزارش، مرحله نخست توافق شامل توقف عملیات نظامی مستقیم و پرهیز از هرگونه تشدید تنش یا گشودن جبهه‌های جدید در منطقه است. مرحله دوم نیز بر امنیت کشتیرانی، بازگشایی تنگه هرمز و ترتیبات امنیتی ویژه گذرگاه‌های دریایی و خطوط انرژی متمرکز است.
به نوشته الحدث، مرحله سوم این توافق شامل اعتمادسازی اقتصادی، کاهش محدود برخی تحریم‌های جمهوری اسلامی، آزادسازی بخشی از اموال مسدودشده ایران و ارائه تسهیلات مرتبط با صادرات نفت است.
بر اساس این گزارش، مرحله چهارم توافق پیچیده‌ترین مرحله به شمار می‌رود و ممکن است ماه‌ها طول بکشد. این مرحله شامل بررسی برنامه هسته‌ای ایران، سطح غنی‌سازی اورانیوم و سازوکارهای نظارتی و ترتیبات امنیتی منطقه‌ای است.
@withyashar</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/13470" target="_blank">📅 11:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13469">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مجتبی خامنه‌ای: هدف دشمن اینه فشار اقتصادی بیاره تا مردم ناامید بشن، مردم باید مقاومت کنن تا به قله برسیم
@withyashar
🥴</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/13469" target="_blank">📅 11:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13468">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ممد امین میمندیان، نویسنده پاورقی :  شایعه تجاوز به محمدرضا شهبازی، خزعبل و شایعه است و کاملا تکذیب می‌کنم.  برنامه طبق روال در حال پخش است و امشب هم منتشر می‌شود @withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/13468" target="_blank">📅 11:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13467">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jC55T5-XrwrRScGuf8lB1wxqY0zWLYZelyDY9g_4ePD_jfT6x41ixKFIQAtAXpUBCWPpd8eqkR2Jhognhee18foc48jO_HvCrTFGVMOugS-l4F8qYzBTK_SQ4m2A4CdEjTO7AmZYJ24DKkc5eXfIuOdd7Tz7VmKnXXERsKQLVd3d6PcJQrZFnMSP0vfhTrnKsu_3ATtyi9ELNteCRHYpTMF1yaOmTClRtU0IxZveIS1OikkXLFx0CKECvSUdU0CXvdAIZwcRy4CQb7ywgTdrpHi22dfOhUJffL8w4Npt28eZhC6OQ3AMo7FUTeh39y3P3kLt_H797VRST38ktllNBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موتور پهپاد شاهدی که به فرودگاه کویت برخورد کرد پیدا شد
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/13467" target="_blank">📅 11:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13466">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وزیر دفاع اسرائیل: به هدف قرار دادن زیرساخت های حزب الله در لبنان ادامه خواهیم داد
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/13466" target="_blank">📅 11:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13465">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6Ar9s0JvaY80x9Id6tfLKK2QqKkUAGskNcCvBMUc46fWcq669CSEW-I70lt8zmmqNP7uZq-k0aJCdepuZnKjEqXTpavBwXpoOqLpjUsfa-OvuE0nNHB0rgIz6z1l8VeFnCqcPFlrucxq3cR5cUNRKNTj4UG8Q1S5ItNV67l0B-ZILbWmB6iYxq8gHUP8WU4yCkGTerhzAVzyyN_MS3rZtyP9EgDV2umMKUP1aEBSguJcN4j-2bc46oY_mR5RfDhzlTfYuydxRrrO50x_it8MURgrOuz2HUIQgSmGj490CUIlXd2OLQu6jfMYNtD-ZmD1rJbzwaHRxrCRUDDeEvnhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای Falcon 900EX متعلق به دولت ایران در حال پرواز بر فراز دریای خزر به سمت روسیه است. این هواپیمای خاص توسط مقامات ارشد ایرانی استفاده می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/13465" target="_blank">📅 11:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13464">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مقام اسرائیلی: ایران تصمیم گرفته در صورت آزادسازی اموال بلوکه‌شده‌‌اش، بخشی از آن را به حزب‌الله اختصاص دهد.
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/13464" target="_blank">📅 09:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13463">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جنگ ترامپ با ایران و اختلال در حمل و نقل نفت از طریق تنگه هرمز، ذخایر نفتی آمریکا را به پایین‌ترین سطح خود از سال ۲۰۰۴ رسانده است.
برای کمک به مهار افزایش قیمت سوخت، آمریکا میلیون‌ها بشکه از ذخیره استراتژیک خود را آزاد کرده و همچنین صادرات به اروپا و آسیا را افزایش داده است تا جایگزین عرضه از دست رفته خاورمیانه شود.
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/13463" target="_blank">📅 09:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13462">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c487f9f7b.mp4?token=hBC_XS6LiAz9CAeTTVzreULh3twBQwOWrrlSFTYc6qdEV_ON5vlgcOLrKBuOeSyBqVtpx9jUfD8PNpwQzh-8WHzdANMiwy5KgvjFRX76a_C5PetiL_IvOfYSRj2bBcMtX55fR8_HAeKg8XZQvmOJMzORlUsm3-MW4AJKG_de95v5HJLb46dLpYV_fSQ_pQHeqxVxc8ZsVKzLC8kfLEgyDIJfyy3cjRftaj9XR9kUZrp4M-iyKK1ncFFpiMzrE9V8EG95lc1JiTMVp-2nmBioYSMRFY8LpVFgPi6MGJMKAXLvKb8rRvceMjynZrK4AgzK174JzXSZXg8rIUt_Zb_QVZ2POMsWZK0zOTP6o-l5zuf3sjvbNvZOc3LolNE8namjElRDLVO5RzOu2OcLnIHAbQ9AtIIEzy7fVmwsyHU7qJyIm0gIgGMN2FL0GK03sDKADTdHE3rpBTmNqEJL5Lb3LZaQ_WHlPCR5bxFnEreoFN8FCILoXvr3FHUl286J3fFijORAFTx1YbVPxuRJQ6BLZ_GCdMpGiQQbbtoQFKBYZyv0rGmvFEWlyO1l-BUJ-NSmFOqDtyCDshAjOANL9Psf1vI_2RM7zbUaMwagqsdjiVZEHkKrF05v_CplCNGbFzimnNdNCYoQ7dk5blEBXXF4T-zOBjejYap5dR6hYygnF0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c487f9f7b.mp4?token=hBC_XS6LiAz9CAeTTVzreULh3twBQwOWrrlSFTYc6qdEV_ON5vlgcOLrKBuOeSyBqVtpx9jUfD8PNpwQzh-8WHzdANMiwy5KgvjFRX76a_C5PetiL_IvOfYSRj2bBcMtX55fR8_HAeKg8XZQvmOJMzORlUsm3-MW4AJKG_de95v5HJLb46dLpYV_fSQ_pQHeqxVxc8ZsVKzLC8kfLEgyDIJfyy3cjRftaj9XR9kUZrp4M-iyKK1ncFFpiMzrE9V8EG95lc1JiTMVp-2nmBioYSMRFY8LpVFgPi6MGJMKAXLvKb8rRvceMjynZrK4AgzK174JzXSZXg8rIUt_Zb_QVZ2POMsWZK0zOTP6o-l5zuf3sjvbNvZOc3LolNE8namjElRDLVO5RzOu2OcLnIHAbQ9AtIIEzy7fVmwsyHU7qJyIm0gIgGMN2FL0GK03sDKADTdHE3rpBTmNqEJL5Lb3LZaQ_WHlPCR5bxFnEreoFN8FCILoXvr3FHUl286J3fFijORAFTx1YbVPxuRJQ6BLZ_GCdMpGiQQbbtoQFKBYZyv0rGmvFEWlyO1l-BUJ-NSmFOqDtyCDshAjOANL9Psf1vI_2RM7zbUaMwagqsdjiVZEHkKrF05v_CplCNGbFzimnNdNCYoQ7dk5blEBXXF4T-zOBjejYap5dR6hYygnF0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوربین‌های مداربسته لحظه‌ای را ثبت کردند که یک پهپاد کامیکازه شاهد-۱۳۶ ایرانی، اوایل صبح چهارشنبه به ترمینال ۱ فرودگاه بین‌المللی کویت حمله کرد.
@withyashar
😟</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/13462" target="_blank">📅 01:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13461">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edeb5c80d.mp4?token=e41RR4daw6ceXOo0Bb5U27e_lWr9xW418QdqFSshuu0TyPTtHrEgw2wxl4ASbMOrKZ-gDBIxIGk0NA4gESx7GXDcpqeDRUbHJ0xbKK0XwblZsY-WjIWnJBMZj4Fyllw5HhLL3CN0BWU5seUVkqfBtxQXMyp3jsO49NCrnE0NvSrsfnZG05uNQy6n4Q6sL1RAFsIaiTMKceldK5O72ylBDV1GhfgGpM1FgS4tA_TsnEU0CmRLwEuo7K7XmPAGdQ1JUkH9ezJazOpXK4ESZ3FU5T-ndFpgD7DnxvMGGWTBDb8QigT9qcHlfq7tm-29bzUGMCVYTMKDrASTL8D8KnS65w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edeb5c80d.mp4?token=e41RR4daw6ceXOo0Bb5U27e_lWr9xW418QdqFSshuu0TyPTtHrEgw2wxl4ASbMOrKZ-gDBIxIGk0NA4gESx7GXDcpqeDRUbHJ0xbKK0XwblZsY-WjIWnJBMZj4Fyllw5HhLL3CN0BWU5seUVkqfBtxQXMyp3jsO49NCrnE0NvSrsfnZG05uNQy6n4Q6sL1RAFsIaiTMKceldK5O72ylBDV1GhfgGpM1FgS4tA_TsnEU0CmRLwEuo7K7XmPAGdQ1JUkH9ezJazOpXK4ESZ3FU5T-ndFpgD7DnxvMGGWTBDb8QigT9qcHlfq7tm-29bzUGMCVYTMKDrASTL8D8KnS65w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان ایالات متحده قطعنامه‌ای درباره اختیارات جنگ مرتبط با جنگ ایران را با رای ۲۱۵ به ۲۰۸ تصویب کرد.
این قطعنامه تا زمانی که توسط سنا نیز تصویب نشود، اثر قانونی الزام‌آور ندارد و بنابراین تأثیر فوری آن محدود است.
با این حال، این اولین رای موفق مجلس نمایندگان است که قدرت‌های جنگی کنگره را در مورد جنگ ایران تأیید می‌کند و اقدام نظامی آینده بدون تأیید کنگره را محدود می‌سازد.
چهار جمهوری‌خواه به نفع آن رای دادند.
@withyashar</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/13461" target="_blank">📅 01:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13460">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">داداش اون بحث خیلی طولانیه اون میشه زمان ریست فکتوری طوفان بزرگ ( که با داستان خیالی نوح میشناسید ) تا اینجا بدون که قبلش تمدنهای بسیار پیشرفته بود روی زمین ، باشه برای بعد از آزادی
😂</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/13460" target="_blank">📅 01:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13459">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from00:30</strong></div>
<div class="tg-text">درود ولی من‌میرملاس لرستان رفتم اونجا دیوار نوشته هست‌مربوط به 12000 سال پیش</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/13459" target="_blank">📅 01:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13458">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یاشار : دمت  آقا دایی ، مردی ، خواستم تکمیل کنم که عدد
۲۵۰۰ سال
به طور مشخص به
سابقه پادشاهی شاهنشاهی ایران
اشاره دارد، نه به کل تمدن ایران ،
تمدن در فلات ایران ۵۰۰۰ الی ۷۰۰۰ سال حتی بیشتر سابقه دارد
@withyashar
😁
🙌🏾</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/13458" target="_blank">📅 01:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13457">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">علی دایی: هیچ قدرتی توان شکستن تمدن ۲۵۰۰ ساله ایران را ندارد
هرگز قدرتی نتوانسته و نخواهد توانست تمدن و فرهنگ ۲۵۰۰ ساله ایران باستان را که در قلب و جان یکایک ماست در هم بشکند.
‏ایران زمین، روزگارها دیده است آنچه سرافراز می‌ماند همیشه تا ابد وطن است.
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/13457" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13456">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دو منبع مطلع در مذاکرات به i24NEWS عبری:
مذاکرات بین آمریکا و ایران به دلیل اصرار ایرانی‌ها بر آزادسازی پول‌ها، «پول نقد»، از میلیاردهایی که مسدود شده‌اند، حتی در مرحله اول، متوقف شده است .
در روزهای اخیر، میانجی‌ها تلاش کرده‌اند در این موضوع مصالحه کنند اما ایرانی‌ها بر دریافت پول در همان مرحله اول، در چارچوب توافق کلی، قبل از انجام هر اقدام واقعی در میدان، اصرار دارند.
مقامات ارشد آمریکایی تأکید می‌کنند: در ابتدا پولی آزاد نخواهیم کرد مگر اینکه ایران گام مهمی در مسئله هسته‌ای و هرمز بردارد و همچنین توافق کلی بسیار معنادارتر باشد.
@withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/13456" target="_blank">📅 01:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13455">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DL33p_i0Cnlou-1l2APlPZrsGLlC27DgCUfLQHnvtTJDwKcMrbTgeYCb7JGnFZjvSyjK8z-rj3ksp08BRX-vALpXG6q3xyv27GeNVp4PNtxV43Z9j5Is49USGXwkSjLHDIjeHmzkViRxEhmASsMEjCaW0C_3JSGr4xbl0Zjj3SqyvFJh-ky3nUcz_5UyswW-JHsQDWALQZC61Itb2fZ86ZNctLZkCX1pBFctyyszTUN7hbvp7_AKyCIuBF2-uPMX9hUmtj6hmlADxqqOPH78JoLHKDLLV68BozL41Z2rUJMp78lPh_YjTPx8IWvDRqoJfRd2xbjHuPhFWkGjdl3hoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقامات آمریکا
جمشید قومی
، شهروند دوتابعیتی ایران و آمریکا و مدیرعامل شرکت «فرار پرداز رایانه» در تهران را به نقض تحریم‌ها متهم کرده‌اند. طبق ادعای دادستانی، او طی بیش از یک دهه تجهیزات شبکه، امنیتی و رمزنگاری ساخت آمریکا را از طریق واسطه‌هایی در دبی به ایران، از جمله سازمان انرژی اتمی و وزارت دفاع، منتقل کرده است. همچنین متهم است حدود ۱۵ میلیون دلار درآمد حاصل از این فعالیت‌ها را به آمریکا منتقل کرده و با آن یک عمارت ۳۵ میلیون دلاری در کالیفرنیا ساخته است. در صورت محکومیت، با حداکثر ۲۰ سال زندان فدرال روبه‌رو خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/13455" target="_blank">📅 00:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13454">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">منابع العربیه: پیشرفت‌هایی در مذاکرات لبنان و اسرائیل حاصل شده است، اما هنوز توافق دائمی به دست نیامده است
اختلاف بر سر سلاح‌های حزب‌الله همچنان مانع اصلی هرگونه توافق بلندمدت است
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/13454" target="_blank">📅 00:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13453">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ:
ما در واقع برای اولین بار با حزب‌الله صحبت کردیم. نمی‌دانستیم آن‌ها صحبت می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/13453" target="_blank">📅 00:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13452">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ : تنگه هرمز فوراً باز می‌شه وقتی من یادداشت تفاهم رو با ایران امضا کنم
تنگه هرمز باز خواهد شد، مین‌روب‌هامون اونجاست
زیر آب هستن، خیلی خوبن، تکنولوژی‌شون فوق‌العاده‌ست
ما مین‌ها رو جمع کردیم، بیشترش رو پاکسازی کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/13452" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13451">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دوستان خواهش میکنم دایرکت جای کامنت دادن به مطالب نیست
😟
خدایا به چه زبونی بگم ؟ بفرستید برای دوستون و باهاش‌چت کنید ، به بچه آدمیزاد چند بار میگن</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/13451" target="_blank">📅 00:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13450">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خبرنگار
: شما هفته قبل گفتید آمریکا می‌ره داخل و مواد هسته‌ای دفن‌شده رو در هماهنگی با ایران بیرون می‌کشه. آیا ایران واقعاً با این موافقت کرده؟
ترامپ
: خب، بستگی داره داری درباره کدوم روز حرف می‌زنی. این چیزها خیلی هم بزرگ‌نمایی شده. من خودم هم اون رو یه‌جورایی بزرگ‌تر از واقعیت نشون دادم.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/13450" target="_blank">📅 00:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13449">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a531a29092.mp4?token=CpjPVAvMAK3mFOrDVLwHM9XRRF8uMCmZjk1dEWVPwWOe42p5nufwpUmwXvZbss4RH0zyfhXCuruK-TOdysBYHEugT__yxm1JKPdeKRwJ5FeRJeclpME5pdne877jgpbFsmdS3GvheQ68R1GhPFR3ezL_ipOfcc2vuyD53JQrfaf6qk3dlY9ngtFQX18_c9u2ExpW7K8m7xMLqmYPRTUKg82FP_1Xe2VFbz_kOaIBix7sB7P-Ih6bTP4xufGwwWMTVMjR257q86JStSztE33gHimc3Mn2uKm3-ZYS0Ni_A0RFMOADk-WeFkh6Lvdh_C6oe0_qTa-qY_gjTZNQRMqejA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a531a29092.mp4?token=CpjPVAvMAK3mFOrDVLwHM9XRRF8uMCmZjk1dEWVPwWOe42p5nufwpUmwXvZbss4RH0zyfhXCuruK-TOdysBYHEugT__yxm1JKPdeKRwJ5FeRJeclpME5pdne877jgpbFsmdS3GvheQ68R1GhPFR3ezL_ipOfcc2vuyD53JQrfaf6qk3dlY9ngtFQX18_c9u2ExpW7K8m7xMLqmYPRTUKg82FP_1Xe2VFbz_kOaIBix7sB7P-Ih6bTP4xufGwwWMTVMjR257q86JStSztE33gHimc3Mn2uKm3-ZYS0Ni_A0RFMOADk-WeFkh6Lvdh_C6oe0_qTa-qY_gjTZNQRMqejA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ما می‌توانیم دو یا سه هفته دیگر ادامه بدهیم و همه را از بین ببریم. انجام این کار خیلی آسان است.
اما اگر بتوانیم چیزی را روی کاغذ بیاوریم و مکتوب کنیم که بدون کشتن همه، همان نتیجه را به دست بدهد، ترجیح می‌دهم آن راه را انتخاب کنیم.»
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/13449" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13448">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07761ae5b.mp4?token=U3RFAa1TjYcJjMwCPP86vdE6GbhTcC1PDOJYbY1U_UkKN-JysMrwLlx2CpI4nZR3MIjGCFTqJA-vaPcPxa0SII_Z7gqq-qROrMjerKWgpxsWnTu2mkVvH7H7RI9HOV9-ovGW7xRr2nIN4XRxYLdEE61L6y_yJYjn53UA1EI2RnoAy4qV2g8GcgD3LXtON7oLKedl6hIQLKNEKx1Z_WuTVJcBcKpIC5vGjQaTLOe5r12OgTRSzIUN4UrXHO8yc8I_YjxUDhDQbENueEo5uDy-jyCPpinwfs3l3WudlSBNJwE7LoRvZwt4q1GW-BuvchU4onUEw7NCpVDdn3rw93ZH6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07761ae5b.mp4?token=U3RFAa1TjYcJjMwCPP86vdE6GbhTcC1PDOJYbY1U_UkKN-JysMrwLlx2CpI4nZR3MIjGCFTqJA-vaPcPxa0SII_Z7gqq-qROrMjerKWgpxsWnTu2mkVvH7H7RI9HOV9-ovGW7xRr2nIN4XRxYLdEE61L6y_yJYjn53UA1EI2RnoAy4qV2g8GcgD3LXtON7oLKedl6hIQLKNEKx1Z_WuTVJcBcKpIC5vGjQaTLOe5r12OgTRSzIUN4UrXHO8yc8I_YjxUDhDQbENueEo5uDy-jyCPpinwfs3l3WudlSBNJwE7LoRvZwt4q1GW-BuvchU4onUEw7NCpVDdn3rw93ZH6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
در آن بخش از جهان«خاورمیانه»، آتش‌بس زمانی است که شما به شیوه‌ای معتدل‌تر تیراندازی می‌کنید.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/13448" target="_blank">📅 23:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13447">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ درباره حمله ایران به کویت:
برای هر چیزی دلیلی وجود دارد، و ما به آنها ضربه‌ای سخت زدیم... آنها کمی تحریک شده بودند؛ آنها در حال پاسخ دادن بودند.
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/13447" target="_blank">📅 23:54 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
