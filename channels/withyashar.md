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
<img src="https://cdn4.telesco.pe/file/ibnf0F9-tf6r2wrUf8JY-Sr5svkjz_sBvxtmdvzkiEQ60wtDTR9u6zqMHOIx_CuPmvZmFNUkBM-IJF4MuSc_TXpNIylZ4WXVQtR7wGJIvTFXrcclxDGLKwjqKpFeQq0ANz0CSR_99UUCysWvTJCJ54zoAbERpwM3NqUuM1FXQmsvKre0OLmXw7yvyaepOv0vht88u3VzddDQ6bfR_Zrw5ywuc3paHMPdrhStciXsYFnGx0bIK706qsP2BekQKI-AEeH323FT6punZ9IOPRYMnesySnv2HQYe2xuXWm0IoE_QPXqjFNg0_vnzPDi_UQAZcaAcVHzxcmXUN19Evyp9kw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 329K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 19:46:32</div>
<hr>

<div class="tg-post" id="msg-14835">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ: من با نتانیاهو صحبت کردم و بهش گفتم:داری چه غلطی می‌کنی؟
@withyashar
🤣</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/withyashar/14835" target="_blank">📅 19:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14834">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کرملین: پوتین و ترامپ درباره ایران و اوکراین گفتگو کردند
@withyashar</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/withyashar/14834" target="_blank">📅 19:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14833">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در تماس اخیر با رئیس‌جمهور ترامپ گفت که اسرائیل با عقب‌نشینی کامل از جنوب لبنان، از جمله پنج نقطه‌ای که در حال حاضر توسط نیروهای دفاعی اسرائیل (IDF) در اختیار است، موافقت نخواهد کرد، طبق گزارش معاریو.
نتانیاهو همچنین عقب‌نشینی از خاک سوریه را که اسرائیل از زمان سقوط بشار اسد اشغال کرده است، رد کرد
@withyashar</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/withyashar/14833" target="_blank">📅 19:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14832">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">شبکه ۱۴
:
ایالات متحده در حال حاضر از طریق واسطه‌های مختلف تلاش می‌کند از هرگونه حمله احتمالی نیروهای نظامی ایران به اسرائیل جلوگیری کند.
@withyashar</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/withyashar/14832" target="_blank">📅 19:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14831">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">باراک اوباما : توافق ترامپ که از ماله من زاقارت تره
باراک اوباما، رییس‌جمهوری پیشین آمریکا، در گفت‌وگو با ای‌بی‌سی نیوز گفت بعید است هر توافقی که میان آمریکا و جمهوری اسلامی حاصل شود، تفاوت چشمگیری با برجام داشته باشد یا نسبت به آن بهبود قابل توجهی محسوب شود.
اوباما با اشاره به برجام گفت این توافق بر محدود کردن برنامه هسته‌ای ایران، تعیین سقف برای غنی‌سازی اورانیوم و پذیرش بازرسی‌های آژانس بین‌المللی انرژی اتمی در ازای رفع بخشی از تحریم‌ها و آزادسازی دارایی‌های مسدودشده ایران استوار بود.
او همچنین ابراز امیدواری کرد بمباران‌ها متوقف شود و مردم عادی دیگر از پیامدهای جنگ رنج نکشند.
رییس‌جمهوری پیشین آمریکا تاکید کرد دیپلماسی را به اقدام نظامی ترجیح می‌دهد و گفت نباید تصور کرد که می‌توان با زور یا بمباران به راه‌حل دست یافت.
اوباما خواستار بررسی کامل گزینه‌های دیپلماتیک شد و گفت توافق‌هایی که همه مشکلات را حل نمی‌کنند اما ۸۰ یا ۹۰ درصد آن‌ها را برطرف می‌کنند، می‌توانند از جنگ جلوگیری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/withyashar/14831" target="_blank">📅 19:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14830">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رسانه‌های اسرائیلی: شهرداری‌های ایلات، تل‌آویو بزرگ، نتانیا و حیفا پناهگاه‌های عمومی را باز کرده‌اند.»
@withyashar</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/14830" target="_blank">📅 18:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14829">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">منابع عربی : امریکا در پیامی به اسرائیل گفته امشب ایران حملات موشکی انجام خواهد داد
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/14829" target="_blank">📅 18:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14828">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1fbuXsikBY6sQ54CRt5zCh-cXtibL164ss5QNSV2UODHmos29M3hmBljZ7wZPpwJWAy9Rsqz_jZN5eyXMlS0jq1zzjmVIqePhWDO7IZrA0h80bu5gLA0b0J7SJMavZuBLWKreFwrehx3R4Zk5WrpRPi-Yk0ekpqryC7xTJWXjSf0Idvib9G_yu0LoXmVke2NfBlyzJbUWDpL9LRFYqyBbXbD2_e_aWBmbmcI2lW1rICfQn2u5wprDD3-hNQODuL1Vm5otySvujlqtlLg12FPmNp3XmCZ5VQz_sH4TWXdPJX80Nl8exFPfG9_ZmamiRlIIKJFTkadNipRHC7gUvl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «حمله امروز صبح به بیروت نباید رخ می‌داد، به‌ویژه در چنین روز مهمی که ما تا این اندازه به دستیابی به یک توافق صلح با ایران نزدیک شده‌ایم. اسرائیل حق دارد از خود در برابر تهدیدها دفاع کند، اما حمله‌ای که در واکنش به آن انجام شد بسیار کوچک و بی‌اهمیت بود؛ هیچ‌کس آسیب ندید، مجروح نشد یا کشته نشد و نباید این روند مهم را مختل کند. ما بسیار به توافقی نزدیک هستیم که صلح را برای منطقه، از جمله لبنان، به ارمغان خواهد آورد و همه طرف‌ها باید از درگیری و تشدید تنش خودداری کنند. نباید هیچ حمله دیگری از سوی اسرائیل در هیچ نقطه‌ای از لبنان انجام شود، اما در عین حال نباید هیچ حمله‌ای از سوی هیچ طرف دیگری، از جمله حزب‌الله، علیه اسرائیل صورت گیرد. این می‌تواند آغاز یک صلح طولانی و زیبا باشد؛ نگذارید این فرصت از بین برود! از توجه شما به این موضوع سپاسگزارم. دونالد جی. ترامپ، رئیس‌جمهور ایالات متحده آمریکا»
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/14828" target="_blank">📅 18:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14827">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">هگست، وزیر جنگ آمریکا:
من انتظار ندارم که حملات اسرائیل به حومه جنوبی بیروت مانع توافق با ایران بشه؛ اگر ایران میخواد این موضوع ادامه پیدا کنه، باید حزب‌الله رو مهار کنه.
@withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/14827" target="_blank">📅 18:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14826">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/14826" target="_blank">📅 18:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14825">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromALIREZA</strong></div>
<div class="tg-text">تو ویس گفتی یه سری بزنیم به کانالهی رژیم اسگولا اینو منتشر کردن</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/14825" target="_blank">📅 18:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14824">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlcDyNhTaIpe2kuwQj7Benq0H2c36WFZ80mOxioZFUGe1lFMIzvDhY4W_Y5pGbezoWdXwi74B2lFUz01t6jhwJ21QE7g_U87faDNhC8U6JzScS-_4LiDtjRv4MVMLQuxvJN0q2KGPnRt-4RlhmH8J3Nej1OaPPGdmsEcKrvL9KxqjtRohT-KoWnNTpd74N-HcKgWKJFBkZQd1lBHVcc6HICFX7TVL-vdtaQOJEtAc6Lr84OUHsrLwSZfvhRx6gVIiDAyutHhx1J6DMzbJ5VkwEJa2T7W4g7fKIgOnGBuK6kLUTBN5FMLPDgWPZ4Ohxw6EPur--cDYnIAK7VNrXIbng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی‌پیش ستون دود جنوب‌کرج
@withyashar</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/14824" target="_blank">📅 18:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14823">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1de42f04e.mp4?token=PmY3zlamaTpyerBCGIUsS6fhqWGGOCU_j4DldkGJde_sLxbkZJ58ZmHiyk2qubnwwJlUb25Kent9SYxZ9egiBy9YKIKCTo5jfpznGIaQIpkAi97Qcro6PqW2idREz3gdiunXXSmiEGHs1drfueZm8aUk1fIpfKfErdg6resEhWGf8QFVf07bPHIt8W2BY_NGWIPfT5GM1X09m0DdUJPclSynPYgjpJQ0f5gn2gOH2X2yD2vCVYSO1btQuYqq8o6lZETbsxi6aKnZk2MMBHW9QdAfKB1Ik3pEPS8rlPHtB0tFGW3siWgLPn0E1COV8iRjWbU_1wYqiSf8o1ngaA9VDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1de42f04e.mp4?token=PmY3zlamaTpyerBCGIUsS6fhqWGGOCU_j4DldkGJde_sLxbkZJ58ZmHiyk2qubnwwJlUb25Kent9SYxZ9egiBy9YKIKCTo5jfpznGIaQIpkAi97Qcro6PqW2idREz3gdiunXXSmiEGHs1drfueZm8aUk1fIpfKfErdg6resEhWGf8QFVf07bPHIt8W2BY_NGWIPfT5GM1X09m0DdUJPclSynPYgjpJQ0f5gn2gOH2X2yD2vCVYSO1btQuYqq8o6lZETbsxi6aKnZk2MMBHW9QdAfKB1Ik3pEPS8rlPHtB0tFGW3siWgLPn0E1COV8iRjWbU_1wYqiSf8o1ngaA9VDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/14823" target="_blank">📅 18:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14822">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02564fdd83.mp4?token=KaG3wGsWs6bffCncTXR78RaRPDpLepjbgJ1sdgZ2A3tpSN0UASdYntHu1W7B9Uovzlfdl5Jl8KYazS2vKlkRROuVflXz384IwYm1kMxIphhQL40_fNhFTTtRAe_Hocj5537F-tHBWlU1MD9fOpbo4dNN_WdQGYVLcFanM_dxlpr09x6-GN2WC_ledUbjRzuRWGG3BOqIbfZysWyyGbFsVd709fHiPLhHPUIBgf8taNN6Qm9mKpLVeaqvNOdarLYKpBgEGcPgLofQ55glNSSl1ULSHw5zuWdkx9wHPRVn3I47Qjf-kk8pKx8vPgwZJlwZA-j9nnUa6bVbiYNPfoTC_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02564fdd83.mp4?token=KaG3wGsWs6bffCncTXR78RaRPDpLepjbgJ1sdgZ2A3tpSN0UASdYntHu1W7B9Uovzlfdl5Jl8KYazS2vKlkRROuVflXz384IwYm1kMxIphhQL40_fNhFTTtRAe_Hocj5537F-tHBWlU1MD9fOpbo4dNN_WdQGYVLcFanM_dxlpr09x6-GN2WC_ledUbjRzuRWGG3BOqIbfZysWyyGbFsVd709fHiPLhHPUIBgf8taNN6Qm9mKpLVeaqvNOdarLYKpBgEGcPgLofQ55glNSSl1ULSHw5zuWdkx9wHPRVn3I47Qjf-kk8pKx8vPgwZJlwZA-j9nnUa6bVbiYNPfoTC_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای عراقچی‌ شما گوه میخورید
🤣
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/14822" target="_blank">📅 18:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14821">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/14821" target="_blank">📅 17:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14820">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ارتش اسرائیل: آماده شلیک از ایران در ساعات آینده هستیم، در حال حاضر تغییری در دستورالعمل‌ها وجود نداره.
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/14820" target="_blank">📅 17:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14819">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کانال 15 اسرائیل:تمام سامانه های پدافندی در اسرائیل به حالت آماده باش کامل درآمدند و در انتظار پرتاب موشک قریب‌الوقوع از سمت ایران می‌باشند
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/14819" target="_blank">📅 17:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14818">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل دستور تشدید عملیات‌های زمینی در جنوب لبنان رو صادر کرده و به نیروهای دفاعی اسرائیل دستور داده که عمیق‌تر به خاک لبنان پیشروی کنند.
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/14818" target="_blank">📅 17:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14817">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سفیر آمریکا در سازمان ملل متحد:
رئیس جمهور ترامپ و معاونش جی‌دی ونس، کاملاً به امضای توافق امروز متعهد هستن.
@withyashar</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/14817" target="_blank">📅 17:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14816">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مرندی عضو تیم مذاکره کننده:
فعلاً مذاکره دیگر در کار نخواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/14816" target="_blank">📅 17:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14815">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزارت امور خارجه‌اسرائیل در واکنش به تهدیدهای ایران اعلام کرد: “این حکومت طبق معمول دروغ می‌گوید. نماینده ایران، حزب‌الله، همان طرفی است که به اسرائیل حمله کرده است. ما شلیک آتش به سوی خاک خود را تحمل نخواهیم کرد.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/14815" target="_blank">📅 17:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14814">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ بیدار شد
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/14814" target="_blank">📅 17:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14813">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الحدث: علی الحاج، از فرماندهان ارشد حزب‌الله در حمله به ضاحیه بیروت هدف قرار گرفت. تداوم ضربات سنگین به بدنه فرماندهی گروه‌های نیابتی رژیم ایران در لبنان. @withyashar</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/14813" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14812">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الحدث: علی الحاج، از فرماندهان ارشد حزب‌الله در حمله به ضاحیه بیروت هدف قرار گرفت.
تداوم ضربات سنگین به بدنه فرماندهی گروه‌های نیابتی رژیم ایران در لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/14812" target="_blank">📅 17:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14811">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وب‌سایت اکسیوس گزارش داد ارتش اسرائیل اندکی پیش از حمله به منطقه ضاحیه بیروت، فرماندهی مرکزی آمریکا (سنتکام) را از این عملیات مطلع کرده بود.
ارتش اسرائیل پیش‌تر در بیانیه‌ای اعلام کرد در واکنش به شلیک پرتابه از سوی حزب‌الله به شمال اسرائیل و نقض آتش‌بس از سوی این گروه تحت حمایت جمهوری اسلامی، یکی از مقرهای حزب‌الله را در ضاحیه بیروت به طور دقیق هدف قرار داده است.
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/14811" target="_blank">📅 16:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14810">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">الحدث به نقل از منابع:
علی الحاج، فرمانده حزب‌الله، در حمله هوایی اسرائیل به حومه بیروت ترور شد
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/14810" target="_blank">📅 16:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14809">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خبر ترور ‌نعیم قاسم تایید نشده است منتظر تایید هستیم @withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/14809" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14808">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کانال های امنیتی: فرماندهی موشکی هوافضا ایران در حال آماده سازی یک حمله گسترده
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/14808" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14807">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">موسوی، سخنگوی پیشین هیات رئیسه مجلس:
هدف حمله امروز اسرائیل به ضاحیه بیروت در روزی که قرار بود توافق امضا بشه، تحقیر جمهوری اسلامی بود.
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/14807" target="_blank">📅 16:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14806">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فاکس نیوز به نقل از  دیپلمات شرکت‌کننده در مذاکرات:
حملات امروز بیروت مانع از نهایی شدن توافق شده‌اند
این یک تلاش آشکار اسرائیل برای خراب کردن توافق رئیس‌جمهور و کشاندن مجدد ایالات متحده به جنگ است
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/14806" target="_blank">📅 16:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14805">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUPiezQJk8Kb_qlPbrzPGJsYffdWRmN02Jl0UBttYG8lGvCXU_g8jGtjFCr7nHI0vCsAzBgdNcD5ovTYlzE-WV2AFSKp45k-wVrlW_4jBJfC0kHHtAkQqQ4XPjp2E35REcLEk3kixJ2R9bDhWCLavL_DvWFeeYu9xaGxT9zXo9pnBxYMBBpfT-0723fqDqWlEBGCSb6W7SbKkhRTRDFiB-9OFjgw0Ao09QKz54fWVrzMj9qCNz5AA1N83hJV6zkOCDl2hNBhXQoxo4Y2A9YueFvddjSG9lBZtCfnlL6aEjnNY_msqTgRw4k48bjjgcjjUQsEEBhNAmoAzAzQbUe64A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد بزرگ شطرنچ نتانیاهو اول تصویری از حمله به بیروت رو منتشر کرد و تو پست بعدی تولد ترامپ رو تبریک گفت :
@withyashar
😁</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/14805" target="_blank">📅 16:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14804">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/14804" target="_blank">📅 16:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14803">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/14803" target="_blank">📅 16:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14802">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/14802" target="_blank">📅 16:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14801">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">قرارگاه خاتم: پاسخ کوبنده میدیم
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/14801" target="_blank">📅 16:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14799">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فاکس‌نیوز: یک دیپلمات حاضر در روند مذاکرات گفته حمله اسرائیل به بیروت فعلاً توافقات رو به گره انداخته و به همین خاطر امضای توافق تا این لحظه انجام نشده.
@withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/14799" target="_blank">📅 16:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14798">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبر ترور ‌نعیم قاسم تایید نشده است
منتظر تایید هستیم
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/14798" target="_blank">📅 15:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14797">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کانال ۱۲ اسرائیل به نقل یه مقام امنیتی: حتی یه موشک از سمت ایران پرتاب بشه، با حمله‌ای گسترده به اونا پاسخ میدیم و آماده هر سناریویی هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/14797" target="_blank">📅 15:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14795">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/14795" target="_blank">📅 15:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14794">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خبرگزاری رسمی اسرائیل: حمله به حومه جنوبی بیروت توسط دو هواپیمای جنگی انجام شد که چهار موشک هدایت‌شونده شلیک کردند.
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/14794" target="_blank">📅 15:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14793">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syJhEzGx5KT_D16EZ85bfUnsDgkyHl0o1-5iQrNSGHCwQ-mvqg59bsumxTkTcwi-v3Ym3_8d0FTDKnKU2xfSy9AB53HyPSvqu7dHprDQqCvpIgT65FRo0OZFcWPqtp4Od-_c7h-gsRcFzcXcOOuiuidfGySyL1rXXUhnxdugfWzcdHnLgeIlNk0pP1jx81Pt6kFwoCF8MPUYut5oAg7fWTLwXXbG8fENOjCX3bXScQdwW6QR9RnWpBJfNRn6RGWxIUhRL5hA3DkULZMtqtktuG8Ws76AsMdmRu2PVWDRa0aa8CgMJZCE6SiXnq45wrfpirWtsI3f8EC0dPieLKaFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصفهان دید از ملک شهر الان
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/14793" target="_blank">📅 15:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14792">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خبرنگار صداوسیما: تنگه هرمز طبق اعلام نهاد مدیریت آب‌راه خلیج فارس تا اطلاع بعدی همچنان مسدود است و هیچ کشتی خارجی حق ورود و خروج ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/14792" target="_blank">📅 15:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14791">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">العربیه: قطری ها و پاکستانی ها فشار زیادی می‌آورند تا تشدید تنش رخ ندهد!
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/14791" target="_blank">📅 15:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14790">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f830c996b.mp4?token=FSS6-p_jM7fM1-rkCIU-q0tsYg7UEB7mX-viD1pVf8yvMV5Oxoy6bZqBZXPDKRvgTB6iUbNtULl5NZ1clnVPtIk9aaBh7nxaNs00Qt46CVDofyqREpOREBwtDv37fIxZ5WF_bZQ11orqMtnKA7Yf8pN6qc_PUfLYdmvbuojpCDQNCJbZd-nSJXw8qZt7jQduFMy3MlqJxdujJ_oI64kyb3LoB2zkf-s_HPsq65iLW6Y2vGAqhkBo-ZDJvj--aiganBfu8B5fEJzvSF8dt-_gjyMmMzwASEz9CaBo4rPwAPR5ofoCgWogZDHkIfmra5urIX8NfGtRPWSRWQFbULHjdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f830c996b.mp4?token=FSS6-p_jM7fM1-rkCIU-q0tsYg7UEB7mX-viD1pVf8yvMV5Oxoy6bZqBZXPDKRvgTB6iUbNtULl5NZ1clnVPtIk9aaBh7nxaNs00Qt46CVDofyqREpOREBwtDv37fIxZ5WF_bZQ11orqMtnKA7Yf8pN6qc_PUfLYdmvbuojpCDQNCJbZd-nSJXw8qZt7jQduFMy3MlqJxdujJ_oI64kyb3LoB2zkf-s_HPsq65iLW6Y2vGAqhkBo-ZDJvj--aiganBfu8B5fEJzvSF8dt-_gjyMmMzwASEz9CaBo4rPwAPR5ofoCgWogZDHkIfmra5urIX8NfGtRPWSRWQFbULHjdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل به فارسی با انتشار این گیف از ظریف نوشت:
هفته خوبی داشته باشید
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14790" target="_blank">📅 15:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14789">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">منابع عبری: ارزیابی‌های کنونی در اسرائیل نشان می‌دهد که ایران تعادل را حفظ کرده و به حمله در حومه جنوبی بیروت پاسخ خواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/14789" target="_blank">📅 15:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14788">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مقام اسرائیلی به نیویورک تایمز :
توافق آمریکا و ایران آخر بازی نیست و هنوز ماجرا ادامه داره
ما از آمریکا خواستیم تو محدود کردن عملیات نظامی‌ تو لُبنان دخالت نکنه
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/14788" target="_blank">📅 14:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14787">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سخنگوی آتش نشانی تهران: دود مشاهده در قسمت شمالی شهر تهران، مربوط به حریق فضای سبز در محدوده ولنجک است.
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/14787" target="_blank">📅 14:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14786">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b57768c317.mp4?token=u-059AOxUDnuGM5C-UN9R01NL0FfyBGsUlQwZt7vIz2csLQ6LIT66zlCcCFc3SH1bS8AdWqvBQM98__RG4O59V0rhXZWwT5tByhdIKyT41i81Cv4qMG-mGJ0PoSGEAvUh8VssHOC36HUvhcbZ3vaK3TZaQHOS2kvpwef7cvyzR61GYVEL8hpY5DrC8jUGJpsNT1p8RmrpM5XcoW3LZ5wg--zQvuzoOYmb3f0chmGjUam7aLj25yGeVCwoEA-XIN9gw_SS1R1w59DHDhMUOlLsr_LYBmxdQSb6-Zb4ELZpksB00H2FyWVUiCXE-5DnkHzabpM2Nsdh2bhVU6wsj3W5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b57768c317.mp4?token=u-059AOxUDnuGM5C-UN9R01NL0FfyBGsUlQwZt7vIz2csLQ6LIT66zlCcCFc3SH1bS8AdWqvBQM98__RG4O59V0rhXZWwT5tByhdIKyT41i81Cv4qMG-mGJ0PoSGEAvUh8VssHOC36HUvhcbZ3vaK3TZaQHOS2kvpwef7cvyzR61GYVEL8hpY5DrC8jUGJpsNT1p8RmrpM5XcoW3LZ5wg--zQvuzoOYmb3f0chmGjUam7aLj25yGeVCwoEA-XIN9gw_SS1R1w59DHDhMUOlLsr_LYBmxdQSb6-Zb4ELZpksB00H2FyWVUiCXE-5DnkHzabpM2Nsdh2bhVU6wsj3W5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل: مرکز فرماندهی حزب‌الله تو ضاحیه بیروت رو زدیم
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/14786" target="_blank">📅 14:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14785">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کانال ۱۲ اسرائیل: هدف حمله هوایی در ضاحیه جنوبی، فرمانده ارشد در سیستم ارتباطات حزب‌الله بود
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/14785" target="_blank">📅 14:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14784">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اتاق جنگ با یاشار : این موج مکزیکی بلند رو مدیون بی بی هستیم
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/14784" target="_blank">📅 14:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14783">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رسانه های اسرائیلی از اماده باش کامل ارتش اسرائیل برای حمله احتمالی ایران خبر می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/14783" target="_blank">📅 14:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14782">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بیانیه نتانیاهو و کاتس: ارتش اسرائیل اهدافی متعلق به حزب‌الله در ضاحیه جنوبی را هدف حمله قرار داد
زیرساخت‌های حزب‌الله در ضاحیه جنوبی را با دقت هدف قرار دادیم
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/14782" target="_blank">📅 14:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14781">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شبکه ۱۴ اسرائیل : ما جشن تولد ترامپ رو امروز تو بیروت جشن گرفتیم!
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/14781" target="_blank">📅 14:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14780">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پنج ساختمان در بیروت مورد حمله  هدفمند قرار گرفته اند!
@withyashar
🚨</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/14780" target="_blank">📅 14:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14779">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کانال ۱۲ اسرائیل: هدف در حمله به ضاحیه جنوبی نعیم قاسم بوده است
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/14779" target="_blank">📅 14:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14778">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اتاق جنگ با یاشار :  سفت بگو یا موسییییییییی
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/14778" target="_blank">📅 14:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14777">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ارتش اسرائیل: حزب‌الله با نقض آتش‌بس، سه موشک به سمت شهرهای شمالی اسرائیل شلیک کرد و ما در پاسخ به بیروت حمله کردیم
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/14777" target="_blank">📅 14:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14776">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79c0e7c974.mp4?token=ll3HiMoVUuRAujAmv1fhoQe4yE3Tbl86mSCmWbIkeqizSbybTMkzharenBBeRfwR5D9OLB18GxuPtratw1hs9-5G8PJQFpCZPEe55t7-alnWY9aNTv_r03VN8jUXXVKIX8Caxz0_C9_G4zU_VAcTz9L9ly5swgbCQ3XY1ssIGn8oI9ZA9EPJqep9223QGZVp72DDXGramGbcfqLB2vsdtjCpUgKwcdKOhkaz1Uq9SDmItoQs0IkinrFLRB74IleMdnxtLLYdVf3B73p9HZWn2U7MKBNYay7z_HPrBOLnVS64o9iqL13pSFbiEOZR-wm0IDH2G3Z-6yX8GLC8RXCZZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79c0e7c974.mp4?token=ll3HiMoVUuRAujAmv1fhoQe4yE3Tbl86mSCmWbIkeqizSbybTMkzharenBBeRfwR5D9OLB18GxuPtratw1hs9-5G8PJQFpCZPEe55t7-alnWY9aNTv_r03VN8jUXXVKIX8Caxz0_C9_G4zU_VAcTz9L9ly5swgbCQ3XY1ssIGn8oI9ZA9EPJqep9223QGZVp72DDXGramGbcfqLB2vsdtjCpUgKwcdKOhkaz1Uq9SDmItoQs0IkinrFLRB74IleMdnxtLLYdVf3B73p9HZWn2U7MKBNYay7z_HPrBOLnVS64o9iqL13pSFbiEOZR-wm0IDH2G3Z-6yX8GLC8RXCZZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به بیروت
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/14776" target="_blank">📅 14:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14775">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بیانیه مشترک نتانیاهو و کاتز:
ارتش اسرائیل اکنون در پاسخ به شلیک حزب‌الله به سمت اراضی اسرائیل، اهداف متعلق به سازمان حزب‌الله را در بیروت مورد حمله قرار می‌دهد. اسرائیل با شلیک به سمت اراضی‌اش مدارا نخواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/14775" target="_blank">📅 14:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14774">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یک مقام ارشد ایرانی به رویترز: آمریکا موافقت کرده است که ایران اورانیوم غنی‌شده را در داخل خاک ایران رقیق کند
@withyashar</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/14774" target="_blank">📅 13:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14773">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43d5bc7f03.mp4?token=VGvwGg8653WT3d82taBj_dJqgeu-8QdiDj7l4JAGeJ9HvFK74y7_Z0NhUZIgWtNMFrIe51EVSHkImfD9H1fGoI9erdzGNOzqH-UDOuQGDQIxEr2rgfqxSotfwiikMj1doX1kxi2WDjc7Pky6UoPg5DyN80MQFVxDJvTXOhnW2U-2cFL8U7uG1mEgb_yRFjNLwRPAk-kNfW7JF-KSA8dmeO0kq1IFxR4KiQHzgLFuMVv2e2j7uGP7A81zpMGZZ4V4MKWMsdsP7ppPJ3e0ru4jhYczf6HaItgFqo-IrepOVKBC6LfWTfyd6Nj8fWNrdlQwaBgu6L9an0uzBw067CFkMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43d5bc7f03.mp4?token=VGvwGg8653WT3d82taBj_dJqgeu-8QdiDj7l4JAGeJ9HvFK74y7_Z0NhUZIgWtNMFrIe51EVSHkImfD9H1fGoI9erdzGNOzqH-UDOuQGDQIxEr2rgfqxSotfwiikMj1doX1kxi2WDjc7Pky6UoPg5DyN80MQFVxDJvTXOhnW2U-2cFL8U7uG1mEgb_yRFjNLwRPAk-kNfW7JF-KSA8dmeO0kq1IFxR4KiQHzgLFuMVv2e2j7uGP7A81zpMGZZ4V4MKWMsdsP7ppPJ3e0ru4jhYczf6HaItgFqo-IrepOVKBC6LfWTfyd6Nj8fWNrdlQwaBgu6L9an0uzBw067CFkMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا سیما
: پاکستانی‌ها برای میانجی‌گری به ایران نمی‌آیند، بلکه مرتب پیام تهدید و‌ ترور می‌آورند
!
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14773" target="_blank">📅 13:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14772">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">صندوق سرمایه گذاری عمومی قطر اعلام کرده بعد از گلی که دیروز بوعلام خوخی در دقیقه‌ی ۹۵ به سوئیس زد ۳ میلیون دلار به همراه یه رولز رویس فانتوم آخرین مدل به ارزش ۵۵٠ هزار دلار پاداش خواهد گرفت!
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14772" target="_blank">📅 13:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14771">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فرمانده مرزبانی آذربایجان‌غربی اعلام کرد حسین رسولی ستوان سوم نیروهای مرزبانی هنگ مرزی چالدران در جریان درگیری با نیروهای پ.ک.ک كشته شده است. PKK مخفف نام کردی ‌به معنی (Partiya Karkerên Kurdistanê)
«حزب کارگران کردستان»
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14771" target="_blank">📅 12:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14770">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzxnHO4lGISlFf74QfRnHufDHvkYAQwnUpdBjMTLuYzITuzGe_Vr2Wt_ho6y_EszyC_hCk98YTTCrLpfTlyQCpTvg5_oqMNQC-9S5tT93SssG4YLVrYkS1qGpod9b6YGDNe76prDtW_r1-3kXRwcH_vlVcXSXjFofVePRIqrCBUI-pn6B1PpVj9OE_WTxJIc8LCEunieua697pGCEv0Oe9uGYlmCYTKNWJdOYapsIX3BmvQ-dtgl7ZUvulJppH2hTxImbSDTFCVlku2OPYk4ZHRV9Zqq-XRBI-jiOMONKY7MAMNPdGX7y7HPH8PZV1gtj1o-7aywZQsEMLmFCLCdqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی‌ها: تا مجتبی خامنه‌ای نیاد جلو دوربین و نگه از خون بابام و خانوادم گذشتم، ما این توافق رو قبول نمیکنیم
@withyashar
🤣</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14770" target="_blank">📅 12:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14769">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">صدای انفجار ناشی از مهمات عمل‌نکرده در غرب تبریز
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14769" target="_blank">📅 12:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14768">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14768" target="_blank">📅 12:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14767">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14767" target="_blank">📅 12:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14766">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d0048bfa4.mp4?token=X5PecJ3pQ6fXvkm978GOeMmXjEls2PUd3elI6qOVtx-c6vFTWbXo8bn7YNM82XbTgvhTRZy0IpmRJvYT1dUhHilt5cqfIJbLAQOqTIaak7Gm5Gx9y8g8Z2kY6Beh32ZOSnEHwjbuxXBr3xVM4XJs00hJf18DsNBrVtGT5o0PRcaBjBBOmtUo57Lx6bmtFRekSrHflCeS_GQPOymB-sxWgJEkva3ugl9PefeargoPjN2_PINGb0kzUltJ_Dhxho-XcHn4Hi4HAwbonmUQrHpRYZQ5c6-g8QTdOW5AxdBhc0yNe6K1c2sDE5WjZ7-1kr-h9mx8kguSx9_cqUxKDHU5Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d0048bfa4.mp4?token=X5PecJ3pQ6fXvkm978GOeMmXjEls2PUd3elI6qOVtx-c6vFTWbXo8bn7YNM82XbTgvhTRZy0IpmRJvYT1dUhHilt5cqfIJbLAQOqTIaak7Gm5Gx9y8g8Z2kY6Beh32ZOSnEHwjbuxXBr3xVM4XJs00hJf18DsNBrVtGT5o0PRcaBjBBOmtUo57Lx6bmtFRekSrHflCeS_GQPOymB-sxWgJEkva3ugl9PefeargoPjN2_PINGb0kzUltJ_Dhxho-XcHn4Hi4HAwbonmUQrHpRYZQ5c6-g8QTdOW5AxdBhc0yNe6K1c2sDE5WjZ7-1kr-h9mx8kguSx9_cqUxKDHU5Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترافیک کشتی‌ها در تنگه هرمز طی ۲۴ ساعت گذشته که با استفاده از اطلاعات سیستم شناسایی خودکار (AIS)
قابل مشاهده است، نشان می‌دهد که هیچ کشتی‌ای با استفاده از طرح جداسازی ترافیک ایران عبور نکرده است؛ با این حال، چند کشتی از طریق آب‌های عمان در امتداد مسیر امن پروژه آزادی که قبلاً ایجاد شده بود، عبور کرده‌اند.
همچنین مشاهده گشت زنی دو شناور نظامی آمریکایی در تنگه هرمز ، البته نوع این شناورها مشخص نیست
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14766" target="_blank">📅 11:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14765">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">منابع مطلع به شبکه «العربیه» : هیئت‌های نمایندگی آمریکا و ایران به منظور امضای نهایی توافق صلح، در یک نشست مجازی (ویدیویی کنفرانس) حضور خواهند یافت. یادداشت تفاهم صلح در جریان این نشست آنلاین با نظارت مستقیم میانجیگرانی از کشورهای پاکستان و قطر با حضور «جی‌دی ونس» (نماینده آمریکا) و «محمدباقر قالیباف» (نماینده ایران) به امضا خواهد رسید. بلافاصله پس از امضای این توافقنامه، محاصره بنادر ایران لغو خواهد شد. از دیگر نکات، بازگشایی تنگه هرمز و صدور مجوز عبور و مرور برای کشتی‌ها بدون نیاز به پرداخت هیچ‌گونه عوارض عبور خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14765" target="_blank">📅 11:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14764">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رسانه‌های کشورهای خلیج فارس: جلسه مجازی نمایندگان آمریکا و ایران با حضور واسطه‌هایی از پاکستان و قطر امروز انجام خواهد شد
در این جلسه مجازی آنلاین، یادداشت تفاهم با حضور ونس و قالیباف دیجیتال امضا خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14764" target="_blank">📅 10:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14763">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سی‌ان‌ان: مذاکره‌کنندگان قطری برای نهایی کردن تفاهم راهی تهران شده‌اند
شبکه آمریکایی به نقل از یک منبع مدعی شد که مذاکره‌کنندگان قطری صبح امروز در هماهنگی با ایالات متحده به سوی تهران پرواز کرده‌اند تا به تسهیل روند نهایی‌سازی توافق (یادداشت‌تفاهم) بین ایران و آمریکا کمک کنند
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14763" target="_blank">📅 10:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14762">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">الجزیره: جمهوری اسلامی هنوز تصمیم نهایی خودشو درباره تفاهم‌نامه رو اعلام نکرده.
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14762" target="_blank">📅 09:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14761">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فاکس نیوز به نقل از یک مقام بلندپایه در دولت آمریکا: معتقدیم به توافقی عالی و بسیار مستحکم دست یافته‌ایم
ایران تنگه هرمز را بدون دریافت هزینه مجدداً باز خواهد کرد
محاصره آمریکا هم‌زمان با بازگشایی تنگه هرمز لغو خواهد شد.
مرحله بعدی بر عملیات مین‌روبی در تنگه هرمز متمرکز خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14761" target="_blank">📅 09:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14760">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a7ce7d92b.mp4?token=hMRM69rxbpof4GlB4n-wqa3mb3AhSbUxFNgDD7pBbt7x9hA6YNs536R7bR0D7yJUAO8K4_x2DpEJ3SItxtPPalnWFAmh4TxR8JodRPMMcI_blXdSN7XG5twRzeHOEvHlHY67WIr4h3I-rsWCumuq7hUynDfgKgIt5XeG3Pl0cgLGPIGl-qmMliLo2F4DRKDGASY2VzzOo51Y4EleUP0356EtYQm9MtUEUQEN-UR7ZYnEFneO0A9WbCHad58R7WsBIpHvhpvokTU1NYLb9BQg5DMGPMmAsQ9_m0DagWywhZK2hWg-BOM_9XiaQuqaXP3JUtoa3nblZF3Uy7GCB77hBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a7ce7d92b.mp4?token=hMRM69rxbpof4GlB4n-wqa3mb3AhSbUxFNgDD7pBbt7x9hA6YNs536R7bR0D7yJUAO8K4_x2DpEJ3SItxtPPalnWFAmh4TxR8JodRPMMcI_blXdSN7XG5twRzeHOEvHlHY67WIr4h3I-rsWCumuq7hUynDfgKgIt5XeG3Pl0cgLGPIGl-qmMliLo2F4DRKDGASY2VzzOo51Y4EleUP0356EtYQm9MtUEUQEN-UR7ZYnEFneO0A9WbCHad58R7WsBIpHvhpvokTU1NYLb9BQg5DMGPMmAsQ9_m0DagWywhZK2hWg-BOM_9XiaQuqaXP3JUtoa3nblZF3Uy7GCB77hBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/14760" target="_blank">📅 02:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14759">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8785098a7.mp4?token=rvGvicw8jl5aNnttjPrRVjBsXpv9U25MsLUSKRsnRxgHFAC9MQCY2z-GDGejVkD6k5YNQaY_b_-u4cyJo-Oq8P65Xh7ZWx3RKulXaKW8hqxnTPXUBwMioNMTpvsKqe9HhHKSo3_uYQ9frMJlNDgaDXVP_Cyxd4Zkln5Dzo0IjwfirrD1shdCTWyoh8uMyQe7uC24dJ-IkuChFapjDXyGJdEFRIomKgQj-ArUVemWo9yDLWf4uumO07ypJmAzXoSX7ECGdLvp8edU0oY0zPfPgDI0W1my_hIe0Ta0COm1u5rhr-Kb9OGSUy30Ruv1JA83d2NNwNI8k-QisDVmHEFfXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8785098a7.mp4?token=rvGvicw8jl5aNnttjPrRVjBsXpv9U25MsLUSKRsnRxgHFAC9MQCY2z-GDGejVkD6k5YNQaY_b_-u4cyJo-Oq8P65Xh7ZWx3RKulXaKW8hqxnTPXUBwMioNMTpvsKqe9HhHKSo3_uYQ9frMJlNDgaDXVP_Cyxd4Zkln5Dzo0IjwfirrD1shdCTWyoh8uMyQe7uC24dJ-IkuChFapjDXyGJdEFRIomKgQj-ArUVemWo9yDLWf4uumO07ypJmAzXoSX7ECGdLvp8edU0oY0zPfPgDI0W1my_hIe0Ta0COm1u5rhr-Kb9OGSUy30Ruv1JA83d2NNwNI8k-QisDVmHEFfXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توافق دیجیتال فردا
@withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/14759" target="_blank">📅 02:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14758">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دوبار تنگه دعوا شده !
🚨
🤣
@withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/14758" target="_blank">📅 01:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14757">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">قشم صدای انفجار‌
🚨
احتمالا از سمت تنگه
@withyashar</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/14757" target="_blank">📅 01:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14756">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">عبداللهی، سردبیر خبرگزاری تسنیم:
احتمال توافق نهایی با آمریکا بسیار بسیار ضعیفه؛ باید برای حمله ناگهانی آماده بود.
@withyashar</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/14756" target="_blank">📅 00:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14755">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پست جدید کلیک کنید کارای‌ اداریش رو انجام بدید
😁
✌🏾
https://www.instagram.com/reel/DZimqXCxxza/?igsh=Z3lhb2FhYWhlc2Yz
بسیجی‌ در ‌برابر سرکوبگر برنامه امشب خیابان های‌ تهران
🥴
استقبال زیاد باشه بازیشو میسازم
🤣</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/14755" target="_blank">📅 00:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14754">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به وای نت:
این یک توافق بد است. هیچ‌کس از آن راضی نیست. آنها می‌فهمند که این برای ما خوب نیست و به منافع اسرائیل آسیب می‌زند.
چیزی که نگران‌کننده است این است که اسرائیل نمی‌تواند تأثیر بگذارد و صدایش شنیده نمی‌شود.
این عمدتاً یک «توافق جام جهانی-جشن‌های ۲۵۰ سالگی تولد ۸۰ سالگی ترامپ» است.
هدف این است که برای همه رویدادهای بزرگ فعلی در آمریکا کمی آرامش بخرد. واقعاً چیزی نیست که دوام بیاورد.
@withyashar</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/14754" target="_blank">📅 00:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14753">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/14753" target="_blank">📅 00:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14752">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اتاق فایت با شما : میدون ابن سینا درگیری شده
بین مامورا و تند روهاااا
میدون ابن سینا رو کامل بستن
@withyashar</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/14752" target="_blank">📅 00:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14751">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/14751" target="_blank">📅 00:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14750">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نبویان: آمریکا پیروز شد
@withyashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/14750" target="_blank">📅 00:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14749">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Myh51bbzvFt-K-gY_v944doAP7vndijJ-DWR4iasURBpwcdggvgyIUtQinT8Rs9m-01pHqoqRIhNf4wx6328IbZh9QFRHuc_Z7dzLgqdPnOi6x0qM5ocmz4oP42b5ZAm2F7KPakxTTDzuBPzjRRcNyfrLFE6QkNyDkXfB2Kn9WwJwgKor-e8EBzcfrNy4t3Qu1hdKE4YgX1y5Bg3Mb8tIQpjbj8gQtLTSgn2Osc14IP931v1hmvZUJKoRjSwblXEjYFdE-29obwtiQkTQDGNQu_Xc4XcjugfGaKW4lI_8guRi8xvlUfH6e4Z7RcOsxC7lekXqkTrEDHfLlKofPDS2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوخت رسان ها از تلاویو بلند شدند
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/14749" target="_blank">📅 23:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14748">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ظریف:
این جماعت مخالف توافق عده‌ای نفهم هستند که هیچ درکی از واقعیت ندارند.
@withyashar</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/14748" target="_blank">📅 23:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14747">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
اطرافیان نتانیاهو می‌گویند: نگرانی بزرگ این است که ترامپ در بحث توافق با ایران، با ما همان کاری را بکند که اوباما با ما کرد.
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/14747" target="_blank">📅 23:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14746">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">«زمان تنها خدای واقعی است»
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/14746" target="_blank">📅 23:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14745">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/14745" target="_blank">📅 23:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14744">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/14744" target="_blank">📅 22:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14743">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/14743" target="_blank">📅 22:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14742">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/14742" target="_blank">📅 22:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14741">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رسانه های آمریکایی: مراسم تشییع سید علی خامنه ای رهبر سابق جمهوری اسلامی ایران در روز 4 جولای، زمانی که آمریکا روز استقلال را جشن می گیرد، برگزار خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/14741" target="_blank">📅 22:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14740">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">الان روبیکا ، بله و سروش فیلتر‌ میشه
😂
@withyashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/14740" target="_blank">📅 21:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14739">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شورای هماهنگی بانک‌های دولتی:
اختلال در سامانه‌های چهار بانک ناشی از یک حمله سایبری محدود بوده، اما هیچ‌گونه نشت اطلاعات یا دسترسی غیرمجاز به داده‌های مشتریان رخ نداده است
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/14739" target="_blank">📅 21:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14738">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مقام ارشد اسرائیلی به کانال ۱۲ اسرائیل: این یه توافق مزخرفه
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14738" target="_blank">📅 21:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14737">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مردم طرفدار حکومت اعتراضاتی رو در چند استان شروع کردند @withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/14737" target="_blank">📅 21:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14736">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کارشناس شبکه افق:به زودی جنگ را به خاک آمریکا می‌بریم و دیگر قرار نیست در خاک خودمان با دشمن بجنگیم جمهوری‌ اسلامی هنوز کارت های خود را رو نکرده
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14736" target="_blank">📅 21:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14735">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb7b47099c.mp4?token=KXDOVa-mA9V5eo8d8S6PLZ-Im8RPO9LeKiJ3nIzyPLDDNlj4o7_sNnyCtVgX0hnKeVaep1gJg-6PxCrISNMgYHNsq8YTmZvKk8-MPKiLYsOt56K-nNCLL-vbfcBC4yV2fy73sX7h_cIzbJ8MafVwr1ZwAuCXi6vE3iIf8FrMe5d7EXtkYSQ5L4rFs78rTp0nwxb77fHEOEHDPTsGmSWj8qWBIWWkRMF8IWOC4fh-6VSzsB-6sotbTg_OT3wjU8snOREEJV1DqXhu6-RTw6SegDLiHTbWeXuPk0xAfrHPqLE_hGcenvp0wE52Gu1XaoFPOrhpocWV0pwTRE0f3JZYoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb7b47099c.mp4?token=KXDOVa-mA9V5eo8d8S6PLZ-Im8RPO9LeKiJ3nIzyPLDDNlj4o7_sNnyCtVgX0hnKeVaep1gJg-6PxCrISNMgYHNsq8YTmZvKk8-MPKiLYsOt56K-nNCLL-vbfcBC4yV2fy73sX7h_cIzbJ8MafVwr1ZwAuCXi6vE3iIf8FrMe5d7EXtkYSQ5L4rFs78rTp0nwxb77fHEOEHDPTsGmSWj8qWBIWWkRMF8IWOC4fh-6VSzsB-6sotbTg_OT3wjU8snOREEJV1DqXhu6-RTw6SegDLiHTbWeXuPk0xAfrHPqLE_hGcenvp0wE52Gu1XaoFPOrhpocWV0pwTRE0f3JZYoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم طرفدار حکومت اعتراضاتی رو در چند استان شروع کردند
@withyashar</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/14735" target="_blank">📅 21:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14734">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رادان : هرکس در تجمعات علیه وحدت ملی و مذاکرات شعار یا حرفی بزند بعنوان تفرقه‌افکن باهاش برخورد میکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14734" target="_blank">📅 21:38 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
