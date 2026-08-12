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
<img src="https://cdn4.telesco.pe/file/VbFKqv_IfLOja11Z5_AjvY2IGg7hQHMPWiEkSyC-nGPWj9oJwIEiF5sYQGYQK5cgp7VrhHS7jCcVs_JpBWq96bn9RJaOKnBlaEh_2PH7Iyne-SR9TsCDW3cj6DeEMEnbYoA9UnkojlrkkerZ5OhjzIVgR2Gdwe3ZEK3eEGdOsK3zDkOlBAhIPbXeUjcndGoEPA9vucHv36W5miwkrJXiiJ3V5K6El1YXtxgH975gDoAwXVeX8BxcOe3q-G_ad_kkGsTZIynAi0_6ys22jYwuQpkjl2er6j7yoeLJB-CyK0H_IDzBO8J1lstJv5U49FTo13WqXXaYGqkimL-pAJbqIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 21:44:00</div>
<hr>

<div class="tg-post" id="msg-137899">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0cYMXDWHGmiCX8EoHTOOSpGByAlaCn57A1fmRj_dxFzITpIdc2rLDIs-4klk17zAXmItd4YO5PLtdyM_Aw3pl__WJ4QNtOpQEJOkZZkj81SAow0u5G9Y4s-kXeemvIjNvi22BrK8H3M8kl8RzcMmoVdjXSdybEg34Xm3GWZHrz3r5FzN1otTc0TMMXCXctpU0iL0quaoVSnQyIvSyc9fdtn1stxGvC9urg71pDk4-ss6_b-Y1pqLGEic66VMEmpBIgC2HPmQ_bnggxhqtIeqX083xNqXSRS63_u5P9P0TYtS8DcSZu6My8AsySEqfXmjePTwZepICgjXky1xqg90g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇪🇺
شطرنج پاریس و استون؛ فقط یک برنده!
یکی برای تحمیل قدرت می‌آید، دیگری برای شکار لحظه‌ها؛ ۹۰ دقیقه کافی‌ست تا یکی رویایش را به واقعیت تبدیل کند.
🏆
فینال سوپرکاپ اروپا
[
پاری‌سن‌ژرمن
⚽️
🆚
⚽️
استون‌ویلا
]
⏰
چهارشنبه ساعت ۲۲:۳۰
🏟
استادیوم ردبول آرنا
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/137899" target="_blank">📅 21:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137898">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووری
❌
محمد قربانی سورپرایز مدیران باشگاه پرسپولیس بعنوان آخرین خرید در بازار نقل و انتقالات خواهد بود
▫️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/137898" target="_blank">📅 20:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137897">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
❌
محمد جواد حسین نژاد دقایقی قبل ضمن تشکر از باشگاه پرسپولیس آفر این تیم رو ردکرد و به‌پیمان‌حدادی مدیرعامل‌سرخپوشان اعلام کرده که فعلا قصد نداره به لیگ برتر ایران برگرده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/137897" target="_blank">📅 20:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137896">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
❌
طاهرخانی
🗣
🗣
محمد قربانی در نزدیک ترین حالت ممکن به پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/137896" target="_blank">📅 19:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137895">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
✔️
ادعای آناتولی به نقل از منابع پاکستانی:
❌
آمریکا و ایران با تمدید ۶۰ روزه آتش‌بس بر اساس یادداشت تفاهم، موافقت کرده‌اند؛ طرفین در حال تبادل پیام هستند تا درباره مدت زمان تمدید، تصمیم‌گیری کنند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/137895" target="_blank">📅 19:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137894">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
❌
طاهرخانی
🗣
🗣
محمد قربانی در نزدیک ترین حالت ممکن به پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/137894" target="_blank">📅 19:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137893">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔄
🔄
😳
😳
😳
😳
محمد قربانی به پرسپولیس پیوست/ پنبه کار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/137893" target="_blank">📅 19:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137892">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
مهدی تارتار هفته گذشته یک دفاع چپ خارجی به باشگاه معرفی کرد و اعلام کرد قرارداد بیفوما و گرا فسخ بشه اما مدیران باشگاه پرسپولیس به این نتیجه رسیدن هم بیفوما و هم گرا بمونن
👀
‼️
📰
قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/137892" target="_blank">📅 19:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137891">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
❌
طاهرخانی
🗣
🗣
محمد قربانی در نزدیک ترین حالت ممکن به پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/137891" target="_blank">📅 18:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137890">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
❌
طاهرخانی
🗣
🗣
محمد قربانی در نزدیک ترین حالت ممکن به پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/137890" target="_blank">📅 18:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137888">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
گفته میشه که کوروش اژدهاکش بازیکن جدیدمون قرضی 1 ساله میره نساجی..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/137888" target="_blank">📅 18:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137887">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
سازمان لیگ به استقلال گفته کارت بازی آسانی رو صادر می‌کنیم ولی اگه بعدا بازی‌هاتون سه هیچ شد پای خودتونه
🔹
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/137887" target="_blank">📅 17:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137886">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
واکنش مسی به درگذشت پدرش
❌
❌
«بابا، هنوز نمی‌توانم باور کنم که دیگر نیستی، یا بهتر بگویم، نمی‌خواهم باور کنم. تصور اینکه دیگر تو را نمی‌بینم و حرف نمی‌زنیم، خیلی سخت است.»
❌
❌
«همیشه از من می‌خواستی که آخرین جام جهانی‌ام را بازی کنم. چند روز مانده به شروع…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/137886" target="_blank">📅 17:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137885">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
‏ مسی در مراسم ختم پدرش
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes ‎</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/137885" target="_blank">📅 17:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137884">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
📰
باراک راوید، خبرنگار آکسیوس: توافق ایران با عمان و امریکا نهایی شده و فقط شورای عالی امنیت ملی ایران باید اون رو تصویب کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/137884" target="_blank">📅 16:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137883">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEDuLeNL9cZ2zCksCE5dFlO7jbcgTeRiIQfBl86kJnpuWH9fh5D8uBcGeZtWxRymmGKeWZ0-pS8S0Y9yrz6mqRvxy92QXbXavyaJV_UbyBO3arCS3mjLaMLOX1umNHHezxXhQPRMZh4agkTaIc41K8EGWXVYoocM3UP91NJRjN_I3CiCy-WiwubZ4JPsJ-mCYuvlewD0dGz3GNX7V6AdJ5l5cOd7B0QCKaWAWhffHSoEX8fmmiYcN76yBrsB3mNUhJxMATgRu2ss8-cx-gKahqkTYQzMqQocrRmLCWxT2rdo_ZCQeGjOidGpc_R6rnjPS6FimnBodD5wRJygv-_GzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
صدای ماندگار موسیقی ایران خاموش شد
✔️
حسین خواجه‌امیری، خواننده نامدار موسیقی ایرانی که با نام هنری ایرج شناخته می‌شد، ساعتی قبل در سن ۹۴ سالگی درگذشت.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/137883" target="_blank">📅 16:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137882">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
تارتار رسما اعلام کرده به هر چهار مدافع تیمش نیاز داره و اجازه جدا شدن به حسین رو نداده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/137882" target="_blank">📅 15:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137881">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🤝
🤝
🤝
قربانی رو بیار و بهترین پنجره تابستونی تاریخ رو به نام خودت ثبت کن دکتر پیمان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/137881" target="_blank">📅 15:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137880">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
رسانه های ورزشی آذربایجان هم در حال پوشش خبری پیوستن قربانی به پرسپولیس هستند‌.....  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/137880" target="_blank">📅 15:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137879">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
تلاش باشگاه پرسپولیس برای جذب قربانی ادامه دارد و به نتایج مثبتی هم رسیده و اگر اتفاق خاصی رخ ندهد، او به زودی به پرسپولیس ملحق خواهد شد / ورزش سه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/137879" target="_blank">📅 15:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137878">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
تسنیم: قرارداد دانیال ایری با پرسپولیس پنج ساله بسته شد و مبلغ رضایت‌نامه این بازیکن 2,5 میلیون دلار ثبت شد که پرسپولیس بتونه بعدا ازش درآمدزایی بکنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/137878" target="_blank">📅 15:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137877">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
#فووووووووووووری
🚨
خرید بعدی پرسپولیس مشخص شد
💣
💥
⏺
طبق اعلام منابع خبری نزدیک به باشگاه پرسپولیس، مدیران باشگاه پرسپولیس که پس از نهایی کردن قرارداد دانیال ایری به سراغ جذب محمد قربانی رفته اند با باشگاه الوحده به توافق رسیدند
⏺
حالا باشگاه پرسپولیس در…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/137877" target="_blank">📅 15:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137876">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
tik tak...  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/137876" target="_blank">📅 15:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137874">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cwy6-zLAnlRvg0HXJw1R0ZvUI_dnxxdVpP5ORX8U8lxycDbwDRteIvrITFS-Ttods7aqJwst2wMn_3kX1q1qOSfhMz63ACsklZSTHZW3R8A1zQCcnXeWBeW7JZlhejtnAcqjPHOcv-xDPfgAld9SFJnXQ5CGYTji_9qHPEnN-v-ndQwHK_M8zNvnUa76IWnAAh7T43OxkUsEOvPkQFNu7GMUG2xUCCa8yilorikCWnpyLcQI7OvdOUr3d4R9twU_xTrFOHiRHGmh1D3rQxFCNCTnVWfN9L5Cz4zwNxNhhCV-AHHR0u8Eg9zIUTBF4DeBu4BxfEO0TOT7fMp6gZ-ZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوریا شهرآبادی تو بازی‌های پیش‌فصل 8 تا گل زده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/137874" target="_blank">📅 15:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137873">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR6YQQUszBBSic2Sqm94uYmLJbilsb-u4nwxdwZTOxSBUx1D-CjQtAUT00N_z7ZPGCoHXPVw_7HTFSpliHrpsOI8dYUUsyNUWHXnsW8Oy0G-Tiso1bFEHp1JzPcoqnXaCsKn9z88yvqgh9aIBVRCTSlqd5On8HpJ8kMU6eOQrs-UWj8fOCJhrhBIY3l0aN_dRmclqOoY6-lVbZbVMIhSZB1vP6-03VrAlkkKhZD2ycvoCvp-NyIUhflIEfpf9xpjq5znSZCmLZWkWkMZdI6ARjkH5adT5bnL1myU1c3xdPQnC4OpK5Z9uA6SMnfIobHGcLMV9L7krI24pOXG57S9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پاریس در مسیر فتح یک جام دیگر!
🔵
PSG -
🔵
AstonVilla
⏰
ToNight 22:30
🏟
Red Bull Arena
پی‌اس‌جی با موج حملاتش می‌آید تا از همان ابتدا نبض بازی را در دست بگیرد، اما استون‌ویلا تیمی نیست که عقب بنشیند، ضدحملاتش می‌تواند هر لحظه معادله را برهم بزند. یک طرف قدرت پاریس، یک طرف جاه‌طلبی ویلا؛ نبردی که می‌تواند تا سوت آخر نفس‌گیر بماند.
🎁
بونوس ویژه اولین شارژ:
فقط با یک پیش‌بینی، می‌تونی ۱۰٪ بونوس خوش‌آمدگویی رو به موجودی اصلی حسابت اضافه کنی.
📌
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و پیش‌بینی خودتو ثبت کن:
👇
🟣
[
برای ورود به سایت کلیک کنید:
]
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/137873" target="_blank">📅 14:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137872">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
شهاب زاهدی: بجز سردار آزمون و مهدی طارمی اونم با اختلاف خیلی کم هیچ مهاجمی رو بالاتر از خودم تو ایران نمیبینم
😀
😀
😀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/137872" target="_blank">📅 13:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137871">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
فوری : رامین رضاییان با قراردادی ۱+۱ ساله به فولاد خوزستان پیوست.
✍️
خبرگزاری فوتبالی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/137871" target="_blank">📅 13:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137870">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
❌
بند فسخی که پرسپولیس برای ستاره‌های جوونش گذاشته:
🔹
🔹
پوریا لطیفی‌فر: 1.6 میلیون دلار
🔹
🔹
پوریا شهرآبادی: 1.7 میلیون دلار
🔹
🔹
محمد مهدی زارع: 1.8 میلیون دلار
🔹
🔹
دانیال ایری: 2.5 میلیون دلار
😀
مدت قرارداد همه شون 4 و 5 سال هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/137870" target="_blank">📅 13:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137869">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
قدوسی: مدیران باشگاه پرسپولیس به ما گفتن با وجود عنایت زاده، باکیچ، خدابنده لو ، پورعلی و لطیفی فر امکان جذب توأمان هر دو بازیکن (محمد قربانی و محمدجواد حسین نژاد) وجود ندارد و یکیشون جذب میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/137869" target="_blank">📅 12:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137868">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏
✅
️ برنامه مسابقات هفته اول لیگ برتر فوتبال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/137868" target="_blank">📅 12:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137867">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1TQFq2DBX7WRUNhexxb-WmxnfofVe-rRYpUTvi_Lz9mYp1GZbnyarp2NNcx_fEXxm4mgQF1A9nHQqtNYUltYAZLp4si0u5-8pajMwUw3Gz-G4GIJAYG6RxvfwbKqzYAkAo8Ub72z-y1iHgFE1ecj8VmnJsV0VqOoxoI-7yqzlNOnDO-p_Z16XrASuzfF9iXouFQkEkJgcNh_I2LYMfqq0n7pjDIfmTGHBEzhMMbArVh2oCEoLiisyd9wCVnQSs6HXbkKYqAZV2g3M948YxIl__rFhf806Y05MH2SM1-bvOu7u2QXHENBHHzUdYGagakTkIIuovuq-3OxQukBFkVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
✅
️ برنامه مسابقات هفته اول لیگ برتر فوتبال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/137867" target="_blank">📅 12:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137866">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
لباس پرسپولیس عوض می‌شود
⚡️
⚡️
باشگاه پرسپولیس برای فصل جدید رقابت‌های فوتبال، در آستانه تغییر برند تولیدکننده البسه خود قرار دارد.
⚡️
⚡️
⚡️
برند «یوسف جامه» در فرایند مربوط به انتخاب تولیدکننده البسه باشگاه پرسپولیس، توانسته نظر کمیسیون معاملات باشگاه را جلب…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/137866" target="_blank">📅 12:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137865">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔄
🔄
توافق نهایی پرسپولیس با دانیال ایری و نساجی انجام شد و صبح شنبه از ایری رونمایی میشه
⚪️
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/137865" target="_blank">📅 12:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137864">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/137864" target="_blank">📅 10:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137863">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
شهاب زاهدی: بجز سردار آزمون و مهدی طارمی اونم با اختلاف خیلی کم هیچ مهاجمی رو بالاتر از خودم تو ایران نمیبینم
😀
😀
😀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/137863" target="_blank">📅 10:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137861">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
خرید بعدی پرسپولیس محمد قربانی خواهد بود / ورزش 3
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/137861" target="_blank">📅 10:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137860">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
قربانی آخرین خرید پرسپولیسه/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/137860" target="_blank">📅 10:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137859">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
🆕
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس دانیال ایری با شماره پیراهن ۸۹ برای پرسپولیس به میدان خواهد رفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137859" target="_blank">📅 09:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137858">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
❌
گویاآمادگی پوریا شهرآبادی بیشتر از علیپور و سرگیف بوده است اما برای اینکه فشاری بهش وارد نشود قرار است کم کم وارد ترکیب اصلی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/137858" target="_blank">📅 09:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137857">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
باشگاه پرسپولیس موفق شود محمد قربانی را جذب کند پرونده نقل‌وانتقالاتی خود را خواهد بست و اگر موفق نشود دیگر بازیکنی جذب نخواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/137857" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137856">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
باشگاه پرسپولیس موفق شود محمد قربانی را جذب کند پرونده نقل‌وانتقالاتی خود را خواهد بست و اگر موفق نشود دیگر بازیکنی جذب نخواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/137856" target="_blank">📅 09:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137855">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
محمد قربانی پرسپوليس
‼️
✅
🔴
همچنان چونه زنی بر سر رضایت نامه قربانی ادامه دارد
✅
‼️
🇦🇪
الوحده اول رضایت محمد قربانی را ۶۰۰ هزار دلار اعلام کرد و بعد از اومدن تراکتور به عنوان دیگر مشتری قربانی الوحده رقم رضایت نامه را از ۶۰۰ هزار دلار به یک میلیون دلار افزایش…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/137855" target="_blank">📅 09:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137854">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
❌
پرسپولیس باید ۶٪ مبلغ قرارداد بازیکنارو پرداخت کنه تا کارت بازی‌شون صادر بشه.اگه امروز پرداخت انجام بشه، همه بازیکنای لیست برای بازی با شمس‌آذر مجوز بازی دارن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137854" target="_blank">📅 07:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137853">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJ4e3rnUXqivIXJlX8nYlH7Vt_L82tJnnURZ0QWbYkmxn3mNyCj8rZOpkNp15QNcJNupRvKPkgIs0ZgzZJFfrekEHT_hqluSnhWC8vI2xh1A1eXsd0KuujIScN10HY3P7SDPwY9qfWqBepWha7pmXWbmD66I7a2KTM2ERW3NSYzsYKsY2-4Yg510JfLktYKFN3VkvupdvSnXut5AwGPAquvXIW2xKk0FpWFjZQ36s-q1ndINtnfJauzt8brg2qZ52Hv_JnFdaeMvoJ6rrb7BGjIRy2kcdSkdMH4e4-B6iwkbu2iLlpjT8GlolNOTG71XdM81-0GQxB6nvi0Inn26Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137853" target="_blank">📅 07:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137852">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK7-8r7pKICfPzUl4avWkudFw-3J3MPedLy4cqqqudv3wyOYgQqh63et7uAH4WiXWilnNTdfVMgSoPTtkFZceRZOlf3-nt3ChYZa86FCYevehXOHES2FdaVPRp_5X2jZJPBxRSPctNqDYzmsE-mR7oEkqrEMWL-LcvNizy17B7MNqED3EITjs0IbkwjdpQ7-B5m8wNFTdAutTG81h314Nc7HQ1MgmFvomYyHZTvKz1RDigfpaGWkbOeVHPT8KGiTbXrOxMigXU7gzzkd8E7xfB-qU-eDjC2dc76zGwUjn4vtNkr0Sbb0nndX1x0NCGPG6Lcc71bQLYt4NaAS5a55hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
هر چرخش یک شانس تازه برای برد!
🎰
اسلات با هر اسپین، ترکیبی تازه از نمادها و شانس یک برد هیجان‌انگیز را رقم می‌زند.
از بردهای کوچک تا جک‌پات‌های بزرگ، همه‌چیز در چند ثانیه مشخص می‌شود.
قابلیت‌های ویژه، فری‌اسپین و نمادهای Wild می‌توانند هیجان بازی را بیشتر کنند.
اسپین کن و ببین شانس امروزت چه چیزی برات رو می‌کنه!
🕹
همین حالا وارد دنیای کازینوی وینکوبت شوید و با اولین واریز خود ۱۰٪ واریز بیشتر دریافت کنید. شاید برنده بزرگ بعدی شما باشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/137852" target="_blank">📅 02:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137851">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvXa_FUMb588y0DhupZbifL18fktstUrS3Z5zP555V1kkWlo2vyfWqaz_MG7k837CC6swxuqVX2XsbyWWTHeBkjrjEmVaQ35EXIUr_Epc8b5292GB3C3fWocxUs6rSQq_FJoqooq2jx2mPQMTE_jKuig-eYZYScKkInjGazpNbsglyH0LrthBJfG60LUP5WU2DfY8NYSlQ5a_WOHBnmS6sai_5NOvqrqYyF3OiIec8MnCli-kQBMPRhl-1L0eaWLPbf-UBfHf2Zxq-SpxHVO--dneCZ7hwnc42cv2DL-kaaGGBszCmajcSHvk7BeMbBbdWV_UOpw4G2KieOGEqOvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
شبتون بخیر سرخدلان
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137851" target="_blank">📅 01:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137850">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
یک مقام مسوول باشگاه نیم ساعت قبل به قرمزآنلاین گفت قرار بوده ایری امشب برای امضای قرارداد و برخی امور جانبی به باشگاه بیاید.
❌
اکنون برخی رسانه ها خبر داده اند ایری در باشگاه حضور دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/137850" target="_blank">📅 01:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137849">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
سازمان لیگ به استقلال گفته کارت بازی آسانی رو صادر می‌کنیم ولی اگه بعدا بازی‌هاتون سه هیچ شد پای خودتونه
🔹
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/137849" target="_blank">📅 01:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137848">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
استعلام فیفا درمورد آسانی هنوز به باشگاه استقلال اعلام نشده. و در صورت هرگونه بروز مشکل حقوقی در این پرونده، سازمان لیگ مسئولیتی در قبال صدور کارت بازی آسانی و مستندات آبی‌ها ندارد و همه تبعات و هزینه‌های آن را استقلال برعهده گرفته‌ است / فرهیختگان
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/SorkhTimes/137848" target="_blank">📅 01:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137847">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
عجیب اما واقعی!
✔️
تخلف عجیب و بزرگ سازمان لیگ؛ قرارداد جدید آسانی ثبت شد
‼️
بزرگترین تخلف تاریخ سازمان لیگ فوتبال از بدو تاسیس تا به امروز رخ داد و کارت بازی بازیکنی که قرارداد شو فسخ کرده و از تیمی که پنجره نقل و انتقالاتش بسته ست و امکان ثبت قرارداد…</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/SorkhTimes/137847" target="_blank">📅 01:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137846">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
❌
فوتبال ۳۶۰ : کسری طاهری به سپاهان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/137846" target="_blank">📅 01:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137845">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚫
یه عده میگن یکی از اعضای هیئت مدیره داره سنگ اندازی میکنه، من اطلاعی ندارم اگر صحت داشته باشه و اثبات بشه کونشو پاره میکنیم کاری نداره که…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137845" target="_blank">📅 00:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137844">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a39HOMvHlGd5sJx8Ew4tjfSKbsc7VpdoeCE_sUDnqCrYOHikuByDNdzMRrTKNOEe4xFdZhDu5WSAxmywSXZ86uPn0IBJFIp4Ig8_u28oH1GXPUs4v6kdWqjiW5yD2MpaMoKAxgaiplo8TYKxxSNFoCluJtE7sis4cm4qYk0iZt_wCm1gMydfKakZYekb2TEpt8YVtRhUbn7I8v9iGCwagJ9P9z1pM-BuaN7uLBTKZLoG2uJhfsKOik8z1QFvn3nxPIPqsAJJNGDzjwtaTfsJqmFFAvyBtUPU6Vp4ClTO5eHq-R1ZR7SRZZWKuzP0tp-Jjlk5e0xTaoFYC1yyV1dHZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوووووووری
❌
طرفداری:
❌
❌
محمد قربانی سورپرایز مدیران باشگاه پرسپولیس بعنوان آخرین خرید در بازار نقل و انتقالات خواهد
بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137844" target="_blank">📅 00:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137843">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
🆕
🏅
به گزارش رسانه «سرخ تایمز» و طبق گفته های عضو هیئت مدیره باشگاه پرسپولیس، باشگاه مصر هست تا محمد قربانی رو به خدمت بگیره و خود محمد قربانی هم علاقه منده تا به پرسپولیس بیاد اما مشکل اینجاست باشگاه الوحده داره بازی در میاره و تا الان…</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137843" target="_blank">📅 00:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137842">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
🆕
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس دانیال ایری با شماره پیراهن ۸۹ برای پرسپولیس به میدان خواهد رفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/137842" target="_blank">📅 00:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137841">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
🆕
🏅
به گزارش رسانه «سرخ تایمز» و طبق گفته های عضو هیئت مدیره باشگاه پرسپولیس، باشگاه مصر هست تا محمد قربانی رو به خدمت بگیره و خود محمد قربانی هم علاقه منده تا به پرسپولیس بیاد اما مشکل اینجاست باشگاه الوحده داره بازی در میاره و تا الان جواب نامه باشگاه پرسپولیس رو نداده و مبلغ رضایت نامه رو اعلام نکردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/137841" target="_blank">📅 00:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137840">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
فوووووووووووووووری
❤️
دانیال ایری با عقد‌ قراردادی رسما و شرعا به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/137840" target="_blank">📅 23:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137839">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4tgpuzXX85WsaLHkHw5qoIW79Y26RipjNdFCSdp83VLASUdxHT-_os_Ph906zpIrAQZnEoF8rMWsc3XB4A3947S6_X5ugWeT5eoZfNUOoGefXLOjS30FeyVv6IvgpFpMrpmnSIh7B8WBAvI_LzbpJuRTQjcG2-LL66JtsAWbY_15FOauKBGECcQ5pVV5vr7hBmzU1GcvD5ZwSSP9SwCovo-k2wke7TfiAqMpMH3XE4jPGzki6b2BpUBxy8LaI2W66Njku2IEWKOfz-D6Bn6iRaMoIEfcZNHh1mxcU2k6zRnnC4E7U-jYZIPVjNbCRaYJk-IqCMyNOJNbVGWi1Xk7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
مهدی تارتار هفته گذشته یک دفاع چپ خارجی به باشگاه معرفی کرد و اعلام کرد قرارداد بیفوما و گرا فسخ بشه اما مدیران باشگاه پرسپولیس به این نتیجه رسیدن هم بیفوما و هم گرا بمونن
👀
‼️
📰
قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/SorkhTimes/137839" target="_blank">📅 23:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137837">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
❌
سازمان لیگ 11 و 12 شهریور را برای برگزاری دربی در نظر گرفته و پنجشنبه 12 شهریور گزینه احتمالی است.
❌
با این حال، تاریخ نهایی مربوطه هماهنگی با برنامه تیم امید و مسابقات آسیایی تیم‌های ایرانی خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/137837" target="_blank">📅 23:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137836">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⛔️
میره تراکتور بیخود به دلتون صابون نزنید، ایجنتشم منصور عظیمیه بازیکنشو نمیاره پرسپولیس و در اخر اینکه ما اصلا هافبک دفاعی لازم نداریممممم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/SorkhTimes/137836" target="_blank">📅 23:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137835">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">💢
💢
💢
فووووووووری
💢
آخرین پیشنهاد باشگاه به نساجی
❌
130 میلیارد نقد + اژدهاکش و پویا اسمی ( قرضی)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/137835" target="_blank">📅 23:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137834">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
❌
فوتبال ۳۶۰ : کسری طاهری به سپاهان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/137834" target="_blank">📅 23:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137833">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
❌
فوتبال ۳۶۰ : کسری طاهری به سپاهان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/137833" target="_blank">📅 22:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137832">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
✔️
طبق استعلام دو باشگاه استقلال و پرسپولیس خرید کسری طاهری طبق قانون فیفا پل حساب میشه و هرکدوم از تیما بخرنش باید تا نیم فصل صبر کنن تا کارت بازیش و itc این بازیکن فعال شه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/137832" target="_blank">📅 22:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137831">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
رضا درویش: سرژ اوریه بازیکنی است که بعد انقلاب بازیکنی به این کیفیت به فوتبال ما نیامده است و او سابقه بازی در منچسترسیتی و پاری سن ژرمن را دارد. به زودی مشکل او حل خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/137831" target="_blank">📅 22:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137830">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
باشگاه سپاهان از باشگاه استقلال به دلیل استفاده از بازیکن غیر مجاز ( ماشاریپوف ) در بازی برابر این تیم شکایت کرد و خواستار سه بر صفر شدن آن‌ بازی شد /ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/137830" target="_blank">📅 22:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137829">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
#فوری؛ بعداز حرفای‌ دیشب تاج برای اهدای جام قهرمانی فصل گذشته به باشگاه استقلال؛ مدیران دو باشگاه‌ سپاهان و تراکتور به فدراسیون اعلام کرده اند یک‌ تورنمنت سه‌جانبه برای تعیین قهرمان برگزار کنند. به‌ اینصورت‌که تراکتور - سپاهان به مصاف هم برند و برنده اون‌…</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/137829" target="_blank">📅 22:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137828">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQFfGah_UYoIcMKCHN2Lagiz4-gE8TBNuQceG8lLcC92Gwh6jYdWCA1YoYalQdhtO3kPjOyJzAMlANKkpJZwjaztv4Iz5h_Q2x8HrAgDKPa2Q1anHywSq6ZiL7hGCV0FQpk12kSzEDmGN_4k3pGqA1QP5kV6VYfmUg7LkNWEeidGLYErxbO7DCEOsaWAar5xRL5-w9rlqpPtYVADsqqJCz_KWSXJuW4faonIlFSDqdvaYC2WLbZ2WMmBcUOB2Nn637oy00gZL1eIF5kwVmTpsu5hfg5ML5e7kKVdGhZErloxl91U2b6yU49EwA6HfAvjqZ3Ickicvr5r7EbtIxLVfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
هرچی حساب میکنم استقلال از طول و عرض سرویسه
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/137828" target="_blank">📅 22:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137827">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⬅️
⬅️
⬅️
حسین پنبه‌کار:
🌀
شهاب زندی از صبح در دفتر باشگاه استقلال حضور دارد و مراحل نهایی جذب دو بازیکن جدید در حال انجام است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137827" target="_blank">📅 22:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137826">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
❌
پرسپولیس قصد نداره حتی با وجود جذب ایری، ابرقویی رو بفروشه و او آلترناتیو دفاع چپ هم هست/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/137826" target="_blank">📅 22:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137825">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tEi9OUGhN4x4G2C0MprnQXLwX8Hk8x6WD57zDQCmf6Yu52XEdynCwyvVWz8XwRymO6TbP_uz0yTiYHJZqaSY8SntcGsZYIMVpHQFxM33WSu6ukBxXWHkCsagqwSsTmkL_Pnt3QGQuUzichaFb44791aszHgw0odzF9rPw8DWz-l3LLfpP3_I4JMP8Lf8xhlSeFQKC6PPjCnGSrKxij_vsqJ1uPRS6SXNHvXJ-DXtF7R7B2WrYTpqhdRCureFSdbHVYAu2mBKESJN2QPhEdAfWgLe7IEiD0TC-Se0W1afj5eMGrtz--43VdF-kXI6EJmqaY30szQEDpFZhSAQHy8pYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یا الله بسم الله اسماعیل کارتال ...
🔥
❌
پ.ن چه تیمی داره حاج اسماعیل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/137825" target="_blank">📅 22:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137824">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
مهدی تارتار هفته گذشته یک دفاع چپ خارجی به باشگاه معرفی کرد و اعلام کرد قرارداد بیفوما و گرا فسخ بشه اما مدیران باشگاه پرسپولیس به این نتیجه رسیدن هم بیفوما و هم گرا بمونن
👀
‼️
📰
قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137824" target="_blank">📅 22:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137823">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWLOwAQJTwd0OPr0_0mdaZtyh6LVAT0OWgjPJOgyk_5CNeciYsqzg7ad-X7WofS9Mn84QFBSRoR6kpurNg_8YTbG52K8fl8faE_BF0u-cVpwqhLAhN3vVVPF28rTpT564KX5fb9QtjzPYXtVNhpRVvPNv5oV1sUpb9QqT0TJstEiN2FU9ogmO7WZnssV87kyX7xHp02HmlId0KM-b3_9N5_0rmDjNFIsgkm7hEIrGwqwhNFK3awh6LDs5Pde8-9BqeyvcGimja3hict0dQwekcSMGyhYncpl69S2GCsUPvvYiSnwS-xane3xx06NI7NYA6VHGod3DxujqZ8ty-GNSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👎
🤡
نرینی یه وقت سلطان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/137823" target="_blank">📅 22:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137822">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">چراغی جان با تمام احترامی برات به خواطر رزومه این چند سالته قائلم ولی هوادار تصمیم میگیره تیم چه نیازی داره و تصمیش رو عملی می‌کنه  زمان ثابت می‌کنه  جلوی فشار هوادارو نمیتونی بگیری عزیز</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/137822" target="_blank">📅 22:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137821">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirmahdi</strong></div>
<div class="tg-text">چراغی جان با تمام احترامی برات به خواطر رزومه این چند سالته قائلم
ولی هوادار تصمیم میگیره تیم چه نیازی داره و تصمیش رو عملی می‌کنه
زمان ثابت می‌کنه
جلوی فشار هوادارو نمیتونی بگیری عزیز</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/137821" target="_blank">📅 22:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137820">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🙂
🤩
ایری امروز داشت میرفت اون تیمه ولی یهو پرزیدنت حدادی و احمدی سر کیسه رو شل کردن…بسوزززززید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/137820" target="_blank">📅 22:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137819">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
❌
حدادی یه قربانی فقط همین ...تمومش کن دکتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137819" target="_blank">📅 22:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137818">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🤝
🤝
🤝
قربانی رو بیار و بهترین پنجره تابستونی تاریخ رو به نام خودت ثبت کن دکتر پیمان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/137818" target="_blank">📅 21:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137816">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
❌
تراکتور و سپاهان با زدن نامه ای به فدراسیون فوتبال تهدید کردن که حق ندارید جام قهرمانی رو به استقلال بدید چون شرایط جدول لیگ پارسال خیلی نزدیک به هم بوده؛ در این صورت ازتون شکایت میکنیم./ آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/137816" target="_blank">📅 21:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137815">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⚡️
⚡️
دقایقی پیش جلسه مهم پیمان حدادی و شهاب زندی برگزار شد و طرفین به توافق نهایی رسیدند/ایسنا و فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/137815" target="_blank">📅 21:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137814">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔄
🔄
فوووووووری
✔️
مهدی تاج: ورزشگاه آزادی نیم فصل دوم در اختیار پرسپولیس و استقلال است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137814" target="_blank">📅 21:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137813">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
فوووووووووووووووری
❤️
دانیال ایری با عقد‌ قراردادی رسما و شرعا به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/137813" target="_blank">📅 21:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137812">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGxaRf1hG7fQ7c_t2TnxDEeBuWNUIAoOkl6BwcBWqMajBrm_7KpVb0u3J3p6EgpoGnMoyhdaW3RG7H-h3XgNhRoYkhzcXXu57iLvCzl1ucSJImWS54sRGQggBn5rfc6zmaakXP4om2NwhxIbh_jxQienXnEt8u8lpXEVdfuAIS64p_Cd6y8OFIkILSmsTD3DmvaGxpHgvemdPhp9AqxFvFjO87MVgdoVNGMBVAJvvTqrEeMzxFYI4JE_JpBRFvkvpmHRo5wVtFcuVId_CI9PlWYRGfnbpIe0wDbZ80YBLxytVsfXd0_a65PthYLoyZrv37oIdYlymyuNx4ATykEpOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوووووووووووووووری
❤️
دانیال ایری با عقد‌ قراردادی رسما و شرعا به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137812" target="_blank">📅 21:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137811">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
🚨
قدوسی : قرارداد دانیال ایری فردا امضا میشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس   @SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/137811" target="_blank">📅 21:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137810">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrR_abKPHsRkp98zhrGhNFuaE_WU4x9c-eBxOVAhC-Wj9CTEL3CP5o6LCAkW7jAzxCwjsO0v9cX1tAnGlsfm-AAEh3g75unWFBLRG9UjRNHFsuMXW1c9s7oXngNJj-K2O15YpAdRs9aMFdbuzgv8FzmWlV_w6LJVcVJ02a3EpioRvn6lsqkuMGaZkrxat2HODCfgS9_w4vyaK1UszcUGMVgxUzP_WMNdfpPYrXKVvXzvPbhMe0d4kLubA4GO1mS_8ro6TsRWE5-6ImDuwjSonZCS0iyMbJq_x-A67MK33pU2w2QF7B0d1R--D3EfI7wWHLz9o2cKkfwX95zZjj26uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بازگشت سرخپوشان به تمرینات بعد از یک روز استراحت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/137810" target="_blank">📅 20:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137809">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc676823cb.mp4?token=HyaboYnoDTB8SgC7fnQYAok8Qt_2yEGDDbmjNV0U5yQbJDCeolt-adX3hZZIlCJkbP9AhRq5dnKOI-Drrr1POPWarSi41y34Pv8qMopKJTycDzh4wzyjPUcTj23IXhF0wqxjX7k_RSf4Qq6GajkRVKfNUxFi2WXd_8vswdLEOenIu-YzEvd-jTwD8rpTDklKZuBQLjk2NJRiG296FVDhH-isEXovygiIanLJ-08Wdw-nNboOe1rIHqzim45AHT1VtgeN4PhndDZHirmDrmg-G2WVUI0LTIdvrBLTeS1LwPmJ6USeKcre4-bh88bcs3DRV_KRZvzbSWbwoCkeEgfDvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc676823cb.mp4?token=HyaboYnoDTB8SgC7fnQYAok8Qt_2yEGDDbmjNV0U5yQbJDCeolt-adX3hZZIlCJkbP9AhRq5dnKOI-Drrr1POPWarSi41y34Pv8qMopKJTycDzh4wzyjPUcTj23IXhF0wqxjX7k_RSf4Qq6GajkRVKfNUxFi2WXd_8vswdLEOenIu-YzEvd-jTwD8rpTDklKZuBQLjk2NJRiG296FVDhH-isEXovygiIanLJ-08Wdw-nNboOe1rIHqzim45AHT1VtgeN4PhndDZHirmDrmg-G2WVUI0LTIdvrBLTeS1LwPmJ6USeKcre4-bh88bcs3DRV_KRZvzbSWbwoCkeEgfDvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
پاختاکور ازبکستان 3 بر 0 الحسین قهرمان اردن رو برد و به لیگ نخبگان صعود کرد! بشار رسن، هافبک سابق پرسپولیس یک گل زد و یک پاس گل داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/137809" target="_blank">📅 20:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137808">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDH3l6WDmrNxnqAXH4S7vF7gEkv_BSpXsX475Q30mWJFVEflvSgU8_-N1tWxl9uHyIN3mAQx7A9O3klHFpd3iAUtdG-rdD7YuCpQRn2efODP2uLbcL6EQj4JYQmC_7aAnG43uKQsDaAr_gpzvsMdU-6onS0Qb4OMM2Es41bnE-SkKJnQ7XB7eripUJyTDWRR9tdqz4vnd2HCgAGNoLHiMZQmGLvnHo4e90RJSaKqp8KwB4Nk1VHCT0OPHisynsz2xlcpAuxydPT6z9Yp-tnhxbBOFchntVM5-lc674f9BoswbSe6ZA7Dq8pPoAcc7mN_F1BF6MYKiZeh528wRufvbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لیون برای جبران؛ اسپارتا برای حفظ برتری!
🔴
LYON -
⚫️
Sparta Perague
⚽️
لیون در خانه به دنبال جبران شکست ۲-۱ بازی رفت است و از همان ابتدا باید فشار بالایی روی دروازه اسپارتا وارد کند.
اسپارتا با برتری بازی رفت دست بالا را دارد، اما حفظ نتیجه مقابل فشار هواداران لیون کار ساده‌ای نخواهد بود.
انتظار می‌رود بازی از دقایق ابتدایی تهاجمی شود و هرچه زمان می‌گذرد، ریسک‌پذیری لیون بیشتر شود.
یک شب سرنوشت‌ساز در لیون؛ جایی که یک گل می‌تواند تمام معادلات صعود را عوض کند.
📌
در وینکوبت ثبت‌نام کن و با ۱۰٪ بونوس اولین واریز دیدار امشب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/137808" target="_blank">📅 20:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137807">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔜
🤩
سکوت حدادی معنای خاصی دارد! منتظر خبر خاص یکشنبه باشید
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/137807" target="_blank">📅 20:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137806">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
بیفوما هم موندنی شد و خارجی جدیدی جذب نمیشه/قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137806" target="_blank">📅 20:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137805">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
✔️
✔️
✔️
پیوستن رامین رضاییان به پرسپولیس شرعا و رسما کنسل شد
✔️
آنا
🥈
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/137805" target="_blank">📅 20:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137804">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⏺
تفاهم نامه سه جانبه پرسپولیس و نساجی برای جذب دانیال ایری فردا امضا خواهد شد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/137804" target="_blank">📅 19:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137803">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/137803" target="_blank">📅 19:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137802">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
✔️
✔️
ورزش سه :توافقات انجام شد و دانیال ایری به زودی پیراهن پرسپولیس را برتن خواهد کرد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/137802" target="_blank">📅 19:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137801">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
قدوسی : باشگاه نساجی به پرسپولیس‌ تخفیف داده و مذاکرات پایانی در حال برگزاری هست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/137801" target="_blank">📅 18:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137800">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
گرا باز هم زیر بار فسخ کردن نرفت و چون ۸۰ درصد مبلغ قراردادشو خواسته باشگاه نگهش میداره/قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137800" target="_blank">📅 18:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137799">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
❌
مرتضی پورعلی گنجی با عقد قراردادی به پاختاکور ازبکستان پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137799" target="_blank">📅 18:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137798">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
گرا باز هم زیر بار فسخ کردن نرفت و چون ۸۰ درصد مبلغ قراردادشو خواسته باشگاه نگهش میداره/قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/137798" target="_blank">📅 18:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137797">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">💢
💢
💢
غیررسمی: دنیل گرا در پرسپولیس ماندنی شد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/137797" target="_blank">📅 18:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137796">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
✔️
جدایی دنیل گرا از پرسپولیس جدی شده.
🗣
🗣
باشگاه دنبال فسخ قراردادشه، ولی چون قراردادش بالاست، نمی‌خواد ضرر مالی زیادی بده. احتمالاً یکی‌دو روز آینده تکلیفش مشخص می‌شه و اگه مشکل قرارداد حل بشه، قبل از شروع فصل جدا می‌شه.
✔️
فارس  «سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/137796" target="_blank">📅 18:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137795">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
مدیران نساجی بعد از درخواست خود دانیال ایری به پرسپولیس تخفیف 20 میلیاردی دادن و مذاکرات فعلا در جریان هستش!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137795" target="_blank">📅 17:17 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
