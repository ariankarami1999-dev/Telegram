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
<img src="https://cdn4.telesco.pe/file/OER4rwaYjGteJr2OTltTXzJUy7PKVDg3lU7qmVfAO2YOXIhlIYPfOi5O7fuMpzJz48R9STxEzydPbtn3LKEryNiyTCKC0MxV_LUScdRp7m7IMqeWIDb0KRpLqqHoOTzvgR2hwyN_Kvlx3X9xaDrsi5XkrDvMbu7e3bhuZrpIFD_c7Ex28nV1M8PRF_VfCNMOJqoWSUlj_0bYQDuCf_QVHg9JDa3McVWu-z1Fa-BkfTHnqXC2ngYhnlhgrwsWizTOTkcpa3mDRsQXyLTUN-2GsG3WRAo_HKxA-3PRxKOqACyuv0uNHLRlmyMf-QZ8l5WhrXEY9URsPLRqvd15w9Rx0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 285K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 19:19:40</div>
<hr>

<div class="tg-post" id="msg-13152">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/withyashar/13152" target="_blank">📅 19:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13151">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ارتش اسرائیل: به سراسر لبنان از ضاحیه گرفته تا صور حمله می‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/withyashar/13151" target="_blank">📅 18:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13150">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وزارت کشور کویت به ساکنان خود هشدار داد که در انتظار حمله قریب‌الوقوع ایران در مکان‌های امن بمانند
@withyashar</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/withyashar/13150" target="_blank">📅 17:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13149">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
تسنیم: مذاکرات با آمریکا کاملا متوقف شد!
ایران خواستار توقف کامل تمام عملیات‌ها در غزه و لبنان برای از سرگیری مذاکرات با آمریکا است.
همچنین ایران به میانجی ها اعلام کرده است که بستن کامل تنگه هرمز و همچنین تنگه باب المندب را در دستور کار قرار داده است
@withyashar</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/13149" target="_blank">📅 16:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13148">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تسنیم: ایران تبادل پیام با آمریکا را در اعتراض به جنایات اسرائیل در لبنان متوقف می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/13148" target="_blank">📅 16:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13147">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بعضی رسانه ها مدعی شد تا ساعتی دیگر، پاسخ نقض آتش بس توسط جمهوری اسلامی ایران با حمله گسترده به رژیم صهیونیستی، داده خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/13147" target="_blank">📅 16:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13146">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEUDN6NL4zP3VAj-tWQuyXydnhrm8_rFZ5afPD2jGCPUYDcEdsiWrlmPtOIvYdnfV6DmhqfgCTyYd7A1dYdSQ0sI_BMmnA-6rXQ43lpxgxoX-usCqwl7faX7WuHjJNr6TxKXmwP6NYZqxBGkcT7kPIyKmJsfCwQnnvSznld-IKubKsCAaOlaICku6jcseTAVKeruaK6CJlF3wbW1JMPe6T6moMHb5QSviraf-_cMmzEIORrfatGgo-yNJp-nmmyQDra3UMyE_tfpnN300cgAENKsb8K1fbyAlXZki8zED-pwbzodjBJDmav2osofhaOqrh4AIUTo7_x2smkg1iWF4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداسیما طی خبری فوری:
نیروهای مسلح : حمله متوقف نکنن علیه لبنان ماهم حمله میکنیم
@withyashar</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/13146" target="_blank">📅 15:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13145">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که دو موشک بالستیک رژیم جمهوری اسلامی دیشب ساعت ۱۱ شب به وقت شرقی(۶:۳۰ صبح تهران)به سمت نیروهای آمریکایی در کویت شلیک شده است. موشک‌های ورودی سرنگون شدند و هیچ آسیبی به پرسنل آمریکایی وارد نشد.
@withyashar</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/withyashar/13145" target="_blank">📅 15:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13144">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/withyashar/13144" target="_blank">📅 14:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13143">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd86679833.mp4?token=YVp7jwFDnFdeNNkujliCOsCC9dd-FqJJ62d3QroZyI0DmnmfZMWN6EBWIzZvDncQ4FcU4VmVvIji4T1KYRsZgEMUveAKnMTFmIn4KyhOJRskjcv_4aloH8COhbmtoIsmR06WHzLx2HiphWD_SVNuL1feKsQF4avx6coyJHn1WXcRPSf2_UyQ1rxCkaCVTmzUSIXCqgGDkyItgrrhjLajvbkqmDuSL46e1LqnKATX8rKlwGQUp4NnFC7XdlyLa6_cd9MbQ9hLqk750z0RSFC5GtIxMIezAEyPBYFd8YcLYt38qbBkGH7JR03ydqTXbHO4bAPfzEs15vosjIB2LHyoEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd86679833.mp4?token=YVp7jwFDnFdeNNkujliCOsCC9dd-FqJJ62d3QroZyI0DmnmfZMWN6EBWIzZvDncQ4FcU4VmVvIji4T1KYRsZgEMUveAKnMTFmIn4KyhOJRskjcv_4aloH8COhbmtoIsmR06WHzLx2HiphWD_SVNuL1feKsQF4avx6coyJHn1WXcRPSf2_UyQ1rxCkaCVTmzUSIXCqgGDkyItgrrhjLajvbkqmDuSL46e1LqnKATX8rKlwGQUp4NnFC7XdlyLa6_cd9MbQ9hLqk750z0RSFC5GtIxMIezAEyPBYFd8YcLYt38qbBkGH7JR03ydqTXbHO4bAPfzEs15vosjIB2LHyoEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش فاکس نیوز از چند حمله آمریکا به قشم !
@withyashar</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/13143" target="_blank">📅 14:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13142">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تانکرترکرز: چهار نفتکش ایرانی با محموله هفت میلیون بشکه‌ای به ایران بازگردانده شدند و نتوانستند محاصره آمریکا را بشکنن
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/13142" target="_blank">📅 14:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13141">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عراقچی:
آتش‌بس میان ایران و ایالات متحده، بدون هیچ ابهامی، آتش‌بسی در تمامی جبهه‌ها، از جمله لبنان، محسوب می‌شود.
نقض این آتش‌بس در هر یک از جبهه‌ها، به منزله نقض آن در تمامی جبهه‌ها است.
ایالات متحده و اسرائیل مسئول پیامدهای هرگونه نقض این آتش‌بس خواهند بود.
@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/13141" target="_blank">📅 14:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13140">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36b672cbbb.mp4?token=q1nuyxxQASsylb9jeeVTp8gshR8anaAsB0fMF6VoK-NqLZ4ARVbNaUQ4-WyCAU-DsPRL-3gb7N2Omxk1XM6BAWSSbKIY7uzsXl0Axs2uOoptpXUvrg3GYdnMXfjwAp8mKKqp0vsu-9DMwOaDnJihQVWk2hOpovUeD707CQh0CjCvtqtkb_bVQ5qUPqVtvxcOGpA7RCN1IuUv0rZE3OuRTz2kvAeSxIRIsm14tSfsYkK8g_GFOkEbFA9I1oUqm9sjZCwlREbUQWinM3qyWjm0A8Jhvo4U1a3osh__e0ZDkNP48TNijfFk1-T0vLiuKU-qlp_DNM8c4LYn4hPEW3tMjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36b672cbbb.mp4?token=q1nuyxxQASsylb9jeeVTp8gshR8anaAsB0fMF6VoK-NqLZ4ARVbNaUQ4-WyCAU-DsPRL-3gb7N2Omxk1XM6BAWSSbKIY7uzsXl0Axs2uOoptpXUvrg3GYdnMXfjwAp8mKKqp0vsu-9DMwOaDnJihQVWk2hOpovUeD707CQh0CjCvtqtkb_bVQ5qUPqVtvxcOGpA7RCN1IuUv0rZE3OuRTz2kvAeSxIRIsm14tSfsYkK8g_GFOkEbFA9I1oUqm9sjZCwlREbUQWinM3qyWjm0A8Jhvo4U1a3osh__e0ZDkNP48TNijfFk1-T0vLiuKU-qlp_DNM8c4LYn4hPEW3tMjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوچ جمعی مردم بیروت پس از هشدار اسرائیل به بمباران
@withyashar</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/13140" target="_blank">📅 14:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13139">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">علیرضا فغانی به اولین داور تاریخ تبدیل شد که در ۴ جام جهانی قضاوت میکند
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/13139" target="_blank">📅 14:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13138">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اتاق جنگ با یاشار : اولین پرواز بازگشت زائران حج تمتع امروز ۱۱ خرداد ساعت ۱۶:۳۰ در مشهد به زمین می‌نشیند این عملیات ۱۱ روز دیگر ادامه دارد و در ۲۲ خرداد «جمعه» آخرین پرواز بازگشت انجام میشود , ۲۲ خرداد جمعه هفته دیگر ۲ روز قبل از‌ تولد دونالد ترامپ است و شب…</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/13138" target="_blank">📅 13:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13137">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اتاق جنگ با یاشار : اولین پرواز بازگشت زائران حج تمتع امروز ۱۱ خرداد ساعت ۱۶:۳۰ در مشهد به زمین می‌نشیند این عملیات ۱۱ روز دیگر ادامه دارد و در ۲۲ خرداد «جمعه» آخرین پرواز بازگشت انجام میشود , ۲۲ خرداد جمعه هفته دیگر ۲ روز قبل از‌ تولد دونالد ترامپ است و شب آن مارکت هم برای آخر هفته بسته میشود
@withyashar
همچنین یک هفته بعد از آن یک آخر هفته طولانی داریم چون جمعه هم تعطیلی رسمی فدرال است جونتینث  «روز پایان برده داری در آمریکا»۱۹ جوئن ۲۹ خرداد</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/13137" target="_blank">📅 13:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13136">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گالانت : نتانیاهو اعلام کرده خاورمیانه دیگر جای حزب الله نیست و تا نابودی کامل جلو خواهیم رفت
@withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/13136" target="_blank">📅 13:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13135">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">قالیباف در توییتر(X):
«اعمال محاصرۀ دریایی و تشدید جنایات جنگی در لبنان توسط اسرائیل عدم پایبندی آمریکا به آتش‌بس است.
هر انتخابی، هزینه‌ای دارد و صورت‌حساب آن هم از راه می‌رسد؛ همه چیز سر جای خودش قرار خواهد گرفت.»
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/13135" target="_blank">📅 13:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13134">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بنیامین نتانیاهو به همراه وزیر دفاع دستور حمله به ضاحیه بیروت را اعلام کردند
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/13134" target="_blank">📅 11:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13133">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سخنگوی وزارت خارجه: ما حق دفاع مشروع در برابر نقض آتش‌بس توسط آمریکا را داریم و امروز هم مبدأ تجاوز به خاک کشور را هدف قرار دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/13133" target="_blank">📅 11:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13132">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ به نیوزویک : مردم ایران از من تشکر میکنند چون بجای یکبار، دوبار رژیم رو عوض کردم
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/13132" target="_blank">📅 11:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13131">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromThis.is ⁰²:³⁵</strong></div>
<div class="tg-text">داش جان جدت ری اکشن
🤣
رو باز کن</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/13131" target="_blank">📅 11:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13130">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/13130" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13129">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZ58Wkdt3R_ztlUafyAC3gPA8J_5rl7XER3n242LrExDGEMezBB3Co29roLgMaJBL2loqSze39H9XEGHL8oWC3Z6vRvjV2gJlCVPx62PpVo0Q4a_bsUZVcTowadHc6wb9uunIQsS7NppTKxjrxB-5T77vqIM9UbiQUHQoGc-jUbysAR14lNOllYju1EoN83VzEWF1xwgp3aP-wmHb5SHDdEYrxGs9WCjFDB-O_3kl-N3DfWMEobxjhjju90yPs4FWj-Q0nLVrB-2EoPuADHl_bcN1lpERNphfblD4VshkF6Kux96gwRV2deTh9ai-mQN1tAjYbryrK50SkRA4p2M9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥴
🤣
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/13129" target="_blank">📅 11:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13128">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اطلاعات  تایید نشده بهم رسیده که  اندیشه ترور هدفمند بوده   شخص‌ مورد نظر مسئول قراردادهای بین صدا و سیما و قرارگاه خاتم‌الانبیا بود @withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/13128" target="_blank">📅 11:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13127">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارش های از مشاهده خط شلیک موشک از همدان
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/13127" target="_blank">📅 10:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13126">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">صدای انفجار مهمات عمل نکرده اصفهان پادگان پانزده خرداد
@withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/13126" target="_blank">📅 10:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13125">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">البته توجه کنید که گفته بودند از قبل که خنثی سازی مهمات عمل نکرده دارن  @withyashar ولی با توجه به اینکه سنتکام ساعتی پیش گفته حمله کرده و رادار زده هشیار باشید</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/13125" target="_blank">📅 10:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13124">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گروه تروریستس ۳پا امروز در بیانیه‌ای اعلام کرد در واکنش به حمله ارتش آمریکا به یک دکل مخابراتی در جزیره سیریک، «مبدأ حمله» رو هدف قرار داده و هشدار داد در صورت تکرار این اقدامات، پاسخ متفاوتی خواهد داد.
کویت حوالی ۶ صبح از فعال شدن سامانه‌های پدافندی خود برای مقابله با حملات موشکی و پهپادی خبر داد ولی مبدأ حمله را اعلام نکرد
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/13124" target="_blank">📅 10:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13123">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اتاق جنگ با شما : یاشار تتر داره کندل سبز میخوره همینجوری
این صداهای امروز مثل اینکه جدی تره
@withyashar
اتاق جنگ با شما :نهم اسفند هم همین ساعت ها بود داشتن حمله میکردند خدا به خیر کنه
😂
😂
💔</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/13123" target="_blank">📅 09:48 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13122">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/13122" target="_blank">📅 09:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13121">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">صدای انفجار در اصفهان
@withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/13121" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13120">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دوباره صدای انفجار‌ در بندر
@withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/13120" target="_blank">📅 09:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13119">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/13119" target="_blank">📅 09:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13118">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/13118" target="_blank">📅 09:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13117">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeb</strong></div>
<div class="tg-text">یعنی جنگ رو پنهان میکنن ؟؟</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/13117" target="_blank">📅 09:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13116">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اتاق جنگ با شما : صداش دقیقا مثل جنگنده آمریکایی یا اسرائیلی بود
@withyashar</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/13116" target="_blank">📅 09:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13115">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارش های زیاد از صدای جنگنده در تهران
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/13115" target="_blank">📅 09:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13114">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سنتکام : ما حملات دفاعی به رادار پهپاد و سایت‌های فرماندهی و کنترل در گوروک و قشم ایران انجام دادیم. @withyashar</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/withyashar/13114" target="_blank">📅 09:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13113">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گزارش چندین انفجار بندر عباس
🚨
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/13113" target="_blank">📅 09:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13112">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k86X0NuFFVge8UQSZV1XrJRIxpcKm5ZChVW4mMTCErpkxrbZI0zrxkpIqUDxyDtcvQsDkqjO8Tas5is3OcUTmJvl1PjmcJeLubcKUApGaVbVcqmtIa20hXRiGc999eTv5FMRmrTW5vZMUkkh7qnxTrSg7FkKbBKqF-s_y02LdXd0cMPmLQxfegOQP6GZZkXOa8ioPpWD60_u2IfcRUN732JOfwhpTxybmr7F7mruV1hRBiDIaV5punxQBxdjC489G9idb72n8yrMs0Q-7YoG7bQY-QZN_oCbQpIwH0g1RT12oP636wyxWd7A-F4Vn67hXFwVDosSJNqU5KxYbby30g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی قوه قضائیه ایران(میزان) اعلام کرد که دو نفر دیگر از معترضان دی‌ماه ۱۴۰۴ را به اتهام «آتش‌زدن مسجد»، «لیدری کودتا»، «تخریب اموال عمومی» و «مسدودسازی خیابان‌ها» مجازات کرده است.
نام این دو عزیز که ساعاتی پیش جاودانه شدند، مهرداد محمدی‌نیا و اشکان مالکی اعلام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/13112" target="_blank">📅 09:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13111">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سنتکام : ما حملات دفاعی به رادار پهپاد و سایت‌های فرماندهی و کنترل در گوروک و قشم ایران انجام دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/13111" target="_blank">📅 08:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13110">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گزارش شلیک موشک از امیدیه در استان خوزستان به سمت کویت۶:۳۰ دقیقه و ۸:۳۳ دقیقه
@withyashar</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/13110" target="_blank">📅 08:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13109">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PENkF-DI0t3Sa7KpiwGWsCKq4m5BXI27rQASyzQ-rEUbTq3aUsrLkGukRgN5jDVYsyYmtRBnjE0lLuK9ktiQ8iiwZIIYBXdL8AH9vsWE3Ls9eZ8vgzZ4u8eQ65ZAnvc5vO6oBWiXLY5FvPJZ0p7b9T-yshm0G-tsdrtNg9tMzM74vaPWks8gKISm-WxhVFCcfOipb8jQsMlAQGiML07FEt4pMKsjjxjXzE3saw9_qt9ZVIJjBiT3JE067S17L5LnO8E7DCA264-dhdXUsq3zBcFVVAt7R915tj3tUUfe3yi0Rk5g4lEfYIuwyr8T60ektQveb0adYtcBlH8kex5fEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
ایران واقعاً می‌خواهد به توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود. اما آیا دموکرات‌های کودن و برخی جمهوری‌خواهانِ ظاهراً غیرمیهن‌دوست نمی‌فهمند که وقتی بازیگران سیاسی مدام، بارها و بارها و در سطحی بی‌سابقه، با نیش و کنایه منفی می‌گویند باید سریع‌تر حرکت کنم، یا کندتر حرکت کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست کارم و مذاکره کردن برای من بسیار سخت‌تر می‌شود؟
فقط بنشینید و آرام باشید؛ در پایان همه‌چیز خوب پیش خواهد رفت همیشه همین‌طور است!
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/13109" target="_blank">📅 08:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13108">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گزارش‌ها از حمله پهپادی ایران به گروه های مخالف ایرانی-کرد در نزدیکی اربیل، شمال عراق!
@withyashar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/13108" target="_blank">📅 00:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13107">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eae745a43.mp4?token=O_MnzgdJzkQ1DStZh3WSCoKRPErXGj_KO4KAQMQXQ4tUltSvkwQO-CGzUflsiNs3uHCbh2r1ZrPJkp4LgmHRPdi7vS7HQuHVR_pvbbzUbfgB3rqRLu3O87tjLODSR_g6-61KLhCCA9F5sYpz5IXTUFpe51QrWcEog-ILap0NeOIh1d0bHNPF_buMs_JFCZu4gElHrVgG55RP0t0Rmx_7Ow6IoAx1QIMSf1uYjybXV4b9wMdXtyW5exEH3aVYRuIXxb_WRMN3NFRD5p3ShZ-GQP92nSgQOYGw686VnDxqtwrtPiej3N4745mjBVd2P4zkOBfsnJaj69ntTBCCdGYP0qvIh3-QSoX0UDWmrnxJeI98VZX74ogzscyVG6vKiQ9rf8_lWJ1CMFX66IXgqCR_xiPabITW_iGApI9All9JJtkf0tf4EDX60U8HeRaOcVJPd2bncaV7QKsKvPBGXr6NmKzoVAU6WszNfUCjaKk6MWE5mhjFXkehfoErznggEXCJGhWBmRzKGEwlZXQZ2YKT9W2hSGJLorldv4OesoCEQByer2BImh25XeL6H3mTEQbyGwGAY_6RD_tAvWw8JtLeNiZOSNa0unJZgP453ZEXJpeX1q0BJE-3OoN2Lk9d3yaBHgAFcoe4zmTdzuymLaR1pVGvSIdQiHLrikuxgKIkY5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eae745a43.mp4?token=O_MnzgdJzkQ1DStZh3WSCoKRPErXGj_KO4KAQMQXQ4tUltSvkwQO-CGzUflsiNs3uHCbh2r1ZrPJkp4LgmHRPdi7vS7HQuHVR_pvbbzUbfgB3rqRLu3O87tjLODSR_g6-61KLhCCA9F5sYpz5IXTUFpe51QrWcEog-ILap0NeOIh1d0bHNPF_buMs_JFCZu4gElHrVgG55RP0t0Rmx_7Ow6IoAx1QIMSf1uYjybXV4b9wMdXtyW5exEH3aVYRuIXxb_WRMN3NFRD5p3ShZ-GQP92nSgQOYGw686VnDxqtwrtPiej3N4745mjBVd2P4zkOBfsnJaj69ntTBCCdGYP0qvIh3-QSoX0UDWmrnxJeI98VZX74ogzscyVG6vKiQ9rf8_lWJ1CMFX66IXgqCR_xiPabITW_iGApI9All9JJtkf0tf4EDX60U8HeRaOcVJPd2bncaV7QKsKvPBGXr6NmKzoVAU6WszNfUCjaKk6MWE5mhjFXkehfoErznggEXCJGhWBmRzKGEwlZXQZ2YKT9W2hSGJLorldv4OesoCEQByer2BImh25XeL6H3mTEQbyGwGAY_6RD_tAvWw8JtLeNiZOSNa0unJZgP453ZEXJpeX1q0BJE-3OoN2Lk9d3yaBHgAFcoe4zmTdzuymLaR1pVGvSIdQiHLrikuxgKIkY5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : چشم آسمان ، هواپیما آواکس
@withyashar</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/13107" target="_blank">📅 00:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13106">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/13106" target="_blank">📅 23:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13105">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انفجار در فاز یک اندیشه شهریار خیابان شیشم شرقی در یک ساختمان که چندین مصدوم داشته  @withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/13105" target="_blank">📅 23:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13104">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجار در فاز یک اندیشه شهریار خیابان شیشم شرقی در یک ساختمان که چندین مصدوم داشته  @withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13104" target="_blank">📅 23:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13103">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8091569054.mp4?token=tl3q92KqwruPaxwATTIqj-oAsH9pAC5U9H7wfwWDkGncwoNIdeGTSNCkb8EHSwP67EA8CskLa0f7mOOfkZ6N93W_4YpFVEjZ7I925v62Ay_vGOq0wyS-ZNlNCX7DDtvtDnb8zwrqKKxkWlwDS5AIZ_e5H1p8p2g_AHZ8HL1lItjwIcAGNH9223dTViR_CpxlKsPjezSCYv59VGeYdwUsZFjbalNnjkE39zdb-xGGrGnWRBKo3QxtgtmnuEo9tfMRioq2aMSdyfkuW3eBAIw1cLGtlqfPjvsv8jJ0Ezd5iZ1HLWffMPdAMcGWMkrpP4G3suriT-TTedvWzo_RkaJU3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8091569054.mp4?token=tl3q92KqwruPaxwATTIqj-oAsH9pAC5U9H7wfwWDkGncwoNIdeGTSNCkb8EHSwP67EA8CskLa0f7mOOfkZ6N93W_4YpFVEjZ7I925v62Ay_vGOq0wyS-ZNlNCX7DDtvtDnb8zwrqKKxkWlwDS5AIZ_e5H1p8p2g_AHZ8HL1lItjwIcAGNH9223dTViR_CpxlKsPjezSCYv59VGeYdwUsZFjbalNnjkE39zdb-xGGrGnWRBKo3QxtgtmnuEo9tfMRioq2aMSdyfkuW3eBAIw1cLGtlqfPjvsv8jJ0Ezd5iZ1HLWffMPdAMcGWMkrpP4G3suriT-TTedvWzo_RkaJU3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/13103" target="_blank">📅 23:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13102">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پدافند قم فعال شد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/13102" target="_blank">📅 23:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13101">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b4864ff2.mp4?token=OkK2VFwVVae0ktv0_dFpMnN4Nd9eq8qiprSuS3fXf_Mg8jwj6yagWc02Gb1Ui315fwpywBCk_bWKodwqVokSmXfuKXezfz4sTUxZka94zucq1gQZv_gAwGJONwkZm7gHZ-4pl_SfaxvqKsU4sXLYFJ-g24Ncw4Mdno-J3iDNPsR2h5QOgtq7viD7USZo-fJO7evRoacXqmulMD1Wp6IOKl98TGHnHX-Y-IUvtMof86wrGaYN1LTGps-bsKkPkFzJp-aIFDjf_hiJac6mEKn7ODvHB1gDXd8fRAhQnbIAj7-BhuuhzgsZXpFY2g4Pgw-rATaTGTVJUlD2cD2t_0rzqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b4864ff2.mp4?token=OkK2VFwVVae0ktv0_dFpMnN4Nd9eq8qiprSuS3fXf_Mg8jwj6yagWc02Gb1Ui315fwpywBCk_bWKodwqVokSmXfuKXezfz4sTUxZka94zucq1gQZv_gAwGJONwkZm7gHZ-4pl_SfaxvqKsU4sXLYFJ-g24Ncw4Mdno-J3iDNPsR2h5QOgtq7viD7USZo-fJO7evRoacXqmulMD1Wp6IOKl98TGHnHX-Y-IUvtMof86wrGaYN1LTGps-bsKkPkFzJp-aIFDjf_hiJac6mEKn7ODvHB1gDXd8fRAhQnbIAj7-BhuuhzgsZXpFY2g4Pgw-rATaTGTVJUlD2cD2t_0rzqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار در فاز یک اندیشه شهریار خیابان شیشم شرقی در یک ساختمان که چندین مصدوم داشته
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/13101" target="_blank">📅 23:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13100">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تسنیم : ایران تغییرات بیشتری در یادداشت تفاهم ایجاد خواهد کرد. اینکه ترامپ در حال ایجاد تغییراتی در این یادداشت تفاهم است، به این معنی نیست که این تغییرات برای ما قابل قبول است. ایران کاملاً برای شرایطی که هیچ توافقی حاصل نشود، آماده است.
@withyashar</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/13100" target="_blank">📅 22:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13099">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حمله به کشتی حامل مس در تنگه هرمز
در پی درگیری‌های اخیر در تنگه هرمز، یک کشتی خارجی که حامل مس بود، مورد هدف قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/13099" target="_blank">📅 22:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13098">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c322df9e96.mp4?token=XOuLLJJ3b_sWKa7M5TQ4Tu_JfxaPsb_Xp56JdhDScl4B7L6V7lnO-W-s4VVmXextAgmj1A5SNGj_9_tULBxT-A4hPRNSZ4vjkKDNYuzQSxQr374j_VZ7GVtywJq6cr4SHS0Pq9nIZVitX_YniZSDAl_unqZVSHfwsqL3QQCwWZiPJepHpn8h3mgZVkk5hIRqr6VIrvmGqAfvTnQowMK_UUx50wNvkZ2KC7Z1AMHA03mlOJ3GrK3yyn2bJ0U3tiGd-MYBfypCU7D2mPQXLF2wDx9sROOiGyywPz4ZIt3EnKxGB62RFjYTBL3CptNVNMsWU9waS0zjiUvI6f0QUuTiGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c322df9e96.mp4?token=XOuLLJJ3b_sWKa7M5TQ4Tu_JfxaPsb_Xp56JdhDScl4B7L6V7lnO-W-s4VVmXextAgmj1A5SNGj_9_tULBxT-A4hPRNSZ4vjkKDNYuzQSxQr374j_VZ7GVtywJq6cr4SHS0Pq9nIZVitX_YniZSDAl_unqZVSHfwsqL3QQCwWZiPJepHpn8h3mgZVkk5hIRqr6VIrvmGqAfvTnQowMK_UUx50wNvkZ2KC7Z1AMHA03mlOJ3GrK3yyn2bJ0U3tiGd-MYBfypCU7D2mPQXLF2wDx9sROOiGyywPz4ZIt3EnKxGB62RFjYTBL3CptNVNMsWU9waS0zjiUvI6f0QUuTiGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تردد خودرو های منطقه آزاد در سراسر کشور آزاد است
@withyashar</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/13098" target="_blank">📅 22:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13097">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/481d5e13ac.mp4?token=ike7sdFRdDCn5cEAvtuq4ZhU7xf48pyEWcOlpPTbRQsTAXP0poKYULklLyxQ7P14l23L_7LsIzxbqrngfmHsk0MNNiBJVIfZqp5nLjZj3OBSoaaKgd6EDOWt0x4Kk5fkkxoYrvGP0MRf2Ruzx1PsefqnWFWE04zvUAlAdJG1gQNUu7dxY0tkG9a0Yn8J7uGpkXjaBZ3KXjKN6t4gkt9uyVgDg8HySuUC2CoTSz-oOJjfADHSNRwTMcN5u7YuUm3gu-KKyEKDno7EA4lf33e_2YBBgpxeJc4sBOjqj9I6-Wxqaut0I_L7kylc-_GbLGwyexk7uTPGF3dt9TxjTTlfOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/481d5e13ac.mp4?token=ike7sdFRdDCn5cEAvtuq4ZhU7xf48pyEWcOlpPTbRQsTAXP0poKYULklLyxQ7P14l23L_7LsIzxbqrngfmHsk0MNNiBJVIfZqp5nLjZj3OBSoaaKgd6EDOWt0x4Kk5fkkxoYrvGP0MRf2Ruzx1PsefqnWFWE04zvUAlAdJG1gQNUu7dxY0tkG9a0Yn8J7uGpkXjaBZ3KXjKN6t4gkt9uyVgDg8HySuUC2CoTSz-oOJjfADHSNRwTMcN5u7YuUm3gu-KKyEKDno7EA4lf33e_2YBBgpxeJc4sBOjqj9I6-Wxqaut0I_L7kylc-_GbLGwyexk7uTPGF3dt9TxjTTlfOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
اشتباه بزرگی که ایرانی‌ها مرتکب شدند حمله به همسایگانشان در شورای همکاری خلیج فارس، همسایگانشان در خلیج فارس بود، زیرا ما متحدان بسیار خوبی داشتیم که شاید در مورد پول با ما کاملاً شفاف نبودند، پول ایران که در سیستم‌های بانکی آنها بود، ناگهان بسیار مطیع شدند و حاضر شدند حساب‌ها را تحویل دهند یا به ما در مسدود کردن حساب‌ها کمک کنند.
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/13097" target="_blank">📅 22:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13096">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کانال ۱۵ اسرائیل: گسترش عملیات اسرائیل در لبنان با هماهنگی دولت آمریکا انجام شد.
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/13096" target="_blank">📅 22:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13095">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">جروزالم پست: منابع به واشنگتن پست مدعی شدند که مجتبی خامنه‌ای، رهبر ایران، هنوز به آخرین پیشنهادات ایالات متحده، از جمله تفاهم‌ نامه‌ای که در جریان مذاکرات اخیر مورد توافق قرار گرفت، پاسخی نداده است.
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/13095" target="_blank">📅 21:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13094">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">عراقچی: ویزای تیم ملی فوتبال ظرف یک تا دو روز آینده صادر می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/13094" target="_blank">📅 21:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13093">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37fe276eb1.mp4?token=qy3NzI15bcthcv-o5xbxNAj63a51fo26fFRp3ZVE9tbxWln-q2IK4MjkFHaffzA6ZHPtcxxyjMeM7BIf3wrM4K864jA3aJsuxxs5r6WAHqQxMQ7XoD48siDl30YgURfWeZxnQ0pc6iKsJuL9uaO6GvD77umuY_3Js6gf7t50oxdj2vNx0K5XNLxIdioHauRhN7wg4VvDljMQ3HQgJY_5gYuIBZn5q9GAx__QVEieXYMrG4AV2Z3ofklymZvEmkBwyepqRfLCoXsKe86Ur32HgdnOFYuHzDYwNudmBrTuBW6szhnVVPl_SNFKQNOJyx9ZiZWohNIst0YC2at5C5RxAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37fe276eb1.mp4?token=qy3NzI15bcthcv-o5xbxNAj63a51fo26fFRp3ZVE9tbxWln-q2IK4MjkFHaffzA6ZHPtcxxyjMeM7BIf3wrM4K864jA3aJsuxxs5r6WAHqQxMQ7XoD48siDl30YgURfWeZxnQ0pc6iKsJuL9uaO6GvD77umuY_3Js6gf7t50oxdj2vNx0K5XNLxIdioHauRhN7wg4VvDljMQ3HQgJY_5gYuIBZn5q9GAx__QVEieXYMrG4AV2Z3ofklymZvEmkBwyepqRfLCoXsKe86Ur32HgdnOFYuHzDYwNudmBrTuBW6szhnVVPl_SNFKQNOJyx9ZiZWohNIst0YC2at5C5RxAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی:
آنها در تلاشند تا قانون شریعت را نه در دمشق یا تهران، بلکه در خیابان‌های بلژیک، خیابان‌های پاریس، خیابان‌های لندن تحمیل کنند.
تا چه حد اجازه می‌دهید این رادیکالیسم ادامه یابد؟ این تهدیدی مستقیم برای ثبات و جمعیت‌شناسی اروپا است!
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/13093" target="_blank">📅 21:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13092">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">منابع اسرائیلی:ترامپ در تماس تلفنی آخر خود با بنیامین نتانیاهو اعلام کرد که در صورت همکاری با واشنگتن برای این تفاهم‌ نامه 60 روزه موقت اسرائیل کاملا در لبنان و غزه آزادی عمل خواهد داشت
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/13092" target="_blank">📅 21:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13091">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">به گزارش رسانه‌های محلی، فعالیت جت‌های جنگنده بر فراز کرج در استان البرز  گزارش شده است.
@withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/13091" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13090">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">صبح امروز سپاه اعلام کرده یک پهپاد MQ-1 را در نزدیکی جزیره قشم سرنگون کرده است. هرچند اسرائیل یا آمریکا این موضوع را تأیید نکرده‌اند، اما چند ساعت بعد یک حمله در همان منطقه انجام شده است. منابع می‌گویند در این حمله، «محسن سپاسیان» (مسئول تدارکات سپاه هوافضا در استان) و «ستوان سینا نجارپور» کشته شده‌اند. تاکنون هیچ طرفی مسئولیت حمله را بر عهده نگرفته است و این خبر را تایید نکرده است
@withyashar</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/13090" target="_blank">📅 21:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13089">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/13089" target="_blank">📅 21:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13088">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">زرشکیان قهر کرد !  اینترنشنال: مسعود پزشکیان با ارسال نامه‌ای به دفتر مجتبی خامنه‌ای خواهان استعفا از سمت خودش شده. @withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/13088" target="_blank">📅 21:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13087">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/withyashar/13087" target="_blank">📅 21:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13086">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/13086" target="_blank">📅 21:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13085">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNd</strong></div>
<div class="tg-text">مشکلش چیه اصلا همین امشب باشه چه بهتر! هرچه زودتر بهتر اصلا! خیلی زودتر از اینا حتییییی
🫠
🫠
🫠</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/13085" target="_blank">📅 21:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13084">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">و اینکه لطفا خودت هم یه پست بذار ما شاهزاده رو تگ کنیم</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/13084" target="_blank">📅 21:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13083">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">قرار‌ ما فردا شب ۱۱:۱۱ دقیقه تهران</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/13083" target="_blank">📅 21:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13082">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/13082" target="_blank">📅 21:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13080">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromT</strong></div>
<div class="tg-text">مگه امروز یکشنبه نیست؟
😅
قرار نبود دوشنبه باشه؟</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/13080" target="_blank">📅 21:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13078">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/13078" target="_blank">📅 20:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13077">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">متن کامنت بررسی ‌کنید
جناب شاهزاده رضا پهلوی گرامی،
پدر ، این پیام، جمع‌بندی دیدگاه‌ها و پیشنهادهای گروهی از ایرانیان داخل و خارج کشور با هدف تقویت انسجام ملی و ایجاد مسیر عملی برای دوران پیش از گذار است.
عناوین چکیده از هزاران پیغام مردمی به‌صورت خلاصه:
* ضرورت ایجاد ساختار منسجم برای سازماندهی نیروهای مردمی داخل و خارج
* همگرایی و اتحاد جریان‌های مختلف مخالف
* ارائه نقشه راه و چارچوب زمانی شفاف برای اقدامات جمعی
* آمادگی میدانی و سازوکارهای حمایتی در شرایط بحران
* تقویت تیم‌های مشورتی، تخصصی و شفافیت در تصمیم‌گیری
* توجه فوری به بحران معیشت و فشار اقتصادی مردم
* ارتباط مستقیم‌تر و مستمر با جامعه
جمع‌بندی: جامعه آماده تغییر است، اما این مسیر نیازمند انسجام، شفافیت و ساختار اجرایی روشن است.
درخواست پایانی: فراهم شدن امکان ارتباط مستقیم برای انتقال منظم دیدگاه‌ها و ادامه گفت‌وگو با جناب آقای یاشار « yashar » که از طرف ما به عنوان گردآورنده و ارتباط‌گیرنده این مجموعه دیدگاه‌ها معرفی و تایید میشود.
این متن نسخه خلاصه‌شده است و نسخه کامل از طریق ایمیل، دایرکت و … ارسال  شده است. ممنون از توجه شما
پاینده ایران  و درود بر خاندان ایران ساز پهلوی
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/13077" target="_blank">📅 20:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13076">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">EmergPhase_FA.pdf</div>
  <div class="tg-doc-extra">6.2 MB</div>
</div>
<a href="https://t.me/withyashar/13076" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پروژه شکوفایی ایران : برنامه اضطرار
🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/13076" target="_blank">📅 20:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13075">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/13075" target="_blank">📅 20:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13074">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM.!</strong></div>
<div class="tg-text">درود، میشه بی زحمت اون 250 صفحه رو بفرستی تو گروه ممنونم
🙏
🙏
🙏</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/13074" target="_blank">📅 20:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13073">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">با توجه به اینکه بخش محدودی از دفترچه پروژه شکوفایی«اضطرار» حدود ۱۰٪ به دوران پیش از تغییر رژیم «زمان حال» اختصاص دارد، لازم است به دغدغه‌ها و پرسش‌های مردم در این حوزه توجه بیشتری شود و برای آن‌ها برنامه‌ریزی دقیق‌تر و اقدامات سریع‌تری در نظر گرفته شود، زیرا این موضوعات برای افکار عمومی اهمیت مستقیم و فوری دارند.
اینم به متن اضافه میکنم</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/13073" target="_blank">📅 20:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13072">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">زرشکیان قهر کرد !
اینترنشنال: مسعود پزشکیان با ارسال نامه‌ای به دفتر مجتبی خامنه‌ای خواهان استعفا از سمت خودش شده.
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/13072" target="_blank">📅 20:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13071">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">متن چکیده نسخه  ۲۱  بیانیه جمعی از ایرانیان داخل و خارج کشور خطاب به شاهزاده رضا پهلوی  پدر گرامی ،  این متن جمع‌بندی مجموعه‌ای از دیدگاه‌ها، نگرانی‌ها و پیشنهادهای طیف گسترده‌ای از ایرانیان داخل و خارج کشور است که با هدف تقویت انسجام ملی، افزایش شفافیت و…</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/13071" target="_blank">📅 19:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13070">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/13070" target="_blank">📅 19:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13069">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/13069" target="_blank">📅 19:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13068">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromabol</strong></div>
<div class="tg-text">یاشار جان سلام یه سوال فنی داشتم ،
بعد بر اندازی و سقوط ایده برخورد شما با عرزشی یا حالا بسیجی که دستش به خونی آلوده نیست صرفا موج سوار بود یا اصلا همراه بوده چیه اوناهم باید مجازات بشن یا باید گذشت و همکاری کرد ؟</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/13068" target="_blank">📅 19:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13067">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkKelrGdi9c_qUvE9HKl621z1qnnnSShBlyQNrcVeituMj8b_oGYqNp6jphyrOfy-JooJHiX2Cp8HE6XfN4rTzEMc1cRwFSgQlDPMIXPjXdmNyq-bXH68JorCNbf6tKZoumNZKhvKSBoswFz2_jld563Acyv2ClbyM8ef5vrlo4r6WEcv6F6Jwno_aW0O6Pq9r7FlG8wbHdLqDtnYAv9VLd7ktCWiIfXLcuzSNqUROVtdVwH7eECylkOiGDx_aexJveLl_TKVj80BNY3rwyruuWMexWmwofbDATg0bwpeEUj9lP3I3bovsi66zOlWJeMXwVGrv_iF3gTb8b20jk2GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی ایرانی به نام «IRGC TOLL COLLECT» به معنی « اخذ عوارض توسط سپاه پاسداران » در تنگه هرمز ظاهر شده است
@withyashar
مفتبر جاده هرمزه
🤣
تلکه بگیر سر گردنه</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/13067" target="_blank">📅 19:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13066">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یاشار همین الان مرکز تهران دو صدا  مهیب انفجار مانند ۱۹:۳۲
@withyashar</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/13066" target="_blank">📅 19:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13065">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/13065" target="_blank">📅 19:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13064">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShiva Abdolahi</strong></div>
<div class="tg-text">من اون 250 صفحه دوره گذار و خوندم واسه وضعیت الان ما بیشتر شبیه رویا میمونه
الان برنامه برای سقوط مهمه
که هیچی در موردش توضیح نمیدن
🤦‍♀
🤦‍♀
🤦‍♀</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/13064" target="_blank">📅 19:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13063">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/13063" target="_blank">📅 19:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13062">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/13062" target="_blank">📅 19:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13061">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سی‌ان‌ان: ترامپ با آزادسازی هرگونه دارایی ایران در توافق احتمالی مخالفت کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/13061" target="_blank">📅 19:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13060">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">متن چکیده نسخه  ۲۱  بیانیه جمعی از ایرانیان داخل و خارج کشور خطاب به شاهزاده رضا پهلوی  پدر گرامی ،  این متن جمع‌بندی مجموعه‌ای از دیدگاه‌ها، نگرانی‌ها و پیشنهادهای طیف گسترده‌ای از ایرانیان داخل و خارج کشور است که با هدف تقویت انسجام ملی، افزایش شفافیت و…</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/13060" target="_blank">📅 19:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13059">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/withyashar/13059" target="_blank">📅 19:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13058">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/13058" target="_blank">📅 18:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13057">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLord</strong></div>
<div class="tg-text">آقا یاشار آخرش یک کم باید محکم تر باشه شما‌ فقط پیگیر دیدگاه‌ها‌ نیستی بلکه کلی قرار‌ راه کار بدی
درسته ارتش یک‌نفره هستی ولی تعداد‌ زیادی از مردم‌ با‌ شما‌ هستن . آخرش باید قوی تر بسته بشه</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/13057" target="_blank">📅 18:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13056">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/13056" target="_blank">📅 18:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13055">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/withyashar/13055" target="_blank">📅 18:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13053">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">متن چکیده نسخه  ۲۱  بیانیه جمعی از ایرانیان داخل و خارج کشور خطاب به شاهزاده رضا پهلوی  پدر گرامی ،  این متن جمع‌بندی مجموعه‌ای از دیدگاه‌ها، نگرانی‌ها و پیشنهادهای طیف گسترده‌ای از ایرانیان داخل و خارج کشور است که با هدف تقویت انسجام ملی، افزایش شفافیت و…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/withyashar/13053" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13052">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/13052" target="_blank">📅 17:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13051">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">متن چکیده نسخه  ۲۱
بیانیه جمعی از ایرانیان داخل و خارج کشور خطاب به شاهزاده رضا پهلوی
پدر گرامی ،
این متن جمع‌بندی مجموعه‌ای از دیدگاه‌ها، نگرانی‌ها و پیشنهادهای طیف گسترده‌ای از ایرانیان داخل و خارج کشور است که با هدف تقویت انسجام ملی، افزایش شفافیت و ایجاد مسیر عملی برای آینده ایران ارائه می‌شود.
برای انتقال دقیق‌تر این دیدگاه‌ها، پیگیری پیشنهادهای مطرح‌شده و ایجاد ارتباطی مؤثرتر میان مردم و جنابعالی، لازم است امکان برقراری ارتباط مستقیم با اینجانب ، به عنوان گردآورنده و منتقل‌کننده این مجموعه نظرات فراهم شود. از همین رو، علاوه بر طرح مطالبات و پیشنهادهای مطرح‌شده در این بیانیه، یکی از اهداف اصلی ارسال آن ایجاد این مسیر ارتباطی و گفت‌وگو مستقیم است
با توجه به اینکه بخش محدودی از دفترچه پروژه شکوفایی«اضطرار» حدود ۱۰٪ به دوران پیش از تغییر رژیم «زمان حال» اختصاص دارد، لازم است به دغدغه‌ها و پرسش‌های مردم در این حوزه توجه بیشتری شود و برای آن‌ها برنامه‌ریزی دقیق‌تر و اقدامات سریع‌تری در نظر گرفته شود، زیرا این موضوعات برای افکار عمومی اهمیت مستقیم و فوری دارند.
با نظر جمع مطالب مطرح‌شده در این پیام بر خلاف همیشه، عمدتاً ناظر بر مرحله پیش از گذار و چگونگی تسهیل روند تغییر رژیم کنونی کشور است
1. ضرورت ایجاد ساختار یا پلتفرم سازماندهی ملی
مطالبه گسترده مردم، ایجاد یک ساختار منسجم است که بتواند نیروهای مردمی داخل و خارج کشور را شبکه‌سازی کرده، نقش‌ها را مشخص کند و از پراکندگی و موازی‌کاری جلوگیری نماید.
2. انسجام و اتحاد میان جریان‌های مختلف مخالف
درخواست جدی جامعه، ایجاد سازوکاری برای همگرایی جریان‌ها و گروه‌های مختلف مخالف حکومت است تا انرژی سیاسی و اجتماعی در مسیر مشترک و هماهنگ قرار گیرد.
3. ضرورت اعلام چارچوب زمانی و نقشه راه عملی
یکی از دغدغه‌های اصلی مردم، نبود زمان‌بندی و مسیر روشن برای اقدامات جمعی است.
مطالبه عمومی این است که سناریوها و مراحل حرکت به‌صورت شفاف و مرحله‌بندی‌شده مشخص شوند و در صورت امکان، برای اقدامات جمعی و هماهنگ، چارچوب‌های زمانی روشن و قابل فهم اعلام گردد.
4. آمادگی میدانی و سازوکارهای حمایتی در شرایط بحران
بخش قابل توجهی از پیام‌ها بر ضرورت ایجاد سازوکارهای حمایتی و سازمانی برای شرایط بحرانی تأکید دارد تا از طریق شبکه‌های امن، هماهنگی اجتماعی و توانمندسازی، هزینه انسانی تحولات کاهش یابد.
5. تقویت ساختار مشورتی، ارتباطات و شفافیت عملکرد
یکی از مطالبات اصلی، تقویت همزمان ساختار مشورتی، ارتباطی و شفافیت عملکرد است.
در این چارچوب پیشنهاد می‌شود:
گسترش تیم مشاوران و کارشناسان در حوزه‌های مختلف از جمله سیاسی، اقتصادی، اجتماعی، رسانه‌ای و امنیتی
استفاده از متخصصان حوزه امنیت، مدیریت بحران و مطالعات راهبردی در کنار سایر تخصص‌ها
تقویت و حرفه‌ای‌سازی نقش رسانه‌ای و ارتباطی
ایجاد ارتباط مستمر و مؤثر با مردم و مشارکت گروه‌های مختلف اجتماعی
فراهم کردن زمینه ورود دیدگاه‌ها و ایده‌های جدید از جریان‌های تخصصی و فکری مختلف
افزایش شفافیت در عملکرد و تصمیم‌گیری‌ها همراه با گزارش‌دهی منظم
هدف از این پیشنهادها، افزایش اعتماد عمومی، ارتقای کیفیت تصمیم‌سازی و تقویت هماهنگی میان ظرفیت‌های مختلف جامعه است.
6. معیشت و وضعیت اقتصادی مردم
در کنار موضوعات سیاسی، بحران معیشتی یکی از اصلی‌ترین فشارهای روزمره مردم است.
درخواست عمومی این است که در کنار برنامه‌های کلان،
راهکارهایی برای کاهش فشار اقتصادی و حمایت از اقشار آسیب‌پذیر در حال حاضر
نیز در نظر گرفته شود.
7. ارتباط مستقیم‌تر با جامعه و گروه‌های مختلف
مردم خواستار ارتباط فعال‌تر، مستقیم‌تر و مستمرتر میان رهبری اپوزیسیون و بدنه اجتماعی هستند تا اعتماد، شفافیت و هماهنگی افزایش یابد.
جمع‌بندی
در مجموع، پیام مشترک این دیدگاه‌ها چنین است:
جامعه ایران آماده تغییر است، اما این مسیر تنها با انسجام، شفافیت، ساختار اجرایی روشن و ارتباط واقعی با مردم ممکن می‌شود. هدف این پیام فقط بیان مشکلات نیست، بلکه ایجاد مسیری برای رسیدن به راهکارهای عملی از طریق همین ارتباط است
⸻
درخواست پایانی (از طرف جمع امضاکنندگان)
در پایان، جمعی از امضاکنندگان و نمایندگان این دیدگاه‌ها، با نهایت احترام درخواست دارند امکان ارتباط مستقیم برای انتقال منظم دیدگاه‌ها، هماهنگی بیشتر و ادامه گفت‌وگو فراهم گردد و پاسخ این پیام  ارسال شود.
این جمع، جناب آقای
یاشار
را به عنوان نماینده و پیگیر دیدگاه‌های مردم معرفی می‌نماید.
راه‌های ارتباطی:
….
پاینده ایران
و درود بر خاندان ایران‌ساز پهلوی
@withyashar</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/13051" target="_blank">📅 17:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13050">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205d44aab0.mp4?token=kyeiHcLALmrlL7s0Y5mOhxn6Ppng7KRDWm-yDJMpsROwY7ST_65IZAROqQcWWUqH6-brjdtqZf0MmlY4hmTjTsZjGv2ckE29azHKrsOg5UO0NWAVa502UlbaVBTYE5XhRqObHU8C4G6GUugjsVlolKo-c_PpWiMdojntQccWJL2e0LrOwy78Q-U7XXRcOs0HLP4vWMIPxJQSJOPHexN_UzpxDtPcX1j8JAZH1AKtHavejhBxdv_sVtxsY36iJPKrNtn9ApMPspz8kmcfoL6b34YqQ_vNZIY66_DbGy9yP1niOvtCzwrpsWc00vVbtdNTS4Z40bpJqbIqr-4RPK-ldQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205d44aab0.mp4?token=kyeiHcLALmrlL7s0Y5mOhxn6Ppng7KRDWm-yDJMpsROwY7ST_65IZAROqQcWWUqH6-brjdtqZf0MmlY4hmTjTsZjGv2ckE29azHKrsOg5UO0NWAVa502UlbaVBTYE5XhRqObHU8C4G6GUugjsVlolKo-c_PpWiMdojntQccWJL2e0LrOwy78Q-U7XXRcOs0HLP4vWMIPxJQSJOPHexN_UzpxDtPcX1j8JAZH1AKtHavejhBxdv_sVtxsY36iJPKrNtn9ApMPspz8kmcfoL6b34YqQ_vNZIY66_DbGy9yP1niOvtCzwrpsWc00vVbtdNTS4Z40bpJqbIqr-4RPK-ldQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از یه زاویه دیگه اتوبان ستاری ,جنت آباد جنوبی
@withyashar</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/withyashar/13050" target="_blank">📅 17:18 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
