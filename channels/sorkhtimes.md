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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 19:02:49</div>
<hr>

<div class="tg-post" id="msg-139860">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
تارتار:سازمان لیگ بیجا کرده بازی مارو لغو کرده...ما هیچ درخواستی برای تعویق بازی نداریم و میخوایم بازی کنیم...  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/139860" target="_blank">📅 18:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139859">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
✔️
سازمان لیگ چرا باید سر خود همچین تصمیمی بگیره  وقتی باشگاه  نخواسته بازیش به تعویق بیوفته؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/SorkhTimes/139859" target="_blank">📅 17:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139858">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
✔️
چه دلیلی دارد بازی پرسپولیس خیبر لغو شود وقتی پرسپولیس درخواستی نداده و خیبر فقط یک ملی پوش دارد
❌
می دانیم بهاروند لرستانی است و لرستانی ها در فدراسیون قدرت دارند اما.......
✔️
می خواهید جام حذفی را برگزار نکنید؟بازی ها فشرده است؟بعد نزده می رقصید و…</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/SorkhTimes/139858" target="_blank">📅 17:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139857">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
✔️
✔️
سازمان لیگ چرا باید سر خود همچین تصمیمی بگیره  وقتی باشگاه  نخواسته بازیش به تعویق بیوفته؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SorkhTimes/139857" target="_blank">📅 17:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139856">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
✔️
چه دلیلی دارد بازی پرسپولیس خیبر لغو شود وقتی پرسپولیس درخواستی نداده و خیبر فقط یک ملی پوش دارد
❌
می دانیم بهاروند لرستانی است و لرستانی ها در فدراسیون قدرت دارند اما.......
✔️
می خواهید جام حذفی را برگزار نکنید؟بازی ها فشرده است؟بعد نزده می رقصید و…</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/139856" target="_blank">📅 16:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139855">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
✔️
✔️
چه دلیلی دارد بازی پرسپولیس خیبر لغو شود وقتی پرسپولیس درخواستی نداده و خیبر فقط یک ملی پوش دارد
❌
می دانیم بهاروند لرستانی است و لرستانی ها در فدراسیون قدرت دارند اما.......
✔️
می خواهید جام حذفی را برگزار نکنید؟بازی ها فشرده است؟بعد نزده می رقصید و…</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/139855" target="_blank">📅 16:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139854">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
✔️
چه دلیلی دارد بازی پرسپولیس خیبر لغو شود وقتی پرسپولیس درخواستی نداده و خیبر فقط یک ملی پوش دارد
❌
می دانیم بهاروند لرستانی است و لرستانی ها در فدراسیون قدرت دارند اما.......
✔️
می خواهید جام حذفی را برگزار نکنید؟بازی ها فشرده است؟بعد نزده می رقصید و…</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/139854" target="_blank">📅 16:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139853">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
✔️
سازمان لیگ چرا باید سر خود همچین تصمیمی بگیره  وقتی باشگاه  نخواسته بازیش به تعویق بیوفته؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/139853" target="_blank">📅 15:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139852">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
✔️
سازمان لیگ چرا باید سر خود همچین تصمیمی بگیره  وقتی باشگاه  نخواسته بازیش به تعویق بیوفته؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/139852" target="_blank">📅 15:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139851">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✔️
✔️
تارتار: ما از تصمیم سازمان لیگ شوکه شدیم و درخواستی برای لغو بازی با خیبر نداشتیم؛ ما منتظریم تا بازیمونو سر وقت اعلام شده انجام بدیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/139851" target="_blank">📅 14:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139850">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
تارتار: ما از تصمیم سازمان لیگ شوکه شدیم و درخواستی برای لغو بازی با خیبر نداشتیم؛ ما منتظریم تا بازیمونو سر وقت اعلام شده انجام بدیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/139850" target="_blank">📅 14:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139849">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/139849" target="_blank">📅 14:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139848">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/139848" target="_blank">📅 14:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139847">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/139847" target="_blank">📅 12:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139846">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
پرسپولیس-خیبر فعلاً طبق برنامه
🔺
باشگاه پرسپولیس تا این لحظه هیچ درخواستی برای لغو دیدار مقابل خیبر ارائه نکرده، با توجه به شرایط موجود، این دیدار طبق برنامه قرار است یکشنبه برگزار شود، مگر اینکه در ادامه تصمیم جدیدی در این خصوص اتخاذ شود  «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/139846" target="_blank">📅 12:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139845">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
یحیی گل‌محمدی: فکر نمی‌کردم لوکادیا روزی در جام جهانی مقابل آلمان بازی کند/ او یک بازیکن حرفه‌ای بود/ از روزی که در تمرینات حاضر شد مربیان از نوع تمرینات‌ش راضی بودند/انگیزه زیادی از خودش نشان داد/ لوکادیا یک مهاجم شش‌دانگ در محوطه جریمه بود
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/139845" target="_blank">📅 12:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139844">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔵
رسمی؛ رضا شکاری به پیکان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/139844" target="_blank">📅 12:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139843">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/139843" target="_blank">📅 11:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139842">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❤️
علی علیپور:
🇮🇷
🇮🇷
واقعاً افتخار بزرگیه که اسمم کنار علی آقا پروین، اسطوره بزرگ پرسپولیس قرار بگیره. خوشحالم که با کمک همه هم‌تیمی‌هام تو این سال‌ها تونستم تعداد گل‌هام رو به 96 برسونم  ﻿
🔴
ولی حتماً از قول من بنویسید که میراث، رکوردها و افتخارات علی آقا…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/139842" target="_blank">📅 11:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139841">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/139841" target="_blank">📅 11:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139840">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
عبدالله ویسی بعد از باخت مقابل پرسپولیس، از سرمربیگری ذوب‌آهن استعفا داد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/139840" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139839">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
سازمان لیگ به باشگاه اطلاع داده اگه میخواین میتونید طبق قانون بازی تون مقابل خیبر لغو کنید و بازی نکنید حالا قراره تارتار امروز تصمیم نهایشو بگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/139839" target="_blank">📅 09:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139838">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
باشگاه‌هایی که درخواست تعویق بازی‌هایشان را داشته باشند ممکن است دیدارهای آنها لغو شود.
🔴
پرسپولیس هم ۳ بازیکن در اختیار تیم امید قرار داده. در صورت معوق شدن بازی‌ها، فشردگی بازی‌های آینده‌شان بیشتر می‌شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/139838" target="_blank">📅 09:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139837">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
باشگاه‌هایی که درخواست تعویق بازی‌هایشان را داشته باشند ممکن است دیدارهای آنها لغو شود.
🔴
پرسپولیس هم ۳ بازیکن در اختیار تیم امید قرار داده. در صورت معوق شدن بازی‌ها، فشردگی بازی‌های آینده‌شان بیشتر می‌شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/139837" target="_blank">📅 09:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139836">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUGf4VgUHY9LotLfbguKU5rsRx9QrCiAJRY78mdCNRdq_NsWnPSOlqAfoj5H4cPbYz_FILN0DBALi-FmUcYRR1vwELCSF53LBmvZ2F4IZkbjDhyDBFNN4KkgTPjbl18cZoQoiKIm0ndEzTAzf_vDjgQfZiTNfPgrMI3MC_I_Ob3qicV99byqZ5jji4S0-_PNLu7bpL6wqyFpBtawfpsiQnWQTEsXBXeSiP8JV2YPKwXoNtkK7kAHy0lf2mSz_efDW88Ml7BFnC3oSTUOc_91ttCKiFSBzVQ7OvgsYpHwwUY9CFNuLmp9UflHQD_vdcJTUvWyW8rGqOtueMEzJtJa_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/139836" target="_blank">📅 09:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139835">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139835" target="_blank">📅 01:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139834">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
✔️
باشگاه‌هایی که درخواست تعویق بازی‌هایشان را داشته باشند ممکن است دیدارهای آنها لغو شود.
🔴
پرسپولیس هم ۳ بازیکن در اختیار تیم امید قرار داده. در صورت معوق شدن بازی‌ها، فشردگی بازی‌های آینده‌شان بیشتر می‌شود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139834" target="_blank">📅 00:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139833">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
احتمال لغو چند دیدار از هفته هفتم لیگ برتر
✔️
برخی باشگاه‌ها از جمله سپاهان سه بازیکن در اختیار تیم ملی امید قرار داده‌اند و به‌این‌ترتیب احتمال دارد برخی از مسابقات هفته هفتم در روزهای شنبه و یکشنبه لغو شود.
✔️
✔️
باشگاه‌هایی که درخواست تعویق بازی‌هایشان…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/139833" target="_blank">📅 00:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139832">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❤️
❤️
حدادی در بین هواداران، بعد از بازی با ذوب آهن.
✔️
هوادار:
❌
دمت گرم با این تیمی که بستی، تا آخرش همینجوری وایسا.نیم فصل دو تا ضعف رو برطرف کن، بخدا تا آخر فصل ازت حمایت میکنیم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139832" target="_blank">📅 00:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139831">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381bd5fd51.mp4?token=pT3NtF210rpqytrTkPbtpCTnezwhOMi82HEKCkbc1mJvjkwIVEXdwVSXJA_AOx0n7-Uob2O9mG8K6v1ZvALlT8p0JaBKv34SiTIr3ebKu_NiXOWh0z-rHzqd0rH7L3e4HF9s7rmfO7uEikMwDMhF7j8kjqeiPNISwEhaNnU-jO0airdpPHAaSKLypKh5fje2G973WuutZ7NgFt_bCtsAJ3ZUjU1IhBQ9yKd89Uksf8p2Zn-ctUjsjvELWVVCEMXN06v3y8i2d_zADCHkrIHgwBPDVRzyDyEtLrl37XJZIM4uj4-ganrt1bcPXvrH68_RBVUGrq7OAkGJW05kTrkzeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381bd5fd51.mp4?token=pT3NtF210rpqytrTkPbtpCTnezwhOMi82HEKCkbc1mJvjkwIVEXdwVSXJA_AOx0n7-Uob2O9mG8K6v1ZvALlT8p0JaBKv34SiTIr3ebKu_NiXOWh0z-rHzqd0rH7L3e4HF9s7rmfO7uEikMwDMhF7j8kjqeiPNISwEhaNnU-jO0airdpPHAaSKLypKh5fje2G973WuutZ7NgFt_bCtsAJ3ZUjU1IhBQ9yKd89Uksf8p2Zn-ctUjsjvELWVVCEMXN06v3y8i2d_zADCHkrIHgwBPDVRzyDyEtLrl37XJZIM4uj4-ganrt1bcPXvrH68_RBVUGrq7OAkGJW05kTrkzeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ ویدئویی منتشر کرده که تو پایانش بخشی از سخنرانیش تو زمان شروع حملات مشترک آمریکا و اسرائیل به ایران آورده شده: «خطاب به مردم بزرگ و سرافراز ایران، امشب می‌گویم که ساعت آزادی شما نزدیک است. وقتی کار ما تمام شد، حکومت خود را به دست بگیرید. این حکومت از آنِ شما خواهد بود.»
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139831" target="_blank">📅 00:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139830">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/139830" target="_blank">📅 00:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139829">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
پزشکیان پیگیر حل مشکل آزمون برای همراهی تیم ملی
🚨
مسعود پزشکیان، شخصا پی‌گیر رفع موانع بازگشت سردار آزمون به تیم‌ ملی شده و به احتمال فراوان مشکل آزمون برای همراهی تیم‌ملی در جام‌ملت‌های آسیا حل خواهد شد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139829" target="_blank">📅 00:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139828">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
نیویورک‌تایمز: آمریکا و اسرائیل احتمالا هفتهٔ آینده به ایران حمله می‌کنن و تو جنگ سوم تأسیسات هسته ای ایران به شدت هدف قرار میگیرن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139828" target="_blank">📅 23:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139827">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❤️
❤️
❤️
علی علیپور با گل امشب رکورد علی پروین را شکست و دومین گلزن برتر تاریخ پرسپولیس  شد
😀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139827" target="_blank">📅 22:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139826">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139826" target="_blank">📅 22:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139825">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری
❌
با اعلام کفاشیان، جام فصل قبل به کیسه‌کشا داده نمیشه و باید برگردون تو غار  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139825" target="_blank">📅 22:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139824">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
✔️
تسنیم: پرسپولیس بیش از حد به بیفوما وابسته شده؛ بدون او سرخ‌ها توانایی خلق موقعیت ندارند!
✔️
نظر شما چیه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139824" target="_blank">📅 22:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139823">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139823" target="_blank">📅 22:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139822">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139822" target="_blank">📅 21:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139821">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139821" target="_blank">📅 21:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139820">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⚡️
⚡️
ترامپ:
⚡️
از نحوه مذاکره آن‌ها راضی نیستم من هنوز درباره ایران تصمیمی نگرفته‌ام، آنها نمیتوانند سلاح هسته ای داشته باشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139820" target="_blank">📅 20:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139819">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBCNf8BgqFy_YpRrTcJo8wsHicG_my3mUbcWzlNZkUerFp3MqGR23jefwZzhxnBIpndrUD_938xRIuc9FGsuChl5DYMrbpH-nMo_DgJI_3wlfe1wUgjmSRQ7VQfYfXEvCxtlzVPCNd-GdQYFK7OLLk2vnGmEgFxONAfMMiexhM0dhpwjq2CbpLZ4uoINsNOi8k7wkpMUSA9I9PjiwT6HwfBuYfmlEW2C48_BU3y_SWhWPpsdA4b_4cRUGmIPp3X3oKk-chjFJ9jC7ub-y4kwhau7UPeIjOwgDbG88-RPMcFpOfe5fZbt0yNqJWKBa3i2-ewwkOTXr0JEVGtr91rhNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
پرسپولیس مدل دهه شصت
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139819" target="_blank">📅 20:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139817">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">😐
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139817" target="_blank">📅 20:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139816">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">😐
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139816" target="_blank">📅 20:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139814">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139814" target="_blank">📅 20:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139813">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meqXedyYotvSZHS6TUhylCPOLDzfA1wIpCHfC4aMFCz0SeMtfmTOSlgkGHtY1s0LZqWzybD99SeL0804W1CBXlNTupDALBNvAAWdRnT1oqZrMXpZGlwEeuLw9Cv8a30X-aKBsNd_PhTyaf9M4PgXnIZNeGZgvQwosaoImgMMdpHa5r35yRhNXDLXsf99J_bwLNY0QLyWvkIzYZ8kVaNJ4ibdIB-A7PFJXuS7oMDVG3Sd_Vgam06lvT68EzZd5YvhBFsNs9f9LH9g6oQiUx0rD2jUMd_bZVfHGq1lJvW2dBbcetIC6CkrmxvkmVFyH_BUHLz00pe6o3snNqNOLTTpZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139813" target="_blank">📅 19:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139812">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🗣
🗣
شهرآبادی، ایری و لطیفی‌فر به دلیل حضور در اردوی تیم ملی امید، بازی با خیبر را از دست دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139812" target="_blank">📅 17:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139811">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139811" target="_blank">📅 17:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139810">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139810" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139809">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139809" target="_blank">📅 17:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139808">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
عضو پنجم هیئت مدیره پرسپولیس مشخص شد.
✔️
به نظر می‌رسد روند انتخاب عضو پنجم هیئت مدیره باشگاه پرسپولیس به مراحل پایانی رسیده و حسین صابری خورگو به عنوان عضو جدید این هیئت معرفی خواهد شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139808" target="_blank">📅 16:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139807">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
فوری؛ سردار آزمون پس از یک دوره غیبت به تیم ملی بازگشت و اسمش در لیست اولیه جدید تیم ملی قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139807" target="_blank">📅 16:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139806">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139806" target="_blank">📅 16:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139805">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‼️
⚠️
🇮🇷
تصویری از ناخن‌ بلند کنعانی زادگان در صحنه درگیری با آقاسی که در برنامه فوتبال برتر نشان داده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139805" target="_blank">📅 14:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139804">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
برانکو ایوانکوویچ سرمربی سابق تیم پرسپولیس بعنوان‌مشاورفنی زلاتکو دالیچ به کادر فنی‌اش در تیم ملی امارات اضافه شد و قراردادش رو امضا کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139804" target="_blank">📅 14:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139803">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139803" target="_blank">📅 14:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139802">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139802" target="_blank">📅 14:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139801">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
رکورد تاریخی پرسپولیس
✔️
پرسپولیس با تفاضل گل +۹ بعد از ۶ هفته، بهترین شروع تاریخش رو ثبت کرده؛ آماری که فقط یک‌بار در لیگ سوم بازهم توسط پرسپولیس و یک‌بار هم توسط سپاهان در لیگ دوم تکرار شده بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139801" target="_blank">📅 14:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139800">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
✔️
آمار جذاب پرسپولیس تارتار
✔️
گل‌های زده پرسپولیس تا هفته ششم در ۹ فصل اخیر بی سابقه‌ست که نشون دهنده هجومی بودن پرسپولیس در این فصل هست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139800" target="_blank">📅 14:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139799">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdhXxXLwK27Z-96DjDdiWuFkQ-9OhEKXPW_A4U7lRVmnHdDV8RpD7tAbIZstxZHRdRXXpz-Mu5WKQycvsC3V9779jyX6azb6oFenterjPp65ALMazFTdngEjJBUCtrMieIJheQxKUE1_aEqZJ8zY3u-ai8pq8RXG-QByJW0kuWj7l5ovyO23r-gHAehLmr-5hRsRdpiTyN8l4HeTTmsF6nk8mmNwlyrSYlULDYNt7GTMBoPK7izczPZrYqQRtKmFkL1198aS4uAqGjp65D-3aEAOiZGxTeyQnveTk0-wkNzVarLK148e8raEjL8tObLPYS1mtU-JsRvBenycks_dZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139799" target="_blank">📅 14:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139798">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmgZsvSLCSkLYdN8nSyAz2i70wrNx8qDXkD9kNFQFnALhJhR9VpmdGtDkWTvT6Ht0mAptPD7mA6ysBB_hJyr_TeNc8LCyYkqTZ7IIkgVoBEz94YnXjy6-ZvVr3OA7jA0QXtnAYCF-ZS1Qn-UsU2Ap2j0kMvKK3xuQOYNoEBgh40i1H-NKK9QsYiXwQm9N7N0SyQpnWjQHkM7CxIua1NvNRSH_LfcQ6vpHmX8qoefXMzgbJZOP2YYaGqueLMsM9Dvl_gV8nHj3Yh1Rmk_hfmdBzgVoBb_d3mkfsgB5m1BxXgIyO-E8BwQUFYO4esUhXH5w2w0hF25gMD4vPu24xh2uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139798" target="_blank">📅 12:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139797">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOw0WH9F3fZJ83n-B7bsLTjvcVZ1s4dShXFY66ISUi3OhMSOghX4MeRyhZHIjaT1J3AvmdM_NZAh0079GIF6hBZqJyLuLzv7d_2GiFq6R5BSxg2N-CbRWAL042yvZcXtYwjwl4iBioSu8pWb45LKxUyxxjPEJ1eDLGrG_6xASnDGR52oixbkchrwud2eLODWr9pfYRO5DVANJ-CqxT2ImOdnr8cNrnJQwmMivXIJEsXYCObsMw8WllCh22xzPVo6Roid5NEB9NA7qAZy88HYgiFswZA8olzqFuUtbhHS1CjBIGXw7RT_jAT1nQgKDVSQ-eY5tL5VTOOlsSWQ9V-5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گفته می‌شود که باشگاه پرسپولیس تمایل دارد قرارداد علی علیپور و حسین کنعانی دو کاپیتان تیم را برای یک فصل دیگر تمدید کند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139797" target="_blank">📅 10:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139796">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✔️
🇮🇷
پوریا شهرآبادی جوان ضمانت کننده آینده خط حمله پرسپولیس؛ یک خرید بسیار هوشمندانه از گل‌گهر که با استایل مناسب و دوندگی بالا در همین ۶ هفته ابتدایی که به عنوان بازیکن تعویضی به زمین اومده، نمایش قابل توجهی رو‌ رقم زده. امیدواریم با مدیریت درست کادرفنی و…</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139796" target="_blank">📅 10:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139795">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❤️
❤️
تارتار از امیر حسین محمودی خیلی راضیه و احتمالا مقابل خیبر زمان بیشتری بازی کنه//ورزش سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/139795" target="_blank">📅 10:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139794">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✔️
دکتر حقیقت: ما کارمونو بلدیم نگران نباشید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139794" target="_blank">📅 09:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139793">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa6dd97ad3.mp4?token=Os7u6IlgQ_3SUp5OjsKuOCyz1hIAhflMTQj_2_NmU5hkHWf6zbcUPrlHXgKXMtUJgJp5Iv2uuFlSajqc9BffbF8dSNayw6Ynty-3c3CxdK2ddC8zPF0UwW_Jh0ciwJTw5xj8qyUf7PWuHcrn_vipZpo26B8p-8Zx14_0r3cKDoVeW7_VwN39YE6QEeM2-y_lAyF8y9HAYXApAG3zoj36K3SzJ_etsveFbgwL8Mb-eguK3u7XZparOAxqS3ltxBBDEmV3ybRjUaGfNfOcVDGePaGsPVSM5OOP97T1dqz-f07wS0_AgHPP2Ulu91N_tj-wftO8_VvP447TAZlmpt-HmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa6dd97ad3.mp4?token=Os7u6IlgQ_3SUp5OjsKuOCyz1hIAhflMTQj_2_NmU5hkHWf6zbcUPrlHXgKXMtUJgJp5Iv2uuFlSajqc9BffbF8dSNayw6Ynty-3c3CxdK2ddC8zPF0UwW_Jh0ciwJTw5xj8qyUf7PWuHcrn_vipZpo26B8p-8Zx14_0r3cKDoVeW7_VwN39YE6QEeM2-y_lAyF8y9HAYXApAG3zoj36K3SzJ_etsveFbgwL8Mb-eguK3u7XZparOAxqS3ltxBBDEmV3ybRjUaGfNfOcVDGePaGsPVSM5OOP97T1dqz-f07wS0_AgHPP2Ulu91N_tj-wftO8_VvP447TAZlmpt-HmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🔴
دو گل پارس جنوبی به پرسپولیس در دیدار تدارکاتی دیروز.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139793" target="_blank">📅 09:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139792">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
سلام صبح همتون به خیر و شادی ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139792" target="_blank">📅 09:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139791">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvnvEaxfGNRtNXuVvnxez1CPmqqp5Hg5dFBQ-hv1_Gjebvs835bTDgNBpsBDalN1V75LSFwxtoKcJ2f2_R-91sN-1zl-gSWqUHRhofKYZiSKwFP8XvAsO0SHVnLTIKX4wlvFEPy50AcI7VRZ-xi4FnCPZxBtKEEcTOXc5dWxd9C5ie0rj5fnltdOmrXKNMBWSDQtOldnbiaU5Oh4J6gIVqsS2P5k1qrEtn8Rmb9sU8JXCKN4OXhIHkFy4GqpN8Kupws4HLIq8rLKVtMnCcbAk2yiLcsX_TAnaUem88LF5lZLZ8m00GeJTam0rJDJTfSLd-D5GqoMb3It3C1TlOd81A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/139791" target="_blank">📅 01:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139790">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
✔️
زارع: جلوی خیبر نیستم ولی تلاش می‌کنم بازی بعدی باشم  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/139790" target="_blank">📅 00:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139789">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/139789" target="_blank">📅 00:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139788">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
پرسپولیس امروز در دیداری تدارکاتی به مصاف پارس جنوبی جم رفت و در پایان ۲-۱ شکست خورد.
✔️
سرخپوشان در این بازی با ترکیبی از بازیکنانی که در بازی شب گذشته مقابل ذوب‌آهن حضور نداشتند و بازیکنان تیم جوانان خود این بازی را آغاز کرد و در ادامه به دلیل…</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/139788" target="_blank">📅 00:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139787">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/139787" target="_blank">📅 23:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139786">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
✔️
شرط سنگین گرا برای جدایی از پرسپولیس
✔️
✔️
شنیده‌ها حاکی از آن است که تارتار نگاه مثبتی به استفاده از این بازیکن در ترکیب تیمش ندارد و همین مسئله بار دیگر بحث جدایی گرا از پرسپولیس را مطرح کرده است.
✔️
✔️
دراین‌بین گرا برای جدایی از پرسپولیس خواهان دریافت…</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/139786" target="_blank">📅 23:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139785">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
بازی رئال مادرید و اینتر هم شروع شده که رئال  دو گل زده تو سی دقیقه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139785" target="_blank">📅 23:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139784">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/139784" target="_blank">📅 22:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139783">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nv-1syZGc89iXxOdsg7eCsGBr6ylbl2smUEzHckuyIW6rluPtA9MM8PqglJqAWtc5LowULOd5BQL-gCsj8Y2MWoRLpJrXl2wiBwKaAKjclk1cZj0ykvPZ6QIiFuacxzQP48ZNs_onSlviQ4wjcXB0ef0QAM01lIuVYY1OT_jAc8SdDL1s1VgX9MTSiTZeu2_QqvhquG401we63N6Ih01i0o85gVWy0_TCsz74QdZ7uwj7XwJs5y6XJ2tGdqT9YW1y2UeLRqaFykP5DnmyKd6zC8zWM07O1cKRxGh9Ghqv_KNbGx7rKsg9C98ZEFEGDTCyYhTHQIb7H6KlLN74XjzlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/139783" target="_blank">📅 22:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139782">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OreznM8cf_eZl5str4uRgAbiklyuNorhxd8rXr_ozfAU08JR9c8zIou9y9R8LpNjbobDfQYypkCQAghxozuR3A4IvFIklczCGB2CqyPUIpT_00rJqdzagPjyjpoY0QwqKTx8lLfhe090tsUCfLbCjfukayZM7TCQnyJtRvarSkETnBYWZ6W4-jx2nglV7LgXfWyTBBGwig1Z58Ff_Zf_2EqHFjCnJd_G35IYy71s047pMCFjnT_dK0Wxrrmq5PlGqUklW7oEVzYcyBkyChtYXmsDyw8Id258FtYVc1DDJViXma8C0-lzx7pnyVcVCQLh5b4tFnZvHyHJNcxhc85MZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
تیم ملی امید راهی ناگویا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139782" target="_blank">📅 22:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139781">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✔️
✔️
دکتر حقیقت: پارگی نسبت بزرگ بود اما سعی میکنیم به بازی خیبر برسد حالش هم عالی بود تقریبا بیست دقیقه پیش مرخص شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139780" target="_blank">📅 22:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139779">
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
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139779" target="_blank">📅 21:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139778">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5ITsFKIyA_ldWFgjmoXPxqLmyTnBYdHdYbyFXs66N3aJNwK3AcCGgziTJMfL1dpHGu_KqdVQJfIBf_xj_dVq1rCsxQUyK9DlZ5OD7UIPOwv3hqkOamW0L65erSDb4EWKYxiOTGNK643BMxDz2vKWzwM31G95okwelZ-BayX9exTAUi0sL2yxqFyI36BJLbrqPwvS0ySgjRolcx7GvOEOy6VPcP9-xz2B9JcCmZCAehots-mPpU_bKgwhGbvhXpXSe9OOfhzEAg7TWCuw_yrHiqxexXiSSrGidC0tZ5nbFB84cLstsKOZr9CCE3nU5Ln6qJFjLKuRTwHYNo1aBDojg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139778" target="_blank">📅 21:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139777">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
فوری| زارع مصدوم شد!
⏺
محمدمهدی زارع بعد از تمرین و هنگام دوش گرفتن، پایش به‌شدت برید و ۸ بخیه خورد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139777" target="_blank">📅 21:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139776">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNX4_lDFXDmNqVmf8hXiTG61X1zX7NpVNdO5xt4BFQIC4GBmq2qe9MQdS1i2Mfvgnqj7vVSKRj7ra64FK3UROX6Qpz0Kk1rNRoI-_CyhRAya-85jf-xGHTkzKHmwTjZYBI12-IVzjMUSkmGltekrieiPsIY6VNPGVM6y4yqogcrW301DEoCnb0vQ1XN9MH4yF5wKPjpuvufIoeyuY2YRTaqEOjujPfiFUDy66BncvhgwFmQIIiYYQwoaXuzsjVgVVLiGEJkPsFNAuZu8orzpK-Elcd4PA_Ou8S0cp6xmdmh4AQ3Hvn-RPcwyWlWvjjk1nXAPdEBZ8K3ozm_nyDV0Mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uPWHB7xkx-3XJm0ZQWSXW4xbplwQtnhdEKQZION1Lq92lUJEUBciu3uvuk5lcY0W61lwXHQ-1wVLU33mWYK2woJCFPD5jIJZecPGOUY-hGQRV4UQjM4ZrbkbdAhAIdutRB6LXgm_TnQYHOIdqZPJYnCcUUeNB5zv13_OnEpPN2f7uMUufvwQRUmyKbIVMwnVVjpsTLpqq3xxerLrQJ8ZCLcIvfP52Y_Vamuo9dkU_Hc2DFTdxHRf_qMpwxi5egRPLr06NczLAMRM1vavSz1ZAEVvcyqkbgnkUMFpPQI2vDkZ7IGP_ApKNtyT8cIJztd0TRmt5NFejuQgvIqpmsn8vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
پوریا شهرآبادی جوان ضمانت کننده آینده خط حمله پرسپولیس؛ یک خرید بسیار هوشمندانه از گل‌گهر که با استایل مناسب و دوندگی بالا در همین ۶ هفته ابتدایی که به عنوان بازیکن تعویضی به زمین اومده، نمایش قابل توجهی رو‌ رقم زده. امیدواریم با مدیریت درست کادرفنی و فرصت‌دادن دوباره به پوریا، شاهد درخشش دوباره این بازیکن باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139774" target="_blank">📅 20:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139773">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYlrYBJATrSMV5WdCzY65tsN-ulAt-hHnW20BzxLE3M0feFleS-92B8XEHx53wqPDB1rvwsuoGJXQ8PfgBJ_C5f9220BPTwHXlhd8vz7OwIbRoFy2eZ6B6hP2kZT5-BZIP44bMz6yho80LU1_HYZksIF4UvlBgowzpJL_xfAMyoXdFaZuG22ahR3YYaqvM33NAwMB6PxDPh7gMXcEo4NXe_5Koa8QKeEopbdBuoZ0UwSF3lTRr-51KukggbjsV4yn24GkXPH6mwb3_Q_6pHxr1ZZ1RRVYo0IOwPkPvbwOlw4iLceNNxIQIfQOPX_xJAmN1b3JK2K5Q0ZuHWCpY8bkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش تصویری بازی دوستانه پرسپولیس - پارس جنوبی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139773" target="_blank">📅 20:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139772">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
با توجه به مصدومیت محمدمهدی زارع و غیبت احتمالی او در بازی بعدی، ممکن است پرسپولیس با حضور دانیال ایری در تیم ملی امید مخالفت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139772" target="_blank">📅 20:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139771">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh9Pwod-lnN1YxprQJ98F7pdjPx8xGs6zvbyLITVRxGRdPStoNNUdNmlAbBKTRpEjpfqtrpgy5aV5T2c8Vh4D3X4Lu3M2WBHF8zxBpTS2hNjfZFdE5gxlRQqao8D9ACSH_fkBz0W5bQxW4Ej7aLeXHGi1s_Odd9PR1T8nN6D9iDClWU-vQ1Vjdf_HvpbHRuV9LK8cyi9zpOhNUxtM9fW-URDjPcs2wrTYrq_DapqErRdzQfZsc0j5ZNvrp5mgVaFRCJ5Of0ZtotQC3jp0VPh9cQSf5LjLP3KGXblP84z6G6_ULG6xmZfzpPvAUirKDt_w6RmK7F_SBVfYj85q5PyZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139771" target="_blank">📅 20:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139770">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
فوری| زارع مصدوم شد!
⏺
محمدمهدی زارع بعد از تمرین و هنگام دوش گرفتن، پایش به‌شدت برید و ۸ بخیه خورد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139770" target="_blank">📅 20:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139769">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
پرسپولیس امروز در دیداری تدارکاتی به مصاف پارس جنوبی جم رفت و در پایان ۲-۱ شکست خورد.
✔️
سرخپوشان در این بازی با ترکیبی از بازیکنانی که در بازی شب گذشته مقابل ذوب‌آهن حضور نداشتند و بازیکنان تیم جوانان خود این بازی را آغاز کرد و در ادامه به دلیل…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139769" target="_blank">📅 19:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139768">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
امید عالیشاه: بر اساس چه مدرکی من رو محروم کردید؟ من فحشی ندادم و چیزی نگفتم! اصلا در رختکن تیم ما بسته بود از کجا تشخیص دادید من بودم که منو محروم کنید؟  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139768" target="_blank">📅 19:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139767">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🤥
🤥
دنیل گرا مدافع‌مجارستانی پرسپولیس به مدیریت این تیم اعلام کرده با دریافت 400 هزار دلار حاضره قراردادش رو با سرخ‌ها فسخ کنه. به احتمال فراوان بزودی گرا فسخ خواهد کرد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139767" target="_blank">📅 18:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139766">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139766" target="_blank">📅 18:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139765">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
پرسپولیس امروز در بازی تدارکاتی به مصاف تیم  پارس جنوبی جم می‌رود تا به بازیکن هایی که دیشب کمتر بازی کردند یا اصلا بهشون فرصت نرسیده، بازی بدهد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139765" target="_blank">📅 18:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139764">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7MgN9NWCJijmawUCBzKxwkSfi8xRRsi-_czYSgUFU-ILudiLAEhFphiFHOF25rUN9TSl62yAbCAj9BEtVKf8r0Kt_gbwKUiZ4Jje15p-qVU8bY4M_RfBoIIwcfaHeqUVGOQ7zI_oMQ4yqXWy8wVUxZDwr2y-mQ8hyzD1G1MbDZgX2-SPFZ5NnWKNcrDVXhr5CZx8kqDE_JG813D42t4w9r2uWpigyl0NZUkKGFRRxaabNXtJyMIfXY2qJcVrjgMRSMiPieeoyBC6CRjdgDWylfXI8uiNHjTOMDZ3uxOrQZ3suEiuajMFgSRydLxggcpb05idT6YdZuTp8IFp3xLFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYhYwIqhpBKIqVhUxPZZm4YQzfRtnKWzcP2K-MafXT9YtSoiFvWx5eqBSFa2flaXju2KQQef6MOKRzUoxS4RbHkV9Rsm5JAmdq_etJa7dBxbDfoLmUi5VqL9Ko7cKZcwLh56oY4dlipMUEtOmJbIinbH56A7dwNto5-DIjHAqjBlyYmyG2uk8wra3mk0BKFtAQS-Yo8NVILg5WmeZgVRqaigCnl8S4w5_u9Cb1-zFp4FFec-WXfayY6BVUt5NVXpu5BDoMABYx8T1zNvTX3ZXyhHuvVe2q39p0jfSN8m2k7Z336U1Sck-F4MFY7udrwsEfRVA_ujVpJfhqmJH_tVWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asxsBgs13BUkWeGlaPReL8MWHMrxP--QZsNavnXwNAZJFLg_b1dX2vXxLy_VTuCUxtSGwtcDJQFapabjCl2rSDNFwCAD0tdm2Ss7UsMVSJy6YKGJWtznMKSZoKWkIKwN8iDghhVGfYRD31oVZjR43RjjSLLAOCN7m62aJcb1TbCJ-2v074LkQiOXRVcb-RhYH4hCWB2ePDHXU5Nc72BcblsWFk-O7j0GB0nF2ahYjMrRYQTQFz38DmYBUfVDscf0FFMsC0GpnZchd1frVge2EkirMuN_gGEwQ2I7aKguMCCzLOTWXPsED0aB6JjXtqHdoL8Sr6Wy-eo7fO0ZeqjcWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🔴
میرور: فوتبال سرژ اوریه به پایین ترین سطح کریرش رسیده و می‌خواد در لیگ دسته هفتم فرانسه در تیم محلاتی مونتینی-آن-گوئله بازی کنه و انتقال اوریه به دلیل تاخیر در ارائه مدارک از سوی فدراسیون فوتبال ایران به تعویق افتاده است!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/139761" target="_blank">📅 14:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139760">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🎙️
فرشید اسماعیلی:
✅
کابل VAR را کشیدند چون عجله داشتند که زودتر بروند؛ در گوشی به داور گفتند که پنالتی شده اما داور گفت من سوت پایان را زدم!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/139760" target="_blank">📅 14:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139759">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❤️
❤️
بیفوما که به تیم ملی کنگو دعوت شده بود دعوتو رد کرده و گفته تیم ملی من پرسپولیسه و به تیم ملی نمی‌رم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/139758" target="_blank">📅 13:21 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
