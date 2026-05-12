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
<img src="https://cdn4.telesco.pe/file/GmlbRDIKhn0Ussu6ZWHH711tuSxn5XFd2GfIQma6718jGpdhPOM-nAp1soCxEWmuefnG2OFVHOpXsTc1-I3vV7sfnyFsg4QKKxDCfO4w7_E80i_STTIe71z6r4l-vFW8g0nXFMwTsaQ_uVMYkSZMAtSKZFNwgqZbfQXm_HG8Nck9oFO5wGeCnllRF96ZjMR0N-3wBIqt40QuLLVgUQCxKbFWT2W_uzR0_wbsTxmNTYaxhFFfT3jZypBfYmEGA2z_17PGM7pAbZw1JQ-euTR9iLPpUVIW7o3TiQwblORa1W9zR5-obTpO3GtoDUzWJW3GIyLVR91OYzRJG5kaxa81QA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 21:28:40</div>
<hr>

<div class="tg-post" id="msg-435174">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خبرگزاری فارس
pinned «
یک منبع آگاه به فارس: ایران بدون انجام ۵ شرط اعتمادساز وارد دور دوم مذاکرات با آمریکا نمی‌شود
🔹
یک منبع آگاه تأکید کرد که پیش‌شرط‌های اعلامی ایران، تضامین حداقلی اعتمادساز برای آغاز هرگونه مذاکره با آمریکا است.
🔹
پنج پیش‌شرط ایران برای طرف آمریکایی شامل «پایان…
»</div>
<div class="tg-footer"><a href="https://t.me/farsna/435174" target="_blank">📅 21:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435173">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یک منبع آگاه به فارس: ایران بدون انجام ۵ شرط اعتمادساز وارد دور دوم مذاکرات با آمریکا نمی‌شود
🔹
یک منبع آگاه تأکید کرد که پیش‌شرط‌های اعلامی ایران، تضامین حداقلی اعتمادساز برای آغاز هرگونه مذاکره با آمریکا است.
🔹
پنج پیش‌شرط ایران برای طرف آمریکایی شامل «پایان جنگ در همه جبهه‌ها به‌ویژه لبنان»، «رفع تحریم‌های ضدایرانی»، «آزادسازی پول‌های بلوکه‌شده ایران»، «جبران خسارات ناشی از جنگ» و «پذیرش حق حاکمیت ایران بر تنگه هرمز» می باشد.
🔹
ایران همچنین به میانجی پاکستانی اعلام کرده است که تداوم محاصره دریایی در محدوده دریای عرب و خلیج عمان پس از برقراری آتش‌بس، گزاره غیرقابل اعتماد بودن مذاکره با آمریکا را بیش از پیش تقویت کرده است.
🔹
بنا بر اعلام این منبع آگاه، مجموعه این شروط صرفاً در چارچوب ایجاد حداقل اعتماد برای بازگشت به روند گفت‌وگوها تعریف شده و تهران معتقد است بدون تحقق عملی این موارد، امکان ورود به مذاکرات جدید وجود نخواهد داشت.
🔹
بر اساس اطلاعات به‌دست‌آمده توسط خبرنگار فارس، ایران این پیش شرطهای ۵ گانه را در پاسخ به پیشنهاد ۱۴بندی آمریکا معین کرده است؛ پیشنهاداتی که به گفته منابع آگاه، کاملاً یک‌طرفه و در راستای تأمین منافع واشنگتن تنظیم شده بود. به گفته این منابع، آمریکایی‌ها در این پیشنهاد تلاش داشتند اهدافی را که در جنگ محقق نکرده بودند، از مسیر مذاکرات به دست آورند.
@Farsna</div>
<div class="tg-footer">👁️ 297 · <a href="https://t.me/farsna/435173" target="_blank">📅 21:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435172">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37dea67a11.mp4?token=LqQV2_yVvCsjdzJfuqd_Z3aYWqNNzIp7ujeVBOQ5w8v-abJzbRHQW1QLL5J8ThjAaLbc3wIHSk7E5gfzKzDabHkIgLjZYHmpPxfjb-6mM1VaW-uIHYGV4-ZfpqYnNXOWN6mUD1XSWxFSuWt5FdI0UswUhfw6oRM4gUZ4PVXvFK4NiCF0WveVXxZ8dW1gPJV35vXmes3LgeBjgwEQumiWobE5eY1izvtYbzUHGmzGLF-wYWuUuupdOgwxkG9sr365UU2SL6N8IgOtvAZN8WAXz9mGUQG-bOaxa9i9Jw8TbgmEmdeD32WFgt8KXu_mVkBdYMjpmKm8Z5LG6uBuqU5G7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37dea67a11.mp4?token=LqQV2_yVvCsjdzJfuqd_Z3aYWqNNzIp7ujeVBOQ5w8v-abJzbRHQW1QLL5J8ThjAaLbc3wIHSk7E5gfzKzDabHkIgLjZYHmpPxfjb-6mM1VaW-uIHYGV4-ZfpqYnNXOWN6mUD1XSWxFSuWt5FdI0UswUhfw6oRM4gUZ4PVXvFK4NiCF0WveVXxZ8dW1gPJV35vXmes3LgeBjgwEQumiWobE5eY1izvtYbzUHGmzGLF-wYWuUuupdOgwxkG9sr365UU2SL6N8IgOtvAZN8WAXz9mGUQG-bOaxa9i9Jw8TbgmEmdeD32WFgt8KXu_mVkBdYMjpmKm8Z5LG6uBuqU5G7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظهٔ اصابت موشک حزب‌الله به محل استقرار  نظامیان صهیونیست
@Farsna</div>
<div class="tg-footer">👁️ 310 · <a href="https://t.me/farsna/435172" target="_blank">📅 21:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435171">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تهران طوفانی شد
🔹
هواشناسی: از ساعتی پیش، وزش باد ۵۵ کیلومتر بر ساعت همراه با گردوخاک در تهران آغاز شده است.
🔹
توصیه می‌شود شهروندان از تردد غیرضروری در فضاهای باز و ماندن در مجاورت درختان کهنسال، سازه‌های موقت و تأسیسات ناپایدار خودداری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 662 · <a href="https://t.me/farsna/435171" target="_blank">📅 21:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435170">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299a972263.mp4?token=MAueGj6R9KdEAwWKJqCrv5qdt2RZyGEQPQT79CxrAUQLqEAJVkcf5KYsILXEFlayR0y355hrSkqhWtb-_k44U5-45f4404y9mMiBUDTeUWbxxwQnRcgC6EJlmA5qS0mpGyK2cVoqfUyGWIkCcWq5svA_nXK1eZcHU5ytNglChWG22v78RKHPySfqYjiaUi6UsOnkDGz98FF58oW0C-vOr2WYLf7HdC0c-q61cTuDYyiwet1j5OcOdZBJ-B8yN6VUFYCJuGhQfZZQVEBisZfh7ZtPTZyfcoPdRKV8vIUrVZ_cUfwsu5JKIXAfKTQ_95B-INXGdx26DiO1IKUwfVS7ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299a972263.mp4?token=MAueGj6R9KdEAwWKJqCrv5qdt2RZyGEQPQT79CxrAUQLqEAJVkcf5KYsILXEFlayR0y355hrSkqhWtb-_k44U5-45f4404y9mMiBUDTeUWbxxwQnRcgC6EJlmA5qS0mpGyK2cVoqfUyGWIkCcWq5svA_nXK1eZcHU5ytNglChWG22v78RKHPySfqYjiaUi6UsOnkDGz98FF58oW0C-vOr2WYLf7HdC0c-q61cTuDYyiwet1j5OcOdZBJ-B8yN6VUFYCJuGhQfZZQVEBisZfh7ZtPTZyfcoPdRKV8vIUrVZ_cUfwsu5JKIXAfKTQ_95B-INXGdx26DiO1IKUwfVS7ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تروریست آموزش‌دیدۀ گروهک تروریستی انصارالفرقان اعدام شد
🔹
رئیس دادگستری سیستان‌وبلوچستان: بامداد امروز حکم اعدام عبدالجلیل شه‌بخش فرزند جلال، عنصر آموزش‌دیدۀ گروهک تروریستی انصارالفرقان اجرا شد.
🔹
در پی بازداشت عبدالجلیل شه‌بخش در جریان اقدامات ضدتروریستی…</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/farsna/435170" target="_blank">📅 21:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435169">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">افزایش حقوق بازنشستگان تأمین اجتماعی امروز تعیین تکلیف می‌شود
🔹
خبرنگار فارس کسب اطلاع کرد، تکلیف افزایش حقوق و زمان پرداخت ۳۰ درصد باقیماندۀ همسان‌سازی بازنشستگان تأمین اجتماعی در سال ۱۴۰۵، احتمالا در نشست مشترک سه‌شنبۀ مدیران سازمان و نمایندگان کانون‌ها…</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/farsna/435169" target="_blank">📅 21:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435168">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">معاون وزیر خارجه: رویکرد فعلی آمریکا مذاکره نیست، اجبار است
🔹
غریب‌آبادی: تاکید ایران بر اصولی روشن است: توقف دائمی جنگ و عدم تکرار آن، جبران خسارات، رفع محاصره، رفع تحریم‌های غیرقانونی و احترام به حقوق ایران.
🔹
نمی‌توان هم‌زمان از آتش‌بس سخن گفت و محاصره را ادامه داد؛ از دیپلماسی گفت و تحریم را تشدید کرد؛ از ثبات منطقه‌ای حرف زد و به رژیمی که منشأ تجاوز و بی‌ثباتی است، پشتیبانی سیاسی و نظامی ارائه کرد.
🔹
چنین رویکردی، مذاکره نیست؛ ادامه سیاست اجبار با واژگان دیپلماتیک است.
@Farsna</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/farsna/435168" target="_blank">📅 21:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435166">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682dd68c95.mp4?token=MyWNhvN5NWXBLWlZZyO5ibnZhcxfOVX6POLTuVFym5rzhF6IcqF1dT4GRV11BNwWzVuM5GDD6T2AAaAQ2s3_dBifq8mjusKE2fVR207F9-tG4uyRlfS3aL_uYR1jVbfnDnQdQLVmg2KI4P5ko0NZBXWJvd_a10iN1BCtpO13T7h2sO_7YtRQ8qErV9bkdbwiwCphHc1xK4UipjqQP4hF3CK9jo2eHLlk2qy5GwMPHHnVkfK2TUf_f-Q_ruXoCQZslNePaxck4_u8E6Rm_EzigdN3_4Vi6rVfaGTqu5SqGrut6Ig4Uuv9yNUCbFrOhOtj00lYoN314ao5wxs-CcJmhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682dd68c95.mp4?token=MyWNhvN5NWXBLWlZZyO5ibnZhcxfOVX6POLTuVFym5rzhF6IcqF1dT4GRV11BNwWzVuM5GDD6T2AAaAQ2s3_dBifq8mjusKE2fVR207F9-tG4uyRlfS3aL_uYR1jVbfnDnQdQLVmg2KI4P5ko0NZBXWJvd_a10iN1BCtpO13T7h2sO_7YtRQ8qErV9bkdbwiwCphHc1xK4UipjqQP4hF3CK9jo2eHLlk2qy5GwMPHHnVkfK2TUf_f-Q_ruXoCQZslNePaxck4_u8E6Rm_EzigdN3_4Vi6rVfaGTqu5SqGrut6Ig4Uuv9yNUCbFrOhOtj00lYoN314ao5wxs-CcJmhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کریس کونز، سناتور آمریکایی خطاب به وزیر جنگ آمریکا: شما در جنگ با ایران موفقیت‌های «تاکتیکی» دست یافته‌اید اما در آستانهٔ یک شکست «استراتژیک» هستید، چون ما اکنون درحال مذاکره هستیم تا فقط [تنگه باز شود].
🔹
وزیر جنگ آمریکا: این حرف خیلی احمقانه است!
🔸
کریس…</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/farsna/435166" target="_blank">📅 20:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435165">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWnDurrsaxRyXcz3GgPPFX6evLusybGwQpr6BNaX1Whqfd7mjdGGGnkaUHPycUxl5B1XTFhjc0ogGMowFABwABRB4kbhFsZHyJ2xJsvMUIBcL8sltfGpdaGPdkskJ9Hqo5pdEei4dHb8rgv_dFFTdFckG4bRD4gt4g00EiebxQy-sz5HvK3U9mbYJMeJZGEdky7BlO1QdJ6GQ5t7_btUokVvbekU5qDDsjscDuNhULmQD-Nmity6sKHgxtFmMEuajX6sJM2mpj56QtVUiUgiU7pzDf7MvtZtVBZOitAVPLrK1S_zTUeKiRfmAhS-BTqRrSdYFJo4EkjlUyPnfxvB4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حسین پاک، خبرنگار حوزۀ مقاومت: حاکم بحرین ۲ هزار شیعه را زندانی کرده است.  @Farsna</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/farsna/435165" target="_blank">📅 20:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435164">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/005efbb538.mp4?token=NtzhxvAU8pfcVhrkckF8oWknZNzqByj3ohlzuQ4nDAvODvjHPvEQf6H1IXv7vwqY8fD2va-rIAGOvrkZZIdXGqperJfcn0e0uqfklGHiS4yHyhgpcxvBcSQOhp1wsaa2UImvZIaqgkQwLI50pbfscYgsE_J5Hp84Itcu4iqlxnP4h_v8DDhjL0BqxW8eVFKwzumHuhiCWr1Sk6r1JYelk44sLCBpV2t2lHYg-uRyzcDnB9Qv5Dq1XpL4vwWrHJPTaNQrVR0WgPUxYssUPa5RzPcEvk0fkhg3tEvLR7fxF4yM6iuRxhmGQOGZR5KdM5pPLilR7eq7bs5DCNDv1L2jyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/005efbb538.mp4?token=NtzhxvAU8pfcVhrkckF8oWknZNzqByj3ohlzuQ4nDAvODvjHPvEQf6H1IXv7vwqY8fD2va-rIAGOvrkZZIdXGqperJfcn0e0uqfklGHiS4yHyhgpcxvBcSQOhp1wsaa2UImvZIaqgkQwLI50pbfscYgsE_J5Hp84Itcu4iqlxnP4h_v8DDhjL0BqxW8eVFKwzumHuhiCWr1Sk6r1JYelk44sLCBpV2t2lHYg-uRyzcDnB9Qv5Dq1XpL4vwWrHJPTaNQrVR0WgPUxYssUPa5RzPcEvk0fkhg3tEvLR7fxF4yM6iuRxhmGQOGZR5KdM5pPLilR7eq7bs5DCNDv1L2jyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی خطاب به وزیر جنگ آمریکا: شما ادعای کنترل تنگهٔ هرمز را دارید اما مشخص است که تردد کشتی‌ها در دست ما نیست
🔹
کریس کونز: آقای وزیر، شما همین چند لحظه پیش گفتید که «ما کنترل تنگه را در دست داریم». اما کاملاً مشخص است که بازگشایی تنگه هرمز برای…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/farsna/435164" target="_blank">📅 20:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435162">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3953e09c1f.mp4?token=Krr2CP1byjfxduihE3CWkJE7RCHHBNz2-nWbY3sB0aWXmoXf0qbAHcfrMDf9kwjkd5uqIrZvJXK6DhYAKq44-UWs3GsGAwDC-5rHJbZmzUwg9YKRl2ACupFhPn-YdHWSRXX2dZktLl7bhoMwmuvVJ63mR4F-5oNRXgXBrTIwtROa427pl-mNM320tomRrJojbJMzxPPys9dU6sfEtfpXvusRLwlrfcyl0y7yTLSQX7tvmiZYcSalKTbe9c7ro_bdPhf_FSvEtk_HuWriRQ8CgJCAfyXZcT8OveqZ2AaJIcMkv5Amp-27HdkG_fc_JJg2dX11J8GrR_ZBAizDeS-CoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3953e09c1f.mp4?token=Krr2CP1byjfxduihE3CWkJE7RCHHBNz2-nWbY3sB0aWXmoXf0qbAHcfrMDf9kwjkd5uqIrZvJXK6DhYAKq44-UWs3GsGAwDC-5rHJbZmzUwg9YKRl2ACupFhPn-YdHWSRXX2dZktLl7bhoMwmuvVJ63mR4F-5oNRXgXBrTIwtROa427pl-mNM320tomRrJojbJMzxPPys9dU6sfEtfpXvusRLwlrfcyl0y7yTLSQX7tvmiZYcSalKTbe9c7ro_bdPhf_FSvEtk_HuWriRQ8CgJCAfyXZcT8OveqZ2AaJIcMkv5Amp-27HdkG_fc_JJg2dX11J8GrR_ZBAizDeS-CoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی خطاب به وزیر جنگ آمریکا: شما ادعای کنترل تنگهٔ هرمز را دارید اما مشخص است که تردد کشتی‌ها در دست ما نیست
🔹
کریس کونز: آقای وزیر، شما همین چند لحظه پیش گفتید که «ما کنترل تنگه را در دست داریم». اما کاملاً مشخص است که بازگشایی تنگه هرمز برای تردد تجاری همچنان از دسترس ما خارج است؛ و دلیل عمده‌اش این است که ایران ذخیره قابل‌توجهی از پهپادهای ارزان و مرگبار «شاهد» را حفظ کرده و رقبای ما نیز در حال کمک به آن‌ها برای بازسازی این ذخایر هستند. آقای وزیر، برنامه شما برای بازگشایی تنگه هرمز چیست؟
🔸
وزیر جنگ آمریکا: بخش عمده‌ای از سوال شما بسیار غیرمنصفانه است.
@Farsna</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/farsna/435162" target="_blank">📅 20:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435161">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675f7d368f.mp4?token=q-xhCi995L8zIGM1ELS9I_6gSn3DAzBS73GIIWmrzYmxlVQDSYaYHM8Hww9utowe4wc3RdYBtev1M707K94WRiLmDmgo-Cx5RDWMs8km_szpB26UQdJdL2rkYmhAmApmEsTJnfXs3mYseHyQzjtFPeBaSY_HVqDUgfLjDrDNBxhVlN_YHBH23WbuXFJHpqT0ySTS8D3bkBvnSgFYtk4zw84LZvTBNAp0pRc-J4-_YqpG-XSKv_VDAiISBSYdeICqRG39kvUtGyOhpPh1uAtqDueeqE-BhnyofwWMbLCFVQajTjSUnHoR9s25B--wzrGcZz-fI0k14jD9bYfVkp25xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675f7d368f.mp4?token=q-xhCi995L8zIGM1ELS9I_6gSn3DAzBS73GIIWmrzYmxlVQDSYaYHM8Hww9utowe4wc3RdYBtev1M707K94WRiLmDmgo-Cx5RDWMs8km_szpB26UQdJdL2rkYmhAmApmEsTJnfXs3mYseHyQzjtFPeBaSY_HVqDUgfLjDrDNBxhVlN_YHBH23WbuXFJHpqT0ySTS8D3bkBvnSgFYtk4zw84LZvTBNAp0pRc-J4-_YqpG-XSKv_VDAiISBSYdeICqRG39kvUtGyOhpPh1uAtqDueeqE-BhnyofwWMbLCFVQajTjSUnHoR9s25B--wzrGcZz-fI0k14jD9bYfVkp25xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری منوتو صدایِ نوجوان ضد جنگ را هم تحمل نکرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/farsna/435161" target="_blank">📅 20:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435160">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5bb8f93b5.mp4?token=pqGx5MtQs5mi2gTur6xpEAFCMvKBmi0KCvS4BfCrLCcchwvTcJhZv1aPKZa8q9BTzPoD5II6ZA9TCup9xFViVrRDtDYu3s14CjtXCqe3iYpY4NFMYEgW-fDxl-QAxo1Kuvcp8xHiGMCnS1DdCDMZW70dFizj3pwPcT4Or92lb7Njy120fYC1qVOOd6gu1Q4UIjy5J7swEvuuHPoZDMl7LMMwkF_1AXy3VycFR71W_4L8hE2JJy3sPghGEIlnp3tY2_Y9dBpk5Gh8Ib7MGfdoY1aK9UQ3RRSGTxlIPKEaoA4rt6n7Zkw75_2RvCcGr0qBHfGmnyUgF8KCB4XRB6gkqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5bb8f93b5.mp4?token=pqGx5MtQs5mi2gTur6xpEAFCMvKBmi0KCvS4BfCrLCcchwvTcJhZv1aPKZa8q9BTzPoD5II6ZA9TCup9xFViVrRDtDYu3s14CjtXCqe3iYpY4NFMYEgW-fDxl-QAxo1Kuvcp8xHiGMCnS1DdCDMZW70dFizj3pwPcT4Or92lb7Njy120fYC1qVOOd6gu1Q4UIjy5J7swEvuuHPoZDMl7LMMwkF_1AXy3VycFR71W_4L8hE2JJy3sPghGEIlnp3tY2_Y9dBpk5Gh8Ib7MGfdoY1aK9UQ3RRSGTxlIPKEaoA4rt6n7Zkw75_2RvCcGr0qBHfGmnyUgF8KCB4XRB6gkqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس دفتر رئیس‌جمهور از آخرین دیدار شهید لاریجانی با پزشکیان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/farsna/435160" target="_blank">📅 20:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435159">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_XhgI648R_tByBDhFJF41qIHThkhocRU8C8BBguB-1sh0dXjg66HWTRTlySWo8GaK6ikKPmqdm9EASEBVHdI2DaQmoWNC5df5GpXdWYpjxdo7iG_JbRJ_GH4fclmlu92Axs4YN36ykiFy6qZfGPJ5NelJaLbno8x7Su_cU_GP0wk0wHrp4ccdrWdGJmC0ZALqXzLeQloEGTTzThj3HLtYs0pCrMo8hxthAjDrs3q06tAkaLGjoUuE1F3jQ9_-xoq3xO-bdpI1lS-b2rOyG4TJAnc9nTWs17pYFZzrokiskjHLL9ESaTPssW6Go4NbN6mPkGy1gw0otWitRN9PEh1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۴.۵ همت کالای قاچاق و احتکار شده توسط اطلاعات سپاه
ِ
اصفهان
🔹
اطلاعات سپاه استان اصفهان چندین هزار تن کالاهای اساسی، سوخت، لوازم خانگی و مواد پتروشیمی احتکار شده و قاچاق به ارزش بیش از ۴.۵ هزار میلیارد تومان را کشف کرد.
🔹
همچنین یک انبار بزرگ حاوی ۱۶۸۰ تن الیاف مورد نیاز بازار پوشاک به ارزش حدودی ۱.۷ همت که در سامانه جامع انبارها ثبت نگردیده بود، توقیف شد.
🔹
پرونده مجرمان جهت رسیدگی به مراجع قضایی ارجاع شده‌است.
@Farsna</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/farsna/435159" target="_blank">📅 20:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435157">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0f0907b65.mp4?token=bWwSnnJTemj9lqGvUedCmUaFIMcapbiLq1DgwzSnH5hRuhdYvt088XZAQFsDAcDdvB93RhPuxIpVWZp7dBEj-AtYIm0dAWtF6xKTfYi4ObXBTIJChlCMQJAibZmZQrFR-G2VpKDxIvepJQBegPGTVw6d58MXqMS6ABOMZNqIIlMfXef_3E9XBR8U1OhsJwbk29_8Kbw24TLfdThu20fDDOOMxYIx9sLSPm-SP6KxEABR3zMQkBFm4A7zQ15YX08PPq6vxaJxutNXzRxwl4eAKWq2R2140BAo48ol5rYN_6_umsaJXU0tMmDcIVUdE1SKlXeuWxJPf0MKllfop1Ug2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0f0907b65.mp4?token=bWwSnnJTemj9lqGvUedCmUaFIMcapbiLq1DgwzSnH5hRuhdYvt088XZAQFsDAcDdvB93RhPuxIpVWZp7dBEj-AtYIm0dAWtF6xKTfYi4ObXBTIJChlCMQJAibZmZQrFR-G2VpKDxIvepJQBegPGTVw6d58MXqMS6ABOMZNqIIlMfXef_3E9XBR8U1OhsJwbk29_8Kbw24TLfdThu20fDDOOMxYIx9sLSPm-SP6KxEABR3zMQkBFm4A7zQ15YX08PPq6vxaJxutNXzRxwl4eAKWq2R2140BAo48ol5rYN_6_umsaJXU0tMmDcIVUdE1SKlXeuWxJPf0MKllfop1Ug2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
واشنگتن‌پست: ایران حداقل به ۲۲۸ ساختمان یا تجهیزات در پایگاه‌های آمریکا حمله کرده است
🔹
این حملات شامل آشیانه‌ها، پادگان‌ها، انبارهای سوخت، هواپیماها و تجهیزات کلیدی رادار، مخابرات و پدافند هوایی بوده است.
🔹
میزان تخریب بسیار فراتر از آن چیزی است که دولت…</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/farsna/435157" target="_blank">📅 20:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435156">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mr1pygj68PeRoe_iliZeWqafgmZzll_IvdjKrAu8VOKWUrC6sGTn9RU-lH9W6ZEOYajIODt0DnrdrE43rOFIqbWRgiey7peIEarXIgec6FG-2_sNHRZ3d7wqRSpfJETEx1CA1NC91dFaJp4TO4pvCOUIzRzgQ2qcpAbTCC03qoR30TN5x2tAhnVkq3oelZh7iBj37rGXI0s549hXqTfJ-FoJtJIB-hXEs4rJjEPMm9pRk43nSnfYZJFGJAiM1yT_ynjbPHlqM2CMTiDagTSjZoAEOz1gqRlIjQxTfoD6HFvq4wHywwBr7MIjpR2M6U3gTRAt-b4eC3uLCoSgi7FDNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتایج یک پیمایش ملی از ابعاد پنهان تجمعات شبانه
🔹
یک پیمایشی درباره تجمعات شبانهٔ ایران که با مشارکت ۴۳ هزار و ۳۹۱ نفر در بازه زمانی هفتم تا یازدهم اردیبهشت سال جاری انجام شده، ابعاد مختلف این حضور جمعی را از منظر انگیزه‌ها، تجربه اجتماعی و پیامدهای آن بررسی کرده است:
🔸
۹۴.۸ درصد پاسخ‌دهندگان اعلام کرده‌اند حضور مردم در تجمعات داوطلبانه و خودجوش بوده است.
🔹
۹۳.۱ درصد شرکت‌کنندگان با این گزاره موافقند که نهادهای مردمی نقش اصلی در سازماندهی تجمعات دارند.
🔸
در شاخص «توجه و شکر نعمت وحدت» میانگین امتیاز ۸۷.۵۴ درصد ثبت شده است.
🔹
۹۱.۸ درصد پاسخ‌دهندگان هم معتقدند در تجمعات بر حفظ وحدت اجتماعی تأکید زیادی می‌شود.
🔗
شرح کامل پیمایش را از
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/farsna/435156" target="_blank">📅 20:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435155">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TluJEUrjG2D1iwcaoenpuBkZa1KQ72x1dX2HvUPoTz1SaCYUKgII0eQn2nW_-STcMMkJ95AlQfraCQXwwegLw4f6vYriYWSbGeh1E_XDY3VQbOpbnU6cYpC4Lrmo8ypFJ-W2_ye80EtTLlcmsRNAh_Id1APEdex8Ty_hpA7mAdnGJfnYl1kdPPvEep4M3iUZjAVhe2H6_9XMVdWzhPhZhyvx1Y-fv40Oqt3ES2yo_KpQIxv9Dxr6EocMTAhRtZScpAMdbMIvMGH-8Mrnb5MMUABoFodsCneWP2tul3vzUFoEoKoq2RZkhYBl0mXTL3ciMRc3SkkTL4E31Y-XSiML9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برد پر گل تیم سفید ایران مقابل تیم قرمز
⚽️
گلزنان بازی:
علیپور، ایری(۲)، یوسفی، حسین‌زاده
⚽️
تیم سفید ۴ - ۱ تیم قرمز
@Sportfars</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/farsna/435155" target="_blank">📅 20:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435154">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c11c0a8608.mp4?token=DlBraGikJloX6MxG_TBdERW0eoQlkeMMyWNRLN3RvmDE6py1h6I4O4NHbQLdsMFz9xGmfUHTb2SiYHrygd3GsK1FTqCChbxPG4z83rSv7UrtM3miOAo_KgfO1s2lg6-qhBFgzGeRFCM3yGV2MPY7YlNuXBSRZvlND6LBDfuPvM6O3UANCD4B8GJca0DJwkXQyrkCOUHPrRtFfpvKdp2_p-Rp7nhsgU00RfpwepC4j82z_nz02MfBLsq9PHIFDRS3wQjHj38FOcP_NCkrxpUHlkM0uuzGCiFKcWrRInbW4X8essI12LLPYgxqXEfv4IBE52qcHLG91-tnef85k8w_1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c11c0a8608.mp4?token=DlBraGikJloX6MxG_TBdERW0eoQlkeMMyWNRLN3RvmDE6py1h6I4O4NHbQLdsMFz9xGmfUHTb2SiYHrygd3GsK1FTqCChbxPG4z83rSv7UrtM3miOAo_KgfO1s2lg6-qhBFgzGeRFCM3yGV2MPY7YlNuXBSRZvlND6LBDfuPvM6O3UANCD4B8GJca0DJwkXQyrkCOUHPrRtFfpvKdp2_p-Rp7nhsgU00RfpwepC4j82z_nz02MfBLsq9PHIFDRS3wQjHj38FOcP_NCkrxpUHlkM0uuzGCiFKcWrRInbW4X8essI12LLPYgxqXEfv4IBE52qcHLG91-tnef85k8w_1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوحهٔ حماسی کریمی در میدان انقلاب: «رهبرمون هرچی بگه همونه»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/farsna/435154" target="_blank">📅 20:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435153">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKZK8QROVSnMY29sYMkTKgizLm-SRmfDNciFsQaj_Pdf9k1RFxEszPugEBkYOnqcNSyYudkX8HTQs7XDiYQCg-YCGWurbLAdJMFtAJbZZKsGwOWJGmh0zON6ZF-I-BNFIbOYoZr9-ApudBLDBkVHT0t1HhXecigeXBK-T7GqpByELDIC3HILrR3Ohl-HvhzMaLe8UXZXF8SJSglbISYfsKM9sTlTNs5q7PeQ-ZNA9-C52TtlTKeQARSloKIa7vIygiR4L5XYSZGXgnNje_vq2xkt7rfiml42oQFaMwPk2HfkEpZ1yauvYoUbQhkCv95RfEGQqE_Qn9VJ1h9nKpPwKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افرادی که وسط جنگ هم دست از افزایش قیمت خودرو برنمی‌دارند!
🔹
طاهری، عضو کمیسیون صنایع مجلس: ایران‌خودرو با مدیریت جدید نباید هر اقدامی را بدون توجه به سیاست‌های کلان انجام دهد.
🔹
پیش از این بارهاهشدار داده بودیم که واگذاری‌ شرکت‌های خودروسازی از نظر ما با تعارض منافع همراه خواهد بود.
🔹
انتظار می‌رود قوه قضائیه به‌صورت جدی به این موضوع ورود کند زیرا تصمیمات مدیریتی در حوزه خودرو مستقیماً بر زندگی مردم اثر می‌گذارد.
🔹
الان کشور گرفتار افرادی است که وسط جنگ خودرو را گران می‌کنند.
🔹
حتی در دوره‌ای که مدیریت خودروسازان دولتی بود، اگرچه مردم از وضعیت خودرو رضایت کامل نداشتند، اما سیاست‌های کلان حاکمیت در حوزه قیمت‌گذاری رعایت می‌شد و کم‌تر شاهد تصمیماتی بودیم که در شرایط حساس کشور موجب افزایش قیمت‌ها شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/farsna/435153" target="_blank">📅 19:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435152">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db78859303.mp4?token=Agf_mUVlwSyIqYn1N1LbdsYmkeM0AYpEDVQ8vXwlXlF3JfJ4jp4Rmzx1ppAR4eDupxI_ScxUSj4HhboEU7WV0HUkms2SFCBBL5rcaZX_tzZWFc4yA9mepemBLuM4fxFlKC55mJ8l-q9dOWbz8ZWyYoIx-JzineVZ1P0gUJO_CHCdzHLIRXU581bR-iQfLjzZfDNGzuTGmmhM94G6Y1RY4EIWE1AQEFDR9bEcxpuCuEesyCTPnjQ4n-5sPtFDIUdVxyuBl140xGu-sQkMloBdKPUdPebLiR-EJGFQ7Oc8-ZDszzQ5kxaB92GgAVzdCH-_qSD7ZdCLu2aDP0k6DHv7-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db78859303.mp4?token=Agf_mUVlwSyIqYn1N1LbdsYmkeM0AYpEDVQ8vXwlXlF3JfJ4jp4Rmzx1ppAR4eDupxI_ScxUSj4HhboEU7WV0HUkms2SFCBBL5rcaZX_tzZWFc4yA9mepemBLuM4fxFlKC55mJ8l-q9dOWbz8ZWyYoIx-JzineVZ1P0gUJO_CHCdzHLIRXU581bR-iQfLjzZfDNGzuTGmmhM94G6Y1RY4EIWE1AQEFDR9bEcxpuCuEesyCTPnjQ4n-5sPtFDIUdVxyuBl140xGu-sQkMloBdKPUdPebLiR-EJGFQ7Oc8-ZDszzQ5kxaB92GgAVzdCH-_qSD7ZdCLu2aDP0k6DHv7-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هزینهٔ جنگ آمریکا با ایران ۴ میلیارد دلار بیشتر شد
🔹
نماینده پنتاگون: چند روز پیش برآورد هزینهٔ ۲۵ جنگ میلیارد دلار بود اما در حال حاضر فکر می‌کنیم این رقم به ۲۹ میلیارد دلار نزدیک‌تر شده است.
🔸
پیش از این سی‌بی‌اس فاش کرده بود که هزینۀ واقعی آمریکا نزدیک…</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/farsna/435152" target="_blank">📅 19:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435151">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40069255e.mp4?token=qMnwb2sjNSnN_KRVcQETGkbRhNaGhRLM-PVcH3ZhAzkvxUVmR8EUb1jhRkN2fRhRnLXf4IElw572MYsiO_jNOyinVsYFXQ_xpoIW7V5snmWDyuMUNs-EBiMcrjkqm8ur-UrXrXBABgnk6pykCBqkAxwTpqQyy7Twg3mVUyfFtI_ta7Iu5KuXzXvHeA6Y9GNrxQkaIFOXG1nm5I97Y8BQiai6SK-xsjLJlPd30K_517atYByzJegZB4RkhTyODL_sB7LqTmE8fkCWUvVvFJQatcMQXoFMOiJzxC42NjlDbJj_PbiDGw7g47AJUQQ2fnEtrTpPo4H8OHULMaQKvFUVVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40069255e.mp4?token=qMnwb2sjNSnN_KRVcQETGkbRhNaGhRLM-PVcH3ZhAzkvxUVmR8EUb1jhRkN2fRhRnLXf4IElw572MYsiO_jNOyinVsYFXQ_xpoIW7V5snmWDyuMUNs-EBiMcrjkqm8ur-UrXrXBABgnk6pykCBqkAxwTpqQyy7Twg3mVUyfFtI_ta7Iu5KuXzXvHeA6Y9GNrxQkaIFOXG1nm5I97Y8BQiai6SK-xsjLJlPd30K_517atYByzJegZB4RkhTyODL_sB7LqTmE8fkCWUvVvFJQatcMQXoFMOiJzxC42NjlDbJj_PbiDGw7g47AJUQQ2fnEtrTpPo4H8OHULMaQKvFUVVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماینده کنگرهٔ آمریکا: طبق گزارش‌ها ما تا یک ماه پیش در جنگ با ایران ۳۹ هواگرد از دست داده‌ایم که برخی از آن‌ها جایگزین ندارد
🔹
اِد کِیس، نماینده کنگره: طبق گزارشی در پایگاه «وار زون»، ما حدود ۳۹ هواگرد از دست داده‌ایم، که البته آن گزارش قدیمی است. متعلق…</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/farsna/435151" target="_blank">📅 19:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435150">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b70a136fd5.mp4?token=qju5tKiaINhie0JAPlzNgS56d4OtjqUcf9ilL9bJxch8VDA5T3GWgl-OCivKOem3K1vTRfvReSG37MKizba3U6nbSiXk1_EJoKdpbZsZRYpyLE6xpwfem7pnzqhqXj9NhJUiVXE0wkdcr3BPKaeIBgAqa4yV6o-Cf89gRF4qfmHg0Fb9Amg3z9W7dvd8iOaFLce2aF68QFZzv474TVUx91U-x7Emmq_kNSVNkLih7qwVkW0AG5yoLpbXozs73GsdG70Duui3BiGq1Bxu2Rj11DRJHOmja11842ybIakfmi8fr8BLXZ80tW5HE24v2G39LkGpEJXWcJjEvSGVtdd0TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b70a136fd5.mp4?token=qju5tKiaINhie0JAPlzNgS56d4OtjqUcf9ilL9bJxch8VDA5T3GWgl-OCivKOem3K1vTRfvReSG37MKizba3U6nbSiXk1_EJoKdpbZsZRYpyLE6xpwfem7pnzqhqXj9NhJUiVXE0wkdcr3BPKaeIBgAqa4yV6o-Cf89gRF4qfmHg0Fb9Amg3z9W7dvd8iOaFLce2aF68QFZzv474TVUx91U-x7Emmq_kNSVNkLih7qwVkW0AG5yoLpbXozs73GsdG70Duui3BiGq1Bxu2Rj11DRJHOmja11842ybIakfmi8fr8BLXZ80tW5HE24v2G39LkGpEJXWcJjEvSGVtdd0TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماینده کنگرهٔ آمریکا: طبق گزارش‌ها ما تا یک ماه پیش در جنگ با ایران ۳۹ هواگرد از دست داده‌ایم که برخی از آن‌ها جایگزین ندارد
🔹
اِد کِیس، نماینده کنگره: طبق گزارشی در پایگاه «وار زون»، ما حدود ۳۹ هواگرد از دست داده‌ایم، که البته آن گزارش قدیمی است. متعلق به تقریباً یک ماه پیش است. آیا هزینۀ جایگزینی تمام آن هواگردها را می‌دانید؟ با این فرض که برخی از آن هواگردها قابل جایگزینی نیستند، اما قاعدتاً باید آن‌ها را با نوعی ظرفیت و توانمندی جایگزین کنید.
🔸
نماینده پنتاگون: هزینه‌هایی در این مورد وجود دارد، اما می‌خواهم جزئیات دقیق آن‌ها را به صورت مکتوب به شما ارائه دهم. چون همان‌طور که می‌توانید تصور کنید، محاسبه هزینهٔ تعمیرات هواگردها کار بسیار دشواری است. ما می‌خواهیم پیش از برآورد هزینه، یک عیب‌یابی کامل از هواگردها انجام دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/farsna/435150" target="_blank">📅 19:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435149">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d359f5beb6.mp4?token=JsvWZlHV7Zb_OF0t131_dWMWMe707tFv7a30Daqr3DOzyy0Fd0W8xsyCfBd6vEhamlCfdSJrKKKpfPOCfXvItW4XNr_O_3jHjc5bazjwvxKczA7PQJP953kg8QXE3kBSZ8Tie0nFAbvVFxugOKt6kHV6dKrXbokrwrZx5AbOzBKvgt3Dpkb-v5QpyrvXMMYoi39d0H4vVrSJ4IGkPY3BXRTHpiRp1keVhqH6xE_xe0LPoxLAMAdh4hOJghdS9xhRIP18u9Z20ogG12y7MITX2mmcVKAnpzjPTg1T6481qXs3MzOtT18lI1qDFqeMEEep8N7bwikaoJoWaCrukn_Azw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d359f5beb6.mp4?token=JsvWZlHV7Zb_OF0t131_dWMWMe707tFv7a30Daqr3DOzyy0Fd0W8xsyCfBd6vEhamlCfdSJrKKKpfPOCfXvItW4XNr_O_3jHjc5bazjwvxKczA7PQJP953kg8QXE3kBSZ8Tie0nFAbvVFxugOKt6kHV6dKrXbokrwrZx5AbOzBKvgt3Dpkb-v5QpyrvXMMYoi39d0H4vVrSJ4IGkPY3BXRTHpiRp1keVhqH6xE_xe0LPoxLAMAdh4hOJghdS9xhRIP18u9Z20ogG12y7MITX2mmcVKAnpzjPTg1T6481qXs3MzOtT18lI1qDFqeMEEep8N7bwikaoJoWaCrukn_Azw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی در پایگاه نظامی اسرائیل در شمال فلسطین اشغالی
🔹
منابع اسرائیلی گزارش دادند این مقر در نزدیکی شهرک «مرگالیوت» قرار دارد و دچار آتش‌سوزی شده است.
🔹
این مسئله ناشی از حملات حزب‌الله به این شهرک اعلام شده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/farsna/435149" target="_blank">📅 18:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435148">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce65d3c53.mp4?token=Stiu9-qHjVdy7voh-hpRomyONm0dFqGSPP7KDLTo-__1i7tv5H4QTXmHey_-UbYuqd2JUT7pkf-CtESMkyDo17SfLN876Rxbm6Wjn1MF8UvAvwZtzxAsRvuzRCYykxoG_I9CG4WNR6sS9oPbBGBZxZ633_Ey32U-HIub9H2WVRH9gclqrCSYDcGSywC21_reDuxlexEla_RdMw25Dt-ayWbSHryTIgTEiCzWji35CmVjPU5cMWNJnlPnN2DSHJO8cigEhIt0dZ9DP5kEWGZm2nsAjn8Kbg2GM_K6v8MFCFf6lFyKcPWi3j8yYy0wD7y68se88BjRETFzg91HA38JLh1WxvoKxsnQxUvWoDDmYbBZA_09M0iVOSTXZyd5_zLl8WGMj5ru3-N38uyy6gFemVJkyuUjG6GDfx2FydVuL4_lCkyKoABccVGNiWrv07uZFKfTv8alTo7njRnoZitd8y2RNwv7Ip29m9LtROtj5kwn9EfmPKGsfQssj7fbrx36NvmVvFXTdU-kbDhxyYmqgBKvdLRqK2LIqIg_0sEyFxE06JuJcw0k8Ph93DGX1mCCCBjW_si5o6j9WlHnl59zM5OwISOU_IYWSOrPtERwHDZyN9YK5-_r33dDiN3XXrTT7WujMzj65A5wqozAdRhjx6DsRExQlSXWP3QqS8vaWQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce65d3c53.mp4?token=Stiu9-qHjVdy7voh-hpRomyONm0dFqGSPP7KDLTo-__1i7tv5H4QTXmHey_-UbYuqd2JUT7pkf-CtESMkyDo17SfLN876Rxbm6Wjn1MF8UvAvwZtzxAsRvuzRCYykxoG_I9CG4WNR6sS9oPbBGBZxZ633_Ey32U-HIub9H2WVRH9gclqrCSYDcGSywC21_reDuxlexEla_RdMw25Dt-ayWbSHryTIgTEiCzWji35CmVjPU5cMWNJnlPnN2DSHJO8cigEhIt0dZ9DP5kEWGZm2nsAjn8Kbg2GM_K6v8MFCFf6lFyKcPWi3j8yYy0wD7y68se88BjRETFzg91HA38JLh1WxvoKxsnQxUvWoDDmYbBZA_09M0iVOSTXZyd5_zLl8WGMj5ru3-N38uyy6gFemVJkyuUjG6GDfx2FydVuL4_lCkyKoABccVGNiWrv07uZFKfTv8alTo7njRnoZitd8y2RNwv7Ip29m9LtROtj5kwn9EfmPKGsfQssj7fbrx36NvmVvFXTdU-kbDhxyYmqgBKvdLRqK2LIqIg_0sEyFxE06JuJcw0k8Ph93DGX1mCCCBjW_si5o6j9WlHnl59zM5OwISOU_IYWSOrPtERwHDZyN9YK5-_r33dDiN3XXrTT7WujMzj65A5wqozAdRhjx6DsRExQlSXWP3QqS8vaWQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخست‌وزیر سابق قطر: آمریکا با جنگ به دوستانش در منطقه آسیب زد
🔹
شیخ حمد آل‌ثانی: اقدام نظامی [علیه ایران] در کل به سود هیچ کسی در منطقه نبود. آمریکا به دوستانش در منطقه آسیب رساند.
🔹
عملیات نظامی تنها به سود شخص نتانیاهو بود. به برنامه‌های او کمک کرد.
🔹
او به‌صورت آشکار از ضرورت ترسیم یک نقشه جدید در منطقه و تشکیل ائتلاف‌های جدید برای اسرائیل بزرگ صحبت می‌کند.
🔹
آن‌ها اطلاعی از ساختار قدرت در ایران ندارند؛ این هرم [قدرت] طی ۴۷ سال و از زمان خروج شاه ساخته شده. به آن شکلی که آنها فکر می‌کنند سقوط نمی‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/435148" target="_blank">📅 18:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435146">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کویت سفیر ایران را احضار کرد
🔹
وزارت خارجۀ کویت با ادعای ورود چند نیروی سپاه پاسداران به جزیره بوبیان، از احضار سفیر ایران خبر داد.
🔸
کویت مدعی شده گروهی از نیروهای سپاه با ورود به این جزیره با نظامیان کویتی درگیر شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/farsna/435146" target="_blank">📅 18:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435145">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df4b69123b.mp4?token=STu1eZEBm3fsmQMCiTMrh9wTmXRYFEFF6tYb5uI2PjB55DRWkOIMMwiG_k0pRHcSrKe2BfcjxL7MqqwCROy4sNS8xcDsa_keWRC0Vbf81v6WxVkCZPya3y1qXUs2qLEPZ0tJkaG2iX6WHv_CNPMnhvQE5CRsSS_KZrJOKQUs99lR2aAPzctIjz30B-aoxxpUchNHx1ZniG8lFlVygbdG2f7BzOjwdy3cPa03NgVgayLWlrP5RJnLttRyW5apDx42gw7c_xYtYJZxZVOkQxRkwD4HIc2-PNt9H_IgNJ1znVSsPqB-iQEPvPmTZfgQhdfYl6GW5I5U2wTcav-vHLMSVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df4b69123b.mp4?token=STu1eZEBm3fsmQMCiTMrh9wTmXRYFEFF6tYb5uI2PjB55DRWkOIMMwiG_k0pRHcSrKe2BfcjxL7MqqwCROy4sNS8xcDsa_keWRC0Vbf81v6WxVkCZPya3y1qXUs2qLEPZ0tJkaG2iX6WHv_CNPMnhvQE5CRsSS_KZrJOKQUs99lR2aAPzctIjz30B-aoxxpUchNHx1ZniG8lFlVygbdG2f7BzOjwdy3cPa03NgVgayLWlrP5RJnLttRyW5apDx42gw7c_xYtYJZxZVOkQxRkwD4HIc2-PNt9H_IgNJ1znVSsPqB-iQEPvPmTZfgQhdfYl6GW5I5U2wTcav-vHLMSVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مارک
کلی، سناتور آمریکایی: وزیر جنگ ترامپ گفته جایگزینی مهمات استفاده‌شده در جنگ ایران سال‌ها زمان می‌برد
🔹
دولت ترامپ حجم عظیمی از مهمات را در جنگ با ایران مصرف کرده است. بعد از ۱۵ هزار حمله، تنها چیزی که نصیبمان شد، ۱۳ کشتۀ آمریکایی، بسته‌شدن تنگۀ هرمز، بنزین ۴.۸ دلاری بود.
🔹
آن‌ها بدون هدف استراتژیک، بدون برنامه و بدون جدول زمانی وارد این ماجرا شدند. حالا هیچ راهبردی برای خروج ندارند و به دست‌وپازدن افتاده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/farsna/435145" target="_blank">📅 18:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435144">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9337725a2.mp4?token=Xj-5IhxKMTvkOHc1jG2bbY0TK8IZBMpnl172LUB0MvDJgrLgOH47gS38qTGmWieLXHz-3hdz0EFfBlcFk6Aoz-4RWDWHiUZx93eJmMRxNmFuZfYAyaKzGkrGdG1OIFeXPVwFvgJTaA2FOkYA3MvLheVezz9ZLdhZcYPNpwr8J2-IeIjVYApqen1e2oTzpuhy91WxJxhby8EsLRDfZeyyugvj1nnq_bHGViu3Ikv_CxSF-OO-dK1yezNw03n1YATwAR6NowkeobaMWgr7UbhSXeGcKKzOKHU2XMwFE-LFlyN59zpuDRGrZTE2QyRU-UWupIbLOUazimiCYfdRNMSkjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9337725a2.mp4?token=Xj-5IhxKMTvkOHc1jG2bbY0TK8IZBMpnl172LUB0MvDJgrLgOH47gS38qTGmWieLXHz-3hdz0EFfBlcFk6Aoz-4RWDWHiUZx93eJmMRxNmFuZfYAyaKzGkrGdG1OIFeXPVwFvgJTaA2FOkYA3MvLheVezz9ZLdhZcYPNpwr8J2-IeIjVYApqen1e2oTzpuhy91WxJxhby8EsLRDfZeyyugvj1nnq_bHGViu3Ikv_CxSF-OO-dK1yezNw03n1YATwAR6NowkeobaMWgr7UbhSXeGcKKzOKHU2XMwFE-LFlyN59zpuDRGrZTE2QyRU-UWupIbLOUazimiCYfdRNMSkjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدیه متبرک خادمان حرم امیرالمومنین(ع) برای آسیب‌دیدگان جنگ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/farsna/435144" target="_blank">📅 18:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435143">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">🎥
سلام نظامی ملوانان ناو دنا هنگام نواختن سرود ملی
🔹
ملوانان ناو دنا، مهمانان ویژۀ سومین بازی درون تیمی تیم ملی هستند.
@Sportfars</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/farsna/435143" target="_blank">📅 18:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435142">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار چهارمحال و بختیاری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8369afb88.mp4?token=fZ5051heN8SX1P0Nn2NDtPMn_RLmU4ibHgr9mhmQRTl095LcsV9-oKh1YwfrRTxbSD3ArmCfzMW3nD6pNDnUQjp9nS9zvBGjZpG1PCGm57PD1fUSrRxXHzazMDo8ciS-opejX3WZY-gFy_rBBIQgCnN_S4ZuHgdTWXYSat2vBhwSnorl6W7lbdoYZgc2BXT2nvM2s84hjUGHFE_rg8ONZ8Z2cH9a7sCACz3TfY_RNSLG4L55qNgN2YXC41v4TYayq8QQNW5-P0XGmHBBZzI0ZUQV7Z90LCHVv9MDCvPVwMoYGOGfvPVjSu0ugo4uiJ61Pze-XPXYPkeyizUJLb9waQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8369afb88.mp4?token=fZ5051heN8SX1P0Nn2NDtPMn_RLmU4ibHgr9mhmQRTl095LcsV9-oKh1YwfrRTxbSD3ArmCfzMW3nD6pNDnUQjp9nS9zvBGjZpG1PCGm57PD1fUSrRxXHzazMDo8ciS-opejX3WZY-gFy_rBBIQgCnN_S4ZuHgdTWXYSat2vBhwSnorl6W7lbdoYZgc2BXT2nvM2s84hjUGHFE_rg8ONZ8Z2cH9a7sCACz3TfY_RNSLG4L55qNgN2YXC41v4TYayq8QQNW5-P0XGmHBBZzI0ZUQV7Z90LCHVv9MDCvPVwMoYGOGfvPVjSu0ugo4uiJ61Pze-XPXYPkeyizUJLb9waQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا خانه مادر شهید سردار خادمی رئیس سازمان اطلاعات سپاه است
🔹
ماجرای عجیب لحظه شهادت سردار شهید خادمی و حرف زدن مادر پس از ده سال!
آخرین خبرهای جنگ را اینجا ببینید
👇
@Fars_Chb</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/farsna/435142" target="_blank">📅 18:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435141">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۳۳.pdf</div>
  <div class="tg-doc-extra">2.2 MB</div>
</div>
<a href="https://t.me/farsna/435141" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۳۲.pdf</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/farsna/435141" target="_blank">📅 18:05 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435140">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLlo29w23Rg5cedRU_rBP6CR0o2x25DnclwSW-TqPpNmwQNq13KVtz83RPTmTB_Gb-cxrCQZCS3udvYMySUA5hR6OSc0rH9NxGqplVtysnhneHwzgJrjTser1A-qZMkIN2xbQURIokZlCi1AitYSRJn0XfvDaC5_1i0nPNGuBEJk1gQO5Q0k2ZLOB7U3_nUocmnHRtzStucME_pZswj6OWPNd3g3vIdrjOcpIyp7et6SbCuZQePI8unblAmA9dVRiA1E9nSc-trwB3GxI_nVTrJo5VXKBpYI_zBjT_GpHl2b9F0wkEdNvX6o1ZpghleDw4hmjzYGwdGkQMxL-gYNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: ارتباطات مبتنی‌بر فناوری اطلاعات و اینترنت به بخش جدانشدنی زندگی مردم تبدیل شده
🔹
به آقای عارف ماموریت دادم با لحاظ حساسیت‌های حکمرانی، نظر رهبری و وعده‌ای که به مردم داده بودم، در قالب ساختاری چابک موجبات خدمت‌رسانی بهتر دولت و تحقق انتظارات عمومی را فراهم سازد.
@Farsna</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/435140" target="_blank">📅 18:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435139">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd9b7db5f8.mp4?token=phcprMmcv6NiNvi_A0hUzH05POgWtIW6Mtl3NKOxSdQFlRNGzMwAP1kh6vgm4BmNPyCZ0WOyAGZfXH-VdoaomBI8fzQt0xaqlCoWkVWEvWgXAPtb__29I0LiCopLydo8XpBWBqKhh5O6DJcGg1fnkq67yVRT91ezL06gGWPaIyldsidBAezCWr6rUNuQl_-yf7sDqq-sSquPq8Muiv8aqh_SbGgMs3U5rTlfpDwsZtm6d8WyypTAcMDNKQdDip9WL9IV4sYd3KNdWOIMnzm1APmniOLgNouhClywPIGM_j5ubzaDtHFCcsQwf-LgklsKcjGPkcpYZD7RTl4RCBocZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd9b7db5f8.mp4?token=phcprMmcv6NiNvi_A0hUzH05POgWtIW6Mtl3NKOxSdQFlRNGzMwAP1kh6vgm4BmNPyCZ0WOyAGZfXH-VdoaomBI8fzQt0xaqlCoWkVWEvWgXAPtb__29I0LiCopLydo8XpBWBqKhh5O6DJcGg1fnkq67yVRT91ezL06gGWPaIyldsidBAezCWr6rUNuQl_-yf7sDqq-sSquPq8Muiv8aqh_SbGgMs3U5rTlfpDwsZtm6d8WyypTAcMDNKQdDip9WL9IV4sYd3KNdWOIMnzm1APmniOLgNouhClywPIGM_j5ubzaDtHFCcsQwf-LgklsKcjGPkcpYZD7RTl4RCBocZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بحرین، کشوری که با طناب پوسیده دیگران به ته چاه رفت
🔹
بحرین دهه‌ها تلاش کرده معظل جغرافیایی و  سیاسی خود را با تکیه به دیگران پوشش دهد؛ اکنون در زمانی که امید داشت از این راهبرد بهره ببرد؛ با واقعیت‌های بی‌رحمی مواجه شده است.
🔹
در ذات موقعیت ژئوپلیتیکی خود،…</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/farsna/435139" target="_blank">📅 17:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435138">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5ab333d5b.mp4?token=Su1Ahuae8kxbZSboMNzHWGa4SNkwIhExjePXb5pF6TyWJ4DCFhcvwqdPpWe6m393o7wMSZQHSio4KRFmGTDZEL4yJ9I16ads2fE9sCGutxbWbOTIUeymMyjXtDllKBudHz9y6IUq503QjQy8OYQbz-HJpEOkW55dAd10eEaXZ6u7xVOyp6d37_cHUp0pW9VMNS4CAqLIloMKvE9xWu9HnSd61dcF6o3knNGS8LRuCylC8rOUA5opQ_CFwNMnLuCVGbYuu1-YXYgk-6ltwBQt5hLRD40vGX7dDIRulnShBgeRleuUpHi2vKLAVNMNV8gTv8Dl1r-_avCE2PqvhBSsEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5ab333d5b.mp4?token=Su1Ahuae8kxbZSboMNzHWGa4SNkwIhExjePXb5pF6TyWJ4DCFhcvwqdPpWe6m393o7wMSZQHSio4KRFmGTDZEL4yJ9I16ads2fE9sCGutxbWbOTIUeymMyjXtDllKBudHz9y6IUq503QjQy8OYQbz-HJpEOkW55dAd10eEaXZ6u7xVOyp6d37_cHUp0pW9VMNS4CAqLIloMKvE9xWu9HnSd61dcF6o3knNGS8LRuCylC8rOUA5opQ_CFwNMnLuCVGbYuu1-YXYgk-6ltwBQt5hLRD40vGX7dDIRulnShBgeRleuUpHi2vKLAVNMNV8gTv8Dl1r-_avCE2PqvhBSsEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پخش لحظه شکار سامانه چند ده میلیون دلاری گنبد آهنین به وسیله پهپاد ۲ هزار دلاری حزب‌الله از شبکه سه
@Farsna</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/farsna/435138" target="_blank">📅 17:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435131">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUb39khlNkk9MxtfEtuww7-nPsAgv7Bj3i44_jEki0ge1pNnVgNHUYSMspNA-i1TiCQe_Krpyp3_QZLbzqXS11chF69pwRangwTb0q8XbLNLcc_QU57m0nu0Spw_oBSuZTRB85ujUj4_8kY8sPTpE6dLvuk_mqcCR3XeknD4PHYrIOe_70s-hgUvwaocd_QDqT-o5P3UUYxuND0d5LcGzCUn870s2aQXNyI5B6STbwwqKTLJvVwvzfejJsqvzLshVFMTIj8GCkKKIGV34qzayGhwIMJO6E5gjvZYShowcvk14O38L-fNVShMNNs5CUaZzHXDQFVaL1lSqpv_qyjtdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IczG0EwMTKwO3ftrlTHkMNFg8mJbe_fwmjHyjvIDXH7rJExrt_be6et-_wOeY9Rs8GNlJ25kQXRLfyCuXP2_UIjA4jShCNsGDmCuc9BQYY5jyt275GMco0Bhxm-8IOm15HtCl-sQoJdoYnNxUJ7qLSUdXfBYnHNF7bV4qQfMl6VTczMBOcktQVeC2gh9kZLWa85Ys8io_93BWym1IyAdAX0LQHsHU_C6iKjGSm4MvJWf2GTVKVPvwouZwm5VEgtOcSMupWp8XGAyjQ2ajDMRx9dZEUtoqhs6BWSor18KXMZLvjfOC9fZrOFzrERb2H7B8vnF5C_oVNNv5K8EeBWi_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vr4ItaFn02lFp4A_P6viqoz0PMTFQhLbs7jXK-VpIX10_0cmYqUR13UEbxs1i4JX97Lx-8oNjF_dP76BmtEiz7dPVVgA3Q1VrMvEhmvc7EaPAIQNJcr807g4Sd_SpBwfF2vhH0j8GdCcU1sPDCYpT5ACYfgsknMnmfIV_LjNz8hzLSOOcbBRzc58C60rxrMxjtmra5443fWDcwoeF6luQZfv16_Qnhf87xSmtgPIKd_jvB3k-yC1_eFS_aakcRvOWDK1yitys-BnrZZbfO0dxV31wiJa3dsk4zyeLEUflI3o4AIHmMJF3Hlw6UdqeNI8Xw6b3Xb_IWQAeo47KEQX8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ekZUpj0gW0cKM0Anfm8_gOGpLgP9DSgknNnCY5CmEtvkooPMitwEv36jAuQ4NV4fnEb6ceWrT3u9N2PrTLDS9_ckJNXFIH7JdXphgb93yx6-unPtFmvyvzEn113SGO87uWrnTqUaqntkTaEAgjm9gx3FHbLZDw1EPmHsf_kV2MMJ3zMB5_DcyPY2VX-eFHkCHdUPCC14SdhCRVw1caBGpPQnlvC3XtStvm1FzpwIhdh0mCVrcMjJE_u9rpS4a92ZSkhRN0TDFWCc4R1FbRPCSG95m6b8sZm8k2nIO3pwrn-GqHmzld7O7geLNVGtIbnLDGsw8XprD9_LbUBE0OJcdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/edrmWs3VO5R9tSleffsDun0FM_9TU1PjRzb-hENXV3oTCrbUmBKqp_WubkHMQuC7zoTKfqgkfUrKFmdrUgehlr4t7oVUvUewRqR-5JNp7FpD0sP1VmZYtf8csNrUtLHD1h0eYWh1bWeyLHG6rrz708_9DzCC0OlXtcSId-hwv4jcgnm8bu8sM4xvumZIjyjiY38Qf3ez02WzyTyGO2s5vJu_lf8vBkQEFNvSyeNdx5qsSWZNkcvpQr0zxw7l3zrjZ-ZOTo5w2MtwE8_ASuokWp8WK-awAExejMkXV_qAYVNQr6aQSlWIiudn_zmAYIPHiTDHJhgQFRHH3ymSReViZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGpS7Z0RWhJPORDthqu3WVYBGeaqMw0S158q-z9amTJmgVsNWtA1cJetWZcWTQcLW2UasElWFjtDJ36n_vKEwFJd8-5ucmTFgrTlZWyxxA20UYEUG5QXX0aj-FlFYJk67NbdrjK7JjrviyCJayL61TQR2QSUiZN6lO3lDTM5cv6JO9XkFi0GAaNrEtJr9YtWtiQtzrp0iJlCo6FA534dAylOQNXj_7k739OOjOI7wp4HSWSF1LplJhbLZaMbL0KjsQquz0b2aJJBKpJtSncrRuT_yqny28_cW3QpKp8IVFRKZM6jy5ZzPZ5bhM_cBKIXzjwYeHxgwYvFszQDfnydhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BtEEeit5U7rgCEvsJ49ixtec3qnshkvE5ggpYL6TckAbvKPbom9wBTUcWwm6-7DIHRl5b5eDiPqVOhR2TlP2ZcuW2t1j8rPfWaeXahXIP-wBsLYobASOkbMqhXjYWEH9rkvW6L76372OMl6P5zhrIo9ExlHVaNvmE3NW_TFymhNUpsIk9IGU8iBowKBxrgfO3uL4D-91_JfzAEnXH2DCZib_tRGBfxoyLsIOsIRcv8WdADw5ynkL4Oj_RYte5Hz8rrW4oDFG7TnCFqG6LrsJKHAuPY_YQcJwa4pEgPElWKJDH1_yX7SiAYslQpsOEFbCz3_EXLJFHlbq4XN9BytixQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عطر نان و زندگی روستایی در دامان سبز دشت مغان
اردبیل
عکس:
رضا خانبابائی
@Farsna</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/435131" target="_blank">📅 17:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435130">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2H7EI17U5vpdFLPbwatb1o8M8G88XPYWZetmNgub4xphRNXWf2RvzuUYbLM5lHic5LzePc-59DI7LKBc3R1qrqeZk_ZxIwR_u2UaPM9NkrMlRkibg-6eHG_l53BnI5aDO24jVLLWwSaimZ9BZnHpH8Lp9L4rk9joQ6jbkEMtl7lFWpAjiG8sTRtUTrJ9Y4woHwjax7JGH-jh6GYZ3C99Fo9WRYyCu0AYFMXJhmNnLEROdJar-gWIp1GzJR_CrEQzkW2Na6qiS9JZfMOvpAUQdOGCS3MrEYNPbn0jcKQ8nfCTY4R97aA1_IQhjFwfuaazsVgQgLVXON1LLoJP12m6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانهٔ عبری: زندگی در شمال اسرائیل به جهنم تبدیل شده است
🔹
خبرنگار کانال ۱۲ رژیم صهیونیستی: «زمانی که عملیات‌های رهگیری و تیراندازی از داخل اسرائیل به سمت لبنان انجام می‌شود، زندگی در مرزهای شمالی به یک جهنم واقعی تبدیل شده است.»
🔹
این خبرنگار می‌پرسد: «تا چه زمانی قرار است در لبنان بمانیم؟ آنجا چه می‌کنیم؟ ما فقط به یک پاسخ درباره مأموریت‌مان در آنجا نیاز داریم.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/435130" target="_blank">📅 17:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435129">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad0a7cb8b0.mp4?token=JuNqJB3DbOoRDDLAfvpliyr1hNQ-LTnDXNXr-Jb43D9GxO0W7I9GtR_r9rKodhmN9dA54ctyC6lUPTnVAE_Z5FqoprbYT4BYa5kU5ZsxZkbMKoh-LM5nG2Ye747EnseFRwJu_IXZPAULS4sGkP-K1FGH1O2AzT6XFVGvchdLFCD3aQamW5KOOikheH5MkmGMHcJRM5qXHBTGxJ4V4mn0sPznx074kZlGdWY9pRadS2nf45cPuymspQflt2oxphVOHdu4KStjQfaojwzhO6Psh3AfpOUcvF6w71lxW3hNTWucGv8Ib6ASb2o346ialwqMRZGOyvXD0rxhXywxCDaGYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad0a7cb8b0.mp4?token=JuNqJB3DbOoRDDLAfvpliyr1hNQ-LTnDXNXr-Jb43D9GxO0W7I9GtR_r9rKodhmN9dA54ctyC6lUPTnVAE_Z5FqoprbYT4BYa5kU5ZsxZkbMKoh-LM5nG2Ye747EnseFRwJu_IXZPAULS4sGkP-K1FGH1O2AzT6XFVGvchdLFCD3aQamW5KOOikheH5MkmGMHcJRM5qXHBTGxJ4V4mn0sPznx074kZlGdWY9pRadS2nf45cPuymspQflt2oxphVOHdu4KStjQfaojwzhO6Psh3AfpOUcvF6w71lxW3hNTWucGv8Ib6ASb2o346ialwqMRZGOyvXD0rxhXywxCDaGYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربهٔ سازمان اطلاعات سپاه به ۵ شبکهٔ قاچاق سلاح
🔹
سازمان اطلاعات سپاه تهران: ۲۰ عنصر در قالب ۵ شبکه سازمان‌یافته ناامن‌ساز، وابسته به گروهک‌های تروریستی و قاچاقچیان سلاح و مهمات، شناسایی و منهدم شد.
🔹
از این افراد بیش از ۵۰ قبضه انواع سلاح گرم، ۷۰ کیلوگرم مواد منفجره، ۲ هزار فشنگ و مهمات مرتبط کشف و ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/435129" target="_blank">📅 17:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435128">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حملهٔ‌ حزب‌الله به محل اختفای نظامیان اسرائیلی
🔹
حزب‌الله خبر داد با یک موشک هدایت‌شونده، یک منزل مسکونی را در شهرک «حولا» هدف قرار داده است؛ نظامیان اسرائیلی در این منزل مخفی شده بودند.
@Farsna</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/435128" target="_blank">📅 17:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435127">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8c9n7sRawew4cXAenxMR1MEaVVfJRF_hqSDskV1N0Glu56PDv5LJWziw1jheCKOF5OKo3uUrIU4HAuoH2x7A-XZSwKFQRkVbQGdla4mmYjCOyuRweh7fff3jbf0rTZ3-ur69AFQi4aaHFWaDFqP6iXIAaG26_SKQHZbbln5tVUcaFcDb2UDyjotZUyvuPYY96ShtbfR1LqnAZKrfXZNrZnbaZAdSSygmGbAW4IXCGPveHzMJBurEUOMfN5Rvgqu0ngAnsF9mlXUvdg_zCPSiA1HrMrjSeHY8fmLrYPpDuion3K8tDGdLOCZDZoGFrY_ZHjQqHw7LcmobSlo-W6fUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نفتکش قطری در تنگهٔ هرمز متوقف شد
🔹
طبق گزارش بلومبرگ نفتکش «محمزم» حامل محموله‌ای راس‌لفان قطر، وارد منطقهٔ تحت کنترل ایران شد و پس از دور زدن متوقف شد.
🔹
سیگنال‌های این نفتکش که مقصد خود را پاکستان اعلام کرده است، نشان می‌دهد که اجازهٔ عبور از تنگه هرمز…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/435127" target="_blank">📅 17:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435126">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLOg_OVy77IAWpG7U3St2eQkz1glEq5cWWJ-hTNqya4VjVwsoYB6xcSN-SXbeRrPeNi1fek6U9wDCvqCxHlAlPr4xtX0-QRKClbyriRaZ51X6mg53cIjDnBrbdxOcdX9u3B4hJb7sQBl4HDuj9-FLsVupAYvh5UD7bb-WtxKcJbNJH22hreG4fKXup0rPzxn2oths_2NoDuZ2-W_QG0a1xeilhqmolLiMkssnEHS7ASwfX9DXsIbEbgzVshJIehk6esQAsCbJH3u6iKLbYZI6hyFfl2j1m4OOxW433QyskH8_yrZHIkbs3N3ldBo_1WctsbWRsNonjOKSfVvHPaAkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی به هند می‌رود
🔹
سیدعباس عراقچی وزیر امور خارجه جمهوری اسلامی ایران برای شرکت در نشست وزرای امور خارجه کشورهای عضو بریکس به دهلی‌نو سفر می‌کند.
🔹
رئیس دستگاه دیپلماسی در این سفر ضمن شرکت در نشست وزرای خارجه بریکس که در روزهای پنجشنبه و جمعه، ۲۴ و ۲۵ اردیبهشت، به ریاست هند و با تمرکز بر ثبات منطقه‌ای، همکاری چندجانبه و تاب‌آوری اقتصادی برگزار می‌شود، با سوبرامانیام جایشانکار وزیر امور خارجه هند و سایر وزرا و مقام‌های شرکت کننده در این نشست گفت‌وگو و تبادل نظر خواهد کرد.
🔹
این نشست، مقدمه‌ای برای هجدهمین اجلاس سران بریکس است که قرار است در شهریور امسال در دهلی نو به ریاست هند برگزار شود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/farsna/435126" target="_blank">📅 17:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435125">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">جایزهٔ ۱۵ میلیون دلاری آمریکا برای مختل کردن سیستم مالی ایران
🔹
وزارت خارجهٔ آمریکا از برنامهٔ «پاداش برای عدالت» خود برای پرداخت تا سقف ۱۵ میلیون دلار به افراد همکار با این کشور، با هدف اختلال در سازوکارهای مالی سپاه پاسداران خبر داد.
🔹
این اقدامات در ادامه کمپین موسوم به «خشم اقتصادی» دولت ترامپ علیه ایران انجام می‌شود در حالی که آمریکایی‌ها خود اذعان دارند چنین اقداماتی تاکنون نتوانسته اقتصاد ایران را از مسیر توسعه و تعامل با شرکای بین‌المللی خارج کند و بیشتر جنبه روانی و رسانه‌ای دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farsna/435125" target="_blank">📅 17:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435124">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🎥
ضرب شست اطلاعات سپاه به ماموران موساد در ایران
@Faesna
-
Link</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/435124" target="_blank">📅 16:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435123">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lw3etR7GZ2Y_w-NZSe8Y_I7XjAXRIfnPllimaK-4qX7t-WAbRmCkitlIzS41Jk-FOREDT8zzjUMxgHzdSPIXcMrrCKfdcbSx5gzBobbKQhghOH49uh7r0eM6-kLv1YDdcbYS5LT8J_NwxUG2Xw8SQJdE_oOBj9xcWlAGFW3ASDijB7K6O0VOoBfHTGYFSgGhRJ39UHgDraPdVh6KdLCYaTHNG0pOOv3RyxB0ahTOvUZHXc6BsxR8HjF9nLSO8Fh7BKX9US-cM0aeZkBPDlZwsmK1O-9T0S2_R59oQGYPtA5o-Ysk7GFOOu7KGCBQS6SgEIevyW60cMxfy8Fxn2QFJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی کمیسیون امنیت ملی: یکی از گزینه‌های ایران در صورت حملهٔ مجدد می‌تواند غنی‌سازی ۹۰ درصد باشد. در مجلس بررسی می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/435123" target="_blank">📅 16:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435122">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jutIZpdvvSCW1Mr94NrAjN1_-fcD_xsQSHkkJf50sY-uDvbwesAWt0RFOr9_6yNsNEeOjCzRhLwXES2xaEtL2zg1vBnEvvb7DUjBZhQdNEY5Id7SKETgXnnA9qqfT4NKod6zgcixuCBRVAiIZiFllADaeqb4KiniB-CS2tO6IvK-T9XG1asD-cMOBp7xvhGQThOiuii8YT9NnoixaTqMx1JY4VdnsxCM3qsu9vroWeNJipuFaz5tde0T8audSK2LdSRa1bdwiagIe9FOk3QbeYooyfE1kacXYI2iTLocZRW_q1fN5rupdVurXhLcDFzAAvsx2JrdJ4Gsrhy-6XINQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان اداری و استخدامی: ساعت کار اداره‌ها از ۲۶ اردیبهشت تا ۱۵ شهریور ۷ صبح تا ۱۳ خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/435122" target="_blank">📅 16:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435121">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">در تنگهٔ هرمز، کابل‌ هم حکم کشتی‌ را دارد
🔹
رئیس اندیشکدهٔ اقتصاد دانش‌بنیان: در تنگهٔ هرمز طبق حقوق بین‌المللی، ما این حق را داریم که همان تصمیمی که راجع به عبور کشتی‌ها از تنگه گرفتیم، در مورد عبور کابل‌های فیبر نوری نیز بگیریم.
🔹
یعنی شرکت‌های عبوردهنده و ذینفعان این کابل‌ها خود را ملزم بدانند با ایران دربارهٔ این موضوع همکاری داشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/435121" target="_blank">📅 16:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435120">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7af0ab7803.mp4?token=eYez1w4N6D5WGAqU_S8AFkaqt6HLFO310JRsZbql7T3xyilWXcg-X86wuuSStLfUof40cYZjA9zz9MtUvnPM9hGN99ymqIBs9FITS9u76NX-sUYaCO2MiNkFQ0uq575ZquDuZ47MeHNSXYq3RD0trdqqsSI1cdDkcKF6AlP0g8SzUAXTAOaZ71v5MsAkl5Xp9MVStdRXf6GSZlOeeLQOH4okbwat6jdlnAHAUI82lwXMqfo4AWsTWXUZYtq1Wu8qIoG76Tuv9_8R80tq-rZNMl2sZ7bXddiVft6UCFL4QVu84PHoJVbR_hQ8WqIMws_-MRCayFUO-x7VUp6ta6QXnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7af0ab7803.mp4?token=eYez1w4N6D5WGAqU_S8AFkaqt6HLFO310JRsZbql7T3xyilWXcg-X86wuuSStLfUof40cYZjA9zz9MtUvnPM9hGN99ymqIBs9FITS9u76NX-sUYaCO2MiNkFQ0uq575ZquDuZ47MeHNSXYq3RD0trdqqsSI1cdDkcKF6AlP0g8SzUAXTAOaZ71v5MsAkl5Xp9MVStdRXf6GSZlOeeLQOH4okbwat6jdlnAHAUI82lwXMqfo4AWsTWXUZYtq1Wu8qIoG76Tuv9_8R80tq-rZNMl2sZ7bXddiVft6UCFL4QVu84PHoJVbR_hQ8WqIMws_-MRCayFUO-x7VUp6ta6QXnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای پیگیری آیت‌الله نوری‌همدانی در مورد تعطیلی درس خارج رهبر انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/farsna/435120" target="_blank">📅 16:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435119">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3yqjxJHvwlllQ7L_i864lRe4mE2xuFnmAp_T9WlKbMTAK3_rRnNzmCwHOmB4bwZQV2ICm4sMySEbQ03CsxLHcjhE0EH6kTFYAvwdm9Dxyu0qrYI-pJ-U9brh1Gb_bMzLuUGVgplj0w0DK_Ry3-zLxG-cF6SShA6G2i71QwsJd1h8HOT4U9qc-FLSobSN2yUp9OuT4ugXEXu5vzKRkpM0LP2lRV0iWeSKqd-0P1kEEI2mC7-QzvC5UHuQvQOC9_giY3ZwhJaZ0012BsXBlqDmEvvS6y7LmgT5W1jgoDNpFquElSpaHgJp0LttFbrDzw1D3_aaemO0TBw00UDUDvuIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای پتروشیمی‌ها و احتکار در فضای باز
🔹
با وجود ادعای دپوی محصولات پتروشیمی در فضای باز، محصولات پلیمری در هفته‌های اخیر با مازاد عرضه مواجه بوده‌اند و بخشی از عرضه‌ها به دلیل نبود مشتری راهی انبارهای روباز می‌شوند؛ لذا متهم کردن تولیدکننده به «عدم عرضه» در حالی که تابلوی بورس کالا گواهی بر عرضه مازاد می‌دهد، آدرس غلط دادن به افکار عمومی است.
🔹
از سوی دیگر، پتروشیمی‌ها نباید از ابطال ادعاهای غیر کارشناسی برای خود «حاشیه امن» بسازند؛ برخی شرکت‌ها با سوءاستفاده از فضای روانی ناشی از تهدیدات زیرساختی به دنبال توجیه نوسانات قیمتی هستند.
🔹
برای حل این مسأله، دولت و مجلس باید به جای رفتارهای تبلیغاتی کنار انبارهای کالا، بر دو عدد کلیدی متمرکز شوند:
🔸
فرمول قیمت‌گذاری پایه در بورس کالا از هاب‌های صادراتی به قیمت تمام‌شده واقعی به علاوه ۱۵٪ سود متعارف تغییر یابد تا رانت ارزی از بین برود.
🔸
الزام به عرضه حداقل ۹۰٪ محصولات تولیدی در تالار داخلی با نظارت بر «کد نقش» خریداران، تا واسطه‌گری حذف شود.
🔹
اگر پتروشیمی‌ها مدعی هستند دپوی کالا ناشی از نبود مشتری است، باید طبق ماده ۳۷ قانون رفع موانع تولید، مجوز صادرات مازاد را در قبال بازگشت ۱۰۰٪ ارز به سامانه نیما دریافت کنند.
🔹
هرگونه انبارش بیش از ۱۵ روز تولید باید مشمول عوارض سنگین «مالیات بر انبارش غیرمولد» (معادل ۵٪ ارزش روز محموله به صورت هفتگی) شود تا هم پتروشیمی از تنبلی در فروش دست بردارد و هم نماینده مجلس از تخیل احتکار.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/435119" target="_blank">📅 16:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435118">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-text">🎥
خاطرهٔ ناگفتهٔ شهید سلیمانی از روزی که تا پای شهادت رفته بود اما دست تقدیر برای او سرنوشتی دیگر رقم زد
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farsna/435118" target="_blank">📅 16:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435117">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dd6eddd4.mp4?token=e0wZ-AuwAiMZIYeDIxG90HL6vVo_kg9onAUZ20R2PLrj01cbkcVH7iWBJq7QG-Xcp_MbuRNRq0dCNRgm5aPeMQZg-i_jPGJK8yuw3STaKpz-dYvczb2CFd5Kwdu_MAM-0oxxoMthW1j_BSvtzlrpSWkQY7I97fo_y1kWnAxKv31iSU0KIpqP3_MrNzAM9mfBo-rlsdgaru_idPMs9NNXn5FxxVMyFQuJUFeJbFXWTX7k5-Srx37uXIXR-i4ucu2dDhjZQYxVtXN1-n7hy19mQtfnaF8oDFzrwM_6VesvztNPT0Eyac7puUV7ZEbB6YVL1dcR0NpAcVh_58_6Gh9WSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dd6eddd4.mp4?token=e0wZ-AuwAiMZIYeDIxG90HL6vVo_kg9onAUZ20R2PLrj01cbkcVH7iWBJq7QG-Xcp_MbuRNRq0dCNRgm5aPeMQZg-i_jPGJK8yuw3STaKpz-dYvczb2CFd5Kwdu_MAM-0oxxoMthW1j_BSvtzlrpSWkQY7I97fo_y1kWnAxKv31iSU0KIpqP3_MrNzAM9mfBo-rlsdgaru_idPMs9NNXn5FxxVMyFQuJUFeJbFXWTX7k5-Srx37uXIXR-i4ucu2dDhjZQYxVtXN1-n7hy19mQtfnaF8oDFzrwM_6VesvztNPT0Eyac7puUV7ZEbB6YVL1dcR0NpAcVh_58_6Gh9WSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم‌هایی که از دست‌ها جدا نمی‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/farsna/435117" target="_blank">📅 16:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435116">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b57aec0e.mp4?token=r0ZSDawMPwYgcZ9m1oLun4n37FUu5tkHp7WCNIVrmV7DjNSBlzMF_4cwf7Zosp1QDtlIn-zs_elPZuxXxb0XI8nfTnFU4NMRRnGlsGNFxoT1VaJeCI3mQ2MjJmIF2xo-YeH7V5430zeCtVvoKNmqwTxCuk3bgTrOl4Qyn2tJ16GjCZYfpDk_V5GECevcLadVBymieiSPYB9FXz-QnY3x7o-FT30kPJoJyWAVChEw71mFjxhCbhhGbjjaezV4yXXqeuwb5VGL5L7IyI6PaXPCGju5G7GVISRdYjzOa7v5SXYf9O8mIKZKgqHwiuQ-OtRDV_h9QaboWBMkyxVz1c_dTIjyImzfJ_TRXOV_1gZmAhJER7Q5WcA5D4raaxQSpGv4jE4k5Qu06KsWZAXx8JuUD3oC6ysOH5tlmM8YuiHiByx4_wkYS41gdndNSSfAxoKXTkjMcDH5k1b6ueh7JynnfmkuAFpKpSOm2zG9tPh7FL1z4PSJCF1dPIlFUhtxdi4iLvu24PLGiO6Kpf5rU9upRAS2X-dA7YXkuzwCksjZqFh_nAmJxPj7PaYcuasFDZQs2vpbax5-dt1hWK4cTtByYlJmZ39qj4HLFletC-jyI7NGFvzjyu2ZqGj0VyykZFwZVfjWwY2Zbtcog7CNyT6jISbjg3G2zUb5xhQXmGo9YLU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b57aec0e.mp4?token=r0ZSDawMPwYgcZ9m1oLun4n37FUu5tkHp7WCNIVrmV7DjNSBlzMF_4cwf7Zosp1QDtlIn-zs_elPZuxXxb0XI8nfTnFU4NMRRnGlsGNFxoT1VaJeCI3mQ2MjJmIF2xo-YeH7V5430zeCtVvoKNmqwTxCuk3bgTrOl4Qyn2tJ16GjCZYfpDk_V5GECevcLadVBymieiSPYB9FXz-QnY3x7o-FT30kPJoJyWAVChEw71mFjxhCbhhGbjjaezV4yXXqeuwb5VGL5L7IyI6PaXPCGju5G7GVISRdYjzOa7v5SXYf9O8mIKZKgqHwiuQ-OtRDV_h9QaboWBMkyxVz1c_dTIjyImzfJ_TRXOV_1gZmAhJER7Q5WcA5D4raaxQSpGv4jE4k5Qu06KsWZAXx8JuUD3oC6ysOH5tlmM8YuiHiByx4_wkYS41gdndNSSfAxoKXTkjMcDH5k1b6ueh7JynnfmkuAFpKpSOm2zG9tPh7FL1z4PSJCF1dPIlFUhtxdi4iLvu24PLGiO6Kpf5rU9upRAS2X-dA7YXkuzwCksjZqFh_nAmJxPj7PaYcuasFDZQs2vpbax5-dt1hWK4cTtByYlJmZ39qj4HLFletC-jyI7NGFvzjyu2ZqGj0VyykZFwZVfjWwY2Zbtcog7CNyT6jISbjg3G2zUb5xhQXmGo9YLU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار معاون وزیر خارجهٔ نروژ با عراقچی
🔹
آندریاس کراویک معاون وزیر خارجهٔ نروژ که برای رایزنی با مقام‌های کشورمان به تهران سفر کرده است، عصر امروز با وزیر امور خارجهٔ ایران دیدار کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/farsna/435116" target="_blank">📅 16:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435115">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2QL--gvPUBSEslkkQflIp6XhJV46hub0z2daaSwAflAuEAyoJHcqiC4YN-1nxk3-Ax-z1Pi0YFw6BB5LpMfiIAWeYAHdaiwUVCHunKfJIE-Ptz9V9zi0RSk3P4IDieUwVb7oh76TU_mq53Jqs4Bb9uxi9j0Dt79fJVGCYodjB5CMfkC_hp3oqEgXqws92D1ltBgybjuZMpJNKiuCFjf-13129THI4gCqB-KliTilMijLG7wsE5RxQqGMJTInJI8OrU1JYL1KHJdZNRYLjMvPW2gWzOXaC0oaza0EY3N1vp-uUMswRbo73l0eURoJ8OfYUkFHFthDCI7NtCn3O_HjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای تازه ترامپ: کوبا از ما درخواست کمک کرده است
🔹
رئیس‌جمهور آمریکا در تازه‌ترین پست خود در شبکه‌های اجتماعی، بار دیگر کوبا را هدف قرار داده و تأکید کرده است که آمریکا قصد مذاکره با «کشور شکست‌خورده کوبا» را دارد.
🔹
دونالد ترامپ که در حدود یک سال و نیم حضور دوباره‌اش در کاخ سفید، بارها تنش‌های گوناگونی را در سراسر جهان ایجاد کرده، در پست جدید خود در «تروث سوشال» نوشته است: «هیچ جمهوری‌خواهی تا به حال با من درباره کوبا صحبت نکرده است. کوبا کشوری شکست‌خورده است و فقط در یک جهت حرکت می‌کند: رو به پایین! کوبا درخواست کمک کرده است و ما قصد داریم مذاکره کنیم!!! در همین حین، من به چین می‌روم!»
🔹
وی در حالی مدعی درخواست کمک کوبا شده است که مسئولان کوبایی پیش از این، با هرگونه دخالتی در امور کشورشان مخالفت کرده‌اند. مسئولان کوبا تصریح کرده بودند که «تمامی پیشنهادهای آمریکا که به نوعی به تغییر حاکمیت یا امور داخلی کوبا مرتبط باشد، مطلقاً غیرقابل مذاکره است.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/435115" target="_blank">📅 16:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435114">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🎥
رزمایش سپاه تهران بزرگ با رمز «لبیک یا خامنه‌ای» برگزار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farsna/435114" target="_blank">📅 15:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435113">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb3f9417d8.mp4?token=FKs9-G_k6DzDyYEUXm_RDZ65pbn0cgJGo_oDGCeLKNG1m3gB33KhHAdbS4D7fMgg5GbRzm4OdzFf9h6yTukYcW-vYqQg5-UZtvrirYl26mPAAhMRvPsYls15phvVb7yWWfHummBjkH3eR64Br709isbY0YQ2EzhNP3EpKI466hboPhcEqkQUk_g4XUoAsJrBcCqqVelsndn--QpEx846tB77KYVKPiyiOYvdzyWeXpuQkBpNOpW0696SskiGSMQeYvGU_OpEo7VG_9RN44SsUsctv9JrCPxsmi3bLlHwzVtexxyjuTm_dHa68x7St0Ko_NNQV7qsDclL3lHTpsww02RS9KkEXLwNBGop0HbAOkFMy3MYteXmgylzLLP0PEhT8l-6lNgwPQZVLB0JMOB7qtJ-U9r8iS-CKuM2EPm6JiSioLjJKwCxHOq8twWTBU7vg0bNgttZx8WKsRIPqqBFsceh_clKQp9O4FGg8rsePc0tQw366Hz3qgUdlIDazVINMSYb8VCFM2ZJ4cytLRla2xTzSeZOfybn7SCOMuOXSH0j3FBCjo1LSxZXHMQCPdCFDqwzYT0NmseYwZ2Cy8XRO6R0TMvIITjURjyUwYBuBUnscw4evyvXXz41V5ZZeaEfQRdYGfkHqJkS8uDIR5xw9Oopw5OGGHaG75bBwH_hosQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb3f9417d8.mp4?token=FKs9-G_k6DzDyYEUXm_RDZ65pbn0cgJGo_oDGCeLKNG1m3gB33KhHAdbS4D7fMgg5GbRzm4OdzFf9h6yTukYcW-vYqQg5-UZtvrirYl26mPAAhMRvPsYls15phvVb7yWWfHummBjkH3eR64Br709isbY0YQ2EzhNP3EpKI466hboPhcEqkQUk_g4XUoAsJrBcCqqVelsndn--QpEx846tB77KYVKPiyiOYvdzyWeXpuQkBpNOpW0696SskiGSMQeYvGU_OpEo7VG_9RN44SsUsctv9JrCPxsmi3bLlHwzVtexxyjuTm_dHa68x7St0Ko_NNQV7qsDclL3lHTpsww02RS9KkEXLwNBGop0HbAOkFMy3MYteXmgylzLLP0PEhT8l-6lNgwPQZVLB0JMOB7qtJ-U9r8iS-CKuM2EPm6JiSioLjJKwCxHOq8twWTBU7vg0bNgttZx8WKsRIPqqBFsceh_clKQp9O4FGg8rsePc0tQw366Hz3qgUdlIDazVINMSYb8VCFM2ZJ4cytLRla2xTzSeZOfybn7SCOMuOXSH0j3FBCjo1LSxZXHMQCPdCFDqwzYT0NmseYwZ2Cy8XRO6R0TMvIITjURjyUwYBuBUnscw4evyvXXz41V5ZZeaEfQRdYGfkHqJkS8uDIR5xw9Oopw5OGGHaG75bBwH_hosQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش رهبر شهید به ایجاد مکان امن برای محافظت از ایشان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/435113" target="_blank">📅 15:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435112">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pk-bsQVqRfKSrA8RMFs09KudNGYCW9nLHdWu7TIXoeLFf2ib0LZ1zz-kIG9fH5GD9WeAx6E0b4zSrYIuwx_22Op9MA2YrsOOBn2PXt1RcGxiT4UVm-Y1bdyNfOrewiq-WP9UCxYHhb4FEzKMZy8C8yWutVwXJYOxDXTTJRK6JDf5Gn_VVqkYYNa1d5gk-kXQqq9_JUp3hhaPOx8pDX-SXCZOYcbLFBev2kYIwEsH222pplwLKIn9ov1xqsEAhPwD9Ly12kGEOl_ZD1Uw4dTtLX33SvzniWrgOEQheViKU6w8YgRPw7iN5wORDn-tHfsbovzUfXwth0EPa7oYheOHzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه: عراقچی برای شرکت در نشست وزرای خارجهٔ بریکس به هند سفر می‌کند.
🔸
نشست وزرای خارجهٔ کشورهای عضو بریکس پنجشنبه و جمعه در دهلی‌نو برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/435112" target="_blank">📅 15:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435111">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/677c946765.mp4?token=KpJKFNtX3k6uxDmakF_K8M4eB02U_HE-52eCU6VBl2bc47LDZUksdj_azUtp9EBF6954g0DUUKxKgAOf-Bui4XX2taBN0gVolWbxKUG619jzjM4u-X7bB3HEp55w8Sk-UjZd_beL7fRprwvboToYgmxH1IKVjquhm43Z6ftTcFrvyj-a41t0AeGoa9WwGs81RiDWuOt-e1nFxTz6X36q4vEzlrLcR17mXI9jUbU1XcVM_kZykRUmhAy1DYUWog6T7ycCFJHWMyHYvbuCbP5Qj-FlDqH0BNBGlB6rarMiGrfyr0989-YLPMIa-D4O013aWFJJwHb2pO4IAXPiVrxhkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/677c946765.mp4?token=KpJKFNtX3k6uxDmakF_K8M4eB02U_HE-52eCU6VBl2bc47LDZUksdj_azUtp9EBF6954g0DUUKxKgAOf-Bui4XX2taBN0gVolWbxKUG619jzjM4u-X7bB3HEp55w8Sk-UjZd_beL7fRprwvboToYgmxH1IKVjquhm43Z6ftTcFrvyj-a41t0AeGoa9WwGs81RiDWuOt-e1nFxTz6X36q4vEzlrLcR17mXI9jUbU1XcVM_kZykRUmhAy1DYUWog6T7ycCFJHWMyHYvbuCbP5Qj-FlDqH0BNBGlB6rarMiGrfyr0989-YLPMIa-D4O013aWFJJwHb2pO4IAXPiVrxhkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجاهد: کوتاه آمدن از تنگۀ هرمز ظلم به دولت پزشکیان است
🔹
مهدی مجاهد، معاون دفتر شهید رئیسی: بعضی کشورها به‌دلیل تبعیت محض از آمریکا، در امور اقتصادی ایران کارشکنی می‌کردند. به‌عنوان مثال، به‌دلیل سازوکارهای مالی، کشور امارات در روند اقتصادی ما اختلال ایجاد…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/435111" target="_blank">📅 15:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435110">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9rHCFc6UkBIsIFTc61GnbD1ymA8lzsqT7sc_gJ5RKd-JG06NWmnRnGqD5QSY0n1a-Rk5hRSCpOppcpDLbPcd5xPrl9Vvbai0jCLAZjZQnrs6eqljBQfaV8jaLSKONUDME5lpk4vpNiPqy-nEamrPXBxRvQo5ddxhqHlJoK3alzgH4GuQpPavSsKMW0B1s9MHHVp9sdUuDQMdw5rZZj9IDsoZ6fr8JHiiRrMUY-ns6IGh0xR3_hTckGYjtYd_ik1K_B2_IibdIvgQOmiyw0vRkimLZpnj5PvLcXV9pYTy1kcc_xWgT9OTw7euHfeYXqHvoLJQ_H2ezpGS5oBT087dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگرداندن اولین نفتکش غیرایرانی از محاصرهٔ آمریکا
🔹
پایش ماهواره‌ای کشتی‌ها نشان می‌دهد، نفتکش حامل نفت عراق که با اجازهٔ ایران از تنگهٔ هرمز عبور کرده بود، توسط نیروی دریایی آمریکا بازگردانده شده است.
🔹
دیروز این نفتکش یونانی با نام آگیوس فنوریس، پس از عبور از تنگهٔ هرمز در آب‌های دریای عمان سیگنال ارسال و به‌سوی مقصدش ویتنام حرکت کرد.
🔹
حالا اکانت ردیابی ترددهای دریایی، منچ‌اوسینت نوشته است: این نفتکش حامل نفت عراق به‌خاطر اینکه از تنگه‌ای عبور کرده که ایران کنترل می‌کند، مجبور به بازگشت شده است؛ اگر اقتصاد جهان درحال فروپاشی‌ست تقصیر ایران نیست، مقصر آمریکاست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/farsna/435110" target="_blank">📅 15:19 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435109">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b3257d08.mp4?token=sxpFJSc_jnCVEniQ8IdyE7anh9pRp2KEgDvgS7W05Bc4olF4Oa50vmgUcpXIrF5zqHv-AmxbalQ5MqsSM3_Fd-mLDHVWAEXP-A7NTQPv3ANgpknbmQQnaNTeHysU8JIKi667Lu5AsuaNnybfBuR3Wl6t6A5RuzThBW6xezgPrZqDj8UKg0p8Fi_e3nlGF98g6N2W3n4dIaJl43WPn_DGWWPeLYJGC-IwYOnY_g0kUBmlR9J8kEi2xipXZAgCs6g36jbd8rDVWdW9MqlbqL3x68SI-Oh5EXs5sTNxWhTgvAFunvb0h2ckgUJQuIqXjn3a1PNLy4oJrJab3tsa_EbB3VEi8ksOfOORW3Xqibfn6yZMcUyE4AigS8tv-DNXop5lgUSfFh_h93PattvkmA7G-P7uy15GDgnE-pOLGXmEq6ZtYrx6ovFfclSJZowtQyshOW0oGXaS-6NMjHtLVqFx1g0v-2b-wv6ctBnK6GW6r4Elsxh_6xTaU4-wCC8y3JBmZHgP1IRosZBUc7fDc3NQuRK9tUB5IOYnuR_qs0_uvQ194r4unOJ3yQGV2lOvpBuNLWu5GEEfPW39I7A_g-JKuC7SqN8L4VJKFDigYKbkmJLqE6EZSVftuTzLKLrQQoPEkk0OjswZwFwlCVk_U1S9A2Z7wHiHU7Wk3AxgxElG-qY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b3257d08.mp4?token=sxpFJSc_jnCVEniQ8IdyE7anh9pRp2KEgDvgS7W05Bc4olF4Oa50vmgUcpXIrF5zqHv-AmxbalQ5MqsSM3_Fd-mLDHVWAEXP-A7NTQPv3ANgpknbmQQnaNTeHysU8JIKi667Lu5AsuaNnybfBuR3Wl6t6A5RuzThBW6xezgPrZqDj8UKg0p8Fi_e3nlGF98g6N2W3n4dIaJl43WPn_DGWWPeLYJGC-IwYOnY_g0kUBmlR9J8kEi2xipXZAgCs6g36jbd8rDVWdW9MqlbqL3x68SI-Oh5EXs5sTNxWhTgvAFunvb0h2ckgUJQuIqXjn3a1PNLy4oJrJab3tsa_EbB3VEi8ksOfOORW3Xqibfn6yZMcUyE4AigS8tv-DNXop5lgUSfFh_h93PattvkmA7G-P7uy15GDgnE-pOLGXmEq6ZtYrx6ovFfclSJZowtQyshOW0oGXaS-6NMjHtLVqFx1g0v-2b-wv6ctBnK6GW6r4Elsxh_6xTaU4-wCC8y3JBmZHgP1IRosZBUc7fDc3NQuRK9tUB5IOYnuR_qs0_uvQ194r4unOJ3yQGV2lOvpBuNLWu5GEEfPW39I7A_g-JKuC7SqN8L4VJKFDigYKbkmJLqE6EZSVftuTzLKLrQQoPEkk0OjswZwFwlCVk_U1S9A2Z7wHiHU7Wk3AxgxElG-qY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روزنامه‌نگار لبنانی: اگر به ایران احترام بگذارید، احترام می‌بینید
🔹
حلا جابر: کشورهای حاشیهٔ خلیج فارس کم‌کم دارند می‌فهمند که پایگاه‌های آمریکایی به دردشان نمی‌خورد و اقدام هوشمندانه، متحدشدن با ایران است، نه ایالات متحده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/435109" target="_blank">📅 15:11 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435108">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQtUkIbhff7NSpKFJ6iUizRAUssL6NPKyByHk9zK-dqqd8OW7fp0O4Vo_Kum7j6HkAPNYNUnfv_agmpsVnHo2ksqpM9doKIlwQzTN9QRmnD0CgPX0kPvnKs-vZEk3VWL7DYnonNwu9dvdPORoiMg076cdX7ADohpAxfI4OGtVZtNpaC8k-JEY5llj-W2wWWOmGCZJ5iSEPRDSaqI08Bc2QdykNFocm9TkoqXrMdd6vla7cBfzXGWbB4K3aTdDe1dNjUekVhkBYtoCKWxv8JXHjiuVreZuGPNE_zi3wwXftBWqbl3k-a96Ar_H5aCO52xTD80FhqaxkiK_nZ6CEZ-cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لغو پروازهای شرکت هواپیمایی فرانسه به ۴ مقصد
🔹
ایرفرانس در بیانیه‌ای اعلام کرد: به‌دلیل شرایط امنیتی، پروازها به دبی، ریاض، تل‌آویو و بیروت تا ۲۰ می (۳۰ اردیبهشت) لغو شده است.
🔹
ازسرگیری عملیات پروازی منوط به ارزیابی مجدد وضعیت محلی خواهد بود که به‌شدت درحال…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/farsna/435108" target="_blank">📅 15:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435101">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_8uX9n4C2LZrlgfARO6YSG1Sn3u2J6RGv8Z5R1e7Z3LLT7Z1URVOs3ox-H_u52G4MTpen-ueO0Zajiwo-TFykZGcztYcPJjP6m5ZcFxzCcVExQjliU-tZbWtHWU4qZ0jyp-i5LmhHQlyVQHi8ALGENEKPPMCWOByM8kY48bF2_kUFBvnVNakTP99RCMMxWfsyYEM17uTc2fmObGBFPiU0yuN3GALHy3KJ39aEkehU6oUJvmL95dABsn8f0EMxFPLMh8wjVrEXOrAopXjiDyYIRv1SCw1HiKB8M2EmwRr_YpvxbvUbj30TbvUX8KUrUT37QAfgbRYZq9olK9LsmylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7zZ6BtsbodBkfpVP-tdLJuyF4QFQv1y20jUUKr05I_KWCR7nJfykg7gBvAxFEseewGxkXVbytnP158nyHRh-cxHyAcu1gC4nlYZjtJvBcRpjOMOyuEs4Dalr3pOFNUdyVYohoHsM4yYQVFpsd3vlOOiz9p35PzEX12XzK5PibRvRTfR-DhXEZZy9UQMtJLVST2YOB5lTDf30el3l5hIOjOLQgqGMdJWMoaStjGCj_HaS6_Ae7EMES6G0ZQJwN2J-j0r2qS-RPH4qgwh4YmDHHCVB0fMTT7HTfHP3ZTVubh6xgI7V70I_LjD4XN9r15UYHeHeVJ3laoReaWWuY5PTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SzE4dKm5gnZk4H7xYWh1oBYOOu9_pVMIhi2BMgzcbPq3c_hYjPKfA7UpnKb_FlQy4_rOxj9Yz7m0w7NFdH_2k-4wveNCgwLeBGQC_8kDi5-LIFcVwsqK0v3oZMrne9woc3xUTk-jdQ4WaVkCryseCW_9hhYrsXbCUp3M5-a2pvMD7h7wg-bk9UemYWxzU81swASpXc_msHOeYLgZW7lTFtmmlHW9jtJm_GoH3HQez20L-sx3NIE60URI0XYVH3ZqxupQaSwIgZEB0ZogC6EsgssONjsrcCABzQ12_-vds0eJMJJXIvHJxykOwjXMHTxFl4qPVgudOM1oPEUKTPyh0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h23-swnWmmURgkb4qiidJaPWMVT-_7VXjHwBlqYQavk4Sf8DgmRUBRX3KqLnbvkeMTpTRqVIYwEFLHfMk0mkvWjgmeiw7qhGRK6GDda_y4eNLKxxfaSFzP4LE6wGCPesVKAcK5JTrzIeBmhnezvefAv1oK9_O2SXx25M_sd-anbnB2uZLXHWyD-82iuA3sW87jqTN9rxk9t2aXasvsPfkjHv99QL418AYDEiD4bWT2qhktQcCdCyHr5hRa4xGimGNQYzEaicJHmiAQZDeXc7yVGKdHyxs0PNS40k_VvzJGKp7qs9Uth75VZukfuT6ofZDjKge8C7ajzx_j4GQh0hbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCsQo7rbBQOFr6lv6hLlWMsHHheKwVQinsluutZctcFU2_60Qis6G0MZtTT5vig5enysXMomwivtj6S5iLPn5VHNv1JilzNSFWzwHqzy4A1tdFHbjSt1ZBX-y0Q-Vt6q9tP-NGnkXyXPtuWW6WPjD7znZAhBCGtPSgxn5WA0T0T-jSs_QyJ54GpaGwQVfeAy21lz2ReI_0pS4DuX9kTAu7ZUB83wnxZfuk4WvSqCXdGA6MVm6WXNzJY1l_8W9SsL9HXhTft961xI8RTGQf4vXDkEE4XLRKKvORNiU8ChWZxnsg-31E0WawsE7Mk2xIP0qNt44ljwC-jl0No_A_AzZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RKGfCx4-YPdWsUlvMyQv2U-cuSV3dz2sVdmANwo4ObVahOEyWf9hSN34rF_iwX4oO7q0a5-FNjl12v95FBMXMaNalWiEyTgocR5hCHlGeuxR9JRRK0_gR0T5YKAFP4FT36ZCr22w_1fyoZvzL3tZwjejN-1RDV6wUC1IKhtUB3K1CnypQhLifPJHOhkeXKq1Fs_CR_EA_t9BYkbo8C1cLFInflG41AyW2Sr9DBmHgXRhloRK9Ego8H-8xWPO9eZHKnOttKRmhF8iqsbGMAkXiSXEgc-eBw-lf0NztTJUHgRzJYKX1J_HUnWzr67eJnYY3dVK6hIpRIT_g1J5JndaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zow-eL_6AuFfAm4C4sF5XG0CWkCDdwEFEFSAI0OaNxd_6SKeB1bnS0h3mXZFcTa6MQm8AD9ZOYPKuTFqTnk1AaGch0ZfLWowZMGzv2jANBKBC83DBpjT8g0ag1zvUv7DRUpTVTHo9r_WftiQ7i_fwsvVdDrTlqXBE9nLygw-edJkuVF7Aob1K_HW9_nWnYc0VjcV9hgbvxbMtqSLNIXt4MSk5GWpoY8V8Wg8PPWhoH7CyO0x8ZOgfbl0e2in20_QE8fw-nNZXIYMHt534V4PQof3U6XjkngPXunJd7DFWf_2WRqkDePac6decZKwb5bzF0qHc8-GxNXgN7a-L4J2YA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پاسخ سخنگوی دولت به سوال مخاطبان فارس من دربارۀ خدمات درمانی برای کودکان زیر ۷ سال
🔹
مهاجرانی در پاسخ به فارس: خدمات درمانی کودکان زیر ۷ سال به سه دسته بستری، اورژانسی و سرپایی تقسیم می‌شود. بر اساس بازبینی سیاستی برای جلوگیری از افزایش خدمات غیرضروری و…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/435101" target="_blank">📅 15:02 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435100">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5152ed2193.mp4?token=g1miSkIhjvC4aB9m9RV6jM2gzb1dYcHtH59dORPcu-Lp7HDgmRYuNvYSgur1OJyFIWLhqFPlnrmoR_cbJFLrliHDUjZyiIftHysYKC2DFBMDSym_ylOEK2WOPRgTTi3_Ro0Ym7dGf7Hrw53m5hqQBRmFs1wo1PXTVDmRfLxqYVYYey4T75BYLHoJ-eOQ0Lx9sqq7YPR4MybbYj2EcS6U-ml8iTTtbUI6fT_B3grsLHfIetq0qFzk_Sq6Xz6p2JFlirZsAGamzGeZgWTVWkhIqwGkuyM7mGTesIIDajEhcVGv53959xYMx-mcHQvnR97YGUJ4xNT54xX1choUG0_Ba2acWKNYjH0JXdx3rfISintOvyHZZUl_Bmnbj5SeRCUXo9EF61gFlHtCrzPc5YGsOh25mGIiQDC29dKfKZ906246RL3xZaOwT1O-ToyI7oWZKSMo2YZy3tj7dOW_zGYS3Nv2ZwfCB8gnv7Wam771NJafpaARoPq8ACZEHvNC8y9GODf-MKTWNbvAIP3YC_6duUpk9_cAnASG6_dwJTXnQw-N68it7vm3q_eQRW-Xrl611-yxqCGk4GEXgTk-eEKBeSKyZu7QAZiUDrwUxgde_csLsRYN3iU0suj2V7GxccnrbPg2uMtHJeuVZgH0ac5vVrl5Oq34ClbfSABUwjGriyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5152ed2193.mp4?token=g1miSkIhjvC4aB9m9RV6jM2gzb1dYcHtH59dORPcu-Lp7HDgmRYuNvYSgur1OJyFIWLhqFPlnrmoR_cbJFLrliHDUjZyiIftHysYKC2DFBMDSym_ylOEK2WOPRgTTi3_Ro0Ym7dGf7Hrw53m5hqQBRmFs1wo1PXTVDmRfLxqYVYYey4T75BYLHoJ-eOQ0Lx9sqq7YPR4MybbYj2EcS6U-ml8iTTtbUI6fT_B3grsLHfIetq0qFzk_Sq6Xz6p2JFlirZsAGamzGeZgWTVWkhIqwGkuyM7mGTesIIDajEhcVGv53959xYMx-mcHQvnR97YGUJ4xNT54xX1choUG0_Ba2acWKNYjH0JXdx3rfISintOvyHZZUl_Bmnbj5SeRCUXo9EF61gFlHtCrzPc5YGsOh25mGIiQDC29dKfKZ906246RL3xZaOwT1O-ToyI7oWZKSMo2YZy3tj7dOW_zGYS3Nv2ZwfCB8gnv7Wam771NJafpaARoPq8ACZEHvNC8y9GODf-MKTWNbvAIP3YC_6duUpk9_cAnASG6_dwJTXnQw-N68it7vm3q_eQRW-Xrl611-yxqCGk4GEXgTk-eEKBeSKyZu7QAZiUDrwUxgde_csLsRYN3iU0suj2V7GxccnrbPg2uMtHJeuVZgH0ac5vVrl5Oq34ClbfSABUwjGriyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریاچهٔ ارومیه با ترک‌های عمیقش خداحافظی کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/435100" target="_blank">📅 14:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435099">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UP2lBVGLN1fabnZqB6xniJ97EYGgfo1pk-ig-p3vDWtkofWlFpHnzcMfIVViSXIkHjdUv_04Ddk_IlDEup1LnNdo0e8wFzrKwzM6X-I-rSBTYbqyPD4ALLKYfj13pRjl4X-bjrtqtSHND8ft-wI09gkECqS945SIqqyIF2g8oiqce6T4xeXyS3Png9qtCDpEjO8yfqCTmDQG3rCu0o37DzAooZHct_usQgZ7Cba89NCjaCNyYc5cfQPn0AFMltYgacjJaDfIrv03v2LXejudzKAFfim2CHSFehjzxsWxXCXm4nlgbHTF3TLmEgrjWAn3fOWmAA7inkS18clek539Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عارف: یک مادر کودکی را به گرمی در آغوش گرفته و دیگری کیف خونین فرزندی را که هرگز برنگشت.
🔹
چگونه جهان می‌تواند آرام بگیرد وقتی لبخندهای یک طرف با خون طرف دیگر جبران می‌شود؟
🔹
درد انسان مرز نمی‌شناسد؛ این را به اشتراک بگذارید تا سکوت هرگز به هنجار جهانی تبدیل نشود.
@Farsna</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/435099" target="_blank">📅 14:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435098">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
حزب‌الله: یک تانک مرکاوا و یک سرباز صهیونیست را در اطراف «خربة المنارة» مقابل شهرک «حولا» با پهپاد انتحاری هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/435098" target="_blank">📅 14:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435096">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87d25d355d.mp4?token=uKaFonbtlnqYr-DDh84bXzXjrZxb7_sZcn6PnhO5RhIvcAcC_qTXntrPciRIsKxw1nnHU2NdYjngVBTACEl4tuWEkV3of0K1lxqr3S81EBPhkM5FcpF4lEGY-zd08VmDKwyGg3LlviyPg0mmbZxWkU0YiACbFMQbZDv_SyJf9DVinezwjzz0lPi7JV_PxuN1gb57vRbKm3k1prFf37ssyxVxvXCCV3KSS08CuYQUgZrcs9lq8gd_xkG7dcqIMMHGcFgMRSC8_BYKkzyDwkBN1Mgl0XhFdEJFXS5WNmwheN9LjT0_zDSKULk4XenyDSNnf6ooRr0FqWk1VLLyqocmKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87d25d355d.mp4?token=uKaFonbtlnqYr-DDh84bXzXjrZxb7_sZcn6PnhO5RhIvcAcC_qTXntrPciRIsKxw1nnHU2NdYjngVBTACEl4tuWEkV3of0K1lxqr3S81EBPhkM5FcpF4lEGY-zd08VmDKwyGg3LlviyPg0mmbZxWkU0YiACbFMQbZDv_SyJf9DVinezwjzz0lPi7JV_PxuN1gb57vRbKm3k1prFf37ssyxVxvXCCV3KSS08CuYQUgZrcs9lq8gd_xkG7dcqIMMHGcFgMRSC8_BYKkzyDwkBN1Mgl0XhFdEJFXS5WNmwheN9LjT0_zDSKULk4XenyDSNnf6ooRr0FqWk1VLLyqocmKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ارتش صهیونیستی مدعی رهگیری یک پهپاد در جنوب سرزمین‌های اشغالی شد
🔹
ارتش صهیونیستی: برای اولین‌بار از آغاز آتش‌بس یک پهپاد را در ایلات رهگیری کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/435096" target="_blank">📅 14:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435095">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b9d012baf.mp4?token=EJkL9a5p0EXCoZgYIbO_pZRjGy-z_85xeexkhGWYnNCmGR5_jyvjEp6el5UYHSImPSeyB1lkthC65PpuUQ0UJc1VX4CgNu76H-wJMuv5TTLNMVCNlum-XsHLLH9XQYcmxkYKi9S-ifFUS3Q1gN463ndU9j6OmISm8XY3XvUoDBJ2LNmr7SO98UsxtOO-AHOEUtQpx3WvpnBpiNTtcpTbNabWAl5JPPjc63f66FZwC8cuJBOKfGsd9dqKyf3KiPe6NpwUpogEqyNAXAk_UJceoZ947iUNaX_X78Fac60tSHLOpfVCNTCbcFO8IMq5C3kYffUXoY6mjSY05w7mc9U4Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b9d012baf.mp4?token=EJkL9a5p0EXCoZgYIbO_pZRjGy-z_85xeexkhGWYnNCmGR5_jyvjEp6el5UYHSImPSeyB1lkthC65PpuUQ0UJc1VX4CgNu76H-wJMuv5TTLNMVCNlum-XsHLLH9XQYcmxkYKi9S-ifFUS3Q1gN463ndU9j6OmISm8XY3XvUoDBJ2LNmr7SO98UsxtOO-AHOEUtQpx3WvpnBpiNTtcpTbNabWAl5JPPjc63f66FZwC8cuJBOKfGsd9dqKyf3KiPe6NpwUpogEqyNAXAk_UJceoZ947iUNaX_X78Fac60tSHLOpfVCNTCbcFO8IMq5C3kYffUXoY6mjSY05w7mc9U4Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجاهد: کوتاه آمدن از تنگۀ هرمز ظلم به دولت پزشکیان است
🔹
مهدی مجاهد، معاون دفتر شهید رئیسی: بعضی کشورها به‌دلیل تبعیت محض از آمریکا، در امور اقتصادی ایران کارشکنی می‌کردند. به‌عنوان مثال، به‌دلیل سازوکارهای مالی، کشور امارات در روند اقتصادی ما اختلال ایجاد می‌کرد.
🔹
به‌دلیل اتفاقات اخیر، این کارشکنی‌ها ممکن است بیشتر شود. اگر ما ابزاری برای کنترل این کشورها نداشته باشیم، مدیریت دولت سخت می‌شود.
🔹
به‌همین دلیل بزرگ‌ترین ظلم به دولت پزشکیان، کوتاه آمدن از ابزار تنگۀ هرمز است و نباید دست دولت را خالی بگذاریم.
@Farsna</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/435095" target="_blank">📅 14:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435094">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آقامیری، عضو شورای شهر تهران: از چهارشنبه مترو پولی می‌شود مگر اینکه شورا یا شهرداری تصمیم دیگری بگیرند
🔹
طبق مصوبه فعلی، رایگان بودن مترو تا روز سه‌شنبه ادامه دارد و اگر مصوبۀ جدیدی تصویب نشود، به‌طور خودکار از صبح چهارشنبه بلیت‌فروشی انجام می‌شود؛ مگر اینکه…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/435094" target="_blank">📅 14:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435087">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CmgO-pvr_b1zMVrALxyKUjErUZr2E6jgva0-Mi2Hy2F319UpFc69zUSl_5AxMN1CeP9Qab0i_3h-jC0XFzXD0yQPfyXQubJv56y8O3P8FJq0Sm2ujP2P00QUJwYLaBcmvLyVOWF0BYKRBfvlH6QdUnEW0P5NBQsJez5JhSaFbV7w3y8AuPZyGq2PAT_uUAC0O2AWzoY668Nj_96ZB2amuZ0arUo9UjJmCf95Y8ZrV6aQz774k2EQF9f-9w12_0rLpbcDdImm6XPCTguFeZxThVGrZaqli7y31QCoZ-B0BnjsJcluX5sdpJ9PsdJt3tQSBge52f9m2j6U_9bcnm6oKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YCEBJxXsJGKlXgJyy38RG9Z9iJjlM3VTKgpkJg96Rx5GqYT0Zj7YsGObwebHXo9riJnPEefQV3sCzEMAq2sr_TKmQz1AcXXkM9ceMQzwB5h9FmZ5xxx2Y4VygYA3t50_oA0HWUjAajo3Q2hZbofL9ptOOxwZPM_0JPJExmISMOQNlvvfCk8O4LznghNbCF0iGY-PB3Ch4E5u_K13Hbm81csxiRJs85lH0zSmvzKdE1T9T5Dcj_vewQ9uL7nuLZ6Lgf7WsZ27NqmTFc1gy3Gy34S4jgL6aSu1QlorD2HC1O_tyBx8p3IktgBCe-61wBSIIliXBHekiWDp7LdCjiEnzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TZ4DHZrWQAnkcp_CxBbtWpR0bov-lpYJXEu5vZt4byDhLNCgzETBcbVm_dF4IfrZ2L2OoTc7LylRGslUHdsVkWqwvjWSvCKiQTLfIcF7eg5Xx2gUemtu_0sYMl68C6h9u-VU_UE1ChPSMAxXaB3oxWTsewHHwnZB7qBjRECgkAaSNqJR4hdujKNdV6Cy83HI1V2E4EPZR7T23vEsxfk4iJi0l5LbPmwGfoZO7j6A5aIM2gzUZ2LfFuzPo2r-9Q-sJYp60xvXpsabKOSrib84HAHewedBm2sZmL8_bwH7c41QUnBKVQWOnmvQ5Q7FymkpLGbw4QRsrszyem0gAwgRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dh3kY1rqHM9M-OsKbZ5EKcvR16C6YjAvfD0IauYEbKE2WCO2qLsH9-ssAs8dQUwxVgN65uzQvYAmANwdh7grEbc5qot2V2b4Y-0_LmO2hPLAsTDdK7-kLX_YppmyXoUvuiMlCCIFn2oWxV3JT0FGyLL-HOsVWht7IS6yIlr6LMSgS3jJgFxI8mQbDqAWwAYe4aueFfPiUuzLAdT_dI8KYrXbG4KeGYNFMBd5CW9srVAiyFx71-T22KwTniZSjAOzlfrEVzHDYjwqWylf2Rpv52wV_gAxO-lFJIBOr1dqSvXSoDECQdSVlgK5r5iV8_Zt-7JZ1eJjp_CuqB8D_sI4nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rq4DBM86PhueCEVkdQGhz4DACVCrYM1OBgb2v796I27rauTfl-yITxsdVPAcYFbSH41vfqq0YhquaTGVJrtg-8bUQ58Vcb6vf_GsTIUnP1auNsTfdkAKUOg7YaHP0CKEyeh7IIvr9Pmm-OGYILgoR0CekIewuvnEyoVUeh8oP6Anut9z6Ry9l5kRjXlFsIl1q-M9TVNycFAUgx4aDnmvjlRrPdObptlLf7R5G-ENJoCFQiLmlNQEKu_TKAfe1XTR8trnCsNF99DlOdJgugA7H2ijZwbIvxx0Aum3hfG5gkHWEHRMMrAlKbiRUB7tmOaf8ZOQAlEOkh1mDge4yawTzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q4UVRWhkKo3V-b86VzwQ5tJaJdQ45dfVZQfzEppx6ra6sVheCymTIIUN8ap0WMqEV_SDjbCwwVg_1aTO3cO25Rm0DBygmz_bew-1rwN1mVaAlrjZ7qUIbb0p8YM_IeU_FJ7OfsaZKtJEB_A9zJ7vAzcGmJRbw55asrbPAKfMxq8gOmglIyAQNFDVgmU9SMJTPXTzDN4s93YkCZ32Q6eF5u9Rd3L8ytK3GZYBbS8Ele7P5RB1N1_bHOSew0bA2YaH0gPX85p3mmBvHg3YofG8M0k9zCDChCduIL0UXTzj9ly7WfNLmhxexUZdKXM7yJ5WbzoKWRej_aD7Gp_Gjg3Ktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7YWm9dL0kbR_vN3oNQ3ryogIUBdoRGYdWHbfJyB8pBcq7I7Fr6aTZQlzwwefJuE-i2WIm-8S6PRGEE3Km3Cd29GrMuKTHv2JKjG4yVLRUm9nC7mXJdH8_7yZ66AE90XEvDomC7Xyb-CUo9ujzRSa8XX47GViLidHsvFK-SiUNcnujdCzV8nsDjSH7JBhHhq_rbQ2qEDchWewY3YS3EK8Dp7-uIJFebbnUfNgb-S3IMDGreTdaD1EsoDF67FcSpT-fzA4o97yBz6_QlZUuLvQkJd5FzJ7MEjXybhjjJhABVSDw6ert6RwcZ9ArdP9Pxws92_UK3RlmV27s8fcRIT0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین ایستگاهِ خط هفت مترو تهران افتتاح شد
🔹
ایستگاه مترو ورزشگاه تختی به همراه ۲.۵ کیلومتر مسیر تونلی در خط ۷ متروی تهران، امروز افتتاح شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/435087" target="_blank">📅 14:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435086">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MESBU58YxvY0ivXdnN3BfBUbe-1q7Kk0Eq9YyqHH58AGqjk_W6XA4YD3lIaGjviAFKb22Z042ZwW3-S5ZSCJcpgamrW3JzGWoCFaJO6w3tdmXNKT-hVeBjwT-lTf_tUULrqYOWnyXKJ7pEH9nD9Hyj13v6n2n0Xqgg4sJgXkseDcYb5mBAYdgdxRJ0Q3e0zSkdeDQSARGjVha1dz3-FbgK5_CII0qF2zThs0MMzN9AkP0Q_oiqLyl-5ZbWyMW8cLOesPvfcgX2WjCzg8aoUMCQlciMNVm57uAtnYwMYwnU21A_4gzOlykGArBK3eoiDVFpggOtuJTwyxfBQs6iEkSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسال پیامک‌های تهدیدآمیز منتسب به ایران به شهروندان اسرائیلی
🔹
اسرائیل هیوم از ارسال پیامک‌های تهدیدآمیز به زبان عبری به شهروندان صهیونیست خبر داد که در این پیام آمده: «به شما قول داده بودیم که به‌زودی ستاره‌هایی را در آسمان شب خواهید دید که ستاره نیستند...…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/farsna/435086" target="_blank">📅 14:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435085">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apGXzaz9wUsSihkOvYV85d6A5rGETlvBRIjCsjh9f5dGZRwEzySFf5Fv12u3uO4BCwKbjz3fQ9UfsHMD4KK5wkx2lVLjPynKvfHwZRm2hlmAnZEozAQSRXIC8I3XNHEJ2sNvpH_zr4ydtwY0y5fuIlO3zOn7yIQjBOYWcXgAYoiefPsAqkxtx5jeVtYibyubW-tBZlWd0gxUAwVbairjBkbGTZE9djxS7QUHKncT_zDWPL_Qr27muN_APWnXC-_U5NxB7zQSyjxwDgAIzg-fwwjn9r4sztsWYHAM-dGTHBPS427E5RFQZB8eyIo1Aofcb67xKhQztNEFqLCZpCiPUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«دان خوابالو»؛ هشتگی برای ترامپ
🔹
روز گذشته دونالد ترامپ، رئیس جمهور ۷۹ ساله آمریکا، میزبان یک رویداد رسمی در دفتر بیضی شکل کاخ سفید با موضوع سلامت مادران بود. در طول این مراسم که با حضور مقاماتی چون رابرت اف کندی جونیور (وزیر بهداشت) برگزار میشد، ویدیوها و تصاویری منتشر شد که نشان میداد ترامپ برای مدت نسبتاً طولانی چشمانش بسته است و سرش پایین افتاده است.
🔹
رسانه ها گزارش دادند که به نظر میرسید او در چندین نوبت مختلف این رویداد، در حالی که دیگران صحبت میکردند، چرت زده است. این صحنه ها به سرعت در شبکه های اجتماعی دست به دست شد و حالا هشتگ "Sleepy Don" (دان خوابآلو) که کنایهای به لقب "جو بایدن خوابآلو" از سوی ترامپ بود، ترند شده است.
🔹
واکنش کاخ سفید به این تصاویر بسیار تند و قابل توجه بود. حساب کاربری رسمی "واکنش سریع ۴۷" (Rapid Response 47) در شبکه اجتماعی ایکس، در پاسخ به یک عکاس خبرگزاری رویترز که عکسی از ترامپ با چشمان بسته منتشر کرده بود، نوشت: "او در حال پلک زدن بود، ای نادان تمام عیار." (He was blinking, you absolute moron.)
🔹
این پاسخ خشمگینانه با تمسخر گسترده کاربران و حتی برخی نمایندگان دموکرات کنگره مواجه شد. آنها با بازنشر ویدیو، این "پلک زدن" را "بسیار طولانی" توصیف کردند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/435085" target="_blank">📅 14:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435084">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در اصفهان
🔹
سپاه اصفهان: امروز از ساعت ۱۵ تا ۱۸ در محدودهٔ زردنجان احتمال شنیدن صدای انفجار کنترل‌شده وجود خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/435084" target="_blank">📅 13:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435083">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqL98RholiChFHRfm93G0Tf62L9Id054uCo5gwjfU00PgeUGFX4NkRi4UeKAGjTfTfXX_GX4_YVZxpO9uUd-fOND7HAh37basUOigsO4O9xMbY2-OdClZNOQPvzSlrEIj6bkGeDo0CPDQE1UkKFPKLcp9IMr51UFGzmT9PTNhM7YLkotT7XM8G7_YxZRY2807wY5v2qVrLmpbGyBL697ic28Qv6WKRWljjMdKDGbQhSJ4hioQ3E-Ezo2pgZRE2YQXp--TuQbSqe9EOzYT9EFCNusAUaZIqq3ystsWUg6VFIthNp6LhPqTqtEf_DZr4MuCdXV-B3qsp_DesPalK4qVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توری که امارات برای ۲ بانک ایرانی پهن کرد
🔹
وابستگی ارزی و تجاری ایران به امارات به نقطهٔ حساسی رسیده و به گفتهٔ خاندوزی، وزیر اسبق اقتصاد، امارات با استفاده از شرکت‌های پوششی، صرافی‌ها و حتی شعب ۲ بانک ایرانی به مرکز اطلاعات مالی ایران تبدیل شده است.
🔹
وزیر خزانه‌داری آمریکا نیز اعلام کرده است کشورهای خلیج فارس اطلاعات مالی ایران را در اختیار واشنگتن گذاشته‌اند.
🔹
خاندوزی به بازداشت مقام بانکی ایران و محدودسازی حساب‌های درهمی اشاره کرد که برای فشار ارزی انجام شده بود.
🔹
اکنون با وجود اینکه بیشتر کالاهای وارداتی فقط از مسیر امارات عبور می‌کنند، نیمی از تسویهٔ تجارت ایران در این کشور انجام می‌شود.
🔹
کارشناسان علت این وابستگی را عادت تجار و سود ناشی از ارز چندنرخی می‌دانند و پیشنهاد می‌کنند ایران از مسیرهای جایگزین لجستیکی و شبکه‌های مالی چین، عمان، ترکیه و تهاتر استفاده کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/435083" target="_blank">📅 13:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435082">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsPi3h-qqa8eCCHZxJ2gsXFi8UBt9QQG6c_i94s-IX3j6HRF-2iN68moxR-qWHxQVnlNqfWQ2V0xufGo8I_syVJpxvejSQTVxa5_6ibey077Uyu2T4nNHY7S4Zkk2zMA_GSwikyw4TShj4V9siesESWjNe_sf2q86OVMeuj-AOKvlbxTsu-sXL_T2BF2lpgghIHMD19d5782q4jqli5BUG9kdg8Nk8nZzodkA86p8hywGHGAB_wbsz522chrWJ5F-mrkmcuCsJKA4UJ1B-8OYpVgN7shHcI7aMfFJFixz6X4pgH0Zl1q_xIIfZiaVsNnQIGiky3fxn7gpowrxM2R9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت صمت تأمین نشدن قطعات سایپا توسط کروز را تایید کرد
🔹
مفتح، قائم‌مقام وزیر صمت: زنجیرۀ تامین قطعات وابسته به شرکت ایران‌خودرو، باید براساس قراردادی که با سایپا دارد قطعات این خودروسازی را تامین کند، اما این موضوع انجام نشده است.
🔹
از بهمن پارسال هزاران خودروی کوئیک، اطلس و شاهین به‌دلیل عدم تامین قطعه در پارکینگ‌های سایپا مانده و قابل تحویل به مشتریان نیست. تعداد این خودروها آن قدر زیاد است که خودروساز دیگر جایی برای نگهداری آنها ندارد.
🔹
بخش زیادی از این قطعات به گفتۀ مسئولان سایپا قبلا توسط شرکت قطعه‌سازی کروز که حالا مدیریت ایران‌خودرو را برعهده دارد تامین می‌شد.
🔹
وزیر صمت پیگیر ماجراست و در صورت اجرا نشدن قراردادها از طریق مراجع قضایی عمل می‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/435082" target="_blank">📅 13:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435081">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b219d0099.mp4?token=VJsk2IrlAuag6S5UPzi-pvwilRVFdytQPNaZ8APWVtvDH6YlOsW5VgPsacTgKHjMwnm4Hpn-26EC9JFifA4boKmEFF8_MPJS_nfzWgi0lsu1H-BjfssPvMAMZS_XO3Fi83M2wG8Y4cE-eEAZJ-gHcWs67wyUbhpfwcNKrz87BrrqBrviVGu4DSdbB8mDd1VC-gei8e8IHdJeVtr2YIRd7p-YpC8fuZMh1jp064W_SPlaLp0Dvm_obdwBjJhEByrziBtWKKe8TqBcw3qI2LlWCORhVbLRghaLICL3RHndeyar04st7IF2qMP1Np1CDPnBbjuiheD2qlC8hOmKstaqnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b219d0099.mp4?token=VJsk2IrlAuag6S5UPzi-pvwilRVFdytQPNaZ8APWVtvDH6YlOsW5VgPsacTgKHjMwnm4Hpn-26EC9JFifA4boKmEFF8_MPJS_nfzWgi0lsu1H-BjfssPvMAMZS_XO3Fi83M2wG8Y4cE-eEAZJ-gHcWs67wyUbhpfwcNKrz87BrrqBrviVGu4DSdbB8mDd1VC-gei8e8IHdJeVtr2YIRd7p-YpC8fuZMh1jp064W_SPlaLp0Dvm_obdwBjJhEByrziBtWKKe8TqBcw3qI2LlWCORhVbLRghaLICL3RHndeyar04st7IF2qMP1Np1CDPnBbjuiheD2qlC8hOmKstaqnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محل تحصیل فوتبالیست‌ها بازهم سوژه شد
!
@Fars_plus</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/435081" target="_blank">📅 13:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435080">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c04d602d9.mp4?token=Pc593oOO7UHTXgJSIEtWZPwhI8974pzLI08uL4Tm-RzVXp-avDPIAQTVLbB5VWJniSTTCePFZ1h7fEbgubXGrn4gq3P89wJvoI41soBydjHcPQiKkb-GPfSpVhv2EaQaLwqsYNPbW1lHmkYKoqT-RwKYSTd0jOKWHQZr0KjKoDsfJvrIwidfsUfu0H3OzzkZO-1aL7yH53gFMYU4GwodDGqE-SViLKesL5Asly_cfd5Hxe1Qx08FKLU41P4HufVowQYtL6Vm5N_aWUwLYiXy3asKHIKbq6_609PLPWMhaI9ttsqpX5ZoqtzPh4tMsgLvhPeN6wXtfrfzPsqNxt364A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c04d602d9.mp4?token=Pc593oOO7UHTXgJSIEtWZPwhI8974pzLI08uL4Tm-RzVXp-avDPIAQTVLbB5VWJniSTTCePFZ1h7fEbgubXGrn4gq3P89wJvoI41soBydjHcPQiKkb-GPfSpVhv2EaQaLwqsYNPbW1lHmkYKoqT-RwKYSTd0jOKWHQZr0KjKoDsfJvrIwidfsUfu0H3OzzkZO-1aL7yH53gFMYU4GwodDGqE-SViLKesL5Asly_cfd5Hxe1Qx08FKLU41P4HufVowQYtL6Vm5N_aWUwLYiXy3asKHIKbq6_609PLPWMhaI9ttsqpX5ZoqtzPh4tMsgLvhPeN6wXtfrfzPsqNxt364A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدای پرنده ترامپ را ترساند
🔹
رئیس‌جمهور آمریکا در سخنرانی خود، هنگامی که صدای یک پرنده را شنید، ناگهان ترسید و گفت: «فکر کردم پهپاد است.»
@Farsna</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/435080" target="_blank">📅 13:01 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435079">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: دولت لبنان نباید با صهیونیست‌ها مذاکرات مستقیم داشته باشد
🔹
ما بر مذاکرات غیرمستقیم تاکید داریم، جایی که برگ‌های قدرت در دست مذاکره‌کننده لبنانی است، و خواستار عقب‌نشینی از مذاکرات مستقیم هستیم که تنها به سود اسرائیل و به معنای امتیازدهی…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/435079" target="_blank">📅 12:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435078">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: توافق ایران و آمریکا که شامل توقف تجاوز به لبنان است، قوی‌ترین برگ برنده برای توقف حملات صهیونیست‌ها به شمار می‌رود
🔹
ما از ایران برای توجه به لبنان و مردمش سپاسگزاریم و از هر طرفی که در توقف تجاوز سهم داشته باشد، قدردانی می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/435078" target="_blank">📅 12:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435077">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: میدان را رها نمی‌کنیم و آن را برای اسرائیل به جهنم تبدیل خواهیم کرد
🔹
به تجاوزها و نقض حریم‌ها پاسخ می‌دهیم و به شرایط پیش از ۲ مارس باز نخواهیم گشت. دشمن دیر یا زود تن به شکست خواهد داد‌. @Farsna</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/435077" target="_blank">📅 12:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435076">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/889ffe9d37.mp4?token=sOhK7dTChTb_C84jTf3DPWS3nMD4NCIMDqkcxTfhqTFcwKlilZDBrprh1mT33PFvIvQy2hiym5jbtXDVIRr12-WgcAOFfnrMvMPZ4kIQXZf_FJAlqm2Mt1TFUaZK94B99SYbZXQ--JZf8LxHhAEnhR5rxIDseuCB44PXe4-1Gh5oSIPfA3JSSktBOqJMmK6hUV9S5qVIlM4hjnPMlz7oA783D-XqbGc4ME0T45alHbQlhikQkqe9ihsfiwtkjoZQpJUWNJV_8eqF4HxbuUcRi5OzISjYqmpfyhzsxa04tCT6v5a3IE_sjgyTvAbfAfPaGBU9oqz7cOX-gPLBb-tamg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/889ffe9d37.mp4?token=sOhK7dTChTb_C84jTf3DPWS3nMD4NCIMDqkcxTfhqTFcwKlilZDBrprh1mT33PFvIvQy2hiym5jbtXDVIRr12-WgcAOFfnrMvMPZ4kIQXZf_FJAlqm2Mt1TFUaZK94B99SYbZXQ--JZf8LxHhAEnhR5rxIDseuCB44PXe4-1Gh5oSIPfA3JSSktBOqJMmK6hUV9S5qVIlM4hjnPMlz7oA783D-XqbGc4ME0T45alHbQlhikQkqe9ihsfiwtkjoZQpJUWNJV_8eqF4HxbuUcRi5OzISjYqmpfyhzsxa04tCT6v5a3IE_sjgyTvAbfAfPaGBU9oqz7cOX-gPLBb-tamg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حزب‌الله تصاویری از انهدام خودروهای نظامی ارتش صهیونیستی با ریزپرنده را منتشر کرد
@Farsna</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/435076" target="_blank">📅 12:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435075">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: دفاع از لبنان و مردمش را تا هر زمان که لازم باشد ادامه می‌دهیم
🔹
هرچقدر هم که فداکاری‌ها بزرگ باشد، هزینهٔ آن از هزینهٔ تسلیم‌شدن کمتر است. @Farsna</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/435075" target="_blank">📅 12:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435074">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: هرگز تسلیم نخواهیم شد
🔹
ما با تجاوز اسرائیلی-آمریکایی روبه‌رو هستیم که می‌خواهد کشورمان لبنان را تسلیم کند تا بخشی از «اسرائیل بزرگ» باشد اما ما هرگز سر خم نخواهیم کرد و تسلیم نخواهیم شد. @Farsna</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/435074" target="_blank">📅 12:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435073">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: هرگز تسلیم نخواهیم شد
🔹
ما با تجاوز اسرائیلی-آمریکایی روبه‌رو هستیم که می‌خواهد کشورمان لبنان را تسلیم کند تا بخشی از «اسرائیل بزرگ» باشد اما ما هرگز سر خم نخواهیم کرد و تسلیم نخواهیم شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/435073" target="_blank">📅 12:44 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435070">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oR-Dc3aOtjVkCjKSTDkOb_tSKdZamkSNP_8s053TI9rDgTqLPJq0Wbu5rq9ha0nl6yrJVfLx2AyYvYXtHgH6HXnWIAP2sZalRw1PVxPsOAWbj6ZIvF4gEgYUltBbKiu_MkJrCdjmCsfyfxpz5TUGn6KMI0EYN-4X1u_0PSS5vPDdt1J1APEZx_GnrADZxn5Opodo8zkI2QQ8P62S4Tyh6qWTRMR6ZZVSTtPCVhvkueb8jjmWnuzwxzOmcZZik37wDqRrwdfI7dptiDYqmZfidFp9WTBKb2LK8zFq_kqwsZ97BNYORuc881f6xSodQgfrYar6L3lPHfQe-kCeqsxZrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nMEybxtgvT7BRWolkLrfyFe-8fqC10m12_o_lNWA15xn4_gr_gf-S3zYX8abFJpILFwPtLPY7t2OQ4vc4s62MbSLRA8S1j6O9Hrg0fOuyanlZiMa6FcJMtOGhh81JNNcQ_98v_ZjP_W7nG9WBmHVQiC4xKJn2vBiqhqIqW0qWYumoWAD3LkOgSpfhi18GmyxIwVXkYr7ORPQf_9CxXGidJ-bbI7-fdGuJmPr_YE8wysuVabxPULm3f7jCyNDlmPDgEFAq5flVXtOxfpZ1EHDjwWm0Cxp0qGQAWCTL7o-PSl2UcYcQwIX7I-WyzUn0IKe83GCADA50PM-CAWc7EYq9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pnc235MAltDw2uaH-oMpYJkHEHoPwTiciPooqpMpWFqj6La6eI2PbxfrL1kkacUD04lgd2TKYi0j3NBfYn_DP9Czlyqj5eAU_JwZZ1VDvVvC3S9ykTznFuBJuFBr1yR8cmuBkHo5bBUPmnjxs8pbdskVxARtjevsgVivrMasB6aw4Wsi4Shu96d7oaA0g9wyFtbTW4-82gr0ZYtO67rp1DW997LNQ2xsvJ_oeZtu3Mlkjis1mOAI3GEtu4rdKWBjmZG0KUawYEBni8SZTqmgMoFqnBQgqy9eRpRTT5yNs3m38HlSlGV_9nGaQbF4sju79aO1pZsI6i2SGMP3okrT2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ارسال پیامک‌های تهدیدآمیز منتسب به ایران به شهروندان اسرائیلی
🔹
اسرائیل هیوم از ارسال پیامک‌های تهدیدآمیز به زبان عبری به شهروندان صهیونیست خبر داد که در این پیام آمده: «به شما قول داده بودیم که به‌زودی ستاره‌هایی را در آسمان شب خواهید دید که ستاره نیستند... به زودی خورشید را در آسمان شب خواهید دید، اما...»
🔹
کاربران معتقدند که خورشید در آسمان شب اشاره به حملات موشکی و پهپادی ایران دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/435070" target="_blank">📅 12:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435069">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انفجار کنترل‌شدهٔ مهمات در بروجرد
🔹
فرمانداری بروجرد: امروز و فردا انفجارهای کنترل‌شدهٔ مهمات صورت خواهد گرفت؛ مردم نگران صدای ناشی از این انفجارها نباشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/435069" target="_blank">📅 12:29 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435068">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انفجار بمب در پاکستان جان دست‌کم ۹ نفر را گرفت
🔹
در پی وقوع انفجار در یکی از بازارهای شلوغ منطقهٔ شمال‌غرب پاکستان ۹ نفر کشته و ده‌ها نفر دیگر زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/435068" target="_blank">📅 12:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435067">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
پاسخ سخنگوی دولت به سوال مخاطبان فارس من دربارۀ خدمات درمانی برای کودکان زیر ۷ سال
🔹
مهاجرانی در پاسخ به فارس: خدمات درمانی کودکان زیر ۷ سال به سه دسته بستری، اورژانسی و سرپایی تقسیم می‌شود. بر اساس بازبینی سیاستی برای جلوگیری از افزایش خدمات غیرضروری و کاهش پیامدهای منفی احتمالی، فقط خدمات سرپایی (مانند برخی آزمایش‌ها) از ۲۲ فروردین لغو شده است.
‌
🔹
خدمات بستری و اورژانسی کودکان زیر هفت سال همچنان به قوت خود باقی است و نگاه حمایتی دولت در راستای سیاست‌های جوانی جمعیت پابرجاست.
🔹
معاون درمان وزارت بهداشت نیز در آذر ۱۴۰۳ تأیید کرده بود که مصوبه اصلی لغو نشده، اما این تغییر جزیی در فروردین اعمال شده است.
@farspolitics
-
Link</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/435067" target="_blank">📅 12:17 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435066">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkiAxrtZUVLUMwp4tJ9nvsAP2gTdVAo_OhwlZNRxLa70-EEKAz4bXWU6OmanavQTxbzTG8a9TBoTSss3eNHRCNnRunzMTLf4gcFDDFRRQTxr67IQ78RxzhyIQ4H-vM2AySPaRpBrWQ2zKMTgl3m9j2Y_hB4VXd6jtzusQo5ZGbihSPAYyuZwQphUq-GMxdNVkoW1WkZbzc8tw8x00YWzXON6pOyHCli4Zraoei0hr_lOZ2s9aRnrIeXt3CtHFkfZKOnQgmfVuELgODJt2IWBYr7Rw4XukIj1hNUNrW8CmDMOIdRrmL7M9BdePcD7youEeeHmEbBkGuQI8P-q-8DZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۷ همت کالای قاچاق و احتکاری در کرمان
🔹
فرمانده انتظامی کرمان: درپی برخورد با مخلان امنیت اقتصادی در ایام اخیر و جنگ رمضان چندین انبار و محل نگهداری اقلام مختلف و کالاهای احتکاری شناسایی مورد بازرسی قرار گرفت.
🔹
در این عملیات‌ها بیش از ۴ هزار تن میلگرد، ۱۴۰۰ حلقه لاستیک خودرو، ۱۰ تن برنج، ۱۲۱ هزار قلم انواع لوازم آرایشی و بهداشتی احتکاری و ۷۲ هزار قلم اقلام دارویی به ارزش ۷ همت کشف و متخلفان دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/435066" target="_blank">📅 12:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435065">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/621ce4d683.mp4?token=hV9z8Xt62h30U04Sumr_ohN6hhFuTWFR4l6Svcmyi_p0DUDHRyMpJ-C_QtAFAPh0CwkbAu6ndv3ivwjnXXoxshgCM07acAdcPHXcenYc1XOOPEI0AEN1CF0VwoGhQyCUqvsn62sp3bH8hi8cr7Jr69MVB4CiygCh6RA-83HPvKSjak-LFVNcOzBfg172rFbXv1PSxCGtS9wEHhBz44WVEA7fTqZbrdxXDi2IKadgNtg2LPrVEdpItNc-d0Jb0HTNq5y8fmx5HLdO4AefdxN8Ms5whrm4StTYrLM3KL_h10h_h0o96SG5aa-__i4qmbshAEMAR-Bz0FPnEL29ZC2CGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/621ce4d683.mp4?token=hV9z8Xt62h30U04Sumr_ohN6hhFuTWFR4l6Svcmyi_p0DUDHRyMpJ-C_QtAFAPh0CwkbAu6ndv3ivwjnXXoxshgCM07acAdcPHXcenYc1XOOPEI0AEN1CF0VwoGhQyCUqvsn62sp3bH8hi8cr7Jr69MVB4CiygCh6RA-83HPvKSjak-LFVNcOzBfg172rFbXv1PSxCGtS9wEHhBz44WVEA7fTqZbrdxXDi2IKadgNtg2LPrVEdpItNc-d0Jb0HTNq5y8fmx5HLdO4AefdxN8Ms5whrm4StTYrLM3KL_h10h_h0o96SG5aa-__i4qmbshAEMAR-Bz0FPnEL29ZC2CGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیروزه جابانی</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/435065" target="_blank">📅 11:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435060">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JS_CfwnhJlwkxnTQ-LoMIsspQ4lyIx5HKkkD4VFgYUD8cYTbzrY4J8_2ikRJkzTXm7paPe__U8MXIFXT3R4WjA0sWVTCfORS85exvTKgJUW9wIj0_OwjnrmwpzGnR3eSrPDQDMUjbt66J_w8UEXABQj_cK2YecKkZJWjEWbZJdCZ70Z4QACp4GjFednEJyYcviIGNMhP616-pFts2IUxCaIKYLgE_XsksX_4AoGJ4nzPhXxK8UhlmiMlH8SYuHd_Ed2EQPjO8tbUooVEUjiDPOlYV7aiVgZOOYKHtywZ8OLDk8zn_gUUbPA3QpfvwELXFVWQVROBQVPMjtR4rkoigA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h83xJ0rm6kYcVMyZxVjT6OtK7zq1aB9ieaYwTA6dvpDbTBCalcJYiTrlLSSYV9om_M7mymH_-UwGdsNiqNxwNHUyEPiAD9zHXwxQHy0Q1rE81cfr0t1bl0INntluESJs_DniGoEAYa_-_o02IykLtEqdVcnePELn-0rfolNZcdEPKxT2iwuM7dPNUfeCX_69cQgnZ0jX5L2hZ0ifQCWhn3LFjiwX0LtSKVaT23UVnimXLAOsvw9rGxb6D3BtTOnx3xXUYX1ADMJ1T1ZFyKA4SJWRZnUyknLWC5ZKuDaYw5VB6oVIrQgEvqKA5PuwDsBTemMmpCEvvw7dYZnHDNNAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bk7J4usr6nAiImrh5qpO8FnvqYpf09oUzboZ9xHmIpAFV_aTo83d6Y_CqTyYnBBouBEvDNmD2IH9-KKG2onA3Kxd5FFtggLD2ePwrOrU9UWP7QNoY1SY83bmkiueUsMMpoI3iWjKU_6sRHRcjv06_QKVPJJdubVdTCRgfRFvAJsHFE4wAtiPtJMjOxgXl9kyK_9F_yHA2Cu63Vz31O7gdW9yktSNU1-S580AtwODzNzjM_xP_4I5xEma3r_rZqfAb7qekal7vN0dJi7TLWr8G7xkumn1L2fAh0VZQEx60e8zZafsFozpzyfaenoE5DWu7kxFUglYnksldYxUQ2h2tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ftFLqmq2ZBIkr6JFRnCAHOPefb_LeKHPMwz9V9VolBKuryDxK2d2wZA6JU1VOxf0uEnG9zMcCNthI2OjWfMZZ-yH2Le7P2wmA0jvtZW5MN0Nzzl1XYT_sN2pgXXOKX5IlvesIZ-kakRwAL4Daz_mYnEUHmOatk3iMhwbRGdF5dnqmhyC508D1ooGDJuczCPX7aLyK-gZ5wpLqoS9t7TnAtNh-jfjMnMAWGuPXQPo5Ii4VPr0PWMJsbMNo-2kmJGvUhev8oAjkwKXqPbD5bI6ivKOt7xc8V8iPVEzRYZa7DcY42cwTUmHIPRwqyjDpxtdoH8FVgHIUFEB08u3a1Wcvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t_xtyohgexta8VRx-u1pdEPJWiuK61akj__MtrPIGs0QdZCuQtZJDERJ-dSTgRKi3WW2raCb-JryOFLCGh69X-HO1OCmrORBxmdloI-dzjL7GWdHhOg3Vp50KT5GhDwdGCWZ7jtfURGE5zFg9MM0eP0D9sJXQQZklG8MSeQP2M6Z3Xb_BI9u1IZSGVSxZ6HOz5MdCdLplKOnS4KZobh17VZqtiaXqUu_MqoHHSdU0af00xePrr0vSU6zk8inTUALGlBGGstEZys95-2wDFm057q3b3SC3HUSFqzPpOPtShJny4QEkj1RdMojjJ8iScbyBXXYWD-4wl30Dde9IyeqIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: اجازۀ سوءاستفاده از شرایط جنگی و فشار بر معیشت مردم را نخواهیم داد
🔹
رئیس‌جمهور در نشست بررسی الگوی مشارکت اصناف در تنظیم بازار: یکی از سیاست‌های اساسی دولت در شرایط فعلی «کنترل مصرف و جلوگیری از شکل‌گیری تقاضای القایی و کاذب» است.
🔹
ایجاد تقاضای غیرواقعی بدون تأمین متناسب کالا، منجر به نارضایتی عمومی خواهد شد.
🔹
دولت بنا ندارد برای فعالیت اقتصادی سالم محدودیت ایجاد کند. اجازه نخواهیم داد عده‌ای با سوءاستفاده از شرایط جنگی، معیشت مردم را هدف قرار دهند.
@Farsna</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/435060" target="_blank">📅 11:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435059">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae34f29f31.mp4?token=qY9S-1eDhRIP6OiJ9dun5K9qOL7iiUbRbbqGLRVrq37JfCQ5CTDgLgVrzcUG7GTv9pZz_zSCuuPQPkzXZoRwAUfeJglkGWcdkuRqQ9BVoJWjiQAM2P_HmiRIw2IuLmKGqK9jqj_9rmc3dJvpOs_AgBEomCrtGVTjlCLrVVFKfuLnYD7BP7OfwTVB1Bvaj9qmyHoOVHKkvZF81XcFIhpfpoWHozGPMpo8d_7R2kRZeKEKfFrNT7HTDwGGRS7cYuBMpGAc9TL80TQYuzfWGF7mmRXVyBvokc4x-lOdkDdzVplHZ0yQAjeTwnuJyRKsIl_3ruVIxNFLvnuN4bJXQRKpLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae34f29f31.mp4?token=qY9S-1eDhRIP6OiJ9dun5K9qOL7iiUbRbbqGLRVrq37JfCQ5CTDgLgVrzcUG7GTv9pZz_zSCuuPQPkzXZoRwAUfeJglkGWcdkuRqQ9BVoJWjiQAM2P_HmiRIw2IuLmKGqK9jqj_9rmc3dJvpOs_AgBEomCrtGVTjlCLrVVFKfuLnYD7BP7OfwTVB1Bvaj9qmyHoOVHKkvZF81XcFIhpfpoWHozGPMpo8d_7R2kRZeKEKfFrNT7HTDwGGRS7cYuBMpGAc9TL80TQYuzfWGF7mmRXVyBvokc4x-lOdkDdzVplHZ0yQAjeTwnuJyRKsIl_3ruVIxNFLvnuN4bJXQRKpLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران مهمان این روزهای آذربایجان‌شرقی است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/farsna/435059" target="_blank">📅 11:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435058">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8f588c713.mp4?token=OFl2XOiqSKO_9sPyTXAG8wtro67m3nKQEPTiI6qCuxSWrDC1VsNk_p8yTIEApZOsI6MCexB5VJFdTvF8OqzpqMfMoZhcl7xoN5BpO29aknkiG0fKJy4ruJMUhchgryPeBxJmRpT3d6vmcj_5kWAJ5G9A7C95thcgGRWYjTLmxRIwUO34E_zCABeyxwYvtquBcrAOBVvETUKNggM5QHOo5oPfOSJu7O43wQkHMqdyFR2ZumC5ymmMQensdbXCE4tn_w6gQePGK1fWg7f8cZEJZbmw4oNhxxnO_fneT82yC5lO2gowC1yrS8T7um7jDLrWlqGllgiCBw-99bBCPKwACw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8f588c713.mp4?token=OFl2XOiqSKO_9sPyTXAG8wtro67m3nKQEPTiI6qCuxSWrDC1VsNk_p8yTIEApZOsI6MCexB5VJFdTvF8OqzpqMfMoZhcl7xoN5BpO29aknkiG0fKJy4ruJMUhchgryPeBxJmRpT3d6vmcj_5kWAJ5G9A7C95thcgGRWYjTLmxRIwUO34E_zCABeyxwYvtquBcrAOBVvETUKNggM5QHOo5oPfOSJu7O43wQkHMqdyFR2ZumC5ymmMQensdbXCE4tn_w6gQePGK1fWg7f8cZEJZbmw4oNhxxnO_fneT82yC5lO2gowC1yrS8T7um7jDLrWlqGllgiCBw-99bBCPKwACw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای در جلسه با وزیر ارتباطات: مسئله‌ٔ اینترنت پرو و سفید مثل پتک در ذهن مردم شده و باید با موارد خلاف قانون در این موضوع برخورد شود.
🔹
در این جلسه دادستان کل کشور و وزیر ارتباطات به رئیس قوه‌قضائیه گفتند: با بررسی‌های صورت‌گرفته، احراز تخلف در قضیهٔ موسوم…</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/435058" target="_blank">📅 11:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435057">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3750246ce.mp4?token=ZtMnplD2p0aMGNA3_19sV3JY7n5q32bKF4Su7BBAAbgF3BfALVOtXDZYGz0vGT9cbd5ULN34OoJ-ktm94wAHx-9JCaD8kzwPnLwnG5HXrkJMoVoCpmA2qYAZlZ8tGjBWX5qv-yAe6AdEIqKwi_18IKNqDkIrk6ux69QOeCT1uAU21PvCTkoEbLNM0JBJK4SYQvoCSYvcLmdfbDD3TqJYT2o2E77m5OCSWCUnVGrdHmshWabg5UZMHcsVq1wBvhuITorL1FVoQug0gBzOleV7F_VDF0DqSIhQUHo1zoH8Wyv57ot4FFjZoFsf9TjXp1IerXAPPoDcxHEY4meKGFodXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3750246ce.mp4?token=ZtMnplD2p0aMGNA3_19sV3JY7n5q32bKF4Su7BBAAbgF3BfALVOtXDZYGz0vGT9cbd5ULN34OoJ-ktm94wAHx-9JCaD8kzwPnLwnG5HXrkJMoVoCpmA2qYAZlZ8tGjBWX5qv-yAe6AdEIqKwi_18IKNqDkIrk6ux69QOeCT1uAU21PvCTkoEbLNM0JBJK4SYQvoCSYvcLmdfbDD3TqJYT2o2E77m5OCSWCUnVGrdHmshWabg5UZMHcsVq1wBvhuITorL1FVoQug0gBzOleV7F_VDF0DqSIhQUHo1zoH8Wyv57ot4FFjZoFsf9TjXp1IerXAPPoDcxHEY4meKGFodXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: در جنگ تحمیلی سوم ما ۵۰ نفر شهید ۱ تا ۵ سال داشتیم
.
@Farsna</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/435057" target="_blank">📅 11:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435056">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b106a12408.mp4?token=cahSYKxRnnWdG9uu_qwAbJxcJmpRk1mg1v5FZGFPdwCcVItXKZlqmRVUcPzcw6dkIAbqEjdqrhQIOwAroEeAYA_xXYWO3hbk0mPTirZuSeX-l87a7NAJ8zADKbJyLaVbbaN7tJoAGlMvzvKjjo1cKAUcipN2n3f_WUBX5jXqxswuTcZ-Yvaofe4kp-FxpTqqBolPHyv14VFFm4TE2PbT6H7Ai1ruMKholW7cN3R0LQepOr6e2lUsuuf51Y8bmBVfxIRiwNdh76Mz--aw74W6cYdMdIU5oVw6jrGGa1XbrogQirGtSjy-9mJIDOaIEV98wfb3qrEoU_a-gcMae2VTPa_YTZ6r-32kQQoGj1Zx_TQzHPenJ-r9X5vQG_xBGzm_zXmmBguQ6mZZYqSXr2EpsIhA6qbmg4UwKauqDKmPDckeRaM1vIl2fiHQlm0fiJzCq5eZwrVA9oFrtv5lZeemaZVqKsUgu96vqy7IoCLHv91oI-zwnPngTt96IQakfUJg9vp9-65suXWT8E00wjGPstDgLnNbvXLwaKXYhm9NTmw1UB-FU1NYjJ099GeEhWBOwjPLLKoOorjZ3gpyTFO8ZPv3xZHmRGzl0W6F1iaZsRVH3MZLb1vg9uzKOEr1bo0_iLC-u1FGrNC8IzZrqsKBYeS6H9bpBPnfNLrBI17I4yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b106a12408.mp4?token=cahSYKxRnnWdG9uu_qwAbJxcJmpRk1mg1v5FZGFPdwCcVItXKZlqmRVUcPzcw6dkIAbqEjdqrhQIOwAroEeAYA_xXYWO3hbk0mPTirZuSeX-l87a7NAJ8zADKbJyLaVbbaN7tJoAGlMvzvKjjo1cKAUcipN2n3f_WUBX5jXqxswuTcZ-Yvaofe4kp-FxpTqqBolPHyv14VFFm4TE2PbT6H7Ai1ruMKholW7cN3R0LQepOr6e2lUsuuf51Y8bmBVfxIRiwNdh76Mz--aw74W6cYdMdIU5oVw6jrGGa1XbrogQirGtSjy-9mJIDOaIEV98wfb3qrEoU_a-gcMae2VTPa_YTZ6r-32kQQoGj1Zx_TQzHPenJ-r9X5vQG_xBGzm_zXmmBguQ6mZZYqSXr2EpsIhA6qbmg4UwKauqDKmPDckeRaM1vIl2fiHQlm0fiJzCq5eZwrVA9oFrtv5lZeemaZVqKsUgu96vqy7IoCLHv91oI-zwnPngTt96IQakfUJg9vp9-65suXWT8E00wjGPstDgLnNbvXLwaKXYhm9NTmw1UB-FU1NYjJ099GeEhWBOwjPLLKoOorjZ3gpyTFO8ZPv3xZHmRGzl0W6F1iaZsRVH3MZLb1vg9uzKOEr1bo0_iLC-u1FGrNC8IzZrqsKBYeS6H9bpBPnfNLrBI17I4yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دوربین مخفی|
استخدام وزیر شعار برای تنگۀ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/435056" target="_blank">📅 10:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435055">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47b3f0d347.mp4?token=ZDMvAAHGN1oxFeBsOur7WSs_4cB7LVQy7g3ncbpkyB2TuJURm0vT55DCu6wQSOGz5otE7kzD2fwVjDD0j8cx6LwTO3Wg0CkCJY7eYZ2sH0RiHUJ6MFAjspkvIArpO9Pk_r4T0Q787FSG7eGBBqAD8-nHaI4OSL5Hnq4KwIOvrNvbwrO1k7hFlEikOLX8D1J9L9uTiEBSokfwH3AcHt8XJLHhrbiwY3qIxsFLR2XuobWLvDRnwmyD4LAfaQiQa8z526Dy4BwgsALijhrPN8C2s8HcT-AzSfv0JJrL1G-g_crLez5HiubJh1B79UGYrdRsysJc9ZTyiyUsgCBpU_v-Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47b3f0d347.mp4?token=ZDMvAAHGN1oxFeBsOur7WSs_4cB7LVQy7g3ncbpkyB2TuJURm0vT55DCu6wQSOGz5otE7kzD2fwVjDD0j8cx6LwTO3Wg0CkCJY7eYZ2sH0RiHUJ6MFAjspkvIArpO9Pk_r4T0Q787FSG7eGBBqAD8-nHaI4OSL5Hnq4KwIOvrNvbwrO1k7hFlEikOLX8D1J9L9uTiEBSokfwH3AcHt8XJLHhrbiwY3qIxsFLR2XuobWLvDRnwmyD4LAfaQiQa8z526Dy4BwgsALijhrPN8C2s8HcT-AzSfv0JJrL1G-g_crLez5HiubJh1B79UGYrdRsysJc9ZTyiyUsgCBpU_v-Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستور رئیس قوه قضائیه برای پیگیری اختصاص سیمکارت‌های سفید یا اینترنت پرو به برخی افراد
🔹
حجت‌الاسلام‌والمسلمین محسنی اژه‌ای: وفق گزارشات واصله، در قضیه موسوم به اینترنت خط‌های سفید و اینترنت‌پرو، اتفاقاتی حادث شده که ضروری است دادستانی کل و سازمان بازرسی…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/435055" target="_blank">📅 10:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435054">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iO-j1gB7NTt9bCmsGrhSOIeiQ2_DtvasCt_s8RIGrGh7vC_YD7wEPGdZ3-HV6Q-0uo9AxRMDilD0BcgNer_2bXl0zlXHubLH0-HnQj5IkpJ1XGpPWactxPuE6YZxMahbnCiZWblrbCnnb6Bq_PvI-L3msHW-P8qn8FzSuwSKA4hd-eYZYiimHAC4Nw2lCL-sx5VA66K00ZUV3NS0pXzEkQez73Ekqo6nX_NlGgi2t1t8qa_oLtlwZe6nIxBQpYMZLlHJLsiwmUTz7_wApptTMOgdX2B-YY3YYrUZFuVswmGsRyeQ7BCxeNR6bBWtHf2I6NVoKxi4xL-6FY7tHrYR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فشار ترامپ برای محاکمه خبرنگاران «خائن» در جنگ ایران
🔹
در حالی که زیر سوال بردن ادعاهای دونالد ترامپ درباره جنگ با ایران توسط رسانه‌های آمریکایی ادامه دارد، وال استریت ژورنال از فشارهای او برای محاکمه خبرنگاران خبر داد.
🔹
طبق گزارش از این روزنامه، شکایت‌ها و گلایه‌های ترامپ در مورد افشاگری‌های رسانه‌ها درباره جنگ با ایران، «تحقیقات تهاجمی وزارت دادگستری» علیه خبرنگاران را برانگیخته است.
🔹
به روایت وال استریت ژورنال، «رئیس‌جمهور ترامپ ماه گذشته به طور خصوصی از تاد بلانش دادستان کل موقت، در مورد افشاگری‌های رسانه‌ای در پی جنگ ایران شکایت کرد.»
🔹
یکی دیگر از مقامات دولت ترامپ خبر داد، رئیس‌جمهور در یک جلسه مجموعه‌ای از گزارش‌ها و مقالات خبری را که او و دیگر مقامات ارشد فکر می‌کردند امنیت ملی را تهدید می‌کند، به بلانش داد که روی آن نوشته شده بود «خیانت».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/435054" target="_blank">📅 10:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435053">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
معاون نیروی دریایی سپاه: محدودهٔ تنگهٔ هرمز برای ما بزرگ‌تر شده است
🔹
در گذشته، تنگهٔ هرمز به‌عنوان یک محدودهٔ محدود در اطراف جزایری مانند هرمز و هنگام تعریف می‌شد، اما اکنون در چارچوب طرح جدید، محدودهٔ تنگه هرمز به‌طور قابل توجهی گسترش یافته و از سواحل…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/435053" target="_blank">📅 10:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435052">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obr88e9wypWfaHEx5_IfFE6sWhTVfDOoXobBxQCOpDgbNvKoLZqcoonVLtBCAmgMC5JeBCPPomqdEqsDLj-b-FPCB0KL9I774bMD_e3J4nkmAROcNoOVqZSC_BwyifSKMiCD1ujZWxyzVWmq9qAegbgwiiQGJ0cZ6HFTFvJi_X4G3JMvFfIxP--A5myuFZaYIjdIWTETiBBrz1Zqs1Df4wiJYlyiJTXQ5C8ESjcWuYxKKM8vcmkG0-OgUIe2OrVYeX_dtL9zbTxvTMyBIn3t9updoUMaajoDT-v5zWgiHbueuX0PiCnRAVA88q5DiRq2jYUoFyPcq9ED6skmYkwowQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خادمی پردیس احمدیه در حرم امام رضا(ع)
🔹
بازیگر سینما تصویری از انجام امر خادمی خود در حرم امام رضا(ع) را منتشر کرد و در صفحۀ شخصی خود تصاویری از حضور در حرم رضوی به اشتراک گذاشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/435052" target="_blank">📅 10:42 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435051">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8hVy2-tzUh40_aiOyYD70QPwXDOAjJsZ6SYh2Zc4Ja6VPH31xSRMnwIrkRpYTj2YCw-mM1AgutD8SlNFXFyn5PX1vlzFefnYcNvZI76C1CNeyyi9KHRQQsousafw0TOnw7scoCmA3T6n8sEpzxpem0rAAVtQyvv9XITgY5JJwWzlfMSNweCQXa8XBK4kbXpsudwWw67LQ7xfSj03k_D4HIOQ0DUdWinSdANb6btPVYKU4GE0Z2p1RCMWUbiRex32dGx6CmBh41foXHNzQWLhYbPvX1Jv5IvDpCI_XAO_HT_WmG-MOk87peQNq6HvG3jCltNpUhlIjXchtKjHFFB1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان گزارش شبکهٔ آمریکایی دربارهٔ حضور هواپیمای ایرانی در اسلام‌آباد را رد کرد
🔹
وزارت خارجهٔ پاکستان گزارش سی‌بی‌اس نیوز دربارهٔ «استقرار هواپیماهای نظامی ایران در پایگاه هوایی نورخان» را گمراه‌کننده و جنجالی خواند و هدف از آن را تضعیف تلاش‌های جاری برای ثبات و صلح منطقه‌ای توصیف کرد.
🔹
این وزارتخانه اعلام کرد که «هواپیماهای ایران و آمریکا در طول دورهٔ آتش‌بس و مذاکرات اولیهٔ اسلام‌آباد برای انتقال پرسنل دیپلماتیک، تیم‌های امنیتی و کارکنان اداری وارد شدند و ارتباطی با هیچ وضعیت اضطراری‌ای ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/435051" target="_blank">📅 10:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435050">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMuNDn7Tpj2qO_Sh9pEivDdcSZaCN12ITs4u_fp4HXQBr_JAyA5L3HjcsQWKavsPUMtzyq0FkTaG2P3BdxLRr8uWkns9qZrfco63yjj4vRm8DxVGcWL463AFx9mmXM4dQWqvMCHGeTM4BQ8V2cWaKwM1jGf_-7RNdqAQ9r0Ng_nwHfgbyiKrnxyjF_uMXMeDCkJyIpSPNQ2dlAKLIjyVUL_AHUyy0H2vRoazaDyJssFg-ivXdXTswh5TQLoeS6U88IJaMamB225iMoLBv5NxTAyct6wChgoxIswHOh-QS_L5CImsAQl5gVIWBAHMY3bOwpyeU83s6QH_ZpVOnGwagg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شادی بن گویر کنار کیکی که بوی مرگ می‌دهد!
🔹
تصویری که به تازگی در شبکه‌های اجتماعی منتشر شده، چهره وحشیانه کابینه رژیم صهیونیستی را بیش از پیش نمایان کرده است.
🔹
در این تصویر، کیک تولد ایتامار بن گویر، وزیر امنیت داخلی رژیم صهیونیستی، با یک طناب دار تزئین…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/435050" target="_blank">📅 10:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435049">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
زخمی‌شدن ۸ نظامی صهیونیست در درگیری با حزب‌الله
🔹
رادیو ارتش اسرائیل خبر داد که در ۳ درگیری بین نظامیان اشغالگر با نیروهای حزب‌الله در اطراف روستای «زوطر» ۸ نظامی زخمی شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/435049" target="_blank">📅 10:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435048">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
معاون نیروی دریایی سپاه: محدودهٔ تنگهٔ هرمز برای ما بزرگ‌تر شده است
🔹
در گذشته، تنگهٔ هرمز به‌عنوان یک محدودهٔ محدود در اطراف جزایری مانند هرمز و هنگام تعریف می‌شد، اما اکنون در چارچوب طرح جدید، محدودهٔ تنگه هرمز به‌طور قابل توجهی گسترش یافته و از سواحل جاسک و سیری تا فراتر از جزایر بزرگ، به‌عنوان یک پهنه راهبردی تعریف شده است.
🔹
به‌عبارت دیگر، تنگه هرمز بزرگ‌تر شده و به یک منطقه وسیع عملیاتی تبدیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/435048" target="_blank">📅 10:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435046">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52478a45c6.mp4?token=JCfUUtbIpF3qg_6O-t3g9EDqRVb5MlEuQp2oWqultowCQjCPBYTWFAqr3eTdsyWBODEY-r2KOei6vYhZIp9rAuxuFA99X3uqyk5L7NMU313DdVwScNeoYhQ6LZbGxEFs20sXcRLE51IptHq5Czh8ZQ9fT_hDAOjyy0ZQAnX15B53RJJneN3Wufi2jk03HQyhs1yd2Lf-3aTQZBxmmK4Yu22F-BIQOrZLiCjJsMJodvya-6z8IJSDoyD0dKszlFxebAJRxU-fPK4BJH7O-kxVZg-5MImkUR5L1v4GPibJKXWjbBqaTeMkrf7m8Nwh7eFWYvyghfN6wPACA1bKJlcZZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52478a45c6.mp4?token=JCfUUtbIpF3qg_6O-t3g9EDqRVb5MlEuQp2oWqultowCQjCPBYTWFAqr3eTdsyWBODEY-r2KOei6vYhZIp9rAuxuFA99X3uqyk5L7NMU313DdVwScNeoYhQ6LZbGxEFs20sXcRLE51IptHq5Czh8ZQ9fT_hDAOjyy0ZQAnX15B53RJJneN3Wufi2jk03HQyhs1yd2Lf-3aTQZBxmmK4Yu22F-BIQOrZLiCjJsMJodvya-6z8IJSDoyD0dKszlFxebAJRxU-fPK4BJH7O-kxVZg-5MImkUR5L1v4GPibJKXWjbBqaTeMkrf7m8Nwh7eFWYvyghfN6wPACA1bKJlcZZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار نارنجی؛ به حریم و بستر رودخانه‌ها نزدیک نشوید
!
@Farsna</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/435046" target="_blank">📅 09:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435044">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تروریست آموزش‌دیدۀ گروهک تروریستی انصارالفرقان اعدام شد
🔹
رئیس دادگستری سیستان‌وبلوچستان: بامداد امروز حکم اعدام عبدالجلیل شه‌بخش فرزند جلال، عنصر آموزش‌دیدۀ گروهک تروریستی انصارالفرقان اجرا شد.
🔹
در پی بازداشت عبدالجلیل شه‌بخش در جریان اقدامات ضدتروریستی در شرق کشور، پرونده‌ای علیه وی تشکیل و دادسرا او را با عناوین اتهامی بغی از طریق حمله مسلحانه به مقر‌های انتظامی و عضویت در گروه باغی انصارالفرقان به دادگاه انقلاب معرفی کرد.
🔹
نظر به بررسی دقیق پرونده در مراحل دادسرا و دادگاه و وجود مدارک و مستندات متقن استخراج شده از وسایل ارتباطی و فایل‌های صوتی متهم و همچنین اقاریر صریح وی در مراحل مختلف بازجویی و بازپرسی؛ سرانجام با ابرام حکم وی در دیوان عالی کشور، حکم اعدام این عنصر تروریست بامداد امروز اجرا شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/435044" target="_blank">📅 08:43 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
