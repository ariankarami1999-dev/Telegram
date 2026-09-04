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
<img src="https://cdn4.telesco.pe/file/NGPOw7oOB-as50MFkT7tVO6WZGBTTsDQXgBPoZ2ncE0U_UT6fuvCWXyKRtU1HTi8EGChWQ_QANVujpica8m4uAR1hHRPZrh0pfha3oPg35GawhVIxwhr42ak8tIx3ocWZYNtZvn8EbFIKvFaC3H_NaTZk20gQcPM8eVhy2-lfHpo4RTkuNOUEANZYs6TArdPoR_u_RPq0zQyYJHLzNRqWH9Ba3s9fEpHXs4GaJWF_YXf2BmxzWPzaJzA735DqxbmLLWKulJPUXoCUMf_TSs71iq7y2o5x1PQCEjz9KfMApZBuCqMr52T8ee4L4DBLkPLFSniuetuhG1s7yzPr_mwKw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 20:46:44</div>
<hr>

<div class="tg-post" id="msg-139547">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👀
❓
محمودی ۱۵ دقیقه هم بازی نکرده امسال… اقا تو پستش ترافیکه درست ولی نمیتونی هر بازی بهش ۲۰ دقیقه بازی بدی بازیکن روحیش از دست نره ؟! محمودی چند ساله دیگه عصای دست پرسپولیس میشه اگر آقایون نسوزونن بازیکن رو…فقط بازیکن هایی که از گل گهر آورده رو بازی میده اقا…</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SorkhTimes/139547" target="_blank">📅 20:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139546">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
با اعلام باشگاه پرسپولیس، آکو باتری اسپانسر جدید این تیم خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SorkhTimes/139546" target="_blank">📅 19:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139544">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XenmXEaFVDy2wqWFZtVNlZ8wkwGsAzc0vkTH-JNcfV341fJZpv4-UkDJ3YdXro11ZvTSyjrR8TUPpAMpQ5F2eeoGx2vn8CxLwIGZp6ow5sMSknpq3H9IrMKEY10TgHNKXaSniBXOotQMVGMzuWgmxF5V0gZPSnZKUJoY-yRYgY970kmhFqOm3uWXi9-FJRJElBVPRpSt6R_7rXyf5j3SIUyFkz6nAHkIXY8mFJ03f0xZzURbf7wjAuWGtNubRyMxhzxGECUa-AssRJYiCrxvK98-Lr-1jBl8NkSYqXD1QlSWLOk_TlzmMkzShoKb3XMzOaRJj0vj4enzVcXglH_TXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
🆔
| ورزش‌سه:
🔴
❤️
با ادامه‌ی روند فعلی مارکو باکیچ از پرسپولیس جدا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/139544" target="_blank">📅 18:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139543">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❤️
❤️
باز هم بزرگی و عظمت پرسپولیس در این سال‌ها به بهترین شکل خودش را نشان داد
🔻
🔻
در سال‌های اخیر، بازیکنان زیادی با آرزوی رسیدن به پیراهن تیم ملی، راهی پرسپولیس شدند و پس از درخشش در این تیم به هدف خود رسیدند؛ گولسیانی و گندوز نمونه‌هایی از این اتفاق هستند…</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/139543" target="_blank">📅 18:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139542">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: ما پیگیر شکایت از یاسر آسانی هستیم و برای اینکه پرونده را به دادگاه CAS ببریم ابتدا باید در کمیته انضباطی شکایت کنیم و جواب بگیریم بعد به CAS ببریم
✔️
بعضی ها می گفتند ما اورونوف را بازی نمی دهیم که او را  بفروشیم/ واقعا خنده دار است چرا باید…</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/139542" target="_blank">📅 18:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139541">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
✔️
جنجال و حاشیه در اردوی کیسه؛ با اعلام سهراب بختیاری‌زاده، صالح‌حردانی بدلیل رفتار ناپسند و درگیری با سرمربی و یاسر‌آسانی در بازی دربی، تا اطلاع ثانوی از حضور در تمرینات کیسه منع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/139541" target="_blank">📅 18:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139540">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⚪️
⚪️
⚪️
فوتبالی: سهراب بختیاری‌زاده به حردانی، مهار اورونوف و بیفوما رو سپرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/139540" target="_blank">📅 17:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139539">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
نصیرزاده: شکایت از آسانی، دنبال نخود سیاه رفتن است!
✔️
تیم‌ها با شکایت از آسانی دنبال نخود سیاه هستند؛ فقط استقلال می‌تواند از این بازیکن شکایت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/139539" target="_blank">📅 17:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139538">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b00df71c.mp4?token=Dp4KKed9Y-lOSzxFv3Bnt7c1jzpMy1H9dc9rdz9YsRfL3S2NA4xNy8tL3W1t_oCuXffvOA8iEXE2aWNIlQvTPeV3EFIVPsKzOLt3lNyyxpuRixpZXIsOiH4nNAMl9P5e6ARvKJ1n1ssRUTy8Kzh5zt5xVIleb1_KUwXnixytGLGQpGkc1M8MjjB3dfece5m-7DMnBemlMXUBKMCF01fdllfj-WQ5-X0s5APYgpX1LUWJoNAr5Olbe9VzsfUO2RpLJ0u3ycrjr5C1b6ULPv_2WopYN96lyvV25GLcik-n0_0hPp02Uax1iPWJZBnZvbZgzkNLiB6PW_skBB28wkzGng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b00df71c.mp4?token=Dp4KKed9Y-lOSzxFv3Bnt7c1jzpMy1H9dc9rdz9YsRfL3S2NA4xNy8tL3W1t_oCuXffvOA8iEXE2aWNIlQvTPeV3EFIVPsKzOLt3lNyyxpuRixpZXIsOiH4nNAMl9P5e6ARvKJ1n1ssRUTy8Kzh5zt5xVIleb1_KUwXnixytGLGQpGkc1M8MjjB3dfece5m-7DMnBemlMXUBKMCF01fdllfj-WQ5-X0s5APYgpX1LUWJoNAr5Olbe9VzsfUO2RpLJ0u3ycrjr5C1b6ULPv_2WopYN96lyvV25GLcik-n0_0hPp02Uax1iPWJZBnZvbZgzkNLiB6PW_skBB28wkzGng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
نصیرزاده: شکایت از آسانی، دنبال نخود سیاه رفتن است!
✔️
تیم‌ها با شکایت از آسانی دنبال نخود سیاه هستند؛ فقط استقلال می‌تواند از این بازیکن شکایت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/139538" target="_blank">📅 15:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139537">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✔️
✔️
رضا جباری:
✔️
این نسل پرسپولیس از لحاظ اخلاقی و فنی بهترین‌های حال حاضر فوتبال ایرانند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139537" target="_blank">📅 14:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139536">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
کیسه و ترتر شش امتیازی شدن و کلین شیت و حفظ کردن امیدوارم فردا بازی و ببریم و پیام هم کلین شیت شو حفظ کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/139536" target="_blank">📅 13:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139535">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🎥
🔹
تمامی گل‌های هفته پنجم لیگ برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/139535" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139534">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87b97822e9.mp4?token=GFqwu1OPhBpL6TFgudV4boYqYq_YBYcw1Kac8mzHZlE4zytB-5t9C4PesWM_dWVk3OCKuqdkyx2soEZbm2Et7sR9SqDXqvyiEhLBffk1cTXK18mtbvHLr2AwfmSxb_zhyz80Z5lnf8DgZ9S8oYN0fxSHDSEFCwNrDpJNiXTclE7RcTxWUNjcGsSYuVdr7Nv-3JRDIEioNz-tbNtsYbiGUEbWv7yy3V_eHgeFa9VxU_uoGThX33fw1sw6_hn7PQvB6GjUWdJYrcVD1vQqRvOpInfc4eCi9g3L-T4wE_XY927no5q1Sm7iB8J86sV_GyrTXlppQeLknguFT42lNDa9MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87b97822e9.mp4?token=GFqwu1OPhBpL6TFgudV4boYqYq_YBYcw1Kac8mzHZlE4zytB-5t9C4PesWM_dWVk3OCKuqdkyx2soEZbm2Et7sR9SqDXqvyiEhLBffk1cTXK18mtbvHLr2AwfmSxb_zhyz80Z5lnf8DgZ9S8oYN0fxSHDSEFCwNrDpJNiXTclE7RcTxWUNjcGsSYuVdr7Nv-3JRDIEioNz-tbNtsYbiGUEbWv7yy3V_eHgeFa9VxU_uoGThX33fw1sw6_hn7PQvB6GjUWdJYrcVD1vQqRvOpInfc4eCi9g3L-T4wE_XY927no5q1Sm7iB8J86sV_GyrTXlppQeLknguFT42lNDa9MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▫️
گل محمدمهدی محبی از زاویه‌ای متفاوت
▫️
▫️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/139534" target="_blank">📅 13:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139533">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
فنونی زاده : به حدادی گفتم حواست به خلیلی باشه میخواد مدیرعامل بشه و زیر پای تو رو خالی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/139533" target="_blank">📅 12:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139532">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚫
عادل فردوسی پور: با دیدن فوتبال ایران میتونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/139532" target="_blank">📅 12:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139531">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00fbdf9821.mp4?token=Syr6CvwrwVjdKpUC8W8h-gUk5Kz3yvQE0_-RfxA_YjyOXTd0EeBE_e7-rU75hYGOjOe5TBl43nZByvglBWrZDOuVNrs1rYs-DAGUbzXNpCVmFqqOoYiNyy7_P-pP50TVewYWD2wUJNtKeGvFx1Nt3xnhLZeKqQPfX4-aPrhvHnce-cBiFGxGaSr8tBLjSJrWS0taMpYv3sqHhr5NhDn22ch19b8gpGek5Cjern8sigMgOZ9PaYFtDIQyYRlFWpYN0oEk6HexJ_190UbtAvsdDlPNqIebCZKXpbkx9QePkaw2cParqPfRb_VVMDvRXqxF5Uwc5lVn-kGwWmUYR2GRCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00fbdf9821.mp4?token=Syr6CvwrwVjdKpUC8W8h-gUk5Kz3yvQE0_-RfxA_YjyOXTd0EeBE_e7-rU75hYGOjOe5TBl43nZByvglBWrZDOuVNrs1rYs-DAGUbzXNpCVmFqqOoYiNyy7_P-pP50TVewYWD2wUJNtKeGvFx1Nt3xnhLZeKqQPfX4-aPrhvHnce-cBiFGxGaSr8tBLjSJrWS0taMpYv3sqHhr5NhDn22ch19b8gpGek5Cjern8sigMgOZ9PaYFtDIQyYRlFWpYN0oEk6HexJ_190UbtAvsdDlPNqIebCZKXpbkx9QePkaw2cParqPfRb_VVMDvRXqxF5Uwc5lVn-kGwWmUYR2GRCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
اتفاق عجیب؛ نیمه دوم بازی شمس آذر و تراکتور ۱۶ دقیقه وقت تلف شده داشت اما داور دو دقیقه اعلام کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/139531" target="_blank">📅 12:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139530">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
🔴
پرسپولیس موفق شد امتیاز تیم دسته اولی فولاد نوین رو بخره و تبدیل به پرسپولیس ب خواهد کرد و سید جلال حسینی هدایت این تیمدرا برعهده خواهد گرفت/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/139530" target="_blank">📅 12:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139529">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
✔️
شنیده میشه که همکاری یحیی گل محمدی با باشگاه دهوک عراق به زودی به پایان خواهد رسید و این مربی به زودی به لیگ ایران باز خواهد گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/139529" target="_blank">📅 12:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139528">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
فرصت به ستاره خاموش سرخپوشان نیز خواهد رسید؟!
✔️
✔️
مهدی تارتار قصد دارد بصورت چرخشی از بازیکنان جوان خود در ترکیب تیمش استفاده کند و در هفته‌های اخیر شاهد بازی کردن بازیکنانی همچو سلمانی و لطیفی‌فر در پست خط هافبک سرخپوشان بودیم.
✔️
✔️
حالا بنظر میرسد…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/139528" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139527">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
پافوس قبرس با هدایت ریکاردو ساپینتو از پلی‌آف لیگ اروپا حذف شد و راهی پلی‌آف لیگ کنفرانس اروپا شد. تیم ویتبسک بلاروس هم که میلاد محمدی را در اختیار دارد، از لیگ کنفرانس حذف شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/139527" target="_blank">📅 12:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139526">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: هوادارا فقط میگن چرا اورونوف بازی نمیکنه؟ خب وقتی بیفوما در آماده ترین ورژن ممکن هست چرا اوستون بازی کنه؟ بیفوما خیلی خوب بازی کرده و حق دارد فیکس باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139526" target="_blank">📅 11:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139525">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی مدیر پرسپولیس: بیفوما الان شرایط خیلی خوبی دارد و دارد خوب بازی می کند ولی دارند حواشی درست می کنند که چرا ارونوف بازی نمی کند. هواداران ما  باید صبور باشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/139525" target="_blank">📅 10:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139524">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcMmcjlZ9nlAH61syqS7j3BH8MEsF3s-ctJYFW5uxGHiAeYuhQtH8MVm7UWwfH534kdwX7eVVesYyiyFVgUkADY6SDMj4Ru5t3YMM7kPMjNeOtGj1X0Guskm7XZ4r7Hs5nqP9kLzerfZ_54vHvIfP11SBAeZm_60oWNcTNRtKCpnSxmKK6H09QzGKAOePnT8rHHsD23xk-aYK2VsheRiZcw-dp4l5rILeyvhu1azwiSMlYZ492Uwz9yhXQsxn8E6FZ2TRu1ZXvHJD7ll8q7FCL5yYZ1WoEZlgsgZprnLNPOtjbjGCAeglQY1TGe02tPbX78ma4Llvy_JB4Rcv16KyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌬
پایان دیدار
🇮🇷
ایران
3⃣
_
0⃣
نیوزیلند
🇳🇿
👀
✔️
ایران گام اول را محکم برداشت، شروع مقتدرانه شاگردان پیاتزا در مسابقات قهرمانی آسیا
🇮🇷
۲۵ | ۲۵ | ۲۵
🇳🇿
۱۵ |  ۱۲  | ۲۲
🏐
#قهرمانی_مردان_آسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/139524" target="_blank">📅 10:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139523">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❤️
محمدمهدی محبی زننده ۲۰۰ مین گل تاریخ دربی بود
👌
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/139523" target="_blank">📅 10:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139522">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❤️
صبح آدینه تون بخیر و شادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/139522" target="_blank">📅 10:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139521">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA-JZSwXdU07yRqPJd6d-GMHIeZBN-sXZsYmRdjd-4oHOuDO4T0L5otDZrNjMmrYhGdANu1E0P33NowbEkJVfROIB0-MOujf-gv0RUU9xhO3-V7gYOkrdQ2t1YnWUCGHYZwbPgjgN45QJ5fhWb73YLHpQNtd2vPGRzwJYjQSJdB_oDzslRA8ufwd3SG1MNLrycog1FNZaR80F50CiMgFL_XnjHEnk7AR_m9rtjyVFylwW-ydAzHyLI4hpVNqwhJCRPSc4FLfFHTnZR_5cYe253FtRsugqxGWGWjH-kJWiC7ojcQXgd9l7-T8Qd0SzrFXu-q5_y5Hs_yQ1QE_kCXhRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
دوئل ستاره‌ها و مدعیان در نیویورک
جوانی، تجربه و انگیزه در یک شب هیجان‌انگیز
زورف و تین به‌دنبال عبور از سد فرانسوی‌ها
🎾
گائل مونفیس
🆚
لرنر تین
🎾
الکساندر زورف
🆚
کوئنتین هالیس
🟡
کدوم ستاره‌ها از این نبردهای هیجان‌انگیز موفق بیرون میان؟
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
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139521" target="_blank">📅 02:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139520">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRBUg9tUdSyNa9aQUjYNaCWY8mGwnVw7x0c6Ool6LO-jVq40Hpfd6IeoZ3BdS3173hzo8A7DwDC929ARNiOsuRcwk-kumHAvSRjXAZnCBZilBW2ABX6_ZCiyEqAaSReFCBs3iB_393LFrw4RWL16OREDJ3rXzB-QoBZgBryk1MQOJGQYWk9GbSvPHh3QSlNn-CrqjDMMZ3xOkQJyBOicvY3Uhj1tFBZsnD89_Orl5HU4D7eO74Ym7y4y9DKydjTg2asqq56CEMEsJ4C_3_SIxfKrjHysYwteK7iFnU0Ob0FG4jUPC0qs64PJE6zX5hV7IC1AEBGuuQaSBFhI9Ya1VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🇮🇷
تصویری از ناخن‌ بلند کنعانی زادگان در صحنه درگیری با آقاسی که در برنامه فوتبال برتر نشان داده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139520" target="_blank">📅 01:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139519">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
فوری ترامپ: آماده حمله دیگری به ایران هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139519" target="_blank">📅 01:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139518">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7cfe803aa.mp4?token=s1iisiLwykARniPIxmovUhk0CF-VxL-p_7X-u6khI3EOczmMMxp9HJZijkukBX5u2NfBNhSJB5CyrpLUxe4Fwfvv7dw80hniQBFRx-81f2zPG4DfJGYje5_6O7OBhpF7NOpMrTQrzeMVds2bclDb0AFyjKrRKocRU_G-VmLSXmdGLF7Z3PNJmrjGvMO8p81gZx1ZDBXfoKmIbPAgvCjbYfI4D4r-qXQbYN52Q85qOFEbAr6xc-H-isTSeq8ZgaSccp3FtRaevpM93U8diGVnhFtuZmma3f6jGX_mfk5YML5VmDxUYCVYZOSU1h1G1awzwI6bu03aMvD-XUSDmbwLNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7cfe803aa.mp4?token=s1iisiLwykARniPIxmovUhk0CF-VxL-p_7X-u6khI3EOczmMMxp9HJZijkukBX5u2NfBNhSJB5CyrpLUxe4Fwfvv7dw80hniQBFRx-81f2zPG4DfJGYje5_6O7OBhpF7NOpMrTQrzeMVds2bclDb0AFyjKrRKocRU_G-VmLSXmdGLF7Z3PNJmrjGvMO8p81gZx1ZDBXfoKmIbPAgvCjbYfI4D4r-qXQbYN52Q85qOFEbAr6xc-H-isTSeq8ZgaSccp3FtRaevpM93U8diGVnhFtuZmma3f6jGX_mfk5YML5VmDxUYCVYZOSU1h1G1awzwI6bu03aMvD-XUSDmbwLNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
تصویری از ناخن‌ بلند کنعانی زادگان در صحنه درگیری با آقاسی که در برنامه فوتبال برتر نشان داده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139518" target="_blank">📅 01:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139517">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: شما تعویض های تارتار در دربی را ببنید که تماما هجومی و در خط حمله انجام شد
❤️
محسن خلیلی: اینجا پرسپولیس است شما نمی توانید ناگهانی 80 درصد تیم را جوان کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139517" target="_blank">📅 00:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139516">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: شما تعویض های تارتار در دربی را ببنید که تماما هجومی و در خط حمله انجام شد
❤️
محسن خلیلی: اینجا پرسپولیس است شما نمی توانید ناگهانی 80 درصد تیم را جوان کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139516" target="_blank">📅 00:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139515">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⚽
🎙
رضا جباری:پوریا شهرآبادی جزو 3 مهاجم برتر لیگ است؛بازی در پرسپولیس پرمهره از بازی در تیم ملی سخت‌تر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139515" target="_blank">📅 00:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139514">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
خلیلی: بهترین نقل و انتقالات چند سال اخیر را امسال داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139514" target="_blank">📅 00:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139513">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✔️
✔️
دعوت بیفوما به تیم ملی کنگو بعد از درخشش در پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139513" target="_blank">📅 00:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139512">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
✔️
باشگاه استقلال:
✔️
سرعت بیفوما خیلی عجیب غریب بود و مشکوک به دوپینگه! ازش شکایت میکنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/139512" target="_blank">📅 00:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139511">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2lALEhpkxcGtAX1KKvRJuL4UiWU84TqKjbw-s0VsjxRVlGS5n0EAzpDpn49WWBZAwABX_rbKZZ8hFCXgRGzdO__fA5AT-U-1-5bOpDePpCZAR-udZ9ssyqcTMChSIwkeSWJGnYGmYRwzXJuSqMYqTZJI9PC0lVr_tibFBbdi2U-Vpf_lngKQg46ZUYFg7p1B8HD8xLIQAyjwZnySbhiH88HHQ5i3PIZghcEk3VO6ZDxIYVyjPqJPMubezXzfEMVbLyBo8KM2S1RP3II8VVK4-PVV72LVe6FGE91EY6cnmHeICp73JcLaJeKsUCkhCpDBITVlTtNOjMuL9McUyidQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🟠
جدول لیگ برتر در پایان هفته پنجم
👑
تراکتور با فاصله ۲ امتیازی همچنان صدرنشین است
👀
فاصله منطقه سقوط تا رده پنجم؛ تنها ۳ امتیاز!
❌
چادرملو و استقلال خوزستان؛ تنها تیم‌های بدون برد
🔼
تراکتور، استقلال، آلومینیوم و فجر؛ ۴ تیم بدون شکست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/139511" target="_blank">📅 00:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139510">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: برای دربی 5 بازیکن جدید در پرسپولیس بازی کردند اما استقلال تیم پارسالش در دربی به میدان رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/139510" target="_blank">📅 00:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139509">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: من شاهد هستم که تارتار واقعا دارد در پرسپولیس زحمت می کشد اما یک سری هجمه ها روی این مربی وجود دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/139509" target="_blank">📅 00:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139508">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👤
محسن خلیلی:
✔️
با کفش‌های بیژن طاهری هتریک کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/139508" target="_blank">📅 00:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139507">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
جباری: سبک بازی ارونوف و نوع بازی تیم با توجه به تغییرات در حال هماهنگی است و به مرور زمان بیشتری برای بازی پیدا می‌کند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/139507" target="_blank">📅 00:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139506">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e2475d08.mp4?token=u5gvjr2DicRPl4qO2RmA6eYk2e128SBXw8K7po5TpDtTlYt4k5QJhy96qdSwF6_rd__8FXuw1PsjUfydbwyRacHechZlf65mgYRaBNkF4W9bK8k6IO-hkTcJQgCL5LZg1s5hTvF7VruUrwD1c4xrgk_0RBOsx5p-WIj6Sm6sEjCPVQYDoGZQB2Kk1O7N9gBu4AYn13Sjw0AxSBTVdZj40kBAwPcxe09MiYnsShIiP_aFmJzVbttXhlHMAyXO0YRYwDykLqn_Fr4T8c2Wn9-3xgCJIulmyOEA3osDkk8Y6SHqBKycnN0r2-ui-pXAdpb866rK_kYD8lHi1jdSpXfPrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e2475d08.mp4?token=u5gvjr2DicRPl4qO2RmA6eYk2e128SBXw8K7po5TpDtTlYt4k5QJhy96qdSwF6_rd__8FXuw1PsjUfydbwyRacHechZlf65mgYRaBNkF4W9bK8k6IO-hkTcJQgCL5LZg1s5hTvF7VruUrwD1c4xrgk_0RBOsx5p-WIj6Sm6sEjCPVQYDoGZQB2Kk1O7N9gBu4AYn13Sjw0AxSBTVdZj40kBAwPcxe09MiYnsShIiP_aFmJzVbttXhlHMAyXO0YRYwDykLqn_Fr4T8c2Wn9-3xgCJIulmyOEA3osDkk8Y6SHqBKycnN0r2-ui-pXAdpb866rK_kYD8lHi1jdSpXfPrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
محسن خلیلی:
✔️
با کفش‌های بیژن طاهری هتریک کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/139506" target="_blank">📅 00:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139505">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇷
🇮🇷
نظر محسن خلیلی و بیژن طاهری درباره برگزاری دربی در اصفهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/139505" target="_blank">📅 00:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139504">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a595378b0.mp4?token=lh__Zbdf43Eg5i9D1bnXMFKhkk58beqoZ6BaZxPWcRhbDnEt_DeOp-XtizKHxFq1QwAwNsXTt71I4w-tBzZuJ6mSVN27-osI5f-P1KlzXrVkPR0WWdsuiwN9Lic0ybt33EHT-HzJI4WRSIQzweKUD5jweKHZfeDEk-kCleSFPNXXwC4lbvHAhXBEUZRex4etoibq51oyzo5Qb8DsM_eTiozjWoR3G8id-HwjkUh5EChZsrccdO2gacQtdspf_8q-NxdqvJjEoMmXAurHoiq7d5txtaJDMp4FLzh9tg7ntAhGb24TArU0N7H87_hOnDtB6QLqSufeWVmcfYHK_S-UKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a595378b0.mp4?token=lh__Zbdf43Eg5i9D1bnXMFKhkk58beqoZ6BaZxPWcRhbDnEt_DeOp-XtizKHxFq1QwAwNsXTt71I4w-tBzZuJ6mSVN27-osI5f-P1KlzXrVkPR0WWdsuiwN9Lic0ybt33EHT-HzJI4WRSIQzweKUD5jweKHZfeDEk-kCleSFPNXXwC4lbvHAhXBEUZRex4etoibq51oyzo5Qb8DsM_eTiozjWoR3G8id-HwjkUh5EChZsrccdO2gacQtdspf_8q-NxdqvJjEoMmXAurHoiq7d5txtaJDMp4FLzh9tg7ntAhGb24TArU0N7H87_hOnDtB6QLqSufeWVmcfYHK_S-UKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
محسن خلیلی مدیر پرسپولیس: ۸۰۰ میلیارد بودجه لازم تا ورزشگاه آزادی تا چند ماه آینده آماه شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/139504" target="_blank">📅 00:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139503">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⚽
🎙
رضا جباری:پوریا شهرآبادی جزو 3 مهاجم برتر لیگ است؛بازی در پرسپولیس پرمهره از بازی در تیم ملی سخت‌تر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/139503" target="_blank">📅 00:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139502">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⚽
🎙
رضا جباری: کنعانی و علیپور با رهبری‌ خود نقش کلیدی در ایجاد همدلی و ساختار کلیدی تیم دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/139502" target="_blank">📅 23:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139501">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
جباری، مربی پرسپولیس:  یکی از جذاب‌ترین داربی‌هایی بود که در این سال‌ها دیدیم. تیم پرسپولیس همیشه بالاتر از همه‌ی نام‌ها است. دنبال ۳ امتیاز بازی بودیم که به آن نرسیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139501" target="_blank">📅 22:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139500">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GW3Ao9_avuoBQd2kNxzhJKiHGerVDJdNmCoYCaESie1rbnjy5gr3rg6R83aBtAPKJuJQJHdJ7vkQDr_L6e8xG5ReJL4VV5sQkUXsn3qVn6FH1cep7KjY5FiWd3ChUV9ecrVCY8knxTxWG01U0ztCf-WXdJDVFafU7ZitVXdMXY4OEUpWSmcrdlu1thuIzKN1MyqShoouVdKPv-DrrRkEZ4FAHYr9sWaZefdT0zGIL-pj4bRLZmohfSUMPmImHxEm3ylJEt1Y8jQRu4OdEfYRMSTWFeQ0dcFqN5kBUg1BmpUVDemwcBLQCNvgLFzpBQ_d4kAVT906JSjnTLa1fpV8sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
تست های پزشکی تیم بانوان
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139500" target="_blank">📅 22:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139499">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4KkZkwFRuzkNqfAXUizSaYWWiK1SvbPlnbB0_6_qde_lh1IY_YXeHTuy1XaBRSDI_fcyp15MriVTnWJRtCVFqiY3VSgwSsHQqRMYjVAUOBzeeg_bxNiLjuPHIZ0XzLvTBMxuXki1QDWvNYbLayWdFwh6Ihrd71mS2P9e81klQ1NIF5vQXn77bswKKfrZRHEelhZXomQVsqrKik4Xw-svEjkTFRCbaaJ8ypoWp6xxedkdocriJuPeRhnFnXR5n74bIf7xUxexayGbIjnpp-KU0DEYk93sNbPt8XvrrIpak6I0sHB2fNKkoLdX2Qa0vmDnY5UEr4hXRqmcEpoeW1lNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کمپانی دیشب یازدهمین بازی بدون شکستش مقابل استقلال رو انجام داد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139499" target="_blank">📅 22:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139498">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_HAAOTLzuUmFw5K7u5abi_YCniFPvKbBy0Ze_jRy1K_UlU00V8ktsv70ukhx_-TV91fhjbNt9O3zstY2aE1Cxy0MisQDMcRcaSqES27tr4NP3X_DrWnq3QJt670-sfsUb667NX3QDphXapn5tSrODxJhfA3q4Me6f-0pV1tlyGBxb_jl3_m55QdxumeK5YnqZA7Rbqvnhm0gJBBhujgKx_vxSwxYiPHwM-qbwHjZVtfv6-7cNRL0TLKJmQClP7yvKQ_EBgBjTP8sw_-MkHoIbb_D3OCnzOTa9lwkBlH-iONpd6UaXtEdJDeLni56MHayBtvpKnedGGyXHKEdxiD8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139498" target="_blank">📅 22:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139497">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✔️
✔️
تارتار ضعف پرسپولیس را پیدا کرد!
✔️
تارتار به این نتیجه رسیده که پرسپولیس نیاز به یک رهبر در خط هافبک داره و نیم فصل قطعا در این پست تقویت خواهیم شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139497" target="_blank">📅 20:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139496">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPO5DzkABoPU8mYVPION_axw14sUa1JXygSFaPSoCbzFC6fbtsQgufDJpTGymXQSjc1zWmHbDze8xhU3LkyNjykockflJXbgGGogt1r-Cmy_fT0Wwq4V24ZYspBheoHTdgF3l1V_Bl0LTTXGvQAtZGb97Voa6JQweoFhFEsKEpNnrgiVg3EcbHGBp0Cg3MjXBVNe0198e0i4ygbLlkk8DX1R1Fn4hmmLDDJ-rCkToasFYZZUKmk6AEuP8eVyOD8ELsDAQV8zyQnSQQGzBlN-rmrCR902yK6mY9LHZzvuI76cOzv8PZM1tYCdAnGF6TkoC8XeAql1inFyJrU_LTi1EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🎙
خلیلی سرپرست پرسپولیس:
❌
مصدومیت گرا از ناحیه آشیل است. تارتار گفت اول باید او را ببینم و در مورد ماندن و رفتن وی نظر بدهم. هیچ اختلافی بین اورونوف و کادر فنی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139496" target="_blank">📅 20:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139494">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTTTM9EkAKcj5bG47GaGiGK2iF2ZXJf4srAZTvri84em5S3PrNZ0bcoT6P-oM4v-x8x8kwdDLc76IXPVnAhhqXuEEmluhdb6Qty_1QzjAHfIRSjjWvXCAMirPLXVIuY7VwtldwhoatgIeORFkaPl3_GIiLp0hg9fJVpN2Q_KOrIuwIk1I7pwoReFL6_hXqhg6bdtdU2AAKgOIWRYTakSt0S6641UCS65XBRsjTZKlhkDjNGJqQglkNH0tFv_JtW1aeee43iCwoFyiOfNG0-jSZvWrGYgS7TqP6EFwk6FSsz_YE5serZLharLrmhpErJqETsJdeSMdw8rza15y4w4fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد سرویس و قدرت در نیویورک
فریتز به‌دنبال عبور از سد بلوچی
شانس بیشتر با ستاره آمریکایی!
[
تیلور فریتز
🎾
🆚
🇮🇹
متئو بلوچی
]
🟡
تنیس یواس اوپن
⏰
امشب ساعت ۲۰:۳۰
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
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139494" target="_blank">📅 20:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139493">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHYRtWmxtU_P4IEYJvu0C1phbGZZIZEp755tNyhPeoA-LgSFq3n3T0Yl5yiszkuOU0WtQUVSaXBGyRzWnabSfru-11AQXFFOiI-2tm98tjcwZIKoTPCY1VAFQhoVTQ_WHplWBwf-2lu15GCaVajvhRjyqf7EpvpaGSBokQ96-2NSxQ_4Y7q8bY82HP-bOwCzJnniToWxgMgSNp0fep6WdeVaG-fi94XsTupjxgqmRFQKw4lhmbd4N71IFCMzt3zHH6XythhM_3c86GQiuQ1uXc8aNy_nO6qPluUFUuwmN0qtp8kv81ohnrWptzh7FmmYe_n8YrBybiMlsyuzme2rGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
حضور ابوالفضل جلالی در بازی امروز
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139493" target="_blank">📅 19:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139492">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmGUAOtxn985gsdFj7mITGiXNpK7IUQyocDi-y2xfxUAIUBfWTbph4KtU2RDKAbJ5FotyKI_YONeVT2zRArK3SFXOef3nU0GRJoE8OIS9ZJGIbZWV_09DjwwM2yLDooxXNVhyYMTzsxGOWWlt-mK63nnqdsqVxe3kO5_mJH8k_xYrupouAmUFOik8Iq5e3yxirMnOafrt-gAQK4yM9E20SEMdXIqZ2wqTU0g81QiRE-pZmbXRqyLAgO7lnKqGVWu0GMziNkPJyT1-5QwT8gp5SLNRtVfeE93q24nUKCTlL58iYtQUbpmaQaPbzpdKve85TMxUI6vonqZbD9flEPHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
محمدمهدی محبی زننده ۲۰۰ مین گل تاریخ دربی بود
👌
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139492" target="_blank">📅 19:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139491">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">#بماند_به_یادگار
🔗
💯
تا روزی که اردوبادی و اینانلو داخل هئیت مدیره هستن این تیم رنگ آرامش نخواهد دید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139491" target="_blank">📅 19:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139490">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRtlNFb_g3n7hYBQjdVna19f35_swo50oD8Cyad-Z6y4MEKML2DjgYFHCZvm5l9vg2wPzNyiI11oTYRUBo-K7xJ8qr4zvV80rgaO-hP-VUF9EeXJrh6IzKhftJ1SZEwcF4Vj-9dZV8Fcimy5wgTevptqdy8NZ-P4Z1-L5aAcBK0tYUaBGbREnE6ld3HE7naZqs6Fx2Gra0Fxe72wUYih9JnZnFASzm-O6TQxwH_xNTo2rszjcCcjDMmf4KTORThcMt7MdDNp_DHnTMV7tXdP9enunQOmUSR027ZcGDb-vGhO3McqyBreJ1JWf95FuZ2qkwZzzM5uC7FRYzpt3MTo3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
پرسپولیس امروز در دیداری تدارکاتی به مصاف مس رفسنجان رفت و با تک گل پوریا لطیفی‌فر به پیروزی رسید.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139490" target="_blank">📅 19:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139489">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAc94DeSu07bdZGtx0kTS1ISfcbgMA2aV01FKbGHWrcSGW8ssHBoemk-JVnX5rYo96enNvvHrezD_-Mq_MOLr4yD3iec8R2uvr2GqqIvpue3xF3GpZZRFk_tJMYU4cTVk9ZAxr_JEec_m9xyoZIzDZRODSE81y7Q2TpW7qM-XuRsKGp1MEBafulk_A3qxJBjqeZAf8cdJv1fz0SJQ8Z-kagSPc_LHqfSxcVUW5lhX0rcIGquY65BwP5fdEMeSbCM3QssSj7SudmQ5v3J4j9nPRrjSO0I_p6eUviYRwZ1Q4SsPhhy13oERlNo393hqK25eN3EwFRYDtBfYVxODhxCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
محمد عمری از فصل قبل تا الان توی ۱۷ تا بازی برای پرسپولیس فقط ۲ تا گل زده!
⬅
⬅
با اینکه آمار همه‌چیز نیست و کارایی بازیکن روی بازیِ تیم هم مهمه، اما هوادارها اصلاً ازش راضی نیستن و انتظارات رو برآورده نکرده. امیدوارم بازی دیشب براش درس عبرت شده باشه، تصمیم‌های درست‌تری بگیره و بیشتر به درد تیم بخوره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139489" target="_blank">📅 18:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139488">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🏅
باشگاه استقلال قصد دارد به دلیل حرکت حسین کنعانی‌زادگان در دربی ۱۰۷ مقابل عارف آقاسی علیه این بازیکن شکایتی را به کمیته انضباطی فدراسیون فوتبال ببرد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139488" target="_blank">📅 18:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139487">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1znxyGPEumtlPHw88Vh9cvKVDHPaOsu9JVfbDZa0jJ6c8lV7qOQIJ_VM-2GjIag4_wLaxNEj6bR8aPeQ8wrAg3hYErjpIaI-B8DZ_i-lTLW0O2gfFCRSAWIcAvWF6-cj9U09FPrHksnqjI2RVWzT6KQCVN5lxkgIUO-iwnUhlvYETWt1h08zWYpwH2X_bHe6dwrHcfI3bnjV2cfCZC5iiBx85WC8jMXt_eK8BYIM-LfrseUogmtlUfvoPdnOqG-lhwUt1gH4YAhujHjjIfiFNPcknNAi-yyrSlj_cJsRzugglAPXHLZAifzyjCWlIHKx474sjLplnResYPHh6IsVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
باشگاه استقلال قصد دارد به دلیل حرکت حسین کنعانی‌زادگان در دربی ۱۰۷ مقابل عارف آقاسی علیه این بازیکن شکایتی را به کمیته انضباطی فدراسیون فوتبال ببرد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139487" target="_blank">📅 17:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139486">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✔️
✔️
دانیال گرا مدافع مجارستانی تیم پرسپولیس برای هفته پنجم از لیست بازی خط خورد تا یک سهمیه خارجی سرخپوشان برای فصل آینده به خطر بیوفته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139486" target="_blank">📅 16:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139485">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✔️
✔️
خبرگزاری مهر:
🔴
پرسپولیس پیشاپیش شکایت خودشو برای حضور یاسر آسانی تو دربی آماده کرده. پرسپولیس اعتقاد داره کمیته انضباطی و سازمان لیگ صلاحیت لازم رو برای پرونده درباره یاسر آسانی رو ندارن و استعلام فیفا باید منتشر بشه
🔴
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139485" target="_blank">📅 16:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139484">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
❌
❌
طولانی‌ترین روند شکست‌ناپذیری در تاریخ دربی؛ پرسپولیس با 20 دربی بدون باخت
✔️
✔️
کیسه کش حسرت برد دربی رو به گور می‌بری
😂
🫵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139484" target="_blank">📅 15:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139483">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=ZcLcOOF86_2AeTBGjVJR3VwD4CBGN0kkSurAAvAPOU0JFqq55dmNfaQIHScwcs9NHuMvieahy3jtujyAY-NMFbipn8O874ttWWmTvfFWjr26lHZMIoHXlDJtJHhTWkXtYSssiis_giHYFLpJ1S6e9hJXRXjz6jAPmf7GCMlqgAozaXnRVa8oy5YZn1eSTPQlBUY_b5sQJUv2I40V-rn5cr-N0At6q3Rlw9xlDXMtHbnzW_jJWIQVdkTrVl7IO2b5CmEHsaiLW4B25CBtwZR7ItjP9Pf470FuFf12RhuaLN4a6mvBAnuOB-ws4McvOuSdX_DLFICRngbwfYh940wKyUR_nKWT0VLkdJ1PJl2tdMRpSHf9NUqVAQ2pzUyMKDhC-P-fzQwN-41HRusgAEBrQCwvH-vcnojy9xnxsXYDzSKUUaaJw2Vrd01KIBlnAY2ivgwExWAasMPO8yAaJxy0tK7r5ZdNr0EJEF79ScAn4Q4TUX-BJfP3JyDCblabMAqeyRx1IpUJSDIrzl0dmwnKdhn5jLXk7xPWLOVmCxDPycD45G_mUaMl4CE5m9Pem1a0EveItUEj-MkAfCZg1iqYxqdVvAxZ1ncMQIZvEVAqKdK3PqYj6kVsQVS2pdNfDSlFb4cLZJnClRmEwTcs2EQvobOujDAu1vHa5ufk5gAktHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=ZcLcOOF86_2AeTBGjVJR3VwD4CBGN0kkSurAAvAPOU0JFqq55dmNfaQIHScwcs9NHuMvieahy3jtujyAY-NMFbipn8O874ttWWmTvfFWjr26lHZMIoHXlDJtJHhTWkXtYSssiis_giHYFLpJ1S6e9hJXRXjz6jAPmf7GCMlqgAozaXnRVa8oy5YZn1eSTPQlBUY_b5sQJUv2I40V-rn5cr-N0At6q3Rlw9xlDXMtHbnzW_jJWIQVdkTrVl7IO2b5CmEHsaiLW4B25CBtwZR7ItjP9Pf470FuFf12RhuaLN4a6mvBAnuOB-ws4McvOuSdX_DLFICRngbwfYh940wKyUR_nKWT0VLkdJ1PJl2tdMRpSHf9NUqVAQ2pzUyMKDhC-P-fzQwN-41HRusgAEBrQCwvH-vcnojy9xnxsXYDzSKUUaaJw2Vrd01KIBlnAY2ivgwExWAasMPO8yAaJxy0tK7r5ZdNr0EJEF79ScAn4Q4TUX-BJfP3JyDCblabMAqeyRx1IpUJSDIrzl0dmwnKdhn5jLXk7xPWLOVmCxDPycD45G_mUaMl4CE5m9Pem1a0EveItUEj-MkAfCZg1iqYxqdVvAxZ1ncMQIZvEVAqKdK3PqYj6kVsQVS2pdNfDSlFb4cLZJnClRmEwTcs2EQvobOujDAu1vHa5ufk5gAktHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
❤️
👀
✔️
تو این صحنه کسی متوجه نشد ولی وقتی از دوربین نزدیک تر صحنه پخش شد مشخص شد نوک انگشتای نیازمند بود که باعث شده توپ به تیرک بخوره وگرنه گلو خورده بودیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139483" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139482">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
20 بازی بدون شکست
🔥
✔️
حسرت کیسه در آستانه ده سالگی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139482" target="_blank">📅 15:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139481">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❤️
خدا بنده لو، بازیکن پرسپولیس:
⚪️
بیش از اندازه در مورد ارونوف حرف زده می شود. چیز خاصی اصلا وجود ندارد و هنوز خیلی از بازی ها باقی مانده است. او اصلا افت نکرده است و اصلا زیاد بازی نکرده که بخواهد افت کند. همه از کیفیت اورنوف خبر دارند و هر تصمیمی سرمربی…</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139481" target="_blank">📅 13:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139480">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139480" target="_blank">📅 13:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139479">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
✔️
باشگاه استقلال نسبت به عملکرد و سرعت بالای تیوی بیفوما مشکوک شده و احتمال می‌رود درخواست تست دوپینگ از این بازیکن پرسپولیس را مطرح کند.//هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139479" target="_blank">📅 13:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139478">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaDWpYaSIpEEMrHmWHK3J3Zkzc-PlmRStVYBq-mSZg_B8Ghy4Y8J_QdlpUvmyZlkL7msXQh2uc9qqkilur-B6pQUFnFHJvUCeG3Tv-cuimZDbsj8gmf9wxGA7JZYYDB-25QEkIw0r15zLVMhiZRZWPossWvQzTQJpo37bhYzti05-XsdikG0GVevDeEg2_mjsLZ0Sy_vtD3JABJn6zb46R12zDlfWrvFbfRszeAKEqB2s6f9nbWMNl3TgruHg9Hb6WU0G-q2pbJcuURDFTI7Vf3eA-HGwZTNhIqUx7Hg_sCK6pgretIvbiFsFVDNAA8RLzuVhHQE11CceZwB7yMtlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سوسیداد و سلتا؛ جدالی برای سه امتیاز
دو تیم آماده برای یک نبرد نزدیک و تماشایی
کدام‌یک دست بالاتر را خواهد داشت؟
[
رئال‌سوسیداد
🔵
🆚
🔴
سلتاویگو
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
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139478" target="_blank">📅 13:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139477">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔄
🔄
🔄
با حضور یاسین سلمانی در بازی دیشب حالا مهدی تارتار به تمام بازیکنان پرسپولیس بجز محمدحسین صادقی که تا حالا در لیست قرار نگرفته بازی داده و تمامی بازیکنان با ذهنیت آماده به سراغ ادامه‌ی لیگ میرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139477" target="_blank">📅 13:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139476">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🤩
| فارس:
🔴
❤️
🔄
تارتار امید چندانی به دنیل گرا ندارد و حتی درصورت بهبود مصدومیت هم نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139476" target="_blank">📅 10:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139475">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
باشگاه استقلال نسبت به عملکرد و سرعت بالای تیوی بیفوما مشکوک شده و احتمال می‌رود درخواست تست دوپینگ از این بازیکن پرسپولیس را مطرح کند.//هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/139475" target="_blank">📅 09:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139474">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
♨️
🗞
| #فوووری از تسنیم:
🔴
🔵
👤
پرسپولیس بخاطر استفاده از آسانی مستقیم به فیفا شکایت می‌خواد بکنه نه کمیته انضباطی
⚠️
❌
کمیته انضباطی فدراسیون شکایت های گذشته در مورد آسانی رو رد کرده بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/139474" target="_blank">📅 09:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139473">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
✔️
عادل فردوسی‌پور: ترابی قطعاً ادامه فصل رو از دست میده، با خودش صحبت کردم و گفت دو پزشک بهش گفتن رباطش پاره شده و باید عمل کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/139473" target="_blank">📅 09:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139472">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✖️
✖️
هافبک و کلا استقلال برداشته و خیلی خالی هست هافبک ما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/139472" target="_blank">📅 09:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139471">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❤️
❤️
❤️
❤️
🔴
صبحی که دربی و مساوی کردیم و هنوز داریم حسرت تک به تک نزدن علیپور میکشیم بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139471" target="_blank">📅 08:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139470">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfxqopTtKDs8pCj7DFpqL5CUAykjnFLQhw7cOvd0Kvh5sOkn8-KnShy7qOoiIgjWQaEyriyajQqBcpRsrAuD0dxXYpm48Mzhv5YczItcmkLNfWQCfbsEy5uqKmkthmHPv2ZA5FJD19nZARkSMlzMazuEQrMe6KlzPt27wwHeXuzNWViq4SYjSYTXbZtSszJnVROXLk-TwmMvf760pdldXV-We7nryOVcDjTjvgu2lXsiAyupo72iKLBs3dynOzQGhjoZ6bbszRSuSp88ib-x7e39_XlHgMqgZSMZN-ee1BmqtW0e1VOk_vWoZ0PJxXeRnm80x08VuhC9wjhH47wYMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
دوئل‌های جذاب در یو‌اس اوپن!
🎾
جیمی فاریا
🆚
کارلوس آلکاراز
🎾
رِی ساکاموتو
🆚
فرانسیس تیافو
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
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/139470" target="_blank">📅 01:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139469">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
✅
سه بازی مهم هفته بعدی
✔️
شنبه :گل گهر و تراکتور
✔️
یکشنبه : آلمینیوم اراک و کیسه در اراک
✔️
دوشنبه : پرسپولیس و ذوب آهن شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139469" target="_blank">📅 01:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139468">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⚽️
⚽️
استقلال و پرسپولیس امشب در مجموع 33 شوت بهم زدن که 9 تاش در چارچوب بود، برای درک بزرگی این عدد باید بهتون بگم که در مجموع دو دربی قبلی 33 شوت زده بودن که 10 تاش تو چارچوب بوده که یعنی امشب به تنهایی اندازه دوتا دربی قبلی روهم موقعیت دیدیم
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/139468" target="_blank">📅 00:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139467">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQDYdUW18eMNFJfPwzJfi4vh2G3yMzcnw-CA_7s9LQsksExg1l68Q2UM8uMY9KWg-sDBF0AFSLetVcdT8YtBt1RINvJQj9PihDjC8sK6E3PdX4wVrd2xuP4eozJj-QTXi1apd-SJrHRT_FeTKzois3kHvS_jQD92ai0IsmhyKyjvKs5nBPrT4eXpdbz2ZmmfsSI5cZhXGzXjUsMyLJoEa84eq7TUUP4I4_FpWI3NerIgs9jzXtwU2IeBnmcQNd_dimqMvdQy5xHn8utXV5buTZQzu783JtIt7NSa3niCFIFqwPEXP57hjGAqG_2lLKqFSllQT9BQZuDUHQTMy8WOBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
استقلال و پرسپولیس امشب در مجموع 33 شوت بهم زدن که 9 تاش در چارچوب بود، برای درک بزرگی این عدد باید بهتون بگم که در مجموع دو دربی قبلی 33 شوت زده بودن که 10 تاش تو چارچوب بوده که یعنی امشب به تنهایی اندازه دوتا دربی قبلی روهم موقعیت دیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/139467" target="_blank">📅 00:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139466">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
20 بازی بدون شکست
🔥
✔️
حسرت کیسه در آستانه ده سالگی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139466" target="_blank">📅 00:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139464">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
فارس : نظر می‌رسد نظر کادرفنی پرسپولیس نسبت به ۲  بازیکن دانیل گرا و تیوی بیفوما  تغییر کرده و احتمال ماندن آنها در جمع سرخپوشان بسیار زیاد است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/139464" target="_blank">📅 23:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139463">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kxk_tQeTy2suwhuXY9FtUIaw9jjhjGeuhdSduYoasXf_wogkIbMViZA9_q6W28cHWky4DR4meSoFzWzuZQbPH1zrQ4BmM-M7zcUrHTaew3nDxqV0cblQFq3s5DjdI4VH8iN3nRwU5g3vh0M0FfFvbrw_lvQ3VFUFZnxXAEkWPpZ6HdmrFHlHj5LmN9PwSrtMvObpHqa_yUU739ucgmIIsmjAoklnU62Y4DffWxJ_QNy6fPhroDXP38T7ACEnvfPgAlWZvauxzfl5QlUPQeQF89AwW9-yrCr3rID-8xUEZESOxd7jQXrzdUDkuHXrymWzuoDk04HGnRyuasr29fx16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
پایان بازی | شکست ناپذیری پرسپولیس به ۹ سال رسید/دربی جذاب برنده‌نداشت  استقلال
1️⃣
-
1️⃣
پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/139463" target="_blank">📅 23:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139462">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc62967a0.mp4?token=Wgb_UF4DjPKUQczglD_zX9E3eetoL9dz_VjyFXQV7bYsTKFNG_u01QmfMz1nEwS5cjDAix7Ud9zD8smuBmlji7BSRlY3sk6vKCYuRZIScAo10_feF8eUWG2RbVfVK89GkXFBZm3H7M1UCfeKN76GG6zMB6ROTT-ImrqEx7dXSi9DoALxkGBxKIk-GsOms7Z8yriCsEDhK2Z7LGOydvsEReYrpLeSOFqqV9fIRbXOLkRCtGtNNER55QaMsTFevQl22vJYEU8mCVELEd0jLOg-Nj2QU1P3MKwhUtweSnUSTKFE8DdVfGn87cXbWVCvJXve5gShMJawVOSZPTArY7ts5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc62967a0.mp4?token=Wgb_UF4DjPKUQczglD_zX9E3eetoL9dz_VjyFXQV7bYsTKFNG_u01QmfMz1nEwS5cjDAix7Ud9zD8smuBmlji7BSRlY3sk6vKCYuRZIScAo10_feF8eUWG2RbVfVK89GkXFBZm3H7M1UCfeKN76GG6zMB6ROTT-ImrqEx7dXSi9DoALxkGBxKIk-GsOms7Z8yriCsEDhK2Z7LGOydvsEReYrpLeSOFqqV9fIRbXOLkRCtGtNNER55QaMsTFevQl22vJYEU8mCVELEd0jLOg-Nj2QU1P3MKwhUtweSnUSTKFE8DdVfGn87cXbWVCvJXve5gShMJawVOSZPTArY7ts5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
بیفوما امشب دوباره یه استارت ۴٠ متری زد فرعباسی وحشت کرد دستپاچه توپو زد بیرون‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/139462" target="_blank">📅 23:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139461">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
جدول لیگ بعد از هفته پنجم .اختلاف با صدر سه امتیاز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/139461" target="_blank">📅 23:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139460">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❤️
خدا بنده لو، بازیکن پرسپولیس:
⚪️
بیش از اندازه در مورد ارونوف حرف زده می شود. چیز خاصی اصلا وجود ندارد و هنوز خیلی از بازی ها باقی مانده است. او اصلا افت نکرده است و اصلا زیاد بازی نکرده که بخواهد افت کند. همه از کیفیت اورنوف خبر دارند و هر تصمیمی سرمربی…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/139460" target="_blank">📅 23:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139459">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
کنعانی زادگان: تارتار تیم خیلی خوبی بسته است و امیدوارم آخر فصل قهرمان شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139459" target="_blank">📅 23:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139458">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
کنعانی زادگان: تارتار تیم خیلی خوبی بسته است و امیدوارم آخر فصل قهرمان شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/139458" target="_blank">📅 23:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139457">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❤️
❤️
❤️
ترکیب پرسپولیس برابر استقلال
🇮🇷
پیام نیازمند، مهدی زارع، حسین کنعانی، مهدی تیکدری، مجید عیدی، پویا پورعلی، محمد خدابنده‌لو، محمدمهدی محبی، تیوی بیفوما، ایگور سرگیف و علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/139457" target="_blank">📅 22:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139456">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
✔️
هر دو گلر بد خوردن گلارو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/139456" target="_blank">📅 22:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139455">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: ما و استقلال خانه نداریم!
✔️
پرسپولیس و استقلال متضرر می‌شوند و ما خانه نداریم در شهرقدس از پتانسیل هواداری نمی‌توانیم استفاده کنیم.امیدوارم هر چه سریع‌تر استادیوم آزادی آماده شود.
✔️
اورونوف هم یکی از آن‌هاست هر کسی از هم‌پستی‌اش جلو بزند،…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139455" target="_blank">📅 22:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139454">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
تارتار در نشست خبری: گروه داوری امروز خیلی خوب عمل کرد، خسته نباشید به آنها می گویم/ امروز هم پرسپولیس خوب بازی کرد و هم استقلال
✔️
✔️
به خاطر گل مساوی که خوردیم واقعا حسرت خوردیم
✔️
✔️
هم ما می توانستیم برنده بازی باشیم هم استقلال اما در مجموع ما یک مقدار…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139454" target="_blank">📅 22:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139453">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👤
خدابنده لو، بازیکن پرسپولیس:
✔️
بازی بیرون خانه برای ما حساب شد‌. امیدوارم ورزشگاه آزادی زودتر درست شود. در مورد خودم نمی توانم اظهار نظر کنم. الان فضا بازتر است و امیدوارم ادامه دار باشد. دو تیم موقعیت های خوبی داشتند و آمده بودیم برای بردن اما حیف شد.‌شرایط…</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139453" target="_blank">📅 22:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139452">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bebc6bdd.mp4?token=OoODzU72EJoi0sM71_qvVkVFJWzoZfnRr5XZIheXhJkmSwdi81gNR4rGXfpU59v7HIi7vYrXuQdKnV6DJf9NgGQ-vFwABA_PT56jG7SXEmAEhskausbbtebRUwn0QDmU6cuhRWehsTkAeGnfh__pVPSN85u_macUqQeuxHjTEt6zVghIw__xgCmlTBjV2IpF6WY8l7Q6J52mOB1F9UTdF2i11Bubfq4ib3YQ65LxTdZVDmnVK7N6vD9mTAazBwoV2Jv1WmogcOLGtnYd-h5T-HmvpPeqPdEwIN980VipBcJUj6kHMB4wM3GPlbuOXrU7H-d8o0GJ1ZTNF6UyQwTWNoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bebc6bdd.mp4?token=OoODzU72EJoi0sM71_qvVkVFJWzoZfnRr5XZIheXhJkmSwdi81gNR4rGXfpU59v7HIi7vYrXuQdKnV6DJf9NgGQ-vFwABA_PT56jG7SXEmAEhskausbbtebRUwn0QDmU6cuhRWehsTkAeGnfh__pVPSN85u_macUqQeuxHjTEt6zVghIw__xgCmlTBjV2IpF6WY8l7Q6J52mOB1F9UTdF2i11Bubfq4ib3YQ65LxTdZVDmnVK7N6vD9mTAazBwoV2Jv1WmogcOLGtnYd-h5T-HmvpPeqPdEwIN980VipBcJUj6kHMB4wM3GPlbuOXrU7H-d8o0GJ1ZTNF6UyQwTWNoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
خدابنده لو، بازیکن پرسپولیس:
✔️
بازی بیرون خانه برای ما حساب شد‌. امیدوارم ورزشگاه آزادی زودتر درست شود. در مورد خودم نمی توانم اظهار نظر کنم. الان فضا بازتر است و امیدوارم ادامه دار باشد. دو تیم موقعیت های خوبی داشتند و آمده بودیم برای بردن اما حیف شد.‌شرایط تیم خوب است و همه متحد هستیم. هواداران صبورتر باشند ما تغییرات زیاد داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139452" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139451">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
✔️
مهدی تارتار : بازی زیبایی دیدیم/هم ما و هم استقلال میتونستیم برنده باشیم/از مسئولین اصفهانی و از داور تشکر میکنم/حسرت میخورم که نبردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139451" target="_blank">📅 22:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139450">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n88xAN2BVe3IVkH_b9xqOL0qkh8U6Mm-uKoffVbYkC32bvXDpYnxFHcUztLzcw-yJ5GCkhkVEp18izClHFPUMPGf2hrM4n9IT8r79xb3nUfQ3vInNPCiqU9YjYbhUAXuXy4B4efamYX6HQ6zVKloVJTB1yw8RymzildKrL4CvjJa_Wju0U_VYbKJQX-MGXqSDhxP75aatt46GaHT6R5Q1YED74MSnDMEx_3hmBJvutRO6cVkPPXUdAI_rvUJJpPnyl2hTj2CPVUnIlVeklNlsriQ42-2RZX0dnQQGsRSOTWu1LrMDevcfEoM3vySZ8807103cIZ5M_eeQ4S1XoHNyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
جدول لیگ بعد از هفته پنجم .اختلاف با صدر سه امتیاز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139450" target="_blank">📅 22:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139449">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
ترامپ: من استفاده از سلاح هسته‌ای علیه ایران را رد کرده‌ام/ ما دوست داریم با همه کنار بیاییم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139449" target="_blank">📅 22:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139448">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
🤩
🤩
خداییش یکی از بهترین داربی‌های چند وقت اخیر بود
✔️
داربی چهارشنبه‌شب نقش جهان، برخلاف پیش‌بینی‌های اولیه/ اطمینان وریا در مقایسه با سیدجلال، موقعیت‌های استقلال بیشتر بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139448" target="_blank">📅 22:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139447">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4d2d12ad.mp4?token=ozKCnk2iYBSseeP1M70jvfU8fJXjdlDm4EWYhTaQV0zOIE4cdPb4CpCV7jlS_mBzP2buj9EMQSZtg1KONyaX1H4j6el82q8XP6kmE-vqXBjy615hSMIgMgYa_KlA0ZcTwz-K9vwVOW3YSpwfvRBi9n3u1BRUQSRzVTEQJMZwCggz7qHISFSzgVbWniH6VE0AHNojAc7pN8T4z0Ynvq-D9KjfHmqjywPGvjPgJ0-pasgMobw700ukyTTfp8E-HIF69CtSYO9rjHTy08EVwJhR1aQ9g3eCIq28by9HOgfZ3T1-1KfALuJOxHqbYnxn0xCDVnkWyTGrZSRjdPCkPMi6-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4d2d12ad.mp4?token=ozKCnk2iYBSseeP1M70jvfU8fJXjdlDm4EWYhTaQV0zOIE4cdPb4CpCV7jlS_mBzP2buj9EMQSZtg1KONyaX1H4j6el82q8XP6kmE-vqXBjy615hSMIgMgYa_KlA0ZcTwz-K9vwVOW3YSpwfvRBi9n3u1BRUQSRzVTEQJMZwCggz7qHISFSzgVbWniH6VE0AHNojAc7pN8T4z0Ynvq-D9KjfHmqjywPGvjPgJ0-pasgMobw700ukyTTfp8E-HIF69CtSYO9rjHTy08EVwJhR1aQ9g3eCIq28by9HOgfZ3T1-1KfALuJOxHqbYnxn0xCDVnkWyTGrZSRjdPCkPMi6-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🤩
🤩
خداییش یکی از بهترین داربی‌های چند وقت اخیر بود
✔️
داربی چهارشنبه‌شب نقش جهان، برخلاف پیش‌بینی‌های اولیه/ اطمینان وریا در مقایسه با سیدجلال، موقعیت‌های استقلال بیشتر بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/139447" target="_blank">📅 21:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139446">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6faf16beef.mp4?token=PeTdQtdAC4iiQUPgy7e6GaJ4F-UHcgqR3Kqanknpp8YHts3oZHMsYjusNqTWvDUkDOp_dUe-YkPoW-6I13A8j8sS90tohKX47qqCUiZwpmYtJy3IVC1T_t79lV6jErN7BYHAYSfhEMeXECnctstRswNTSMdeCUj8vdfoGnJYC2mEG80zflt6bXB5UQTFID5NzpWcHvKijxR0OZFnGoIcjLHZwr_kU8w3bgApT4THb96yzExfGIHcD5-09usaxatmBB2tXxi0B1eOOqjAVZFFL1R4OIPTi9BAjxy4QnUQdadFXANZ4Hd5Tp2bBOJU5rcV5eIFJ6GUVAZdXguTTkIBJDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6faf16beef.mp4?token=PeTdQtdAC4iiQUPgy7e6GaJ4F-UHcgqR3Kqanknpp8YHts3oZHMsYjusNqTWvDUkDOp_dUe-YkPoW-6I13A8j8sS90tohKX47qqCUiZwpmYtJy3IVC1T_t79lV6jErN7BYHAYSfhEMeXECnctstRswNTSMdeCUj8vdfoGnJYC2mEG80zflt6bXB5UQTFID5NzpWcHvKijxR0OZFnGoIcjLHZwr_kU8w3bgApT4THb96yzExfGIHcD5-09usaxatmBB2tXxi0B1eOOqjAVZFFL1R4OIPTi9BAjxy4QnUQdadFXANZ4Hd5Tp2bBOJU5rcV5eIFJ6GUVAZdXguTTkIBJDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
تشکر بازیکنان پرسپولیس و استقلال از هواداران‌شان پس‌از پایان داربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139446" target="_blank">📅 21:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139445">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔱 Hero 🔱</strong></div>
<div class="tg-text">سر لجبازی ایشون سهمیه های فصل بعد ما هم به باد میره،نه با گرا فسخ کردن ،نه به ارونوف بازی میده نه باکیچ،هر کارشناسی هم حرف میزنه میگه ارونوف فاصله داره با ورژن خوب خودش،سوال من اینجاس ارونوف دقیقه ی ۸۰ به بعد اومده تو بازی چیکار بکنه تو کمتر از ده دقیقه؟؟؟ اونم دربی</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139445" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
