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
<img src="https://cdn4.telesco.pe/file/CzkjVa6VyTe59Ds_gIgwgwN8Udr1tguE2C38FUVeLAl3eM77rBwC9jSvlSnBZeY21cj-jeKASVcd1wzT10UVHfw2dCSQSOgpTMIkqIUXjaZIemVAshxTJmn054mIuI9UJ4Qmq-Ru-jpZeW3r7oCo85M7liR0meUnNexH9ak2piffYKmn94OvX93Q3qaNkYlKVQpC0WiFA-AKmy6FhaDjDHnAfvR1Tjpn1Kne9qpZ1Lq4hDkwtKtKd2SqHtu5d9W7Fnm2PqBQ9y6qnHtr7kh0VAy3xWdVcuhRNAleDVWiu5MkW4yfjZ4Yl4d7ldSD8-C4vaH2AJZxVnj6GU25dz4P0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 928K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 19:02:49</div>
<hr>

<div class="tg-post" id="msg-146718">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
بلومبرگ به نقل از منابعی گزارش داد، از آنجایی که جنگ علیه ایران توانایی قطر را در تأمین گاز مشتریانش به شدت محدود کرده است، دوحه در حال مذاکره برای عقد قراردادهای بلندمدت خرید گاز طبیعی مایع از تأمین‌کنندگان آمریکایی است
🔴
طبق گزارش این رسانه آمریکایی، شرکت دولتی «قطر انرژی» به دریافت محموله از پایانه‌های صادراتی فعال و در حال ساخت آمریکا علاقه‌مند است
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/alonews/146718" target="_blank">📅 18:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146717">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8527590cc0.mp4?token=Gg1SmN-G_fHN-sDPwwyy6HXaxQEmkS3qria4vfGZ6g22feJ7DZ0J2g4xOci4bpzrBV5SqRln7bUro8SPbiQhv4Uk7MMazy6QCiriIEC0Vm0kAfKXu1g6qe_Odw-2t-wIysaN6SmYSt-LqYpbbnm6LmyXIkkl2snfM7rEwfTR5BnUVK-02VTKdx-fqHDUypajF34tfybmXXLjV0OTH-Tt0tMkwmqSJlMQQbg9sW4csCkJ4pmQg1LbSdEu1lth_Ilgfodc2O5FMcpk-jtTvzD1JuUOc8Nvv2aFiNP48oIxODm_3tkMZSUs0Yll8X_B6W7K02DCukd2r4klitU91Pk1JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8527590cc0.mp4?token=Gg1SmN-G_fHN-sDPwwyy6HXaxQEmkS3qria4vfGZ6g22feJ7DZ0J2g4xOci4bpzrBV5SqRln7bUro8SPbiQhv4Uk7MMazy6QCiriIEC0Vm0kAfKXu1g6qe_Odw-2t-wIysaN6SmYSt-LqYpbbnm6LmyXIkkl2snfM7rEwfTR5BnUVK-02VTKdx-fqHDUypajF34tfybmXXLjV0OTH-Tt0tMkwmqSJlMQQbg9sW4csCkJ4pmQg1LbSdEu1lth_Ilgfodc2O5FMcpk-jtTvzD1JuUOc8Nvv2aFiNP48oIxODm_3tkMZSUs0Yll8X_B6W7K02DCukd2r4klitU91Pk1JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هیلاری کلینتون: ما باید به خطرات بالقوه خود توجه کنیم، به ویژه به این که شی جین‌پینگ چه فکری می‌کند: می‌دانید، "آنها دیگر نمی‌توانند از کسی محافظت کنند، زیرا توانایی دفاع از خود را ندارند. شاید بتوانیم تایوان را وادار کنیم که به سادگی تسلیم شود، زیرا هیچ حمایتی وجود نخواهد داشت."
🔴
منظورم این است که اگر به نقشه جهان نگاه کنید، وضعیت برای ایالات متحده مناسب نیست، و من معتقدم که این تا حد زیادی به دلیل تصمیمات بسیار اشتباهی است که توسط این دولت گرفته می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/alonews/146717" target="_blank">📅 18:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146716">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
نماینده پاکستان: دیپلماسی و گفت‌وگو باید اصول راهنما برای حل موضوع هسته‌ای ایران باقی بماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/alonews/146716" target="_blank">📅 18:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146715">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
روسیه در شورای امنیت: اجازه بازگشت تحریم‌ها علیه ایران را نخواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/alonews/146715" target="_blank">📅 18:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146714">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e130fadb40.mp4?token=A6Va2rVY-_wYU1m3KU0hx99S4i38roG4RE4iRePLZDQq5vAGHcq8ZrdDhPXkXYWdm8DAbLfyJpf1NUTru2W06YIRCcl3fI5sgT9VF14BnaTC_UYIVfXPPiSK4fXoe8T_f_PlWG_8cMnYCilJCu7p8Mw-JjYh5e11tTEXM0WSDBxqtLBhlqzPhVkfFeWM0AlCE8Qe6lh6YCcBiodXMf7M3eeWZIqcFYLc_43xZ3CHwasZjIOxEQVycTrU3dCmv6oSrz2A6OfmFN8rpZEPhryVZPdhpha5T-VFAsuGBHz12Q3A5Nl8k7_W4Jp01eBJ5g3LbhqvGw_jjCitwTq30nWjVjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e130fadb40.mp4?token=A6Va2rVY-_wYU1m3KU0hx99S4i38roG4RE4iRePLZDQq5vAGHcq8ZrdDhPXkXYWdm8DAbLfyJpf1NUTru2W06YIRCcl3fI5sgT9VF14BnaTC_UYIVfXPPiSK4fXoe8T_f_PlWG_8cMnYCilJCu7p8Mw-JjYh5e11tTEXM0WSDBxqtLBhlqzPhVkfFeWM0AlCE8Qe6lh6YCcBiodXMf7M3eeWZIqcFYLc_43xZ3CHwasZjIOxEQVycTrU3dCmv6oSrz2A6OfmFN8rpZEPhryVZPdhpha5T-VFAsuGBHz12Q3A5Nl8k7_W4Jp01eBJ5g3LbhqvGw_jjCitwTq30nWjVjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای ائتلاف "جنوب غول" همچنان دسترسی به شهر عدن را مسدود کرده‌اند و نیروهای مورد حمایت عربستان سعودی را در جاده‌ها به دام انداخته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/146714" target="_blank">📅 18:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146713">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
الحدث: روسیه و چین مخالفت خود را با بررسی تحریم‌های ایران در شورای امنیت اعلام کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/146713" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146712">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
دبیرکل ناتو: مین‌روبی در تنگۀ هرمز به ما مربوط نمی‌شود
🔴
موضوع مین‌روبی در تنگه به قلمروی ناتو مربوط نمی‌شود. البته ما آنچه درحال وقوع است را زیر نظر داریم و کشورهای عضو ناتو از نزدیک با یکدیگر هماهنگ هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/146712" target="_blank">📅 18:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146711">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
تسنیم: تنگه باب‌المندب به تسخیر رزمندگان یمن درآمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/146711" target="_blank">📅 18:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146710">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
نماینده بریتانیا در شورای امنیت: برنامه هسته‌ای ایران منبع نگرانی و تهدیدی برای امنیت بین‌المللی است. ایران تشدید تنش را انتخاب کرده، برنامه هسته‌ای خود را گسترش داده و بیش از 400 کیلوگرم اورانیوم در اختیار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/146710" target="_blank">📅 18:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146709">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npKPVLgZVbplRBqOP4-1yaXM0q20_c7MkD4_vHT07sEyK6A4wTV0Xmxic_R3frC25ptNoee5gdbmVBmHrnE8v13ODXR4mCGKGmNbn-8EI8FXf6q98HSeKlk7UEOTSa_JXPGylYghBPTIVdEfKF8Nm4F3weSeGIzFml9PMioHcsu4gAAleNAuDe7o2h6A9sv9p9te5eV3-IKAQY60FB9SNit051VoVCxPql4qn1E6Z4KlzbryYwsHqI_7mndcpX7n8n1lu50QXkflNz0-8Jrqz-Na4BJRDv52pdmN_f71TP1vw_Ue7CyIKaMf9xA4QOKUTg6TlDbfdIxw36z0pTCnzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جدیدترین تصویر از جنتی که امروز منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/146709" target="_blank">📅 18:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146708">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
نماینده بریتانیا در شورای امنیت: ایران با آژانس بین‌المللی انرژی اتمی همکاری نکرده است.
🔴
نماینده یونان در شوراى امنيت: از ایران می‌خواهیم در مورد برنامه هسته‌ای خود با آژانس بین‌المللی انرژی اتمی همکاری کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/146708" target="_blank">📅 18:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146707">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d44c8477f.mp4?token=aIbl8f18I0HtWSOhnFR_M33N-vq87xTrACcd3BKJGC9bTGHJmOt7JKmJv9etTbfCGX4h4Pw4EMrS2Osq2Q9JcSVOKAf9FRf1cSKY0wIi-4-FNLsDBtFymACH02rdY3Cm8L7dGGQxrdJD7tKjpsdUXZM0jIkQAnnhQVpumQTXgpY-ZE-oziABnXM-UU49UYxM37ZUabr952qO5RkIA6z2H9dx5HEiS5KJHLKq2uUsphTgbhbDop3ceDtpjotZVLxjkegNRsIhOF4g8UCvQUnjL0NfJW7DDE-Fpp1wYzjYFeJYipRk1PDkFoE0QUl_7atDJ6Fq9wH_loWcJY1Ntbm1fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d44c8477f.mp4?token=aIbl8f18I0HtWSOhnFR_M33N-vq87xTrACcd3BKJGC9bTGHJmOt7JKmJv9etTbfCGX4h4Pw4EMrS2Osq2Q9JcSVOKAf9FRf1cSKY0wIi-4-FNLsDBtFymACH02rdY3Cm8L7dGGQxrdJD7tKjpsdUXZM0jIkQAnnhQVpumQTXgpY-ZE-oziABnXM-UU49UYxM37ZUabr952qO5RkIA6z2H9dx5HEiS5KJHLKq2uUsphTgbhbDop3ceDtpjotZVLxjkegNRsIhOF4g8UCvQUnjL0NfJW7DDE-Fpp1wYzjYFeJYipRk1PDkFoE0QUl_7atDJ6Fq9wH_loWcJY1Ntbm1fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده بحرین در نشست شورای امنیت سازمان ملل با موضوع ایران: حملات اخیر ایران به ما و کشورهای منطقه نشان‌دهنده عدم پایبندی این کشور به قوانین و حقوق بین‌الملل است و باید در برابر آن ایستاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/146707" target="_blank">📅 18:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146706">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f588e43d4.mp4?token=dPuCapazRLBDa0G48uysK3Op0tUB1Pd07olGh4HKECuG9NIAXVYG814QClpM4ON1Nbi-SxUeAlrUsjLlUURrDpHyOt18NtLIEGzmyFH71HYxS9vHihUN9uK56Z2gmxvjUnwATOxvl5AotmUEwx53rp2EGVuS63ghN2ATPKcZkZjxwBriaSbUF2msQ0iKm_A001_n8umzAJ_irbHbqzxrlcQew5gX9hTDhPFr8M6ueMBJhmxwUOHZWL5fU9G7usD7ne-_WMCELk5jgjcmk72sjwfo81rP6DCny0TaNAdQr_RAL2bBun_lc23BY-NMu4obmDD5AWFSV0llWqRl588waA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f588e43d4.mp4?token=dPuCapazRLBDa0G48uysK3Op0tUB1Pd07olGh4HKECuG9NIAXVYG814QClpM4ON1Nbi-SxUeAlrUsjLlUURrDpHyOt18NtLIEGzmyFH71HYxS9vHihUN9uK56Z2gmxvjUnwATOxvl5AotmUEwx53rp2EGVuS63ghN2ATPKcZkZjxwBriaSbUF2msQ0iKm_A001_n8umzAJ_irbHbqzxrlcQew5gX9hTDhPFr8M6ueMBJhmxwUOHZWL5fU9G7usD7ne-_WMCELk5jgjcmk72sjwfo81rP6DCny0TaNAdQr_RAL2bBun_lc23BY-NMu4obmDD5AWFSV0llWqRl588waA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تایید برنامه جلسه امروز شورای امنیت برای بررسی برنامه هسته ای ایران با وجود مخالفت چین و روسیه
🔴
11 تایید
🔴
2 مخالف (روسیه و چین)
🔴
2 ممتنع
🔴
این رای گیری صرفا برای تعیین برنامه امروز شورای امنیت و تایید بررسی برنامه هسته ای ایران صورت گرفت و رای به پیش نویس قطعنامه نبود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/146706" target="_blank">📅 18:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146705">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
نماینده آمریکا در نشست شورای امنیت سازمان ملل با موضوع ایران: ایالات متحده قویاً اظهارات چین و روسیه را رد می‌کند و از مواضع بریتانیا حمایت می‌کند.
🔴
سال گذشته این شورا تصمیم گرفت قطعنامه‌های تحریمی علیه ایران را بازگرداند و روند اجرای این تحریم‌ها را از…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/146705" target="_blank">📅 18:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146704">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20260b4433.mp4?token=BxBvna7PH0841GoT5zaT-75-IUgacBXOymFFZDWN9EfY5o6_aI3TilIjgtQp2NqQY83n8bMDRG35nF6A0ys68wrNYnk4lA05h0ffWlmHVG9z3IVK_WESjL_6X2e_qv11syuHAbYRxHM9HakpWb-4BHcDCVg_S9WU6qLTow21oZoSkr60eMRo_-cT1KvCZuMQH5dQ3Hz6CIXK4ptzmFFn9U1fNdkVZ_t6COnvwo55BkKhqdxf74FPtlzvsKMKdDcXtaCoB1_AbxgSr8moMpMDt5esj4chqdIM6ZQ41gx5bdWFOueAd0TSQs7Cucqj5VT3dBF6kEybMlcx-OlzQTYwkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20260b4433.mp4?token=BxBvna7PH0841GoT5zaT-75-IUgacBXOymFFZDWN9EfY5o6_aI3TilIjgtQp2NqQY83n8bMDRG35nF6A0ys68wrNYnk4lA05h0ffWlmHVG9z3IVK_WESjL_6X2e_qv11syuHAbYRxHM9HakpWb-4BHcDCVg_S9WU6qLTow21oZoSkr60eMRo_-cT1KvCZuMQH5dQ3Hz6CIXK4ptzmFFn9U1fNdkVZ_t6COnvwo55BkKhqdxf74FPtlzvsKMKdDcXtaCoB1_AbxgSr8moMpMDt5esj4chqdIM6ZQ41gx5bdWFOueAd0TSQs7Cucqj5VT3dBF6kEybMlcx-OlzQTYwkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده آمریکا در نشست شورای امنیت سازمان ملل با موضوع ایران: ایالات متحده قویاً اظهارات چین و روسیه را رد می‌کند و از مواضع بریتانیا حمایت می‌کند.
🔴
سال گذشته این شورا تصمیم گرفت قطعنامه‌های تحریمی علیه ایران را بازگرداند و روند اجرای این تحریم‌ها را از سر بگیرد.
🔴
امروز باید گزارش ۹۰ روزه ارائه شود، اما دولت ایران متأسفانه دسترسی‌ها به مناطق هسته‌ای را مسدود کرده است.
🔴
روسیه و چین می‌خواهند قطعنامه‌ها را نادیده بگیرند و با وتو کردن آنها از ایران دفاع کنند؛ آنها در حال نادیده گرفتن اصول بنیادی سازمان ملل هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/146704" target="_blank">📅 18:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146703">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7af20ea1.mp4?token=jZxD4Nh174yN5lMdM0oGYMOfUxap7zJR_LumSk_Z22JYoVrD5_FoTK7sKO4ErCnBIzN3I9pq9bBSu58yWS7rkjRJrAXrdfgqWZ0635QS9JDlY4nd4l2CFm0-DZLhjD0uQCYt0bNgtFpqEPMAKmsu3DFaVNyn88QpfyamBQqP3fU8kH5DCHiEJCedqfFRl8olQm3eGTZq3kTRZVL9qgcJYmgwyad_fqUEODpkV4K2KqjelEm9gcw6jeCrrhIx0GWjHsKz-oBlX6makb3AYk7ggngBYoR788NekjQNHoXNF5kKd1BWGGdh_kSeySmNcpYQuyIZ5IBjjbS_s5tM2Che5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7af20ea1.mp4?token=jZxD4Nh174yN5lMdM0oGYMOfUxap7zJR_LumSk_Z22JYoVrD5_FoTK7sKO4ErCnBIzN3I9pq9bBSu58yWS7rkjRJrAXrdfgqWZ0635QS9JDlY4nd4l2CFm0-DZLhjD0uQCYt0bNgtFpqEPMAKmsu3DFaVNyn88QpfyamBQqP3fU8kH5DCHiEJCedqfFRl8olQm3eGTZq3kTRZVL9qgcJYmgwyad_fqUEODpkV4K2KqjelEm9gcw6jeCrrhIx0GWjHsKz-oBlX6makb3AYk7ggngBYoR788NekjQNHoXNF5kKd1BWGGdh_kSeySmNcpYQuyIZ5IBjjbS_s5tM2Che5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هیلاری کلینتون درباره ایران
:
ما کسانی هستیم که ایران را تقویت می‌کنیم. آیا ما از آنچه در ۲۵ سال گذشته انجام داده‌ایم، هیچ چیز آموخته‌ایم؟
🔴
و من فکر می‌کنم ایران، نه فقط با تشویق بلکه با کمک هر دو چین و روسیه، بازی بسیار هوشمندانه‌ای برای کاهش توانایی ما در دفاع از خود و متحدانمان انجام می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/146703" target="_blank">📅 18:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146702">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
اسکات بسنت: ایران در حال حاضر به‌دلیل محاصره دونالد ترامپ و تحریم‌های فلج‌کننده خزانه داری آمریکا با پیامدهای سنگینی مواجه است
🔴
آمریکا کنترل کامل تنگه هرمز را در دست دارد، صادرات نفت ایران رو به کاهش است، صف‌های طولانی مقابل جایگاه‌های سوخت شکل گرفته و اوضاع هر روز بدتر می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/146702" target="_blank">📅 18:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146701">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
هم اکنون جلسه شورای امنیت سازمان ملل درباره برنامه هسته‌ای ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/146701" target="_blank">📅 17:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146700">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏
👈
طرق گزارش مسافران: فرودگاه‌های ترکیه پذیرش محموله و باری که مقصد نهایی‌اش ایران اعلام شده را متوقف کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/146700" target="_blank">📅 17:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146699">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
گروسی: نمی‌دانیم در کوه کلنگ چه می‌گذرد
🔴
مدیرکل آژانس بین‌المللی انرژی اتمی می‌گه از طریق تصاویر ماهواره‌ای فعالیت‌های هسته‌ای کوه کلنگ گزلا رو زیر نظر دارن، اما نمی‌دونن دقیقاً چه خبره.
🔴
از طریق تصاویر ماهواره‌ای فعالیت‌های هسته‌ای کوه کلنگ‌گزلا رو زیر نظر داریم ولی نمی‌دونیم چه چیزی داره رخ میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/146699" target="_blank">📅 17:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146698">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
فوری/بلومبرگ:
آژانس انرژی اتمی وجود فعالیت هسته ای در سایت کوه کلنگ ایران را تأیید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/146698" target="_blank">📅 17:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146697">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از منابع نظامی دولتی: حوثی‌های یمن به جزایر حنیش بزرگ و کوچک در دریای سرخ رسیده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/146697" target="_blank">📅 17:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146696">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
رئیس سابق سازمان جاسوسی بریتانیا:
فکر میکنم وضعیت کنونی با ایران چند ماه دیگر نیز ادامه یابد، اما فشارهای اقتصادی از مقطعی به بعد، آثار خود را بر ایران نشان خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/146696" target="_blank">📅 17:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146695">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
فرماندهی جبهه داخلی اسرائیل: از سال نو لذت ببرید، اما برای هرگونه تشدید ناگهانی و غیرمنتظره وضعیت، آماده بمانید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/146695" target="_blank">📅 16:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146694">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
در حال حاضر ۶ فروند هواپیمای سوخت‌رسان و یک فروند P-8A Poseidon در منطقه در حال پرواز هستند. شمار اعلام‌شده هواپیماهای سوخت‌رسان، شامل هواپیماهایی که در حال بازگشت از مأموریت‌های خود هستند نمی‌شود.
🔴
۵ فروند از هواپیماهای سوخت‌رسان متعلق به اسرائیل و یک فروند متعلق به قطر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146694" target="_blank">📅 16:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146693">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1738045bd1.mp4?token=hg7gjFxXLVdoriWXhV2_bMMQosGHhGPiMdOpSRVLfnJYFs_OLTXQudDJbmadQ59Jg_gczCCw54cLH-hXgY4tfZs3akKFQIlSr4OBLcXgeEp5S6Nk_rPYVTCoa612_dTqbe4NfbuS800znqrCM4VrdYBxVPoll3fyEaZIDpcNleNxs4jVsPh892eSpq8l3lyq0yqfdg2tquNnJj5ZCQyrJZF_MCLpdb-0L5qM_eiEmM1yupDz8PISJn5g1WdbyrxU27SScUHbjHHwYltqmkPxUftV40tScxKAegipvFE8i4sOFnUVGO5Rfs42_VLtohPMpX06wffQiu1sh4zaSXCzFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1738045bd1.mp4?token=hg7gjFxXLVdoriWXhV2_bMMQosGHhGPiMdOpSRVLfnJYFs_OLTXQudDJbmadQ59Jg_gczCCw54cLH-hXgY4tfZs3akKFQIlSr4OBLcXgeEp5S6Nk_rPYVTCoa612_dTqbe4NfbuS800znqrCM4VrdYBxVPoll3fyEaZIDpcNleNxs4jVsPh892eSpq8l3lyq0yqfdg2tquNnJj5ZCQyrJZF_MCLpdb-0L5qM_eiEmM1yupDz8PISJn5g1WdbyrxU27SScUHbjHHwYltqmkPxUftV40tScxKAegipvFE8i4sOFnUVGO5Rfs42_VLtohPMpX06wffQiu1sh4zaSXCzFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حوثی ها، پس از تصرف بندر المخا، تجهیزات نظامی متعلق به عربستان سعودی و امارات متحده عربی را به غنیمت گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146693" target="_blank">📅 16:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146692">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/69e8c3e218.mp4?token=Er1sJiesDujF7FT6HwzDl2YmB4z7iOHKpSBdd8Xz9mqbQjiCZEsuy5iI9UpnhZkpMie8m-h1TVlx8T9AZKm2d1M-g7-CgbK60yXDtjem6FHLchkM0NXGu3JQz9R7icaQu9_VA1fOHusKCBe2r7r8lMCdYR1rGfoESefV38hdQZV0qK1KL2-iSO3qXwpExNGrkFQi1aECjiU0eUIcEg4kU4MwosoTf4EASWXtO0HedAY8uBu69VYk1TBkrn9f7MU24N6y_SZICLOYZBuemjS1UXImRNREuWo5GANLDdZcLG_evgQqY5-7B2kmbu6_g-RXfV1cieqlZzxQRnu7L7bDQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/69e8c3e218.mp4?token=Er1sJiesDujF7FT6HwzDl2YmB4z7iOHKpSBdd8Xz9mqbQjiCZEsuy5iI9UpnhZkpMie8m-h1TVlx8T9AZKm2d1M-g7-CgbK60yXDtjem6FHLchkM0NXGu3JQz9R7icaQu9_VA1fOHusKCBe2r7r8lMCdYR1rGfoESefV38hdQZV0qK1KL2-iSO3qXwpExNGrkFQi1aECjiU0eUIcEg4kU4MwosoTf4EASWXtO0HedAY8uBu69VYk1TBkrn9f7MU24N6y_SZICLOYZBuemjS1UXImRNREuWo5GANLDdZcLG_evgQqY5-7B2kmbu6_g-RXfV1cieqlZzxQRnu7L7bDQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این ویدیو مربوط به آتیش گرفتن موتور یه پیک هست و یکی اون وسط داره بلندبلند شماره کارت پیک موتوری رو می‌خونه و مردم گوشی به‌دست دارن شماره رو می‌زنن که بهش کمک کنند موتور جدید بخره
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/146692" target="_blank">📅 16:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146691">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
آیا پاییز و زمستان قطعی برق خواهیم داشت؟
🔴
وزیر نیرو: از الان نمیشه پیش‌بینی کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/146691" target="_blank">📅 16:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146690">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0yoV7RgCDejVpsu6zZCza1-NKTa4iIhCAJFlahwUtRH3TZAwkFEhyAjQV3WRIy05E4tV5AetmwBoDRXwFmwJJ_leL_mU_IR3Qt0Vx71hJSRCFsmFb0ICphNhj0VPCSOONjbQh42VyBtSyyRMZ3p9sjV_FnmRd4WI1KXJMpkV9lyZHJ3qWk0ZLd5So0AhRYT1HYTLb59sbJyPV61m4M-6rfnuTAqCfAYtbVWgLfvIBEGLlAeA46vYWoI1zKoF2kWsuzu1vXZD2aufR3BEkMlxJ_gPItkMEuIKwJDdQlw7K8pPgrnT04etQSiwK0VDC8dRJ13DhixpIIRofzfym_C_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سه حمله هوایی اسرائیل
نبطیه الفوقا
در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/146690" target="_blank">📅 16:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146689">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9EAuqcaTNpSGt8qATsWEccp0mjeDCNUaH-BosGsnS7dkEMeYehclzuWwTBlmpiSUU1Q-DYRn4Q87YReLOGa-g25tIT0452tdP1ySjaUVfvf6jYEwOblQnfzG1ocP-H4CurlvTdKenB04bxoaoU9LU-QM81hnk_p_C-JJAl-m0u8cGB7Xk9sC9ihhWcW2Leovix-J1nyRjQaL0pvIJOw1QIfesUCvXzqbjVoTp_VJSnxom5WDmcUkADh-O0uPZLaNTbhhfB2c17S8pg5F5NQn-iN4RY11cN1iWWumeIX7F0hRq9cAaPqUpIXGK027UTYba5Vt05U45n-8CLMuAZr_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۱۰۴.۲۹ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146689" target="_blank">📅 16:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146688">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XrKV-LpDhed66tbOCzk3JPr5aULnIJ7Yt__vMY3gsJg7fIYEvwaOJhZ0AWjVK8YcZUYK1gatdOPMeojmX2r0flxGbu2EsbmOlpgnCGrj2HyyoB9pWcvpiYcEn5ELn_OulAh0M2nZMTTYhDITeweogtKPhChyCP_RfB2rxG1gyLk-ZCPoFKLTAhfL6V-suHOy5x-7UrEJR8ymsXJGo3Qoh-mTpWVJ8iXbNvAtAy9DYbEUJlB6r20uOTlXEyWwtLGC2DnnO9CJFeM8Ok-Pk52y7gcVP-friKwAY5csftx8j0jpXpDSrE84GOF6LQxmOBZbsK7_jA1RS17ueJ-pdiqdfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت «۱۰۰۰ دلار تتر» کاملاً بصورت رایگان
🌟
این پاداش بزرگ تونیکس است
💎
🔺
بدون سرمایه‌گذاری
🔺
بدون پرداخت هزینه و کاملا رایگان
🔺
بدون بازی و فعالیت سخت و زمان‌بر
📍
فقط کیف پول خود را وصل کنید و پاداش خود را آنی دریافت کنید.
توکن های دریافتی از همین لحظه قابل معامله و استفاده هستند
💯
فرصت و تعداد توکن ها محدود است همین الان اقدام کنید !
⬇️
⬇️
https://t.me/+jtexLpNX-fNlYjcx</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146688" target="_blank">📅 16:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146687">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی وزرای خارجه قطر و عربستان درباره آخرین تحولات منطقه‌ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/146687" target="_blank">📅 16:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146686">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
نیروهای انصارالله، تمام جزایر دریای سرخ، از جمله جزایر ابو علی، هانیش کبیر، هانیش صغیر، سویول هانیش، الممالح و جبل زوقار را به تصرف خود درآورده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146686" target="_blank">📅 15:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146685">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMd-zBkzJ5Dw_E6B8_3CMw9t-RKkBzBx1hSVOUNUxOLBGQp3DNVnQeOONceVCy41_vUZJbVdqcKMaD6RfVG76qvR9IrOrfItHbXaG20_gpdbic4Z89r1Ar9UhsgYO0H7wEUY_qt0i7kqU3VMZBYDO-WJdvp-hYxrUOx4nEpe-uJG9B61W0DDqWzHwSQcfww75ocJMO1MWwiEp8Xn-8JsSndji6CMDQr6SbJKvTWhMswJf-3rKIM-Ac1Bx1w_hWTYYYRCqcMGrFkSEHADbUwlCJsAN5_Sb5qT-hoSyM0MnUNs39oNOXRLAmBtgRPXgLgP_1-yG6o65269IwEKn0oqvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای انصارالله، تمام جزایر دریای سرخ، از جمله جزایر ابو علی، هانیش کبیر، هانیش صغیر، سویول هانیش، الممالح و جبل زوقار را به تصرف خود درآورده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/146685" target="_blank">📅 15:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146684">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoNv2jdL62OJtUNdthhT_iUcDuZyZwoZ-WzL4Cn9msZyNUokuprQVq2x083xSEQb5y3hAlqAC3aJ_HpWlVwk_vDmmGEh3x61QcZGTMfHsupfD8GmjnYYLosRV_UvzM77HnbqHqPHX-8FXtFInXPQAGggria5wVxKRi0LZH_OAu41mfBlYI55PzTVLodvwkiMcLkDOnPwzT6me75tGEaHlW7TlFuAd9HE1GhhNk82k7MoEv2FIl7rLv6-VK2Vx9Fix3b_bt1t8pGF7s0s9TaD57QOxP5IDqcK4Klsm2Y-qYHGjrdtHCEKrCMT79gx55FrC-7pR3gtzJS2RBGNLmWaZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دلار هم اکنون 236,750 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/146684" target="_blank">📅 15:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146683">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0abdca06.mp4?token=IO1sBjCOJR9wsqpKZ-n4zQofpGZR4JofnOG236_NB5jgdckvI4tJnEjZT2YWNwBA0--C8ziGZ4mcGVeyEcch6-HMq08S5EgBcb7oOEvtGlC0K1jhxLmk6tVclxrR1vku3zWPoJ_rT9KhEb6rWmdg2TxGRK3s9AvJyQAeI5olQzQnPzNeDXPJyoRvT1QWMDaonXD2hNlpRvZJVn-Vm50bLOkKA9g3jOswfChiFpOqzh8hO5slZKjWLB2VTNRNJhV4XGZR0T2mePIxKTfmN_1JJhjHC8DORTvFj-kUBOWGUXrJT3bKJEQVVU59SCJ2tk0PhE1d8Lpnz6wh3_yjN6MZ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0abdca06.mp4?token=IO1sBjCOJR9wsqpKZ-n4zQofpGZR4JofnOG236_NB5jgdckvI4tJnEjZT2YWNwBA0--C8ziGZ4mcGVeyEcch6-HMq08S5EgBcb7oOEvtGlC0K1jhxLmk6tVclxrR1vku3zWPoJ_rT9KhEb6rWmdg2TxGRK3s9AvJyQAeI5olQzQnPzNeDXPJyoRvT1QWMDaonXD2hNlpRvZJVn-Vm50bLOkKA9g3jOswfChiFpOqzh8hO5slZKjWLB2VTNRNJhV4XGZR0T2mePIxKTfmN_1JJhjHC8DORTvFj-kUBOWGUXrJT3bKJEQVVU59SCJ2tk0PhE1d8Lpnz6wh3_yjN6MZ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حادثه مرگبار برای کشتی خارجی در چین
🔴
خبرگزاری «شینهوا» خبر داد که یک کشتی باری خارجی در حین تعمیر و نگهداری در کارخانه کشتی‌سازی در شهر چینگدائو آتش گرفت.
🔴
به گفته مقامات چین، در نتیجه آتش گرفتن این کشتی در چینگدائو استان شاندونگ در شرق این کشور، ۲۰ نفر جان خود را از دست دادند و ۵ تن دیگر مفقود شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/146683" target="_blank">📅 15:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146682">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
رویترز: «سجاد حیدر خان»، سخنگوی وزارت امور خارجه پاکستان، گفت این کشور در حال حاضر بررسی حمله به حوثی‌ها در چارچوب توافق امنیتی مکه نیست.
🔴
او افزود: «در حال حاضر چنین موضوعی مطرح نیست… وقتی زمانش فرا برسد، طبق این توافق عمل خواهیم کرد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/146682" target="_blank">📅 15:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146681">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
نیروهای انصارالله پس از رسیدن به اردوگاه عُمری دریافتند که این اردوگاه از پیش تخلیه شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/146681" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146680">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
بلومبرگ: ایران توانمندی‌های موشکی خود را بازسازی کرده و مشاوران کاخ سفید هشدار داده‌اند که جنگ ممکن است تا سال ۲۰۲۹ ادامه پیدا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146680" target="_blank">📅 15:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146679">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0zJ6_2YPYZWbSMbFw-pHiQyxK7i4Et6Li-oupwk8SXfNifIffWlTE_4ya4J6yii5OeL_2bdjC8fZtVoqHeK01c84P-aErWTcYcVXgPa-3Q260Af9amG3D16JGx8hpG4N9dfNgdMSp3wUQmzbjCXj5Xb4lVYYEIXYDLi6mjQ5L9VR9pECGAGuHBMwbPgmsmyauvyBs6Yf3Ovyq1vsN9VBVLLLtjuQI1SXQk4KWBux3VB5a2qb4chQ7Isi4YHY3xS39XCEnQxO3GHMUjftkkWffqxmKCO93C4W0ZDszM3QdndUqD5SDEt0Wr1wFA1THI3nAJEc1Oe6FQl_Sk7DZ0qjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت دیروز سفارت ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146679" target="_blank">📅 15:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146678">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
رویترز: الجزایر تصمیم به قطع روابط دیپلماتیک با امارات متحده عربی گرفته است.
🔴
تلویزیون دولتی الجزایر اعلام کرد تمامی تلاش‌ها برای حفظ روابط دوجانبه به پایان رسیده، اما دلیل دقیق این تصمیم هنوز مشخص نیست
🔴
رسانه‌های الجزایری پیش‌تر امارات را به تلاش برای…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146678" target="_blank">📅 15:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146677">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c171ce10fb.mp4?token=W33LmuxlPJTpj824rWFoW2svrrZ1U3bUpwrUQYLPSHws-xEfQF9H3ECnjWUhqARPlpIuFES8ELlFEQa6yrt6O_Mcq079G8jyYW2zUl8qn4atKIu--yBoIugtAPV2XPZWsJZOhNqsf9UB0gspnSxN_etd1b3G_-eC9t_9l23e69QldU2NpiEvNUVTl51siQtJtgs4eF9tMd3B5scIIa3aOY7azit3WKa65sr9cGiustciUtb_myeAoZDkgnTKsXQsZuMblkfrbetgWj6fM3Sg9KqWkWH3cvIM1WY7QdE6HNrwmCKufyGe732VY62l_Tx4cJhlqOACfo_vAe3NyQoVBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c171ce10fb.mp4?token=W33LmuxlPJTpj824rWFoW2svrrZ1U3bUpwrUQYLPSHws-xEfQF9H3ECnjWUhqARPlpIuFES8ELlFEQa6yrt6O_Mcq079G8jyYW2zUl8qn4atKIu--yBoIugtAPV2XPZWsJZOhNqsf9UB0gspnSxN_etd1b3G_-eC9t_9l23e69QldU2NpiEvNUVTl51siQtJtgs4eF9tMd3B5scIIa3aOY7azit3WKa65sr9cGiustciUtb_myeAoZDkgnTKsXQsZuMblkfrbetgWj6fM3Sg9KqWkWH3cvIM1WY7QdE6HNrwmCKufyGe732VY62l_Tx4cJhlqOACfo_vAe3NyQoVBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمباران گسترده زیرساخت‌های حزب‌الله توسط نیروی هوایی اسرائیل در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146677" target="_blank">📅 15:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146675">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jjqi4rCHzZSY8npIVoDVB1GnXVoPtwZlYKs58yLDuiljun9Ejron195oZItMH85XC6NaJ0OO-Zxp2yuCw59aEOan-X9bqmc70riUB3T181fgJYBBpVmyKTYrJB9nUxEuSRzA1Pj1kYcMDBIs90V8OebH7yjxzAelnMdDycs-aAQIXjIRtyI58CligmVZl8ZIhHaPa7lHfyL52wbAUMFhzDNXhLv9cjhPHpWmA17E115WgaivvdcmmC3ac2DaD4WF6X4swFIlzukbYr3VY2qzTwAxk0tJf9c-VYr-jeaYC1Y2mVuCP9ZUprMb_T9_tltO7DeEg3ARzvkDch4QRl8rdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c62ff9ff.mp4?token=qQJAOMIkKNP-ofv-jgEPuzVkVktEdiFueO04YBKXyKisM89B73wkqAiEeuYv-oX10t1owH5RyN2_GYkDhT3FPKTvvZ81HRjItfax1cf8BYGC-yZqjnegdQNubDqX2fE4wixaSDbaSa2bVWBnFLbAEih_IVvwg1utHsDlju4axjoCt19dof2a98tUW9IispcGhhnqbJqHM6ND-v5FsZiwpGDnNAfQZ2Y2uEfQ3IRl5Vl86VgsV3DKfLXnDHESVyQNDSQYq8B-pxY8pF9-JLOtIsvDgtA_3OL1FDZ93vsPeHb03XPV2B8OTbpfLRo9XerobgjlGXHzJSKTRuKMmE92qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c62ff9ff.mp4?token=qQJAOMIkKNP-ofv-jgEPuzVkVktEdiFueO04YBKXyKisM89B73wkqAiEeuYv-oX10t1owH5RyN2_GYkDhT3FPKTvvZ81HRjItfax1cf8BYGC-yZqjnegdQNubDqX2fE4wixaSDbaSa2bVWBnFLbAEih_IVvwg1utHsDlju4axjoCt19dof2a98tUW9IispcGhhnqbJqHM6ND-v5FsZiwpGDnNAfQZ2Y2uEfQ3IRl5Vl86VgsV3DKfLXnDHESVyQNDSQYq8B-pxY8pF9-JLOtIsvDgtA_3OL1FDZ93vsPeHb03XPV2B8OTbpfLRo9XerobgjlGXHzJSKTRuKMmE92qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای بیشتری که تخریب سه مخزن نفتی در منطقه جازان عربستان سعودی را پس از حمله اخیر یمن تأیید می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146675" target="_blank">📅 15:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146674">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvTxU68cI4GWvcxusUmDjhOByooG1ok2dpy6hxjoaZbYGDKuscKQJVmpvjILdfQtrWVXWbxPQM5EQbWkAdEoh8l2zJgsPRfLXExv6rU3RE-Sqcw40rcUhwZHODsEhPWPI7dSZJTb1oxu2ZldCbyh57edAbUwsjKkv09vi4QlHyQ3GORCsrZg-sbzd3NtUH8sPzEWBwdnWDFvx_LlEONv8paVfmdp5m7hFMAdhX4-x61q3VcLD4x0MRzRMeH8td5nRN7j8nzgvwu-DvVl_sNmv81kKo2twaoRIGEItCTMO-qmMyCkJczkx1_0Ruggkam771I-sA9rjEo0Tj63a_6PqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی مطهرنیا:
مقامات اصلا نمیدونن جنگ سر چیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/146674" target="_blank">📅 15:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146673">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏
👈
پزشکیان: سالن‌های همایش و استخرهای متعلق به دولت ادغام می‌شوند
🔴
در مدیریت فرایند اصلاح الگوی مصرف، دولت پیشگام است و شخصاً بر جزئیات این روند در مجموعه‌ای که مستقر هستیم، نظارت دارم.
🔴
به‌منظور افزایش بهره‌وری و صرفه‌جویی در مصرف سوخت، بیشتر سالن‌های همایش، استخرها و ساختمان‌های متعلق به دولت برای عبور از بحران تعطیل یا ادغام خواهند شد.
🔴
همچنین توسعه و تسریع در نصب پنل‌های خورشیدی سقفی در واحدهای دولتی همچون استانداری‌ها در دستور کار قرار گرفته است.
🔴
از سوی دیگر سیستم روشنایی و گرمایشی هر نهاد دولتی در فصل سرما با الگوی کاهشی کنترل خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146673" target="_blank">📅 15:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146672">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851878f527.mp4?token=jnyKe16PrZM2oPTr9QoKLux2F54OiAnoYN3AsNBmUpbUweUn_vbs2YkPZH7C7nNC2b5daSq9d7Kplnvigy1j_0V84MZjJwei6UsNM0yHq5P4rN_xD6-qexBBrqhuhFFxntp4_3eqz5BJ_MX7K_vKDTl0il0EW_EWKA5JV65b-E1J9S2iDbN2xiJYf-c6oilyXuocOygQKTmQQH7FFLDKJZ66TF34YdgND9g65-cavKRpXyXLATXHJsbNAvHHv2s_7qbSgvJacPXv3TGoD1q0wvCsXQGJz3imCDW97AZlPFodzolnCtanu78VJw_l9sEMXZW9w4VSnVxeI6SISRe-2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851878f527.mp4?token=jnyKe16PrZM2oPTr9QoKLux2F54OiAnoYN3AsNBmUpbUweUn_vbs2YkPZH7C7nNC2b5daSq9d7Kplnvigy1j_0V84MZjJwei6UsNM0yHq5P4rN_xD6-qexBBrqhuhFFxntp4_3eqz5BJ_MX7K_vKDTl0il0EW_EWKA5JV65b-E1J9S2iDbN2xiJYf-c6oilyXuocOygQKTmQQH7FFLDKJZ66TF34YdgND9g65-cavKRpXyXLATXHJsbNAvHHv2s_7qbSgvJacPXv3TGoD1q0wvCsXQGJz3imCDW97AZlPFodzolnCtanu78VJw_l9sEMXZW9w4VSnVxeI6SISRe-2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو: آلمان با استقرار دائمی یک تیپ زرهی جدید در لیتوانی، به امنیت متحدان کمک می‌کند.
🔴
سپاه یکم آلمان-هلند نیز مسئولیت فرماندهی جدیدی را در جناح شرقی ناتو بر عهده گرفته است.
🔴
آلمان برنامه دارد تا سال ۲۰۲۹، معادل ۳.۵ درصد از تولید ناخالص داخلی خود را صرف هزینه‌های اصلی دفاعی کند؛ یعنی بسیار زودتر از مهلت تعیین‌شده تا سال ۲۰۳۵
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146672" target="_blank">📅 14:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146671">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba73a5c62c.mp4?token=pnokZPI7I8GZ_g5fUonmI0vnyKtfLhfzGbMcEYO1Fbsx6283vTx4pA0kpxJQk-hoFLjASAGYcJXPpRrjQNPc4AS176VX9KWMkW22P8TW8Nb7IJFvudCx_6Uw5ilPpfX0lGWewp1-APjRlPPWhlYheNPLDLB-HzA7VKv7LL_72XAi3g44Cka1G4kfjtvXJIk06QmBrWSmpcny7y9mWNCDvyufNfh3O9sBB5cKe93BGGUosbVUhbyuLl0ZEYo3A-8rCEVZyLzfTdoEb0t0cPvNKo8atwC5NkC3xloIsN5eXlTYBD36e6lrVBMH1NgWWGx7KRvzjFpaPPTxElAif58s_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba73a5c62c.mp4?token=pnokZPI7I8GZ_g5fUonmI0vnyKtfLhfzGbMcEYO1Fbsx6283vTx4pA0kpxJQk-hoFLjASAGYcJXPpRrjQNPc4AS176VX9KWMkW22P8TW8Nb7IJFvudCx_6Uw5ilPpfX0lGWewp1-APjRlPPWhlYheNPLDLB-HzA7VKv7LL_72XAi3g44Cka1G4kfjtvXJIk06QmBrWSmpcny7y9mWNCDvyufNfh3O9sBB5cKe93BGGUosbVUhbyuLl0ZEYo3A-8rCEVZyLzfTdoEb0t0cPvNKo8atwC5NkC3xloIsN5eXlTYBD36e6lrVBMH1NgWWGx7KRvzjFpaPPTxElAif58s_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک روته، دبیرکل ناتو: «همه برای یکی و یکی برای همه؛ این همان شیوه‌ای است که ناتو عمل می‌کند. روسیه می‌خواهد ما را از هم جدا کند، اما ما متحد هستیم.
🔴
روسیه می‌خواهد مانع کمک ما به اوکراین شود، اما ما کمک بیشتری به اوکراین خواهیم کرد. روسیه می‌خواهد قدرتمند به نظر برسد، اما ما قوی‌تریم.
🔴
اقدامات روسیه نشانه ضعف و نشانه شکست این کشور در رسیدن به اهدافش در اوکراین است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/146671" target="_blank">📅 14:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146670">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فوری / یک حادثه دریایی در نزدیکی سواحل یمن رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146670" target="_blank">📅 14:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146669">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
رویترز
:
الجزایر تصمیم به قطع روابط دیپلماتیک با امارات متحده عربی گرفته است.
🔴
تلویزیون دولتی الجزایر اعلام کرد تمامی تلاش‌ها برای حفظ روابط دوجانبه به پایان رسیده، اما دلیل دقیق این تصمیم هنوز مشخص نیست
🔴
رسانه‌های الجزایری پیش‌تر امارات را به تلاش برای افزایش تنش‌های منطقه‌ای متهم کرده بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146669" target="_blank">📅 14:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146668">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری / یک حادثه دریایی در نزدیکی سواحل یمن رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146668" target="_blank">📅 14:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146667">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
به گزارش بلومبرگ، ایرباس ممکن است برای کنترل بیشتر بر تأمین قطعات، مالکیت یا کنترل مستقیم برخی شرکت‌های تأمین‌کننده را در دست بگیرد.
🔴
این تصمیم پس از سال‌ها گلوگاه در زنجیره تأمین و صنعت پیمانکاری مطرح شده؛ مشکلاتی که باعث تأخیر در تولید و عقب‌ماندن ایرباس از اهداف تحویل هواپیما شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146667" target="_blank">📅 14:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146666">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rR4NSWiGxfjf5DqxN6-QGcWZLKvJFbMqO1vi8Yuzl3oJQkKrQayyk7AsdIk1eab_CjuSj8a5uqvrwwD6MHeDPMMEr6NCLr0Brxwm0jroT2vRQYC9JLpHZNj158sxIK4XSXy07PzgWiRYqKDkJlxmruE2MDMthVMNwTuAWAkNe3MxXpwj3jMTyOW87neUA2V2IxnObe2HF-8HDotWxJuko-Mz6TrN-qlDUNzcnBOV_C1q_M6w1DUpXW6Lr-Rozo33RNJfTRr7llnuGcC7KzuqXPanLFOfCZ4IxrI1q2A_W80wqTXCfVLtKf-rH6ewPkI7NncfDCRMntKy7AxjfIDCww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به‌روزرسانی نقشه کنترل و درگیری‌ها؛ فاصله ۶۰ کیلومتری ارتش یمن تا باب‌المندب پس از تصرف المخا
🔴
بر اساس نقشه‌های جدید کنترل میدانی، پس از تسلط نیروهای ارتش یمن بر شهر بندری المخا، هم‌اکنون فاصله این نیروها تا تنگه راهبردی باب‌المندب به حدود ۶۰ کیلومتر رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146666" target="_blank">📅 14:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146665">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
نیروهای جنوبی وابسته به امارات، از ورود عناصر مرتبط با عربستان سعودی به شهرهای جنوبی جلوگیری کردند، این اقدام پس از فرار این عناصر در برابر پیشروی ارتش یمن صورت گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146665" target="_blank">📅 14:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146663">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
پزشکیان: ممکن است در برخی جا‌ها با کاهش سوخت‌رسانی مواجه شویم، لذا باید سوخت و تجهیزات گرمایشی جایگزین به آن مناطق برسند
🔴
جهت عبور از بحران، بیشتر سالن‌های همایش، استخر‌ها و ساختمان‌های متعلق به دولت تعطیل یا ادغام خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146663" target="_blank">📅 14:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146662">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
شبکه سی‌بی‌اس گزارش داده در حمله موشکی بالستیک ایران به پایگاه هوایی «موفق‌السلطی» در اردن، یک هواپیمای تهاجمی A-10C نیروی هوایی آمریکا یکی از بال‌های خود را از دست داده است.
🔴
بر اساس این گزارش، حدود ۸ فروند جنگنده F-15E نیز به‌صورت جزئی آسیب دیده‌اند.
🔴
سی‌بی‌اس افزوده جنگنده‌های F-15E آسیب‌دیده پس از بررسی و تعمیر، دوباره به خدمت بازگشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146662" target="_blank">📅 13:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146661">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=oDnQdi1sXj5Hd6MbIwfoHuTvV9XOsDHOY8nAz5VX_cYj4HJP8X7DSU2A6Sw1G21NOoJWmq4-GWZW3I9PH1-iMd6AzRgNDDpANqkycBveMGSS3Ep1hrAhASGSNWnLCzysf_eXr3MIERwL6zxlC4G91iq7M7d0fpj61QCm0ZTxVTquJiVYB912qdcZ_S8ibOXscfCib6yYy2w2DV5ZU5ggbnEA2ao78qAplJEWrHHPnIuotb54NgbVjLXRPz_hvWaVKK9A1gtU-QK4l4VvW4XOuIBui36Ds9pFhL7Jq4R0hI5Twe9ABqDL0P21AoN64P2UuhJ9bvk9aHO8mjGjCOH_kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a695c5e874.mp4?token=oDnQdi1sXj5Hd6MbIwfoHuTvV9XOsDHOY8nAz5VX_cYj4HJP8X7DSU2A6Sw1G21NOoJWmq4-GWZW3I9PH1-iMd6AzRgNDDpANqkycBveMGSS3Ep1hrAhASGSNWnLCzysf_eXr3MIERwL6zxlC4G91iq7M7d0fpj61QCm0ZTxVTquJiVYB912qdcZ_S8ibOXscfCib6yYy2w2DV5ZU5ggbnEA2ao78qAplJEWrHHPnIuotb54NgbVjLXRPz_hvWaVKK9A1gtU-QK4l4VvW4XOuIBui36Ds9pFhL7Jq4R0hI5Twe9ABqDL0P21AoN64P2UuhJ9bvk9aHO8mjGjCOH_kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسن روحانی خطاب به تندرو ها: انتقام رهبر رو امام زمان که ظهور کنه میگیره
🔴
وسط مذاکره برای اینکه راهی پیدا کنیم که جنگ زورتر تموم شه یه عده میگن باید انتقام بگیریم خب چجوری ؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146661" target="_blank">📅 13:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146660">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5c767001.mp4?token=gf4Or-blAM17oKhgwKBistQFqHgel8sK5AyppU73sTTsioCm3LBlsKvtz2XX5xilma6HSm-WoIPp51eRPnkXWNbn9_UZkRQkaRuY2PbIIHX8imiq1krPJMOiwYxmDslYeRYFKIoZV0GDkciyGhPreo27oyDdZIsSQ9Eph7ax7xvFIt95kxs4c1TXV6K98KFXbxJWehNJeIFbiCB6mTR5rIkbfIWYU6gYtGIPbImmAZM8VZolrka180JGPPQFMbPnQl8m4kceqWarMqSZJo0EekS1LvWtnlDNfSh-t9Iv9SsFy64ChgfDBLBtOYZZ3-hclxQpe6SQQl3pS8Z_oYeYkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5c767001.mp4?token=gf4Or-blAM17oKhgwKBistQFqHgel8sK5AyppU73sTTsioCm3LBlsKvtz2XX5xilma6HSm-WoIPp51eRPnkXWNbn9_UZkRQkaRuY2PbIIHX8imiq1krPJMOiwYxmDslYeRYFKIoZV0GDkciyGhPreo27oyDdZIsSQ9Eph7ax7xvFIt95kxs4c1TXV6K98KFXbxJWehNJeIFbiCB6mTR5rIkbfIWYU6gYtGIPbImmAZM8VZolrka180JGPPQFMbPnQl8m4kceqWarMqSZJo0EekS1LvWtnlDNfSh-t9Iv9SsFy64ChgfDBLBtOYZZ3-hclxQpe6SQQl3pS8Z_oYeYkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما بعد از زدن بست نابی: بانک مرکزی کشورمان ۵۰۰ میلیون تن طلا دارد
🔴
طلای موجود در بازار ایران و منازل مردم ۵۰۰ میلیون تن است!!
🔴
این درحالی است که کل طلای موجود در جهان حدود ۲۰۰ هزار تن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146660" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146659">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏
👈
مخابرات اعلام کرد از ۲۰ شهریور، تعرفه خدماتش رو ۴۵ درصد گرون میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/146659" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146658">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وضعیت این روزای ایران خیلیامون رو به بن بست کشونده
درآمد 95 درصد مردم الان ریالیه اما قیمت همه چی به دلاره
اگر بخوایم از زندگی عقب نمونیم
و جزو اون 95 درصد مردم نباشیم چاره ای نداریم جز اینکه درآمدمون دلاری باشه
همه وارد کانال زیر بشید لینکشو گذاشتم  همه رو به درآمد دلاری میرسونه لینک کانالشو میزارم عضوش بشید
👇
👇
https://t.me/+fDXpi2Dbi185ZjRk
https://t.me/+fDXpi2Dbi185ZjRk</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146658" target="_blank">📅 13:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146657">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل ،کاتز :هرگونه حمله به اسرائیل از سوی ایران، به هر دلیلی و از هر مکانی، با پاسخی قوی و بی‌سابقه مواجه خواهد شد.
🔴
پاسخ به ایران شامل تأسیسات اصلی انرژی آن خواهد بود.
🔴
این حمله‌، ایران را دهه‌ها به عقب بازمی‌گرداند و آن را تضعیف می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146657" target="_blank">📅 13:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146656">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkEzheEL3NB_4UmsmgDJpp8Z_QjZh9ZYh3BCVTSUUx2dpLJ7Br4K7XFv4ogyWfvGGMcm0HWgA105ZThDF66hYlVbPiSg0HOk7pt6oxG0ZT9mqcgrhLLZIducR0LpujQg_42Fy05kH-l_wtHr2mkdkvOfp6pHSwXQUB0AR0a4S7HqW0rIOeAt9_pb_rEJwfzKSFy0dcj1MksDdOz1Ke2VU4RTqOu1fgnfwzTwQo5ve1x9M6GHE39OKZv1onMBTVWHFd50LFMnge-tYWUcDzTAslGQXTj5RM8ZoALcWJ_YZ0x7I_UUIh6u8BNZO-I80UTSvb4QJ7r2-g36W7t4x6uTQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سید صادق حسینی، خبرنگار: در روزهایی که کشور درگیر جنگ و محاصره است هنوز کسانی هستند که مسئله‌شان حجاب، قطع اینترنت و تعطیلی کافه‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146656" target="_blank">📅 13:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146655">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kku2WlFSn5ZocTA0kISoAP18N_mafS3pU1wgH4Nup5OWL2h3LSILzEGF5QtnLrkpGQYr_4qFF65eNMg7hnJwnmIqhx5acYmhQNPlXhY8LwKcgmuVASeRQK_twIc-m3ILBDV-o8pusUPaeM0T9OkEXbZXw7Z8bnXwf0GNWz8Oh6EMdtLIsj7wniv9ySV0mEGrz1Fm5pw9S31OYwKLy9y14GDFkUGeoMNnIiIB6TEhkEtyqdmPIpcVQnw4UiEpVGLwaHMjKfrIDEYMzzfpTigZeAUwW7ScJTQ1ZlA5cq9w2CgD4PgZUQX06MjheWCUU2_cV_3k4wqEJEvXRUdd5CQoZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۱۰۲.۵ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146655" target="_blank">📅 13:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146654">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
شرکت مخابرات ایران در اطلاعیه‌ای، از افزایش ۴۵ درصدی تعرفه برخی خدمات ارتباطی از ۲۰ شهریور ۱۴۰۵ خبر داد.
🔴
بر اساس ابلاغ وزارت صنعت، تعرفه مکالمه تلفن ثابت با تلفن همراه، تماس‌های همراه با همراه و پیامک تلفن همراه تعدیل می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146654" target="_blank">📅 13:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146653">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b79e89930c.mp4?token=PFBqZHFPqURIcKd9KgWROC4G9Eh5nuJfYKh78N32AORts6UmB-P4hm2JKjOCx9_mWBxZVJ6OYBx66LyWyCKC55RXEMYzjoOgLsRYIIJGGhbpYi-NnQdxo6OcFfRvHKMxRBQLKpfqhAQSs3mBrZe5Fhx9t5_5PIjCSH92-d2ddxWcJiQIh5Oqsp6h0E8EkxZxnbzjk83BU5xG9B9CC1n5K7wtB0zYRRYp9Dcy_IHxRITC-3-gHEhqCUsjifod3Y12ayCji3YKf8tcZY30cUnqxRHSqpsjya2eqK9yRDOqXE3CiADEs1vxxs40Eon1q0F9FDyLnabYMdUHLfA6s-AuGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b79e89930c.mp4?token=PFBqZHFPqURIcKd9KgWROC4G9Eh5nuJfYKh78N32AORts6UmB-P4hm2JKjOCx9_mWBxZVJ6OYBx66LyWyCKC55RXEMYzjoOgLsRYIIJGGhbpYi-NnQdxo6OcFfRvHKMxRBQLKpfqhAQSs3mBrZe5Fhx9t5_5PIjCSH92-d2ddxWcJiQIh5Oqsp6h0E8EkxZxnbzjk83BU5xG9B9CC1n5K7wtB0zYRRYp9Dcy_IHxRITC-3-gHEhqCUsjifod3Y12ayCji3YKf8tcZY30cUnqxRHSqpsjya2eqK9yRDOqXE3CiADEs1vxxs40Eon1q0F9FDyLnabYMdUHLfA6s-AuGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر منتشرشده از ورود نیروهای انصار الله (حوثی های یمن) به بندر راهبردی المخا، در استان تعز و مشرف به تنگه باب المندب
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146653" target="_blank">📅 13:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146652">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
نایب رئیس شورای امنیت روسیه، مدودف: می‌توانیم کاری کنیم از کی‌یف و تاسیسات ناتو فقط غبار هسته‌ای خاکستری باقی بماند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146652" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146651">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری / هم اکنون شلیک موشک‌هایی از یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146651" target="_blank">📅 13:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146649">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
رویترز: شمار کشتی‌هایی عبوری از تنگه هرمز در روز چهارشنبه، به ۷ فروند کاهش یافت
🔴
داده‌های اولیه ردیابی تردد کشتی‌ها نشان می‌دهد شمار کشتی‌هایی که روز چهارشنبه از تنگه هرمز عبور کردند به ۷ فروند کاهش یافته است؛ این رقم در روز سه‌شنبه ۱۲ فروند بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146649" target="_blank">📅 13:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146648">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ccb685b3.mp4?token=JVh8smtIHcoiKFfv2No5OzS1hsD4mQI4gsleU56Y-OLA01M4uWwkgmym1Z5kf5iSZ7kHpdEhNDpy4s001Up7wXPg1OprI61mFtkGB4WpydHwQlXXYvkiKc_eGDqD2361qDZAKmd39JgEbdb5offc677UhWxjEAb6Lv-6HwBHtFfY-FM8mrhj6is3QCZIfEeAZ1EfBTCXMa7uSIBwGOsiK6WqGdZikdd3lFlwmwfV_XBe_J0X_LfANzO2fsm89rHik5yLeQalurM1u-8yai-ASg9Wkh4ilnwsAcIDgaX-JTYpwryTitaupfF7nUo8J9sW0PKVOV9T-sFeeW5KRo2_Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ccb685b3.mp4?token=JVh8smtIHcoiKFfv2No5OzS1hsD4mQI4gsleU56Y-OLA01M4uWwkgmym1Z5kf5iSZ7kHpdEhNDpy4s001Up7wXPg1OprI61mFtkGB4WpydHwQlXXYvkiKc_eGDqD2361qDZAKmd39JgEbdb5offc677UhWxjEAb6Lv-6HwBHtFfY-FM8mrhj6is3QCZIfEeAZ1EfBTCXMa7uSIBwGOsiK6WqGdZikdd3lFlwmwfV_XBe_J0X_LfANzO2fsm89rHik5yLeQalurM1u-8yai-ASg9Wkh4ilnwsAcIDgaX-JTYpwryTitaupfF7nUo8J9sW0PKVOV9T-sFeeW5KRo2_Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری فاکس نیوز: ۵۰۰۰ دلار برای هر شهروند برای هر رای؟
🔴
یعنی ۱.۳ تریلیون دلار. منتقدان می‌گویند رئیس‌جمهور در حال رشوه دادن به رأی‌دهندگان است و کشور را ورشکسته می‌کند؛
🔴
معاون ترامپ: رئیس جمهور ترامپ می‌خواهد شهروندان را در این ثروت عظیم ناشی از تعرفه ها سهیم کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/146648" target="_blank">📅 12:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146646">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سردار حسن زاده : آمادۀ عملیات‌های تهاجمی برق‌آسا هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/146646" target="_blank">📅 12:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146645">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح عراق: اجازه استفاده از خاک خود را برای هدف قرار دادن سایر کشورها نمی‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146645" target="_blank">📅 12:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146644">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=vMIlc4RStPnUI0Z7iTzkGTWa7T85JoLBjxFrnPgJJellApOgNqGQBJ-lUUB5cldpquzBkSgLnnUqfopazA06OiDRnS7CfHH_bBOcjIi3t5kL0HFSZBhrAwvV45RLeOP4g6T_YgWt7Ol1ZJDr4qaLDtqoUAuNO0PRQYj1KC115dWEiZsseFWnrduR4d81G6jRelOAJAz13uvn3NxokY4j8x4gtTj1eiB_ZovsCFsgAjCfsAbJ-MfzS6wA0IgNFcH43aati8jAqTSsETc2uTInARChLKtrsNhp4fJI8vvcRe08kyDcdRWMGO7HqaNxiunw6WP7vHpl0LWUL-MXzv4wVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=vMIlc4RStPnUI0Z7iTzkGTWa7T85JoLBjxFrnPgJJellApOgNqGQBJ-lUUB5cldpquzBkSgLnnUqfopazA06OiDRnS7CfHH_bBOcjIi3t5kL0HFSZBhrAwvV45RLeOP4g6T_YgWt7Ol1ZJDr4qaLDtqoUAuNO0PRQYj1KC115dWEiZsseFWnrduR4d81G6jRelOAJAz13uvn3NxokY4j8x4gtTj1eiB_ZovsCFsgAjCfsAbJ-MfzS6wA0IgNFcH43aati8jAqTSsETc2uTInARChLKtrsNhp4fJI8vvcRe08kyDcdRWMGO7HqaNxiunw6WP7vHpl0LWUL-MXzv4wVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتشفشان ساکوراجیما در جزیره کیوشو ژاپن فوران کرد و خاکستر و مواد آتشفشانی را تا ارتفاع چند هزار فوتی به هوا فرستاد.
🔴
آژانس هواشناسی ژاپن همچنان سطح هشدار ۳ را برقرار کرده و محدوده‌ای به شعاع ۲ کیلومتر اطراف دهانه آتشفشان را ممنوعه اعلام کرده است.
🔴
این فوران بر جمعیت محلی و حمل‌ونقل منطقه تأثیر گذاشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/146644" target="_blank">📅 12:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146643">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
قیمت نفت خام برنت به 102 دلار برای هر بشکه افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146643" target="_blank">📅 12:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146642">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706322ff6b.mp4?token=N-siwGD8T2loh5Jd68z07lOHAP51FgX5SCaOucdD7qQ5qqNweOGRerV1MA-acIV8-1NV5p5dUCctz9D4Pm67a2nFEoyXlNzlM5fgF8s1ZC4-MDweT9Ffzd-z37HXLawnDjrFq4YQ63hn65gv0WobKuWQuzGBUDfTM-74USe9R1_cfzdCCOj1W7Grvf0oMRjWfmF4UdOqA9m-QqB7RV0watHsIkfrSKo8A-5OwdbDkjtBpSJZ6EDmiV_ohnJ1fhbuG1ZMGkUglKuFVpqwfsmOneeatitgWfvAjD5KFXyWtrnF8QSPlcVhC75-UWGRbM2w82vi4YrTs4BJSbLc3Nva8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706322ff6b.mp4?token=N-siwGD8T2loh5Jd68z07lOHAP51FgX5SCaOucdD7qQ5qqNweOGRerV1MA-acIV8-1NV5p5dUCctz9D4Pm67a2nFEoyXlNzlM5fgF8s1ZC4-MDweT9Ffzd-z37HXLawnDjrFq4YQ63hn65gv0WobKuWQuzGBUDfTM-74USe9R1_cfzdCCOj1W7Grvf0oMRjWfmF4UdOqA9m-QqB7RV0watHsIkfrSKo8A-5OwdbDkjtBpSJZ6EDmiV_ohnJ1fhbuG1ZMGkUglKuFVpqwfsmOneeatitgWfvAjD5KFXyWtrnF8QSPlcVhC75-UWGRbM2w82vi4YrTs4BJSbLc3Nva8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تخریب عجیب یک کاروان‌سرای تاریخی در سبزوار
🔴
رئیس میراث فرهنگی سبزوار: این بنا سردر باشکوهی داشت که برای ثبت در فهرست آثار ملی اقدام شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146642" target="_blank">📅 12:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146641">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ایرنا: حدود ۱۰۰ تن مرغ فاسد در مشهد، پس از فرآوری به سوسیس و کالباس تبدیل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146641" target="_blank">📅 12:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146640">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
بلومبرگ به نقل از منبع ایرانی: ایران تا زمانی که اطمینان پیدا نکنند آمریکا در آینده برای حمله مجدد بیش از حد محتاط خواهد بود، جنگ را ادامه می‌دهد
🔴
دولت ترامپ تنها به تهدید و تشدید تنش پاسخ می‌دهد
🔴
تهران آماده ورود به جنگی شدیدتر است و اگر واشنگتن به تجاوزات خود ادامه دهد، حملات متقابل خود را تشدید خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146640" target="_blank">📅 12:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146639">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpxpfB4bzMojaFCk2Y3KKcu1AdHOIdkm81UosEpXf4gzueUwj8kYvASaduhcuRjBDdR6ujpUjicCuGWSzDatYwaIIp0xfRGs1IXTHotdO6Ff0D3yr6RvbvSUhld0CPtXsTqa0VtWqSrZO75oKomSr3GggIPN7WZfFfUczPwCTGH_lS3YRPl5jj6yH-2ldsNLww_NmUKdj6HsqJ1c05u2PexzJKyRi1YQkUCkAnSpgbXyHw9wcgLyWMePhWVviepUyOxT7PEY3gPSC9mzBMiXBzaDLCcZzXAKaQJwjtqgYgTm67CTuUwtSvSVyjnwKgc5InhbeInqYLaRFlABaihW9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش CBS، حمله موشکی بالستیک ایران به پایگاه هوایی موفق‌السلطی اردن در دو روز گذشته، به چند فروند هواپیمای آمریکایی آسیب زده است.
🔴
۸ فروند F-15 دچار آسیب «جزئی» شدند. یک فروند A-10 به‌شدت آسیب دید و یکی از بال‌های خود را از دست داد.
🔴
نکته: آخرین بار که یک هواپیمای آمریکایی با عنوان «آسیب‌دیده» گزارش شد، مربوط به یک فروند E-3 Sentry در پایگاه هوایی ملک عبدالله دوم (PSAB) بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146639" target="_blank">📅 12:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146638">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
حوثی ها (انصارالله) اعلام کرد که یک پهپاد شناسایی و رزمی سعودی به نام "کرایل" را سرنگون کرده است، در حالی که این پهپاد در حال انجام فعالیت‌ در فضای هوایی استان حجه بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146638" target="_blank">📅 11:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146637">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزارت خارجه پاکستان درباره درگیری حوثی ها و عربستان سعودی: هیچ موضوعی درباره پاسخ نظامی در دست بررسی نیست.
🔴
توافق‌نامه مکه یک پیمان دفاعی است و در حال حاضر هیچ برنامه‌ای برای گسترش این توافق‌نامه وجود ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146637" target="_blank">📅 11:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146636">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
الجزیره به نقل از ونس ، معاون رئیس جمهوری آمریکا: ما ایران را از صادرات نفتی خود محروم کرده و این کشور دیگر هیچ درآمدی از بخش انرژی ندارد. ایران دیگر گزینه های زیادی پیش رو ندارد و اگر ترامپ بخواهد می توانیم با این کشور به توافق برسیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146636" target="_blank">📅 11:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146635">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
پاکستان: در حال حاضر تصمیمی برای الحاق عضو جدیدی به «توافق مکه» گرفته نشده
🔴
ایران برای استفاده از انرژی صلح‌آمیز هسته‌ای حق مشروع دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146635" target="_blank">📅 11:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146634">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
رانندگان اسنپ در اعتراض به پایین بودن کرایه‌ها، افزایش هزینه‌های فعالیت و همچنین تغییرات جدید در قیمت بنزین و نحوه تخصیص سهمیه سوخت، دست به اعتصاب زدند
🔴
در ادامه این اعتراض‌ها، اسنپ اعلام کرد به صورت علی‌الحساب مبلغ ۲۵۰۰ تومان به ازای هر سفر به رانندگان پرداخت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146634" target="_blank">📅 11:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146633">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
خبرنگار: آیا پاییز و زمستان قطعی برق خواهیم داشت؟
🔴
وزیر نیرو: تلاش می‌کنیم کمتر باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146633" target="_blank">📅 11:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146630">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fb52346c.mp4?token=ILPm41Vlnv5m0HeNFktq_fiXTdbDSvlhtN6SQaOlqPwAoP-55ZUsuk59Q4UhHjmuygnxl2of9-JShBrLeJi3RsX6c7_TZbTafqHDN4byMYWzjzmlkVe04sYtPNwidIba_FcNqgz59BNX46saydUYlyfuaGoN0mgZUoO-EoXrwLR6AgV1o8chvWuJ8oBBf1Va5JGwtdg1nQryxzjkCnpAm5dKoJ3ibiDcOtorf9t3-17Mz9m36tKDlsD1OUsc8r_s8P7SuFv0C-UTXYb-mifPtWfj8vq9CixO_IwliamwIAe9W8mRzZ38HqG_i7FojLdhsjOUOggp9tpJCdsXbSEIqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fb52346c.mp4?token=ILPm41Vlnv5m0HeNFktq_fiXTdbDSvlhtN6SQaOlqPwAoP-55ZUsuk59Q4UhHjmuygnxl2of9-JShBrLeJi3RsX6c7_TZbTafqHDN4byMYWzjzmlkVe04sYtPNwidIba_FcNqgz59BNX46saydUYlyfuaGoN0mgZUoO-EoXrwLR6AgV1o8chvWuJ8oBBf1Va5JGwtdg1nQryxzjkCnpAm5dKoJ3ibiDcOtorf9t3-17Mz9m36tKDlsD1OUsc8r_s8P7SuFv0C-UTXYb-mifPtWfj8vq9CixO_IwliamwIAe9W8mRzZ38HqG_i7FojLdhsjOUOggp9tpJCdsXbSEIqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نسخه تاشو ایفون ۱۸
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146630" target="_blank">📅 11:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146629">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
رفیعی، نماینده مجلس: مذاکرات با کشور عمان برای رسیدن به توافق بر سر تنگه هرمز سبب شد طرح تنگه هرمز با کندی پیش رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146629" target="_blank">📅 11:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146628">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-Vb-FYEVWK31juV6qdWswLPH2v5ANB_UxX_F7_3LPUO_4vvsPxfG9Bd9mc-npnLfK34K-VpuI39EvgoeySL-qH_0cTr-YyKz57hKYkNXDCgGMw5FMMYafb9fCRm0lLQJVkVYypYwE1yNLhIiL4p1xc-WOCyAkPee8HCf8ouzTlmwvv9a67qTTqvSg00NbIfwk5JiUemErXrDIcuLLOInBzAbQqKHqi_Upp019feYIwTTNiZxndZwDQrcWwRCee0lLmoPxoXn6QIq9jAmJpgfn4z_1vXN7PEdlM0fuYvW6mzL9x3fpiek23GA5oQ1BGYtogFBXMcoQ1ig_zmT7MwGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با پول پژو ۲۰۷ به قیمت ایران، در کشورهای مختلف چه ماشینی می شود خرید؟
🔴
امارات لکسوس ۲۰۱۶
🔴
المان بی ام و سری۳
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146628" target="_blank">📅 11:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146627">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
قیمت نفت ۱۰۱ دلار و ۶۰ سنت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146627" target="_blank">📅 11:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146626">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رئیس سازمان مدیریت بحران: تاکنون ۴۵۰۰ میلیارد تومان خسارت در مازندران برآورد شده و احتمال افزایش این رقم تا هزار میلیارد تومان دیگر وجود دارد.
🔴
جبران خسارت‌ها برای طرح در هیئت دولت پیگیری خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146626" target="_blank">📅 11:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146625">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/151ae0ccb2.mp4?token=rtGsd6p9HOct9SqRTm2YmiMk13qfvqZYTW93fk2GV5uv42UKUBuZQr0Myr3YARRuAtQH3L-2X2FJXVTgSMxy6h1jSDHWJQDzMGFSamoIHolLPmRyNWDiXk5Abc0ZJtJKNzWFbNGI416_fZL4d-uF-46QANq2TyK2sLOF8a01LrnXCnrhG6qxGLcf4W6B5Ba-_HeAHDfCmQLCzCBHdJkAaxppi2u1ZB8Bi8K6EqMqK9l1pc_c0U1OoNbrS8je5cimpIRrdLgY4RW_rfMaBklUioHfTCwy9Um6BtYjTywiSHlv8kDVyDwl77VtzcglObzBCG6IyV0faHJBWAxvBgzTtoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/151ae0ccb2.mp4?token=rtGsd6p9HOct9SqRTm2YmiMk13qfvqZYTW93fk2GV5uv42UKUBuZQr0Myr3YARRuAtQH3L-2X2FJXVTgSMxy6h1jSDHWJQDzMGFSamoIHolLPmRyNWDiXk5Abc0ZJtJKNzWFbNGI416_fZL4d-uF-46QANq2TyK2sLOF8a01LrnXCnrhG6qxGLcf4W6B5Ba-_HeAHDfCmQLCzCBHdJkAaxppi2u1ZB8Bi8K6EqMqK9l1pc_c0U1OoNbrS8je5cimpIRrdLgY4RW_rfMaBklUioHfTCwy9Um6BtYjTywiSHlv8kDVyDwl77VtzcglObzBCG6IyV0faHJBWAxvBgzTtoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: اگر ایران سلاح هسته‌ای داشت، من با رهبرشان تماس می‌گرفتم.
🔴
می‌گفتم: «آقای رهبر حال شما چطور است قربان؟ آیا کاری هست که بتوانیم برایتان انجام دهیم؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146625" target="_blank">📅 11:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146624">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGxfMnlZ24iWfrtsQf1cZYjB3_OvMh7OSnY7z0jp5wAZe-eH8urs1B-8Es6ftvabWdjsMiRBnJ8ObtqZGwxnHGv68CtE06YQjuhyEOQbP7kXSoUjF3JnFdJ0f0SJm4n5_Eay2z_b8QtKbdXEkkKMZ8hAK7XRUWRZiAAytBNXYfm3Mjmy6wcAD9pWrRb4cvqCmNQfwHC8feMaQwengWlQAwu9UcUlUwqYUq3sfMrDIZrP_lCqmAPdTNgmXUKDCjLpHf8VFBEWvSwILeV9Jo6m2PoJt-USQmGfKw7yYVftwyNU81q8TWxXgQK3wIFPYuaoD2E8NbmZOzBc0uXfHqxefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجارهای اسرائیل شهر المنصوری در جنوب لبنان را هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146624" target="_blank">📅 11:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146623">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/574dd70fc0.mp4?token=Y-m-_R3usXyhVyZDBv5IeKw6KiVr-SBb2K2nTDOocCgcWrKdzjX2omXbvZULOiyD5oG0Oz5I-MBXoBuQ04mVZ0wV0NTcsbWJwYbIkyyZalO9sxlp6ps2jAsRBQWatOu5YJIonKFeann1OVKEx77fKxXVigA_bUS5uk_FVEd6XZzISoSW-Nofx0nawGBTCDZw_GPw0JybwRCjpoPz2PPy6a4431YSJce7L38qL6ggsCJliWHeY87XYtQEz0iNAUosAvRIRcKFRuxDK0bmg7Cb4TrLjdDOpC9ilZPd-6DdqWwqVVdaYtqIBkDjh0HPejt9gShmskHqxuRY_ptkvNkHGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/574dd70fc0.mp4?token=Y-m-_R3usXyhVyZDBv5IeKw6KiVr-SBb2K2nTDOocCgcWrKdzjX2omXbvZULOiyD5oG0Oz5I-MBXoBuQ04mVZ0wV0NTcsbWJwYbIkyyZalO9sxlp6ps2jAsRBQWatOu5YJIonKFeann1OVKEx77fKxXVigA_bUS5uk_FVEd6XZzISoSW-Nofx0nawGBTCDZw_GPw0JybwRCjpoPz2PPy6a4431YSJce7L38qL6ggsCJliWHeY87XYtQEz0iNAUosAvRIRcKFRuxDK0bmg7Cb4TrLjdDOpC9ilZPd-6DdqWwqVVdaYtqIBkDjh0HPejt9gShmskHqxuRY_ptkvNkHGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دختره باباش براش یه مرسدس بنز به عنوان هدیه گرفته و پشتش نوشته خواسته هایی که شما بخاطرش تن به ازدواج میدین رو، من توی خونه بابام داشتم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146623" target="_blank">📅 11:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146622">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOel9bksFEsA8qVsTUEYwq4lxV4uxf0ydWac1fdVWJW4jjusox3U40QnF3b2CjPSRAw-VQ2pp_u-glwegDoISrPMgnLu9aMqmhilYV8QCMA0SuwmAJCR4SGBJ1sIUQj8QiUEQk-dIewrPQFRXUchQxL3rsL_KHDvmgBoJyPUuUa61ZmKzeoFV6D8DShoFKC4_qWVVjpJiuRrbo-NxkiogxpZq0q0w-3ST0qpJdsD7Ci_IPUjBWY2ROWa3b386mDoH_sahXzTAh5-5sq_-eZyUJtE4r5GA9CjOLhA8jhMnYn-cYOwVpJdKji8b94FKwON-qppKY2eqizoDkBYvAc7oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار ناشی از عملیات اسرائیل شهر المنصوری در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146622" target="_blank">📅 11:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146621">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9djdnk4W_HI2po922aSt4DK6zZOVUUiFOaB7lL5djoTUUtAGdFFRLoJ8m1Db6_u9MGp7037hAODdLQl4j68HowBzMxbGvUI2bj6xKVcT-RSZpbLbQE0l7HHk3zLY_hUqjwMxCH2tFxFSU5oS1jBSG4D468CPSizglSK6tjYmxHfaGE9IxtFLCoixg19ICDOn97V2dbGrcnV6czY07eXbiupOQ727c6OGF2J90X2CZ4o5myRJEWOirvm44aBsnagu2gOCnK7Bd4YDzSWEC4plRCZC5k5pNYjzp3vmexZpO--UYldw2ONEKG0rh-rRunlz30ds8vMyYNJRZKolfFZig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده تصمیم گرفته است که سازمان‌های فرانسوی را از یک برنامه کمک مالی وزارت امور خارجه که از اولویت‌های دولت ترامپ در اروپا حمایت می‌کند، حذف کند. این تصمیم به دلیل نگرانی‌ها در مورد اتهامات مداخله خارجی قبل از انتخابات ریاست‌جمهوری فرانسه در سال ۲۰۲۷ اتخاذ شده است، طبق گزارش رویترز.
🔴
این برنامه، مبلغ ۱ تا ۳ میلیون دلار به گروه‌هایی که در زمینه‌هایی مانند دموکراسی، آزادی بیان، مهاجرت، سانسور و حاکمیت ملی فعالیت می‌کنند، ارائه می‌دهد.
🔴
وزارت امور خارجه اعلام کرد که این برنامه هنوز در حال بررسی است و از تایید یا رد این موضوع که آیا گروه‌های فرانسوی از این برنامه حذف شده‌اند، خودداری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/146621" target="_blank">📅 10:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146620">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
به گزارش رویترز، پاکستان و ترکیه تصمیم گرفتند نیروهای خود را به یمن نفرستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146620" target="_blank">📅 10:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146619">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lj-_Ji0vKQosAl3EgL2BPz1eC9-v_YnHn-5pS4AceI-3QTIm5bG9aStt8DgNCBXtipJi-p1gnttZu7_RLNn50-Yg-NPdz4YvP4ia4qHlw3CNEurtRUqWKb7CIiHACtK9LFRDcQr8gaThDhtVVCuQPc0sqeQAfylmEM7Bj4zM7YmkUoaLBc7cilfJ0aH_XyDCGmpPaAP2e-kxpjqWV0vJf6rIPToxhwN4g8YQ1OyrEKkQLJRRKeo0-0AW1CW1RipIGl10EJYSUIRXT91A6YjiCP7X8kWzfW2wm11ryUsh4M9UOOqqSigxlu4wzToZFrEetYWxOVk_dS4LB-3ySD-Lsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارشات منابع تقریباً با نقشه اگر مخا هم تایید شده بدانیم، مناطقی که بدست نیروهای انصار الله یمن افتاده، اینطور است. جزیره زقر در سمت چپ تصویر بالا هم که مشاهده میشه طبق گزارشات مواضع نیروهای مورد حمایت سعودی چند مورد هدف حملات موشکی و پهپادی نیروهای انصار الله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146619" target="_blank">📅 10:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146618">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a63e09cd5c.mp4?token=ovtinmC1Th8tba8oEwRRWPUE_41XabTrMq_2JrYtHfiM8lOtJhLJJilur5UZYvzJ6nKxXufqemxLaP_dhS_mvltyaMuUt62_NB_MOdAdSEVrpydiJxNEgBRjUbKJO1v3rnz8ZXh5OIVS16Y_e1P-JaNbNfgmThhD97z-Ocsywc69GvUACSiR0cm6ra2JdyMR6Ftf8n26-inEV_WzdZxcY5XNCxR4lVuACxe1giNHNC6qoRKv8-jlzMp-vzZ4xSbcYwcOjJY_fVCxZ4Z0pBqB8eFlH8iBIwGoIMWYOHT2D5G5SNIqzqQHaiXAPSwSr8YePYJ-jH1E2vFGtXFAb5ywxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a63e09cd5c.mp4?token=ovtinmC1Th8tba8oEwRRWPUE_41XabTrMq_2JrYtHfiM8lOtJhLJJilur5UZYvzJ6nKxXufqemxLaP_dhS_mvltyaMuUt62_NB_MOdAdSEVrpydiJxNEgBRjUbKJO1v3rnz8ZXh5OIVS16Y_e1P-JaNbNfgmThhD97z-Ocsywc69GvUACSiR0cm6ra2JdyMR6Ftf8n26-inEV_WzdZxcY5XNCxR4lVuACxe1giNHNC6qoRKv8-jlzMp-vzZ4xSbcYwcOjJY_fVCxZ4Z0pBqB8eFlH8iBIwGoIMWYOHT2D5G5SNIqzqQHaiXAPSwSr8YePYJ-jH1E2vFGtXFAb5ywxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر لحظه رهاسازی مواد منفجره توسط یک پهپاد اسرائیلی در شهر بنی حیّان در جنوب لبنان را نشان می‌دهد؛ اقدامی که به نظر می‌رسد در آماده‌سازی برای انفجارها انجام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146618" target="_blank">📅 10:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146617">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VL9Zq3PPyho96ca6ALvF-_6AN2afC95_Ivt6IdrcEhwm4g8s01PaateH6dU81TDW7UBDOoCRmGmBvGoDq0lo1nePVplEzoSVQNvCBFAMBDPDGaXUMXoGaFwvw0K3ltlP0769oq_GyhC87CMnYQGYYpAThm9MB3DEcHvX4G7E5sAyaIvnuw5MnGtLV68YqmgAffRkQLS0xJ3Mu5BJPV8t4MdLju2DAL0ZLh4_UwI2sdyt63V9MemsFU_O4JuE-CawZy7JEgWVJZtJ00PN0QM0LhHgBCyKeTXtxdy2oguEnwrLjMD-BR810bO4CESX7C27nJi9LT-PfFrQnaYHTFrubQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توپخانه اسرائیل روستای کفرشوبا در جنوب لبنان را هدف حمله قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146617" target="_blank">📅 10:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146616">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
یک رسانه ترکیه‌ای: نیرو‌های انصارلله (حوثی ها ) شهر المخا را تصرف کردند و حدود ۲۶۰۰ کیلومتر مربع از مناطق یمن را به کنترل خود در آوردند
🔴
کنترل المخا به انصارالله اجازه می‌دهد تا از نظر جغرافیایی به تنگه باب‌المندب و مسیر‌های کشتیرانی بین‌المللی نزدیک‌تر شود
🔴
سقوط المخا به معنای از دست رفتن مهم‌ترین پایگاه نظامی و لجستیکی عربستان در سواحل غربی خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146616" target="_blank">📅 10:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146615">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
دونالد ترامپ درباره نظارت نیروی فضایی آمریکا بر کوه کلنگ
:
«به لطف
نیروی فضایی آمریکا
، ما می‌توانیم همه‌چیز را ببینیم. حتی می‌توانیم نوشته روی لباس آنها را ببینیم؛ محمد الفیاض، محمد العزوری.
🔴
می‌توانیم آن را از فضا بخوانیم؛ باور می‌کنید؟ از هزاران مایل دورتر.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/146615" target="_blank">📅 10:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146614">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f498f58530.mp4?token=nldc6oqBcwWuJEM8g6z1-hkzGSWD9IgyievpZ_iGmknmbItl1zo7BKbyTQVH_ojG1AVgXCsUEua8GTcjvwJtqpFHgwMVgZguYOYp6EshO_wNFdWGpAYIRT6N3yGCu76MU8c9oS7KZ13Ya-tMVG3g2bdFiqZ6FQkaNTjBuifTq6ebbRfl-PFkyENqduvGpcdOTg5b3Bsh5FUevhuZE6VVVGmNRKAXNxUT_24Ir0tJ4fG-8WgjHSrcKzY2jEmLwXQv7OhBrghvYE-_a2pSmsxe6gxEWRTEEbLwbMC-c969aDXAhe1zk9fiEUXGiTXuODncS5sZLu9d4PU5pSQXjLrMTVRMN4htOApNXRmFpr-MweKzOBryalhhWf0adJE3B-2RGjiNxcAQcaF0pixiHV9Ik_pet6z2GgDOognLCAwo2nma46VEgLUnbCArunv6YFmNam_hNzGgFLtz_kcyeWqqHlWddBVbxH9uPD2w9Q3YsyMMyTdTVh3ZuiSUMLy67fWRl4KUwyj-i0glOO2zMuWXdiBgtBQod9ktXmN5X0wGwyGdkzX10pdf7iuc465y_6ijIqW8JiCHEGdgntdeei7nHdLS7q_CG5PN8kqq1ImMtIEwLHbhwlnuszIzMtuP0GfjlIatpxRK6JkPbomK-2FC_lNLAIXn-Hvchuj4WHnrcz8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f498f58530.mp4?token=nldc6oqBcwWuJEM8g6z1-hkzGSWD9IgyievpZ_iGmknmbItl1zo7BKbyTQVH_ojG1AVgXCsUEua8GTcjvwJtqpFHgwMVgZguYOYp6EshO_wNFdWGpAYIRT6N3yGCu76MU8c9oS7KZ13Ya-tMVG3g2bdFiqZ6FQkaNTjBuifTq6ebbRfl-PFkyENqduvGpcdOTg5b3Bsh5FUevhuZE6VVVGmNRKAXNxUT_24Ir0tJ4fG-8WgjHSrcKzY2jEmLwXQv7OhBrghvYE-_a2pSmsxe6gxEWRTEEbLwbMC-c969aDXAhe1zk9fiEUXGiTXuODncS5sZLu9d4PU5pSQXjLrMTVRMN4htOApNXRmFpr-MweKzOBryalhhWf0adJE3B-2RGjiNxcAQcaF0pixiHV9Ik_pet6z2GgDOognLCAwo2nma46VEgLUnbCArunv6YFmNam_hNzGgFLtz_kcyeWqqHlWddBVbxH9uPD2w9Q3YsyMMyTdTVh3ZuiSUMLy67fWRl4KUwyj-i0glOO2zMuWXdiBgtBQod9ktXmN5X0wGwyGdkzX10pdf7iuc465y_6ijIqW8JiCHEGdgntdeei7nHdLS7q_CG5PN8kqq1ImMtIEwLHbhwlnuszIzMtuP0GfjlIatpxRK6JkPbomK-2FC_lNLAIXn-Hvchuj4WHnrcz8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ: «دو نکته وجود دارد. اگر من
برجام را لغو نکرده بودم
و اگر با بمب‌افکن‌های زیبای B-2 خود به تأسیسات هسته‌ای آنها حمله نکرده بودیم، آنها همین حالا سلاح هسته‌ای داشتند.
🔴
اگر آنها سلاح هسته‌ای داشتند، من با رهبر عالی ایران تماس می‌گرفتم و می‌گفتم: «آقای رهبر، حال شما چطور است؟ کاری هست که بتوانیم برای شما انجام دهیم؟»
🔴
نه اینکه مثل الان، حسابی آنها را بمباران کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146614" target="_blank">📅 10:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146613">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=SGhiojc6na_sQy_R332z-d8wvLSzzCCdvtaPbR2mZKAY-VAOZ7UJRfQjts7M043itsHPem5SaszMOYHoqq2dzqit5TOhDtHAd9jmWuGCevNsiViemPqVXw04VH1IM23a-rkyPGLr9gBDXZiPlNuhRNbhGpY3WwWhOHrutsxMpYeanoxdYCCP0Hv-W14uYSb2uJ3qj3ds3FWvFVEW-xj0QLMb-NdEXMBqa_dof6uRbY-UMGMKvicFzK-f8Bjf-tZVU3sk5vHrH6dNIQCVic8y8YkGBoFhnOQXV0FfADE19DOiqsY-0eWml4ZY1XzS4pcFwz6862cm2KA2oVjEgB3mq6rWJVlpQPW4SDTb3AmucwQvnroYmsBvmNRSoWSa32XzUa6u6pxXtlh8aAc-mLtAClvaU7eCOsxZONJtoO1U-SdPMZl_MuPIkRSBb6wl171oaFw6EgrMML9UC6XFyoCVOJEP_R_IF0QBCHH297Arzx39lR-8tVteF1LQ_DSCKwBOPkmWMw_ODa-hQgl4fPlJNxH-UeOp5ov2rXpVtK_Cz3MIQnpBBbJTMJNXAYB2UvrJ2ZRvmSHiPD9J357VTgAn5WYs-OVfbjusdi3lFoOkj_4bApCl2_p-_5I4gFptGHaZI-R_olWBoWqDSmdTyUShsL9fSJDPcgLBtlOje-P3E7c" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=SGhiojc6na_sQy_R332z-d8wvLSzzCCdvtaPbR2mZKAY-VAOZ7UJRfQjts7M043itsHPem5SaszMOYHoqq2dzqit5TOhDtHAd9jmWuGCevNsiViemPqVXw04VH1IM23a-rkyPGLr9gBDXZiPlNuhRNbhGpY3WwWhOHrutsxMpYeanoxdYCCP0Hv-W14uYSb2uJ3qj3ds3FWvFVEW-xj0QLMb-NdEXMBqa_dof6uRbY-UMGMKvicFzK-f8Bjf-tZVU3sk5vHrH6dNIQCVic8y8YkGBoFhnOQXV0FfADE19DOiqsY-0eWml4ZY1XzS4pcFwz6862cm2KA2oVjEgB3mq6rWJVlpQPW4SDTb3AmucwQvnroYmsBvmNRSoWSa32XzUa6u6pxXtlh8aAc-mLtAClvaU7eCOsxZONJtoO1U-SdPMZl_MuPIkRSBb6wl171oaFw6EgrMML9UC6XFyoCVOJEP_R_IF0QBCHH297Arzx39lR-8tVteF1LQ_DSCKwBOPkmWMw_ODa-hQgl4fPlJNxH-UeOp5ov2rXpVtK_Cz3MIQnpBBbJTMJNXAYB2UvrJ2ZRvmSHiPD9J357VTgAn5WYs-OVfbjusdi3lFoOkj_4bApCl2_p-_5I4gFptGHaZI-R_olWBoWqDSmdTyUShsL9fSJDPcgLBtlOje-P3E7c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ: «فکر می‌کنم باید نام تنگه هرمز را به «تنگه ترامپ» تغییر دهیم.
🔴
خانم‌ها و آقایان، اعلامیه‌ای در این‌باره خواهم داشت. آن را تنگه ترامپ خواهیم نامید و مطمئنم رهبری ایران از این موضوع بسیار خوشحال خواهد شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/146613" target="_blank">📅 10:16 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
