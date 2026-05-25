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
<img src="https://cdn4.telesco.pe/file/SZnCslrkV6i9soFGPeM_8sbSxNra2Htmj5kI6EvBRv2IW8HArmpNQZKmVGEfahrdYdozQl9SH1AnSe6go6i4jYHHWAtd2d6-fLKbKIQnDSrhQdHO-snv39-M8E8J5P7jBkzFHTONy1BntRVd0Pc7tNHiUkPeP2OvxJ3n4azpqp7JTNcsRx1kOBzyGY336l4hILd1D9s4wVRMmb9-b8Ku1CDb3sllvKgUP3b5sPAXxXwPtjnDHXnrn3sLFwIXOwefPB3UZhEjU2avlosnOYAmWIvkdXOHX74KkqYoEh2kXNbS00YEBP9Ifo0ELIHhF0_Aym4KCIYFrEfsP87VdMZJlA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 137K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 01:10:31</div>
<hr>

<div class="tg-post" id="msg-65064">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک  @News_Hut</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/news_hut/65064" target="_blank">📅 01:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65063">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHAtyPSq7EGr_mMR7BUSR83TT5FShXr-mf_jSrVSZTPPGxEfY7ozgIdevt-ky0o43_KRqJly5EcSFWj5LSZIemjy_QqDWxITZvsHGFmMJQs61laJEu2nYQiSBNop4teOYPUN-nht7bsuFyOoQ3p2PLTliZFZSzGfESpj0B1RlERGPBfuM22FBWvdg9sahin_ZGHid7etuEKXc0olR_M1kfmpgIKcDFmMKyAMW9l5Px_KbRaZs754K4AsK3Ki64J5xNXb6GpNGDT3M5VX6mGdIhFzn3FUG7zbKqTn7vYD3CaZOQTqHiOz5eq6IzrCmEiXVxDGpE4qndesUA6rIOw8Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری تایید نشده مربوط به انفجار لحظاتی پیش در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/news_hut/65063" target="_blank">📅 00:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65062">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/news_hut/65062" target="_blank">📅 00:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65061">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
📰
آمیت سگال، خبرنگار شبکه 12 اسرائیل:  ایران در حال حاضر فقط حاضر شده به توسعه سلاح‌های هسته‌ای رو متوقف کنه، در حالی که ایالات متحده چندین گزینه برای ذخایر اورانیوم غنی‌شده ایران پیشنهاد می‌دهد، از جمله فروش آن به ایالات متحده، انتقال آن به یک کشور ثالث یا…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/65061" target="_blank">📅 21:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65060">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">به صورت قانونی، ما یه "شورای عالی امنیت ملی" داریم که به "شورای عالی فضای مجازی" دستور میده که به بقیه اپراتورها بگه که اینترنت رو ببندن. به صورت غیرقانونی هم سپاه رو داریم که زنگ میزنه میگه اینترنت رو ببندن. زورش میرسه، میکنه! حالا دولت رفته یه "ستاد راهبری…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/65060" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65059">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
ترامپ: من به صورت الزامی از کشورهای خاورمیانه درخواست کردم که پیمان ابراهیم را سریعا اما کنند تا «جمهوری اسلامی ایران» را در ازای بخشی از توافق پیمان ابراهیم داشته باشند  @News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/65059" target="_blank">📅 19:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65058">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
ترامپ: توافق با جمهوری اسلامی ایران!! به خوبی درحال پیشرفته این یا توافقی بزرگ برای همه هست یا بازگشت به جنگ بسیار بزرگتر.  @News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/65058" target="_blank">📅 19:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65057">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🇺🇸
تروث طولانی و مفصل ترامپ درباره توافق با ج‌ا و پیمان ابراهیم:  مذاکرات با جمهوری اسلامی ایران به خوبی در حال پیشرفت است! این موضوع تنها یک توافق بزرگ برای همه خواهد بود یا اصلا توافقی صورت نخواهد گرفت؛ بازگشت به میدان نبرد و شلیک، اما بزرگتر از قبل و هیچکس…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/65057" target="_blank">📅 19:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65056">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‼️
فارس: همتی، رئیس بانک مرکزی برای بررسی و گفت‌وگو در مورد آزادسازی ۱۲ میلیارد دلار پول بلوکه شده تو قطر به دوحه سفر کرد @News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/65056" target="_blank">📅 19:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65055">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfU0vce32abf3mHz2LV-uofBIkU4MoNVsCS2j-zxwwwutM5VZ-6ZzvNY1_A4pB_w9FcSlkJHfdVVhzbBMfaErdY7LgdbLjSA3ZLfu8yjLVJcZd5nnTeTcpp7m6mECj88p8fYzw7MboOuacrKc25qI0wiipDnvDfoYu0T8bD8D6gZABGnEB_cTWuB7iTMZilkjBY6DT8xG6UeJ2tmyyt4eSCvgRA0t0RBy_TEOUZ8_hXEh3y1C6qpmkgRC6Lll41IIhZ23pauWYdEGnPOIe8FNwyrb2v8hY-oebS4mTeVH7GockZsrVnThzio8JFWyNt2vwXXNNZeI23RKIRCRfQBdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی گفته یا اموال بلوکه شده تو قطر رو آزاد کنید یا حتی یک گام هم در راستای توافق بر نمی‌داریم  در واقع الان دست بالا با جمهوری اسلامیه نه ترامپ! اینطوریه که می‌گن می‌خوای حمله کنی؟ خب حمله کن ۴۰ روز کردی مگه ما چیزیمون شد؟! #hjAly  @News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/65055" target="_blank">📅 18:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65054">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">جمهوری اسلامی گفته یا اموال بلوکه شده تو قطر رو آزاد کنید یا حتی یک گام هم در راستای توافق بر نمی‌داریم
در واقع الان دست بالا با جمهوری اسلامیه نه ترامپ! اینطوریه که می‌گن می‌خوای حمله کنی؟ خب حمله کن ۴۰ روز کردی مگه ما چیزیمون شد؟!
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/65054" target="_blank">📅 17:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65053">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">چه افتخاری هم می‌کنند حیوون های حرومزاده...  سه ماهه حق طبیعی مردم رو ازشون گرفتین و الان از بازگردوندش، دستاور می‌سازین؟ باید رید به سر تا پای دولت حقیر پزشکیان و امثالهم #hjAly</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/65053" target="_blank">📅 17:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65052">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‼️
فارس: همتی، رئیس بانک مرکزی برای بررسی و گفت‌وگو در مورد آزادسازی ۱۲ میلیارد دلار پول بلوکه شده تو قطر به دوحه سفر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/65052" target="_blank">📅 15:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65051">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خبرگزاری فارس: در جلسه ستاد ویژه ساماندهی فضای مجازی که با ریاست عارف برگزار شد بازگشایی اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف مصوب شد.  @News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/65051" target="_blank">📅 14:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65050">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJ-ZAVlXoKO7TQVaQ6v2inZivZCrOpn_im9UcvLB0usvp1LuNazYGFXiaXl1kz91rLfuZkdmooh92KC3Y6DosUHzTmF5q3yirpIh87W1OkS8WsjbPzZKf1MRxwtWoFiukylcBhGi-lqXDSL9xn2O3JkEEXme2gR3kkbntPcqc4zg8tXEksy4aGk0ZB3KqU-eJkdbqKghgeaH7eRNNsU4p27mf-75OYcCt2yac4f8mO02b3u9-F34MQccqd9qEHRiLvUzZUXUuAmFWQZ_72yICqNEFKzeHAT8j6Y1rrm60_iGaM83aFwhFDBYSxaz-mHu70hvs8Ed_UtUCDr8duL5Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: در جلسه ستاد ویژه ساماندهی فضای مجازی که با ریاست عارف برگزار شد بازگشایی اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف مصوب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/65050" target="_blank">📅 14:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65049">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df45acb25e.mp4?token=n0tumdSiTBnReTq9rZdT1ohVZ1tKsYXHwU5b78ThQtBi0PpjnDloEqtPuaaQPlkP2b41GLi3wQ1TYboUrbj7P_zlwTi8oJcc6Oy_cYyzKA6rIhNNnOYGTgb0tr6UxQLw3rz22htN24upCuyg3TRoqyp7lRSmGIZrkkHJQxtCO1uPPlukw0qn02AL4MMrnRlf8ut0dk5zj7I2_AyDNcckb_diSMa5c4DrN1s4Uhli82X3-3-ZvQiD3R0maYqLefJ14EfoBJ4IOt8A9w8S7eItBLP9LsldVbeeFx6v338pHTpni4Gvb4PdK5__Xw-Rz2rRgp-wQpGipCtNxT5TQ-Zwqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df45acb25e.mp4?token=n0tumdSiTBnReTq9rZdT1ohVZ1tKsYXHwU5b78ThQtBi0PpjnDloEqtPuaaQPlkP2b41GLi3wQ1TYboUrbj7P_zlwTi8oJcc6Oy_cYyzKA6rIhNNnOYGTgb0tr6UxQLw3rz22htN24upCuyg3TRoqyp7lRSmGIZrkkHJQxtCO1uPPlukw0qn02AL4MMrnRlf8ut0dk5zj7I2_AyDNcckb_diSMa5c4DrN1s4Uhli82X3-3-ZvQiD3R0maYqLefJ14EfoBJ4IOt8A9w8S7eItBLP9LsldVbeeFx6v338pHTpni4Gvb4PdK5__Xw-Rz2rRgp-wQpGipCtNxT5TQ-Zwqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمد نگینی‌پور، مستندساز حکومتی مستندی ۴ دقیقه‌ای از حضورش تو پزشکی قانونی کهریزک منتشر کرده از اعتراضات ۱۸ و ۱۹ دیماه‌،
تو خود مستند حکومتی که منتشر شده تعداد بالای کشته‌شده‌ها و کانتینتر های حمل جسد دیده میشه که جنایت خودشون رو به کار دشمن ربط میدن و ابعاد بزرگ این جنایت مشخصه!!
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/65049" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65048">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2rayYar</strong></div>
<div class="tg-text">🔐
سرور اختصاصی با پینگ فوق‌العاده پایین
مناسب گیم، ترید، استریم و استفاده حرفه‌ای
✅
سرعت و کیفیت عالی
✅
آی‌پی ترکیه واقعی
✅
پایداری بالا و بدون قطعی
✅
مناسب استفاده 24/7
✅
بدون محدودیت زمان و بدون ضریب
💰
قیمت تک: هر گیگ 150 هزار تومان
🤝
قیمت همکاری: هر گیگ فقط 120 هزار تومان
با ضمانت عودت وجه در صورت قطعی
🙏
برای تست و ثبت سفارش پیام بدید و از طریق ربات هم میتونید خرید هاتونو انجام بدید
✉️
:
@V2rayYar_bot
@V2rayyar_sup</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/65048" target="_blank">📅 13:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65047">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d1b11fd8.mp4?token=s3IG9X_NqzYUCCPHDKmfT6gifTMrfY8ln5xBnM2s0YsHBSLrhM0Po2z5jgxQhjb4b38k80yvugYf1uqN75X6wtvcscHOAzU_sfydop19zgI1f3b4jtTpvZ4nOY5hf5wF5R8K0sOBI-SGTS7mLszjHqtpIvVqHLkBq9qg5rqhpFJUcBrDs4RJlEkjceRd7MWfRbiCAC1due_MTLZ1K-I0vpu2z_V-CySsQOqs0HuqsVcWANKxCg3sqSs_7b1892LsHh1kmSqydx_8hR4EIyTEMNk5xKoNz9lBINCW3O77iePMRsTI5CrNHdehYnt1ngzjYzKOrfwfv12l6obyZSKagg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d1b11fd8.mp4?token=s3IG9X_NqzYUCCPHDKmfT6gifTMrfY8ln5xBnM2s0YsHBSLrhM0Po2z5jgxQhjb4b38k80yvugYf1uqN75X6wtvcscHOAzU_sfydop19zgI1f3b4jtTpvZ4nOY5hf5wF5R8K0sOBI-SGTS7mLszjHqtpIvVqHLkBq9qg5rqhpFJUcBrDs4RJlEkjceRd7MWfRbiCAC1due_MTLZ1K-I0vpu2z_V-CySsQOqs0HuqsVcWANKxCg3sqSs_7b1892LsHh1kmSqydx_8hR4EIyTEMNk5xKoNz9lBINCW3O77iePMRsTI5CrNHdehYnt1ngzjYzKOrfwfv12l6obyZSKagg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو:
ترامپ قرار نیست توافق بدی امضا کنه. هیچ‌کس به اندازه ترامپ تهدیدِ هسته‌ای شدن ایران رو جدی نگرفته
خیلی مطمئنم که یا به یه توافق خوب می‌رسیم یا مجبور می‌شیم یه جور دیگه باهاش برخورد کنیم.
ولی ترجیح ما توافق خوبه.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/65047" target="_blank">📅 13:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65046">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">قالیباف دوباره به عنوان رئیس مجلس انتخاب شد
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/65046" target="_blank">📅 11:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65045">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZc4cMZjNE-_5oT8xWpVl1-ACXcAo0MNfKc74eQQM3cXVMYEKcNoXYn0bqITGczC6O-kkff2klgm6L2bDnSPK59ey-GvRfznam0wQ2tYieYWg5gtMoSEVtT4RwsW5fkNxZQfkZFBH3VksojdCtmebBHD7e11XST78Auhl05ezo3Ppv8YvvV2ba_qixIHSXPm23PDMX3U2IVl_4B25ix-DPX49PUlNLeBG5DFTHFEfdMNow3tVEY9l4vzm6PtzkixPgKFuzCjM2M9TLVXyl9xvF9oofGWraaKOBTxGoZlHuYQ0Q4Bq56iAbIKN9SkE5rYj9QA93Ut0ssHe-4cZ4qHJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوج حقارت ارتش
ایران
به روایت تصویر:
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/65045" target="_blank">📅 10:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65044">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو: توافقی برای پایان دادن به جنگ علیه جمهوری اسلامی ممکن است «امروز» حاصل شود
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/65044" target="_blank">📅 10:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65043">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام: اگر در واقع به نتیجه این مذاکرات برای پایان دادن به درگیری ایرانی، متحدان عرب و مسلمان ما در منطقه توافق کنند که به توافق‌نامه‌های ابراهیم بپیوندند، این توافق را به یکی از مهم‌ترین توافق‌نامه‌ها در تاریخ خاورمیانه تبدیل می‌کند.  پیوستن…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65043" target="_blank">📅 00:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65042">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKHbHi3o4Q6PLw224OhGtC26TNGxJJmA6CJpU3db1DjJFLZIuw_xwib-2-yVjVgQJp1df37dnAXzAaWWuBBmQoLHyrEtVpwISm3Ohx0kwrls7lPBf4MeA0c-G-XQm0eeJLT49vHoc7fxI4KDTHK4RCUNKtgyXQgCi3zPFxIMaZ-hCT_wad6RlUnovAlF_gZFjsEb7IHBwqH6kqdRBjVAGPjzwLhxYnlkc4VvWoNlFQzMZfg4UVC-U78VMorwFxed55R1o5UYswgqp5op-Xy0B_m_lZlQnlJG4lDzzPxbY7SSh_WOARRNwmqdGiYcdjs7GCxwTY8sdkKe8KhBgYFKlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
اگر در واقع به نتیجه این مذاکرات برای پایان دادن به درگیری ایرانی، متحدان عرب و مسلمان ما در منطقه توافق کنند که به توافق‌نامه‌های ابراهیم بپیوندند، این توافق را به یکی از مهم‌ترین توافق‌نامه‌ها در تاریخ خاورمیانه تبدیل می‌کند.
پیوستن عربستان سعودی، قطر و پاکستان به توافق‌نامه‌های ابراهیم فراتر از تحول‌آفرین برای منطقه و جهان خواهد بود. این یک حرکت درخشان از سوی رئیس‌جمهور ترامپ است.
به عربستان سعودی و دیگران: اکنون زمان جسارت برای آینده‌ای جدید در خاورمیانه است. من انتظار دارم، همان‌طور که رئیس‌جمهور ترامپ پیشنهاد کرده است، شما در واقع به توافق‌نامه‌های ابراهیم بپیوندید و به طور موثر درگیری عرب-اسرائیلی را پایان دهید. اگر از رفتن به این مسیر که توسط رئیس‌جمهور ترامپ پیشنهاد شده است خودداری کنید، این موضوع عواقب شدیدی برای روابط آینده ما خواهد داشت و این پیشنهاد صلح را غیرقابل قبول می‌کند. علاوه بر این، این موضوع توسط تاریخ به عنوان یک محاسبه‌گری بزرگ دیده خواهد شد.
رئیس‌جمهور ترامپ: در گرفتن یک معامله خوب با ایران بر موضع خود بایستید. به همان اندازه مهم است که بر موضع خود در اصرار بر پیوستن عربستان سعودی و دیگران به توافق‌نامه‌های ابراهیم به عنوان بخشی از این مذاکرات بایستید.
دوباره، این یک پیشنهاد درخشان از سوی رئیس‌جمهور ترامپ است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/65042" target="_blank">📅 00:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65041">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آیا دونالد ترامپ، باراک حسین اوبامای دوم خواهد شد و دستور آزادسازی ۲۵میلیارد دلارِ جمهوری اسلامی را می‌دهد یا خیر؟!  بزودی خواهیم دید! @News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65041" target="_blank">📅 22:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65040">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_7RSwefEq7FzLYLjJasOMhExQApmBUMrpTLMNLMXAQ0_FOXQRB6SI2Yza71REutbKs6G6a-JLm7V1rijzLiJOFkEyj4Hg5-P8bMAuqbaW6goaD3syFvP8NRkGqvX6tAS5RJ3-qOqTWBAEU-yjJvPqrv7q9x68vqIEBRjiUutBRUhCnRZWbHiNXfTNs8Jl08Rnuwt4_0XALRdpErDbmA2BnVrwvwGJHvfaLLgVdGyAMmIKc1gTPiCeDeJK45vsopu701PhILgMePsdtzmUEuE34ZbsBCI1ERvF0CYCjtNYvxZ1umxCDWypNFy7sZzHKNBvCGZnBzWk3pLRbxMfU6jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:  اگر من با ایران توافقی انجام دهم، توافقی خوب و مناسب خواهد بود، نه مانند توافقی که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری روشن و باز به سوی سلاح هسته‌ای داد. توافق ما دقیقاً برعکس است، اما هیچ کس آن را ندیده یا نمی‌داند چیست. هنوز…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65040" target="_blank">📅 22:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65039">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgaXH5RUI9d-Py7XMKdhHvcpRDwjG105e7nQ0IYaE7-0G3_b4354NUIGySEBv_ZANNCJaMJZscj4029wsDKojy1r-e7qsCgD5XJAt-F0UkyZDs-UEB2FxFkcdcgwL_-zxkeBs55sH7Uxjx4ox3UosimJ6i353l5DVe7OVXwJPYtWE33SYwsZcx9vlMizYFMizd-ApucD6kRWwVVXgy2FJn9xNOnYUXvxyrHUDapr1HSYl-jXbYRy2epE1rm7ocLhDHqqjiplFPDfs2leYl71OtTlqV1X55LBnAdqoWeTa-x2b9nxQ3GvpnV0eNERSn_KALtntT3pbX9PEzimOcsyzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
اگر من با ایران توافقی انجام دهم، توافقی خوب و مناسب خواهد بود، نه مانند توافقی که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری روشن و باز به سوی سلاح هسته‌ای داد. توافق ما دقیقاً برعکس است، اما هیچ کس آن را ندیده یا نمی‌داند چیست. هنوز حتی به طور کامل مذاکره نشده است.
بنابراین به بازندگان گوش ندهید که از چیزی که هیچ چیز در مورد آن نمی‌دانند انتقاد می‌کنند. برخلاف کسانی که قبل از من بودند و باید سال‌ها پیش این مشکل را حل می‌کردند، من توافق‌های بدی انجام نمی‌دهم
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65039" target="_blank">📅 22:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65038">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو: توافق نهایی با ایران به معنای برچیدن تأسیسات غنی‌سازی هسته‌ای و حذف مواد هسته‌ای غنی‌شده است. من و رئیس جمهور ترامپ توافق کردیم که هرگونه توافق نهایی با ایران باید خطر هسته‌ای را از بین ببرد. این به معنای برچیدن سایت‌های غنی‌سازی هسته‌ای ایران…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65038" target="_blank">📅 20:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65037">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: من معامله بد انجام نمی‌دهم؛ در مورد جزئیات توافق فعلا حرف نمی‌زنم، صحبت های خوبی در راه است
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65037" target="_blank">📅 17:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65036">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تنها چیزی که ترامپ تغییر داد رژیم غذایی مردم ایران بود
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65036" target="_blank">📅 15:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65035">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db79f15b4f.mp4?token=BGX7lmupHBdLVMqT1KyZdsaRMjbFJwqhfwpxk38KYaKzxyk_Ndo23p4VHsv-XUbtJEk8A1OFBHZJL7wNvkE_GJK8mbo5KwzlZIDWGkBJuCXNrLQSA18RwP7GLYeySabY5UFvi-nNbm2GaIqPJpFY9D2WxiZ8gCELMetj5xKnjUB3brIbrQK-nJLSmEszdnYUq6oeWCd7JibH0e84PGNp5flS-OFFF5f-wEJ9EdT_ylsN7md9oM9hNSsspfX6ErYPMmpxKJB3LdcgHTxo6IvGm46WOXMJT-cydsDyiVsxeKWSmVvbzOE-yCSViOp-eavfhYsSgfo8cM0__Y3bQSgI8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db79f15b4f.mp4?token=BGX7lmupHBdLVMqT1KyZdsaRMjbFJwqhfwpxk38KYaKzxyk_Ndo23p4VHsv-XUbtJEk8A1OFBHZJL7wNvkE_GJK8mbo5KwzlZIDWGkBJuCXNrLQSA18RwP7GLYeySabY5UFvi-nNbm2GaIqPJpFY9D2WxiZ8gCELMetj5xKnjUB3brIbrQK-nJLSmEszdnYUq6oeWCd7JibH0e84PGNp5flS-OFFF5f-wEJ9EdT_ylsN7md9oM9hNSsspfX6ErYPMmpxKJB3LdcgHTxo6IvGm46WOXMJT-cydsDyiVsxeKWSmVvbzOE-yCSViOp-eavfhYsSgfo8cM0__Y3bQSgI8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو: امروز اخبار بیشتری از توافق با ایران منتشر می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65035" target="_blank">📅 14:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65034">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIWk9CfEqvOzRx2Nfc_n9S3Q_PClUHUlWhjw32rZgopwa7MFo7xiimyzvhYq85rleYSSabQdPqBxqk05Z-f1U83CCHIwSsm3walu7LM5CrjZG7a_xwzeXhVQmT5L_FiErmh5YqmCAOvR5TJcg4JJfcTpuM2VloWae-lbZ3jgh9r27pL-TD_tJkgHmGVUGZC7AcqvpY5YW0Erlbt1c4Ba4vSwOUqQi2Z_TWiWEL5cd9oFoTqppU_KIfCn8nmdiDSz3NF59j6z7HC7rjN1qexeYgJVUuz33lOgdjIFCVrBCKssw1m-oL0Ai-JzCaz0_0PfWjRIGJmRhJLwaPH475OEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کجایند مردان بی‌ادعا؟
🗿
#Fun
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65034" target="_blank">📅 14:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65033">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مراد ویسی: سپاه می‌خواد روحانی، احمدی‌نژاد و پزشکیان رو ترور کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65033" target="_blank">📅 10:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65032">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BVF5ponrdWOcY52KyfA1oDKpcnKPmPXdsBDu5g-TjRkhPFPKkX_7Eon_IoTyin5bD9s3qM3NJxh9my7f-63s3VTIA8Jw2ZffYoJqqsoaE5NSmNx9zerUzPD7qVaphm9nuDqndySRK-mB_ox8sZI3tUMGmx3f7neQxSACR-WuR6LFuYU7A4Zbu-gSbKyEKc6CYqDeVcYQIb7YhUFHVWhba0clfh3Iw6_uZ_Tg0M-7AC7lW1zduKLlNafFaPd3XMXWLK9RL4onwrb5AVXEr3LUHvAQEUb_m-FSr8NH0Z0XpaWZbCIxmAx5OVwUcgKx4tOzF4mMNcBAelkpByW0RJ6fmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار تتر بعد از اخبار دیشب درمورد توافق تا زیر 170 هزارتومان ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65032" target="_blank">📅 10:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65031">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
آکسیوس: توافق بین دو طرف امضا شد.
👎
این خبر فیکه و آکسیوس و خبرنگاراش همچین خبری نزدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65031" target="_blank">📅 01:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65030">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f43de325c3.mp4?token=o3r4J8CfG7jAyRs2MGMIazB1-tkF9p-elUIOkTts4tvdfmroYihbwBAVJg00gftZhCM44Jdvh9xShjzP5ok964KT8Kdo2IwEx7qY_V9Rdv0YMsGNqTIL1SiXchCjl62a_PHd9OmBxOKIucNeVIiOYg9pE9SUJz_o_2V5V8FbrFkubz47locK38CWgqRTwgXu8fRDjMLYGrCemNGkD-b3fitvxMgFUUBkkonKzd_Z0eV3XPoLWli1jb52uLeMCDs5OmHh8NWpk6VE-0ps4j9kDfAekO4acUF5YfPrWkdg4l28YpYO4_FH5r1IrCkNRfzf0k4a5WA7WBNZpMwQeGzW0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f43de325c3.mp4?token=o3r4J8CfG7jAyRs2MGMIazB1-tkF9p-elUIOkTts4tvdfmroYihbwBAVJg00gftZhCM44Jdvh9xShjzP5ok964KT8Kdo2IwEx7qY_V9Rdv0YMsGNqTIL1SiXchCjl62a_PHd9OmBxOKIucNeVIiOYg9pE9SUJz_o_2V5V8FbrFkubz47locK38CWgqRTwgXu8fRDjMLYGrCemNGkD-b3fitvxMgFUUBkkonKzd_Z0eV3XPoLWli1jb52uLeMCDs5OmHh8NWpk6VE-0ps4j9kDfAekO4acUF5YfPrWkdg4l28YpYO4_FH5r1IrCkNRfzf0k4a5WA7WBNZpMwQeGzW0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همونطور که اکثریت رسانه‌ها گفته بودند، احتمالاً یک راستی آزمایی ۳۰ روزه در قالب توافق موقت، برای پایان رسمی جنگ و بازگشایی تنگه هرمز شکل خواهد گرفت، و بعد از این توافق طرفین به سراغ مسئله‌ی اصلی یعنی هسته‌ای و تحویل اورانیوم ها خواهند رفت  شما اینطور بخوانید…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/65030" target="_blank">📅 00:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65029">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fad8544d2.mp4?token=GtPHt7-EAx-o4NsJ2J35zJa83-xFaF2BgQgyGf9BLztgo9mvTqaV6givnjenDFG2hhH4_gXUwSKh7UCwzDwUya8oncTrYr1irT_yOIrAJxFtuqI0yweDo0RLgHFAcHHS0ZkFOt8ASFE1uA47RDnGvQU-Cs9IJho8AgvC5_6MewB7vQ3LX6gffyV3-u5bNeFU0FLehQOOod5VqV5eGsXGnTfJd8yBSbU1RdjaPd3UcIsozlnV4YIr9EZJXtqumi3jEKb4x0CE4O9Ah4epwUi78KmCuZTQXfp10tWgj7SBw8lFUREtL6LU-0H4_Gv2n9MxkkbDgjkYGuW_jWAqBTPi9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fad8544d2.mp4?token=GtPHt7-EAx-o4NsJ2J35zJa83-xFaF2BgQgyGf9BLztgo9mvTqaV6givnjenDFG2hhH4_gXUwSKh7UCwzDwUya8oncTrYr1irT_yOIrAJxFtuqI0yweDo0RLgHFAcHHS0ZkFOt8ASFE1uA47RDnGvQU-Cs9IJho8AgvC5_6MewB7vQ3LX6gffyV3-u5bNeFU0FLehQOOod5VqV5eGsXGnTfJd8yBSbU1RdjaPd3UcIsozlnV4YIr9EZJXtqumi3jEKb4x0CE4O9Ah4epwUi78KmCuZTQXfp10tWgj7SBw8lFUREtL6LU-0H4_Gv2n9MxkkbDgjkYGuW_jWAqBTPi9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همونطور که اکثریت رسانه‌ها گفته بودند، احتمالاً یک راستی آزمایی ۳۰ روزه در قالب توافق موقت، برای پایان رسمی جنگ و بازگشایی تنگه هرمز شکل خواهد گرفت، و بعد از این توافق طرفین به سراغ مسئله‌ی اصلی یعنی هسته‌ای و تحویل اورانیوم ها خواهند رفت  شما اینطور بخوانید…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65029" target="_blank">📅 00:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65028">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تا این لحظه طبق اخبار، الحدث، آکسیوس، نیویورک‌تایمز، سی‌ان‌ان، آسوشیتدپرس و... احتمال توافقِ موقت بسیار بالاست، یعنی توافقی که در اون توافق کنند برای به ثمر رسیدن توافق هسته‌ای!!!!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65028" target="_blank">📅 00:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65027">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IKVCl5n3CLGNTeFmfheDOTunc1HpxzLNXurx1o7g6DGjZs_iRipBaDM3jcQdytjJnjVU9KvJICJ9iBTilUT9nntUcwDEhj7gXY8YQg1wUYlzN-YftA33W4opSgfYG1uuVQqbnfJ1S2sKcGdfsCYQEP7iDOPo7YsSRmVOw96avNNg4XyR8u5kKyvj3kG5sC2vWmrLEPn6rK_JFc_njwcjNloscdR8UJJ9a64nwpl_nioqC92s0Snb9hnqn0gProNADpK7b45vNG0qkXz5V3x8a-gjK-mjchWTGnLIVZUDcBr0DMafTURikUjtR-_rhGOsIUzo8z2uHmIASz85P8tqmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ:
من در اتاق بیضی کاخ سفید هستم، جایی که همین حالا تماس بسیار خوبی با پادشاه محمد بن سلمان آل سعود، عربستان سعودی، محمد بن زاید آل نهیان، امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی، و وزیر علی الثعادی، قطر، مارشال فیلد سید عاصم منیر احمد شاه، پاکستان، رئیس‌جمهور رجب طیب اردوغان، ترکیه، رئیس‌جمهور عبدالفتاح السیسی، مصر، پادشاه عبدالله دوم، اردن، و پادشاه حمد بن عیسی آل خلیفه، بحرین، در مورد جمهوری اسلامی ایران و تمام موارد مرتبط با یک تفاهم‌نامه مربوط به صلح، برقرار شد. توافق‌نامه‌ای به طور کلی مذاکره شده است، مشروط به نهایی‌سازی بین ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگر، همان‌طور که در بالا ذکر شد. جداگانه، من با نخست‌وزیر بیبنتانی، اسرائیل، تماسی داشتم که به همان ترتیب بسیار خوب پیش رفت. جنبه‌های نهایی و جزئیات توافق‌نامه در حال حاضر در حال بحث هستند و به زودی اعلام خواهند شد. علاوه بر بسیاری از عناصر دیگر توافق‌نامه، تنگه هرمز باز خواهد شد. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65027" target="_blank">📅 00:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65026">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahshid</strong></div>
<div class="tg-text">بله  مگه چیه ما با ۹۰ هزار ... گواهینامه مون گرفتیم</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65026" target="_blank">📅 23:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65025">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گواهینامه شده ۱۵ میلیون تومن!!!!
الان یکی میاد می‌گه حاجی ما با ۵۰ تومن گواهینامه گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65025" target="_blank">📅 23:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65024">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بستن تنگه‌ی هرمز در جنگی که ۹ اسفند آغاز شد، تمامِ معادلات آمریکایی هارو بهم ریخت، اون‌ها حتی چند روز قبل مین‌روب های خودشون رو هم از منطقه خارج کرده بودند! دومین مسئله‌ی شوکه کننده برای اون‌ها حملات وحشیانه به کشور های عربی بود  هر زمان آمریکا_اسرائیل به…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65024" target="_blank">📅 22:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65023">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">باز تو این دقایق فیک‌نیوز و نویز‌ها بشدت افزایش پیدا کردن، اخبار ضد و نقیض زیادی به گوش می‌رسه، اما کلیت ماجرا اینه که تهران آخرین پیام خودش رو به عاصم‌مونیر داده تا به آمریکایی ها برسونه، ترامپ نهایتا تا دو روز دیگه بعد از دیدارش با ویتکاف و کوشنر، تصمیم…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65023" target="_blank">📅 22:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65022">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">باز تو این دقایق فیک‌نیوز و نویز‌ها بشدت افزایش پیدا کردن، اخبار ضد و نقیض زیادی به گوش می‌رسه، اما کلیت ماجرا اینه که تهران آخرین پیام خودش رو به عاصم‌مونیر داده تا به آمریکایی ها برسونه، ترامپ نهایتا تا دو روز دیگه بعد از دیدارش با ویتکاف و کوشنر، تصمیم می‌گیره، یا از خواسته هاش عقب نشینی می‌کنه و یا اینکه دوباره جنگی برای اعلام پیروزی شکل می‌گیره، تا این لحظه طبق اخبار، الحدث، آکسیوس، نیویورک‌تایمز، سی‌ان‌ان، آسوشیتدپرس و... احتمال توافقِ موقت بسیار بالاست، یعنی توافقی که در اون توافق کنند برای به ثمر رسیدن توافق هسته‌ای!!!!
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65022" target="_blank">📅 22:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65021">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ شنبه با ویتکاف و کوشنر دیدار می‌کند و یکشنبه تصمیم نهایی برای توافق یا جنگ دوباره گرفته می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65021" target="_blank">📅 19:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65020">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ شنبه با ویتکاف و کوشنر دیدار می‌کند و یکشنبه تصمیم نهایی برای توافق یا جنگ دوباره گرفته می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65020" target="_blank">📅 19:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65019">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
📰
ترامپ در گفت‌وگو با آکسیوس:  در حال حاضر احتمال کاملا 50 / 50 است که یا با ایران به توافق برسیم یا دوباره جنگ از سر گرفته شود. یا چنان محکم‌تر از همیشه به آنها حمله نظامی می کنم که تا حالا مثل آن را ندیده‌اند، یا توافقی خوب را امضا می‌کنیم + ترامپ شنبه با…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65019" target="_blank">📅 19:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65018">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
فایننشال تایمز: ایران و امریکا به یک توافق آتش‌بس ۶۰ روزه نزدیک شدند!!  @News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/65018" target="_blank">📅 19:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65017">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
📰
#مهم؛ فایننشال تایمز: میانجی‌ها معتقدند که به توافقی برای تمدید آتش‌بس به مدت ۶۰ روز نزدیک شده‌اند.  این پیشنهاد شامل: بازگشایی تدریجی تنگه هرمز گفتگو درباره رقیق‌سازی یا انتقال ذخایر اورانیوم غنی‌شده بسیار ایران کاهش محاصره آمریکا بر بنادر ایران رفع تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/65017" target="_blank">📅 19:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65016">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eU2NdRiqCFZ4WfhOaZR9TS5zmHwGoivEXJ-Ka2Vqnbow3MdsVjB6pDtB45o9AmH5a-3ts5XWW9ILbZYu41lXlPPxnpmX3EcoDNsr42KeATqIvoCHLw-iD_vbpKRPDdZabb9S4ivl6N5bCBGhoU0UXShtwcSLanJMJZzE5p9LwRoNOIuiROBeREZEn5QcPclICSf2jgieLyzR-J_4uH_w7UvgBhjK8XWVcxYz0zAHAxAnsPQXSuBMzOQgk8bWn_vRp272LxdkQJf0tHqjo4xtTaxJNjZVnV6hgwhNEz5hvf209Jd9vtfZhhTgsMtwxAFdpvRuKRcF-GB_JI3wF3bf1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید ترامپ تو تروث‌سوشال: ایالات متحده خاورمیانه!! با پرچم امریکا روی نقشه ایران
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/65016" target="_blank">📅 18:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65015">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛ مارکو روبیو: ممکنه امریکا به زودی خبری در مورد ایران منتشر کنه شاید هم نکنه امیدوارم این اتفاق بیفته
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/65015" target="_blank">📅 17:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65014">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b75d0f1f7.mp4?token=qKTpg4MIsCtu8nbPFxeDR5eRJwyHeWg9WWPHVE-MjSXN7MiMV2ZrsiWBt3bwYbFvVAWapESj6MQsTEsQJCOvTmqEIJJQ9JkpB2ipbr5ffB9uF_9oHAF4zbuvkNM1Jy_yxe5bBD4l8l7H-zjiZiflKiArYU4i0ExQSULOQlty1Z_Bnwhgv5VL7HOYnOZn8nTgoY9mNwf25sON-XFc9cVkgcS3_DHpqTH4IVKsZeKWmv3nI5eePLSpI8OmH3TNVGSYTomT2OEfpKtvy66BzmNoaaYtdj1eSgsnFrtZ6OhCfMvVkHFgxD4IuFy1VrdAkXSZw8y6Mt3tAlBhZ0_FrZOExg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b75d0f1f7.mp4?token=qKTpg4MIsCtu8nbPFxeDR5eRJwyHeWg9WWPHVE-MjSXN7MiMV2ZrsiWBt3bwYbFvVAWapESj6MQsTEsQJCOvTmqEIJJQ9JkpB2ipbr5ffB9uF_9oHAF4zbuvkNM1Jy_yxe5bBD4l8l7H-zjiZiflKiArYU4i0ExQSULOQlty1Z_Bnwhgv5VL7HOYnOZn8nTgoY9mNwf25sON-XFc9cVkgcS3_DHpqTH4IVKsZeKWmv3nI5eePLSpI8OmH3TNVGSYTomT2OEfpKtvy66BzmNoaaYtdj1eSgsnFrtZ6OhCfMvVkHFgxD4IuFy1VrdAkXSZw8y6Mt3tAlBhZ0_FrZOExg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقائی، سخنگو وزارت خارجه:
ما هم بسیار دور و هم بسیار نزدیک به یک توافق هستیم.
دیدگاه‌ها به هم نزدیک‌تر شده‌اند، اما نه به حد یک توافق — بلکه به حدی که ممکن است بتوانیم به راه‌حلی برسیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/65014" target="_blank">📅 17:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65013">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73653df566.mp4?token=YCJNA5mw3yh47xra9wUIqrevmtUhZz60__3YXUlpMZ_mCn9bgntV_zI29zkDSs67LSvsSOSy6TjCVmKbnNodRPp6Ujr2brWksAFqQopMyuViD-2q1Oq2a3U9whDCrGnicZRFI-EiR16yrndk6D4IH6H0RrjwD1dVaule1cgDdlxnyiGqhQrCT3RCXKnD6JkY14Z53bRVtDKzXW-A2UHe7KhmRokFrrt2AP8FOwXrR2j8k_e0S3IwHrpqF8A2pEkEHx8fUMbID-z4tjUsJFFpCLe_AuKozLojfgkfjWHlOIdhYbLWb8AEaxDlOw1PLVb8jmZhQNZWKVZ1aReZ8gkGXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73653df566.mp4?token=YCJNA5mw3yh47xra9wUIqrevmtUhZz60__3YXUlpMZ_mCn9bgntV_zI29zkDSs67LSvsSOSy6TjCVmKbnNodRPp6Ujr2brWksAFqQopMyuViD-2q1Oq2a3U9whDCrGnicZRFI-EiR16yrndk6D4IH6H0RrjwD1dVaule1cgDdlxnyiGqhQrCT3RCXKnD6JkY14Z53bRVtDKzXW-A2UHe7KhmRokFrrt2AP8FOwXrR2j8k_e0S3IwHrpqF8A2pEkEHx8fUMbID-z4tjUsJFFpCLe_AuKozLojfgkfjWHlOIdhYbLWb8AEaxDlOw1PLVb8jmZhQNZWKVZ1aReZ8gkGXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توئیتر اکانت ترامپ که با هوش مصنوعی به ویدئو درست کرده از مجری سی‌بی‌اس که مخالف خودشه و ترامپ میندازدش تو سطل زباله :/
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/65013" target="_blank">📅 15:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65012">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hQJmV-vg-aHj6HEzFC6PujccYIlAYRfAf_j55MMw5uQkHt2vlzNpn5f86PVFrlVcNS4sy-aC881GGfsquV9-4onr_Oa_XyAZDl6z8B330TEcV2jkR4emDaLU6-oLYpXx_hzjIoJZCVH2JmCinWSUMShEhBcWPJY5dltYFKhy6Pf_K4V-XhEI1k9NLkQvCuhhBF2ldNfnmQp7DaFuZA1syChgEgK-eWhWFqs9yhJu2Oj9snyzZyD-zFnRcftGFocoXf6FUxWdLuDBn34YOeHw3nlXcLP2rfAVaScLEErK2xXi_d1nCgUoK6v6qZwCfCdFI1C1GVDK_HGO8-5xAeqkYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ عروسی پسرش بود نرفته، آخر هفته برنامه گلف داشت که کنسل کرده و تو کاخ سفید مونده حالا خبرگزاری‌ها شدن دو دسته یه دسته میگن توافق نزدیکه حتی متن توافق منتشر میکنن یه دسته متن توافق بقیه رو تکذیب می‌کنن و میگن کلا حتی نزدیک توافق هم نیستن دو طرف.  این وضعیت…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65012" target="_blank">📅 14:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65010">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S4bBiJ3S0Uaoio48apD7KvHSY1GFpnTMOVLtmXauN9XGB0qQha0cgaE1So2HcqzbkQ-hUG_LP5DIpApXNSWu2mlepQ9KGB-Xnf8cH4YMqtQ91bydsRRBPgcKCEHtXmL-rH3dJzPnaC_PggggaLqQEoMV2S4sQ99naP6HQ-QHAD27Hj1zefUtqIMFjEUeZMBOFwHSP0-MkkzwSp1xlFohmMg8asD6IWR3gVgiSR7jFBkleW8tbYircJQN05Bu0nE28Mf0DCeXkWmiYFNQGRrSdKJRQTJ7-RwP_-lJJt8H2eoW4Pufw-vDBoRkfN3OO3ZD0jboHC2PII3_qJXQnEY2Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6eddfffea5.mp4?token=Igrzian1tQveXZ5BPXfJRRIkvzCSpr2KHc3J2jS1wNwEvuMBFS48v-Nlpg6COqc8bq53Cw27CRwDkwp-4WtOga5DkIjQB1yWUbCNgcR7GaVlQrpmKWV-CeNuOK2nUjTgLko2b2DdLcExWvMnst5k2hdrGXNWH-k9_K0rzjdcm30OVDfX3mUwqRoAAlpmZ2x4XOmev3A5WSMq858AzskWmpb9g2Q_dVu5gIlZ6SnS3PUsmojoSP4ZH2p7_eeFd7snJ8-WJlX1wZJromZg8wnYVfz-CjbfqlWpfcCXejNVlusRPqj6O_2nPTfBskWLnRViwYDeyhG78GfMnF1ZGkVzCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6eddfffea5.mp4?token=Igrzian1tQveXZ5BPXfJRRIkvzCSpr2KHc3J2jS1wNwEvuMBFS48v-Nlpg6COqc8bq53Cw27CRwDkwp-4WtOga5DkIjQB1yWUbCNgcR7GaVlQrpmKWV-CeNuOK2nUjTgLko2b2DdLcExWvMnst5k2hdrGXNWH-k9_K0rzjdcm30OVDfX3mUwqRoAAlpmZ2x4XOmev3A5WSMq858AzskWmpb9g2Q_dVu5gIlZ6SnS3PUsmojoSP4ZH2p7_eeFd7snJ8-WJlX1wZJromZg8wnYVfz-CjbfqlWpfcCXejNVlusRPqj6O_2nPTfBskWLnRViwYDeyhG78GfMnF1ZGkVzCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بابک زنجانی از برنامه جدیدش به نام مای دات رو نمایی کرد و برای تبلیغات نوشت:
اینستاگرام پولی میشه ولی برنامه ما رایگانه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65010" target="_blank">📅 13:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65009">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
⭕️
ایران با صدور اطلاعیه‌ای، پرواز در بخش غربی حریم هوایی خود را تا صبح دوشنبه ممنوع اعلام کرد.  @News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65009" target="_blank">📅 03:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65008">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
⭕️
ایران با صدور اطلاعیه‌ای، پرواز در بخش غربی حریم هوایی خود را تا صبح دوشنبه ممنوع اعلام کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65008" target="_blank">📅 01:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65007">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">واقعاً خوشبحال جمهوری اسلامی که با چنین اپوزیسیون احمقی طرفه، نه تنها پادشاهی خواهان با [به اصطلاح] دموکراسی خواهان دائما درگیر هستند، حالا خبر رسیده که علی کریمی و شاهین نجفی از داخل گروه پادشاهی‌خواهان هم باهم بشدت درگیر شدند
!
شما با این وضعین می‌خواین در مقابل آخوند بجنگید؟ جای تاسف داره واقعاً، حیف مردمی که گوش به پست و توییت های شما بودند و هستند!
#hjAly</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65007" target="_blank">📅 22:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65006">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ec1cebe91.mp4?token=Xvrrn5GAc9zxg86JvVFGw0iLfrMabN8W4dceBwBe1xyQjBg6hDYBYVCb24wkPSB7lXqjaMHj7UeWieyAHFQuLag2ZzKR-lBcgUOeL-aP-MnWPdrXJLQykw39B63KCCYOz39GDBWWqOf8y-RE-4dAgTk3T8uHwYSoUS9TYFQtaL9RhawiQFISiIqNO6LPSvFmCUY9YAzucXVx3kbSMg_RvPqzehkxVdVtRG_LsD490bT_4hhHz7GLH3R5THvDPfvhMXeHlrYKBxR6Oj8XOB4LE0dZ6orm4Uv5QjfOiesZAOGUJ5IQiDTn8NViWbH0brfzxoZZfI3E7QbRRuDBd41c1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ec1cebe91.mp4?token=Xvrrn5GAc9zxg86JvVFGw0iLfrMabN8W4dceBwBe1xyQjBg6hDYBYVCb24wkPSB7lXqjaMHj7UeWieyAHFQuLag2ZzKR-lBcgUOeL-aP-MnWPdrXJLQykw39B63KCCYOz39GDBWWqOf8y-RE-4dAgTk3T8uHwYSoUS9TYFQtaL9RhawiQFISiIqNO6LPSvFmCUY9YAzucXVx3kbSMg_RvPqzehkxVdVtRG_LsD490bT_4hhHz7GLH3R5THvDPfvhMXeHlrYKBxR6Oj8XOB4LE0dZ6orm4Uv5QjfOiesZAOGUJ5IQiDTn8NViWbH0brfzxoZZfI3E7QbRRuDBd41c1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امتحانات نهایی پایه یازدهم و دوازدهم تو بازه ۱۵ تا ۲۰ تیر به‌صورت حضوری برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65006" target="_blank">📅 22:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65005">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🎙
خبرنگار: آیا در عروسی پسرتان شرکت می‌کنید؟
🇺🇸
ترامپ: او دوست دارد من بروم. من سعی خواهم کرد. گفتم این زمان مناسبی برای من نیست. من یک مسئله به نام ایران و مسائل دیگر دارم. او شخصی است که مدت‌هاست می‌شناسمش.  @News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65005" target="_blank">📅 21:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65004">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
العربی‌الجدید: سفر عاصم منیر به تهران دلیلی بر توافق نیست و پیام جدیدی منتقل نکرده است، گزارش‌ها درمورد مفاد توافق گمانه‌زنی است و اختلاف بین طرفین هنوز زیاد است.  @News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65004" target="_blank">📅 21:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65003">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
📰
العربی‌الجدید به نقل از یک منبع نزدیک به مذاکرات:  سفر فرمانده ارتش پاکستان، عاصم منیر، به تهران به معنای این نیست که توافق در دسترس است. گزارش‌ها درباره وجود پیش‌نویس احتمالی توافق صحت ندارد و صرفاً گمانه‌زنی‌های رسانه‌ای است. وزیر کشور پاکستان پیام جدیدی…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65003" target="_blank">📅 21:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65002">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
📰
العربیه: طبق منابع العربیه، انتظار می‌رود پیش‌نویس نهایی یک توافق احتمالی میان ایالات متحده و ایران که توسط پاکستان میانجی‌گری شده است. که ممکن است ظرف چند ساعت اعلام شود.  شرایط کلیدی آن عبارتند از: آتش‌بس فوری، جامع و بدون قید و شرط در تمام جبهه‌ها، از…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65002" target="_blank">📅 21:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65001">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خبرگزاری های حکومتی: عاصم منیر وارد تهران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65001" target="_blank">📅 19:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65000">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2227480c5d.mp4?token=qMWrET3Vs4HXR4YcdiP2_FldyeXQH8yVZDvfze5hgi7fYg-euPAsCBUHeWoG9TqyFLN-CgqPl6iuHlrl7xEFU-KbGxxPKLwPVycYsHhIHKaEgiDWy0wlAQloYbuNpOQPbh3_uNNNdk9uoAGz2x9lw4d9OjqVOf0cII6tOSorXC4ts3p0xwpQlSt1TAgioxUyeZWXgvT1JsccvU0khVBY5NQ5Cawnn-8MJT7YS5INCuULcwGLKfm2CkczqN1l8tkSv_QlwhoFYUbu5kGTXhI2_UJNo-xi4R2PIB4UoF9NosS4ZV9NqscoktXlCN39wnVEMkN7v2I12mtfIgNPUcK1nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2227480c5d.mp4?token=qMWrET3Vs4HXR4YcdiP2_FldyeXQH8yVZDvfze5hgi7fYg-euPAsCBUHeWoG9TqyFLN-CgqPl6iuHlrl7xEFU-KbGxxPKLwPVycYsHhIHKaEgiDWy0wlAQloYbuNpOQPbh3_uNNNdk9uoAGz2x9lw4d9OjqVOf0cII6tOSorXC4ts3p0xwpQlSt1TAgioxUyeZWXgvT1JsccvU0khVBY5NQ5Cawnn-8MJT7YS5INCuULcwGLKfm2CkczqN1l8tkSv_QlwhoFYUbu5kGTXhI2_UJNo-xi4R2PIB4UoF9NosS4ZV9NqscoktXlCN39wnVEMkN7v2I12mtfIgNPUcK1nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو:
ما باید شروع کنیم به فکر کردن درباره کاری که اگر چند هفته دیگر ایران تصمیم بگیرد، «ما اهمیتی نمی‌دهیم؛ ما تنگه‌ها را بسته نگه می‌داریم؛ هر کشتی که به ما گوش ندهد یا به ما پول ندهد را غرق می‌کنیم» چه باید بکنیم — آن وقت کسی باید کاری در این باره انجام دهد.
امروز این نکته را مطرح کردم؛ خیلی‌ها سر تکان دادند؛ خیلی‌ها بعد از آن نزد من آمدند و آن را تأیید کردند، اما امروز خبری برای شما نداریم که چیزی در حال وقوع باشد.
باید پلن B داشته باشیم برای اینکه اگر کسی شروع به تیراندازی کرد و چطور تنگه‌ها را باز کنیم، و من امروز این نکته را مطرح کردم. نمی‌دانم که آیا این لزوماً مأموریت ناتو خواهد بود، اما قطعاً کشورهایی از ناتو می‌توانند در آن مشارکت کنند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65000" target="_blank">📅 18:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64999">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoAdmin</strong></div>
<div class="tg-text">⚠️
مدت این آفر 3 روز هست
⚠️
💎
پلن حرفه ای
1 گیگ : 280,000 ت
5 گیگ : 1,150,000ت
10 گیگ : 2,050,000ت
20 گیگ : 3,900,000ت
40 گیگ : 6,900,000ت
💎
پلن اقتصادی
5 گیگ : 850,000ت
10 گیگ : 1,600,000ت
20 گیگ : 2,800,000ت
40 گیگ : 5,100,000ت
🟢
کد تخفیف به صورت خودکار روی ربات فعال هست و نیاز به وارد کردن چیزی نیست
✈️
آیدی ربات جهت خرید :
@AmoAdmins_bot</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/news_hut/64999" target="_blank">📅 18:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64998">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqWJH753o5zygQVbJsjJV-ohq-l-nzdS1_kf0aDbaki7Ku-z9DmzStVTQDafz1LHrRf91r4r2TD4XGSCb6CFflTXUGoxsdvFzA2mhBSwlE1SAY_4k8wv9msZGZvS-oIfL3m9VvcKrCrbOpUnnFoUyC495pGVrvpN_o4tzgl3-FyPxc0z230HB9wnfrBRL8Oc_YMjin69a7cT30XFriH-qQf7eFMY1rfZ2zkFNapSDKSohiI4ID-CJptxLk_HZEengvQX2Pux1XPeG7L7QI91y9uDea-h0VLiN06Umkwf272VWoHwbkhte9f-_WeEzDAYmbEM1RPaFDYRtEDiajSduw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
لارنس نورمن، خبرنگار وال استریت ژورنال: یه منبع میگه هر چیزی درباره پیش‌نویس توافقی که داره می‌چرخه، دروغه و صحت نداره!
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64998" target="_blank">📅 18:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64997">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
📰
رویترز: یک تیم مذاکره‌کننده قطری امروز به تهران آمده است با هماهنگی ایالات متحده برای کمک به پیشبرد تلاش‌ها به سوی توافقی برای پایان دادن به جنگ با ایران و حل مسائل باقی‌مانده.  @HutNewsPlus</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64997" target="_blank">📅 17:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64996">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGGyFEs3vNGsX4zwCcYTyW9lhgeglb9CIvhpSOrVwp_PhWENVm9CGH8kob7CyOQkmdEWmjs7Wc73Ee0PDym0LUHM7qKe4JnnGN2Uq6DHeixNiCYykPrLhaKBmHzxfDljnxsGo77m-fBVOzbnSzL59ESn05P2NSPXUJcE_p5Ra7rfcBL7LBzKE2A72M8ke1B0rs4WosPKpqg2ScfHDc0uyedTgQQF0dcoEiILwe9-mt8SQ3bxuSwpa84hvRJ77w1h_1fhLIUYdDP8LFzYUEBc9uY5gC7R7PrQsp_Q_9v2PTxL_W-wubfuY5vaymKh59Kp8iNaQhY3B8FJ9xGxWtewVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو هواپیما دولتی پاکستان راهی ایران شدند؛
احتمالا عاصم منیر در راه تهرانه
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64996" target="_blank">📅 16:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64995">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t67EzfYoHunbeR-g2uwqtMG7x_L7LBG92JlNCjwhISnPCkctq_ulC5NACe32KBMUqIyWP2xLk1TCLL3Sc36BmJ2r9Ce5VmqH4XrUNtydN8Y2qZ3DALMoHDoX1L6CTh16WqJ5mfmk-cPUFGJGcsDfb1w-J1EKfVxP34paQKGfGaFzC6itqLQOCPSwOC17hGbxhj366cl_DvXXrpuOqAqASXTqfjoixp2UQjTsZ81DZHrmMWSSZpl0YXl0DnF2ND5zDURgUDzeVd5uhbkM4MtwheDAUYqVACH6mA5SwbSbGg9n28x2OSzt_2qtk7DJxAjiVxFXKUi-0hy-1Lu15Dh0YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یزدی‌خواه، نایب‌رئیس کمیسیون فرهنگی مجلس: نهادهای بالادستی به این نتیجه رسیدن که بازگشایی اینترنت به صلاح همه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64995" target="_blank">📅 14:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64994">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سپاه: تو ۲۴ ساعت گذشته به ۳۵ کشتی اجازه ورود و خروج از تنگه هرمز رو دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64994" target="_blank">📅 14:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64993">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
سفرِ «عاصم منیر»، فرمانده ارتش پاکستان به تعویق افتاد، این یعنی هنوز اختلافات ایران و آمریکا حل نشده
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/64993" target="_blank">📅 23:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64992">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3890f54566.mp4?token=P8N-Kgk6tGlLQMfBOPRFA7jMA0JomnzwaRSwkRPgwJ2TllXs55shV3j9JWXVwn-PISD1aNN6aWVeLOQHMp97wfXqxlP4qOr81zbjOx-SdbJatKgpLtxKH411oWGlY9lha7JtjBaxCaCEEVWax6EFREftNBJevlMfgSMeRnzZhiV6O-Z6Af5_UCEPZycbqBblIzeo-WsOgaNzk0yAuLeSX9xx9PKOKIsYstYedGTetDTz6_Y7seBDHX3Eidq4nW1E69R-wIaIKPu_sAz6Y_078EALfydV-ZGYnaO2g0sskwStTuJA0ru5cZZ8L7R7WXysb0XjuIrbG1B7F2JS2KZsBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3890f54566.mp4?token=P8N-Kgk6tGlLQMfBOPRFA7jMA0JomnzwaRSwkRPgwJ2TllXs55shV3j9JWXVwn-PISD1aNN6aWVeLOQHMp97wfXqxlP4qOr81zbjOx-SdbJatKgpLtxKH411oWGlY9lha7JtjBaxCaCEEVWax6EFREftNBJevlMfgSMeRnzZhiV6O-Z6Af5_UCEPZycbqBblIzeo-WsOgaNzk0yAuLeSX9xx9PKOKIsYstYedGTetDTz6_Y7seBDHX3Eidq4nW1E69R-wIaIKPu_sAz6Y_078EALfydV-ZGYnaO2g0sskwStTuJA0ru5cZZ8L7R7WXysb0XjuIrbG1B7F2JS2KZsBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: آیا در عروسی پسرتان شرکت می‌کنید؟
🇺🇸
ترامپ: او دوست دارد من بروم. من سعی خواهم کرد. گفتم این زمان مناسبی برای من نیست. من یک مسئله به نام ایران و مسائل دیگر دارم. او شخصی است که مدت‌هاست می‌شناسمش.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/64992" target="_blank">📅 22:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64991">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43db173db6.mp4?token=sk-4DtrYTpq5Syvyzc9_qUn-QX4kKZEFhe8Sdpiao4KOk8723_t5QQPgHQbiyWks457qSG3G9Ksmg9apGfcRGRekgjLaIo8yLKuDG4nG0iEUf2yAAIOLGHVv7cmIRUEAbT9kIV6mKAoNRn5mQ95qW3jXS03II2MWGhmKDpAq9dqzYV5oSuTjRA_Hdu0x8SD9DAZDqYWBSN89xUc-P01FR2bRwOaXEBytEC0Ek9gX3VQyGQoWxPcOBNbdK9lNs2BJLsqG1ePtOM9RWY2qjSX6pmN2rtUYwZ391XKwbQROCR3VpTVFzaOKy5JYmg8c8sKwFxEljZUf0KcKjcKAylSZUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43db173db6.mp4?token=sk-4DtrYTpq5Syvyzc9_qUn-QX4kKZEFhe8Sdpiao4KOk8723_t5QQPgHQbiyWks457qSG3G9Ksmg9apGfcRGRekgjLaIo8yLKuDG4nG0iEUf2yAAIOLGHVv7cmIRUEAbT9kIV6mKAoNRn5mQ95qW3jXS03II2MWGhmKDpAq9dqzYV5oSuTjRA_Hdu0x8SD9DAZDqYWBSN89xUc-P01FR2bRwOaXEBytEC0Ek9gX3VQyGQoWxPcOBNbdK9lNs2BJLsqG1ePtOM9RWY2qjSX6pmN2rtUYwZ391XKwbQROCR3VpTVFzaOKy5JYmg8c8sKwFxEljZUf0KcKjcKAylSZUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🚨
ترامپ:
ایران نمی‌تواند اورانیوم غنی‌شده خود را نگه دارد. به محض اینکه آن را به دست آوریم، احتمالاً آن را نابود خواهیم کرد. ما آن را نمی‌خواهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64991" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64990">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZEbH_Px62LFsdASIDan5lslbLWxGCADHkkLJJZ-gdyLIa1GpNmjEOnWda2YD1ARZNOoXJAsVsjiEQNZtD91MAueoyIpdQoKeRMuYerfjgnNlRq4vEUDjgBOkDRIcD4qigy0KmW_1k2fNkG--MNtHoL7QAmCU-fPb9K8-ZSxy_XtvQW_7nSZ_CJWgCs-GthgjV0MhHdRJq02YqEYyhHEdxGWjLkjmVgfpvE_VYcSY3fNZFK0_B9C_R3MqMqxzFTRuNyDwY_kS1FWzAdNBxA9WZc3NzH8ZSM3yKnFYAiHRAhH_2S19n58TJu1ZOzwenjUcCEdZ5YV2eKNNkp5ZU_Ltw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ یه پست از نشریه نیویورک پست بازنشر کرد که تیتر خبری‌ش هست؛«چطور میشه تهرانو تو سه حرکت نابود کرد»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64990" target="_blank">📅 16:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64989">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYwlf9jScqTxUj3bHcLHcMYOePwS1pjeN5TZVde1lr4R4c6B8c6Uhc_NTF6Udal_duXBINzYKcxgVNRRr6ALahPKqNE_ZjGXwNUhrRPkR1yZrroLShmQMvYwgFQdXSaaqR3AZ9Rukj7qv43n3DFhvXbZMZkJXWt6Cu2H80g8bR2WVKQfMhcQb5_OyYj2pJeNRaaBvzgF1in3teUdEGlj-72M-7-Q-0Ji6CbNKR5bqH7LcFi6QT445oHA1hbPzFrLVPNZwzz6adu8tVR1kKBuoRG7TQ8Vy8AjLsADyvIV3paWKp-y3ULCWwWJzJtg4Av6xztSje_2iuFOkogowZVEVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ جدید هزینه‌ ریجستری گوشی‌های آیفون
ریجستری آیفون ۱۷پرومکس، ۱۰۴ میلیون تومان!!!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64989" target="_blank">📅 15:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64988">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM1wuNKvTnleZSEDksL2p7yQqjpAryTDIyjR7G8miA4QyrBYx6n8TrfHQc_xVAxqVEt91NwNTz-6rua32eqLBT7XgjJYBWqsRi6Oxj9LplSPlXyuKUPhcycgQ-nA97K7jFpugErOpdJW4KCMuyXCuS3wqJfIvVV3xHugQKl1om2fxavePCkidrASGiVczze1xYAjJTX5ui1AldnGS6bU0-HxuGuHh2fqpXYetxIVKhad-Gb30kGfLLu1VyY8BTIt3kpNHVQRgxs-XN0Mb-L5jwQRmI7NbMtSQFKRGwC8Ma40kJn9mGp3JdFbkk8zLNXdGm25w03lNHeTGJUILLs5LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فهرست کاخ سفید از مهم‌ترین دشمنان امریکا که در دوره فعلی ترامپ حذف یا دستگیر شدند:
رئیس‌جمهور ونزوئلا - مادورو
رهبر رژیم جمهوری اسلامی- خامنه‌ای
معاون رهبر داعش - ابو بلال المنوکی
و برای رائول کاسترو رئیس‌جمهور سابق کوبا (و برادر فیدل کاسترو) کیفرخواست صادر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64988" target="_blank">📅 15:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64987">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
📰
رویترز: منابع ایرانی می‌گویند رهبر معظم(مجتبی)اعلام کرده است که اورانیوم غنی‌شده باید در ایران بماند.  آمریکا می‌خواهد اورانیوم بسیار غنی‌شده ایران به خارج فرستاده شود مقامات اسرائیلی می‌گویند ترامپ به اسرائیل گفته است که این اتفاق خواهد افتاد دستور رهبر…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64987" target="_blank">📅 14:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64986">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
بندرعباس ۴.۶ ریشتر زلزله شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64986" target="_blank">📅 13:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64985">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/miP6JPhibw70dQi0-t904GgC0ZmSPSsSbhU1FaHSyYqke6attLi32NB55BDOLvalI8T0KAw6e47Qu-EzkM9FKbwdxAeMVOAFCLlh-xUZuS4Uk-g77bOoV3En_93-HT1bugpBwYypPAG5xJTGIn4F-o5MtBqaffBMmm4xQQKmAIJYY0x4kTCvzyG9IUMAvPv0VqrViUduw7-z79rkOLctOsV2m7eykbZ8BJjJg6P_7OxltTVWI5xkuvuFDZMpzFcGGkbEDaAAF7JYIN4NYNw8i_lcCGRYT8X4U5mt8FTzZszDyB8q2eMtqZdVjitNCcWlKnIB0qB3p1y6U8E-LHSx3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شریعتمداری: تا زمان شکست امریکا و کشتن ترامپ تنگه رو باید ببندیم
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/64985" target="_blank">📅 11:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64984">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: اگر فرمانده ارتش پاکستان به ایران سفر نکند، توافق نهایی ممکن است ظرف چند ساعت اعلام شود  @News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/64984" target="_blank">📅 10:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64983">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرنگار: آقای رئیس جمهور خیلی از خانواده ها در آمریکا نگران گسترش هوش مصنوعی هستند، نظرتون چیه؟
ترامپ: هوش مصنوعی عالیه، ایران نباید سلاح هسته‌ای داشته باشه :)))))
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/64983" target="_blank">📅 04:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64982">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: کار برای نهایی کردن متن توافق میان واشینگتن و تهران به طور جدی در حال انجام است و دور بعدی مذاکرات پس از حج در اسلام‌آباد برگزار می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/64982" target="_blank">📅 18:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64981">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: کار برای نهایی کردن متن توافق میان واشینگتن و تهران به طور جدی در حال انجام است و دور بعدی مذاکرات پس از حج در اسلام‌آباد برگزار می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/64981" target="_blank">📅 18:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64980">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F5TyuiRbE-DPcACL4YgpyaZ8ebJn7KziDQKzEc4TdInyIwwwBe2tDrwXh7z7MOf7DcDDHVUsP-XaSz4-CUQwUD4VBE5LSLeV2-ztFr4CkOsDoqO_htlgqICiEcXf9Y8DQ08RdxDaXvmGtcM0g97Zq2IjeulBSw7FxFRvH6nz8o_YMXceCMlBUkNI64SmAJKPt-4WScsmWg_MHEFVRdN-1yJKT1QQCxnBWI1kIO3xv7qMvYz8tCng-FZbDco8Miprf6JjBMUDu-2gv2WGDuK9_FwEPzRxZwCONEH9Fz1LhRSnPWgsm3o-4nqmBniyy5jmKWj2jZdYlKlM8QMhBHJtPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای مرضیه حسینی خبرنگار ایرانی کنگره: یک منبع مطلع اینجا در کنگره به من گفت که ترامپ روزهای چهارشنبه یا پنج شنبه پیش رو، به ایران حمله خواهد کرد.
به گفته این فرد، این حملات برای یک عملیات “دو تا سه روز” متمرکز خواهد بود و به مراکزی با هدف بازگشایی تنگه هرمز انجام خواهد شد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/64980" target="_blank">📅 13:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64978">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2VyIGn1twsC7rSymGnrFINo1HFnom2BuQTRzBUsy0QZkNeK8MSt5CFVy4hN5F8hBKHFu-CHRTxiNQynG5gkzLz0VUKk5pfEJokyrNTWQfVkfv_PTR450zXVirC8BulG0PCkckxzBbiiIdHfkh1WOwd-zR7ii_-w__j0fDwUWa6bqQnJdm9wjLEvWenP0yLOKtbnmP8brg0VFYSa2Q-A2t6hWHRHV-QTWfW4KMCzRnODN_hqMVTC4bWRa4pXFiSA2ld8TB__-YesghgWo2AiMKmabASt0Rzynhq1Gb4y_E_YABWbyeXwmoV4M1r6xzBkC1qLSNCrfZAq6UsPFQoUZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iqyr9x375H4J16Wx2Whfr0RQ4MjaN3k5DXVZs8PlRseuZPoJHOrKZoOjHlntm0qKAMA-x9b28a77l0PS3WI4OvZY2INts133Is0DcYULbUGmUwnJxwQk7UaRYvykUTxYJK2TQXOWMNBZ2NIm-RTd0iJVaZekpeUJOTRXKgsufJO2UG-sWUFjrdl6Ef_9rstCWOrzUmJBxF1FsYJg58ivdvjjUemlEypC0XXJHaCmJpcJFspr-xeJI_0DX3t8np42a5cOovW0XEiHlgnrvN5SqaSTV1PLr8hu91aTGQ8eUSB6PEpplEO9ozjKq2RV38bl0_NTKkFfXRCU-5GcbXCqWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
گزارش NBC از موبایل جدید ترامپ  به نام «Trump mobile»:
مدل T1 با قیمت «تشویقی» ۴۹۹ دلار به فروش می‌رسد و به صفحه‌نمایش ۶.۷۸ اینچی، دوربین اصلی ۵۰ مگاپیکسلی و حافظه ۵۱۲ گیگابایتی مجهز است.
گوشی ترامپ موبایل در چهار نقطه از بدنه و نرم‌افزار، لوگوی «ترامپ» حک شده، پرچمی آمریکایی با ۱۱ راه‌راه به جای ۱۳ راه‌راه روی آن حک شده و از پیش، شبکهٔ «تروث سوشال» روی آن نصب است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64978" target="_blank">📅 13:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64977">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358ed734a6.mp4?token=X6WeprPOpfHNLUaDYEWh83iVu5PD4ijqAh1JR41jZ83W2JnmVDUUoFIRf-M9bNarI51iF34LcR1Xi33DDFanhihIvT33Hm5ZL7k5GS2V6eg_piZ0qh2LS4tgQOTO6Of72mugHQsPidYXlh5ajsTXDsCip2sKJhR7aO6tZHKiaXP-RDEOfgSiRT13ZQNycSFrPnS3ij1BTLDlTJgB0qYq7jbdNMJuPDJ2LcM9zegT40YR3q3ETV7kpN53HHmN5fiLwOHymiJNmqvu_VqtTt2vYAiY8TgX1F9t8oLgSgtc1VvabpPRYKWXCDQ8kxHwc6P-4NqIOq3ztBcvF2aq8n8OXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358ed734a6.mp4?token=X6WeprPOpfHNLUaDYEWh83iVu5PD4ijqAh1JR41jZ83W2JnmVDUUoFIRf-M9bNarI51iF34LcR1Xi33DDFanhihIvT33Hm5ZL7k5GS2V6eg_piZ0qh2LS4tgQOTO6Of72mugHQsPidYXlh5ajsTXDsCip2sKJhR7aO6tZHKiaXP-RDEOfgSiRT13ZQNycSFrPnS3ij1BTLDlTJgB0qYq7jbdNMJuPDJ2LcM9zegT40YR3q3ETV7kpN53HHmN5fiLwOHymiJNmqvu_VqtTt2vYAiY8TgX1F9t8oLgSgtc1VvabpPRYKWXCDQ8kxHwc6P-4NqIOq3ztBcvF2aq8n8OXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خضریان،عضو کمیسیون امنیت ملی مجلس:
امیدوارم خبر سفر عراقچی به نیویورک برای مذاکره در خصوص تنگه هرمز دروغ باشد!
چرا ما در خصوص موضوع تنگه هرمز باید در خاک اسرائیل و آمریکا مذاکره کنیم؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/64977" target="_blank">📅 10:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64976">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
📰
نیویورک تایمز:  ایالات متحده و اسرائیل پیش از جنگ با ایران، طرحی را برای نصب محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، به عنوان رهبر جدید کشور مورد بحث قرار دادند. احمدی‌نژاد گزارشا در مورد این طرح مشورت شده بود، اما پس از اینکه در حمله‌ای اسرائیلی به خانه‌اش…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64976" target="_blank">📅 09:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64975">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دموکرات های احمق برای بار nام خواستن جنگ رو متوقف کنن که بازهم رای نیاوردن  @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/64975" target="_blank">📅 08:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64974">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9FWGp7hSq8K9U6qiq-pYXV70GOqhC3dAwglhZ7NpC_OqO6qgm2Rr7mIUDtcMPr8CPVQWaP9g-TkIJpCP-2UB7g69r34E-jrJm6BXzYISqWQZ_G2-eoCelRsOGZei_7-Mr94TNwpbXTG0LzaOzL5ctan6KB1GjEiy9stshgXS9fFRBkR5Bskxpq-IjrK6yogasgYEgdTwPaukA91YKQxWCcF8WcArj_bbg8WMaV2l8mivuf7LNNA1DVtmxgSk76692zdjT01XRB6q8kVECxixclXqLw_AM4TgRPsbRLYrPezVhFyJQ2LT3K9DXQaAgFb9itakvWg1S4sILjkS6BR2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور لیندسی گراهام:
امیدوارم و انتظار هم دارم بعد از این چند ماه مذاکره با ایرانی‌ها، دولت ترامپ هر تلاشی رو که برای دوباره کش دادن مذاکراته رد کنه.
این رژیم ماه‌ها وقت داشت به توافق برسه، ولی به نظرم واضحه دارن بازی درمیارن
من ترجیح خودم راه‌حل دیپلماتیک هست، ولی قدیمی‌ترین ترفند ایران همیشه این بوده؛ امروز و فردا کردن، کش دادن، کش دادن، کش دادن
در مورد هر توافقی هم، منتظرم بره سنا و اونجا بررسیش کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64974" target="_blank">📅 07:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64973">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prR6MYFlXqCEozlnn82if1CvUJF0mYZBXTK1urE4ThiYgj28Qshsf8WWMkkFxNyiwwpG1VXaGEOPuo6lihQeT-6Ju4g8ybKpzlu7NIBRmSjNJo-rtO7ntB0BGwboXGTDoQTX55cw-2UpIBNiMt121zqvaVId0w8LvAPoIpSUDqVMSxaeiwwmLv6oxHRiHOufqDZS6xnQmdcGFJkOnimVw9HpYcN7vT7Xd_IYtsEw5jb5bfo1ByO0TThH0OtRR6gOWfDB692naoJPQ1O1ud_FUCkQ4b1IKRfL9A-xQhOYeuXBFm5AJoq-yvaA9iFDfaFLhHgxg_IZT5fVMRvc1AjR7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غریب‌آبادی، معاون وزیر امورخارجه:
امریکا میگه دستور حمله رو به طور موقت لغو کرده و در سایه تهدید می‌خواد مذاکره کنه
اونا باید اینو بدونن برای ما، تسلیم معنایی ندارد؛ یا پیروز می‌شویم یا شهید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64973" target="_blank">📅 00:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64972">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🇺🇸
اولین اظهار نظر متفاوت امریکا نسبت به حمله انجام شده به مدرسه میناب و جان باختن کودکان این مدرسه:  برد کوپر، فرمانده سنتکام: ایالات متحده عمدا به غیرنظامیان حمله نمی‌کند. مردم ایران دشمن ما نیستند. سپاه پاسداران انقلاب اسلامی در این مورد دشمن است. تحقیقات…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64972" target="_blank">📅 23:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64971">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b854a8a43b.mp4?token=ATuFh_9bqlkH8kqXojnqZYtejnPvkym-ZdYEuQQdghYgkjXcVcA7rF-rpm4RTTAw0xf_Hn4bfvdTdqxOKBVcsiJRb5pEO_SS7N_gXpLpABZVT9CiCdUSoP-dNA7-gkuQpkAJ16ujO9TKPCApv6Fyk4Ww8i3ZtBBh6vjzFVL42AiyahjgfA2UNDiJCy49PAfQ4OAUHz7TgBn0DR5ygW2_x3jUVNWAZmrVe1aYRnu2JlILONzfPLHZ6mV15k9AC3kJXWg_EZiFG21uCTcKeJRegXUF5E3CFr8zXZ_Z0ZSRnPmKtRpSkQ9rJClpyIxhsw_eoTb9QP-h4sf2Ym1Sp_EAOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b854a8a43b.mp4?token=ATuFh_9bqlkH8kqXojnqZYtejnPvkym-ZdYEuQQdghYgkjXcVcA7rF-rpm4RTTAw0xf_Hn4bfvdTdqxOKBVcsiJRb5pEO_SS7N_gXpLpABZVT9CiCdUSoP-dNA7-gkuQpkAJ16ujO9TKPCApv6Fyk4Ww8i3ZtBBh6vjzFVL42AiyahjgfA2UNDiJCy49PAfQ4OAUHz7TgBn0DR5ygW2_x3jUVNWAZmrVe1aYRnu2JlILONzfPLHZ6mV15k9AC3kJXWg_EZiFG21uCTcKeJRegXUF5E3CFr8zXZ_Z0ZSRnPmKtRpSkQ9rJClpyIxhsw_eoTb9QP-h4sf2Ym1Sp_EAOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جی‌دی ونس، معاون رئیس جمهوری ترامپ:
گاهی اوقات کاملاً مشخص نیست که موضع مذاکره‌ای تیم ایرانی چیست.
گاهی اوقات سخت است دقیقاً بفهمیم ایرانی‌ها می‌خواهند از مذاکرات چه چیزی به دست آورند.
در حال حاضر برنامه‌ای برای تصاحب اورانیوم غنی‌شده ایران توسط روسیه نداریم. این هرگز برنامه ما نبوده است.
نمی‌دانم گزارش‌ها درباره این موضوع از کجا آمده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64971" target="_blank">📅 23:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64970">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoAdmin</strong></div>
<div class="tg-text">⚠️
مدت این آفر 3 روز هست
⚠️
💎
پلن حرفه ای
1 گیگ : 280,000 ت
5 گیگ : 1,150,000ت
10 گیگ : 2,050,000ت
20 گیگ : 3,900,000ت
40 گیگ : 6,900,000ت
💎
پلن اقتصادی
5 گیگ : 850,000ت
10 گیگ : 1,600,000ت
20 گیگ : 2,800,000ت
40 گیگ : 5,100,000ت
🟢
کد تخفیف به صورت خودکار روی ربات فعال هست و نیاز به وارد کردن چیزی نیست
✈️
آیدی ربات جهت خرید :
@AmoAdmins_bot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64970" target="_blank">📅 23:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64969">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=B_1oOfL3GJO839b1UTWRr-0x5HZR-vSdW2bR39HSoAdKOitZos3HRzaJDObLvSlvTJRkUE2IF5Si3XGd-L-H6uAd7d-UGm-tK2Pl8FJ8J16NtmvfwxAlt4sujteTVt6XnbUxt_dqfFsXrnnQaGsQKG4xsgvpx8MZHDawzH1tJyuhS7nedtgM2K3sFM4W7otI9wDOJS5dNt1y4cv7o4rzTll-9_0om1MFiUVl2CSDEGbG4tj_IMz4Mlb1y1qOcQfLZRZx6ydiMS3WNgBlmVb5n0JdCzy7Lck_o23N5qQfIPeY_ZemVky58cjGNjUewNKC99NryafH_o9g5tTTU__Ygw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e8365c27.mp4?token=B_1oOfL3GJO839b1UTWRr-0x5HZR-vSdW2bR39HSoAdKOitZos3HRzaJDObLvSlvTJRkUE2IF5Si3XGd-L-H6uAd7d-UGm-tK2Pl8FJ8J16NtmvfwxAlt4sujteTVt6XnbUxt_dqfFsXrnnQaGsQKG4xsgvpx8MZHDawzH1tJyuhS7nedtgM2K3sFM4W7otI9wDOJS5dNt1y4cv7o4rzTll-9_0om1MFiUVl2CSDEGbG4tj_IMz4Mlb1y1qOcQfLZRZx6ydiMS3WNgBlmVb5n0JdCzy7Lck_o23N5qQfIPeY_ZemVky58cjGNjUewNKC99NryafH_o9g5tTTU__Ygw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره اینکه ایران چقدر وقت داره تا توافق کنه:
دو یا سه روز. شاید جمعه، شنبه، یکشنبه. شاید اوایل هفته آینده. یک بازه زمانی محدود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64969" target="_blank">📅 18:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64968">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2efb45471e.mp4?token=fRRByHzE_s-Aj0ydZwH0pcg8oi_R047UuvCy778M_n0IntOAX2LJSRMCtdGo2rHkouyuM73EUngtTl4LXytAvlidcshuVghx6cVbaJu89tUgrOfA2Qv9Iaq6Z947cQGxcUtEhF8Tcdx4ZP-RKdgUA1Ym3NaFMoOhTlapqyFOL_uKww_T3sfpiGZflTxL3gl4xKPpe7PqfOmDERUfdI9Az6G4fKg2V18RH694m14ZcBo_7gFnFIWCmAoTV2vIZCJHyNidjqg-6X1j37HPwikGX3drZ5ziDTnvsfznh4DGX9JavaTiUcfPrdx8r4WDqoS5uQ1q0DJvxH38oTvC-9IDGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2efb45471e.mp4?token=fRRByHzE_s-Aj0ydZwH0pcg8oi_R047UuvCy778M_n0IntOAX2LJSRMCtdGo2rHkouyuM73EUngtTl4LXytAvlidcshuVghx6cVbaJu89tUgrOfA2Qv9Iaq6Z947cQGxcUtEhF8Tcdx4ZP-RKdgUA1Ym3NaFMoOhTlapqyFOL_uKww_T3sfpiGZflTxL3gl4xKPpe7PqfOmDERUfdI9Az6G4fKg2V18RH694m14ZcBo_7gFnFIWCmAoTV2vIZCJHyNidjqg-6X1j37HPwikGX3drZ5ziDTnvsfznh4DGX9JavaTiUcfPrdx8r4WDqoS5uQ1q0DJvxH38oTvC-9IDGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: دیروز چقدر به حمله به ایران نزدیک بودید؟
🇺🇸
ترامپ: یک ساعت فاصله داشتم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64968" target="_blank">📅 18:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64967">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:  ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم. خیلی زود خواهید فهمید.  @News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64967" target="_blank">📅 18:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64966">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9954bd7931.mp4?token=mh8uNYRMV63lmvRvV5mdtA-Iq8A0g497Zsi75cvAJNQNOFEyW99o1v9pl6nj3nX7l1SShANaxUAepK0_VZULYQ42mQTGRHX4vFXPE5hBSsgr1Js_amrS0NyYjf1TElS8E9is1kpvwM-dlMfuSUpYRRWHHfljzOl-Id1QMaaZvVuhaoMZlSuYUz3ebLrUqs5g_4AT0qgwLpiOJ80V_K0hV4bCQY947Dg7kDRwDY-rqiXHS1JIuLrrGQoKvx9GPOG_l4X6woZSlj3r7JjCxnfK3Z6okvuFL8IyKPf9xGXdTQnUJJirdKqZMaoEJW4rjNKgmgfvfawwbpj3BXcaLXlN0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9954bd7931.mp4?token=mh8uNYRMV63lmvRvV5mdtA-Iq8A0g497Zsi75cvAJNQNOFEyW99o1v9pl6nj3nX7l1SShANaxUAepK0_VZULYQ42mQTGRHX4vFXPE5hBSsgr1Js_amrS0NyYjf1TElS8E9is1kpvwM-dlMfuSUpYRRWHHfljzOl-Id1QMaaZvVuhaoMZlSuYUz3ebLrUqs5g_4AT0qgwLpiOJ80V_K0hV4bCQY947Dg7kDRwDY-rqiXHS1JIuLrrGQoKvx9GPOG_l4X6woZSlj3r7JjCxnfK3Z6okvuFL8IyKPf9xGXdTQnUJJirdKqZMaoEJW4rjNKgmgfvfawwbpj3BXcaLXlN0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم.
خیلی زود خواهید فهمید.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64966" target="_blank">📅 18:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64965">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba90deb154.mp4?token=kAJxfXGF0L-Ep_i5VNbyKMBdPxR1ArcLXb56GQLKsUn1naDQLy2vhj1Z-v5IfyA06gDQiGtr6X0RsTVIOzqMSzO2dPypu_6bEg5XoSov5xDAxTmvQDjDofa0G8VJZKQFDidMdEfoLQN75yTnAiFwSDrBZnitANis2jGUFMQWyg6WNl2YfVy9pIC47rvZ0vB_lFYQmzWd7ajILskwinYKEbsqb_LDDK9Ll2ZKEAR7XTWnCWeJRHXsoDBvv5sU40Efbg_AJIg4cTtVsIqPzDEdHQtgtxRSJPQoEkduuJl683pqhRehbpwn0XCHm-u0LNkzSyVdDKmxJh1xEd4bPc9tlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba90deb154.mp4?token=kAJxfXGF0L-Ep_i5VNbyKMBdPxR1ArcLXb56GQLKsUn1naDQLy2vhj1Z-v5IfyA06gDQiGtr6X0RsTVIOzqMSzO2dPypu_6bEg5XoSov5xDAxTmvQDjDofa0G8VJZKQFDidMdEfoLQN75yTnAiFwSDrBZnitANis2jGUFMQWyg6WNl2YfVy9pIC47rvZ0vB_lFYQmzWd7ajILskwinYKEbsqb_LDDK9Ll2ZKEAR7XTWnCWeJRHXsoDBvv5sU40Efbg_AJIg4cTtVsIqPzDEdHQtgtxRSJPQoEkduuJl683pqhRehbpwn0XCHm-u0LNkzSyVdDKmxJh1xEd4bPc9tlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار طرفدران حکومت تو تجمعات شبانه: مرگ بر امارات!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64965" target="_blank">📅 15:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64964">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
خبرگزاری مهر: صدای انفجار ناشناخته در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64964" target="_blank">📅 14:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64963">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5tuXEVVacpd--QslHk4iRNA2utoq_L_IR_KWDrmPmFQN0Er0ecabiGegjVYIVX2Q28uLYnuZ2o9UFG0fdoXZohnVeyW4N9DLW-yMqYsaUv73W95kodio5Juo7R07DcOPAtmdM6QJsIrDY33f6NSRngPnbC7Dq10wuKu54QFBiAPEqEogopx7H_iIBU3pcsePFR0doA7p8oRHfFZ8izceEM69-mzRRj5hL7Hteq5EALMcCGBDLWy9zPJtKFYDi0TN6xpfLzhywi54QPnixQXt7AKqBQ3bGbn-sCg3YKS7p4fYVYgDbhHUXdjBaixYoS-fzhSy4qRMMwViKsXk2-TzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:   من از طرف امیر قطر، ولیعهد عربستان و رئیس امارات خواسته شدم که حمله‌ای که برای فردا علیه ایران برنامه‌ریزی شده بود رو فعلاً متوقف کنم، چون مذاکرات جدی در جریانه و احتمال یه توافق وجود داره. این توافق به نظرشون می‌تونه شامل این باشه که ایران به…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/64963" target="_blank">📅 01:56 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
