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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 17:07:57</div>
<hr>

<div class="tg-post" id="msg-139539">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✔️
✔️
نصیرزاده: شکایت از آسانی، دنبال نخود سیاه رفتن است!
✔️
تیم‌ها با شکایت از آسانی دنبال نخود سیاه هستند؛ فقط استقلال می‌تواند از این بازیکن شکایت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/SorkhTimes/139539" target="_blank">📅 17:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139538">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/SorkhTimes/139538" target="_blank">📅 15:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139537">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
رضا جباری:
✔️
این نسل پرسپولیس از لحاظ اخلاقی و فنی بهترین‌های حال حاضر فوتبال ایرانند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/139537" target="_blank">📅 14:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139536">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
کیسه و ترتر شش امتیازی شدن و کلین شیت و حفظ کردن امیدوارم فردا بازی و ببریم و پیام هم کلین شیت شو حفظ کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/139536" target="_blank">📅 13:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139535">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🎥
🔹
تمامی گل‌های هفته پنجم لیگ برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/139535" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139534">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/139534" target="_blank">📅 13:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139533">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
فنونی زاده : به حدادی گفتم حواست به خلیلی باشه میخواد مدیرعامل بشه و زیر پای تو رو خالی می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/139533" target="_blank">📅 12:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139532">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚫
عادل فردوسی پور: با دیدن فوتبال ایران میتونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/139532" target="_blank">📅 12:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139531">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/139531" target="_blank">📅 12:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139530">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
🔴
پرسپولیس موفق شد امتیاز تیم دسته اولی فولاد نوین رو بخره و تبدیل به پرسپولیس ب خواهد کرد و سید جلال حسینی هدایت این تیمدرا برعهده خواهد گرفت/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/139530" target="_blank">📅 12:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139529">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/139529" target="_blank">📅 12:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139528">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
فرصت به ستاره خاموش سرخپوشان نیز خواهد رسید؟!
✔️
✔️
مهدی تارتار قصد دارد بصورت چرخشی از بازیکنان جوان خود در ترکیب تیمش استفاده کند و در هفته‌های اخیر شاهد بازی کردن بازیکنانی همچو سلمانی و لطیفی‌فر در پست خط هافبک سرخپوشان بودیم.
✔️
✔️
حالا بنظر میرسد…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/139528" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139527">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
پافوس قبرس با هدایت ریکاردو ساپینتو از پلی‌آف لیگ اروپا حذف شد و راهی پلی‌آف لیگ کنفرانس اروپا شد. تیم ویتبسک بلاروس هم که میلاد محمدی را در اختیار دارد، از لیگ کنفرانس حذف شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/139527" target="_blank">📅 12:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139526">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: هوادارا فقط میگن چرا اورونوف بازی نمیکنه؟ خب وقتی بیفوما در آماده ترین ورژن ممکن هست چرا اوستون بازی کنه؟ بیفوما خیلی خوب بازی کرده و حق دارد فیکس باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/139526" target="_blank">📅 11:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139525">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
✔️
محسن خلیلی مدیر پرسپولیس: بیفوما الان شرایط خیلی خوبی دارد و دارد خوب بازی می کند ولی دارند حواشی درست می کنند که چرا ارونوف بازی نمی کند. هواداران ما  باید صبور باشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/139525" target="_blank">📅 10:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139524">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/139524" target="_blank">📅 10:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139523">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❤️
محمدمهدی محبی زننده ۲۰۰ مین گل تاریخ دربی بود
👌
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/139523" target="_blank">📅 10:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139522">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❤️
صبح آدینه تون بخیر و شادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/139522" target="_blank">📅 10:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139521">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/139521" target="_blank">📅 02:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139520">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRBUg9tUdSyNa9aQUjYNaCWY8mGwnVw7x0c6Ool6LO-jVq40Hpfd6IeoZ3BdS3173hzo8A7DwDC929ARNiOsuRcwk-kumHAvSRjXAZnCBZilBW2ABX6_ZCiyEqAaSReFCBs3iB_393LFrw4RWL16OREDJ3rXzB-QoBZgBryk1MQOJGQYWk9GbSvPHh3QSlNn-CrqjDMMZ3xOkQJyBOicvY3Uhj1tFBZsnD89_Orl5HU4D7eO74Ym7y4y9DKydjTg2asqq56CEMEsJ4C_3_SIxfKrjHysYwteK7iFnU0Ob0FG4jUPC0qs64PJE6zX5hV7IC1AEBGuuQaSBFhI9Ya1VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🇮🇷
تصویری از ناخن‌ بلند کنعانی زادگان در صحنه درگیری با آقاسی که در برنامه فوتبال برتر نشان داده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139520" target="_blank">📅 01:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139519">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
فوری ترامپ: آماده حمله دیگری به ایران هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139519" target="_blank">📅 01:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139518">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139518" target="_blank">📅 01:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139517">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: شما تعویض های تارتار در دربی را ببنید که تماما هجومی و در خط حمله انجام شد
❤️
محسن خلیلی: اینجا پرسپولیس است شما نمی توانید ناگهانی 80 درصد تیم را جوان کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/139517" target="_blank">📅 00:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139516">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: شما تعویض های تارتار در دربی را ببنید که تماما هجومی و در خط حمله انجام شد
❤️
محسن خلیلی: اینجا پرسپولیس است شما نمی توانید ناگهانی 80 درصد تیم را جوان کنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139516" target="_blank">📅 00:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139515">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⚽
🎙
رضا جباری:پوریا شهرآبادی جزو 3 مهاجم برتر لیگ است؛بازی در پرسپولیس پرمهره از بازی در تیم ملی سخت‌تر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/139515" target="_blank">📅 00:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139514">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
خلیلی: بهترین نقل و انتقالات چند سال اخیر را امسال داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139514" target="_blank">📅 00:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139513">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
✔️
دعوت بیفوما به تیم ملی کنگو بعد از درخشش در پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/139513" target="_blank">📅 00:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139512">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/139512" target="_blank">📅 00:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139511">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/139511" target="_blank">📅 00:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139510">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: برای دربی 5 بازیکن جدید در پرسپولیس بازی کردند اما استقلال تیم پارسالش در دربی به میدان رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/139510" target="_blank">📅 00:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139509">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
محسن خلیلی مدیر پرسپولیس: من شاهد هستم که تارتار واقعا دارد در پرسپولیس زحمت می کشد اما یک سری هجمه ها روی این مربی وجود دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/139509" target="_blank">📅 00:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139508">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👤
محسن خلیلی:
✔️
با کفش‌های بیژن طاهری هتریک کردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/139508" target="_blank">📅 00:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139507">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
جباری: سبک بازی ارونوف و نوع بازی تیم با توجه به تغییرات در حال هماهنگی است و به مرور زمان بیشتری برای بازی پیدا می‌کند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/139507" target="_blank">📅 00:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139506">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/139506" target="_blank">📅 00:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139505">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇷
🇮🇷
نظر محسن خلیلی و بیژن طاهری درباره برگزاری دربی در اصفهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/139505" target="_blank">📅 00:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139504">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/139504" target="_blank">📅 00:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139503">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⚽
🎙
رضا جباری:پوریا شهرآبادی جزو 3 مهاجم برتر لیگ است؛بازی در پرسپولیس پرمهره از بازی در تیم ملی سخت‌تر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/139503" target="_blank">📅 00:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139502">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⚽
🎙
رضا جباری: کنعانی و علیپور با رهبری‌ خود نقش کلیدی در ایجاد همدلی و ساختار کلیدی تیم دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/139502" target="_blank">📅 23:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139501">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
جباری، مربی پرسپولیس:  یکی از جذاب‌ترین داربی‌هایی بود که در این سال‌ها دیدیم. تیم پرسپولیس همیشه بالاتر از همه‌ی نام‌ها است. دنبال ۳ امتیاز بازی بودیم که به آن نرسیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/139501" target="_blank">📅 22:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139500">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvPF6tu4doRKcKuoi-bUuItfNSvyARhc7ap5ET_tEJOXD5th85t_kPsLF5u2l0llx678gX4AK3oPcVB_Fxu7rvsTj0DdTkJTXXAXMgqNdRwHjJCYBhRC6FqUeUMMSD8A9tp3j-4kDjUe5QWTeSArJYyhsxVOT46UQpD2q0YxGFnQqRqekuk8KdKXj5ycOOmDE2oAjbXkcl9o171GCsiLEoZcYAamDH1vBqJ1JxJch5bWRJ_-agyROZli-ILl6REgWODZ_sA5ErFjQdOw0TT7o2zB-kbiy29PHuWBkJbp1ek5hViQv_ebVMec2vUue15_Y9eTX3K3HZCawO96eKLErg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
تست های پزشکی تیم بانوان
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/139500" target="_blank">📅 22:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139499">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_ZTH48sc3_ToV2Qi9jgIrE5GJgRvzcS5EuO6DdJeSdHt_pQEcB7udp8PoeV0cPmj7dt8xxTVfEz6Du_H7uyN8H0OMy4tKCWqK-FCuolu3-wt7tYT8TezJX8wWqvrE18vghkFAQxxWQZ1dLMqzfcYICbpHsiGnqXF5OwQwsi35gxwn5L9K7ZWmfaNLl0XeuSZCkkWMBB3uttOvrkmerPTfYg1rLz8AbapRyjataKYpms70KPy5AUhvVtIMeTc2MugHhwXv4lpbAKJT91USEzx122YnygGkKTEBCW56C4M4zO46pdGu1kFYiQSefchN6g20CQCrAH8NFRhMk-S9PD8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کمپانی دیشب یازدهمین بازی بدون شکستش مقابل استقلال رو انجام داد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/139499" target="_blank">📅 22:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139498">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO2XFSS03v3zv8X-a1-wcDmIwgy7P1TbZXhxiqgZAjy96VLx1d8mDYd-xjIEPT8v7TnougLAX13sKQXdXU7TWPQRCQdJDk6OZMckGG4BmnZoOYySb41XsdWdYZdnhYw5J2Tgk1atmDfOGN50nsM0xLyObywprTIHJY1tfmDq2nc12iDi4aErMvgekfDIFYeUdTGfZwczsgCEZWnf995DgogLFm18g03e_QghWjE3aVZvO-ZXnApznF0-tcPd3X0VMF0DD88P1BW_lklYra2I8BIIFqVRQ8ieM0h-r1Hffbz5IeazNKB5VWSepztCC4miVOtuVADaupXUHoCsoK2tcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/139498" target="_blank">📅 22:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139497">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
تارتار ضعف پرسپولیس را پیدا کرد!
✔️
تارتار به این نتیجه رسیده که پرسپولیس نیاز به یک رهبر در خط هافبک داره و نیم فصل قطعا در این پست تقویت خواهیم شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139497" target="_blank">📅 20:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139496">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjSyPq5cvYQwg5Ya5H6WEfA--03rAljQ5B7epmGzKELhMUj0sy2eRQKofRZWGenqcX8DptxaNZtEBOvFRKqyDf-r5C5z0AAQCebNXqLHsoZEXhc90PWov5H2DtC7ejhtROmKO1L2d26J8il0MDytX3osVEFWVIsNihve9S-4sglfQiv4zaEMFPfxfZjoWRMWMKSQvKRrgzM7J1CwyFYeOeGD2VpR3gCOxzbtc-hhQ68LVJh9OpZxD0yId5ePppulXwH5thWjDsYegN16aeH43BiGW0uGs-kji4hD3oyODrdm3dcZK9e77VsF-pR9rAociA2o6aBf9EUj_fTkeqOb6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🎙
خلیلی سرپرست پرسپولیس:
❌
مصدومیت گرا از ناحیه آشیل است. تارتار گفت اول باید او را ببینم و در مورد ماندن و رفتن وی نظر بدهم. هیچ اختلافی بین اورونوف و کادر فنی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/139496" target="_blank">📅 20:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139494">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNmGHGy3GI2j_cv_OeTHIe6xN7639jnSi5mg8VRRpH3aJEymJovogCb7zc85Wl5ZCCKisjU8ITCyrbK6WCnlI0Hcafmrk1Id8QivARiBo3aSoE_9Z-m0yiGcY3x09yy5YjxyGLxRRmIcNeMJenkVYJu2TLk__9tN8GBv5o56412I4DzWRG5M5ovxDxk3vMhoLuPBKHZDfzznfaS55lC1Zzj_tgzZwHxxYLBNlvIeh_IGgj-u3DpOGl1yH1hodBfWIRc9D7C2LN6ZNHCyT8ZHKJTBy_yczCPibJzc5AgWM_L7op60ZlPme5tcwmsXW0vGPRgLABYq3jx1O__tzwgdvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139494" target="_blank">📅 20:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139493">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJNus-P56ln7FU_KlgxuUn2haJ23DDsaHLg9oz_z7EWJBwUcwgodg1scW1nvQD5Df3ls3agunaweCiZHZMnQ0x-ea4hkXrps98Cs8EHt5pVWl_XdP1lZCiip18CL4Z57k9L5DnpPKXNS_vZZLcWz3K-vmqtj_2x8hYy9kaF24eSQwACTuRuOq0i_oJj6zO6T19I_NyI-A2d8v1d6ftULeTPHOWwamaRoqCEpvAKyYfP62qoyxadHcD11eKtjGcTwtp1OZWEyuGCNEYrECbJaCT06iWJv9cSnml-6REkQx4dQmhOLNhj5c27oRMtsXGmHLqIJsj9UasFMHvoRop6_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
حضور ابوالفضل جلالی در بازی امروز
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139493" target="_blank">📅 19:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139492">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFi1tRCUANZ8nk1nxwc4q7rJdT4-YmFoTv1lN-aNkPkQqiBeLucxW6m6AIweKRv7cY6tz_gjSM6yr1bPTGHWpoxEDwd9LUmv6JOOOPpRHqL2wxeiR7o828RfF1Keu1PUG6KwpX8KJyIE47kF1R42W75p0_hWr4KmT8ZL8_LNa_JdvCNo9HsMkcCyuiR0a9b2s-SMbeHDvUBhNrF6wSjE5Y8NI7eA8xexhf87wYYDiFD5qSGQSc1H-Je63Vj-HVfpaPdg0wPCMww2x2zVbNAzUciyHL65U_nx4g-5ZHM1fwabgdbSigjFAoQnFNkxV_kHGuxSHwzkW0tj09neZ4fH8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
محمدمهدی محبی زننده ۲۰۰ مین گل تاریخ دربی بود
👌
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139492" target="_blank">📅 19:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139491">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">#بماند_به_یادگار
🔗
💯
تا روزی که اردوبادی و اینانلو داخل هئیت مدیره هستن این تیم رنگ آرامش نخواهد دید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139491" target="_blank">📅 19:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139490">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0nhU1Cl4JhyNZAyZNVkEUEXNFgs_3wqcejx8lj3EmerPakPceHz2WQJv7T6_DJEgK5N3UlIjatMbPIrYigeI4Ac1aPxcA0XSe5dPfE4Uk2EytYp3_qX7_qqk5aqIZ7FE2I94kL2Vy3L9Mf-4LOhTVm1GkFzi7xYXV4SoMEIBeml1Fe_wEivA7zOGwk3vNfXNUkGoWvWuLaFTUF-v_GCsKbwgdt8PIuuFKnxZaqsx7EudHo_M8Xgv46IC50WAWR9egf1r1w7jlqVn1T6KIb_ku92J4vOCUvLju1uEPY_JcmK8pJrIviBrgalWzkJ2Okzkqi8-0L9vhFCV9NQa1MztA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
پرسپولیس امروز در دیداری تدارکاتی به مصاف مس رفسنجان رفت و با تک گل پوریا لطیفی‌فر به پیروزی رسید.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139490" target="_blank">📅 19:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139489">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFzvEi-H564HroUjkZhIqJZSrQZ3rY-KqWA4vcarAmJI-9ERW1bjB_UJZN4MORevkQzOYFQDt2b4oSkBE1GlhTEh3yBvT8OYp-O9oWHMd-CofHsGBLJW6Txp7UCyc9YMRhmhY0xn_jtgty0FvoiFCsbD91LqO7EmcdAUXeqQ8vd5aS7ANmwcgp5mjaHKqDATjoV5N8t50uqOBtYwvmDJEznIavli3IF3giNztKQCCzY6soW11ahXnmCa7KC9Inv7GxgGA7S_fQRsdK6GxwaXOcTuaMNaDEHLncE_OG0D03pYALwAls1dQYXHLXKmNC-4jboOJkgc60fChSmUwt5r-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
محمد عمری از فصل قبل تا الان توی ۱۷ تا بازی برای پرسپولیس فقط ۲ تا گل زده!
⬅
⬅
با اینکه آمار همه‌چیز نیست و کارایی بازیکن روی بازیِ تیم هم مهمه، اما هوادارها اصلاً ازش راضی نیستن و انتظارات رو برآورده نکرده. امیدوارم بازی دیشب براش درس عبرت شده باشه، تصمیم‌های درست‌تری بگیره و بیشتر به درد تیم بخوره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139489" target="_blank">📅 18:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139488">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🏅
باشگاه استقلال قصد دارد به دلیل حرکت حسین کنعانی‌زادگان در دربی ۱۰۷ مقابل عارف آقاسی علیه این بازیکن شکایتی را به کمیته انضباطی فدراسیون فوتبال ببرد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139488" target="_blank">📅 18:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139487">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ1WaNsUB4zytZNgrHFJaa6aJ-taFpPurfZE6tRBk_b3iuW0aHpwun5ScpmhW1gYUfaGwRzb8-QZ8BiT2u4PFDL4xXDF7IaJtQ8ZXO_SHdBg2qEWR6yi3hXy1xrp_8khxYRq9FQVCJr1lkfwYdz046Wp-JGLWMNXgFL_mUaHPzwplxXn3I2xjABfLHIfnLcg1A5FbKAHq18uQlR0TjW12zDPaOo4Uq7Ju5RQxUJ9Ihc5OvF6eaaSsxTle9Aq2qtLr3AgWHkWxMz8a7LlbFaTDGUh5rehmPtDxmfAJXr9tWS6LY50kWsG6-1HyXcdWyShedL3O3eBZ8Ajg5xmx4bFYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
باشگاه استقلال قصد دارد به دلیل حرکت حسین کنعانی‌زادگان در دربی ۱۰۷ مقابل عارف آقاسی علیه این بازیکن شکایتی را به کمیته انضباطی فدراسیون فوتبال ببرد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139487" target="_blank">📅 17:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139486">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
✔️
دانیال گرا مدافع مجارستانی تیم پرسپولیس برای هفته پنجم از لیست بازی خط خورد تا یک سهمیه خارجی سرخپوشان برای فصل آینده به خطر بیوفته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139486" target="_blank">📅 16:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139485">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
✔️
خبرگزاری مهر:
🔴
پرسپولیس پیشاپیش شکایت خودشو برای حضور یاسر آسانی تو دربی آماده کرده. پرسپولیس اعتقاد داره کمیته انضباطی و سازمان لیگ صلاحیت لازم رو برای پرونده درباره یاسر آسانی رو ندارن و استعلام فیفا باید منتشر بشه
🔴
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139485" target="_blank">📅 16:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139484">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139484" target="_blank">📅 15:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139483">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=WYaBV8GDn1Ai2NeSDeSoUEywnrj8FlIotSorqZGme9buUpfVjJ-PGRP3Lob7xLLqe8M51dE7AdVziru53WQEcUTx9GrOlt_rHfgz8GK0RiKOejac7A8lLgaT4kFTayrs6CYhtxhqDbUb6Twp8dbOWXk7oeWcAeZcmBr7MNOFn8xOLCcba5nrGbi5ti7EJWcwzXuxxCimH0OfuHKOwHQCFW78pAAiEZZ3aJem6pc3q_RxkUR1LqnZ_ByOP3-1ET-ofA6zuevRZ6P9P-DsmWTymJTCgTq1i28ySrzFjB_KlKVQZDkqdPa6HPdOjYzjbNF8KW_PRl-vHkmOgDA8x4ErGpunm-4THjHoBPQIaDTHbRspT6XR03qvrSkVKCrglQxmqb5Ji3obzNHQ--pvpFO-0jJDn0Ymy_5rfWHogV7dEDvy8TdPn-rd8pnLe85bHX4ezta95NDI58TpWwCXpHt-PwMYM2dq8qXmStXUhRXzLY0GQdqng5lwMaQYfEjINqsSxjT35V-Gc6DF5HpofO4jghdxZfdJrrYQY7RUQDfHNPvVXmbzKyFYvlp51EfRgOKBPizVU04BZeedDr1dXJO6L9_B-yHMJH8zGdI7IAcMtJxwbrNbIvzzUiQAJ5RHbLzOwCYnb_fC7CKUa4iiMjHFSkNjtU2TvUBX1vo6UqUXuQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=WYaBV8GDn1Ai2NeSDeSoUEywnrj8FlIotSorqZGme9buUpfVjJ-PGRP3Lob7xLLqe8M51dE7AdVziru53WQEcUTx9GrOlt_rHfgz8GK0RiKOejac7A8lLgaT4kFTayrs6CYhtxhqDbUb6Twp8dbOWXk7oeWcAeZcmBr7MNOFn8xOLCcba5nrGbi5ti7EJWcwzXuxxCimH0OfuHKOwHQCFW78pAAiEZZ3aJem6pc3q_RxkUR1LqnZ_ByOP3-1ET-ofA6zuevRZ6P9P-DsmWTymJTCgTq1i28ySrzFjB_KlKVQZDkqdPa6HPdOjYzjbNF8KW_PRl-vHkmOgDA8x4ErGpunm-4THjHoBPQIaDTHbRspT6XR03qvrSkVKCrglQxmqb5Ji3obzNHQ--pvpFO-0jJDn0Ymy_5rfWHogV7dEDvy8TdPn-rd8pnLe85bHX4ezta95NDI58TpWwCXpHt-PwMYM2dq8qXmStXUhRXzLY0GQdqng5lwMaQYfEjINqsSxjT35V-Gc6DF5HpofO4jghdxZfdJrrYQY7RUQDfHNPvVXmbzKyFYvlp51EfRgOKBPizVU04BZeedDr1dXJO6L9_B-yHMJH8zGdI7IAcMtJxwbrNbIvzzUiQAJ5RHbLzOwCYnb_fC7CKUa4iiMjHFSkNjtU2TvUBX1vo6UqUXuQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139483" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139482">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139482" target="_blank">📅 15:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139481">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❤️
خدا بنده لو، بازیکن پرسپولیس:
⚪️
بیش از اندازه در مورد ارونوف حرف زده می شود. چیز خاصی اصلا وجود ندارد و هنوز خیلی از بازی ها باقی مانده است. او اصلا افت نکرده است و اصلا زیاد بازی نکرده که بخواهد افت کند. همه از کیفیت اورنوف خبر دارند و هر تصمیمی سرمربی…</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139481" target="_blank">📅 13:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139480">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139480" target="_blank">📅 13:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139479">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✔️
✔️
باشگاه استقلال نسبت به عملکرد و سرعت بالای تیوی بیفوما مشکوک شده و احتمال می‌رود درخواست تست دوپینگ از این بازیکن پرسپولیس را مطرح کند.//هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139479" target="_blank">📅 13:37 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139478">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJcinnqj4KNZ3bkuMzu_C_fxlMWWanYKhbpr-g4a2gd5BU9MhzF3NRyltMDi_l2g5q96RoY1-VNzgqHwA7UgwMWY37B4Fd1I5i1mU4Dvzt9knQKiwygdtMNJhOVb0NLdQCpu0Mteew2HbdXhYIQ9LniV7NQh_iuS2kXFEdFYLN7PQq05xJt5tChwa8t7Mk0KXC8vI4gwcmrnkL0eGPqQIWgxkgfreh7YOSzblq4SaZ8QNQ_P9U4MOelrSS_l8ynDYeDCMgqPfdt5U70r0IswcQO8A9Trgc1fSRPTwZpJNNZEu-D4fZeQZOTeTOmwwIBF-etsR2Mcw4iNvi6l2b_d3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139478" target="_blank">📅 13:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139477">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔄
🔄
🔄
با حضور یاسین سلمانی در بازی دیشب حالا مهدی تارتار به تمام بازیکنان پرسپولیس بجز محمدحسین صادقی که تا حالا در لیست قرار نگرفته بازی داده و تمامی بازیکنان با ذهنیت آماده به سراغ ادامه‌ی لیگ میرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139477" target="_blank">📅 13:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139476">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139476" target="_blank">📅 10:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139475">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
باشگاه استقلال نسبت به عملکرد و سرعت بالای تیوی بیفوما مشکوک شده و احتمال می‌رود درخواست تست دوپینگ از این بازیکن پرسپولیس را مطرح کند.//هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139475" target="_blank">📅 09:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139474">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/139474" target="_blank">📅 09:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139473">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
عادل فردوسی‌پور: ترابی قطعاً ادامه فصل رو از دست میده، با خودش صحبت کردم و گفت دو پزشک بهش گفتن رباطش پاره شده و باید عمل کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/139473" target="_blank">📅 09:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139472">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✖️
✖️
هافبک و کلا استقلال برداشته و خیلی خالی هست هافبک ما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/139472" target="_blank">📅 09:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139471">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/139471" target="_blank">📅 08:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139470">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rylLceaKxTlxXIKhO4LNuaaowIXajPKgBfqGbJI3j2WEfTw9AfoddzORcvZ6-Lxpkv5ONeC--DIQVWs6js3C7oyas7dP7wlpO1EmZx9Z15eW5q_PSDl2IeU-Q7gt270Ia04X_PR4f-Ds_tti81Xg8eDPTCBjOyKlaTmx8OE3xJNvPbNRc8dZr9pjayMlKWAsPPpH5rvgaJs27RCQHNf4slN_ASPUPUAezJF2rjMBJx9_R6E-mebgnifB5ZWYJYZNXZ11M1jpx9Q6dLqLt1fbaxyYCZy-VTKKi3Xh4QECZ0mSdZfxzfidu4G_LSifL9yoe-XOm4IuwURX5fjJVtSTdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/139470" target="_blank">📅 01:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139469">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/139469" target="_blank">📅 01:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139468">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⚽️
⚽️
استقلال و پرسپولیس امشب در مجموع 33 شوت بهم زدن که 9 تاش در چارچوب بود، برای درک بزرگی این عدد باید بهتون بگم که در مجموع دو دربی قبلی 33 شوت زده بودن که 10 تاش تو چارچوب بوده که یعنی امشب به تنهایی اندازه دوتا دربی قبلی روهم موقعیت دیدیم
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/139468" target="_blank">📅 00:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139467">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETEsc5_0gOODk7y3DojIOu_-JXbOHbp2wuBdyv2XaJxH76r1xznHNdTMliqrbsnKLc7qE4jXCWmhfQz0u0pNTwFUy-AJO14pvLb3H1MdpiVvGf4jii98MOxXqV2YmSLaGeWBZLxXRndVlNVMNp1xwjXgCPC5v9D5uaWm4tSiIFxjYc3mst9AmuV_1KLTU8lX9Agti3AmhSx9L9ugAiCg2Vbgf33NCiAU7t8PpNTS62_09Obxe1di2045LmlAVPMK5ApT-dBLQF5Qs_AQCzp_rxdqZeDqQ7xVTEURgLeYkNiHOvuk35iCMPEdl1vnRqcTI2c8yQYs8KihlsJ76iOyjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
استقلال و پرسپولیس امشب در مجموع 33 شوت بهم زدن که 9 تاش در چارچوب بود، برای درک بزرگی این عدد باید بهتون بگم که در مجموع دو دربی قبلی 33 شوت زده بودن که 10 تاش تو چارچوب بوده که یعنی امشب به تنهایی اندازه دوتا دربی قبلی روهم موقعیت دیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/139467" target="_blank">📅 00:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139466">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/139466" target="_blank">📅 00:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139464">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGcN15pYDRLiq1dd4rBgUdz0HYZrd1h4A9ug4EHZVeuayQq9j8wwG36ZAMML6VMG6cA4NaKeBlOLwfT4JQAJraNS8QDnMqgzP61AXugTTsEdCsTJE2YH0rNTvMsAPWQPMITLusUf6GjXozR0J9EDf5608oOQJopA10ezNfuvYCg_gFujT0JdqgmbWFORFPyl1Etn1MNMO1tResAhlBJVYgDTwskzySqKd1o6LYEv-lQjjVGMNBO4Is0dEY2yQaW_v5tPw2fIjekEryUoBAgKlcNoE_rGrQcQ6fo6bc0oF8XbPktMox0shVirJDysbHXrdzrvEkJ8FrdXVrQKGnbkuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/139463" target="_blank">📅 23:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139462">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc62967a0.mp4?token=b5l3uLt4-5MLjaZmaiobawgBX39dhpVnf4n0LSyOj2xCYZhzl_0WR7i908qkz7QxNLihMAAyXGHeAK77tPfDqO9WN-XvpY20COxlce1kW9ERlI5IUNyw6uFcF0dean0UoO_vRwFrFaEck5V3VvhRq5ufuh58COfbJkZHk500B9yZLANLbpZoAGhMlQ8c8UUuCcQTnzN_R3yth794yuwQJfSEPaZO14213HyB0-b1-CoTBymm63hr5xIRNcKF20zpN8UvDZxlK5rL-F3YACBdNeA1J24F4UHzgwPlj2PXkpekCCiFNCEoTVWKKtaaALAa4mUilRIHryiQ9qF1u65tNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc62967a0.mp4?token=b5l3uLt4-5MLjaZmaiobawgBX39dhpVnf4n0LSyOj2xCYZhzl_0WR7i908qkz7QxNLihMAAyXGHeAK77tPfDqO9WN-XvpY20COxlce1kW9ERlI5IUNyw6uFcF0dean0UoO_vRwFrFaEck5V3VvhRq5ufuh58COfbJkZHk500B9yZLANLbpZoAGhMlQ8c8UUuCcQTnzN_R3yth794yuwQJfSEPaZO14213HyB0-b1-CoTBymm63hr5xIRNcKF20zpN8UvDZxlK5rL-F3YACBdNeA1J24F4UHzgwPlj2PXkpekCCiFNCEoTVWKKtaaALAa4mUilRIHryiQ9qF1u65tNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
بیفوما امشب دوباره یه استارت ۴٠ متری زد فرعباسی وحشت کرد دستپاچه توپو زد بیرون‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/139462" target="_blank">📅 23:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139461">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
جدول لیگ بعد از هفته پنجم .اختلاف با صدر سه امتیاز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/139461" target="_blank">📅 23:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139460">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❤️
خدا بنده لو، بازیکن پرسپولیس:
⚪️
بیش از اندازه در مورد ارونوف حرف زده می شود. چیز خاصی اصلا وجود ندارد و هنوز خیلی از بازی ها باقی مانده است. او اصلا افت نکرده است و اصلا زیاد بازی نکرده که بخواهد افت کند. همه از کیفیت اورنوف خبر دارند و هر تصمیمی سرمربی…</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139460" target="_blank">📅 23:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139459">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
کنعانی زادگان: تارتار تیم خیلی خوبی بسته است و امیدوارم آخر فصل قهرمان شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/139458" target="_blank">📅 23:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139457">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/139457" target="_blank">📅 22:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139456">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
✔️
هر دو گلر بد خوردن گلارو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/139456" target="_blank">📅 22:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139455">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: ما و استقلال خانه نداریم!
✔️
پرسپولیس و استقلال متضرر می‌شوند و ما خانه نداریم در شهرقدس از پتانسیل هواداری نمی‌توانیم استفاده کنیم.امیدوارم هر چه سریع‌تر استادیوم آزادی آماده شود.
✔️
اورونوف هم یکی از آن‌هاست هر کسی از هم‌پستی‌اش جلو بزند،…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139455" target="_blank">📅 22:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139454">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
تارتار در نشست خبری: گروه داوری امروز خیلی خوب عمل کرد، خسته نباشید به آنها می گویم/ امروز هم پرسپولیس خوب بازی کرد و هم استقلال
✔️
✔️
به خاطر گل مساوی که خوردیم واقعا حسرت خوردیم
✔️
✔️
هم ما می توانستیم برنده بازی باشیم هم استقلال اما در مجموع ما یک مقدار…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139454" target="_blank">📅 22:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139453">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👤
خدابنده لو، بازیکن پرسپولیس:
✔️
بازی بیرون خانه برای ما حساب شد‌. امیدوارم ورزشگاه آزادی زودتر درست شود. در مورد خودم نمی توانم اظهار نظر کنم. الان فضا بازتر است و امیدوارم ادامه دار باشد. دو تیم موقعیت های خوبی داشتند و آمده بودیم برای بردن اما حیف شد.‌شرایط…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139453" target="_blank">📅 22:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139452">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bebc6bdd.mp4?token=XiCm4IaAjvi_xILOBgxo9hEkPwlz4WTnCQ2G3xBtAxWBryjRbUJiU5Si89pW2nMwvI8zLeoDtAUVH1wRxc00yX6H08I8nyi_JVV3D6k01wsYnpiLlmjYaRn3igWSENLRrlj94FnQatganeiSgdT9VlHEvbqewsU2r8Qa4dbsTAg8kSNyDavKoa2juzHUFl0v5Z1LYB4K9PpP7pumjNA3trjB_0U12BiQt8ZW-SOfwtRC9bC0e0AHTPwZb-2R6fkyKPodkbBj5h4-WSrgn4HNwm5F9CGSuVhnNk5zi1H2uBqk-hP6MwLHA8vmIh0gbUa6t2ERla8iFcS2DCj5JT7fRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bebc6bdd.mp4?token=XiCm4IaAjvi_xILOBgxo9hEkPwlz4WTnCQ2G3xBtAxWBryjRbUJiU5Si89pW2nMwvI8zLeoDtAUVH1wRxc00yX6H08I8nyi_JVV3D6k01wsYnpiLlmjYaRn3igWSENLRrlj94FnQatganeiSgdT9VlHEvbqewsU2r8Qa4dbsTAg8kSNyDavKoa2juzHUFl0v5Z1LYB4K9PpP7pumjNA3trjB_0U12BiQt8ZW-SOfwtRC9bC0e0AHTPwZb-2R6fkyKPodkbBj5h4-WSrgn4HNwm5F9CGSuVhnNk5zi1H2uBqk-hP6MwLHA8vmIh0gbUa6t2ERla8iFcS2DCj5JT7fRDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
خدابنده لو، بازیکن پرسپولیس:
✔️
بازی بیرون خانه برای ما حساب شد‌. امیدوارم ورزشگاه آزادی زودتر درست شود. در مورد خودم نمی توانم اظهار نظر کنم. الان فضا بازتر است و امیدوارم ادامه دار باشد. دو تیم موقعیت های خوبی داشتند و آمده بودیم برای بردن اما حیف شد.‌شرایط تیم خوب است و همه متحد هستیم. هواداران صبورتر باشند ما تغییرات زیاد داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139452" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139451">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
✔️
مهدی تارتار : بازی زیبایی دیدیم/هم ما و هم استقلال میتونستیم برنده باشیم/از مسئولین اصفهانی و از داور تشکر میکنم/حسرت میخورم که نبردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139451" target="_blank">📅 22:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139450">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3-gNKp_M50PjkyuamGyMcIX_SMn-fpj8We6mlXFrFVkxV18bBAokMyOJU5HgxcbcRz5bWWUTKlBuPptjcSPgg6vrq-zOwwnGFBk5KZPnT3_J73WQOGcuhBom7q7WNt6d1xl6wQq8WEpeQeztNydtiB7k9LY2Rkt3F6mM48spfSbqM9JZHWoplqxnrNZo7NjtM2V-hRY3Ml6b_O4n0O88_LsnS7E_Rix3KQbW2BHWLg2NYtsOD5G3-FHXD-A-l7gZd9bA1dsSp6K0oko7ktUPvfjNftwgEz5zVNfTnD_LK9iWxGBQb02KRAiWv2kpo9goOgMjeKzFUrLbWzHVc3KTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
جدول لیگ بعد از هفته پنجم .اختلاف با صدر سه امتیاز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139450" target="_blank">📅 22:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139449">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
ترامپ: من استفاده از سلاح هسته‌ای علیه ایران را رد کرده‌ام/ ما دوست داریم با همه کنار بیاییم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139449" target="_blank">📅 22:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139448">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139448" target="_blank">📅 22:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139447">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4d2d12ad.mp4?token=VHUNOyx1PkDhv2JspXpr8iKdLrusug1wecLWhdjDU5x1Ay8tCOd1x60XWNRs0lv7ASH-YvbxdaykDrZwAp9qIv8grWyK-rH0xLxRvcnl3hPjgwQH-0i8mb4hYZeMSuEcKTWTNsD7KmwXqVI4ITwGOpPjVqqXk_eDeyK3mKxMjtMPkWQCBRlQoJ3jzj1EI6DZ21kCiap-cMwjMP1ZNZk9mf9rKnfBRgRv0haqY5uZuqE_v9VrsC7eLWwAUY9-jrkaCQ9exiFjzFA1-jLG4vxi79L5si-WRyMHfACOLllQMSxWZ1__-wBtDQXWKqkJ9oCUi5UD2TtnBvCaZH-qeZt7WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4d2d12ad.mp4?token=VHUNOyx1PkDhv2JspXpr8iKdLrusug1wecLWhdjDU5x1Ay8tCOd1x60XWNRs0lv7ASH-YvbxdaykDrZwAp9qIv8grWyK-rH0xLxRvcnl3hPjgwQH-0i8mb4hYZeMSuEcKTWTNsD7KmwXqVI4ITwGOpPjVqqXk_eDeyK3mKxMjtMPkWQCBRlQoJ3jzj1EI6DZ21kCiap-cMwjMP1ZNZk9mf9rKnfBRgRv0haqY5uZuqE_v9VrsC7eLWwAUY9-jrkaCQ9exiFjzFA1-jLG4vxi79L5si-WRyMHfACOLllQMSxWZ1__-wBtDQXWKqkJ9oCUi5UD2TtnBvCaZH-qeZt7WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139447" target="_blank">📅 21:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139446">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6faf16beef.mp4?token=KFsVvcAINdwZdUgzgrZDZBQK2oQl7XZQe0peySItRMvuRm3ZG4RPTnjjDwTwnceY2BVxps1r8-SOMHLiZlni7mJMqTb8nA6DRH5XYboYbJnRVosJeAaBnffBLdbUqeCn5Lcx-Qj7Skg4GjqAKrr7uVIDrHIdqx9sPG9iVvTwWc6MVdsKXmAp9R_3VTtXm80DBA4aTtZjhape51mHnn3jjTMpz50YDNNUYG-7ewrRnz2USLJDAs4bWeRfXA7X5OtICZ7UbeznHknMdA-o9BuwWdVol-iB4p4E2qghb5TOFTLlr0_o8llnSEzQGkdtXG1TtgA-4VsHWWQPb1LusvW9SDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6faf16beef.mp4?token=KFsVvcAINdwZdUgzgrZDZBQK2oQl7XZQe0peySItRMvuRm3ZG4RPTnjjDwTwnceY2BVxps1r8-SOMHLiZlni7mJMqTb8nA6DRH5XYboYbJnRVosJeAaBnffBLdbUqeCn5Lcx-Qj7Skg4GjqAKrr7uVIDrHIdqx9sPG9iVvTwWc6MVdsKXmAp9R_3VTtXm80DBA4aTtZjhape51mHnn3jjTMpz50YDNNUYG-7ewrRnz2USLJDAs4bWeRfXA7X5OtICZ7UbeznHknMdA-o9BuwWdVol-iB4p4E2qghb5TOFTLlr0_o8llnSEzQGkdtXG1TtgA-4VsHWWQPb1LusvW9SDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
تشکر بازیکنان پرسپولیس و استقلال از هواداران‌شان پس‌از پایان داربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139446" target="_blank">📅 21:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139445">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔱 Hero 🔱</strong></div>
<div class="tg-text">سر لجبازی ایشون سهمیه های فصل بعد ما هم به باد میره،نه با گرا فسخ کردن ،نه به ارونوف بازی میده نه باکیچ،هر کارشناسی هم حرف میزنه میگه ارونوف فاصله داره با ورژن خوب خودش،سوال من اینجاس ارونوف دقیقه ی ۸۰ به بعد اومده تو بازی چیکار بکنه تو کمتر از ده دقیقه؟؟؟ اونم دربی</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139445" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139444">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⬇
👤
آقای تارتار بازنگری بکن وسط زمین وله، چرا از باکیچ و لطیفی فر استفاده نمیکنی ؟! لطیفی فر هم بازیکن مستعدی هست هم قامت بلندی داره،مسئلت با خارجی هارو کی میخای تموم بکنی ؟ به چه قیمتی میخای اورنوف و باکیچ بازی ندی؟دقیقه ۷۵-۸۰ برای بازی دادن بازیکن جوان و تلنته…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139444" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139443">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOqvjWs7Ql34yOksoHv_PlbcERCrPI1LCXHwIeCj8sUVRbjYIa5Vh2vp3Q8nVUjrvNNkNws3603zIgxoqyHeGzZDh5IdibEr6cy9znjcFrLKOLNqXW0Guqr0ttPBR74NGhVIKVmBbF-5Rqn6x5-kj6WQqRm4GT_ooD6ciJnx5bi9mc1bNTXzgQou3wVJcXzSmPiprVEWXplHXLlimss2kV2CBN2mQQJd0uD3f3tdb9uGVhjmrUPhTAx9WYDHIrAyv5GWQWzx1stsmQIClBOZ2daiz9vnsNKmQbpFUf8f3-CFSCAcftSb9Gd6JAtgkwVAIziutUxVlKwVADJQoUB62g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
♨️
🗞
|
#فوووری
از تسنیم:
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
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139443" target="_blank">📅 21:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139442">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
هر دو تیم و هر دو سرمربی به مساوی راضی بودن و خوشحال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139442" target="_blank">📅 21:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139441">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🗣
🟥
بازی خیلی خوبی بود از هر دو تیم ولی بنظرم بعدا حسرت این امتیاز های از دست رفته رو میخوریم، تراکتور تیمی نیست که مثل بازی جلوی شمس آذر به راحتی مساوی بده و باید قدر این موقعیت هارو بدونیم، بنظرم راحت میتونستیم ببریم اگر تعویض ها زودتر انجام میشد و باز هم…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139441" target="_blank">📅 21:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139440">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🗣
🟥
بازی خیلی خوبی بود از هر دو تیم ولی بنظرم بعدا حسرت این امتیاز های از دست رفته رو میخوریم، تراکتور تیمی نیست که مثل بازی جلوی شمس آذر به راحتی مساوی بده و باید قدر این موقعیت هارو بدونیم، بنظرم راحت میتونستیم ببریم اگر تعویض ها زودتر انجام میشد و باز هم اگر وسط زمین رو داشتیم متاسفانه هم جلوی تراکتور هم استقلال وسط رو دادیم و همین باعث میشه دقایق حساس فشار سنگین بیاد روی تیم و بعدش با کوچک ترین اشتباهی باعث میشه گل بخوریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139440" target="_blank">📅 21:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139439">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139439" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139438">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139438" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
