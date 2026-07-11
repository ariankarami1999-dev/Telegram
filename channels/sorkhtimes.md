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
<img src="https://cdn4.telesco.pe/file/FWiGQUMtIa772MhHLQZTCv0gxTshBD1sMXATaDcI6xj2LF3qaxrB-tD9tlSpOzR5pXOY1r6O3xm4zPg5htS6PUYDVYLSXz4CV2IvwbMXaxzudx1SKSeYuwphiIxm1wuRWHZekaVut6S78Vi4lovoMYIMylbzqjAjLd8cE8a8QNKa3kdekzQL-ysvGbY23mdGleS1-6CAHIv-Ye5z9dLbuOnym_CgM1UoRaP-9-UGBGnGx0myjahlgU74CL81UqPy_wKyZk7ifer7WnlraxcaWnQD8SnL0b2eFf6g2PMSEJ7aFotfRdR7USNmt4yeW3FhZef3BkRr8S6WYVORtrTHjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 14:08:51</div>
<hr>

<div class="tg-post" id="msg-135484">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6oTK7B5HgY6Rodjvt1XNBnIzrr5jhSBlIZx8AWrUZal2oKWcOKjQGR1LKktxW6ctWzot1nrdb2ol06ghrVEynBsJDPEKANI1A9SS3N_XiDklJIq8xyFuZzEj7qCKLH_FJ3GwJFo3IwNeykk5gtyPkc9Buky5PLb7aAmLpxG-c9SYv4a7Fuba2ip_iw0i--QTVgzsr0JsBhEY1SCsvRZPJ2Lzuf6_yMMyqtKiML4BQ40n8seNyxRNjOd_mIySo2jih_maHjRNK_Zrv0jBNgpkla1zlpU90V5VVeAEKeXWy3lUzVga30-ehHk1fQ5PeBYZruBRh52pTbyZO8aHYJu5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
میعاد قاسمی، آنالیزور و دستیار تارتار تو گل گهر سیرجان به عنوان آنالیزور جدید پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/SorkhTimes/135484" target="_blank">📅 13:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135483">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❗️
❗️
باشگاه امروز به شکل رسمی نامه زد تا پورعلی گنجی، عالیشاه و سرلک در این تمرین شرکت نکنند!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/SorkhTimes/135483" target="_blank">📅 13:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135482">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nO-IrMqf8gQ5PUoumFQ6bStP96piY_0hjoz3iw6FOI5sHsT84se4ZSsv8A8Ro2EiSrD64r0ZIR0yuvxM_tvNKGd7hOPiK4YfXJ9eDXcxcmcxN_f3uTWv5kcfUx6ojUpSZUmNnHlV7qny-FDA8w_1AIG8-M60MCSW1chC5bYWUxUlbfjaPS4_8nNfNfe55Imq9ajYum_LWhcFgD6k9Q6xxTp0pCzhCIuH-KKo2rSema9T7M4a4iTieHVCgZnnzQpWX_WXe7P1x1wITFJTfoIB9FhVs_UTaTeIrBBf-xEeR4X5do_dXzq47XUF4wYQiBYofburS82FzAk8fk82ga0jcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تمرین امروز سرخپوشان در سالن وزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SorkhTimes/135482" target="_blank">📅 13:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135481">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
🔴
علیرضا بیرانوند در پایان شهریور 1405 یعنی حدود 2 ماه دیگر سرباز است و دیگر مجوز بازی در لیگ برتر را ندارد؛ مگر اینکه راهی یک تیم نظامی شود.
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SorkhTimes/135481" target="_blank">📅 13:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135480">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
مجتبی فخریان بصورت قرضی راهی گلگهر شد تا پوریا پورعلی بصورت رایگان به پرسپولیس بپیوندد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SorkhTimes/135480" target="_blank">📅 13:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135479">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
فووووووووووووووووووری
📊
محمدمهدی زارع در تلاش است تا رضایت نامه اش را برای پیوستن به پرسپولیس بگیرد /فرهیخگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/135479" target="_blank">📅 11:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135478">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
فوووووری / ایسنا
🔴
پیشنهاد پرسپولیس به اسلامی و کوشکی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/135478" target="_blank">📅 11:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135477">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
📊
علیرضا کوشکی وینگر استقلال تهران در لیست خرید پرسپولیس نیست/تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/135477" target="_blank">📅 11:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135476">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxjU944p3MkoXlqJGuGA4B1jUabgN84ruOTcTlsM7qNKTPeN8u1Wm5j6kWeixTFKZI0rQfqDWR4STk-BA8VWBynVD0PegYibGJZziPBcdo7My2g_Cq_4NMT3GxFWtbYLmkaG1JLsOH-XHz6jywv7vJW-ZaLzfVvrrSImuPNKGC_zISg3U-w9YCTMDQgBlV-XxgWtvygTg7PZdvU4BK3h0zxpoIf7uTpFzLqvQsnrO16SODwPIdq75B49TTQPqoZ2Yo7ws2RJNII5e4rP9O5MR2zBd6j4WQivzSOspNnptEkhdK2p-HJ3gMtyKXcW4Oc3vAU7xaO8j9TSFHbiCahiUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
مراسم رونمایی از مهدی تارتار امشب ساعت ۲۱.۰۰ برگزار خواهد شد و از شبکه اینترنتی باشگاه پخش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/135476" target="_blank">📅 11:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135475">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
پرسپولیس میخواد برای جذب احمد نور به کلبا نامه بزنه/فوتبال 360
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/135475" target="_blank">📅 11:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135474">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">💢
مدیران باشگاه‌ موفق شدند با محمد مهدی زارع به توافق شخصی برسند و قرار است مذاکرات با باشگاه اخمت گروژونی انجام شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/135474" target="_blank">📅 10:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135473">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
✅
پرسپولیس برای برگزاری اردو پیش فصل جمعه هفته آینده به مدت یک هفته تا ده روز راهی ترکیه خواهد شد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/135473" target="_blank">📅 10:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135472">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
فرهیختگان: تارتار درمورد این تصمیم خواهد گرفت که آیا وحید امیری در پست مربی در جمع پرسپولیسی ها خواهد بود یا به عنوان بازیکن؛ چرا که هم وحید امیری با تجربه است هم چند پسته است هم از آمادگی بدنی خوبی برخوردار است و ممکن است به عنوان بازیکن به پرسپولیس اضافه…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/135472" target="_blank">📅 10:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135471">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
پرسپولیس؟باز هم نه؛ترابی بازیکن آزاد نیست!
🔴
فرهیختگان: در شرایطی که در روزهای اخیر اخباری منتشر شده که مهدی ترابی بازیکن آزاد است تا دوباره جنجال‌های بازگشتش به پرسپولیس برای چند فصل متوالی تکرار شود، براساس شنیده‌های «فرهیختگان» او یک فصل دیگر با تراکتور…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/135471" target="_blank">📅 09:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135470">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFDZNhajNyTgtICZd9bwhUaGdncZ01Gx5Wd2q7htPiQXuhSsYyTg0-KkYtbGJZDIWpF6cLoM9rRuFol4eB0hl3OOlWrxzUVJDr3DpA9XQ6SJ6wWOVJyLpo5FOLfqSscYgTanLixXy2MX49RAcAIv7eZBOUwBea4XQiXmUKIhv_wG_upRDnSUOZiYn1SBCKq9Fg0Cmv_5oA0aCHlArAaIxnkhuueciCPZaQ0RimFQSkvqU7Y3TpC-3V3hxqV7XYg0x8oMNmDcUgGplyltmUCfhX5jOGSxB6Kj4-SdEBZHcSfH6eTlGemNljtf6QWnzILZZIXN2tqaCz8SqdubO730Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه پرسپولیس به میلاد محمدی ۴۸ ساعت فرصت داده که برای تمدید قراردادش به باشگاه مراجعه کند در غیر اینصورت باشگاه تصمیم دیگری خواهد گرفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/135470" target="_blank">📅 09:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135469">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔹
🔹
🔹
شایعات؛ اورونوف فردا میاد ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/135469" target="_blank">📅 09:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135468">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
✅
ترانسفرمارکت ترابی را بازیکن آزاد اعلام کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/135468" target="_blank">📅 09:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135467">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
پرسپولیس می‌خواد برای عالیشاه مراسم خداحافظی بگیره؛ حالا باید دید خودش این خداحافظی رو قبول می‌کنه یا نه.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/135467" target="_blank">📅 08:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135466">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔘
🔘
به‌عنوان طرفدار پرسپولیس، تنها می‌توانیم بگوییم: مرسی امید، ممنون آقای عالیشاه!
🔘
🔘
تشکر بابت تمام دویدن‌ها، عرق ریختن‌ها، جام‌ها و جنگیدن‌ها، اشک‌ها و لبخندها و تمام خاطرات ریز و درشتی که با تعصب و غیرت، با شهامت و شجاعت برای خودت و ما ساختی. سهم تو در سال‌های…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/135466" target="_blank">📅 08:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135465">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hki-mo1aFSe0qTtwdd7F-B16Ez-x48KktYMFCab2OFBTAyFTW5EK1Io7mEwddQmyoWrwktYw3QEnj_RabErdNZ1rwusWR5W78PGt2K2-6cloKJUJRBAPHhxi0sQNZGVmlane7f4wRvBDeQVJnmhuJWk2ytCLjfbRldrpVK1tS9pNW0zA9Hk3qDJp-uQxyx7gb3DVy8C4uOQejkg3ioZMrPOanMEFuPM84P5_cM3HH7FDSHERiQPqXSAQgy0LDHXuPt8D-z60JQGmOFL9nM21wRLvZsnBFKxLeFS0tCrHfFasPOPJFUMh-SezcC_q9oiNySHGE-ERCKqnEKm9EOa8GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
صبحتون بخیر ارتش سرخ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/135465" target="_blank">📅 08:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135464">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135464" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر پنجشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/135464" target="_blank">📅 02:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135463">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4_oa7GVbWrFiIAGv0LJ5kzJRScKpBozYCNdqg4bEqfNwO-alFA_Gjiq5MPOIreveBqjgRx5F1p8Uq_6-OoaLgNfVE147a3uuExCEyPnrvB0SJaRL90CJMLYU0lJFG_EzMCLMj1V0_KJJ5nBssJhEqHr3j-fXh3204kMi0Wqgax3dHDVIOd4428FzpUPokTNYI9edN1d0oC5V5H0jSXxnidMnQ0ArOLV2LO_4-jOp2rxxCEku2zy0-VsTRxfaLv4rgtBMpevicQr_WHfpAl3CUo598bDKcO5M1lbr7lRw4N_WARCbp6YpdCGndEAHKUJ5JL2_QPH8PohqAm0Fdbl-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《 لینک سایت برای کاربران ایرانی》
👍
《 دانلود اپلیکیشن اندروید》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
Ⓜ️
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/135463" target="_blank">📅 02:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135462">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
🇳🇿
محمدرضا احمدی به عنوان گزارشگر دیدار ایران و نیوزلند انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/135462" target="_blank">📅 01:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135461">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhIf6wgr4-IqTANS0EiS6CM1PWPRaVVcCaIyWaNXyxkkEstG8td6BNoYcV0FBDrrHg6Izh1FrkULu87dz8qvuS0uUit8NUErPMG1JnBK9GxUn_8PrAPpJGfGfcCcFtXobF7qN4Mj-9b6_QpIFd3UTFOJHuaotkEsh2Dl14qGFrxXoytDXWD_noXH09YyEamQ9TQukMv2qYAPApaw7-mWBg04Q2VIOB4zHh0PJyh3WgQhJT5b2oGWVyAytuXQH01DRcb624xPaP_QxeMprpwsQdWboqTBdzLzltaR0kQFz0_jNTfXyp3HJpRzqQgec-qKIaMh_SGk5VelnM8AvEJ3dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
میلاد محمدی هم با اعلام ترانسفرمارکت بازیکن آزاد اعلام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/135461" target="_blank">📅 01:34 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135460">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">💢
#شایعات
🔴
میلاد سرلک با عقدی یکساله به فولاد خوزستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/135460" target="_blank">📅 01:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135459">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
بعد از منیر حالا اندونگ هم رسماً از استقلال جدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/135459" target="_blank">📅 00:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135458">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/135458" target="_blank">📅 00:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135457">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5LQFYYekhnctpU99sVatgbZl_uQ58M4Gd57d5hGgwVnXxFmzh5_wLPMyQz__SR0RMr3v_9oFVZoVCV6oV_SYSxJatRp3J54He_tOL9yAFRuHlyDEBFNk1AmG12LMDw0wOUR9Q4h5o6FHj1jPXtiJCgtRJhQP5NDys6rlm9NrmwWdILLxMi95QQ3tx3OfgtlFP_QNjmMT882hH-aBi2sLmR7M6GYv_uGeIeIEaPW0Q7jUafHucjAIjZQXEvsjX0FoLLbKjvVxjcp1swJNtR7NinvGCNxMkBBDZmsXfs64rHi6y7uwPNwmP_ou_8jOFAF0HSRMP1pdKQdVPL6SVTHWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوررررریییی با اعلام ترانسفر مارکت علی علیپور از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/135457" target="_blank">📅 00:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135455">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D87qTw8SDbCW4gVBtpSlzv5Jk0mBngTja_OrS4OyUVVw-r2c8YtEKf0blTrYEX-XkYXXdJ8_m73nmL2wgBPRpJEbb1BvdmuFhYG4EfWRlL4IcAMQ7EEiNXTNN64ylmktF5VDmXQtvJxumG-UH7TWqA7ecCP6OdaOBloJ2sIPpUTB-9TPrCOAuOdwQAx5xs3OeoilvZRHtR4Cqkw4kzqmxHG4NPdN392jjIWVUx_Q1eDAjHG1ugmwGxMQg5MoGwjBDv9fPe8n61qTpA6rQ1uKHmGW9FA3u8lNO6v8b2JALXXS0AuKAsWTXOdC7GwM8bGBvpURKUgpdQ1oh3IexdrTuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بترس پرسپولیسی؛ رضا اسدی از گل‌گهر جدا شد!
😐
پ.ن نیاد جای علیپور صلوات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/135455" target="_blank">📅 23:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135454">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
فوررررریییی با اعلام ترانسفر مارکت علی علیپور از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135454" target="_blank">📅 23:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135452">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjdTMIE63oWXUfy9r4Xc18zIDLZiM0qxte5jt1REhnY_HCLQOcrcb3wcASRw2-UR0vtVwXLicswldeAemblz88qisV9ZK5qMBNbrg8x63KzISwHAx4eiRxTjP2lT_C1SHObFyIwk-k1cwCXcdAIJIUOwsnncEnColTtnaRICzB2sF8lCvDNLnevq_x1Ztjg-eWYIOC2VtqcSMvFpRQg-tm-n1-r688GAxk0zqBikK55-Hd2XOqtnmPkn2y1jmoJ-KxGr-gKE_1dMzlSucwYvfDfFfcBQ_esbpjAOQBz5Og1KcvvQ39RqFh3wKXBIbFei8xxZJEkPzCQnIPpPozQ4jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوررررریییی با اعلام ترانسفر مارکت علی علیپور از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/135452" target="_blank">📅 23:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135451">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🚨
خرید پنجم پرسپولیس نهایی شد
🚨
با اعلام سید مهدی رحمتی سرمربی گل گهر سیرجان پویا پورعلی از این تیم جدا شده و فصل آینده در این تیم نخواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/135451" target="_blank">📅 23:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135450">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
فووووووووووووری
🚨
خرید پنجم پرسپولیس نهایی شد
🚨
با اعلام سید مهدی رحمتی سرمربی گل گهر سیرجان پویا پورعلی از این تیم جدا شده و فصل آینده در این تیم نخواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135450" target="_blank">📅 23:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135449">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
اسپانیا گل اول و به بلژیک زده و اسپانیا همچنان تو کل این جام جهانی گلی نخورده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135449" target="_blank">📅 23:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135448">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❗️
برنامه کامل مرحله ¼نهایی جام‌جهانی
😀
فرانسه
🆚
مراکش
😀
🗓
پنجشنبه ۱۸ تیر ساعت 23:30
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
😀
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
😀
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/135448" target="_blank">📅 23:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135447">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bs2j8xtBZa0f3FCddFsOVHJaHWlG4C34xj4NnNEfuFmvn65lyfR1y3CsOLdTY3DP6FqweaOw0CmsIx9RMurbic0nsGexLCgfpPflA_shqd6gzeTCrlw9NY6aeP1k2AJvbjteNOKHx1juuO0aO0O3zo-yLH7FoFwS-DYUR9PIO666Bk2wpLNhkE4ZONrP4msGxkebk39lZk5Gs_xfxnR-LDM_gI1CDYNQs6whOSRfrZmGqrMzcQBAVi4CIZO3kMmUuhFZrFcME86SyTgcooCwPSZLynYAhIWemIy-jfRvkg4I3UOhq-6ocLC2qj0TDRlQhE50u4TpYa8NC9lA2fh_JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مازیار حسینی در راه هیئت‌مدیره پرسپولیس؟
❌
شنیده می‌شود مازیار حسینی، که سابقه مدیریت در شهرداری تهران و بنیاد مستضعفان را دارد یکی از گزینه‌های ورود به هیئت‌مدیره پرسپولیس است و حتی ممکن است رئیس هیئت‌مدیره پرسپولیس شود.البته فعلا چیزی قطعی نشده و در حد گملنه زنی است/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/135447" target="_blank">📅 23:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135446">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
قبل از آمدن تارتار با پرسپولیس بسته بودم،خوشحالی تیکدری، پسر حاج‌مهدی، از انتخاب او به عنوان سرمربی سرخ‌ها!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/135446" target="_blank">📅 22:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135445">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
تمام ملی پوشان بعد از جام جهانی و مرخصی از فردا باید خودشون و به کادر فنی جدید معرفی کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135445" target="_blank">📅 22:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135444">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
اگر اتفاق خاصی رخ ندهد و پیشنهاد بالاتری نرسد؛ دانیال ایری مدافع ملی پوش نساجی مازندران به پرسپولیس خواهد پیوست
🚨
🚨
توافقات نهایی شد و میلغ رضایت نامه مورد قبول هیات مدیره قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135444" target="_blank">📅 22:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135443">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZZ6xiFjImW7MzaePOC4o1Urr1BL1pST-pDEW29jGBdMxfa0uI2D4ys03E0pcMfd8lMBguReF-2M8GkZ2SL-GmR5LWNEYOS-Q-QUjh36qxtkUH29XwPds78Uy5ZtMPEE4aUB2GKhWC3LnidX_TAnkB5qzYbpKptJSgrM855NHsMy-niAoY37tJF9Vw6hvC08xjoFx8ea1oU8VA0Jvy3ScR4e7ZLdDCNHRZQPcgyWLFp-sFEPoOEAhfC8v5eWWlYR5d_yaulFMOHRPlIFu6nH53hYwRiOL8SPtQh6GVfEixLTz-w3iOrXzOifpZ95B6tgnUIgUl4qmzcrGx3kdLUI7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یا گو، مربی یونانی تیم، در تمرین امروز پرسپولیس شرکت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/135443" target="_blank">📅 22:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135442">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
فرهیختگان: تارتار درمورد این تصمیم خواهد گرفت که آیا وحید امیری در پست مربی در جمع پرسپولیسی ها خواهد بود یا به عنوان بازیکن؛ چرا که هم وحید امیری با تجربه است هم چند پسته است هم از آمادگی بدنی خوبی برخوردار است و ممکن است به عنوان بازیکن به پرسپولیس اضافه…</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/135442" target="_blank">📅 22:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135441">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
❗️
مهدی تارتار از آمادگی وحید امیری در تمرینات رضایت داشته. احتمالا وحید امیری برای فصل بعد به عنوان ی بازیکن تعویضی و برای مدیریت رختکن و...دوباره به پرسپولیس برگرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135441" target="_blank">📅 22:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135440">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b6deee68.mp4?token=mQB3Tt3ZS7Ja6t3X5_Ebask-GxMHXM85XH3IUdNJNfMzqMIm2GeDnMvov4ftLFDCLcHZtt3QNmqsUIu30e-HVh9shFoSfVhPig5ndqt7aK-v_xcvL5g391qtkBpkyFfzr51WxYqwwlSGImAuByFTsWStwHA-ttvW_1BdA-N2aV3AuFFR_u02F4k6Mh2nlLHamLB-IchZVLZwwywj4XrAXriZ3tRVum27WPsyxh2lWzq-mNuSDRYUG1ugI_vPXQM92fq8ok-5R-NA18AmN3ueAAQyVWrc0LaBB2nXPSJpQPqibEtzXce0Kj0Zzn1elKNopmJEt-08aypfV-Qde5OD8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b6deee68.mp4?token=mQB3Tt3ZS7Ja6t3X5_Ebask-GxMHXM85XH3IUdNJNfMzqMIm2GeDnMvov4ftLFDCLcHZtt3QNmqsUIu30e-HVh9shFoSfVhPig5ndqt7aK-v_xcvL5g391qtkBpkyFfzr51WxYqwwlSGImAuByFTsWStwHA-ttvW_1BdA-N2aV3AuFFR_u02F4k6Mh2nlLHamLB-IchZVLZwwywj4XrAXriZ3tRVum27WPsyxh2lWzq-mNuSDRYUG1ugI_vPXQM92fq8ok-5R-NA18AmN3ueAAQyVWrc0LaBB2nXPSJpQPqibEtzXce0Kj0Zzn1elKNopmJEt-08aypfV-Qde5OD8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
قبل از آمدن تارتار با پرسپولیس بسته بودم،خوشحالی تیکدری، پسر حاج‌مهدی، از انتخاب او به عنوان سرمربی سرخ‌ها!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135440" target="_blank">📅 22:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135439">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8efabe672d.mp4?token=pU33oN3wV5MFfJpuUP-AbMbMwc3nPbz_EXTTX_ynEX4XJKxsrC_8uPq9etulFrhvuYva0xJinX8giOi3tojKCb2A30xLFXTTxEUMizyNsCzFuYXN-cNfeTwcbjULIdVFHKqCqvwKESn4XJ8g5svE53AgJIEkybBvVdG0FZda2MoKqZMAShlxC7Cdd5EzLJc2wxfcfjoWSyWc9B3D8Xpi8_BJ_3G1y-EHqGrCOJdW-xDYvY2O75QL6ns4NJTcQWAdDMI9OH0CDu6kdTwu-BglXLQzGyF8Zdpa-NM-GRhOZuFk0RdXbzCpKzwMk7mAuRuKhs36VNurzHs7LI1A6XRkuDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8efabe672d.mp4?token=pU33oN3wV5MFfJpuUP-AbMbMwc3nPbz_EXTTX_ynEX4XJKxsrC_8uPq9etulFrhvuYva0xJinX8giOi3tojKCb2A30xLFXTTxEUMizyNsCzFuYXN-cNfeTwcbjULIdVFHKqCqvwKESn4XJ8g5svE53AgJIEkybBvVdG0FZda2MoKqZMAShlxC7Cdd5EzLJc2wxfcfjoWSyWc9B3D8Xpi8_BJ_3G1y-EHqGrCOJdW-xDYvY2O75QL6ns4NJTcQWAdDMI9OH0CDu6kdTwu-BglXLQzGyF8Zdpa-NM-GRhOZuFk0RdXbzCpKzwMk7mAuRuKhs36VNurzHs7LI1A6XRkuDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
قسمت بود به استقلال نروم
🔴
روایت مهدی تیکدری از منتفی‌شدن انتقال ۲ سال قبلش به استقلال؛ آماده شده بودم که دیگر هیچ‌وقت نتوانم برای تیم محبوبم بازی کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135439" target="_blank">📅 22:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135438">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» مدیران باشگاه پرسپولیس با نظر مهدی تارتار با این چهار بازیکن وارد مذاکره شدند.
⬅️
مجید عیدی
⬅️
محمد قیرشی
⬅️
پوریا پورعلی
⬅️
پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135438" target="_blank">📅 22:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135437">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135437" target="_blank">📅 22:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135436">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfVXLWrqGN-JuCSbF1-hqtDhTE0lwvohYJMjPBOhn-etLXo-aNO5E6ykiqQfWvRlXFqBj0ExqrhFlNbvi0Bau_IiteQaZcMDoY7X7hwjE0Bl3AFm3zzhxudDxk89FbhSfjbwMsmEeNycaO5SnqfLZigMB1lERmmAD7PTJ3n9__v_QR7qtduififWyWqXenqpUaFlDA_1WRvlKz9d-1JzPl664epauUMiRyFQQ4htkeQ6Z3fQZASHpIHg5ai524Tkdk6oWopuT6m7rfPFZg0z5W_KhePt3Z7P1Cciesck8sKUDynJjPxY71zsLcMGDU5O3f34FLdiuWGQK2pyTw0mww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گزارش تصویری از تمرین امروز پرسپولیس و اولین حضور ابوالفضل جلالی در تمرینات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135436" target="_blank">📅 22:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135435">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❗️
❗️
احتمال همکاری امیری با پرسپولیس برای فصل بعد چه به عنوان بازیکن و چه به عنوان عضو کادرفنی بالاست/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/135435" target="_blank">📅 22:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135434">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بزرگترین کانال پیشبینی فوتبال در ایران
🔥
فرم های بزرگ ترین جام جهانی رو از دست ندید...
⚽️
@Tabanii_Mafia
@Tabanii_Mafia
⚽️
@Tabanii_Mafia
@Tabanii_Mafia</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135434" target="_blank">📅 21:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135433">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IskmIt8gCJTClmAJXuze4V5TOO6Hk7vl5vLaYkbpdcZNbsFBbAxwdVzJfF-4UMwXGpwIMEAZ8pASa1AlieAOW7Rec35OasHEMoxFjF4qhiMvYsmMlpoo0m5XM02MbUMjLr1KhX8TP_-QR5dsVZUibLEjD-KJaKTitSH51Xmi0kdohPtjNhlmsj7mNaxrxPlW644E57pRGlBoUFDU6IoIPIFNYxeMTVsjApC-szhU9Mt-DqSN1QaYZNoQHPThGAnDpS1xur8oQD4vrxrqEdV5owiJfm1w-YlBx8JTdxEfrILjBw4m9RZkWaqZwzZ_bi4yWuAVQKXiYCNoIASwMoec7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تک آپشن عالی برد شد
❤️
✅
✈️
@Tabanii_Mafia</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/135433" target="_blank">📅 21:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135432">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
❗️
قدوسی: تارتار خواهان حفظ هر دو مهاجم خودش شده اما خلیلی و حدادی به او اطلاع داده اند برای صرفه‌جویی بودجه باید یکی در تیم بماند و یکی جدا شود.........!
❌
❌
تارتار علیپور را انتخاب کرده و اگر علیپور تمدید کند باشگاه با سرگیف توافقی فسخ خواهد کرد
😐
😐
😐
😐
😐
…</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135432" target="_blank">📅 21:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135431">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
امروز جلسه‌ای بین کریم باقری و باشگاه پرسپولیس برگزار خواهد شد در مورد شرایط ادامه همکاری با یک‌دیگر گفت‌گو کنند/تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135431" target="_blank">📅 21:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135430">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
ترامپ: این اقدام، تلافی بمباران کشتی‌ها توسط ایران در دیروز است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار وخیم‌تر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135430" target="_blank">📅 21:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135429">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCl5eGkW3q2XxTvT9levKtogvaRj385aTXKe0BII-3y9LaKY_EZAyzv0OSJSw_zYoZ7Yx56Z0u8p7K82Flw-OyU0_uI_u1TjyyzakQ_lPv33KHTUTqknef8t5Iwe_MJQLGdO43tsgX9DzALPL_vZFGBN6G85MaAQY1YfpVdWed-2LVU1f9gC2_60gUK2qQ-HOiyTRDZyzB0DPJMA-H23bh1afgSQqa9fvS0fEvcMVg4kUAj9kL0Lj_QLZOWyzPgHlLeIyX2ohkjqf9gOk0QPfjb8Qo9F31zvr7A0LheA5La6IzzsRut7gtkahjuGeJSbSjPm7mszQmeBqpT9X45Wdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعد از منیر حالا اندونگ هم رسماً از استقلال جدا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/135429" target="_blank">📅 20:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135428">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">💢
سپهر خرمی: پرسپولیس و رامین رضاییان در حال مذاکره هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135428" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135427">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
✅
به دلیل مسابقات آسیایی ناگویا ژاپن پرسپولیس، کسری طاهری، فرزین معامله گری، پوریا شهرآبادی، علیرضا همایی فر، امیر حسین محمودی و در صورت جذب (دانیال ایری، پوریا لطیفی فر، مسعود محبی یا مهدی زارع و فرهان جعفری) را از اوایل شهریور ماه تا اواسط مهر ماه در اختیار…</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/135427" target="_blank">📅 20:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135426">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
❌
🔴
دفاع راست ها :
✅
عیدی و تیکدری و براجعه
🔴
دفاع چپ ها :  محمدی و جلالی و معامله گری   نظرتون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/135426" target="_blank">📅 20:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135425">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
تصاویری از حضور بازیکنان تیم پرسپولیس برای انجام نخستین تمرین برای شروع فصل جدید که چهره ها نشون از روحیه و شادابی بچه ها داره با کادر جدید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/135425" target="_blank">📅 17:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135424">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZ6oO_vMWZVYtlZU3EG-0HGJR7XCo2TceLTnDCmFFDj3MB-u09IEAFuzsyWiEg6dS4rKEVlKa4WhHHt513gtKdgzyZRBDOdkzAVZQUKJWeBOKQaB2dIZs8J31bNzuUwEbpdYKh_ESuqgj9TV8egWunMuwxF2leyepKTUMPtNfcxP5VfnsWGq4lqfKt63EMo_2soJ6busCzRJTpA3Rs-Ct98r6RRNbMgXCCW8mM4IgUXJULXPSC6APo8KC3cCbCvX4-qUAR2SSEP7EXjwY-GfTNm3G-RGXIup5zlpljQD2D_ksxRYfrQ08CqIov-PYb7MrAm7kGTXH5ebJe9GjlVPvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار ابوالفضل جلالی بازیکن جدید پرسپولیس
✅
جلالی تنها دفاع چپی که در یک فصل ۱۰ پاس گل داده و بهترین پاسور لیگ شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/135424" target="_blank">📅 16:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135423">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔖
منهای ورزش
🔴
جمعیتی عجیب و غریب در تهران که انتها ندارد؛ تصاویر هوایی از حضور حماسی مردم در مسیر تشییع پیکر رهبر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/135423" target="_blank">📅 16:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135422">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqAbLgljG3DXX1OvxHYjuK9zwaoshyR0o7OLUsGasmOI1hMwTEZDwJTnq55Vl9JqXX7laZ2_hBW28j0GIM9S1eTYabQAw75gdVvJwktK7We3BORkKY93F2sIdWvnw_XwLKp438dtQhNLX-RVlbeE999lUe5SJpAY39by8PExZ_ind1Y5Ab7YYAi7R5BQx4w0FopKDmSo2PRAa1nPgERICqYtX-33g6xbHbSda6evEN6iLDSVbd4NkbSJaVrA8nMABjc-xQiIoetAjjweVZkxBSV5a7Vt0Cwt4tvVW4oFjh0TYLKrgw84KU4IaTLBzAotfBX-xzxyL3OlCd7Ltzqn-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کاپیتان‌های فصل بعد پرسپولیس؛ با رفتن امید عالیشاه و سروش رفیعی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/135422" target="_blank">📅 15:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135421">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
✅
یکی این شلوار شیش جیب و صندلی رو از باشگاه بگیره.همه رونمایی ها همین بوده
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/135421" target="_blank">📅 15:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135420">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
❗️
#رسمی؛ ابوالفضل‌جلالی مدافع سالیان اخیر استقلال با قراردادی دو ساله پرسپولیسی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/135420" target="_blank">📅 14:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135419">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135419" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/135419" target="_blank">📅 14:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135418">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/135418" target="_blank">📅 14:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135417">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
سازمان ملل : شاید باورتون نشه، بخاطر درگیری‌های مجدد تو خلیج فارس، ایندفعه خیلی بیشتر ازقبل نگرانیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135417" target="_blank">📅 14:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135416">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
❗️
#رسمی
؛ ابوالفضل‌جلالی مدافع سالیان اخیر استقلال با قراردادی دو ساله پرسپولیسی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/135416" target="_blank">📅 14:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135415">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5cU0QmcfPSvhGJgG6nSICcyZzz0VBUgM5r448qMY3CQyagwixTT1Ydq-AwIL5Lh2dlDjaygqVhrZofeX5R-Iwn2J3Kn8Giweqfrlt5GrX8c56IjzpDvzKCiztWIWZo1jZP7MyvbLWf2qFCDQQZKCIKkSJOm4afqEN4ez17gFr77fgzE8HemKggQqwFDGPF7WY1UPm4esoCLXNpMNc3UdYRjnzzx2gEkDC2OP0K0uiuMQIVHgjcc3BKht9Q1RoLZn00JdeAZ9HSCst2yUf0BhVL61BZqSM5FGqziFLiamtHC-LekAS725Rf9o871-MNjNXNCkIDP2h5HYUy0CKjaBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باز هم تایید شد .جزو اولین کانال ها اعلام کردیم جلالی و مبارکه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/135415" target="_blank">📅 14:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135414">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
تایید خبر دیشب مون
🚨
🚨
🚨
🚨
تسنیم: ابوالفضل جلالی دو ساله به پرسپولیس پیوست.همچین پوریا شهرآبادی چهار ساله با پرسپولیس امضا کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/135414" target="_blank">📅 14:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135413">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
چادرملو اردکان با برتری مقابل گل‌گهر سیرجان در ضربات پنالتی، راهی لیگ قهرمانان 2 آسیا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/135413" target="_blank">📅 14:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135412">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗️
غایبین تمرین امروز پرسپولیس:
❌
پیام نیازمند ( تیم ملی )
❌
محمدحسین کنعانی زادگان ( تیم ملی )
❌
مرتضی پورعلی گنجی ( مازاد )
❌
میلاد محمدی ( تیم ملی )
❌
دنیل گرا ( مازاد )
❌
میلاد سرلک ( مازاد )
❌
مارکو باکیچ ( نامشخص )
❌
امید عالیشاه ( مازاد )
❌
علی علیپور (…</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/135412" target="_blank">📅 13:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135411">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
✅
باشگاه الشمال قطر با ارسال ایمیلی به پرسپولیس خواستار جذب اورونوف شد. این تیم اعلام کرد که حاضره 3.5 میلیون دلار برای‌ جذب اورونوف به‌ پرسپولیس پرداخت کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/135411" target="_blank">📅 13:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135410">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔹
🔹
🔹
🔹</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/135410" target="_blank">📅 13:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135409">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔹
🔹
🔹
🔹</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/135409" target="_blank">📅 13:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135408">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔹
🔹
🔹
🔹
#شایعات
🔹
🔹
باشگاه پرسپولیس با رامین رضاییان مذاکراتی انجام داده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/135408" target="_blank">📅 13:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135407">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
🔴
دنیل گرا با نظر تارتار در لیست مازاد تیم قرار گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/135407" target="_blank">📅 13:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135406">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
خوبی بازیکن های مثل کسری طاهری پوریا شهرآبادی اینه که هیچ کدوم لیست بزرگ سال پر نمی کنن و همین طور سهمیه لیگ برتر حساب نمیشن هم جوون و آینده دارن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/135406" target="_blank">📅 13:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135405">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
انصافا بعد از سالها تیم داره جووون میشه ...همه بازیکنان خوب و با استعداد و جوان داره جذب میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/135405" target="_blank">📅 13:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135404">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
با اعلام‌ ترانسفرمارکت امید عالیشاه از پرسپولیس جدا شد
🔴
خداحافظ کاپیتان...؛ بابت تمام خاطرات خوبی که برامون ساختی ازت ممنونیم.
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/135404" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135403">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gk8HGr7_YPGIusquatLEds-p-KiUyEwZNAFLac20mvVbMJUOliFNC9AbzqbXKJTXnSVRkiGKsEdzSmjsm2Hmr31myaTrVD5WSFc5QN86KZgGWATBIbZRvXpJseL9RcqnnBejJg1cIroa_mht6HJkXDJ524qsrCUSGr7i_yUkGhvapVbpRuhsKGcUPXAtsq6kkfDkZSGySc5KtgG6rPUAhhc5-UT9fTVgdDBz45zmqvW_njk-qDbusojJoa3dRsGococ53onfK7acwbPuv58OGLXBiBWXZqnmNgzJRFEMQiRztEL-zDpq6KjVBurBPcD9z28Pmd_YjBTRMx8qtwXBcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام‌ ترانسفرمارکت امید عالیشاه از پرسپولیس جدا شد
🔴
خداحافظ کاپیتان...؛ بابت تمام خاطرات خوبی که برامون ساختی ازت ممنونیم.
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/135403" target="_blank">📅 12:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135402">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔘
🔘
🔘
باشگاه پرسپولیس فردا یعنی روز شنبه مذاکرات نهایی و پایانی خود با دانیال ایری و باشگاه نساجی را انجام خواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/135402" target="_blank">📅 12:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135401">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jM6UgxezDXavW0VIbOYzBbaaordFut8VmLJmfCUqtoQLWqn5h_mNxBtg9H1G01VwdyvPiYkLCL38Bh3I4yGLxJHnia1-dUYfqUEh_gl4du4ZiU0plMod6N6Dhkch1OM-cbRdXN7HAq07ENuelJcnNwliwoui7Q0gWsWuWbfOtsVf4HgcuO48HcsDBx8jZM5qifataYMh5EaU7NS6ZC2oEG7hd4E_gH3LHyb5qHEkyDbVPW6ZKIBF3K1nDx5WZYTPPq-DJ0PZbAhoRN_SwthnwIcRmcMrjMt1mxz-feqfml6akABRHrxftumvSJNvidazjAwtH5-tmtL-OAO87Gvykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آقای گل لیگ عراق چرا بدون تیمه
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/135401" target="_blank">📅 12:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135400">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
دور جدید مذاکرات با ایری امیدبخش بوده و مسئولان باشگاه به جذب ایری امیدوار شدن/ قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/135400" target="_blank">📅 12:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135399">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gn9Ifp5E351vrhoPLKY59fqtGA8uUXlwFeIE_aCDMxEWVvpdTzt595BVNCg0ziyYclbBeDYq4-KsZmLgrd93U49tibTGGR2owZ5VukPLAANg8Jmsvx0gAiW025RLifANOblT60lLBeDPgwTCR2L87AlTJmGefSfXG6TH_MBBlb8Ih3W4V770EtM6QEGxinBMZRE-fgAZzUiqQU_-uccgVXb-KnD7kXjNNP83ttPB3oJpdDcsRqiIlVPq56icBBYOoY0KoCB0MolDI_Q-wP4yT4euO7ribv66EF_fZkfhOtq5-TnE6zZxjPl38NAksq5lnqgPBPNAQKwrW95w7-Cgag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پناه بگیرییییییید، اریک باگناما بازیکن ازاد شد.
🔴
پ.ن اوه اوه .فقط مونده این بیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/135399" target="_blank">📅 11:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135398">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">💢
💢
💢
🚨
💢
فرهان جعفری ، دانیال ایری و پوریا لطیفی فر سه خرید بعدی هستن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/135398" target="_blank">📅 11:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135397">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗️
دیروزگفتیم ابوالفضل‌جلالی قراردادش رو با تیم پرسپولیس بسته فقط‌مدیریت این باشگاه بهش گفته فعلا مصاحبه نکن. حالا با اعلام ایجنتش در ترانسفر مارکت؛ سیدابوالفضل جلالی رسما سرخپوش شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/135397" target="_blank">📅 10:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135396">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
پرسپولیس برای جذب ایری خیلی تلاش میکنه و بسیار خوشبینه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/135396" target="_blank">📅 10:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135395">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
🔴
دنیل گرا با نظر تارتار در لیست مازاد تیم قرار گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/135395" target="_blank">📅 10:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135394">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
طبق گفته مدیران باشگاه یک سری مسائل حقوقی پیش اومده و تا اونا حل نشه از جلالی رونمایی نمیشه
⏺
البته یک منبع دیگه معتقد بود باشگاه میخواد‌ اول تمدید قرارداد میلاد محمدی رو انجام بده و بعد از جلالی رونمایی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/135394" target="_blank">📅 09:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135393">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
ترابی در لیست پرسپولیس نیست
❗️
درحالی که در چند روز گذشته خبرهایی مطرح شده بود که مهدی ترابی مورد توجه مهدی تارتار سرمربی پرسپولیس قرار گرفته اما پیگیری خبرنگار آنا نشان می دهد که ترابی در لیست خرید سرخپوشان نیست و مذاکره ای هم با او نشده است.
✍
خبرگزاری…</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/135393" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135392">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
حضور مدایم وحید امیری در تمرینات پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/135392" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135391">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
برای تمرین امروز چهارشنبه به بازیکنان  پرسپولیس اطلاع‌رسانی شده و در این بین به ۳ بازیکن دارای قرارداد، گفته شده که تا مشخص شدن وضعیت‌شان، در تمرین شرکت نکنند.
✅
امید عالیشاه، مرتضی پورعلی گنجی و میلاد سرلک این سه بازیکن هستند.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/135391" target="_blank">📅 09:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135390">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135390" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر پنجشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/135390" target="_blank">📅 02:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135389">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8NWSC_BEpkYF5eEyBcD6Bg0eUGB41KQ2xGVj65mAHCUzuVHaljh45NtYaW_pXK-6MqdT83ZoKh256Pyz5LodWEcZtfScz5FwJhPSSgYEXjkXkhAK9KUtG_Gyx8pAnTu3cvU_v0uKJ88E4-MzInmf-D9EfFYfbaLIUg8BffoiScMbtiskQxIaNAbxjnNOnUAYrrMxrwRx844CCDYU3XLnD5sZ04AifVb3vHxkqyVxKEi9dzVML4-z7djA26m5A8E_00rm-xG7ZmzYEMpMqltyr_tqB0Zfx4Fy7UcKQHc5g1rh4nc1ug0mRmn2mWdS7gtIHLHFl5AiC0KO50NMV1SRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《 لینک سایت برای کاربران ایرانی》
👍
《 دانلود اپلیکیشن اندروید》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
Ⓜ️
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/SorkhTimes/135389" target="_blank">📅 02:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135388">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
فعلا عکسی از جلالی بیرون نیومده ..شاید هم کلا امروز نبوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/135388" target="_blank">📅 00:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135387">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
علی بازگشا، سخنگوی باشگاه پرسپولیس: «اینکه پیشنهادی آمده بی‌اطلاعم، اما ما می‌خواهیم اورونوف و سرگیف را حفظ کنیم.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/SorkhTimes/135387" target="_blank">📅 00:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135386">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
برگام فیروز کریمی شده کارشناس بازی های جام جهانی کانال  gem tv
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/SorkhTimes/135386" target="_blank">📅 00:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135385">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">💢
💢
💢
🚨
💢
فرهان جعفری ، دانیال ایری و پوریا لطیفی فر سه خرید بعدی هستن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/SorkhTimes/135385" target="_blank">📅 00:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135384">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
✅
باشگاه پرسپولیس از دنیل گرا و بیفوما هم دعوت کرده برای مذاکره جهت فسخ به باشگاه مراجعه کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/SorkhTimes/135384" target="_blank">📅 23:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135383">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">💢
💢
💢
🚨
💢
فرهان جعفری ، دانیال ایری و پوریا لطیفی فر سه خرید بعدی هستن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/SorkhTimes/135383" target="_blank">📅 23:36 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
