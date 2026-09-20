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
<img src="https://cdn4.telesco.pe/file/ZPSi90vRTDu91IdczzyjE9fw1FWiyCs2jDhaycyQK1U3sOidwlYF83dvDkwBfMmKM_SR7h-ydBliikj3CZvytwqdnHuT6u91Ogrlvt108zv0-jMkpPA6jyK-sNdHQ7LX7xroOg7r5dL7URCrmVKcvpSJzpa5jzzxYhmJidIqIVTRfe0huENWHehycAXVtemd9-G8RQHl4ff2C_uBEIjvqCqom8EJfMpuQ0MToUeyK1qQ2EW_H2KhGjkLAk_teovl5acPVX0d3nHEcRuNNbsG5CMunicQ1RkIWqQwCOlUxBRD7qYhJCOmAM79aiwTf7pUB7JMwcclVxps4Ht8wzEQrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 989K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 23:31:04</div>
<hr>

<div class="tg-post" id="msg-148456">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiLbyZPyR3d5PeiodLYtKDdnB43JMuP-RufgK2vg3fOEG2g8lSC_0wrkRkCjkCvSyOHl6gTA73UFGmCBUfLDJxBKDHP6Wt3Q5bqCCC4A1d4O2byp1UKsm8rJvYbx-jQmVnQFcIFYHHB08sEcOCth8S5nyoM8pPqdW6hfbklAJninRmq-4IOoAmYobqzyGvmkfFCh3m67OXsi-8rzIq5ivWj-U154BCadEX7LfFu2BpCgoERtLr9J5-U6sAnXcv5xTCHQ2xD2QHTpF_9tYjoBU9rjR_Z0b8Mn7TcCsV4uRE3pGi6EFbXleaaVY8h7HRLYrRrsOJsb0FZbaxAcG6MabQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلهکی:  تحرکات جدید برای مذاکره از سمتِ آمریکا، بخاطر وضعیتِ بُغرنجِ دولت ترامپ در انتخابات آتی این کشور است؛ «آمریکا اصرار دارد ایران باید تا ۴۵ روز آینده وارد مذاکره شده و همه موارد را توافق کرده و امضا کند»،
🔴
«مباحث هسته‌ای از روز اول مذاکره مورد بحث و بررسی قرار گرفته و روی آن توافق شود»، «تنگه از سوی ایران باز شود» و آمریکا نیز متعهد می‌شود مذاکره تا قبل از برگزاری انتخابات آمریکا به نتیجه برسد!
🔴
دستاوردی هم که آمریکا برای ایران در نظر گرفته، «رفعِ محاصره» و «آغاز نکردنِ جنگ جدید با خسارات زیر ساختیِ بالا»ست که هیچ تضمینی وجود ندارد که بعد از انتخاباتِ آمریکا، مجددا ایران مورد حمله گسترده آمریکا و متحدانش قرار نگیرد!
🔴
باید دید ایران از خطوطِ هسته‌ای _یا به بیان بهتر ۷ شرط برای توافق_ عقب می‌نشیند یا خیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/alonews/148456" target="_blank">📅 23:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148455">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
هم اکنون پرواز جنگنده های ارتش در آسمان تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/148455" target="_blank">📅 23:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148454">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVG0hXO2nRmY132Ee0msshNHf7GZWe9wZsbVify95-kBBPxtjRxzx0jNb8x_wNuMHx2vTV3xRnQEp1bN46a83GHb94IDqW_xQ0WhBkWR57Zanwse-A9Xo4M23E0qCqHB1hpB1xRL1_iNtFy16NEW3EpG4L8--T8imyIjG_I3jGXWfMAYWvnagsM3FQkca4qJLRfGz2OTk8oo10kxpqoXQatGnMLxVcg8qtJBhGCR2Dm83Gtj09YgwWn0A7ghrtaVxbXkf3L7sR-4JlP62q9ovh80JbscrwPf5FC6LVT-cYuHKmgmZ2DKK6WJhHS6uuxpqwZrL3GIJ9ZoFR-1Hrw1Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت مجازی آمریکا در ایران از تمام شهروندان آمریکایی حاضر در خاورمیانه خواست برای احتمال لغو پروازها و بسته‌شدن حریم‌های هوایی آمادگی داشته باشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/148454" target="_blank">📅 23:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148453">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
خبرنگار دولت: ادعای ترامپ برای دیدار با پزشکیان آرزوی محال است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/148453" target="_blank">📅 23:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148452">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
خبر لغو پروازهای ایران و عراق از روز سه‌شنبه تکذیب شد
🔴
به گزارش خبرنگار مهر، طی ساعات اخیر اخباری مبنی بر لغو تمام پروازهای هوایی میان فرودگاه‌های عراق و ایران از روز سه‌شنبه در فضای مجازی منتشر شده است.
🔴
در همین راستا، مجید اخوان، سخنگوی سازمان هواپیمایی کشوری، در گفتگو با خبرنگار مهر ضمن تکذیب این خبر اظهار کرد: تاکنون هیچ اعلام رسمی از سوی دولت عراق، وزارت حمل‌ونقل یا مراجع هوانوردی این کشور درباره توقف کامل پروازهای میان ایران و عراق منتشر نشده است.
🔴
وی تاکید کرد: ادعای لغو تمامی پروازهای میان عراق به ایران و بالعکس فاقد تأیید رسمی است و این خبر تکذیب می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/148452" target="_blank">📅 23:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148451">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
انور قرقاش، مشاور دیپلماتیک رئیس‌جمهور امارات: ارتباط با ایران ادامه خواهد داشت؛ به‌ویژه با مسعود پزشکیان، رئیس‌جمهور ایران
🔴
قرقاش تاکید کرد باز نگه داشتن کانال‌های ارتباطی با ایران می‌تواند به منطقه برای عبور از ماه‌ها درگیری کمک کند.
🔴
او دیدار اخیر ولیعهد ابوظبی با پزشکیان در حاشیه اجلاس بریکس در دهلی‌نو را نشانه اهمیت حضور «صداهای عقلانی» برای بازگرداندن صلح و ثبات دانست.
🔴
این مقام اماراتی در اجلاس رسانه‌ های عربی در دبی گفت: «تا زمانی که خصومت‌ها متوقف نشوند، نمی‌توان آینده را بنا کرد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/148451" target="_blank">📅 22:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148450">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jvwa9WCEU_BOIa3ohiCkDv30rxdFm2bKj52lLMviKnksIVXR3ZrMj6ijVePabXf7gdkIznVLI77Vbh8mrsR0uQETG_Oi4VDVFIOmXF13OdfYUEWNBS4L4DKfhOlDfv1_ZtxLw86XQADDxuySgeYgRu9_WLGiqxDQil08xL2IEdAX4uH86YliATFUhVX3LDw-u1q8rtwFOldRqxxuc_uyuqnQvTJK6Ssnf0a2qR33gvN7qNeBRB_-TmjhaJJeKmS36H6-9BcOWT3-u_sI5FFVaprupYv4Folr4s8WgK0FCZWm05pYsBCZ_mOKH1cSXZAw5jwiOAT9w0LrwhFxaH0Jhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمدعلی ابطحی: اجلاس سازمان ملل جای مذاکره و احقاق حق مردم مظلوم است
🔴
اجلاس سازمان ملل بزرگترین‌ اتفاق سالانه دیپلماسی جهان است.
🔴
از پارسال تا امسال به مردم ایران ستم شد و ملت ایران سرافراز و سربلند باقی ماند، آنجا فقط جای مذاکره و‌گفتگو و احقاق حق مردم مظلوم ایران است.
🔴
گفتگو و به دست آوردن‌ رفاه برای ملت تحت تحریم وحصار اقتصادی حقی است‌که مردم ایران طلب می کنند و‌ دیپلماسی جای حل آن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/148450" target="_blank">📅 22:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148449">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
این وسط وزیر کشاورزی به ازبکستان رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148449" target="_blank">📅 22:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148448">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOrTGeJH_ol1em4tVMX9Fxj1uU4jGRGdIJT6tz0YjsDcITz_rHqdkCe_acWbR95AQmFNsjWDm8-03VT3HVJNqKGWeoU5stPMIa3pkIhNJ1vKPv9139YykYKz6fEjjid_kI2G4XCEcbeKD6zbVHtqeCXY74sMmLIFmvuwXrtY_pVSbg6Jd6fkeuCYPsqX1aAPNEpxWeHS4RoYOLEcYMQ5pXKTD1Wu4t8ivfCXCa0C0Zb1jVMslrBE96pO6IX4uMWLMwhZlCfEJNmkMdbahN4nSpRQUDaXpHPTOibkU27uEhvoCKvV3GFVb8v-FJmAA7HCw7wCk8iCIrsgedMXiButjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی از دوحه راهی تهران شد تا یحتمل امشب راهی نیویورک بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/148448" target="_blank">📅 22:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148447">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
آذری جهرمی به پزشکیان:
سفر نیویورک را لغو کن و نرو!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/148447" target="_blank">📅 22:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148445">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bu2u3a90wF2ZrLUTGT_F99lQOoTAU8WuSFvGxPJ40HdaaUR_oLwyIhLjyK8FSQmDG6F6wT6XoR-lgX_VIdsC1GBRCI4XIlIWjzZtYEt09fvZbiTln-cCdPj6H3NmV_qHoEKe4Cop1SmUSYD4B9IRuyuaLrMea65o4D5_uBfywouT54r9EvswmnOtXgTX8LDJO8fbFbIT_nq-FSeiVc8VlEnuYF5YE7dNgzwDmLtuXWgutg7fGJCxKbdpP2l0uAV10E0giapWL0OHu7sldmI8tm7AWkubO58cNou5p6k15VC9SannGicdHco75vqJ69q3xyK5hySB1o2NKQIYDvkDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lettlCirh98-qiCx2GGEoWFGWpcn8BPquzAcel2U8Hw7LSTx0N3y-nzn1MQWOE0vzEdS6qSVcZ8SIlLTXs8vx3PUQzt6OF7QemCeHBnPKT7x3DzjsZbJZr3gGmn63HKxV-qyhvEtYZPbDPRmuzhB73k3eMaqSbScC_CwNsbYrDrLldkiITTAt2xN4ArKKiewg6COXZzq7dVYTv2b5lqoIWf1EcpgFBu2ZGL__Xdv4Osvqmp9QeDbl1DxLwbWj5zLQyHOZ1AR858O0zDyOtB8mTMBJ9kqofTw8wDD5LwCBJpBkK1CHBIIU5fiQPKXmqgrTgAJ7dmHm8DD02o20B1cLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای که امروز صبح گرفته شده‌اند، نشان می‌دهند که عربستان سعودی به طور همزمان هفت تانکر بزرگ نفت را در پایانه های رأس تنوره و جوایمه در خلیج فارس (معادل حدود ۱۴ میلیون بشکه نفت خام) در حال بارگیری بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/148445" target="_blank">📅 22:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148444">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ولودیمیر زلنسکی رئیس‌جمهور اوکراین:
من تازه با پرزیدنت ترامپ صحبت کردم. این یک گفتگوی مهم بود و توانستیم درباره بسیاری از موضوعات بحث کنیم.
🔴
ما توافق کردیم که در نیویورک دیدار کنیم و این دیدار می‌تواند تغییرات قابل توجهی را به همراه داشته باشد. یک پویایی دیپلماتیک در جریان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148444" target="_blank">📅 22:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148443">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
حوثی‌های یمن (انصارالله) اعلام کردند که جنگنده‌های سعودی در ۲۴ ساعت گذشته، ۲۸ حمله هوایی انجام داده‌اند. این حملات با استفاده از جنگنده‌های F-15 و تایفون از پایگاه‌های هوایی خمیس مشیت و طائف صورت گرفته است
🔴
این حملات مناطق طعز، الجوف و مأرب را هدف قرار داد و در مجموع، تعداد حملات هوایی سعودی‌ها در طول این درگیری به ۷۶۰ مورد رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148443" target="_blank">📅 21:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148442">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/148442" target="_blank">📅 21:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148441">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148441" target="_blank">📅 21:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148440">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88138fc09e.mp4?token=Sn4Wn2k8XgjcZHP6721eDMNlvepzBPY4Czr47S4-3Ahw6bnXQ0V97xwm_nMDEs-JGahIyFlH1KqrzgWVNHC0vFGt1WVBSix5km73saMhyYAZCqTFOclF2iPURuS3Tus4YlEXV_BirkQt43hGcYUF5Qqn_tlVfwGJG79vEBQwdsLESZQQm8UCf75quppcfbCLmYzTA_xjCsVrMvykFTVLmsR6Lc0_8k9cNjHftrfU4scZsqwyFPnnmvq7pyDzq_rURFWmY9L-Fnw9Zfs8aSjCeQ_JNzKwPJW_xneKA6a7qxQ_t8udPiPvX473owD-wLEbb-KtGtgpHRF1twOIXuSp4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88138fc09e.mp4?token=Sn4Wn2k8XgjcZHP6721eDMNlvepzBPY4Czr47S4-3Ahw6bnXQ0V97xwm_nMDEs-JGahIyFlH1KqrzgWVNHC0vFGt1WVBSix5km73saMhyYAZCqTFOclF2iPURuS3Tus4YlEXV_BirkQt43hGcYUF5Qqn_tlVfwGJG79vEBQwdsLESZQQm8UCf75quppcfbCLmYzTA_xjCsVrMvykFTVLmsR6Lc0_8k9cNjHftrfU4scZsqwyFPnnmvq7pyDzq_rURFWmY9L-Fnw9Zfs8aSjCeQ_JNzKwPJW_xneKA6a7qxQ_t8udPiPvX473owD-wLEbb-KtGtgpHRF1twOIXuSp4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بر باعث و بانیش تا قیام قیامت لعنت
#رقص_میله
#رقص_پرچم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/148440" target="_blank">📅 21:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148439">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سفارت آمریکا در ریاض: به دلیل وضعیت امنیتی جاری در عربستان، از تمامی شهروندان خود می‌خواهیم هوشیاری خود را حفظ کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148439" target="_blank">📅 21:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148438">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
فوری / عراقچی پس از توقف کوتاهی در قطر برای شرکت در نشست سازمان ملل عازم نیویورک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148438" target="_blank">📅 21:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148437">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0sfTN1-beRFKW5alDNSHeAW_0BnDGAEcwnO8FWOlRAMj84pdJu7Swqu7T_EPWIdo769wIVdYnaWY-kyWsSJ265LgAiQMHXVpo8aOlo_7nTtT2Qh6NDOCT_yuX-KDLXM9ofN-y72euZRxmAIzSnOCOWYZGe-1kr1QtLfLC21AB9r-6JUvlhZcUXuoZXYjWAV9Dl0SAeiuBAoMA66KNVSEBUoPtM5H8SzRuTFT-Xy6XB4jC0vMuJ-sxcqBk5tUIJi3tspQlRlVR4kqBqyFxnMpHSoFvbHZnQQJrE56aZysyB98daZDNibre4YSmH_iAJjpt7xvNjvKI3BnNmyPI-zAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه واشنگتن‌تایمز: دونالد ترامپ قرار است شخصا در فرودگاه پایگاه مشترک اندروز از شی جین‌پینگ، رئیس‌جمهور چین، استقبال کند.
🔴
طبق اعلام مقامات ارشد دولت آمریکا، هواپیمای شی جین‌پینگ روز چهارشنبه در این پایگاه فرود می‌آید و ترامپ برای خوش‌آمدگویی در آنجا حضور خواهد داشت. این کار غیرمعمول است، چون ترامپ معمولاً از رهبران خارجی در کاخ سفید استقبال می‌کند نه فرودگاه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148437" target="_blank">📅 21:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148436">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDxcomRzG7LbCL1URiVY1N_HaK2GKIa8X8zrd9qMGrpvAvgqGXt_9f16YS6SOw6Y8_AGqAhVPz33xmuFxoH8qdRYJyOfPDtTk9ovOyohKeadFyHDW44hJi7PIDPvKyHenjh1t67fooNVevJVMpeF0zmrJCocaxDxg9kaOj9nrptGzxiOEMzWYJ2F1zi9ybVnKp8V6QfTsHybfKmQRmuYyaw1FTJT-Nqoe9y_NWOHTMl2H4c64n4l1Vp0dFOUu5yrO0muw2oQRlyewuZZ-Bm-VrD44rDMVd6woYRJBjbuiBbUBw14QHQyX0TGR1s2n66tiQISB9pva7m53RYyx7O6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون با تاچ دیدار کرد
@AloSport</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148436" target="_blank">📅 21:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148435">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
افزایش شدید قیمت دلار و طلا تو تاریخ......
پیش بینی عجیب نوستراداموس ایران
😳
👇
https://t.me/+sN8qmnF1jDJlZGRk
https://t.me/+sN8qmnF1jDJlZGRk</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148435" target="_blank">📅 21:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148434">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
صابرین نیوز عربی : دولت عراق تصمیم گرفته است که تمامی پروازها به و از ایران و از تمامی فرودگاه‌های عراق را از روز سه‌شنبه آینده لغو و متوقف کند.
🔴
ترددها فقط از طریق مرزهای زمینی بین دو کشور امکان‌پذیر خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/148434" target="_blank">📅 21:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148433">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
امام جمعه قم: شرایط الان جنگیه و هرکی اعتراض کنه خائنه و باید کشته بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/148433" target="_blank">📅 21:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148432">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXpW5ul47SQwD8wNelC9sJJ7t5GLqS_bq5x_J_WJlYAoEQmkrDFAf0DDCTr4R1J4QmOs47irpsX_1qpL0JQWKvGGYwW6MIdBAE70fXTw7ZGlx6p97bc701IpN7qTSfms_K5Y6_lmrSP0uppbW9OnO0P4OPzQdFsqYKw8beCR_u6y66w1C707X1cnuyWJleNBzKwOi6tnucHfEDPJZnF-GetRARO4STBHkKR2WC3pfyLnE6qKFpmmCVjc38h_3pzZY1_8Qu-R4mPFYV_UhJb0il2R8m7L_UzNni1Kt-yQtIJ3Q6rahhpjMzcxjIYC42Fi5L3m4neQNwBLKHxXJiqQDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد باقر قالیباف، رئیس مجلس:
این وضعیت شبیه به شرودینگر است: امپراتوری در کابینهٔ سوه با ظروفی که در حال افتادن هستند، هژمونی را به تصویرk می‌کشد اما کاملاً عریان شده و سعی دارد ایران را خفه کند بدون اینکه عواقبی برایش پیش آید (که غیرممکن است).
🔴
این پایان‌بندی قابل مدل‌سازی نیست. آن گشوده خواهد شد و دست ایران از قبل روی اهرم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148432" target="_blank">📅 21:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148431">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
کارشناس صدا و سیما: ترامپ بارها اعتراف کرده که ایران پیروز شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/148431" target="_blank">📅 21:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148430">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
یمن: نیروهای سعودی از تمام مناطق ساحلی غربی یمن اخراج شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148430" target="_blank">📅 21:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148429">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUtU04Bla49D948zkOtd_rsQROgGOW3ryl4a5wPv0FcSWkWeOqn7SKbmEQdPOhpysunQ6ByI52Cn94Nu3mgQMXmqyNmTdYwsOJ8VhMPGwdEdE5xGAUCSvmBtGxgfEqwBSUC7-A0i0SCd7Z8gki2QiGCTmeuWcGmshymRbq2GY27MDGjTlvY_6E3QMWkdGd27Pk-G4pjx4bNwh_DdIpXHMcelo82z9zIeBw0GZZ5jVvmUU7bB_Am2aGfjcDz0pWXWHWnk_3sjXM7ekZorUMD00Zb0H1R20MzuVR3eIJ69KIQTaYAZcQivTtlR2Z2BbY35RxurGQpsX0xbQ24EIDkR6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تمرین چین برای حمله به جت‌ها و سامانه‌های پدافندی آمریکا و ژاپن
‏
🔴
وبگاه بردی افریک: چین نمونه‌های هدف گیری جنگنده‌های F-35 و F-16 آمریکا، سامانه‌های پدافند هوایی پاتریوت و هواپیمای هشدار و کنترل هوابرد E-767  ژاپن را در یک میدان تیر ساخته است.
‏
🔴
چین از سال ۲۰۲۱ تاکنون، نمونه‌های تمرینی تجهیزات نظامی آمریکا  و ژاپن را در بیابان‌های سین‌کیانگ برای تمرین تیراندازی واقعی و کالیبراسیون موشک‌ها می‌سازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148429" target="_blank">📅 20:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148428">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترامپ فردا در جریان بازدید خود از سازمان ملل، با ممدانی شهردار نیویورک ملاقات خواهد کرد‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148428" target="_blank">📅 20:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148427">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee7db5a25f.mp4?token=L9yegoO_IuA9DeT7hzUx2tPPCEzMyDcaOqEOWZPY_fXTSn89ZPKmjrhgTW90HXNV1d-oaLDOEf1gfazp3TGfd6Qw2QFOzZPP14U-jIY5J4-O0GPckDFjIl35PNytfMLLt7GTJ8hxFyNAqIXIU0k0YEcKsRicFWBKgVpGMqgf_rnUZ8d--33pwFqkvTCM7oLQ6U1cs9aRtTzWI6kVMdsHSnX5rKayuEcu2Cpi-JCjbfMstfuQ2DonKnW3LIP0b6pUc2tRenCZBj24406g7EkSJluZ_N1gtjV8LX-6jT-3hbIuLpSX1N7fzLM6EEx00GdsYL0cVwWGX4siFC3FplbrEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee7db5a25f.mp4?token=L9yegoO_IuA9DeT7hzUx2tPPCEzMyDcaOqEOWZPY_fXTSn89ZPKmjrhgTW90HXNV1d-oaLDOEf1gfazp3TGfd6Qw2QFOzZPP14U-jIY5J4-O0GPckDFjIl35PNytfMLLt7GTJ8hxFyNAqIXIU0k0YEcKsRicFWBKgVpGMqgf_rnUZ8d--33pwFqkvTCM7oLQ6U1cs9aRtTzWI6kVMdsHSnX5rKayuEcu2Cpi-JCjbfMstfuQ2DonKnW3LIP0b6pUc2tRenCZBj24406g7EkSJluZ_N1gtjV8LX-6jT-3hbIuLpSX1N7fzLM6EEx00GdsYL0cVwWGX4siFC3FplbrEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لیلاز، استاد دانشگاه: روزی که تفاهم‌نامه را دیدم گفتم چرا ترامپ باید چنین امتیازاتی را به ما بدهد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148427" target="_blank">📅 20:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148426">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28266dd36.mp4?token=mLdvF84LUczFq0sRqjqyd3PeAA-VBZiKsoGAY64PwMIDVi4vGMRFWVWpA9DGA9pWjRg9AGjWyhvLqIZ25dxWM_9jbSX93wEOKHNjsu_Hu5TGpXUZ2nfKImXOicX8TSwbjnqxxwNldRZBMBTANPajRPY0_iytC0mxpaitx7RwDglt56YD79MEkjYJLh4BLPsL9bpxfl-2H_HTEvUlzPqzsZ7hhC4RAEqVf2yxTm-8DcdgF4yFHV1bvZp4BL148FasqoiKkpkGebi-8e2eBW3ibX-JWtYhElsBuE5S2YTy_0bdyOSybi7PmI7X7MEY-tb8pX_HEEdyRYbdqARrN5v-bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28266dd36.mp4?token=mLdvF84LUczFq0sRqjqyd3PeAA-VBZiKsoGAY64PwMIDVi4vGMRFWVWpA9DGA9pWjRg9AGjWyhvLqIZ25dxWM_9jbSX93wEOKHNjsu_Hu5TGpXUZ2nfKImXOicX8TSwbjnqxxwNldRZBMBTANPajRPY0_iytC0mxpaitx7RwDglt56YD79MEkjYJLh4BLPsL9bpxfl-2H_HTEvUlzPqzsZ7hhC4RAEqVf2yxTm-8DcdgF4yFHV1bvZp4BL148FasqoiKkpkGebi-8e2eBW3ibX-JWtYhElsBuE5S2YTy_0bdyOSybi7PmI7X7MEY-tb8pX_HEEdyRYbdqARrN5v-bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لیلاز، استاد دانشگاه: شکی در اصل مذاکره وجود ندارد اما به هیچ وجه نباید از مواضع‌مان کوتاه بیاییم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/148426" target="_blank">📅 20:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148425">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
هفت هواپیمای سوخت‌رسان نیروی هوایی آمریکا در نزدیکی تنگه هرمز در حال پرواز هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148425" target="_blank">📅 20:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148424">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-2z2lfiIAZ248xmTvT0kX9NvBOeR3b53CHtpFNEUApVkB-UADc66afi2RTSwOYIyb6vA0IBN6f8UbrypvjtrQpaFB-yRU79oAScW-hTYAy5KrxoFE6EjRaY03fvMjUikCx8RZvxZM0G8ATPN5pdDD8kRos1xkGJU1wML9EWL5ymCfYAtwfEsxuYKbAJ9YE4TgAD6lDT4nKJ5SF8mYiHZGKKHLH3XpsYnokTh9YMqgAzgG6Aj5LlDy__7ij1ws8cwXIO78H3L_GURUibqj9srkc2iLve2Tc0pjK4YvT6P4tKo8MVUTnBXxPa5OZg2dGbGOhILHvmOkXVligEVAxNOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ دیس به خبرگزاری هایی که اجازه ورودشون‌به وایت هَوُس رو نداده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148424" target="_blank">📅 20:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148423">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ارتش : انهدام یک فروند پهپاد شناسایی پیشرفته اوربیتر بر فراز تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/148423" target="_blank">📅 20:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148422">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
آمریکا به‌دلیل شرایط امنیتی، تردد کارکنانش در عربستان را محدود کرد، سفر به «طائف» و «ینبع» نیازمند مجوز ویژه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/148422" target="_blank">📅 20:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148420">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNiu7rLeW8GdJzLv8xUoAy8tOACViNkJ28TrxvLtEnJXGYOXr7q5lw7GbREsEw45m_IM1T8jQYz5rTYf730XRTMGQlLFXLIMZTim0UMhmEAUm3GISpw85AEgPOG1Pcy5CtRzDsjE9_HffTD6OhrG27En5i4Hk-KjrGsrsSMBRsJg2dtCMh9D-5bLYttL_YYZktgmkOY94WNzFMsUxoP6vq3A1OK6I3LH0TeJlKsxuYAeR996EY99YvECafU_WrSxb2KESvtX35SCQGICCcoYjQQ7y9tzRzDh1xiHXGZqqZFpadAr7mop5WnQ6bb1vNAIo88uzFhUFqjw-LMp2n8lnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو حمله هوایی نیروی هوایی اسرائیل، مناطق مرتفع علی الطاهر در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/148420" target="_blank">📅 20:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148418">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری / راشا تودی: عباس عراقچی، وزیر امور خارجه ایران، وارد دوحه، پایتخت قطر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/148418" target="_blank">📅 20:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148417">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⛔️
بیایید ببینید هوش مصنوعیه یا نه
😂
⚠️
مشاهده فیلم</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/148417" target="_blank">📅 20:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148416">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
حمله پهپادی به اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/148416" target="_blank">📅 20:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148415">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHpeV6vnoo_8kP7_tnZuRRLP6L7jx5pL4U07axR1XlwlcPJBI12qfD7dlImrHIMtrV0yfoG8X11PT8Xr7a10AAqmb2LO8KCRMT58R2FZHuK9sVath7_Bsu9p5xeHV8zmleZCRvBYZnpQHxvybZc1gASbYLZWtpXaO6iQCoXxN-FPa2cOe81UAXMmPKEX_QjnV73xjBvPOigPFxwD1R63Gu5HHFX2oemKocE2W6BsJQpgNzjsz_HnfllNCsqz6bTSjFK7jiGS6riECwmReB8GCcgqVunlhTCFEzkchA2ml8NNiy5Xvdcc6cL-wPJiYRlfvYze2E6YYgvtPuy14XMWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هفت هواپیمای سوخت‌رسان نیروی هوایی آمریکا در نزدیکی تنگه هرمز در حال پرواز هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/148415" target="_blank">📅 20:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148414">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ: مایلم با پزشکیان در حاشیه اجلاس سازمان ملل دیدار کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/148414" target="_blank">📅 19:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148413">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda312692a.mp4?token=Q1Y1WeR5a5GgI73cxtMvD6V7IYWEd-s7tLvHWRIv9SfyPPDg2lQ7-ZfSFKPop4bi9K-6l1QfHHG8ul2NKKe7CDfgwkvRec2jS2CNiBtPT9_4zZIAidkO4ruE_P4eZ2ca0iw5c9zaI2-ZAU3fl8wa_OHdILWrWFqkwhn3AgsWTYfz1JPQc2YAJ-OiMhqrR87U5mVHNAHIUtfmogwrlHzGAH0HIor3bTzPcXJ174YwiMGXGa3il1X_vPtiyp5njVepY379hYI-opWzHAlj3mBqpldYqFm5vMq_qzwUc5jfkZe4MsAxyS3nDPJpz1xId6d9ZxBscdfhua-j1aTwJNNCYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda312692a.mp4?token=Q1Y1WeR5a5GgI73cxtMvD6V7IYWEd-s7tLvHWRIv9SfyPPDg2lQ7-ZfSFKPop4bi9K-6l1QfHHG8ul2NKKe7CDfgwkvRec2jS2CNiBtPT9_4zZIAidkO4ruE_P4eZ2ca0iw5c9zaI2-ZAU3fl8wa_OHdILWrWFqkwhn3AgsWTYfz1JPQc2YAJ-OiMhqrR87U5mVHNAHIUtfmogwrlHzGAH0HIor3bTzPcXJ174YwiMGXGa3il1X_vPtiyp5njVepY379hYI-opWzHAlj3mBqpldYqFm5vMq_qzwUc5jfkZe4MsAxyS3nDPJpz1xId6d9ZxBscdfhua-j1aTwJNNCYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسعود قدیریان بعد از قهرمانی در مسابقات جهانی بدنسازی گفت که مدال طلای خودم رو به رشت میبرم تا تقدیم مادر جاویدنام مسعود ذات پرور کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/148413" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148412">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
فرود اضطراری ایرباس در مسیر استانبول-تهران در تبریز
🔴
مدیر روابط عمومی فرودگاه بین‌المللی تبریز:   یک فروند ایرباس A330 «هما» که از استانبول عازم فرودگاه امام  بود، به‌دلیل نقص فنی اعلام وضعیت اضطراری کرد و در فرودگاه تبریز به‌سلامت فرود آمد.
🔴
تمامی مسافران در سلامت کامل هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/148412" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148411">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
اولین ربات تحلیل اقتصادی رایگان
‼️
🔴
اگه نمیدونی کجا سرمایه‌ گذاری کنی یه سر به اینجا بزن
👇
@Sygnl_bot
@Sygnl_bot</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/148411" target="_blank">📅 19:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148410">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
محسن رضایی: برای یک جنگ سرنوشت‌ساز کاملا آماده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/148410" target="_blank">📅 19:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148409">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
رسانه قطری : به نظر می‌رسد وزیر امور خارجه ایران عراقچی در حال سفری فوری به قطر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/148409" target="_blank">📅 19:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148408">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
خبرنگار سی‌ان‌ان‌: جلسه ترامپ در کمپ‌ دیوید، جهت بررسی و رایزنی درباره گزینه‌های حمله به یمن بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/148408" target="_blank">📅 19:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148407">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY9jbgftV7dNzvQ2xTWnYKOE41-uDdiVKIBGTt9fthONg1HKWrSUs65KekAvWDCtPRwySuKbKHQah_HTzS1kMy_Zf3NwNShCoq0RLBQYLghPxUOWZncqDBupxqQ7oofme9RUV7R8qCubtFRjhpiO9KVIRWeJsLHJj-4IIpFTitItUcDSmX6bu2Q8_oY113uOLFltStvXmMKlkOCQoclFeDZb11OUxGCM3IusrrfvHoCS_ghMJS-J7viP2-TAL94CcHXAStNUgnR0B32CELmxrwsuJyD4sbrFlGkZ3KRNy1NlwRByBw70iqP8YtCbFYC-KjoSA-bvMHel-y3Rf0ICvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار معاون نخست‌وزیر چین و وزیر خزانه‌داری آمریکا
🔴
اسکات بسنت، وزیر خزانه‌داری آمریکا، با «هه لی‌فنگ»، معاون نخست‌وزیر چین، در نیویورک دیدار کرد
🔴
این نشست در آستانه دیدار دونالد ترامپ و شی‌جین‌پینگ انجام شده است
🔴
بسنت، وزیر خزانه‌داری آمریکا در تشریح این نشست مدعی شده این مذاکرات به زمینه‌سازی برای پیشبرد منافع اقتصادی آمریکا و کسب نتایج ملموس برای مردم این کشور کمک می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/148407" target="_blank">📅 19:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148406">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8497b2ccea.mp4?token=cGepdfdg2a-y4XWDj_ShRlQmCiwI_cxcpmCGvOKp0vGVq0JzgCEpZOQHZJBTmDYfk5GpU55Hm9wTn79wAan2qWwspxShd1_OS1JRUwPlKybCFbChrOczwn_ZKe7qojqkkxVZxLTKO5OGGA8gqYKyXmj-TAonCBcWmxmUYxJbVELqWxjZIjPnyp5OkJ0mbhKvZWcBWxmZi_0u86KsbJ5NyQ4u-aXV9tr0vqqcLcdkLcxdfgJ6R0FIJoFXf8yCMjZxvUoQ1J59IMpEDHn5JUuGagGTwwgyzCgatpAQVxlsJfNju08BOWjWnA-0YyqMoCePZw5KQIDUSXLf5gv9DW0Gaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8497b2ccea.mp4?token=cGepdfdg2a-y4XWDj_ShRlQmCiwI_cxcpmCGvOKp0vGVq0JzgCEpZOQHZJBTmDYfk5GpU55Hm9wTn79wAan2qWwspxShd1_OS1JRUwPlKybCFbChrOczwn_ZKe7qojqkkxVZxLTKO5OGGA8gqYKyXmj-TAonCBcWmxmUYxJbVELqWxjZIjPnyp5OkJ0mbhKvZWcBWxmZi_0u86KsbJ5NyQ4u-aXV9tr0vqqcLcdkLcxdfgJ6R0FIJoFXf8yCMjZxvUoQ1J59IMpEDHn5JUuGagGTwwgyzCgatpAQVxlsJfNju08BOWjWnA-0YyqMoCePZw5KQIDUSXLf5gv9DW0Gaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از لحظه حمله به پالایشگاه مسکو که یک شهروند ایرانی آن را ثبت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148406" target="_blank">📅 19:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148404">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srHNP_U6Ayg-15IodhyhiWZPv29J72XBOGZ8ux798btyguoOTqwtzcseLov9obYD4WhBhjW7NIUQdfJAArraTkB8a0pVUBOrorMqd0wvV1i-PRsgyNd7chTbiU9qCpduW2w-VzUabbXj3FOVy9paJoTDhG7Kc0LUero7jFYzan_3WwMqLbmUUmJpghJ3O1izipTBubJZNSJWeYUfMlY9HiEEKBPzrMqLRccyb3NLqBeqk3Ua7obtFQGLchhbEsZK6kiPWCzzP-WQCjxiXwFiCd2uyvzkwBrOBZR-2n1jiIa6r-lcWhJRX9QYIJJPDffkpCqGXbhiChRVCGJUgMAZ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/آسمان اسرائیل کلیر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/148404" target="_blank">📅 19:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148403">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
تا ماه بعد وضعیت طلا چجوریه؟</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148403" target="_blank">📅 19:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148402">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر:
ما از مقامات دولت آمریکا تضمین‌هایی شنیده‌ایم که آمریکا می‌خواهد به توافق برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/148402" target="_blank">📅 18:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148401">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hR36Rx3T-ccYSZZfql-ECedcJrcWVZhRRRWdflOGsSmwFrAZVYL5EMZWN1ks3JO5x986aPMQ5Jt7R8PEfEdnG7gkOiJTilxaN9CCrAOMrhKTWatPUMV_VBmSdg1vzyLX7RZjdWd9FN75uAt6HJPLcNcCUf64rHxC9lbJJBWKFtjGLhEjw3G7ArnzUBb7E8llTu4RLbOtyRAZzUpdUfusXNoKjUzyJkkrVVfMMmolrcH2M7EfNY-C8ua1TdI-nNICh_57wLlInwZS10P5qYzJOdiGfYRHGulL8vT5vZtZs_-aXsQoX5sGoCesqDqkhO3JKRshZVaAaAgtF-yRQgPWGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که نیروهای آمریکایی، به عنوان بخشی از محاصره اعمال شده بر بنادر ایران، مسیر حرکت 109 کشتی تجاری را تغییر داده‌اند.
🔴
این تعداد شامل 4 کشتی بیشتر است که از آخرین به‌روزرسانی که روز جمعه منتشر شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/148401" target="_blank">📅 18:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148400">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ارتش اسرائیل:
نیروهای ما در تمام جبهه‌ها در آماده‌باش کامل، مستقر و آماده هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/148400" target="_blank">📅 18:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148399">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c78f54f4ca.mp4?token=gbOQsA7b-3dRJZzn9yQlPJN8XGoBMvKXrHpBOa03_-4UDuq73Ee7DgNZLx9vHzD8pBP_kef_apLhbFIGYZW1yheKPbiADIrq_leAsv4uyf1wN4fLUde-7zByOMhHy_DUfH3aocmqHZ-NSw_ZtnZw7T1BzL3IRa6eAvb1S_epWXXjJ79ctPfmvyPR6PGwUVLgpZeRJIBVRDg0AenN3sAPiy_h-BbUCsto4vOYZoR8WUKY5TblwMt5JlQs4WhKgNIfOiWAM9IT2nugTPINp1pGzFZp2_YADEuvoQYucfQOne5BdZZdfsfNucU3afRbz06A7sgcW5bE5ZBBfmPcfZ_s9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c78f54f4ca.mp4?token=gbOQsA7b-3dRJZzn9yQlPJN8XGoBMvKXrHpBOa03_-4UDuq73Ee7DgNZLx9vHzD8pBP_kef_apLhbFIGYZW1yheKPbiADIrq_leAsv4uyf1wN4fLUde-7zByOMhHy_DUfH3aocmqHZ-NSw_ZtnZw7T1BzL3IRa6eAvb1S_epWXXjJ79ctPfmvyPR6PGwUVLgpZeRJIBVRDg0AenN3sAPiy_h-BbUCsto4vOYZoR8WUKY5TblwMt5JlQs4WhKgNIfOiWAM9IT2nugTPINp1pGzFZp2_YADEuvoQYucfQOne5BdZZdfsfNucU3afRbz06A7sgcW5bE5ZBBfmPcfZ_s9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله پهپادی به اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/148399" target="_blank">📅 18:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148398">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وای‌نت: بیمارستان‌های سراسر اسرائیل به حالت اضطراری تبدیل شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/148398" target="_blank">📅 18:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148397">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_kciZ2hs6bsoVuQNFdoR_y633RHpPFHDkxW6-jxmcg6h-XehuGtIZNEaLzSsnPeFew3TwfNZWPKizDXfcHaMnobJwWmyWRt1dcOVARBMzfUpV01NiTKSYH5zDkMykPtBNMaruz2KycbF2vQGCQH0CqJBVhaxQCPwSLuwfOoWQRe1mMJBntESfQsShZhxdW9PqXFAVNvjC9Anj82bdReZL7syFJ5iCxNM8G4sPegICzF-3IO4ilQAdrXkW-egBH_QfDFc1VRX3CUw8hV_WLv9Vq2YpeOAH8NET3FwlOXhzWBuAOGUzaQQB-EwZRL9-YxoIvU0WNBPJrPW0Q7NyzaoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش قیمت صندوقهای طلا پس سخنان ترامپ مبنی بر دیدار با پزشکیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/148397" target="_blank">📅 17:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148396">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
رئیس سازمان سیا، اطلاعات مرکزی آمریکا به صورت ناگهانی وارد خاورمیانه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/148396" target="_blank">📅 17:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148395">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7129a2730c.mp4?token=JCZH1tA2GwKvvqzy46-xfzpFwczqUHFthzmHqy_SDvmd9yrEOJAICCrifjgjsRTxVuSCz6S8Yaz3wyekzaE2MubNz-CMW_sWontigDGIBXPCXLlULhNwc-uQH-Q5b_sTbbTagcMLQJtIBXNythhU6wrl2X0LNBrXr5fqaFjkTbapnGwFdKK62kfO1l-T5ZpWKx2WxEJ525YQwjlXVi13wTP5Qn8fpm5wNtFgaIgWL8yyvQcro_XMZuvvczhjl53uI-M0xIYWkxAtPDNftI3ki3sZDBaTzjo4dsGmylq-yZYxjwcu6Cyt9Lw1r-aOfJDRGKrk3iGPkCQPTZwLc9bSCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7129a2730c.mp4?token=JCZH1tA2GwKvvqzy46-xfzpFwczqUHFthzmHqy_SDvmd9yrEOJAICCrifjgjsRTxVuSCz6S8Yaz3wyekzaE2MubNz-CMW_sWontigDGIBXPCXLlULhNwc-uQH-Q5b_sTbbTagcMLQJtIBXNythhU6wrl2X0LNBrXr5fqaFjkTbapnGwFdKK62kfO1l-T5ZpWKx2WxEJ525YQwjlXVi13wTP5Qn8fpm5wNtFgaIgWL8yyvQcro_XMZuvvczhjl53uI-M0xIYWkxAtPDNftI3ki3sZDBaTzjo4dsGmylq-yZYxjwcu6Cyt9Lw1r-aOfJDRGKrk3iGPkCQPTZwLc9bSCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز:
برخی از مقامات ایرانی مانند موش‌ها پنهان شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/148395" target="_blank">📅 17:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148394">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7979df2c0d.mp4?token=LFZI5FbFyMnS1Ekz4mWbDYvBs4-_Bnh5G7xWk7PgIIPeqIgl3vIQ0L3J6c2OBFKP73_D1as562hyqatFdMEWuPIvR4YOc1X0KiZ0X88H0FfnZnuZ2WXv9dY6c4Nig7kk2futYrN8WD6tIl3M3feeX83Q1Dwn_s8MWbbxEFXWueI3Rr8tFGywW_352Tc89KoimAW__nfvX3J9yN8QioBVMEliIPRR83u4QSrKHYVT4aROdfxKyDF29C_ot5GnCHl-rXX3xVwNBvuqAlHtvcuE7sLMMzCvkR_KiXEGL-QAi_QZZjdi5M393oiZO3qKDLD9k2ICSuRP0gLSbRvMC95A3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7979df2c0d.mp4?token=LFZI5FbFyMnS1Ekz4mWbDYvBs4-_Bnh5G7xWk7PgIIPeqIgl3vIQ0L3J6c2OBFKP73_D1as562hyqatFdMEWuPIvR4YOc1X0KiZ0X88H0FfnZnuZ2WXv9dY6c4Nig7kk2futYrN8WD6tIl3M3feeX83Q1Dwn_s8MWbbxEFXWueI3Rr8tFGywW_352Tc89KoimAW__nfvX3J9yN8QioBVMEliIPRR83u4QSrKHYVT4aROdfxKyDF29C_ot5GnCHl-rXX3xVwNBvuqAlHtvcuE7sLMMzCvkR_KiXEGL-QAi_QZZjdi5M393oiZO3qKDLD9k2ICSuRP0gLSbRvMC95A3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز:آمریکا در ارتباط دائمی با حوثی‌هاست، و آن‌ها توافق کرده‌اند که با آمریکا نجنگند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/148394" target="_blank">📅 17:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148393">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: برخی از مقامات ایرانی پنهان شده‌اند و یافتن افرادی که قادر به انجام معامله باشند غیرممکن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/148393" target="_blank">📅 17:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148392">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: گزینه‌های فعلی روی میز، محو کردن ایران، رها کردن آن به پوسیدگی اقتصادی یا رسیدن به توافق است.‌‌
🔴
سوال من این است که کی و آیا قرار است تمام ایران را منفجر کنم و آنها بهتر رفتار کنند.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/148392" target="_blank">📅 17:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148391">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏
🔴
فوری/ترامپ:  ممکن است به‌زودی اتفاق بزرگی در مورد ایران رخ دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/148391" target="_blank">📅 17:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148390">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏
🔴
فوری/ترامپ:
ممکن است به‌زودی اتفاق بزرگی در مورد ایران رخ دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/148390" target="_blank">📅 17:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148389">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1502a1e1.mp4?token=oHsxIYa-a2E9iGSaOhddAQOUw-jhaNywkted5lmVuxGdlbIjwiDNUuHAcTUEaMy3CZxuY5k2CDw8UUd54-nR2cHgs0dEvz0Cd1S0M3Rb-J9KWxkvTC8-dYrfLAJXHQCulwNEJ9C4gLvKj-RbicEwcpw5-kBtvXDF3h57AVnOLnNJzCW2pRQCHjxMfT6d6qqnQw9yx8fFOfqw9mm1ReD0V8p_60yFMK7YmYIH90MGcybe8ziJzQ1OvAWas_PM34DQtr8TnktPt10WYqclehnJSX27v3FzisCE-_zUozHCGcltAVgXA4KhI9IwEqFXFTF4uzkXZTh6Y_mFHouzVrB-3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1502a1e1.mp4?token=oHsxIYa-a2E9iGSaOhddAQOUw-jhaNywkted5lmVuxGdlbIjwiDNUuHAcTUEaMy3CZxuY5k2CDw8UUd54-nR2cHgs0dEvz0Cd1S0M3Rb-J9KWxkvTC8-dYrfLAJXHQCulwNEJ9C4gLvKj-RbicEwcpw5-kBtvXDF3h57AVnOLnNJzCW2pRQCHjxMfT6d6qqnQw9yx8fFOfqw9mm1ReD0V8p_60yFMK7YmYIH90MGcybe8ziJzQ1OvAWas_PM34DQtr8TnktPt10WYqclehnJSX27v3FzisCE-_zUozHCGcltAVgXA4KhI9IwEqFXFTF4uzkXZTh6Y_mFHouzVrB-3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تداوم حملات عربستان به استان‌های یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/148389" target="_blank">📅 17:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148388">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
پزشکیان: صلحی که دشمن تو را به آن دعوت می‌کند، نباید دفع کرد
🔴
نمی‌توانیم قانونی بنویسیم که ضمانت اجرایی ندارد؛ گاهی به نام دین بر روی مسائلی متمرکز می‌شویم که اصل نیستند
🔴
ایجاد توقع در بین جامعه بدون در نظر گرفتن ردیف بودجه معین و پشتوانه مالی، نادرست است
🔴
از بیان حرف‌هایی که حتی فرع هم نیستند، دور شویم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/148388" target="_blank">📅 16:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148387">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
خدمت اجباری سربازی در آلمان مجددا از سر گرفته می‌شود
🔴
وزارت دفاع فدرال آلمان در برلین: نیروهای مسلح فراخواندن مردان ۱۸ ساله برای خدمت سربازی را که علاقه خود به خدمت را ابراز نکرده‌اند، آغاز کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/148387" target="_blank">📅 16:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148386">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t51QJlrCKsXNmUXnG2uW6jMTrPbHEFqhmWfZjVAAqcjfuHCCZ5vcdy4FyVrefVtCl4Zztz6QZWsnzkG6g6HcsTJg-A-L7f-6e1zN-oLdUQVn0aPYceMRMQMAj4FvQb6Ylb0UencDz6P0Kv5nm069Vs6Wb00S56dyQ7w4pktermER0_JAAUbTJokNJ6cBtYslXWb_IXSXVkmjJasgW24p7rNGsf5-feiQyi5pW7yCyNafEc6F8QuuofoXHf5G8RiBmUz3A30bW4Pg3gOwdap7RDmv9y4rHiHHZdhn0E9Svss2ReiXp7ZLgDIFZ94dzSGGx_Pg1VIhNb68zzl4egt7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تاکنون، بیشتر هواپیماهای تانکر سوخت از قطر تخلیه نشده‌اند و بعید است که ایالات متحده قبل از تخلیه این پایگاه، حمله‌ای را آغاز کند، زیرا تقریباً 20 درصد از هواپیماهای تانکر سوخت ایالات متحده در این پایگاه مستقر هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/148386" target="_blank">📅 16:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148385">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1d9cbe58.mp4?token=i7JUNN2brRQkO6wGJuf8xdxQQ9btRt8Pu2BTnjEPtSMhDAlKAnNKLhNtOvx2elxATVtpEhuzhxCFMQzQnQ4vwv6YItAffwzcecW_2DtBdGGWcgYDIdv0vkMQaX-in4VwebgyEGC-kbY2M9zcxY-x_cHyZYFnKwcgHqF9NhxA1DIpxOwiby86eJTOmxJ3PkvvMkiW7ebTITaqjpV8n80mjAGO3QLy53tjMO_rX5VkLf2YNsBBlwW2pd2IVrZFzsgnlu2JpCOkvTjOSDzmcEbWs2JxUe0JU7ANaB4R3P3xwT1uDgYjgG_JwaR5a80KGI-zho0zSU4gUHKNucX-n4A7tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1d9cbe58.mp4?token=i7JUNN2brRQkO6wGJuf8xdxQQ9btRt8Pu2BTnjEPtSMhDAlKAnNKLhNtOvx2elxATVtpEhuzhxCFMQzQnQ4vwv6YItAffwzcecW_2DtBdGGWcgYDIdv0vkMQaX-in4VwebgyEGC-kbY2M9zcxY-x_cHyZYFnKwcgHqF9NhxA1DIpxOwiby86eJTOmxJ3PkvvMkiW7ebTITaqjpV8n80mjAGO3QLy53tjMO_rX5VkLf2YNsBBlwW2pd2IVrZFzsgnlu2JpCOkvTjOSDzmcEbWs2JxUe0JU7ANaB4R3P3xwT1uDgYjgG_JwaR5a80KGI-zho0zSU4gUHKNucX-n4A7tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان به فالوور گفت تعقیب کننده
🔴
پزشکیان: حالا فالوور نگیم صداوسیما گیر نده بهمون
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148385" target="_blank">📅 16:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148384">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
فارس: یگان‌های واکنش سریع ارتش در مرزها مستقر شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/148384" target="_blank">📅 16:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148383">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد که بر اساس اطلاعات دریافتی، ایالات متحده تصمیم گرفته است اقدامات خود علیه ایران را از سر بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/148383" target="_blank">📅 16:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148382">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ارتش اسرائیل: نیروهای ما در تمام جبهه‌ها در آماده‌باش کامل، مستقر و آماده هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148382" target="_blank">📅 16:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148381">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر حملات توپخانه‌ای اسرائیل به مناطق یوهور الشقیف و خیام در جنوب لبنان منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/148381" target="_blank">📅 16:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148380">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
تا دو انتخابات تعیین کننده و مهم در آمریکا و اسرائیل به ترتیب ۴۴ و ۳۷ روز باقی مانده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148380" target="_blank">📅 16:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148379">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzxfyISyh5TI4kFzicyUftTmtLSXWGA6coW7v4EnL-l1y4LXkQkAonu5TD6V5hfeBbeyykL8uuSRsU5miTUNvQDCX6GBng8HiEMsVhFmdi6pB41Hru08rohyiprB4nxzW0nJzKZOmDmWS45tTrk5glQRlCFtG-sf6GEWAPfC_Qz76n98rJe1jQp2Btwzh4JZtbNMwPBK4Y8DP4GqX45q9aG2BsDKU0ALYcEsA4zOeA9emeoUvgpmQnLla16pYAkmDHE6EQ6_0PwYcQ6NPJW20NKIK3EtGl_L0ovXMckiODCiB8vUt59PYB4r1QWRg4HUatzW74yGIveSCD4fMbuh0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💱
بات سیگنال و تحلیل خودکار
💱
اگه دنبال تحلیل و سینگال دقیق هستید حتما عضو ربات بشید
🆓
آیدی ربات:
@Sygnl_bot</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148379" target="_blank">📅 16:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148378">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
اوکراین خطاب به پوتین: از پنجره کرملین سوختن مسکو را ببین
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148378" target="_blank">📅 16:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148377">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ژاپن: کره شمالی دومین موشک خود را شلیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148377" target="_blank">📅 16:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148376">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
فارین پالیسی: ترامپ و پوتین در جنگ، شباهت‌های زیادی به یکدیگر دارند
🔴
در تحلیلی در فارین پالیسی آمده است که هم دونالد ترامپ و هم ولادیمیر پوتین تصور می‌کردند جنگ‌هایشان با مقاومت جدی روبه‌رو نخواهد شد و در مدت کوتاهی به پایان می‌رسد.
🔴
نویسنده این مطلب معتقد است هر دو رهبر تا حدی تحت تأثیر روایت‌ها و تبلیغات خود قرار گرفتند و برای یک درگیری طولانی‌مدت آمادگی کافی نداشتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148376" target="_blank">📅 16:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148375">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
محسن رضایی:  اگر آمریکایی‌ها جدی هستند، بگذارند سربازانشان بیایند و وارد ایران شوند، چرا نمی‌آیند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/148375" target="_blank">📅 16:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148374">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
مرکز زبان وابسته به سفارت فرانسه در تهران با دستور قضایی پلمب شد.
🔴
قوه قضاییه اعلام کرد این مرکز بدون مجوزهای لازم فعالیت می‌کرد و پیش‌تر چند بار درباره ضرورت دریافت مجوز به مسئولان آن اخطار داده شده بود.
🔴
در گزارش قوه قضاییه، اتهاماتی مانند استفاده از آموزش زبان برای پروژه‌های علیه امنیت ملی و تسهیل خروج نخبگان از کشور نیز مطرح شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148374" target="_blank">📅 16:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148373">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
پزشکیان: باید راهی پیدا کنیم که مردم ما به عزت و سربلندی و قدرت برسند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/148373" target="_blank">📅 15:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148372">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
نتانیاهو برنامه سفر خود به آمریکا در روز های آینده را تغییر داده و بلافاصله پس از سخنرانی در مجمع عمومی سازمان ملل بدون دیدار با ترامپ به اسرائیل بازمی‌گردد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/148372" target="_blank">📅 15:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148371">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ra-M0eoynHmxgSCqVAfR3ZDtvK73FWawA3z0mSgs2W_vXGuhoZG8gjCqFcfBpiwrCW9DRft5Ihc9CzoQhFq1MeJfJIe83MF6US8ywaEpUe7KqqxfpSj5J0XiVvm0vmVuY-6jueOF_gb8kQJxQLi-7fSL92KGU59iCldcHFzsA6sGahnEpEPZuUctJumyBaAHCURcjF3F9t_cE7rKe0HPUYxT8cNJid3AmBzbynXOX1YKY7-4CC_TqczhoJOeyJn12kg23TbnOOLEVidl1WTL5wwWo4mFEqtoBozmQxPc1uR2YXrCT1aEaIxPlUDinKlJdUvegdRz4a86VavHdr2vsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : به درخواست قوی ارتش ایالات متحده و به منظور حفظ امنیت ملی، من موافقت کرده‌ام که بنای باشکوه "طاق پیروزی" را که از دوران جنگ داخلی، یعنی سال‌ها پیش، برنامه‌ریزی شده بود و در محوطه "دایره پذیرایی" مجاور پل یادبود آرلینگتون قرار دارد، به یک مجموعه نظامی/طاق پیروزی درجه یک تبدیل کنم. این مجموعه برای نگهداری، ذخیره‌سازی و استفاده سریع از تعداد زیادی پهپاد، به همراه تک‌تیراندازها، در مناطق سقف و محوطه، و همچنین ذخیره‌سازی مقادیر زیادی مهمات تک‌تیراندازی، طراحی خواهد شد.
🔴
هیچ سازمانی مانند این در هیچ جای دنیا وجود نخواهد داشت. از بین 59 شهر و پایتخت برتر جهان، واشنگتن دی‌سی، تنها شهری است که طاق پیروزی ندارد، اما اکنون این مشکل برطرف خواهد شد و این طاق، بزرگترین طاق پیروزی در جهان خواهد بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/148371" target="_blank">📅 15:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148370">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
صداوسیما: حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148370" target="_blank">📅 15:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148369">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
فیلد مارشال رضایی: آمریکا و ترامپ خواهند رفت. همه می‌دانند که اقتصاد آمریکا در واقع در مسیر فروپاشی قرار دارد. در طول 10 سال آینده، آمریکا آن‌طور که امروز است، نخواهد بود.
🔴
اما ما و کشورهای عربی باقی خواهیم ماند. ما هستیم که باید این منطقه را سامان دهیم. ما باید امنیت را در خلیج فارس برقرار کنیم. ما باید یک پیمان برای همکاری اقتصادی ایجاد کنیم و در این منطقه با یکدیگر دوست باشیم.
🔴
ما یک خانواده هستیم – خانواده خلیج فارس. ما هشت کشور هستیم و باید بر بازسازی و توسعه اقتصادی تمرکز کنیم، با یکدیگر همکاری کنیم، در سرمایه‌گذاری‌های یکدیگر مشارکت کنیم و حتی یک ارز واحد و یک بازار مشترک داشته باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/148369" target="_blank">📅 15:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148368">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی، دبیر شورای عالی امنیت ملی : اکنون به تمام کشورهای عربی و تمام کشورهای همسایه می‌گویم: اگر آمریکایی‌ها تلاش کنند روابط تجاری و مالی ما را مختل کنند، ما دو کار انجام خواهیم داد.
🔴
اول اینکه، حتماً به شرکت‌های آمریکایی حمله خواهیم کرد – مانند شرکت‌های حفاری آمریکایی که به طور گسترده در اطراف ما فعالیت می‌کنند، شرکت‌های تجاری آمریکایی و کسب‌وکارهای آمریکایی.
🔴
ما آن‌ها را هدف قرار خواهیم داد و خواهیم گفت: حمله به اقتصاد آمریکا در پاسخ به حمله آمریکا به اقتصاد ایران – حمله به ازای حمله.
🔴
از طرف دیگر، ما همچنین به کشورهای همسایه هشدار می‌دهیم: با آمریکا همکاری نکنید، زیرا ما به طور متقابل پاسخ خواهیم داد. اگر یک کشور همسایه با آمریکایی‌ها در تحمیل یک محاصره اقتصادی به ایران همکاری کند – به عنوان مثال، در مسائل مالی و فعالیت‌های مرتبط با ما – ما به کشتی‌های آن کشور در تنگه هرمز تذکر خواهیم داد.
🔴
ما محدودیت‌هایی را بر تردد و عبور آن‌ها و همچنین برخی از فعالیت‌هایشان اعمال خواهیم کرد، یا ما به طور متقابل در مورد همکاری‌های اقتصادی پاسخ خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/148368" target="_blank">📅 15:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148367">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
پزشکیان: ما باید طوری کار کنیم که چرخ تولید بچرخد و از کار نیفتد
🔴
هر جایی را که می توانیم قطع کنیم ولی نگذاریم چرخ تولید قطع شود
🔴
دشمن به دنبال این است که تولید ما از کار بیفتد؛ نبود تولید یعنی بیکاری و تورم و کمبود و گرفتاری
🔴
همه کمک کنند که تولید کنیم. باید این فرهنگ در جامعه جا بیفتد که ما خودمان در سرما بمانیم ولی چرخ تولید متوقف نشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/148367" target="_blank">📅 15:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148366">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
صداوسیما: حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/148366" target="_blank">📅 15:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148365">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
پیشنهاد ایران به آمریکا به نقل از ارم‌نیوز امارات:
🔴
توقف غنی‌سازی بالای ۵ درصد
🔴
آزادسازی بخشی از دارایی‌های بلوکه‌شده
🔴
بازگشایی کامل تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/148365" target="_blank">📅 15:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148364">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5da053393a.mp4?token=Zw76CfOc06gH3QVnF0p2dHnW5yu51_NC8ujoWA8yMYaCWbN-Dx3Xpz1ONWGx80g7GPWDfdz6-NcCQqCOHhrxE0VY-fkKwkziVOx7hqQ6a2dHbrjDwXp2kB1Uaq0pdlAs-fo-QaMhvyaKrx1TKQeK-OqxC2ER1lIrQN3wInIVxBjTtsQsoM4TfPBw0TdzDkWrX4yOirRl-p9stL9xGAYAgtTDgjoeBAdoc7Qb6YA5xHZCCST6414ZAt6xOZVxXcgyET18Jr1eZfLtHNLOYlY44uRa8wTyXJdldiRBv5gssGwilzzz_cp3AKGyjafrUzvL3zV9E_CAKN2sx9YygWUx4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5da053393a.mp4?token=Zw76CfOc06gH3QVnF0p2dHnW5yu51_NC8ujoWA8yMYaCWbN-Dx3Xpz1ONWGx80g7GPWDfdz6-NcCQqCOHhrxE0VY-fkKwkziVOx7hqQ6a2dHbrjDwXp2kB1Uaq0pdlAs-fo-QaMhvyaKrx1TKQeK-OqxC2ER1lIrQN3wInIVxBjTtsQsoM4TfPBw0TdzDkWrX4yOirRl-p9stL9xGAYAgtTDgjoeBAdoc7Qb6YA5xHZCCST6414ZAt6xOZVxXcgyET18Jr1eZfLtHNLOYlY44uRa8wTyXJdldiRBv5gssGwilzzz_cp3AKGyjafrUzvL3zV9E_CAKN2sx9YygWUx4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/148364" target="_blank">📅 15:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148363">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
تسنیم: در روزهای آینده پزشکیان قراره توی مجمع عمومی سازمان ملل در نیویورک حضور پیدا کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148363" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148362">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
رئیس سازمان سیا، اطلاعات مرکزی آمریکا به صورت ناگهانی وارد خاورمیانه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/148362" target="_blank">📅 14:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148361">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
فایننشال تایمز: عربستان از برنامه تحت رهبری چین که بخشی از تلاش‌های پکن برای ایجاد یک نظام پرداخت فرامرزی جایگزین دلار است، خارج شد
🔴
ادعای یک منبع آگاه: خروج ریاض از این برنامه به علت فشار واشنگتن، نادرست است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/148361" target="_blank">📅 14:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148360">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d8158ff0.mp4?token=NCHn4EognVp9EKq1h6_Tg-9tVWJtvHpbHJhb9oc6MAkMKULZ8QWacyslY2uyoz2N3p3BY-Z8xQtt2_dNx7glal4QLxhFUi0GbA0EMGMUgerbHQ3HDh3Xvusvu47mk5KK4OG6WVnuUY3z8MqnuJI8XZBc9ZBIDWe0OaTm4BgCIuPH03ThdU5GUaDnTUupIZw7DBw1UP0POR8PFst4UVr9l8UiVg7Qv72182-dQb01WbiTeYuolSNVIcXrd7kaczdXAjR_0GIXTnQCqenM_99-dNXyrrWkdgnTatdLB9-DgOC9RWDZpPVgFNSC8HDnUDSvch8s9LwfFf4RtDqqrOHfRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d8158ff0.mp4?token=NCHn4EognVp9EKq1h6_Tg-9tVWJtvHpbHJhb9oc6MAkMKULZ8QWacyslY2uyoz2N3p3BY-Z8xQtt2_dNx7glal4QLxhFUi0GbA0EMGMUgerbHQ3HDh3Xvusvu47mk5KK4OG6WVnuUY3z8MqnuJI8XZBc9ZBIDWe0OaTm4BgCIuPH03ThdU5GUaDnTUupIZw7DBw1UP0POR8PFst4UVr9l8UiVg7Qv72182-dQb01WbiTeYuolSNVIcXrd7kaczdXAjR_0GIXTnQCqenM_99-dNXyrrWkdgnTatdLB9-DgOC9RWDZpPVgFNSC8HDnUDSvch8s9LwfFf4RtDqqrOHfRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چین ۹ ماهواره به فضا پرتاب کرد
🔴
طبق گزارش رسانه‌های دولتی چین، این کشور ۹ ماهواره را با موفقیت با استفاده از موشک حامل «لیجیان-۱» به فضا پرتاب کرد.
🔴
به گزارش خبرگزاری دولتی شینهوا، این ماهواره‌ها عمدتاً برای پایش محیط فضایی، پیشگیری و کاهش خسارات ناشی از بلایای طبیعی و انجام آزمایش‌های علمی مورد استفاده قرار خواهند گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/148360" target="_blank">📅 14:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148359">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2wUYvqh4GJWqmAUuSn40q796Zfqwrw4iGeFTdhkmuOP8BwD1comEnldM7ygFD28L-S7SvExRoOBM9YWK8dU0no0w4IWpFl2jqn8epZp9H_jfUxS2wDAytJwx7pXGypvcr2sDyi4H4eexej5ldci5ot1Q9lnwPt_2pfmaTJuJf0XVQUaZq3rGvGuRX-nWM1u-T5gX_iwKiRXttPjlcV27sztE_ohLPiJXHAjlMNZha8XRTx2eTYg1B8aZmdAAFxpcL46Y4r_Uur_n5aEUqAASTwoDhPPzefdwzWaaahkKyVSClsqQifuBtGoPhQiJagCM8TvpO_0I8Ea6_vcfu_Rdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فکر کنم اگه روسیه بمب اتم داشت، اوکراین جرات نمی‌کرد اینطوری به پالایشگاه‌هاش حمله کنه...!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148359" target="_blank">📅 14:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148358">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سفارت آمریکا در امارات: با توجه به تنش‌ها در خاورمیانه، وضعیت امنیتی همچنان پیچیده است و احتمال تشدید غیرمنتظره تنش‌ها وجود دارد.
🔴
شهروندان آمریکایی که در حال حاضر در خاورمیانه حضور دارند، باید هوشیاری بیشتری به خرج دهند و نسبت به احتمال لغو پروازها، بسته‌شدن حریم‌های هوایی و اختلال در سفرها آگاه باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148358" target="_blank">📅 14:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148357">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سپاه : به ایالات متحده هشدار می‌دهیم که اگر هرگونه اشتباهی علیه ایران مرتکب شود، تمام مراکز و منافع آن در منطقه مورد حملات مداوم، موثر و دردناک قرار خواهد گرفت.
🔴
همچنین هشدار می‌دهیم که اگر کشورهای منطقه با ادامه سیاست‌های دوگانه خود در تهاجم به ایران، با این اقدام همسو شوند، ما آن‌ها را شریک در این عمل خصمانه تلقی خواهیم کرد و دیگر نمی‌توانند انتظار خویشتن‌داری یا مدارا از نیروهای ما را داشته باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/148357" target="_blank">📅 14:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148356">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
حدادعادل: بنیاد زبان و ادبیات ترکی در تبریز تأسیس می‌شود؛ تقویت و حمایت از زبان و ادبیات ترکی ضروری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/148356" target="_blank">📅 14:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148355">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
دولت کویت مدارس ایرانی فعال در این کشور را تعطیل کرد
🔴
رئیس مرکز امور بین‌الملل و مدارس خارج از کشور وزارت آموزش و پرورش:
دولت کویت در اقدامی غیرقانونی، مدارس ایرانی فعال در این کشور را تعطیل کرده و مانع ادامه فعالیت‌های آموزشی این مدارس شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/148355" target="_blank">📅 13:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148354">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
رویترز: سهام عربستان سعودی و کشورهای حوزه خلیج فارس در آغاز معاملات پس از حملات اخیر به ریاض، پایتخت عربستان سعودی، کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/148354" target="_blank">📅 13:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148353">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a87d1892.mp4?token=IRs0Bw87CfnB02JzAJya1J76nRi-TciCZmwWsyTr3yhWsbRoWgUN1Ko9MUUR6uKqRO3PVMZzPgyYEP80KgMlNtRjNJBVat3BBi6kkvcL1bOfASCso3koJFT3IkP1-FBjBIa4qTzzmdSjXWvOWzJeVttfVVVvqFCV6Ix2qWdZkTXFZJN86581naCzTeGrpeLUcubX3VPGG8S6l5QoSngxjrOa9bbFlXW7bsD7WucDigDFhWBBvG5a0_-X1JrPP6Gq-PknWsqoPCm5heu0XL9F-esHBIUcWgW2YfOw5YoWH_7ntdpEKiGMGxRxLK0uY4yYbAIvkcGrtyp-fE_pUX0_0lZghb6d0QAWIXx1B-SUWNaDrUUXtWGt5-Yv_HJ3MylzItHQfpl-NV1JHUIVj2nKU8-yxD0CV76cX1R7Vrm0m7y6FLWxIK9cW7CAJRk-S9DOxHrnijRXiSLRl2x9yvRVMGMDruZVqD2eHp6knsGIBHAf5LmN0i6yiYtjf0DkCn19TCmzotiBg0ZgIdSsUn-U9vFETBTxemhN-7WdUVnDZlY1i3ZTzsFSV9LGemqpETQnMjpnVS2KegI6fHQtUXHBXxMA-tl8_hdYdrKp5xolu7Ud6TmD_KgM6vYxKtA4_rRE5-SW2PL1GAfIRK6t08YDvaAv_VW17zSLDsFJIPhfFNY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a87d1892.mp4?token=IRs0Bw87CfnB02JzAJya1J76nRi-TciCZmwWsyTr3yhWsbRoWgUN1Ko9MUUR6uKqRO3PVMZzPgyYEP80KgMlNtRjNJBVat3BBi6kkvcL1bOfASCso3koJFT3IkP1-FBjBIa4qTzzmdSjXWvOWzJeVttfVVVvqFCV6Ix2qWdZkTXFZJN86581naCzTeGrpeLUcubX3VPGG8S6l5QoSngxjrOa9bbFlXW7bsD7WucDigDFhWBBvG5a0_-X1JrPP6Gq-PknWsqoPCm5heu0XL9F-esHBIUcWgW2YfOw5YoWH_7ntdpEKiGMGxRxLK0uY4yYbAIvkcGrtyp-fE_pUX0_0lZghb6d0QAWIXx1B-SUWNaDrUUXtWGt5-Yv_HJ3MylzItHQfpl-NV1JHUIVj2nKU8-yxD0CV76cX1R7Vrm0m7y6FLWxIK9cW7CAJRk-S9DOxHrnijRXiSLRl2x9yvRVMGMDruZVqD2eHp6knsGIBHAf5LmN0i6yiYtjf0DkCn19TCmzotiBg0ZgIdSsUn-U9vFETBTxemhN-7WdUVnDZlY1i3ZTzsFSV9LGemqpETQnMjpnVS2KegI6fHQtUXHBXxMA-tl8_hdYdrKp5xolu7Ud6TmD_KgM6vYxKtA4_rRE5-SW2PL1GAfIRK6t08YDvaAv_VW17zSLDsFJIPhfFNY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از لحظه وقوع تیراندازی در شهرک اسرائیلی نِوه تسوف (Neve Tzuf) در نزدیکی شهر البیره در کرانه باختری منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/148353" target="_blank">📅 13:46 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
