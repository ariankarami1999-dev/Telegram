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
<img src="https://cdn4.telesco.pe/file/BUz83Gbf2giGZ2WgEGO9fvykYjJRThPoQAnnPQH3T7jziiE1G-ougLx4QW6KImlIdGI5v9Qr-hqwayYhvqQKxi04k0W1c7MQuo3G5RajXupGP7GAFk2ovQM9f8K860SflBWKtFpRihyvlJR10vlP_CrPcewZUWJ4ms5U8rswO8W2REgehQ2BMButVKlfPjFotgXmTnHv5gjU9-9yTeWuCqGrTfNp5A6DpP9MhRYfyk2QNzMNGEhBe4OYEtN5DTXWKtnTgcjqKatBucOLBkP1mrXi2Yhcf3bbHwSRPvVPzI2WVD9r6bKs1nkbhTNQlVBaX7W9_zeodfQdSHiSR1aCew.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 447K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 17:07:57</div>
<hr>

<div class="tg-post" id="msg-22283">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پنتاگون اعلام کرده است که در جریان حملات موشکی و پهپادی اخیر ایران به مواضع نیروهای آمریکایی در اردن،
۱۲ نظامی آمریکایی زخمی شده‌اند
.
@WarRoom</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/withyashar/22283" target="_blank">📅 16:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22282">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جی‌دی‌ ونس : «همه چیزهایی که ممکن است اتفاق بیفتد روی میز است؛ فشار اقتصادی، فشار نظامی، فشار دیپلماتیک و فشار مخفیانه (
به شکل مخفیانه عملیات‌های خرابکارانه در ایران انجام شود
).»
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/22282" target="_blank">📅 14:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22281">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b10940b05.mp4?token=Z9Arbf08iFUBMtLi4dv6SphWofRxPrjY8CC51MXcFaHYpPFDqOtIFce6Yb3vas_aCGSmf7LLHtjBjnPlHn6HkZc9PEHfk78dZ02pTzr8FMa1THujN8k2xA-bKalXK0Z5oc1tqO2Gz9Uj4D3oIWwCbrJbBO3jQINA5pFcwH6QXyRx6iUtgdT1bK2DQUp7kY9H4WmX49JSmFjF2XdDD_dLoJOnIqclG3a5metQc62mOjkaws4BO3O8DCCpZA2UBzUweibdhRtCzedAwlBGz1ilX7TXBNv7aEImpIXvuMoZkGwDxHBUKa2ihNsrbFXTQBrKoVC3_BsO7DED1MlysY9e-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b10940b05.mp4?token=Z9Arbf08iFUBMtLi4dv6SphWofRxPrjY8CC51MXcFaHYpPFDqOtIFce6Yb3vas_aCGSmf7LLHtjBjnPlHn6HkZc9PEHfk78dZ02pTzr8FMa1THujN8k2xA-bKalXK0Z5oc1tqO2Gz9Uj4D3oIWwCbrJbBO3jQINA5pFcwH6QXyRx6iUtgdT1bK2DQUp7kY9H4WmX49JSmFjF2XdDD_dLoJOnIqclG3a5metQc62mOjkaws4BO3O8DCCpZA2UBzUweibdhRtCzedAwlBGz1ilX7TXBNv7aEImpIXvuMoZkGwDxHBUKa2ihNsrbFXTQBrKoVC3_BsO7DED1MlysY9e-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من از ۶ سال پیش استوری کردم، به دوستای نزدیک و بچه‌های پیجم گفتم! از اتاق جنگم ۴-۵ بار گفتم، بازم میگم ما تا آخر ۲۰۲۸ تو جنگیم و درگیریم! حالا بقیشو من روحیه میدم تا بکشین تا تهش
🙌🏾
پس دیگه تکرار نمی‌کنم، هر کاری می‌کنید توشه راه رو داشته باشید. حتی فردا صبح…</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/22281" target="_blank">📅 14:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22280">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24b2ff651.mp4?token=fFqOWNtaAcBqxG0kwivxWI94p42bDxcMmpTXpZFvr4eg9FPG-bkl5wGofEEsLmPjoogjWt4nypviPcuPdb4HH_wAqyw_AFftUSCyVxhc8CHv38tE4-BReg0g8wWdEMoohGQCsl854lnomz0hfxKGfVAQW3pN93LBg-n-7ojcpNxJi_kdqzENJM-pApofKrlg9Ovl0UkmVOI5i8n6WAQfJHHfF5vtcjIVbhitLYsax_KiormNl-zGOK7aGay8Z3FIRCQyDxMtQnJDOwruRa3WF5KElzhgJeTbHxlOcFYwLlth33JJeYDi0h1Ux67U3n825pGQPwll5Im0uBeJHT-I2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24b2ff651.mp4?token=fFqOWNtaAcBqxG0kwivxWI94p42bDxcMmpTXpZFvr4eg9FPG-bkl5wGofEEsLmPjoogjWt4nypviPcuPdb4HH_wAqyw_AFftUSCyVxhc8CHv38tE4-BReg0g8wWdEMoohGQCsl854lnomz0hfxKGfVAQW3pN93LBg-n-7ojcpNxJi_kdqzENJM-pApofKrlg9Ovl0UkmVOI5i8n6WAQfJHHfF5vtcjIVbhitLYsax_KiormNl-zGOK7aGay8Z3FIRCQyDxMtQnJDOwruRa3WF5KElzhgJeTbHxlOcFYwLlth33JJeYDi0h1Ux67U3n825pGQPwll5Im0uBeJHT-I2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله بوشهر ، کشتی هدف قرار گرفته شده توسط آمریکا
@WarRoom</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/22280" target="_blank">📅 14:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22279">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رویترز: برخی تأمین‌کنندگان چینی مواد معدنی کمیاب، از فروش و ارسال این مواد به شرکت‌های آمریکایی خودداری می‌کنند. این شرکت‌ها نگران‌اند که به‌دلیل همکاری با برنامه‌های آمریکایی برای بررسی و شفاف‌سازی زنجیره تأمین، با مجازات دولت چین روبه‌رو شوند. چین اوایل…</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/22279" target="_blank">📅 14:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22278">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رویترز: برخی تأمین‌کنندگان چینی مواد معدنی کمیاب، از فروش و ارسال این مواد به شرکت‌های آمریکایی خودداری می‌کنند.
این شرکت‌ها نگران‌اند که به‌دلیل همکاری با برنامه‌های آمریکایی برای بررسی و شفاف‌سازی زنجیره تأمین، با مجازات دولت چین روبه‌رو شوند. چین اوایل اوت ائتلاف کسب‌وکارهای مسئول آمریکا را تحریم کرده بود. مواد معدنی کمیاب در صنایع مختلف، از جمله
تولید تراشه، هوافضا و تجهیزات دفاعی و نظامی
کاربرد دارند
@WarRoom</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/22278" target="_blank">📅 14:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22277">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">صحبتهای زیبای یک کاربر : ‏آقای ایرج مصداقی، نمی‌خواهید این حاشیه‌ها را تمام کنید؟ صبح تا شب مقابل دوربین نشسته‌اید و به این و آن حمله می‌کنید؛ نتیجه‌اش هم چیزی جز خوراک دادن به پهلوی‌ستیزها و فراهم کردن بهانه برای حمله به رضاشاه دوم نیست. ‏شما عضو جریان عدالت…</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/22277" target="_blank">📅 14:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22276">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ایرج مصداقی متولد۱۳۳۹ ، نویسنده و زندانی سیاسی دهه ۶۰ و از بازماندگان اعدام‌های سال ۱۳۶۷ است که حدود ۱۰ سال در زندان‌های اوین، قزل‌حصار و گوهردشت زندانی بود و بعدها خاطراتش را در مجموعه چهارجلدی «نه زیستن، نه مرگ» منتشر کرد.  مصداقی در سال‌های ابتدایی دهه…</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/22276" target="_blank">📅 13:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22275">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">من کدومم ؟
😁</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/22275" target="_blank">📅 13:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22274">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNokte_sanj</strong></div>
<div class="tg-text">من فیلمبردارو زنده میخوام</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/22274" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22273">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">جی دی ونس: ما تا زمانی که ایران از شلیک به کشتی‌ها دست نکشد، با آن مذاکره نخواهیم کرد @WarRoom</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/22273" target="_blank">📅 12:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22272">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الجزیره: ایران لیست سیاه ( متخلفین ) خود را برای کشتی‌ها به بیش از ۵۰ مورد کشتی به‌روزرسانی کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/22272" target="_blank">📅 12:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22271">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فایننشال‌تایمز تایمز از تلاش میانجیگران عمانی و قطری برای تدوین چارچوبی جدید برای مذاکرات میان ایران و امریکا با هدف مدیریت بحران میان دو کشور خبر داد
@WarRoom</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/22271" target="_blank">📅 12:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22270">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">من کدومم ؟
😁</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/22270" target="_blank">📅 12:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22269">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c519fba49.mp4?token=PckLkKe662_3h0G6LNMuqk7u_L-xkETsXd-y5M-8YMLHNs5OYGDXs9yg5jp1TiBSwgm21uVK6CzcSk2PSmqsEj60j5FwKOa-vRYuIG0K-o89qcO1EYJhCrAew1uS8aTlAdFb14SsTo_Jn30UMlGy3DfHzhD3AHCK-wcCksGMsGnY3vUEm8sXxFpra1_wXwPOzFnqeABgqZBK3HT6xP37cWSUNn6d4ufTCcu5TLGDbuqVwIemYxJWyL3GBVnCo19M1HjoS-o16g9IgNJPKfqkcWf6oQb6L8dUajC9kXBrIzTyNz-n-3pkKphC1cceys7GAiOksXJ4ylzFUMSmGcBvTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c519fba49.mp4?token=PckLkKe662_3h0G6LNMuqk7u_L-xkETsXd-y5M-8YMLHNs5OYGDXs9yg5jp1TiBSwgm21uVK6CzcSk2PSmqsEj60j5FwKOa-vRYuIG0K-o89qcO1EYJhCrAew1uS8aTlAdFb14SsTo_Jn30UMlGy3DfHzhD3AHCK-wcCksGMsGnY3vUEm8sXxFpra1_wXwPOzFnqeABgqZBK3HT6xP37cWSUNn6d4ufTCcu5TLGDbuqVwIemYxJWyL3GBVnCo19M1HjoS-o16g9IgNJPKfqkcWf6oQb6L8dUajC9kXBrIzTyNz-n-3pkKphC1cceys7GAiOksXJ4ylzFUMSmGcBvTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کامتم زیر پست جدید و جنجالی نتانیاهو
https://www.instagram.com/reel/Dc25xWUsghi/?comment_id=18135318097727381</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/22269" target="_blank">📅 11:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22268">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohammadreza</strong></div>
<div class="tg-text">سلام یاشار جان
امروز بانک ملت شعبه مرکزی شیراز رو داشتن دور تا دورش آهن جوش میدادن ساختمونه شیشه‌ایه داشتن آهن دورش جوش میدادن خودشونم میدونن قراره چی بشه</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/22268" target="_blank">📅 11:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22267">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">فرمانده قرارگاه خاتم‌الانبیا:
به‌زودی دشمن رو در میدان غافلگیر میکنیم
رفتارهایی با دشمن خواهیم داشت که کاملا گیج، مبهوت و شگفت‌زده خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22267" target="_blank">📅 10:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22266">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ccab60afb.mp4?token=SclDBp1mYUvSGbQvfAlUe9z4Q089Kdy_FQ7Ws029jqe_ueFsKXbnO7YT37oqjpR-mLQQFmQfYU__Ko_Mftu6CA1gI5ndztyLHjDL1BLDEp2hcgFHr62a5xCxqvWG9iMdkwB8PVOV1r0-r9u7ePYEvl0LG2RKMl4KVURTSkuRcsDmixhe8mXlnxaopHrE4SxSbR1_g_jQbkvKeDWuwpIrJvGUphyZgwAcTX_WB0UdSAJz36Y-xQRDeiDbb2CvexoiFCHj3wVXWORJXjOUNv0yKFCwQxaG-_iO0m191JgXPmQ5p4qgaOKq9VE_Jo0kR4TrZ46ruJTGGIFp5-vj-072NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ccab60afb.mp4?token=SclDBp1mYUvSGbQvfAlUe9z4Q089Kdy_FQ7Ws029jqe_ueFsKXbnO7YT37oqjpR-mLQQFmQfYU__Ko_Mftu6CA1gI5ndztyLHjDL1BLDEp2hcgFHr62a5xCxqvWG9iMdkwB8PVOV1r0-r9u7ePYEvl0LG2RKMl4KVURTSkuRcsDmixhe8mXlnxaopHrE4SxSbR1_g_jQbkvKeDWuwpIrJvGUphyZgwAcTX_WB0UdSAJz36Y-xQRDeiDbb2CvexoiFCHj3wVXWORJXjOUNv0yKFCwQxaG-_iO0m191JgXPmQ5p4qgaOKq9VE_Jo0kR4TrZ46ruJTGGIFp5-vj-072NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از ۵۰ هزار نفر شامگاه پنجشنبه در مراسم مذهبی «سلخوت» در محوطه دیوار غربی (دیوار ندبه؛ بخشی از دیوار حائل محوطه کوه معبد در اورشلیم) گردهم آمدند و به دعا پرداختند. بنیاد میراث دیوار غربی اعلام کرد که از آغاز ماه «اِلول»، بیش از ۵۰۰ هزار نفر در مراسم سلخوت در این محل شرکت کرده‌اند. این مراسم که از ۱۴ اوت آغاز شده، تا شب یوم‌کیپور در ۲۰ سپتامبر ادامه دارد. پس از آن، روش‌هشانا (سال نوی یهودی) از شامگاه ۱۱ تا ۱۳ سپتامبر و یوم‌کیپور از شامگاه ۲۰ و ۲۱ سپتامبر برگزار می‌شود
«این مراسم در آستانه اعیاد بزرگ یهودی برگزار شد؛ دوره‌ای که از شامگاه ۱۱ سپتامبر با روش‌هشانا آغاز می‌شود و تا ۴ اکتبر ادامه دارد و مقام‌های اسرائیلی نسبت به احتمال حمله ایران در این دوره هشدار داده‌اند.»
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22266" target="_blank">📅 10:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22265">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818a226b89.mp4?token=E-1uNsQmAlQ1Nfs5ZhqAMuVIrXJetPPy3PB-N5t36LOxIUuuexVEASq3yNlaFktSnjiKx-f3C4deQFwfDKZDFWwtaL9_AA7RLLkBQOVVk9GWjN7Bw_4yNh3AxeP2EfOUkCKUyIKiUg9jyq57VgbmAuJynydxIbSEBiJKkVRTTQ4Ip92R2bmvbmSEKnNglRe5ng-40rl5SC5hI1yCKGmXkMcmPn6rFR3jUYE3nSZojfvL_3-zk5PGudPQD5g--drDAEGgg7V9EFyUe8uEjn4u0YxmWWfJiXU_k85CEMmuhwt2UQ-QY_wmCUybCh2xnCXOqxEJ4ETXu6SYr8FlZNyYYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818a226b89.mp4?token=E-1uNsQmAlQ1Nfs5ZhqAMuVIrXJetPPy3PB-N5t36LOxIUuuexVEASq3yNlaFktSnjiKx-f3C4deQFwfDKZDFWwtaL9_AA7RLLkBQOVVk9GWjN7Bw_4yNh3AxeP2EfOUkCKUyIKiUg9jyq57VgbmAuJynydxIbSEBiJKkVRTTQ4Ip92R2bmvbmSEKnNglRe5ng-40rl5SC5hI1yCKGmXkMcmPn6rFR3jUYE3nSZojfvL_3-zk5PGudPQD5g--drDAEGgg7V9EFyUe8uEjn4u0YxmWWfJiXU_k85CEMmuhwt2UQ-QY_wmCUybCh2xnCXOqxEJ4ETXu6SYr8FlZNyYYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در باره ایران
: «به محض اینکه به پیروزی برسیم»
اما بلافاصله متوجه شد و گفت زیاد طول نمیکشد و بعد سخنش را عوض کرد و گفت
: «همین الان پیروز شده‌ایم
چون آنها نمیتوانن‌ سلاح هسته ای داشته باشند
»
و اگه
ما امروز از جنگ علیه ایران خارج بشیم هم بازسازی این کشور ۲۵ سال طول میکشد
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22265" target="_blank">📅 10:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22264">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22264" target="_blank">📅 09:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22263">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اتاق جنگ با یاشار : کره جنوبی جفت کرد !
رویترز: کره جنوبی در حال آماده‌سازی برای اعزام نیروهای نظامی به تنگه هرمز است
؛
رسانه‌های محلی کره جنوبی با استناد به منابع نظامی و دولتی گزارش داده‌اند که این نیروها برای حمایت از
آزادی کشتیرانی (امکان عبور ایمن و آزاد کشتی‌ها)
در تنگه هرمز مستقر خواهند شد و سئول قصد دارد آنها را
پیش از پایان سال
اعزام کند. این تصمیم در حالی مطرح شده که دونالد ترامپ،
رئیس‌جمهور آمریکا، در ماه اوت اعلام کرده بود در حال کاهش همکاری نظامی با کره جنوبی است
؛ بخشی از دلیل این تصمیم، به گفته او، خودداری سئول از کمک به واشنگتن در جنگ علیه ایران بوده است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22263" target="_blank">📅 04:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22262">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اعلیحضرت همایون شاهنشاه آریامهر محمدرضا پهلوی
: هیچوقت به زندگی فعلی خود قانع نباشید و همیشه دنبال بهتر کردن زندگی خود باشید.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22262" target="_blank">📅 03:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22261">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا: اتحادیه اروپا رسماً به کارزار انزوای اقتصادی علیه ایران پیوست و ما از موضع قاطع و به‌موقع آن قدردانی می‌کنیم. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22261" target="_blank">📅 03:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22260">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رویترز :
یک بات‌نت (شبکه‌ای از رایانه‌های آلوده) به نام
«سلیتی»
که از سال ۲۰۰۳ فعال بود و طی هشت سال گذشته برای سرقت ارز دیجیتال نیز استفاده می‌شد، در عملیات مشترک آمریکا و اروپا از کار انداخته شد. این شبکه بیش از
۱۵ هزار رایانه آلوده
داشت و برای سرقت رمزارز، ارسال هرزنامه و حملات سایبری استفاده می‌شد. هم‌زمان، کمیسیون معاملات آتی کالای آمریکا از دادگاه خواست شکایت
سی‌ام‌ای گروپ
درباره معاملات پرپچوال رمزارزی (قراردادهای بدون تاریخ انقضا) را رد کند. همچنین وزارت دادگستری آمریکا اعلام کرد
بیش از ۵۶۰ هزار دلار رمزارز متعلق به حماس (گروه اسلام‌گرای فلسطینی)
را که برای تأمین مالی این گروه در نظر گرفته شده بود، توقیف کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22260" target="_blank">📅 03:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22259">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">چندین پرتاب موشک/پهپاد به سمت تنگه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22259" target="_blank">📅 03:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22258">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا: اتحادیه اروپا رسماً به کارزار انزوای اقتصادی علیه ایران پیوست و ما از موضع قاطع و به‌موقع آن قدردانی می‌کنیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22258" target="_blank">📅 03:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22257">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کانال ۱۴ اسرائیل: ارتش این کشور شبکه زیرزمینی راهبردی حزب‌الله در منطقه تپه علی‌الطاهر را به‌طور کامل پاکسازی کرده ,
نیروهای لشکر ۳۶ کنترل عملیاتی منطقه را در سطح زمین و زیر زمین به دست گرفته‌اند؛ در این شبکه‌ها اتاق‌های فرماندهی، انبارهای سلاح و امکانات اقامت طولانی‌مدت کشف شده و برخی نیروهای
نیروهای
حزب‌الله و سپاه
حاضر در این محل
کشته یا متواری
شده‌اند.
این زیرساخت زیرزمینی که به گفته اسرائیل طی حدود دو دهه با تأمین مالی و برنامه‌ریزی ایران ساخته شده، همچنان در حال منهدم شدن است
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22257" target="_blank">📅 02:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22256">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دیدبان اتاق جنگ سیریک :  امشب تنگه خیلی صدا میاد از ساعت ۱۱ تا الان بالایی ۱۵ صدا اومده ، کمی پیش پرتاب موشک انجام دادن ولی الان از تنگه یه صدای مهیب اومد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22256" target="_blank">📅 02:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22255">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25f2f2934c.mp4?token=kh2zQmkIKIYvgUj_cOJK5S9D6fgnEKhE9h1R1aZZV5s4IFWDf30zHcdXCZvJyqUo3FFSkmMKy5R636JIfGoIE3tFaqtS3FKDlQ6ucHvNppYZfqNnSvPp60oLhteR0-z9978VVoR1hYS-eEG__PitkeJdelkJqxrjEbQJOxW3jImVL5RY_lsSYR16S6RFEmh4hSwjwcLedu1QnAEzT5Mgks64DdxASvnGslx3oNQf1xhR5O74nZjnATIbnFLj-p-AtZH4ezcEiQvSHx6vgGsUs4bMxgRahgoO_FKPGGFvcveZLvDEXcVvXq7Xl62wyWCW167WvL5OtdRZhSh7Mr6tDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25f2f2934c.mp4?token=kh2zQmkIKIYvgUj_cOJK5S9D6fgnEKhE9h1R1aZZV5s4IFWDf30zHcdXCZvJyqUo3FFSkmMKy5R636JIfGoIE3tFaqtS3FKDlQ6ucHvNppYZfqNnSvPp60oLhteR0-z9978VVoR1hYS-eEG__PitkeJdelkJqxrjEbQJOxW3jImVL5RY_lsSYR16S6RFEmh4hSwjwcLedu1QnAEzT5Mgks64DdxASvnGslx3oNQf1xhR5O74nZjnATIbnFLj-p-AtZH4ezcEiQvSHx6vgGsUs4bMxgRahgoO_FKPGGFvcveZLvDEXcVvXq7Xl62wyWCW167WvL5OtdRZhSh7Mr6tDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد شناسایی غرب تهران چیتگر
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22255" target="_blank">📅 02:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22254">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb363544dd.mp4?token=P8GwI6XERhkdJmqG-0jukvxXKE6OrFKmvEpWtMoJBSCVq520rVvZLv9YdYxlu8SionWdpx0YwH8K-mJs-NgWYbupUXeVoEsbe3bWiPdwWXAZ0j1-FSVqjLx_VC-zOJlMOsUElAA-jnRtEKswsAM42jUQ1sWUw5zmV_NidMVXoy2Nj8_Bo59kcr8koNKv6KZ3mKXZ4Ti1igOkNj8iVVo_zUZ9eVJiO-y7sIyxGpZzVtSWO3XWf-_8fqnZXbnu3zIFZqwCcjICkCfI4vyrmCiynYMiSISHOVFrRw6uSx39wCDPvxOj_TMCCRZx7edRS3SuZmAX1mpLr8nylPKr7AQEriRoSc0NC_OZXzNYGVXCnVVIE9YPP7DUzbDzW0vnNo0ITHB6xdTFLq7C0bszVw_hyIJdE_zhR1ASEDqWi6OfLvTtghdTvLNmgpB91NPywNKnHSLfTWD-4Z240UADRdIPaXkmo0QGkiatGwXEqW8lz3asPdx8Ke4WYa6Fu8vtraTB-z9sOuiLmFKW9W7Jp7I-UcGjRTYD_IOLJaaeONUgJs8UjbESD4DDH4avCSmIPrItsZ-7Nx7MYsh5YXhiuoQTbrCFATr_mZTsTX4nw6TGsitigJ2BP-ScDStey39bMMZa7vTff7MZMMtLIvPN9YMUibBrBGEFMVsF3QSLRULtRmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb363544dd.mp4?token=P8GwI6XERhkdJmqG-0jukvxXKE6OrFKmvEpWtMoJBSCVq520rVvZLv9YdYxlu8SionWdpx0YwH8K-mJs-NgWYbupUXeVoEsbe3bWiPdwWXAZ0j1-FSVqjLx_VC-zOJlMOsUElAA-jnRtEKswsAM42jUQ1sWUw5zmV_NidMVXoy2Nj8_Bo59kcr8koNKv6KZ3mKXZ4Ti1igOkNj8iVVo_zUZ9eVJiO-y7sIyxGpZzVtSWO3XWf-_8fqnZXbnu3zIFZqwCcjICkCfI4vyrmCiynYMiSISHOVFrRw6uSx39wCDPvxOj_TMCCRZx7edRS3SuZmAX1mpLr8nylPKr7AQEriRoSc0NC_OZXzNYGVXCnVVIE9YPP7DUzbDzW0vnNo0ITHB6xdTFLq7C0bszVw_hyIJdE_zhR1ASEDqWi6OfLvTtghdTvLNmgpB91NPywNKnHSLfTWD-4Z240UADRdIPaXkmo0QGkiatGwXEqW8lz3asPdx8Ke4WYa6Fu8vtraTB-z9sOuiLmFKW9W7Jp7I-UcGjRTYD_IOLJaaeONUgJs8UjbESD4DDH4avCSmIPrItsZ-7Nx7MYsh5YXhiuoQTbrCFATr_mZTsTX4nw6TGsitigJ2BP-ScDStey39bMMZa7vTff7MZMMtLIvPN9YMUibBrBGEFMVsF3QSLRULtRmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد شناسایی در آسمان شهریار
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22254" target="_blank">📅 02:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22253">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22253" target="_blank">📅 01:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22252">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اتاق جنگ با یاشار: قوه قضائیه جمهوری اسلامی حکم اعدام شاهزاده رضا پهلوی را صادر کرد!
جمهوری اسلامی در تازه‌ترین اقدام خود علیه
شاهزاده رضا پهلوی
، پرونده‌ای با اتهام‌هایی از جمله «افساد فی‌الارض»، جاسوسی و همکاری با دولت‌های متخاصم تشکیل داده ؛ اقدامی که یادآور سابقه جمهوری اسلامی در تهدید و صدور احکام علیه مخالفان خارج از کشور است.
سلمان رشدی
؛ در سال ۱۳۶۷، روح‌الله خمینی فتوای قتل نویسنده بریتانیایی را صادر کرد و برای سال‌ها جمهوری اسلامی در تعقیب او بود، اما رشدی زنده ماند و به فعالیت خود ادامه داد.
دونالد ترامپ و بنیامین نتانیاهو
نیز بارها هدف تهدید به قتل و مجازات قرار گرفته‌اند و در
تجمعات حکومتی جمهوری اسلامی، عروسک‌های آنها را به چوبه‌های دار آویزان کرده‌اند
؛ هم‌زمان مقام‌های حکومتی نیز بارها از مجازات و اعدام آنها سخن گفته‌اند. حالا شاهزاده
رضا پهلوی
نیز به این فهرست اضافه شده است و نشان از مسیر درست ایشان و ترس حکومت از وی دارد ؛ فهرستی که از
ترامپ، نتانیاهو
تا
سلمان رشدی و اکنون با شاهزاده رضا پهلوی
امتداد پیدا می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22252" target="_blank">📅 01:53 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22251">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دستور پنتاگون برای تغییر نام جنگ علیه ایران
شبکه خبری CBS به ایمیلی از نیروی هوایی آمریکا در ۷ اوت دست یافته که نشان می‌دهد پنتاگون دستور داده نیروهای آمریکایی دیگر برای اشاره به عملیات جاری علیه ایران از عنوان «عملیات خشم حماسی» استفاده نکنند و به‌جای آن عبارت «عملیات برون‌مرزی در حوزه مسئولیت فرماندهی مرکزی آمریکا» را به کار ببرند. پنتاگون اعلام کرده «عملیات خشم حماسی» رسماً در ۵ مه پایان یافته بود؛ همان روزی که مارکو روبیو نیز پایان آن را اعلام کرد. با این حال، عملیات نظامی آمریکا علیه ایران پس از آن ادامه داشته و دیگر تحت این عنوان ثبت نمی‌شود. در ژوئیه نیز ارتش آمریکا ابتدا چهار نظامی کشته‌شده در عملیات‌های مرتبط با ایران را زیر عنوان «خشم حماسی» ثبت کرد، اما بعداً آنها را در دسته «عملیات برون‌مرزی» قرار داد
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22251" target="_blank">📅 01:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22250">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خبرگزاری صداوسیما: ادعای نتانیاهو مبنی بر تصرف تپه‌های علی‌الطاهر هنوز به تایید مقامات لبنانی نرسیده است
@WarRoom
خوب کسی اون منطقه زنده نمونده که بگه
😆</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22250" target="_blank">📅 01:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22249">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝓜𝓪𝓱𝓭𝓲</strong></div>
<div class="tg-text">دوباره فعال شد پدافند غرب</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22249" target="_blank">📅 01:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22248">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromnasrin</strong></div>
<div class="tg-text">ما اكباتانيم همينجور صداي پدافند و شليك مياد</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22248" target="_blank">📅 01:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22247">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEhsan</strong></div>
<div class="tg-text">سلام داداش سمت شهر قدس ساعت های ۱۲ و  خورده ای شروع شد به شلیک پدافند چند دقیقه قطع میشد باز فعال میشد تا چند دقیقه پیش هم بود ، ۴ دقیقه پیش هم یه صدایی مثل پهباد شاهد بود اما نمیدونم واقعا پهباد بود یا هواپیما با ارتفاع پایین داشت پرواز میکرد چون فرودگاه مهرآباد هم هست اینجا اما خیلی صداش شبیه پهباد بود و بعد ۵ ثانیه قطع شد انگار که قطع بشه شاید سقوط کرد اگر هواپیما بود انقدر سریع صداش قطع نمیشد فکر کنم یه پهباد بود</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22247" target="_blank">📅 01:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22246">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromamirali</strong></div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22246" target="_blank">📅 01:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22245">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhossein</strong></div>
<div class="tg-text">داداش سمت غرب (شهرقدس ) یه چی اومد انگار سقوط میکرد
نمی‌دونم چی بود عین هواپیما یا پهپادی ک داره سقوط می‌کنه</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22245" target="_blank">📅 01:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22244">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromامیرشون🪐</strong></div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22244" target="_blank">📅 01:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22243">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پدافند غرب تهران فعال شد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22243" target="_blank">📅 01:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22242">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromامیرشون🪐</strong></div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22242" target="_blank">📅 01:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22241">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">BTC = 82000$
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22241" target="_blank">📅 01:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22240">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ: اگه ایالات متحده همین امروز از جنگ علیه ایران خارج بشه بازسازی این کشور ۴۵ سال طول میکشه
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22240" target="_blank">📅 01:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22239">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22239" target="_blank">📅 00:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22238">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22238" target="_blank">📅 00:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22237">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22237" target="_blank">📅 00:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22236">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22236" target="_blank">📅 00:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22235">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22235" target="_blank">📅 00:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22234">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldkTIjSATU7SYD4OnUi81FCb6in1d6F_PHF5jMoI1JQBECacxGEAFcFYsf9RVZcEpgzjwdWtLgxGyNvD1dogSN9LhjcynQVofWQQT-z4Dw4tmbpbkwNI-hZxKWmZzZtS4sCLeqvWGcaXDIZ09mWo6ECTsJFPp0bbSro5ZR8BSokwPVViK4_Av0ZpaEvow3PqgfKZKvhJghNykE4z3u5KPbSDqd_fCN4Y4ERwABxZTXLr_TVYBFOs4_JyT-WTIh01DwUPk4KVuLAcXwu1Cm924oZne5saBlVWzK1l_xw0CHhYApBVlPykxb1swAbYKqMW91QZeQo5bW7vZF3GTwxH_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست : FBI وارد ماجرا شد بعد از آن که
شیرین سعیدی
، استاد اخراج شده دانشگاه آرکانزاس و حامی جمهوری اسلامی، پس از افشای اتهام سرقت علمی و حمایت از حکومت ایران، لادن بازرگان، فعال مخالف جمهوری اسلامی، را در X تهدید کرد که «با یک ارتش» به سراغ او خواهد رفت و اضافه کرد « کاری با تو خواهیم کرد که در تاریخ ثبت شود.» . او همچنین تهدید کرده قبر برادر اعدام‌شده بازرگان در کشتار ۱۳۶۷ را پیدا کرده و روی آن «رقص» خواهد کرد. سعیدی در سال ۲۰۲۵ نیز با استفاده از سربرگ دانشگاه آرکانزاس، نامه‌ای در حمایت از حمید نوری، مقام سابق زندان‌های ایران که در سوئد به‌دلیل نقش در کشتار ۱۳۶۷ محکوم شده بود، ارائه کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22234" target="_blank">📅 00:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22233">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22233" target="_blank">📅 00:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22232">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXwxoCO715ampefmbyr1vJlqvSLoxv4esPyAZLTRbeJ6OQzMEot83kY8iaxD2LN950K_LybhV06sIabBPeVZeynVsJbcHrZozmsamfFOd1UyGpF8tyb6tYrw6Sm6EkV1nlbG0Xy3S9LTJ-shJagNz-ySHll8T51FbLkCFz2lW7LIuRsXH1-Or_LMIwkm-6Tv6W2f6ywKXfCF1vyoAaGsgvFeKywMamCLrhZwFporTLxy0792eRouMNVy_Vjanr7KpAQvP4GBVBg2Moyl_ZXHBYORLGbP4E4bnmpd3h7SkVwVU6Q7tZZ8XFqtgEjeAtmPxPRxD-7SPeX9HtCQDyi_7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی نفت‌کش "مرجان" متعلق به ترکیه، از تنگه هرمز عبور کرد و از مسیری استفاده نمود که توسط ایران تعیین شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22232" target="_blank">📅 00:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22231">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نتانیاهو: ارتفاعات علی‌الطاهر لبنان دیگر تهدیدی برای ما نیست!
وی همچنین گفت که نظامیان اسرائیل، شمار زیادی از «شبه‌نظامیان» را در این منطقه از بین برده‌اند. ارتش اسرائیل ساعتی قبل اعلام کرد که به‌صورت عملیاتی بر زیرساخت‌های وابسته به حزب‌الله در ارتفاعات «علی الطاهر» در جنوب لبنان مسلط شده است
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22231" target="_blank">📅 23:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22230">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وای نت عبری : حملات نیروهای دفاعی اسرائیل در المنصوری در منطقه صور، در وادی السلوقی و در زوطر الشرقیه در جنوب لبنان در حال انجام است
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22230" target="_blank">📅 23:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22229">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گاردین : رئیس سیا در سفر به روسیه از مسکو خواسته حمایت خود از تهران را کاهش دهد
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22229" target="_blank">📅 23:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22228">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ارتش اسرائیل : عملیات پاکسازی دو تونل زیرزمینی حزب‌الله در ارتفاعات علی‌الطاهر در جنوب لبنان به پایان رسیده و اکنون در حال خنثی‌سازی این زیرساخت‌ها هستیم
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22228" target="_blank">📅 23:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22227">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سنتکام : از دیروز فقط یک دشت کردیم ، مجبورش کردیم دور بزنه برگرده
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که نیروهای آمریکایی
مسیر ۸۷ فروند کشتی تجاری را تغییر داده‌اند
، ۳ فروند را غیرفعال کرده‌اند و ۲ فروند را بازرسی کرده‌اند تا از رعایت مقررات پس از تشدید محاصره بنادر ایران اطمینان حاصل کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22227" target="_blank">📅 23:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22226">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اتاق جنگ با یاشار : گزارشهای زیادی دارم از شلیک کوتاه پدافند شرق و همچنین بعد از مدتی پدافند غرب تهران . فکر کنم بی‌بی پهپادهای شناسایی را برای رصد تحرکات تهران اعزام کرده است. مسأله ای که خود رژیم نیز بارها به حضور پهپادهای شناسایی آمریکایی/اسرائیلی در آسمان پایتخت اعتراف کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22226" target="_blank">📅 23:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22225">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏ کانال ۱۴ اسرائیل : پاکستان و قطر طی دو هفته گذشته دو بار از ترامپ خواسته‌اند بخشی از دارایی‌های مسدودشده ایران را برای کمک به کاهش تنش آزاد کند، اما ترامپ هر دو درخواست را رد کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22225" target="_blank">📅 23:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22224">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جی دی ونس : اگر به ترکیه، آذربایجان، قطر، امارات متحده عربی و عربستان سعودی نگاه کنید و به طور کلی به سراسر جهان بنگرید، در واقع شاهد تعداد زیادی از کشورها هستیم که گاهی اوقات حاضر به بیان علنی این موضوع نیستند، اما در پشت پرده کارهای بسیار خوبی انجام می‌دهند تا به ما کمک کنند تا اطمینان حاصل کنیم که ایرانیان به دلیل شلیک به کشتی‌های تجاری، مجازات شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22224" target="_blank">📅 22:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22223">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">جی دی ونس: ما می‌توانیم منطقه را ترک کنیم، اما کشورهای عربی حاشیه خلیج‌فارس به ما می‌گویند این بدترین اتفاق ممکن است, با وجود اختلافات سیاسی ما با چین، آنها مایل به همکاری با ما برای اعمال فشار بر ایرانی‌ها هستند
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22223" target="_blank">📅 22:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22222">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22222" target="_blank">📅 22:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22221">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeBlvfazGKr9vEjcKXa6h5GxffRDGuufmpEOFZs_XIqavR498c8MTRcrWhsVK9MRf9jQOqnO-8S-FFEqZHCFN7IoddWMPTE_gnO8lKsi8J8OGbEiktGygxCEoLD4_oYCJOLZeeauUg6QoTVqc1dsCk-pXoeGNBhq6pfR9UBnlQ5aECVz4HYkTxvv07CuiRTa2E-IsbN8SueBILcJFKkddvKc4eCK2lHxMBR1VD5mszBaEURUcYcWLFz1rMf1P_c8N2NGsQbB8d8_zuME1vEf6T8HORL3KpkwRiM1x19y3Lb4_kzPizeyllBKPOf1k5mFuifcmGUD_ue-lUiuI6zVuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
🙌🏾</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22221" target="_blank">📅 22:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22220">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نه قزه، نه لبنان، جانم فدای ایران.
عراق، سوریه، لبنان، فدای ایران.
شلیک به قلب دشمنان
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22220" target="_blank">📅 22:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22219">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22219" target="_blank">📅 22:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22218">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">جی دی
ونس: ما تا زمانی که ایران از شلیک به کشتی‌ها دست نکشد، با آن مذاکره نخواهیم کرد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22218" target="_blank">📅 22:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22217">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22217" target="_blank">📅 22:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22216" target="_blank">📅 22:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22215">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22215" target="_blank">📅 22:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22214">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22214" target="_blank">📅 21:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22213">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کانال ۱۴ اسرائیل : ارتش اسرائیل با غلبه بر هشدارهای صریح تهران، شبکه استراتژیک زیرزمینی حزب‌الله در رشته کوه علی الطاهر را با موفقیت پاکسازی کرد. تمام تروریست‌های حزب‌الله و مربیان سپاه پاسداران از بین رفته یا مجبور به فرار شده‌اند.
تخریب این دژ اکنون در حال انجام است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22213" target="_blank">📅 21:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22212">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">لحظاتی پیش یک مقام ارشد سیاسی اسرائیل به شبکه 14 این کشور اعلام کرد:
ما نشانه های جدی مشاهده میکنیم از آمادگی ایران برای حمله موشکی به اسرائیل.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22212" target="_blank">📅 21:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22211">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2759f740dd.mp4?token=bgTrHG8O3CwRgDKCVyX54uYQTL4sYh7r54IBAeboQj5nlS54shTPPwX_Nt5wFTv2qp4pKZtxY5svRsu3cn4SWDSASeQC7FZ_TMv6SILQKYJQes7zZVxK4J0LUUmmfBKA2QGZuBZJyz30SOHfxmzOO_xN1ei1iSc5VW_jiR5VGFFAx6SDy3Jc_1E8r0e43KMJp0z7fO-j35T67opNM0-4iF555lQNW2QRKqes4bcUrmQu5PAcMiCD2IRKvpOd8e2EutQLh5AVTGx29sx5SQdiajuFMbquSuXMa8dBr7b8DtiXs6aeAt5JG3-A3UancpSrVP3E6ioHeASqIXRprAZBTF8BZxMCk-ADEurwJME9n2g64WPk4pW8pKG6QKYDDC25O6rG2eKGqLuPV9JSMu_5FsE3kBT8l40rSoIUuqoxIlIuYIvIVBNriKfWWNQsvfR-4SxkA0ZOIjgEI-18bHKR3YI0I8D5hnBjBWnv-lulymRs2XYiWrUYXGi9KvmztLv4xq50Z_UtCpwZ8638nX2D2tdghZox8bb-zIpO81ZPnZFjDHvpXteY0M0kj-bdFKdY_eXxIpul252DAeeiPn8PXBUfGBQ5q7SPEmr2ZjGhyHVKTTfHGzQFyP-Z6vJ4ro7efZg7-3tU_oqmtiw9GQGriF0BkXBe-lJQj4XZQkwQVoM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2759f740dd.mp4?token=bgTrHG8O3CwRgDKCVyX54uYQTL4sYh7r54IBAeboQj5nlS54shTPPwX_Nt5wFTv2qp4pKZtxY5svRsu3cn4SWDSASeQC7FZ_TMv6SILQKYJQes7zZVxK4J0LUUmmfBKA2QGZuBZJyz30SOHfxmzOO_xN1ei1iSc5VW_jiR5VGFFAx6SDy3Jc_1E8r0e43KMJp0z7fO-j35T67opNM0-4iF555lQNW2QRKqes4bcUrmQu5PAcMiCD2IRKvpOd8e2EutQLh5AVTGx29sx5SQdiajuFMbquSuXMa8dBr7b8DtiXs6aeAt5JG3-A3UancpSrVP3E6ioHeASqIXRprAZBTF8BZxMCk-ADEurwJME9n2g64WPk4pW8pKG6QKYDDC25O6rG2eKGqLuPV9JSMu_5FsE3kBT8l40rSoIUuqoxIlIuYIvIVBNriKfWWNQsvfR-4SxkA0ZOIjgEI-18bHKR3YI0I8D5hnBjBWnv-lulymRs2XYiWrUYXGi9KvmztLv4xq50Z_UtCpwZ8638nX2D2tdghZox8bb-zIpO81ZPnZFjDHvpXteY0M0kj-bdFKdY_eXxIpul252DAeeiPn8PXBUfGBQ5q7SPEmr2ZjGhyHVKTTfHGzQFyP-Z6vJ4ro7efZg7-3tU_oqmtiw9GQGriF0BkXBe-lJQj4XZQkwQVoM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: درباره حمله به یک مراسم عروسی در اوایل این هفته که ایران می‌گوید چند کشته و ده‌ها زخمی بر جا گذاشته، آیا گزارشی به شما رسیده و آیا آمریکا مسئول آن بوده است؟
جی.‌دی. ونس: از این موضوع اطلاع دارم و سنتکام در حال بررسی آن است. من هم گزارش‌های عمومی رسانه‌ها را دیده‌ام، اما درباره روایت رسانه‌های دولتی ایران از وقایع این درگیری تردید جدی دارم. با اطمینان می‌گویم آمریکا برخلاف سپاه پاسداران، هرگز غیرنظامیان را عمداً هدف قرار نمی‌دهد و چنین کاری را نه انجام داده و نه انجام خواهد داد. البته در جنگ ممکن است اشتباهاتی رخ دهد، اما درباره این حادثه هنوز اطلاعات کافی نداریم و بررسی کامل و همه‌جانبه آن ادامه دارد. برای ما مهم است که حقیقت را بدانیم و اگر اشتباهی از سوی نیروهای آمریکایی رخ داده باشد، آن را بررسی کرده و از آن برای جلوگیری از تکرار اشتباهات درس می‌گیریم
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22211" target="_blank">📅 21:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22210">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ارتش اسرائیل: طی ساعات گذشته به کنترل عملیاتی ارتفاعات «علی‌الطاهر» در جنوب لبنان دست یافتیم و دو مسیر از زیرساخت‌های زیرزمینی حزب‌الله در این منطقه را پاکسازی کردیم. عملیات برای خنثی‌سازی تونل‌ها و تأسیسات زیرزمینی حزب‌الله همچنان ادامه دارد.
علی‌الطاهر
؛ منطقه‌ای راهبردی در نزدیکی نبطیه که حدود ۱۵ کیلومتر با مرز اسرائیل فاصله دارد و حزب‌الله و سپاه در زیر آن شبکه‌ای از تونل‌ها، مراکز فرماندهی و انبارهای تسلیحاتی ایجاد کرده اند.
ایران پیش تر اعلام کرده بود در صورت حمله به این مجتمع زیر زمینی در جنوب لبنان که نیرو های سپاه نیز در آن حضور دارند شدیداً به اسرائیل حمله خواهد کرد.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22210" target="_blank">📅 21:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22209">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/188d3827bd.mp4?token=DdnKL8jQ9RWEXBwtL1HZ6dWBqyUKsJnUdXtH8XOZUBVSpvDn9YL-HxJI2eFL13HVWUCFcFAIYDRmV2xdNqSbR5vOOm8jHl6w-H5HLhM0C5Oj4AVvNIEsilTU73WDyrgM0HuzLe0UVcpg5mmeJyWQm5a8m6NlJQxQwSmHubbeofGEVc0ufYmXT9-41e7DRp1uZFYhnDr39OvwnvZGKHkkIjPcvr_BKnEd5WNYkBYcf0ZpaKeteQdb5-OH2ljAeIWI8M8JYNVQiayJfGjQwpFtvruS1J_zTXmA0kVSuMTS9dPtCvwKOzXDZkO09Y0T3FTEGaRv4NFoSt5E3JjJFpXy47zFDf3Ak5w_nwUjhhAhadbIqAClMSr5zs9b_LmdcwgWWIg8d5n42tTo4KO0FTbD3j5TJDgnt-FCMudCo3g2PzD8RTpTbwzqucGqXDJjB2501VtCh_6aHBoCi6SN6DbqmAJuUiAVtIpH9ye4KvMNRPqZY_Rlnd-xA-xbsh81D-_XeONib1l4-D_7VGHUOpGM49u7Z6dq4Jg2_C9u7lgl5fJn7A0P6kDAAFzFPJgpif_ixkUQxVjr6bYTWOWu14DpEMx7wJ-GLgOrxncd2CqkrNNwe6rGozI1CBOXPySl7SQ7KPL-1f1lxI_YjnVkf8SUxyZXYVha2ODq8QV0ZCYqsrk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/188d3827bd.mp4?token=DdnKL8jQ9RWEXBwtL1HZ6dWBqyUKsJnUdXtH8XOZUBVSpvDn9YL-HxJI2eFL13HVWUCFcFAIYDRmV2xdNqSbR5vOOm8jHl6w-H5HLhM0C5Oj4AVvNIEsilTU73WDyrgM0HuzLe0UVcpg5mmeJyWQm5a8m6NlJQxQwSmHubbeofGEVc0ufYmXT9-41e7DRp1uZFYhnDr39OvwnvZGKHkkIjPcvr_BKnEd5WNYkBYcf0ZpaKeteQdb5-OH2ljAeIWI8M8JYNVQiayJfGjQwpFtvruS1J_zTXmA0kVSuMTS9dPtCvwKOzXDZkO09Y0T3FTEGaRv4NFoSt5E3JjJFpXy47zFDf3Ak5w_nwUjhhAhadbIqAClMSr5zs9b_LmdcwgWWIg8d5n42tTo4KO0FTbD3j5TJDgnt-FCMudCo3g2PzD8RTpTbwzqucGqXDJjB2501VtCh_6aHBoCi6SN6DbqmAJuUiAVtIpH9ye4KvMNRPqZY_Rlnd-xA-xbsh81D-_XeONib1l4-D_7VGHUOpGM49u7Z6dq4Jg2_C9u7lgl5fJn7A0P6kDAAFzFPJgpif_ixkUQxVjr6bYTWOWu14DpEMx7wJ-GLgOrxncd2CqkrNNwe6rGozI1CBOXPySl7SQ7KPL-1f1lxI_YjnVkf8SUxyZXYVha2ODq8QV0ZCYqsrk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو، درباره جمهوری اسلامی: ما با تهدید نابودی از سوی رژیمی مواجه بودیم که می‌خواست با استفاده از بمب‌های هسته‌ای ما را نابود کند. من به توانایی ما برای از بین بردن این تهدید برای همیشه، یعنی سرنگونی این رژیم، اطمینان دارم. این مأموریت محوری همچنان پیش روی ما قرار دارد، اما نزدیک است؛ غیرممکن نیست و در دسترس است. آنها بی‌دلیل از حمله به ما اجتناب نمی‌کنند؛ آنها به همه حمله می‌کنند، فقط به ما نه، چون از قدرت ما، نیروی بازوی ما و اراده ما آگاهند. من به دشمنانمان به‌طور کلی می‌گویم: با ما بازی نکنید. اگر چیزی آموخته‌اید، با ما بازی نکنید. ما قدرت، اراده و وحدت درونی لازم برای غلبه بر شما را داریم
@WarRoom
فقط عرق خوری‌آخرش
😂
🍷</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/22209" target="_blank">📅 21:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22208">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش پرتاب موشک/پهپاد از اطراف تبریز ، حتما به کمپ کورد های عراق
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/22208" target="_blank">📅 20:54 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOZpgOGa12719w1dlxfCT-nGRmRIeJTEGxKN_fThXsNza6zvX6sDISyKM-oOz_cyzlALgyB5Tw0L0Mknkns189rbJaQjs7u5h1cFwNIGNXbNnPw2S4E8j5Hz9gplvCYauxyiVcilSwOKNwVUh7e_1zb7QJ2WHdFaQtsQ--VEpVqUnKvdClS7AI6pKrJIGx7RNO1nwX6j7YzemHiqa6XYY8dtnhTaF_tA97o2uTNxZbPpCs_BIN1zPiXRukT0k8muxwT5U5iQllcCTmRQVoNjcbU_nQvudhLmt2uO52BKSGJE_23_a7_EOloi6DYdZEj68Poe3YgQdvulg6pjlaqM3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا : امیر یاریاب، فرمانده عملیات سایبری فرماندهی سایبری-الکترونیکی سپاه پاسداران (IRGC-CEC) است. او در این سمت، گروه‌های سایبری مخرب وابسته به سپاه، از جمله «شهید همت» و «شهید شوشتری» را برای هدف قرار دادن زیرساخت‌های حیاتی آمریکا هدایت می‌کند. ما برای اطلاعاتی که به شناسایی یا یافتن یاریاب و افراد یا گروه‌های مرتبط با این عملیات‌های سایبری منجر شود، تا
۱۰ میلیون دلار پاداش
تعیین کرده این.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22207" target="_blank">📅 20:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کانال 14 عبری: افزایش قابل توجهی در سطح آمادگی و هوشیاری در داخل اسرائیل، با توجه به احتمال از سرگیری درگیری‌های نظامی مستقیم با ایران، مشاهده می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22206" target="_blank">📅 20:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/090e602491.mp4?token=Dmevlw0M_iewk8GVZo6FdcJSkeHDks5gywLhkEWei09RLW1k9LKR2WTWNKSxiXONi9SWUpHP-WTbt551aSMS9U9Q5yoKV6I64KjNiozUsjNc5_wBRpG1GMaTmQfCczQthMFwgBzacWM_hKJwgHkPYOsGn4TgY3FaCPX94vRPFSPSQ5BE526pcmICMjzvb8KU0rBrVJ9asiVSWBWyAjkZ19U5cHVhiC9NTbRGmSdg98ldFaU3ZWUBH27VFFXcUy5duxKLPt42m459_l0fhdyUUr81NblgSs93PONiVgKTlVNtra4vTZfLP713rFusXjuYWL0Ltk1lWRAmeqgm4THHPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/090e602491.mp4?token=Dmevlw0M_iewk8GVZo6FdcJSkeHDks5gywLhkEWei09RLW1k9LKR2WTWNKSxiXONi9SWUpHP-WTbt551aSMS9U9Q5yoKV6I64KjNiozUsjNc5_wBRpG1GMaTmQfCczQthMFwgBzacWM_hKJwgHkPYOsGn4TgY3FaCPX94vRPFSPSQ5BE526pcmICMjzvb8KU0rBrVJ9asiVSWBWyAjkZ19U5cHVhiC9NTbRGmSdg98ldFaU3ZWUBH27VFFXcUy5duxKLPt42m459_l0fhdyUUr81NblgSs93PONiVgKTlVNtra4vTZfLP713rFusXjuYWL0Ltk1lWRAmeqgm4THHPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره بریتانیا : کشور شما خوب پیش نمی‌رود.
فراموش نکنید که درصد بالایی از نفت خود را از تنگه هرمز دریافت می‌کنید.
و شما برای کمک به من آنجا نبودید. کشور شما برای کمک به من آنجا نبود!
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22205" target="_blank">📅 20:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22203">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نیویورک‌پست: عمان به‌طور محرمانه پیشنهاد ایران برای دریافت هزینه از کشتی‌های عبوری از تنگه هرمز را رد کرده است. به گفته یک مقام ارشد منطقه‌ای، مسقط حتی با دریافت هزینه‌های داوطلبانه برای خدمات زیست‌محیطی و امنیتی نیز موافقت نکرده و این پیشنهاد برخلاف ادعای پیشین سپاه پاسداران، هنوز به توافق نهایی تبدیل نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22203" target="_blank">📅 20:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اتاق جنگ با یاشار : نتانیاهو داره هر روز رژیم رو انگول می‌کنه و صحبت از تغییر رژیم می‌کنه بعدم جنوب لبنان رو میکوبه سفت
💥
😂
خواهیم دید چه خواهد شد @WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22202" target="_blank">📅 19:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22201">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اتاق جنگ با یاشار : نتانیاهو داره هر روز رژیم رو انگول می‌کنه و صحبت از تغییر رژیم می‌کنه بعدم جنوب لبنان رو میکوبه سفت
💥
😂
خواهیم دید چه خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22201" target="_blank">📅 19:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نتانیاهو: "ما اطمینان داریم که قادر به سرنگونی نظام ایرانی هستیم. این وظیفه اصلی است و به زودی به انجام خواهد رسید."
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22200" target="_blank">📅 19:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22199" target="_blank">📅 19:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">@WarRoom
جنگ خاموش ؟</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22198" target="_blank">📅 19:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22197" target="_blank">📅 19:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQYa7LKNYvZKlr0BkqSB2WTB0kS8UoGeJx3dOg5emRRCw0ylrbTQzMCRux0jjHJe21nmbhikz31lQEjZppkhl1sG-IwjnDnKn5UQBx6cxVPRovuaaHrvOp2dAh-dINbAAfuS2hF_TMVw0mL9oJqLtmD6ESh7FQF3bmi_cNdWzlCi-t09EsXfRgOzFEjfaX4iwYNIU68mCk9fHO2ZaMG3V7jHGpjgSiZEsWcnon9YxzNU4pg8iwa60d0wk-WcUWLqNozpAEmCInkn_hZ2-fAnda1NQjf9nCyhhwXj6QALmgsbRntk1Q8I5t56OANW14_kLtqman5i6QaiyCd1ZaOkDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش پرتاب موشک/پهپاد از سیریک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22196" target="_blank">📅 19:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گزارش تایید نشده : یاشار پدرم تو نیروگاه برق همدان کار میکنه ,میگه نیروگاه برق ۴۰۰ کیلو ولت رو زدن ,حدود یک ساعت پیش تا دو ساعت , میخواستم باهاش تماس بگیرم ولی نمیشد الان زنگ زد گفت
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/22195" target="_blank">📅 19:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6kw1iF-3A9cwTzIhD2DxjO9GWndW8zQ5BOvGfOTpXgOtES4k8mxLKDbzbGmsUZgH8yk04Znr6R7djLxdP_54LKBrri6lY6dfbq4ypqweMl8YdLKpC-ZOq6NiBjQFweNg6b7_fcBnEUycfnwAbPXMvE23gl0EJ89wjF6IOJ_YCxLTkbnOEjnVxkfqgxC9qFTvCPBTwwamZqcnwGiPo1ltW0WRn7_t_F4eTIuom1vYzMS90h1TYz8qGc73hAYbuAf-83hJL04D8j4ky-gIAqwoNV7geIPGIBgsrrIP-D9ge6xGpl2B1HnC6AFZEQFcC69b4CmZ2krq8_HMtTWLoZq3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تبلیغ از طرف من نیست ! پولی ندید  بهش !</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22194" target="_blank">📅 19:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cx1nvSNk5woBtGUvqAkhiWBeYteqz7f3H1aCz1x5HXe4ZrGCLbiFOhyltjbQ-VbaoFN64MA14Blz8IAMoNd7-bVyfIETqqYJkNYMq0fMnTjo6M_-HjhYbefoodIumxTiZETCPvN2H4MX4VJHKreRi8iQIR63Uea4AQlBc3ZQ6uR85-Y0SlboH5FKvYGxSUvTEX31RxnVM9qytpXNE3y65Jl7RFgcrcRV0PN56TIwcyvc-HTMQM3eLT8U58A94xzXNWy1jaxjpborwqJs_pZtPfBddZSs6y3RsiNKT0U-LaGNrO0AyJwYIiIlC2RApNqCOW_PQwQqkbvzFvssW_dsxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای رسانه‌های خائن و پلیدی که از گزارش دقیق عملیات نظامی ما در ایران خودداری می‌کنند، باید گفت ما عملاً مقادیر نامحدودی مهمات درجه متوسط تا بالا در اختیار داریم؛ بسیار بیشتر از آنکه بتوانیم در این عملیات یا هر جنگ دیگری (که بسیار بعید است!) که به‌طور غیرمحتمل رخ دهد، مصرف کنیم. علاوه بر این، ما مهمات را در سطحی بی‌سابقه تولید می‌کنیم. ما در حال انباشته‌سازی و آمادگی برای هرگونه سناریوی احتمالی هستیم. ما این مهمات را برای خودمان، یعنی ایالات متحده آمریکا، نگه می‌داریم نه برای فروش به دیگران؛ اما فروش به متحدان به‌زودی از سر گرفته خواهد شد. همچنین، لطفاً اعلام شود که دولت بایدن بسیار بیشتر از آنچه ما در ایران مصرف کرده‌ایم، مهمات را بدون هیچ هزینه‌ای به اوکراین اهدا کرد. صدها میلیارد دلار به اوکراین و ناتو به‌صورت رایگان داده شد؛ هزینه‌ای که اروپا می‌توانست پرداخت کند اگر تنها از آن‌ها درخواست می‌شد، اما ما آن مبلغ را مطالبه خواهیم کرد، اگرچه با تأخیر!
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22193" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22192">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adgvOFMXPbDmAXeF1wXnOJnX9MHkl4o-OV_jDesF7ZdlL2deS-UMVE3sMb-Pl1e-0lkgNvhsKtUtJ9S1hNQaSsaQM7TzTCg2jD_hHgkD3rknKTDfWOebYGyDsh83GZI6jmYk3h23YlBpAEROcz_0aObVkHpaYe_mlwTlH9JQaTGatmK2NpPZq5z0E_WXAKxOAqRxixIWw4ter9wi2yMEosAOyPeVhoG4C8JVon-_mkk9v4gGtLcxMx3m38ZagazAz_V7Np8KJMb1Ca4yIHPF8mrOl3uPQMPbL6RSVe0C5D0OXuG_mTI-X0pVPe4I7CsZeNg-1quawgZg8ISSkupcHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : مردم و رسانه‌هایی که مدام بر این موضوع تأکید می‌کنند که ما مهمات نداریم (و صددرصد اشتباه می‌کنند!) در واقع خائن هستند. آن‌ها این کار را می‌کنند زیرا ترجیح می‌دهند ایالات متحده در جنگی که به‌راحتی در حال پیروزی در آن هستیم شکست بخورد، تا اینکه ببینند من پیروز می‌شوم!
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22192" target="_blank">📅 18:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22191" target="_blank">📅 18:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اسرائیل نشنال نیوز : کانال ۷ عبری مدعی شد موشک‌های ایران به هتلی در اردن که افسران نظامی آمریکایی در آن اقامت داشتند اصابت کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22190" target="_blank">📅 18:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f75591b88.mp4?token=klEiynjnOjg8kQIcX4fmRMfDzV-9lO4Y2ZOzNfFsu_D0qrBRJlFYVH_rIwr5uqTVSLJN2xg2onGcOCNyZxAtttxC5Z4jsey-89iqcANBuBP6evINFMajuedcM08aZp6j1QUgOeuWhKm94jnDwqtjwIMi8Cyw42evsgpV_sse5rE0nz6k_U-S6RPvgDOWOfZQqvDYjQWfckbX54rwYDvaCwBTWvPDIiCQpsfGRMtjscUzttD2p-DroxGWwwRHW2wUEgpt_xCFwZCRjmNsaeAapR6N_pL__hOWiBt4sCxLmLM7wQaXaN1rq538dEgnSnEo0A3MsWLxmA9Th1tBSxT4gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f75591b88.mp4?token=klEiynjnOjg8kQIcX4fmRMfDzV-9lO4Y2ZOzNfFsu_D0qrBRJlFYVH_rIwr5uqTVSLJN2xg2onGcOCNyZxAtttxC5Z4jsey-89iqcANBuBP6evINFMajuedcM08aZp6j1QUgOeuWhKm94jnDwqtjwIMi8Cyw42evsgpV_sse5rE0nz6k_U-S6RPvgDOWOfZQqvDYjQWfckbX54rwYDvaCwBTWvPDIiCQpsfGRMtjscUzttD2p-DroxGWwwRHW2wUEgpt_xCFwZCRjmNsaeAapR6N_pL__hOWiBt4sCxLmLM7wQaXaN1rq538dEgnSnEo0A3MsWLxmA9Th1tBSxT4gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای اسرائیلی، با پشتیبانی تانک‌های مرکاوا، در حال پیشروی در جنوب لبنان هستند
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22189" target="_blank">📅 17:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مقام آمریکایی به خبرگزاری الجزیره گفت پایگاه‌های نظامی آمریکا در منطقه، از جمله پایگاه‌های این کشور در کویت، در جریان حملات تلافی‌جویانه شب گذشته ایران
هیچ‌گونه آسیبی ندیده و هدف حمله قرار نگرفته‌اند
. الجزیره پیش‌تر گزارش داده بود که ایران در واکنش به حملات آمریکا، موشک‌ها و پهپادهایی را به سمت اهدافی در کویت، بحرین، اردن و عراق شلیک کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22188" target="_blank">📅 17:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22187">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">در صورت ازسرگیری جنگ، ایران ۳ گزینه برای تشدید حملات در اختیار دارد
۱.
گسترش حملات به کشورهای عربی خلیج فارس
، از جمله هدف قرار دادن تأسیسات نفت و گاز، نیروگاه‌ها و تأسیسات آب‌شیرین‌کن؛ اقدامی که می‌تواند به افزایش شدید قیمت انرژی و آسیب به اقتصاد کشورهای منطقه منجر شود.
۲.
جلوگیری از خروج بیشتر نفت از منطقه
با تشدید فشار بر کشتیرانی و تنگه هرمز و تلاش برای متوقف کردن صادرات نفت از خلیج فارس.
۳.
گسترش حملات به منافع آمریکا و کشورهای غربی در خارج از منطقه
، از جمله حملات مستقیم یا غیرمستقیم به اهداف غربی.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22187" target="_blank">📅 17:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بلومبرگ: درگیری آمریکا و ایران به بن‌بست رسیده و هیچ نشانه‌ای از حل‌وفصل قریب‌الوقوع آن دیده نمی‌شود. در حالی که حملات متقابل ادامه دارد، تلاش‌های دیپلماتیک برای پایان دادن به درگیری پیشرفت قابل‌توجهی نداشته است. تهران همچنان از عقب‌نشینی از مواضع خود خودداری می‌کند و واشنگتن نیز فشار اقتصادی و نظامی را ادامه می‌دهد. هم‌زمان، دولت ترامپ در حال بررسی راه‌هایی برای مهار درگیری است، اما احتمال طولانی‌شدن جنگ همچنان جدی است. گزارش‌های امروز نیز نشان می‌دهد درگیری وارد مرحله‌ای فرسایشی شده و آمریکا حتی استقرار نیروهای خود در منطقه را تا سال ۲۰۲۷ تمدید کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22186" target="_blank">📅 17:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سخنگوی قرارگاه خاتم‌ الانبیا:
عملیات های تهاجمی علیه آمریکا ادامه خواهد داشت.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/22185" target="_blank">📅 17:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nsg4eDQeVuzLT9t1PiugQQcRPe1y42bnS-pwocHbtVSxbC_D22Mt1PYDWmOj-UsgdCuZKHPiaGr07d0cnxol-_OqRhI-DCZSc8Le6-H0SpaJFp2pTYaj3b6emMRG2WNNaGPEPsdqqSDUbQhKZ-ViTCnxyhzy96AUoIgtqJQH3ZQ1AFsNYocam9M_W7xb3cbflNDEb3QAYjRjrw-IM9J3LpvhHojvvSXPcMPUOPrSIPLKQ_3tISGFA6vkPWQ1cYGpPEdtt9NSeonlp40zPhCa1dJ1ruX5JQdl8ldWYdelTObcXSRS3ksFuPKYjghF3HWwleSN5krF_CzSp4rdV0g8vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش اولیه تاییدنشده
از حمله به یک سایت در استان فارس
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22184" target="_blank">📅 17:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c459a770c1.mp4?token=mGNjmoqqVSlr5l1oi6vpMqJVtkYsSTB8mJlZFL0AWPMwAFLyBPw90kVX6C48y0NeDqJvbzDCV8uuehOty5LlTTBWnJSDodrj1BCcdieFx5gt3rueDRdI7TKdY1xC52eFIUfalhWesjSQTJA4vASp5QeKusdcN_04cyDG8rVjRt412llbCzLm7mAd9MEOCopriDrnYHf6iBPSsSggc8wCp8KSnDZZge_rv1PPxf1tirciL7Sea8roCuOAmHnHFZDnE9CgMCeG77RV2_n5VOiLYKhQbeHHsL2aw7YC2jenv-yzcNK3Da9yzaj0OMICCZsZOXjdkAdqsK8QJW4L44x0ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c459a770c1.mp4?token=mGNjmoqqVSlr5l1oi6vpMqJVtkYsSTB8mJlZFL0AWPMwAFLyBPw90kVX6C48y0NeDqJvbzDCV8uuehOty5LlTTBWnJSDodrj1BCcdieFx5gt3rueDRdI7TKdY1xC52eFIUfalhWesjSQTJA4vASp5QeKusdcN_04cyDG8rVjRt412llbCzLm7mAd9MEOCopriDrnYHf6iBPSsSggc8wCp8KSnDZZge_rv1PPxf1tirciL7Sea8roCuOAmHnHFZDnE9CgMCeG77RV2_n5VOiLYKhQbeHHsL2aw7YC2jenv-yzcNK3Da9yzaj0OMICCZsZOXjdkAdqsK8QJW4L44x0ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خدمه‌ ناو هواپیمابر آبراهام لینکلن ، به تایلند رسیدن و رفتن تا پس از یکسال در دریا بودن در خشکی عشقو حال کنن
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/22183" target="_blank">📅 16:56 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
