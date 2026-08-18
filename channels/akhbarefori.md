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
<img src="https://cdn4.telesco.pe/file/ruQz66cNyZAQfFMlewHMgl1m3B0dTLs8wEP4mTYC4_IK2ggdPrihuAqD8lCW5WHV24fPFg5VvLjdbJZB0yNNorzr80PeXelWRgu9na4ILKLOPC6Tu_WphVJKKH_4u2xGWi68ATefeBp_JwKOsVb1rGuukDz8NEihUchHV7m4SzQfa3vBJ6YrYDYJFZThYIidjUnR4HwZl6hmut2VSfFb2dNniRG3CGwctGXT5NG9s-FtaBGSp-1JpF_VD5jREbsEr_lgJBITnyKlKyveaOKAIVjZ-gF545otO4bZKx7NWUlmDNr9u1VdvOV3j5xSgsYElsscegTG3ehP95BgieNjfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.09M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 21:20:59</div>
<hr>

<div class="tg-post" id="msg-682337">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-Axg7FaU_Udu8YiK95RIt-0DOsZiWRqFpiafdAlVFYMn-TTZyfxwYPTD4s_XC-NittRdpTlKykq9Ow75V2BZ7dXdGXvwIElIRwEb3PNWCjU6JhXMA47VYvf5Ffku30RMeaW7Z87ok0-300sI4AAFy1XAMFE9R3_OCVPHsyl2BLYnOp3kMP0jIPbOnDnOBrXPXJRaQtdEdxENqFIpLcIkyykqUvjdhT_J7YuMlnGKqWiAJ6bc4RMqxfHWYNpxl1dL99uwQ_lAR3dBVDpZU818pxm58LtaSnxN94FS3a1LAOCP1dPvVw9axiEQtiBJOtW7bsIJXM9qoAazZF8dbgF4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر انقلاب: بیگانگانی که از هزاران کیلومتر دورتر، طمع‌کارانه در خلیج فارس شرارت می‌کنند، جایی در آن ندارند مگر در قعرِ آب‌هایش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/682337" target="_blank">📅 21:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682336">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c91454bf7.mp4?token=vpME581UUQ86Xgd_ZICNwvwp8Mcqs_mS0Aoj91qa9QCMFo05GA9-Mk5WVnZL5C-bAZlW4zKVoa3ksI7zxqh9rkFb2v4D228s79HZHcXe7Qu7JXfyjoli1waPgPgJDKfzE_Mq4x-IkQMN1LTbsxZENWNWM1hoBMb4K6JVzTGtkPdeyU7SyXT7nubUqBkpQXLjKL2spy-IBlQCOtsumeFnMcaXxxHFBnkVfeUeR8UbtTGhYBJF58ulg9g8lJ__ba3u_0lF7nh_mh0a6QxyZ9BQCuGFHd-pJrfLdBVC9VWi1HC7UY7dq7hSwGE5QvLqXPjJQpcfD_pzMBnZxt382Wu6Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c91454bf7.mp4?token=vpME581UUQ86Xgd_ZICNwvwp8Mcqs_mS0Aoj91qa9QCMFo05GA9-Mk5WVnZL5C-bAZlW4zKVoa3ksI7zxqh9rkFb2v4D228s79HZHcXe7Qu7JXfyjoli1waPgPgJDKfzE_Mq4x-IkQMN1LTbsxZENWNWM1hoBMb4K6JVzTGtkPdeyU7SyXT7nubUqBkpQXLjKL2spy-IBlQCOtsumeFnMcaXxxHFBnkVfeUeR8UbtTGhYBJF58ulg9g8lJ__ba3u_0lF7nh_mh0a6QxyZ9BQCuGFHd-pJrfLdBVC9VWi1HC7UY7dq7hSwGE5QvLqXPjJQpcfD_pzMBnZxt382Wu6Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده مجلس:‌ با وجود این که ۲۵ سال است از مونتاژکاران خودرو حمایت می‌شود تنها ۲۰ درصد موفق به داخلی‌سازی شده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/akhbarefori/682336" target="_blank">📅 21:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682335">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
وقوع حادثه برای کشتی در نزدیکی آب‌های یمن
🔹
سازمان تجارت دریایی انگلیس از وقوع حادثه برای کشتی در فاصله ۴۰ مایلی بندر المخا در استان تعز یمن خبر داد.
🔹
این نهاد انگلیسی تصریح کرد که کشتی مذکور پس از حمله در مقابل بندر المخا دچار آسیب شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/682335" target="_blank">📅 21:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682334">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlMYWMw7lq5QAJ5ew7vygi441VVkXyXjG0tmX6ceeyggdTiBdcWm-Br-uepualfor9QwXRCl-JY02gcfSkN07dvZvGI59B2ayAjc8B3Po0YkjinOfu4lwaey8e9N308DjFaXe-VEcv8mty09-Q0DNmMy4PsMeEj2dWmSx_T7grcgA9SOVsDZsqP2S8Xo8vjvqMkvWFiJObasvzZNd7QQoDPicaMHi9Bou8cZYpqv8S9y5BICtDQJRN1-IXLWImwZ_jwjv_faHD9lIy3m8OUt9_oHsNEmsOYRCFfFymYXGzy7WZ7a4itjIb0nxgmyL3eyYYqCVWqNs-juzG49VAkklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: به نظم پساآمریکایی در خلیج فارس خوش آمدید
سرلشکر پاسدار محسن رضایی:
🔹
شکاف بین ناتوانی آمریکا در بازگشایی تنگه هرمز و ادعای مالکیت آن، از فاصله ۷۰۰۰ مایلی بین واشنگتن و خود تنگه نیز بیشتر است.
🔹
به نظم پساآمریکایی در خلیج فارس خوش آمدید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/akhbarefori/682334" target="_blank">📅 21:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682333">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f2a62fbe1.mp4?token=e5hAPdnsYyj9oS-K0CkQHsYMI2nTRjGtxtCVN-tcextsztxFvnJ4UkEj3XIFaDDLgF2Nze78pzxGZo1xsbT7DiDlwQJQCNv1Tq5cLxkZrIQr4cAADU1CNHI1kdb0Ws2BWQ5z6iMTuixxYcl22rdXF5lJ4LZydDui2a9FmxCmMwJaLQEnEphp0Y1guxSznVWG-f0TOpxfIIwHkSC2whdPqNjHtybTQZq2VRbqKCQO-kjwAyM-0-ydq8pj_i_9LEkUSi82paeTb5C9c8f1mceMejrl7OnT0Trgnejp2IZ0WxgJWLmC7aNb1WpcdPHxVWaE4SaW-ayyghK9eWAitnICsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f2a62fbe1.mp4?token=e5hAPdnsYyj9oS-K0CkQHsYMI2nTRjGtxtCVN-tcextsztxFvnJ4UkEj3XIFaDDLgF2Nze78pzxGZo1xsbT7DiDlwQJQCNv1Tq5cLxkZrIQr4cAADU1CNHI1kdb0Ws2BWQ5z6iMTuixxYcl22rdXF5lJ4LZydDui2a9FmxCmMwJaLQEnEphp0Y1guxSznVWG-f0TOpxfIIwHkSC2whdPqNjHtybTQZq2VRbqKCQO-kjwAyM-0-ydq8pj_i_9LEkUSi82paeTb5C9c8f1mceMejrl7OnT0Trgnejp2IZ0WxgJWLmC7aNb1WpcdPHxVWaE4SaW-ayyghK9eWAitnICsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: جنگ اخیر ثابت کرد آمریکا حتی از پایگاه‌های خودش هم نمی‌تواند دفاع کند  وزیر امور خارجه:
🔹
جنگ‌های اخیر نشان داد کشورهایی که فاقد پایگاه‌های نظامی آمریکا بودند، آسیب کمتری دیدند؛ در حالی که پایگاه‌های خارجی نتوانستند حتی از منافع خود در برابر ضربات…</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/682333" target="_blank">📅 21:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682332">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2cDs4rPY7x2F8UpV1tuW2mzeFYanpQJUPtgRXwPLCxgV5e-fdFeVpJgqwwEuKz2js455JSsxi_mvUtI0mBRBM2WerdT04mV0bSEVXYGShkmzV8Y-R5jq4inU-cv_6um0Yt4VMsFvnipu3jtqHR_osMvx02TYVqcPJ55e1l_NmCdVW-laiUGmEP1TH4EdXYw03gh1-MVJt_4O7idIELCLRTPmsUw6pWjTTs2JJzOmKpiOKmEKvwfbuNNw3BdLi4COZDuLUyCLbbNJHhrnJFY13Gdi3DESgsRuiD0f1sqFbmC4xbl5QgNrMX9x_nzCJ1eYgpehsUQfakJWVDiC-0pLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا استفاده از آمپول‌های لاغری برای شما مناسب است؟!
⚠️
این روزها اسم آمپول‌های لاغری (مثل مونجارو) زیاد به گوش می‌رسد؛ اما این روش درمانی برای همه مناسب نیست و مصرف خودسرانه آن می‌تواند عوارض خطرناکی به همراه داشته باشد!
پرسشنامه زیر توسط جمعی از پزشکان متخصص غدد و تغذیه تهیه شده تا شما با پاسخ به چند سؤال کوتاه در کمتر از یک دقیقه متوجه شوید آیا شرایط استفاده از آمپول‌های لاغری را دارید یا خیر.
🟢
شروع ارزیابی</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/682332" target="_blank">📅 21:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682331">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q84Hagg0444bazWYebO5DYNJuAGX9Va1JYB_Q0U_kxtrpBy61GORkATknyFb9kMvrENoLcB_0LEckwY5sWJfe2l7l8ufD_hmzCsF0aHTEZ1Yk3aRExeX1k9fpfa_DE9vqKCnTF6ViX0AahMBsJVLir9wsXE8d5dE-SNATVADotzjCfEtBb3VYuW6jpl8tDs_Uz-mDrrB5l7W5Yeymw36z4aEx7vBij2Cy0O8qZn7hp4XzY-CII3_qczAQ2hwcDJ3sMamaUseTp_umDts04AJHYgQlnhC7zpoW6Zfcwy7cYZ_RlqJY_1Xb-MVahfHJF5fRk3lGG89cJPdESLrbzOP4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهش ۲۶ درصدی تراکنش‌های «تاپ» در نیلسون ریپورت ۲۰۲۵
🔹
به گزارش روابط عمومی تجارت الکترونیک پارسیان(تاپ)، جدیدترین گزارش نشریه تخصصی و بین‌المللی نیلسون ریپورت (Nilson Report) شماره ۱۳۱۲،  مربوط به عملکرد سال ۲۰۲۵ میلادی منتشر شد.
🔹
آخرین گزارش نشریه معتبر نیلسون ریپورت حکایت از آن دارد که تعداد تراکنش‌های پردازش‌شده توسط تاپ در سال 2025 به ۸.۰۲۷ میلیارد تراکنش رسیده که نسبت به سال 2024، رشد ۲۶ درصدی داشته است.
🔹
بر اساس این گزارش، شرکت تجارت الکترونیک پارسیان با ثبت برجسته‌ترین عملکرد عملیاتی، موفق به صعود به رتبه ۳۸ منطقه خاورمیانه و آفریقا و کسب رتبه سوم در میان شرکت‌های پرداخت الکترونیک (PSP) ایران شده است.
@AkhbareFori
|
Link
:
👈
لینک خبر</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/akhbarefori/682331" target="_blank">📅 21:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682330">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
عراقچی: زمانی‌که آمریکایی‌ها در جنگ درخواست مذاکره کردند، آقای پزشکیان معتقد بود باید به این درخواست‌ها توجه و راهی برای خاتمۀ جنگ از این راه پیدا کنیم
🔹
آقای قالیباف به پیشنهاد رئیس‌جمهور به ریاست تیم مذاکره‌کننده انتخاب شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/akhbarefori/682330" target="_blank">📅 20:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682329">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c6a90c8b3.mp4?token=sJSmRbSHt9KEdKlcAGU1jUZ_givxoZLHucAgIFoZdz7rOJrpj09J1Y6fdSDGDXDtsPCOhchFKWwwexk-DfjuSgFqQLVKIvUkyBQxl4IyY4LLLJClYfC9BVqbgrwnKbDI09otjr_rHlTRhH_1n60x8aKnp4rWzWLyugea6dm4JxReIP9cs14rlZSWxgZvOFb3d0h-FaG4Ex5JW5JXNcbfGvlziMF-bQ8-eDRG5deu6Q74O9Yr7zsHvTw3Jwmz6uJ_aqrKAfiQ94zzSpNsapc5ALkrztwHwJ8HYiDdsgr4gYDTg-hRxhASOtiDnJ1D4wgUUu2x5mPXoq50DQrqF-Ppvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c6a90c8b3.mp4?token=sJSmRbSHt9KEdKlcAGU1jUZ_givxoZLHucAgIFoZdz7rOJrpj09J1Y6fdSDGDXDtsPCOhchFKWwwexk-DfjuSgFqQLVKIvUkyBQxl4IyY4LLLJClYfC9BVqbgrwnKbDI09otjr_rHlTRhH_1n60x8aKnp4rWzWLyugea6dm4JxReIP9cs14rlZSWxgZvOFb3d0h-FaG4Ex5JW5JXNcbfGvlziMF-bQ8-eDRG5deu6Q74O9Yr7zsHvTw3Jwmz6uJ_aqrKAfiQ94zzSpNsapc5ALkrztwHwJ8HYiDdsgr4gYDTg-hRxhASOtiDnJ1D4wgUUu2x5mPXoq50DQrqF-Ppvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول استقلال به نساجی توسط آزادی
🔹
استقلال ۱ _ ۰ نساجی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/682329" target="_blank">📅 20:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682328">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/084c864e2a.mp4?token=XZEdYedPUIGYU-OUsVoSzP4HY8fxTZIH2CdJuzN324z00wWnUs3Q4PxnqNrre6Xnxeyqgby-bfF4liBcwue2birV5YyNnV3yLRZg-fo5BBgGPVQ2Lyavh3Qd9r74l4OCldBIM1EQNGiI-KmlY_XjelN_MWYr1NKljVOmNe4wTprb67nE4Myrmzw7Qvfi1RM42Po_JPKGKXTobD9YdI4asmuBl4MyuyhBq47YrRCTyzQNvBKi4Ta06EKkaYRog6VOjgSnykb2CygBD1tlAoQOrA1xcMImhoNKeW00Qazmft-3i6JOCVmqKLIcEgi6KxsASpWwAZpaI26MAS67rPhIwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/084c864e2a.mp4?token=XZEdYedPUIGYU-OUsVoSzP4HY8fxTZIH2CdJuzN324z00wWnUs3Q4PxnqNrre6Xnxeyqgby-bfF4liBcwue2birV5YyNnV3yLRZg-fo5BBgGPVQ2Lyavh3Qd9r74l4OCldBIM1EQNGiI-KmlY_XjelN_MWYr1NKljVOmNe4wTprb67nE4Myrmzw7Qvfi1RM42Po_JPKGKXTobD9YdI4asmuBl4MyuyhBq47YrRCTyzQNvBKi4Ta06EKkaYRog6VOjgSnykb2CygBD1tlAoQOrA1xcMImhoNKeW00Qazmft-3i6JOCVmqKLIcEgi6KxsASpWwAZpaI26MAS67rPhIwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی، وزیر امور خارجه: رئیس‌جمهور به همه مردم توجه می‌کند نه بخشی از مردم
🔹
دوست و دشمن به اخلاص رئیس‌جمهور اعتراف می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/682328" target="_blank">📅 20:56 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682327">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2238f7d033.mp4?token=MqLW9Hye2SxDx-bweGuT0kdkjILJlp4x_Hh4GFPVkToZDTQvHa3qBSkvcwo3IJtIAwnxdfr-Esl0AK27IwNbBwNYzkpP42cNUleb0QA8QUyvGVYP8JhNubGqdKhlATCrPbbbPg_ZxyBEWuTsh8YOVqtKEW1l2kjRflwLrK73b7UJoWj5rTPUrk7CxpOTSMpzq5FnFezPs-gTaL-Xp_ApXDUCFRERd4wPvYiU2PHpwvSpZfQ6jFLEfuXzj3p_0-B0octSDhFHhE6yTSrEYPYTeMr5LlGqX77AeHnaS2d5qpr0XU8gLE5Gjjb7sciAl8Lanz1pA78UjKg9jGJhLCEnXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2238f7d033.mp4?token=MqLW9Hye2SxDx-bweGuT0kdkjILJlp4x_Hh4GFPVkToZDTQvHa3qBSkvcwo3IJtIAwnxdfr-Esl0AK27IwNbBwNYzkpP42cNUleb0QA8QUyvGVYP8JhNubGqdKhlATCrPbbbPg_ZxyBEWuTsh8YOVqtKEW1l2kjRflwLrK73b7UJoWj5rTPUrk7CxpOTSMpzq5FnFezPs-gTaL-Xp_ApXDUCFRERd4wPvYiU2PHpwvSpZfQ6jFLEfuXzj3p_0-B0octSDhFHhE6yTSrEYPYTeMr5LlGqX77AeHnaS2d5qpr0XU8gLE5Gjjb7sciAl8Lanz1pA78UjKg9jGJhLCEnXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: کُردی صحبت‌کردن رئیس‌جمهور روابط ما با کردستان عراق را تکان اساسی داد
🔹
ارتباط کلامی آقای پزشکیان با رئیس‌جمهور آذربایجان روابط ایران با جمهوری آذربایجان را از این رو به آن رو کرد.
🔹
در جنگ ۴۰ روزه مشکلی پیش آمد که رابطۀ ۲ کشور را تلخ کرد اما یک تماس…</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/682327" target="_blank">📅 20:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682326">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6284525301.mp4?token=f3ek6MIfv1zR7rhkK6IxgFrFHYMqVWixtY0d-U3DJcPai1l6jTgiIZK5GCzH33gYuJlacnDVSWMDqrjjJa_tQx9Kx1pav_zv10wxE_cegGxN5gLJjsY5o6czbJCGo8lZMQTrsXGqjz28RMk8MJ-Kj6BVRzLccdvPZabmQbopS6DSqN_YZsshvYafVmu_cpSCf-aKnVxwgSQ1YCFEI833GxGgKTiyYfPshHI7RMlqT70Iqofe-4PdAVsxJy264cMLN3HvgcgRyaM96-JgwUooa3PllnAk1wKQMYUOMCkWS_Y_3HZ4oN_vblyOd3CMa1hMCR6K96jHDKVzlYhMRT3uhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6284525301.mp4?token=f3ek6MIfv1zR7rhkK6IxgFrFHYMqVWixtY0d-U3DJcPai1l6jTgiIZK5GCzH33gYuJlacnDVSWMDqrjjJa_tQx9Kx1pav_zv10wxE_cegGxN5gLJjsY5o6czbJCGo8lZMQTrsXGqjz28RMk8MJ-Kj6BVRzLccdvPZabmQbopS6DSqN_YZsshvYafVmu_cpSCf-aKnVxwgSQ1YCFEI833GxGgKTiyYfPshHI7RMlqT70Iqofe-4PdAVsxJy264cMLN3HvgcgRyaM96-JgwUooa3PllnAk1wKQMYUOMCkWS_Y_3HZ4oN_vblyOd3CMa1hMCR6K96jHDKVzlYhMRT3uhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر امور خارجه: نگاه کشورهای غرب آسیا به ساختار امنیتی منطقه بعد از جنگ رمضان تغییر کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/682326" target="_blank">📅 20:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682325">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8QQb3h0XAWy647eeYrnqIB9WulT3HLfGQw6dZR7eLXlz5E6mRPxgSeSqqF4TkocGgfBVD5HOoxG14GwnMkMz3vQJ_kfKjJBLKL7J9eBwf6uYt-8GQGpejQYOIWump9f5m-A3G_ZHF2qR9ZKpPSSTOu6APnC31fDf8PTKy60FGEaBmy17DyJInwMD1s4RFFRPHsIFW_eqyaNdQovjCmwvSyEm2F4eWm-pqmUB5Q9d0W8xCrkSwZ6zxKlRaYFWIQWz2iVRWM6-nmXxN5cIXKRXWG9IdrbHcuOrNaCobrvAKiDl0_q1GdJRaERKa9YY21TjfVSCVKDIuVZXm4ep-GqXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: آمریکایی‌ها خیال می‌کنند با فشار بیشتر بر ایران می‌توانند امتیازاتی بگیرند که اصلاً بخشی از توافق نبوده است
🔹
وزیر خزانه‌داری و وزیر جنگ آمریکا در حد و اندازهٔ این کارها نیستند.
🔹
منتظر نباشید که این تیم دلقک‌ها خرگوشی از کلاهشان بیرون بکشند و گندی که زده‌اید را پاک کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/682325" target="_blank">📅 20:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682324">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54e9d06f8f.mp4?token=Eaaqoc9H5jDqcDM-jW8iyPZWvXV-rfI30IuDMBbp0zb0I3di_OcKOSbDw6M7tIsGfSgzJUcrPXRYUl1vzWQoKBbz8Ry-QtAeyULiFnfdDZPG4pwnb-R8xFXhCtBBF0Se71DPE735BZyV6pxnS9LFUInQmFpaSY6zSv7pm8tv7QXGxPKAl-C3Sz1DSE1VJfKHBY8X5UwRYu0cTqFSvRSFWczfm58QiKPINyVRNsezH0IRvTMNowGGvcOMIC2yApbS_lbMkalnsss8p3rtAIanr0PFuXcHbuzCjR89Bl-wujloqvBCQCMYly-SMif-COwT83aiJ2MPEz_EWeHiGF4YIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54e9d06f8f.mp4?token=Eaaqoc9H5jDqcDM-jW8iyPZWvXV-rfI30IuDMBbp0zb0I3di_OcKOSbDw6M7tIsGfSgzJUcrPXRYUl1vzWQoKBbz8Ry-QtAeyULiFnfdDZPG4pwnb-R8xFXhCtBBF0Se71DPE735BZyV6pxnS9LFUInQmFpaSY6zSv7pm8tv7QXGxPKAl-C3Sz1DSE1VJfKHBY8X5UwRYu0cTqFSvRSFWczfm58QiKPINyVRNsezH0IRvTMNowGGvcOMIC2yApbS_lbMkalnsss8p3rtAIanr0PFuXcHbuzCjR89Bl-wujloqvBCQCMYly-SMif-COwT83aiJ2MPEz_EWeHiGF4YIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: به میانجی‌ها گفتیم آتش‌بس را قبول نمی‌کنیم، باید جنگ خاتمه یابد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/682324" target="_blank">📅 20:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682323">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c79df0400.mp4?token=Mj2kPQtAYKLsB0xXyi1EVlTR9FpH2JV5wUt9YFKlisC9FfaIPJWYotmxm6ZcYfNA6-YCqhbON8dQ811RV1OLyrPtL4Dreh1HYUob8IeCGXQc-Mjx-QJEarV8pRBJ8G0uqdaEcQ5XnbeBmdd7B5tQ7PnPamkWYmg1A06jP5mF2jTKF_VLpPIEazZb2kBUrihzbxNKMCcgbPZPKmWOg2q6kS-mY4BIgpcMDPM-fehPHaAx6T7DxJkoM3xR0caDVXP-FpNMr9wozYU45q1ZlEV-kNFQUBvTQI3_Bu9ef24rN1Ar7kmYRjNPLU5az3vnGa0CniXvrvB5m2vcKojcqc4hzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c79df0400.mp4?token=Mj2kPQtAYKLsB0xXyi1EVlTR9FpH2JV5wUt9YFKlisC9FfaIPJWYotmxm6ZcYfNA6-YCqhbON8dQ811RV1OLyrPtL4Dreh1HYUob8IeCGXQc-Mjx-QJEarV8pRBJ8G0uqdaEcQ5XnbeBmdd7B5tQ7PnPamkWYmg1A06jP5mF2jTKF_VLpPIEazZb2kBUrihzbxNKMCcgbPZPKmWOg2q6kS-mY4BIgpcMDPM-fehPHaAx6T7DxJkoM3xR0caDVXP-FpNMr9wozYU45q1ZlEV-kNFQUBvTQI3_Bu9ef24rN1Ar7kmYRjNPLU5az3vnGa0CniXvrvB5m2vcKojcqc4hzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر امور خارجه درباره عملکرد دو ساله: رئیس‌جمهور با یک تماس تلفنی با الهام علی‌اف، فصل جدیدی در روابط ایران و آذربایجان رقم زد‌
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/682323" target="_blank">📅 20:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682322">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4d25c1842.mp4?token=nytIha7Iga4_NkyFaMd-b3lUOJ9LoIGG-nKwSPakEQbO0l3GSqB9lACpHamVB3G8L1ftQrtURcTf8bqesYQT0kctcJa_uhfZhmCY5vJc64MksvZJMBMy-83L_aMB-AnHTuO2gnHUGi8L7mr6ZQiklbwvzts7C9xEUsG7FFJW7Jnrcz0JgNw6e8lAGiKQzrAKIiLsJTBmwoJif-PS5PCz1J9usfkR2VqqzbqV-LQL5o1GLt3Ayt0bR0PrKKodXk8DPDdc3bPT1avNIYomURBY37aTwCV6mwdR3U0D2s-5ewKodedEMumKsqi0f2HsEZxjtqO3F7V6vxq7CPMpSGTdJpLYtjwUfGAydOqmUPYMJZuREErnG1APvOUww_JCxFTxxAkSjPK6k-IGkSJLtYVKggN4m__ZacHQDP-RY522YpAECCq3a54C3KR9HisR3k3mioV40l_Tu_WeiginlYYvAulSxlOhFpVp5sRYKUPH2ymgJeJiWv6X6p86ZPN9x4pc9h1kkjtiSovxxsjExzpDXODl6VrLGtPCNfwbgoNr828wA6gGVBCJCkQK5ct3lbyjxAGfek8V-wW3LxzHA-c9He4zsOal5AUPnyyzdCvLx9tKXxaj_BkAOuhMKgKGlryniXPZCeWqsSBFze9QcjPBdZQfGUcg8xtsPHkshtVdkH4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4d25c1842.mp4?token=nytIha7Iga4_NkyFaMd-b3lUOJ9LoIGG-nKwSPakEQbO0l3GSqB9lACpHamVB3G8L1ftQrtURcTf8bqesYQT0kctcJa_uhfZhmCY5vJc64MksvZJMBMy-83L_aMB-AnHTuO2gnHUGi8L7mr6ZQiklbwvzts7C9xEUsG7FFJW7Jnrcz0JgNw6e8lAGiKQzrAKIiLsJTBmwoJif-PS5PCz1J9usfkR2VqqzbqV-LQL5o1GLt3Ayt0bR0PrKKodXk8DPDdc3bPT1avNIYomURBY37aTwCV6mwdR3U0D2s-5ewKodedEMumKsqi0f2HsEZxjtqO3F7V6vxq7CPMpSGTdJpLYtjwUfGAydOqmUPYMJZuREErnG1APvOUww_JCxFTxxAkSjPK6k-IGkSJLtYVKggN4m__ZacHQDP-RY522YpAECCq3a54C3KR9HisR3k3mioV40l_Tu_WeiginlYYvAulSxlOhFpVp5sRYKUPH2ymgJeJiWv6X6p86ZPN9x4pc9h1kkjtiSovxxsjExzpDXODl6VrLGtPCNfwbgoNr828wA6gGVBCJCkQK5ct3lbyjxAGfek8V-wW3LxzHA-c9He4zsOal5AUPnyyzdCvLx9tKXxaj_BkAOuhMKgKGlryniXPZCeWqsSBFze9QcjPBdZQfGUcg8xtsPHkshtVdkH4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقتصاد، ما را از انقلاب و رهبرمون جدا نمی‌کنه؛ خداروشکر زندگی‌مون می‌چرخه و امیدواریم مشکلات اقتصادی هم برطرف بشه/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/682322" target="_blank">📅 20:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682321">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
حقوق ۲۵ میلیونی با هزینه ۹۰ میلیونی | نبرد در ریاضتِ بقا | چند درصد مردم درآمد ۹۰ میلیونی دارند؟
🔹
محاسبات تازه درباره هزینه‌های زندگی خانوارهای کارگری نشان می‌دهد که سبد معیشت یک خانواده متوسط ۳.۳ نفره در پایان تیرماه به حدود ۹۰ میلیون تومان رسیده است؛ رقمی که فاصله آن با دستمزد رسمی کارگران، تصویری روشن از تشدید بحران معیشت در ایران ارائه می‌دهد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3238688</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/682321" target="_blank">📅 20:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682320">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8e6cfe160.mp4?token=umbocC-fSAR9SHhPc02rmqrouxB_5kDwiMvlOXQ1kXMIPOkHAux3xoR_TV5fH9_VS1SWD_EGVxCAcAaD86oVIw7eZ7Ud2QXrN44OCRdxkh1ZGyEKMUWfcZgF4aWd8HFVUiCW_cxeNT98O811Tm2hwEQtnfMliMpYlF9q2QC1o7Y4c_dnFJfq04U3SHd22TTv0rTfmvWXs971ZE1mHWhdLqwzXTX4Qx0MvHP35jcNt79o6F8UhCmrGhPuKb5sZZq-9W3FBFGLly46i3kJzYtXp2BlrV6UINnTyJ91lnBdTCXhnjLOgMS9nJsA6s4qIWvT0zCCESQ-WJJthIll8piMdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8e6cfe160.mp4?token=umbocC-fSAR9SHhPc02rmqrouxB_5kDwiMvlOXQ1kXMIPOkHAux3xoR_TV5fH9_VS1SWD_EGVxCAcAaD86oVIw7eZ7Ud2QXrN44OCRdxkh1ZGyEKMUWfcZgF4aWd8HFVUiCW_cxeNT98O811Tm2hwEQtnfMliMpYlF9q2QC1o7Y4c_dnFJfq04U3SHd22TTv0rTfmvWXs971ZE1mHWhdLqwzXTX4Qx0MvHP35jcNt79o6F8UhCmrGhPuKb5sZZq-9W3FBFGLly46i3kJzYtXp2BlrV6UINnTyJ91lnBdTCXhnjLOgMS9nJsA6s4qIWvT0zCCESQ-WJJthIll8piMdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر امور خارجه درباره عملکرد دو ساله: دیپلماسی استانی مکمل دیپلماسی همسایگی است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/682320" target="_blank">📅 20:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682319">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
هشدار صنعاء نسبت به توطئه جدید عربستان و آمریکا در عراق
🔹
وزارت خارجه یمن در بیانیه‌ای رسمی، رژیم سعودی را به تلاش عامل دامن زدن به اختلافات داخلی و ایجاد فتنه در عراق با استفاده از پوشش حمایتی آمریکا دانست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/682319" target="_blank">📅 20:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682318">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a321fc3a.mp4?token=syeYUqFgvev3Ip9KhRWNVqxcemYO3XZHqrrsD6gXeoDslgVuEyr21CL8LidfcrSNjYX9GgeowVaZ5A1pi1-otuR4mMCWx2fMJMrd5C1-1XvvM0kIJ-gmO0cDMgd90b437VbKjHyEv3D33hHyhJq3HhLzZ-HqAPlk1vdLjP2Kd_OiLxSJfUNvw3EKrSYePRraPxASMRW4z1X57UkAaDFNjhfs5tFjg_p9m29ag9RtseJlrc9eUgoldBp2LnKkQWzT6qnaQcA0SG0sHegMLCaiYOl-v0h7bMSk8EJpRa54C0LQ9dlITKVDsX0Nj3CY3ootxr3Gzx-pec_adhd1plweYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a321fc3a.mp4?token=syeYUqFgvev3Ip9KhRWNVqxcemYO3XZHqrrsD6gXeoDslgVuEyr21CL8LidfcrSNjYX9GgeowVaZ5A1pi1-otuR4mMCWx2fMJMrd5C1-1XvvM0kIJ-gmO0cDMgd90b437VbKjHyEv3D33hHyhJq3HhLzZ-HqAPlk1vdLjP2Kd_OiLxSJfUNvw3EKrSYePRraPxASMRW4z1X57UkAaDFNjhfs5tFjg_p9m29ag9RtseJlrc9eUgoldBp2LnKkQWzT6qnaQcA0SG0sHegMLCaiYOl-v0h7bMSk8EJpRa54C0LQ9dlITKVDsX0Nj3CY3ootxr3Gzx-pec_adhd1plweYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتحاد و همبستگی رمز ایستادگیه، ما نسل قدیم شاید دیگه توان گذشته رو نداشته باشیم، اما جوانان امروز دارن پای کار می‌ایستن/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/682318" target="_blank">📅 20:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682317">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
حمله مزدوران سعودی به مناطقی از استان تعز یمن
🔹
گزارش‌ها از استان تعز حاکی از آن است که عصر امروز، مزدوران وابسته به عربستان سعودی بخش‌هایی از این استان را هدف حملات موشکی قرار داده‌اند.
🔹
منطقه «الاکمه» در بخش «مقبنه» استان تعز، هدف چندین فروند موشک کاتیوشا قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/682317" target="_blank">📅 20:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682316">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ecd41f5ec.mp4?token=VsXQ9ibGtvemY9puUcYYHMp1xVAhUfbxejPW2VXN-DeOTQT0KzsJ74os6YtmwwdJgjdXKKetxKpXgypzKFUVEfYGng5ehML1UwXZfPPDgr0coNqkF5DWZz3BdA_HVLVAeynYpPQY-XkSIbRn1wg2llsa0G8yBcDyBzv5nIRTRx4ETzh_W4k5AGDuv4wwcGBW9bkicjwkXh_jwYeUTYbHSkbtBSFakJvPBVSiQ7_OeMCw0CdONPkMwwkT6QcFJjjb5QZDpvoospJmpoMYIJAnkEZZz7U0Ep-1wWyi06XCIvnWeWNnjSOOfyI2CsEYCrqCt3ZWqZgKOF1pSetcFf6N-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ecd41f5ec.mp4?token=VsXQ9ibGtvemY9puUcYYHMp1xVAhUfbxejPW2VXN-DeOTQT0KzsJ74os6YtmwwdJgjdXKKetxKpXgypzKFUVEfYGng5ehML1UwXZfPPDgr0coNqkF5DWZz3BdA_HVLVAeynYpPQY-XkSIbRn1wg2llsa0G8yBcDyBzv5nIRTRx4ETzh_W4k5AGDuv4wwcGBW9bkicjwkXh_jwYeUTYbHSkbtBSFakJvPBVSiQ7_OeMCw0CdONPkMwwkT6QcFJjjb5QZDpvoospJmpoMYIJAnkEZZz7U0Ep-1wWyi06XCIvnWeWNnjSOOfyI2CsEYCrqCt3ZWqZgKOF1pSetcFf6N-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار و آتش‌سوزی گسترده در یک کارخانه فنلاندی «استورا انسو»، نزدیک مرز روسیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/682316" target="_blank">📅 20:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682314">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
یک جانباز ۵۰ درصد در گفتگو با خبرنگار خبرفوری از آرزویش برای شفاعت در آخرت گفت و در ادامه، از مسئولان خواست بیشتر صدای مردم را بشنوند/
خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/682314" target="_blank">📅 20:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682313">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
اخبار تائید نشده از شلیک چند فروند موشک از سوی نیروهای مسلح یمن خبر می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/682313" target="_blank">📅 20:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682312">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
گلف‌نیوز: ایران دو ملوان مصری را آزاد کرد
ادعای گلف‌نیوز:
🔹
دو ملوان مصری که از ماه ژانویه در بندرعباس و در داخل کشتی «ریم البحار» بازداشت شده بودند، آزاد و مجوز بازگشت به کشورشان را دریافت کرده‌اند.
🔹
رئیس دفتر حفاظت منافع مصر در تهران، پیش از عزیمت ملوانان از ایران به قاهره، شخصاً با آنها ملاقات کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/682312" target="_blank">📅 20:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682311">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d1d447e4a.mp4?token=l6gyeA3nlATVMeoHyx8F_D_t7kEAtbZF4bXOmEm5GLal4Sq_LhghFzdTN2dYMAd1Gi0jkwWiY4lg4LjQzdOVq0D2FvQM7lwPfVCzC4W00utqTT9BF1BiLxY1A5tnCGZSBzmm24ihRAOtK2dG2kdAJDZJWANQAOKT8zK2DUtkhYk4K2HUOLUZTGg7WJQGvSimt_E7zKzwbKURnDL_46z-V-Bj2ni0IODVxlbr-OabPDGIIM68Ic0Jfkz9kilkRAwhhJRyXitxTeiQfmaD6UCDTujQSlYIcu1IUvPE_qiVGgKVgvMuIFIgL5QgNCbjOZBQ3qSJVOUwhu2uYXTX3ysXIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d1d447e4a.mp4?token=l6gyeA3nlATVMeoHyx8F_D_t7kEAtbZF4bXOmEm5GLal4Sq_LhghFzdTN2dYMAd1Gi0jkwWiY4lg4LjQzdOVq0D2FvQM7lwPfVCzC4W00utqTT9BF1BiLxY1A5tnCGZSBzmm24ihRAOtK2dG2kdAJDZJWANQAOKT8zK2DUtkhYk4K2HUOLUZTGg7WJQGvSimt_E7zKzwbKURnDL_46z-V-Bj2ni0IODVxlbr-OabPDGIIM68Ic0Jfkz9kilkRAwhhJRyXitxTeiQfmaD6UCDTujQSlYIcu1IUvPE_qiVGgKVgvMuIFIgL5QgNCbjOZBQ3qSJVOUwhu2uYXTX3ysXIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر امور خارجه درباره عملکرد دو ساله: دیپلماسی استانی مکمل دیپلماسی همسایگی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/682311" target="_blank">📅 20:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682310">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بازنشسته‌ها و حق‌التدریس‌ها کمبود معلم امسال را جبران می‌کنند
مصطفی آذرکیش، معاون آموزش متوسطه وزارت آموزش و پرورش در
#گفتگو
با خبرفوری:
🔹
امسال کسری نیروی انسانی آموزش‌وپرورش با استفاده از ظرفیت فارغ‌التحصیلان دانشگاه فرهنگیان و شهید رجایی، حق‌التدریس شاغلان، بازنشستگان و پیشکسوتان و همچنین سربازمعلمان جبران شده است.
🔹
برنامه‌ریزی برای سال تحصیلی جدید به‌ گونه‌ای انجام شده که مهر امسال، کلاس‌ها با حضور معلم در تمام پایه‌ها آغاز شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/682310" target="_blank">📅 20:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682309">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029e3f4ae2.mp4?token=lWbahzFeob--xH5bCdYxOJZ_KdVeEghgEkzy8rDRcyXYNACsdzHTxeCSm6yKo9Tt5WITaXdSQc8pgPlBQRGUSOZGW8OSW5ilPYpYhaN-UXd2v7v3JjFc6zW2wyDzkxrdSraL1s6t2tR4t-Q1fhIzZ8ZJR7yQojuNtq8nOg122etu3A-zonO5kj5eCJHQeZAHgAnEXSLxV5KBJPQANYfmsEa4s2t2p-Wu80wKqr5s-iZJYA5A7xRAWj0kdKNfPaafrGZfQMWjwVAgOVGdpiakgQd927ThTqwUHwaxvucd_4U7wGK-VwMWJq_ycRdFTKCg6n1oncgyBL1TslJqcDylQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029e3f4ae2.mp4?token=lWbahzFeob--xH5bCdYxOJZ_KdVeEghgEkzy8rDRcyXYNACsdzHTxeCSm6yKo9Tt5WITaXdSQc8pgPlBQRGUSOZGW8OSW5ilPYpYhaN-UXd2v7v3JjFc6zW2wyDzkxrdSraL1s6t2tR4t-Q1fhIzZ8ZJR7yQojuNtq8nOg122etu3A-zonO5kj5eCJHQeZAHgAnEXSLxV5KBJPQANYfmsEa4s2t2p-Wu80wKqr5s-iZJYA5A7xRAWj0kdKNfPaafrGZfQMWjwVAgOVGdpiakgQd927ThTqwUHwaxvucd_4U7wGK-VwMWJq_ycRdFTKCg6n1oncgyBL1TslJqcDylQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلامت موهایت را با یک لیوان آب بسنج! #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/682309" target="_blank">📅 20:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682308">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای وزارت دفاع امارات: دو موشک بالستیک از ایران شلیک شده را شناسایی کردیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/682308" target="_blank">📅 20:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682307">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc0f1428f.mp4?token=KIAUQ767CYQoqacvWKGXWSZghxyYRcwWFZ7Cg9DgahuBBZyqeW-ye61RNOGxKUvOPFHWv23U2WGq_wPwFIOT4HtW0zbNp9zsmXYNFOoFmpKhov1QFxXCKwLX4skd1YSppgqMOotcry8eGteMlW6zVWSc8LukZisL-w8wxigMzB-kbhsCqs128PElghqN7ZynwRmPIA8BTYRXnWOBLVOmZFiq8oYEDcqn6i_vOGg_47Uqr8JhxpccV8FDrgKR9fpr-foDT8RBg3qgOhyCa1-ar_riNY1RpnZVKTfyDhUKKVD8Gi2pMtLyGH3kw0W6_ONb2LBTDmhnTmDb0OGllp6B0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc0f1428f.mp4?token=KIAUQ767CYQoqacvWKGXWSZghxyYRcwWFZ7Cg9DgahuBBZyqeW-ye61RNOGxKUvOPFHWv23U2WGq_wPwFIOT4HtW0zbNp9zsmXYNFOoFmpKhov1QFxXCKwLX4skd1YSppgqMOotcry8eGteMlW6zVWSc8LukZisL-w8wxigMzB-kbhsCqs128PElghqN7ZynwRmPIA8BTYRXnWOBLVOmZFiq8oYEDcqn6i_vOGg_47Uqr8JhxpccV8FDrgKR9fpr-foDT8RBg3qgOhyCa1-ar_riNY1RpnZVKTfyDhUKKVD8Gi2pMtLyGH3kw0W6_ONb2LBTDmhnTmDb0OGllp6B0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: بودجه داریم اما در اولویت‌بندی دقت نمی‌کنیم  رئیس مجلس در جلسه علنی امروز مجلس:
🔹
دو موضوع کالابرگ و بحث نیروهای مسلح، موضوعات مهم و فوری ماست و باید به نحوی پیگیری کنیم که خدشه به آن وارد نشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/682307" target="_blank">📅 20:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682305">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeTvtu-kHSBzGEveBcIMQaJtTLk8We5S-eS12bLHrGRuCDMEGZOs04ssLlo8opf9zl4huHFHrv72Hb7uDMh4WPMZCC9MwpAbA260ja6HZzDK6qo_vISsqbGL_uV3K7YxHOPNxFhRTuz93Au8HlJ9CPzf01p4MYeWujZ5hEOcBHWZ-9pqDWGfpVOULkwIfzoW-2Hd0WSxT7fmQi-WixMxnNdgF_KamMBz0bjM0Y41RG9n_uhRi3u-Z0XOd2vnWvXjMYkKFq3yrmcpMTuBAJn5BvE3peFbOknk3ho15Uy0DTrnZWoY5J5c8Lk112W5ZuwquCh-2GckqkfAQ-8_LoBn5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولوریتا(
®️
Velorita) چه تاثیری روی کبد چرب و قند خون داره؟
داروی
سماگلوتاید (Semaglutide)
تولید
کشور کانادا
با نام تجاری ولوریتا تولید شد.
ولوریتا می‌تونه علاوه بر کمک به
کنترل قند خون
، در روند
بهبود کبد چرب
هم نقش داشته باشه. این دارو با اثر روی اشتها و کاهش دریافت غذا، می‌تونه به کاهش وزن کمک کنه.
🟡
مصرف این دارو باید زیر نظر پزشک انجام شود. از مصرف خودسرانه پرهیز کنید.
@allaboutobesity</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/682305" target="_blank">📅 20:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682304">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68d1b7f113.mp4?token=WsMtQ69LanFDaO7xYlVNpsrSYumI45Z6WSTC_aOPjCmuoaq-pscSgRP1ntvaa-Zn5lN9VitZ8piSfcjoUk_Wjycf1RGz5lcRIIa6aAlprZAUct8eIremp9K_zSUjCbZ3Lu7BKQbj8807zohjeYeB1IAotXXe0ruLl4IuKSUpm1XRm1P6gybxegssxT8uIVzdQM-D1oKXwF0YB5-AMr9iHMRZ2fgCtzTpDtCtodnD-uiXs_lyZHtObGj7lRJm4OKOZIvl_ppzsY2K4cY-o5J4iW6UFmomv5Ox7mnGOuHW6WvgF8yBCx91nzPcUK0uZVhgA_ppptF6QrUH_rL-fy_XPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68d1b7f113.mp4?token=WsMtQ69LanFDaO7xYlVNpsrSYumI45Z6WSTC_aOPjCmuoaq-pscSgRP1ntvaa-Zn5lN9VitZ8piSfcjoUk_Wjycf1RGz5lcRIIa6aAlprZAUct8eIremp9K_zSUjCbZ3Lu7BKQbj8807zohjeYeB1IAotXXe0ruLl4IuKSUpm1XRm1P6gybxegssxT8uIVzdQM-D1oKXwF0YB5-AMr9iHMRZ2fgCtzTpDtCtodnD-uiXs_lyZHtObGj7lRJm4OKOZIvl_ppzsY2K4cY-o5J4iW6UFmomv5Ox7mnGOuHW6WvgF8yBCx91nzPcUK0uZVhgA_ppptF6QrUH_rL-fy_XPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: اطلاعات خوب و دقیقی نسبت به تراستی‌ها داریم و باید در این موضوع نظم حاکم کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/682304" target="_blank">📅 20:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682303">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d6cc303f.mp4?token=toiFjGEGVhWehcpDQRKyU1DD-Pu7ev5h1LIsL6OzdSHIn59hDZ_Q_muqa-kTo54-Y4IxGaXTAWG9RCr4V8yIlalRgZOMmMA8e_OM2FEyRmZynxNFFRWgEtTN_wJCf_-R2mTzWnyqtmGN447JBYB21VkRAFO1K6BEfvXUxhbJrm1SQXQFW35f2y1yXaUGycANEfddu9F3Dud0HBsQ7FkQYqa678uG07zl9_bdBQzMPfMr2pOIgDM9mExqy4mBDsJArPn05nKs5M1AwVwv09GYCcwxP9N2VD6reV_Knc0DjIhX2ebt6Xje_V4m0Dn9iNQHln834sbQzINhyp9Y4hbLaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d6cc303f.mp4?token=toiFjGEGVhWehcpDQRKyU1DD-Pu7ev5h1LIsL6OzdSHIn59hDZ_Q_muqa-kTo54-Y4IxGaXTAWG9RCr4V8yIlalRgZOMmMA8e_OM2FEyRmZynxNFFRWgEtTN_wJCf_-R2mTzWnyqtmGN447JBYB21VkRAFO1K6BEfvXUxhbJrm1SQXQFW35f2y1yXaUGycANEfddu9F3Dud0HBsQ7FkQYqa678uG07zl9_bdBQzMPfMr2pOIgDM9mExqy4mBDsJArPn05nKs5M1AwVwv09GYCcwxP9N2VD6reV_Knc0DjIhX2ebt6Xje_V4m0Dn9iNQHln834sbQzINhyp9Y4hbLaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: ۲ موضوع کالابرگ و بحث نیروهای مسلح، موضوعات مهم و فوری ماست و باید به نحوی پیگیری کنیم که خدشه به آن‌ها وارد نشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/682303" target="_blank">📅 19:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682302">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024c1f2502.mp4?token=rtSojlAiGipo_STx-H86RcdU1fbWVq3FusdBWasKA7NbhotwTQW_s7veQheVuk-WNFqrdVJ6Nqb-VkETlfpmQcW4eBnbPW6FeYnVJNTA8Tali4SsCZs2hjy2rHjN45j8nMK5CmDxt0Afb4TtepLVqr-DLCfwrTYQmO53NZsT44Kpt4qZnf4pgxcgRyPIQXflZPcHglPCCxNAeYOfYqwn6BMityVDg-hEjc9c7bBv-S_tWG-u1QTW2f1DFKkM9gtsDuhGnfPtSUGvI6KF-V11jQOZlsCgTFnR7hQxNVYv5rSCLy4TEDHphLWRhKe0vFJopmr6jvb_2ouXDCutMWfJ1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024c1f2502.mp4?token=rtSojlAiGipo_STx-H86RcdU1fbWVq3FusdBWasKA7NbhotwTQW_s7veQheVuk-WNFqrdVJ6Nqb-VkETlfpmQcW4eBnbPW6FeYnVJNTA8Tali4SsCZs2hjy2rHjN45j8nMK5CmDxt0Afb4TtepLVqr-DLCfwrTYQmO53NZsT44Kpt4qZnf4pgxcgRyPIQXflZPcHglPCCxNAeYOfYqwn6BMityVDg-hEjc9c7bBv-S_tWG-u1QTW2f1DFKkM9gtsDuhGnfPtSUGvI6KF-V11jQOZlsCgTFnR7hQxNVYv5rSCLy4TEDHphLWRhKe0vFJopmr6jvb_2ouXDCutMWfJ1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: قول می‌دهیم به اجرای کالابرگ خدشه وارد نشود
🔹
در نیمۀ دوم سال هم باید به افرادی که بیشتر نیاز دارند، با اولویت‌بندی پلکانی بيشتر کمک کنیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/682302" target="_blank">📅 19:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682301">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c30e01754.mp4?token=u-dIhcYrx5t3v8cJwLNtLrOQXxhEr9frcXwHyK5kh9qqLoqEyoB7iTS3fOn1-ETghBCzs1VJ6rcfP_cW_8rAR5VRPEI34jbuhC3o4G0qK6doL4JgWce_Q7WpbaR-pcq96kdTNgAyoxsvNISlKzswHSjSgpBGjVLWXnyzCsP7dDuKnqxYWwDQuhgTE2_CxIc-I44XMHtc9mpXu9YqlAvhKXvIppPXLhUSeRCw3d6ueqWfqYtesel9NFmPjLaF5JH_lZ8z0qfaRS1tXH0CIukG1FQ8M0-Nglwi6dmbDG2fgIKpa2RMIUBmLs2LZbdCyECLdF0y9SINVef0kptJdl4IeYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c30e01754.mp4?token=u-dIhcYrx5t3v8cJwLNtLrOQXxhEr9frcXwHyK5kh9qqLoqEyoB7iTS3fOn1-ETghBCzs1VJ6rcfP_cW_8rAR5VRPEI34jbuhC3o4G0qK6doL4JgWce_Q7WpbaR-pcq96kdTNgAyoxsvNISlKzswHSjSgpBGjVLWXnyzCsP7dDuKnqxYWwDQuhgTE2_CxIc-I44XMHtc9mpXu9YqlAvhKXvIppPXLhUSeRCw3d6ueqWfqYtesel9NFmPjLaF5JH_lZ8z0qfaRS1tXH0CIukG1FQ8M0-Nglwi6dmbDG2fgIKpa2RMIUBmLs2LZbdCyECLdF0y9SINVef0kptJdl4IeYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما اینجا هستیم که بگیم تنهاش نمی‌ذاریم؛ در رکاب رهبری هستیم و تا آخر ایستاده‌ایم. این ملت و مردم ایران همیشه سرافراز و سربلند می‌مونن
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/682301" target="_blank">📅 19:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682300">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc70156c4f.mp4?token=BLLajwNbOVWRut1CPXEpVPiH-SCwIpWbvdUIke-VZyR7pygMKHn1pN1e08ULskyeEeD1hF75mnYiXCNqDiWJxDlh4QJfWXWvD5m8oOVYh8zHR4Cy5GxbTZewp62vh0xvJ2fnHtV1coXUM0IA3XkI3AN4j2PL-5dwaT64ORi49ruzPbywQhs3pFcp0zB6IfZ0rA-YlJxu5G9iZn3e2tpBB6odpAc0et3wAprCkRthTRBk4speP347X_cK8qqA_q4hoYUYkYM43_u2VRIsiqIC5Xb75OmRNjwtG7KAL8UCppLqT5PdvkxKghTcd32r7zcYj8_4iQHPnENz4KZGEe7Byw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc70156c4f.mp4?token=BLLajwNbOVWRut1CPXEpVPiH-SCwIpWbvdUIke-VZyR7pygMKHn1pN1e08ULskyeEeD1hF75mnYiXCNqDiWJxDlh4QJfWXWvD5m8oOVYh8zHR4Cy5GxbTZewp62vh0xvJ2fnHtV1coXUM0IA3XkI3AN4j2PL-5dwaT64ORi49ruzPbywQhs3pFcp0zB6IfZ0rA-YlJxu5G9iZn3e2tpBB6odpAc0et3wAprCkRthTRBk4speP347X_cK8qqA_q4hoYUYkYM43_u2VRIsiqIC5Xb75OmRNjwtG7KAL8UCppLqT5PdvkxKghTcd32r7zcYj8_4iQHPnENz4KZGEe7Byw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: قول می‌دهیم به اجرای کالابرگ خدشه وارد نشود
🔹
در نیمۀ دوم سال هم باید به افرادی که بیشتر نیاز دارند، با اولویت‌بندی پلکانی بيشتر کمک کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/682300" target="_blank">📅 19:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682298">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63deccee4.mp4?token=R0TDFMWIpMWf7kmWyN-d1NzdHw2pNw6VpQzwgkm1OnmlhLaeBeyOYxOaNdf8--VR8BW2sAXTUfzitqD1k2myScCWSaAp9WfLatQB0gDxTDq12t4mpYq4V3qyowF-hYNSA_c_Qr0ihzVXPkLisQCVoqbUJ4UbvlTW6rFq4PARQyomGdUUigODA44pSxmGdxFLXpkBtmg4XsAQlaGwCH7Oz5PqWXYIlIKZzrCQ6cNWGJm1zdEV5Y663hgZluzslh77u3_BUiHgP-VFWVGyhtcSnd6Dxgf3lyLSKb7RshMQNypvDzPXHYBC9-U_252drEhoa67K6226UrvJdcxxMZ8KBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63deccee4.mp4?token=R0TDFMWIpMWf7kmWyN-d1NzdHw2pNw6VpQzwgkm1OnmlhLaeBeyOYxOaNdf8--VR8BW2sAXTUfzitqD1k2myScCWSaAp9WfLatQB0gDxTDq12t4mpYq4V3qyowF-hYNSA_c_Qr0ihzVXPkLisQCVoqbUJ4UbvlTW6rFq4PARQyomGdUUigODA44pSxmGdxFLXpkBtmg4XsAQlaGwCH7Oz5PqWXYIlIKZzrCQ6cNWGJm1zdEV5Y663hgZluzslh77u3_BUiHgP-VFWVGyhtcSnd6Dxgf3lyLSKb7RshMQNypvDzPXHYBC9-U_252drEhoa67K6226UrvJdcxxMZ8KBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخاستن ستون‌های دود با منشا نامشخص در سلیمانیه واقع در کردستان عراق
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/682298" target="_blank">📅 19:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682297">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
جنگ ایران چرا به نفع کشورهای خلیج فارس نیست؟
🔹
جنگ ایران اگرچه می‌تواند قیمت نفت را بالا ببرد، اما همزمان هزینه تأمین مالی کشورهای عربی خلیج فارس را افزایش داده است.
🔹
پس از آغاز جنگ، صرف ریسک اوراق بدهی این کشورها از حدود ۲.۶ درصد به بیش از ۴ درصد رسیده؛ یعنی دولت‌هایی مانند عربستان برای استقراض باید سود بیشتری به سرمایه‌گذاران بپردازند.
🔹
برای اقتصادهایی که میلیاردها دلار پروژه توسعه‌ای را با انتشار اوراق تأمین مالی می‌کنند، این افزایش هزینه سنگین است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/682297" target="_blank">📅 19:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682295">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUgO0ZRjGuUUN_dkg_ZojWCFkj7kbfw-2pZT6J4NE8bL5HGmyxDGJXvRJuj3MU2P8OkHG61QWHR2m1BPU_8QtXgfk5XymyFZtIzL8X87PffO7hp3sUkp8Lu2yEd7CPIE0TLmyKxGoC6yN5SF4FdJXYmgAGSyjD8gVNr1CaZsTry5-x1XGancSPP5L-eMCK_ViMWu9B9MCwmDA4qiriJUBtrlUnwOO-0givOsCEa14FCljVsNsBYvPgvUV9ctv4NgwoFcDGPENO2unTzE-aBDpcui665gct3zh2M2S88UNwcjIeLTgG6O6m8ZP5FRXZLG0VyB_BYNdcB7dPOrVXAtRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07a0c49ace.mp4?token=aBh3TUrnXLCvxpwHjK-KM6nGaczDz6qdIXXQg4wKVeSWDD2eFrwe4l0aFByVmVSjYbdnxKkXOySRy1ThomPznxWAawqiOndFa6nM8HE9oQawe72Hgc_-iHcgcI5Tdyq0XqYgSg5ZM1MDLyQjHPYrvQpzyQKVeEFv22XIf8srOXlpr9c0eNCPHW9lYhTDeEBtovNzSwdoop2_NJ6IdMTXGCF2MZqHbneB5hpvFb7CQQmxRaYiAijE6O8WTsRr_5YkO4W6XUpUhzJfVEWALPl1UgYHNcsy7IgkeAQfhdtNqdsMzd8eAcYkg-9ZWu1lfQsEVrb7yIVcBaiY8jX9Uz53rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07a0c49ace.mp4?token=aBh3TUrnXLCvxpwHjK-KM6nGaczDz6qdIXXQg4wKVeSWDD2eFrwe4l0aFByVmVSjYbdnxKkXOySRy1ThomPznxWAawqiOndFa6nM8HE9oQawe72Hgc_-iHcgcI5Tdyq0XqYgSg5ZM1MDLyQjHPYrvQpzyQKVeEFv22XIf8srOXlpr9c0eNCPHW9lYhTDeEBtovNzSwdoop2_NJ6IdMTXGCF2MZqHbneB5hpvFb7CQQmxRaYiAijE6O8WTsRr_5YkO4W6XUpUhzJfVEWALPl1UgYHNcsy7IgkeAQfhdtNqdsMzd8eAcYkg-9ZWu1lfQsEVrb7yIVcBaiY8jX9Uz53rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار شدید و بلند شدن ستونی از دود به آسمان در سلیمانیه عراق
🔹
منابع خبری از شنیده شدن صدای انفجاری شدید در سلیمانیه واقع در شمال عراق و بلند شدن ستونی از دود به آسمان خبر می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/682295" target="_blank">📅 19:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682293">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d4fae581.mp4?token=hsqSdObiqeqSJH4H-749TbEqYcUbIvbGwvhfukjiIF3jxprf7JjyFJcrgEXzJvzxdP5qF_j4XF44npBNywwXB7OKCvSqanjrYKriVuRLjVK0mamjKsYiBt6nyoQbRCGEnke8IegLKevkWvFekfK7gjvtuxk_9zLPJKyHaEfH1LJ3f9x7BI4MlymMPNvMF-rLKxCPnRVzk-gIaXDjyA1NAAza5LBnsEEncjGsH1mbUAxxiKzgqjudh7Mj5mAATX7t-KnECEqWGR4DKTkmjWAN6I7lmg3_TToIzLRHwvW9sMr9AEea1ZOhQkqi3cAPiEPPkjrInO8h8n2BueszGDwIVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d4fae581.mp4?token=hsqSdObiqeqSJH4H-749TbEqYcUbIvbGwvhfukjiIF3jxprf7JjyFJcrgEXzJvzxdP5qF_j4XF44npBNywwXB7OKCvSqanjrYKriVuRLjVK0mamjKsYiBt6nyoQbRCGEnke8IegLKevkWvFekfK7gjvtuxk_9zLPJKyHaEfH1LJ3f9x7BI4MlymMPNvMF-rLKxCPnRVzk-gIaXDjyA1NAAza5LBnsEEncjGsH1mbUAxxiKzgqjudh7Mj5mAATX7t-KnECEqWGR4DKTkmjWAN6I7lmg3_TToIzLRHwvW9sMr9AEea1ZOhQkqi3cAPiEPPkjrInO8h8n2BueszGDwIVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری در بین هواداران تیم استقلال و نساجی
/ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/682293" target="_blank">📅 19:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682292">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a54317960a.mp4?token=WsVDkhOmcq0Dk6ooJhOjA9NIuB0Ghjdg2DNZ9Ic_TLL8I0rZSS_lwgl3D2i3Hu3dCunsp2av7mE5dw1rZ0rbGEOkbWkZsQ2SrsXknFnx9MIeicCL-Kq9OimUekluFuFDmi0VRPIZ4SZT84QTuxPImcd9z42i0_D3EhQW5ivO1LVSQlSjzuWHQIQPUxYlsh_KasEQ936rvAGRW7z5YMlF4l4k9ZJtC6DhggbnPeqfAeFPPjjdl1tqzBtx_TsAvpZ-8P-LrzXh3ZjDWVEUqiQLfvQjwE-YOHIIrY1zsAFUeX-BJB-2zeYxqgJDE6Za0oPaC9PN_9_sNz7jUo5wdYUMSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a54317960a.mp4?token=WsVDkhOmcq0Dk6ooJhOjA9NIuB0Ghjdg2DNZ9Ic_TLL8I0rZSS_lwgl3D2i3Hu3dCunsp2av7mE5dw1rZ0rbGEOkbWkZsQ2SrsXknFnx9MIeicCL-Kq9OimUekluFuFDmi0VRPIZ4SZT84QTuxPImcd9z42i0_D3EhQW5ivO1LVSQlSjzuWHQIQPUxYlsh_KasEQ936rvAGRW7z5YMlF4l4k9ZJtC6DhggbnPeqfAeFPPjjdl1tqzBtx_TsAvpZ-8P-LrzXh3ZjDWVEUqiQLfvQjwE-YOHIIrY1zsAFUeX-BJB-2zeYxqgJDE6Za0oPaC9PN_9_sNz7jUo5wdYUMSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرف مردم بعد از ۱۹۵ روز دوری رهبر شهید: اگر الان بخوام باهاش حرف بزنم، می‌گم خیالت راحت دست پسرتون بالای سرمونه. ما هنوز اینجاییم، هنوز پای کاریم و راهی که گفتید رو فراموش نکردیم/
خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/682292" target="_blank">📅 19:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682291">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CU_nt3L8i7vl5-NyLp0bvpsp-88_BLut3DN8UNmLnqOfKhxpTlOSfyploauloGNIflp_4x0fGoov0uSJpFkWETShKfGgYr-c2Sd-tiW6iCvwUSaOzQANjQCqvh3LuS7E8Oz59uW6suAdNUgtno2u6RjwT4UmHWtRiS1KjtM9iU6dL1WZoh6-Y_M2uyw5qNSBg6hAK54gWcHp4FbxeWA6wi58QB3NzxGVdk3b4CunXG8mPx7Fo6A16MWG_xNVl7EvtEfLoXQGcepf2U69EU1pAth2hJtFPZ5EmsFYuMUistbwM0ru070kvK6ajDXtLUGAHGEb5iGR2szJqF9il8SRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیقات نشان داد:
آمپول لاغری علاوه بر کاهش وزن، چربی پنهان اطراف اندام‌های داخلی را هم کم می‌کند
چربی احشایی
چربی‌ای است که در عمق شکم و اطراف اندام‌های داخلی مثل کبد و روده جمع می‌شود و خطر ابتلا به دیابت نوع۲ و بیماری‌های قلبی‌عروقی را بالا می‌برد.
در یک مطالعه ۵۲ هفته‌ای،
آمپول لاغری حاوی تیرزپاتاید(مثل مونجارو در آمریکا-اروپا و زیکورپا در ایران)
توانست در افراد دارای اضافه وزن و مبتلا به دیابت نوع۲، حجم چربی احشایی شکم را
تا ۱.۶۵ لیتر
کاهش دهد. چربی زیرپوستی شکم و چربی کبد هم کاهش پیدا کرد.
نمونه تغییرات یک نفر که در این مطالعه حضور داشت در تصویر آمده
👆
منبع:
SURPASS-3 MRI,
The Lancet Diabetes&Endocrinology
, 2022</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/682291" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682290">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWme5YGsZK0HHjD3KdV-m_n-JK1Gq3-6dj6uRsS1NqwoGYXe29sOf7vat3un5w2CWlKtQQSG0nWmzNn169CEKF7gJnBCr1AzVh62kh1Us-jUbBqgulnJ7LFXrepTlUA2g1-7fS9lV1CxdQJRv8aba15KZk3x6nhHrrz4wMcwIbH6E39Rpos8mlecLd_auqtmuac-daGT6w6o8Us35iySMy8QlZ93gGVtUiDeV0LS2KrmlYHopcRDwVsb3WEEHXiymTOu1ireXVnaLZRmp0c4c4P_i3eKL7_BtG3BTGhO3MxSSFqEWrtAEt-H-9SQVwoeYBMQGbIxdInPlqGYlb2GKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فشار جنگ بر ذخایر پدافندی آمریکا
🔹
آمریکا از آغاز جنگ با ایران تا کنون ۲۰۰ فروند از رهگیرهای THAAD خود را مصرف کرده، درحالی‌که کل مصرف آن در سال ۲۰۲۵، ۱۵۰ فروند بوده است.
🔹
رهگیرهای دریایی نیز با سرعت بیشتری مصرف شدند؛ شلیک ۱۳۰ فروند SM-3 در جنگ، در برابر ۸۰ فروندی که در سال ۲۰۲۵ و ۳۹ فروندی که در سال ۲۰۲۴ مصرف شده، نشان‌دهنده افزایش قابل‌توجه مصرف است.
🔹
این افزایش، ذخایر موشکی آمریکا را تحت فشار گذاشته و بازسازی آن را به یک چالش بلندمدت تبدیل کرده است.
@amarfact</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/682290" target="_blank">📅 19:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682289">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFUHysvfZacm7Hw3Fp7GkAnvqloarJcl8UvuthPhf3HeEleJEYx5XWok_M1p-LZ8xp613cMwki9-WmK778laKxpB3rByh1xi6j_hFwqe1vYU05eTJBhqzzZNwAyE5toxCeCBBZg6nfE70_m2RlQ5cx1JuBwWfrFOmaq5ZvG0DOtypBAzmdzywPyyARibl7amK66trC6K3DT9egWdHJ6NuRfWFVDsaWFnTm4r_Qx7mqp2co-blNeEiCNkNXdZUi3wLRC_iKxXDgyNxWKwZUkk85QgOkLALW3Lz9I6KwnlD05mlXrKZQl2BaWr6emOk_oXKvptdNyu9YsD0f6VeQG_HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ تصویری از آرزویی که گراهام با خود به گور برد را منتشر کرد
ترامپ:
🔹
لیندسی همین چند هفته پیش داشت خوش می‌گذراند! کلاه را ببینید!
🔹
اشاره ترامپ به کلاه گراهام است که بر روی آن نوشته «ایران را دوباره با عظمت کنیم»، شعاری که گروه‌های برانداز و تجزیه‌طلب در آغاز تجاوز آمریکا و رژیم صهیونیستی به ایران زیاد به کار می‌بردند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/682289" target="_blank">📅 19:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682288">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ادعای رسانه اوکراینی:‌‌‌ روسیه برای بازسازی زرادخانه نظامی، مواد منفجره به ایران می‌فرستد
رسانهNV اوکراین:
🔹
با استناد به سندی از یک دولت اروپایی، روسیه تامین مواد منفجره و مهمات برای ایران را آغاز کرده است تا به تهران در بازسازی زرادخانه موشکی و پهپادی خود پس از حملات آمریکا و اسرائیل کمک کند.
🔹
بر اساس این سند ادعایی، مسکو به طور مشخص مواد منفجره، مهمات و قطعات پهپاد را از طریق دریای خزر برای تهران ارسال می‌کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/682288" target="_blank">📅 19:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682287">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYxl71sCwFImKmwflDYVNOKYgg1j4tSrn6k1zdT3sauBYG_tiY7khxDmw55ZaNd_cEyvO1KKr601qf6HHXNaeoEjOqzXoaBmqVWRx5M8_skQXIyU9cCkhhBeze5eX8LpxSXZqvIjScjpm5mL39tPfT88eck3x3llImQQRnBcw3CK7Xl_iQwvelSZ7I5u-j9YQDgXjvAlXAvAXeNpkYE9LRNVQTzeLU5-wAE_iWBdB6jWAakaRNfPvSIvNgowRj3LjmwL462ZCMkydF4NGoL2ybXYoleR39r7QzsY_TnSxwyWDMu4bIaehE6cKRxmuqhtw80boaXVyG3hn78W_gKXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
یک پهپاد در استان مأرب یمن سرنگون شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/682287" target="_blank">📅 19:23 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682286">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
واشنگتن‌پست: پنتاگون در حال بررسی کاهش حضور نظامی آمریکا در خلیج فارس پس از جنگ ایران است، زیرا حملات ایران آسیب‌پذیری پایگاه‌های اصلی آمریکا در منطقه را آشکار کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/682286" target="_blank">📅 19:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682284">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887752b933.mp4?token=V091Loba9Vq4UPZ2Mq_mKbzpe5y2hmwrA1EKhRsZOHvDXh5VtnVxnJdLeyMeOniOk7tDISoTpPVR533XmgHXtB5JtsxoXaRrepNGNvRKw6yOtPa_cuYXOawdb44nD79UNRSpOyfrkmjaK3H0-Z5l7tIuK7autBrPE5AaOfqcGkm1x5jkqx79TyQy7oQ9EcIk7B48A8ZPIYIBX-orUnwr3ncrlr48oJtkPHWzO2cLXnf0DyUplr4-C9gU6GTKFvzGXeaov7kttQRLWXXeZNxt_e3s8rkFtqtVwfNAxkFq9izpn8_c17e8cW3rZGYjPjujr_F9Byqbd31WLkNAJDtxFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887752b933.mp4?token=V091Loba9Vq4UPZ2Mq_mKbzpe5y2hmwrA1EKhRsZOHvDXh5VtnVxnJdLeyMeOniOk7tDISoTpPVR533XmgHXtB5JtsxoXaRrepNGNvRKw6yOtPa_cuYXOawdb44nD79UNRSpOyfrkmjaK3H0-Z5l7tIuK7autBrPE5AaOfqcGkm1x5jkqx79TyQy7oQ9EcIk7B48A8ZPIYIBX-orUnwr3ncrlr48oJtkPHWzO2cLXnf0DyUplr4-C9gU6GTKFvzGXeaov7kttQRLWXXeZNxt_e3s8rkFtqtVwfNAxkFq9izpn8_c17e8cW3rZGYjPjujr_F9Byqbd31WLkNAJDtxFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فواید و ضررهای انواع مواد قندی از زبون خودشون
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/682284" target="_blank">📅 19:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682283">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITEQbkBNvpcU4Q_Cd78q2tlAPOR4YoNGrARaLbgLCHMtJc4Qj5PXMdca9UHBFzccnYiZGmj8wVGvLmVt9aMVZY4hB4D5CMGy_HSDN6hNHolJeOq7HZ80Lrt6muIikZ0pSVp3ta9Z_TgrwO8tJdYnjstGF-m5Rc7iEovu7xAHevSCvK9gw3T6pisfVKoY6BMczMGuTgw84waPPVs-zWDlVNwut2VvpCEuRSFoYe7QQ-RA5_6GaPh4-lT3XZC7lratJYPAIt0MG34EYhG7gpvuIObwBp1YMFDDFuSmydTCG635qKhzCb4oMW6hRnmkjA8vbyYgg-Sz2leREk643vavnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۰۰‌هزار تومن تخفیف خرید با اسنپ‌پی در شبکه‌های اجتماعی!
دیگه با اسنپ‌پی می‌تونی از بیشتر از ۴هزار فروشگاه و برند محبوب در شبکه‌های اجتماعی مثل اینستاگرام، بله و تلگرام، خرید کنی
و با درگاه پرداخت امن اسنپ‌پی هزینه‌ش رو در
۴قسط، بدون سود و کارمزد
پرداخت کنی.
با وارد کردن این کد تخفیف توی درگاه اسنپ‌پی، خریدت رو نهایی کن:
✨
کد تخفیف:PAY5SCMD
از طریق لینک زیر، لیست برندها رو ببین و با تخفیف و قسطی خرید کن:
https://l.snpy.ir/br9ej
https://l.snpy.ir/br9ej
https://l.snpy.ir/br9ej</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/682283" target="_blank">📅 19:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682282">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gz54hxLZW9xcNSDlKED_UPUrGg6Dhc9rIkvYDIa5MXMYOgLr3-YKHP-cOF3nSapLCaodleXrTC2-NIZHqUpwPRYSanKw3bX7KSRBAmmqjWe3psJpmDghBs48cQiPcCpYNfHyf5VZmCdDalixoeyP4sY468Z5N0dQAep-SgOYxReU4cqyAbaLBZLusDqi5FilgilldQ5BwtwXxcn6ZlM00gOeUTYoYzKWN-nTx-tsYtkTEuOXo4f0INsgDia-X4LvjcId8cAHy01k1gSfwCILMe5rp08z3N0jvrMrCd8nT6gqP3rhXG25fQVQj0v2dhO0W4qyWl_1Wn0eiAvc6xDaXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👉
👉
👉
Vakilar24.com
👈
👈
👈
هفت روز هفته در هر ساعت از شبانه روز با ورود به سایت ما و یک تماس مشاوره فوری با وکیل داشته باشید و مشکلات حقوقی خود را با ما در میان بگذارید .
وکلای ما هر لحظه آماده مشاوره با شما هستند.
🟡
مشاوره فوری تلفنی
👉
👉
👉
Vakilar24.com
👈
👈
👈
با عضو شدن در کانال ما ضروری ترین و به روزترین اطلاعات حقوقی را داشته باشید .
🟡
کانال تلگرام
@vakilar24
🟡
مشاوره فوری تلگرام
@vakilar24_ads
موسسه حقوقی قانون گستران عدل جاویدان
شماره ثبت : ۴۸۵۸</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/682282" target="_blank">📅 19:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682281">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
هشدار فوری وزارت کشور امارات درباره تهدید احتمالی موشکی
🔹
وزارت کشور امارات با ارسال پیام‌های هشدار اضطراری (Emergency Alert) بر روی تلفن‌های همراه ساکنان، خواستار رعایت فوری تدابیر امنیتی و پناه گرفتن در اماکن امن شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/682281" target="_blank">📅 19:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682280">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f6748d8ed.mp4?token=T2JkVl80RUKe4HF8qnuhzjlt_TK05okfH_nemkXyhVC0rdi5kj-BIbl1dRYzjLvLytIEYUVe1hlYNJe422D86MPUHAs7QhJoutbT_lO5771WUdpikG-DV2kmvkxkEVRA_tQnRSnn4M0BkbCgTxcLFU9i7-wdMD9lchSJiV2V92z1q9bmZpFMIWSWLux39Hnkr-AQzEMMtBS1q6iP4JGmSNHbwjdicmX-54D-r8e1euCoiQ6pUd7t0AF4DzJfC83eoRUPMdPb8Hyf7qcLK8vtGU_0Y7QasMYcTiKlO73nGcQtIpjnHf8Oo6rYNz3dERiWY4HUZ8sC2lzmkZ8ruvs6UYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f6748d8ed.mp4?token=T2JkVl80RUKe4HF8qnuhzjlt_TK05okfH_nemkXyhVC0rdi5kj-BIbl1dRYzjLvLytIEYUVe1hlYNJe422D86MPUHAs7QhJoutbT_lO5771WUdpikG-DV2kmvkxkEVRA_tQnRSnn4M0BkbCgTxcLFU9i7-wdMD9lchSJiV2V92z1q9bmZpFMIWSWLux39Hnkr-AQzEMMtBS1q6iP4JGmSNHbwjdicmX-54D-r8e1euCoiQ6pUd7t0AF4DzJfC83eoRUPMdPb8Hyf7qcLK8vtGU_0Y7QasMYcTiKlO73nGcQtIpjnHf8Oo6rYNz3dERiWY4HUZ8sC2lzmkZ8ruvs6UYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لبیک یعنی با امین ‌الله بودن، بعد از علی با مجتبی همراه بودن
🔹
شعرخوانی مهدی رسولی در مراسم چهلمین روز تشییع و تدفین آقای شهید ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/682280" target="_blank">📅 18:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682279">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d275989b83.mp4?token=CQJ-CvVDiZMt7IfebPyCztBNJT-8_bAD8Bew_48RitKderHdJyQdrKC9rbQQO1aRMPDic5AgUdGBeugSVdq8UThisorAb2P5JlcRm11MNI0295fu8LRcxEipNReGoEyek1KK-tEGTtTSoTlUaw08bEWakT4naebZgLtj5dxoOOJ3_xqIlXpo4v59UPBa7jiczZpKgVEYSw8YcNGjDHi7E0th6Tob-8I1BhqzirQXfM3OC8AT7q-D6k2pR9x0rgL7INAPmMop85nV0g-pQ7h09mRR4d9Tg_lPudtG8aBNfSPDD724zFNZmjoOiGR1nDus9yL7nZ8X86Lu9SWzICbMbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d275989b83.mp4?token=CQJ-CvVDiZMt7IfebPyCztBNJT-8_bAD8Bew_48RitKderHdJyQdrKC9rbQQO1aRMPDic5AgUdGBeugSVdq8UThisorAb2P5JlcRm11MNI0295fu8LRcxEipNReGoEyek1KK-tEGTtTSoTlUaw08bEWakT4naebZgLtj5dxoOOJ3_xqIlXpo4v59UPBa7jiczZpKgVEYSw8YcNGjDHi7E0th6Tob-8I1BhqzirQXfM3OC8AT7q-D6k2pR9x0rgL7INAPmMop85nV0g-pQ7h09mRR4d9Tg_lPudtG8aBNfSPDD724zFNZmjoOiGR1nDus9yL7nZ8X86Lu9SWzICbMbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران من، با خونِ دل دوستت داریم و با جان، از تو می‌خوانیم؛ پرچمت که برافراشته شود، قلب یک ملت دوباره به تپش می‌افتد
🇮🇷
❤️
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/682279" target="_blank">📅 18:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682278">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
عراقچی: جنگ باید به گونه‌ای تمام شود که دیگر تکرار نشود
🔹
همسایگان ما در اولویت هستند.
🔹
یک تلفن آقای دکتر پزشکیان به رئیس جمهور آذربایجان و استقاده از چهار مثل آذری کاملا ورق را برگرداند.
🔹
کشورهای منطقه اصولا نگاهشان به ساختار امنیتی منطقه تغییر کرد؛ چرا؟ چون جنگ باید به گونه ای تمام شود که دیگر تکرار نشود.
🔹
صلح و جنگ در قانون اساسی ما کاملا روشن است که تصمیم گیری آن با چه کسی است.
🔹
بزرگترین مصیبت جامعه ما دوقطبی‌هایی هستند که بیشتر کاذب و بعضی وقت‌ها واقعی ایجاد می شوند.
🔹
هیچکس نیست از دوست و دشمن که به اخلاص دکتر پزشکیان شک بکند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/682278" target="_blank">📅 18:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682277">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa77c0845.mp4?token=vVEkgH8suZ65Y_EVVjnL1XVQ8dWc7G0ee7pDf79XfsG3kqNK8Q50ChshgKudRsbE3E5R2IxdPkemQR_MdRWeR__xLH4EwH7oeE5JTrB2a75zIOXemuvL1xREaNhfEOXaraVAkft71dvadhm4U08YS3yDrRrPoAP6zcO0ZxyMuM6-enaEqDU9RS1Z52vbKVwXy0R0krTfb-_IOm74YJMwAo1qc6TJblKHn8fWJo6BWUTIJnqj8UAkJFBdMd8qaQDiv9TjzziaeXFTPA5-sBSUrMSI-IV8wH6YSfDNmFHctaVKHXpZHbgHCKG0hE1MWbDjVjKa9vK4dZgHsaFVkkUuqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa77c0845.mp4?token=vVEkgH8suZ65Y_EVVjnL1XVQ8dWc7G0ee7pDf79XfsG3kqNK8Q50ChshgKudRsbE3E5R2IxdPkemQR_MdRWeR__xLH4EwH7oeE5JTrB2a75zIOXemuvL1xREaNhfEOXaraVAkft71dvadhm4U08YS3yDrRrPoAP6zcO0ZxyMuM6-enaEqDU9RS1Z52vbKVwXy0R0krTfb-_IOm74YJMwAo1qc6TJblKHn8fWJo6BWUTIJnqj8UAkJFBdMd8qaQDiv9TjzziaeXFTPA5-sBSUrMSI-IV8wH6YSfDNmFHctaVKHXpZHbgHCKG0hE1MWbDjVjKa9vK4dZgHsaFVkkUuqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی رژیم صهیونیستی به بندر غزه
🔹
منابع خبری از حمله پهپادهای ارتش اسرائیل به محوطه بندر در غرب شهر غزه خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/682277" target="_blank">📅 18:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682276">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
تالاب انزلی؛ اختلاف‌نظر درباره مقصران آلودگی، اتفاق‌نظر درباره ضرورت نجات
🔹
در حالی که مسئولان محیط‌زیست بر امید به احیای تالاب انزلی و ضرورت تمرکز بر راهکارهای نجات آن تأکید دارند، اظهارات مدیران حوزه آب و فاضلاب و کارشناسان محیط‌زیست، ابعاد تازه‌ای از عوامل تخریب این تالاب را آشکار کرده است.
🔹
از نیاز به بیش از ۵۰۰ میلیارد تومان اعتبار برای اجرای طرح‌های احیا گرفته تا نقش فاضلاب‌های شهری، صنعتی، بیمارستانی و حتی شهر صنعتی رشت در آلودگی تالاب، هر یک از مسئولان روایت متفاوتی از وضعیت امروز تالاب انزلی ارائه می‌کنند.
#نجات_تالاب
🔹
جزئیات کامل این گفتگوها را اینجا دنبال کنید
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/682276" target="_blank">📅 18:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682275">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eP1qhCg1pOVzw5M3RmiX_Pks5BOuMjcvj9Fe1R9Dyxx8PRDfE2ZdkZsoZ7bx3pnDsvqCm3z3SsyQWapzB1c4NF6t_Uzm2G8gyJI_ecd6cbE1ncX8RIEmFDAeZGsVVKxDT85sIEwifUigxMs7lMJTgWksJoSizxljxD9_UQlOjo6CHkMFAzSAN-1sS4vyDsJwDlPHvYVE-duSETL49ZZutbBbgjUNN44KpFwkqjyIe1gGS-E9pFcAUgcbnEIjStuQSGOKrm0PgJjFKuKeIrooSR40-bcAImlLXi83WK8N8bgmSPcZjCrqS8M-Ys5xwijNKTgoZFC9IL0ATXZdMBmJaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از حضور خانواده رهبر شهید انقلاب و روسای قوای مقننه و قضاییه در مراسم چهلمین روز تشییع و تدفین آقای شهید ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/682275" target="_blank">📅 18:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682274">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b52782ffe6.mp4?token=bzoBgtzXUDRW3XLnb8MFJiPD18YeRXOPK5VIuhdt-xhwk4QDYJ68tI1pZipjDQbpwIEGqQ9riiz23kqn3Mb96ZkLQ_4q_UPcZhRzNNDo0CJmnvnC6-IJNubl9YZn2peooHzCJ4fQXe2B1lKYz9V4R5uF_oynp8LWFtI_UBVAqmVqtQX0NxkWOT70dawDN8_vOXUwJJQFA3A9cIXfC3CzQfW_v9rqdPV51qspb-F6rYmgXB8zzDiHh5JPJKwS2TqEWkYD0gPLDWXDMsMZH--AmQT6jA1S_Tj0_GipY0AmNIVdPjZQvT5lfM9HpYQ4qUT7yVwA3y7OUtRVpcFKBJmaHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b52782ffe6.mp4?token=bzoBgtzXUDRW3XLnb8MFJiPD18YeRXOPK5VIuhdt-xhwk4QDYJ68tI1pZipjDQbpwIEGqQ9riiz23kqn3Mb96ZkLQ_4q_UPcZhRzNNDo0CJmnvnC6-IJNubl9YZn2peooHzCJ4fQXe2B1lKYz9V4R5uF_oynp8LWFtI_UBVAqmVqtQX0NxkWOT70dawDN8_vOXUwJJQFA3A9cIXfC3CzQfW_v9rqdPV51qspb-F6rYmgXB8zzDiHh5JPJKwS2TqEWkYD0gPLDWXDMsMZH--AmQT6jA1S_Tj0_GipY0AmNIVdPjZQvT5lfM9HpYQ4qUT7yVwA3y7OUtRVpcFKBJmaHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سردار قاآنی و محمد مخبر در مراسم چهلمین روز تشییع و تدفین آقای شهید ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/682274" target="_blank">📅 18:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682273">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
اخبار تائید نشده از شلیک چند فروند موشک از سوی نیروهای مسلح یمن خبر می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/682273" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682272">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRdwFk6QLKqWreFTIw1OaQvHcMB8xE54LYwo-wmrutLsBqQISJGZntYYD1C7SLU7LKYGeTAkLBIapoKgbjCR2bex-d4ojSU1kWMEr6_AdRiLiTSPRXSM6xmLA3zmYdNJQL8ch1RO1jtGBxTiQ041iiQW5zmm49xsjpSdicxKiu4gG0VqqXYmQwVPqUKQM9M-XANOJ5H1I_BDs4HclhVqRMcCKIlOr5FMuB0SyORPxT9uUXkRjS-VQPJLxXqGrO-YsCI8rnnYU7OzlXwdJEOzxMFL5uIog0fbwPNP81Hynel76SBJYxw9xQ-IAzx2o9cSiuifd5uXATuE_p772CUtNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شنیده شدن آژیرهای هشدار در دبی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/682272" target="_blank">📅 18:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682271">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7353b8c3c0.mp4?token=J5Euc_GB11taLZFao6-VkM7-oeWazQjHDyFDlIjrKQ2USC1Sx28u0VL1nixaaM4v2MS0iY_Tor4P2cqeRnpfcap4CUxgIOdM3EnYRGjwNSPNqh4HlN-LkLQMWYk04WP6x3KzgkesIQVrgs-zVwLqb9zm-M7uHD1rKhaYI8fT-wm_lhwsrDARIqxL4AGhtKfbGfrY0EuzlXLlGbqGhKM3Go963EJ3tPGtx9MYvgaR3LNSAbvnnxv831MiZDnmx0WIy2f4ciXhI1x_AUNTaOFOGqvKgNBmr6vHz8bPkNFn0AVBgqVOSpxfr6MW6wFyjHgI-GgbGS6PDjeEJZ6zIJN4qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7353b8c3c0.mp4?token=J5Euc_GB11taLZFao6-VkM7-oeWazQjHDyFDlIjrKQ2USC1Sx28u0VL1nixaaM4v2MS0iY_Tor4P2cqeRnpfcap4CUxgIOdM3EnYRGjwNSPNqh4HlN-LkLQMWYk04WP6x3KzgkesIQVrgs-zVwLqb9zm-M7uHD1rKhaYI8fT-wm_lhwsrDARIqxL4AGhtKfbGfrY0EuzlXLlGbqGhKM3Go963EJ3tPGtx9MYvgaR3LNSAbvnnxv831MiZDnmx0WIy2f4ciXhI1x_AUNTaOFOGqvKgNBmr6vHz8bPkNFn0AVBgqVOSpxfr6MW6wFyjHgI-GgbGS6PDjeEJZ6zIJN4qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور قالیباف و سیدحسن خمینی در مراسم بزرگداشت چهلم آقای شهید در مصلی تهران  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/682271" target="_blank">📅 18:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682270">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
شنیده شدن آژیرهای هشدار در دبی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/682270" target="_blank">📅 18:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682269">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e34991202.mp4?token=Y4md0X1YEq2_IvVPxzqqqpE_dA1Tz0OQSn2pqSu0I_yGbKTPozXiFndG-zK1ehH_gqY9y_lnZ-HHFdNQGmCHzpBdh3994ZQS67mluppPERK4Lq2B5Du5ivx2vcE566MdVRnWCBH_68cwkmfI5mOktGHM6yaD7glyBpypfjMf-aYlmNT1r4dJrPJUZOJH_D-Fg7zu0TczcmdGb6XA4TfPVt-xLNdOhgbtnpR6-LMc95MPo1avVv4PWc1dR8QfHUBmCvTkYqjVWeFmDHFEmyKo4ZZ_cGHxo8YXoB9XpBJlXDIJnbUDaBL3oC8a4LbIM4-0a9nzgugp12Q3cKqnmg1YhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e34991202.mp4?token=Y4md0X1YEq2_IvVPxzqqqpE_dA1Tz0OQSn2pqSu0I_yGbKTPozXiFndG-zK1ehH_gqY9y_lnZ-HHFdNQGmCHzpBdh3994ZQS67mluppPERK4Lq2B5Du5ivx2vcE566MdVRnWCBH_68cwkmfI5mOktGHM6yaD7glyBpypfjMf-aYlmNT1r4dJrPJUZOJH_D-Fg7zu0TczcmdGb6XA4TfPVt-xLNdOhgbtnpR6-LMc95MPo1avVv4PWc1dR8QfHUBmCvTkYqjVWeFmDHFEmyKo4ZZ_cGHxo8YXoB9XpBJlXDIJnbUDaBL3oC8a4LbIM4-0a9nzgugp12Q3cKqnmg1YhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ازدواج موفق چه ازدواجی است؟
🔹
احساس می‌تواند آغاز رابطه باشد، اما ادامه‌ آن بدون منطق ممکن نیست؛ همان‌طور که یک ازدواج صرفاً منطقی هم بدون عشق و پیوند عاطفی عمیق، به نتیجه مطلوب نمی‌رسد./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/682269" target="_blank">📅 18:22 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682268">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
سقف تسهیلات ساخت، خرید، جعاله و ودیعه مسکن افزایش یافت
🔹
هیات عالی بانک مرکزی در راستای حمایت از متقاضیان تسهیلات مسکن، تقویت عرضه و تقاضای بخش مسکن و افزایش قدرت خرید و حمایت از مستاجرین با افزایش سقف تسهیلات پرداختی از محل اوراق گواهی حق تقدم برای ساخت و خرید واحد مسکونی، ودیعه و جعاله، به شرح زیر موافقت کرد:
۱) تسهیلات خرید و ساخت مسکن
شهر تهران؛
🔹
مبلغ تسهیلات خرید و ساخت (انفرادی) ۱۰ میلیارد ریال
🔹
مبلغ تسهیلات خرید و ساخت (زوجین) ۲۰ میلیارد ریال
مراکز استان و شهرهای بیش ۲۰۰ هزار نفر جمعیت؛
🔹
مبلغ تسهیلات خرید و ساخت (انفرادی) ۸ میلیارد ریال
🔹
مبلغ تسهیلات خرید و ساخت (زوجین) ۱۶ میلیارد ریال
سایر مناطق؛
🔹
مبلغ تسهیلات خرید و ساخت (انفرادی) ۶ میلیارد ریال
🔹
مبلغ تسهیلات خرید و ساخت (زوجین) ۱۲ میلیارد ریال
۲) تسهیلات جعاله مسکن
🔹
سقف تسهیلات تعمیر (جعاله) واحد مسکونی از محل اوراق گواهی حق تقدم از ۲ میلیارد و ۸۰۰  میلیون ریال به ۴ میلیارد ریال افزایش یابد.
۳) تسهیلات ودیعه مسکن
🔹
سقف تسهیلات ودیعه مسکن از محل اوراق گواهی حق تقدم از ۳ میلیارد ریال به ۴ میلیارد ریال در شهر تهران، از ۲ میلیارد و ۲۵۰ میلیون ریال به ۳ میلیارد ریال در مراکز استان ها و شهرهای بالای ۲۰۰ هزار نفر جمعیت و از یک میلیارد و ۵۰۰ میلیون ریال به ۲ میلیارد ریال در سایر مناطق افزایش یابد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/682268" target="_blank">📅 18:11 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682267">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQRbTC7xCFnx_b_Sf650_kQyhkOTs9cYyRiI7Xnp9id9BfwJTgTiI72zFNqsqHm3XACACFopsMYsNhM3jBHLnLENxAL58yobfKsSDn8sCJyzmWUk6PbvG5OpKZnA5cLvC8MuUVMbY0TxS50wi77UTeQ1kgxGKR8azbF3yODYxUUQZ2a_4j0gXFT7E5PVeFGLf_BwfJS7tqpVkg2cRfOd0m9LidCxxF6Z8Z9SU4A41XSFj52vaVm4oTCGlkcCR8SbnMGv56dXczMPRUM4nYMbdoMK0YwRsORyz4p70l3uCk059aPJhVuSOfd7yd-FZqCQg02qkPOr0v270EDib0-8Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قلمرو جدید ایران
🔹
دونالد ترامپ در ادامه مواضع جنجالی اخیر خود، در پستی نوشت تنگه هرمز؛ قلمرو جدید آمریکا. ادعایی که بیش از هر چیز، بیانگر رویکرد مداخله‌جویانه و نگاه توسعه‌طلبانه او به مناطق راهبردی جهان است. چنین تفکری، در صورت تبدیل‌شدن به سیاست عملی، می‌تواند ایران را هم به سیاستی وادار کند که در پی مالکیت سرزمینی مناطقی چون جمله بحرین، قطر  و امارات باشد.
🔹
هشتصدوسی‌‌وهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/682267" target="_blank">📅 18:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682266">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
سازمان تجارت دریایی انگليس: یک کشتی باری هنگام عبور از محدوده تنگه هرمز هدف اصابت یک پرتابه ناشناس قرار گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/682266" target="_blank">📅 18:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682265">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODybslvvs6S_Ms8cljwn1S3-bm-GZD4GLi6BfOggY6RjqMMEty3NCpyhMI-0VASoSYhieMhNak0BjQT8OE1LsoBQm5MYMmeCN-tV0k3322Ahx_fs7uWRrN2Gk6JeveBZDMM3NFQIjyahqLJU8SdKMoHEKSx5cqvZzw5M5fNV04vl7oztgGXHjJSbC95qnZ1WzYEV-H0WyBdVUD9PJ4DLfqOKqkhj0pYPIGAuiPhRdGU76hEMD8onVAbKkc0gfhVDK6KgAJdG3kBYZLeFaFCU9_F60GfYBlYwJR9zjokj_hfokzwdkW4L75tZIC0EzfkyXORq1_O7E7cd2vNCX0OegA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هنرمندی که نامش با واقع‌گرایی، ظرافت و شکوه نقاشی ایران درآمیخته است؛ کمال‌الملک
🔹
محمد غفاری، مشهور به کمال‌الملک، از برجسته‌ترین نقاشان تاریخ معاصر ایران بود که با دقت کم‌نظیر در جزئیات، نور، رنگ و واقع‌گرایی، جایگاهی ویژه در هنر ایران پیدا کرد. آثار…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/682265" target="_blank">📅 18:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682264">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc5f2b213c.mp4?token=BPADyP_LxcHCvghzgfGWaE0xyGUvvzIFMA6CiJZXMiCWS0kBWIMu4tKb2KAzo6DvJ3lXPJVZOzqVLtv5Z5CfijadP3uUYhWWzx49-hBnijYQd8Ml_mk5aIaLkgML54AAPkQZMmIf41yFdvRtycxmDBMuYg56eCDYLJOAIASXnuECK8CYMx0NcwLuqpQTFjWvMl1euPa6_erw6Nia8ZtKKr_RJNC_v1Y8RLSCPjNOTgbaRPPeLQ39b00Hw0JlWDkGvyi5LN2RgJt1xgp_jxc-TPG7y43FkUYK5nixmHIHDLq15n8Shu8aiXXW3r8e22k5ePUCA3JUVXNf1bqLjvXQZWkXLSQ5zYIzx93MfwAAbV59c9v1ghngwZzqbS9wU4sV4K1hBgu5NBVMa7xnDA651UsaYZ1MSgR72nT7jP1Z8Z5UyYLp8pgDiPj1YZInSi-elz6q4i2-rJId_NsXx5DXR2bi9DoIz1XhulIKl37RCpNvrnQfvE-0GqeNaGAO-9m98ZBHgMnqW7A6pzDDRqKpqQmEIJ7jXXbAihhIpnPBlcyg0FdJT9DhbO-K5VdNVDKT776rHr_i8TPzZpxshZ8eiEkm-IVKTEe9_d3cAPJBQXgKRkrnjpzHdfJpwfUIwb67PjEAli_DFqMJb8PP8Vcx-DQvuPJSokr0OPYZjrytARY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc5f2b213c.mp4?token=BPADyP_LxcHCvghzgfGWaE0xyGUvvzIFMA6CiJZXMiCWS0kBWIMu4tKb2KAzo6DvJ3lXPJVZOzqVLtv5Z5CfijadP3uUYhWWzx49-hBnijYQd8Ml_mk5aIaLkgML54AAPkQZMmIf41yFdvRtycxmDBMuYg56eCDYLJOAIASXnuECK8CYMx0NcwLuqpQTFjWvMl1euPa6_erw6Nia8ZtKKr_RJNC_v1Y8RLSCPjNOTgbaRPPeLQ39b00Hw0JlWDkGvyi5LN2RgJt1xgp_jxc-TPG7y43FkUYK5nixmHIHDLq15n8Shu8aiXXW3r8e22k5ePUCA3JUVXNf1bqLjvXQZWkXLSQ5zYIzx93MfwAAbV59c9v1ghngwZzqbS9wU4sV4K1hBgu5NBVMa7xnDA651UsaYZ1MSgR72nT7jP1Z8Z5UyYLp8pgDiPj1YZInSi-elz6q4i2-rJId_NsXx5DXR2bi9DoIz1XhulIKl37RCpNvrnQfvE-0GqeNaGAO-9m98ZBHgMnqW7A6pzDDRqKpqQmEIJ7jXXbAihhIpnPBlcyg0FdJT9DhbO-K5VdNVDKT776rHr_i8TPzZpxshZ8eiEkm-IVKTEe9_d3cAPJBQXgKRkrnjpzHdfJpwfUIwb67PjEAli_DFqMJb8PP8Vcx-DQvuPJSokr0OPYZjrytARY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بوگاتی‌ای که روی زمین پرواز می‌کند
🚀
🔹
این بوگاتی با ارتفاع بسیار کم، جلوپنجره بزرگ و طراحی خاصش، یکی از متفاوت‌ترین ابرخودروهای دنیاست؛ خودرویی که با رسیدن به سرعت ۴۰۰ کیلومتر بر ساعت، حس یک جنگنده را به راننده می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/682264" target="_blank">📅 17:56 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682263">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دشمنان، بدانید مردم ایران بیدارند
!
🔹
گزارش خبرفوری از بین جمعیت حاضر در مراسم چهلم رهبر شهید انقلاب
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/682263" target="_blank">📅 17:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682262">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فایننشال‌تایمز: ایرلاین‌ها بر سر کاهش قیمت بلیت در بحبوحه کاهش هزینه سوخت جت، در بن‌بست قرار گرفته‌اند.
🔹
ادارات چهارمحال‌وبختیاری فردا تعطیل است.
🔹
ادارات هرمزگان فردا تعطیل شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/682262" target="_blank">📅 17:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682261">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین علت کاهش تمایل مردم به خواندن کتاب چیست؟</h4>
<ul>
<li>✓ جایگزینی شبکه‌های اجتماعی</li>
<li>✓ کمبود وقت</li>
<li>✓ عدم جذابیت کتاب‌ها</li>
<li>✓ ضعف در فرهنگ‌سازی</li>
<li>✓ افزایش قیمت کتاب</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/682261" target="_blank">📅 17:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682260">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nz6qZMyjKnpHtJwVUtZLkrQPPH00iR4Hc3ETiisY6B2LXC2v1K1LaXIZZi_POZpc43px3wHIGcG0xIPrdkUo64dyU2jkQ8BM4a8DGb3guY1B7Qb0LYT3jOBb4SxHihUrDpLRbztjmKkstpSSziksP6ZCs-uPK4hZSobQUvODBWZJhc_XXMax7NSU8OJ-K_IlQ-HZhAFxeiREds12O5qqqvepIT9bWCwd_eM3jSZEl8ZecMH9INezZ7xIqnfdye_1u8bG6ZUEwgMiSX21Oxk6cSUbnOrq0SOgRzSYuXwfgRNG2YDte89vruhwRgY_San3625BypVsTK_n-zc8Ftr3FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعاهای مضحک و تغییر پذیر ترامپ متوهم
🔹
ترامپ در ساعت ۸:۰۰ صبح: عمان را با خاک یکسان خواهم کرد
🔹
ترامپ در ساعت ۳:۰۰ بعدازظهر: ایران را با خاک یکسان خواهم کرد
🔹
ترامپ در ساعت ۷:۰۰ شب: کوبا را با خاک یکسان خواهم کرد
🔹
ترامپ در ساعت ۹:۰۰ شب: من تنها رئیس‌جمهوری…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/682260" target="_blank">📅 17:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682259">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
پزشکیان: دریافت هرگونه خدمت در کشور منوط به ارائه کد پستی و کد ملی می‌شود
رئیس‌جمهور:
🔹
آگاهی از داده‌های مکانی، هویتی و مالی پیش نیاز اساسی برای تصمیم‌گیری‌های کلان و سیاست‌های اجرایی است
🔹
تمامی اشخاص حقیقی و حقوقی و دستگاه‌های اجرایی و خدماتی باید دارای کد نشانه‌گذاری دقیق باشند
🔹
دریافت هرگونه خدمت در کشور، منوط به ارائه کد پستی و کد ملی خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/682259" target="_blank">📅 17:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682258">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28411a1567.mp4?token=OwJvJp7xmnZFR3xHoMeQncEMA8D94QxeenRtfP5e5yl9Bi7gVd27I4BxAtNtdUOfEvwqBtc85EtuMOIrmR-THydXoL3719ALTHGo5gAsnhwbc3Ql5yLNgmxUyqiJJIoYXspg5p8YC3OWd-Ass2wAjrq04zxcOBIP2N17UYxHnfzC5kjhzS6fzvyPZRtyAfdwbBoWHHQFat3Kr2JyVw8y_RKHmyrpuLaK-FDcBMNFWAa67y6vOlqHFBEeoGQem22UrLb_jJfxQeAdkjpDNccfAIbBP8lHD67NXMA5GCtHhBkbFHfIh1E6H5L8Nh3SLJti5840hGcMxAdEb8xv-h-2lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28411a1567.mp4?token=OwJvJp7xmnZFR3xHoMeQncEMA8D94QxeenRtfP5e5yl9Bi7gVd27I4BxAtNtdUOfEvwqBtc85EtuMOIrmR-THydXoL3719ALTHGo5gAsnhwbc3Ql5yLNgmxUyqiJJIoYXspg5p8YC3OWd-Ass2wAjrq04zxcOBIP2N17UYxHnfzC5kjhzS6fzvyPZRtyAfdwbBoWHHQFat3Kr2JyVw8y_RKHmyrpuLaK-FDcBMNFWAa67y6vOlqHFBEeoGQem22UrLb_jJfxQeAdkjpDNccfAIbBP8lHD67NXMA5GCtHhBkbFHfIh1E6H5L8Nh3SLJti5840hGcMxAdEb8xv-h-2lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر و پرچم‌های خونخواهی در مراسم چهلمین روز تشییع و تدفین آقای شهید ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/682258" target="_blank">📅 17:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682257">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f3b5f8e0.mp4?token=BavGN46BFtDIm8RYZfFUf_Mx8bwgYIU6Dci5OpURKmXGyfCIszRJ5iJUg6v1aRnn4SzdC_u-uVeMtgurHQBe4ua54s_h_puOZ_K6bsY8c87L8zp48R1E4Vbk1L89BRRQaFo_lGyDlFpfz-HNwd5hvmK_eADIxdEw1gn7iI9v4GHx_0Hn3Xliq14xW5RwGXcHY6CeBZ7hqho7BZiarq8WTweWtNuGVT8RDKtXrA3NZkooTjpijCiLYBv30xxsNsGQRwtJGLZ9rt8Uvit4mOlIIPadHPJAC2uujvJ5WH8PwSU3lbGy43xUAvAMOHnh36uABin6-8oYx-l7Yew84dSjpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f3b5f8e0.mp4?token=BavGN46BFtDIm8RYZfFUf_Mx8bwgYIU6Dci5OpURKmXGyfCIszRJ5iJUg6v1aRnn4SzdC_u-uVeMtgurHQBe4ua54s_h_puOZ_K6bsY8c87L8zp48R1E4Vbk1L89BRRQaFo_lGyDlFpfz-HNwd5hvmK_eADIxdEw1gn7iI9v4GHx_0Hn3Xliq14xW5RwGXcHY6CeBZ7hqho7BZiarq8WTweWtNuGVT8RDKtXrA3NZkooTjpijCiLYBv30xxsNsGQRwtJGLZ9rt8Uvit4mOlIIPadHPJAC2uujvJ5WH8PwSU3lbGy43xUAvAMOHnh36uABin6-8oYx-l7Yew84dSjpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور فرزندان رهبر شهید انقلاب در مراسم چهلمین روز تشییع و تدفین آقای شهید ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/682257" target="_blank">📅 17:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682256">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
پروژه رمزارزی ترامپ جنجالی شد/ ارتباط با شرکت چینی دردسرساز شد؟
🔹
پروژه ورلد لیبرتی فایننشال، پروژه ارز دیجیتال مورد حمایت خانواده دونالد ترامپ، به دلیل ارتباط با یک پلتفرم هوش مصنوعی که از مدل‌های توسعه‌یافته توسط شرکت‌های چینی استفاده می‌کند، با انتقاداتی روبه‌رو شده است.
🔹
بررسی‌ها نشان می‌دهد پلتفرم ورلد کلاو که با این پروژه همکاری دارد، میزبان مدل‌های هوش مصنوعی شرکت‌هایی مانند
علی‌بابا و بایدو است. این شرکت‌ها پیش‌تر از سوی وزارت دفاع آمریکا در فهرست نهادهای مرتبط با ارتش چین قرار گرفته‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/682256" target="_blank">📅 17:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682255">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7af673f51d.mp4?token=s7swJMDhYKLzv_rPODU1LIxMddIKP-y1G3NgRbwT90rw3f8iVPT49zv868YNacLptyJA72YCtedR7hmwHyRX-moWuE4JzX-u60-86R-YXEGc1I_R8Jm7ZUqj56XE7Ec3g3h2H6eZDdLaqJ0hkUAH0sYmI560zxZuT3_2yKJZYBnGxOL9txteYF85ZNC9zVhL3NE2pSvUUJFJvfAvFn6tuiptFpYpI0cfR0FBS2mdQABRH7Wgdm_x0-BNreevwAVXr1UZ6BOcdJkpvC5KERyjby8jjR1lC29U3kZEQwSV2VREiiqzCYDJk0R6URhRdDIPWxsv6syCaQ4rxU3Ofy6wkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7af673f51d.mp4?token=s7swJMDhYKLzv_rPODU1LIxMddIKP-y1G3NgRbwT90rw3f8iVPT49zv868YNacLptyJA72YCtedR7hmwHyRX-moWuE4JzX-u60-86R-YXEGc1I_R8Jm7ZUqj56XE7Ec3g3h2H6eZDdLaqJ0hkUAH0sYmI560zxZuT3_2yKJZYBnGxOL9txteYF85ZNC9zVhL3NE2pSvUUJFJvfAvFn6tuiptFpYpI0cfR0FBS2mdQABRH7Wgdm_x0-BNreevwAVXr1UZ6BOcdJkpvC5KERyjby8jjR1lC29U3kZEQwSV2VREiiqzCYDJk0R6URhRdDIPWxsv6syCaQ4rxU3Ofy6wkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم دلداده‌ای که برای شرکت در مراسم بزرگداشت چهلم «آقای شهید ایران» به مصلی تهران آمدند
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/682255" target="_blank">📅 17:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682254">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78251d66b1.mp4?token=Fi7AHA_bEL4l8gTwuYcWlvtLI1ubsJdtzY5vu2qJNO1JNRaFm9dZ3V1wo56IWxlMG0oKUofxdRTaMOAXu0KgLFBMzvWUOM2E6c9r6DY4Ca0QbhCfADhgBeSUM_WmoFWMj8XJ3i7jkCGFIbBI5ZNoBOJoBFHMpIoYzSTE-TEtlokjRy0AtEh1Bkg3YVJSAzZE3PT4Aa8m_mkJB1kiiaKp6cWJzWxHX1UPNfQ9Cds5nlt0smG4GC-T6CKb7feJWUlhYQBBf1XdZb6qkYvcaSD2haXzKUqmQj-V_k0VPrOHLoma6ZS95eemO-T4Bbw96tw6qyYOs2Dgt5ggHNUn69rPYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78251d66b1.mp4?token=Fi7AHA_bEL4l8gTwuYcWlvtLI1ubsJdtzY5vu2qJNO1JNRaFm9dZ3V1wo56IWxlMG0oKUofxdRTaMOAXu0KgLFBMzvWUOM2E6c9r6DY4Ca0QbhCfADhgBeSUM_WmoFWMj8XJ3i7jkCGFIbBI5ZNoBOJoBFHMpIoYzSTE-TEtlokjRy0AtEh1Bkg3YVJSAzZE3PT4Aa8m_mkJB1kiiaKp6cWJzWxHX1UPNfQ9Cds5nlt0smG4GC-T6CKb7feJWUlhYQBBf1XdZb6qkYvcaSD2haXzKUqmQj-V_k0VPrOHLoma6ZS95eemO-T4Bbw96tw6qyYOs2Dgt5ggHNUn69rPYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرود اضطراری جنگنده F-۱۵ ژاپن
🔹
یک فروند جنگنده F-۱۵J نیروی هوایی ژاپن پس از پایان مأموریت رهگیری، به دلیل نقص فنی در ارابه فرود، مجبور به انجام فرود اضطراری در فرودگاه ناها واقع در اوکیناوا شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/682254" target="_blank">📅 17:23 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682253">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8fcea082.mp4?token=m2Y-tGxODidkot7MtlBSyxrkwI4eTNS0_7-UW5uWVHdcYXc1VJPbIeCYvv3JvyR-GzKziNP4fGPUtiZhHppGDPj7PkKiGlD3TkCMN_XFYijoU-Hv1zKDMCD3M3rPdjRpYZsryrAjRhiIXUweLuSoIMzdBzzpDzfl3ftaqsLzL3G-hDPUcsiGL1nwYI64Z0hIL85pwSUb7SVR5EaUXUEjTB8UQtamz4otW1XU1QuIY7kcYV0hYLTnIPErCHPl55w12A4v1LDSDDUR7vNfkIf6oexm_pFXhGXK-rsw0XkGqRj2hn952l1s9r509_a6aHX9Jyun5XRH-E55CYmL2GdmSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8fcea082.mp4?token=m2Y-tGxODidkot7MtlBSyxrkwI4eTNS0_7-UW5uWVHdcYXc1VJPbIeCYvv3JvyR-GzKziNP4fGPUtiZhHppGDPj7PkKiGlD3TkCMN_XFYijoU-Hv1zKDMCD3M3rPdjRpYZsryrAjRhiIXUweLuSoIMzdBzzpDzfl3ftaqsLzL3G-hDPUcsiGL1nwYI64Z0hIL85pwSUb7SVR5EaUXUEjTB8UQtamz4otW1XU1QuIY7kcYV0hYLTnIPErCHPl55w12A4v1LDSDDUR7vNfkIf6oexm_pFXhGXK-rsw0XkGqRj2hn952l1s9r509_a6aHX9Jyun5XRH-E55CYmL2GdmSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور فرزندان رهبر شهید انقلاب در مراسم چهلمین روز تشییع و تدفین آقای شهید ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/682253" target="_blank">📅 17:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682252">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54846534cc.mp4?token=CqlYYMeM33Jn82NMM4hlMdMRWVUDZyxiu21KsIzM5JqgXRUc6PZX8YduJGyAV26xpv8dWi7y-ZSHGvUtTQ1pjzwGRaFIM5brotdtb_Qjv_EyiRjY-8MpxT69edn4RnqTGjdR8ST2at-zWawYpNMO3ckGuA6uSqEPc6pHLgLFMPXITi39V1tpn7TY_SeEX9kRRY8mxOvmHd46Gn_8JZBw0-Y1ap0wV_L9WVOmmk3E1kRBZ7S6W7NrfKBlfEa25Un-eCfVFH8Ka_seIahTU8K8ifPZ6PDrFE-p99VvcvbZNnS-Qaz_qV4YKUppKYvThudpioJnKvRFfTYRukDfX3G7s6A9EoZxfl-NK34IRor6LbrW-DYikI97YooT4yWnodhGVsJMBCCLjxrjAgcwTXr1uAWHXdFc6wOcgS6V3w9utD3tcfCnjY0senJiKK0HNCKrR1HaNNJvDrts3CuxELOWJXQoYXpuUEqg9rV6yq9FXMi0ZRJ-F4NyZHJdaHAaJgBGtBqahika_eEAwDhDgPaGZtE8hWo-azwF86RzoalCmPqzTWY-Q4Qhj60Q0wV4py3wkZ5FwMISV0ABE6RchbD2KVdD40s_2GsDSBPXlNyVW3-y_CPAbuykJuF_TM1I1LrBBQfLB_Fc8LKjFBOMo-cGq2HQtZXOYHxC_U8a307vKic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54846534cc.mp4?token=CqlYYMeM33Jn82NMM4hlMdMRWVUDZyxiu21KsIzM5JqgXRUc6PZX8YduJGyAV26xpv8dWi7y-ZSHGvUtTQ1pjzwGRaFIM5brotdtb_Qjv_EyiRjY-8MpxT69edn4RnqTGjdR8ST2at-zWawYpNMO3ckGuA6uSqEPc6pHLgLFMPXITi39V1tpn7TY_SeEX9kRRY8mxOvmHd46Gn_8JZBw0-Y1ap0wV_L9WVOmmk3E1kRBZ7S6W7NrfKBlfEa25Un-eCfVFH8Ka_seIahTU8K8ifPZ6PDrFE-p99VvcvbZNnS-Qaz_qV4YKUppKYvThudpioJnKvRFfTYRukDfX3G7s6A9EoZxfl-NK34IRor6LbrW-DYikI97YooT4yWnodhGVsJMBCCLjxrjAgcwTXr1uAWHXdFc6wOcgS6V3w9utD3tcfCnjY0senJiKK0HNCKrR1HaNNJvDrts3CuxELOWJXQoYXpuUEqg9rV6yq9FXMi0ZRJ-F4NyZHJdaHAaJgBGtBqahika_eEAwDhDgPaGZtE8hWo-azwF86RzoalCmPqzTWY-Q4Qhj60Q0wV4py3wkZ5FwMISV0ABE6RchbD2KVdD40s_2GsDSBPXlNyVW3-y_CPAbuykJuF_TM1I1LrBBQfLB_Fc8LKjFBOMo-cGq2HQtZXOYHxC_U8a307vKic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار حسن‌زاده: مردم تا زمانی که احساس کنند حضورشان لازم است در خیابان می‌مانند
فرمانده سپاه استان تهران:
🔹
مردم از همان آغاز جنگ با احساس مسئولیت در میادین حاضر شدند و تا زمانی که احساس کنند حضورشان ضرورت دارد، به حضور خود ادامه خواهند داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/682252" target="_blank">📅 17:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682250">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fE5y_MB4ag3Oyv-SBqc0gSDUcbTefrgID_mZUhsyhNSL00jxp5Ls3YhNRFvwolvVxsG28mQ5afFzNwqhvexVgLUKI28BLemfhFdy92XdpULCkcDz5v7uJADTYpE28NnZROxKEL47LKQs_V5sJyTI8LP4LovHcCkGoaVqlxU2HOUhF94NEeJ8AxpCLoT4bH16Bj0YY5qARjOlpk4EMzW7u5bvINOdS8erReXWpTvrZhxekOYVFlGyZjw9wqmdtalUhRgkmyvAbdPwadIYY85l3KW-4D3wWZPd154md4wa1qnUCZVbMPFrV31h8fRrVfsoyPmcm1KPT2OttdtnZ2sGfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان رسمی توافق ۶۰ روزه ایران و آمریکا/ حالا چه می شود؛ جنگ یا توافق جدید؟
🔹
پایان توافق ۶۰ روزه سبب شده که برخی از تحلیلگران و کارشناسان از پایان یک دوره سخن بگویند؛ دوره ای پرفراز و نشیب و پر از حادثه که اگرچه سست و لرزان بود اما به هر روی، توانست سبب تفوق دیپلماسی بر جنگ، اختلاف و چالش سخت شود. اما بعد از پایان این توافق، چه می شود؟
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3238348</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/682250" target="_blank">📅 17:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682249">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcmQmQxwQnmJEBC4PTCjHcM_5j4ODfdegFq9Hsw-c1PdyfxcYBi6d2gEmfT14rhPDjUfWCmp9qGyGuJ3d3hJVQYa9q41klVfG9CJTDD4R7JFlSspNs2NmrsHsjAj5xWU0K4CpHTTKmW0kfyueUr62chjlKOpJGmdkF_kDJhtE_XhqBV-LlRLfRGa4TthMyhef6BXk3zORBqLcWH6NF7ALvsqp29aAzf-qk6y0XQDaSHDzz_z0EmkIHGCML3cUv0Jqe1BNH5iSZxtKNWgqh8GRyAjDhxAkt7E46RaIaSp2GAYOcuf2-PnwrZgU-E51yMU_yXfHwyWdlVjcvEx8Gp76Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ قمارباز: هیچ مذاکره‌ای با ایران نداریم؛ محاصره کامل پابرجاست
ادعای ترامپ:
🔹
در حال حاضر هیچ مذاکره یا گفت‌وگویی با ایران در حال انجام یا برنامه‌ریزی نیست
🔹
محاصره دریایی با قدرت و به طور مؤثر ادامه دارد و تنگه هرمز باز است و کار در آنجا ادامه دارد.
🔹
محاصره دریایی ایران به طور کامل پابرجاست.
🔹
تنگه هرمز باز و عملیاتی است و تمام مین‌های دریایی جمع‌آوری یا منفجر شده‌اند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/682249" target="_blank">📅 17:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682248">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر بهداشت: سالی ۵٠ هزار مرگ و میر به علت آلودکی هوا اتفاق می‌افتد.
🔹
فرمانده ارتش لبنان: رژیم صهیونیستی همچنان به تجاوزات و نقض توافق‌های موجود ادامه می‌دهد.
🔹
اکسیوس: انتخابات اسرائیل برای ترامپ از اهمیت بالایی برخوردار است.
🔹
سوریه انتقال مواد هسته‌ای به خارج از کشور را رد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/682248" target="_blank">📅 17:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682247">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwOGEjCSnznW0LngHXLl4dDOzaln9TgRnN8VHnYiEpst9UsX9o7SAI14NXeCblnK4YbHQQPDUyIbGvt4gBmTMVwiiXgdwCUGba-7iaxlTcygRGwkf3jgDuHV5folITUehtgpmma9PU2-pFkNy5fFLah3PKPMpfcivPsNKimIHW3yH3xVjFDskOQs7zbbKtknbpgIWjRCPqPgInE6l4yeng6wYPt7KB3av0kfEkXFmDlW5YcsTvYSSfAPFJXuSmEOWy12uBwGSFDlzG1Ti-nvrYPdZbfhkXgIfstF6blljHburQJVDj3C8rqDKQF7MP-QTVeDAhRLB32W_ZhWUmto4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ مورد رو موقع مسواک زدن رعایت کنین
🪥
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/682247" target="_blank">📅 17:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682246">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
پولیتیکو
:
ادعاهای ترامپ در مورد تنگه هرمز با داده‌های تردد نفتکش‌ها در تضاد است
پولیتیکو:
🔹
دولت ترامپ مدعی است که تنگه هرمز برای تجارت باز است و عبور و مرور نفتکش‌ها در جریان است. این در حالی است که ردیاب‌های بازار تصویر نه چندان خوش‌بینانه‌ای را نشان می‌دهند.
🔹
کارشناسان می‌گویند که نمی‌توان به ارقام دولت ترامپ اعتماد کرد زیرا هیچ داده‌ای وجود ندارد که نشان دهد واقعاً حجم نفت از طریق تنگه هرمز در حال حرکت است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/682246" target="_blank">📅 16:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682245">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
هشدار سازمان غذا و دارو درباره عرضه یک داروی ضدسرطان تقلبی در بازار
🔹
سازمان غذا و دارو از شناسایی فرآورده تقلبی «ضد سرطان» با دُز ۱۴۰ میلی‌گرم و سری ساخت H6980H05 در بازار دارویی ایران خبر داد و خواستار جمع‌آوری فوری آن شد.
🔹
پولیوی «Polivy» در شکل دارویی پودر برای تهیه محلول تزریقی عرضه می‌شود و دُز ۱۴۰ میلی‌گرمی آن نیز در منابع دارویی ثبت شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/682245" target="_blank">📅 16:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682243">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7QsHudAmtY488Lkjr40I9nkBs1yU1qkPvyT2QQaAjGqIWafsUkaTqgbnt92DxWqaI_nYDtXKBHzVVoKJhgrGdc5qt4K2CmcKF0NjFQ9-UYlwqJX7f9SGoeezobvgIKRmQg6aYFUWS-CW3Lt87oj9qAMILgYhFbqtcxA6L1ESgpfo7iHZCP0EM-B_ohdbkIVKb7OhToK4I4CN6z6OR6SjmP7Uu5a-Q413meyc-LJiztAwgJWb_NxgkmG_Qf9edPnBf6R6hPlqLXVLBKUX0HyastCBOr13cxZZn_7gvXXIiUULa_7kxZ_WYEAF_SfOKEUvDwwL96c-43rZFhvvXC6uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-CV2jLc3ftZDkWd7_-TwF609YJLjRdOwVGdOLliKuqMr7yggGSurlarlL5Od-yyyRxqFcpfNgm26bXgnHHUgxqIt6JwOlF2fKBMbxga5JXwU6PleLAxsiVj5iaNIFJWUhQuZybDgECoRTx_t22a30enKFsoIL4tTwrPMbvCqw7F8L9eTvdiUKkjJ36gnnpmm0hKLwm8iK5LdyLw6TwLKvMJIh0eym-gjokO_OTKOvlot_lUVtCMwD0AoTXFRERHEbw1lxRS8CdFQx2SnCmqwOr7ThrIfPZtH1hIn2IZ2t11QlBTOboLmp1DgvI7ZxDswjLt-M-VFXyqAMlGZ24_6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جزئیات توافق رونالدو و جورجینا: در صورت جدایی، جورجینا ماهانه ۱۰۰ هزار یورو تا پایان عمر دریافت می‌کند و مالکیت خانه‌شان در مادرید، به ارزش تقریبی ۶ میلیون یورو نیز به او واگذار خواهد شد
🔹
این توافق همچنین از سرمایه‌گذاری‌های شخصی رونالدو محافظت می‌کند…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/682243" target="_blank">📅 16:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682242">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
محمولۀ مواد مخدر و مهمات از مرز رد نشد
🔹
مرزبانان سیستان‌‌وبلوچستان با شناسایی محل اختفای قاچاقچیان مسلح، موفق به کشف ۹۶۴ کیلوگرم موادمخدر شدند.
🔹
در این عملیات همچنین ۲ خودرو، ۵ گلوله آرپی‌جی۷ و ۳۰ نارنجک دستی کشف و یک نفر از قاچاقچیان نیز دستگیر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/682242" target="_blank">📅 16:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682241">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIfn4uNbGeVQ9SKTba6LdGEskS9n_u5_wFUl8HkXvh4iCwwNrVnarCCGtpMfca5CnvafYkG_5OxwOLMsw0C60QCpEcg2iG-gXoTMiIt_vPMtfgu0Yh0BPoyN4dk_nOJDcyYHEjgq5efj6_Pw8Zu2-HDyyguOGvj50Nf9uOtH9TSxszK-WESN27DI68NoVbptTaRYboy1BWUsqMgT4RyzNtztSdcb_lchbJg-6na_rpdYZ7ajMPs9AJD7_4eotWiYj1wqlT-JQVY3jiKeRetkQect87zDXd2qa5yZgb_gs5NFsC6u7Z_Jlp3sSNu0njrrGbmbRAJpVzql1lgA_LoNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش نرخ ۸۲ قلم دارو
/
رشد ۱۲۰ درصدی میانگین قیمت آنتی‌بیوتیک‌ها
🔹
در میان اقلام مشمول افزایش قیمت، قرص دنپزیل با افزایش نرخ حدود ۵۴۳ درصدی در صدر قرار دارد. همچنین نرخ کلاریترومایسین حدود ۳۰۸ درصد افزایش یافته است. نرخ آموکسی‌کلاو حدود ۱۱۵ درصد، کولیک اسید حدود ۱۸۴ درصد و شربت استامینوفن و دیفن‌هیدرامین حدود ۱۳۵ درصد افزایش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/682241" target="_blank">📅 16:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682240">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87eca95a3a.mp4?token=vKAZou02zDRW4Tqa68ju2kdkoqZYLkEYK9wp_OJhOtUIPwI1_aIZFLl-p8iNDhtBu5rw56Lfmg4xHyD9Wis1Ow_7mUTlJVoRReM_WpFm1mTJQbsHCngCT1qVyS_U7XUqcttnh1r5_59VbS_IL6hn-sGI_kSLeSXy_6S5qEKI6Cb0VfmVQbtrvtYmatjQUf2TdFZQdDb_RQghluMyB11C-6-l9zi83I2fpNEgzTVtBBdYm78FiV5V6VG0vJBTKJQU0Nx29FRv8ZluGUy-63LaaGuhgmsc5OfcMJJFPjCyQxcCzKLD2LOBhnnQLNbrR99tOjA5y11W1XARDgvcMMixJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87eca95a3a.mp4?token=vKAZou02zDRW4Tqa68ju2kdkoqZYLkEYK9wp_OJhOtUIPwI1_aIZFLl-p8iNDhtBu5rw56Lfmg4xHyD9Wis1Ow_7mUTlJVoRReM_WpFm1mTJQbsHCngCT1qVyS_U7XUqcttnh1r5_59VbS_IL6hn-sGI_kSLeSXy_6S5qEKI6Cb0VfmVQbtrvtYmatjQUf2TdFZQdDb_RQghluMyB11C-6-l9zi83I2fpNEgzTVtBBdYm78FiV5V6VG0vJBTKJQU0Nx29FRv8ZluGUy-63LaaGuhgmsc5OfcMJJFPjCyQxcCzKLD2LOBhnnQLNbrR99tOjA5y11W1XARDgvcMMixJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دهه‌ بیست‌ تا سی سالگی نقش پررنگی در آینده مالی خانم‌ها داره و اگر حواسمون به بعضی اشتباهات مالی نباشه تا آخر عمر دنبالمون میاد #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/682240" target="_blank">📅 16:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682239">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCT5DCdVmVGfG_KVds7IMygel9EPbJ198FluhfS-8nS6JNctRNy7sU3lCmbDsF2byK-t7pjLKxV555u1Ime05xBbu8qD73fvnD4Ix0Ya6CttyijI3Htk_p8J4jCITsC6_Wurk156lZHgdvEN1WQd_X5Js76J-RjUFXFIopz0MHuBwawdjuSd8sLtwpWBOBJtaH7sH3wT1l7rDYVkGLQNRDO24aRamax5Bj5SmiPVAGDXKYhSgF6M0nNtg5uwBMUFoOQ-Jcfumg5Z1sM1T_OFsfiIsLvASnL8y8vF19smSYwrJdMPlXkVI_XNiJOGS7aoygwBR6avSjx8DxPYbyv1gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حداقل و حداکثر حقوق بازنشستگان صندوق کشوری اعلام شد
🔹
طبق آخرین آمار صندوق بازنشستگی کشوری، حداقل حقوق با ۳۰ سال سابقه ۱۶.۸ میلیون تومان و برای سابقه کمتر از ۳۰ سال ۸.۴ میلیون تومان است؛ حداکثر حقوق نیز ۷۹.۸ میلیون تومان و بیشتر اعلام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/682239" target="_blank">📅 15:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682238">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dca9c54e6.mp4?token=UxV7Hqz3g4_OYvMpNDxBBpBWd3Spmj3pSWoN3HJMxpOUflYgRIXeKkX-BQuOdF2Tu_E1weE2DSKpudyUZa8xgMbGMTQsbgBHiVewKEiet0a4n-TZpEuQvZBuHDgvkvkCyv7qGNi3GEUgcx0CtMXRwB8FU1BrJFYHSmoPPkMVQ4V1oY7Bc4piDIWEVhfOuOh62I0v5U4rwuC_kGOFXbytNsiDerhv3hDmhiWpAb5MkPmtehB6jK_OtrHLiXhcJH96NKKoX_cxgFrXX-YX6naTWEppbZQNL310awBHmbkOTbMobFOWyOXnxpnu4G5EX2e0lrwG2g_sVSBA5ST82Muyqi8JhKKmrD7CZLlf6n2VxJpaKFq00CDDKwzNKkYNW4ucYlxUiflqvfW0ahOBnX3bZmRqMRuqOKFSPw1oJW6RCWZta0MYlP331pX3sGDXFQkxezuBM5t7s4SCymAHtRVOU5ze3A3DH-jJhPu2BJomzsXMkOlvqtu9KIrRdY-_t6hnd8YuCDjporpJ2Eke6WVpS4AmpRKXftvM3BXNWWOcgdGwAR-WKD1o88imIpIVX9CSbQ-CJaw3QZMU7Tg7Y7MaRFJ9OAZ_TURv1QiX-BuxFA8-rXC_hZKx5_B2uXQeHqMl4vD55bJRV_3K53CV27etXcMn2l1FoPfMpW4toapa19w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dca9c54e6.mp4?token=UxV7Hqz3g4_OYvMpNDxBBpBWd3Spmj3pSWoN3HJMxpOUflYgRIXeKkX-BQuOdF2Tu_E1weE2DSKpudyUZa8xgMbGMTQsbgBHiVewKEiet0a4n-TZpEuQvZBuHDgvkvkCyv7qGNi3GEUgcx0CtMXRwB8FU1BrJFYHSmoPPkMVQ4V1oY7Bc4piDIWEVhfOuOh62I0v5U4rwuC_kGOFXbytNsiDerhv3hDmhiWpAb5MkPmtehB6jK_OtrHLiXhcJH96NKKoX_cxgFrXX-YX6naTWEppbZQNL310awBHmbkOTbMobFOWyOXnxpnu4G5EX2e0lrwG2g_sVSBA5ST82Muyqi8JhKKmrD7CZLlf6n2VxJpaKFq00CDDKwzNKkYNW4ucYlxUiflqvfW0ahOBnX3bZmRqMRuqOKFSPw1oJW6RCWZta0MYlP331pX3sGDXFQkxezuBM5t7s4SCymAHtRVOU5ze3A3DH-jJhPu2BJomzsXMkOlvqtu9KIrRdY-_t6hnd8YuCDjporpJ2Eke6WVpS4AmpRKXftvM3BXNWWOcgdGwAR-WKD1o88imIpIVX9CSbQ-CJaw3QZMU7Tg7Y7MaRFJ9OAZ_TURv1QiX-BuxFA8-rXC_hZKx5_B2uXQeHqMl4vD55bJRV_3K53CV27etXcMn2l1FoPfMpW4toapa19w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراض نمادین به جنایات رژیم صهیونیستی در مقابل سفارت این رژیم در واشنگتن
🔹
فعالان ضدجنگ در واشنگتن با اقدامی نمادین، خشم خود را نسبت به استمرار کشتار غیرنظامیان در نوار غزه نشان دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/682238" target="_blank">📅 15:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682237">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
از کمیسیون صفر تا خانه‌های بازسازی‌شده؛ اسنپ چطور پای زنان ایستاد؟
رکنا نوشت:
🔹
حمایت از زنان در سال‌های اخیر از سطح کمک‌های مقطعی فراتر رفته و به یکی از محورهای مهم برنامه‌های مسئولیت اجتماعی شرکت‌ها تبدیل شده است.
🔹
در این میان، اسنپ اعلام کرده است که با اجرای بیش از ۱۶ طرح در حوزه آموزش، اشتغال، سلامت، توانمندسازی و حمایت اجتماعی، بیش از ۵ هزار و ۴۰۰ زن و دختر را در نقاط مختلف کشور تحت پوشش اقدامات اجتماعی خود قرار داده است؛ اقداماتی که از حمایت از زنان سرپرست خانوار و ایجاد فرصت‌های شغلی تا آموزش دختران و حمایت از زنان آسیب‌دیده از خشونت را در برمی‌گیرد.
🔹
یکی از تازه‌ترین اقدامات اسنپ، مشارکت در تهیه و بازسازی ۲۰ خانه آسیب‌دیده از جنگ برای زنان سرپرست خانوار در هرمزگان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/682237" target="_blank">📅 15:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682236">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e305080a.mp4?token=EFXyIeQc_hsNl7-l4Ut7lXYYWmyf10c9_MkeTmB-2ICj6UlwD4Zq2qiygT4n_JRS0TvJuVtFzoOG1OAdwzpRxDB9JFREpDcHx6TfuNax8YywOmuF3SJmmXerm7793RbQNDUajSkmXi2t9ScUiroCMX4VGhrUfKAH4ssfFIoP0ZSlmLCgv3v2zgFkgUNGMsu8nDmOJmAaWTyxBYkhI60-YJpnOpdSAz8p5tNC-2z_tXHjcIPDBqgHnB-xnKOWVGbBEslG_bdTUypLfxDCLo1_UvXHDsS2hQ33VtakeY71YQd8Rmk3tQRX4aDe5g2UTfT1G4yknCcofFrN9Nbq-z57_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e305080a.mp4?token=EFXyIeQc_hsNl7-l4Ut7lXYYWmyf10c9_MkeTmB-2ICj6UlwD4Zq2qiygT4n_JRS0TvJuVtFzoOG1OAdwzpRxDB9JFREpDcHx6TfuNax8YywOmuF3SJmmXerm7793RbQNDUajSkmXi2t9ScUiroCMX4VGhrUfKAH4ssfFIoP0ZSlmLCgv3v2zgFkgUNGMsu8nDmOJmAaWTyxBYkhI60-YJpnOpdSAz8p5tNC-2z_tXHjcIPDBqgHnB-xnKOWVGbBEslG_bdTUypLfxDCLo1_UvXHDsS2hQ33VtakeY71YQd8Rmk3tQRX4aDe5g2UTfT1G4yknCcofFrN9Nbq-z57_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفتار صحیح با مواد غذایی به زبون خودشون
😀
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/682236" target="_blank">📅 15:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682235">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff225759e5.mp4?token=nAwJXPuNHAHSU2GiBeN9HzBEtqCQ89IFgzZa43kMKDfYKagQ3r2uRVDLDDMJ7PLe0jAH206qT0T71a6blG1xlQyoUR-9KetrGnpkJFdGTKU4MvOzFjz42_M4n48mHALz-7RVXm8rGuGl-OJiE-VLZYdP2YBVFOajGnFjf9s_2YpoGSr78TOASblm9Zw3Qx0bw36di20vYnwhTFFz5T6Fc-hGOiXX8LCGi1W5d1KuEz2dzcjaLEEjSQpi_lVido2zjjdePULA59jvd7LWuwum9DqmGBkEbM9qGIBmxHzYT0KEcRctUroI6NSuQa9snabodDM66Yb6BLVFYtAneKrGmYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff225759e5.mp4?token=nAwJXPuNHAHSU2GiBeN9HzBEtqCQ89IFgzZa43kMKDfYKagQ3r2uRVDLDDMJ7PLe0jAH206qT0T71a6blG1xlQyoUR-9KetrGnpkJFdGTKU4MvOzFjz42_M4n48mHALz-7RVXm8rGuGl-OJiE-VLZYdP2YBVFOajGnFjf9s_2YpoGSr78TOASblm9Zw3Qx0bw36di20vYnwhTFFz5T6Fc-hGOiXX8LCGi1W5d1KuEz2dzcjaLEEjSQpi_lVido2zjjdePULA59jvd7LWuwum9DqmGBkEbM9qGIBmxHzYT0KEcRctUroI6NSuQa9snabodDM66Yb6BLVFYtAneKrGmYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: حامی اصلی ما در مسیر مذاکرات، رئيس‌جمهور بود
🔹
وقتی آمریکایی‌ها درخواست مذاکره را مطرح کردند، پزشکیان معتقد بود باید از همین طریق راهی را برای پایان جنگ پیدا کنیم.
🔹
انتخاب قالیباف در تیم مذاکرات به‌پیشنهاد رئیس‌جمهور بود و حتی در صورت‌جلسه‌ای که تهیه شد پزشکیان اصرار داشت که «باید نام آقای قالیباف به‌عنوان مسئول مذاکرات نوشته شود تا من امضا کنم».
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/682235" target="_blank">📅 15:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682234">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab02ee3fce.mp4?token=L_xmhFgKRm1LBG5hTUS28hENEnJuVArdaJp0PWPNq4OOyovih4RFmtoEd_B36FZ7XNi0l63pkIqR4rdZ87S29OU0qrnzwO1Abf_j1oNXlcWrb2a-WDFpc1PQPOs6nMNebbfh66jke-9i_LZEVtYzWlv47nWm9tjYC7GScMG0SoMaI5VeQz9ftXOQCKY0STG7g39Hzr962ZigekHT3LOypGxbX0Zm0kqaXRrRi7kwoiLhIoHqCdZsCSYnBV42vU4i9SkUGLzq7gOpcgZDXDxe-30eYjt0NUPFoBUSl8Xcu-FaQTSOCgX3vQ5yt0BLSMaOD2oZ9wbfIVTjpdWOYmkgOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab02ee3fce.mp4?token=L_xmhFgKRm1LBG5hTUS28hENEnJuVArdaJp0PWPNq4OOyovih4RFmtoEd_B36FZ7XNi0l63pkIqR4rdZ87S29OU0qrnzwO1Abf_j1oNXlcWrb2a-WDFpc1PQPOs6nMNebbfh66jke-9i_LZEVtYzWlv47nWm9tjYC7GScMG0SoMaI5VeQz9ftXOQCKY0STG7g39Hzr962ZigekHT3LOypGxbX0Zm0kqaXRrRi7kwoiLhIoHqCdZsCSYnBV42vU4i9SkUGLzq7gOpcgZDXDxe-30eYjt0NUPFoBUSl8Xcu-FaQTSOCgX3vQ5yt0BLSMaOD2oZ9wbfIVTjpdWOYmkgOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط با یک نخ و سوزن لباس‌تون رو به سبک پینترست استایل کنید
😍
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/682234" target="_blank">📅 15:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682232">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdjXD4kKWAEs2VAZpLFur8Ovp5-cSp6edJfHkyy4yfIZ-coCj5YEv-pHH1-UpeXG3feE4-6Itj6ztBPyCc1BlfitBAPP2yJelOMRnKFg9L3UkdD8ZHMfQlJC0HTdGJnkZY7MhtQEgBVHDoDhcAXQsBedWz23xmCTqxkE9hQAk9uzxhIDM8LrnTbx_tese0XQIz6vP4yR81D3uI-Rv6PsQO0pe4hIV8CtS8b4JjIXxy9PrL96u21-udHP2gIUw9UdvFbyZ0Gpnm1uag71PXVI0L2VORM_pgsGP0v7ezAW4mqhyY6250Hspe8iS6EFs0LAi3i2qo5yXA6CSJyE7te1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
صندوق نقره «یاس» چهارشنبه ۲۸ مرداد پذیره‌نویسی می‌شود
صندوق «یاس» جدید‌ترین صندوق نقره، چهارشنبه ۲۸ مرداد ساعت ۱۱:۴۵ از طریق تمامی کارگزاری‌های بورسی پذیره‌نویسی می‌شود.
در حالی که میانگین حباب صندوق‌های نقره به ۱۲ درصد رسیده است، این پذیره‌نویسی سرمایه‌گذاری با حباب صفر را فراهم می‌کند.
⭕️
اطلاعات بیشتر و آموزش شرکت در پذیره‌نویسی را اینجا بخوانید.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/682232" target="_blank">📅 15:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682231">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeXJKvB9KXSbyQ_X1n6J7dW9G_lqqnzie9JKpXef70DgNf3vO2-3IbOVdGa9plSJ0L_1bBFX-9G37A7se38c59n8cO5lFAEmnOxITiDdvL9LTw7twzAjgT3oSzrIZ9B1ZJZjDpIHF4ThcEYjekVP5iXPsaHM4-Ukcp_fq3cxfHN3hUcwY7xTZukmFK9y7mSZGxCNqqdu9i0NPO5Oe8ldbgIxI24G2LmzBDcApOBDm-RYN2vJcAMV7av_bt5-aNolgnHYfTUu7z7kAvQiBG9hzZ2xcaPlJs8LfcSaGT8_23z4YeMir6f-EupkaZfVFoQl2gZCmVWaIH3V4E_FWCajgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیاده‌گویی ترامپ قمارباز در تروث سوشال: تنگه هرمز؛ قلمرو جدید ایالات متحده #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/682231" target="_blank">📅 15:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682228">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsqEugslXIdfrF1n4PhB3BwEEXkEPi3iZdBksV7wpU7TeSh7dqTgr1zrwOnfSFupRCHrTo98EPuC5mAnRQkl0nZ0kvMWwUlJf8yRT0LjpT3zYq__YxsbGNpaMnvCX48Rz3MouZjgKcVZs1cjQ4KoGHhTfa2laQiPHZrTbm4Ji1U3FK9AEAceSUGSdA8IdGg2jp_-F0rN-SK0wJ52WoGXqNz7Efsy2hfq16BOfgi54c5DGTWeeoC1iUvVWkGtSUncFsiZF4FWWrbDI6l3SqCJrTXFvBaa0vIi1DsCh_WtPAPLmgun1lbpEl7hQCMEpnn-3vhSHLr9Fvr5M7Tsx2YZeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیاده‌گویی ترامپ قمارباز در تروث سوشال: تنگه هرمز؛ قلمرو جدید ایالات متحده
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/682228" target="_blank">📅 14:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682227">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه قطر: میانجی‌گران منتظرند عمان و ایران ابتدا به یک توافق دوجانبه درباره تنگه هرمز دست پیدا کنند و سپس به مذاکرات گسترده‌تر بازگردند
🔹
در مذاکرات عمان و ایران هیچ تحول جدیدی رخ نداده و منتظر دستیابی آنها به توافق هستیم.
🔹
دستیابی به توافقی درباره تنگه هرمز می‌تواند ازسرگیری مذاکرات ایران و آمریکا را تا حد زیادی تسهیل کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/682227" target="_blank">📅 14:49 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
