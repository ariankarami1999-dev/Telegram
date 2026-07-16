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
<img src="https://cdn4.telesco.pe/file/p-hI0ly1lm7c1VTKhaMth0gzLXHUlV2A-BH9E1cVMZJK35nMFBEVenufJqyVytgmMiKiMhSZw-8PipeW0OL4AsvSVTv4DKHUa4RDSIxQCltaRSvTzgS_mK-Y_kttN_AMOMJgVfwjnaLvbwxmhK7t1rDAj2_jZRvwg05tfLR6AyFWyXuz17WZhZo_F_84oiu7uPfagKdlVb0YlG3Ot02ftgh_xjncFzG_IMKxnVuggt2plHyAvbNfbzX9HElO_Cmu7UKR-tRxw6i4kf0iuOQn1DKAVvChCu1ER4wvWlxjZQvUhQruY2DltzEUVWSErjShU8GgIe0tNHUhTPsuuDBAbw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 395K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 12:08:39</div>
<hr>

<div class="tg-post" id="msg-18351">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کانال الاخباریه سوریه، وابسته به رژیم جدید این کشور، از منبعی در وزارت کشور در دمشق گزارش داد که «یگان‌های ویژه، تلاش برای قاچاق محموله‌ای از سلاح‌های پیشرفته و موشک‌ها از طریق مرز با عراق را خنثی کردند.» به گفته این منبع، «تحقیقات اولیه تأیید می‌کند که محموله توقیف شده قرار بوده از طریق خاک سوریه به حزب‌الله منتقل شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/withyashar/18351" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18350">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بیانیه جمع کثیری از ساکنان جنوب به اتاق جنگ :  ما ايرانيان ساكن جنوب
كشور، ترحم نمى خواهيم؛
ايرانى بدون جمهورى اسلامى
مى خواهيم.
@WarRoom</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/withyashar/18350" target="_blank">📅 11:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18349">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbdd26b83a.mp4?token=u-i3qTVBf5rd89R59P-UIiDGjADY1FGseTgE-BbO_cQi-Hm2LFFq0a7twF0vgvsAninfFep5USHtMt-FAOxBk5aRimfHkz5COCqIaM7LriLulOJdOXV6kc-_UXyV4iNgFXHTCJIjK3RvmSaeysJKBzRRb4Ti_sS98DNHvSZpronc_CT56NQGTZ14J1xGtS_UnTeeNOtvj86oDF3vvQUGHWXzlL6WlosjQaenyuFYl85r9qplCcI-_f3P9qNcY_ti2oA_YVG4IVIRpDd-FKEjyuCYT8Bq-EItcVnqBDlwrPT3gDf029x7CwYQK7Z1CLVzrbEw6uNUleotnSZrA2B_81Ttp9dy4G2UKBjMm0evgodVHwGuiFWSVXd3wPb2r0v6hW8VSkT9NU21Iywt0UWLwcvlVgYq-XhXRInYyyt5kH4aXWduu8wfkCWJV11QpRYQRYU8fJ-rNf93vaA0P3fxJO8_Jr33fKZduCE0Oqrtcky9zexXzpPhp6s6KeZkskHa1B5XIc6q-yr3UBMMjeJLLjX5vCRYns0wdNU777gse_KZGcLNmfPpterR5qCji4ujgiUK_2P2ZeR3tQlXdxwvit_2pkM27N0-NazQUl1brJFVtea3qHEFsN3TGFxdX0vH_fRC1cih-1joL2vctDGwPriRdqM_gFdeVuEvld1dM1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbdd26b83a.mp4?token=u-i3qTVBf5rd89R59P-UIiDGjADY1FGseTgE-BbO_cQi-Hm2LFFq0a7twF0vgvsAninfFep5USHtMt-FAOxBk5aRimfHkz5COCqIaM7LriLulOJdOXV6kc-_UXyV4iNgFXHTCJIjK3RvmSaeysJKBzRRb4Ti_sS98DNHvSZpronc_CT56NQGTZ14J1xGtS_UnTeeNOtvj86oDF3vvQUGHWXzlL6WlosjQaenyuFYl85r9qplCcI-_f3P9qNcY_ti2oA_YVG4IVIRpDd-FKEjyuCYT8Bq-EItcVnqBDlwrPT3gDf029x7CwYQK7Z1CLVzrbEw6uNUleotnSZrA2B_81Ttp9dy4G2UKBjMm0evgodVHwGuiFWSVXd3wPb2r0v6hW8VSkT9NU21Iywt0UWLwcvlVgYq-XhXRInYyyt5kH4aXWduu8wfkCWJV11QpRYQRYU8fJ-rNf93vaA0P3fxJO8_Jr33fKZduCE0Oqrtcky9zexXzpPhp6s6KeZkskHa1B5XIc6q-yr3UBMMjeJLLjX5vCRYns0wdNU777gse_KZGcLNmfPpterR5qCji4ujgiUK_2P2ZeR3tQlXdxwvit_2pkM27N0-NazQUl1brJFVtea3qHEFsN3TGFxdX0vH_fRC1cih-1joL2vctDGwPriRdqM_gFdeVuEvld1dM1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این به من قدرت میداد که در مقابل  حوادث و اشکالات هیچوقت خم نشوم
@WarRoom</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/withyashar/18349" target="_blank">📅 11:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18348">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWNmiDrqwHTZx08S4bbAvSZstbrl6c5UG_O6XFc3R42ASed7F8g0XYfpCoR0DHNQ-cXQ5UH7tlWWSW0op5gMQ2fQHmctPIMCvSGv2DbUqi0fuNTQ2fFoy0PL3e2UpHPUYI9kAB2WIJvqfiak2Pd91ioXeNXehfTxH4RWro93YcIyXS6wkMa1x1K09P00XHqYetvIVgWxZNd5NIFtSl0J8BIB1JVqIOTF7TKjfxMKPGQ8w76uKtbCLGElyKFhy7OlLN5DKketCcXoVuckCjgRpBF6AYSEy-_2aHOb49oxQzOcWDO5iylm-IlN_MNAA9BMZLfYKdcMigWSjyKGzmyGzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😁
@WarRoom</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/18348" target="_blank">📅 11:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18347">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارش های زیاد از‌ سر تا سر مازندران مبنی بر قطع شدن آنتن ایرانسل
@WarRoom</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/18347" target="_blank">📅 11:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18346">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نیروهای دفاعی بحرين: سامانه‌های پدافند هوایی، تعدادی از حملات هوایی خصمانه رژیم ایران را امروز شناسایی و خنثی کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/18346" target="_blank">📅 10:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18345">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کپلر: ۷ کشتی دیروز از تنگه هرمز عبور کردند که هیچ‌کدام نفتکش یا حمل‌کننده گاز نبودند.
@WarRoom</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/18345" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18344">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وزارت خزانه داری آمریکا؛ ۱۳۰ میلیون تتر دیگه از دارایی های ایران رو مسدود کرد!
جمع کل تترهای مسدود شده بانک مرکزی هم تو یک سال گذشته از ۱ میلیارد تتر عبور کرده...
@WarRoom
Tether = 189,000 T</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/18344" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18343">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اتاق جنگ با یاشار : ‏قرمساقا هر چی دلقک و لمپن و خالتور تو فضای مجازی بود رو بعنوانِ کارشناس آورد تو صدای آمریکا فقط و فقط برای اینکه به پهلوی حمله کنن، تهشم میگفت صدای آمريکا بیان کننده نظرات رسمی دولت آمریکاست!
@WarRoom
🤡</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/18343" target="_blank">📅 10:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18342">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اتاق جنگ با یاشار : تمامی کودکان بیمارستان سرطانی اهواز در سلامت کامل هستند و حدود دویست نفر آنها به مکان دیگری منتقل شدند. این بیمارستان هدف هیچگونه حملاتی نبود. فقط چون حملات بسیار سنگین بود در اهواز و در نزدیکی آنجا، مانند تمام نقاط دیگر و تمام کودکان آن شهر و دیگر شهرها، در آنجا هم بسیار احساس میشد در نتیجه سوژه خوبی برای پروپاگاندا رژیم قرار‌گرفت ، تمام کودکان ایران فرزندان ما هستند و دردشان درد ما ! مانند دانش آموزان ما که صدایشان شنیده نمیشود و باید به آنها هم توجه شود !
@WarRoom</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/18342" target="_blank">📅 09:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18341">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شهر هایی که دیشب مورد حملات ارتش آمریکا قرار گرفته اند
💥
اهواز
💥
بندرعباس
💥
جزیره قشم
💥
سمنان
💥
سیریک
💥
چابهار
💥
کرمان
💥
بوشهر
💥
همدان
💥
کنارک
💥
راسک
💥
خنداب
💥
پاکدشت(پدافندی)
گسترده تر شدن موج حملات ارتش آمریکا و حمله به شهر های مرکزی
@WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/18341" target="_blank">📅 09:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18340">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دفتر کاتس ،وزیر دفاع تأکید کرد که اسرائیل بر ماندن در مناطق امنیتی در سوريه، غزه و لبنان اصرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/18340" target="_blank">📅 09:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18339">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/18339" target="_blank">📅 09:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18338">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در درباره تهدیدهای مطرح‌شده از سوی ایران علیه جانش: «اصلا فکر نمی‌کند».
او در گفتگو با فاکس بیزینس تاکید کرد: «اگر به این مسائل فکر کنم، دیگر نمی‌توانم مؤثر باشم.»(۳دقیقه با زیرنویس)
@WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/18338" target="_blank">📅 09:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18337">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اطلاعیه سپاه  استان تهران درباره صدای شنیده‌شده در پاکدشت : عملیات پدافندی بود؛ هیچ اصابتی رخ نداده است
@WarRoom</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/18337" target="_blank">📅 09:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18336">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/18336" target="_blank">📅 08:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18335">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNarges</strong></div>
<div class="tg-text">وقتی صبح دیدم از ساعت ۲ هیچی نذاشتی، فکر کردم گرفتنت
😭
😭</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/18335" target="_blank">📅 08:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18334">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وزیر علوم: کنکور سراسری در زمان مقرر برگزار می‌شود
برای برگزاری آزمون، هماهنگی‌های لازم از تأمین برق حوزه‌های امتحانی تا هماهنگی‌های امنیتی، با دستگاه‌های مختلف انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/18334" target="_blank">📅 08:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18333">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مشاور رهبر در امور بین‌الملل: تنگه هرمز متعلق به ایران است و هیچ قدرتی در جهان نمی‌تواند حاکمیت ما را بر آن سلب کند.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/18333" target="_blank">📅 08:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18332">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فارس: آمریکا در حملات بامدادی خود نقاطی در کبودرآهنگ، استان همدان را هم مورد هدف قرار داد
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/18332" target="_blank">📅 08:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18331">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شب گذشته به فرودگاه سمنان / خنداب نیز حمله شده است
فارس ‌با تایید : سخنگوی ستاد بحران ناشی از جنگ استان سمنان: بامداد پنجشنبه، بخش‌هایی از فرودگاه سمنان هدف حملات هوایی دشمن قرار گرفت.
نیروهای دستگاه‌های امدادی در حال انجام اقدامات لازم پس از وقوع این حملات هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/18331" target="_blank">📅 08:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18330">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15343948c.mp4?token=bK-WnkGlnC-YVe0aGpTmR_w5_Hu56MAc6Jrw0aJxS2f-nxi6hZsJthjXcjPPXe2e3Ggn2VaNzzvDvT9_u1edkjDsZaIiMrEety543UiGSNOfMOaW6rrtbZurdYX4rsbo0O56uLmtorfq8w_zdFGuK09Pfd90goUwhbaoo7OfQnLKRtZCRJqaa0WMtCIR0mqedmU7dAnAiNwyLJ7XC77xz52t8vuy8ihXhezBDKFoyXfW6EMLO2ZYCOW5rLRX_XbGSC1CRRNSsWhjyBA8boqRb0T4vWxCWJJfkzvi7ZHWiac4rfQweudgm82jRB2tF9H4BohTZo_-H1dfns-H11YqiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15343948c.mp4?token=bK-WnkGlnC-YVe0aGpTmR_w5_Hu56MAc6Jrw0aJxS2f-nxi6hZsJthjXcjPPXe2e3Ggn2VaNzzvDvT9_u1edkjDsZaIiMrEety543UiGSNOfMOaW6rrtbZurdYX4rsbo0O56uLmtorfq8w_zdFGuK09Pfd90goUwhbaoo7OfQnLKRtZCRJqaa0WMtCIR0mqedmU7dAnAiNwyLJ7XC77xz52t8vuy8ihXhezBDKFoyXfW6EMLO2ZYCOW5rLRX_XbGSC1CRRNSsWhjyBA8boqRb0T4vWxCWJJfkzvi7ZHWiac4rfQweudgm82jRB2tF9H4BohTZo_-H1dfns-H11YqiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شب گذشته پدافند در شرق و غرب تهران فعال شد همچنین صدای انفجار در حوالی پارچین و پاکدشت شنیده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/18330" target="_blank">📅 08:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18329">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9Xlw51evGxdCvXbyS3EbMiMT0i_2Vz4cmiP99ANKV9TCIxDYHo9bmGt5fbAqA_61BikVbEd-6llw6HGDtvx1DYkIfs2EdyD0lVcF4xCxjp6rFZJhWnIFho5LfPrDV6MEd67sSqot6EKVGzK3_JrVGdLe-TTdZYVtMdNLiW5PnoDDy2Vu1RavGnj6Afh7PO2UoONyf7wqeDt4hPHZNRnzGAMR0rl-z0pU1bU6VR_W-BmCLtBcSzl2hIW5ufiyr6xI6h3-MTq-eF9T4_uTnDfXnE5F18LzN609hvNYUv5r7z3WhJaBpP3mAjmh1nuMBfZnj6zdQVdU6IgQMA4yPyRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایران به یک شهروند آمریکایی که در دسامبر ۲۰۲۴ در زمان «ریاست جمهوری» جو بایدن خواب‌آلود به ناحق بازداشت شده بود، اجازه خروج از کشور را داده است. او اکنون در سلامت کامل و در شرایط خوبی در خارج از ایران است. ایالات متحده آمریکا از این اقدام حسن نیت ایران قدردانی می‌کند!
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/18329" target="_blank">📅 08:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18328">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c5179795.mp4?token=mLzqizEVzGToFV7CgJ4V1gKAFtLb82pF9o8cvh5RQlG3AGEZRiNX63NVDM-BkZJehXVfZA4k_m9Yxgf_5CFr8a5OI550bsavQlgVagTSCVEXSmmSKpUACSCxSc_M2hcpo1A9dS7OlV8_V3JsyC9zm6aj7V6Qy0lZpSAD6P18OxpZmGKQNZXfRvUSk1IH7T-wO5pDJbEp_8jU0c75HffedbWlUlEnTmDyOUPY0iWd84OrJw88EIGDtRLWKZDVwjpxGsBOjgMOY-udWxQOIO__0t_VUcBg9LE2CuR7qRf9Py7yAMa6ju-Hp5pRXSv9mOk2ddukmydt2uTBoYa60oHUjSGWYiBS99DburjqLWtSErtshgyEBvhiZEpQkQAF5l4KqWeD8swX5hBw3zWMb8CIfWJRA8Bqke-t8xk4cE1InThFDl2_f-wPqMSfm4vWS89dSVZvVIK81iNHvctODJFZVOtMu9AvextX4oZZ4viAnFm2EmioS_PCe_XUGO5joFyR72-bX-La12Il4TLMG4AFNgWVPsfX9sXJ8wqC_p2RQvQ1Kv9cMgVHW3EdU4jO17apOILGsPqIHdbNuSPe5bCm7swLZN1H5BTZnow06t7-E99nqZ6Md-ZkVUMO1eNsuEc739Pa1TRnyrSSL5IqVixwdzY5w2Ab2R8CtemDKT4Pw4M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c5179795.mp4?token=mLzqizEVzGToFV7CgJ4V1gKAFtLb82pF9o8cvh5RQlG3AGEZRiNX63NVDM-BkZJehXVfZA4k_m9Yxgf_5CFr8a5OI550bsavQlgVagTSCVEXSmmSKpUACSCxSc_M2hcpo1A9dS7OlV8_V3JsyC9zm6aj7V6Qy0lZpSAD6P18OxpZmGKQNZXfRvUSk1IH7T-wO5pDJbEp_8jU0c75HffedbWlUlEnTmDyOUPY0iWd84OrJw88EIGDtRLWKZDVwjpxGsBOjgMOY-udWxQOIO__0t_VUcBg9LE2CuR7qRf9Py7yAMa6ju-Hp5pRXSv9mOk2ddukmydt2uTBoYa60oHUjSGWYiBS99DburjqLWtSErtshgyEBvhiZEpQkQAF5l4KqWeD8swX5hBw3zWMb8CIfWJRA8Bqke-t8xk4cE1InThFDl2_f-wPqMSfm4vWS89dSVZvVIK81iNHvctODJFZVOtMu9AvextX4oZZ4viAnFm2EmioS_PCe_XUGO5joFyR72-bX-La12Il4TLMG4AFNgWVPsfX9sXJ8wqC_p2RQvQ1Kv9cMgVHW3EdU4jO17apOILGsPqIHdbNuSPe5bCm7swLZN1H5BTZnow06t7-E99nqZ6Md-ZkVUMO1eNsuEc739Pa1TRnyrSSL5IqVixwdzY5w2Ab2R8CtemDKT4Pw4M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که
موج حملات شامگاهی
علیه ایران در ساعت
۹:۰۰ شب به وقت شرق آمریکا (ET) روز ۱۵ ژوئیه
(۰۴:۳۰ بامداد ۱۶ ژوئیه به وقت تهران)
به پایان رسید.
به گفته سنتکام، نیروهای آمریکایی
مراکز فرماندهی، سامانه‌های پدافند هوایی، توانمندی‌های موشکی و پهپادی، و تأسیسات پایش و دیده‌بانی ساحلی ایران
را هدف قرار دادند تا توانایی ایران برای تهدید دریانوردان و خدمه کشتی‌های تجاری که از
تنگه هرمز
عبور می‌کنند، بیش از پیش تضعیف شود. سنتکام اعلام کرد که در این عملیات از
مهمات هدایت‌شونده دقیق
استفاده شده و اهدافی در چندین نقطه، از جمله
بندرعباس
، مورد اصابت قرار گرفته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/18328" target="_blank">📅 08:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18327">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1feec959.mp4?token=STN_eKlm0oGj392Sa7SyaGqrzRimlN0LWJWT4O9kMfPqn3Z0KTfLuFhRtWS589hpbLYj5TnMzSoBmrS_HKVTB5FT0R8lZ_ImE3FxD1-zhFBusp2Pkg193AYzNPOEOFiIA7RafqeyAtN9BbMEpyywTuIXzJJ0G-P4tZ35Te6K4lZoj-rZ5BiQztr7lgC21273FrNOwsOgzmJN3m8DDzQ6flDlZXU0UKS3DjKs_Vm-diC9I5r-m94bEpKly4USAg461uvs-R_kgPCoQhpiuSS54DMZGdcLUNSJbxJ7vs3mVFDPWI8g-DHm5qlI2Jm0ummNTsC4s2w703bnwA9Ofuq9jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1feec959.mp4?token=STN_eKlm0oGj392Sa7SyaGqrzRimlN0LWJWT4O9kMfPqn3Z0KTfLuFhRtWS589hpbLYj5TnMzSoBmrS_HKVTB5FT0R8lZ_ImE3FxD1-zhFBusp2Pkg193AYzNPOEOFiIA7RafqeyAtN9BbMEpyywTuIXzJJ0G-P4tZ35Te6K4lZoj-rZ5BiQztr7lgC21273FrNOwsOgzmJN3m8DDzQ6flDlZXU0UKS3DjKs_Vm-diC9I5r-m94bEpKly4USAg461uvs-R_kgPCoQhpiuSS54DMZGdcLUNSJbxJ7vs3mVFDPWI8g-DHm5qlI2Jm0ummNTsC4s2w703bnwA9Ofuq9jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند ثانیه از اهواز
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18327" target="_blank">📅 02:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18326">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">قشم و سیریک هم گزارش صدای انفجار
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18326" target="_blank">📅 01:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18325">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بندرعباس رگباری دارم میزنند دوباره
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18325" target="_blank">📅 01:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18324">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آغاز حمله جمهوری اسلامی به پایگاه های آمریکا
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18324" target="_blank">📅 01:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18323">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سخنگوی سپاه: دشمن تصور نکند که می‌تواند جنگ را فرسایشی کند
عملیات‌های ایران فعلا متمرکز بر انهدام زیرساخت تهاجمی آمریکا در منطقه است. سپس گام‌های بعدی آغاز خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18323" target="_blank">📅 01:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18322">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">همین الان پایگاه هوایی بندرعباس رو زدند
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18322" target="_blank">📅 01:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18321">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بندر صدای انفجار
@warroom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/18321" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18319">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پدافند شرق تهران درگیر شده
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/18319" target="_blank">📅 01:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18315">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/18315" target="_blank">📅 01:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18314">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گزارش انفجار های قشم به حدود ۱۰-۱۴ مورد رسیده
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/18314" target="_blank">📅 01:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18313">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">استانداری هرمزگان تأیید کرد که نقطه ای در حوالی سیریک مورد اصابت موشک های آمریکایی طی اوایل بامداد پنجشنبه قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18313" target="_blank">📅 01:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18312">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/18312" target="_blank">📅 01:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18311">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بازم روستای «‌مسن» قشمرو دارن میزنند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18311" target="_blank">📅 01:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18310">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پرتاب موشک از شیراز
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/18310" target="_blank">📅 00:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18309">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">قشم رو خیلی زدن پشته هم ۷-۸-۱۰ تا همه ریخت بیرون
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18309" target="_blank">📅 00:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18308">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d120a1732a.mp4?token=QtUOTsryPWXWWtSPQz0iXYDvvRQYtWafzVoER7MuIl-gTR7Qbi_KK6tzUqYmEGgwYV3C5IjNYOEXDCv3ooKMWod4Oq-ps-0Lkx9uAW5ZB5jm-e9KYsnhZZz5I767F5hvrVEqYIocTVZR0dFluNLvBmr_JcVuRJjWqnrBHI1MsICLLj1YNHIVeaZk5EE8LFtaAvquX5wXgh4tPuYiouH26j4HJ3Cc0xOoCniMrQWIvJhmkyxms6Wpi_O1VI-Cmr4g2mkYAFMQUyF1Dn0sGorP0BEx9Yl2da4IQHabXOXoJ5EBb_yCw2IVg2WitdktuIFzzcEGisMgpPz9SBq16oacby8F1wo2oyuUDplPBFqctlHbUC_6qwAcEe6b2bmZFreodFJKcM7mUbmGW1go-jDBWfx5K7XHv6u-_mq1LP8h9IVonUuyM1UtZau12qK680zHxQ_5UJNpkPn9tfTH-WmuQGtafnjecgT6X9JlHzdgsNH2KEKoJ9vTklL7keQKZJ3ZS1-Jzb2jvF8c61gN2tMbCl83U9sJhSUq9-BJ9nXnO2L1DAM0_OygLzsxvCHdGs2Yk9YUHL0hyH14c4G54xYylymmORH3_MlIYgzGAufvUiAF6GjYZmAUqI-1_dFGinSeHxeukQv17xMhgs_3x5AaKutXQft9huhwDJ3D7n85tM4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d120a1732a.mp4?token=QtUOTsryPWXWWtSPQz0iXYDvvRQYtWafzVoER7MuIl-gTR7Qbi_KK6tzUqYmEGgwYV3C5IjNYOEXDCv3ooKMWod4Oq-ps-0Lkx9uAW5ZB5jm-e9KYsnhZZz5I767F5hvrVEqYIocTVZR0dFluNLvBmr_JcVuRJjWqnrBHI1MsICLLj1YNHIVeaZk5EE8LFtaAvquX5wXgh4tPuYiouH26j4HJ3Cc0xOoCniMrQWIvJhmkyxms6Wpi_O1VI-Cmr4g2mkYAFMQUyF1Dn0sGorP0BEx9Yl2da4IQHabXOXoJ5EBb_yCw2IVg2WitdktuIFzzcEGisMgpPz9SBq16oacby8F1wo2oyuUDplPBFqctlHbUC_6qwAcEe6b2bmZFreodFJKcM7mUbmGW1go-jDBWfx5K7XHv6u-_mq1LP8h9IVonUuyM1UtZau12qK680zHxQ_5UJNpkPn9tfTH-WmuQGtafnjecgT6X9JlHzdgsNH2KEKoJ9vTklL7keQKZJ3ZS1-Jzb2jvF8c61gN2tMbCl83U9sJhSUq9-BJ9nXnO2L1DAM0_OygLzsxvCHdGs2Yk9YUHL0hyH14c4G54xYylymmORH3_MlIYgzGAufvUiAF6GjYZmAUqI-1_dFGinSeHxeukQv17xMhgs_3x5AaKutXQft9huhwDJ3D7n85tM4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : بزن زنگووووو
🔔
@WarRoom
رکورد جدید ۱۱ تانکر سوخترسان در خلیج فارس
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18308" target="_blank">📅 00:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18307">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گزارش انفجار های پی‌ در پی قشم
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18307" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18306">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">به طرفداران ارژانتین تبریک میگم از جمله بی بی عزیز
😂
من خودم که فوتبالی نیستم ما دنبال این توپا نیستیم
😉
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/18306" target="_blank">📅 00:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18305">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9690f3c84.mp4?token=Jdjpr2skKWwU0l0hP-JNd5JifqLj1Idg-7SFPTuffkxzeH0O8laQIn9_lEIGshcR3PSU16GU29qPU-BT1LYhWLlCD6gukQdluHyd4jBUAt_JucKC05YOOtVc6Kw1QWKc_Eo1LV1Ov-_80DaC-BYIiLuIszYT3BcAofC3WA6n-SAr5soi504_q_K4nVMPH98K8zXzzycIDRsHd1uuZN7c8d2NlJfq1lQJ1k3G7cVeX1rYHLVw1XATThBb0mggbpUPICntB_wV5UMtF23XQHlt9XwaoCXvL-KGJZEkRQOra7blVSAZu-JSD2y7r72SXwpTmacWAb9mFHWOKr87hEsBjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9690f3c84.mp4?token=Jdjpr2skKWwU0l0hP-JNd5JifqLj1Idg-7SFPTuffkxzeH0O8laQIn9_lEIGshcR3PSU16GU29qPU-BT1LYhWLlCD6gukQdluHyd4jBUAt_JucKC05YOOtVc6Kw1QWKc_Eo1LV1Ov-_80DaC-BYIiLuIszYT3BcAofC3WA6n-SAr5soi504_q_K4nVMPH98K8zXzzycIDRsHd1uuZN7c8d2NlJfq1lQJ1k3G7cVeX1rYHLVw1XATThBb0mggbpUPICntB_wV5UMtF23XQHlt9XwaoCXvL-KGJZEkRQOra7blVSAZu-JSD2y7r72SXwpTmacWAb9mFHWOKr87hEsBjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد نیروهای آمریکایی در
۱۵ ژوئیه
و در چارچوب اجرای
محاصره دریایی علیه ایران
، یک نفتکش خالی از محموله را که در حال حرکت به سمت یکی از بنادر ایران در خلیج فارس بود، از کار انداختند.
بر اساس اعلام سنتکام، نیروهای این فرماندهی نفتکش
M/T Belma
با پرچم
کوراسائو
را هنگام عبور از آب‌های بین‌المللی به مقصد
جزیره خارک
رصد کردند. به گفته سنتکام، این کشتی تجاری با وجود دریافت چندین هشدار، تلاش کرد محاصره دریایی آمریکا را نقض کند. در پی آن، یک هواگرد آمریکایی با شلیک
موشک‌های هلفایر
به دودکش کشتی، آن را از کار انداخت. سنتکام می‌گوید این کشتی دیگر به سمت ایران در حرکت نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18305" target="_blank">📅 00:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18304">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">جی‌دی ونس درباره ایران: «ما قرار نیست فقط بمباران کنیم، بمباران کنیم و باز هم بمباران کنیم.
ما تلاش خواهیم کرد از نیروی نظامی‌مان به‌عنوان یکی از ابزارهای متعددی که در اختیار داریم برای حل این مشکل استفاده کنیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18304" target="_blank">📅 00:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18303">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انگلیس ۱ ، آرژانتین۲
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18303" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18302">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18302" target="_blank">📅 00:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18301">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انگلیس ۱ ، آرژانتین ۱
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18301" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18300">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef977aa121.mp4?token=oZ15KL4WoLPAjqHrSVyOPomClmQWCjmTvmpshSLNdQUYdiK2G8W-79M0BExe732Im-AetHMqKecrZzW1iED7ZbuRn8eYYx98d3CiAXuNaTGMaNihmPyNE5y0qOVw4g_g34x5-r86zGQrST6tj6OMt8iaFx2TZekPvDcoHWUN_vqZq4VTlxDfEGJKSfRH4zbL_5UTEq9qyURWqbbBNbVUJXJeF7TqQb1QVff3hVp5iNrSYnq1cPsXxPe_4aa5hG-wvyL37qaA4sAjxPR3M8HHTGzIiz3kw-_TRLgqGUJeu_1Cdy5iSscMctS86cSd8g_SMLodDmjLOgrz2XwGWiPdnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef977aa121.mp4?token=oZ15KL4WoLPAjqHrSVyOPomClmQWCjmTvmpshSLNdQUYdiK2G8W-79M0BExe732Im-AetHMqKecrZzW1iED7ZbuRn8eYYx98d3CiAXuNaTGMaNihmPyNE5y0qOVw4g_g34x5-r86zGQrST6tj6OMt8iaFx2TZekPvDcoHWUN_vqZq4VTlxDfEGJKSfRH4zbL_5UTEq9qyURWqbbBNbVUJXJeF7TqQb1QVff3hVp5iNrSYnq1cPsXxPe_4aa5hG-wvyL37qaA4sAjxPR3M8HHTGzIiz3kw-_TRLgqGUJeu_1Cdy5iSscMctS86cSd8g_SMLodDmjLOgrz2XwGWiPdnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما وارد خاورمیانه می‌شویم و آن(تروریسم منطقه) را از کار می‌اندازیم و بعد به خانه برمی‌گردیم. همه می‌پرسند چرا این کار را کردیم... ما بزرگی و عظمت بدست میارویم مثل کاری که ونزوئلا کردیم ( همه شوک شدن)
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18300" target="_blank">📅 00:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18299">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ارسالی : شهرک صنعتی زنجان تمام شیشه هامون ریخت
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18299" target="_blank">📅 00:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18298">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ درباره ایران:
بسیار زود شکست خواهند خورد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18298" target="_blank">📅 00:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18297">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اقلیم کُردستان: ائتلاف بین‌المللی به رهبری آمریکا، 8 پهپاد انفجاری سپاه را بر فراز اربیل رهگیری و سرنگون کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18297" target="_blank">📅 00:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18296">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7046544db.mp4?token=dVKPB3qRXLPGmGhhseCSPWbfr2tVsgL7x0wqXNwmweUTmCaFNf0f0fFsoU8NI746PV30KIgsYx1AgvdJTUr7ObjT8mHgtkGI1_LGah977GBjdGw8iYRMPZo6bpfAvsHXlcoveGw0mWakMOPXOqzooUQhcrJwNUV4FAUHNNaTHfGC-5zm-p1YItJl5I76R7IzDBRM3qlAwfdWCquy9c2t_JaPMpt3Lg_DPEEO6rSTyJ5PSCGi2lGE4_-9hxpIlefKg3JA8s2rZsS-F_3jtoSQ3UwBo_oIKllu74GsghbwU4tlmAr-u0ARjaa_Hko4eXwwWxfEKpARIQB09A5sIqjqfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7046544db.mp4?token=dVKPB3qRXLPGmGhhseCSPWbfr2tVsgL7x0wqXNwmweUTmCaFNf0f0fFsoU8NI746PV30KIgsYx1AgvdJTUr7ObjT8mHgtkGI1_LGah977GBjdGw8iYRMPZo6bpfAvsHXlcoveGw0mWakMOPXOqzooUQhcrJwNUV4FAUHNNaTHfGC-5zm-p1YItJl5I76R7IzDBRM3qlAwfdWCquy9c2t_JaPMpt3Lg_DPEEO6rSTyJ5PSCGi2lGE4_-9hxpIlefKg3JA8s2rZsS-F_3jtoSQ3UwBo_oIKllu74GsghbwU4tlmAr-u0ARjaa_Hko4eXwwWxfEKpARIQB09A5sIqjqfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهواز الان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/18296" target="_blank">📅 23:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18295">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اهواز همچنان زیر حملات
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18295" target="_blank">📅 23:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18294">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انگلیس ۱ ، آرژانتین ۰
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18294" target="_blank">📅 23:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18293">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">@WarRoom
حمله زمینی ؟</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18293" target="_blank">📅 23:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18292">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=l8AXSmBfHTADvlh0VdWhxZ36n4M4wkQXboH5LajFL94ZqmqedWmP_m2_t0Ou0Z9sS9xBU0hXZ1TfYn-NJDV6trru19QaZjKqupJV80qtzrho-voqSvEgiYq8K-OzThX4tnfJlioD0pVOglPeNqeaKrRju-o0anq23YqpZ9A9qIVj2TuMlv3z7OWC1CyXTixn6O-MF6OLzH3ijU-0v_veIZAQHFwWPC0lGwmSTelson6-1XCBzoHpRcxGrX865jpK9VCLrzpPWZmiEqnOgmAQECNNIyKOjusckHXucK_f4s_e90_MdBILxaCJZU21pL4WgRUQ4CJpYOvojvxc4VNFkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=l8AXSmBfHTADvlh0VdWhxZ36n4M4wkQXboH5LajFL94ZqmqedWmP_m2_t0Ou0Z9sS9xBU0hXZ1TfYn-NJDV6trru19QaZjKqupJV80qtzrho-voqSvEgiYq8K-OzThX4tnfJlioD0pVOglPeNqeaKrRju-o0anq23YqpZ9A9qIVj2TuMlv3z7OWC1CyXTixn6O-MF6OLzH3ijU-0v_veIZAQHFwWPC0lGwmSTelson6-1XCBzoHpRcxGrX865jpK9VCLrzpPWZmiEqnOgmAQECNNIyKOjusckHXucK_f4s_e90_MdBILxaCJZU21pL4WgRUQ4CJpYOvojvxc4VNFkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18292" target="_blank">📅 23:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18291">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f335c33224.mp4?token=INkkKzS4WH5H2FwYL_EgN_tt_1gguqm1IYXA87dgYsd9ioAfZ7TlYoRTjkhLFqPUEyZV079rIFYAqdoamGJpsf4OP8oyXgwDRJhgBL9wLg0T2iQDM8j8hUXldt36aDIs2GuXmGXX7WUXHhn6neZud_9liUwi3603w20dOq8kHCGjyI3rF_0C7gjW_R4tECMx2iZKYFqO4tcG0yKrGDo1T-AOoC4BwI9QfI4NvAG0eG4KHuHYutwChRuAGL43bkhrf_wF-10nBGWOEpPgMJ1v3VEH2tWOJ-c720LjZ2LkF-xsvUIyat62mOqic9SjvWkWD8C023lTUeLfH3SA_MqKZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f335c33224.mp4?token=INkkKzS4WH5H2FwYL_EgN_tt_1gguqm1IYXA87dgYsd9ioAfZ7TlYoRTjkhLFqPUEyZV079rIFYAqdoamGJpsf4OP8oyXgwDRJhgBL9wLg0T2iQDM8j8hUXldt36aDIs2GuXmGXX7WUXHhn6neZud_9liUwi3603w20dOq8kHCGjyI3rF_0C7gjW_R4tECMx2iZKYFqO4tcG0yKrGDo1T-AOoC4BwI9QfI4NvAG0eG4KHuHYutwChRuAGL43bkhrf_wF-10nBGWOEpPgMJ1v3VEH2tWOJ-c720LjZ2LkF-xsvUIyat62mOqic9SjvWkWD8C023lTUeLfH3SA_MqKZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهواز، جهنم شده ه ه ه ه
معلون نیست چیه همینجور میسوزه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18291" target="_blank">📅 23:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18290">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پدافند زردشت اهواز مورد هدف قرار گرفته
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18290" target="_blank">📅 23:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18289">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">۵ انفجار استان کرمان
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18289" target="_blank">📅 23:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18288">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7aa831776.mp4?token=LdC_CneiznVOxVw6mbZtTmAbku_DqRR52JPeL8YXRva6fWMQp9SISmiEiT4VA6PONXMHzK6rDl--pIlsMblcpOFyVb5S2hWkhm6tXnWZrfBpUtXhkMgltgo_l921j4pwKyLXsdFiJmHSYUrsAIg0_9mhZg2mQoz7eDV1qz17yJZwlTitV7q7KJeM-PcxpyxJL8wxlvP4tDH9UxgJmoydWfgOGSMg3fDR9OpDehtgFcijK0jqFfNBqW0VKjkBi7bxtpWzznrNDRNNEXE1dPP8lKKya7VV77ZCfANqmzf3BotHcpoy8MMy48SQA8k8Jh8rOECojg2eTKcRmCb8fau-oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7aa831776.mp4?token=LdC_CneiznVOxVw6mbZtTmAbku_DqRR52JPeL8YXRva6fWMQp9SISmiEiT4VA6PONXMHzK6rDl--pIlsMblcpOFyVb5S2hWkhm6tXnWZrfBpUtXhkMgltgo_l921j4pwKyLXsdFiJmHSYUrsAIg0_9mhZg2mQoz7eDV1qz17yJZwlTitV7q7KJeM-PcxpyxJL8wxlvP4tDH9UxgJmoydWfgOGSMg3fDR9OpDehtgFcijK0jqFfNBqW0VKjkBi7bxtpWzznrNDRNNEXE1dPP8lKKya7VV77ZCfANqmzf3BotHcpoy8MMy48SQA8k8Jh8rOECojg2eTKcRmCb8fau-oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلشهر ، چابهار
@warroom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18288" target="_blank">📅 23:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18287">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گزارش انفجار کنارکککک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18287" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18286">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دقایقی پیش ترامپ: به این نتیجه رسیده ام که نمیتوان با سپاه پاسداران انقلاب اسلامی مذاکره کرد. خبرنگار: آیا یعنی ممکن است همانطور که با داعش کردی، آنها را از بین ببری؟ ترامپ: "بله، درست است. خواهیم دید چه میشود @WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18286" target="_blank">📅 23:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18285">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دقایقی پیش ترامپ: به این نتیجه رسیده ام که نمیتوان با سپاه پاسداران انقلاب اسلامی مذاکره کرد.
خبرنگار: آیا یعنی ممکن است همانطور که با داعش کردی، آنها را از بین ببری؟
ترامپ: "بله، درست است. خواهیم دید چه میشود
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18285" target="_blank">📅 23:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18284">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">انتشار این پست و معرفی من در گروه ها و تمام دوستاتون تنها کمک شماست
🙌🏾
🌐
instagram.com/Yashar
🌐
t.me/WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18284" target="_blank">📅 23:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18283">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارش انفجار بوشهر
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18283" target="_blank">📅 23:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18282">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">️تسنیم:
پرواز جنگنده‌های آمریکایی بر فراز سواحل جنوبی سیستان‌و‌بلوچستان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18282" target="_blank">📅 23:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18281">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اهوازی های عزیز ماشین بازن ، به چیزای خوب فکر کنید بعد آزادی،  پیست میبینمتون
❤️‍🩹
قویییی‌ باشین
🦾</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18281" target="_blank">📅 23:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18280">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اهواز سفتتتتتتت زددددد اینبار
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18280" target="_blank">📅 23:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18279">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هم اکنون پایگاه شیخ عیسی بحرین هدف موشک های ایرانی
@WarRoom
هدف نه اصابت</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18279" target="_blank">📅 23:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18278">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اهواز بازم زدن
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18278" target="_blank">📅 23:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18277">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🤯</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18277" target="_blank">📅 23:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18276">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b902c0e83.mp4?token=s5kZbBqPbkd8CRLIBx7pZECtapllkm1zHLCPLlHLKNPkv3fYrf7eWFPH9ty0N1uXMR5jOZde3t1A_2xsIj6IzdFsElB4GXsA9pSHdWIL-9vKNdRJMus8vaNvj4YmzejGWemHfVEobRGUmtJ_gA2oQ-YpRvY0mCsaEPi41WflPPWEvVHJjaAa6e3xEfcoLnHfs7P4VlVJTCmW_m7arpVvOeWvsVrbJN3cI0OiQ_aduSk6TfEclcG-HxDcDfbwjm2C68gkZGYqdYIn3KKhbjZEfO-PHaeRUwPHde22iFpVwJafxprpTNAyAOtpyWO9V89x5T1UplfgISa4TP65XfyJGYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b902c0e83.mp4?token=s5kZbBqPbkd8CRLIBx7pZECtapllkm1zHLCPLlHLKNPkv3fYrf7eWFPH9ty0N1uXMR5jOZde3t1A_2xsIj6IzdFsElB4GXsA9pSHdWIL-9vKNdRJMus8vaNvj4YmzejGWemHfVEobRGUmtJ_gA2oQ-YpRvY0mCsaEPi41WflPPWEvVHJjaAa6e3xEfcoLnHfs7P4VlVJTCmW_m7arpVvOeWvsVrbJN3cI0OiQ_aduSk6TfEclcG-HxDcDfbwjm2C68gkZGYqdYIn3KKhbjZEfO-PHaeRUwPHde22iFpVwJafxprpTNAyAOtpyWO9V89x5T1UplfgISa4TP65XfyJGYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین الان پاسگاه احمدریزه چابهار
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18276" target="_blank">📅 23:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18275">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اهواز قیامته دیگه نگمممممم</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18275" target="_blank">📅 23:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18274">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVgJ1w71l3oGoyX9G_DTH6VcXW6Q0a6rtS-TGWuKp3BDMxHszCBV_EB8LkL75U193uM9KpGLX_eP5ttWbSlE8L4kBZ9NH5kcqZzaWZCIumuJs17QtpaQd9uv6uAmxPibtoudts35TMuiDjY6InzHPbxlE25djai2-Q_FGGEE84kL3rnRa-GtIuJkgDkHvcDqe1OMSO8uNkALkLrO_ODRH0B-kirjF16dgb3WqaxGXokie-JI63SpazVl6AN_aYbsAswTJ2r2Q_6uMp3TiwHh6ZQzqsWtufjb_r39Pg-ZZfO8pUj_vGssuOG2FvKe9GqWrBb7xpQdYfzV5ggd2cWqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راسک سیستان بلوچستان زدن
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18274" target="_blank">📅 23:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18273">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/294a418fbc.mp4?token=uyuTQvrZLq31bhGNfny4823rfOVYD4jhJQeTtSWMH4J5LBmsoq5JwsavSTUqjTx3Ro8zNcm-1Sbj4swraAYC9irmnfwCWdFPgSfx_pTIXjs5J-l6CWBgtHDXNhLZeNiQLymcma9y78z0BlRyC8ZUQGZru8NvpwPnCHknKuOpW3SKFPk3GWZPXDQSgHQX1iDgmgq6V1bw2859uHc08UnSmVHDBXaPmG2C9DB822-43JfmNDyUBtDfix5ZkS-uvBa-giwJtUcKLbu6NVIgi4lQh3-iM96IaJ1CHzolsr5w2OT9mc3YIyM8TtUJuuhlhPvqDU51oSjfzlwidrKBVbpdJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/294a418fbc.mp4?token=uyuTQvrZLq31bhGNfny4823rfOVYD4jhJQeTtSWMH4J5LBmsoq5JwsavSTUqjTx3Ro8zNcm-1Sbj4swraAYC9irmnfwCWdFPgSfx_pTIXjs5J-l6CWBgtHDXNhLZeNiQLymcma9y78z0BlRyC8ZUQGZru8NvpwPnCHknKuOpW3SKFPk3GWZPXDQSgHQX1iDgmgq6V1bw2859uHc08UnSmVHDBXaPmG2C9DB822-43JfmNDyUBtDfix5ZkS-uvBa-giwJtUcKLbu6NVIgi4lQh3-iM96IaJ1CHzolsr5w2OT9mc3YIyM8TtUJuuhlhPvqDU51oSjfzlwidrKBVbpdJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهواز الان
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18273" target="_blank">📅 23:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18272">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اهواز رو همینجور میزنه کلا
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18272" target="_blank">📅 22:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18271">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گزارش انفجار سنگین بندر عباس
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18271" target="_blank">📅 22:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18270">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سنتکام : در ساعت
۳:۰۰ بعدازظهر به وقت شرق آمریکا (ET)
(۲۲:۳۰ به وقت تهران)
، نیروهای ایالات متحده عملیات
دومین موج حملات
امروز علیه ایران را آغاز کردند.
این حملات توانمندی‌های نظامی ایران را هدف قرار داده است؛ توانمندی‌هایی که به گفته آمریکا برای تهدید کشتی‌هایی که به‌طور آزاد از
تنگه هرمز
، آبراهی بین‌المللی و حیاتی برای تجارت جهانی، عبور می‌کنند، مورد استفاده قرار می‌گیرند.
ارتش ایالات متحده اعلام کرده است که
به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، ایران را در قبال این اقدامات پاسخگو می‌داند
@WarRoom
یاشار : دقیق نیم ساعت بعد که گفتم شد
💥</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18270" target="_blank">📅 22:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18269">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سنتکام : شروع کردیم
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18269" target="_blank">📅 22:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18268">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجار سنگین در اهواز حتی از قبلی ها هم سنگین تر
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18268" target="_blank">📅 22:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18267">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دوباره چابهار رو زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18267" target="_blank">📅 22:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18266">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1-Lq9vp7jcz9hmN8IaegiEa07IEiPztPrei8spmrKbwy-ustnxmehGQC7F5vTGdrXwwnhRmz5CCTsjoqdDQ_WPvbcUtmy2SdHdpqTiIjiw3TIc22poqB2CtHTsdl6XnQfE_eVFecY2AVR_iFVoggxxu9GvJBB4DfaE8ZX28rQhAqgjA34W3pvRISOVsBK4WuQBgGhD7a1440deqAGyP52uV6ut2M784AxDKLle4FZq1md7rdij6BLk0nLuIihuP8Vp-3IoCXzmzdF8F0crffrx1oXqS7UWUkpq27gm6xhzpNNjwHMFAWKNUlw7xoHgtWuBZiINnWHkuR43Pkqup9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منوجان در کرمان  پایگاه سپاه رو زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18266" target="_blank">📅 22:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18265">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انفجار سنگین منوجان در استان کرمان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18265" target="_blank">📅 22:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18264">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">در مجموع ۸ انفجار شدید در اهواز گزارش شده
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18264" target="_blank">📅 22:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18263">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">۵ تا دیگه اهواز رو زد شهر تکون خورد
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18263" target="_blank">📅 22:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18262">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">۲ انفجار شدید چابهار
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18262" target="_blank">📅 22:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18261">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارش انفجار چابهار
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18261" target="_blank">📅 22:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18260">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یاشار دوتا دیگه زدن اهواز خونه داره می لرزه صداش ۲ برابر دیشب
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18260" target="_blank">📅 22:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18259">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یه نیم ساعت دیگه سنتکام بیانیه میده شروع کردیم موج ۴رم
😂</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18259" target="_blank">📅 22:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18257">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">۳ تا سنگین زد اهواز و انگار زلزله اومد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18257" target="_blank">📅 22:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18256">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجار‌ اهواززززززز
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18256" target="_blank">📅 22:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18255">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ :  من از تعیین ضرب‌الاجل خوشم نمی‌آید.
@WarRoom
یاشار : نیست خیلی هم رأس پایان عمل میکنی و۴۷ بار‌تمدیدش نمیکنی.
🤒</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18255" target="_blank">📅 22:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18254">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارش دو انفجار در کنسولگری آمریکا در اربیل
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18254" target="_blank">📅 22:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18253">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارش صدای انفجار اهواز
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18253" target="_blank">📅 22:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18252">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18252" target="_blank">📅 22:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18251">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0279bf2042.mp4?token=tyfQ2vqr0y2t6j16cP1KSq2jvBXIbJdOUqzlPG1YAD8iMX8zXbAd24wCl2nMFeAIHBw_BHo5hPvzZ8RuAIfXRdOxF_bVfxofy1zIkOqXqgcgCqsQXIFAYhslefWatVzIpVrRXa1ZpdYYD0w7pAHz4trAeQ3O30W_bfqZCcqsPU8cmj3AOFKx8QIP8xREurTIYtn6UyR0jtPGr8HSSzPNIz30cvospYz28Bfr_IR9VCIfolODqcYCuG_8WTQ4RZ3Bsx0yIx4HcEaWlTuIZttsrm6CYeB3rRNnrtPxDs8N0SK3mPyEONBpmaPu7z9Ry-MDfTqf3RwHmC-MTNWDfVXMNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0279bf2042.mp4?token=tyfQ2vqr0y2t6j16cP1KSq2jvBXIbJdOUqzlPG1YAD8iMX8zXbAd24wCl2nMFeAIHBw_BHo5hPvzZ8RuAIfXRdOxF_bVfxofy1zIkOqXqgcgCqsQXIFAYhslefWatVzIpVrRXa1ZpdYYD0w7pAHz4trAeQ3O30W_bfqZCcqsPU8cmj3AOFKx8QIP8xREurTIYtn6UyR0jtPGr8HSSzPNIz30cvospYz28Bfr_IR9VCIfolODqcYCuG_8WTQ4RZ3Bsx0yIx4HcEaWlTuIZttsrm6CYeB3rRNnrtPxDs8N0SK3mPyEONBpmaPu7z9Ry-MDfTqf3RwHmC-MTNWDfVXMNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ  : همین الان اربیل عراق ، درگیری پدافند آمریکا با حملات ۳پا
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18251" target="_blank">📅 21:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18250">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1SNLvFXz37CKUY5gc6-y1KFMdP03o0miNgS2rA7Az6sUSRWm8FMH5vuqBYfRX-L0NM37UsivJCxZ32XI6FQwFn1AOs7aKdy2kAqgXKmw1p-jRIKYeewgSIrL4E_NyMSrpvM9gANiOlGcNx7Rgbj2VBrATHuxTE02chU2Q67YCY-UUqckZLUjdfAKuWQWADlL8euI-Qv9UBNiHt_qfaBu0IdxPpNb9TCK0MgjeN3czgzPgnPqDGbsXBMVEZuo7ol8AH1jKoIqvgqtp-nL8p5u2WpIVDZ5tVodLix7guc_yEoTmV8ufP6g7BKU6CrbHkt-5BcBviOHWXR_mexrLVWlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا اعتراضات و اعتصاب از پاساژ چارسو و علادین شروع شده و حسابی شلوغ شدن @WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18250" target="_blank">📅 21:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18249">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گزارش انفجار بندر عباس
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18249" target="_blank">📅 21:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18248">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سپاه پاسداران ایران در حال حاضر سامانه‌های پدافند هوایی SAM ساخت داخل، S-400 روسی و HQ-9 چینی را در نزدیکی خلیج فارس، مرز عراق و تنگه هرمز مستقر کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18248" target="_blank">📅 21:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18247">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ بار دیگر تهدید کرد: هفته آینده بدترین هفته برای ایران خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18247" target="_blank">📅 21:13 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
