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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 17:17:09</div>
<hr>

<div class="tg-post" id="msg-136596">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
✅
زارع و شهرآبادی دوباره در ترکیه؛ استراحت دو روزه برای سرخپوشان
⏺
مهدی تارتار امروز را به شاگردانش استراحت داده و فردا نیز سرخپوشان خود را برای سفر به ارزروم ترکیه آماده خواهند کرد. در واقع فردا عصر کاروان پرسپولیس عازم این سفر خواهد شد و 10 روزی را در آنجا…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/SorkhTimes/136596" target="_blank">📅 17:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136595">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
فرهیختگان: محمد‌مهدی محبی در لیست مازاد اتحاد الکلبا قرار گرفته و باشگاه اماراتی پولی بابت رضایت نامه محبی نمیخواد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 517 · <a href="https://t.me/SorkhTimes/136595" target="_blank">📅 17:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136594">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از تسنیم
🔴
استعلام باشگاه پرسپولیس از فیفا رسید و هیچ مشکلی برای جذب دانیال ایری و کسری طاهری وجود نداره و این بازیکنان ظرف امروز و فردا قرارداد شون رو با پرسپولیس امضا خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 728 · <a href="https://t.me/SorkhTimes/136594" target="_blank">📅 17:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136593">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه، حتما عضو شین و‌ چک کنید چقد راحت سود میشه کرد
😉
✅
JOIN JOIN JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/SorkhTimes/136593" target="_blank">📅 16:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136592">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpxWqfCkPfPBB2aoEapclFWA4ShtwVbJe_1uQlDfKJVkG2ZszGLXp38gETGRWOOAopR7TeCEdl2REinUpb8pr2WkhKvUPR43nERJOVwQsiRhDZRbG7NyXO1-Aq07I9vAivwbEICLu-dDGxDuSTpuWWvfTdSlaYI0W2pNayKz8sMorC5tdhwd7xoF_jBP7m8n7zZ-LKAyYaKvzKj6x2ImEqDzpesq8dV_Q1bgsS5VvTRRxr_ZQs2g9VBTMHPozc3rrIWzG8Ag6SxsdhNVZaEdV3ClFWLqJR-WCGyaiXkFX_WGDyAWgJoLqBSuJHuBA9GRUAytFVXiBbreSKzmA-u-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب حتی با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🤷‍♂️
@PeakyBetBlinders
@PeakyBetBlinders
@PeakyBetBlinders</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/SorkhTimes/136592" target="_blank">📅 16:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136591">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
ایشونم از روستوف‌ روسیه جدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/136591" target="_blank">📅 15:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136590">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPS11knlTwFFmObmH_Sq0e1t0mAV-9QI0gKY-Bnua9vUnEQYVvJF_vTjJ9Yqq6uFwxrhz1NQFwtYZpBodDdB_52j1XNaGlW30sp7rSc09lKRtXUHkb4A-Hr0xqQlWKAOgYpgulq4DuiKGG_xgPmhjJZJuN6D9xlLnRcEvKDSQK0f5Op49nNMvdMAKf9tX8BthTRLv6zSQHMLVKVfG3LvB6G-7zczB4D70awYptGkdnXYw9fgrFWmpeQjfrteBBeQD92bU0wObuWVsxyACEiuOI1QVtLVbTtoOwdbQFl_pY7qFdqB-0Hpfcy3G2FU-Qyv3LC8gtoWaeciFlxSapWHkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایشونم از روستوف‌ روسیه جدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/136590" target="_blank">📅 15:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136589">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/136589" target="_blank">📅 14:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136588">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❗️
❗️
درویشی وکیل ورزشی :از نظر حقوقی انتقال کسری و ایری از نساجی به پرسپولیس خطرناک و ریسک بالایی داره..
🤔
امیدوارم مدیران استعلامات کافی و گرفته باشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/136588" target="_blank">📅 13:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136587">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
با اعلام ترانسفر مارکت رامین رضاییان بازیکن آزاد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/136587" target="_blank">📅 13:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136586">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
✅
پیام گلر یک پرسپولیس و ۹۹درصد گلر یک ایران در جام ملت‌ها است. برای چی باید اخباری جذب بشه که خودش رو در سطح گلر یک می‌دونه؟ که چی بشه؟
❌
❌
ضمن اینکه امیر رفیعی هم گلر مطمئنیه. چرا باید الکی چالش درست کنیم توی پستی که اصلا مشکل نداریم!!! به فرض جدایی رفیعی…</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/136586" target="_blank">📅 12:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136585">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❗️
پرسپولیسی‌ها نخستین جلسه تمرینی خود در اردوی ارزروم را در سالن وزنه‌ پیگیری کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/136585" target="_blank">📅 12:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136584">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
✅
محمدامین کاظمیان بخشی از قرارداد توافق پرسپولیس با گلگهر برای جذب پوریا لطیفی فر می‌باشد
🔹
محمدامین کاظمیان + حدود ۸۰ میلیارد رضایت نامه = پوریا لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/136584" target="_blank">📅 12:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136583">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
شنیده ها:قرار بود دیشب از پوریا لطیفی فر رونمایی بشه ولی به خاطر بازی تدارکاتی گل‌گهر، جلسه لغو شد و به امروز موکول شد
🔴
امروز به احتمال خیلی زیاد، پوریا لطیفی فر پرسپولیسی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136583" target="_blank">📅 12:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136582">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🌀
🌀
امیررضا رفیعی این امکان را داشت که قراردادش را به‌صورت یک‌طرفه با پرسپولیس فسخ کند، اما فعلاً این کار را انجام نداده و منتظر است تا باشگاه ابتدا گلر جدید جذب کند و سپس از جمع سرخ‌پوشان جدا شود.
⏱️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136582" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136581">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCnrj6L6hA8qyNYO1k4PCW93s0koUXeeF9Rek94LVKNuD1R7xLvh5h9w6MyLP-KVfQq3xFHSotRRmPQ5z_2sRVnTtX-zKRmCMtXink5PQI6WxrR0LW-lv2OPw8zku6X5Gmxf8rgVpyBe3Gm3QlaJmdIYiVjO3XwgDvHp05r-qY5A9qGZQ489Hil6MgQl2ok9iE5grGzf63Lfl7Z49Y1ZwUvyE4gyLPkAICx0ku9i9ZE4z-OSWBIlqSWu2jYsu8nr46ucDFmYR8atnWm3AjWwT-CK4Tm5jnFGM75FMKtQxnIqXhvbmWPL1OOSnjFx2QXeQ-pLQl-jqE0tn-I6v_k2hQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/136581" target="_blank">📅 11:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136580">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/136580" target="_blank">📅 11:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136579">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❗️
❗️
هنوز قرارداد اخباری، ایری و طاهری امضا نشده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/136579" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136578">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136578" target="_blank">📅 10:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136577">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/136577" target="_blank">📅 10:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136576">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JB_3l2CHDFHbVp9VoPlO9D24kR8mgP8gj4mUy4xTAWKJJ5Fj52lFmxk1LWuWAyO0lpNu4P-J8UUtCq7EBdWNRmVKrol5c0BMdG4mv5nHdpeY1OZpeUUF6m3UYypEaHXtJ5V-WPZSLmnJtoPmf4NqNMXu9QRHZm_bxhWZ6H_qIAD_iHFvVVWvUPYsnNF8lAev0_M_lzJNtoh1HUe12GoKYEkmQep-F7A0_ZZ4N2LrEBpxl-1yTgbEQ8lA_eAdwJ_tdBflTaHCzgEl92LS5yaKr2aHiSK6tcRVFy-GOoj4TIwsm2SMgEd1Iwdb5HXvGbpY2DrwVrxhG1ylNvXU56bz7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
با اعلام ترانسفر مارکت رامین رضاییان بازیکن آزاد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/136576" target="_blank">📅 10:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136575">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
فورییییی از رسانه برزیلی UOL: جنگ بین آمریکا و ایران مستقیما تو این انتخاب نقش داشته و ترامپ در انتخاب داور فینال جام جهانی دخالت کرده
❗️
رابطه نزدیک اینفانتینو با ترامپ هم به عدم انتخاب فغانی کمک زیادی کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/136575" target="_blank">📅 10:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136574">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlQmV4AqwAyLoL6mQfROuvSyEvSVujX50k-q-wGsZbgsDtd0wjM7og4n9I136zdqqE-f98vHfszqK5pZ6TYfznUPAq1LTVTECHpHYTeY70badTwqZGl84cP6eImqy8MNJoFueVZTbsrPURzE4YPu3deQm94Av9CHhrw-3W4TzxK_hTGcNRT2c18ETxE6pvIm9qAohTPlVLX54rwKoMt4bqyK_DTSlM6FOkIdC_fm0J2Fc8tID1HT5DtuT_O1Asw7xFS_o1aF2GLMDv9Ny8y_pUPLcV_wAq0nVM8CukV-hql2uQOHTS5I-g8O9qoDBAtJUVCLcBjyj2OI-_23QgV9ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تارتار در گفتگو با پیمان حدادی از وی خواسته که هیچ‌پیشنهاد خارجی را برای اورونوف بررسی نکند چون این بازیکن اصلا فروشی نیست و فصل‌آینده ستون اصلی ترکیب تارتار خواهد بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/136574" target="_blank">📅 10:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136573">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🫥
🫥
شایعات: محمد قربانی در لیست مازاد الوحده‌ امارات قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136573" target="_blank">📅 08:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136572">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووووووووووووری از هفت ورزشی
🚨
مذاکرات پرسپولیس با پوریا لطیفی فر، هافبک ۲۲ ساله فصل گذشته گل گهر مثبت پیش رفته و اگر اتفاق خاصی رخ ندهد، لطیفی فر هفته آینده بعد از امضای قرارداد با پرسپولیس راهی ترکیه خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/136572" target="_blank">📅 08:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136571">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136571" target="_blank">📅 08:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136570">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/136570" target="_blank">📅 01:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136569">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOyLskX6gkohgrb190DwxnTDZPX72Inm40HDfWaHGhcHduQNG9smQpoDcfut6MoSJ0i-QU5eV5U-HNeBhQ0s4U2dGR_kPm2uuTjd9NjYB3kYTrtzsUdKwD_y4K6IO1DDRYLhuER93bXaERCSZ6jaz1xWFf5btIl9tnb5_f9WFAGfjFfVAUCx8bPNUlNibtStZJnroUOzIhEasxpskWPjw-P0t4LtEML7eMW8MIHruMLXP_OQwrPiDVOM3IaMH7kL5gLWRff35fnglI-MtxxwRcHUQucMDt3013Nw8RPjb39rL7djsAzjQxqAs3KGwMh5mfNJf2QBxPoyoGBhOdVaBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/136569" target="_blank">📅 01:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136568">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/136568" target="_blank">📅 00:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136567">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136567" target="_blank">📅 00:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136566">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">💢
کاظمیان + رفیعی میرن گل‌گهر پوریا لطیفی فر میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/136566" target="_blank">📅 23:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136565">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
شوک به استقلال: آسانی فسخ کرد!
🔴
یاسر آسانی با ارسال نامه‌ای رسمی به باشگاه استقلال، به دلیل پرداخت نشدن مطالبات فصل گذشته و پیش‌پرداخت قرارداد فصل جدید، فسخ یک‌طرفه قرارداد خود را اعلام کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/136565" target="_blank">📅 23:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136564">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❗️
❗️
زارع به اردوی پرسپولیس اضافه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/136564" target="_blank">📅 23:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136563">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJLp5yeqSijwhtqYtWOazdzkCIg4Rrxbi_TEiLCsbS7ECUexuudzJYoN8rOkGv11tocOadiIv3nQ9Xdwk9IYUAls-0GKX8dCg0WDfxtdT8Zx3fwI6lLjHgA-sFGg56_7yC9gX-Yz0bcK1Z95eaNWyZVroXWYDEwDp9VGgQnncSzp9DdBdX4_75A0s03zFLPf9XUl0Cqirts6pXJgl6hgHwIf-3a51-w_brYOWxB_IGRq74GX2K_zOdfvfwdlku8NiS7c2J9GDn4ck3OwcENlwNpN2NOFGGepgJ3bFr0OjqfZ92egh51wc4bAzdEqJrGU4TXQtPEFi4gdJoG-EdjkIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
پرسپولیسی‌ها نخستین جلسه تمرینی خود در اردوی ارزروم را در سالن وزنه‌ پیگیری کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/136563" target="_blank">📅 23:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136562">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
کاروان پرسپولیس دقایقی قبل وارد ارزروم ترکیه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136562" target="_blank">📅 23:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136561">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
✅
رضایتنامه‌ی قربانی خیلی سنگینه و کنسله/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/136561" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136560">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
رفیعی خودش قراردادش رو با پرسپولیس فسخ کرده و حالا دستش بازه هر تیمی خواست بره. احتمالاً هم راهی گل‌گهر یا شمس‌آذر می‌شه و اخباری جاش به پرسپولیس میاد.
✅
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/136560" target="_blank">📅 22:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136559">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
#فوری |ترامپ به شبکه 12 اسرائیل: من در حال بررسی امکان انجام حمله‌ای بزرگ‌تر از هر چیزی که در گذشته شاهد بوده‌ایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/136559" target="_blank">📅 22:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136558">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
فوری از سپهر خرمی:
🚨
بعد از کنسل شدن تمام گزینه های پرسپولیس در پست هافبک دفاعی، مسئولان این تیم دوباره سراغ محمد قربانی رفته‌اند اما اینبار با پیشنهاد بهتر!
🚨
قربانی از تراکتور هم پیشنهاد خوبی دریافت کرده اما تمایل داره به پرسپولیس بیاد!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/136558" target="_blank">📅 22:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136557">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/136557" target="_blank">📅 22:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136556">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zz7BcvlWiUIbIlhrNtkRHxvGWC5G12AALsUsHcG5QMgITdwa4FpaJ0MYderc0yLbOUnoXZV1AdXZG4CaT_ZYBism09qt8pJ5mSKphU2cBsZySZ3IJdcQF4nxuzwEcHRnf3jMOea-PnCk00ih21SIWNBa3tpsZq97VgLVfIeP4qhWl8KAHHXrDM6SChKZdpgnxEV9SaDMyKHkrHyeUzkmO9ez3OVWoVMhvI-LzqKs3vWL4tqicaZrLOJp-DxbOqQQaSTgD7k9kjaqNbymB97nL7Bo-8aLcsqkTKwJ367Jr8-huOsbocHxRUQm7VwDbm4V90GzzAk_p9RcFfZ9Rp7cQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کاروان پرسپولیس دقایقی قبل وارد ارزروم ترکیه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/136556" target="_blank">📅 21:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136555">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
قاب ماندگار بازی پرتغال - اسپانیا؛ دلجویی یامال از رونالدو پس از سوت پایان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/136555" target="_blank">📅 20:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136554">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
مرتضی و کاظمیان با تیم به ترکیه نرفتن و جداییشون تقریباً قطعیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/136554" target="_blank">📅 20:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136553">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/136553" target="_blank">📅 20:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136552">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/136552" target="_blank">📅 20:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136551">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WIsrJARmnw2UCM-GTDWPmanfZYBBzjVLbO9g7CMvcr5kJQfUn7NDAbGmd3dp-S-2xnrw8uS3RZ5xAf3GmFiMDVdjiBmG9Qps7CLpxOUoc85X-GHoeYQbkltP0tSjV78SXJACDUdqaobpnLA7BfEFk9GURQelYeZpOcZFaz8ubcrlPS1GKfyvnRWI0cpBDytvivNWW_ZuH8WA_U90m46R8hIwgy_GOVBcIKt28cxTjIucrSI-AljYb-4mXpprq4SIOhkh75S9twB--nJ55thN4zQOPh2gYnEOaS2kcUmdUL3TOyo9xI7nHPJ4d6NW2iHQ6rEDJPWq1TP7qLaSahgX9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136551" target="_blank">📅 20:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136550">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🥇
🇹🇷
تیم فوتبال پرسپولیس برای برپایی اردویی ۱۲ روزه تهران را به مقصد ترکیه ترک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/136550" target="_blank">📅 20:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136549">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136549" target="_blank">📅 19:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136548">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpQtX4px-ggy2rBz70m2y-GdTVtXHOrpxkhwoaOgUoN5KikcqEF5mvHUrJ5Po-2qRCNGkRNSvsn5i4pPWyiFVIPxTEtVpaBgXrIcgD4A4vpfWiIcZRpLK8LhBce0KLSCMLH_ougyU_S5apt_KUDLXCZ7i7pU0n7RHgED7ymviv57fPEmhOXdFkySss2_Q6qbwE1jTmLeeWx2Zc5oRT8mG382eaVLVh0yUUISZd3RcQ6RCek6y_4CIhQ2HXYZqVyoYbhFkUgFBNwxwlwcGAyZpsw-XkzVfg0XBBN0TJzLlK4bZWXtvMXNWYvW6LCAGRFFhu-mbJEPDBNBYyStfeUugw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/136548" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136547">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❗️
❗️
هنوز قرارداد اخباری، ایری و طاهری امضا نشده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136547" target="_blank">📅 19:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136546">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔹
فوووووووووری
😐
🔹
ترامپ: دستور دادم در های جهنم به روی ایران باز شود  ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136546" target="_blank">📅 19:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136545">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8Lc8Jy_IpotmG_0rxzn0pk_p2AjY9O3wSbWsik5yrj9h6gjPDPXIJ7QWTcxNtuc9QAPfcu6CWlVtiiMxkkjvvBi4F2fQQkIT0HPZXuQbUeokEC3DqYMc4tzxF6J-cQ3BkCuKmHda8zphvL-xyhF9BuR2n_2SUeV9Td6eRmpByesMBTdgu5HXN4ZpEn8KOxkOMIp_e7-rsIVz9UzebHQsT4WqfXqHrH3iKOtOCWB38YhGuY1KCBFrQ8oGsSD7KXe8rH94jiZ5P1IwsHCrIx8cANo_naS3aueh51t0nHX0pTyqR19vKe9wl58vUQ8f5uHxWFByeQi4iLbrw8wCwY0GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیپور تنها بازمانده نسل طلایی برانکو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136545" target="_blank">📅 19:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136544">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feaf2d5596.mp4?token=JOKRHxwQK4-CItXTBLJFidnoyFzFh65VxXHgOfLe5nU-LpZvOg0q0hAmlrRMUoGZfRCG8jTjQp0bJvZHwQh3AysFmMiAFapOXSaGdPcRyJT0QjlEF2rrJgoxHjVyQDo5ivvqRDJdDhJ-1ovAXTuaiE6MOS5CQ9jjFqDB2MDOFmaDQ9wBog_jgLlcwikaMql0Hi8E23kndVARP_uoFbotGNzih64qDjqUCVwf_aAWPa1DoqVQ5_hRXvoZNOGme43rYXmU8_t4R3rWArT2EX9tgKul28lPG2bkWgLsJNkQbkAiuwkH_yY55rTt--Bw8dxmLN5y-L2eMBpHg0A6oWQhAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feaf2d5596.mp4?token=JOKRHxwQK4-CItXTBLJFidnoyFzFh65VxXHgOfLe5nU-LpZvOg0q0hAmlrRMUoGZfRCG8jTjQp0bJvZHwQh3AysFmMiAFapOXSaGdPcRyJT0QjlEF2rrJgoxHjVyQDo5ivvqRDJdDhJ-1ovAXTuaiE6MOS5CQ9jjFqDB2MDOFmaDQ9wBog_jgLlcwikaMql0Hi8E23kndVARP_uoFbotGNzih64qDjqUCVwf_aAWPa1DoqVQ5_hRXvoZNOGme43rYXmU8_t4R3rWArT2EX9tgKul28lPG2bkWgLsJNkQbkAiuwkH_yY55rTt--Bw8dxmLN5y-L2eMBpHg0A6oWQhAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
استوک صورتی با کیسه فسخ کرد
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136544" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136543">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJppHVsxKkDspL6Fa1MCPZtBysH042Q6_LZIMR7QeqynPxCothL8cads0IduT5-Zzt10boWB0ZkAGM4Rxj05I6mea5TKEoDgdFc-gAs9dPuTXm63PSAYicwJ7d-x2XSjXRSm2qSBI5_deRtnxO102L-FjGyN_ConyWljYJWJ_uOoxslv2nwU5xbQVOqCQgtJTQSHBGk5cjHUut6ePPJ7cpvj4wytn9HJypzTGejLgpgFPaqAJzew5XjMOdAwhI7_zbhpC32GYVcDTZ-hF7J761v4ocozoebBKDfJM_DBM5yKs1JIpyDXA54uk67Nux6H0PpcxFoTfmJvca50M-tEqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از تمرینات خبر رسیده پویا اسمی کاپیتان ۱۶ ساله تیم نوجوانان یکی از خوب های پرسپولیس بوده
🚨
این بازیکن در این سن با این فیزیک و قد مناسب شدیدا آینده داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/136543" target="_blank">📅 17:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136542">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwBigl8Gid7PfnYhnjTCF9Jr-3pmDTJqJ8k7wLX_REjwskkS_FLB6vnAo-yQZYGyD3mK2IUTaDXpy9IKX47WDTckYLNbicXq6OQrKM18P0UNKP1YTRzBo9QBrWh5uKAwCrYTaCIkq_FcJBd93Zmoc_mzR9EsDL_PxuFrGgn4XZ9H95wWHDkW_JavsNObmD_w_oAu2iza67ql_2KdaX1bVtoCP4mO6dKsnSmwvyAuB8Wwdoqmt5yS6pejaVNI-MvwQMMLQikb4MLBiFQkuBFK3sKjZM2OPR6OXZ7bkMq_VQMNQUudlpT915JXTlFk853dO1z1vwELp5lDVBAp80q-QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
🇹🇷
تیم فوتبال پرسپولیس برای برپایی اردویی ۱۲ روزه تهران را به مقصد ترکیه ترک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/136542" target="_blank">📅 17:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136541">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
✅
طبق شنیده ها   احتمالا فردا باشگاه از سه تا بازیکن رونمایی خواهند کرد .که شامل محمدرضا اخباری و کسری طاهری و دانیال ایری هست.
🔴
باید دید چه اتفاقی خواهد افتاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136541" target="_blank">📅 17:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136540">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGIRyGKXNtEqCZRGje-rC893Lnar_lPwQxvgdZwaLLoirmxyLSrJ75qoHJYiqhl5XipnCNB6nKrfJRTGhwi-hQ6GnwtiCs9uAL45JRHYPJ_jDT5X7fxFIs5g13bSJCnIl-62jZd_ULT8ONGHuCPwEQx010rHIrgzkvm-Gh2ov3nyQTp_IJdSw3tU6eTFpFzedkIbngr3WJCspOpNzNSJUr_aZbxGsAjUWBTPT21Euu77zIBHW3Y9H1UegEB-usTpJ3VmG_7Dv9GbWkskaOij1rJ2FcpMdsUAJzXW-371RF1WtNv13mXyIghxAtxNc5AseL0fEbH3ahZkBN3JqL6itg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تیم رفت ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/136540" target="_blank">📅 17:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136539">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/875cf546b8.mp4?token=FaDh9riANJIrLryQYWhH1RyXBCQZWhEhWKp5jcrJGEJFjEtx1FOewgg1FGaMQ4a-PWyfBe8N8u14Ez7uNTaSqBdmGDjJr0MLRkMFbLjB8oZqEkpHBVmClJk38fBP7m5YrQyIoO94X-SxrxcrbDWwdiXQxyeC2BcluPRbHv7Dn6tg5KTrS1BvqvIEvk9rC4CcUncHSiaQt1CgD1Q5jmbljjdci56_MEH5ljXJa3FfIb7gnlOOagjbMahCGGU3kr3YWEycIbh53yirphjeeJh7j2exo2IltBe2vkSQPhMOjpbGb5ed5bF3SbkM5GIfAOjHEr6d_1WXS7k5rikzxFtFgjFuWIvtAk81DfWVsVeSevly4b2qGYDswz_PWnem0NPlzCOpjZ5wLzZdi_Y-08Xzzbd-L-mq6egoK_JrgWtOO2nQHNyA-Qb-cStA5hIU28rUjaiVSkRc-zMqHHcfkklGQMnoYw5Je07Bnez4hPZ25mcpZRQ6_V-t8Qz7oOW2jCMwXCwx4K-k6lJlZIn91fjcPUNpgk78MRe-6fWISvtSKR18Qf2OCvJ4hxP3oyq-i1lM2g1wZ3VXnnuRYG9yuSe4_zVZjTx5R7TON8hs_-HX75cSiUDjMuzCd9pW3I0pT4T7xyo_G7DDP-XplZbGOBrhyOHNGWRug4saLUYpsLrYJcI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/875cf546b8.mp4?token=FaDh9riANJIrLryQYWhH1RyXBCQZWhEhWKp5jcrJGEJFjEtx1FOewgg1FGaMQ4a-PWyfBe8N8u14Ez7uNTaSqBdmGDjJr0MLRkMFbLjB8oZqEkpHBVmClJk38fBP7m5YrQyIoO94X-SxrxcrbDWwdiXQxyeC2BcluPRbHv7Dn6tg5KTrS1BvqvIEvk9rC4CcUncHSiaQt1CgD1Q5jmbljjdci56_MEH5ljXJa3FfIb7gnlOOagjbMahCGGU3kr3YWEycIbh53yirphjeeJh7j2exo2IltBe2vkSQPhMOjpbGb5ed5bF3SbkM5GIfAOjHEr6d_1WXS7k5rikzxFtFgjFuWIvtAk81DfWVsVeSevly4b2qGYDswz_PWnem0NPlzCOpjZ5wLzZdi_Y-08Xzzbd-L-mq6egoK_JrgWtOO2nQHNyA-Qb-cStA5hIU28rUjaiVSkRc-zMqHHcfkklGQMnoYw5Je07Bnez4hPZ25mcpZRQ6_V-t8Qz7oOW2jCMwXCwx4K-k6lJlZIn91fjcPUNpgk78MRe-6fWISvtSKR18Qf2OCvJ4hxP3oyq-i1lM2g1wZ3VXnnuRYG9yuSe4_zVZjTx5R7TON8hs_-HX75cSiUDjMuzCd9pW3I0pT4T7xyo_G7DDP-XplZbGOBrhyOHNGWRug4saLUYpsLrYJcI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
علی علیپور: از آقای قلعه‌نویی تشکر می‌کنم که شانس حضور در جام‌جهانی را به من داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/136539" target="_blank">📅 15:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136538">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
فوری، حمید مطهری با جدایی ابوالفضل رزاق پور، مدافع چپ فولاد خوزستان و پیوستن این بازیکن به پرسپولیس مخالفت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136538" target="_blank">📅 14:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136537">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/si29LQ4zLaiHygee9wYcQgZcWwbGxKWCJdlmOp3lWj6n3KPkPXXPB5zWuu3f497nRtPO8GKJdRATiRpSXE1NE4MRZr-5k1-22FUiAFQH_dnVrkxKAwxoiMACpY8uDq7LkXlS3hPhAeHu6hH6D7Ton6pGlksQ0akLaUoj80nuKdgoIEIQBbsffMrCDqs8o6sApCnS5OLxY1mHNoLMFgB061uctxs2wvoCFQR8dHjSVfqPc1pszyniz_5owul6_7to1jeiJeFr1xyBrKUZUbYiql-F3Zla8Kxb44UVk_btJ9Bpsl7vIJdWT1erQSKwDr1F2oLo7J6eYq0LyfdNwetGRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پرسپولیس امروز برای برگزاری تو این کمپ زیبا و
اردوی ۱۲ روزه راهی ترکیه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/136537" target="_blank">📅 14:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136536">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
میلاد زکی پور، مدافع چپ سپاهان پس از قرار گرفتن در لیست خروج محرم نویدکیا، به پرسپولیس معرفی شده تا جانشین میلاد محمدی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/136536" target="_blank">📅 14:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136535">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
فوووووووووری از ورزش سه:  دانیال ایری و کسری طاهری از نساجی به پرسپولیس پیوستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/SorkhTimes/136535" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136534">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
فوری، حمید مطهری با جدایی ابوالفضل رزاق پور، مدافع چپ فولاد خوزستان و پیوستن این بازیکن به پرسپولیس مخالفت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/SorkhTimes/136534" target="_blank">📅 13:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136533">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
شنیده ها: محسن خلیلی ساعتی پیش با حمیدرضا گرشاسبی برای انتقال ابوالفضل رزاق پور دیدار کرد و قرار است در صورت توافق شخصی با بازیکن و واریز مبلغ رضایت نامه این بازیکن راهی پرسپولیس شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/136533" target="_blank">📅 12:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136532">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
✅
با نظر مهدی تارتار ، محمدحسین کنعانی زادگان به عنوان کاپیتان اول پرسپولیس انتخاب شد / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/136532" target="_blank">📅 11:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136531">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
مخالفت AFC با درخواست فدراسیون فوتبال ایران؛ گل گهر نماینده ایران در آسیا شد!
🚨
🚨
کنفدراسیون فوتبال آسیا با ارسال نامه‌ای به فدراسیون فوتبال ایران اعلام کرد گل گهر نماینده کشورمان در لیگ قهرمانان آسیا ٢ خواهد بود و در خواست فدراسیون برای حضور چادرملو را نپذیرفت.…</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/136531" target="_blank">📅 11:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136530">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
✅
پرسپولیس انتخاب کاپیتان را به تارتار سپرده؛ احتمالاً رقابت بین علیپور و کنعانی است.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/136530" target="_blank">📅 11:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136529">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
✅
طبق شنیده ها   احتمالا فردا باشگاه از سه تا بازیکن رونمایی خواهند کرد .که شامل محمدرضا اخباری و کسری طاهری و دانیال ایری هست.
🔴
باید دید چه اتفاقی خواهد افتاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/136529" target="_blank">📅 10:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136528">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iC2WCjrfwHxysBzl54Qap5zQgFgTtG6lprUkZpssyPHe4gq3g5ZepYAot8fyplXwJ2jx6JTJL6To0SqoojIV6DzhFzsHb8A_4YZsrFScHj_OysXf3Tl6aXI3CVJYJkm0UU5iPNOjhKzp6zKcpwGfOiS8Jbj1v0w2HXN4mUxf7oj3zyifcrn7m4nJ6Z9G8-npcBSOBqLS89DdP9QzzsSVqqlESs1HIZD2LsRu1b1PW9n-lvFH6H-Du38L0yb_hQQWGV5XXb9dh0jUcfPSMwFSXRLSLSZQDUNKWchsIX5mY8UQUM9WQEbcPDoIlSY8yoLS2abdiKNyIdAybgTu4qbJWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
خط دفاعو ببین پسرر
...شیر پسر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/136528" target="_blank">📅 10:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136527">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/El7NlXLITPKbi34W8sG3dhjqfYRxSZsuJJFKTrzqY9jWaBE_xDnBNA-Q85YnFOQiCuWEOAMtQUEVp5MZAkpCeznZWFWasl-qP0NH73lOyAiQ-LlvLn4N_K1Tq-ooCmoGypGpbBjgZQhO6TVYM9kCe6nbvoCyZUFedOXT8UFkC5tQ3Rlvzb5IKw5Z7Y-Fb9XMCKEbUI8HEJlMmzTtLwNQe2z5V-085CDwm5n66EbOL4shSfdRUsY43PleKN8c1ardMeVDLnF_BZjgoyE_BJC7wxqJsBKWZwN3KhbU5XmHQEl5VeSfA8kTzUO-toyFqaAWZfIcLrKXFAXvRgGvaPkfqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باراک راوید خبرنگار آکسیوس: یک فروند از بمب‌افکن‌های استراتژیک B-1B Lancer نیروی هوایی ایالات متحده، شب گذشته به ایران حمله کرد
❗️
پ.ن بیچاره مردم که دودش فقط تو چشم مردم می‌ره این جنگ ها و حملات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/136527" target="_blank">📅 10:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136526">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQinHRPYvGQeUnuk7uw1HSYHqDHvzd4tfxe_if-w7-VUEFdWmWL1cvS7fj0G2Expiodoo2aGmfx6dddsEPaYMm6jWEDMHv5dNERQwhyS2RZAJJKERM7vLs7wGeBG9UKCEIb4IQu7Fu-sqHXzIvmNTavTz3wQBvd8oBRSZemIILcttUZzmy3LTVdHSN6CvnEQ8nfhEsq5WiUbPidFmNzyL6JtxwcuseQZtD-Gf-n2uq_la06enTs5CT53okQM-gKRbNr7Z6mklpJk4BqbEYev_HDo8iTXpZFcVfVMxQuH4axsgsvCxggXCnAnsbMaKzKjQUlZSontSWVACDADOIrPJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرهیختگان: محمد‌مهدی محبی در لیست مازاد اتحاد الکلبا قرار گرفته و باشگاه اماراتی پولی بابت رضایت نامه محبی نمیخواد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/136526" target="_blank">📅 09:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136525">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
کسری طاهری و دانیال ایری طی 48 ساعت آینده قراردادشان را با پرسپولیس امضا خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/136525" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136524">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
محمدرضا اخباری دقایقی پیش با حضور در باشگاه پرسپولیس قرارداد‌ دو ساله شو با پرسپولیس امضا کرد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/136524" target="_blank">📅 08:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136523">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7rNyhzD2KHIakwKd9u1nOS2Ujth3cVDMZWmNqDbpW6eHVx0I6PDJscCOihw6taMgfsT-8DWEPPlJsBPZnVGA9N9z3FDJcz4jEkcsW6O0efOELQVFjtFwJl6qz6Nublby4Y16zAMuvlH0BVhz2gie4zfxBYwmCpHIcp9Oi_LQs5S3kYhinBIMlH1Ba9MlcpuqnG8cEGO09zzz2aO0OhJSzC_AZfgLLCRL98p2LBb9QwvfLaDZZtcyGuc9-NqP3rNkRqmblYHrYsXXJ6OusalEDqnJhkWSZ2g3ya74xpHNVHrK0MRf8-y66l826Qkc4102Pwy5S3Ck9ARqLiu1hMoOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/136522" target="_blank">📅 08:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136521">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/136521" target="_blank">📅 01:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136520">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spt7LhgkToiUrVDtLFGvOzJB2zhv-2DrY2PNkFDPs5IHE3nI2aiF-j0WkQWPGz1mkwcirUu71OwiU74XEgzYZNDtgouwXTXqpgRaLswBMKxyVeFn-zszDO2zTmYF0DRgZrsX9ZyUIvXFxIYT11EJkFRnSEoWkOKHJa3bsHErvneuNg0DiOAMuxr6HRwFN86w1M8g6fz9v9kjoJE0CqUokYyd6rAlJZ2QwmSoe50kZweknt70V1i0zzq2IXwVHgriXVoiA0CjCyon3i0gkYLvsy_Pz18uYYhC_lmX0gA5ENTybjjRjPHyVFwghtHxqfxZvCqsz2RcFuMipYzbACZEFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136520" target="_blank">📅 01:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136519">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Edoq5xu_WrfITyTlVjeTLZYfyxJYAUNQ0n3vnAC0L0IDFywE5LPKgu45gp3d-GDuEA-8WkDmWwE6lEFZf0rK6_rka29UAIO2ptaLnEKe5YMtSVjR5NB8dzU0RRRdXZ5CEABw8Ct523KLX00eQB60i6455tzpnIkJohOk48DtUoqONGGlxqpuBEir0NBxM2T2ZOUsyik-lFZUKreXnNQgDVIk0gAqXl7nwqAzITf1rq1EBbRdhZWskZKuUnZvB01yABamLNsTqGc1lFHTeUWtvKO9SzczzQ7OU0vNOv3o_FlKqaxaVe3hWLnla3xrqQVIVhGuQlYjEYcyEW77HnCtmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
درگذشت قهرمان جوان ژیمناستیک‌ تهران
🔻
محمدصدرا رحیم‌زاده ورزشکار ۱۸ ساله و از قهرمانان ژیمناستیک استان تهران که هفته گذشته در حین تمرین دچار سانحه شده بود، دار فانی را وداع گفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/136519" target="_blank">📅 01:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136518">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
حملات امشب شروع شد و فعلا چندتا شهر خوزستان صدای انفجار داشتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/136517" target="_blank">📅 00:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136516">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
حملات امشب شروع شد و فعلا چندتا شهر خوزستان صدای انفجار داشتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/136516" target="_blank">📅 00:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136515">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
✅
زارع و شهرآبادی دوباره در ترکیه؛ استراحت دو روزه برای سرخپوشان
⏺
مهدی تارتار امروز را به شاگردانش استراحت داده و فردا نیز سرخپوشان خود را برای سفر به ارزروم ترکیه آماده خواهند کرد. در واقع فردا عصر کاروان پرسپولیس عازم این سفر خواهد شد و 10 روزی را در آنجا…</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/136513" target="_blank">📅 00:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136512">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
✅
دیروز در بازی با خیبر، جلالی مصدوم شد و از بی دفاع چپی جای خودشو به دنیل گرا داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/136512" target="_blank">📅 23:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136511">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
یک مقام رسمی باشگاه پرسپولیس خبر امضای قرارداد دو ساله با اخباری که وایرال هم شده را تایید نکرد.
🔴
وی در گفت و گو با قرمزانلاین درباره اینکه گفته می شود مذاکرات امیدوار کننده بوده و توافق اولیه حاصل شده گفت؛قراردادی امضا نشده است.بیشتر نمی توانم فعلا توضیح…</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136511" target="_blank">📅 23:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136510">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
فوری از سپهر خرمی:
🚨
بعد از کنسل شدن تمام گزینه های پرسپولیس در پست هافبک دفاعی، مسئولان این تیم دوباره سراغ محمد قربانی رفته‌اند اما اینبار با پیشنهاد بهتر!
🚨
قربانی از تراکتور هم پیشنهاد خوبی دریافت کرده اما تمایل داره به پرسپولیس بیاد!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136510" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136509">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
✅
پرسپولیس با محمدرضا اخباری به توافق رسیده و اگه اتفاق خاصی نیفته، امروز رسماً ازش به‌عنوان دروازه‌بان جدید تیم رونمایی می‌کنه.///فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/136509" target="_blank">📅 23:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136508">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
🔴
باشگاه پرسپولیس در آستانه توافق نهایی برای جذب دانیال ایری و کسری طاهری است.
✍️
قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/136508" target="_blank">📅 23:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136507">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
رسانه‌های مملکت: نساجی با انتقال طاهری و ایری مشکلی نداره و اونا در اردوی ترکیه به سرخپوشان اضافه میشن و حتی ممکنه کاظمیان هم در ازای رضایتنامه‌ی یکیشون راهی قائمشهر بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/136507" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136506">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
تیکدری امروز بازم مثل بازی قبلی یک گل و یک پاس‌گل به نام خودش ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/136506" target="_blank">📅 21:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136505">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qroK0F6RUymgXf3ZynoTib-EskDhw4Y6uSywgI-auySvzR0vVkivJcCrs_UCCd1LVt6RUbSkR2KZ3PtH5C7F1bMwaH0yy0pLHHkndqWs6dzjkAZsN-MzxgJPoSJS-5nUtUEEIwERRpHp5KJbZdOEVQ-jC8c1QL7Y7PUbuquYNOc8TCmlRJcbV-0BqYQqUx1m2OffKb4ZFvIIMdolJZ3AqKDrWg-feuJEuqN83j0g6c7DvJ3e3OEqnH2IePoV1Ar8Hg4eiL62t2Azjo-hC-8G9QFzYNwyzMCcoLyRi8P2SSbqJPxRVGUusMZ7NIDfdCzAxd-_jqt3O_-cGrZgLSlB8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
رسانه‌های مملکت: نساجی با انتقال طاهری و ایری مشکلی نداره و اونا در اردوی ترکیه به سرخپوشان اضافه میشن و حتی ممکنه کاظمیان هم در ازای رضایتنامه‌ی یکیشون راهی قائمشهر بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/136502" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136501">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
تکمیلی :فرهیختگان: استعلام از فیفا اومده و مشکلی برای انتقال نیست و احتمالاً هردو قرضی رایگان تا نیم فصل + بند خرید با تیم راهی ترکیه میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/136501" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136500">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8GBELmGD3pBjRXkwQyxq-94iz8yXLb4Gw3vUQ30YOnRs1ATgEHmKv-UTjpjtyNwyEQqn1IeSguEg9r0Xz16pg7LtxBMpQecND55fKPQIsu2jmJyDbBq-C-XjdvtwgLoKvXLS6F_hIAagjQgrQZD9Ny1n-CoVcJ9XJgUmnpsP1MCk4z8GIN_XI9lJyZVx4s4Gmrxi1DtpY9Dzu_TA_WpWhzXtOOIteEV4Y_Z50zudKJf9yfY62D9bm6TKZ0l9Rv9DUw4kyzuHjt0cgk7Ki0ZrJvYehdnuniMtxPTReT2USfePGkAzm0gYQavT-GhoVyQdqah_WL0z2tP4TPVqeLPaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی طاهرخانی:
❌
میلاد زکی‌پور با ارسال پیغام‌هایی به بعضی از افراد خواهان پیوستن به پرسپولیس شده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/136500" target="_blank">📅 20:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136499">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه، حتما عضو شین و‌ چک کنید چقد راحت سود میشه کرد
😉
✅
JOIN JOIN JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136499" target="_blank">📅 20:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136498">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOlCzY5F3DY-FmTm2rADSnCXbW2E0sVHkFWbbF6oQEgaus6taXVpFFAJG--aIUpf929lrPuXDqbTspg6TIbdieEu15VuC68ZQU2a-G0Z0r5IvasNaF9StZj6hnzAon3qo0uhExEGt1JH8Qb42r2Kc94pY4FllrTRQp5oILg-CFFuXaytnm3-synhOC4nWLZ28YmeW94nWRAb8wnHMitGJHT5ZTCLvxGO_4ZmOnJcPTI4ZggcQ51bLvomcsjgkXDp4N22K-2Wi-B2T5Die7YDWXiJeOu6s4GqZkThfWcxIepJTC1-wR1cJJpCpvlVK9T8msS243rkGecPyT2B3I0GrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
Ⓜ️
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@ARON_TIP @ARON_TIP
@ARON_TIP
@ARON_TIP</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/136498" target="_blank">📅 20:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136497">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❗️
❗️
به این ترتیب با وجود رد شکایت باشگاه پرسپولیس، همچنان موضوع اصلی پرونده محرومیت 4 ماهه بیرانوند به قوت خود باقی است و این دروازه‌بان در شکایت به دادگاه CAS خواستار لغو محرومیت و جریمه مالی خود شده است.
🔴
🔴
شنیده می‌شود هنوز علیرضا بیرانوند در موضوع شکایت…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/136497" target="_blank">📅 19:24 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
