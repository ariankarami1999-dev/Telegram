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
<img src="https://cdn4.telesco.pe/file/MMiBcX7SbWP4nLRHFmLrq9qswXnoneZZhpvw8kfiwCd5jiBhwP2m_lyXnuPZeBBA-aYPtMpdcw4JaiiVLdvCO17bdBRZVLDJ1X1eV2h7EruB7aXrHqHc-RHYGaJLjBx7VQKk12W8jLbSW4A1OchjzjK-t9VB8Bwgxf_onNWexUypb4ZStaZR1OgLA69xlOiYG9m8ds8O6e1-9zo3kRMUhQmJurGlNoScaUNts7p0w6TySmf9Mpi5gGlgE0I4drUvBepwK7cQf9IpNIM26SfD6p7WUxQxRj5PNkJGCxwqV0pEBjWlxCJRElNAumsB0JcdvWI5AqXnUGAMd9I7V_NOKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 21:18:32</div>
<hr>

<div class="tg-post" id="msg-450938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ed02AlMZWAW4C1Ee9wejHROFg7wYZh8vNwA7wPGOBwgKXETwkYHNewxBwhBKUr7sjDGX5hITzxBqTM_DcI9dpV8yQcRMon0eAN9sHZikc64q9-EC6HTIFgUYFeSSGgVBgFibHWVdIfwZ-rTRUIHYRvhqps0Ms8Aze_R2xAy_lvV5O25JMqJRlmPWxON5fjRvXcdQENziECMbfHV_LTHFkdjs2i2zGVzXTQAyYdMDn61D3ZTin-vOe5_yvcSFyN7I1vJRFz7EDDIM2WPgH2JX7t2tI1dKJSkQ--L5-jvw8ZxV8xj9a3iz_Q3bFOqOKEkYqhA1QWAoVoFaYVoGf5C4aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسکاری‌ها برای پرداخت پول کالابرگ شروع شد
🔹
بیش از ۲ هفته است که برخی فروشگاه‌های طرف قرارداد کالابرگ مطالبات خود را از دولت دریافت نکرده‌اند؛ در حالی که طبق قانون، تسویه باید حداکثر ظرف ۷۲ ساعت انجام شود.
🔹
بانک مرکزی می‌گوید از ابتدای سال ۱۴۰۵ دیگر مسئول تأمین منابع کالابرگ نیست و این وظیفه طبق قانون بودجه بر عهده سازمان برنامه و بودجه قرار گرفته است.
🔹
اما سازمان برنامه تأکید می‌کند این نهاد نیز مسئول تأمین منابع نیست و منابع کالابرگ با وصول درآمدهای دولت به‌تدریج تأمین و سپس از سوی وزارت تعاون پرداخت می‌شود.
🔹
در حالی که فروشگاه‌ها از کمبود نقدینگی گلایه دارند، سازمان برنامه می‌گوید درآمدهای دولت به‌صورت تدریجی وصول می‌شود و مطالبات فروشگاه‌ها پس از نقد شدن این منابع پرداخت خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/farsna/450938" target="_blank">📅 21:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450937">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/008837f665.mp4?token=ZjUvo2IlfptC75gkML-FIQE-JGAK6zpXJNmkvid-UEqDCWoeYYDHfUMWcm9KQMmh9K50XQblT9H89cLkUQsrX-C54asIHmFymeKEAVMUtADBm4cfnpi23XUNu0XgwtB2xNukEMl8f6EoHQfNKE9wnCZX0LvB5px-ppcIqtTqkAv0YRnKxZWiHehN5puygTdqOjGBxIBtEcQBWVVULAWXMvSFrhMPX5B7HhHbMky6gpu-f1xvrIp-vwnI3aFbiE57OcOxEgms83GR6hcSsFqwiGunpA7SJc9K9S2LXwfh5kNjW38Dh52HSxO7qm027GFe_0xjPL6294iPKKQGZ8iB6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/008837f665.mp4?token=ZjUvo2IlfptC75gkML-FIQE-JGAK6zpXJNmkvid-UEqDCWoeYYDHfUMWcm9KQMmh9K50XQblT9H89cLkUQsrX-C54asIHmFymeKEAVMUtADBm4cfnpi23XUNu0XgwtB2xNukEMl8f6EoHQfNKE9wnCZX0LvB5px-ppcIqtTqkAv0YRnKxZWiHehN5puygTdqOjGBxIBtEcQBWVVULAWXMvSFrhMPX5B7HhHbMky6gpu-f1xvrIp-vwnI3aFbiE57OcOxEgms83GR6hcSsFqwiGunpA7SJc9K9S2LXwfh5kNjW38Dh52HSxO7qm027GFe_0xjPL6294iPKKQGZ8iB6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس ستاد اربعین: هیچ مشکلی برای تردد زائرین در مرز خسروی وجود ندارد
@Farsna</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/farsna/450937" target="_blank">📅 21:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad26fa7899.mp4?token=auedItVgw8q2kK19s6j945b4FdFm8xqJlpfrEfXlrjxdhJyrZXkHKDwZXY8MowmGXABpmWqRoMVH6PC_6l43t0n0yZH9TLWblQ4U_3QyHKUChcpfpI6Qv3byir_gyG7UKgcEwq3zDpkBF0ArzrxSHfRlFtRxFsQS6KyrAxkKoh4yoxKhL9MhD_apLPnq-Gk0D5y2MuvAjsjLqz9xJr9eQZzncQf3GXdT0wzDAhI75dErnCqP2AXNF0gUT2AYeLuWMxIH9BOWwoZmM1tbK3XrGIMEWNLnCZCaZsxpX2LK5bboRDg9B5NUUeATYiWOydPAC2CDlgny6e9d0wwIcGIKNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad26fa7899.mp4?token=auedItVgw8q2kK19s6j945b4FdFm8xqJlpfrEfXlrjxdhJyrZXkHKDwZXY8MowmGXABpmWqRoMVH6PC_6l43t0n0yZH9TLWblQ4U_3QyHKUChcpfpI6Qv3byir_gyG7UKgcEwq3zDpkBF0ArzrxSHfRlFtRxFsQS6KyrAxkKoh4yoxKhL9MhD_apLPnq-Gk0D5y2MuvAjsjLqz9xJr9eQZzncQf3GXdT0wzDAhI75dErnCqP2AXNF0gUT2AYeLuWMxIH9BOWwoZmM1tbK3XrGIMEWNLnCZCaZsxpX2LK5bboRDg9B5NUUeATYiWOydPAC2CDlgny6e9d0wwIcGIKNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازگشایی مسیرهای آسیب‌دیده در مناطق جنوبی کشور با همت نیروهای جهادی
@Farsna</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/farsna/450936" target="_blank">📅 21:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۹۷.pdf</div>
  <div class="tg-doc-extra">3 MB</div>
</div>
<a href="https://t.me/farsna/450935" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
دستِ پُر به میدان بروید
🔸
اگر برای اجتماعات انقلابی به‌دنبال شعر، شعار یا تک‌بیت‌های روز هستید، ویژه‌نامهٔ «خط» پاسخگوی نیاز شماست.
@Farsna</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/farsna/450935" target="_blank">📅 21:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450934">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/446f1163d1.mp4?token=aG879b0mL8TE2uwe6KHDSKZc-9ZM4VDTp7mVLRRuprhVZknVmgHC8PSADIZRzx3nRoJz2RWatwn7j0b3E4llLXkKHNZEM_Muv4c1cVZFSJ3GRucksHmtRnwL9xX1LnBLLNQQ-a3fZUznNoYbQj9q_S26eGo4UIfXyZCpHA3ExLSyFwemFJqyIZzVjGgQEUUJvpubY5eEwWDoZSPuBctOQ10vV0lg0oij2nHbWPSLpru-nt8e8GhBL0Q3NAHx-3TkVD64xixRR1uerg6A4OAYhUERRXNrYn8_UJdShSXnt_wz8bwypmbFxv2LFCerWrnpa0lJ1pZRFVvifSOzNkVuBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/446f1163d1.mp4?token=aG879b0mL8TE2uwe6KHDSKZc-9ZM4VDTp7mVLRRuprhVZknVmgHC8PSADIZRzx3nRoJz2RWatwn7j0b3E4llLXkKHNZEM_Muv4c1cVZFSJ3GRucksHmtRnwL9xX1LnBLLNQQ-a3fZUznNoYbQj9q_S26eGo4UIfXyZCpHA3ExLSyFwemFJqyIZzVjGgQEUUJvpubY5eEwWDoZSPuBctOQ10vV0lg0oij2nHbWPSLpru-nt8e8GhBL0Q3NAHx-3TkVD64xixRR1uerg6A4OAYhUERRXNrYn8_UJdShSXnt_wz8bwypmbFxv2LFCerWrnpa0lJ1pZRFVvifSOzNkVuBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁨ ⁨
💫
ارز اربعین؛ خدمتی از بانک شهر برای سفری آسوده‌تر
📱
سفر اربعین، سفری از جنس عشق و دلدادگی است. بانک شهر با همکاری اپلیکیشن آپ، امکان ثبت آنلاین درخواست ارز اربعین را فراهم کرده تا زائران بدون مراجعه حضوری برای ثبت درخواست، تنها با چند گام ساده، شعبه منتخب بانک شهر و زمان دریافت ارز را انتخاب کنند و با خیالی آسوده راهی کربلا شوند.
✔️
ثبت درخواست برای خود و افراد تحت تکفل در اپلیکیشن آپ
✔️
دریافت ارز از شعب منتخب بانک شهر
✔️
تا سقف ۲۰۰ هزار دینار
⏳
لطفاً پیش از ثبت درخواست، ثبت‌نام خود را در سامانه سماح نهایی کنید.
بانک شهر؛ در کنار زائران، در هر قدم از این مسیر معنوی.
#آپ
#اربعین
#سفر
#بانک_شهر
⁩⁩</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/farsna/450934" target="_blank">📅 21:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450933">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه معلم | MIC Insurance</strong></div>
<div class="tg-text">🔸
«کام»، خریدی هوشمندانه؛ آینده‌ای مطمئن
🔹
با طرح ملی «کام»، خریدهای روزمره شما فقط یک پرداخت ساده نیست؛ بلکه فرصتی است برای ساختن آینده‌ای بهتر.
🔹
در این طرح، بدون آن‌که مبلغ بیشتری پرداخت کنید، با خرید از پذیرندگان منتخب، بخشی از مبلغ‌ خریدهای شما به‌صورت خودکار به اندوخته‌ای ارزشمند تبدیل می‌شود.
🔹
مزیت مهم طرح «کام» این است که این اندوخته در قالب بیمه‌نامه سرمایه‌گذاری رایگان نزد بیمه معلم برای شما تشکیل می‌شود؛ یعنی بدون پرداخت هزینه اضافی، هم از خرید خود لذت می‌برید و هم برای آینده‌تان سرمایه‌گذاری می‌کنید.
🔹
گام‌های پیوستن به طرح «کام»:
▫️
ثبت درخواست در وب‌سایت بیمه معلم
▫️
ثبت کارت‌های بانکی از طریق اپلیکیشن سکه به‌پرداخت ملت
▫️
خرید از پذیرندگان منتخب و شروع خودکار فرایند اندوخته‌سازی.
#بیمه_معلم_همراه_هم_وطن
سایت
|
بله
|
اینستاگرام
|
تلگرام</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/farsna/450933" target="_blank">📅 21:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/farsna/450932" target="_blank">📅 21:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450931">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">استانداری هرمزگان: شنبه تمام اداره‌ها، سازمان‌ها و بانک‌های استان با حضور ۵۰ درصدی کارکنان، فعال خواهند بود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/450931" target="_blank">📅 21:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450930">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26d005a4bd.mp4?token=tPaIH5CFYD9bwv7eJTMqaWjmsmrQLSg3TYuyxRs-tuO7plcoANk_I4juaWpbo72SdhZSsPlWYnnCd5WUJTwstVHWtWhuJTtm41fy_jNaDQaOs6zhGtc0NXAivXPnuXpgi3DpY4EJsIUErZj5DoTTrM2RxstNH6o_yDWUwxDKt3rIDlnfTBBFD-0eNdLGKAJ0ckU1fTabNF9Ngl5EIbgwqlED3E7g22eoM-2doftZFVEHYd4Zxm7-GZjLjfXpx_GAe-Lje6bCPlVE47foCoBYdU4cywt0RXR5k7SxnppOvpWgDKPoHdXvTh3PE2xM7SWpBahTwindRAOazEEzw2LO6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26d005a4bd.mp4?token=tPaIH5CFYD9bwv7eJTMqaWjmsmrQLSg3TYuyxRs-tuO7plcoANk_I4juaWpbo72SdhZSsPlWYnnCd5WUJTwstVHWtWhuJTtm41fy_jNaDQaOs6zhGtc0NXAivXPnuXpgi3DpY4EJsIUErZj5DoTTrM2RxstNH6o_yDWUwxDKt3rIDlnfTBBFD-0eNdLGKAJ0ckU1fTabNF9Ngl5EIbgwqlED3E7g22eoM-2doftZFVEHYd4Zxm7-GZjLjfXpx_GAe-Lje6bCPlVE47foCoBYdU4cywt0RXR5k7SxnppOvpWgDKPoHdXvTh3PE2xM7SWpBahTwindRAOazEEzw2LO6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قدرت‌نمایی موشک‌های ایرانی با اصابت به اهدافی در اردن
@Farsna</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/450930" target="_blank">📅 20:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450929">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
🔴
اعتراف سازمان تروریستی سنتکام: ۲ نظامی آمریکایی در حملات ایران به اردن کشته و ۴ نظامی مجروح شدند. @Farsna</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/450929" target="_blank">📅 20:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450928">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌ اعتراف آمریکا به زخمی‌شدن ۱۳ نظامی در حملات ایران
🔹
فاکس‌نیوز به‌نقل از مقامات آمریکایی گزارش داد که از آغاز حملات ایران به پایگاه‌های آمریکا در کویت، بحرین و اردن، تاکنون دست‌کم ۱۳ نظامی آمریکایی مجروح شده‌اند.
🔹
با وجود گذشت چند روز از این حملات، مقام‌های…</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/450928" target="_blank">📅 20:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450927">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">حادثه امنیتی در نزدیکی سواحل عمان
🔹
سازمان عملیات دریایی بریتانیا اعلام کرد که گزارشی از حادثه‌ای بین یک کشتی تجاری و نیروهای نظامی در فاصله تقریباً ۱۰۰ مایلی در شرق شهر دقم در سلطنت عمان دریافت کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/450927" target="_blank">📅 20:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450926">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6849fcb1a4.mp4?token=olAHsh3V4Lhl9TIAEyc3M0bIx2k5Wq7B8QxqVWEBQQFQWdt0CsvVp3pMwU9OmY4GY2FBMfsMAuBkD7wUZ9uvZ9K8nCS25E58-2gbgVVvl46PuOMsOSeD_QzRgUKtoFc1Kri9l3LqlLAUP4Y9NpV35vKT_axgl3MhymBBaEta1yZFiOtNAFlYs_dyBantc7qsPsC-yml-qOy1BAF7VNJwUHHtDRBKlvkPaKsMKd9o9yJjjUmCFmznZyQ7_K6eFLaa0haJNQpA61B2FcYxILO425eE3HpOfnwvw7__Q94syB9-mPbTEiX3s-p9Red6qXQIwrW6I3aJCfV6sdw_zjeesQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6849fcb1a4.mp4?token=olAHsh3V4Lhl9TIAEyc3M0bIx2k5Wq7B8QxqVWEBQQFQWdt0CsvVp3pMwU9OmY4GY2FBMfsMAuBkD7wUZ9uvZ9K8nCS25E58-2gbgVVvl46PuOMsOSeD_QzRgUKtoFc1Kri9l3LqlLAUP4Y9NpV35vKT_axgl3MhymBBaEta1yZFiOtNAFlYs_dyBantc7qsPsC-yml-qOy1BAF7VNJwUHHtDRBKlvkPaKsMKd9o9yJjjUmCFmznZyQ7_K6eFLaa0haJNQpA61B2FcYxILO425eE3HpOfnwvw7__Q94syB9-mPbTEiX3s-p9Red6qXQIwrW6I3aJCfV6sdw_zjeesQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از پارک ممنوع تا پارک ایمن؛ آنچه زائران اربعین باید بدانند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/450926" target="_blank">📅 20:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450925">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">متن کامل پیام رهبر انقلاب.pdf</div>
  <div class="tg-doc-extra">144.6 KB</div>
</div>
<a href="https://t.me/farsna/450925" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‌
🔴
رهبر معظم انقلاب: نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد
🔹
هم‌زمان با این حماسه [بدرقه‌ٔ آقای شهید ایران]، نقض عهد‌های مکرّر شیطان بزرگ نسبت به تفاهم‌نامه امضا شده بین رئیس‌جمهوران ایران و امریکا بار دیگر این…</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/450925" target="_blank">📅 20:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450924">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
پیام رهبر معظم انقلاب دربارۀ حماسۀ عظیم بدرقه آقای شهید ایران و تبیین مسائل مهم کشور تا دقایقی دیگر منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/450924" target="_blank">📅 20:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450923">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‌
🔴
رهبر معظم انقلاب: بدرقۀ آقای شهید ایران حماسه‌ای تاریخی و رستاخیزی بی‌سابقه بود
🔹
ملّت عظیم‌الشّأن و شگفتی‌ساز ایران! سلام و درود و سپاس بر شما که با حماسه‌ی بی‌نظیر و تاریخی خود در رستاخیز بی‌سابقهِ‌ی بدرقه‌ی آقای شهید ایران، نِصاب تازه‌ای از جلوه‌ی بعثت…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/450923" target="_blank">📅 20:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450922">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌ رهبر معظم انقلاب: انتقاد به عملکرد مسئولان نباید موجب ظلم به بیگناهان و شکست وحدت و انسجام اجتماعی شود
🔹
ملّت عزیز، با تداوم بر اعتماد به مسئولان دلسوز در هر سه قوّه که تلاش ایشان برای رفاه و سعادت ملّت، مشهود می‌باشد، همچنان برای تضمین صیانت از منافع ایران…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/450922" target="_blank">📅 20:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450921">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AF6rmG4Ir_jNOn2MhxQp5gpy9b4Span9ximhHM2nyadsb3PF7ADZ1w12GRtBw83QvpIkfeRE5B9lenv7Y8EjFpk9GN4kBCVecoubkGcqQyas5Q9qSrSRjEv-RXHGnbe56gajWkHLOlu9ILzD904tEz7a0uPORsqVFfkKOUaG9er51MbWrb-VoCoUI5gh57DUi0S-pV4R787yDXN7iXl77YwwlnRvqsImB4-uq76Po8ZAhA1-0nnBgSuH6Z0gkjl1kuxiQIZLh1myqIAgOJmCQf8hpNoshxCxQnj1HS-TBbTCLhZG_6HM3OhELHqm-eU9BZebs_TtKkc2yka2xAItEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر معظم انقلاب: از اصولی‌ترین امور، اصرار بر اتحاد مقدّس در همه‌ی سطوح است؛ پرهیز از تفرقه و تنازع وظیفۀ همگانی است
🔹
لازم است به شما مردم باوفا و سرافراز ایران عرض شود که از جمله اصولی‌ترین امور در این برهه، اصرار بر وحدت کلمه و اتحاد مقدّس در همه‌ی…</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/450921" target="_blank">📅 20:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450920">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‌
🔴
رهبر معظم انقلاب: نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد
🔹
هم‌زمان با این حماسه [بدرقه‌ٔ آقای شهید ایران]، نقض عهد‌های مکرّر شیطان بزرگ نسبت به تفاهم‌نامه امضا شده بین رئیس‌جمهوران ایران و امریکا بار دیگر این…</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/450920" target="_blank">📅 20:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450919">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aK_XVl0_KUUqAuGyyiFgiOgcTNG2w3cQ0E7eYY9mKB81qYGcQyG5LtybT9KNTdNHVPBlGfPnMOOT7SdbRZo9zCScDZByuwrqHrfzwi2gkRHBxGBCMDePBe6NGY26IeuOrlLWjS1J4T4I6u1or5aRM-rGyHP8VSovWblO0PvX47epx2IpWGCmGd6QEmSAaGdfoiQ8pqiFFDwLdjYJDIyRDW43MTFW6YsQesJbROspUmTck2D6vLmYteIkd7L3STiAaYBZ-rZXCznwXqh8ZJu3z7yH7cs02KDEiXHTwnnOr4i4OxYTYKUzXimlrvI-iF2ZQ5lELXKfGl8D1IV980sc3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیام رهبر معظم انقلاب دربارۀ حماسۀ عظیم بدرقه آقای شهید ایران و تبیین مسائل مهم کشور تا دقایقی دیگر منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/450919" target="_blank">📅 20:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450918">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ادارات خوزستان دوشنبه دورکار شدند
🔹
استانداری خوزستان: با توجه به پیش‌بینی تداوم گرمای شدید، ساعت کاری ادارات استان در روز یکشنبه تا ساعت ۱۱ خواهد بود و فعالیت ادارات در روز دوشنبه به‌صورت دورکاری انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/450918" target="_blank">📅 19:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450917">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114af211a3.mp4?token=txpBXlb9a4zdZ9X3g0ngiy-3pJb4yCBTYKacYF7iTVVbltbPrRn5gkuMevZkCqi2aKM0VBTeH8ArQfaCZ0Heyl4yr8ushWQThQP-idNYhpD7kevy3076olr4UsGqulAiD89K2Yn5RYV0GWoSl3hwTcmEI952M--diUeaTAvWrwULzBdQHodtBbiDfRcGXERuD9HrKTL9EumAFnUjgL0_JBWHWfnykwfWF1zRwhNZFvt_h1rIQYLtpxn_wiT4BINy4mcmgBK9aYn42R2TJbVCYp6ZyMdIsAFpiWmaiYwUwx_sgNV_zlhyqrrc7MsbXaJ2me9bd-_f7qCit17E81VPlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114af211a3.mp4?token=txpBXlb9a4zdZ9X3g0ngiy-3pJb4yCBTYKacYF7iTVVbltbPrRn5gkuMevZkCqi2aKM0VBTeH8ArQfaCZ0Heyl4yr8ushWQThQP-idNYhpD7kevy3076olr4UsGqulAiD89K2Yn5RYV0GWoSl3hwTcmEI952M--diUeaTAvWrwULzBdQHodtBbiDfRcGXERuD9HrKTL9EumAFnUjgL0_JBWHWfnykwfWF1zRwhNZFvt_h1rIQYLtpxn_wiT4BINy4mcmgBK9aYn42R2TJbVCYp6ZyMdIsAFpiWmaiYwUwx_sgNV_zlhyqrrc7MsbXaJ2me9bd-_f7qCit17E81VPlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایتخت سوئد امروز شاهد راهپیمایی در حمایت از غزه و اعتراض به جنایات نتانیاهو بود
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/450917" target="_blank">📅 19:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450916">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
پیام رهبر معظم انقلاب دربارۀ حماسۀ عظیم بدرقه آقای شهید ایران و تبیین مسائل مهم کشور تا دقایقی دیگر منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/450916" target="_blank">📅 19:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450915">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635337e268.mp4?token=lTIevtUv4LKdIg9iD4ZCJBbZsQ5PY5b0PBbiWhw0sEDZee4kDPege_neutaBqhLGQ0ivMjsXEkRQQ-LsKFfL_mWyCH77qSC4syEOTIETZQEG6rLOv8oSC48leAaIr5-pek3CFj6lKtbQfH4y3j23zlDvn87FMO3E_TInRs8wBtU4BPii6mucoikcbU6WzzywuQY-0MWYsYcnXSTpeiHUyWPv9U4cNZZBxwFW1Gb7SZJzz7Ft-58w8Ay4EZdUPaRITq7fPx8Oo3m2A-CCxrVPuyXaqyth8BkDaAyZ0dm99m1YGHaSKeGiS2iiIlmjEPMntqYXE_AsFLhO8kZGBl3Sjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635337e268.mp4?token=lTIevtUv4LKdIg9iD4ZCJBbZsQ5PY5b0PBbiWhw0sEDZee4kDPege_neutaBqhLGQ0ivMjsXEkRQQ-LsKFfL_mWyCH77qSC4syEOTIETZQEG6rLOv8oSC48leAaIr5-pek3CFj6lKtbQfH4y3j23zlDvn87FMO3E_TInRs8wBtU4BPii6mucoikcbU6WzzywuQY-0MWYsYcnXSTpeiHUyWPv9U4cNZZBxwFW1Gb7SZJzz7Ft-58w8Ay4EZdUPaRITq7fPx8Oo3m2A-CCxrVPuyXaqyth8BkDaAyZ0dm99m1YGHaSKeGiS2iiIlmjEPMntqYXE_AsFLhO8kZGBl3Sjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت پردۀ کاسبان جنگ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/450915" target="_blank">📅 19:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450914">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‌  بقایی: براساس یادداشت تفاهم، هیچ نکته‌ای وجود ندارد که به آمریکا اجازه دهد مسیر موازی مستقلی در تنگه هرمز ایجاد کند
🔹
آنچه آنها انجام دادند، نقض تعهداتشان بود. آنها کشتی‌ها را مجبور کردند از مسیر دیگری عبور کنند و عملاً مسیر هماهنگ‌ شده با ایران ــ که مسیر…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/450914" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450913">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بقائی: تک‌تک بخش‌های یادداشت تفاهم از سوی آمریکا نقض شده است
🔹
سخنگوی وزارت خارجه: تک‌تک بخش‌های یادداشت تفاهم اسلام‌آباد طی یک هفته یا ۱۰ روز گذشته از سوی آمریکا نقض شده است.
🔹
ایرانیان هرگز خواهان جنگ با هیچ کشوری، چه در منطقه و چه خارج از آن، نبوده‌اند؛…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/450913" target="_blank">📅 19:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450912">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiDDuc12pIqq5Y1vjc_qAmlGoSg2_BpMl5sHht6pHV8lxvBMEo_-ubV18LApAcG0bEA8Bf6QNNQeMweNAcZW8Fh9tSO7o9THYhgrL2R7Xy8c6MmnHMScgmhhMkqmBjizv9fx2nLvuf0jp-BjQIEuURcJSFN6wlPamR7puyoF2YbXFSxJbmUpC4tSomqZXoTyHtyshJ95W3tl4slts0x-ZS8e_FUxGIou2Qvi5GadAINofsobp4qQekGtrn9zWK4CQO_lLXT90z1k938f8NJ3464xLHa7lAfo4ZwpbBMFXBf8Nx9xoYnDPFgEjeLLJc0eHbcto5vvUgctUBcs8YqKDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: تک‌تک بخش‌های یادداشت تفاهم از سوی آمریکا نقض شده است
🔹
سخنگوی وزارت خارجه: تک‌تک بخش‌های یادداشت تفاهم اسلام‌آباد طی یک هفته یا ۱۰ روز گذشته از سوی آمریکا نقض شده است.
🔹
ایرانیان هرگز خواهان جنگ با هیچ کشوری، چه در منطقه و چه خارج از آن، نبوده‌اند؛ ما صرفاً از خود دفاع کرده‌ایم و این جنگ بر مردم ایران تحمیل شده است.
🔹
تعهد آنها این بود که در طول دوره اجرای این یادداشت تفاهم، ایران به تمام دارایی‌های مسدودشده خود دسترسی آزاد داشته باشد. قرار نبود آنها پولی به ایران پرداخت کنند. این پول، دارایی خود ایران است که سال‌ها به‌صورت غیرقانونی مسدود شده است.
🔹
هیچ هدفی را جز پایگاه‌های نظامی و تجهیزات نظامی آمریکا مورد حمله قرار نداد‌ه‌ایم، ایران و جمهوری اسلامی از یکدیگر جدا نیستند و ملت ایران هیچ دشمنی با مردم آمریکا ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/450912" target="_blank">📅 19:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450911">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HajlgaHtbWiCsLbv-thT8MgzoHPUYRtf0i4T0Zl3YsaHYg4B9F8Qt0yQXwB1O_hUtgtmGixsbYLnhvdK_acKXZZbkqoz6qZFJQPF9kw-laMtyQJ4CG9gJoD-txkwGoW-hsYdsRNsIgdljhQCa1GUGwVHtkYuQUHAaxfPCfU5CSd7yOK1SbRd-TQQmTIvKQB26G5tuZuu61IiO9rm0utalv5WsyuGPKyHAIsoeXEc9N9oKAKRvbw84GU4vh7rAlUaYJOEvSMga15HTJt3qOvtFI9ifI6-yDa26Xu5d5sBvVw0hXnjHLWo63FqVYVY50UID9t73m65z5TojA7sI0m-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چت‌جی‌پی‌تی تخلفات نوجوانان را به والدین گزارش می‌دهد
🔹
انگجت: اپن‌ای‌آی از گسترش قابلیت‌های نظارت والدین در چت‌جی‌پی‌تی خبر داد. بر اساس این تغییر، در صورت غیرفعال شدن حساب یک کاربر نوجوان به‌دلیل نقض سیاست‌های مربوط به تهدیدها یا اقدامات خشونت‌آمیز، والدین متصل به حساب فرزندشان یک اعلان دریافت خواهند کرد.
🔹
اعلان جدید فقط از غیرفعال شدن حساب به‌دلیل نقض قوانین خبر می‌دهد و دسترسی والدین به محتوای گفت‌وگوهای نوجوان را فراهم نمی‌کند. این قابلیت برای کمک به مداخله زودهنگام خانواده‌ها در صورت بروز نشانه‌های نگران‌کننده توسعه یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/450911" target="_blank">📅 18:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450910">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
حملات متعدد موشکی دشمن آمریکایی به حوالی سیریک
🔹
استانداری هرمزگان اعلام کرد: در ساعت ۱۲:۳۰ و ۱۶:۳۰ و ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله نظامی دشمن آمریکایی قرار گرفت.
🔹
در حملات جدید آمریکا به سیریک هیچ مصدوم غیرنظامی گزارش نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/450910" target="_blank">📅 18:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450909">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8a32ee92.mp4?token=nPy_aMEkID7ctkpJ-TieX4OE_rMP-xwMW43kk1RMD850xbZxJLN0jzTuap3dvImMWkb2eV_eMdQW2WYFDzqz0BucpQJaLJLkRb1Xp2GXp9USjExyXYO-f9rpUvjDwQ-Z2cbPjAR1_-TBsM2Wkb-BYFk4V_nBj54m9W6fBAnI0Yf9yQoN-gFm-hXkCxYzs1UkJCjaHcFOb7wAS0znsg6Xz0ONJnhKRTGgDjZ2cb-4qAAyrElOgGwzjgx7txuwpsXXcikQIcIFswpHL7OTMoIYu1G_jYtVPGghUAz9Pp2Y1fxXZgieKTGRP1c1fqYih0QzirMJhE4Qe-ejK5eq0Aw4-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8a32ee92.mp4?token=nPy_aMEkID7ctkpJ-TieX4OE_rMP-xwMW43kk1RMD850xbZxJLN0jzTuap3dvImMWkb2eV_eMdQW2WYFDzqz0BucpQJaLJLkRb1Xp2GXp9USjExyXYO-f9rpUvjDwQ-Z2cbPjAR1_-TBsM2Wkb-BYFk4V_nBj54m9W6fBAnI0Yf9yQoN-gFm-hXkCxYzs1UkJCjaHcFOb7wAS0znsg6Xz0ONJnhKRTGgDjZ2cb-4qAAyrElOgGwzjgx7txuwpsXXcikQIcIFswpHL7OTMoIYu1G_jYtVPGghUAz9Pp2Y1fxXZgieKTGRP1c1fqYih0QzirMJhE4Qe-ejK5eq0Aw4-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احساساتی‌شدن داوران برنامۀ محفل ستاره‌ها با تلاوت فوق‌العادۀ خلبان کوچولو
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/450909" target="_blank">📅 18:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450908">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d76f189634.mp4?token=ZeFsdsdS6WWrJfZm5N_Gky5-7h7crt_kNEJ5yYKsM9HzmlZfrmmUeEGEwhFLzP58kvO9zok5FmMO6Bv3W5eEoQwoQD3in03ISwwRoF6yzUsI1xcvnPGJzsztgYR2VuyB1jNgkSX9e46UKeu8w4gOlX3DMts09SM_IB8s-eupkgvFOR4aK_sLPPRZ97fwCg6VxH0wM88k04xHOR5vUWnXeqyLyTOQxnh2q5rpzVW2mp4xho-I48uX2YUcfeBT68TBviwtoJ_OlX8zolknI2Afuv6s-zKa5-tOn1umRJrVso30B6BumudOHGIhg6E09TlV7B0gPZm7zOpFw764CowRBJM-PZHudfmbXkgDyxSfQkjE3uEZ9GIqksA77RAk3kiV2LTKmRl_QC94a2R-yinWIFKwRL7qHG3g4xq4HJfXQpsxa7RqfkoyQJUMCIidJPfr2c1kycenPpytOZno4qIabBzQhP1dKDUL1baITxnVqOzo-Ttb6fZPxZqLnw1TOkOSyf5Cd1jls8ntxpYb_lXpb8B2v93BMldls3oAZuceGjZLYfzXshXs9YtgPR4fdhctN1_oezIj7-gO-LA4tblLNC06oqxH2QsDWE07b6lqKr1uBVorNd6bJmOoJTpa4qKJCnIVgs-bo_jDIYQdGb9gQJ9da36beovlsShRTA0kxFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d76f189634.mp4?token=ZeFsdsdS6WWrJfZm5N_Gky5-7h7crt_kNEJ5yYKsM9HzmlZfrmmUeEGEwhFLzP58kvO9zok5FmMO6Bv3W5eEoQwoQD3in03ISwwRoF6yzUsI1xcvnPGJzsztgYR2VuyB1jNgkSX9e46UKeu8w4gOlX3DMts09SM_IB8s-eupkgvFOR4aK_sLPPRZ97fwCg6VxH0wM88k04xHOR5vUWnXeqyLyTOQxnh2q5rpzVW2mp4xho-I48uX2YUcfeBT68TBviwtoJ_OlX8zolknI2Afuv6s-zKa5-tOn1umRJrVso30B6BumudOHGIhg6E09TlV7B0gPZm7zOpFw764CowRBJM-PZHudfmbXkgDyxSfQkjE3uEZ9GIqksA77RAk3kiV2LTKmRl_QC94a2R-yinWIFKwRL7qHG3g4xq4HJfXQpsxa7RqfkoyQJUMCIidJPfr2c1kycenPpytOZno4qIabBzQhP1dKDUL1baITxnVqOzo-Ttb6fZPxZqLnw1TOkOSyf5Cd1jls8ntxpYb_lXpb8B2v93BMldls3oAZuceGjZLYfzXshXs9YtgPR4fdhctN1_oezIj7-gO-LA4tblLNC06oqxH2QsDWE07b6lqKr1uBVorNd6bJmOoJTpa4qKJCnIVgs-bo_jDIYQdGb9gQJ9da36beovlsShRTA0kxFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انتقام رهبر شهید، مطالبه‌ای که خاموش نمی‌شود
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/450908" target="_blank">📅 18:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450907">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bc6b40448.mp4?token=rh5ntSt41DtlwZHTm7DvBCiZgDPFWxM6eCWSUihnQLI1s15SDbm1C3tD1Q6KPOaIFagbgRcZ9IPob1qlefIfd7lW0EgMkLhByWvPxyh1V0fFgvA6FvMhILSOeTZU5WCHFm6dfh_m_CuRO_D1AM4p_HcCSXTSVz_p6c6yWa0wekhpMt4tbm2xW5dCJlkkjt0yIB_ziPDvSkh4erclAHVKI6v5nCZia9faLH26oozByoXPXvCcuCUQfXskYnmpjAf2vcJNIYURvPcjTOsc9VYCwS-7r8LxT7j1yfqrCvI4bX60u1luG1nZiJgnA3S5Ja1QwlJHG6oBcUJjHmAqBVcFkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bc6b40448.mp4?token=rh5ntSt41DtlwZHTm7DvBCiZgDPFWxM6eCWSUihnQLI1s15SDbm1C3tD1Q6KPOaIFagbgRcZ9IPob1qlefIfd7lW0EgMkLhByWvPxyh1V0fFgvA6FvMhILSOeTZU5WCHFm6dfh_m_CuRO_D1AM4p_HcCSXTSVz_p6c6yWa0wekhpMt4tbm2xW5dCJlkkjt0yIB_ziPDvSkh4erclAHVKI6v5nCZia9faLH26oozByoXPXvCcuCUQfXskYnmpjAf2vcJNIYURvPcjTOsc9VYCwS-7r8LxT7j1yfqrCvI4bX60u1luG1nZiJgnA3S5Ja1QwlJHG6oBcUJjHmAqBVcFkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چه روشی جلوی ترامپ جواب می‌دهد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/450907" target="_blank">📅 18:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450906">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/360c979e00.mp4?token=b2OMU17quBWfH7jIUdgAatjpjQlQ24bh0pCXzUTVet1PJrZk4Cuh7XxsoyU4n6gKLSvxlev01ZZPGT_SeMdAZON9t_pBhod6xeyS1bd_qN4HGpy9YjyYd9-MD9iu4V3iLNNMj8_y1gm-bDhmdcsTpXC2GqVCOaCLvTSbVdYJnruFK6y_ZXv-CrZ8mQPEufYnM-wmsPAecT0lXyFSWhUypRyubPuBP1uAA9nDO6NqveoZAdvM4oICF-r319ITdbrQPpbLrZTDiW5oCKoOxv_USNlhnXrWTTFe9frb-_vqStdH-PUCFsGzpI9BmDCGLr_oA-9pN9hgsigrkUr5s9P58Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/360c979e00.mp4?token=b2OMU17quBWfH7jIUdgAatjpjQlQ24bh0pCXzUTVet1PJrZk4Cuh7XxsoyU4n6gKLSvxlev01ZZPGT_SeMdAZON9t_pBhod6xeyS1bd_qN4HGpy9YjyYd9-MD9iu4V3iLNNMj8_y1gm-bDhmdcsTpXC2GqVCOaCLvTSbVdYJnruFK6y_ZXv-CrZ8mQPEufYnM-wmsPAecT0lXyFSWhUypRyubPuBP1uAA9nDO6NqveoZAdvM4oICF-r319ITdbrQPpbLrZTDiW5oCKoOxv_USNlhnXrWTTFe9frb-_vqStdH-PUCFsGzpI9BmDCGLr_oA-9pN9hgsigrkUr5s9P58Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش ۲.۵ متری برف در شیلی
🔹
در ۲۴ ساعت گذشته، ۲۵۰ سانتی‌متر برف در بخش‌هایی از شیلی بارید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/450906" target="_blank">📅 18:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450905">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6ee473e85.mp4?token=bsOQOoMA5io-8sKzWXyNgXqeIdGhtNwTZ-kJr33sxVRQINxVVT_QKolaBWblWvkfd5FZcmhmAwuLMAZINj6_fqMjCAtAHAMlDH9cNIwogcHIMJeqK9tPNXUh3kxxamO6lE_QC3WA7dG7zyaaBkLyceTSAwZYWLKUaDUUa_Z9sc0FQHi47iuKQEndJs76XMhFvp6rSSHyIqEWXchDQPJuCzzzTQF4jvZ5Pqej_EsQhfK5LVO8jSxiarpjJbhF-Ya8IAJmeYovOVffG2iHEN0ygA_d3r0WhLojUIiDBdsiI_9A5j35pVw5U71ytrHIVyofGEYq2tiYoT7E1VDO0WEYVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6ee473e85.mp4?token=bsOQOoMA5io-8sKzWXyNgXqeIdGhtNwTZ-kJr33sxVRQINxVVT_QKolaBWblWvkfd5FZcmhmAwuLMAZINj6_fqMjCAtAHAMlDH9cNIwogcHIMJeqK9tPNXUh3kxxamO6lE_QC3WA7dG7zyaaBkLyceTSAwZYWLKUaDUUa_Z9sc0FQHi47iuKQEndJs76XMhFvp6rSSHyIqEWXchDQPJuCzzzTQF4jvZ5Pqej_EsQhfK5LVO8jSxiarpjJbhF-Ya8IAJmeYovOVffG2iHEN0ygA_d3r0WhLojUIiDBdsiI_9A5j35pVw5U71ytrHIVyofGEYq2tiYoT7E1VDO0WEYVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، کارشناس حوزۀ مقاومت: پایگاه‌های آمریکا در اردن پاسبان اصلی رژیم صهیونیستی هستند
🔹
تمرکز ما بر اردن باید به اندازۀ سرزمین‌‌های اشغالی باشد. @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/450905" target="_blank">📅 18:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450900">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t7FtsllaODEdVFrH4B6OkF0cjC34S6FR-O_zoKACie0pwQRDDKlHfst7NJBglLYqsJb13ZtckON_nA26cMDb6EtBJO5aern6Cp2kO2lvAZ3JCBDDih32w0Nsfa0W2hyxBmSg_Hzma7hjqfKk6G9_cQzB3hgENS1_3fy4P3J-bR1he37yHaTlb7yRPIDbOcyL4pg2tDRW0mdKskrKMJDP6XN6vn0H4bvlCO3NAxYcddOAizxL_rfwYsiS2YZodL5z1RFHBZkV5G_AJM2DuM6iM7MHdUbrFZpE5fVN6xnbIsXke6BV7HOy-clEVsucp6QwQtRshffxXkhfoheXlkL0pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k8Ive0Ovq7u31tfockwvqiyRonxpWIb53he3b_SrllMilodr30l6ojeMqKYoz87Ixmf7KJL93jFFQ1U_qMw1MFZQ2PIhnKDBu14w_GdwfyYNWhXAVoa47FkW91ToCBkcEKKF8ChwF4yaxxEBsqj4kpfux5s9VedcWeIDUhP0PJleNTUhusdY5Jb7BGgQfNK92L2z0K_qqBnzxADIYGC0cEVzhpYbosXFxtPgUx0x6Sgg6OReMQ28hUlTCUh0NshE8_LF1rG6kOJ4C2cXf6pCEdOjcOjrdzN_MpUQtUfbCZnSGPY0Pyh1dfaSxPp4pK_e-arv-nuC2E_6wPJ36nOBhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n4iF_Bfwwsedb4lcJIpQ80H5u3ZBep6kUSuG0NhktP_0_b5wgFvDKWflOP1ojGYW2_xWn4U4EcuLP0ozWr1cwt4wRz_6qhhj1c4SDMxLp-k7hibHT3B3cuoeNToAjJKgu8xRAUgsuzfgJ_GzskArA3YPY_YDYOLnC-Nv92ACEqY5pvzlBjiMF95H6LyaSru6e0xiXXLFCtXJdhxK6iDxzgdvmG7u1DAo5t5BnoPd4Gyd69sT2cIjuO6Km2ZwBQJ2vQvWcdzSZsRClfgd7BkhQ6VBasDsDsv8gmbZlza6SxZeQeQr4qKunaC5aLihWSgYXuWeGhK8cX15gzRMv1eFZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1x6-hWGBCNXceQ3-OLlTgZdFKhphXWGGl-Q-TUfgZr_VyLi2kbBCZoQaYC3HG7LNVDmuuTE_uIdTRNJ9cSFR5xqQO1VQrTRdR3UGtUQzadpLYeyxAr3kMWS8500nV500wlXxqq1I79OR_ErvFpWo2zWdrjIvp9cJUjZG6yu6j2WXCg0gOqqszrKYGdWUM85gsHJLI4tEXqGoAD__glSkWeCdq9lYMxYTFY8UgYv65m8X0jr83S_yvoDJXlATFYjlNA71m77AYAgNnRV9Z2EQB3FpCwGOCh7wXKqwpzk_7OpGCyk6D7J98j-HLszSInA2FC-G-YjC53-pdxjUn-Gpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pfidtyx8fnYEzF3rxYGJ5kI7Ej089cCsUtk6PS9kGu9kAm0LyIS6cLMXqHsnhWkMZonL3xjOVs2RfkdQzYsOxjyOcxybyy0DAtT1aZpjYPCKEuevxmbCdT7wWomKuYQ56Kc0NPQ4MggUlfzm4IMg4wy3StvY888MMhxGbgUjBmn6lU7EMCUfnSSaCergzA2Gik6QN4otzO73e75rLIGBcnAU9x0ShME4nzTviTz6xr_w_mq6VjDdDI1pe3gIvLR6UAvvVrXQaBIYZpbTL17NTUL2rItyHkkRkCjhqHtDSP1O5XAFYpQZlsjBO2pTysUHeF98cJS4c68y12VllxHuKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم بزرگداشت رهبر شهید انقلاب‌ از سوی آیت‌الله سبحانی
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/450900" target="_blank">📅 18:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450899">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BC9haJ_DQr1mrrdJEKv7mzaxxA_rpEk-JxnVw31sazSl6MVp9t9CcdTpsrnCS9L_G0P4DpuBB2mqsAxw6XBR81ucgKcsNQb0zq6YeDCbiROUoZ2cTKU-KSIIz2W4rGBdHlKAT0DwilWMpZhnJ2KveQsuD4O3Omttpne4eS1iPpo9FnYHzGKFDRWI9YyOQn208BosgyNWSWIL_hwDOwyDthDWnD5QJn1B8B7IDpI-A1FCO6Twn7fI6YsphO1dcsiHf5QT1oPxyRIOkBk2JceCgI7QRd5bbu-ZIKJyIG4B2iJ8srReuJqmuv9WDpyDJ9cQrZnIpjeyKyqM1TxRoecXWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واریز بخشی از مطالبات گندم‌کاران
🔹
بنیاد ملی گندم‌کاران: ۳۰.۸ هزار میلیارد تومان جدید به حساب گندم‌کاران واریز شده است. با این پرداخت، مجموع واریزی‌ها به ۹۳.۱ هزار میلیارد تومان رسید.
🔹
از زمان آغاز خرید تضمینی در فروردین ماه، ۶ میلیون تن گندم به ارزش  ۳۰۰ هزار میلیارد تومان از کشاورزان خریداری شده و حدود سی و پنج درصد مطالبات پرداخت شده است.
🔹
بر این اساس، حدود ۲۰۷ هزار میلیارد تومان از مطالبات گندم‌کاران همچنان باقی مانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/450899" target="_blank">📅 18:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450898">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🎥
می‌خواهم در پایگاه‌های آمریکا شربت پخش کنم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/450898" target="_blank">📅 17:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f462e38c0.mp4?token=lNOmKKClD6COBUOQ6tofRd0heAqP6lIdHjzperME__B64nRG0QUsg8C_foa-f752dGZz1HfsE21q1Ooc2ryO4CFiYr5GuJ4srdKZPppSgrXhwKUbflc4IW_a8CsAgbbQORI_D2aomvv_FaxflBrCAResLRRcbPJj_RgmotrYcbqmOFskFD7JAICLZ5_wkVuI27eROdRhZe_FsKLBEyrUqhvpUwrpYVMmMWRcrGZ4CIqdOgxWkuOxIgz5UcbRtft0lfiV5zBRuTUGYAxtvIq6Z1FUOiPA2XzWkDCLq4shZ8htDVA4AZZY7s6mOG7sV7L_KjsAAqQEdy2CKzdiC6N01w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f462e38c0.mp4?token=lNOmKKClD6COBUOQ6tofRd0heAqP6lIdHjzperME__B64nRG0QUsg8C_foa-f752dGZz1HfsE21q1Ooc2ryO4CFiYr5GuJ4srdKZPppSgrXhwKUbflc4IW_a8CsAgbbQORI_D2aomvv_FaxflBrCAResLRRcbPJj_RgmotrYcbqmOFskFD7JAICLZ5_wkVuI27eROdRhZe_FsKLBEyrUqhvpUwrpYVMmMWRcrGZ4CIqdOgxWkuOxIgz5UcbRtft0lfiV5zBRuTUGYAxtvIq6Z1FUOiPA2XzWkDCLq4shZ8htDVA4AZZY7s6mOG7sV7L_KjsAAqQEdy2CKzdiC6N01w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پنجمین تلاش آمریکا برای توقف خبرگزاری فارس!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/450897" target="_blank">📅 17:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450896">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‌‌
🔴
سی‌بی‌اس: مقامات آمریکایی اعلام کردند که ایران در این هفته دست‌کم ۲ پایگاه در اردن را هدف قرار داده و چندین نفر از نیروهای نظامی آمریکا مجروح شده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/450896" target="_blank">📅 17:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450895">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKlJ0-CA3EiEQTxPVymFkMSTzArkLloTj1Vh1PzATGgnx1VAqsFxMRGl9jPWXJkiZUtrOIKSAfX3VCvSZY7dfu-lxZq0VOKDT_bOubcL3VQaideE0CZ4bTB7uSwjYFkaAhuoitfgZZdjWZ7S-U_qB9GeHfylQrzB7aBjsV4Eg93M8jOE_5r4e4wh9PhBLJ7VPyB9mPy9-zPMMUt8AQWFRAtOIbfcAL5d95nA47eMud4TMZRW2KdLPITVR0Scfj8WSc1DAGrO-h4QKV7UWXVknFiWMHWJx__zLsNFiPpxnLKBB3FASZzMTaQtqDfpK_cmfwhDknfAxwMQuaNUUJQjlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسران والیبال ایران بر بام آسیا ایستادند
🔹
تیم ملی نوجوانان والیبال ایران در فینال قهرمانی آسیا، ۳-۱ ژاپن را شکست داد و بدون شکست قهرمان شد.
🔸
ایران در ۱۳ دوره‌ای که در مسابقات شرکت کرده موفق به کسب ۸ عنوان قهرمانی، ۳ نایب قهرمانی و ۱ مدال برنز شده و پرافتخارترین کشور این رقابت‌ها محسوب می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/450895" target="_blank">📅 17:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450893">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1dd38297f.mp4?token=PVbWfsuMfNdf4J4T8f4UJr7rfFsj3LtC_7XWZopxVNQjEecV_e39KtB282J8FbeHhkMc7KyNU_q-fFKHkZqHIs8IBWgIJfa06IUOHKbEUkeubSruG--5OMr3JigvjgAyKr8IfhNygnGMgFreI9M6TcsAfffJ1OrlaGHREyxenjo1WlhsilxUmZ9UbO9yPRcJvQ6CHAJbPm6U2aFXvUDlBx-t_hqZo-jQTRwNIfoYPVOBjd5_rNkew60oBbROn8a2dUtJ-JHMvywlfHPMwRkW21QpzIc3RV3YP3Xy4DF7HHm2UeM-DQyEFAImxgsSbyaKjTUzLiH6yOduhM4hBFVfpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1dd38297f.mp4?token=PVbWfsuMfNdf4J4T8f4UJr7rfFsj3LtC_7XWZopxVNQjEecV_e39KtB282J8FbeHhkMc7KyNU_q-fFKHkZqHIs8IBWgIJfa06IUOHKbEUkeubSruG--5OMr3JigvjgAyKr8IfhNygnGMgFreI9M6TcsAfffJ1OrlaGHREyxenjo1WlhsilxUmZ9UbO9yPRcJvQ6CHAJbPm6U2aFXvUDlBx-t_hqZo-jQTRwNIfoYPVOBjd5_rNkew60oBbROn8a2dUtJ-JHMvywlfHPMwRkW21QpzIc3RV3YP3Xy4DF7HHm2UeM-DQyEFAImxgsSbyaKjTUzLiH6yOduhM4hBFVfpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هجوم مسافران برای خروج از کویت
🔹
بعد از هدف‌قرارگرفتن اهداف آمریکایی در کویت، فرودگاه کویت روزهای شلوغی را سپری می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/450893" target="_blank">📅 17:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450891">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Aq0_QvuEcIe8F_6OgxVwjhkeVqmFVLCG85VoSEfYU52UtfKv2GcrmDG9D5ce2j6Ir73Gk8A2LlTnN8u-z0PIQBBD9V8RpIl5JHYwZ5ahhwCgYhtkUL3e55MRPhQkZMgo5eoZXKACTZmx0S2Zqc0txWVlXl1uXck7XnEL0cZUmUGIzF84hoywobEwC78_VkgarhNjK-ro_Qh7yDSvk0hmC1E6I74EbGHOjW8haYXtSMrDTVT3XybHL6_07B-ve8VYRctKHPtQuYJSZZZfvtgml7lTQmen1kQUXkuUiumhTLWpkvfxov-HLQVduheq1G8QnhFL00n4pIhvMYJLWwxjlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZ6jczelrnpINpPOFrA7srhZv5V2ho0uOjPibHn9DIIvKQxlUCPAaW7inrnJqSkceQn9SdW53p4UgEoJ-WFaUEK1u1Jcwc8-zJB2z9wK8uEdF9FYhQUef5D1SLvEtuK6-1Lj487cR3yDSa1YpXjYrYjY2s8oHNeib5ECnk6r7V4xex8728LKfvljomG8aFGSZ3xZoYut5UYVdeK1yta0z5phRhenwffOBBoXn4EhqDMAdy_-29kSPAy-tf-L96OJtUL5ntioF3IEqA5wqcA8HniiIlkjztOAUTV9IhCfrb_vvi9HRJPuvGYGYCiPvEE_Cvjm_QrpxXpKUqbVqkGsuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
حمله به تروریست‌ها در سلیمانیه عراق
🔹
به گزارش منابع خبری، در این حملات، مقرهای تروریست‌های تجزیه‌طلب ضد ایرانی هدف قرار گرفت.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/450891" target="_blank">📅 17:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450890">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/behevu-dKwY4OmN7dDb3Spk7TM4znK2FakOInoEPyJATzmBv3vYyM3-vORG6Nzxi3ExFwKHdMmx4Ix8J37uhOIGGgqNWYhCAphgy_OUOvwI6EfV0GzVIqVSTDpHczsFmGYiJIOg6LdTloiN8l1XWN0F4r59a3z23PfQfM4Mfc4aOgs6oRm4WxFjBbG-f1MBgTfCwTGIsMJ3kJ5EPMH_BWjw5iKt-WdJBS5nm20gEF_FOZe5NeS785FnTYZdHP3Z8gxu7PCB4U3UOIXTFQw3q8adxI2NmzB90MRcCAoGm_IFdrb9ZWnfKyBpicyI9nvgC5woz5Y7lKEJ0mqxFEirZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع برق بیش از ۵۰۰ ادارۀ بدمصرف در تهران
🔹
شرکت برق تهران: تاکنون محدودکنندۀ مصرف برق در بیش از ۵۰۰ اداره که از سقف مجاز مصرف فراتر رفته بودند، عمل کرده و برق این ادارات قطع شده است. این رویه تا زمانی که ادارات مصرف برق خود را کنترل کنند، ادامه خواهد یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/450890" target="_blank">📅 17:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450889">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
هشدار یک مقام امنیتی در گفت‌وگو با فارس: در صورت حمله آمریکا به زیرساخت‌های ایران، فرودگاه‌ها و بنادر امارات باید فوراً تخلیه شوند
🔹
یک مقام آگاه در نیروهای مسلح در گفت‌وگو با خبرگزاری فارس ضمن هشدار نسبت به پیامدهای هرگونه اقدام نظامی آمریکا علیه ایران اعلام کرد: اگر امشب آمریکا به زیرساخت‌های غیرنظامی کشور حمله کند، برای حفظ جان شهروندان از حملات متقابل ایران، فرودگاه‌های دبی و ابوظبی و همچنین بنادر فجیره و جبل‌علی باید فوراً تخلیه شوند.
@Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/450889" target="_blank">📅 17:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450888">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c448a578a.mp4?token=o2Y7uX7Y0uafeEPTYsvvkrSqnVe79LXOhDsdieuXVHwtRXcDv6plHvewLMVBdQuaMVjJgFXvk9W0bJRWrusINAD-8ReQC8XrSIjV1AND6uM-dfMg1MbJ0I5mp2p3Ce8eBatlzj24P6YGjuYoq7lJXtBeIyJwxigUodF7nN2E9ULaTc5KkuNFLCpB7enoOsAyR7yv7duewDQ_-s4-Zc72iuMFhkK43nQ76Fo5stnLmG-tviv_hduUCfA6H6It5tburoqWMNs6pLARAUzP27ThhHtWVOUrc2e-UU9b1-K7tdQC9gvpdgYaLaWjPnOt99qk1Czej4vNTeOMzWLrB3mfOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c448a578a.mp4?token=o2Y7uX7Y0uafeEPTYsvvkrSqnVe79LXOhDsdieuXVHwtRXcDv6plHvewLMVBdQuaMVjJgFXvk9W0bJRWrusINAD-8ReQC8XrSIjV1AND6uM-dfMg1MbJ0I5mp2p3Ce8eBatlzj24P6YGjuYoq7lJXtBeIyJwxigUodF7nN2E9ULaTc5KkuNFLCpB7enoOsAyR7yv7duewDQ_-s4-Zc72iuMFhkK43nQ76Fo5stnLmG-tviv_hduUCfA6H6It5tburoqWMNs6pLARAUzP27ThhHtWVOUrc2e-UU9b1-K7tdQC9gvpdgYaLaWjPnOt99qk1Czej4vNTeOMzWLrB3mfOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هجوم مسافران برای خروج از کویت
🔹
بعد از هدف‌قرارگرفتن اهداف آمریکایی در کویت، فرودگاه کویت روزهای شلوغی را سپری می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/450888" target="_blank">📅 17:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450887">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6hsXUnDEbiIPfL7M14V7QmdmS9I1jz5nBtYB3VkzoOzfcTcuDCCaj519RVwPX-NXURiCly33aObrMR8CF6SwEYoB5Oadsiv2MRtpgInW2eXLWXNvNB2YL1a4GXM00WSMPOlsibtwR5yqhTC6QnkGY1qijVKs4v4fHRNycSxjYTbHiD2MNknD8WSCR79rVtLNZpw4o89i5hNJ1gwVq1lIi6-WUF-UM4bfux2oNszIMYaprAiZrVjTYGQ7BxJ8jClQ8WU0RT1TXUJTIBb9CalfgODmShNBVQNK10YJPNXsBGm-Js0lXp-voGZ3HA6Sn9t48mDs2pVNVKGjV0FcGhsPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل تصاویر ویرانی مراکز حساس کویت در حملات ایران را محو کرد!
🔹
براساس بررسی تصاویر ماهواره‌ای گوگل، مشخص شد که این شرکت تصاویر با وضوح بالای چندین تأسیسات حیاتی در منطقه «الشعیبه» کویت را به‌طور عمدی محو کرده؛ این تأسیسات شامل نیروگاه برق، تأسیسات آب‌شیرین‌کن،…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/450887" target="_blank">📅 16:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450886">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2109385f6f.mp4?token=ShsMJmLLdthz701kDl67Gykw6FnonQcYW1uVzfUwgm8y-5-2K1rOUDx1XCq3CT_J2ytiA3rR1xOc2Sq12_XndDQCLLDbrqYAimvQC-C4lZ4iJ4pjrjDk2UDDuLdeeW43J8sx54XgwuN7EyaeSwIRb8-_CKnpZfENfYtnYGfP9eczUuUvyZVva1Tqkyi6BsYZpfjp_VxVqGOvhYDGezbT6cEhuup9ig-FrdnXxBraY7F6aVceCd2LHgBwio9ackOdfMThZGVAn9fbOsZpp75g5SqrMH_q-RO_Qz2tDgDdv5ssS7h_O4j6FT2-1EYa18N1qeH4WevXS4R9GXqGbPePxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2109385f6f.mp4?token=ShsMJmLLdthz701kDl67Gykw6FnonQcYW1uVzfUwgm8y-5-2K1rOUDx1XCq3CT_J2ytiA3rR1xOc2Sq12_XndDQCLLDbrqYAimvQC-C4lZ4iJ4pjrjDk2UDDuLdeeW43J8sx54XgwuN7EyaeSwIRb8-_CKnpZfENfYtnYGfP9eczUuUvyZVva1Tqkyi6BsYZpfjp_VxVqGOvhYDGezbT6cEhuup9ig-FrdnXxBraY7F6aVceCd2LHgBwio9ackOdfMThZGVAn9fbOsZpp75g5SqrMH_q-RO_Qz2tDgDdv5ssS7h_O4j6FT2-1EYa18N1qeH4WevXS4R9GXqGbPePxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، کارشناس حوزۀ مقاومت: پایگاه‌های آمریکا در اردن پاسبان اصلی رژیم صهیونیستی هستند
🔹
تمرکز ما بر اردن باید به اندازۀ سرزمین‌‌های اشغالی باشد.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/450886" target="_blank">📅 16:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450885">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اطلاعیه دولت: مراسم بزرگداشت امام شهید انقلاب که مقرر بود روز چهارشنبه از سوی دولت جمهوری اسلامی ایران برگزار شود، به روز یکشنبه ۲۸ تیرماه، ساعت ۱۰ صبح موکول شد.
🔹
این مراسم به میزبانی قوای سه‌گانه کشور در مصلای بزرگ امام خمینی (ره) تهران برگزار خواهد شد.…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/450885" target="_blank">📅 16:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450884">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45191fb108.mp4?token=CqkdLCMwplOkUWJbhWKx69BmrReipQqXnBIqDo9SUIKe8gXUsx4EabE4pK0RMbMqyFsJRcY5hsYd6VsJ3orrZH3gpiAnIuSqRw-raQJSPnrj8Gh1r8OtwDzHvMbnXZxkFxmLLUVAUodQSG1Rr0VD_l0I0666x8lef6iwzvRyuexq53RTzbsuVHUoqfh7XtCUni6haWTQ-nTbSzueAz4_8tZe1aGyUO65ENeGpop0srt0vkQ1fJjaSxkWEnkOQZ8QGPb005rFupsU0oaE6-JPrjfgkUhSS-DgCzVZ5LyPzgOes5-jWRolWbR6M6BwQXrZ9gL4KxQ1J9EA6ocl640csQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45191fb108.mp4?token=CqkdLCMwplOkUWJbhWKx69BmrReipQqXnBIqDo9SUIKe8gXUsx4EabE4pK0RMbMqyFsJRcY5hsYd6VsJ3orrZH3gpiAnIuSqRw-raQJSPnrj8Gh1r8OtwDzHvMbnXZxkFxmLLUVAUodQSG1Rr0VD_l0I0666x8lef6iwzvRyuexq53RTzbsuVHUoqfh7XtCUni6haWTQ-nTbSzueAz4_8tZe1aGyUO65ENeGpop0srt0vkQ1fJjaSxkWEnkOQZ8QGPb005rFupsU0oaE6-JPrjfgkUhSS-DgCzVZ5LyPzgOes5-jWRolWbR6M6BwQXrZ9gL4KxQ1J9EA6ocl640csQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاکر کارلسون: ادعاهای آمریکا درباره قدرت نظامی‌اش، پوشالی از آب درآمده است؛ تحقیر مداوم ایالات متحده، چشم جهانیان را به واقعیت باز کرده؛ ارتش ما با بودجه ۱.۵ تریلیون دلاری حتی نمی‌تواند یک تنگه را باز نگه دارد
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450884" target="_blank">📅 16:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450883">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">۱۱۶ دکل مخابراتی هرمزگان از مدار خارج شد
🔹
اداره‌کل ارتباطات هرمزگان: در حملهٔ دیشب آمریکا به‌خطوط انتقال ترافیک و پهنای باند در بندرعباس و حاجی‌آباد، ۱۱۶ دکل مخابراتی از مدار خارج شد.
🔹
درحال‌حاضر تلفن ثابت، تلفن همراه و اینترنت در برخی مناطق شمال استان…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450883" target="_blank">📅 16:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450882">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رئیس کمیسیون اصل ۹۰ مجلس: ادعای تبرئۀ زنگنه کذب محض است
🔹
حجت‌الاسلام پژمانفر: ادعای تبرئۀ بیژن نامدار زنگنه در پروندۀ کرسنت، کاملاً کذب است. اگرچه رأی صادره در اردیبهشت‌ ۱۴۰۵ مبتنی‌بر «تبانی در معاملات دولتی» را از حیث میزان مجازات ناکافی می‌دانیم، اما واقعیت این است که در مرحلۀ بدوی، زنگنه و مهدی هاشمی رفسنجانی به یک سال حبس و انفصال دائم از خدمات دولتی محکوم شده‌اند.
🔹
البته مهدی هاشمی پرونده‌های دیگری نیز دارد و ۶ نفر دیگر که مرتبط با این پرونده هستند، هر کدام به ۳ سال حبس و یک سال انفصال از خدمات دولتی محکوم شده‌اند.
🔹
ما این اخبار کذب را بخشی از یک جریان سازمان‌یافته می‌دانیم که در برابر این فساد بزرگ شکل‌گرفته در کشور، تلاش می‌کند به مردم القا کند دستگاه قضایی در برخورد با مجرمان هیچ اقدامی انجام نداده است.
🔹
این احکام هنوز قطعی نشده و پرونده در نوبت رسیدگی تجدیدنظر قرار دارد و در ماه‌های آینده بررسی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450882" target="_blank">📅 16:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450879">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4286e833.mp4?token=hUXGZTjYO_s9ZSfFsyyIMpYy_cAIrYe695mMNvr0TymNx8dxkmH2_4kxgXTDXX_vYDdTqDJ15K4UVdgHRyL7NWhbvY3G-MEO-0yFehaK_Xnemp0QcH1YigM9FBASOc4nTSAtfsmSr47u4GrkdfixiFRpMA18CUc5pXEgixlDAyYnMmDLTQwy8G6DJejDE1a3nycsJ2bvgOSmhbxFO0Boz0OTS9uot-8sfGG3uUGyy2VkStXYEK80V6CAI2hbVcodLxML1LQscNcQYz-Woto8glStaI5Vdk5K8DyQ1A3Gle2JrOe6YIl9J1o4Lr2MM3OS4Z6eKhHumzknffKUTMFciw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4286e833.mp4?token=hUXGZTjYO_s9ZSfFsyyIMpYy_cAIrYe695mMNvr0TymNx8dxkmH2_4kxgXTDXX_vYDdTqDJ15K4UVdgHRyL7NWhbvY3G-MEO-0yFehaK_Xnemp0QcH1YigM9FBASOc4nTSAtfsmSr47u4GrkdfixiFRpMA18CUc5pXEgixlDAyYnMmDLTQwy8G6DJejDE1a3nycsJ2bvgOSmhbxFO0Boz0OTS9uot-8sfGG3uUGyy2VkStXYEK80V6CAI2hbVcodLxML1LQscNcQYz-Woto8glStaI5Vdk5K8DyQ1A3Gle2JrOe6YIl9J1o4Lr2MM3OS4Z6eKhHumzknffKUTMFciw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
ارتش کویت از تداوم حملات پهپادی و موشکی به خاک خود خبر داد
🔹
ارتش کویت با بیان اینکه چند موشک و پهپاد را در حریم هوایی خود رهگیری کرده است، گفت که ترکش این موشک‌ها باعث وقوع خسارات مادی شده است.  @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/450879" target="_blank">📅 16:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450878">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان می‌خواهیم که به نزدیکترین مکان امن بروند.  @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/450878" target="_blank">📅 16:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450877">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bac2171a2.mp4?token=XbzWxcouTPiDY4WnP9xgshuTlmh7_tSgCiFoOGpBtoBVL5E5KRcDK26IA3GS_86FVQPaJLsz-qeqGHzOt4EH7SzHa3UCcpi32Qj9QFp7_CoEun6i1bzXODAsVZHl_8847yqLJg-us1JbSS-XiccszSMVubbVIwVHOZfumkXsU9WNbinMLqt4mPss0qXUNoI7Yd3X_YUIMzhOS-yhmeiowoig9ZI5QyFBRPAeyjeJ2S92fLaCrESjHCLzypSvUhQ77qVBgbmwtA0zund9jpO38N45MplgysOTkh4GgBd0G2TrG5y4VzoGusBgjRNZA7sNu9LO2r65TzBRvV40xmHO7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bac2171a2.mp4?token=XbzWxcouTPiDY4WnP9xgshuTlmh7_tSgCiFoOGpBtoBVL5E5KRcDK26IA3GS_86FVQPaJLsz-qeqGHzOt4EH7SzHa3UCcpi32Qj9QFp7_CoEun6i1bzXODAsVZHl_8847yqLJg-us1JbSS-XiccszSMVubbVIwVHOZfumkXsU9WNbinMLqt4mPss0qXUNoI7Yd3X_YUIMzhOS-yhmeiowoig9ZI5QyFBRPAeyjeJ2S92fLaCrESjHCLzypSvUhQ77qVBgbmwtA0zund9jpO38N45MplgysOTkh4GgBd0G2TrG5y4VzoGusBgjRNZA7sNu9LO2r65TzBRvV40xmHO7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بغض‌های سفارشی برای جنوب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/450877" target="_blank">📅 15:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450876">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ba45eebb.mp4?token=lgK9yY6MkMmyfFCIUOduBI0GWzHiD32lL7CKhtt57XiJ7OWmXATGL0oavPYawG3Zf_C_LOqwDNFE-_Rh8ZOKfK0qvSJ8OnY66VkWJk5nBnjBRVa9W38YH8NRrsrifhbuIlPUIvoCoXCQpCzqrguss3tTH9LkDV0W_8xw_k26eo8veECclIaOK1g5qbDLbOaZ_zv_7nR6fz5JShwewjpbm8waLj2mmXVbDaVh3QePNgW8YEAWCNpb56ceY1kd0T6gzJ1JwbH1iFotuuPT0bTaF5YwWdbt9fjhrX_e7NQRu84gHQyeJyJgX_uDlkRKjrtwITYM1VOIoFS8C5ckMwDCkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ba45eebb.mp4?token=lgK9yY6MkMmyfFCIUOduBI0GWzHiD32lL7CKhtt57XiJ7OWmXATGL0oavPYawG3Zf_C_LOqwDNFE-_Rh8ZOKfK0qvSJ8OnY66VkWJk5nBnjBRVa9W38YH8NRrsrifhbuIlPUIvoCoXCQpCzqrguss3tTH9LkDV0W_8xw_k26eo8veECclIaOK1g5qbDLbOaZ_zv_7nR6fz5JShwewjpbm8waLj2mmXVbDaVh3QePNgW8YEAWCNpb56ceY1kd0T6gzJ1JwbH1iFotuuPT0bTaF5YwWdbt9fjhrX_e7NQRu84gHQyeJyJgX_uDlkRKjrtwITYM1VOIoFS8C5ckMwDCkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غریب‌آبادی: تعهداتمان در تفاهمنامه اسلام‌آباد را متوقف کرده‌ایم
🔹
معاون حقوقی وزارت خارجه: آمریکا تمام تعهداتش در چهارچوب یادداشت تفاهم اسلام‌آباد را زیر پا گذاشته و متوقف کرده است.
🔹
ما هم تعهدات خود را متوقف کرده‌ایم، در حال اجرای آن‌ها نیستیم و مشغول دفاع از کشوریم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/450876" target="_blank">📅 15:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450875">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سخنگوی قوهٔ‌قضائیه: دادگاه رسیدگی به پروندهٔ شهید امیراحمدی آذر برگزار می‌شود
🔹
پروندهٔ شهید سلمان‌ امیراحمدی که در اغتشاشات سال ۱۴۰۱ به شهادت رسید در دادسرا تکمیل شده و دادگاه در آذرماه برگزار می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/450875" target="_blank">📅 15:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450874">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان می‌خواهیم که به نزدیکترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/450874" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450872">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd7c7e6a3e.mp4?token=fDPNv6KUB9HoRR0uDbszN-NdKFwE0LKjJF3upaeFospejXN6TV5Zmh_NPpqvYkJ45Cxh_OwsHwSSaLGNqYkagZdhKaeDRuq0Q6kHxMWL7u0XWoM-Ohi9mahbthXnGSrbgVAWH06Gl8ruSUrNtHBvosPEo_XtaG8qEdyR8z9EOvpaaDiCox4r0lAfiunupDU-G9KbyRJ4diRZjyJXbFu439__5u8lPuYFLAdbC3v2BTObXHKUGcP1wnAqMdrH9Tlt7WBr0l45ZqflNacm7gBg44CzNlpt0MOnRYgA9P9zSX_IQ99BIR0UNHDSH0wfbyfB6HudYucfjiTbPp3rkMrVt7XFoKpdjUrFnsW9qAvJ7h7Ouj64FYkEthgqFcnGDZD5SxBsTPTy-Cy3EpgRDBWraSmjlLb9-HNmwn1P2OTo8o2h29fNub7ee5q04nUD4HRZPSPE6JedTkuSh7WfFqHXgs6fAZY8k4q4MyOJIXhO9aHppVs6OCohkXDbPj-s6w0AZsklfc2hScOiXvBEc1BaeasKxV9X65r_OrHkl2Mij5VwrBUQdlyBFXVJugdI9ydA4ds8_k5znfL4INpQTk26uJe9EBr2fAlPDaMpr7SD1ZdUjuF_pAG66RD6pGqCAsBNdMzaZoiIjpRcskuX5AZ_Xf8U31OrVDsHW4UYE5FVlN8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd7c7e6a3e.mp4?token=fDPNv6KUB9HoRR0uDbszN-NdKFwE0LKjJF3upaeFospejXN6TV5Zmh_NPpqvYkJ45Cxh_OwsHwSSaLGNqYkagZdhKaeDRuq0Q6kHxMWL7u0XWoM-Ohi9mahbthXnGSrbgVAWH06Gl8ruSUrNtHBvosPEo_XtaG8qEdyR8z9EOvpaaDiCox4r0lAfiunupDU-G9KbyRJ4diRZjyJXbFu439__5u8lPuYFLAdbC3v2BTObXHKUGcP1wnAqMdrH9Tlt7WBr0l45ZqflNacm7gBg44CzNlpt0MOnRYgA9P9zSX_IQ99BIR0UNHDSH0wfbyfB6HudYucfjiTbPp3rkMrVt7XFoKpdjUrFnsW9qAvJ7h7Ouj64FYkEthgqFcnGDZD5SxBsTPTy-Cy3EpgRDBWraSmjlLb9-HNmwn1P2OTo8o2h29fNub7ee5q04nUD4HRZPSPE6JedTkuSh7WfFqHXgs6fAZY8k4q4MyOJIXhO9aHppVs6OCohkXDbPj-s6w0AZsklfc2hScOiXvBEc1BaeasKxV9X65r_OrHkl2Mij5VwrBUQdlyBFXVJugdI9ydA4ds8_k5znfL4INpQTk26uJe9EBr2fAlPDaMpr7SD1ZdUjuF_pAG66RD6pGqCAsBNdMzaZoiIjpRcskuX5AZ_Xf8U31OrVDsHW4UYE5FVlN8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آن شب، آن بیمارستان
🔹
با اینکه خدمت‌رسانی دوباره در بیمارستان شهید بقایی اهواز پس از تهاجم هواییِ آمریکا به محدودۀ آن از سر گرفته شد؛ اما آنچه در آن شب رقم خورد، از خاطرات مردم خوزستان پاک نمی‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/450872" target="_blank">📅 15:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450871">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">۱۱۶ دکل مخابراتی هرمزگان از مدار خارج شد
🔹
اداره‌کل ارتباطات هرمزگان: در حملهٔ دیشب آمریکا به‌خطوط انتقال ترافیک و پهنای باند در بندرعباس و حاجی‌آباد، ۱۱۶ دکل مخابراتی از مدار خارج شد.
🔹
درحال‌حاضر تلفن ثابت، تلفن همراه و اینترنت در برخی مناطق شمال استان با قطعی مواجه است که تلاش برای وصل‌کردن آنها در جریان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/450871" target="_blank">📅 15:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450870">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cckDhqideT2AYneSjyre6Igp5BsXAhlAq8eBWHIDnDt_tKusUCot7ELNUWo5fV4YA--8wvCLjwPSkS5Db-VNy635jKCie-BOc6duUHswffB94QXPAhwitgAyq9IIi72naA0_aH9oSZG6VJDNNmbsStNyf3LmSIkRz-mD-0PN__As7vfNIP7UFSQDuC56lo2KMw_Yi2YD8OC0KR61qf-Co1X85dLXbmRZlHmRdKHmFfqFNev4oUualBQAgnQ8PAvz796E60KjQ-xG0Z6HYGR51Qo-UPTExudGRdZVDxhHrTSU6pys0nYKPNr6BC4mWaC1AA6IDYBSz9oQW5H_oZO8hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
حملات پهپادی به مواضع آمریکا در اردن
🔹
درحالی‌که منابع خبری از شنیده‌شدن صدای چندین انفجار در اردن خبر دادند، ارتش این کشور مدعی رهگیری ۳ پهپاد شده است.
🔹
منابع خبری می‌گویند در این حملات که با چندین پهپاد انجام شده، پایگاه‌های آمریکا هدف قرار گرفته…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/450870" target="_blank">📅 15:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450869">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3238bd6396.mp4?token=OJC3ygIWudXbbf7kbVAUA6AQmN4gSvWAVDMw-AtCdrscY7DEtwxvhiIiF-REmLpE4-ns7V2GPYzu4wnykJXwIyqzrxAJ--QzsoakOr_01Y_xsp4pcXqzX4-jjCTBsmCsPnGciRcYqov-hNlLivO99y5-UNqobFEwSKs5-9Wx9mIL3BI-kCAfhnjZlu0UPaVDp9YQo62_7rsmqQs2zllHp6yJ96AGtz313LpAXJ6mobGfryXnuANOisQW5ESR_eISS_r5GbHWba8-pjgOPCkIfhQITfiK4_H-i2iCsDJIYNIkX3hiUqkDmDCGBjgPfNfBFR1kRXZHm21Gpdk2U5wo7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3238bd6396.mp4?token=OJC3ygIWudXbbf7kbVAUA6AQmN4gSvWAVDMw-AtCdrscY7DEtwxvhiIiF-REmLpE4-ns7V2GPYzu4wnykJXwIyqzrxAJ--QzsoakOr_01Y_xsp4pcXqzX4-jjCTBsmCsPnGciRcYqov-hNlLivO99y5-UNqobFEwSKs5-9Wx9mIL3BI-kCAfhnjZlu0UPaVDp9YQo62_7rsmqQs2zllHp6yJ96AGtz313LpAXJ6mobGfryXnuANOisQW5ESR_eISS_r5GbHWba8-pjgOPCkIfhQITfiK4_H-i2iCsDJIYNIkX3hiUqkDmDCGBjgPfNfBFR1kRXZHm21Gpdk2U5wo7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استاندار هرمزگان: با وجود تهاجم به آب‌شیرین‌کن‌ها در ۲۰ روستای شهرستان جاسک، اختلالی در روند آب‌رسانی به مردم وجود ندارد
🔹
در روزهای آینده آب‌شیرین‌کن‌ها وارد مدار می‌شوند.
🔹
دشمن فکر کرده با زدن چند پل و تونل می‌تواند در روند ارتباطات استراتژیک بندرعباس…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/450869" target="_blank">📅 15:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450868">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5afb3ddfbf.mp4?token=hQ-GVjjwfRdEDx8zhZ06pZRZBaV00wPwhOqdRREIQIvJ7FYXo_-9-b5msYoCahRNytoB07TXTMahnqJJRskR6dNPxGs2Rpkb71FN5S4q7F0o4wQF7rhA4FqmVooixe2R6U-umW7Fmva-hy3Jx4hpDO6Gga_My2GuLaqinC7twq5R-8VgD33e5gBeBBduRNRaAqg2FDqYxOToB7dOrhRpgbyRu72orZN9QMRQ1iC33B2trbfXO6chBPgea_b-2rVQL64DUOd0zeTKogsqny-fX-5rygst3TJns4yZ4eyfjtn_yJfPF6j6WeCvUcPWAlfeO6S4Egwh4iX2TTOmN1gStQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5afb3ddfbf.mp4?token=hQ-GVjjwfRdEDx8zhZ06pZRZBaV00wPwhOqdRREIQIvJ7FYXo_-9-b5msYoCahRNytoB07TXTMahnqJJRskR6dNPxGs2Rpkb71FN5S4q7F0o4wQF7rhA4FqmVooixe2R6U-umW7Fmva-hy3Jx4hpDO6Gga_My2GuLaqinC7twq5R-8VgD33e5gBeBBduRNRaAqg2FDqYxOToB7dOrhRpgbyRu72orZN9QMRQ1iC33B2trbfXO6chBPgea_b-2rVQL64DUOd0zeTKogsqny-fX-5rygst3TJns4yZ4eyfjtn_yJfPF6j6WeCvUcPWAlfeO6S4Egwh4iX2TTOmN1gStQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازگشایی یکی از تونل‌های آسیب‌دیده محور بندرعباس-سیرجان
🔹
مدیرکل راه و شهرسازی هرمزگان: یکی از دو تونل گلوگاه شهید میرزایی در جادۀ بندرعباس-سیرجان بازگشایی شد.
🔹
تردد خودروها از ساعتی پیش در این تونل آغاز شده و عملیات تخلیۀ ترافیک این مسیر درحال انجام است.…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/450868" target="_blank">📅 14:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450867">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‌
🔴
شرکت نفت کویت: صبح امروز یک مرکز نفتی مهم توسط ایران هدف حمله قرار گرفت و خسارت‌های زیادی به آن وارد شد. @Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/450867" target="_blank">📅 14:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450866">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d8390497.mp4?token=oFZIZS2kttlzOCwrdGVJxvRT_9PoccSw2ceGQQc3kpHYE1Nu_ItvCAFFNk3QTvUHJxrapeWz6QPpoB3YYacHvjbdXrIh42MC8lBsMp4ykSmsBtWrzAaOF_b6Z1gO8r-Aye3osl24bYCQ8ORRgPH-LJ0CijRNXVSrvmqjEl-99reX_c5Q1L1Vb0Eh-fi4_gHQqkhzax5YtZkl7q3YFfDfVuOicyIHzddI_vIulqZKSrA15TxuwRGvly_SAfvOVTqQ6TXWeQmj9DwtzN1OyyqahfwpbG48GfXznN_w4YfHV2gz-1EKz8LbenNoFou0Un2V5KMqzYt698wSmGHLKMR8qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d8390497.mp4?token=oFZIZS2kttlzOCwrdGVJxvRT_9PoccSw2ceGQQc3kpHYE1Nu_ItvCAFFNk3QTvUHJxrapeWz6QPpoB3YYacHvjbdXrIh42MC8lBsMp4ykSmsBtWrzAaOF_b6Z1gO8r-Aye3osl24bYCQ8ORRgPH-LJ0CijRNXVSrvmqjEl-99reX_c5Q1L1Vb0Eh-fi4_gHQqkhzax5YtZkl7q3YFfDfVuOicyIHzddI_vIulqZKSrA15TxuwRGvly_SAfvOVTqQ6TXWeQmj9DwtzN1OyyqahfwpbG48GfXznN_w4YfHV2gz-1EKz8LbenNoFou0Un2V5KMqzYt698wSmGHLKMR8qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ شهرسازی هرمزگان: یکی از ۲ تونل گلوگاه شهید میرزایی در جادهٔ بندرعباس-سیرجان بازگشایی شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/450866" target="_blank">📅 14:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450865">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfad249ab3.mp4?token=t85RYeIoWrqsZ5nijah6h0M13eXmp05r2CZVipQeNkkwGPaao1PKrk09toptCCa8hTqx1se8tcx2cIEn7bXp3KV9umKIypKkP-y3UYpFMv6tIyR35_L2ADXlMSWI3u97BieRmUTs_xRZjWzcm3Qww2pZWZ9artV8Sd1ppCbeysSwl1GlG6xyPxktYM_VlpHIKjMEH9ZUrqHEO9XaDmL5uDXMtHk0jQOeda4mwhEkG0b6W3ENVTREIp3MHUGE1iZA4MLjPXVrq78lhkby_Ku5la5hUIYr_oHMr348hnVbyDM9AIx6itejnNusUnKwL1-oDgvj40VjK0MmhzICTrKjqHjEwSGTV16QaS-_tFDK3rfsXu5mtXpjpBQ54s5e_5AgM0lPJcVVYEJ3xhbk3X9QOCUdlGI8fXMa_sa7ZkImwtFpFQJSaTaIB_djthifzIOSttCvqbZ4gWTJ0fcgB0TjUznsJ5oSktPMOlGv8A5WCNmFvxLWMIHtmbcC6KroU3RuDvSNjHpCrniJ4Q3xVwLgOLnJs74ZKDPnnMEL-iquBpI1LfDk3dqmUjRMk9wjyOuUs6WiWoSUKxm7UzQeqRO4TVmeKO1j2CGA_xQU9ljN8iBvp1nfXwYeMwfRo02X48c1YvcZp9oT5HH2qWymTsALo_UdJCMeiHoOJpeP8YdZ_68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfad249ab3.mp4?token=t85RYeIoWrqsZ5nijah6h0M13eXmp05r2CZVipQeNkkwGPaao1PKrk09toptCCa8hTqx1se8tcx2cIEn7bXp3KV9umKIypKkP-y3UYpFMv6tIyR35_L2ADXlMSWI3u97BieRmUTs_xRZjWzcm3Qww2pZWZ9artV8Sd1ppCbeysSwl1GlG6xyPxktYM_VlpHIKjMEH9ZUrqHEO9XaDmL5uDXMtHk0jQOeda4mwhEkG0b6W3ENVTREIp3MHUGE1iZA4MLjPXVrq78lhkby_Ku5la5hUIYr_oHMr348hnVbyDM9AIx6itejnNusUnKwL1-oDgvj40VjK0MmhzICTrKjqHjEwSGTV16QaS-_tFDK3rfsXu5mtXpjpBQ54s5e_5AgM0lPJcVVYEJ3xhbk3X9QOCUdlGI8fXMa_sa7ZkImwtFpFQJSaTaIB_djthifzIOSttCvqbZ4gWTJ0fcgB0TjUznsJ5oSktPMOlGv8A5WCNmFvxLWMIHtmbcC6KroU3RuDvSNjHpCrniJ4Q3xVwLgOLnJs74ZKDPnnMEL-iquBpI1LfDk3dqmUjRMk9wjyOuUs6WiWoSUKxm7UzQeqRO4TVmeKO1j2CGA_xQU9ljN8iBvp1nfXwYeMwfRo02X48c1YvcZp9oT5HH2qWymTsALo_UdJCMeiHoOJpeP8YdZ_68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زندگی در بندرعباس، اهواز و بوشهر جریان دارد.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/450865" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450864">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pr6vbDn8-jtet7ewqICY9cHwC1QtDNqeT190CUOVD_BaO---YfVpP63_t6-KF87gly9zLnZ73tJners47v4cyb0jmxehUQmWqqFcwJxyNY6gfTIW8C4QmcAJwlLFPrxPKsMhX706OjxNTTWsrOaBcFHizu4ctTzgPkqZM5a9dDA0VegDXmIHFi34iQYEdAm5MvJNA8eT8ZxCldaF85EmYzwMHKafi-JDiSNFkXV-zHVHKeossSXyqdU2aQ4Ta8UPLvRq_T0lpgaWYahNe2U4wztqR-AuRaww9seWVCCna70Hmfi1NaH7U7vRDk-1nL-GQv0zPak_bOOSm99kz1dPog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ سانسور کامل تصاویر ماهواره‌ای در غرب آسیا
🔹
درحالی‌که آمریکا مدعی دستاوردهای بزرگ در جنگ با ایران است اما دولت ایالات متحده از تمامی شرکت‌های ارائه‌دهندۀ تصاویر ماهواره‌ای تجاری درخواست کرده است که به‌طور نامحدود انتشار تصاویر مربوط به منطقۀ درگیری در خاورمیانه…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/450864" target="_blank">📅 14:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450863">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">قوه‌قضائیه: رأی نهایی پرونده کرسنت هنوز صادر نشده است
🔹
مرکز رسانۀ قوه‌قضائیه: رأی نهایی پرونده کرسنت هنوز صادر نشده و پرونده همچنان در مرحلۀ رسیدگی در دادگاه تجدیدنظر قرار دارد.
🔹
در رأی بدوی این پرونده، تعدادی از متهمان محکوم شده‌اند، اما پس از اعتراض آن‌ها، پرونده به دادگاه تجدیدنظر ارجاع شده است.
🔹
تاکنون دادگاه تجدیدنظر رأی خود را صادر نکرده و بررسی پرونده همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/450863" target="_blank">📅 14:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450862">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انهدام ۲ باند سارقان مسلح در درگیری با پلیس چابهار
🔹
فرمانده انتظامی سیستان‌و‌بلوچستان: در جریان انهدام ۲ باند سارقان مسلح در چابهار، پس‌از درگیری مسلحانه ۳ نفر از سارقان مجروح و ۷ نفر دیگر دستگیر شدند؛ ۳ کلت کمری، مقادیری مهمات و ۲ خودروی سرقتی از متهمان ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/450862" target="_blank">📅 14:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450861">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8c90faa4.mp4?token=J-tWf1z4T2cWbmuAWY5Yd-pUMtrcZ-VAYU1GyvbnbM7Ukr5QKS8GQsnCurx1Yl1WgNlH--gCGG3GReQXG8w2e8JVklW2YmRQYh0C_Bqv9cFtGUvu37SinHBen96Qjl_fRGZLVV8uBYlC89yRraF1cKIlVkFpdouP2IwmNtA3-8kI1V1jHRHIX4a1RkDLdgmBwzxLYUV-DtYKEZd-Y21FUt4plwOTXouojPeVBgUr0IOHnt2xGiTpr8cI8NDxguqF0w1j_CGjiupM_Q9jOO_VYFcuoXsxqsJlIh-arZEH4FUDGPR68UFBmJvysESJsHcO9E3UaxfEGs41Lw8IzdBmsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8c90faa4.mp4?token=J-tWf1z4T2cWbmuAWY5Yd-pUMtrcZ-VAYU1GyvbnbM7Ukr5QKS8GQsnCurx1Yl1WgNlH--gCGG3GReQXG8w2e8JVklW2YmRQYh0C_Bqv9cFtGUvu37SinHBen96Qjl_fRGZLVV8uBYlC89yRraF1cKIlVkFpdouP2IwmNtA3-8kI1V1jHRHIX4a1RkDLdgmBwzxLYUV-DtYKEZd-Y21FUt4plwOTXouojPeVBgUr0IOHnt2xGiTpr8cI8NDxguqF0w1j_CGjiupM_Q9jOO_VYFcuoXsxqsJlIh-arZEH4FUDGPR68UFBmJvysESJsHcO9E3UaxfEGs41Lw8IzdBmsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
حمله کوبنده و همزمان موشکی و پهپادی به شیلترهای جنگنده‌ها و یک رمپ بزرگ توقف در پایگاه آمریکا در الازرق اردن
🔹
روابط‌عمومی سپاه: مردم شریف و ارتشیان غیرتمند اردن؛ همانگونه که ۱۴۰ شبانه‌روز حضور میدانی مردم ایران در خیابان‌ها در حمایت از انقلاب اسلامی دنیا…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/450861" target="_blank">📅 14:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450860">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1w7hh-C0ZpVHrrmAB7eyBbMJxUA2i7-CokaGSPk_O_IJOHp3xobWz3_4qJoIBj_CF3mXKeu2kgEacbNYG1EE26BZv7vMAYi6-tbOFwJDsYC2oy78vOSB2nCI2z2QWdeZ2w2OL-MNZzJkoL54LV8sN80TCFE7gUCNtr6FI4ktXrbRuuhmrw3ZKTc6NGieeJiTXcbZc5Ss4lbR_etC9aOnrA5a39F9jKANLQcYddoVZZOp1ps-3z64y_BtkRHIOL6DADFNr84CWzMKo8St3F5tDyPJByP1Pd3Xj6gV9xedL18h78Ogt91rfMonf_4Rox9NJSRCEiDZZp3yGQXYTFXWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: انسجام میان سران قوا بی‌سابقه است
🔹
در طول تاریخ انقلاب، چنین انسجامی میان قوای مجریه، قضائیه و مقننه برای پیگیری یک حقوق ملت ایران بی‌سابقه است.
🔹
آقایان اژه‌ای و قالیباف با تمام توان، ما را در این مسیر همراهی می‌کنند و این همراهی شایسته، گاهی حتی با نقدهای غیرمنصفانه نیز مواجه می‌شود که جای تقدیر و حمایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/450860" target="_blank">📅 14:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450859">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
گلوگاه شهید میرزایی بندرعباس که دیشب مورد حملهٔ ارتش تروریستی آمریکا قرار گرفت، درحال بازگشایی است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/450859" target="_blank">📅 13:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450858">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b25dd44d31.mp4?token=qIINTEdVQj5dpp0m-zGDw0wxY5sQNXRb9bAST5jOSnm3vkX6sB7EE-LvuHc8CUk4I71c4t4Yoj_Ecjywu8pGxYn442YxpPr3shpq4-HwhAjWKi8JvrStFBjEll1yVLvQo1eAbEil5IGKTeKFAlSb_gjjGr6Rg009ucZ4LijKFHGicLggWcs0ZacisjB9-XcOLy3QWolQ-gZZgkj4eAjg_VDsHTWxDTjjSE_6g0IkAUVc5QVmKM1Ty-TWLseUpFPxOrFhRBCYKGuf6XL4Oj77PGq16wOcNjH4lOQYhLSz9Gmywue1Bogf_4IYDfVu4u7zFUr8tNueY1EAtvuHfi7f5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b25dd44d31.mp4?token=qIINTEdVQj5dpp0m-zGDw0wxY5sQNXRb9bAST5jOSnm3vkX6sB7EE-LvuHc8CUk4I71c4t4Yoj_Ecjywu8pGxYn442YxpPr3shpq4-HwhAjWKi8JvrStFBjEll1yVLvQo1eAbEil5IGKTeKFAlSb_gjjGr6Rg009ucZ4LijKFHGicLggWcs0ZacisjB9-XcOLy3QWolQ-gZZgkj4eAjg_VDsHTWxDTjjSE_6g0IkAUVc5QVmKM1Ty-TWLseUpFPxOrFhRBCYKGuf6XL4Oj77PGq16wOcNjH4lOQYhLSz9Gmywue1Bogf_4IYDfVu4u7zFUr8tNueY1EAtvuHfi7f5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهارمین سوگواری آیینی محرم شهر با حضور و اجرای بیش از ۵۰ گروه هنری از امشب ۲۷ تیر تا ۱۲ مرداد از ساعت ۱۹ تا ۲۳ در میدان آزادی برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/450858" target="_blank">📅 13:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450857">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc523b2083.mp4?token=WWaRIuY2KFXwzBcoZl8vgjisHnt_DD1UjY98fsOlM0dP8eW2ySEZdiowNC5Mr1sT4CzZXROOz7GQ5Cr8AlQWh43AhlpGfE27MfLg151IbMsAHQ4xoGWcvsLOxte13irmnomvq0pT0uuAKtpd-crExz2KLuB5jcPxHWqKpGF4LxoB7W8o09DJ4mXVY5TqoeSc0XxU-_mJ5Wzgbpg86vWlEXqGYq6ijGi9GwyVLDUijAeGgQS4S3_wITxsvJ4QzIXPrmWKBwMoQZ-ufhAykEHDjD1ZJ9VqGAtRE2OFUWNzq4PzgJHhQrmFSeovTeKDnUtF6PVeY3qeBKD2aT-1F07Tdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc523b2083.mp4?token=WWaRIuY2KFXwzBcoZl8vgjisHnt_DD1UjY98fsOlM0dP8eW2ySEZdiowNC5Mr1sT4CzZXROOz7GQ5Cr8AlQWh43AhlpGfE27MfLg151IbMsAHQ4xoGWcvsLOxte13irmnomvq0pT0uuAKtpd-crExz2KLuB5jcPxHWqKpGF4LxoB7W8o09DJ4mXVY5TqoeSc0XxU-_mJ5Wzgbpg86vWlEXqGYq6ijGi9GwyVLDUijAeGgQS4S3_wITxsvJ4QzIXPrmWKBwMoQZ-ufhAykEHDjD1ZJ9VqGAtRE2OFUWNzq4PzgJHhQrmFSeovTeKDnUtF6PVeY3qeBKD2aT-1F07Tdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
✨
✨
حسابتو طلایی کن
✨
✨
✨
‌
🟡
۶۶۶۶ سکه طلا برای ۳۳۳۳ نفر
و میلیاردها ریال جوایز نقدی دیگر ...
‌
✨
جشنواره بزرگ قرعه‌کشی حساب‌های قرض‌الحسنه بانک سپه
✨
‌
#بانک_سپه
#نخستین_بانک_ایرانی
‌
🌐
https://omidbank.ir
‌
🌐
https://banksepah.ir
‌
📲
@banksepahofficial</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/450857" target="_blank">📅 13:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450856">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/450856" target="_blank">📅 13:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450855">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYj3pkaRr2NFNnKqqzTYn9PaWu3ioz4rhpD9mG9Hl-0C-nNzT-6inp-ER_7K-5BdVvtswMs2FqU9CfBzalEh40KPTXnjGlOYSV76ijB7RmYocCzb5Kkdvbi35WPtalOIAQ6vYL1Mr9fxrIV11Sm1U78ClvTYn2eafMsYfIA98NojEcFcnE4umFj30pYwW1o8SedAklBJEx6kplscYRvzDrF4vQ_EC1g69tn7k1kdQvkCqTO8WPcldgY567a1TRfdo6aLSrR0lO5FGJiw9qxqvsn2ZkYtDyP4f-osY9uiqr7lpogvbZ_Mi_v-RL75uugkZEI88CMpxzID5bfg76v2GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قهرمان جام جهانی قربانی قوانین ضدایرانی آمریکا
🔹
خوان کاپدویلا، مدافع چپ سابق تیم ملی اسپانیا و یکی از اعضای نسل طلایی این کشور، در آستانه فینال جام جهانی ۲۰۲۶ با مشکلی غیرمنتظره روبه‌رو شده. مشکلی که ریشه آن به سفری ۱۰ سال قبل به ایران بازمی‌گردد.
🔹
قهرمان جام جهانی ۲۰۱۰ که قصد داشت همراه خانواده‌اش برای تماشای دیدار فینال میان اسپانیا و آرژانتین راهی آمریکا شود، اعلام کرد مجوز سفر الکترونیکی (ESTA) او از سوی مقامات آمریکایی رد شده است.
🔹
این ستاره سابق فوتبال اسپانیا در گفت‌وگو با رسانه‌های کشورش توضیح داد که علت رد شدن درخواستش، سفر او به ایران در سال ۲۰۱۶ برای حضور در تیم ستارگان لالیگا مقابل ستارگان فوتبال ایران بوده است.
🔹
ماجرای کاپدویلا در حالی خبرساز شده که در هفته‌های اخیر موضوع محدودیت‌های ورود به آمریکا بار دیگر در حاشیه جام جهانی مطرح شده است؛ از مشکلات صدور ویزا برای برخی اعضای تیم‌های ملی گرفته تا انتقادهایی که نسبت به سخت‌گیری‌های مهاجرتی مطرح شده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/450855" target="_blank">📅 13:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450854">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‌
🔴
کویت مدعی شد در جریان حملات موشکی به این کشور، یک نیروگاه و تأسیسات آب شیرین‌کن به‌شدت آسیب دیده است.  @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/450854" target="_blank">📅 13:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450853">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اختلال در آب‌رسانی ۲۰ روستای جاسک به‌دلیل حملات آمریکا
🔹
آبفای هرمزگان: درپی حملهٔ دیشب ارتش تروریستی آمریکا به آب‌شیرین‌کن بونجی، تامین آب آشامیدنی ۲۰ روستای جاسک با جمعیتی حدود ۱۰ هزار نفر با اختلال کامل مواجه شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/450853" target="_blank">📅 13:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450852">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
برخی منابع خبری از شنیده‌شدن صدای انفجار در کویت و اردن خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/450852" target="_blank">📅 13:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450851">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
برخی منابع خبری از شنیده‌شدن صدای انفجار در کویت و اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/450851" target="_blank">📅 13:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450850">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">امتحانات دانشگاه‌‌های ۳ استان جنوبی مجازی شد
🔹
وزارت علوم: امتحانات دانشگاه‌های ۳ استان هرمزگان، بوشهر و نوار جنوبی سیستان‌وبلوچستان به‌صورت مجازی برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/450850" target="_blank">📅 13:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450849">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شهادت یک مامور انتظامی کهگیلویه‌وبویراحمد در درگیری با افراد مسلح
🔹
معاون اجتماعی فرماندهی انتظامی کهگیلویه‌وبویراحمد: درپی درگیری ماموران پاسگاه دمچنار با دارندگان سلاح غیرمجاز در منطقهٔ عشایری زنگوا، ستوان‌یکم رحمت‌اله سجادی‌مهر به‌شهادت رسید.
🔹
در این راستا ۲ نفر دستگیر شدند و عملیات برای شناسایی سایر عوامل این حادثه همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/450849" target="_blank">📅 13:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450848">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انهدام مهمات عمل‌نکرده در پاکدشت
🔹
سپاه تهران: به‌دلیل انهدام مهمات عمل‌نکردهٔ دشمن در پاکدشت، احتمال شنیدن صدای انفجار ناشی از این عملیات تا ساعت ۱۵ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/450848" target="_blank">📅 13:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450847">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkvBlWNggjYBYm4LDKFK89FEPS6liOwxjoQUSOqccHxdxH0PZIVcl9iRajihYVAqOsb8ppuUtroRun53m5AuzorIYi1ME6BtWSN8NVFC5OFins-3-onQ4e7JY94pOHtvvgg7u4o9s45q16_BWpkbCRgqVNNg4z3PM_qU0-V3ElkAo27In6c6-r5HEG69cKMmQC2coPTlGFoIFLlvxazkNK1PSW5cVvT0VRhojOd90dinRVkNNAyxfAC1IVQ3SH8YjZxuTWRbna09OnvgPYEMpoFugP1Xd4KGoo6PcNWxNtmap-gwju0JF4r_XDk3-qYhBikoq6Sf6T55F407JcgWdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با ریزش ۱۱۷ هزار واحدی به ۴ میلیون و ۷۷۷ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/450847" target="_blank">📅 12:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450846">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2OvBxEx2f9NEBN3sJ3ZS7kRDexjkHWhtUPzQQmwPx3JVNmQ0PYyroPBD2SuXhgz6eXDsI3VDE3lakipGqQeASgrenNMxP8-CgJm2MlJAKjguOAi-YzkJ8twODblx6ddo_Ijbj-_3DjJCXYAUVmHGq9MwgMCReJ5f-viBqeskoSCid3sAQj17_oQ-G6utfpn91NnXVH1OCmBDs5rEB6ywcZ0-eWPdqRRsJ4KFSnbH4T1E4FyTXzKeUYmFM-yMkBf6kiNKl7pq90YMTm1bWSXUrdPyJ7SkAQrEGtadDQQc8-0pvkbyR9Ky7eoZIohqCUG7l9PcCJJ5yvehlXSrXxpVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدوس برای پرسپولیسی شدن رقم بالایی می‌خواهد
⚽️
پرسپولیس برای تقویت ترکیب تیم، جذب سامان قدوس را دنبال می‌کند. مدیران باشگاه نیز مذاکرات اولیه را برای بررسی شرایط این انتقال انجام داده‌اند.
⚽️
یکی از موانع اصلی برای انتقال، رقم بالای مطالبات مالی سامان است. گفته می‌شود دستمزد درخواستی قدوس نسبتاً بالاست و همین موضوع می‌تواند ادامۀ مذاکرات را با چالش جدی روبه‌رو کرده و حتی باعث شود مدیران پرسپولیس از جذب این ملی‌پوش صرف‌نظر کنند.
⚽️
هنوز تصمیم نهایی گرفته نشده و سرنوشت انتقال به روند مذاکرات روزهای آینده و احتمال نزدیک شدن دیدگاه‌های مالی دو طرف بستگی خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/450846" target="_blank">📅 12:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450845">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8LkYiNzL-eDqLaKWC7mLS1M-SZb3NlWssy-eFv0rMkFDqYzjERVaRBzqU8Gim2ssE7d2yKVRwBz42_e8Tx_WQEBBK3VyU6G0RgowsTD-4oRHSBXg2ie4vZoU-ylccor6GbCjsQdc0L0ztOULHTlbQZhpnm4oQ6GdcalH-PYtTYLxLcmQHbMxPXdJGuUppNOSvUXrPjfZtPuLt6wa2eeFfBOl9rkTJn17_jPpkxB60Na2DrwsqJxYDjVdfmIdN3sOUHuj2FW_Rs_Zy80xFmy5a19MmNkzldSjxvzZGLgH4yVu3cZDgAMLVvNpyy5pqOBwKNuhI0uzZi_GwuKMAleOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلال تمامی بانک‌ها برطرف شد
🔹
داده‌های اتاق مانیتورینگ شبکۀ بانکی نشان می‌دهد تمامی بانک‌ها از جمله ملی، صادرات و تجارت به چرخۀ خدمات‌دهی بازگشته‌اند و وضعیت ارائۀ خدمات بانکی از صبح امروز پایدار بوده است.
🔹
طبق داده‌ها در نمودار مربوط به بانک ملی به‌صورت…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/450845" target="_blank">📅 12:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450844">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KL76porOXQpjhquHhbCbjTqJeofI9T4MjsO8T5sWri75tyxaQB9V0CING2dXXx8qL2bZi6Booem4PFThj4fNNawSNFXeIbkRyzvw16F7SwEnj54yeF7dA3VnouheaISzJclc3WpHXXTofcobjVfA1Ct25hG4UWCJHVEtxBM7Woma-E6c82b--6C-GOLAVFEXwHWQYDhWNeCwRP32yzXqea_ZxCN3b8MuuFBnJ_j9-jrsK2B4ywcwiCT1c6IvoGMUHh-tm74wFglh9fRpqSnEgtkiYtB4gmnA-8ol1kuWM0830sN8xS5h8URL4kXpA27nBaNEK-gan0CvJ-lAUqVRTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی قوه‌قضائیه: بیش از ۲۴۰۰ گزارش تخلف اقتصادی در شرایط جنگی ثبت شده
🔹
براساس گزارش دادستانی کل کشور تاکنون ۲۴۱۶ گزارش تخلفات اقتصادی ثبت شده که از این تعداد، ۴۴۷ پرونده برای رسیدگی به دادسراها ارجاع شده و ۱۹۲۳ پرونده هم به سازمان تعزیرات حکومتی ارسال شده است.
🔹
پرونده‌های ارجاع‌شده در دادسراها و سازمان تعزیرات حکومتی در حال رسیدگی است و پس‌از مشخص‌شدن نتایج و میزان محکومیت‌ها، جزئیات آن در نشست‌های آینده به‌اطلاع مردم خواهد رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/450844" target="_blank">📅 12:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450843">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f470048b5.mp4?token=ic3rkNatD-cT4K83IwZYoqzXrI5hCEfCBZWP5BIU5lv557SlixMCeYZ0Sri0ZzotzT7WNgptYXq0aEbyh6vFGUqkvywwdV7uAty7uN6DXR9UhaNlWrH-uJChuhQvC5IcGF30VewAMbMro7F8K7JNV6mvENbaRkb7_9WFhh600OUxphqn4iizLXg0XXhGt-LiVGM01QiTsWIRJckehXyd7k_3D0zF2ntsmgaatAsxvdq2WyvuhRl0u4SC-BY5aplqfyc89b5mb0SnjZ14zcknFi1PHHhshUFcSRk3o0oGIcM362no3gyndmlfLSxDiIh8m6Dn8LLeBkxZTHJSTboHLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f470048b5.mp4?token=ic3rkNatD-cT4K83IwZYoqzXrI5hCEfCBZWP5BIU5lv557SlixMCeYZ0Sri0ZzotzT7WNgptYXq0aEbyh6vFGUqkvywwdV7uAty7uN6DXR9UhaNlWrH-uJChuhQvC5IcGF30VewAMbMro7F8K7JNV6mvENbaRkb7_9WFhh600OUxphqn4iizLXg0XXhGt-LiVGM01QiTsWIRJckehXyd7k_3D0zF2ntsmgaatAsxvdq2WyvuhRl0u4SC-BY5aplqfyc89b5mb0SnjZ14zcknFi1PHHhshUFcSRk3o0oGIcM362no3gyndmlfLSxDiIh8m6Dn8LLeBkxZTHJSTboHLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عبدی و روزنامه اعتماد مجرم شناخته شدند
🔹
سخنگوی دادگاه مطبوعات: هیئت منصفه دادگاه‌های سیاسی و مطبوعاتی با اکثریت آرا عباس عبدی و روزنامه اعتماد را مجرم شناخت و آنان را مستحق تخفیف در مجازات ندانست.
🔸
پیش‌ازاین، دادستانی تهران با استناد به محتوای یادداشت…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/450843" target="_blank">📅 12:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450842">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مصادرهٔ ۳ همت از اموال قاچاقچیان مواد مخدر در گلستان
🔹
دادستان گلستان: حکم مصادرهٔ ۶۳ ملک متعلق به قاچاقچیان مواد مخدر به‌ارزش بیش‌از ۳ همت صادر شد.
🔹
همچنین اموال دیگری از جمله خودرو، طلا، واحدهای مسکونی و تجاری و حدود ۷۰ هکتار زمین کشاورزی نیز در پرونده‌های مرتبط شناسایی شده‌ و در مراحل رسیدگی قضایی قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/450842" target="_blank">📅 12:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450835">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gbp51FVG7wASvqfRVc4mcxLNa5AycxdE3YYo8rLSEt7Me4ZEDUNAPoVGHKVDWpsRcg9PX09eRru38xiSOnE8upEdZwXrnsToDaebebh9HSz3VusbSSN1gxeT0VAejPw8NebbicNrAJdTVWTWdqMmbZCSDh8isXkhICJa4GcxaVR81haJOVWeHx3D8E7Yv9ErxsANid4HsWuj2P3asHHzEWpcKg1zZvUQoOtNiwQY02e2vh9cacdxSSLu1-gKnFIakeIna6VxpYJmtFfWaJlaKgfUZPBfDkd5MC7QsdRzi_tZALLP4tqHQjB6zaurixNnNvTtlmsinRO6pPR48e1pAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NnIv_jf7s1ULsRwHC-TOHqP7OiyJSvBWawn29jUW_tPDBsj4mjvqTJcKR_MNVe5wwF6o8CuBTvEAVHEIrhlmOQbJz6dxGGVdS7L_d8nJ6PAct00Qjt8ysAVOZMaI5aXnx3uGvQjHhiYuNTRnkCa6KgBvOEimRu96AMle0eJztBUCDqXTOzMMVzkrJvVCEHVinR2uq6o8nW3jZWq5eBFLsU0Pg2a2EgWQCjQMWgCGKgXQeSYJldisFECGalRgMcbOYoxKPCgTA9-zpQfOEy_5EHagZ86mYSbqhN3eX4hNzFPfMW_CbCdlPfRpZ-pFQo30A2puAt9RI4hRRJ7SK3dUoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQdBfwvZxuTCXr-hiyLLBVN_k6gvWw6KdhHZPRSYNIRuOc9EtzIasIsnhvNcbIdJeYtHThRFMzzJG0RSVmgc7kgGPDnyh-ecUnEjJckRByG24WBraYgz0VQ0WNez4N54gHkhBpXJOiSuEso7mxGwgo7XwwM5knH1cfAeB3wqofusMd0EMqZK0uSryxRhUqUiqEBdhMZknQTJGCqohJPdP8JP8xpWXJ98o4pttE9qV_LiU5tZbUG4WJFmaoED5ZgDb02SeRsTsuH80TsRVmtnIT_4b8Us6y8lH3VM9MojOR757aYdqCQIEIYjuBBfbostsgdOQdhthvUWzE365OSlUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/klyEpylQLvNR0O9H_YgIEmxhwV5l4Q190QFiAROk6OZ4RgDudWCD_atlC1Ys3BKjpdeHFiiPGHd2iNx4MJBmCLXNqbZz76xtjgdGqyxVQYXCaK3etGnZGSAWw4dm1UAMb9KvS2sA53bsdIPO8BNjFDlHD4WIBlCBU1whTqeVljKKym8ZGGX0l8c-jHhgAHKfFZVe3eQOf9hvErOAEoSKpwg_wY-vp6EE9o-hFi70_nKtoadxeE6ljvDqcmCuiskNilc18f895cUCP4rTGVsXr93LA5nv6mmq-TJ0jkxIhjHRpkuPdTeOy-V36OPpUX4MUFaR7XifoN9lELzsSOiCvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BF9hma0qGBGj33BMpRmT44DzeMhHJcasZHW9_zooPie3kA85Xd2clrZR-AVhZw9WxXKu6ZIWKSMvTq4CmbCmBrzS5o6px3Nkmgx5eq3Iiu_kKSpQOfUO3Ohe8hfUNHefULRUqLYlsB0RAZwk4hdXSV9OrZT4AQN1eaivo3ws-66qeNFv_i1B2IHOE9X3fsm3BZiZzGmgkLyEazqE9_IkT8NHztj2pm3AHKpxw-CFuY1Yjh3rcMh-G-WXxudElhCwq3k8sfzV_W-xGbbxsf7TG_m0g3VjmvYlcGf_h7RDXUSpcpVVhvFYYHtP_FY2b6YJ9xnIZNdcq3ouqRyKfPyPZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oW8isozASiDz-rKyRvEZdKqj2EZtdLwbHSHUr1iarRML_eMJV5afQVG-OpQcQF6GFs99MOv2qLc445z3zFB59bFaKNne7NrAerUfHeoS0idClPXbtcHZDKRBeDxJhP5gBZk1T9z8Mla6VCxCDTKaM33K3etGc0QekugzyUg5Sdsy6TJbZlCVLhnh3ESD0ElAu17LF9keuYjSgMU_55DG3vfg8c-1CbkiH9vXy6eacZarB9nWNtcXNZxaL8M4QadF19VpRZQZ3Xg0axdRa3y5OdUHwbJCqaICWiVQ72aD4Y_mvLHeludrBhWy_HQM1k5AJHbeeZeCfd4rtls7RIUbWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ni71K4TpfII45QJCSjuwmPIBdb9LbxdjFRB954c5opB1TDDq1E0Sz-E7wbDajYdpmF5y7Nws0TBcGkwxo3UUF_jqVb25xLv5WHHBDw__L5SgE9y0UyXgXDQuw4r8UOEThdknDIdoUK7Vxo41LtD2O3wKBSMojknhLkcpBUYPc0xCXPJcYX4Udloh_BhkalOHj_UwzDcV0R4DFyJgNRtxZ3pP30nbm5EUj8fXUfRK-1_pLnHrO6J7Qhv5A6q-tA0-DSTwf5dhL8mGq_ofKsD9BqHqaV_wQ3Yj2b8e9dGkctfKVVF1dsxfFfLDudvitU3WWGstCxB56d5whiz_JgQ2Iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تنگهٔ هرمز؛ میراث ایرانیان
عکس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/450835" target="_blank">📅 12:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450834">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
حملۀ دشمن آمریکایی به انشعاب راه‌آهن بندرعباس
🔹
استانداری هرمزگان: حوالی ساعت ۲۴ ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی مورد هدف قرار گرفته است که متأسفانه در این حادثه ۲ نفر از هموطنانمان مصدوم و به مراکز درمانی اعزام شده‌اند.
🔹
این ایستگاه…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/450834" target="_blank">📅 12:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450833">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa2574dccf.mp4?token=NasgGxlvHMlXo0cEjM6aPfAuOZcSzb0DSYVFDI12hip-pmmnXJxh9VLPqQUhh8EHzXilY0NqesdYgYRBnd4YMoQVh1D-hYkKI2lumpq3f81o0l0MqH0OBlDrcNRiEIWsEAgCiD1PpJyRVLOgIxNW8TlfcIH6Y--S0n_BCVZguQLjHCFyFevxtrh2Etoczzf2rvF9YV2JTwO2d9wNnkDGyLmByxnxMXXHKq_Eu0ZUd6VKjhzkVYGXLlqpJTdUBX_0K7OPVTXsU0yjPbdeLr-tK1ABwI8098VNL_SLhnjQIwZ8dYXWcaDQvwgBDaab1XZ7BIYf3M0NO3ZH-dUd_D5qGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa2574dccf.mp4?token=NasgGxlvHMlXo0cEjM6aPfAuOZcSzb0DSYVFDI12hip-pmmnXJxh9VLPqQUhh8EHzXilY0NqesdYgYRBnd4YMoQVh1D-hYkKI2lumpq3f81o0l0MqH0OBlDrcNRiEIWsEAgCiD1PpJyRVLOgIxNW8TlfcIH6Y--S0n_BCVZguQLjHCFyFevxtrh2Etoczzf2rvF9YV2JTwO2d9wNnkDGyLmByxnxMXXHKq_Eu0ZUd6VKjhzkVYGXLlqpJTdUBX_0K7OPVTXsU0yjPbdeLr-tK1ABwI8098VNL_SLhnjQIwZ8dYXWcaDQvwgBDaab1XZ7BIYf3M0NO3ZH-dUd_D5qGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: برای مزدورانی که با دشمن همکاری کردند و خواستار حمله به ایران شدند، پرونده تشکیل داده‌ایم
🔹
این عوامل شبکه‌های ترور راه‌اندازی کردند و به‌دنبال بمب‌گذاری بودند؛ اتهام آن‌ها در جنگ‌های ۱۲ روزه و رمضان، «همکاری با دولت‌های متخاصم»، «اقدام…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/450833" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450832">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0SI0U2J-IQdwzKesJyQCdZfIoauCaPhK53VpbUU8SKRyClWccieejoUCsM_MEHLK7oTpkhefTSZVf2eR4-lB-jWfyjD1LtjCKoh8j_M16djZP2s08j8oh9ltn3QoOsJw6VMpmQ05jRza8L5skbgMNakR-7sYa0wv5P0vtiNyU9Wmnudb2PTwGMjxWOk7OHnSsM3oPMq5K_qagrNp7r0xy5PmEk3473mbFgcnCxwEbBg4iyZhQg187OLe9CYDanvysyBGv23JHZR9Kkah6tJu6J5Mjb2i5vvQ4Omiw61bVOp-hDHgHaMFaQPfH00aA6OxV53gAuNqf-TYd38KJPJgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدارهای امنیتی آمریکا به اسرائیل رسید
🔹
پس از هشدار وزارت خارجه آمریکا درباره سفر آمریکایی‌ها به غرب آسیا، سفارت واشنگتن در تل‌آویو هم درباره احتمال «تنش‌های پیش‌بینی نشده»، هشدار امنیتی صادر کرد.
🔹
سفارت واشنگتن در تل‌آویو اعلام کرد: «ما به آمریکایی‌های ساکن منطقه یادآوری می‌کنیم که همچنان باید احتیاط کنند و آنها را تشویق می‌کنیم که اخبار مربوط به تحولات فوری را دنبال کنند.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/450832" target="_blank">📅 11:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450831">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15960123c.mp4?token=NmKHkgM_iMLhtBX0imO2D__hr6tdGo6LbrAvz8AY3UJm0K2HkZB5RZRB_ijYTcx8AXX2PquiAWMLbK26lPkll-iZkJSl-6qfFXyv_4m7KHzKQ-aC8o15U6W4v0guP1h_K2eC_uLc1F3Tjl1swdFFUj0a2aPXXElr6Lscfh6krkRiTMIty5RZj75txa7a4YYXLBYU3OXyh6RBERpZxUloO4RNH7fTPXGwDGP4YPpDqN4akSVSFAxYvQshW93CuSZ7YTSqwfXSPUzZWI1y_uu6DKVS5oayHJ6ZZH0XNQN4aSgED_Lg8nSWHm7NV5XQl_w4EGUMyoRlwguX66mSsxyMpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15960123c.mp4?token=NmKHkgM_iMLhtBX0imO2D__hr6tdGo6LbrAvz8AY3UJm0K2HkZB5RZRB_ijYTcx8AXX2PquiAWMLbK26lPkll-iZkJSl-6qfFXyv_4m7KHzKQ-aC8o15U6W4v0guP1h_K2eC_uLc1F3Tjl1swdFFUj0a2aPXXElr6Lscfh6krkRiTMIty5RZj75txa7a4YYXLBYU3OXyh6RBERpZxUloO4RNH7fTPXGwDGP4YPpDqN4akSVSFAxYvQshW93CuSZ7YTSqwfXSPUzZWI1y_uu6DKVS5oayHJ6ZZH0XNQN4aSgED_Lg8nSWHm7NV5XQl_w4EGUMyoRlwguX66mSsxyMpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
پروندهٔ رضا پهلوی، فرزند شاه مخلوع به دادگاه ارسال شد
🔹
دادستان تهران: پس‌از تکمیل تحقیقات، دریافت گزارش‌های مراجع ذی‌صلاح، جمع‌آوری مستندات و انجام اقدامات قانونی، کیفرخواست پروندهٔ رضا پهلوی مطابق قانون صادر و پرونده برای رسیدگی به دادگاه صالح ارسال…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/450831" target="_blank">📅 11:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450829">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/303c1c6f25.mp4?token=O2uUpeMVC11VxcaCiZjqDxDgBSYXAjZs3fUiuz9AIMui0xfdaBJ_bW2Gn4YZwR7plZpw6bvlH5kHiDkZZ7QyDF5uGYdqMQxYNaOrqH_VTOgbvNQVX1azuIdTsdCehAYSlSV93Tsk8ssctQPfrUQsMXGC0TjegB9OL83-SMCkl5MgwiNNcz69v9yzu1qMbPqVTNdvg7RHfv44rjZPLeS31yITK1W__4t29BuNbWEc0vT2K0hOf4VolPlXQ3AvkanMsNHuAnZ13lzqsM4s0Eb6GkCjnAXMGVntj0MhjX8sJSPd-B3Y0F8mtNgIemXv52ykvAtEQUavfGA7msLBJgCNXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/303c1c6f25.mp4?token=O2uUpeMVC11VxcaCiZjqDxDgBSYXAjZs3fUiuz9AIMui0xfdaBJ_bW2Gn4YZwR7plZpw6bvlH5kHiDkZZ7QyDF5uGYdqMQxYNaOrqH_VTOgbvNQVX1azuIdTsdCehAYSlSV93Tsk8ssctQPfrUQsMXGC0TjegB9OL83-SMCkl5MgwiNNcz69v9yzu1qMbPqVTNdvg7RHfv44rjZPLeS31yITK1W__4t29BuNbWEc0vT2K0hOf4VolPlXQ3AvkanMsNHuAnZ13lzqsM4s0Eb6GkCjnAXMGVntj0MhjX8sJSPd-B3Y0F8mtNgIemXv52ykvAtEQUavfGA7msLBJgCNXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملۀ دشمن به ۳ پل و تونل دیگر در هرمزگان
🔹
استانداری هرمزگان: تونل شهید میرزایی در مسیر رفت و برگشت به دلیل حملات دشمن مسدود است.
🔹
پل رودخانۀ شور هم در مسیر بندرعباس به سیرجان مورد حمله هوایی دشمن آمریکا قرار گرفته است.
🔹
همچنین پل محور رفت سه راه‌میناب…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/450829" target="_blank">📅 11:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450828">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9179bbd562.mp4?token=XpEfaY61toLUvx2EMe6f9v1n6Wd-Kni01TSc8uB63Lce2A96e1SaKRlhjqG0DfIH4HzWbAYL2oSQc7jms-g25DzTMzhoIkx1gk8kFvtnEY6-odvmm2R-ur9ge5AHPukpX9m57fLMXapHGbtmz7N4aTXigH9IsNDl-0tdtn8lHus5IMBVrfvaU8zv7mq_efdzOhQJz-em4yD2-ZGdZEsm6L8L9s2MYcMmLksUdTWK_6ysN2gftXPV7-vR9qQpQT1BjjAGa4g6KwwuDMMILy4L3FUsAbec1ZJ17NZ3QXC7OhX8uOPVN8-jPxmXELiTtx8eAIWeE2xzf3Yj_S_kmudJuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9179bbd562.mp4?token=XpEfaY61toLUvx2EMe6f9v1n6Wd-Kni01TSc8uB63Lce2A96e1SaKRlhjqG0DfIH4HzWbAYL2oSQc7jms-g25DzTMzhoIkx1gk8kFvtnEY6-odvmm2R-ur9ge5AHPukpX9m57fLMXapHGbtmz7N4aTXigH9IsNDl-0tdtn8lHus5IMBVrfvaU8zv7mq_efdzOhQJz-em4yD2-ZGdZEsm6L8L9s2MYcMmLksUdTWK_6ysN2gftXPV7-vR9qQpQT1BjjAGa4g6KwwuDMMILy4L3FUsAbec1ZJ17NZ3QXC7OhX8uOPVN8-jPxmXELiTtx8eAIWeE2xzf3Yj_S_kmudJuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: تاکنون ۳۵۰ پروندهٔ حقوقی دربارهٔ جنگ ۱۲ روزه و جنگ رمضان علیه آمریکا و رژیم صهیونیستی ثبت شده
🔹
در جنگ ۱۲ روزه ۲۶۰ پروندهٔ حقوقی در شعبهٔ ۵۵ دادگاه حقوقی تهران علیه آمریکا و رژیم صهیونیستی ثبت شده که بیش از ۳۰۰ هزار خواهان دارد.
🔹
همچنین ۲۰۱ پروندهٔ کیفری در دادسرای امور بین‌الملل دربارهٔ جنگ ۱۲ روزه ثبت شده که ۱۳۷ پرونده با شکایت ۸۰۰ شهروند و ۶۵ پرونده مربوط به شکایت‌های ادارات و سازمان‌هاست.
🔹
در مورد جنگ رمضان هم تاکنون ۹۰ پرونده تشکیل شده است. مرکز وکلای قوه‌قضائیه هم مستنداتی را دربارهٔ خسارت‌ها جمع‌آوری کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/450828" target="_blank">📅 11:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450827">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdktHF2IPmJBerZCym0rM6B5r8ThOPeIi7-_P4tPU_qHq0ua3Fe2-TKwp8TxkPfhfCfGy3KeilMKALoqFo5viXlAmH6DOCX5vkjqpJwla7seAhnIaGgv-x21aRxCYpWYMfVjrvA5RsQ8MWZLxm8csb86tc01JTRNPIMjPZ05WPsNKmwpdySpj4iStfmOly-e7IPDdGkwSTOHjTgYstMQZ56g-a8J4uDuP_49hLCY0TWnq0d-DjgmKl0G_OJiSfth2myv0ajwuqjm1F7YqPM52qxuCukI7-8wwwMmI4T12yXGSFSKwJtse54Hsyvh1MfpzlvXdCVYGQ9T-B_F2qwQzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلافوئنته: یامال آمادۀ فینال است
⚽️
سرمربی اسپانیا: مسی بی‌همتاست؛ او یک استعداد فوق‌العاده و الگویی برای نسل‌های جوان است.
⚽️
اما لامین باید خودش باشد و بهترین کمکی که می‌توانیم به او بکنیم، این است که اجازه دهیم همان لامینی باشد که همه می‌شناسیم.
⚽️
…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/450827" target="_blank">📅 11:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450826">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d04de4038.mp4?token=rgOGopjhHSDgZSQ-L5K3KEZfVRCyP8wH_lk2OE78uCLRAnsPdmz3joBnUCES2Dza1ZF9QnJNXX-KG5TLOSkfZTgWHJF9el4KQDzdDVcKBtl03W4c7aKTRO9eMP0Mvn324gJHnLEUVSwCTtsKiG_drSnzuhLSjfgNFukaVixb2I86AD06G_j2g9RxJWz0jnGvWMLhWp1zMAxG10rntz1RIkq_yrcskIgPV0yuzkVWDLETQDoOnNhrL-nNzAcOTymz-BjidATuxZkymJyahpfXgrNIOT7yY4m4AjKkNOffrEKgm1vbRQIgQlEkbYnwgPGanrYF7YKkx-qYJlJI8dnfBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d04de4038.mp4?token=rgOGopjhHSDgZSQ-L5K3KEZfVRCyP8wH_lk2OE78uCLRAnsPdmz3joBnUCES2Dza1ZF9QnJNXX-KG5TLOSkfZTgWHJF9el4KQDzdDVcKBtl03W4c7aKTRO9eMP0Mvn324gJHnLEUVSwCTtsKiG_drSnzuhLSjfgNFukaVixb2I86AD06G_j2g9RxJWz0jnGvWMLhWp1zMAxG10rntz1RIkq_yrcskIgPV0yuzkVWDLETQDoOnNhrL-nNzAcOTymz-BjidATuxZkymJyahpfXgrNIOT7yY4m4AjKkNOffrEKgm1vbRQIgQlEkbYnwgPGanrYF7YKkx-qYJlJI8dnfBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملۀ دشمن به ۳ پل و تونل دیگر در هرمزگان
🔹
استانداری هرمزگان: تونل شهید میرزایی در مسیر رفت و برگشت به دلیل حملات دشمن مسدود است.
🔹
پل رودخانۀ شور هم در مسیر بندرعباس به سیرجان مورد حمله هوایی دشمن آمریکا قرار گرفته است.
🔹
همچنین پل محور رفت سه راه‌میناب…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/450826" target="_blank">📅 11:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450825">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‌‌
🔴
سی‌بی‌اس: مقامات آمریکایی اعلام کردند که ایران در این هفته دست‌کم ۲ پایگاه در اردن را هدف قرار داده و چندین نفر از نیروهای نظامی آمریکا مجروح شده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/450825" target="_blank">📅 11:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450824">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iq5SPEKHoGkN6hox6A2yYdigkchMS7OgbTovYikZIAohkMB-lsKUUkkDYgwi8Bwy6ULBuusif_Ztq3IKegTGv8mcnrUK-NvV5MYRBCBQ18I21kVFDWkl9R2Da_PZMIaGWFoLhNE4hulgbr6fcPnmm2yE6PiJvlDL3OocNhs6_eax4BnpEIr88Zb3B2C4AhyFflou_z-6-U4mBh4TLDXRJ09BHgPW3Tm90ZvipcoeXFyIqOgsDyWuMXqArlVPzOl9_XGXIRHTZdOeI9nC2Zj4Y8IeVfe92zVZ7Zmwo9KtscWWNxz-FJC7UVUBbSWyCTjCh2-1jT1ssmG9Xo43PrPV4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تأسیسات برق و پمپ‌های آب‌شیرین‌کن اسکلۀ روستای بونجی هدف حملات موشکی قرار گرفت
🔹
معاون استاندار هرمزگان: در تداوم حملات دشمن جنایتکار آمریکایی به نقاط مختلف هرمزگان، این‌بار تأسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکلۀ روستای بونجی از توابع شهرستان جاسک…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/450824" target="_blank">📅 11:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450823">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b936586a88.mp4?token=iHt7vuEuPQRbHuXrHoCDZlAEJfKBAgSmf0t2COR_TRsWeWYeqm3ZfFyCMaPAmo0fx8uBijMk8ht9nEYwkuxkcAgHNWzKO-hORGuJqVOwhZnjFl4va70WMip4lj2bdiY7UF3cKt4mdiJipL6ZZYKVJcM7mxZsVfaBaBYSynlmjPlU--ZEVwLCOosT_MImKs4AUZKw40o_sLaAvGfaKeDdiDeCbZ9lZ2yHe5xRroDqb92Gt-CI0h5eycc9Q9BF3MSGUtuaRyU2XCkiDLEaef144S03G22x2NU_Oa2v528N5ObxhAOJzIkEaj_T2iULcYkFp9KJ_SHMD3IGtDN8xgCUiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b936586a88.mp4?token=iHt7vuEuPQRbHuXrHoCDZlAEJfKBAgSmf0t2COR_TRsWeWYeqm3ZfFyCMaPAmo0fx8uBijMk8ht9nEYwkuxkcAgHNWzKO-hORGuJqVOwhZnjFl4va70WMip4lj2bdiY7UF3cKt4mdiJipL6ZZYKVJcM7mxZsVfaBaBYSynlmjPlU--ZEVwLCOosT_MImKs4AUZKw40o_sLaAvGfaKeDdiDeCbZ9lZ2yHe5xRroDqb92Gt-CI0h5eycc9Q9BF3MSGUtuaRyU2XCkiDLEaef144S03G22x2NU_Oa2v528N5ObxhAOJzIkEaj_T2iULcYkFp9KJ_SHMD3IGtDN8xgCUiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
کویت مدعی شد در جریان حملات موشکی به این کشور، یک نیروگاه و تأسیسات آب شیرین‌کن به‌شدت آسیب دیده است.  @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/450823" target="_blank">📅 11:14 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
