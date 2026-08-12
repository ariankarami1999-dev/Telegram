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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 01:06:13</div>
<hr>

<div class="tg-post" id="msg-137929">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🤝
🤝
🤝
قربانی رو بیار و بهترین پنجره تابستونی تاریخ رو به نام خودت ثبت کن دکتر پیمان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 769 · <a href="https://t.me/SorkhTimes/137929" target="_blank">📅 01:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137928">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🤝
🤝
🤝
🤝
🤝
🤝
🤝
🤝</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/137928" target="_blank">📅 01:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137927">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/137927" target="_blank">📅 01:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137926">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
✅
فارس: عرضه بنزین با نرخ آزاد پالایشگاهی توی کرمان فعلاً متوقف شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/SorkhTimes/137926" target="_blank">📅 00:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137925">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
✅
🎙
جلسه فشرده با الوحده برگزار شد
👀
واقعا یک قدم مونده تا امضای قرارداد با محمد قربانی چون باشگاه الوحده بسیار خوش‌بینه تا بتونه قربانی رو بفروشه. امروز مکاتبات و جلسه فشرده‌ای برای این انتقال بین ۲ باشگاه برگزار شد.
❌
❌
خود محمد قربانی هم بسیار مشتاقه تا…</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/SorkhTimes/137925" target="_blank">📅 00:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137924">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
منهای ورزش
🚨
معاون استانداری کرمان: از امشب طرح بنزین 87,200 تومنی رسماً آغاز می‌شود؛
🗣
طرحی با 4 نرخ:
🔴
نرخ اول: 60 لیتر با قیمت 1,500 تومان
🔴
نرخ دوم: 50 لیتر با قیمت 3,000 تومان
🔴
نرخ سوم: 40 لیتر با قیمت 5,000 تومان
🔴
نرخ چهارم: بنزین آزاد با قیمت 87…</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SorkhTimes/137924" target="_blank">📅 00:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137923">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
منهای ورزش
🚨
معاون استانداری کرمان: از امشب طرح بنزین 87,200 تومنی رسماً آغاز می‌شود؛
🗣
طرحی با 4 نرخ:
🔴
نرخ اول: 60 لیتر با قیمت 1,500 تومان
🔴
نرخ دوم: 50 لیتر با قیمت 3,000 تومان
🔴
نرخ سوم: 40 لیتر با قیمت 5,000 تومان
🔴
نرخ چهارم: بنزین آزاد با قیمت 87…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/SorkhTimes/137923" target="_blank">📅 00:49 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137922">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس، پرسپولیس فصل آینده در لیگ یک تیم داری خواهد کرد و اگر مشکل خاصی پیش نیاد بزودی امتیاز فولاد نوین به پرسپولیس منتقل میشه؛ در صورت نهایی شدن انتقال امتیاز فولاد نوین سید جلال حسینی به عنوان سرمربی پرسپولیس ب انتخاب خواهد شد و کمال کامیابی نیا به عنوان دستیار اول در کنار او خواهد بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SorkhTimes/137922" target="_blank">📅 00:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137921">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
خواکین گیل دستیار سابق کالدرون در پرسپولیس قرار است به عضویت کادرفنی استقلال و به عنوان دستیار سهراب بختیاری‌زاده انتخاب شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/137921" target="_blank">📅 00:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137920">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
امروز جلسات بسیار مثبتی با الوحده برگزار شده و قربانی به پرسپولیس خیلی نزدیکه/خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/137920" target="_blank">📅 00:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137919">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/137919" target="_blank">📅 00:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137918">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZs7_7MnliU8Rs55ODcd3JXlaap1-uTwJHt_pT5pCz_rhypmHCaxPCfxLShhYHapJVoeUXTvYmD1A3OXhnAN4sMirvw7CkDSd7ASNAnE-6HTeXtfjZbbztPJ4EDjIXllAv7UKM9I1CJw8XZMsCSTWBmwkLP45e0B53TpM6Q2jEkhH8-eW7utHnPE7b9PyunFzqKxJEje3mqlSkQU4q8zpZDrQmpYSi3oeuKDQTJPQ9kPJhWWHXa8ydushkH27YfHjMWGkqpCnJppAbI4C7pZwh3hNgl_8I3Og4iG7aINlElq1LFlzg9qLsfCw9msWhCn8LLx2XJYUnMtr4i_PR9U3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی شیخ الاسلامی آنالیزور ساپینتو در استقلال بعنوان آنالیزور جدید مهدی تارتار انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/137918" target="_blank">📅 23:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137917">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⚡️
⚡️
ایری همچنان در تمرینات نساجی شرکت می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/137917" target="_blank">📅 23:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137916">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
❌
پرسپولیس باید ۶٪ مبلغ قرارداد بازیکنارو پرداخت کنه تا کارت بازی‌شون صادر بشه.اگه امروز پرداخت انجام بشه، همه بازیکنای لیست برای بازی با شمس‌آذر مجوز بازی دارن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/137916" target="_blank">📅 23:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137915">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
بااعلام سازمان لیگ؛ دیدار این هفته استقلال مقابل مس شهربابک در ورزشگاه شهر قدس با حضور هواداران تیم استقلال برگزار میشود. بعد از 229 روز بالاخره پای هواداران فوتبال به استادیوم باز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/137915" target="_blank">📅 23:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137914">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
تسنیم: قرارداد دانیال ایری با پرسپولیس پنج ساله بسته شد و مبلغ رضایت‌نامه این بازیکن 2,5 میلیون دلار ثبت شد که پرسپولیس بتونه بعدا ازش درآمدزایی بکنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/137914" target="_blank">📅 22:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137912">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
منهای ورزش
🚨
معاون استانداری کرمان: از امشب طرح بنزین 87,200 تومنی رسماً آغاز می‌شود؛
🗣
طرحی با 4 نرخ:
🔴
نرخ اول: 60 لیتر با قیمت 1,500 تومان
🔴
نرخ دوم: 50 لیتر با قیمت 3,000 تومان
🔴
نرخ سوم: 40 لیتر با قیمت 5,000 تومان
🔴
نرخ چهارم: بنزین آزاد با قیمت 87…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/137912" target="_blank">📅 22:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137911">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
حمید رسایی: دولت میخواد قیمت بنزین رو تا ۲۰ هزار تومان افزایش بده.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/137911" target="_blank">📅 22:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137910">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
❌
فوتبال ۳۶۰ : کسری طاهری به سپاهان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/137910" target="_blank">📅 22:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137909">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇷
ادعای رسانه مصری؛ ژاوی گزینه هدایت تیم ملی ایران!
🔴
رسانه‌‌ Smashi Sports مصر، در گزارشی مدعی شد که "ژاوی هرناندز" سرمـربی سابق بارسلونا، در فهرست گزینه‌ های فدراسیون‌فوتبال ایران برای سرمربیگری تیم‌ملی قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/137909" target="_blank">📅 22:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137908">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
✅
خبرنگار: چرا کسری و دانیال رو خریدی!؟
🔴
شهاب زندی: من وظیفمه برای این هوادارا بجنگم. باید بهترین بازیکنا رو بخرم و باشگاه رو به سمت درامد زایی ببرم. شما نساجی را در سه سال آینده ببینید. قول میدهم بیشترین لژیونر و جوان را تحویل فوتبال ایران بدهیم
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/137908" target="_blank">📅 22:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137907">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
❌
پرسپولیس هنوز به دنبال جذب دفاع چپ است و شاید سعید کریم‌آذر مدافع چپ تراکتور که به چادرملو رفته به فهرست سرخ‌ها و میز مذاکره برگردد./ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/137907" target="_blank">📅 22:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137906">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇪🇺
شطرنج پاریس و استون؛ فقط یک برنده! یکی برای تحمیل قدرت می‌آید، دیگری برای شکار لحظه‌ها؛ ۹۰ دقیقه کافی‌ست تا یکی رویایش را به واقعیت تبدیل کند.
🏆
فینال سوپرکاپ اروپا  [ پاری‌سن‌ژرمن
⚽️
🆚
⚽️
استون‌ویلا ]
⏰
چهارشنبه ساعت ۲۲:۳۰
🏟
…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/137906" target="_blank">📅 22:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137905">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🟣
با اعلام مدیر ورزشی باشگاه الوحده جدایی محمد قربانی از این تیم قطعی شده و مقصد بعدی این بازیکن یکی از دو تیم تراکتور یا پرسپولیسه‌.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/137905" target="_blank">📅 22:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137903">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
بازیکنان پرسپولیس امروز زیر نظر کادر فنی، برنامه‌های فشرده خود را دنبال کردند.
🔴
در این تمرین، سرخ‌پوشان پایتخت پس از گرم کردن، به اجرای دستورات تاکتیکی و فوتبال درون‌تیمی پرداختند.
⚡️
نشاط و آمادگی بالایی در میان بازیکنان مشهود بود.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/137903" target="_blank">📅 21:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137902">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEI0GZb8wPIrADoRsimpPWixPqolkLdmJ4MJxEf5JTwalk3_DUf3oEXABkps7JDFERYjbRD0LBdjIw2EV3Ue1cwTSAjQX3tELv8wwpOP2Bj9haBYahfyGZKCLh-TdbmMJ0T7B2mQTV9jWySLPTPw5gax54U-Qvm_NcYlcSaKEC8yyNizBWy5LxO9beM_r6oGjfW_Fy8Q5Zlna56jslj11c3FER9qqeWsnhJDBa4JYqjI8P8OJEsWKTZUyO0zUjCwoyqMKjp6bFzjBm0VOXA6l92UvjgqtzAZ66LF0D4FqzGFa8Ee7r06eLJdnl8TYi6C8ZeJ01846s0fXVzHrLVQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بازیکنان پرسپولیس امروز زیر نظر کادر فنی، برنامه‌های فشرده خود را دنبال کردند.
🔴
در این تمرین، سرخ‌پوشان پایتخت پس از گرم کردن، به اجرای دستورات تاکتیکی و فوتبال درون‌تیمی پرداختند.
⚡️
نشاط و آمادگی بالایی در میان بازیکنان مشهود بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/137902" target="_blank">📅 21:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137901">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
باشگاه‌ الوحده ‌امارات: دوباشگاه ایرانی برای جذب محمد قربانی مکاتباتی با ما داشته‌اند و بزودی تکلیف نهایی این بازیکن نیز مشخص خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/137901" target="_blank">📅 21:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137900">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
ممد قربانی برای دهمین روز پیاپی در تمرینات الوحده حضور نداشت تا خروجش از تیم اماراتی قطعی بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/137900" target="_blank">📅 21:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137899">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/137899" target="_blank">📅 21:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137898">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/137898" target="_blank">📅 20:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137897">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
❌
محمد جواد حسین نژاد دقایقی قبل ضمن تشکر از باشگاه پرسپولیس آفر این تیم رو ردکرد و به‌پیمان‌حدادی مدیرعامل‌سرخپوشان اعلام کرده که فعلا قصد نداره به لیگ برتر ایران برگرده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/137897" target="_blank">📅 20:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137896">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/137896" target="_blank">📅 19:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137895">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
✔️
ادعای آناتولی به نقل از منابع پاکستانی:
❌
آمریکا و ایران با تمدید ۶۰ روزه آتش‌بس بر اساس یادداشت تفاهم، موافقت کرده‌اند؛ طرفین در حال تبادل پیام هستند تا درباره مدت زمان تمدید، تصمیم‌گیری کنند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/137895" target="_blank">📅 19:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137894">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/137894" target="_blank">📅 19:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137893">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137893" target="_blank">📅 19:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137892">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
مهدی تارتار هفته گذشته یک دفاع چپ خارجی به باشگاه معرفی کرد و اعلام کرد قرارداد بیفوما و گرا فسخ بشه اما مدیران باشگاه پرسپولیس به این نتیجه رسیدن هم بیفوما و هم گرا بمونن
👀
‼️
📰
قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137892" target="_blank">📅 19:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137891">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/137891" target="_blank">📅 18:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137890">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137890" target="_blank">📅 18:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137888">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
گفته میشه که کوروش اژدهاکش بازیکن جدیدمون قرضی 1 ساله میره نساجی..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137888" target="_blank">📅 18:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137887">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
سازمان لیگ به استقلال گفته کارت بازی آسانی رو صادر می‌کنیم ولی اگه بعدا بازی‌هاتون سه هیچ شد پای خودتونه
🔹
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/137887" target="_blank">📅 17:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137886">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
واکنش مسی به درگذشت پدرش
❌
❌
«بابا، هنوز نمی‌توانم باور کنم که دیگر نیستی، یا بهتر بگویم، نمی‌خواهم باور کنم. تصور اینکه دیگر تو را نمی‌بینم و حرف نمی‌زنیم، خیلی سخت است.»
❌
❌
«همیشه از من می‌خواستی که آخرین جام جهانی‌ام را بازی کنم. چند روز مانده به شروع…</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/137886" target="_blank">📅 17:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137885">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
‏ مسی در مراسم ختم پدرش
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes ‎</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137885" target="_blank">📅 17:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137884">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
📰
باراک راوید، خبرنگار آکسیوس: توافق ایران با عمان و امریکا نهایی شده و فقط شورای عالی امنیت ملی ایران باید اون رو تصویب کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/137884" target="_blank">📅 16:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137883">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEDuLeNL9cZ2zCksCE5dFlO7jbcgTeRiIQfBl86kJnpuWH9fh5D8uBcGeZtWxRymmGKeWZ0-pS8S0Y9yrz6mqRvxy92QXbXavyaJV_UbyBO3arCS3mjLaMLOX1umNHHezxXhQPRMZh4agkTaIc41K8EGWXVYoocM3UP91NJRjN_I3CiCy-WiwubZ4JPsJ-mCYuvlewD0dGz3GNX7V6AdJ5l5cOd7B0QCKaWAWhffHSoEX8fmmiYcN76yBrsB3mNUhJxMATgRu2ss8-cx-gKahqkTYQzMqQocrRmLCWxT2rdo_ZCQeGjOidGpc_R6rnjPS6FimnBodD5wRJygv-_GzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
صدای ماندگار موسیقی ایران خاموش شد
✔️
حسین خواجه‌امیری، خواننده نامدار موسیقی ایرانی که با نام هنری ایرج شناخته می‌شد، ساعتی قبل در سن ۹۴ سالگی درگذشت.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/137883" target="_blank">📅 16:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137882">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
تارتار رسما اعلام کرده به هر چهار مدافع تیمش نیاز داره و اجازه جدا شدن به حسین رو نداده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/137882" target="_blank">📅 15:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137881">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🤝
🤝
🤝
قربانی رو بیار و بهترین پنجره تابستونی تاریخ رو به نام خودت ثبت کن دکتر پیمان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137881" target="_blank">📅 15:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137880">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
رسانه های ورزشی آذربایجان هم در حال پوشش خبری پیوستن قربانی به پرسپولیس هستند‌.....  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137880" target="_blank">📅 15:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137879">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
تلاش باشگاه پرسپولیس برای جذب قربانی ادامه دارد و به نتایج مثبتی هم رسیده و اگر اتفاق خاصی رخ ندهد، او به زودی به پرسپولیس ملحق خواهد شد / ورزش سه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/137879" target="_blank">📅 15:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137878">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
تسنیم: قرارداد دانیال ایری با پرسپولیس پنج ساله بسته شد و مبلغ رضایت‌نامه این بازیکن 2,5 میلیون دلار ثبت شد که پرسپولیس بتونه بعدا ازش درآمدزایی بکنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/137878" target="_blank">📅 15:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137877">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/137877" target="_blank">📅 15:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137876">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
tik tak...  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/137876" target="_blank">📅 15:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137874">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cwy6-zLAnlRvg0HXJw1R0ZvUI_dnxxdVpP5ORX8U8lxycDbwDRteIvrITFS-Ttods7aqJwst2wMn_3kX1q1qOSfhMz63ACsklZSTHZW3R8A1zQCcnXeWBeW7JZlhejtnAcqjPHOcv-xDPfgAld9SFJnXQ5CGYTji_9qHPEnN-v-ndQwHK_M8zNvnUa76IWnAAh7T43OxkUsEOvPkQFNu7GMUG2xUCCa8yilorikCWnpyLcQI7OvdOUr3d4R9twU_xTrFOHiRHGmh1D3rQxFCNCTnVWfN9L5Cz4zwNxNhhCV-AHHR0u8Eg9zIUTBF4DeBu4BxfEO0TOT7fMp6gZ-ZtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوریا شهرآبادی تو بازی‌های پیش‌فصل 8 تا گل زده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/137874" target="_blank">📅 15:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137873">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/137873" target="_blank">📅 14:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137872">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/137872" target="_blank">📅 13:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137871">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
فوری : رامین رضاییان با قراردادی ۱+۱ ساله به فولاد خوزستان پیوست.
✍️
خبرگزاری فوتبالی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/137871" target="_blank">📅 13:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137870">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/137870" target="_blank">📅 13:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
قدوسی: مدیران باشگاه پرسپولیس به ما گفتن با وجود عنایت زاده، باکیچ، خدابنده لو ، پورعلی و لطیفی فر امکان جذب توأمان هر دو بازیکن (محمد قربانی و محمدجواد حسین نژاد) وجود ندارد و یکیشون جذب میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/137869" target="_blank">📅 12:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137868">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏
✅
️ برنامه مسابقات هفته اول لیگ برتر فوتبال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/137868" target="_blank">📅 12:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137867">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1TQFq2DBX7WRUNhexxb-WmxnfofVe-rRYpUTvi_Lz9mYp1GZbnyarp2NNcx_fEXxm4mgQF1A9nHQqtNYUltYAZLp4si0u5-8pajMwUw3Gz-G4GIJAYG6RxvfwbKqzYAkAo8Ub72z-y1iHgFE1ecj8VmnJsV0VqOoxoI-7yqzlNOnDO-p_Z16XrASuzfF9iXouFQkEkJgcNh_I2LYMfqq0n7pjDIfmTGHBEzhMMbArVh2oCEoLiisyd9wCVnQSs6HXbkKYqAZV2g3M948YxIl__rFhf806Y05MH2SM1-bvOu7u2QXHENBHHzUdYGagakTkIIuovuq-3OxQukBFkVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
✅
️ برنامه مسابقات هفته اول لیگ برتر فوتبال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/137867" target="_blank">📅 12:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137866">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
لباس پرسپولیس عوض می‌شود
⚡️
⚡️
باشگاه پرسپولیس برای فصل جدید رقابت‌های فوتبال، در آستانه تغییر برند تولیدکننده البسه خود قرار دارد.
⚡️
⚡️
⚡️
برند «یوسف جامه» در فرایند مربوط به انتخاب تولیدکننده البسه باشگاه پرسپولیس، توانسته نظر کمیسیون معاملات باشگاه را جلب…</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/137866" target="_blank">📅 12:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137865">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔄
🔄
توافق نهایی پرسپولیس با دانیال ایری و نساجی انجام شد و صبح شنبه از ایری رونمایی میشه
⚪️
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/137865" target="_blank">📅 12:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137864">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/137864" target="_blank">📅 10:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137863">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/137863" target="_blank">📅 10:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137861">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
خرید بعدی پرسپولیس محمد قربانی خواهد بود / ورزش 3
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/137861" target="_blank">📅 10:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137860">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
قربانی آخرین خرید پرسپولیسه/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/137860" target="_blank">📅 10:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137859">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
🆕
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس دانیال ایری با شماره پیراهن ۸۹ برای پرسپولیس به میدان خواهد رفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/137859" target="_blank">📅 09:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137858">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
❌
گویاآمادگی پوریا شهرآبادی بیشتر از علیپور و سرگیف بوده است اما برای اینکه فشاری بهش وارد نشود قرار است کم کم وارد ترکیب اصلی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/137858" target="_blank">📅 09:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137857">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
باشگاه پرسپولیس موفق شود محمد قربانی را جذب کند پرونده نقل‌وانتقالاتی خود را خواهد بست و اگر موفق نشود دیگر بازیکنی جذب نخواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/137857" target="_blank">📅 09:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137856">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
باشگاه پرسپولیس موفق شود محمد قربانی را جذب کند پرونده نقل‌وانتقالاتی خود را خواهد بست و اگر موفق نشود دیگر بازیکنی جذب نخواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137856" target="_blank">📅 09:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137855">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/137855" target="_blank">📅 09:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137854">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
❌
پرسپولیس باید ۶٪ مبلغ قرارداد بازیکنارو پرداخت کنه تا کارت بازی‌شون صادر بشه.اگه امروز پرداخت انجام بشه، همه بازیکنای لیست برای بازی با شمس‌آذر مجوز بازی دارن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137854" target="_blank">📅 07:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137853">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJ4e3rnUXqivIXJlX8nYlH7Vt_L82tJnnURZ0QWbYkmxn3mNyCj8rZOpkNp15QNcJNupRvKPkgIs0ZgzZJFfrekEHT_hqluSnhWC8vI2xh1A1eXsd0KuujIScN10HY3P7SDPwY9qfWqBepWha7pmXWbmD66I7a2KTM2ERW3NSYzsYKsY2-4Yg510JfLktYKFN3VkvupdvSnXut5AwGPAquvXIW2xKk0FpWFjZQ36s-q1ndINtnfJauzt8brg2qZ52Hv_JnFdaeMvoJ6rrb7BGjIRy2kcdSkdMH4e4-B6iwkbu2iLlpjT8GlolNOTG71XdM81-0GQxB6nvi0Inn26Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137853" target="_blank">📅 07:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137852">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/137852" target="_blank">📅 02:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137851">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvXa_FUMb588y0DhupZbifL18fktstUrS3Z5zP555V1kkWlo2vyfWqaz_MG7k837CC6swxuqVX2XsbyWWTHeBkjrjEmVaQ35EXIUr_Epc8b5292GB3C3fWocxUs6rSQq_FJoqooq2jx2mPQMTE_jKuig-eYZYScKkInjGazpNbsglyH0LrthBJfG60LUP5WU2DfY8NYSlQ5a_WOHBnmS6sai_5NOvqrqYyF3OiIec8MnCli-kQBMPRhl-1L0eaWLPbf-UBfHf2Zxq-SpxHVO--dneCZ7hwnc42cv2DL-kaaGGBszCmajcSHvk7BeMbBbdWV_UOpw4G2KieOGEqOvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
شبتون بخیر سرخدلان
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137851" target="_blank">📅 01:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137850">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
یک مقام مسوول باشگاه نیم ساعت قبل به قرمزآنلاین گفت قرار بوده ایری امشب برای امضای قرارداد و برخی امور جانبی به باشگاه بیاید.
❌
اکنون برخی رسانه ها خبر داده اند ایری در باشگاه حضور دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/137850" target="_blank">📅 01:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137849">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
سازمان لیگ به استقلال گفته کارت بازی آسانی رو صادر می‌کنیم ولی اگه بعدا بازی‌هاتون سه هیچ شد پای خودتونه
🔹
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/SorkhTimes/137849" target="_blank">📅 01:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137848">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
استعلام فیفا درمورد آسانی هنوز به باشگاه استقلال اعلام نشده. و در صورت هرگونه بروز مشکل حقوقی در این پرونده، سازمان لیگ مسئولیتی در قبال صدور کارت بازی آسانی و مستندات آبی‌ها ندارد و همه تبعات و هزینه‌های آن را استقلال برعهده گرفته‌ است / فرهیختگان
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/SorkhTimes/137848" target="_blank">📅 01:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137847">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
عجیب اما واقعی!
✔️
تخلف عجیب و بزرگ سازمان لیگ؛ قرارداد جدید آسانی ثبت شد
‼️
بزرگترین تخلف تاریخ سازمان لیگ فوتبال از بدو تاسیس تا به امروز رخ داد و کارت بازی بازیکنی که قرارداد شو فسخ کرده و از تیمی که پنجره نقل و انتقالاتش بسته ست و امکان ثبت قرارداد…</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/SorkhTimes/137847" target="_blank">📅 01:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137846">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
❌
فوتبال ۳۶۰ : کسری طاهری به سپاهان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/137846" target="_blank">📅 01:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137845">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚫
یه عده میگن یکی از اعضای هیئت مدیره داره سنگ اندازی میکنه، من اطلاعی ندارم اگر صحت داشته باشه و اثبات بشه کونشو پاره میکنیم کاری نداره که…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137845" target="_blank">📅 00:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137844">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWGvDd9PYAhPwma_7u9J5CQ2lXYNWki_scnxIQRfcYFoGQM90pYRwnzQf4fgpootaedDpRFZy02DCqHtmbAU6agBg7ZpExgomOTu90xmLYzjxCsx9KsRm6hs2_QknGg11JPuYEMVed47vqc0lZh91JTWvHoH2fHj1EMmcCoRaDhoN18cQtwdrg6JZdPVDodvW_cDQfZaK12d8XMvcwMLnRhUAyndZQW1RXxQCV8K1ptuRkVJVa44enfO4VRyWQEEGkU2iugfSGlDiv27JvUPnq5ZTrbBXqgGN7LGegSCYil415joWJZm_JDntQuzOfYIJMAlveBg60H4jLaEcQ9aLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/137844" target="_blank">📅 00:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137843">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
🆕
🏅
به گزارش رسانه «سرخ تایمز» و طبق گفته های عضو هیئت مدیره باشگاه پرسپولیس، باشگاه مصر هست تا محمد قربانی رو به خدمت بگیره و خود محمد قربانی هم علاقه منده تا به پرسپولیس بیاد اما مشکل اینجاست باشگاه الوحده داره بازی در میاره و تا الان…</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137843" target="_blank">📅 00:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137842">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/SorkhTimes/137842" target="_blank">📅 00:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137841">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/SorkhTimes/137841" target="_blank">📅 00:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137840">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
فوووووووووووووووری
❤️
دانیال ایری با عقد‌ قراردادی رسما و شرعا به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SorkhTimes/137840" target="_blank">📅 23:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137839">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftq7BRnr0q1TkU0kiegNbfp_HUl5fluzm1jUGbeEPH8du1ivMnUNic3WnDs9aB3cuzsHqgc4CJ0EvwMerNkat5FCrusVfXL1oGNKYMXjRtj7NvpgeMF32eDtts-xooeoABEbS4gWvpd5azl7pwgvUu9Tk7S8JIKfVTuwq8a_zgkTt7ErT1RSqNJoMFIuYyn261Y3W9N3HoHQLXnX4ZymdevKnlgP74pXKQ0-k3JAaXIzTISITO8zPYnqGsz435eCsBDKXTj4M4dCJ98tmpqIWhYdlceCkMuu5miG_kgTVmH8TxIAnrHttF5kapE4AOVtzR3ADeMczlKVCMv5DFwmIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
مهدی تارتار هفته گذشته یک دفاع چپ خارجی به باشگاه معرفی کرد و اعلام کرد قرارداد بیفوما و گرا فسخ بشه اما مدیران باشگاه پرسپولیس به این نتیجه رسیدن هم بیفوما و هم گرا بمونن
👀
‼️
📰
قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/SorkhTimes/137839" target="_blank">📅 23:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137837">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
❌
سازمان لیگ 11 و 12 شهریور را برای برگزاری دربی در نظر گرفته و پنجشنبه 12 شهریور گزینه احتمالی است.
❌
با این حال، تاریخ نهایی مربوطه هماهنگی با برنامه تیم امید و مسابقات آسیایی تیم‌های ایرانی خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/137837" target="_blank">📅 23:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137836">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⛔️
میره تراکتور بیخود به دلتون صابون نزنید، ایجنتشم منصور عظیمیه بازیکنشو نمیاره پرسپولیس و در اخر اینکه ما اصلا هافبک دفاعی لازم نداریممممم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/SorkhTimes/137836" target="_blank">📅 23:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137835">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/137835" target="_blank">📅 23:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137834">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
❌
فوتبال ۳۶۰ : کسری طاهری به سپاهان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/137834" target="_blank">📅 23:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137833">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
❌
فوتبال ۳۶۰ : کسری طاهری به سپاهان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/137833" target="_blank">📅 22:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137832">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✔️
✔️
✔️
طبق استعلام دو باشگاه استقلال و پرسپولیس خرید کسری طاهری طبق قانون فیفا پل حساب میشه و هرکدوم از تیما بخرنش باید تا نیم فصل صبر کنن تا کارت بازیش و itc این بازیکن فعال شه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/137832" target="_blank">📅 22:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137831">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
رضا درویش: سرژ اوریه بازیکنی است که بعد انقلاب بازیکنی به این کیفیت به فوتبال ما نیامده است و او سابقه بازی در منچسترسیتی و پاری سن ژرمن را دارد. به زودی مشکل او حل خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/137831" target="_blank">📅 22:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137830">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
باشگاه سپاهان از باشگاه استقلال به دلیل استفاده از بازیکن غیر مجاز ( ماشاریپوف ) در بازی برابر این تیم شکایت کرد و خواستار سه بر صفر شدن آن‌ بازی شد /ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137830" target="_blank">📅 22:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137829">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
#فوری؛ بعداز حرفای‌ دیشب تاج برای اهدای جام قهرمانی فصل گذشته به باشگاه استقلال؛ مدیران دو باشگاه‌ سپاهان و تراکتور به فدراسیون اعلام کرده اند یک‌ تورنمنت سه‌جانبه برای تعیین قهرمان برگزار کنند. به‌ اینصورت‌که تراکتور - سپاهان به مصاف هم برند و برنده اون‌…</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/137829" target="_blank">📅 22:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137828">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQFfGah_UYoIcMKCHN2Lagiz4-gE8TBNuQceG8lLcC92Gwh6jYdWCA1YoYalQdhtO3kPjOyJzAMlANKkpJZwjaztv4Iz5h_Q2x8HrAgDKPa2Q1anHywSq6ZiL7hGCV0FQpk12kSzEDmGN_4k3pGqA1QP5kV6VYfmUg7LkNWEeidGLYErxbO7DCEOsaWAar5xRL5-w9rlqpPtYVADsqqJCz_KWSXJuW4faonIlFSDqdvaYC2WLbZ2WMmBcUOB2Nn637oy00gZL1eIF5kwVmTpsu5hfg5ML5e7kKVdGhZErloxl91U2b6yU49EwA6HfAvjqZ3Ickicvr5r7EbtIxLVfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
هرچی حساب میکنم استقلال از طول و عرض سرویسه
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/137828" target="_blank">📅 22:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137827">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/137827" target="_blank">📅 22:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137826">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
❌
پرسپولیس قصد نداره حتی با وجود جذب ایری، ابرقویی رو بفروشه و او آلترناتیو دفاع چپ هم هست/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137826" target="_blank">📅 22:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137825">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dZy5Wb6tgpgtfFtyD_y8ey1aHqAOUOSrEw3B3lcjwdHR19HcGpnKaQkzoO4juAhbyJEYZoC-O45YdGD4JdvF9dFUfTKPQJ5CeVfL82LDyjcUb0fNbZ7tyqY-uyvBJNpBWtl401oOzQOKpQXpq4nZZTpyjtC-OT6kHAfnOSCtKOBaJLspFmyavWGMrhg0vAysjrm6sl1U5-u3E8m5p-u7NNXm3IJjEUH1w13Ew2_jdWGwYhwQ_lMQ_b1Qr-BU1RvA_KDwNpD0zSxnZkQue45pU6-s5JpoUKBeY3jFuTuLaLQWQOKRqMLKiBwbZTRRErw6Afylw-wnRTJK7_9rEIb1Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یا الله بسم الله اسماعیل کارتال ...
🔥
❌
پ.ن چه تیمی داره حاج اسماعیل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/137825" target="_blank">📅 22:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137824">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
مهدی تارتار هفته گذشته یک دفاع چپ خارجی به باشگاه معرفی کرد و اعلام کرد قرارداد بیفوما و گرا فسخ بشه اما مدیران باشگاه پرسپولیس به این نتیجه رسیدن هم بیفوما و هم گرا بمونن
👀
‼️
📰
قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/137824" target="_blank">📅 22:17 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
