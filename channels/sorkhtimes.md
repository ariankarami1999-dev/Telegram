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
<img src="https://cdn4.telesco.pe/file/Vudf0qAZ4gUSTsbCjpCpF7eKWp9LfcqgjQTS7l5wOSM5QNnmP4mSMIWyWH3vrW43ijb93b8lxUTnkffcOhhmSuJASK1PRRC1syAVDwYenII-yVEY2lJ6JXp7hQrNBndbLwgDu9_o4T2yLK1rOy5fTCsss8MTgcCvXULT-40MnkXh3sEbnZPQdxFu17AaCN_JmLv1erLpgdqvX2VxZPovFaqX89su2MIqcq_dAs3R2ED9QjtgTWlTNUoqKxGFKnrVGCIpOJk_YbsBlL3us6KQW__dpyhAaAVYUXryG4N0bNwnEB_gnzUb0_Qlrzxd-G4fhR0UtRXBbM8tOpOkVp-MJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 18:43:11</div>
<hr>

<div class="tg-post" id="msg-138820">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
فوری؛ بیانیه کمیته انضباطی علیه استقلال تراکتور و گلگهر: ندادن بازیکن به تیم ملی در هر رده سنی به هر دلیلی تخلف حساب میشه و حضور بازیکنان حاضر در لیست در اردو ملزمه و هر تیمی سرپیچی کنه باهاش به شدت برخورد میشه و بازیکنان از حضور در لیگ برتر محروم میشن و…</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/138820" target="_blank">📅 18:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138819">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
❌
استقلال، تراکتور و پرسپولیس اعلام کردن قرار نیست بازیکن به تیم امید بدن! با این حساب ۱۰ ۱۲ تا بازیکن از این لیست خط میخوره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/138819" target="_blank">📅 18:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138818">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🤥
🤥
#شنیده ها
👀
مهدی تارتار قصد دارد در دیدار مقابل تراکتور از سیستم 3 دفاعه برای مهار شهریار مغانلو و حسین زاده استفاده کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/138818" target="_blank">📅 16:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138817">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
همه شواهد و مدارک حاکی از سرباز شدن علیرضا صفربیرانوند پس از بازی با پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/138817" target="_blank">📅 16:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138816">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
پرسپولیس تا پایان نقل و انتقالات ۲ بازیکن دیگه جذب میکنه/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/138816" target="_blank">📅 16:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138815">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_xLmgR4h845oydL3Vu_fknOD4ITyEW7N_vSbjpjG1bkyJW8mwKvHRQqenWVoh7cmCIkY4WJ6h-RPwADI9a4gp4bTBLBpIpCDeQRrshCBUuJOaIndt8xUJilfnClTOrxnoFbhkl7_LkeCTZwmIkaD7I5hoFr_Z8Ji9xbZwz40VA_3KRSrzxem1YTPO0a9m8y4Pu4AD2ciWnsrRBnd0sF00FBLfAA6xcb_g1elzNMysoo24yTagUbrBaUA6YxanqTSGfGf6rOV4Pbd7QyVAMDYqT3QKCeoQPBPsiv1UhXmIZ64RiH0Cm3DPI7TJDJ4dBbOz_raNtQclUkNKCdrGjX0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
همه شواهد و مدارک حاکی از سرباز شدن علیرضا صفربیرانوند پس از بازی با پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/138815" target="_blank">📅 14:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138814">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
مدیریت پرسپولیس در تلاشه تا ۷۲ ساعت آینده قربانی و امیر جعفری رو جذب کنه
🔴
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/138814" target="_blank">📅 14:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138813">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
✔️
خبر سرباز بودن بیرو به هیئت فوتبال آذربایجان شرقی ابلاغ شد
👍
بر اساس آخرین استعلام هیئت فوتبال آذربایجان شرقی از سازمان نظام وظیفه، معافیت تحصیلی علیرضا بیرانوند تا اول مهرماه ۱۴۰۵ اعتبار دارد، اما طبق مقررات فعلی، او تا پایان نقل‌وانتقالات (چهارم شهریور)…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/138813" target="_blank">📅 14:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138812">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
❌
فووووووووری
🚨
محمد عمری به دلیل کشیدگی از ناحیه آرنج دیدار برابر تراکتور را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/138812" target="_blank">📅 14:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138811">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlcmGbQ0mQbzymOACX8pPDttkYKPm_GhKj2M_qoYZu3QxgwdCubZId3q-3kSMi6PKmhTr_cW5m_-nZMmcrfolpntWER1c4OFcd8og_0AnWUA98iw7SxQDrWyzDX5a2twb-Oclnf5lcHqSdSRMVq0eEtji0oLKK0drWZBtXNWYqaXDGZ6n2zHb4xwM19SBLpI26yM27zkB7CG-oK1eGmPCZGlkD0rxI4kt4246oyFn-JRku-Y44Q8x9fFRTPoZoa8nYP9JxHo7qhNRJNcMQwDsp9iKN5-eDMPoXDeMpe5xALEBoqmI0pl4UxN2Zxq7wvu5T6KQG2TslFrsV5FoxuIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبرد مدعیان در شهر قدس!
استقلالِ آماده مقابل سپاهانِ مدعی؛ یک بازی حساس که می‌تونه معادلات بالای جدول رو از همین هفته تغییر بده!
[
استقلال
⚽
🆚
⚽
سپاهان
]
🔵
بونوس ویژه بازی Scarab Temple در اسپورت‌نود، کاربران می‌توانند با هربار شارژ حداقل ۱ میلیون تومان، متناسب با مبلغ شارژ خود اسپین رایگان کازینو دریافت کنند.
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
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/138811" target="_blank">📅 14:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138810">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🟧
🟧
اطلاعیه‌سازمان‌نظام‌وظیفه: بازیکنانی که مشمول خدمت سربازی هستند تنها میتونن در دو تیم لیگ‌برتری‌فجرسپاسی و ملوان بازی کنند و امکان گذروندن خدمت سربازی در تیم نظامی وجود نداره. علیرضا بیرانوند هم اگه معافیتش رو به هر شکلی تمدید نکنه تنها تا 4 شهریور فرصت…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/138810" target="_blank">📅 13:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138809">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
❌
فووووووووری
🚨
محمد عمری به دلیل کشیدگی از ناحیه آرنج دیدار برابر تراکتور را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/138809" target="_blank">📅 13:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138808">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
✔️
مدیریت پرسپولیس در تلاشه تا ۷۲ ساعت آینده قربانی و امیر جعفری رو جذب کنه
🔴
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/138808" target="_blank">📅 13:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138807">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
پرسپولیس همچنان در به در دنبال مدافع چپ ..این معضل ادامه داره.. کسی برای جذب نیست ...رایزنی ها ادامه داره ///قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/138807" target="_blank">📅 13:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138806">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/138806" target="_blank">📅 13:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138805">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/138805" target="_blank">📅 13:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138804">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
باشگاه الوحده امارات جواب آخرین نامه پرسپولیس رو هم نداد و به نظر میرسه قربانی در الوحده موندنی شده / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/138804" target="_blank">📅 11:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138803">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
الوحده با 3 بازیکن تهاجمی به توافق رسیده و تا زمانی که لیستش و خالی نکنه امکان عقد قرارداد جدید نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/138803" target="_blank">📅 11:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138802">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
🇮🇷
عکس یادگاری یحیی گل‌محمدی و علیرضا منصوریان در حاشیه دیدار دوستانه دهوک و الطلبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/138802" target="_blank">📅 11:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138801">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
خبرنگار اسپورت امارات: قطعی شد محمد قربانی از الوحده جدا خواهد شد و به ایران باز میگردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/138801" target="_blank">📅 11:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138800">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUPOHUBpEjIM8XSlIHDuss0JFgA-OzZs2J5AgtThFaXxS9j2NukX9geKBGhzge2j9Db5x3vlMuff1th-05_ke9fwAY_VuZfMXOtigKjkmlwMlFSO8smM3bkEVSaR6rXUgSyzY9S8tAEVd3yjupMqgivC5PmWeN7F7AvPgECWWDzEGJkns7sUEqeYKD2yontFG7ayXxQxne9ASOmfgGOUiLbXiTotHZPGHOON0z3tLBwORSlavpfw137cKaxmuiKbfeohLOuRxzF9Q1ajCzOiv5qdvLt31eXxrdZdOD8byxE0jmXNIlYiTUZwytL8-8GVwSZWZXVan8k16Bl9d3LeWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ایجنت دنیل گرا:
✔️
«دنیل به قراردادش با پرسپولیس پایبند است و بعد از پشت سر گذاشتن مصدومیت، با تمام توان برمی‌گردد.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/138800" target="_blank">📅 09:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138799">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
🚨
العازی‌ خبرنگار اسپورت‌ امارات:
👀
🇮🇷
محمد قربانی دراین پنجره‌ از تیم‌الوحده‌امارات جدا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/138799" target="_blank">📅 09:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138798">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
🚨
العازی‌ خبرنگار اسپورت‌ امارات:
👀
🇮🇷
محمد قربانی دراین پنجره‌ از تیم‌الوحده‌امارات جدا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/138798" target="_blank">📅 09:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138797">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rxb8QtoRC1-xnrlHnT5X8ujRpFiErA0MZ3R6l0CizPP4-Z4ErYts9PCFinDdq6TE5XupETu8f0psDBkyMgU23tMAwbNybE2FOA8K0CNP8HIfMfUjd_Dx-gS9KcfPIlXWrpq9xYGi2QtZK1SPHq0guiOEQx8g_Cp_aqRBu9dFZIrpc9ql7f6m7dN8pmuRMAUZdBajPw_Kka2hVMrgFaShlxx525HoHqckm_imrKHYLl3Z-QZLnpkb5lmElBnsypL0RE6FQGslW31d_Zcnt6BnCV9NTY6h3HuvB_A_fBpzxMivf896-M8zYXdB0AxtrfQiidD4-PS4NZAC5USV6XvXTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/138797" target="_blank">📅 09:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138796">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyQgZGovzcfXgiTGd_LOjF3p-ylesftsDLtcB08G-06ASt0TPL0uDx7kFM4SJ5bjvSKNuhDkYY3jFHHifugUynH83QjaTmB_nEpX6doQUGHY4V8IGFDcKd_sZN3XneQzd3JVkxJvG0CoPJEkQ9ej2XvHREZaFs6QLHAwxmOs56fgtmZ0WLSOhN-YwmMXljrPTr1u3ZkdgXpU8zD0NZpyt5d48a5TP06H4p1VcaBcIB3MGfHz1ZtrIh61Rmvih3Cygo5vav2s-hAh0sUahquZCelPZgIExzfsCD6Icve834UWQvA9gks38rtGTEnlSiZPBbM_C0TEkcTHGrXaappD1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بونوس ویژه بازی Scarab Temple
🔵
کاربران می‌توانند با هر واریز واجد شرایط، متناسب با مبلغ واریزی خود برای بازی Scarab Temple چرخش رایگان دریافت کنند.
در عکس فوق شرایط دریافت چرخش این بونوس ویژه توضیح داده شده! هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
📌
نسخه جدید سایت:
Sportn5b2.com
📌
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/138796" target="_blank">📅 01:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138795">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⚽
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/138795" target="_blank">📅 01:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138794">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
پرسپولیسی‌های تراکتور:
🗣
علیرضا بیرانوند - شجاع خلیل‌زاده - فرشاد فرجی - دانیال اسماعیلی‌فر - مهدی شیری -صادق محرمی - محمد نادری - مهدی ترابی -شهریار مغانلو
🗣
تراکتوری‌های پرسپولیس:
✔️
مهدی تیکدری - پویا پورعلی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/138794" target="_blank">📅 00:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138793">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
❌
لیست تیم ملی امید برای شرکت در مسابقات آسیایی ناگویا اعلام شد
🗣
🗣
دانیال ایری، پوریا لطیفی فر و پوریا شهرآبادی از پرسپولیس به تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/138793" target="_blank">📅 00:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138792">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⚽
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/138792" target="_blank">📅 00:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138791">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
✅
✅
فقط تا چهارشنبه پنجره نقل و انتقالاتی بازه و تکلیف قربانی باید معلوم بشه.بعد از چهارشنبه دیگه فقط میشه بازیکن آزاد گرفت   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/138791" target="_blank">📅 23:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138790">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
انقلاب در الوحده پس از دو شکست!
🔴
مدیران باشگاه الوحده پس از دو شکست پیاپی در شروع لیگ دست به اقدام تاریخی زدن و در یک روز با سه بازیکن خارجی سطح بالا توافق کردن و به زودی از اونها رونمایی میکنن
🔴
با توجه به جذب این سه بازیکن به زودی دو بازیکن خارجی از…</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/138790" target="_blank">📅 22:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138789">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
علی قلی‌زاده: امیدوارم سال آینده در پرسپولیس باشم!
💬
فصل گذشته تمام کارهای انتقال من به پرسپولیس انجام شده بود اما ناگهان ورق برگشت/ باشگاه لخ‌پوزنان امروز یک‌رقم می‌خواست و فردا رقم رضایت‌نامه را افزایش می‌داد/ به هرحال این ماجراها بین باشگاه‌ها طبیعی است/…</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/138789" target="_blank">📅 22:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138788">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
انقلاب در الوحده پس از دو شکست!
🔴
مدیران باشگاه الوحده پس از دو شکست پیاپی در شروع لیگ دست به اقدام تاریخی زدن و در یک روز با سه بازیکن خارجی سطح بالا توافق کردن و به زودی از اونها رونمایی میکنن
🔴
با توجه به جذب این سه بازیکن به زودی دو بازیکن خارجی از…</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/138788" target="_blank">📅 22:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138787">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1145503d.mp4?token=N4RLBirDm3gvWujCMnmZGaAmOetD5Y78nhu9MAzNcPKvmVlgkLULemSNIAaE7NZrg4RUJZKztl3caCtGhAmyBr8MkB37tuPzSiu97Zr0YjyTln6ROGImVS8egUoQ0--fsb-Sh3_tQqxtpXXwgpUbWdSO2xe_ybV0kjmXKdBJBT0qybyMjxtrRViXJAEQPTKcJ0u2A1sIs1ohXH87dHIjrn30uA2CP3zN5V8uPe2vmURPx0iTNDPaEqFplRhMy-EtPkxj4AF7ohd9GMz1iY8jNDe3rOHt4DZ1Y3t57kwCONMbVmt0ArVweCNYZAy-EG90mUWQbEzXjbswnpa1gbLwKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1145503d.mp4?token=N4RLBirDm3gvWujCMnmZGaAmOetD5Y78nhu9MAzNcPKvmVlgkLULemSNIAaE7NZrg4RUJZKztl3caCtGhAmyBr8MkB37tuPzSiu97Zr0YjyTln6ROGImVS8egUoQ0--fsb-Sh3_tQqxtpXXwgpUbWdSO2xe_ybV0kjmXKdBJBT0qybyMjxtrRViXJAEQPTKcJ0u2A1sIs1ohXH87dHIjrn30uA2CP3zN5V8uPe2vmURPx0iTNDPaEqFplRhMy-EtPkxj4AF7ohd9GMz1iY8jNDe3rOHt4DZ1Y3t57kwCONMbVmt0ArVweCNYZAy-EG90mUWQbEzXjbswnpa1gbLwKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
علی قلی‌زاده: امیدوارم سال آینده در پرسپولیس باشم!
💬
فصل گذشته تمام کارهای انتقال من به پرسپولیس انجام شده بود اما ناگهان ورق برگشت/ باشگاه لخ‌پوزنان امروز یک‌رقم می‌خواست و فردا رقم رضایت‌نامه را افزایش می‌داد/ به هرحال این ماجراها بین باشگاه‌ها طبیعی است/ امیدوارم سال آینده در پرسپولیس حضور داشته باشم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/138787" target="_blank">📅 22:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138786">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❗️
❗️
قلی زاده: فکر نمیکنم تو ایران برای تیمی جز پرسپولیس بازی کنم ؛ چون قلبا پرسپولیسیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/138786" target="_blank">📅 22:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138785">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2zRBBkR34gM3GZMqqlZs9ERHfMbkOiO4_HAEvu3nh1ej1ORQXOgzj30sWoIizWia6wQCmogge2XmZji0emDCQXPEDQDgleG2whPHIKrtrD_s8ro0bsrgaKK-XvyJVltvSO_-NyyCiePYoR_N5ndPU12C0uCAP0kESE5up8EWSVjLATFtLPPThLXsftGFWlarvPP8yZ-h1YG1PiYGfm5T6r_j4ckXp5-b9Nh9k0rRWKDZdtU8dI4pZAuOWY-FBSgNTFkMdyApJMaGjCRAiosdFZrkTsBYRdstAO-sLamvpK7h3LjhCUMtn9hoekFDwputXnBhsUF1s6tS_aRkn1dkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بازگشت آقای خاص؛ شروع دوباره کهکشانی‌ها!
🔥
- رئال مادرید در اولین آزمون فصل، مهمان اسپانیول؛ آیا مورینیو با ۳ امتیاز برمی‌گردد؟
[
اسپانیول
⚽️
🆚
⚽️
رئال‌مادرید
]
🎁
بونوس ویژه بازی Scarab Temple در اسپورت‌نود، کاربران می‌توانند با هربار شارژ حداقل ۱ میلیون تومان، متناسب با مبلغ شارژ خود اسپین رایگان کازینو دریافت کنند.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🌐
نسخه جدید سایت:
Sportn5b2.com
🌐
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/138785" target="_blank">📅 22:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138784">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">💢
💢
🚨
مدیران باشگاه الوحده امارات پس از شکست در دیدار امروزشان به دنبال جذب دو بازیکن خارجی جدید هستند و از همین روز از نماینده محمد قربانی دعوت کرده اند فردا برای جدایی و فروش این بازیکن به باشگاه برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/138784" target="_blank">📅 21:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138783">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/138783" target="_blank">📅 21:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138782">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
✔️
رسمی شد؛ مهدی طارمی به الوصل امارات، حریف استقلال‌ و تراکتور در لیگ نخبگان آسیا پیوست.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/138782" target="_blank">📅 21:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138781">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHcR0vgylglAXMWOIkMS_NSaaCdrYPWEN0PyBTOI4q47v0WN19auMoCwKkg0yPz_P28eHzZaIrboV3n3xnw1lhXYYxAcFDnSjV_z2RS4aehiCiHoeSzK2qucln8jhzUNjw-wPH6XP_RUtplOx9NRmwXe26BWPeJdm-Mo6lD-BWV8JO55InRK-3TpGK_fggpoRwO2P-821kqhvi2YgwkWVT-5DFC71w74TOch-B0lef7fI9YcUCHpd1aTJrOcTt1F4xJIgJrYPZSQ9Kz5fU_9n7HYYmvs-PVWbS9wA9NbKkL51bcBH30SipGoQfeEkz7igbFMMiInFAH9AkHLwcvs3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/138781" target="_blank">📅 21:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138780">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyqO9AoLKPkgNlHRip9aDPsu8UuJpT9RPukGFDU2J5hfVZqDaEHfCLbzZ4Z_gAEOeibkO0HfEeFtmI2-0l8T4D4xjyvOSXTxXDd7_Ws7N0kFTInjBKCfD80i9GowT3APApj4PRWELL4rkPtFlhhjfvAR3WoR293Pawnzh_LPf2gOD0FdCJEJ2UWjLb2A1WLmx1whkLKx4-bs3-DPndSxxm-KUFoh9GSBIe3ZvwlrO6IAqSsUNx_vQm_DKc78e1ondHhH41CKw8_wgEyv8P1J1XypAlC7XdZZnMTovtPoCYeMP4f8pcpBeCT90CcYMFP_gnjIzXYUCOuDagSdje1qXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🔹
سمیه آوج، الهه افشاردوست، سمیه اسماعیلی و کیمیا عباس‌زاده با امضای قراردادهای خود به تیم بانوان باشگاه پرسپولیس پیوستند.
🗣
✍️
همچنین قرارداد الهام عبدالرحمانی نیز برای دو فصل دیگر تمدید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
‌</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/138780" target="_blank">📅 20:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138779">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
❌
لیست تیم ملی امید برای شرکت در مسابقات آسیایی ناگویا اعلام شد
🗣
🗣
دانیال ایری، پوریا لطیفی فر و پوریا شهرآبادی از پرسپولیس به تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/138779" target="_blank">📅 19:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138778">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
❌
لیست تیم ملی امید برای شرکت در مسابقات آسیایی ناگویا اعلام شد
🗣
🗣
دانیال ایری، پوریا لطیفی فر و پوریا شهرآبادی از پرسپولیس به تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/138778" target="_blank">📅 18:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138777">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dk93kMKNHeAmIjN7yppHy3wk6QC-_k68hdAvzKBnVQLOkpJ1H8q9WMfPgqvFf2nm98PNMVOsSQJLewBYfyvhlu51EYKgAOSpDCMH3njdO5aRJNeXCNofl06yzhP6XZ0t6NhRGtRe9k8uEXEvhedQfgbyhAdcOQQtmFyIB40SVfMfYlTyBVhyFzZx1Jjlc6dLQ_os5dqxkJ1KeoNdlZGsGHNffNvZ_Q2JyMAJ8Rv5eEqw-VaJSafQHS05Ej_V-P5xXvJO-rucah1nJskfRdXqNkjayz-x5nxO-plgr86pizdDGpkHvRNMs2IKRsd7919C2WgBck2W_MsilqMNAoZqTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هواداران ملوان در واکنش به سرباز شدن علیرضا بیرانوند، کمپین نه به بیرانوند را راه انداختند!
👍
👍
👍
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/138777" target="_blank">📅 18:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138776">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔄
🔄
بازی با پرسپولیس آخرین حضور بیرانوند در تراکتور؛ بیرو در راه فجرسپاسی!
✔️
✔️
علیرضا بیرانوند به گفته مسئولان نظام وظیفه باید از اول مهرماه راهی خدمت سربازی شود. این در حالی است که بیرانوند اکنون در تراکتور حضور دارد و نقل‌و‌انتقالات تابستانی فوتبال ایران…</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/138776" target="_blank">📅 18:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138775">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
امیر عرب‌باقری داور دیدار تراکتور و پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/138775" target="_blank">📅 18:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138774">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
✅
✅
فووووووووووووری
🚨
انتقال امیر جعفری به پرسپولیس کنسل شد و گل گهر مخالفت کرد  / ورزش سه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/138774" target="_blank">📅 15:47 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138773">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⚽️
⚽️
⚽️
⚽️
از بین ابرقویی، تیکدری یا عیدی یکی دفاع چپ پرسپولیس مقابل تراکتور خواهد بود/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/138773" target="_blank">📅 15:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138772">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
فوووووووری / فارس :
❌
جدایی رزاق پور از فولاد منتفی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/138772" target="_blank">📅 15:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138771">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✔️
✔️
✔️
رسمی شد؛ مهدی طارمی به الوصل امارات، حریف استقلال‌ و تراکتور در لیگ نخبگان آسیا پیوست.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/138771" target="_blank">📅 15:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138770">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
رسانه‌های‌یونانی: باشگاه‌‌الوصل امارات 1.5 میلیون‌دلار بابت رضایت‌نامه مهدی‌طارمی به باشگاه المپیاکوس یونان پرداخت خواهد کرد. با خودِ مهدی طارمی هم 6.5 میلیون‌یورو بسته‌اند برای دوفصل!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/138770" target="_blank">📅 15:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138769">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
علیرضا بیرانوند هیچ راه فراری برای نرفتن به سربازی نداره و قطعا مهر ماه سرباز میشه
😂
/ تسنیم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/138769" target="_blank">📅 15:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138768">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🟧
🟧
اطلاعیه‌سازمان‌نظام‌وظیفه: بازیکنانی که مشمول خدمت سربازی هستند تنها میتونن در دو تیم لیگ‌برتری‌فجرسپاسی و ملوان بازی کنند و امکان گذروندن خدمت سربازی در تیم نظامی وجود نداره. علیرضا بیرانوند هم اگه معافیتش رو به هر شکلی تمدید نکنه تنها تا 4 شهریور فرصت…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/138768" target="_blank">📅 14:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138767">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGhCmDReKJmL_rRP7W-OW_Bpz1YNSO7hBjt9TNHyh2qIZYuGwvgU_5tTScTPMJC5n_pEmCbEU8Eidsze7VKekrmNvsDlvG5p4kSvHBR5wmEROmmBqnkVpOfP5wIRbyD2fMGLa-cYExOL8frtidPGmX-m-ArANi8PE_I7-oXgWzC97RZ7lv0TmASiDGPudNDxEnCJQEK3M_z2HigWeytyo8uGLuIu4zLjSSeTOsCcbKfxXsxy6Y12LH5JjSVHwV8p01N9E652giGHY4kaVZknPNv9tIF0y1fU2MhIwX8uI7Tukf74HzFWBrjYpNKniFc-rSeZODF3vSFUwT8sKz8WbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟧
🟧
اطلاعیه‌سازمان‌نظام‌وظیفه: بازیکنانی که مشمول خدمت سربازی هستند تنها میتونن در دو تیم لیگ‌برتری‌فجرسپاسی و ملوان بازی کنند و امکان گذروندن خدمت سربازی در تیم نظامی وجود نداره. علیرضا بیرانوند هم اگه معافیتش رو به هر شکلی تمدید نکنه تنها تا 4 شهریور فرصت داره راهی ملوان با فجر بشه چون پنجره بسته بشه دیگ نمیشه.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/138767" target="_blank">📅 14:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138766">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
❌
فووووووووری
🚨
محمد عمری به دلیل کشیدگی از ناحیه آرنج دیدار برابر تراکتور را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/138766" target="_blank">📅 13:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138765">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
حضور پرسپولیس در مرکز پزشکی و فیزیوتراپی فدراسیون کشتی
✔️
بازیکنان تیم فوتبال پرسپولیس پس از دیدار برابر استقلال خوزستان، با حضور در مرکز پزشکی ورزشی و فیزیوتراپی کمپ تیم‌های ملی کشتی، به ریکاوری پرداختند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/138765" target="_blank">📅 13:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138764">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔻
🔻
🔻
میثاقی: احتمال داره حسین زاده و بیرانوند به همراه تیم ملی امید راهی بازیای ناگویا شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/138764" target="_blank">📅 13:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138763">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
بخش رسانه‌ای تیم ملی: مسدود شدن سایت و برنامه فوتبال 360 عادل فردوسی پور هیچ ارتباطی به سرمربی تیم ملی ندارد و ایشان نه شکایتی کرده نه هیچ عملی انجام داده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/138763" target="_blank">📅 12:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138762">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
قدوسی: علیرضا بیرانوند گفته نه تنها سربازی نمیرم بلکه نیم فصل با استقلال برای فصل آینده قرارداد میبندم
😀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/138762" target="_blank">📅 12:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138761">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hu0fHOtR0LkM5gG7ZV_PZHeR4TgXRKEiwa_hcCT6z7CCNj9QVCdlAEfYsrmGUCn3lTTCflUqePee1KH4DsyRfT0L8OnTlNf-dz12D35iN-XO-9Q7DbwBYk1oLJW_bOIZX1hNrlAvO1bfjbdGbTa0KVjl0peY6ETFZbmoVZ9_0J9EacnbWD7KXQ9fEuOXxgrTISiKQ-j9MhJU66_URbVZJhYFpseAJkIrc1akwfmHAwN1k4814oJ8NJtMfYgyNILWPDpleU8at7BzMzPEL2Jkvyw8KQv6ZFh7hBY7LEB5a92rQXEAM2mN68r7mdw_jWYO4yPPUb5eSsA400W00elV_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نبرد غول‌ها برای اولین جام فصل!
دورتموند در خانه مقابل بایرن؛
- امشب کدام تیم جام را بالای سر می‌برد؟
وقتشه پیش‌بینی‌تو ثبت کنی!
⚽️
فینال سوپرکاپ آلمان
[
دورتموند
⚽️
🆚
⚽️
بایرن‌مونیخ
]
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🌐
نسخه جدید سایت:
Sportn5b2.com
🌐
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/138761" target="_blank">📅 12:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138760">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e244643a2.mp4?token=RpsqEnZziy7ENehipevR6RsSZZOG4izSkkBOhRMJrxaGXzxTeXHkp8kYUYbmyT992bcs7w_3skwQ99s356cyn4xLb7WAtGGhrF2u7ELuOjsjaMQ4gfsPwHsa7l5SGZ42GaDhh-Rh1YLkQiNka27fx-xSeMcvQsMsoctOz_yNQVHXqacug-VAgPeXFo7pGKJ-bT23JdTnRNm7BX4zZzJvlA6Z9irPPuOnySl3N_oqE6ALujSbKV5xawySI14TWF0AYjETtfigdDAQw7QCJZDuI2mb7AzrhsHcXWUxU2mAqRqBvPWL-lFs7thgdSfl7o1HckawcE1e5Jr-gjkmYUzc1BPXAVFDEgq54VoJJvQGXqFc2MPRFqC3S5FaEraQl9xSzvpENlUhfiGvdFysmTI9ix3qpSKQ-KxLtK8bctH75qYrewmv7Xzj0A90cUFK3DKa5qizYTi8Mr1eUxziGo-VryeKfmX73-d4ehTEV22P16uOliEhgIA7KgTqv6KHok5jiJtPgp7yCZ7nywuA57NwqsA406ESAk-TKu0FBswFygmX_6SfAj8YkZQTGRUcnfXy60k-YSQ6UUgXtMym_nSyoc5YKjxRWJITUv19z2si1_H6_BZ1A8Rak0QCeOJpEc1Tr4-GyFXQZs5pWW01-l95zDl0zP_rtuJxgUPJOfKYF28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e244643a2.mp4?token=RpsqEnZziy7ENehipevR6RsSZZOG4izSkkBOhRMJrxaGXzxTeXHkp8kYUYbmyT992bcs7w_3skwQ99s356cyn4xLb7WAtGGhrF2u7ELuOjsjaMQ4gfsPwHsa7l5SGZ42GaDhh-Rh1YLkQiNka27fx-xSeMcvQsMsoctOz_yNQVHXqacug-VAgPeXFo7pGKJ-bT23JdTnRNm7BX4zZzJvlA6Z9irPPuOnySl3N_oqE6ALujSbKV5xawySI14TWF0AYjETtfigdDAQw7QCJZDuI2mb7AzrhsHcXWUxU2mAqRqBvPWL-lFs7thgdSfl7o1HckawcE1e5Jr-gjkmYUzc1BPXAVFDEgq54VoJJvQGXqFc2MPRFqC3S5FaEraQl9xSzvpENlUhfiGvdFysmTI9ix3qpSKQ-KxLtK8bctH75qYrewmv7Xzj0A90cUFK3DKa5qizYTi8Mr1eUxziGo-VryeKfmX73-d4ehTEV22P16uOliEhgIA7KgTqv6KHok5jiJtPgp7yCZ7nywuA57NwqsA406ESAk-TKu0FBswFygmX_6SfAj8YkZQTGRUcnfXy60k-YSQ6UUgXtMym_nSyoc5YKjxRWJITUv19z2si1_H6_BZ1A8Rak0QCeOJpEc1Tr4-GyFXQZs5pWW01-l95zDl0zP_rtuJxgUPJOfKYF28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
حضور پرسپولیس در مرکز پزشکی و فیزیوتراپی فدراسیون کشتی
✔️
بازیکنان تیم فوتبال پرسپولیس پس از دیدار برابر استقلال خوزستان، با حضور در مرکز پزشکی ورزشی و فیزیوتراپی کمپ تیم‌های ملی کشتی، به ریکاوری پرداختند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/138760" target="_blank">📅 11:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138759">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
در صورتی که انتقال ابوالفضل رزاق پور به پرسپولیس کنسل بشه، امیر جعفری گزینه بعدی دفاع چپ خواهد بود / تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/138759" target="_blank">📅 11:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138758">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">💢
💢
🚨
مدیران باشگاه الوحده امارات پس از شکست در دیدار امروزشان به دنبال جذب دو بازیکن خارجی جدید هستند و از همین روز از نماینده محمد قربانی دعوت کرده اند فردا برای جدایی و فروش این بازیکن به باشگاه برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/138758" target="_blank">📅 11:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138757">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
❌
آب پاکی فدراسیون فوتبال روی دست تراکتور، پرسپولیس- تراکتور، بدون تماشاگر
✅
✅
عضو کمیته استیناف فدراسیون فوتبال: کمیته استیناف به‌عنوان مرجع نهایی صدور رأی در ارکان قضایی فدراسیون، حکم کمیته انضباطی مبنی بر برگزاری دیدار تراکتور و پرسپولیس بدون حضور هواداران…</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/138757" target="_blank">📅 11:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138756">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
شایعات : تارتار میخواد مقابل تراکتور یه ترکیب سر و پا هجومی بفرسته تو زمین  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/138756" target="_blank">📅 09:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138755">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
حسن اکرمی داور بازی پرسپولیس و استقلال خوزستان شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/138755" target="_blank">📅 09:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138754">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0Zre_gpwuEhWaUmglSgjMcXGtRE-gm8VdD62z33AEWu2mX4gWUd0JdgmAwWxhoQLbQBZK7TO_yr7jCgiyKApU_rYrJzusHGonCOD6QtmMB2_BUZus9Xv0sYp4If-CMqtdLp6HKRPchARj6xYtt46-tl3-ObYJD5wHfAXDbT75fr7dXw3h0udAMn_iNZqOTdJDv1J681BsbM2c5Cn2ufqe2oeskZxG9qrEo8W5CeRreRTKk1rVTEbYmOW9tH65VXSG9XtEVIU5M0JeWcqbYOxpJtGokLPeQsxcjbb2CeobhBEJMSFiR4DFbqxzuA2mRJubtPHqDlBLPChFKuUZnejQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبح بخیر ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/138754" target="_blank">📅 09:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138753">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">7️⃣
وقت چرخشه! | SCARABTEMPLE
🎰
همین حالا با هر بار شارژ حداقل
۱ میلیون تومان، اسپین رایگان متناسب با مبلغ شارژ
دریافت کن!
💰
شارژ بیشتر؟ اسپین بیشتر!
🎁
هر چرخش، شانس دریافت جوایز نقدی
⚡️
اسپین‌های بیشتر، فرصت‌های بیشتر برای کشف جوایز بازی
😳
👾
اسکرب‌تمپل
، با یک سیستم اسپین پرهیجان و جوایز متنوع:
👇
🔵
نسخه جدید سایت:
Sportn5b2.com
🔵
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/138753" target="_blank">📅 01:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138752">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❤️
❤️
❤️
سهیمه خرید لیگ برتری پرسپولیس در نقل و انتقالات
⏺
1_مهدی تیکدری نژاد
⏺
2_سید مجید عیدی
⏺
3_محمد مهدی زارع
⏺
4_سید ابوالفضل جلالی
⏺
5_پویا پورعلی
⏺
6_محمد مهدی محبی
⏺
7_دانیال ایری
⏺
8_ خالی...
🌏
سهیمه بازیکنان آزاد فیفا:
⏺
1_خالی…
⏺
2_خالی…
⏺
3_خالی……</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/138752" target="_blank">📅 00:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138751">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‼️
‼️
فووووووووووووری
🚨
ورزش سه: سردار زاهدی بار دیگر در ارتباط با ما اعلام کرد علیرضا بیرانوند سرباز شده و از مهر ماه ( یکماه دیگر ) باید به خدمت مقدس سربازی اعزام شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/138751" target="_blank">📅 00:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138750">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
❌
ورزش‌سه:
🔴
الوحده به خاطرات تغییراتی که باید تو لیستش بده تمایل جدی به فروش قربانی داره و بعد باخت امشبش این اتفاق قطعی شده
💣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/138750" target="_blank">📅 00:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138749">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
✔️
ترامپ درباره ایران:
🔻
به نظرم این جنگ به‌زودی پایان خواهد یافت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/138749" target="_blank">📅 00:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138748">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
در صورتی که انتقال ابوالفضل رزاق پور به پرسپولیس کنسل بشه، امیر جعفری گزینه بعدی دفاع چپ خواهد بود / تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/138748" target="_blank">📅 00:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138747">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
یکی از سایت های اماراتی گفته قربانی با قراردادی ۱.۱ میلیون دلاری و سه ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/SorkhTimes/138747" target="_blank">📅 00:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138746">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22323c2ffc.mp4?token=iEtD76CTXnqZ9X0gOd8nrNLWCz_jM8k0Q-msDiKkss4Ff7rba02p3AaCk6gdMAa031hc256GRTSPXb6fGUd6BG4uO4UKPYvssihaOXXfsTOcrVl2btu1tThDu5rhH3ZhlnKeqF_FC0UvcD4DmchnRDMyr0YVXZE73mhAaQDS22DtlsXk2KU65V7r8MpauCsM6mGfUiNuUJl993tIc9Pes2ikj4LfJvvwCxfd3dcMhcMty6W12VxO6LGGc-k6kkBNsFhmulz16_SoUr1uoD9LKjH1y0gu_NbXLB-uNONViGwrYCMHKxoG0N6rNzlNsPbXMhkKQSQD5LO8R6An0lmJVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22323c2ffc.mp4?token=iEtD76CTXnqZ9X0gOd8nrNLWCz_jM8k0Q-msDiKkss4Ff7rba02p3AaCk6gdMAa031hc256GRTSPXb6fGUd6BG4uO4UKPYvssihaOXXfsTOcrVl2btu1tThDu5rhH3ZhlnKeqF_FC0UvcD4DmchnRDMyr0YVXZE73mhAaQDS22DtlsXk2KU65V7r8MpauCsM6mGfUiNuUJl993tIc9Pes2ikj4LfJvvwCxfd3dcMhcMty6W12VxO6LGGc-k6kkBNsFhmulz16_SoUr1uoD9LKjH1y0gu_NbXLB-uNONViGwrYCMHKxoG0N6rNzlNsPbXMhkKQSQD5LO8R6An0lmJVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
محمد تقوی، در آنالیز فنی بازی پرسپولیس - استقلال خوزستان گفت:
❌
❌
«در فاز حمله، همیشه ۶ بازیکن پرسپولیس شرکت داشتند. اما جدا از شیوه هجومی بازی با توپ پرسپولیس، بازی بدون توپ این تیم، غافلگیرکننده بود.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/138746" target="_blank">📅 00:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138745">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bL6T_f-5E_wDYJu8cg4dEQsUC1DAi4nCUDcJhEV-0VHEMVPoiYWfT5KmIbW1y24C9S1Zyp2SqtpJmHA5AoZqMy1cJlj8rddm55sHfq0vGJYMmsweKLLBUvLnlIhgRMMrRlPkVPjvKkn33g0rr0u_e6kCfc-zH0GDjG95NXOhwSfPYplFxub41mm69adih5_8bgKUN8a2OWv9SqHAJygJghtTFL7geQ3pDOTZNpS4CKqJ66UVQtVmxJbezpWJdcuviMruhECrk4Q5KWSRxA3s6GspMx9kTxkib-Hylk3SqLQxubwXI7pqDiBY7Ac_N9cs9Cr49op1YmkEcwPeDeHKkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
مهدی تارتار قصد دارد ترکیبی هجومی در بازی پرسپولیس و تراکتور استفاده کند و ممکن است یک سورپرایز هم در این بازی داشته باشد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/SorkhTimes/138745" target="_blank">📅 23:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138744">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
❌
تسنیم به نقل از سردار زاهدی معاون نظام وظیفه گفته که بیرانوند در لیست تیم امید نیست و از ۱ مهر سرباز میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/SorkhTimes/138744" target="_blank">📅 23:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138743">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
❌
تسنیم به نقل از سردار زاهدی معاون نظام وظیفه گفته که بیرانوند در لیست تیم امید نیست و از ۱ مهر سرباز میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/SorkhTimes/138743" target="_blank">📅 23:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138742">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
در صورتی که انتقال ابوالفضل رزاق پور به پرسپولیس کنسل بشه، امیر جعفری گزینه بعدی دفاع چپ خواهد بود / تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/SorkhTimes/138742" target="_blank">📅 22:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138741">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
❌
روی اشتباه محمد قربانی و بازیکن دیگه الوحده پنالتی رخ داد والنصر گلش کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/SorkhTimes/138741" target="_blank">📅 22:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138740">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🟧
🟧
🟧
دیدار پرسپولیس و تراکتور قطعا بدون تماشاگر برگزار می شود
🔻
حجت الله بهمنی سخنگوی سازمان  لیگ اعلام کرد هر دو دیدار رفت و برگشت پرسپولیس مقابل تراکتور قطعا در این فصل بدون تماشاگر برگزار می شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/SorkhTimes/138740" target="_blank">📅 22:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138739">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
حالا شانس ما یا گل میزنه یا میشه بهترین بازیکن زمین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/SorkhTimes/138739" target="_blank">📅 21:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138738">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
❌
فوری از عطا حسینی فرد نزدیک به تراکتور:
✅
هاشم نژاد و ترابی به بازی پرسپولیس نخواهند رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/SorkhTimes/138738" target="_blank">📅 20:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138737">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
🇦🇪
محمد قربانی در ترکیب فیکس تیم الوحده
🗣
پ.ن شاید سرکاریم خبر نداریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/SorkhTimes/138737" target="_blank">📅 20:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138736">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
یکی از سایت های اماراتی گفته قربانی با قراردادی ۱.۱ میلیون دلاری و سه ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/SorkhTimes/138736" target="_blank">📅 20:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138735">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووری از تسنیم
❤️
ابولفضل جلالی مدافع چپ پرسپولیس دیدار مقابل تراکتور و ملوان بندر انزلی رو به دلیل مصدومیت از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/SorkhTimes/138735" target="_blank">📅 20:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138734">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrRyQ5Y0vmCMHOoOFW0SEWj3CR0BA0n1IGmJTZQ5Lohne4xDJDgH02H0PrXYKq4m6FH2Cp29L3QbaXpLWK621ePwO-i_ZzbIyqI8LQQ2N-ab69vyv1APsCnNz6WtgWpdLTMULGthMoGUxqXUcaf_hXpU8gdo2GS5XAeuZkv2Dl4Losq2dD4q2oHbfF2dCsR6LP0DVvRtXazGOmmRScA09oX-hzgzFxgB1mS8vgJnzBA_HT1xqMOZ4RTLbcj8ahCb2WcIJcVw6F5iuDy747T--gniIUTn0V9xf4CtZf53PYQXJCNpbsHYLWS1OSA4K1yX9XZJnYXvdoKFyX0Cf54uDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ویژه بازی Scarab Temple
7️⃣
کاربران می‌توانند با هر واریز واجد شرایط، متناسب با مبلغ واریزی خود برای بازی Scarab Temple چرخش رایگان دریافت کنید.
در عکس فوق شرایط دریافت چرخش این بونوس ویژه توضیح داده شده! هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
🔵
نسخه جدید سایت:
Sportn5b2.com
🔵
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/SorkhTimes/138734" target="_blank">📅 20:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138733">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✔️
✔️
✔️
تارتار به حدادی گفته یه دفاع‌چپ از بین امیر جعفری و رزاق‌پور باید جذب شه/تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/138733" target="_blank">📅 18:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138732">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faR6iEZZM0ZKI6A8NS1SxIrOTPRt7gvp3kEl9nbuiHbIpRSLwCjH75fjIA0dodksk3JOCc7mkjzYkkjDFc0n0O8QPfhfdjJQQVILW_28Vs13vuyaIZhVn9UqvBUu8esAYByjeg_HNSZlMdbcSXy9D6jmmncxE2JgPCJhGUgxrAT3I3v7JbsYCoEW75M7hJrO7I7cFxSUIAYtIqQsQ7k7TH0KYZZbBS-u1rLq1Sn9BS06gsZkuzYb0Om4OQvfWtOjWT4OL_cFPA4tlxmef4F5BidkwGLCseH4ZfKeejTD6M_ZPLMWSoT849ZD9ceIL1lKKW2xXchYai_oJMff7_UyyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚽️
✔️
پیام نیازمند با 3 تا سیو موقعیت و ثبت کلین شیت بهترین دروازه‌بان هفته اول لیگ شد..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/138732" target="_blank">📅 18:22 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138731">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
❌
بعد از مصدومیت ابوالفضل جلالی، امیر جعفری، مدافع چپ گل‌گهر دوباره گزینه باشگاه پرسپولیس شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/138731" target="_blank">📅 18:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138730">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووری از تسنیم
❤️
ابولفضل جلالی مدافع چپ پرسپولیس دیدار مقابل تراکتور و ملوان بندر انزلی رو به دلیل مصدومیت از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/138730" target="_blank">📅 18:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138729">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYR1zxS3I2Ga1oTBL9BWTbFwvEV5CezUNct6KUzDP2Ndx2wCSNweHzYRLP_LCevf0mgfpDSQ6CrM-6UBjudqbIxM7od5gqXs9aflnlOSOjHXWjQCSsPbQv9cYQOQTarZQ6xOragAlGJWfQCA3PtbVKWiBqtPan8qhyQgjXsNBgJLmP8ej_3MXj-Yov2U-akwUiA2OtandkORNUP5w6TOdZzXN0W_GR2CSZnkDeU6rrYrMJ0NTiWYzotnz5eai2-VLV8sC9qnFTZ4pBGwECFG7CcXDeiETKF2P50qneo84oA-Wm_OnDwgqqO1bKZvj2-TD6U693lAfzIZJpE2jGbakw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/SorkhTimes/138729" target="_blank">📅 16:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138728">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/138728" target="_blank">📅 16:22 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138727">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
بعداز مهدی ترابی ، مهدی هاشم‌ نژاد بازیکن تراکتور هم بدلیل مصدومیت دیدار با پرسپولیس و سپاهان را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/SorkhTimes/138727" target="_blank">📅 16:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138726">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
❌
تسنیم به نقل از سردار زاهدی معاون نظام وظیفه گفته که بیرانوند در لیست تیم امید نیست و از ۱ مهر سرباز میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/SorkhTimes/138726" target="_blank">📅 16:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138725">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
ورزش سه:
🔴
سه سهمیه بزرگسالان برای علیرضا کوشکی، حسین‌زاده و هاشم‌نژاد اختصاص داده شده نه بیرانوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/SorkhTimes/138725" target="_blank">📅 15:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138724">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔄
🔄
فووووری: چون نام بیرانوند در فهرسته ارسالی اولیه وجود نداشته در فهرست نهایی ام نمی‌تواند باشد و نمیتواند به عنوان سهمیه بزرگسالان همراه تیم امید باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/SorkhTimes/138724" target="_blank">📅 15:44 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138723">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tImV8jmqAllr3NraHDwQePuKv2hDGTDsh3UsIdNvxZOp6msXJxkeNkYHZtX1s89zMtRjt6M8qM9SCp6Rlv8q3Y1ZJQhlRz7aGJgyuUzFymXwZrg9d32ROJDWXJM-4V_p84FiGWAnky4hYm6-E2OJc02GKZWWW7Yh_tfMETEAJe9QOqp_yW3WftEirhlBp4TkE1pb93YeHKJNr7-ET_AManEDoRjmVu3YNSdpazfIrFQHruKHRo3RVtP5ms8vIxxK4wwui9fbLE0bSwKXbdkNFvUkMR0TgVna9yzvWpzNgDv9bqMJcaIARckhmZ6fNzZV84DTSPVHQ6_TnHal8DYDKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووری از تسنیم
❤️
ابولفضل جلالی مدافع چپ پرسپولیس دیدار مقابل تراکتور و ملوان بندر انزلی رو به دلیل مصدومیت از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/SorkhTimes/138723" target="_blank">📅 13:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138722">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
✅
✅
فقط تا چهارشنبه پنجره نقل و انتقالاتی بازه و تکلیف قربانی باید معلوم بشه.بعد از چهارشنبه دیگه فقط میشه بازیکن آزاد گرفت   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/SorkhTimes/138722" target="_blank">📅 13:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138721">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‼️
‼️
‼️
موافقت فولاد با معاوضه بیفوما و رزاق پور؟فعلا خبری نیست.قبلا فولاد حاضر نشد در ازای رضایتنامه رزاق پور علاوه بر بیفوما ۸۰ میلیارد هم پول بگیرد.
❌
❌
پرسپولیس همچنان مصر به جذب رزاق پور است و راهکارها را مطرح می کند./قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/138721" target="_blank">📅 13:39 · 30 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
