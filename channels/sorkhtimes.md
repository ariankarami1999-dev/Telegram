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
<img src="https://cdn4.telesco.pe/file/GRGrhHHtuc-75E_VRfNE_oNnHPy1vM_gEmDdMet82tWWginGHdrFrEhciSS1f4pAkYw73p4t_7xYaE0vWr0E46sZ67PquX1ZUf6aLsXLTkm0OudMSwK7PPWwaXpCovTaepF8uXxt6X53k88KITiShp7N-I02M7a-P0W-4crm9Utd_wBattmYX4I_YoP2YVbsFTOedN155LT-JISGF9oSnMGm8q6T-2gRQgbmaAfSI97GW1MKlIBGCJ_xM_gd7GHY1EltHCatHBc7OnLhEukM9OCXiR-mCBCe9eCWf4XUcqdWK3XinejiXKhVlwheHRYnFeeFI3WBZpO4paU08izI6w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 20:59:37</div>
<hr>

<div class="tg-post" id="msg-140361">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyO4Huj436f_UnGZTWRHVFolWtrJ6yQLBiGTdUl3pBDYtpufqLJrn23nXN1nA4rpusM4fq5pZPvEv7my4nmI2m8sx1cvsNHKRTmjT2Oz2NmAW-bBJo4xTwaLQlo4O_yfwOg-JsDELWGNTkUVMi30R-LGwM0MZ3n8D3_OGZ5C0c0DHP1u0W46mf45yBBd8SSQLPY9HBseeh-zUGW3SEJsN0q8GTbhqMTeHCPedURhnypILOfVe1Za7H4P0JrbkkITK4KspNJB0uQk96-2rtZ30LkZeqUfWRL5bMBYyNdJJM8kYDSLa3EunJiRyTowgShVuu7HAj7Z410L5eLARbpsSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرحله حذفی جام ملت‌های والیبال به اوج هیجان خود رسید!
🏐
نبردی حساس و تماشایی بین اسلوونی و صربستان در پیش است؛ جایی که هر دو تیم با تکیه بر قدرت سرویس، دفاع روی تور و بازی تیمی، برای کسب برتری و نزدیک‌تر شدن به هدف خود به میدان می‌روند. دیداری که می‌تواند با رقابتی نزدیک و ست‌های نفس‌گیر همراه باشد.
🏐
اوج هیجان همراه با اسپورت‌نود، دوشنبه ساعت ۲۲:۳۰ دوتیم اسلوونی
🇸🇮
-
🇷🇸
صربستان به مصاف یکدیگر می‌روند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 974 · <a href="https://t.me/SorkhTimes/140361" target="_blank">📅 20:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140360">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
🇨🇬
تیوی بیفوما به علت مسائل سیاسی کشور کنگو و در حمایت از مردم، دعوت تیم ملی فوتبال رو رد کرد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SorkhTimes/140360" target="_blank">📅 19:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140359">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
تیم‌ملی امید فوتبال ایران در دومین بازی از مرحله گروهی بازی‌های آسیایی برابر چین با تساوی بدون گل متوقف شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SorkhTimes/140359" target="_blank">📅 19:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140358">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
با ‌درخواست تیم ملی علیرضا بیرانوند تا نیم فصل اجازه بازی خواهد داشت تا در جام ملت ها آمادگی داشته باشد سپس به سربازی میرود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/SorkhTimes/140358" target="_blank">📅 19:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140357">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGYGTqYu7OITRtjUogX1K_RA2WLOEa5woE6iOHx9OKV7DNbVMYDAEMkoKlxlh6VY7y49axctbkUwO3maojjMa1GbgN7SBxTYT-po_BY2tL8ZSMoyi39K3gseKyy_yC6uZ-oZFHcxwGI0pw0po7aAABploPItOm9YiKf2-dYvL1v_MiJHbNJv55J00eZZtBJ5ld3tYOBL1KmkzvpNVytSU0ICZKzv3zWD8IPOheJ8DrR5sny6xnuL37hNRF-ezmVZGpLXtQCzoBjoRlaDJryUeiYgn43j63XsM7MbtcuxhOKBwQacM69zhZjAW_Qlw6nf-nnUzGxrwSiGUw9GDzuDEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حمید کرمی مدیر اجرایی تیم پرسپولیس شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SorkhTimes/140357" target="_blank">📅 19:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140356">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری از فوتبالی
🚨
سازمان لیگ کارت بازی علیرضا بیرانوند برای تراکتور را باطل کرد.
😅
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/140356" target="_blank">📅 18:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140355">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISCDrW7KtoSXuFXZl4DWvmEWyIdn21cs5Uo7l_PG2K2gSpRxBsXpkyR36pEb8qBwtPbIPv3k12vuOnJSGGv0CErf8C35CPN3ikxcgqwjoTSqfqbgQNUQRZVFMPqREFglvrT1sy22Jaoru7KT1B_MKMDDWPAmnbCo7V8UfvnmpiZJ_9K5GSoOuQxEHgiOwQgnvEJs5DC66_t3CtF3p1hRlmOuNcM-yS7pqoREncqUuLhy6sY-xmsR7tVT74RoUuEOpycRVxE2Bg-QyzVGByvMKy5wwSVlNh_xzfWgCqxaP3iveASWdMv6_i4fUBqyS35Yud2DfvQfC4myu1DyqoUoUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری از فوتبالی
🚨
سازمان لیگ کارت بازی علیرضا بیرانوند برای تراکتور را باطل کرد.
😅
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/140355" target="_blank">📅 18:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140354">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/140354" target="_blank">📅 18:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140353">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbMAXl3cvxfCdmnmDVGvjZhDSCFQBaY4g6yZLVuoXazNFXMR1yXsehLJUxzjv-mrKBCI98Cfj3J_o0iDfCcCNBLg7AAthJD1TCHYkUD9qwra_L_zo8RJiNWFItsYZet0ZhZ9Eaf7nRke58JVay0VF02BlnX06WaFLxGDMl5G1_1TVA4UhNYPO3M5Rsu5Ya_IubTIGNZnfMusdfHRahakzvJU6xppSmZl3ukomeDKfrgTqBlqZNYUGIE8h5vPY7nYQbHhC4hWS3KGwt8H-gsK7yaiSv155dDaoc1zqUbHjkXdjf51fPIuoTLTVMVlwmxvHX5rv3oofYBddT6gzQaXPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بسته شدن پرونده حقوقی بانک گردشگری علیه پرسپولیس
🔺
باشگاه پرسپولیس با انتشار اسنادی، خبر از تسویه بدهی این باشگاه به بانک گردشگری خبر داد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/140353" target="_blank">📅 16:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140352">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✔️
✔️
میلاد محمدی در آستانه دیپورت از لیگ بلاروس!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/140352" target="_blank">📅 16:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140351">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
پیگیری‌ها از مسئولان باشگاه پرسپولیس نشان می‌دهد که هیچ پیشنهاد رسمی از سوی باشگاه‌های خارجی، چه از قطر و چه از سایر کشورها، برای جذب محمد عمری به باشگاه پرسپولیس ارائه نشده است و بحث جدایی این بازیکن صحت ندارد. / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/140351" target="_blank">📅 15:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140350">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
✔️
از باشگاه پرسپولیس خبر می‌رسد مسئولان این باشگاه در مرحله استیناف مدارک جدیدی علیه یاسر آسانی را نیز ارائه کرده‌اند و امیدوارند با بررسی این مستندات، رأی مرحله نخست تغییر کند/ فارس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/140350" target="_blank">📅 15:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140349">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
پیمان حدادی با حضور در ورزشگاه درفشی‌فر ضمن بررسی شرایط آکادمی، با بازیکنان و کادر فنی تیم‌های امید و جوانان دیدار کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/140349" target="_blank">📅 13:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140348">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7sfO0WOyEL9ZxSgS5JonlnHrtM_2nzpc6geZxbtHiAzeuLiWXR7haxEZZxhYlUttMHSirl6OOZpYQbS8TSgivhDWFQRmoJLTbyTJMcFX1d6D6BAxnTX6mn3bADPaDkrOpbJOjtz90j1BG7Ym9b5sS0RrB1URqa9eyfwMwcGrkZtx0ajmHBIayN6AjXKGpdXcEdoKieT5KAdjZvOJ_URIDmhaty5ZcUUjvkIrh43J7E_jRa4-748lCaEJ3WhixM1UNfT5OJZF6WBd2rJM9kl2fNn7vmIHVafdk4mAF6oc6OIOnPLa8TqMCn06x34GSP5aa1XBgxpNw9wQ1BBJyA2ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیمان حدادی با حضور در ورزشگاه درفشی‌فر ضمن بررسی شرایط آکادمی، با بازیکنان و کادر فنی تیم‌های امید و جوانان دیدار کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/140348" target="_blank">📅 13:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140347">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/140347" target="_blank">📅 13:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140346">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2tPtmbq2WaJIHJgvkhLwYyanEToA5PRcjY61u6d8jEFOc0uWwGhYbJMHEZO5L8AsZLr2HJYExcjLQp1LeAWomaVs8rWRNKGD4BGe3UItcvJhspvR6EkqW3sn7ubY9DTquJDmN6Fmi7eJCA5oQuvzv3_3DUHTFij2U7Isd9Lcg8-EZIyCPcpLKZJ_GM_drPLANsuFCMl1MTxUlepPsMv7gvbDAogxUcVu2G849M2lFhxkqiTAACHaHeCDJ0vq-_kWZ8iMXiIS2pQvm8svZkBJNmetdFHmjEftuzJ9WOo2KShvNTzIphSrk1LK_HEs7z9g3XuQvuC7HIlsguKoGwnMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جام ملت‌های والیبال اروپا
🇸🇮
Slovenia -
🇷🇸
Serbia
⏰
Tonight 22:30
🏐
اسلوونی با سرویس و بازی سرعتی از مرکز، تلاش می‌کند دریافت صربستان را از نظم خارج کند؛ نقطه‌ای که می‌تواند جریان ست‌ها را عوض کند. صربستان از نظر قدرت حمله و توپ‌های بلند خطرناک است، اما نوسان دریافتش مقابل تیم‌های قدرتمند می‌تواند دردسرساز شود. با توجه به حذفی بودن مسابقه، انتظار ست‌های نزدیک و طولانی منطقی است؛ احتمال کشیده‌شدن بازی به ست ۴ یا حتی ست ۵ هم بالاست.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدار هیجان‌انگیز امشب رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/140346" target="_blank">📅 13:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140345">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
✅
✅
رونمایی از مدارک جدید پرسپولیس علیه آسانی در کمیته استیناف
✔️
✔️
باشگاه پرسپولیس پس از آنکه شکایت این باشگاه از استقلال به دلیل استفاده از یاسر آسانی در کمیته انضباطی با رأی منفی مواجه شد، نسب به رأی صادره از این کمیته به کمیته استیناف ارجاع داده است. …</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/140345" target="_blank">📅 10:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140344">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
پرسپولیس قراره ۳ ،۴ بازیکن جوانش رو با هزینه باشگاه به چند تیم پرتغالی بفرسته تا تجربه کسب کنن و دیده بشن؛ در صورت انتقال، سرخ‌ها هم از ترانسفرشون سهم می‌گیرن.
❌
فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140344" target="_blank">📅 09:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140343">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
✔️
پیمان حدادی: به‌دنبال این هستیم بازیکنان آکادمی پرسپولیس را به پرتغال بفرستیم!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/140343" target="_blank">📅 09:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140342">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHadJs0KrK9rIZ-Y5aOhMF9Md9ZH3omlVIcZUfiIG6G_6HDkJE9i0WU65CXmXtxXprDzHlwSqMFZbEglovEffGBYLmPeCdMfhmNOmeMsedKzHDJOW2S39IFz5nU4HnZfo7zqM-ICKbDN-WKM4PmpHSaZw4FBzXLqkVyZIwmpxvqm05RvnkrUW9ZNyALDxEFe3_JfqYiANdl3BfeMSAn1QINAM5oVR0zfOd3jYxHfu72pPN3mAVW6gqGjCteODOr292V8WLL6u45YFcoR0suVkwwKcvjNloxtx1RUAbWjLukyGMpGSng5db6IpLC4SPAPPv8rp6U-xOdu7K7sK6YTqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/140342" target="_blank">📅 09:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140341">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esRHlZMCdm8L_YB7RrcJWRURty8_xF7f4s7uG937Ejqc2nGjH3i-DI73iCgOFCg9TctxItP3orezFXmSlSVZY7XebAW_7zoMb-8RRIGZK0kI7TH7-UClspMxaxjGU4GxJwbndSmfPPgsafixhBDe1y0GlCFpViz1xeCLM3eR-hMyC7fjuH-T8zrBKFhkpZAK8mGMaIdjR4HhZiJAawRF_pOEu14pWSgarfTJJqyCSp0pzFpk3fkWXSSZAOmAMrjH2j9DuspKJadslN_bAxoMgrUzSJEmT7_6sQntcr7GIy_T60NhcJbUNF8DgnKi4K5ZgZIwKFQtdaM6M2lLUb1jWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
ربات وینکوبت در دسترس تمامی کاربران
🟢
بدون اینکه از تلگرام خارج بشید میتونید مستقیم وارد سایت و بخش بازی‌ها و کازینو بشید، پیش‌بینی ثبت کنید و براحتی واریز و برداشت انجام بدید.
📌
حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر براتون باز میشه:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140341" target="_blank">📅 02:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140340">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
تاج: بسته شدن مرز عراق مشکل جدی نیست و با AFC مکاتبه کردیم/ عده‌ای با کارشکنی و انجام اقداماتی به دنبال عدم خروج تیم‌های ایرانی از کشور هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140340" target="_blank">📅 00:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140339">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
✅
✅
سرگیف، اورونوف، آشورماتوف و ماشاریپوف از لیست ازبکستان خط خوردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140339" target="_blank">📅 00:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140338">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9814f0d7ba.mp4?token=EhLjFxqogelgq6FxY7XWxA9SiMR_UXovG9Xd-F8qUG51gzIggcUO9FT_HpDxcOMgTH_1EGon26SxE0cYk4wMjCJuFIchLx-CeRPaThwmNOn9aLLc_muPFvtgVutsKX4u11DaIBZSIhYpMb_XbcEcBMViNhNHZxLKJZkm-T748IecZfrJNqK_IWadSZzNVmkpHWW92QFtRraVPd5bhguDSDS0SfbdcdnD4hU8ORtmGFEQUH7svz-XADcf_3B73i5E-W_EhDnGvdNjQGH1QRGF7n2MK1acb3vnKfPOaeNzw0LLaa_TwQPeP8PZDuwuHL_gyRmCtAgwb1XyztJ0JBPlgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9814f0d7ba.mp4?token=EhLjFxqogelgq6FxY7XWxA9SiMR_UXovG9Xd-F8qUG51gzIggcUO9FT_HpDxcOMgTH_1EGon26SxE0cYk4wMjCJuFIchLx-CeRPaThwmNOn9aLLc_muPFvtgVutsKX4u11DaIBZSIhYpMb_XbcEcBMViNhNHZxLKJZkm-T748IecZfrJNqK_IWadSZzNVmkpHWW92QFtRraVPd5bhguDSDS0SfbdcdnD4hU8ORtmGFEQUH7svz-XADcf_3B73i5E-W_EhDnGvdNjQGH1QRGF7n2MK1acb3vnKfPOaeNzw0LLaa_TwQPeP8PZDuwuHL_gyRmCtAgwb1XyztJ0JBPlgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فووووووری و رسمی: وارد فیفادی شدیم و تا 3 هفته خبری از بازی‌های باشگاهی نیست...
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140338" target="_blank">📅 00:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140337">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔄
✔️
✔️
✔️
🔄
سعید دقیقی بعنوان سرمربی جدید نساجی انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140337" target="_blank">📅 00:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140336">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pih8Rx4JsrTYINOALSqcXvv5rk6L55lFM8KnkwJudysQJLZxyYrMLS-UViLI7ZnRkXGZOLtE0-OhXluasM-Xi0rrJkR40BHzuTxVR7TvOQrsdxvBSBgObCyqY0Nt8PkD8L9wc9RcEdUXQ94dewPdX1sQ2nxncAyW1-0CvVjYFTwMNSIuisKhghrnxbNYU1JNZEJHwApCep1kSRdqaQc1ps06uZACaKrmZcZSyuYNU9VWF2e3KFH92f0kFq4-RefJfTsK8Kz0-wUrKhVYuUht6JHnRTHPaNNxC_Wqa2s7w0Lt8cnk9s7vSftev9o-BiTTlDoLB4bC7QQnfOWRJuAdug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
💛
🔥
غوغا کردی امیر قلعه ؛ جوون‌گرایی نوین قلعه‌نویی: ( جمع سن نفرات تو عکس : ۱۰۹ سال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140336" target="_blank">📅 00:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140335">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری؛ ترامپ: تمایل دارم با دکتر پزشکیان در سازمان ملل دیدار کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140335" target="_blank">📅 00:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140334">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔄
دیدار استقلال و تراکتور در هفته هشتم لیگ‌برتر روز پنجشنبه ۱۶ مهرماه در ورزشگاه تبریز برگزار می‌شود. بزودی برنامه هفته‌های آینده لیگ‌برتر اعلام خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140334" target="_blank">📅 00:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140333">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HpBgwTnB5hTZgh5YwXUGi9Mpkgf_N_zSiWciFn1gBy-vgfvgwo4QOTwey6lgAfPtnxtiMkiVkzUG9VvAmK8tG9cE7gvFiZ6sdZXhzVSFC1AtM39_ecAubfWIN5yFuqCSaCJCYj_DiKX_vK_rcQhUild8vY9Yw-QVNLZx0mQ2nInwL_nA2b24Sc5pU2oZvvjSV2MNMiAbFZvustipl9uDkrudMMYRNK2YEplRANNgMmO3J6g15x0lhT7dwQxFgRIHf2RwR6_njc3gikoVOVOXY7zoDHgwXvTEPYWB4OGteBLzWTEwqjrg0REOw_Chywr2ayuRWL_3SpWVjudn_raNhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛎
پپه لوسادا مربی پیشین پرسپولیس به عنوان مربی بدنساز تیم ملی انتخاب شد.
🚨
خبرگزاری آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140333" target="_blank">📅 23:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140332">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJdxeteDII1kJv-u87poPWgFgfX1ArYD0JbkS7ssOmjTSYEe0krQsm94xhrgoEChzwaZ6cqlffM6WnxnUGX5-H8As0icnCN_bz9gI78j3LCngYEIbVNXqR4ExYrK_Z6ADVXAUkato-soOoXsNIZlCmkOH-_7Nh6sK-haPI4hAFlxFi5iWFKb1QHjrU_ZH9k47HkXmGNm2zTAOKt9wkD67V_GAEoI7usuOuVhpiqp_8yKpV6qEJlw3AzjmYc9uPtEA_gHXz3nW0B3xdNbOTlt2VvlOjI8ZVaMsqSOCI_uA63BIAgKIq6GRHWHetWAUaLNeGyXVqAGnQKejPaHv9aosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
مهرداد خانبان به کادرفنی قلعه‌نویی اضافه شد
❌
❌
پس از پایان همکاری آندرانیک تیموریان با تیم ملی فوتبال ایران، کادر فنی این تیم با یک تغییر همراه شد و مهرداد خانبان به جمع دستیاران امیر قلعه‌نویی اضافه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140332" target="_blank">📅 23:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140331">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtOLmX8ggBLenqzb5cVkQ3hDBbhJ1uAcmcCqa71vbB4ZZLClEGrkTtce-kHXLCaM_45dx19VNtA6XH--YUQ5CYanT_JzDNTDLwJqqXVAs_AxNidj5nA612HZpbkFQ0KmtkXP6njXNFNkDM3sULCoZRxzq3_vhb5jUqzWakRnBbkX-xcpet7XsI7ZqMNHwa0qtRRXsyheBIYx6HzZh6fFaK6gx9wUuXP-N4FIC7yqb4qGeoBnFxsSLKmfxsh4Db_-cK1x_6O5nC48WurJ4GTiH-UCqCp6tfdLjhz1t8HZhyu1b5hk5xNT71jntoSoUS3pstybsR3tC6AMs1s2bt5GjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
خبرنگاران عربستانی: کریستیانو رونالدو نیم فصل در انتقال آزاد راهی فنرباغچه خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/140331" target="_blank">📅 22:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140330">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQQH-V7cAGhnKIjoJ9r3vLEQXycx1YxJO3dXsfH-l77NfJJXSEsH_8U9feT_OCFJPf8k7oVpqme2sKTRMl4XH5OaNESOvDRy02i02EM6Y8hCk97RXEB_D8LJ4Xkh8y9Z2LbpkB8n9gY24Z0PfZTNkfKSci4i2qnyKelUgq3io4NU7hCqFRGcY2wI-10jM8SawsLZ0RURFrlnglHc2N7aP03VEX0eY4q8emWBBdbe5Y-5CeAnzXSnGN8-pVaNZUOb9SvlhLVcYs6-0YsbqfzVQ-HsgMAcxQGmL4_wUwpZxCcZaWZjQ22-ui7lvetlOM303VyDCd0bTxeBZ6Djm-z_DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤍
🇮🇷
سردار آزمون با بخشش 5 درصد اموالش به کمیته امداد خمینی به تیم ملی برگشت:))
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/140330" target="_blank">📅 21:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140329">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
فرهیختگان:
🔄
⌛
بشار و فرهان گزینه‌های روی میز تارتار در زمستان؛ پرسپولیس به‌دنبال پلی‌میکر
😀
درصورت تایید مهدی تارتار مذاکرات با بشار رسن آغاز خواهد شد و فرهان جعفری نیز گزینه‌ی دیگر سرخ‌هاست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140329" target="_blank">📅 21:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140328">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
رسانه‌ های عراقی: باشگاه پاختاکور ازبکستان با ارائه پیشنهادی جدید به بشار رسن قصد داره قرارداد این‌بازیکن 29 ساله روتمدیدکنه اما فعلا پاسخ مثبتی به‌این افر نداده. اولویت‌بشار بازگشت به پرسپولیسه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/140328" target="_blank">📅 21:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140326">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSDJII-tTyEIrNmIaCh1dQUlJzvlP8uaT-31QWN7zt7BnsVxYl4TNlZKX9sarJRBafCcAep_OXkgX-bS7TdgWtMFtRe9T6zQV-yZGmVJ8YIXZxqxRS8JwXDdQAl57183QGaoLLgxFpseIpSKfNfmAIvt7y5TjS0L3zdP3pVr5XnSZTspuIZ52zHArWS_HbI3WLgBzXkx8POm4dr3j46nIl9HM5FocAq5_CSK6YNlnhxysBUEEHQ7vglm4AaeyoOLHeOpMWtCv58nDhzhZeliWDPvHvaSvmA20BOKKJMPZwUuyGUJ-XutZS7hGp2QCMupi1ANwBSraKVyawjd3Txsew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
Marseille -
🔵
PSG
⏰
Tonight 22:15
🏟
CEPAC Vélodrome
🔵
مارسی با شروع ضعیف فصل، در ۴ بازی فقط ۳ امتیاز گرفته و ۳ شکست داشته؛ پاریس هم با ۵ امتیاز هنوز در حد انتظار ظاهر نشده است. در ۵ تقابل اخیر، پاریس ۳ برد، مارسی ۱ برد و یک بازی هم مساوی شده؛ آخرین تقابل هم با برد سنگین ۵-۰ پاریس تمام شد. از نظر تولید موقعیت، پاریس میانگین ۱۸.۷۵ شوت و ۶.۵ شوت در چارچوب در هر بازی داشته؛ مارسی به‌ترتیب ۱۳.۵ و ۵ ثبت کرده است. با این حال، ولودروم و حساسیت «لو کلاسیک» می‌تواند بازی را نزدیک‌تر کند؛ انتظار یک بازی پرفشار با موقعیت‌های جدی دو طرف می‌رود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدارهای امشب لیگ اروپا رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140326" target="_blank">📅 21:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140325">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INHrawdY3mfDvm_CeaIPct4NEWoq8VhmctOPD0ADU43eyvq5lRcd_MZNMdEKwMG_BA7VGzwOhwk5II9WeTYFFIkJKIU-w3mOqJqTr8OzeLBqXNPo5U_LA4eSz6jfJvYOrAuiIHcW4UBSHhuCZuw7-u70bImnT202hiluz56ehn6VCPkcTJzXzFkFgZn_sUi8XOahMIOGowJjn1eqkFVUGJj5C2Ib4dW4s3UYBssPOCZkUXAwTC1hpVJIwJfgMzN6WGDa2QabzwVXiIEdUFmcsXTH8IOCQAx1Tjvmfh9qo3G1PtjQVCRQWPFpeOS-PR3-e0csPmR-ZYeanlsqV1MUQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏅
پیمان حدادی با حضور در ورزشگاه درفشی‌فر ضمن بررسی شرایط آکادمی، با بازیکنان و کادر فنی تیم‌های امید و جوانان دیدار کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140325" target="_blank">📅 21:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140324">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
✔️
✔️
✅
تصمیم پرسپولیس درباره اورونوف
✔️
✔️
پرسپولیس فعلاً هیچ برنامه‌ای برای جدایی اورونوف نداره و این بازیکن همچنان در برنامه‌های باشگاه و کادرفنی قرار داره.
✔️
✔️
شایعه انتقالش به تراکتور به‌خاطر نیمکت‌نشینی تأیید نشده و حتی اگر در آینده بحث فروشش مطرح بشه،…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140324" target="_blank">📅 20:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140323">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
❌
ادعای خبرورزشی :
❌
تراکتور به دنبال جذب قرضی اورونوف از پرسپولیس
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140323" target="_blank">📅 20:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140322">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
ادعای خبرورزشی :
❌
تراکتور به دنبال جذب قرضی اورونوف از پرسپولیس
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140322" target="_blank">📅 19:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140321">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcuA9OlGDoyH-mzTYVQ2El8TujcB-ayF_pDWtFDvHjWDeEdPqdXYkRhXB7rOhVeq_Ke7YWtkBedWjDAc_sOwIK8SVe-azUG1fnrumcmCEaaGid1n-UzyAwmxpNJoAKeRB7nPQOfTow8-XcUN4JKae169AhiqlgemO2oigWXqhyW7Q8zEH4iswhxPvC3J52XGZqauGy9RFLmv690MfrlIerzagN9Ly9WNM1pyG4XYB27WkYiZGFl5xVjhoFzlOE2rfn69ehwEl3suqVcIjq_dJ65vwZwKaTwn57Q0ScrfwZJrvyRSXyQ9PpdbkkKp0gLdzq7IY6lMBMPmMSx9XmOVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
گزارش تصویری از تمرین امروز تیم ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140321" target="_blank">📅 19:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140320">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5DW2a5V_uisPO7UT4oB6hPqA52QSxadX1lRvmprsfikp6eJVMIL10MkWvrc59wCZLt9Tb2zG1Paz1tCYZwgmwGD-OXPyjxS8DU3bY_vjshTzVgQLmaYTrPdDSsdEtfYzSvvLCVQsiB2DNeZKTQEM1O8ldVFkdH7JspgojYOux-7UNJdBYbb4Ut2uodFKk9OV-6ujSr1P0XQFLb1vOLqW-ZDD0jjnkzT8I5Dn_7hvT2TeApIWiJhX6jLFYaaEIS4xpzmrf9ymnRyKZDOqZV2IJhoe2FsltbGXeB2bxCcS-x0cNlXQeqA7L6g6LRh7rhcSSGTodVN27kNo0b248NQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری؛ ترامپ: تمایل دارم با دکتر پزشکیان در سازمان ملل دیدار کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140320" target="_blank">📅 18:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140319">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✖️
✖️
✖️
🇺🇸
ترامپ به فاکس‌نیوز:
❌
من می‌خوام با مقامات ایرانی
🇮🇷
مذاکره کنم، ولی چالشی که الان باهاش روبه‌رو هستم اینه که اونا مثل موش تو سوراخ‌هاشون قایم شدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140319" target="_blank">📅 18:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140318">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
فوری ترامپ: آماده حمله دیگری به ایران هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140318" target="_blank">📅 18:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140317">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
فووووووری ...شنیده ها
🔴
قرارداد استون اورونوف با پرسپولیس با دستمزدی ۲.۲ میلیون دلاری تمدید خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140317" target="_blank">📅 18:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140316">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
رسانه های مملکت گفتن آمریکا مجوز لازم رو از چند کشور منطقه برای شروع دوباره جنگ علیه ایران رو دریافت کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140316" target="_blank">📅 17:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140315">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140315" target="_blank">📅 15:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140314">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
❌
صداوسیما: حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140314" target="_blank">📅 15:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140313">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
❌
⭕️
⭕️
فوری/کانال 13 اسرائیل گفته آمریکا و اسرائیل تو تدارک حمله سنگین به ایرانن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140313" target="_blank">📅 15:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140312">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56fa29145b.mp4?token=cEqUUhia_TbkCKy3RlSIIFgi7jn4xqFqNXAGalFdZb7CWtZrf15JRa8Emq8uL-JcTfPE1ErsgXlt-c-LAPETliGpVp7wP_F6malIXVJWmHJu9oTDAOYCjU-KF7xYStX2p8WRA4b7FUWgfLWLCVfeExUgSX5hCBrEHkKC3ASAtBM67igtMXRxyZjhQC_nckPa10Izk5QsD3hIFNKRTuJIQJGPgNl5gdz1xiJgox8x1ZI2g_A6l_xK7Rdz0w1op65CkCCwsRzO2DtRZreyj89nYe0ZmoTGF6UlSJ2t0nIzmcxgbNNc3DFFbHkxNDVcNXlPlbezV20MVgTJ8uQftT47KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56fa29145b.mp4?token=cEqUUhia_TbkCKy3RlSIIFgi7jn4xqFqNXAGalFdZb7CWtZrf15JRa8Emq8uL-JcTfPE1ErsgXlt-c-LAPETliGpVp7wP_F6malIXVJWmHJu9oTDAOYCjU-KF7xYStX2p8WRA4b7FUWgfLWLCVfeExUgSX5hCBrEHkKC3ASAtBM67igtMXRxyZjhQC_nckPa10Izk5QsD3hIFNKRTuJIQJGPgNl5gdz1xiJgox8x1ZI2g_A6l_xK7Rdz0w1op65CkCCwsRzO2DtRZreyj89nYe0ZmoTGF6UlSJ2t0nIzmcxgbNNc3DFFbHkxNDVcNXlPlbezV20MVgTJ8uQftT47KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤩
| فوری از برنا:
⚪️
❌
ظاهراً عباس کهریزی از ناحیه رباط صلیبی مصدوم شده
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140312" target="_blank">📅 15:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140311">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✔️
✔️
ورزش سه:
🔄
🔄
علیپور و خدابنده لو به خاطر عملکرد خوبی که تو 6 هفته ابتدایی داشتن، در لیست قلعه نویی برای جام ملت های آسیا قرار دارن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140311" target="_blank">📅 14:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140310">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROpgI4P-XxIty19f13PeSCdQOQCHht0K-91obW5EvhYvDLo211iTF_QW1Sttz7cir65t6qhQnho4qXKY6McBBv0qS6OKBWNXvC36oQJHdyoBiuOTq10zWztx7SaAsVQHhiqX-xsQDmM1gxECVQZHAt0hqtPS3uNxeNH1ME01ED2jPIPB16N_Nhl3XSrYj-tJ6burQUH0PGviVuzLH0-59yeYgHguZxmbDA9zldjHgs33FOdZJEK_tgwFHTLX_ot5jJzwCutmuNnTqve7GCWATLAn6nqeECu_SOWFcqNPBaatXumcaKfJiUqI0rNGrMCZnTymD7Pnd0iWeHhVaBlSoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مادرید در انتظار یک شب داغ؛ اتلتیکو یا رئال، کدام‌یک حرف آخر را می‌زند؟
[
اتلتیکومادرید
🔴
🆚
⚪️
رئال‌مادرید
]
⚽️
اتلتیکو با بازی فیزیکی و فشار در میانه میدان می‌تونه ریتم رئال رو مختل کنه. رئال اما در انتقال سریع و خلق موقعیت از کناره‌ها، تهدید جدی‌تری برای خط دفاعیه. دربی مادرید معمولاً پرتنشه و استفاده از کوچک‌ترین موقعیت‌ها می‌تونه سرنوشت بازی رو تغییر بده.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140310" target="_blank">📅 14:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140309">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
اوستون اورونوف و ایگور سرگیف از پرسپولیس به اردوی تیم ملی فوتبال ازبکستان دعوت شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140309" target="_blank">📅 14:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140308">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
✔️
✔️
#تکمیلی؛ فرهاد مجیدی سرمربی سابق استقلال ضمن تشکر از حدادیان‌مالک‌نساجی آفر این باشگاه رو کرده و اعلام کرده در ایران تنها حاضر است سرمربی استقلال و تیم ملی ایران شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140308" target="_blank">📅 14:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140307">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">😰
مدیران نساجی دارن با فرهاد مجیدی مذاکره میکنن تا این سرمربی جانشین مجتبی حسینی بشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140307" target="_blank">📅 14:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140306">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4GDfUjDkLsMpSkxtriIzfFuCLSrcN4gvt_Ar5HgPBheQ5WewYk_58hlHUibsvAMkW-2qeLyENZTENGVNszTk454SvDuXX34RpJ6Wxs2fvutqzCVwvmatlFEeaWTZ0VoVgjJGVi4Fk5nHGu34VSRe08DCWM_tlH8ilc6eCTIWb7axjbzh2pQoh1O1Vh_JoUD2w7XJ3MASFpBplz9enT4WKN6S5F8G_oUlH1suIWERDxjV1G7GdkBaEJ6y2Xjhba03IdRnYmyI6Cf_XKgY6HoNfGXRWgqNGxhlpYelaeHbSOiik7V7OffizBNH1jA5cJ7y67rOtR_QBHi8v_Qzii0bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیرضا جهانبخش قصد دارد در پرسپولیس به فوتبالش پایان بدهد
✍️
ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140306" target="_blank">📅 11:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140305">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7sL7UDCc7BnUtslWLMnhrBYYpVAJa-djGsBvxj5TVZGxOwWT4JEtx9b7IGaVFui7uFxNGMCappaOOnHspfrfJ7iDXYGTmBNbLlauIggeTLsyDJ8OSmsYjHav4egeYAxSFZ2R40wHMv-WByS4siNF_TQ5oT5fbQ8reyK81UtKkpJl5qfijdR2UE5IhCiWOuNJOEc7uW2n31KF_tbYwH2kkof40FK01vRXE-zECVNeIGwSonQDrnKDU7ds8o6BbgX8aljKXf5MCxYBlFDNgkB54YOPYBDmBHoF9rd7kF7vqR2hsGnEa8IW-1a33qVp68zR_sVSN0VbK_Ezzt4I6UEMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم‌ملی امید فوتبال ایران در دومین بازی از مرحله گروهی بازی‌های آسیایی برابر چین با تساوی بدون گل متوقف شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140305" target="_blank">📅 11:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140304">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIFJXngyWfC8eqt5U0fk6BZQtRUvs-QFocE3pAeHffuTdiiHoR8z_eXMDLFIz9WYF4XWNn3MA9sZYngf-agP5dIP12FMOui8_lTiPc64ozAYw-LemMla2RQthh4Dfr6aOZu3nvYN1fLsl5P_zZYCqQ4N-H5XXr224VVkC2d3D1DRSVHkkvdrYfjbEIZxIJGcvPBLUSQ4AHbKioPT15d1upZX_WfWuCStoyKhmDL-AQ4D9A0sZIYwhssu7NE4BE50heQ0CM_dtc4NQHLu9eYr1CifCbjO7rrWgAmn_NC_0E96Kyhbe1x7ehFIZO10InKg8wPVzrrs6WrmOmlAF1OWSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
✅
امیرحسین محمودی بعد از اتمام فیفادی برای تمدید قراردادش به باشگاه میره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140304" target="_blank">📅 11:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140303">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⚪️
مهدی مهدوی کیا: مجاهد خذیراوی به حقش در این فوتبال نرسید/ حیف شد و واقعا سوخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140303" target="_blank">📅 09:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140302">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140302" target="_blank">📅 09:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140301">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
ترکیب تیم امید ایران مقابل چین
✅
✅
محمد خلیفه، دانیال ایری، امین حزباوی، فرزین معامله‌گری، ابوالفضل کوهی، امیرمحمد رزاقی‌نیا، اسماعیل قلی‌زاده، عباس کهریزی، مبین دهقان، امیرحسین حسین‌زاده و پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140301" target="_blank">📅 09:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140300">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
تیم ملی امیدمون‌ امروز صبح ساعت 8:30 به مصاف چین خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/140300" target="_blank">📅 07:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140299">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">■
دنبال راه‌حلی برای ورود به سایت بدون دردسر میگردی؟!
🔵
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/140299" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140298">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDzgGWNitak2-OZ5t5mPajTlsjJd5WMfG6K8SC6hhsbdi_iep_JLdc14sWfS0q_WPeyzZ0fCmHtuHnbEW-PDCLc4ZduNHgygCT0MH_zqT5FSpPI0eDlAOLwHvFKiUeXdX_LS7zZsqOIoTRXbULHxqNJz8lOT6SQASPY4Ogi2UqMeuujv1DGMJMM2HOzDojBYR-nAaW1W5i-DKbljYhSfE90dP9QcLZbCLor3LH12vE4Ezftm2YnJUmNVzjNZboMCWUP9iPetROHo_qk1hJ0ZHQX1ONbluPJBpeCKpbVFNxxSbf7Ga93byPnZtguHaqQepqLezyu4uq30E5KbYR1vPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم ملی امیدمون‌ امروز صبح ساعت 8:30 به مصاف چین خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140298" target="_blank">📅 00:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140297">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
باشگاه نساجی مازندران کسری طاهری رو با 703 هزار دلار خریده و با 863 هزار دلار به سپاهان فروخته!
❌
❌
قطعااااا این انتقال پل محسوب میشه و باشگاه سپاهان تا نیم فصل حق استفاده از کسری طاهری رو نداره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/140297" target="_blank">📅 00:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140296">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
❌
دوگزارشگردیگر نیز با صداوسیما قطع همکاری کردند؛ نیما تاجیک و سعید زلفی دو گزارشگر مطرح، خوش صدا و با سابقه تلویزیون بعد از قطع همکاری باصداوسیما به پلتفرم نماوا اسپورت پیوستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140296" target="_blank">📅 23:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140295">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
رسانه هفت ورزشی:
✔️
پیشنهاد نخست لوسیل قطر که خوب هم بوده به محمد عمری ارائه شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140295" target="_blank">📅 23:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140294">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
❌
فووووووووری
❌
پیمان حدادی با درخواست مالی امیر حسین محمودی برای تمدید قرارداد با پرسپولیس در صورت گنجاندن بند 1.8 میلیون دلاری موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140294" target="_blank">📅 23:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140293">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
تیکدری‌ جای جلالی را گرفت!
🗣
🗣
مصدومیت ابوالفضل جلالی می‌توانست برای تارتار دردسرساز شود، اما مهدی تیکدری‌نژاد با عملکرد خوب در پست دفاع چپ حسابی جایش را پر کرده.
🗣
🗣
تیکدری در ۴ بازی اخیر فیکس بوده و پرسپولیس در ۲ بازی اخیر کلین‌شیت کرده. حالا با این عملکرد،…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/140293" target="_blank">📅 23:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140292">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTwUsNtztr4mwgNvA1cYOeedwyP590LgzC6eAC8DMrMkODAmmyNyRqmUWTdeUShFDWX5d-yMOUWLDe2kLmonI-C5V2YRaCizutu361FhjmtZnQ8FjaZt77GeCu8HPX4gPxjkg4jJ09j-8ZdjW14OrwNAOO65WcNwIbTMV7yroeStWZYKs9-y8BI2blWNYWFrsPVGkgke4DniZuYM-7-E294sEvQCtmnxbsqUVXWwHLYzy5qt7FSIWUSkoj6SiztLj5eUql2gqbxypvvuWGnh6IkFSBk8mUF6F6S8ugIYnh4wxMIzsMss1-9gj4_pNYuxbg-0VYXhB4qJp9vE-FjTJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گزینه جایگزینی یحیی در دهوک مشخص شد
❌
باشگاه دهوک به دنبال توافق با گل‌محمدی برای جدایی است و رسانه عراقی «روداو» این موضوع را تأیید کرده است. مسعود میرال، سرمربی سوئدی، گزینه اصلی دهوک برای جایگزینی یحیی گل‌محمدی معرفی شده است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/140292" target="_blank">📅 22:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140291">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d7cf776d5.mp4?token=ovczWeA-8kG8ps_tOktDSYsAkgE5zTSLRE7syYK_Eu6NWbpj_wkwxSJEey9wsi7UA3GN6xatUUxPndy81m3T-6GwhuXtnxZJ3GJ4UmUK2kBevnSKStv1xZ08f6-bUf0tv7-j9ehPBLOGDo2E12gZuxceQlKlyUCF6RYgMwj8S7pPdMMvUuAEg8fN2Mh0MRChv3dpPi4g0RtE1ukcElQYuvtvBwgHP0UH_LeUxadPyMz3kpmNOAAr4PKaScFb12cZbXsSP1qlQ29CoQTrW2G6v0nr_2qlcQP0lvCJaI9avuLElff7kmNP2YM5Z-BBy3ByxwcsJ6jzyvs5bfEIRY_o3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d7cf776d5.mp4?token=ovczWeA-8kG8ps_tOktDSYsAkgE5zTSLRE7syYK_Eu6NWbpj_wkwxSJEey9wsi7UA3GN6xatUUxPndy81m3T-6GwhuXtnxZJ3GJ4UmUK2kBevnSKStv1xZ08f6-bUf0tv7-j9ehPBLOGDo2E12gZuxceQlKlyUCF6RYgMwj8S7pPdMMvUuAEg8fN2Mh0MRChv3dpPi4g0RtE1ukcElQYuvtvBwgHP0UH_LeUxadPyMz3kpmNOAAr4PKaScFb12cZbXsSP1qlQ29CoQTrW2G6v0nr_2qlcQP0lvCJaI9avuLElff7kmNP2YM5Z-BBy3ByxwcsJ6jzyvs5bfEIRY_o3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
مرتضی پورعلی‌گنجی تو بازی امروز تیمش دقیقه ۹ اینجوری ساق‌پا بازیکن حریف رو قلم کرد و خورد کرد و اخراج شد
❌
بعدش جالبه اعتراض میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140291" target="_blank">📅 21:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140290">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufJlZ2IygEULrdpoRRKWLDjVS3CbErfIA5yHlQq6sifID8TIH-AzBSfKrL65ysPZJc8duaucgrmTHgMOIIhmdJ2q9DPdWiRwHAkZsvVG1pXjZdpEKLisTn5y9Mrjpebws1PyeFEnpuCxjzKaCAFe46E42c7msDNqlglLtTTjCCMdyStajVpUre0L41NIufRskeiltbm7CtQ4SGi1vB6l61GX-p8VVftO39IE7pnoZsS6yjd3RQvh0e0qHUc_UuZQ9swCv0n-B1uRDksYbYoGH2qJbXOEpUmCksW9FvScFogMcbqrhr1gCU-MmOLYlG-CdaUWuVn2Z2ecTewADDhpLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
با معاینه پزشکی بیرانوند موافقت شده و اعزامش دو ماه عقب افتاد رسما میره تا نیم فصل
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/140290" target="_blank">📅 21:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140289">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
⚽️
⏳
۴ گزینه‌ی جانشینی مجتبی حسینی روی نیمکت نساجی
🔴
در صورت قطعی شدن جدایی مجتبی حسینی از نساجی، سعید دقیقی، سعید الهویی، محمود فکری و جلال امیدیان گزینه‌های جانشینی حسینی خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140289" target="_blank">📅 21:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140288">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔄
🔄
محمدرضا احمدی از صدا و سیما به طور کامل حذف شد و حافظ کاظم زاده مجری فوتبال برتر شد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/140288" target="_blank">📅 21:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140287">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
بشار رسن پست مربوط به بازگشتش به پرسپولیس را لایک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/140287" target="_blank">📅 21:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140286">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
❌
❌
آخرین وضعیت سربازی بیرانوند از زبان مدیرعامل فجرسپاسی: معافیت بیرانوند تا پایان آذرماه است و این بازیکن در تراکتور می‌ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140286" target="_blank">📅 20:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140285">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3ztVbZmTbZu41ZjaXrAufb3Roy5Sm910tXQdQDJJbsx5iw79xnwSA5SALJ46UkdTiFYIwVH5YIjAFeEAtfeITRVOKbAjTB9Bk6K2sSMY8_5-1n1oy8MrENAu-iQ_osDYxC2bnBAP9IchN6mXDSW2LhmN21m0PVqRVmwB91LWQ9vPP4e1R_3g7JXengcNc3NUE4tE-rtCNoYso_0NQissBCHd21dL2Eq6CJyPy-WsBZj8KqFmLlhwmLiOiw_Aw274Q1ppyG4-3hrD0zgciTnGa1UARHwhKL_kD1SpNb-q7e3i4_oijQHwsiwsBI_sCfN4KIhwnMWkqqf2pQ6U4qK6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزگاری سیدجلال حسینی با وجود اختلاف قدی بیش از ۱۰ سانتی متری که با کیروش استنلی داشت با پرشی فوق العاده سرزنی کرد و رکورد فوق العاده ای از خود به جا گذاشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140285" target="_blank">📅 20:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140284">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
✅
با معاینه پزشکی بیرانوند موافقت شده و اعزامش دو ماه عقب افتاد رسما میره تا نیم فصل
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140284" target="_blank">📅 20:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140283">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgNpvi83VcQUbW3WJYm7-cUeXsLMiDe_fVZsmfK5ijcaxd_WVanq5PA4pV_KCwH9m2M9LtxKdbX2uPBDlWzvwumYw3eArQjNp8aKKv5LbOt2DUNElCfNmU3Y6txmS_0q6ZvNq-xPMwWc23AQv7RTUJLg0zn31pm4XaJKAWfkexgHVCJ8jg2RSge80hipmYJhr-KK7X6_T68XGjW4ZRUld6NI0aGMUso2-TTc7JtPW8IxSYu-vcy2nhpjX0SSqHF3Nb-WsJ6tiKgyIFvzNywhuDxsVxm6UF_gPgEWXyCqdmCd7CZUtvKaRwHCIlVgsbduhtTqRc3cKkIjMZF9w9-dmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نبرد آندلوس با کاتالان‌ها؛ سویا سد راه بارسا!
[
سویا
🔴
🆚
🔵
بارسلونا
]
⚽️
سویا با اتکا به بازی مستقیم و فضای هواداری، می‌تواند کار را برای بارسا سخت کند. بارسا از نظر مالکیت و کیفیت فنی دست بالاتر را دارد، اما مقابل فشار سویا باید کم‌اشتباه باشد. تقابل دو سبک متفاوت؛ جایی که مدیریت فضا و استفاده از موقعیت‌ها می‌تواند تعیین‌کننده شود.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
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
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140283" target="_blank">📅 20:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140282">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGfjKZSRBTSfoMS83-J7jmCnzKYJpA7Yt7Xj6hYmomBPq1U7-pH6PmMw38S6l7xHM8vOENO4QyT2LXzV5z2FICWhjcb7KxmrVg2YjB4aUda879Svopz2fzly8ZvG9IbBpvWlFZ71mm-QhMpp3EDbvI7MHZ27-UK-mYoVZC9s6arQjW-PSv4Km_YOw6quoW1ZwCUa7BL7s8lRWJhxBwa2dlI0vQhZA8RBt_yQh18wbA7BYmYFWFS18p9e5avMQ8vZgVDyHk6HfxlpsFXPZQfBUGlwg5pj66aHxNOGS5x---RVHQWJ4E5uEbN-DmmQyOiU1H0IhQ0Ax9yBdqwyWdNpLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرینات امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140282" target="_blank">📅 20:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140281">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWaAzV2aC9jcUD-2orNYfHQiBQHeJtsdDH5j3UaNsj3hszvV7VUJijLZGKtZAsE2yRJr3z66FlaGst-lJ7_KNOS_WUo0nBIOD3dMX70_jwylADpBEcUhtrNXNkNDECdiyWABSPrGe9tP3IpGfZmM68eK0jQeJCJju89q4jT6MDputCS2RWwaSrcaGCLGUa0jxtGJ7nucco_y8wvthO8b4M7i6k-kjTlrQ5b08kw-77FhrA-vgYb8GqnFkzIMUpppg-ui8m83ecN4HRqBNMMBQoyL2lkCieiwKp19rRtlZzpA79-2tZSULyjXsETd-1rq6NewFDSncEfJdWh4felrVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
⚽
بازگشت سرخ‌ها به تمرینات
⏺
تمرینات پرسپولیس پس از 5 روز استراحت امروز با حضور 15 بازیکن از سر گرفته شد.
🔻
ملی‌پوشان و بازیکنان خارجی تیم غایب تمرین بودند.همچنین حسین کنعانی؛علی علیپور؛محمد عمری؛حسین ابرقویی و امیرحسین طاهری به دلیل مصدومیت زیر نظر کادر پزشکی تمرین کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140281" target="_blank">📅 20:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140280">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI1ltb1rDiJ8N235SKQKMty44ucxjqSc2KALvZ4CRFSoPtyineShVuPAfRAONVCVlZdATQLj1PPIboavjCziKABp7L3WXD-vnljfhBUreiFPWmXm1TjQmVRI5BCvM8k8QmLxwraIgALCpW5Uqfur_ckSWpFyYlCY0ikfF7x5Kz96_qVRp2Q8OXS9sh9eQHhvqajlV05zlw1GFLk-kVtTmgDts7xqTTy3Cf1Lg4H0aaFA8C-T2TritHRkLbXGcIjfDM38ycW2C04XWqsLB9mH-e7y1yyxipeKrYAutp2FOycOt_FgznAdCye12lY-_xdZWkxrPztu7z7DF71PatZtlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووووری شایعات
🔴
🔁
🇮🇷
ایگور سرگیف پایان فصل از پرسپولیس جدا خواهد شد و مهدی طارمی به پرسپولیس باز خواهد گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140280" target="_blank">📅 20:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140279">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/227e813e97.mp4?token=lF5I0V_NxtLkzooXu4xJnYvoag-_bpX2o5HieznppiQqM7nYDpqziBKbUXXRf__nrH2ov44U6j19a-09ducmdFw9Q03zM1aotOSYjankux9l8_OP8N3KXXoxBVOx011DWPOr_Er0yw7pJrJuPvpX8PPwIdb4EBOw_aG-Jg6HzhQgcPgTVlMlUobVIbssKxEgG7O-5GGbsCJSixIM2OF2ZO7K_iQFoz4xFSEkHPd9-yqlYTIF7t62HAcVM16CnhRVpK_cXfO3QeuBXsoVV61nSW3iSxkCpM_4aZl2QwNxpVTTfiLE3ho8xVIJVAQY-6I8yUhPphfLLlFUdONknxcTiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/227e813e97.mp4?token=lF5I0V_NxtLkzooXu4xJnYvoag-_bpX2o5HieznppiQqM7nYDpqziBKbUXXRf__nrH2ov44U6j19a-09ducmdFw9Q03zM1aotOSYjankux9l8_OP8N3KXXoxBVOx011DWPOr_Er0yw7pJrJuPvpX8PPwIdb4EBOw_aG-Jg6HzhQgcPgTVlMlUobVIbssKxEgG7O-5GGbsCJSixIM2OF2ZO7K_iQFoz4xFSEkHPd9-yqlYTIF7t62HAcVM16CnhRVpK_cXfO3QeuBXsoVV61nSW3iSxkCpM_4aZl2QwNxpVTTfiLE3ho8xVIJVAQY-6I8yUhPphfLLlFUdONknxcTiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
گلزنی احمدنور در دیدار امشب کلبا مقابل خورفکان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140279" target="_blank">📅 20:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140278">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxkWDCGLGznttRpJ1F8TGBHamhYd3rzP5TtQs_0fNuEl7kenvCEHIEp2AX67tb0v_rrt3jyWAWA_xQsZbQYi7gHkmI9uzJ-c7KE3N7704l99OLLSPpnuOOWQS0uG4FqjllUNcq3lZqXhQ5lwjUkDWefOB02e-C1nfnIHC17QmbtaiVv3fS5O6MRxt64Yn5GbnEj6XZOpbaQYJQmuKqvALSY9p4PcEA46v00z8rcUXAEzFdoH86hT4c0iJOoTEqkNVVE5-QEfgliHXsyGF-oPtIJdbl4-_AzUT5k-C82jT1bX4FRnEM_yN4XCxpT-aExjClwn8uATjLry3AerbGJk5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
با درخواست علیرضا بیرانوند مبنی بر انجام معاینات پزشکی موافقت شده و او برای بررسی‌های بیشتر به بیمارستان معرفی شده است. این اقدام باعث تعویق موقت زمان اعزام او (که قرار بود اول مهر باشد) شده است. اکنون مشخص نیست که اگر او موفق به اخذ تاییدیه وضعیت پزشکی…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140278" target="_blank">📅 17:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140277">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
⚽️
⏳
۴ گزینه‌ی جانشینی مجتبی حسینی روی نیمکت نساجی
🔴
در صورت قطعی شدن جدایی مجتبی حسینی از نساجی، سعید دقیقی، سعید الهویی، محمود فکری و جلال امیدیان گزینه‌های جانشینی حسینی خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140277" target="_blank">📅 17:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140276">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
بازیهای دوستانه ما تو فیفادی:
✅
پرسپولیس
🆚
گل‌گهر
❌
پرسپولیس
🆚
چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140276" target="_blank">📅 17:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140275">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
بازیهای دوستانه ما تو فیفادی:
✅
پرسپولیس
🆚
گل‌گهر
❌
پرسپولیس
🆚
چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140275" target="_blank">📅 17:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140274">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
پیام صادقیان خطاب به امیرحسین محمودی:
✅
بهش گفتم سرت تو فوتبال باشه و فقط به تمرین فکر کن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140274" target="_blank">📅 17:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140273">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
بیرانوند قصد دارد پیش از رفتن به فجر سپاسی، قراردادش را با تراکتور فسخ کند تا مشکلی بابت چند ماه باقی‌مانده قراردادش نداشته باشد. با توجه به بسته شدن پنجره نقل‌وانتقالات لیگ برتر، بیرانوند از ابتدای نیم فصل دوم می‌تواند برای فجر سپاسی شیراز به میدان برود.…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140273" target="_blank">📅 17:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140272">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiRuFws9l2HD87hif_PfbV3SNvVsf03lJ10ms48nvUzJHPaEANARHjuOfBuK3jQqW15ne01T-985bC5iWpVf-9E6tllzumqWEMXEJY8c3uOFrOlLC4woyHaDMr1NiTKQf-0WaJ5Uiqlpt5Tpr1z00Fn-4ZMMI6uBk9v_5ipXSeMIPsuDN48r9V9z1ld2sR87lYM4NycVGWH1FMkDyByCyoKcyuxlB4vS2YCE3-DvRLaGtuAujgwxrNviHwzup7pNSxe9sz9RClOrjo-wMPJ5Escb9RlR1vfeREopD92ClTr6KmbSVMPjGC0M9n2mGWQKyOvwXneUlV4yt5O8uaCmSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
ROMA -
🔵
INTER
⏰
Tonight 19:30
🏟
Stadio Olimpico
🔵
رم در خانه با تکیه بر مالکیت و فشار هواداران، دنبال کنترل ریتم بازی است؛ اما اینتر برای تغییر جریان مسابقه فقط به مالکیت نیاز ندارد. نبرد اصلی در میانه میدان و انتقال‌های سریع رقم می‌خورد؛ جایی که کوچک‌ترین اشتباه می‌تواند ورق را برگرداند. یک بازی نزدیک و تاکتیکی که احتمالاً تا لحظات پایانی، نتیجه‌اش باز بماند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدارهای امشب لیگ اروپا رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140272" target="_blank">📅 17:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140271">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc94830254.mp4?token=jBk_hiMYMXb39ySM3Dq_oo7IkFBepGDO1CG-k5x_uPpc4jFp3Q4UW-z_PuXW2p33ID8i9HdB8kWF0jiA9rzvHlEP4ccmWGsrI3vwRZXG4fzfZ-iU2n0PI7ZQEGNl1X_OTf5_BZZHpacaX4AYoIv3PpoZ9mCN2tphlwHUlR2fdIx08axGq9EdNmBCgLOYfvKcBrDZJK9ihk_u1eRCOh5xDKVH0OtAw6odv7cJ6Kg4KBfcsCwVi4Ft3TOgQtzHurRLoYCo2zuyiYMBd6IBuuaQN1zBImEvIqJ-xFC-PXAdze2miFJlPdNIYOBmGtm6AW4DL9EOJ56d6cIp-vhWSlHg0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc94830254.mp4?token=jBk_hiMYMXb39ySM3Dq_oo7IkFBepGDO1CG-k5x_uPpc4jFp3Q4UW-z_PuXW2p33ID8i9HdB8kWF0jiA9rzvHlEP4ccmWGsrI3vwRZXG4fzfZ-iU2n0PI7ZQEGNl1X_OTf5_BZZHpacaX4AYoIv3PpoZ9mCN2tphlwHUlR2fdIx08axGq9EdNmBCgLOYfvKcBrDZJK9ihk_u1eRCOh5xDKVH0OtAw6odv7cJ6Kg4KBfcsCwVi4Ft3TOgQtzHurRLoYCo2zuyiYMBd6IBuuaQN1zBImEvIqJ-xFC-PXAdze2miFJlPdNIYOBmGtm6AW4DL9EOJ56d6cIp-vhWSlHg0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حمید مطهری سرمربی فولاد: پرسپولیس تا الان نتایج خوبی گرفته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/140271" target="_blank">📅 16:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140270">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‼️
💢
💢
💢
باشگاه پرسپولیس میخواد در پایان جام ملت‌های آسیا برانکو ایوانکوویچ‌ سرمربی‌ سابق سرخپوشان رو بعنوان مدیر فنی این باشگاه به جمع سرخ پوشان برگردونه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140270" target="_blank">📅 16:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140269">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
💢
💢
✔️
✔️
مدیران باشگاه پرسپولیس هفته گذشته‌ مذاکرات برای تمدید قرارداد پنج ستاره آغاز کردند
❌
پیام نیازمند
❌
محمدحسین کنعانی زادگان
❌
تیوی بیفوما
❌
اوستن اورنوف
❌
ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140269" target="_blank">📅 16:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140268">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
قراره در فاصله تعطیلی لیگ، برنامه آماده‌سازی پرسپولیس با برگزاری ۲ یا ۳ بازی دوستانه دنبال بشه تا سرخپوشان از شرایط مسابقه دور نشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140268" target="_blank">📅 16:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140267">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7dB-yv6Td8xO8tb1jTnglptzb8dUII85SDPc_8M3_WwVFRmHiYk8AGZH5bjmY2ehXaWgWkDgOeo6Gea_SpYoE6n3yXk2DZLgbpONsOwz3NhA9GzadKt0t-DogdN07wejWgcE7xQ5K2XAkXt7M0mqT0xY2-CzZzvhwGzBLmiJ7008V2KDFAXCNLMaBbb1ikMmho3DDa1kIL7-Q9SzJlAODsNfVVQIaprPT0E_moDn6W5vYZ5BQHtL2dXKUEndZ633b8JPRFBNXVrgfX5Ii-RSTvcj6ZXxD2QbQloHH7bAjsAiAeeorZ5H2xeNuiLSyUxGjN4wjf0lTpz-HJ1QTo5fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تیتر روزنامه‌ گل درخصوص دعوت شجاع خلیل‌زاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140267" target="_blank">📅 15:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140266">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
✔️
میلاد محمدی در آستانه دیپورت از لیگ بلاروس!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140266" target="_blank">📅 15:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140265">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
فرهیختگان:
❌
مدیران پرسپولیس معتقدند که مدرک کافی برای پیگیری شکایت یاسر آسانی در CAS را دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140265" target="_blank">📅 14:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140264">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
❌
فووووووووری
❌
پیمان حدادی با درخواست مالی امیر حسین محمودی برای تمدید قرارداد با پرسپولیس در صورت گنجاندن بند 1.8 میلیون دلاری موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140264" target="_blank">📅 13:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140263">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
❌
🗞
فوتبال۳۶۰:  بشار برای برگشتن به پرسپولیس پالس مثبت نشون داده.تارتار تأیید بده برگشتش قطعیه
✔️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140263" target="_blank">📅 13:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140262">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
آغاز تمرینات پرسپولیس از یکشنبه در تهران
✔️
✔️
تمرینات پرسپولیس پس از چند روز تعطیلی از روز یکشنبه ۲۹ شهریور در تهران از سر گرفته خواهد شد.
✔️
✔️
برخلاف برخی شایعات درباره احتمال برگزاری اردوی خارج از تهران، مهدی تارتار در شرایط فعلی برنامه‌ای برای برپایی…</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140262" target="_blank">📅 13:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140261">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/052167cdae.mp4?token=i05GyfysXlwmeTdsGGvIMuxPxyBdggC5uWRK5bDTCA_a-jxLqWZOtvm3Fbh42A0VBtDWdRZCfslNMN3lKzfc6Eh-vOIESqOb0o0Wp-A1pT8X2pq3vgvuFvi_LmeGk8gW5SiQ5KQzRUKk8Xm8osX_hdfCnBjUzU9Jp6--uvtcnXiDtcPlrnbtxhzn-uzcfmwUSTkB4Epgzb9CqVVSlikpbVAj1JXT1ikQKqVznkF1Nbb4V1E-S4z2QRE4I98w4uBD1EjGLsZbGRd7_czJZIodMZvZNYevcePnV4bXRr7QCEYUwMkwxVKFuC80zM-TRruvModAqmq9dhB0t6C3XCiTsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/052167cdae.mp4?token=i05GyfysXlwmeTdsGGvIMuxPxyBdggC5uWRK5bDTCA_a-jxLqWZOtvm3Fbh42A0VBtDWdRZCfslNMN3lKzfc6Eh-vOIESqOb0o0Wp-A1pT8X2pq3vgvuFvi_LmeGk8gW5SiQ5KQzRUKk8Xm8osX_hdfCnBjUzU9Jp6--uvtcnXiDtcPlrnbtxhzn-uzcfmwUSTkB4Epgzb9CqVVSlikpbVAj1JXT1ikQKqVznkF1Nbb4V1E-S4z2QRE4I98w4uBD1EjGLsZbGRd7_czJZIodMZvZNYevcePnV4bXRr7QCEYUwMkwxVKFuC80zM-TRruvModAqmq9dhB0t6C3XCiTsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
آغاز مراسم افتتاحیه بازی‌های آسیایی ۲۰۲۶ در ناگویا
❌
مراسم افتتاحیه بیستمین دوره بازی‌های آسیایی در ورزشگاه میزوهو شهر ناگویا ژاپن آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140261" target="_blank">📅 13:06 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
