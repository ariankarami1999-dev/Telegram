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
<img src="https://cdn1.telesco.pe/file/PEG1IC_wIwVky0eM-sApqiTGKy6UbEdmA2m69vhBME1l836ftFrbOOUrAWIFqvlPBks9r9DXsGd9OaDa4W9w-19GZBLCQyh_jSTeUrYofnz_Vs3Cvm_8XrysKWi39iMVq9fAXCGJds2nWfH1CIvxmxNz89cERFGnIJ9aHy2HS7CfhrUxqyPazkaUebqddhYacUXWz7SvKV4H2Pm2JQLsPrg8CInPrzKv8u3sZjZooLC9qbGfBi4pYfbfDyIlkVweoR5L5UN-GYT_uwyEmtXP3wk5ql29br_tie4uJ-P8f_btqlwcmTDTrI7IR5prEd0qQWdJ61O9yss-09ZAioOBaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 157K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 05:11:23</div>
<hr>

<div class="tg-post" id="msg-4737">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">知的な戦い</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/MatinSenPaii/4737" target="_blank">📅 03:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4736">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">روسیه دیگه دید زورش به اوکراین نمیرسه، گیر داد به پاول</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/MatinSenPaii/4736" target="_blank">📅 23:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4735">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگیفت بازار | Gift news(𝗂𝖼𝖾(𝜶))</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9nSyeByBrBmtsqJQ5Y01r-otFB02OJZkaXbhGN3n_-NCEF_N2W1zuMO6gzIkvpHy_cgYv5IZqymEEkvATRIv_vTqeFWCkRGjlF9vWJvri3No0nMKaoUy6wigYYV0sOnRqXBmFUAcUw3grsxOptA3C9Ow9UDhIeI0vxjpCsnBoA-dmshrcU1NjL-whOEUjZxwgAbKNeyNx9P5zpQa62JMwXNCPp1jM4y2tygmYhV6JmtRVRb0NmaEP1mPI5TTZN0qRIH9tGSzGKAO-ASISoe0Ez2e5b_h7mrZ0D7E4DtvPJ2mfuv0cQrMZ1E5kEUvWrzxVDQHy_5q5nxpWPHiq6iJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری | روسیه پاول دوروف را تحت پیگرد قرار داد
💸
بر اساس گزارش رسانه‌های بین‌المللی،
سازمان امنیت فدرال روسیه (FSB)
علیه
پاول دوروف
، بنیان‌گذار و مدیرعامل تلگرام، به اتهام
«تسهیل فعالیت‌های تروریستی»
اعلام جرم کرده و نام او را در
فهرست افراد تحت تعقیب بین‌المللی
قرار داده است.
💸
این اقدام می‌تواند پیامدهای حقوقی و سیاسی قابل‌توجهی برای
تلگرام و فعالیت‌ جهانی این پیام‌رسان
به همراه داشته باشد.
💸
بر اساس ادعای مقام‌های روسی، تلگرام اقدام کافی برای حذف
کانال‌ها، چت‌ها و ربات‌هایی
که به گفته این نهاد توسط
سرویس‌های ویژه اوکراین و گروه‌های تروریستی و افراطی
برای هماهنگی اقدامات خرابکارانه، تروریستی و جرایم سایبری استفاده می‌شدند، انجام نداده است.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/MatinSenPaii/4735" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4734">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iPnRAyTsfsAbpWPQI9-KNKFhVmSkj03pe9-ugcGEBiyzYSBRbOSk-IuQVEuM-9Dsw61Qx_7GHO7ssdxwZAU7MLXKmecDwKrVz-hndQK-xoqLdt3UUayWAy0nbdcoZFa8bbacajZiNXXFaWbXzVqo-JCln9vqVZXfo456WNmw6cBuOzg3lzA6XbaF6b2ni9Gl9BcQCCjqN7lb3YVQrovZt6BO7LAxxmVV7M0ZDWROyYxY5LE2aFCQzZswD0sqzKPGV6XiLY1lnUMo4zHpEO6hjZ7huG85nF-4NAKgwzjuVzDDO0zSqalMuFO4HqYDV_Di86n45A9NC-1JGpnSr6Rtww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم این کار خیلی قشنگیه که هم برای حمایت از پروژه‌های اوپن سورس و هم برای تبلیغ کسب و کارتون، می‌تونید انجام بدید</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/MatinSenPaii/4734" target="_blank">📅 23:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4733">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">آپدیت جدید Aether:
https://github.com/CluvexStudio/Aether/releases/tag/v1.5.0
\\\\\\
بزرگ‌ترین آپدیت تا الان رو دادم دو تا قابلیت جدید و یه سری فیکس امنیتی. توصیه میکنم حتما آپدیتش کنید مهمه و خیلی بهترش کردم و بشدت بهینه شده و شانس وصل شدنتون هم روی شبکه های پر اختلال هم بیشتر شده:
- پشتیبانی از Zero Trust (وارپ سازمانی) "وارپ پلاس"
قبلا Aether همیشه به عنوان یه دستگاه معمولی وصل میشد. الان اگه اکانت Zero Trust دارید میتونید با همون وصل شید. هم روی مسک هم وایرگارد کار میکنه.
(پلن رایگان داره کلی فیچر اضافه بهتون میده نیازش داشتید میتونید بگیرید و وارپ از حالت معمولیش میشه پلاس ولی بیشتر برای Enterprise ها هست چون Egress Policy داره میشه لوکیشن خروجی تنظیم کرد)
موقع اجرا گزینه ۴ رو میزنید
نام تیمتون و ایمیلتون رو میدید یه کد براتون ایمیل میشه وارد میکنید و لاگین میشید.
توی داشبورد کلودفلر Zero Trust نیازه ستاپ کنید..
\\\\\\
قواعد مسیریابی مثل Xray اضافه کردم:
یکی برای بلاک کردن کامل یکی برای اینکه از اینترنت خودتون بره و تونل رو دور بزنه (مثلا برای اپ بانکی یا سایت‌های داخلی که آی‌پی خارج رو قبول نمیکنن) لیست بلند رو هم میتونید از فایل بدید.
\\\\\\
فیکس باگ گول که بی‌صدا قطع میشد. این رو یکی از دوستان گزارش داد (issue #65)
\\\\\\
قطعی‌ های کوچیک شبکه دیگه کل تونل وایرگارد رو نمیبندن...
مصرف رم روی سشن های طولانی با قطعی زیاد فیکس شد.
-----
ترتیب اسکن رنج آی‌پی‌ هم فیکس شد الان طبق داکیومنت کلودفلر اسکن میکنه...
\\\\\\
روی شبکه‌هایی که سرور ثبت‌نام کلودفلر رو بسته بودن
به دلیل فلگ شدن آی‌پی یا هر دلیلی... کاربر اصلا نمیتونست وصل شه.
الان یه راه جایگزین داره...
کلی فیکس و آسیب پذیری هم رفع شده اینجا جاش نبود بگم...
ممنون از همه کسایی که issue دادن و گزارش کردن :))
لینک اصلی پروژه:
https://github.com/CluvexStudio/Aether</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/MatinSenPaii/4733" target="_blank">📅 23:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4732">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/MatinSenPaii/4732" target="_blank">📅 22:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4731">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VyXWN5TpQxP_EDsX1yW_LRpHAcypV1jOxT3Voud_PDU-stbImDWBwDv1YWJ6UQwo7j2lVszUvU5YRAdFlNd81cJ5YjdjxOifkJSRzP-4chu4S5eKgWrk8KVfx3OMKnSPygS7rBK3FxG5ZsRTRvkr5R9s7Sbvg8jssY04mgDTTJiHZBjDreBAfapl34S2pIJMqEm6CubEfN-2kuC0mziawh65HFHUdOK1VXxS_kuEcxtFdK3hu2vyKdl_Au7pJ1rwW9H4gQ0LrlkYJ6UcPCCy19CE0C2gZrBcIsBcbg6-EtHBrCzYdYorZAbH-EjLiS6C5cUa5VtAkFHWFqU68tdQtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین دسکتاپ لینوکسی که کامل توسط AI نوشته شده!
یه پروژه به اسم Starling منتشر شده که ادعا می‌کنه اولین دسکتاپ لینوکسیه که از صفر تا صد توسط هوش مصنوعی نوشته شده. این نشون می‌ده که توانایی AI توی کدنویسی و توسعه نرم‌افزار به سطح کاملاً جدیدی رسیده:
https://starling.build
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/4731" target="_blank">📅 19:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4730">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/00a76c08a4.webm?token=DAIXrfXlr6o_vnBUWfYPZj1xsS6oVql4BXxvP2npFodraSQGipO4aUh6JqpBDSgtkIqAvsTxfGUd7EyGhg5Sk9vJ8cZ43GLj05TP48r06wnWirxBcHEzxrXYL76x-BRilJZ7zcKswXRotPjX1RG_ukeXwIAl0R4vY_kKKKeFsonJvlebotQjRKMQfv3DM2oaCPfSAOmkUGMj0jJwWr481eu8mFmen0nmdoRhwsjmhSVwNv-h_EoLsSfpa53Ft7ici9dtEixFLSnZ2FnZ6hUsHFJ887VpedxUyP4rFTAHnsSLsICoyazl-9Hu3XV_RP6wkO37IbYMa38A-N3Fl-59Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/00a76c08a4.webm?token=DAIXrfXlr6o_vnBUWfYPZj1xsS6oVql4BXxvP2npFodraSQGipO4aUh6JqpBDSgtkIqAvsTxfGUd7EyGhg5Sk9vJ8cZ43GLj05TP48r06wnWirxBcHEzxrXYL76x-BRilJZ7zcKswXRotPjX1RG_ukeXwIAl0R4vY_kKKKeFsonJvlebotQjRKMQfv3DM2oaCPfSAOmkUGMj0jJwWr481eu8mFmen0nmdoRhwsjmhSVwNv-h_EoLsSfpa53Ft7ici9dtEixFLSnZ2FnZ6hUsHFJ887VpedxUyP4rFTAHnsSLsICoyazl-9Hu3XV_RP6wkO37IbYMa38A-N3Fl-59Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4730" target="_blank">📅 06:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4729">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">چقد جمعمون همه پولیسیم
خوشم اومد</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4729" target="_blank">📅 06:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4728">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/laG0MoS5Tu0DxiKgOfhJZ08sZiEwM-ouWCFRmpCMuaPTTqzbaOuSeskRdEk9p05kuNX1IcPSNrRwSXVMnnQXktjrMoudwnLjkwytrWMKx913AwG5j5ZBzmdJC-ETuEcZEFsxR_cFQ0vDVn3LKvKILhJpgUZ51s00XKAPqGfomFTFVi2GbS2kDCawlxuPTPrMVxLJEZr3gIxVUSGT_Sj4sfSlvLcPIHi1Sk4vRt5c_BHwhq1OvfhGa6BKt54XMD7EIA_UcrpCPhLGpqHfCkXjZX2OCxNZWFNjL32lIHImUgTamWPYZLSLWnJtoWjTI46VEfIyu8Qd1A6yjTUl7o0yzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقریبا بیست روز پیش هم این اتفاق افتاده بود</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4728" target="_blank">📅 06:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4727">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BJUh319BE1Zwx-SgGMY5BRWnld6ZOclv1L71aChjbhOiq8izS76rxfnGUGMTg3cMhEm0zpkbFoPlCU815sQ_q6e-RN_sOSNO9B_7I7BVi0nS3Je7FL_QNZrUqPXSfMak5EXSS3vYlsLxhKac7LKgf5h3kQcJprlyyis4JbjtmXCcp_fsIEHkM1Ea9e0VSiuGnTdZuMv2R8wgSEjpOqPfmDAIENvAqZ9sZkz6WZ2U4U_Xy_WX-CcDQVJLMDbHCzMl6QGcF2YqfeUGfSN31ddkvyguTpHri8aDMSFRZdKTvddDqGrc-G3gROo_QlWddQVKQWM3HuGs99t6OIADiNtRyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه چیز خیلی عجیبی که دیدم و تست کردم، این بودش که اکثر بات‌های روسی/انگلیسی دانلود تیک‌تاک و اینستاگرام و یوتوب و Shazam و... همه یا مال یک نفرن؛ یا از یک زیرساخت استفاده می‌کنن. یکیشون اگه خاموش باشه برای چند دقیقه اگه همزمان به چندتای دیگشون هم پیام بدید…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4727" target="_blank">📅 06:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4726">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دیشب گویا روی نت هم یه گندهایی زدن
زیاد شنیدم از بچه‌ها که ۵-۳۰ دقیقه نت قطع یا به زور وصل بوده روی اپراتورهای مختلف</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/4726" target="_blank">📅 06:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4725">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یه چیز خیلی عجیبی که دیدم و تست کردم، این بودش که اکثر بات‌های روسی/انگلیسی دانلود تیک‌تاک و اینستاگرام و یوتوب و Shazam و...
همه یا مال یک نفرن؛
یا از یک زیرساخت استفاده می‌کنن.
یکیشون اگه خاموش باشه برای چند دقیقه
اگه همزمان به چندتای دیگشون هم پیام بدید
می‌بینید خاموشن:)
ماشالا به هوش کسی که پشت ایناست</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4725" target="_blank">📅 06:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4724">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SLwv2JuNffcCwJu08L3YV8u3nspuV_BAipXQzRQeRJF1K8dHa4cmS7ZrkWSNxsD5lSHlq5Blay7U1OTLSTYEVYuk7Lzl4cYuxs9qnXzpC4IQBvvGtC4N0NgGKYhKLttbo5_EEJ6XOP_2vqRZRpvJlDMb4uy5A1HeOnpBFU0jzzSQqc2rsaoIvFAKZs3jHkjIQFOsGiPSC9sAkPEsCesHNgwNxz48r0Fy479E051SEqe0RjwF3VsrfZgMWZCB8Yd6-bhyuQUm_8J-IkKAvXdG1CL9NkoPENnSYHnS4qilIDGHiV8h5OB-kkbVJNY32PGetkUD3_1W7JaA7Mv2VTBavQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیشب به شدت این اپلیکیشن رو توی کانال‌های تلگرامی مختلفی دارم میبینم که گذاشته میشه به عنوان توییتر.
از هر کانالی که داره نشر میده تقاضا می‌کنم که نشر ندید و لینک گوگل پلی بدید.
به خدا گوگل پلی نه فیلتره نه چیزی.
نشر دادن این apk ها توی این شرایط یا از حماقته واقعا، یا از ندونستنِ مردم سؤاستفاده کردن.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4724" target="_blank">📅 23:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4723">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sOmjgcCiK7njR81VFxbfvfG6wADWt48FxKjmUIXFCvjPQLEBhf02sh0QazCt4Qyh87XlV8WEolc-nebswzXlQciKhhgRL6x1a-ZXn0Li8Ctl5tzGktoKKo7P5x65L1V8k1OIqLhZsNVxW6K9DEKvpGr5GePMu0cvtdwFbreUQ6VLTIPt_T2p-8jHq0X_YdHpEfRsrLMttAYgxRvnjAkdnR5_pCNLBqvh9kV3bPRFPeX_e-CNeuqZPSNynlzLJvWxGrn9-vZ6lt_TTl3L7Pu02MXOzs6obs7EMpaoGc5fzXE86syXiBLbzLIgJTj6jI2e1liGq8MgTdEdDy2FHuIKsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت Moonshot AI بالاخره مدل Kimi K3 رو اوپن‌سورس کرد و همون روز اول Telnyx بردش رو Inference API خودش. مدلش خیلی گنده‌ست (2.8T) و برای ران کردنش زیرساخت خفنی می‌خواد، به قول یکی از بچه‌ها در حد نیم میلیون دلار. ولی چون تلنیکس GPUهای خودشو داره ادعا کرده که سرعت و تاخیر رو خیلی خوب کنترل می‌کنه.
قیمتش هم فعلا در حد Sonnet 5 هست تقریبا، با قدرتی که میگن معادل Fable 5 هست که نمیدونم چقدر درسته واقعا
https://telnyx.com/release-notes/kimi-k3-telnyx-inference
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4723" target="_blank">📅 20:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4721">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pnqLljbfB6DXy1Q3JOyTdaptOYNqTPuRB-0fz6EZlNwcHLL0snhyWWRVxng45NRb2rZ9TvnbLNbBpRzQj3w-fbNAK-xeBfYGwxlI7V3w6YOje6dGYCAM9zGbacd9MjBiZGev4-hY78ECF1Vs5aiO9AJjQ9mUmpUwADs6AAHiJXH3xAmNb_FPO8op8Ix-sx6va0krXGzn4BYf8ev5CgBQsd8IiOnERv17kz07vkfj_2KjzAuviMkA9lvuDsnl7rG3kJiZBg_Eyrtu54v6v8xR1K2dofdiqnVECFCdc1RNMO4LwhU-X4wr-BMsc1fZZPZhauH7GMpqO4m9jhnIYIK42Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H_B8XSftgFnWzCiFaXhVMmGaJlNZu_cJkjRniN5EDhXQWKX477FVGjPgHiNlvXMsYRhB79DP4drgbPSyra7zbuaBr2qj42FJ6W4EVRGpJLZa38vRonHmXUU6QwPF_Xuv2Wo03I_tkw05drAX9_du8Yx-WU6NDLl6hPAMadsobm_YSm7baQ8Q-VUOeoPabUFchXoAlUh8I61pFm1kUgay4GgNoTtqAVFK0p9pK3vgirUONKdjDkk6gHGNjvPi0ptK-0mPlApmg9qrMPjbOUoFtUsHVB032JeWDwj4jK0Zio2kG2l6Ffheaq8j3jEdSpIUphUBxzxeWXCpYbhEBsTsjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سرور جدید CottonDNS برای تست در نسخه 1.6.0
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید  cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiZ2dzIiwic2VydmVyIjp7ImRvbWFpbiI6InYuYXNoZW50YWppci5zYnMsIGMuYXNoZW50YWppci5zaX…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4721" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4720">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بچه‌های WhiteDNS انقدر زود به زود آپدیتای خفن میدن من اصلا فرصت نمیکنم بذارم:)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4720" target="_blank">📅 14:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4719">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">به زودی کارهایی برای Aether-GUI انجام میدم
دلیل بررسی نشدن PRها همین بود</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4719" target="_blank">📅 14:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4718">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS   cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcn…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/4718" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4717">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/MatinSenPaii/4717" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4712">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.6.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/MatinSenPaii/4712" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4711">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRTUMdDDz0LdIPKZP2oyKUGtnF7kiTIkhY1X_rRf72y7bft0K2cU6HJbm4XvxESIyGMxsbMSDDyWDNMvPjsp2WXpjJbxnyK1Pu08M4U8MFljimimRVCmbp36LdfOAckA_rkydncHyP84gSAVawUcGavVvYDdlUIxw_QJWDcCwYVMBltkCM4iv1xYWIx1t4kzs1yzWJEolleKawZK6jtSiJdLdGSkhWBupc07-l23QuxS8kefhua_l8Pj_eczx_EBWBIqARFOrZSA10KQ3W7p7e5A1vZjOJ7ZaQuy9A7kaEFCReKszH7Qdmf64zN6v2mKmVrXoKvzYRZp7yDWNC8kGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
در این نسخه، پشتیبانی رسمی از موتور
CottenDNS
به WhiteDNS اضافه شده است.
CottenDNS برای اتصال پایدارتر در شبکه‌های دارای فیلترینگ، پکت‌لاس، DNS Poisoning و اختلال شدید طراحی شده و در هر دو حالت
Proxy
و
Full VPN
قابل استفاده است.
مهم‌ترین تغییرات
* اضافه‌شدن موتور CottenDNS
* پشتیبانی از چند دامنه در هر پروفایل
* تنظیم مستقل MTU، FEC، Duplication، رمزنگاری و روش انتقال
* بهبود Import و Export پروفایل‌ها
* بهبود رابط کاربری و دسترس‌پذیری
* سازگاری بهتر با Android 15
* ادامه پشتیبانی از پروفایل‌های StormDNS و MasterDNS
این نسخه انتخاب و مدیریت روش اتصال را متناسب با شرایط مختلف شبکه ساده‌تر و انعطاف‌پذیرتر می‌کند.
📱
دانلود WhiteDNS ورژن ۱.۶.۰
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚠️
⚠️
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0
@WhiteDNS</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/MatinSenPaii/4711" target="_blank">📅 14:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4709">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33e9f6f644.webm?token=F-KFPL_cFO6_NsnUpVQqsSDi_oxToLKegv_2Td78tnAjS03ZCmY4llMQsNjpNGaGYoW6d27Y3Zsz2UeeF8QNKwUpTrSO4fQZrnVENFDafITCzruFmpkyk35yEifNd2zitKncz2kXH6nTva5sIAEo3IMMiIWhgt-C0ykvQMjRdXJXzz-Wg2R26meBucrBhv6ixT0ea0Lor7P9Yh6CtuLSaI5mrZqaIHoICTxRNTzRb3XU1ucu-ZwO4GBZCydIE52QE7Ob4BCr-mKtVb1hX_ULNaanPIN1MEa2xYAnFHy28peQL9MejqnGtEXS9s0JgyTh01KLygUqTER40FsHfpPnsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33e9f6f644.webm?token=F-KFPL_cFO6_NsnUpVQqsSDi_oxToLKegv_2Td78tnAjS03ZCmY4llMQsNjpNGaGYoW6d27Y3Zsz2UeeF8QNKwUpTrSO4fQZrnVENFDafITCzruFmpkyk35yEifNd2zitKncz2kXH6nTva5sIAEo3IMMiIWhgt-C0ykvQMjRdXJXzz-Wg2R26meBucrBhv6ixT0ea0Lor7P9Yh6CtuLSaI5mrZqaIHoICTxRNTzRb3XU1ucu-ZwO4GBZCydIE52QE7Ob4BCr-mKtVb1hX_ULNaanPIN1MEa2xYAnFHy28peQL9MejqnGtEXS9s0JgyTh01KLygUqTER40FsHfpPnsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تخریب چرا؟ اندازه پنج جلسه تراپی کمکش کردم.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4709" target="_blank">📅 00:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4708">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بانو یه جوری تخریب کرد که فکر کنم طرف کلا توییتر رو دیلیت کنه بره به درس و مشق و کلاس‌های تابستونه کانون پرورشی برسه</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4708" target="_blank">📅 00:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4707">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PylTw58DoJZ_a1la5MnYwMZCepLwm5tqa3-UxkSt_kI9A4wpwgf097_dJo8jhP0jKmctb6Z5dp6WSwy0ZpBxutGvOMeLbY_QhusGTSvvPGlSJL5_k9L5iIxPK8CLdawqpD95E0MTyYwZMaKFId5V5dzrYSwqrmz47GW3M5REeHxgllZRZvJEZ1Sk6YzLVnvuVVp2Z1jAKD_DHJyHo-F6c0XPHLKPDc3oEz3my_ChLO8L-mGexDu6mOJ5bBO4EfhsdyNPVWjceMwtNHeqOHpmfVM7r93B0Vw-grh9lKtQcdLh24R7KfafGYk8gGtRZ0cUr6Hvva_TceOuXnHp6TCOtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو یه جوری تخریب کرد که فکر کنم طرف کلا توییتر رو دیلیت کنه بره به درس و مشق و کلاس‌های تابستونه کانون پرورشی برسه</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4707" target="_blank">📅 00:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4704">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IRLQzd81pdZHjQhT4SbdsTtJAW9ZwVnQW1Hp_4moFwT9JtSOmubPWGWGHaq2eASdtcgHVc7-_w0qfC4OzNppk5VKfVUQnvPW7zWxdP35bMJMi0Ai0g5e4uSWCard5UnKYnY5JhwQQ-x_ca6dvI10gnvzkI8_OplQ5jeyKa9z-2QEpWMYyfNo1mlo9l_w9e7ihOYodqg8GleG_K_GU9Y6QNf3aGfS_l_0w9Z7dPJ0AB4JdRLtpo0wh2BYmdcefkehk3UOdq8N6UCBQD4X00aqh-xDIFdhtQy6I9HNwhoVh6-bSeO_cpZODp3ke08u1siZqS3UJlvn2ZolHvS8HSr6fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BwoYjKyfKJpNsj9lMHqqoQsT-Gg-sFopZu8xObtZFQgnUdsrzEtykbgBrx6mYks3D3U3u3B0r98s8t8QG7ERlvWVQkKlo-MpEvgP0jMPEkFsH-yJt7P67f55m_w9GbpZ4zoLhZ6Mae0rn34fuzHhqiXA1HJzbcSsg6I_SX0_9KVUP-e363PrjWBdnLiWLjwqkRG_SW8AsicgDHPfkdLyxGJ111ABaxrts2W-A4W0_sILt0tQvBNqTJxpkEyTZjNyHJcScDndqXDlpWvvuhEZpjfJzxzXcJjkULUIvf6-ukBfdHEbsy5Nu-tXPR-Ow1fHdCddOVID1_DIx_bIJ6XjsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r9OSITIbR3fp-V0hAZMoMXSct1fAYBvNGMUZhjS07ZpY5YJcvfnhNSgoIts57E2Bu3glsN_PhgaIRLXsk1IQ8uK4LDP4OVruNXXEsCbGvGKFfY1o_OTcNkhXap18WTOk27-Omwc3uv2LogNijH9jOFHEWHS8LRc2w1Ub8j4omQEuS3axFf-cKhV8MDbOTSS6GaYfnMjD7GgPPxPvtfv_wMavflE9yiUG4EDjY9UDtEBdJ2sJl6fwahxgqGrDNhOJXQ87y8FYlN_3yuxu1GVXiGIzfG8MLc-v7GCTRFcsQBVGX9uH_P5Vg7bEu6kDTvjqqWru4LqvgXp25cahJLEgQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ماژول رایگان و قدرتمند حذف پس‌زمینه‌‌‌ی FeyNoBg
:
تیم شرکت Feyn از مدل جدیدشون به اسم FeyNoBg رونمایی کردن که برای حذف خودکار و فوق‌العاده دقیق بک‌گراند (حتی برای مواردی مثل تار مو در باد یا ویدیوی ضربات ایستگاهی فوتبال) طراحی شده. در کنار خود مدل، کتابخونه پایتونی که باهاش مدل رو آموزش دادن و اجرا می‌کنن به اسم NoBg رو هم به صورت کاملاً اوپن‌سورس روی گیت‌هاب منتشر کردن که می‌تونید همین الان روی هاگینگ‌فیس تستش کنید و از کدهاش استفاده کنید:
سایت اصلی:
https://usefeyn.com/blog/feynobg
مدل روی Hugging Face برای تست:
https://huggingface.co/feyninc/FeyNobg
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/4704" target="_blank">📅 23:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4703">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o9p1TaA3XAc-USOnASwRfyRAHu1SXi_s87IsCY8kuiH4e1QGYX4uU1u4d1GmF4T3quDO3KnksIYSnKct4Sd9l_WpMDnOnMDoKf578I2XF4T6dSxjxqhMY9rOsVUX0MV0bax9XnGYjjrdccO39nAESNFESwJpFQlgpaOVSccqtzqd4WIhsk6iKhbJydcRT2gv8dsPMR3vsoafUnua4PaaQrqfPIhL9BZ_gO8H7FyRNPsL5PU14QBtQRuKOTix16cFF_P25vgpFMQo4B5twNZ38AgvhhI8BxKZ_py3akYSzqoSZ6m4RPu0qKpjtMal4gRmMjqXQ0yIBBsfsBGrU_tbeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوشحالم که هنوز اشخاصی رو مثل سعید عزیز، در کنارمون داریم...
و ناراحتم از اینهمه آزار جنسی و تجاوز و پدوفیلی که توی دنیای واقعی و فضای مجازی میبینم که خیلی‌هاش هم متأسفانه منجر به خودکشی میشه.
ای کاش لااقل نهادی بود که مثل کاری که سعید سوزن‌گر یه تنه داره انجام میده، کامل و به طور رسمی و جدی پشت این قضایا بود. که این عوضیای بی‌صفت، نتونن انقدر راحت توی اینور و اونور با شماره کارتشون فیلم و عکس‌های این چنینی بفروشن
دردم میگیره اینا رو میبینم.</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4703" target="_blank">📅 18:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4702">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سالواتوره سن‌فیلیپو، هکر ایتالیایی و خالق Redis، توی مقاله‌ی جدیدش توضیح میده که نبوغ واقعی لینوس توروالدز(خالق لینوکس) فقط توی کدنویسی اولیه کرنل لینوکس نبوده، بلکه بزرگ‌ترین تصمیمش این بوده که خیلی زود کد زدن مستقیم رو کنار گذاشت و روی رهبری، هماهنگی و تعیین اهداف پروژه تمرکز کرد. برخلاف خیلی از مینتینرها که خودشون رو درگیر پیاده‌سازی جزئیات می‌کنن، لینوس فهمید برای مدیریت پروژه‌ای به این بزرگی باید زمانش رو صرف رهبری کنه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4702" target="_blank">📅 16:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4701">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پشت‌پرده بازار فروش غیررسمی توکن و کلیدهای API هوش مصنوعی
تحقیقات جدید نشون میده چطوری یه شبکه‌ی بزرگ (عمدتا توی چین) برای فروش توکن‌های LLM با تخفیف‌های سنگین شکل گرفته؛ این پروکسی‌ها از طریق سوءاستفاده از اکانت‌های Trial رایگان، ربات‌های پشتیبانی ناامن سایت‌ها و ترکیب کلیدهای API مختلف کار می‌کنن.
که برای به سرقت رفتن اطلاعات مهم استفاده میشن یا Train مدلهای AI چینی.
به زودی بیشتر تحقیق می‌کنم و بهتون میگم
https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything
اینم لینک مقاله‌اش
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4701" target="_blank">📅 03:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4699">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">خدا لعنت کنه این جاوااسکریپتو با این سینتکسش من ده تا زبان بلد بودم اومدم بکنمش یازده تا جاوا اسکریپت رو هم اضافه کنم بهشون، همشون رو یادم رفت الان فقط جاوااسکریپت بلدم
@Linuxor</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4699" target="_blank">📅 20:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4698">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">روی اوپن کد هنوز میتونید از nemotron3 انویدیا استفاده کنید</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4698" target="_blank">📅 19:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4697">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فعلا میریم nvidia(با اینکه delay زیاد داره) تا ببینم api رایگان امن چی پیدا می‌کنیم باز</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4697" target="_blank">📅 19:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4696">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مهم
راجب Mimo
😭</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4696" target="_blank">📅 19:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4693">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TxHopgJtXBN9sfCj5EtZJJRyGwBB-jNZQHpyCyArUsYKZQanig7HCwzuiFZzi6zzxX74qkeaq_wkFCQ77WnCte68tDL8svp8Bk9HDkjzn9ivH7Sd-HwZ2sFd8mOiL9Pn6fJbKNRQNGxQ6PTZeR9WxfHJbj_ycZ7e6AOcwPIpjlCpuoI4yGgWdiEmlltOlzSif1T-yopTKEm0SraOZGZ2iSrraIEDeyG8FDEGlg5s2OCxXuvRw2dA42RSgUKmgojAnhj2Sq7CP_tqtUgoDcTBeviV39UXUCkXSTrrpsbOJA_zuQfcHiFoLt183swz5HjF8qIUIuWfaPgOdUa_xinddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sy3-2ChZlD13PnFFnezWh2hbqje0s0UoTm0Tm9KEuGg8W7VbklT7Ee9k-ZpiWUApbiiwRHLxqzq-P8mAGnVx1o_VZ-EivmqiEwPE2FmnYT9ajrzdmyL4i3O7oq4Vqp9eESdv_362lGbYqEeXCxlvb3b278MsBsFDC0U4ltMRrNL4Y59ANm85QGFbaSQGDIhdv8Y4K0I2xp4pEq7icDWOXlIN0t-QFmw3KklheMQJnI0RBqMmyiw_hwVOqpMHA5ZHBMg_fgQzs4gx2TauPYjnfZDxX6PvdIORrJhxLUG630gzlHgh8TQzvL0GcV0rskLPMj0wOwZDi-5LH0AhIpxEKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A0j0ixY7FjJi99se9gQ0Vc2wTxNju0qJlotJ7rHZrGZPAiPtVkiQpsiie4ELAYvuHWpOfRURDrKaXJj0lFBfwD7FtkETkis9TreM0NNsGZ5kOqq9CMxhE5naALqn2K_clbpMxiOAkuhOTu_UV6fnmMsPP2zVzNttHpzZl1eqeE9fygsIMOSfXGfpkHS5_zvB3atZ5_Sn6jntiVzX995ont1bHaICSLrQqYXSJbJlvAONeL2yzGcy8Ayzn8gFCnZAMC84tmEAlu3MRTPOcUMy3ojokTBeeRCMmVl9FMh6_HtyN16MRO9TDd0tDkpV6W3VkKJD9l_NC-VepHY0Nk-l1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برای این از proxy relay کلودفلر که توی ویدئوهای قبلی یاد داده بودم هم استفاده کنید مشکل برطرف میشه دوستان</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4693" target="_blank">📅 18:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4692">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">همینطور اگر ارور the model provider is ratelimiting میگیرید، به خاطر شلوغ بودن سرورهای Mimo هستش طبیعتا از روش‌های دیگه‌ی api رایگان که توی ویدئوهای قبلی یاد دادم می‌تونید استفاده کنید برای 9router و بندازید پشت همون Combo</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4692" target="_blank">📅 17:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4689">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.2.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.3 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4689" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Aether 1.2.2</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4689" target="_blank">📅 15:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4688">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VHzuqZccMrQb4zVTzFXI3Z-lfnHHE_1xvTm6BOwNAs4r6ZyzazG6V-6drVChi9EQD2IzETxK8TGfdcRs6_RlfqNzyINzXmmJFoir77xqUk1SN51Eg7Uavv8Le38f-pTraL9eeyWEG8mSjom1xDykf-7CQUuT_QKGaV1ARKnOOeZY6yJcM9BkdYOY1CZx0FYOhiSadPT1Bclw_tdQ3OLDC2Y_I8isLukfBNdb74cG9cWo_n5oh7cp8upZqK9a-7uhJrfo5IIOb1dnTD2KUwnhhF28jSJK5inpo9yfCYaVAkLogFxqTe_A9qrPZaNt2yJMLDJ54oxxYHN__j02Bm-enQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
تازه‌های نسخهٔ ۱.۲.۲ کلاینت موبایل Aether
🚀
یک به‌روزرسانی بزرگ و بنیادین با تمرکز بر امنیت حداکثری، کاهش شدید مصرف منابع سخت‌افزاری و ثبات اتصال منتشر شد! در ادامه خلاصه تغییرات این نسخه را برای شما آماده کرده‌ایم:
🔄
۱. مدیریت خودکار و ارتقای هسته (Core)
ارتقا به نسخه پایدار ۱.۴: هسته تانل داخلی برنامه به آخرین نسخه پایدار ارتقا یافت.
خودکارسازی در CI/CD: فرآیند همگام‌سازی و اعمال پچ‌های اختصاصی اسکن رنج به صورت کاملاً خودکار و هوشمند در خط‌لوله بیلد گیت‌هاب پیاده‌سازی شد تا از بروز کوچک‌ترین ناسازگاری یا خرابی در فایل‌های نهایی جلوگیری شود.
🗑
۲. حذف کامل سیستم به‌روزرسانی درون‌برنامه‌ای (ارتقای امنیت)
افزایش شفافیت و امنیت: بخش دانلود خودکار درون‌برنامه‌ای به همراه دسترسی‌های پرخطری مانند REQUEST_INSTALL_PACKAGES کاملاً حذف شد.
دلیل فنی: برای اطمینان از اصالت کدها و عدم نصب ناخواسته فایل از منابع ناشناس، از این پس تمامی آپدیت‌ها صرفاً به صورت رسمی و امضاشده فقط از صفحه ریلیس گیت‌هاب پروژه قابل دریافت خواهند بود.
🌐
۳. حذف لوکیشن‌های فیک و واگذاری اتصال به هسته هوشمند
حذف منوی انتخاب کشور: از آنجا که شبکه WARP کلاودفلر از آدرس‌های Anycast استفاده می‌کند، انتخاب لوکیشن در کلاینت عملاً تزئینی بود.
اتصال هوشمند واقعی: در این نسخه منوی لوکیشن حذف شده و وظیفه اسکن رنج‌ها و انتخاب بهترین و نزدیک‌ترین لبه ارتباطی (با کمترین پینگ و پایدارترین حالت) به صورت پویا به خود هسته برنامه واگذار شده است.
⚡️
۴. کاهش مصرف رم، پردازنده و بهینه‌سازی رابط کاربری (UI)
کاهش مصرف CPU در حالت آماده‌باش (Idle): تغییر ساختار مانیتورینگ اتصال از حالت Polling به حالت Blocking روی پروسه هسته که باعث می‌شود پردازنده گوشی در زمان اتصال بدون ترافیک، به خواب عمیق برود.
حل نشت حافظه (Memory Leak): محدود شدن حجم لاگ‌های ارتباطی به یک بافر حلقوی ۸۰۰ خطی (حداکثر ۵۱۲ کیلوبایت) جهت جلوگیری از مصرف بی‌رویه رم در اتصال‌های طولانی.
رابط کاربری روان‌تر و سریع‌تر: حذف انیمیشن سنگین شفق قطبی (Aurora) در پس‌زمینه و جایگزینی با رنگ ساده ساکن که بار پردازش گرافیکی گوشی را به صفر می‌رساند. همچنین منوی تنظیمات پیشرفته اکنون بدون کوچک‌ترین لگی فوراً باز می‌شود.
🔌
۵. رفع تداخل با v2rayNG و حل مشکل نصب (Over-Install)
تغییر پورت‌های پیش‌فرض: پورت‌های اشتراک‌گذاری شبکه محلی Aether به 10810/10811 تغییر یافت تا با پورت‌های پیش‌فرض v2rayNG تداخل نداشته باشند. همچنین سیستم شناسایی هوشمند ابزارهای موازی اضافه شده است.
حل دائمی مشکل امضای دیجیتال: گواهی امضای اندروید در بخش بیلد تثبیت شد؛ کاربران نسخه ۱.۲.۱ می‌توانند بدون نیاز به حذف برنامه قبلی، نسخه جدید ۱.۲.۲ را مستقیماً روی گوشی خود نصب کنند و تمام تنظیماتشان حفظ خواهد شد.
🔒
۶. ممیزی امنیتی ۱۰۰ درصدی خط‌به‌خط
کد منبع برنامه تحت ممیزی سخت‌گیرانه قرار گرفت و از نظر مواردی همچون اطلاعات هاردکدشده، نشت DNS/IPv6، ذخیره‌سازی محلی ناامن و ترافیک رمزنگاری‌نشده کاملاً پاک‌سازی شد.
📥
هم‌اکنون نسخه ۱.۲.۲ را به صورت رسمی و امضاشده دانلود کنید:
https://github.com/QW-AI-Code/Aether
@whitedns</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/4688" target="_blank">📅 15:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4687">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">همینطور اگر ارور the model provider is ratelimiting میگیرید، به خاطر شلوغ بودن سرورهای Mimo هستش
طبیعتا از روش‌های دیگه‌ی api رایگان که توی ویدئوهای قبلی یاد دادم می‌تونید استفاده کنید برای 9router و بندازید پشت همون Combo</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4687" target="_blank">📅 15:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4686">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خوشحالم که این ویدئو برای خیلیا کاربردی بودش
🔥
روی یه سری آموزش دیگه هم دارم کار میکنم واستون</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4686" target="_blank">📅 15:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4685">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vRuaMYVFqVWT8oentQbHG41MPg6argTCT1XpzYoGJo3hOW8XjeDby9jZEL_xWdEYqfEUxqtcMGN4CPHIUUWl27lSaQ4XvWaeBBLeS2bq-KQENCS1SH9AKY1RNdxlmH83o5Dcbxapkvrby5V8boerrjcVHTf0l-b6DcYt4feORRnrIBd06y0MX707QtHPhRW80sfNBhLYjeD0ac42ZQmP-ntiJbEdmO0uW4cO7zEAtM2hM50G8cIWhdWumz_OyDwh6iwdQtSb_Bnvw-58UvHpSd1ccyYI7ofJuGF__e1U0mCbgMXD-3oImB37Ra37ibVNfqLI49-Ir-7R318x2WfGDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان اگر به ارور workspace has been restricted خوردین، باید یه ایمیل جدید بسازین، با ایمیلتون اول اکانت گیتهاب بسازید، و با اون اکانت گیتهاب توی railway ثبت نام کنید تا بهتون گیر نده و فکر نکنه اسپم هستید. خودم الان یه بار با continue with email ساختم دقیقا به همین ارور خوردم بلافاصله بعد از ساخت 9router، ولی درجا یه atomicmail تازه ساختم و باهاش یه اکانت گیتهاب ساختم و باهاش لاگین کردم، سریع ساخت 9router رو و گیر نداد</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4685" target="_blank">📅 05:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4684">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">عبارت VPS هم زیاد درست نیست. صرفا جهت شیوا بودن کاری که قراره انجام بدیم بیان شده
👍</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/4684" target="_blank">📅 04:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4683">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-railway.txt</div>
  <div class="tg-doc-extra">168 B</div>
</div>
<a href="https://t.me/MatinSenPaii/4683" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک‌های استفاده شده در ویدئوی بالا</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4683" target="_blank">📅 04:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4682">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rdLmah02mxCvj59Dj-zIjKBTMkqLpq6GeR62IaamRrleo0OaCDZaCp9lleiUUKVRWK_mvLw3q_q59YnGR1e0nVrEiwxWmvievHzUbbI3_znQHnxNJEUmwKFCaO39u7P3RNFCICv-sEYXNcPp_LJ6LfWbmRAtjUBUg0Xs8kXWfZKJvdDwBOXRVzNfD4HWZ6Ilyncl0k0Ie9d51lneKAIs_RXfYdtm5ZssDG0JE5Mh6IIBMmFIdlp2KX8gRUBHkPO2pzEqcpulTTG-54c9-HtQg_EsRAOVuxNOZObeIea_9XQV0Lid3XAZsWARM-ZP7LWOTFZlGu_oOdtleZY2zGmc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
هرمس رو با گوشی موبایل روی VPS رایگان و تلگرام اجرا کن! + آموزش بکاپ کامل از Hermes
⚡️
دستورات نصب استفاده شده در این ویدئو:
https://t.me/MatinSenPaii/4683
⭐️
توی این ویدئو:
1- بهتون یاد میدم چه شکلی با گوشی آیفون/اندروید/لپ‌تاپ، هم Hermes و هم 9Router رو به رایگان روی سرورهای Railway بالا بیارید.
2- وصلش می‌کنیم به تلگرام و از مدل Mimo رایگان روی OpenCode استفاده می‌کنیم و API 9Router رو ست می‌کنیم.
3- به طور کامل بهتون یاد میدم که چه شکلی می‌تونید از اکانت گیتهابتون استفاده کنید تا Hermes رو بهش وصل کنید و به راحتی، هر چند ساعت یک بار از تمام داده‌هاش برای شما بکاپ بگیره.
4- به علاوه روش ایرانیزه شده‌ی استفاده نامحدود از کردیت رایگان 5 دلاری Railway
😂
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api و سرور رایگان هم استفاده شده توی کل ویدئو
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4682" target="_blank">📅 04:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4681">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فکر کنم من تنها کسی باشم که از اینکه مردم از کانالش لفت میدن خوشحال باشه
😂
به خدا حس میکنم هرکسی لفت میده، جمع اینجا خلوص بیشتری پیدا میکنه و اصلا کیف میکنم
شبیه عصاره‌گیریه</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4681" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4680">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">منم دارم یک چیزی برای بچه‌های کانال آماده میکنم که با گوشیشون هر جا که میرن، رایگان، بدون فشار اومدن به منابع گوشی و روی هر گوشی‌ای(آیفون/اندروید/...) بتونن با بکاپ گیتهاب، هرمسشونو راه بندازن و از تلگرام باهاش چت کنن 24/7 خیلی باحال میشه</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/4680" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4679">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DIw6hWmyNvnyy7csqV48dF7hGh9eTbwZXH1XQsQiigjFXOtujMmQ6lVudo7a-QJ3G8yFGKQvcu6jDt3KfUdcnQeRLPJeJbYQfrRXw5DiY7vGyE7Ju7OglCSYH44NnHN4g2aSwyJOcoVqjz2fJ5di_uTO_RnoS4Ru4tWjNf4I4qLy_uO4G1Ybon6ciqBcNh9tPM_UUiGFNCAPmVxNGq8eKtmEqxbK9Z37vhOzC_3JM15onXttY_TujPTkj3DnG8WpVfMKnFnGmpKWpk0s3ibqFD_UjE_jr2E9arC5WJEUkUf4MhvA5tZb8ca9nQ0Pmko3iaEKOQri9_mMsI9ngEkxFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم دارم یک چیزی برای بچه‌های کانال آماده میکنم
که با گوشیشون هر جا که میرن، رایگان، بدون فشار اومدن به منابع گوشی و روی هر گوشی‌ای(آیفون/اندروید/...) بتونن با بکاپ گیتهاب، هرمسشونو راه بندازن
و از تلگرام باهاش چت کنن 24/7
خیلی باحال میشه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4679" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4678">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">برو برو
🥰
موفق باشی بعدا میتونی معرفیش کنی خودت و بگی چطوری توی تحقیقاتت کمکت کرد</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4678" target="_blank">📅 01:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4677">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خجالت کشیدم، میرم پروژه رو راه میندازم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4677" target="_blank">📅 01:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4676">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تینا شاگرد نمونه‌ی منه و به ترسش غلبه کرد و هرمس رو راه انداخت
❤️
پرسید، تلاش کرد، به ارور خورد، و آخر سر تونست با اینکه تجربه‌ی چندانی از کار با کامپیوتر هم نداشت</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4676" target="_blank">📅 01:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4675">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">باعث خوشحالی منه</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4675" target="_blank">📅 01:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4674">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">من به شما افتخار میکنم.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4674" target="_blank">📅 01:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4673">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">در مورد این، یه وقتایی به نظرم بهتره آدم کمی پروژه‌های پیشرفته‌تر ببینه که هم بدونه دانشش در چه حدیه، هم یه دیوار جلوی خودش ببینه. نه برای اینکه بترسه، بلکه برای اینکه بدونه دیواری هست که میتونه ازش بالا بره! و انگیزه‌اش بشه. من خیلی از مطالبی که میفرستم اینجا…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4673" target="_blank">📅 00:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4672">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">امروز اولین جلسه ی کلاسم با متین برگزار شد و واقعا دوسش داشتم
🌱</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4672" target="_blank">📅 00:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4671">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">موافقم و روش تدریست رو خیلی دوست دارم. اما خب، شاید برای کسی مثل من که کلا هیچی از دنیای کدزنی و چیزهایی که آموزش میدی نمیدونم کمی ترسناک باشه این موضوع  این‌ روشی که بهش اشاره کردی رو توی کلاس هم پیش گرفتی و اونجا به من هم حس اینو داد که خب وقتی متین نمیگه…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/4671" target="_blank">📅 00:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4670">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خود هرمس و راه‌اندازیش مثلا شاید یه دیوار بوده برای خیلی‌ها.
من و بقیه‌ی بچه‌ها توی توییتر و تلگرام و اینور اونور، طبیعتا تجربه‌ی کار با کامپیوترمون بیشتر بود، زودتر راه انداختیم.
انقدر نشستیم بالای دیوار و از منظره تعریف کردیم، که چندین نفر دیگه هم ترغیب شدن و تلاش کردن بیان و بهش غلبه کردن.
چون واقعا کامپیوتر، و همچین مفاهیمی که شاید برای یه سری از دوستان ساده به نظر برسه، برای عده‌ی زیادی اولش ترسناکه. و باعث میشه فکر کنن خب، اونا که تونستن از پسش بر بیان باهوشن یا هر چیزی، و من نمیتونم.
که اصلا درست نیست.
کامپیوتر و این مطالبی که اینجا قرار میگیره
همه‌اش مهارته.
و هر کسی با تلاش و پشتکار، بدون استعداد، میتونه یه مهارت رو یاد بگیره.
شاید یکی زودتر یاد بگیره، سریعتر متوجه بشه، ولی در نهایت همه با تلاش می‌تونن بهش برسن</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/4670" target="_blank">📅 00:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4669">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اما تفاوتی که هست اینه که تمرین‌هایی که توی کلاس میدی در راستای چیزیه که بهم قدم به قدم یاد دادی اما مثلا اون پستی که برام فرستادی برام آشنا نبود اصلا</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/4669" target="_blank">📅 00:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4668">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">موافقم و روش تدریست رو خیلی دوست دارم.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/MatinSenPaii/4668" target="_blank">📅 00:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4667">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">به نظرم این شکلی یادگیری خیلی مؤثرتره
😂
موافق نیستی؟ آدم اگه 5 بار هم قدم به قدم جلو بره با ویدئو یا آموزش یه نفر دیگه، خودش اگه یه جا گیر کنه ممکنه نتونه انجام بده ولی اگر خودش درگیر بشه، واقعا تأثیری که داره صدهزار برابره.  بچه‌هایی که تازه اومدن توی کار،…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/4667" target="_blank">📅 00:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4666">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">من تاحالا وارد گیتهاب نشدم، پروژه گیتهاب دادی بهم گفتی برو برای خودت درستش کن
😭
😂</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/4666" target="_blank">📅 00:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4665">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">:)) کاملا درسته بانو
❤️</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/4665" target="_blank">📅 00:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4664">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شما فکر میکنید متین به سوالاتتون توجه نمیکنه و برای همین جواب نمیده اما روش تدریس متین اینطوریه که تمام چیزی که نیازه بلد باشی برای اینکه خودت بری دنبال یک چیز رو یاد میده و بعدش خودت باید تلاش کنی تا ازشون درست استفاده کنی.  دیروز یه پست برام فرستاد از هرمس،…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/4664" target="_blank">📅 00:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4663">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شما فکر میکنید متین به سوالاتتون توجه نمیکنه و برای همین جواب نمیده
اما روش تدریس متین اینطوریه که تمام چیزی که نیازه بلد باشی برای اینکه خودت بری دنبال یک چیز رو یاد میده و بعدش خودت باید تلاش کنی تا ازشون درست استفاده کنی.
دیروز یه پست برام فرستاد از هرمس، بهش گفتم من هیچی نمیفهمم:>>
گفت جلسه قبل بهت یاد دادم چطور چیزی که بلد نیستی رو با استفاده از AI ساده‌سازی کنی برای خودت..</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4663" target="_blank">📅 00:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4662">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یک کاری دارم میکنم مربوط به هرمس و مدل رایگان و ران کردن هرمس روی گوشی بدون هزینه و 24/7
نتیجه خوب بود بهتون میگم
😁</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/4662" target="_blank">📅 00:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4661">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بیش از ۹۰ هواپیمای سوخت رسان آمریکایی در اسرائیل حضور دارند و هواپیماهای ترابری به صورت گسترده و بی‌وقفه درحال پرواز به سوی اسرائیل هستند.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4661" target="_blank">📅 22:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4660">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">یکی از دوستان برای OpenWrt یک پنل مدیریت نوشته.
این پروژه یک اسکریپت نصب برای Aether روی روترهای OpenWrt است که امکان مدیریت از طریق LuCI و CLI را فراهم میکنه
https://github.com/moein8668-git/aether-openwrt-client
خودم تستش نکردم
اگر مشکلی یا باگی مشاهده کردید لطفا به توسعه‌دهنده اصلی گزارش بدید. (Issue)
توجه: این پروژه فقط برای روترهای OpenWrt طراحی شده.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4660" target="_blank">📅 22:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4659">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اگه بک‌اند کار می‌کنید و Go می‌زنید، پروژه‌ی Gsxui احتمالا براتون جذاب باشه. این پروژه کامپوننت‌های فرانت‌اند استایل Shadcn رو مخصوص اکوسیستم Go زده که اگه با ابزارهایی مثل HTMX ترکیبش کنید، می‌تونید خیلی سریع وب‌اپلیکیشن‌های تمیز و مدرن بسازید بدون اینکه درگیر فریم‌ورک‌های سنگین جاوااسکریپتی بشید:
https://ui.gsxhq.dev/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4659" target="_blank">📅 19:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4658">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⏺
عراقچی: کتاب نوشتم، «قدرت مذاکره» نتیجه‌اش هم داریم می‌بینیم.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4658" target="_blank">📅 16:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4657">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
برای اینکه مطمئن بشی VPN درست کار(نشتی ip نداره) می‌کنه، می‌تونی از سایت BrowserLeaks استفاده کنید. این سایت IP فعلی، موقعیت تقریبی، اطلاعات شبکه و همچنین تست DNS Leak و WebRTC Leak رو نشون میده تا مطمئن بشی
#اطلاعات
واقعی اینترنتت لو نمیره. اگر بعد از اتصال به VPN، آی‌پی و DNS نمایش‌داده‌شده مربوط به سرور VPN باشه و نه اینترنت خودت، یعنی اتصال به‌درستی برقرار شده و نشتی وجود نداره.
این سایت ها
#امنیت
سرور و نشت در اپ ها رو نشون میده:
https://browserleaks.com/ip
https://myip.theazizi.ir/
@xsfilterrnet
👑
@xszapass
🤩</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4657" target="_blank">📅 15:04 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4656">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تا اکانت گیتهاب سازنده‌ی Aethery اندروید درست میشه، به هیچ وجه از پروتکل MASQUE روی اپ اندروید استفاده نکنید.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4656" target="_blank">📅 05:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4655">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tHnO5FZHO2RMVwebP9-GSI5PstRUyX1-8rWjWf5U-iEzyR7h6R8lKDJLJJL7ADmGKcdnqBfERuAu1vX6EMgFH9nbqgxvzdvB9LXLVMWuNfenj4IM-NkklXiRjk_NrpFtXhS19CRUFijSY5nuOgXpRr3YDpYerPOq7MQYEnqY8Mxo-T7FissfxPmEEPIWzTMn187jeGYca3IqUjlxXQaVlMziAy-B46fBJU6U8d2bG1fl3fuMDlZWDnpEDZFouoGiTRZCWt2o3YLXrP_0bvsME60RE3Qqz5jy2Om2EtwX70t8LzH3Q7uJrrEh2_XYPGlizuPpJkS8u6Vzu3cRfhwqQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!
هسته‌ی برنامه رو به نسخه‌ی جدید v1.4.0 ارتقا دادم. تو این نسخه تمرکز اصلی سازنده روی تأمین امنیت MASQUE، فیکس کردن باگ‌های مموری و بالا بردن پایداری اتصالات WireGuard و Gool بوده.
منم یه مشارکت کوچولویی روی خود هسته داشتم.
تغییرات اصلی این آپدیت:
1-
امنیت در پروتکل MASQUE:
قبلاً وقتی وصل می‌شدید، کلاینت هیچ تاییدیه‌ای از سرور نمی‌گرفت و اگر کسی وسط راه سعی می‌کرد با یه سرتیفیکیت فیک گولتون بزنه، برنامه متوجه نمی‌شد. اما الان اتصالات MASQUE سرتیفیکیت سرورهای کلادفلر رو به صورت دقیق (از طریق هش‌های SPKI) بررسی می‌کنن تا دیگه کسی نتونه ترافیک رو شنود کنه.
2-
پایداری WireGuard و Gool:
قبلاً بعضی وقتا برنامه بهتون می‌گفت متصل شدید، در حالی که دیتا اصلاً ردوبدل نمی‌شد و فقط روی یه پروکسی SOCKS5 گیر کرده بود. اما الان یه سیستم بررسی سلامت (Health Check) مداوم داره که اگر دیتایی از سمت سرور برنگرده، خودش به صورت اتوماتیک اتصال رو قطع و دوباره وصل می‌کنه.
3-
اتصال مجدد خودکار در Gool:
تو نسخه‌های قبل اگه تونل بیرونی Gool قطع می‌شد، کل فرآیند کِرَش می‌کرد و خارج می‌شد. الان Gool هم مثل بقیه پروتکل‌ها خودش هوشمندانه دوباره ریکانکت می‌کنه.
4-
فیکس شدن نشت مموری (Memory Leak):
یه باگ رو اعصاب بود که وقتی اتصالتون زیاد قطع و وصل می‌شد، تسک‌های قدیمی تو بک‌گراند باز می‌موندن و آروم‌آروم رمِ سیستم پر می‌شد. این مشکل تو تمام پروتکل‌ها کامل برطرف شد.
5-
هوشمندی در مصرف منابع:
از این به بعد Aether همون اول کار، تعداد هسته‌های CPU و مقدار رم سیستمتون رو می‌خونه و میزان اسکن همزمان (Concurrency)، بافرهای شبکه و صف‌های داخلیش رو بر همون اساس تنظیم می‌کنه. این قابلیت برای کسایی که می‌خوان ابزار رو روی روترها و بردهای ضعیف‌تر بالا بیارن فوق‌العاده‌ست.
لینک گیت‌هاب برای دانلود(نسخه‌های مک، لینوکس و ویندوز):
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.6.0
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/4655" target="_blank">📅 05:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4654">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lVdgtE_cYp8ZcNJRh4Nd4x1CsikP_gbECj7tZdEKX_bkxxDtVB7tRnmd5xvlEs0QD69SqOK6xmxZf95vzAg5pnA3XcbWvORWfO13e4LU-GbO0avEVqiKvOHR8hsux8fYp1cgTg2Ju1EIb2JGLC0sBejVcEy3BEHl1QensDDPiUWREBQffTFSsCy8GCnjCWOzYDXArKMipMBVWILkKF7wk4QPx9_j6G-sphgmZ4vn4mrU7F0EDJqZ2OARfiT1iwRcHNPQFRWvgrnEYxCFW6U3hqN--coviiHZm3zoOTSuz7dq_5Ucl_nmbv7GKKQydB-vLWR8bURl3pI_1w164pN6mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با تشکر از علیرضای عزیز بابت تیزبینیش و زحمتای @CluvexStudio  این مشکل خطرناک که شانس MITM داشت حل شدش. حتما aether رو به نسخه‌ی 1.4.0 به روزرسانی کنید. آپدیت GUI هم به زودی منتشر میشه https://github.com/CluvexStudio/Aether/releases/tag/v1.4.0</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4654" target="_blank">📅 05:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4653">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آپدیت جدید Aether v1.4.0  https://github.com/CluvexStudio/Aether/releases/tag/v1.4.0  توی این ورژن بیشتر رو امنیت و پایداری واقعی اتصال کار کردم (توصیه میشه حتما آپدیت کنید) :  فیکس امنیتی مهم: توی ورژن های قبلی اتصال MASQUE اصلا سرتیفیکیت سرور رو چک نمی‌کرد…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4653" target="_blank">📅 05:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4652">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">آپدیت جدید Aether v1.4.0
https://github.com/CluvexStudio/Aether/releases/tag/v1.4.0
توی این ورژن بیشتر رو امنیت و پایداری واقعی اتصال کار کردم (توصیه میشه حتما آپدیت کنید) :
فیکس امنیتی مهم: توی ورژن های قبلی اتصال MASQUE اصلا سرتیفیکیت سرور رو چک نمی‌کرد (verify کاملا خاموش بود)
یعنی از نظر تئوری یه نفر که بین شما و کلودفلر قرار بگیره میتونست یه سرتیفیکیت جعلی بده و ترافیک رو ببینه الان اضافه کردم که سرتیفیکیت edge کلودفلر با هش‌ های واقعی که pin شدن چک بشه هم روی HTTP/3 هم HTTP/2 این رو یکی از کاربرا (Matin Senpai) گزارش داد و خودش هم pull request فیکسش رو فرستاد بررسیش کردم درست بود، مرج کردم :))
فیکس مهم دیگه روی WireGuard و گول (WARP-in-WARP): گاهی اوقات "Connected" میزد ولی داده رد نمیشد. الان هر دو مدام چک میکنن که واقعا داده از طرف مقابل میاد یا نه.
اگه یه مدت هیچی نیومد خودش میفهمه تونل مرده و خودش دوباره وصل میشه. گول هم قبلا اگه تونل بیرونی قطع میشد کل برنامه میبست. الان اونم دیگه ریکانکت میزنه.
یه لیک هم فیکس شد: هر بار reconnect میشد (روی مسک یا وارپ) تسک‌ های پس‌زمینه‌ قبلی درست بسته نمیشدن. که روی نشست‌ های طولانی با قطعی زیاد رم رو الکی بالا میبرد. الان هر reconnect درست پاکسازی میشه. :))
--verbose
قبلا همه‌چی رو یهو میریخت بیرون که خوندنش سخت بود برای بعضیا که الان
--log-level
اضافه شده با ۵ سطح:
error warn info debug trace
دیگه راحتین :))
حالتِ info آرومه و عادیه
debug
جزئیات تونل رو نشون میده
trace
همه چی رو حتی تک‌تک پکت‌‌هارو
و...
Aether
الان موقع اجرا رم و تعداد هسته سیستم رو خودش میسنجه و اسکن و بافر ها رو خودش تنظیم میکنه که روی روتر یا برد ضعیف زیاد مصرف نکنه. با
--perf low/medium/high
هم میشه دستی مشخص کرد.
پشتیبانی از OpenWrt کامل‌ تر شد: علاوه بر armv7
الان بیلد استاتیک برای x86_64 و aarch64 هم هست
aether-linux-x86_64-musl.tar.gz
aether-linux-aarch64-musl.tar.gz
لینک اصلی پروژه:
https://github.com/CluvexStudio/Aether</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4652" target="_blank">📅 04:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4651">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مدل Opus 5 توی یه سری بنچمارک‌ها از Fable 5 هم قدرتمندتر بوده توی کدنویسی
با نصف هزینه
ای کاش زودتر بیاد توی کلاد کد تست کنیم. فعلا توی اپ اومده</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4651" target="_blank">📅 00:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4650">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/26436ea3fa.mp4?token=Z9IaTctb4zsp16nJg-cjvz14-KsHVmI5gJbE0D0XTuR2skrfXRDGA4U_MnEc2UetROw6GPVIVAc12dm5pMtHU4vmMoIiJD-hyDa60LAm2H_vOhUBSB6qBOPzAngaPukDccZGA4Gt0ly5UIyiNKuubT512zrTwFkZLuOU9DLVRfRuqG2UuEfTbxadq5vkEL-LpxTVG2fI8NiBtRPZYpgtxsTzlcnbSr1BmzN13thyhw7PscUFWB8FMmdJ1VcTDauhkDtACTU3GHPN43wCnxY810P4NnxlmA3FHh7_x1Yjb8s3iOYjiqBITS3iKozDY18_8oZSFYmoy2BdTmSE4Dm4xFes3jYgzCuoM2wGbHOU-UsfsKfPaVGTshHahX9CrBx9xm4soQnByhKiffliMgza0NEeGEvXcmeZo-1k9R1HndMhWM22uLcw-lt3kpMHWkX79d_izxgvFFQQipNNlczxX--l9yT4f7VWYJ7p53XHIDOC3eJFKmM-sIYIcd9AhsIHXQhkh3MrsyxNK-QyrnUViS0hTr1Q2Bn2S2E980FrUyDcb9pmlL0UA40NgqudjcYJhT79S8lz22qoIuZekEXMj7dqp4oU2e4QRlrih9Sfr2OzJOWXYJlEkzKP80WDn7DVZ4y9nA8V1t7Ymisii2JCzr5JoZQaPTmqhb3ngPcGv9U" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/26436ea3fa.mp4?token=Z9IaTctb4zsp16nJg-cjvz14-KsHVmI5gJbE0D0XTuR2skrfXRDGA4U_MnEc2UetROw6GPVIVAc12dm5pMtHU4vmMoIiJD-hyDa60LAm2H_vOhUBSB6qBOPzAngaPukDccZGA4Gt0ly5UIyiNKuubT512zrTwFkZLuOU9DLVRfRuqG2UuEfTbxadq5vkEL-LpxTVG2fI8NiBtRPZYpgtxsTzlcnbSr1BmzN13thyhw7PscUFWB8FMmdJ1VcTDauhkDtACTU3GHPN43wCnxY810P4NnxlmA3FHh7_x1Yjb8s3iOYjiqBITS3iKozDY18_8oZSFYmoy2BdTmSE4Dm4xFes3jYgzCuoM2wGbHOU-UsfsKfPaVGTshHahX9CrBx9xm4soQnByhKiffliMgza0NEeGEvXcmeZo-1k9R1HndMhWM22uLcw-lt3kpMHWkX79d_izxgvFFQQipNNlczxX--l9yT4f7VWYJ7p53XHIDOC3eJFKmM-sIYIcd9AhsIHXQhkh3MrsyxNK-QyrnUViS0hTr1Q2Bn2S2E980FrUyDcb9pmlL0UA40NgqudjcYJhT79S8lz22qoIuZekEXMj7dqp4oU2e4QRlrih9Sfr2OzJOWXYJlEkzKP80WDn7DVZ4y9nA8V1t7Ymisii2JCzr5JoZQaPTmqhb3ngPcGv9U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از کاربرا اومده توی توییتر یه مقایسه‌ی خفن بین مدل‌های Claude Opus 5.0 و Fable 5 Max برای ساخت کدهای فضای 3D (توی وب) انجام داده.
نتیجه این شده که تکسچرها، نورپردازی‌ها و جزئیاتی که Opus 5.0 تونسته خلق کنه، اونقدر باحاله که هیچکس باورش نمی‌شه همه‌ش فقط با کد زدن ( و بدون نرم‌افزار گرافیکی) درست شده باشه.
البته مدل Fable 5 هم این فضا رو با یه بار تلاش (One-shotted) در آورد، ولی خروجیش جای کار و بهبودی داره.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4650" target="_blank">📅 20:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4647">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اگر نمیدونید معماری پردازنده‌تون چیه، این نسخه رو نصب کنید
Universal</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4647" target="_blank">📅 14:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4642">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">20 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4642" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4642" target="_blank">📅 14:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4641">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6kUuQYKO7iddyXDWkS81Y3JzI_--CglhbT4wzA3HsdfGrUlHWvbuJiVwKBiBMbKSi6i7erbgF-MWBurZWTx5okqvdgsipV9poahV8xYlly5FaX5z_7MixRcHIkGdHzyZM3l2vD1MRoOCuiGGNzqsrurvjdL_g8unzE1OhcJHTR50rAFIxmqwSuBamEIG4EfdguJX1gqllG14xa21_De9EQVJaZmcJ-zk39JyOMgV7cfLz_3l4XDPjf8jxjdIuXXteSaUs0bssq0rLCmJeP2iY8VOzHgak6vfnzoJfFwkpVn_ZAMm-sjvkDHn2R2_7PP7vJoMXaBk6kHZIBmtRoqWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN
• پشتیبانی از فارسی و انگلیسی
• انتخاب پوسته روشن، تاریک یا هماهنگ با دستگاه
• ارتقای هسته Mihomo به نسخه v1.19.29
• مدیریت بهتر سابسکریپشن‌ها و کانفیگ‌های دستی
• پشتیبانی بهتر از WireGuard، WARP Pro و Amnezia Noise
• بهبود اتصال روی Wi‑Fi و شبکه‌های محدود
• بررسی واقعی سلامت اتصال و استفاده خودکار از Clean IP
• تنظیمات پیشرفته شامل TLS Integrity، DNS رمزنگاری‌شده، Split Tunneling و IP Fronting
این بهینه شده تا با ورژن جدید BPB  به خوبی کار کنه.
برای استفاده از اپ، سابسکریپشن های Mihomo را از پلن BPB داخل اپ وارد کنید.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4641" target="_blank">📅 14:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4640">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4640" target="_blank">📅 02:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4639">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KPZrQdRFwhSS1tWlx0Rrq5Rcksi_ieyrwhvkGYKTOYYCvguzYjcbosQ11EARI8rUakU5Her_-cmznQi0ukwovFy-8tki7GQzfLS6upErNpr6Pw8a7W9lcuW8bYACwCRZUN57eOIhfwwTOuFpieeoZnMW0MYe18CICdb-Mv5YNRjLydaY6Qtiyw7lphA5Lbx2odhh_Y4YCbT3kwnwyP2eR3BxENwRC724uYiG1Sr2EbeHUV29WpH-cR5CPwNGT2QrrnG5cNgpX4XKOhH5oeX9GPV4e9uMH4V6zEcHi147HnxWEWEtqCf38zlUiRMZpD750HBp58EshwMFvg-FevYUaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استارتاپ Screenpipe ابزاری ساخته که تمام تصویر و صدای سیستم رو به صورت لوکال ضبط می‌کنه. این ابزار به Agentهای هوش مصنوعی یه «حافظه قابل جستجو» میده تا بدونن چی دیدین و چی شنیدین، که برای اتوماتیک کردن کارای تکراری و ساخت SOP خیلی کاربردیه.
میشه گفت رقیب اوپن سورس کلاد توی این مورد
https://github.com/screenpipe/screenpipe
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4639" target="_blank">📅 01:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4638">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انگار دارن یه چیزی رو روی فایروال تست میکنن</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4638" target="_blank">📅 17:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4637">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یهو خیل عظیمی از آیپی تمیزهای range 104 کلودفلر واسم از کار افتاد
ایشالا که خیره</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/4637" target="_blank">📅 17:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4636">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyPgCvMuISuFbCiLos4ptU5G8rYHxQ1EMFiS6fgf1SR6V1b5fif5olK_pgOHp147qf7YHdIkKqE79uEI-YOJkec0NC_ULRY8YlWspROske8kHFrPZ8O1AkKucu_zozZNFaFhAxRIm9osg0Ojg5qZgiYp9LHsB8C7x268dpMWRZ6u1ffAZde9zubkdanzPRTQt2zUNfri_AsN9UybwLVpjrjP0F02JpxYxomeWpfJqiNTDPWHSLeVxdgoA6ssV-ZYGZMNWPdJy_VDO3f5y4dsQaQeQt0XH-kpSV-7gf7DrYTEkoxE2xuuPGJXsGy__aVdXTNRVRTDWEFl7gvkx8nMJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین سرور اختصاصی برای اپ WhiteDNS
🌐
Tunnel domain:
v.anonymous.observer
🖥
IP:
78.135.93.50
🔐
Encryption method: 3
روش رمزنگاری را روی AES-128-GCM تنظیم کنید.
🔑
Encryption key:
b275039199b1c8c9
➖
➖
➖
➖
➖
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4636" target="_blank">📅 13:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4635">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XteVewkQiRsaaBxFyQpgQ0i_aB_aIrNFbpWBTkX1ha6hhQgWvEEygqxLSdZlwBAUy2ywNBPtwq5zMYXrnDOFfcD_MmekvSP2M2gmypPeln9N-j9ZhTD-jPoOeDewQQlEglkla6eHkxWmLg8Gr1f3wMdZKjKRw8wgJP6PqWDDby6NS5yd1-0XkS7MkvZH45yuf9myUK-Um4q56qztAG5How53e5Iat4YMXMLCeJ2j26WDCW2CMutlKbzdMlfWqdqSjZQ1AUPo2HFsVTRS9Eomg724ehkUseww3aiSnHbg7RiUaifuGF-zOSEgJdlR-IRX62EIYMr6dga2gBphx98eCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام
😭
اکانت Nous Research سازنده‌ی هرمس ریپلای زد روی توییتم
ولی واقعا قدرت این ترکیب hermes+9router+opencode+mimo هنوز باورم نمیشه که از پس این تسک پیچیده بر اومد</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4635" target="_blank">📅 04:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4634">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بچه‌ها من اگه کمتر هستم این روزا، چون دارم روی یه سری ویدئوی کاربردی کار میکنم که اگر اینترنت قطع شد به دردتون بخوره. و یه سری مهارت که تا اینترنت قطع نشده بهتره یاد بگیرید که بعدا اگر لازم شد آموزشی بدیم، بتونید سر راست برید سراغش</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/4634" target="_blank">📅 02:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4633">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard  https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/4633" target="_blank">📅 21:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4632">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard
https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4632" target="_blank">📅 19:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4631">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دقیقا. درخواست نوشتن راجب ریتالین هم داریم چون متاسفانه خیلیا به خطراتش آگاه نیستن</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/4631" target="_blank">📅 18:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4630">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">متاسفانه من مثال‌های واقعی زیادی از مصرف خودسرانه خیلی از دارو ها دارم میبینم و متوجهم که ما همیشه دنبال یه راهی هستیم که زودتر جواب بده، اما همین راه‌ها هم بدون آگاهی ممکنه شرایط رو بدتر کنه
❤️</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/4630" target="_blank">📅 18:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4629">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">این روزها خیلی‌ها رو می‌بینم که وقتی خوابشون به‌هم می‌ریزه، به ملاتونین پناه می‌برن؛ و چون بدون نسخه در دسترسه و یک هورمون طبیعی در بدنمونه، خیلی‌ها فکر می‌کنن حتی اگه یک سال هم ازش استفاده کنن، کاملاً بی‌ضرره.  ملاتونین در مصرف کوتاه‌مدت برای خیلی از افراد…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4629" target="_blank">📅 18:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4628">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این روزها خیلی‌ها رو می‌بینم که وقتی خوابشون به‌هم می‌ریزه، به ملاتونین پناه می‌برن؛ و چون بدون نسخه در دسترسه و یک هورمون طبیعی در بدنمونه، خیلی‌ها فکر می‌کنن حتی اگه یک سال هم ازش استفاده کنن، کاملاً بی‌ضرره.  ملاتونین در مصرف کوتاه‌مدت برای خیلی از افراد…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/4628" target="_blank">📅 17:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4627">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBloom.(Tin.)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwB43X9a19z_Rogq3RNl9VLIo_mZiT2DlHhK8owT0PC0B31VkfTQ0zM3uhtxSGmi_NTtIKMcyuv5OgQlekXQ9eeh7CDwFgQBx0IeipWD4LzspQmqvPZ5BGmYUTAUdPiKszQrDMEAxmy9OJ-K3CafZfQcwpFseEwdsD2o6MpgcNmc-eCfb4zEHK1qmiNoOEmC4iY7Ur62cbzycbAF0SA8LTQrXB0ZauDVDH09aKbkXYe9QhyCWUI4p4GZAIc1ytMytIGiR-8jOPspIcYKaOEbLyctkOI7YfQrwiazDzlrDatDEpWJHq8b1KrsACB_Xe33VnOegBq4y3UHkLlpFdtunQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این روزها خیلی‌ها رو می‌بینم که وقتی خوابشون به‌هم می‌ریزه، به ملاتونین پناه می‌برن؛ و چون بدون نسخه در دسترسه و یک هورمون طبیعی در بدنمونه، خیلی‌ها فکر می‌کنن حتی اگه یک سال هم ازش استفاده کنن، کاملاً بی‌ضرره.
ملاتونین در مصرف کوتاه‌مدت برای خیلی از افراد ایمن محسوب می‌شه، اما درباره استفاده طولانی‌مدت هنوز اطلاعات کافی نداریم. بعضی مطالعات، مصرف طولانی‌مدت اون رو با افزایش برخی مشکلات سلامتی مرتبط دونستن، هرچند هنوز رابطه علت و معلولی ثابت نشده.
از طرفی، عوارضی مثل خواب‌آلودگی روزانه، سردرد و سرگیجه هم ممکنه در بعضی افراد دیده بشه.
ملاتونین
دارویی هست که به‌صورت آزاد می‌تونید از داروخانه‌ها تهیه کنید؛ پس تحقیق درباره نحوه مصرف و حتی مشورت با یک متخصص قبل از استفاده از اون، اهمیت زیادی داره. معمولاً پزشک با توجه به شرایط فرد، پاسخ بدن به درمان و علت بی‌خوابی، دوز و مدت مصرف رو تعیین می‌کنه. اما اگر قصد مشورت با پزشک رو ندارید، بهتره از مصرف خودسرانه و طولانی‌مدت، به‌خصوص بیشتر از یک ماه، خودداری کنید.
جدای از همه این‌ها، بسیاری از متخصصان خواب معتقدند ملاتونین نباید اولین راه مقابله با بی‌خوابی باشه. تا زمانی که سبک زندگی، بهداشت خواب و عادت‌های روزمره اصلاح نشن، نباید انتظار داشت هیچ دارویی به‌تنهایی مشکل بی‌خوابی رو برطرف کنه.</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/4627" target="_blank">📅 17:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4626">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ldPx2Fr0hRhh7oGRJMP4x_kC2iqVt5JX5Dr0URFiNXMcU_RR00vXpp-w1lo_vyAtfHNsdAavOjncdKjvNLQ-LFYk0vbUuoKJMGRk6hItNWi7DzQHqnZpLd9s50kbXsY5zndm3HYsQ-YE7IL5zLqPm9Lbutjsw5C5R5xAoN0u9A9Gid426FPo5zzAYLes-GGj1Sotp6yPVLQmDqELFBzsfuESliAHcMTAUl9KhzePD7FxCb3cHnJuvxIKXaCXNtdYHtikO7RWuemir1Gp9B181rSTVj4l4oPDWRpZVGaOEOpB1YEwoj66-KHnR4TvjjRMIt-SZtkCVcA5zosazw9Djg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای فقط داره گند میزنه
الان نفهمیدم واقعا چرا نیازی به 3.6 flash بود
😑</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4626" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4625">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بچه‌های Fireworks AI یه بررسی تخصصی منتشر کردن که نشون می‌ده مدل Kimi K3 نه تنها با Fable در حال رقابته، بلکه ترکیبشون به سطح SoTA (بهترین عملکرد فعلی) تو خیلی از بنچمارک‌ها رسیده و می‌تونه انتخاب خیلی جذابی برای برنامه‌نویس ها باشه.
البته برنامه‌نویس‌های پولدار متاسفانه
😞
https://fireworks.ai/blog/kimik3-fable</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4625" target="_blank">📅 11:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4624">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4624" target="_blank">📅 07:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4623">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4623" target="_blank">📅 07:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4622">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge
https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/4622" target="_blank">📅 07:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4621">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">نسخه‌های اندروید(اگر نمیدونید کدومه برای پردازندتون، Universal رو دانلود کنید)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4621" target="_blank">📅 07:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4616">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4616" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4616" target="_blank">📅 07:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4615">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">آخرین نسخه‌های مک-ویندوز-لینوکس</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4615" target="_blank">📅 07:20 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
