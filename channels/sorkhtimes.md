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
<img src="https://cdn4.telesco.pe/file/Ix5viNvfz0ZkEYrGFLEA60wn_RmSXLfxw9Oqv8yUbxby5QJY3RIB_-ld7Hb-ISqs7-Trco3lZj4YQGdCEroRAmfmZknBJcpkx50jSb3aFgJm4p_le8Lq24ZPH7IDP_OIUz7ZtMt-w50JtoZqdh5JIfaiWIOhHs3DOxhdBX6X1n7KcONjzw_KG634xL968EFtHiNhNsOCsWq5WjPoOe1UWGafpa8T_LLJ_SlKYvpMpDvWynZaQSrw6vFBTuVu0I8Lk9yQm9GDPvRr0GHlp3LnZJRKT-xov534G-kcYAhZ-Xrqtt-Z0W_jnYy2ZKUaZCd9m4mxD1WCpX2iovbkD89ZYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.8K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 11:50:57</div>
<hr>

<div class="tg-post" id="msg-131911">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0T9VlJawS0_akaZOyWhBrLKRpZfV8w34WpSwEKch8OwGGcLNy9J5bBP_Bp8LwVRNsYlZAdmJUpXF5eoypZNI8HVpsWfiGJD1d2Ezj85YXHFqTN5ZJsIPrFJXr7jDyXBdEL_SLZayoSIQ-m4VIDF1DpzFNWACmxP4lNy2_QtEoCwxge2qFuaY5lgnbkXWocbEolmKMwx6qz5FYSCTp69elOX8FYPbUDEh-4jn-n0fbDTgpU1fCQR3NTvm4gwpjbbJTOPh4lNnCpJ6uVvDCqilMoG5w8W161FJgxrubnNO7DSZmu7YyCCOYN6fhvryAVbS5_kETN4DzQAaYJY76uQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک تایمز :
🔴
فیفا قصد دارد دوباره ورود پرچم «شیر و خورشید» ایران پیش از انقلاب و لباس‌های مرتبط با آن را به ورزشگاه‌های جام جهانی ۲۰۲۶ ممنوع کند. این پرچم در جام جهانی ۲۰۲۲ قطر هم محدود شده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 259 · <a href="https://t.me/SorkhTimes/131911" target="_blank">📅 10:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131910">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
شایعه حضور تارتار روی نیمکت پرسپولیس از کجا آب می‌خورد؟
💸
یک دلال با سوءاستفاده از شرایط جنگی و شایعات درباره بازنگشتن خارجی‌ها ، پیشنهاد داد در صورت نیامدن اوسمار ، تارتار سرمربی پرسپولیس شود.
⛔️
این پیشنهاد جدی گرفته نشد و مدیران پرسپولیس قصد دارند همکاری…</div>
<div class="tg-footer">👁️ 275 · <a href="https://t.me/SorkhTimes/131910" target="_blank">📅 10:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131909">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
ونس معاون اول رئیس‌ جمهور در مصاحبه جديد خود اعلام کرد اصلا متوجه نمیشم مقامات رژیم ایران چه میگویند یا چه چیز میخواهند فهمیدن حرف هایشان واقعا سخت است و مدام حرف ها و خواسته هایشان تغییر میکند و نميتوانند به یك تصمیم واحد برسند ، اون 440 کیلو اورانیوم باید…</div>
<div class="tg-footer">👁️ 312 · <a href="https://t.me/SorkhTimes/131909" target="_blank">📅 10:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131908">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
قاتل الهه حسین زاده با اذان صبح فردا اعدام می‌شود.
❗️
استوری خواهر الهه: امشب، قصاص مرهم داغ خواهرم نمی شود... اما شاید کمی از بی عدالتی این دنیا کم کند. الهه جانم...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 310 · <a href="https://t.me/SorkhTimes/131908" target="_blank">📅 10:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131907">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 250T
2 گیگ 500T
3 گیگ 750T
5 گیگ 1.2T
10 گیگ 2T
40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 326 · <a href="https://t.me/SorkhTimes/131907" target="_blank">📅 10:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131906">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">●
بدترین حس وقتیه که میخوای سریع وارد سایت شی، بازی شروع شده، ولی VPN وصل نمیشه یا سایت نصفه لود میشه.
😑
● برای همین
ربات تلگرام وینکوبت
این روزا خیلی کاربردیه چون کل فضای سایتو داخل خود تلگرام میاره و عملاً بدون دردسر میتونی مستقیم وارد بازی‌ها و کازینو شی:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 655 · <a href="https://t.me/SorkhTimes/131906" target="_blank">📅 00:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131905">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 250T
2 گیگ 500T
3 گیگ 750T
5 گیگ 1.2T
10 گیگ 2T
40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 669 · <a href="https://t.me/SorkhTimes/131905" target="_blank">📅 00:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131904">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❗️
#فارس مدعی شد ؛ مدیرای پرسپولیس اصراری به موندن علیپور ندارن و اگر اوسمار هم بگه نمیخوام قرارداد علیپور تمدید نمیشه.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 805 · <a href="https://t.me/SorkhTimes/131904" target="_blank">📅 23:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131903">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⚪️
مهدی تاج: اگر پرچمی به جز پرچم جمهوری اسلامی وارد استادیوم شود به آمریکا نخواهیم رفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 791 · <a href="https://t.me/SorkhTimes/131903" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131902">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
⭕️
🔴
حضور حسین کنعانی زادگان و رضا درویش در منزل خانواده زنده یاد الهه حسین‌نژاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 793 · <a href="https://t.me/SorkhTimes/131902" target="_blank">📅 23:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131901">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⚖
پژمان جمشیدی تو جلسه دادگاهی امروزش: «من قسم میخورم که هیچکاری نکردم و این اتهام درست نیست. من با این دختر کاری نکردم و اصلا بهش دست هم نزدم. به روح مادرم قسم میخورم که من کاری باهاش نکردم.»
◽️
وکیلش هم گفت ادله و مستنداتی به دادگاه ارائه دادیم که بی‌گناهی…</div>
<div class="tg-footer">👁️ 728 · <a href="https://t.me/SorkhTimes/131901" target="_blank">📅 23:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131900">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">💢
مزخرفات خنده دار سهراب بختیاری زاده سرمربی کیسه: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 830 · <a href="https://t.me/SorkhTimes/131900" target="_blank">📅 22:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131899">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">💢
مزخرفات خنده دار سهراب بختیاری زاده سرمربی کیسه: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 776 · <a href="https://t.me/SorkhTimes/131899" target="_blank">📅 22:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131898">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=JtuDKVnhebJF8VfaA9eJr50u0khZcr3p10hbN7wnRv8fupnMi9lEORG8nbYW8jvJZEwBaKGnDInUyU0De6KOR62CxsTfB6N9a5x39plha8MnOIRl3F_RFRGvYfTEG137gPXSGC8QfJssaVKb3FhpmbVHilk0I-nWdG_CXIr6WZpVpXxML463fi-0rQUwhfl6G8dP795X44JHIWXuoCIEkoNnJjwyZv8QQBseMaSiAkhOfgLTNGI4b1TuVPvGuGkRqOVTYgIWV53_3tSlsxUMxa-IljbfXlfS1cnAGd1kPPpOLPn3EOVIYJhVyWmzRjg0TVZ6b8V75ByMIkSf0Jvzug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=JtuDKVnhebJF8VfaA9eJr50u0khZcr3p10hbN7wnRv8fupnMi9lEORG8nbYW8jvJZEwBaKGnDInUyU0De6KOR62CxsTfB6N9a5x39plha8MnOIRl3F_RFRGvYfTEG137gPXSGC8QfJssaVKb3FhpmbVHilk0I-nWdG_CXIr6WZpVpXxML463fi-0rQUwhfl6G8dP795X44JHIWXuoCIEkoNnJjwyZv8QQBseMaSiAkhOfgLTNGI4b1TuVPvGuGkRqOVTYgIWV53_3tSlsxUMxa-IljbfXlfS1cnAGd1kPPpOLPn3EOVIYJhVyWmzRjg0TVZ6b8V75ByMIkSf0Jvzug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
مزخرفات خنده دار سهراب بختیاری زاده سرمربی کیسه: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 780 · <a href="https://t.me/SorkhTimes/131898" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131897">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
باشگاه پرسپولیس: ما میگیم لیگ برگزار بشه ولی ما رو نادیده میگیرن، اونوقت تیم‌هایی که میگن لیگ کنسل بشه، معرفی میشن واسه آسیا. نمایندگان ایران تو آسیا باید با عدالت و در زمین فوتبال معلوم بشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 772 · <a href="https://t.me/SorkhTimes/131897" target="_blank">📅 22:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131896">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
💢
بیرانوند از جام جهانی محروم نمی‌شود
💢
رسول باختر، حقوقدان ورزشی در گفت‌وگو با ایسنا: در رای استیناف آمده بود که محرومیت بیرانوند شامل مرحله نهایی مسابقات بین المللی در تیم ملی نیست.
💢
با توجه به این موضوع، حتی در صورت صدور رای CAS پیش از جام جهانی، بیرانوند…</div>
<div class="tg-footer">👁️ 733 · <a href="https://t.me/SorkhTimes/131896" target="_blank">📅 22:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131895">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
نصیرزاده، وکیل علیرضا بیرانوند: در صورتی که حتی رای محرومیت ۴ ماهه این دروازه‌بان توسط دادگاه CAS تایید شود، محرومیت وی شامل جام جهانی نخواهد شد.
⏺
به محض اینکه هزینه دادرسی واریز شود، رای صادر نمی‌شود. تا بخواهند رای را صادر کنند جام جهانی تمام شده است.…</div>
<div class="tg-footer">👁️ 735 · <a href="https://t.me/SorkhTimes/131895" target="_blank">📅 22:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131894">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❗️
پرسپولیس شاکی از بمب درویش/ حدادی: اجازه دهید دلایل را نگویم!
🔴
مناقشه باشگاه پرسپولیس با سرژ اوریه، مدافع سابق این تیم، وارد مرحله جدیدی شده و این باشگاه رسماً علیه بازیکن ساحل عاجی خود شکایت کرده است. پیمان حدادی، مدیرعامل پرسپولیس، با اعلام این خبر، ابراز…</div>
<div class="tg-footer">👁️ 736 · <a href="https://t.me/SorkhTimes/131894" target="_blank">📅 22:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131893">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
ترامپ درباره ایران: ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم
🔹
خیلی زود خواهید فهمید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 776 · <a href="https://t.me/SorkhTimes/131893" target="_blank">📅 21:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131892">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2773afe10e.mp4?token=L8Sua2jpvqOHyH0J4R0yy1zR0Bt-Vcy7J8xHOvy4vWK2wzoeLpXmafZ2xiMI_cu81ktuM1U1iZS-60gnoeovJhhptKKZLCbit10Lsm0iGZuzaex-mc-kRS7wD4oJjUZlaSUz7O_68aXHULYnrihGVIUeGqH-V6AGPdv-KfpOK2C-SQNLIc463NejfrejfaXiYkRD8mmDt-9xgJ3dvPqtoQYhyA6ydW2IzdWgMyhHidkJdy8GCh8OT2IYdRuiVQULeVq3Jw7z2tSIQTYGYg_ezC2lydMHjR56sLq3lMheFWSvS7-MgpSXmQQQ_Dn-ifaepfpJnZNaZf_fPyCgjtW_ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2773afe10e.mp4?token=L8Sua2jpvqOHyH0J4R0yy1zR0Bt-Vcy7J8xHOvy4vWK2wzoeLpXmafZ2xiMI_cu81ktuM1U1iZS-60gnoeovJhhptKKZLCbit10Lsm0iGZuzaex-mc-kRS7wD4oJjUZlaSUz7O_68aXHULYnrihGVIUeGqH-V6AGPdv-KfpOK2C-SQNLIc463NejfrejfaXiYkRD8mmDt-9xgJ3dvPqtoQYhyA6ydW2IzdWgMyhHidkJdy8GCh8OT2IYdRuiVQULeVq3Jw7z2tSIQTYGYg_ezC2lydMHjR56sLq3lMheFWSvS7-MgpSXmQQQ_Dn-ifaepfpJnZNaZf_fPyCgjtW_ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره ایران: ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم
🔹
خیلی زود خواهید فهمید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 922 · <a href="https://t.me/SorkhTimes/131892" target="_blank">📅 19:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131891">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
🔴
اگر وحید هاشمیان و پرسپولیس توافق نکنند، تکلیف صدور کارت مربیگری اوسمار چه می شود؟ هوشنگ نصیرزاده پاسخ می دهد
‼️
‼️
نصیرزاده: برای فسخ قرارداد یا برکناری سرمربی هیچ محرومیتی تعیین نشده است و فقط باید غرامت پرداخت شود. اگر در قرارداد وحید هاشمیان مبلغی برای…</div>
<div class="tg-footer">👁️ 970 · <a href="https://t.me/SorkhTimes/131891" target="_blank">📅 18:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131890">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
باشگاه پرسپولیس با ارسال نامه‌ای به مسعود پزشکیان خواستار جلوگیری از بی عدالتی در اعلام نمایندگان ایران برای فصل بعد رقابت‌های فوتبال آسیا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 922 · <a href="https://t.me/SorkhTimes/131890" target="_blank">📅 18:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131889">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
اعتراض کنایه‌آمیز باشگاه پرسپولیس: نماینده ایران در آسیا نباید با تصمیمات سلیقه‌ای و خارج از زمین فوتبال مشخص شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 934 · <a href="https://t.me/SorkhTimes/131889" target="_blank">📅 18:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131887">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✅
با اعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 996 · <a href="https://t.me/SorkhTimes/131887" target="_blank">📅 15:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131886">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⚡️
حکم جلب رشید مظاهری گلر سابق کیسه به خاطر بدهی ۴ میلیاردی صادر شد، میگن متواری شده!
⚡️
عجیبه با این قرارداد های میلیاردی که داشتن ۴ میلیارد بدهکار باشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131886" target="_blank">📅 15:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131885">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
یکی از گزینه‌های اصلی باشگاه ، برای گلر ذخیره جایگزین امیررضا رفیعی آرمین عباسی گلر جوان پیکان تهران است   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131885" target="_blank">📅 15:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131884">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVdfY6jWgyk4A9dFqq1-1FYpBbUZH_AN913Q7XZ0ZZFKorZrRzQ8U7bpP-pLRE7B3Wew4q34BIGmvqWgThmABnEpg7-88afcK1P8x8iBe9tdiuUfWJ8L9BhS3__b7oKTgGiR0rld2gfkSUov_dVUuGePhbmdYaQHW4P4oecQ3QkYVQh_y_q0CnzKAJ1JJj2iX6Tsmer3acJC2yLdXmdZYAoOi3DPq6QhfSidYh1AYi2-uGh50uDPTLiPpyx56o5Db4iwI6DnB8wBkEF0Q3xEHywgZe4E4AK2WLpKEUL_Hi_8oxZfXFZFY8oKj2a9ZZ2L68gfxmVPnXetyvjFLADaNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اعتراض کنایه‌آمیز باشگاه پرسپولیس: نماینده ایران در آسیا نباید با تصمیمات سلیقه‌ای و خارج از زمین فوتبال مشخص شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 979 · <a href="https://t.me/SorkhTimes/131884" target="_blank">📅 15:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131883">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
ترامپ درباره ایران : من فعلاً عقب انداختمش، امیدوارم شاید برای همیشه، ولی شاید هم فقط برای یه مدت کوتاه
🔴
چون با ایران مذاکرات خیلی مهمی داشتیم و باید ببینیم چی ازش درمیاد  -
🔴
از من خواستن عربستان، قطر، امارات و چند کشور دیگه که اگه میشه این رو دو سه روز…</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131883" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131882">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
علوی، سخنگوی فدراسیون فوتبال: دو هفته بعد از 10 خرداد و به طور کلی قبل از جام جهانی باید سهمیه‌ها را به AFC اعلام کنیم/ استقلال، تراکتور و سپاهان الان هستند ولی قطعی نیست؛ باید مجوز حرفه‌ای آنها صادر شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131882" target="_blank">📅 12:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131881">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdYElz5UbsSVgy32wrY4JEgbSycK7p6Rkj_ULozIRbShQPBDPpHBDruS522u9QVQiC7yZHXmzHBLfBIEVFCFhs-6lDepcwCTC39lAElORqo4W_VzJGK59hg5dQPgX5NcKJhIcz8JG_JTsfz5bBveS_RJPQloCtpKHtoQEcFhbtid2wQm3diiFFnlu-8rlSrG9oOFiRXrnOZkJBC_ZwB7omWsq_O83Yr02aRyDrD5z24pUZOYNEWkukdUVqwKjZsZaDvP3d8fR-Qncqs7mpuXk6MtFPGnQ5uQWbjV2-oaOONfTcutpFoTnCIzjUta_ByteHkKkfP6zrs4_zlZSqgOyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یک تراکتوری در رادار پرسپولیس
◽️
با توجه به نیمکت نشینی صادق محرمی در این فصل در تیم تراکتور به نظر می‌رسد در انتهای فصل از این تیم جدا شود و با توجه به تمدید احتمالی اسماعیلی‌فر و حضور مهدی شیری در پست دفاع راست تراکتور صادق جایی در ترکیب تراکتور نخواهد داشت و از پرسپولیس به عنوان متحمل ترین گزینه وی یاد میشود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131881" target="_blank">📅 12:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131880">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
تغییر بزرگ در نقل‌وانتقالات؛ لیگ برتر ایرانی‌تر می‌شود
❗️
فوتبال باشگاهی ایران در آستانه فصل جدید رقابت‌های لیگ برتر با شرایطی متفاوت نسبت به سال‌های گذشته روبه‌رو شده و به نظر می‌رسد سیاست اکثر باشگاه‌ها در نقل‌وانتقالات تابستانی به سمت کاهش هزینه‌ها و استفاده بیشتر از بازیکنان داخلی تغییر کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131880" target="_blank">📅 12:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131879">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 250T
2 گیگ 500T
3 گیگ 750T
5 گیگ 1.2T
10 گیگ 2T
20 گیگ 3.5T
40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131879" target="_blank">📅 11:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131878">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🛜
سرور نامحدود 1 ماهه
Anyconnect
سرعت عالی،یوتیوب رو هم ساپورت میکنه
فقط و فقط 4.5T
🔥
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131878" target="_blank">📅 09:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131877">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mf3Qvra4hxnQhBJfn0RjwFTlSXrNuEhHvRXETZFjo6nG9BMMz80yscOgh4tImG9aTeXPZAk1sDV_2WcDaHtqTjXvocB9esDHDDFD9b-6lL4S45RhektUnIFFikMOBcHzGWnPPscCdtjmLlCOQNOD7eHzAHJDcf5lDed4VeXtSg5OyK3KcQ_2LA_ai-FZk-CaCgypLzeekeHszJfj21NglTPKH7tFI9_m4gAf0wgeXh7wZJTtXDum6bl8foJH5hxLjNXGoTrtKFup6jwL59fF12XH93X7rSZz7WuFB3Rz2UqvwY-BWNVCw7rqVlszWPgjPLDwiqdPDAB0L8FImFrWJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
دسترسی سریع و مستقیم به
وینکوبت
📌
دیگه لازم نیست بین لینک‌های مختلف بگردی یا وقتت تلف بشه.
📌
فقط با یک ورود ساده به ربات رسمی، مستقیم وارد سایت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
⚡️
ورود سریع و بدون معطلی
⚡️
بدون لینک‌های اضافی و گیج‌کننده
⚡️
دسترسی مستقیم از داخل تلگرام
😀
همه چیز برای راحتی کاربران داخل ربات فراهم و قرار داده شده.
🔵
برای تحلیل‌ها و اخبار سایت وارد کانال سایت شوید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/131877" target="_blank">📅 02:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131876">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe16cfa21f.mp4?token=SX0I351hp5PStnXEqJvRkqh79TT4NbR1yalixZhBevVdgk-MbdegMWER3qtl4Fd_WbSUMVezqRaQPf6P7ABnqeM7SipXKC1PVA1vMVpZCEqHzCBM7vH21c3LZXSS7sphbOwIilPlDvMXE24HooK06Ap7c95r2gBEOpF_VKXI_GgSoXjdpSmXxRCIHcpkFSxQqFv1WDx9cwCjb9GrThrXABs3y6s7a9HaFUhOWS0jwcDe_VdwFdmDN3MnsXRwsGO0Fcl-IcrC0pH3l2NdOm3J6NQKdjJ6KffR7belHtD2eAr7tk9D4JQ21lB4Rn8K_U4ueBtetuCpq2Z5o6xSjtPhSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe16cfa21f.mp4?token=SX0I351hp5PStnXEqJvRkqh79TT4NbR1yalixZhBevVdgk-MbdegMWER3qtl4Fd_WbSUMVezqRaQPf6P7ABnqeM7SipXKC1PVA1vMVpZCEqHzCBM7vH21c3LZXSS7sphbOwIilPlDvMXE24HooK06Ap7c95r2gBEOpF_VKXI_GgSoXjdpSmXxRCIHcpkFSxQqFv1WDx9cwCjb9GrThrXABs3y6s7a9HaFUhOWS0jwcDe_VdwFdmDN3MnsXRwsGO0Fcl-IcrC0pH3l2NdOm3J6NQKdjJ6KffR7belHtD2eAr7tk9D4JQ21lB4Rn8K_U4ueBtetuCpq2Z5o6xSjtPhSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری فوتبال برتر: فردا قرار است جلسه‌ای برگزار شود تا چمن استادیوم آزادی را به بهانه ویروسی شدن جمع کنند و سپس طرح هیبریدی اجرا شود.
🔹
ما چمن هیبریدی را در تبریز دیدیم. نکند چمن آزادی هم به همین سرنوشت دچار شود. چمن در فوتبال ایران مافیا دارد. مراقب باشید کاسبی اتفاق نیافتد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131876" target="_blank">📅 01:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131875">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
ترامپ درباره ایران : من فعلاً عقب انداختمش، امیدوارم شاید برای همیشه، ولی شاید هم فقط برای یه مدت کوتاه
🔴
چون با ایران مذاکرات خیلی مهمی داشتیم و باید ببینیم چی ازش درمیاد  -
🔴
از من خواستن عربستان، قطر، امارات و چند کشور دیگه که اگه میشه این رو دو سه روز…</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/131875" target="_blank">📅 01:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131874">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ : ما داشتیم آماده می‌شدیم که فردا یه حمله خیلی بزرگ و جدی انجام بدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131874" target="_blank">📅 01:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131873">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26879febf9.mp4?token=GPcf8Zwy8IolA94yGl8Dy0W76OXyZ93_LUfkG_FBrM_BXi3wrZIYUphv-hh3a2t4jGJG11-iMSZMeq11QJCnRG1Q1QIMJ0XbmRsqEqJh6SV7Bsr7157-o84H24bGOFILYknQCvr2VotilN7VK9zK6mtXYBvZL6eern-po_Q_0h2W0ClFN7Eaw_J38QIw4XoCCdeuu2VgQx3WguF_tVZuNyHkGfFqRBdxp_irXMATXxtIf2IK2FrkT4WsH8yQizY0Rf5-Kn98Q5rLqgH4D3zIQ9sMZyq6jlSr3pJhKD9tSB5c_6TIdAYfGFs4CZRsornZ_GhJ_z4PrxusfCiadVA1pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26879febf9.mp4?token=GPcf8Zwy8IolA94yGl8Dy0W76OXyZ93_LUfkG_FBrM_BXi3wrZIYUphv-hh3a2t4jGJG11-iMSZMeq11QJCnRG1Q1QIMJ0XbmRsqEqJh6SV7Bsr7157-o84H24bGOFILYknQCvr2VotilN7VK9zK6mtXYBvZL6eern-po_Q_0h2W0ClFN7Eaw_J38QIw4XoCCdeuu2VgQx3WguF_tVZuNyHkGfFqRBdxp_irXMATXxtIf2IK2FrkT4WsH8yQizY0Rf5-Kn98Q5rLqgH4D3zIQ9sMZyq6jlSr3pJhKD9tSB5c_6TIdAYfGFs4CZRsornZ_GhJ_z4PrxusfCiadVA1pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما داشتیم آماده می‌شدیم که فردا یه حمله خیلی بزرگ و جدی انجام بدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131873" target="_blank">📅 01:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131872">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0edd05b28.mp4?token=qgn5HBDZlVt2Nklwcu1OnFkrP3S-STmZ_TGI4-VQ0eyd67792yHDERMLQg_gudAlpKR0Hi1NApaZOaBsN3mJHj7UDEPOXfeMPflJjzC6vOdL4isfPJhk2Iy3vYmpCeZYhnseXb3bfz-c0SMy19B3jvWZsVzN7P73RHPQfGMVz17-m7g1bIg7GCNPWJ4lDNvqw-BFRqilci5RZ9LpjaSqCw207Lp-nKWJyUBfvV6uPobA-yV29NRUgFx52lJ992GiBky7-CZhMzD_WxbLQm_ZX2WlNqxp94Ujel7RzEIkN2m187uRQZw3HL72Btfqnw7cI76cNitDgi_r_PA-ebkyHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0edd05b28.mp4?token=qgn5HBDZlVt2Nklwcu1OnFkrP3S-STmZ_TGI4-VQ0eyd67792yHDERMLQg_gudAlpKR0Hi1NApaZOaBsN3mJHj7UDEPOXfeMPflJjzC6vOdL4isfPJhk2Iy3vYmpCeZYhnseXb3bfz-c0SMy19B3jvWZsVzN7P73RHPQfGMVz17-m7g1bIg7GCNPWJ4lDNvqw-BFRqilci5RZ9LpjaSqCw207Lp-nKWJyUBfvV6uPobA-yV29NRUgFx52lJ992GiBky7-CZhMzD_WxbLQm_ZX2WlNqxp94Ujel7RzEIkN2m187uRQZw3HL72Btfqnw7cI76cNitDgi_r_PA-ebkyHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمله عجیب سخنگوی فدارسیون خطاب به تیم‌هایی که هفته اول خرداد تمرینات‌شان شروع می‌شود
◻️
علوی: شاید آنها خبری دارند که ما نداریم؛ ورزش کردن اتفاق خوبی است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131872" target="_blank">📅 01:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131871">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db79861a4e.mp4?token=JR6aa97ME4LQsmtBtYDLRWe83_qYfqbAM1WLQRTtQNHuNDPKnvZ66l_dMO_DDY-R7LcrKO0H6EvCeK1KawyuYVReTQyoeHfTOWWb2klqyFq83ESHUd6CQnAd7iLDyFbiR9L657xT3lbB28zDqo-N1FJuvJypW0L5pDzjNzctVvdZO7G9SeeptGan0tXcn9_Phe4BMcrsBXAu21T_f5va3PsAFCWXI7s1W4SVey1GgxXozLJb__qgknx0AWe0iNptN3ExlpYsdrg1BAuSQ2FhSE-_AWIq49nfYa7-y0knY5nxqQAja_qHAQO94-ejW1JQOqvoB-Zh9w5l9NPgpzi0Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db79861a4e.mp4?token=JR6aa97ME4LQsmtBtYDLRWe83_qYfqbAM1WLQRTtQNHuNDPKnvZ66l_dMO_DDY-R7LcrKO0H6EvCeK1KawyuYVReTQyoeHfTOWWb2klqyFq83ESHUd6CQnAd7iLDyFbiR9L657xT3lbB28zDqo-N1FJuvJypW0L5pDzjNzctVvdZO7G9SeeptGan0tXcn9_Phe4BMcrsBXAu21T_f5va3PsAFCWXI7s1W4SVey1GgxXozLJb__qgknx0AWe0iNptN3ExlpYsdrg1BAuSQ2FhSE-_AWIq49nfYa7-y0knY5nxqQAja_qHAQO94-ejW1JQOqvoB-Zh9w5l9NPgpzi0Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
علوی، سخنگوی فدراسیون فوتبال: دو هفته بعد از 10 خرداد و به طور کلی قبل از جام جهانی باید سهمیه‌ها را به AFC اعلام کنیم/ استقلال، تراکتور و سپاهان الان هستند ولی قطعی نیست؛ باید مجوز حرفه‌ای آنها صادر شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 941 · <a href="https://t.me/SorkhTimes/131871" target="_blank">📅 01:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131870">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f7d54cae7.mp4?token=KvckV35DDTcE5wkvfdLzpbAN7lAU7budeOqhNtt04eZbrI_osbKLFchXHGOc3IMT_wvnwFOS3x1CxtocJOSQ8eDNACw6GMTMbBVrmloh6LU1adwlkfrGrgKtQVibUHZ0pWOzZY19Go5bAzhlAfyCF-xPAbNeC-Q8mn30pKBa_fgwvpxkMI8vE3D2dJJSopmM1Npse3sRINGfA3hR5cVk4HbfcAWQqa4aCqqX6fPaZZyt-Ust2j6ymogd2cifgDQYG3AB-tNbNHJp4_cqS8I3eTdJ5BtBDswNRkCG7HGTcw-W_VBU9eXMHAIurclcLUGnBmOofDGD1bYU9nLJYS3P2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f7d54cae7.mp4?token=KvckV35DDTcE5wkvfdLzpbAN7lAU7budeOqhNtt04eZbrI_osbKLFchXHGOc3IMT_wvnwFOS3x1CxtocJOSQ8eDNACw6GMTMbBVrmloh6LU1adwlkfrGrgKtQVibUHZ0pWOzZY19Go5bAzhlAfyCF-xPAbNeC-Q8mn30pKBa_fgwvpxkMI8vE3D2dJJSopmM1Npse3sRINGfA3hR5cVk4HbfcAWQqa4aCqqX6fPaZZyt-Ust2j6ymogd2cifgDQYG3AB-tNbNHJp4_cqS8I3eTdJ5BtBDswNRkCG7HGTcw-W_VBU9eXMHAIurclcLUGnBmOofDGD1bYU9nLJYS3P2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤍
علوی، سخنگوی فدراسیون فوتبال: در حال پیگیری هستیم که باشگاه‌ها از تاریخ 9 اسفند به بعد درپی شرایط اضطراری به خارجی‌هایشان حقوق ندهند؛
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 924 · <a href="https://t.me/SorkhTimes/131870" target="_blank">📅 01:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131869">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 250T
2 گیگ 500T
3 گیگ 750T
5 گیگ 1.2T
10 گیگ 2T
20 گیگ 3.5T
40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 961 · <a href="https://t.me/SorkhTimes/131869" target="_blank">📅 00:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131868">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سه ماه تعطیلی؛
🚨
🔴
وظیفه اصلی که هیئت مدیره پرسپولیس فراموش کرده
🔺
هیئت مدیره باشگاه پرسپولیس که طبق قانون موظف است به صورت هفتهگی جلسه برگزار کند (و عادت داشت این جلسات را دوشنبه‌ها برگزار کند)، اما بعد از آتش بس چرا نزدیک به سه ماه است حتی یک جلسه رسمی نداشته؟
🔺
در این مدت، اعضای محترم هیئت مدیره همگی در تهران حضور داشته‌اند. در بازی خیرخواهانه حاضر شدند، مصاحبه کردند، واکنش نشان دادند، ابراز نگرانی و همراهی کردند؛ اما وظیفه اصلی خود را زمین گذاشته‌اند.
🔺
مدیرعامل باشگاه بدون پشت گرمی مصوبات هیئت مدیره، عملاً دست و بال بسته است. هر حرکت اجرایی نیاز به تأیید و چارچوب دارد؛ وقتی جلسه‌ای تشکیل نشود، خبری از مصوبه نیست و مدیریت قادر به گره‌گشایی از کارهای روزمره و بلندمدت نخواهد بود. نتیجه؟ باشگاه لنگ می‌زند. قراردادها روی زمین می‌ماند، برنامه‌ریزی مالی بلاتکلیف است و تیم در آستانه فصل حساس، سردرگم اداره می‌شود.
🔺
هیئت مدیره نباید تنها به حضور نمادین در رویدادهای عمومی و مصاحبه‌های احساسی اکتفا کند.
فریاد هواداران را بشنوید: «هیئت مدیره، به وظیفه قانونی‌ات عمل کن، وگرنه باشگاه را بیشتر از این به زمین نزن.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131868" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131866">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
#فوری | ترامپ:
🔴
امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس‌جمهور امارات متحده عربی، محمد بن زاید آل نهیان، از من خواستند که حمله نظامی برنامه‌ریزی‌شده‌مان علیه ایران را که برای فردا تعیین شده بود، به تعویق بیندازیم
‼️
…</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131866" target="_blank">📅 22:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131865">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
#فوری | ادعای ترامپ:
🔻
حمله به ایران را که قرار بود فردا انجام دهم به تعویق انداختم
‼️
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131865" target="_blank">📅 22:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131864">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/372dcfefd5.mp4?token=G4vBEqiR3saGYmDvsiJIzZEVqMShkl0uhbJ7qSqYdLc2xeMD9Oi08uUR5IT75spogVqKIWPx1ssb0BfyY0TstpKPrkoEzjnrtWuSlumWsqh487mMq38JOfEH8f2bbG0IAH2Rlz4Z1-46CzLg8wj0rRzjDsewnObBIU_0hnLxPx9kZC40ebt1xfjPiv8t-WKOJX7KZYejafLRG1HNJxS1V0D4l2IRsMK9ge_CsPdwOiFlVZBr4kKj426GsftsZKOrwCt3iVHDl0AowRhu-Yo7PkJT6O9mWXXy3JLhxCZpI34hKiO5PP4dsfNLsURq5syn_plULn_SVgXt04tSRH266w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/372dcfefd5.mp4?token=G4vBEqiR3saGYmDvsiJIzZEVqMShkl0uhbJ7qSqYdLc2xeMD9Oi08uUR5IT75spogVqKIWPx1ssb0BfyY0TstpKPrkoEzjnrtWuSlumWsqh487mMq38JOfEH8f2bbG0IAH2Rlz4Z1-46CzLg8wj0rRzjDsewnObBIU_0hnLxPx9kZC40ebt1xfjPiv8t-WKOJX7KZYejafLRG1HNJxS1V0D4l2IRsMK9ge_CsPdwOiFlVZBr4kKj426GsftsZKOrwCt3iVHDl0AowRhu-Yo7PkJT6O9mWXXy3JLhxCZpI34hKiO5PP4dsfNLsURq5syn_plULn_SVgXt04tSRH266w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
| ادعای ترامپ:
🔻
حمله به ایران را که قرار بود فردا انجام دهم به تعویق انداختم
‼️
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131864" target="_blank">📅 22:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131863">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
ترامپ: ایران می‌داند به زودی چه اتفاقی برایش خواهد افتاد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131863" target="_blank">📅 22:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131858">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXwwS-f2TPIsJyT0EiHF9MAVLiLBX8tvzbqtNDxvj_pRKbYwxxk7eg0wwLqzTFBZz-IpdgwrtHLFWBQPZyEzx8WWwN9yN3sXk6EgWlZOlmrtG5JBlW7EF68uYdmG4wHUj6xN14tNE_yJyI7Bh3zOk2o0W0tS3FZuVYX5x7CtXxDFskpp5Zws3_zAjGIlEnbJQESZJirxOd10crcR9N2WtoDbImLv4fE_ShGsayRbLIxmFta5D7YxyZVcwHt5m_kTOmUGruLfZfgsZ5xWU1WXFBq4uVrwA-Ts8w18HUCEl26Rt77TQ5t_5dlpWDfNTjNj1a-QhgT-oOcEn6Co2dWinA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یورگن لوکادیا، مهاجم هلندی سابق پرسپولیس، به اردوی تیم ملی کوراسائو برای جام جهانی ۲۰۲۶ دعوت شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131858" target="_blank">📅 21:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131857">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
کاخ سفید: آخرین پیشنهاد ایران که امروز ارائه شد نیز به دلیل ناکافی‌ بودن به صورت کامل رد شد، دیگر بمب ها مذاکره خواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 966 · <a href="https://t.me/SorkhTimes/131857" target="_blank">📅 21:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131856">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
🚨
ممکن است مجوز حرفه ای چند باشگاه مطرح صادر نشود و از شرکت در رقابت های آسیایی حذف شوند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131856" target="_blank">📅 21:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131855">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
باشگاه تکذیب کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 925 · <a href="https://t.me/SorkhTimes/131855" target="_blank">📅 21:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131854">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXhRbdG2pOqhYrYLWoPLy_Wg2j53H6U5_5sUHfbdM0WDs3yB5e344EVK3ikTlMBlewaMXBPiWfsVI2jf-RRtGHiofMF-yjHSyeY5UP8hLdTtCNCi30OSXtC-HdhWtS8JAxf7XxGIJoE57OXoGWwqCwWecbC6phjxJQ21V0dD_zzDz6AA3HyJflz_p4akUdVHOIjbySv_2x75Jh2_m-If-vlqfjh8wzVTSMPVixH1v6HwepWK_z72PdZ_r2K8WbyVb1BFJW0nE_qcrAp7ZxsD2V8q5EG8BsFynQyFr-5fGzkWViVfSLCuUYUt_0oG8Au5XFNZ3_evRkUdJ7sfx1F0eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🏅
⚽️
واکنش باشگاه پرسپولیس به شایعات در مورد معرفی نمایندگان ایران به AFC
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 903 · <a href="https://t.me/SorkhTimes/131854" target="_blank">📅 21:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131853">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
🔴
اوسمار گفته اگه دوباره جنگ نشه میام و تمرینات رو اغاز میکنیم ولی اگه جنگ بشه فسخ میکنم ولی خب غرامتی نمیگیرم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/131853" target="_blank">📅 19:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131852">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
امروز جلسه ای تصویری میان اوسمار ویه را و پیمان حدادی مدیرعامل باشگاه پرسپولیس برگزار شد و اوسمار برنامه خودش برای شروع رقابت ها و همچنین نقل و انتقالات به باشگاه داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131852" target="_blank">📅 19:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131851">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
⭕️
#شایعات
🗣
اوسمار خواهان بازگشت دانیال اسماعیلی فر و مهدی ترابی شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131851" target="_blank">📅 19:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131850">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
#فوری |   ادعای العربیه از پیشنهاد جدید ایران:
🔻
آتش‌بس چندمرحله‌ای و بلندمدت و بازگشایی تدریجی و ایمن تنگه هرمز
‼️
🔻
در این طرح از پذیرش توقف بلندمدت برنامه هسته‌ای به‌جای برچیدن کامل آن، انتقال مشروط اورانیوم غنی‌شده به روسیه به‌جای آمریکا، و جایگزینی…</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131850" target="_blank">📅 19:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131848">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b6bdc9d91a.mp4?token=QsbNuJoY9BBG_A4pGeThBDL2dMRZTKCuIDcb0pY2qJWoaZddxyegNFQZ5uYE2HBBQXE_DAw_oeTu2VnG6ALPXH0Rz671a3QWi3nK0azVMt7osvWLHqMvJadVugO-W-i9BRWt-x31NhoZHoWJuhDDhoGwDEh5NKmHLNgbCBeFpJLoaT75TvUNhM4SzoNuarIF8Q63Bhs7YkxTHDhU62zK8sbr0bulri8pxhQr_aN9u7d2Jr2n0xCFu8OY_MxvZeBWGZSOosxryKgnhZ9knBis5cSMTDy2-7NWHBSKZmZp_7kJwWXE4yIiqwoQlD2K18gccRmBAjLQ-yTVfNZcGR1mZg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b6bdc9d91a.mp4?token=QsbNuJoY9BBG_A4pGeThBDL2dMRZTKCuIDcb0pY2qJWoaZddxyegNFQZ5uYE2HBBQXE_DAw_oeTu2VnG6ALPXH0Rz671a3QWi3nK0azVMt7osvWLHqMvJadVugO-W-i9BRWt-x31NhoZHoWJuhDDhoGwDEh5NKmHLNgbCBeFpJLoaT75TvUNhM4SzoNuarIF8Q63Bhs7YkxTHDhU62zK8sbr0bulri8pxhQr_aN9u7d2Jr2n0xCFu8OY_MxvZeBWGZSOosxryKgnhZ9knBis5cSMTDy2-7NWHBSKZmZp_7kJwWXE4yIiqwoQlD2K18gccRmBAjLQ-yTVfNZcGR1mZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
|   ادعای العربیه از پیشنهاد جدید ایران:
🔻
آتش‌بس چندمرحله‌ای و بلندمدت و بازگشایی تدریجی و ایمن تنگه هرمز
‼️
🔻
در این طرح از پذیرش توقف بلندمدت برنامه هسته‌ای به‌جای برچیدن کامل آن، انتقال مشروط اورانیوم غنی‌شده به روسیه به‌جای آمریکا، و جایگزینی غرامت با تسهیلات اقتصادی بحث شده است.
🔻
این پیشنهاد بر ضرورت تضمین‌های بین‌المللی، تفکیک مسیر دریایی از پرونده هسته‌ای و نقش‌آفرینی پاکستان و عمان در مدیریت تنش‌های تنگه هرمز نیز تأکید دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131848" target="_blank">📅 18:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131847">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
🚨
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه  علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه  احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی  سامان قدوس، روزبه…</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131847" target="_blank">📅 18:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131845">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbAq0UPVbkvpPI43K_x6MEC6ImYsR3AuA0okLwy3D8Xj9YpbNL964pPcSwHv0ES9hwRvu2MnOYD-SeWPERusJyaChea09ZZoyYuJuH4AlzRewb2svCdMDj-BBX2u_sl4E2ksHBFqxmDLaJ98TEvacB8nFlkabS6F9vamXqPQaqhu7uE-ERf88n1kuNGjPZgRjwpLs7tSYfO8zk3ojU3fREsDxZLGRcF-NcB-ROLRSs-aTruqnXPnDnQ-AN8JeUpUz2Ar3MgzLk5m0jVSMGFDej86riWIk7H9tiSMwnE62euJi6OvujMyT2ZCVJVzbVgZ6vp_y8g6IGtqhZMqTdjuWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مدیرعامل پرسپولیس عضو هیات رئیسه فدراسیون هاکی شد
🔺
پیمان حدادی مدیرعامل پرسپولیس با بهرام قدیمی رئیس فدراسیون دیدار و گفت‌وگو کرد. بعد از این دیدار قدیمی با اهداء حکمی، حدادی را به عنوان عضو هیئت رئیسه فدراسیون هاکی منصوب کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131845" target="_blank">📅 17:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131843">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89becc508b.mp4?token=Wdo41ticPXu0DPfTRior_cva2PsX_vhHDac-UDn0yx-1LZ6fuZ6-ozccV4HqXn2lP3t4-2Zl8e4P7TVXNWQeug0tcdyVV6g8rc5imHSZydWLeuYMwrr1IoMqbS2MPmhygjjTn6i3CB3EgqY3_buALwnPSeY2jYYPhOtDYklRdxk5NcU_JQp6eSO_IublQhEV1nr3u_54BdkzJ2iFwLEYZE_epDatq_cKTgbvi7VFoXvbopqC881lTVtG35nwCyNyLlcMU2Iz6skiZbu_hwQyFsOGgJ8HRLkbP-RpuJX5lUIhmepCSNzRrNjT-kdcRN14We4lcmDubVJemQ4e_Ef474i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89becc508b.mp4?token=Wdo41ticPXu0DPfTRior_cva2PsX_vhHDac-UDn0yx-1LZ6fuZ6-ozccV4HqXn2lP3t4-2Zl8e4P7TVXNWQeug0tcdyVV6g8rc5imHSZydWLeuYMwrr1IoMqbS2MPmhygjjTn6i3CB3EgqY3_buALwnPSeY2jYYPhOtDYklRdxk5NcU_JQp6eSO_IublQhEV1nr3u_54BdkzJ2iFwLEYZE_epDatq_cKTgbvi7VFoXvbopqC881lTVtG35nwCyNyLlcMU2Iz6skiZbu_hwQyFsOGgJ8HRLkbP-RpuJX5lUIhmepCSNzRrNjT-kdcRN14We4lcmDubVJemQ4e_Ef474i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
قلعه‌نویی: امیدواریم ویزای ۲۸ بازیکن را بدهند/ ۴۰ درصد عقب‌ماندگی بدنی و فنی داشتیم که ۲۵ درصد آن را جبران کردیم/ شرایط سخت است ولی نباید بهانه بیاوریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131843" target="_blank">📅 17:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131842">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bfd63331d.mp4?token=jwSGFMAjwm9BqCk2-EN-SZlCqUvP6DxL7Z4zqM1M3JrC7BnZUkHzksws2ZYVA6ob9akdP-pzWxnEBNLGgH85TgGc54c0XuFiqKyCgssa1a1LrmDWdgPy462Fxq4ndZuEUSUI1uRgEvS_yQAzFFcZf7H78jciyyPgGm2FgW8pD-gsA-aNsbQYRYTN9unVosC3oVyHlKwNbpoXS0t7hRM0_h-DOf9njbHnXgOI9STnTClspVeKCul6ugPrAIIv7Ho4ppysra5xzUFmCpcTxS-xRZE-BTYCYBQKZ1zUJ0y9gJu60M5DHeHw55tEC0shWiRmZRJykCLIsZQpr5Drt_vG7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bfd63331d.mp4?token=jwSGFMAjwm9BqCk2-EN-SZlCqUvP6DxL7Z4zqM1M3JrC7BnZUkHzksws2ZYVA6ob9akdP-pzWxnEBNLGgH85TgGc54c0XuFiqKyCgssa1a1LrmDWdgPy462Fxq4ndZuEUSUI1uRgEvS_yQAzFFcZf7H78jciyyPgGm2FgW8pD-gsA-aNsbQYRYTN9unVosC3oVyHlKwNbpoXS0t7hRM0_h-DOf9njbHnXgOI9STnTClspVeKCul6ugPrAIIv7Ho4ppysra5xzUFmCpcTxS-xRZE-BTYCYBQKZ1zUJ0y9gJu60M5DHeHw55tEC0shWiRmZRJykCLIsZQpr5Drt_vG7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ورود کاروان تیم ملی به آنتالیا برای برگزاری اردوی آماده‌سازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131842" target="_blank">📅 17:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131841">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">#
منهای‌پرسپولیس
🚨
یاسر آسانی وینگر آلبانیایی استقلال در آستانه انتقال به ختافه اسپانیا قرار دارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131841" target="_blank">📅 16:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131840">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🏅
بازیکنان پرسپولیس چقدر پول گرفتند؟
⏺
پیگیری‌ها از باشگاه پرسپولیس حاکی از آن است که بازیکنان این تیم مبالغی بین ۶۵ الی ۷۵ درصد از قراردادهای خود را دریافت کرده‌اند و پرداخت صددرصد قرارداد چند بازیکن صحت ندارد.
⏺
فقط یکی از بازیکنان خارجی پرسپولیس مبلغ بیشتر…</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131840" target="_blank">📅 16:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131839">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b213799d6a.mp4?token=k6BrhlIroGzvEWEWPv-GBrn9Qw5PjhMpopzdZjf6tlTFLiW_mrlrrl5pyg-b8Vp3xtWdy-RgE7Hfek3bZ1ggvvTWCuSFo1cJnM8iN93J38VdT4vH_wTBgZMabHbSkNZMRvCS-3U6J_Rltn03zM9mG5c8d-IeMdnC4C3x-xoz8L-efBvbt3jaP_5F2UzzqmdOL7IEVonIeLFNWUjAVXiaHCJbBLO33QS9HZKOQDI-YY30OvaAHTLTVfXcuDSUgKfiNm2Ipkymj-WaCS6y_BFErmDmohDEacExC2_ax4HuxsKBl1Zg53VGwDy8FI34q0DgHAd66JyiRUDlyEPDnilvoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b213799d6a.mp4?token=k6BrhlIroGzvEWEWPv-GBrn9Qw5PjhMpopzdZjf6tlTFLiW_mrlrrl5pyg-b8Vp3xtWdy-RgE7Hfek3bZ1ggvvTWCuSFo1cJnM8iN93J38VdT4vH_wTBgZMabHbSkNZMRvCS-3U6J_Rltn03zM9mG5c8d-IeMdnC4C3x-xoz8L-efBvbt3jaP_5F2UzzqmdOL7IEVonIeLFNWUjAVXiaHCJbBLO33QS9HZKOQDI-YY30OvaAHTLTVfXcuDSUgKfiNm2Ipkymj-WaCS6y_BFErmDmohDEacExC2_ax4HuxsKBl1Zg53VGwDy8FI34q0DgHAd66JyiRUDlyEPDnilvoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
#فوری
| نیویورک تایمز مدعی شد:
🔻
آمریکا و اسرائیل در حال آماده‌سازی گسترده برای احتمال ازسرگیری جنگ با ایران در همین هفته هستند و این گسترده‌ترین سطح آمادگی از زمان آتش‌بس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/131839" target="_blank">📅 16:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131838">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
لاوروف:پروژه نیروگاه هسته‌ای بوشهر به هیچ‌کس جز روسیه و ایران تعلق ندارد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131838" target="_blank">📅 15:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131835">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">محمد پروین، فرزند علی پروین:
پدرم به دلیل زخم پا (به علت دیابت) در بیمارستان بستری شده است، اما مشکل خاصی ندارد و به زودی مرخص می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131835" target="_blank">📅 14:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131834">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
#فوری | پست جدید ترامپ درباره ایران  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131834" target="_blank">📅 13:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131833">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
۷۹ روز از قطعی اینترنتی ایران گذشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131833" target="_blank">📅 13:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131831">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAfx_h8bvXqNnkavqAv131D1TJVJePXFEQBDcwbQnSQj5FDGr3UL2VPssxGPTL2ITI670vlQ-HoGOLpTZK33VTyzP9Ao7byfVD1JUFwBCydjTI2SYOG0IQYXHO0Bty5TxxHoTVCD5HEnuLi8iMjEh53mKwVUF31U6BHB9OVH5ygc6jO4PTT4x_h9x4i89Yc6exewKtQ5lpm-2Ut2kGKEBPgKW0HCOx0S7MV4R7SjuW3aJ2O3_jrU8fgWhTMDnx2jmpu8OI4YB79cMXFy-_9mverEO1SNm_BDJqKrbG51xiWBUk-R_0FCg6dER5ByUOkW4sWLeLRZbIjc5Lr6cRjB4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سردار آزمون پس از خط خوردن از لیست نهایی تیم ملی برای جام جهانی ۲۰۲۶، تصویر پروفایل خود را از لباس تیم ملی به پیراهن باشگاهی شباب الاهلی تغییر داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131831" target="_blank">📅 11:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131830">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇷
بازیکنان تیم ملی و امضای پیراهن های جام جهانی برای تقدیم به مردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/131830" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131829">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87ff620cb1.mp4?token=d9bBJs0AOMu-xYQ_IJj9-IzPxDGD8rkDOyL82vSXnj14nz_cHIPn2kNZRpf1T2fFMjPVcYc9gJbQU2jdUCwWlch17XDSb3iHZIv-FOGEDz9Al_Mmp78rB79CnoaGdgrnZ35ARMUAhTrKy3vVAFcXQWVDH2oqI4-3yPxce8t5BaeKONHSdLb7M09zTxmVOacrxm8CzOOaVrCoAbGafzf2WvQDdZuDMo3tKpy7FTdxABWfmFwuweF4PLT3t5CD9N7bUYXkx4n4l1sIIUNXEMnOF8Atda0dGjHM9v1gOg7TX8rBrOvfrynQhOeFnapPFsSSxIbKKURjLTxMI73EXDp8KIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87ff620cb1.mp4?token=d9bBJs0AOMu-xYQ_IJj9-IzPxDGD8rkDOyL82vSXnj14nz_cHIPn2kNZRpf1T2fFMjPVcYc9gJbQU2jdUCwWlch17XDSb3iHZIv-FOGEDz9Al_Mmp78rB79CnoaGdgrnZ35ARMUAhTrKy3vVAFcXQWVDH2oqI4-3yPxce8t5BaeKONHSdLb7M09zTxmVOacrxm8CzOOaVrCoAbGafzf2WvQDdZuDMo3tKpy7FTdxABWfmFwuweF4PLT3t5CD9N7bUYXkx4n4l1sIIUNXEMnOF8Atda0dGjHM9v1gOg7TX8rBrOvfrynQhOeFnapPFsSSxIbKKURjLTxMI73EXDp8KIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بازیکنان تیم ملی و امضای پیراهن های جام جهانی برای تقدیم به مردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 990 · <a href="https://t.me/SorkhTimes/131829" target="_blank">📅 11:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131828">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0f3d0278.mp4?token=lzDCNUk2pgrPyrh4nyzmoWSq2npmKXNk6i7csrwI8iRoZREAchyaX6urxtU8YwMHgCEebEc0DfCF_z02WUpvUaWzr9h-jmTRcXWsjjiSiLEjYuwKqisdHp1OgYog3yEYLbG6EK-gWeT2DH0gysDW1eBxlQGi7NfLte0FkHvSiVXuFcfhz8mMibXo4hB_3Z3poUuz6buJWL5MzePKH6PiC3v2UmUEPhe_wd4G1PO7XvPXDmOkhRodsMJcAJSpkYy3MvLlrxvL7S_uFGlik6iplgtujqjILFHDzWYSBPdYuMMrpHvbKF6GNOvMUhhx6mVlExLtpV04sgfTT3iEHlBQAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0f3d0278.mp4?token=lzDCNUk2pgrPyrh4nyzmoWSq2npmKXNk6i7csrwI8iRoZREAchyaX6urxtU8YwMHgCEebEc0DfCF_z02WUpvUaWzr9h-jmTRcXWsjjiSiLEjYuwKqisdHp1OgYog3yEYLbG6EK-gWeT2DH0gysDW1eBxlQGi7NfLte0FkHvSiVXuFcfhz8mMibXo4hB_3Z3poUuz6buJWL5MzePKH6PiC3v2UmUEPhe_wd4G1PO7XvPXDmOkhRodsMJcAJSpkYy3MvLlrxvL7S_uFGlik6iplgtujqjILFHDzWYSBPdYuMMrpHvbKF6GNOvMUhhx6mVlExLtpV04sgfTT3iEHlBQAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امیر قلعه نویی و امضای پیراهن تیم ملی با جمله تقدیم به ابر ملت جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131828" target="_blank">📅 11:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131826">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVa7yDcFqFDdrqKb6zejLdrcTv4vkoz7LDSY2wLKk9PUu2TFh9nnti7P6cOsfv78wZqjRkZadVICiDRPFlPZEOfW3DE5eGSsG-rS6BuKxL4Vtx-KKjuKQG_2HuVvqyOuRZtEAYQOQppxGBVBzKaSxrWoTZ_zexC2w_Elcyk-WUXab77xvBHfRUbpkw_vkyj8Sbo6R2n9QKXDuUmI76mGKRK0m_JZWCPPCaPZxYUZfG3B336y6MOWepALJ0yZ6lQJk6AIoxKQOid8_mJppyEL9oXe7dIMtuYN0i5MjMF7jK0Zq2UckLXnQVj2pp-N9d4WzwS-kuLvb7-VDUCr3lRzTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ لحظه شلیک مجری شبکه افق به پرچم امارات را منتشر کرد و گفت: خواهیم دید چه خواهد شد
!!!!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131826" target="_blank">📅 10:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131825">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gw90IqQM-KI1saBDJvcCY1TXeqyHAQrtpxBC6WahziN8QgOEiVtletMsSm3b6VXRGsBmRZCSXb9-xiOcmAed4KE9e9wFy_FRZ72BpgdlQvyK8vfvsy8-LAF0SBvebvUjSr3LE0LfSFpyqOVpp0ilqJRbVzAa6txNr2cELnrOkm8y4U0YD2l3XPVUR6VtPpoJM8wrq_Ncf79FN3_t88EXy8_KTZZoXIPJ9OQfc7ZoPKiotYSU9i2ifPkjD83wGMX5Pgb5iaYd3j5vKDXGYSfWmmYHjK5ZvjyiI8Rkxbk8DWALjI4l2eDl6gmQ7LJ4dMTt5IofKqMi8cCrdsoyrCygrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیمان حدادی مدیرعامل پرسپولیس قول داده که درصورت ماندگار شدن وی در نقل و انتقالات تابستانی یک تیم مدعی و جوان را تحویل دهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/SorkhTimes/131825" target="_blank">📅 10:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131824">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
امروز جلسه ای تصویری میان اوسمار ویه را و پیمان حدادی مدیرعامل باشگاه پرسپولیس برگزار شد و اوسمار برنامه خودش برای شروع رقابت ها و همچنین نقل و انتقالات به باشگاه داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131824" target="_blank">📅 10:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131822">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⚪️
امیر قلعه‌نویی: ما بازیکنایی داریم که همین الان میتونن تو رئال و بارسا بازی کنن. حسین کنعانی چیزی از سالبیا کم نداره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131822" target="_blank">📅 08:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131821">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlMLomxzzSI4_naiNAhBreH3W2oiatYcgtMM86A7DbAJ3Bqv24mxl8KgjsTRLb0voSSMqEnSCy432zSZjpDG4K7nQUWhmSi0y190XHqsKDyF95Ht3Jis3t5pCt6T2GKtjgiO6uuEX5gj7J_QBkFRiEZ-T0Di56IvbUHMCnzGnBSkdDfs1iRRlfft9zGdlAbtncS6kofddzUo7f9nlZEtVPkM3Y29_CKwClqocAEQNrmZ1nj58MCvUaC_FYBWpsHZowJ2StZSeFbTOhfg9Wy7TZ4y-KZzR--80zs41ZOntTuIjRV7tBO2zieD21ICiFpd1emwHBgcXrKsg6d8tqMQzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
۹۰٪ کاربرا هنوز اشتباه وارد سایت میشن!
تو جزو اونایی یا میخوای حرفه‌ای عمل کنی؟
✅
ورود سریع به وینکوبت فقط با یک کلیک ساده:
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
نه لینک اضافی
📌
نه سردرگمی
📌
نه اتلاف وقت
📌
مستقیم، سریع، بدون دردسر وارد شو!
⏳
دیر بجنبی، از بقیه عقب می‌مونی.
🔗
الان وقتشه مسیر درستو انتخاب کنی:
🤖
@Wincobet_bot
📌
برای تحلیل بازی‌ها و آخرین اخبار سایت جوین بدید:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/131821" target="_blank">📅 01:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131820">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
#فوری | پست جدید ترامپ درباره ایران  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131820" target="_blank">📅 01:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131819">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h5maZQlqAOb50msf_1gfw5hF6K73IhX6rvKyogBSGwyrLajG-Ke-gtmGtZBelYOrExeQyMeHH2t3ogrdegwZTHvoR7cAc57JcEs7u5EPA0ye8iu__4NzT6kufAXql9OQ6Dq2NxbYaDV-yFmz0Ae--ltA69ovnNZ7nZaypVsgb9chl2g7tKYozNuv3y6s0ogKaOlzyTtSickioIebi2bx_XkX3A7Ne9dCNA3qqcoeJ6gJ7UKxYXfJdtq5xcdoK7mgrxLEtOseFtNlftjc1zyKpvq_QBSoLiPEHkfOEvlTKfDauNnIB7lFvqj_VBcUpW4A3D0riIJQC7UtGI_YwTydJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فوری
| پست جدید ترامپ درباره ایران
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/131819" target="_blank">📅 01:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131818">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
علیرضا بیرانوند: سرود جمهوری اسلامی رو با صدای بلند میخونم و مخالفا هم هیچ کاری نمیتونن بکنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131818" target="_blank">📅 01:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131813">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
یکی از گزینه‌های اصلی باشگاه ، برای گلر ذخیره جایگزین امیررضا رفیعی آرمین عباسی گلر جوان پیکان تهران است   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131813" target="_blank">📅 23:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131812">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFNPDo3s4WtT51H2TfhocsaIhuAKOQ_GMTMyC7zqwVufoRh-eA6z3vIvKkmlctB6JqQSWtoRcgogZasrFsaBsnERdWxuMpwW14RxrsTaBXWxgznMNLqOfKycuWVplYmQfPi-hatfabcpl6XXZqQ1yNHVOMMrI6OhFgRrVIbMPZyRS5Uknf6sa32Q-gtfqmVCnvcBisHdEzNCymh27ZaadNKnT9e9FsNUzldyualPehLKPhXJH2BH2m4z7wZ78Vd4FXBsGZkGcFuW-1kRI818HTfxiIv3xvMj6Vb6XVUEgsqMX4hS9QaDU6pyg9VhX5CZFY3-X8XjJFObl994MkNN3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
#شایعات
🗣
اوسمار خواهان بازگشت دانیال اسماعیلی فر و مهدی ترابی شد!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131812" target="_blank">📅 23:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131811">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
امیررضا رفیعی گلر دوم سرخپوشان پایتخت پس از چهار سال حضور در پرسپولیس از جمع این تیم جدا خواهد شد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131811" target="_blank">📅 23:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131810">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwXC88oz41YYSj-0pGYRBpkanhlQHgBP9u5bLtREr1ZwApjhFglyuRom7IyghmWOvft7er5Pu4cE_UpgS8thKGwxkdCe4ynwwDT5fakLw3Jv-ZiuTRBjpKaNOiTjYMMfXRUZlKmVvlIJAd1kIqgSt-j_3GSl9sGRTNn3NwFR1mChl7WqUJKhCG0nCnuqsUu3QKUrFRNS92r1rP9kKAwDZ2uanHT0yqgA8uH9c5PJyjuVJWg55oG-77l5IYwsIHUcbkOTGRV-Q_DRy44_4GOWG4DIgmfvhbekB57cOT34a9BPGmIehIP1wsntMjjTaUaz9SudeYR3G3N3TaiGl3AntQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مدیران باشگاه کیسه اول فصل رفتن دنبال جذب این بازیکن و براشم پیش قرارداد فرستادن با مهر و امضا رسمی ولی لحظه آخری از جذبش پشیمون شدن حالا طرف رفته از کیسه شکایت کرده و گفته غرامت 800 هزار دلاری میخوام :)
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131810" target="_blank">📅 23:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131808">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚩
🚩
🚩
🚩
#فووووری
✅
فرهیختگان خبرداد؛واسطه پیمان حدادی مدیرعامل باشگاه پرسپولیس در روز های گذشته جلساتی فشرده با مهدی تارتار سرمربی گل گهر داشته تا این مربی را جایگزین اوسمار ویه را در پرسپولیس کند!!!!   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131808" target="_blank">📅 22:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131807">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
رضا غندی پور پس از استوری علیه قلعه نویی از اردوی تیم ملی امید هم خط خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/131807" target="_blank">📅 22:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131806">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
مدیران باشگاه پرسپولیس روند تمدید قرارداد علی علیپور را به اوسمار ویه را واگذار کردند و در صورت رضایت این مربی قرارداد او را تمدید خواهند کرد/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131806" target="_blank">📅 22:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131805">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فرهیختگان: یه واسطه تارتار رو پیشنهاد کرده که اگه اوسمار رفت بشه سرمربی پرسپولیس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/131805" target="_blank">📅 22:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131804">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
🚨
دونالد ترامپ: ساعت برای رژیم ایران در حال تیک‌ تاک میباشد و بهتره است خیلی سریع شروع به حرکت کنند وگرنه هیچ چیزی از آنها باقی نخواهد ماند ، زمان یک عامل بسیار حیاتی و مهم است   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/131804" target="_blank">📅 22:21 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131803">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4KQFUgWUkZ_zWwkD5fktTpIQduJ8f67Kqp49geiGSosFFQtQ3E4vLhSUWJFsPY7FOUt6IFhsrQzqsErSaHCpYp6f2Oz0jvFwD9YnHf3kaZq6vQ9RvlckTC-eltb9s0fDloQJSXshuNr1Gj3-GvoUT4qPbUXc3LCqaSD8LQfdhphwVkZYAPFiQiawv8MKgBrV_BIZIr5mBXsapSFJcYAyiqS6qN6adbCtoWuDasalCudf0UZE-CTn5LoARIBj3zEZQixSAyDlNTpefbEJ8_5cHkmA78gOSGjorLiOvMIQCWX2xBdpl0KqyQV8EmtwKqx0vX9c6hw3sU1onl-fU7IuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
🚨
دونالد ترامپ: ساعت برای رژیم ایران در حال تیک‌ تاک میباشد و بهتره است خیلی سریع شروع به حرکت کنند وگرنه هیچ چیزی از آنها باقی نخواهد ماند ، زمان یک عامل بسیار حیاتی و مهم است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/131803" target="_blank">📅 22:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131801">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
ترامپ: ایران خواهان توافقه و منتظر پیشنهاد به‌روز شده‌شون هستم؛ پیشنهادی که امیدوارم بهتر از آخرین پیشنهادی باشه که چند روز پیش ارائه شده بود.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131801" target="_blank">📅 22:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131800">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
بر اساس گزارش منتشر شده از
CNN
سپاه به چند شرکت نظیر گوگل ، مایکروسافت و آمازون گفته باید بابت انتقال اینترنت از کف خلیج فارس عوارض پرداخت کنید وگرنه قطعش میکنم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131800" target="_blank">📅 22:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131799">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
فارس: محوز حرفه ای باشگاه پرسپولیس صادر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/131799" target="_blank">📅 21:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131796">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m55PKlk1qXUbzeI5DkhMcx-m4xB4G0cTsVie3uksuksq3Osbcb3DYNvnrjQesf_aslOvv0ZBoii_DQ7szdK5tZPT9uC9lcwJVYAqaWm6FbLkLQlkQbnZ0QDZWba-waPM2a9ouR7725eu76w6Kog2npoEevj9TxmGaI5hSNPmHR2WhezwJfZRItfrhN8-WeLlC_-UfPI2JsWjjfJlWkEjmHqOeRfNNaS7FttnS8P0HxFbfxsuYJeMW0vptdl5dWBROIOcpAQ80wlQpEae98vO04_DGu6ErqW1YMBKbIqw99fjBoQtqPsQHTXbbrPgugKsSTne3mYspAUxFJW0fqYgbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ از طریق Truth Social:
🔺
برای ایران، ساعت در حال تیک‌تاک است و بهتر است سریع حرکت کنند، وگرنه چیزی از آن‌ها باقی نخواهد ماند.
🔺
زمان اهمیت حیاتی دارد!
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131796" target="_blank">📅 20:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131794">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTKKrYNYob0u5QlrXxWkqzVrm9U0GYmexD4Ew9RqbGo4NvRWNqG_MalNCKj7LOcbdeNczQq7OcsJZX0sgzK7ykWFZxL3gYEhlj4dhBjyAnvJFfUIUTsdfMAwnB5WnPAuSMB5Zdc5PUFgH3uVsJ_qY7xdI9Mv3Q0XKGzQeSNMdb938thNPJ_R7QkAqho4z9pUlK3v9xAyd9Hhta4dFy2SQwUDWNmYbBuuVjNb4AtRzGEs5WdrxoVyI_X4uNgk-uPV7Ttq8NUjme9jkn0KhQLwZxbvSi_VGlbsgBWvj3QsPrJuJsVlNSTLzLiNFNB94rysxhZsp2HmcuXFq0ErfGU7Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سه سهمیه مستقیم لیگ نخبگان برای ایران
🔺
با شکست شب گذشته النصر در فینال لیگ قهرمانان آسیا 2، حالا فوتبال ایران برای دو فصل آینده به‌صورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود.
🔺
در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات دوم شد و ایران بالاتر از قطر، رتبه سوم غرب آسیا را حفظ کرد. بر اساس سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 969 · <a href="https://t.me/SorkhTimes/131794" target="_blank">📅 20:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131793">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W13pSr-ySSf4r-P3-KbafDyEry-S6ZYPCD9bA8E8sw2HWdqfIbKwO1Pgj5gI9JE8HsTTttu5PCMqAt2gdt7C2I6vbbGEPwQa7l2xscOchEkpTUdjWF66d_-xEwePmCPO1jI4CiC6Ml5a3YxbJT0shOqi16kyqsjcxvT6pMdYsgapjMGN9cD-YKQm9qh8yDl-OM9ExLup3jhg_8BrKsnHrj0WKDq7UkiUdfHdPs2Plxxt9L0gEgOK4ZrX4pdLGm61LfoVeEK60jggHeWndMTyCJszWRT0ZcM9Hu8GbMMmnk0o04AMlxUKEH_2vR8b6Pdq-3ssmLG_y-ZhNBCfKpBfLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
استوری باشگاه پرسپولیس به مناسبت روز ارتباطات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 881 · <a href="https://t.me/SorkhTimes/131793" target="_blank">📅 20:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131792">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
ورزش‌سه: علی پروین بخاطر افت فشار ناگهانی در بیمارستان تندیس جردن بستری شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 840 · <a href="https://t.me/SorkhTimes/131792" target="_blank">📅 20:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131791">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjyERdpCMk-DBlm1BfRQWZZ2MNgmoBVbICEAgNxalvPEVHfSQlfogeepRIDyeSL1DGvTq4PVpJ_oxOc1ICYKMTY4ByZGe9bEfTm-f0B7mopkvLmJKHqmDsWQaP8_gBInASicqIgsY5VHrGoDHCgWOkaDaCDj0bRXWpn3B4_oSrTIqTk_JUIFlgOxaGoXvwbynBhVfppdPTByQwlUlTl_zDIIiRaUVRBBwjYKhQADJ11da0-A4fV9f1WFp5ZxN1ywTPv7rBkyjyPwBCWF2zWWdREX4Zw2MjrQg7wDv8ZKrOZLEXmGUJUrE3cNeLcN43UFi_M-7XVkvZYrxpAcLK-2Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابل توجه کاربران محترم وینکوبت، تمام قابلیت‌های سایت یکجا در
ربات وینکوبت
در دسترس کاربران
قرار دارد.
📌
کافیست با استارت کردن ربات و زدن دکمه‌ی وبسایت، وارد سایت بشید و به‌راحتی ثبت‌نام و پیش‌بینی مسابقات ورزشی رو انجام بدید:
👇
🤖
-
@Wincobet_bot
🎰
از پیش‌بینی مسابقات ورزشی تا کازینو آنلاین، بدون نیاز به خروج از تلگرام با مینی‌اپ هوشمند وینکوبت بازی کن!
📌
در
وینکوبت
ثبت‌نام کن و با شارژ از طریق کریپتو ۵٪ شارژ بیشتری رو دریافت کنید، همین حالا شروع کن:
👇
🤖
-
@Wincobet_bot
📌
برای اطلاع از تحلیل بازی‌ها و ورود به کانال سایت جوین بدید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131791" target="_blank">📅 19:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131788">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky8a9QNe38lQc20jpoDNXUd4x_9LwV6ZM_NsTcMTKr5ipoq53OinGNs0LXzZAoCg2gfVdOCdyM92LkZxVmOoyKESq0oMgdJPWRTQ76cVGPQby8h4-kTOaVFsaDYsOFOLnivjXHB0okQmeyxDLzZu1fOjnHdFiJ9mmJT-883EerIfWX6tWSoBX59xVsyk9W_HiuJGEhy9MrwxZDN-HKm9hdD1LoPcynerPyHZquWo8Yg_U_TtOgDHAdivZ83vInm9FkWrhXiknD5yFG6vihdGlffMOL7eAfXkqxl-hPTzvaIYjDQHcN2gR2-DuNjrVAL3dQ6ZBUp6k1rDUXAYx4bdtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🚨
فووووووووووووری
🚨
مجوز حرفه ای باشگاه پرسپولیس تایید و توسط afc صادر شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 977 · <a href="https://t.me/SorkhTimes/131788" target="_blank">📅 18:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131787">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
اورونوف: با پرسپولیس قرارداد دارم و فصل آینده در این تیم خواهم ماند، میخواهم با پرسپولیس قهرمان لیگ و آسیا شوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 984 · <a href="https://t.me/SorkhTimes/131787" target="_blank">📅 18:34 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
