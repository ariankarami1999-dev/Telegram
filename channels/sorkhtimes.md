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
<img src="https://cdn4.telesco.pe/file/Z17RYuk81tmqgAh_WGWk64EVsk3jINzG7njZQdsKhucRoTdO_l8zOpUZ0CABknwXxWQzKwycZ2ZKFm_C0gTGVoDm7RWeJTj4WRHbWgFmPSKfp8eAGMB5ofmkmR5TgKb-lUnPgWZWuu7_mn1-2D1Frdj1Hc3qg2Q3QdRi5SluxacRummaZzdFDYogAeiC1uEDH2TIKQ3Zm5eF8DTmFOlwMNugIFMBfSLqNzXp3TRJxhF5RHMHND9cmwde9HL8Sf1F3qSNTBgXu4ukM7fBKQhkzbXMSrpAkV3p4QonsAnp6DrvqrmDwRyKzU0QQ-AqmbDRb4Jsf84u-gxCMr-sKO0Hjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 10:41:44</div>
<hr>

<div class="tg-post" id="msg-139391">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlfipSJo9aOKZwhRY7nRwiGdSpLUTYoN_Jz7StfR069IkbKQ8QPDMLUSqJ7zaApCzEBMMI4JntNox21GF4scJk2A2E-ZqpEzblZ8JFembMJTXhPVpPGd32ubJoVNItDfF-y4Dswy3wFQnyWPKuaCyAl0ORii3BKRiZ9WKA2ioQ1umH9hzGcSIB20G-GAvoGu_BpJhOmtEWdnp2CeV39SyR3xd5NLUpZuRKrnWazSkpyUPY53aqiUtxVGtSPPFjxuL-nMa3rMUTzk4rTK2h5VM9-EWp9I22pMsFG62lpme7e5a9Qu_gKLx6rUPHGuwLKeC0Z79BfBTHpyRrQAQJ89OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⚽️
تسنیم: شایعات الکی و بی مورد نسازید، دربی با حضور تماشاگران و بدون هیچ تغییری در استادیوم نقش‌جهان امروز برگزار خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/SorkhTimes/139391" target="_blank">📅 09:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139389">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkScJWT0xHJMH979ldV2mVCvIHISioHvirzW6nMWTVlR20bZXOA-oHJ-JethLGg_3pkcPoegcYph-Wx-FsboRqxx1OZo1SZbfCrLLNxh8oo8INJWQ14rROrmD0d9IitgOVw-MH6OUiJ8aZzF8F19QBeiLGgmP9NuLsFgNq2bIm5S_MaAmzDhsfYrAefq8Pjvd2J6-Rq1dCPyi9nY771kwksAZLLrNXDhdligjVKMZpvCPZsQ0jvzXd9pbeJVqOjyiGFNqxTuKkIkgCwN6amXNXqYCg1AvGasuoNf2I_8fPMa9NGLfcuG8TMrNOO7zt6v1hxOqa1CxOZ0edAdsCLA_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
با اعلام استاندار اصفهان دربی تهران در ساعت 19:30 در استادیوم نقش جهان اصفهان با حضور تماشاگران برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/SorkhTimes/139389" target="_blank">📅 09:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139388">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❤️
تکذیب شایعه برگزاری بدون تماشاگر دربی استقلال و پرسپولیس در نقش جهان
⚪️
⚪️
استاندار اصفهان شایعات مطرح‌ شده درباره برگزاری بدون تماشاگر این دیدار را تکذیب کرد و گفت: این مسابقه با حضور تماشاگران و طبق روال پیش‌بینی‌ شده برگزار می‌شود./ مهر
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SorkhTimes/139388" target="_blank">📅 09:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139387">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
خبرهای رسیده از فدراسیون فوتبال حاکی از اینه که احتمال لغو یا برگزاری بدون تماشاگر دیدارهای فردا لیگ برتر، از جمله دربی وجود دارد
❌
❌
تصمیم نهایی به‌زودی اعلام خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SorkhTimes/139387" target="_blank">📅 09:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139386">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇷
🇮🇷
صبح روز دربی و پر از استرس بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SorkhTimes/139386" target="_blank">📅 09:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139385">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIkPwiWhVSdK5EsziHsEd1kakYhMFyme0E92ARfo4z8crZCQwIzInwxlQIo8crVb77L3oEhHfcc-Ya2OqFFxBUykbhCBmrkwmxUjuHRNI88XP5SsnQuCb4sCG9qwmz8_h6rbmNWJ1T5duVkq8XAzEjV-gxLNAnAWHKnd_AYr5t4_XoWrcWrdKN27meFPDHYm_LY21_0CtQigzQzcv0AtIlp7j0F7h4g4MTA76op-tVO1gGXDmOK54UyPtU-klsRrMQms-hWzeuXttH9J5f9EN_k3B6ttU7Oya20xXj3hAQ8c1NQkyHqR9dLSZ18n2rVf5Ude-bJdIQY8GgInntEMAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
دوئل‌های جذاب در یو‌اس اوپن!
🎾
الکساندر زورف
🆚
لورنزو سونگو
🎾
آندره‌آ گِریِری
🆚
الکس د مینور
🟡
کدوم ستاره‌ها از این نبردهای حساس سربلند بیرون میان؟
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی دیدارهای یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/139385" target="_blank">📅 01:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139384">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
فووووووووووووری
🚨
شورای تامین استان اصفهان فردا 8 صبح جلسه اضطراری داره
🗣
سه سناریو پیش رو دربی پایتخت قرار داره
⏺
1_ برگزاری دربی پایتخت بدون مشکل
⏺
2_ برگزاری دربی بدون حضور تماشاگران و عودت پول بلیط به هواداران
⏺
3_ لغو دربی پایتخت و برگزاری آن…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/139384" target="_blank">📅 00:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139383">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
✔️
#مهم
❌
❌
دربی لغو نمیشه و اینکه یکم دیگه هم ایران هم آمریکا حملاتشون رو تموم میکنن و دوباره جو اروم میشه !
🔄
🔄
البته درسته خیلیا اینترنت شون اختلال خورده ولی تا فردا صبح درست میشه
✔️
به امید برد پرسپولیس
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139383" target="_blank">📅 00:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139382">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❤️
ترکیب احتمالی پرسپولیس:           ‌‌‌‌‌   نیازمند تیکدری زارع کنعانی عیدی  ‌‌‌    پورعلی خدابنده‌لو ‌‌‌    عمری بیفوما محبی      ‌‌‌‌‌‌‌‌       علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/139382" target="_blank">📅 00:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139381">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
✔️
#مهم
❌
❌
دربی لغو نمیشه و اینکه یکم دیگه هم ایران هم آمریکا حملاتشون رو تموم میکنن و دوباره جو اروم میشه !
🔄
🔄
البته درسته خیلیا اینترنت شون اختلال خورده ولی تا فردا صبح درست میشه
✔️
به امید برد پرسپولیس
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139381" target="_blank">📅 00:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139380">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
در صورت بالا رفتن درگیری ها، احتمال لغو پروازهای داخلی وجود دارد و از این رو تیم ها برای سفر به اصفهان باید برنامه خود را تغیبر داده و با اتوبوس راهی این شهر برای انجام دربی شوند
✔️
✔️
البته تا این لحظه خبری مبنی بر لغو پروازها مخابره نشده است///طاهرخانی…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139380" target="_blank">📅 00:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139379">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
❌
تموم شد
✔️
اولین توقف تراکتور تو قزوین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139379" target="_blank">📅 23:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139378">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=hWYQFxBov_lRn5OoPtGetnk25nxSfIv9kvu67wjc-S9TAAvqU592w3Ubi9-SX7fhQeKVP_WZcoOec3tiBKfvAcEoxcM1CZyDyF_b2xWJfdpvwymnl_qArJThCQKOy3VeoUHGAv7MDhxeosOWH8hSleLLG0H8j9Up04J79suPYHYFyhyKCYqVdfPHtOgAeLnlIHnaXmTmFYAEGOBn2g6DXcjTN1MfMBSkjVul8ils_znAwtvDCiNeMRQdc-dvokN1C94Kck333zRBv0u3fpwn_weR5KVWbxhTq5QSIvGCtybFI-NSZtaFfAgg3ZWf8UbRqMSc389w86rURgk-ONU2-xRPjV3g0viGyD9LIwB5ms46owHPjvmCe7mM7BGlBPn_9MqUw6zx7pHkqPBUHpVs8CqplOrpnah_gNt3otg9_1hA1fyA0y4SN-0Sqii3216kaaENmCBTbzcA34cfK-AfboTu9MIvObrjj7imUFScxRcUolwwOSrweNhFJF5PH8tHzSXterc-0fzJ9UuvZJ6Qth15aRbCqgQXKLTva1Z5V0RXVfIiVZPCg3lC7hRCsnO4IQ5NNci4Dg2KpXAGnF058tuodA5sS_5qmJdqqPMRMlXKFO1rmNtRsfbVjBA38bRaDKKcrRFNLikNb94GI1Oz5tWcCGpcC24ljJSbpGdR18U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344f252bb4.mp4?token=hWYQFxBov_lRn5OoPtGetnk25nxSfIv9kvu67wjc-S9TAAvqU592w3Ubi9-SX7fhQeKVP_WZcoOec3tiBKfvAcEoxcM1CZyDyF_b2xWJfdpvwymnl_qArJThCQKOy3VeoUHGAv7MDhxeosOWH8hSleLLG0H8j9Up04J79suPYHYFyhyKCYqVdfPHtOgAeLnlIHnaXmTmFYAEGOBn2g6DXcjTN1MfMBSkjVul8ils_znAwtvDCiNeMRQdc-dvokN1C94Kck333zRBv0u3fpwn_weR5KVWbxhTq5QSIvGCtybFI-NSZtaFfAgg3ZWf8UbRqMSc389w86rURgk-ONU2-xRPjV3g0viGyD9LIwB5ms46owHPjvmCe7mM7BGlBPn_9MqUw6zx7pHkqPBUHpVs8CqplOrpnah_gNt3otg9_1hA1fyA0y4SN-0Sqii3216kaaENmCBTbzcA34cfK-AfboTu9MIvObrjj7imUFScxRcUolwwOSrweNhFJF5PH8tHzSXterc-0fzJ9UuvZJ6Qth15aRbCqgQXKLTva1Z5V0RXVfIiVZPCg3lC7hRCsnO4IQ5NNci4Dg2KpXAGnF058tuodA5sS_5qmJdqqPMRMlXKFO1rmNtRsfbVjBA38bRaDKKcrRFNLikNb94GI1Oz5tWcCGpcC24ljJSbpGdR18U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💣
⚽️
❤️
حمله شجاع خلیل زاده به عادل فردوسی پور: من دو سال است که فحش می‌خورم اما خم به ابرو نیوردم، فشارهای زیادی روی منه و خدا رو شاهد میگیرم که یزمانی می‌خواستم از فوتبال خداحافظی کنم اما این کار رو نجام ندادم، دو سال فحاشی به من شد و تمامی این فحش‌ها تقدیم به عادل فردوسی‌پور
🔻
همه مردم تبریز می‌دونن عادل فردوسی‌پور با تراکتور مشکل داره از زمان برنامه 90 همین بود، الان هم همین است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139378" target="_blank">📅 22:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139377">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
شنیده میشود که چندین بازیکن تراکتور به دلیل بدنسازی بد مصدوم شده اند و باشگاه تراکتور با تعطیلی لیگ به دلیل اردوی تیم ملی امید موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139377" target="_blank">📅 22:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139376">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
✔️
شایعه شده که تارتار دوباره میخواد همون قمار از پیش باخته بازی تراکتور رو تکرار کنه و با یه مهاجم وارد بازی شه و عمری رو به جای سرگیف بازی بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139376" target="_blank">📅 22:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139375">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✔️
✔️
سهراب بختیاری‌زاده: می‌خواهیم ریتم خوب شروع لیگ را ادامه دهیم و پرسپولیس حریف خوبی است که به امید خدا بتوانیم آن‌ها را شکست دهیم و با روحیه بالاتر راهی لیگ نخبگان شویم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139375" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139374">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
✔️
✔️
تراکتورسازی تا دقیقه ۷۷ نتونسته به شمس آذر گلی بزنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139374" target="_blank">📅 21:11 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139373">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
شنیده میشود که چندین بازیکن تراکتور به دلیل بدنسازی بد مصدوم شده اند و باشگاه تراکتور با تعطیلی لیگ به دلیل اردوی تیم ملی امید موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139373" target="_blank">📅 20:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139372">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
#فوری | شنیده شدن صدای چندین انفجار در شرق بندرعباس و اطراف قشم منشا صدا مشخص نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139372" target="_blank">📅 20:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139371">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
صحبت‌های سهراب بختیاری‌زاده سرمربی استقلال در نشست خبری پیش از دربی:
🔻
دربی همیشه خاطره‌انگیز است و بازی‌ای است که در تاریخ برای بازیکنان ثبت می‌شود.
🔻
ما شاید موقعیت‌های بیشتر و بهتری نسبت به فولاد داشتیم ولی استفاده نکردیم ولی از بازیکنانم با توجه به شرایط…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139371" target="_blank">📅 20:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139370">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
مهدی تارتار به کنفرانس مطبوعاتی نرسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139370" target="_blank">📅 20:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139369">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
✔️
شایعه شده که تارتار دوباره میخواد همون قمار از پیش باخته بازی تراکتور رو تکرار کنه و با یه مهاجم وارد بازی شه و عمری رو به جای سرگیف بازی بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139369" target="_blank">📅 20:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139368">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
✔️
فوری/حملات آمریکا شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139368" target="_blank">📅 20:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139367">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔽
🔽
کانال ۱۲ اسرائیل: شماره معکوس حملات به ایران آغاز شده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139367" target="_blank">📅 20:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139366">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gP8IxzBeeJR81XByPlj-u82S06QblmV1oisvkNmpAHZ_S3XkQ8dx2VkLsPdUOI-vDbEF6FsqojfCtbyaE-Lk_oGsU491KmbsRAVekSENbmPt1v9SMIsM_fxXwGkIDuyn7QlO_CPJ21pknej56OtIWXfTisNJgmckRI9w9dPU_eCROTbreqn__-wtspRqcqqwIwtgnBP7m2N0neM1ts9kttKmgfnAAT2009wiwaSf5h1HdPyL9Rr7XMysnYccP1twPzuv8sSE7N0MySkFIdyq-2mttito6EVCjz0omqAqA_-ZEGQ9oIdbxbAa5jDHh2acREFl-njAm0ndxseCU5o-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
نبردی برای صدرنشینی!
⚽️
الهلال و الاهلی؛ جدال غول‌های عربستان
سه امتیاز، هدف مشترک دو مدعی.
[
الهلال
⚽️
🆚
⚽️
الاهلی
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139366" target="_blank">📅 19:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139365">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
تصاویری از آخرین تمرین پرسپولیس پیش از دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes   ﻿</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/139365" target="_blank">📅 18:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139364">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
با اعلام کمیته انضباطی قرارداد یاسر آسانی با استقلال قانونی است و مشکلی برای همراهی این تیم ندارد
✔️
البته خب انتظار دیگه ای هم نداشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/139364" target="_blank">📅 18:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139363">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HP7HJHQ0DHDkqBqZj9txXs-ppNpC46sQF92oxHZH5CYsJIyFb8C9x6E69ZAaGkETktTwURmj95MBrJ2_jJ200BeQD0VPvtL_zhIqnXfbvHCZ1RqjzfpKUiokzscNo1y3CSLfyi6D-aIaoTaIEdkFR3b_vbLtgklZTxn9B6dhGpltHYxC9cDWwuKZaDsAjcEpteN1B3od7zkLfXa7ABuKYRBPik-fjr1iO5iw502Rt1gP_zCXuz_F-njtCUigvs4eyZ67aagJO_cdlCDM0mRm_BvSd1MPanXwcvtmogREgXmswpGqatzfmbyKfy9-zl4a-jKxuIt98LcJv43LGfCBCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از آخرین تمرین پرسپولیس پیش از دربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139363" target="_blank">📅 17:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139362">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0MwBvdJnXPIcP6m8o707MtdxCXlk1Mm29cbsQODbuSZ8m74z7Ct0OXntM9tVtwCMxntpWxvZoAb2DSAk3EAC_uLe7ditY_Q8JIQwxUYD4SmLBG-CeOMfsmbcqTqKm85kqoec6EoRylLq0aV3N-G8skn8itDzNWj1LjFBSF877Ey6M4r7aT2DJi-3nGsMkSI5sCYKCB4ZPcPcTYrO4lIbFRHQ3gG18xD7KmafYHPa5G-K5KRDoDsLDIsmc9X7HXCwOugC7dzFu3XNd0ESy_YOWLVOcfAka7MiUvrfukX831XOIRiHzXnkLtbPG9q2XvB7fp68elxPXdOBInB-_fsHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
کاروان پرسپولیس راهی اصفهان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139362" target="_blank">📅 17:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139361">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
کاروان استقلال با تاخیر به اصفهان می‌رود
⏺
پیش‌تر قرار بود کاروان استقلال همزمان با پرسپولیس و ساعت ۱۶ با پروازی اختصاصی پایتخت را به مقصد اصفهان برای برگزاری دربی صد و هفتم تهران ترک کند.
⏺
با این وجود به دلیل همزمانی حضور تیم‌ها در فرودگاه و رو‌به‌رو…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139361" target="_blank">📅 17:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139360">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
تیم داوری دربی ۱۰۷:
⚪️
داور: موعود بنیادی‌فرد
⚪️
کمک‌داوران: علیرضا ایلدروم، بهمن عبداللهی
⚪️
داور چهارم: سیدرضا مهدوی
⚪️
ناظر: اسماعیل صفیری
⚪️
داور VAR: میثم حیدری
⚪️
کمک VAR: علی احمدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139360" target="_blank">📅 16:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139359">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139359" target="_blank">📅 16:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139358">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
❌
💢
💢
💢
گفته میشه تارتار قصد داره ترکیب پرسپولیس مقابل استقلال رو بازهم تغییر بده و عمری برای مهار آسانی بجای سرگیف وارد ترکیب بشه!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139358" target="_blank">📅 14:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139357">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
رئیس مرکز روابط عمومی وزارت بهداشت: تا ساعت ۶:۳۰صبح ۲۶ تیر، شمار مصدومین حملات آمریکا از ۴۰۰ نفر عبور و ۳۸ نفر هموطن جانشان را از دست دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139357" target="_blank">📅 14:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139356">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
هفته هفتم لیگ برتر فوتبال ایران به دلیل اصرار بر اعزام تیم ملی امید به بازی‌های آسیایی ناگویا و تداخل برنامه‌های اردویی این تیم با مسابقات باشگاهی، در آستانه لغو قرار گرفته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139356" target="_blank">📅 14:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139355">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ftt-5jM2oWs04ott3uwxPqztHv1DLqAckcVzYPqjBUYaiE1uUltHpeqXD22sBPK_Nu6hMlbn71LVlxUYe62FyP0Mp4V3U8n5aTDogLRw8n4_3gXRzsKT8xNJtP4VBItQYbgDVFlYtkH8egAFKOa4KcMazXKIamUf8gfJkfZgVWY8jMBz3Hm88ugiOK6hW834gnBXCnuc_2VTdlu765BUn-kJ9DpVZ5osuJHh0gzM1xHVYG2UnNuZnCTX5K-0Q2Cbj0kiL-1IT-mRWRu3OGLvjnVqleyWhx5-J3HaGucY1K0ydM5nzX14JIXJqImSJxCNeFHifpJBzr0QyL13SCA-NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبردی برای سه امتیاز در قزوین!
⚽️
تراکتور با انگیزه‌ی برد به مصاف شمس‌آذر می‌رود؛
یک بازی سخت، حساس و تماشایی در انتظار دو تیم!
[
شمس‌آذر
🟢
🆚
🔴
تراکتور
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139355" target="_blank">📅 14:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139354">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
✔️
گویا هفته هفتم لیگ برتر بخاطر مسابقات تیم ملی امید لغو شد
❌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139354" target="_blank">📅 12:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139353">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
✔️
فووووووووری
❌
احتمال تعطیلی لیگ ایران بعد از بازی دربی وجود داره. علتش هم برگزاری اردوی تیم ملی فوتبال امید هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139353" target="_blank">📅 12:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139352">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
تا کنون حدود 40 هزار بلیط برای بازی دربی فروخته شده و ظرفیت فروش پر شده اما احتمالش وجود داره‌ بازهم چند هزار بلیط دیگه شارژ بشه؛ ظرفیت کلی ورزشگاه نقش‌جهان 75 هزار نفر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139352" target="_blank">📅 12:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139351">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🚨
رسول باختر کارشناس حقوقی: یاسر آسانی بازیکن غیر مجاز است و دیدار استقلال و مس شهر بابک سه بر صفر خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139351" target="_blank">📅 12:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139350">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇷
🇮🇷
عکس یادگاری یحیی گل‌محمدی و علیرضا منصوریان در حاشیه دیدار دوستانه دهوک و الطلبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139350" target="_blank">📅 12:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139349">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
✔️
✔️
فووووووووری
❌
احتمال تعطیلی لیگ ایران بعد از بازی دربی وجود داره. علتش هم برگزاری اردوی تیم ملی فوتبال امید هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139349" target="_blank">📅 11:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139348">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
☄️
تماس تلفنی پیام صادقیان با پدیده ۲۰ ساله پرسپولیس
✔️
✔️
ستاره تکنیکی و سابق پرسپولیس قبل و بعد از پیروزی شاگردان مهدی تارتار با امیرحسین محمودی جوان گفت و گو کرد.
✔️
✔️
گویا پیام صادقیان، پدیده 20 ساله پرسپولیس را دعوت به آرامش کرده و از او خواسته است…</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139348" target="_blank">📅 11:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139347">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی: ابوالفضل جلالی به دربی رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/139347" target="_blank">📅 09:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139346">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
🎙
سامان آقازمانی، بازیکن پیشین پرسپولیس:
‼️
اصلا دوست نداشتم جای بازیکنان تیم ملی باشم. راست بری، با دولت درگیری. چپ بری با مردم درگیری. بی‌طرف هم بخوای باشی بهت تخم‌مرغ میزنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139346" target="_blank">📅 09:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139345">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
فووووووووووووری
✅
شنیده می‌شود سازمان لیگ تنها مجوز فروش 70 هزار بلیط برای دربی داده است! ظرفیت ورزشگاه نقش جهان اصفهان 75 هزار نفری است...!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139345" target="_blank">📅 08:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139344">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139344" target="_blank">📅 08:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139343">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAbMAncqze3bZKj_1G5NkTamsATy6WjftF2vMYXGd2bntFsFuCUb6bwrASkEvqnf9Rxuz95RGI1_4VDjM6RkLPSY5GBUvV-Ue7fMB_DPnR9ZwcZdeYCc_ZKCHp-JuqdykbqdyjpCQ0Hqb9hwvzyXQ7b1-aVZ3npZ9wPmzIMssAd6RHF-XZH-upWrpX-NeXrEKI-N2UcM8CtrGSxjdHPqhFd2xsAS0hrWXI576LEBS5I_bEi8ppfKAw4Oxpqp4avrZTcQ_fNjV5ixQtYzF9Mo9FioalrZflowhIKkTxlvNTT23YFAg_pa4HmdnrhR6fOqmIfpqLsyihubya6zkO-Z9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139343" target="_blank">📅 08:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139342">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkrzV6W8NT8LE3jOimHPpV3lg3a8Z-vP1Hq31qxTcIoUclL4nJ1uL7wPi2T7-LRG80fxG4p2igd05blulk5TTcyyuMGdcWjTgAG00bETj5zeCUACgZp98B6-6oUvoB6EohLMZGj1-XUsRvT7BUdDamSXRcECqIGgTe5WDxejUqfuskZO61gXcENvyF4e0tXK3yDCDRujCebKzPbyU_1xJzVbEcsLL0-XGHdo1sPnvHDwBQscn5SLC7aIsZi5C1LPcoD5v_v6--Z8LdVfbXPW00kWNFFWK3VQp2u_JkSYumnnqIacC2BpvacNM5OzR08k6U9i3c154To7w0-_JGcnZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
دوئل‌های جذاب در یو‌اس اوپن!
🎾
بن شلتون
🆚
خریکسپور
🎾
تیافو
🆚
مارتین دام
🟡
کدوم ستاره‌ها از این نبردهای حساس سربلند بیرون میان؟
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی دیدارهای یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/139342" target="_blank">📅 02:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139341">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✔️
✔️
پیام صادقیان: فوتبالیست‌های ایرانی قلیان می‌کشند
✔️
✔️
چرا باید دروغ بگویم؟ بازیکنان ایرانی قلیان می‌کشند. قطعا فوتبالیست حرفه‌ای نباید این کار را انجام بدهد اما متاسفانه این موضوعات وجود دارد. در ترکیه چیزهای بدتر از قلیان می‌کشیدند
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139341" target="_blank">📅 01:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139340">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
پیام صادقیان: حضور من در ورزشگاه شهر قدس خیلی حس خوبی بود/ دوست داشتم لباس عوض کنم و به زمین بروم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139340" target="_blank">📅 01:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139339">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
پیام صادقیان: حرفه‌ای ترین دوران فوتبالم ترکیه بود اما زیر تمرینات پرفشار آنها بدنم دیگر جواب نداد و فوتبال را در ۲۷ سالگی کنار گذاشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139339" target="_blank">📅 00:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139338">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
✔️
پیام صادقیان: بهم گفتن سایت شرطبندی که میزنی قانونیه مثل نیمار و فوتبالیست های بزرگ و اسپانسرش هستند و نمیدونستم قانونی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/139338" target="_blank">📅 00:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139337">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
✔️
پیام صادقیان:
❌
شرط‌بندی هر نوعش تهش باخته و فقط شما می‌بازید؛ من اشتباه کردم و همینجا میگم پشیمونم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139337" target="_blank">📅 00:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139336">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
✔️
صادقیان : شرط بندی تهش باخته و سرابه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139336" target="_blank">📅 00:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139335">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
پیام صادقیان: با محسن مسلمان تو تیم ملی زیر 10 سال با هم بودیم بعد هم در پرسپولیس و تیم ملی با هم بودیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139335" target="_blank">📅 00:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139334">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
ورزش‌سه: در تمرین امروز تارتار به سبک بازی با تراکتور بازی با ۳ هافبک و ۳ مهاجم رو تست کرده که مثلث خط حمله رو علیپور ، بیفوما و محبی تشکیل میدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139334" target="_blank">📅 00:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139333">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
✔️
پیام اومده فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139333" target="_blank">📅 00:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139332">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139332" target="_blank">📅 00:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139331">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfcdef74da.mp4?token=hgMcol6r5OdtJ7oBGd92DwVFG64lEcbiO1Zvsuf80urtC8H1bAG5oY_cDuF5Ad_aMmUjTVFMyceDHHdJKvK1HENR31ECOHgmK5AO7PuhHxrGSurcQH3qT3HAXc6m8pVPeERkm1lq625PcJrXco8A_7VNfILv0h1DdXMIwJs67NWcuw5GT8FPvc9UipItPJ8M6gNim4on8vJ0aYcnn2LdxGN8v7HXP0CnHGb9I53mOgHuhJszYZdwDO5oVN4wha-IJG3RYrhX45QhuWRZsqA9RCs7v3jglHv1NxQlgjoCnl0zzpiqRzXwVglQXO2k-mOZuj2RkakJgaPTKT5bAAZJYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfcdef74da.mp4?token=hgMcol6r5OdtJ7oBGd92DwVFG64lEcbiO1Zvsuf80urtC8H1bAG5oY_cDuF5Ad_aMmUjTVFMyceDHHdJKvK1HENR31ECOHgmK5AO7PuhHxrGSurcQH3qT3HAXc6m8pVPeERkm1lq625PcJrXco8A_7VNfILv0h1DdXMIwJs67NWcuw5GT8FPvc9UipItPJ8M6gNim4on8vJ0aYcnn2LdxGN8v7HXP0CnHGb9I53mOgHuhJszYZdwDO5oVN4wha-IJG3RYrhX45QhuWRZsqA9RCs7v3jglHv1NxQlgjoCnl0zzpiqRzXwVglQXO2k-mOZuj2RkakJgaPTKT5bAAZJYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚫
عادل فردوسی پور: با دیدن فوتبال ایران میتونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139331" target="_blank">📅 23:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139330">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">📸
صادقیان دیشب تو ورزشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139330" target="_blank">📅 23:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139329">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❤️
❤️
اورونوف در تمرین آماده بوده اما وضعیت جسمانیش همچنان بهش اجازه نمیده که ۹۰ دقیقه بازی کنه و قراره نیمه‌ی دوم به بازی بیاد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139329" target="_blank">📅 23:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139328">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✔️
✔️
‏ ترامپ به شبکه فاکس نیوز: ما امشب به حمله ایران به نیروهای آمریکایی که شب گذشته در اردن رخ داد، پاسخ خواهیم داد.ما به آنها ضربه سختی وارد خواهیم کرد. پاسخ داده خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139328" target="_blank">📅 23:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139327">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❤️
❤️
10 دربی بدون شکست برای کاپیتان
✅
حسین کنعانی در آستانه یازدهمین حضور خود در شهرآورد پایتخت قرار دارد؛ کاپیتان سرخ‌ها در 10 دربی گذشته که به میدان رفته، هرگز شکست نخورده است. او حالا به دنبال حفظ این رکورد ارزشمند در یازدهمین شهرآورد خود است.
✅
پیش از کنعانی نیز کاپیتان دیگر سرخ‌ها یعنی امید عالیشاه که امسال از جمع تیم جدا شد. با ثبت 18 دربی بدون شکست، یکی از ماندگارترین رکوردهای سرخپوشان در تاریخ این رقابت را به نام خود ثبت کرده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139327" target="_blank">📅 22:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139326">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139326" target="_blank">📅 22:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139325">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a89afdca4.mp4?token=r-Wcsuqq4jsMlooOLndotflnLAW1XTkMh-dAHPY30JFoVC2AwGUaJhnLjt4bs2nsHVH3CY5opquulxsszBZaOidLVRVJwA3kMUJvN14EMC8kMGWi090JNpIYKNZN8dGZaqVd5EUBjgYitJmqa8kPotOiWxwWQNH1WlR1ZPPak9l2KIGkkg-WCjAFchQC1JL-ebT2OLapHMWz4T8gwRL3VRrc5gSjBQsJmmyJ7az4tQVagVf9CpPy1kKdRyzVxJuB1nVncLLBo1Bv9eaN4V2MxqngVOMY9vKWYnqfV9zrQDbJS9LC39hD7FabaUGE-lOBYRoB-tBAOJv-lNWtxlqpig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a89afdca4.mp4?token=r-Wcsuqq4jsMlooOLndotflnLAW1XTkMh-dAHPY30JFoVC2AwGUaJhnLjt4bs2nsHVH3CY5opquulxsszBZaOidLVRVJwA3kMUJvN14EMC8kMGWi090JNpIYKNZN8dGZaqVd5EUBjgYitJmqa8kPotOiWxwWQNH1WlR1ZPPak9l2KIGkkg-WCjAFchQC1JL-ebT2OLapHMWz4T8gwRL3VRrc5gSjBQsJmmyJ7az4tQVagVf9CpPy1kKdRyzVxJuB1nVncLLBo1Bv9eaN4V2MxqngVOMY9vKWYnqfV9zrQDbJS9LC39hD7FabaUGE-lOBYRoB-tBAOJv-lNWtxlqpig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی تو لیگ دو روسیه‌ با پرتاب اوت پاس گل داد و پشمای گزارشگر به این شکل ریخت
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139325" target="_blank">📅 22:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139324">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
تأیید پارگی رباط صلیبی «مهدی ترابی» بعد از MRI اول، در انتظار نتیجه معاینه دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139324" target="_blank">📅 22:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139323">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoN6ngOaPMi4RbQLveuhal1jYJWOrt8qT5VxEoGm_RhJHRCkvWlp6ldZxC97LcObyeQcNc9c3aV_oO3_vWKEp7WShx8dkWJloBSrl-BUaRSiuhxacjKN8fAaMwqb0lbzQJrwJHrLu0-ia6n33qBHeV8gVoB5bdSmrHsy0qSa7vbe5zci2qPnK8QLk8ij6Q9CX2OyTx1bYS3KaK0JyLRQvO0PwYyoN3z_XV5fHlnCE8Z8XF3M6Mgw-JhbKz16d0xBiXRVVgkkQFhYE5p2qxspsir3DhXcRBHnEhCK1pojb1MnV4kiUaQyewmsSAU2PycCMzDXfNPIuA2T1VYa2FNR8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
سرخپوشان راهی اردو شدند
🔴
🔴
تمرین امروز تیم پرسپولیس در حالی برگزار شد که ابوالفضل جلالی همراه با دیگر بازیکنان در تمرین شرکت کرد. در پایان تمرین، بازیکنان راهی اردو شدند‌ و فردا هم یک جلسه تمرینی خواهند داشت. سرخپوشان سپس برای دیدار مقابل استقلال راهی اصفهان می شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/139323" target="_blank">📅 22:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139322">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووری
‼️
🔵
🔹
رسمی، با اعلام فدراسیون فوتبال موعود بنیادی فر داور دربی پایتخت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139322" target="_blank">📅 21:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139321">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
اسپورت عراق؛ یحیی گل محمدی داره با سپاهان مذاکره می‌کنه، اون اصلا حواسش به تیمش دهوک نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139321" target="_blank">📅 21:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139320">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
✔️
جلالی مصدومیتش تموم شده و از دیروز به تمرینات گروهی اضافه شده
❌
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139320" target="_blank">📅 21:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139319">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🔴
بلیت‌فروشی دربی پایتخت آغاز شد  هواداران عزیز از طریق لینک زیر برای خرید بلیت اقدام کنید تا روز چهارشنبه ورزشگاه در دست ارتش سرخ باشه
❤️
https://ticket.sepahansc.com
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/139319" target="_blank">📅 21:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139318">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5Pjgucz4OjM6edmOJ05q6a-44UP0IFduLi7dcRUeIRbIBYrNetnhKmGxUpuYamTWx-vqVboOD2cyjPX_dS36FRRpLIxlygd4yCwk139fd4_IB1is4scCtGzQqVVRQdiEkIuDNZtM5u62a7pRbjo_VnO1lEGuV-lS0oPZ01UXxOqLpqspJsC8psD_nEIT31BlIZpK0O7agthvZBZSdY9Mweo3VxdcSW5a7KvnBJY12piJVHWGnM5Oaf4y4rm77K_7NNMnhgJWDmf-VAo-9RgW8JxVCVTjdxYhJKvnEDGpDhmzBApxc7DUCXL9daMnsPwhcRG67KMw5Qx_qpKpTkQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووری
‼️
🔵
🔹
رسمی، با اعلام فدراسیون فوتبال موعود بنیادی فر داور دربی پایتخت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139318" target="_blank">📅 21:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139317">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSWMPJIWoOqNbahFNIIVyLiYs_jKn0C_KnQPEp_VT1PVCmxbUnyQ9zOu4Rv297FfNzfZkXA0REfoXNktEUhxbswWyenbBKvw8avwPofhOcReA0btDBIpxSUAlrygb-9iLLVOhioSIcbgd_1ykDFnZ4DpF6q6TNjHbZ3QTLPJcyBtagSIZ2wjvIoG9pDc0LTdjH-53mbzyJvGDqBXsh0O_4yjgeYK7Ft6ggnd2Exm_hCiQy4chej-xb2WbSjzQVUKeyLehlvmNzTsmZGKakFBl55ZCwzzU9-ZuuBbFCaLQrxHmCk_3AKc1urKTJtFSQVp7iuA0WKIPaMaUDhTpoN3fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
بلیت‌فروشی دربی پایتخت آغاز شد
هواداران عزیز از طریق لینک زیر برای خرید بلیت اقدام کنید تا روز چهارشنبه ورزشگاه در دست ارتش سرخ باشه
❤️
https://ticket.sepahansc.com
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139317" target="_blank">📅 21:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139316">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIguywx4xg05J7zxg430K-IQ4n-mAHwgs_sDbkmmC0cRSI4Rkc3zxTiwpheH36eFV3UMKFTtKvvpUmZvkLUEgP2618VcEUWQPWaorJpSIl9zSy-68BHV44c0CwIY22O_2ReB_eemk3S_rtDbJIxvQR7EaJxOAd7jDbpgrJ9dy5Dyy_QdRaHhaVA0uvSqitLlGr_QFSWYcNQ8X0G1_-WrxYMvSpxtdT6P7hk0NcX-dTI_2c-XUgyrEROfe03PSYQriwKigWSZbj7YyC1H09KYdUWTgHOr6F4GSS7gTG991fEa3ddLGpfXC2unSV2hPozP5EDXtx8vNyigXvXpSrQ8zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بارسا به دنبال ادامه مسیر بردها!
⚽️
رایووایکانو آمده تا کار را برای کاتالان‌ها سخت کند؛ نبردی برای صدرنشینی جایی برای لغزش نیست!
[
بارسلونا
🔵
🆚
🔴
رایووایکانو
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139316" target="_blank">📅 20:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139315">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
اردوی تیم ملی امید تعطیل شد و کسی بازیکن نداد و سه ستاره‌ی پرسپولیس به دربی میرسن/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139315" target="_blank">📅 20:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139314">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
✔️
احتمال زیاد پرسپولیس با ۲ مهاجم بازی میکنه و بیفوما هم وینگر چپ هس تا پرسپولیس تو حملات با توجه به ۳ دفاعه بودن استقلال کمبود نفرات نداشته باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139314" target="_blank">📅 18:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139313">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
کامنت کریستیانو رونالدو برای مسی:«لئو، توی این روزهای سخت، یه بغل خیلی بزرگ برای تو و عزیزانت میفرستم. خیلی قوی باشین.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/139313" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139312">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⭕️
⭕️
🇺🇸
ترامپ: اگر به کشورهای منطقه حمله کنید، تلفات سنگینی خواهید داد و بهای بسیار سنگینی خواهید پرداخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/139312" target="_blank">📅 18:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139311">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
✔️
✔️
جلالی مصدومیتش تموم شده و از دیروز به تمرینات گروهی اضافه شده
❌
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/139311" target="_blank">📅 15:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139310">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
تارتار نمی‌خواد ریسک کنه!
✅
به احتمال خیلی زیاد جلالی در دربی به میدان نمی‌ره و تیکدری مثل بازی‌های قبل در پست دفاع چپ پرسپولیس قرار خواهد گرفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/139310" target="_blank">📅 15:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139309">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
فوری؛ هدایت ممبینی برکنار شد و با حکم مهدی تاج، حامد مومنی به عنوان سرپرست دبیرکلی منصوب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/139309" target="_blank">📅 15:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139308">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⭕️
⭕️
⭕️
با اعلام یاسر همرنگ
🚨
کوپال ناظمی داور دربی شد
📺
موعود بنيادی فر داور var شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/139308" target="_blank">📅 15:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139307">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🤩
پیمان حدادی: وظیفه تلویزیون اینترنتی باشگاه، بازتاب صدای هواداران و پیگیری مطالبات آنهاست؛ رسانه‌ای که باید تریبون هواداران باشد و خواسته‌های آنان را به گوش مسئولان برساند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139307" target="_blank">📅 15:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139306">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4Ad3us3q8dvluYmsq28GTJXELTzVFEV-V0VORb-MjqZzCEiU4XN51nf-hG-p6URe_cSIrsQeZ6VGwK7729ROPffaxShogzh0u9JI9d9aVvx9ofjVjuynn1jxSDgfnTOPkMZtYTfoRAXyK5clf5qYOlkZKav7IR_OEMiopLLaH-F9XRiR7AkOos8LTNeaNPvkMfhZr6T5lCaaLjYcpQFiemCOMdFe6dUN2_bCcZ6vw1RGQucMkoYQJ4fXafWUlq_XC4Cm9N8G2C9NYuzpDVpTIFCPS9EHPPkFJwXYdbo56LkGzMCv35ny1IMbPLF3YLoM-JkgIHNnjssS6XUDa8TkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
ویلا پارک آماده یک شبِ آتشین
🔥
استون‌ویلا و آرسنال؛ جدال قدرت و جاه‌طلبی
اینجا هر اشتباه می‌تونه بهای سنگینی داشته باشه!
[
استون‌ویلا
🔴
🆚
🔴
آرسنال
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/139306" target="_blank">📅 14:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139305">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
حدادی قول داده فردا صبح پاداش پیروزی مقابل ملوان رو بریزه به حساب بازیکنا تا قبل دربی انرژی بگیرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/139305" target="_blank">📅 13:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139304">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‼️
‼️
بلیت فروشی عصر امروز شروع میشه که ۲۹ هزار بلیت برای آقایان و ۶ هزار بلیت برای بانوان به صورت ۵۰ ۵۰ بین هوادارای دو تیم تقسیم میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/139304" target="_blank">📅 10:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139303">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✔️
✔️
✔️
فووووووووووووری
🔄
🔄
با اعلام باشگاه استقلال بلیط فروشی دربی از ظهر امروز آغاز خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/139303" target="_blank">📅 10:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139302">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
بلیط فروشی دیدار پرسپولیس و استقلال خوزستان شروع شد . از طریق لینک زیر میتونید برای خرید بلیط اقدام کنید   https://footballeticket.ir/buy-ticket.zul;jsessionid=23B55854CCBC6E89F276AA81C2DC01A1#  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/139302" target="_blank">📅 10:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139301">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‼️
ممبینی : به عنوان دبیر کل فدراسیون فوتبال تا الان نمی دانم چه کسی گفته است که تورنمنت سه جانبه برگزار شود/  هیچ کسی هم نمی گوید که من گفتم و اصلا نامه ای هم در این زمینه وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/139301" target="_blank">📅 10:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139300">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/me2eu6HPbaC3lMNJ8naN_iBThJ0NpIAK06SnbJVTTF3f_SKzTH7fBS-m_XWGzzOWvJsVpsE-9zPJywTvoiA-hYJHnQU1OtU2aa4B53CTWAXqGgcQ5VSJgrLqr0WjxTYQFYZqgbqrNjJwrCKRjVQGWHkECcN6z7JVka46of4pWNwL3gRuXDGELpt60n46mg4B3FeQAa03dxGpp43OjhPoj8gaUrM1sx13fgE4c1DUNEtowNAtz6BVVaq8olGGT3gXxERjm7AjmNn_66C0xcfDhpmCJGKZpELFjcGP3QjamP7SWGJItKxere-5JXrNvkAxTl1_F70d3qOLmYAuKetcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسپورت عراق؛ یحیی گل محمدی داره با سپاهان مذاکره می‌کنه، اون اصلا حواسش به تیمش دهوک نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/139300" target="_blank">📅 10:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139299">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🏅
هوادار همین سبکو میخواد آقا تارتار تیمی بدون ترس و سراسر هجومی تیمی که می‌تونست امشب خیلی راحت بالا 5 تا هم گل بزنه
⏺
خداشکر با روحیه بالا سراغ دربی رفتیم و امیدوارم تو دربی هم همینطور و همین سبک رو ارائه بدیم
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/139299" target="_blank">📅 10:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139298">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
✔️
از هتل المپیک خبر رسیده است مهدی ترابی ستاره تراکتور به علت مصدومیت ادامه فصل را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/139298" target="_blank">📅 10:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139297">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
چند دقیقه پیش تهران لرزید کیا حس کردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/139297" target="_blank">📅 08:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139296">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
سلام صبح همتون به خیر و شادی ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/139296" target="_blank">📅 08:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139295">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
سلام صبح همتون به خیر و شادی ..
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/139295" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139294">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4I6Of6KtGCyVkE9Y66M2HlD7GtKeeVi--gHtBqaI7iym6hA0Qpxqo2Gmqqs__wdoUseXFBGMuivs0ndOPp81KaGKVy0-dFw2dY8MoKG7oZFHL2UpYa6VaT7fHSCbtHYJzU0mTcagAMSVv6bz66X2UuBT-kk0UWws-7Xzi5EuDpDyLZgtVi1h60wosH-gOlLVmYefqvQIOgr0Ersvpc6ZX3Z24kcrl7srHPGm85h1X4UuAfSv_tiGJvOSZza_PDJkZawDRVnGZ6eo39YMaJ2ek5NDKK7Tvr0AqFdCn1IhBhRgsphWuvTbL2b5ODAB0Elei7G6ttLt1h48WjaVjiUTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد در نیویورک شروع شد!
🟡
گرنداسلم یو‌اس اوپن؛ جایی برای جنگِ ستاره‌‌ها
🎾
بزرگان تنیس برای آخرین جام بزرگ سال می‌جنگند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی رقابت‌های یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتونو ثبت کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/139294" target="_blank">📅 02:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139293">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
سپاه پاسداران انقلاب اسلامی :
🔴
🔴
تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/139293" target="_blank">📅 01:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139292">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
✅
قیمت دلار برای اولین بار در تاریخ به ۲۰۶ هزار تومان رسید  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/139292" target="_blank">📅 01:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139291">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">📸
صادقیان دیشب تو ورزشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/139291" target="_blank">📅 01:13 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
