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
<img src="https://cdn4.telesco.pe/file/FMfvbt8os8L0QgRgY3r1RJZqUjhGSrWgSJIFxwunHPHgHwT4GhS5eZeBCUuSJT8ZITdXW6o6K5dvNVcIVaxJFvMgvBYRuO2ZF1MLjTSVikVKfaMsReDPEO4GZyMfMTaXU6f40t3eZbqMn8Vvboax_KscTAcKq8Gq16pS9MwMBIwi64xlpjX81dlz58Jpm0qSKBaXHYTWDisQN0WI8u8Qgwgvi0owv1DRDPeIBsgrkFXh7sEeJmRdWvwTqysolLkOk2NLKgZ20-iXpex03qudmuS_NrD4fi2UHHX5LmU-vKV6mhONBL9CEQyeLc1rnJnABfCMpnNMxpFQyIuhJKBSgg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 11:50:28</div>
<hr>

<div class="tg-post" id="msg-140035">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
فووووووووووووری از ورزش سه
🎙
🎙
علیرضا بیرانوند از اول آبان به طور قطعی و صد در صدی سرباز محسوب میشه و دیگه نمیتونه برای تراکتورسازی تبریز بازی کنه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
〰️</div>
<div class="tg-footer">👁️ 154 · <a href="https://t.me/SorkhTimes/140035" target="_blank">📅 11:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140034">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
تیکدری‌ جای جلالی را گرفت!
🗣
🗣
مصدومیت ابوالفضل جلالی می‌توانست برای تارتار دردسرساز شود، اما مهدی تیکدری‌نژاد با عملکرد خوب در پست دفاع چپ حسابی جایش را پر کرده.
🗣
🗣
تیکدری در ۴ بازی اخیر فیکس بوده و پرسپولیس در ۲ بازی اخیر کلین‌شیت کرده. حالا با این عملکرد،…</div>
<div class="tg-footer">👁️ 760 · <a href="https://t.me/SorkhTimes/140034" target="_blank">📅 11:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140033">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
علیرضا بیرانوند: به عنوان یک سرباز جان بر کف ایران و اسلام، آماده رفتن به خط مقدم و خدمت مقدس سربازی هستم و از اول مهر به هر تیمی که معرفی شوم حضور پیدا خواهم کرد و در زیر این پرچم مقدس به انجام وظیفه خواهم پرداخت!
😁
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 899 · <a href="https://t.me/SorkhTimes/140033" target="_blank">📅 11:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140032">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
❌
❌
حریفان پرسپولیس در نیم فصل اول:
✔️
هفته اول: شمس‌آذر
✔️
هفته دوم: اس‌خوزستان
✔️
هفته سوم: تراکتور
✔️
هفته چهارم: ملوان
✔️
هفته پنجم: استقلال(میهمانیم)
✔️
هفته ششم: ذوب‌آهن
✔️
هفته هفتم: خیبر
✔️
هفته هشتم: صنعت نفت
✔️
هفته نهم: مس شهر بابک
✔️
هفته دهم: فولاد…</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/SorkhTimes/140032" target="_blank">📅 11:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140030">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
علیرضا بیرانوند: به عنوان یک سرباز جان بر کف ایران و اسلام، آماده رفتن به خط مقدم و خدمت مقدس سربازی هستم و از اول مهر به هر تیمی که معرفی شوم حضور پیدا خواهم کرد و در زیر این پرچم مقدس به انجام وظیفه خواهم پرداخت!
😁
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/140030" target="_blank">📅 11:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140029">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_bwC0Ky2a1nNLE7Ctv4C5VRfWZiqpgY10EqkjYKdnvYz7m94_rpRH0MV0r_DTQGIHP4a8UaS-dQbtPkKVs7QWUx8Byg48CnjADKqfGvlP4mK6yKlPFGyljVp9icJ2bFvzSKLWTvpbSr3bqlKCu250_Y4dXLH3dpIXuJJdvfKsLbyuRrFUWYpH9WHc_vEO5Szy-yvV7DajOg9j34m1bB5thdKHbdw9iHifLn1GoIpQzgIIuQFd5DxUoxtKyNPQfE32O8C_r54csnahJPTnVnPn0_rvR1wsK3OcQkO9MFZomrrDZ4sSJIZXzaEBWFvDrzQ1K-XkBmdMwBnd12QALfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
دیدار استقلال و تراکتور در هفته هشتم لیگ‌برتر روز پنجشنبه ۱۶ مهرماه در ورزشگاه تبریز برگزار می‌شود. بزودی برنامه هفته‌های آینده لیگ‌برتر اعلام خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/140029" target="_blank">📅 11:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140028">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
پرسپولیس برای خرید امتیاز و راه‌اندازی تیم «ب» با بعثت کرمانشاه و فرد البرز مذاکره کرده؛ قیمت پیشنهادی این دو تیم هم به‌ترتیب 120 و 125 میلیارد تومان اعلام شده. احتمالاً تا امروز یا فردا تکلیف نهایی خرید امتیاز مشخص میشه
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SorkhTimes/140028" target="_blank">📅 09:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140027">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
پویش مردمی با عنوان فرستادن صفر بیرانوند بعنوان #سرباز_نخبه به جزیره سیریک در جنوب ایران راه افتاده
✔️
✔️
این بازیکن به دلیل پرتاپ های بلندش می تونه نقش پدافند سیار ایفا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SorkhTimes/140027" target="_blank">📅 09:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140026">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPhc76d0jZIH7eJz5EMHtOqCqexU1M_JbRzZh_GKfNWiHt9dT-elJCnDIPNpRN3vC23YeWIqaHlUzG09rVxNTR9r84e17OFn1QMxz5rB1UTLZG__HOsu6Qt0WV6bpcVFEO91xJ-VGdl1O25ZJRqQSpsXsaocP2ncAnpYahPepoPSTkJHH0LLxmOEtIy2gRSSb3AmkjOD6IE5gJXEM8OGMG9F8jb5VoH__dfk7gjjiUITjtySMnQDJPeqMJ89TuRtBX6SfgjFMsN24gH-v_EoaMV1rELJ6F0nlziNKOzzXTSHbN7KmKmm4asuArqjzfZmjDcPbx6pCPWFev0wzEhTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/140026" target="_blank">📅 09:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140025">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dgqDGsvTzT8pNQ0gapAffQTbYEE5aZbEX4ZQVbrwX-fTKj6Zj3j9J5gCI_YrNN-7LjMmmqc-LeBqhJgjtGZEx1CIz9tl6JnI7L2Vh_Z7kTrUfBllrL_MNdRArcAJuJnWz6d959vo2UicBZn6Vmtj6XTHK1i6hO1qDbhIUwZi8sfFgBh-rQx8jiSuRKI5r3biOHIfXPYoLLj2ZReOQNKuQ48OuTzIY78c1wwTj490O4W2DhLsVa63sbp0CGfJn4Y3ro-rdDB_IEqsGz4nVp9C3r1ysDZem-nDGXdLsxyx_YWdYKOcZH7Ck6-dcstwY123M3vCTrp7q4dnKNUxH43pCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بونوس ویژه اسپورت‌نود
🔵
با هر واریز بین ۵ تا ۱۰۰ میلیون تومان ۱۰٪ بونوس ورزشی تا سقف ۵ میلیون تومان دریافت کنید.
🔗
آزادسازی بونوس خیلی ساده‌ست؛ فقط کافیه یکی از این دو روش رو انجام بدی:
👇
📌
شرط تکی با ضریب حداقل ۱.۹
📌
شرط میکس با ضریب حداقل ۴
🟢
مدت استفاده از بونوس ۲ روز می‌باشد.
🔗
همین حالا واریز کن، بونوس بگیر و شانس بردتو بیشتر کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
مینی‌اپ رسمی اسپورت‌نود:
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/140025" target="_blank">📅 01:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140024">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
خدابنده لو: ارونوف به من گفت در ایران فقط دوست دارم برای پرسپولیس بازی کنم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/140024" target="_blank">📅 00:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140023">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
✔️
✔️
تیم دهوک عراق با مربیگری یحیی گل‌محمدی سرانجام بعد از ۵ هفته به اولین برد خودش دست یافت.
🇮🇶
در این مسابقه، دهوک که میزبان هم بود تا دقیقه ۷۳ یک بر صفر از نیرو هوایی عقب بود اما با دو گل ایگور برزیلی در دقیقه ۷۴ و ۹۰ به برتری جذابی رسید.
🇰🇬
دهوک با ۷…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/140023" target="_blank">📅 00:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140022">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
🗞
علیرضا بیرانوند ۶ روز پیش دفترچه سربازی شو پست کرده.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/140022" target="_blank">📅 00:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140021">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
فارس :
⚪️
اگه بیرانوند مهرماه دفترچه اعزام بگیره شاید بتونه با تمدید تو دو یا سه بازه تا نیم فصلو تراکتور بمونه
🗣
ولی اگه امکان تمدید تاریخ اعزام نباشه یا باید تا نیم فصل بدون تیم بمونه یا بره دسته یک و برای نیروی زمینی بازی کنه تا نقل و انتقالات زمستانی…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/140021" target="_blank">📅 00:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140020">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
پویش مردمی با عنوان فرستادن صفر بیرانوند بعنوان #سرباز_نخبه به جزیره سیریک در جنوب ایران راه افتاده
✔️
✔️
این بازیکن به دلیل پرتاپ های بلندش می تونه نقش پدافند سیار ایفا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/140020" target="_blank">📅 23:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140019">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a30d045eab.mp4?token=nT-M4suiOP9TyLN-7IZloQwpRvB3Ppdu8vuAHga-UajAZcwyDxQSeRcPgGZrEPk7e19FI2cUONaOGbSNR7FN3NpJS7K4AHuE6krB_ZiKCGc7qd0d5Q-soItQODx8whAiZBB1cjELa2pAvNsHMdhSepYbnRAYreRp_FezyCrDgGMBTRdb5GydGi-cf3UZ9wSslqwpih0NT4hoO4KKx5aAV0Tk4KGNpJE4HkM1Zy3ZuVDv45Eci0gCpWoZYohb2k0hFW4PfS50J95EEV-oBhX4jbm2IHj-RD1r1pZgPudRdpqHGpBaRD4LiaZj8bBdu2-5GAwY0GWh-D7rvw3CMi3rrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a30d045eab.mp4?token=nT-M4suiOP9TyLN-7IZloQwpRvB3Ppdu8vuAHga-UajAZcwyDxQSeRcPgGZrEPk7e19FI2cUONaOGbSNR7FN3NpJS7K4AHuE6krB_ZiKCGc7qd0d5Q-soItQODx8whAiZBB1cjELa2pAvNsHMdhSepYbnRAYreRp_FezyCrDgGMBTRdb5GydGi-cf3UZ9wSslqwpih0NT4hoO4KKx5aAV0Tk4KGNpJE4HkM1Zy3ZuVDv45Eci0gCpWoZYohb2k0hFW4PfS50J95EEV-oBhX4jbm2IHj-RD1r1pZgPudRdpqHGpBaRD4LiaZj8bBdu2-5GAwY0GWh-D7rvw3CMi3rrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/140019" target="_blank">📅 22:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140018">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e82ae3f4.mp4?token=ZT7yECmXlzLZOxDFvkd1kTIV1SuycfQjBMJp-3kT5eXMfAq41qpXKa9hfe7wl-_4yCg2GVI7E49QunH12dRYPxzvf7vfPjUVCb7Xwot4utBKWp_KmZ9EJoxn9CVlJOWpwFUKb9yls4TYLcZMCyq5OwEj6NP4K3USKb5tMRONoC3wk00s_noSXzuRl74VCSdfUMaI0A6q_O2ZahvBma01ntMysn_8RrpUUJfWLqSdfa-YxGUdcU2ellzmv4tsy3S7uctivCJSB0GVZMsGH7Hg00WA7vprqMVv-XIufee3-pm2t8ocP2zSiKARo2NUoxt2XdLAobd2ZRW_ZbtXBii8fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e82ae3f4.mp4?token=ZT7yECmXlzLZOxDFvkd1kTIV1SuycfQjBMJp-3kT5eXMfAq41qpXKa9hfe7wl-_4yCg2GVI7E49QunH12dRYPxzvf7vfPjUVCb7Xwot4utBKWp_KmZ9EJoxn9CVlJOWpwFUKb9yls4TYLcZMCyq5OwEj6NP4K3USKb5tMRONoC3wk00s_noSXzuRl74VCSdfUMaI0A6q_O2ZahvBma01ntMysn_8RrpUUJfWLqSdfa-YxGUdcU2ellzmv4tsy3S7uctivCJSB0GVZMsGH7Hg00WA7vprqMVv-XIufee3-pm2t8ocP2zSiKARo2NUoxt2XdLAobd2ZRW_ZbtXBii8fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خدابنده لو: ارونوف به من گفت در ایران فقط دوست دارم برای پرسپولیس بازی کنم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/140018" target="_blank">📅 22:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140017">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e23b00c48.mp4?token=h_ZF1wJus-sP4VvoBKHadACwMrLFj4Pkqxz_0F5esmUQsirv1TmuClvLDrnHsKFt09CMiBDaxoTqNGvQOlbiL0fSlGh1uQRflkZ6XKZ_jvfToW-C2BPw7VPjwTG09CcNwNpOqNsE2m-NEw-BEUTTwna2oRGR-ACqjYcRUsu5zsVuLQURf2N5r_rJhGAz2FiKLJrZgXDDYlkJFvf3tFyn4PNEeAcTrh4uFYjYjyd91DhZ7Xff9BWqjNqF4HKqJA3mGlYYf7ZbKMOh3CgaGdWMEBie01kDTUHqLkALls7MVeAOk2H5LOVTXQICqc50rs_nwug0uJXu1OyWwEKDZnjdjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e23b00c48.mp4?token=h_ZF1wJus-sP4VvoBKHadACwMrLFj4Pkqxz_0F5esmUQsirv1TmuClvLDrnHsKFt09CMiBDaxoTqNGvQOlbiL0fSlGh1uQRflkZ6XKZ_jvfToW-C2BPw7VPjwTG09CcNwNpOqNsE2m-NEw-BEUTTwna2oRGR-ACqjYcRUsu5zsVuLQURf2N5r_rJhGAz2FiKLJrZgXDDYlkJFvf3tFyn4PNEeAcTrh4uFYjYjyd91DhZ7Xff9BWqjNqF4HKqJA3mGlYYf7ZbKMOh3CgaGdWMEBie01kDTUHqLkALls7MVeAOk2H5LOVTXQICqc50rs_nwug0uJXu1OyWwEKDZnjdjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
کنایه تیکدری هافبک پرسپولیس به شرایط ورزشگاه آزادی: قول داده اند آزادی را تا 10،15 سال بعد آماده کنند!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/140017" target="_blank">📅 22:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140016">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f06355658.mp4?token=YAHvn9YedH02joKOzUXtilm6Qa-5-cmGGjDNiq8Yco9h6rDz-EorVBxBb0M9tDeEPASZE1-EtqJtUcmjgS-kmHu9ywmj-ge0pfPL9P2FrwBdfEAMgkpRsylCL2zoqfuxgNiuWVDgRSYq0SYy86Of43Jq_hH_CJckbWhbytz3VeusyuGkxOc_9W1Qrvmm7K-PWzW5PtGe4WTLd0DeVPKT30hvH4hXnvyLUpRBRci-wJr0fwSDQvVLUNlEom9WJIz9a924FlukBnb74L4UX2E4PdKgG0TYtM2ElnZ4ZcpMGT6X2ZYeMKj0yFb9AArq8hQGF4SxMrJr-lweLbk5ILcSXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f06355658.mp4?token=YAHvn9YedH02joKOzUXtilm6Qa-5-cmGGjDNiq8Yco9h6rDz-EorVBxBb0M9tDeEPASZE1-EtqJtUcmjgS-kmHu9ywmj-ge0pfPL9P2FrwBdfEAMgkpRsylCL2zoqfuxgNiuWVDgRSYq0SYy86Of43Jq_hH_CJckbWhbytz3VeusyuGkxOc_9W1Qrvmm7K-PWzW5PtGe4WTLd0DeVPKT30hvH4hXnvyLUpRBRci-wJr0fwSDQvVLUNlEom9WJIz9a924FlukBnb74L4UX2E4PdKgG0TYtM2ElnZ4ZcpMGT6X2ZYeMKj0yFb9AArq8hQGF4SxMrJr-lweLbk5ILcSXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
خدابنده لو هافبک پرسپولیس: امسال متحد شده ایم که هم در لیگ برتر و هم جام حذفی نتیجه بگیریم و هواداران را شاد کنیم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/140016" target="_blank">📅 22:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140015">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ff628214.mp4?token=d_Cl3Eeed-wKij-YxJDhuJrcHApR0vNR_JCeY8GXYBJECniwKU3OvbNkavjB0815dcHDDhjgicieCv5HUvXd6aOMUSosR0iaj-8QTR6mAqtioKWHAtA64L7GZS9L7DhErxgYi2SN5qDKPRzrFpd0XoN_HY0MGIKj0VIWHNPxXGkhphGyQOQyn-2t4BEJdepJREalQO3tO6e3J4DetCGEn1ne-Jk2xywZ8dTSesg-uIMieoL1_eo14gnmfXSNwZ_3QJX_P-Quz2PkgvA-uVR68b-6Cvd-GQPE2xCHGYL1nqxcq0edZW_atMyFLVqW6VUoZlymybaFHcIk0mOkJFEDIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ff628214.mp4?token=d_Cl3Eeed-wKij-YxJDhuJrcHApR0vNR_JCeY8GXYBJECniwKU3OvbNkavjB0815dcHDDhjgicieCv5HUvXd6aOMUSosR0iaj-8QTR6mAqtioKWHAtA64L7GZS9L7DhErxgYi2SN5qDKPRzrFpd0XoN_HY0MGIKj0VIWHNPxXGkhphGyQOQyn-2t4BEJdepJREalQO3tO6e3J4DetCGEn1ne-Jk2xywZ8dTSesg-uIMieoL1_eo14gnmfXSNwZ_3QJX_P-Quz2PkgvA-uVR68b-6Cvd-GQPE2xCHGYL1nqxcq0edZW_atMyFLVqW6VUoZlymybaFHcIk0mOkJFEDIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
خدابنده لو هافبک پرسپولیس: از اردوی ترکیه به بعد ترجیح دادیم بیشتر کار کنیم و عملکردمان را نشان دهیم تا اینکه در فضای مجازی باشیم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/140015" target="_blank">📅 22:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140014">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e456b94978.mp4?token=F2dMlQDM4CQYNEzeTEFy6NFr7neukEnWhkaNBr0AREbyyLbBFyEFpbL9QaE8NmeVSIixdKWCvJxKz3M8foRF_GSBIzrlMptRWd9TAZsgso5WJHO93JAj7IMGiMo1ghvqIvduzZSMgbMG_PFGWLvb3Ro3oZ5IsXwL9XYdyVzlYMFWEOq93gp2dXT_CU44tLe0WQgzQjaBzjTR0a5Ea6fQGvgfiLJtFpegHTy5VKDkpnJP0dsxeuI3rmCt6JUF0MHAeNoSCSQaZ7vbtQELom5PHZsRWPnkFegFYWw_9WNF4FU_7XNg-pd_-yR5PJwSNZ76sDf1t7IHtQXaBAGNFVSquw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e456b94978.mp4?token=F2dMlQDM4CQYNEzeTEFy6NFr7neukEnWhkaNBr0AREbyyLbBFyEFpbL9QaE8NmeVSIixdKWCvJxKz3M8foRF_GSBIzrlMptRWd9TAZsgso5WJHO93JAj7IMGiMo1ghvqIvduzZSMgbMG_PFGWLvb3Ro3oZ5IsXwL9XYdyVzlYMFWEOq93gp2dXT_CU44tLe0WQgzQjaBzjTR0a5Ea6fQGvgfiLJtFpegHTy5VKDkpnJP0dsxeuI3rmCt6JUF0MHAeNoSCSQaZ7vbtQELom5PHZsRWPnkFegFYWw_9WNF4FU_7XNg-pd_-yR5PJwSNZ76sDf1t7IHtQXaBAGNFVSquw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
خدابنده لو هافبک پرسپولیس:
🔄
🔄
تا روزی که هواداران و باشگاه مرا بخواهد در پرسپولیس می مانم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/140014" target="_blank">📅 22:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140013">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98087f79b6.mp4?token=cKwh2v2atE-QssUhdiejdARr3DQppJ7puItirX2MF02w5AahRIeDhCz2FVf7BApki2Cym3Cmj3JtMI_8TKBDQn99sFFlb7XW7Y9UiIxIGUUYAPF4RrmoAvzNJAEko9iIJgFvfZGXWX7Tgu8ERF0TTR21XfbMJq9FMtNDkZa86geKcAOmmaZOU24yA390wvDOT8m-NLFg4ZrXmB-M_CdYUHULj5zRMTZ0AG0Bu6JiJCUKo8ugAw3p-PS1HiGhOKzcmcA6jeFgmaXQxbaDlfySpBMes_EhmysYSlYegO7sBnX4OytaL2CnEqnuLwgpnERNRRxgbgZJ4glKc48k8H3MxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98087f79b6.mp4?token=cKwh2v2atE-QssUhdiejdARr3DQppJ7puItirX2MF02w5AahRIeDhCz2FVf7BApki2Cym3Cmj3JtMI_8TKBDQn99sFFlb7XW7Y9UiIxIGUUYAPF4RrmoAvzNJAEko9iIJgFvfZGXWX7Tgu8ERF0TTR21XfbMJq9FMtNDkZa86geKcAOmmaZOU24yA390wvDOT8m-NLFg4ZrXmB-M_CdYUHULj5zRMTZ0AG0Bu6JiJCUKo8ugAw3p-PS1HiGhOKzcmcA6jeFgmaXQxbaDlfySpBMes_EhmysYSlYegO7sBnX4OytaL2CnEqnuLwgpnERNRRxgbgZJ4glKc48k8H3MxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
مهدی تیکدری بازیکن پرسپولیس:
✔️
امسال یک تیم گردن کلفت داریم و نظر همه  هم همین است که امسال حقمان قهرمانی در لیگ است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/140013" target="_blank">📅 22:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140012">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9eb4ad0d3.mp4?token=rsLGMu3FcK4J5-qQppd3Lu1CnAuGUmgHXhRI90Rd6glpc7i3DEIKL_D50C74cxbmylFLolldyHaFD0tjHchz48z3LiXbRc67FmVptyNEzejsg_cDKkevCQ2P6fN_yPSTvUW1uHEyTy2f1fqGTERdsNQFzCX6Cv3s6Juls1gQSiNOl4UKTAePmEEQV-vH6xxw7KzGPUentmMfVFcdAvT3r-3zpaSm3r_0OTUam5VcijtFuuVRXHRmQ-SNfhMmnUZuXFp_KOBPidMvfrYXHf2XzsJEi5lKV2pVbHOp156Ny50wcW9lm4M7l8qJpRD9aP5mGzknq2erbnj2sxbu7H_2lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9eb4ad0d3.mp4?token=rsLGMu3FcK4J5-qQppd3Lu1CnAuGUmgHXhRI90Rd6glpc7i3DEIKL_D50C74cxbmylFLolldyHaFD0tjHchz48z3LiXbRc67FmVptyNEzejsg_cDKkevCQ2P6fN_yPSTvUW1uHEyTy2f1fqGTERdsNQFzCX6Cv3s6Juls1gQSiNOl4UKTAePmEEQV-vH6xxw7KzGPUentmMfVFcdAvT3r-3zpaSm3r_0OTUam5VcijtFuuVRXHRmQ-SNfhMmnUZuXFp_KOBPidMvfrYXHf2XzsJEi5lKV2pVbHOp156Ny50wcW9lm4M7l8qJpRD9aP5mGzknq2erbnj2sxbu7H_2lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بازگشا سخنگوی پرسپولیس: دنیل گرا در هر تیمی که قبل از آمدن به پرسپولیس بوده است کاپیتان آن تیم بوده و بازیکن بسیار پخته و باشخصیتی است!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/140012" target="_blank">📅 22:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140011">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5221c79f.mp4?token=hyN5OoEFg-sraHfE3hSgaQjE7o1mlYjfuJwnLUc-D1r4QUtHDSPfqSaMVSV75WnR4hNgK9RHbY7nKCHbu7tKSSBuvnWpidTmkv1L1olwqjRukBXBAGc3mT4M0kmF8GgUSz_5NhXUlaDDIjHxQ5VbHxnftPlmKKaxvVvt56XuZBEcmqXWgDkna-iuJVthZT_6Rh6kqha4VGF7K5dO8fZ5qQF1yuxsMIb790FiEARWvgrnxy5kkee8QpCEQvIiFkuTEtBKR-Xr8SFGntByl8kpAba0w8Ap7QF4BbFjZQjnm_rSIExIwlVnxL1_fNBt2gcDu2m4H0DnRxaf_OkyeN3jTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5221c79f.mp4?token=hyN5OoEFg-sraHfE3hSgaQjE7o1mlYjfuJwnLUc-D1r4QUtHDSPfqSaMVSV75WnR4hNgK9RHbY7nKCHbu7tKSSBuvnWpidTmkv1L1olwqjRukBXBAGc3mT4M0kmF8GgUSz_5NhXUlaDDIjHxQ5VbHxnftPlmKKaxvVvt56XuZBEcmqXWgDkna-iuJVthZT_6Rh6kqha4VGF7K5dO8fZ5qQF1yuxsMIb790FiEARWvgrnxy5kkee8QpCEQvIiFkuTEtBKR-Xr8SFGntByl8kpAba0w8Ap7QF4BbFjZQjnm_rSIExIwlVnxL1_fNBt2gcDu2m4H0DnRxaf_OkyeN3jTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
بازگشا سخنگوی پرسپولیس: ما باید تعطیلات فیفادی را با صدرنشینی لیگ شروع می کردیم اما نخواستند که به این شکل شود
💢
پاسخ سازمان لیگ را ندادیم و به جای آن رفتیم به فکر آماده سازی تیم خودمان شدیم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/140011" target="_blank">📅 22:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140010">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b66e5d4924.mp4?token=Flzra5fgcHajV8-yZVMJK8II-zdCer2KgyERGdwZHNkBmgJZTM4TTHIg3FWWB8PFM_0XRdqrwsScoRqN9fDS2YCcje4jxFXWJDrIsSsGrazluT90---F3QNQoaopvIfoCmQhNru_TT-hLUIHCVhwpUiR8JqzHURuwUVz4Nbo5RdSAzhJtC8KT7E8YYpC_sjEPtNEriWkqBSt9zYTKzi56BFxN3ct3UuCGtFDOMCxy3SekOFzkz-4RXd0tGkL0zjRwH8SrTPgjDML4yLiFPEpj70IoJEQ1bY4fOLU0qbNUCOiFb2khuzHQc43IzP124FRorCBrF0tKJc0EsBaj-C8vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b66e5d4924.mp4?token=Flzra5fgcHajV8-yZVMJK8II-zdCer2KgyERGdwZHNkBmgJZTM4TTHIg3FWWB8PFM_0XRdqrwsScoRqN9fDS2YCcje4jxFXWJDrIsSsGrazluT90---F3QNQoaopvIfoCmQhNru_TT-hLUIHCVhwpUiR8JqzHURuwUVz4Nbo5RdSAzhJtC8KT7E8YYpC_sjEPtNEriWkqBSt9zYTKzi56BFxN3ct3UuCGtFDOMCxy3SekOFzkz-4RXd0tGkL0zjRwH8SrTPgjDML4yLiFPEpj70IoJEQ1bY4fOLU0qbNUCOiFb2khuzHQc43IzP124FRorCBrF0tKJc0EsBaj-C8vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
بازگشا سخنگوی پرسپولیس: با احترام به وحید هاشمیان، تعداد مصاحبه های او از تعداد دفعاتی که روی نیمکت پرسپولیس نشسته است بیشتر شده است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/140010" target="_blank">📅 22:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140009">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
نماینده محمد عمری ستاره 25 ساله‌تیم‌پرسپولیس این بازیکن رو الشارجه امارات و لخ‌پوزنان پیشنهاد داده تا درصورت موافقت کادرفنی هرکدوم‌ از این دو تیم با عمری قرارداد امضا کنند. عمری علاقمند به لژیونرشدن در نیم‌فصله.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/140009" target="_blank">📅 21:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140008">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
🔴
مهدی تیکدری (۲۷)، یاسین سلمانی (۵۹ پنالتی)، ابوالفضل زارعی (۷۰) و مجید عیدی (۸۵)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/140008" target="_blank">📅 21:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140007">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
اورونوف در دیدار امروز نمایش قابل قبولی داشت، در این بازی یک پاس گل ارسال کرد و یک بار نیز تیرک دروازه حریف را به لرزه درآورد.
✔️
✔️
این بازیکن در طول دقایق حضور در میدان چند بار با حرکات تکنیکی و نفوذ از جناحین برای پرسپولیس موقعیت خلق کرد و از استاندارد…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/140007" target="_blank">📅 21:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140006">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvC0oXSvDw0mLLx_0MVwQKxHk4s-SyTPh_uqg_O0GJ_YnoBfNA3367WteOKkPDVnvonsW6hTn8GqdZLrCrxv4j4hiCupnSeRS18rvisO-XFNEyALuANYGHyHqJ_AlOmU3c0LOS8a5yA5KZsBhpWUVOD-TouwoyuOHENMeV3NpRD_oebCjL80pHiPDBzgrWA2wA2y97JyTZCnHoeVTkXsfWyyhW4u_3xjGL4zhAQbHasyDOY-Rz3tpFI-D58XsNWtd3La-k76xxWp_dzBXoyBKj5PGYUMvHOMtnjeA79mX6tA4GAl75VPGkQlgCRKb63hodyZzhporJbP_VujdAljlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
برانکو ایوانکوویچ، مربی کروات که اکنون به عنوان مدیر فنی تیم ملی امارات فعالیت می‌کند، با حضور در اردوی تراکتور در دبی، با سید حجت کریمی، مدیرعامل باشگاه، جواد نکونام، سرمربی تیم، و جمعی از بازیکنان دیدار و گفت‌وگو کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/140006" target="_blank">📅 20:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140005">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
✔️
اطلاعیه رسمی قرارگاه جانفدای کشور:
✔️
از سه شنبه 24 شهریور ماه قراره هزار گردان مقاومت ملی تشکیل بدیم که شامل کسایی هست که جانفدا ثبت‌نام کردن.
✔️
قراره به این افراد آموزش نظامی و امدادی بدن تا اگه جنگ شد، فورا اعزام بشن.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/140005" target="_blank">📅 20:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140004">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
✅
اورونوف نمیخواد جدا بشه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140004" target="_blank">📅 20:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140003">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🏅
❤️
فووری از رسانه داریو ازبکستان: باشگاه تراکتور به دنبال جذب اوستون ارونوف وینگر ازبک تیم پرسپولیس در نقل انتقالات نیم فصل است
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140003" target="_blank">📅 20:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140002">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiLxFEFQsDM6vmqXJJtlppXLcu7WpG0XnJQIRowRzWBg_zhdhf2ewYwZF1EBDd7narzuxwbPLFXDaF06aY1bco15JnkROh7k08_VU24M2OjLo2QPR0NE0rgsGx27ZbyvzqI1VSgBVA4kbxCpnU6oWxtNVGesU9ndjm8J6u7-uyGIBgw0X4DhllIv0lySzTdZQJ0u--1ecicI1OTH7QT7x2W-tovtsHzm6jLss8hcbjRL5ZNJYiyJm7hDzOjSYh7xscsJWD92YsZi4guIrnzEpZFNHRl-USku_QecEEDu6Tdu7Jxma23GzHs8HNEQFKm39egB00sf63cQQ1aYTlL-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
جدال نزدیک و نفس‌گیر؛ برست و پاریس برای یک برد ارزشمند امشب به میدان می‌روند!
[
برست
🔴
🆚
🔵
پاری‌سن‌ژرمن
]
⚽️
بازی برای هر دو تیم از نظر امتیازی مهم است و انتظار می‌رود محتاطانه شروع شود. پاریس روی مالکیت و کیفیت هجومی حساب می‌کند، اما برست در انتقال‌ها می‌تواند خطرناک باشد. با توجه به سبک دو تیم، تقابل نزدیک و کم‌فاصله‌ای می‌تواند شکل بگیرد.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
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
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140002" target="_blank">📅 19:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140001">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⚽️
باشگاه پرسپولیس در دیداری دوستانه با نتیجه 4-0 تیم شهید قندی یزد رو شکست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140001" target="_blank">📅 19:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140000">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7Ay1EFRy3zPFIbg0Kae2WnwuVUkMYZRAUkXMtoOe_DsuuoBnrZKRhtJkitj3EGopDJlKgC4i2eEeATqrcgCgbwwNsjVBVsVNxzKFjmcwIzv46bGJlA7x8XvTMskwA8B7fGRpy8n3DXOtP96pu47O4IbSU4aNYJslwwQOSiScfpLh3xfH17iHIZX2_J7DPpb3Um7qzG45_BTqWxZ4e58hPXmjSqJYr0BiCtlerJ3jdmUKxuOcHbfRC5_Lm9y9_5qH4cwxztMs_1QtGgmB8FdT9-9whBkPNXnqvmC8xg2yslQUa0-db6tRvjA3evHI4MqCEYnCFFWOkP8ye5vAiQ8YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
بیرانوند سرباز شد
😂
😂
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140000" target="_blank">📅 18:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139999">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
سردار رادان: بیرانوند شامل قانون سرباز قهرمان نمیشود و از اول مهر سرباز است و باید یکی از تیم‌های ملوان یا فجرسپاسی را برای بازی انتخاب کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/139999" target="_blank">📅 18:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139998">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=rzS611M0to6f0_bzUzNZr8KNSKoWqUvCVmEBx1yrKagDMKL09xGSetgEIayg27XbUusgzAS2MN2bIYiURK_yrc3foGli-8qrt4hY4OrQkt1eww3FVD63J1Z_-ySoL-1ZHG-whviQT4Ym09LY2lf0EyEf0Ktj2m-Kknyd5-9W99oQy9L5six4HkHeBtZ35S7sHOAO4eJtoWjah5Hkjkqh4qEbatnAWuva4B0TBlwO6Vwcv6E8P3G7HrCvgAS256KX7WuyT7I7viRC2j0KKLN-eHk-SlMAeWu4933hgakzsYRmgk4R2Q2pbbUHdTNEFtdvA3Pjbf5ajiLeEK7TNT9OM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=rzS611M0to6f0_bzUzNZr8KNSKoWqUvCVmEBx1yrKagDMKL09xGSetgEIayg27XbUusgzAS2MN2bIYiURK_yrc3foGli-8qrt4hY4OrQkt1eww3FVD63J1Z_-ySoL-1ZHG-whviQT4Ym09LY2lf0EyEf0Ktj2m-Kknyd5-9W99oQy9L5six4HkHeBtZ35S7sHOAO4eJtoWjah5Hkjkqh4qEbatnAWuva4B0TBlwO6Vwcv6E8P3G7HrCvgAS256KX7WuyT7I7viRC2j0KKLN-eHk-SlMAeWu4933hgakzsYRmgk4R2Q2pbbUHdTNEFtdvA3Pjbf5ajiLeEK7TNT9OM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سردار رادان: بیرانوند شامل قانون سرباز قهرمان نمیشود و از اول مهر سرباز است و باید یکی از تیم‌های ملوان یا فجرسپاسی را برای بازی انتخاب کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/139998" target="_blank">📅 18:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139997">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⚽️
باشگاه پرسپولیس در دیداری دوستانه با نتیجه 4-0 تیم شهید قندی یزد رو شکست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/139997" target="_blank">📅 18:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139996">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
✔️
اطلاعیه رسمی قرارگاه جانفدای کشور:
✔️
از سه شنبه 24 شهریور ماه قراره هزار گردان مقاومت ملی تشکیل بدیم که شامل کسایی هست که جانفدا ثبت‌نام کردن.
✔️
قراره به این افراد آموزش نظامی و امدادی بدن تا اگه جنگ شد، فورا اعزام بشن.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/139996" target="_blank">📅 18:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139995">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
تو 24 ساعت اخیر سرچ «لغو عضویت جانفدا» بیش از 5 هزار درصد افزایش داشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139995" target="_blank">📅 18:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139994">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEuNiuf0hmzUHTEioq2phNcG1n_etIeux5RcihFGwLMJTiJM1ZCNaui8c4J7ZlsfgCOvmAo5eYE_guAe906rVlCK3iMlT1SyKsGUCYyt_9_qYHa6FESwQLMRxXCpRMmRvrwuIP-l5TDIZjLEcrAd00amMKYPWMn97nbSvunJk3spzXWY88MEjZDhNvquD5YjVeAQiyGMaX6AzgNmzLFyWGDUYrjcz-pRvZvD6kHqXiMOb5pxNumQYjHP_5FIURfQbxS-ON1uiT7IUhLhmO0NDeZLnfrFNi01Fl9vwqao1fHRHRkaKFrzUr6E4gaZ9UPJyHHCkjP1qSkb_WekPl2xbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
باشگاه پرسپولیس در دیداری دوستانه با نتیجه 4-0 تیم شهید قندی یزد رو شکست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/139994" target="_blank">📅 18:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139993">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🗣
#یادآوری
✔️
✔️
هتریک بیفوما مقابل بارسا‌، گل‌هاش یکی‌از یکی قشنگ‌تره و خلاقیتش رو به‌رخ میکشه
✔️
✔️
وقتی تو سن ٣۴ سالگی جلو ملوان استارت شصت‌متری میزنه یا اون پاس‌گل جلو اس‌خوزستان میده از سر فوتبال‌ بلدیشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/139993" target="_blank">📅 16:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139992">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
حضور هانی نوروزی پسر زنده یاد هادی نوروزی، کاپیتان فقید پرسپولیس در تمرین تیم دهه شصت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/139992" target="_blank">📅 16:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139991">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
فارس: محسن نامجو با هماهنگی به ایران برگشت، احتمالا شادمهر عقیلی هم به کشور برمیگرده و حتی کنسرت هم میذاره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139991" target="_blank">📅 16:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139990">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
از داخل ایران مدارکی به باشگاه السد ارسال شده که در صورت بازی کردن یاسر آسانی، ازش شکایت بشه
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139990" target="_blank">📅 16:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139989">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
دو ست و فعلا باختیم و واقعا زورمون به ژاپن نمی‌رسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/139989" target="_blank">📅 15:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139988">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
میثاقی:
✔️
مهرداد محمدی یه چیزی گفت شش ماه محروم شد اما خداداد چهار ماه؛ ساکت الهامی هم شش ماه محروم شد!
✔️
یکی از دوستان حقوقی گفت شکایت قضایی این موضوع چهار ماه زندان دارد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139988" target="_blank">📅 15:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139987">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReGAhBTQNn_z6_8EdeACji5S_91rGAWHEPh7W4MM4xCA-ZNucJs9v50QWfLjraveq8oLRvyffsLNa1lQh3tAQ1AvznfVxv6edcd8wuVIaxYcFbxJg5Drxn1MybsSTh5fY4tZ0Ca9yE-lxGam3UkDXvTjnhmCmsnwmlstBqvtjoLwVBn1DCPbfN46IhuoE4ZeYpfBNctHGaWgWOw0WgfzAYgIHzlgHHrASd-QFb0gvOm45ZfkCMtJu6jShkzJnw7gQZo972UqvLihV2VuOvC5xcNW84OebabhOtYtqmip1TNa5AbLz7lnWH8vhDLazEwGTYhCMYFhY4klAczhaWo25g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
پس از آنکه محسن خلیلی در ابتدا اعلام کرد: «جام حذفی برگزار نشود بهتر است»، حالا پیمان حدادی برای چندمین بار خواهان برگزاری این مسابقات شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139987" target="_blank">📅 15:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139986">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
ژاپن 3-0 کره جنوبی
❌
ایران و ژاپن فردا ساعت 14 برای کسب عنوان قهرمانی و سهمیه المپیک به مصاف هم میرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139986" target="_blank">📅 15:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139985">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
♨️
🆔
| ورزش‌سه:
🔴
❤️
با ادامه‌ی روند فعلی مارکو باکیچ از پرسپولیس جدا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139985" target="_blank">📅 14:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139984">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
❌
تیکدری: روز اولی که به پرسپولیس اومدم گفتم با تمام توان در هر پستی بازی میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139984" target="_blank">📅 14:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139983">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vflX3LcEuHTJXOBqMkFrZSf7NWi0NOSUiix8gFoGMoe4DnE8AIY6c1hzKFvl34F3LNRPchhMg4laA4_yneo0l5Ew8x-QXzdSPL3jclqxghmZJwRRN4XDMPIJ9_hbLf9SU6w3rXlPSlTiNknPtRdAkNr03-LJZ_LoyWaf8M0hQoVrC8YN6SWCc4R3hMLqh1b_k_ijCQGFCRiB5dS0GIzLY7l2W7uoXP-2bE8cHi5tlQmWWrSY_cN48tncOyHyanhQxDATXudLVlE1PbmMwrRNzNx4Q5EyRfvoPB1cKNQdEmVha8OsN7kvtqwa67ZdTqRHpTENP1GuZxK3No5c0N9l8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Man United -
🔵
Man City
⏰
Tonight 19:00
🏟
Old Trafford
🟣
منچستریونایتد در اولدترافورد با تکیه بر انرژی هواداران و ضدحملات می‌تواند سیتی را به دردسر بیندازد، اما ضعف دفاعی‌اش نگرانی اصلی است.
سیتی با شروع قدرتمند فصل و خط حمله آماده، کنترل میانه میدان و فشار روی دفاع یونایتد را هدف می‌گیرد؛ دیداری که پتانسیل گل‌دار شدن دارد.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139983" target="_blank">📅 12:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139982">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔥
⚽️
رکورد جالب پوریا شهرآبادی؛ شروعی درخشان در پرسپولیس!
🔴
پوریا شهرآبادی در حالی که تنها ۲۰ سال سن داره، تبدیل شده به دومین گلزن جوان تاریخ باشگاه که در کمترین زمان ممکن به ۲ گل می‌رسد.یعنی شهرآبادی برای زدن ۲ گل، حتی به اندازه‌ی دو بازی کامل هم در زمین نبوده…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139982" target="_blank">📅 12:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139981">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">💢
💢
بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139981" target="_blank">📅 11:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139980">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
ساپینتو : من و کلارنسس سیدورف مخالف ۱۰۰ درصدی جذب جنپو بودیم ، ولی تاجرنیا اصرار به جذبش داشت بعدا متوجه شدیم بازیکن و ایجنتش ارتباط نزدیکی با تاجرنیا دارن...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139980" target="_blank">📅 11:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139979">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb6f48f178.mp4?token=ZSNJnr6-vvLAFImP1igZ1No1wYTPV4ePDw-SwyV2qd9-9I1bgS49hgjz_dMcfOqNYur-Hcc0s_eRySJQbdWlonOfXlhMax_rvr2pS8Wa3bbmpnHvmZqwgYfZM12tQJt2vkfOA7WxIn9LmnhhoSqwyoCVNb9tYn7-7yvwCnWs_KtL5AFG86qmAELreeaAwOgwqQTTIGc-O0WgyG9EpgsqkFtn9UoPEwl0iAJYK1Bf-vA8Z51N9b-xXTLP6BR_PtxcU8LU3Ldptq2pXk6c8pE6DietDfpzxgC-pFpPy3f0oLHSeXILZrzBKO3Fgk-GoHdjUF9x5K-WlkUAsEzwO3Ak7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb6f48f178.mp4?token=ZSNJnr6-vvLAFImP1igZ1No1wYTPV4ePDw-SwyV2qd9-9I1bgS49hgjz_dMcfOqNYur-Hcc0s_eRySJQbdWlonOfXlhMax_rvr2pS8Wa3bbmpnHvmZqwgYfZM12tQJt2vkfOA7WxIn9LmnhhoSqwyoCVNb9tYn7-7yvwCnWs_KtL5AFG86qmAELreeaAwOgwqQTTIGc-O0WgyG9EpgsqkFtn9UoPEwl0iAJYK1Bf-vA8Z51N9b-xXTLP6BR_PtxcU8LU3Ldptq2pXk6c8pE6DietDfpzxgC-pFpPy3f0oLHSeXILZrzBKO3Fgk-GoHdjUF9x5K-WlkUAsEzwO3Ak7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣
#یادآوری
✔️
✔️
هتریک بیفوما مقابل بارسا‌، گل‌هاش یکی‌از یکی قشنگ‌تره و خلاقیتش رو به‌رخ میکشه
✔️
✔️
وقتی تو سن ٣۴ سالگی جلو ملوان استارت شصت‌متری میزنه یا اون پاس‌گل جلو اس‌خوزستان میده از سر فوتبال‌ بلدیشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139979" target="_blank">📅 10:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139978">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjBixYe46G6cJClE3w5q8gLUQ8Z5gwdFGLLAk3wQfguzxU032oxWOHaugVQL-YN8tdYYwhQRmAKRoFthFNFDWGGVgAXfL-hSaGOjWLoWAOD2tw9GCtJH4_gPgb799M70DloV_K13LD61nwnKo18dnEOoPMTs8Je1heaAYwF02sVM_AFI7GrX8osMgvN8QZu4lCSmWpqeelebLi-qaumxqTrC2JkKYOkbiLSKrnIJJKDrGUAZTLLWBYXewiotSZuCTNR6ae5kkQZWz12E51ClAP_VN5XhjwwbQNnBnIq2ehJ5iHJRtekjRsKL_6Yw6OJdDBmt0QAn55Zjyv9YlRWv6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
کاروان تیم فوتبال گل گهر امروز برای اولین بازی خود در لیگ قهرمانان آسیا مقابل الجزیره امارات راهی تاجیکستان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/139978" target="_blank">📅 10:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139977">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOV-t3EF0DItCIOmCSHGSVETKfIKo79WESQKPQbTx0X51w2c-WT0rwCSZN6RTEjm6p8XhNHbwjcgM4GLwD9ghs89Uet1krmB9_24z8FfFd6xXaCGytqI4-gomAbMJx4K2oWsg2WU1b_lTFy0qybSEqDWg9OvKYEI_6zbmFfgXu0Kd2F3B_wksZELs-PEUi8lWFyto56bIecjo5no09IPdul4q9d_ETos-hc_RPwRYOn2uKShVW5BZq1k7BWis-gA79qq5VSY-btOFgUJjXd7GIeDJH3HSbyDqd3chJzwbf2pLqGTk9OOR_XRNuILbnxEmI6QkynG5xomAPHg9lPyNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پرسپولیس امروز عصر در دیداری تدارکاتی به مصاف تیم شهید قندی یزد می‌رود. این دیدار در زمین شماره ۳ آزادی و پشت درهای بسته برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/139977" target="_blank">📅 10:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139976">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🗣
🗣
🗣
🗣
🗣
🗣
حمید درخشان: هیچ‌کس در باشگاه پرسپولیس دوست نداشت موفقیت من را ببیند. همین‌جا در خبرورزشی با صراحت می‌گویم چند بازیکن آن زمان پرسپولیس کم‌فروشی کردند تا تیم نتیجه نگیرد و با حمید درخشان موفق نشود.
✔️
✔️
امیدوارم این بازیکنان حالا پس از گذشت ۱۲ سال جواب…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/139976" target="_blank">📅 10:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139975">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">💢
درخشان: بازیکنان پرسپولیس هنوز به هماهنگی کامل نرسیده اند. قطعا پرسپولیس در ادامه لیگ بهتر می شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/139975" target="_blank">📅 10:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139974">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1ZAesrmrudAwmz9j1yhirD5OyjwSln7uNllwS2RinnbtwL9_b7z0xc6FIAwun9y4iNSOiSLTMmIRU9mpKPn5Puaw1tsuMPHfNrU6YataIn3t9M-k395I1RO7E1FY0ttfjaNnEwN8ydgsbu9Ee_aja8TVgmOaA1f1VVolos52QcQHgl-M-bJCrRb-Y3RY_XFG1DkSoNw92DBX06mjQzrSEa-VsrHpX6Sg6TQOafHEkUV-xYWe_rskxalCBtHopG87MKeLHNbQgA78OH_2NozLEH7h05Bw0jWi0CbO4xwZ8qSSAcQs1UxjdNnLM_WYYyG_jwIdx10fHpxXCD59PdX1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗣
🔴
❤️
پیمان حدادی:
🔻
بازی با خیبر را لغو کردند تا یک‌ماه دیگر به صدر نرسیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139974" target="_blank">📅 08:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139973">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBydcO5-3xC_Nt1ErDcYJouPSjo1E-bkoTWNxpAwoB_9BcQkBmcmHE94CGnrJtczBNpssktzf8zmOTXljwhEhIKJHr9M1WftDDtj-sgYCnK1Hf6tlUmlI3ZO2PrZhh61rxUYOzEpDJCgUkuaRat6uwM5wDn1yyzNqvQRI-HiU80KJqVm-JnEvHqwwkDty2leAXxpbHD8ImToc-ET-QWn1xruackBFtphapdoPMpph-Cd5-rD3ODKtF99KxMBsURVnRmXu_M_TKaJzf7OFzZ9_360oxZgM916ZXoR8isS2NqDgTuFUhAbUlvNEMuMPgi7ApS5TWyuzhDc_InZ_W6N9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/139973" target="_blank">📅 08:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139972">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
می‌خوای پیش‌بینی کنی، ولی نمی‌دونی چطور حسابت رو شارژ کنی؟
وینکوبت کار رو برات ساده کرده!
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🎁
بونوس ویژه اولین شارژ:
فقط با یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و به موجودی اصلی حسابت اضافه کنی.
🟣
آدرس سایت وینکوبت:
wincobet.com
🔗
همین حالا وارد مینی‌اپ وینکوبت شو و اولین شارژت رو انجام بده:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139972" target="_blank">📅 01:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139971">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b9033e7e.mp4?token=H6dmzAup1Mfx2wS2K3l602p3fo4TBSQqPeAB5lXTNxQfKBK8Erb2pqCSIQQBw30gDkqMaDUqt3OiAWdVh-NbHCK0D0uKESbeqMsx59xsVeQIG5bsNRjOHvQlMPkOUrj6pM786lI7WkrhARhFK8dTizpPhd6_xoVjO3WKB-Jkv4FuPfNYkL3rzzokZ1lmCqgUtYk1uAP7DBg7xB3vGxG_3GJAsDPBUCNga4Z2KzAtC5bBb-PIXRpofOFL27CyoyojtWyDodqObG3k7K1TVNQ_ebeOYK4qVQtkD9qrnAgCgH3BsD5lq-7tu0eRaRHFxyR0XqE_mOnDs6PRJVmV37QOVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b9033e7e.mp4?token=H6dmzAup1Mfx2wS2K3l602p3fo4TBSQqPeAB5lXTNxQfKBK8Erb2pqCSIQQBw30gDkqMaDUqt3OiAWdVh-NbHCK0D0uKESbeqMsx59xsVeQIG5bsNRjOHvQlMPkOUrj6pM786lI7WkrhARhFK8dTizpPhd6_xoVjO3WKB-Jkv4FuPfNYkL3rzzokZ1lmCqgUtYk1uAP7DBg7xB3vGxG_3GJAsDPBUCNga4Z2KzAtC5bBb-PIXRpofOFL27CyoyojtWyDodqObG3k7K1TVNQ_ebeOYK4qVQtkD9qrnAgCgH3BsD5lq-7tu0eRaRHFxyR0XqE_mOnDs6PRJVmV37QOVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔴
آرش فرزین: پرسپولیس خسته را پدرم به عشق پروین خواند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139971" target="_blank">📅 00:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139970">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✔️
✔️
‌ ۵-۶ بازیکن از پرسپولیس در فیفادی جاری به تیم ملی دعوت میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139970" target="_blank">📅 00:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139969">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
تعطیلی ۲۵ روزۀ لیگ برتر
🗣
🗣
لیگ برتر حدود ۲۵ روز تعطیل خواهد بود. بخشی از این تعطیلی نسبتاً طولانی به دلیل همکاری باشگاه‌ها با تیم ملی امید است و بخش دیگر نیز مربوط به روزهای فیفاست که از ۳۰ شهریور تا ۱۴ مهر است.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139969" target="_blank">📅 00:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139968">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
🔴
پرسپولیس موفق شد امتیاز تیم دسته اولی فولاد نوین رو بخره و تبدیل به پرسپولیس ب خواهد کرد و سید جلال حسینی هدایت این تیمدرا برعهده خواهد گرفت/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139968" target="_blank">📅 00:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139967">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
✔️
درخشش بشار رسن در ازبکستان ادامه دارد؛ هتریک پاس گل این بازیکن در دیدار روز گذشته تیمش که با برتری 3 بر صفر پاختاکور همراه شد
✅
✅
آمار او در این فصل : 25 بازی، 4 گل، 9 پاس گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139967" target="_blank">📅 23:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139966">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
ساپینتو : من و کلارنسس سیدورف مخالف ۱۰۰ درصدی جذب جنپو بودیم ، ولی تاجرنیا اصرار به جذبش داشت بعدا متوجه شدیم بازیکن و ایجنتش ارتباط نزدیکی با تاجرنیا دارن...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139966" target="_blank">📅 23:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139965">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❤️
پیمان حدادی: وقتی لیگ تموم شد و به همه جا اعلام کردن نیمه تمام هست، هیچ جای دنیا پس به تیمی جام نمیدن و خیلی غیر منطقی هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139965" target="_blank">📅 23:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139964">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
ریکاردو ساپینتو؛سرمربی سابق استقلال:
🔻
من با مدیران زیادی کار کرده‌ام اما تابه‌حال مدیری به شهرت‌طلبی و دروغ‌گویی علی تاجرنیا ندیده‌ام.
✔️
✔️
از روز اول تاجرنیا به رابطه من و مدیرعامل وقت آقای نظری جویباری حسادت می‌کرد و انتظار داشت من مسائل تیم را با او…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139964" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139963">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
✔️
✔️
منهای ورزش :همراه اول تو جدیدترین شاهکارش، سقف مصرف بسته اینترنت ۷ روزه «نامحدود» شبانه رو از ۱۰۰ گیگ رسونده به ۲۰ گیگ!
✔️
اینترنت نامحدود تو ایران = ۲۰ گیگابایت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139963" target="_blank">📅 23:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139962">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
✔️
ساپینتو: پیشنهاد عجیب تاجرنیا برای استقلال!
✔️
✔️
ساپینتو مدعی شد تاجرنیا به او گفته قرار است سعید فتاحی به استقلال اضافه شود تا با توجه به ارتباطاتش با داوران، مدیران سازمان لیگ و فدراسیون، مشکلات داوری و برنامه‌ریزی مسابقات را به نفع استقلال حل کند و…</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139962" target="_blank">📅 23:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139961">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❤️
پیمان حدادی: خیلی ها آرزوی قهرمانی دارن اما پرسپولیس در ۸-۹ سال اخیر ۶-۷ جام گرفته. بازی ما رو لغو کردن تا صدرنشینی ما یک ماه عقب بیفته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139961" target="_blank">📅 23:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139960">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❤️
حدادی: هاشمیان قبل و بعد از پرسپولیس کجا مربیگری کرده است؟ دوستان در یک سال، سه بار او را دعوت کرده‌اند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139960" target="_blank">📅 23:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139959">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
دکتر حقیقت: محمد عمری تا ۳ هفته‌ی دیگر به تمرینات برمی‌گردد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139959" target="_blank">📅 23:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139958">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
از داخل ایران مدارکی به باشگاه السد ارسال شده که در صورت بازی کردن یاسر آسانی، ازش شکایت بشه
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139958" target="_blank">📅 22:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139956">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✔️
ژاپن 3-0 کره جنوبی
❌
ایران و ژاپن فردا ساعت 14 برای کسب عنوان قهرمانی و سهمیه المپیک به مصاف هم میرن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/139956" target="_blank">📅 21:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139955">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JA0mwGFwEccM1TnhsTl6yM1L6XwwPZlr8o9syXSgld4Z4Sq9njtGmOrK4MuXzQLOODYW7eLBPtH46rMCHtj5w-osWaFmDsjaTECVFAo2NwHIWv-4EOTw6EdDh7ac8GDC6zGW-fdQdcJpbrRdHUp9HT5c3TIGlk_o6_8Q_HkhfZX07oPlGIH9Ki86lKvkMdMVAzZMitSCejHZloa6weutjx-2wBAAbIFH_B9ku57xfWeVYgk_32O2xjL6iMkhpOxvjWkwBLW7G4Xu7dTToRESxSCO0LP06JeBrlGCkS9W1xXFTb6Q8LTRMqiXLwWTx2D5Djl8U0NuUADiImqCjYeQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تصاویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139955" target="_blank">📅 21:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139954">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6060af132f.mp4?token=qlDXh3syTiHEwAg2iKQ7kNWY4RBdh1xZMDILOUxjmzXnT-6L6zZF8Djc0UHRKfalXm3_rZ-9aWewPz1cKLGw_xcN-r6KqTAUwhJCoyvqtWfVREsVcC9Ts5zoNNmJKKxrM2_bpZiIi1MpupZ6Q-FJXcR-Rs9xwO9THhM2ZEgIIhuciQvqo15eJwW48MTMCkYD9jrSf9uGqgZ52oInJzhFoBxug1ubVkkogDXSuAsIy2OBXz0KINVjJg97PnsrINLMCyZdZqHJH2yJJvIEHyeN0g6uqzYC_92tGbo7a-8Nut5ti6xtyYdFoMkRI-qQKYoTO3k7fHjbTHmgUpao-nbnKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6060af132f.mp4?token=qlDXh3syTiHEwAg2iKQ7kNWY4RBdh1xZMDILOUxjmzXnT-6L6zZF8Djc0UHRKfalXm3_rZ-9aWewPz1cKLGw_xcN-r6KqTAUwhJCoyvqtWfVREsVcC9Ts5zoNNmJKKxrM2_bpZiIi1MpupZ6Q-FJXcR-Rs9xwO9THhM2ZEgIIhuciQvqo15eJwW48MTMCkYD9jrSf9uGqgZ52oInJzhFoBxug1ubVkkogDXSuAsIy2OBXz0KINVjJg97PnsrINLMCyZdZqHJH2yJJvIEHyeN0g6uqzYC_92tGbo7a-8Nut5ti6xtyYdFoMkRI-qQKYoTO3k7fHjbTHmgUpao-nbnKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
صحبت های وحید هاشمیان علیه پیمان حدادی:  حداقل درویش از مدیریت الان مرام بیشتری داشت و به نظرم برکنار شد چون من را برکنار نکرد. چطور برای اوسمار این چنین مراسم بدرقه ای انجام دادید ولی با من این گونه برخورد شد؟  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139954" target="_blank">📅 21:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139953">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
السد در 4 بازی اخیرش 19 گل زده
🔥
پ.ن یعنی دوباره قراره عروس بشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139953" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139952">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ee53113a6.mp4?token=EvAGM4i3oXiWnavZxvKYligg0tC_Jp34A33Lv4YJbg9Tt_uxJmw2oSquJgcnr0UAidvCOvhk2Z_bLDY8pAEt90WbwZXU2fZriHGYoUZKnvVuUczgkxOinK06v0eQePlxihJALtINGvSdSWk8i-VsiaUNvvGpYwvLnCYqOk89Mkw38pohxMRdLDgXCbGWruAm-cmjyBDSCbzOR3BFIdROQWoGAd4_3EFB8ytcuvZnamvg7pXyOVu4rhLJIyCOTOVGYxFx5zy7mY6Kg188Bz3ZJhUU01uteLDIW57GKQ-USq_u2bVEgmYNNb_PRGdLNnXix2mWC4rVeVRGyQ_aZEO3GG8phxSydgj28SBM05Lny6Lurpw_mOuTnmciXQTNa9zoVYgsTjWzgz8hGu52UdujSZkOJHG4hWDVaLQTTwSlg1v4_9TPaTX3sVvqgfOC5is51P1hJv7_0DxPZDprTlJmQQb68nZSwCQF_BYtaNR9rX3MLIVIIb38eYeubBvY2i7TpF7GFeQzNjvQpKQUePemswqLDFrjO7JjK4YFeRqK5CVr0Fdz-oTgyv660AaCQE38FpdM4fDpJM6Hm2ShMUmantrOp14H1L0HvchfmcWpN2LTHeyqOb5XLxS2L2OczEfoxi6Y56Cy9Y7asbHWNn-ECRyxB_kTZF9lTeqXAe-n4Gc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ee53113a6.mp4?token=EvAGM4i3oXiWnavZxvKYligg0tC_Jp34A33Lv4YJbg9Tt_uxJmw2oSquJgcnr0UAidvCOvhk2Z_bLDY8pAEt90WbwZXU2fZriHGYoUZKnvVuUczgkxOinK06v0eQePlxihJALtINGvSdSWk8i-VsiaUNvvGpYwvLnCYqOk89Mkw38pohxMRdLDgXCbGWruAm-cmjyBDSCbzOR3BFIdROQWoGAd4_3EFB8ytcuvZnamvg7pXyOVu4rhLJIyCOTOVGYxFx5zy7mY6Kg188Bz3ZJhUU01uteLDIW57GKQ-USq_u2bVEgmYNNb_PRGdLNnXix2mWC4rVeVRGyQ_aZEO3GG8phxSydgj28SBM05Lny6Lurpw_mOuTnmciXQTNa9zoVYgsTjWzgz8hGu52UdujSZkOJHG4hWDVaLQTTwSlg1v4_9TPaTX3sVvqgfOC5is51P1hJv7_0DxPZDprTlJmQQb68nZSwCQF_BYtaNR9rX3MLIVIIb38eYeubBvY2i7TpF7GFeQzNjvQpKQUePemswqLDFrjO7JjK4YFeRqK5CVr0Fdz-oTgyv660AaCQE38FpdM4fDpJM6Hm2ShMUmantrOp14H1L0HvchfmcWpN2LTHeyqOb5XLxS2L2OczEfoxi6Y56Cy9Y7asbHWNn-ECRyxB_kTZF9lTeqXAe-n4Gc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی: بازی خیبر را عمدا به تعویق انداختند تا روند پرسپولیس را متوقف کنند!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/139952" target="_blank">📅 21:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139951">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❤️
❤️
حدادی در بین هواداران، بعد از بازی با ذوب آهن.
✔️
هوادار:
❌
دمت گرم با این تیمی که بستی، تا آخرش همینجوری وایسا.نیم فصل دو تا ضعف رو برطرف کن، بخدا تا آخر فصل ازت حمایت میکنیم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139951" target="_blank">📅 21:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139950">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
از داخل ایران مدارکی به باشگاه السد ارسال شده که در صورت بازی کردن یاسر آسانی، ازش شکایت بشه
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/139950" target="_blank">📅 20:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139949">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
پرسپولیس فردا به حای بازی لغو شده با خیبر احتمالا تو یه دیدار دوستانه به مصاف تیم شهید قندی یزد میره و بعد از اون تمرینات مدتی کنسل و بازیکنان به استراحت میرن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/139949" target="_blank">📅 20:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139948">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cO1InXnuw5Jy9ZxwD8SljBcDmonsPIqgl023IK3OyQiKLjEz3qnzbmYhuxylAUpie7W5nrO0ykRfowTKe-dM5ukgdOeCuu4jbtsTdT7EDYOq3jB7tAPYqaRPj0WKGzVmvvm1WZWGl_PdvCN0RRhlUevrCGd4RfGUbwkQcCpfZW_1KTi_jFkJ9NscA6bpsmd-cv7Ux9OeDZjBvZUTcnV18A-DqXc3uvY7ZxdC0NkT3XbeIPbPw6eB_PbaJkdB-Z_BdbvL9PhhArgNzF5_plCTenHnDzgga2KjJmEqryDLFD_qKeyVcPRmf7Az0Ki9uUIweCa8OEXSm_5iDypP5A84sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیس فردا به حای بازی لغو شده با خیبر احتمالا تو یه دیدار دوستانه به مصاف تیم شهید قندی یزد میره و بعد از اون تمرینات مدتی کنسل و بازیکنان به استراحت میرن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/139948" target="_blank">📅 20:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139947">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mppev_BnMvsCMuCEhFBbzMcRPo157ue9dz4hzYIU6KlHLr0FQvV0vmCQAaGbSOTDogfYSMvZxg9HmT_hIpAk9JK5Jy4xvEskqvN00BqUDfDaTA2Pn6cPX7NDeU2weLKMP4sY8wH51Se_1LjwxZhhGwdvQdMsg4WvXJb3-2b3TkYROvXPZLSkbUpQiMqZSGN_dKieFOCawLl06E8lbvunEsM_m4oe5vEz3CAUlCwfs4arMMrZT7YcdOrxn5N3wpT1zVWSugnhRhPy8A-X6xM1DrE3B0oqaP9zVHDgx5wFd5RhYaBthWr_8MVmEAHRixnIwiITVtE4vjF8BQ9S4jeNhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
Real Madrid -
⚪️
Rayo Vallecano
⏰
Tonight 22:30
🏟
Estadio Bernabèu
🟠
رئال با برتری کیفیت فردی و مالکیت توپ، از همان ابتدا برای کنترل بازی جلو می‌آید.
رایو وایکانو احتمالاً با دفاع فشرده و ضدحملات سریع، سعی می‌کند ریتم رئال را برهم بزند.
کلید بازی برای رئال، باز کردن لایه‌های دفاعی رایو و استفاده از فضاهای کناری خواهد بود.
با توجه به اختلاف کیفیت دو تیم، کفه ترازو به سود رئال مادرید است و شانس بردش بالاتر به نظر می‌رسد.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139947" target="_blank">📅 20:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139946">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✔️
✔️
فوری؛ در آستانه بازی استقلال و السد در بصره عراق، به دستور نخست‌وزیر عراق، تمام مرزهای عراق با ایران بسته شد و پروازها نیز به حالت تعلیق درآمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139946" target="_blank">📅 18:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139945">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a080739df.mp4?token=DaOv1hzYFR4PXkngk0-sdgmHjGwMNcsD9WOwFC_pjcK1C_HGxk1Xp9qthciI0C8HBni51wjIf8n9njw6hvW0suRfKqMoRW8QAadMp0B8gDEdSzOgVCJGXBnrywwj_qoiLL0ySzXD6jvtgZZ6_lWDLvno6TMxiafXXoxYiOIlxwqnVYjOOSDWlcPy7Vz-gwl6gx_xfMwohsJ8fvxR2ljCTLIeuMqZoOGrsWEyCvf3t7exUIu6SlPD2p3-NMUdHo6rR0fcChffBELgUS0PfMPAwaS7FZIPhTn-YkGdbBPxvm-9bslppzIfH0v729FzV2JsXgYFtLEX_-fd0K0NqxI7ZqzoznQPZ3tMXzLAjltDBT-9cKocAeV-wD5q5fsQUuv0_gh0rGIyZPDg33GCI44ZywjWpzz7NEzHMksmCQlIfxxbhV7N_LoW6j0UhIlqq1toErZGLMQ51mBS_1kNNphNpANkXP_twwILrfW_SJCG6DCX3NIX4mK_oPFesBSaoPQhPsWtVzKKqh3aUo_tmUXokTYQJyetlFdkt4x4P4QTVHntDHlAaWih8z5it0LaQGciEZD97RJQF-Jp_TpHAsuw_mSzrUevz9WTPi1jxc_h17o4IiOfh1ZI29dF4__qe3IcncKiZf6cRc2xjDLH2EkZww_52TtPeUfpvMKvT727lqs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a080739df.mp4?token=DaOv1hzYFR4PXkngk0-sdgmHjGwMNcsD9WOwFC_pjcK1C_HGxk1Xp9qthciI0C8HBni51wjIf8n9njw6hvW0suRfKqMoRW8QAadMp0B8gDEdSzOgVCJGXBnrywwj_qoiLL0ySzXD6jvtgZZ6_lWDLvno6TMxiafXXoxYiOIlxwqnVYjOOSDWlcPy7Vz-gwl6gx_xfMwohsJ8fvxR2ljCTLIeuMqZoOGrsWEyCvf3t7exUIu6SlPD2p3-NMUdHo6rR0fcChffBELgUS0PfMPAwaS7FZIPhTn-YkGdbBPxvm-9bslppzIfH0v729FzV2JsXgYFtLEX_-fd0K0NqxI7ZqzoznQPZ3tMXzLAjltDBT-9cKocAeV-wD5q5fsQUuv0_gh0rGIyZPDg33GCI44ZywjWpzz7NEzHMksmCQlIfxxbhV7N_LoW6j0UhIlqq1toErZGLMQ51mBS_1kNNphNpANkXP_twwILrfW_SJCG6DCX3NIX4mK_oPFesBSaoPQhPsWtVzKKqh3aUo_tmUXokTYQJyetlFdkt4x4P4QTVHntDHlAaWih8z5it0LaQGciEZD97RJQF-Jp_TpHAsuw_mSzrUevz9WTPi1jxc_h17o4IiOfh1ZI29dF4__qe3IcncKiZf6cRc2xjDLH2EkZww_52TtPeUfpvMKvT727lqs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔴
آرش فرزین: پرسپولیس خسته را پدرم به عشق پروین خواند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139945" target="_blank">📅 18:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139944">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
✔️
با توجه به لغو بازی با خیبر، پرسپولیس فردا در دیداری دوستانه به مصاف تیم شهید قندی یزد خواهد رفت.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139944" target="_blank">📅 17:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139943">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
✅
تصمیم تارتار درباره تمرینات پرسپولیس
⏺
با وجود لغو مسابقه پرسپولیس و خیبر، تمرینات پرسپولیس طبق برنامه امروز برگزار خواهد شد و سرخپوشان پایتخت یک جلسه تمرینی دیگر را پشت سر می‌گذارند.
⏺
مهدی تارتار، سرمربی پرسپولیس، قصد دارد از فرصت به‌وجود آمده برای…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139943" target="_blank">📅 17:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139942">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🆔
| ورزش‌سه:
🔴
🔄
پرسپولیس امروز هم تمرین می‌کند و روز یکشنبه نیز در دیداری تدارکاتی حاضر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139942" target="_blank">📅 17:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139941">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
✔️
✔️
علیرضا بیرانوند دروازبان تیم تراکتور، دو دیدار آغازین مقابل شباب الاهلی امارات و الغرافه قطر را به دلیل محرومیت غایب خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139941" target="_blank">📅 17:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139940">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ml7-Ou52PlGDtJb2f7zvP5khtR0gMZLGZkA9-mohT5i6BmQG6w3-HCDib1kzOYXD9sOQD0G-LQSL68oyH2FUJUqbCTqnTsmokyS0cK-VMjuMW1fABQ3FC7d8XUlMw4uirX_RtHeFbv7UyM60Ypg1gTK8PhmhwNO7iGBLPqgRHbgtIORI0WWO11O8AzTKOKLH-AUPkmUDCKsaD9u5qrRWnnKGhLYRCwHX6_mGBZY9En6Si122GBkmoKqUwBkFo5M5pZj-LT3QiHuyK3OqYBojfQR47xxXyEFr_7RORD0J3CTni0JSCwOQg26AfnjX1Cxqgu9pZYZO4gFifMwBy3f48Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
میلان در آزمون لاتزیو؛ جدالی نزدیک و تماشایی
⚽️
میلان با تکیه بر کیفیت هجومی و امتیاز میزبانی، دست بالاتری روی کاغذ دارد. لاتزیو اما با ساختار دفاعی و ضدحملاتش می‌تواند بازی را برای روسونری سخت کند. انتظار دیداری نزدیک می‌رود؛ جایی که جزئیات می‌تواند سرنوشت بازی را تعیین کند.
[
آث‌میلان
🔴
🆚
⚪️
لاتزیو
]
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه دریافت کنید.
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
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139940" target="_blank">📅 16:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139939">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
✔️
فوری؛ در آستانه بازی استقلال و السد در بصره عراق، به دستور نخست‌وزیر عراق، تمام مرزهای عراق با ایران بسته شد و پروازها نیز به حالت تعلیق درآمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139939" target="_blank">📅 16:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139938">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">💢
ویدئو باشگاه پرسپولیس برای گئورگی گولسیانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139938" target="_blank">📅 16:06 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139937">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPa9HiFUqqNOX83eCfoHtXPBOPBuG6oJ7vc8YVj8fp4mHbqCP4zTeWxEg2CGJSXorhqYcs5iWb5EBKhNqw9q5wG2ZSVNF07zCyuvowmIsZ-LxtLYSt-KYxxrUTESysTjRP62Z5v_CNkeUS-0_VkhfySCekehXwA04Kq-CLtaRfDyKlDz9konvBp3QFLcHTUqztXQII02pw5LjRKU2F-OzlTTZKb9gjObYrusy5Ay0T6nX0r570LjE9EZ3nQub0knIWOl9I9cf-4M0tllYofJXGMT2YF0gZZHRTDUPTagNtZ4IryftBzBindiHJndW9KuWWoV8dYR4DhjkOpp82ij7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
⚽️
رکورد جالب پوریا شهرآبادی؛ شروعی درخشان در پرسپولیس!
🔴
پوریا شهرآبادی در حالی که تنها ۲۰ سال سن داره، تبدیل شده به دومین گلزن جوان تاریخ باشگاه که در کمترین زمان ممکن به ۲ گل می‌رسد.یعنی شهرآبادی برای زدن ۲ گل، حتی به اندازه‌ی دو بازی کامل هم در زمین نبوده است.
📊
۶ بازی | ۱۳۰ دقیقه
⚽️
۲ گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139937" target="_blank">📅 14:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139936">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
باشگاه آلومینیوم اراک هم از بازی کردن آسانی شکایت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139936" target="_blank">📅 14:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139935">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">💢
ویدئو باشگاه پرسپولیس برای گئورگی گولسیانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139935" target="_blank">📅 13:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139934">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
عادل فردوسی‌پور: ترابی قطعاً ادامه فصل رو از دست میده، با خودش صحبت کردم و گفت دو پزشک بهش گفتن رباطش پاره شده و باید عمل کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139934" target="_blank">📅 13:58 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
