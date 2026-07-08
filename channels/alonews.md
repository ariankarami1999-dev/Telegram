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
<img src="https://cdn4.telesco.pe/file/EqFI2UokJEolmIbK9pNbdtcJ1NZQQurgw03JUc5bzQVSn_7Zw_QFba2wIJaBfJ4Dv0k93QsTHbAUtxGlBPqQVt_3WYlG7Xi7sUmGrNWCYv6NTq6nIJk6N3eCwif8MSSwIUQTHeUQMsmzP7OQtVLvzlCVg0REnEWNabnNRfu6mwB3l9HNUZnogGONSsTN8RrhNI11N0J-I3HRGz7ouemnTT_TLadha9vbVlJHoXtU000ed42pKxxQWhs9hibs1eOyvTN7i_kri4jx4xX28LHZDSerfA9IUY8TJKQG6xVJlUFnos2CmCmGHNIuOiOMbkTnnAWuI6eo5mvl9-jDZf5aqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 925K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 15:30:20</div>
<hr>

<div class="tg-post" id="msg-132506">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RONb0U4gq5f2EEllfcNomk9spNv59GPtn1P5jh5Nr7JGVO1u0obsGIQEM6sS-cKLYa0wGog79KVuowLmeHG_2UMvV2GLhFqDo70pXmrbuU_wHpX7In0cDKxNqRokidtx4kC9X3V-riwnqlaptm5VKXrdolWx1ViWqAlM-U_bNy-h4Nn1qN3JfosbLsl68r7ZCN65BjYb7ZYfmQPlYWq5IDc3EbCaD5ungT-y9Yy5_iP2gSHwIgpl5eXeFrMlyqWHzLDi5GOH8Ilqg8IxLiGM-KimNVfDwwwBdjfHDH5a2BeIO04kf5M8N8Iwm8DzkCV-oFfVn4mp2n19foTRc0ukwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عزت‌الله ضرغامی: سفیر ‎ترکیه را احضار کنید و به او هشدار دهید
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/132506" target="_blank">📅 15:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132505">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
فایننشال تایمز: عربستان انتقال‌های بانکی از حساب‌های خود به دریافت‌کنندگان در امارات را به تأخیر می‌اندازد یا مسدود می‌کند
🔴
این مسئله تجارت را مختل و برخی شرکت‌ها را مجبور کرده که وجوه خود را از طریق بحرین منتقل یا از روش‌های پرداختی گران‌تر استفاده کنند
🔴
ریاض اعمال محدودیت‌های خاص علیه یک کشور مشخص را رد کرده و گفته بانک‌ها اقدامات استاندارد مبتنی بر ارزیابی ریسک را اجرا می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/132505" target="_blank">📅 15:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132504">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ام تی وی : لبنان موضع خود را تغییر داد و با رفع نگرانی‌هایش، موافقت کرد تا در مذاکرات رم شرکت کند. در همین حال، طرف آمریکایی از شرکت خود و حمایت از این مذاکرات با اسرائیل اطمینان داد.
🔴
این بدان معناست که این مذاکرات صرفاً دو جانبه بین لبنان و اسرائیل نخواهد بود، بلکه یک مذاکره سه جانبه با حمایت آمریکا خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/132504" target="_blank">📅 15:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132503">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQCm_prhauNjSkBrb7ZkWQRTbtcq7C0-q2FlYqk3u490SCv8fSKsl5vyB8KXE3y2Be2GrwJlfluFjxglX7PC69bcR1P5PVTUWPJgRUQpigen45o0TQaXdXXTWapPcHgXTpgSAb1zA61KvlMV3R2LbLj2bFUckDyZVx_mjImpHfbipoUPkXFsan666zG25yiUKil4KX68Naa6_7yNfjEpg6oUrGqZ6RILwA5Ky7fAhIVWqZGiAWUVJs8Ott-cFz_qXN6y21GcilzgiVIh0hAkHCjaxYGaPCDaKChAzyaoLFIJBig9eFH8mCQEG93N8lRfMAkbM7BWEEaXnm7a5_ve1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترافیک دریایی کریدور عمان در تنگه هرمز به صفر رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/132503" target="_blank">📅 15:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132502">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7EP1FE8Z_KK05RWY5JKqGvBYfH4XX75iJVeGaGQ0RLXlda3MO6FPZBKYjrTKGHpDgBgBgMHrJoZ1OXMDg_55xkEWspeZvFPUCDaw6rnDe64kcOpp8BxwJc4nzSt5JviGXMScsnoO-Surg__ibra3NZUKUthe5896NOqyILJsgP87SF-ioqe_0efL7wq67dgBJZCAAiQ23v4pd-qb48VCCcyY4tjmwRbmEK1tbYGPex2q-PxC0-fuZTcKT7f5kPz8Uyk7k1z3z_T_t_DzLPCMFnKvgD5uPjgLnunNotMSkNC54tYQL77h4Ig_JiqAldj952Ioh5oSfxRd2VjNAscxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل عملیات تخریب در شهر ارنون در جنوب لبنان را انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/132502" target="_blank">📅 15:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132501">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
رئیس جمهور لبنان، ژوزف عون: من مسیر مذاکره را انتخاب کردم، زیرا نمی‌توانم بی‌تفاوت بمانم و تماشا کنم که کشورم به خاطر منافع یک کشور دیگر، به سوی نابودی پیش می‌رود.
🔴
فرآیند مذاکره از حمایت اکثر لبنانی‌ها، از جمله اعضای جامعه شیعه، برخوردار است؛ جامعه‌ای که در جنگ‌ها، سنگین‌ترین هزینه‌ها را پرداخت کرده است.
🔴
من مجبور بودم گامی بردارم که بتواند ویرانی و تخریبی را که توسط اسرائیل انجام می‌شود، متوقف کند و در نهایت، به پایان دادن به اشغال را به ارمغان بیاورد.
🔴
من انتظار دارم که سفر من به واشنگتن و ملاقاتم با رئیس جمهور ایالات متحده، نتایج مثبتی برای لبنان به همراه داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/132501" target="_blank">📅 15:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132500">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q-9kWWsSuDs3wfkMM4QnUEMKnvOSyWJospNYuDRxLYXKSDllIOY-_cyCgo06z9Lr4fk-4X_jdJyGM44beqkC4XFJ7EM00LciNlmza4h5AxTQrtMYncDLFHZNAJOo0dfB3sFPRV4k3854vuySyk0TRizDhFKAPk5ikjAe4wh4TdpReUJR1e24-IEr_2ScDq3aBebMUS1pRnbAcedosodHUWa9zv4ildbkYcCPK_O0JG8V49NzA5WcCwrVFoUKUgnDQRr4282MMTtgCLMXMOiEzfKogYyYq09M2f8TVnQmfH39poiVXEaNqvv5IVtlJ4dvP2W4SIQYfihA2HfGmYatSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اصلاحیه برنامه امتحانات نهایی پایه یازدهم تیر و مردادماه 1405
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/132500" target="_blank">📅 15:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132499">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4268fce83.mp4?token=DlwLAPtODX0pE6JLNqi3zqIUbELaDd32osnOE9GbNpErrS9Nnp8cZEmFPnZBHOWMa4fzPOXVAWEn_j1rz4ehQ7V9p6Lir-KydQaS2uyHxaqQOaqbgy4uzOPwCe3X98VbEmv0c2-jwmGtaSjiETHbhNffP4J4cUCkFY35AGJzkbXFXJqvKt5Xrmeu8Mfamspu1Siq7cUDNZIp5xosSxIobDHh7RTRgqUJ6b8WzwH70rUgrureuOQneP92kRhkQYuo6LVkI3f8hftrjXqkg4UXMly-kRxFXRK32GnZug00vuqHFAkjQ9a_yUm1OEfv26v_IwGyWe0w5YdXTe6UzRFQJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4268fce83.mp4?token=DlwLAPtODX0pE6JLNqi3zqIUbELaDd32osnOE9GbNpErrS9Nnp8cZEmFPnZBHOWMa4fzPOXVAWEn_j1rz4ehQ7V9p6Lir-KydQaS2uyHxaqQOaqbgy4uzOPwCe3X98VbEmv0c2-jwmGtaSjiETHbhNffP4J4cUCkFY35AGJzkbXFXJqvKt5Xrmeu8Mfamspu1Siq7cUDNZIp5xosSxIobDHh7RTRgqUJ6b8WzwH70rUgrureuOQneP92kRhkQYuo6LVkI3f8hftrjXqkg4UXMly-kRxFXRK32GnZug00vuqHFAkjQ9a_yUm1OEfv26v_IwGyWe0w5YdXTe6UzRFQJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دبیرکل ناتو: حملهٔ دیشب آمریکا به ایران کاملاً ضروری بود
🔴
فکر می‌کنم بسیار حیاتی است که آمریکا با قاطعیت و قدرت واکنش نشان دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/132499" target="_blank">📅 14:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132497">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avD1XXyHyr-I1fCO3ALRlrfWGYflI0kEidwQFXkyUgv3_LBCibd6I2a2n5keBaUEOiBRALFdFL1iY8Q35d-h4PeVxY-Rx-9_KoR-ifSjLz51JqFj5qFlKVFKN6ezLCIQ7TFR7S9cdnoVStZvWwaBjrn6UeAnf80AN5IL-VIDKdXf1RnmNmchnO9G38IzukbiZD4uguHepcWsz252Y6YIo_tanKJ6fgfTV5IjpOVKo9Qmwrs5wUbrdlvnuEsNoChGvOu_4wBfYPuZkuONHHpm6cqenpv8x58l0O_NR2Q3ejW11AXZY8cm4T_tIWFR5XDLAystYmP7JLVfxggMKdwySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55185ece21.mp4?token=oGwBtzsO6MN-7gFZKuqhyhWxHkOPQJ6ddta3wbS-cTUSyjNUuJKXS3KPU7z-5RlL1gOjKXfVOl3TgsnrLTmv5bSOCSLqzsPZFg77ssvdy64WyxmiA2N18ZvNhd11ugaJdT72H1-9AS3MBlVni39NmSDzw7At28mw67nUH_ET2lC7VMDKIPnibrlz2EKFDLGmbap5XGnwTEBV7kLsls7Z9NyY6GS5P44Z2r_ylXAB2KGosSP4fqWZWd7z0DAQ95rBrXbfq9I9EzsDsSIreyrix8LiCk0JBTPAf7o2J3iFBoFCXDNzFb8xfYH5ZtPWDrRKcw-sPzS_eNis3zUYaBoWCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55185ece21.mp4?token=oGwBtzsO6MN-7gFZKuqhyhWxHkOPQJ6ddta3wbS-cTUSyjNUuJKXS3KPU7z-5RlL1gOjKXfVOl3TgsnrLTmv5bSOCSLqzsPZFg77ssvdy64WyxmiA2N18ZvNhd11ugaJdT72H1-9AS3MBlVni39NmSDzw7At28mw67nUH_ET2lC7VMDKIPnibrlz2EKFDLGmbap5XGnwTEBV7kLsls7Z9NyY6GS5P44Z2r_ylXAB2KGosSP4fqWZWd7z0DAQ95rBrXbfq9I9EzsDsSIreyrix8LiCk0JBTPAf7o2J3iFBoFCXDNzFb8xfYH5ZtPWDrRKcw-sPzS_eNis3zUYaBoWCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایالات متحده، هواپیماهای تانکر خود را از فرودگاه بن گوریون در اسرائیل به پایگاه‌های دیگر در خاورمیانه منتقل می‌کند.
🔴
تقریباً 15 فروند از هواپیماهای تانکر سوخت‌رسانی نیروی هوایی ایالات متحده از فرودگاه بن گوریون در مرکز اسرائیل خارج شده و به پایگاه‌های منطقه‌ای دیگر، از جمله پایگاه هوایی الاودهید در قطر، منتقل شده‌اند.
🔴
تا تاریخ 24 ژوئن، حدود 47 فروند از این هواپیماها همچنان در این فرودگاه مستقر هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/132497" target="_blank">📅 14:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132496">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tE2z5vM-BvxntVBTcYQXQm24X-ugjxRvMdyMv7OxKV9rw9Q3FnpepgiAFCYiyyiXkHnjPnyO4dx9r3t0C8tVr_qQ8LCcZjNrMP_Ld1ETJJM2eunMjyjbL1QPplzDcErh4Xfqc_wPAFcszMfdhLthwycqD28Z6Ocvtad9TdtjAQt1I0PidBKCN14IizI5lxvpKCbJ-9sOOiCj6FMS3LLwizxcOdXXWQR2FdyfO_iFlL3CW4QrJC3zojCpk3M_teqaGGDeuL9Evxaciu6X5f7tkrvy9NKCAYrR-RQqODJamEva34OurBz47uWnd_TrKH-paX8jUDu5ytpXdzxCiH8R0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر ماهواره‌ای از یکی از سایت‌های پدافند هوایی ارتش در جنوب کشور نشان می‌دهد یک لانچر صیاد-2/3، یک رادار کنترل آتش نجم-804 بی و خودروی ژنراتور همگی در جنگ اخیر مورد هدف قرار گرفته و سرکوب شده‌اند. علاوه‌بر سامانه‌ها، شلترهایی که طی یک سال اخیر ساخته شده بودند نیز در اثر اصابت بمب‌های SDB-1 آسیب دیده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/132496" target="_blank">📅 14:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132495">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
موبایل در امتحانات دانشگاه آزاد، آزاد شد
🔴
بر اساس اعلام دانشگاه آزاد، همراه داشتن تلفن همراه در جلسه آزمون پایان ترم تحصیلات تکمیلی با رعایت ضوابط و تحت نظارت مراقبان مجاز است. همچنین در امتحانات نظری دوره دکتری (غیرپزشکی)، استفاده از ابزارهای هوش مصنوعی نیز بلامانع خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/132495" target="_blank">📅 14:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132494">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGey7cunPzJXZzBxSSuQ6UJcONCD4Xe7ANldTDTC8pJ5DTA__fh66p1atJfXGFpyg-0qaxQn5RdNK0mtvjEt0QrkyWnjAKuf_nBfahha4SIS7N9Z8g0qwhgs-RohixuyTrA7J-sW5Z8zCEyBeDgw6lWAVulRSfeBCDg4LxcRHTsufj_2sDk-wVwbch7ygcHYIH6SMr3V-tPvBL2NarW0duBuv0unJ1le1wQasjv94J8ug-LZ1RW1UFghlwwhVw4Jr2_lPpL582UQZENzuD-_I2VKUOPzhuKcU40TWhuM5isQeChL-xS7QFdeHPyTUMJk2Xy8xLGqBg-DDGxOEZH_7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی هوایی اوکراین گزارش داد که یک هواپیمای جنگنده روسی را سرنگون کرده است
🔴
آنها محل سرنگونی این هواپیما را فاش نکردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/132494" target="_blank">📅 14:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132493">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
فارس: ایران باید پایان رسمی تفاهم را اعلام کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/132493" target="_blank">📅 14:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132492">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
مردم محلی شمال شرق تهران میگویند پدافند در پارچین و خجیر فعال گردیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/132492" target="_blank">📅 14:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132491">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
یک کشتی در تنگه هرمز مورد حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/132491" target="_blank">📅 14:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132490">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
چین به آمریکا و ایران درباره «شعله‌ور شدن دوباره جنگ» هشدار داد و از هر دو طرف خواست اختلافات را از طریق گفت‌وگو و دیپلماسی حل کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/132490" target="_blank">📅 14:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132489">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
جو کنت، مدیر سابق مرکز مبارزه با تروریسم دولت ترامپ: حالا که تفاهم‌نامه با ایران عملاً مرده، دوباره به تلاش جهت یافتن یک راه‌حل نظامی برای تنگه هرمز بازگشته‌ایم
🔴
مشکل این است که ما این تفاهم‌نامه را امضا کردیم، چون هیچ راه نظامی‌ای وجود نداشت
🔴
بهترین گزینه این است که به سادگی کنار بکشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/132489" target="_blank">📅 14:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132488">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل اعلام کرد فرمانده یک گروه ویژه «حماس» را در پی یک حمله هوایی به جنوب غزه هدف گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132488" target="_blank">📅 14:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132487">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
اسموتریچ، وزیر اقتصاد اسرائیل، درباره ترکیه: ما برای هر سناریویی آماده‌سازی می‌کنیم
🔴
ما درک می‌کنیم که یک تهدید وجود دارد و اجازه نخواهیم داد که چنین رژیمی، وجود اسرائیل را تهدید کند، همانطور که اجازه ندادیم و نخواهیم داد که رژیم ایران این کار را انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/132487" target="_blank">📅 14:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132486">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWRCgy_tV26lbay1LBz3dfH02LAHEZwoAbayVWRYCxhOXU51oK6YvNdU0cohd43UHB0o6RTSzmWrv7LnjCaLFxh2YiVd0S9ifwUN1aSpZLDbuU3ZX-INYYAjImKergkM7MNdoUluWryXQ6IyjzkDsQxkvUaHHyfiGOFxhR9GKVCFomifO-RMqpoZA-IxIsaqRCh2sSZyiOqv2bRiYrQbTC1kkRpHxwFnwt0XaCu-IwplD5GKyxUxuLcZ3CkDp-FFEfzonEugQFXiwJafKdWoWjFtceGWUhVM2JENqbi94-etIMUuR6K9exKaYxuQRbGocnK1s_aMZm4fmo5RvkKYcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای سوخت‌رسان نیروی هوایی آمریکا هنگام پرواز بر فراز تنگه هرمز در حال خاموش کردن فرستنده‌های شناسایی (ترانسپوندر) خود هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/132486" target="_blank">📅 14:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132485">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
اتحادیه اروپا: حملات ایران علیه بحرین و کویت غیرقابل قبول است و حملات به کشتی‌ها در تنگه هرمز را ناقض مفاد تفاهم‌نامه می‌دانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/132485" target="_blank">📅 14:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132484">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری / رویترز: نفتکش آمریکایی شورون در دریای سیاه هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/132484" target="_blank">📅 14:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132483">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سازمان دریایی بین‌المللی: ۶۰۰۰ دریانورد همچنان در تنگه هرمز به سر می‌برند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/132483" target="_blank">📅 14:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132482">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری / یک مقام ارشد اماراتی به روزنامه هاآرتز: جمهوری اسلامی ایران امشب بهای بسیار سنگینی خواهد پرداخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/132482" target="_blank">📅 14:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132481">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وزارت خارجه عمان: تشدید تنش‌ها در منطقه، تهدیدی برای امنیت و ایمنی دریانوردی است
🔴
طرف‌های درگیری، راه‌حل‌های دیپلماتیک را در اولویت قرار دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/132481" target="_blank">📅 14:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132480">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ: ما دیشب با رئیس جمهور اردوغان شام خوردیم. من به آن نمره ۱۰، شاید ۱۲ می‌دهم.
🔴
ما جلسات بسیار خوبی داشتیم، به خصوص با ترکیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/132480" target="_blank">📅 14:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132479">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
قیمت گاز در بورس‌ های اروپایی پس از اظهارات ترامپ مبنی بر پایان توافق‌نامه با ایران، افزایش چشمگیری داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/132479" target="_blank">📅 13:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132475">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KycJbjLYMOm1eKB68l01zVt_psyyXYaXyO7FX1u111soyjZp0tBhDxZLpDmCOzuZdX7PeKbgryLiPQSFywQumng_wKU4gITVon9TK8CwXSzJbMFiCjmZm2eDX_MyI2M1H-97mGahymDqedP7233uJxTImR-5DgvX481X_G8RHlVDYGBW5lnx8vqaAXSUdT3JsahxESW_rsYYpc4i6KkPdH3lBGmdC6QqhNaYzYydohyK6JMiGqym826hJhUx8XFIqp71VCATox0eoUqt-smPFDD_ZXYt_hlQbVs_dLzh1kE7EmaB8UA-9A-Q2ZPiMXVPepnH-RooLl6zE7k-RQiRDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MLqkj-zzHy7TzwV2iDtg2zkOrnEX9jS8FZjpxYFRYzPDD4nQy9KyHIDQ2QfZrWmV93YPO4fEo52fyhJyr36-mR8k5wamiaa8IMxM8oVTwn-1E9kgD_Z8nU-hKeQraSYBhWlfuwrDtO5IiFW_AKOSsy7rkG33GYNg0Vd9hv0vv5K2CjXEllOHiAtzdBQ25bEYDhPrAP2qrI7_s9D7mnMUEu3eWq1qsu67-RXh4ncUO7xpkm3aqmehgqBfgb5SXvTQvLDq8zl9QLat8KNufhW6tTng08yXDsZpcgDCuJw0e7osmkjN4BmFu6QLjxBdglmNonXOa60SQxn4YKHBdm3dwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BtG1l5l_4pHiVz14BPqfsC22SyURS7UU2cHmHz4OVWVo-5XzESiP4eoOArayUaYH0ZmEb-1PCU9J3VbCwwLE-86q-nJfXokNKOHofT-fHO0jwQKC55FBapunEnMHgm_jkrOrUvE-c-gqWpTm67VecILfTQFeKVrnXlraPDJd3ElWP2SEcJlo6M3trY3TgqEm-cPzawZhmdkkUOzVQ63kT7axW6PVhlj8SgzpHFufMm9P0TgWToihOK_oqdAUva4CZbGQiFYzGOrdRq7N1zZRn4CVH-X4-02ERpldh3bhHQ-NRBod9h-Lx120Az2Nom8SRHZUxQtdR92SVSN85NeGDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UjDYQROpt9G7w-UDo_dPTq0gwETwE4UYbSCTOLFLXkAGdmjiOHwIDrwzYV-4t37ANyIStJDITxrAxgDHibCf9X81RD-OcZ5VJNj1RGMk91WaOOTQHTWjgf3mydn2ji4beTYkJGSSetfFC6UycaWkO4ntu98wclO1YK41yvcwvA8LG5Fo6TyqpW_64P4ocJwaO_Y52Zq9zguiRmVlJB10yXoqz7Wj5nnOepmU5DWybGlItX8qu4qUHegaB6Z6AXh-3xz_j3FLnz3rsHigWlE4Fuh9Ls1JWkU6uI7Wdnf_RrhZ2VJVRnZHhc56Bw9YVO7Ulb1L1LkRmQylU0TOtV6sMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تسنیم با انتشار این تصاویر نوشت دیشب یه پهپاد MQ9 زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/132475" target="_blank">📅 13:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132474">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
کرملین: در برابر استقرار سلاح‌های هسته‌ای در کشورهای بالتیک، اقدامات متقابل اتخاذ خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/132474" target="_blank">📅 13:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132473">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t459HIflpDqCCWKz8PyLB7uZgkV2MXlY4iIumb_KkDthRcL6J44GxeaI0Qio1YCywfoShXJ6eVQI5jFFY6avcdFnJhezoALtmvJb7H8Y3E1Ih-of148ilJDxgOP0vJL0t-gnYRW_ubhmXJMe8OFWuXOlEy_fackGW3VwGtE1p3K_8Ysn90oDDBGcZH3hpxk8EOrjbhQ8H6KszgkrB9Nob5NYD6w7XOpKHDsE62tSbNmMXLDG7TJehIzxuhnIcjHQJwaanYeeUFVglZhyLiV0LxtEx76fa6F8ZsDExyrFC7YIeunsrx55eFKBqUY9tSav7W6yhAHQUGrgYqGx8B-Ksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاهده دود در آسمان بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/132473" target="_blank">📅 13:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132472">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6REXFr6wO1TON1Hy9rBXbHbxpcdBCza7hj0xSmVuaP41JnOhs4hWLsoe0hTJQIBAbG-tGjJmdpoceEG-dYDlUKnUBlMBsvvCqkMhWf4YFBSyVgm_FpkeoZcH1bG079rRQRseEl61efejjcrKAh3roFFFx7JSJbVXWeADZiv__WILExPl2o02Z0L0hgAxkMVrt4FdoTI6g-kFedN8aLhiWFvm9NN6cVvo-NzIVOUL8N0bYyykWsJQWyTePsnx7wfgex1uExk3Re3yiSu_7hj6iH2RGkZxvkmFGsyVVJtr7FT64XgshUmqG443-QqTTJaIAsPrXh92XNo-MoDNRKAVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات شدید تندروها به قالیباف و پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/132472" target="_blank">📅 13:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132471">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb8b1d87d.mp4?token=Jc2cOmvrzphNC7ntfBhg9Xzf-9E3Vf6-XxMbC0tQWYzr2JY5kFfDTzCODhT_b-p8AR7sUFvCwGsgJa2aR6Zbra9W6Nve0C-aGBEYmG9phIprPTP52c0mvPW5zcwwJ-JedTz_FgSsC355mt6X2U567Nug9E1CMLFmeyuMxDs0mR9SYfSz51rp264nhWBnhvaSvW_jY_SSDU-4Y8FG5cojbvBoz7iih0_02W_aVjTJ3tSmdGW8dukaSWDn3p2LTtWn7GpeuCyUqQnd0NkXqVIvUrfHMj2EFEdCH1PzW36dnXaA2CrcoKhh5sO5PTMHHpPpTFqAAWaqHRwJn4ya7nUvzTJIm1SWQtqFUSGLUruVbfLrbnjQmsft3A7OWzMg0oW0L_-8VIO0tm-W-gXheADmMrflHRDvKPAGXmCeWQaJN-ItGiMi_2x0cNUjNGTeRZbdvZl6gZdFPBXObxtDDaeW9on2O8LKj1my46BIToy8C7mI5KeYq6AK2fJMbrtQxpxzah-B0A7UlJtALVVH5reERvgZkkvyJa6NZvWblmhhr0o0yh1mTRWsckpAI8hMjkUMCip4xfGPcQw6XfgE39Ws5-tWRilhMJTRivQOuTq0Wg-UxYQPE8NvBhuv4PvbsGDZFXUOTAnB9Ap4uvIJO8HXICrRNkj5nXs0asZU8tfZPFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb8b1d87d.mp4?token=Jc2cOmvrzphNC7ntfBhg9Xzf-9E3Vf6-XxMbC0tQWYzr2JY5kFfDTzCODhT_b-p8AR7sUFvCwGsgJa2aR6Zbra9W6Nve0C-aGBEYmG9phIprPTP52c0mvPW5zcwwJ-JedTz_FgSsC355mt6X2U567Nug9E1CMLFmeyuMxDs0mR9SYfSz51rp264nhWBnhvaSvW_jY_SSDU-4Y8FG5cojbvBoz7iih0_02W_aVjTJ3tSmdGW8dukaSWDn3p2LTtWn7GpeuCyUqQnd0NkXqVIvUrfHMj2EFEdCH1PzW36dnXaA2CrcoKhh5sO5PTMHHpPpTFqAAWaqHRwJn4ya7nUvzTJIm1SWQtqFUSGLUruVbfLrbnjQmsft3A7OWzMg0oW0L_-8VIO0tm-W-gXheADmMrflHRDvKPAGXmCeWQaJN-ItGiMi_2x0cNUjNGTeRZbdvZl6gZdFPBXObxtDDaeW9on2O8LKj1my46BIToy8C7mI5KeYq6AK2fJMbrtQxpxzah-B0A7UlJtALVVH5reERvgZkkvyJa6NZvWblmhhr0o0yh1mTRWsckpAI8hMjkUMCip4xfGPcQw6XfgE39Ws5-tWRilhMJTRivQOuTq0Wg-UxYQPE8NvBhuv4PvbsGDZFXUOTAnB9Ap4uvIJO8HXICrRNkj5nXs0asZU8tfZPFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، رئیس‌جمهور ترکیه، رجب طیب اردوغان، را با کیم جونگ اون، رهبر کره شمالی، مقایسه کرد و گفت که نمی‌توان به ترکیه اعتماد کرد و نباید به آن هواپیماهای جنگنده F-35 تحویل داده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/132471" target="_blank">📅 13:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132470">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
کلاس های تابستانی دانشگاه ازاد مجازی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/132470" target="_blank">📅 13:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132469">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
نخست‌ وزیر بلژیک: ایران موضوع ناتو نیست اما درباره آن نیز گفت‌وگو می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/132469" target="_blank">📅 13:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132468">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
آژانس ایمنی هوانوردی اروپا: شرکت‌‌های هواپیمایی باید به دلیل تنش‌ها از حریم هوایی ایران، عراق و لبنان اجتناب کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132468" target="_blank">📅 13:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132467">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ: اگر ایرانی ها سلاح هسته ای داشتند استفاده می کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/132467" target="_blank">📅 13:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132466">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d24ddfc6.mp4?token=jJYMhngI-gu5jUYmha9yVxB-zgHy-SXOjQf9PuGTyPp_JasR7B75a8CzASouPi61rdmUMvyTZRz4XQaLjlq57mksZ5lDFoQr6yoNL_-sgb_IAxUzbaffkIvU6fWfRFKojEfgwlDMqYmBrZzmnR1NWTKLRgVfCS7pOSrtTZZtDfR_qllJaUlF91XdARPXMjAG6lER3g-eKI_6nTfs26mIhCuOoJerSAZxEFKwKMv_HMd59nA39Fwu6tZHd7jHEEjKEKEgfpeqb9SU2a1yGZoaDgdwKaduWA1M3SZOGJfVreaH1693Qm5-pUEs5UDrKCx-ufiKDHnB7rAvuiCAhyLVLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d24ddfc6.mp4?token=jJYMhngI-gu5jUYmha9yVxB-zgHy-SXOjQf9PuGTyPp_JasR7B75a8CzASouPi61rdmUMvyTZRz4XQaLjlq57mksZ5lDFoQr6yoNL_-sgb_IAxUzbaffkIvU6fWfRFKojEfgwlDMqYmBrZzmnR1NWTKLRgVfCS7pOSrtTZZtDfR_qllJaUlF91XdARPXMjAG6lER3g-eKI_6nTfs26mIhCuOoJerSAZxEFKwKMv_HMd59nA39Fwu6tZHd7jHEEjKEKEgfpeqb9SU2a1yGZoaDgdwKaduWA1M3SZOGJfVreaH1693Qm5-pUEs5UDrKCx-ufiKDHnB7rAvuiCAhyLVLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخبه دانشگاه شریف: تنگه هرمز عملا از دست ایران خارج شده و ایران دیگه کارتی نداره، اگه شروط ترامپ رو نپذیره کارش تمومه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132466" target="_blank">📅 13:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132465">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
والا نیوز عبری : ارتش اسرائیل جلسه‌ای با فرماندهی مرکزی آمریکا برگزار کرد، به منظور آمادگی برای از سرگیری جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/132465" target="_blank">📅 13:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132464">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
اتحادیه اروپا: درگیری‌های آمریکا و ایران مذاکرات پایان جنگ را پیچیده‌تر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132464" target="_blank">📅 13:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132463">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
اردوغان : با وجود کارشکنی‌ها از ترامپ بابت مدیریت قاطع بحران ایران و پیش بردن آن به سمت حل‌وفصل تشکر می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132463" target="_blank">📅 13:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132462">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزارت برق کویت: خطوط انتقال برق به دلیل ترکش‌های ناشی از پاسخ به حملات به این کشور از سرویس خارج شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/132462" target="_blank">📅 13:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132461">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
اردوغان : تو غزه و لبنان، همه ما مسئولیت داریم
🔴
همچنین باید با تروریسم، در هر شکل و هر جایی که باشه، قاطعانه مقابله کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/132461" target="_blank">📅 13:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132460">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
نتیجه نشست ترامپ با اعضا ناتو / ترکیه هم وارد شد !
🔴
اردوغان: ما برای یک عملیات احتمالی پاکسازی مین در تنگه هرمز آماده هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132460" target="_blank">📅 13:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132459">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
اردوغان در جریان نشست ناتو: «ما تلاشهای دیپلماتیک خود را دربارهٔ ایران و بازگشت کشتیرانی در تنگه هرمز ادامه می‌دهیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132459" target="_blank">📅 13:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132458">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPUkha_7aKdg2tsPlv2H_BZdXDrzzIcHjY1kPQ72Ovp6-E6OZOj8TizAFr8q0qaNu7bm6zavs5ndOPri98hNJQy7_v3uIMkqf_73VyTOtxnTv0k3V-_cR-3aXA5VInnqHL963Cqm9-9FO3kDfrLZ-xN9p_Uzv5WAFBlIbl83YZHhtlroifbGcurJRw-L0HK2y9-ebOkX6gQ62focpWDOMzmWVafK4duacIjKeAPevlJpVtXUT-tGj1wgJ6ox8THrV--BfEomJKEPMbK_3sZncaiFtahf1C0UEl8LWFeZrKtSfNJ9L-ThHUxMqpMlooP4zTGAwipUtm-Mc3WSSAkSLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت تتر در پی تنش های ۲۴ ساعت اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132458" target="_blank">📅 12:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132457">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef22ccab1.mp4?token=WwO19oreYj0T6g1yvBvjOpy0vdfV258gZhLkzM2qJhzNe84S9rRsfn6cJWqQEkZLHtf_TUKEvRp4vsrR9E4HLlPYzKrPVD5187j6M1s049zLyzpsxFnjDf75FpMJkI-gO-xhL44Ye5gG8DHDzaHp2vARfCFwZqQapsMRelJNs4wtx8o3q2Wz6eponRCtOVU5SYGmadrCie8R_ZaTEmYEHKC_UjiImQElPSZs38Tz9xnzVmkWN9_zWLBWJhWgdm9OvSexrwlq2S_41xWdaKea3iKMtdJQq90ZAMG7TdmUMfZV-SQ0Wn1wgyUojWnUKTo9u5rW3O8MAJ0ffcZefR2HcBo4cFTwfcUUBYggdgJilKLfsAF9mzhe74Xilf04URQ5XT1lOZv_RgE9TBdhqiJdeR05NmMxdxdYloVS0R9_zsBUQX_nkYqo0f1w3DAphz36Y0gqDHwG1Few2jh1pnhnJlvdbqHVP7NG9MK90kCOO08U0dhAOKUZHN17dTRy6Apvqn6uAvHMhPM8sIFLDgJXqiUFtAUBoXZmEgfqJiXcBOsh2N8-3ijoSndmLyrq7y48IXQ4uOSKU2vg_jQVFD99ltBS9QYoNtMxkSgvQQ-bCgkS7_Z3_GSk7oQl4QcbVgu5gKFByZkaLzhBnSMbrv-aEqAqtgX0mJWvXQBNKDKsNbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef22ccab1.mp4?token=WwO19oreYj0T6g1yvBvjOpy0vdfV258gZhLkzM2qJhzNe84S9rRsfn6cJWqQEkZLHtf_TUKEvRp4vsrR9E4HLlPYzKrPVD5187j6M1s049zLyzpsxFnjDf75FpMJkI-gO-xhL44Ye5gG8DHDzaHp2vARfCFwZqQapsMRelJNs4wtx8o3q2Wz6eponRCtOVU5SYGmadrCie8R_ZaTEmYEHKC_UjiImQElPSZs38Tz9xnzVmkWN9_zWLBWJhWgdm9OvSexrwlq2S_41xWdaKea3iKMtdJQq90ZAMG7TdmUMfZV-SQ0Wn1wgyUojWnUKTo9u5rW3O8MAJ0ffcZefR2HcBo4cFTwfcUUBYggdgJilKLfsAF9mzhe74Xilf04URQ5XT1lOZv_RgE9TBdhqiJdeR05NmMxdxdYloVS0R9_zsBUQX_nkYqo0f1w3DAphz36Y0gqDHwG1Few2jh1pnhnJlvdbqHVP7NG9MK90kCOO08U0dhAOKUZHN17dTRy6Apvqn6uAvHMhPM8sIFLDgJXqiUFtAUBoXZmEgfqJiXcBOsh2N8-3ijoSndmLyrq7y48IXQ4uOSKU2vg_jQVFD99ltBS9QYoNtMxkSgvQQ-bCgkS7_Z3_GSk7oQl4QcbVgu5gKFByZkaLzhBnSMbrv-aEqAqtgX0mJWvXQBNKDKsNbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سران ناتو در یک عکس خانوادگی در جریان اجلاس در آنکارا، ترکیه، حضور دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132457" target="_blank">📅 12:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132456">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZD12wwMtjnXcltZ6rP-ybbUyIyVNUIfi5oR6ag_LyI7_iko9bRUuowVr2EK9EaSbxcHQ_U4GBqGkkzLaWngXnr9oravf1uYuUJcIi9IXVl9XySBObHKyUUtkF_Z-OiuMzMvr-elVEmSDPHuEjb3s0kixVfSwdN1SRvCRwGXWkLqYsVQwuU3Ktm4LP8GRvF5ISiAyrpsFfbdbvACRasdsxulEB2YQjwJ_U7TsgDntFg1u0mx8jFg49jQ6o77shoe72S_zPcTHTBxx_xFQOJnc0C3BQ5Ontemvlnf2iEMZJt51JtxjNhwCQjbA4uJZIlEfz1RfTAmOuS2W60cIzcIpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:باید حملات رو شروع کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132456" target="_blank">📅 12:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132455">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb87e8e96.mp4?token=KrhHHgC8PGKhaSiAHzo5OuoqCCdkLxOhKL06YVG30D47GoH57j6we6K9yIQ4tSrc1XAlFb1VpucRqJt8semIlQATvPuqOY0V0DftQV-0L139hqPESErFxYVfL7G-SGK8QQOTjstY0Y-RlHuS5l4ArxeTdjt9B21aO02HliflTt0fl4eju8TAe1MI-UJFQZGc9oFTi-v-ZlWuaqvoT3PS1B-T256Vfi1Ccdqb-kUqwqxMbo-_5jsPlzH5NwWFZ5iSSrJLWqW8bvoCyokAIf24rf9rREiRPjOMw72eJv6KRUC-d2XQ0d8WrBk6pEOZSeodBaGdZcV1vWx1-wfRQaDO_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb87e8e96.mp4?token=KrhHHgC8PGKhaSiAHzo5OuoqCCdkLxOhKL06YVG30D47GoH57j6we6K9yIQ4tSrc1XAlFb1VpucRqJt8semIlQATvPuqOY0V0DftQV-0L139hqPESErFxYVfL7G-SGK8QQOTjstY0Y-RlHuS5l4ArxeTdjt9B21aO02HliflTt0fl4eju8TAe1MI-UJFQZGc9oFTi-v-ZlWuaqvoT3PS1B-T256Vfi1Ccdqb-kUqwqxMbo-_5jsPlzH5NwWFZ5iSSrJLWqW8bvoCyokAIf24rf9rREiRPjOMw72eJv6KRUC-d2XQ0d8WrBk6pEOZSeodBaGdZcV1vWx1-wfRQaDO_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: به نظر من، اردوغان هم از ایران خوشش نمی‌آید.
🔴
اردوغان شخصاً فردی عاقل است، در حالی که ایرانی‌ها (به طور کلی) رفتارهای عجیب و غریبی دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132455" target="_blank">📅 12:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132454">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
عمان: حملات ایران علیه نفتکش ها در تنگه هرمز را محکوم می کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132454" target="_blank">📅 12:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132453">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
العربیه: قیمت نفت حدوداً ۶ درصد افزایش یافت و به بالاترین سطح در دو هفته اخیر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/132453" target="_blank">📅 12:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132452">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ: "من از بیبی (نتانیاهو) خوشم می آید، او دیروز حرف های بدی درباره ترکیه گفت. اردوغان عالی است - او به دلیل من به جنگ نپیوست."
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132452" target="_blank">📅 12:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132451">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
کویت اعلام کرد که نیروهای مسلح این کشور، دو موشک بالستیک و ۱۳ پهپاد را در فضای هوایی کویت، بامداد امروز، مورد اصابت قرار داده و ساقط کرده‌اند.
🔴
وزارت دفاع کویت همچنین افزود که این عملیات هیچ‌گونه خسارت مادی یا جراحت انسانی به همراه نداشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/132451" target="_blank">📅 12:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132450">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
خبرگزاری آسوشیتدپرس امروز نوشت که رئیس جمهوری آمریکا، رهبران ناتو را که برای حضور در اجلاس ۲ روزه آنکار در ترکیه حضور دارند با انجام مجموعه‌ای از حملات علیه ایران و لغو مجوزی فروش نفت این کشور غافلگیر کرد.
🔴
در ادامه گزارشگزاری آمریکایی آمده است: این حملات متقابل پس از حمله به سه کشتی تجاری در تنگه هرمز رخ داد و شکنندگی توافق موقت برای پایان دادن به ماه‌ها جنگ بین دو تهران و واشنگتن را برجسته کرد.
🔴
ترامپ این حملات را اندکی پس از ترک ضیافت شام به میزبانی رجب طیب اردوغان رئیس جمهور ترکیه، انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132450" target="_blank">📅 12:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132449">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBx5Xy2bA4TnNNaCnctKqc0VvgDj4m3R7-9VPw4xCJHYmVqixHMe0BGxzpZwCNnhKQTSIJwT5Iq7pWIXXSaijH0A0kNWn3p9mu5fp35zPOODqlw9e3F8wbYr0GdkTZAGUac37bWx3iwbXBUZla8lKUQDC1KQSGCJqyeRhmZcn8Ozf9aeaYSaIeUtdBRorubLZCWPOqrEJD0OWpvRRbsCwmly9pPebgoNdnGzv6jUUQ2PClcE7ztgQSmJw5vKqVWCpAcHoMmZ8AcqMylGPAyvru60PS99xncNAMZuVy7l_lNV0MUl8FwJKn5ohO7JUx8-9SgFkzBIJq-SGX5gv835-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور سوریه، احمد الشعار، به آنکارا سفر کرده است تا در جلساتی که در حاشیه اجلاس ناتو برگزار می‌شود، شرکت کند.
🔴
قرار است او امروز با ترامپ دیدار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132449" target="_blank">📅 12:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132448">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fopi1yRYOBpD1m9Ny9-_l7W1yhJoHTikit735xGSL6tCuEbVwkT5ySpkE4p_jftELEvnix1kQTH1lcE01WDXwvtHP62yfuCYZ6SSU-qE6VvU2hVGMQ7byAqfxliF2ZeohTbeJBvLE0BQVy-laISVPrxvo2yGcNtd5QqJa3MZ6xFAwLbpmTZU2s9-vJI_Rq91XHBBQxTSXQq663COvLJkLq9ysd4V4w1Gaxcr0SnKbFETBrIixT675A6knIE0owBEYbcSpo2GGMHEAHEgRTTX5DteTa3vfiR0S0H9iLPoCETS2wVc2taxsd-xvupRMsAsjKE-4uvUcxoa4GXb_bZH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان : رفتار دولت آمریکا به عنوان میزبان جام جهانی، نشان‌دهنده سیاست خارجی همیشگی آن است: زیر پا گذاشتن قوانین، زورگویی با رقبای خود، ایجاد موانع و تقلب.
🔴
این همان روش "اول آمریکا" (MAGA) آن‌هاست. ایران از چنین بازی‌هایی امتناع می‌کند. ما به طور قاطع از حقوق خود دفاع خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/132448" target="_blank">📅 12:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132447">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ: ما دیشب به آن افراد بسیار خطرناکِ وابسته به ایران، با قدرتی بسیار زیاد حمله کردیم... یک مشکلی در آن‌ها هست.
🔴
ما می‌گوییم: "بروید مراسم عزاداری‌تان را برگزار کنید"، اما آن‌ها به‌جای این کار، دیروز شروع کردند به شلیک موشک به سمت کشتی‌ها. دیشب خیلی سخت به آن‌ها ضربه زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/132447" target="_blank">📅 12:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132446">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
دبیرکل ناتو: ۵ هزار هواپیما برای حمایت از عملیات نظامی علیه ایران از اروپا پرواز کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132446" target="_blank">📅 12:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132445">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری / جروزالم پست: وزیر جنگ آمریکا، به دنبال حملات علیه ایران، سفر خود به اسرائیل را لغو کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132445" target="_blank">📅 12:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132444">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ درباره ایران: «ایران سعی کرده من را بکشد، اما من تا حالا خوش‌شانس بوده‌ام... فعلاً.»
🔴
او ادامه داد: «من در تک‌تک فهرست‌های آن‌ها هستم. و تا اینجا، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی خیلی دوام نیاورد.
🔴
چون اوضاع همین‌طور پیش می‌رود، اما ما آدم‌های فوق‌العاده‌ای داریم.
🔴
اما این‌ها آدم‌های شرور و مریضی هستند، و ما باید سرطان‌شان را ریشه‌کن کنیم. سرطان را باید زود از بدن بیرون کشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132444" target="_blank">📅 12:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132443">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ : فکر می‌کنم مقام‌های ایران بی‌کفایت هستن
🔴
اگه کاربلد بودن، ۴۷ سال پیش توافق کرده بودن
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/132443" target="_blank">📅 12:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132442">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffb99aef2c.mp4?token=rKCR5haWzjyNeFQEM4Nja5-H9Ru-Iyhzgei0-vRXGK9YEX2bWkE4i9mAI57FwlJUfzTzPwIkKPiLISLqQxalS_4OwksWmQAoPUuVVHYkI8-kZvRk3Kuqjj9FokcknIjhyDyvJoDP5dB0vTk9qgXBncY3ZY8SvLagIy9A9W1h_gM-KRwxUndCBeiw3J76Fr6MdtrfNDGqMdQ6R9manpZqrV4nD5TBUQ-XoAQZGNUROLTFS2O12eF97duRIZnlVcHavqPMWn6SqX8DiIszzJOJyFRei7Vxb38Wr0W_cTEJH3qhWYxpC0Hja7nNTKX_Ops3Yz8tSQamjLZQ09as1KBwxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffb99aef2c.mp4?token=rKCR5haWzjyNeFQEM4Nja5-H9Ru-Iyhzgei0-vRXGK9YEX2bWkE4i9mAI57FwlJUfzTzPwIkKPiLISLqQxalS_4OwksWmQAoPUuVVHYkI8-kZvRk3Kuqjj9FokcknIjhyDyvJoDP5dB0vTk9qgXBncY3ZY8SvLagIy9A9W1h_gM-KRwxUndCBeiw3J76Fr6MdtrfNDGqMdQ6R9manpZqrV4nD5TBUQ-XoAQZGNUROLTFS2O12eF97duRIZnlVcHavqPMWn6SqX8DiIszzJOJyFRei7Vxb38Wr0W_cTEJH3qhWYxpC0Hja7nNTKX_Ops3Yz8tSQamjLZQ09as1KBwxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ آخرین آمار کشته های دی ماه رو 54 هزار نفر اعلام کرد!
ترامپ: رژیم جمهوری اسلامیه، درغگوعه، کلاهبرداره و آدم‌های مریضی هستن.
اونا توی اعتراضات دی ماه ۵۴ هزار نفر از مردم بی گناه رو کشتن‌.
مردم دست خالی بودن و اونا با مسلسل بهشون شلیک میکردن.
از نظر من مذاکرات و توافق با ایران تموم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/132442" target="_blank">📅 12:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132441">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ: رهبران ایران، بی شرف و رذل هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132441" target="_blank">📅 12:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132440">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما دیشب خیلی قدرتمندانه به ایران حمله کردیم.
🔴
آنها «تفاله» هستند.
🔴
ایرانی‌ها رهبران آمریکایی، از جمله خود من را هدف قرار دادند.
🔴
ایرانی‌ها دیوانه‌اند، ما از آنها خوشمان نمی‌آید.
🔴
فکر نمی‌کنم ایران بداند چه می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/132440" target="_blank">📅 12:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132439">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFAmDqYlhaWNvl8bjYsKc5MMXJcoBX4w1zM6fXM6Z_fmgnWhrLam2Ldk8ZGWjQRne5duWKTQ1ZPuyQs45vyqAe1DwGtpFo2B8dzm4WzezJxxrKci-5w7Ln80xeCpq41INB8t0ZJIxDTMxCof6lFUCHuBiLoLQ5GTgQBBiVLIYutQq0wSeZIh7HCBIus4xkiZ18gMi-_t_iGfjucfjKqWe1wgL31dRAiWuSqLGkhMZGOaqe5JAuVtdIoODnucqk7vXZzminMLdcDtzy5kcpL454Fb9AKz4Wznav-nxea65pdzJe2HbviMR_iTsHDiVQlrcgXyff0EGtFVk4bO6FVZLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بعد از حرف‌های ترامپ، قیمت نفت ۵ درصد افزایش پیدا کرد و به بشکه‌ای ۷۷.۴۰ دلار رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132439" target="_blank">📅 12:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132438">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ : شی جین‌پینگ هم وارد جنگ نشد و هیچ تجهیزات نظامی به اون‌ها نداد
🔴
کارش درست بود، من هم به رئیس‌جمهور شی احترام زیادی می‌ذارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/132438" target="_blank">📅 12:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132437">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d804ebbfd.mp4?token=okY4QWE19ug7cBImJPOp7tGMZEReeXzx4z-tZLU7XgMjjbg5d5LucbaQNfkc9UoXFA7j8QbpQyh9HrYc4-8DRkOu2kzfj2uhmKq_Y1zgg-SDkaK4BPlZLVaH6yo3IFl5eq2gCAcd-MmI3etd2CfJAaUHB0ZM0yUE_QZPll0LFYylRUDd2gEqtHrjLtotL7nMlAipcfc7g1ZN9pdlrAvbWyUHOgmTX-ETIicJQfZp6lW8x9bbWSHBiAUhR6_CVIW54aTawLMbqzxKvGfESZ65hSI-mfr9R2soQL_rnKmLBcM25f0fwU4KwMTMjwr-1Qux-0yDgEa1LHvWN5M8bWW1Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d804ebbfd.mp4?token=okY4QWE19ug7cBImJPOp7tGMZEReeXzx4z-tZLU7XgMjjbg5d5LucbaQNfkc9UoXFA7j8QbpQyh9HrYc4-8DRkOu2kzfj2uhmKq_Y1zgg-SDkaK4BPlZLVaH6yo3IFl5eq2gCAcd-MmI3etd2CfJAaUHB0ZM0yUE_QZPll0LFYylRUDd2gEqtHrjLtotL7nMlAipcfc7g1ZN9pdlrAvbWyUHOgmTX-ETIicJQfZp6lW8x9bbWSHBiAUhR6_CVIW54aTawLMbqzxKvGfESZ65hSI-mfr9R2soQL_rnKmLBcM25f0fwU4KwMTMjwr-1Qux-0yDgEa1LHvWN5M8bWW1Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ناتو: من از عملکرد ناتو راضی نیستم، به دلیل آنچه که در مورد گرینلند و ایران انجام دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132437" target="_blank">📅 11:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132436">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری / ترامپ: من فکر می‌کنم توافق‌نامه همکاری با ایران به پایان رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132436" target="_blank">📅 11:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132435">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ترامپ: من به مذاکره‌کنندگان عالی‌رتبه‌مان اجازه خواهم داد که در صورت تمایل به صحبت ادامه دهند، اما من این موضوع را بعید می‌دانم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/132435" target="_blank">📅 11:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132434">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ درباره رهبری ایران: آنها دروغگو هستند. ما یک توافق می‌ کنیم. همه موافق هستند. هیچ سلاح هسته‌ای. ما یک توافق می‌ کنیم.
🔴
آنها به بیرون می‌ روند، با رسانه‌ها صحبت می‌ کنند و می‌ گویند که ما اصلاً درباره این موضوع صحبت نکرده‌ایم.
🔴
مشکلی در وجودشان وجود دارد. آنها دیوانه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132434" target="_blank">📅 11:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132433">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ: هیچکس آن قاتل‌ها را دوست ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132433" target="_blank">📅 11:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132432">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ: مقامات جمهوری اسلامی آشغال هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/132432" target="_blank">📅 11:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132431">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فووووری/ترامپ: وقت تمام شد، آنها پست فطرت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/132431" target="_blank">📅 11:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132430">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ : برام مهم نیست می‌خوان مذاکره کنن، بکنن
🔴
ولی به نظرم فقط وقتشون رو تلف می‌کنن. اینا یه مشت دروغگو و حقه‌بازن
🔴
من تمام عمرم معامله کردم و موفق بودم. اما وقتی با اینا طرف می‌شی، می‌بینی از یه جنس دیگه‌ان؛
🔴
دروغ می‌گن، فریب می‌دن و آدم‌های خطرناکی هستن. به مردم خودشون هم آسیب زدن و تا الان ده‌ها هزار نفر از معترضان کشته شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/132430" target="_blank">📅 11:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132429">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ: ما نیازی به رابطه تجاری با اسپانیا نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/132429" target="_blank">📅 11:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132428">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ: ایران، بازیگران غیراخلاقی هستند، آنها "بی ارزش" هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/132428" target="_blank">📅 11:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132427">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ: ایران موشک‌هایی به سمت کشتی‌ها شلیک کرد، به همین دلیل آمریکا پاسخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/132427" target="_blank">📅 11:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132426">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترامپ: گرینلند یک مشکل بزرگ برای آمریکا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/132426" target="_blank">📅 11:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132425">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ: ما نیازی به رابطه تجاری با اسپانیا نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/132425" target="_blank">📅 11:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132424">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ در حضور دبیرکلّ ناتو اعلام کرد که دیشب حملات سنگینی را به مواضع ایرانی انجام داده‌ند
🔴
او گفت که ایرانیان را دوست ندارد و مقامات ایرانی را بی‌لیاقت توصیف کرد چون توافق نمی‌کنند!
🔴
ترامپ ساختار فعلی ایران را "سرطان شوم" توصیف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132424" target="_blank">📅 11:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132423">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ: ایران سران آمریکا از جمله من را مورد هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/132423" target="_blank">📅 11:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132422">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ: ما اجازه نخواهیم داد ایران به سلاح هسته‌ای دست یابد؛ آنها دیوانه هستند و هزاران نفر را کشته‌اند.
🔴
ما وقت زیادی را با ایران تلف کردیم و باید کار خودمان را انجام دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/132422" target="_blank">📅 11:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132421">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FF9YQZe8XCc1be-q1n3X_k_DTZ-tHBx0-pXBEBzzqFt25ROKl5ir8ipkRj9RFNJW7s6ma5KIvmsBORpAOhubyG8HmLwwOlwENRMBW76oM0d44hGm7nfvYNoZS7BGWA_sNfYYocvKS4ZGq0v4FS6pss1OdM_J9hUvRs7gVR5g1qzzWmsymrTaqkMJCAfqaJ5zAniiTQeCAg6JaQ0oWNdoaUx-zOCYDyLuDMV9WgJ2c7q8F2VkIPAqZ_srl59omyVa2fRXVWB5s_y3dyoVg7oa-8mUeIkJUonWVjMXPggAw1VYiDZNaHtYUPW9LnqzBAO-OR05xrIYPmejAYbnrRXlKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گفته‌های سازمان فرودگاه‌های هرمزگان به خبرگزاری ایرنا، در حملات شب گذشته، هیچ خسارتی به فرودگاه بندرعباس وارد نشد.
🔴
در حمله شب گذشته به این شهر، هیچ خسارتی به زیرساخت‌ها یا تجهیزات فرودگاه بین‌المللی شهدای پرواز ۶۵۵ بندرعباس وارد نشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/132421" target="_blank">📅 11:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132420">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
کویت: مجدد بر حق خود برای پاسخ به حملات ایران تأکید می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/132420" target="_blank">📅 11:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132419">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
خبرگزاری فرانسه: چین، آمریکا و ایران را به خاطر تشدید تنش‌ها و احیای دوباره جنگ مورد انتقاد قرار داد و خواستار گفت‌وگو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/132419" target="_blank">📅 11:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132418">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
قیمت نفت در پی تحولات جدید خاورمیانه و لغو مجوز فروش نفت ایران از سوی آمریکا، بیش از ۲.۵ درصد افزایش یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/132418" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132417">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkRzksq9yfkJFHbjXHooEdwKZa5fed9IxXoSf_9R20wm4fEFbkPbc2SZcUgxcYqA7CvYjbHhYOW9Y9T5xFSQYhzYykrms-dv-twniNggBaxn7twRakkKJRJTKt9QAfstcrAzr0IV0bu7H7SljS24KByiiBwHg_UDqcrYUFeNdwVCDlHdOZUIywMoDs6HW4N0Q0pIV_24X3z30XQo00FxHrNVEu7hr4N-8nefTxO-zHcwSnJbDZW45Uh0qdtrZvy795kKpdPU1Ld5oXV8pKiPaIKeqIos9iZ1SUhzCWOFdRtCwYrMSBjRKXsPkc0bUBbSrSeXLeHK7_OSiqDyS4Nx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتانیاهو به نیوز مکس: خطر ایران همچنان پابرجا است و تهران همچنان قادر به بازسازی برنامه هسته‌ای خود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132417" target="_blank">📅 11:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132416">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس:
نظم جدید و ایرانی را در تنگه هرمز به رسمیت بشناسید؛ تنها راه همین است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/132416" target="_blank">📅 11:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132415">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
اولیانوف: حضور کامل آژانس بین‌المللی انرژی اتمی در ایران در آینده نزدیک امکان‌پذیر نخواهد بود
🔴
میخائیل اولیانوف، نماینده دائم روسیه نزد سازمان‌های بین‌المللی در وین به ریانووستی گفت، در آینده نزدیک نباید انتظار حضور کامل بازرسان آژانس بین‌المللی انرژی اتمی در ایران را داشت.
🔴
وی افزود: ممکن است بازدیدهایی از برخی تأسیسات، مانند نیروگاه هسته‌ای بوشهر، که از حملات آمریکا و اسرائیل آسیب ندیده‌اند، انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/132415" target="_blank">📅 11:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132414">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از آژانس ایمنی هوانوردی اروپا: اپراتورهای هوایی نباید در حریم هوایی ایران پرواز کنند.
🔴
تعلیق پروازها از طریق حریم هوایی ایران و عراق تا پایان ماه اوت ادامه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/132414" target="_blank">📅 11:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132413">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usvw-RPX9fW9zphtEn402AFW0gzCRAAtl7W9jM6K5c0-Dvwe62Puk6wzPbsH7KuAz2kZCxN-eepax-EHx_AspJRTeDMTH-35KwH7oxP_cKEE6pF9LLW2uGMEJaF7mBEsOheOUjqAbPLLnsf5yRaKEOorVZrZMhCoOrzDriIH3iTmGLt-_1tWTB0P_GDKC196zRbAjB6nFsWa84MctpYOiKIRFtR5gdJuxCalKXcysm4tMegoq6fIdj0r3O1kxxFNC3WjZKgkMI8ggsJUuLS5FEVk-t3O5mgz9J4Kf5iGDAokaQmRtEObxkB3XPOIUubWy8nqPzjhfRuDYD7JHh9qGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گابریل ادواردز، فرمانده اسکادران هلیکوپتر نیروی دریایی آمریکا پس از ناپدید شدن در هنگام فرود اضطراری هلیکوپتر در دریای عرب، کشته شد.
🔴
با وجود گشت چهار روزه برای پیدا کردن جنازه او ، تلاش نیروی دریایی با شکست مواجه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/132413" target="_blank">📅 11:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132412">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d638495cb.mp4?token=NfNd2HBJi9lZIhTGZJ_eppjtKudVw7iEfDwlya942zvd-Rbl-X18KySPLm6tfyLp2j3JzY1FtQJSaEFgh3a_9ywElV5Gld7DpjhaAn8xDT6kvq7vHbQ7xae9m_luaCeqy5oXO1FP_2MCnZAYUn-eawwiLJ-6CES3j6yriBDHiAo2r6nY5WsGjKJbzc3l0E19ZZeKqVHXg64VIyVXVMkhj-8du4KlgUPNn7PFuRDgEgeY4Auoqrfl3ZmGsI3YkEKD24Pu-nUmF40ScHN4960HIfmUTX5b29hegWpGifIg1vUQBP62J6o-cz_kmF3mGry-SemhjjKHvpzhHmmsO0RlgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d638495cb.mp4?token=NfNd2HBJi9lZIhTGZJ_eppjtKudVw7iEfDwlya942zvd-Rbl-X18KySPLm6tfyLp2j3JzY1FtQJSaEFgh3a_9ywElV5Gld7DpjhaAn8xDT6kvq7vHbQ7xae9m_luaCeqy5oXO1FP_2MCnZAYUn-eawwiLJ-6CES3j6yriBDHiAo2r6nY5WsGjKJbzc3l0E19ZZeKqVHXg64VIyVXVMkhj-8du4KlgUPNn7PFuRDgEgeY4Auoqrfl3ZmGsI3YkEKD24Pu-nUmF40ScHN4960HIfmUTX5b29hegWpGifIg1vUQBP62J6o-cz_kmF3mGry-SemhjjKHvpzhHmmsO0RlgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مردم عراق میان دست میکشن رو سره عراقچی بعد میمالن به صورتشون
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/132412" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132411">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
معاون امنیتی استاندار بوشهر: امروز یک مقر نظامی در شهرستان دشتی و یک مقر نظامی در حوالی شهر چغادک از توابع بوشهر مورد اصابت پرتابه‌های دشمن قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/132411" target="_blank">📅 10:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132410">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
سی‌ان‌ان: پیت هگست برای اولین بار به عنوان وزیر جنگ به اسرائیل سفر کند
🔴
انتظار می‌رود این سفر امروز انجام شود و  هگست با بنیامین نتانیاهو و اسرائیل کاتز (وزیر جنگ اسراییل) دیدار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/132410" target="_blank">📅 10:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132409">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKU1JJB19gmZRuZHKV2uqvwzfd_U-yq6L6I4DWD5qqyrbVRVnyYQ2IOipzRZVae4dQPlJYBPB2C0kNw_BBylosqnx_zDq76iovmpOp9OL_KphYynGSunvY0VsAn0MjrIu0-zrwWgC0M5C99ImY3fi5sQ7bELXolXEqYEkJn_1k_kAbNJ2EgkR3LUszzFqY1LB9uBhjyjyLEOCLRN8NCOlVSWWX5EaPWk0AzobmS_Qz3StrvZT7bCCtsePS7kkS6x_eJXpg1LEUUr8eGmRJUv_881bphcWGLB1MOs35JTCPSAmp-43in_kdBO1qHNcrKE0Jn24sY01m0SMnKLD0HJQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه وزارت خارجه درباره حملات آمریکا و نقض يادداشت تفاهم خاتمه جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/132409" target="_blank">📅 10:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132408">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ارتش کویت مدعی شد ساعاتی پیش چند موشک بالستیک و پهپاد شلیک شده از سمت ایران را منهدم کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/132408" target="_blank">📅 10:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132407">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YryLjzPXffqrZpuiMgEvMT4qBSOI2eiW56aF-ZBVQx2qc5dTkeumVffbmURJ8xmyoWH_NezcBTkBPKx2FgIxFl3a4NSKJ7zjlIpBTJw2o8xPW9VdqhDUI49C18gOIhGNF1an6_u3UFV5NxhWL_xQX4AO26mj5zux_7tIyH10lVJHy-HhV-F4lxx2-yWLZsARFsBjm2ghBsXoMvP_LSQeedB9nFPdTi1RkFyuxIiLRf4lqdb0et-kNWZ8ZPpMnuroedr96i3nMkvniaT-few-_9iNZmKe7m_l6-C7r-ilJwKlWYfdvzDrmMpN9ymgfENs3LEbskwCWyywsuKS9Z0NMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسام الدین آشنا در واکنش حمله سوپر تندروها به عراقچی: همان که سنگش می‌ز‌نید؛ سنگتان را به سینه می‌زند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/132407" target="_blank">📅 10:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132406">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tl4DsQuiAG5LWOwJWQeblzi5bAUZ-YGnMHDoFojMVHittlpkXbOe5COMDj2sdMTfdbiZ72mdpG6PGGYwXvPgxMJdGiH3C0OySINtz4oTl0jvSO8msYAc0afTxF3XP71LK8ML_D5zOiU3T1Y7iS9YI-tc6MDNlpt9am58g7Ktt3m7vmEJt9canvlanlJnjWy8oFvdFbnZ8tbsjsrztKHh_CFIBNQVWr3NlDkAQK_r4pVdLuhnRfLgYm1vd31IN_g-UghEVjCX6VhptKyDpgTqxbSxge066JDRhVPQTV1f1lbeZYgFY9-SxwS2M134xtuObtUrBFtR9Foz0txPV7Etkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه ۱۱ اسرائیل
🔴
ایران: روزنامه «کیهان» که سردبیر آن از سوی دفتر رهبر معظم منصوب می‌شود، به‌طور علنی خواستار ترور دونالد ترامپ و بنیامین نتانیابو شد.
🔴
در این روزنامه همچنین آمده است که بیش از ۱۰۰ میلیون دلار از مردم جمع‌آوری شده و قرار است به‌عنوان جایزه به فردی که ترامپ را ترور کند، پرداخت شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/132406" target="_blank">📅 10:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132405">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4mJxzQ6CQbWYVYCaIgPnH5JvV6HFZaR-Sq08i3XnuZwwO6vzqWXhv5cnHB2QqFY-N7GU5eTyexvWo5nBpnVPyLTaVb7z07EChPN4sOZcyyqvrBpMDcWgbz51wDKVsdG4moA772Y7czaH9OwqbM4amwyWvgQZZfPwwrx8o8PP6gmJphrPR16dnHHO0YRbo_y1NVYGdDR59730VN0wZJ1ptwFMyb7IM7wa2RI0veRrSDCAoLXxb69pKwkFT-0UN4FtdKPANJTtb1RuOjTSXB-VHewEl-Cn1Dp7PBOFmTZQYrNBWrnViWXaAxCkoktMRXtPrdxtCmYl7je2I7KSqaHaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لارا روزن  :از منظر تهران، اهمیت راهبردی و بلندمدت تنگه هرمز بر هرگونه منفعت اقتصادی که ممکن است از توافق با آمریکا یا بهبود روابط با کشورهای خلیج فارس حاصل شود، برتری دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/132405" target="_blank">📅 09:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132404">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
آژیرهای هشدار در بحرین برای بار چهارم به صدا درآمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/132404" target="_blank">📅 09:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132403">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از یک مقام آمریکایی: ما مذاکرات خود با ایران را ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/132403" target="_blank">📅 09:47 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
