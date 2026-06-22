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
<img src="https://cdn4.telesco.pe/file/t3KQqeGcR1_NBhvsWyql0PxRp4R6cuLImz-ePVi3w5nAE6lI0HTwIzLtLF_xmnkYU_BKmCQv87m9cjyrrGBecsx4f7ZZ1xVEbtjMOEo8QmKbnHCKmAV-DxyR6hnKLGCnhg_F6Fz45jC1LIhjTa0mPdqE96nW64kdmmfWimTLvK5DYvZK2pe2yppFGKxOkSSJRGx_P5usGmfeMejkRYhWAJH9nlCMoO39sxsQrTOoQsvXl_q62ZYqa_AU8XIUe8E5HwzSxQC8EaXd65XErPIxoRnoqVYSvBq5h6SQo_xAv6sKtDwhwliZU9QvSWfATF2sXboDBNixC14FErCt8seHhg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 953K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 10:42:50</div>
<hr>

<div class="tg-post" id="msg-129653">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزیر دفاع آلمان: در نهایت، دونالد ترامپ مشکل بشته شدن تنگه هرمز را ایجاد کرد، نه ما، اما ما در بازکردن دوباره آن ذینفع هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/alonews/129653" target="_blank">📅 10:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129652">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vw7ZgYH9fBQRxRP_CRpI_dX6iuQD9e9Bc5e2r0if4qy1nCkFiaiVtUY-WqYXBJxt4xi35t3YlGKjiqtBi-l5EzQnNPJjbYES5EX55dX8UyH2QxMKsA_mO5fsTM9Ft7gWYOTryWWj_XOwScTYxzSeN3567-SHX5Pho7MQ0DLIB2qJ35MY5ygKmsOk9PTR2HRTMA6dCI5eNtezlvTrzOgOGFcLo1GxHmwy1UxU0c9dU8IvK1TYxWlGumS_afxLlcfjSpyxFbJTlcMMoW9GdsQbBysXbHsNVqI64HF-ShqeeV7bxRxw0q2-XPtQwNkX7VXJfScb0sP2O5gHACEbaMk0dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از مذاکره نخست‌وزیر قطر و ونس معاون رئیس جمهور امریکا در حضور جراد کوشنر داماد و فرستاده ترامپ در حاشیه مذاکرات سوئیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/alonews/129652" target="_blank">📅 10:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129651">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">️
👈
وزیر دفاع آلمان:
ترامپ مقصر بسته شدن تنگه هرمز است
🔴
وزیر دفاع آلمان اعلام کرد که رئیس جمهور آمریکا مسئول بسته شدن تنگه هرمز و باز شدن این تنگه در راستای منافع اروپا است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/alonews/129651" target="_blank">📅 09:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129650">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
تانکر ترکرز:
ایران از پانزدهم ژوئن سال ۲۰۲۶، بالغ بر ۳۶ میلیون بشکه نفت خام صادر کرده است همچنین معادل همین میزان  به صورت محموله‌های شناور در نفتکش‌های مستقر در آب‌های سرزمینی ایران ذخیره شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/129650" target="_blank">📅 09:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129649">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJij6Igu5BqxDwjO9lGVgS_qeUdpLaBgj7YURq08Z_ByF3nSmGR-WV3510wdFA1HgfmxYp3s_cqdK5s8PzotpMkUwB1A0Dcg3lBh_ywXI-UnNj72M4YYXAyS7mziYJHUax9B4qAHUBslmfxy5sSH68QOCFYz6ykvxwSsn4fVphIZr22hK-jIQoS3Gh_V2vupMZTTaamvrfHQCmg1dYXKLCAmomfUKiyxKoBodkvYurQxYJdn8RXtAq1_zpv3-Lf0FthEUugwseiA4iTNRMikXC-y4s4SBcu5hDPAOtc-pIDN-o6HO9LaC3zGrR7nRHUo9h_dORTEyS9sXJEpfAwBHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سدهای کشور چقدر آب دارند؟
🔴
بر اساس آخرین آمار از وضعیت مخازن سدهای مهم کشور، میزان پرشدگی سدهای مهم کشور تا ۳۰ خردادماه، ۶۶ درصد است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/129649" target="_blank">📅 09:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129648">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
اولین تصاویر از دوحه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/alonews/129648" target="_blank">📅 08:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129647">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
شهباز شریف: امیدواریم مذاکرات به سندی منجر شود که صلح و رفاه جهانی را تقویت کند
نخست‌وزیر پاکستان:
🔴
انتظار دارم مذاکرات جاری در سوئیس به میانجیگری اسلام‌آباد و دوحه برای پایان دادن به جنگ آمریکا و ایران، به «نتایج بسیار سازنده‌ای» منتهی شود.
🔴
امیدواریم وقتی به خانه‌هایمان برگردیم، سند فوق‌العاده‌ای در دست داشته باشیم که صلح، پیشرفت و رفاه را در سراسر جهان ارتقا دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/alonews/129647" target="_blank">📅 08:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129646">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
بقائی: اظهارنظر تهدیدامیز امریکا باعث شد ایران حاضر به ادامه نشست چهارجانبه نباشد
🔴
در زمان نشست چهارجانبه اظهارنظر تهدیدامیز امریکا منتشر شد که باعث شد ایران اعلام بکند در چنین شرایطی حاضر به ادامه نشست چهارجانبه نیست.
🔴
قطر و پاکستان تلاش کردند گفتگوها ادامه پیدا کند و ما گفتیم به صورت چهارجانبه نخواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/129646" target="_blank">📅 08:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129645">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvnnVk0jmY4e8-IjAfB19QFvBHw2bWueGXe_hgi8-dd5drUTDFZyJCvwh0iWaOxq-_BVv522wuvOqV0U8cNPndhpcpzy7KjC-Pv2Y5vHeEg5DHFPUQLh9nVBoh91tbymh29JtmroylZCj5nJOmS6zCzgwvmY0jMpv267div8-CO8gWxXP835dVa2cZvHFbokC8Kw6L_qPDuEI5Z8nbn94bRqm3cO91X1BlC0wZvnpZiil1hgw4ymDzLIu3XpNNQl1fj3KsENoYNs9gbyVHnRL8pERruKB4jSa-JP8hf8CdfJlKOoirKKchNcPFKgaRgwINe6d9XfvDBN_pRWe1979g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی:
ایالات متحده، بر اساس تفاهم خود با جمهوری اسلامی ایران، مسئول تجاوزات و اقدامات تحریک‌آمیز رژیم صهیونیستی در لبنان است و باید پاسخگو باشد.
در صورت تهدید علیه ایران، ما آمریکایی‌ها را مسئول خواهیم دانست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/129645" target="_blank">📅 01:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129644">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7ARCX64__7J0Y4I2PIkK4T-z2ZFIi7bLtQSNSVQ5bTpkqiOVphmkNyGaw5jo6vO8hqR6AWYBsHbqxXZ1ngt4h8t5I_lU7fSYYj1hVfatN-Grku2Hn80fMOHWneGigJX5N3LeoRbMompU8AV92fE9MqSQDUyxp2d1acM_ysghIMn01iQ1zGfOI6we5aliom-7zp0WlhjW6GyuAtxCvuYkSC3-zssPZlYyAcx2Fga-84k6Vez3RZHesCnE73YHB7vL2ik7gX8A5luwFaqYuw52jFWK6KF8ibFEI9TEyU3sog8D-MnBuAIuxBBjCZTKQyVrU6V1JZYiIQyr_5iiBeWOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جای اینا تو جام جهانی خالی بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/129644" target="_blank">📅 01:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129643">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgM_xru60rCjbk6zQ81BBBMPD6dhU48e2asayXjTt9G1vm2bTRGJo80srBGS3YFjr3XqvvEdkX4sX1YySIDqt05Y77uBsb__nm-vqTHRWJp5o4lpGbyT2QBwyGPJCp5lpqWf3klnLocJfrGN7vU83c23cT-sAtWBPNYYypG1DUI7gFlE1DyGkIqlczZay_VJLdkev4ibFOXQEZ2ByxX7_GS1hPYaz9ZXYrdJ75blSCzd0ocY4iUliXue66zmoGa8OOyfS7yyNd8XR7JsmsNcJuxy540hpZ31MVf_7HvprMSxlKGGzWudtqnPwqJMLoJZfxxNwM3Unh45qU-AdiFHYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : نیویورک تایمز نوشته بعد از نزدیک چهار ماه جنگ، تقریباً هیچ چیز عوض نشده
جدی؟!
🔴
ارتششون عملاً از کار افتاده، نیروی دریایی و هواییشون نابود شده، موشک‌ها و پهپادهاشون و توان تولیدشون تقریباً از بین رفته
🔴
رده‌های بالای رهبریشون حذف شدن، تورم سر به فلک کشیده
🔴
اقتصادشون به هم ریخته، سربازهاشون حقوق نمی‌گیرن، تنگه هرمز بازه، نفت همچنان داره جریان داره
🔴
و بازار کار و بورس آمریکا رکورد زده.
ایناست که عوض شده؛ و تازه این فقط بخشی از ماجراست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/129643" target="_blank">📅 01:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129642">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8518f567d8.mp4?token=U7GsmSJPOv-Ne8Wd8EaUgu9YKRxfDB3FdXUN16jEWNJKDXjhIbittMupR5TBoeDdSzotg23NcCRO8eJhBhb0S_cA7BNzTSeDB-mh53eDid0MJNVfsYlb33u5bzbUzCJXevj0R9zz56uAXtysot5FthuCBJRZPPS9yLO0-_Cxlgw1i8DfyTb-Fv9l0yg2mWmaYz7wpmsWjGaO4pL6EnfWS-82HuboZVZbBefCJro6G6x1wERUakM-Ytx_FOwb1gM-niPUC8qRu9QTmL8mdWbkAYHjsJdCMItc0Lb9T5blshN67kxUI5JPZ1UiFdXcND7NTQg0Ci5JzeeSJhqxNKSxaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8518f567d8.mp4?token=U7GsmSJPOv-Ne8Wd8EaUgu9YKRxfDB3FdXUN16jEWNJKDXjhIbittMupR5TBoeDdSzotg23NcCRO8eJhBhb0S_cA7BNzTSeDB-mh53eDid0MJNVfsYlb33u5bzbUzCJXevj0R9zz56uAXtysot5FthuCBJRZPPS9yLO0-_Cxlgw1i8DfyTb-Fv9l0yg2mWmaYz7wpmsWjGaO4pL6EnfWS-82HuboZVZbBefCJro6G6x1wERUakM-Ytx_FOwb1gM-niPUC8qRu9QTmL8mdWbkAYHjsJdCMItc0Lb9T5blshN67kxUI5JPZ1UiFdXcND7NTQg0Ci5JzeeSJhqxNKSxaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور گراهام: مردم لبنان کمک در راه است
حزب‌الله مدت‌هاست که کشور شما را ترور می‌کند. این موضوع به زودی به پایان می‌رسد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/129642" target="_blank">📅 00:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129641">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
قلعه نویی: تیم برتر بودیم و باید میبردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/129641" target="_blank">📅 00:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129640">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
آکسیوس به نقل از یک دیپلمات آمریکایی:
مذاکرات بین تیم‌های فنی ادامه خواهد یافت و آنها احتمالاً برای ادامه کار خود در سوئیس باقی خواهند ماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/129640" target="_blank">📅 00:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129639">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
بلژیک اخراج داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/129639" target="_blank">📅 00:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-129638">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
بچه‌ها بریزیر تو الو اسپورت
⬇️
⬇️
⬇️
@AloSport
@AloSport
صحنه‌های جذاب بازی رو اونجا میزنیم</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/alonews/129638" target="_blank">📅 23:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129637">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
فاکس نیوز: مذاکرات همچنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/129637" target="_blank">📅 23:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129636">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
نیمه دوم شروع شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/129636" target="_blank">📅 23:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129635">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa19e4420f.mp4?token=gBgXvkCM-Y_H4x6xgM4nwS2nBvcudeOyx6M6ZPzIGnJXbqr2xh9D5inaOpFSlTgqHKE6S-s7ov7ay1zQWnzgxEW6_jekgcUMDrFp4gEzMg6XNrpjkbmqaQSAz8tOasw2eJ1Nriyt9yeykoq0IkjDI04qKQhsMYgn1hecCeUhQ1-vPyjJsnouuJtrGdNTDwlBDD1JucAaRBN3pk8zIG_laRx2IGuBL5jk-w7g9s8PJ7j0HwI-2CQUjOiKIzSzwcMKIEOdm05Y0-hrRUA1duzbdI2suqXoVZ7EK__1ZP72vzxZiua_QboC25VITnJ-dnOPkLNYDwTZ7E_Fbh84x171_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa19e4420f.mp4?token=gBgXvkCM-Y_H4x6xgM4nwS2nBvcudeOyx6M6ZPzIGnJXbqr2xh9D5inaOpFSlTgqHKE6S-s7ov7ay1zQWnzgxEW6_jekgcUMDrFp4gEzMg6XNrpjkbmqaQSAz8tOasw2eJ1Nriyt9yeykoq0IkjDI04qKQhsMYgn1hecCeUhQ1-vPyjJsnouuJtrGdNTDwlBDD1JucAaRBN3pk8zIG_laRx2IGuBL5jk-w7g9s8PJ7j0HwI-2CQUjOiKIzSzwcMKIEOdm05Y0-hrRUA1duzbdI2suqXoVZ7EK__1ZP72vzxZiua_QboC25VITnJ-dnOPkLNYDwTZ7E_Fbh84x171_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار صداوسیما: هنوز نمی‌توان گفت که مذاکرات به پایان رسیده است یا خیر اما از شواهد به نظر می‌رسد هیئت ایرانی در آستانه بازگشت به کشور است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/alonews/129635" target="_blank">📅 23:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129634">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bw6ieROhBjup4SAFBHDZP302UPDf9zvXwiOnjmZMBnLxTiNDeYj0f0Vv-m0QJVXzjUbAFaw-KSvjnjY_fiZHIgnuxZngCmxnTLXMiL9rBLPo3c_EOk-oN45rxn-18T_pt33GylnP4K7Isj8jc4lqchpUcuIxfw6nvECqTaLkhjJ6SNkU2L9tXheIkvgH4oGgAvFaXcCYoWzHGeTwWNg2ZsrrTziM7OcgOIzZK2SmJfpy3QGyVgYvSstebd1dRBagkabcbkGTo0wAA7F2szIjymA8FCaADwqVikptuiL95Jwn8Nuzv-Xj06HYzlIrdQQhti6gn6sqMsun7mFtrIRQVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار خارق‌العاده نیمه اول
🔥
@AloSport</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/129634" target="_blank">📅 23:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129633">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
اولین تصاویر از دوحه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/129633" target="_blank">📅 23:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129632">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zcu4ayVQ9OGqAfZ13LncrMibHbhoVjSeHSHHCGk93y86uFlyqe59E00Puhk9SkJZwAjYA288HbZ98rcfO3P7y5sm-4ulJ1QYWRhDsBEcRITf-oqJyledXtBBUf9-aJAXMJsIQ0VldtCnpBfEIDIFKu1px8aorKrYs5h3GmHxOYBUR-XgTfG2KhUpOEi8BFCL3ycXqUlxCOtdiQZuQzhni1cH1psTzYe_v7G1wTDpMECa0BcKjukxsEZzjexusg6SyFOgRYXsg74o3lcFgpO3LtDO4Ts4ezcno3WTstzJKQJe-q_Ag2SU-1eKgxGxJuIPAx6-mW-p_DzCk--9lIFgZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اولین تصاویر از دوحه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/129632" target="_blank">📅 23:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129631">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
رویترز از شنیده شدن صدای انفجار شدید در دوحه قطر خبر داد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/129631" target="_blank">📅 23:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129630">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
رویترز از شنیده شدن صدای انفجار شدید در دوحه قطر خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/129630" target="_blank">📅 23:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129629">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe7c09349.mp4?token=d7keKl5uQYMfJh2Rp3P0_vD5JRNs2HEVmCOzoiHUmdODF_j0zs4epRf_p6GTY-aL43boJPtx4eSTqBlXDgEaP0TdxKjC4KFlO9qDCF4xAOsTXVUcBRPCv7Np8T-ACBl_WLLLz94DrZtAlkX28Hho4c2RYFyA5vKuiM9UcsSnyuR22N_iOGELg8Ypk7WVzKO0F6vwg-AS497_e51QpR3_TTSOTZ9VJ0p4jO7s8Kzuox2Vyc4DcZayRKWPwrnFgOz1ip8Tr8W8NI-xwJ2k7JcEMmSPrW-8KMHZn5IbixD0-WrkTmifMGjclrijvjB-6IJRYFQVtorz-qGSD5CtefC4HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe7c09349.mp4?token=d7keKl5uQYMfJh2Rp3P0_vD5JRNs2HEVmCOzoiHUmdODF_j0zs4epRf_p6GTY-aL43boJPtx4eSTqBlXDgEaP0TdxKjC4KFlO9qDCF4xAOsTXVUcBRPCv7Np8T-ACBl_WLLLz94DrZtAlkX28Hho4c2RYFyA5vKuiM9UcsSnyuR22N_iOGELg8Ypk7WVzKO0F6vwg-AS497_e51QpR3_TTSOTZ9VJ0p4jO7s8Kzuox2Vyc4DcZayRKWPwrnFgOz1ip8Tr8W8NI-xwJ2k7JcEMmSPrW-8KMHZn5IbixD0-WrkTmifMGjclrijvjB-6IJRYFQVtorz-qGSD5CtefC4HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش پزشکیان به علی الاصول گفتن‌های بی پشتوانه و بیجا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/129629" target="_blank">📅 23:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129628">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ-SuEy-lSg2n4bcaqMXj_spJoe9VHVPG8HuU8S3VlFpxqRALnE_LW3t5gtqvY8kHYqupikY29-C0cMjmOGsz2pj41sFJ9fDDmd8iTuUeEHxtwmR0kXDTWZ3llTjYNgr2rH3T3l_563EnaWrO-r8zR4KsWGjAN77lqot0kYxVZlXsi6XHWj_PGU1qOUHJqZOZ82yeaHX234ennh0n7u_P6pUkf9OUJjFlGdQs01KnrfVZz7xLKRnIwwpYPM8VeMgYL6Ep-eFJNEt1_mX3xQ212RDeIqLCKlwJ5GZ0W4wAqTpcFZsBY8PMgfubtBDE2-sNEAQyVY9lbG4zt_LFM-7FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی : اینترنت رو قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/129628" target="_blank">📅 23:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129627">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
صدا و سیما حلال خور، حق پخش رو دزدیده و پولی نداده و خودش کلی تبلیغ چپونده تو زمین و دور زمین
#دزد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/129627" target="_blank">📅 23:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129626">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
مجری صدا و سیما:  گل‌های ایران افسایدشم قبوله
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/129626" target="_blank">📅 23:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129625">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
مجری صدا و سیما:
گل‌های ایران افسایدشم قبوله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/129625" target="_blank">📅 23:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129624">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
زلنسکی: دیروز ما با حمله به پالایشگاه نفت آن‌ها در منطقه تیومن پاسخ دادیم. اگر بخواهیم دقیق صحبت کنیم، فاصله حدود ۲۰۷۰ کیلومتر بود.
🔴
پهپادهای جدید ما با موفقیت به هدف اصابت کردند. مسیر واقعی پرواز آن‌ها حدود ۲۵۰۰ کیلومتر بود.
🔴
آن‌ها قادر خواهند بود ۳۰۰۰ کیلومتر و حتی بیشتر پرواز کنند. این‌ها پهپادهای جدید هستند—پهپادهای خوب.
🔴
آن‌ها به فاصله‌های بیش از ۳۰۰۰ کیلومتر خواهند رسید، چون ما می‌دانیم تمام کارخانه‌های نظامی آن‌ها کجا قرار دارند، تأسیسات نفتی‌شان کجاست، مخازن گازشان کجاست و غیره.
🔴
ما به ابزارهایی نیاز داریم که بتوانند مسافت‌های دورتر را پوشش دهند. و ما در حال ساخت آن‌ها هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/129624" target="_blank">📅 22:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129623">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ایران گل زد که آفساید شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/129623" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129622">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
نتانیاهو: ما در برابر یهودستیزی مبارزه خواهیم کرد.
🔴
ما در برابر بی‌اعتبارسازی خود مبارزه خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/129622" target="_blank">📅 22:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129621">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
آسوشیتدپرس:
هیئت ایرانی و آمریکایی هنوز در سوئیس در حال مذاکره هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/129621" target="_blank">📅 22:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129620">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
نتانیاهو، درباره رژیم ایران :
فکر می‌کنم ما شرایطی رو فراهم کردیم که رژیم ایران سقوط کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/129620" target="_blank">📅 22:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129619">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
نتانیاهو:ما یک «منطقه امنیتی» در غزه ایجاد کردیم.
🔴
ما یک «منطقه امنیتی» در سوریه ایجاد کردیم.
🔴
ما یک «منطقه امنیتی» در لبنان ایجاد کردیم و تا زمانی که لازم باشد آن را حفظ خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/129619" target="_blank">📅 22:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129618">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
صداوسیما: ادامه‌ی برنامه‌ی مذاکراتی هنوز مشخص نیست
🔴
واکنش‌طرف مقابل به پاسخ رئیس هیئت مذاکراتی ایران، در برابر صحبت‌های رئیس جمهور آمریکا مهم است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/129618" target="_blank">📅 22:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129617">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
شبکه کان اسرائیل: ارتش اسرائیل شروع به کاهش نیروهای خود در جنوب لبنان کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/129617" target="_blank">📅 22:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129616">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
نتانیاهو:
در آمریکا می‌گویند که ترامپ هر کاری را که من از او بخواهم انجام می‌دهد.
و در اسرائیل می‌گویند من هر کاری را که او بخواهد انجام می‌دهم.
هیچ‌کدام درست نیست. ما رهبران کشورهایی مستقل و با افتخار هستیم.
من نماینده منافع اسرائیل هستم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/129616" target="_blank">📅 22:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129615">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سی‌بی‌اس:
دولت ترامپ خواستار عقب‌نشینی جزئی اسرائیل از جنوب لبنان شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/129615" target="_blank">📅 21:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129614">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-poll">
<h4>📊 دوست دارید کی ببره؟</h4>
<ul>
<li>✓ ایران</li>
<li>✓ بلژیک</li>
</ul>
</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/129614" target="_blank">📅 21:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129613">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
بیرانوند: دروازه رو مثل تنگه میبندم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/129613" target="_blank">📅 21:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129612">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1jtOcOvKoj_u7IBc2iZSVIdXWJ2erzySo9MOybeXWqIdEZck11Lw13_nl-IG7K2Oy--MA3vLtY0MakfW-hrUN50CS5Cas2R3wLTgvA7saBEL1nKL7VhUZy43ZN0abZJLIEjfA2YkYkLcjsyzlSKKDEsWK8CEOrEDlMUM8DXvn_KdxntMhPT-08PXMeH7YKhJf7nR3x_omZfHuiS9QWm-8yIpeiXfedVCRyl0VUND8Bqk6_QQ77OsksEf7nkTCCjq5Bfd4fV5wHauVvVAXOXXm6X5_Mre4pKn1S4qDz_7vCP5ZBHGqszOf0mPH-6F9ruQtVQb9hF8V0j1yifzMeeow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از نکات فنی قلعه نویی به تیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/129612" target="_blank">📅 21:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129611">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
المیادین: هیأت ایرانی تا زمانی که ترامپ عذرخواهی نکند و اسرائیل از جنوب لبنان عقب نشینی کند، به مذاکرات باز نمی گردد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/129611" target="_blank">📅 21:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129610">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2b50d32cb.mp4?token=p1fEKBU8OqB38aYAg2mIkCBYZPOJ4syAr7ZYFjoLBlZDtbm21LyNmc0EjwzA451uiNjdR-PEsUOQgoBIfsWjhwZkUmvkavnhfSn6-yuE9oz5QDjnu8eRYWfoj4HHOJaf68vEyAbbrlXFDc5VKt5fheXY3-0X5ZSwDAeYAERCDiCuQDxqBwhFk_zGFIaGCvNtsk16a-LBihbd5ZSCVQ7buj0yGK2TszpG_o4Ru-GoGhNJq8vE71R5IgRjzUw8rl8aD7AZw9MwYFztSJlICSg1xej8Ah1Lo5qDfyANFuq9JCXHi2orjyHeXiFHK7jgrrcY3DyfjRwFRlpgI9rgL_MIdUYdreY37WbnyFWjS9-LhodXBmMPWt6oQghjaemimo92MXQsNEh2tQu9OGF_FwU4WgJaPgqJdrGNjBc9006YVPxJLVT-lonnIB2fUnV_OxjKXFlG9dTg4_P3dfeM3q5KPcLFC8oq9acJm3nBfxmOuQNn_r2_hlFzswGdQ9P4vlIZnHCZQ3U-Xvp1514wS9G28wXkykrj3mp5hV8qmpazHkQH3NBWX2qXqS8haKOdXDg5TZDmO6TlPwj6oEn6OCLmwrtf6LNv8tIm2oEWlGrxJaaW2WoDjmEBFvNEp04lMWkidwVGTjUjqb7ZFPORDBATsLsc6meb3ANIKXcTi9NYlZ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2b50d32cb.mp4?token=p1fEKBU8OqB38aYAg2mIkCBYZPOJ4syAr7ZYFjoLBlZDtbm21LyNmc0EjwzA451uiNjdR-PEsUOQgoBIfsWjhwZkUmvkavnhfSn6-yuE9oz5QDjnu8eRYWfoj4HHOJaf68vEyAbbrlXFDc5VKt5fheXY3-0X5ZSwDAeYAERCDiCuQDxqBwhFk_zGFIaGCvNtsk16a-LBihbd5ZSCVQ7buj0yGK2TszpG_o4Ru-GoGhNJq8vE71R5IgRjzUw8rl8aD7AZw9MwYFztSJlICSg1xej8Ah1Lo5qDfyANFuq9JCXHi2orjyHeXiFHK7jgrrcY3DyfjRwFRlpgI9rgL_MIdUYdreY37WbnyFWjS9-LhodXBmMPWt6oQghjaemimo92MXQsNEh2tQu9OGF_FwU4WgJaPgqJdrGNjBc9006YVPxJLVT-lonnIB2fUnV_OxjKXFlG9dTg4_P3dfeM3q5KPcLFC8oq9acJm3nBfxmOuQNn_r2_hlFzswGdQ9P4vlIZnHCZQ3U-Xvp1514wS9G28wXkykrj3mp5hV8qmpazHkQH3NBWX2qXqS8haKOdXDg5TZDmO6TlPwj6oEn6OCLmwrtf6LNv8tIm2oEWlGrxJaaW2WoDjmEBFvNEp04lMWkidwVGTjUjqb7ZFPORDBATsLsc6meb3ANIKXcTi9NYlZ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ضرغامی در مصاحبه جدیدش علنا به حکومت دوره آقای آیت الله خامنه‌ای انتقادات سخت وارد و اعلام نیاز به رفراندوم کرده است
🔴
ضرغامی گفت مردم باید تصمیم بگیرند که چه سرنوشتی داشته باشند و خودکامگی کار فرعون بود.
#تغییر_پارادایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/129610" target="_blank">📅 21:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129609">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: قطر و پاکستان از ترامپ خواستند تا پیامی‌برای کاهش تنش تنظیم کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/129609" target="_blank">📅 21:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129608">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
خطاب به اونایی که ۲شبه علی الاصول راه انداختن
🔴
اصول خدمت به مردم و راحتی زندگی مردمه که سما درکی ازش ندارید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/129608" target="_blank">📅 21:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129607">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: اسرائیل در حال بررسی «عقب‌نشینی‌های محدود» در لبنان است که شامل خروج از قلعهٔ بوفور (شقیف) نیز می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/129607" target="_blank">📅 20:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129606">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HHAdkMbekAhk-f_oSvc34TZF8vH9YNvkrWv5XslU0cimNupZ1wUFoD2YsMpMf-imA3ttl6ZqCjzULzbClO718vxZWAmD-_EphEizt8Is96eeCpBHGtdzMF7bx0fsHQLDAPMVMWE9Hfs83KBOecf0qdVlMAmxsEZ72WPZDXS4jN4CPWnhk2zQKTwg9_8VaRQQHvvUW-qsYuyRxBIglfDSr4UrJctfO9mAAAAKrNLEtn8ovcnDeH6wM3hXpQUJj_zWCOINMVhyGIq_Nn0P45O13NgR8jD7TGA59hNAnCc6l-fYMxaOMQGqFtHAcMvcDlkfUkAGumGYSMEgQP84uAoJ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
ترکیب ایران مقابل بلژیک
@AloSport</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/129606" target="_blank">📅 20:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129605">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
العربیه: هیئت ایرانی به محل مذاکره برگشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/129605" target="_blank">📅 20:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129604">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfJcfjbZILjczlNrriq6vIFW0tkhqJsHriz6DlRptzvnT9ImYpYPZhiXKmFEXt755QvmE8Fv6S4FB401vywvl1a_LaOhuYYzJpVgHEHCAigSeh-Bb9_-M_qNenuKiBByiIooc-AddLokkpq89aubXHX60P-cTZjJKmQD2cIPayfgz2_DIU74AnIE-mMotVf_yo-I7ryF7kUV5wI9WVzKN8wIh9dFWdYWIPUmmGliaO8tacGvys_t8PeSm_Bp45sMDyITV3jKGUeU8XzUSISaUzPqGKkA_Nk14M4VokoSTRtzlxko-qv1Dk3Vc2oNF2kIBhQgSks6jIjfXPBQbpT8Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید خبرنگار آکسیوس:
مقامات ایرانی هنوز نرفتن و مذاکرات همچنان ادامه داره.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/129604" target="_blank">📅 20:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129603">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ایرنا: هیأت ایران پس از دیدار با هیأت قطری به‌عنوان یکی از طرف‌های میانجی، ساختمان محل مذاکرات را ترک کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/129603" target="_blank">📅 20:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129602">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده:
ایران مصمم است روند اجرایی شدن تعهدات طرف مقابل را با وسواس و جدیت پیگیری کند.
🔴
نشست امروز در سوئیس، برای پیگیری اجرای مفاد یادداشت تفاهم خاتمه جنگ مورخ ۲۸ خرداد ۱۴۰۵ است.
🔴
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است.
🔴
بدون اجرای این مفاد به‌ویژه بند ۱ (خاتمه جنگ در همه جبهه‌ها شامل لبنان) ورود به مرحله مذاکره برای توافق نهایی ممکن نیست.
🔴
گفت وگوهای امروز، متمرکز بر اجرای بندهای مزبور، به‌ویژه بند ۱، و نیز مرور تدابیری است که برای اجرایی کردن بندهای ۱۰ (موضوع صادرات نفت ایران) و ۱۱ (آزادسازی دارائی‌های مسدودشده ایران) پیش‌بینی شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/129602" target="_blank">📅 20:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129601">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
منابع ایرانی به العربیه:  تهدید ترامپ باعث توقف مذاکرات شد و امکان ادامه آن را زیر سوال برد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/129601" target="_blank">📅 20:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129600">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
عضو هئیت ایرانی در سوئیس به صداوسیما: اگر جنگ در لبنان پایان نیابد، مذاکرات ادامه نخواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/129600" target="_blank">📅 20:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129599">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
المنار: هیئت مذاکره‌کننده ایرانی در اعتراض به تهدیدات ترامپ محل مذاکره را ترک کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/129599" target="_blank">📅 20:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129598">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
فوری / فارس: مذاکرات متوقف شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/129598" target="_blank">📅 19:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129596">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری/تسنیم:
مذاکرات آمریکا و ایران در سوئیس زودتر از موعد با خروج ایران از جلسه پایان یافت، به دلیل پست ها و تهدید های امروز ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/129596" target="_blank">📅 19:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129595">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
جی‌دی ونس: من شوخی کرده‌ام که دو نفر بسیار، بسیار مهم در زندگی من وجود دارند: یک هندی و یک پاکستانی.
🔴
هندی همسر من است و پاکستانی فیلد مارشال منیر است. احتمالاً در سه ماه گذشته بیشتر از هر کس دیگری با فیلد مارشال منیر صحبت کرده‌ام.
🔴
بدون دیپلماسی او اینجا نبودیم. او یک رهبر نظامی است، اما فکر می‌کنم نشان داده است که یک دیپلمات بزرگ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/129595" target="_blank">📅 19:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129594">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwBZ3WBzffWF1Z7ouZg2xZrKW3hbS1DH0xxfc__58Bh1afH6LWuIWNnxPGPQf_QKW-t13RsML25RQ77n7MEE3A7_FR_KYM8vh2VExS6Nj17kQzWVtrIhoW5E1RckBT406gg8h_P43Zq8e8wuRT7tqjCZGDncuI9uvx7rs-KcWNVoV-v0YzCLd5WqNBLUhnP7usSXcO6JJysmJWQ_AIlGuBrmbbYtYPTC7TJ75e832gymSHwDdPgwq6txPolrMPM3FJBzKB8hSoquaBZh2P1ymfRQ4zEHft4inuzGfKwXYrD8lb6a6IUczGmiYLb1vyoQNuGEUCSJ2_TPVUrYhgO7JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید قالیباف در واکنش به تهدیدای ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/129594" target="_blank">📅 19:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129593">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
جی دی ونس: گشایش تنگه هرمز، پایان دادن به برنامه هسته ای ایران - این چیزها قبلاً انجام شده است.
🔴
اکنون سؤال این است که چقدر بیشتر می توانیم با هم انجام دهیم.
🔴
آیا می‌توانیم روابط در خاورمیانه را برای همیشه تغییر دهیم یا به انجام کارها به روش قدیمی بازگردیم، که ترجیح ما نیست، اما مطمئناً ممکن است اتفاق بیفتد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/129593" target="_blank">📅 19:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129592">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
مدیر عامل شرکت ملی نفت: از دوشنبه هفته گذشته، کشتی هایمان از خط فرضی محاصره، با ۲۵ میلیون بشکه نفت عبور کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/129592" target="_blank">📅 19:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129591">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
دبیرکل حزب‌الله: چیزی به نام «آتش‌بس به همراه آزادی عمل برای اسرائیل» وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/129591" target="_blank">📅 19:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129590">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
نماینده آمریکا در سازمان ملل: می‌خواهیم برنامه هسته‌ای ایران را به طور دائمی از بین ببریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/129590" target="_blank">📅 19:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129589">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
العربیه:جلسهٔ دوم مذاکرات اندکی بعد آغاز می‌شود.
🔴
هیئت ایرانی به سالن مذاکره بازگشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/129589" target="_blank">📅 19:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129588">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
اکسیوس: یک مقام آمریکایی می‌گوید که هیئت اعزامی برای نشست چهارجانبه شامل افراد زیر بوده است:
🔴
جی‌دی ونس، معاون رئیس‌جمهور آمریکا
🔴
استیو ویتکاف، فرستاده ویژه کاخ سفید
🔴
جرد کوشنر
🔴
جیکوب رِسس، رئیس دفتر معاون رئیس‌جمهور آمریکا
🔴
دکتر اندی بیکر، معاون مشاور امنیت ملی و مشاور امنیت ملی معاون رئیس‌جمهور آمریکا
🔴
کلیف سیمز، مشاور امنیت ملی معاون رئیس‌جمهور آمریکا
🔴
نیک استوارت، مشاور ارشد ویتکاف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/129588" target="_blank">📅 19:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129587">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
خبرنگار صداوسیما در محل مذاکرات:  گفتگوی دوجانبه هیئت های ایران و قطر، بعد از مذاکرات چهارجانبه آغاز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/129587" target="_blank">📅 19:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129586">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
پرس تی وی:
هیئت ایرانی اعتراض خود را به طرف آمریکایی اعلام کرده و اکنون در حال بررسی گزینه‌های پاسخ مناسب به تهدیدات لفظی اخیر دونالد ترامپ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/129586" target="_blank">📅 19:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129585">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
لیندزی گراهام: من روز جمعه ۴ ساعت و نیم پیش ترامپ بودم و چیزی که فهمیدم این بود که اگر توافق صورت نگیرد، او بلافاصله حمله سنگینی به ایران انجام میدهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/129585" target="_blank">📅 19:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129584">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/727d10eda8.mp4?token=C-QNUbYwDjPczDyeiiYCVTuKu00bPtf_00LAexXjmhE1EOCN32zIcuTtfW0vERJ1qYjGlxH6IGbHkaeY2_8Qg2S3DZ4jGinuUB6nCoyyUCcQuqtFAVHRYojia4shMEPfAL5DbQuVAYs1O-gByCzVqP-FvpI0Y22ExwaB6dUSDZ4pn6nRCKFcSPb-46G_j98SjzOgOn2lJydZ4KdiTPOJ8jveXHzwYCi35LyLUKvUDeEBPCYbZ2kLIreSSlMTJJKRXRkdMxa3kmwX3F4kI0icjQOyjVAUDTbjf6FelEZk722-JJlejEf6SedbvOSlkkGHukmhi0BEXU_kf8gpLBxN0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/727d10eda8.mp4?token=C-QNUbYwDjPczDyeiiYCVTuKu00bPtf_00LAexXjmhE1EOCN32zIcuTtfW0vERJ1qYjGlxH6IGbHkaeY2_8Qg2S3DZ4jGinuUB6nCoyyUCcQuqtFAVHRYojia4shMEPfAL5DbQuVAYs1O-gByCzVqP-FvpI0Y22ExwaB6dUSDZ4pn6nRCKFcSPb-46G_j98SjzOgOn2lJydZ4KdiTPOJ8jveXHzwYCi35LyLUKvUDeEBPCYbZ2kLIreSSlMTJJKRXRkdMxa3kmwX3F4kI0icjQOyjVAUDTbjf6FelEZk722-JJlejEf6SedbvOSlkkGHukmhi0BEXU_kf8gpLBxN0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نظر سیدعلی خامنه ای در باب مذاکرات همراه با تهدید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/129584" target="_blank">📅 19:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129583">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtBIGPHi4HNrNurY2j_R2aMaN_Bwvj7Wj0pRaVil-eSWWUYkGUNJB9OfO6n4SOy-w6o_a7uEOZO5xDNlCmhKdDNZEmSZ7lRgk4yq0ACjd-OG93hEqLQzSyEHbVbyVPf0jYSng5UWPmrnRK9voBr7RO--2hIwkYMToNHW_8VNwRNlabeUJ7OZMRa1QVCm9VZyf3lTdU5MHA3hejbrp10BP2ZBlFAlklTYj_wSikaD7flkxK6njYWxFNbZbpU47E8UCenBCRO6Fi0pDELx5nGPVnnllzCxPDvpp9lrlu3bFLGr1K25Bdhozp3sD9MHfyTZiWvxiUq1Cum07l4pq0RAwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی : شرطای آقا رو زیر پا گذاشتید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/129583" target="_blank">📅 19:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129582">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
درحالیکه منابع رسمی داخلی می‌گویند مذاکرات فعلی متمرکز بر لبنان و اجرای مفاد تفاهمنامه ایران و امریکاست و منابع غربی نیز اذعان کرده‌اند که بحث لبنان و ایجاد سازوکار حفظ آتش‌بس در لبنان در اولویت نخست مذاکرات امروز است، جریان رادیکال در ایران از صبح امروز به صورت پیوسته در حال پخش این شایعه است که گفتگوها وارد حوزه هسته‌ای شده است
🔴
لازم به ذکر است که به گفته تلویزیون المنار حزب الله، با پافشاری مذاکره کنندگان ایران، در ۲۰ ساعت گذشته دیگر شلیکی از سوی اسرائیل به لبنان صورت نگرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/129582" target="_blank">📅 19:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129581">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFREdqM9rJHQeknUIWVA5PHPkPrZgDFiQprGhuT040Ie0KRB1dmU4RLzhb9dLri05Nj6xcSEyYaol05nv6CwNa38L1ww13jYGq6EI0LEPM1onsyijK2moZEbtfI89-g-4_TVrgQb6RhFLOSwFtSY4YQzw91hJ32Pxvw_19ffRfiky5oyChsvlNaEA_eXqs7OWP1ioNCbCvbRI54uGXao-sseFcQiPQrKEe5WkYqftAMFnOiy1JsPpLKNBGhKlvWBqvJ82yuSyuIPFO3zxaStqlzamd0qflkxMNTK-g-tBGYvvG08VPeKGDgseiA8VIjPZkHfC95qbIwklLDuyYZ0Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس: گروسی را به مذاکرات راه ندهید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/129581" target="_blank">📅 18:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129580">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
نتانیاهو: تا زمانی که لازم باشد  در جنوب لبنان باقی خواهیم ماند
🔴
و در مورد ایران، هرچند تحولات سیاسی باشد، اجازه نخواهم داد ایران به سلاح‌های هسته‌ای مجهز شود
🔴
تا زمانی که من نخست‌وزیر اسرائیل هستم، این اتفاق نخواهد افتاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/129580" target="_blank">📅 18:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129579">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک دیپلمات: مذاکرات جاری در سوئیس به جنگ در لبنان، تنگه هرمز و ذخایر هسته‌ای ایران می‌پردازد.
🔴
جلسات سوئیس به عنوان یک گفتگوی آزاد با صراحت فراوان آغاز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/129579" target="_blank">📅 18:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129578">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
نشست چهارجانبۀ سوئیس پس از ۸۰ دقیقه گفت‌وگو جهت مشورت های داخلی متوقف شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/129578" target="_blank">📅 18:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129577">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
جر و بحث مجری و کارشناس صداوسیما با هم بر سر نقض تفاهمنامه ایران-آمریکا
🔴
کارشناس صداوسیما: شما وکیل مدافع تیم مذاکره کننده هستی! پس من سوال می‌پرسم و شما پاسخ بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/129577" target="_blank">📅 18:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129576">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caed9884f2.mp4?token=muI1RF7HhJg5OXduR_PgT5jwAr9ACo8l7xXF-lV7Z_4_mL_mqVGc9b-_5cjIJdpKUB64dnHpju8XMGJKFy8bJyDbUnneD4pxAZuBzuSZslWrkfocVbl3DBFfthzVRMPa6ZRE4zxiJiX8LDgYILciRdp31kVfPgTHVwg_EOoevBTHaMh8ovE2Kytc9D7m0zQ81vOyjZFBwNsE4y8UIfcCzsnXFCjlNruU7l0ytpa-HTi9EhCswwVl1TedqbHPzrNAoowL52SzrkUYPN049Z0zGtZoiPNV3s9CQT6gT8YaEO289t141YR4NqaAnxYAa7hk5vuQkD-6Af58nIIOHXGDoLO_QNH12ygIO5BNa_8iafsCUvzzoJt7CG98IupZi6JYdBucMoX6bXq8Z_2d_pzDFZTCNmvH9OfS407PL0FnpVJsGXe97z-Y32RV9CyycNLP_paahX7x9Rz8YKJnROQUvwKoOzFqJgJQ4OqzdENSLe9fTzzHXp45WcCbuL0xQSXgrgBatv-Ww1J_LrJ_WlunfIvv0fqkosI0KEKSEMRHLjbpctYsl-x20DwTl9tH2RbM0PuZ9SfQY0NjjIT9Pzx0wTdQuK6DxCxfGQZxoavXRlvX2qzKX18NO9MtrZnpxL5pxEB0bi30y7L5j1e1SQ3uLyb7j8bMqmFWhdh7OLronXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caed9884f2.mp4?token=muI1RF7HhJg5OXduR_PgT5jwAr9ACo8l7xXF-lV7Z_4_mL_mqVGc9b-_5cjIJdpKUB64dnHpju8XMGJKFy8bJyDbUnneD4pxAZuBzuSZslWrkfocVbl3DBFfthzVRMPa6ZRE4zxiJiX8LDgYILciRdp31kVfPgTHVwg_EOoevBTHaMh8ovE2Kytc9D7m0zQ81vOyjZFBwNsE4y8UIfcCzsnXFCjlNruU7l0ytpa-HTi9EhCswwVl1TedqbHPzrNAoowL52SzrkUYPN049Z0zGtZoiPNV3s9CQT6gT8YaEO289t141YR4NqaAnxYAa7hk5vuQkD-6Af58nIIOHXGDoLO_QNH12ygIO5BNa_8iafsCUvzzoJt7CG98IupZi6JYdBucMoX6bXq8Z_2d_pzDFZTCNmvH9OfS407PL0FnpVJsGXe97z-Y32RV9CyycNLP_paahX7x9Rz8YKJnROQUvwKoOzFqJgJQ4OqzdENSLe9fTzzHXp45WcCbuL0xQSXgrgBatv-Ww1J_LrJ_WlunfIvv0fqkosI0KEKSEMRHLjbpctYsl-x20DwTl9tH2RbM0PuZ9SfQY0NjjIT9Pzx0wTdQuK6DxCxfGQZxoavXRlvX2qzKX18NO9MtrZnpxL5pxEB0bi30y7L5j1e1SQ3uLyb7j8bMqmFWhdh7OLronXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از مانور مشترک نیروی هوایی ترکیه و مصر که در مصر برگزار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/129576" target="_blank">📅 18:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129575">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مذاکرات دو ساعت دیگر به اتمام می‌رسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/129575" target="_blank">📅 18:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129574">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزیر انرژی آمریکا به ای‌بی‌سی:
۶۷ کشتی دیروز از تنگه هرمز عبور کردند و حجم نفت در حال عبور، نزدیک به میزان پیش از جنگ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/129574" target="_blank">📅 18:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129573">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سفیر ایالات متحده در اسرائیل:
آمریکایی‌ها، چه درک کنند و چه نه، باید به خاطر مردم یهودی به خدا سپاسگزار باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/129573" target="_blank">📅 18:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129572">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سفیر ایالات متحده در اسرائیل، مایک هاکبی
:
آمریکایی‌ها، چه درک کنند و چه نه، باید به خاطر مردم یهودی به خدا سپاسگزار باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/129572" target="_blank">📅 18:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129571">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
فوری / ترامپ: نزدیک است که مسئله حزب‌الله را به سوریه بسپرم
🔴
آمریکا ممکن است در آینده در صورت لزوم تنگه هرمز را تصاحب کرده و عوارض دریافت کند
🔴
این به معنای حضور آمریکا به عنوان «فرشته نگهبان» تنگه هرمز و خاورمیانه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/129571" target="_blank">📅 18:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129570">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACsw8JmuzvIfJLbHvr4kCeqQvxqkeqYwcPAYYlAkP0QEqQ_uDU6wmWGhfhhdY50inmCwx5pNJnyZr63YLQFM-Kcp0CMQ73mbiNUEWmi1AtJpLYMdRF2Z_h2VynvK3v8QZqnqUBB2USo9TYf3MjykQBrF8seHJg1MUYAHyxpHgTHm5lckW3Y2YAYmJiIhnv355m86ZLkkwpEbsnnFMW-RJMAC4RzLeSD34D_TVvQ1qPniA34eBkaa6tSkv0dD8O5vMshPqctJzdujmlOGCdyPlKJocCsZ7CYAiVWWgRLi2oIIbxWHetCgASV8Bh_MfZPGsvbYd4hrPZW0wTPjFwBnzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بند اول تفاهم‌نامه اسلام‌آباد: جمهوری اسلامی ایران و ایالات متحده آمریکا متعهد می‌ شوند از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/129570" target="_blank">📅 18:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129569">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIBP8PNeXjvRKWZaOURNdUZ_yjiu3wUMzXkcSdf6CcVGIbsaO5lx25lEwEtJXPvOnSqiT7-Zi4EBcWjghMHyoFbc6GkTDBWf7KO3Xbfr8IqZ0-pN9dWopZH4t_nV5xgtYmANYXs8ZUEA8w9LTAiI3RaYPoH7ytb0SzxyuJzJ0NCPX3kZ6ZRAoHYjCsqY3Go34Okzf3mVlZcQ5OPapCtC8wy2M8FrDixCaLLant8e49Zpp3NWu9dnunerX0ukPxxclfe9ntt1SkgUU8-MmQviL4p1_VZS09iSBAzSHwvvhvEsW-1e-z8HHbj0_-Avxao_WZ6V9rfKGmFA0HcC9Pdxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی هوایی اسرائیل به
اردوگاه
البریج تو لُبنان، حملهِ کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/129569" target="_blank">📅 17:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129568">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ef202698d.mp4?token=Xp6w2wqlTzbM35BQ6vc6QGmeCg7JwJlGFyFf3GO_KihtGqT1Mok4cWO0OSQ5Qo_2FUKHMFXrIv98uMt-xWeCgd5mgOQ366lVGStehk4LHmRgFVn6Q4-osqxn4kg1P8EG8voUvAg49r9ALSAwcKESsANAbkRN8qhqX-ogiDg2fZAf63sT-ogAV3O2IpzWfUiZrFsxFqJJan0u1VE9hZR6fayVdjvtUwUJmBxQA880y_jpc1N09MTJYS8Ztf3NGuBsbL3-BXGMqQ0MKCXTIkoubhkm9tij4u4y5csdFzPQf7L_dR6yBuaxy2HHvcYKCW7tMspwnZYntj2RfnZPbBimyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ef202698d.mp4?token=Xp6w2wqlTzbM35BQ6vc6QGmeCg7JwJlGFyFf3GO_KihtGqT1Mok4cWO0OSQ5Qo_2FUKHMFXrIv98uMt-xWeCgd5mgOQ366lVGStehk4LHmRgFVn6Q4-osqxn4kg1P8EG8voUvAg49r9ALSAwcKESsANAbkRN8qhqX-ogiDg2fZAf63sT-ogAV3O2IpzWfUiZrFsxFqJJan0u1VE9hZR6fayVdjvtUwUJmBxQA880y_jpc1N09MTJYS8Ztf3NGuBsbL3-BXGMqQ0MKCXTIkoubhkm9tij4u4y5csdFzPQf7L_dR6yBuaxy2HHvcYKCW7tMspwnZYntj2RfnZPbBimyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیبر امنیت داخلی آمریکا، مولین : شاهد افزایش غیرعادی شهروندان ایرانی هستیم
🔴
اونا سعی می‌کنن از مرز شمالی آمریکا، نه مرز جنوبی، مخفیانه وارد کشور بشن
🔴
این موضوع نگران‌کنند‌ست برای ما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/129568" target="_blank">📅 17:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129567">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سازمان دریانوردی بریتانیا: گزارشی از حادثه‌ای در ۵۰ مایل دریایی سواحل یمن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/129567" target="_blank">📅 17:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129566">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رئیس ستاد کل ارتش اسرائیل: آتش‌بس اعلام شده در لبنان شکننده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/129566" target="_blank">📅 17:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129565">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-YNqE6ClvC5nB7cgZul1omHpIitfnlt--fiFlmGpzZLkRj452Sk3PEgBae3CdUsQnCCNsqah31nDXftGIHgl4u8hSLdoD_I6pntztwUd4BgTRX-y8XCHSVlCFD6zvFY7e2M7_fOEXR1tBQ_xqx4StHkv7b5BRVU6QCG6_CaDDc7cZPHnK_6jMbc_4C7IID54dBqipp5v3n0heRArO44BxVhFapsSLhDCTwPyqI5iv9ZVRStVAwRE4OcyxDi7gK6YYzlPASAPaQwXf2-FZedsfQXjFB0uxEU-Y_D0gCvwLy_jM_feH1jv7LDvssOmmf1XUoA12rF4PqRIT1CyyTDxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: کیر استارمر از سمت نخست‌وزیری بریتانیا استعفا خواهد داد.
🔴
او در دو موضوع خیلی مهم به‌طور بدی شکست خورد — مهاجرت و انرژی (باز کردن استخراج نفت دریای شمال!). برایش آرزوی موفقیت می‌کنم!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/129565" target="_blank">📅 17:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129564">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DumTte6xASlhTGzsBolMiIasJ7kiK4Jj8DzTwfmu99csZlBfwNmF2QRNNlDZPWjBjeYqwORf3VaMgQo9mWqHBQ0pysEtzlLAqYVVypd-CNkqOTQVwGLBBsNVK9Kuw7nEvythvqUdpcQn751ZHOqZLbsU4xvIe_tlaiDBPNHid0yjb-yPiVhm9hA6P68SN7K4goE-opfP6C2PmZ3DtnaOWgwugOBgF_2y7awPRxNzcsustvGKCep8mtp3tSi0xQ_EB0d_03EEIhcsuZXXo1hHCD3IZrU7nvF0ucZxR43PO6vZWHO4gQ5obUc_g7La7J-YPe0n6zGnSt2bWriDeiiwqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی، عضو سابق تیم مذاکره‌کننده در واکنش به توییت ترامپ در مورد عوارض تنگه هرمز: هزینه‌ای دریافت خواهد شد، این قطعی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/129564" target="_blank">📅 17:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129563">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری/ترامپ: یادداشت تفاهم صرفاً تمدید آتش‌بس است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/129563" target="_blank">📅 17:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129562">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=gyZd4fHhHXmwewMLkJWfDxtSJqd7lOLh1yaD0Qf4zIRFFAXw0-RvWeu0qx0F1PgrO1mbF-UhpwW8-ycyRmIPjKHr4-KU4F3VhLkvgzP8mLNo4MZ6PqaOUomglFblqshDO1fwjae0Utp6bd_wbHp8lfmzNainM9YcVSxelPmViZUTibBpPf6q2GDwGuH8zEjvfxjbpEIBuPrDz0XCfkd8wjfafub5eASmEtXsBlg3Amfz-9MU2o7AEbjNhzA2wzFRZKyykveLaPNGqvM5Klel8RlCn0dHu3sV0LHq6z6-TGqVXPFQpJcTxc3iAccCukTqbglPcHtlC2ic8Pn18Djkd0XBh4-Isns0OLblJJ0uu78mPXOaxmyctI-eHYiF7Bo6McIVolzmDbRLOLa6_o-b2NS_gjjgds5MQx1c4mfYpEfZdl9PnGhMbbSLxoWefvvdOmnc1TOSZS9r1DlFL4nYda4qlSEcBxEf_BCCSpTrdlwYnV2qLjE5rSyXtwbq_6MV1O5KUTGf2-XQUbxBurzM-nUVdUyeWLo8C_rMMfXJw8zh-3yvzk3kOMGEotH5vzw8jOEQZ-S55pnKt_zNvEPLfwmFnHis6_k0G8LIZ40zSfhT3DernTzjfgemZC80rBOj0e0Hx1-Ps_yBUo1qp3hHJdlllZiKE1UAoNPySEkjKes" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=gyZd4fHhHXmwewMLkJWfDxtSJqd7lOLh1yaD0Qf4zIRFFAXw0-RvWeu0qx0F1PgrO1mbF-UhpwW8-ycyRmIPjKHr4-KU4F3VhLkvgzP8mLNo4MZ6PqaOUomglFblqshDO1fwjae0Utp6bd_wbHp8lfmzNainM9YcVSxelPmViZUTibBpPf6q2GDwGuH8zEjvfxjbpEIBuPrDz0XCfkd8wjfafub5eASmEtXsBlg3Amfz-9MU2o7AEbjNhzA2wzFRZKyykveLaPNGqvM5Klel8RlCn0dHu3sV0LHq6z6-TGqVXPFQpJcTxc3iAccCukTqbglPcHtlC2ic8Pn18Djkd0XBh4-Isns0OLblJJ0uu78mPXOaxmyctI-eHYiF7Bo6McIVolzmDbRLOLa6_o-b2NS_gjjgds5MQx1c4mfYpEfZdl9PnGhMbbSLxoWefvvdOmnc1TOSZS9r1DlFL4nYda4qlSEcBxEf_BCCSpTrdlwYnV2qLjE5rSyXtwbq_6MV1O5KUTGf2-XQUbxBurzM-nUVdUyeWLo8C_rMMfXJw8zh-3yvzk3kOMGEotH5vzw8jOEQZ-S55pnKt_zNvEPLfwmFnHis6_k0G8LIZ40zSfhT3DernTzjfgemZC80rBOj0e0Hx1-Ps_yBUo1qp3hHJdlllZiKE1UAoNPySEkjKes" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: اگر لازم باشد ممکن است تنگه را تصرف کنیم. من آن‌ها را کاملاً نابود خواهم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/129562" target="_blank">📅 17:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129561">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=GdbIiAb15zLZny_H2QSib2jfjQ-gPO3H-RtRfEnuCbfRRX6cK9aDAs8XCjgnphSt_yJbgIgP1N120snKusvea_EQS0G2iWRerymttDSsKDjZEKD4f5Ao9Dv8qDiZtYx6JmCmg-Z89qicKsvMRpnonLTllWWB2Il7WfpgZSJzaFKCwF_0LtMhkKIhkifWu-K1Luov1lcjEx2ElyQNPCoWNUo3gBnroesxFjPlEmPQBZueDM4Swn6HdrRyOXZQn6uacxesjmczqZDykkT48aCDrUdm0Bs5ouoYtB6JWUNQMAmpu6cPuM4ugOoYh65oAWCl4Gy5-K0MGzUg4f7giOBxN3NBb02pxIfsG__M0PGIQJ9kDiRXae-oCoAEax7UFWrJbzbIjfm55JsBBsAaLHfAj_iycQkbXSzGjPruwRBXLNjaexSGTq7-VR3QaeKH8m0wuISbiic9v_2xM3WubXW8P4sfrW8MjBDyceoSTqrBxGK3dXZ4YS5Prf6O7WjLLCkL30fp_OxkwGTV-fWB-qvqMKKeH-fFhDJNkWCxJhsx3Fuarnw8xcCjcr_E27q5-4SSFgodGSSebHNz57VRnKVpJQMvPC1l3uqqYmKciEV3jZPz2GuH1fRiABrhv_vezymj7frxAq2_P5LUflU25J47cPS8qSsEWDKF_0n63Ncp9Mk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=GdbIiAb15zLZny_H2QSib2jfjQ-gPO3H-RtRfEnuCbfRRX6cK9aDAs8XCjgnphSt_yJbgIgP1N120snKusvea_EQS0G2iWRerymttDSsKDjZEKD4f5Ao9Dv8qDiZtYx6JmCmg-Z89qicKsvMRpnonLTllWWB2Il7WfpgZSJzaFKCwF_0LtMhkKIhkifWu-K1Luov1lcjEx2ElyQNPCoWNUo3gBnroesxFjPlEmPQBZueDM4Swn6HdrRyOXZQn6uacxesjmczqZDykkT48aCDrUdm0Bs5ouoYtB6JWUNQMAmpu6cPuM4ugOoYh65oAWCl4Gy5-K0MGzUg4f7giOBxN3NBb02pxIfsG__M0PGIQJ9kDiRXae-oCoAEax7UFWrJbzbIjfm55JsBBsAaLHfAj_iycQkbXSzGjPruwRBXLNjaexSGTq7-VR3QaeKH8m0wuISbiic9v_2xM3WubXW8P4sfrW8MjBDyceoSTqrBxGK3dXZ4YS5Prf6O7WjLLCkL30fp_OxkwGTV-fWB-qvqMKKeH-fFhDJNkWCxJhsx3Fuarnw8xcCjcr_E27q5-4SSFgodGSSebHNz57VRnKVpJQMvPC1l3uqqYmKciEV3jZPz2GuH1fRiABrhv_vezymj7frxAq2_P5LUflU25J47cPS8qSsEWDKF_0n63Ncp9Mk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در واکنش به حرف پزشکیان که گفته بود «از حق غنی‌سازی خود عقب‌نشینی نمی‌کنیم» گفت: بهتره مراقب حرف زدنش باشه. بهتره رفتارش رو درست کنه، وگرنه بقیه کشورش رو هم در اختیار می‌گیریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/129561" target="_blank">📅 17:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129560">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
نخست‌وزیر قطر: ما شاهد فداکاری و تلاش‌های بزرگی از سوی ونس، نخست‌وزیر پاکستان و وزیر امور خارجه ایران بودیم.
🔴
آنچه امروز در این نشست رخ می‌دهد برای امنیت منطقه و جهان اهمیت دارد.
🔴
نشست امروز تنها آغاز راه برای تحقق اهداف است.
🔴
این فقط آغاز است و ما برای آینده‌ای بهتر برای منطقه‌مان تلاش می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/129560" target="_blank">📅 17:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129559">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaKnOPNrGGT3vXL51UqFuKgF609OcpC6deGwJhUOjZTa-pP1dv6IhDHnM1d3ZUkEE6LcUzLucWsvzy5n3hsx6wX7tYSx3HEEQ5VVtZMkQn7cifgVch9KULK4JSUgHnrWavN2uwBqtI-grhm6sFcyn0lw3Pe9eZD1RafKGqg0aSUP7E2oPBsnuh_phESuPrGDoSl6gHlO0j-E6b0jcPKXW9X4MWTGP7DVxZlN6DUOTZHp_Z9aL-Wr4EZNx18rMotOnj3id4rBNVhOM5FQPr8xsQ-Eqwbj0iSgJ23RQ4dw9auBA39Rg5AItNxEQLOwcx5-PEWw8vfraJj5zdO0cXom5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ :  ایران باید فوراً جلوی دردسرسازی نیروهای نیابتی پردرآمد خود در لبنان را بگیرد. اگر این کار را نکنند، ما دوباره به ایران ضربه سختی خواهیم زد، درست مثل هفته گذشته، فقط شدیدتر!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/129559" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129558">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b4fe6074.mp4?token=BRd-Oz9yCd97O0RS-3jkQK7DRsP4ENFBaMQMWoKjJqCYXAXt5aKCyiLRD4cQ0mxOrr-q5R7VcPk_77IklJbR4Ap597zh5Ws8dkVxf7U4gfxHuEfvwOiH7jHaSv7axbvI5_Oz7ZUmXd82XR7XXys3-67b6-KkOON6QfnKSf8c4leEm6EoB3OmrrY3oAfDNwBi8X331CAQOvjPSNsORnBj6uDO5Dx78PTIV-m0yE2vu4t2fgmK3p3azFSg5pFR2FWycyqzhKBavv2r4QlWrt2bOOuxY_XJBbxyanGTJvmrPLL7Eb_q8nG_VnC7U3Pwj8mOY1TT_TIzcI2kQzM5gYPdQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b4fe6074.mp4?token=BRd-Oz9yCd97O0RS-3jkQK7DRsP4ENFBaMQMWoKjJqCYXAXt5aKCyiLRD4cQ0mxOrr-q5R7VcPk_77IklJbR4Ap597zh5Ws8dkVxf7U4gfxHuEfvwOiH7jHaSv7axbvI5_Oz7ZUmXd82XR7XXys3-67b6-KkOON6QfnKSf8c4leEm6EoB3OmrrY3oAfDNwBi8X331CAQOvjPSNsORnBj6uDO5Dx78PTIV-m0yE2vu4t2fgmK3p3azFSg5pFR2FWycyqzhKBavv2r4QlWrt2bOOuxY_XJBbxyanGTJvmrPLL7Eb_q8nG_VnC7U3Pwj8mOY1TT_TIzcI2kQzM5gYPdQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: دیروز ۱۹ میلیون بشکه نفت خام به دلیل این تفاهم‌نامه با ایرانی‌ها از خلیج فارس خارج شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/129558" target="_blank">📅 17:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129557">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: دیروز با مقامات ایرانی صحبت کردم و به آنها در مورد بستن تنگه هرمز هشدار دادم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/129557" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129556">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ: من یک گزینه ۶۰ روزه دارم؛ بعد از آن می‌توانم هر کاری که بخواهم انجام دهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/129556" target="_blank">📅 16:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129555">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
تسنیم: هیات ایرانی با عکس مشترک با هیات آمریکایی مخالفت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/129555" target="_blank">📅 16:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129554">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
صدا و سیما: خروج خبرنگاران در پی شرط قالیباف برای عدم حضور رسانه‌ها در این نشست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/129554" target="_blank">📅 16:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129553">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
جی‌دی ونس: باز شدن تنگه هرمز و متوقف کردن برنامه هسته‌ای ایران، کارهایی است که همین حالا به سرانجام رسیده. حالا سؤال اصلی این است که چقدر می‌توانیم جلوتر برویم و دستاوردهای بیشتری داشته باشیم. آیا می‌توانیم روابط منطقه را برای همیشه متحول کنیم، یا دوباره برمی‌گردیم به همان روش‌های قدیمی؟ روش‌هایی که دوست نداریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/129553" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
