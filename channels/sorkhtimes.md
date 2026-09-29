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
<img src="https://cdn4.telesco.pe/file/mNuyzeQRvIOwgdkpl7Xncvf1VRMNLccEEpUt8IKaLHFrhAyhSX1gMDO5RpGnP54hAtcjVMAk0w_CgDbRFK0NV4wYJpo3h3qnbnMiyr9whD3UoGl4c9JVlYDJsU8O6w4M6eX5TW-rLzP3VVz_yyYr11jw-GtESw1CqTN8gbyKEjjPqlnEsd8YVh1MIYdnr0Vm6qPEl3p4r1ePMEQoCkELM3XGejpnV1_1A6CkEEPMhuYpxOCW_zA8ZdaSZW204ISZZtJpbR2ksxIc_G2o6CKk6lv9AxZ6mDua9a-C95I1O5AMZHiKyfKZAwMz6D7odCVm2rId4qN4TI-LQeFrNi1GrQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 23:34:57</div>
<hr>

<div class="tg-post" id="msg-140723">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp0Mg6Ed075itxo_dq947nHS88GDMPn3QhDtCOV_zakENV6FnSs5FecXdDIPGJvhGdBPXGwr4wNChThdygfYNAc7HN35axSsAeTi64YuNk56apc37JKjGA3-b4U1NfMyft4pofHQTjuO50c5z2fopjL4aI-d1yIie7a4MmzLcxwocS0Y9T00auGc7PwFRyHqDBzMvSmb5nqpgSiO_UB-qXHWJWYrmcpeEBd1bHsbTapX2pX8zVRozwZRukkmLn_Q-HNhvj-Pz7PftMcOoguGEWPtMu7HpL4UGtStiCZ5mzBKU0TGATzyi8s6XmMmAdtebQGxbNzg7-2kyisfrxPFFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🔻
مدت قرارداد احتمالی جدید نیازمند با پرسپولیس مشخص شد
⚪️
⚪️
پیام نیازمند گلر پرسپولیس که اخیرا مذاکراتش را با این باشگاه برای تمدید قرارداد آغاز کرده طبق شنیده ها به توافقات نسبی دست یافته. طبق شنیده‌ها قرارداد جدید نیازمند با پرسپولیس 2 ساله خواهد بود و گلر فعلی سرخپوشان قرار است دو فصل دیگر نیز در جمع پرسپولیسی‌ها باقی بماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/140723" target="_blank">📅 23:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140722">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">📘
📘
در 14 بازی آخر تیم ملی با هدایت امیرخان فقط سه برد داشته که اونم مقابل گامبیا، تانزانیا و کره‌شمالی بوده
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/140722" target="_blank">📅 23:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140721">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJby9p1HSSaHbhAk2taaF9SH82y6eCsQmcTKSR2TgCgXS77Ami1uUEvU5Sf8Rp5EnPKHSoiOaD0p3YuQOTVpNPcf2KJoSW6z65bjC7FrlDx2MlwM1DwooWT4VdsQ9xVEcvapepS-qiXJFVCfSEb1_bS_cfe4dDnTWnUNoovabBf_mP_mUQHdaq17LsuejqVr0cEy2AhINYpEdiB40VBbgwoevL4m9czpKh46zUOc05qUif0ikZ8uwCGRATvUan66mk4yA1_0SX4E9zyk4-9VbPg2gkB5mHdzen-lf5SQ0N-iMmJ9VYI3zM6IvblLA1vTBDKRo8ihNe0VYOO8qGm5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
قرارداد ۱۳۶۵ میلیاردی پرسپولیس برای تبلیغات البسه
✔️
✔️
باشگاه پرسپولیس قراردادی به مبلغ ۱۳۶۵ میلیارد تومان برای تبلیغات بر روی البسه تیم‌های خود شامل بزرگسالان، رده‌های پایه و بانوان منعقد کرد.
✔️
✔️
این قرارداد برای فصل جاری جهت اطلاع عموم بر روی سایت کدال…</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/SorkhTimes/140721" target="_blank">📅 22:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140720">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z04aOE82aRO85-mCuepe-48W7VlU_SoK05yj9jqP8lWLh2OBDYDiPbxCQzTgGFA_5MPvjtHWGk7cFbdBwcPUmWvBjSrU1UvWGViJq-OFgXhcTtVrMt3IBUBqq5kxRC6an9uqcYO0jFELYeoMeSoEd-G2Cr-vu24zWHhUw5ZADhWK5i3EUAjZLMAvVTpyn_XjBXXUTXjyEsyZzNvWSQYQ3W2_nshfMxbT7BmFJ-mWeq_X3H3Q2KBe1rZsCe-7hH5qQ7KUEFWP86FAxP6xyBfdHTIRjZGrPQQ1S0mlCFuYGcHBpqPcUDEJClBhCIX8ChGO1NpUa4hEppV9I9ryLXDBeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب اگه پیام نیازمند نبود، فاجعه بازی انگلیس تکرار میشد؛ تفاوت دروازبان درجه یک با دروازبان معمولی اینجور جاها معلوم میشه
❤️
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SorkhTimes/140720" target="_blank">📅 22:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140719">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
لباس پرسپولیس عوض می‌شود
⚡️
⚡️
باشگاه پرسپولیس برای فصل جدید رقابت‌های فوتبال، در آستانه تغییر برند تولیدکننده البسه خود قرار دارد.
⚡️
⚡️
⚡️
برند «یوسف جامه» در فرایند مربوط به انتخاب تولیدکننده البسه باشگاه پرسپولیس، توانسته نظر کمیسیون معاملات باشگاه را جلب…</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/140719" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140718">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1880075a0d.mp4?token=hKA9UPDQmS9qBn1IvsMSXbZxHCSdMJNE0eGnR0nVdFDup0rzh-v0ReKXyGO6fm7cplPqSnV1nzRbQ1Ad6krANxdjwTmgv8tBsRPR7RyZbEdPE0brbELqD13gtwD4be4NDfTL6J43lK10WET0EWCAzHPfCQVbs4W0Mi18b-OyYpaTVgnOLvsQptOsLVvxbYsHyrD5cC_NnmJ2Tbncm-R-fkY64EjhsmuEjF6LpHfwzAJwpOgW5wGRTl61Sct8Qq0wh7k67GMI9_C8jmWZNxoHEqRf5E4ldE9q6oSrsllTv_CxUkvgIwMZfqb4Kj1lMB4t3wgRqy8PL9TmEXgIp3vQpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1880075a0d.mp4?token=hKA9UPDQmS9qBn1IvsMSXbZxHCSdMJNE0eGnR0nVdFDup0rzh-v0ReKXyGO6fm7cplPqSnV1nzRbQ1Ad6krANxdjwTmgv8tBsRPR7RyZbEdPE0brbELqD13gtwD4be4NDfTL6J43lK10WET0EWCAzHPfCQVbs4W0Mi18b-OyYpaTVgnOLvsQptOsLVvxbYsHyrD5cC_NnmJ2Tbncm-R-fkY64EjhsmuEjF6LpHfwzAJwpOgW5wGRTl61Sct8Qq0wh7k67GMI9_C8jmWZNxoHEqRf5E4ldE9q6oSrsllTv_CxUkvgIwMZfqb4Kj1lMB4t3wgRqy8PL9TmEXgIp3vQpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
درگیری شدید در بازی رده نوجوانان لیگ تهران میان تیم‌های کیسه و شاهین!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/SorkhTimes/140718" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140717">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
پرسپولیس هنوز هیچ توافق یا مذاکره‌ای با اندونگ انجام نداده/طرفداری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SorkhTimes/140717" target="_blank">📅 22:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140716">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
پایان  بازی روسیه 2 _ 0 ایران
✔️
✔️
یک نمایش ناامید کننده دیگر از تیم ملی/ با «مدل بازی متفاوت» هم باختیم!
❌
❌
در حالی که امیر قلعه‌نویی وعده داده بود تیم ملی با مدلی متفاوت برابر روسیه به میدان می‌رود اما نمایش تیم ملی همان همیشگی بود؛ نگران کننده و ناامید…</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/140716" target="_blank">📅 21:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140715">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66e4f7259.mp4?token=LZ08swxDCfWxcPzUE8P7J0QJegd9BtQo8wjDZbllIHLeWJEiZe6YamsJeK_aGZ9-OMUGcUS6eGdq8K2m6I_3vLgP2vS7KpjkzwSFYPvZDzLs9RDwM_eRFDNWN0dM-xcuMrvSblg47Y-v6EsF7eZhC76AwGcei6MEciMYgeUMAYCl3DA7t2QGXU6sYT9QQZyKix4TOxYFPc6AHKRqhU-2NCWcjKxmTYpGjxQRXzapXqrI3_kgG5Sxa4SoP5yhU9r4MEa_r2sVhjTdxgR2m_TwzmR5wJCLg9NjNoGckIe0S_Ie3gNKDn9fj1xBtm_rb9sLo9gsmAMhKZX-3o_g_gmk8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66e4f7259.mp4?token=LZ08swxDCfWxcPzUE8P7J0QJegd9BtQo8wjDZbllIHLeWJEiZe6YamsJeK_aGZ9-OMUGcUS6eGdq8K2m6I_3vLgP2vS7KpjkzwSFYPvZDzLs9RDwM_eRFDNWN0dM-xcuMrvSblg47Y-v6EsF7eZhC76AwGcei6MEciMYgeUMAYCl3DA7t2QGXU6sYT9QQZyKix4TOxYFPc6AHKRqhU-2NCWcjKxmTYpGjxQRXzapXqrI3_kgG5Sxa4SoP5yhU9r4MEa_r2sVhjTdxgR2m_TwzmR5wJCLg9NjNoGckIe0S_Ie3gNKDn9fj1xBtm_rb9sLo9gsmAMhKZX-3o_g_gmk8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📘
📘
در 14 بازی آخر تیم ملی با هدایت امیرخان فقط سه برد داشته که اونم مقابل گامبیا، تانزانیا و کره‌شمالی بوده
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/140715" target="_blank">📅 21:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140714">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
✅
سومین سوپر سیو از پیام !!!
⬇
دمت گرم واقعا پیام جون
🔄
یه تنه جلوی آبروریزی رو گرفتی سلطان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/140714" target="_blank">📅 21:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140713">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVTG678TTo0XI0sGGlmTX8EPQpy9sWWrz4MhfnHseMNqTRflCBn-FIhHyseOMuWmXIYJXELTIwGabmRGi_0xwN03xDro6lcbJ3wADoUF-FLxeifUkWSya6dvhh9MBgLCTG_2iT4fuMz7O5mCvodROXfTIDgQuBa9tezUcQeZRBynfVbCBKxy098FL4kPhUrQue4Z57Q2fdhibEtfDKOr31OUxTzDTJeBh7yMGK1nPG2WQpnHysgjHV37cffxFaC4EcNWqwwrPJx3swcWDBbZo1ppCjV9ZHYj3w05HfacUy9GxXZv2fwHzW32eZMuV10NN5L7iKez2Fs3rzXfMm0oCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
🔄
تصاویری از تمرین امروز تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/140713" target="_blank">📅 21:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140712">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
✅
آقای قلعه نوعی با ی خداحافظی کل ایران و خوشحال کن .....سومین گل هم از ازبکستان خوردیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/140712" target="_blank">📅 21:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140711">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
❌
با دعوت احسان حاج‌صفی به اردوی تیم ملی این بازیکن در صورتی که مقابل ازبکستان و روسیه حتی یک دقیقه بازی کنه رکورددار بازی با پیراهن ایران خواهد بود و از علی دایی و جواد نکونام عبور خواهد کرد
✔️
جواد نکونام ـ 149 بازی ملی
✔️
علی دایی - 148 بازی ملی
✔️
احسان…</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/140711" target="_blank">📅 20:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140710">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⭕️
⭕️
⭕️
خبرورزشی: مرغ حدادی یه پا داره بردن شکایت آسانی به Cas همین و تمام
⭕️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/140710" target="_blank">📅 20:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140709">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
کنعانی و علیپور به دیدار مقابل صنعت نفت نخواهند رسید/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/140709" target="_blank">📅 20:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140708">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
✅
آقای قلعه نوعی با ی خداحافظی کل ایران و خوشحال کن .....سومین گل هم از ازبکستان خوردیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/140708" target="_blank">📅 20:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140707">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41fa93705.mp4?token=hPKnLIsGLA5wnncvZAEe4v34vf9urqoOSsFKzSt96YMURMo6wax2A2gtwnS18fahcyp0sH__l0t3dtOPkTdijJtoUQjrR-zXD1luoGSnzEfNXMSpNyax8heuZcp-tVEj2kr8ApM_QJYlBoY4xouNY961-jACCLMGI70_tsbgJLWnKE0BjMbCjD5BaFFLna5pu3gHZhkIkGbjefxUznRurcTXBEAjN0WNLpgbjkTzInRXvp17KXJA-sw0tdz8i1GQpsHoR895eGJ3yt-dWnudRiX_z_wrggoVR27xh8dDlM03jU95HJkIwgT99U0JtlKyzDpsu2TUbAv8W0FZqzyb1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41fa93705.mp4?token=hPKnLIsGLA5wnncvZAEe4v34vf9urqoOSsFKzSt96YMURMo6wax2A2gtwnS18fahcyp0sH__l0t3dtOPkTdijJtoUQjrR-zXD1luoGSnzEfNXMSpNyax8heuZcp-tVEj2kr8ApM_QJYlBoY4xouNY961-jACCLMGI70_tsbgJLWnKE0BjMbCjD5BaFFLna5pu3gHZhkIkGbjefxUznRurcTXBEAjN0WNLpgbjkTzInRXvp17KXJA-sw0tdz8i1GQpsHoR895eGJ3yt-dWnudRiX_z_wrggoVR27xh8dDlM03jU95HJkIwgT99U0JtlKyzDpsu2TUbAv8W0FZqzyb1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇷🇺
گل دوم روسیه به ایران توسط گلوین در دقیقه ۳۵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/140707" target="_blank">📅 20:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140706">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7bSp-giHV6Nh8veM8hkiopKLCgIrZs0Vl3nSovM4Hosbpcii8JFHRpwhYAg54iWCIlrAGWGZ6w1HDCNY-5iQCPZE9B2jSEVEGJNE8DqzNi7keWmxR_fJKtQQNVXObSX7xnD1gSoiueXXf4aD7Ka8ulxXhgxVC5zbFfDA3xjGtCXdeTjMaNn_lTH59DUCkLU2o9RjXOOT1USWo46hdi54lz0P_4JBBcQ8lXQClP0SpS70_fNGuwCv5bjnsUz6SD1Kk07GxH6ecGbqKQsqD9pc7lHvGQa4bZBz9MFjYsO-tHwLcqAPHxYsREgA5KF9L9RCMEj97VvM7gp8oqt4qrhKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد ماتادورها و شطرنجی‌ها امشب در یک دوئل تماشایی!
🔥
⚡️
[
اسپانیا
🇪🇸
🆚
🇭🇷
کرواسی
]
⚽️
اسپانیا بعد از برد ۳-۲ مقابل انگلیس با ۵ برد متوالی وارد این بازی شده و در ۶ تقابل اخیرش با کرواسی ۴ برد داشته است. کرواسی هم در بازی اول ۲-۱ چک را برده، اما مقابل مالکیت و پرس اسپانیا احتمالاً بیشتر به انتقال سریع و ضدحمله تکیه می‌کند. باتوجه به روند دو تیم، سناریوی بازی نزدیک اما پرموقعیت محتمل است؛ اسپانیا از نظر خلق موقعیت دست بالاتر را دارد و یامال می‌تواند مهره کلیدی باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/140706" target="_blank">📅 20:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140705">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
تعویض زودهنگام محبی، به دلیل مصدومیت که احسان حاج صفی جای او را می‌گیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/140705" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140704">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be44fa519.mp4?token=KhjEUIAEBxlo-BQ7Dl9lMe5KijtW6vuHN5YMHf0MvunankoKPfZW0EdnfGwJIGSqRldNM_cbv4HPNzcGgJW9YHAF6DNLHbeYwr04ahp52YHfycJy3ROLch_Zn5zfy58Y_U6QLj1o76TO7RvV1Oxq9LVXW9l2ahyyukAOmCqIMp5I-TIZt01mk4xDvQf3yQwQWHiosKJpRvZtPP77zs3pMHfcRLns9BDDJxgE_WxtTTiwo5V7q0gmNvE19JXblf7v95eFL0g7oFpCZj8xvqwpnTq9nvCDyQkeGD4HSwx63QBSMPhyWXaaeyrqH7_PmeJYuH3YmCo33r-p-hYdi-wQ6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be44fa519.mp4?token=KhjEUIAEBxlo-BQ7Dl9lMe5KijtW6vuHN5YMHf0MvunankoKPfZW0EdnfGwJIGSqRldNM_cbv4HPNzcGgJW9YHAF6DNLHbeYwr04ahp52YHfycJy3ROLch_Zn5zfy58Y_U6QLj1o76TO7RvV1Oxq9LVXW9l2ahyyukAOmCqIMp5I-TIZt01mk4xDvQf3yQwQWHiosKJpRvZtPP77zs3pMHfcRLns9BDDJxgE_WxtTTiwo5V7q0gmNvE19JXblf7v95eFL0g7oFpCZj8xvqwpnTq9nvCDyQkeGD4HSwx63QBSMPhyWXaaeyrqH7_PmeJYuH3YmCo33r-p-hYdi-wQ6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تعویض زودهنگام محبی، به دلیل مصدومیت که احسان حاج صفی جای او را می‌گیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/140704" target="_blank">📅 20:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140703">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
تیم قلعه‌نویی گل اول از روسیه هم خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/140703" target="_blank">📅 20:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140702">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a7b7886c.mp4?token=g4xcDZxRamTBrBqhvKEXECEK7aHPGT8B1VgHLSNQdBeX-jObrP7bykmsCksUGNAqt1j1bh1QiZsWCWp19Z-OUPLMLYf4L3xe7Z4rkEdgWRdL6-Y42RvrEe1wx8RG-vNKKiE_bs8whF0lclHfDwXrmYEIhwUSvkyJ6V-hrsDUaKwNOCtdbMCvzrzDhJ34Cf8fNqHPhns5l58hcS1zjeitfxbvf8vnvD-tVZSIPB3TNWGZKmcuANE5stnZsK4yLxlbmwkzI2a53WJRSb6zIBxc46_D7xqq1LzqZGynj2myoleWp0McEsjOzv9kGsgl3SEWS2NwODzrp9Zy812es4DvmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a7b7886c.mp4?token=g4xcDZxRamTBrBqhvKEXECEK7aHPGT8B1VgHLSNQdBeX-jObrP7bykmsCksUGNAqt1j1bh1QiZsWCWp19Z-OUPLMLYf4L3xe7Z4rkEdgWRdL6-Y42RvrEe1wx8RG-vNKKiE_bs8whF0lclHfDwXrmYEIhwUSvkyJ6V-hrsDUaKwNOCtdbMCvzrzDhJ34Cf8fNqHPhns5l58hcS1zjeitfxbvf8vnvD-tVZSIPB3TNWGZKmcuANE5stnZsK4yLxlbmwkzI2a53WJRSb6zIBxc46_D7xqq1LzqZGynj2myoleWp0McEsjOzv9kGsgl3SEWS2NwODzrp9Zy812es4DvmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تیم قلعه‌نویی گل اول از روسیه هم خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/140702" target="_blank">📅 20:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140701">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
غایبان پرسپولیس در دیدار دوستانه امروز
⏺
حسین کنعانی، علیپور، عمری، ابوالفضل جلالی و حسین ابرقویی، باکیچ، ارونوف، نیازمند، زارع، محبی، محمودی، ایری، لطیفی فر و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/140701" target="_blank">📅 19:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140700">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
همه هواداران پرسپولیس از مدیران باشگاه عاجزانه تقاضا دارن تا ماجرای یاسر آسانی رو تا ته تهش پیش برن.
🔺
آخرش اینه که یه پولی میخواییم بدیم و رای هم صادر نشه به نفعمون، این همه پرونده بوده که هزینه کردیم و باختیم، اینم روش
🔺
دقیقا از روزی که فهمیدن…</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/140700" target="_blank">📅 19:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140699">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01dc83e8df.mp4?token=Q1YPy1whzvETzxGs4oQHqSH0j7PnSgvfna_iQEyTkXqmxyUO_zCAufBE5lrzgj6TSZc3vBHwNSHkNbeZ2MGlZhn3Y2QVVzYaIbdhh54NvFhNvq99noevDI9iOrlgkwK6nkL2WOzEDyGtpZ0SoVWyk-80IIR5wuoNJITPavnD6N9jUhvr0g0WKrJialRsV-yf7C-IsJIfDef2tIpnqj9E6YcZi4r0op7qfxT7u42GFbNWucJZikE_6Ss65uonenEe-wXJ-PMHDmn68ip7svWHGNo0TQQp7Uz0FwmmdHQc4qQ2sgCztVcribgDzTn8noPKEWIE5Ku7nont74eroTkMQiakmcnJ1Q5AqlQMWzztKsAqCkXQCU8CVOoAIXNQfL48uwgkcD1VSonQhthsNcVPBaabWkBgbMslWcm1p4B05NaLgfO5W_apVSDJ0UX9T83ZmHm8iHiyAHysvoh9U0VYjou7cqxAqbFqrY2y2tJ08JOvSWLDzgRde4DN7aNaTG2ehooPGNVFQrXYTwPtN1rEMd2PFGLYgvvpMKX_cWkbRZihlz1trxoR3cJd_sLDIo9SfaGB8RCsRh2QfVRJvxLhPBFOF0eR5tz_pxD6vZoBssiVd78uPFaFV8F2iQSV0OmRtvwYXCVfKvh-yG8p7oPjL5ssfvdvaPoNxIowWgc6d4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01dc83e8df.mp4?token=Q1YPy1whzvETzxGs4oQHqSH0j7PnSgvfna_iQEyTkXqmxyUO_zCAufBE5lrzgj6TSZc3vBHwNSHkNbeZ2MGlZhn3Y2QVVzYaIbdhh54NvFhNvq99noevDI9iOrlgkwK6nkL2WOzEDyGtpZ0SoVWyk-80IIR5wuoNJITPavnD6N9jUhvr0g0WKrJialRsV-yf7C-IsJIfDef2tIpnqj9E6YcZi4r0op7qfxT7u42GFbNWucJZikE_6Ss65uonenEe-wXJ-PMHDmn68ip7svWHGNo0TQQp7Uz0FwmmdHQc4qQ2sgCztVcribgDzTn8noPKEWIE5Ku7nont74eroTkMQiakmcnJ1Q5AqlQMWzztKsAqCkXQCU8CVOoAIXNQfL48uwgkcD1VSonQhthsNcVPBaabWkBgbMslWcm1p4B05NaLgfO5W_apVSDJ0UX9T83ZmHm8iHiyAHysvoh9U0VYjou7cqxAqbFqrY2y2tJ08JOvSWLDzgRde4DN7aNaTG2ehooPGNVFQrXYTwPtN1rEMd2PFGLYgvvpMKX_cWkbRZihlz1trxoR3cJd_sLDIo9SfaGB8RCsRh2QfVRJvxLhPBFOF0eR5tz_pxD6vZoBssiVd78uPFaFV8F2iQSV0OmRtvwYXCVfKvh-yG8p7oPjL5ssfvdvaPoNxIowWgc6d4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◀️
🔴
حضور پیمان حدادی مدیرعامل باشگاه پرسپولیس در ایستگاه 88 خیابان پارک وی به مناسبت روز آتش نشان
🔴
مسئولان پرسپولیس در این دیدار ضمن خدا قوت به پرسنل این ایستگاه آتش نشانی با اهدای گل و یک پیراهن پرسپولیس از این قشر زحمت کش تقدیر کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/140699" target="_blank">📅 18:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140698">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
ساعت بازی ایران و روسیه تغییر کرد
❌
❌
فدراسیون فوتبال روسیه از تغییر زمان آغاز دیدار دوستانه تیم ملی این کشور برابر ایران خبر داد.
❌
❌
تیم ملی فوتبال روسیه به هدایت والری کارپین، روز ۲۹ سپتامبر (۷ مهر) در شهر کازان به مصاف ایران خواهد رفت. سوت آغاز این مسابقه…</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/140698" target="_blank">📅 18:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140697">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
🔴
🔴
رسمی/ صنعت‌نفت برابر مس پیروز اعلام شد
🔄
🔄
کمیته انضباطی فدراسیون فوتبال در پی عدم حضور تیم مس رفسنجان در دیدار پلی‌آف مقابل صنعت نفت آبادان، نتیجه بازی را ۳ بر صفر به سود صنعت نفت اعلام کرد. با این حکم، صنعت نفت به لیگ برتر صعود و مس رفسنجان به دسته پایین‌تر…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/140697" target="_blank">📅 16:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140696">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‼️
😳
⚽️
بیرانوند: سربازی من نهایت ۵ماه است!
❌
فجرسپاسی؟ شاید اصلا به تیم نظامی نروم/ کل سربازی من با کسری‌ها 5 ماه است؛ در همان تبریز به پادگان می‌روم و با تراکتور هم تمرین می‌کنم!
🚫
❗️
۲۱ ماه خدمت چطوری و با چه کسری‌هایی یهویی شد ۵ ماه؟ بجز تاهل و ۲ فرزند و راه…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/140696" target="_blank">📅 15:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140695">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jm_488PEIhIsL6fAfw5o02oUxA51H_0QoWToCaVkxeMMmbGydh09QkxTsgQc-me_ZRTBEgUm-nwkynhjOqi_VWe9anTH4P-k6cqv90TfZukOaVMvuitFvH19dDIWux1pSbBlvM4mgTiCRsTg_OQjTOGD56vrfg_uI9qKmQVUAMcOSFm3cdXPbw5oyOq3zKNj3gCGgUm91wPDaZdmHN2vrU5i2HkzaKgWHxyew5b2EN17HzxEhp9tckW0Qbhu-sxGBeMM6qFi_GkQ0ED0rqIivq2rxbnFzjpRJlxDAP7JCRyptDzLUw0xMvBOewDlAPtJ79Vm2zEZmIQOGyzo4z72Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری | رسما شرعا جام قهرمانی به کیسه اهدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140695" target="_blank">📅 15:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140694">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
افشین قطبی، رسول خطیبی و پیروز قربانی به عنوان سه گزینه نهایی سرمربیگری تیم ملی امید انتخاب شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140694" target="_blank">📅 14:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140693">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
علوی سخنگوی فدراسیون: تراکتور، سپاهان و پرسپولیس پیشنهاد دادن جام قهرمانی فصل گذشته به شهدای میناب اهدا بشه‌ و فردا تصمیم فدراسیون در این مورد مشخص میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140693" target="_blank">📅 14:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140692">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🟥
دانیال اسماعیلی فر از تعویض ناراحت شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140692" target="_blank">📅 12:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140691">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140691" target="_blank">📅 12:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140690">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
❌
تیم ملی والیبال کشورمان با شکست ۳ بر صفر مقابل ژاپن نایب قهرمان آسیا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140690" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140689">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGElrNWomL1f9fjchE2P0eO8KF7HWEfaWClQvS7xnj3wTY5JOnA1aLjvPvoYJPSV7yUVLP2vh4mHkysc0BBrLf-StU8b7KUWFzC3M3V90QEgc0mQC4LxXQaOTZqpr3GjxCqAVrqvukOfKnwFyTZ7oGZpMCZ9_zFr5Uf5mJJ883e3TZ9kUOCwovtwPS2_1gc8a-Ekui3TF6-X8VA-MHUD8v2IstaGeZcFeWYDv7ffOqTDe5Pr1jB_s6xY5GVK5As8McABODNTTV6_d6_EhfrabRh5OlHJwkDpEeR3iR6GYu0yHBOSTeiSx_jLRJP4NCpSLiMVhwAd4L3UmCj95BDoWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
Spain -
❤️
Croatia
⏰
Tonight 22:15
🏟
Ramón Sánchez Pizjuán
⚽️
اسپانیا با ۵ برد متوالی و بدون شکست در ۳۹ بازی اخیر وارد این مسابقه خواهد شد؛ کرواسی هم در بازی نخست ۲ - ۱ چک را برده است. در ۱۱ تقابل قبلی، اسپانیا ۷ برد، ۱ مساوی و ۳ شکست داشته و آخرین بازی دو تیم را هم ۳ - ۰ برده است. مدل آماری پیش‌بینی، شانس برد اسپانیا را ۶۱.۷٪ و کرواسی را ۱۸.۶٪ برآورد کرده و احتمال زیر ۲.۵ گل را ۶۶.۹٪ می‌داند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140689" target="_blank">📅 12:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140688">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
علوی سخنگوی فدراسیون: تراکتور، سپاهان و پرسپولیس پیشنهاد دادن جام قهرمانی فصل گذشته به شهدای میناب اهدا بشه‌ و فردا تصمیم فدراسیون در این مورد مشخص میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/140688" target="_blank">📅 11:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140686">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9d2810e6e.mp4?token=uUWyvZqF9zOewEIZbbkxzByKUSCuroidjjOiKZJU1No8UB8HzXSpTMbcxVzZ9l96VkFOoOKCmQxXBot36UFoOrt_YrOpifDxOui2yw_olflcXL6HZE6rM6otMqDH7Vej8wV02EgYNBkRzjvQqQXrZezn79CJFDBKz9lyOtmz4Ds2TNSGYLf3GOUVu4XPGGBTh9aRTwyiYcyBNknIHMLhuXymEW-e9VA8_RkPRYPQuaIQCuPotbamu3La6YbkqBcc0jqS7KwH5u0yRMjJDhzI9XThkDNW1zCFcUrQXAkXEJgGl_zvL2mx1oh_QkNLCemW6WqHPGeTwHoVUcZW-mlrXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9d2810e6e.mp4?token=uUWyvZqF9zOewEIZbbkxzByKUSCuroidjjOiKZJU1No8UB8HzXSpTMbcxVzZ9l96VkFOoOKCmQxXBot36UFoOrt_YrOpifDxOui2yw_olflcXL6HZE6rM6otMqDH7Vej8wV02EgYNBkRzjvQqQXrZezn79CJFDBKz9lyOtmz4Ds2TNSGYLf3GOUVu4XPGGBTh9aRTwyiYcyBNknIHMLhuXymEW-e9VA8_RkPRYPQuaIQCuPotbamu3La6YbkqBcc0jqS7KwH5u0yRMjJDhzI9XThkDNW1zCFcUrQXAkXEJgGl_zvL2mx1oh_QkNLCemW6WqHPGeTwHoVUcZW-mlrXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😳
⚽️
بیرانوند: سربازی من نهایت ۵ماه است!
❌
فجرسپاسی؟ شاید اصلا به تیم نظامی نروم/ کل سربازی من با کسری‌ها 5 ماه است؛ در همان تبریز به پادگان می‌روم و با تراکتور هم تمرین می‌کنم!
🚫
❗️
۲۱ ماه خدمت چطوری و با چه کسری‌هایی یهویی شد ۵ ماه؟ بجز تاهل و ۲ فرزند و راه دور[سرجمع ۹ماه کسری]، چه سهمیه‌ای گرفت یهو؟
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140686" target="_blank">📅 10:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140685">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
یک شکایت جدید از استقلال؛ پیکان این بار از ماشاریپوف شکایت کرد
✔️
باشگاه پیکان مدعی است نام ماشاریپوف فصل گذشته از لیست استقلال خارج شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان، حضور مجدد این بازیکن در لیست بازی با خودروسازان غیر قانونی بوده…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140685" target="_blank">📅 10:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140684">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
❌
تا نیم‌فصل بیرانوند میتونه به‌ صورت کاملاً قانونی و بدون هیچ مشکلی برای تراکتور بازی کنه!/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140684" target="_blank">📅 10:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140683">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
فوووووووری از بیرانوند: چرا فکر میکنید سربازی نمیرم؟ 3 ماه معافیت تاهل دارم، 3 ماه فرزند اول، 3 ماه فرزند دوم و 3 ماه دوری راه تبریز تا خرم‌آباد و یعنی کلا حدود 6 ماه خدمت دارم؛ اصلا شاید نرم تیم نظامی برم پادگان تو تبریز و بالا برجک وایسم موقع مرخصیم میرم…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140683" target="_blank">📅 09:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140682">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
✔️
فوری و رسمی/ دلار 250 هزار تومان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/140682" target="_blank">📅 09:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140681">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
✅
بازیکن پرسپولیس نیامده جدا شد
🔹
فرزین معامله‌گری که از تیم شمس‌آذر به پرسپولیس پیوسته بود، با توجه به مشمولیت، برای گذراندن خدمت سربازی راهی ملوان بندرانزلی شد.
⏺
پس از پایان دوران خدمت سربازی، وضعیت ادامه همکاری او با سرخپوشان مشخص خواهد شد.  «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/140681" target="_blank">📅 09:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140680">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
زنوزی علیه کیسه
❌
زنوزی: کیسه خیلی جام دوس داره بیان من پولش رو بدم  برن منیریه برای خودشون جام بخرن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/140680" target="_blank">📅 09:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140679">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BL_kenQ_2ajrKbi-gH-Sf0wWkjIuO905v8jSCO_09VjaGaphOXlhEv70O0XxcAij_8Nrm1wFP6AdBeMZlx1k-tHaJ3EsxCjxnuIgGvank-ZlPvln-s0QApcgEL_40n1fgQmXeXUwuSKj20tXV60w0O7AVcfGWxIqZUUxGAiuoJHEqzIwLg1RLduXl9kpMXL8hZTTNsZfTG0sWpAMDyp58liLbHZ3gAbtCQPKLljfc-A9pTsSHTwCpY3KORqnOHmpcxNWwcCy-VsvhbRsmWgx1UhE9HAgL7ollhOyM4H0lm05PffbF-eKs_N_Kd9ZYMcOsCfTLEkqubEXrthFX9Wpqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/140679" target="_blank">📅 09:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140678">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvUI9zMa5NEzVcxfphj2ZYHGxeRlXDnRk7c3KbvmJDKzzHqZQq3ssbC7mFT-OpANFlVfi8tbPIavIlZNU_uD8ft503RZosbsoA1szBIUp2h49mRT9CJGbB4vA61QoUO6-DWvIBzgEe71tH_eNA6jIUhm1shHZHfr7Mswg_2uM629gcpjRZbrUOlNUTA0P4_Jkm67SBPox01iFUTcBCff1AxCA6Anq1v_pKFWBJUhnWHfCKJDbvSmzgaQKUTtWdt4bLjS_IOYTWnvVGOWo16x9DTIKuGe1pYdgvksQ-Xl6N8oUpoFw7nq0ItiOxTYN_gaZB4etgUTK4eEIbEbC0TmTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Russia -
🇮🇷
Iran
⏰
Tuesday 19:30
🏟
Ak Bars Arena
⚽️
روسیه با فرم هجومی بهتر وارد بازی می‌شود؛ ۳ برد در ۵ دیدار اخیر و میانگین گل‌زنی بالاتر، نقطه قوت اصلی این تیم است. ایران در مقابل تیمی است که در انتقال سریع و ضدحملات می‌تواند خطرساز شود. تقابل‌های اخیر دو تیم هم نزدیک بوده و در ۴ بازی آخر، هرکدام یک برد و ۲ تساوی ثبت کرده‌اند؛ بنابراین انتظار می‌رود بازی درگیرانه و کم‌فاصله دنبال شود و سناریوی گلزنی هر دو تیم دور از ذهن نباشد.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140678" target="_blank">📅 01:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140677">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
فرزین دبیری عضو هیات رییسه فدراسیون فوتبال: تراکتور، پرسپولیس و سپاهان مخالفت‌هایی با قهرمانی استقلال دارند
✔️
✔️
اینکه ما از الان مخالف قهرمانی استقلال هستیم، اشتباه است اما قطعا مخالفت‌هایی در مورد قهرمانی استقلال خواهد بود چرا که سپاهان، تراکتور و پرسپولیس…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140677" target="_blank">📅 00:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140676">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🔴
افشاگری عادل فردوسی‌پور از ماجرای پول گرفتن ۷۵۰ هزار دلاری فدراسیون از باشگاه کیسه، قبل از اردوی ترکیه تیم ملی بزرگسالان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140676" target="_blank">📅 00:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140675">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♨️
🤩
🤩
افشاگری باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!
🔄
🔄
محمدحسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/140675" target="_blank">📅 00:24 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140674">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3190d23c56.mp4?token=LS1ZW2G5viHkinmusHRqNGe9In0NilM2t61lp7GXqcpkisUANirgC_DBaJJ6dbwrkV0cMGpbcLk2zFhOysyBwsVyVhwEgT7Yv9wlvl70uR3pLFJIoBgwpITM96Jmtg-epC1VsZuMmIndcKomnB9R9ynHw2WVkv2b-pRrQrmIHI4moddgB8t6jWq3qkYH3FBgLkoczeyAw8qTjgvJM2vDe60CFPPgX_EUh-NWqVAQKMQDrAJVKsYnKS5pXjOvllEUUMqcD1_t6mhNxzVlUdXhB-E_GVGNiHKlrLyYkSeUVMKltMx9VkTayXXHcm1uXHJC2Q8TEsl4a7C6uhyGb4IDTBDriSod01KAnhArIV8pBDc9mwg0Ec2Hjz-dRb9BS0jvu1qbB_vMLfeILy-Y1B-a3yUR8zC2bzezTrR0iN_MmFSKJ2QgcL-7lADpiycJgGOadi22RrI6HIjTbLIu_a_ChKD8GhJMEAZAwQEFbBSHg3AvtejmE9_TvAMrquHcyGSeNupbOiOGyO4fe8XGGAWdygl55mv_IXtRZTcI3BxZB6IGIQg03uuPgMtsKZAGtAU0ZmA3TnxEv1zqOReR3uB0qGSmpwOtSS872uVs0qv2YgwX51AC1YHxuhg5WHR_YytUadf2hg6lN5JeVVDiF0WyEo0h2IVq5hZMw7dszuE0qxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3190d23c56.mp4?token=LS1ZW2G5viHkinmusHRqNGe9In0NilM2t61lp7GXqcpkisUANirgC_DBaJJ6dbwrkV0cMGpbcLk2zFhOysyBwsVyVhwEgT7Yv9wlvl70uR3pLFJIoBgwpITM96Jmtg-epC1VsZuMmIndcKomnB9R9ynHw2WVkv2b-pRrQrmIHI4moddgB8t6jWq3qkYH3FBgLkoczeyAw8qTjgvJM2vDe60CFPPgX_EUh-NWqVAQKMQDrAJVKsYnKS5pXjOvllEUUMqcD1_t6mhNxzVlUdXhB-E_GVGNiHKlrLyYkSeUVMKltMx9VkTayXXHcm1uXHJC2Q8TEsl4a7C6uhyGb4IDTBDriSod01KAnhArIV8pBDc9mwg0Ec2Hjz-dRb9BS0jvu1qbB_vMLfeILy-Y1B-a3yUR8zC2bzezTrR0iN_MmFSKJ2QgcL-7lADpiycJgGOadi22RrI6HIjTbLIu_a_ChKD8GhJMEAZAwQEFbBSHg3AvtejmE9_TvAMrquHcyGSeNupbOiOGyO4fe8XGGAWdygl55mv_IXtRZTcI3BxZB6IGIQg03uuPgMtsKZAGtAU0ZmA3TnxEv1zqOReR3uB0qGSmpwOtSS872uVs0qv2YgwX51AC1YHxuhg5WHR_YytUadf2hg6lN5JeVVDiF0WyEo0h2IVq5hZMw7dszuE0qxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♨️
🤩
🤩
افشاگری باورنکردنی میثاقی از یک ایجنت، عارف آقاسی، پرسپولیس و پیش قرارداد برای یاسر آسانی!
🔄
🔄
محمدحسین‌میثاقی: پرسپولیس به یک ایجنت ۱۰۰ هزار دلار پول داده بود که عارف آقاسی را به پرسپولیس ببرد ولی این بازیکن را به استقلال برد و الان باشگاه از این ایجنت شکایت کرده است
🔄
🔄
در همین راستا این ایجنت قرار شده است مدارکی به پرسپولیس درباره فسخ آسانی بدهد و همچنین این بازیکن به پرسپولیس ملحق شود و مذاکرات حتی تا پیش قرارداد هم جلو رفته بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140674" target="_blank">📅 00:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140673">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
علیرضا بیرانوند: چون من تو یک تیم مدعی بازی می کنم این همه فشاره که به سربازی برم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140673" target="_blank">📅 00:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140672">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
باشگاه پرسپولیس در پرونده مهدی فراهانی و حمید مریخ برنده شد و این دو نفر باید سرجمع 220 هزار دلار آمریکا (51,216,000,000 تومان) و 12 هزار فرانک سوئیس (3,414,120,000 تومان) به باشگاه پرسپولیس پرداخت کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140672" target="_blank">📅 00:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140671">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrkxB_669fImiokpe_VdyYbt8pQJDYFGN69XA9PeFclXrZGSRfcZJRxSleh44MF0iYyDipPpshNxgaSaOhoDigi7V28cksvfupAPQ_AAMyNRarX7di6WjF4wWUy0VVMhvb-hkvmMjQzHSp7GH0pX1dcA5JM0oWLOivHlPmzBtoJaIxQ2Vo7k6Zf1MnrusCNM6Oh8p2ras-CWbw1yuQLUoBl3IJC5ErLM4xWCeDrcVPAJGvUBhv4o8oMT9jmcpMi8HdC4bbOlapn3bcv9jZO_SFHv1tWU5LzQDQXuqCL-7dhmfGSFTarkWmuYuRnBBAZNBksx5ytHFB1U9QpyD3clcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
وارد فیفادی شدیم، شخصا از فیفادی نفرت دارم چون پرسپولیس لذت دیگه‌ای داره برام
❌
میشد که قبل از فیفادی یک برد دیگه و یک بازی دلچسب دیگه از تیم محبوبمون ببینیم اما کارشکنی‌ها جلوی برد دلچسبمون رو گرفت..
❌
دم تک تک بازیکنامون و کادر فنیمون گرم که کاری کردن وقتی بازی پرسپولیس رو نمیبینیم بجای اینکه خوشحال باشیم، حسرت میخوریم که چرا چرا چرا یه مدت نمیتونیم بازی تیم خوب و جنگنده‌مون رو ببینیم..
❌
بعد از فیفادی میبینمت پرسپولیسم؛ منتظر بازیهای هجومی‌تر از قبل و پر‌گل تر از قبل هستیم آقای تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140671" target="_blank">📅 23:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140670">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
یاسر آسانی: رامین رضاییان کسی بود یک دقیقه بعد تمرین تمام اتفاقات رو لو میداد و همه میفهمیدن و ساپینتو برای همین لج کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/140670" target="_blank">📅 23:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140669">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
علیرضا بیرانوند: چون من تو یک تیم مدعی بازی می کنم این همه فشاره که به سربازی برم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140669" target="_blank">📅 23:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140668">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
✅
علیرضا بیرانوند دروازه‌بان تراکتور : من نردبونم و همه دارن ازم بالا میرن کینه‌ای که بعضیا از من دارن کینه نیست علاقه و دوست داشتنه.
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140668" target="_blank">📅 23:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140667">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
#فوری
🗣
خبرگزاری مهر : تعویق خدمت شامل بیرانوند نشده و او رسما از 1 مهر سرباز غایب محسوب شده و هر گونه بازی کردن او غیرمجاز است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140667" target="_blank">📅 23:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140666">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🤍
🇮🇷
سردار آزمون با بخشش 5 درصد اموالش به کمیته امداد خمینی به تیم ملی برگشت:))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140666" target="_blank">📅 23:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140665">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇷
💙
💚
یاسر آسانی خطاب به عادل فردوسی‌پور: من میدونم که طرفدار پرسپولیس هستی
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140665" target="_blank">📅 23:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140664">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1981c5068c.mp4?token=ux6cgAj08jt1xTrrzr8xtjoUfIg4ndphW7iDCk4pa0FaNNjhE935vyr52fDQEoUxipVQdXL1qmwj9JDBpPaJEf14aISR2Rqe5RE3AjBcxdZk8zOUhZk-6nOVs2CS62xWI5YTd5vkVCL3PoRYF-Ygowd6TuqxjpB7y4V7ToKWTGTwiH5-irsKfXlU50QAr_YxXoiT18430M5T6pR_b2OSDzQqzBT_BqgyttErQ1Crbe4cwuhizMf2nH1Gzmh5M4aQ5wwBfq6cC7pQv0tnAJQyTCuTTrFrzHB6xasH2i9X6WAJ3AyeVYE8xtKx8BIeorKy1Hh2hWAWDJCoa-t1CPfT_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1981c5068c.mp4?token=ux6cgAj08jt1xTrrzr8xtjoUfIg4ndphW7iDCk4pa0FaNNjhE935vyr52fDQEoUxipVQdXL1qmwj9JDBpPaJEf14aISR2Rqe5RE3AjBcxdZk8zOUhZk-6nOVs2CS62xWI5YTd5vkVCL3PoRYF-Ygowd6TuqxjpB7y4V7ToKWTGTwiH5-irsKfXlU50QAr_YxXoiT18430M5T6pR_b2OSDzQqzBT_BqgyttErQ1Crbe4cwuhizMf2nH1Gzmh5M4aQ5wwBfq6cC7pQv0tnAJQyTCuTTrFrzHB6xasH2i9X6WAJ3AyeVYE8xtKx8BIeorKy1Hh2hWAWDJCoa-t1CPfT_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
💙
💚
یاسر آسانی خطاب به عادل فردوسی‌پور: من میدونم که طرفدار پرسپولیس هستی
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140664" target="_blank">📅 23:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140663">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
یاسر اسانی: ابوالفضل جلالی بهم زنگ زد گفت نمیایی پرسپولیس؟ گفتم حاضرم از ایران برم ولی به پرسپولیس نه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/140663" target="_blank">📅 23:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140662">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
❌
ورزش‌سه: پرسپولیس به سند جدیدی تو پرونده یاسر آسانی دست پیدا کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140662" target="_blank">📅 23:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140661">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
پوریا لطیفی فر: از بچگی رویای پوشیدن پیراهن پرسپولیس را داشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140661" target="_blank">📅 23:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140660">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🤍
🇮🇷
سردار آزمون با بخشش 5 درصد اموالش به کمیته امداد خمینی به تیم ملی برگشت:))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140660" target="_blank">📅 22:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140659">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
خبرورزشی
❌
❌
باکیچ با وجود عملکرد خوبی که در فصل گذشته داشت، به اون صورت مورد علاقه تارتار واقع نشده و احتمال جداییش کم نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140659" target="_blank">📅 22:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140658">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⚽
🤩
سپاهان باکیچ را می‌خواهد!
❌
گفته میشه سپاهان به‌دلیل عملکرد نه‌چندان خوب هافبک‌های فعلیش، دنبال جذب مارکو باکیچ در نیم‌فصل رفته و محرم نویدکیا هم تأکید زیادی روی جذب هافبک پرسپولیس داشته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/140658" target="_blank">📅 22:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140657">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
تسنیم:
📰
جلسه امروز فدراسیون که به گفته رسانه‌ها برای تصمیم‌گیری برای جام فصل پیش بوده ؛ اصلا راجب به قهرمانی و اهدای جام به استقلال نبود و این موضوع در جلسات بعدی فدراسیون مطرح میشه!!
❌
احتمالا درباره مربی تیم ملی امید باشه
👀
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/140657" target="_blank">📅 22:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140656">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kha8hPNkW7xozEzAmkXDT8AkFow66WYxfe-idy02fff51RSjsEfj0xJzhe60dAxamgCbEnMy03hQKtCA5or4-HGK_6bJtxFFyES1ds4HgyzgMLW_wYzHTnOqHogWj2qs5cLuPgSalOlLZaD_GuX5-rbtD_G657ntzCO6D51FSZCPjVMF3DwBRSZ7YM8cCjCxR5meHlhVfv74Zw6cKSttnhBXuvq_mwqIkDwuWpv8Iz13D6s8xZXArPxMOcefRDd1tLQETlfIcWu_sZ7wJS8r6OnQmb2VvSEzzGx8fn5eK583N6VFEGBiv5lOHJNDM1WDJjubsrEsL1xfl8--r9f99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Belgium -
🇫🇷
France
⏰
Tonight 22:15
🏟
Roi Baudouin
🇪🇺
بلژیک در بازی اول با ۲ گل و ۱۹ شوت ایتالیا را برد، درحالی‌که فرانسه با برد ۱ - ۰ مقابل ترکیه وارد این مسابقه می‌شود. فرانسه در ۵ تقابل اخیر ۵ برد داشته و در این ۵ بازی فقط ۲ گل دریافت کرده؛ ضمن اینکه امشب بدون امباپه بازی می‌کند. از نظر روند، بلژیک در خانه ۶ بازی شکست‌ناپذیر است؛ بنابراین انتظار بازی نزدیک و کم‌فاصله از نظر موقعیت‌ها می‌رود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/140656" target="_blank">📅 21:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140655">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140655" target="_blank">📅 21:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140654">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
پاسخ مثبت پرسپولیس به برگزاری جام حذفی بدون ملی‌پوشان
❌
باشگاه پرسپولیس با برگزاری رقابت‌های جام حذفی حتی در صورت غیبت بازیکنان ملی‌پوش موافقت کرده و خواهان برگزاری این مسابقات در فصل جاری است.
❌
با توجه به فشردگی برنامه مسابقات و حضور ملی‌پوشان در اردوهای…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140654" target="_blank">📅 21:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140653">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdzyme-Uryq52semz8Frx0bRNrLeuOoO7ERId5TbWDiItm5DyqMzAw5T2RcM1DNntlN3ZuJDPdCRxS_wPBL2kwMFnFva5ywa0y96V6qLn2VTvFf7EtW4Fa5lJaifVxYQN0yRf8UceUcnKUgioL-0xGKsykpJKMQ7Xs4ADy7AoeF4hsTBNPzG_rOqJf43ujdxQyDYThXotWdXMiZHE9YnAYW7owlr8lTtWPomWbF2Zp9rxuLxGTmYqpPsDFIpaK6bfEUZ-CKwOoI5xc_lCLjuxt64qx0amBs1-tPGb8-FxxY4kR74fHjcxKT4XUFB8x_fETjId8-gjb1Pg3FL7ZUQ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بازگشت دنیل گرا به تمرینات پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/140653" target="_blank">📅 21:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140652">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
رسمی:با استعفای حسین عبدی موافقت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/140652" target="_blank">📅 21:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140651">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
افشین قطبی نزدیک‌ترین گزینه به هدایت تیم امید است.
🤝
فوتبال ۳۶۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140651" target="_blank">📅 21:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140650">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
✅
واکنش فدراسیون فوتبال به اظهارات تاجرنیا درباره جام قهرمانی فصل گذشته
❌
❌
اظهارات علی تاجرنیا، رئیس هیئت‌مدیره استقلال، درباره وعده اهدای جام قهرمانی فصل گذشته به این باشگاه، با واکنش جدی فدراسیون فوتبال مواجه شده است.
❌
❌
پس از موج واکنش‌های مجازی و اعتراض…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140650" target="_blank">📅 21:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140649">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
همه هواداران پرسپولیس از مدیران باشگاه عاجزانه تقاضا دارن تا ماجرای یاسر آسانی رو تا ته تهش پیش برن.
🔺
آخرش اینه که یه پولی میخواییم بدیم و رای هم صادر نشه به نفعمون، این همه پرونده بوده که هزینه کردیم و باختیم، اینم روش
🔺
دقیقا از روزی که فهمیدن…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140649" target="_blank">📅 19:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140648">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
پاسخ مثبت پرسپولیس به برگزاری جام حذفی بدون ملی‌پوشان
❌
باشگاه پرسپولیس با برگزاری رقابت‌های جام حذفی حتی در صورت غیبت بازیکنان ملی‌پوش موافقت کرده و خواهان برگزاری این مسابقات در فصل جاری است.
❌
با توجه به فشردگی برنامه مسابقات و حضور ملی‌پوشان در اردوهای…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140648" target="_blank">📅 18:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140647">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✖️
گفته میشود باشگاه پرسپولیس برای تمدید قرارداد 5ساله با امیرحسین محمودی و 3ساله با پیام نیازمند به توافق رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140647" target="_blank">📅 18:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140646">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
✔️
✔️
✔️
❌
جواد عطایی، سامان نقیبی، ابوالفضل شیرازی، محمد حسین پژوهان،‌ پوریا آزاد رنجبر و محمدامین دهقانی بازیکنان تیم‌های جوانان و امید پرسپولیس بودند که امروز در ترکیب سرخپوشان به میدان رفتند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140646" target="_blank">📅 17:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140645">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfRkgk3rluKtVfCarr4S18Zw8ce2ta9rtMSif5rzPgM4C3TJ8wUbM3EL4uqmTZAnrsiISxDLzh2eOe4Zha6htIpwOsdjO2vmunTNNmCal3yQnTrad6o40X714YTUvhlSrpla6yEF5L8cItRiCf9NLOnOFpt3s7YT5JEetX9k4O0Gb0wqYCeI1fWj3VJmY-v0KPGT6Hyn6gwBPI7eqYWXtwQ5B-DrT_q4oK6HkERL-BisHyYku127Hv6U2lS_s5lnviE2PSM9o6lntZzFxCFutTv5RLx71ArfyK0vbFwjyTuWWymNr6OO1XZJK2XhtSbWjhCyb_gsUhLrQ91xjQdgJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
آتزوری در برابر ترکیه؛ نبردِ کنترل و غافلگیری!
🔥
⚡️
[
ترکیه
🇹🇷
🆚
🇮🇹
ایتالیا
]
⚽️
تقابل دو سبک متفاوت؛ ترکیه با بازی مستقیم و انتقال‌های سریع می‌تواند دردسرساز شود، اما ایتالیا در کنترل توپ و سازماندهی دفاعی دست بالاتر را دارد. باتوجه به کیفیت دو خط دفاع، نیمه اول می‌تواند محتاطانه و کم‌گل دنبال شود و جزئیات کوچک روی نتیجه اثر بگذارد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140645" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140644">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✔️
✔️
#رسمی؛ صابری عضو هیئت ‌مدیره پرسپولیس شد
⚪️
⚪️
با استعفای اردوبادی، حسین صابری به‌عنوان عضو جدید هیئت مدیره پرسپولیس معرفی شد. سمت دقیق اعضای هیئت ‌مدیره در جلسه آینده مشخص و بعد از نهایی شدن در کدال اعلام می‌شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140644" target="_blank">📅 16:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140643">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
مدیران پرسپولیس آماده ارائه پیشنهاد تمدید قرارداد ۴ ساله به اوستون اورونوف هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140643" target="_blank">📅 16:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140642">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
❌
فوری؛ بیژن مرتضوی که چند ماه پیش در فینال جام جهانی برنامه اجرا کرد، پس از چند دهه حضور در امریکا دقایقی پیش وارد ایران شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140642" target="_blank">📅 15:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140641">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
بیفوما با ساخت ۱۲ موقعیت گل، یکی از خلاق‌ترین بازیکنای این فصل لیگ بوده
🔥
🔴
اگه نصف موقعیت‌هایی که ساخته تبدیل به گل می‌شد، با اختلاف بهترین پاسور لیگ بود!   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140641" target="_blank">📅 15:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140640">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140640" target="_blank">📅 15:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140639">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
💢
💢
✔️
✔️
مدیران باشگاه پرسپولیس هفته گذشته‌ مذاکرات برای تمدید قرارداد پنج ستاره آغاز کردند
❌
پیام نیازمند
❌
محمدحسین کنعانی زادگان
❌
تیوی بیفوما
❌
اوستن اورنوف
❌
ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140639" target="_blank">📅 13:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140638">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
جلالی دوباره مصدوم شد
‼️
🔹
ابوالفضل جلالی در جریان تمرینات اخیر پرسپولیس بار دیگر دچار مصدومیت شد. البته شنیده می‌شود مصدومیت جلالی جدی نیست و بیشتر به گرفتگی عضلانی شباهت دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140638" target="_blank">📅 13:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140637">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140637" target="_blank">📅 11:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140636">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
اجرای بیژن مرتضوی در کنار ارکستر فیلارمونیک بین نیمه بازی فینال جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140636" target="_blank">📅 11:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140635">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccc2b8cd01.mp4?token=GQY6P4_nl9vq8iESUVGbkZDwuyE-YSmb-InAGURpQHDeKGY4aTwSfNtqaP_jR2BUIeNzNuOQX3NDA9gVhVTcPfVpgv8kjdrnxUmJoLk94jcwz5lKKyqvesUDtalb_5lwTObkT0xf_ntqNfi4yu3OhflrWlKHgdgqaTtmim21fbqyWRkCvSp8VZRhv-pQvscxH5vS0XD5xQJvJqhTCpr6ndHQ3hmtWLh5njospnM2jgTvNi0KiW1NLcLEQzl8Tp8oY6jH7_SKxFb3oiN2xOgjplsiKP3wyB8Q11Kn82jIDo3HAZAW418MM4JNhh5BeCmwvWMjGYroXn4X8aZo-6tQJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccc2b8cd01.mp4?token=GQY6P4_nl9vq8iESUVGbkZDwuyE-YSmb-InAGURpQHDeKGY4aTwSfNtqaP_jR2BUIeNzNuOQX3NDA9gVhVTcPfVpgv8kjdrnxUmJoLk94jcwz5lKKyqvesUDtalb_5lwTObkT0xf_ntqNfi4yu3OhflrWlKHgdgqaTtmim21fbqyWRkCvSp8VZRhv-pQvscxH5vS0XD5xQJvJqhTCpr6ndHQ3hmtWLh5njospnM2jgTvNi0KiW1NLcLEQzl8Tp8oY6jH7_SKxFb3oiN2xOgjplsiKP3wyB8Q11Kn82jIDo3HAZAW418MM4JNhh5BeCmwvWMjGYroXn4X8aZo-6tQJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دلداری خیابانی به بیرانوند قبل خدمت رفتن
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140635" target="_blank">📅 11:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140634">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
فوری؛ باشگاه پرسپولیس درخواست مدیر برنامه‌های یاسر آسانی از پرسپولیس، پس از فسخ قرارداد با استقلال را هم به مدارک خود اضافه کرده و خیلی امید دارد که سندی بر فسخ قرارداد آسانی باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140634" target="_blank">📅 11:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140633">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
رسمی:با استعفای حسین عبدی موافقت شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140633" target="_blank">📅 11:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140632">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140632" target="_blank">📅 09:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140631">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
فوری؛ باشگاه پرسپولیس درخواست مدیر برنامه‌های یاسر آسانی از پرسپولیس، پس از فسخ قرارداد با استقلال را هم به مدارک خود اضافه کرده و خیلی امید دارد که سندی بر فسخ قرارداد آسانی باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140631" target="_blank">📅 09:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140630">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
❌
مدرک جدید پرسپولیس در پرونده آسانی، پیشنهاد رسمی اینجنت او به پرسپولیس بود.
❌
❌
بعد فسخ، این پیشنهاد ارائه شد با این مضمون که او با استقلال فسخ کرده و پرسپولیس می‌تواند برای جذبش اقدام کند.
❌
❌
مدرک از این معتبرتر ؟ / اگر باشگاه پرسپولیس با رقم عجیب و غریب…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140630" target="_blank">📅 09:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140629">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✖️
✖️
#فوروووووی
✅
سپاهان به جمع مشتری های ایرانی بشار رسن در نیم فصل اضافه شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140629" target="_blank">📅 09:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140628">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqVOh7mBQiL2OfWSnGq-rb3ISMcsMBndzc25RQG4IfKHPg-IUvY39921YkRLImbQu6t1j-f9RhjoCjtmjlDYYVFStBaIirVAwuHXEhO3oRp1ZF6eAO1oF63-DM7pw7K3CuoPacxzcC-i0HLUMEvsBsgFdIO88xrWKak-wGfXTSgtELG_Zb0YEvjEXKT6C4l5JGfMNZh2pvDyklZ_STOjRhqj3tNhCuLyRdnVj3_4lBKMMZYUTRYNYBw6k5EkNvYNY5AlJZ0HG3xMlgd1T4DitkZ-ekuzUN-eOv8irc7ps4yV87OtsoxEwAEHCysrznAjJjXZNkM2Oo1tUWDYjRpl3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140628" target="_blank">📅 08:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140627">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3HmS4LF9Km5e3GhMXvpHmNkPRIPdviV1KmUq3N-aWYPpunNe76yPCq7rsd5Wc6EJyS1wH1v5pFNDvPEN6MwUrCPHQO6t1hE2yqtNtqLFp6g5K9gGYuRYgbOvA_juxb3Bu596tFhhaNhz4iiOj9EP6P0QhY2gVZbBBrrcZPUT7UWQYgoIhgiHGyupxU5a6pzL0xNf0LbV86aHzcH8OGjMxnKn9YkFWJBWVGsggauUZEmRte46KLAy_g37NuiIM-Vbq4JpBDNhuA-mtGELWut1dovAYUrA0t-asBaLFbUg2D2dN_b8ABeZGyN4VV0bhKhrwzAVrl-cCpE5AnRZF25kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد جذاب خروس‌ها و شیاطین‌سرخ؛ جایی برای اشتباه نیست!
⚡️
[
بلژیک
🇧🇪
🆚
🇫🇷
فرانسه
]
⚽️
فرانسه در ۵ تقابل اخیر مقابل بلژیک شکست نخورده و هر دو تیم هم شروع خوبی در این دوره داشته‌اند؛ بلژیک ایتالیا را ۲-۰ برد و فرانسه ترکیه را ۱-۰ شکست داد. بازی در بروکسل است و بلژیک با فشار تماشاگران احتمالاً شروع تهاجمی‌تری خواهد داشت، اما فرانسه در انتقال سریع بسیار خطرناک است. با توجه به ۵ برد متوالی فرانسه در تقابل‌های اخیر، سناریوی بازی نزدیک و کم‌گل محتمل‌تر به نظر می‌رسد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140627" target="_blank">📅 01:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140626">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBBdMQuoY74o03mG14Z5nHBhYeIpp1_ufJs2zFfsMx7O0ndBQ3XpApL2qwZiOqJIf1Vv1-7QMqeGS32KeX2UERIRcegFqTRf4_OKjl_aalddwOeNy4O-zH-Fqrgvm8uis5eAjwWLQA0tBCckEtCQhESZYQRakFhjmUwe0k3CITpT3QwjuhpxJoarSGZtm048dKBqEqLQEpGYzX2t-7tbKbys7ALfH-sHX-eyGlOo5QsZMRObQ43xp_5bKWyJbX4d4hZNBHEV2PP_hjaLysdDMZ25Vz-7XSKSTiR5JkYJPit6S4Kc9iROZyDmHOcNnBLY1kzpKMCFLHE70vvtSUUeJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️
🔴
با دستور پیمان حدادی، شورای هواداری تشکیل شد تا صدای هوادارا رو به باشگاه برسونه و پیگیر خواسته‌هاشون باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140626" target="_blank">📅 23:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140625">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u48Wsr8zbLHvmpd3H_AAvPcRsW-zJHssnTRLPi7d8XCpi9UFDcv0KEdmQK6b589BvbqTTYPHGweQFiJgis2l6Tvd1fTqIzXhXqohtkJ8t-F6Et1ZkDy_l-uV9cQjsKo6p4miA5owxIq8Xd_9A1h40WfA2eFNZeR6iebRdUeX9cojoLvkKpEpT8g2-rI_dXnGrdBs-pd8iF9C5v-3vZjcUOA-kZYbn688365UR_vpGx-vDzaIqX8ZyirYpJaGnOmDB2vuS6Q9jGLv8XxoIwPoZDG-WUmIPs06Y8lvlqun-aX17X3Sxzyl-Vu-frkcGpMBf6cDAjHGA1uThFsb3xQ0bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☑️
آقای فکت رسانه‌ای شما خواهشا از آسیا و سهمیه صحبت نکن که خودت با اون باخت ۷تا مقابل الوصل به اندازه کافی آبرو ریزی کردی بعدشم از سهمیه ای صحبت میکنی که بهتون هبه شده مثل پنالتی های معیشتی‌تون
❌
❌
شمایی که باشگاهت که با وجود ۶-۷ تا خوردن تو آسیا حرف از تخصص می‌زنین ، هنوز ۷-۸ هفته مونده به پایان لیگ خودتون قهرمان میدونین و دارین گدایی میکنین، جام ندیده های بدبخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140625" target="_blank">📅 23:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140624">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
❌
❌
❌
❌
❌
❌
❌
🚨
اورونوف در تعطیلات موفق شده ریکاوری خوبی رو پشت سر بگذاره و از نظر روحی و بدنی دیروز  آماده نشون داده
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140624" target="_blank">📅 23:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140623">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
❌
🎙
تاجرنیا: به من قول دادن که قبل از بازی بعدی جام قهرمانی دوره قبلی رو به ما میدن.
❌
پ.ن چه قدر حقیرید شماها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140623" target="_blank">📅 23:38 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
