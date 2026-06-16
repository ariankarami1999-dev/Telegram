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
<img src="https://cdn4.telesco.pe/file/Z2wavl9CF3feAbtAZItZc3LGziFz6td2DJSh5O1auGFJZ7Jk79QBSVKAfHmdlSGGn7ilLtUzR9ShOc0RwmoIJbOTG69N-kc1mjmAZLZahl4fu8K9hY3cxgw8CteCWdvxMVS5k_7p0fOCbUTQejOcqzH-BI-nzdMhFlpaIOCdoUwVI2Ex4kLKrN6yfqLE0LHQOkssC6o4EZjwhP4r5QSVKIjAEXZLUGb9pqS9qVUD9hUV62cQj3Cw5AQYBzZPsP6IpxbYm-Axha0Aq5YciL0c8qNix__aQBWiUII1Py5NyWJAf9-a1g-rj1yx7lLE81HrnqqJ_DTuTNcg6c589X9Brw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 02:30:10</div>
<hr>

<div class="tg-post" id="msg-133709">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CldN1Odu30b8xP8qz_mEv5FjcgAjf1IXttCQ0fbzXQUkTb2bzSV8g4UfrpdC002cDoTEoTwY4Ii55LHIfsaDdkE3-nek9L9e_stOpwUDpC_ViyDpx5uCSLHbuNUQ1e-daQf3Mn0RqDnW3SDWAZKlpj1uHMcl1XbrAdWfDyylUdwsyTsBHzCDjuPYimeE_xWtXpQYd1p72EJIm5MV0g8mYWnT-erjkWWkS2Ajo_2BA9WJLCfpacDoM5xMaJwvpMRsqxDaagfXP9s580VSOYeytYfBhJ67IfPyCxeLMQ_XlHdRj8wxtgcFmlbRPnAiO8yLZMmbZ0CubHsXGhqx8mhdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
گروه J جام‌جهانی ۲۰۲۶
[
آرژانتین
🇦🇷
🆚
🇩🇿
الجزایر
]
⏰
بامداد چهارشنبه ساعت ۰۴:۳۰
🏟
استادیوم اروهد
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
<div class="tg-footer">👁️ 261 · <a href="https://t.me/SorkhTimes/133709" target="_blank">📅 02:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133708">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
#فوری
| سنا با محدودکردن اختیارات جنگی ترامپ در قبال ایران مخالفت کرد
🔻
سنای آمریکا روز سه‌شنبه با اختلافی اندک، طرحی درباره محدودکردن اختیارات جنگی «دونالد ترامپ» را در قبال ایران رد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SorkhTimes/133708" target="_blank">📅 01:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133707">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLUCQNzzK-xtIvzHIoyxOU0RdJmqatRLtrz6V2g4jE3eClSXYyUAXMrYHrzbMQAz2JPcC7dUyDFqPnhKtTIn7CAh33Ube2IGoUmuQUrQT3avT14wagLNqqdO-1lhvbAhAHajBrszw0C0OJb_c11eHPYgT4eQHSKixCCqBTyG2xAwCJHjWqN9QOprurr4tRa5PIS3UeNnRc1HT0dxPyUyIuA5cQSQmzhLdoXTt0yD7aweIA1pqK5pbfmfrAM-yzcwGCxOqNyQ4Cklwl-Eh72Ey4uNdJ91ojiYpQUKWXYA6QoVMHY69wwUhRKO9WADDzGD_g3B-y2_z0C37P2r2ZO_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
پست اینستاگرامی اکبر عبدی با عکسی در کنار علی دایی در بیمارستان
🔴
علی دایی، اسطوره فوتبال ایران، با اکبر عبدی، بازیگر سینما و تلویزیون که در هفته‌های گذشته دچار حمله قلبی شده بود، دیدار کرده و جویای حال او شد.
🔴
اکبر عبدی با انتشار این تصویر در اینستاگرام، از علی دایی بابت پیگیری احوال خود، قدردانی کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/SorkhTimes/133707" target="_blank">📅 01:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133706">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad4cd3bf3.webm?token=jwo28gfftulsYRLzfW7d_CgAJ88YZuWD2rJc-HcvAriFIL7MYSbzSAD7Du66t5AlSVVCWNW0rA7PBjHlKMRy3aW69fyAZuVgdHycPtdjBek_go_Udl6xwvBSqPIY_DHcsGDKhCbctnVJ7B6QKm7aKOCjzg0qIZVf15G9jRbLM8IyVYlzEskJhry8tzLsrzkb3ASZXGGRtKc5xOYM4wTL1yl3wC01UlhYncxspqbgfNGSU7Uy8TKJ712HH4uZr2PZbJkvvW2hmU3ifk7xQkOeDHafyJmSsCzhgGGZ6cFlLrs7ptq8xIEELKliUO4pNKOJinNUCJ4Ocev-Z_bxjNo0UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad4cd3bf3.webm?token=jwo28gfftulsYRLzfW7d_CgAJ88YZuWD2rJc-HcvAriFIL7MYSbzSAD7Du66t5AlSVVCWNW0rA7PBjHlKMRy3aW69fyAZuVgdHycPtdjBek_go_Udl6xwvBSqPIY_DHcsGDKhCbctnVJ7B6QKm7aKOCjzg0qIZVf15G9jRbLM8IyVYlzEskJhry8tzLsrzkb3ASZXGGRtKc5xOYM4wTL1yl3wC01UlhYncxspqbgfNGSU7Uy8TKJ712HH4uZr2PZbJkvvW2hmU3ifk7xQkOeDHafyJmSsCzhgGGZ6cFlLrs7ptq8xIEELKliUO4pNKOJinNUCJ4Ocev-Z_bxjNo0UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
شنیده ها
🚨
🔸
میگن فردا از کسری طاهری رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/SorkhTimes/133706" target="_blank">📅 00:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133705">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
🚨
🚨
🚨
کسری طاهری، تیکدری و گودرزی خریدای پرسپولیسن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SorkhTimes/133705" target="_blank">📅 00:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133704">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT16Qa_dl6E00CN3b5Oo0d6yhNwTT-PGaNbz98KlcuwSXYcTHEvVTfQXiiCLQXJkIy8oqYX1mwRe22TLchtFBraV7w0ZDjCJ4WbMkemMoMhFT9jo1H4HF_MWVrcH5yA2Wz1Sp4jgCv31gKIK1y-dX1WdW2n_fqzNaLAdzwEMuWLgIQWJoulmke1M-DU3LyMxLL8i49IPPWZ7-CxU4ut2ik_ofTrPqEHPD_Fy8qYYWjaoQ9zVQNz6OduJaXO9O2o9PIGmArNPOLqyZV5uCl1sO9Qmp851fqyL2MY4IZEWpGHSray0p5QAfSUdBPfFM-MwPHQGBL2hOuqmtvqplizdSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سیدجلال: اوسمار پیشنهاد داد برگردم
❗️
صحبت‌هایی در این زمینه انجام شده و آقای اوسمار هم پیشنهاد هایی داده‌اند اما تصمیم‌ گیرنده نهایی من نیستم. این موضوع به نظر مدیران باشگاه و افرادی که درباره مسائل فنی تصمیم می‌گیرند بستگی دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SorkhTimes/133704" target="_blank">📅 00:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133703">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feaf2d5596.mp4?token=MmgBAMCu8dqbtaXDqZnQ_XC5wEAdI79fm0sRbJoL6gAWX4pRizih0l3-x9OluekFa_dhbNjQi5dgiF1uqkUCLHwTaMvv6QbJ1Wfm3Da_Zt6AaId_cl9jMDcHDjZBv7RFJVvVDGCSm9ZnIBFVxlLyjfZPQtTrjg9Qt46MegZLmyRbc-_q5PmcFU7RMkDH2DVFdNvsHdNxsg4Ev6DVsTyyvMcOWnlPkp562oSP4EW54g0jnzFjbQ4oyI3rCMOLn3TqepI25I4KEDvTQnevsHrqheoyncBm0p3G5jgqHnaOv0X1VtLf3sjQZ-nSJpP_jeTv_zqBq0clvN_4XO7y6Axoww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feaf2d5596.mp4?token=MmgBAMCu8dqbtaXDqZnQ_XC5wEAdI79fm0sRbJoL6gAWX4pRizih0l3-x9OluekFa_dhbNjQi5dgiF1uqkUCLHwTaMvv6QbJ1Wfm3Da_Zt6AaId_cl9jMDcHDjZBv7RFJVvVDGCSm9ZnIBFVxlLyjfZPQtTrjg9Qt46MegZLmyRbc-_q5PmcFU7RMkDH2DVFdNvsHdNxsg4Ev6DVsTyyvMcOWnlPkp562oSP4EW54g0jnzFjbQ4oyI3rCMOLn3TqepI25I4KEDvTQnevsHrqheoyncBm0p3G5jgqHnaOv0X1VtLf3sjQZ-nSJpP_jeTv_zqBq0clvN_4XO7y6Axoww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
‏پیروز قربانی سرمربی فجر: با
بچه‌های شیراز نیوزلند رو میبردم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/133703" target="_blank">📅 23:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133702">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
مهدی لیموچی در یکقدمی پرسپولیس/ایلنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/133702" target="_blank">📅 23:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133701">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSHYIo7WR34VMvkcuLN9v45ARzwjVt99yQoedDoTLH7YLMNtQpvY3QiGk_3aDH0qbPwfJ5wGwSqz8lBfTY38CfrqvimOlPFT9QwxkCuzf4_lqDOIkdPE3zf_dB7WP5idV6AM41YEz2OOVnhoG_Flzejyer_ekdu7XUqoMa8dpyeU8C9ZDOo3_baDN9U_Ss34xIGXl9OCL_UxXMwjd1_TxFJnao8uPrSg9dZzEOq1S9ygKLT1ER3ndEqmkV1oj69UFnzYPN3X_nlxB7HzI4YogIHsFCud2t6Qtyx82XOnO-eMXJmYuH77F5ycu4fzh5SM_VFyD2yHH-Xd4BkgniUANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان در بین ملی پوشان: میخواهم تا چهل سالگی دربالاترین‌سطح خودم فوتبال بازی کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/133701" target="_blank">📅 22:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133700">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
رامین رضاییان: شادی گل من سیاسیه اما اینجا نمیخوام دربارش صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم می کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/133700" target="_blank">📅 22:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133699">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
برنامه بازی‌های روز پنجم جام جهانی
🙄
سه‌شنبه 26 خرداد
⏰
22:30 |
🇫🇷
فرانسه
🆚
🇸🇳
سنگال
👀
چهارشنبه 27 خرداد
⏰
1:30 بامداد |
🇮🇶
عراق
🆚
🇳🇴
نروژ
⏰
4:30 صبح |
🇦🇷
آرژانتین
🆚
🇩🇿
الجزایر
⏰
7:30 صبح |
🇦🇹
اتریش
🆚
🇯🇴
اردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/133699" target="_blank">📅 22:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133698">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6uS7_Qn5PCC2rp5qm02j8mZo1IIeaJ2GHCRh0ZMd5MAO0Ds_CqxBtXTpZ4DStn4j-wGAKNUG5kOrXVdYVBlkmiyUVwdGpiiyurtyLKCTU-XE5Som8rCT22qHmNb55CDO5qMToNkvkV9EiXOPTI2vampsQiKbG42Nyqi4ayoRwU4yL9SDTMBu6eoEmCvNcCp_dmcT0Oi7fp2-Pa9UGRqDOmeo69cvMB7rkxF47SkJXntML9eUZahWlcBN-VryWzLgIBb916pAbFzkJy276OEF6HrMAOZXBfpZC_a6NCbv5R-nuShTGdN5HGM43A-E4LhsSwcOCAxt_q2tDKTlP8vXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رامین رضاییان: شادی گل من سیاسیه اما اینجا نمیخوام دربارش صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم می کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/133698" target="_blank">📅 22:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133697">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔸
نشریه‌ معتبر ESPN: علیرضا فغانی که‌ داور دیدار امشب سنگال و فرانسه‌ است اصلی‌ترین گزینه فیفا برای سوت زدن دیدار فینال جام جهانی ست، و اگر اتفاق خاصی‌ رخ ندهد علیرضا فغانی فینال رو سوت خواهد زد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/133697" target="_blank">📅 21:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133696">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaEbwEMV0rUDlPmYMjGGBYjbQdvhNtXluLJW2yCfFetO4SUScjPswyu3v33xr67qE4Hhan5HQjDEeqPaST0WqA-eEwM1j9JfBaqDO-J5aasV-xzAH9MNqFAynjw5T61SSfUylSkJctw_cuvR8i1AhHdee4nEeEwzD9g8AG0-H4pLokuB8_a-fnDbI_Bus6XD3LARR_cGR1zeWek0JwbVG5frRyFh7cFfsEk26_z2kaBjp3BdEFrfKoDBFmditV9Ak4UamglQT5A9anGSz-FJ1qwr-0iIFIcK8aRDHXfgF58x0n57DzELcOAyOZPRqZT8eIn8TPmClpB0QOwJF1BEZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
نشریه‌ معتبر ESPN: علیرضا فغانی که‌ داور دیدار امشب سنگال و فرانسه‌ است اصلی‌ترین گزینه فیفا برای سوت زدن دیدار فینال جام جهانی ست، و اگر اتفاق خاصی‌ رخ ندهد علیرضا فغانی فینال رو سوت خواهد زد
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/133696" target="_blank">📅 21:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133695">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری :
🔴
مهدی تیکدری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/133695" target="_blank">📅 21:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133694">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCRHPikJNqn-vuMplOBZ-NJwlI6576nxdchQUKnivZuXBfDt1Xmya2Lu8hO9iAt93FkCJg64HyePD7wOlsfcuoEKIivXxr8rv-8Q5EldRQO1ozqJFYKS_K8fwOoY35A5hl3IiKeZbWB2oX0yLyq1XYn5Uz3p9WkpT4Jh4i94biZFLex9dJ3UmTf6ejtWvwldx8j8tJgGleC-6y0hpOWINKn_p3thYUktpa3oX3tShf5_T8x8xNAjKecyBHzcM01Z2bfPeJXSvyG8_SX8dOhUGSXLFwGp-HcVJzVgP9BZE86YhYnIUGjKFQ8OCI5BRff53vBDaBSQKCA6JTDDEaiiOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بونوس ویژه جام‌جهانی وینکوبت ادامه دارد!
🔵
FRANCE -
⚪️
SENEGAL
⚫️
جام‌جهانی گروه I
⏰
سه‌شنبه ساعت ۲۲:۳۰
🏟
استادیوم مت‌لایف
🎁
۱۵٪ بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا هفته آینده دوشنبه ۱ تیرماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/133694" target="_blank">📅 21:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133693">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
مهدی تیکدری نژاد مدافع راست گل گهر سیرجان با عقد قراردادی سه ساله به پرسپولیس پیوست/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/133693" target="_blank">📅 21:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133692">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری :
🔴
مهدی تیکدری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/133692" target="_blank">📅 21:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133691">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⁉️
⁉️
حضور عزیزی در پرسپولیس قطعی است؛ آغاز فعالیت‌های سرپرست جدید در امور نقل‌وانتقالاتی
🕯
حضور خداداد عزیزی در پرسپولیس قطعی شده است و حتی او پیگیر برخی امورات مربوط به تیم و نقل و انتقالات نیز است.
📊
📊
عزیزی خانه خود در تهران را حدود ۱۰ روز پیش در جلسه که…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/133691" target="_blank">📅 20:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133690">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6WRjo3-D1-x8te4hxeAAgiLhiWteQJ4DJdHSXuwzj-IH6-Ei_RAa_r0K_uVRrbl8RRZZBXzFFgitqA-6xK8h4XIgYyX20dwYrF7ClbeIXVCQbEY1QScX8lv1OGyLvDYYY5TK07DWPqBt1ivxTfpbwgWhUAqUwPrejhiig33-GIuv-jDC4xQmK3vUUZkcu24E8aIBzu7qbTMrqKMAWNoQRL07CHDQocn0YCfb8lqRamHogvS5Azd4zH9Ugf-lpD21cPhwhWAOVeFBzlyG88tCqaHIpmsR2FhX1trAPOj22pazqA2QjfOdwr4whyXJGN1L7FzPmg-j7YzxeimDSFL9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری
:
🔴
مهدی تیکدری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/133690" target="_blank">📅 20:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133689">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
🚨
🚨
🚨
کسری طاهری، تیکدری و گودرزی خریدای پرسپولیسن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/133689" target="_blank">📅 20:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133688">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90353b1248.mp4?token=K_5DfZYTbN1pxYDnAup5iAv9Y5dohn8sDRZn2GnJgDI5jH4hvAgnaPHRBEzt5aC0hsy_RgRi9FppLZmKA1KVt0OAGk5QUs5TGnujZ1hTWfkRCRqx31m6Dw__f-2kzrQCs2Hb1V0sUEjJVGa-LFbpsor33KlozlgV55FzGHI_NnNr30pDZ4xVG5fVl7aH-pnqWzggAuWa2M8RIQk60dTnFMTZ7zJyCqzogeu0vbInBl3Sq1n73FlctEPR3aFKLDXnySYtSyBI7d7gAsvmxHqxN5QWhDeiQF4weYTGRXfk6YFmQ0vK432aNhN5xGfo4PBaLZiwDJ8AqQeLlG-C6rukMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90353b1248.mp4?token=K_5DfZYTbN1pxYDnAup5iAv9Y5dohn8sDRZn2GnJgDI5jH4hvAgnaPHRBEzt5aC0hsy_RgRi9FppLZmKA1KVt0OAGk5QUs5TGnujZ1hTWfkRCRqx31m6Dw__f-2kzrQCs2Hb1V0sUEjJVGa-LFbpsor33KlozlgV55FzGHI_NnNr30pDZ4xVG5fVl7aH-pnqWzggAuWa2M8RIQk60dTnFMTZ7zJyCqzogeu0vbInBl3Sq1n73FlctEPR3aFKLDXnySYtSyBI7d7gAsvmxHqxN5QWhDeiQF4weYTGRXfk6YFmQ0vK432aNhN5xGfo4PBaLZiwDJ8AqQeLlG-C6rukMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سرمربی پرسپولیس: خوشحالم که دوباره به ایران برگشتم. منتظر تصمیم فدراسیون برای برگزاری بازی‌ها هستیم. آماده‌ایم به هدف هوادارها در رسیدن به آسیا برسیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/133688" target="_blank">📅 19:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133687">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56204fee3b.mp4?token=JL2W2BceqDD3zxGBzaIOB_ky_jVzZmfG9tual5ESo_HVyA7T-GP36mTEW83_GuLlbQ6sJUz3b03RKn7viE1kcCdDwG6y0j4gCRyXWaPRV57MKHY0qC4Fn9XX8lXmyh7CE6YAOUP2BZXesdeHOR-o6JRmxd4lz-C0o1q9dqEhqSK4SVsFAcwMw91qoZv4jqKb07GsNOnsU44LTU1y0JyhYF-kB7DK7wo00nkvwnqfNp_GXljVLare6kU9Ul-C1atZi9TIEh_jKL_mTD56AePAZNsenu_Vp5usEBo5U0kCsSrakNTP5x0F-wtJ88xreQR5lw54iR0JTRxeysKWO5XHP3h7NEtVgjNnju04IQazZxHmWGH0VfK9kntgP6CgFpHbx0YTdqtMP2BBx3vsnDySgDJPpsr3B6VK8ZvLAENZRiU0k4osU0GDKw7N2TzNYBppSACMMebORef7n6SewK0rFH7GZFsaHWRhHH2F-bqpyGYe98faIKEZu1hFudfye2IejQ9UJhHfOcLr1wWP5iL5t3dL60MdCOF6IIDF4eQXC1cqqZ97OGZ10J8y4HaiLuYeJ0tf20aO_8kZaM-5lypLMyukZr75E0AhG59fK-u3KN_8G7B8hP_rAniHhlVQj-VSae_EYbFu1H38CbT1TNcbijvGy83foY1kj98uWhlRrOI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56204fee3b.mp4?token=JL2W2BceqDD3zxGBzaIOB_ky_jVzZmfG9tual5ESo_HVyA7T-GP36mTEW83_GuLlbQ6sJUz3b03RKn7viE1kcCdDwG6y0j4gCRyXWaPRV57MKHY0qC4Fn9XX8lXmyh7CE6YAOUP2BZXesdeHOR-o6JRmxd4lz-C0o1q9dqEhqSK4SVsFAcwMw91qoZv4jqKb07GsNOnsU44LTU1y0JyhYF-kB7DK7wo00nkvwnqfNp_GXljVLare6kU9Ul-C1atZi9TIEh_jKL_mTD56AePAZNsenu_Vp5usEBo5U0kCsSrakNTP5x0F-wtJ88xreQR5lw54iR0JTRxeysKWO5XHP3h7NEtVgjNnju04IQazZxHmWGH0VfK9kntgP6CgFpHbx0YTdqtMP2BBx3vsnDySgDJPpsr3B6VK8ZvLAENZRiU0k4osU0GDKw7N2TzNYBppSACMMebORef7n6SewK0rFH7GZFsaHWRhHH2F-bqpyGYe98faIKEZu1hFudfye2IejQ9UJhHfOcLr1wWP5iL5t3dL60MdCOF6IIDF4eQXC1cqqZ97OGZ10J8y4HaiLuYeJ0tf20aO_8kZaM-5lypLMyukZr75E0AhG59fK-u3KN_8G7B8hP_rAniHhlVQj-VSae_EYbFu1H38CbT1TNcbijvGy83foY1kj98uWhlRrOI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اوسمار سرمربی پرسپولیس: اگر تصمیم گرفته شود که بازی‌ها برگزار شود ما آماده هستیم/ اول باید تکلیف کادر فنی مشخص شود بعد سراغ لیست بازیکنانم خواهیم رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/133687" target="_blank">📅 19:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133686">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
اوسمار سرمربی پرسپولیس: بازی‌های لیگ می توانست برگزار شود/ تیم ملی ایران نیمه دوم بازی خوبی مقابل نیوزیلند انجام داد
🚨
بازی‌های بعدی تیم ملی می تواند عملکرد خوبی داشته باشد
🚨
بازیکنان خارجی تیم همراه ما هستند/ سروش رفیعی؟ تصمیم شخصی خودش بوده است که هراه تیم نباشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/133686" target="_blank">📅 19:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133685">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7b067e8b9.mp4?token=M3SompUEMWCKSagb8JrQMIAtIFHoTMSQ3MX38tYn-uXGi12S2I3cevaCHYbc09WNqng7Oor3hkbqIwJeNRx1dunAMhVD42TKK-jECO0M_v_xKbQ0yqTs0HHGieKiu00BPUkcA2JmQnkJDWLoItbcVLSKNhmCpa2qRA7eUe8Lh4sZVURfkFvNmQ7VjmS12-cacTrgoDJxVQ4kWeftQEa3VP937Mi0nJpUxIJcBmcGP0ffrEi1shrAUDWNKJcv-ZkocXjkw2pnUdSnYfCGMq78LEave6j-rfZ8OF_Lts8hFfaxkyr-XqUK132lVJAe-g9jRX2pQ5jZAAbDo36cgrxJzGguNyQVG9kjF8Jm-y3flTQYX3uPWdaP4Abfhgr7S3ak2GuaXIdRAK4HU2fhK405asl2cmxChgswrD2lPhjUaYc-9dCssQGM3vCRziAeUJm19rBlb1xgJKgaWkMptM8fvSrOrTPJ8naxXSzg_J3kNCBa9y2A1L4TRI7V5I6bXqQW1fhjrBhNotzxuO403DjBvDgJYzQ_ZDsDkNF3r-ee8uskWphwJYV_g6P2QHnO4ihawuegXJ-7nhIKrh4kaf_olzLkCYzrvYqSYWFf016BeSXAOgcBVeG59BrMxUjFG7ujENYOj2nPpV4jHHsqqEWog8v9pIkGPBbJej16Q3mQw_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7b067e8b9.mp4?token=M3SompUEMWCKSagb8JrQMIAtIFHoTMSQ3MX38tYn-uXGi12S2I3cevaCHYbc09WNqng7Oor3hkbqIwJeNRx1dunAMhVD42TKK-jECO0M_v_xKbQ0yqTs0HHGieKiu00BPUkcA2JmQnkJDWLoItbcVLSKNhmCpa2qRA7eUe8Lh4sZVURfkFvNmQ7VjmS12-cacTrgoDJxVQ4kWeftQEa3VP937Mi0nJpUxIJcBmcGP0ffrEi1shrAUDWNKJcv-ZkocXjkw2pnUdSnYfCGMq78LEave6j-rfZ8OF_Lts8hFfaxkyr-XqUK132lVJAe-g9jRX2pQ5jZAAbDo36cgrxJzGguNyQVG9kjF8Jm-y3flTQYX3uPWdaP4Abfhgr7S3ak2GuaXIdRAK4HU2fhK405asl2cmxChgswrD2lPhjUaYc-9dCssQGM3vCRziAeUJm19rBlb1xgJKgaWkMptM8fvSrOrTPJ8naxXSzg_J3kNCBa9y2A1L4TRI7V5I6bXqQW1fhjrBhNotzxuO403DjBvDgJYzQ_ZDsDkNF3r-ee8uskWphwJYV_g6P2QHnO4ihawuegXJ-7nhIKrh4kaf_olzLkCYzrvYqSYWFf016BeSXAOgcBVeG59BrMxUjFG7ujENYOj2nPpV4jHHsqqEWog8v9pIkGPBbJej16Q3mQw_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
اوسمار سرمربی پرسپولیس: مدیران پرسپولیس کارشان را به خوبی انجام می دهند و به ما کمک می کنند/  دعوت امیرحسین محمودی به تیم ملی؟ ج اگر چه در لیست نهایی تیم ملی قرار نگرفت اما حضور در کنار تیم هم تجربه خوبی برای اوست.
✅
مارکو باکیچ ، بیفوما و دنیل گرا نفرات خارجی پرسپولیس در تمرین امروز حضور داشتند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/133685" target="_blank">📅 19:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133684">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f00ec62d09.mp4?token=NrejpX2R5OM69GKmjDO5ml3ueae93mmZTrJMVGKe1pBuubEdWbv2W7-k3e9sBk32Gmp6u7sNTSgR0-schV-cTMW750B4Am5B3HF9F2QweAR-gSgvIO-XYdzi9I4N1TiXL2kwbjAfsIsCAASDyRhr7gLJaVry2Rb-AsdX_VXMwm5BleET3wT0DUkAtXuE5MYn-Orw2dtQtgXo8j9rZ5uwGprrwj4RzuIOkTLCbloV5Kvy2eYXHbNv30jMqnyoeJrAy-wonJKM4XYHdlx1OA5J0gN0kDwIZQ5FO7yi4s_kEd7sogoRsBWE6XhnvqEvI8IdZcMTTIlFGs_7bIl_rAcCag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f00ec62d09.mp4?token=NrejpX2R5OM69GKmjDO5ml3ueae93mmZTrJMVGKe1pBuubEdWbv2W7-k3e9sBk32Gmp6u7sNTSgR0-schV-cTMW750B4Am5B3HF9F2QweAR-gSgvIO-XYdzi9I4N1TiXL2kwbjAfsIsCAASDyRhr7gLJaVry2Rb-AsdX_VXMwm5BleET3wT0DUkAtXuE5MYn-Orw2dtQtgXo8j9rZ5uwGprrwj4RzuIOkTLCbloV5Kvy2eYXHbNv30jMqnyoeJrAy-wonJKM4XYHdlx1OA5J0gN0kDwIZQ5FO7yi4s_kEd7sogoRsBWE6XhnvqEvI8IdZcMTTIlFGs_7bIl_rAcCag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اوسمار سرمربی پرسپولیس: تا وقتی این فصل تمام نشود لیستی اعلام نخواهد شد/ یاسین سلمانی؟  خودش فهمیده است که اشتباهاتی داشته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/133684" target="_blank">📅 19:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133683">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❗️
❗️
اوسمار:فدراسیون می توانست بازی های لیگ را برگزار کند.مدلهای دیگری هم برای انتخاب تیم ها برای آسیا بود
💬
به خاطر فشارهای غیر فوتبالی روی تیم تاثیر گذاشته بود اما در بازی های بعدی جبران می کنند
💬
وضعیت سروش رفیعی و تمرین امیری در کنار پرسپولیس؟ در مدتی…</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/133683" target="_blank">📅 19:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133682">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
نمایی از تمرینات پرسپولیس در حضور وحید امیری و با اضافه شدن تیوی بیفوما، محمدحسین صادقی و فرزین معامله‌گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/133682" target="_blank">📅 19:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133681">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be8a9600b.mp4?token=sVqtdMRBBpo9Ht4QyeaNBx0wjfzgYXdRqvT6ulXTxAaB_fZDnCUYIyrukz105l4DfuDcJ1hngVJpvOMR6nAeWpp4EAo6gcKbvgsFOScrIawXL9YkL0VPAOXkEAwdh_IjjjiJDjA_s5jF335RJIj58Ezff39H6Vd_APn9HegyxqxaND9dIuuS4t_GTT5S6xvgtxyKqn1gVkQOFXMEXAN3XV_ILJmPsvYnM3EpfDLIx_z4J8ycwkMx7g98kqJXlKyrG16-AGo5x1GZegX0guxeTJzTwRmTqze5uQ1KIC_0c5KgEHCAqlU-Kvs5H0_5AT_8jA3a8vI_oB9QZD_hEMht_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be8a9600b.mp4?token=sVqtdMRBBpo9Ht4QyeaNBx0wjfzgYXdRqvT6ulXTxAaB_fZDnCUYIyrukz105l4DfuDcJ1hngVJpvOMR6nAeWpp4EAo6gcKbvgsFOScrIawXL9YkL0VPAOXkEAwdh_IjjjiJDjA_s5jF335RJIj58Ezff39H6Vd_APn9HegyxqxaND9dIuuS4t_GTT5S6xvgtxyKqn1gVkQOFXMEXAN3XV_ILJmPsvYnM3EpfDLIx_z4J8ycwkMx7g98kqJXlKyrG16-AGo5x1GZegX0guxeTJzTwRmTqze5uQ1KIC_0c5KgEHCAqlU-Kvs5H0_5AT_8jA3a8vI_oB9QZD_hEMht_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نمایی از تمرینات پرسپولیس در حضور وحید امیری و با اضافه شدن تیوی بیفوما، محمدحسین صادقی و فرزین معامله‌گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/133681" target="_blank">📅 19:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133680">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
ترامپ: متن تفاهم‌نامه را نه تنها منتشر می‌کنم، بلکه احتمالاً یک نشست خبری برگزار می‌کنم و آن را کلمه‌به‌کلمه می‌خوانم تا رسانه‌ها آن را به‌درستی پوشش دهند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/133680" target="_blank">📅 18:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133679">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1srkvDRTSB6HZRoEE1LGi1QwfENAy7g8vyY_pJSgaHeoqbjrEvShcq-BnOR58i95P0YUTP9B1Ci-5XQfo5h2cKDqSh7yQDtX-JFa_XdCmfr_hxgjiQhap_nvppU9LVaCQU0FGs4NnB43LFtDNFzF5rkGC_AKDCtcJJ9lwE8P5sGgzEuE4aiTaab6HssBjcNAcl1rCRoPadC0UEBFQuo31xFaEJDiQIJ0LsmQBnO48N_KUidZMmfUpsbe41IxACSHGjqdDqnrzt1uZxUnEzJ3-1PaeGjyMTglq8j2Ko6Ua19ozh9h0vbQEdhsLoPumvfrR_TtNWALHh2TBjoCySrIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
مثل اینکه قراره جمعه توافق اولیه تو همچین جایی امضا بشه
🇮🇷
❤️
روستای بورگنستوگ تو مرکز سوئیس که تا حالا میزبان کنفرانس‌های صلح زیادی بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/133679" target="_blank">📅 18:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133678">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123eaa1e7a.mp4?token=vSppA_BGkvllYMXwm6vCZbayNoyVcnpWHjV0H0jIoz3WR_Nd4Mz0hGzq2sJKE6ozfM-KO-16t1QKfmJkRaP9W_vGer26fPSFPD5SzQtODYpY-G1jSJm8HtjqG12nfbzQhj4vZzzjjxa_umsNo7LM_ZUdMYiSmdy0vkRlYcEreZq7eNn2mzV8LA05ArQpunBNkxmPVTJ5DtZfIaAAhtsYcoIPp1VYwceBc63BbF7NX4NiDYUHZL3tZa8JjCMhb0o_Oxr5Q6AjBj3tsRCYU0TiE-02_8Hr240cIeR5PsEchpDikynfqybT1xkYNgI6mii4o_Q0M88wadCWe2KCwefjoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123eaa1e7a.mp4?token=vSppA_BGkvllYMXwm6vCZbayNoyVcnpWHjV0H0jIoz3WR_Nd4Mz0hGzq2sJKE6ozfM-KO-16t1QKfmJkRaP9W_vGer26fPSFPD5SzQtODYpY-G1jSJm8HtjqG12nfbzQhj4vZzzjjxa_umsNo7LM_ZUdMYiSmdy0vkRlYcEreZq7eNn2mzV8LA05ArQpunBNkxmPVTJ5DtZfIaAAhtsYcoIPp1VYwceBc63BbF7NX4NiDYUHZL3tZa8JjCMhb0o_Oxr5Q6AjBj3tsRCYU0TiE-02_8Hr240cIeR5PsEchpDikynfqybT1xkYNgI6mii4o_Q0M88wadCWe2KCwefjoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظاتی از تمرین امروز پرسپولیس باحضور کریم باقری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/133678" target="_blank">📅 18:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133677">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
ترامپ: چیزی که مرا به امضای این یادداشت تفاهم ترغیب کرد، اطمینان از این بود که ایران سلاح هسته‌ای نداشته باشد.
❗️
اگر ایران به دنبال دستیابی به سلاح هسته‌ای باشد، جهنمی به پا خواهد شد.
❗️
ترامپ: ایران طبق توافق هسته‌ای به سلاح هسته‌ای دست نخواهد یافت
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/133677" target="_blank">📅 18:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133676">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❗️
❗️
خبر پیشنهاد به اسکوچیج دارد فراگیر و جدی می شود.
🔴
تکلیف کادر فنی را مشخص کنید بعد بازیکن بگیرید.اینکه فلانی خیلی خوبه و همه مربیان او را می خواهند استدلال زیبایی نیست.دو فصل اخیر هم با همین فرمول تیم بسته شد و یک سوم خریدها هم با نظر گاریدو و هاشمیان…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/133676" target="_blank">📅 16:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133675">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
انتقاد مهدی طارمی از ندادن ویزا به برخی از اعضای تیم ملی:
❗️
فیفا به ما گفته است که همین الان لس آنجلس را ترک کنید/ در صورتی که ما باید فردا صبح ریکاوری انجام می دادیم/ حقیقت را بگویم شرایط برای ما فاجعه است، هیچ ارتباطی با فیفا نداریم/ رییس فدراسیون و نایب…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/133675" target="_blank">📅 16:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133673">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
امروز صبح در فرودگاه لس‌آنجلس، مهدی طارمی و سعید الهویی هنگام بازگشت به تیخوانا، چند ساعت توسط مأموران نگه داشته شدند و از آن‌ها بازجویی شد. در نهایت، پس از پیگیری‌های فیفا و فشارهای فدراسیون فوتبال، اجازه خروج برای آن‌ها صادر شد.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/133673" target="_blank">📅 16:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133672">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⚠️
⚠️
فوووری از ورزش سه: کسری طاهری مهاجم روبین‌کازان با پرسپولیس به توافق نهایی رسیده و بزودی از او رونمایی می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/133672" target="_blank">📅 15:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133671">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
مهدی لیموچی در یکقدمی پرسپولیس/ایلنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/133671" target="_blank">📅 15:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133670">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
✅
با اوسمار هنوز تمدید نکردن ولی با بازیکنای مدنظرش مذاکره کردن و تهشم رفتن به یه مربی خارجی گفتن بیا تیم ما/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/133670" target="_blank">📅 14:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133669">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxN5k10rjUccY2eL5zpcHzOxBwp_Sf8lnrmjd8f1ZVaU9M0-ZdNiqH0ZNm61b-sC1y4wSZnSgwbyDIFLyxAJ4TJ7Gctz3Xbnajh3AoBmWmoy8D35CsgVdX0Hq_VmryxdL2P_YYx5PEf6MZcVW007IuMjvsZjbiSmCdc0WF3bKpktt3FT_8JXQLx6NzjVF-nnlgpl_kCy9gifjCHFKUBKiXEo3N5KHxP5P9I9DhS_vaxAJVhRm6gSgk3dHjr_4yDocMKgvahjqmllW8GjlzaOp0EG5LZmcsVsKGfQDPicUpyDfLgfApXkiirnLEEdYOxNPSdsU4ZbW0J8iaoXUtZJ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امروز صبح در فرودگاه لس‌آنجلس، مهدی طارمی و سعید الهویی هنگام بازگشت به تیخوانا، چند ساعت توسط مأموران نگه داشته شدند و از آن‌ها بازجویی شد. در نهایت، پس از پیگیری‌های فیفا و فشارهای فدراسیون فوتبال، اجازه خروج برای آن‌ها صادر شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/133669" target="_blank">📅 14:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133668">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GG0X6nWPveLilH1Rw2SAfQF8ROUvsFaVcGUgZT5T2UX_1ahRO0w7wM6XHY85CqvmLk08sErY2TJAn9LbFIPSjWTLmNsOnXZp5k6Kj-uJuXtK_Pi59aX2jFdokF5wsJyTM-KM5zFMTNKo3LEDHLwCE6EBdQYDdRfbgYqe1y_SvLyXcUlKuH88litQl-MICxqknwWK72SwW0L8jGLsKakIO5ktR5OJPMeLag90P9keMxAxoihyx5lXBKuQweTzCRSKpVTC_90O3g_ttkqMWaDTO1f9tcJ31wjWi1KrziFNl8sjf8dB0lpKj39lm36A1RwHAxNzEgS0rw1nxqxG21QEng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قلعه‌نویی همینو قاب می‌کنه میزنه دیوار منزل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/133668" target="_blank">📅 14:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133667">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/133667" target="_blank">📅 14:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133666">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rjD1TQXAJVC2UWaUsXkeP_2thIxW7KdcfG8rSsW11Oh9Ynr5KVmMTuiYNmVtwAl89trRkgugY4f07Vjp-HggcuekEshk69AzwDi_w3Yxxe-elxtmEM72cP6L8U-dK8t8ksQ3J_xTVPJEd962-drMwFsYzr3JM_7S50OTnMQbYlEmbjpCXY7j1NJAjsXFq3Hay9sBxVGrnGruaX0h5HJLYJ9cIBuYF7kHGU3K33UQxBI5G3uYOg2qYMUi2-CAKFIaX8cEFw1nQToBsjZu-5kb-zYsj-a9g0seiSM5PZ01UIxxw9aJgvHOZxeIkQjCHJr98HU1bH6QJeY4EtJTbkXdiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بونوس ویژه جام‌جهانی وینکوبت ادامه دارد!
🎁
۱۵٪ بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا هفته آینده دوشنبه ۱ تیرماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/133666" target="_blank">📅 14:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133665">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❗️
❗️
فرهیختگان: لیست خرید پرسپولیس شامل طاهری، یوسفی، لیموچی، زارع، محبی، نوراللهی، مغانلو، ایری و اون یکی محبی هستش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/133665" target="_blank">📅 14:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133664">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCwZzcy0nNuHrMC31S7RyuuKSuICE7-4FiM8Nniml7bDxMabp--czMjiJgWwZPxODt9Sp3IvfALHoYubQfHjwOkxC-e3zmVS_vDaPMCBAcKz5vYhctGnej6CSiEkocM1DxJdr6pb8DG08dzpw6Zx5Ag0QQ1tqV0plG30QKZfZrqYtLs1_z3VY-yZRTa-BRCGTkyd91SM0tAigZtmCbIW-ywLanwZNsK6NHTipcLqI1BOKDPhLH09HMtuMVejIovU3OJDBkvctod2HEiGYvqlaRmK7gAdEGWQAjGWl3qAPgbfIrSDR1KFSmaOzg5IzWOvBrFy4DRHKM_KIoTHno7b5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🫪
برگ ریزون
😳
🔽
دروازه بان کیپ ورد که جلوی اسپانیا کلین شیت کرد توی کمتر از ۱۲ ساعت فالوراش از ۵۰ کا شد ۶ میلیون
🔥
🔥
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/133664" target="_blank">📅 14:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133663">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
یکی از نزدیکان احمد نور به ما گفت؛ احمد تو ایران فقط و فقط لباس پرسپولیس رو بر تن می کنه
🔴
همه ما زیاد از این حرف ها شنیدیم اما تو این مورد، مادامی که پرسپولیس خواهان احمد نور باشه، این هافبک تو ایران انتخاب اول و آخرش مشخص است.///طاهرخانی
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/133663" target="_blank">📅 14:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133662">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
ترامپ: من به تغییر رژیم اعتقاد ندارم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/133662" target="_blank">📅 13:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133661">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
✅
ترامپ: تلاش‌هایی برای تغییر رژیم در ایران صورت گرفت، اما موفق نشدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/133661" target="_blank">📅 13:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133660">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇺🇸
🇺🇸
ترامپ: من علاقه ای به تغییر رژیم در ایران نداشته و ندارم. تحریم های ایران طبق توافق برداشته می شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/133660" target="_blank">📅 13:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133659">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4Y4CvaLjQafSPzrkpfYvGcAIt066cL7M1EC0PvxcdtI3MIvaWohlDpwZR4h0ArRDVea7fKOv402NhjWhzb5zn86Wfs4ISjSSSRAP46ulpUQjuB7titZnpiv9nivM-_Gt4WTuF2pFHTZhILaX6vXuWmQjg7QAZLL0tAWg3HEOEKreG2qbBtosvOrmqwotA-JMVjmLHCDf21wSc2OnX9C4wpWRljmQckBMj10lsVgVXv7DcjQokSWRUBtYgYIvJ8KKagza4oOuhywipu8PJ2PCU5wviWaVRdvsd1hL8LT42GYWhKrh4sX-5wsM2mHy8apsrh4SagS3NrE__y0jwSjBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو کشت انجام میدی.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/133659" target="_blank">📅 12:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133658">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/402b94c148.mp4?token=cYi4h5mzgvO3CtEKWmWvoc60520jU7z4cf2QdetZkz-5RCU-lAmTRDcaI4GH4FXHFoH3T9GFD-LWlWUJo82oICSABarqVIc2JiaXSGl5p9WqRXr7PhH5_AOVpaFXu4OgOCHFJlIejtb7XEIz1cKIqicmNt2v0gi9kGRVaa67UKEFpKs8PWfsVTC7M5ZdKRkxfRad6BcPra_PL4Y2QHVW1-vN51yyZ9LkJX0V8GxHVLePfVZP1U3s2En8Q8sMDpckdimLjaqAajhNKF9Kgxex2EMU-BdSzV_3-P2eMMvnMwHPhKLuOzYOk6hYKXT8hywgY73QsjYj98KGLCgFC1C96A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/402b94c148.mp4?token=cYi4h5mzgvO3CtEKWmWvoc60520jU7z4cf2QdetZkz-5RCU-lAmTRDcaI4GH4FXHFoH3T9GFD-LWlWUJo82oICSABarqVIc2JiaXSGl5p9WqRXr7PhH5_AOVpaFXu4OgOCHFJlIejtb7XEIz1cKIqicmNt2v0gi9kGRVaa67UKEFpKs8PWfsVTC7M5ZdKRkxfRad6BcPra_PL4Y2QHVW1-vN51yyZ9LkJX0V8GxHVLePfVZP1U3s2En8Q8sMDpckdimLjaqAajhNKF9Kgxex2EMU-BdSzV_3-P2eMMvnMwHPhKLuOzYOk6hYKXT8hywgY73QsjYj98KGLCgFC1C96A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
انتقاد مهدی طارمی از ندادن ویزا به برخی از اعضای تیم ملی:
❗️
فیفا به ما گفته است که همین الان لس آنجلس را ترک کنید/ در صورتی که ما باید فردا صبح ریکاوری انجام می دادیم/ حقیقت را بگویم شرایط برای ما فاجعه است، هیچ ارتباطی با فیفا نداریم/ رییس فدراسیون و نایب رییس را نداریم و برای مثال آنالیزور تیم مجبور است کار رسانه انجام دهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/133658" target="_blank">📅 12:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133657">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
✅
با اوسمار هنوز تمدید نکردن ولی با بازیکنای مدنظرش مذاکره کردن و تهشم رفتن به یه مربی خارجی گفتن بیا تیم ما/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/133657" target="_blank">📅 12:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133656">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
مهدی ترابی: در گذشته زیاد آهنگای تتلو گوش میدادم و تتلیتی بودم، اسطوره ورزشیم علی دایی هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/133656" target="_blank">📅 11:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133655">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
این شادی گل جنجالی محبی که به شکل اسلحه به دست هواداران بوده، به سوژه رسانه های خارجی تبدیل شده و خیلیا این خوشحالی رو تهدید کردن آمریکا تلقی کردند و سعی دارن این بازیکن رو محروم کنند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/133655" target="_blank">📅 11:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133654">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❗️
❗️
احتمالاً اسکوچیچ سرمربی بعدی پرسپولیسه/طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/133654" target="_blank">📅 09:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133653">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
اسکوچیچ مربیه خوبیه هیچ شکی نیست ولی 2 میلیون دلار ففط خودش مسلمون ها؟! چقدر مگه روش میخاید بخورید البته حق دارن تعداد بالاست
😄
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/133653" target="_blank">📅 09:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133652">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV1kKpi79-Z6NZg8oaYPv298m3UlUjgHAXmYS5PHwO8hADftghDEXtSO8WLP9Q762ij7e3SKA9w9ozPgTqggocNAjIulHxHbzGi6Glbf9mutjm_J5fipEK1h290dhz5yztKlxdLKfkUbm19ATbvtdIhhhKueBrfjiZkcVtSm0KdpJzzVYrAYBDUe8eR2WGoyv8Amn1YVzCrVRtvdmUxHfRY8VU2_FQkFk7tiTkVky6KiUejy6lixlT8kdgUadxrccYqUi5VXueC5gGHzodyPurQceUMAITO-6TgNpYo6B6uYZqHtWa1OPe8aH4kYXajyaNQK-slPSJyS5FUkjABTRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
استادیوم سوفی لس‌آنجلس که بازی ایران و نیوزلند توش برگزار شد گرونترین استادیوم جهانه و تو ۴ سال با ۵.۵ میلیارد دلار هزینه ساختنش و سقفش از بدنه ورزشگاه جداست و بزرگترین نمایشگر ۳۶۰ درجه ورزشی دنیا با کیفیت 4K رو داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/133652" target="_blank">📅 09:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133651">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=Y3vvJyNfZdbCNpN6IUA025XHGgfFAaak4_PTWSo55cBm6zpwRCqhDhEj8_Q0QZ9gNKa3NmFnPkOknFsDXDBmfgppupRlaj4xBnHKlAEHh9Q8YZcHoQMvQwjpAhOjdD0ec3O5wmRPmShZitz_XfnlGgIS1V7OoDnoHZBGf9gq5m4q33YoZMVLLXtxnvZLT2KZxw7ZynXiagBSUGXO0vr-fM8796pdYDVV7itvgBSYUDGtYwe69vvO5SkZNM1ZjiAVGOK18Tqd0dCBiAw3nn0T_6H_oSq5qzlw-6wbXIVgaN_T1qwDDpvY_rtZPihmGq_cSkVIua3Eb0rY17hvj0v45A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=Y3vvJyNfZdbCNpN6IUA025XHGgfFAaak4_PTWSo55cBm6zpwRCqhDhEj8_Q0QZ9gNKa3NmFnPkOknFsDXDBmfgppupRlaj4xBnHKlAEHh9Q8YZcHoQMvQwjpAhOjdD0ec3O5wmRPmShZitz_XfnlGgIS1V7OoDnoHZBGf9gq5m4q33YoZMVLLXtxnvZLT2KZxw7ZynXiagBSUGXO0vr-fM8796pdYDVV7itvgBSYUDGtYwe69vvO5SkZNM1ZjiAVGOK18Tqd0dCBiAw3nn0T_6H_oSq5qzlw-6wbXIVgaN_T1qwDDpvY_rtZPihmGq_cSkVIua3Eb0rY17hvj0v45A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
این شادی گل جنجالی محبی که به شکل اسلحه به دست هواداران بوده، به سوژه رسانه های خارجی تبدیل شده و خیلیا این خوشحالی رو تهدید کردن آمریکا تلقی کردند و سعی دارن این بازیکن رو محروم کنند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/133651" target="_blank">📅 09:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133650">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
اینفانتینو به رختکن ایران آمد
🔴
تمجید رئیس فیفا از عملکرد تیم ملی در بازی برابر نیوزیلند و گلایه قلعه‌نویی از رفتار میزبان علیه ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/133650" target="_blank">📅 09:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133649">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378c7d7f9a.mp4?token=F4e7xfCqNXmKbn3R2LZ60Xt7MNYVdrtV8Jw8GfcfQJSVvZqbxlAdxN-4aiyNh7ddEBGlfuwBzUV8dLT_001PH5qc7-4vXPKV9VtQBsmWLjbZGqSZf8BA1NMp8zTaYOJ2kkX1ZTPB8z9nL3ke9I_758OyMwptDSppwxWqRl30gIi57NVH_fNrfFRlvQX-4tG6NcktxqhmRbEdJPXeV3RSEhwIjGyhHSE5qthuiepQYkOq0Xh0tTGTZF3dG2wGJddBoKnBMZdReBOk8r82Gb-U4UhvfSPrOv_BVfbBQ8mbVE5MImKUnxglo7EUVLTmmRUCYDWHGjjGccqBP9NPDqyNoRFANJQKJzboDiWzJqn_oSNPff3Xk51mibSRjhTKNyFBS8A2pMz9ClI5RhNYsvCDpTLMw_EtyOcg9huII6uN-z4vH6mZ0ZVAk1aiZk6LcfoxtRvyrlyWPTOxbKciUQjIkrcviSU-lggmGjUHvKgLKlMijDi9lYOtxI-uJAnCQwX-k4ZBrltHYWW41wp2SuhgMP4rrUy0a9b1SNx2IBU5om4nfR0FJpCOvlF3DbwzDnlgclNh7aCFoP9QQbcl0eoIJythstIVdu3Qzcxyy0WSW3h8IzqKNfEmd53BgdsrFbbupnG0SH1HfD16yze0opxI6_8ws7CFpATkEmmRusmzezY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378c7d7f9a.mp4?token=F4e7xfCqNXmKbn3R2LZ60Xt7MNYVdrtV8Jw8GfcfQJSVvZqbxlAdxN-4aiyNh7ddEBGlfuwBzUV8dLT_001PH5qc7-4vXPKV9VtQBsmWLjbZGqSZf8BA1NMp8zTaYOJ2kkX1ZTPB8z9nL3ke9I_758OyMwptDSppwxWqRl30gIi57NVH_fNrfFRlvQX-4tG6NcktxqhmRbEdJPXeV3RSEhwIjGyhHSE5qthuiepQYkOq0Xh0tTGTZF3dG2wGJddBoKnBMZdReBOk8r82Gb-U4UhvfSPrOv_BVfbBQ8mbVE5MImKUnxglo7EUVLTmmRUCYDWHGjjGccqBP9NPDqyNoRFANJQKJzboDiWzJqn_oSNPff3Xk51mibSRjhTKNyFBS8A2pMz9ClI5RhNYsvCDpTLMw_EtyOcg9huII6uN-z4vH6mZ0ZVAk1aiZk6LcfoxtRvyrlyWPTOxbKciUQjIkrcviSU-lggmGjUHvKgLKlMijDi9lYOtxI-uJAnCQwX-k4ZBrltHYWW41wp2SuhgMP4rrUy0a9b1SNx2IBU5om4nfR0FJpCOvlF3DbwzDnlgclNh7aCFoP9QQbcl0eoIJythstIVdu3Qzcxyy0WSW3h8IzqKNfEmd53BgdsrFbbupnG0SH1HfD16yze0opxI6_8ws7CFpATkEmmRusmzezY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
قلعه‌نویی: این بازی بهترین بازی دور اول بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/133649" target="_blank">📅 09:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133648">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FopiHk5RFdF5VYGsCGRjKaKoDLqNMXywcMLNPRCIUf4-_B4Mng2MvB1B6q8uJpoyXBH_o5ypoKAL6ZdL48ARcN7V0Bx0KQOws1WIMQUkbSTtv_p-MK-OlHxyrn30QK2YZfbcjGZYKC855CNKuXPoo-Nkt52VpftjWk1xKbN88bYmT7y-lOQczsGI-hmbizoQqWO2bkZKzeIijNpih0qqVIPsU14Cdeeg_lS2bTmdlKbF-ZhR1frBgqqFjNzMw2AVPJMy9qa8hlG5_4f9x1sglf-f2GkZ1OwXLpMD0ajOvX1O-hsW3pk_TAIdcT4s0keeVZmPhk_sqq5qD0O1ndAkrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
70 هزار و 108 نفر تماشاگر بازی ایران - نیوزیلند در استادیوم سوفای بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133648" target="_blank">📅 09:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133647">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKHy-7nBumjPW1RZB576j-3iNxy3JlDVvZqCZnwA8JWkR490NCJjcOU1_C8tI3PZKJ3xoir6qZ4YDDa3GDLczim76m8-UJumGHk2VaXhKELz_cPoqB4dm6ewDigFIxE2cRA0CvvFchger0zH1MQBt0k7YACghjg9UtVeBfcXMv5A9ZLkrWYdKsuhI0LWuwskLdYgPJ0CsmggWsLYMW1AQc_7DXJhiRW3Psvxcl4vWN6NNn6wQcGyaAGxwXZJxyFzxRmWAamTeZBbciRyfdLlKxXhmyqiJXLcXy-T7UHr0Bwe6u9bpkDmaj0KrFrJmDUwGwGOGWLS_36o20Wc2CXutg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
تصاویری از هواداران ایرانی به یاد «شهدای مدرسه میناب» در استادیوم سوفای لس آنجلس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/133647" target="_blank">📅 09:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133646">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2RdwqU3GpEdGsnI6E7xBIJO8mNfJwFyYZ1lxvK3kJVijCApxIkgsC1OivJB2_lr693WCv0TlgDhMsU-58C6qMY80lS6J_9VlBvcwfuZ8oE2o4gqoP_fRGSePNKGVm8c9ZNHXApjwgiqFUgGkAM7gE1Iu9xGj7-x1dOX3ntf9MvaEQI3xEoEoOhhwcd76wBF5LfGUGvTL0X3SznrjfYPWtDrW6c36mH4SmZRPAsybRSIxEcn3m8Cnn1ApBY5cQ25bRy_J82bAkDCQjjvimgx0Rxgw7icwBWmAfL_WztsDV5IhQoCY_LRV3QQ5BVl-7dUOLmBMzksPO0oj7dtgG-wqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بونوس ویژه جام جهانی وینکوبت ادامه دارد!
⚪️
IRAN -
⚪️
NEW ZELAND
⚫️
جام‌جهانی گروه G
⏰
سه‌شنبه ساعت ۰۴:۳۰
🏟
استادیوم سوفای
🎁
۱۵٪ بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا هفته آینده ۱ تیر ماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/SorkhTimes/133646" target="_blank">📅 06:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133645">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
🔴
و تمام بازی مساوی تمام شد و حیف که از این نیوزیلند ضعیف ما سه امتیاز و نگرفتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/133645" target="_blank">📅 06:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133644">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
گل دوم هم زدیم و شد دو بر دو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/133644" target="_blank">📅 06:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133643">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
دو توپ دو گل برای نیوزیلند ....آقای نعمتی سلطان سوتی   پ.ن دو توپ آورده دو گل زده نیوزیلند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/133643" target="_blank">📅 06:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133642">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
بریم برای نیمه دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/133642" target="_blank">📅 05:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133641">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
هر چی دارن باید بزارن ..راحت میشه سه امتیاز این بازی و گرفت ...تیم سختی نیست نیوزیلند ..مهمترین 45 دقیقه ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/133641" target="_blank">📅 05:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133640">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
نیمه دوم قایدی و علیپور و حسین زاده میتونن کمکمون کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/133640" target="_blank">📅 05:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133639">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❗️
راحت و با تمرکز بیشتر میشه سه امتیاز این بازی و قشنگ گرفت ..نیوزیلند تو دفاع خیلی ضعیفه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/133639" target="_blank">📅 05:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133638">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
گل اول ایران به نیوزیلند توسط رامین رضاییان در دقیقه (32)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/133638" target="_blank">📅 05:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133637">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
نیمه اول یک بر یک تمام شد ‌تو بازی که یک گل زدیم ..یک گل آفساید و یک تیرک ..و عالی بودیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/133637" target="_blank">📅 05:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133636">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗️
❗️
گل تساوی و خداروشکر زدیم ...این نیوزیلند و میشه برد ...در دفاع ضعف دارن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/133636" target="_blank">📅 05:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133635">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
همچنان توپ و زمین دست ماست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/133635" target="_blank">📅 05:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133634">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
✅
ما داشتیم خوب بازی میکردیم که نیوزیلند گل اول و زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/133634" target="_blank">📅 05:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133633">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
بازی و خوب شروع کردیم .و سرحال نشون داده تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/133633" target="_blank">📅 04:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133632">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇷
❤️
کم کم بریم برای بازی تیم ملی ایران در جام جهانی 2026....انشالله تیم کشورمون ببره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/133632" target="_blank">📅 04:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133631">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVHUiGAjSSJ8Sq5cxuAUsCht1cnateYc2WGiWbuk6DvGGlgY2YVGVNOmvCzGuVUacaPUHUD2ZxoCTNS2J96WavMjuFhgSaKIKJLG1HcAcA9DmAn-CEJ0j643h8Nh0rWiMacSTV8iJz0EMqglqaXvKkk-MarwomePwMmdR56psZN9z_bCVh8sevkIqrJe1ZqtJ161OdDTyWldO02BY0aFc0iXe8sQawZcAjbYug-EJ8Zi9o5MNACZ68xOzaCok9RKIAiJ22CO5rbfP6cxzpSQmgfiLVGvym8yjvtQ0rqEujF9Z53pzRzP80QpBMNE-a-vvUppyf1vvkzLpAR1Ptr-Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هم اکنون ورزشگاه مملو از تماشاگر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/133631" target="_blank">📅 04:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133630">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🤍
📸
تصاویری از هواداران ایرانی روی سکوهای استادیوم سوفای برای حمایت از تیم ملی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/133630" target="_blank">📅 04:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133629">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UINYGC2WAJgAgzMbcFZS-PLpn-dzG0F9UZRhc-bzhaJPWAwSm_OAf4SM5DUVvPkkmTxKleNhJ-Tph5H-F4wrqFD8T_vT6nyFBLoF-8q48avrlxpSIPTIrmFe1xdiDgtqmgVNJA7qg0QZA2zQoBXYK7HMWC9hzumi3zDI42J3ZIQ77HcbOud35XN2f12Aq3-0NPWM3e4NbhpbzcOVNRLQ9dAX9jbteuz8HBCZL-4I1O8AkFa_LD_AZVr_52x2TGQfK2OdHLRLL4PjYAONkaEtcEN7ju4qZVzaTzTBagniKtvEdvD6xw3VJ_coYaK4ouNZXnj1OhcQ-PNQov9yiHcy_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤍
📸
تصاویری از هواداران ایرانی روی سکوهای استادیوم سوفای برای حمایت از تیم ملی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/133629" target="_blank">📅 04:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133628">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❗️
جو و حواشی امشب ورزشگاه شاید صداوسیما رو مجبور به سانسورهای شدید و یا حتی قطع تصویر بکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/133628" target="_blank">📅 04:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133627">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
تیم های آسیایی تا الان عالی بودن  اگه قلعه نویی نرینه به آمار شون
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/133627" target="_blank">📅 04:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133626">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❗️
🔻
وزیر ورزش:
🔹
در جام جهانی پرچم غیررسمی بیاورند یا شعار بدهند، سرپرست تیم مسئولیت دارد که بازی را متوقف کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/133626" target="_blank">📅 03:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133625">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇷
حرکت اتوبوس تیم ملی به سمت ورزشگاه سوفای
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/133625" target="_blank">📅 03:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133624">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇷
حرکت اتوبوس تیم ملی به سمت ورزشگاه سوفای
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/133624" target="_blank">📅 03:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133623">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgsunDqCDS0cYd0DC-xAt5I1LSdE5ZaB2GFLjeK7_fe6k8eLbHvfShqTq7CyjNZiHJbLJDJhrzAAOji00wT77eSMqEfJuS6Qc1unG02p47wZrW_CdrtCnnkS8iYAgUp48yesylKpgJxURrOw0umzNl0whytN2LMYX1aku5bi-vTeEQbLf4A32k-HJkaeiGgfvUEaG97QIJFurdjzu5VSG3N9aCSzJqBk3A0NqYJ2CX24EtwiRIL9iiZaait3f2l7iYPEpFU8gBt-J7npWpeoCcFKN_jVctcmp5MZmGCf7Tg0Is7T-FF9oHOATvxCnl261BCC8ujvuKLH65MyX-r5LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
گرون‌ترین ورزشگاه جهان در تسخیر ایرانی‌ها
❌
این استادیوم 70 هزار نفریه که فقط 5 هزار بلیط از نیوزیلندی‌ها فروش رفته و 65 هزار ایرانی قراره امروز بازی رو از نزدیک ببینن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/133623" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133622">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8709c9d008.mp4?token=jvaQ3CBY1sTHjvmQOGyXo4-gyVJGxJFYyTrbQOdezhBTk1fc8Iog7japuoU9ZtqIFCjsq3nt6Rh9osI0lol0I4oNKt9cG8CO24v5kjyQxVd6GyYasg0ZqVuDlujWFhsmwQQ-sp0BiooUvEDxuPNFcBYXy0wzEoje7nyrDREA1d1tk_01XNBy9H9D_MP3ULRnLGJJt7xjPSAwG2QmBhRt9tMpudw6EeE9akFP5519zij1UguaIQb6ONA7oiuuddcHP6rE6jYE3TgwyiUPLErPqAbAko2qVIt0xngMqGURzOAcoJsmLjjF7xwnasqTez5dxDgVw_H3Nz8jWwOqvg8uUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8709c9d008.mp4?token=jvaQ3CBY1sTHjvmQOGyXo4-gyVJGxJFYyTrbQOdezhBTk1fc8Iog7japuoU9ZtqIFCjsq3nt6Rh9osI0lol0I4oNKt9cG8CO24v5kjyQxVd6GyYasg0ZqVuDlujWFhsmwQQ-sp0BiooUvEDxuPNFcBYXy0wzEoje7nyrDREA1d1tk_01XNBy9H9D_MP3ULRnLGJJt7xjPSAwG2QmBhRt9tMpudw6EeE9akFP5519zij1UguaIQb6ONA7oiuuddcHP6rE6jYE3TgwyiUPLErPqAbAko2qVIt0xngMqGURzOAcoJsmLjjF7xwnasqTez5dxDgVw_H3Nz8jWwOqvg8uUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرکت اتوبوس تیم ملی به سمت ورزشگاه سوفای
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/133622" target="_blank">📅 02:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133621">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❗️
جو بیرون ورزشگاه سوفی آمریکا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/133621" target="_blank">📅 02:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133620">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186dc9ec7b.mp4?token=eWTlXi1GoZY0T-jMWuqs3HX9mMpLBZDDtDEMv5IxYnOEL0WA-86f9t0bqclczDPagFkzL2s0mQtEtHdcJyCAUEZjoinBNjE4d_CKaX6H70vfteVE-KnTTfiEz-KabukLpks7W0QEmFer93H8EsvzfPL1gf28y5_QVro6Exofs5wGUQrjpJObetlA9CSCCwvk23-g_C1ReYkCkUKtUGIR8rWyMld8BKXBr9fPYkvguXzjm9tk1zK9vAeJd92FDqOx7KksHuep871hsZFrk1uY2apEEJvv9ISjj2t8UrbOTKBMT2psFIUOST7YLCrIqffnRj5uEjqkTpbicrZ3BTfmVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186dc9ec7b.mp4?token=eWTlXi1GoZY0T-jMWuqs3HX9mMpLBZDDtDEMv5IxYnOEL0WA-86f9t0bqclczDPagFkzL2s0mQtEtHdcJyCAUEZjoinBNjE4d_CKaX6H70vfteVE-KnTTfiEz-KabukLpks7W0QEmFer93H8EsvzfPL1gf28y5_QVro6Exofs5wGUQrjpJObetlA9CSCCwvk23-g_C1ReYkCkUKtUGIR8rWyMld8BKXBr9fPYkvguXzjm9tk1zK9vAeJd92FDqOx7KksHuep871hsZFrk1uY2apEEJvv9ISjj2t8UrbOTKBMT2psFIUOST7YLCrIqffnRj5uEjqkTpbicrZ3BTfmVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
جو بیرون ورزشگاه سوفی آمریکا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/133620" target="_blank">📅 02:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133619">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
جو و حواشی امشب ورزشگاه شاید صداوسیما رو مجبور به سانسورهای شدید و یا حتی قطع تصویر بکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SorkhTimes/133619" target="_blank">📅 02:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133618">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
ورزشگاه لس آنجلس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SorkhTimes/133618" target="_blank">📅 02:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133617">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
⏱
پایان نیمه اول
🇸🇦
عربستان ۱ - ۰ اروگوئه
🇺🇾
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/133617" target="_blank">📅 02:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133616">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
هلند و ژاپن مساوی کردن
✅
تا اینجای کار تیمای آسیایی خوب بوده عملکردشون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/SorkhTimes/133616" target="_blank">📅 02:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133615">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8Q6XH1Gyc_gJ7QCuxh6yzpuzU_SNCMXCL2aBMbSKfzWvHJFwhynhe3iyIW4FJ21OEwRWYr8b_vWWocuHuI-Y9RusDGFJJ_mKpZF8CRURojLtKuSWfT2GzOajrkdyz22d_BZoKgaYSd85l_LgTMQp8volMUcxlT6fp51O2ZxpBAE74INPdnerY6MS99N1N4TrTKOLXUa4p9F70uOzEXE4USH6l5670_Ri0joI9FxqTTPlgy-MBggbIiRrjOtmFg2834TCkaw6XV9yfzXRcFQEzej0A6WICEGDWfCtqHlV6kaRk4fKw-q1MrZf98Knnmy9GgyqLi_mwx3wMjaA7FQZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بونوس ویژه جام جهانی وینکوبت ادامه دارد!
⚪️
IRAN -
⚪️
NEW ZELAND
⚫️
جام‌جهانی گروه G
⏰
سه‌شنبه ساعت ۰۴:۳۰
🏟
استادیوم سوفای
🎁
۱۵٪ بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا هفته آینده ۱ تیر ماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/133615" target="_blank">📅 02:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133614">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
محمد سیانکی گزارشگر صدا و سیما جمهوری اسلامی راهی آمریکا شده و قرار است هر سه بازی تیم ملی را در جام جهانی گزارش کند
🫥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/133614" target="_blank">📅 02:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133613">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH9-WkzGm_39TgAEJbTtp8ZCAfMw4erGE7VaFrv8ruY6l2c7OzvRdxdm96pEajP2WXOVJvU_Tp91y_OWLj_LP5KnC57Qb8u-CZm9mROWAeGiIDSwSFmr25fTWYt6Df2erOpXUCSLxmLKPdwUlkWHWonxbQpqndUBpE8rPZr6n0IaCGZk2whRMsHjD97YMBdSd6YE81vL8x3v_BYUj-Ctied1IhtlPbotM8xJ0TMmvDceqE-J5Kj6Saj1j5HQIX9qbsq15ujWoG963eqzAl8bw5QIFXz27ak6yOda6BZ5YEMLi6kgZ9MByY9ModYdMo_S1LjjBjJxeaCd29_RZ7l3Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ورزشگاه لس آنجلس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/133613" target="_blank">📅 02:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133612">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
جام جهانی| کیپ‌ورد نخستین شگفتی جام جهانی ٢٠٢۶ را رقم زد؛ ماتادورها پشت سد کیپ‌ورد؛ لقمه‌ای که از گلوی اسپانیا پایین نرفت
❗️
اسپانیا صفر - کیپ‌ورد صفر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/133612" target="_blank">📅 01:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133611">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❗️
فوری و رسمی/هم اکنون محاصره دریایی آمریکا علیه ایران کاملا برداشته شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/133611" target="_blank">📅 00:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133610">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
جام جهانی 2026؛ تساوی رقبای ایران در گام نخست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/133610" target="_blank">📅 00:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133609">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKZEcd3LVACf24OVPY75DxkIBC5MUoKfO4FGxtUfczWkZ5_7_VNS9zYeKwWXTWEDEpmMvlqYeQtSpGb714Xfsnxg5d-QzMROs624_tMXSpV1UgI0Y5JbBDc0kNAqhvepvOaFMh7mqX-RONC-WeeGySKPgi-ekMlqT0zQw1Rz6yjyrs08Vr9DjU5Vld3S8wEZu5dbnmtAxbOZsOpyaeeQpoFVfqTn0yBuI6JWcXoU6ldmw0T-YpfJMyO8w4CID3fp0Q3cXhFXtxkGkQzxZlMkKDeFJNWUNysJ5y2FlyD9EYuDkSkJrnqz7VHrg6gqZpn4Pf_dXmL5Ii1VdodsGEhUuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جام جهانی 2026؛ تساوی رقبای ایران در گام نخست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/133609" target="_blank">📅 00:33 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
