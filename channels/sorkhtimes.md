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
<img src="https://cdn4.telesco.pe/file/vP-6_qDtNeRC8pQMHUYdqrWO0NT6C0u-IY6vAmDbFOmJ8HmnDTj69JQdg1rQ0HThugrjzWKcWwlusRxb9DBu9AL1fF78alIAEDgcw5PrPB3p2MrGWJ3SFjVM2mZZYscKOTBeWZo8H5K0J9fzpGQdyN4BkfggooAGyQpSxkWdRuw97Oqhb90HNUOiA35hl_X9jWYdpeP-WLoSM0gjq52_q3v7QPcE4IvUKRT2ntcjtUzmxdq0zbgOuFB239qI9e7bDmu2Az97nBAUUJu013d50wCxYWqfC3QXUJvm0DbkC3MjSl_h4JQXAtAUWWsndU4apSCWSgSgcUDvZgLJBHPs2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 18:50:44</div>
<hr>

<div class="tg-post" id="msg-136833">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">#شفاف_سازی
🔖
🏅
نساجی دانیال ایری رو پارسال ۷۰ میلیارد از ذوب آهن خریده الان زندی گفت ۱ میلیون دلار بدید…پول زور
❌
کسری طاهری ۷۰۰ هزار دلار خریدن گفتن ۸۰۰ هزار دلار… باشگاه میگه با همون ۷۰۰ هزار دلار رو میدیم
❌
باشگاه اگر ۸۰۰ هزار دلار بده هم تا نیم فصل نمیتونه…</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/136833" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136832">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⭕
هرکسی از ننش قهر کرده گوشی دست گرفته کانال هواداری زده هر کصشری میخان میزنن، اون حروم زاده ها اگر میخاستم بیان پرسپولیس چرا رفتن نساجی؟! صدرصد هم خود بازیکن هم ایجنتشون با زندی بستن
‼️
یکم عقل تون به کار بندازید خداوکلی چرا هرکس هر کصشری میگه طوطی وار تکرار…</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/136832" target="_blank">📅 18:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136831">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‼️
🥇
آقای مدیرعامل بزار چند صباحی از پرونده عظیم فساد تون داخل باشگاه مس رفسنجان بگذره… بعد ادای آدم های سالم و مظلوم رو در بیارید
❌
هر موقع پای میز مذاکره زورشون نمیرسه پول مفت بگیرن که از روش بخورن به هوادار دنده میدن، هوادار هم که ماشالله مسائل رو تجزیه تحلیل…</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/SorkhTimes/136831" target="_blank">📅 18:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136830">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‼️
🥇
آقای مدیرعامل بزار چند صباحی از پرونده عظیم فساد تون داخل باشگاه مس رفسنجان بگذره… بعد ادای آدم های سالم و مظلوم رو در بیارید
❌
هر موقع پای میز مذاکره زورشون نمیرسه پول مفت بگیرن که از روش بخورن به هوادار دنده میدن، هوادار هم که ماشالله مسائل رو تجزیه تحلیل نمیکنه شروع میکنه کوبیدن باشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/SorkhTimes/136830" target="_blank">📅 18:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136829">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOw7oDt4C62TP4G_47jhqpl_jRnKTSguisABiV0mcuv_qJMNbs4NQIA3RzPRckKIw36Y9iCyjGZnbHOxg-GH2lvtxl-XuO6gWGnMfj3szG4OOtecekyRl7_FrLk9WANBugrlTYrIeFWSQ3wrSCMVJ89CwiDwoXLHY3GMDQDGJt-ElUfJHrtWATrtUrbzt0x9mH8WVwT_gO9Z73MbcMyzDylADX02YVNTPk7hYZw1wTu5VDsXikftAosp59azb35MKWSVEbCi_XT0tKU_RUfEYUmupHmquGfhe-TkJFRMrmxZno8SgpRSeBiudBLN6vPDkN0G83T0gGhxBKw7-E3Szg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیرانوند اصلا دانشجوی دکتری نیست
🔺️
رئیس مرکز ورزش و تربیت بدنی دانشگاه آزاد گفت آخرین مدرک بیرانوند، کارشناسی ارشد است و او حتی دانشجوی دکتری هم نیست.
🔺️
پیش از این بیرانوند در تاریخ ۵ خرداد ١۴٠۴ و در برنامه فوتبال برتر ادعا کرده بود که دانشجوی دکتری است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/SorkhTimes/136829" target="_blank">📅 18:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136828">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SorkhTimes/136828" target="_blank">📅 18:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136827">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔄
🔄
ماهم مانند شما بلاتکلیفیم و خبر قطعی و رسمی نداریم و این شرایط برای خودمان نیز آسان نیست؛
🔴
🔴
ما نیز میخواهیم هرچه زودتر تکلیفمان مشخص شود تا به فوتبال و آینده خود برسیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SorkhTimes/136827" target="_blank">📅 18:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136826">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emOnL3qgPadRcFr7u2yo0Ythf3dkBFJMNLOBu5dvM6Y4PHUe-PwDsQAOhKbcHnFbFdlWivN4r1-G970qmkYEfenBhLjacVXhzdK7OcPmGoZ5cehWbZjH2htPUnbuO4nnMnuiExWjHVKYYCT2kpJ6nubf691jF5jW4EIGuqjqW7qSUXFSR1KrKA2EfPLgNjpdXRr_q8j4gUfXcTSoXNchMuQaTfpZLM_SIkI8jou7yfFAOBE70K04QcqSYB--Czitexh9MNGdl_FenHeP4KsnobOlEqoz6k6NkeIoEfm3kydLj1iiIbodc5F69fk9klvQA64psdK3-mnUxvRP7aIh8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
📸
آغاز یک روز پرفشار و همراه با انگیزه سرخپوشان در اردوی ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SorkhTimes/136826" target="_blank">📅 18:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136825">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔄
🔄
استوری مشترک کسری طاهری و دانیال ایری برای هواداران؛ ماهم مانند شما بلاتکلیفیم و خبر قطعی و رسمی نداریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SorkhTimes/136825" target="_blank">📅 18:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136824">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔄
🔄
گوهری گزینه ی گلری پرسپولیس نیست/قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SorkhTimes/136824" target="_blank">📅 18:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136823">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
🔴
🔴
انتقال دانیال ایری به پرسپولیس نهایی شده است.
❌
اما جذب کسری طاهری هنوز قطعی نیست و نهایی شدن این انتقال به حل مشکلات حقوقی بستگی دارد. //خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SorkhTimes/136823" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136822">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
❌
امیر عابدزاده که به تازگی بازیکن آزاد شده و احمد گوهری از گزینه‌های باشگاه برای گلر دوم می باشند ناگفته نماند وضعیت اخباری همچنان مبهم است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/136822" target="_blank">📅 17:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136821">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⚪️
⚪️
⚪️
انتقال کسری طاهری به پرسپولیس فعلاً نه قطعیه، نه منتفی. سرخ‌ها علاوه بر دردسرهای قانونی مربوط به قانون «پل»، بابت مصدومیت رباط صلیبی قبلی این بازیکن هم نگرانن. پرسپولیس تأکید کرده بیشتر از ۷۵۰ هزار دلار برای طاهری هزینه نمی‌کنه و تا وقتی از نظر حقوقی…</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/136821" target="_blank">📅 17:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136820">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
باشگاه استقلال پیشنهاد 5 میلیون دلاری آسانی رو قبول کرد و این بازیکن شنبه به ایران برمیگرده !!!
😕
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/136820" target="_blank">📅 17:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136819">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
پرسپولیس و تراکتورسازی پشت پرده توافق کردن که پرسپولیس بیخیال قربانی بشه و تراکتور هم بیخیال محبی تا باشگاه های اماراتی بازار گرمی نکنن و مبلغ رضایت نامه رو نبرن بالا
😐
/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/136819" target="_blank">📅 17:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136818">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
🔴
🔴
انتقال دانیال ایری به پرسپولیس نهایی شده است.
❌
اما جذب کسری طاهری هنوز قطعی نیست و نهایی شدن این انتقال به حل مشکلات حقوقی بستگی دارد. //خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/136818" target="_blank">📅 17:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136817">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
محمد قربانی: پرسپولیس و تراکتور مرا میخواهند/ مبلغ رضایتنامه‌ ام ۲۰۰ تا ۳۰۰ میلیارد است
🔴
🔴
بهتر بود نام تیم نیاورم، اما حالا که سئوال میکنید، میگویم. هم پرسپولیس و هم تراکتور با من و باشگاه الوحده مذاکره کرده‌ اند و در نهایت باید ببینیم ظرف روزهای آینده…</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/136817" target="_blank">📅 17:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136816">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">😳
😳
😳
😳
😳
😳</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/136816" target="_blank">📅 17:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136815">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">😳
😳
😳
😳
😳
😳</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/136815" target="_blank">📅 17:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136814">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قدوسی اعلام کرده یک مقام از باشگاه منتفی شدن دانیال ایری و کسری طاهری رو رد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/136814" target="_blank">📅 15:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136813">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
⚪️
🔴
#فوووووری
⚪️
⚪️
منتفی شدن انتقال کسری طاهری و دانیال ایری به پرسپولیس
🔴
🔴
طبق پیگیری‌های ایسنا از مسئولان نساجی، مدیران پرسپولیس حاضر به پرداخت مبلغ درخواستی از سوی مدیران نساجی برای انتقال این دو بازیکن نشدند تا انتقال آن‌ها به پرسپولیس منتفی شود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/136813" target="_blank">📅 15:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136812">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">📎
📎
📎
یه سوال پیش میاد اگه واقعا حس میکنید هنوز تو دفاع راست مشکل دارین پس عیدی چرا جذب شد؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/136812" target="_blank">📅 15:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136811">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
⚪️
🔴
#فوووووری
⚪️
⚪️
منتفی شدن انتقال کسری طاهری و دانیال ایری به پرسپولیس
🔴
🔴
طبق پیگیری‌های ایسنا از مسئولان نساجی، مدیران پرسپولیس حاضر به پرداخت مبلغ درخواستی از سوی مدیران نساجی برای انتقال این دو بازیکن نشدند تا انتقال آن‌ها به پرسپولیس منتفی شود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/136811" target="_blank">📅 15:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136810">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jL6xED61iOQyRv-cT_MAC_sdo--Hc5mRAeckrNrW4frw82XfMgT1Rp_0NU7QAliV48P9YXl4xEDevvRYTAs9XhDIwCWj6n27aF6nX9iNdnff8rkleKGJPqG_dSZmZZlAkn4YQAJnZfmOabjq42f9-IVVeeaSrJYOCskXq2WV5Ofy3zp0rJJPAbuoBn95_o8N_WXXWoDmfUo_1aJMYZYVvkiHAytTqFfJVwoZ_Ss9qDzIMTxYD7shOLciLfFtNhRij9U5rKH--WhX9J3byD9PzQlH0g4ji-HcsEz7zKYfbWfuzeTP9XdoFg39wtRFEWqGkPErxibKXXxOpGw0hLOp9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کاظمیان به گل‌گهر پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/136810" target="_blank">📅 15:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136809">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/136809" target="_blank">📅 15:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136808">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/136808" target="_blank">📅 15:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136807">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
⚪️
🔴
#فوووووری
⚪️
⚪️
منتفی شدن انتقال کسری طاهری و دانیال ایری به پرسپولیس
🔴
🔴
طبق پیگیری‌های ایسنا از مسئولان نساجی، مدیران پرسپولیس حاضر به پرداخت مبلغ درخواستی از سوی مدیران نساجی برای انتقال این دو بازیکن نشدند تا انتقال آن‌ها به پرسپولیس منتفی شود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/136807" target="_blank">📅 15:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136806">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBvg9y8gsgwcgnCZ8GWb8JMRMd7ybnbKKeqS8zLQcxYsVYmo9ZbNbm4Z-7RjVknr2yi-Kcur84X1EXIPU91upkXdfc1Eq5lw_yNGS2MtxvXQIeFnGtqF_gQg-Wr9w0ygxcRGNop_RSM-ywoo3NovLgBFQfNLvHoahjmykoQVxk9JCm7XHQWVFGKF0cJL3DuNdexARuw7haxF01AW72L9VRRtucvDZ-vm7auJUYkumxZ07xTnYiL4472B85IjDNED7JPKejK0e--O1LjqNxXAG9ehuyXLGuaxco6czsWj9AJdF94OtHU-9VkYAsuCzYlfaP4UrsWZPBQu9qvHUHQZqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
وقتشه پوکرو حرفه‌ای بازی کنی!
🎰
اگر به دنبال تجربه‌ای متفاوت و پر از هیجان هستید، بخش کازینوی وینکوبت بهترین انتخاب برای شماست. از بازی‌های کلاسیک مانند بلک‌جک، رولت و باکارات گرفته تا صدها اسلات جذاب با جوایز بزرگ، همه چیز برای یک سرگرمی حرفه‌ای فراهم شده است.
🕹
همین حالا وارد دنیای کازینوی وینکوبت شوید و هیجان واقعی را تجربه کنید. شاید برنده بزرگ بعدی شما باشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/136806" target="_blank">📅 14:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136805">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
❌
باشگاه نساجی گفته از اقدام پیمان حدادی به شدت ناراحت شده و میخواهد دانیال ایری و کسری طاهری را به باشگاه های دیگری بفروشد
😀
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/136805" target="_blank">📅 14:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136804">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
پرسپولیس میخواد رفیعی رو برای بازگشت راضی کنه؛ کاری که خیلی سخته چون امیررضا میخواد جایی باشه که بهش بازی برسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/136804" target="_blank">📅 14:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136803">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
شنیده‌ها: با توجه به عدم جذب اخباری احتمالا یا رفیعی برگرده یا گوهری که بازیکن آزاد جذب بشه
🚨
پ.ن: برای گلر دوم رفیعی یا گوهری هم جوابه بعید برن سراغ گلری که قرارداد داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/136803" target="_blank">📅 13:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136802">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
🚨
باشگاه تراکتور پاسخ هایجک محبی رو به پرسپولیس داد و محمد قربانی تا ۷۲ ساعت دیگر تراکتوری میشه/ ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/136802" target="_blank">📅 13:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136801">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
به دلیل تعلل مدیران باشگاه پرسپولیس در جذب کسری طاهری و دانیال ایری حضور این دو بازیکن در پرسپولیس از سوی شهاب زندی مدیرعامل باشگاه نساجی منتفی شد /ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/136801" target="_blank">📅 13:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136800">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
🔴
پوریا لطیفی فر ستاره 22 ساله تیم‌گل‌گهر با عقد قرار دادی چهار ساله رسما به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/136800" target="_blank">📅 13:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136799">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
به دلیل تعلل مدیران باشگاه پرسپولیس در جذب کسری طاهری و دانیال ایری حضور این دو بازیکن در پرسپولیس از سوی شهاب زندی مدیرعامل باشگاه نساجی منتفی شد /ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/136799" target="_blank">📅 13:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136798">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/136798" target="_blank">📅 13:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136797">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/136797" target="_blank">📅 13:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136796">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
عجیب اما واقعی؛ پرسپولیس و سپاهان داداشی شدن و پیمان حدادی کمپ شهید کاظمی رو در اختیار سپاهان گذاشته تا اونجا تمرین کنن…!
☹️
☹️
🫥
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/136796" target="_blank">📅 13:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136795">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lABcs1yk2Dyzx48WOcH5QCb-BZeEE1MAw3O7wHykL56zm9ky8770ui0VqivqTYTDQSXqnX-Pl7fObYMJsMcUSMJDE4_sZ16IAyWGYwVsnuuIYmk2JQUkn22qJuhvJc6loQQxiMtbjozjsIr-64ReQIG_dFBfqsaP_UiLOZ8OWSh4sAaJf0gxvjK7rFhOQfHqU_WUGVUrlm__yKehPs_FZDEYTS8VGvaM09MNF_x43HEmmkeZWa3HHffZMXxOBWcyPkoTqq2dOisuk2Io8CjgyyM6IBHzNxyYLFVn-7NJ8W6GGkdKatbTge073c1f1SsRtof7Fxu5tbiP4M1S3DWa5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
باشگاه سیرجانی با انتشار تصویری از محمدرضا اخباری به صورت رسمی اعلام کرد این دروازه بان با قراردادی دوساله به گل گهر پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/136795" target="_blank">📅 13:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136794">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
#ورزش‌سه : ممکن است به زودی یک قرارداد معاوضه به اضافه پول نقد بین دو باشگاه پرسپولیس و سپاهان شکل گرفته و احتمال دارد نام‌هایی مانند محمدامین کاظمیان، حسین ابرقویی و آریا یوسفی در این معامله جای پیدا کنند. حتی احتمال رخ دادن این اتفاق برای محمد عمری نیز…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/136794" target="_blank">📅 13:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136793">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSJbpa33k1gp8LFxs9T3pszODhyqejo67gGpUtnx3cnLUnZ8Y7Rn3hKmxi8uVkcKIYSFQdT7td3UVqTV2X0NZuCV2VLePFYAtOAyZ5Q0VXHhXKN9bdy1USuR7gklh4PdKnccfnSE7LnM4x-fzjbsculGnX-38JJUCbgXE30LNTX6u9tdvHHJ_s3TSL3bHzbbACefK50W6UjBUeOA51dx2WcCPuJQM4aTQsbRwTnABpjytuxydYjMTF39BRJtuMQbj4TZCmKJkGRjDuHHKzih85L-87p3kbK-Yoo_qGAx6tnuRMdKXbgOiVVb20lds3s2bXRTS5H1YXIoTBj9YemL1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووووری :
محمد قربانی به تراکتور پیوست!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/136793" target="_blank">📅 13:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136792">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">➡️
➡️
➡️
➡️
⬅
تارتار به دنبال پاکسازی پرسپولیس!
⏳
💬
مهدی تارتار پس از بازگشت از ترکیه قصد دارد چند نفر از اطرافیان باشگاه را به دلیل لو رفتن ترکیب تیم کنار بگذارد.
⬇️
سرمربی پرسپولیس به چند نفر مشکوک شده و پیگیر این موضوع است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136792" target="_blank">📅 10:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136791">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
🔴
ورزش سه: هیچ کدوم از هافبک های پرسپولیس بازیساز نیستن و دو خرید جدید پرسپولیس در این پست (لطیفی فر و پورعلی) بیشتر وظایف دفاعی دارن. پرسپولیس اگه پست 8 بازیکن نخره تو شروع فصل به مشکل میخوره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/136791" target="_blank">📅 10:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136790">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
❌
امیر عابدزاده که به تازگی بازیکن آزاد شده و احمد گوهری از گزینه‌های باشگاه برای گلر دوم می باشند ناگفته نماند وضعیت اخباری همچنان مبهم است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/136790" target="_blank">📅 10:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136789">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🌀
🌀
🌀
پرسپولیس خواستار جذب مدافع تراکتور شد
🌀
باشگاه پرسپولیس با ارسال نامه به باشگاه تراکتور خواستار جذب صادق محرمی مدافع تیم فوتبال تراکتور شده است.
🌀
محرمی پیش از این سابقه بازی در پرسپولیس را داشت و از همین تیم راهی دیناموزاگرب کرواسی شد.
🌀
باشگاه تراکتور…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/136789" target="_blank">📅 10:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136788">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
صادق محرمی درخواست خروج از باشگاه تراکتور را داده و قصد ندارد فصل آینده در این تیم باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/136788" target="_blank">📅 10:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136787">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
گل پرسپولیس به تیم مصری توسط بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/136787" target="_blank">📅 09:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136786">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
فرشید حقیری: یاسین سلمانی دیروز پشت دروازه تمرین کرده و احتمال زیاد می‌ره مازاد تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/136786" target="_blank">📅 09:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136785">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❗️
❗️
لیست تیم ملی امید اعلام شد.
❌
در این لیست 4 بازیکن از پرسپولیس به تیم ملی امید دعوت شدند.
🔴
امیرحسین محمودی
🔴
علیرضا همایی فرد
🔴
سهیل صحرایی
🔴
فرزین معامله گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/136785" target="_blank">📅 09:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136784">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
خبرنگار پرسپولیس:
🔴
امروز محمدمهدی زارع و پویا پورعلی در تمرینات عالی ظاهر شدن .تیکدری هم مثل همیشه خوب بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/136784" target="_blank">📅 09:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136783">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
🔴
گزینه بعدی پرسپولیس برا گلر دوم گوهریه آماده س ولی برخلاف اخباری سهمیه لیگ برتری  حساب میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136783" target="_blank">📅 09:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136782">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkKMQ81pqotJ93xwNw3KeZDrl_Zm2RyagCu92Sje5yZET_ZA1_Mqxtyaqsy6OFWfD4ZEceF24NV1O62eyDOXXR5cctc_viJtQhwW5iM_95B2yDElGtPRmouKMTTy7u0hyta-dsLbbHtNnFV9KMQEN5G9cf80l4oP-ansa0kajn42B6IKtkxqzle4mPEfjqxtzfV4aBy7RmviVnNKV22x0NZmjMEURQoI0b8P0zJuwL5xfUz4JpRaQqP7HPpJ_4xZ38wL-53vBq16RVTDv79eguk066s9RNML3E3R3Ep2kO4s56EvVPEQJsZGWQfiRPnjTnFrs4Y6cf1hxPWINCua1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کریم باقری : پرسپولیس فصل گذشته مشکلات زیادی داشت و من خودم شخصاً جزو کسانی بودم که از عملکرد و نتایج تیم راضی نبودم اما نسبت به فصل آینده امیدوارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/136782" target="_blank">📅 09:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136781">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQPYXRAubJ9pz8BMj6jtmEy4ykN4-49ERu9Rl16K3aNkHLyGUJHRSkxDW0kQ1zSjnyCIMYokkxtyfBdcHh3nB5haVtzrd4mFfn9uh3U_LjW-t-NgDJoJ_UsoqD74RWexIjF1zlJa9FKhN7HzcZ2BMcK518GgiScNZRDJ-SyOtM4WawU4nn7aEtWtNU-nBKu_vxXT61VfmHDQHx3jDbEjaqsV_CRf9xL4ktwEPl8lTAHJRRoVXEaVXyOM4MQG0eFi7AMk737Ddo8behrY4wsqEXpVlymoUS4VXpjuYNMyKJCasEZRmL-5hZWbVOpQNJONCB0-fYPnRacpx3lUhoRqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبح 5/5/5 تون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/136781" target="_blank">📅 08:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136780">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZttuSPxVcRE8wCutnlrB79ZOnZPFeSuqe3vQHQC3SZ84YV5duqlVWRSKcdBbIMWA5vL3MeYF_q189IIm2hzMhc0Xgt_bi9ZQw0INYFVzU-EYu8Nbn4pOy9lsVWHDCoa2blO68zCw8WRUMbJxKu3uuN33nHVVb_izzBjo1NL1FvsBgvoz__UOadj0nl4Qv08Vircc74tUt3b5DwZlxGDTX1Mrd2fW0cPIItJKjPBtMOixe5ixoVWkPtsYFK8L4r9lLa-pDl3Bcv-C29fmLRrInGsHlAmbSzQ6zJbVU1GtgAkCwDPvhvMWUgNWJr7S6JsXX0AdtVCp1nIgZqXg1kA3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
ربات وینکوبت در دسترس تمامی کاربران
🟢
بدون اینکه از تلگرام خارج بشید میتونید مستقیم وارد سایت و بخش بازی‌ها و کازینو بشید، پیش‌بینی ثبت کنید و براحتی واریز و برداشت انجام بدید.
📌
حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر براتون باز میشه:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/136780" target="_blank">📅 01:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136779">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
✅
✅
نظر شخصی :یا به گندمی اعتماد کنید که  الان تو اردوی تیم هست .یا رفیعی و برگردانید ...یا به امثال آرشا شکوری و آرمین عباسی اعتماد کنید و جذبشون کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/136779" target="_blank">📅 00:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136778">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">➡️
➡️
➡️
➡️
⬅
تارتار به دنبال پاکسازی پرسپولیس!
⏳
💬
مهدی تارتار پس از بازگشت از ترکیه قصد دارد چند نفر از اطرافیان باشگاه را به دلیل لو رفتن ترکیب تیم کنار بگذارد.
⬇️
سرمربی پرسپولیس به چند نفر مشکوک شده و پیگیر این موضوع است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136778" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136777">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
تارتار اسم یه مهاجم خارجی رو به باشگاه داده و درصورت جدایی بیفوما و گرا مدیریت برای جذبش اقدام میکنه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/136777" target="_blank">📅 00:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136776">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/136776" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136775">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/136775" target="_blank">📅 00:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136774">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
مهدی طارمی: این جام‌جهانی فاجعه بار است، فاجعه‌ بارترین. فیفا باید هر مشکلی را که وجود دارد، حل کند. اما متاسفانه از همان ابتدا نتوانستند چیزی را حل کنند. اکنون دوباره برای رفتن به تیخوانا سفر خواهیم کرد، بدون ریکاوری. این منصفانه نیست. اگر این از نظر فیفا…</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/136774" target="_blank">📅 00:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136773">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
وکلای باشگاه پرسپولیس گفتن جذب کسری طاهری خیلی پر ریسکه! باشگاه پرسپولیس مجدد از یه وکیل خارجی داره مشورت میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/136773" target="_blank">📅 00:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136772">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
در حرکت رونالدینهویی هایجک خوردیم و اخباری رفت به گل گهر و شاگرد رحمتی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/136772" target="_blank">📅 23:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136771">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔘
🔘
امیر عابدزاده هم تنها گلر بزرگسالی هست که سهمیه لیگ برتری محسوب نمیشه چون لژیونر بوده   جذب گلر بزرگسال اشتباه بزرگیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136771" target="_blank">📅 23:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136770">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔘
🔘
امیر عابدزاده هم تنها گلر بزرگسالی هست که سهمیه لیگ برتری محسوب نمیشه چون لژیونر بوده   جذب گلر بزرگسال اشتباه بزرگیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/136770" target="_blank">📅 23:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136769">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
شنیده‌ها: با توجه به عدم جذب اخباری احتمالا یا رفیعی برگرده یا گوهری که بازیکن آزاد جذب بشه
🚨
پ.ن: برای گلر دوم رفیعی یا گوهری هم جوابه بعید برن سراغ گلری که قرارداد داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/136769" target="_blank">📅 23:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136768">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
در حرکت رونالدینهویی هایجک خوردیم و اخباری رفت به گل گهر و شاگرد رحمتی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/136768" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136767">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⚠️
⚠️
اخباری قرار بود امشب رسمی بشه ولی انگاری تماس مهدی رحمتی باعث شده به فکر رفتن به گل‌گهر بیفته ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136767" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136766">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🫥
🫥
حالا باید بگردیم دنبال دروازبان مطمین برای ذخیره پیام ...حالا چرا این وسط چرا رفیعی رفت دلیلش معلوم نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/136766" target="_blank">📅 23:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136765">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
در حرکت رونالدینهویی هایجک خوردیم و اخباری رفت به گل گهر و شاگرد رحمتی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/136765" target="_blank">📅 23:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136764">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1IWthz9QpWKk8gu9mhTeZ8BKP-hshUA8UNAL2oIGx8hUBKwrhjb33Jil4oO_NafSNeb9A4oEvpMhLNhk5J8vPiOW8IDLTQRaECvvpfxXTYyNxsu960nA0bX_JSjw3PF0Io9jEASK24Ra4ij6pbTfF77eQ_fjn6fII05a6-u-nk81niWdhVhFPkjvREgFxP-sUkMmD5Uv8-0mEHTrCho9RzTOf0VqqY9lKn6p4tjkwUKH-cQhp5RjXa4ezR-Dh4YduQHnAQHuvqhjV13ZebrT0nG6DdRfTyKTVL_IRlmI3D1SVs3X_qnf-VxW4DAvtVoNFgdn76yL1DZm5f95MmOGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📸
از بازی دوستانه امروز با نماینده فوتبال مصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/136764" target="_blank">📅 23:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136763">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
در حرکت رونالدینهویی هایجک خوردیم و اخباری رفت به گل گهر و شاگرد رحمتی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136763" target="_blank">📅 23:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136762">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
در حرکت رونالدینهویی هایجک خوردیم و اخباری رفت به گل گهر و شاگرد رحمتی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/136762" target="_blank">📅 23:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136761">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🚨
محمدرضا اخباری تا دو ساعت دیگه قرارداد شو امضا می‌کنه / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/136761" target="_blank">📅 23:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136760">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔻
⚽
ویدویی از حال و هوای پرسپولیسی‌ها در اردوی ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136760" target="_blank">📅 23:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136759">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🕹
هیجان واقعی کازینو؛ جایی که شانس و مهارت به هم می‌رسند
!
🎰
اگر به دنبال تجربه‌ای متفاوت و پر از هیجان هستید، بخش کازینوی وینکوبت بهترین انتخاب برای شماست. از بازی‌های کلاسیک مانند بلک‌جک، رولت و باکارات گرفته تا صدها اسلات جذاب با جوایز بزرگ، همه چیز برای یک سرگرمی حرفه‌ای فراهم شده است.
🎰
چرا کازینوی وینکوبت؟
• تنوع بالای بازی‌های کازینویی
• میزهای زنده با دیلرهای حرفه‌ای
• گرافیک و کیفیت فوق‌العاده
• بونوس‌ها و پیشنهادهای ویژه
• محیطی امن، سریع و کاربرپسند
🕹
همین حالا وارد دنیای کازینوی وینکوبت شوید و هیجان واقعی را تجربه کنید. شاید برنده بزرگ بعدی شما باشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/136759" target="_blank">📅 22:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136758">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🟠
🟠
🟠
مهدی عبدی در لیست مازاد مازیار زارع قرار گرفت.
✅
✅
چه بلایی سر خودت آوردی پسر..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136758" target="_blank">📅 22:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136757">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
فووووووووووری و رسمی؛ رای نهایی دادگاه پژمان جمشیدی صادر شد و نتیجه آزمایش تجاوز منفی اعلام شد و پرونده بازیکن سابق پرسپولیس و فوق ستاره فعلی سینما مختومه اعلام شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136757" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136756">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
ویسی:
❌
اومدیم که امتیاز بگیریم و میگیریم
🎗
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐️
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/136756" target="_blank">📅 22:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136755">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❗️
رامین رضاییان نام استقلال رو از بیو پیجش پاک کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136755" target="_blank">📅 22:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136752">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oif5Vh5zwBXyxXGrjkpeB_xgKvdVJWtcP89akgOVirpA2IrgsB6-YnzYzrvJzh9D_bxwpQGvitErEuHwdxA1HdURmLyRwW-aANUwoVWcnedkf-U9LhgVemQqU1MXx__vzXTn3xVJko_AdJKaCvHi6hj2sonaZjAPg2VpuyEPQwxW_MgPNJ9bip_CW8L_nfQSSbVAwBllb9GzuThnF0Y8DCDGxA6IbpGYaLLWeTU_cbVsVxl-p0jgEmiB5ddgPRhA4rIeoDaPrCG0bsReowhsDVW47-5JZlo-4DbW0Fw2LFmJpkzTlHCkGHSiwxEO0NdLk3q6KyZMJExLA2YbU79Nnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فووووووووووری و رسمی؛ رای نهایی دادگاه پژمان جمشیدی صادر شد و نتیجه آزمایش تجاوز منفی اعلام شد و پرونده بازیکن سابق پرسپولیس و فوق ستاره فعلی سینما مختومه اعلام شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/136752" target="_blank">📅 20:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136751">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726dada166.mp4?token=DWMsh0S4Uv3n8bqzJ4utbvi2zrh6Xawx3YbUBRcRBkZUwKjc9CXsHnKPWE_UtQB37iqAjkavG7ZG6Nipwj_yhE4N-QhNwXjAzt1-euiYg5fR1NVF2tHYV2mJbEJN2mwSBVgH6KBB808ZsmKuDC6bweWkfo0rJAI_APMUpQ2lAp5btouwXqGFPUCB0zPp1gdj39Klth1It0uF8eYcEr21LT3DBdTknKiAgHOlQkPdVz4CiPXHqlk5U4mynQz50f79pjhwT1kGTPZiKZTGilyxqfkz9Gglz9juYn3KzZpInMhpyvvklemn0MqrzXXgfjha4wVhCKarBYYYm5p_Lwrl1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726dada166.mp4?token=DWMsh0S4Uv3n8bqzJ4utbvi2zrh6Xawx3YbUBRcRBkZUwKjc9CXsHnKPWE_UtQB37iqAjkavG7ZG6Nipwj_yhE4N-QhNwXjAzt1-euiYg5fR1NVF2tHYV2mJbEJN2mwSBVgH6KBB808ZsmKuDC6bweWkfo0rJAI_APMUpQ2lAp5btouwXqGFPUCB0zPp1gdj39Klth1It0uF8eYcEr21LT3DBdTknKiAgHOlQkPdVz4CiPXHqlk5U4mynQz50f79pjhwT1kGTPZiKZTGilyxqfkz9Gglz9juYn3KzZpInMhpyvvklemn0MqrzXXgfjha4wVhCKarBYYYm5p_Lwrl1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گل پرسپولیس به تیم مصری توسط بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/136751" target="_blank">📅 20:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136750">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⚡️
⚡️
🚨
🚨
🚨
🚨
فووووووووووووری
✅
محمدمهدی محبی نهایتا امشب یا فردا قرارداد شو امضا می‌کنه
🔽
تمام توافقات با کلبا نهایی شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/136750" target="_blank">📅 20:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136749">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">⚠️
⚠️
نیمه نخست دیدار تدارکاتی پرسپولیس و پیرامیدز مصر با نتیجه صفر - صفر به پایان رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/136749" target="_blank">📅 20:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136748">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🏅
ترکیب پرسپولیس برابر پیرامیدز مصر
💢
پیام نیازمند، حسین ابرقویی، سین کنعانی‌، علی رضا همایی فرد، مجید عیدی، پویا پورعلی، مارکو باکیچ، مهدی تیکدری، محمد عمری، علی علیپور، ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/136748" target="_blank">📅 19:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136747">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">💠
💠
💠
آخرین خرید ها از زبان قدوسی:
😀
با محبی به توافق کامل رسیدن
🔹
اخباری تا چند ساعت آینده امضا می کنه
😀
ایری و طاهری هم باشگاه داره محکم کاری می‌کنه تمام شدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/136747" target="_blank">📅 19:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136746">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
اعضای کادرفنی تیم پرسپولیس :
🔴
سرمربی : مهدی تارتار
🔴
دستیار مربی: وحید فاضلی
🔴
دستیار مربی: علیرضا محمد
🔴
دستیار مربی  : رضا جباری
🔴
دستیار مربی  : کریم باقری
🔴
مربی دروازه بان : حسین اینانلو
🔴
مربی بدنساز: یاگو
🔴
آنالیزور: میعاد قاسم زاده و محمد کهن  …</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/136746" target="_blank">📅 18:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136745">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">💠
💠
💠
آخرین خرید ها از زبان قدوسی:
😀
با محبی به توافق کامل رسیدن
🔹
اخباری تا چند ساعت آینده امضا می کنه
😀
ایری و طاهری هم باشگاه داره محکم کاری می‌کنه تمام شدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/136745" target="_blank">📅 18:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136744">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">https://www.facebook.com/100050246329900/videos/1060805676383532
لینک پخش زنده بازی پرسپولیس _ پیرامیدز مصر داخل فیسبوک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/136744" target="_blank">📅 18:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136743">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🏅
ترکیب پرسپولیس برابر پیرامیدز مصر
💢
پیام نیازمند، حسین ابرقویی، سین کنعانی‌، علی رضا همایی فرد، مجید عیدی، پویا پورعلی، مارکو باکیچ، مهدی تیکدری، محمد عمری، علی علیپور، ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/136743" target="_blank">📅 18:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136741">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
خبرنگار پرسپولیس:
🔴
امروز محمدمهدی زارع و پویا پورعلی در تمرینات عالی ظاهر شدن .تیکدری هم مثل همیشه خوب بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136741" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136740">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⚠️
☹️
کانال ۱۴ اسرائیل مدعی شد: ایران دستور توقف کل حملات به کشور های عربی را صادر کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/136740" target="_blank">📅 17:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136739">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
تایم و رقبای سه دیدار دوستانه پرسپولیس در اردوی ترکیه مشخص شد.
❌
سرخپوشان در تایم های 8،4 و11 مرداد ماه با  تیم‌های «پیرامید»، «آنالیا اسپورت» و یک تیم دیگر به رقابت می‌پردازد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/136739" target="_blank">📅 17:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136738">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">💛
حسن روشن علیه قلعه‌نویی و فدراسیون
💢
حسن روشن:
«۱۴۰ میلیارد برای قلعه‌نویی ناچیزه؟! خدا رحم کرد تیم حذف شد! لابد اگر صعود می‌کردند به قلعه‌نویی و بازیکنان هرکدام یک استان می‌دادند!»
• روشن همچنین پیشنهاد فدراسیون برای تمدید قرارداد قلعه‌نویی به شرط قول قهرمانی در جام ملت‌ها را «خنده‌دار» دانست و گفت چنین پیشنهادی اصلاً منطقی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/136738" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136735">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⚡️
⚡️
🚨
🚨
🚨
🚨
فووووووووووووری
✅
محمدمهدی محبی نهایتا امشب یا فردا قرارداد شو امضا می‌کنه
🔽
تمام توافقات با کلبا نهایی شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/136735" target="_blank">📅 17:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136734">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔹
🔹
🔹
فوری/کانال ۱۴ اسرائیل:
🔹
ترامپ دستور توقف تمام حملات به ایران را تا اطلاع ثانوی صادر کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/136734" target="_blank">📅 17:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136733">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
شنیده می‌شود در صورتی که امیر قلعه‌نویی قول قهرمانی ملی پوشان در جام ملت‌ها را بدهد، در تیم ملی ماندنی خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136733" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136732">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
❗️
محمد مهدی محبی با عقد قراردادی سه ساله رسما و شرعا به پرسپولیس پیوست / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/136732" target="_blank">📅 17:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136731">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
خبرنگار ورزش سه حاضر در ترکیه: محمدرضا اخباری هم اکنون در تمرینات پرسپولیس حضور داره و تیم رسانه ای پرسپولیس در چند روز گذشته هیچ عکس یا فیلمی از تمرینات گلر های پرسپولیس نمیزارن / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
…</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/136731" target="_blank">📅 17:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136729">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
#تسنیم؛ پرسپولیس سفت و سخت افتاده دنبال علی نعمتی و میخواد با یه جلسه حضوری کارو تموم کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/136729" target="_blank">📅 15:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136728">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/136728" target="_blank">📅 15:29 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
