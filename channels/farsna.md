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
<img src="https://cdn4.telesco.pe/file/fogeeeXndhxjkGs-GzOht5B7gFZYrvaeD_tkztzLFC_YSf58gBERtqi3c59FvbhdFgjMIxv6igspPGf97tRaHtwIo2WHX7BnGwAvFnvCpBEPRa2HcZFHNpYbDwMBiqM75DnE9zLfFbAnm_jfro79RU76rxPfXVo09ZiJi8dMSEMoodgFPtuttikzBWgipQOH21TOm8lwHQ1xQkP4fTjZmMa9gg0pFUOi_cpkYApy0DCSbtYY-aobFuImbzJiRYtQ7Xf_ccDLlpZcYGdNF2CDqi3FDkoywQy14IyJIUYsZ6MfMq-gUHobi8kWWHqcR1IWX3PkWROIahWRbLuwqngV_g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 18:28:11</div>
<hr>

<div class="tg-post" id="msg-442313">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خداحافظی با رفت‌وآمد بین سایت‌های دولتی
🔹
وزیر ارتباطات اعلام کرد اجرای طرح «زیست‌بوم‌های دیجیتال دولت» از ماه آینده آغاز می‌شود؛ طرحی که قرار است خدمات پراکندۀ دستگاه‌های اجرایی را در یک بستر واحد تجمیع کند.
🔹
با اجرای مرحلۀ نخست این طرح، هفت زیست‌بوم شامل مالی، مالیاتی، انرژی، سلامت، تجارت فرامرزی، زنجیرۀ تأمین و مهاجرین و اتباع به‌صورت یکپارچه در دسترس قرار می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 625 · <a href="https://t.me/farsna/442313" target="_blank">📅 18:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442312">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8535b8b7f8.mp4?token=EjxpZ2Y95T2k-4lfD-5siJUV11pJi_IBdkx_ea21tYrE8lc9MJGf2yRy6VErqZ-4zXXqyMbq1owp-tp5zTG3PoK3Ay5Wo_eIoDHm7_QmPTQIA6Fwpzit6nE57yYXe0EtJLaM69c36FKEEfFNd6NRMKiOM6wamje5vD-JS3e-fGt8kdvR0t8OMUoXE5ULb04RAbhe499gAVeNYZ-uM6rOcpk4J4JdJoEUBN6Yd4__JzkhnOzwksOV_OYtXNKTVmlCIL0pcWiaU-2hlSmGP3ONolLJLEfY-__J2wL4vXgnNzpiIKr4aLhdm97BglBgreMFYEAESwbpzJaGwy7ffE7S4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8535b8b7f8.mp4?token=EjxpZ2Y95T2k-4lfD-5siJUV11pJi_IBdkx_ea21tYrE8lc9MJGf2yRy6VErqZ-4zXXqyMbq1owp-tp5zTG3PoK3Ay5Wo_eIoDHm7_QmPTQIA6Fwpzit6nE57yYXe0EtJLaM69c36FKEEfFNd6NRMKiOM6wamje5vD-JS3e-fGt8kdvR0t8OMUoXE5ULb04RAbhe499gAVeNYZ-uM6rOcpk4J4JdJoEUBN6Yd4__JzkhnOzwksOV_OYtXNKTVmlCIL0pcWiaU-2hlSmGP3ONolLJLEfY-__J2wL4vXgnNzpiIKr4aLhdm97BglBgreMFYEAESwbpzJaGwy7ffE7S4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امام رضا(ع) با آئین اذن عزا به استقبال محرم رفت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/farsna/442312" target="_blank">📅 18:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442311">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5HdhaFTfG1tSTyBNFJEgR9mtJ6CZ0_P-MKy1yCF0D2dcP7jxBYhNA_JlYhWkSw8ULjHQ7SisypAy_g1MXfSqnln-0innFSeL5z9sQrnv18_17OlyvNtUW97Or-q7QHp6KuiGFMzbyEuBDO24aXuIwjRlO7s3t0MEqPuZrGKc6jA22JPtdq2PgE0l27mCbBbK3tasc9eLo4NIK32m53ri6c9zLYc4Xk8NlUHN2F-1y5vnT0aeLfhIryr4EI2eSA1cQnMk4hd9jqC9SHKQ59167G-LfVSJiRKc8WFAI4h7JaJxROzTzR0ZZ0gW76Oc6KlMS0qSffzdAJHF2oVYbXLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اینفوگرافیک | روایت نقش‌آفرینی بانک صنعت و معدن در توسعه زیرساخت‌های انرژی
⚡️
۴۱ طرح نیروگاهی، ۸ هزار مگاوات ظرفیت و سهم ۱۰ درصدی در تولید برق کشور
🔹
بانک صنعت و معدن با ایفای نقشی مؤثر در تأمین مالی پروژه‌های نیروگاهی کشور، از اجرای ۴۱ طرح در حوزه تولید برق حمایت کرده است؛ طرح‌هایی که با ظرفیت ۸ هزار مگاوات، سهمی ۱۰ درصدی در برق تولیدی کشور داشته و گامی مهم در تقویت امنیت انرژی و توسعه زیرساخت‌های صنعت برق به شمار می‌روند.
@Farsna</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/farsna/442311" target="_blank">📅 18:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442310">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt5IAQ6unVBTTVEcM6tymEaCbwCdhHfmoXxvJ55cLxMkTRKjLdtzDlhgU1-mxcKS6TIDXaS1DYot44ibtY4ShPz104mEB3Umoae8qZmgSx2uH4qIjvN56SXDQQSLkK73-Fepc8QdaJ3FLGbEGw3oOZTJ_9R5vl8pYJfTKSXFeSEPM0PxbcBt-5XnfbWuEW3Ii8OohWD228gVKbCdQMIgusoCBlONPDX_O8ZueN6zirfRWN3UuwhAtihMvABF3Y1AUJsvb0VDQzj9jkVYIoZPKmChleHQRh1wuqv31ic5YiCzelI6v9FMOS57NcWZGJK8nZq4SNDYsyb4aW4igVphXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
در مدارِ آینده؛
🔰
دومین شماره مجله «عصر مس» منتشر شد
🔻
دومین شماره از دوره تازه مجله الکترونیک «عصر مس»، روایت صنعت مس ایران، منتشر شد.
🔹
به گزارش پایگاه خبری مس‌پرس
، این شماره با یادداشت دکتر سیدمصطفی فیض، مدیرعامل شرکت ملی صنایع مس ایران، با عنوانِ «مس؛ روایتی که باید گفته شود» آغاز می‌شود؛ یادداشتی که بر ضرورت روایت‌گری ملی از صنعت مس و نقش آن در توسعه و آینده ایران تأکید دارد.
🔹
در این مجله، با بهره‌گیری از روایت‌گری، رویکرد چندرسانه‌ای و طراحی تعاملی، موضوعاتی همچون تولید، طرح‌های توسعه‌ای، بومی‌سازی، مسئولیت اجتماعی، ورزش و روایت‌های انسانی از زندگی و کار در صنعت مس مورد توجه قرار دارد.
🔸
دومین شماره این مجله به تاریخ خردادماه ۱۴۰۵ را ازطریق لینک زیر دریافت کنید:
👇
https://media.mespress.ir/d/2026/06/14/0/15451.pdf?ts=1781420523000
#عصر_مس
#روایت_مس_ایران
#StoryMag
@mespress_ir</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/farsna/442310" target="_blank">📅 18:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442309">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/farsna/442309" target="_blank">📅 18:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442308">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۶۶.pdf</div>
  <div class="tg-doc-extra">3.9 MB</div>
</div>
<a href="https://t.me/farsna/442308" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۶۵.pdf</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/farsna/442308" target="_blank">📅 18:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442306">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGM5FrAzG_Opho9VhPXEyiOUdgxuYx6UBIdsbavAlkbRAPXOA2ijv5WdUeTFFuuj93oqhco1qTMAt572ZNHBY6Dt8B0H_A1YbPLDA84HXfBbhGuNgw4WEydVtUpAdVkG4Ezt7rwtwL-TKfl0IFFwfGfJz7RLY4eqnC7jc4KjNmZdwrbrVEVHAl7MHfFqt8ALhz6oGWaptD8l628V2Ouw9JtCiUHWAWCs8lyfst8XuzS8yipvaVBHs34JzFokBzW5yB4WVxuQSKzl-x6u6DbgJXOFyCrc7Zs5-oRrDc8sVAgcW5k6LdlfbN64SXoWJ_X7zauCCX8h5QzpDdD4ERFPhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام تو به یوزهای ایران در جام جهانی چیست؟
🔹
ساعاتی دیگر تیم ملی ایران نخستین دیدارش در جام جهانی را برگزار می‌کند؛ مسابقه‌ای که برای ایرانیان، فراتر از یک بازی فوتبال است.
🔹
اگر برای ملی‌پوشان پیامی دارید یا می‌خواهید حال‌وهوای خودتان هنگام تماشای بازی‌های ایران را با دیگران به اشتراک بگذارید، متن، عکس یا فیلم خود را با هشتگ
#میناب۱۶۸
در صفحۀ فارس تعاملی منتشر کنید.
🔹
همچنین می‌توانید پیام خود را از طریق پیام‌رسان‌ها به نشانی‌های
@Interactive_Fars
و
@fars_ma
ارسال کنید.
🔹
در پایان نیز به قید قرعه به ۱۲ نفر از شرکت‌کنندگان هدایایی اهدا خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/farsna/442306" target="_blank">📅 17:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442305">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3d4695485.mp4?token=FOZLBY08gZBqZ8oHZ7qCgSPFkURlxeNy_Fdn3xsLV2TuyhPZ_qT7pDxAn6ntOsxrLLbxCIneWsP-ptwZB5YtC-UFzEea97fjkIGwu5LB8_rgo8MbqwYDg7JBpaClrN8FqceE6FsRfm6BXFbaEak9Pqgho2KTUkCo0T3jHlmMUCsnNxP0tiwsdiiIgxlNUKbgaLdmTrJ9wWfiyJ78g9DMjhpxA08pkefUGgAGRfECLuvFpYJjNFaZFRwA6UWR8XEPX2GlnhioNkRZJcfa-pgIg6P8UygDpxfC-yI7hcFCVDCP4BjfmNXlEDErlvJEjI6up8q5MAj4rtayajO0HRy4Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3d4695485.mp4?token=FOZLBY08gZBqZ8oHZ7qCgSPFkURlxeNy_Fdn3xsLV2TuyhPZ_qT7pDxAn6ntOsxrLLbxCIneWsP-ptwZB5YtC-UFzEea97fjkIGwu5LB8_rgo8MbqwYDg7JBpaClrN8FqceE6FsRfm6BXFbaEak9Pqgho2KTUkCo0T3jHlmMUCsnNxP0tiwsdiiIgxlNUKbgaLdmTrJ9wWfiyJ78g9DMjhpxA08pkefUGgAGRfECLuvFpYJjNFaZFRwA6UWR8XEPX2GlnhioNkRZJcfa-pgIg6P8UygDpxfC-yI7hcFCVDCP4BjfmNXlEDErlvJEjI6up8q5MAj4rtayajO0HRy4Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم مطهر امام رضا(ع) آمادهٔ‌ عزاداری سالار شهیدان شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/442305" target="_blank">📅 17:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442304">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd29612d12.mp4?token=aUNHqTKnk4roQREnzYd5wqfQgeB9XyEttXwmCYK-544keT6_Pc3aZGgKhIXQX44B3tYOfxobvwbVfbNBaOtmquZJq0-RWR8UVvRuR8uDr0iFN8CoR-sQdv-NFyS5RDDO2k0EVwj4RtxI3mVbGu-GnXHwGNUQpa0rz9wMAbrAhCHAOznZRiDc7ZdTNmM1WFjx-r0Bu6oE-vSm_3iaTct4k1z7KoLs-D9foNmkKjN1kg7O1YeMxj7uH9UU7JXZR4oFqbhh36urL5KE6Va5tUrAerb26zyuO2Fn6fllZxKDR6UVriSi80rgXVtxO1SOfxN-QpNvx4Qk45gwE4D-9yQ4OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd29612d12.mp4?token=aUNHqTKnk4roQREnzYd5wqfQgeB9XyEttXwmCYK-544keT6_Pc3aZGgKhIXQX44B3tYOfxobvwbVfbNBaOtmquZJq0-RWR8UVvRuR8uDr0iFN8CoR-sQdv-NFyS5RDDO2k0EVwj4RtxI3mVbGu-GnXHwGNUQpa0rz9wMAbrAhCHAOznZRiDc7ZdTNmM1WFjx-r0Bu6oE-vSm_3iaTct4k1z7KoLs-D9foNmkKjN1kg7O1YeMxj7uH9UU7JXZR4oFqbhh36urL5KE6Va5tUrAerb26zyuO2Fn6fllZxKDR6UVriSi80rgXVtxO1SOfxN-QpNvx4Qk45gwE4D-9yQ4OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳۰۰ خودروی جدید آتش‌نشانی‌های کشور واگذار شد
@Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/442304" target="_blank">📅 17:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442303">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پزشکیان: اگر همۀ مفاد تفاهم‌نامه به‌درستی عملیاتی شود، به‌عنوان سندی افتخارآمیز برای کشور تلقی می‌شود
🔹
اجرای کامل این تفاهم‌نامه می‌تواند بسیاری از مسائل را برطرف کند و شرایط تازه‌ای را در ایران و منطقه رقم بزند. این تفاهم‌نامه نه‌تنها برای داخل کشور، بلکه برای کل منطقه و نیروهای مقاومت نیز افتخاری بزرگ به شمار می‌رود. جزئیات آن نیز ان‌شاءالله در زمان مناسب ارائه خواهد شد.
🔹
لازم می‌دانم از اعضای تیم مذاکره‌کننده تشکر کنم؛ از آقای قالیباف که زحمات زیادی کشیدند، از آقای عراقچی و همچنین از اعضای شورای‌عالی امنیت ملی و همۀ کسانی که در این مسیر نقش‌آفرینی کردند.
🔹
در شورای‌عالی امنیت ملی، پس از بحث‌ها و بررسی‌های مختلف، تقریباً بیش از ۹۰ درصد اعضا با این روند همراهی کردند و رأی دادند که این اقدام باید انجام شود.
@Farsna</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/442303" target="_blank">📅 17:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442302">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38f89a4ac.mp4?token=dcwgFkAgY11Nz3H7vZglrubw24HMKN7R5k8KnL786napt7qagvOsi6wDbfgVyqIjAHULUHymA0Gbxg9mKNbYA7NMieK71VJ5OshKAdpIra1CEt2_q_Aht54fMHlTYipf0LehvvJZkxAbxzJHlWRuHtHfA_IprrwdCU6S6pbuHEsHQIDbyCc7mx2koB-kamL5VrOhHp1e5r6iO-vizo6u_L-T02_2CK5qMThbZNJT5vyd_N5kOkjF1JSC6Vq-6khcThifWi5ugC5IvQ7RjvJVV6jTRWBLgQIsn_ICjLPo_f31rOnmjWn2icsToGsl6BGfOgj3MGtepZWqJyLrDJBjDhboXxP4mDi2ID5pBnEnxaIyecvxPx2fw4YP_36JRWv8W8L7xhoP4qK7mEFkbKDbJJqOK--WNCmmBt07S_-k7hgWKji6G5gAyF0uAAkBrpgYs8s4yJ4bg1g8PmXZNdxvWKUXovZftq-rlE8SFnD09L9AH2koKhh0sEPxkZ2r2kMoWK6LyOBOQEDWxA5C_KnqVoUh0IQs2oMnrmj-8ivyzxPNf62mIFrR43AP5xlv_JmiPCjbgnnF8joKc4xFb95wq23KKKzQeYvAC0RG-CAmQMPe34a6ePsLOsl1meLe850lWaeQCHuW3aZHDBVIe3KrGSilfGEJo02OAtJRvtTZeys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38f89a4ac.mp4?token=dcwgFkAgY11Nz3H7vZglrubw24HMKN7R5k8KnL786napt7qagvOsi6wDbfgVyqIjAHULUHymA0Gbxg9mKNbYA7NMieK71VJ5OshKAdpIra1CEt2_q_Aht54fMHlTYipf0LehvvJZkxAbxzJHlWRuHtHfA_IprrwdCU6S6pbuHEsHQIDbyCc7mx2koB-kamL5VrOhHp1e5r6iO-vizo6u_L-T02_2CK5qMThbZNJT5vyd_N5kOkjF1JSC6Vq-6khcThifWi5ugC5IvQ7RjvJVV6jTRWBLgQIsn_ICjLPo_f31rOnmjWn2icsToGsl6BGfOgj3MGtepZWqJyLrDJBjDhboXxP4mDi2ID5pBnEnxaIyecvxPx2fw4YP_36JRWv8W8L7xhoP4qK7mEFkbKDbJJqOK--WNCmmBt07S_-k7hgWKji6G5gAyF0uAAkBrpgYs8s4yJ4bg1g8PmXZNdxvWKUXovZftq-rlE8SFnD09L9AH2koKhh0sEPxkZ2r2kMoWK6LyOBOQEDWxA5C_KnqVoUh0IQs2oMnrmj-8ivyzxPNf62mIFrR43AP5xlv_JmiPCjbgnnF8joKc4xFb95wq23KKKzQeYvAC0RG-CAmQMPe34a6ePsLOsl1meLe850lWaeQCHuW3aZHDBVIe3KrGSilfGEJo02OAtJRvtTZeys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم‌داری سرتیم حفاظت رهبر شهید انقلاب از زبان فرزندش
🔹
فرزند سردار شهید سیدمجید طباطبائیان ( سرتیم حفاظت از رهبر شهید انقلاب): برخلاف برخی تصورها، امکانات ویژه‌ای برای تیم حفاظت از رهبر شهید انقلاب در کار نبود و پدرم حتی با راه‌اندازی صندوق قرض‌الحسنه تلاش می‌کرد گره‌ای از مشکلات همکارانش باز کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/442302" target="_blank">📅 17:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442301">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zt9M5OVX5wgHub44_8xhmMQYYcWEUGesfzEkVULvMMOhg7o3smJlAAPYHOOLsgtxihzmVmGm2nWtFKPYZctvoOlSkCy4GRWfvPGP-_xpKBcVZAqzzXNOp0CvQewGvfuepHVVsHo1G5WxhkFHZKd1HlAPPfq_YmR_Zbp2xpp32qqfOREmmYFiI-_CrcL5iP0LZEDu9DdUsK1cHSo5FAlSxHE4vlBdggb6WgBaZLeDjVROkh2fB-8NB1C34m_qP8BoRuFte6vJ2xgSBALFoUrqA6OUy04_yv7Rln71wXNsryVs7D88QQLb8XOUSpUcWXIzXYygeQvRaEUdbGrBghVUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقلید عادل فردوسی‌پور از ابوطالب حسینی
🔸
«فوتبال ایران با مدیر انقلابی تحقیر شد». شاید فکر کنید این تیتر رسانۀ ضدایرانی اینترنشنال است اما این‌طور نیست. در هفته‌های منتهی به حضور ایران در جام جهانی رسانۀ ۳۶۰ متعلق به عادل فردوسی‌پور از هر فرصتی برای حمله به تیم ملی استفاده کرده.
🔹
بخشی از کارکرد رسانه‌ها همواره نقد برای بهبود شرایط است. به فدراسیون فوتبال ایران و تیم ملی نقدهای بسیاری وارد است. همین حالا می‌توان رونمایی از لباس تیم ملی، کش‌دار شدن ماجرای سهمیۀ آسیایی و ناتمام‌ماندن لیگ برتر را به‌عنوان‌مثال ذکر کرد.
🔹
اما چیزی که در مورد تیم ملی نادیده گرفته شده، فشار خارجی است. تهدید جانی تیم ملی از سوی ترامپ، تلاش برای لغو بازی‌های ایران، ندادن کمپ آریزونا و صدور ناقص ویزای اعضای تیم ملی همگی بخشی از کارشکنی است. سنگ‌اندازی که در دنیای فردوسی‌پور محلی از اعراب ندارد. او ترجیح می‌دهد تا جلوتر از نوک بینی‌اش را نبیند و تصویر بزرگ‌تر را نادیده بگیرد.
🔹
نقد ساختاری به بهبود شرایط کمک می‌کند، اما تمسخر صرفاً جنبه سرگرمی دارد و ارزش‌افزوده‌ای برای پیشرفت فوتبال ایجاد نمی‌کند. مسیری که فردوسی‌پور پس از جدایی از نود آن را شدیدتر دنبال کرده. حالا همه چیز به «وایرال‌شدن» بستگی دارد.
🔹
«قلعه‌نویی حالا طوری ساعت می‌بندد که همه باید ببینند». جمله‌ای بود که «عادل» در واکنش به فتوشات‌های سرمربی تیم ملی با ساعت رولکس بر زبان آورد.
🔹
او قبل‌تر حرف‌های قلعه‌نویی درباره سخت‌تر شدن صعود به جمع ۱۶ تیم برتر جام جهانی را هم پای «خنگ» بودن خودش گذاشته بود. حالا دیگر نقد فنی قرار نیست زمان برنامه را پر کند. همه چیز به اندازۀ آیتم‌های ابوطالب فکاهی شده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/442301" target="_blank">📅 17:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442300">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ad819e65.mp4?token=Xb5O48MuTbu8ZAgpn6nqPVjCLCuAXw51eRS5c7jGBEDQoPEGeFiZWdxcgnALWEAJiHrIrDPbXP4qr5bsgg9yeutr7lQ7U_awiQ8ZLOi9W6cIMnAJ91fs-77I3ucIlnYlqi0WrSxxrP37OHdMDulHH-0JCBUdTnt3iIxzE1OVDW-rlYDkebbRTpQ9pOfoMpDNp-Rf2YB1pHKk6eQbko6YzAfdFq7fjuc2-IlqtkyesNlLOsEDgboBdOc8Ax7nyEhvsRu_xzf8ZIrNZ06-6JDihQ9RGzcfavxpzuIDhWO-5XTytsvhHqOamtdDoQQZKgu0v8rJ88hCVHSHV9RMjjtUXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ad819e65.mp4?token=Xb5O48MuTbu8ZAgpn6nqPVjCLCuAXw51eRS5c7jGBEDQoPEGeFiZWdxcgnALWEAJiHrIrDPbXP4qr5bsgg9yeutr7lQ7U_awiQ8ZLOi9W6cIMnAJ91fs-77I3ucIlnYlqi0WrSxxrP37OHdMDulHH-0JCBUdTnt3iIxzE1OVDW-rlYDkebbRTpQ9pOfoMpDNp-Rf2YB1pHKk6eQbko6YzAfdFq7fjuc2-IlqtkyesNlLOsEDgboBdOc8Ax7nyEhvsRu_xzf8ZIrNZ06-6JDihQ9RGzcfavxpzuIDhWO-5XTytsvhHqOamtdDoQQZKgu0v8rJ88hCVHSHV9RMjjtUXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماکرون: ناو فرانسه می‌تواند ظرف ۲ تا ۳ روز آینده در تنگهٔ هرمز مستقر شود؛ البته با هماهنگی
🔹
ما می‌توانیم از همین فردا یک ناو محافظ و ظرف ۲ تا ۳ روز آینده، ناو شارل دوگل، تجهیزات مین‌روبی و ناوهای محافظ شرکایمان و سایر تجهیزات را در منطقه داشته باشیم.
🔹
اما…</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/442300" target="_blank">📅 17:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442299">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9cfcb123f.mp4?token=GGaxiOoti5qewyFQyn1ux6rXw1Oo-WQ0Q87y0us9K8vm4dpcLEQJTCm0YJmP3rj2IUXDA9DdlrVJMxh95nyjHsdGjr8bZ4jZcSmDCApmagmnSGlMuNggmfcLabXqsJGJ8OFHA4pNBXBXQEbuOPpCJ0v3eXSQdgaP7G9xa1liOOL4tdgU6mJxLcf3KMmhdiU9QyM_zesp0QLfCKguJj0t_5UIg4xTatQvZB0aI5TExnkWHd9gtGwcuEqtnG4lA6qNhWMfIhVGgeRO5Qh6QWlFMKMUr2Zs84Fg4VO_cDU_7_4dTdZxd68NoY-aSgU2E632f0l6fI8JUCJg3ObLW-KYAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9cfcb123f.mp4?token=GGaxiOoti5qewyFQyn1ux6rXw1Oo-WQ0Q87y0us9K8vm4dpcLEQJTCm0YJmP3rj2IUXDA9DdlrVJMxh95nyjHsdGjr8bZ4jZcSmDCApmagmnSGlMuNggmfcLabXqsJGJ8OFHA4pNBXBXQEbuOPpCJ0v3eXSQdgaP7G9xa1liOOL4tdgU6mJxLcf3KMmhdiU9QyM_zesp0QLfCKguJj0t_5UIg4xTatQvZB0aI5TExnkWHd9gtGwcuEqtnG4lA6qNhWMfIhVGgeRO5Qh6QWlFMKMUr2Zs84Fg4VO_cDU_7_4dTdZxd68NoY-aSgU2E632f0l6fI8JUCJg3ObLW-KYAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماکرون: ناو فرانسه می‌تواند ظرف ۲ تا ۳ روز آینده در تنگهٔ هرمز مستقر شود؛ البته با هماهنگی
🔹
ما می‌توانیم از همین فردا یک ناو محافظ و ظرف ۲ تا ۳ روز آینده، ناو شارل دوگل، تجهیزات مین‌روبی و ناوهای محافظ شرکایمان و سایر تجهیزات را در منطقه داشته باشیم.
🔹
اما تمام این اقدامات تنها در صورتی معنا خواهد داشت که یک توافق بین‌المللی وجود داشته باشد.
@Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/442299" target="_blank">📅 17:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442298">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82d1ca889d.mp4?token=q0_7d_FiJMnQ0DhFEI4yX60FwZz4sOZ0fA_0K0D67OV5wQdcwq5MjnKCFT0tFRaOMu4FkNTJuYOTSaWKGLxi3Y8EK1vyMQjaP6UundAXRASllnfvboVWfNZCeWqx0jPKkeO9EmBXySYaSwO4dazqLs4lYZsVOipu8tVxamOHskjqIKMIZy-P-49qvz0D4PsGe6Qij6Y0XQhfejjh6YPvkdmJfJ8KQMtuqI-vC65jLDNyZv1qDrh3C4ackIYIBmGuE0CPg-b0rziHKhPaRxiEHQxm7rv-bzHxYJqDiSJz8NFTe7kVvGm6snWPAuzK1zY5UxA5VDP6sIP077qovMyEIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82d1ca889d.mp4?token=q0_7d_FiJMnQ0DhFEI4yX60FwZz4sOZ0fA_0K0D67OV5wQdcwq5MjnKCFT0tFRaOMu4FkNTJuYOTSaWKGLxi3Y8EK1vyMQjaP6UundAXRASllnfvboVWfNZCeWqx0jPKkeO9EmBXySYaSwO4dazqLs4lYZsVOipu8tVxamOHskjqIKMIZy-P-49qvz0D4PsGe6Qij6Y0XQhfejjh6YPvkdmJfJ8KQMtuqI-vC65jLDNyZv1qDrh3C4ackIYIBmGuE0CPg-b0rziHKhPaRxiEHQxm7rv-bzHxYJqDiSJz8NFTe7kVvGm6snWPAuzK1zY5UxA5VDP6sIP077qovMyEIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش بقائی به ادعای معاون رئیس‌جمهور آمریکا در خصوص سرازیر شدن مزایای اقتصادی به ایران: ما را به خیر تو امیدی نیست
🔹
«از آمریکایی‌ها خیلی زیاد رسیده است! من فکر می‌کنم این مزایایی را که می‌گویند، باید از مردم میناب، مردم لامرد و خیلی از نقاط ایران پرسید…</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/442298" target="_blank">📅 16:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442297">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/663ecfe4e0.mp4?token=hdrv2bCwgVddjd9RToKtEWPd5-r3UQm1_fRRuzdptaa5pnPwmaHr_9xqInzsFpVEzsVmOTPmSMr-KVN967JpPosSbbTFGqastAFwYTfCBEStx45uU9OJxszSn_GnFEO2uaJcNuQvVq5-40a6ekWEVfMeGPLDe6t10p4NACsVeQkh9a6VuiX6f4UbWl0nVThTv3g-eORTEUIFqEDqxQBYS2whDXPRloZvGIMgqR3dMY3qxb-K7CqoY9ejDPmEuBWXpla2PGy9FT02CKLX28V662CYKrHjO-Axbf5TeUGKnohjVqIuOmj1CZTJkmtYip5IkUQv5dNY24M4FtuvdXe86w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/663ecfe4e0.mp4?token=hdrv2bCwgVddjd9RToKtEWPd5-r3UQm1_fRRuzdptaa5pnPwmaHr_9xqInzsFpVEzsVmOTPmSMr-KVN967JpPosSbbTFGqastAFwYTfCBEStx45uU9OJxszSn_GnFEO2uaJcNuQvVq5-40a6ekWEVfMeGPLDe6t10p4NACsVeQkh9a6VuiX6f4UbWl0nVThTv3g-eORTEUIFqEDqxQBYS2whDXPRloZvGIMgqR3dMY3qxb-K7CqoY9ejDPmEuBWXpla2PGy9FT02CKLX28V662CYKrHjO-Axbf5TeUGKnohjVqIuOmj1CZTJkmtYip5IkUQv5dNY24M4FtuvdXe86w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کنایۀ بقائی به حواشی امنیتی پیرامون کمپ تیم‌های ملی مختلف در آمریکا
🔹
خوشبختانه کمپ ایران در مکزیک است نه آمریکا؛ از مکزیک بابت میزبانی خوبش تشکر می‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/442297" target="_blank">📅 16:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442296">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZb6ihTZLnPuO7_uvDc1oqkuuBAvTsrwnMYOlcRl53AzweBtWWSR2qSVNt3QSusQmlzAvEau6iWw1fuXkagFcnPDw2qHHdR8GlwjAbg2DWx27OF-Xy5RmTSLelrBcTMh6ht3IH1oV_4bDOw1DMTlAhfGUBc6-2iGL4jqhoFR9qk7E-zDFblbK84KNtDhWE4yS-kNRwOfVL9boggsg0_6hZ6a0OmglfAAijG7fJWVbAwaw34k6DfyXsC2V4j4p-028yBZ8U1KCAvqr4z8NL0axpvf1jidR4-Sr-54bGcYK0H79SpnL-kdrR9xcEcwYFsqOrif0T88SyR680ertXR7yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پوستر صفحهٔ رسمی جام جهانی برای بازی ایران و نیوزیلند
⚽️
این بازی ساعت ۴:۳۰ صبح فردا در ورزشگاه لس‌آنجلس برگزار می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/442296" target="_blank">📅 16:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442295">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e51b0e9f7.mp4?token=WOD_If_ZGPdERI8ZX-SQnOt6beyxVnGrbIiyIZ_LFkGREc2pFtmjGBExJy47Ns7WuTN0D-Z53PCVNYZfbZ6mP8bSEhcHJJdYCvbtYPpMUoosuhSpuvViKzB5wYh7vToDYBBViOj2KOlC7RC4pYMgE0QG_uRAsBC3YaVxQb9Gt_ky036prY2vmsqzUFsl3X7oHMrqJr-1JlSe3DyCnY7j3rVldeOCfZc24kcZjJnYX72K_aEdsQ_rh9RJv5YPoNf9fuU7vEQ3pfyw4_CRC0f3bmmLAf-doapIRyn7960rqUfKVD07PlZRqvNKtJHXutBULxEE8yf0qnRo0-SfxUFwIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e51b0e9f7.mp4?token=WOD_If_ZGPdERI8ZX-SQnOt6beyxVnGrbIiyIZ_LFkGREc2pFtmjGBExJy47Ns7WuTN0D-Z53PCVNYZfbZ6mP8bSEhcHJJdYCvbtYPpMUoosuhSpuvViKzB5wYh7vToDYBBViOj2KOlC7RC4pYMgE0QG_uRAsBC3YaVxQb9Gt_ky036prY2vmsqzUFsl3X7oHMrqJr-1JlSe3DyCnY7j3rVldeOCfZc24kcZjJnYX72K_aEdsQ_rh9RJv5YPoNf9fuU7vEQ3pfyw4_CRC0f3bmmLAf-doapIRyn7960rqUfKVD07PlZRqvNKtJHXutBULxEE8yf0qnRo0-SfxUFwIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مردمان ما به‌عنوان صاحبان کشور حتما مراقب عملکرد مسئولان کشور هستند.
🔹
مردم ما وقتی مجاب و قانع شوند که بهترین تصمیم‌ توسط مسئولین گرفته شده است پشتیبان ما خواهند بود. @Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/442295" target="_blank">📅 16:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442294">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318f9ae212.mp4?token=p1iddgT7-UaZxsIdhcnBjgPgvQAH3qVlL4CyFiKJ8I4DudoGRD0_cSpixs_WpJyQUqV9eTp1wFCY200j3WT7Bi40Off1ble_SaWVTwxv-0w-8ORWSFDnjKOIfojEp4Vo33aRI9J2SeoDEsSRv7VZK28lwvUjYMTcr6AJh04DktM6-WIXWeFdvVJ2nYH20jmMV7mBQlkOK3iAeA2iRiCM_jW7POkzXd1BZKY6zE-Bxs_OajULLl7An5CDnkKrkpq5OhUKaNzxHrl9xACZA2rk_DUuQNoMXUv4jBVAIhxF2l_vK22Kuy5E1Mtho1YoVICkjRCUfBtUVpgHAEY7SEvKSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318f9ae212.mp4?token=p1iddgT7-UaZxsIdhcnBjgPgvQAH3qVlL4CyFiKJ8I4DudoGRD0_cSpixs_WpJyQUqV9eTp1wFCY200j3WT7Bi40Off1ble_SaWVTwxv-0w-8ORWSFDnjKOIfojEp4Vo33aRI9J2SeoDEsSRv7VZK28lwvUjYMTcr6AJh04DktM6-WIXWeFdvVJ2nYH20jmMV7mBQlkOK3iAeA2iRiCM_jW7POkzXd1BZKY6zE-Bxs_OajULLl7An5CDnkKrkpq5OhUKaNzxHrl9xACZA2rk_DUuQNoMXUv4jBVAIhxF2l_vK22Kuy5E1Mtho1YoVICkjRCUfBtUVpgHAEY7SEvKSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما به رژیم صهیونیستی هیچ اعتمادی نداریم کما اینکه به آمریکا هم نداریم
🔹
این امر ثابت شده‌ای است که این ۲ در اجرای تعهداتشان هیچ وقت صداقت نداشتند.
🔹
در عین حال ما ابزارهای خودمان را داریم. آمریکا باید تعهداتش را انجام دهد و باید اطمینان…</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/442294" target="_blank">📅 16:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442292">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8cd6fc55e.mp4?token=fFZJz2_9lgspmvHHLb-fqVy5r3ot1C-dLjr7zbR0gxafZezrfNxMO1sZx0tEcBbDHRxgMSAnqKJW7fBbVIL0O7KWOHZxBHB2lLRoTKrDtQ9JuzmX8b-kQeJ6cKqWSTmxspJue89aZhfImfCOpylUphKSJH54MwjekipJwBIZexTMsJy0rlXVK1SGLyjMXYbCBZr5bzdTRv5-fgNmrTrZm6htM32GaWfqtPpPaCLRaFv_q3UmtXq9WAJDdRRnKVTVCsVotMSQbxuqmlZl6diPbzEit6Cpsj0GMB6ojY7GMT2IrOcUzGLrtkW-ua3Pj_V_0Hru-KhMc7g1gAAMlIFyvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8cd6fc55e.mp4?token=fFZJz2_9lgspmvHHLb-fqVy5r3ot1C-dLjr7zbR0gxafZezrfNxMO1sZx0tEcBbDHRxgMSAnqKJW7fBbVIL0O7KWOHZxBHB2lLRoTKrDtQ9JuzmX8b-kQeJ6cKqWSTmxspJue89aZhfImfCOpylUphKSJH54MwjekipJwBIZexTMsJy0rlXVK1SGLyjMXYbCBZr5bzdTRv5-fgNmrTrZm6htM32GaWfqtPpPaCLRaFv_q3UmtXq9WAJDdRRnKVTVCsVotMSQbxuqmlZl6diPbzEit6Cpsj0GMB6ojY7GMT2IrOcUzGLrtkW-ua3Pj_V_0Hru-KhMc7g1gAAMlIFyvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مذاکرات در مورد موضوع هسته‌ای و رفع تحریم‌ها ظرف ۶۰ روز انجام می‌شود
🔹
در متن یادداشت تفاهم راجع به جزییات موضوع هسته‌ای بحثی را مطرح نکردیم و به‌صورت کلی تفاهم شده که در یک بازۀ زمانی ۶۰ روزه بعد از امضای تفاهم در خصوص موضوع هسته‌ای…</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/442292" target="_blank">📅 16:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442291">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حزب‌الله: انعقاد تفاهم میان ایران و واشنگتن را که به برقراری آتش‌بس در همۀ جبهه‌ها از جمله لبنان انجامید، تبریک می‌گوییم
🔹
این موفقیت بزرگ حاصل ایستادگی کم‌نظیر، پایداری استثنایی و فداکاری‌های عظیم ملت ایران و رهبری خردمند آن در مسیر حفظ کرامت، حاکمیت و استقلال ملی خود بوده است.
🔹
حزب‌الله از مواضع ثابت ایران در حمایت از لبنان، مردم و مقاومتش و نیز اصرارشان بر حضور لبنان در هر توافقی که به توقف جنگ و حفظ حقوق این کشور منجر شود، قدردانی و تأکید می‌کند جمهوری اسلامی ایران بار دیگر نشان داد که پشتیبان و متحدی قدرتمند و وفادار است.
🔹
لبنان باید از این پشتوانۀ منطقه‌ای و بین‌المللی به بهترین شکل برای تحقق حاکمیت خود در چارچوب وحدت داخلی بهره ببرد.
🔹
آنچه محقق شده، مقدمه‌ای برای تکمیل آزادسازی کامل سرزمین ماست.
@Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/442291" target="_blank">📅 16:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442290">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfrzMyaQaQ1VbuJGOGsCMFciqK-QDp9JqIIEKhFm98JKBL8UvO_87WjXgg0xrRNZnE6OurCjTnUhar1wtFez3kDKAnK2tnYeiMDzU-FMae1ZP4IMnNB1gXV6AbfanfPavx4mY0yCfO1yUgzxlsTwMETlO48oV_8VjFOOJeBjhZ06JixByC939K8_CSFnISMaoWHMW4Rwv0TZZbwzqU6jU4BAENPpOPOE5JCHrz3ctiTeR4LBKsRfxecZHfuJReApHw5Cl9XLFJLnkrqvS3zE2sWdLNRL8hT75HTQ9b4k6VzvILxSve_lmtGVHwesjzVs6xjrOBnnU3fWC9DvbHYqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پوستر صفحهٔ رسمی جام جهانی برای بازی ایران و نیوزیلند
⚽️
این بازی ساعت ۴:۳۰ صبح فردا در ورزشگاه لس‌آنجلس برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/442290" target="_blank">📅 16:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442289">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bffcd01d81.mp4?token=fYN6VbFmFecuiUrWZjXBSmCHh4Tzf8vJvpub8DJ3o4OBNLKUKr3Y3gX6GuRTw5nn7S0ara4uM1kI6CyACkWBxFpYsdUjjpkDpoGzpMFHUR3N3TZyOhRwIldC1TLWSAg84v7oN6c2I4zVtfuWTB1--eNDUkhJFrL076R-qLDZQZCmk47_5IpQkrvJx3XEpodDxmo4dB47lPpKG0Oet-hst9o5Jp8_XfF_Ysh0_E9HNKWLYmr0z5KMBp8BePR-en-N86iOyF2hez2ftswebvuQJeQzcd5JTgSKLtIFpGaMBtseSO3vnDs4bFpqtOfaZFfFbUWxotf3negNZSx2_0knLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bffcd01d81.mp4?token=fYN6VbFmFecuiUrWZjXBSmCHh4Tzf8vJvpub8DJ3o4OBNLKUKr3Y3gX6GuRTw5nn7S0ara4uM1kI6CyACkWBxFpYsdUjjpkDpoGzpMFHUR3N3TZyOhRwIldC1TLWSAg84v7oN6c2I4zVtfuWTB1--eNDUkhJFrL076R-qLDZQZCmk47_5IpQkrvJx3XEpodDxmo4dB47lPpKG0Oet-hst9o5Jp8_XfF_Ysh0_E9HNKWLYmr0z5KMBp8BePR-en-N86iOyF2hez2ftswebvuQJeQzcd5JTgSKLtIFpGaMBtseSO3vnDs4bFpqtOfaZFfFbUWxotf3negNZSx2_0knLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مردم منطقهٔ‌ ما نمی‌پذیرند که رژیم صهیونیستی اقدامی بدون هماهنگی آمریکا انجام دهد.
🔹
هر نقض عهدی از سوی متحدان آمریکا صورت بگیرد، مسئولیتش با آمریکاست. @Farsna</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/442289" target="_blank">📅 15:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442288">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b78ba35a.mp4?token=n3tzi9Lc001dsDwP354tKKh3z5GW3rX1w_qIo2Q1DAmyZDFonduuejPLMzRHUwfAVoi0hqAjBVj9owz1vSDovL5_syKp1bNg7TjvuSfyumCkT3venI3_9YtFrGFATGez6TU6PIsRo0HRIpdijy9d_w9cQhc5vNkccFHOl3Zw45qElbBInSWqkd9ab8WOsDFm6YaXtkk9GmKeN5aFKJsmp68fOusDcYOHdYEt8BUNYlPsVmoLV0HJPS_lm5XNkBxswNGwEI3Xb-MTFRJjCQFaD4RzchiGCeVrxmO7wlSXzrgmGNY7zum-K2KYZ9oPAb4ZGXBpx6Q_uwVMnr_iOhfSvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b78ba35a.mp4?token=n3tzi9Lc001dsDwP354tKKh3z5GW3rX1w_qIo2Q1DAmyZDFonduuejPLMzRHUwfAVoi0hqAjBVj9owz1vSDovL5_syKp1bNg7TjvuSfyumCkT3venI3_9YtFrGFATGez6TU6PIsRo0HRIpdijy9d_w9cQhc5vNkccFHOl3Zw45qElbBInSWqkd9ab8WOsDFm6YaXtkk9GmKeN5aFKJsmp68fOusDcYOHdYEt8BUNYlPsVmoLV0HJPS_lm5XNkBxswNGwEI3Xb-MTFRJjCQFaD4RzchiGCeVrxmO7wlSXzrgmGNY7zum-K2KYZ9oPAb4ZGXBpx6Q_uwVMnr_iOhfSvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: به ازای خدمات ناوبری و بیمه در تنگۀ هرمز هزینه‌های لازم طراحی و دریافت خواهد شد
🔹
برای مدت زمان مشخص قرار است متناظر با اقدامات طرف مقابل تردد ایمن در تنگه هرمز را مدیریت بکنیم.
🔹
این موضوع به عهده دولت جمهوری اسلامی ایران به عنوان دولت…</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/442288" target="_blank">📅 15:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442287">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9122e82f3.mp4?token=Xso5Vy6knl3zBsPz7lyMoxuI9GBpNLoIBt-yNi_ewtNypNyLrluh29RzEKNRBvN4oTvo1dA-I3hIQOfrFGH2yO0MJgPilHRQm84omLG6i6752kay3ZdkwMl8rZ3Q9RjdVuSPbyzzsFLn4yZMrwqensJGVYxX1SdlyFHB1aiNsutoceems48aUzv43Tsx1WkIrmV7DVscSlNt3ZtXvFqg1DUjr8D5SWB7wf68kOS12c4F0IXbUqs_JDW4hTrJo7Yd1pQGjIjI0TLjokD0OwD2WrUW2ZlAcyl4A8diEDelFIyPBjNg_6TolavWXiaOyRpluyOEALXxCTGIv4wspe3d5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9122e82f3.mp4?token=Xso5Vy6knl3zBsPz7lyMoxuI9GBpNLoIBt-yNi_ewtNypNyLrluh29RzEKNRBvN4oTvo1dA-I3hIQOfrFGH2yO0MJgPilHRQm84omLG6i6752kay3ZdkwMl8rZ3Q9RjdVuSPbyzzsFLn4yZMrwqensJGVYxX1SdlyFHB1aiNsutoceems48aUzv43Tsx1WkIrmV7DVscSlNt3ZtXvFqg1DUjr8D5SWB7wf68kOS12c4F0IXbUqs_JDW4hTrJo7Yd1pQGjIjI0TLjokD0OwD2WrUW2ZlAcyl4A8diEDelFIyPBjNg_6TolavWXiaOyRpluyOEALXxCTGIv4wspe3d5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: طرف آمریکایی متعهد به  آزادسازی اموال مسدود شده ایران و بازسازی خسارات می‌شود.
🔹
طرف آمریکایی موظف به رفع همه‌ی تحریم‌ها می‌شود؛ ایران باید بتواند بدون هیچ مشکلی فروش نفت را انجام بدهد. @Farsna</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/442287" target="_blank">📅 15:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442286">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d86a184db.mp4?token=WyIekvCeCDPDv_34P7pATEsRHIVBcyZ5nXcKu-xoQ9cCGXj0P_npyJ0xN9QDIN1P8O7les4ZLPPEszp8DdSu0kYspDh-w_RJGdAfwA68Rxx0bL8iCIPiL_yT7aaq6v_BNK888NsYFMB79yi4WROawGDNcWBhc_4B6JBUjnmEkvllYPv3HPgwPPUl3YQauzdJ2qC_5sTx4fGtJA_Lk-0Xz1OVT9fWidmb51FqcB-F7twiS4kF203poKiY2fwik4v_SVIvOaAvlymBlvZgVNNJQprDMncLqgaiNs_JoJDRIY1afRjZ7npZIv6MHaEOpL14m-jjKxkqbO5N21wmBjYy0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d86a184db.mp4?token=WyIekvCeCDPDv_34P7pATEsRHIVBcyZ5nXcKu-xoQ9cCGXj0P_npyJ0xN9QDIN1P8O7les4ZLPPEszp8DdSu0kYspDh-w_RJGdAfwA68Rxx0bL8iCIPiL_yT7aaq6v_BNK888NsYFMB79yi4WROawGDNcWBhc_4B6JBUjnmEkvllYPv3HPgwPPUl3YQauzdJ2qC_5sTx4fGtJA_Lk-0Xz1OVT9fWidmb51FqcB-F7twiS4kF203poKiY2fwik4v_SVIvOaAvlymBlvZgVNNJQprDMncLqgaiNs_JoJDRIY1afRjZ7npZIv6MHaEOpL14m-jjKxkqbO5N21wmBjYy0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: موضوع خون‌خواهی از همهٔ شهدایمان دائمی است و هیچ‌کس نمی‌تواند به‌هیچ‌‌عنوان از جنایت بزرگی که در حق ملت ایران شد، بگذرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/442286" target="_blank">📅 15:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442285">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">منبع آگاه: ایران مانع ورود موضوع موشکی و منطقه به مذاکرات شد
🔹
یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایرانی در گفت‌وگو با فارس، با تشریح برخی ابعاد یادداشت تفاهم اسلام‌آباد، تأکید کرد: یکی از مهم‌ترین دستاوردهای هیئت ایرانی خارج کردن دو مطالبه راهبردی آمریکا یعنی محدودسازی توان موشکی جمهوری اسلامی و قطع حمایت از جبهه مقاومت از دستورکار مذاکرات بوده است.
🔹
او با اشاره به تلاش چندساله آمریکا برای گسترش دامنه مذاکرات فراتر از موضوع هسته‌ای گفت: طرف آمریکایی در مراحل اولیه خواستار طرح موضوعاتی از جمله برنامه موشکی، توان پهپادی و روابط منطقه‌ای جمهوری اسلامی بود، اما هیئت ایرانی از ابتدا اعلام کرد این مسائل هیچ ارتباطی با موضوع مذاکرات ندارد.
🔹
این منبع آگاه افزود: برخلاف برخی برداشت‌ها، موضوع صرفاً این نیست که ایران درباره توان موشکی خود تعهدی نداده باشد؛ واقعیت این است که پرونده موشکی اساساً از دستورکار مذاکرات خارج شده است. یعنی نه در تفاهم فعلی بندی درباره برنامه موشکی و پهپادی ایران وجود دارد و نه قرار است این موضوع در مراحل بعدی مذاکرات مطرح شود.
🔹
او ادامه داد: در جریان مذاکرات، هیئت ایرانی به صراحت اعلام کرد توان دفاعی جمهوری اسلامی ایران موضوع مذاکره نیست و طرف آمریکایی نیز در نهایت این چارچوب را پذیرفت. بنابراین بحث موشکی نه تعلیق شده، نه به آینده موکول شده و نه قرار است در قالب مذاکرات بعدی دنبال شود؛ بلکه اساساً از دستور کار خارج شده است.
🔹
این منبع آگاه همچنین درباره موضوع مقاومت منطقه‌ای گفت: در این حوزه نیز شرایط مشابهی وجود دارد. آمریکا در مراحل اولیه خواستار طرح موضوع روابط ایران با گروه‌های مقاومت بود، اما این مطالبه نیز در متن نهایی جایی ندارد و از دستور کار مذاکرات کنار گذاشته شده است.»
🔹
او تصریح کرد: بر این اساس، مذاکرات آتی صرفاً بر موضوعات هسته‌ای، رفع تحریم‌ها و مسائل اقتصادی متمرکز خواهد بود و پرونده‌های دفاعی و منطقه‌ای جمهوری اسلامی ایران خارج از حوزه گفت‌وگو باقی خواهند ماند.
🔹
این منبع آگاه در پایان تأکید کرد: حفظ کامل توان موشکی، پهپادی و ظرفیت‌های منطقه‌ای دوستان ایران  یکی از مهم‌ترین خطوط قرمز هیئت ایرانی بود که در روند مذاکرات رعایت شد و در متن نهایی نیز بازتاب یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/442285" target="_blank">📅 15:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442284">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3584d1320a.mp4?token=mrgkNJpMAVw3Q_6RpiX2jxuc0kT3tceoW_B8Hv9XDJeoq-CAXTxAdyU3voYSQMAHZykDdaVbOgXfWygzdJollxvWxEghPqTZvZsFw7ieEkT1BEZsBwGy7Vs0WR0smdC2KPKD86pARoP3PyZM4wq-OlSzeogdNhbAuALFdtJi2Ydyr7SpoAkeTVUZL57sRtlHgQ2od0DxldJ0QLnK3PtNreE3MEsFM2MzGevtRO6Lr0McZUm04Vnbwxp_ugYo6cr-iw4PBsRnQtssYrQe2XFtWBQvn21aiWIHKuFap2utwyDcKqbcnHsdr-davJKVYaT6l7fAFamz0OYzacVxlU9Hnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3584d1320a.mp4?token=mrgkNJpMAVw3Q_6RpiX2jxuc0kT3tceoW_B8Hv9XDJeoq-CAXTxAdyU3voYSQMAHZykDdaVbOgXfWygzdJollxvWxEghPqTZvZsFw7ieEkT1BEZsBwGy7Vs0WR0smdC2KPKD86pARoP3PyZM4wq-OlSzeogdNhbAuALFdtJi2Ydyr7SpoAkeTVUZL57sRtlHgQ2od0DxldJ0QLnK3PtNreE3MEsFM2MzGevtRO6Lr0McZUm04Vnbwxp_ugYo6cr-iw4PBsRnQtssYrQe2XFtWBQvn21aiWIHKuFap2utwyDcKqbcnHsdr-davJKVYaT6l7fAFamz0OYzacVxlU9Hnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بقایی: جزئیات ابعاد دیپلماتیک توافق به‌زودی رسانه‌ای خواهد شد
🔹
در خصوص نحوه و سازوکار امضای یادداشت تفاهم، تصمیم‌گیری نهایی ظرف امروز و فردا صورت می‌گیرد و نتایج آن به‌صورت رسمی اعلام می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/442284" target="_blank">📅 15:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442283">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb5948c916.mp4?token=jLVnSEsjU_28xV43vtgZ-EZP3VU2B2cn-zrgOqHDQb2cLaxkNFUknjSQ4lUvYxkFWemMEjBUZAvi7fVikr2n-ufmbKekFNOdad-InAn_fqchSZkZILPp7n1T5aAxqa5dlq-9qGVMnfqu7OuFHZI_cd3m7nAAAY7-t86jU7Pn2zdnYC0DvZcbtLe3UnM0lXgktJ5FMXr_Y7WAuU87rQOmdJSJCBcYTay56TKbI-Tb-WOxceo8SaFqN8uS6MUb3V8JqvNLE1LUljygbPXwvpMo1DlO5GxnznGJZhv_dgjn7kiSAQkYLVUFjkR1xY33AXlsAFanqp0_pxTa_xxagh8lyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb5948c916.mp4?token=jLVnSEsjU_28xV43vtgZ-EZP3VU2B2cn-zrgOqHDQb2cLaxkNFUknjSQ4lUvYxkFWemMEjBUZAvi7fVikr2n-ufmbKekFNOdad-InAn_fqchSZkZILPp7n1T5aAxqa5dlq-9qGVMnfqu7OuFHZI_cd3m7nAAAY7-t86jU7Pn2zdnYC0DvZcbtLe3UnM0lXgktJ5FMXr_Y7WAuU87rQOmdJSJCBcYTay56TKbI-Tb-WOxceo8SaFqN8uS6MUb3V8JqvNLE1LUljygbPXwvpMo1DlO5GxnznGJZhv_dgjn7kiSAQkYLVUFjkR1xY33AXlsAFanqp0_pxTa_xxagh8lyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بقایی: در یادداشت تفاهم، ۳ بار اسم لبنان آمده و احترام به تمامیت ارضی و حاکمیت لبنان جزو تفاهم است.  @Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/442283" target="_blank">📅 15:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442282">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c95a58607.mp4?token=UBpx_lT_IdVATUPFVHvd6TiGGdqSWBqP8_YLR18uaftTG1Oz4Y8-H0WBjFFxldjE0mArIoIwF7Fxinui_PL4bdtrkh7DE23qcrLi59ZArfgXk-MgAUAbaAGsyrdmxYDPKZYw-IVoWUtNVSTc33mItKKnflx4Xr_I6pDiryNtLtT-UotdA7GYidaT9wekIGVD-Oa-KTRtoE6wwcevX-ChxOsn7bR-6s7NDMyuFmnAQJUw6lxnnD7-0GIj_Edjytm5OpLgWpVhK_vuqRUgQdQC6mDrSePG_ke0XRkFv6-ieZ0o-qduJaEmhTWkpHFu_GRgRX_NDrgRW9cgKDX-JilUbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c95a58607.mp4?token=UBpx_lT_IdVATUPFVHvd6TiGGdqSWBqP8_YLR18uaftTG1Oz4Y8-H0WBjFFxldjE0mArIoIwF7Fxinui_PL4bdtrkh7DE23qcrLi59ZArfgXk-MgAUAbaAGsyrdmxYDPKZYw-IVoWUtNVSTc33mItKKnflx4Xr_I6pDiryNtLtT-UotdA7GYidaT9wekIGVD-Oa-KTRtoE6wwcevX-ChxOsn7bR-6s7NDMyuFmnAQJUw6lxnnD7-0GIj_Edjytm5OpLgWpVhK_vuqRUgQdQC6mDrSePG_ke0XRkFv6-ieZ0o-qduJaEmhTWkpHFu_GRgRX_NDrgRW9cgKDX-JilUbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: لبنان و خاتمۀ جنگ در لبنان بخش لاینفک تفاهم خاتمۀ جنگ است.  @Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/442282" target="_blank">📅 15:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442281">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f31afa1dfe.mp4?token=jLDyyokluubBNEBytiSKhJpC7ZY6KHGOMPFd2NSxeomPMvLCk2VDdOaYBWu5OxJfok-ClnftcEgWO-ZIo1XCBS1FPxyHQZ3x7OqQ5j8QS8gXQxFiNyo9hJ9oelY2vGvoEjwEhy5R2EWWWWEfKyKEL62hVUCatDt6baezczQV4eHNaD3dqhHuHES3qSCTdjR6w4S2W9MUfyuC-yMWuKCkdipKG4OHyXSo7AeNMZucZ3wPTxRToH6lw3bXsWwvqDM4jeyfjjvXoey1Kc8ownVKu03jNUdQMYwhnG9CHjLgdyP1LcFJduL11l5Bou8AxulmuiAFNLCu4inQi4NRjmsoiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f31afa1dfe.mp4?token=jLDyyokluubBNEBytiSKhJpC7ZY6KHGOMPFd2NSxeomPMvLCk2VDdOaYBWu5OxJfok-ClnftcEgWO-ZIo1XCBS1FPxyHQZ3x7OqQ5j8QS8gXQxFiNyo9hJ9oelY2vGvoEjwEhy5R2EWWWWEfKyKEL62hVUCatDt6baezczQV4eHNaD3dqhHuHES3qSCTdjR6w4S2W9MUfyuC-yMWuKCkdipKG4OHyXSo7AeNMZucZ3wPTxRToH6lw3bXsWwvqDM4jeyfjjvXoey1Kc8ownVKu03jNUdQMYwhnG9CHjLgdyP1LcFJduL11l5Bou8AxulmuiAFNLCu4inQi4NRjmsoiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: لبنان و خاتمۀ جنگ در لبنان بخش لاینفک تفاهم خاتمۀ جنگ است.
@Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/442281" target="_blank">📅 15:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442280">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S99uV3D06edvyx677shXD6pIPbgt7qFpxYpuRkm_B15XzMiIpeqmmksrc4c1pwHMg7dR3ntP8WtirIXaJCyquzApV7DhTe2DsWp0l-k0thpi6hN8vIO-Q8VDhKyMFKLEeHowZ2wY71HfpMk-QNytD2wKjuKIytONVgZaKZOaPzXUcgZQE4bqR8sd5n0oDq5UTD31TrcYBcuOWciZf6KjZ6uxzsdPnuv1WaNrg8abwuUQUFvQEQRkjLsQ50iD000qhVleU3nLJjvkVvGNuM346-dMmv2HFF-oIzaR8JXYat0FexoLFil4WNCytzw5XvJYgi5z5puPL22U15wNaAY6YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده نیروی قدس سپاه: ملت ایران اثبات کرد خون بر شمشیر پیروز است
🔹
مقاومت متکی بر ایمان الهی یک بار دیگر از میدان انقلاب تهران تا میدان آزادی ملت‌های مظلوم به پیروزی رسید.
🔹
آفرین بر ملت امام حسینی ایران و مقاومت منطقه‌ای قهرمان که در آستانهٔ محرم حسینی اثبات کردند هیهات منا الذله یعنی چه و واقعاً خون بر شمشیر پیروز است.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442280" target="_blank">📅 15:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442279">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d3f2d805.mp4?token=RwikXIAsE3r_GlDL7WeFLxhSrkWom62K9z0cRsTRzisAKX3z0PuRqgM3AMsQ5gi4nugAR9p384rylQC5CveDo9lyX6Aqkl1fZsFxGfwmowB14QPygg3RlbW60nmNx2jIzy80xNstQicVWgeQqa4iVRypnVi09fpsjsw1f5w8ci3E1HJJU1T6n5JFUaxFnb_UWO8PyxfS3SBqyGU3xjn26cKPtNk76XkGRGP2QZXiPJhPq3GOG38uhKlrm_tdlZhkC0ZsvZcn0CV4LDrXXoVf3497JUB14mPHFPeGTKWBFF1kcXJjig4j2k1i8ovNlZvVjDpU4OtzLrRLCvhGdg7UpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d3f2d805.mp4?token=RwikXIAsE3r_GlDL7WeFLxhSrkWom62K9z0cRsTRzisAKX3z0PuRqgM3AMsQ5gi4nugAR9p384rylQC5CveDo9lyX6Aqkl1fZsFxGfwmowB14QPygg3RlbW60nmNx2jIzy80xNstQicVWgeQqa4iVRypnVi09fpsjsw1f5w8ci3E1HJJU1T6n5JFUaxFnb_UWO8PyxfS3SBqyGU3xjn26cKPtNk76XkGRGP2QZXiPJhPq3GOG38uhKlrm_tdlZhkC0ZsvZcn0CV4LDrXXoVf3497JUB14mPHFPeGTKWBFF1kcXJjig4j2k1i8ovNlZvVjDpU4OtzLrRLCvhGdg7UpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ردپای ۲ یوز ناشناس دوباره پیدا شد
🔹
۲ یوزپلنگ آسیایی که اوایل خردادماه برای نخستین‌بار در پناهگاه حیات‌وحش میاندشت جاجرم در خراسان‌شمالی مشاهده شده بودند، پس از ۲۲ روز بار دیگر مقابل دوربین محیط‌بانان قرار گرفتند.
🔹
مسئولان محیط‌زیست احتمال می‌دهند این ۲ یوز به خانوادۀ شناخته‌شدۀ «هلیا» تعلق نداشته باشند و ممکن است این موضوع نشانه‌ای از حضور یک خانوادۀ جدید در منطقه باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/442279" target="_blank">📅 15:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442278">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nhl1ROy_Htk_uhFvfJN_7o7imEaIB7qDAf6E9SXzTQ1lDLR-OD5_2JQI_pZivT1Zt98J7BWXl9RbmdOieeNsGR9llRuD58KWoyBEQjeOGN-Ly051Kvc2C2nCd9pb_W85RYcieAUQa7KrTdw0JIoiuNOefvRtQ4DePLJkBx9F4U-XLG5dA5k6ZVTlIJib-bWkytS4lGEZeakYOpCL3QrmLvXrEn6OyUh-JVM3IDF3IHjoEJAMRC2k98dkOUoUB4WuSVX9NI7AQRuKrCN5LwLLULNRL88vrWpFHDNXoK1vdYTqtuCU_PeSKOInWWMyGlilylYb1u1rM5XUlHG37pV_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یارانۀ ۴۰۰ هزار تومانی دهک‌های ۱ تا ۳ به حساب سرپرستان خانوار واریز شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/442278" target="_blank">📅 14:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442277">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کشف یکی از بزرگ‌ترین پرونده‌های زمین‌خواری کشور در تهران
🔹
با اقدامات قضایی و پیگیری دادستانی تهران، یکی از بزرگ‌ترین و پیچیده‌ترین پرونده‌های زمین‌خواری در غرب پایتخت کشف و در دستور کار رسیدگی قضایی قرار گرفته است.
🔹
در این پرونده با جعل وقف‌نامه، اسناد رسمی و سوءاستفاده از وکالت‌نامه‌ها، منجر به تصرف غیرقانونی اراضی در منطقه فرحزاد شده که از نظر ارزش ریالی یکی از بزرگ‌ترین پرونده‌های زمین‌خواری کشور محسوب می‌شود.
🔹
اطلاعات این پرونده طی ساعات آتی منتشر می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/442277" target="_blank">📅 14:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442276">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_eapde1EO_zJa7byj-4-iPU7yEHY0xFWWH7ovM-Vs3n7YXEgy2L4hNDng0w_yd6OXNcmWOaNQfbFNYQEQpUZm2U6_YP8I5vdpv5QuoRnC3WzHgKZTy2OEnQr_dKbQE5TpQihw-BMP8GuZEx18ogUX6djNKqrC2PDrikP3NIN7Af0yVBMWrOO-wTlvzMosqZNJ25HmeZCb2vdc768ssXyalJeGndA2fGvgd2PGixWiLHOr5paTDExF4QhVjAaQPLZLndkNwFtt9YAe1zdMbplDcg3Ib1gksm9PgnAiIujYq7pGxnRucft0aj9x5eLC-bAocdOW-KfykoZHuhZxl3Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک‌میلیون عراقی خواهان حضور در تشییع رهبر شهید
🔹
عبیری، مستشار سفیر ایران در بغداد: براساس برآوردها نزدیک به یک میلیون نفر از اقشار مختلف عراق خواهان حضور در مراسم تشییع پیکر رهبر شهید انقلاب هستند.
🔹
پیش‌بینی می‌شود حدود ۵۰۰ تا ۶۰۰ هزار نفر از این زائران از طریق مرز مهران وارد ایران شوند و سپس به‌سمت شهرهای تهران، قم و مشهد حرکت کنند.
@Farsan
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/442276" target="_blank">📅 14:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442275">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e02d90ea3.mp4?token=sigRKWTj6ODJfHJ3c4dbAodbhaF93X1cI3wVp0UaOy8DnPgHLIWS4SV3QyUq6UM-on35gFUjo0cJ_t9BB1fsBrTf09wTnSwPFumaE9cddOZo_qkw9NBdGRb5X-UibqS6jjO1MlH0kH57-bP982W2x9GprYVVnu0CPlRxTzkRw4eOASyRwb0h76jpCZFCn0LIrMR64aSwiLsNrX_REq45OKWqcEfxxLN2hUxG4KNtiyjJPwTUEoZ6UYQAkySTgS1PN7XvBHQvGkrfi8X8nxyMeBP2eShZ_p59JGoqtnKAbKcfVdG3BkiVuwXleQ54O_Vqjowl4mMMEoEgmQ6XEbpRUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e02d90ea3.mp4?token=sigRKWTj6ODJfHJ3c4dbAodbhaF93X1cI3wVp0UaOy8DnPgHLIWS4SV3QyUq6UM-on35gFUjo0cJ_t9BB1fsBrTf09wTnSwPFumaE9cddOZo_qkw9NBdGRb5X-UibqS6jjO1MlH0kH57-bP982W2x9GprYVVnu0CPlRxTzkRw4eOASyRwb0h76jpCZFCn0LIrMR64aSwiLsNrX_REq45OKWqcEfxxLN2hUxG4KNtiyjJPwTUEoZ6UYQAkySTgS1PN7XvBHQvGkrfi8X8nxyMeBP2eShZ_p59JGoqtnKAbKcfVdG3BkiVuwXleQ54O_Vqjowl4mMMEoEgmQ6XEbpRUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبور صفر در تنگۀ هرمز
🔹
تنگۀ هرمز تا اطلاع ثانوی بسته است و بیش از ۹۶ ساعت است نیروی دریایی سپاه اجازۀ عبور هیچ شناوری را نداده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/442275" target="_blank">📅 14:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442274">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87cd6dfe2c.mp4?token=YUqq0D6NL6e1_eJN-D9omHJEO7fTkgD5OObs1q93hKRCIPhBj8WkHccPzNA-U6LUiUqK3EhiVSgpsj9XzIUmpdfU48fpVOjxmmtZJ9fXbQCmTYYjbrBkGm-GFRyiTngBoi6RLwqIUzCNs2G5Bbc278up-Jpsdg2eHeaxhMYX9tihI6R7obRp1M5v-0_22Ayeew4yC-bhgEO1Tbrpgpv8gS-uLduQYgzxMM0s9CBjcE9dbwgLAzFLTiT0Hc-EELMKWMXLGI3cb3-RJJ7qdZFV2dEY31BcqZsVhVzMVWa_DDmk_M0-cMU9EQrwKdW0dUrEf2M4q0S-YqXq2NxB26QhVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87cd6dfe2c.mp4?token=YUqq0D6NL6e1_eJN-D9omHJEO7fTkgD5OObs1q93hKRCIPhBj8WkHccPzNA-U6LUiUqK3EhiVSgpsj9XzIUmpdfU48fpVOjxmmtZJ9fXbQCmTYYjbrBkGm-GFRyiTngBoi6RLwqIUzCNs2G5Bbc278up-Jpsdg2eHeaxhMYX9tihI6R7obRp1M5v-0_22Ayeew4yC-bhgEO1Tbrpgpv8gS-uLduQYgzxMM0s9CBjcE9dbwgLAzFLTiT0Hc-EELMKWMXLGI3cb3-RJJ7qdZFV2dEY31BcqZsVhVzMVWa_DDmk_M0-cMU9EQrwKdW0dUrEf2M4q0S-YqXq2NxB26QhVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهدی طارمی: وقتی مردم زیر موشک بودند فوتبال دیگر هیچ اهمیتی برایم نداشت. ترجیح می‌دادم در زمان جنگ در ایران می‌بودم.
@Sportfars</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/442274" target="_blank">📅 14:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442273">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba73f97814.mp4?token=W82VR4J1GFU_gVjOJSDW40_jQvyXOegxV7-g-okKH0oJq9dFpFbIRL-0I40fzFGGM_9zizmTQBZxtY7wpqpLD61DLFrKhAIwpz8wvciq6HjdHLpm507_aH5pL9NEoSKs7FTadqkGpAvjGvVieIzzLiyIZZ7uQOCRci2AMB79sJJg1SMqD2x0xXa5uUv0E-jLdZRoB0ZmpBo52qb7T8rUrUarod9d2VTiBuz33ToQkoIBLmlt-N2z4ilx6l8jTTqqR5bM1IppZlAYPa-7PEvBxoF_FNx5cdiQnzJtAEIndWZN4aItUgB9JrPr1A0Q0doESyrLAI-2RW47-glZHL4BfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba73f97814.mp4?token=W82VR4J1GFU_gVjOJSDW40_jQvyXOegxV7-g-okKH0oJq9dFpFbIRL-0I40fzFGGM_9zizmTQBZxtY7wpqpLD61DLFrKhAIwpz8wvciq6HjdHLpm507_aH5pL9NEoSKs7FTadqkGpAvjGvVieIzzLiyIZZ7uQOCRci2AMB79sJJg1SMqD2x0xXa5uUv0E-jLdZRoB0ZmpBo52qb7T8rUrUarod9d2VTiBuz33ToQkoIBLmlt-N2z4ilx6l8jTTqqR5bM1IppZlAYPa-7PEvBxoF_FNx5cdiQnzJtAEIndWZN4aItUgB9JrPr1A0Q0doESyrLAI-2RW47-glZHL4BfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار امنیتی خوش‌چشم، ‌تحلیلگر مسائل استراتژیک
🔹
کشتی‌های عبوری از تنگۀ هرمز درحال نقشه‌برداری و رصد موقعیت آبراهه جهت عملیات‌های نظامی در آینده هستند. این کشتی‌ها باید بررسی دقیق شود. @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/442273" target="_blank">📅 14:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442272">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWLqINu6iu_oVHl0J5lX5SGjA0Ba2oiSovbaePIK6vPfvAzv7sQIIySkfHieAq0gkKMPBoMiRAnbFDlAPak36kKuWTRRUqm5fMmG4npWZp480wgQ1A7JwMASzxjNrbVJmv923HaFOw1diupoKUms4ZOtVStEREDZOut2Bsd29JODrY_l51RHKzrXHrHh2XRCj2lGkhICm3nyM2ulHLAxKnw3cTijLHIVrDc-gjI9rAmFiYvrTTtefqryi74-7Kqs_XwHc5elRu4nmExzY-9ibiFob14tzf0DSEIXJlx6Crn6HAeUedQyPI_uTZpFZCzTnXQ7s2F4u01ad-WlD9uPwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: رهبری آیت‌الله سید مجتبی خامنه‌ای در استمرار رهبری امام شهید انقلاب است
🔹
آیت‌الله سید مجتبی خامنه‌ای با وجود همۀ مشکلات و داغدار بودن، مدیریت بسیار مناسبی داشتند و با تدبیر دقیق خود کشور را هدایت کردند. ما نیز باید این راه را ادامه دهیم و تکلیف خود را نهایی کنیم.
🔹
پیروزی ایران در جنگ اخیر حاصل رهبری هوشمندانه، دقیق و مدبرانه آیت‌الله مجتبی خامنه‌ای و ایستادگی ملت ایران در جبهه‌های میدان، خدمت، خیابان و دیپلماسی است.
🔹
امیدواریم یادداشت تفاهم ایران و آمریکا به موافقت‌نامۀ خوبی تبدیل و تحریم‌های ظالمانه و محاصره‌ها که سند زشتی برای غرب است، برطرف شود.
🔹
مردم در ۱۰۶ شب با انسجام و وحدت ملی ایستادند و رفتاری کم‌نظیر حتی در مقایسه با مقاطع مهم تاریخ انقلاب اسلامی از خود نشان دادند.
🔹
جبهۀ خدمت نیز خوش درخشید. انصافاً دولت به‌ویژه شخص رئیس‌جمهور، در خدمت به مردم باوجود همۀ دشواری‌ها، هوشمندانه، شجاعانه و دقیق عمل کردند و دولت در این آزمون ملی خوش درخشید.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/442272" target="_blank">📅 14:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442271">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9INC-g5coZxB1l5cMgnfO67OxGZ3R0gccf6qXYR_ovn2Knjv3rZL1IP9xjvIJUDAk-Gfi-V_l65lqvi_2OAHjLxiHFQKDs7etBd5LGNMXJS8eSu1lpc8gyEdZXP6OZJ8N7OafzBXViu09_UN9aekHBuKr3n8EoI6ZPoQmvwkHDWSL01kwfliL1VBjwrGZT6Of8t9x5BZeTAnX_u6TuU5gOnCQWwsUuhllxbPMYR0Ro-RsnDKb8l0k31D6s_wgdnEKztfKUGTP-K-9Eun43nDDJEFF3DCwpRqddRdqGfKAEo_rgni91qh1eSucaeODc4YX4wyz-hS2zP8TdnoScHwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
انهدام یک هستهٔ تروریستی ۴ نفره، بازداشت یک جاسوس و ۱۲۶ عضو شبکه‌های اغتشاش خیابانی در طول جنگ تحمیلی سوم   @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/442271" target="_blank">📅 14:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442270">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eee2ec1f6.mp4?token=Uz6aHwdU_PmCDErXm__T7_Fe3qf2--3L16ocmuukOGzmEUOvvs04zlWkt-8BFkLXNEyXkgx8GEH_0HFJO-NgAhEIcj0pUfKrkzgS4VxKDMw-iwd4kgfKL95nrk1mgH3oNMpmNz3yISrX-ct3pQveZgh0kHH9QHd8KQlb2qY8AMgqQ4DPtogQpqPEClmUDpqE-2r8N5Ufs0-Nh4SQm_-JXk-fAoGZos6FwRr6hzdL4sYwPAEWBr_ruA7eJk4RilKcWXgnbWdicsF5laNjxFrX8NHqHOork_lOnPr50028zkgjaoqt5rJxbA08T7Sq2wA7qIrc-v_1-iqZJxCemU1eVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eee2ec1f6.mp4?token=Uz6aHwdU_PmCDErXm__T7_Fe3qf2--3L16ocmuukOGzmEUOvvs04zlWkt-8BFkLXNEyXkgx8GEH_0HFJO-NgAhEIcj0pUfKrkzgS4VxKDMw-iwd4kgfKL95nrk1mgH3oNMpmNz3yISrX-ct3pQveZgh0kHH9QHd8KQlb2qY8AMgqQ4DPtogQpqPEClmUDpqE-2r8N5Ufs0-Nh4SQm_-JXk-fAoGZos6FwRr6hzdL4sYwPAEWBr_ruA7eJk4RilKcWXgnbWdicsF5laNjxFrX8NHqHOork_lOnPr50028zkgjaoqt5rJxbA08T7Sq2wA7qIrc-v_1-iqZJxCemU1eVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشدار امنیتی خوش‌چشم، ‌تحلیلگر مسائل استراتژیک
🔹
کشتی‌های عبوری از تنگۀ هرمز درحال نقشه‌برداری و رصد موقعیت آبراهه جهت عملیات‌های نظامی در آینده هستند. این کشتی‌ها باید بررسی دقیق شود.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/442270" target="_blank">📅 14:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442269">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXKachlSsb_fo8PRakXH5PkTNdaeAftcgEV3b8F9yEAHJYOvSvmwUZSgzxetnbWAHWGsDu62-w-m1P5uCxInYkghcVmur4ZIYeSYEZDbf-k8Y6NrKxy0iDLvyRLE9Qf2cenpYD8uPYzAwozfPwCZVc-xHVR2ZyJmPHjFbFUNF7rIYk9dULhw0tSQxiC2S0y6LdvfvU_mCSPjEEzMsF2WeCnmvawyud73tlmOIxjwTeE4h37fLSy8bhYghuEhDKqRRy6QWFBuRQm6k7-DU4Si7_0rPifEcXrOMEFwFaC8Kiv51ve-x25FzYhLtxmiv84r4ygOTGhPzggOcmXaLWAc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر حاتمی: دشمن فهمید باید به ایران احترام بگذارد
🔹
فرماندۀ کل ارتش: دشمن در جنگ رمضان و جنگ ۱۲ روزه تصور می‌کرد با به شهادت رساندن فرماندهان و رهبر شهید انقلاب می‌تواند کار جمهوری اسلامی را تمام کند، اما محاسباتش اشتباه بود و ملت ایران بار دیگر در صحنه ایستاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/442269" target="_blank">📅 13:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442268">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfKQ1Nsw6vuOZAc1UUjiFhwRlWwLSvAaHv66gudlNJSe4VEEJ3eAB9XcpekrEmA88iXHEO_VaJkaJ8AUCwER0whHvBAIpZfry74Ur7SbajlaqReN9tHv2D8i3hZNvGtJPAdj6mS1YTMBnJP1otxJafZHN9acPg8PVSoZvdzift3d2zHi41saZXJVCCzBKQBl2ehg2n_H3OMQGn68Lq8a6fQsBFKqMkbxTKEMAOn8sb3QuJ4d2bL2Yrl4TLxOLW30b47oU6i_O2XekIogTZ8YS0mdW9myKEfWHaaGqXtv_apmRYzDgf2CDsNyRvfFr_fWamXAvIhSYr-rC-XVRMBPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
حمایت ایران از لبنان
🔹
کاریکاتور جدید کمال شرف، کاریکاتوریست یمنی
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/442268" target="_blank">📅 13:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442267">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پس خون رهبرم چی؟
🔹
بامداد امروز پس از ماه‌ها کشمکش، یادداشت تفاهم ایران و آمریکا نهایی شد. با این حال، در روزهای اخیر موجی از سوالات و شبهات در میان مردم چه در تجمعات خیابانی و چه در فضای رسانه‌ای شکل گرفته است؛ شبهاتی که به گفتۀ برخی ناظران، نبود اطلاع‌رسانی شفاف و به‌موقع بر دامنه آنها افزوده است. در چنین شرایطی، تحلیلگران حاضر در مذاکرات تأکید دارند که دشمنی که با ادعای «تسلیم شدن ایران» پا به مذاکره گذاشت، در تمام اهداف راهبردی خود شکست خورد.
هنوز پیروز نشدیم اما دشمن شکست خورد
🔹
محمدمهدی رضایی تحلیلگر مسائل سیاسی با اشاره به مواضع پیشین آمریکا توضیح داد: «آمریکایی‌ها آشکارا اعلام کرده بودند که ایران باید تسلیم شود، برنامه هسته‌ای و موشکی خود را برچیند و مواد هسته‌ای را بدون قید و شرط خارج کند و از حمایت جبهه مقاومت دست بردارد. هدف پشت این خواسته‌ها چیزی نبود جز براندازی نظام جمهوری اسلامی ادعایی که مقامات آمریکایی بارها به آن اعتراف کرده‌اند.» اما نتیجه نهایی مذاکرات چه بود؟ به گفته این تحلیلگر، آمریکا به هیچ یک از اهداف خود نرسید؛ ایران نه تنها تسلیم نشد، بلکه در جریان این مقاومت، قدرت بازدارندگی خود را تثبیت کرد و رسماً از سوی برخی ناظران بین‌المللی به عنوان «قدرت چهارم دنیا» نام برده شد. رسانه‌ها و چهره‌های بین‌المللی – حتی حامیان آمریکا و اسرائیل – روایت تحقیر ترامپ و ایستادگی ایران را بازتاب دادند.
🔹
وی تأکید کرد: البته این به معنای پیروزی مطلق ما نیست، اما یقیناً معنای آن شکست قطعی دشمن است. دشمنی که می‌خواست با به زانو درآوردن ایران، برای کل دنیا خط و نشان بکشد، خود مغلوب اراده مردم و نیروهای نظامی ایران شد.
هزینه‌ها بهای مقاومت، نه نشانه شکست
🔹
در این گفت‌وگو به خسارت‌های سنگین وارده نیز اشاره شد: شهادت جمعی از مردم، مسئولین و فرماندهان و بالاتر از همه، شهادت رهبرمعظم انقلاب. با این حال، این تحلیلگر تأکید کرد که هزینه‌های سنگین به معنای شکست نیست: «شکست یعنی طرفی که جنگ را آغاز کرد، به اهدافش نرسد. دشمن جنگ را شروع کرد و به هیچ هدفی نرسید، این دقیقاً تعریف شکست دشمن است.» او افزود: «ما عزاداریم و خونخواهی رهبر شهید و مردممان را فراموش نکرده‌ایم و تا قصاص ترامپ و نتانیاهوی جنایتکار آرام نخواهیم نشست. اما نباید تحمل هزینه را با شکست اشتباه بگیریم.»
چرا برخی اصرار دارند روایت شکست ایران را تبلیغ کنند؟
🔹
بخش مهمی از این مصاحبه به بررسی شبهات برخی افراد دلسوز و مومن اختصاص داشت؛ افرادی که به گفته رضایی، اصرار عجیبی بر تبلیغ روایت «شکست ایران» در افکار عمومی داخلی دارد. او با اشاره برخی مصادیق این سوال را مطرح کرد: «آیا با تحقیر ملی سودی عایدمان می‌شود؟» به باور وی، مهمترین دستاورد این جنگ و مذاکره، اراده، اعتمادبه‌نفس و باور به توانایی ملی بوده است. مردمی که در برابر ابرقدرت‌ها ایستادند، امروز با پوست و گوشت و استخوان خود درک می‌کنند که باید قوی شوند و این قدرت بالقوه را به فعلیت برسانند. اما برخی به رغم حسن نیت، می‌کوشند این دستاورد روانی و راهبردی را نادیده بگیرند و شکستی را روایت کنند که در واقعیت رخ نداده است.
هوشیاری از موضع قدرت، نه از سر ضعف
🔹
رضایی معتقد است که متن توافق نیز مبتنی‌بر بی‌اعتمادی به طرف آمریکایی تنظیم شده است. این تحلیلگر مسائل سیاسی با تأکید بر اینکه «ما هرگز به قاتلان رهبر شهیدمان اعتماد نداریم» خاطرنشان کرد: آمریکا همواره پیمان‌شکنی کرده؛ بنابراین برنامه‌ریزی باید به گونه‌ای باشد که چیزی نقد به دشمن داده نشود، منتظر «نسیه» نباشیم و گام به گام از موضع بالا و برابر حرکت کنیم. او این هوشیاری را نه از سر ضعف، که از موضع قدرت توصیف کرد.
🔹
رضایی در پایان تاکید کرد: «ما نمی‌گوییم حتماً پیروز شدیم؛ اما می‌دانیم که دشمن قطعاً شکست خورده و افکار عمومی جهان این را درک کرده است.» اصرار بر روایت شکست ایران، خواسته یا ناخواسته، خوراک تبلیغاتی برای همان دشمنی است که تحقیر شد. دلسوزان واقعی نظام که خودشان به درستی به رویه خودتحقیری برخی غربگراها انتقاد دارند، به جای تحقیر ملی، باید با تقویت نقاط قوت، خونخواهی شهیدان و مطالبه گری صحیح به تکمیل مسیر پیروزی کمک کنند و بدانیم که پیروز نهایی – تا نابودی رژیم صهیونیستی و استکبار جهانی و قصاص ترامپ و نتانیاهو – هنوز محقق نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/442267" target="_blank">📅 13:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442266">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quvEOl4EQ2VtsEMF4plAAxsUTwp9dkuA-oK36MCC37wdvj7Xkx5dZm58rD4-6u63Hx6tZ52KufqZHEiFmfrnEioqa4kv1OkbBd6gKmyLv22AxutX7Ml3bmX1LVbF6Ilm6x-qv7SxgFoDZJqSEFs3KBt441acNrT6oAdkuAWCyxyE9BUCDe2-DFE_nHRTIxGJxDPR4IJH2wmb8pOObZ18ejMcHKzoMb61K10PcdlS2jkUDggK8TQ0aeSd2NHYtJn3p6yetC3P4lyW1rr8rSDZDTlt-VvlXLMVqUts91Q5L5pDVwDSDppeATfOR_Au8sHWFG-VRsN2LwBq29SfJOGeBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس با رکورد جدیدش از ۴.۸ میلیون هم عبور کرد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۳ هزار واحدی به ۴ میلیون و ۸۱۹ هزار واحد رسید و مثل روزهای گذشته رکورد تاریخی جدیدی را ثبت کرد. @Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/442266" target="_blank">📅 13:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442265">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8AsIMXqxVP-TbB8qE7cRAsw6TUt6v8H7MxPfg6cCywf0tY0TrbY4EIPXy3SBbnt_-TmZ8A0aGdqD_IY6C8TTM5VGSNBFOhsTgewkp3xQVNxsmlDhYHm7s7fG62I-hoPIocLuQLDTRYc_LVq_OgfgbyL6ejnlLKh8D9QJK0wdguzj6XJanwDdQPzuutv8Wd-D1oox9uMozcWPXQHCPBzFp08mS72R2q5kOLTMmUGgbAx4YG_16cka-LRuqIszgjQkEaLy8uSf_vgMYf0InC8HZh5jaBsuxue3TkGs3GSf8jOUbpuSdG1q9LWc0nx5P1XCadDd-1jlB_5QRsUe1MUow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زابل گرم‌ترین شهر جهان شد
🔹
داده‌های هواشناسی جهانی نشان می‌دهد زابل در ۲۴ ساعت منتهی به صبح ۲۵ خرداد با ثبت دمای ۴۷.۶ درجه، گرم‌ترین نقطۀ جهان بوده.
🔹
شهرهای الاحساء عربستان با ۴۷.۴ و سبی پاکستان و ینبع عربستان با ۴۷ درجه در رتبه‌های بعدی قرار گرفتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/442265" target="_blank">📅 12:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442264">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plnJ20pma1mOaxdQytmoqwC5m_LxI8MgilnJY99-uLbZ5MAZRLOQ6sWc6czkh6cGVMCHrt6ZX50CgI8UfCZymMJsP6L-d-ZORvrxAdzWc2NERYOTYSb5IVaQWJQgXQIOfAm5seHy6u627zCM4RFJ7NZS36HGbi-1_Q7FikMbz7zF16wAhPSRA3JmbJhlGyQjXyVb_aaFMTyQMNK_Jk7v6ydv4Ss91B0Zh6UA9iEiYd6evVMLCYoG66J678dbrph99qrWvA70iihvhFFVH2R6nqoF2IL8sjgFkO6zj9iWLX7DFXvVI0CBBFeRD6sbgD8UMzPWKOqFiDp7JDL8fkjXOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقوع حادثه برای یک کشتی در نزدیکی یمن
🔹
سازمان عملیات دریایی انگلیس: گزارش‌هایی درباره حادثه امنیتی برای یک کشتی فله‌بر در آب‌های جنوب یمن دریافت شده است.
🔹
این کشتی در ۲۶ کیلومتری جنوب عدن، گزارش داد که یک قایق تندرو حامل چندین سرنشین به آن نزدیک شده است.
🔹
سرنشینان قایق تندرو به سمت کشتی باری تیراندازی کرده و سعی کردند وارد آن شوند؛ تحقیقات درباره جزئیات این حادثه ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/442264" target="_blank">📅 12:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442263">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
ماجرای تغییرات لحظه‌آخری یادداشت تفاهم ایران و آمریکا چه بود؟
🔹
یک منبع نزدیک به تیم مذاکره‌کننده در گفت‌وگو با خبرنگار فارس جزئیاتی از کم‌وکیف اقدامات ۲۴ ساعت اخیر دربارۀ توافق با آمریکا را تشریح کرد.
🔹
به‌گفتۀ این منبع، پس از آن‌که روز شنبه کلیات یادداشت…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/442263" target="_blank">📅 12:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442260">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fnu5FzLm2iLxgDtGzrk-NwsQeI0tAs1TecixsRMtD7F0CZCqboUNNj-IFCFhIHVp2AaL1-m3oVCRCc5WKNBq-to0HAtB2HAeqiKWTNeDlLfFhh3xAcR7IMJgcxgDn1yxJNjiMePCDhzYid2Mh9aw0vC7RCpzvjAZQG2NvoHtpm-iZta6gN0AkVL4jdk2IToCsdmaFXF1qDLXs6BbzYxAHqGKP4fT3p7jXxSvMx4OiQ6C7mVkIFZVgoaF7CoenldKmLLcZYSEMNm4HGMkQgHkgAiQBlSKsKuXN1CMtcEwelghPO6I2hNTJ8KAha2hB14cvCYsvB63R27xM3uUOSiHJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V6eWd_TdgqmfPlz00o5nd-lttubRDXkYPqKuuLhJ4VYqKdsW86pLVgpDC7sJ5xDpTgAf2Y1JunqTmxJa74IQmmwsw0soN2W25tRIHYnlsa6dy0KWf2wivEI-FZDAAVu7wRJ43--fHBtTJ023TI-6XtWcGK81f4PkYa2qkaRyDfL6ug0A-026E-0P5rp9Nrl52fxH1Jhbv8mNZftFqVi_vaYA9QT99IUo7O9rNkmK237pf7U2MRrAopzeK2v91Zi2l358i8ZtNqm1A_Unw3AAtNkHy-cgDQAEKuGOXABFGO4pa7f_V6D44JXCH9g77S1o7AqHMI9mZgNeoWMVmSpucg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b075e3305.mp4?token=LHmGYLmJcWQfGh9w8v38SRnqXbNDUxCLn0FNbNVIjnDdejjEFJ3cD5vl97JwSAWC_xl2chVemcs3Ob7hE9LfC-gbo3Ey5ZJ-wiFfRKMFUZv3hwW3Tr7JL5AeRxvR9cIoeQjAMCvQGV7O-OSrqahlwnx2Fm8S9qSGHicXsIjO4OYSZt0386v3-YMjiOz09rJOwLpJ3iBIrp-j6VvI2Ldnr9HJAjC8D03l9AJHZNIKuktSdibEndzxGTEn8ts1h29LDaLPSPPVk9d0nXZ7dlg2Kal76KxQlTDur8BvAvd-n3pIMRf_6aWWtxY00BZf7ENvcwelgOmbA_3tMhNediDzbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b075e3305.mp4?token=LHmGYLmJcWQfGh9w8v38SRnqXbNDUxCLn0FNbNVIjnDdejjEFJ3cD5vl97JwSAWC_xl2chVemcs3Ob7hE9LfC-gbo3Ey5ZJ-wiFfRKMFUZv3hwW3Tr7JL5AeRxvR9cIoeQjAMCvQGV7O-OSrqahlwnx2Fm8S9qSGHicXsIjO4OYSZt0386v3-YMjiOz09rJOwLpJ3iBIrp-j6VvI2Ldnr9HJAjC8D03l9AJHZNIKuktSdibEndzxGTEn8ts1h29LDaLPSPPVk9d0nXZ7dlg2Kal76KxQlTDur8BvAvd-n3pIMRf_6aWWtxY00BZf7ENvcwelgOmbA_3tMhNediDzbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملات رژیم صهیونیستی به جنوب لبنان
🔹
منابع لبنانی از حملات هوایی و توپخانه‌ای رژیم صهیونیستی به شهرک زوطر، مرکبا و شهر الخیام خبر دادند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/442260" target="_blank">📅 12:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442259">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mg8qaR5Fbq12NnUS4vEwGcdjHwu8Rx7E07buIEDMkbFJmIz5TxhMMFcKENIdO-eaCVCd2aVGt3FiFMtoDvpIKZStEB4k1ZCV-23nOq7hzxNyroAc_LMfTPD8cQmkRt565s0y7J2j-tCu2p2e219PjePO9qb8Ynti_spnDTS2YeXeUB7YJ0ruiBv37AjwmgAshz1ZsSKqCOkU5ZMYkRdZowTKBZYhmgScZ0cimWksCXaG8IeKSwoITtwRO3NhWZn_HONkA4q1lv_WeiFTF_vDEAIcM0CJObsubobzvqu3gh46LLoiNdy4wgpEE_EO8HlFQvr49HgEgmgTbx0WGthDHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر جنگ اسرائیل: قرار نیست از لبنان عقب‌نشینی کنیم
🔹
اسرائیل با وجود همهٔ فشارهای کنونی و آینده، با خروج ارتش از لبنان مخالفت می‌کند.
🔹
من و نتانیاهو سیاستی روشن را دنبال می‌کنیم که براساس آن ارتش اسرائیل برای مدت نامحدود در مناطق امنیتی لبنان، سوریه و غزه باقی خواهد ماند.
🔹
این سیاست شامل تخلیهٔ منطقه از ساکنان محلی و نابودی تمامی زیرساخت‌ها، چه در سطح زمین و چه در زیر زمین، از جمله خانه‌های واقع در روستاهای مرزی است.
🔹
نتانیاهو این موضع را به رئیس‌جمهور آمریکا و دیگر مقام‌های ارشد آمریکایی منتقل کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/442259" target="_blank">📅 11:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442258">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3c004074d.mp4?token=UMKRjsE9GMM15T8lBfm-bbHLkqWSmhEqHBdDOYjdRqIsAdtc6VJXAcytKdA3l7fwxK9SMPuHGm3XXkGOMDU_vnZUBgwNvxiGw-HRnzO5oe11VTd_1tdGFYBRva_OEpttjaSzCJ8Htyvxgf2z6Zr78RMq3bsi2iTtknHLG2Q6fudcxdPG6Ymmdn3gU6IBmCNGOjOpllJVu4DLFdmAMzIj69yVhV3ruKn3aMQ7U03r72yIll78hzEY5lx2g6ilKVqz9GdGo-f8jPMifpYf20OlBYO6st5CPC_EM2FQTEF90bYe-4P3q4npmBB2JsnPxOLvaC1vEQOCEwwZFbCxtbNsDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3c004074d.mp4?token=UMKRjsE9GMM15T8lBfm-bbHLkqWSmhEqHBdDOYjdRqIsAdtc6VJXAcytKdA3l7fwxK9SMPuHGm3XXkGOMDU_vnZUBgwNvxiGw-HRnzO5oe11VTd_1tdGFYBRva_OEpttjaSzCJ8Htyvxgf2z6Zr78RMq3bsi2iTtknHLG2Q6fudcxdPG6Ymmdn3gU6IBmCNGOjOpllJVu4DLFdmAMzIj69yVhV3ruKn3aMQ7U03r72yIll78hzEY5lx2g6ilKVqz9GdGo-f8jPMifpYf20OlBYO6st5CPC_EM2FQTEF90bYe-4P3q4npmBB2JsnPxOLvaC1vEQOCEwwZFbCxtbNsDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امیرالمومنین(ع) سیاه‌پوش عزای ماه محرم شد
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/442258" target="_blank">📅 11:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442257">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">جلسات شورای شهر تهران علنی شد
🔹
سخنگوی شورای شهر تهران: جلسۀ فردا در صحن علنی شورای شهر و با حضور مستقیم اصحاب رسانه برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/442257" target="_blank">📅 11:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442256">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e70803c3.mp4?token=chdhlfkIwZ8aaBSUe82oX_3V158SndW7F8XjtK68_oq1bTyQcBvPxKJnaI8SBA-kBnHNOgf3oace9lb2SPNDIfsaQZwTUhPqq7bXWA9l9SAY6HcK4KUVk1W5dzWPX2BRXIuGnva0eOInYfp9VcpHRsFhQPMx3PmQxcb10Sb42ECOAArRIh-NbH7PA00eCfoZeAvP3sfwbh5GSD4ONCaSFz9oyMSwATUAKT3oRwskvvM9StKypIhqDOYP_eVLQnO9PddL4gXahrHzCJr1KjivinzgpaYD7htnOy0t6i9JGV71wskCCb4ZNfQhSzTrG9dVvE9agWuDTcrz47kWCUAPQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e70803c3.mp4?token=chdhlfkIwZ8aaBSUe82oX_3V158SndW7F8XjtK68_oq1bTyQcBvPxKJnaI8SBA-kBnHNOgf3oace9lb2SPNDIfsaQZwTUhPqq7bXWA9l9SAY6HcK4KUVk1W5dzWPX2BRXIuGnva0eOInYfp9VcpHRsFhQPMx3PmQxcb10Sb42ECOAArRIh-NbH7PA00eCfoZeAvP3sfwbh5GSD4ONCaSFz9oyMSwATUAKT3oRwskvvM9StKypIhqDOYP_eVLQnO9PddL4gXahrHzCJr1KjivinzgpaYD7htnOy0t6i9JGV71wskCCb4ZNfQhSzTrG9dVvE9agWuDTcrz47kWCUAPQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: زیر بار زورگویی آمریکا نمی‌رویم
🔹
ما که تسلیم نمی‌شویم تا هر غلطی خواست بکند. آنها منتظر بودند ما در کشور با قحطی مواجه شویم.
🔹
اگر دانشگاهیان به میدان بیایند، از بحران‌ها عبور می‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/442256" target="_blank">📅 11:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442255">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در مبارکهٔ اصفهان
🔹
سپاه اصفهان: به‌دلیل انجام انفجارهای‌ کنترل‌شده تا ساعت ۱۳ امروز، احتمال شنیدن صدای انفجار در مبارکه و اطراف آن وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/442255" target="_blank">📅 11:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442254">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXCkyM04dxnrxMVbDHtHYYiu3BLD3lmQ_-Gzc_ipsX5x3Zh6KM4uCLKK_vVl5JKOPlGYwOdNQdJcsDKXDNlSP5b2QUGpDTX8DMUFiZkZ6rUG7kvDa8Tk__sOspBfAr0fXCHXlAGWmulp1U3TMlkEJEvfi2zXX9sqrZCUcWaISy9iU-YXMj2gd09P89HU9g01P5DmyopqMjZ4sQO3sS6WBzHSeutLKjI0BfxoERM5ddhnOhJAk8s8rTYkoYayxu_dujvTNgdyWd84Gd8yYgK5uA6A4Y96lY1gPbtCL1Pkb2Rh1I9AoLvdiWmeOZSTt1mku4EGEWLCIdCDx0I_F2eVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لَا یَوْمَ‏ کَیَوْمِکَ یَا اَباعَبْدِاللهِ
🔹
به‌مناسبت فرا رسیدن ماه محرم و غم فراق رهبر شهیدمان از جدیدترین دیوارنگارهٔ میدان ولیعصر(عج) رونمایی شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/442254" target="_blank">📅 11:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442253">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7fHKIAF4o-dRussQUfdbvYoo6MvpOpIH8pIoUW-wJIZbdxl7H57X-G4Zu60hIJ6zVkcLhBvHjz2VQbAxB4AUXVdr5VJtMKzaJGoWFQp9Y9BC-B5XGiR7tIiV1V3zP7NM5rNGITXutmOWyDjmT9hwZ1diprh9jW7OqCb3TVohlNMxg1n83njRSiOLcQSfJ3cplogekvtxSuvgnQTDKRMA7YJGMhrfEQydABUKUCJbF_Rgpu5C54jD1e-mtt7uXenXh6-p2LcMOtBvXYxUyHeCwG_iI7BhHykMp_clGMB4Pt229i-enFxMf7iC2tKT7TYst8boLSeCK3gXHAVm1A8Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفت‌وگوی تلفنی عراقچی با وزرای امور خارجهٔ ترکیه، عراق و مصر
🔹
وزیر خارجهٔ ایران در تماس‌های تلفنی جداگانه صبح امروز با وزرای خارجهٔ ترکیه، عراق و مصر، با اشاره به مسئولیت آمریکا در قبال اجرای توافق، بر لزوم توقف کامل تجاوزات و حملات بی‌ثبات‌کنندهٔ رژیم صهیونیستی علیه لبنان تأکید کرد.
🔹
وزرای خارجهٔ ایران، ترکیه، عراق و مصر همچنین بر تداوم رایزنی‌ها و همکاری‌های نزدیک در خصوص تحولات منطقه‌ای و ضرورت تقویت تلاش‌های دیپلماتیک برای حفظ صلح و ثبات تأکید کردند.
@Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/442253" target="_blank">📅 11:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442252">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حذف وثیقۀ خروج از کشور مشمولان غیرغایب در محرم و صفر
‌
🔹
سازمان وظیفه عمومی فراجا وثیقۀ خروج از کشور را برای مشمولان غیرغایب در ایام محرم و صفر حذف کرد.
🔹
متقاضیان زیارت اربعین می‌توانند از ۲۶ خرداد تا ۲۲ مرداد درخواست خود را در سامانۀ
sakha.epolice.ir
ثبت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/442252" target="_blank">📅 11:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442251">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/615a222da0.mp4?token=oxgYpQXf_rCRz9nHQ_6OPCCEdF94xzekqBJUD_BY8PWiExsqVmrIiQRiXxRxDfotfNSzSmPDLEItW69tH4iR_U2BM6TaKravjtSXUOvPvfIN8k7FAmo8j_o0a1oEiIl8IRDkVdau_XG7V9Kzj0JtLF7QaNroFYs7HnQdk-V0WG9QIH9p2JfGA1AB1vICAJRPhrjOHq0uyJnbJvA51AL1mm7fzNp6rKg1Ul8sALFREUj6gJ9NvCJDJLc1Uq9eAN7i0a5jsi0wE_DGbznUluPMSgvR8ts5pcdxK-33NkHqq6P6m4nMEu0KOHof4YeXoGUqgPjJXHVRagPf_B-h_VhxTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/615a222da0.mp4?token=oxgYpQXf_rCRz9nHQ_6OPCCEdF94xzekqBJUD_BY8PWiExsqVmrIiQRiXxRxDfotfNSzSmPDLEItW69tH4iR_U2BM6TaKravjtSXUOvPvfIN8k7FAmo8j_o0a1oEiIl8IRDkVdau_XG7V9Kzj0JtLF7QaNroFYs7HnQdk-V0WG9QIH9p2JfGA1AB1vICAJRPhrjOHq0uyJnbJvA51AL1mm7fzNp6rKg1Ul8sALFREUj6gJ9NvCJDJLc1Uq9eAN7i0a5jsi0wE_DGbznUluPMSgvR8ts5pcdxK-33NkHqq6P6m4nMEu0KOHof4YeXoGUqgPjJXHVRagPf_B-h_VhxTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روایت جذاب از مسئولیت‌پذیری و همدلی؛
این انیمیشن یادآوری می‌کنه که صرفه‌جویی در مصرف برق، یک انتخاب کوچک با اثری بزرگ برای همه ماست.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/442251" target="_blank">📅 11:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442250">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEQptnWAtHyd7uKOGoWSG1PvKsOBareR47kaMJFnsvs5AFKd_RwMHsmR-0jMlwUWgslgNuIrVXL7DAYSFuk9FqOc53rJR38dn7jgl1k2O9fxe-zfvA9T_HEcoArwD0RTVKl1Ufev5rsJKx-W0gCThweSugyHdivLduA763SdXNDEDWgnhr8mnNx5VQ561RFzzcurQHDx_YsG-8L3ios4Gas0r_Jnm0_MLCJHLIA7SVZZyN_Z35fjCj149Wr5dnaqQx3HWFhLHeYav5n1TYkli7bSGFopmn4yahuPpcjXhUbdGdOR6QD0XkSoOmwrou5WgSMy8800RWJQYGOfJojbiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
مبلغ تسهیلات قرض الحسنه بازنشستگان به ۶۰ میلیون تومان افزایش یافت
🔹️
مدیرعامل بانک رفاه کارگران از افزایش مبلغ و تعداد تسهیلات قرض‌الحسنه بازنشستگان خبر داد.
🔹️
دکتر اسماعیل للـه گانی با اعلام این خبر گفت:  بر اساس تفاهم نامه با سازمان تامین اجتماعی مبلغ این تسهیلات در سال جاری از ۵۰ به ۶۰ میلیون تومان افزایش یافت.
🔹️
وی افزود: برای این منظور بالغ بر ۲۰ همت اعتبار برای پرداخت ۳۴۰ هزار فقره تسهیلات از سوی بانک رفاه پیش بینی شده است.
🔹️
این تسهیلات با کارمزد ۴ درصد و بازپرداخت ۲۴ ماهه به صورت کاملا غیرحضوری به بازنشستگان واجد شرایط پرداخت می‌شود.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/442250" target="_blank">📅 10:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442249">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/442249" target="_blank">📅 10:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442248">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083b61f28f.mp4?token=gQ1v2sGIprF8iGEUEKhTMkKW1qwcbkzci11dcifAEy7kEvLVimL-5peAogA0f7b9VUBnNsvP8J2000hICLZyp_B2111PrGh2rNAsiqJF9eaL4t_EIMFpDVncR_d5tSULnIlEoac30NlDScr9-aAes2TtUy0Gd8tLc4-tZQmevPEaxS4x0yHrgJn4IHL23kke5thLpwuyvDP8plL6xgul3naDVqUK3eXia1qYnIpEEWtHYxDayPjElYfxV2t9qLajhy56KXecE8guVVTG1BsvHj-VY9ncG87IvUrO2TiCoEhMaVoOWmPaNFkMmROJ39RSFFtZOVDAzZo-Il4Qn9CScg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083b61f28f.mp4?token=gQ1v2sGIprF8iGEUEKhTMkKW1qwcbkzci11dcifAEy7kEvLVimL-5peAogA0f7b9VUBnNsvP8J2000hICLZyp_B2111PrGh2rNAsiqJF9eaL4t_EIMFpDVncR_d5tSULnIlEoac30NlDScr9-aAes2TtUy0Gd8tLc4-tZQmevPEaxS4x0yHrgJn4IHL23kke5thLpwuyvDP8plL6xgul3naDVqUK3eXia1qYnIpEEWtHYxDayPjElYfxV2t9qLajhy56KXecE8guVVTG1BsvHj-VY9ncG87IvUrO2TiCoEhMaVoOWmPaNFkMmROJ39RSFFtZOVDAzZo-Il4Qn9CScg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهروز رضوی، گویندهٔ پیشکسوت رادیو و از صداهای ماندگار ایران، پس‌از تحمل یک دوره بیماری درگذشت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/442248" target="_blank">📅 10:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442247">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1NEfPnbf1oNLwIS5wvNZjwcWNJTtH-dvjd5bpDszuDh8D38ueJvrqnwXfCzNGNf0htkwbpErMMMs5ibu3owpdysoJZTqMRtIC4YRIQ0708GSYvzIKnBkaB1K2xjGHSDiXqZhoVNfBIdcBfcggwEcc7dTWWiZCrsbjL-RHbfjIu3OpZmOPLlJzVCjbTL07-DREUsh1Wa5enepSSM1CjrGNlZubviuAnMe1Tb5HJpRbIBjk7j586cLsDjwuwyX9hMOG3jSZVrPnXQ2Fu62F96Htkkvmk8QfgcEee7XlJYsCav6OZm5EohPEb2WDAi6FMrbsEGaHRglHvznjpktAA4WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعمال محدودیت و خاموشی برای بدمصرف‌ها
🔹
وزیر نیرو: اعمال محدودیت و خاموشی باید متوجه مشترکانی باشد که الگوی مصرف را رعایت نمی‌کنند، از سقف مجاز تعیین‌شده فراتر می‌روند و عملاً بدمصرفی را ترویج می‌کنند.
🔹
باید با استفاده از منابع و ظرفیت‌های موجود، شرایطی فراهم شود که مشترکانی که الگوی مصرف را رعایت می‌کنند، مورد حمایت و تشویق قرار گیرند.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/442247" target="_blank">📅 10:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442245">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDqsfXL4nbrG1HwQmiki3sMPPpD_EhJwec_2BmQSFQY2wkuFNZFA6GBGL6XoMK10xzwCUQohPMXgUPTieWICJro3TwiFa3IPFNWl-df84fV18qp3fp0d_SEkjZvTbrkfmyCrFa-cLGmSARnH0bp0E5h6VxYmqto0DpoRJFDnQyc9AQDk0RmSq4_Mr4ttKuB7bL74QOQl7shu5Oyv65TRIy1L0tXzKhw65R-LIfCoHPnMvkcW7DSdf0Qe-5Qq9xphaPM10cEh-hxTIyZe9P5n8CLRqq7RVdzw4f6T9LZHgbtYEeXxB_fFSZuZGHweOFSD_YdKaoTRZ49d5Y-U1rDwRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلال خدمات بانکی ۴ بانک برطرف شد
🔹
شرکت خدمات انفورماتیک اعلام کرد خدمات خرید، انتقال وجه و مانده‌گیری بانک‌های ملی، صادرات، تجارت و توسعه صادرات به حالت عادی بازگشته است. @Farsna - Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/442245" target="_blank">📅 10:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442240">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmrUKiDOr9pK3NxPCeQzK-t0Tb6OmzPr6ZlM7reWJz72Mzo2c-qslnPSSd0WpDvHFxG41tEfRedLcamFBVuuVSm1WNqrZifWSvaXlc2Yo69zHmGwehe7Z8WHTY3rFPA_gA9qz_-DhH--f9KTHTljrdohmlMb2HUxCJ4ocg2jGHIa2ZWAdSkiJYf2sroHVcr5FQTklhX6N6B75Fge2f8K6GgjLYbxPAZZO_3VUZiaXzaGWBgV_WthFpB1EKirwjZJsfm6AXj5PoUUhGyxSILf4J1I2xt5YL7u1nhEpU0MSNj45bZjfUteJzp1msFtAbxdJNdNJ0z4zHR5T__x8LLfmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهروز رضوی، گویندهٔ پیشکسوت رادیو و از صداهای ماندگار ایران، پس‌از تحمل یک دوره بیماری درگذشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/442240" target="_blank">📅 09:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442239">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68bc8b1da1.mp4?token=WsGzDV0gSZ4kcfwp-jxiKZUXA2nzyupQxbeSopWxeMrPzaNGA6Et8YNXrCesX0U0PEy9x0TC0jhFeZtGNAPNvsIpxKny1u0PUmbJvNBtwihcMY5GhfdSW8AgJiv-F18TomBkP0pLdIY0SmRww7e5i77-8E3VhwibsZtzUBGmusXy79rT4FiFgFsI8rTWalkInJnbyskQSVPKJn6IxrYlpzECkPaOP6Ri7My501PnehOwCOoLmobGZqqwDt1n8BGnzcXaIGHEjLahSygX5TyDyfFDb2ObACXe3LUwyPr8104wpAne0uNBBCnguG-p26yoRKKs4DqKy6Pm2ejeWNWGog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68bc8b1da1.mp4?token=WsGzDV0gSZ4kcfwp-jxiKZUXA2nzyupQxbeSopWxeMrPzaNGA6Et8YNXrCesX0U0PEy9x0TC0jhFeZtGNAPNvsIpxKny1u0PUmbJvNBtwihcMY5GhfdSW8AgJiv-F18TomBkP0pLdIY0SmRww7e5i77-8E3VhwibsZtzUBGmusXy79rT4FiFgFsI8rTWalkInJnbyskQSVPKJn6IxrYlpzECkPaOP6Ri7My501PnehOwCOoLmobGZqqwDt1n8BGnzcXaIGHEjLahSygX5TyDyfFDb2ObACXe3LUwyPr8104wpAne0uNBBCnguG-p26yoRKKs4DqKy6Pm2ejeWNWGog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صهیونیست‌ها شبکۀ‌ آب‌رسانی در کرانۀ باختری را تخریب کردند
🔹
منابع محلی گزارش دادند که اشغالگران رژیم صهیونیستی شبکه‌های آب‌رسانی در مناطق «عاطوف» و «راس الاحمر» در شمال کرانه باختری را تخریب کردند.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/442239" target="_blank">📅 09:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442238">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6dDUU8XGAVpYVhDdFp85zHxWZ-hjWK8wnpd4dlzJCB1q-wktjvWZZD2dsMkK021cazmBup6NcSFEFNtd0gQBO9vmQnCJUi7_mKvYoKRo2qMmOn05v0EZfo1iy_q-B4Filfuz6jVid_L8sK-oPEBTQmPc2rQjv8QcL-oEazAPDoit7UsI9bVr96lKYOAX2hZUerj46L2nrM8VL5iv6zT3jlRq-GHYYjkDwWEy84FgZy_zjdTR-prhUiDAs0sMpvjqHWnG4ZVzo_43mwxuSMW2zSX_o6WkFA3T-zpfDSoMO8DAOt6CO-YCjFjokYQo3wxtE3BJRBo5Pct-THiwZVgvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قلعه‌نویی: از کشور بزرگ و قدرتمند ایران به آمریکا آمده‌ام
⚽️
نشست خبری سرمربی تیم ملی پیش از بازی با نیوزیلند:خیلی خوشحالم از کشور بزرگ و قدرتمند ایران اینجا حضور دارم و امیدوارم فوتبال وسیله‌ای شود که کشورها و فرهنگ‌ها به هم نزدیک شود و خوشحالم که از طرف…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/442238" target="_blank">📅 09:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442237">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/653e3beb68.mp4?token=GE_GTmX9ND8yb5nxsYdkHQeXat2nqL9n4wbrdwFCEYtGmaRw_V-8Bhc5E_oALBIUGeBcK9G-s0OaOTUsC5jLn1DkaQ98Xy3hmZYtVhrKktaW_nJweYIXSDZTkF4LjEh0O_2jN8GJy5370oH0dDYRfiFseFo5R9fkM1yfjdtgYDuc5ykaiytEH-wApfRHkaxO_FF-n9Pp8agcXv7taL1gdsPTLtUNg_wvZ5NuKntqhU1sal2TW3jeqn0K7oRFadpLaiUsi5vw2sxxwvD1dB5pWEEBenfhdAnJ0gqo_rPZttdE7T4bWrnrflaLCe-PBy1IMrmXeI7FDVKGWyi0UVm4VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/653e3beb68.mp4?token=GE_GTmX9ND8yb5nxsYdkHQeXat2nqL9n4wbrdwFCEYtGmaRw_V-8Bhc5E_oALBIUGeBcK9G-s0OaOTUsC5jLn1DkaQ98Xy3hmZYtVhrKktaW_nJweYIXSDZTkF4LjEh0O_2jN8GJy5370oH0dDYRfiFseFo5R9fkM1yfjdtgYDuc5ykaiytEH-wApfRHkaxO_FF-n9Pp8agcXv7taL1gdsPTLtUNg_wvZ5NuKntqhU1sal2TW3jeqn0K7oRFadpLaiUsi5vw2sxxwvD1dB5pWEEBenfhdAnJ0gqo_rPZttdE7T4bWrnrflaLCe-PBy1IMrmXeI7FDVKGWyi0UVm4VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اگر به لرستان سفر کردید، سری هم به روستای گردشگری ونایی بزنید.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/442237" target="_blank">📅 08:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442236">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPW2F-g1JDDq_p6j_3TNOmlY4ZCYloG6nky0m74PVOLU8wI-KnJFHi4dG6W5gD6mkiyzGzLL8eRs86Ctqx-oitJEY2MaCevhgvvGFuzJuGad9ORnXsFk4lXrVdOr7w5CudxctpqRrtA41UpX55d7ugjvvvTGHj9bVchRhxHCXbrGPDVfWdmNagbbhZ-NBGRsXBpirezKyzD0oqLSJeOTxIEsu-gSZ_aoc8DTURjhvEwTw47Q74DpxAZ9E3C_24Q09C9EvQhSzHrPjQW3IA_794yTjuhjklrUgRycaps9xKlv-j_BJ15KbhgV0Ngz7XNGooGX40KQuIVTC8auFPkiKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
بازدید بازیکنان تیم ملی فوتبال ایران از ورزشگاه سوفای لس‌آنجلس
⚽️
دیدار ایران و نیوزلند فردا ۴:۳۰ صبح برگزار می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/442236" target="_blank">📅 08:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442235">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/649bfa6d78.mp4?token=Lyg0SljSuHfUyCQ7ZEGZLX4lGq_3_6mWTrEg36G-qvJca9BWL_gyyYnIRpV9krYJmhzhgfsh3IUna0QTgwbRawNco_4Z7uGb6AIKvFOkop-u_BTcSvbp3RQcRtcaz6THSGhCXezvPTquqCkf02_GvDrdT_Pa2ypFjJSkIHUomCcg89TiAXKSESL5HJIez5Jmukfnrk_IPlvXkTrDNxeYFcRpwmKr_1jjML8Raj-ifNZsekczdZJTyxBdbjDm54HyxMwLvc-A8qyo2cYX3tBrxMjqbJiHNGJ4-LpNWK39-P2oy2cXwC2e7wCqrWlwceBdWQsaqHebHj-qe5PjH-f94Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/649bfa6d78.mp4?token=Lyg0SljSuHfUyCQ7ZEGZLX4lGq_3_6mWTrEg36G-qvJca9BWL_gyyYnIRpV9krYJmhzhgfsh3IUna0QTgwbRawNco_4Z7uGb6AIKvFOkop-u_BTcSvbp3RQcRtcaz6THSGhCXezvPTquqCkf02_GvDrdT_Pa2ypFjJSkIHUomCcg89TiAXKSESL5HJIez5Jmukfnrk_IPlvXkTrDNxeYFcRpwmKr_1jjML8Raj-ifNZsekczdZJTyxBdbjDm54HyxMwLvc-A8qyo2cYX3tBrxMjqbJiHNGJ4-LpNWK39-P2oy2cXwC2e7wCqrWlwceBdWQsaqHebHj-qe5PjH-f94Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدور پروانۀ ساخت برای ۱۴۲ هزار واحد مسکن ملی
🔹
مدیرعامل شرکت شهرهای جدید ایران: روند تحویل واحدهای مسکن ملی سرعت بیشتری گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/442235" target="_blank">📅 08:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442228">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/khKcoewl5wFtzdaT5Z5jzPKScETziFse-3UO8ukZhs9OroKhoGV-oIEndkhrVk_nvA6LqXup8TqfyU4Ky0jVX8eYTgXq4dn8KtHBSZh0Tov_UKiVZM3ZBfM4lR0abOxgxCLSwWpJ-CZpu-QT6d-H7DySiVknhd2a4YLDAhgVoTCRcFoVsV9ipPJ8SGSY7hkdqNVk_OTj41FIznN7nynfiPXZjgTZR-s0AvtsFtpoWUPs94DnFGxcZioppTgCqUdmR6EiO60zXtvOonsRu6RNqfswS6dwGTY6ThE8CAzH-5xQcawIJo3OkypVfJ2zF4Y-mOmhpAAGYN91k7R-C8_Qjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QApovq6GEvqMXtP-bo-SZjzp-P5MJH5QrUBO-unC42CU-KMcmYbJEouBDRrJkaMQkDXRsDFo09KuWvtWOriQ8JbLfSIF74d3jd6WQ247UttNxdZca11QUBVxw_duRpkQZzOf_eHFN3PmZb0hosVBAAZXfP69kPdST4FMdTpHpmorfXSLtMIO4NBgV_Tf0Iy_luI7nH_62mBK-ygn7y9TEQ58inz92oJmWuZ_hjLpEytLhXYRJSmD4Bsdv3B4bXKc-UoFo_-9Ch6SbqPccDvuf2yS32-pZn_VizmeGo0rM1umiJlNPbWaBanjOs-kSp0tNN7QBmnMxB1F8edJ3QZ-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ta5Di7olFxEoW8KctCgW9H9Zbf9U1ercY7YI45srSqAzxGm9RLHq8F1zH6jgpvtL00QNY_L1VpBq16tdZBmhdmiTKLh8kbx5qBaoNm6cu-ajqxHbU-Ye_3RoAg9PRpyAcOuszswcRrbdWsHZPXbJNDW2kT-gfZ6V24y1AnXzTDKbU4EywfF1Oler_gVBcACZdNRtC6L59uMfSd9OUCRgzISqO1JRflA66t6e5lLAFNepUeKXqCp-X_GvA8e-UjqdOZ7QZuoUvdMWFkCi76Bw7wcWuHDcwSoAGzslak66M_0rpdfbxM2H_o6zEEuKgTqguF9DEdYsal1QAJb8m5K8Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nx219rLBClpL2LIdqsMpTWt1poiww73jO5NIT8p9HXGQOtnUxiyR2ve7v9OLS6UpxQkFwlG4db4OpKzzwTJ2lr6uGdcYH-69B1iRK0fG4YwYcNfH9h4LOa9d-JQQ5dJuWJjxq0sWWyGIGpJTpakSfpvSKMpj_0w05v7pioW33enp3hsC1RN0LM3KbAO14BpueKZHIcWiSYZjBsVdo0nZTY4YwIeSuLEhkR-Yqojw2UJUh0uDCZIZgyaMqV20-E9IOjNskAWy64x0hLJa2CGkF_m63FaNSUooemzxo9HttdMD-5EJ9jKr28nJXc-aMASxUZecJKrIWLVMtmUi1HQG2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_-Xlhc6TqHe6PSWlY2gmNLNBBBn11htBbOhZYS2LdWcKPJZdWDK5vmYcAbmoUAuPE_IuAJMUCZGrqw8aKjF9Yb47uF6o8rzEfi4-mZa-I_WYMXIKU9S-BTf4Ndja0obxded8JibvyvH3r2B_lO0jZq1TSA7q3n771loXOuynrSXGUj7USxtYkCaNFvdraD5_jDWlTdsyOCCg3Lh_6FvQYC8628CjHQ4FKi9OqNS5qPCuT2iI5qZYcnj-amhBgFdtTfbbwBt-QZDknKgrwyP8-97ZEKDxp46n6ssvzuUUx626burAs1fg_T005LeKUf0UvXI1-iqQXEnuiF6yl-a2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mSsoXNHc6NUp3aTZhVeltSM7H0_sQ-yMocpl6qJciAcxGgRpB4dlzfABM3nnnT51h9NgWAc8uTOcAmuSvJy48_QBN3svYT1XUXzbrEeF5TqpLAdMOgEJsDyCFb4MLkGcYB1kDsMQI-2J79hySEMeK0r1ZgCe569T90Zoiohrp0xCRWCFRESKx65ZWPaWomWyrQsvaYZrKYQLAUdvFWGL_vKMO55K6oGo46zF6SQO8v7jA6WC4Ld5ffuoyKRu625TJNWXOaE6H-pvT4RlPHvYIQYis0f9RmpkakSHRa0u0O81g2X9nT6GNtte0MjhhSDFAA9F-Xl7NvYfu7DSZmjYEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDsJd-k-7522aOHdQK5NHkGBP0plf3ckord6_QoP2W0a0ilwfItaALL2cqZVTqE3ElWrMcQUajtlcin2HjhDmQbbXx9gsSf4W_MbqvOBq9bHX0VnvW2DxQXmpr8NV6fr9r9lqO7m7vOLGMHRsK6hiFd6HxdG4nsSbT91QCe0ronWuQB-Qfqk6imGoC75vjwQ-NRiOQ1aaBU-idovMts3zFPsJgicMJ1sWy0S5OjWfXiEcWCPR1cxuDHl6WaQgXbmDR6fdtXakBIciwT_Ic4H3F3y68TrzUD-SwKffbt5ctoIJugho1roBswQnSLQzAwVq_T267LNPW_rMS3v5mu1KA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید بازیکنان تیم ملی فوتبال ایران از ورزشگاه سوفای لس‌آنجلس
⚽️
دیدار ایران و نیوزلند فردا ۴:۳۰ صبح برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farsna/442228" target="_blank">📅 08:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442227">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Muz1oAGtMqaNB6QwDca7SOejLph1WwLelWsSCmkSd7sIiNoxSDrfY3MiCx4oaOghYstCa1s56D38db-zbtUPcxmuc_ra_MIkgdWYbGFxwSx7I7OXaKQB1wcqgiXp7X19-fRnWLEMnmyEJ9n6cuzrtYgv-0k7Q96gtr1FlAcDHp1KjYNsP34jxFCujechDRndsmw2uWYPIIjJT5Imqo6agfLVy8V8NpndFhMlZoIDG63cCW-KqiZWXKOiFDA4vwhpHjT_JMIXaUygidIAnCPrLiDzweyk_evOroJXgARWa9JNcSSWBbhZuHa9IX4qsq4JxE_8CGwb_O8ubr4eF2iKEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی پرگل سوئد برابر تونس
⚽️
سوئد ۵ - ۱ تونس
@Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/442227" target="_blank">📅 07:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442226">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8obnbcc4YNelFK2NcONaSiTrpCtSLKBXZu6NIEYjfwURDJPjmm9qG0YLKDgxtFYuo4J9fkD4TskAXpla5upv9m-KhNCD2iR19ARFvdEEUSD5zqyVuv0Z9amf7SQqP4wSXhXpoN9HEeBtHLGiSwUGdVTbDSpWGYFg8OMuvtqDkmrOZfCDgoUeYv2H6zNwFwT6A5Zo8ZgFmjdhvjz9L5rar8_eGcxPCGx0CCH4oMPjVTFwcRBrjAR2xikqR1M49s8SluLdeo31u_8Tj3mAiZFQPkg7E8oQnPMhhyOzG4bwCH-FpPARQtuf6gVkAV8X-F_dcYu_eV10u9w3OdhFM3yCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان واردات برنج‌های بی‌کیفیت
🔹
برنج‌ پاکستانی، تایلندی و اروگوئه در کیسه‌های عجیب‌وغریب، خریداران را گیج کرده است؛ برنج‌هایی که اصالت آن‌ها معلوم نیست و گفته می‌شود کیسه‌های آن‌ها با محتوای داخلشان تفاوت دارد.
🔹
حالا با بخشنامۀ جدید وزارت اقتصاد، ازین پس سلامت، اصالت و مرغوبیت برنج‌های وارداتی کنترل و نظارت می‌شوند.
🔹
براین اساس، سازمان ملی استاندارد مکلف به تعیین اصالت برنج‌های وارداتی شد، و گمرک نیز بر صحت آن نظارت می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/442226" target="_blank">📅 07:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442225">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCg4voeNAuSX0jXFlwFF2eiQxEyg1ulo6WoDs6kGjCm84xhQ3OlFbtGYyY00yvKQbECSXz-Aq87MDKT4IpKvwBU6chDaVwXFYS7ebWVVTlxEAuJspushT-MafVmbb_1mTd6CONYYiSu5WUZZHcMvaIrN4KuWUPNXurVGK4kTtDLykFLe2d2YtIJoNaVmxmrUW2X0Bru5EUrhPLGtJf4K4_x_6eYNxvG03B1Xkc-sWrtjcuybM5fXxUwX_hUFnJ8DDpYJPeeg9ZR-9teuBGURw19EehUqi4y7mWerm_WUs5mrG9S8oGHH6YU8fBz0r0g9KYSLjzBCxfLWXszRWYLy-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتبار کالابرگ سرپرستان خانوار دارای رقم پایانی کد ملی ۷، ۸ و ۹ شارژ شد.
🔹
بر اساس اعلام وزارت رفاه، اعتبار کالابرگ این دوره تا پایان تیرماه قابل استفاده است.
@Farsna</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farsna/442225" target="_blank">📅 06:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442213">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MjjwbpMuOzfrb-YWmFMrPYMLOAt_tXUfuidoEoOMD3DPj6YugFKRLVHDjtZNyxw9NhJ-2Q_sgDhQHXrV_OdTkQ6Wkhc2JteOaDm3XYvN5l0Z-r0zvek3rm7OhifSDP31GaqujDMcEfHYsfJSpNCJ5ioh-8EyPKkQfteCDuxhOGFh1EF5kt78Lv_K9Xc6XEjE5qAnA1rhrUPiYUZYY3xBAN9Ml5bj43hIDjC38CTFa3Ykl7htMJV_mJsujsrP7m8SMiZcNGMa41kEO7TiyoVpmY0nisOOp5iPKxy2YBSlkWLBLrEMkZRpt-WyqKM6kY02qHzMDvzJTxHtKf1KYUHvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/frLAaJooRjqBCDCxg4Gxd_kho670PHRUcajVH_OV-xWFmKLoKqBQNe3iX_dkbzEvOBCCb3zEh1mVpXK3s7tUs7KT27j5iAyTKxEV1W_OIDaaSCpKuKyNL50ncaLhHfs62lzKNpl4Sbzu3hunk9XfmtK-DQq01mS7sVx8d9Ufh_qCcksrwORDhwjx7iFPd7QWOFZX4CLO2qHD5sd3N5tj__68YTc46gwTljvfNjiRJ89JP3sB6pDhVK7Zic3l_ZrOJ3Aabi4Kb0mdfRE6kCjYJuhAHB-qYDgcKoMplOjr28Y78oJKT304cvv74dFU94Yt6p-PjXiDkkSgQKqPUyrHUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DccR9j6nGVV7tmP4PznlUGA4bmeuu3S3JIUkz1l-hnGbaXgoGt3iPEXltgo1EqsQg9BlKOFtAsW7u65U003XObFEzrlOsvNBoh6xBPENzkIXA1UmPt6TOL9EfLksGhZq9mGh05VGX_P7lFWzb-a6ElN73kERnd266KS52NTA-srAWFqJpS7B7qVm3F01r400X0lB2hovxB0tsrvSMhDaa0HGiEodO-Y0Xmcj6cIlVoVQwzrevI8bQ1jXM_3Tjg_PdcCp9lqZpS73qclSyb-ybN5GRt0-lAtmaBL2yFB5sBQ3u64UPIworRw2i94GkSWecqI86Wj8rZ3XQc8nRMAJMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mbS7icAlNH4bMT5kL2k2REQbVl1VzbfhVxCeJvZDD-UnZNHyqxKpooKXq6mG7TmjXRFLvfUb6lwZltLnoV5oHWuSQ4rk1CJIxg9uCoN5zWhka5uNFW28J9JMvRux6-jUuaMJD0zl_ejvN_cSwwR0ARD8jkIH1ggAodvWTFDFPit9yZNZuu2WtzGvg8k0wAQvh9xqi9tX93iOSOiMJJFbBFenLv2-WzhtK6uNHXiwMmjpTfbQMseHsDumYB2nDrJUBvZQ2fIFufTBwRvvb460i7JZoqMgk5PDEtzgAUwLf8a1Khs74rziIP7WNgpUE3-2S3g0WvwzloPbdqf52oV7qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGCmSwJa3ZFcvLO7r9WJSUl2-dV45-dYO6jpmJnMb_UQYy_FF7Ao4xUVQvxPiAUIxdDnnlPVvhCdHHmEQDa9YZuGPSglD_IXI4uql_l1AOAWDSbiwRogCePPI0pqbTNG0ZX0AFIRowkqX29eMe8Zfi9QeLp2hK3Q-jsNIdhc5w1sBxmJEz_NJV_Z0bv5z_O2SCcwZ_Z5_Nu5P303bK3XYV5PF2SaKkZ_VlvTY0fLI7II2y52HjmwQzkNlZCgu9_KiftTSWE08yvfiMQgnrvEyFLOiKodgSCGvQ9iCdAXg8I6Xz9tqSvmvFL99CHEpw8DrujR4cMjmCAFmv5iV-ckvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uTXlPV2QCGNM5U741O8N7Kos6aO6HJWk9pki-ZrGetcSFotxT3CmkOtfoZZ8T_8zApjO5LUnKAgyUtAM5ySy4IXHRWpJ7Y-i5kpo6CtCRhsdoWrrfCEU_p9e5nAF7f_G3GOQOHUXWjjWtq-O6RbDxroGjQ6D1CMP6K6yqrQY-pi8P7IJLvuD9mTb2azPwtXpF_SUvFyDStQLAji2GcSkvliO3tCID5MFBoxm0F3vEIgQox_fNaw7Ez4zJE8ILTyh3xNCKbOcTSwpA3LTlEghsP-OJ6hTgLbzkt3iFbKvQmyAkNEk86I3pvagxP2bek5jai4ILShoQA3CNvg1E3NVYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
طبیعت زیبای بهاری در مراتع جنوبی چالوس
عکاس:
غلامرضا شمس ناتری
@Farsna</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farsna/442213" target="_blank">📅 06:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442212">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLo2ppiJK0oYNiDbVw8bQHrZGad2zMfaI0vFvDPbx4XjRTuTLQn5yW_AuwoBF4_2npl4ZJAFeD4gAr-NiKRKHmfOr2fruZ9rFfq8bm6ZMm5aFRhDRxh7Cqck7TD6pHju-rzf8GhBHNddekgpOef9lp9cRSmz76ll54zd5TkssdKXLaSuFLSV7ch8i0IveNpP_A3zrdjAITqhCtX5e4vkpQtB4sSZcv27S-ruEIDsEHzYq_cqd1AYc7UuwhSl4WvimfNEsfIfAYqWQuEyeVI9jwN-k4WdyXc_1-8qfMXkR-Nj5qCZCxNPfX1m21W-H0n4_RaUTzuRPwiTaK4HdlKwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹۳ درصد حجاج به خانه رسیدند
🔹
رئیس سازمان حج‌وزیارت: تا پایان ۲۳ خرداد، ۹۳ درصد حجاج ایرانی به کشور بازگشته‌اند و عملیات انتقال زائران در مراحل پایانی قرار دارد. @Farsna - Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/442212" target="_blank">📅 05:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442211">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-gu6dWS7yVkmFQ35KLHvqdaQx49sod286CDsVHgS8xeVITYIqRh5K34Ip41d_zOQM082Qjx07rIAdD8qOTzKPlVvzBGAgrc0EOMgObEYSIB9vHggs-TtRQazUF3aeEdMRYR6rM-tlu_NDHxX94jCCOsZfkOlKQhhsZQq7NhaqcKgxjXOW08LNK3_jkY3wYXBRsc-1ML6_Cax4H8M-Tl7UibEPyhVu6Es1cBZfTDSibqT7GZn3fKEEKOhQ0xSxnA6UQT8Gk4vP1EBqC-vndfN9TkVmTZ_srj8Ac2gKgZfPmYgp_A-AzKoM20kHUptZx5Bs_ZDwFYq2k4F2I9_WEoFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساحل عاج با نتیجۀ یک بر صفر، مقابل تیم اکوادور به پیروزی رسید
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/442211" target="_blank">📅 04:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442210">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5914235d7.mp4?token=hzU3EkI_pyK_x1pC8VoaQ3Axi6To0NEgGj2IeC4v_NASB4J952-UzdOtwgyyqMu0SizMwNW9AoxxUmKd-Uk4qSoxCaVSTV1FIgvnPfCcYYQilulWdIPcUwnF1HRD-kQJ7cXP36DQ6eRZeSLF8lC2doP-Xdu7YBz8A0LwdcKZYfpP5TQ0Q0BRSMjnoUyt56FX6Yg3f3MGDjIcoFVsMqNPMzUrPXA-suQt6bHsQ-ykZfu40zR1kOh6trvMQpF2GKwcKqpBP99xHQxQ20cM9_WCT-Pt3scR382ydL0i72sNOBmOU6oUk42aluBfac3lq5v7Iv4uTzhNmQWQcwowAwzJgIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5914235d7.mp4?token=hzU3EkI_pyK_x1pC8VoaQ3Axi6To0NEgGj2IeC4v_NASB4J952-UzdOtwgyyqMu0SizMwNW9AoxxUmKd-Uk4qSoxCaVSTV1FIgvnPfCcYYQilulWdIPcUwnF1HRD-kQJ7cXP36DQ6eRZeSLF8lC2doP-Xdu7YBz8A0LwdcKZYfpP5TQ0Q0BRSMjnoUyt56FX6Yg3f3MGDjIcoFVsMqNPMzUrPXA-suQt6bHsQ-ykZfu40zR1kOh6trvMQpF2GKwcKqpBP99xHQxQ20cM9_WCT-Pt3scR382ydL0i72sNOBmOU6oUk42aluBfac3lq5v7Iv4uTzhNmQWQcwowAwzJgIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برای سفر آخرت محتاج مَرکَب هستی
🔹
امیرالمومنین(ع): آه از کمی توشه و درازی راه و دوری سفر.
🔹
آیت‌الله جوادی: سفر طولانی فقط به توشه نیاز ندارد بلکه باید مرکب هم داشته باشی.
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/442210" target="_blank">📅 04:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442209">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1Djjo7BzYDkx3CxlbbkpnmlHdmsozsZxQdmzL58QLLiCsz8y_9u7N8nQRL52E1hXUvazVrncLkLioa1mwTW_JzwZTXW9YP4b0_SaahFtPJxC_ST4CKgpJkzaGII3bpJh5eq_6E9g2gB--hcRa1pXmBAtM824I84Pd_trb0Q73yqYTRNsTyQRvS2i7YdD5UHIWF4-z1ap1xVMH26sl2hKRCBF2PK98toVQZPxh4E7CNhTsF6RYyrEa8pPxpSiIN8ipwq6bXfAN0OrFFFE6jQM4y6-gKvG5goQilW5YXBXtQ9PEGEY1D0Yi5lkRscWgIbcJSLn-QgBDnYe49Z3m3UMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طارمی: با فوتبال، کشور متمدن ایران را متحدتر می‌کنیم
💬
مهدی طارمی در نشست خبری:  ما برای همۀ مردم ایران چه کسانی که داخل هستند و چه کسانی خارج حضور دارند بازی می‌کنیم و فوتبال می‌تواند همه را متحد کند. دنبال شاد کردن همۀ مردم ایران هستیم. با فوتبال کشور متمدن ایران را متحدتر می‌کنیم.
@Sportfars</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/442209" target="_blank">📅 04:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442208">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6V3fYlK4RqxoyhcyUvn1eZxDwfgpRzg0h7IE9jU5EE21rGL3bAcO5jCJ1ymZ-PcwdF7a81gnFNdCoJ5SuK8gssPvk2gzYJO3XHxWufAYWVoj96lqjTfK-EqKqb7rFBb6sv80V3p7rNO3VwUAk-LcyryFLUGjuo8_JtYIS_vWBUMP8DB22w-4xc0z2Twgg7P2fyC9-w0HF5_qGbn0RJ-QI0Su643b57sezEDwsHi4YKCUcY4chOKWPbkeDSswb3JGfL8urrIhSRIzqlWyR1cRs4Tx1QXmVkjOi3goAicLOICoJ5ckAzQNkzzVa-0pos62D1hqCaBHtlphj7J7Of48Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس، معاون ترامپ بعد از اعلام تفاهم با ایران: مردم آمریکا از افزایش قیمت بنزین رنج می‌بردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farsna/442208" target="_blank">📅 03:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442207">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🎥
سنگ‌تمام مکزیکی‌ها در بدرقۀ تیم ملی کشورمان به لس‌آنجلس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farsna/442207" target="_blank">📅 03:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442206">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ou5Bm0EUq2wQdhSSj9SLMWoulhvhU4dqfScQirS2qVRQYQIYk5vjhDhGORiXx_94PShZQeGtmqpgXR-bYuwXp5USCxTPJEFm-GY_eIlUSzbHSfK9SyFnc0WatkOuw-N_bbvnRuFsHGO_FtwEnR-PknfMQQgVi3bm8cJWAz_6TiLLT5myliZZ6FFiH4krYO3LXkJJG8iKMD3PcpNtKDQovGnkyixxwcekhbCSSMWF5Nd9Dr93s4fr_BPArBktX86M8Y2539ShKapaQA2kPnzW5BGBVddBNC214uuTFAhO7F3EAl-SEAidS2PUFtFGjE4MMyyDOfwqWkMqdcZEM8vyfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در مصاحبه با نیویورک تایمز: اسرائیل باید قدردان آمریکا باشد
🔹
هر توافق احتمالی، ایران را به غنی‌سازی در سطوح پایین محدود خواهد کرد.
🔹
در صورتی که مذاکرات به توافق نهایی منجر نشود، واشنگتن حملات نظامی علیه ایران را از سر خواهد گرفت.
🔹
نتانیاهو فرد بسیار دشواری است و باید بابت اقداماتی که انجام دادیم از ما قدردان باشد؛ زیرا اگر ایران به سلاح هسته‌ای دست پیدا می‌کرد، اسرائیل حتی دو ساعت هم دوام نمی‌آورد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farsna/442206" target="_blank">📅 03:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442205">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLpqhZp8TQFP3cd-TNOj3aeO3qiPeKqCzrjVOfbI6s0nnXFtG167lch9s1lbC92MtynheWaNohM_7MRv94krFit_P_0cNM6QSh6BnEqoVZPghKEfuulkGuMwQ6GIY2EOlSY61ImIQDwD_aASfcAys3d9AmYe365nRxoGaqVmeoeoJ0CHOro91M6kdSeI4tqJokJ-7ccxR1O_OlJf-uOGkQsQ6pdbAiHDRdO1X_nJbi3Z99TBX9Onpf4Tz6ZfRXoGVkzH-vjP9kXSMco2QLRUHQvIs_G_UqLy_G_cke2pCAQkyrcM9JQDcEJ_-RIct7C97o9BeFsnknleA9oRu2_HGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با فشار ایران حرفش را پس گرفت؛ بازگشایی محاصرۀ دریایی آغاز شد؛ اما بازگشایی تنگه بعد از جمعه انجام می‌شود
🔹
دونالد ترامپ، رئیس دولت تروریستی آمریکا ابتدا در پیام خود در شبکه‌های اجتماعی نوشته بود که از این لحظه هم محاصرۀ دریایی ایران پایان می‌یابد و هم تنگۀ هرمز بازگشایی خواهد شد.
🔹
با این حال او دقایقی بعد با تاکید و فشار ایران، سخن قبلی خود را اصلاح و تاکید کرد که بازگشایی تنگۀ هرمز بعد از روز جمعه (روز امضا) انجام خواهد شد. او در پیام خود چیزی درباره تعلیق بازگشایی محاصرۀ دریایی نکرده است.
@Farsna</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farsna/442205" target="_blank">📅 03:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442204">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNkYkz7bNfXfrVoi1a5uQetFKbeWBN6tqspriufjiFKZoqP_pAdEHiy5tam6b34pmdFBSZV3jZLfwe2HB7ghwYrlkvrfNyjRVcQY3h6zi8ndz6_7CKQ_ZbcxLbVUvAz5r5965U4sJ2d3FPGqXXJL9bGa75PbagwyRSyqMHRrta6qEgSY3Q5MJgZFwu3DpQkw_qaWCQ8uunqtuPQUCdQj4MAzN7WH2NCGBpk8jlxM_Qmj60y2bFtJ5S1Bj1F0bqryYJ2D5RFSN2zXYj3Jk5MmG3O7ZqUUdtoTh8thC2NQuWNMfJ_6DV_ecfdBjywAwvX4oLyroQNAIICeeWQpKwo9hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس: تفاهم احتمالاً منطقه را به وضعیت پیش از جنگ بازمی‌گرداند؛ اما با این تفاوت که ایران اکنون با توانایی خود در تأثیرگذاری بر کشتیرانی تنگهٔ هرمز، به اهرم فشار جدیدی دست یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farsna/442204" target="_blank">📅 02:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442202">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
ماجرای تغییرات لحظه‌آخری یادداشت تفاهم ایران و آمریکا چه بود؟
🔹
یک منبع نزدیک به تیم مذاکره‌کننده در گفت‌وگو با خبرنگار فارس جزئیاتی از کم‌وکیف اقدامات ۲۴ ساعت اخیر دربارۀ توافق با آمریکا را تشریح کرد.
🔹
به‌گفتۀ این منبع، پس از آن‌که روز شنبه کلیات یادداشت تفاهم در شورای عالی امنیت ملی تصویب شد، از صبح یکشنبه با ورود تیم قطری، برخی مسائل باقی‌مانده مورد بحث قرار گرفت. به نظر می‌رسید که این مسائل لاینحل بمانند تا اینکه حوالی ظهر امروز، اسرائیل به منطقۀ «ضاحیه» حمله کرد و عملاً از خطوط قرمزی که ایران تعیین کرده بود عبور نمود.
🔹
در این لحظه، ایران آماده می‌شد که از چند جبهه، حملات گسترده‌ای را به سمت رژیم صهیونیستی آغاز کند و مذاکره به سمت تعطیلی پیش می رفت. اما با ورود مجدد ترامپ و امتیازهایی که در ازای عدم حملۀ ایران به اسرائیل ارائه شد، تیم مذاکره‌کننده قانع شد که این توافق در راستای منافع کشور و منافع مردم لبنان است.
🔹
مهم‌ترین تغییرات لحظه آخر عبارت بودند از:
🔸
برداشته شدن فوری محاصرۀ دریایی (به جای بازه ۳۰ روزه که قبلاً توافق شده بود)
🔸
پایان جنگ و عملیات نظامی در همۀ جبهه‌ها و همۀ مناطق لبنان و ضرورت احترام به تمامیت ارضی این کشور
🔹
نهایتاً این رایزنی‌ها تا ساعات پایانی شب یکشنبه ادامه داشت. در حالی که همه چیز برای حمله به اسرائیل آماده بود، با تمکین آمریکا در برابر خواسته‌های ایران، عملاً موانع امضای یادداشت تفاهم برداشته شد و قرار شد روز جمعه این یادداشت تفاهم امضا شود.
@Farsna</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farsna/442202" target="_blank">📅 02:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442201">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBeX7Ln8n1e7uOaFuslsLOcT5YDEtEir0nvcntU2ggdPydEVcqnkwe1p58jA1tZtHbW5ivM5fKYUEIpnvK1Qm0tkf9Mut3j51Avlk76WpkyQ_CzF2HlxIxaV0NvEZR-lOlkA48xH9aR-OUEhgypOj717t0T_75NJpDiQyrmyWmzdhTJ3JcTrk5JwEF4fuiwQFb6ieSgB6GnOlD4CCmV0PfgSIpHYVJ8bfHGKEZ5uAFbQuVv9az-NmlAfQLI0l0sJSscq-R4d7TwbFGPsEiepNL2q-8Ork7VGNFnkAgwssCRFSpTUEYEAIr8OFD3tmI7r3VlRlVKIlWmEG2c6Dz6Bkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بیانیۀ دبیرخانۀ شورای‌عالی امنیت ملی دربارۀ توافق پایان جنگ میان ایران و آمریکا
بسم‌الله الرحمن الرحیم
به اطلاع ملت شریف ایران می رساند:
🔹
جمهوری اسلامی ایران در پرتو راهبری رهبر شهید خویش، تفوق خود در برابر دشمن امریکایی صهیونی را تکمیل کرده و ذیل تدابیر رهبری عالی قدر نظام (حفظه الله تعالی)، حمایت های آحاد مردم و تلاش مجاهدانۀ رزمندگان اسلام، به‌دنبال یک‌دوره مذاکرات دشوار و فشردۀ چندماهه، و براساس مصوبۀ شورایعالی امنیت ملی، متن یادداشت تفاهم در خصوص مذاکرات پایان جنگ (مذاکرات اسلام آباد) را میان ایران و امریکا در شامگاه ۲۴ خرداد ماه، نهایی کرد.
🔹
بر اساس توافقات انجام شده، جنگ و عملیات نظامی در تمامی جبهه ها از جمله لبنان از امشب به‌صورت فوری و دائمی پایان یافته و به علاوه، محاصرۀ دریایی علیه ایران بلافاصله و به‌طور کامل خاتمه می‌یابد.
🔹
امضای این یادداشت تفاهم در روز جمعه ۲۹ خرداد به‌طور رسمی انجام خواهد شد.
🔹
مذاکرات برای توافق نهایی، به پس از اجرای تعهدات طرف مقابل وفق یادداشت تفاهم موکول خواهد شد. جمهوری اسلامی ایران از تلاش های جمهوری اسلامی پاکستان و دولت قطر قدردانی می کند.
والسلام علیکم و رحمت الله و برکاته
دبیرخانه شورای عالی امنیت ملی
@Farsna</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farsna/442201" target="_blank">📅 02:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442200">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ریزش قیمت جهانی نفت
🔹
قیمت نفت با کاهش ۳ دلاری به ۸۴ دلار در هر بشکه رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farsna/442200" target="_blank">📅 02:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442198">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVxFBLytce4XaMh_DSeHO55Kzxhog23juQp1cAfF5dR0C5hxvC_m6ZfkW7vlc1MnIpd8MWGyb2Ufc9jCAzCCrgWWzXm-8cMfR6Rhp-b_c_qww9qTfoPSthVPLq75xfo6UrMYbRRKSdqrHATCd5e-NXhfjCo94LtZrNDxuJnU3G72x9hyynCT7G3pPhQHG3Uv8913zU08hHeB0KWsbJIJvOa73cOsI00s-eRjY3cKVSJdhqgm7rbHspGqmZDKfQjDDeYHy94gIqfvLJ_0olGmJr-TBh04dlAI-v78pD2qdnubayOl5FRUyzGnSr3D8E4jdEu8IJNg1vijKKjhtvX9kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مرندی: حماقت نتانیاهو بن‌بست مذاکرات را شکست
🔹
برخلاف برخی گمانه‌زنی‌ها، تا پیش از حملۀ جنایتکارانه او هیچ متن نهایی‌ای وجود نداشت. این حمله بود که ترامپ را وادار کرد خواسته‌های ایران، به‌ویژه در مورد لبنان را بپذیرد.
🔹
حماقت نتانیاهو نتیجۀ معکوس داد. این یک عقب‌نشینی تاریخی از سوی «امپراتوری شر» است. هرگونه نقض توافق با پاسخی سخت و قاطع از سوی ایران و محور مقاومت مواجه خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farsna/442198" target="_blank">📅 02:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442197">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">قرارگاه خاتم: مردم و نیروهای مسلح ایران ثابت کردند که دشمن راهی جز پذیرش شکست و تسلیم ندارد
🔹
بیانیۀ قرارگاه مرکزی حضرت‌خاتم‌الانبیا(ص): مردم مقاوم و سربلند ایران و فرزندان دلاور و شجاع ملت در نیروهای مسلح مقتدر کشور و جبهه مقاومت با عنایت پروردگار متعال و تحت تابعیت فرمانده معظم کل قوا مدظله العالی با تحمیل اراده الهی و پولادین خود به دشمنان زبون آمریکایی و صهیونیستی با قدرت ثابت کردند که راهی جز پذیرش شکست و تسلیم در برابر مردم مبعوث شده و جنود پروردگار متعال ندارند.
@Farsna</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farsna/442197" target="_blank">📅 01:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442196">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c3048e7ee.mp4?token=ikt2LKm8g-j1D5quwWgqvD7VMcq9aC6CPHtoR1dvL9JbHZ0TYuqtxo1lF44YZC1-CA7B42VmHh9qnAMXWQTIb45w35fzejl53pSU35NiynUQIy9W9Q4CtvTj713AM2fOw7GJcYpdTppnAA-mvlmlDLNckxDMRkcfsUHjkoTr0IMhASS26NdYsdsNMppFhYum0qlb2Ir6spYqBK-k3h15eq6HwNdnnJleiGbU4eg4UtFiBqQTrbvqgTziUPkJlZdoP809_EEe-7C5MAMvQTFuQTHFrbzsRmASzoYmgP9O7036dJtUaFEGof-iwqIObk68A-L2Rzb62LPZV7q7RbvOsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c3048e7ee.mp4?token=ikt2LKm8g-j1D5quwWgqvD7VMcq9aC6CPHtoR1dvL9JbHZ0TYuqtxo1lF44YZC1-CA7B42VmHh9qnAMXWQTIb45w35fzejl53pSU35NiynUQIy9W9Q4CtvTj713AM2fOw7GJcYpdTppnAA-mvlmlDLNckxDMRkcfsUHjkoTr0IMhASS26NdYsdsNMppFhYum0qlb2Ir6spYqBK-k3h15eq6HwNdnnJleiGbU4eg4UtFiBqQTrbvqgTziUPkJlZdoP809_EEe-7C5MAMvQTFuQTHFrbzsRmASzoYmgP9O7036dJtUaFEGof-iwqIObk68A-L2Rzb62LPZV7q7RbvOsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
غریب‌آبادی، معاون وزیر خارجه: ورود به مذاکرات ۶۰ روزه منوط به اجرای تعهدات از سوی آمریکاست. @Farsna</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farsna/442196" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442195">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‌
🔴
غریب‌آبادی، معاون وزیر خارجه: روز جمعه امضای رسمی تفاهم را خواهیم داشت و روسای هیئت‌های ۲ طرف درباره تعیین ترتیبات آتی مذاکرات گفت‌وگو خواهند کرد. @Farsna</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farsna/442195" target="_blank">📅 01:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442194">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‌
🔴
غریب‌آبادی، معاون وزیر خارجه: تا زمانی که آخرین نکات مدنظرمان را وارد متن نکردیم با تفاهم موافقت نکردیم.
🔹
گفت‌وگوها تا یک ساعت پیش ادامه داشت. @Farsna</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farsna/442194" target="_blank">📅 01:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442193">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‌
🔴
غریب‌آبادی، معاون وزیر خارجه: به‌زودی متن تفاهم را منتشر می‌کنیم و مردم خواهند دید چه میزان دستاورد داشتیم و چه میزان تعهد دادیم
🔹
تعهدات ما در قبال دستاوردهایمان قابل قیاس نیست. @Farsna</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farsna/442193" target="_blank">📅 01:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442192">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‌
🔴
غریب‌آبادی، معاون وزیر خارجه: اقتدار نظامی امروز به پیشبرد موضوعات ما و نهایی‌شدن تفاهم کمک کرد
🔸
نیروهای مسلح ما آماده پاسخ به صهیونیست‌ها بودند. @Farsna</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farsna/442192" target="_blank">📅 01:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442191">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‌
🎥
غریب‌آبادی، معاون وزیر خارجه: هرجا نقصان اجرای تعهدات طرف متقابل را داشته باشیم، متناسب با موضوع، اقدام خاص خود را انجام خواهیم داد. @Farsna</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farsna/442191" target="_blank">📅 01:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442190">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48e31d731a.mp4?token=Rjle7hZLsFz1lEvesAiME_qOQGbEI300J788vfyh4iHEnpKWr47d2Jo8KzERFpLUaAks3_tY5BDn16LcLDV5OfLLUKyDQwwM-nWCRDcJFLb2WGgdGSOD76f5HteqyZxRF4Dmj045_i_OwvEpFYWS5_sc80Y53shD36VEqzCB2g497AX2YKZp3xuN1SLOEN51n32F8uFq_W7ez7Lqkf3YkmUJaiWg9pFWvdU0SntPDVbGcs1brhs9_EbBUI7CTQChuBINaIitNwNiAy0POZRy_5vKqAFh3uPLzt2dSqHV3ntla8WwBewTjcf-qgLKKsDyJvuNKQyQ4QoM8pOQl-t1yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48e31d731a.mp4?token=Rjle7hZLsFz1lEvesAiME_qOQGbEI300J788vfyh4iHEnpKWr47d2Jo8KzERFpLUaAks3_tY5BDn16LcLDV5OfLLUKyDQwwM-nWCRDcJFLb2WGgdGSOD76f5HteqyZxRF4Dmj045_i_OwvEpFYWS5_sc80Y53shD36VEqzCB2g497AX2YKZp3xuN1SLOEN51n32F8uFq_W7ez7Lqkf3YkmUJaiWg9pFWvdU0SntPDVbGcs1brhs9_EbBUI7CTQChuBINaIitNwNiAy0POZRy_5vKqAFh3uPLzt2dSqHV3ntla8WwBewTjcf-qgLKKsDyJvuNKQyQ4QoM8pOQl-t1yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
غریب‌آبادی، معاون وزیر خارجه: در پیش‌نویس تفاهم، تمامی مواضع خودمان و موضوعات مهم گنجانده شده است
🔹
پس از امضای رسمی، متن تفاهم‌نامه منتشر خواهد شد. قبل از امضا نیز از طریق رسانه‌های عمومی، ابعاد مختلف یادداشت تفاهم را تشریح خواهیم کرد و دستاوردها را خواهیم…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farsna/442190" target="_blank">📅 01:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442189">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌
🎥
غریب‌آبادی، معاون وزیر خارجه: پایان فوری و دائمی جنگ و عملیات‌های نظامی در جبهه‌های مختلف و از جمله لبنان، از همین امشب اعلام می‌شود
🔹
اتفاق دیگر خاتمه محاصره دریایی است. @Farsna</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farsna/442189" target="_blank">📅 01:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442188">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ffc4fe9c3.mp4?token=GYk1C0bDRuAM0BPul_blE4_RG3GXTsDSCT8t5k-mDpooIsOn5uCCLI7IuXuugpveDKpPG6pMB16SyP-ce4u_A2ciYVxk_VmsJKlnQmFh8c1GwIbL3yEbnJt6FdUC6xvNgKJDyzqX17M24ag-rlj_WPFmYdjZhf8ib7w9VYj8OoFFaGMRRj4eeC337ydyRNWqQELNeftflRzh-5vfT3y36EWlrw7UqGUG29Z-1hrYnVIzZ_sy2PQq4cpsgbh4nQw-LBq61_35mhBlMZ-zZBwPfDc1Hxg5v9fwYx5hHXlt-iFdwRus15INo4YGpHWBF8RmfRr8F9AWB3geHweiEU2oyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ffc4fe9c3.mp4?token=GYk1C0bDRuAM0BPul_blE4_RG3GXTsDSCT8t5k-mDpooIsOn5uCCLI7IuXuugpveDKpPG6pMB16SyP-ce4u_A2ciYVxk_VmsJKlnQmFh8c1GwIbL3yEbnJt6FdUC6xvNgKJDyzqX17M24ag-rlj_WPFmYdjZhf8ib7w9VYj8OoFFaGMRRj4eeC337ydyRNWqQELNeftflRzh-5vfT3y36EWlrw7UqGUG29Z-1hrYnVIzZ_sy2PQq4cpsgbh4nQw-LBq61_35mhBlMZ-zZBwPfDc1Hxg5v9fwYx5hHXlt-iFdwRus15INo4YGpHWBF8RmfRr8F9AWB3geHweiEU2oyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🎥
غریب‌آبادی، معاون وزیر خارجه: متن یادداشت تفاهم نهایی شده و امضای رسمی یادداشت تفاهم اسلام آباد روز جمعه در سوئیس انجام خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farsna/442188" target="_blank">📅 01:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442187">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcc9f565e0.mp4?token=EdQD0CO7XO0ZoM7AxU0AtGNzIa3Y6LfadxCYg6X753r3zoLgDncxE-NghqaaEm-0VyBXS8bU2C12brmTl_DHNGG6WyJtqxNT7tLirza5B9UZO9ibqIhUzHhFCCiIYD_NcmLby-lzg3p4geDJ_2XwRvhun7A4fZq0BXBeRjNUrJtzNATxfz87fuZacDEFcnzydEpxlZlOH4zVkjfCcksnB3Dsy6taMhROn7Tu8iElDsGkli-fLnAnuJ33gEc_7MgPUkWEm1-RcMZ-gh0Bd8A_jX_mDK2dSQfFokEhkL3c7ew9wZjFWglsdgowZxqdqzjKJQ07FtcU9m5qcSylJ5O8dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcc9f565e0.mp4?token=EdQD0CO7XO0ZoM7AxU0AtGNzIa3Y6LfadxCYg6X753r3zoLgDncxE-NghqaaEm-0VyBXS8bU2C12brmTl_DHNGG6WyJtqxNT7tLirza5B9UZO9ibqIhUzHhFCCiIYD_NcmLby-lzg3p4geDJ_2XwRvhun7A4fZq0BXBeRjNUrJtzNATxfz87fuZacDEFcnzydEpxlZlOH4zVkjfCcksnB3Dsy6taMhROn7Tu8iElDsGkli-fLnAnuJ33gEc_7MgPUkWEm1-RcMZ-gh0Bd8A_jX_mDK2dSQfFokEhkL3c7ew9wZjFWglsdgowZxqdqzjKJQ07FtcU9m5qcSylJ5O8dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
به گزارش فارس، دقایقی دیگر بیانیه رسمی دبیرخانه شورای‌عالی امنیت ملی درباره توافق آتش بس منتشر خواهد شد.
🔹
براساس این گزارش، ایران پس از حمله به ضاحیه بیروت، مذاکرات خود را لغو و آماده حمله به رژیم صهیونیستی شده بود. اما در نهایت با امتیازهای لحظه آخری که…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farsna/442187" target="_blank">📅 01:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442186">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
به گزارش فارس، دقایقی دیگر بیانیه رسمی دبیرخانه شورای‌عالی امنیت ملی درباره توافق آتش بس منتشر خواهد شد.
🔹
براساس این گزارش، ایران پس از حمله به ضاحیه بیروت، مذاکرات خود را لغو و آماده حمله به رژیم صهیونیستی شده بود. اما در نهایت با امتیازهای لحظه آخری که از سوی رئیس‌جمهور آمریکا ارائه شد، از جمله حفظ تمامیت ارضی لبنان و عقب نشینی اسرائیل از مرز لبنان و رفع بلادرنگ محاصره،  متقاعد گردید که از انجام حمله خود صرفنظر کند.
🔹
همچنین مقرر شد نظام حقوقی تردد در آب‌های خلیج فارس با همکاری ایران و عمان  تنظیم شود.
@Farsna</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farsna/442186" target="_blank">📅 01:20 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
