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
<img src="https://cdn4.telesco.pe/file/t2Z1z7nFdM4fUk6T1Wk7NpnGNKS-tEdOzv09Swy0GdclncylkJMzHgG83Rfe4vRZ5kKKHkxgle-Q8MDcXVK5191Id0hnFkTdpfYafrorHYBtTD-d65I8KfSkxMGpvvVxV0cGkJTOk-IVoJrCM_qQ-c_u_Zw5-u4m67W0r1APqPv3sd3xIOkxUE7KJZjx4G3nI09ABzqXYd2NtpkegbGptUU9WGPaNG2ox60si29OOAYexZPFW4-FtAf6QnoK_Tre8V21C5WhQ1m1AGuALiBlJ-2qU3y040FAMwm3TpI4YmivqWQ-2HZHQ_jDhMsYJ8QvYMhe0BUuPQsjuNx1WJRSWQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 19:19:40</div>
<hr>

<div class="tg-post" id="msg-132594">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a1bce686.mp4?token=utKI_tm0AblVrERMmJ2CAB2LYjt8H2PFdgt_qt8kNQ6OVVInBmc77n8mbl5F1lvEeFXh20AJjkzdF0DCNLDVCbR38OMdKvENxD9lcXTiy0pJHCejIm8EOg5W3qwTWTcBBZ7gnBuCzVOVX2hZxIWQaMfeYSa71Sv0Y7j75LWZvuxGbApIUPg3_DoTcJWOidKllN2dnBnRpUXe1IvbeTcBkrSAJ245DbjxlM2WNAhhU3Iy8A3tPy75kWrmbvqakiN8JivTlvOR47vuj6c5ZZZ-h6QhYayfBfnasjMxvlOjADBdX1G5OzkKE68u1twkjWj6SlsAiRRc_537xM_zQVyGUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a1bce686.mp4?token=utKI_tm0AblVrERMmJ2CAB2LYjt8H2PFdgt_qt8kNQ6OVVInBmc77n8mbl5F1lvEeFXh20AJjkzdF0DCNLDVCbR38OMdKvENxD9lcXTiy0pJHCejIm8EOg5W3qwTWTcBBZ7gnBuCzVOVX2hZxIWQaMfeYSa71Sv0Y7j75LWZvuxGbApIUPg3_DoTcJWOidKllN2dnBnRpUXe1IvbeTcBkrSAJ245DbjxlM2WNAhhU3Iy8A3tPy75kWrmbvqakiN8JivTlvOR47vuj6c5ZZZ-h6QhYayfBfnasjMxvlOjADBdX1G5OzkKE68u1twkjWj6SlsAiRRc_537xM_zQVyGUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دو سال پیش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 747 · <a href="https://t.me/SorkhTimes/132594" target="_blank">📅 18:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132593">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
خلیفه، نورافکن، محمودی، حبیبی‌نژاد و طاهری خط خوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 785 · <a href="https://t.me/SorkhTimes/132593" target="_blank">📅 18:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132592">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
مهدی لیموچی با ارسال درخواست رسمی به باشگاه سپاهان، خواهان فسخ قراردادش با این تیم شد.///قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 949 · <a href="https://t.me/SorkhTimes/132592" target="_blank">📅 18:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132591">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/SorkhTimes/132591" target="_blank">📅 16:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132590">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
خلیفه، نورافکن، محمودی، حبیبی‌نژاد و طاهری خط خوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/SorkhTimes/132590" target="_blank">📅 16:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132589">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔰
آف ویژه سرویس VIP
🔰
5 گیگ 150T
🔥
10 گیگ 300T
🔥
20 گیگ 400T
🔥
30 گیگ 500T
🔥
40 گیگ 600T
🔥
70 گیگ 900T
🔥
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/SorkhTimes/132589" target="_blank">📅 16:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132588">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❗️
خب سپاهان که مجوز نگرفت. گل‌گهر هم بازی اضافی‌ش حذف میشه و چادرملو هم فاکتورهای لازم برای مجوز AFC رو نداره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SorkhTimes/132588" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132587">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SorkhTimes/132587" target="_blank">📅 15:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132586">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SorkhTimes/132586" target="_blank">📅 15:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132585">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siyFw70xJIZjGSjmTLo3R3YDws6mHSsP6lTjw7Z5VObNo1Mx0p6YEXND9_hIwgdvYSwpJ8zp5AMoVhwSe0aoCOjBb8UqnhYOUIGEQO07pQLny49USftAWD8UNg7SHMvlX8TxFCVRw9toIEkapkiowecjv9UdllctDeIY6GaFSOJjhFzZHeY6GeofRI7rlhzv9Fw12dHIG1fbdGo36bNT77q623vAABSGWguIZQyXt6TI98GRY5bEUOGdZpIZsx53v6qSRFybLaobBhwrviUE2PKHSTdWVaJ4jxoSkqoHAnrE2tTZfS7JCNslENmjba9dN1JGgti5CAhfQuo-Mri7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SorkhTimes/132585" target="_blank">📅 15:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132584">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOkpeuJv84Hu3ae3qDLuqjZ9MKkTa6ZpFfQWPO4Iq7_0lisXkqqQY8qeB1RVTyAGzuh2A47ybFJfmZ9LOYatJmZwYg-tB2galagCFkCJmnhyqP4AoYMlmXW0M_1UcoHMkte1TfG6OplFVHnzfaXa9Vk8R6MyWcgbvrKhwQA8CyzDyQt4XX2bvp7xm5I_2GjyFd3weRrCRH8Uacnl6oh4LxAgxgHJDUrC4WynJkn7VO4TATys234XRyF9RCPgq5vCcZS0WOIsOAXCOz8prpeeyvzPFaY405BIVoYEaMy4iZRHS5OWMtFWNGafS5NFHjgHdB4ppzCeUuHri6caFaApZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مراسم معارفه مصطفی میر ابوالحسنی به عنوان مدیر جدید حراست باشگاه پرسپولیس با حضور پیمان حدادی، برگزار شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SorkhTimes/132584" target="_blank">📅 14:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132583">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPdFmF23ulezpbOO9XPgaPJm02OupdKgtMBfyWtKhJxruozZV2jjVdPc_bOAZE7VgBP7qsnSiJ0mzJyeVa9hEjZtFBDLM4XUOifTngDmmyOteH6kkur-MtTB-63ud8RTFyMxhmBf54cLQajrPSacV1NilGcOsjdJxWWOq5NhqKFKlT56aQCgQ9hBGUuI-OBaB1E6glPi5YaxLCjMLJ-3AQwX353as8v3KU5PUxSk3Gz-ucfhOMtHOheAmrbcwBVhvdUFISC69wxjBvi258PtBfq5CcldV-7WK9Emg_riA5cUoadtL46e4Ob5FgjvfF5atyExseZiI7gOwCwZjyjMuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SorkhTimes/132583" target="_blank">📅 14:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132582">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
لیست مازاد فعلی پرسپولیس به ادعای تسنیم:
🚨
سروش، پورعلی‌گنجی، سرلک، بیفوما و گرا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/132582" target="_blank">📅 14:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132581">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: افشین پیروانی قرار بود به یک کشور دیگر برود نه آمریکا/ او برای رفتن به سفر از من اجازه نگرفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SorkhTimes/132581" target="_blank">📅 14:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132580">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
فووووووووری
🚨
شانس پرسپولیس برای آسیایی شدن زیاد شده و ممکنه با تبصره ماده پرسپولیس راهی آسیا بشه/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SorkhTimes/132580" target="_blank">📅 14:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132579">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🛜
سرویس نامحدود Open VPN
یک ماهه تک کاربره 1T
🛜
سرویس نامحدود وایرگارد
یک ماهه تک کاربره 1T
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/SorkhTimes/132579" target="_blank">📅 13:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132578">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAPUd_o7JnjE-66lf41VR-BlrmHjDXf0D9yZIiiej_NX9gGyJXN9SEo56NFbS1l7u9VDvoWab1GEOwwxnyAEeDb_GwJgpW7b4HuK-40UxrD08sCnE3qjUkiKPVFg1_1nM9IOdZbkIAAaXKAJCxS75uXyA2jkoSkLeyckjIVW_WE17vbGq6UMoqN40Hc7p9yooDwettUwFAsR-4xdcW_XM10KrK9diuXqX3nsLZoTQfoUJEOxMWPu-qbzFdiD3J2FWgN_dCPd2lVWc5iz6n-_JabftfSfsE1ixW0Iu7vapT1ToXdxFoGHY4kicjPxGqG1RSVB01hWKeTNYTHpu_-GDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💭
تقویم مسابقات جام جهانی ۲۰۲۶ در ماه ژوئن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SorkhTimes/132578" target="_blank">📅 13:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132576">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NY8y5myia-llZFePlrUDZ0B0xbRf9ROCWGIimXGi4_J2zmfko9Mmf5d0wqPSjtSuYyALJ7ErD38BbW4wtfpgSi2kSr8mU5W0Tv5pFjVNdtTR8WARQEp12JfNne6ua-j8P7QXbep6GUXDu_HlACFnjSxhp7LdU6alAcUs7uleUKMRjgVMbHXibw0KHbbkqMOKFq2bfAW4hEJImcOyR7XEiCJhwGJKHl9M7y28ZrQglE7ZXstJ9pv1M4xwFLqmIAVSYAgFvhJgB34AT7_99iG2zamz1F03bibieEajorvFjICEjpudV9Uy1X8AT95PKUEnbPGocgZe7TR6hqh9LT5Etw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه سال پیش توی همچین روزهایی؛ پرسپولیس قهرمان لیگ برتر شده بود
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SorkhTimes/132576" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132575">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yh_ov4jX40i7JMdeATHXxi0nc1TKhAeV8zbBTGbkQ7XeB1Vdi-MS8B2mCQtCVKymlR8M-yOLoswTB1r1tiF8jjxcJnkKfJSa5F5DVivXtOARtJF5p2DF0-sI4FVoghFpW9hsm5IDu1JiuOal9b9XIlItWvFI48YNwrlik0DbqBtJrq6KJCmPTkp_9U6UxZJmfX0mDG9xnWEg2rKct-TYonwajQtvKd-VmUxfenZi5tMdG3fs81P2JxdA5tkOrlmSXrTmY7HDhpUjYa2hie8yoRGVu52kQOzykR9JROAvNTAnE4gjJ9jiAWPJn3liCodxzONIhjAruroz1lT8zUt86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
❌
۲ پرسپولیسی در آستانه خط خوردن از تیم ملی
⏺
شنیده می‌شود حضور پیام نیازمند، محمد حسین کنعانی‌زادگان و میلاد محمدی در لیست نهایی تیم ملی برای حضور در جام جهانی قطعی شده اما این احتمال وجود دارد که از بین علی علیپور یا امیرحسین محمودی یک یا دو نفر از لیست نهایی تیم ملی خط بخورند.
✍
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/132575" target="_blank">📅 11:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132574">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwhKVBxWjMev00foFMVNZCCtViWDIz6wLQ6z_yht7qgeXvbq1vl_4DfhPA4L1EfM4d0w52Mnemt0dB5-Kwt3y0dPHwbY2uSEQzG5lXPRy5-1FyvUvvF3n_7s0NIX7bN1TrzhbHx5OriSXWLQOUHHS4eRrssKjpavyhUU_qGif_RHvh82Tm0Duqc9P6dMB9P1OiIWdvQ0fKRfYMOd2UX6xGKPxDbqQpHDEAqcqwGbXDH5XGK0PTrqsRlhh25Bri4Ek8q7mj92gzLBfLExjPPF01ROzJtTGYiDi84Ivwc3dbbntM6-7_BeMmIlw6dA-qiYzIt2LLcPxzWvpytaUedxxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست خرید اوسمار به نقل از فوتبالی:
🔴
اوسمار برای هر پست ۳ تا گزینه معرفی کرده و حتی اولویت‌بندی هم کرده
✅
دفاع راست
✅
دفاع میانی
✅
هافبک
✅
دفاع چپ
✅
مهاجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
‌</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/132574" target="_blank">📅 10:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132573">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
ایرنا: مدیران باشگاه تراکتور با مرتضی پورعلی‌گنجی، مدافع پرسپولیس، برای انتقال تماس گرفته‌اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/132573" target="_blank">📅 10:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132572">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
قول بزرگ وکیل علیرضا بیرانوند به تاجرنیا رئیس هیات مدیره باشگاه استقلال: پنجره باشگاه‌ تون باز شود بیرو بعد از جام‌جهانی با تیم استقلال سه ساله خواهد بست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/132572" target="_blank">📅 09:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132571">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjdphfJHpO-m4jdxWc8c8kPAoCV2S1yoGGwLvFDwVsxiNU9jVLyAxKYB6AdoIhEWVsBLRcAzwglr3095_xTLoWV3PLzrS2igIid5XDmfrvua_O0JataARaVhkdYiKQXrA2Jv0jmZp4p7CvgrwhHj4fm-9LMRTQznUJjZx7M1wJ2oJemF7xcapPXiuwW9kpi0EIZV7nCJjwXOriD011tJNbpITZxw8Q31y1HOcOr679N18V7wwoGOQVkXTz33ENC7BL03o6j9Hika7eCGLHuUiu-u0Gnfdmh3qLILA5kmM8fhNsqvWPGWLutBnSBTdGzdSIZtwhTtBfzrXs7lTrukWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
‼️
هواداران پرسپولیس حواسشان باشد؛
🔺
برخی ایجنت‌های نزدیک به اوسمار در هفته‌های اخیر فعالیت رسانه‌ای خود را افزایش داده‌اند و گفته می‌شود با استفاده از بعضی کانال‌های تلگرامی در تلاش هستند فضای باشگاه را تحت تأثیر قرار دهند و زمینه را برای جذب بازیکنان مدنظر خود فراهم کنند.
🔺
بر اساس برخی شنیده‌ها، این جریان رسانه‌ای از همین حالا کلید خورده و هدف آن ایجاد فشار روی مدیریت باشگاه در آستانه تصمیمات مهم نقل‌وانتقالاتی است. به همین دلیل احتمال می‌رود در روزها و هفته‌های آینده شاهد افزایش شایعات، اخبار جهت‌دار و حاشیه‌سازی‌های مختلف پیرامون پرسپولیس باشیم.
🔺
هواداران باید با دقت بیشتری اخبار نقل‌وانتقالات را دنبال کنند و هر خبر یا شایعه‌ای را بدون بررسی منبع و اعتبار آن نپذیرند؛ چرا که در چنین مقاطعی معمولاً منافع برخی واسطه‌ها و ایجنت‌ها با منافع باشگاه و هواداران همسو نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/132571" target="_blank">📅 09:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132570">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
سپاه پاسداران انقلاب اسلامی دقایقی پیش به کویت حمله موشکی کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/132570" target="_blank">📅 09:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132569">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
به تیم ملی جمهوری اسلامی واسه جام جهانی قراره ویزای ساعتی بدن یعنی واسه هر بازی چند ساعت ویزا میدن بیان بازی کنن بعد سریع باید برگردن مکزیک تازه این ویزا فقط برای بازیکنان و کادر فنی صادر میشه نه افراد دیگه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/132569" target="_blank">📅 09:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132568">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-rG1hANio5FgOfWwt2uA3G9hzTpJckwdQ9V6UG3pxn5GNweSQ2YtzHIOCKnYhbouOdaNzn35S1M4XOfzxZv-HCOAOE9wZazEcVBInlEUWwu5MqBLHu80iEjRiF22WE5nbiO8_8D2dk_8lzFKbR-2H5O9AzyXw1VGqH_iujg3MUUGOZPBlN9JjhdDFy7lcqfZFdN3T0MHQYYjq5iSLDiZfDY0tqSOhbhU8V6yL7kDf36qI854bGBTFfo70OPlM0fMMaUcpDGOyGObhljN0BMgUUzSVdsWFm5QnLDadDn14uRMuVhVlzNNpNYtbhZqgfAZS-RDfP6U1AGxed9q32I5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/132568" target="_blank">📅 01:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132567">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❗️
بین‌گلگهر و پرسپولیس؛ احتمال زیاد پرسپولیس راهی لیگ دو آسیا خواهد شد. اگه اتفاق خاصی رخ ندهد! گل گهر رضایت نسبی خود را اعلام کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132567" target="_blank">📅 01:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132566">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukiYZauRkPNQg4gbhvrC_gW0g_qE4IJO2pBcH6p6GwBPNQXKmurq3B3qfpVyGsb0oZZrq7zo7MSxQ9lnA4FjxfBY1Xp9K2yaofnSGygkDCNzCyDP1Hdhv9QBW_wzEmKUlnroP6dMA2LjXPw8KRxsTP0xn6bCvxoYVGHu7CsgQ6pJX2o5kb_X7aadGY4W937-lRgXOqHu3l2pLvMfSXaxND7ZiYyS2bDrk5RpIRWQa_1bPnwGNcGlB-rq-ZCfzg50H47m1gEKtxKxXWFTkjChe8dj9W50Pakuu8D-DEEC_G1y-AcmyeqOg6MQc5GTleb4jDAgHLQQgGdsuQcLprMU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یه سایت هوش مصنوعی اومده تیم های صعود کننده به مرحله بعدی جام جهانی رو معرفی کرده که تو اینا ایران تو گروه خودش دوم میشه و بالاتر از مصر به دور حذفی صعود می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/132566" target="_blank">📅 01:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132565">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⛔️
پلیس مکزیک گفته بازیکن های تیم ملی بعداز ساعت ۸ شب بیرون نرن چون ممکنه لولو بخورتشون..
😂
🤧
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/132565" target="_blank">📅 00:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132564">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⚪️
مهدی تاج:
فدراسیون فوتبال دارد تلاش میکند که سپاهان از آسیا کنار نرود و اگر سپاهان نتواند پنجره‌اش را باز کند طبق روال جدول لیگ نماینده ایران به آسیا معرفی میشود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/132564" target="_blank">📅 00:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132561">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
شنیده ها :مدیران باشگاه پرسپولیس با مدیران‌دوتیم چادرملو اردکان و گل گهر سیرجان تماس‌ گرفته‌اند تا رضایت این دو باشگاه رو برای رفتن سرخپوشان به آسیا بدست بیاورند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/132561" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132560">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
لیست مازاد فعلی پرسپولیس به ادعای تسنیم:
🚨
سروش، پورعلی‌گنجی، سرلک، بیفوما و گرا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/132560" target="_blank">📅 22:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132559">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❗️
خب سپاهان که مجوز نگرفت. گل‌گهر هم بازی اضافی‌ش حذف میشه و چادرملو هم فاکتورهای لازم برای مجوز AFC رو نداره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/132559" target="_blank">📅 22:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132558">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‼️
امید فهمی مهاجم جوان سابق پرسپولیس به پیکان پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/132558" target="_blank">📅 21:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132557">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
خبرگزاری فوتبالی: استقلال داره لابی میکنه که قهرمان لیگ اعلام شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132557" target="_blank">📅 21:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132556">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
ترامپ: بهتر بود اصلاً وارد ماجرای ایران نمی شدیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/132556" target="_blank">📅 21:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132554">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
اگه تمام نماینده های پرسپولیس در لیست تیم ملی برای جام جهانی باشند چقدر پول گیر پرسپولیس میاد
⁉️
🔴
نماینده های پرسپولیس : اورونوف - سرگیف - نیازمند - کنعانی - ابرقویی - محمدی - علیپور - محمودی
🔴
یکسری از رسانه میگن که الکسی گندوز هم اگه بره جام جهانی پاداش…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/132554" target="_blank">📅 20:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132553">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
ادعای نیمکت نیوز : مهدی لیموچی امروز درخواست فسخ با سپاهان رو داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/132553" target="_blank">📅 20:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132552">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
توییت پزشکیان بعد از خبر اعلام استعفای آن توسط اینترنشنال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/132552" target="_blank">📅 20:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132551">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckj9Y5HsArQnSvmXA9opEQ5v9xClsNmk67PzVjHL8faEcvhZfUmd_Q0fnr7wZH23XM4sJXC2gONU1-IBKMuwQLx5vWKsNVe_zbyCpZLLS_2m6zLTYKgpxL_xDlTrwG7iNXiLU0qE8dUIJWYNUMkGcCSXwvKRyXMt7kTEYX2GVA5xKrB-Z_Da7ldsIhwkqiKovBjsyArJXpKT4UOst1NLOBJv0ryMqR9Z6HVloGcjCrZQ10PR-So7TN8KNY4U8NpYUXdXycA3ewgHpslf28nkIO4hvMMR2tmgJrdE6atkLwaEe_Rfnvf61gAkThSJj5O0kGA9PWDDXV6DGjgn-9rgmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
خب سپاهان که مجوز نگرفت. گل‌گهر هم بازی اضافی‌ش حذف میشه و چادرملو هم فاکتورهای لازم برای مجوز AFC رو نداره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/132551" target="_blank">📅 20:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132550">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hgqtll1ZrGw5439S9nTZ8zHZCpeJPZQy1LKg_YxfefXYFX1Jndc-x4T1iaD-YBPZ4CaYI94RO6QrqBWog3XU8ABzTeiyfwuB1-5YpiIG17syDZ5fWAGQ5HLIp8BsVqCLlWclbyFWGVwxUUcz_Iv_mMwbMymHOGwLPM64EO9N5SzVbpc4v6lMjx3iWwH9nuwmXykG7v4kLolSenaycf6RniwtyDPfXcUvZni3XPGT2fsXQ6tUkkVIGZvExywwQqiGSa18cZ8s4lTgUxET6pP_KcNGSrZrMOitxReN3RtZmFr0JcYibxMSaLu1CywlJUYmN1UjNr_vkRlfINsy9CaehQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توییت پزشکیان بعد از خبر اعلام استعفای آن توسط اینترنشنال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132550" target="_blank">📅 20:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132549">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🟡
سپاهان حذف شد
▫️
گل‌گهر یک بازی اضافه داره
🔸
چادرملو از بازیکن غیرمجاز استفاده کرده
🔴
پرسپولیس برای ۳ امتیاز بازی با ملوان شکایت کرده
⁉️
باید دیگه چه تصمیمی گرفته میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/132549" target="_blank">📅 20:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132548">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
طبق جدول لیگ برتر؛ گل‌گهر با یک بازی بیشتر ۳۶ امتیاز دارد و رده چهارم است. چادرملو و پرسپولیس هر کدام ۲۲ بازی انجام داده‌اند و ۳۵ و ۳۴ امتیاز گرفته‌اند. در صورت معرفی گل‌گهر، قطعا هر دو باشگاه اعتراض خواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/132548" target="_blank">📅 20:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132547">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4MlYUm-9RyMXxpGD8rwDxppZy4myU4QeXuutf6cfpBgrgE5QJ4Dt8eQ4aliaM_B5Mp7SYmq4GgyeoVt4WuYTjdn5hc3LS_ja7dNJkjK4XCvVRHsF5AjBERIc3yXFwSY5n8WOW0BKOk8RqaisZ_mEwo6dNrV2nT8gZX-Eyssg0cXD4p_ArmJoIW-7bsNGLXHInkztO_nTTl8QdHiGMydwG0sohbl_NNxfk7N_gzeuMBrhC7CBsq5SSuVKyUn6q5vccMjUSE3tVCGlB680-7xpINAVZVAfY7gpT2CavkddEP6LjB-zx_DZs6Iub3EPtJqxC1kWhKBN18bLqdlfEUtfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی سریع و مستقیم به وینکوبت
🟢
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی انجام می‌شود:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🟢
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/132547" target="_blank">📅 20:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132546">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
خروجی های پرسپولیس تا به این لحظه :
🔺
سروش رفیعی
🔺
میلاد محمدی
🔺
مرتضی پورعلی گنجی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/132546" target="_blank">📅 19:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132544">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
گل گهر، چادرملو و پرسپولیس به ترتیب به علت حضور در رتبه های چهارم، پنجم و ششم در صورت کسی مجوز حرفه‌ای جایگزین سپاهان در لیگ قهرمانان آسیا سطح دو خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/132544" target="_blank">📅 19:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132543">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فوری
⛔️
‼️
با مخالفت Afc, سپاهان مجوز نگرفت و از آسیا حذف شد
◻️
کنفدراسیون فوتبال آسیا به دلیل اینکه پنجره بارگذاری مدارک  باشگاه سپاهان بسته شده است، مدارک مجوز حرفه ای این تیم را نپذیرفت تا به این ترتیب این تیم از  حضور در لیگ قهرمانان آسیای فصل آینده حرف…</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/132543" target="_blank">📅 19:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132542">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فوری
⛔️
‼️
با مخالفت Afc, سپاهان مجوز نگرفت و از آسیا حذف شد
◻️
کنفدراسیون فوتبال آسیا به دلیل اینکه پنجره بارگذاری مدارک  باشگاه سپاهان بسته شده است، مدارک مجوز حرفه ای این تیم را نپذیرفت تا به این ترتیب این تیم از  حضور در لیگ قهرمانان آسیای فصل آینده حرف شود.
◻️
به این ترتیب حالا  یکی از تیم های گل گهر، چادرملو و  پرسپولیس طبق مدارکی که به ای افرسی ارسال کردند شانس حضور به جای سپاهان را دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/132542" target="_blank">📅 18:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132541">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpLTtLFUvrckJlmCet78irwP921QGkdZSZH0c-CqTnpi2kzzcUSUq7VPWE5KasMv98JI7zwHNQqmHEkC7pYJq7xfWqAx72tKUyT4WhdSel6RGJg0gzhisR9dIVkBWeVT5kcFI0F4SPuV-yD3rcpb1OpT1rTUr9LsD9b1lR2LAzK4HnH0jDQF8frWV7FunF0Ea4sPf0NLDSyrqKq9RW8FzFvbXrfCD0u_6VzHJgD0TNKWIHEpsEJ-OHplr8B0uMf7oUSTK-6P3tm3amEGY9GopJTNK4EKfD_H4vZ9zn0YU-yNwF755jUFRweqK7kZsURKviXos0qNqS6gcAuDhSK-pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سهیل صحرایی، مدافع جوان و آینده دار پرسپولیس، دیروز ۲۳ ساله شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/132541" target="_blank">📅 18:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132539">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
خبرگزاری تسنیم:
◻️
باشگاه پرسپولیس به دنبال جذب چند بازیکن جوان و ملی است تا میانگین سنی این تیم را برای فصل آینده به طور چشم‌گیری کاهش دهد.
◻️
بازیکنانی مانند سروش رفیعی، مرتضی پورعلی‌گنجی، میلاد سرلک، تیوی بیفوما و دنیل گرا از جمله بازیکنانی هستند که به احتمال زیاد فصل آینده در جمع سرخپوشان حضور نخواهند داشت.
◻️
مدیریت پرسپولیس از طریق چند واسطه پیام‌هایی را نیز به چند بازیکن جوان و لژیونر ارسال کرده تا شرایط آن‌ها را برای جذب بررسی کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/132539" target="_blank">📅 17:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132538">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
🗣
حمید درخشان:
🔺
در حق پرسپولیس اجحاف شد؛ در ۸ بازی باقی مانده هر اتفاقی ممکن است رخ دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/132538" target="_blank">📅 17:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132537">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5B5COTfuhgiNQD7NZy30i3HzHhuQYRZ28Myl6jXRtD59dqKJXZA7nGicyziO5mOWougc7e8d7w4IDuCm3fLR6p3svzXUC5V3BLZFVFtisauM8uoB9p3ds8JChZNmYzYWECDegA4Z0M6PrLsU71XacEtfhX2rxbZeeGVExkVcrKXtYWD2T0us4WZaelJXHJ57sUmesed7xZ8nXSqcYkMEjVd12EKgL6Cr5Xx-OEDN1rY2jnMiXJI00hUZuqoXxwLPHKD7FiTfi-1a4oFa98Ad-GhbZQYz1A8nJLSlUlQGj5hwp2VoZWOure7XNLNcuLAHkTn66ldL-pdRNLRc8DmnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قول بزرگ وکیل علیرضا بیرانوند به تاجرنیا رئیس هیات مدیره باشگاه استقلال: پنجره باشگاه‌ تون باز شود بیرو بعد از جام‌جهانی با تیم استقلال سه ساله خواهد بست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/132537" target="_blank">📅 17:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132536">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
خوردبین: تیمی که در ایران مجوز نگرفته چرا به آسیا معرفی می شود؟
🔻
آرزو به دل ماندیم متولیان فوتبال یک بار تصمیمی درست بگیرند. آقایان بگویند این تصمیم را با چه معیاری گرفتند. یک مثال بزنند در کجای دنیا با لیگی که ۹ هفته از آن مانده تیمی را برای حضور در سطح…</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/132536" target="_blank">📅 16:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132535">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
ترامپ: بهتر بود اصلاً وارد ماجرای ایران نمی شدیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/132535" target="_blank">📅 16:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132534">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری؛ با اعلام دبیر سازمان لیگ، ادامه مسابقات لیگ برتر برگزار نخواهد شد و نمایندگان آسیایی ایران بر اساس جدول فعلی تعیین می‌شوند. به این ترتیب پرسپولیس سهمیه آسیایی نخواهد گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/132534" target="_blank">📅 16:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132533">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNJjNVsfJl_2vXyLj0qxPpS7S9G9NmGy9yBiq3sTIyX3RsnIP-wyOBd5HLM8RQyYKzhvYyGYUShua2L95kxnXYchyW0ACe0hrTlYSiAuQtAM25KdqZ0dDumax9eq1Lizeq8GpNzIY30bvWRA5ysXfi2p5z_Kl5kv9gWEn9IZXJPTUZ_oOJUV9oEkPtVLApLgiL2ZyXhUFgo0bMZwZulFOsyakJ8aJkH-Vs6GNcSJ6bUw1BXb4IOeWfYPuJ08xlYuW_QOPPVBOqk75ujVYpbu6pTnd7T55u17FeBu1DrwQdIJEa0nNeLJc4HpJ5oT_ccMxptPGmn4eNP3G-K1mVjQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مایل به تمایل…!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/132533" target="_blank">📅 16:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132531">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CL77qP0j2Oy3abMMZJ9E2Lr3HiVpeiiTamYWQMJ3GOT_2YKP-ue6DW9sMS0oBgl11KK5MLvEt5hgDNgipWErKlya9vnF8bk3FUrd-u_s_NTOa-79DpDC1cV7dt5BUoAQVDDPSucdJePW2YOvoJGY56_SUuUC4hVglYUeb3ykBBY9GRp9ry4_W6luJcu39IVnJfOtzUqPTG8urn_Exrpd6jSQa_HVnW4iY_PCl-3_tmdMNOKJwLhLhxEihPN8xPOeVT2S5LZmQvbFiw2VfNjrX4wZqyhfDDQkBJCitabOgRU5ipXJI_192zJC2ULHQ2Od1CftbO-Iog4aPniB9n2eSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دسترسی دیتاسنتر همراه اول به اینترنت برقرار شد
🔴
اولین نشانه بازگشت اینترنت به دیتاسنتر ها  باید منتظر باشیم و وضعیت بقیه دیتاسنتر ها رو هم ببینیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/132531" target="_blank">📅 15:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132530">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
اوسمار به باشگاه پرسپولیس گفته واسه فصل بعد بازیکن خارجی می‌خواد و از باشگاه خواسته اگه جذب خارجی ممکن نیست، زودتر بهش بگن تا گزینه لژیونر معرفی کنه
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/132530" target="_blank">📅 15:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132529">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=SeXY4KScMq5vHOrSTd4RiYT2fm5R4Ge8_FXFuQZoROt53CNNilq4lhUROIIV0ZWfgaguIi857GaFcWSEGCdON_8z1fFwG5X2JFXc1nADASFvryDLB36zIYUqxiYZGsPEH8PF_f9_ap_bozE1XiCWuq0LapKl8UfJDi5j-pE9RUqGWH6giPjwi5WJ9R_Udr54pTxRkjFqEFxJqwU2CEUEla03KeYQzgSaIqjhGHnzIvht6XVFw4xL_1Gzjsb0mC5IXdF6uanEkbq_qtJBCxpb48p-4tCH8IDPuVcJD-aThChHUZenaGL24PC16ha9pVmQC_5jSOcZX0Lgdch8rQKXhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=SeXY4KScMq5vHOrSTd4RiYT2fm5R4Ge8_FXFuQZoROt53CNNilq4lhUROIIV0ZWfgaguIi857GaFcWSEGCdON_8z1fFwG5X2JFXc1nADASFvryDLB36zIYUqxiYZGsPEH8PF_f9_ap_bozE1XiCWuq0LapKl8UfJDi5j-pE9RUqGWH6giPjwi5WJ9R_Udr54pTxRkjFqEFxJqwU2CEUEla03KeYQzgSaIqjhGHnzIvht6XVFw4xL_1Gzjsb0mC5IXdF6uanEkbq_qtJBCxpb48p-4tCH8IDPuVcJD-aThChHUZenaGL24PC16ha9pVmQC_5jSOcZX0Lgdch8rQKXhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪
︎ اگه این روزا سایتا سخت لود میشن، ربات تلگرام وینکوبت خیلی کارو راحت کرده:
👇
🤖
@Wincobet_bot
بدون اینکه از تلگرام خارج شی میتونی مستقیم وارد بخش بازی‌ها و کازینو بشی، پیش‌بینی ثبت کنی و حتی واریز و برداشت انجام بدی.
▪
︎حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر باز میشه:
👇
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/132529" target="_blank">📅 14:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132528">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
مدیرعامل آروان کلاد: از نظر فنی همینطوری که میشه توی یه لحظه اینترنت رو قطع کرد؛ همینطوری میشه تو یه لحظه هم وصلش کرد. زمانبر بودن بهبود وضعیت اینترنت از نظر فنی فقط بهانه ست. وضعیت اینترنت در حال حاضر بسیار ناپایدار و ضعیفه و اصلا به شرایط قبل از جنگ برنگشته.…</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132528" target="_blank">📅 13:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132527">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
قـلعـه نـویی امروز لیست اسامی ۵ نفری که قراره خط بخورن رو میده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/132527" target="_blank">📅 12:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132526">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
امیر قلعه‌نویی:
👍
دو سه شبه که از بس به فکر چیدن لیست تیم ملی هستم، نخوابیدم. راستش رو بخواهید، هر چه تا امروز خواستم نشده، ولی خداروشکر. من به این تیم ملی امیدوارم، هرچند مشکلاتمان خیلی خیلی زیاد است.
👍
این روزها برای انتخاب نفرات واقعاً روزهای سختی است.…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/132526" target="_blank">📅 12:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132525">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز
🔴
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس شایعات منتشر شده در صفحات مجازی صحت ندارد و مارکو باکیچ فصل آینده در پرسپولیس توپ خواهد زد؛ و بند مشروط قرارداد باکیچ فعال شده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/132525" target="_blank">📅 12:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132520">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
ترامپ: ایران باید قبول کنه هیچ‌وقت سلاح هسته‌ای نخواهد داشت
🔴
تنگه هرمز باید فوری باز بشه و عبور کشتی‌ها بدون هیچ محدودیتی انجام بشه. هر نوع مین دریایی هم باید کامل جمع‌آوری یا نابود بشه
🔴
کشتی‌هایی که به خاطر محاصره متوقف شدن می‌تونن برگردن به مسیرشون و…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/132520" target="_blank">📅 10:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132519">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
سپاهان به بازیکناش اعلام کرده فصل آینده با کمبود بودجه روبه‌روئه و احتمال فروش چند ستاره این تیم بالاست؛
🔴
پرسپولیس و استقلال هم می‌خوان از این فرصت استفاده کنن و برای جذب بازیکنای کلیدی سپاهان وارد عمل بشن...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/132519" target="_blank">📅 10:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132518">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
زمزمه هایی شنیده می‌شود که امیر قلعه‌نویی پس از جام جهانی از تیم ملی جدا خواهد شد و یحیی گل‌محمدی گزینه اصلی جانشینی او است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/132518" target="_blank">📅 10:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132516">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
سهراب بختیاری‌زاده از وقتی فهمیده استقلال بدنبال سرمربی جدیده شاکی شده و میخواد استعفا بده !
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/132516" target="_blank">📅 10:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132515">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
عضو هیئت رئیسه فدراسیون فوتبال: تصمیم فدراسیون بر ادامه لیگ است/ منتظر رای استیناف درباره سپاهان هستیم
◻️
رحمان سالاری عضو هیات رئیسه فدراسیون فوتبال، در خصوص تصمیم اعلام شده توسط سازمان لیگ:
◻️
اینکه لیگ تمام شده اشتباه محض است.
فدراسیون فوتبال به دنبال این است که لیگ را ادامه دهد حتی اگر لیگ هم تمام شود ما قطعا قهرمان را اعلام نمی‌کنیم.
◻️
براساس مصوبه سازمان لیگ و با موافقت فدراسیون فوتبال
ما ۶ تیم اول را به آسیا معرفی می‌کنیم و براساس دریافت مجوز بهترین تصمیم را می‌گیریم
اما با این حال اگر تیمی موفق به دریافت این مجوز نشود، تیم بعدی جدول که شرایط لازم برای حضور در آسیا را داشته باشد، می‌تواند جایگزین شود.
◻️
ما به دنبال این هستیم که بهترین تصمیمات را بگیریم که حق تیمی ضایع نشود.
در خصوص تیم سپاهان منتظر نتیجه کمیته استیناف هستیم و بعد از نتیجه این کمیته باید منتظر نتیجه AFC بمانیم که ببینم این موضوع قرار است چطور پیش برود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132515" target="_blank">📅 10:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132513">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_MfjphfRjOsCv_w7nZCEiafN_b3CEd0-kV5sK7I1HFCv51uIVrUu2oHMMAtjK4fJldglap2zzYSomPpkrm7quwE3EdZNLTvFfY0pIDzQp6tQyIALDVxMmt4Kg6Krug2V8ywXSF_ZvAPg3aVnNxqznC7xofkewQKfM_pS_qHbA0gkmsnKwLBAgZ3QTYqYY1FHRTirPoROvgIyy5J7v3CQ4iSsF9C_etHpmYg8tPbyHevXRL9C8xneZ4QjwmQVaUAmdKlt5TfapxbXji2qs404L5YVwxoQt_t_H4x1uajj--_ffaCj9JN9gQ6vHzdeNoe4gI9u6E4kO_-4NDTLmYulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⛔️
ورزش سه: حرکت غیر ورزشی تاج
‼️
🔴
در جلسه کمیته استیناف برای بررسی مجوز حرفه ای باشگاه سپاهان، اعضا دو بار (صبح و بعدازظهر) به این نتیجه رسیدن که اعتراض این باشگاه رد شده و مجوز حرفه ای صادر نمیشه
◻️
اما مهدی تاج، رئیس فدراسیون فوتبال، با اصرار و فشار شخصی خواستار صدور مجوز شده
دلیل اصرار تاج، قول دریافت 250 میلیارد تومانی از کارخانه فولاد مبارکه اصفهان برای تیم ملی هست در نهایت، کمیته استیناف همچنان مخالفه و پرونده معلق مونده
👀
‼️
🔥
رئیس کمیته صدور مجوز تهدید به استعفا کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/132513" target="_blank">📅 09:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132512">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
قهرمانی دراماتیک پرسپولیس تو فصل ۸۱-۸۰ رو ببینید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/132512" target="_blank">📅 09:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132511">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز
🔴
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس هنوز باشگاه وارد نقل و انتقالات نشده و منتظر اوسمار هستند!
♦️
لیموچی و هر اسمی که به گوشتون خورده در حال حاضر هیچکدوم شون صحت ندارن و تا این لحظه باشگاه هیچ مذاکره ای با گزینه…</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/132511" target="_blank">📅 09:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132510">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
محسن خلیلی: باشگاه پرسپولیس حق دارد از حق و حقوق خود به هر طریقی دفاع کند
◻️
متأسفانه در روزهای اخیر شاهد آن هستیم که برخی افراد از طریق مصاحبه‌های رسانه‌ای و به صورت غیررسمی درباره نمایندگان ایران در مسابقات آسیایی اظهارنظر می‌کنند. این درحالی است که طبق بخشنامه AFC، فدراسیون فوتبال ایران برای معرفی نماینده های ایران به آسیا تا روز 9 تیر فرصت دارد و باشگاه پرسپولیس حق قانونی خود می داند که فدراسیون تا آن زمان برای انتخاب و معرفی نماینده های ایران صبر کند. چنین رویه‌ای و اقدامات این چنینی به هیچ وجه حرفه‌ای نیست و می‌تواند باعث ایجاد ابهام و سوءبرداشت در افکار عمومی و میان باشگاه‌ها شود.
◻️
اعلام رسمی نمایندگان فوتبال ایران در رقابت‌های آسیایی، باید از مجاری رسمی و مکتوب انجام شود. طرح این موضوعات در قالب مصاحبه‌های شخصی، نه تنها کمکی به شفافیت نمی‌کند، بلکه می‌تواند موجب بروز حواشی غیرضروری شود. باشگاه پرسپولیس حق خود می‌داند که موضوع مطرح‌شده را از مسیرهای قانونی و حقوقی پیگیری کند تا از حقوق و منافع این باشگاه به طور کامل صیانت شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/132510" target="_blank">📅 09:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132508">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awVR8vcgI8dxoWJBAz1cWUULFKR_SRanJkw9BUi2eurHTNdwdIPpurpo5I8rELlWhiV-z_dZxheiaPEeQchmuPAAOpC518LC6X11qZsnaXUYs0wCdQOELm5w-5l3MmZmTXJGKAHsT6_DXMpnKvInDtUByQKsBHAFyLIS9aZO1EzSQpMCDxuu0ft2zsc8Wor0TRjr3RZrjjd2U2_RIySb_Xjge2-tRzWF_pV12MNvdVP4mxsjczrQk6S8pA7OgMMYMsLWLvi3GXEg-to2GWn761ZOhkAMCJOD5-GWWmkheax4ScJqG_8PLJ3snXBIoUQ097rxYulRkU2fPh7tGeCs3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت فعال شد!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/132508" target="_blank">📅 00:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132507">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
در پی فشارهای تاج بر کمیته حرفه‌ای سازی برای تایید مجوز سپاهان، مصطفی زارعی مسؤول این کمیته تهدید به استعفا کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/132507" target="_blank">📅 00:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132506">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
کمالوند سرمربی خیبر شد!  پ.ن و. احتمالا پنگوین (مهدی رحمتی )سرمربی کیسه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/132506" target="_blank">📅 00:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132505">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=Wk6bJ76jWigSYURjD2F-KTP0kHyoPO-848-8YV5ATMq_oG1l1kEXhSaj8rJj0jIGYfmCUOyaqR7nwAXNUOkOQ-90RFtR-XEXbdRxZvaUOD8vNLGJ0GYzL5rp-bhFuvlja1QzxJPQEnAKN7Swud0Su2HX4YUW16lRL3vVNTvMhjWu9cV5A5j_ZdeFm2AEv-p_2dStQY0aZ4R7U2dl9Tt6GgJgtHtRhkQFJPiITkkVd2ErnccI02B7mxr5-7D08DTBjWffKHfYLXHTsiZmmezCm5D9AnM7gcaPA2VZaugBeNQlAx4NQgf4Kq4Fgm6WjsfiJGKQVNmdpU6qaCMerrM9iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=Wk6bJ76jWigSYURjD2F-KTP0kHyoPO-848-8YV5ATMq_oG1l1kEXhSaj8rJj0jIGYfmCUOyaqR7nwAXNUOkOQ-90RFtR-XEXbdRxZvaUOD8vNLGJ0GYzL5rp-bhFuvlja1QzxJPQEnAKN7Swud0Su2HX4YUW16lRL3vVNTvMhjWu9cV5A5j_ZdeFm2AEv-p_2dStQY0aZ4R7U2dl9Tt6GgJgtHtRhkQFJPiITkkVd2ErnccI02B7mxr5-7D08DTBjWffKHfYLXHTsiZmmezCm5D9AnM7gcaPA2VZaugBeNQlAx4NQgf4Kq4Fgm6WjsfiJGKQVNmdpU6qaCMerrM9iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های امشب عادل فردوسی‌پور در آپارات اسپورت بعد از مدت ها برای گزارش بازی فینال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/132505" target="_blank">📅 00:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132504">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فوووووری
🚨
مدیران باشگاه پرسپولیس در مذاکرات با چند بازیکن جوان شکست خورده اند و موفق به‌ توافق با بازیکنان و باشگاه های اونا نشدن/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/132504" target="_blank">📅 00:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132503">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
سپاهانی‌ ها از بهمن‌ماه سال گذشته دیگه دریافتی نداشتن، از طرفی مدارک مالی هم بارگذاری نکردن و گفته شده استیناف رای به عدم اخذ مجوز حرفه‌ای این تیم داده اما تاج همچنان داره براشون زور میزنه
✔️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/132503" target="_blank">📅 23:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132502">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bc9aa4117.mp4?token=QQEQyqrvD_DplyWGIiZx6hwQAsYVVq0oDFcFjheOgGHSwIQKTQMOVErKXG-89ywg1cfF0hcPB5KFP7t27cGvrMW3dpPL407qJWjwoaUZqAFc5zOhV4bselE7aLditR-KLXJEVA0jTUEMXKVDNp4SAbm4N5r_vgM0bPQFSU8ArJhibxPuVqK7lQ9Yg7pDw1cOenmvUtG5OcdNZ8KLdMEwtUyORlgJLGJOk4VkK-Dk2-GEpczrFXBEtbeQEb5tmgCDoqqNP5UPPBT03Jx4BEmGa0tdYfwM5guI_O4c3OP18mQ8gN5Pu9us2nayIHDGRXN3EM2_DNT2Fes2K8xj7nqNpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bc9aa4117.mp4?token=QQEQyqrvD_DplyWGIiZx6hwQAsYVVq0oDFcFjheOgGHSwIQKTQMOVErKXG-89ywg1cfF0hcPB5KFP7t27cGvrMW3dpPL407qJWjwoaUZqAFc5zOhV4bselE7aLditR-KLXJEVA0jTUEMXKVDNp4SAbm4N5r_vgM0bPQFSU8ArJhibxPuVqK7lQ9Yg7pDw1cOenmvUtG5OcdNZ8KLdMEwtUyORlgJLGJOk4VkK-Dk2-GEpczrFXBEtbeQEb5tmgCDoqqNP5UPPBT03Jx4BEmGa0tdYfwM5guI_O4c3OP18mQ8gN5Pu9us2nayIHDGRXN3EM2_DNT2Fes2K8xj7nqNpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗼
لحظه قهرمانی پاری‌سن‌ژرمن در لیگ قهرمانان اروپا با خراب شدن پنالتی گابریل
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/132502" target="_blank">📅 23:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132501">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
🏆
فینال لیگ قهرمانان اروپا| انریکه جام را از آرتتا ربود؛ پاریسی‌ها در ضربات پنالتی برای دومین بار متوالی قهرمان اروپا شدند
🇫🇷
🔴
آرسنال یک (٣)- پاری‌سن‌ژرمن یک (۴)
⚽️
گل آرسنال: هاورتز
⚽️
گل پاری‌سن‌ژرمن: دمبله  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/132501" target="_blank">📅 22:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132500">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
بازی رفت به وقت های اضافه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/132500" target="_blank">📅 22:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132497">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
گلللللل اووول آرسنال به پاریس توووسط هاورتزز دقیقه 6  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132497" target="_blank">📅 21:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132496">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
گلللللل اووول آرسنال به پاریس توووسط هاورتزز دقیقه 6  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/132496" target="_blank">📅 21:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132495">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
به تیم ملی جمهوری اسلامی واسه جام جهانی قراره ویزای ساعتی بدن یعنی واسه هر بازی چند ساعت ویزا میدن بیان بازی کنن بعد سریع باید برگردن مکزیک تازه این ویزا فقط برای بازیکنان و کادر فنی صادر میشه نه افراد دیگه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/132495" target="_blank">📅 21:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132494">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⚪️
باشگاه پرسپولیس سازمان لیگ را به مناظره دعوت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/132494" target="_blank">📅 21:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132493">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqg3RQZVC3EXsplbGB0h_KK7Wrq__ZFt1X4TxsIy4NoBrO74uz18al344BSh24Uan66qwEnk23K9IzaWyLxCe0dntjNlccYo3blykPyITVJuNcjRZxKIBDC2Qh7cGRcdRnvayOcSBbyrEangbMBDM3qefCt5feRCbLFZHQdSpTBnLoUcZ4Zg5t5pSil7X-LbJMJooZRu8bO7-T7kvcbdmTrjyJE-7BYa8FrYe7RL7gwgepIB7UqUkhYsOZMgI4r31imNX0kO9GisPYVCMC2q6mv0yBvkJxOl7Wk-p1Rg9aIu75zudfUCMFMFDeK_a9Jk1pIS_hedu_WXAEMsasqXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
Champions League - Final
🔵
PSG -
🔴
Arsenal
⏰
Tonight 19:30
🏟
Puskás Aréna
ربات تلگرام وینکوبت تو این شرایط که اینترنت زیاد قوی نیست خیلی خوبه، چون کل سایت داخل خود تلگرام اجرا میشه و دیگه لازم نیست هی بین سایت و VPN درگیرشی:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
به کاربرانی که تا قبل از نیمه دوم بازی در وینکوبت ثبت‌نام کنند بونوس ۱۰ چرخش رایگان کازینو با جوایز نقدی و شانس بالا تعلق میگیرد.
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/132493" target="_blank">📅 20:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132492">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a6f96dc5.mp4?token=Ycuc2maoapCLl4p6jzUCgjgcEx6SQI1PvUXq-L5ILg26ju5kXqel2k4WxfUK_lVH2IhVIzntNur0Pa1LIsXdo4hZac2yvN_pOEP5eYGbmjnYKuzmhVXNBLLal-Nfbvqw3QhAHeTUsYNSNP_r1wCpeV7vxmuFaQnw7OuuDCFpS1nPT1IGuKi3qND-gvxltBqUyKZMUatU98HEGjzNL0pVC3lunhoDpgj5XxOlQfr2hEierEoScRccDokQ4v2J-BBfw6j0TsJVPKa57x41L4JY6PMn_khDGw9L3aTI-Y54xBDGu3_Ptq-CkxcgqLASahVzYHe8Bb5_wYORg2tmLaQAkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a6f96dc5.mp4?token=Ycuc2maoapCLl4p6jzUCgjgcEx6SQI1PvUXq-L5ILg26ju5kXqel2k4WxfUK_lVH2IhVIzntNur0Pa1LIsXdo4hZac2yvN_pOEP5eYGbmjnYKuzmhVXNBLLal-Nfbvqw3QhAHeTUsYNSNP_r1wCpeV7vxmuFaQnw7OuuDCFpS1nPT1IGuKi3qND-gvxltBqUyKZMUatU98HEGjzNL0pVC3lunhoDpgj5XxOlQfr2hEierEoScRccDokQ4v2J-BBfw6j0TsJVPKa57x41L4JY6PMn_khDGw9L3aTI-Y54xBDGu3_Ptq-CkxcgqLASahVzYHe8Bb5_wYORg2tmLaQAkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گلللللل اووول آرسنال به پاریس توووسط هاورتزز دقیقه 6
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/132492" target="_blank">📅 20:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132491">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
شایعه حضور تارتار روی نیمکت پرسپولیس از کجا آب می‌خورد؟
💸
یک دلال با سوءاستفاده از شرایط جنگی و شایعات درباره بازنگشتن خارجی‌ها ، پیشنهاد داد در صورت نیامدن اوسمار ، تارتار سرمربی پرسپولیس شود.
⛔️
این پیشنهاد جدی گرفته نشد و مدیران پرسپولیس قصد دارند همکاری…</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132491" target="_blank">📅 20:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132489">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❗️
ساعت 19/30 فینال جام باشگاه های اروپا بین پاریس و آرسنال انجام میشه ...پیش بینی شما از این بازی چیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/132489" target="_blank">📅 19:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132488">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhY6__LZrx4Ftp9J6HcaUIXfmrO2vgXy99DEVRoI7Xa_T5Hf9Bfn_tdnoJDJd5AptRaJtBnB3kE040cfhMd4PMV8nA8aUsXJ48aMHEAKmodxIa6WH6GLXAiDl59klcLMD8cYnDkDj4G4DjrEQG7YN-RRdCvap0BXqNFeAMylXnRMw8ZO99mhpSO78tetyoTpOh7x9h5BeOip40usXcTHx70wMEQUQOMX3yALfRuTl0fA8rhxpSnyM-Umvw3KbZDVFTden0YnEpI4LTVH3-81S479UuIEWgpDDRb_0N1Es5Ge6vLc051mRpuCryHK9LDLMADGHfCejC7EMppM7JXeVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
باشگاه پرسپولیس سازمان لیگ را به مناظره دعوت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/132488" target="_blank">📅 19:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132487">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkZ5BNFJBvi2_hmElX1rOS_PxxnJgzSHszYKc9wvArf7HP0hSrM0DEDJm3YzdP4fLUUupErD06a-NShTUxIKk00MXi_JJOC6lbzElrr516rD9NuHQA_-XxT-g27m91AvTmLTOgXQ9TmZ09MjTMsOf8F6hPnL4Y1elOLZRg0G5c8uw9glUmGZ9L7E0_X1uWTN74oIMqA1q15QCUwhsfoTTvHTT-Z8SoVGdljfF2CxV9QXm28b_s2trC-4N-iYmn1AWp9A07KpJpnAbcLrDwHQ80hVq7XKxurMI3-J1a8kM7S-W6cHd8-kWlMRF1-DWhNBlmcOuWB0brqkT7gN_t_XPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری؛ با اعلام دبیر سازمان لیگ، ادامه مسابقات لیگ برتر برگزار نخواهد شد و نمایندگان آسیایی ایران بر اساس جدول فعلی تعیین می‌شوند. به این ترتیب پرسپولیس سهمیه آسیایی نخواهد گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/132487" target="_blank">📅 18:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132486">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
مهدی لیموچی با مدیران پرسپولیس به توافق رسیده و به زودی با اتمام قراردادش به جمع سرخپوشان پایتخت اضافه خواهد شد/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/132486" target="_blank">📅 18:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132485">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
ساعت 19/30 فینال جام باشگاه های اروپا بین پاریس و آرسنال انجام میشه ...پیش بینی شما از این بازی چیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/132485" target="_blank">📅 18:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132484">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
اولین بمب تابستانی پرسپولیس؟
🔴
ادعای سایت هفت ورزشی؛ اگر اتفاق خاصی نیفتد آریا یوسفی را باید اولین بمب تابستانی باشگاه پرسپولیس برای فصل آینده لقب داد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132484" target="_blank">📅 18:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132481">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
امیر عابدینی: فدراسیون هر کاری می کند تا سپاهان به آسیا برود؛ لیگ باید ادامه پیدا کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132481" target="_blank">📅 16:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132480">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
اوسمار کراش زده رو آریا و لیموچی و حزباوی و باشگاه در تلاشه برای جذب شون راهی پیدا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132480" target="_blank">📅 16:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132479">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⁉️
⁉️
نت بلاکس: سه ماه پیش در چنین روزی Iran دسترسی به اینترنت جهانی را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با فیلترینگ شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/132479" target="_blank">📅 16:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132478">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ec1381c4.mp4?token=VouWJLMUaWldwphiV2xWCsfTU-J-Q9kBUWUT4PCs4Dxew8CVhMwEYTMoP5fq4GFa0fLFtZtVyvVSZMOCM5vnDkLj-fiy27ouN1sJiK7-YNI5XG8y5a5knxukpql0NgeRdb1NdIIpiGsto5FalsOinPa78EH-oB7fxwhQ1RTyjzLC3295fZrg_xJo-o4L81W0g8AajBVYso1Pj6PVnnbNh4vVnPM_MUD7SppUUBOOsF4o0GzvorJgylN95bs1U-FkPqarpzuiF5V477zbNgx15sniOOg1uGkf0_G69_1na02mpSHCQ8wyJQeQNAyAXilQwOj1CFwHBReF5_Jc_T2WEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ec1381c4.mp4?token=VouWJLMUaWldwphiV2xWCsfTU-J-Q9kBUWUT4PCs4Dxew8CVhMwEYTMoP5fq4GFa0fLFtZtVyvVSZMOCM5vnDkLj-fiy27ouN1sJiK7-YNI5XG8y5a5knxukpql0NgeRdb1NdIIpiGsto5FalsOinPa78EH-oB7fxwhQ1RTyjzLC3295fZrg_xJo-o4L81W0g8AajBVYso1Pj6PVnnbNh4vVnPM_MUD7SppUUBOOsF4o0GzvorJgylN95bs1U-FkPqarpzuiF5V477zbNgx15sniOOg1uGkf0_G69_1na02mpSHCQ8wyJQeQNAyAXilQwOj1CFwHBReF5_Jc_T2WEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
محسن خلیلی، سرپرست پرسپولیس: وقتی پیراهن تیم ملی را میپوشی، سرود ملی را هم با افتخار بخوان!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/132478" target="_blank">📅 16:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132476">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
🔴
وقتی قرمزآنلاین فاش کرد محمودی از سوی ایجنت ها محاصره شده و برای تمدید قرارداد هر هفته یک ایجنت را به باشگاه فرستاده متهم شدیم به حاشیه سازی اما انچه گفتیم حقیقتت بود.از او خواستیم مراقب باشد.محمودی از برترین استعدادهای فوتبال اسیاست.
🔺
احسان خرسندی، سرمربی…</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132476" target="_blank">📅 15:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132475">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
باوجودی که فدراسیون فوتبال رسما اعلام کرده بود موافق برگزاری مسابقات شش جانبه است اما در تصمیمی ناگهانی و عجولانه، بر اساس جدول نصفه نیمه و ناقص، نمایندگان آسیا رو معرفی کرده!!!
🔴
سپاهان که قطعا مجوز حرفه‌ای نمیگیره ولی جدی میخوایین گل‌گهر یا چادرملو رو بفرستین…</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132475" target="_blank">📅 15:40 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
