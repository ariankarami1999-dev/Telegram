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
<img src="https://cdn4.telesco.pe/file/qBw32K-FIc_TpGgH61CrFSkFQTB4ZAdIwC8LWVgOZcRXAZ8vDFQjpaJIfJHq2pg7mKBvAyqOw3Gaoq1RLUcVH4kr3T6bB8T-rIsSfMIhUCqkh_mEEompaHlUEHV78ohDmezAUBxGJvfVVkxTC3V6slEzO13UcutMAitu-2qlsL-mEWHFpno1Et1XeP9_x4fVpH3NSTNea59P2n5-ABUtLqufxRMu2RPqtpdvIMBtM5WvOgG4qKEAe5WIS0cnUitDc3U5W8i2LE-Wki0HAIhIGync_jJCc6SPGab3MRfgXeA1kzOPps_IYcP6IAuOCWcz3qnDiw8ubJK6yajS0G0zJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 20:31:06</div>
<hr>

<div class="tg-post" id="msg-136601">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
✅
امیرحسین محمودی در فصل آینده با شماره 10 برای پرسپولیس به میدون خواهد رفت. شماره ای که سالها بر تن بزرگی همچون علی آقا دایی بوده
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/136601" target="_blank">📅 17:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136600">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEVl8JSISaE5PGIdlAFQX0hga7my8TsrBI38lWi6z-u5IUHEabI_BjCos3Z0lYT5TOdCZkGpCT9RCznJjGvCPK23YdyqPzr2nP1mbnFpvLSXvhU5R76sujvCxipSQSE_RnNd5s4j_-_1y5o4CA8wx17ekShM16R3gtNWR-8zWaklw0Qd6wmF5BP6gac-YFnuij-Er86rU-yTlsFYekldCaSgUuLQTmEy6uR5Znlj2VURcI9PETTI0veY_fdkqLyAMi2rFhbPtcqdqslvDrX0xP8hAuh4Q7Bju3pClNgxRnrnxPxd3TxJAHfrvLaPU604BIegRpi9T3G0CQez9xPCyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خواکین گیل دستیار سابق کالدرون در پرسپولیس قرار است به عضویت کادرفنی استقلال و به عنوان دستیار سهراب بختیاری‌زاده انتخاب شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/136600" target="_blank">📅 17:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136599">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⚠️
⚠️
تیم فوتبال پرسپولیس در اردوی ترکیه با فنرباغچه که هدایت آن برعهده اسماعیل کارتال است، یک دوستانه بازی برگزار خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/136599" target="_blank">📅 17:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136598">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
تایم و رقبای سه دیدار دوستانه پرسپولیس در اردوی ترکیه مشخص شد.
❌
سرخپوشان در تایم های 8،4 و11 مرداد ماه با  تیم‌های «پیرامید»، «آنالیا اسپورت» و یک تیم دیگر به رقابت می‌پردازد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/136598" target="_blank">📅 17:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136597">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
فخر فوتبال ایران، چشم و چراغ باشگاه پرسپولیس؛ بازیکنی که همیشه پیام‌آور افتخار و موفقیت برای ایران در عرصه جهانی بود
❌
اسطوره محبوب و محترم پرسپولیس، تولدت مبارک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/136597" target="_blank">📅 17:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136596">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
✅
زارع و شهرآبادی دوباره در ترکیه؛ استراحت دو روزه برای سرخپوشان
⏺
مهدی تارتار امروز را به شاگردانش استراحت داده و فردا نیز سرخپوشان خود را برای سفر به ارزروم ترکیه آماده خواهند کرد. در واقع فردا عصر کاروان پرسپولیس عازم این سفر خواهد شد و 10 روزی را در آنجا…</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/136596" target="_blank">📅 17:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136595">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
فرهیختگان: محمد‌مهدی محبی در لیست مازاد اتحاد الکلبا قرار گرفته و باشگاه اماراتی پولی بابت رضایت نامه محبی نمیخواد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/136595" target="_blank">📅 17:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136594">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از تسنیم
🔴
استعلام باشگاه پرسپولیس از فیفا رسید و هیچ مشکلی برای جذب دانیال ایری و کسری طاهری وجود نداره و این بازیکنان ظرف امروز و فردا قرارداد شون رو با پرسپولیس امضا خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/136594" target="_blank">📅 17:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136593">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه، حتما عضو شین و‌ چک کنید چقد راحت سود میشه کرد
😉
✅
JOIN JOIN JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/136593" target="_blank">📅 16:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136592">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpxWqfCkPfPBB2aoEapclFWA4ShtwVbJe_1uQlDfKJVkG2ZszGLXp38gETGRWOOAopR7TeCEdl2REinUpb8pr2WkhKvUPR43nERJOVwQsiRhDZRbG7NyXO1-Aq07I9vAivwbEICLu-dDGxDuSTpuWWvfTdSlaYI0W2pNayKz8sMorC5tdhwd7xoF_jBP7m8n7zZ-LKAyYaKvzKj6x2ImEqDzpesq8dV_Q1bgsS5VvTRRxr_ZQs2g9VBTMHPozc3rrIWzG8Ag6SxsdhNVZaEdV3ClFWLqJR-WCGyaiXkFX_WGDyAWgJoLqBSuJHuBA9GRUAytFVXiBbreSKzmA-u-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب حتی با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🤷‍♂️
@PeakyBetBlinders
@PeakyBetBlinders
@PeakyBetBlinders</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/136592" target="_blank">📅 16:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136591">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
ایشونم از روستوف‌ روسیه جدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/136591" target="_blank">📅 15:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136590">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPS11knlTwFFmObmH_Sq0e1t0mAV-9QI0gKY-Bnua9vUnEQYVvJF_vTjJ9Yqq6uFwxrhz1NQFwtYZpBodDdB_52j1XNaGlW30sp7rSc09lKRtXUHkb4A-Hr0xqQlWKAOgYpgulq4DuiKGG_xgPmhjJZJuN6D9xlLnRcEvKDSQK0f5Op49nNMvdMAKf9tX8BthTRLv6zSQHMLVKVfG3LvB6G-7zczB4D70awYptGkdnXYw9fgrFWmpeQjfrteBBeQD92bU0wObuWVsxyACEiuOI1QVtLVbTtoOwdbQFl_pY7qFdqB-0Hpfcy3G2FU-Qyv3LC8gtoWaeciFlxSapWHkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایشونم از روستوف‌ روسیه جدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/136590" target="_blank">📅 15:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136589">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🔴
طبق قول و قرارهای انجام شده پوریا لطیفی‌فر، حدود ساعت 15امروز برای عقد قرارداد به باشگاه پرسپولیس خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/136589" target="_blank">📅 14:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136588">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❗️
❗️
درویشی وکیل ورزشی :از نظر حقوقی انتقال کسری و ایری از نساجی به پرسپولیس خطرناک و ریسک بالایی داره..
🤔
امیدوارم مدیران استعلامات کافی و گرفته باشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/136588" target="_blank">📅 13:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136587">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
با اعلام ترانسفر مارکت رامین رضاییان بازیکن آزاد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/136587" target="_blank">📅 13:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136586">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/136586" target="_blank">📅 12:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136585">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
پرسپولیسی‌ها نخستین جلسه تمرینی خود در اردوی ارزروم را در سالن وزنه‌ پیگیری کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/136585" target="_blank">📅 12:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136584">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
✅
محمدامین کاظمیان بخشی از قرارداد توافق پرسپولیس با گلگهر برای جذب پوریا لطیفی فر می‌باشد
🔹
محمدامین کاظمیان + حدود ۸۰ میلیارد رضایت نامه = پوریا لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/136584" target="_blank">📅 12:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136583">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
شنیده ها:قرار بود دیشب از پوریا لطیفی فر رونمایی بشه ولی به خاطر بازی تدارکاتی گل‌گهر، جلسه لغو شد و به امروز موکول شد
🔴
امروز به احتمال خیلی زیاد، پوریا لطیفی فر پرسپولیسی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136583" target="_blank">📅 12:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136582">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🌀
🌀
امیررضا رفیعی این امکان را داشت که قراردادش را به‌صورت یک‌طرفه با پرسپولیس فسخ کند، اما فعلاً این کار را انجام نداده و منتظر است تا باشگاه ابتدا گلر جدید جذب کند و سپس از جمع سرخ‌پوشان جدا شود.
⏱️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/136582" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136581">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5KFTdAXOzRRyHTe6g3kP22UhfM9kQ7wIN0rKbstaMPH343kUcwXo8ptLWBbWhc7tXmCXYCo96Pd7iHhU-O-lMoQsBljSYDFbBo69wa6zaVrLKmAGqLtNu8zVknJXaT_pKaChufml0ZOZui1ZYIFyyh99GzQ5aOs6UcCnunXYu8Nkg5g0GFDuQTOgdlZM_eJMJ_100iBwnfBEOvQuNUPLaAPDtxSdnHSwjJ6w_THTGCa2JIDBJlBToASTkjsgybvE7j7ZE6_jvM4UDLVSPv44-3Em3sCD-MUjScqlRTa-IMthsmfhCnel9vsK6DwixK-S64L_WobF1m_M_Qz7oWb6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سؤال بزرگ؛ ثبات یا آزمون و خطا
✅
❌
🚨
درویش تو سه پنجره نقل و انتقالاتی آخرش ۱۷ خرید برای پرسپولیس انجام داده که ۱۱ نفر از اونا از پرسپولیس جدا و افرادی مثل بیفوما و کاظمیان هم در لیست خروج قرار دارند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136581" target="_blank">📅 11:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136580">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/136580" target="_blank">📅 11:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136579">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
❗️
هنوز قرارداد اخباری، ایری و طاهری امضا نشده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/136579" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136578">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/136578" target="_blank">📅 10:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136577">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/136577" target="_blank">📅 10:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136576">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/En2JzwJza1hyaZn-zvsd_lqob-3Uw4dI8iNH3I6jgfzP8cq5oyMl_9I-v8cq13wlpXAj9ybSRSOskpjoaT-LlAfM8nJP4ivSmt9vn6Cazt7TG2xxZ3u7Bazv5YDHP_j63PEb7UP07HrYC49vMwjUN3QL4G99jQjXIPcc6_7SdRJBw01O0I4jYU0fp177BjdWF6mLqlgLaVTwQyPXNsVtnZ_RnCJmKpy9gOgXwy3AVeAZ52KLIuSIOl489U5Py3W2nTPQjvfqCKSk8ClDiRPIUqAKdRIA0HIkN8j6qHO5FQ0Whqdx_QLUE0Bzq7U03s2exWig4uVmFu-gGUrEtGNXow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
با اعلام ترانسفر مارکت رامین رضاییان بازیکن آزاد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136576" target="_blank">📅 10:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136575">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
فورییییی از رسانه برزیلی UOL: جنگ بین آمریکا و ایران مستقیما تو این انتخاب نقش داشته و ترامپ در انتخاب داور فینال جام جهانی دخالت کرده
❗️
رابطه نزدیک اینفانتینو با ترامپ هم به عدم انتخاب فغانی کمک زیادی کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/136575" target="_blank">📅 10:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136574">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZAVkkp71qBTF9it93Wa8VdaUtkSu7LK61d0aTM1Q3PwT7oeeRYxSrYDo4KHvotPI2MOIhUYLabpYaXRv3ZBovFT5ZcWTJQ1LAfqpkgPRDBtuGXmlsTr65YIUwoif_kutlBkH3pI39hRQO9c49GXViZe2fcPPjp-tfCuOrNQMkYFH-rydlt39Nz64mcjCyb9pUbg2ha6kbnFDy4iC6qUbkzKnP1A-22aavJONYRroxBk6fFj1hQKjUW9moke0ixGDc5VKnSi6EIqgwUMHBMwsUgGm5oxcphz2thtNGjTbh3mt3XQscwncUec53FU2AJLQibdlSXrHAKpbeOSX-oQKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تارتار در گفتگو با پیمان حدادی از وی خواسته که هیچ‌پیشنهاد خارجی را برای اورونوف بررسی نکند چون این بازیکن اصلا فروشی نیست و فصل‌آینده ستون اصلی ترکیب تارتار خواهد بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/136574" target="_blank">📅 10:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136573">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🫥
🫥
شایعات: محمد قربانی در لیست مازاد الوحده‌ امارات قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/136573" target="_blank">📅 08:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136572">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووووووووووووری از هفت ورزشی
🚨
مذاکرات پرسپولیس با پوریا لطیفی فر، هافبک ۲۲ ساله فصل گذشته گل گهر مثبت پیش رفته و اگر اتفاق خاصی رخ ندهد، لطیفی فر هفته آینده بعد از امضای قرارداد با پرسپولیس راهی ترکیه خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/136572" target="_blank">📅 08:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136571">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/136571" target="_blank">📅 08:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136570">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136570" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/136570" target="_blank">📅 01:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136569">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARS8v-MsytjiZWMh9IoLTKWoyzkYNx7FvjGRKpGwEP45PHd3WPKRp9QVwNvdcGUngv1Na5NAxhn587vfMtERU79bwgIeOa7s3gotPJGCWd4jpeQyt-d6C6RYxcXKTno4zv99g7eLTPq_tIMGOC0lmlPaOxUcvmwEhHSRAmZ5gzB_lQL1Koq0yk0s_M1HUbXVUFM4__bxrrFeY3_-u-IIWNco3mXKJBV1M7ZkX38jTA6fyhpzN9LjEx1djbay3fP_mDJawZmbKm8Yw_kaN4-_EjrWqivPm4-H6Xg_vprPG6lYAYXhRcQZC9e5WPsqbQDMbOMgdtUWgt5H87qn4H6Syg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هر
چهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
Ⓜ️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/136569" target="_blank">📅 01:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136568">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
🔴
فووووری از تسنیم
✅
مشکل سربازی بیرانوند دیگ قابل حل نیست و امسال یا باید بره ملوان یا فجر سپاسی
😂
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/136568" target="_blank">📅 00:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136567">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/136567" target="_blank">📅 00:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136566">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">💢
کاظمیان + رفیعی میرن گل‌گهر پوریا لطیفی فر میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/136566" target="_blank">📅 23:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136565">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
شوک به استقلال: آسانی فسخ کرد!
🔴
یاسر آسانی با ارسال نامه‌ای رسمی به باشگاه استقلال، به دلیل پرداخت نشدن مطالبات فصل گذشته و پیش‌پرداخت قرارداد فصل جدید، فسخ یک‌طرفه قرارداد خود را اعلام کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/136565" target="_blank">📅 23:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136564">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
❗️
زارع به اردوی پرسپولیس اضافه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/136564" target="_blank">📅 23:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136563">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABveO2Mb2S4bwU1KEqeUSZK3EcuDpVdEHY6demF5XCdA0S6cJyGhvVd7aCFZBlb2II5Ny2DDol_-Ei_I3lVf1lu8vQMTqRzuUp6q2jp9LPF49fh2mQh7WtsTvFgnfbiZ7po320uiU6CsfOFFD8paaA92oClLdwNWQwSPte5tFQ9igJ5oruWaqDpdXYLQFfKyZxvjxv_AHx0iE_Ge6ZhoZqjlYtwRkdPFoZ44miPgbx8RrbHjfso39TW0dbZZhfIeL6A2FqPlzZz4SF8UPucT5wtprrIhoE442jI--qo84XJu79htY-IT2Ap5Cb-xbkVKPTsn_F3kPFpiu8pWIbC_dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
پرسپولیسی‌ها نخستین جلسه تمرینی خود در اردوی ارزروم را در سالن وزنه‌ پیگیری کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/136563" target="_blank">📅 23:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136562">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
کاروان پرسپولیس دقایقی قبل وارد ارزروم ترکیه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/136562" target="_blank">📅 23:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136561">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
✅
رضایتنامه‌ی قربانی خیلی سنگینه و کنسله/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/136561" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136560">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
رفیعی خودش قراردادش رو با پرسپولیس فسخ کرده و حالا دستش بازه هر تیمی خواست بره. احتمالاً هم راهی گل‌گهر یا شمس‌آذر می‌شه و اخباری جاش به پرسپولیس میاد.
✅
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/136560" target="_blank">📅 22:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136559">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
#فوری |ترامپ به شبکه 12 اسرائیل: من در حال بررسی امکان انجام حمله‌ای بزرگ‌تر از هر چیزی که در گذشته شاهد بوده‌ایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/136559" target="_blank">📅 22:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136558">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
فوری از سپهر خرمی:
🚨
بعد از کنسل شدن تمام گزینه های پرسپولیس در پست هافبک دفاعی، مسئولان این تیم دوباره سراغ محمد قربانی رفته‌اند اما اینبار با پیشنهاد بهتر!
🚨
قربانی از تراکتور هم پیشنهاد خوبی دریافت کرده اما تمایل داره به پرسپولیس بیاد!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/136558" target="_blank">📅 22:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136557">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/136557" target="_blank">📅 22:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136556">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGZjONk_ANw5VmgIHfDnV6d76fMLaZpLcSd8_uWeAOiCFvinuflaeJ1OCWsB-eLLtZRIbSJZKv-nR5K0awpY-yPl87Gy_3G543347aqK9FgQEAuMaWo_eKZcmyAgJm011O40XL8F_GBJcRc0ndm8mcf-iIgQ_ynjkj57p6fFVBk-ehp8FQoy0Y9V--SBapeMDU0yU1_bfO-FnJh9Xr4Yhurfecue_ctRdCjlGx08nTD8K-VRQt8RdFwptIBdNKWLLVvj-4UtJYT-_w9hhqGyNG2OY6ScbCOrlHDptHOGVzkmkO07B9J5eNHlmOzJwQPXJr-b1UBX7eTiYd-jpp3hBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کاروان پرسپولیس دقایقی قبل وارد ارزروم ترکیه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/136556" target="_blank">📅 21:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136555">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗️
قاب ماندگار بازی پرتغال - اسپانیا؛ دلجویی یامال از رونالدو پس از سوت پایان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/136555" target="_blank">📅 20:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136554">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
مرتضی و کاظمیان با تیم به ترکیه نرفتن و جداییشون تقریباً قطعیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136554" target="_blank">📅 20:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136553">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136553" target="_blank">📅 20:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136552">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet.apk</div>
  <div class="tg-doc-extra">54.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136552" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🤖
جدیدترین آپدیت اندروید اپلیکیشن 1XBET
🍏
برای آموزش ثبت نام مخصوص کاربران ios اینجا را بخوانید.
✅
ورود / ثبت نام از اپلیکیشن
🎖
بزرگترین اسپانسر رسمی لالیگا
🔵
بدون فیلترشکن
از اپلیکیشن استفاده کنید</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/136552" target="_blank">📅 20:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136551">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a66TiuIDqk3FkfR7ZkWi-SUxf2fW0iGe8NnX9gj8eiZT0olXeRdnXeZy9BrHpdbQCgyNJHp_yt3oeSN4zFJ-uLVZhbOWEuMyDNtUs31muApFGRugkBxZevnseDvVklePqWiu6qXmPQMy0Er_xg2SbfDIv_DuFAI39jS690DAtekTzxu7agq0FMWf2SEGY4Y1YFTCjAMJa4J1loIOEqm12MkuNJeSYnnjZqIgjvZ0BaU1YkF-J3E5vNKq9JTdTZp5m_OHwR_LjxOYti9NXpqP9H_YJ_-Ll3TBPHFF_sJIekt3U1RpLQJeduXUXL50Jzpq6q2_Cis6bD-JpLQunIVR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1️⃣
شما هم به خانواده
1XBET
بپیوندید
1️⃣
🏁
جام جهانی تمام شد... اما هیجان فوتبال ادامه دارد!
⚽️
🔥
🎁
پلیر ها پس از 5، 10، 15، 20، 25 و 30 روز متوالی، پروموکد Freebet دریافت خواهند کرد که تا 7 روز اعتبار دارد
🔔
آموزش ثبت نام و واریز
🟦
آدرس وان‌ایکس‌بت:
🌐
Link :
1XBET.COM
🌐
Link :
1XBET.COM
🛑
برای ورود به سایت از وی پی ان (فیلترشکن) کشور های آسیایی یا کانادا یا ترکیه استفاده کنید.
➖
➖
➖
➖
➖
➖
➖
➖
🌐
Channel :
@iran1xbet_official</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/136551" target="_blank">📅 20:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136550">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🥇
🇹🇷
تیم فوتبال پرسپولیس برای برپایی اردویی ۱۲ روزه تهران را به مقصد ترکیه ترک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136550" target="_blank">📅 20:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136549">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136549" target="_blank">📅 19:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136548">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjHNepBYslPI5omBzD75LBGZ6nTX949aDOAn7B9HJJFaXhvHQthskR6n-1Mr1aDpG7SeYTP61sDf_soTDUBXNqBA-Sl6vrRiXjg6aN7AKlve2lnS4MA2PpQxFa9hYy789fTjkVu_b0nGtPCKZY9lmEfeRNwiE-ZPzCE4n5wMvsUakCuSKUgcZxdF4xJNUMODyk-xz6eq5pdGIVLX6z47CIBS1GqeYcu1-fgHtyeZdVkAJ_G85cquhp798gnhvG_yi8zXj8B_U7zB_iuEDW4sH3zt2PhgMkWk5f_i3dtfxAs9XIThDD_hPQ8Hhrc14k8aUVZBrlP6Lb7IGsWou4uanA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/136548" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136547">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❗️
❗️
هنوز قرارداد اخباری، ایری و طاهری امضا نشده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/136547" target="_blank">📅 19:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136546">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔹
فوووووووووری
😐
🔹
ترامپ: دستور دادم در های جهنم به روی ایران باز شود  ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136546" target="_blank">📅 19:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136545">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYux2lvHxwDE46GEJBX1PjvLeSp6Ku11JwnOL8SeFobexNa6IRszK0xqjek4EOK1o_4RmL_-Jc0alcRVjtPhjUFB3Sugq4Fq8BJHGlhgWQJa5pMQscSoVIwdHvzdgNb8hkKpg9BGo13Yjt2lDSkISx3PmBWbspULE_0oMdIudQmUeGZBBE0MB5uGEJtCcI7tIb5LjgwITuJZJr7iLhMWrKxNfAEldcXoZ08jjPLqipOWfrOGg14MtLs8mbp79Qg6o-a7DQ2f2o1-K7N138ZrZY7COH7p2LFwG67vjJILA5ameyLbuKNGYX-fqGt2OCxDW82JIDMagydJsrXCVD0fkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیپور تنها بازمانده نسل طلایی برانکو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/136545" target="_blank">📅 19:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136544">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feaf2d5596.mp4?token=LwFgzEpkw4JSazhAqZ3hVpCzC8AGRmVy-WmcvlTPMDkhMRdYtd_nIzoREHcU6uTE7XbgxnmQqL0BxOZSrV54BaziVOw-jW0x1_ufTckR0Cq_lC_qe3Vr7rSZDjnrSOdhYFOT5blV_2wxTUvNMRNYLwGO9oCNLPyXTXeFZ-GT2U10gufkCqBST3K3eMuct2jDdnZGRrF-ZQFDWnWQzGguOCh6FStNvqrTMxYQ4NEP33VIsmEe9TzgLjPWQ_Kxb4TdMIkwYM7-xmhQ-8aOv3snkDQuaqJeO0In42ps6ri0xQTG9pDcy9_Q3g-nMIzmYB-ipaEtSNG0hKTC7vzs1IlRcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feaf2d5596.mp4?token=LwFgzEpkw4JSazhAqZ3hVpCzC8AGRmVy-WmcvlTPMDkhMRdYtd_nIzoREHcU6uTE7XbgxnmQqL0BxOZSrV54BaziVOw-jW0x1_ufTckR0Cq_lC_qe3Vr7rSZDjnrSOdhYFOT5blV_2wxTUvNMRNYLwGO9oCNLPyXTXeFZ-GT2U10gufkCqBST3K3eMuct2jDdnZGRrF-ZQFDWnWQzGguOCh6FStNvqrTMxYQ4NEP33VIsmEe9TzgLjPWQ_Kxb4TdMIkwYM7-xmhQ-8aOv3snkDQuaqJeO0In42ps6ri0xQTG9pDcy9_Q3g-nMIzmYB-ipaEtSNG0hKTC7vzs1IlRcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
استوک صورتی با کیسه فسخ کرد
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/136544" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136543">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9YiN6e7wh8T_gVTLqroS9VdnFrVCA8DqT05rQ4ttp6lgB8oLy5-EDLeyQO4OfW42hJZ39gBTQcn_xZJx4pfxqkst89qxFv5PxqiqeWoLD_ZQUd_GNDsVPGZqYzEf0wTBqvqRa3mxT4iJ9WD1qCyzW2pDBqhALTwKRGAq1nMcYFU2E6QBbjLaoZpb0CydsaXsbmNK7sTx3Xyy1XvsHt_EYXOj5ydAub-Hs9u6iCcFgnxVt1Gopx5K24xCi6vqtUqVMwVmqmhJUxm-ffyByuZIz--PJQ6s9z9SD80A-k9P_qoAwVTWYPBzDRW3XMPwfK7B3KHrkYAPoM6ntYXQGzqAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از تمرینات خبر رسیده پویا اسمی کاپیتان ۱۶ ساله تیم نوجوانان یکی از خوب های پرسپولیس بوده
🚨
این بازیکن در این سن با این فیزیک و قد مناسب شدیدا آینده داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/136543" target="_blank">📅 17:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136542">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YL5TvJgLJvWKp4ESGin7av-gcUQC8efHGqQmph7hz66qJwGqna_6aJGwDcc1vMRdL5-NliYmxWILE56HtRT_JRCLEZJ3ggI70V0b-uQwAYPHSOAQ95ox6l7c4tCuTNl7-WLD3atUbutXXEM4Up9YfJCEEo2axGiAuAlE2dp5etP15SSsI2Pb0alY0dbLGvCte2Fg2ttMbALOFx0xTjEAUeXuMSqEPd0HzxJzRrK2hmQSdRbuMaEHSR-lTyOvAhvo14Qo2WOUwBD_3x-wRQ8i2VexNHK-5gg2IHXE0nxA04fLCDiDoia553GFGdZfk8reTQ1l13ZgjEnYyTLG8UIA4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
🇹🇷
تیم فوتبال پرسپولیس برای برپایی اردویی ۱۲ روزه تهران را به مقصد ترکیه ترک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136542" target="_blank">📅 17:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136541">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
✅
طبق شنیده ها   احتمالا فردا باشگاه از سه تا بازیکن رونمایی خواهند کرد .که شامل محمدرضا اخباری و کسری طاهری و دانیال ایری هست.
🔴
باید دید چه اتفاقی خواهد افتاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136541" target="_blank">📅 17:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136540">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnUWJhw1oajdpL4d7vCgMeZrKtJNQGw_VfB3Do4AhaqVv7QKjxplzG_U1PV5IJFDlvyXELpRPJ-o-PM5e58vsmjr-ZtgL_Mbt92o_U7qkQssMiS-HP3OzcLg-8W70IO7dL9ClA5vU__GcAqf8niaSSyj9XCNG6nlafC4t2hzEuTEMOvtKvJB5SLFruiD9-x9ii3JpxIgFy00FL2f-pQOlP1DlVo2FwJ3K1oDLyhWwSaKaKIxqGcBpBUM7C-hwNSvSzlGhfuG5YwmYzec4wWFb8Cub8Y4AGxdv7edTIbJbOG2CTxkLwnECsdbA-algFo1bl_HLBWp4VCEVsHkqifW0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تیم رفت ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/136540" target="_blank">📅 17:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136539">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/875cf546b8.mp4?token=JXJn8Oue0Ko7poESjDc4jMR87f78ALNu231KiC74x2Yohh7dA4-qOMGr2KcogEAlDUvyKVg1CAW3xi5R9YpjCFJtfa3dzlO22vWMTQzMpDnHO3rJha3tjPX-6iReg_SotpFUUk0F4tP1cquez-mFy6EfQtWqkuymIdzszE8Gy7CL_mvojqZr_XxkJfF65-5RI7mVly30bxyMNCdBIxo_Z1szpWmYxql1kf5iPUcwm4lGRKCjG4pmtVfRcZ9lJwByM8dcc0mcVbxcCa39IfLF6RURtl_8axvrkyVsjFil7mZqgMxDC2qnmry1HVdAJQ37NMNRn0cfeujzHWjiAAOu3new2wlW80O-HK2yv7nnGnxib836Zz0lw5TXTiqJpenaM_8ocSnL7_Rf2aNoyfi5vUO1W61dy4G_M4rKz2TzKIk14Pf7UcI4k1bgXrZ-n--sf0NUops6YmC0-SyuoIvntw6veEIQz4HBo3QOh0J-vXpthCvT45s_5AhhFQRk2oD5ZDr96O8hEcISJ073GkEnQnzdaaeuwh9YKnIL9S1LUp8bmkltwlgFHvIeKi_XLo3Y-R89DWtoVDDkFIPdmuPIVoB2hfN-ih_Gy7xQT28ewVOap8-yyhjbfExOZ0iUhmVXDzDc6fzOLV8QdOUiN9nR8u8vecMR6D-hlR2K9YrJrPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/875cf546b8.mp4?token=JXJn8Oue0Ko7poESjDc4jMR87f78ALNu231KiC74x2Yohh7dA4-qOMGr2KcogEAlDUvyKVg1CAW3xi5R9YpjCFJtfa3dzlO22vWMTQzMpDnHO3rJha3tjPX-6iReg_SotpFUUk0F4tP1cquez-mFy6EfQtWqkuymIdzszE8Gy7CL_mvojqZr_XxkJfF65-5RI7mVly30bxyMNCdBIxo_Z1szpWmYxql1kf5iPUcwm4lGRKCjG4pmtVfRcZ9lJwByM8dcc0mcVbxcCa39IfLF6RURtl_8axvrkyVsjFil7mZqgMxDC2qnmry1HVdAJQ37NMNRn0cfeujzHWjiAAOu3new2wlW80O-HK2yv7nnGnxib836Zz0lw5TXTiqJpenaM_8ocSnL7_Rf2aNoyfi5vUO1W61dy4G_M4rKz2TzKIk14Pf7UcI4k1bgXrZ-n--sf0NUops6YmC0-SyuoIvntw6veEIQz4HBo3QOh0J-vXpthCvT45s_5AhhFQRk2oD5ZDr96O8hEcISJ073GkEnQnzdaaeuwh9YKnIL9S1LUp8bmkltwlgFHvIeKi_XLo3Y-R89DWtoVDDkFIPdmuPIVoB2hfN-ih_Gy7xQT28ewVOap8-yyhjbfExOZ0iUhmVXDzDc6fzOLV8QdOUiN9nR8u8vecMR6D-hlR2K9YrJrPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
علی علیپور: از آقای قلعه‌نویی تشکر می‌کنم که شانس حضور در جام‌جهانی را به من داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/136539" target="_blank">📅 15:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136538">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
فوری، حمید مطهری با جدایی ابوالفضل رزاق پور، مدافع چپ فولاد خوزستان و پیوستن این بازیکن به پرسپولیس مخالفت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/136538" target="_blank">📅 14:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136537">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vu7vOCPT2ms5NB1kD0xjQ_NrNfi0rNmoEdsRVdDcMkU5fuBbDPRjj33wptuM7HwFJFCbJT26HspWsVekR_z8NJ_rOF8AU8cgfJ_z8p1UnY7gDsJ60t62aVtXR4JcqdUVnpvPcN2PHsoOejgg9lLC04wfZEnmgwelcQNiMh_HkPVR77iOuB1n2ewMU2jzepR7b_iGQRDDnerQ25sjVXtgIKyMfG_uusFAEnfphSU6Hmb03JAWK6uuhDgygLwhLPGKSoVYTU2tW0OQ4MgFNE8XTZ55kLrizZ9wtvvi_85u_rOYyGWIoWk1q5P8Q_JfL4-cjYtUNjiU7GhMyg_6jsQjvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پرسپولیس امروز برای برگزاری تو این کمپ زیبا و
اردوی ۱۲ روزه راهی ترکیه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/SorkhTimes/136537" target="_blank">📅 14:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136536">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
میلاد زکی پور، مدافع چپ سپاهان پس از قرار گرفتن در لیست خروج محرم نویدکیا، به پرسپولیس معرفی شده تا جانشین میلاد محمدی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/136536" target="_blank">📅 14:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136535">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
فوووووووووری از ورزش سه:  دانیال ایری و کسری طاهری از نساجی به پرسپولیس پیوستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/SorkhTimes/136535" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136534">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
فوری، حمید مطهری با جدایی ابوالفضل رزاق پور، مدافع چپ فولاد خوزستان و پیوستن این بازیکن به پرسپولیس مخالفت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/136534" target="_blank">📅 13:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136533">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
شنیده ها: محسن خلیلی ساعتی پیش با حمیدرضا گرشاسبی برای انتقال ابوالفضل رزاق پور دیدار کرد و قرار است در صورت توافق شخصی با بازیکن و واریز مبلغ رضایت نامه این بازیکن راهی پرسپولیس شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/136533" target="_blank">📅 12:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136532">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
✅
با نظر مهدی تارتار ، محمدحسین کنعانی زادگان به عنوان کاپیتان اول پرسپولیس انتخاب شد / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/136532" target="_blank">📅 11:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136531">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
مخالفت AFC با درخواست فدراسیون فوتبال ایران؛ گل گهر نماینده ایران در آسیا شد!
🚨
🚨
کنفدراسیون فوتبال آسیا با ارسال نامه‌ای به فدراسیون فوتبال ایران اعلام کرد گل گهر نماینده کشورمان در لیگ قهرمانان آسیا ٢ خواهد بود و در خواست فدراسیون برای حضور چادرملو را نپذیرفت.…</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/136531" target="_blank">📅 11:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136530">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
✅
پرسپولیس انتخاب کاپیتان را به تارتار سپرده؛ احتمالاً رقابت بین علیپور و کنعانی است.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/136530" target="_blank">📅 11:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136529">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
✅
طبق شنیده ها   احتمالا فردا باشگاه از سه تا بازیکن رونمایی خواهند کرد .که شامل محمدرضا اخباری و کسری طاهری و دانیال ایری هست.
🔴
باید دید چه اتفاقی خواهد افتاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/136529" target="_blank">📅 10:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136528">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuVh0wBqKvCyzbTQnM7Ua6aEwddxL6J6yNxGlrxuEYEUMw8rFCyDhweX-kfKNiShrFCCubm1HSsIav6_jg04irtd7ISDm4ijJCvpDru2p-l8vcT9eTCw_gV4Jf77czQj6OKDWX4iD3_y6jYz8VEIChKcJo0sJoudruMq-x7ZnAFLYrYKS5WqH6-96yNRUPa0vW4P9UA8LS7V9rDKtfwgzQu0Zjd67mZy5uUnBa__3_GYCcaaAe5eFO2xyiYj8-PqdrwNrepWJ1jBVF5zkIY-FTGKblf7SdOlhlnjNmbTD7JloRpMZnv5_12PKqQTx6AF0HG0ZWpoekTz6qNWd-yt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
خط دفاعو ببین پسرر
...شیر پسر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/136528" target="_blank">📅 10:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136527">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WeNzNtYt7jY_9asW1xSZw_xueCq9H1FuLbBJ93DoXoMNemQqO6Y7k7FMZm1f8jxRd0cje1bO4fbaDQM4ZOp7FauHm6AAZeybyz5mtxGDllCcnNOETtDnvooOcHKtj_M344qQp8gxcn-NwtrzIXZa096qZG6jKfOUfIw8N3yiy_3cedRoeEGXJZ3h8OTABC3QMPryZWp34ETt--mEkx0NEEaRP0bdQqBKCdVyLxzAq2d1BgDq3HW6creCWcY_1_fw2SgvYn-JIRTR4jJxwfmlKmElmhmvjvN8yIE1DOVOKw2yfH9e2Zxv7Ec6kn_vnl7Fb2AT8ZrO-_iBA7qQNCn_og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باراک راوید خبرنگار آکسیوس: یک فروند از بمب‌افکن‌های استراتژیک B-1B Lancer نیروی هوایی ایالات متحده، شب گذشته به ایران حمله کرد
❗️
پ.ن بیچاره مردم که دودش فقط تو چشم مردم می‌ره این جنگ ها و حملات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136527" target="_blank">📅 10:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136526">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyp7FQj5qVsPh9I6f20mxSKDNNCLkQctbrfw-1wEoYT4lVSRx2Qyl6TyRYGrSrg4SxGxcqeNVnrB9PLzQHwI48IiWl-uULRY7mOIhQ12UEyjn6KB1e6hpDFwKcbY7QAfJq6BFh9ngNYOP2Q2L-8CkNYP_IuVeENEZDEkg6yaPLIA0y26XGi6DYYob2Zz7QYtFqA1M-yt9uJ1ZdOWmEWRIaqg1V8tryAAZn641fXmGhi-nCiJxv3gTP0oIf6GBhZBcy1tk8IlwRSFWH40Yj3frlUgwux-WHsezaGdS9vNHhtgM14ifZl89TvL2oh3qoIZc49HrqItnvGJRPmvPSxxQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرهیختگان: محمد‌مهدی محبی در لیست مازاد اتحاد الکلبا قرار گرفته و باشگاه اماراتی پولی بابت رضایت نامه محبی نمیخواد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/136526" target="_blank">📅 09:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136525">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
کسری طاهری و دانیال ایری طی 48 ساعت آینده قراردادشان را با پرسپولیس امضا خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136525" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136524">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
محمدرضا اخباری دقایقی پیش با حضور در باشگاه پرسپولیس قرارداد‌ دو ساله شو با پرسپولیس امضا کرد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/136524" target="_blank">📅 08:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136523">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔹
فوووووووووری
😐
🔹
ترامپ: دستور دادم در های جهنم به روی ایران باز شود  ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/136523" target="_blank">📅 08:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136522">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBr9Sk3RvfffCyN5RJElh3wk8Oj5OvGnqu62RhGVT7PnyQFTWxtN73UMuNNfDEZJXKDCLo9sP19jNSKyxkdyhxNdhNLPmmzUEO5bxEweDlOrHCoq96ORV8lOT1Fu_9exTCzmnRYmESbu_mQJ98vtH9E1jY5BJn4LFKZmXQyf4qlaq-Iqk7bT05uvyyO3KnFtaFaaBnzE2NPZRmZR26i1Cg271uQRVSu_6xJVejZm-im2aI3sVdx2ion_imioN1-yW4qLvEFUADe3b0u0zp5GxAcXp4z0vHRyhfdJ2lmGOm-_2i-tuBZvyPZVkpQFTATy--WB2tXKWRLAJdeAwQ7ExA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/136522" target="_blank">📅 08:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136521">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136521" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
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
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/136521" target="_blank">📅 01:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136520">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tC5ot8M1vSzhwJ2gLq8bCHQAf_MkFjIMibeh7HZN6-Bg3KZuga36zv29Wt1b4HKcIjeDpuEAt3thNB335ukU6nxSsJUYpEOeYW1jFLe9J1x9TDE1tvvt3oRxcXtee6KKFy4VKCfR9T5wZlWJk6GWVXKiyzOyavEIlphLuUrRqtq-mOxmYHRXqTYZfatz_-dEColxVmoyxuhC-4TLNdL8f16_l-eTwKXvttq10O-bt_C8P3uB246BhQjGKbMKnhGyvcrfc_PScQArvpLZWqPpE6Ko01LG2UPOjCKw5tlnU0NlOUmIC1ELfqaiRhUdW9_lesTU3K0pXf6NwmIiTZmIDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/136520" target="_blank">📅 01:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136519">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Js9nMXNuPahd6PUUytugyer9Jq-4RsQkCRzF6xTuAweav2AkPaiCCD1EKswjNyqC3PEjStlaS5pChm9JSRVmAIjCRGa91lje5fEugxaX2Ak1lazTOVBcBHZCmmTGdd2SPSmnZ0rt_hNmkUHQWECQ87rYm5bzfHACp6pUgVV0BvYYOZ7GLOaL58BTkuEqa2M5EBnmiiT029zc9GkeOCpjSnuzDgJjDvslI08844s3ckBuNSSLVc9Qd9v9ih101of6_MSiOrvzZjjr39qipQ2LPWzeVzbyIU51iKzZv2RvV3CeAuBWOA1qSU0nnzdS1PQX9ETgv6qHA4-UmHiOpAhQqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
درگذشت قهرمان جوان ژیمناستیک‌ تهران
🔻
محمدصدرا رحیم‌زاده ورزشکار ۱۸ ساله و از قهرمانان ژیمناستیک استان تهران که هفته گذشته در حین تمرین دچار سانحه شده بود، دار فانی را وداع گفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/136519" target="_blank">📅 01:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136518">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
حملات امشب شروع شد و فعلا چندتا شهر خوزستان صدای انفجار داشتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/136518" target="_blank">📅 00:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136517">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
حملات امشب شروع شد و فعلا چندتا شهر خوزستان صدای انفجار داشتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/136517" target="_blank">📅 00:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136516">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
حملات امشب شروع شد و فعلا چندتا شهر خوزستان صدای انفجار داشتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/136516" target="_blank">📅 00:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136515">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
فوری/ سنت‌کام:
❌
دور جدید حملات از الان شروع شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/136515" target="_blank">📅 00:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136514">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
محمدرضا اخباری دقایقی پیش با حضور در باشگاه پرسپولیس قرارداد‌ دو ساله شو با پرسپولیس امضا کرد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/136514" target="_blank">📅 00:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136513">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
✅
زارع و شهرآبادی دوباره در ترکیه؛ استراحت دو روزه برای سرخپوشان
⏺
مهدی تارتار امروز را به شاگردانش استراحت داده و فردا نیز سرخپوشان خود را برای سفر به ارزروم ترکیه آماده خواهند کرد. در واقع فردا عصر کاروان پرسپولیس عازم این سفر خواهد شد و 10 روزی را در آنجا…</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/136513" target="_blank">📅 00:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136512">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
✅
دیروز در بازی با خیبر، جلالی مصدوم شد و از بی دفاع چپی جای خودشو به دنیل گرا داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/136512" target="_blank">📅 23:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136511">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
یک مقام رسمی باشگاه پرسپولیس خبر امضای قرارداد دو ساله با اخباری که وایرال هم شده را تایید نکرد.
🔴
وی در گفت و گو با قرمزانلاین درباره اینکه گفته می شود مذاکرات امیدوار کننده بوده و توافق اولیه حاصل شده گفت؛قراردادی امضا نشده است.بیشتر نمی توانم فعلا توضیح…</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136511" target="_blank">📅 23:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136510">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
فوری از سپهر خرمی:
🚨
بعد از کنسل شدن تمام گزینه های پرسپولیس در پست هافبک دفاعی، مسئولان این تیم دوباره سراغ محمد قربانی رفته‌اند اما اینبار با پیشنهاد بهتر!
🚨
قربانی از تراکتور هم پیشنهاد خوبی دریافت کرده اما تمایل داره به پرسپولیس بیاد!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/136510" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136509">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
✅
پرسپولیس با محمدرضا اخباری به توافق رسیده و اگه اتفاق خاصی نیفته، امروز رسماً ازش به‌عنوان دروازه‌بان جدید تیم رونمایی می‌کنه.///فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/136509" target="_blank">📅 23:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136508">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
🔴
باشگاه پرسپولیس در آستانه توافق نهایی برای جذب دانیال ایری و کسری طاهری است.
✍️
قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/136508" target="_blank">📅 23:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136507">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
رسانه‌های مملکت: نساجی با انتقال طاهری و ایری مشکلی نداره و اونا در اردوی ترکیه به سرخپوشان اضافه میشن و حتی ممکنه کاظمیان هم در ازای رضایتنامه‌ی یکیشون راهی قائمشهر بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/136507" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136506">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
تیکدری امروز بازم مثل بازی قبلی یک گل و یک پاس‌گل به نام خودش ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/136506" target="_blank">📅 21:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136505">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1Dasmoku19lxLafHko_fzKg8jBPRugdGnRdhGSIs2jCWcS8XtBx0B0wYCDgA4ib8ER-gWuTNcoIWIzKsKQFjpdWhqMREsndHJyuOjB6PnNrmWacNgZCkBaB1WB-GQruzqTHUxl3qm7ZzisxXaWo_WTO-3EnYzBBvXygeG1sCnpAeq-wOtR1oJ9oFc526rjYgtDHbQIdMLf_wJ-m2axVX2qzOw5ldikvnSbpL4nYRgZrGWxbOIqXZD0HFGQijMs5A6godKGAx5S4IJY-48EbuGQJvwWrnlCkP9FlHeXo1WLAtYbvbeg6zNC0V9S1VIP7oGPg_d6DYd0Eny_MwPkpGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
فوری/ کان نیوز: اسرائیل از سوی ایالات متحده آمریکا مطلع شده است که این کشور قصد دارد حملات خود به ایران را تشدید کند و در روزهای آینده، و برای اولین بار در این تشدید، حملاتی را با استفاده از بمب‌افکن‌های سنگین علیه ایران انجام دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/136505" target="_blank">📅 20:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136504">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
✅
امیرحسین محمودی در فصل آینده با شماره 10 برای پرسپولیس به میدون خواهد رفت. شماره ای که سالها بر تن بزرگی همچون علی آقا دایی بوده
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136504" target="_blank">📅 20:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136503">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
پورعلی گنجی هنوز با پرسپولیس برای جدایی به توافق نرسیده است
🔹
گفته میشه این بازیکن زیر بار کم کردن قراردادش نمیره و کل پولش می خواد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/136503" target="_blank">📅 20:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136502">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❗️
رسانه‌های مملکت: نساجی با انتقال طاهری و ایری مشکلی نداره و اونا در اردوی ترکیه به سرخپوشان اضافه میشن و حتی ممکنه کاظمیان هم در ازای رضایتنامه‌ی یکیشون راهی قائمشهر بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/136502" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
