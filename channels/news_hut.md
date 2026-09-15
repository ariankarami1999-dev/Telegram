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
<img src="https://cdn4.telesco.pe/file/R5Ywu0DohZXruQ0yJzGH9O4PAuy9CIvbhT3YBBvSfE2_fsCg-y9CUt53rVbP6LKvptjdAZAnMfIB3aQr4r1emi59zIW-MhztpHfUyxe6s8wEtElw8SJG-7JKAZo_fWzVkDa-gzmdwnoWYNoi0kC51Pm8wit_XlcffCcWsy7P7X6hCPRKCd4d8RkAQpom2rn5m518q30l_AC8ghqMQjvasECczkvCuS4iO-F6HAfGJKER3qGr08MwM32Hb1HGzTDid2z6dWWIsKYm6flHbcnf-YAQJ67SInMI2UfrxsGIHyyck4c4M1d0_YSzTIvVhRIcFct42HbbV1sUVc8HMujfpw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 107K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 19:33:43</div>
<hr>

<div class="tg-post" id="msg-71682">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cc9cce711.mp4?token=pvj2JYAm5JEkvoAro3_eBmgYfBalV_iCZ-VBRQ8HBCBZz4Xgq7_UhpnzFnXQ9uGdICVC9lWFJhCBqFHt_pTADUHUQ2jUqoZe5S8_orN34AQEvWWokZVHAumrSj9QGj2IbAXcL0LOWdsnl3YizjlI92c3ervHS3DDQ9c9IHqnQ6weve2uHkoxA_Qy66dQm8Yd0JunVvcSEB7QcTM9tuSYHnw57fNNSWDU08wWE_BhHp4zwX0Ip45P4C9h43XGg457GLzqf8wbEAq84ruTnMPQC7Wv6am1es6t74uHS0MM9WutS0ahFvz1EorDilpFQ4rmzocAQDtG8lw8hPLyGK0fbKAAWY07A0k3HPbI7Ge3exU-lxhjPjeUeqPv8SskLIR4oZVw4bK3qswcHXzufopv6DxOZuy7vBTUBHRaBlZ6LbtjQORVqyurUD-DOOzoGzVEdVNZUGYkyzNFov2R05XMILqk8t8lEFMAWpVjkvLnM9VDzPUgXIguX9upRoa1lOmG3y9FU2P1IMXfuNd8caJjtQS4uRFwbwXUCweCRFtmsJvC8s46j66RZA0UDwBLd57IXHnnWIqe8qCeDHplFjj9glORTUeDzmX17IijD2lsSXTllfeb12_F-d4-Q6_mvdewOY0pqIlW6a8JgbukN3txVBI5Fwk75eHVOk-e7Jg5lIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cc9cce711.mp4?token=pvj2JYAm5JEkvoAro3_eBmgYfBalV_iCZ-VBRQ8HBCBZz4Xgq7_UhpnzFnXQ9uGdICVC9lWFJhCBqFHt_pTADUHUQ2jUqoZe5S8_orN34AQEvWWokZVHAumrSj9QGj2IbAXcL0LOWdsnl3YizjlI92c3ervHS3DDQ9c9IHqnQ6weve2uHkoxA_Qy66dQm8Yd0JunVvcSEB7QcTM9tuSYHnw57fNNSWDU08wWE_BhHp4zwX0Ip45P4C9h43XGg457GLzqf8wbEAq84ruTnMPQC7Wv6am1es6t74uHS0MM9WutS0ahFvz1EorDilpFQ4rmzocAQDtG8lw8hPLyGK0fbKAAWY07A0k3HPbI7Ge3exU-lxhjPjeUeqPv8SskLIR4oZVw4bK3qswcHXzufopv6DxOZuy7vBTUBHRaBlZ6LbtjQORVqyurUD-DOOzoGzVEdVNZUGYkyzNFov2R05XMILqk8t8lEFMAWpVjkvLnM9VDzPUgXIguX9upRoa1lOmG3y9FU2P1IMXfuNd8caJjtQS4uRFwbwXUCweCRFtmsJvC8s46j66RZA0UDwBLd57IXHnnWIqe8qCeDHplFjj9glORTUeDzmX17IijD2lsSXTllfeb12_F-d4-Q6_mvdewOY0pqIlW6a8JgbukN3txVBI5Fwk75eHVOk-e7Jg5lIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
تنها کافی است به سخنان رئیس‌جمهور، رئیس مجلس و رئیس بانک مرکزی ایران اشاره کنم که اذعان داشته‌اند اقتصاد کشور در وضعیتی بسیار وخیم و بحرانی قرار دارد؛ هشداری که خطاب به هم‌قطاران تندروی آن‌ها در سپاه پاسداران و همچنین مردم ایران بیان شده است.
ما شاهد سقوط ارزش پول ملی و تورم سرسام‌آور بوده‌ایم؛
و در کمال ناباوری، کشوری که سومین ذخایر بزرگ انرژی جهان را در اختیار دارد، اکنون با قطعی برق سه تا چهار ساعته مواجه است.
این وضعیت اسفبار اقتصادی ناشی از تحریم‌هاست؛ ترکیبی از تحریم‌ها و اقداماتی که ما طی ماه‌های گذشته برای شناسایی و مسدودسازی مسیرهای مالی و سیستم‌های پرداخت آن‌ها انجام داده‌ایم و در حال اعمال فشار شدید بر آن‌ها هستیم.
به باور من، واکنش‌های تند و خشونت‌آمیزی که اکنون از سوی آن‌ها شاهد هستیم، درست مانند رفتار حیوانی زخمی است.
@News_Hut</div>
<div class="tg-footer">👁️ 594 · <a href="https://t.me/news_hut/71682" target="_blank">📅 19:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71681">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d47763dcd.mp4?token=ekkFnccnzeMli2rfOysqx3Zva1OoJCiqNFhaldWO8ioEi6FURRzBZN7b3-cV8lwgr1cwUw_VKTTEpliermRjfyNzV_stlZlpLaNGAD-rzMp8kOHrjWQF-HGGOIEfR_g57bNgFmmUY-EQGDgC89-7MReOXvptp2wx_qzV0YEC1-XQ7nqSej-P5rwZSsstJL823BRVqKdwowDI6HUtLz3Pg8-mr-s67ZPQv9TCEjKl-VofHGQdSgJtDw0oFWYlAm1zsMZYA5vypKyp2a7VwKEV3KybW_1Yi-hKUTsY4MA1-iM0IfgOjhMhPoxwyJKY1PfwUpr_ujyHuRI-Y26TP_eFrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d47763dcd.mp4?token=ekkFnccnzeMli2rfOysqx3Zva1OoJCiqNFhaldWO8ioEi6FURRzBZN7b3-cV8lwgr1cwUw_VKTTEpliermRjfyNzV_stlZlpLaNGAD-rzMp8kOHrjWQF-HGGOIEfR_g57bNgFmmUY-EQGDgC89-7MReOXvptp2wx_qzV0YEC1-XQ7nqSej-P5rwZSsstJL823BRVqKdwowDI6HUtLz3Pg8-mr-s67ZPQv9TCEjKl-VofHGQdSgJtDw0oFWYlAm1zsMZYA5vypKyp2a7VwKEV3KybW_1Yi-hKUTsY4MA1-iM0IfgOjhMhPoxwyJKY1PfwUpr_ujyHuRI-Y26TP_eFrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر، آتش‌سوزی‌های گسترده در تأسیسات ذخیره‌سازی «آرامکو» در «ابها» واقع در جنوب غربی عربستان سعودی را پس از حملات پهپادی و موشکی حوثی‌ها نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/news_hut/71681" target="_blank">📅 18:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71680">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
لحظاتی قبل یک پهپاد دیگر از نوع MQ-1 متعلق به آمریکا بر فراز تنگه هرمز با استفاده از یک سیستم پدافند هوایی متعلق به نیروی قدس سپاه پاسداران انقلاب اسلامی سرنگون شد.
این سومین پهبادی است که سپاه مدعی سرنگونی آن در روز جاری شده.
@News_Hut</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/news_hut/71680" target="_blank">📅 18:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71679">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8132b94509.mp4?token=dq_SlCtrwzOnbZxUSB8-kPNKTiK7G3eJvyaNA2KXDTZ8NpcnbL5Y50Dbx4hkJjmP7Zl5hdm_IlrmUMjIsoYSmXgzihjpBHgx7lsS72QQY2oXjQ72pNQVbPeTqBjfY9b-jqNP580Pg6WWFR7rWQgc6wphCFbD9vFKowE12hdE_F-W6qRA2O7b2duzcxGgt5_EfjGAa-ZBfd-7TyMo_CZnePPZDfRCpqjNpYsCBM2QJDJ49OO1rfWaYH6Iy2IEvD2_BGczAQRsx3jrKTNLB7_GER9hRryhSpDrSWHqK3U6vgUKCjyvtYGBm5hcibdg1TI0nkTmXA7dwomPhdHDb47u7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8132b94509.mp4?token=dq_SlCtrwzOnbZxUSB8-kPNKTiK7G3eJvyaNA2KXDTZ8NpcnbL5Y50Dbx4hkJjmP7Zl5hdm_IlrmUMjIsoYSmXgzihjpBHgx7lsS72QQY2oXjQ72pNQVbPeTqBjfY9b-jqNP580Pg6WWFR7rWQgc6wphCFbD9vFKowE12hdE_F-W6qRA2O7b2duzcxGgt5_EfjGAa-ZBfd-7TyMo_CZnePPZDfRCpqjNpYsCBM2QJDJ49OO1rfWaYH6Iy2IEvD2_BGczAQRsx3jrKTNLB7_GER9hRryhSpDrSWHqK3U6vgUKCjyvtYGBm5hcibdg1TI0nkTmXA7dwomPhdHDb47u7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از پروازهای داخلی(کرمانشاه به مشهد)دچار سانحه شده و بخشی از کابین دچار شکستگی و اسیب میشه، خوشبختانه مسافران این پرواز سالم به مقصد رسیدند. جزییات دقیق این پرواز و نقص فنی هنوز مشخص نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/news_hut/71679" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71678">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71678" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/news_hut/71678" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71677">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crMEWfHuMyOHXrfUtnN81NGw5j9cc6FzdekykFE8CaKEfBx-fOXUyPKmsxrPlh6Wxu1SO6D7TwGwAJ4NGTus-dSFZwNfSYXq2Wje8UiubCX4_i02UOGM7ZCTrcEevJTQgqs6SUmDf4HQPxCeZKFg1RPSXXdJNynghfLw116kPVswdTBdm4pAIema9czlF98Eu6s9o3g7A_AGwGWjmvM1BnB3ShLRYVTNpXbYobEpkBbjoYRyBvvPJQFwRExHmfIW7re7Zxnq_OD8Y_fpQQ1aihg6eFXoO9gz9cJHPN4nJeLE-Sx_SZg6beKrcodVYWTRVtYYM99v_p4gR6n2O9rUjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
تاتنهام
🆚
لیورپول
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
تاتنهام: ۱ برد، ۲ تساوی، ۲ شکست و ۵ گل زده
⚽️
لیورپول: ۲ برد، ۳ تساوی و ۸ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/news_hut/71677" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71676">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea966d07eb.mp4?token=ZhwmMuxNIs8f28Pv_vuZbiwfuoIQ-7Hcd6fZLsANNWV75tZ-lqpJXDUOrW1x48O8l3uq4Mw0d25SG45RrU1oXgXLvso6BGqHCq7mKEEuW-WqxRULfStpu1h4orwm5mxOsJvcSdnbs1K8sjwfOetDjUHo_wSxnhvY70sZpnStlkvLNkyKhoqPQjbezpFIrUmqbS-CLsJVha_88oLM9EbiVjBxO-tjWDNBBPEiPsRAyz-vOHiml7pkcpLg7xPejydI5aeG_uktdLW_RVuJeunvKh3g2M_rKs0TbIidZtvDfkynfer4TA305e6qYhZ3iqw0_IfyECj-v5_IDTXE6JVZ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea966d07eb.mp4?token=ZhwmMuxNIs8f28Pv_vuZbiwfuoIQ-7Hcd6fZLsANNWV75tZ-lqpJXDUOrW1x48O8l3uq4Mw0d25SG45RrU1oXgXLvso6BGqHCq7mKEEuW-WqxRULfStpu1h4orwm5mxOsJvcSdnbs1K8sjwfOetDjUHo_wSxnhvY70sZpnStlkvLNkyKhoqPQjbezpFIrUmqbS-CLsJVha_88oLM9EbiVjBxO-tjWDNBBPEiPsRAyz-vOHiml7pkcpLg7xPejydI5aeG_uktdLW_RVuJeunvKh3g2M_rKs0TbIidZtvDfkynfer4TA305e6qYhZ3iqw0_IfyECj-v5_IDTXE6JVZ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛
بسنت درباره ایران:
ترامپ در حال اقدام علیه رژیمی است که خود را وقف شعار «مرگ بر آمریکا» کرده و برای تحقق همین هدف به دنبال دستیابی به سلاح‌های هسته‌ای است؛
اقداماتی که رؤسای جمهور پیشین مدت‌ها از انجام آن طفره می‌رفتند.
تحت رهبری او،آمریکا دیگر تهدید ایران را مدیریت نمی‌کند؛ ما در حال پایان دادن به آن هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/news_hut/71676" target="_blank">📅 18:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71675">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAkNQmCT4ANharl8wCrNIyeR3ZXziJ__c5YCKiTIgaoikeLnUE-kXTEOcWIsraZV4XVNBr7vJi3dMXt8QDKRuZr3L1UyZBkhiUuT50L0s6lp4temXTEukvVJlg5AVacpAVD9mlbptzjxLEJNmxwZR3Z43dOyQJiBqpiFHv1twCl5wgfHpK6FY0WdEi3J8SAjukbxWgjccKdAGuGou0m_Bu3ZA3G_htIs2ZzO3cCgsl1H2rvBxi-jmaaDJhKR21DsefQ2gI3QQoxF43IYVolkFF3x07ko1He9HweWW53wVY78FNRx2e5tL-REM5McIs7IYm2Cf84jQL0ZWWOb6-qT6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس:حمله پهبادی ارتش آمریکا به دو قایق در حوالی بندرکرگان در آب های خلیج‌فارس. تعدادی از صیادان مفقود شدند و عملیات جست‌وجو و امدادرسانی آغاز شده.   @News_Hut</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/news_hut/71675" target="_blank">📅 17:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71674">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4824aba9.mp4?token=ip7hYvmURuGxFaJU-GwLNcKUAb0roSU1IWvm6GaY1hfWRNSbsY8RFUYSPhfB2eHZ1WCxs9Tol1pCsPLuAIOQnUkN8YkcP9YI3jyt6ljjM_9eFvE283TKd0LsfOVPch7zRmoHSh-uf6MApXCZtGIQk0299RPBk9_tely6bdmQyDY9J-S6rrjpCmsasWdvOt6mh2m9lpOIm4TIZuc4fmsyHmHP8XRYSX9VCHdP-ODbNk9zuvliJcDbXVQnuAGzvkdHd6qO5pH8jSqi-xOj6Ki_fmSIMSdGRfaAk16u6ABfCULQRcpVDIVtBi1h2y5yEX4kv2XHrLPx8narIjt97b2P8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4824aba9.mp4?token=ip7hYvmURuGxFaJU-GwLNcKUAb0roSU1IWvm6GaY1hfWRNSbsY8RFUYSPhfB2eHZ1WCxs9Tol1pCsPLuAIOQnUkN8YkcP9YI3jyt6ljjM_9eFvE283TKd0LsfOVPch7zRmoHSh-uf6MApXCZtGIQk0299RPBk9_tely6bdmQyDY9J-S6rrjpCmsasWdvOt6mh2m9lpOIm4TIZuc4fmsyHmHP8XRYSX9VCHdP-ODbNk9zuvliJcDbXVQnuAGzvkdHd6qO5pH8jSqi-xOj6Ki_fmSIMSdGRfaAk16u6ABfCULQRcpVDIVtBi1h2y5yEX4kv2XHrLPx8narIjt97b2P8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو سی‌و‌سه پُل اصفهان، یه پسر نوجوون اومد مثلا یه حرکت نمایشی بزنه و از یه ارتفاع نسبتا بلند بپره پایین که فرود ناموفقی داشت و با سر رفت تو زمین...
@News_Hut</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/news_hut/71674" target="_blank">📅 17:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71673">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=sMVlULXfSiGxf5YD8DqHByav7aHyngq6B4szgeb5cg8C5rPAqt8o-r9-VistBpYzKQXVY5y3rgyMj1aVeJ0uJlg6Mm0NIt9ncjze47bUyYKx7rHu8lIwthjexR86zVYcbZ8zdjQ2Em4OhEYxbXnkHqQOmuujIgNKD-wRHUu_gkoBk9oS8l5Dw5GwutVi2lQl0nRPgGDHCaD_pEcfFbcXe5wCt-SZWHBf4Zd4RZjtO0PqAoAhHweCE7KNCuN4UO1yqsnMrGKwoojr0oQ7eY1DyNrvFRQZN2kaxPdr1xQFB3lZ-Q_hNw-EZ-nL4COJSE9-1lGjEYpFOJIvcg6GdrRl_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=sMVlULXfSiGxf5YD8DqHByav7aHyngq6B4szgeb5cg8C5rPAqt8o-r9-VistBpYzKQXVY5y3rgyMj1aVeJ0uJlg6Mm0NIt9ncjze47bUyYKx7rHu8lIwthjexR86zVYcbZ8zdjQ2Em4OhEYxbXnkHqQOmuujIgNKD-wRHUu_gkoBk9oS8l5Dw5GwutVi2lQl0nRPgGDHCaD_pEcfFbcXe5wCt-SZWHBf4Zd4RZjtO0PqAoAhHweCE7KNCuN4UO1yqsnMrGKwoojr0oQ7eY1DyNrvFRQZN2kaxPdr1xQFB3lZ-Q_hNw-EZ-nL4COJSE9-1lGjEYpFOJIvcg6GdrRl_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن هاشمی: من خبر دارم مسئولین در هر دو جنگ از تونل‌های مترو به عنوان دفتر کار استفاده کردند
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/71673" target="_blank">📅 16:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71672">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نفتالی بنت درباره ایران:
این رژیم فاسد و پوسیده است؛ همچون درختی که از درون دچار پوسیدگی شده و سرانجام فرو خواهد ریخت.
در مورد این درخت پوسیده، می‌توانیم اینجا و آنجا حفاری‌هایی انجام دهیم. منظورم صرفاً اقدامات نظامی (کینتیک) نیست.
صحبت من درباره اقدامات اقتصادی، کارهایی که نمی‌خواهم نامی از آن‌ها ببرم، و همچنین تقویت معترضان داخلی و تقویت دشمنانِ این رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/71672" target="_blank">📅 15:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71671">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afac6b01df.mp4?token=AU7qe3XrZunjlX5bRnW_hjE6_KqiXRil0xuqneQBSxgbB-OJGmF4p2a_PYp2aYNqKLsxWngYX6RZTmEuUSNq8orRRYxpmA3VPnaHo7Q-UXGS2wjpy5hYMKlxNPuZcBxd493nkINXS1yrvnmE4dI24V7ADNET8s_XVg_g2yiqfAEmev-d2snk5nEM8eE3jg-q7YpmCWZM5DoUGtlwVvoMrI81auJNanuLQBD93xAdKrTxBJhVH1r2R69N3HyWp9GWQvkegSs0fK22SLHAt-bkuBZ3UNc3zvq9130kfN4UKaBTU4Obg8YKCbV4CALEJhbiKrXwLGb6xsxRdHlJI6Q7tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afac6b01df.mp4?token=AU7qe3XrZunjlX5bRnW_hjE6_KqiXRil0xuqneQBSxgbB-OJGmF4p2a_PYp2aYNqKLsxWngYX6RZTmEuUSNq8orRRYxpmA3VPnaHo7Q-UXGS2wjpy5hYMKlxNPuZcBxd493nkINXS1yrvnmE4dI24V7ADNET8s_XVg_g2yiqfAEmev-d2snk5nEM8eE3jg-q7YpmCWZM5DoUGtlwVvoMrI81auJNanuLQBD93xAdKrTxBJhVH1r2R69N3HyWp9GWQvkegSs0fK22SLHAt-bkuBZ3UNc3zvq9130kfN4UKaBTU4Obg8YKCbV4CALEJhbiKrXwLGb6xsxRdHlJI6Q7tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌ های این خانم به‌شدت وایرال شده و دخترا هم خیلی بهش انتقاد کردن:
اگه یه مرد، دارایی های خودش رو به نام خانومش بزنه، اون زندگی رو با دستای خودش نابود کرده.
آقایون اگه ۵ تا خونه هم به نامشون باشه، هیچوقت تو دعوا خانوم‌ خودشون رو بیرون نمیکنن
ولی اگه خانوما یه چیزی به نامشون باشه به این موضوع فکر میکنن که میتونن بدون اون آقا ادامه بدن.
من خودم خانواده‌هایی دیدم که به دخترشون میگفتن تو که ماشین و خونه به نامت زده دیگه احتیاجی بهش نداری، خودت برو زندگی کن.
خانوما اصلا جنبه‌‌ی اینکه چیزی به نامشون باشه رو ندارن، اون اگه بخواد زندگی کنه با یدونه سکه هم زندگیش رو میکنه، آقایون بفهمید من دارم چی میگم...
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/71671" target="_blank">📅 15:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71670">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5632e037a5.mp4?token=I3ko91kt1zMYZVdHDZabnWM9I-XJ2R3J4ilLY5VN_yvXZL3nkAkfEmeAZeOvUmB_oAJ7e4M10Wwonwli_Jqy2b0quZM1krwAUQvkNUyT9NL4GMFXnRahpCawD9vnknhiRXNroy-w4gqQm2qdpID2k80sprUUjdZW1su4PP0w8hg3g9ytRa02AwLoGQYLzy34psHdZ0vNywfd_aX8DRO_ordLk1-2MN0R9pbF8AiXG5MnU68HB4tcB7sA-y9Nclx8q1y4pnRWyc4i56icY6mlj-0QumgkG2AfuaRnH-F7_ixLE9fUx96CnUFBuMfS-CRdE6n_bECNkTyzvevsZyUBLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5632e037a5.mp4?token=I3ko91kt1zMYZVdHDZabnWM9I-XJ2R3J4ilLY5VN_yvXZL3nkAkfEmeAZeOvUmB_oAJ7e4M10Wwonwli_Jqy2b0quZM1krwAUQvkNUyT9NL4GMFXnRahpCawD9vnknhiRXNroy-w4gqQm2qdpID2k80sprUUjdZW1su4PP0w8hg3g9ytRa02AwLoGQYLzy34psHdZ0vNywfd_aX8DRO_ordLk1-2MN0R9pbF8AiXG5MnU68HB4tcB7sA-y9Nclx8q1y4pnRWyc4i56icY6mlj-0QumgkG2AfuaRnH-F7_ixLE9fUx96CnUFBuMfS-CRdE6n_bECNkTyzvevsZyUBLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیراندازی نیروهای انتظامی به سمت بالگردآمریکایی در جریان عملیات نجات خلبان مفقودی آمریکا در روز روشن
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/71670" target="_blank">📅 15:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71669">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada1fff69c.mp4?token=o7ZfIASwl0ZECb3I2i4WvV9lcCrTRmNWDU1jJDyfNIcCimUWP9NBNIjXheZIgHHL9d8fvRMCVR-_yjKaELghGHim7wIFpgt-OjYz_LBJgZhvvRPSXabhYXPTi1X_sIeuMAbYI3FHSTaUMF2UwnPHMA-ccmVtlhKcnoHgEtDIdVsyxudvGD9o7QQYr1DXlOO3447BZzy9j4Q9XIuADJTIaIYZnuAUFP6lnaaR7OgPbHyiuKVkcPClhqfmNRmtUBrZKK2mA07qTCM3yi4ezErF9T5uWKDOAJiU4xznjoAydLDX9jaofb_Mkg2ty4aq5uf1zV414Wj1zlSRmB4jHbtAJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada1fff69c.mp4?token=o7ZfIASwl0ZECb3I2i4WvV9lcCrTRmNWDU1jJDyfNIcCimUWP9NBNIjXheZIgHHL9d8fvRMCVR-_yjKaELghGHim7wIFpgt-OjYz_LBJgZhvvRPSXabhYXPTi1X_sIeuMAbYI3FHSTaUMF2UwnPHMA-ccmVtlhKcnoHgEtDIdVsyxudvGD9o7QQYr1DXlOO3447BZzy9j4Q9XIuADJTIaIYZnuAUFP6lnaaR7OgPbHyiuKVkcPClhqfmNRmtUBrZKK2mA07qTCM3yi4ezErF9T5uWKDOAJiU4xznjoAydLDX9jaofb_Mkg2ty4aq5uf1zV414Wj1zlSRmB4jHbtAJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادر زنِ مجتبی خامنه‌ای:
مجتبی خامنه‌ای با همسرش سریال " فرار از زندان " رو مفصل نشستن دیدن و درباره اتفاقاتی که داخل سریال افتاده بود هم صحبت میکردن.
یه بار تو یه جمعی گوشی یکی زنگ خورد، من گفتم این چه آهنگیه دیگه؟ که یهو مجتبی گفتش این آهنگِ یکی از فیلم‌های کریستوفر نولانه دیگه، چطوری نمیشناسیش؟
‌
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/71669" target="_blank">📅 14:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71668">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hizZnXTmJ3TpkH-MsNYy6bwmkbpfGq5WCPQwAvHQ1IdDO66IzVty6I0d7XKBzka5G5AcJodh5s-oqbtovn2fPc7wtIhdRxIuQBgOdhLGaSh8tcT9DpobEwP6ahMfTFLKQ2hRh3wvNHyMtytRP9QyvSjNLlMZaZBZZXRimHeNI6w48f5DW7JUKrfjov-QUw3bLwzYzo0H9rQKi0aNK3A1RpCdPTI1QavR6so4BebY4_gaTj26PSW58C4iJ4-6GYnUJzrIWzv1X0KGGy4d9gnFhD0g3TwcLoI6d4gaGYc7CV0MmAsoUmyL4NiPxe12aAnwl3C9PBguY-8fR5R13srDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی قلهکی:
«نشست عمان» با حضور کشورهای خلیج فارس برای تثبیتِ مسیر تنگه هرمز، با نقش‌آفرینیِ جدیِ آمریکا و برخی از کشورهای حوزه خلیج فارس فعلا لغو شد
عربستان» به بهانه اصابت خط لوله‌اش و درخواستی که از پاکستانی‌ها داشته تا ایران را راضی کنند که به انصارلله بگوید از فتوحاتِ جدید عقب نشینی کند، «بحرین» بابتِ ناراحتی از جنگ رمضان و پرتابه‌‌های متعددی که بخاطر میزبانی از زیرساخت‌های نظامیِ آمریکا در خاکِ کشورش دریافت کرده و «امارات» هم بابتِ اُفت جایگاش در آینده‌‌ی منطقه در صورتی که مسیر جدید تنگه تثبیت شود، در نشستِ مهمِ عمان شرکت نکرده و کارشکنی کردند!
ولی بازیگرِ اصلیِ لغوِ این نشست، آمریکاست!
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/71668" target="_blank">📅 13:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71667">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حملات موشکی/پهبادی حوثی های یمن به مکه، طائف و جده عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71667" target="_blank">📅 12:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71666">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTMmgLqweKFXh4V8TDByf0C3ghpnaYO3yoQlU-EB57QNISxUXtB2zj6VVlOii3i4KjzDHOqUeG9rD4xRyE-k6GG1ZkgciTzr3qVkSiEuIIHCrxlQl081Sopirj0JEx-6L8xC4zgDF6K-Z1_2fWt0acuwKG6B2eVW88vKtvq1fqplqXgnmpj3ssCFC7zbNw5_54SClVwu0mXF_03PIAF0pFTH5LsCTsSAtebNStgv3I1xarRtP7TPJ1Pe-oepCegOCgnVV3N4nnCRqgxQT88LSd-BvzmOkU8JsnGr9Yl9HsUEaj-0WrJeomwxw7L9oPCb8RP5yWLRNu0n39HSZ6724A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) :
گزارشی با تأخیر زمانی درباره وقوع حادثه‌ای در تنگه هرمز دریافت کرده است.
یک منبع موثق گزارش داده است که شناوری مورد اصابت یک پرتابه ناشناس قرار گرفته است.
هیچ‌گونه خسارت یا پیامد زیست‌محیطی گزارش نشده و مقامات در حال بررسی موضوع هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71666" target="_blank">📅 12:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71665">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee29acd4a8.mp4?token=pArkhTMapF2y-Bjb6PdgWHU9RNcmhcVu-2ZmYRVmPIlawipYCN_0GYtWO8NOEWSoMxtpOMU11Wn5qKCawzWEqMiAgzcAzyCmVLTg8EYGEa5MA-2OMbz1a81zAsC4Q8h_jqR8dpkPAU06glmvHzh0LUi3HUYFbAf5IjMFvSAviXWSS0Jw9WJp2Pr-ir3Al1CAQK_LHMHhbXxDl6XwjpT2nkmXd35ffCceNcQz3udjwjST48dHIovs_TUZrsKxOZ73XZxuJzxVNA7Ib7sinILjJTG50-w_2nT5FzvFV9cpAx1u9HXHCOe-Jp6DU4pppAku9zyV-IThuD-rgqQrzymdNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee29acd4a8.mp4?token=pArkhTMapF2y-Bjb6PdgWHU9RNcmhcVu-2ZmYRVmPIlawipYCN_0GYtWO8NOEWSoMxtpOMU11Wn5qKCawzWEqMiAgzcAzyCmVLTg8EYGEa5MA-2OMbz1a81zAsC4Q8h_jqR8dpkPAU06glmvHzh0LUi3HUYFbAf5IjMFvSAviXWSS0Jw9WJp2Pr-ir3Al1CAQK_LHMHhbXxDl6XwjpT2nkmXd35ffCceNcQz3udjwjST48dHIovs_TUZrsKxOZ73XZxuJzxVNA7Ib7sinILjJTG50-w_2nT5FzvFV9cpAx1u9HXHCOe-Jp6DU4pppAku9zyV-IThuD-rgqQrzymdNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبه ناو سپاه با عنوان «رودکی» که در جنگ ۴۰ روزه منهدم شد در حال غرق شدن است. این کشتی تجاری بود اما به نظامی تغییر کاربری داد و گفته شد هلی‌کوپتربر است اما هدف حمله قرار گرفت و نابود شد.
در جریان جنگ ۴۰ روزه تقریبا تمام شبه ناوهای سـ.ـپاه و ارتش از بین رفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/71665" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71664">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71664" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/71664" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71663">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvU14PhTcthUwSwA4yy-3VWggmBmELpZU6jtEyVSUm65EvWH3jLslntFY22OcxKcLaEMMIR7Ay3Hw6lCAnt9GYC4i6z3bZXb68OY8hHEDOuEqMYtOK-zDXkJRi3OclDapcgPa7BwtmkY5r7Dh_77Fgp7BMDa2p-iXPcCLEX0KU6TNN9mqdLJANy-Vwz86z9jO8yPiADVzzICOmKjom0XTN1GgFOTo0BAkbFMBAu-Q1vQX4PREx3fB68DU-acxLvU1bayi2RU6g-9VUM_45DB05hbDkkjSODJ3Hk6VQUxdcidXjRwPktJR4xB1Lol0gAGozQTfUv6Y-AHWQR_RE8NBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
رئال مادرید
🆚
الچه
⚽️
را در TrexBet پیش‌بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
رئال مادرید: ۴ برد، ۱ شکست و ۱۴ گل زده
⚽️
الچه: ۲ تساوی، ۳ شکست و ۶ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/71663" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71662">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FT9UxbGmOFFF6HRBCFSyUrBQiDOFdVa8p7eujWaP0zHhwziMedVV2Kj68dLTEqL2OwT1Jge-fURVa3S-t7oXMyVuuo0IyCAZ2AThrkdhOZRXv2BDtjip0pQZ9d9fkJXZXZPNvUydDmR07MshhsqF-ghCiL8Wg1M1cciGhqBjXOCNeOLT81EeGc6d2buJzwLQnk60Vnzy5YCcRUt0_Q3soeK8fcUJhDS3AAD9CQeve7iufYuJXIflpvx37YsvkRAI3UA_QyPE6FFEkklfYh7BDtc-ShOsj0l5JZCJWpGPE3Uz6PXHp0AeRayITALhbKyOzVo2g6gcYhAhCJe_3hXDxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند هواپیمای دولتی ایران با شناسه پروازی «IRAN06» از تهران پرواز کرده و بر فراز ریاض، عربستان سعودی مشاهده شده است
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/71662" target="_blank">📅 11:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71661">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2f2bddd6.mp4?token=MsmvV8clz14we2K0XWH7XZAB_QC4lBU0B2axfos8qxsfK6M0SmDa1OezZYHOfWLQFgNg5adk0rVkm4n2cupKqkJ4ja-zcJuQ8AaS80bR3GN5-5J36zzRU3dvKiaFAm1ACzmzhBQGzQh8chMg3ifHj8xGD-F1g2FkKHqC1Mcis77dvWpWxS3TQNZ83L-Awur2UgmBkdsp2NA1DC1VShHV_Pjt5Zyj7K3qks0cIghxmrSu3u0ydSa0fOvYB2AV1vtQ5pMrFxHKzYcn4KwZtj5HisoCFJbsjJVMenBTL8m8U3oXOBxDV6gmI0GgDx204dn7w-uduQ0ky-Lq3xIgZhpW9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2f2bddd6.mp4?token=MsmvV8clz14we2K0XWH7XZAB_QC4lBU0B2axfos8qxsfK6M0SmDa1OezZYHOfWLQFgNg5adk0rVkm4n2cupKqkJ4ja-zcJuQ8AaS80bR3GN5-5J36zzRU3dvKiaFAm1ACzmzhBQGzQh8chMg3ifHj8xGD-F1g2FkKHqC1Mcis77dvWpWxS3TQNZ83L-Awur2UgmBkdsp2NA1DC1VShHV_Pjt5Zyj7K3qks0cIghxmrSu3u0ydSa0fOvYB2AV1vtQ5pMrFxHKzYcn4KwZtj5HisoCFJbsjJVMenBTL8m8U3oXOBxDV6gmI0GgDx204dn7w-uduQ0ky-Lq3xIgZhpW9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری: آیا قرار است همه ما تا ۱۰ سال دیگر بمیریم یا نه؟ موضوع بحث همین است.
ایلان ماسک: خب، متأسفم که باید این را بگویم، اما همه ما خواهیم مرد.
مجری: می‌شود یک بازه زمانی مشخص کنید؟
ایلان ماسک: بله، نرخ مرگ‌ومیر همچنان ثابت و ۱۰۰ درصد است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/71661" target="_blank">📅 11:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71659">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🎙
صحبت های این خانم درباره سگش:
خرج ماهانه سگم حدود سیصد/چهارصد میلیون تومنه
😳
روتین روزانش صبح حدوداً ساعت ۱۰ بیدار می‌شه، یعنی صبح همه رو بیدار می‌کنه. بعد تا ساعت یازده که می‌شه، یه مربی شخصی داره که میاد می‌بردش یه جا مثل فضای باشگاه.
بعد هم که ساعت سه و چهار غذاشون رو می‌خوره. پوستش حساسه و یه سری شامپوهای خاص داره که ما همیشه می‌زنیم.
شب‌ها من یه دور پیاده‌روی می‌برمش و بعد هم شامشون رو خودم می‌دم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71659" target="_blank">📅 11:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71658">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ea33bdfd.mp4?token=U5Cf3bttInFollQLRlPgawmke740xKZRZNCuaTn_HcSNX2kpJo94wJCClsThAR7fhYUbIwaOk-tnWua3B1XmXqlJS3aaV5CR3JnLpNOXDXFtJhGmH3WVrKEaBll1D61PzSJ1tLyvZqdl0FK3FpKBnU09hsJ2IJoRIU1pNhV-ja7Jp-BMkW-Iy9Ul2-DFhvaunowIVc00Aee2PH9s1lOGFsCnM3dfdNuMfjAZGGPMbsaqLmweGMWYfKx-VP5LLrDuDVDuZsJzq0qt-zINCS3BtewFCeOG_-hm8fK01qu0hT9XbZp73woCIbjqGpvOcPYTOinfPameKK65GOXx1rW1jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ea33bdfd.mp4?token=U5Cf3bttInFollQLRlPgawmke740xKZRZNCuaTn_HcSNX2kpJo94wJCClsThAR7fhYUbIwaOk-tnWua3B1XmXqlJS3aaV5CR3JnLpNOXDXFtJhGmH3WVrKEaBll1D61PzSJ1tLyvZqdl0FK3FpKBnU09hsJ2IJoRIU1pNhV-ja7Jp-BMkW-Iy9Ul2-DFhvaunowIVc00Aee2PH9s1lOGFsCnM3dfdNuMfjAZGGPMbsaqLmweGMWYfKx-VP5LLrDuDVDuZsJzq0qt-zINCS3BtewFCeOG_-hm8fK01qu0hT9XbZp73woCIbjqGpvOcPYTOinfPameKK65GOXx1rW1jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب علیه روحانی در تجمعات شبانه
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/71658" target="_blank">📅 11:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71657">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوباره آمار مبتلایان به کرونا تو کشور داره می‌ره بالا، خیلی مراقبت کنید
من خودمم دو روزه به شکل عجیبی گلو دردم
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/71657" target="_blank">📅 10:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71656">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/840407be05.mp4?token=LQfz4lvZN9mIcNIadPFhcJEP15PA86OnRF9rapaPiF6Rzd4JvgXrkOO-7LnO5MdzPHks5PYNJ1AUtesnrX2f3LStSqsH_2qJP-wQ4YiBSv9ajrv3paYwWlS4MkX01ui9jexOwrWcYuDCwoF3GvX9PZdBDsQMLZRTGFf8hHwahmu7RvEiOrfaBC4YRbH4kpylRFPWGlaHyDMq6dIcE58iKiYy1PRG-idKegSA3vaMQEEAapXb5X9OC_AupAEucHrf44E1sfUDI5JULnfJhgJKHKAN-gF4kxHK0Cuxw6h-AxpFrndFU5Bmf61sgpg5wrL081bYx8tfZI408NULBdCevA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/840407be05.mp4?token=LQfz4lvZN9mIcNIadPFhcJEP15PA86OnRF9rapaPiF6Rzd4JvgXrkOO-7LnO5MdzPHks5PYNJ1AUtesnrX2f3LStSqsH_2qJP-wQ4YiBSv9ajrv3paYwWlS4MkX01ui9jexOwrWcYuDCwoF3GvX9PZdBDsQMLZRTGFf8hHwahmu7RvEiOrfaBC4YRbH4kpylRFPWGlaHyDMq6dIcE58iKiYy1PRG-idKegSA3vaMQEEAapXb5X9OC_AupAEucHrf44E1sfUDI5JULnfJhgJKHKAN-gF4kxHK0Cuxw6h-AxpFrndFU5Bmf61sgpg5wrL081bYx8tfZI408NULBdCevA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلار شده 240 تومن؛
همون لحظه صداوسیما:
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71656" target="_blank">📅 10:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71653">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a54c7cbd.mp4?token=AMc4MXCdCeLWqn8-9plkZyPfo2eY9YtVDiM0UVHO4RM6ooVy-Rhgywfpo-I0Ax9F_Yq3X70DYIQsMgpmviw3K8Hc1rfie-8OGBAzk-hAq1jj7wKlJ77biODBkMSnqlue1oKyrAaOCw4iTQtGClKpUsBkZc6USh9ggZPCvM8eaNfreZJTgJ8phZhixZiFk73V8-kIayQhnyhBuh-2i9-LVvK3ojNkFFYuZ-jZ1t4IZign0yI4XejWNEoArXpRhvSpllB0aH27NT1suJ8bRFW4yz5dmpcsAOPmnjmBAsrjspiTGfViMJ6FVBHEmKrRB48bhs0VIYqNPzMs1pwVW_53jaOD2YtR-7ZPKUYvc5_WKTlTvMuPWsSzkoEStIG16mFlYY59jwxPfde5N0XPefvWcKl8s_mMXZmXlUEyTG0HFjFmJAUgvYjy1EacpPf__bro4wonVlgNudEF2KWkc16lhxuyUEbDF9Eblm9iFyajOxJca3WOPWGErkVo4CG9OHdXhA_LTXmB4DlddRfYjh7T5ASHsK2B7ZJT0o9hUbyUHcV26I3SCzEx9SFsBjK-nQ1UlW6S6OAegWmvucZw_Bpwst2JjbeW2dWnIicNWCO1k7c29Y2NLrZHa8rZYLw8GwGJBPl5jRt_I7JO_RkDL46Va-emPLc2NzQoWIPuhHuC3TU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a54c7cbd.mp4?token=AMc4MXCdCeLWqn8-9plkZyPfo2eY9YtVDiM0UVHO4RM6ooVy-Rhgywfpo-I0Ax9F_Yq3X70DYIQsMgpmviw3K8Hc1rfie-8OGBAzk-hAq1jj7wKlJ77biODBkMSnqlue1oKyrAaOCw4iTQtGClKpUsBkZc6USh9ggZPCvM8eaNfreZJTgJ8phZhixZiFk73V8-kIayQhnyhBuh-2i9-LVvK3ojNkFFYuZ-jZ1t4IZign0yI4XejWNEoArXpRhvSpllB0aH27NT1suJ8bRFW4yz5dmpcsAOPmnjmBAsrjspiTGfViMJ6FVBHEmKrRB48bhs0VIYqNPzMs1pwVW_53jaOD2YtR-7ZPKUYvc5_WKTlTvMuPWsSzkoEStIG16mFlYY59jwxPfde5N0XPefvWcKl8s_mMXZmXlUEyTG0HFjFmJAUgvYjy1EacpPf__bro4wonVlgNudEF2KWkc16lhxuyUEbDF9Eblm9iFyajOxJca3WOPWGErkVo4CG9OHdXhA_LTXmB4DlddRfYjh7T5ASHsK2B7ZJT0o9hUbyUHcV26I3SCzEx9SFsBjK-nQ1UlW6S6OAegWmvucZw_Bpwst2JjbeW2dWnIicNWCO1k7c29Y2NLrZHa8rZYLw8GwGJBPl5jRt_I7JO_RkDL46Va-emPLc2NzQoWIPuhHuC3TU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوهای این خانم معلم برزیلی مهربان و زحمتکش بخاطر سبک خاص تدریسش حسابی وایرال شده:
تو یکی از ویدیوهاش که حسابی هم وایرال شده به یه دانش آموز فوت فتیشش که درسشو خوب بلد بوده به عنوان جایزه اجازه داده پاهاشو لیس بزنه…
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71653" target="_blank">📅 10:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71652">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f71ea40a.mp4?token=Y5UbOJbNNLIgIhN2Tn_OybbLA55MKNJ_8l49ZOCQHELcndvEMEIv-Jf76E3REKDf9Esg_LbKJo61TqP31m3xTbgZumX3xMEJf51sLBfDLM9eANPED7wxRzP3tnT-UkddfK8jY1mqzw-QklwgYMBuetLA03wQ4INTK8kTxm0X9xc3fIYqPkKlDlESWYcACwzXNAX_qNIK5RfXG-0C-8CTU4Vi-2KnZHflv7t_C1VKziVDQDZESM3oYuN94znDpqJ3eqy1PUSxwpgS-fyjsz_qaCB16U6mKC00B7KNls6BDYIoib0r7SxVbQjKKzZGmubPWRFM4hlEX_ZL_oNoghlAeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f71ea40a.mp4?token=Y5UbOJbNNLIgIhN2Tn_OybbLA55MKNJ_8l49ZOCQHELcndvEMEIv-Jf76E3REKDf9Esg_LbKJo61TqP31m3xTbgZumX3xMEJf51sLBfDLM9eANPED7wxRzP3tnT-UkddfK8jY1mqzw-QklwgYMBuetLA03wQ4INTK8kTxm0X9xc3fIYqPkKlDlESWYcACwzXNAX_qNIK5RfXG-0C-8CTU4Vi-2KnZHflv7t_C1VKziVDQDZESM3oYuN94znDpqJ3eqy1PUSxwpgS-fyjsz_qaCB16U6mKC00B7KNls6BDYIoib0r7SxVbQjKKzZGmubPWRFM4hlEX_ZL_oNoghlAeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوستاد خوش‌چشم، کارشناس صداوسیما:
در عرض ۴ ماه موشکی ساختیم که هنوز اندیشکده‌ها و رسانه‌های غربی موندن که سیستمش چیه. موشکی که بدون نیاز به ماهواره، ناو در حال حرکت رو پیدا میکنه و دنبالش میره.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71652" target="_blank">📅 09:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71651">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/168229fd60.mp4?token=JajxvmGGkCSqxPYOaKLF_QOtLhYnf5dYv2QiOjEPMKD2TqdxioXUtym6BPooQUyiuAy2UY-t6AmnokKlhGuKsxTs4X1lJPrVHvr2EHZqnN64T9c081d1q1mL28NRKqxdzdq1qHmltsdX8JkoSo5fwTcLcAk-6RZLBs5TBQDyTwl-VcfK0IUyr5eEyZUKc2YiLxigqwKEFQQrqK_gdTMd8R2PZT4tFM6p0QkJz8y__6ipU4ccJp6x2m72jqe85M6Xd-CHRgIL5d2NFXtJtKQjEevyrm_jUbw2x2sWsR51kTOvRq3hfP5pSz1HpJyuwa8YneDRr0505KfczdWnPp_G8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/168229fd60.mp4?token=JajxvmGGkCSqxPYOaKLF_QOtLhYnf5dYv2QiOjEPMKD2TqdxioXUtym6BPooQUyiuAy2UY-t6AmnokKlhGuKsxTs4X1lJPrVHvr2EHZqnN64T9c081d1q1mL28NRKqxdzdq1qHmltsdX8JkoSo5fwTcLcAk-6RZLBs5TBQDyTwl-VcfK0IUyr5eEyZUKc2YiLxigqwKEFQQrqK_gdTMd8R2PZT4tFM6p0QkJz8y__6ipU4ccJp6x2m72jqe85M6Xd-CHRgIL5d2NFXtJtKQjEevyrm_jUbw2x2sWsR51kTOvRq3hfP5pSz1HpJyuwa8YneDRr0505KfczdWnPp_G8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواب رییس کمیسیون امنیت ملی به روحانی:
اون روزایی که تصمیمات غلط میگرفتن اون زمان دنبال رفراندوم نبودن بلکه دنبال حاشیه بودن
اکثریت مجلس خواستار برخورد قانونی با روحانی هستیم و این تقاضا رو ارسال کردیم
قرار نیست یکی تو گذشته مقامی داشته الان از عدل الهی و کشوری مصونیت داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71651" target="_blank">📅 09:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71650">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71650" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71650" target="_blank">📅 01:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71649">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0jDSmw3T03usGSjOL5uL5MXBgIMZu2B4KznWCqw820l9B7AxAiXpODuQLPS1c5PSfTA89OFY9Ks3zy-R3CI3NxpdFGlkxNZ26Pe-ZcUbr00BqgPBkUZ04BNPl3sTXuNS_TlnJXwf-RwSyb14SuAZQ-bsvQGPVnCHVci-E9HzwW5MFV5FGryvvR80usES8UrSWBqF07UQStqYppU07pprbDMmjTPuSWUcDeYPFfKt_SO8cPB2Zmdf432gD3q5AlcRuocDegUtQ1kPDf4ugyBckwpOEdnKijX1BVVP0wquBADDmjXTQqnKKWVwd3Skh4bSA0tg0_u3C1TDLiHKGEYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71649" target="_blank">📅 01:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71648">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8b5c1f510.mp4?token=ougQtyWAoe3dXeUaF3inUPRvlvUX99hk3IJdIxY-JIIkOW1ajYe7PD3x9DkLlej7s-klAxRUPKg7d14BRVW0Ihu8_mahXSLljZb8jV2kHb63CFU-WT4KqqYgvssMBNITKz9CM1AbolwJA5_UKayvkqEfdky7VvIdKPjjmCTSqp1wXOGa2nbhgANF9ShTJlR99uNKNyMnp1vIkxgvOYBVgwkS5Bb7LrCXWm9esfHZHDbyHtn7Ch24JX387yzt7h9VMvPFfW_5SUhVRiSANxi3r0d19ILH3RIE3fJQd_v44EXq2m3TLS5NNzbBGBwu8ZEh3emka9WtdvLllMZYbuSAHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8b5c1f510.mp4?token=ougQtyWAoe3dXeUaF3inUPRvlvUX99hk3IJdIxY-JIIkOW1ajYe7PD3x9DkLlej7s-klAxRUPKg7d14BRVW0Ihu8_mahXSLljZb8jV2kHb63CFU-WT4KqqYgvssMBNITKz9CM1AbolwJA5_UKayvkqEfdky7VvIdKPjjmCTSqp1wXOGa2nbhgANF9ShTJlR99uNKNyMnp1vIkxgvOYBVgwkS5Bb7LrCXWm9esfHZHDbyHtn7Ch24JX387yzt7h9VMvPFfW_5SUhVRiSANxi3r0d19ILH3RIE3fJQd_v44EXq2m3TLS5NNzbBGBwu8ZEh3emka9WtdvLllMZYbuSAHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل یک عملیات ترور علیه یک فرمانده حماس در غزه انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71648" target="_blank">📅 00:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71647">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3D_mGOTMAd6OYgGUNceJA-gfd79ZV-gO0OckN8p8MSO_lawfzei3IS7a2miv_eT7Vi-RxfyM7eLHP_f-h6mW4HivsFYLgDKc7G7_Vsq5shdiPhk0U7rTYcTduP9qP3e1mdSh123UoczRf6U3ZrneEhkL05bLc_ohm7w8QACnGP_03wJElSAcNNj0stnO5QsPzHTyFhrbjysbf7w_6-NzqH8MEROzctLTY5NnTZyUGg_rkfc_g4ULsw5FHZsz4PfPkUg26_3otiTVraqJuFbkRYyX5XJJZxNPwiYF7K4yCN5Ep0mTvEqwNbngBXdxJoD44zaAxLcijexrqLDmYqMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
با سیگنال‌های متناقض رئیس‌جمهور آمریکا حواستان پرت نشود؛ از «مذاکره نمی‌کنیم» تا «برای گفت‌وگو آماده‌ایم». معادلات مربوط به نفت و تنگه‌ها تغییر کرده است. دست و پا زدن برای کنترل تبعات، جلوی آنچه در‌راه است را نخواهد گرفت.
تا زمانی که شروط ایران محقق نشود، هیچ مذاکره‌ای در کار نخواهد بود. تمام.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71647" target="_blank">📅 00:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71646">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فارس:حمله پهبادی ارتش آمریکا به دو قایق در حوالی بندرکرگان در آب های خلیج‌فارس.
تعدادی از صیادان مفقود شدند و عملیات جست‌وجو و امدادرسانی آغاز شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71646" target="_blank">📅 23:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71645">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itiUeTnsu8Jpb10RE4Bvb3H9ZCLhouTwXCfOiJMOOlBY3OlEFmfTj5MRvPY8uDGpq0W1VvfPeN7kpmEZknCKbEStpm93foMsSN1oZ77rb6Y5G_iW4TqJP2V3-LqcSUHb273ylFTAK5O54eSe9kdvtXLgWiGxTi2N8pPNEbGAeJxaRuI4689z1YtWyyTx1bfE2EyCGaNwHcUgXjJJH6X3svaH_a8fhnl8XoOnPaB3na4HKQg76k-HjJS6DUEjnVOECBw18d2FaMJpLnkUBLL-2bC9KXOcUakFHmWv7HYMUWfCtotG1Yk3SLpcHwmEOlMm9Dx_wz7q1sZcZK_FoHuszw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
ماه گذشته، نفتکش «ال‌گایا» با پرچم پاناما هدف اصابت موشک ایرانی قرار گرفت و از کار افتاد. آخر هفته گذشته، در حالی که این کشتی در آب‌های ساحلی عمان لنگر انداخته بود، ایران بار دیگر با استفاده از پهپاد به آن حمله کرد.
این نفتکش هم‌اکنون توسط یکی از شرکای منطقه‌ای در حال یدک‌کشی است. ادعای کذب سپاه پاسداران، نمونه‌ای دیگر از دروغ‌پردازی‌ها و تلاش‌های این نهاد برای ارعاب و ایجاد مانع در مسیر تردد کشتی‌های تجاری در این تنگه(هرمز) است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71645" target="_blank">📅 23:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71644">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دیروز در بروجرد گروهی از معتادا در اعتراض به شرایط بد کمپ از اونجا فرار کردن و با این کار انعطاف و آمادگی بدنی بالای خودشونو نشون دادن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71644" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71643">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71643" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71642">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71642" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71641">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSnwu3rXMIBfm43vb_buTUmt8liyqnF1rJOc1hoFNgnK2sKY5ee26hJJUgbaxpcqmvfFXlfKCF1fMbj8J60M9v9Cjt-ATScSSlN5BhugthQ-WbUUH7aBS5DMoLVXzedo-8JKXKQWmvTjgIvZAba0kma3ac4KxwL6xwlYshre4KMAhdB3BglcF33S-8w91fq_RCKsi8DbKkmT8d-6OYiIOBAGRMXCsCkh4iJrXmX1ppx7ndSqVJW3854UgLwoGvsfa_e5LShIUUNMVhwd4K8lcIPqaJFneil0WGgTHcb8cyKcDl-LIpSpIXcCo3icU3PHLSxAgYPNmvO6-2xlEe1v9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران:
نفت‌کش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در جنوب تنگه هرمز، با یک مین دریایی برخورد کرده است.
تلاش‌ها برای مهار آتش بی‌نتیجه ماند و تمام بدنه نفت‌کش در شعله‌های آتش می‌سوزد.
سپاه پاسداران اعلام کرد که پیش‌تر درباره خطرات این مسیر غیرقانونی هشدار داده بود و تأکید کرد که تنگه هرمز «همچنان بسته و تحت کنترل هوشمند ماست.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71641" target="_blank">📅 22:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71640">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d776b60914.mp4?token=veJZh9t3ginHKJ8oxJo2FwtgmrFqkONb3w3BkGRRE7I8E37ANAvaAcOVIqoGG6iXXWIJYIY-ExMLzKn2a-erkoM8Igad2LvkidkDjFy1cylSHfD7XOl3A3GLKw_7xLsPeL2d18BxqeElCPEv4ddw8i8SvL0i-VqoFuOoJKSA91JkqYj2fG9xtl6yr2AHyjsPCWEBC7TqAOYQvATfIxhag2-RquAqboR4lp6DdSzvpLQIMcA606LzlN2DaUvVdOiYbvBqWzBf_bLntm2zHETlQlJvAvs7iMRlwdtrf8OWSzUeqNWT1lNEPpHgmXDZZryHUfV75xReu8i9c1aBEvjGxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d776b60914.mp4?token=veJZh9t3ginHKJ8oxJo2FwtgmrFqkONb3w3BkGRRE7I8E37ANAvaAcOVIqoGG6iXXWIJYIY-ExMLzKn2a-erkoM8Igad2LvkidkDjFy1cylSHfD7XOl3A3GLKw_7xLsPeL2d18BxqeElCPEv4ddw8i8SvL0i-VqoFuOoJKSA91JkqYj2fG9xtl6yr2AHyjsPCWEBC7TqAOYQvATfIxhag2-RquAqboR4lp6DdSzvpLQIMcA606LzlN2DaUvVdOiYbvBqWzBf_bLntm2zHETlQlJvAvs7iMRlwdtrf8OWSzUeqNWT1lNEPpHgmXDZZryHUfV75xReu8i9c1aBEvjGxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه آخوند درباره سرگرمی های روزمره :
سودوکو بازی نکنید اعدادی که کنار هم قرار میگیرن یه رمزه یه چیز نهفته رو آزاد میکنه
فضای سیاه سفید تخته و شطرنج هم شدیدا جذب کننده اجنه هستش
🎙
مجری:
اونوقت بگو هیچی بازی نکنیم دیگه
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71640" target="_blank">📅 22:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71636">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k5jd39p67Gv8XiMbs6rJQz2aRTSeXWYkrz9v31QP7oVTlNLDY2qqmViaCekTdLZ4Xv1FFKCJRZH9SyetXRoQ8iD6SLZ3MPXVV5GQT1pb0EaIy-K3mAVCIswUiJ1NwwmfmcPdAPm9zjWr_VAn3bBUZZwTM0GekB5oXHUEej17s7QrbWv-tQEly7tRI-F_c5hLvX8_Bg8QHIfQLutB0f-y3DuJcZfuscaMrv0Pw_NO2HPW729WTMaCzcFCqpIpDXLMHecSKY4yulls6grCZetooqCdZV_a_r_sEe0WpR-jEOQx5-LwUVycrhgcTEoQFTPiQ1u9RXhO94Ks2T6VIBIEqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZdlvTHfJpDE2fNXvmOWOdaiciWo5L2Vn0ZIpJ5wGp4HoFsqId58QlkSPLJW_Jn0rtJ8vD2aak_-pSjduksDFbMlTdJEunlIkXp2dJk1zej7UyZ2Hi7ybS6bFb0xlyA2KxNRuJmC8qZJNmmbW7UBhGcwv1HpUGh0T0Xt_o51s01tK9YFEM9yI3QL9Rfvs2SAEzhARxDLUsav_862ysuyz_7KEZnTKCHa6Q2aACJlDv8SYzR0Ur7pGXwoZp6oRqLHackorPQJRO2iQ8Z6Ra2WCvUP3W8RHmX58i4ehjZFq5qnwd4w7v6EeXwRukaw1FvO7xslEAxE25SNNDTsv-MOTHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیامکی که داره برای مردم ارسال میشه، از فردا رسما جانفداها برای شرکت در دوره‌های نظامی و امدادی، اعزام میشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71636" target="_blank">📅 22:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71635">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f9266483.mp4?token=vc-4fFD4Lk1t5OZ4hlOet7NfnBqOAi4UCNiTUeoIHrjk5v8ewrexcOvAUrLxKRl_LIYkA-4egIpmDHxL5q5It3jJWuwxOpMf9AwAFGUh7gGTD1VJKzGsdxZ7FcNOF9qELf5vvpdz_W32sAZEfDGOdEHhGVnlZG0y5ftQ99GtElpWDeN9zW5UrkqQDxgZ_QxSmEJ71M0SY8_0baCQQVhIP99p_90IwSbouiIZk_v01b6j401f0IhH05JqjULNTU4WF4yY6bQDv7HGyZw87buDf7-YtApzRikX9wGkrcrDPzVa7kfDjLIJ_t0CTziFRqd9za_b8GqQXXxpIpyOpRWwIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f9266483.mp4?token=vc-4fFD4Lk1t5OZ4hlOet7NfnBqOAi4UCNiTUeoIHrjk5v8ewrexcOvAUrLxKRl_LIYkA-4egIpmDHxL5q5It3jJWuwxOpMf9AwAFGUh7gGTD1VJKzGsdxZ7FcNOF9qELf5vvpdz_W32sAZEfDGOdEHhGVnlZG0y5ftQ99GtElpWDeN9zW5UrkqQDxgZ_QxSmEJ71M0SY8_0baCQQVhIP99p_90IwSbouiIZk_v01b6j401f0IhH05JqjULNTU4WF4yY6bQDv7HGyZw87buDf7-YtApzRikX9wGkrcrDPzVa7kfDjLIJ_t0CTziFRqd9za_b8GqQXXxpIpyOpRWwIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
سیاست ما روشن است: ما به نابودی زیرساخت‌های تروریستی در «منطقه امنیتی» لبنان و رفع هرگونه تهدید علیه دولت اسرائیل ادامه خواهیم داد.
به دشمنانمان می‌گویم: اگر تا به حال درس نگرفته‌اید و تصمیم دارید دوباره به ما حمله کنید، ضربات سنگین‌تری متحمل خواهید شد.
هنوز کارهای ناتمامی باقی مانده است و به یاری خداوند، آن‌ها را به سرانجام خواهیم رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71635" target="_blank">📅 22:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71634">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-4ia36pfDiU08XNdxtCBMLJ1jK_mfvyGynHohV65_cFSiM43txwVxLyyn8vGZaRJK3OMyC7tFVGHq44tkb7aRAkaQCy_iF4rJxtqscbkeLKPzHDk5jidKtL6qT4nqvH7LcXGZewdTiC6vVzUL4TLoBNwEnB1J8FbCi1tVDhl-u4QzOsL2zYWi97JUDN_D3W2W6xLvWDx_NZfVDpqGVyTeR6rZ7ehe0Sf_ctm31PC5oWLYKKicfmGJT6X4hJu8dKrGTVQcPblFznsdIt06_-BsfqPncWyGO9hPQl_sKiLqaYiZyLMtTHFyJvOr-rH1NfIINmZj5ZIsjbDaItXCAxiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
❌
🇮🇷
اسکات بسنت وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری «عملیات طرد اقتصادی» (Operation Economic Outcast) را با هدف قطع تمامی شریان‌های حیاتی مالی رژیم ایران و حامیان آن آغاز کرده است. به همین دلیل، من فراخوان جدیدی صادر کردم تا افشاگران اطلاعات خود را درباره کسانی که اقدامات تروریستی ایران را تسهیل می‌کنند، ارائه دهند.
خطاب به هر کسی در سراسر جهان که اطلاعاتی درباره این شریان‌های مالی دارد: این فرصت شماست. اگر اطلاعاتی قابل‌استفاده برای وزارت خزانه‌داری دارید، ممکن است واجد شرایط دریافت پاداش باشید؛ فارغ از اینکه کجا زندگی می‌کنید یا چه کسی حقوق شما را پرداخت می‌کند. اگر چیزی دیدید، اطلاع دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71634" target="_blank">📅 21:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71633">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHAZXITBkfSjZXU9vfXjjAe5_bWvYVBwpSY_X-MaGuw13PlHC4ZwS6LRrPqtN0JyfJsl3hDRcMyMWAGrqELUGbBbNYWIuUx8b9DvNSiHKMdgJn2wjuIZ8bWXqzUXQh-jzIKs6NPv3f1ehsdpSiBvkCA9OmGu0L4UOc9vjb-iNXL4UL7QmrjqBUFlmPtpBFla7QaWCzf7M4dudRFS3RgTE6xX15kEksLnnvM7Bd1aX901WOOif-7BCPA4LlUtTKp6gG619fWW6UDoYz-1Ban9O89emO2djJU_vbzJXvIkpifEP-9QQj_Mf4oBblBHP8TQ5kFtgZFDKy35AAxnOj2vEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
نفت در حال عبور از تنگه هرمز است.
کشورهای جهان — که هیچ‌گونه کمکی به ما نکرده‌اند — باید پس از پایان یافتن این غائله و فتنه‌انگیزیِ ساختگی، هزینه‌های ایالات متحده آمریکا را جبران کنند؛ و قطعاً چنین خواهند کرد.
ما این کار را بسیار بیشتر به خاطر دیگران انجام می‌دهیم تا به خاطر خودمان، و نسل‌هاست که چنین رویه‌ای داشته‌ایم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71633" target="_blank">📅 20:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71632">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nqz7TzyH7WcSp3Gs5E7LAF65vmtq2APopyuQWYplavVWGzDFuACxyyPcPPU8jLvZGmTJAKAMWj3VT8dcjgYKZPVA98fs-tDgJ8EfNuKF43gxS2OsttAfpNGhHmDDKCq01s1cPWXTsKLBixfzjeI-86QDYTCLW8CG_7zhhOsnTc6grGbQP8pcSMdeR4PPyODFKfjeheBVPr1UEjAuID9neJmfD45uJ_EsBjah_Qh-nXVIjxwCFb_QpHdR2_EBmQbKcdh9CiqWQRwYhqgiUAWlAx2wOU8IPDnCcgViBZSoj5BERLzBBZKwoxBg6Ula_mIdEVjnUw-WoXz2zl99-kzF5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
امیدوارم همه متوجه باشند که افزایش قیمت‌ها در سراسر آمریکا ناشی از عملکرد «جو بایدنِ خواب‌آلود» و دولت او بوده است، نه «ترامپ».
حتی قیمت نفت در دوران بایدن بالاتر از سطح فعلی بود، حال آنکه ما مانع از دستیابی ایران به سلاح هسته‌ای شده بودیم!
به‌جز نفت که فعلاً وضعیتی متفاوت دارد، قیمت‌ها به‌شدت در حال کاهش هستند؛ قیمت نفت نیز به‌محض پایان یافتن درگیری نظامی با ایران — که زمان زیادی هم تا آن نمانده — به‌شدت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71632" target="_blank">📅 20:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71631">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-l6RLb9KSPpgw1bW4uS2PgiUMAQ460aix5QoF9FuCik5sJxHKPPl14CR0kcJSMpp81n2FecQ1MN79Rosbk0KDzk-17DJblWDp4i_LFfbLK04OUIpqYWPijGwNmwkOwrodC9R-VwNlmh2qP9jQfP9tQ2Di81MQMMhuGqG--P_i4mtQuokdJ-RGk0bA5AEqlRwTsBkWHPqWNXYni1MCzeIZVk9mSS1S1E2-EFMp1U1v8xzZg99YH45D-41Miz8_BPtzfjikEXVRQngVJU6HZH8KPVyzLmuwtstT5JO4ipW2sId3HkU_Ektgw4JNE7ai1DppxDEdxqJFsHKLgsRE66bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
من به تازگی گزارشی دریافت کرده‌ام مبنی بر اینکه ایالات متحده بیش از هر زمان دیگری در تاریخ خود، سلاح‌های نفیس و ویژه تولید می‌کند.
این سلاح‌ها روزانه به نیروهای ما در خاورمیانه و فراتر از آن تحویل داده می‌شوند. کارخانه‌های شرکت دفاعی ما به صورت شبانه‌روزی در حال فعالیت هستند و همزمان به طور متوسط هر کدام ۴ تا ۵ کارخانه جدید در مقیاس بزرگ می‌سازند!
تمرکز اصلی این تولید بر روی پاتریوت‌ها، سیستم‌های THAAD، تاماهاوک‌ها و سایر سیستم‌های موشکی استاندارد بوده است که ما در حال حاضر تعداد زیادی از آنها را در انبار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71631" target="_blank">📅 20:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71630">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
تسنیم:
ایران بارها اعلام کرده است که به دنبال مذاکره برای رسیدن به توافقی با دولت ایالات متحده نیست.
ترامپ همچنان ادعاهای نادرستی درباره توافقی با ایران مطرح می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71630" target="_blank">📅 19:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71629">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:  «ایرانِ در حال فروپاشی، می‌خواهد هرچه سریع‌تر و به‌شدت به یک توافق برسد. این من هستم که تصمیم می‌گیرم آیا آمریکا وارد این تعامل شود یا نه؛ البته ما در اصل، با چنین ایده‌ای مخالفتی نداریم.  @News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71629" target="_blank">📅 19:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71628">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THBZcuztfbSZQvmOFGfaoWvjc2yRp3gGe-o7vjI8jM6PTAIfnKNIsg1gLJIhi5MKBWMlSQcJpBe8b_PgGnBx5R2X2NvSSEJOc1dSvj6_1iun_kR9X1m09Ds2v7aWDlNP7AxB1MFF9UrpDkgNkLPO451_Q6sM9ZMMVg6cnRncan7nBQRTk0OaccP_3dJ7JcigpugSKG0qKT0IOxRGjhwn-uy6TJBvT-3S-lWwibGP-QC6k_gPNj2ynpYiRC9LjmQ5-JNMIZC8e7gRtb4X81d4ugtS0M84pD15zU2SmGmj8sEveBDiIj0WklO_CVzKi1o8ZNHU4eTin0NfXno9bI3vBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
«ایرانِ در حال فروپاشی، می‌خواهد هرچه سریع‌تر و به‌شدت به یک توافق برسد.
این من هستم که تصمیم می‌گیرم آیا آمریکا وارد این تعامل شود یا نه؛ البته ما در اصل، با چنین ایده‌ای مخالفتی نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71628" target="_blank">📅 19:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71627">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7f7efeeca0.mp4?token=hloZfamgnA-_qcnECzVS1cWyg07pPAiA4ylnI771ZwKguSOyza05jWUCTvXi6APPNLquehXEL2vXk490cnVbgv4kEcjE_UI0pakm4meokmjtWIThxFdIrwbq2hl-1kqn61aFzTc-1RImO_cN4ymTWadZ9FCbhl_mlXgg-blPLiUe4ha6ZVEEj45Omc1b5rpjATltWyujuF02QPeTh6JqvR5b83O3b_8Mf7_w0-VjsUVX6gaaQD4UJ8e3sXXCZodnlyiqjocy27N-M_TyequinEtVdA35csc7sckh861hcrG5rH3nGmOp8fry4NGRnSZq1T044-DHi_Z5q3cw1TVpzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7f7efeeca0.mp4?token=hloZfamgnA-_qcnECzVS1cWyg07pPAiA4ylnI771ZwKguSOyza05jWUCTvXi6APPNLquehXEL2vXk490cnVbgv4kEcjE_UI0pakm4meokmjtWIThxFdIrwbq2hl-1kqn61aFzTc-1RImO_cN4ymTWadZ9FCbhl_mlXgg-blPLiUe4ha6ZVEEj45Omc1b5rpjATltWyujuF02QPeTh6JqvR5b83O3b_8Mf7_w0-VjsUVX6gaaQD4UJ8e3sXXCZodnlyiqjocy27N-M_TyequinEtVdA35csc7sckh861hcrG5rH3nGmOp8fry4NGRnSZq1T044-DHi_Z5q3cw1TVpzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ رفته ایرلند و چپای ایرلند هم برای اعتراض این حرکتو زدن؛
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71627" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71626">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71626" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71626" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71625">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp1rWXjdMbjEWKeSJq84ADZMZ9j8R3bCCjynbLAYf46rs5DdLO824ToHAGPbKG5mvJyk5bpEZgnhd6IRTTQuAEikBR4qAqF3K-zgqZPLBTJVdOPw2Id1-tcnxDWSfZkQHNQT-oIDIbMhmIgkDO3SxJNeRwHVjM0O_Uay85UgaIVmU0NxGyZB0PmZ9Bn7HgPV6m6y2zsnZ2NC4J-ZdzKi2rroDAu9MpEoFuhNW3TJieeQJCSWnC0ys43OfUa0HCYU0SoH8GuJxD-CrJ8lHsoX0ZvnnLobAGukIlro10003T9b_GLRQE7IUZ_N9PC_UYkeuTJeCu37xRyR3wC190Y12g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
شب بزرگ فوتبال آسیا !
نبرد هیجان انگیز
⚽️
السد
🆚
استقلال
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل دو تیم باهم:
⚽️
السد: ۲ برد، ۳ تساوی و ۱۰ گل زده
⚽️
استقلال: ۳ تساوی، ۲ شکست و ۶ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71625" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71624">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqwEikuyYDf9qD4OrSg7rSlRsLQ7TFRsVs1MCplyFReFGEHlkyhWjMPt70Uv6kBL7F8_kvXozfy56GIz7Mf69ahjHvNhb9ZUgQCB19ZyU8peDp3lscCcQHtqVH5ykcGNNvsMREEUz_6a6o9Ic2r9pixKBck-GB3OxCndVAEN8VswX-PrhFAxX_XmlFfrf9GVhxWgOBK2BktttNQ7vqMFJbiFz87TxSGxZAjZcSkNM78HangUaT0qVwvr7rsQTkI5Y4-jj4-S5I4F4l1QKKPNNxWCE6c5SdW6TJxB8kY6L22EzxmrByHzjGBs1f_JvxielsJ5X8ZdnB_On4gZyK_b2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
اوکراین موافقت کرده است که به تأسیسات انرژی روسیه حمله نکند؛ روسیه نیز متعهد شده است که همین کار را انجام دهد!
افزایش قیمت جهانی گازوئیل عمدتاً ناشی از جنگ روسیه و اوکراین است، نه ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71624" target="_blank">📅 18:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71623">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
دقایقی پیش چندین انفجار سنگین در چابهار سیستان و بلوچستان رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71623" target="_blank">📅 18:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71622">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
ویدیویی از عملیات نجات افسر تسلیحات ملقب به "براوو Bravo"(زیرنویس فارسی)
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71622" target="_blank">📅 18:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71621">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exleDvIFcVQBIgNcX0gGhvsiFI-sLQIQmwxlo9m9LmKB6Qoq0NYAhglxGRxVoBZmJm8Ouz8Ms4RDwA33jEKvIl7wXH0D1hUJy0Zi771puMHLN4nUtqRhcLSG6Gk3jGvhOtJ65cKcfR-UOZmZ4H2z03bWUSengEeL_h1NVo3BQ57V89VqNJe4G30ztXHlkZmrLzsXN0XZkGW9f5vQTflGAsR3Wo8Z8lYSHPhoI60eLRTeoWYC7am9UuWuhi_u2MMi6DyGMSbu4kpZYjzmKTBR_ry3P9sY4xctDK0eN2vSCxMdPiLYHVlpiyKu2SnK8XwiZ8bm3fyH2hRVmXbxwpfzew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو هفته آینده برای سخنرانی در مجمع عمومی سازمان ملل در نیویورک خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71621" target="_blank">📅 17:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71620">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36d8765cb4.mp4?token=HE2-vrmIxE7Ed4_64wbzpvBvTosOLsREaRNelrNd6seojwSW1_osvkkpIyYTCLKpp7kOMCo9f0qC-58v3jLukgBR57KhoZqfjafy6VqYW95PEbwhnuGuaohHT3gKxpaXcBPI3tFIB7SXDd-1VRa8-UBK4S8sx2DlhRJTL0jDj6oswULTRtynadeStCxDbskb4rNrkpWtES0oxpP968Up4aUdrGu7iE3qTtWuoAQUSsBgU_K8SctYD01CSK3JlWuCBDMbiZn3F0f2dh2bfneuBQAqA2CbuO9Nu3eVAKFmbEhYMqMlYJFiRh4nCPPJmowdSc78T48smZel4DlfxFjgPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36d8765cb4.mp4?token=HE2-vrmIxE7Ed4_64wbzpvBvTosOLsREaRNelrNd6seojwSW1_osvkkpIyYTCLKpp7kOMCo9f0qC-58v3jLukgBR57KhoZqfjafy6VqYW95PEbwhnuGuaohHT3gKxpaXcBPI3tFIB7SXDd-1VRa8-UBK4S8sx2DlhRJTL0jDj6oswULTRtynadeStCxDbskb4rNrkpWtES0oxpP968Up4aUdrGu7iE3qTtWuoAQUSsBgU_K8SctYD01CSK3JlWuCBDMbiZn3F0f2dh2bfneuBQAqA2CbuO9Nu3eVAKFmbEhYMqMlYJFiRh4nCPPJmowdSc78T48smZel4DlfxFjgPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
یک پهپاد روسی «گران» (Geran) در بخشی از جاده در شهر «پاولوگراد» که مملو از خودروهای غیرنظامیان بود، سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71620" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71619">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f9fc5142.mp4?token=gxmXZYCgDIH9aKbTzoNbZqH8rlV0cS3FipJyIJx4Ie_4MZNVmi02iV_VoL1BNOPe7e1msInVAu3lJxxXYZJqduArlu8Y_aL2x2j93Fn614spT6MKt9ypVp9bGLB6SZgwF1dLfXR-Mr7UEq0AHsvTz2rz7FlxA2B65K67uBsoZHy_4P5o4eTjKUpb1eCRTJkX5ireyChBOP3qt0QaxchYpyxCott5iwQAWdWc259HWv9JwYB5o2OlN95SbkTJPIS98KyR2goYq6T2ipOvhZVDLJ1c871k4WSBsP1yKTRTGdFGOeUwNjiegy5e1NVYZ8hHV8obs0WmylLM5TsqC7_7Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f9fc5142.mp4?token=gxmXZYCgDIH9aKbTzoNbZqH8rlV0cS3FipJyIJx4Ie_4MZNVmi02iV_VoL1BNOPe7e1msInVAu3lJxxXYZJqduArlu8Y_aL2x2j93Fn614spT6MKt9ypVp9bGLB6SZgwF1dLfXR-Mr7UEq0AHsvTz2rz7FlxA2B65K67uBsoZHy_4P5o4eTjKUpb1eCRTJkX5ireyChBOP3qt0QaxchYpyxCott5iwQAWdWc259HWv9JwYB5o2OlN95SbkTJPIS98KyR2goYq6T2ipOvhZVDLJ1c871k4WSBsP1yKTRTGdFGOeUwNjiegy5e1NVYZ8hHV8obs0WmylLM5TsqC7_7Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگزاری این کنسرت خیابونی مختلط توی کیش باعث شده صدای طرفداران حکومت در بیاد
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71619" target="_blank">📅 16:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71618">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9cbffc3d5.mp4?token=Pz-PoVq6bIzdlxqVaoZGIHmWkaEoN0ufQPQI0FGDyUPQ9f_f-jdH1BA-CvlbBPLt3SezGsIzVb3TydyKh-_92hT_w1ML2loEsKJQK5oZsT_ZeA9iEURcmnisnr4AryuMTOCC6TWfD02za3xt_x_-LT6lLgm66O_Ez_1-KeQiq16CjtqoorDa_frIi7noFPbtF18PD-dIu55gwnjjs0BUdqUj9J4MhiXx5TCzU3MQbYXGnlQJ6_fsW-QJgdCsQnSVJILLleRBaTAVpo1w2FcH9bLr4MYujaFeAwL1LK_fAvS7abkc8rq1bgoGYoYdS3NQgRU_b366DIZd6HlhJBOpww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9cbffc3d5.mp4?token=Pz-PoVq6bIzdlxqVaoZGIHmWkaEoN0ufQPQI0FGDyUPQ9f_f-jdH1BA-CvlbBPLt3SezGsIzVb3TydyKh-_92hT_w1ML2loEsKJQK5oZsT_ZeA9iEURcmnisnr4AryuMTOCC6TWfD02za3xt_x_-LT6lLgm66O_Ez_1-KeQiq16CjtqoorDa_frIi7noFPbtF18PD-dIu55gwnjjs0BUdqUj9J4MhiXx5TCzU3MQbYXGnlQJ6_fsW-QJgdCsQnSVJILLleRBaTAVpo1w2FcH9bLr4MYujaFeAwL1LK_fAvS7abkc8rq1bgoGYoYdS3NQgRU_b366DIZd6HlhJBOpww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ و بی‌بی ترسیدن نکنید اقا
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71618" target="_blank">📅 16:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71617">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eadd25c0f.mp4?token=F5U4pcVq7v1qJHZB3zSmx4UXCuMvqy1h5miwfMtYajsoUJa52aeU8q9p1QGCP341cQo1jUtlE4viqVGHeu7Nvj1_qcGAKLirBw8rirZzUp-cvDiPfFOepyANZnIKNp5j8RuYsh4dJtrroJXZSMlJITVS5HtilJ1nwmB75NhNNzHa4NDXkk7GKW2KfuTtbMks7dKQ3QWrdNim4V3SldMJwfI32NaPERrmO2dVI5kFyUZH4kj98F548jFIw8YFVrIdcAxLWZH-itPNZdfr6qixyIHOPBLofRCUlzSlrCi72opQ1sGi0KNSUklvC5AkV1EogYgelxTxmGL98vZcESunNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eadd25c0f.mp4?token=F5U4pcVq7v1qJHZB3zSmx4UXCuMvqy1h5miwfMtYajsoUJa52aeU8q9p1QGCP341cQo1jUtlE4viqVGHeu7Nvj1_qcGAKLirBw8rirZzUp-cvDiPfFOepyANZnIKNp5j8RuYsh4dJtrroJXZSMlJITVS5HtilJ1nwmB75NhNNzHa4NDXkk7GKW2KfuTtbMks7dKQ3QWrdNim4V3SldMJwfI32NaPERrmO2dVI5kFyUZH4kj98F548jFIw8YFVrIdcAxLWZH-itPNZdfr6qixyIHOPBLofRCUlzSlrCi72opQ1sGi0KNSUklvC5AkV1EogYgelxTxmGL98vZcESunNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سرقت آیفون ۱۷ پرو ، در کسری از ثانیه در کافه ای در اندرزگو تهران
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71617" target="_blank">📅 15:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71616">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4caee63fca.mp4?token=q-P8SrIvy9YZ79_jq9jk7AB-QORx6bdF3nmWmoId8e4-uQX4KO5Gn9jMkKZqTj1-X6mt9O2lUjNx181vYeyl2h57cD8_bIe92ShOZgg0VY8l-d33i-0sXTQUWY1g-XUrY7lcI0_UCHmKoN94UVY0SVOR9IauUERyj_AeHl-xPpUStZE5BGmh4osHBLkk37xQm0dnOwx9E3IRwzTDuKT5oBCirMJOP8ioyfXsLd18TqTkVxkxt5Z4T10E_UQooDaQe0A07k94JYUH3WqI4BFW6KRRwg_kKlO5y8Itl4Vuh3SBkG_N_PFBvuodrb824_fxGeF_zDKHmn-UfZ2lDH16Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4caee63fca.mp4?token=q-P8SrIvy9YZ79_jq9jk7AB-QORx6bdF3nmWmoId8e4-uQX4KO5Gn9jMkKZqTj1-X6mt9O2lUjNx181vYeyl2h57cD8_bIe92ShOZgg0VY8l-d33i-0sXTQUWY1g-XUrY7lcI0_UCHmKoN94UVY0SVOR9IauUERyj_AeHl-xPpUStZE5BGmh4osHBLkk37xQm0dnOwx9E3IRwzTDuKT5oBCirMJOP8ioyfXsLd18TqTkVxkxt5Z4T10E_UQooDaQe0A07k94JYUH3WqI4BFW6KRRwg_kKlO5y8Itl4Vuh3SBkG_N_PFBvuodrb824_fxGeF_zDKHmn-UfZ2lDH16Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
در ۴۵ روز گذشته، ۹ آتشفشان فوران کرده؛ انگار در جهان، یک تغییر بزرگ در جریانه
!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71616" target="_blank">📅 15:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71615">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c7aec3e1c.mp4?token=e2N2F7Fe5_loca-bJniPQE0R4w21nSwQ4Vqo8Xu1jk0NjFARR4-ULgFnINyDA7Pbrwv7rD-1F2CQFQmvB1ZC9kjslPPc2wIdoacv9ZM76-fZhQakkL_hvoVhQ5JYFuBwEr4i8K38OFrABQNrahgd_tkkvS4Ign135HxP57-b6h_GhZ1eLIGREkNyhtFsnxq_D6R75298H-Kzyt79PtcxvSVyqgQCZPxs4ZWcuOvPFcfDQkqwa9bOSGnD7FZFe1wi-Gh0VNP0hQeoDXI9Gymrn0XiEeu0vHwPirjpO19fIPHdd6gHKsVB6IEWA3ANaGS_NY1iJnUV9a6p42mdxTro3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c7aec3e1c.mp4?token=e2N2F7Fe5_loca-bJniPQE0R4w21nSwQ4Vqo8Xu1jk0NjFARR4-ULgFnINyDA7Pbrwv7rD-1F2CQFQmvB1ZC9kjslPPc2wIdoacv9ZM76-fZhQakkL_hvoVhQ5JYFuBwEr4i8K38OFrABQNrahgd_tkkvS4Ign135HxP57-b6h_GhZ1eLIGREkNyhtFsnxq_D6R75298H-Kzyt79PtcxvSVyqgQCZPxs4ZWcuOvPFcfDQkqwa9bOSGnD7FZFe1wi-Gh0VNP0hQeoDXI9Gymrn0XiEeu0vHwPirjpO19fIPHdd6gHKsVB6IEWA3ANaGS_NY1iJnUV9a6p42mdxTro3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رادان:
ما امروز از قبل از جنگ هم آماده‌تریم!
تو حوزه مرزبانی، انتظامی و خدماتی آماده‌تریم.
با امنیت مردم شوخی نداریم، ما شرایط‌مون جنگیه، اگه وطن‌فروشی به دعوت دشمن بخواد ناامنی ایجاد بکنه، ما اون رو مثل دشمن می‌بینیم و باهاشون برخوردی رو می‌کنیم که دارن با دشمن برخورد میکنن.
دشمن میخواست چهارشنبه آخر سال 1404، همون مدل دیِ 1404 رو راه بندازه ولی حضور مردم تو صحنه، متوقفش کرد.
مردم ما فریب دشمن رو نمیخورن، 30 میلیون جان‌فدا داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71615" target="_blank">📅 14:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71614">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYuyx5-WqRYiXw-0KhCEYDDTSLFhAMgPdrNGvajFzbRuwLixZEGT7uCE6k7wnpeO55KCOafwAOknP6F3qKjLh-fYh6760Pg4bXIfdAG7Scp1v8sLs7dznse6uT8T6lE9HygvtPP7xQWBm1K2_RZoXFVFHGIHeeU8NezYjfR0jdNaGb18hT3q1BB7W1erPXT38WiZivKuir2pc-zHZ6rMKBhVMfJ7AXTC-lKR4Z-3kg280pNHtb9Xmfeol9NdL1uU1uDUGMFi30Fc-2ONwtnr09lwQrlypqu-zOLXmuKjMXFQgBS5IyWFjkqBylWjSwJRQHsqq_kcA928StthhpdLKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🇮🇷
🇺🇸
بلومبرگ:
پس از آنکه اتریش تحت فشار دولت ترامپ از ورود محمد اسلامی، رئیس سازمان انرژی اتمی ایران، به این کشور جلوگیری کرد، حضور او در کنفرانس عمومی آژانس بین‌المللی انرژی اتمی در وین منتفی شد.
قرار بود اسلامی روز دوشنبه در این کنفرانس سخنرانی کند؛ اکنون احتمال دارد نماینده‌ای دیگر از ایران در اواخر هفته به جای او سخنرانی نماید.
انتظار می‌رود کریس رایت، وزیر انرژی آمریکا، در این کنفرانس ضمن تأکید بر اینکه «ایران هرگز نباید به سلاح هسته‌ای دست یابد یا آن را تولید کند»، خواستار همکاری کامل ایران با آژانس و دسترسی بازرسان آن شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71614" target="_blank">📅 13:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71613">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec91c05b9.mp4?token=EdcTrr-rUZBmM040ZXiigSwOjFCRAvWmgrbA7dKOsTVl9jTaOum8AT0acop9vxOSEeQDNsIZYVEpKljGgDTiGRzFyI9GtUVZp1s0xEWwPhxuVWyYidhNXKftRTmHe3dmuY-zYh2zMP8_XSa4MUmvhdc7iagQaWNYRk8nZ_NHn8BLHLGze6pH-IWSNXEQ6Ja_lFoGo2A49bQ3moZjWOa4K2oJJrjyKlFHiuaN3fBXWwPCC-GOQrReMjAZx74jtpBNEVMmMuNwWU8s7rWs-WV9lb-ji0IQBAWDBSNSXdhSMNRcvuL2m3N5ta8n-VHl-hp-tDJPGss_G6zy8DjP-P3l3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec91c05b9.mp4?token=EdcTrr-rUZBmM040ZXiigSwOjFCRAvWmgrbA7dKOsTVl9jTaOum8AT0acop9vxOSEeQDNsIZYVEpKljGgDTiGRzFyI9GtUVZp1s0xEWwPhxuVWyYidhNXKftRTmHe3dmuY-zYh2zMP8_XSa4MUmvhdc7iagQaWNYRk8nZ_NHn8BLHLGze6pH-IWSNXEQ6Ja_lFoGo2A49bQ3moZjWOa4K2oJJrjyKlFHiuaN3fBXWwPCC-GOQrReMjAZx74jtpBNEVMmMuNwWU8s7rWs-WV9lb-ji0IQBAWDBSNSXdhSMNRcvuL2m3N5ta8n-VHl-hp-tDJPGss_G6zy8DjP-P3l3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇳
سخنگوی وزارت امور خارجه هند در جریان سخنرانی مسعود پزشکیان در اجلاس بریکس در دهلی نو، با خوردن یک‌نفسِ یک ظرف آجیل — شامل خوردن، لیسیدن انگشتان و برداشتن دوباره از ظرف تا زمانی که کارکنان تشریفات آن را گرفتند خبرساز شد
😏
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71613" target="_blank">📅 13:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71612">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/567356c89d.mp4?token=UzbHL2qhDVr-yqisZwAEy4C9Hyt5OFDyRjX_bJj-xWLKZygNJcYF2yNfOWcItNULxiJMZuebuymaQjN4aEPotA-UNbxfhjD-soSY6aPvOCLzfX9Bnq0m4HcPmuTxz6RYwCxnCqAZMIBcUqWVHDnb2sihub-dniBTtnw5RjYKr5aoSkHVhjP-Ni-CS8QR1_I8k_RwMuM0seGfNkK2RNIt0aPRzfQ5zuYAB8vdSnvDbmpVYzT-kSwGg7nTkvMEOxbRIpP4ez5m4a7ctU7C3aMt33bYfz5Rq0790F1JAKp68UHYu63042Dgc2-7Bdv4VeFYw9dBQaqE1MDm7yamIEkrUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/567356c89d.mp4?token=UzbHL2qhDVr-yqisZwAEy4C9Hyt5OFDyRjX_bJj-xWLKZygNJcYF2yNfOWcItNULxiJMZuebuymaQjN4aEPotA-UNbxfhjD-soSY6aPvOCLzfX9Bnq0m4HcPmuTxz6RYwCxnCqAZMIBcUqWVHDnb2sihub-dniBTtnw5RjYKr5aoSkHVhjP-Ni-CS8QR1_I8k_RwMuM0seGfNkK2RNIt0aPRzfQ5zuYAB8vdSnvDbmpVYzT-kSwGg7nTkvMEOxbRIpP4ez5m4a7ctU7C3aMt33bYfz5Rq0790F1JAKp68UHYu63042Dgc2-7Bdv4VeFYw9dBQaqE1MDm7yamIEkrUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه جمهوری اسلامی:
توافق میان ایران و عمان حاصل هفته‌ها مذاکرات فشرده است و حقوق حاکمیتی هر دو کشور را به‌طور کامل محترم می‌شمارد.
از کشورهای همسایه انتظار می‌رود اختلافات گذشته را کنار بگذارند، برای تقویت امنیت منطقه‌ای گفتگو کنند و نفوذ بازیگران مخرب فرامنطقه‌ای را محدود سازند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71612" target="_blank">📅 12:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71611">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fkMTY44YpsAcu_Q9Oi4Ja6at7nbJZPMHm4Dd0Kn2o7DdTtMElKtnTTFeVWe55IC_nwCpn97NzaMWpe-cD81sp9hSRyaRCaqz65Rk-OUy1EHWNS75M66nI0_o_h5Wc799149AayVJ-DaNMgJvzlwqLoaCb86zw-GYD3ku0qXlXoKSI0IavS8CCUNf8ANY2CCNYjIgTxHeWqYedcduCnJ8dq3UYCW3VysecRHJdotuVZkXoc--mXPpDUPQ_XPmAFWeUZKHCffx0zWaiOS2_KASD356xdF7m__s3sCxllBfqIgyLYumoF95ySa7oVODLVV4V8qqHhvh9TN9kl3_NaY4jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه دختر شماره یه پسرو که روش کراش داشته داده رفیقش، و رفیقش تو نیم ساعت این اطلاعات رو از پسره درآورده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71611" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71610">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71610" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71610" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71609">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebcY0gR22x33el5AHcdfrWDTI1PuHLLwuoPwvbCPD-ezMXZLf48I-JilIAGMDXzkkIr5tcXAl62_hopG5gDQq5h5LIkaFm9g1NperjEa_k45X5RcQ1fTnkD_XQhQS4CTNMrmW3M4CtHdpAnFtL84kTJZABg-yR9ex7pfurrle_vmZa-DicSWc_SLsWY9ElA-P2AMRhFsSC4sD-P0zaK4vASLtnUkYATyv-CdFRY4c-XP6CL-kDEjrvp43B2y7IBH9bcXZYXVjjHU4J3eAp6BvlkWwnpPc5L560gSF7UDlJC5fxcGbJicefwvUgHoTJ3InNabhZMSgDFBdmfS-eFN8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
نیوکاسل
🆚
لیدز
رم
🆚
تورینو
اودینزه
🆚
اینتر
السد
🆚
استقلال
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71609" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71608">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001bfae793.mp4?token=M6PHKc3gZZboveSBaP3VF6AaSJ3JF9tdKE923m6LLatbjO7BibEdEaxe2XUWRkdDs__Ce76RbdbI_pdWy7H9LjQgOONxjAKsqjcmyuH4eIfA4NVb4rMi4zZz7CxeIrH1rHcLoPc09kZVTTEjUqNSnyZB3uctAnk1BAgD5PKanQ01oTUY2qvGOrz33zF6ZHil-f6iWX3CjdCmkn5pxi_wHpDv0QHJKY5DNohJsquNODnfFAOaaO5_CeGxab8Pm6fES_6PLL6qAcYnJVtSpXtdQugvY0f75_Va-E1LvCUF1tSIaJgvATlNPvZ_kuxd_SNRXOV2Qb5PvZsPnN2gENammA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001bfae793.mp4?token=M6PHKc3gZZboveSBaP3VF6AaSJ3JF9tdKE923m6LLatbjO7BibEdEaxe2XUWRkdDs__Ce76RbdbI_pdWy7H9LjQgOONxjAKsqjcmyuH4eIfA4NVb4rMi4zZz7CxeIrH1rHcLoPc09kZVTTEjUqNSnyZB3uctAnk1BAgD5PKanQ01oTUY2qvGOrz33zF6ZHil-f6iWX3CjdCmkn5pxi_wHpDv0QHJKY5DNohJsquNODnfFAOaaO5_CeGxab8Pm6fES_6PLL6qAcYnJVtSpXtdQugvY0f75_Va-E1LvCUF1tSIaJgvATlNPvZ_kuxd_SNRXOV2Qb5PvZsPnN2gENammA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤡
مجری صداوسیما:
اصلا نگران نباشید اوستاد خوش‌چشم مجدد توی برنامه ها شرکت خواهند کرد و انقد پیام ندید و مارو نوازش نکنید که چرا اوستاد چند وقته نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71608" target="_blank">📅 12:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71607">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19ca22a78.mp4?token=Ua1fGlAT32nE8EIShan965dPRE-zYfDwcx8su0ya73bBgdbV_gUoDpfhDFFV1Te53FYBoDAIlsx9fqwX9MDF3iJz2521wOkHR5qqe2gnSg8E-RXjnUKAXop8av34WGtnZxRtEDCZ1HIximRGqTBgIbE6ZiLOSQZmoHDWReOgOtan36ikm62lHXSXeE_HeHpX45T5uFZpJz7aqZkffU3bHBxGbL6ecJ01qqlu6qGnqiZptMcPLu4rx-7Xdjr7hNwBRXIQ6ew30_jcnzEmRgTL1Nv1zzoLg37x3mCmVQ-J8kOAYNOdU-gQzdhUAZAqz9UH2pB6et1E5fANDz17B4puiKe-LY4EOfM4Nzj23XOjz084hz9K_qF3xKpHPcOynMkFekWFyQPDQ20Y_sIlI_6OcfOvxjYjNXTfQ5auv3gSSXiO6TYUwpp06k51bTQWD0CKmQOj_LnvOOlFBzBn5sbwmEIJSYwnDmNe9uuZsoE4sinjiFg-FHCmAhVFNJZdvZY38c9hIDqn-xNSjJti1j-yt7AkFo9Bq6TItN63gLtuLsQTwGnbYV_e-5mdrvnstQYmMS6NswkFdfkMsVModw7QI23BzVM3wHVC4xW2PpxMi-imxichEHncZZgagSUoMGQTw_cepFRnNuNTs_zRtxJ5yEUeQL2OLBPNSZofe8IFyL4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19ca22a78.mp4?token=Ua1fGlAT32nE8EIShan965dPRE-zYfDwcx8su0ya73bBgdbV_gUoDpfhDFFV1Te53FYBoDAIlsx9fqwX9MDF3iJz2521wOkHR5qqe2gnSg8E-RXjnUKAXop8av34WGtnZxRtEDCZ1HIximRGqTBgIbE6ZiLOSQZmoHDWReOgOtan36ikm62lHXSXeE_HeHpX45T5uFZpJz7aqZkffU3bHBxGbL6ecJ01qqlu6qGnqiZptMcPLu4rx-7Xdjr7hNwBRXIQ6ew30_jcnzEmRgTL1Nv1zzoLg37x3mCmVQ-J8kOAYNOdU-gQzdhUAZAqz9UH2pB6et1E5fANDz17B4puiKe-LY4EOfM4Nzj23XOjz084hz9K_qF3xKpHPcOynMkFekWFyQPDQ20Y_sIlI_6OcfOvxjYjNXTfQ5auv3gSSXiO6TYUwpp06k51bTQWD0CKmQOj_LnvOOlFBzBn5sbwmEIJSYwnDmNe9uuZsoE4sinjiFg-FHCmAhVFNJZdvZY38c9hIDqn-xNSjJti1j-yt7AkFo9Bq6TItN63gLtuLsQTwGnbYV_e-5mdrvnstQYmMS6NswkFdfkMsVModw7QI23BzVM3wHVC4xW2PpxMi-imxichEHncZZgagSUoMGQTw_cepFRnNuNTs_zRtxJ5yEUeQL2OLBPNSZofe8IFyL4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ℹ️
باز و بسته کردن (مونتاژ و دمونتاژ) کلاشنیکف AK-74 توسط این بانوی روس
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71607" target="_blank">📅 11:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71606">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‼️
اگه نیسان کشنده ندیده بودی
این ویدیو رو ببین تا ببینی همچی توی ایران ممکنه
😟
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71606" target="_blank">📅 10:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71605">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ed023bda.mp4?token=kCnLR-I6WGlcbkrw7BZUujD0f_c3brGfj88VvIIrLKiTl2aZebDD7SyY18tF3guRlE8x-XRkMmaoOEwjBsh73vQ1kG5435rKFeme4BQ_BQ05-Q4YJoRWqVJr2h7FDhX4PD4Ltq6P6yc2Zdwf7Rvsme338JwAIZo-WLU9vP_pqdnWcM6qSldaEHyLavZlVByjkvvy2hCaDfFefbsQEaKhus6IsU02YP0pR4RzSIse6hNY0VmMPDgKb7d8ZobsX7ZPlqQQKHBKDHQelf28amUEq30b0Z5H6oXFLR96l-YSZ93tjf0CW9_8IW9J6TMKVA-yv34co1XMBjKizW4vWfIm8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ed023bda.mp4?token=kCnLR-I6WGlcbkrw7BZUujD0f_c3brGfj88VvIIrLKiTl2aZebDD7SyY18tF3guRlE8x-XRkMmaoOEwjBsh73vQ1kG5435rKFeme4BQ_BQ05-Q4YJoRWqVJr2h7FDhX4PD4Ltq6P6yc2Zdwf7Rvsme338JwAIZo-WLU9vP_pqdnWcM6qSldaEHyLavZlVByjkvvy2hCaDfFefbsQEaKhus6IsU02YP0pR4RzSIse6hNY0VmMPDgKb7d8ZobsX7ZPlqQQKHBKDHQelf28amUEq30b0Z5H6oXFLR96l-YSZ93tjf0CW9_8IW9J6TMKVA-yv34co1XMBjKizW4vWfIm8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تست سلاح جنگی بر روی شتر توسط یک عرب
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71605" target="_blank">📅 10:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71604">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e312dde1.mp4?token=XoAUgeAInDroAxIbDVx6euSRZztZS92PnsAEWvB9kBGb0Ou9IQnUudLXM95oLh4EjSwXBz1uT-QEyQ6oxJMa-iar1x__ORpdI7rmBLPYlZIXDHKAQsXmkhFgswrTEMRSuL7ReHdv_ZOsJdX2UKmEjoHtxNSzuBSVP2wPJ6wE-Z7R24BK6L9-GO_GRa8DNrxKcw_IfMI06MWRQKoGJ3USR9VKgV-gIuDnhHjyMYqw6PBXukgEz08jxKvY1ytVYZnGSGqtS98lGg1tbrx0XvYou4w0kBwI6BgpF3lhzDCgtwFiWy7th6oX1by-qrZOvKwl49-S7rafaiepZTEXVeK13Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e312dde1.mp4?token=XoAUgeAInDroAxIbDVx6euSRZztZS92PnsAEWvB9kBGb0Ou9IQnUudLXM95oLh4EjSwXBz1uT-QEyQ6oxJMa-iar1x__ORpdI7rmBLPYlZIXDHKAQsXmkhFgswrTEMRSuL7ReHdv_ZOsJdX2UKmEjoHtxNSzuBSVP2wPJ6wE-Z7R24BK6L9-GO_GRa8DNrxKcw_IfMI06MWRQKoGJ3USR9VKgV-gIuDnhHjyMYqw6PBXukgEz08jxKvY1ytVYZnGSGqtS98lGg1tbrx0XvYou4w0kBwI6BgpF3lhzDCgtwFiWy7th6oX1by-qrZOvKwl49-S7rafaiepZTEXVeK13Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
زنده یاد مانوک خدابخشیان:
تنها برگ برنده دونالد ترامپ این است که پرونده رژیم جمهوری اسلامی بسته شود. این بزرگترین پیروزی است، درست مثل فروپاشی شوروی؛ این را فراموش نکنید.
چرا او باید وارد جنگی شود که سال‌ها طول بکشد و دوباره در باتلاق خاورمیانه بماند؟
هدف این است که از خاورمیانه بیرون بیاید.
شما به اصطلاح آن دکه جمهوری اسلامی را ببندید، همان‌طوری که دکه کمونیسم بسته شد و همه فرو ریختند، تمام این‌ها هم فرو خواهند ریخت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71604" target="_blank">📅 10:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71603">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران:
لحظاتی قبل یک فروند پهپاد پیشرفته MQ۱ توسط سامانه نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور بر فراز آسمان تنگه هرمز رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71603" target="_blank">📅 09:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71602">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
یه ایرانی رفته توی تجمعات حامیان فلسطین توی خارج و بهشون میگه <<کص ننت فلسطین>> یعنی فلسطین رو دوس دارم
😂
اونا هم بدون اینکه معنیشو بدونن دارن تکرار میکنن
در ادامه میگه فلسطین رو از حماس آزاد کنید
در آخرم شعار جاویدشاه رو سر میده
👑
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71602" target="_blank">📅 09:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71601">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
مصاحبه کامل و ترجمه شده افسر تسلیحات نجات یافته ملقب به "براوو Bravo" با برنامه Minutes 60 پیرامون عملیات CSAR که در ماه آوریل در عمق خاک ایران انجام شد.
@News_Hut
|Cataphract1</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71601" target="_blank">📅 09:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71600">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
⭕️
تصاویر تازه‌منتشرشده‌ای که توسط برنامه «۶۰ دقیقه» (60 Minutes) پخش شد، عملیات نجات دو افسر نیروی هوایی ایالات متحده را نشان می‌دهد؛ افسرانی که با نام‌های عملیاتی «آلفا» و «براوو» شناخته می‌شوند و جت جنگنده F-15E آن‌ها در ماه آوریل بر فراز ایران سرنگون شده بود.
این دو نفر در حالی که نیروهای ایرانی در جستجوی آن‌ها بودند، در منطقه‌ای کوهستانی در جنوب اصفهان و با فاصله‌ای حدود پنج مایل از یکدیگر فرود آمدند. در این گزارش همچنین تصاویری از حمله به نیروهای ایرانی به نمایش درآمد.
آلفا» هشت ساعت پس از خروج اضطراری (اجکت) از هواپیما، طی یک عملیات پرخطر در روز که با مشارکت ۲۱ فروند هواپیمای آمریکایی انجام شد، نجات یافت.
«براوو» حدود دو روز در پشت خطوط دشمن باقی ماند. او با وجود شکستگی کمر و سایر جراحات ناشی از فرود سخت (به‌دلیل نقص در چتر نجات)، از یک خط‌الرأس کوهستانی به ارتفاع ۷۰۰۰ پا بالا رفت تا اینکه دو تن از نیروهای ویژه امداد و نجات نیروی هوایی به او رسیدند و وی را به بالگرد آمریکایی منتقل کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71600" target="_blank">📅 07:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71599">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71599" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71599" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71598">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTJLSVDDs8tZM8LbLN6AsXyMzQebvPxYG3iRBfq-45S1keOB7ZpAcrH76_1wjNbH1syBB2WKOksMgWmF0aFjQ5cJX4F3RcteJY-_S3sxrXorzyCSTNmN-PnTnqFbYkwHLYV5B8N_fOqe0TvC94tNDLDiN32qUb6UmB8hFLBq7zTzCy8VgTwt7_7BIghRgsaGqs59XcD18AWhLQ5igbrxcs5X_v5vdYhAxHqVx97oVa7nd8QfwQKAxFDiQxTQ7COxo4ReNILZzsAOR5lN5NWd4yh2tFJt1m_yw7AQcKNpRj6WegXzi8qbd2wImCpVWpzlTqdJV9P3nARdVTlKVXXQzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71598" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71597">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b94dc744f.mp4?token=B7m8h_SNcit5HguDOlG2Tj8GT7mnx81yS7enjJW-Br9O45FydCOp9Ce26yKdnPy35BS3DYOe_PyJWLPqUHe3fhyTW9EumVv5ZpRWYMYrTHD6gNYWmm9pKE83q6vDmaV_uEwpiPNPGdmVLFr_Ylx3n2Uxd9LR0RxlYxLPV6zs190oWIABM5u4gUCNUwBEZnQWUHozgeyQ2STNdsVTdY5Jp0nMANVzKH_nQWzzGZBv5lUwmKQipCZPUFU-OFRuTOaM7R86DvrmaQsw9QHbR6zFtTOT3Nlcx08QmFOo1fP9FLEclPijXIrWOl3NQads8nX1-xCTwC9LvpsoAtDHfa40sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b94dc744f.mp4?token=B7m8h_SNcit5HguDOlG2Tj8GT7mnx81yS7enjJW-Br9O45FydCOp9Ce26yKdnPy35BS3DYOe_PyJWLPqUHe3fhyTW9EumVv5ZpRWYMYrTHD6gNYWmm9pKE83q6vDmaV_uEwpiPNPGdmVLFr_Ylx3n2Uxd9LR0RxlYxLPV6zs190oWIABM5u4gUCNUwBEZnQWUHozgeyQ2STNdsVTdY5Jp0nMANVzKH_nQWzzGZBv5lUwmKQipCZPUFU-OFRuTOaM7R86DvrmaQsw9QHbR6zFtTOT3Nlcx08QmFOo1fP9FLEclPijXIrWOl3NQads8nX1-xCTwC9LvpsoAtDHfa40sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سپاه به طرف تنگه هرمز موشک شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71597" target="_blank">📅 01:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71596">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaZi5vtFYnlXVorT4t0kktyG38Ym6E2eqmtKKldGRDhb5tUq9QH-JtVNeAYzq4AVdq5pUfxXEtsaJIlzjan1L1SIS540fovI2_c9xZnvJd4GFdJoEwaOXvExtzCvqGmlmkqO0AuL7aV7PryvytOZfUc9VvFE1s_2zRE0dd0_2yBCjxGGLoFJZv_74qqOHV-fTz4p8zEOhTQVQSY9kl2ZRkRiW3GEDQFMr-qrsTZns6zfmgi8YOPlSVTMiePoEKx6CR0h8HAY3kZt97aJRu9wlEpgaDhGVe4v_0vNGF5B4zEGijR-11p287HIJIIRUCtacwI7rzRvkAbRd25AJ3ZHjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
❌
🇮🇷
🇴🇲
باراک راوید:
یک مقام حوزه خلیج فارس به من گفت که عربستان سعودی اصلاحاتی را در طرح پیشنهادی عمان و ایران در خصوص تنگه هرمز ارائه کرده است؛
زیرا نگران بود که عبارات پیشنهادی عملاً منجر به ایجاد وضعیت موجود جدیدی در این تنگه شود که برای این کشور یا سایر کشورهای عضو شورای همکاری خلیج فارس قابل قبول نباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71596" target="_blank">📅 01:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71595">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c7311729.mp4?token=quMjpwJJcTbYMziMbqitHzuHA_UN-OnC4eQOnY1sfPg6qXT_4mWbL7vhE9aGcTanxAu8MWKdOscOIAj4sJ97gXXFnujIR6vj6yzX8Ay-6_Swh0_0ffihCo7yMjvJQ5p2BQWXUhv7cj4icDXRBnPLI_-iCHPGE8s_XMYD0AbJ5C5-TXjgHIloS13lLZhbR1fChrccy3ImTLLmP1goUTJrm1zu6zwwu9RosxqwoT7DoodxtAItItJcupBdJBJQQ7E9FeJazIw1lNXjUGNiqoMRqzoIgZqGS7nHSEtTUEVYayjtuWaA7n6PfyTZKGKGToxcbHk4WYnbcNPE9YtDBpUDWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c7311729.mp4?token=quMjpwJJcTbYMziMbqitHzuHA_UN-OnC4eQOnY1sfPg6qXT_4mWbL7vhE9aGcTanxAu8MWKdOscOIAj4sJ97gXXFnujIR6vj6yzX8Ay-6_Swh0_0ffihCo7yMjvJQ5p2BQWXUhv7cj4icDXRBnPLI_-iCHPGE8s_XMYD0AbJ5C5-TXjgHIloS13lLZhbR1fChrccy3ImTLLmP1goUTJrm1zu6zwwu9RosxqwoT7DoodxtAItItJcupBdJBJQQ7E9FeJazIw1lNXjUGNiqoMRqzoIgZqGS7nHSEtTUEVYayjtuWaA7n6PfyTZKGKGToxcbHk4WYnbcNPE9YtDBpUDWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
ایران می‌گوید دیشب به یکی از شناورهایش حمله شده است. آیا کار آمریکا بود؟
🇺🇸
ترامپ:
نمی‌خواهم بگویم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71595" target="_blank">📅 00:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71594">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3oa96YKcXUHirpEYd7MUFe-5nuGzlntq0sZgNsI_kC2QW41Y3vHXthnEX0T9ZyQhn5u5d1mCVM2yhWu3Wi3VCTCtq2aW0vTUdxZMGU71UjUxY9NDp8BJeP0yZINeRtDdLahnIoTyP_vkYQ-_vsYTEdBCo4PKU_QmylsnyUr0Mr-VqEEMqAGYJ9DFBa3PuCElvlDX3jBjjFNpjRM1vqeY8qSJTNXNaMMGA6xTKJ5CReJuTVQK50al1AUYnPs45MGsTdbPONtr-QBMPBgcS-1D8nSVC_-IjFBIZN9JXREHZkZJ9XCMmDXNJmCE81mG2DHkdX8Ot8cXVI17slpuT7Kgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇴🇲
بدر‌البوسعیدی وزیر خارجه عمان:
در راستای دستیابی به اجماع، نشست منطقه‌ای که قرار بود فردا در صلاله برگزار شود، به تعویق افتاد.
ما همچنان به ترویج گفت‌وگویی که حامی ثبات و همکاری پایدار در منطقه ما باشد، متعهد هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71594" target="_blank">📅 00:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71593">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
⭕️
نشستی که قرار بود فردا در عمان میان ایران و کشورهای حوزه خلیج فارس درباره تنگه هرمز برگزار شود، به تعویق افتاده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71593" target="_blank">📅 00:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71592">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpskWlBOVeIDOjE72PqE1IR41iNGFCVzvIVRjogk95n6_9lmeZsuoQLVo2dZrktO2fpxH1udDNju69vUHc8uXo-DqY66C4xsEu4uT4LvbrZBm-q4ViDDHZlsgc4IL-drwdnD2aqVbACJXV_vFjSI3sfyTJ78vXFG12ZMhSoaSbDPtyer7Xyp2uNTuI-ZIy1bkJQ8o4fgql9tQ13gomHmdpWk_pnDu9QVXTpWdKLyc6DowmiagSvK5EWToYVbJ4nTZF5_j1PQ0BwaIoebY6rjmRkLL8qzYyBFkLsYqyc0znlBKxhw6siNqbrDSTVeSAcXwVmOrfgXyUfaAVCwP36MbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت های عجیب پوریا بختیاری کارشناس اقتصادی در مصاحبه با علی ضیا درباره ابراهیم رئیسی:</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71592" target="_blank">📅 00:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71591">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec76e7285d.mp4?token=iTVJOCEmV6skGdtZHdxHViOMu-rm2DBoBKYTVzX0AmIJiRAmMVSyYV0LJ7uaFp_7J6zrSplbj5qh_OJ4hTnNObAi3iEX8xuE76u-uGky7PtIj1IRUO23-8CEcZhDFCwFsxXec5P_1KF8fvc7PYGD1Ai68dDWAezXByix8BTVj-jr3vWZhCI5kzm8r-fhjdsgQIpmNrzGAT9sRzVaqwOJEIPYA-Thtk47CzEcIcRk5c4qxvBUFvK4KUsRSvAfkFEkUuZ4nJHCEG2jg2Cjlmf1WBJHCER2Q5g1p1Ox8swwLjgWX1oSvmQT9JHS4dzS8taEuDaHYJy2e2yuXJQSkX7xhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec76e7285d.mp4?token=iTVJOCEmV6skGdtZHdxHViOMu-rm2DBoBKYTVzX0AmIJiRAmMVSyYV0LJ7uaFp_7J6zrSplbj5qh_OJ4hTnNObAi3iEX8xuE76u-uGky7PtIj1IRUO23-8CEcZhDFCwFsxXec5P_1KF8fvc7PYGD1Ai68dDWAezXByix8BTVj-jr3vWZhCI5kzm8r-fhjdsgQIpmNrzGAT9sRzVaqwOJEIPYA-Thtk47CzEcIcRk5c4qxvBUFvK4KUsRSvAfkFEkUuZ4nJHCEG2jg2Cjlmf1WBJHCER2Q5g1p1Ox8swwLjgWX1oSvmQT9JHS4dzS8taEuDaHYJy2e2yuXJQSkX7xhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیو تبلیغاتی بانو سیدنی سویینی برای novig
😟
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71591" target="_blank">📅 23:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71590">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrY035yBDsTzBDsUfV_NBQPRcMLaVeF0fC0H-NYa28Dg3vtKe0QLT7_zywbk1RSP6bGEaf9t1yQp9EBGmrdqrGOadr6wmtHNK2AcmbDkplFZUQOWkBh2Klv20D8rK6iCfRSxDaj_trpL3I0PUWjXwkbIIyOuHby-bhohIEwWRBZ6qoxdX6KtVfuEVss_3NEvqPC6Wn3Mk7ZL8zuNbrhmHjHEup4tCkPkxW9vRQxmAjHRxyo1XlKvw8ZZNCCla-o2zOFk7MchuWgO9T8ZQKJwHqY_PdH_GBsasbZg-W-Ndj2pN_-VPfGA67eHjOHFw0JPmE2yCoJNh5zb3Zi5xOsOHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
🇺🇸
نیویورک‌تایمز:
مقامات ایرانی می‌گویند که رهبری این کشور طی هفته‌های اخیر بر سر دو راهبرد برای شکستن بن‌بست با ایالات متحده دچار اختلاف نظر بوده است: بازگشت به مذاکرات یا تشدید درگیری‌ها.
بر اساس طرح تشدید تنش، ایران حملات خود به اهداف آمریکایی - از جمله شناورهای نیروی دریایی و نیروهای نظامی ایالات متحده - را افزایش می‌دهد و هم‌زمان تلاش می‌کند با بالا بردن قیمت جهانی نفت، طرف مقابل را وادار به پایان دادن به محاصره دریایی کند؛ محاصره‌ای که تجارت ایران را فلج کرده و صادرات نفت این کشور را به صفر رسانده است.
ژنرال‌های تندرو، از جمله سرتیپ سید مجید موسوی (فرمانده نیروی هوافضای سپاه پاسداران)، طرح جنگی مفصلی را به شورای عالی امنیت ملی ارائه کردند. این طرح خواستار آن بود که ایران و گروه‌های هم‌پیمانش - به‌ویژه حوثی‌ها (انصارالله) در یمن و شبه‌نظامیان شیعه در عراق - دامنه حملات خود علیه نیروهای آمریکایی و زیرساخت‌های نفتی منطقه را گسترش دهند.
مسعود پزشکیان، رئیس‌جمهور، و محمدباقر قالیباف، رئیس مجلس، با این طرح مخالفت کردند و هشدار دادند که اجرای آن می‌تواند ایران را به جنگی بسیار گسترده‌تر بکشاند، موجب حملات هوایی سنگین‌تر آمریکا شود و بحران اقتصادی کشور را عمیق‌تر سازد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71590" target="_blank">📅 23:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71589">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02f69702f.mp4?token=BaZfWvNK8_NIV4ga0ht6Wi3GPQTxI6OKrtJYE_PvzrtFbNNENAVdW9vBfFDiQkPqLwC1kRqXNxhA8jpg4hQSf6CBOLsldPj142YHZ1tEyH_09KOJ8FPFzu7xzu7b-4ISoMUHXfwM9XJ4vH4Ggh2ovi8VR-3fHDEeLA0i6AsyKK-HYWi7nNhKtsYOPqXHJwzLkRVc8UHYlZEmD8gcZNdGaMxWd0NCYjWI6HADK3Jp5VXzIf-U3yi8q6sQTwit9vqNsSjS1Jgbr8rVQEDEoVpkPPbu4UufskirBWQKKcIMLpLCY80QHXP5DQdHPjYABULNwoA2lQf_om8pAH0dS-gF6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02f69702f.mp4?token=BaZfWvNK8_NIV4ga0ht6Wi3GPQTxI6OKrtJYE_PvzrtFbNNENAVdW9vBfFDiQkPqLwC1kRqXNxhA8jpg4hQSf6CBOLsldPj142YHZ1tEyH_09KOJ8FPFzu7xzu7b-4ISoMUHXfwM9XJ4vH4Ggh2ovi8VR-3fHDEeLA0i6AsyKK-HYWi7nNhKtsYOPqXHJwzLkRVc8UHYlZEmD8gcZNdGaMxWd0NCYjWI6HADK3Jp5VXzIf-U3yi8q6sQTwit9vqNsSjS1Jgbr8rVQEDEoVpkPPbu4UufskirBWQKKcIMLpLCY80QHXP5DQdHPjYABULNwoA2lQf_om8pAH0dS-gF6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کشتی که امروز صبح در نزدیکی جزیره قشم در جنوب ایران مورد حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71589" target="_blank">📅 22:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71588">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ae06116.mp4?token=cKjrl3z37DjlFZCWZi193oNw4JdKBoL4PxPj5uJK3NfXTLPT1qxjWu_noekFeB8rknDHisU_c71fwgSuMrF2uoD_2gRucO1R8eFZyTOZkLPnm6lu5YxIOUGEEDD6r9HGQeQHeRYGFMElpInd_JZSRQMQYVSyfPawA8QcEzP_dGYuVsqoHlSs5AGaxbIqFI85hNZAfDQ0EEWnBDX4pwwRlA1A7sxdYmOL3tyy-bW3iX6BD3ocaIW-M2HeG__WHh8f6PL1hYnl6beq6hUUfKyAD2fXeizf1CpKtRxYrguitAHwKmWsbFAAaM2fyzXHsi400Ch-vS4P_X74fiaY0tjlXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ae06116.mp4?token=cKjrl3z37DjlFZCWZi193oNw4JdKBoL4PxPj5uJK3NfXTLPT1qxjWu_noekFeB8rknDHisU_c71fwgSuMrF2uoD_2gRucO1R8eFZyTOZkLPnm6lu5YxIOUGEEDD6r9HGQeQHeRYGFMElpInd_JZSRQMQYVSyfPawA8QcEzP_dGYuVsqoHlSs5AGaxbIqFI85hNZAfDQ0EEWnBDX4pwwRlA1A7sxdYmOL3tyy-bW3iX6BD3ocaIW-M2HeG__WHh8f6PL1hYnl6beq6hUUfKyAD2fXeizf1CpKtRxYrguitAHwKmWsbFAAaM2fyzXHsi400Ch-vS4P_X74fiaY0tjlXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
زهران ممدانی شهردار نیویورک :
قربانی اصلی حمله ۱۱ سپتامبر عمه‌ی من بود که بعد از اون اتفاق نمی‌تونست با امنیت از مترو استفاده کنه چون حجاب داشت
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71588" target="_blank">📅 21:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71587">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0CaojFD0BbXzNT4-OrF5V4mNCJl4AYpeeCXJ6pROkiPZtVuqWkwC9g00haYARp88YMYsS7I24T_Srm_lcCNgfneQBlwG5roYGHJm0Rw9ymRc6typVCeRj-MnkSRF670RbihqOsB6DcXAj_DkStTdntiinef9-zLrSsKCnzG78Qri-joRt0_jsN1ardfnhddjKl9BGg0iJH0yK66KDkRdonQVbg0-B-qbg-DJRW5IHDvHzVI0uIfOvWruHQQ33O3dXRcWuZkJOPIvF-HK8keAX-JYb3Jp4jcT8GakxdxL1uC12Rp3kR262K7B1FVlSqCHmp-vLBfrwHBa7Z2hX60tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧩
🎮
کنسول بازی ps5 pro به قیمت تقریبا ۳۰۰ میلیون تومان رسیده!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71587" target="_blank">📅 21:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71586">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/643027f01a.mp4?token=ir9v4Ga0CSwHIjitQ2dK4h1BTepTKVkwC9WCG2rBcsyojTI3zWC0yiHXVqlpd-r1SU_HctDEmFFh8mij4CsiK5M6LJmdib5R1QSqV5Elb7BKHuMjDWpDMzWoh8EB7DO56bHcKUZhrk6i9kDCuB0oKj18SpyK4LitTGeDY5ZQY3qNG0v4nDJ28DcE1PEFZr9VOMeE0FttPYDfrFOBQnVeQQlO0npcT-OqxpTU8MaC8msMspoOxIGtS8mCHwwuv9DRh9zExqw_3uL-psaF5oIIGv1kX4dM37f1lVW0oYNh1gZ-y3boKimkuxdvgbY4CjZraRsEqTbaabi4npISGaaaag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/643027f01a.mp4?token=ir9v4Ga0CSwHIjitQ2dK4h1BTepTKVkwC9WCG2rBcsyojTI3zWC0yiHXVqlpd-r1SU_HctDEmFFh8mij4CsiK5M6LJmdib5R1QSqV5Elb7BKHuMjDWpDMzWoh8EB7DO56bHcKUZhrk6i9kDCuB0oKj18SpyK4LitTGeDY5ZQY3qNG0v4nDJ28DcE1PEFZr9VOMeE0FttPYDfrFOBQnVeQQlO0npcT-OqxpTU8MaC8msMspoOxIGtS8mCHwwuv9DRh9zExqw_3uL-psaF5oIIGv1kX4dM37f1lVW0oYNh1gZ-y3boKimkuxdvgbY4CjZraRsEqTbaabi4npISGaaaag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
مدیر سامانۀ هوشمند سوخت:
خودروهای نوشمارۀ بالای یک میلیارد تومان سهمیۀ ۱۵۰۰ و ۳۰۰۰ تومانی بنزین نمی‌گیرند!
این خودروها ماهانه ۱۱۰ لیتر بنزین ۱۰ هزار تومانی می‌گیرند
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71586" target="_blank">📅 20:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71585">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
اطلاعیه قرارگاه جانفدا:
از سه شنبه 24 شهریور ماه قراره هزار گردان مقاومت ملی تشکیل بدیم که شامل کسایی هست که جانفدا ثبت‌نام کردن.
قراره به این افراد آموزش نظامی و امدادی بدن تا اگه جنگ شد، فورا اعزام بشن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71585" target="_blank">📅 20:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71584">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c23e20e2.mp4?token=f29P6-EgLhVrBItgZSpE9ljxdU4NbifjUcxGAaepa1njjMZNZMLAF9mUdyXL9RMmUOi_yQgNB-l1nibfwQhWYgWpy62FS_ye2ksik0-R5B6cGGD108wYNU3V1lwZtJr2YadUhjQymRP88lyKa-ZJ--KzkuTaG3cxTMbrMsrVFijRCzEt8dKnEUJh0X5yI2pqxpmonbCZ9LZAn7v4VRflbvZ7gG5cFbjtoqS1XKWxxpWk38S8U56i2IgnVQqOCAB4b_88a_RDKHVCGKisqTnhk3T-w0I08gRrdmlTUwBNuJEM-qrFEyMoe1Wh99_rrR0y6jx4EINx4ObeqSVxtfYC2XdcIYhiXWZ4WsV3VluOgDmLI9fSSUfoiitPa9S-4NZgF8_CKJ5XNa_VZu5RaKxcvy0YBmUXc-mFCfhWleD27RHb8lNRpRXvaMAohW-haMDYj1MZCQPbQdOybhjOQ-d_ipTbiRzWO0AUUF1jQp3cINhZrBmM9_jSUQxgst91eNchtK1Eip2uWSsrPBYM4OObr8q6lyZVhyiTvqZE7Fax7X80hrER7OGyADlMYPiNGzxKLnUa8m6KzwANRMPyNmmnM8cxy_pMUhwQIDUKkU3uDdJvgVXFbbdm5ZfwSPtqSwBbObSL6di6wCmW61Kgi3UbkakxyNmhON_Hdk-G6ECZ7n8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c23e20e2.mp4?token=f29P6-EgLhVrBItgZSpE9ljxdU4NbifjUcxGAaepa1njjMZNZMLAF9mUdyXL9RMmUOi_yQgNB-l1nibfwQhWYgWpy62FS_ye2ksik0-R5B6cGGD108wYNU3V1lwZtJr2YadUhjQymRP88lyKa-ZJ--KzkuTaG3cxTMbrMsrVFijRCzEt8dKnEUJh0X5yI2pqxpmonbCZ9LZAn7v4VRflbvZ7gG5cFbjtoqS1XKWxxpWk38S8U56i2IgnVQqOCAB4b_88a_RDKHVCGKisqTnhk3T-w0I08gRrdmlTUwBNuJEM-qrFEyMoe1Wh99_rrR0y6jx4EINx4ObeqSVxtfYC2XdcIYhiXWZ4WsV3VluOgDmLI9fSSUfoiitPa9S-4NZgF8_CKJ5XNa_VZu5RaKxcvy0YBmUXc-mFCfhWleD27RHb8lNRpRXvaMAohW-haMDYj1MZCQPbQdOybhjOQ-d_ipTbiRzWO0AUUF1jQp3cINhZrBmM9_jSUQxgst91eNchtK1Eip2uWSsrPBYM4OObr8q6lyZVhyiTvqZE7Fax7X80hrER7OGyADlMYPiNGzxKLnUa8m6KzwANRMPyNmmnM8cxy_pMUhwQIDUKkU3uDdJvgVXFbbdm5ZfwSPtqSwBbObSL6di6wCmW61Kgi3UbkakxyNmhON_Hdk-G6ECZ7n8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی آموزشی برای دخترای موتور‌سوار چنل که قطعا بکارشون میاد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71584" target="_blank">📅 19:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71582">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/efbuEF3HDhGgjyvh_XX3WgAMTkJhYCtFcth81O6KmBY6hBpTnLpbDMgylNYS4ddscTnFRe9dmBsae4JAgn5QridZ63ZVmnIWlrq5TuweY_zxmMyCtOXymkI3eyh8lpXztSPpayT7cAOSp9mwCsw7me7pQvBd6dvGdhkWDxcGi73vAbxt-effgOeXNfmuA7FBMAebC-Rswc3xmccM2t5uINhi7BmWlSJmg-XI5l1MSthXf3-Fs1n0Bz1L9uEYeIfcP9MZFr10aZPtLpBw6eIcMK6HYSl7HPtboRIrlBAhmm3FLW4elAX7MEB31heDi3YwMgoZKaBV6OIitPVTGGgETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ekpgCwjqHPq12uSDHsJyxgdHN6GXxf7bheNo_3v5EYEjCAeEewCvtyWPOjjho4n4B8bgT6JiBR6RolnpdGecgvZPORhnIzL-C4WD8vh-yx9T7IzRdrnPWRwsUj1RisR8CQZnlCSohpHDZZhAZH2iBQqtg08Dj24JDof5z1SKJh7hMWEIYYRMGSDnwxwWV8IkjKAHjY5qUvFA9318iXN30BqlQSYw6cDt-YtDb1WzyNklgtgvxlW3GEuB6SSrw11G15zgSjZvVut-ZBVzL8TCGAeGSJovttaJVJZqcLcShCBvAx4f6Pg-Q0TDcpWnKpGe2xBxnpROdvOuPsYucYUvlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👑
دفتر شاهزاده رضا پهلوی:دستگاه کشتار و سرکوب جمهوری اسلامی بار دیگر قصد جان یک زن جوان را کرده است. سودا (مرضیه) ابراهیمی شمس‌آبادی، بلاگر ۳۳ ساله اهل بندرعباس، پس از ماه‌ها بازداشت و تحمل شکنجه، تنها به دلیل فعالیت رسانه‌ای، در بی‌دادگاه رژیم با مجازات اعدام روبه‌رو شده است.
صدای سودا باشیم و از همه ظرفیت‌ها برای فشار بین‌المللی جهت توقف ماشین کشتار رژیم استفاده کنیم.
سودا ۳۳سال دارد و ساکن بندرعباس است.
او در تاریخ ۹فروردین بازداشت و اکنون با اتهاماتی چون "عکسبرداری از فاصله دور محل اصابت یک موشک و ارسال این تصویر برای یک رسانه فارسی خارج از کشور" به اعدام محکوم شده است.
او حدود شش سال است که به بیماری ام‌اس مبتلاست و علاوه بر آن از بیماری‌های پسوریازیس، نارکولپسی و کولیک معده نیز رنج می‌برد و نمیتواند در زندان بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71582" target="_blank">📅 18:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71581">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eG9SsIz0Ehgdj_-KGXLcSj7SFeklguf1UHT95iYSsZCus4FKC6vBz9YEnHFrYBRZURRJKqTX5gvJ5wTs-_LM2nwKR-b80ybtyBpO7d9Uvr2Rvnl-UkOKXxJDE7TQhw2WzDCzoCWapI2oWWEf06k4GXsF9_9rMiTvc7KhF5Cwo6r5fA5iLZ4JxP1XkEWOR6xe-yk9ztMLIDWwP4jLjRfrqnbKfj1JJ166Fp0ejNYsptcXMUyF0R4x7Ax2fdNhBFzr__s2nCeYJmgtvNDMCft8wPIROVWjBIYmx-Dw21j-YdlA5TXbTA1Hr4pYcmnYv9WyikTjsRNHleCXM3wjL3aTbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇺🇸
نیویورک تایمز:به گفته مقامات ایرانی، تندروهای ایران با صدور دستور حمله به سه کشتی تجاری در تنگه هرمز در تاریخ ۷ ژوئیه، مخفیانه توافق صلح با ایالات متحده را که اوایل همان ماه حاصل شده بود، مختل کردند.
گزارش‌ها حاکی از آن است که مسعود پزشکیان، رئیس‌جمهور، احمد وحیدی و بخش عمده‌ای از رهبری ایران از این عملیات بی‌اطلاع بودند.
بازرسان رد این تصمیم را به جناحی مرتبط با حسین طائب — روحانی بانفوذ و رئیس پیشین اطلاعات سپاه که از همان ابتدا با این توافق مخالف بود — رساندند.
حملات ۷ ژوئیه منجر به حملات متقابل ایالات متحده در روز بعد و همچنین یک کشمکش قدرت بزرگ در داخل ایران شد.
تا ماه سپتامبر، ژنرال‌های تندرو دست بالا را پیدا کردند و به جای بازگشت به میز مذاکره، راهبرد تشدید حملات علیه نیروهای آمریکایی و زیرساخت‌های نفتی منطقه را پیش گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71581" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71580">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71580" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71580" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71579">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dh7MwpDJ923-2Q5YxODGWBLuISpQRg2X259_8tZDp46diEs631Nti-0NI4aKkssHOUpXgFu3kHvhfhMTMLhNhttdxD1pOSro5MfShVz-WbiGuT3G6Nl1JG8w3JZx_27A-pLdmXh3Tx5_NL2FQV-rm-1rn1CaA1aKYfeHmcDEzHH_mA-C0Wv9P4zLKYPEIQXWBZG2o7k4sxN3q9csw_EY6xCS2L3DcsxWyAZ1aYnfjsY_CRfRP2K8UwP0_ykYnUp1sn2IBVN2hFcvquxUg8llkIIBGC8ISXvOKYTC21kqEqs-ipr_OAAMN2-X8M2G1Vnxj8YTrogOSpPuVi5PjloEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71579" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71578">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc5dc935e.mp4?token=BUlTW41HOLrp6NYSkomdd_5BzsRt8CMcxZw2IuMt781LfCRVuRbfJGHjBITaY4CdpAawiKX1tHu30kJMhOcYsX0hYdan1ZbeUbzpP27zXeTyXMtDrgABuGepfuRQBn3Qk5enwjD3ho1a_n2jbDUc5tZpjJ70ELX5LuoH7A0LO0sfjiNAstD-p1XwSCd93r_CY_L8-kayA1Hssbuthuku-qNk32VEJ-i2nTp5_uIdYMHReb1N2aoY9-40Ijyay9B93eAJ7ZV9y1cnPC2NE_hFo3lcVppOWVdpV8Ll3c0DOO_0BOBstjmHkcvcsMNM8y2CSAn-bVzg7-WUcChc0vbyG1IrGMFWtpUcPYYlyVfzN_9FZELdw9PfhRL_nX73GVgNotlH_6OUhEjHxkVDV1iPxrnPtf_rGsrsge-5_vado3bYlkzJc2UZafNhUPav3Y_5iNT_zf1LgTbmVWSo93vovDlWUcF7ai875D5VDz15OfJXRPoYYfIhGvKrM2rjQD2MUBwKkOQJQM2nl_TzK_SRiai8yAjZ7DTigFbhVz45oU1LeVsvjrL5D9VXQvbEJ3MkBeuBQ-oXifGs2RZ4bh3fSlRYmGDfMqu1nkIydaegq5C_V1RgI8xx4yydt6ccSwV2xk1O-1Y8FpCmaq9gWned2_klKQDb0YVMDuiAK-uU8R4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc5dc935e.mp4?token=BUlTW41HOLrp6NYSkomdd_5BzsRt8CMcxZw2IuMt781LfCRVuRbfJGHjBITaY4CdpAawiKX1tHu30kJMhOcYsX0hYdan1ZbeUbzpP27zXeTyXMtDrgABuGepfuRQBn3Qk5enwjD3ho1a_n2jbDUc5tZpjJ70ELX5LuoH7A0LO0sfjiNAstD-p1XwSCd93r_CY_L8-kayA1Hssbuthuku-qNk32VEJ-i2nTp5_uIdYMHReb1N2aoY9-40Ijyay9B93eAJ7ZV9y1cnPC2NE_hFo3lcVppOWVdpV8Ll3c0DOO_0BOBstjmHkcvcsMNM8y2CSAn-bVzg7-WUcChc0vbyG1IrGMFWtpUcPYYlyVfzN_9FZELdw9PfhRL_nX73GVgNotlH_6OUhEjHxkVDV1iPxrnPtf_rGsrsge-5_vado3bYlkzJc2UZafNhUPav3Y_5iNT_zf1LgTbmVWSo93vovDlWUcF7ai875D5VDz15OfJXRPoYYfIhGvKrM2rjQD2MUBwKkOQJQM2nl_TzK_SRiai8yAjZ7DTigFbhVz45oU1LeVsvjrL5D9VXQvbEJ3MkBeuBQ-oXifGs2RZ4bh3fSlRYmGDfMqu1nkIydaegq5C_V1RgI8xx4yydt6ccSwV2xk1O-1Y8FpCmaq9gWned2_klKQDb0YVMDuiAK-uU8R4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ایران به‌شدت خواهان توافق است.
آن‌ها مدام تماس می‌گیرند. می‌خواهند توافق کنند. اما باید توافق درستی باشد؛
من تن به توافقی که خوب نباشد، نخواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71578" target="_blank">📅 17:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71577">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46b70464e.mp4?token=MrNEMGEOVPUOCPCTFJWauCks9MDKBYly5tima2Cn-6V13oVHaHrh5H2eY2lg6q2gt0O5ntCzwZVtmlBy5SKDV6hVSxD0Pa4boRvWaYHIG4cEZHzzCh71Z2x1UBCh4ZY6JY67dW2CqcHKLSEDS5ViWOZFOmfjqGlep_UY9SKNmkzGZDEpppWapfQq1QI_7_p6g66Ieq8hUW9tdr9YLLgA8D8oUg33Wh2Tgvf-dRKj8ds-LGdjur2OBD5huWXFC9lzyWVs8cFdjqxSUcc5ddAB2ienORrAcNX8Yl31868oOlEP1PzoesHHZ36TVXFp9klpzCiGLHg_eoHuHzXOuWPGw10iDXbUx8Xbe6angV5UayB9UTHtF7oMHBBFw-6hUOml4MbjhdZr0SIQBsMZ0oyGTJpDUELo6Lp5F1lhVkzEvz8CK93zytKzIvC1KUzKNadoJTnWuStwxZhE58g1nr3bdnGiRFLCUsd3cCvJrTKBkX6nqXvlFV2BbsPC8LcFyQyNt2HKL9NLN9I-Qtp_3fKTB62FzNYZYyJlIlPdceBBNs8AUPCyODXhl2gRfbRi8lRMw-b64EhBeaeAojUY34hMGBMqo8FodV0K0AvR-tYQGltXzCFMKNVmIZFOvoYuD0_h6D3FsrdDuBuY0id7FuCYfLq--uRh3sCIF5R-LHJOJwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46b70464e.mp4?token=MrNEMGEOVPUOCPCTFJWauCks9MDKBYly5tima2Cn-6V13oVHaHrh5H2eY2lg6q2gt0O5ntCzwZVtmlBy5SKDV6hVSxD0Pa4boRvWaYHIG4cEZHzzCh71Z2x1UBCh4ZY6JY67dW2CqcHKLSEDS5ViWOZFOmfjqGlep_UY9SKNmkzGZDEpppWapfQq1QI_7_p6g66Ieq8hUW9tdr9YLLgA8D8oUg33Wh2Tgvf-dRKj8ds-LGdjur2OBD5huWXFC9lzyWVs8cFdjqxSUcc5ddAB2ienORrAcNX8Yl31868oOlEP1PzoesHHZ36TVXFp9klpzCiGLHg_eoHuHzXOuWPGw10iDXbUx8Xbe6angV5UayB9UTHtF7oMHBBFw-6hUOml4MbjhdZr0SIQBsMZ0oyGTJpDUELo6Lp5F1lhVkzEvz8CK93zytKzIvC1KUzKNadoJTnWuStwxZhE58g1nr3bdnGiRFLCUsd3cCvJrTKBkX6nqXvlFV2BbsPC8LcFyQyNt2HKL9NLN9I-Qtp_3fKTB62FzNYZYyJlIlPdceBBNs8AUPCyODXhl2gRfbRi8lRMw-b64EhBeaeAojUY34hMGBMqo8FodV0K0AvR-tYQGltXzCFMKNVmIZFOvoYuD0_h6D3FsrdDuBuY0id7FuCYfLq--uRh3sCIF5R-LHJOJwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ماجرای ایران درست بعد از انتخابات میان‌دوره‌ای تمام می‌شود؛ شاید هم قبل از آن، اما قطعاً بلافاصله پس از انتخابات میان‌دوره‌ای پایان می‌یابد.
قیمت بنزین به‌شدت سقوط خواهد کرد،خب، من می‌دانستم چه کار می‌کنم و باید آن کار را انجام می‌دادم.
ایران نباید به سلاح هسته‌ای دست پیدا کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71577" target="_blank">📅 17:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71576">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a78bb4d113.mp4?token=N7QjeSHAxMFELrvF2s2t7YCXSQuA7iop_EgMfSCc9QpPCt7pyyRozscL-u46EfdpAPZzJ5OglgSkL0Nde2Qt9O7ujhA7ZZXWWxDw-FgM4RItGLugKWUE9ca7z82q4RcmBXBp5f4xowPoooXS6yoCYMyUf5rv05oM0zSx25xGx-xOTBVRt79RWHa1fgAIa73G6J4sswRWhFmxpyI7aRUFEYUkJOsBXI7EIC2iwlgPaONTuLMzwVQr9x16DtuveXVOeHqXEvqjbYr-RDDA0sk1VPffxAW0FbmYJvSjdtuDkIpjEuQCRRMrT3D9DbOn8RyOsvFCZbe3n00BjflpH89oDFzIfSJxZtaqk26Sga2C557j9exm2_PToeZswS2jLmqmEpwW3PLurAZ3ryx8G9LeePtNUmS8d9Nxj_YXnkid-_7PRNFBqlwo6M0R61atvJ43oHmGVCHdhf3-5bmrHTDyMBoasWi811qzvw548gj2z_Q4HtvaQTl0HxCmPnPy8_ezb4qdZHLdHrTo8yOUVs1jHgXuYD3noBCUmri25EXqTM6064LFKA4BhinTR55kP656qPz5tPrzA7NtTuTUxZLkKpJ6npLh2ClEGSuswhdlEFEIjlxH2vi0N-TKD3gBB1Qj4ycyeWEwFLOuV9JjaKi2K33zZNKeTUKXx_MSX3jsITc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a78bb4d113.mp4?token=N7QjeSHAxMFELrvF2s2t7YCXSQuA7iop_EgMfSCc9QpPCt7pyyRozscL-u46EfdpAPZzJ5OglgSkL0Nde2Qt9O7ujhA7ZZXWWxDw-FgM4RItGLugKWUE9ca7z82q4RcmBXBp5f4xowPoooXS6yoCYMyUf5rv05oM0zSx25xGx-xOTBVRt79RWHa1fgAIa73G6J4sswRWhFmxpyI7aRUFEYUkJOsBXI7EIC2iwlgPaONTuLMzwVQr9x16DtuveXVOeHqXEvqjbYr-RDDA0sk1VPffxAW0FbmYJvSjdtuDkIpjEuQCRRMrT3D9DbOn8RyOsvFCZbe3n00BjflpH89oDFzIfSJxZtaqk26Sga2C557j9exm2_PToeZswS2jLmqmEpwW3PLurAZ3ryx8G9LeePtNUmS8d9Nxj_YXnkid-_7PRNFBqlwo6M0R61atvJ43oHmGVCHdhf3-5bmrHTDyMBoasWi811qzvw548gj2z_Q4HtvaQTl0HxCmPnPy8_ezb4qdZHLdHrTo8yOUVs1jHgXuYD3noBCUmri25EXqTM6064LFKA4BhinTR55kP656qPz5tPrzA7NtTuTUxZLkKpJ6npLh2ClEGSuswhdlEFEIjlxH2vi0N-TKD3gBB1Qj4ycyeWEwFLOuV9JjaKi2K33zZNKeTUKXx_MSX3jsITc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آقای رئیس‌جمهور، آیا فکر می‌کنید کنگره باید آن ۵۰۰۰ دلار را تصویب کند؟
🇺🇸
ترامپ:
همان‌طور که گفتم، نمی‌دانم اگر جمهوری‌خواهان پیروز شوند، انجام این کار چقدر آسان خواهد بود.
صحبت از ۵۰۰۰ دلار برای تمام بزرگسالان کشور است و ما به‌راحتی از پسِ آن برمی‌آییم، چون درآمدهای کلانی داریم؛
وضعیت ما هرگز تا این حد عالی نبوده است. دموکرات‌ها نمی‌توانند چنین وعده‌ای بدهند، چون در آن صورت اوضاع بلافاصله به هم می‌ریزد و نابود می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71576" target="_blank">📅 17:32 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
