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
<img src="https://cdn4.telesco.pe/file/FWiGQUMtIa772MhHLQZTCv0gxTshBD1sMXATaDcI6xj2LF3qaxrB-tD9tlSpOzR5pXOY1r6O3xm4zPg5htS6PUYDVYLSXz4CV2IvwbMXaxzudx1SKSeYuwphiIxm1wuRWHZekaVut6S78Vi4lovoMYIMylbzqjAjLd8cE8a8QNKa3kdekzQL-ysvGbY23mdGleS1-6CAHIv-Ye5z9dLbuOnym_CgM1UoRaP-9-UGBGnGx0myjahlgU74CL81UqPy_wKyZk7ifer7WnlraxcaWnQD8SnL0b2eFf6g2PMSEJ7aFotfRdR7USNmt4yeW3FhZef3BkRr8S6WYVORtrTHjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 21:55:24</div>
<hr>

<div class="tg-post" id="msg-135535">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b795de8c95.mp4?token=JB2LjPu7zda_jajCBhRuVQu6PTavY9Pn8MwJfI44JU6KMuGob4QrD0YsYTgfv03DkFfujbAXq_zKV4u-oSmDvvSQoGUIOXBM0h2mjMUxgLpgYxnm8DzCmvlJe8CCeqTy_rcETK0B2H2o5RrskflIxmfoZEAz9z4Ludxav852Dr78qwtrRqsHPBn52oBDswBB5BARWskyofU2v31KCMHQf1E5SWVYW7m152CHQODYnyg7lRkgSxMxWwC300Jz6eDdk1xRFJDWKoyhTlSeIcVLvXaLS9fR2yDjiBv2_rFyBFzydssj1S06ajqg1Xyo22C_6Tym2uGBssNqiOm13pIPiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b795de8c95.mp4?token=JB2LjPu7zda_jajCBhRuVQu6PTavY9Pn8MwJfI44JU6KMuGob4QrD0YsYTgfv03DkFfujbAXq_zKV4u-oSmDvvSQoGUIOXBM0h2mjMUxgLpgYxnm8DzCmvlJe8CCeqTy_rcETK0B2H2o5RrskflIxmfoZEAz9z4Ludxav852Dr78qwtrRqsHPBn52oBDswBB5BARWskyofU2v31KCMHQf1E5SWVYW7m152CHQODYnyg7lRkgSxMxWwC300Jz6eDdk1xRFJDWKoyhTlSeIcVLvXaLS9fR2yDjiBv2_rFyBFzydssj1S06ajqg1Xyo22C_6Tym2uGBssNqiOm13pIPiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شهاب زندی: دانیال ایری بازیکن ماست و دیگر قابل فروش نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 153 · <a href="https://t.me/SorkhTimes/135535" target="_blank">📅 21:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135534">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
حدادی: هی میگن چرا از گلگهر بازیکن میخری؟ مگه تراکتور از ما بازیکن نخرید چنتا رفت قهرمان شد؟ گل گهر با سه امتیاز کمیته انضباطی نایب قهرمان لیگ برتر و جام سه جانبه هم در آستانه قهرمانی بود
😕
😕
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 427 · <a href="https://t.me/SorkhTimes/135534" target="_blank">📅 21:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135533">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
طبق سیاست مون بازیکن بالای 30 سال نمیگیریم
🔴
آخر هفته از سرلک و عالیشاه قول گرفتم بیان سر تمرین تا مراسم خداحافظی داشته باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 457 · <a href="https://t.me/SorkhTimes/135533" target="_blank">📅 21:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135532">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
فوری از فرشید حقیری: پرسپولیس با وحید امیری قرارداد بسته!!!!
❗️
پ.ن جونم به این جوان‌گرایی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 700 · <a href="https://t.me/SorkhTimes/135532" target="_blank">📅 21:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135531">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
پیمان حدادی : فردا یا پس فردا با آقای علی علیپور برای تمدید جلسه داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 913 · <a href="https://t.me/SorkhTimes/135531" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135530">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❗️
پیمان حدادی : ما به میلاد محمدی پیشنهادمونو دادیم فردا آخرین فرصته که قرارداد رو امضا کنه اگه نکنه از لیست تیم خارج میشه این پرسپولیسه که واس بازیکن تعیین تکلیف میکنه نه بالعکس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 914 · <a href="https://t.me/SorkhTimes/135530" target="_blank">📅 21:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135529">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
پیمان حدادی : صحبت از مهدی ترابی، دانیال اسماعیلی فر، آریا یوسفی، رامین رضاییانه آیا تیم رقیبمون به ما بازیکن میده وقتی قرارداد دارن؟
✅
مثل اینه من اورونوف رو به اون تیما بدم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/135529" target="_blank">📅 21:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135528">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
پیمان حدادی : این معقول نیست من برم دفاع ۲۱ ساله رو ۲ میلیون دلار بگیرم؟ اگه این دفاع رو ۲ میلیون بگیرم به بازیکن ملی پوشم چقدر بدم؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/135528" target="_blank">📅 21:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135527">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
پیمان حدادی : بازیکن های ۲۶ تا ۲۹ رو قصد داریم طوری جذب کنیم که رضایتنامه براشون پرداخت نکنیم
❗️
بازیکن های زیر ۲۵ سال هم با قرارداد ۴ یا ۵ ساله جذب کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/135527" target="_blank">📅 21:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135526">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
پیمان حدادی : تیمی که داریم میبندیم تو ذهنمون هست که میانگین سنی بازیکنا بین ۲۵ تا ۲۶ باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/135526" target="_blank">📅 21:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135525">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❗️
❗️
پیمان حدادی : یکی از اشکالات ما در فصل های قبل این بود که در پست های مختلف بازیکن رقیب نداشته و بازیکنایی رو میاریم که انگیزه داشته باشه، بازیکنی که ۴،۵ جام گرفته دیگه اون انگیزه سابق رو نداره، قصد جوونگرایی داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/135525" target="_blank">📅 21:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135524">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
پیمان حدادی : تو نیم فصل با اون شرایط کشور ۳ تا بازیکن جذب کردیم ولی هوادار از این پنجره نقل و انتقالاتی باید از عملکرد مدیریت انتظار داشته باشه با تموم محدودیت هایی که وجود داره، از این به بعد کارنامه مدیریت تو نقل و انتقالات مشخص میشه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/135524" target="_blank">📅 21:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135523">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
پیمان حدادی : شما بهترین سرمربی رو هم بیارین وقتی ابزار لازم رو نداشته باشه نمیتونه نتیجه بگیره، اون سالی که آقای اوسمار تیمو قهرمان کرد اورونوف رو ساعت ۳ و نیم شب آوردیم عبدالکریم حسن و آل کثیر رو آوردیم ولی تو این ۲ فصل ابزار لازم رو سرمربی هامون نداشتن…</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/135523" target="_blank">📅 21:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135522">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
پیمان حدادی : ما به درخواست هوادار آقای اوسمار رو آوردیم ولی اون چیزی که انتظار داشتیم نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/SorkhTimes/135522" target="_blank">📅 21:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135521">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
پیمان حدادی : خیلی سعی میکنیم که دچار هیجانات فضای مجازی تو تصمیماتمون نشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/SorkhTimes/135521" target="_blank">📅 21:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135520">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‼️
🏅
تفاهم نامه همکاری بین باشگاه پرسپولیس و فدراسیون کشتی توسط پیمان حدادی و علیرضا دبیر امضا شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/SorkhTimes/135520" target="_blank">📅 21:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135518">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
امروز اقا کریم با باشگاه جلسه داره و تکلیفش مشخص میشه/ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SorkhTimes/135518" target="_blank">📅 21:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135517">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/135517" target="_blank">📅 21:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135516">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗️
باشگاه پرسپولیس خبر داد: امید عالیشاه با توافق دوجانبه از پرسپولیس جدا شد
❌
باشگاه ضمن قدرددانی از فسخ توافقی خبر داد و برای او و سرلک آرزوی موفقیت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/135516" target="_blank">📅 21:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135515">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
ویدیوی باشگاه پرسپولیس برای جدایی میلاد سرلک، هافبک این
تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/135515" target="_blank">📅 21:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135514">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join
Join Join Join</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/135514" target="_blank">📅 21:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135513">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Na16ZPUx4UC_wtPrBydAhOFSEMN46ZOru3e1V-Sc3AXhp6TPa92PxXQ5LTZ1zhuCe89j-ODImmTH__rEaEKFfJaZenozr9Ft0C77dHxX171vov2Uz3voT_Yl9Y3icCz6UuLmiD8IPQDp0T6B_6K5zo_LPOQSWwmuycXrrHmi9KRJZco5KQKUyW0E0IGh2h4yJhUolYwc8sjGtLWVkCQq42-NvNWMyArokiB_DjfWZZAzDGD2s1UAHZw9Gc8omPK9PAvfAwK-QqGkwPbQPP5CkZfvYe4wqWQ19UH0XUkQ72eGSpHYfhITvy9WdIAu49yuKrpbUPAOnCZhaBzdOP1YZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکسمون عالی برد شد
✅
💵
✈️
@Bet_Giantss</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SorkhTimes/135513" target="_blank">📅 21:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135512">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlYt3Jv5QL8p-qGZHSclVmP32A6EWQKU9BlUYAakwPwmGm3voQ5e7UHD3aomYuB7nC9bPn0UeSuwLsnNh0KogjJWm4BA0OY9ilCQ0JDNfxbIg5Iftnncx2gXeq3fqDm43skJwhlQ2vG0CSNR626BwGfk6s8RNJFFBzZfrut0Lju4DZYeKVnj11yzV0WnZYahpVWvssBes0YxC-AkyQik8mOWbKth_6uJujCyx82J2oqW1Ajv1pEGeC23lXMCv8AYscprvyvmYMU-41yyVOvNms2kmKQT6RAqJcHlENJL4gaa0aJdBkRnol3DNFiDCWp9fSnrxB5E-X0dlvm2R-Dzxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔴
امید عالیشاه.. کاپیتان پرافتخارترین پرسپولیس . پس از 13 سال از پرسپولیس جدا شد
😭
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/135512" target="_blank">📅 20:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135511">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
باشگاه پرسپولیس خبر داد:
امید عالیشاه با توافق دوجانبه از پرسپولیس جدا شد
❌
باشگاه ضمن قدرددانی از فسخ توافقی خبر داد و برای او و سرلک آرزوی موفقیت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/135511" target="_blank">📅 19:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135510">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2uYS0MK_PHlCOw3oAYe5x7ECj83NvTGfXV0gxjzixr-0nq6Zh2T8cTjpdLzakcBrE8urqleIkJ-3dqujOJfKZzd-kF-a3YKIAl6UR0-lE7hr3Y7KpKjq101cpjNdM1qgoU58wASlMnrE5iVTaSHJ0YLIk0m3wmVRsAuTqr1ozQQdPuAly2rP86O0ub-d1S6JswfLwhbC9kyRfQukEJbQHReTOu20rNU9UcErlqk8KHGJ_dvGibBGZ8-0ATlzTTD50nIrZ3-niFKtORX7JW5MsSY_xhti20l2Y_FFnFkKNU1BNnce6UfeFtlV8k1-fY7AGgR3CGKIizo4YzYU8QW3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/135510" target="_blank">📅 19:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135509">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
میلاد سرلک به شکل توافقی از پرسپولیس جدا شد
🔴
پس از مذاکرات انجام‌شده بین مدیریت باشگاه و میلاد سرلک، هافبک تیم فوتبال پرسپولیس، طرفین به توافق نهایی برای فسخ توافقی قرارداد دست یافتند.
❌
در جلسه‌ای که امروز برای بررسی وضعیت قرارداد وی برگزار شد، با موافقت دو طرف، درنهایت قرارداد میلاد سرلک فسخ گردید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/135509" target="_blank">📅 19:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135508">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFJLYyxgtKZaBpjzgfZbvNqmt33CKy4eLuE3l9-AGD7wezOq4wUY8lhZUdWnQJf8Bm7j_kZpYxd6VBz5PiDScfz3VBB91lLF6enLFfLxScZqyoCRPRqzwajYL0NN9tjXqALiNOmSism2bSYymHq1JK9IxJKAPX0j6R4iXe3o5OV_kXo1Tr766Ug6QX3Gi2WfxLbzdQPnE9vznRyvfP7GGqEHGtMdoqaMAeuBWf2HraHym00NtoZAWLYdK5LLl8KluC1bOG2n3_kmyP67s0Zc960Um3QzDBKgY1L9M_54LhSndggRJTNdOdKY7N8TGrkhIeQVOUxDeOtNBSQSGf1ccA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
❗️
سرلک بخشی از قرارداد فصل بعدش رو دریافت میکنه و بعد جدا میشه/ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/135508" target="_blank">📅 19:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135507">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/135507" target="_blank">📅 18:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135506">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/135506" target="_blank">📅 18:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135505">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
بنظر میرسه امشب پورعلی هم رونمایی شه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/135505" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135504">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
✅
پوریا پورعلی با خداحافظی از گل گهر یک قدم  به پرسپولیس نزدیک شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/135504" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135503">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
فوری از فرشید حقیری: پرسپولیس با وحید امیری قرارداد بسته!!!!
❗️
پ.ن جونم به این جوان‌گرایی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/135503" target="_blank">📅 18:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135502">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KFgLFUziEDg7ypR-6MNVUH98ILdzJQPHb1GhN2SVJeBhhTRJ6Dn8m7r9KNmQcOjNGUoQxSJ5UaUOAVDJAo7Y67A-8ANOb9WOb-BuOd9ancMSf4KG4lvo8Va9lafu-7M99rTOssdaKvqi2vfMoHSkDKj_k_tviEKu4Ez3Rs6HzOLHHldNqyrBHILZ3C-tG-_9b6QG9Lxdy5OBAtpbaIqbt3VYpRji6P5T8EzQL8rZbpcDKP2vI0wf9Iq9qBkxpUsw5b5eHTp2RXwOsFaSUyTKg9dMq73uJsG5fol0eLNIvMkQwNruijbe6Y3rB9PPrF7FUp2puKktnJHVWoxSJr-isA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ادعای فرهیختگان: محمد عمری از لیگ قطر و امارات پیشنهاد داره و ممکنه باشگاه با دریافت ۶۰۰ هزار دلار از این تیم‌ها رضایت‌نامه عمری رو صادر کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/135502" target="_blank">📅 18:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135501">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❗️
❗️
سرلک بخشی از قرارداد فصل بعدش رو دریافت میکنه و بعد جدا میشه/ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/135501" target="_blank">📅 17:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135500">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔘
🔘
🔘
باشگاه پرسپولیس فردا یعنی روز شنبه مذاکرات نهایی و پایانی خود با دانیال ایری و باشگاه نساجی را انجام خواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/135500" target="_blank">📅 17:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135499">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
🔴
🔴
تارتار گفته چون فعلا تو جذب هیچ وینگری موفق نبودید اجازه نمیدم بجز عالیشاه وینگر دیگه ای جدا شه و هروقت جذب کردید میزارم جدا شن
🔴
بدین ترتیب بیفوما و شکاری فعلا با تیم میمونن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/135499" target="_blank">📅 17:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135498">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
برگام فیروز کریمی شده کارشناس بازی های جام جهانی کانال  gem tv
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/135498" target="_blank">📅 17:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135497">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
فوررررریییی با اعلام ترانسفر مارکت علی علیپور از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/135497" target="_blank">📅 16:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135496">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4YcU2MPmJGBeI8s2W7zn4IF4VXNb6lp8_4tFHgYlUYQjYTCDsttVTdWovZHOoagmGK0d3OxnZXMJVZHlBtlByT_DOU-0LE8quBJ4Da1w9Ovk_D_e01QdfiRIUn6WHXPuHntdFqZeedRnRpJLxQ9SF3nWEWZsNainR70n795lfkOs6OlnYv0-uaymNYXsohFLVjArIXslHq7mPqXecA4ccQy4Y_dzZ742HdzYJ8APaX1aDN-Sh4ja-d32OLj83bD3AtCdclPkjE2iTg251EwOHWy5DGlkj8F5u9IafzVTksK2y_M68sIeDyxCzpk9sdrSJbhe4ErIYeN7vPxEYqjLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوری؛ شنیده ها: رضا شکاری از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/135496" target="_blank">📅 15:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135495">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dOcJf5RKXQlu_Zye0iTrCm9jKYzeroNXXeYbSesva640ByVLIKsFIqVYfjV3drQyy9ZjIC6oZ-z3VAnxQxHKme62uCft21VvsiATLe8PgtSkNryArX8u78LVKm9QMRh-eBOR7GzCNq2aBMbKfSSmciOU9rImUr588jGBS-Exi1cp4yBcFt1qGPXkbRadZ_X5h_S9kdUvNO8NV3Ae2ySFeWsquaZStjYpQRitrPcc-KybYWT46pW9sTubPmKK7cuY7-an5cDfqZhgEFgmddOVNY4zoGlW-0mbE2fGMR2m-rCodl9rO4qvelmiJhQJRT5OmEnnTVnDCLbuVup9POLaYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری از فرشید حقیری: پرسپولیس با وحید امیری قرارداد بسته!!!!
❗️
پ.ن جونم به این جوان‌گرایی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/135495" target="_blank">📅 15:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135494">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evgkWZzoPbpjQrWbDenluMazucA5fT8RrTSbxs019Ivn0AAg-a8BhHkAk1HkzqjJ3wRNGQfE3yXzFYCt_hN_xmLW0b1m5mlkFKxPhgsnnmCjKsKpjD1Qu0Os1E_G55O8SbV7XuBhf-9nPR_iwhqpMpcn8W4nG8tmXEerkTbBzW-VjD3RGIuFj-vqJT5CHG9odVr4HRPHpJEHJV2NFcD6sKWZfd6HRYsrYrqVBEjzVg5U6GCpJ_da8_k4dAgeHj0f1AKJOaPI8LckU3u6kI6c0ZTUnAev5OA6xr8ZwbNF0v0vjerSR3z65RD1k5FRKeWAzlZi6-NhucfhEu2oY2PJFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏅
تفاهم نامه همکاری بین باشگاه پرسپولیس و فدراسیون کشتی توسط پیمان حدادی و علیرضا دبیر امضا شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/135494" target="_blank">📅 15:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135492">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏅
پس از امضای تفاهنامه با باشگاه پرسپولیس؛
🎤
صحبت‌های علیرضا دبیر، رئیس فدراسیون کشتی
❓
دخالتی در قضیه خداداد و پرسپولیس نداشتم
❓
ما فقط معرف بودیم
❓
من نوکری ورزش ایران را میکنم
❓
از ایرانی‌های آمریکا تشکر میکنم
❓
بهترین ایرانی‌های خارج از کشور در آمریکا هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/135492" target="_blank">📅 15:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135491">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
🔴
🔴
ورزش سه در خبری اختصاصی مدعی شد استقلال به سپاهان و پرسپولیس هایجک زده و علی نعمتی رو به خدمت گرفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/135491" target="_blank">📅 14:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135490">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
کریم باقری از شنبه یا یکشنبه به تمرینات برمی‌گرده و مشکلی برای حضورش نیست.
✍
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/135490" target="_blank">📅 14:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135489">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
باشگاه پرسپولیس می‌خواهد برای کاپیتان مراسم خداحافظی بگیرد؛
✅
✅
باشگاه در تدارک برگزاری مراسم خداحافظی برای امید عالیشاه است؛ اتفاقی که در سال‌های اخیر برای هیچ بازیکنی رخ نداده و نشان می‌دهد باشگاه قصد دارد با احترام از کاپیتان سابقش تقدیر کند.
❗️
❗️
حالا…</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/135489" target="_blank">📅 14:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135488">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
مجتبی فخریان بصورت قرضی راهی گلگهر شد تا پوریا پورعلی بصورت رایگان به پرسپولیس بپیوندد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/135488" target="_blank">📅 14:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135487">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135487" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/135487" target="_blank">📅 14:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135486">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jx2QtNN8wP7YAVlBFmUgW4GjfXmDhYpgOFi9h2rRmAR4J-6cHYLhLWsah5i--19s8Hs5XWgHyyN_S62q6B7Q7F4sc6bfy_2vwRnaxfu1lGj5Z2ezFaSod4ypwE6ThEVyRa9P4aMRmmHw-dWOEicPH9VRPMsZqbCKjuCwhgR47Mspm6RjZBjvP1jlU6D4wVqTUqQfQ1d_FBxZ08M1yk0D5-Lhzp29ziCdl4x8__ZhYFgwXSpabdu1Ztj4fmqMFBMAjomqohXAVai6EwlkVSj3lqSb8F6Vrjj6EZapq7xonollHiWHc35U7ZcsdyTe-BLr9Bc2o3faJm-5P8wHgL36CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/135486" target="_blank">📅 14:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135484">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6oTK7B5HgY6Rodjvt1XNBnIzrr5jhSBlIZx8AWrUZal2oKWcOKjQGR1LKktxW6ctWzot1nrdb2ol06ghrVEynBsJDPEKANI1A9SS3N_XiDklJIq8xyFuZzEj7qCKLH_FJ3GwJFo3IwNeykk5gtyPkc9Buky5PLb7aAmLpxG-c9SYv4a7Fuba2ip_iw0i--QTVgzsr0JsBhEY1SCsvRZPJ2Lzuf6_yMMyqtKiML4BQ40n8seNyxRNjOd_mIySo2jih_maHjRNK_Zrv0jBNgpkla1zlpU90V5VVeAEKeXWy3lUzVga30-ehHk1fQ5PeBYZruBRh52pTbyZO8aHYJu5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
میعاد قاسمی، آنالیزور و دستیار تارتار تو گل گهر سیرجان به عنوان آنالیزور جدید پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135484" target="_blank">📅 13:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135483">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❗️
❗️
باشگاه امروز به شکل رسمی نامه زد تا پورعلی گنجی، عالیشاه و سرلک در این تمرین شرکت نکنند!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/135483" target="_blank">📅 13:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135482">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nO-IrMqf8gQ5PUoumFQ6bStP96piY_0hjoz3iw6FOI5sHsT84se4ZSsv8A8Ro2EiSrD64r0ZIR0yuvxM_tvNKGd7hOPiK4YfXJ9eDXcxcmcxN_f3uTWv5kcfUx6ojUpSZUmNnHlV7qny-FDA8w_1AIG8-M60MCSW1chC5bYWUxUlbfjaPS4_8nNfNfe55Imq9ajYum_LWhcFgD6k9Q6xxTp0pCzhCIuH-KKo2rSema9T7M4a4iTieHVCgZnnzQpWX_WXe7P1x1wITFJTfoIB9FhVs_UTaTeIrBBf-xEeR4X5do_dXzq47XUF4wYQiBYofburS82FzAk8fk82ga0jcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تمرین امروز سرخپوشان در سالن وزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/135482" target="_blank">📅 13:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135481">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
🔴
علیرضا بیرانوند در پایان شهریور 1405 یعنی حدود 2 ماه دیگر سرباز است و دیگر مجوز بازی در لیگ برتر را ندارد؛ مگر اینکه راهی یک تیم نظامی شود.
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/135481" target="_blank">📅 13:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135480">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
مجتبی فخریان بصورت قرضی راهی گلگهر شد تا پوریا پورعلی بصورت رایگان به پرسپولیس بپیوندد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/135480" target="_blank">📅 13:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135479">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
فووووووووووووووووووری
📊
محمدمهدی زارع در تلاش است تا رضایت نامه اش را برای پیوستن به پرسپولیس بگیرد /فرهیخگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/135479" target="_blank">📅 11:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135478">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
فوووووری / ایسنا
🔴
پیشنهاد پرسپولیس به اسلامی و کوشکی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135478" target="_blank">📅 11:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135477">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
📊
علیرضا کوشکی وینگر استقلال تهران در لیست خرید پرسپولیس نیست/تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135477" target="_blank">📅 11:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135476">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxjU944p3MkoXlqJGuGA4B1jUabgN84ruOTcTlsM7qNKTPeN8u1Wm5j6kWeixTFKZI0rQfqDWR4STk-BA8VWBynVD0PegYibGJZziPBcdo7My2g_Cq_4NMT3GxFWtbYLmkaG1JLsOH-XHz6jywv7vJW-ZaLzfVvrrSImuPNKGC_zISg3U-w9YCTMDQgBlV-XxgWtvygTg7PZdvU4BK3h0zxpoIf7uTpFzLqvQsnrO16SODwPIdq75B49TTQPqoZ2Yo7ws2RJNII5e4rP9O5MR2zBd6j4WQivzSOspNnptEkhdK2p-HJ3gMtyKXcW4Oc3vAU7xaO8j9TSFHbiCahiUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
مراسم رونمایی از مهدی تارتار امشب ساعت ۲۱.۰۰ برگزار خواهد شد و از شبکه اینترنتی باشگاه پخش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135476" target="_blank">📅 11:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135475">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
پرسپولیس میخواد برای جذب احمد نور به کلبا نامه بزنه/فوتبال 360
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/135475" target="_blank">📅 11:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135474">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">💢
مدیران باشگاه‌ موفق شدند با محمد مهدی زارع به توافق شخصی برسند و قرار است مذاکرات با باشگاه اخمت گروژونی انجام شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/135474" target="_blank">📅 10:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135473">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
✅
پرسپولیس برای برگزاری اردو پیش فصل جمعه هفته آینده به مدت یک هفته تا ده روز راهی ترکیه خواهد شد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/135473" target="_blank">📅 10:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135472">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
فرهیختگان: تارتار درمورد این تصمیم خواهد گرفت که آیا وحید امیری در پست مربی در جمع پرسپولیسی ها خواهد بود یا به عنوان بازیکن؛ چرا که هم وحید امیری با تجربه است هم چند پسته است هم از آمادگی بدنی خوبی برخوردار است و ممکن است به عنوان بازیکن به پرسپولیس اضافه…</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135472" target="_blank">📅 10:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135471">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
پرسپولیس؟باز هم نه؛ترابی بازیکن آزاد نیست!
🔴
فرهیختگان: در شرایطی که در روزهای اخیر اخباری منتشر شده که مهدی ترابی بازیکن آزاد است تا دوباره جنجال‌های بازگشتش به پرسپولیس برای چند فصل متوالی تکرار شود، براساس شنیده‌های «فرهیختگان» او یک فصل دیگر با تراکتور…</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135471" target="_blank">📅 09:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135470">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFDZNhajNyTgtICZd9bwhUaGdncZ01Gx5Wd2q7htPiQXuhSsYyTg0-KkYtbGJZDIWpF6cLoM9rRuFol4eB0hl3OOlWrxzUVJDr3DpA9XQ6SJ6wWOVJyLpo5FOLfqSscYgTanLixXy2MX49RAcAIv7eZBOUwBea4XQiXmUKIhv_wG_upRDnSUOZiYn1SBCKq9Fg0Cmv_5oA0aCHlArAaIxnkhuueciCPZaQ0RimFQSkvqU7Y3TpC-3V3hxqV7XYg0x8oMNmDcUgGplyltmUCfhX5jOGSxB6Kj4-SdEBZHcSfH6eTlGemNljtf6QWnzILZZIXN2tqaCz8SqdubO730Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه پرسپولیس به میلاد محمدی ۴۸ ساعت فرصت داده که برای تمدید قراردادش به باشگاه مراجعه کند در غیر اینصورت باشگاه تصمیم دیگری خواهد گرفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135470" target="_blank">📅 09:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135469">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔹
🔹
🔹
شایعات؛ اورونوف فردا میاد ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135469" target="_blank">📅 09:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135468">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
✅
ترانسفرمارکت ترابی را بازیکن آزاد اعلام کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135468" target="_blank">📅 09:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135467">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
پرسپولیس می‌خواد برای عالیشاه مراسم خداحافظی بگیره؛ حالا باید دید خودش این خداحافظی رو قبول می‌کنه یا نه.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/135467" target="_blank">📅 08:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135466">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔘
🔘
به‌عنوان طرفدار پرسپولیس، تنها می‌توانیم بگوییم: مرسی امید، ممنون آقای عالیشاه!
🔘
🔘
تشکر بابت تمام دویدن‌ها، عرق ریختن‌ها، جام‌ها و جنگیدن‌ها، اشک‌ها و لبخندها و تمام خاطرات ریز و درشتی که با تعصب و غیرت، با شهامت و شجاعت برای خودت و ما ساختی. سهم تو در سال‌های…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/135466" target="_blank">📅 08:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135465">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hki-mo1aFSe0qTtwdd7F-B16Ez-x48KktYMFCab2OFBTAyFTW5EK1Io7mEwddQmyoWrwktYw3QEnj_RabErdNZ1rwusWR5W78PGt2K2-6cloKJUJRBAPHhxi0sQNZGVmlane7f4wRvBDeQVJnmhuJWk2ytCLjfbRldrpVK1tS9pNW0zA9Hk3qDJp-uQxyx7gb3DVy8C4uOQejkg3ioZMrPOanMEFuPM84P5_cM3HH7FDSHERiQPqXSAQgy0LDHXuPt8D-z60JQGmOFL9nM21wRLvZsnBFKxLeFS0tCrHfFasPOPJFUMh-SezcC_q9oiNySHGE-ERCKqnEKm9EOa8GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
صبحتون بخیر ارتش سرخ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/135465" target="_blank">📅 08:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135464">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135464" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر پنجشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135464" target="_blank">📅 02:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135463">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4_oa7GVbWrFiIAGv0LJ5kzJRScKpBozYCNdqg4bEqfNwO-alFA_Gjiq5MPOIreveBqjgRx5F1p8Uq_6-OoaLgNfVE147a3uuExCEyPnrvB0SJaRL90CJMLYU0lJFG_EzMCLMj1V0_KJJ5nBssJhEqHr3j-fXh3204kMi0Wqgax3dHDVIOd4428FzpUPokTNYI9edN1d0oC5V5H0jSXxnidMnQ0ArOLV2LO_4-jOp2rxxCEku2zy0-VsTRxfaLv4rgtBMpevicQr_WHfpAl3CUo598bDKcO5M1lbr7lRw4N_WARCbp6YpdCGndEAHKUJ5JL2_QPH8PohqAm0Fdbl-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《 لینک سایت برای کاربران ایرانی》
👍
《 دانلود اپلیکیشن اندروید》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
Ⓜ️
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/135463" target="_blank">📅 02:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135462">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
🇳🇿
محمدرضا احمدی به عنوان گزارشگر دیدار ایران و نیوزلند انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/135462" target="_blank">📅 01:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135461">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhIf6wgr4-IqTANS0EiS6CM1PWPRaVVcCaIyWaNXyxkkEstG8td6BNoYcV0FBDrrHg6Izh1FrkULu87dz8qvuS0uUit8NUErPMG1JnBK9GxUn_8PrAPpJGfGfcCcFtXobF7qN4Mj-9b6_QpIFd3UTFOJHuaotkEsh2Dl14qGFrxXoytDXWD_noXH09YyEamQ9TQukMv2qYAPApaw7-mWBg04Q2VIOB4zHh0PJyh3WgQhJT5b2oGWVyAytuXQH01DRcb624xPaP_QxeMprpwsQdWboqTBdzLzltaR0kQFz0_jNTfXyp3HJpRzqQgec-qKIaMh_SGk5VelnM8AvEJ3dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
میلاد محمدی هم با اعلام ترانسفرمارکت بازیکن آزاد اعلام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/135461" target="_blank">📅 01:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135460">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">💢
#شایعات
🔴
میلاد سرلک با عقدی یکساله به فولاد خوزستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/135460" target="_blank">📅 01:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135459">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
بعد از منیر حالا اندونگ هم رسماً از استقلال جدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/SorkhTimes/135459" target="_blank">📅 00:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135458">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/135458" target="_blank">📅 00:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135457">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5LQFYYekhnctpU99sVatgbZl_uQ58M4Gd57d5hGgwVnXxFmzh5_wLPMyQz__SR0RMr3v_9oFVZoVCV6oV_SYSxJatRp3J54He_tOL9yAFRuHlyDEBFNk1AmG12LMDw0wOUR9Q4h5o6FHj1jPXtiJCgtRJhQP5NDys6rlm9NrmwWdILLxMi95QQ3tx3OfgtlFP_QNjmMT882hH-aBi2sLmR7M6GYv_uGeIeIEaPW0Q7jUafHucjAIjZQXEvsjX0FoLLbKjvVxjcp1swJNtR7NinvGCNxMkBBDZmsXfs64rHi6y7uwPNwmP_ou_8jOFAF0HSRMP1pdKQdVPL6SVTHWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوررررریییی با اعلام ترانسفر مارکت علی علیپور از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/135457" target="_blank">📅 00:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135455">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D87qTw8SDbCW4gVBtpSlzv5Jk0mBngTja_OrS4OyUVVw-r2c8YtEKf0blTrYEX-XkYXXdJ8_m73nmL2wgBPRpJEbb1BvdmuFhYG4EfWRlL4IcAMQ7EEiNXTNN64ylmktF5VDmXQtvJxumG-UH7TWqA7ecCP6OdaOBloJ2sIPpUTB-9TPrCOAuOdwQAx5xs3OeoilvZRHtR4Cqkw4kzqmxHG4NPdN392jjIWVUx_Q1eDAjHG1ugmwGxMQg5MoGwjBDv9fPe8n61qTpA6rQ1uKHmGW9FA3u8lNO6v8b2JALXXS0AuKAsWTXOdC7GwM8bGBvpURKUgpdQ1oh3IexdrTuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بترس پرسپولیسی؛ رضا اسدی از گل‌گهر جدا شد!
😐
پ.ن نیاد جای علیپور صلوات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/135455" target="_blank">📅 23:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135454">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
فوررررریییی با اعلام ترانسفر مارکت علی علیپور از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/135454" target="_blank">📅 23:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135452">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjdTMIE63oWXUfy9r4Xc18zIDLZiM0qxte5jt1REhnY_HCLQOcrcb3wcASRw2-UR0vtVwXLicswldeAemblz88qisV9ZK5qMBNbrg8x63KzISwHAx4eiRxTjP2lT_C1SHObFyIwk-k1cwCXcdAIJIUOwsnncEnColTtnaRICzB2sF8lCvDNLnevq_x1Ztjg-eWYIOC2VtqcSMvFpRQg-tm-n1-r688GAxk0zqBikK55-Hd2XOqtnmPkn2y1jmoJ-KxGr-gKE_1dMzlSucwYvfDfFfcBQ_esbpjAOQBz5Og1KcvvQ39RqFh3wKXBIbFei8xxZJEkPzCQnIPpPozQ4jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوررررریییی با اعلام ترانسفر مارکت علی علیپور از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/135452" target="_blank">📅 23:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135451">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🚨
خرید پنجم پرسپولیس نهایی شد
🚨
با اعلام سید مهدی رحمتی سرمربی گل گهر سیرجان پویا پورعلی از این تیم جدا شده و فصل آینده در این تیم نخواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/135451" target="_blank">📅 23:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135450">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🚨
خرید پنجم پرسپولیس نهایی شد
🚨
با اعلام سید مهدی رحمتی سرمربی گل گهر سیرجان پویا پورعلی از این تیم جدا شده و فصل آینده در این تیم نخواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/135450" target="_blank">📅 23:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135449">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
اسپانیا گل اول و به بلژیک زده و اسپانیا همچنان تو کل این جام جهانی گلی نخورده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/135449" target="_blank">📅 23:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135448">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❗️
برنامه کامل مرحله ¼نهایی جام‌جهانی
😀
فرانسه
🆚
مراکش
😀
🗓
پنجشنبه ۱۸ تیر ساعت 23:30
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
😀
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
😀
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/135448" target="_blank">📅 23:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135447">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCtrGmaTvJJP59hxSiH26vM8AmywdOaa6iX7qwG4u_Tmqqei8FtspEXIYdTp9PGGuK_A7sBdi5SNNnGmgtcIYfwB9EaYZXlY6JD4mFnoG6fsJlN9j8IPSZPEHippQ9LTJpuypWQOC_2s3O6lxQdmxwdM1JZOPdKKzg5qMjJ8VuJ5F9gEBYBI9Uko1Hz4GKp1h62j2s3S_2738KvWfxFE1ax0PcEGTQkQwsrcCe1jOtK3toLpocKjQ8y0B8nbkzOgJ6KMrcNmCCXhQa_5qOi_gOnsDhknsp5saYCd3kaSfu1A8Pav8ZlXyKLw2o1GVs32L8j9SSJN7YVV2ymakQFFiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مازیار حسینی در راه هیئت‌مدیره پرسپولیس؟
❌
شنیده می‌شود مازیار حسینی، که سابقه مدیریت در شهرداری تهران و بنیاد مستضعفان را دارد یکی از گزینه‌های ورود به هیئت‌مدیره پرسپولیس است و حتی ممکن است رئیس هیئت‌مدیره پرسپولیس شود.البته فعلا چیزی قطعی نشده و در حد گملنه زنی است/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/135447" target="_blank">📅 23:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135446">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❗️
قبل از آمدن تارتار با پرسپولیس بسته بودم،خوشحالی تیکدری، پسر حاج‌مهدی، از انتخاب او به عنوان سرمربی سرخ‌ها!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135446" target="_blank">📅 22:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135445">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
تمام ملی پوشان بعد از جام جهانی و مرخصی از فردا باید خودشون و به کادر فنی جدید معرفی کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/135445" target="_blank">📅 22:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135444">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
اگر اتفاق خاصی رخ ندهد و پیشنهاد بالاتری نرسد؛ دانیال ایری مدافع ملی پوش نساجی مازندران به پرسپولیس خواهد پیوست
🚨
🚨
توافقات نهایی شد و میلغ رضایت نامه مورد قبول هیات مدیره قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/135444" target="_blank">📅 22:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135443">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyAKVfeRGa37PVWMIbSnc1SKnYnklVf__V0e7DN_s-OKh69pVHcEoq85o0h987yzIxyw4vrHb3-gaJyatCQ0o2QnTL_bRRxZ-rSaDRXW1iTnocCgWOvs9ZxyknAHvV09GiWrdp1ZkL464GEQkzC4M4nFfLb8eSqOCLEAj5D2J4qpemL9ZFSHvOu4dtd7gPDLkI7qg6L-qs26NOLjcmcGU2SFjxv8PA_7sbX8chtBkfl7-MXIb0hH0vOAqwDOPVP-ePF68FHynPXWY8ObmPxGpHNHsT34nfjvMQ7saoabqURE2xb4JYDZNkD1hDO6kXpYf8uTQtGfraUNmZAyK4wVWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یا گو، مربی یونانی تیم، در تمرین امروز پرسپولیس شرکت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/135443" target="_blank">📅 22:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135442">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
فرهیختگان: تارتار درمورد این تصمیم خواهد گرفت که آیا وحید امیری در پست مربی در جمع پرسپولیسی ها خواهد بود یا به عنوان بازیکن؛ چرا که هم وحید امیری با تجربه است هم چند پسته است هم از آمادگی بدنی خوبی برخوردار است و ممکن است به عنوان بازیکن به پرسپولیس اضافه…</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/135442" target="_blank">📅 22:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135441">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
❗️
مهدی تارتار از آمادگی وحید امیری در تمرینات رضایت داشته. احتمالا وحید امیری برای فصل بعد به عنوان ی بازیکن تعویضی و برای مدیریت رختکن و...دوباره به پرسپولیس برگرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/135441" target="_blank">📅 22:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135440">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b6deee68.mp4?token=jKnQAzSAjDHA3Pfzf11slOLIU3moNYE6UiM2tWxKml1mBKKzS2QhQAaTp8B1RJTo_c6-2DqwcWuKb4CqFmfQbghBK2SqIkuppi2bhJpnHpxHlpkDChXmTJsf_tYEQxEvT1z-MTw4MoFI4PSwwMjFr_qpOxTvhRfwQGOhlly6-Y5x8TKz3_QGFoLWivxQX3DAFbnRPF-KrLq8JSuIKuj6oWA8ZU-4DJECZcnuYYVTvPq5Du_l0hmVQNaldxRNJL1Fp9MOtjMWv96V6-KNq7vw1b5g91Q4s0wSw2VDK3NqWvz5G59z7TvkcvPawbeJtYPuazVgDNhiCFytpSuad8YkRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b6deee68.mp4?token=jKnQAzSAjDHA3Pfzf11slOLIU3moNYE6UiM2tWxKml1mBKKzS2QhQAaTp8B1RJTo_c6-2DqwcWuKb4CqFmfQbghBK2SqIkuppi2bhJpnHpxHlpkDChXmTJsf_tYEQxEvT1z-MTw4MoFI4PSwwMjFr_qpOxTvhRfwQGOhlly6-Y5x8TKz3_QGFoLWivxQX3DAFbnRPF-KrLq8JSuIKuj6oWA8ZU-4DJECZcnuYYVTvPq5Du_l0hmVQNaldxRNJL1Fp9MOtjMWv96V6-KNq7vw1b5g91Q4s0wSw2VDK3NqWvz5G59z7TvkcvPawbeJtYPuazVgDNhiCFytpSuad8YkRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
قبل از آمدن تارتار با پرسپولیس بسته بودم،خوشحالی تیکدری، پسر حاج‌مهدی، از انتخاب او به عنوان سرمربی سرخ‌ها!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135440" target="_blank">📅 22:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135439">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8efabe672d.mp4?token=TTfex3yVuyfVqjOPzSpUsruc2--yxmW7hQF19M5-S_Oj5iZFbhiayLDQm1873yPONdyA0ufYpMbYtS7K412hSXquS5NXt_PHRkz8IzFuxTPlFLBa2iFX_dNDUpn3Opa2ZS8vkt6tpN3_YdIPscTMMWy27nnKM_diZ_5FcMPONWlVClIYnrgUv1zM4-4y3Pp8uvdkwKv7pOljTQVeswEJsPPFmtMafMkMNdPoUYWUdLV4NZCc8Kbz74qpvETE2-vv9AwLIDZEKVy8LZ4qPeByCsqqJdkGOoaIxpMypzoO6BBbWp2Ky9LPzr_4yeGTPHiKv_sGDJsHlnvlty6QUWOtUoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8efabe672d.mp4?token=TTfex3yVuyfVqjOPzSpUsruc2--yxmW7hQF19M5-S_Oj5iZFbhiayLDQm1873yPONdyA0ufYpMbYtS7K412hSXquS5NXt_PHRkz8IzFuxTPlFLBa2iFX_dNDUpn3Opa2ZS8vkt6tpN3_YdIPscTMMWy27nnKM_diZ_5FcMPONWlVClIYnrgUv1zM4-4y3Pp8uvdkwKv7pOljTQVeswEJsPPFmtMafMkMNdPoUYWUdLV4NZCc8Kbz74qpvETE2-vv9AwLIDZEKVy8LZ4qPeByCsqqJdkGOoaIxpMypzoO6BBbWp2Ky9LPzr_4yeGTPHiKv_sGDJsHlnvlty6QUWOtUoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
قسمت بود به استقلال نروم
🔴
روایت مهدی تیکدری از منتفی‌شدن انتقال ۲ سال قبلش به استقلال؛ آماده شده بودم که دیگر هیچ‌وقت نتوانم برای تیم محبوبم بازی کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135439" target="_blank">📅 22:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135438">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» مدیران باشگاه پرسپولیس با نظر مهدی تارتار با این چهار بازیکن وارد مذاکره شدند.
⬅️
مجید عیدی
⬅️
محمد قیرشی
⬅️
پوریا پورعلی
⬅️
پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135438" target="_blank">📅 22:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135437">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135437" target="_blank">📅 22:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135436">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMVBQvxZt8mXRVNopoDMKY0fiIO4iuI52b_fku1sRkmb2bYUVwVVyxXUt6KoC1MjR5mUgT-kkIa75UriZQcW5XR_XK9uc84c_KlQuvjmULB9TJACDvWh6-i0oZ8oCGW8hW8p4HJDfTJQZ7oZqDlNsYOdqtiXtpBf3Gt9wGLWDPsUkex9UnrcW2JtU3BXJpBFBX0lyqCIBzwk1MTKrKScjX5SfIZmZfLUBs7kG_VHmgf8-g0c5yBKjxBduwK6kAdU5HmEvy7yzRC3qA2Y_JtixTp2_S56ImcRZ0xGPP3cH96jjf1W8M-Ax28gR3dSfsxCghBASZT9UL7LFu4dX19l5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گزارش تصویری از تمرین امروز پرسپولیس و اولین حضور ابوالفضل جلالی در تمرینات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135436" target="_blank">📅 22:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135435">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
❗️
احتمال همکاری امیری با پرسپولیس برای فصل بعد چه به عنوان بازیکن و چه به عنوان عضو کادرفنی بالاست/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/135435" target="_blank">📅 22:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135434">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بزرگترین کانال پیشبینی فوتبال در ایران
🔥
فرم های بزرگ ترین جام جهانی رو از دست ندید...
⚽️
@Tabanii_Mafia
@Tabanii_Mafia
⚽️
@Tabanii_Mafia
@Tabanii_Mafia</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135434" target="_blank">📅 21:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135433">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iS0eS_Ff45z5IpTxIT4tct3Z6-dDF3nMIy8xo0jyRB3qL2Be8A0UBfzEbbVIKfzleEdWhq_3Pk7F69Bh-KX4avLk8wCDKOFtxlTaHWiRpI1jhfzLazh9WyT1cq5YNtvJwgP4klQ3-83dYYgi40kMyuq_HC0OImyd-0fWHWpUwuLP04u0oTf3spm0Q_c8lc8xPsho9yaCSr4i3jVYncH5WetxwrkmL1CWN4FR0yZHWS0T6GI7IThHBOvePQl0DZn7QcKOiBSJN7aBDS0tlKDxK0q35H92PZfYTNc1x6xcwDju7ng2NfuLV3EO-3eU6m8G7UDbksYSVQGMchZfSaYOpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تک آپشن عالی برد شد
❤️
✅
✈️
@Tabanii_Mafia</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135433" target="_blank">📅 21:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135432">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
❗️
قدوسی: تارتار خواهان حفظ هر دو مهاجم خودش شده اما خلیلی و حدادی به او اطلاع داده اند برای صرفه‌جویی بودجه باید یکی در تیم بماند و یکی جدا شود.........!
❌
❌
تارتار علیپور را انتخاب کرده و اگر علیپور تمدید کند باشگاه با سرگیف توافقی فسخ خواهد کرد
😐
😐
😐
😐
😐
…</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135432" target="_blank">📅 21:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135431">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
امروز جلسه‌ای بین کریم باقری و باشگاه پرسپولیس برگزار خواهد شد در مورد شرایط ادامه همکاری با یک‌دیگر گفت‌گو کنند/تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/135431" target="_blank">📅 21:03 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
