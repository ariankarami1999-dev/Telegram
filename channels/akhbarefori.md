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
<img src="https://cdn4.telesco.pe/file/GoxK92jFV1TD4kSacUT0namVFn_4mZHzbld4AdeZRTyZUvQK3LX8-qrXbdECKfsvB8KxpghfmuK2m5h9R5A5dAqdT4tcQtdUrUuXqOnhzmTZSeT3GzPjn_0UO6DKWkILbfUlaPbtww67hdjGMpe7EeYQByyydbTSLOqRtqGxxXEzzgprf5DK1mJm6pUI0NlsdXNX2H22kIiMsD401o0VH8il0UBaDjBFSWLNpXjKy-MfUr9K7tXgFOcL8PUcDufH8xGSWGtGtVpCjhLWNxmfHqezdOjrLn8eFO8IuqsFTmRt9kLMzxr3m-OAjt4xkG_PK6-huLK-8CkZr_AXKZ3o9Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.17M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 18:41:02</div>
<hr>

<div class="tg-post" id="msg-665000">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ابطال
فرمان اجرایی ترامپ از سوی دیوان عالی آمریکا
آسوشیتدپرس:
🔹
دیوان عالی آمریکا بار دیگر تأیید کرد که هر کسی در خاک آمریکا متولد شود، شهروند این کشور محسوب می‌شود.
🔹
به این ترتیب، فرمان اجرایی دونالد ترامپ که می‌گفت فرزندان افرادی که به‌طور غیرقانونی یا موقت در آمریکا به سر می‌برند، شهروندی دریافت نمی‌کنند، باطل اعلام شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/akhbarefori/665000" target="_blank">📅 18:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664999">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6721e5386c.mp4?token=BGcQqM53CskJ5h9awjnWhcehu-8031v-ikKlrIkr6mk0Kcs6luRK2Tc59HfAkeKcjuL0iR3zXT5PH13CTR9eh6MqIt4_RVkSK3R-LDsqO355FOqtbIl220o_TSASU5AechaSqBfUgN6OHZYkQTnB5F3V2aEpwJ070L5z0txC4etivvxTL7Y0AP3UWUb6hvZhSbC7ZXWSDA1VR4LlH2AEcqR3qUCQwd4ge_Ca-ISOOnSZ1v9TyFDoFuFJAvYaxzlLtNHuxkoTRyiKJD49kHgVEb6uQajuLN6FqgLJsyshzIz92A3rztJEHG9oVUIUvUIFSCNl2g_442tYvsRd1O_QRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6721e5386c.mp4?token=BGcQqM53CskJ5h9awjnWhcehu-8031v-ikKlrIkr6mk0Kcs6luRK2Tc59HfAkeKcjuL0iR3zXT5PH13CTR9eh6MqIt4_RVkSK3R-LDsqO355FOqtbIl220o_TSASU5AechaSqBfUgN6OHZYkQTnB5F3V2aEpwJ070L5z0txC4etivvxTL7Y0AP3UWUb6hvZhSbC7ZXWSDA1VR4LlH2AEcqR3qUCQwd4ge_Ca-ISOOnSZ1v9TyFDoFuFJAvYaxzlLtNHuxkoTRyiKJD49kHgVEb6uQajuLN6FqgLJsyshzIz92A3rztJEHG9oVUIUvUIFSCNl2g_442tYvsRd1O_QRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار حوزۀ مقاومت: مسافتی ۳ برابر غزه در لبنان اشغال و غیرقابل سکونت شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/akhbarefori/664999" target="_blank">📅 18:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664998">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjgrE0yVQGLWb1i0S5SEMnh4UjAasaVHPFbLN9Mf2gGtAI6dwQg4jrBV1satsd-2GMFXtoKAftqIavMNJHBNN0L3HcgPEOzvguDIU2jLk6BQiM0pBftHBUfMDYinkxy_WRY5jo9vYtwqvp5QLgOBdXPjjXff7V6j8KKlSmvr9y0LYQdu9TerMuKeyLk0tL_VlL0GuzZykiqWRSL-czGPO0DEcDI6RR5uz1dEHb4QBztCGTHFFewq5-SbKE6l-qpjqa16k46z_3-22Me7e5jaiBnP42AW4xs9WTEAUPpAXc-3sXf2J89-KGIwL_NQoVS89B8WfrOPz2fH0gd6faf5xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
سوگواره بدرقه یار
▪️
از تمامی هنرمندان، عکاسان، اصحاب رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود تا با ارسال آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور در سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» شرکت نمایند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگو تایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبر فوری ارسال کنند.
▪️
به برگزیدگان هر بخش، جوایز ارزنده‌ و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق آیدی
@Badraghe_yar
در تمام پیام‌رسان‌ها ارسال کنید
▪️
برای کسب اطلاعات بیشتر به کانال رسمی سوگواره در تمامی پیام رسان‌ها مراجعه کنید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/akhbarefori/664998" target="_blank">📅 18:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664997">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wh_SfnzcM3-T_V4jbaYq1WLWK5pV9SCnSkg-U1MlNf5kbB76NzaQ8iu7ZO17EzxVWOadXfRXuxTRlhRSLejNBeK47cfAfiPV8DLlKrWYJSiQ889J8F7EPQ902yiEP2Xc7OefiPwZ5Zms5YCgdjEbCi3kNm0Z4jYxtF6avXQhtZOflHNbDdq-MDubpxAlXp-XFcomJpTbABSAUc6YQ18_QeX8faqj2m4ck7TZqWb7EFlDd-BoDVxNmNyOtrkeSC_-ym6GQHRynSvjVDagCctW5ssHAfxZYnBQw6SVALYIKX-yJIlFS2y-cmbKe4SA_laBAjL2fxq2gOh4JUQLsuNHzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روز حساب، فراموش نمی‌شود
🔹
ورق‌های تاریخ دیر یا زود ورق می‌خورند و هیچ تصمیمی بدون قضاوت زمان باقی نمی‌ماند. مطالبه مردم عدالت است.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/664997" target="_blank">📅 18:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664996">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu5IirX9BdLhJ4LMHlEoTuP1dI6YTmv-7tYtTymW-Y4X5wKgNUFtfxcqUez06S6OEKlha9yPAx7y1XLOQWozvij8kChu4XshlSAaw1ICpep8PGYd2ZvM8V9q_g6f6crvmFIDFSKPzAwsj6484RD-2kad4Ws4Mr9Rz6_jy14SuHbeSo_mcG2PPD04-Qz68QIj3H0_Cntd9go3FDP28pfz1iE3OUdpLjg6MCkpVWZI_9iCsZ9pPOLlNe03s2_ZlwzHdBEbDrKsNVU6q1Aznl4Ic2EErLi8fJGRzi7dlZ_uR6ocE8ZA9t3cHDCXTFcb7-E2og5GbkPrctCC2CZBZIVDKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی آمریکا به یک هواپیمای مسافربری شلیک کرد
🔹
۱۲ تیر ۱۳۶۷، پرواز مسافربری ۶۵۵ ایران‌ایر که در مسیر عادی بندرعباس به دبی در حال پرواز بود، بر فراز خلیج فارس با شلیک دو موشک از ناو آمریکایی «یواس‌اس وینسنس» سرنگون شد. در این حادثه، هر ۲۹۰ سرنشین هواپیما، از جمله ۶۶ کودک، جان خود را از دست دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/664996" target="_blank">📅 18:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664995">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFZH2DGzRF2sehSMpCIXpjwkXV_8ULyYjuDwa1I5YifLSi2n-RfODwUtUNI-rD1L-L37WNn2MLptRiB02fDtUaYBcDg6R75U0VNXEcky0TdcTtlxkmnsthPTydRe6qYhnCIPkxY4E-h-dXN8eHueE1r_VcZveCjqpkXneRuTOjXacRBVfCQef4-sQ07LMVi-BEIXlC0bx8RFCuCgG0CZYr-qDMoc8wPggQDBuyf_2Cul8BoXMt06s7MTo0fD4eTIbuZEqQFXi4l9u2UmINVO3m1oC0tfFcObMz9Vnkqpn36DV2AJBJ-OFNLJ8e4f_bvJg4VT7qbm5eiDZtr7bkvjtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">٪۴۳ ترجیح می‌دهند در برابر بی‌عدالتی اداری سکوت کنند
🔸
در این نظرسنجی بیش از ۲۵ هزار نفر شرکت کردند که سهم روبیکا ۵۷، بله حدود ۲۹ و تلگرام ۱۴ درصد بوده است.
🔸
بیش از ۴۳ درصد از شرکت‌کنندگان گفته‌اند اگر در فرآیندهای اداری احساس کنند حقوقشان رعایت نشده است، ترجیح می‌دهند برای اینکه کارشان دچار مشکل نشود، موضوع را پیگیری نکنند.
🔸
حدود ۲۶ درصد از آن‌ها به دلیل آگاهی از حقوق خود، موضوع را پیگیری می‌کنند و ۱۸ درصد نیز به علت پیچیدگی و سختی روند، تنها تا حدی پیگیر می‌شوند.
@amarfact</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/akhbarefori/664995" target="_blank">📅 18:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664994">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9GJe9-qBFvauN6ubD0yi5q69cc3X6xhFSHU15YuqqhjgDBZW8rL4lbzNBNULmDOFX74yfZV1tDbVrVGTzuZ4lrd1MkAzEXtIZ7W2Ojzcxm1MNB58H8WvLY8qTM709wHRrdBrYvlQjwKHLuy6g5JpHgzGGnqsblxPf_b5qPveYlftfGjiolyvdsrxz19orQNvKehYYZAozPOWQW40KvPJ0loVvT9THDCNvnYBliVLzPYDFdj2I556gWdQYBHZ3XCyQKzcAtrBq5kU8fu-xDJZpjDqkk5rGYnz9FoqHOgU8bPZPJrqw1U1jTySq-s3z7zTBCTCbV7WZQUz6-UzNyw2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷ میراث مکتوب رهبر شهید
#بدرقه_یار
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/akhbarefori/664994" target="_blank">📅 18:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664993">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19e60e87d6.mp4?token=Or1Y5MvwwEbLihxiVv8mC1Ui-9ZS3t3Mo3CyBI6m85xcEV96kqh9_fhXQHwtOpcqvG1RyQxBypT274lzxMaqqJ3h95WKZ21gglB5lTZ1fcQQ1i64eW-lVuP2ZlHqSeeqN54P21MZmyin-RomNhodIKvlYa4Jhj4lWsEFLaZPmKhYVwC6MwqBy3DstvcOeO6RH_zJ1xfKACz4Lz4J7Rdk6oo6x5T4vyw7-pRV3LJG0J28WQ1YziyJVJP52wY1IV-1w9mPTZqAqXMbB6lMKbANV-zgyGLhgona6ocfT3ZteFkpXEfwIByCnXufmGoCANzCJQGbotu9vTTWg2DilwPSdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19e60e87d6.mp4?token=Or1Y5MvwwEbLihxiVv8mC1Ui-9ZS3t3Mo3CyBI6m85xcEV96kqh9_fhXQHwtOpcqvG1RyQxBypT274lzxMaqqJ3h95WKZ21gglB5lTZ1fcQQ1i64eW-lVuP2ZlHqSeeqN54P21MZmyin-RomNhodIKvlYa4Jhj4lWsEFLaZPmKhYVwC6MwqBy3DstvcOeO6RH_zJ1xfKACz4Lz4J7Rdk6oo6x5T4vyw7-pRV3LJG0J28WQ1YziyJVJP52wY1IV-1w9mPTZqAqXMbB6lMKbANV-zgyGLhgona6ocfT3ZteFkpXEfwIByCnXufmGoCANzCJQGbotu9vTTWg2DilwPSdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺️
بسیج عمومی ناوگان سوخت‌رسانی برای خدمات‌رسانی در آئین تشییع رهبر شهید انقلاب
محمدصادق عظیمی‌فر، معاون وزیر نفت و مدیرعامل شرکت ملی پالایش و پخش فرآورده‌های نفتی از بسیج عمومی ناوگان سوخت‌رسانی برای خدمات‌رسانی در آئین تشییع رهبر شهید انقلاب خبر داد و تأکید کرد:
🔹
۱۷ هزار ناوگان حمل‌ونقل سوخت و ۶۰ دستگاه سوخت‌رسان سیار آماده سوخت‌رسانی مطلوب به مسافران و میهمانان این مراسم هستند.
🔹
تدارکات لازم برای سوخت‌رسانی پایدار انجام شده و ادامه دارد.
🔹
تواید فرآورده در پالایشگاه‌ها با حداکثر ظرفیت و ذخیره‌سازی در مراکز تجمع جمعیت به میزان کافی انجام شده است.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/664993" target="_blank">📅 18:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664992">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcN5A1-ac_S5C3K29ViOFMfIHZGso-sJq3GkBczeux_B8geXRaE1_kHVeaIdoNvE6MGA9fqBi5FW2fvhOO7HP2lz9wTUS8k8uKCZI6V7Mkcmg1aLD5WF44xZUZpDuQ8zI6vFim8JRzdxf7SrjwNMv-zcd5W-OeO_CCHr_WO6NKi0KiNOXSAtedc3-Wt__cl6kA4l7VGq-zucvqkHXnlAG5H42oIe0HaCvv5KER-ajRPxLNMYvePIAmy_-GiFDdkThNqHly5Gs6cuV_I02OTQuYg0Nro-kE86DKOlPSI15TjVwJ9B8_bSxTcWs-krgXVzl7AhvrwsmAFbgcmXplxCEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مامان‌وباباها، رقبا شروع کردن و وقت خیلی کمه؛ اگه می‌خوای فرزندتون عقب نمونه و کنکور 1406 رو با رتبه‌ای که آرزوش رو داره و داری تموم کنه، دیگه فرصتی برای تعلل نیست!
🎯
فول پکیج کنکور 1406 کلاسینو
شامل:
🔸
دوره جامع
🔸
دوره آمادگی امتحان نهایی
🔸
آزمون‌های آزمایشی (برای سنجش دقیق سطح و رتبه فرزندتون نسبت به سایر داوطلبان کشور)
🔸
همایش جمع‌بندی
همه‌ اینا فقط با 15 میلیون تومان!
از تابستون 1405 تا روز کنکور 1406، یه لحظه هم فرزندتون رو تنها نمی‌گذاریم.
💳
خبر خوب: کل هزینه به‌صورت اقساطی قابل پرداخته!
همین الان وارد سایت کلاسینو شو و ثبت‌نام فرزندت رو نهایی کن:
wwwclassinocom</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/664992" target="_blank">📅 18:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664991">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad19fb633.mp4?token=SESBBNYViXYJ08W8qgdBWu3Vkeu3RHnLJeNiJP9TE--avRzCc7lqg7poCsrXRbrvSk_QGFwTA10CNuYEO6ufMNntHdiJvJ_gbBGl2XqqASHOg4CSwodZexq64nU-k68lxblwC8xbDwwTXUxg1H9Fbn3qQwIsDAx7OkM96VkENYI0SZrSdybcNVqPPjuDTy_Ao2hh8nX-NLTkO3QPwI7GxfWQOW2eN3d86QxZxcrE3m6cdLi0TrLcYpyqstL9bxWYi2bLb9TwxcYf5G0A4Rr8PQgsZx43IuAs4wmxfvnCXpk1sdwZwUa77WCvIAHkU-d7n4LX8bFVSXoWrJy7qIJgoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad19fb633.mp4?token=SESBBNYViXYJ08W8qgdBWu3Vkeu3RHnLJeNiJP9TE--avRzCc7lqg7poCsrXRbrvSk_QGFwTA10CNuYEO6ufMNntHdiJvJ_gbBGl2XqqASHOg4CSwodZexq64nU-k68lxblwC8xbDwwTXUxg1H9Fbn3qQwIsDAx7OkM96VkENYI0SZrSdybcNVqPPjuDTy_Ao2hh8nX-NLTkO3QPwI7GxfWQOW2eN3d86QxZxcrE3m6cdLi0TrLcYpyqstL9bxWYi2bLb9TwxcYf5G0A4Rr8PQgsZx43IuAs4wmxfvnCXpk1sdwZwUa77WCvIAHkU-d7n4LX8bFVSXoWrJy7qIJgoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروش خیابانی مردم پاریس در حمایت از مردم فلسطین
🔹
در ادامه واکنش‌های جهانی به فجایع نوار غزه، شهروندان پاریسی با برگزاری یک راهپیمایی گسترده، ضمن اعلام همبستگی با مردم فلسطین، وضعیت انسانی در غزه را به شدت محکوم کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/664991" target="_blank">📅 18:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664990">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94d0f8bf94.mp4?token=e409YFlvTzefcbpwzZF9Mgnyb0rCHjlLdAZaMFk-q549LqHVatGkoP4LL2nMeVnMKLYMov1WkH-R_-Sn5vbbPoP4Oi3wHXPp7gQj1vhVnJMlk9kb85iVMDPjNx82KD2Uovt5aDDWPn_QZNDhlXL5ZxJQ0-AvU5mVzbiWBaCH3Eo1f518VMF941nu2-3a-ohX70fQ8rJOp5f03nuWVWhY7H2759h3wPv9LQjhVJiLK1CB5YCjn5IVDbqerQMHHbawvhpXVM1pXZtjpXbbStfq5ah9BsddzwY_KOdF3yNO7Wh0FgMwpBZ9kdo4ZCUvhaKorMCjGlHsRnDxlag6r7MsGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94d0f8bf94.mp4?token=e409YFlvTzefcbpwzZF9Mgnyb0rCHjlLdAZaMFk-q549LqHVatGkoP4LL2nMeVnMKLYMov1WkH-R_-Sn5vbbPoP4Oi3wHXPp7gQj1vhVnJMlk9kb85iVMDPjNx82KD2Uovt5aDDWPn_QZNDhlXL5ZxJQ0-AvU5mVzbiWBaCH3Eo1f518VMF941nu2-3a-ohX70fQ8rJOp5f03nuWVWhY7H2759h3wPv9LQjhVJiLK1CB5YCjn5IVDbqerQMHHbawvhpXVM1pXZtjpXbbStfq5ah9BsddzwY_KOdF3yNO7Wh0FgMwpBZ9kdo4ZCUvhaKorMCjGlHsRnDxlag6r7MsGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار حوزۀ مقاومت: ۵ هزار لبنانی در جنگ اخیر شهید شده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/664990" target="_blank">📅 18:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664989">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
منابع العربیه: ایران تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدود شده خود را دریافت خواهد کرد.
🔹
ادعای وزیر خزانه داری آمریکا: چین همچنان تنها خریدار نفت ایران است.
🔹
چین خواستار حفظ روند مذاکرات میان ایران و آمریکا شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/664989" target="_blank">📅 18:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664988">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY8tn5z6w6WJT3qenKsemrH2_G1m8WtpMGXUSXV9Epm3hGC7xOewkA3NcH8mTnziiYoJk5ywpMwQTyVycGt5HCr2-XMx_Ej9rkZTlSvmij_UYUw-k0MwW0qnDBnO80LuQoPdEQw-MxVy5m7MIxtyxT4gVgsbEKo6-msc-Hje7dx6EkaxtkVAvxX35PAl4MZhsTzzL3-Dl3LvkcqzkkgN4PQroW6C6KCwH80HNpneOAEqYjAnrJ9goEm5NXSBF5XlDiZEW48SNLHFY39I6Eda9_HmiEUEW4q81D9AN4CpySZ3NRdswY1izfutOMZINxFgHlHWbmU6w0f4pDbUvq4ovQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخستین خلبان زن ایرانی را بشناسید!
🔹
عفت تجارتچی، نخستین زن خلبان ایران بود. او پس از تأسیس باشگاه هواپیمایی در سال ۱۳۱۸، نخستین زن ایرانی شد که در دوره‌های رسمی خلبانی ثبت‌نام کرد، گواهینامه خلبانی گرفت و نخستین پرواز مستقل خود را انجام داد. تجارتچی پیش…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/664988" target="_blank">📅 18:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664987">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
بازداشت شهروند آمریکایی در قدس اشغالی به اتهام همکاری با ایران
🔹
رسانه‌‌‌های صهیونیستی گزارش دادند سازمان امنیت داخلی رژیم صهیونیتسی (شاباک)، یک مرد حدود ۲۰ ساله با تابعیت آمریکا را در پی اتهامات مربوط به فعالیت‌های جاسوسی برای ایران بازداشت کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/664987" target="_blank">📅 17:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664986">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
خبرنگار شبکهٔ المنار گزارش داد که توپخانهٔ ارتش رژیم صهیونیستی شهرک بیت یاحون را در جنوب لبنان هدف گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/664986" target="_blank">📅 17:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664985">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏
♦️
نیویورک تایمز به نقل از دبیرکل سازمان بین‌المللی دریانوردی: امکان ایجاد صندوقی برای پرداخت‌های داوطلبانه برای تنگه هرمز وجود دارد
🔹
گفتگوهایی با مقامات عمانی درباره مدیریت تنگه هرمز انجام شد.
🔹
گفتگوها درباره هرمز با هدف یافتن راهکارهایی برای بحران پس از جنگ انجام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/664985" target="_blank">📅 17:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664984">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21eeb708c5.mp4?token=Fe6wpa7FjU7AD5cJgYbAaGHXvJkk8SVKYz9VBcdNpPSLBMXovFhSecwP03GB8GSMyuyUQZaHmxvF4nZufvczD1IxGqzCyMZ9jqGI43Ljgxh9cgPGovMyr_M6r6paqmc8Ib1xXX_hOqetoG3kPpBTPKjSffDoHKoOsJFCAjk5RG2BJET23qq-Yzn4kTYQc93owtsrD3qnKb8UqnxzNL_wTi_-ge7EyL7lK0TZpfy3c8_C4n_AWoUO9N1F0pQ-l583WPOBWWov3JrxYoSPY0j4xlgm5sR4naxRE6BKJEAjhXPq1YkPrjvS4AmL8f1luq_xWcYe1IhR1_-h0Z_FuEUSLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21eeb708c5.mp4?token=Fe6wpa7FjU7AD5cJgYbAaGHXvJkk8SVKYz9VBcdNpPSLBMXovFhSecwP03GB8GSMyuyUQZaHmxvF4nZufvczD1IxGqzCyMZ9jqGI43Ljgxh9cgPGovMyr_M6r6paqmc8Ib1xXX_hOqetoG3kPpBTPKjSffDoHKoOsJFCAjk5RG2BJET23qq-Yzn4kTYQc93owtsrD3qnKb8UqnxzNL_wTi_-ge7EyL7lK0TZpfy3c8_C4n_AWoUO9N1F0pQ-l583WPOBWWov3JrxYoSPY0j4xlgm5sR4naxRE6BKJEAjhXPq1YkPrjvS4AmL8f1luq_xWcYe1IhR1_-h0Z_FuEUSLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«شاه‌بوف» بزرگ‌ترین جغد ایرانی در قاب دوربین محیط‌بانان آبیک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/664984" target="_blank">📅 17:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664983">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bzi6YXMOKh5AcKkUtGrobqifjGDWf4VAKvbrqHsBP0f8yRvW4AURFRfXZqNdHq4rSChaxRLCLxTlpQ7t9-E1Q3xRFL80jDLOa3g5YyhtQyc9VwQqYgyAAd35vfzpF-xA-HgTcfqsCePmKW--eOhzrFfYqKDqOjV_AUnS6f1fn5BUVKgbtxjXI3ZFZB6DFAjoFikugclA0-zpwXVwBbbF-2E4lRkgtO8Z45Zl2YQGqQAIyGUXAl7gDjItCO3z_R1hVhXmBXI0k2lkxUS64yN9U2Zn7x_kQJu6MTXBw1Ur_q-k-tmVyZDQhgnKVhikhVG4zTOXvJMlsVnGgQISSWsRzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایرنا متن خبر درباره رای سعید جلیلی درباره توافق با آمریکا را تغییر داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/664983" target="_blank">📅 17:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664982">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
با ورود سازمان بازرسی به پرونده‌های بزرگی نظیر «چای دبش» چندین هزار میلیارد از حقوق بیت‌المال بازگشت.
🔹
پیکر فرزاد جمشیدی فردا در قطعه هنرمندان به خاک سپرده می‌شود.
🔹
رئیس‌جمهور گرجستان در مراسم تشییع پیکر رهبر شهید ایران شرکت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/664982" target="_blank">📅 17:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664981">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e5ccb5800.mp4?token=mB0cVbd9y2QcaFigiYgiMhfIAs0JWVupkDqEVgjM9snB0qxaWvSV141JEJjwxwdARJ69DgtMMpIMaEfixIgWsck_gLQvKGPgX20NZsRat4ndYzrBAcC1dXlaX9XIQVaDkqgeN49pfb_X28_Q1l3-X_95u9Z6PuVspRNaD8cn_Cb8nua6HO9lgUkIZRSkWXAwt4NN1Cl1AO1I8byPFvtlgyH10yzc8fHv9TbU1aknjHDROoBZFa2HSe2cozUQg9H5Rqy1TADi4ywbaxphQs9chZPBZuU32CCZcRgRlT8M6wK9Mzk66XgGuE2-WmDkrXdKnwUPNFPHS_UEcE3mHiysiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e5ccb5800.mp4?token=mB0cVbd9y2QcaFigiYgiMhfIAs0JWVupkDqEVgjM9snB0qxaWvSV141JEJjwxwdARJ69DgtMMpIMaEfixIgWsck_gLQvKGPgX20NZsRat4ndYzrBAcC1dXlaX9XIQVaDkqgeN49pfb_X28_Q1l3-X_95u9Z6PuVspRNaD8cn_Cb8nua6HO9lgUkIZRSkWXAwt4NN1Cl1AO1I8byPFvtlgyH10yzc8fHv9TbU1aknjHDROoBZFa2HSe2cozUQg9H5Rqy1TADi4ywbaxphQs9chZPBZuU32CCZcRgRlT8M6wK9Mzk66XgGuE2-WmDkrXdKnwUPNFPHS_UEcE3mHiysiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات گسترده به شیعیان روستایی در حمص توسط عناصر وابسته به الجولانی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/664981" target="_blank">📅 17:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664980">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b656067582.mp4?token=SEIzp6UTGWGdX7jgLwzKLVhWngSkH7iUhONa0HSMH6tVHMNh8_obbVL-FljLYTfCkq9A8voWDCQmwMlwHEA3WjBFc8_muikZAU8qoJjK-3Krx0hOjk9yW1r4HzIEN2u_r6EXQLgrK0vLzjQFMIPn3dMBbC-zGQVOM5Nle2KDOb-Sie1CUw4bu107q_ErRlml4n7hFW4kj45zLZZXVqX2UF64kElYFpJ4VioM2iGiZSDxADhH0Kicumr9ak2gUCIwUTVXqOcCtoPkz-37nnHTFAaP4vP6l5-2pTHINtMmrUsgg1aqiCTcJM2EJvqZ6zy3BfnkUFeGVPYhKMz0TWzvhlH9GBp7qe1EluHExf6vmOChreHQ1UR5-oRrjnXKf1jY2bidGptoYQe5TEKBhFQAKBiAOa9Q9XmQYNUWfrUsj8Q6BTtyks1aNyoX_jZf4v0hdAwyrFfNhWwiIRfuMHlwwfdUWru2aLcLTQjAwqYVnPoT0TMhKSe1jRD2v8nf61XTH_KyLsdQKb807dlbAoBiCpUiByeArmhCqY0aDpIwYdccGzRKeAtUUvHEYwVHaYlqJYRjkfQsfIACJlPEYMjur-0cGNg5961hDCJYFNI_aVFSOYJCVT9Gf2Tz7WmKaZo7re1pU-UjZA4kRySFL9JAmNKAk-x2OxnyBBTrcvuUsOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b656067582.mp4?token=SEIzp6UTGWGdX7jgLwzKLVhWngSkH7iUhONa0HSMH6tVHMNh8_obbVL-FljLYTfCkq9A8voWDCQmwMlwHEA3WjBFc8_muikZAU8qoJjK-3Krx0hOjk9yW1r4HzIEN2u_r6EXQLgrK0vLzjQFMIPn3dMBbC-zGQVOM5Nle2KDOb-Sie1CUw4bu107q_ErRlml4n7hFW4kj45zLZZXVqX2UF64kElYFpJ4VioM2iGiZSDxADhH0Kicumr9ak2gUCIwUTVXqOcCtoPkz-37nnHTFAaP4vP6l5-2pTHINtMmrUsgg1aqiCTcJM2EJvqZ6zy3BfnkUFeGVPYhKMz0TWzvhlH9GBp7qe1EluHExf6vmOChreHQ1UR5-oRrjnXKf1jY2bidGptoYQe5TEKBhFQAKBiAOa9Q9XmQYNUWfrUsj8Q6BTtyks1aNyoX_jZf4v0hdAwyrFfNhWwiIRfuMHlwwfdUWru2aLcLTQjAwqYVnPoT0TMhKSe1jRD2v8nf61XTH_KyLsdQKb807dlbAoBiCpUiByeArmhCqY0aDpIwYdccGzRKeAtUUvHEYwVHaYlqJYRjkfQsfIACJlPEYMjur-0cGNg5961hDCJYFNI_aVFSOYJCVT9Gf2Tz7WmKaZo7re1pU-UjZA4kRySFL9JAmNKAk-x2OxnyBBTrcvuUsOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار فیلمی از حضور رهبر شهید در حرم امام رضا (ع) برای نخستین بار - سال ۱۳۶۴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/664980" target="_blank">📅 17:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664979">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
انهدام تیم تروریستی در مرزهای شمال‌غرب
🔹
قرارگاه حمزه سیدالشهدا(ع) از انهدام یک تیم ۶ نفره از عناصر گروهک‌های معاند در ارتفاعات میان مهاباد و پیرانشهر خبر داد؛ در این عملیات چهار جسد به‌همراه سلاح و تجهیزات کشف شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/664979" target="_blank">📅 17:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664978">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIxjZHn6VtmWsBTIqzXdYq8WFRuGS0VbB94lOK3Nm1aEFdavUZKjGuuz-GflK0OzCuNFvmj_lS8kCpT3sBw3-7OOIpXNnlqOIDeqKLq3s5ND12byEhWNviDQMU0KUJaYQ0rc8oh8lh-gl4t8kxnSyesJrfLtimfJ2-fqH0kH7yXG16ehpSC5ficjcJPsfMxiZ8OQx67vRfycQjQWgUKFfTaGBkKcy4E5vsP7FKmLGKOwi-uzCobQt43dQ-ObdZ5Yky8tOkseuQpdxf0DL16ji6m5zqdiAJZ-TCM8O-FyK0jnP4xvaMGP7K7fzHUrvXuIN1VZBn2ZkyqAXqLpNuIiWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشتی‌ها از تنگه هرمز فرار کردند!
نیویورک‌تایمز:
🔹
کشتی‌ها پس از چهار روز حملات توسط ایران و آمریکا و افزایش خطر از تنگه هرمز عقب‌نشینی کردند. طبق داده‌های کپلر، با وجود خطرات آخر هفته، ۲۲ کشتی روز یکشنبه از تنگه عبور کردند که نسبت به ۳۸ کشتی در روز شنبه کاهش یافته است. روز چهارشنبه نیز، ۷۴ کشتی عبور کردند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/664978" target="_blank">📅 17:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664976">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
اختلال گسترده GPS در کشور؛ تهران بیشتر از شهرهای دیگر تحت تاثیر است
🔹
طی روزهای گذشته بسیاری از کاربران، به ویژه در شهر تهران، گزارش‌های متعددی از اختلال گسترده GPS داده‌اند. بررسی‌های دیجیاتو نیز این مسئله را تأیید می‌کند.
🔹
روابط عمومی مسیریاب «نشان» این اختلال‌ها را تایید کرد و گفت: «اختلال GPS طی سه روز اخیر شدت گرفته است. این اختلال‌ها به‌ویژه در شهر تهران بیشتر دیده می‌شود.»/ دیجیاتو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/664976" target="_blank">📅 17:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664975">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4a5d2d004.mp4?token=CeSP--xIIOM5Qo62nwsyBz2h01qOQXkfae7f7XaVQta1nrhDUEVIXWCSk6DvLkubZzojZhTxXAyipMs9WiQD7gb2u1Pcp6mDmXyv4PXHs9Rx1BdP1CxtjQeVf5YpzBNqeCEkvTnL-76ijCfyzoMwhUeool1fKATu8yFIZp_S-jBTsIJDQ3X_rKBJil-XUkWL1OEmAU6BMa6La2z8Pdf4G_Es_3OAY9SIvkVpnqR9nomD8sCBzizUYvtM43qFaBQteUA1Br7CWgoeZp8c1Ve9hVQk6gQRBm3pSmZ98RlXitfu179NmOyFx6I9TjwDTh0gHtYnP5ADwph6l5kDwenTWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4a5d2d004.mp4?token=CeSP--xIIOM5Qo62nwsyBz2h01qOQXkfae7f7XaVQta1nrhDUEVIXWCSk6DvLkubZzojZhTxXAyipMs9WiQD7gb2u1Pcp6mDmXyv4PXHs9Rx1BdP1CxtjQeVf5YpzBNqeCEkvTnL-76ijCfyzoMwhUeool1fKATu8yFIZp_S-jBTsIJDQ3X_rKBJil-XUkWL1OEmAU6BMa6La2z8Pdf4G_Es_3OAY9SIvkVpnqR9nomD8sCBzizUYvtM43qFaBQteUA1Br7CWgoeZp8c1Ve9hVQk6gQRBm3pSmZ98RlXitfu179NmOyFx6I9TjwDTh0gHtYnP5ADwph6l5kDwenTWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادامۀ انفجارهای سریالی خودروها در اراضی اشغالی
🔹
کانال ۱۲ رژیم صهیونیستی گزارش داد خودرویی در حیفا منفجر شده و صدای انفجار در سراسر منطقه شنیده شد.
🔹
تاکنون علت انفجار اعلام نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/664975" target="_blank">📅 17:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664973">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3gJXTIAPp2hipYRVz0LKZZPIyIsd76DeN6InVkhHpV3f41M6T4IWlrqYP7bXAlTm-Jsk5LOIpW6L1qWR88gcFePPBs5ptSlcCSPxLyYe7F7wPcsO8Wt8-GImPDGW6WJaYrBr4_eLu2EwkLA5KmpgqaSuR7_4Ef4TfxE0oG3BO3p7MFhxnb-9egfbR7qebb0s40R7bw3SxOE1ABx1IqbmUsrIAitVt5pwOcoUcIhw0QlzMjUcXZdtlN7aqFmvqyPw3hMsG1-E1Gw2xWx8NftCiUGEKNcc36jYIGyIzLpKDBqVjzfLthstskPC7MTChLcfIWu63qVRZ_X39Sycag0pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ردپای کربنی سفرهای رئیس فیفا زیر ذره‌بین
🔹
از زمان آغاز جام جهانی، جیانی اینفانتینو، رئیس فیفا، برای تماشای ۲۵ بازی در ۱۶ شهر مختلف سفر کرده است.
🔹
او در این مدت با هواپیمای شخصی خود بیش از ۵۰ هزار کیلومتر پرواز کرده است.
🔹
گفته می‌شود این پروازها به اندازه آلودگی کربنی سالانه ۷۸ نفر گازهای گلخانه‌ای تولید کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/664973" target="_blank">📅 17:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664971">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a561da02c.mp4?token=JbdYUDp73xkoLjuloS6j89G0lPCjcAMs-RbTIAEgiRYa8Rfz1rSxzS5__X2CewvWeQYfZUXedd1Oe2ZDbpDAdKB5loMoEP1MQV7Le-wxQdMjzdT6PuO-fZNDIv3DrYnBLXDRcVpeSxH4zCi0fxTts_Q95tAJRSW2sAUS7YikJcUO6LMWt0YSUpvCo6iU0-DzTTOl-pSPqHW16j_cfYd47m6Yh6yYie_dcuBhg5KpsTC4jU66oGNpFfdCHwJdEAWr5bB2zrwlUVToGmGxPxTuqXVF2AxuJJSTww7bU2uf3g_nnv83THTt7mxUEuOwtw-NK7kn69ytRnctEbMNwkHe4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a561da02c.mp4?token=JbdYUDp73xkoLjuloS6j89G0lPCjcAMs-RbTIAEgiRYa8Rfz1rSxzS5__X2CewvWeQYfZUXedd1Oe2ZDbpDAdKB5loMoEP1MQV7Le-wxQdMjzdT6PuO-fZNDIv3DrYnBLXDRcVpeSxH4zCi0fxTts_Q95tAJRSW2sAUS7YikJcUO6LMWt0YSUpvCo6iU0-DzTTOl-pSPqHW16j_cfYd47m6Yh6yYie_dcuBhg5KpsTC4jU66oGNpFfdCHwJdEAWr5bB2zrwlUVToGmGxPxTuqXVF2AxuJJSTww7bU2uf3g_nnv83THTt7mxUEuOwtw-NK7kn69ytRnctEbMNwkHe4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه در پاسخ به سوال خبرنگار خبرفوری: همه ارکان نظام در جریان تصمیم‌گیری‌های مربوط به جنگ و صلح و مذاکرات قرار دارند
سخنگوی وزارت امور خارجه در پاسخ به سوال خبرنگار خبرفوری در مورد برخی انتقادها از هیئت مذاکره‌کننده ایرانی و برخی شعارها و اعتراضات در تجمع‌های خیابانی:
🔹
ما جامعه‌ای چندصدایی داریم و طبیعی است که همه مردم ما تحولات را هوشمندانه و با دقت رصد بکنند و دغدغه امنیت ملی و منافع ملی داشته باشند.
🔹
همه ارکان نظام در جریان تصمیم‌گیری‌های مربوط به جنگ و صلح و مربوط به مذاکرات و گفتگوهایی که برای وضعیت فعلی و آتی کشور بسیار اساسی است، قرار دارند. این‌طور نیست که یک وزارتخانه یا یک دستگاه خاص به تنهایی تصمیمی را اتخاذ بکند. حتماً هر تصمیمی با توجه به سنجش معایب و مزایایش اتخاذ می‌شود و وزارت خارجه در نهایت موظف به اجرای دستورالعمل‌هایی است که از سوی نهادهای بالادستی، از جمله شورای عالی امنیت ملی، به آن ابلاغ می‌شود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/664971" target="_blank">📅 17:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664969">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbGvxgTO_IJvJaVea0FPLi0mVNa7kOAmaFIBxOkKCjUj8y1vuv7UCXFgUZGRM4kJdBt4088JtljMGPgtjt5x5xTT8SJYgKXWoj8NMrLHAdsoQfJw23ZHV6PKbK7Kj-cUyHMAxW7cIZI-HmJEVM_RAJI3Karu4o_6ji27_EYZXQRczuFkLByVuPYhHNlHPZtgMcI4-XcDP18rrVeQcwH2c1J7cvkV04TLvqHfejLi4wef7l7LOmSLMhvqMu8Fy0sLkgUbNQJt2KAJ65n5RW1uIC_4pDSKCNAf-47gKDr4Cyho9jXC-FeLigu3OeXrc4PCIruBamgmCdqguUQyR2vEdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیماری لوپوس؛ وقتی سیستم ایمنی به جای محافظت، به بدن حمله می‌کند
🧐
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/664969" target="_blank">📅 16:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664968">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlZojn-PZG4ZChQ9ucKXbiXtaWWj6NZVKC2hiYWb-ZSdA83p_3jynOkABiJyW3UDrS6P2JAhlo-MJmhuyhcceAG_P-QbtedSpMOUiHDvsJ0ueFeoq5xBZZCgc6DUcsXSEEBJveFV1WowQn742vHX0Y7shvjdjujf5XVVm6UUvqxZnPlAb-6qChwd-m13sZRdr315gOI_x6aHcIrsvq6GinBh7kbzJOdo0h-TmYsV8i_Wj-Wr-bvOHC_2jmB5YAtfBq_J9H4C1tR03cBPRXD27WMTPVEgrzKZiU-CbUXNsMaokzirFX1Kr88ZjVBuJ22-KI_08N2KpRzO7GtKOvKvEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری زیبا از ماه، پل‌خواجو و زاینده‌رود
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/664968" target="_blank">📅 16:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664967">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBcu4gAYsXKMOVzqlFPZf-B6AwKf4T8U6qho5FsoNdLm4hyvaBtyvnM3-TgH1LxXZjsi8bJm5PsRGVOXTODVDxtph2CxCCSVp0xg71CSWOzVe7ei0yuCaFCFm9p-jSQCbln6kB__d2rGrqZlLbkkhrkYh9Nqv6FzkfeOr8-JXyv2TLzbH-3DrGM78AwK7GSxkYjpXvW0zJU6HXSlNxJcwG9LzM1QGUzXE6c36SjOEJuIrOT4sl-rnR8lPQMa9ungfFnDrYtxqV2xq4xwDrdZ0XJINAbXokzvOrNQ0K0qopG1Nv3yYAYIA0JLpQDcdqrYzh529PBl7pNHGGKD_DJ5aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آنچه مسلّم است گریبان جنایتکاران را بایستی گرفت و آنان را به سزای اَعمال مجرمانه‌شان رساند
۷/تیر/۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/664967" target="_blank">📅 16:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664966">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-UlsObVarh2xOlamZQuNg-P5b8OQ8sS1C3Rz-gs4nSCkIl036_Mxd7Rcyn_K2RAojZwmabOqfRiseUy9vDkxfzS7tUvt18ILbO9yDvpwl9C_Rjg4EiHDORgXdo2eCdSgpY_dVRA3HBELhFjvHiOJVA5_FpxRJpYbzyhvShRj9MfuCrs26YtFBidtfN7olD0sAi3jb7UUMREk1388zXtNn2bSoaEctOUC2Yea3ImSMYsz3BfQQx2e1oF7FNB-4N68b2444a1OAG_s9fFscANXjMt73wxrdzKmaAsIOikfYZ7bFXVGFlrk9qrg9dHYwRWLC04HAhw2AWJPl4XeTgBEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هوش مالی کودک از خانه شروع می‌شود #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/664966" target="_blank">📅 16:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664965">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
پرواز مشکوک جنگنده‌ها از ورشو به مقصد تل‌آویو و انحراف آن‌ها به قبرس
🔹
گزارش‌های خبری از یک عملیات هوایی غیرعادی خبر می‌دهند که در آن جنگنده‌ها از مسیر پروازی خود منحرف شده و به سمت قبرس تغییر مسیر داده‌اند. جنگنده‌هایی از ورشو به سمت فرودگاه بین‌المللی بن‌گوریون اعزام شده بودند.
🔹
طبق گزارش‌های اولیه، این هواپیماهای جنگی در جریان پرواز، مسیر خود را تغییر داده و به سمت قبرس هدایت شده‌اند. این حادثه با توجه به ماهیت نظامی پرواز، ابعاد و دلایل دقیق آن هنوز به طور کامل مشخص نشده است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/664965" target="_blank">📅 16:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664964">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2SwPbmGgMTcW9yPE1eqlvSwDjM6QgqoS2RbMX5PY7TSaeSMW_SxqzV_0nCg-8-4_tQvb8mhyrLFJ1aB8w0AEpgTGgf1gOpBTdeDY5Jm57mUWcTE-22O06shcYe9iFfbqQxA7prdUi2FK9Nso5vhe0jH3qiul8KoTbGpvVPwIqn4QhtbZOUJm3rfxgu0oKV3CpmlHMR-Xk8jRNtaeLKJuemnOogHY48KDs0buJPl42cmHJnLh0B85GqXlnK-jLOwx486lRUXgpm-w_iXcBCXtJ8yuI1JDIbgEapk7JYfeh3c0hQ9mm0DgCeeP-eQFXpC0gNE92ksRaqwaHQzGmDq7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جایگزین‌های ساده برای کاهش مصرف پلاستیک
🔹
استفاده از محصولات چندبار مصرف، یکی از مؤثرترین راهکارها برای کاهش زباله‌های پلاستیکی و حفاظت از محیط‌زیست است.  شماهم به این پویش بپیوندید
👇
#نه_به_پلاستیک @Ertebat_baforii</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/664964" target="_blank">📅 16:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664963">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fb403db1.mp4?token=tMXUO9u2nHetPoNtvO2T1Sumn04pyfdIIhIhxgyu7QLjUPPxR7rM6bagCFpm1FulGLQ9dAEiatuf-0vH16SDrxo8U90KJLbE6N1GgA6Jgjhp30T9mogFNhjpV3M64qfh-P-ztht1dOrLjBiffCV2DUghy8hrHSy9J-rHOq8DIdAUPW6eGWfApVLhFSXra1MsjjPyn-En_D2g73HeB6q9aniyEzvzj64CllyXXuSGtxbVHbgZvXsCbtB_vpRAzurF3UuOSqoIPGdCT6pCXvcbQDfxy_KuKTl8tGbYxFQ0vY2jWkmYnT6O9x6BOrh2hzQw86Udlf_WhaWVKInBhky2LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fb403db1.mp4?token=tMXUO9u2nHetPoNtvO2T1Sumn04pyfdIIhIhxgyu7QLjUPPxR7rM6bagCFpm1FulGLQ9dAEiatuf-0vH16SDrxo8U90KJLbE6N1GgA6Jgjhp30T9mogFNhjpV3M64qfh-P-ztht1dOrLjBiffCV2DUghy8hrHSy9J-rHOq8DIdAUPW6eGWfApVLhFSXra1MsjjPyn-En_D2g73HeB6q9aniyEzvzj64CllyXXuSGtxbVHbgZvXsCbtB_vpRAzurF3UuOSqoIPGdCT6pCXvcbQDfxy_KuKTl8tGbYxFQ0vY2jWkmYnT6O9x6BOrh2hzQw86Udlf_WhaWVKInBhky2LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش اسرائیل یک شبکه تونل ۱۶ کیلومتری حماس را با سیمان مسدود کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/664963" target="_blank">📅 16:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664962">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/475436de97.mp4?token=R87NSjRxF_EeYEjhWGTkMJYiLSlBodNa0jAJ4OKxZXRlUIit9JC_owo_kSwDLGqX21LhRua-Js6hyzbQ7gzIr4RdKGkJcBdpexZ7USMCIwYwYIoRY6H1iC49YiQhnbxq4aiv5DgYhY0aNmnKaTcAbiyT_zCj_57xQyBP-wvBU2R5OMED3F42qMoV0iPiWGaLta_RI5KxtCoxI2TtUDxfyaxrUpj2SLDR3tdzdR2VBpmIVzRyMfVl_hnHw5Urgs1HKeUyMZwRCPQjw5vU9Cv14BYVMu44SSB03v6xetxx2LhpHK_0lQhu311Mf1wl0limMjhzj-eh0ddYojnNtPKRQUvVBtkaqLMIineRdKuu-p9koar1aQQNCGXrhSmS5Xc0Gq1vhBNJUpAlVX-OvggMHQTEPB9GGZH16wY9DY5J0TmHUJCra2okrnXvkXvx32yJj-0A-cYxvsqezt0abCw17kegt8j6J3_TMSr4W6xiVffh4HEmVH5KnF0gMKDabMK8SlU5xiMOJ6i-rjG1x6bLWNPlGiPayOUKJM2Etm4uOs36CcX8IAZb5e4m_bX5yriejDndow_CTvNZYDeGfC7YDeXEqtXGWFVemqaIuu67vJMFKXkrdeqzIsZr-TTVyHd4ANf6EXneSwcem5sZEFRU1b8kanhAewBnh6YnVmHGZc4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/475436de97.mp4?token=R87NSjRxF_EeYEjhWGTkMJYiLSlBodNa0jAJ4OKxZXRlUIit9JC_owo_kSwDLGqX21LhRua-Js6hyzbQ7gzIr4RdKGkJcBdpexZ7USMCIwYwYIoRY6H1iC49YiQhnbxq4aiv5DgYhY0aNmnKaTcAbiyT_zCj_57xQyBP-wvBU2R5OMED3F42qMoV0iPiWGaLta_RI5KxtCoxI2TtUDxfyaxrUpj2SLDR3tdzdR2VBpmIVzRyMfVl_hnHw5Urgs1HKeUyMZwRCPQjw5vU9Cv14BYVMu44SSB03v6xetxx2LhpHK_0lQhu311Mf1wl0limMjhzj-eh0ddYojnNtPKRQUvVBtkaqLMIineRdKuu-p9koar1aQQNCGXrhSmS5Xc0Gq1vhBNJUpAlVX-OvggMHQTEPB9GGZH16wY9DY5J0TmHUJCra2okrnXvkXvx32yJj-0A-cYxvsqezt0abCw17kegt8j6J3_TMSr4W6xiVffh4HEmVH5KnF0gMKDabMK8SlU5xiMOJ6i-rjG1x6bLWNPlGiPayOUKJM2Etm4uOs36CcX8IAZb5e4m_bX5yriejDndow_CTvNZYDeGfC7YDeXEqtXGWFVemqaIuu67vJMFKXkrdeqzIsZr-TTVyHd4ANf6EXneSwcem5sZEFRU1b8kanhAewBnh6YnVmHGZc4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افزایش سود بانکی به ضرر مردم یا به نفع آنهاست؟
🔹
زمزمه‌های افزایش سود بانکی در فضای اقتصادی کشور، باعث شده موافقان و مخالفان بر سر این موضوع جدال داشته باشند! اگر چنین زمزمه‌ای تصویب شود آیا اقتصاد ایران جان می‌گیرد؟ وضعیت مردم چه می‌شود؟
🔹
پاسخ ایمان زنگنه، عضو هیات مدیره انجمن اقتصاددانان ایران را در این‌ باره بشنوید
@TV_Fori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/664962" target="_blank">📅 16:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664960">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODCi2Ru1F5gvwh82uWvcsF5lHjPHB-WhQ9T3DTbxFGhWGIikwbRJY2iZMJFCTMzlZXj9PDvesecex5sR9Pqg0Lbx_NnkkmZQLdcaYz7f3fIwbUt-jWEyIgDtRuXP-cT0McgvVrFuClYklf_mvnfecvQ2HNHJHvoi8b1dhdCiE1bNviYQlL1t8UmkgaPdbgv4E1gZKdXe6dgFq721s-_ncEbcqWDnev3zih1uV755FdTqGZM5lQ1woImnTrMcuACuPYqhLY9GbX4xadlyB7hbYtOqwpir7394IIJqhtsCRYzxSfZuUhim6nzpRb5b9zOpRxUa3RQkkDKxo8wWctNklQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنجال کیف‌های ارلینگ هالند در جام جهانی؛ یک مجموعه ۳۱۷ هزار دلاری
🔹
به گزارش سی ان ان، ارلینگ هالند در جام جهانی ۲۰۲۶ با مجموعه‌ای از کیف‌های لوکس برند هرمس به ارزش بیش از ۳۱۷ هزار دلار خبرساز شد؛ گران‌ترین کیف او حدود ۷۰ هزار دلار قیمت دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/664960" target="_blank">📅 16:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664959">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
دوشنبه بورس تعطیل است
🔹
شنبه و یکشنبه بازار سرمایه به شکل عادی فعالیت خواهد داشت و دوشنبه ۱۵ تیرماه این بازار تعطیل خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/664959" target="_blank">📅 16:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664958">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQn6jouYTWqbCvmcwXjmAP9jwnEEgaTDprW-_SFOLWHifF0fJo72E-sfVnd4ydb8mzntw5NeAC0-1lcsY_Ql_VmsGrxLZwqAvE8dbc9K62paBSG_9HKeqp_gPQUhZpARUi9s7Myet__PkvlUue6ppC3bmkvK-YJJfQEq9GSuwBM9JGkTijBCKvSogmeLge22-gvztCmqy1Bg5pdb0oTsytZNlNs3vG4nm4L6BI1gCwQQ-VKNpnwJsw35B0-F2FgdJiKNVro3bPI3sDZ22fSDOSeE6qbezdX0kgQs5nZVJOSA_2xcAuCGq6RVcM-iZ2DZBReD4FkzDvhZ5xBW7gbu5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ایران یک چهارم پاداش قهرمان جام جهانی را گرفت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/664958" target="_blank">📅 16:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664956">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
بقایی: فروش نفت و فرآورده‌های نفتی و پتروشیمی بسیار تسهیل شده‌است.
🔹
استاندار: تعطیلی ادارات البرز برای شنبه و یک‌شنبه در دستورکار نیست.
🔹
مقام لبنانی: تجاوزات اسرائیل تمام بیمارستانهای جنوب لبنان را هدف قرار داده است.
🔹
محرم نویدکیا فصل آینده هم هدایت تیم سپاهان را بر عهده خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/664956" target="_blank">📅 16:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664954">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntp867X22DevSW8wdXTVreFwP6ynuwoVNC1sz1F5ti-_Kd0Yz0CHBt7nXkU-BMUx-V_8I31pOgnAd0nlLptGOGbXP8FZNeu-cfs_A3CWmj5xDN-oxxPyM8_ArS1Y4PmrcQyVmZSN2E5aLpBO3UvyBhKN9T0FcKFBhT9C6JuS5o7d1jW-puNPZRxxC2vE32diA6VHNNk8R8aItPV3pc0X0lXdmkBH-L8iS98EFpUkxsYBs3TLCnxXGy9E69j1fUPUoWiitPwqupQkrf38HdJ4sWkL8iH56M3ST8B-_4rhhHhmlgi8NUHo4pH4Ksw9qax-K_S3chLMaN188kb8GYOwNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y26k8SM5TrwkjW6maaDBUxA_z8nT3w7OgBpTg09KF9iQor30c77vxz8WKS8xSUXw5EjEILacnxSi5emP06iA_PNQIY8jh32Rb48njL67rs-2M6XaMXj2_U0K-Iyi1yJoGdqoe8H_cmkw6_zRvMatL1epRypjzKlg3hDqoVvO5_L4CnWwzzhr8ow33l60Ai0o-qfqCYNHwI0vgeMLG5D3cjbQ9t4m3nj1k0xhq_OX0JFXoA3TWZpBxPRgi_Srm713mH1oBoEpehGRCL1xUKA9mnWTBGGiMNGW3SPiuiMLAWrxqen7WL5Bz8syyHJy2dYCCRXKSp0q48KMOW5Anplt7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نیروهای امنیتی عراق همچنان به منازل نمایندگان عراقی میریزند و حجم زیادی پول از خونه ها درآرودن!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/664954" target="_blank">📅 16:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664953">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU9v_XCZlO3uOD4MB2bvPc7WWgDFVBzBzTpjBs4L2cf4ljjJqA88WQP--OZS3Tnby-O096IKetLfBk8sl-dzu2406y7YENbd6H1zm_rJUYsEPHfnLHWBhvLEh2qerldH-eBNU2CQVez5p7DKCUlfajIK13NvSckOrajLyP11fqyZGQ3-_4uK9hh2Y5S74uVIaehSRjTyS2lHDS3VCRgMsccbn1-Oz3sYwTVgcF2Hhq51Oh33Qlq9yQZ45ZvQ1V3l0fFtG9jJ-PJ4EC-70TOOF1Z6_Ouf89SVXBKoHtEgKDn6KAGXQjjUVy2PS7SN6EZg7z7Sv4uH6JuaXFxg10NJ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عجایب زبان‌فارسی که از شنیدن آن حیرت‌زده ‌خواهید شد
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/664953" target="_blank">📅 15:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664952">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0a535da08.mp4?token=MsbF0SzPvLAUGUP4LAjYVkUPV6OWTizrLipWb-NZpX1Fl9yzW79NLSagDGi4UzzmzW1sVQmWJ3NifXLnjfmpfGig7QUYfYtSCoiC7PkB6FvmtmMVRFlDu5rdJ1zsD3JUmb7YdytLBU-ZoDK2uEHmbRNDvxcSGgA__Hn-ZEVYn3DySlRwxjMFtiL_3pORJVVWmSWflUN5FoHEMQ-krye8WhHcwA4GYQc0fOAPc0SCUAHLODKq-olCLbsl6sBRWSethTjXJiJKZZCoN9pUu6T1xCydDBogc-mbq1vclB8a7DXtgn3ae0G9hle3vkA5ZjphpnQT3Ey08qr4E5yehMyAQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0a535da08.mp4?token=MsbF0SzPvLAUGUP4LAjYVkUPV6OWTizrLipWb-NZpX1Fl9yzW79NLSagDGi4UzzmzW1sVQmWJ3NifXLnjfmpfGig7QUYfYtSCoiC7PkB6FvmtmMVRFlDu5rdJ1zsD3JUmb7YdytLBU-ZoDK2uEHmbRNDvxcSGgA__Hn-ZEVYn3DySlRwxjMFtiL_3pORJVVWmSWflUN5FoHEMQ-krye8WhHcwA4GYQc0fOAPc0SCUAHLODKq-olCLbsl6sBRWSethTjXJiJKZZCoN9pUu6T1xCydDBogc-mbq1vclB8a7DXtgn3ae0G9hle3vkA5ZjphpnQT3Ey08qr4E5yehMyAQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: قالیباف به‌عنوان نمایندهٔ ویژهٔ ایران به چین سفر می‌کند و ترکیب هیئت همراه و جزئیات سفر به‌زودی اعلام خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/664952" target="_blank">📅 15:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664951">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
۶ میلیارد دلار متعلق به ایران است، اما فقط برای خرید کالاهای بشردوستانه
سخنگوی وزارت امور خارجه قطر:
🔹
۶ میلیارد دلار دارایی ایران متعلق به ایران است، اما طبق توافق ۲۰۲۳ با آمریکا، فقط برای خرید کالاهای بشردوستانه قابل استفاده است و قطر مالک این منابع نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/664951" target="_blank">📅 15:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664950">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a301d9738e.mp4?token=hNv-2SQCZv2bsXJv9yjAcphnxL58uZiz6EwYBG9O2RL9k3YxKWQXcIuddj2Ep_fmGK2OCuegOhjYhezNAtsAWpGUxtgcoNon7g-cYrHIl-SWYMAAfd6he5OZvA_5veUl1M3snAuOLbx4M13Gd9R3pRT0DSNB0NBQntwgcVYOm11I4rNQkHqGATs9s6j3Yida3pYvDaHnM2ldH5HMKjlpN2GD_lII3Rx5Lt6-JMcMARDfKZ2176uae33ay7tTJrqqNHDw_KqepuMCRXwpBqkvK2nSSri_qEEw6Mtu_ArDLwkBmTxJeyd1BwZAlpNnNFD2ocFewZufduCHLJ61u8lEMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a301d9738e.mp4?token=hNv-2SQCZv2bsXJv9yjAcphnxL58uZiz6EwYBG9O2RL9k3YxKWQXcIuddj2Ep_fmGK2OCuegOhjYhezNAtsAWpGUxtgcoNon7g-cYrHIl-SWYMAAfd6he5OZvA_5veUl1M3snAuOLbx4M13Gd9R3pRT0DSNB0NBQntwgcVYOm11I4rNQkHqGATs9s6j3Yida3pYvDaHnM2ldH5HMKjlpN2GD_lII3Rx5Lt6-JMcMARDfKZ2176uae33ay7tTJrqqNHDw_KqepuMCRXwpBqkvK2nSSri_qEEw6Mtu_ArDLwkBmTxJeyd1BwZAlpNnNFD2ocFewZufduCHLJ61u8lEMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صنعت‌زدایی؛ راهبرد تازه پس از ناکامی پروژه براندازی
🔹
برخی تحلیلگران معتقدند پس از ناکامی سناریوهای براندازی، تمرکز فشارها به سمت تضعیف زیرساخت‌های صنعتی و زنجیره تولید ایران تغییر کرده است. در این نگاه، هدف فقط توقف تولید نیست، بلکه افزایش وابستگی اقتصادی و کاهش توان خوداتکایی کشور است. از این رو، تقویت صنایع راهبردی، توسعه فناوری بومی و تکمیل زنجیره ارزش، مهم‌ترین راهبرد برای حفظ استقلال و امنیت اقتصادی کشور به شمار می‌رود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/664950" target="_blank">📅 15:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664949">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f4c0cc01.mp4?token=iTW7XimQmrqpATQuZKGM2pIEnM9VGDhXReh1-lZ4Y0VmMSJgL_CkDmTj6PXIDIsXSZyrb7Gi9wWA069fJvOCaViG4FAJBDiXGYYji-GF_gdA5BD_uIjhupMP85UF4aj20-35JdpKxnDAbJ0TToLolqwecPVAraW2H0ApoDtlFi3th3RM0xPi8vKzjElN1F-1iw3DhHDY89f-wSbMrfQ3qmvI9mOYHf-H9Dci1fa0GxwI2qXh222MbVaZ9W0w0pamsAhPs_5sTY53EUHYEVqTs9rR1vBSRh2kYo32KYRVRsElcSBtZQzo8QNDwKivevlEhwKaZljRDz93t0eYwhVfcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f4c0cc01.mp4?token=iTW7XimQmrqpATQuZKGM2pIEnM9VGDhXReh1-lZ4Y0VmMSJgL_CkDmTj6PXIDIsXSZyrb7Gi9wWA069fJvOCaViG4FAJBDiXGYYji-GF_gdA5BD_uIjhupMP85UF4aj20-35JdpKxnDAbJ0TToLolqwecPVAraW2H0ApoDtlFi3th3RM0xPi8vKzjElN1F-1iw3DhHDY89f-wSbMrfQ3qmvI9mOYHf-H9Dci1fa0GxwI2qXh222MbVaZ9W0w0pamsAhPs_5sTY53EUHYEVqTs9rR1vBSRh2kYo32KYRVRsElcSBtZQzo8QNDwKivevlEhwKaZljRDz93t0eYwhVfcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از شهدای حمله تروریستی در پاوه
🔹
روابط عمومی سپاه استان کرمانشاه از شهادت دو تن از نیروهای بومی سپاه پاوه، «برهان کریسانی» و «خالد خالدی‌نیا»، در پی حمله تروریستی و تیراندازی بزدلانه به درب منزلشان در شامگاه دوشنبه خبر داد.  #اخبار_کرمانشاه در فضای…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/664949" target="_blank">📅 15:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664948">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
آغاز مرحلۀ سوم ثبت‌نام طرح مسکن استیجاری
🔹
طبق اعلام وزارت شهرسازی مرحلۀ سوم طرح آشیان؛ ویژۀ استان‌های گلستان، ایلام و کرمانشاه، از ساعت ۱۲ امروز آغاز و تا پایان روز چهارشنبه ۱۰ تیر ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/664948" target="_blank">📅 15:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664947">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
بقایی در پاسخ به سوالی درباره اظهار نظر گروسی که گفته بود اجرای توافق وابسته به دسترسی آژانس و بازرسی‌هایش در ایران است گفت: تعامل ایران و آژانس به همان شیوه‌ای که تا الان بوده ادامه پیدا خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/664947" target="_blank">📅 15:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664946">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d935105e6.mp4?token=ebjGq5dMKH1fXZ3ESTa0zJiS6mxPdmpXZP88eFLVVHtERaD0EqiApfE5zS7rrnPi0dD_77MStfkVk3_cqeuUF7wFFhrXOFACvJ4DwRqGLeNI80jK6qlbc_NGwSdcA5lUHljUktjrnU-WLnqiuC1OJePbaG_LWCKMnZt3vVBbaN-pgqeIslPOziMaGQXhPO1A9a9gfMwNo8TWlCxK_Y7iLwQjAJPwHQbuZrZlcq5_N2DwOGqJEwq5TT0f2ZVLp29B7B8R9GFtXHZl90XEngyu9Pr4PrgUbOjNGEjHNOz4t271kVZd_p60fATC91TDjz9sk0X0QSJdiOWnBm1m-nSw7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d935105e6.mp4?token=ebjGq5dMKH1fXZ3ESTa0zJiS6mxPdmpXZP88eFLVVHtERaD0EqiApfE5zS7rrnPi0dD_77MStfkVk3_cqeuUF7wFFhrXOFACvJ4DwRqGLeNI80jK6qlbc_NGwSdcA5lUHljUktjrnU-WLnqiuC1OJePbaG_LWCKMnZt3vVBbaN-pgqeIslPOziMaGQXhPO1A9a9gfMwNo8TWlCxK_Y7iLwQjAJPwHQbuZrZlcq5_N2DwOGqJEwq5TT0f2ZVLp29B7B8R9GFtXHZl90XEngyu9Pr4PrgUbOjNGEjHNOz4t271kVZd_p60fATC91TDjz9sk0X0QSJdiOWnBm1m-nSw7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشت تلخ کره جنوبی به اینچئون؛ هواداران خشمگین به استقبال تیم حذف‌شده آمدند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/664946" target="_blank">📅 15:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664945">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هرمز؛ برگی که نباید بسوزد!
🔹
همه نگاه‌ها به تنگه هرمز دوخته شده؛ آبراهی باریک که این روزها شاید ارزش آن از بسیاری از میدان‌های نبرد هم بیشتر باشد.
🔹
شواهد نشان می‌دهد نبرد اصلی دیگر فقط بر سر عبور کشتی‌ها از این تنگه نیست، بر سر این است که چه کسی کنترل مهم‌ترین گلوگاه انرژی جهان را در دست بگیرد.
🔹
امروز تنگه هرمز مهم‌ترین برگ برنده ایران در معادلات منطقه‌ای و مذاکرات با آمریکاست.
🔹
برگی که اگر از دست برود، تهران یکی از قدرتمندترین ابزارهای چانه‌زنی خود را از دست خواهد داد و به میز مذاکره با شرایطی نزدیک به گذشته بازمی‌گردد.
🔹
به همین دلیل، مخالفت ایران با هرگونه دخالت خارجی در مین‌روبی یا مدیریت تنگه هرمز، صرفاً یک موضع نظامی نیست، بلکه دفاع از یک دارایی راهبردی است.
🔹
در چنین وضعیتی، طرح‌هایی با بازیگردانی غربی‌ها برای ایجاد مسیرهای جایگزین کشتیرانی و سپردن امنیت تنگه به بازیگران دیگر مطرح شده است.
🔹
پیشنهادهایی که با استفاده از ظرفیت کشور دوست یعنی عمان، در ظاهر با هدف تسهیل تجارت جهانی ارائه می‌شود، اما در عمل می‌تواند نقش ایران را در مهم‌ترین اهرم ژئوپلیتیکی‌اش کمرنگ کند.
🔹
اما این فقط یک ضلع ماجراست؛ ضلع دیگر عمان است، کشوری که شریک تنگه هرمز و یکی از معدود میانجی‌های قابل اعتماد در سال‌های اخیر بوده است.
🔹
برخی بازیگران به‌خوبی می‌دانند اگر تهران و مسقط بر سر آینده تنگه اختلاف پیدا کنند، مسیر اجرای طرح‌های ضدایرانی هموارتر خواهد شد.
🔹
نبرد واقعی امروز، نبرد بر سر کنترل روایت و مدیریت تنگه هرمز است. هر تصمیم درباره این آبراه می‌تواند توازن قدرت در منطقه را تغییر دهد.
🔹
ایران باید بیش از هر زمان دیگری مراقب این بازی چندلایه باشد، بازی‌ای که شاید با یک پیشنهاد دیپلماتیک آغاز شود، اما پایان آن می‌تواند تغییر موازنه قدرت در حساس‌ترین آبراه جهان باشد.
../خبرفوری
#سرمقاله
@TV_Fori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/664945" target="_blank">📅 15:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664944">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نگاهی به عملکرد ۳ سال اخیر بانک توسعه صادرات ایران
🔹
از رشد شاخص ها تا بهبود خدمات بانکی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/664944" target="_blank">📅 15:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664942">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ded290b18.mp4?token=BiR6iEb0GHKNUPYO7pYW1Fdbl5CANbq3sDg8rjepX5bG4GpiWkroGmsRGLFGe4CDfry2c-zZR4a_5qVCHfAi5G1GWmevXW1hIUCPdA47I1j3iyu9PzX3SS6faZ140e2fdM8riFDAadMiiyAoPyuCy1dox3ZFDtWePCKnxNQbTns3TEfBi08W-UC_LUjpQyfZB1hbMIS4JQjqhWWwbzDvA-sEZYCWdlIFXYmC2qc56RodhF6tcuAxxahcLZgLoy2PoJs6D8XZq0ZHt2F-ZYHSADPYxMvWtYnabg0z_q6J7Gf4FqRTAvD5KQGmMa2dJ8B2pioQkXODNbmVhwjJGTm24Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ded290b18.mp4?token=BiR6iEb0GHKNUPYO7pYW1Fdbl5CANbq3sDg8rjepX5bG4GpiWkroGmsRGLFGe4CDfry2c-zZR4a_5qVCHfAi5G1GWmevXW1hIUCPdA47I1j3iyu9PzX3SS6faZ140e2fdM8riFDAadMiiyAoPyuCy1dox3ZFDtWePCKnxNQbTns3TEfBi08W-UC_LUjpQyfZB1hbMIS4JQjqhWWwbzDvA-sEZYCWdlIFXYmC2qc56RodhF6tcuAxxahcLZgLoy2PoJs6D8XZq0ZHt2F-ZYHSADPYxMvWtYnabg0z_q6J7Gf4FqRTAvD5KQGmMa2dJ8B2pioQkXODNbmVhwjJGTm24Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی دیده نشده از شهیده زهرا محمدی گلپایگانی نوه رهبر شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/664942" target="_blank">📅 15:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664941">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ادعای اکونومیست: جنگ ۶۰۰ میلیارد دلار به ایران خسارت وارد کرد!
اکونومیست:
🔹
در چهار ماه گذشته، طبق گزارش صندوق بین‌المللی پول، جنگ ۶۰۰ میلیارد دلار به ایران خسارت وارد کرده و تا ۷ درصد از نیروی کار این کشور بیکار شده‌اند.
🔹
اقتصاد همسایگان ثروتمندتر ایران در منطقه خلیج‌فارس نیز کوچک شده و این درگیری ممکن است امسال دو درصد از رشد تولید ناخالص داخلی را در خاورمیانه بزرگتر کاهش دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/664941" target="_blank">📅 15:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664938">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czwTLFwopqEEUxIiMGm8WVHbeDEZZpuYDhXplmz5SxfdA9_t3I1E-31GZyFLZfNfydYVMW4NeUYOFNdxcNzFS7hm5cwTnbmmKDaD3_k_gZxIEc0uepDYtncKcwvs3c3JfNc7V6x_1ufsLGaEXxOA5z5bKOF3ZL-ohmgtdJ-kJe57FxAGvAjjglZAaJyL1sUFQT1EcFf5Pqqap9Z9n8w8QqtpH_i_uLbj8zZnEryYnNC25xjjFfCEYRuvD3kPNFdQqH67uRkj6XPdsxXcoDNRWGYgYgTkP2dfwCIGGuHrdNW98NHC0gDX4MPgbMjcrZnMYicxdmlrc9Nelmjr9uNe-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وسایل بهداشتی ضروری برای مراسم تشییع
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/664938" target="_blank">📅 14:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664935">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd43a26eb.mp4?token=PKmf7xtamjTgMLSVa6FBC4SQQ2VHKnEtt6SzVIQVRtgWSWYrsE2T7UnW-X5vf0EiMO8Zs3HPqmNy5w-6r994NIPx8kWIccTsOFQqRNdzrb3MfsnJ4UckTg_d0wIUMHZE1W3TLUFcMvtqRjPAcOYrQBAwMkxPpu435DqUyAUC-6oQI2PnbiJoR8-Hc51oYEqw3qu1_f53kseiZClEgWOHBxL23OWwvz1RP2mtmNRLXTqGG7BF6A_REfMQex14H_-i8n4Twevv50gLkZUpWZ91HiWnreVqbB7mloudQc3M5HNoVoLOyfdgmNfnga0Vu6w5FJeLzTcrnUJ7Ky4He-4Wzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd43a26eb.mp4?token=PKmf7xtamjTgMLSVa6FBC4SQQ2VHKnEtt6SzVIQVRtgWSWYrsE2T7UnW-X5vf0EiMO8Zs3HPqmNy5w-6r994NIPx8kWIccTsOFQqRNdzrb3MfsnJ4UckTg_d0wIUMHZE1W3TLUFcMvtqRjPAcOYrQBAwMkxPpu435DqUyAUC-6oQI2PnbiJoR8-Hc51oYEqw3qu1_f53kseiZClEgWOHBxL23OWwvz1RP2mtmNRLXTqGG7BF6A_REfMQex14H_-i8n4Twevv50gLkZUpWZ91HiWnreVqbB7mloudQc3M5HNoVoLOyfdgmNfnga0Vu6w5FJeLzTcrnUJ7Ky4He-4Wzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کادوهاتو شکلاتی بسته‌بندی کن
🍬
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/664935" target="_blank">📅 14:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664934">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تشکیل وزارت مدیریت بحران در دست بررسی مجلس
کامران پولادی، عضو کمیسیون امور داخلی کشور و شوراها در
#گفتگو
با خبرفوری:
🔹
در دنیا حدود ۴۵ حادثه و بحران وجود دارد که ۳۴ مورد از آن‌ها مانند سیل، فرونشست زمین و... در کشور ما در حال وقوع است.
🔹
خیلی از کشورهای دنیا برای این منظور وزارت مستقلی تحت عنوان وزارت مدیریت بحران دارند؛ ضمن اینکه ماموریت دستگاه‌های مختلف در این راستا نیاز به یکپارچه‌سازی داشت که ذیل یک وزارتخانه قرار بگیرد و فعلا تشکیل این وزارتخانه در مرحله مقدماتی است که روی آن بحث صورت می‌گیرد.
@TV_Fori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/664934" target="_blank">📅 14:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664933">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlXCILegzV81l14gj2721wH35tWKokhiR-WO85bveRiL45z79C5WfCWO3KibxlBAe8xUzvIHV3Ga2DCsbG3BipOTz4gNAr9cAEEta-SnVfsMSPKm_pInt8vAne5Dmf-Yome6fqmwhFpJNru8k_xG_DiIMYBGg6vixAIDVzhnJLKk3H4-AQhPULkjq-Np197PphySunsJYFthS62E1hiCk2b6chRID62viJQsx4ls2rPT3mhmmZVa5Gd3mnljQI2Oi0gsttZ6mUk78YCVhlZXzfXB3wnrCmEFpuiVn4UkCwuKZz6j5z2JDFMdVAW26R3-owBR2oBofO84iSU3ZddhKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایرنا متن خبر درباره رای سعید جلیلی درباره توافق با آمریکا را تغییر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/664933" target="_blank">📅 14:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664932">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
تهران ۳ روز تعطیل شد
🔹
به مناسبت برگزاری مراسم وداع، نماز و تشییع پیکر رهبر شهید و خانواده ایشان، تهران به مدت سه روز تعطیل شد.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/664932" target="_blank">📅 14:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664931">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iI9ikYj4krwVkSDCPeA_LYtrh0yEewKIjlEGnyx3NYQnZrjZAItM8kPbit7aUr0NeMuHuj5Qlk2diYNdN0SqZ3MlzxmE7PLrmc0y-_6B6Uk4XfFrxvCfniFLMHls4pXQcd_wHKkTmmcG7k_RrGtbgOdDTDAEMyLvdrH3MEPpAZ2sMLZJtBHZFML_iNAmXzBD8lPH7KefLkvZbI67ORNODwMZSpeN8WocCaf4A9HMGMwtqtVFvI3j1hBgt7dZMonqJAck4VgxftoUGUhIpUjoYXSJqRhoM54h2S4thdbfB_3hXdcYP4W3xMUpKJzOLHSr0lef36pDtvF6AYPiFRGZnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بالاخره بعد از سال‌ها یوزرنیم به واتساپ اضافه میشه!
🔹
واتساپ بعد از مدت ها قابلیت انتخاب یوزرنیم برای حساب‌های کاربری رو اضافه کرده و از همین الان میتونید یوزرنیمی که مد نظر دارید رو برای خودتون رزرو کنید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/664931" target="_blank">📅 14:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664930">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وششم از فصل چهارم
🔹
در این قسمت بخشی از روایت تجربه‌ نزدیک به مرگ خانم زهره ابراهیمی که چند روز قبل از تجربه حضور ملک‌الموت را در کنار خود احساس می‌کردند و در شبی با رؤیت ایشان و فشار اجزای اتاق روح از بدنش جدا شده و با سفر به عالم برزخ و درک کامل از مرور زندگی گفته‌های شنیدنی را نقل می‌کند ، نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: زهره ابراهیمی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/664930" target="_blank">📅 14:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664928">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9b6b04288.mp4?token=DtdXk-Jx-LIhxYyVpymiNHATk2knaT19gFnZ2veEDcpw0oKIjemwZlyJi45kIo7r4hIde-4pSiJRU-1ZocGkJQduLiKnigntRInfv_yMH1AX8vSYqa3l86xzWgOusklYXaJ_KK89EYr79h0K4I_vyn3IPNzsEZTsUqFYs5e8ZWy3NsiWM1tP-Pi8o0PuOuFFqhD2OZg_oCpj8D18TLxu-KXlqRz6WO-e3jdoDTPmOtrxyCIX6xinQ599bTzzCywVuMmukJZE0Skdinkl5IWkSoIABbo2mch2d5tYVuEq2kxsmIT_y0RrZmq-CrnI4qswegNX3YUB4VE6weFnT25XohREHO5eiliJ8WIKuYznhwy5Ak_2CxHZ_hLR546fF7m3z7NUoyRKlM0aXeBFnzLn-LB9LR1RFpxZIHpedPNSduoclZ-zCfCO3O8eoTAp9NcYv6aOFG_Foe__ftLfXtyJ-0Wa4CaXu4YdDURuW_STcCymBg1KoNoDc5zxxBrpvG7FZUagBnBIeo4f9O2YjLvThNh8UZnn75W3cTjGSjW5P0nmVIxYVQByraCLwqAa3iULHcyy1IFL7wirMrrC750KKF46RY3qAkHme4PMRI0jFhOjGoZRw54xUTUJmpNz8d1O-VS0TyBdM8LGbc-2yt9KCz9NJ65rVTBeORj2Se30oD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9b6b04288.mp4?token=DtdXk-Jx-LIhxYyVpymiNHATk2knaT19gFnZ2veEDcpw0oKIjemwZlyJi45kIo7r4hIde-4pSiJRU-1ZocGkJQduLiKnigntRInfv_yMH1AX8vSYqa3l86xzWgOusklYXaJ_KK89EYr79h0K4I_vyn3IPNzsEZTsUqFYs5e8ZWy3NsiWM1tP-Pi8o0PuOuFFqhD2OZg_oCpj8D18TLxu-KXlqRz6WO-e3jdoDTPmOtrxyCIX6xinQ599bTzzCywVuMmukJZE0Skdinkl5IWkSoIABbo2mch2d5tYVuEq2kxsmIT_y0RrZmq-CrnI4qswegNX3YUB4VE6weFnT25XohREHO5eiliJ8WIKuYznhwy5Ak_2CxHZ_hLR546fF7m3z7NUoyRKlM0aXeBFnzLn-LB9LR1RFpxZIHpedPNSduoclZ-zCfCO3O8eoTAp9NcYv6aOFG_Foe__ftLfXtyJ-0Wa4CaXu4YdDURuW_STcCymBg1KoNoDc5zxxBrpvG7FZUagBnBIeo4f9O2YjLvThNh8UZnn75W3cTjGSjW5P0nmVIxYVQByraCLwqAa3iULHcyy1IFL7wirMrrC750KKF46RY3qAkHme4PMRI0jFhOjGoZRw54xUTUJmpNz8d1O-VS0TyBdM8LGbc-2yt9KCz9NJ65rVTBeORj2Se30oD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدون فرمان، بدون پدال؛ تسلا آزمایش تاکسی‌های آینده را آغاز کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/664928" target="_blank">📅 14:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664923">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UAPKgzqHy4Ss_VONuWPWLbN1DX7ai7uMkuxFDnreaX1rt01fBxhMw8cIjAqZPmHl7AMGBwYTPQ4lobAiz4d_cQi9tbQn2m9aU7kASrURgNrgF8Spov1LjRLZTT4ppF_CEbeKKOdA1_pcRb-2Jg8z8zqc9GQH3euh9_k8OFxNkzh_ohqKAkFXZrVF_3os8JZn3Caw8nxYJW1Q37V4pdKUAz-pDzN-t1A8cqB9E7D997Bo2UgjQKcwJ_43RnbpEXkVsPEDXRrDyryJWJBBgW5mj74I-VTSSrn8fhZOPnwtzBkWUNKAl_xtWJqC3eCFCVYbImNIM6BDIEzE-eM9Y4N-uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKAPrcxb5IXIyXyrxx2AxZE30xlwFwUo4PEIHB6BSowY_96oAMyY75ygCD1QSsnLVmJRtAxjwjB2XV0ZXmWPHLazZKhLCSaJGmdlEEb67dQI0XaTZk8F5-I0SYkd_6_P6rgHvJV1AB0nkyLZ4T66-6Ucq0qoqmcQIMbC61eCpxZZ5S_el43J9zClvkxA16RhSxFaY1-BuGUEd1aiVZ7kRwBXTLewIXkwMbPde1d_9fSyBJCJnpob6XWymbEnSaJ1_0m_aR8sZtVSi0llBq16OeSq5uoXmtH8tKqAyYLnUe9H_Vmr607ILBy1-v_5aGKiHgKI6yT6iLx0WDO6X3H7Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8ARzBvC9uCwyPNvYpOzXnXf5i7CBs1efXhsE5vHAQlPxPxxJxM0PC1Xh9zl9MRkTP2PHsHRdtWaVGgy0Hm406mWyzRgxwmtQVpgoIRcENJyGZ3K2miw15DTcCOw0aHsNritbCVC9-L0ZRT9plqHmX7HIb34IaWyrC9SZ-Li_jiXcc0p2grfk3S05jpCPc_LvndCCQSC2Dk_hUrZntAtuTtIzUALGB2KG7jcMZ0s8bqp_6RFYKqoLeKplWSg-eWQE9_HeoHr-X64f8dQ0gFPOahYL8Joo4IuAlLqt7h_ncOcSdpEE3e_Ca4u3EJu3F9kNJKHcOio_v8XgrI0nfpEjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/odIt0DAj_J0srJ8R0vAHIXeHJtiiLi4mgHT_cfHePmPXKnoYsowbaAOh4rPpI50TGe2nLglzv7A2nfXPpE71M2IgtR0NzTSHercKtRI1xjwYM571oE45GwJInKWtrXg0R0FYYF_nHHD8QCWD44v9x7Zm7aPnc_FT8kQrNByaE6-AXuS9scYHw8CHc_u_VrOuNCkiGrAb-pjbgCCvtYeZkR44OQDkZSy_n4MkQEkdzJRAzmhLNmuzZA6DMc8_dEitwPzlmVbf7_vz03sQ0fdMpv-pqiRi7o51_ktUVd91l_rgGIrfpgqQJcLuxbTciAKkjQVxIzvRLhMIY0ymdiEmeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jz6Pa9zyPZCx-NE5j1V6B8iXKL0MF7XNlhPEORlGxRmlO_9gKyes5pTxaMUH0t65OSun7j6boYMYGUpsIEOZ1OMZhg6ryxO_IYuNSQfDGMxewUV3tE4LISEwKDbWp_4ntvv3feOAAuyXGvXpsy1rAp0abGLsQijkBy8zZrSqzYvTDnhs0J8XiSSitEbJkmWLp-17YZGY5OfrRQy0viQXaWbcsYmNrAxnp99E2kdpfcAjW5hhqF0G3xl4kz6whxuqlIESfT_lX9HZkROKAsC0BZGBDMtMas9Xu3JN7DgXFLRcrSIQ_ffF_ht_BoKMzEPaXZrkA_eV2yn4pwmhnmfAJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تأثیر هر قرص بر سلامت و رشد مو چیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/664923" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664922">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcbd4f0172.mp4?token=FeOTZLqbPoIyDAc7Z6k1An-y8a1aWV34mTIAnyxsHaXFfkcwSXtMl6qp8JQpCNVnxSXMBJhzPGI9QT0Cp-AzACCDY95xFIYd8lzipzhPCdnu0MAvsd9nO5PIzUKkXatibfHEO-CZXJidv5HPtURyI-xJZWgKjlxDUYWPd12h1alSDD2vvqWhVwZ3ly9ZaewuyAeZJ45JdTSomWYL-iRpjK6_lO9yer9H1GZ7mkXEiqQKMH1UCkcaQUFoT-wPfjoYlP6YHzfbl3DEUkGKLlsRIFEovKuLlFvjAJLtEyY7McHYF5H4E1uNquXpdmmOqSURLIK2NpELBDpuLzsDwRp1SwYxHJQF8KNYTeg07NPqAX0q0aNFEnwEb0MA01eErDgkjazGCMdNf2crHWXpZFufdnMY6msljSu_vhVfYrjNpzU6GZEfoGeaH9i3pDBF4QgxcgwiB-22IlIpN0XdkEH1a55jL9mogGmPk-D3BnoerEqGpqayFd5m5DROYw7cu9RNBKiZRvRJ0eO4aWZE6XSixEQ7Hj1fj4KQJdKoajqbU74smU4YDxqTDHnvUK7XxafER_4dJGOEDXg3ZeunhmF6pcx6FyIM-lyg81Daj-femQrH9JhBuhygNaQI2IGc0jvG4Y8r28rVbiFZrCW4wpR8NWDT3XqGMEw3g_AOPllbPds" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcbd4f0172.mp4?token=FeOTZLqbPoIyDAc7Z6k1An-y8a1aWV34mTIAnyxsHaXFfkcwSXtMl6qp8JQpCNVnxSXMBJhzPGI9QT0Cp-AzACCDY95xFIYd8lzipzhPCdnu0MAvsd9nO5PIzUKkXatibfHEO-CZXJidv5HPtURyI-xJZWgKjlxDUYWPd12h1alSDD2vvqWhVwZ3ly9ZaewuyAeZJ45JdTSomWYL-iRpjK6_lO9yer9H1GZ7mkXEiqQKMH1UCkcaQUFoT-wPfjoYlP6YHzfbl3DEUkGKLlsRIFEovKuLlFvjAJLtEyY7McHYF5H4E1uNquXpdmmOqSURLIK2NpELBDpuLzsDwRp1SwYxHJQF8KNYTeg07NPqAX0q0aNFEnwEb0MA01eErDgkjazGCMdNf2crHWXpZFufdnMY6msljSu_vhVfYrjNpzU6GZEfoGeaH9i3pDBF4QgxcgwiB-22IlIpN0XdkEH1a55jL9mogGmPk-D3BnoerEqGpqayFd5m5DROYw7cu9RNBKiZRvRJ0eO4aWZE6XSixEQ7Hj1fj4KQJdKoajqbU74smU4YDxqTDHnvUK7XxafER_4dJGOEDXg3ZeunhmF6pcx6FyIM-lyg81Daj-femQrH9JhBuhygNaQI2IGc0jvG4Y8r28rVbiFZrCW4wpR8NWDT3XqGMEw3g_AOPllbPds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری ماندگار از حضور رهبر شهید در رزمایش بزرگ ذوالفقار ارتش سال ۷۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/664922" target="_blank">📅 13:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664920">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fc7a470172.mp4?token=TwBLcXBGbeUOXGZjSXy3BoCpuUewQKaSqpCzBHYEPvzA8rbHxNHwU23X8s3sakREnw4bZcHDUY8yw0W3iC7puk1yrXyW_x48o0tOhq-HuTHqE0w08zvBBy-ZzThwQxygz278CGqvVyiVcAiPyoYmbU--gv8L1WtebVgtB7AOM9K0-U_u0GbhM4fm6ky9Gbay51mRvdeAo9vN-3WCTxvg9T9Q5nUj8dr4g6F8atga66k87HTxNVRt1L5PqaI-0Kp-6TDFfIidiuz1rnObApZBYNxve5RB5aEqTcHGAD1R6K6aRTj1JOK0zZDmh_lxx2MPhmlc_XDj8c5kw4Ytg7LpTw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fc7a470172.mp4?token=TwBLcXBGbeUOXGZjSXy3BoCpuUewQKaSqpCzBHYEPvzA8rbHxNHwU23X8s3sakREnw4bZcHDUY8yw0W3iC7puk1yrXyW_x48o0tOhq-HuTHqE0w08zvBBy-ZzThwQxygz278CGqvVyiVcAiPyoYmbU--gv8L1WtebVgtB7AOM9K0-U_u0GbhM4fm6ky9Gbay51mRvdeAo9vN-3WCTxvg9T9Q5nUj8dr4g6F8atga66k87HTxNVRt1L5PqaI-0Kp-6TDFfIidiuz1rnObApZBYNxve5RB5aEqTcHGAD1R6K6aRTj1JOK0zZDmh_lxx2MPhmlc_XDj8c5kw4Ytg7LpTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شب سقوط غول‌ها؛ آلمان و هلند حذف شدند، برزیل در دقیقه ۹۶ از کابوس فرار کرد
▪️
قسمت دهم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/664920" target="_blank">📅 13:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664918">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kg5YDEz05N2n583WdPicuyU0UFmR9VEU6rHOdPQhGaNwx06drZwb4bXG6KmIVf5MEA7UV8-shKsHpuVPe9JvFWLHaakIK9i5NdQNGzDyhrHPosDusbiUQUsJ_PXdEICmrtbumT5JZ4cjxBn0-Ore2LOo6UigfgiyFq01-vwZh74yAYlLXRgW_uZAwCbmL8-tMxjAglAA3sv28_p9W3Gc3ezK-p53THTMlyDb0zyBXhOfm-ZMEM8We6x0iKJb6QyOAHSUCk5QrBz4B5eerti_2G4Lb039SGR34-1NvH-gZFkCZuRsyiT9RwGVZrrLHTyxMHjM8X6vBVslWQE20kBEjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنان در کدام کشورها به‌طور قانونی حق موتورسواری ندارند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/664918" target="_blank">📅 13:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664917">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
محل تدفین رهبر شهید نقطه‌ای انتخاب شده که در آینده امکان زیارت هم‌زمان برای بانوان و آقایان به راحتی فراهم باشد
دبیر ستاد مراسمات بدرقه و تشییع رهبر شهید:
🔹
همچنین جایگاه تدفین به‌گونه‌ای جانمایی شده که در روند زیارت مرقد مطهر امام رضا (ع) و آمدوشد سایر زائران هیچ‌گونه ازدحام یا مزاحمتی ایجاد نشود. جزئیات دقیق‌تر این آیین در زمان مناسب به اطلاع عموم خواهد رسید./ صداوسیما
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/664917" target="_blank">📅 13:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664914">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
قیمت جدید شکر و برنج اعلام شد
🔹
قیمت هر کیلو شکر در بنکداری‌ها ۹۷ هزار تومان
🔹
قیمت هر کیلو برنج ایرانی  ۲۹۰ تا ۴۶۰ هزار تومان
🔹
قیمت هر کیلو برنج پاکستانی ۱۹۰ تا ۲۶۵ هزار تومان و برنج هندی ۲۴۰ تا ۲۶۵ هزار تومان /باشگاه خبرنگاران جوان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/664914" target="_blank">📅 13:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664913">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس کمیسیون انرژی اتاق بازرگانی: مردم دو ساعت کمبود برق را تحمل کنند تا برق صنعت قطع نشود!
آرش نجفی، رییس کمیسیون انرژی اتاق بازرگانی ایران در
#گفتگو
با خبرفوری:
🔹
پیشنهاد ما این است که به جای قطع برق واحدهای تولیدی، مردم روزانه دو ساعت کمبود برق را تحمل کنند تا تولید کشور متوقف نشود؛ چرا که تداوم تولید، ضامن درآمد و پایداری اقتصادی است.
🔹
به دلیل نبود رگولاتور و نبود نهاد تنظیم‌گر، وزارت نیرو در قیمت‌گذاری، سیاست‌های حمایتی و مدیریت برق هرطور که دلش بخواهد عمل می‌کند و این عدم شفافیت باعث می‌شود مطمئن نباشیم که رویکرد و عملکرد کاملا صحیحی از وزارت نیرو دیده می‌شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/664913" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664912">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
تهران ۳ روز تعطیل شد
🔹
به مناسبت برگزاری مراسم وداع، نماز و تشییع پیکر رهبر شهید و خانواده ایشان، تهران به مدت سه روز تعطیل شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/664912" target="_blank">📅 13:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664910">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPfVX4zu520_Yr4HJJ6ErCzzUKfo2slAOp3B2xgTN0hvMkbRa0yEJDuOL6q_5xdiQcLVIuAnYgkLo1m1RYIPN-u6VTiOTStyZrD2P8vYmK5vzwNmE7zPNGyPwmn8ynlLGk83SeCU1hHjnuayhHI9PrsIjTP1OP-EQDNDADuKxZhR0I45s8jIrHpt2MEiRIla5P7w09p1TxeTb1mmBCYYlqOMhxu3Fy38jfYh3g2mzHRjrYdFe2r5N3GbtDtipvdf-7QQPGOv0ZODerWVOts7qrRIc0xWFbotDP_DVct_sf8twqiqDvh96ZDlP6iAUnfwXxQbvIAdmTfWsEX9uzuJwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرونده جنایت‌ شیاطین زمان نباید مشمول مرور زمان شود
🔹
مسئولان موظف هستند عاملان این جنایت را به میز محاکمه بکشانند؛ عدالت و تقاص، تنها پاسخ معتبر به این تعدّی آشکار است.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/664910" target="_blank">📅 13:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664904">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDGOC1raNiRFzu3zHZ0YWTG49MZzfcQrSuhGJmBWNVHzDa383BdqrINeAxTPlinaDKh9lgcjnWEpwumBrPS0dDtj4YYtnLp5XvKbLk5RWiAmIFrY8IOz8bzHOp02txgaYybr0xqNni998S-lSZLLSn1_J_j844a-IOQhUiJY8jTb9zhmycVJEgin7QjXWOdlVvsH4o_sBjwFT_VJYztkZExnDNbcDVLJZMoDeF1HwXgc5AFz74zsX-fBYHfymR1I0qtr554rFHVEfgiEucga4p531jH__yeyosfBhsEN7M6TlyYgWvcHCgNyiFv2oSz0XKvsE8fr-ETaJvMbtusejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ حرکت کششی ساده برای رشد قد کودکان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/664904" target="_blank">📅 13:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664903">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8b1240f7.mp4?token=Tggjb0lhV-I_Kse0VRwBKb0rwQ89L4rWnRGyDzRIswQhHOJgko89akSNP6OsD2ZuoWSomLAP6AO_pHIjCn3IelQVHLob9Z7hX3F5OhMk4tYhNHyeHgmCL3N4tdtAo-sH9o_SFDY7miBUlaqTIRcpkFfIFFISrDQJTVBqjXIAvZuA5sN6_vloIm4yKEO4m0mpsc20vlGPneNGixOswF9E_x_t0HsTpQJeWmMQV-SssUMZ0oabU_fBDunQfpOHxdQnHvhLZxA2rxyIrNrowixQMcm5AN_qKso-5o-e_AsHW9SEvWGsy3GAEPEuUOj9BfrJcjb7zneSSuuFAMarhqraHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8b1240f7.mp4?token=Tggjb0lhV-I_Kse0VRwBKb0rwQ89L4rWnRGyDzRIswQhHOJgko89akSNP6OsD2ZuoWSomLAP6AO_pHIjCn3IelQVHLob9Z7hX3F5OhMk4tYhNHyeHgmCL3N4tdtAo-sH9o_SFDY7miBUlaqTIRcpkFfIFFISrDQJTVBqjXIAvZuA5sN6_vloIm4yKEO4m0mpsc20vlGPneNGixOswF9E_x_t0HsTpQJeWmMQV-SssUMZ0oabU_fBDunQfpOHxdQnHvhLZxA2rxyIrNrowixQMcm5AN_qKso-5o-e_AsHW9SEvWGsy3GAEPEuUOj9BfrJcjb7zneSSuuFAMarhqraHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسینی، سخنگوی اتحادیه صادر کنندگان نفت، گاز و پتروشیمی: مدارس و دانشگاه‌ها در سال تحصیلی جدید، فقط یکی دو روز باید حضوری باشند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/664903" target="_blank">📅 13:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664901">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kS7xv_47l9lkvsAHcx-hZzbewynaWzId71TQ88xJoXeFtjM07FayQKb9bVHlmGfAPSYJ2DnwrNO_Aw0Q7A5iTQ7bz5FA-9cb6aJwv21fL-UpynibNG7FpHz9lfZ_uS9Aext-ogL4a7Rs8b8ZElugna7O1mV8znNB2Y3eEfwa1VVGxccRJNDB2BT6Jjl3QH0Ce3S1tqYDyiRdSx556o_uzTXG5LGbcHIA19E5afXQA6_oQgk-FbD-3O1ZuFOpNFW5Zt69nTyYkHUzkDSDkzGdjt_o3J4vLYXehYOHZH-UngOyT36EPx17lelsLrNSC2O6dxa8wBsMrgYfWAkq6lJrew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
سوگواره بدرقه یار
▪️
از تمامی هنرمندان، عکاسان، اصحاب رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود تا با ارسال آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور در سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» شرکت نمایند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگو تایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبر فوری ارسال کنند.
▪️
به برگزیدگان هر بخش، جوایز ارزنده‌ و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق آیدی
@Badraghe_yar
در تمام پیام‌رسان‌ها ارسال کنید
▪️
برای کسب اطلاعات بیشتر به کانال رسمی سوگواره در تمامی پیام رسان‌ها مراجعه کنید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/664901" target="_blank">📅 12:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664897">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75235e49d8.mp4?token=UJuY9CICTR1JE3lGFNKEdrbv4awLlBs-aFnGU5-vy5IViIcEBjk-Ko-8sbUXa0a_tHzCfppONjGHmrHAuz2Jixq9iLM53T63xgmZTdDvt8Wjukgp71dC8LwhLhOuI43-vCMPZxrM09ZyUSF56wdWFi4s-RxSGQNSeBlWicuGHlKtvavsaLEN0JR97WL8qIIsQLDosd4vcxe35JfzL8Pdr0Y8hugzUCv4AH3IxTjUs06zkWNFI2H7fSPDtdTRo7fOkR2NYOmFDsQKWsu2XEx2uwZbyV1nLbbyM_bQqS36pL5aWsnAZWdWp190Mv0KZvuJ_fe7DdiZKgAcGmTgytEUAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75235e49d8.mp4?token=UJuY9CICTR1JE3lGFNKEdrbv4awLlBs-aFnGU5-vy5IViIcEBjk-Ko-8sbUXa0a_tHzCfppONjGHmrHAuz2Jixq9iLM53T63xgmZTdDvt8Wjukgp71dC8LwhLhOuI43-vCMPZxrM09ZyUSF56wdWFi4s-RxSGQNSeBlWicuGHlKtvavsaLEN0JR97WL8qIIsQLDosd4vcxe35JfzL8Pdr0Y8hugzUCv4AH3IxTjUs06zkWNFI2H7fSPDtdTRo7fOkR2NYOmFDsQKWsu2XEx2uwZbyV1nLbbyM_bQqS36pL5aWsnAZWdWp190Mv0KZvuJ_fe7DdiZKgAcGmTgytEUAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجات مادر و نوزاد پس از ۳۲ ساعت زیر آوار زلزله ونزوئلا
🔹
نیروهای امدادی ونزوئلا یک مادر و نوزادش را ۳۲ ساعت پس از گرفتار شدن زیر آوار زمین‌لرزه‌های اخیر، زنده بیرون کشیدند؛ عملیات جست‌وجو در مناطق آسیب‌دیده همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/664897" target="_blank">📅 12:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664896">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h27Z2rgRLtt-3tH_1s1FBEBF0tIVCt3TXyNHybVBlZHrLf4z6831plJsqlSABkiN-XwGB1sl32CvoeGK-L_S-a8T1ttDAsavm3iCsjc54sWWui_uGwL1hf4FXxPyFLnkYZC3DT5LLGJ_XcVMwxswxlkAOlMInVed5OdU3YIbjn__TS3dZVj0Mc64ypEPEpN24Hr3YFxFRCABjc_pV7nOT9uHZESYMQ18dK2j638BdGgKhuuli72yxlriYd8ku8gZWCQbcaDdWtnx5GSRxK0cJnzW4mn3onSAluXg_lUjPI9gHcQX5QZM6x90TgZLppNwaX3tMifqInhmqL26rinxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر امنیت داخلی آمریکا: پس از حذف ایران از جام جهانی رقصیدم
نشریه اتلتیک:
🔹
مارک‌وین مولین، وزیر امنیت داخلی ایالات متحده اعلام کرد که پس از حذف تیم ملی ایران از مرحله گروهی جام جهانی ۲۰۲۶، «رقص شادی» کرده و حتی «چند آهنگ» خوانده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/664896" target="_blank">📅 12:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664892">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WbWrFYIrnOPH1fVCrJYyRFfsiJbDs8XunOT0kIj4wYKYLUCWHvBeSFTOtHxJGvNbAhOHp_AzdDg8WN1Ur51_xxjNEX8riI2fSceWxKQP36vvZAClQlWzd78NIMCcniZX3mrv99_TaUqpQsrw7GRa0AbxV2vq7JqRSRHZu9ODwIuwNLtJajSkW1hjcOgs6-_9UWtOkdsBQEKUy5wRA9bw7u6KNkPCdBAjRAvdCEByyre3BRmgs2v8WNTIit9SH6z0_aB9u-Hk4DfYbqejwg-dgXQIp9UQXu6Ikg_oL74z-MGsUa0jv0f_Z4eA73dnQIFKstc4ilVf5Ojcla2UOQuoOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a7dQgteooT-dW6_34bYCSYRAjK03w5mEZoNsHNp_U7G0c4RAl4ZkY9WLuxproAXQg1xEYnHYmTxDQmeqLoZzXj9K23IA3yPahuwnBOlEkRC0N8lMZFvRFPLo3Lj4bm4E2P-KMPe5T_8vOwPDaKBDIU3dlL9UHgcfviqGBdjfLvd1ua3svWaDZDfXLzI6jdGC5HbnkZDgkd867smau5e7mbtboja4OhEefq2SnxbGRy7SE3naj1Hs79Fd3v1vk6PQJICJXBFzkkYmRIehgI5hAka8V6xvezz8pJ3b6Ymxo4IYLbhgU3aZ7byYQia07dzA0aT8IFxZJ0VNI4uBsAO9Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdxA5NVreAFqN_6Cbgv818xu8XrhGLAFVQVgg1shOPbrsnXlE6U8v3Ir51b_OHqtxmXYwBHeEnVvHCkCfGiqM5YhuL0GGREOx0CUiVfPhVsG7qfNnJJisxqsUCaS7pAb7JXlfp-gFVm8shBtQBNu82K-IAZ14tN1J71tPsLbONFoLBd_fAEfHYzQCaskDHknFN3UGVRVBMpoO87cN18nLkU0NHJ7tbY8vxxq6aW0w22KGaCutXq5W7OwFkUXIGX29yeBHflB-GpWARSRmxww7i5uWhHVJW2NUjn2ftYQpWzL29RMQ52KikHjKPI5XhvgKHi4YWL8lvUKIAvm7pgUhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VudF7RjjcXjolpSADw-BLU1Maa5yQ1M4L1rWp-OKqBqB5uptD-RyeokGfs94u7FdBO5c5xw36zWVqr_JbFRFiRjv-JWOcVjabzu0GX9qWwDo8dGkMfsE1t5LoOHVWi0BsBeaCPG0qn95U52H0aAFCK7x9e0XmCnl_RtWgdigeQQhD6xEBPrMP2hqxiUCVnWZq0pZhQ9hMTQYky23v3j2__dylGUJTbNLHK3Wwbe4u3O1aRnNAaVADB_7OzNAkesGHf1mNcTLNAa_OCDeubZ1gN6F1hBxeM5FJJlvNtEQIJy0XZ5T4STFIkPRqtTdpNqbCQAA4WJtNxm9N3TyiOBrGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رازِ میزهای مجلسی؛ ۱۲ ترکیب جادویی سریع و خوشمزه با نان لواش
😋
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/664892" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664891">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTA60Ffh_J-EKxVzfd2dWk4T6I93aEgtxndqHhMf0_HOmyY1QQPiFw4PxWhQ8P0aO0cGRoT6P0CHU22q0PAIXF4iXwKn6D13zo0neEC63Y1Gh7Re4_9yZZHM05PklAbliX8_DwFiFC8lGuQO7dm2YykWlJSJtGzmAI0Q1WAiw-j7jJGueWQJfP1ts2ELV0GolNYPQCGqXF8ENVBo6D5gixPP8ehUP8OfYB_8nOXBBpbDZG20JcBZ-GRXDSlQpuqeXLVWLhtBd1THrQysHudrDZeqgGm7Mz-w-DScati_n5DQgAWKIlcVX61m_CM3UFIcPzQXiyugCr3L79J0tzAYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تداوم حمایت بانک تجارت از خانواده‌های ایران
🙏
💍
پرداخت 4.8 همت در  قالب19 هزار و 345 فقره تسهیلات ازدواج و فرزندآوری توسط بانک تجارت در بهار 1405
🔗
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/664891" target="_blank">📅 12:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664890">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9381c0dfa0.mp4?token=fy8pNwWNnrxop0xVUY5q2_CK7si2WA_8FgPmwSorVJjyJIm4E9_IIvLgVbuGY8m0dJHoQJ11zWpCymUmTTUKb8Xx5xUWRuF8CDa0Xu2NLYSyny1ctTzot3ZJNSmMhtnBz2CCdPCnOM6x2pyN_vtscjzNLLQit0bcNX0m1fyeAwy23HSK7asPgoDP1060uyyGiMYBopzZnDcZ3nUZl5ayr8N-M9B78Pcv8dbPt5b7_s1KARH6-SVCqJWSKtho6Ua2iBfdCizKHWyYN5vYwOOeDcktxjUYUovpYgLh_F3f0q_k9KK2qTZOCvuzG6CafCpxe5_xluRSIBytxTZFudxZnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9381c0dfa0.mp4?token=fy8pNwWNnrxop0xVUY5q2_CK7si2WA_8FgPmwSorVJjyJIm4E9_IIvLgVbuGY8m0dJHoQJ11zWpCymUmTTUKb8Xx5xUWRuF8CDa0Xu2NLYSyny1ctTzot3ZJNSmMhtnBz2CCdPCnOM6x2pyN_vtscjzNLLQit0bcNX0m1fyeAwy23HSK7asPgoDP1060uyyGiMYBopzZnDcZ3nUZl5ayr8N-M9B78Pcv8dbPt5b7_s1KARH6-SVCqJWSKtho6Ua2iBfdCizKHWyYN5vYwOOeDcktxjUYUovpYgLh_F3f0q_k9KK2qTZOCvuzG6CafCpxe5_xluRSIBytxTZFudxZnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روبیو: تفاهم‌نامه با ایران فقط یک تکه کاغذ است
مارکو روبیو، وزیر خارجه آمریکا، در اظهاراتی افشاشده توسط یکی از نمایندگان کنگره:
🔹
تفاهم‌نامه جدید با ایران را فاقد محتوای اجرایی است و این سند تنها توافقی بر سر «ادامه صحبت درباره صحبت کردن» است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/664890" target="_blank">📅 12:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664889">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
امین زندگانی، بازیگر: جلوی لوکیشن، ۳ بار موشک خورد، اما به عوامل می‌‎گفتم کار در این شرایط ادای دین‏ ما است و نباید تعطیل کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/664889" target="_blank">📅 12:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664888">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZnYTkTM6SWGR1FKieQ7R4Ysv7cvEOWUSsjjJWDqVbMR_gDMkWjE5r1KelBnKqcMMVxdTMIxWORMLOO7QTfXJK6zCnFAnDxVpozfm2nNYWjqcY-HkQzfen2TVfgE6wcuPl4-_BD-gLEAfA-uLUH6UPTg5BwJX7hjUphFr3SglmSj4L4wJlT6YSp2A1XHOAAtbBEsZ-offP7ujZy2xbvkPz8W6v4J34NR3PEsOKHiPAmUkKo-FOA_L8Q4h_qj37l-eFtcZyMStvIZDvOm-b2Y_dzmo0E-UYI-KUJ5iwDMQ3Ku8Cb-B6Sk6GdqiyGFwFLqadYIYx9maoVaE1n074YrZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام تیم تروریستی در مرزهای شمال‌غرب
🔹
قرارگاه حمزه سیدالشهدا(ع) از انهدام یک تیم ۶ نفره از عناصر گروهک‌های معاند در ارتفاعات میان مهاباد و پیرانشهر خبر داد؛ در این عملیات چهار جسد به‌همراه سلاح و تجهیزات کشف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/664888" target="_blank">📅 12:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664884">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9a84eb55.mp4?token=lkAPjfI-Imt8r9fKZpTnWbSiLa-8VG96nFyB9wb-QQwXkYhvrNTyCSjNK02wKvk76hoAApFfAdJEI5TIsCrGRy9X4ma1lkGDhG6rs96XhgNXtmM4VSfJEHAIzesmeoOkpa5iCqZccA15tm2owvrk2nMFnlF5vnnjLoJjWuiwfqnYRaH_L-bIcUarhozBseUH-dMF0B07jo68rwwT6109wIU6QpkWDjoJ1vZX_deocSmCxeyWjwqDx7ap9GqX8ORj7WRTsaSWzRy4I-kB5TtRQ9qPPykfH3a236NZb3yGs-tPGWkqNCaTj1wNkD__mT7NrP55RT6_mK7QGnfX_yokHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9a84eb55.mp4?token=lkAPjfI-Imt8r9fKZpTnWbSiLa-8VG96nFyB9wb-QQwXkYhvrNTyCSjNK02wKvk76hoAApFfAdJEI5TIsCrGRy9X4ma1lkGDhG6rs96XhgNXtmM4VSfJEHAIzesmeoOkpa5iCqZccA15tm2owvrk2nMFnlF5vnnjLoJjWuiwfqnYRaH_L-bIcUarhozBseUH-dMF0B07jo68rwwT6109wIU6QpkWDjoJ1vZX_deocSmCxeyWjwqDx7ap9GqX8ORj7WRTsaSWzRy4I-kB5TtRQ9qPPykfH3a236NZb3yGs-tPGWkqNCaTj1wNkD__mT7NrP55RT6_mK7QGnfX_yokHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر ستاد ملی مراسم وداع و تشییع رهبر شهید: چهاردهم تیرماه برنامه نماز بر پیکر مطهر رهبر شهید انقلاب اسلامی و خانواده گرانقدر ایشان در مصلای حضرت امام خمینی(ره) در شهر تهران برگزار خواهد شد
🔹
مراسم اقامه نماز بر پیکر رهبر شهید در قم ۱۶ تیر برگزار می‌شود/ نماز توسط یکی از مراجع تقلید در مسجد جمکران اقامه خواهد شد
#بدرقه‌_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/664884" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664878">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
اولین شگفتی جام در دور حذفی/ پاراگوئه، آلمانی‌ها را به خانه فرستاد
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/664878" target="_blank">📅 11:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664877">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b1531e58b.mp4?token=pyxOGeV1_J-hLz-a5YBVy5fon-q2x4dQ7wDfSDOzMtQltjfEGxL9nxA60RtjNz3qn52Jk7DAAcuqTeeaCYM7to4lQouEKjb_ZPxDoRZP3rTVP1SLfLJg-P9rdmkXEiZmHsyrr6yqSY5ytBYWDMFQFafECWarpUXMtc8V53y3XsZROmEiP6AFeYh7u_JYENDnXjC3DS6CZHSPbukDqX3UMlGA0d7Pa4ba845_Ky8CHV8yoPgnJEtkUG5SiOJcmaI3VrB57r53xu6zhKfyN5MchgRAWAjhsyXEYKPfzecS07O8dx5B6lgf5VQhAN6x8G7ci3rdX9Oah0vLqwMtoaD9og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b1531e58b.mp4?token=pyxOGeV1_J-hLz-a5YBVy5fon-q2x4dQ7wDfSDOzMtQltjfEGxL9nxA60RtjNz3qn52Jk7DAAcuqTeeaCYM7to4lQouEKjb_ZPxDoRZP3rTVP1SLfLJg-P9rdmkXEiZmHsyrr6yqSY5ytBYWDMFQFafECWarpUXMtc8V53y3XsZROmEiP6AFeYh7u_JYENDnXjC3DS6CZHSPbukDqX3UMlGA0d7Pa4ba845_Ky8CHV8yoPgnJEtkUG5SiOJcmaI3VrB57r53xu6zhKfyN5MchgRAWAjhsyXEYKPfzecS07O8dx5B6lgf5VQhAN6x8G7ci3rdX9Oah0vLqwMtoaD9og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو پربازدید از تست ترشی توسط پیرزن خراسانی
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/664877" target="_blank">📅 11:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664876">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPX2bK-y3Ykv-uc9MdjP-zbBamBAI_3JB4hieoBrBoDx0bXBCuwvEbyCH2GfVO2ti24kdNJsHnoSNEQiUSiTQkH7GI1uOZ6HNLGvjU1RWzDwXKvpVAjj_9XuJ3PI1aqn7EQmIrl0DO6g2iylywuYgxqhb-Siy9FplhQzS_fXS4Qe-Ja655P-D_Vh0ejoXheT7yQif1HdC6ikBk4NViCMQRI9Xb3642P_UY2BL8MMcKwfTaQZn46Q6hww8ALB3emzOGlfbXplz1r27bEMyF5TrpOZA4mx-VnY8wb6iyv1cEWhktO2DJO-O0xL1ppzgtNE8J0TOCjJr-MQaKxXL7wKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی برق می‌رود، دخل مغازه هم خاموش می‌شود
🔹
قطعی برق فقط خاموش شدن چراغ‌ها نیست؛ برای بسیاری از مغازه‌های کوچک، یعنی توقف فروش، اختلال در کار و خسارت روزانه #برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/664876" target="_blank">📅 11:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664873">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DedkrrO7hhqBLju9up9270X_yXGkiNI2nSd4MqJF6ioNJ_nNvU2hZybezWpUDqXfgQJsSXOhYwzM9wj5R8Q3P2KJXMJV6DzhIMIIy4ZBsYEzorDB0OZCJadRCS6NvFOpUpuPVS7kD496V-WUWUE9udHTmcvoCFcRWqGwdwGmY2ChnXGlN2WD98FwF49TuGTHBYiZcwo1umTVT3JeY_1r3vGo8uo9oUYJsQfjyRG9R9kDSsbozOjTlQDfGLWzVX06tyE4IlaoX_WN05sb_hKXZSebjxmBpYDCly8qWqs7IncYv1GqWowdOBbOqU336Ml2sRvFVYvPTXhsUlVWuFDUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهی یک بدرقه تاریخی؛ تجربه‌ای شبیه پیاده‌روی اربعین...
🇮🇷
🔹
اگر قصد شرکت در مراسم تشییع رهبر شهید را دارید، پیاده‌روی طولانی، گرمای هوا و ازدحام جمعیت را در نظر بگیرید و با آمادگی کامل راهی این مراسم شوید.
🕊
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/664873" target="_blank">📅 11:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664871">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_qIJhtL1niLoejC7M3xwnNZpecWmBFkgYZy5v4qI_xqHwQo4DfRxQFNS1d054kVpnYeGKVq6xC-fko7lTo9atAK602rPf1YPeKa0IR4QAEXhEX-ggzoH54-rTw0OIUjwQ_BTIrnotMVZ7IpZxzOJGRA_Mmx3P8gV9MJuwVSkw1IBEc4uTR7YVdokq-wdC9aSgS018CPPnQyMVX34wvkhIHPgR9jVrZJDTegxQrd_1n50_OqgFZ9nX-E-ERv8BPe8yZUT2ZfwZSc09SqcpEhwehrMM16lFR9Z73gekqdxkNrkOiCH8eRMuljsR9ZTHeK-w2UEI0YyKBGu9XJRBpezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرزاد جمشیدی درگذشت
🔹
او صبح امروز بر اثر سکته قلبی درگذشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/664871" target="_blank">📅 11:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664870">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c592c0d3d4.mp4?token=n-Kh6hXsU6zGmNW8IHxsLSS9mo8UK2g3G_g5vlqSvQYw6N6WD-haDDTarILFHFYkyYiiBFs9eiPCl9GyWFmbUjNVgWHkXJAZzPKc8Zl9wJJXSSRw58Li4x4gr3fuvPgQ-yDm7ImnONUnYj86fNfXZCZhxiy3tBVf7Iv7d6y3p9bXoL3RDNl_GHh_5rOtPJs2RNE93E8p4iQO0lfVE8xlODUypPqW0pAX_sl0slTV9QApLQLD-mrvTORfcDb7Jin5C31pUD1HKahXuMS1auziy-gA6LoWNF2s3FezU6SeC5rl8arSBz2yS-QjTLv2sIXa6JnJuNh69fGQtXTn52whxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c592c0d3d4.mp4?token=n-Kh6hXsU6zGmNW8IHxsLSS9mo8UK2g3G_g5vlqSvQYw6N6WD-haDDTarILFHFYkyYiiBFs9eiPCl9GyWFmbUjNVgWHkXJAZzPKc8Zl9wJJXSSRw58Li4x4gr3fuvPgQ-yDm7ImnONUnYj86fNfXZCZhxiy3tBVf7Iv7d6y3p9bXoL3RDNl_GHh_5rOtPJs2RNE93E8p4iQO0lfVE8xlODUypPqW0pAX_sl0slTV9QApLQLD-mrvTORfcDb7Jin5C31pUD1HKahXuMS1auziy-gA6LoWNF2s3FezU6SeC5rl8arSBz2yS-QjTLv2sIXa6JnJuNh69fGQtXTn52whxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درب کارخانه‌های خودروسازی را ببندیم و کارمندانش را در هتل پنج ستاره اسکان دهیم، خرجش از این مبلغ زیان سالانه کشتارجاده‌ای، آلودگی محیط زیست کمتر می‌شود؛ مردم هم راضی‌ترند
/ مدار
گفتگوی کامل را در آپارات ببینید
👇
https://www.aparat.com/v/jmrz2dg
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/664870" target="_blank">📅 11:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664869">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vbg315yeLkVrBy8nmQqoGCcXF8bDLjs-erWiAhb1nu27myvR9Usl7Paj9YYIz5W831t1KiZjAmPSa-tci0VKgoyyHtXl81F_mtC-f7RFgAA_The7Do8TGdAiKS7qf_AoctArNEfg3xf1P84kgGexGt8bBIKtc6SzI0sPUkcWp4r0JuZm50UmoOpVEnBEf9XaA5pnp6eFb3hTzIiKIlpe5czddf7ROC-khTNi14a8Pol1eQtwRN6zfZKnQBIAmzSDMXSlDU5cJJvRepQNafpJngfESomEz3RAeGPCth7a08oLlRmRAElWq28DwHoknYBaROyXINupjbRhiKBCEPFvqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه مترو و بی ار تی برای روزهای وداع با رهبر شهید انقلاب
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/664869" target="_blank">📅 11:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664867">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
نفس سامورایی‌ها در لحظات آخر برید/ شاگردان کارلتو به سختی به یک‌هشتم رسیدند
🇯🇵
1️⃣
🏆
2️⃣
🇧🇷
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/664867" target="_blank">📅 11:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664866">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9454900b44.mp4?token=euApx-CN_KWmtjo4qoZVYOS9fGPHCAQ5_Cm_I1gj_SkOWJVPalYG005Xi0y08YPfOUqb7XKj1f78xYYRD5H4Zg1ygycw0JhWs5G0qMfom6IEMXLvO1tf1IzYXKVxBgaYfwMKLIf_DmsCcuc09R6pnuDeBSSTSI13zaQr7nyt3nt0wc_XkaKJuA_wvDAe0VUu_uOdpH-Tb4UamkqEOCpZCvY4GxQIFjnk8VTVhXUSeoG1gZsIujh5MvDY3-Efqap6cbWirO7BsE2SMTJk9tpObNWefX5hW81WXTJWCxv80apO6BmRskKBSYbsUC1HJbQqG1RJezaqkAfsc7zGWhp-GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9454900b44.mp4?token=euApx-CN_KWmtjo4qoZVYOS9fGPHCAQ5_Cm_I1gj_SkOWJVPalYG005Xi0y08YPfOUqb7XKj1f78xYYRD5H4Zg1ygycw0JhWs5G0qMfom6IEMXLvO1tf1IzYXKVxBgaYfwMKLIf_DmsCcuc09R6pnuDeBSSTSI13zaQr7nyt3nt0wc_XkaKJuA_wvDAe0VUu_uOdpH-Tb4UamkqEOCpZCvY4GxQIFjnk8VTVhXUSeoG1gZsIujh5MvDY3-Efqap6cbWirO7BsE2SMTJk9tpObNWefX5hW81WXTJWCxv80apO6BmRskKBSYbsUC1HJbQqG1RJezaqkAfsc7zGWhp-GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پروفسور گرگ سایمونز، استاد
دانشگاه و پژوهشگر سوئدی: آمریکا یک امپراتوری در حال زوال است و توان شکست دادن ایران را ندارد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/664866" target="_blank">📅 11:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664865">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
| فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/664865" target="_blank">📅 11:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664864">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDsZkiybF5I7UfkvHub0zCg9YCXIv_BCFHxyVuP-GNT2Wwd9tJ2tNNpk4XDW43UF85z4sw7t24C85Kq-myZRYEGsfI_ohyfcpo8pi2_oniZfKe-y3ZnzQNX3RS0c-qwrYfLKY4HWTDzsvfk0Inr8xB5EjduIlnzOoXKkLZEVQViKsxmpEwbRYriiXmg45TJHu4fq4LyyyvIDk7NAQD-kSHpkxu3JRGPLZPZyQ1VmuO7I2UzyzfVwvAvGhTrpj9G_PfGLdKUsmd4c4o-CimiZe0BkvQxdjtWahNgOmx1BclZicJGQyy1esITNboyfBL2cbx5GIY2jIQNbsbHJ4IRDXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعویض به‌موقع قطعات خودرو را جدی بگیرید
🔹
تعویض به‌موقع قطعات مصرفی، علاوه بر افزایش عمر خودرو و کاهش هزینه‌های تعمیرات، ایمنی رانندگی شما را نیز تضمین می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/664864" target="_blank">📅 11:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664860">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzasCjLt4gSC7zlRK5IMEhrDpnDRnj4yIdaRX-b2sdev-nE5dptkTYJcGy1Q0pAv3I7QAYgmAoN1dm5CeR7FXTOJ28vOAdqn1kiB1wZ6tGe0P9PhKFO9sSK3q_07_effEc6PHcFHlOdsrV_VQj3iZeesbTl27TCx_el2pTTbzCDmDz5E_YDcrBuHSEpJOsRKptbRCB6eanfX37mBNyaaGLe7eQrvllLyOAeb8qtdDBhFpDyH_RX25UhOIUVcAyAhvUDbdEFtpuWGIFyO9rvw9btlby8C-NY4q2toJs8sgKE20EeraVBf-dR3HfBHzAw791EVsqWAd_tH6I3b1vJN0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این روزها که جنگ خبری و رسانه‌ای اوج گرفته، این ۳ کار را تمرین کنید تا فریب نخورید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/664860" target="_blank">📅 10:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664859">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316b8b1ceb.mp4?token=OIqLoL8tz69HhkHUkoOO_f5R2q73FkPBK2xPFx5lYnKCFcji8iefhLiQCFCaoE7O9LDpBd_Ezl9-chALFnzKTniYYjjebG2RCC8TSPFEG7hr4ccbKmC-h8ZfcaohZp91eCGR4-wxyHhQw2VECA6-SMi0go3kt5YUI7w2LZGaOSXsNZKhJx2POmoJHKWWD1jrjbzHtmjvdABDwxou53C8EgqYIgqVGvq3ztM6Xk7vX5u3AaCjp_fRSjTGxB8w5fNDC6xkGFc6lvsEF42Mz_iFTUAxgFv7qYUuK7iSPCrxrfTlc8bboWOsfdZfPyGvVfIMkMdPelFFwlCcU_Dp6gy4LmD3ZnPJ9Jw5UhBdgRaEl6RKo9pP40JD1qF9lHWCVzKKoX1RqbgJrJFe6Hft2pKHK1OG7Q_Z18hWLKYfvTzXMAC7fnI4BQzFoZhN9XpO2iB2kBvpTfid50QZA4SggCgfIwc65OLT-wcC_bI0c83J4fckvr6tXX1pc67mmVYGpSMC0tkdwdTiY7g851xqTCZBStIS6SbymAZILZGGNgCHUoCkKHSpQAYVXVOi5vgESV5RXD1Mau-lxhFM4-OJBWqS8ev1jFJO1edl_m0GkiGwVmjVEv4pZrWNC8KrZ4R3QwhisNFdWsH8iuHDEtS3rBImXTJ8m99jQ_hBl4dHiobuVdM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316b8b1ceb.mp4?token=OIqLoL8tz69HhkHUkoOO_f5R2q73FkPBK2xPFx5lYnKCFcji8iefhLiQCFCaoE7O9LDpBd_Ezl9-chALFnzKTniYYjjebG2RCC8TSPFEG7hr4ccbKmC-h8ZfcaohZp91eCGR4-wxyHhQw2VECA6-SMi0go3kt5YUI7w2LZGaOSXsNZKhJx2POmoJHKWWD1jrjbzHtmjvdABDwxou53C8EgqYIgqVGvq3ztM6Xk7vX5u3AaCjp_fRSjTGxB8w5fNDC6xkGFc6lvsEF42Mz_iFTUAxgFv7qYUuK7iSPCrxrfTlc8bboWOsfdZfPyGvVfIMkMdPelFFwlCcU_Dp6gy4LmD3ZnPJ9Jw5UhBdgRaEl6RKo9pP40JD1qF9lHWCVzKKoX1RqbgJrJFe6Hft2pKHK1OG7Q_Z18hWLKYfvTzXMAC7fnI4BQzFoZhN9XpO2iB2kBvpTfid50QZA4SggCgfIwc65OLT-wcC_bI0c83J4fckvr6tXX1pc67mmVYGpSMC0tkdwdTiY7g851xqTCZBStIS6SbymAZILZGGNgCHUoCkKHSpQAYVXVOi5vgESV5RXD1Mau-lxhFM4-OJBWqS8ev1jFJO1edl_m0GkiGwVmjVEv4pZrWNC8KrZ4R3QwhisNFdWsH8iuHDEtS3rBImXTJ8m99jQ_hBl4dHiobuVdM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پخش بخشی از وصیت‌نامه منتشر نشده رهبر انقلاب در سال ۴۲ برای اولین بار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/664859" target="_blank">📅 10:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664858">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srsOs3Y8W3tq0BkENjKVcnwCVmsCtrASPyEuYnQ5WgGoUhFMvEydL4I9jwYcFwCLq_saxwNXpHMVG61byIFY4h8VcrWvnJQUYRyiWYeNluUniYhPL3sO3emAjOAqhKnFIOtiHypUxhGbkeI7nijIonVMYLVtqanPCcJR9X_zssKlmcfZXgwshy6PlNotmmn-nYslSOsGhYBVEi-lF5V21NaDtR7ZtkDDFfNhbogjl0Iv-5-Cpvb97tGDNXOFNUJ3CzbXdVvIJ01SG9Sv5iQE1vS95JxOaA4GybuUzZnbUDo5rQkNG8G-BA2BdSg94AA2qvvlUcp_UxXsxi-t7THVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز عملیات طرح جامع پایانه مرزی نوردوز در آینده نزدیک؛ توسعه مبادلات تجاری و ترانزیتی ایران با همسایگان
‌
🔹
معاون وزیر راه و شهرسازی و رئیس سازمان راهداری و حمل‌ونقل جاده‌ای در جریان بازدید از پایانه مرزی نوردوز در استان آذربایجان شرقی، از آغاز عملیات اجرای طرح جامع این پایانه در راستای توسعه مبادلات تجاری و ترانزیتی با کشورهای همسایه خبر داد.
‌
🔹
رضا اکبری گفت: با تأمین اعتبار حدود ۹۰۰ میلیارد تومانی و تعیین پیمانکار و مشاور پروژه، عملیات اجرایی طرح جامع این پایانه پس از ابلاغ قرارداد و در کوتاه‌ترین زمان ممکن آغاز خواهد شد.
‌
🔹
وی به اهمیت راهبردی مرز نوردوز در توسعه مبادلات تجاری و ترانزیتی اشاره و اظهار کرد: توسعه زیرساخت‌ها، افزایش ظرفیت پذیرش و تسهیل در  تردد ناوگان حمل‌ونقل کالا و مسافر از مهمترین اهداف اجرای طرح جامع این پایانه مرزی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/664858" target="_blank">📅 10:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664857">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af34e16564.mp4?token=N2ioBhIiON2BhjU2uoa7m8zuATxMA0MI4RIAwn1N_dyze_6W7xzTDNddLAo64hTdyDzFKh8pmpYsx5sSKPmkr9KPA63LPagAl9c_qfv2WERWE_vfX22xZibzGePfNNZM-Z8CKOPGIuHVtzeYeBLhaIDUydUJIFf-8u6p0Z76NrnlGfc9BMLFT3XlJKygah1zhI-atVbrVEfA-CXof5mOkdSiV4wRyvImlJKpslXDi9pbZdN9U7c2csctWFzCvju7bScOuSqtkgqt2EQPCicVKvk0MO-z8GzWDlD9ykDFJtuvcqwngmKzcsTQyrG44zAsbRxJAdSpVJX0FwU_ZpqiEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af34e16564.mp4?token=N2ioBhIiON2BhjU2uoa7m8zuATxMA0MI4RIAwn1N_dyze_6W7xzTDNddLAo64hTdyDzFKh8pmpYsx5sSKPmkr9KPA63LPagAl9c_qfv2WERWE_vfX22xZibzGePfNNZM-Z8CKOPGIuHVtzeYeBLhaIDUydUJIFf-8u6p0Z76NrnlGfc9BMLFT3XlJKygah1zhI-atVbrVEfA-CXof5mOkdSiV4wRyvImlJKpslXDi9pbZdN9U7c2csctWFzCvju7bScOuSqtkgqt2EQPCicVKvk0MO-z8GzWDlD9ykDFJtuvcqwngmKzcsTQyrG44zAsbRxJAdSpVJX0FwU_ZpqiEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزی روزگاری نوکیا
🔹
نوکیا N95 در سپتامبر ۲۰۰۶ معرفی و در مارس ۲۰۰۷ عرضه شد. این گوشی پرچم‌دار چندرسانه‌ای نوکیا با فروش بیش از ۱۰ میلیون دستگاه یکی از موفق‌ترین گوشی‌های دوران خود بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/664857" target="_blank">📅 10:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664855">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fb57cd5f5.mp4?token=MjAAyHzd5JXn4K42-PmwPv85nYnPlwZBelADitzz_UCoibIsNEETtx_pJtPwXx-GHLi8AgqL00F1JZSsnaWxjz2R1aTHc6xWoj_fEpcLQhb53GMzIaiQOI0AR59lcznvu9LEP3FJb4lg2ef2FZ0QWt8iyqcFaFSlQieFV4L9P7ZD8kp_hFqtlMq6nccqa4sxWE_pnnUy2FRjbeCpN5XqSHUqAokQEql7vZHYi1-caRzUlMKjnsBhugIFOAJ9DJu2RbWWqMFPuIiwWYbPhSleQmW8GaE-Ee4Cexjyayox_20LTRrE431UWAwhzGvvKChe_cdOqOM-ygzCBvGvaRjYxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fb57cd5f5.mp4?token=MjAAyHzd5JXn4K42-PmwPv85nYnPlwZBelADitzz_UCoibIsNEETtx_pJtPwXx-GHLi8AgqL00F1JZSsnaWxjz2R1aTHc6xWoj_fEpcLQhb53GMzIaiQOI0AR59lcznvu9LEP3FJb4lg2ef2FZ0QWt8iyqcFaFSlQieFV4L9P7ZD8kp_hFqtlMq6nccqa4sxWE_pnnUy2FRjbeCpN5XqSHUqAokQEql7vZHYi1-caRzUlMKjnsBhugIFOAJ9DJu2RbWWqMFPuIiwWYbPhSleQmW8GaE-Ee4Cexjyayox_20LTRrE431UWAwhzGvvKChe_cdOqOM-ygzCBvGvaRjYxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در
مزرعه پسر یکی از نمایندگان زن عراق میلیون‌ها دلار که در زیر شن‌ها دفن شده بود، کشف شد. همچنین تعدادی اسب و خودرو مدل بالا نیز توقیف شده
است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/664855" target="_blank">📅 10:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664854">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
اعتراف دبیرکل ناتو به همکاری با آمریکا در جنگ علیه ایران: هزاران پرواز از اروپا به سمت ایران بلند شد/ آمریکا بدون اروپا قادر به انجام این عملیات نبود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/664854" target="_blank">📅 10:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664849">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f41fd695a5.mp4?token=hvbb5Oz23Skdj3FjHQVDUUVxJdEVKFWp96jn8mdKrP80GdQ_9EOJrOM1N5ITH10ZFDXITF7oaZFu9QRt2-bQiS0iXxX5JSY0mt2uMyrynfisRb9JeDmOg08rBoAmcLZ2SczXjTTmqKmCbo3T4G8jARKCH4WMiVh4iKAEmikOXMZaENODGqfofiQnA7oltXKe8MYwXNHzyQzRyZjeh28Wjkt0JfmqFiMgIj2a2EgpztYsw86ddlYv8UsbjwSrPZIReelgOcO4oC-EuYvKKW3P2dKZyMD2qp0Y8ZdjHhocYCYCHombjJCznSK4ALUR7N_Qq1vA1h3pVaxT9HGP15KveA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f41fd695a5.mp4?token=hvbb5Oz23Skdj3FjHQVDUUVxJdEVKFWp96jn8mdKrP80GdQ_9EOJrOM1N5ITH10ZFDXITF7oaZFu9QRt2-bQiS0iXxX5JSY0mt2uMyrynfisRb9JeDmOg08rBoAmcLZ2SczXjTTmqKmCbo3T4G8jARKCH4WMiVh4iKAEmikOXMZaENODGqfofiQnA7oltXKe8MYwXNHzyQzRyZjeh28Wjkt0JfmqFiMgIj2a2EgpztYsw86ddlYv8UsbjwSrPZIReelgOcO4oC-EuYvKKW3P2dKZyMD2qp0Y8ZdjHhocYCYCHombjJCznSK4ALUR7N_Qq1vA1h3pVaxT9HGP15KveA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول مراکش به هلند توسط دیوپ/ مراکش با حذف هلند، ‌حریف کانادا در یک‌هشتم شد
🇲🇦
1️⃣
(۳)
🏆
(۲)
1️⃣
🇳🇱
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/664849" target="_blank">📅 10:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664848">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa6f773f03.mp4?token=ksAeDuauS1Uq8WmNGDUNyzdE7ntzD-VDsp3jQnCvThSSWG0i-AS7j8H6h5HdIFjpumdT9Zn6t84vo8Q2Y0QDAiL1r2Nwv_tINk6rx4JfwHH3jcy2qNekBQsvRtP1jIEzl_A9uXx--0gQ0x8ieLaV_hxP9FWpEY4E7AVe83PWR9UhN2Vtbzp5UzjbQWaObN9PlmG8NZKi20X8caVJv-j0lJb2IfPi3MiOimWg7sZ39rkgbdGa4NIOP_xasr3v5JH-HZysjeOA65BumJyfe9Vdwime66jKpzwrBeYB5fL4sdq6BoXO8LxX6udqp-ZMP-0jcVDZ02fAn4H6vQQOr3U8Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa6f773f03.mp4?token=ksAeDuauS1Uq8WmNGDUNyzdE7ntzD-VDsp3jQnCvThSSWG0i-AS7j8H6h5HdIFjpumdT9Zn6t84vo8Q2Y0QDAiL1r2Nwv_tINk6rx4JfwHH3jcy2qNekBQsvRtP1jIEzl_A9uXx--0gQ0x8ieLaV_hxP9FWpEY4E7AVe83PWR9UhN2Vtbzp5UzjbQWaObN9PlmG8NZKi20X8caVJv-j0lJb2IfPi3MiOimWg7sZ39rkgbdGa4NIOP_xasr3v5JH-HZysjeOA65BumJyfe9Vdwime66jKpzwrBeYB5fL4sdq6BoXO8LxX6udqp-ZMP-0jcVDZ02fAn4H6vQQOr3U8Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خطاهای شناختی در یک نگاه #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/664848" target="_blank">📅 10:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664847">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kp8C97t-43EJ1sUhiU8oYHeu_P-dFUIND8ht6Phg81Tlwbj8Qki2fTxXOitQer-En0hH5OUIAlXqoKluqF4pfhahjsUq-rLIaOqwcidHrkgdJWDEqIA3rX5W1gx6tdRiKOUHTz7pIQ-EdSdMLVJdAd6rjex91EZOSD-5Kc3bj9jHjK9vZkgkRa3V54ZYogrXpf8MG5-3KYV_YN8ZUH4PC55br2NUImZVAOw75wx82qglZc36cumEkJ9uhkUDGY3Y04MRSqYXCwHXMQhk6CxrEmR7HDBrjdT4z1ty36wo1-LuAQpKXvMCwhPXEgDC3uM7N04girvhKY1qdfjb0kDENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نامه زیبای جمعی از ایرانیان مقیم خارج از کشور به تیم ملی: اگر صدای بی‌احترامی از عده‌ای را شنیدید، لطفاً بدانید که آن صدا، صدای همه ایرانیان نبود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/664847" target="_blank">📅 10:11 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
