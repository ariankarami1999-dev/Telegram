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
<img src="https://cdn4.telesco.pe/file/F4jCF1Cm2B3UF3Rz1yfhetGH6jaF4tswcKSQ0dOy90Aa7b0o2lFQD3pj4jPddHWAFhvHm8O1xNtEi6QxO3keeogNiZtn5z6skfvG0HbIxxRUUZmDYO06vovUiJtkVF04f_YkwkNKir_yZ-Dmiaju3ekI1ydnKOa_3JcZlKZ3qNDFARd_OV7Medg4czOxAa0IJgkpZcy00LeT_elI9BbYDfzKwwV7hj-GT1DafnjYx_jZgiV2sK97dEtHbyUEolvvHicOILommkxvFk61uIcqWflp3G15ZdZUM9F5PDJWQ_ZDpdiWkMCje_ooWytUa7g9WkMJII6V4-qI3knec3UYSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 15:05:25</div>
<hr>

<div class="tg-post" id="msg-139851">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✔️
✔️
تارتار: ما از تصمیم سازمان لیگ شوکه شدیم و درخواستی برای لغو بازی با خیبر نداشتیم؛ ما منتظریم تا بازیمونو سر وقت اعلام شده انجام بدیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 857 · <a href="https://t.me/SorkhTimes/139851" target="_blank">📅 14:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139850">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
تارتار: ما از تصمیم سازمان لیگ شوکه شدیم و درخواستی برای لغو بازی با خیبر نداشتیم؛ ما منتظریم تا بازیمونو سر وقت اعلام شده انجام بدیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/139850" target="_blank">📅 14:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139849">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
با اعلام سازمان لیگ، ۴ دیدار از هفته هفتم لیگ لغو و زمان جدید برگزاری آنها متعاقباً اعلام خواهد شد.
✔️
ذوب‌آهن - سپاهان
✔️
خیبر - پرسپولیس
✔️
ملوان - فولاد
✔️
فجر سپاسی - آلومینیوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes…</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/139849" target="_blank">📅 14:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139848">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔔
🔔
فووووووووری
🚨
مهدی تارتار با لغو بازی با خیبر مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
〰️</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/139848" target="_blank">📅 14:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139847">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6BUMCqRVZ56P4LyerUZMdBA5MoZRikRcswNrfhsuy4yGMELSJl7jeQ3ZA74wAXcLthFTSHoHN7eAoUOY1j-WdADADWolA8drmmQx6u4bnsYrLjORjWgkew1PCEBU0Rx0rJt_f5skrIVoDCuJTiJG_5OyC00yho4rS48H6H9faXGDZrpWF3gavgi49GBznfDUPsyp9gm1yZ26YkoAdf3dTtEQqaSE2Oq56h4hepviiKIiyGf9HIskwDHV3qXquRdmwBKZtvcXfH7C3HJRDP1qIFTGuHklfQiMMb7LM8xsbr5sto81_2o3HV4ctX0q8jXVHOXTh7u3nCoAlxDLVOkCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبرد مونیخ؛ بایرن آماده‌ی شکار بودوگلیمیت!
⚽️
بایرن با مالکیت و فشار هجومی بالا، شانس اول این دیدار است؛ اما بودوگلیمیت نشان داده مقابل تیم‌های بزرگ با جسارت بازی می‌کند.
انتظار می‌رود بایرن از همان ابتدا برای گل زودهنگام فشار بیاورد و برتری کیفی‌اش را به نتیجه تبدیل کند.
[
بایرن‌مونیخ
⚽️
🆚
🇳🇴
بودوگلمیت
]
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SorkhTimes/139847" target="_blank">📅 12:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139846">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
✔️
پرسپولیس-خیبر فعلاً طبق برنامه
🔺
باشگاه پرسپولیس تا این لحظه هیچ درخواستی برای لغو دیدار مقابل خیبر ارائه نکرده، با توجه به شرایط موجود، این دیدار طبق برنامه قرار است یکشنبه برگزار شود، مگر اینکه در ادامه تصمیم جدیدی در این خصوص اتخاذ شود  «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/139846" target="_blank">📅 12:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139845">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
یحیی گل‌محمدی: فکر نمی‌کردم لوکادیا روزی در جام جهانی مقابل آلمان بازی کند/ او یک بازیکن حرفه‌ای بود/ از روزی که در تمرینات حاضر شد مربیان از نوع تمرینات‌ش راضی بودند/انگیزه زیادی از خودش نشان داد/ لوکادیا یک مهاجم شش‌دانگ در محوطه جریمه بود
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/139845" target="_blank">📅 12:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139844">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔵
رسمی؛ رضا شکاری به پیکان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SorkhTimes/139844" target="_blank">📅 12:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139843">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
این بازی لغو نشه خیلی به نفع پرسپولیسه.
✔️
✔️
تیم به هماهنگی نسبی قابل قبولی رسیده و دلیلی نداره الکی وقفه بیوفته.‌ خیبر هم توو اوج نیست!
✔️
✔️
ضمن اینکه سه بازیکن ملحق شده به تیم امید جزو بازیکنان فیکس ما نیستن که جای نگرانی داشته باشه.
✔️
✔️
تقویم رو بی‌دلیل…</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/139843" target="_blank">📅 11:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139842">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❤️
علی علیپور:
🇮🇷
🇮🇷
واقعاً افتخار بزرگیه که اسمم کنار علی آقا پروین، اسطوره بزرگ پرسپولیس قرار بگیره. خوشحالم که با کمک همه هم‌تیمی‌هام تو این سال‌ها تونستم تعداد گل‌هام رو به 96 برسونم  ﻿
🔴
ولی حتماً از قول من بنویسید که میراث، رکوردها و افتخارات علی آقا…</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/139842" target="_blank">📅 11:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139841">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
این بازی لغو نشه خیلی به نفع پرسپولیسه.
✔️
✔️
تیم به هماهنگی نسبی قابل قبولی رسیده و دلیلی نداره الکی وقفه بیوفته.‌ خیبر هم توو اوج نیست!
✔️
✔️
ضمن اینکه سه بازیکن ملحق شده به تیم امید جزو بازیکنان فیکس ما نیستن که جای نگرانی داشته باشه.
✔️
✔️
تقویم رو بی‌دلیل…</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/139841" target="_blank">📅 11:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139840">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
عبدالله ویسی بعد از باخت مقابل پرسپولیس، از سرمربیگری ذوب‌آهن استعفا داد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/139840" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139839">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
✔️
سازمان لیگ به باشگاه اطلاع داده اگه میخواین میتونید طبق قانون بازی تون مقابل خیبر لغو کنید و بازی نکنید حالا قراره تارتار امروز تصمیم نهایشو بگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/139839" target="_blank">📅 09:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139838">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
باشگاه‌هایی که درخواست تعویق بازی‌هایشان را داشته باشند ممکن است دیدارهای آنها لغو شود.
🔴
پرسپولیس هم ۳ بازیکن در اختیار تیم امید قرار داده. در صورت معوق شدن بازی‌ها، فشردگی بازی‌های آینده‌شان بیشتر می‌شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/139838" target="_blank">📅 09:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139837">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
باشگاه‌هایی که درخواست تعویق بازی‌هایشان را داشته باشند ممکن است دیدارهای آنها لغو شود.
🔴
پرسپولیس هم ۳ بازیکن در اختیار تیم امید قرار داده. در صورت معوق شدن بازی‌ها، فشردگی بازی‌های آینده‌شان بیشتر می‌شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/139837" target="_blank">📅 09:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139836">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OV_zhpFyHYk3QXMt6UGeYO48pAFsk43fQSKUFK1wf-QpHswjTGYuH7ABl6ToWk9lswqYh4AxeJphPmvuCDwCFEgJTFAAa3oH2auUJBmgRZWh-WA2WaG_mqZ8OQrmSZmhLoI1WQzOhKGw3hjkfySCtAduB6KzY8gZNLv-t_MuGA8Cm8Ks6_W7a3luE0P6xIsbnf7EaCl6cV0zV1NRfV3lGT_7tj3VqaN-HqhPqgAV98Dqk9t3MqXeibiWPkymY3L16FhqKkzl0UPfISEzhb_U520AsgjDPiGTcJNmGRvHPvE2TulnLhIRjDnCwTofysJgOD7x-e0DTjFS-A6MXBJNkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/139836" target="_blank">📅 09:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139835">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAx4COnqHRRLpAnu9XnG2zt3g6019UKH_4Ekgp7N_gf-kVF8QMlz0R6Nepderz8V-9u9wFV0mSwyFxTqVmUrlCpIsR4fq9ThpKRdxVTVjnsWV5QCh6SB6wK3iN1HUCwGuLcnl0zAS7ZKX2qjBBS0wEfeEmzsoRHCvhLjoJIrTq8UITImoxkzm14mRi7WjcaDH_Z2RiJPEvHEM8lSNWJ7fdSbhS0M39zEKkUGp9O3KxQokl1j_gstD06Iwl5rxWxJKdDTpfdIgMWYOorcTdmhuHg5zDbdIkySEMbccl7FhnQ1DrWBBPj7dUFvO8u0O1Xm3DhQdq93sFyZ1yWVaJ-F6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
جدال قدرت با جاه‌طلبی در یواس اوپن
[
الکساندر زورف
🆚
بوتیک فان دِ زاندشولپ
]
⏰
بامداد پنجشنبه ساعت
۰۳:۰۰
🎾
زورف با اتکا به سرویس قدرتمند و عمق ضربات از انتهای زمین، دست بالاتر را دارد؛ مخصوصاً اگر بتواند رالی‌ها را کنترل کند.
زندشولپ اما با سرویس و بازی مستقیم می‌تواند ست‌های نزدیک و تای‌بریک بسازد و زورف را تحت فشار بگذارد. با توجه به فرم اخیر زورف در US Open، کفه ترازو به سمت زورف است.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
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
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/139835" target="_blank">📅 01:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139834">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
باشگاه‌هایی که درخواست تعویق بازی‌هایشان را داشته باشند ممکن است دیدارهای آنها لغو شود.
🔴
پرسپولیس هم ۳ بازیکن در اختیار تیم امید قرار داده. در صورت معوق شدن بازی‌ها، فشردگی بازی‌های آینده‌شان بیشتر می‌شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/139834" target="_blank">📅 00:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139833">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
احتمال لغو چند دیدار از هفته هفتم لیگ برتر
✔️
برخی باشگاه‌ها از جمله سپاهان سه بازیکن در اختیار تیم ملی امید قرار داده‌اند و به‌این‌ترتیب احتمال دارد برخی از مسابقات هفته هفتم در روزهای شنبه و یکشنبه لغو شود.
✔️
✔️
باشگاه‌هایی که درخواست تعویق بازی‌هایشان…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/139833" target="_blank">📅 00:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139832">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❤️
❤️
حدادی در بین هواداران، بعد از بازی با ذوب آهن.
✔️
هوادار:
❌
دمت گرم با این تیمی که بستی، تا آخرش همینجوری وایسا.نیم فصل دو تا ضعف رو برطرف کن، بخدا تا آخر فصل ازت حمایت میکنیم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/139832" target="_blank">📅 00:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139831">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381bd5fd51.mp4?token=SM7Sk7xsMzbMI7gLddiECtpS3hd-cQFH6SUya1nZ9-s8xAHEv4qxUjRHjKjpirljFvYFttdaB68KtYpPeOz6SwlRIJmpQi_e6rke6hbiX4PA3Ip_VcLQIx6SevoztfHjKN10euC0CqQT-RW-GJORcAEvumVsYwj1V_nZ6mpojgnRhHuEURVJ97l0vXxsJT8hX_px2yaYAyRvXaLRPYmzSj5mWFvIp7aQKRYDoc19zEw5MGR1teTUKyAaBZ67q9yBSaLLnbbjgV7NF1R3vz5Lo0YFxyLZjig27v3qCpBBtWp6SoMLqS3O13VKk8h2ZzE48ogzs-7QCAGRfBWOEjTogQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381bd5fd51.mp4?token=SM7Sk7xsMzbMI7gLddiECtpS3hd-cQFH6SUya1nZ9-s8xAHEv4qxUjRHjKjpirljFvYFttdaB68KtYpPeOz6SwlRIJmpQi_e6rke6hbiX4PA3Ip_VcLQIx6SevoztfHjKN10euC0CqQT-RW-GJORcAEvumVsYwj1V_nZ6mpojgnRhHuEURVJ97l0vXxsJT8hX_px2yaYAyRvXaLRPYmzSj5mWFvIp7aQKRYDoc19zEw5MGR1teTUKyAaBZ67q9yBSaLLnbbjgV7NF1R3vz5Lo0YFxyLZjig27v3qCpBBtWp6SoMLqS3O13VKk8h2ZzE48ogzs-7QCAGRfBWOEjTogQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ ویدئویی منتشر کرده که تو پایانش بخشی از سخنرانیش تو زمان شروع حملات مشترک آمریکا و اسرائیل به ایران آورده شده: «خطاب به مردم بزرگ و سرافراز ایران، امشب می‌گویم که ساعت آزادی شما نزدیک است. وقتی کار ما تمام شد، حکومت خود را به دست بگیرید. این حکومت از آنِ شما خواهد بود.»
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/139831" target="_blank">📅 00:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139830">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95197e80eb.mp4?token=mAbZ4vmGOi7Su8JSmZI3QvA60WnNB0TXlTC6EzQZ8YaAWdvfmruBUR38LDeD7PGqAhZPXbVPPsj5vmQQ5wfADbt6--zAP5nva3YXdHmfEpNBhXLmpWCj-Nw27sZ2eIqxp45SMUWW8FZYwD8oP878XTgpyOlytnT9V4TWfgm4prCLqVBn1EGTuk-OAvMe3G4-Velef6-UI8Cy9sLTeydvkNs5P-7d03q9oRyoGkGy2vRcfttJfHdrXA34TxFAhrW7-0cnvLLPzS_MK3S-JI9DSqXm8IXfERcM069NT5nGCPlzxOGi5DzRK2qOX-UwrSXKqi6L5sHSVAuZFsdG21YN_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95197e80eb.mp4?token=mAbZ4vmGOi7Su8JSmZI3QvA60WnNB0TXlTC6EzQZ8YaAWdvfmruBUR38LDeD7PGqAhZPXbVPPsj5vmQQ5wfADbt6--zAP5nva3YXdHmfEpNBhXLmpWCj-Nw27sZ2eIqxp45SMUWW8FZYwD8oP878XTgpyOlytnT9V4TWfgm4prCLqVBn1EGTuk-OAvMe3G4-Velef6-UI8Cy9sLTeydvkNs5P-7d03q9oRyoGkGy2vRcfttJfHdrXA34TxFAhrW7-0cnvLLPzS_MK3S-JI9DSqXm8IXfERcM069NT5nGCPlzxOGi5DzRK2qOX-UwrSXKqi6L5sHSVAuZFsdG21YN_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
❤️
حدادی در بین هواداران، بعد از بازی با ذوب آهن.
✔️
هوادار:
❌
دمت گرم با این تیمی که بستی، تا آخرش همینجوری وایسا.نیم فصل دو تا ضعف رو برطرف کن، بخدا تا آخر فصل ازت حمایت میکنیم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/139830" target="_blank">📅 00:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139829">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
پزشکیان پیگیر حل مشکل آزمون برای همراهی تیم ملی
🚨
مسعود پزشکیان، شخصا پی‌گیر رفع موانع بازگشت سردار آزمون به تیم‌ ملی شده و به احتمال فراوان مشکل آزمون برای همراهی تیم‌ملی در جام‌ملت‌های آسیا حل خواهد شد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/139829" target="_blank">📅 00:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139828">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✅
نیویورک‌تایمز: آمریکا و اسرائیل احتمالا هفتهٔ آینده به ایران حمله می‌کنن و تو جنگ سوم تأسیسات هسته ای ایران به شدت هدف قرار میگیرن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/139828" target="_blank">📅 23:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139827">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❤️
❤️
❤️
علی علیپور با گل امشب رکورد علی پروین را شکست و دومین گلزن برتر تاریخ پرسپولیس  شد
😀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139827" target="_blank">📅 22:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139826">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
برانکو: هر روز به بازیکنان می‌گفتم پرسپولیس بزرگ است و نباید معمولی باشید
❌
❌
به شاگردانم که مربیان بزرگی شده‌اند افتخار می‌کنم
❌
بدترین روز زندگی‌ام، روز از دست دادن جام مقابل استقلال خوزستان بود
❌
❌
اگر به عقب برگردم باز هم پرسپولیس را انتخاب می‌کنم
❌
می…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139826" target="_blank">📅 22:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139825">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری
❌
با اعلام کفاشیان، جام فصل قبل به کیسه‌کشا داده نمیشه و باید برگردون تو غار  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/139825" target="_blank">📅 22:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139824">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
تسنیم: پرسپولیس بیش از حد به بیفوما وابسته شده؛ بدون او سرخ‌ها توانایی خلق موقعیت ندارند!
✔️
نظر شما چیه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/139824" target="_blank">📅 22:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139823">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
✔️
هفت ورزشی: فدراسیون با اعلام استقلال به عنوان قهرمان فصل گذشته موافقت کرد
🙁
🙁
🙁
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/139823" target="_blank">📅 22:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139822">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTzGQRNosMTJKsgiumCdi5pCjSVomzm-KKXDsfRdSaa6vpRli3nM9_r06-FwydqdZDxLX-lLxKus8Rq1_Jx6fmQgYx2CAYuy3XXLlrr59A_pCo8JqRpPt4yPm0LwCDyVe6yb7C1XLfq8VMpQ--XNGyJqsuTrRdWi4_8kvVchMW14Iqebe_yIUdYChz_BpnVrS_KEbuJbO8qDz6aezsRZRBqepVxRnfx4__ZEsZuB7K87Kj7C9KlMND6bEm57ycySsdb_-OP5DU1mJ7jA5nJEmSww4301ydd5Yo7G8lU4xNq5kb-WE_R54mTJcwRVZd9wN9qPME-txgoe3cAhqvFrqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یه جام از منیریه پرت کنید جلوی این کصخل تا خودشو نگاییده
😂
😂
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139822" target="_blank">📅 21:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139821">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcUdPuNrih6vD2jcUh-ikWIGBrM9tLVuwEquK1MD0TXo1T5weqFEuudNL3Vh9xCzRiH1rCda2aE3I-mQeXpYAUZ_yHl-_-3wgS100Axz7RuLotbm7ZCMgWLpqL3k8ZOPRXcaEM4ozvqqCq7gzutxFXwZqPA7y-h9SZ9a85ziv-Bd2rVLyCWTrV9nQTwZONwnsuXPqGNg5CldAoR3UOTFqCHD0Up3hoAH4v-FY4pFDfzkxAX3AafTovypBiJRTxAvfa2yfwynE3fhSj4XAK5sA-BIYD7oU2gdtGWR10ods6ea9nVTbxh6-m7Y_EkqneQLI_wjHRs-I5-dXq72CNdNKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دوئل سنگین امشب؛ لیورپول در برابر اتلتیکوی سرسخت!
⚽️
تقابل فوتبال هجومی قرمزها با ساختار دفاعی و ضدحملات خطرناک اتلتیکو، نوید یک نبرد نزدیک و پُرتنش را می‌دهد.
[
لیورپول
🔴
🆚
🔴
اتلتیکومادرید
]
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
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
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139821" target="_blank">📅 21:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139820">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⚡️
⚡️
ترامپ:
⚡️
از نحوه مذاکره آن‌ها راضی نیستم من هنوز درباره ایران تصمیمی نگرفته‌ام، آنها نمیتوانند سلاح هسته ای داشته باشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139820" target="_blank">📅 20:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139819">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtZW31JMpStRMslhE-69ZJ9XpIWhUVJjwMwRPt2BaJ2WNjYgMh-UpPj8px7zoO5VeyconNC4NVQtCOG4-uwD4WWbYGQCKmVfTYZARypdJJGUHj1eJpzMIsEgcxXSWrk4YJKGT0ZZMMe7JV6OjB1fDne9Sx0wYuuzCr7qg-QOfA2itEss5V9aVgCM8VSldjhKpfNJTpQaWuBX2UcBQ2aBVNJwvBa2Jkf6d51JqUeEwj_68mWO4FP-9ioAVhdl1vjm1f7DWKIJYDwBUKxzJsDR8teEKT46SEVg0ffm49kzGcJLWFdyn1fLI98eHBC7eBl94k5VJ36iLPWxARzqig5iEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
پرسپولیس مدل دهه شصت
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139819" target="_blank">📅 20:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139817">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">😐
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139817" target="_blank">📅 20:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139816">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">😐
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139816" target="_blank">📅 20:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139814">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
✔️
✔️
✔️
✔️
فرهیختگان: دنیل گرا طی ۶ هفته که حتی یک ثانیه بازی نکرده ۳۳ میلیارد تومان پول گرفته!
😐
عجیب اما واقعی: دنیل گرا بدون یک دقیقه بازی برای پرسپولیس در این فصل، ۵۲۷۸۰۶ ریال قطر، حدود ۱۴۵ هزار دلار و یعنی ۳۳ میلیارد تومان پول گرفته است!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139814" target="_blank">📅 20:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139813">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7BGwjdE4rePVFHp2KP8gAnsWlxG8lg10Jta_K6VxTJbM4MN_MiFRgP7POIbs5r8iOQ_-DgwTETuyBGOpmi4IYR1fPIJiJjU7_3D2zXxlhds4VVURQjNNNTC1z2VWRt_0zIGtacl_gg94kLc-xU8smzKSuLrmCxNXl7ySmaYbMX8jCUpPz5hmkqKLEb-A6ZLnYu4SEbcbjj1nUvIRw6nkxjpKSBL49LJvJwqPR3gdxg3uZ1ffW2vqAYJQ7WAq1rviFP64sl_mQL9vVvbykCnqWE5qpGTeXWuC7Ym3HCCBwF7vL_2iEftPvSsjCDuf8noBVrlfzqVKR9r775YzheU2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام رسمی باشگاه پرسپولیس؛ اردوبادی کناره‌گیری کرد، صابری معرفی شد
‌
❌
سیدعلیرضا اردوبادی، رئیس پیشین هیأت‌مدیره باشگاه پرسپولیس، از عضویت در هیأت‌مدیره این باشگاه کناره‌گیری کرد.
❌
در پی این تغییر، حسین صابری به‌عنوان عضو جدید معرفی و با انتخاب اعضا، رئیس هیأت‌مدیره باشگاه پرسپولیس شد. مراسم معارفه وی نیز در نشست هیأت‌مدیره برگزار شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
‌</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139813" target="_blank">📅 19:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139812">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🗣
🗣
شهرآبادی، ایری و لطیفی‌فر به دلیل حضور در اردوی تیم ملی امید، بازی با خیبر را از دست دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139812" target="_blank">📅 17:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139811">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
سهراب بختیاری‌زاده در آستانه برکناری از سرمربیگری استقلال
❌
[ قدوسی - قرمزآنلاین ]  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139811" target="_blank">📅 17:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139810">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
سهراب بختیاری‌زاده در آستانه برکناری از سرمربیگری استقلال
❌
[ قدوسی - قرمزآنلاین ]  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139810" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139809">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
سهراب بختیاری‌زاده در آستانه برکناری از سرمربیگری استقلال
❌
[ قدوسی - قرمزآنلاین ]
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139809" target="_blank">📅 17:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139808">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
عضو پنجم هیئت مدیره پرسپولیس مشخص شد.
✔️
به نظر می‌رسد روند انتخاب عضو پنجم هیئت مدیره باشگاه پرسپولیس به مراحل پایانی رسیده و حسین صابری خورگو به عنوان عضو جدید این هیئت معرفی خواهد شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139808" target="_blank">📅 16:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139807">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
فوری؛ سردار آزمون پس از یک دوره غیبت به تیم ملی بازگشت و اسمش در لیست اولیه جدید تیم ملی قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139807" target="_blank">📅 16:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139806">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
❌
اسامی داوران هفته‌اول پریمیرلیگ ایران
😀
استقلال - مس‌شهربابک/موعود بنیادی‌فر
😀
سپاهان - چادرملو اردکان/امیر عرب‌براقی
🔴
پرسپولیس - شمس‌آذر/بیژن حیدری
😀
تراکتور - پیکان/کوپال ناظمی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139806" target="_blank">📅 16:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139805">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
⚠️
🇮🇷
تصویری از ناخن‌ بلند کنعانی زادگان در صحنه درگیری با آقاسی که در برنامه فوتبال برتر نشان داده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139805" target="_blank">📅 14:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139804">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
برانکو ایوانکوویچ سرمربی سابق تیم پرسپولیس بعنوان‌مشاورفنی زلاتکو دالیچ به کادر فنی‌اش در تیم ملی امارات اضافه شد و قراردادش رو امضا کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139804" target="_blank">📅 14:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139803">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
عالیشاه وکیل گرفت
❌
❌
شکایت عالیشاه از خداداد عزیزی به زودی در مراجع قضایی ثبت خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139803" target="_blank">📅 14:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139802">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139802" target="_blank">📅 14:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139801">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
رکورد تاریخی پرسپولیس
✔️
پرسپولیس با تفاضل گل +۹ بعد از ۶ هفته، بهترین شروع تاریخش رو ثبت کرده؛ آماری که فقط یک‌بار در لیگ سوم بازهم توسط پرسپولیس و یک‌بار هم توسط سپاهان در لیگ دوم تکرار شده بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139801" target="_blank">📅 14:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139800">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✔️
✔️
✔️
آمار جذاب پرسپولیس تارتار
✔️
گل‌های زده پرسپولیس تا هفته ششم در ۹ فصل اخیر بی سابقه‌ست که نشون دهنده هجومی بودن پرسپولیس در این فصل هست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139800" target="_blank">📅 14:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139799">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-nr4W4lsYRNBq9zyFnbHf8K7739rNNzbSiXIWbTGeBPfLLKVLrpv6GfVvFMXS3SloPHv9juHFVSbhaaSUckhfFwOv-LeZ4nUNu_CSZ0KdI_R3HiE2XNFzP8UngliwZ-iFjlhfJmKNB8es17wikF9pO-WBtJ_ejruREvY7NEDEt6JDF3CabFujMlVAjDKStYfwGd0gabpGu8ljB9OU3SXs-rJrq-4NxD7bOMPbxL-Ti-0yne2gBBiWwge9JIeYV3mJgnMAl85ljTiz1h12CQl1KJniPqFRYgBrFLB5_TrVLl00eRYgnOjosSSEjliw1omfREe_MkMt7Xa-xwINaTDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دومین شبِ جنون اروپایی
چمپیونزلیگ دوباره با نبردهای بزرگ برمی‌گردد!
⚽️
شب دوم لیگ قهرمانان با چند تقابل جذاب دنبال می‌شود؛ بارسلونا در خانه به دنبال شروعی مقتدرانه مقابل فاینورد است، در حالی که پاری‌سن‌ژرمن با توجه به برتری کیفی ترکیبش شانس بالایی برای کسب برد دارد. در حساس‌ترین بازی‌ها، ناپولی و آرسنال می‌توانند یک نبرد تاکتیکی و نزدیک داشته باشند و لیورپول مقابل اتلتیکو مادرید احتمالاً با بازی فیزیکی و کم‌فضایی روبه‌رو خواهد شد. اسپورتینگ و گالاتاسرای هم می‌توانند یکی از بازی‌های پرتحرک شب را رقم بزنند؛ در مجموع انتظار می‌رود چند دیدار امشب تا دقایق پایانی کاملاً باز و غیرقابل پیش‌بینی باقی بمانند.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار‌هارو رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139799" target="_blank">📅 14:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139798">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1QUJWF3O9_F49pLC_XfYpeprccoxTahDGZBYCxhkSSYGPZw4vp8QFrEpNbJzZpsADa2c8d54iXWZd2wM9M1PYkvQHwzJCjhhJtvKsapc2nMUrurME7LbWsVLBr6aMXOwJAiTTBKQmdTOtRR0q89jAR81UA9AbQoe0H3uNcqnG4fxSM8anQrIhu41Vd-HpcGIh7c6RTamWP_AjE046gyC5cAXTDkwZNJtOgzlyTQIpHBtUcd5BqrMGsL2nDjUpM2P2cu5IY8eZ-yMCol8KdV4VMrLOarMpGi3ULH3YxX9YLAVzJGtO-MaGrzuBHH7l3r_fZYDNDHfNHrCl6NiXWAWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
فوووری از یاشار سلطانی
🔄
🔄
در پرونده فساد فوتبال برای تعدادی از مدیران ارشد و چهره های فدراسیون کیفر خواست صادر شده
🗣
🗣
مهدی تاج ، محمد مهدی نبی ، احسان اصولی ، تهمورث حیدی و خداداد افشاریان افراد مطرحی که کیفر خواست علیه آنان صادر شده و طبق قانون از حضور و فعالیت در فدراسیون و کار به طور موقت محروم می‌شوند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139798" target="_blank">📅 12:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139797">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpE2k4gfr58AGhna0ukiA03YxkTGzBIa5gEh_fPduj8qncg0vL69uAlFhTwEnu-GrrcwWxxI6oKDfyM3UPt7rZJNjc3kBxPmk7eI0WptSP-TrKBzlmAY79__uo0ZqnY8zpGvAMt_lQijVDNS5-weRz60MveiWMmYS-it_By2I4M_tBWd1PSeHYFqvWuSn8EzxViyaAYJA3L2fEAcLrfS2a_5Z0o_V8hlR5-pSUw-4JtH4fiw2usOe0UeJS5QmSsfsgKICPqwHhg0ecaoR_77xdDF_PPUN6l86htCXVAB2ACCRMayaANssTwLi1GyEEapgjXb6PoKs77-2xVt7sQEZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گفته می‌شود که باشگاه پرسپولیس تمایل دارد قرارداد علی علیپور و حسین کنعانی دو کاپیتان تیم را برای یک فصل دیگر تمدید کند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139797" target="_blank">📅 10:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139796">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
🇮🇷
پوریا شهرآبادی جوان ضمانت کننده آینده خط حمله پرسپولیس؛ یک خرید بسیار هوشمندانه از گل‌گهر که با استایل مناسب و دوندگی بالا در همین ۶ هفته ابتدایی که به عنوان بازیکن تعویضی به زمین اومده، نمایش قابل توجهی رو‌ رقم زده. امیدواریم با مدیریت درست کادرفنی و…</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139796" target="_blank">📅 10:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139795">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❤️
❤️
تارتار از امیر حسین محمودی خیلی راضیه و احتمالا مقابل خیبر زمان بیشتری بازی کنه//ورزش سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139795" target="_blank">📅 10:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139794">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
دکتر حقیقت: ما کارمونو بلدیم نگران نباشید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139794" target="_blank">📅 09:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139793">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa6dd97ad3.mp4?token=eHUq1nUnAr-naqR3s8FYwq-p5lWHDUZtdIIyNQq2O_133Nqp1eh45m-_R4MJoQHKTBki50QYdy_z055c-OE298g5BwGzE3cc2SSUNMTb8DYM8KcLztWgpH8_wnol7pwiCFVeMTjBp-ykZTnIYSxFT85onKoeeKuaScJNV_xUci0ZsAYnN9eBJY5BKqbCa1_TXMId0krLcwkO34X-kXKw0BDLuO3kP6A3ZtAb9MlZ_sQeOg1Qyob4BqaA0spBqfgHfeC-EXvlrPlDB6oY7V_cl0TsHlRxXcbF6GplnLNgiPAzMMVY3eO0uA1eQKy_oynp4gn_OFThLUAnPPOpdiwyJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa6dd97ad3.mp4?token=eHUq1nUnAr-naqR3s8FYwq-p5lWHDUZtdIIyNQq2O_133Nqp1eh45m-_R4MJoQHKTBki50QYdy_z055c-OE298g5BwGzE3cc2SSUNMTb8DYM8KcLztWgpH8_wnol7pwiCFVeMTjBp-ykZTnIYSxFT85onKoeeKuaScJNV_xUci0ZsAYnN9eBJY5BKqbCa1_TXMId0krLcwkO34X-kXKw0BDLuO3kP6A3ZtAb9MlZ_sQeOg1Qyob4BqaA0spBqfgHfeC-EXvlrPlDB6oY7V_cl0TsHlRxXcbF6GplnLNgiPAzMMVY3eO0uA1eQKy_oynp4gn_OFThLUAnPPOpdiwyJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🔴
دو گل پارس جنوبی به پرسپولیس در دیدار تدارکاتی دیروز.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139793" target="_blank">📅 09:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139792">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
سلام صبح همتون به خیر و شادی ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139792" target="_blank">📅 09:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139791">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qH2Mi6RPFARpPAhmMyHyfzpcdws9tzm_XqpH-fKYoAYiZGj889ejZ0pwdrOseSZrSDcQAfV859s8Wf0-yLd0_B4WLvfVORVd7diQZUCgu3UgqtmSUPXWz3e_63cnL4hoWxKELpAsUbcYtpL8XtDrhPEeDMozKm8sXdONrEw9jsFOKrUkKQx_6lFVu3eEp40ia8ewGAZBMZTNkVPlu77qkIv05bUs8YwPLAy6rI0wqL-BI1ZUAC2ZdcaqhzwfyuNEmOazucyanihjdd3bBH4Ts1yNj4J7odrarVNm9IYtuyxFBe83uQPtdlor3fu9aa-PiuEqjx36dn3jBr7MJvPk9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
نبرد قدرت و تکنیک؛ در یواس اوپن
🎾
Ben Shelton -
🎾
Alcaraz
🎾
آلکاراز از نظر کیفیت رالی، تنوع ضربات و توانایی تغییر ریتم برتری محسوسی دارد؛ در مقابل، شلتون با سرویس‌های قدرتمند و بازی تهاجمی می‌تواند فشار زیادی ایجاد کند. اگر آلکاراز روی سرویس شلتون موقعیت بریک بسازد و وارد رالی‌های طولانی شود، کنترل بازی بیشتر در اختیار او خواهد بود.
📌
مسابقه را فقط تماشا نکن؛ از هر امتیازش فرصت بساز و با ۱۰٪ بونوس اولین واریز پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/139791" target="_blank">📅 01:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139790">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✔️
✔️
زارع: جلوی خیبر نیستم ولی تلاش می‌کنم بازی بعدی باشم  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/139790" target="_blank">📅 00:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139789">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
زارع : حالم خوبه به زودی برمیگردم،  نفهمیدم چیشد پام به شیار های حموم گیر کرد و بغل پام پاره شد و بخیه خورده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/139789" target="_blank">📅 00:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139788">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
پرسپولیس امروز در دیداری تدارکاتی به مصاف پارس جنوبی جم رفت و در پایان ۲-۱ شکست خورد.
✔️
سرخپوشان در این بازی با ترکیبی از بازیکنانی که در بازی شب گذشته مقابل ذوب‌آهن حضور نداشتند و بازیکنان تیم جوانان خود این بازی را آغاز کرد و در ادامه به دلیل…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/139788" target="_blank">📅 00:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139787">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‼️
✔️
✔️
✔️
✔️
فرهیختگان: دنیل گرا طی ۶ هفته که حتی یک ثانیه بازی نکرده ۳۳ میلیارد تومان پول گرفته!
😐
عجیب اما واقعی: دنیل گرا بدون یک دقیقه بازی برای پرسپولیس در این فصل، ۵۲۷۸۰۶ ریال قطر، حدود ۱۴۵ هزار دلار و یعنی ۳۳ میلیارد تومان پول گرفته است!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/139787" target="_blank">📅 23:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139786">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
شرط سنگین گرا برای جدایی از پرسپولیس
✔️
✔️
شنیده‌ها حاکی از آن است که تارتار نگاه مثبتی به استفاده از این بازیکن در ترکیب تیمش ندارد و همین مسئله بار دیگر بحث جدایی گرا از پرسپولیس را مطرح کرده است.
✔️
✔️
دراین‌بین گرا برای جدایی از پرسپولیس خواهان دریافت…</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/139786" target="_blank">📅 23:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139785">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
بازی رئال مادرید و اینتر هم شروع شده که رئال  دو گل زده تو سی دقیقه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139785" target="_blank">📅 23:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139784">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
اگه اینترنت‌تون امروز بیش از حد ضعیف شده؛
✔️
طبق اعلام مدیرعامل شرکت ارتباطات، دلیلش اینه که فیبرنوری تو ارمنستان
🇦🇲
قطع شده و دارن فعلا پیگیری میکنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139784" target="_blank">📅 22:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139783">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnEyw6TIRhwHNvSTHx6hi_C6V3QSvYkv2YYTufatONzd2dF1y_w5kOPBzoz9RM9G0s5dB1tOpClisXc9dPvXybK-MA3t0ANChKtrw9SwtwJja7i93tpmSrs4-QKFRj0isQDqH5oTE3zaCbH-BU8Nnl7abcEVN2huSoHF1zdgTyjT8xHJlcH4nxKzSJLQ4N1YaOgj7I5NTHEvq-Z_Nq08Fgj1HlweucorpRyuJOMOF_vA9cVpzBM2D-4Z0JgO5eKscswyiYhuYyHK02Gu0Y6jGLpssJofOggSp281v5m7psnohgNi6_sz2IU4ImeQHtahgrcAo6JtiNyp2IrmmwNKlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
اگه اینترنت‌تون امروز بیش از حد ضعیف شده؛
✔️
طبق اعلام مدیرعامل شرکت ارتباطات، دلیلش اینه که فیبرنوری تو ارمنستان
🇦🇲
قطع شده و دارن فعلا پیگیری میکنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/139783" target="_blank">📅 22:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139782">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A46B_kt1JrhlSGu6ExOpMOH6519Zo2Gzn8NNFDfkMFbjoXcs52TD-z_MUOkIL3hWWoT8tAiE6EkipMcm1k9H5M7ITbH9UC7R1HnJEkz1oGTlqr-jU7vIgD7UZR9oj1Irx2ewaJn0-37_b_7P-t96moCVWM7V-UmZfd82HL4NqH4J0-vq-9By206_AFS3K2mObTDk0EIXlUSlvjE3ehYMyYTmY7-_q6n55Iytpho3ckfb9g2C7E6zSjyZEJJ7hF_NZ50NMVqpxuXG6xMlvGMBHyWK7hZz0Mum1A8wiV2j4QUhJyCxE2Nj5Kvp2JXyyjRM7U6NqYXGxRGdrY7q-rwKbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
تیم ملی امید راهی ناگویا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139782" target="_blank">📅 22:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139781">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
✔️
فووووووری
🔄
با اعلام سازمان لیگ؛ فصل گذشته هیچ  قهرمانی نداشت و یه موز به استقلال رسید
😅
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139781" target="_blank">📅 22:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139780">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
دکتر حقیقت: پارگی نسبت بزرگ بود اما سعی میکنیم به بازی خیبر برسد حالش هم عالی بود تقریبا بیست دقیقه پیش مرخص شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139780" target="_blank">📅 22:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139779">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
فوری| زارع مصدوم شد!
⏺
محمدمهدی زارع بعد از تمرین و هنگام دوش گرفتن، پایش به‌شدت برید و ۸ بخیه خورد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139779" target="_blank">📅 21:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139778">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCDkEtNkMmiX6iMnMyLjdU_VzyES7SOorpzQiPXXSqueYjvY-QOY026dFnaWWHcO-AzH-cS1WUsAwgT1UjtU8RV-WoTgFONwbo5wzXCnWmuBfOfFplBjYRBPbZ6-fkh2wyt5qab0v18qQ0p1h-sSuj5Hf-80Qt1sBSt3o-cra0Cxi-0XsiJ55yNdcTkaS5Se-OmOo_HqM62Jacbe95qUdyIZUzfsgRaxD40NSK7yaxO848esapIC0QIWMlnKv8To1aeomNzIMIcnvQxDbNUApKQiOrREJrRH4s0wOamFRdVfJhOcxlvnvT2uS5qr6aH9jb6I5ODCCnSjYELCi03Oiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
💢
پاسپورت ۱۲ پرسپولیسی دریافت شد
💢
پاسپورت ۱۲ بازیکن پرسپولیس برای انجام امور مربوط به تیم ملی دریافت شده. نیازمند، کنعانی‌زادگان، ایری، زارع، لطیفی‌فر، محبی، علی علیپور و محمودی، هشت بازیکنی هستند که نام آنها در میان نفرات موردنظر قرار دارد.
💢
همچنین احتمال حضور محمد خدابنده‌لو و مهدی تیکدری در این جمع مطرح است، اما نام دو بازیکن دیگر هنوز مشخص نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139778" target="_blank">📅 21:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139777">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
فوری| زارع مصدوم شد!
⏺
محمدمهدی زارع بعد از تمرین و هنگام دوش گرفتن، پایش به‌شدت برید و ۸ بخیه خورد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139777" target="_blank">📅 21:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139776">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
فوری| زارع مصدوم شد!
⏺
محمدمهدی زارع بعد از تمرین و هنگام دوش گرفتن، پایش به‌شدت برید و ۸ بخیه خورد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139776" target="_blank">📅 21:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139775">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JogzYyYX_A1TVNOVycx07pm8HUGuOYfyZoB2aFYX0dyQBfVuPIq1sRDx0X6OhBBEgu_vEFBcEnOEdurnrMCGvmKz5-bn6kiWBCAvOnNaKaf44fNvpCSA9m5vEYj5mD1nPl0QZZ8v_EUs4I_gKwtjWTWoqsZxFclqTjCPeYyqVFJLR9b0xNxnqtjDtSxempE3ophhKRtVHclTgb44QHQnzhKOlyXHh2ph4GK9TrDTD_8yPTQMzWc0cvdeoreNZVfErIqUxNFQWhLNX92ek-lKrQoMva97eirtoqpFjYH1gQID2Es9z8LrcK7KOyyZxHyhamylbW6PBc4cwWLo1PmYsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
تارتار به ابرقویی آماده باش داده تا با تمرکز و آمادگی لازم برای بازی با خیبرخرم آباد آماده بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139775" target="_blank">📅 21:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139774">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bZFRB2Il9mZCxULZhstKDRbgrS15h9eq8ZLAhOuXGNqcV6EQvHbWwuOmxoTYfrCqzogvjxB4NKsnDZrSu6ffChDX76oWPBuqi1FMzdP6Fgf29xRk17OPX6BrsDbM2LbOkqUHtb7-7ywIuoeG7VtWEFW_NdSSQ3hPh17fg-Yfq2VSLTWNTlv1ewCDP5HQzTKgSVYRJAPU4lFaZr3k5Pih8qlGXR8dBJ3NUAjeu2cn37mIcIrLhQdwM8gfqqEE8gTg37flPULATk-Tn5_K7h4CDNbygZru9QovsjsqR4J_EdcDIB3Qvkj1hdrsRekRHArjMxrCfmUnAVmSJMz7B4hDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
پوریا شهرآبادی جوان ضمانت کننده آینده خط حمله پرسپولیس؛ یک خرید بسیار هوشمندانه از گل‌گهر که با استایل مناسب و دوندگی بالا در همین ۶ هفته ابتدایی که به عنوان بازیکن تعویضی به زمین اومده، نمایش قابل توجهی رو‌ رقم زده. امیدواریم با مدیریت درست کادرفنی و فرصت‌دادن دوباره به پوریا، شاهد درخشش دوباره این بازیکن باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139774" target="_blank">📅 20:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139773">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8Uq4BWznpN6Iak1_6UCcrmeTPVGsg50uJsrs-d0agQNRymU7a2BvCA7Duq5nEsIzL_RlfqFSai6WicpIGXG1i7qXJqEyjgaxEpylKQK7I4MUY-Ji18SMdX8x2P6Nig2rfQsZr8YH0WU6koEybM8rI1auQU3P_RXjlmv59-fD39LX9uy_khPkJiy1xJsCj7zm9vAwBk15YgP_9Tk9XxOaoTsYXECGMhPRcJ3Si2plDDQ77QL62KptjUdyz_Dlx00OKSQpZffFOoNGEvnR85bQSLGV6G1ghhR1TFRTmVhVd600T5FP1Iw4tWcCet7S4uM8PrId3n4oVqxNdQZfa6gWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش تصویری بازی دوستانه پرسپولیس - پارس جنوبی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139773" target="_blank">📅 20:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139772">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✔️
✔️
با توجه به مصدومیت محمدمهدی زارع و غیبت احتمالی او در بازی بعدی، ممکن است پرسپولیس با حضور دانیال ایری در تیم ملی امید مخالفت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139772" target="_blank">📅 20:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139771">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVZuVHsIn7IlbXvQmDVE1BnQX-wurjV6o8iQdDnwZuyik1dJ5a3xP7McFQCPjGC9PzsAwKL15JysucU68ei2wWDno904EUeUTdpwSVWqfoeVHxaxLI9v7Vh7uFU9ZITzjE4UraSeA4FD_Gqk1UNPat_zWukROFAa6I7XluJrMzoKRt2i9DsyS6Ts1cVgCdek1S8lZrGp5nGMMVjTUfnkZF5icMIR0N6jwdFknOZMaeFFS6fiNn7UiI11XzHGRjRcOekM0YCZpDY-T7RLIw-fiKe2ThEE5bBSgbKXACGIgRLdPCbsaWjHFHHuRIIu_3XNXRDRZ_88T-jHTxmWC2Bovg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شب‌های باشکوه اروپا در راه است!
جایی که رویاها، ستاره‌ها و جاه‌طلبی‌ها
برای فتح بزرگ‌ترین جام قاره به هم می‌رسند
.
⚪️
RealMadrid -
🔵
Inter
⏰
Tonight 22:30
🏟
Bernabèu
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
⚽️
برنابئو در انتظار یک شبِ کهکشانی
رئال و اینتر؛ کدام تیم پیروز خواهد بود؟
فرصت رو از دست نده و همین حالا وارد وینکوبت شو و پیش‌بینی خودتو ثبت کن.
🔗
لینک بدون فیلتر وینکوبت:
👇
🟣
wngd3co.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139771" target="_blank">📅 20:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139770">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
فوری| زارع مصدوم شد!
⏺
محمدمهدی زارع بعد از تمرین و هنگام دوش گرفتن، پایش به‌شدت برید و ۸ بخیه خورد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139770" target="_blank">📅 20:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139769">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
پرسپولیس امروز در دیداری تدارکاتی به مصاف پارس جنوبی جم رفت و در پایان ۲-۱ شکست خورد.
✔️
سرخپوشان در این بازی با ترکیبی از بازیکنانی که در بازی شب گذشته مقابل ذوب‌آهن حضور نداشتند و بازیکنان تیم جوانان خود این بازی را آغاز کرد و در ادامه به دلیل…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139769" target="_blank">📅 19:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139768">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
امید عالیشاه: بر اساس چه مدرکی من رو محروم کردید؟ من فحشی ندادم و چیزی نگفتم! اصلا در رختکن تیم ما بسته بود از کجا تشخیص دادید من بودم که منو محروم کنید؟  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139768" target="_blank">📅 19:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139767">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🤥
🤥
دنیل گرا مدافع‌مجارستانی پرسپولیس به مدیریت این تیم اعلام کرده با دریافت 400 هزار دلار حاضره قراردادش رو با سرخ‌ها فسخ کنه. به احتمال فراوان بزودی گرا فسخ خواهد کرد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139767" target="_blank">📅 18:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139766">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
بازیکنان دعوت شده به اردو  تیم ملی بزرگسالان از نگاه ورزش سه
✔️
پیام نیازمند
✔️
محمدمهدی زارع
✔️
محمدحسین کنعانی زادگان
✔️
مهدی تیکدری
✔️
محمد خدابنده لو
✔️
محمدمهدی محبی
✔️
علی علیپور  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139766" target="_blank">📅 18:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139765">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
پرسپولیس امروز در بازی تدارکاتی به مصاف تیم  پارس جنوبی جم می‌رود تا به بازیکن هایی که دیشب کمتر بازی کردند یا اصلا بهشون فرصت نرسیده، بازی بدهد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139765" target="_blank">📅 18:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139764">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEYG5paP4bRc2n9X6sbdAm4pACtRdS7qQAXnqHbppHgH-oEfTiE_J05PcyxNafsh41g5yHeJKJWqdCRcebyrqQi8GKM-vwHhQFChItyDVKwYdupZS37T0-EKvKoHQCJohIPUwa18ctJIRD4ZxmSUiijcZJPGuUOqXzx8HeezjVg0t-pF34nfdebbExfgQY-sZQLc_rU9m5hruxyHBlqJxzLwFX95tpckiYa54wxSPH6smOISiw9iprjkj0Vx85LvjMBttWp6bONKfPRTQV1bPm747wd_2QyPiwSHy7Y18UPaiF5r4shkMyUganhJvgLKS13kh47hDfUqIZggcgtLnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
تسنیم: پرسپولیس بیش از حد به بیفوما وابسته شده؛ بدون او سرخ‌ها توانایی خلق موقعیت ندارند!
✔️
نظر شما چیه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139764" target="_blank">📅 15:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139763">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEEXmm9lnPo0k1YJqxj4VddaOvd5O4acc7OJKjB2HTOyDXK0TMe83-JMpHwvab-gQ_wVPEbAwOpBEqR8YTmw6InM-Km30HrOW5xzggbonTZRERUzJoU5uo3IfTT1Hv4C0XrDxdFx74YFLoOFJ6MtEuY2AQBjHhulbQMdYHqDscBhKj5HcjUybGXEvih0GVPfYTgLddT2hE5qaBvkRuy5OmmlVwM3yaX0aCP1_LMmsNweB3ayR2GLFrI93Gna_N0Mb_7_W81jDszwnBr0_DLpi2g5uYejIO3VeeEQpDzZP4pzJ9gurlR1iJO38x8-zrBXjIyIZZCLEi18mMQImqaTmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
شهرآبادی، ایری و لطیفی‌فر به دلیل حضور در اردوی تیم ملی امید، بازی با خیبر را از دست دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139763" target="_blank">📅 15:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139761">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnlXXSLri3zbhCZhgUS5RH1coVZVzKnKHFJVoaVY2IQRr8uUjFjyp1n93w1AnFvHWi3Econmp0rwe2wL0MnZJSAhMAtOzpEBnzQi2wzTzTts-eEKtGgsv7Cg2nE2CZZNFuE3Y-Gdu0_j0BuxagZLEPr6MBnwOEyPHMyxwVQH0VkbCQX1aBe9Spo5pH8-UFuRfP55xc1JeO97Q3-B8n-2FRN1JMP78WdsQ49wsMX4y4pGhBbHq5W7txLpsLbNeZiMKCe0TkO1NBhWUGHzQRSX8OsJ5eYIQuI22zVnDTnUADbSZ48l6In9LaqFoVGZh63Vi50yECiSdPp10a7QJum99Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🔴
میرور: فوتبال سرژ اوریه به پایین ترین سطح کریرش رسیده و می‌خواد در لیگ دسته هفتم فرانسه در تیم محلاتی مونتینی-آن-گوئله بازی کنه و انتقال اوریه به دلیل تاخیر در ارائه مدارک از سوی فدراسیون فوتبال ایران به تعویق افتاده است!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139761" target="_blank">📅 14:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139760">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎙️
فرشید اسماعیلی:
✅
کابل VAR را کشیدند چون عجله داشتند که زودتر بروند؛ در گوشی به داور گفتند که پنالتی شده اما داور گفت من سوت پایان را زدم!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/139760" target="_blank">📅 14:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139759">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❤️
❤️
❤️
خداداد در طول این ۴ ماه حق ورود به هیچ کدوم از ورزشگاه‌های کشور رو نداره
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/139759" target="_blank">📅 13:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139758">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❤️
❤️
بیفوما که به تیم ملی کنگو دعوت شده بود دعوتو رد کرده و گفته تیم ملی من پرسپولیسه و به تیم ملی نمی‌رم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139758" target="_blank">📅 13:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139757">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✔️
✔️
پرسپولیس امروز در بازی تدارکاتی به مصاف تیم  پارس جنوبی جم می‌رود تا به بازیکن هایی که دیشب کمتر بازی کردند یا اصلا بهشون فرصت نرسیده، بازی بدهد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/139757" target="_blank">📅 13:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139756">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgL62CUND0aOd5AxKEm1xlcUFUTmPG6Z4BGA6YFG4O1hn06MPPWtD7jukT04VWgvegPlHMc3P01dYy3U-N11vlgRx_ztq0N9WNWjcQXRO3OIHyYyPpVynC3nclou_Nkina4d4fgALLucWcAIZDsJy7qdkHhzVZye1huJ37lvlf1uMAQOIsuzQEzUI7gIC1dokGOiauBqfi-QjNnbcgBJ_p1G4t0ZcvTxMEeM53qvvIeOE4a5VMIiex8XYiMyOxI27UNqZLnOsucmF1Lj6qRa7WZ281539lPbGlnWlewdZvR8WllCFt6nV2JJtH_KNdED_qp_SuQxEsyda0BjMTArTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رئال و اینتر؛ دو غول، برای یک شب بزرگ
⚽️
رئال با تجربه و کیفیت فردی بالاتر، اما اینتر با دفاع منسجم و ضدحملات خطرناک؛ دوئلی که می‌تواند تا آخرین دقیقه نزدیک بماند.
[
رئال‌مادرید
⚪️
🆚
🔵
اینترمیلان
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139756" target="_blank">📅 12:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139755">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❤️
❤️
تارتار از امیر حسین محمودی خیلی راضیه و احتمالا مقابل خیبر زمان بیشتری بازی کنه//ورزش سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139755" target="_blank">📅 12:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139754">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
✔️
تیم خسته اس ..ساق بچه ها خستگی داره ..امیدوارم نیمه دوم با آوردن صادقی و بیفوما و محمودی بتونیم از این خستگی رها بشیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139754" target="_blank">📅 11:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139753">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
محسن خلیلی مدیر پرسپولیس: ۸۰۰ میلیارد بودجه لازم تا ورزشگاه آزادی تا چند ماه آینده آماه شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139753" target="_blank">📅 11:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139752">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJHkNJdfn9T0xv5uyBECsIp_8NH9zW2d8sO4gm1obl7Gp2uNbROeeeMmVS7eynAtjRgJO4jKIcauR8O2YiV469ObC1aNerxmRVs-I4vKzGfBNVoFLf0oaITU1yJnDVYGkVvqCafgqf7DpsyeT_IGbjKOY7KMVzmpeP-xLSU_kJCC-vMY0YVxp-Gz6nII0DppRAESVSbT5dD2SjRrWm9F1-bqigCfAsMcDUxzoKuyBwQ6k2RvlfLYN55ew4Zxlj7vN-UstQZsGACxeC2_XxtU3gOLqf88YmuY2mgK0QnTObZCv3dQoZssn4eT46CuQtAtzCFfkYcJ6PXSRJ32IWO2Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ایری در پاسخ به یک هوادار: تا روزی که جبران نکنم، شرمنده شما هستم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139752" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139751">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: دنیل گرا با باشگاه قرارداد داره و  بازیکن ماست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139751" target="_blank">📅 09:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139750">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🗣
حجت موتوری مدیرعامل ترتر: به شجاع خلیل زاده و علیرضا بیرانوند در بازی با چادرملو فحش ناموس دادند، آیا این درست است؟
😂
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139750" target="_blank">📅 09:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139749">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/us47pevrVBNI7d_3u5gY8gef2XU6o0s7EvmhnMc82FRouf554PJPl-xuQzdrGuoaiJ3hRWi8duBhLDTqQXeLgvoaZvKfUQs73UiGO1-oe4gvOUpHG4AVQzrlc3KTOD0gMXZ-f6f_ak1rKybwkHtjPTfakWKmNAyd6RwFE4MkIovY8WkpotjBRrnG9h-QLcFas7HCUKthiaAz9mnKI8dyHEuDFLozkIpw9kYPDE0CciG_ruEBkYQxk49lO_lsalZLODCGjqjxGf-eeYbB3AC5Fui4oN7g8sQIeuzJQJgeBpwnzXX6_0HuKqnVeqDJ2pvEn9cgHZTsjERoqtOvRNqpPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
امید عالیشاه: بر اساس چه مدرکی من رو محروم کردید؟ من فحشی ندادم و چیزی نگفتم! اصلا در رختکن تیم ما بسته بود از کجا تشخیص دادید من بودم که منو محروم کنید؟
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139749" target="_blank">📅 09:17 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
