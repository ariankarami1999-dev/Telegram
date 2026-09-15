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
<img src="https://cdn4.telesco.pe/file/vU0cYvg2ehFajBZI3vdfpz2vtLz407iAWJP-prkxAaFPuRfcmOjf3ZasNAdWKUsIZWylwET1i0NCFNiuPS1n29QNGUHYFKLq4yoXdz-c5JP1uFlwVGqwc0W-uFJgYP7X4U6gZe2ZHqWVqiPhQkUUVtxHN3RQ5ph6mVWxhtOLgpvBACSq2FgFv0K86-SmvEB0L8RuLkbE0Sw058dkdUntaZY03n6AfJMk5JLlk_RA96R4s4-tx-d3cX2XccIs_kUYpEWfId3pn6DV8BgXKqank0ulKemmOJ-ArEwYwyWO5CjufAW-5YKzv7I9GsTXIQoZrye-805k0NYhfwHrUyEI4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 921K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 02:03:36</div>
<hr>

<div class="tg-post" id="msg-147646">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fbd3251f05.mp4?token=I-D_aXYFV4kvu7zJ0t6lEnuoLZUAP7BYx8qhygElL3rx3fkkKw5fMuZPZIfyC9WmgALfBE19VgKaZ8nd4r0jr2yK4sZVGGgwXVn4BabC-UvElCSmKvfdMS3FRrxvA2XMKEhiK4_6oIF8p35adqIiZad-09HKHNHHljEC7HCNG1bzlW_CBisD66cHrdJjU4-Uc6M3SuRZ2vf3S9VdbVRKOfQOVYY5aH5o3RmtHUdJRH13XYTxTI-zLzk4o88vnQ2rWs8Ev-8MBpEQuq9jzi68-ga0FNUHq67xYjYwqSKqEosI8wghfFxqduZVQZUaefORtScsBRUpk3xq0XYNPyvhtw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fbd3251f05.mp4?token=I-D_aXYFV4kvu7zJ0t6lEnuoLZUAP7BYx8qhygElL3rx3fkkKw5fMuZPZIfyC9WmgALfBE19VgKaZ8nd4r0jr2yK4sZVGGgwXVn4BabC-UvElCSmKvfdMS3FRrxvA2XMKEhiK4_6oIF8p35adqIiZad-09HKHNHHljEC7HCNG1bzlW_CBisD66cHrdJjU4-Uc6M3SuRZ2vf3S9VdbVRKOfQOVYY5aH5o3RmtHUdJRH13XYTxTI-zLzk4o88vnQ2rWs8Ev-8MBpEQuq9jzi68-ga0FNUHq67xYjYwqSKqEosI8wghfFxqduZVQZUaefORtScsBRUpk3xq0XYNPyvhtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امشب عادل فردوسی پور از پوریا پورعلی بازیکن پرسپولیس سوال کرد که میدونی چطوری مهدی زارع تو حموم پاشو بُرید؟
پورعلی برگشت گفت آره بابا، من با مهدی زارع، دوتایی باهم رفته بودیم زیر دوش
🏳‍🌈
عادلم هر کاری کرد نتونست جلو خودشو بگیره و ۳۰ ثانیه فقط خندید
🤣
@AloSport</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/alonews/147646" target="_blank">📅 02:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147645">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فوری/درگیری‌ موشکی در نزدیکی تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/147645" target="_blank">📅 01:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147644">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">در عجبم عرزشی‌ها طلاهاشون میدن تا خونه‌های لبنانی‌ها ساخته بشه اما وقتی میگیم همون پولو بدید تو سیستان و بلوچستان خونه بسازیم میگن وظیفه دولته!  [@AloTweet]</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/147644" target="_blank">📅 01:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147643">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQ4REF5-tDLL38OQwR0MGRhe8kBYFQdlDr5lcYQ449wYL7LkNFr0Jas1vOLc5rK4_ET3Dt4Ti003DM0PtyjUKwG3TgjbHrV0mXI8yrBozKOOfsV9f4flWBe2RjLplTTkdLhIdmsNpaH3c9dr_fN_FV_Q2VfmuGvp6jy1xPBZ2srUdSn_1dReAHbUyR5rTvx6hUOyCSgkkUQwVuRZ9P3Wk_sphKiCOaM93HO0_OROav2bWB5ZnGppRSiM_anRGucN0s6dTtr5jZw-Oh8K33tDNB-gehe8sWbaE_8mb139XhRAiBHnEytJpsl0xYYfvEUzn6RF6gZEpbG3ZGCK8wlfsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجلس نمایندگان آمریکا با رأی ۲۳۲ به ۱۴۷ و ۴۷ رأی «حاضر»، طرحی برای آغاز روند استیضاح دونالد ترامپ را کنار گذاشت؛ بنابراین این طرح پیش از رسیدن به رأی‌گیری درباره خودِ استیضاح، عملاً متوقف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/147643" target="_blank">📅 01:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147641">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏
👈
جی دی ونس: ایران تا زمان انتخابات میان‌دوره‌ای آمریکا، به‌تدریج کنترل خود بر تنگه هرمز را از دست خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/147641" target="_blank">📅 00:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147640">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏
👈
جی دی ونس:
ایران تا زمان انتخابات میان‌دوره‌ای آمریکا، به‌تدریج کنترل خود بر تنگه هرمز را از دست خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/147640" target="_blank">📅 00:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147639">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
گویا صبح سه شنبه جنگنده‌های آمریکایی وارد حریم هوایی ایران شدن و برگشتن و برای همین بود تمام اماکن نظامی تخلیه شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/147639" target="_blank">📅 00:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147638">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20a028d46d.mp4?token=Gj5iCXhmf4fb2BtIoqdHNocmAXses0xLZ-sOU74-WO5Bp2xRX85JKFCyqedIkdZWo1l48-4HNSlKA2d3bFYRh56uyCvKBox-QuGx-f3VMk2etgqiuR4fAuOo2HakCYKd3-zFWT-ZilXbHchZnCoy04RJvoICRbx3zdtSurES0hqRCJGnhh94j7PesvjD0WYVJ0AHJND0dOeFOyc773gvJ8HpR7N3OKN64hqOZJ_ESQ3snXVUd4yK80XDXcyvKSCW3wZTgCBBqWBCVvLJXb5o-cT9izA5Hd3V2rSIeHtCudPHn5nXAF45p07nZvpo0jZ42ZKr7rZfWO3oNMo1YHE1bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20a028d46d.mp4?token=Gj5iCXhmf4fb2BtIoqdHNocmAXses0xLZ-sOU74-WO5Bp2xRX85JKFCyqedIkdZWo1l48-4HNSlKA2d3bFYRh56uyCvKBox-QuGx-f3VMk2etgqiuR4fAuOo2HakCYKd3-zFWT-ZilXbHchZnCoy04RJvoICRbx3zdtSurES0hqRCJGnhh94j7PesvjD0WYVJ0AHJND0dOeFOyc773gvJ8HpR7N3OKN64hqOZJ_ESQ3snXVUd4yK80XDXcyvKSCW3wZTgCBBqWBCVvLJXb5o-cT9izA5Hd3V2rSIeHtCudPHn5nXAF45p07nZvpo0jZ42ZKr7rZfWO3oNMo1YHE1bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند:
گرونی شده؟بدبخت شدی؟ به ما چه؟ یاعلی
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147638" target="_blank">📅 00:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147637">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری/گزارش انفجار در قشم
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/147637" target="_blank">📅 00:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147636">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترور آلارم : لیست ترور بروز شد
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/147636" target="_blank">📅 00:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147635">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سی‌بی‌اس گزارش داده مصر پیشنهاد حوثی‌ها برای مذاکره مستقیم درباره ترتیبات جدید کشتیرانی در دریای سرخ را نپذیرفته است
🔴
قاهره نمی‌خواهد وارد چارچوبی شود که بتواند به حوثی‌ها یا هر طرف دیگری امکان ادعای حاکمیت یا اختیار بر تنگه باب‌المندب را بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/147635" target="_blank">📅 00:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147634">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ونس: جنگ چند ماه دیگر وارد مرحله‌ای کاملاً متفاوت خواهد شد
🔴
ما نمی‌توانیم آینده را پیش‌بینی کنیم، اما فکر می‌کنم ترامپ درست می‌گوید که این درگیری چند ماه دیگر وارد مرحله‌ای کاملاً متفاوت خواهد شد.
🔴
من قطعاً درک می‌کنم که مردم آمریکا تا حدی بی‌تاب شده‌اند، اما اساساً آنچه اکنون در جریان است اینکه ایالات متحده در عملیات تهاجمی درگیر نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/147634" target="_blank">📅 23:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147633">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: واشنگتن گفت‌وگوهایی با پکن در مورد ارتباطات مالی با تهران داشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/147633" target="_blank">📅 23:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147632">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/us5W_wIk-J9f9_HP2xNvU_-nDK-OgWOCDfz-SKIpTMFTrxh3oCso9oeJ7E8FC92n1SbaDQvUCoCd7fPdfWffkTlJK2edRZrT_AyzJsiL4KSDZUu5MfTLlN5Ob__y0lXsM8QzcwiC0RE9dy5okhp2ej755a7Kmw70Xu31JOe1btxkmFr89fpCptvKkLTxtrfd_zblA2i9KCL7rSqUuliH6tgvMIAKGuKiUoAtw5c3CW0fRedBLBrvYv9SdkOgRHbiBKRxkrT5i8VAHLPwFyICrVfWP2cyAxEFuy8ZZ_dWk8HVFydUTYGT4rJPrpxKtDnHbMKm6g859pwg79Xs7sYOjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور اوکراین تأکید کرد که اوکراین به بمباران پالایشگاه‌های روسی ادامه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/147632" target="_blank">📅 23:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147631">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
نتانیاهو و کاتس در بیانیه مشترک: ارتش لحظاتی پیش فرمانده تیپ رفح در جنبش حماس را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/147631" target="_blank">📅 23:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147630">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که نیروهای آمریکایی، به عنوان بخشی از محاصره خود علیه بنادر ایران، مسیر 103 فروند کشتی تجاری را تغییر داده‌اند.
🔴
این تعداد، نسبت به گزارش روز یکشنبه، ۲ فروند کشتی بیشتر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/147630" target="_blank">📅 23:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147629">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری / حمله یمن به تاسیسات آرامکو
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/147629" target="_blank">📅 23:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147628">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adb7db192.mp4?token=dW4oZOsYO7xfvsdclPdf13bAlx9BkXeNFQpS6MWiRbAQUp5Ug6OO8xPXlQCKtl8qj9uA0w_tDJ2F9FmShYCFtnyZCPYXPQZEgk-qR3rAk8593NZADwgu1MjY99xFKGr-kfFI4BggxYtSo9_Dbcdu-Fd1j4Zv8yWko1d-SjXeWOvfGj7Z4fzpEIWKb_hR5OCaempyo9eXss2wDAbrczty1PE4xEJRmX7ixQgBgQTAL9Ff1J8t_NExpiAYkyUXz2-7RLpxnN4rSnXoYXr78KzMngUaNLdYW-l7ZQ3330ST34n7tAsIiqOwrAdij2KGIUBmpZ98lE9DWGIofCYGv6zQkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adb7db192.mp4?token=dW4oZOsYO7xfvsdclPdf13bAlx9BkXeNFQpS6MWiRbAQUp5Ug6OO8xPXlQCKtl8qj9uA0w_tDJ2F9FmShYCFtnyZCPYXPQZEgk-qR3rAk8593NZADwgu1MjY99xFKGr-kfFI4BggxYtSo9_Dbcdu-Fd1j4Zv8yWko1d-SjXeWOvfGj7Z4fzpEIWKb_hR5OCaempyo9eXss2wDAbrczty1PE4xEJRmX7ixQgBgQTAL9Ff1J8t_NExpiAYkyUXz2-7RLpxnN4rSnXoYXr78KzMngUaNLdYW-l7ZQ3330ST34n7tAsIiqOwrAdij2KGIUBmpZ98lE9DWGIofCYGv6zQkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فردوسی‌پور: درخواست وحشتناک قلعه‌نویی؛ از ماهی ٣ میلیارد رسید به ماهی ۱۵ میلیارد! چیزی به نام قرار سفید امضا وجود ندارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/147628" target="_blank">📅 23:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147627">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رویترز: بارگیری نفت عربستان از بندر ینبع در دریای سرخ متوقف شده است
🔴
این امر باعث شد امروز قیمت هر بشکه نفت حدود سه دلار افزایش یابد.
🔴
ریاض به خریداران اروپایی اطلاع داده که تحویل نفت خام در پایان سپتامبر را لغو کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/147627" target="_blank">📅 23:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147626">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری / گزارش ها از ترور یکی از اعضای ارشد دفتر رهبر حوثی های یمن خبر می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/147626" target="_blank">📅 22:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147625">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f471b636.mp4?token=E46OHsuyLjv3CrJn2XqEK_v_B6XVMg7Tyvzsmc0Un1o76HZh0EyCiKh2TyTlFGGJ6nj32C8sWFA5Rw1u-oa2Isbcp8H12mcmbIJqx5h0a02ioxjoWgInzSPIsKb-BYGlttw8MYZ34YYB9mZRcNUaFmNInFucBZ7dEW2g3JK2oaNhIt1bRjP14b_ccgnzRdEp-n-KofeG797l9KxmMq65Ojyz-BBWL_VAhvuTdlyWqPtFPYWfGxcE6xxhwL5t56WreWQksABqBwTDJz0xM1p9KKjtlk000YqI2W2BPZlDbv-6Rx8GgsipxMcxI5IuAdD-mn0N6wusoyZIkGUU1Mx0EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f471b636.mp4?token=E46OHsuyLjv3CrJn2XqEK_v_B6XVMg7Tyvzsmc0Un1o76HZh0EyCiKh2TyTlFGGJ6nj32C8sWFA5Rw1u-oa2Isbcp8H12mcmbIJqx5h0a02ioxjoWgInzSPIsKb-BYGlttw8MYZ34YYB9mZRcNUaFmNInFucBZ7dEW2g3JK2oaNhIt1bRjP14b_ccgnzRdEp-n-KofeG797l9KxmMq65Ojyz-BBWL_VAhvuTdlyWqPtFPYWfGxcE6xxhwL5t56WreWQksABqBwTDJz0xM1p9KKjtlk000YqI2W2BPZlDbv-6Rx8GgsipxMcxI5IuAdD-mn0N6wusoyZIkGUU1Mx0EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو این خانوم فضول حسود که در مترو داره به بی حجاب ها تذکر میده در فضای مجازی وایرال شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/147625" target="_blank">📅 22:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147624">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
صداوسیما: خلبان نجات یافته ای که آمریکا باهاش مصاحبه کرد هوش مصنوعی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/147624" target="_blank">📅 22:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147623">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
تخلیه فرودگاه ورشو به‌دلیل تهدید بمب‌گذاری
🔴
فرودگاه بین‌المللی ورشو، پایتخت لهستان پس از گزارش بمب‌گذاری تخلیه شد.
🔴
نیروهای امنیتی و پلیس لهستان در حال جست‌وجوی پایانه‌ها هستند و جست‌وجوها ادامه دارد.
🔴
هنوز مشخص نیست چه کسی این تهدید ادعایی بمب را گزارش کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/147623" target="_blank">📅 22:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147622">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
در اقدامی بی سابقه عربستان سعودی اعلام کرد به دنبال حملات حوثی‌ها و ادامه دار بودن جنگ با یمن، ارسال نفت به اروپا را متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/147622" target="_blank">📅 22:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147621">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/147621" target="_blank">📅 22:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147620">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/147620" target="_blank">📅 22:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147619">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQm0qzx4ONCTH3WPYzK5ecrElUP--MWmcoEGFaXlofYj1l149--T2AEtDAKmqZmkf5m3P4DkXSU5zAzLjUM8ZJJlmb6uk_OEXtEBCJO7MfwGZP5M1PM4W3mttIRokyAuUmKtopxOGJUpl-PLyuByeJxmOhBIn7iUORLkWRbJHRh7Rqxv1n7iPvUZeoLKFnPzvD_Wr7mIVfTMtbAoCsCBNAcDGDIhamU4Cr7dSA2iiuTT9w4TQ01iZOB6YdoUhGuoqRyrNdWV9LyFtsRUssAsqwjFHbYLsBu5Bg-0tBuYkX-2aS1YuSvKrr9obsXcLZr9qDxummb1PlddHghkpgR4qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعتی پیش، ۱۲ فروند جنگنده F-16 خاک آمریکا را ترک کرده و احتمالا عازم خاورمیانه شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/147619" target="_blank">📅 22:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147618">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
رو دلار و طلا سرمایه گذاری کردید؟
آره
✔️
نه
❌</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/147618" target="_blank">📅 22:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147617">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
دفتر بودجه کنگره آمریکا: پنج ماه اول جنگ با ایران ۳۸ میلیارد دلار برای وزارت دفاع هزینه داشته است
🔴
هزینه این درگیری ماهانه بین ۲ تا ۳ میلیارد دلار خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/147617" target="_blank">📅 22:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147616">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
تعلیق پروازهای لوفت‌هانزا تا ۸ فروردین ۱۴۰۶ و ترکیش ایرلاینز تا ۱۰ اسفند ۱۴۰۵
🔴
آخرین وضعیت تعلیق پروازهای ایرلاین‌های خارجی به ایران، بر اساس اعلام این شرکت‌ها
🔴
با توجه به تحولات منطقه، احتمال بازنگری در این تاریخ‌ها و ازسرگیری زودتر پروازها وجود دارد؛ با این حال، هرگونه تغییر در برنامه پروازها منوط به اعلام رسمی شرکت‌های هواپیمایی خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/147616" target="_blank">📅 22:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147615">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZeyeA2Ovq_08hldEY4uH6hqE-6xrNh48xJeS7hKWrAmSk59Oj5o--3eHqNpVDEE4v00CpAr1W7Wg44eS4m868z6elTIeM15du6WH-dU_ack418umcYDZ-qTfygFJVQKvJeme6dGyOyb1asDc564ycJclZHwv012zbnyvW5YykRIwD5G0xA0HVRsuprUBHmjDBFurz446OJdgRXavj-PgZdJaidAoKUFjm7bqlRy9MIZssX0LPrgdYzOAc3_iXTfgRSCmiwQaSroDhEVrWaLK5c5ruWsSkzcfPOV_qQ6lvmzIN-IW-VXTUsxN2o3-jpLHztXIHTZ_1niHgfbbEj68Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : همه می‌دانند که اداره فدرال پلیس (FBI) تحت رهبری "جو بایدنِ متقلب" کاری را که باید انجام می‌داد، در مورد فرد دیوانه‌ای که به من در شهر باتلر، ایالت پنسیلوانیا، شلیک کرد، انجام نداد. تا زمانی که من در تاریخ ۲۰ ژانویه، به قدرت رسیدم، بیشتر اطلاعات مربوط به این حادثه، یا مفقود شده بودند، یا تغییر یافته بودند، یا تحریف شده بودند، یا به طور کامل از بین رفته بودند.
🔴
اطلاعات جدیدی به تازگی کشف شده است! چرا این اطلاعات قبلاً دیده نشدند؟ این تماماً یک توطئه از سوی دموکرات‌ها بود، برای اینکه مرا از انتخابات کنار بگذارند، که این توطئه شکست خورد.
🔴
"کریستوفر وری"، افسر پلیس فاسد، باید بهای عملکرد خود در این تلاش برای ترور و همچنین اظهاراتش را بپردازد. خداوند آمریکا را حفظ کند — آمریکا را دوباره شکوه بخشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/147615" target="_blank">📅 21:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147614">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fK9WX2Jdbljz27lfU9N9H3c4rskTeTf_IvvsuNXdsLooP2aYqOedK2YPeyBvg7S1mNvvj_ak1SoEapkUI7s6ZfXeh9koCNBmDB1n_HtYOf1CT6ynadhR0Z1_ZUp09p-CwDG2cYhHiOY0MKpTlJdqSMVIL1D0Az0WXs1AXhBkejb7aTbb3LOEzb--GWCRRhpSwjP9nHSSy2QHbgWfSMGJZJz7_TDM52rnLGulcgHsiNwuSvqOi1nQ3eipUGDPmT-EVFwLYrEcMP7_8thGaD2o-_TIHWGSIaatiOHud5SDb8MZgfyej8Bh3hLrxb81E3Rf4RzszG0DNdu9CEyeTPNOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تقوی نیا:
امروز تا آستانه جنگ رفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/147614" target="_blank">📅 21:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147613">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIsPE0zDZdkDpuIHcmN5neZUNjN2a-OWNDTijYAb7s54qzgu8y_o3_FjUFzlX-Do7wK1utoefkrNkl90TzY-_lfabZvYBfj05B8Y9-63bO4HQZm8cqa1EoaLPWVxVQTzjB2BiOahDldBatK8ZqKHGnJdKeTJy6dIp4ALCPCzke7vN7f2DIxXbgnLhtuUj5VZJsQkj6OkLuJawuELe-HBdGNgab4y49GhoyBko_0LbPYJ2E4oCqP1MWTS7leoqtQaPT2hBIWCeVTmYzL9AHRtHq8VKqK3aT4fNzHrUhCMIMJS_rOe_oF2DyOSOZurxrui5AOTrTn3egsaEyfLkrhkQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمریکا به اسرائیل چهل هزار بمب ۲۰۰۰ پوندی می‌دهد!
🔴
واشنگتن‌پست: دولت ترامپ در حال تدارک فروش ۴۰ هزار بمب سنگین (از نوع MK-84 و BLU-117 با وزن ۲۰۰۰ پوند) به ارزش ۲.۸ میلیارد دلار به اسرائیل است.
🔴
این بزرگترین معامله تسلیحاتی از این دست در سال‌های اخیر محسوب می‌شود. این‌ها همان بمب‌هایی هستند که بایدن پیش‌تر به دلیل نگرانی‌ از تلفات غیرنظامیان، ارسال آن‌ها را به‌طور موقت متوقف کرده بود.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/147613" target="_blank">📅 21:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147612">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">قیمت دلار منفجر میشه
‼️
این پسره یه تحلیل عجیب گفته
😐
👇
https://t.me/+jkJGKa0y56liZGZk
https://t.me/+jkJGKa0y56liZGZk</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/147612" target="_blank">📅 21:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147611">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMlFTviMNHPzE8l6qAHR4xKB2u2RAeyBFcPdwBbfQsiyoro1OPaT4l_W1iYm_D0E2QTf2s0ohwOhtyeZ3EoM7GAx5IAYUE-zPKAnT47Bm8qLUM89OlGv1rHL7WzPuaVQD__5wZGEPmaYwx9End1SYWFhS09I4pYDEpmZXqUAZzGN5O8E9U8bj6DllNnxpx7AM1L0htOQwD_YguslxdngDANYx0e2V9V9BXYZrBXY_8_PmVA09TLnQGiCF2m6uT6-RnAXihB19Y0Rdn98_n9NGDXQskr5GScui53I00b3x7YGekLIABeHjHDtwlnP0RJlwNyJXB9duo1-LRM9i90jXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت ۱۰۹ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/147611" target="_blank">📅 21:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147610">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
نیروی هوایی ارتش: سه خلبان ایرانی عملیات العدید اسیر هستند و قطر باید پاسخگو باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/147610" target="_blank">📅 21:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147609">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری / گزارش سه انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/147609" target="_blank">📅 21:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147608">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
روزنامه کان اسرائیل: موساد و ارتش اسرائیل از طریق ارتش آمریکا، اطلاعات بسیار گسترده حساسی از حوثی های یمن را در اختیار عربستان سعودی قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/147608" target="_blank">📅 21:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147607">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
حمله هوایی نیروی هوایی اسرائیل به شهر نباتیه الفوقا، در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/147607" target="_blank">📅 21:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147606">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وزارت امور خارجه ایالات متحده:
روبیو در تماس تلفنی با همتای عمانی خود، حملات اخیر ایران به کشتی‌های تجاری و کشورهای منطقه را محکوم کرد
🔴
روبیو، وزیر امور خارجه، در تماس تلفنی با همتای عمانی خود، از نقش مسقط در کاهش تنش‌ها در منطقه تقدیر کرد.
🔴
روبیو بر تعهد واشنگتن به تضمین عدم دستیابی ایران به سلاح هسته‌ای و آزادی دریانوردی در تنگه هرمز تأکید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/147606" target="_blank">📅 21:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147605">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvD4gnwQqEYgyoJ0xWvKvK0zP8hEPSLP_pz3dnGTXPsT9NGpk3uCNcZgqMcvhzYwnDIoq6bzEaQdZMeE8XlC5oj8EzRG1sjOpYPPcsVhFvtpK5qkTHCzkIg-ScZl9_IH1Q8EP7Qz26rwQD9vsTUjkv8lCh1XiWuR8dRXFLbfeY71twQ4FtYPdNNS6eyEPbCET0bKgIjdnbQgByBGGfsYBPUcH9vRuLj6o6xbT_lPnKqp90y3AWmGo1J0aNvr5inSbbGhfG68VAE0nPfvYd37lw3fRJagqpiZ3p0yZOtGHpHabMdu8ZvXpbw_2RKOPW9Nfx5Yyya06-QjFxlMDdWEyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / سفیر اسرائیل در امارات:
کویت ممکن است طی ۴ تا ۶ ماه آینده به توافق ابراهیم بپیوندد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/147605" target="_blank">📅 20:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147604">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1474c81cb6.mp4?token=B3kucUcRNxb_tL_AvHN09uqg3z5DXbaLxu_7bmB5KHrT1oL7G3KMMaV4gBibAvZyr-5x5y4ex3hfGza2vy5lS8EnnxOPbUU4A4MX2l4hXksV9bYrjSyum1ARrlgSRb0sI5XFm-LC1jcaedCvEDB1K_sg8RvhISzgMpTurk8JVarWODvpLMz3qPKTicTAz2al1wP0doozM0Oe_8_gsz5F5qzBfupkguzUH3QUc8Jc-JVqv4SdmzNusOoSEAJxvmeQ2cFPpeTg-WtkTlwkVGimSHiUAa1-jDMcwjiL0Ol5EJYwEP2-mdDuyfsD5yT2pNNnUpeY7FUkHWqsnIn_wRSlbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1474c81cb6.mp4?token=B3kucUcRNxb_tL_AvHN09uqg3z5DXbaLxu_7bmB5KHrT1oL7G3KMMaV4gBibAvZyr-5x5y4ex3hfGza2vy5lS8EnnxOPbUU4A4MX2l4hXksV9bYrjSyum1ARrlgSRb0sI5XFm-LC1jcaedCvEDB1K_sg8RvhISzgMpTurk8JVarWODvpLMz3qPKTicTAz2al1wP0doozM0Oe_8_gsz5F5qzBfupkguzUH3QUc8Jc-JVqv4SdmzNusOoSEAJxvmeQ2cFPpeTg-WtkTlwkVGimSHiUAa1-jDMcwjiL0Ol5EJYwEP2-mdDuyfsD5yT2pNNnUpeY7FUkHWqsnIn_wRSlbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر ارتباطات و فناوری اطلاعات:
فیلترینگ و نظام محدودسازی به کیفیت اینترنت آسیب می‌زند/ فناوری رویکرد منفعلانه را رد می‌کند، باید از ظرفیت آن استفاده کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/147604" target="_blank">📅 20:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147603">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwZQ0oGwFU-_K12vJ_HpQaByWdM9aTTWssv_bzPx2JIfkBXv9_sBoE8RO7n-KGhaQxfl810BlsHvqTckuvfejt0IIcjpJxrPgRlQaiWfvNgVxK7Of9OzPLCdE6QXcFmTbNtqT0EUg2Asi0h6H7iVGNWe268uSNaKYQui9Uzm7HZ20MnSt2YbKbxrzcys6IWzSywJDT6FHpqxGaj1npBFmjHmf6Km1PNmYZP-Yqt-DedA12jexO2mdv5-SVyfwkUV0Njn_s4G-bBPR9lrF35jQXsrzCNbggyIiouet1xzh4XSlXRB-32-CcJyoOZWqMp4Fn21cYw2YChPZOMn14Ladw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: ارتش آمریکا اسکورت نفتکش‌ها در طول روز را آغاز کرده است
🔴
پیش از این روال این بود که نفتکش‌ها شبانه از تنگه هرمز عبور کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/147603" target="_blank">📅 20:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147602">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f75bf3da.mp4?token=DDvtX8AgH-TCywBSfnkb9IpOKNX79yUTLrM8rl-TQ6m7qO52Zchzn_fN3Pl4XvWqOtLIzo3x8WI6qXCbuClSKUrZxUzp-nyC8jgHUvrI0Y10j-jjKBiUjHfAyklaexmuml6yk7QH1Zj1YWzG4oyL0tm3k4pYLZhe2oYoG4RpuuLKpHUB8uxRUHoG_h1rVoZxvq0X7f7DtdMDvfmyOAouvYkp4LH_AvNGF7jViGXw4ZOrETj62YrimiO6e8_83eLfTG3UOVHOYLY-dILJ3Zbyt7B-c-Qc5nTPjPdnsmDVd3gRl5QisDeSAv6Ox7MKMDcJ3NAHdPf7QiDkiJxv5zNDZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f75bf3da.mp4?token=DDvtX8AgH-TCywBSfnkb9IpOKNX79yUTLrM8rl-TQ6m7qO52Zchzn_fN3Pl4XvWqOtLIzo3x8WI6qXCbuClSKUrZxUzp-nyC8jgHUvrI0Y10j-jjKBiUjHfAyklaexmuml6yk7QH1Zj1YWzG4oyL0tm3k4pYLZhe2oYoG4RpuuLKpHUB8uxRUHoG_h1rVoZxvq0X7f7DtdMDvfmyOAouvYkp4LH_AvNGF7jViGXw4ZOrETj62YrimiO6e8_83eLfTG3UOVHOYLY-dILJ3Zbyt7B-c-Qc5nTPjPdnsmDVd3gRl5QisDeSAv6Ox7MKMDcJ3NAHdPf7QiDkiJxv5zNDZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اولین تصاویر از سوپرنفتکش الگایا که در اثر برخورد با مین‌های ایرانی منفجر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147602" target="_blank">📅 20:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147601">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoLlbqLVWOpxjKxxc6qUws_aAe4sCVw8FWwISCkPKTy9AYSwjTNqNYzm3ygEbHTsj1nDeW7aBiq2_4lwbG4MCaSjxKjvrk3pPyUyTpzV-m9vQCAOrsxH2JJrTQCNUr8o-zfo63q-UJpau36OpSYdWH7JlCYGuoc-Ha6aUe_NGqxCCz6RCFhnB_BWK2D7jIt2hvgvtxD3tqb_cIyA6tFcbqJ0PFTrbZ_QdEOCjU2Gtobg841LlhbWBQBF8DGyCL7qkEKABXuW3rqzpy-icFv5cxpwizf9aPr8O20zalOJfG9mkn1MHyRFK1ni92OFiTn8MWROVQ7aJRqrKJAmIUloAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی : در زمان مناسب میزان واقعی تلفات نیروهای آمریکایی را افشا می‌کنیم
🔴
ادعا: ایران بی‌دفاع است
🔴
واقعیت: صدها پایگاه و تأسیسات نظامی آمریکا در هم کوبیده شده و ده‌ها فروند هواپیمای آمریکایی به آتش کشیده شده‌اند. (منبع: پنتاگون)
🔴
این فقط مشتی از خروار است!
🔴
در زمان مناسب میزان واقعی تلفات نیروهای آمریکایی را افشا خواهیم کرد.
🔴
و روسیاهی برای آنها که به دروغ ادعا می کنند ایران بی‌دفاع است خواهد ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/147601" target="_blank">📅 20:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147600">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
آمیت سیگال خبرنگار کانال ۱۲ اسرائیل: تماس‌ها و رایزنی‌هایی میان اسرائیل و عربستان سعودی، از طریق فرماندهی مرکزی ایالات متحده (سنتکام)، در جریان است و هدف از آن، ارائه کمک‌های اطلاعاتی به عربستان برای مقابله با حوثی‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/147600" target="_blank">📅 20:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147599">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XF8fipGIz1OaLw_JMovHavjU5cnxBzO17vMPIHyt8r3vM67jeqDCiG7BT1cwsPdE5u8qiVQPOctvf8MtAVapgC8xMxD9BcSPk4szBDsk9LfaPQ4IMB0Jgr3PYSxtg6gqBQndSET2zsP4Y3G2znMH98hRN1NfLM6O-GNjEkwx6-vNcx5cl3zTWqOdh48jB9RIKX9fBWeaCDL1SiyP6ZAkxwGnHthS0D0Y-UKGcA1PQHTz6FqWlvyNf6Sot9pXnP-T8ZX3jaNnL30p1FcT8dXEnWtqgztcMd6tyf57mxatOf4T1Sm_6Dg0qnZKI7N_D3I88n5AyrxwAue8GVcz81M1bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: فرماندهان نظامی آمریکا، اسرائیل و کشورهای عربی در حال برگزاری نشستی محرمانه در رابطه با ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147599" target="_blank">📅 20:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147598">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658a596829.mp4?token=vIENp4b5FUopHYkEm_KLYUSSnfapyi4nA5OGrI30yclwTGjIS9yJdiBK1UdQiPqjZ5mC4W3TliqFUK-ROFkmv9L82gVgnrpYDZMBN-YHoF8yallDv1vjTFJQMx2yarZTFKD2-w8ylqZk9BLHUt1-1caPjxkdn3IRX34DEujjSQzjRu9JSyML1rbrtRfJsUF5nMdY25_rCwkE2EzyB7_PpNh0uIs6sTdbzHw4pxjDEbem5CmiQdWp-6mbkPc7dpNtA_Oq5lRVr2bctLc62h7ajUrU3UTyf0sdhPXelUqQMIKVhzM6Ex_9HCpvcyZ3BEG5Ii77cFyvM1tQHqwGRCe-XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658a596829.mp4?token=vIENp4b5FUopHYkEm_KLYUSSnfapyi4nA5OGrI30yclwTGjIS9yJdiBK1UdQiPqjZ5mC4W3TliqFUK-ROFkmv9L82gVgnrpYDZMBN-YHoF8yallDv1vjTFJQMx2yarZTFKD2-w8ylqZk9BLHUt1-1caPjxkdn3IRX34DEujjSQzjRu9JSyML1rbrtRfJsUF5nMdY25_rCwkE2EzyB7_PpNh0uIs6sTdbzHw4pxjDEbem5CmiQdWp-6mbkPc7dpNtA_Oq5lRVr2bctLc62h7ajUrU3UTyf0sdhPXelUqQMIKVhzM6Ex_9HCpvcyZ3BEG5Ii77cFyvM1tQHqwGRCe-XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند درباره لاله مرزبان، بازیگر برنده جایزه جشنواره ونیز: بازیگری شیطانی است؛ خاک بر سر مسئول بی‌غیرتی که به او مجوز بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/147598" target="_blank">📅 20:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147597">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
قیمت نفت: ۱۰۸.۴ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/147597" target="_blank">📅 19:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147596">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: «اظهارات صریح و بسیار رو به جلویی» از سوی امارات درباره قطع منابع مالی ایران مشاهده کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147596" target="_blank">📅 19:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147595">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d6f89f5b.mp4?token=dkdDO-OL1V3TAjMaRQcW96MkSjoFROt-Xa3amwhfxKZGRUYlghNGNQvgQpeKI-f7PQoX83kcw7Y5Nr_D8XiBaaxh6RmDHN0IfRARsMmHcewL5nJTRyMeMajBSaXo9gOcKmmTcCYqB9mcLV__drz7GgJw6h0RmGqJ1jC_TAoRWcymbCdqmvsWB0ePR4pyGiYl6drgbzM9T0J3nbtzFmYNqoLx_HUwqoimGITrDuLo4V6_8qtn8PPm9QQQlpvlt9BqXd5-2tdlP9EW68bUD7rWKReHD2QceJPtI14z0I5NFuuoZRdLinP4ey2ddvU9pwgkn7QqKQCjXVmVPHxqAc8Etg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d6f89f5b.mp4?token=dkdDO-OL1V3TAjMaRQcW96MkSjoFROt-Xa3amwhfxKZGRUYlghNGNQvgQpeKI-f7PQoX83kcw7Y5Nr_D8XiBaaxh6RmDHN0IfRARsMmHcewL5nJTRyMeMajBSaXo9gOcKmmTcCYqB9mcLV__drz7GgJw6h0RmGqJ1jC_TAoRWcymbCdqmvsWB0ePR4pyGiYl6drgbzM9T0J3nbtzFmYNqoLx_HUwqoimGITrDuLo4V6_8qtn8PPm9QQQlpvlt9BqXd5-2tdlP9EW68bUD7rWKReHD2QceJPtI14z0I5NFuuoZRdLinP4ey2ddvU9pwgkn7QqKQCjXVmVPHxqAc8Etg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به نظر میاد تجمعات شبانه بیشتر جای مسخره بازی و لودگی شده.
🔴
پای آیفون 18 هم به شعارها باز کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/147595" target="_blank">📅 19:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147594">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExjLmnI0A0spJVJcKEp1WC0beeuryXWLtpS4lUTMxnyU9UkGlq2C6yuaA1W7pzFp6xDS0RDenKmz2Uj-SInR9h31W24-uGTTvqpaDQHC4Uy1EvWia40QU23hVBkw6ybw8IzoAv9AorpFR1CaXiPaQUKSSVsYIHrJ6Q4Z-C6fRnJ9foz4V7MYcE0YVT0uHx_9pvhjZnVwoi_zVnb8RgqAxsvCORbeP0D5zMFQ4tE_HbQoOSxT1uMZBiVT9cnyr6PM6S2NxKjU216bu7-bB3gu5t-Akdc15UksO3c-iSLcH6pO9Cg7rb4c6RST8IijfgMYgjIcrs1-sptRkIegGigFQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال
:
مرکز کندی در وضعیت فروپاشی تقریبی قرار دارد و این وضعیت سال‌هاست ادامه دارد. تکه‌ای بزرگ از بتن و فولاد با صدای مهیبی از سقف یکی از راهروهای اصلی و پرتردد سقوط کرد.
🔴
اگر ساختمان باز بود، افراد بی‌گناه کشته می‌شدند. یک نگهبان امنیتی دقیقاً یک دقیقه قبل از این فروپاشی سقف از آن منطقه عبور کرده بود. بنابراین، او ۶۰ ثانیه با مرگ قطعی فاصله داشت.
🔴
قاضی مجبورمان کرده است که آن را باز نگه داریم، حتی اگر هیچ اجرای هنری وجود نداشته باشد و هیچ‌کس شجاعت ورود به آنجا را نداشته باشد.
🔴
هیئت مدیره مرکز کندی به‌شدت رأی به نجات آن داده‌اند و می‌دانند که من تنها کسی هستم که می‌توانم این کار را انجام دهم، زیرا من توانایی جمع‌آوری پول و توانایی ساخت‌وساز را دارم؛ توانایی‌هایی که افراد کمی دارند.
🔴
من همچنین قدرت و اقتدار ریاست‌جمهوری را دارم که برای انجام کارهای ضروری و دادن شانس قوی به بازگشت به عظمت مورد نیاز خواهد بود!
🔴
به یاد داشته باشید، مرکز کندی زمانی که من مسئولیت آن را بر عهده گرفتم، صدها میلیون دلار ضرر می‌کرد. آن‌ها به‌شدت در حال شکست بودند! این موضوع هیچ ربطی به من نداشت، من فقط آنجا هستم تا کمک کنم.
🔴
من فقط آنجا رفتم تا حقایق را آشکار کنم، به‌ویژه آن‌هایی که مربوط به ایمنی ساختمان هستند. یک قاضی بسیار خصمانه و متعارض (چه خبر جدیدی است؟) به نظر می‌رسد اجازه نمی‌دهد این اتفاق بیفتد و در این صورت، متأسفانه، سرنوشت ساختمان به سوی نابودی است.
🔴
آیا این خیلی بد نیست؟ ما بیش از ۶ ماه را در دادگاه «با بازی‌های بی‌فایده» هدر داده‌ایم. زمان دشمن ماست!
🔴
هیئت مدیره، که متشکل از برخی از برجسته‌ترین و محترم‌ترین افراد کشور ماست، امروز دوباره جلسه برگزار می‌کند. جالب خواهد بود ببینیم چه اتفاقی می‌افتد!
🔴
از توجه شما به این موضوع سپاسگزارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147594" target="_blank">📅 19:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147593">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147593" target="_blank">📅 19:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147592">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1gLIJgPrs7k9i2uLp0RuYabXOLXZErLW2msR7zGJ-5ajcCO8Iina9nMWqZGUmDMJbr6tltod220vuiT1ogxHk6wnYvXNbWMyuZm3eRZpevhkrnV-Ov09JeEikSII0CXH9H76aYVQqu92bjPsqjr3Jiyvi-nzM5MTwB9hJ5cWiJ1DRHONd5Mcb_E7Wu0MRkQ1YiX0_Q8NtIpEeCfXF0NteMPctHr5vJNeMcGqR9KKox5bxkPs1C9N8VsCDQf-X7WJ0DtX18vCj5SMOMBGxhEyTSdY2j9_8dhdlLuBxAzgYflQSKxKGBP0xQcF14fIaqBEDe-74ZoORfMsrcVvQ-HFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همه پروازهای خروجی فرودگاه جده متوقف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/147592" target="_blank">📅 19:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147591">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/789860f816.mp4?token=gC7XTRksSc_T8AARaVwwIAkjvLC4gVLExp73OFO9g6PyMmMNYk8FLYtj1OiVMnJVkuBezoIQyh8dpXcLE10aok1V_mgp1F1wfv1FiQ-eekhhutH0PKrmoDMKgpfbBjqKevMhaLLUxCJztay0dgdjdGyxqU7U1L9V3RIIqAyl--H_iqU6IKWS164meu2X4XS5rH0vJIwirpuxEmTT-_UunLxMxR7_cklGV1tOzMYBbqHA3R8ah8KizMYMnkHCD2UFa7hqNkabmQsdWpIkpfd8M0Jie5_39N5257_FIM8F-7Fai5CpW0oeDaOvWrCSnjWEL1PYHkSE-dqofXvPAY7Azg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/789860f816.mp4?token=gC7XTRksSc_T8AARaVwwIAkjvLC4gVLExp73OFO9g6PyMmMNYk8FLYtj1OiVMnJVkuBezoIQyh8dpXcLE10aok1V_mgp1F1wfv1FiQ-eekhhutH0PKrmoDMKgpfbBjqKevMhaLLUxCJztay0dgdjdGyxqU7U1L9V3RIIqAyl--H_iqU6IKWS164meu2X4XS5rH0vJIwirpuxEmTT-_UunLxMxR7_cklGV1tOzMYBbqHA3R8ah8KizMYMnkHCD2UFa7hqNkabmQsdWpIkpfd8M0Jie5_39N5257_FIM8F-7Fai5CpW0oeDaOvWrCSnjWEL1PYHkSE-dqofXvPAY7Azg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قائم‌پناه معاون پزشکیان:
حساب کردم اگر بنزین ۸۰هزار تومان شود و برق و گاز و... را هم گران کنیم، می‌شود ۷میلیون یارانه به هر نفر داد‌.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147591" target="_blank">📅 19:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147590">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a1a4b63c66.mp4?token=EcXlohSuT32v7ERI7W5b9rjo-cxxkeEL6MS69rxRc5s-ThbxHYj_D4GSazn9YIOTR_p7Ani-PzLco8E7VqEQBTE225Odp8nuMS6yoeFNJkdXR1uMyE-GNEMK4DCcuROuuVV3DX56GpTF4QkxlOd8qxyJkPyg9Q4uJzudZj58X4MwiuU4MyuRI4o8zUD62E_TZ0yly7upvA6YoLolMBY3g9OzttiY9-oBEypqCQnrWFh3K5SI8agQ_ULov_JMc8QKnc0xq27Xl4kM3MxgYlFDVMNrU1SzX5IUOU2sht-ZWLhEoqrW6cOs5Q2xXUOft9TvStSefwYj5UNKS2upmIwfbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a1a4b63c66.mp4?token=EcXlohSuT32v7ERI7W5b9rjo-cxxkeEL6MS69rxRc5s-ThbxHYj_D4GSazn9YIOTR_p7Ani-PzLco8E7VqEQBTE225Odp8nuMS6yoeFNJkdXR1uMyE-GNEMK4DCcuROuuVV3DX56GpTF4QkxlOd8qxyJkPyg9Q4uJzudZj58X4MwiuU4MyuRI4o8zUD62E_TZ0yly7upvA6YoLolMBY3g9OzttiY9-oBEypqCQnrWFh3K5SI8agQ_ULov_JMc8QKnc0xq27Xl4kM3MxgYlFDVMNrU1SzX5IUOU2sht-ZWLhEoqrW6cOs5Q2xXUOft9TvStSefwYj5UNKS2upmIwfbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از عشایر میخواست بزهاش از رودخونه رد کنه و تصمیم گرفت این حرکت شاهکارو بزنه
🤣
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/147590" target="_blank">📅 19:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147589">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رو کدوم سرمایه گذاری میکنید؟</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147589" target="_blank">📅 19:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147588">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
اسکات بسنت در مورد ایران: ما شاهد فروپاشی ارزش پول ملی بوده‌ایم. ما شاهد افزایش بی‌سابقه تورم بوده‌ایم.
🔴
و به طرز باورنکردنی، در کشوری که سومین ذخایر انرژی را در جهان دارد، اکنون مردم برای سوخت‌گیری باید تا چند ساعت در صف‌های طولانی منتظر بمانند، زیرا مجبورند…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/147588" target="_blank">📅 19:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147587">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bl2bbFVt6oGKTJcPZ5ikfsC5BdYKu645qmFX28ZRkq1o5fm2z6LTYI0x_vdCuK809sDR90pnIdu5cDUnQZGSBBrDLSTudt7bEYQtLPeL_pbdtvLlEjJ-LCZpLGm3ZqSHF93HwpXALepNKRX0gdyUTTWqP5BQVvjkzU_2II4osdTMYJpo2zONm35h2bje7nlZMV99KzabPaMZKF1m2ay2UvS_qFMmuKxY8cGMIfcQxT8b5yRB1MlqgJM5pKWUu7DcmL9IEh9lZUzjrLlKwPWbyE9QQJSsld-yFTGVRbyd30fhU1wj-MbK38rBMpP5spsXnFJXfZouYWCHldGosCX8Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جبلی رئیس صداوسیما:
همینی که هست و کارمون خیلی هم عالیه، هرکی میخواد نبینه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/147587" target="_blank">📅 19:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147586">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09289cf68.mp4?token=QCEUm1K0dkXrR5lNWXPd27C3I-soOTjOomDtaXe3dgQVLB_5Hk5swQ8u0tya0KlKr-S1B7gREbT29ak10xLMcM2O67e-oNj3P0LJkGVtknnm0FWPhpaOvl_wNoLiMipWFD2h3ouFcP9gzx5Ox1Gst3UML3d3Rx4ultE7rs7MYv4paCeU8um9Fj5l-jw4w09hGTdEPyEXRgRXrSvfGFbKkX7huXyVQvph4N2pJpGoOItJXgvu4cC9tzoghX1lvX5yfs5oxoIiWiLGDP5xqiwIp6TdoBtakBoHVDZKQI5mw34mpB9Vv0HQ4pRr_AV0ysmmArZ1IERdG1lvxRqVTYZcfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09289cf68.mp4?token=QCEUm1K0dkXrR5lNWXPd27C3I-soOTjOomDtaXe3dgQVLB_5Hk5swQ8u0tya0KlKr-S1B7gREbT29ak10xLMcM2O67e-oNj3P0LJkGVtknnm0FWPhpaOvl_wNoLiMipWFD2h3ouFcP9gzx5Ox1Gst3UML3d3Rx4ultE7rs7MYv4paCeU8um9Fj5l-jw4w09hGTdEPyEXRgRXrSvfGFbKkX7huXyVQvph4N2pJpGoOItJXgvu4cC9tzoghX1lvX5yfs5oxoIiWiLGDP5xqiwIp6TdoBtakBoHVDZKQI5mw34mpB9Vv0HQ4pRr_AV0ysmmArZ1IERdG1lvxRqVTYZcfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت در مورد ایران: ما شاهد فروپاشی ارزش پول ملی بوده‌ایم. ما شاهد افزایش بی‌سابقه تورم بوده‌ایم.
🔴
و به طرز باورنکردنی، در کشوری که سومین ذخایر انرژی را در جهان دارد، اکنون مردم برای سوخت‌گیری باید تا چند ساعت در صف‌های طولانی منتظر بمانند، زیرا مجبورند سوخت خود را وارد کنند.
🔴
من معتقدم که این واکنش‌های خشن و تند که از آن‌ها شاهد هستیم، نتیجه‌ی یک موجود زخمی و در گوشه گیر افتاده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/147586" target="_blank">📅 18:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147585">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🤫
اگه توام دنبال کد تخفیف
🆓
📌
دیجی کالا و اسنپ و ..... هستی بیا
👇
🛍
https://t.me/off_khooneh
🛍
https://t.me/off_khooneh</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147585" target="_blank">📅 18:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147584">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
اف‌بی‌آی: خنثی‌سازی حمله داعش در پنسیلوانیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/147584" target="_blank">📅 18:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147583">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏
👈
وزیر خرانه داری آمریکا: چون ایران قصد داشت بمب هسته ای بسازد، بزرگترین کارزار اقتصادی جهان را علیه ایران اجرا کردیم
🔴
تاکنون سه بانک کمک کننده به ایران را تحریم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/147583" target="_blank">📅 18:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147582">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
پوتین به دلیل تهدید پهپادهای اوکراینی، انجمن سیاست خارجی را به مسکو منتقل کرد
🔴
کنفرانس سالانه والدای پوتین پس از آنکه سرویس امنیتی او نگرانی‌هایی را در خصوص گسترش عملیات پهپادهای دوربرد اوکراین مطرح کرد، از سوچی به مسکو منتقل شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/147582" target="_blank">📅 18:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147581">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
عربستان به مشتریان اروپایی نفت: فعلا نفت نداریم
رویترز:
🔴
عربستان سعودی به مشتریان اروپایی خود اعلام کرده است که به دنبال حمله هفته گذشته و تعطیلی خط لوله "شرق-غرب"،  امکان تحویل محموله‌های نفت خامِ برای اواخر ماه سپتامبر  ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/147581" target="_blank">📅 18:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147580">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsICjSmBqUDgMZ_m-tDgyfozYwK2inFPhlRV9YTz7Nh1I6oSHn-RINwwrVzLqM4IFBXtDrYWJqxwbjPK6kIsQfdiaIkYaktPnsX9EBzUjQ6mQn6Mc0Qm28WRLcpixvpbxLENfAoC0g3gfBe9KY6O4bg4YtUnlIv1kCgApNyjEzCcG66A2vMPYXiBGMQypDXpRide7DY7NtO-_VNHdQkfJ8LVCrRNbZdqxqrT3NQ1sXa_TVDhEUzqMHLZ9bcM-YMSqWM7LX-tFQoZ2qP5zAVWGuvU9Fei8AwoCCRXCzJoSQme2S2tQXKR20wvuXTlambpyG7loQlqOKfi2VOt8nwJrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت ۱۰۷ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/147580" target="_blank">📅 18:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147579">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d827e0ad6.mp4?token=XP7gHOK3l5qYdo0gZ5H5gbXqQLYkcyS7WOaFGVS_LsCS-VXrqXX1fmpZR3mnuuLXW-aBtXuzDjOtDEdAvmwqjuV8P_NEk30q6JcwtElheJ7AeplMF7qpYQswPJ0aMZToKvKNKrmiIH5a1WeQV9fY-Uz0W5AsLXAuI04TG_uSDDr8wN8ZWwbn7JOktiqV5B2EarBLfLGyF3IK0ne7U6gKi7gDII2MhAx_XUq8hzKa5E2o4QAB538pDMnp1a0l03h5iVwu4jGMe7FTYchJtGcvl54d45bvbsJGnTLON6qyWaUtw3ZP8j1PpeV-u9n8imjUoHHDumbLwh29RqLs0r8M0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d827e0ad6.mp4?token=XP7gHOK3l5qYdo0gZ5H5gbXqQLYkcyS7WOaFGVS_LsCS-VXrqXX1fmpZR3mnuuLXW-aBtXuzDjOtDEdAvmwqjuV8P_NEk30q6JcwtElheJ7AeplMF7qpYQswPJ0aMZToKvKNKrmiIH5a1WeQV9fY-Uz0W5AsLXAuI04TG_uSDDr8wN8ZWwbn7JOktiqV5B2EarBLfLGyF3IK0ne7U6gKi7gDII2MhAx_XUq8hzKa5E2o4QAB538pDMnp1a0l03h5iVwu4jGMe7FTYchJtGcvl54d45bvbsJGnTLON6qyWaUtw3ZP8j1PpeV-u9n8imjUoHHDumbLwh29RqLs0r8M0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
یه خبرنگار داشت جلوی سخنگوی وزارت خارجه، تخماش رو میمالید
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/147579" target="_blank">📅 17:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147578">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12945af81.mp4?token=gsybzTfMI_k9WOkfg1ri98NVPNZn22LRODp3Gm6_wtDZhQVESDredgI30X5MUbwGdtAnCfYUzfn8OQI_jcEKonOyXFnjWv8rGr_gjP-lHogkbIV2tZvR7dJfEqNZ-S6H0RTnXDseyRcEz43OiXek51HihA4lVi5Bnf5Cmt0cVNaDiYB85G451nUuoYx_GRHXPoKoTDb_IyhMxA4E4fLWH3czcfXJ7ra-5rTMKHWNA3vOslLlqRzrMXwqa6KSXNgp9xr6c_LmQ8FiylxAbVqrN0TxwwP-ATwlpZclsveKiuve6Q7vwXRezgHdgQ4hJiNiJnTQQdkceiajo7oG8EbISQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12945af81.mp4?token=gsybzTfMI_k9WOkfg1ri98NVPNZn22LRODp3Gm6_wtDZhQVESDredgI30X5MUbwGdtAnCfYUzfn8OQI_jcEKonOyXFnjWv8rGr_gjP-lHogkbIV2tZvR7dJfEqNZ-S6H0RTnXDseyRcEz43OiXek51HihA4lVi5Bnf5Cmt0cVNaDiYB85G451nUuoYx_GRHXPoKoTDb_IyhMxA4E4fLWH3czcfXJ7ra-5rTMKHWNA3vOslLlqRzrMXwqa6KSXNgp9xr6c_LmQ8FiylxAbVqrN0TxwwP-ATwlpZclsveKiuve6Q7vwXRezgHdgQ4hJiNiJnTQQdkceiajo7oG8EbISQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه ترور مولوی یوسف در زاهدان توسط افراد مسلح
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/147578" target="_blank">📅 17:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147577">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
اف‌بی‌آی: خنثی‌سازی حمله داعش در پنسیلوانیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/147577" target="_blank">📅 17:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147576">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏
👈
وزیرخارجه عمان و مارکو روبیو، وزیرخارجه آمریکا در رابطه با تنش‌های ایران و آمریکا و تحولات منطقه گفتگو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/147576" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147575">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
خبر خوب برای معلمان
🔴
کمک هزینه شروع سال تحصیلی آموزش و پرورش برای معلمین واریز شد.
🔴
هر معلم ۳ میلیون تومان
😘
😍
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/147575" target="_blank">📅 16:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147574">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEXtCb2HCyP9nYVj_akXFhvtekbnav9kiM7v9uFSSn3xRsOJQc2pAjZa1Js3BpHRgHwwO2we20_yzHA3vfe_KuYh62qCMyQzp9j8yaRSl4NWKcv7eqcf6vT0wYsz-FpaggO9tJeLFfPlO693BtD4-xKDDVvLWZpOt-EjcqRFe7pzAv_iwZkvl80BM8jWPyfBv6JhFreNlZs4evgMdEzuTsDd_U53GIcjfH6tnxuNfKv77FXLL4VnCsIN9_OPPfn3W7EhJZV6hjxlIflSaFlqP7qSf2g-nQLFcqT7T8Tpez6m2HF79aWOeEgC3aqcxeJpWd9X1mSfCUidYs9GRYRXqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور: اونایی که از لاله مرزبان حمایت میکنن ربات هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/147574" target="_blank">📅 16:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147573">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تحلیل عجیب هوش مصنوعی از دلار و طلا
😳
👇
👇
👇
👇
👇
https://t.me/+cs85WnZxgpM1NjRk
https://t.me/+cs85WnZxgpM1NjRk</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147573" target="_blank">📅 16:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147572">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
آکسیوس به نقل از مقامات آمریکایی:
دو قایق کوچک ایرانی روز دوشنبه پس از تلاش سپاه پاسداران برای توقیف یک پهپاد در حال گشت‌زنی در تنگه هرمز هدف قرار گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/147572" target="_blank">📅 16:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147571">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/52bc7ce3db.mp4?token=isVEbvAL11cYUqxh-7KVPUv4ONJDJ4zG-LfpIsxbe9NoyvtC8qmq1ldIBUrdUqC3GcfQiIY0iL0h5oHt19ljToMiAT0hfaCiqMUQ6HsFBRElczrPEMSbP9KqBfZ_IuWjxtJ6TLdSGeQHiE4ztX6pnuA18xCHeEY7cml3ESI70RPDEZmS3p9esA4gJJCxZz1PstPnOSa5qQJTquHmz8HaJPexBwt2TbisPX5VtToOFEStrnce6K17hFWb9aPXie-9LtCpquqol4BjCwoLss06WJuCAf-cwsBHQ7kCne55C6UrFLze9G-Y5lgMOyhS942PkU2eAPB_awzgKya7LQYGoA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/52bc7ce3db.mp4?token=isVEbvAL11cYUqxh-7KVPUv4ONJDJ4zG-LfpIsxbe9NoyvtC8qmq1ldIBUrdUqC3GcfQiIY0iL0h5oHt19ljToMiAT0hfaCiqMUQ6HsFBRElczrPEMSbP9KqBfZ_IuWjxtJ6TLdSGeQHiE4ztX6pnuA18xCHeEY7cml3ESI70RPDEZmS3p9esA4gJJCxZz1PstPnOSa5qQJTquHmz8HaJPexBwt2TbisPX5VtToOFEStrnce6K17hFWb9aPXie-9LtCpquqol4BjCwoLss06WJuCAf-cwsBHQ7kCne55C6UrFLze9G-Y5lgMOyhS942PkU2eAPB_awzgKya7LQYGoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک فروند بوئینگ ۷۳۷ شرکت سپهران در پرواز مشهد ـ کرمانشاه، پس از برخاستن با مشکل در یکی از لاستیک‌ها و احتمال آسیب به موتور مواجه شد.
🔴
خلبان با اعلام وضعیت اضطراری، هواپیما را به فرودگاه مشهد بازگرداند و هواپیما به سلامت فرود آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/147571" target="_blank">📅 16:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147570">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
اسرائیل هیوم:
منابع دیپلماتیک تأیید می‌کنند، اسرائیل به عربستان سعودی در جمع‌آوری اطلاعات علیه حوثی‌ها کمک می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/147570" target="_blank">📅 16:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147569">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTCFfHjZjztLpagFCWxHAE-udRjw1bkWgeNb3c_6uG_ti52UJPSEpWHgzd4kFJXWVb4vMHMtzxXyjLRwD9OFYgFoY0mrqHAzoQnnb6BBlEOxTVja9-R7kuFZRVcUhUJ50rB39X3IWV-0EKPaidUkFR-CCg6smmXM2OOGyqRGSlUyR7XzBgcE2H75JO6jaVehQXAVVtex4jD89IbMeAdIxTz6iOHegdqB9Z6rql8LkD7qNUz4-ZATwrMH7s9viJ5FVZ0tCFBCnjjJfHZnUTRvMdBOhQQ9_CWVdYtDr9I1fWEFfs524qre-kiIHLU_wKcn3kDKujmlssepysqwTl3zVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
ایلان ماسک:
هرکی بازی ویدیویی نکنه احمقه، بازی کنید چون برای مغز خوب و مفیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/147569" target="_blank">📅 16:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147567">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1OOw3z-7KcUlm-ixbKEcPtK8TtPdozb0oCI_GvCpyw9Lwm6dPodpZRs5acsXyUc77m8gd3qEP9iGJZxH8MpZJg8gESzY23tXwmJp6XkOxqBY9nEoafsag2dqhXQm89dIgkffYP-SxiHXjBMZgJT4RJiiPrM962FvMLRSRUb7-UZ3lPIHVXQ7pQjf5IiZ-N9H523ljQNHJfpYvDzQKT7_920UuUo6HHJmCDGJiJ5m1L5fYEzJoXoXPhUgm7aTJLzOf1SIq5v9wUSRuSQFMpFd_e7awhMyrUKO3C5fD3hLDT6JuhDW8dkjcjBMoBX0HAw4h1oOZO0c42XaUwafALNng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dSHlpjs96Jr5YhQ0hyoCRlThIB3hKSKbnW5F1lZkcznmaZb1XHTvTfe69ylMuP53YtRvYxNmG79FPqP2FGm2yEjtEworKj40DWXYdZGYyngwRhtvEuOH-DbD4k6I4nwJUAde-qpPqZGxdfOZpMn92molNeTwtPAuMTOK8IDjy_FAA1ke7nEXT261lQmvtKGVRRnga8XXqWvvN6TzyRshi55xiO-iRI9GA8b8UmT_LYeyOf1O-hkiahgL1nJAjT1PK-S37gbaVkrMOqzdPCfTZCq5PCMg46qOzbv4BWZswsEikYY1j35R8dIWOgzr30Y6ZKgGxNnxwdwdNmNEsCEyOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF):
نیروهای اسرائیلی در جریان عملیاتی در اطراف
کفرشوبا
، یک سکوی پرتاب و تعدادی راکت متعلق به
حزب‌الله
کشف کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/147567" target="_blank">📅 16:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147566">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
پزشکیان: اکثر کشورها از آمریکا حساب میبرن چون ابرقدرت هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/147566" target="_blank">📅 16:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147565">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
عمان: در حال پیگیری روند انتقال نفتکش مورد حمله واقع شده «ال گایا» به یکی از بنادر هستیم
🔴
۲۳ نفر از خدمه این نفتکش را خارج کردیم؛ جست‌و‌جو برای یافتن ۲ فرد مفقود شده ادامه دارد‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147565" target="_blank">📅 15:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147564">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAK9j22YkpJiqK1DX_VCti9LPcqfcZWBlUkqjUt1KN4AjJhp8waqHJ_ZBi4XGcrcs8TZxSwLfGJLq8x08zti8CbPDjWzJtodkbVcTMZk_lYMJxsPyGHv94zayf7uoOE32u-6jkos3ks0dQm68H-9-ZUEXr_yWKN57OK4vTuO1TK7DdK0kXCmNc4zXMSUIaZzAP4JhqPN_8IyruIjyV5Kr_7itFQDKcnmZv6WxgRJwJGEAa5tusJMAlCxTxcYH0tWgJgDg72KevVckyoM-d3B5_dY1Dp34m2-xtZ9ke012__nm4Q-HNa-6uvh51NEJGYD0KP5-bMDANYirLFTPltxZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری از کفر تیبنیت در جنوب لبنان پس از عقب‌نشینی نیروهای اسرائیلی از این منطقه به سمت قلعه بوفور
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147564" target="_blank">📅 15:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147563">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed891a24b.mp4?token=Zunjbb5X15MYN1KWtqvu9w2G_8pHnMRNqQfIJQIR3C7ANkeE-zbVBUPIRW1F8192eKzGGKXzlW6eZ02l7ACsCr2iUYskrSz08_J6dLRLOfSyxao-XzXv7IejzZ0tWsiMiPcfEvXWUhbKR0x0xUtHalJcKm0EE4Mv_rHhFGIGgZUrlvVSUxNBBijvA5-9EI2iVCa39JfSKGRfuck9EBKoZYyYsEp0OaJtYXFBJIIGScwCytqEyefURfDVPdPVgjR8UCbwBDv9yaqL762Myl6Lrrkdpu-ybJ9d_TDyQ-hDTqd3tEJVy1oDNOwCalpjeU7UbUD_YsZScwfyGAK0uXohEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed891a24b.mp4?token=Zunjbb5X15MYN1KWtqvu9w2G_8pHnMRNqQfIJQIR3C7ANkeE-zbVBUPIRW1F8192eKzGGKXzlW6eZ02l7ACsCr2iUYskrSz08_J6dLRLOfSyxao-XzXv7IejzZ0tWsiMiPcfEvXWUhbKR0x0xUtHalJcKm0EE4Mv_rHhFGIGgZUrlvVSUxNBBijvA5-9EI2iVCa39JfSKGRfuck9EBKoZYyYsEp0OaJtYXFBJIIGScwCytqEyefURfDVPdPVgjR8UCbwBDv9yaqL762Myl6Lrrkdpu-ybJ9d_TDyQ-hDTqd3tEJVy1oDNOwCalpjeU7UbUD_YsZScwfyGAK0uXohEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.
🔴
از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/147563" target="_blank">📅 15:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147562">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رو کدوم سرمایه گذاری میکنید؟</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147562" target="_blank">📅 15:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147561">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z9fnLYGxoPXclzxnNdoEAhu98EQgIcEZfnrkEAhXbAyk4Ed5-BgiD7921Y7C1vlAf0fG_JEyAYAf8au25C2vvkKJhpVY6uLf28UMql2sAZYZialzUzp-6N2t8H9qFdKdXFinJCXe-AlVEV0dw_IaVEkG0WCKSTzEl_I5X5-nM5wRSs7ZfFd1DEv0p_-HYHAvHd367aJlScD5lvrsDaAMSS64yQZBKuaPJFLcky-8Dz3JsaNQ4jV-SyqM9CbswY2inEpEW54j3gGbWuWGOiZyjBStKkjDI6jcxXCizBYeqz8Thow3bWVdg4twdLiKUBg6dGrabdncqc3jdCpGAHI2MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد اطلاعات کاربرانش در دارک وب، به فروش گذاشت، این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع آوری کرد و برای فروش گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/147561" target="_blank">📅 15:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147560">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsmzpVKipiMFvMpI6AtwO46_dDwZ01YeR3R0rhAYYLopjZYd8inWuxjfI24eIzFchpCWc_faYVhTHB6gmtWNRTVvMrZBonm7B19JxnyaRNvKAVfjBsoUZEbqMA_C1JTSKhaENC46LxQQlRu3ZYQmObUe7DoZWoeVLDqgDDyp9HZF1_pP595S1y9zvA0Q8WCfYMGUUgsiXAjtuRuAm0f172Ku0qpZyYsxocvO6NUJboWH2WF0Cb9H02ayTf4u-mhRnzJgFrz63r9CCW63HSTJ9MxjGUqRVhj0Tz969ldLESCn143PBHI8FOPuIQP-Rl2MSlXlklUfQn4wSVRyFs8bTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس نظرسنجی‌های رویترز/ایپسوس، میزان محبوبیت رئیس‌جمهور ترامپ اندکی افزایش یافته و به 35 درصد رسیده است، در حالی که این رقم در اواخر ماه آگوست به پایین‌ترین حد خود، یعنی 33 درصد، رسیده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/147560" target="_blank">📅 15:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147559">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
هاکان فیدان، وزیر امور خارجه ترکیه:
امنیت، ثبات و رونق ایران، به طور طبیعی و مستقیم بر منطقه ما تأثیر می‌گذارد. از این رو، ما خواهان این هستیم که این درگیری موجود در اسرع وقت از طریق راه‌های دیپلماتیک حل و فصل شود.
🔴
افزایش حملات متقابل در دوره اخیر، به طور جدی تلاش‌های صلح را تضعیف می‌کند. این اقدامات که باعث افزایش تنش در منطقه می‌شوند، باید فوراً متوقف شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147559" target="_blank">📅 15:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147558">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17a03d9b86.mp4?token=ETd-EZnh31REN_btMEcZOXAnkms0WUZmZpvLE7HKAN0r3f5nzLlphpdBXjnEJMdM1MrswHZtD7_-Ah0etatkobVh6JW1W2_dJIzgh6qx0YeVIGHOHHJHIQfc9KHcQ32rPbevxk0DPDH6sMTYsaS2sMnP7FmQkheL2tyFFmXfPCz40iUdw4Q6EX3uCEJJtmBTikpQ8tSb4LyMQiAYMqOqai6OJ8HxMwxOX15fJvSglT47fpEQLuKnk6TyzfPLNzdLytfx6v_J9fzboj7x9sOC5ShJm-dqUVj77V9YDXLq6rRApzd9WgVnzX3eAxgWz0GSWJr6j6HP3Hyl7KxNyM9jQUu3PHA0Wa2OqItbFOgF8ihS2BZN7AcSyIOuX26I6AKUwud3Kvy7gBFqmF24yr1klxmXYdHINnnofCu6oePJdPiseSLeBVbhletrT87vQvIPJB-1m2Yn2TQWTgAa5Govd_v5tZYpatfztO3a_QcEfAYsHluJk9Kt1JLs7_fZtUJ4ALxmIx3FMoe6rUEodzK5P8VouerAy-BAkAEgXjQft61bKopo3jTDK5jRX1bEZneLBgn-aKxnnRuFkPtmf6PvYr3ye2rxSTaoEUxY4H2ik3rIhzXM5KIw7GKxZ5M_gll3wWJtTbop7DTrzdxoOiNPBH4PQgJ-564p80tuR-ufEj4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17a03d9b86.mp4?token=ETd-EZnh31REN_btMEcZOXAnkms0WUZmZpvLE7HKAN0r3f5nzLlphpdBXjnEJMdM1MrswHZtD7_-Ah0etatkobVh6JW1W2_dJIzgh6qx0YeVIGHOHHJHIQfc9KHcQ32rPbevxk0DPDH6sMTYsaS2sMnP7FmQkheL2tyFFmXfPCz40iUdw4Q6EX3uCEJJtmBTikpQ8tSb4LyMQiAYMqOqai6OJ8HxMwxOX15fJvSglT47fpEQLuKnk6TyzfPLNzdLytfx6v_J9fzboj7x9sOC5ShJm-dqUVj77V9YDXLq6rRApzd9WgVnzX3eAxgWz0GSWJr6j6HP3Hyl7KxNyM9jQUu3PHA0Wa2OqItbFOgF8ihS2BZN7AcSyIOuX26I6AKUwud3Kvy7gBFqmF24yr1klxmXYdHINnnofCu6oePJdPiseSLeBVbhletrT87vQvIPJB-1m2Yn2TQWTgAa5Govd_v5tZYpatfztO3a_QcEfAYsHluJk9Kt1JLs7_fZtUJ4ALxmIx3FMoe6rUEodzK5P8VouerAy-BAkAEgXjQft61bKopo3jTDK5jRX1bEZneLBgn-aKxnnRuFkPtmf6PvYr3ye2rxSTaoEUxY4H2ik3rIhzXM5KIw7GKxZ5M_gll3wWJtTbop7DTrzdxoOiNPBH4PQgJ-564p80tuR-ufEj4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: عموی من احتمالاً، به طور خلاصه، یکی از بهترین‌ها در تمام دوران بود. او ۴۱ یا ۴۲ سال در دانشگاه MIT تدریس می‌کرد و به عنوان یکی از باهوش‌ترین افراد شناخته می‌شد.
🔴
بنابراین، من کمی از نظر ژنتیکی قوی هستم، اگر به نظریه منابع اعتقاد داشته باشید. من به آن اعتقاد دارم. من از نظر ژنتیکی برتری دارم. من در مورد هوش مصنوعی (AI) اطلاعاتی دارم.
🔴
ربات‌ها جهان را تصرف نخواهند کرد. هوش مصنوعی نیز بقیه جهان را تصرف نخواهد کرد. کل این موضوع یک فریب است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/147558" target="_blank">📅 14:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147557">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8ae5f579.mp4?token=mLVzkp1GsXJyQumudsXDzPRcJIbjIDilGUWzdu6O-2NPuUStYbuVrg7aqZa8fOAR4ahUZWA-9FxZVvos8UrZa3xcC1iA-k5ZjQobADyXEVwa8jmzl7dJbr9VKq24rVRr0SLyNC9jUWpQy-_Jn8nvZN8cGFO0mJgNd5Vyyo2Bmt6wLi15EsoI9iDgQlPddwxDVuaGE9S2MUwLcE63Y6mYwyPea4eBIQJRZSjW_nxwKMsbZ4PtSSpr99Xfx9lLbqz-9ZvnM3Q4j0_bMCpooxx6tqGJwFuqw8TBLjlU34UVUyTZH8d6HpD7TQ2JGjMrqvVAIsDZNMgNTtBP2KS7-ZukuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8ae5f579.mp4?token=mLVzkp1GsXJyQumudsXDzPRcJIbjIDilGUWzdu6O-2NPuUStYbuVrg7aqZa8fOAR4ahUZWA-9FxZVvos8UrZa3xcC1iA-k5ZjQobADyXEVwa8jmzl7dJbr9VKq24rVRr0SLyNC9jUWpQy-_Jn8nvZN8cGFO0mJgNd5Vyyo2Bmt6wLi15EsoI9iDgQlPddwxDVuaGE9S2MUwLcE63Y6mYwyPea4eBIQJRZSjW_nxwKMsbZ4PtSSpr99Xfx9lLbqz-9ZvnM3Q4j0_bMCpooxx6tqGJwFuqw8TBLjlU34UVUyTZH8d6HpD7TQ2JGjMrqvVAIsDZNMgNTtBP2KS7-ZukuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره هوش مصنوعی:
ربات‌ها قرار نیست جهان را تصرف کنند. این اتفاق نخواهد افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147557" target="_blank">📅 14:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147556">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
عمان: بحران تنگه هرمز به زودی به پایان خواهد رسید
🔴
حمد النعمانی مدیرعامل شرکت گاز طبیعی مایع عمان (Oman LNG)، امروز سه شنبه گفت که بحران مربوط به تنگه هرمز به زودی به پایان خواهد رسید.
🔴
وی در کنفرانس بانکوک گفت: بحران تنگه هرمز طرح‌‎های درازمدت این شرکت را تغییر خواهند داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147556" target="_blank">📅 14:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147555">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
آمریکا به دنبال توقیف ۶۱ میلیون دلار از دارایی‌های نفتی ایران
🔴
گزارش‌ها حاکی است آمریکا برای توقیف حدود ۶۱ میلیون دلار از درآمدهای نفتی ایران که به شکل دارایی‌های رمزارزی درآمده، اقدام کرده است.
🔴
در این پرونده نام دو شرکت چینی و صرافی رمزارزی بایننس نیز مطرح شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/147555" target="_blank">📅 14:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147554">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
کرملین: روسیه معتقد است فضا باید عاری از تسلیحات باقی بماند و امیدوار است از طرح خلع سلاح کامل فضا حمایت گسترده بین‌المللی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/147554" target="_blank">📅 14:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147553">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزیر خارجه طالبان: هم جهان اسلام و هم غرب از ما می‌خواهند مدارس دخترانه را بازگشایی کنیم، اما نباید با نگاه غربی به ما نگریسته شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/147553" target="_blank">📅 14:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147552">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
طلای جهانی در آستانه تصمیم فدرال رزرو درباره نرخ بهره، با افت جزئی به ۴۳۰۲ دلار در هر اونس رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/147552" target="_blank">📅 14:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147551">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
رسانه عبری والا به نقل از منابع امنیتی: تماس‌هایی میان عربستان و اسرائیل با میانجی‌گری فرمانده سنتکام انجام شده تا از طریق ارائه اطلاعات، به سعودی‌ها در دفاع از خود در برابر انصارالله کمک کنند
🔴
نگرانی‌هایی در مورد اینکه آمریکا با ایران و حوثی های یمن به تفاهم برسد و سپس عربستان و سایر کشور‌های منطقه را با مشکلات حل نشده خود تنها بگذارد، وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/147551" target="_blank">📅 14:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147550">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
کرملین: پیشنهاد ترامپ برای برقراری آتش‌بس در حملات به تأسیسات انرژی میان روسیه و اوکراین، «ایده خوبی» است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147550" target="_blank">📅 14:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147549">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">💢
رو کدوم سرمایه گذاری میکنید؟
💵
دلار
.
🔴
طلا.
🏠
ملک
💸
بیت کوین</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147549" target="_blank">📅 14:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147548">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tX4riMRkXXrbLGuv-r4DdiBztnmzmGBaTG2i5K5pXPdZP7YjSMEhTHxLOZq9q-EhE-z1PaVuw5UhUZtosCv0bXGtk0Vp3PFMWtJSBYkDOOpXcwUCgld_fkj2Nh6NPIj4lfbAXtCNWuYC48FV5SNDRBzL8-wnbhSfdxzmEoAPQXFkSDbTgfkOQd7Mjz_5_-EJc1VQUtnpm-baZbPmncKZFzfEF80tRBR-4qkmtz9_YiGv7kPz2JxaH7sULTTn-muZ-IyDwvgaYbqF7KlVmrpUu1sRdXx3UBKbsbHkT64xucXsZI9SmZXE0ePl2tWwXoIMggXAkCzQXRiJjOX367OddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کرایه روزانه یک ابرنفتکش از خلیج فارس به چین برای نخستین بار در تاریخ به یک میلیون دلار رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/147548" target="_blank">📅 14:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147547">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزارت خارجه قطر: دولت قطر با جدیت و همکاری با شرکای منطقه‌ای و بین‌المللی خود برای دستیابی به توافق درباره تنگه هرمز تلاش می‌کند.
🔴
دولت قطر با شرکای خود برای پیشبرد گفت‌وگو درباره امنیت کشتیرانی در تنگه هرمز همکاری می‌کند.
🔴
دولت قطر از دستیابی به توافق درباره تنگه هرمز و توافق طرف‌های ذی‌ربط بر سر یک راه‌حل حمایت می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/147547" target="_blank">📅 13:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147546">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
عمان: ۲۳ خدمه نفتکش «الگایا» نجات یافتند؛ جست‌وجو برای ۲ نفر ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147546" target="_blank">📅 13:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147545">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
چمران شورا تهران: ما تو جنگ میریم رو پشت بام، ولی نتانیاهو میره زیرزمین
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/147545" target="_blank">📅 13:39 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
