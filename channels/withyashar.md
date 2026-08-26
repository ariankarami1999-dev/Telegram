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
<img src="https://cdn4.telesco.pe/file/tTriAKSrPmNA7B1e5ak9ZzJj3KQNKNjp6pPtDwC_xYCDqp7WQ5aCppj6oMpSwlpOK2iIgFpG_1r-dzkyOlyyhsTn-W5-Z80Kr1I8G0eXtC05sxXfPn5Ifg6jTGbtQ4FbR7jZC3ePaNnHxWUeTyeOLxvJXqoGMLX0NHxx2snEquGlGcfIHLRc7URpg2NDrAA8mRwdKEz9K2nXHrfbQoFC7Ij-L9LCJALmWYW1zH9eCJOZu6i-ioqOV0gaD4dcE3AgvsX3nnyJDluLP2tN2pjD1LVahu-6pXEwBuTQWDX0tifQ0ywK0V26MXJJuDN4fFNyNi8PEXp0ukR5r1S2h-vH3g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 441K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 21:39:48</div>
<hr>

<div class="tg-post" id="msg-21555">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دیدبان اتاق جنگ با تاخیر : درود من چند وقت بود میخواستم یه چیزی رو بگم ولی شک داشتم بگم یا نه  من ……….. این قسمت پیام  حاوی مشخصات دقیق فرستنده پیام بود و سانسور شد ……  برج مراقبت مهراباد یه تعدادی ادم بودن خیلی مذهبی و عرزشی بودن جوری که انگشت نما بودن  اینا…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/withyashar/21555" target="_blank">📅 21:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21554">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دیدبان اتاق جنگ با تاخیر : درود من چند وقت بود میخواستم یه چیزی رو بگم ولی شک داشتم بگم یا نه
من ……….. این قسمت پیام  حاوی مشخصات دقیق فرستنده پیام بود و سانسور شد ……
برج مراقبت مهراباد یه تعدادی ادم بودن خیلی مذهبی و عرزشی بودن جوری که انگشت نما بودن
اینا چون رادار نداشتن تو جنگ میومدن با بقیه ی برجای غرب کشور با عرزشیاشون هماهنگ میکردن که جنگنده اومد خبر بدن
میگفت ما ۹ اسفند یه ربع زودتر خبر دادیم که جنگنده و موشک دیدیم اگه میخواستن رهبرو پیاده و با پای خودش ببرن بیرون از بیت یا ببرن پناهگاه تو یه ربع میتونستن ولی اینکارو نکردن و گذاشتن بمیره حتی مدرک و اثباتم داشت که زنگ زده بود پدافتد و حفاظت بیت  میگفت حتی از زمان جنگ ۱۲ روزه رابطمونم خیلی خوب بوده با بیت چون خبر میدادیم بهمون اطمینان داشتن
و خب این یعنی ممکنه باقر قالیباف رهبرو با لابی و کودتا قربانی کرده باشه؟
@WarRoom</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/withyashar/21554" target="_blank">📅 21:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21553">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کانال 13: رئیس ستاد ارتش در دو روز گذشته توصیه کرده است که تعداد عملیات ترور هدفمند در غزه افزایش یابد، به عنوان پاسخی به "پرتاب هواپیماهای کاغذی"
@WarRoom</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/withyashar/21553" target="_blank">📅 20:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21552">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خبرگزاری تروریستی فارس : یک نفتکش هند هنگام عبور از تنگه هرمز توقیف شد
@WarRoom</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/withyashar/21552" target="_blank">📅 20:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21551">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4Z3DM1Uqras1jUW0Fe_Rep0v4QBfcKFxbWwZRzgLdE6kwVYRZILsDB58rhMvh_CY52eOt-G8Rgos0l22OmPhuqvNMLbN_SkHJhkzCllYv7mZu1TxrpexETIYJJPj4Jvf-1-kDO3OvXRYKM0pOBx-nszj1mSZU-qi1owSX7P1XbzypViHEouArkX4QXkTSU6Z1mxQDOP8bBaZMIh5YFppctrhHS63kYrSO7LUQ7hdaIxGUra586DkaPoXq0gyhZ2qd8TKbtJSQXf6wOKdTwctnDauOhIuQxLpYaK_4hYm5k8-QvyfejlbDxM4vnLUpqEMO9CFOXguljlUcF5JxS2xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در سال ۱۹۶۴، در دوران تحصیل در آکادمی نظامی نیویورک، در کنار پدرش «فرد ترامپ» و مادرش «مری آن ترامپ». ترامپ در سال آخر تحصیل به درجه «کاپیتان دانش‌آموزی» و شمشیر افتخاری دریافت کرد و همچنین فرماندهی گروهان A را بر عهده داشت. این تصویر مربوط به دوران فارغ‌التحصیلی او از آکادمی نظامی نیویورک است؛ یونیفرم او لباس تشریفاتی یک دانش‌آموز نظامی است، نه یونیفرم ارتش آمریکا.
@WarRoom</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/withyashar/21551" target="_blank">📅 20:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21550">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSW6OzL3UJntssmEvoL4rGBjmi2bffHpLrLCguZX8V0Se1G9lduY35fYIWVOe6SJuanbfnPZv6HVXgFqLGMR1_yS0l-v3v9ti24iDmf_-S9t10OgNnCarplVkDoZhFG5e3gChQr37FgyTy1B_-u__Wfz-Ls7_2FG-PjFRzPQrCivZ5ql8ae74m7Q5PhJ0tjKvwuxD8_4QrNZGy7LsCnvBlwUVTGGY9OjgYaLFI77sK5SJiHIwTyOIEUHH8SxtiLIu27dJfJ2QNvQfMypKC3JSdgHy0lVp-lrnPY37y1xyForK-IbEcEA5i1r_woKRvQ7_R1yyBvSXHnmuErWbPlW1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث مدعی است امسال کار رو جمع میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/withyashar/21550" target="_blank">📅 20:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21549">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJk0tzSqaEH1C62mkl3EJ2kSdDlun4t2ulxc2DI9dJkS1h8DYGXUxr0cY-o7_Hgdfq3h8zTTqB0txv0n5C1khz4vuVkuy0d-khhyVvt5Jleboj05e42hp40hkztUogq3hAXUwuLqOFtlaNtTixFTZ3CsnWm9cm3oyygMXhgF41CrXjoyMioNkFt0Ek8oHiPLsBDoERvaHFv-RWvhxoREwQaXmjxRzsTPUfZqzTxc3u9eAd7FWJR9A15VebTkt2XCwfRAFjblL4L1Mb40jpXYgr4oe4-2gtF4uL7iGAnla99UbMRwKdL6Mta0ODM8dlu__3ZsrQ6CZdZkHnek7a8lbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث پست عکسی از خودش و پدر مادرش را بازنشر داد که در کپشن آن نوشته شده : والدینی که دنیا را نجات دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/21549" target="_blank">📅 19:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21548">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کانال ۱۴ به نقل از آتلانتیک
:
منابع داخلی ایران به این نشریه گفته‌اند که
مجتبی خامنه‌ای، جانشین تعیین‌شده پدرش، یا از نظر بالینی مرده است یا در وضعیت نباتی به سر می‌برد
؛ موضوعی که پرسش‌های جدی درباره اینکه در حال حاضر چه کسی عملاً ایران را اداره می‌کند، ایجاد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/withyashar/21548" target="_blank">📅 19:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21547">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ در گفت‌وگو با الجزیره
گفت او گفت برای ازسرگیری مذاکرات با ایران «عجله‌ای ندارد» و برای انجام مذاکرات نیز «هیچ جدول زمانی مشخصی» تعیین نکرده است
همچنین گفت «ایران با مردم خودش بسیار بدرفتاری می‌کند. آنها تعداد بسیار زیادی از معترضان را می‌کشند.»
من شنیده‌ام تورم آنها ۹۰ درصد است، ولی من فکر می‌کنم تورم آنها در حقیقت ۳۰۰ درصد است.
@WarRoom</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/21547" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21546">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2699b93394.mp4?token=m1GOagt92h0NLQlr6kfhCOq0QjQPTkPDZol-ScZ0kTZvEW6ek_oEXeS4Djh6l7ZAIf9BGsWOtn1cf-H6_5cFY_sbuqMcUECvpymkHO4pI-e-abZ6UtyuyGwAgOp166c23ET19MrwrQIegRov6rDDasbrN51UBw6gZm6DLgh2nerXLxRoBvknrME5b1pz7httVulr92cfQar3ZTTh1fhWvHKBD02Ucm1tTHDuptwHUBoM14EOWOZvsIcogP-CUu06U9ZuLb-w61ZbMTFq1kQA1F69YlwWTprLeFYy2s5Q3_oIxNSFfAoznM5gy2x4BU6x-kUhmG76EEQ8OYZtq71sPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2699b93394.mp4?token=m1GOagt92h0NLQlr6kfhCOq0QjQPTkPDZol-ScZ0kTZvEW6ek_oEXeS4Djh6l7ZAIf9BGsWOtn1cf-H6_5cFY_sbuqMcUECvpymkHO4pI-e-abZ6UtyuyGwAgOp166c23ET19MrwrQIegRov6rDDasbrN51UBw6gZm6DLgh2nerXLxRoBvknrME5b1pz7httVulr92cfQar3ZTTh1fhWvHKBD02Ucm1tTHDuptwHUBoM14EOWOZvsIcogP-CUu06U9ZuLb-w61ZbMTFq1kQA1F69YlwWTprLeFYy2s5Q3_oIxNSFfAoznM5gy2x4BU6x-kUhmG76EEQ8OYZtq71sPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران: وقتی افرادی هستند که حاضرند شما را بکشند، اعتراض کردن در ایران بسیار دشوار است. به همین دلیل است که آنها اعتراض نمی‌کنند.
اما اکنون این احتمال وجود دارد(اعتراضات)زیرا آنها (رژیم)بسیار ضعیف شده‌اند... بسیاری از سربازان آنها حقوق دریافت نمی‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/21546" target="_blank">📅 17:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21545">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAbraham</strong></div>
<div class="tg-text">یاشار جان درود و ارادت
نمیدونم این پیام رو میبینی یا گم میشه لابه‌لای پیام های دوستان
فقط میخواستم بگم دمت گرم که توی این شرایط سخت و پیچیده که این بیشرفها برای ماها درست کردن تو پیشمون بودی و همیشه توی شرایط بحرانی بیشترین انرژی رو برامون میفرستی خدایش دیروز نشسته بودم توی پارک محلمون و به همه چی فکر میکردم ولی هیچ وقت به خ کشی اصلا فکر نکردم چون ماها حقمون این نیست که بخوایم بخاطر یه مشت چاغال بیشرف که بویی از انسانیت نبردن زندگی خودمون تموم کنیم
به هرحال همه ماها یه روزی می‌میریم ولی حداقل با شرافت بمیریم ن بخاطر این پیشرفا
پاینده باد ایران و ایرانی
❤️</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/21545" target="_blank">📅 17:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21544">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBehzad</strong></div>
<div class="tg-text">سلام یاشار جان عرض ادب
من تو کرونا پدر و مادرم رو تو یه تایم ۱۷ روزه از دست دادم و الان تنها ترینم
حرفات کاملا درسته ولی نمیدونم اگر شما ، مثل من ۳ ماه فقط سیب زمینی و نون لواش میخوردی بازم میتونستی اینجوری حرف بزنی یا نه.
برادر اوضاع خراب تر از چیزیه که میشنوی
منم دارم بین خود….. و ادامه دادن میجنگم</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/21544" target="_blank">📅 17:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21543">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">به گزارش خبرگزاری کم اعتبار مهر، ایران و روسیه قراردادی ۲۵ میلیارد دلاری برای ساخت نیروگاه‌های هسته‌ای جدید امضا کرده‌اند. انتظار می‌رود مسعود پزشکیان، رئیس جمهور ایران، و ولادیمیر پوتین، رئیس جمهور روسیه، هفته آینده در قرقیزستان دیدار کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/21543" target="_blank">📅 17:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21542">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/492b9e7ef3.mp4?token=AGNMi2jROMgjx5ZDCcNjRbTezc-D_4-tUpKg9qviBxJOuSOBb2FWVG_tqwdmm4LQ5AoZgwY8BIdS3KBrRoVMRiEX6lJCxyEkKOvPgYEBnSeV_FaD5-p2NQYZoN82wsM-2aNIozIz0eD6q3QZEZdOeBXfPX4BaOpQRe_FgfcnTs8lTaz918wGHe_PB2KfQ10J-PQRR1_8HWEeQQufI5vISUr5b03lY72VW8VxvrqSL866O6KD8itipnKSxHbhGp0AudR5do6C7JbWpMxvuMgI5ttx17DARfVi1K8LC2Cp4SobGQ1wbXQ9s_JWmI_PLnfs94EZDGJbZZUrSQut8z0yIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/492b9e7ef3.mp4?token=AGNMi2jROMgjx5ZDCcNjRbTezc-D_4-tUpKg9qviBxJOuSOBb2FWVG_tqwdmm4LQ5AoZgwY8BIdS3KBrRoVMRiEX6lJCxyEkKOvPgYEBnSeV_FaD5-p2NQYZoN82wsM-2aNIozIz0eD6q3QZEZdOeBXfPX4BaOpQRe_FgfcnTs8lTaz918wGHe_PB2KfQ10J-PQRR1_8HWEeQQufI5vISUr5b03lY72VW8VxvrqSL866O6KD8itipnKSxHbhGp0AudR5do6C7JbWpMxvuMgI5ttx17DARfVi1K8LC2Cp4SobGQ1wbXQ9s_JWmI_PLnfs94EZDGJbZZUrSQut8z0yIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره تنگه هرمز:
«ما مین‌ها را پاکسازی کردیم. اما تنگه [هرمز] باز است؛ تنگه در حال فعالیت است و کشتی‌ها از آن عبور می‌کنند.
بله، هر از گاهی ممکن است یک پهپاد یا یک موشک یا چیزی شبیه آن شلیک شود، اما تنگه کاملاً در حال فعالیت است.
حجم زیادی نفت در حال عبور است.
دیروز ۱۰ میلیون بشکه [نفت عبور کرد].»
@WarRoom</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/21542" target="_blank">📅 17:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21541">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ درباره ایران:
این گروه حاکمان ، آن‌طور که باید، گروه چندان شرافتمندی نیستند؛ این را به شما می‌گویم.
ما خیلی زود در ایران به یک پیروزی بزرگ دست پیدا خواهیم کرد.
ما واقعاً، حقیقتاً، از همان ابتدا ایران را کاملاً تحت سلطه خودمان داشته‌ایم.
من قطعاً با اجرای قوانین شریعت مخالفت خواهم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/21541" target="_blank">📅 17:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21540">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f639ee98c9.mp4?token=nKq4AkerKuPcNtgYVrHlUaSN49Y7LdyUVene5_CKiKC8nCI2JY9smtHvKmaoU5FpUXSzoPz3OhBXBj3vRuRWJHBD8cu1nsZlZKC02Ka6LEOHFoCDmwtRxR9rKhFXaBCMMR-4iwklaQkN4x9iRLECEIFD94u2qGHLbabqKtZBbHnQF19qlHBN-O1ULbgiZpy1BYv_TponRbMXi5dXlhwq4bJZgB-eNrZytHr0MF5IKmY9SSH4d3afgSePz9qiL_tuuVna42JvxocqKGjKhYnOZMTyclTFJMnMbOzk01OJA7JmKPHr2xk23kRJukrKjy5NppAkYqY7ZnjzaIv0yzr8rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f639ee98c9.mp4?token=nKq4AkerKuPcNtgYVrHlUaSN49Y7LdyUVene5_CKiKC8nCI2JY9smtHvKmaoU5FpUXSzoPz3OhBXBj3vRuRWJHBD8cu1nsZlZKC02Ka6LEOHFoCDmwtRxR9rKhFXaBCMMR-4iwklaQkN4x9iRLECEIFD94u2qGHLbabqKtZBbHnQF19qlHBN-O1ULbgiZpy1BYv_TponRbMXi5dXlhwq4bJZgB-eNrZytHr0MF5IKmY9SSH4d3afgSePz9qiL_tuuVna42JvxocqKGjKhYnOZMTyclTFJMnMbOzk01OJA7JmKPHr2xk23kRJukrKjy5NppAkYqY7ZnjzaIv0yzr8rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:فکر نمی‌کنم مجتبی خامنه‌ای مرده باشد.
او به شدت زخمی شده بود، سمت چپ بدنش، بازو، پا، کل بدنش به شدت زخمی شده بود.
اما فکر نمی‌کنم مرده باشد
اگر مرده باشد، آنها نمایش خیلی خوبی اجرا می‌کنند، زیرا مدام در مورد بازگشت و صحبت با او برای گرفتن آخرین دعایش صحبت می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/21540" target="_blank">📅 17:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21539">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">@WarRoom
Apple</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/withyashar/21539" target="_blank">📅 16:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21538">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نتانیاهو:
من به ترامپ گفتم ایران رو تشدید محاصره کن
!
@WarRoom</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/withyashar/21538" target="_blank">📅 16:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21537">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58ac4e3799.mp4?token=AKSy0_OqB3tVAY5CX_nPaU-EhdsvEVFnUvNJUww3uiC6mf9BRg25cW4jv1l9PV_W1YHNT9rWY782WvsgG2yTDyCr8VX_zJXWj3ti6OrYhp2Rvbt7x-L9dv1gee9ANN59OOCr61qgLtUX05b_GcOlH2qVPw5VzBbbLlFhIV957oifybwmh2X0ouuz25lXdX3MR5_9q99zSjsGDAOlIYKaSqbSei30seQjbfcfkkbLUrhy9jqb3_DON-RXd3Xu-d0eScyJfnzukXksv5IhYvhzW7_B9-UDTZipHWAO1mhmFXhD7hXP_mpRGvdlJ5HzVsS1nqK11r5-Bmy5SDwAvt5HMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58ac4e3799.mp4?token=AKSy0_OqB3tVAY5CX_nPaU-EhdsvEVFnUvNJUww3uiC6mf9BRg25cW4jv1l9PV_W1YHNT9rWY782WvsgG2yTDyCr8VX_zJXWj3ti6OrYhp2Rvbt7x-L9dv1gee9ANN59OOCr61qgLtUX05b_GcOlH2qVPw5VzBbbLlFhIV957oifybwmh2X0ouuz25lXdX3MR5_9q99zSjsGDAOlIYKaSqbSei30seQjbfcfkkbLUrhy9jqb3_DON-RXd3Xu-d0eScyJfnzukXksv5IhYvhzW7_B9-UDTZipHWAO1mhmFXhD7hXP_mpRGvdlJ5HzVsS1nqK11r5-Bmy5SDwAvt5HMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکنون فردی در بالای پل طبیعت میخواد خودشو … آتشنشانی در حال مقابله و کمک است
@WarRoom</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/21537" target="_blank">📅 16:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21536">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/21536" target="_blank">📅 16:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21535">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شرکت راک‌استار گیمز سکوت خود را در مورد لو رفتن گیم‌پلی GTA 6 شکست و آنها را «دلخراش» خواند و عذرخواهی کرد که «بدیهی است که این آن چیزی نیست که ما می‌خواستیم شما از بازی ببینید.»
آنها تأیید کردند که بازی «تقریباً آماده است» و فردا یک نمای کلی از آن نمایش داده خواهد شد.
تاریخ انتشار تایید شد: ۲۸ آبان
@WarRoom</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/21535" target="_blank">📅 15:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21534">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خبرنگار الجزیره در تهران: بر اساس گزارشات آمریکا با ۱۶ کشور هم‌مرز ایران برای قطع روابط اقتصادی با ایران تماس گرفته!
۸ کشور درخواست آمریکا را دشوار دانستند و ۸ کشور دیگر پاسخ دادند که در حال بررسی این احتمال هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/21534" target="_blank">📅 15:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21533">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ریزش قیمت خودرو در بازار
@WarRoom</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/21533" target="_blank">📅 14:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21532">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هادی لومپان امسال نمیتونه ویزای آمریکا رو بگیره و در مسابقات آرنولد کلاسیک شرکت کنه ، او با قرار دادن یک استوری گفت : جشن بگیرید هادی چوپان از ایران امسال نیست اما پایانش هم نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/21532" target="_blank">📅 13:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21531">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فاطمه مهاجرانی ، سخنگوی دولت : مردم منتظر بهتر شدن وضع اقتصاد در شش ماه یا یک سال آینده نباشند. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/21531" target="_blank">📅 13:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21530">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فرمول جهانی حاشیه برای معرفی کالای‌جدید
@WarRoom</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/21530" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21529">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fd86e564c.mp4?token=f9lFQwnTJIyekS4y0BphrQfmV4bmGqzYEgr01FuPDUP3uvu6ZGN9Qran9bVDLqRLsxUMEmzQ4YktFj_TWh5XAPZHt5Ug4S0l3l2JZ8XYDBc3ENHJVo-8y2yGWsH_TJH7ZheHQoyTgqtmmRMbscUOy5kuP-mlS0oPg_sOvIlq7-SRnias78qRa4rpVUG_-w9V3q0-_XE7mrxfbsVy7IjUFe9hcaOCQgMULisfgjmrhxuAeLM1j7wPUUMJLaYsZu1OmXZuh2xTQBWzSUwpl_Yx-_nS_0IiC49l_j161DYp85FJiUv6FsIGCaRTQnWajsc9JXl0I0BR47kac6dUroJWcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fd86e564c.mp4?token=f9lFQwnTJIyekS4y0BphrQfmV4bmGqzYEgr01FuPDUP3uvu6ZGN9Qran9bVDLqRLsxUMEmzQ4YktFj_TWh5XAPZHt5Ug4S0l3l2JZ8XYDBc3ENHJVo-8y2yGWsH_TJH7ZheHQoyTgqtmmRMbscUOy5kuP-mlS0oPg_sOvIlq7-SRnias78qRa4rpVUG_-w9V3q0-_XE7mrxfbsVy7IjUFe9hcaOCQgMULisfgjmrhxuAeLM1j7wPUUMJLaYsZu1OmXZuh2xTQBWzSUwpl_Yx-_nS_0IiC49l_j161DYp85FJiUv6FsIGCaRTQnWajsc9JXl0I0BR47kac6dUroJWcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/21529" target="_blank">📅 12:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21528">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69fffd91f0.mp4?token=NLbSOH_NfP9t0S5I1at55RiIrT4F2LKbFXH0t8J9Ppag3u_f5h7U3l5WqMyPNdwjv2prxmxgCi2se2d6tKK5rx5e3-A6AaL72_qlQEY1BOWOGB5cW4fljtjCo8BXXo5dWxoWWU06b01GhU4opu4KOoTlXTvwCXhk_Ptb_3_Rdnfjy9f2glL_KNHlhzZMtC4wXAC-RdvNoLtl3-9N9PXBC1agw-kpWAv4Oxe_sw3wl1urEoHqrVG41B6EBi96PQa9kX8ZWQ4SAH2hqaQXvILO3wNv6bqgPZT_2N2xgsKLAP9R92VgT2ZgsD60E9QeZhJo6gUAu0qWlB-aJ_ZXqS6P3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69fffd91f0.mp4?token=NLbSOH_NfP9t0S5I1at55RiIrT4F2LKbFXH0t8J9Ppag3u_f5h7U3l5WqMyPNdwjv2prxmxgCi2se2d6tKK5rx5e3-A6AaL72_qlQEY1BOWOGB5cW4fljtjCo8BXXo5dWxoWWU06b01GhU4opu4KOoTlXTvwCXhk_Ptb_3_Rdnfjy9f2glL_KNHlhzZMtC4wXAC-RdvNoLtl3-9N9PXBC1agw-kpWAv4Oxe_sw3wl1urEoHqrVG41B6EBi96PQa9kX8ZWQ4SAH2hqaQXvILO3wNv6bqgPZT_2N2xgsKLAP9R92VgT2ZgsD60E9QeZhJo6gUAu0qWlB-aJ_ZXqS6P3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران:
می‌خواهم به شما بگویم: ما هنوز چالش‌هایی پیش روی خود داریم.
چالش ایران تمام نشده است.
ما همچنین باید چالش غزه، لبنان و سایر عرصه‌ها را به پایان برسانیم و مصمم به انجام این کار هستیم.
@WarRoom</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/21528" target="_blank">📅 12:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21527">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296e867e7b.mp4?token=UtLwOKa1qAdnqDeDm0gyPQmzH8pRdJktCyvQA-i0TyLik8n6LupC75uao07vcdj6PvfdtES-hg8zlrjxVE7xyYFKGC1twGkQ7hEv0qCVVK5VENFMEAd1y9CPd5NQp793KJ1vBt6OfaqHUSZBXOWkkBhUt7acYuTwMywjsgTxgNFfU1IMeqoF_NwhJdrIUhu-HWoyneLHnztrU0bNKDULihrZgnvuuvgrxcjwhGcWWJ5OWnG7LuYhB_oNqYIIdztuqTGi0985Lebien3lEMV7NjbPtOilBZZCx9F9BrpwuGYbbjpS3ow_8GVGTS26o2SrYLbnaoxLYOs8gBBYcnP87A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296e867e7b.mp4?token=UtLwOKa1qAdnqDeDm0gyPQmzH8pRdJktCyvQA-i0TyLik8n6LupC75uao07vcdj6PvfdtES-hg8zlrjxVE7xyYFKGC1twGkQ7hEv0qCVVK5VENFMEAd1y9CPd5NQp793KJ1vBt6OfaqHUSZBXOWkkBhUt7acYuTwMywjsgTxgNFfU1IMeqoF_NwhJdrIUhu-HWoyneLHnztrU0bNKDULihrZgnvuuvgrxcjwhGcWWJ5OWnG7LuYhB_oNqYIIdztuqTGi0985Lebien3lEMV7NjbPtOilBZZCx9F9BrpwuGYbbjpS3ow_8GVGTS26o2SrYLbnaoxLYOs8gBBYcnP87A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو : دستیابی به توافق با ایران ممکن نیست‌‌ @WarRoom
🚨</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/21527" target="_blank">📅 12:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21526">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بنیامین نتانیاهو : دستیابی به توافق با ایران ممکن نیست‌‌
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/21526" target="_blank">📅 12:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21525">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نرخ دلار ۱۹۹،۰۰۰ تومان
دلار کف بازار  ۲۰۰-۲۰۵ هزار تومان
تتر۱۹۷،۵۰۰ تومان
بیتکوین ۷۹،۰۰۴ $
انس جهانی طلا ۴،۶۲۸ $
نفت برنت ۸۵،۵۴$
@WarRoom
۱۲ ظهر تهران</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/21525" target="_blank">📅 12:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21524">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bcf3-EX7NMNlG6N-qMMrhdR-rJkzdayaYg9BBPgi1UeZtDtdD6iL5gp-RqHi9gYaXWdL6eW7tL65cjhI6laqGYFZeOoRilMD9V8Va_SeD_ZF6Q50F8e7rVyRf9PAbtue55-Bfivu9BApzKKJJ6_mtrnUiZuGgAqY3SSlmC79sMdBIRIcwUqbJuP3FTNc3mhl6zcmCjHsY0g0dkb-EJv6gaYGKC2yZHzOuTS7gaYzqlhKbMQyd8Vtbuy21FF0KacjqkJPRcjt1BBBwMyTD-KNrn6fDizVbSMMeWKJScvEq6T6BiluNzL8z_c1-fl-jghHfYGaAG0V48XgItPmxiRJcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط با یک دیپلم ساده، می‌توانستی
رایگان خلبان شوی، مدرک معتبر بین‌المللی بگیری، برای آموزش و کار به خارج از کشور بروی، تمام هزینه‌های زندگی‌ات را دریافت کنی و حتی ماهانه حقوق و کمک‌هزینه بگیری
؛ آن هم در شغلی که در سراسر دنیا مایه افتخار و احترام بود. امکاناتی برای ساختن آینده یک جوان ایرانی که امروز باورکردنش برای خیلی‌ها سخت است…
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21524" target="_blank">📅 11:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21523">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تانکرترکرز : امروز دریای عمان حسابی شلوغ بوده و حداقل 15 عملیات انتقال نفت از یک کشتی به کشتی دیگه در حال انجام بوده.
در مجموع حدود 25 میلیون بشکه نفت خام به‌علاوه مقداری فرآورده نفتی در حال جابه‌جایی بوده.
ایران در بین صادرکننده‌های نفت خام این لیست دیده نشده؛ نشونه‌ای از این‌که کشورهای منطقه دارن با انتقال کشتی‌به‌کشتی، مسیر صادراتشون رو تو شرایط فعلی حفظ می‌کنن.
@WarRoom</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/21523" target="_blank">📅 10:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21522">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نیوزمکس: یائیر نتانیاهو هدف طرح ترور رژیم جمهوری اسلامی در آمریکا بود. بر اساس این گزارش، در ماه دسامبر نگرانی‌هایی جدی به وجود آمد که مأموران رژیم جمهوری اسلامی وارد میامی شده و یائیر نتانیاهو را تحت نظر گرفته‌اند. شدت تهدید به اندازه‌ای بود که به او حتی اجازه بازگشت به آپارتمانش برای برداشتن وسایل شخصی داده نشد و تحت تدابیر امنیتی از آمریکا به اسرائیل منتقل شد؛ جایی که بنا بر این گزارش تاکنون در آن اقامت دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/21522" target="_blank">📅 10:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21521">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کارولین لویت به نقل از
بسنت: رهبران ایران در برابر فشار اقتصادی ترامپ «دچار وحشت شده‌اند» او وعده داد «تمام راه‌های حیاتی اقتصادی» ایران را قطع کند.
﻿
@WarRoom</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/21521" target="_blank">📅 10:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21520">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آکسیوس
:
انتظار می‌رود سیاست افزایش فشار اقتصادی علیه ایران تا بعد از انتخابات میان‌دوره‌ای در آبان ادامه یابد
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21520" target="_blank">📅 09:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21519">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">معاون اول پزشکیان : هنوز مسائل مهمی در حال مذاکره هستند ولی ما در صداقت و تعهد طرف مقابل به وعده‌هایش تردید داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21519" target="_blank">📅 09:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21518">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دارلین گراهام در دور دوم انتخابات سنای جمهوری‌خواهان کارولینای جنوبی پیروز شد و با حمایت قوی رئیس‌جمهور ترامپ، نماینده رالف نورمن را با ۵۲٪ در مقابل ۴۸٪ شکست داد.
گراهام که پس از مرگ برادرش لیندسی گراهام به این سمت منصوب شده است، اکنون در ماه نوامبر با آنی اندروز، دموکرات، روبرو است و به شدت شانس پیروزی دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21518" target="_blank">📅 09:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21517">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">منبع مطلع به آکسیوس : استیو ویتکاف و جرد کوشنر، قرار است
روز چهارشنبه
برای دریافت گزارش درباره وضعیت میدانی، به منطقه فرماندهی مرکزی آمریکا ، سنتکام بروند
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21517" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21516">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هم اکنون حملات ارتش اسرائیل به علی طاهر، المنصوری، تزربین و الکنترا در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21516" target="_blank">📅 00:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21515">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کاخ سفید در واکنش به گزارش‌هایی از پاکستان مبنی بر پیشنهاد آمریکا برای پایان دادن به محاصره دریایی ایران در ازای بازگشایی تنگه هرمز و مهار نیروهای نیابتی تهران در منطقه،
انجام هرگونه مذاکره یا تماسی با ایران را رد و تاکید کرد که محاصره دریایی اعمال‌شده علیه ایران «با تمام قدرت و اثربخشی» ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21515" target="_blank">📅 00:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21514">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کاظم دستکج، معاون عراقچی :
چرا باید همیشه منتظر حمله آمریکا باشیم؟
ما می‌توانیم اقدامات پیشگیرانه انجام دهیم.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21514" target="_blank">📅 23:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21513">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کاظم دستکج غریب‌آبادی: شناورهای مین‌روب آمریکا اگر وارد منطقه شوند اهداف بسیار خوبی برای ما هستند
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21513" target="_blank">📅 23:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21512">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است. ایران اکنون دو راه دارد: انزوای کامل جهانی و اقتصادی در حد تأمین نیازهای…</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21512" target="_blank">📅 23:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21511">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_ItDqFOK5SI8MP1U_UDRAMKvnJSy37O1JAqN34oJdBLnk-V7_Ajsz6-tVIo-815T4mHFevKzEkDd9r8a3tcxZ8BB6nN0JtKIUcEPqRrZUqLL5Mz9NartBQAIBjo2TVgvoGHcmQjciLQXSqAWBO7JpUZKiTO_X4qhRUMOMj9a6Z3_B7e5hR7VzVn5tS1YUKzPqH2LZMp9zKXwdFHZ7w0pZlIl8WBW2qWelIq-mKkl4oRM8NP4jAkl6iTcI1TCdYlEsY0qRraqe0QKlYGj4BCQlXJgLNdoswzFgSk9CklYavPhO4c74y3KFR7EztOOs0MfKCHVQxugHFF_CKPhKIQ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه ایالات متحده آمریکا، اداره امنیت دیپلماتیک، برنامه «پاداش برای عدالت»: تا ۱۰ میلیون دلار پاداش برای اطلاعات درباره رهبران کلیدی سپاه پاسداران انقلاب اسلامی ایران. این افراد فرماندهی و هدایت بخش‌های مختلف سپاه پاسداران را بر عهده دارند؛ نهادی…</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21511" target="_blank">📅 23:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21510">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">معاون وزیر امور خارجه جمهوری اسلامی : مسیر عبوری که با عمان در تنگه هرمز توافق شده حدود 7 مایل طول دارد، ولی موقت است و ما در مورد یک مسیر دائمی با آنها مذاکره خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21510" target="_blank">📅 23:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21509">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ریچل ریوز، وزیر خزانه‌داری و وزیر دارایی بریتانیا:
ما از تلاش‌های آمریکا برای افزایش فشار اقتصادی بر ایران حمایت می‌کنیم و به همکاری با آمریکا و دیگر شرکا برای اعمال فشار اقتصادی بر ایران ادامه خواهیم داد.»
خود وزارت خزانه‌داری بریتانیا هم رسماً گفته
بیش از ۲۴۰ تحریم علیه ایران اعمال کرده و قصد دارد برای افزایش فشار اقتصادی، همکاری با آمریکا را ادامه دهد
.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21509" target="_blank">📅 23:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21508">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اکسیوس: زیردریایی‌های بدون سرنشین نیروی دریایی آمریکا، به مدت چند ماه تنگه هرمز را جستجو کردند و بیش از 100 شیء را شناسایی کردند که به عنوان مین دریایی مشکوک بودند.
بر اساس گزارش‌ها، ایالات متحده همچنین از شرکت‌های خصوصی در این عملیات برای شناسایی و خنثی‌سازی مین‌ها کمک گرفت. رئیس‌جمهور ترامپ امروز اعلام کرد که مین‌های موجود در مسیر اصلی کشتیرانی در این تنگه، برداشته یا منفجر شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21508" target="_blank">📅 22:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21507">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4cRN45EioUAQE_rZp2Gmox0wjSEZX16uOga59obP9HMVcZxNJPOYFp4Ee9ZI8G9-memXb5K0s-DlAumr_UUeY4ZmqLaWaCX27rI9jTSAsZguAMkUoYmtr2TZ6DrkCdLfB0723sxJPC44Bjo12jdWGtxa-vk7zM7U4Yp7qCwY4dPlceHqeqyuDwcn4K2Accc3toQuXV0Md7DLDb4x8S6DVKkbFWrzQCq5YtRAAz2bnKUF-2BjLJeXY07mHo5BiSl02x5Ef6nwhgBvUTHJa1xxuBmsTVj1L_Rnxq84UUwfA8TBMlkklunIcEJiw9BVprkAc6wBeNxyOgZ9G_AH0jJOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوه اردوغان , حالا اسمشو چی گذاشته باشن خوبه؟ گذاشتن «گوزیده»
«گوزیده بایراکتار» (Güzide Bayraktar)
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21507" target="_blank">📅 21:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21506">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">زلنسکی: به موشک‌های پاتریوت دست یافتیم اما به تعداد بیشتری نیاز داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21506" target="_blank">📅 21:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21505">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پاکستان امروز رسماً از وزارت خزانه‌داری آمریکا درخواست یک سازوکار ۱۰ میلیارد دلاری برای تثبیت ارزش پول ملی کرده است؛ بزرگ‌ترین درخواست از این نوع در تاریخ پاکستان. این درخواست پس از افزایش نقش پاکستان در میانجی‌گری میان آمریکا و ایران مطرح شده؛ نقشی که روابط اسلام‌آباد با دولت ترامپ را تقویت کرده است. پاکستان در حال حاضر حدود ۱۲.۳ میلیارد دلار بدهی دوجانبه کوتاه‌مدت دارد که برای بازپرداخت آن به تمدید مداوم بدهی‌ها از سوی عربستان سعودی، چین و کویت نیاز دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21505" target="_blank">📅 20:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21504">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lgs0Pj-vT6XO0iCVm61sd8lRLL68H2qN_A_g_zT2EOHqUJRo_lOZZZYYndhKdHcTqJb050CTzR3j381ifqaP_GA5kRSKJPUszhTSYC_9qE25UzmnXWDkkLyzdmaGT-md4sJWRkp39vWxx69AlTUOvdOQgUMvUfd5V-fpKxQb-LADqUtrgOzVvnDD2eQvL4dxTZLJouZ3zMnxFvWe8JKrTqy0Zo85p6Y7RE0s-W4OAPN9GEzOdwn9K8N6gRbMUzt9WTFPmiVlw8bds1wLodjQ7780VyxqaSG_kypU_epzOtn3Dq7UOpESNIbNFUX7-WUq3G5xJx9LtVjlVR3r39oZMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : نفت داره میاد پایین ، ترامپ داره هی‌کارای مختلف میکنه که نفت رو بیاره پایین و جمهوری اسلامی هی موشک ول میده که بره بالا !!! فعلا تو این لوپ گیر کردیم…
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21504" target="_blank">📅 20:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21503">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تنگه دعوا شده ، صدای انفجار ‌از ‌تنگه شنیده شد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21503" target="_blank">📅 20:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21502">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWyJjDrbnN7NszenUMt8Zqcflt1cnshUHRXaKSgWYX9-7P_ua6tUCh3GvqpEANNTEVIlMIXMKXrLDKo5uCrErWQQPqZxJa6QxlNe-39Yfolbxi3leVIz7Tcb4rRah9BbJzZY59lqaImIjZozzih9D6qGFkwVepngR-c3z5PjKOIJ5AmHDYN8P9wtIMdXpxN4_yE3fXiaFtIwCrCErq0RMlWHbggILZBoJcLXbpt9rK82zPdHRTImZ7OE8_-47yOvi5iv1ogej3IvIhcKqeZIOw65epQbIx9ozMaCbdBW75J_rLsfVGswwqNimEn0Wiw3e3lWvp3BvqYoURODRVATCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاطمه مهاجرانی ، سخنگوی دولت : مردم منتظر بهتر شدن وضع اقتصاد در شش ماه یا یک سال آینده نباشند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21502" target="_blank">📅 20:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21501">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بدر البوسعیدی وزیر امور خارجه سلطنت عمان دقایقی پیش وارد تهران شد
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21501" target="_blank">📅 20:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21500">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اردوغان:
اجازه نخواهیم داد سناریوهای خونینی که برخی برای منطقه ما آماده می‌کنند، اجرا شود و از حمایت خود از همسایگانمان دست نخواهیم کشید.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21500" target="_blank">📅 20:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21499">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ : آمریکا جهان را تحت فشار قرار می‌دهد تا ضربه اقتصادی نهایی را به ایران ورشکسته وارد کند. آمریکا در حال فشار آوردن به تمام کشورهایی است که هنوز با ایران تجارت می‌کنند تا روابط خود را به طور کامل قطع کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21499" target="_blank">📅 19:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21498">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">صفحه امروز نیویورک پست : آمریکا جهان را تحت فشار می‌گذارد تا آخرین ضربه اقتصادی را به ایران ورشکسته وارد کند و ملاها را کنار بزند. @WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21498" target="_blank">📅 19:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21497">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نیوز مکس : ترامپ در دور دوم انتخابات جمهوری‌خواهان، رأی‌دهندگان کارولینای جنوبی را به نفع دارلین گراهام بسیج کرد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21497" target="_blank">📅 19:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21496">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بیانیه ایران و عمان : ایران و عمان در حال بررسی یک طرح مرحله‌ای برای
بازگشایی و تأمین امنیت کشتیرانی در تنگه هرمز
هستند که از یک کریدور موقت و مین‌روبی آغاز می‌شود و می‌تواند به ایجاد یک سازوکار دائمی برای عبور و مدیریت تنگه منجر شود
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21496" target="_blank">📅 19:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21495">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نتانیاهو: اگر به ایزنکوت گوش می‌دادیم، حسن نصرالله الان زنده بود.
غادی ایزنکوت یک ژنرال بازنشسته و سیاستمدار اسرائیلی است. او همچنین مدتی عضو کابینه جنگ اسرائیل در دولت نتانیاهو بود و اکنون رهبر حزب «یاشار» است و جدی ترین رقیب بنیامین نتانیاهو در انتخابات پیش‌رو محسوب می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21495" target="_blank">📅 18:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21494">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlejandro Sosa</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTjcjF20HNt7pBkUKtLjnnbx7wFjKWGqg88gF00QjaSTqlAERXxnkXv8YmDrGyINCwVDwi_0bGv_rMKt262-MqTKgzQKKzNoiBWJrx0MeqbBwkhj85tfLSVKV20zPitElPF8JaUVT2o5j4nu_9cDYg2_mwOHgfOWkama1WjBrzn9BsBdmexxLQjAzDJWEjz5MlKPPH6XQ6oZD27RyhdyMsrM7LP0To7fS2Bipk_zNmqtZpNrG3M2bmDvWGpIPLvXIwUWi-YAaDNMD74X7x5D-DrHOknmsCGR55UeycWUQVpPWOp6X1_FGaVZH-O89uqaTeiEW9urUNekjrgAMHQxNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21494" target="_blank">📅 18:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21492">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANQEPab6eCtapN56jIhMI1v-5ehudPxGPIZbcuKV60E9CCIeu9pxZN9YEfTCtH1DjN-LEvBwO93GVSy8E22B_RKY6pJakG1s-DDMGk4w67BXDm7HwVcGmwe4qe88ROkkJwNyH7vY9U4m4Zl_xSejCWXPT7ISD7dPbM2kwhKbLQg2gNa4mb32uO5X-X3Xm2P2-7onpVN6BmplSARjy9bHUMsD0yVhs_2w83YVwaBPiA7f-33yNfiMV4zKcFeU6ipGJqAqLpbtpAypY4sM06-PmIlHZZbjOzYu77NSwS_BLOhDu-w609M46VhQlL8CFsbxGBPHwmbA2U1ChEIidpfVqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌ تروث: نیروی دریایی آمریکا به من اطلاع داده که تمام مین‌های موجود در آب‌های بین‌المللی تنگه هرمز جمع‌آوری یا منفجر شده‌اند. به ایران هشدار داده‌ایم که هر کشتی یا قایقی که اقدام به مین‌گذاری جدید کند، بلافاصله و به‌طور سیستماتیک منهدم خواهد شد. آمریکا با استفاده از نیروی فضایی، تمام نقاط تنگه هرمز را زیر نظر دارد و سیاست «مدارای صفر» در قبال مین‌گذاری به‌طور کامل اجرا خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21492" target="_blank">📅 18:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21491">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مقام کاخ سفید: محاصره دریایی به طور قاطع و مؤثر در حال اجرا است، تنگه هرمز باز است و تمام مین‌های کار گذاشته شده برداشته شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/21491" target="_blank">📅 17:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21490">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F21N_d9ifEfNFlWv6RzyJ5jFBdcg1cPfU3a9LXmyDUg4rSAL9BBZdfNTsMGqi8v4ek0vvXbmuEcAXBY7DTapkHPkvwj3T6VZTAIZoZr4N_8e0tOig24DL67EM3qUzi0w1eD1SIUnmAajuawHoGtmwj3A45nGcsgEmRqLwrzAfOFiNiiaidi1n6O-ITevzJpaRTdkZxDegebAwGscJNosbpK_P3V8tKFrN6xi_Y0TQW5xHxrh9SX3MKruxyssjLWiW-Ia0vFViFcw5isg1t75QxgYGK6DIcLcpOk63IMllkG_0ZbUlz_C4ZS0CK_Es67QqMjC-T6WCZw9Q4qPTpdhYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : بر اساس رابطه بسیار خوبم با کیم جونگ اون، رهبر کره شمالی، از این واقعیت خشنود نبودم که ایالات متحده مدت‌ها پیش با شرکت در رزمایش‌های مشترک نظامی با کره جنوبی موافقت کرده بود. این رزمایش‌ها نه‌تنها پرهزینه هستند و بخش بزرگی از هزینه‌های آن، طبق معمول، توسط ایالات متحده آمریکا پرداخت می‌شود، بلکه پیامی کاملاً نامناسب و خصمانه به کشوری ارسال می‌کنند که از زمانی که دونالد جی. ترامپ رئیس‌جمهور بوده است، تهدیدی ایجاد نکرده و محترمانه رفتار کرده است. بنابراین، با توجه به اینکه برای لغو این رزمایش‌ها دیگر خیلی دیر شده بود، به پیت هگست، وزیر جنگ، دستور دادم که رزمایش‌های مشترک نظامی را به میزان قابل‌توجهی کاهش دهد! در موضوعی که تا حدودی بی‌ارتباط است (؟)، اخیراً از رئیس‌جمهور کره جنوبی پرسیدم که آیا مایل هستند در روند خلع سلاح هسته‌ای جمهوری اسلامی ایران به ما بپیوندند و آنها گفتند: «نه، متشکریم!» از توجه شما به این موضوع سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21490" target="_blank">📅 17:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21489">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">صداوسیما در اقدامی ، اطلاعات به ادعای آنها محرمانه و مکان‌های دقیق تردد پسر ترامپ و نقاطی که در تیررس است را منتشر کرد. @WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21489" target="_blank">📅 16:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21488">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ناو آبراهام لینکلن پس از ۲۵۰ روز و جنگ با ایران برای استراحت در تایلند پهلو می‌گیرد یکی از مقام‌های تایلندی امروز اعلام کرد ناو هواپیمابر آمریکایی لینکلن قرار است هفته آینده در این کشور آسیایی پهلو بگیرد. @WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21488" target="_blank">📅 16:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21487">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxOjgnjLUd0RyS5AEngcRz_BLRKQAx9TpanVUVuYRkWQu-9QB_-GXyZHG7KzMKEYeEdcruzCHMpwYyM4JpqUbOKgVKUcIeHjtIUv16LhJuWNdPrR19ILgm8P_iYME0Z-pCIJYhEXJAhLRydfZMD-utQBLh-Y3D_FEzIVylfthilYoWaGEWdnEmCu1h5D84Cqqc42F6yeCHx510uxUX2yk8PuVseXyOZBMFqTTIbdN_cJhTHm3EiHaZnvrFmaQc9Uwdq5p5C4jKPE5_6Ds6IUzqnr4AT0zT8-gt0AR63M4Z7TI4hbtDVHX5Jw1WQRZ3cyTwOkalZjFKK5JXu1d31B6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو آبراهام لینکلن پس از ۲۵۰ روز و جنگ با ایران برای استراحت در تایلند پهلو می‌گیرد
یکی از مقام‌های تایلندی امروز اعلام کرد ناو هواپیمابر آمریکایی لینکلن قرار است هفته آینده در این کشور آسیایی پهلو بگیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21487" target="_blank">📅 16:24 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21486">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qG1GNquazg7sTtWK0p4R7-FVB5TBd96x31CoBPVMWiOZC-Q_QxfTVfEwARaRDdAHVtblkzlBjLqugQ8L1eCIZ15A0EfRfKG1v2pBTGF6l0b2W0N6GnAJSBxWYMhwdZU4WZ47VyaywKX5E2IvlR1slHWKRghOo86Rkp4Niz0oJRYYwfpR_5kNtDbuaOQOo8gRrrv4t9wdgCS37JbNCqgZZqDMjomQvaCoDnYxKEepnkQgdGtppDLFiqFLr-iajN1mAdi2Ezv8sih-YH684mzyLoxdC1SwCt3UmizQoq_J9YOFj8KH4sIwMOIRvxXKK_RZNYUU-eB7XnxyfSrv0m1SWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : موتور جستجو و پرینت مخفی پست های
ترامپ
ناتالی هارپ، ۳۵ ساله، یکی از نزدیک‌ترین دستیاران دونالد ترامپ است. او در کالیفرنیا و در خانواده‌ای مسیحی و محافظه‌کار بزرگ شد و پس از تحصیل در دانشگاه، در جوانی به سرطان استخوان مبتلا شد. در سال ۲۰۱۹ در یک برنامه تلویزیونی حاضر شد و با تعریف داستان بیماری‌اش، مدعی شد قانون «حق تلاش برای درمان» که ترامپ در سال ۲۰۱۸ امضا کرده بود، امکان دسترسی او به درمانی را فراهم کرده و او را از مرگ نجات داده است. این حضور تلویزیونی توجه ترامپ را جلب کرد و ترامپ پس از برنامه از او تمجید کرد.
او سپس به کارزار ترامپ پیوست، در همایش جمهوری‌خواهان سخنرانی کرد، مدتی مجری یک شبکه تلویزیونی محافظه‌کار بود و در سال ۲۰۲۲ مستقیماً به تیم ترامپ پیوست. از سال ۲۰۲۵ نیز به عنوان دستیار اجرایی رئیس‌جمهور فعالیت می‌کند. هارپ به دلیل اینکه تقریباً همیشه ترامپ را همراهی می‌کند و با یک چاپگر قابل‌حمل خبرها، نوشته‌ها و تمام مطالب اینترنتی وایرال را بدون واسطه برای او روی کاغذ چاپ می‌کند، به لقب
«چاپگر انسانی»
مشهور شده است. او همچنین در مدیریت شبکه اجتماعی ترامپ نقش بسیار مهمی دارد و خودش پست میزارد و ولی اکثرأ متن‌هایی را که ترامپ برایش دیکته می‌کند، تایپ و منتشر می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21486" target="_blank">📅 15:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21485">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/21485" target="_blank">📅 15:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21484">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21484" target="_blank">📅 15:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21483">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21483" target="_blank">📅 15:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21482">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aO2vQv-6Udl2ac6WcGKABHKxsdsV21xsmyvS6ibMWhToRjYuH9P59tylnbAzXkI8ZCh_zMQEydWhcHRUhEfjL2qhTLbXHDH8tJRkxCZvOPJn-gw6P1GIR5dsf77PDPZ7xRXST4B9zF2duz2Co7AticwnwXIbORO_ZhnfSikH78w8L9Gjago4m7SvRwFYSR8AeCAsESX2SKwVHVKVGu3RVrRBNaJFSvxDiVegEMKXlBfkWwghXfIOedd4_FJuJVPTWXNx7yTQp4WLOXzLZv-5mlL-BMNRcrxPR7N3tFw34k4f83uQgJ-2jLY2VLGrblCrLB2-8JL3kMaISj4fqKObHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : جمهوری اسلامی شکست‌خورده ایران به بخش‌های گسترده‌ای از نیروهای مسلح خود حقوق نمی‌پردازد و هم‌زمان معترضان را می‌کشد حتی زمانی که آنها اصلاً در حال اعتراض نیستند در ابعادی که پیش از این دیده نشده است.این یک بحران انسانی در مقیاسی عظیم است و باید همین حالا متوقف شود.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21482" target="_blank">📅 14:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21481">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UO7KhOZOWXwxuI5pNL6Z8zjnkuOid7tjCndtRxIVQ7FnrC3gGbnHKntURWIXBmXCOcW-uAXjCITvjERocuxFm0_002O99qSm3JBEy4ZsF0mdQ6jjbICBq4cJ-Ycac-I6tyFpep0xhR39tUcWoDZATGXRQsTrxZNUeUZzSegdcdNjcjprmTIxFGhQ5N2g8NK2uD7519z6FViW5FxAigodZ_nWN4aNifY2jlMqDZknMh3w3fomJy9b7YYclu-urwNiDifFRSfmx_aEHobTOmS9FcisuKRKqTN57X8Mg5WcbzcwPfRzYDW0kSKMujs13f-Y1Nb4BHgjq3RjlKwCor68AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه امروز نیویورک پست :
آمریکا جهان را تحت فشار می‌گذارد تا آخرین ضربه اقتصادی را به ایران ورشکسته وارد کند و ملاها را کنار بزند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21481" target="_blank">📅 14:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21480">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه ایران؛ فرماندهان ارشد نظامی تحریم شدند!
آمریکا پنج حوزه
دارایی‌های دیجیتال، فناوری، طلا، هوانوردی و کشتیرانی
را هدف قرار داد و شبکه‌های مرتبط با برنامه‌های موشکی و هسته‌ای، عملیات سایبری و انتقال درآمدهای نفتی ایران را تحریم کرد. در بخش نظامی،
امیر حاتمی، رضا طلایی‌نیک و محمدباقر ذوالقدر
تحریم شدند و تحریم‌های چند فرمانده ارشد دیگر نیز گسترش یافت. همچنین شبکه‌هایی در
ایران، چین، هنگ‌کنگ و مالزی
و چند فرد مرتبط با حملات سایبری و وزارت اطلاعات هدف قرار گرفتند. آمریکا چند شرکت، فرد و نفتکش مرتبط با
ناوگان سایه و انتقال نفت ایران
را نیز تحریم و پنج معافیت تحریمی را تعلیق کرد
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21480" target="_blank">📅 14:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21479">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رژیم ایران اعلام کرد که سفر سرلشکر عاصم منیر، فرمانده ارتش پاکستان، به تهران «بسیار پربار» بوده و به دستاوردهای دیپلماتیک چشمگیری منجر شده است که به زودی «آشکار خواهند شد». محسن نقوی، وزیر کشور پاکستان، نیز گفت که مذاکرات شامل احیای تفاهم‌نامه اسلام‌آباد بوده و «پیشرفت قابل توجهی» در این زمینه حاصل شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21479" target="_blank">📅 14:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21478">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اکسیوس: ۵ نشانه از فروپاشی اقتصاد ایران زیر فشارهای ترامپ
؛
۱.
سقوط ریال:
دلار به حدود ۲.۰۲ میلیون ریال رسیده است. ۲.
تورم شدید:
پیش‌بینی می‌شود تورم ایران در سال ۲۰۲۶ به حدود ۶۸.۹ درصد برسد. ۳.
فشار معیشتی:
گرانی و کاهش ارزش ریال، تأمین نیازهای روزمره را برای مردم دشوارتر کرده است. ۴.
سقوط صادرات نفت:
محاصره آمریکا صادرات نفت ایران را به‌شدت کاهش داده و درآمدهای نفتی را تحت فشار قرار داده است. ۵.
رکود و بیکاری:
افزایش بیکاری و کاهش فعالیت اقتصادی، پیش‌بینی رشد اقتصاد ایران را به انقباض حدود ۵.۴ درصدی در سال ۲۰۲۶ رسانده است. با این حال، اکسیوس می‌گوید هنوز نشانه‌ای از تسلیم تهران دیده نمی‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21478" target="_blank">📅 13:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21477">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دیدبان های اتاق جنگ گزارش های زیادی میدن مبنی بر فعالیت های مختلف‌ و حتی ‌در مواردی عجیب رژیم که همه شما هم حتما شاهد هستید در سطح شهر ها ، که مشخص میکنه بدجور ترسیدن و دارن برای مقابله با شروع اعتراضات ( انقلاب ) آماده میشن
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21477" target="_blank">📅 11:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21476">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏وزارت خارجه چین در واکنش به تحریم‌های آمریکا اعلام کرد تعاملات چین با ایران مطابق قوانین بین‌المللی انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21476" target="_blank">📅 11:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21475">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وال استریت جورنال : چند روز قبل از صدور دستور حمله به ایران، ترامپ هشدارهای صریحی از سوی سازمان‌های اطلاعاتی دریافت کرد که به او هشدار می‌دادند که ترور خامنه‌ای منجر به سرنگونی نظام نخواهد شد، بلکه باعث ظهور رهبری تندروتر و سرسخت‌تر خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21475" target="_blank">📅 11:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21474">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGQRmA-xoSglE69SifBeLBWr1fjRda4aAX17SPl0uHOjZAg1PQEpSaBRjbTXz103inXUhBtpTImy0Vc14t8AkxDlpi2EragsUi3_7r7q4RnMHncIGzlxItKNz-GRCw4gn6Ign_6nlk6BdVMr621T7r3EJx_2CM5TbjGPTFNuV9z22IfSM_zrujnA09XcYkPHOtLjSWNeNUGJbKpwKBKkQAFeDINPNuPP40KsiBFHVZ3IHQwmxvo0XjOvAF4egv70UF-ikOczbI2t3NVx5Nhw493iq1pWOSjQUZnUxh70wzMG-agpzFZ7vPOzqxhTU8IaPVsLsGg5qOcsDPqmlt9XiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون یک F-35 از سمت خلیج فارس به سمت عربستان سعودی سیگنال 7700 روشن کرده ودر حال فرود اضطراری است
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21474" target="_blank">📅 04:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21473">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏شاهزاده رضا پهلوی با بازنشر تصویری از دیدار خود با زلنسکی، سی‌وپنجمین سالگرد استقلال اوکراین را به مردم این کشور تبریک گفت و نوشت: «در این روز مهم، مردم ایران در مبارزه مردم اوکراین علیه تجاوز و اشغال، شانه‌به‌شانه آنها ایستاده‌اند. همبستگی شما با مردم ایران…</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21473" target="_blank">📅 03:28 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21472">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏شاهزاده رضا پهلوی با بازنشر تصویری از دیدار خود با زلنسکی، سی‌وپنجمین سالگرد استقلال اوکراین را به مردم این کشور تبریک گفت و نوشت: «در این روز مهم، مردم ایران در مبارزه مردم اوکراین علیه تجاوز و اشغال، شانه‌به‌شانه آنها ایستاده‌اند. همبستگی شما با مردم ایران در مبارزه آنها برای آزادی هرگز فراموش نخواهد شد. ما همیشه دوستان خود را به یاد خواهیم داشت.»
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21472" target="_blank">📅 03:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21471">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏آسوشیتدپرس گزارش داد که دولت دونالد ترامپ در حال آماده شدن برای لغو روادید تجاری و گردشگری حداکثر ۲۰۰ هزار تبعه خارجی است که برای دریافت پناهندگی در آمریکا درخواست داده‌اند یا در حال حاضر به دنبال دریافت وضعیت پناهندگی هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21471" target="_blank">📅 03:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21470">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کارلوس آ. خیمنز نماینده فلوریدا در مجلس نمایندگان آمریکا : اردوغان همچنان فعالانه از تروریست‌های خشن حماس که خون آمریکایی‌ها بر دستانشان است، حمایت می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21470" target="_blank">📅 03:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21469">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کوینتلگراف : گانون کن ون دایک، سرباز آمریکایی، متهم است با استفاده از اطلاعات سری درباره عملیات برکناری نیکلاس مادورو، بیش از
۴۰۰ هزار دلار
از معاملات پولیمارکت سود کرده است. او اتهامات را رد کرده است.
کمیسیون معاملات آتی کالاهای آمریکا
تلاش دارد در پرونده کیفری او دخالت کند و درباره قانونی بودن قراردادهای پولیمارکت نظر بدهد، اما وکلای ون دایک با این اقدام مخالفت کرده‌اند. رسیدگی به پرونده مدنی CFTC نیز تا پایان پرونده کیفری متوقف شده و دادگاه احتمالا اواخر ۲۰۲۶ یا اوایل ۲۰۲۷ برگزار می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21469" target="_blank">📅 02:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21468">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0nJZvEEhrew4YiY7JYAJfeE1xzk22A6bl4ugtHn1k1NGrgx7kRaWuAlcHz3HezBaubpGl104rYrUV3Ql9tFUZq1EEtmz2yc3EEJG1iF9G9BGErbdTJop8QyFVlBlEXEHR1kb467P0jSra1SRUlxIgMnjhiOoZDBTxRbza1sBRc8ahp7U4I1SiB4pei6zv4nym19dSdd1Xf2tHfFy3kLnL5J2wFBQMeavQlQQVIEwQILGb-RLBTdBWxB48r_qdY6GwX6S5ef03JbZ6Kh5Wd-PvQBB9EHK2ymzwUVAsyim1hpeXSWqkKfNOfPauXRvbuSMbA1qyPt9ah3YGFce-gWgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک پست : ایوانکا ترامپ در سفر خانوادگی به کاستاریکا، مهارت‌های موج‌سواری خود را به نمایش گذاشت.
ایوانکا ترامپ و جرد کوشنر در سال
۲۰۰۹
ازدواج کردند و سه فرزند دارند
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21468" target="_blank">📅 02:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21467">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQKlC35qXPV5tyvfyl1LlthRaTpGm_dVkIfPpHlaEuvCZtUUnBpeEReZdOThyD5FpdzW5f1sjdmQzbfZi4Mw3I42DZSPC7b7NIOmg-C-aPFzorIOVteBlYKjQgxkmalggjwL96hgauMTyv_AcJeHAlH8P1Y1bVFHAtFFIGi2H_FDWdUdJ6K80I9xEbt4gA3N3ss28T5d3B4mfVw7t4_tGRHPQkzTShA9B_xlzGhR66sZ3dj4fS8fa2tn9jv_pJRWsccFQS7_0GcDuh0-yfWgWjQpbTcJ_neCtrkJmKdL4UK-6eO0xG2a7bQnZ4NIyyBfCtsCSY-II-xcGjdKXzKnNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : تفنگداران دریایی ایالات متحده در حال انجام تمرینات سنگین آمادگی بر روی ناو جنگی یواس‌اس باکسر (LHD 4) در حین دریانوردی در دریای مکران هستند
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21467" target="_blank">📅 02:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21466">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی از وقوع یک حادثه در فاصله ۹ مایل دریایی شمال‌شرقی منطقه «الشیشاه» در عمان دریافت کرده است. ناخدای یک نفتکش گزارش داده که کشتی با یک پرتابه ناشناس هدف قرار گرفته و در اثر آن، موتورخانه آسیب دیده و کشتی از حرکت…</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21466" target="_blank">📅 01:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21465">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTjqsw66pmYULH34qtM5_20l3G2rE1AomT_LjGtsn50FKhg4Xriz9p-9KHGdYmeNBPJb00x0thhXrBN0wy5FEtTKRsBQ4btbyWo4p_v40a7gPh5Qshgmsa4_e783glT4mIkBc-VM3DOFfs32mYOZ5h8aKY8yN4w3axKYv8t_oA1FRDZXYDBvhA7n8ZIT5ClZjK4E-ctwZHZhw_Sr_UM3EJD4bGTR4BEGSMg0IxIIPQ9QCkeAJpgDRUAqtWQZOho4fyhOhpE-Zj3muBkl9IhSGKcyBpnzKC7cVwywf_Cyz9dVzbrz7RAVLQgATed0Ij9NU17KiFWqoGfoVoF9LStm4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی از وقوع یک حادثه در فاصله ۹ مایل دریایی شمال‌شرقی منطقه «الشیشاه» در عمان دریافت کرده است. ناخدای یک نفتکش گزارش داده که کشتی با یک پرتابه ناشناس هدف قرار گرفته و در اثر آن، موتورخانه آسیب دیده و کشتی از حرکت بازمانده است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21465" target="_blank">📅 01:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21464">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مارک لوین : ایران سعی کرد یکی از پسران نخست وزیر نتانیاهو را ترور کند. آنها همچنین برای سر بارون جایزه تعیین کرده‌اند…
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21464" target="_blank">📅 01:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21463">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cde83dba14.mp4?token=c0hlqIMUUn5mr5496Vzgc9-haBrrKLMMNwr10qgakWFCHty-_U8xEg5bgry9vbAfBjopy_NjANJHGtRk_oimlVhwU1kyknYFhv9200-KJX_4dVnsoPxKw5Eu42ry_56YsH-SOOxIoBJue_VlITNkxA68Dw0jRw3LPGnmX6JwbDMJWkGnz9XeuoikAs1cYFThWBqqpoK8SMtPjgP4VN-mnEG0qOlKnQXnDa4ajC5UimXu0d3yevB0rx1BpFTGkUyJ9Y9t4Le2g4pAEt73BKRQTB3oGcEb8yyAPS35TXNlYk9vdjueaVHmNWbAeweY45unkwWzA4xTtuEomw662NbNUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cde83dba14.mp4?token=c0hlqIMUUn5mr5496Vzgc9-haBrrKLMMNwr10qgakWFCHty-_U8xEg5bgry9vbAfBjopy_NjANJHGtRk_oimlVhwU1kyknYFhv9200-KJX_4dVnsoPxKw5Eu42ry_56YsH-SOOxIoBJue_VlITNkxA68Dw0jRw3LPGnmX6JwbDMJWkGnz9XeuoikAs1cYFThWBqqpoK8SMtPjgP4VN-mnEG0qOlKnQXnDa4ajC5UimXu0d3yevB0rx1BpFTGkUyJ9Y9t4Le2g4pAEt73BKRQTB3oGcEb8yyAPS35TXNlYk9vdjueaVHmNWbAeweY45unkwWzA4xTtuEomw662NbNUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا می‌توان گفت که در حال حاضر حملات نظامی علیه ایران متوقف شده‌اند؟
پیت هگست: نه. اگر لازم باشد از حملات نظامی استفاده کنیم، این کار را انجام خواهیم داد. اگر ایران آن‌قدر احمق باشد که زیاده‌روی کند یا با ارتش آمریکا درگیر شود، ما هر کاری را که لازم باشد انجام خواهیم داد. فشار اقتصادی در حال حاضر بیشترین آسیب را به آنها می‌زند، اما به هیچ‌وجه استفاده از حملات نظامی را، چه در تنگه هرمز و چه در اطراف ایران، منتفی نکرده‌ایم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21463" target="_blank">📅 01:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21462">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baa3f78fcb.mp4?token=mZDJdM_E1_5msNfuDeKrDvDBnizK1wlOI4Sjdpfw8KtWpqGl8mrLu2Zv062gX5xyxSyfpDiNFvGQIzPOD3R7dYtg2mgK1G7WZYBggHpCTI_IbV9RLPnfsOClkBPBIR_xPHCI68nomfh6ecCBnADSLgSgPsCRJUzM5KCNAeaqEzTzdkK41HdAF6bnlTZr3TPzUOLznKbTNMF2JASdy8dGlCc4ZEVwB9_2YrBtiGrEZPikDZ_-45vVN_nToK9ql2uBaiaGGBfcLbuA9dAIJ5O4ki08GkTFKmD5m8fd8EnJGDzoRWlbUAn6aoJmJybkBCNYiAkAVzDH7xCBQJgXtOuDbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baa3f78fcb.mp4?token=mZDJdM_E1_5msNfuDeKrDvDBnizK1wlOI4Sjdpfw8KtWpqGl8mrLu2Zv062gX5xyxSyfpDiNFvGQIzPOD3R7dYtg2mgK1G7WZYBggHpCTI_IbV9RLPnfsOClkBPBIR_xPHCI68nomfh6ecCBnADSLgSgPsCRJUzM5KCNAeaqEzTzdkK41HdAF6bnlTZr3TPzUOLznKbTNMF2JASdy8dGlCc4ZEVwB9_2YrBtiGrEZPikDZ_-45vVN_nToK9ql2uBaiaGGBfcLbuA9dAIJ5O4ki08GkTFKmD5m8fd8EnJGDzoRWlbUAn6aoJmJybkBCNYiAkAVzDH7xCBQJgXtOuDbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: فرماندهی مرکزی ایالات متحده اعلام کرد تا امروز (۲۴ آگوست)، نیروهای آمریکایی ۷۱ فروند را تغییر مسیر داده، ۳ فروند کشتی را از کار انداخته و ۲ فروند شناور را به عنوان بخشی از محاصره جاری بنادر ایران، توقیف کرده‌اند
ویدئویی از ناو هواپیمابر جورج بوش، مستقر در دریای عرب و پرواز جت‌های جنگنده F/A-۱۸ نیروی دریایی آمریکا.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21462" target="_blank">📅 00:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21461">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlJaWDmGFkzDa4M-iPMsyTmIqdH9IlVgO2Ee9TF1DStaBk62Ts-acGsufPCfJFt487Mwj6_kuhFCGDxehzJRYrncdtxUSgKxW7TwBmIOUwZqr1xZ4v1MzxcezZYcbBO2kVwUGGXf6bMTZFqXWOLtihTAiKIzo8H7pqnG5OgbdXvm7GrIoAxBLZ_h7_JHkuQmyjh6RLZ8hC7VmjzrPuc7D3jrJ69cwlwzBItLZjw8tLaVaSXL_svfOjm72e3BhM7Ul0fJy7HhIVOR96zUEq8WzZluoxaDWup4x0RutV_gjYn0DlybndMyLloa4TgEV7gsx96lHY_LMH0ui7h5Puxjgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاصم پاکستانی سیک و زد برگشت… همکنون نزدیک اسلام آباده ، همچنین ۵ سوخترسان آمریکایی همکنون با سیگنال روشن در حال انجام مأموریت در تنگه هرمز  هستند
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21461" target="_blank">📅 23:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21460">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeSlYE8VjI224fz3zAuPVPauWVcSomSvnbsw6eI1uO2USp-ZxzGe_uWGMHJiVP0AwuMHYpugxlycby3cbSvqJQ7SkN4-b0BrYkdfJZbNZPB5rdDGiW-vpwKKzp_ItZj4kCw7rfmhrqe40Uchnbovw_p9hMH1Fj-Ni4An_idR4ipAxQTzW0fZPNjAY_kVg1VyOgKhNuFR4_DJRc8NSV4ogI6WBtaW7giuKCGFYogauNv5KwZeEF7RPNedgJpqhs300Sff4IVDnyC5Olspd8rU20r9xL3fRPrBx5dmYauQ4eB1Nj513tpfqFcMPtN2RDQKnBhki8eJ1ZMsR0RU5ceIIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه ایالات متحده آمریکا، اداره امنیت دیپلماتیک، برنامه «پاداش برای عدالت»:
تا ۱۰ میلیون دلار پاداش برای اطلاعات درباره رهبران کلیدی سپاه پاسداران انقلاب اسلامی ایران.
این افراد فرماندهی و هدایت بخش‌های مختلف سپاه پاسداران را بر عهده دارند؛ نهادی که از دیدگاه دولت آمریکا، برنامه‌ریزی، سازمان‌دهی و اجرای اقدامات تروریستی در سراسر جهان را انجام می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21460" target="_blank">📅 23:46 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21459">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlL4H83uD3eNijooB-b6xSpgLis3A3cvBT5JzWVphhit7K3frHD4JWoLm0wmomaIL-padG2z0OsgrusPeKDYs8nUSwuGV0iT44liAj5wQKC7UX0XcAa2hyHrrg4StIQknPy6F0Llr6LogwzoWkqQZYITP74ZzaRkjg3pd4nGETRj_D6kU2iJjd8aRkGvOqg5QtNZpH3kyiVB-pzh6neghsPqGnz4MxMbH7l9un1NwKHKUjp6BVzvXCCQ6tOqrcUUZMiQ8pv9NOlydGjcAASJE1uRSadPxejOvVN_L42N5SZ5WEkGOQD4Pb6SdZEl2UCCsXrlQRbCpQZhlqqEiSIYLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن کج بند رضایی : نتانیاهو و ترامپ یک برنامه برای 6 ماه محاصره دریایی و اقتصادی علیه ایران را دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21459" target="_blank">📅 23:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21458">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نتانیاهو : تبریک به ترامپ و بِسِن بابت آخرین تحریم‌ها علیه رژیم ایران.
شما به حق هزینه گزافی را از آن دیکتاتوری ظالم و از کسانی که به تجاوز مداوم آن کمک می‌کنند، دریافت می‌کنید.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21458" target="_blank">📅 22:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21457">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">@WarRoom
Economic Covid</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21457" target="_blank">📅 22:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21456">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پرس تی وی : ایران مستقیماً پیشنهاد مورد حمایت ترامپ که چند ساعت پیش از طریق پاکستان به ایران ارائه شد را رد کرد  ایران از سرگیری مذاکرات با ایالات متحده را نیز نپذیرفت @WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21456" target="_blank">📅 22:33 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21455">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f696f41b.mp4?token=j8x7TcQu5uvfbcGOi546uqnHVuUOa7opP2xZksc3V75YhaUiitp_eqG3kKftmZKwI1lnsDIC6FgPK4YcVWz9642bSAmIYGZsOf-yv6Zs0Sg79lY7oCR8gzMZUx3fE2sVh7bwK5q-am_5a5F9B7locA0I1Oc1q2OeIkJqpanZ3ueNP578fbAkCw4A9rQZO0s66A3T9aJd6dkR2NjHWvuRv9qKUvH307cQGFpsHDqykNtMiiOeRy4hkS6r49BKIilFTUeWx4-f83nOfCWlRSNQn4jyYJ-t__7z78tifH8QGcOqlcFLpNCt9CJQK0TPkyVgTTFkxUzvB7OaizBoRtSZ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f696f41b.mp4?token=j8x7TcQu5uvfbcGOi546uqnHVuUOa7opP2xZksc3V75YhaUiitp_eqG3kKftmZKwI1lnsDIC6FgPK4YcVWz9642bSAmIYGZsOf-yv6Zs0Sg79lY7oCR8gzMZUx3fE2sVh7bwK5q-am_5a5F9B7locA0I1Oc1q2OeIkJqpanZ3ueNP578fbAkCw4A9rQZO0s66A3T9aJd6dkR2NjHWvuRv9qKUvH307cQGFpsHDqykNtMiiOeRy4hkS6r49BKIilFTUeWx4-f83nOfCWlRSNQn4jyYJ-t__7z78tifH8QGcOqlcFLpNCt9CJQK0TPkyVgTTFkxUzvB7OaizBoRtSZ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21455" target="_blank">📅 22:29 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
