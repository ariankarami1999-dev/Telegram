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
<img src="https://cdn4.telesco.pe/file/SnJb7UlggJViluTN9Vr-LAUnH7tKgyqnXSSsyEJxKlWbLfo4UvSxevUFfunxaIzm1_K2WpPqxk2BshIy8rQj4RH1PpPmuuUKLXR-jY8jvSPQ2Qhzov6ZJv48zxZDHvA8x-C2-m-Nuq5z3B84AyKtxM-1rBMyRtncM1RpQVTppH3YlQQb9rjCbHa5Pvm6CilDfqlSbU98FOE3i0ZNhUfVMzD6K7iBWOx2M-1EUjM-Le2YoW5JSqhpL5PFISh8oBUWLjHN_GHS7MDBQcdHFcELk8IzY9UpqT9PZqXu2Qt5czM5OFZkpG8Anv2MN45N2Yn-P-Syge9KnnADGeHTUBnw7A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.26M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 00:13:13</div>
<hr>

<div class="tg-post" id="msg-657016">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKKgl3WLHlunI_60jlnCn9VUzxONO7lO7jnANKlN9qxsRd74CIsBcIuOxfQgSnXOQ4W7GB4VoN92xxqF7Qo8UCeixjFAT9bVdgXi3BfHSMu-Ntz6ft1QRqnTgTfhFGlL96RsdF3AcaZJbmuKXXBVlpSeDPrTRPZiUg5OpisV-MXMtnBRH8JHS7TpxjlJKy1exvoMpiexvYQSBU9Sq2N4SinOvnx8POR5fwl7tpzVNilczhXfwEe3K0UfpO3u1Fkhuuc5z1u5xEenbc16KVMlAPy3vBldHUqnc6AjvvXDtJ4-wchyP6gAew4vHS6eUY-jRfu12FlBwKZEjGM2MjS62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
עוקבים אחריך, אל תטעו.
تحت نظری، اشتباه نکن
#WillPayThePrice
#هزینه_خواهید_داد
توییتر خبرفوری را دنبال کنید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/akhbarefori/657016" target="_blank">📅 00:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657015">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ ایران خداقوت</div>
  <div class="tg-doc-extra">مهدی رسولی و محمد اسداللهی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/657015" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
خیابان خدا قوت
میدان خدا قوت
جمهوری اسلامی ایران خدا قوت
ایران خدا قوت ایران خدا قوت
اینجا فقط ما به خدا میگیم ابرقدرت
🎙
#مهدی_رسولی
🎙
#محمد_اسداللهی
مرجع رسمی مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/akhbarefori/657015" target="_blank">📅 00:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657014">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ترامپ به شبکه کان:ما می‌توانیم پس از ۳۰۰۰ سال به صلح دست یابیم
🔹
«فکر می‌کنم اسرائیل به اندازه کافی پاسخ داده است. دیگر نیازی به هیچ اقدامی نیست. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/657014" target="_blank">📅 00:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657013">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
منابع عراقی: نیروهای امنیتی در عراق هشدار جدیدی در نزدیکی منطقه سبز و فرودگاه بغداد اعلام کردند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/657013" target="_blank">📅 00:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657012">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
پدافند در بخش محدودی از غرب تهران فعال شد. این اقدام به منظور افزایش امنیت و آمادگی در برابر تهدیدات احتمالی انجام شده است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/657012" target="_blank">📅 00:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657011">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlmwwZYtvRqv_TfwNuYjYwY31yh1EZbq7gl_P86eI2thqcTCkf1MCr5LHF86fFqT3_z4MtyAfC9b_uPSjnSpXP6iOV9r6UJ7KOtlvE2dBeunvT0NcSV_e1--kOiExnv8TJwfRPbGZ_CWPuVJro8cI5aFWWZcQ2rgnRtdoNsbhP1gy9YrSJTYqBwtvJn6_f5zHmuRUcOoGFzWo5UQLtcyYc4rBIMRqOkwL2LfC34-JibBk5mm-HcLONgKEJqPyoTMawr-g1PBuzbTCfIAbC29CmJjSezT18KXtX1yDIPXIvvMJYrNwV8L37H-BScxg8RiGqXCiOHwuEUDQai2WOhoug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">*مشاوره و تسهیل گری در فرایند اخذ وام های بانکی*
نیاز به وام دارید اما در میان انبوه بخشنامه‌ها و فرآیندهای اداری سردرگم شده‌اید؟
کافی‌نت آراد با جواز کسب رسمی، اینجاست تا مسیر دریافت وام‌های معتبر بانکی را برایتان هموار کند.
✅
خدمات ما:
• انجام مراحل اداری و پرداخت وام در کمتر از ۷۲ ساعت
• مشاوره و بررسی شرایط شما برای انتخاب بهترین وام بانکی
• ثبت‌نام آنلاین دقیق و بدون نقص در طرح‌های تسهیلاتی
• آماده‌سازی و تنظیم مدارک مورد نیاز
• پیگیری روند درخواست تا دریافت پاسخ نهایی بانک
*
📎
برای شروع، پرسشنامه اولیه ما را از طریق لینک زیر تکمیل کنید تا کارشناسان در اسرع وقت با شما تماس بگیرند:*
https://survey.porsline.ir/s/CwzLVsEN
https://survey.porsline.ir/s/CwzLVsEN
https://survey.porsline.ir/s/CwzLVsEN
کافی‌نت آراد؛ پیشگام در تسهیل امور بانکی شما
🏦</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/657011" target="_blank">📅 00:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657010">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c7647a222.mp4?token=c-y_oLdUPLRsQywk1oQNyE5liksf2wSuu0pniGstFIRL4-N07O6bClZ6kuVh39l3jT-IK3wgLAU4tA5sdEcTHdLSL33RNw-UxroDbwOixFRuiMj0SqAk4GSYMKW-mAelaTh7uGnJp54HICI75wVNwbpgVe4m6bRaR8eWai70xcKx0av5J4X2Ls1SBks2Y9UK4RhyD4PD1QzmSstXFWaS8EQ_Fl_nMFwqXAQhGlJq7qhgMednn7uypNPjVrX59rO2v_-ria3ITFPz7EnSR28R7F58CHXa8YQ7w4tQomgj3zKMhUy7N9ydRQESOgrAK41UxAjlmTq-5bywsK4SHrkkag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c7647a222.mp4?token=c-y_oLdUPLRsQywk1oQNyE5liksf2wSuu0pniGstFIRL4-N07O6bClZ6kuVh39l3jT-IK3wgLAU4tA5sdEcTHdLSL33RNw-UxroDbwOixFRuiMj0SqAk4GSYMKW-mAelaTh7uGnJp54HICI75wVNwbpgVe4m6bRaR8eWai70xcKx0av5J4X2Ls1SBks2Y9UK4RhyD4PD1QzmSstXFWaS8EQ_Fl_nMFwqXAQhGlJq7qhgMednn7uypNPjVrX59rO2v_-ria3ITFPz7EnSR28R7F58CHXa8YQ7w4tQomgj3zKMhUy7N9ydRQESOgrAK41UxAjlmTq-5bywsK4SHrkkag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باورتون میشه این‌مدارس در ایران است؟!
ویدئوی بالا به هیچ وجه از دست ندید.
دبیرستان دخترانه هوشمند مدبّران برنده جایزه بهترین سیستم آموزشی خاورمیانه
"مدارسی از جنس رشد و شکوفایی"
🟢
این مدارس توسط
دکتر علی میرصادقی (روانشناس) طراحی وبنیانگذاری شده است.
✅
همین الان جهت ثبت نام در آزمون ورودی و کسب اطلاعات بیشتر به آیدی زیر  در تلگرام پیام بدهید:
@Modaberane_Barsa
یا عدد 4 را به 3000909030 ارسال کنید .
توجه:این دبیرستان ها تنها در تهران دایر است.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/657010" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657009">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
حزب‌الله لبنان: ما تجمع سربازان دشمن اسرائیلی را در مجاورت قلعه تاریخی بوفورت با موشک و توپخانه هدف قرار دادیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/657009" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657008">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
اسرائیل: آماده شلیک موشک‌های بیشتری از ایران هستیم
🔹
ایران تلاش کرد پس از حمله ما به ضاحیه بیروت تعادل جدیدی برقرار کند و ما اجازه نخواهیم داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/657008" target="_blank">📅 00:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657007">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
بعد از قطر آسمان عراق  هم بسته شد
🔹
الفرات نیوز نوشت که در پی حملات ایران به اسرائیل، آسمان عراق بسته شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/657007" target="_blank">📅 00:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657006">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ارتش رژیم صهیونیستی:  اکنون به شهروندان اجازه داده شده است که از مکان‌های حفاظت‌شده خارج شوند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/657006" target="_blank">📅 00:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657005">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAdSlpeGECkEQO3vElXN5C1SpG3DXjd2dTd7dIox2UNlsgygHWf5NNJ23Nl4RUchs2tkb6aRBpEyDMfFjONBpoUcSoTx4pd2CK90j5RIYVNuqt1845TJn1ecBdrPu_1EaYNRh2bVkYsc94pEGLT4RuTxVN8JO_x3RazABeZQwWudZIag5h0XH5dwitwHlkPZM_rqC5JA3-fEYsdMutS6bBD8asOg9gPxTNEzvW5OPZgI03jj2bCDgqd497puZMwG52WsV4-StSUQnVFsupWZGnVzva8bFIT_jfQaFG6-_vINOM84nJ1BBh9Sk2xRu8VjgS8iRjMZFoWW9KIwOe5iPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/657005" target="_blank">📅 00:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657004">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAgeoCWbkh8e-q5XTsIgsq72ywaAQcIzNSrjaZD220Cpkv5AGBBLzMrfMfW8AofWnVMsd3WSAzSlqqisoKYwWTKyq8VxjlmX5bV-uA6uDkk5SqBfXKcYUnUrJwPNG7EqsG37PowvcxYdbOJy5AjQUaXSOh9GNnkOa4FBJZzZUSZQSbpXSdf30TEOI5XAMovA8IISu4K3Kx_8TP_xb9HNSr4myPHbkehyBYnkwtCpZRjjltuCp0XWiXVrVHFgKBJ79uieJwi52noVMh7_lyU3y2lr23_ncmDEfCz55Z2wzOyMsRH1ybZ0ShaEKCOViX49Vhqg85MFuPFCS3Z6QqzlCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک پیام برای سید مجید موسوی و اپراتورهایی که امشب پشت لانچر نشستند و قلب تل‌آویو را هدف قرار دادند بنویسید
👇🏻
🔹
پاسخ‌های شما در خبرفوری منتشر می‌شود و به دست سربازان گمنام امام زمان خواهد رسید
ویراستی خبرفوری را دنبال کنید
https://virasty.com/r/BWcv</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/657004" target="_blank">📅 23:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657003">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUV-22RHziRvRlmZEimaWwUd--mBGD5XSy8JGoefFlLsF9Jmtu4-HbWJnBUh0Fv-s1EZsDre1NBSpfgNKIGVxJSRxGoc4QLzphjSJmxN2qnaFvTL27wfNZHdfaAjkOUwb3Iox0XND-eWyoDdjdj8yOS6Ds_8r93N_jkmRnnq3aEgxSieo-H10BhwC2Wcplm2RFFLv-2oMW4ptzDBi0g2qYC-Mpces5mnmDaLO9x_EVILskJ9nrBr6LVglwRiDHc0bBb44S4djW9Nkz7cgtVLT_eOrNZ73M9pO_AcTK5Jm0xKPOFzbtw7K2LYEMVDQB_F41cGzf-cdCc1HdwmVApfsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوشته روی یکی از موشک‌های شلیک شده سپاه: ما درحال مبارزه با فاسدان جزیرۀ اپستین هستیم
#جاسوس_موساد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/657003" target="_blank">📅 23:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657001">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
هشدار ترامپ قمارباز به نتانیاهو توافق را نابود نکن  ادعای ترامپ به شبکه ۱۲ رژیم صهیونیستی:
🔹
هیچ‌کس در حمله موشکی آسیب ندید. اگر نتانیاهو پاسخ دهد، این وضعیت ادامه پیدا خواهد کرد و ادامه پیدا می‌کند.
🔹
نمی‌خواهم این موضوع توافق را از مسیر خارج کند. هر دو طرف…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/657001" target="_blank">📅 23:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657000">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ارتش رژیم صهیونیستی:  اکنون به شهروندان اجازه داده شده است که از مکان‌های حفاظت‌شده خارج شوند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/657000" target="_blank">📅 23:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656999">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa5acc5df7.mp4?token=mqQjEU5oggHfsCNl5SR1ZRqhKCIBSkMcJT-Y08v7W0KSx3rr3cnyIekNdQkr0N_e_LRmzAevYFSx-xdc3CAQFEohqSnAO98DlYgBbh4dzS4J9qsyU6g1DOI0eaog90k-USCX3PskmHD-PE-hTAN9j5wF1FgP05PiP6n8iXVRKLiqV9upmfsx7XmHJyayAblgA2MMO_g01Lrg8Cj2fYp1YtHCIKMlQiBaGslLRqJR2F45JYFLf3ZP4ENR5kkeHON4UuDTcT85ypw-fZWOlc6fFT1sDP2qjWD8UxwV_iLWgcLe8SWk3WnEAV68GnkMLbXSaEhWVKweeSk06mZPlmc86A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa5acc5df7.mp4?token=mqQjEU5oggHfsCNl5SR1ZRqhKCIBSkMcJT-Y08v7W0KSx3rr3cnyIekNdQkr0N_e_LRmzAevYFSx-xdc3CAQFEohqSnAO98DlYgBbh4dzS4J9qsyU6g1DOI0eaog90k-USCX3PskmHD-PE-hTAN9j5wF1FgP05PiP6n8iXVRKLiqV9upmfsx7XmHJyayAblgA2MMO_g01Lrg8Cj2fYp1YtHCIKMlQiBaGslLRqJR2F45JYFLf3ZP4ENR5kkeHON4UuDTcT85ypw-fZWOlc6fFT1sDP2qjWD8UxwV_iLWgcLe8SWk3WnEAV68GnkMLbXSaEhWVKweeSk06mZPlmc86A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش زنده خبرنگار بی بی سی از بیروت: موشک‌های ایرانی موجب خوشحالی و هیجان لبنانی‌ها شد؛ پاسخ ایران خیلی زودتر از انتظارها انجام شد! همزمان، حزب‌الله هم رادارهای اسرائیل را مورد هدف قرار داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/656999" target="_blank">📅 23:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656998">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/455b452e02.mp4?token=TmXJKwd8k8IQIZmXZfzYA6gBeMe-ygxCvWI1wY_lErIuXFEOlC1J4rtVZpK-l-PYYW-O99TOkM4FfV7DzCAYtLKVy4egJKh9TPxoZFSJgedqoCLV-1BTHzfXwdzpM48YE_JQQvWnXaHpuj5SJKQjfsOrzuX1xR_as0CCuechwV6eQnCNMg3jBxq9srYYLIcLSez0UU2G4Bvlj74qc8DBuJC8guar0kr8M5DwQ3I1xgg9ILhwww8JzR8e9O-GRJDXk9_WPimtMBjVvD6rBrpDl8fJvJTVs2DF-nqbxiuM4C3r-xHXcpeUcbKlF2UfuTLSmwWW_kpNUtRRVE6aGtqU-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/455b452e02.mp4?token=TmXJKwd8k8IQIZmXZfzYA6gBeMe-ygxCvWI1wY_lErIuXFEOlC1J4rtVZpK-l-PYYW-O99TOkM4FfV7DzCAYtLKVy4egJKh9TPxoZFSJgedqoCLV-1BTHzfXwdzpM48YE_JQQvWnXaHpuj5SJKQjfsOrzuX1xR_as0CCuechwV6eQnCNMg3jBxq9srYYLIcLSez0UU2G4Bvlj74qc8DBuJC8guar0kr8M5DwQ3I1xgg9ILhwww8JzR8e9O-GRJDXk9_WPimtMBjVvD6rBrpDl8fJvJTVs2DF-nqbxiuM4C3r-xHXcpeUcbKlF2UfuTLSmwWW_kpNUtRRVE6aGtqU-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی قرارگاه خاتم‌الانبیا: صهیونیست‌ها در صورت پاسخ به اقدام ایران با ضربات کوبنده روبه‌رو می‌شوند و حملات ویرانگر علیه رژیم و حامیانش آغاز خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/656998" target="_blank">📅 23:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656997">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
گفتگوی تلفنی عراقچی و فیدان
🔹
طرفین در این گفتگو درباره آخرین وضعیت روند مذاکرات ایران و آمریکا بحث و تبادل نظر شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/656997" target="_blank">📅 23:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656996">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ترامپ افسار نتانیاهو را کشید
🔹
با نتانیاهو تماس خواهم گرفت و به او خواهم گفت که به ایران پاسخ ندهد #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/656996" target="_blank">📅 23:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656995">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1eb172af.mp4?token=szHxHQbmpHn9Ifdpv9o8uQ4ZM1h06uedR-qG82GwXRIoYk7pXD2sTqXBuwmm8b2wO7Ue3ZFXceuuIfzcST1w3Z75RAAPiC9mFcduPr5txLkIDICfdktuXzls939VrAZc63CCxwhLnB7WThEvrdu0OcVE_ZsTaLPO0pOU2WhMWwozpjCmQl5dBMglczv9pYleJKZzGH6MJh7eZ-gFGNkUCzXRm9ZhoaMKUgmGEYwWureefCpkYwd1-mNrVn7IP8nG-Kx2jnKD5blejMiGZhASWi1KXMmGpbAPR5PvtuazFWvsWN1mkObR-VtovFE0Fq-jScPgrUHQ0WJk_tcCnn5YYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1eb172af.mp4?token=szHxHQbmpHn9Ifdpv9o8uQ4ZM1h06uedR-qG82GwXRIoYk7pXD2sTqXBuwmm8b2wO7Ue3ZFXceuuIfzcST1w3Z75RAAPiC9mFcduPr5txLkIDICfdktuXzls939VrAZc63CCxwhLnB7WThEvrdu0OcVE_ZsTaLPO0pOU2WhMWwozpjCmQl5dBMglczv9pYleJKZzGH6MJh7eZ-gFGNkUCzXRm9ZhoaMKUgmGEYwWureefCpkYwd1-mNrVn7IP8nG-Kx2jnKD5blejMiGZhASWi1KXMmGpbAPR5PvtuazFWvsWN1mkObR-VtovFE0Fq-jScPgrUHQ0WJk_tcCnn5YYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه شلیک موشک‌های ایرانی به‌سوی اراضی اشغالی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/656995" target="_blank">📅 23:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656994">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
بر اساس گزارش‌های اوسینت در شبکه‌های اجتماعی، دست‌کم سه موشک ایرانی به اهداف خود در سرزمین‌های اشغالی اصابت کرده‌اند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/656994" target="_blank">📅 23:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656993">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a33e8867c3.mp4?token=Mzy6j-Dd4txuV6BLRmW5Omcjg8b39iLwUbSi-kaSh6TALMiOOT4z2bdxArf643l3sBIHM-nKildpB9C0TdCVDTrQ8beJp28cMxNZjqJ7cMV8hI6pztulTL3zp6cSZkfHY2ZWGaSSdqzbYnRsT_OuEmncp6pMvo-6aCF0kuubU3G1ca1qQfwNd1WzGOuQZbzyPDtIF556WpoZU02NHeBuExjbL-BSQl0iRA6Lpyhy_zhAXPVwyBmxPC5KKyfG0QK09nObUsJ20AGol7GP0N9klE0boK5rkXMmuF8IAKcrX1usBsh_eXcxKJuTy-I-irzgImJipf9v7UskmZnWsh26WWVcB502ofhQM5oLxCXreE3NnAtz_XtZL3xJEzdtGozBUyMS8_v38aALxerMYGzgoPa-FjFJqdpFgi6AGtreSGsng82Urj27loswaUmYWEoNJQhjXXq1D-AT0LSl58xj6AebDqCNM92PJutDCfG0mULN06XUfrAph6f9NP3qsJ4AMILCk7aI03KZvgyFWqNixQwbYIL7VNyc2QKxsHGDTUOJjPiCJlye9FXkyeio5KttR-7J49GdBhWzYQVPCkXC5436ZHSDms74UcHYKjeZl9EbOUtXGvOyp6WD02MN27Ee359-WJSe49WyyAZbbMbe0HwBs7Pftwa-iwlPpgdaSmU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a33e8867c3.mp4?token=Mzy6j-Dd4txuV6BLRmW5Omcjg8b39iLwUbSi-kaSh6TALMiOOT4z2bdxArf643l3sBIHM-nKildpB9C0TdCVDTrQ8beJp28cMxNZjqJ7cMV8hI6pztulTL3zp6cSZkfHY2ZWGaSSdqzbYnRsT_OuEmncp6pMvo-6aCF0kuubU3G1ca1qQfwNd1WzGOuQZbzyPDtIF556WpoZU02NHeBuExjbL-BSQl0iRA6Lpyhy_zhAXPVwyBmxPC5KKyfG0QK09nObUsJ20AGol7GP0N9klE0boK5rkXMmuF8IAKcrX1usBsh_eXcxKJuTy-I-irzgImJipf9v7UskmZnWsh26WWVcB502ofhQM5oLxCXreE3NnAtz_XtZL3xJEzdtGozBUyMS8_v38aALxerMYGzgoPa-FjFJqdpFgi6AGtreSGsng82Urj27loswaUmYWEoNJQhjXXq1D-AT0LSl58xj6AebDqCNM92PJutDCfG0mULN06XUfrAph6f9NP3qsJ4AMILCk7aI03KZvgyFWqNixQwbYIL7VNyc2QKxsHGDTUOJjPiCJlye9FXkyeio5KttR-7J49GdBhWzYQVPCkXC5436ZHSDms74UcHYKjeZl9EbOUtXGvOyp6WD02MN27Ee359-WJSe49WyyAZbbMbe0HwBs7Pftwa-iwlPpgdaSmU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی قرارگاه خاتم الانبیا: قبلا اخطار داده بودیم...
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/656993" target="_blank">📅 23:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656992">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
گفتگوی تلفنی عراقچی و فیدان
🔹
طرفین در این گفتگو درباره آخرین وضعیت روند مذاکرات ایران و آمریکا بحث و تبادل نظر شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/656992" target="_blank">📅 23:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656991">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilvwiRAM0_c7Nj6K4WPNUON3KlntbaaVu8XQi_hLI09bHQ_6V0575ggqjA7F2eGG_f25mz6-JdmKpEqyYkpUF48MAei7R4Tvtqpsxdr831t0wM6qVzQ3W3C_ReuLZo37_4GMBWlU6WnaKeU8Ushf7isP8N8-alGpzcUOEMdWT_KMvPR9OYoIaA-ODq8eKbZ-US0f3q3ro22SinoGYs3IqmzM0yTY-f5BMQvNc8CJHQ_SyKPvNM3TtWOzQqmglJL_bE__PS7TxCnso_nY2Jis1ZZMeLdOiFOf-oJFI3wJsEQAoueGvLFWe6uers0phrktXIWbv9WH3sE4Meb5XN_CfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
You're so scared that you're digging your own grave
🔹
از ترس قبر خودت رو می‌کنی
‎
#WillPayThePrice
‎
#هزینه_خواهید_داد
توییتر خبرفوری را دنبال کنید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/656991" target="_blank">📅 23:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656990">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
آماده‌باش نیروهای عملیاتی هلال‌احمر در سراسر کشور
🔹
در پی نقض آتش‌بس توسط رژیم اشغالگر در مناطق ضاحیه جنوبی لبنان و با توجه به احتمال حملات دشمنان، نیروهای عملیاتی هلال‌احمر در سراسر کشور به حالت آماده‌باش کامل درآمدند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/656990" target="_blank">📅 23:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656989">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ترامپ ادعا کرد که از حملات امروز اسرائیل راضی نیست
🔹
نزدیک به یک توافق با ایران بودم و حالا این اتفاق می‌افتد
🔹
ادعای ترامپ به فاکس نیوز: حملات اسرائیل با ما هماهنگ نشده بود #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/656989" target="_blank">📅 23:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656988">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07f9652347.mp4?token=R7JuQPf56coP1gHBasbadRrhN2xcUpeT2HsUTtVjgJ11yTO6HsjikfW04B1R7Rzrp1tn9gI5EQXra8YJrYa4CAZKlLdj0uFQZGlBcyFfl3SKNRwKCjSqfTZ5f1AMdGohevkmXPtjNK118d2B5kKS0s2w77IznHfIjrhLCIJNbIYgW3nn0qbvsNAlGFZoCnwDsY-tLqbH25CjCEtnPm-flISaHJ7S8NSUCjv63stFDyETtfkFH_oCx6H1uIshMsuXzWxPvveiLci4tlbA-ybn-2d8fCSDpi-yAlaRMXKRNTZwTvhaGHIP9G8jKoKHsNRQnY2isoDmdNWBgZDWNOUCvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07f9652347.mp4?token=R7JuQPf56coP1gHBasbadRrhN2xcUpeT2HsUTtVjgJ11yTO6HsjikfW04B1R7Rzrp1tn9gI5EQXra8YJrYa4CAZKlLdj0uFQZGlBcyFfl3SKNRwKCjSqfTZ5f1AMdGohevkmXPtjNK118d2B5kKS0s2w77IznHfIjrhLCIJNbIYgW3nn0qbvsNAlGFZoCnwDsY-tLqbH25CjCEtnPm-flISaHJ7S8NSUCjv63stFDyETtfkFH_oCx6H1uIshMsuXzWxPvveiLci4tlbA-ybn-2d8fCSDpi-yAlaRMXKRNTZwTvhaGHIP9G8jKoKHsNRQnY2isoDmdNWBgZDWNOUCvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر واضحی از لحظه اصابت موشک ایران به هدف خود در فلسطین اشغالی
وَلَا تَهِنُوا وَلَا تَحْزَنُوا وَأَنتُمُ الْأَعْلَوْنَ إِن كُنتُم مُّؤْمِنِينَ
🔹
سست نشوید و اندوهگین نباشید؛ شما برترید اگر ایمان داشته باشید.
🔹
سوره آل عمران، آیه ۱۳۹
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/656988" target="_blank">📅 23:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656987">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
یک منبع ایرانی به رویترز: اگر اسرائیل به حملات موشکی ایران پاسخ دهد، ما نیز قطعاً پاسخ خواهیم داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/656987" target="_blank">📅 23:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656986">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ: ارتش (تروریستی) آمریکا در حالت آماده باش است #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/656986" target="_blank">📅 23:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656985">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
سخنگوی سازمان هواپیمایی كشوری از بسته شدن بخش غربی فضای پروازی کشور تا اطلاع ثانوی خبر داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/656985" target="_blank">📅 23:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656984">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
عملیات روانی آشفته سگ‌زرد: می‌خواستم بگویم که توافق با ایران روز دوشنبه امضا می‌شود. شاید سه‌شنبه. شاید هم چهارشنبه... #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/656984" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656983">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
عملیات روانی ترامپ: ایران به میز مذاکره برگردد و توافق امضا کند؛ به دستیابی یک توافق نزدیک شده‌ایم #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/656983" target="_blank">📅 23:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656982">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
یک منبع ایرانی به رویترز: اگر اسرائیل به حملات موشکی ایران پاسخ دهد، ما نیز قطعاً پاسخ خواهیم داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/656982" target="_blank">📅 23:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656980">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
بعد از قطر آسمان عراق  هم بسته شد
🔹
الفرات نیوز نوشت که در پی حملات ایران به اسرائیل، آسمان عراق بسته شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/656980" target="_blank">📅 23:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656979">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
زیاده گویی ترامپ به فاکس‌نیوز: به ایران می‌گویم شما موشک‌هایی شلیک کردید؛ کافی است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/656979" target="_blank">📅 23:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656978">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ادعای اسرائیل: ایران ۱۰ موشک بالستیک به سمت ما شلیک کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/656978" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656977">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
زیاده گویی
ترامپ به فاکس‌نیوز: به ایران می‌گویم شما موشک‌هایی شلیک کردید؛ کافی است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/656977" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656976">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193dcdf4cc.mp4?token=XsUcSH6xpqeE37soK-eWMzSVawvqjC1iPjM7LSKKkD2lB0D4lipDsns6wJ4sRScN_v9nkZb1sl6EAywTCUV1ljSy3q6tf-jT4B2TA6YZjB93OL4RDlnik0wrrkNe2GI9BifTn2LDN9GMqBNE7zlp3xaQpar9uCabBqkEGC5CCT58V3yhtoQjKoi-Vub6Q9nR2uijbGMw-CvzFbrvZZUykwUhiUCjD-AyqCvOEVaEYYTfM_4NT_X8uqm5a7Mw_osn_w5Hg07V55ESkXGnFZ7jYDu59s0QUlDHnNL29zgtyNEsmD1Nm2zCW8w-mKUZ7WDP4V8jdpY7LPInPE_Kb5zb-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193dcdf4cc.mp4?token=XsUcSH6xpqeE37soK-eWMzSVawvqjC1iPjM7LSKKkD2lB0D4lipDsns6wJ4sRScN_v9nkZb1sl6EAywTCUV1ljSy3q6tf-jT4B2TA6YZjB93OL4RDlnik0wrrkNe2GI9BifTn2LDN9GMqBNE7zlp3xaQpar9uCabBqkEGC5CCT58V3yhtoQjKoi-Vub6Q9nR2uijbGMw-CvzFbrvZZUykwUhiUCjD-AyqCvOEVaEYYTfM_4NT_X8uqm5a7Mw_osn_w5Hg07V55ESkXGnFZ7jYDu59s0QUlDHnNL29zgtyNEsmD1Nm2zCW8w-mKUZ7WDP4V8jdpY7LPInPE_Kb5zb-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدان انقلاب تهران امشب در لحظه اعلام خبر حمله موشکی ایران
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/656976" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656975">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
هشدار مقاومت اسلامی عراق به آمریکا: هرگونه مداخله، پایگاه‌های شما را به آتش می‌کشد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/656975" target="_blank">📅 23:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656974">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83835975f0.mp4?token=lv6xE_thcfOVuohMH4CcWdSjNCVSa-9y5vHzBDF1Kke6uCRjWtmHXiXTa71BCA8vfIbZu3yWoE059ndz7Qdakgh-1eVwvE7nZyYG3XAArAX_rub-xis0oUAXq83I49fmwSDViZT7U9ABm-S8OnYPM5de65EfYUo5rIHQLoGWYOJIkEiMTOkqJFp47CoObOpJue1tbiKCKHtzIPdo_AZbe7_uUK7CvB9oa35lWL5NNXf7CWkhho4W3_VxIvqofpZwD0guVzODvfy0VSOx1ySVnmAwjSlPX9OmtKtGbQsOHAEse8HoBkLmv2k_XGAh-cc2CBnmR3Du5zbSUR1sXV5klJ3gSV0_78d3mUx-Vxh8T67bQpdbNnhmKrQzhMQ2hyewWVD-7qGe_NR5uXfgkCl7J9Jsd7PnuxYiU4E9aWgTChJVIiLv-1bGFNFgVHiPPEgHYtU8K8BDX1CmlSMHTgW1tJYmWtz7BLqe2epzX1OV47HOFfSWzP38TKie9xhhkOrNlTuUwanjdkpQ45bnXgabjvXoaOTAnzNa5qD4fiuO_mO19l7sjWZznMxq2MNzZ2PWRSQG-hE_nqGKKtUo2QTvU3VJPVoXWyRUQVIliXNr47PfxNYASwhs4WYhl1TZ9un3VkbfhAZMKsdP87WWIcGxyal008Fd_xZf7jUTgcwdMUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83835975f0.mp4?token=lv6xE_thcfOVuohMH4CcWdSjNCVSa-9y5vHzBDF1Kke6uCRjWtmHXiXTa71BCA8vfIbZu3yWoE059ndz7Qdakgh-1eVwvE7nZyYG3XAArAX_rub-xis0oUAXq83I49fmwSDViZT7U9ABm-S8OnYPM5de65EfYUo5rIHQLoGWYOJIkEiMTOkqJFp47CoObOpJue1tbiKCKHtzIPdo_AZbe7_uUK7CvB9oa35lWL5NNXf7CWkhho4W3_VxIvqofpZwD0guVzODvfy0VSOx1ySVnmAwjSlPX9OmtKtGbQsOHAEse8HoBkLmv2k_XGAh-cc2CBnmR3Du5zbSUR1sXV5klJ3gSV0_78d3mUx-Vxh8T67bQpdbNnhmKrQzhMQ2hyewWVD-7qGe_NR5uXfgkCl7J9Jsd7PnuxYiU4E9aWgTChJVIiLv-1bGFNFgVHiPPEgHYtU8K8BDX1CmlSMHTgW1tJYmWtz7BLqe2epzX1OV47HOFfSWzP38TKie9xhhkOrNlTuUwanjdkpQ45bnXgabjvXoaOTAnzNa5qD4fiuO_mO19l7sjWZznMxq2MNzZ2PWRSQG-hE_nqGKKtUo2QTvU3VJPVoXWyRUQVIliXNr47PfxNYASwhs4WYhl1TZ9un3VkbfhAZMKsdP87WWIcGxyal008Fd_xZf7jUTgcwdMUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
ساعت به وقت خیبر است
پرچم‌به دست حیدر است
این باور یک کشور است
ایمان ما حب الوطن
ایرانِ ما ایرانِ من
مرجع محتوای حماسی در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/656974" target="_blank">📅 23:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656973">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
سپاه پاسداران: عملیات امشب صرفا یک اعلام اخطار بود و در صورت تکرار تجاوزات پاسخ ها گسترده تر خواهد بود و تمام اهداف امریکایی-صهیونیستی را در منطقه در بر خواهد گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/656973" target="_blank">📅 23:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656972">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
پاسخ دادن حق ماست
حقیقت‌پور، نماینده ادوار گذشته مجلس و فعال سیاسی در
#گفتگو
با خبرفوری:
🔹
شرط مذاکرات ایران با امریکا برقراری آتش‌بس در لبنان بوده، اتفاقاتی که ضاحیه رخ داد نقض آتش‌بس است.
🔹
برای این که اوضاع بدتر شود و مذاکرات صورت نگیرد.
🔹
عمدا اسرائیلی‌ها این حملات را شدت می‌دهند و ما هم برپایه تعهدات اخلاقی که به لبنان داریم نمی‌توانیم بی‌تفاوت باشیم.
🔹
شاید لازم باشد از ظرفیت‌هایی مثل یمن بیشتر استفاده کنیم و از آ‌ن‌ها بخواهیم پاسخ بدهند.
🔹
پاسخ دادن حق ما است چرا که آن‌ها آتش‌بس را رد کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/656972" target="_blank">📅 23:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656971">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/909daa1c5a.mp4?token=DrfTTsS0q2oChdwN9o4s8x2wVtYpqJ7TtjuErZ2DVBtYVmdq6wMG8SqayS1TYr3BmcalrazCb9aBlohvUs0JmZRT4DLgzezlqlVMIVde9rgXRsAce4gJjNcZD6XMmLUxoVcYQ_ZZdVFnnDmkAOZ4Bn70gk3fOir8FSkJj35TKehT1NDNwxKC96mTl9EpwigrisY-aT5jbaJRBH2629iXMIsgq5B6l3TU7VMVKwHvw__3OlNe1JFOLKkB3Kb3o1stmbzDMa_dLNXla1xTK1bsTasCzT612NRYghsEbXRvUQ6gFnlOJ86fY5g9IDxYHB_CfZczOYiF7qiGePflKrGlvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/909daa1c5a.mp4?token=DrfTTsS0q2oChdwN9o4s8x2wVtYpqJ7TtjuErZ2DVBtYVmdq6wMG8SqayS1TYr3BmcalrazCb9aBlohvUs0JmZRT4DLgzezlqlVMIVde9rgXRsAce4gJjNcZD6XMmLUxoVcYQ_ZZdVFnnDmkAOZ4Bn70gk3fOir8FSkJj35TKehT1NDNwxKC96mTl9EpwigrisY-aT5jbaJRBH2629iXMIsgq5B6l3TU7VMVKwHvw__3OlNe1JFOLKkB3Kb3o1stmbzDMa_dLNXla1xTK1bsTasCzT612NRYghsEbXRvUQ6gFnlOJ86fY5g9IDxYHB_CfZczOYiF7qiGePflKrGlvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رژیم صهیونیستی در حال شلیک موشک‌های رهگیر کم‌تعداد خود برای هدف قرار دادن موشک‌های ایرانی است
وَأَعِدُّوا لَهُم مَّا اسْتَطَعْتُم مِّن قُوَّةٍ
🔹
در برابر دشمنان هر چه در توان دارید از نیرو و قدرت آماده کنید.
🔹
سوره انفال آیه ۶۰
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/656971" target="_blank">📅 23:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656970">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
سپاه پاسداران اعلام کرد: پایگاه هوایی رامات دیوید، هدف موشک‌های بالستیک قرار گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/656970" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656969">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
سپاه پاسداران: عملیات امشب صرفا یک اعلام اخطار بود و در صورت تکرار تجاوزات پاسخ ها گسترده تر خواهد بود و تمام اهداف امریکایی-صهیونیستی را در منطقه در بر خواهد گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/656969" target="_blank">📅 23:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656968">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
روشن شدن آژیرها در ۲۴۲ نقطه از شمال سرزمین‌های اشغالی
🔹
طبق برآوردهای جمعیتی، به دنبال سومین موج موشکی ایران، ۱ میلیون و ۵۲۶ هزار اشغالگر باید به پناهگاه بروند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/656968" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656967">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">فتح می‌خوانیم برای پیروزی جبهه‌ مقاومت و برای یاری سربازان امام زمان (عج)
▫️
رهبر انقلاب اسلامی در پاسخ به سوالی، قرائت سوره فتح، دعای ۱۴ صحیفه سجادیه و دعای توسل را برای پیروزی جبهه مقاومت توصیه کردند.
⬅️
صوت توصیه های رهبری</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/656967" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656966">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0zu5yUIFSW7GMyfi5I3TcAEeBUpARWRgGu2GugHW6A1JDwID_qfgNZqjJZsU8JT6dr3rWiu14KFpJW32V0zJ0UwUBmhXqjKn95XnWd2eU-J0m_s7HN-z7DujglW7VHu3RGsz0m4tD3JO0Gx2franJ-_ijwAd2BBwKzHcwvRlVQHVp0pHoB3pJukEfqqusGAAu1l9LI2PdhK04eIqOHz1f3ZSqpFQ-4CBhKC3_bAno3_hvA-8VuTxkB92g_qQ-pTa6X6JKkqvauvA31pHrin19qc4-ttFWZPxkke5D8MY2UMYB_vpXlTevVgGzlrKLbQoZ1duggpweIwjmeNtUNRJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله خامنه‌ای به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
❤️
رهبر انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کردند.
🖥
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/656966" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656965">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlIe72awErrBDqiKrF4eNJIl0LDPTr6ZkdsZXUYYXRGPt5Tm0Tm8BwIsybO_cltFrqkbh3jOmeUvdomRDXpUCpPfff6h361zrZXlKef2xCUE2HxPOX6Ey0ht-bBsEVue2A332o8p1pgrXNNKPqzAZH0uD98u1LzVjB-sqZzHQaJQmrAdD-dVFs3wPECN2mck83z5UC_Cw8rO2LgOF0O3RZCwvomplcu3p2LptstToSnSMRoPFLsCb_QAslZMCZB6MRqoGC7wkyHYpUbbq_20GvJS-thgRS1mL0tmxEunLtjhRC0fygWZBpMhxsz7y8ESLwlKQeCuQVtw8XLfPSJJaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روشن شدن آژیرها در ۲۴۲ نقطه از شمال سرزمین‌های اشغالی
🔹
طبق برآوردهای جمعیتی، به دنبال سومین موج موشکی ایران، ۱ میلیون و ۵۲۶ هزار اشغالگر باید به پناهگاه بروند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/656965" target="_blank">📅 23:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656964">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
کانال ۱۲ رژیم صهیونیستی: صرف نظر از نتیجه، ایران ثابت کرده است که پس از بمباران بیروت توسط اسرائیل، تهدیدات خود را عملی می‌کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/656964" target="_blank">📅 23:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656963">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3oEaGAklRc76AHJMNYW8YIL0oGK9Y1ftZzR_CCRLvBn3rv6btKHa8AUMtFHcw4dxRzKNEcZRF2qy9ODZSUEi_oKsoWKMiV28M3cDoBYyAd5h77CyVgNtzW7X0foXj-f8mPBnacW0mpkYF9Mg5Mi9ncmqxL5QYWvRNliJ1U9e5vb9H_XU3PaLZ4zJfRFynDPbY9dwv7CsCOYDbetysSoltwnoZDM5186N1byYLHQOifCsjq2XT4NdwCYFszmFSpQV9s8THM4T6IK9CKIvFYFI0AvqM0OUUYbf_98P5ISBKWHUZqOAjnx4uMfDyvkvIbsPHl8fhrM4UKCfaRuE6Q_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عزیزی: دشمن فقط زبان زور میفهمد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/656963" target="_blank">📅 23:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656962">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
آژیرها به دلیل شلیک موشک‌های بالستیک ایران، بار دیگر در سراسر شمال اسرائیل به صدا درآمده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/656962" target="_blank">📅 23:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656961">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9nP5uyOLg2o0u-zrg3_PYq9kOrtLVv0aDnH2hKxkTL9k3NNw52kl9VSHPvgukl6Zw38PmfWkwMp6oGHF0peq6JDX7L5cAu5jda8rOrCZI7vTF7Y1T3vURmC1OhtokASMXmVA3viecLWI2W4MTYjz68pclQ_EbhH1-ZnKvp6_iSsDq7U8cKXDox_dTLvNdqHTFTkizWi8CFrL3BgeaAIEr6shczVQMOb3NNOjEV1BzK-1-sG27FlKgGeazFhKEP5KTStDX0JaMA7RpfnfbHWsSDfAu_X7o3sdwC-H7YmIux72LnqMFbiTahS8yXM4_uSqc1ucD4l7G_wRoJTwcTHkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی، مشاور عالی نظامی رهبر انقلاب: جمهوری اسلامی ایران بارها اعلام کرده بود که نقض آتش‌بس یا تجاوز به لبنان را تحمل نخواهد کرد. امشب، متجاوزان پاسخ خود را دریافت کردند. این پاسخ، هشداری است برای توقف شرارت‌های آنان؛ هر اقدام جدید با پاسخی کوبنده‌تر و هزینه‌های سنگین‌تری مواجه خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/656961" target="_blank">📅 23:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656960">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
شنیده شدن صدای آژیرهای هشدار در اردن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/656960" target="_blank">📅 23:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656959">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3T15yurpzLltNoI7MNzP44hDetMYxLNPcGHKmfXjCdhWV5nggjp_-H49lDMDjxqwP2tzkHWXfYEVYmvpI1VNcnLlLZMloyZ1om9r_-ANbujQEWxchdPzag8m6YSWhE-s_PEVOgSGZ8l5FLNcwfGb9irR_1nzoBHXS9Fxz2IeSb3F1-A4JwtdEhL4DCArF0qdrji-CYkCgblX-kGiGFwgmm3CK4TCN5OsH9xie2njhUPXgGEj1RwAtWLEuzgpD0NorfNHRPR144mALvyCk_EKRBpydqVV7gQwUYZyR7sS0yxxa6bKPX0O7oQLPYMHD05jrpsxs4W4k7Z8AnyvFsY7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آژیرها در سرزمین‌های اشغالی یک بار دیگر به صدا درآمد
إِنَّ اللَّهَ اشْتَرَىٰ مِنَ الْمُؤْمِنِينَ أَنفُسَهُمْ وَأَمْوَالَهُم بِأَنَّ لَهُمُ الْجَنَّةَ
🔹
خدا جان و مال مؤمنان را خریده و در برابر آن بهشت را داده است.
🔹
سوره توبه، آیه ۱۱۱
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/656959" target="_blank">📅 23:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656958">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
کانال ۱۴ عبری از برگزاری قریب‌القوع نشست نخست‌وزیر رژیم‌صهیونیستی با حضور وزیر جنگ و رؤسای نهادهای امنیتی خبر داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/656958" target="_blank">📅 23:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656957">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
دسته جدید موشک‌ها راهی شدند
🔹
منابع عبری از شلیک موج سوم موشکی ایران خبر دادند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/656957" target="_blank">📅 23:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656956">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
شبکه ۱۲ اسرائیل به نقل از یک مقام اسرائیلی گزارش داد که ایران به دنبال تحمیل معادله جدیدی است اما اجازه چنین کاری را نمی‌دهیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/656956" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656955">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-ZPQRNqQMGAn9gmoMw97YYH33fPnGnpUaql9DfeaFj9MAKk28v-xYH0Y7gbKncaXIFQaXnsgGzRx0ciQsaevcGMQNA0LJWFSKXGjq60U9RQC0Fz36cGwWiYBThm9nbLF5bcgT2t9BVyEP-v1qgczM9ZS-AAl82EIPEdxNbMxSXDQUjAVHpgV4vpPsDMCzbJN9Lv2rZWnWQzVv6YgoSlSkqmH6UtrqAJYjSP2o0RFe8N4MaZ2huaNaFa2JV3UldZxkPDQNjiF6K5fQa3GipLtVraa87aRb5n6E1KbB5YIAnjNe8AJkQ_kGkJStvLVGT3grpDb0sDV_ie_g4aP90DsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الوعده وفا
🔹
پیام کوتاه سید مجید موسوی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/656955" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656954">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13d6b07a97.mp4?token=Gu4Diasvb9SDj6-VxTBMjL3Q2AObNuICf-2I_D40O8ZBF-mwQvo6ZNSo4vhGxZo_Kx3OURzxDqUH4HNX9DdJxCkTb6cy9Wj4DyRShibmcEVQqw3tABBs2UuOdzzpdUUYRyKjiS68c1HhnMqKNNr9zPDAx2iwwjOfnziRibuahbwJJocwjymSi4_fCpf-znknbau-WjlnrQMalRsn--94TQ2nrs5t1iYdIOQkqUMZJ_bYXv635NIXCMO6n0oqAp8-oKrJG9eWlFO8iETy5JTOqFIPiVoZRjKAZx9fooJy4y15nMgqiDSYUqlfro5gXAMi7PO5Fo4hgEAvMY4sTudSKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13d6b07a97.mp4?token=Gu4Diasvb9SDj6-VxTBMjL3Q2AObNuICf-2I_D40O8ZBF-mwQvo6ZNSo4vhGxZo_Kx3OURzxDqUH4HNX9DdJxCkTb6cy9Wj4DyRShibmcEVQqw3tABBs2UuOdzzpdUUYRyKjiS68c1HhnMqKNNr9zPDAx2iwwjOfnziRibuahbwJJocwjymSi4_fCpf-znknbau-WjlnrQMalRsn--94TQ2nrs5t1iYdIOQkqUMZJ_bYXv635NIXCMO6n0oqAp8-oKrJG9eWlFO8iETy5JTOqFIPiVoZRjKAZx9fooJy4y15nMgqiDSYUqlfro5gXAMi7PO5Fo4hgEAvMY4sTudSKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار فاکس‌نیوز در تل‌آویو: موشک‌های بیشتری از ایران به سمت شمال اسرائیل در حال حرکت است
🔹
شبکه ۱۲ رژیم صهیونیستی گزارش داد که مدارس فردا در سراسر اسرائیل تعطیل است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/656954" target="_blank">📅 23:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656953">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
حملات موشکی حزب‌الله هم آغاز شد
🔹
پس از حملات موشکی ایران به فلسطین اشغالی، حزب الله هم دست به کار شد و شمال اراضی اشغالی را موشک‌باران کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/656953" target="_blank">📅 23:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656952">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
رسانه‌های عربی: ارتش اسرائیل محدودیت و سانسور شدید بر محل‌های اصابت موشک‌ها در شمال سرزمین‌های اشغالی فلسطین اعمال کرده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/656952" target="_blank">📅 22:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656951">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ بزن که خوب میزنی</div>
  <div class="tg-doc-extra">مهدی رسولی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/656951" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
به فرق کاخ و تختشان
بزن که خوب میزنی
به زندگی نحسشان
بزن که خوب میزنی
حاج
#مهدی_رسولی
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/656951" target="_blank">📅 22:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656950">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
رسانه‌های عربی: ارتش اسرائیل محدودیت و سانسور شدید بر محل‌های اصابت موشک‌ها در شمال سرزمین‌های اشغالی فلسطین اعمال کرده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/656950" target="_blank">📅 22:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656948">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌
♦️
گروه هکری حنظله با انتشار پیامی، از اجرای یک عملیات سایبری علیه رژیم صهیونیستی خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/656948" target="_blank">📅 22:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656947">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77730b07bb.mp4?token=HYk7msq6mGQ3-W-g1DJY6pj3zthePkzV7TMJTku728Jgkx9QhScp-NRIKMzx_4AOP_fvtF2y-sXcx9aZYtj9lAiCNkMoJqEa8l8QeAeXyoOokEy9TdyvdevRtGUiaJZY9sd3fmZfXr3a-bA5AKoiW88aeTlS8rMCMqMQ4Ry8G6igOiDthXktr-lGhCTqLSGr9UWGU6_LTQM_omn5tVwBUB6iq9C6NM4qV9K-l01cZs4ybpBq8zfgouQJj9-KVtcuTVuKbPqQIvDbhDpan_UKo1R9Be4Ih0T64GMD3tMYKUpCbK6F4R7WRlSqkZmgmg2IBCOoAEtw2jZQqJEyarIh4AQ8qlUX1NeY1msM98mjHBO-nH5Ufa_likNVgyczN3pFTvsEIHkO7qsCuPpjiacbfRtzw4_zWq1eh1YNRTbZdHo3vtScMQwD1DYQ7iSqT73PMZaEDp_tmFgB6wPrrc0v8HME4pbRhybiWYK3vKuZKWQPb65BLetrUypGYWagN-9QmJpP6FD_gGjBElxMbvHWNxYGEohj8ICNxaCuKAo3C-oxYeySDmsxIuJrVq5_Xo23Osi0BwltRuUw7PB_puEbPrw3iY2PCwxY8lcGHPmbm1I-NNdm7j8ufhE-D3-Q_b3CUJgENYwZWgnYBR1PgNdQgoNGDGk4hCOblaO7ql_yBRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77730b07bb.mp4?token=HYk7msq6mGQ3-W-g1DJY6pj3zthePkzV7TMJTku728Jgkx9QhScp-NRIKMzx_4AOP_fvtF2y-sXcx9aZYtj9lAiCNkMoJqEa8l8QeAeXyoOokEy9TdyvdevRtGUiaJZY9sd3fmZfXr3a-bA5AKoiW88aeTlS8rMCMqMQ4Ry8G6igOiDthXktr-lGhCTqLSGr9UWGU6_LTQM_omn5tVwBUB6iq9C6NM4qV9K-l01cZs4ybpBq8zfgouQJj9-KVtcuTVuKbPqQIvDbhDpan_UKo1R9Be4Ih0T64GMD3tMYKUpCbK6F4R7WRlSqkZmgmg2IBCOoAEtw2jZQqJEyarIh4AQ8qlUX1NeY1msM98mjHBO-nH5Ufa_likNVgyczN3pFTvsEIHkO7qsCuPpjiacbfRtzw4_zWq1eh1YNRTbZdHo3vtScMQwD1DYQ7iSqT73PMZaEDp_tmFgB6wPrrc0v8HME4pbRhybiWYK3vKuZKWQPb65BLetrUypGYWagN-9QmJpP6FD_gGjBElxMbvHWNxYGEohj8ICNxaCuKAo3C-oxYeySDmsxIuJrVq5_Xo23Osi0BwltRuUw7PB_puEbPrw3iY2PCwxY8lcGHPmbm1I-NNdm7j8ufhE-D3-Q_b3CUJgENYwZWgnYBR1PgNdQgoNGDGk4hCOblaO7ql_yBRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه اعلام شلیک موشک های ایرانی به سمت رژیم صهیونیستی در چهارراه نبرد خیابان پیروزی
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/656947" target="_blank">📅 22:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656945">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
دسته جدید موشک‌ها راهی شدند
🔹
منابع عبری از شلیک موج سوم موشکی ایران خبر دادند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/656945" target="_blank">📅 22:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656944">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hagl_3DTFlnphPRAApfu0uCy1zBxd56kYtWysrqPT4qLcKgYl1R5Q55m40uEHcNAsMC213pGkNt3mMj3ur8qBX6SRb0HtKYCICRwrJOa3YdzAQqizo3bh1tQsRw1ZoVZJJgDFT6Gph2UQIy3ZBh1axx26SrAYET3JX40QF5aqFIfSUxoq8OibDuEQNgus4ZoJqghxHiiTbUb9QEL6r5Vf0KXP8FAGB5w3Hso3hpW4yaVpv78uVmg-4xKh3xVI8PlMAMcF7qly8wtGQWGRN0B5HEker326rTt4L79xYk6uulRBgkAFPSUs93F347HZGXmuCCVxSqoO73DgQ5MDngnag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دسته جدید موشک‌ها راهی شدند
🔹
منابع عبری از شلیک موج سوم موشکی ایران خبر دادند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/656944" target="_blank">📅 22:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656943">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpvWeO7GiU-7_z4y9RfpITvEDKa_UW--wJLlsEKtDSmS2D-2nQ6Xr-dewtU-Ai5POoJmQsFFytzs3Fnw0gKravyFAWfQHQO0hxtQoLrrd0d49VgzruoovwOP094jWPs0V9tIj4u2yI6ad9_lrZs1Wa5jqkFnYXF1TSvzPsi38dUPAv1WhvMUYzC4jHJPSEdR-pvGrJgFezxwvxTmiDD0GMEtUZl4A1PNTz0m-nuWrA-y-9e63damJa9aYiPrAdppptW3-FZFaVtSGj5BRY83egBLXJsch0YnSvlX-oR4F92FuqFIfBm4RhYCK8xHjyIvBQ4ULQoutJrCHJl28yxMlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست عراقچی در شبکه ایکس با تصویر پرچم‌های ایران و لبنان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/656943" target="_blank">📅 22:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656941">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/840e3fba03.mp4?token=RDwff_lwu29Qlir7hfGKbIm8UpgyfFEPUHKLZbjvHxh02hL7OHk2U7vXu38d9VHXjPA5ENDotji724Ry4Gybu6PO2ZzUll1np8PGl0dWg6skz79fK1MvEzdKFQ9RvJAA3VEu625kef15Wlt1fMMwcymQbdw-x_xOvtTZzAYUYekycjC19vUWHUMqIyzOYB5RgU3IAM-fKzLTbFPRLwoBL0VFv9nMSeJr7V_nI39BM_S9spNqKy0HT9U89J5veTDkqTqOU1PFqpvEJQPQEBvQzISfKMl01QPNAU342Na8btiYP8j5C-2PJhaYHltjmbZk6-DR65X6XH-8vmgVBWtWOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/840e3fba03.mp4?token=RDwff_lwu29Qlir7hfGKbIm8UpgyfFEPUHKLZbjvHxh02hL7OHk2U7vXu38d9VHXjPA5ENDotji724Ry4Gybu6PO2ZzUll1np8PGl0dWg6skz79fK1MvEzdKFQ9RvJAA3VEu625kef15Wlt1fMMwcymQbdw-x_xOvtTZzAYUYekycjC19vUWHUMqIyzOYB5RgU3IAM-fKzLTbFPRLwoBL0VFv9nMSeJr7V_nI39BM_S9spNqKy0HT9U89J5veTDkqTqOU1PFqpvEJQPQEBvQzISfKMl01QPNAU342Na8btiYP8j5C-2PJhaYHltjmbZk6-DR65X6XH-8vmgVBWtWOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری از حمله هوایی ایران به اسرائیل
وَلَقَدْ زَيَّنَّا السَّمَاءَ الدُّنْيَا بِمَصَابِيحَ وَجَعَلْنَاهَا رُجُومًا لِّلشَّيَاطِينِ  وَأَعْتَدْنَا لَهُمْ عَذَابَ السَّعِيرِ
🔹
و در حقيقت آسمان دنيا را با چراغهايى زينت داديم و آن را مايه طرد شياطين [= قواى مزاحم] گردانيديم و براى آنها عذاب آتش فروزان آماده كرده‏ ايم
🔹
سوره ملک، آیه ۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/656941" target="_blank">📅 22:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656939">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nzz2QSstA8luJRYixe2cxhlel3dJxG_KI3oNnERxnMW8R0R27DpmgRCWS-GR5VlNE3JkQAjPkyOMjzUXKThCQb-advNlQrBei9ux4fbb23KDlwFUA0iPIykyF5-_-JxcYQFCtd3Zl7uP_AfHePx-R1jOjtklqrtvkbhoRjVIkVfaJp4Wv2SRELupkNeHFyqd9OLpyPm3HkOWF7L73gxQjW3gPxXUykq0zff-MmM71Ia3J0daaZNk2UXrK5LRraLcqKrBwywndaWCiISeaJgB3x7IgRES0vhV9UJUcRnNaRUp6L4jFdeG20jHUsso2HhCskw5xr2P1L2Faq0PqFJhFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PncA4VN4rziCsVJPrDyYf5c0Y174P8R0MYMj33G0R3YfSoWDke2NH6UjaWeYUbXLzGg7zZIBhe6q0lrLtBMynegGMZJbnzrTieVNu4WHqnp8Y4iYuIvk4cmJ-J5pmq6EoOgi2aFHAV3an2-hu2r7fydy4oo69SdUU9utOJ66VyHbVZDH7k8v9MWrOPVUGAmm2bU6TnmWTOKPIBHceLE7_GwlR2_BxTaIQKnqqGrAO6dgu8eRYAp113kVUGI8NGqp6Jqn-_C_QbTIqReCYtdy597nKrQuLahwaqQ85tnpnLpIqSuc7bcSlVrfsShlD1NK6PsI7HIe1N-efbvnJvFEiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
موشک های ایرانی در آسمان کرمانشاه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/656939" target="_blank">📅 22:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656938">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
بعد از نقض چندباره آتش‌بس توسط صهیونیست‌ها، موشک‌های ایرانی به آسمان سرزمین‌های اشغالی رسیدند  اللَّهَ يُحِبُّ الَّذِينَ يُقَاتِلُونَ فِي سَبِيلِهِ صَفًّا كَأَنَّهُم بُنْيَانٌ مَّرْصُوصٌ
🔹
خدا کسانی را دوست دارد که در راه او صف بسته و استوار می‌جنگند. سوره…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/656938" target="_blank">📅 22:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656937">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW1sAB3662jqFPQTFPXNCmB2eC4Sm-Mk39UA_MTcityrn93LY3wN50J2qLgP4rhmiwQCnvYsO5gMJqcd7B8BVnRbIuqRUHU-X9TM1lGnb6wcNxuoJ4TIi1X_2QTV-I0YZ58P9mnyvcwI0FNaYaIWTPD6G3HFlZPaZygdUdaKQ4GxQDlizcQ-9HUa-Eu7WRNsCToFEC-CylR49x3NYBHe5rlFq_1pCY1-rWu0ryRbDPsPK3W6MsP8W5Rsx1pDmrt3n5o63KyHVhUlj2-i8gyrl1in-ClXr0Kz40q0UIg8KxbdD0c7WI92o9kSFp85i_K52Ow_x9aB91z_pzCGEorb7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش اسرائیل: رگبار جدیدی از موشک‌ها به سمت اسرائیل شلیک شد
🔹
فرودگاه بن‌گوریون در اسرائیل تعطیل شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/656937" target="_blank">📅 22:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656936">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abca4c96af.mp4?token=ifhhImugxQkICLpNhwTFkfGJzznYpIk70RIPKII0oBqGvbtaCNrObbm0VT3zfUmTkxt-g3PKYv3oeEITLAN6jPzY-bcjm_USZo5DIgNJMAKhZwd_5BNjSC59NxhqY8sZ-QupJe10bQRb5wbVHwVl6vHP2-2Kv3vfNK7V4t_pBDhYVtVU6VmNrdyZ_W3QatcFm4LHGwHLqvLWkQXQe0MtfkWiAVREukNFpAZ8spz8ayfKVdFQ1PhiD1tR7gS5v-P-R3wFj7cO0h5kc8ocSCIwjuk5MAaoFrDwIDbSHz231VQQ4z3Z4vLisidfgbCve6M5mmyl57r72Yg0gjQgK7hsGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abca4c96af.mp4?token=ifhhImugxQkICLpNhwTFkfGJzznYpIk70RIPKII0oBqGvbtaCNrObbm0VT3zfUmTkxt-g3PKYv3oeEITLAN6jPzY-bcjm_USZo5DIgNJMAKhZwd_5BNjSC59NxhqY8sZ-QupJe10bQRb5wbVHwVl6vHP2-2Kv3vfNK7V4t_pBDhYVtVU6VmNrdyZ_W3QatcFm4LHGwHLqvLWkQXQe0MtfkWiAVREukNFpAZ8spz8ayfKVdFQ1PhiD1tR7gS5v-P-R3wFj7cO0h5kc8ocSCIwjuk5MAaoFrDwIDbSHz231VQQ4z3Z4vLisidfgbCve6M5mmyl57r72Yg0gjQgK7hsGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از نقض چندباره آتش‌بس توسط صهیونیست‌ها، موشک‌های ایرانی به آسمان سرزمین‌های اشغالی رسیدند
اللَّهَ يُحِبُّ الَّذِينَ يُقَاتِلُونَ فِي سَبِيلِهِ صَفًّا كَأَنَّهُم بُنْيَانٌ مَّرْصُوصٌ
🔹
خدا کسانی را دوست دارد که در راه او صف بسته و استوار می‌جنگند.
سوره صف، آیه ۱۴
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/656936" target="_blank">📅 22:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656935">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
گزارش‌های اولیه از شلیک موج دوم موشک‌ها به سرزمین‌های اشغالی حکایت دارند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/656935" target="_blank">📅 22:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656934">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
منابع عبری از صدای انفجار در «نهاریا» و «طبریا» خبر می دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/656934" target="_blank">📅 22:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656933">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای متعدد در حیفا
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/656933" target="_blank">📅 22:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656931">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
منابع عبری: حدود ۴ شلیک موشک به سمت شمال سرزمین‌های اشغالی گزارش شده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/656931" target="_blank">📅 22:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656930">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2637baccc4.mp4?token=WtL4zNxXS6BirVB4lIaOzmFvj_mykBJROfTnmDpmfLQV-7q8y081frW2-wESeCg_b1bDLWTqHtHIZW-0RK1EdRFyGCmfiCBugQ2ipyyxum_ACAbPOjq0KUWc8OmAk-IVqe87IUQthWGwQW0q68_Gc-XpO5NDsCnpID_d7POOzfeEUgQIKfIo30Vv6b4XKrva5VEh6WeZaoNVcAi-SQ9fe_eW7hSsN5ycIOtSI2WK87Hy0HlxChtO1qgWWwDP7NJlho0okCAKEtk0CqGrchRGVBVHrzibhaH0mil_eF7W64i1rpTg98Kdr_jLxp4lRnRik3RcX7NZ1L96y9b2hvVjeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2637baccc4.mp4?token=WtL4zNxXS6BirVB4lIaOzmFvj_mykBJROfTnmDpmfLQV-7q8y081frW2-wESeCg_b1bDLWTqHtHIZW-0RK1EdRFyGCmfiCBugQ2ipyyxum_ACAbPOjq0KUWc8OmAk-IVqe87IUQthWGwQW0q68_Gc-XpO5NDsCnpID_d7POOzfeEUgQIKfIo30Vv6b4XKrva5VEh6WeZaoNVcAi-SQ9fe_eW7hSsN5ycIOtSI2WK87Hy0HlxChtO1qgWWwDP7NJlho0okCAKEtk0CqGrchRGVBVHrzibhaH0mil_eF7W64i1rpTg98Kdr_jLxp4lRnRik3RcX7NZ1L96y9b2hvVjeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک ها رسیدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/656930" target="_blank">📅 22:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656929">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
گزارش ها حاکی از رسیدن موشک ها به حیفا هستند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/656929" target="_blank">📅 22:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656928">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d76a142916.mp4?token=iJ4UujKxWJwg7zo8YB9pqHVov4qyKqrPD0iVh0fBioqVT3QqN7fTHYk5QAeMjr2PNt92Dkd2FSYcdbubjsqTmngMhU80CEGHgQYixIy8ylo_WEEQsX-enD-DUElKf8cI_hruehihYcsk9aBKtGHelbXiasgWb6HaMvzjZWxVMX3T8aedDoez5rLJzzrDM7tPw57LL7n0RrLe6Kd4xIjxNNUVUNFKUfYXMRVo0Rzy1-mnLpvWnd3v6TFnJH1MMYh7OVTY86XJR4-r-KuFUByBwYmGyZgeomAsjeoBm3U-5R1fjvCu6tUuxBEC8BiPtos2x7VD92LFPw3sEj21eKteQDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d76a142916.mp4?token=iJ4UujKxWJwg7zo8YB9pqHVov4qyKqrPD0iVh0fBioqVT3QqN7fTHYk5QAeMjr2PNt92Dkd2FSYcdbubjsqTmngMhU80CEGHgQYixIy8ylo_WEEQsX-enD-DUElKf8cI_hruehihYcsk9aBKtGHelbXiasgWb6HaMvzjZWxVMX3T8aedDoez5rLJzzrDM7tPw57LL7n0RrLe6Kd4xIjxNNUVUNFKUfYXMRVo0Rzy1-mnLpvWnd3v6TFnJH1MMYh7OVTY86XJR4-r-KuFUByBwYmGyZgeomAsjeoBm3U-5R1fjvCu6tUuxBEC8BiPtos2x7VD92LFPw3sEj21eKteQDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصاویر از شلیک موشک های ایران به رژیم صهیونیستی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/656928" target="_blank">📅 22:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656927">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
گزارش ها حاکی از رسیدن موشک ها به حیفا هستند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/656927" target="_blank">📅 22:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656926">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6vbVo2J3O1V5DJGHTQZREBhC1tZzpMdzEwSioE_I8zThK-3mTaRFxnMfrABrwGozlRfkocpXRjGHz_a7aSSc_w9MAkhqAkH2ZOunW3pRtICtQHR95I_7PUVKmT1CJ-N_6Rsmew6YhmS7cropvEUGF7vWsA6m1tA8UQU4a3XH-M8HelrX-5Cuh5ziS_sASKg9QngBgAPkVklkS0j-KkHEtNjDkJdUHqnm4NqfMwDAVHAKKqcnyKb-Q9hSZ6LyKd7PVfqEN219jTkgQy36hJdDaAv18eoXkN8jldHgri37zWZaHmVPEYUsKqmo10_VZSuv4wrhHwJKXerHAMRaGpViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعال شدن آژیر هشدار در شمال فلسطین اشغالی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/656926" target="_blank">📅 22:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656925">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
منابع اسرائیلی: شلیک موشک از ایران به سمت سرزمین‌های اشغالی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/656925" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656923">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
منابع اسرائیلی: شلیک موشک از ایران به سمت سرزمین‌های اشغالی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/656923" target="_blank">📅 22:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656922">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
قطر آسمان خود را بست
🔹
دولت قطر با صدور یک هشدار هوانوردی نوتام، حریم‌ هوایی این کشور را بست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/656922" target="_blank">📅 22:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656921">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj8gnEhc5p1TJxVRykwp5qzmsgP7mity01dchrCQONzQs6q-7oiCkJvvNdLkK8ZaJfnT7hFDK5y-eeJDkLpmQH2RhJf8oi86Lf0eShvqSdNVWKc69PArGuMdpmQEybp1AKiD1tXLHgQObjXHy3_rkdsZtV3o9L_vrycEVthO75WDLoYhKGHkBVRVTuPLmnM26sYalleB9ZTYvSfYmzJl5D9mq0syfoHq6ilYGKGewDnCj87PD0HJ_d_32So5qfyVkLCXaWIdFjXGm3scgJFpoxfV5-o8_rr7o1R522RXzbHNW6Keqai5zDDuLesy0Yc49DZlsObw14DbJL8L7YMZCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعال شدن آژیر هشدار در شمال فلسطین اشغالی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/656921" target="_blank">📅 22:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656920">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
حمله هوایی رژیم صهیونیستی به شرق لبنان
🔹
منابع خبری از حمله جنگنده‌های صهیونیستی به شهرک سحمر در بقاع لبنان گزارش می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/656920" target="_blank">📅 22:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656919">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ادعای العربیه: وزیر کشور پاکستان از ایران خواست تا در اسرع وقت موضع خود را در قبال خواسته‌های آمریکا روشن کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/656919" target="_blank">📅 22:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656918">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
تیراندازی در ۴ مایلی اردوی تیم انگلیس، در آمریکا، با ۹ زخمی
روزنامه سان:
🔹
در جریان تیراندازی که تنها ۴ مایل با کمپ تمرینی و هتل تیم ملی انگلیس در کانزاس سیتی فاصله داشت، دستکم ۹ نفر زخمی شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/656918" target="_blank">📅 22:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656917">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlMb-BpTnNJHmIRB6WyOb3WQl_7HEAU-qmOotf59L2j1LYazu3bHXdFVUNi5nl2AybFakjRGK10xZ3soiIrm7J3h6BhvzhzxSdK-KcTH30LYs8gTstJVsRm5iSk4HFpGRlIcv6zFjUQDh4OUARwlbPv_gnNztaZfhoOoJ2tnxPSpeSu9sYrwm2GjlhOilfqDpKaRiVGH7qC9F_D-QSZ7KlnTDrZedTgKaZbR218vsNq7ByqDcIQAVP1eDLsAYU4VmQLr7YzsyDA9QH_eKZymmdPvI2jg0ycm81t-RdUY7xu7Q9zcn8lwt788iOfYT0yAyRqq09HwbllTBwmFl4ZKlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار دانمارک و اوکراین به دلیل بیهوش شدن کریستین اریکسن متوقف شد
🔹
اریکسن پیش از این و در یورو ۲۰۲۰ هم دچار حمله قلبی شده بود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/656917" target="_blank">📅 22:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656916">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نیکزاد: همه محورهای مقاومت نیز ذیل این عزت و خط قرمز تعریف می‌شوند
علی نیکزاد، نایب رئیس مجلس در
#گفتگو
با خبرفوری:
🔹
سیاست ایران در میدان و دیپلماسی بر پایه حفظ عزت و اقتدار کشور و حمایت از محور مقاومت است.
🔹
هر رویکردی که این خط را مخدوش کند پذیرفته نیست و همه محورهای مقاومت در همین چارچوب تعریف می‌شوند.
🔹
مسیر پیش‌رو با عقلانیت و اقتدار ادامه دارد و پاسخ‌ها در میدان و دیپلماسی مقتدرانه خواهد بود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/656916" target="_blank">📅 22:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656915">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
کمک فوری / حال این کودک خردسال وخیم است
🔸
دختر بچه خردسال جهت عمل جراحی و شیمی درمانی نیاز به کمک فوری دارد.
🔸
متاسفانه غده سرطانی بدخیم داخل شکمش دارد و طبق نظر پزشک معالج بایستی چند دوره شیمی درمانی و سپس عمل جراحی شود.
🔸
پدرش کارگر و توان تامین هزینه های لازم را ندارد و نیازمند کمک و یاری است.
💯
امیدواریم بتوانیم با کمک و یاری خداوند متعال و شما عزیزان مبلغی تامین و به درمان این بیمار عزیز هدیه بدهیم.
یا علی
اطلاعات بیشتر:
https://B2n.ir/fp8594
پرداخت آنلاین:
https://hakeim.ir/pay3/
شماره شبا:
IR090570033881011584199101
شماره کارت پاسارگاد:
5022291900030667
شماره کارت صادرات :
6037697090184034
شماره شبا  :
IR
900190000000120448806002</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/656915" target="_blank">📅 22:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656914">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOWtID9leQBjt5ZknQmUzBbLPHpCTWRj-gC3jwgvBCbht5Uxu-ESh-ISRYKJPLTSkux6HSb9_jJUX9M2EbaJNnE9k5mfipSA1_f8KZQV_aCwmbForEd94LgmhjtPcJINKbzefEBTrFyDMm9P_rjmCCrUoQ_WI6YS2FR9NDLPflSW4savD5xjToPtFE-CIp2XQSOf-RoiswmzltHD1Eg-4_ZksClBkAb7jq7tOzRdgc8qmoQz9hGelzt7eXePucuny0_cycL5EWOIBsgOTirUXNlLgNCugR7TYgS6GjL8XeE9mt1wHaGSZNfV_n9uI8RVHP_-VlTNmh24S7Mq_hFGqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از کجا وام بگیریم که کارمزد کمتری داشته باشه؟!
ما یک بررسی جامع و کامل روی وام بانکی شرکت‌هایی مثل اسنپ‌پی، مانیسا، دیجی‌پی و ازکی وام داشتیم تا ببینیم کدوم یکی منصفانه‌تر وام میده.
نتیجه بررسی‌مون اینه:
1️⃣
اسنپ‌پی کمترین کارمزد رو میگیره
2️⃣
دیجی‌پی و ازکی‌وام بیشترین کارمزد رو میگیرن
3️⃣
تعداد اقساط اسنپ‌پی بیشتر و طولانی‌تره (تا ۲۴ ماه)
برای کسب اطلاعات بیشتر میتونید تصویر همین پست رو مطالعه کنید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/656914" target="_blank">📅 22:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656913">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4cd8d0680.mp4?token=ZWe_za1ktk2_Se3zSjETjzc1F65thMDel-BMHq3seCbZ89ETmXJLBxxzeniU_mHrm7o1zwuwLp24THBUwIwdTl2ynpfOfbXuyTIySId6G6Ff6uvDzyMG_HL6OVo9rJeqJyt9SMmpWpU_McKM57-jPkkXV_wlvRGyZZ73_nv1wEQu00Yz933BSJMVjsAsA9lh33KMbKgE8W1J1OzkNkasdWZcN24QU5eOpbY3z3Ss3Ntc7uVAMjV0ZT95Zu27UfUxZj2gD8ON6GcKk-9cDV9QORqk248zQJExNhPHtoH9uo7Fqr1orUUAtY6zAJnNHddRtIX9Sc3YlRpUDZFZ-7ht_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4cd8d0680.mp4?token=ZWe_za1ktk2_Se3zSjETjzc1F65thMDel-BMHq3seCbZ89ETmXJLBxxzeniU_mHrm7o1zwuwLp24THBUwIwdTl2ynpfOfbXuyTIySId6G6Ff6uvDzyMG_HL6OVo9rJeqJyt9SMmpWpU_McKM57-jPkkXV_wlvRGyZZ73_nv1wEQu00Yz933BSJMVjsAsA9lh33KMbKgE8W1J1OzkNkasdWZcN24QU5eOpbY3z3Ss3Ntc7uVAMjV0ZT95Zu27UfUxZj2gD8ON6GcKk-9cDV9QORqk248zQJExNhPHtoH9uo7Fqr1orUUAtY6zAJnNHddRtIX9Sc3YlRpUDZFZ-7ht_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار دانمارک و اوکراین به دلیل بیهوش شدن کریستین اریکسن متوقف شد
🔹
اریکسن پیش از این و در یورو ۲۰۲۰ هم دچار حمله قلبی شده بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/656913" target="_blank">📅 21:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656912">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7763628114.mp4?token=X-GRSCjA6suGQXYH9qSH0KpH-kd-PDE3rd-r8vXhCm3qDk2QphaeIc0QI21pgD-4Ah_9M1RXWHczgjl1NFjUAdNkTxYoa4-yjx_lWZfJlsFpdSePN1_dFVxWU0eLV05AheveAgCXfZl-ye12WB69X0FrvqvWTPhZqX-MpGGxRon90JNRRTTUoJ_m7rbNdY2xaHAdyYX_JhLnUfB-cUW60Al0Yz9qNpaxQNtQt7thiCpjf4Fn25fJBvG85LcGCSnAlBcMq1dCy7L2hM6d41SaHJJ4F-bE15AxePH41ZH8-6plJpggpQT1-yyqPO4QcdFsVqyh7QuoNlNLf_tp7ANhbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7763628114.mp4?token=X-GRSCjA6suGQXYH9qSH0KpH-kd-PDE3rd-r8vXhCm3qDk2QphaeIc0QI21pgD-4Ah_9M1RXWHczgjl1NFjUAdNkTxYoa4-yjx_lWZfJlsFpdSePN1_dFVxWU0eLV05AheveAgCXfZl-ye12WB69X0FrvqvWTPhZqX-MpGGxRon90JNRRTTUoJ_m7rbNdY2xaHAdyYX_JhLnUfB-cUW60Al0Yz9qNpaxQNtQt7thiCpjf4Fn25fJBvG85LcGCSnAlBcMq1dCy7L2hM6d41SaHJJ4F-bE15AxePH41ZH8-6plJpggpQT1-yyqPO4QcdFsVqyh7QuoNlNLf_tp7ANhbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقدام بە موقع و دلسوزانە آرش لهونی استاندار کردستان
🔹
اقدام بە موقع و دلسوزانە آرش لهونی استاندار کردستان در جریان حادثه دختران آزار دیده سنندج موجب رضایت ، تقدیر و آرامش مردم در سراسر کشور شد.
🔹
در جریان این حادثه تلخ استاندار کردستان بعد از حضور در بیمارستان و عیادت از این دختر آسیب دیده ضمن دستور رسیدگی کامل درمانی، یک واحد آپارتمان را با وسایل کامل به این دختران آزاردیده اهدا کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/656912" target="_blank">📅 21:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656911">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کارشناس صدا و سیما: طرح‌های عملیاتی برای پاسخ به اسرائیل در حال اجرا است!
علیرضا تقوی‌نیا، کارشناس مسائل سیاسی در
#گفتگو
با خبرفوری:
🔹
حمله امروز اسرائیل به ضاحیه بیروت، آن طور که خبرها می‌رسد، تلفاتی در بر نداشته‌ اما به اعتقاد من، این حمله آزمایش ایران در واکنش به تصاعد تدریجی تنش است.
🔹
آن‌ها می‌خواهند اراده ایران را تست کنند و ببینند که اگر مفاد آتش‌بس را نقض کنند، واکنش ایران چه خواهد بود.
🔹
باید طوری امارات و رژیم صهیونیستی را زیر آتش بگیریم که محاسبات اشتباه آن‌ها اصلاح شود و بدانند که ما در موضع قدرت و برتری هستیم و اجازه نمی‌دهیم که معادلات نبرد به ضرر ما تغییر کند.
🔹
ما قطعا به حمله اسرائیل به ضاحیه پاسخ خواهیم داد و اراده ایران برای واکنش به اسرائیل جدی است و تصمیمات اتخاذ شده و طرح‌های عملیاتی در حال اجرا است.
🔹
معتقدم به طور جدی واکنش نشان خواهیم داد و باید محاسبات راهبردی اسرائیل را اصلاح کنیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/656911" target="_blank">📅 21:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656910">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hV6bvunGvsROiWn3wMB3_O-TvItqNAHX-EJZhgEuz4gt3x4xmBS-YRCkmrgdNlT2LkekJk0_0zG60d9tsbwyOAuBjp0Z9KcigTgq67te7UOM_e-1CbleQ185hVByevnIhXg6wk9Yic_j35HxLA96TDG8Og0nyZe_qt7UYnHyaBTivYqmTqJpiraE22wt1etBUCPYa986hfqd6wg3lFwQZj5OZKWadUP8uJVyImAUN6HLsxR2NWER_fkxoqXNUvyLpgYdgYeOo5tjTSvbfdfgX86AtHGIE_bg6pVPgivjKu4Va3nkGeJoL_AHZWqoInYY2nXDVUwdPSKzyJixau2rDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقام آمریکایی: باید فورا به جنگ پرهزینه علیه ایران پایان دهیم
رهبر اقلیت دموکرات در مجلس نمایندگان آمریکا:
🔹
باید هرچه زودتر به جنگ پرهزینه علیه ایران پایان دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/656910" target="_blank">📅 21:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656909">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
پژوهش امنیتی پیرامون متهمان ردیف اول ترور ددمنشانه رهبر شهید: ۱۹ نفر مستقیما در این حرکت بزدلانه نقش داشتند
🔹
بر اساس یک پژوهش امنیتی معنادار که اخیرا در رسانه‌ها منتشرشده، نام دست‌کم ۱۹ مقام ارشد سیاسی، نظامی و امنیتی آمریکا و اسرائیل در ارتباط با پرونده ترور رهبر انقلاب مطرح شده است.
🔹
این افراد به‌گفته منابع امنیتی، در مراحل مختلف تصمیم‌گیری، برنامه‌ریزی، سازماندهی و اجرای این عملیات نقش داشته‌اند.
🔹
پس از انتشار این اسامی مطالبه محاکمه و به تقاص رساندن عاملین و آمرین ترور رهبر انقلاب در محافل عمومی شدت معناداری پیدا کرده است. با این حال، جزئیات مستند درباره نقش دقیق هر یک از این افراد هنوز به‌صورت رسمی اعلام نشده است.
🔹
در ادامه فهرست عاملین و آمرین اصلی که گفته شده مورد پیگرد جدی قرار خواهند گرفت بدین شرح آمده است:
۱. دونالد ترامپ، رئیس‌جمهور آمریکا
۲. جی‌دی ونس، معاون اول رئیس‌جمهور آمریکا
۳. مارکو روبیو، وزیر خارجه آمریکا
۴. بنیامین نتانیاهو، نخست‌وزیر اسرائیل
۵. پیت هگست، وزیر دفاع آمریکا
۶. یسرائیل کاتس، وزیر دفاع اسرائیل
۷. برد کوپر، فرمانده سنتکام
۸. دن کین، رئیس ستاد مشترک نیروهای مسلح آمریکا
۹. ایال زمیر، رئیس ستاد کل ارتش اسرائیل
۱۰. دیوید بارنیا، رئیس سابق موساد
۱۱. تومر بار، از فرماندهان نیروی هوایی اسرائیل
۱۲. عمر تیشلر، فرمانده نیروی هوایی اسرائیل
۱۳. جان رتکلیف، رئیس سازمان اطلاعات مرکزی آمریکا (CIA)
۱۴. کن ویلسباخ، فرمانده نیروی هوایی ارتش آمریکا
۱۵. تروی مینک، وزیر نیروی هوایی آمریکا
۱۶. داریل کادل، فرمانده نیروی دریایی آمریکا
۱۷. رندی جورج، رئیس ستاد ارتش آمریکا
۱۸. ایتامار بن‌گویر، وزیر امنیت ملی اسرائیل
۱۹. رومن گافمن، رئیس موساد
#WillPayThePrice
#هزینه_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/656909" target="_blank">📅 21:37 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
