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
<img src="https://cdn4.telesco.pe/file/b1MYv6YLwpoFWyMIZLBnPD24CLM0L6ugBUnV5nML0E86Oj-FgEFl9ymInWdlKKR_-Ycew9KbdKaPahTliDaGpJIe6LLmmefVconyty7BS-0pH7yPzcanNNue2J0Q3J0TV26bho4OdromKBv4oOyT37Wub6YqrwuQ2p3YngvXGKzr6MmZJAyTzKvpXL7oA8d2Yc858W67ZA5slhWZyAADBLbz0zQPapc9RQgdiFmsFTHgT_J99AVYN9XIGk2-SQdtXEzfcpoijZ25y2pE4OqQyH48kPg9hHorqA6YjJnpQHHg7zS2KlVK4tsxMYNVXYoNC28JVXyCUk7YirZzJF5wnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.57M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 18:04:58</div>
<hr>

<div class="tg-post" id="msg-659040">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUzjuepCtDumYCCEA3bTp4YXibEJQsCtJ5TksVRESoK0GsJiw6NUU6_B4UdfVgFhpEIOwSGHyO2E1bqz29my7onhwso2KGgeclvjsRX_DLWXlXbkiToeqlO-p0NvjRcxSSnUEQXZowdKwO8RZzEVk_RSlcBGM2pLzL1STpQK1OjnDPQDXS5-vvfZXteZ8ernVYRyOJ5bM5M6EyQq3LxuesILdy3THvyY9KJ-zrHKfWFveNyalWHUZAjEOSC-fUo4GDstKoB5OYNKBtddIcWC-Lt0NwSjpjdTgK7koITy7h5J0o1IgThvt62oiqixtkfLh1wxgC_s1A9jmOkXSzrA-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبق پیش‌بینی سایت اوپتا، ایران به‌ عنوان تیم دوم از گروه G صعود می‌کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/akhbarefori/659040" target="_blank">📅 18:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659039">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRVbBu9a_9w8lY-HlT-qRVF003gxvBxr-z-CjOoL9PxD0zILaHW2H0mdgaFtzBoKaPP2pQVX0FJq5-GGe5xOD8trsy5IA_QrQDG2C1gyAUO3T3tmjcFlaOS7q5kPt3xeFzhXAaIOCD2swfRaKtaj28jVn8raEIvIschmn7f7upVo2PwW3FI_Woj0_rQ5Ugc4Xl6G8g0EbEZtPRhRHH2aD5dxdMhhgPlCky_ZM9-78p3nsg9uH3aqc9ASKAzzTYWutb7cDZeYMz15_kQM27h_ejKeR_TkZiRgK7phtUySXCJfTpIDH385FchPKYFd8OTymu4WoB6BSKWXF9NrUQ9FgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستگاه‌هایی که بدون اجازه شما دزدی می‌کنند
🔹
سایل برقی در حالت آماده‌به‌کار، شارژرهای متصل به پریز و دستگاه‌هایی که ظاهراً خاموش هستند، ۵ تا ۱۰ درصد هزینه برق خانوار را به خود اختصاص می‌دهند.
🔹
طبق آمار وزارت انرژی آمریکا، این اتلاف سالانه ۶۴ میلیارد کیلووات‌ساعت برق و ۴۴ میلیون تن دی‌اکسیدکربن تولید می‌کند. استفاده از چندراهی‌های کلیددار و جدا کردن دوشاخه وسایل پس از استفاده، راهی ساده برای کاهش این هدررفت است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/akhbarefori/659039" target="_blank">📅 17:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659038">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXTSGuy6pxYcpMJu-NPzFO-jvN9H8p9Nc-AmKq7eDI2_sFqtzpzJH4v_hckZPT63cV4jhQAIdDsB_DRsnbA8e-nyTD9SM1QFhhsBo_Jf11CsUKslebCjkTMk91ZoVAwPK4XADeJ_qECO1Ap93QFQw65Zf_j-Au6pJeoDUjvNlzf6bLefMXT2hDIc5cOsKmoFK3pXfaqRM22KGyEpTN33fo8kXJT1MvpipKdRXEo--3P-npFULtkoEQdJJBri7-xe6SUg5kGpgPuxSeeRPVmcU7siSKAgXvAhd5_0opCS4W-L9HCfNDd0tveDIl5HbM8iIm0JJIBuc7z5exxutvV_2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
العربیه مدعی شد: عراقچی فردا به پاکستان می‌رود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/akhbarefori/659038" target="_blank">📅 17:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659037">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4I0kmlfRM8Wqrk4pjZt2CvCIVy8G6g8g2vjWT2QyOjMhdxIB3-DFuWwTTdaaYKEL3kpvJBjzElsuYYW-qN9OcrIUjFP9YwK6pSCzoQ_79J8ztv1vr8s-1TmTqElkGL3G1eCxrLxmv-jBleT03FN91WSCAbiMgUeHym6ck6tDTYse4tWL-uxIURqZcKz7uFjNQTin57uoiuTZyOLNzk65uUFLST4KhpZaohrVKE5ncPMT5GAlwgaq8IQegZxB9hK9NonSSLH5iQqVPwjWU2xY5GrTRw4z_d4CXowUgpT4jnfton-ukFkY65JXHmRNqZKpJ-kL8hKzC9qLgbltI6g3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ گیگابایت اینترنت رایگان، بدون قرعه‌کشی!
💥
⚽️
همراه اول به مناسبت بازی‌های جام جهانی، به تمام اونایی که مسابقات رو پیش‌بینی کنن، ۵ گیگ اینترنت کاملاً رایگان هدیه میده!
اصلاً هیچ قرعه‌کشی در کار نیست؛ یعنی پیش‌بینی کنی، قطعی نت رو گرفتی!
🙌
فقط کافیه همین الان:
1. وارد اپلیکیشن «همراه من» بشی.
2. بری توی بخش «زمین بازی».
3. فقط یه نتیجه‌رو پیش‌بینی کنی.
تازه فقط همین نیست، کلی جایزه هیجان‌انگیز میلیاردی دیگه هم در انتظارتونه!
🎁
🎮
⏱️
تا فرصت تموم نشده همین الان دست‌به‌کار شو!
📱
لینک همراه من:
https://www.mci.ir/-4S0XAJB</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/akhbarefori/659037" target="_blank">📅 17:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659036">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ترامپ توییت نخست‌وزیر پاکستان درمورد امضای دیجیتال یادداشت تفاهم ایران و آمریکا تا ۲۴ ساعت آینده را بازنشر کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/akhbarefori/659036" target="_blank">📅 17:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659035">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQFdovmGk64hMyidvBycJbJQRD1n0ZldIZawjC3lCgvl5I2BVBZhCiZJVgFrsVgn_kdSsQx9UXf1_s-btdch8g1IjlYKXciZ53aC5-HR6VqSQRJfg31Ayq-WB-rHtUNm9wS0smzcbea9tGGjixqSewOkEWxWL0F4qmJAjgcAT5j79TmwkPkFvn-gLmx6vOoLlgT7ACLJWnuKeG4PCHh0NAENH6d9EzTXxAXpejeMq0YTFdE8qx1QwR4RwW8n-Y31l7gWNCMYD15-joG_uJYvUH85_IIXzmPBYb8iaQKnd7kKHfb6vaPRzJ-E43yl9fSwGnlDLipJpdE-m3qI6gd7Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لباس‌های جالب شاگردان کی‌روش هنگام ورود به آمریکا
🔹
تیم غنا در گروه L با پاناما، انگلیس و کرواسی هم‌گروه هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/akhbarefori/659035" target="_blank">📅 17:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659034">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde5949fcf.mp4?token=kc6xS5ZfOPeZvdc0MJJ3bezS3pl6RSbx_iJD5VjWiHM1fUxCVrj_K7imMpMywCgArDLg7RY-YnVdncPh3SJeRyBUY7KZQVi2Q9stH7jAMFnB_6t_dsfUE9mDSvZB5V_y3uRvYjksmUMvf9LgYwe3EHfCfN2mTKYvkfc7owE7brU5TXHaRUpXjweMRz3O1v0olsajB77ZU6W03o3qPWHMDYFRLoQ9G47aEXgqcxTg9DPwVDW5ZIvzXykqGZAJDkCdtaGvvQeBGhVIPz8n21sKuBiRqOQMp2Hl0c1FMzn2Im2Y5D4r9kxDMH_a2Slpt0t9Fklw8BccUqaI90_X8LY6spziBuVa9F3jCGFsfoPZWWn_VSp60wP5AHjbbhgzi942qJjBG08txGjgJZ4YA9MgfdzwolV5_YFqv9kW-YbFI1HYXhUPXwnZle-fKo5kSIAxcV3Dyf49EhIvy_DgVTMahAkPhsDZ9znm8R7qDpU8L6QDGCXSHPeMYyxf1nT9uPkEW0SUPglmsfOfJ8aDorJ9WNk65QZbGIPciYvQWPZFrWIduxES80nPSjnkIbEec6py1mDcGHh7Lr7DvOJMfOgYXtjzj3Z5yKSesvssx3101i5cOMoXLZkzezEIMQApdNEN2yxGT65AYbJPDq-sArqpDOjJB97CVB3JTN8PZoj97nc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde5949fcf.mp4?token=kc6xS5ZfOPeZvdc0MJJ3bezS3pl6RSbx_iJD5VjWiHM1fUxCVrj_K7imMpMywCgArDLg7RY-YnVdncPh3SJeRyBUY7KZQVi2Q9stH7jAMFnB_6t_dsfUE9mDSvZB5V_y3uRvYjksmUMvf9LgYwe3EHfCfN2mTKYvkfc7owE7brU5TXHaRUpXjweMRz3O1v0olsajB77ZU6W03o3qPWHMDYFRLoQ9G47aEXgqcxTg9DPwVDW5ZIvzXykqGZAJDkCdtaGvvQeBGhVIPz8n21sKuBiRqOQMp2Hl0c1FMzn2Im2Y5D4r9kxDMH_a2Slpt0t9Fklw8BccUqaI90_X8LY6spziBuVa9F3jCGFsfoPZWWn_VSp60wP5AHjbbhgzi942qJjBG08txGjgJZ4YA9MgfdzwolV5_YFqv9kW-YbFI1HYXhUPXwnZle-fKo5kSIAxcV3Dyf49EhIvy_DgVTMahAkPhsDZ9znm8R7qDpU8L6QDGCXSHPeMYyxf1nT9uPkEW0SUPglmsfOfJ8aDorJ9WNk65QZbGIPciYvQWPZFrWIduxES80nPSjnkIbEec6py1mDcGHh7Lr7DvOJMfOgYXtjzj3Z5yKSesvssx3101i5cOMoXLZkzezEIMQApdNEN2yxGT65AYbJPDq-sArqpDOjJB97CVB3JTN8PZoj97nc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از ترامپ آمریکا دست چه کسی می‌افتد؟
🔹
دموکرات‌‌ها و جمهوری‌خواهان از همین حالا خود را برای انتخابات بعدی ریاست جمهوری آماده می‌کنند، انتخاباتی که دیگر خبر از ترامپ نیست.
🔹
اما در اردوگاه جمهور‌خواهان رقابت داغ شده، آن هم بین برخی از اعضای دولت ترامپ! حالا چه کسی می‌تواند جای ترامپ را در اتاق بیضی شکل کاخ سفید بگیرد؟
🔹
در این ویدئو تماشا کنید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/659034" target="_blank">📅 17:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659033">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DS7SiuLsjJIdXMF-aTkWmgkYw0F9WIYxtqUKzBcABmeHZsE9-u4hrtoqK8W8LEkokBzEc565CZh_4xIOW2qeavzr2Gd3LtMUviEIKiMl8pclCeKg2niiY_hoA6R832_WNLDyiDIQmny_jTUXARKsnHBIJEokH4FhxQcDM1zcmS6t__I-Isjy6IL9o3L7aH6jTkQOe7QJcYk9-P1aOwITcCa8zJI9ZKppqmNPyKFkjdSrrK1DtKcsU7YeEyX8RxUBzixnXZMX_7YNOx95Y6b_0lZJ5yzB0NZtSIeuEF8VXj0RdVGQmKmWMgF9HDEiI32L_EL1SycOuGqO-HgqzIemMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخست وزیر پاکستان: ما بیش از هر زمان دیگری به توافق صلح نزدیک شده‌ایم و احتمالاً ظرف ۲۴ ساعت آینده نهایی خواهد شد
🔹
پاکستان در حال آماده‌سازی برای امضای الکترونیکی توافق‌نامه صلح بلافاصله پس از آن است و پس از آن مذاکرات فنی در هفته آینده برگزار خواهد شد.…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/659033" target="_blank">📅 17:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659032">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db235a359.mp4?token=BAGFLeSzJ7HL-2BjQURy8PaWtx3RJpRxtt7JvGlz4BqQNv5f3qsFsP8d1Dbk0cY3J82FwUUhAOo06S3ddTsqo3NtUU91fAeJ_hrdzzNiqzQs2g0rcAylxfn40JQgG6smHCO2s8tPFoWlBSaV94cJXLN3jgsT0bvXuBeIOqqxFqEscLIoqXkyXvPyZzQJlMABYT5jNZskG9E2meYJjwE7aB5FB3SCMWJEsjDvgxmgYOfYmu5zaJw_LJpniBwgBF0mJao3QDAlfUEScf-yMk9e4cf-HI0HLsCaC41Wm5FWNBuvYN8xNusylMHITmuFUmlsJfhBVxg3qQKbxhyolor2dx6i52Q5l3NSrmChiNxy96PNQV22FtOgDNOuawzeO7vpGW4_-5voaGALcRGBTvE_O17g3iccLLlER-XpjdrklPPBPuGP3FcTMPji0aI4Fkw13ogyqcPqogPMzK9_xoc6xMhG1LMd0v60g-7bF_lnU7AHk5WkCvV4VrYJSJUTLhU0JBv_vTJ4PV89GN54Twy3uCAA9dqaRsHHw2aX-QImDrjr_HzAi8HWQJMepTlYn2HQkPejo33CJS7pzLetUB1k26HR4hqUebigRzRycYu-O71QeYRtVJzBFclf7EGIlsYbjvOHwdF5ogzs-wGwuNOD9adkxUBIS7HIaUnu2saKi0Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db235a359.mp4?token=BAGFLeSzJ7HL-2BjQURy8PaWtx3RJpRxtt7JvGlz4BqQNv5f3qsFsP8d1Dbk0cY3J82FwUUhAOo06S3ddTsqo3NtUU91fAeJ_hrdzzNiqzQs2g0rcAylxfn40JQgG6smHCO2s8tPFoWlBSaV94cJXLN3jgsT0bvXuBeIOqqxFqEscLIoqXkyXvPyZzQJlMABYT5jNZskG9E2meYJjwE7aB5FB3SCMWJEsjDvgxmgYOfYmu5zaJw_LJpniBwgBF0mJao3QDAlfUEScf-yMk9e4cf-HI0HLsCaC41Wm5FWNBuvYN8xNusylMHITmuFUmlsJfhBVxg3qQKbxhyolor2dx6i52Q5l3NSrmChiNxy96PNQV22FtOgDNOuawzeO7vpGW4_-5voaGALcRGBTvE_O17g3iccLLlER-XpjdrklPPBPuGP3FcTMPji0aI4Fkw13ogyqcPqogPMzK9_xoc6xMhG1LMd0v60g-7bF_lnU7AHk5WkCvV4VrYJSJUTLhU0JBv_vTJ4PV89GN54Twy3uCAA9dqaRsHHw2aX-QImDrjr_HzAi8HWQJMepTlYn2HQkPejo33CJS7pzLetUB1k26HR4hqUebigRzRycYu-O71QeYRtVJzBFclf7EGIlsYbjvOHwdF5ogzs-wGwuNOD9adkxUBIS7HIaUnu2saKi0Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیاده روی ۵۶۰۰ کیلومتری برای حضور در جام جهانی
🔹
این هوادار پرشور برای همراهی تیم ملی اسکاتلند رنج سفر پیاده حدود ۵۶۰۰ کیلومتری از لس آنجلس تا بوستون را به جان خرید و خود را به جمع هموطنان هوادار رساند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/659032" target="_blank">📅 17:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659031">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdf641019b.mp4?token=Y3iz9AcSyt07-XjLngQvDYXVVT2puRdyBjZJgYfdOEzX4pmC0h_Iail9cgMz46Nobf7BQ-3rUyhbIlRZ8xvnff08dU5aYTENr0JUv5ZzrHeZ97NRzDT_yAIuHbBGUJyb5BT6KGni1KvHgiy9UhhPCy1Pt78Aq8Vt_9EnuzQkalgdbmbFD3CccAXpTncMMmVLDx3AuYEjnGIGwf7J00IoAYBr2XpBlBOVJf5PT-0Urh38zxvU83Sh3jM-_vHlQFWd-B53wTcebm3tasEAHqIY3N7t2te7-eC7U7ZUK0g32Up529tJSfDl18yjTwfHJx9B4OsNyK9NOc1NL2pM3UxNpla4PNmr7Lyo7y06aFjP7suAidButmdS23OFr2T5f_6I84hSLPCHGr5yTi0URIIiKjDppeSN7FqyYGaLhdwanrIUZYYMxdf5n-2iQMmmcB_2cbMeHpB4Gl_nJ9WCb1ixqW8OgAmsnPS0p4szXGVIZObjbMgSq3awyf8nCXD66fiSiwtDQaGPNAQ8fBWMOqTGC4KH4wDpNf_5fu_ylKXl0cW_cGx0lp7So90RY1v60d8AKLIt6fwedgcAktdOjSvUfxPzxUFkAbxOg92PRu9Qq_lwCdukAoacFyJdOQc4pRw9GsqhSCNIlAIFfW5TcK7cHQiHT1Y7WUqp13AJ3xZFFao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdf641019b.mp4?token=Y3iz9AcSyt07-XjLngQvDYXVVT2puRdyBjZJgYfdOEzX4pmC0h_Iail9cgMz46Nobf7BQ-3rUyhbIlRZ8xvnff08dU5aYTENr0JUv5ZzrHeZ97NRzDT_yAIuHbBGUJyb5BT6KGni1KvHgiy9UhhPCy1Pt78Aq8Vt_9EnuzQkalgdbmbFD3CccAXpTncMMmVLDx3AuYEjnGIGwf7J00IoAYBr2XpBlBOVJf5PT-0Urh38zxvU83Sh3jM-_vHlQFWd-B53wTcebm3tasEAHqIY3N7t2te7-eC7U7ZUK0g32Up529tJSfDl18yjTwfHJx9B4OsNyK9NOc1NL2pM3UxNpla4PNmr7Lyo7y06aFjP7suAidButmdS23OFr2T5f_6I84hSLPCHGr5yTi0URIIiKjDppeSN7FqyYGaLhdwanrIUZYYMxdf5n-2iQMmmcB_2cbMeHpB4Gl_nJ9WCb1ixqW8OgAmsnPS0p4szXGVIZObjbMgSq3awyf8nCXD66fiSiwtDQaGPNAQ8fBWMOqTGC4KH4wDpNf_5fu_ylKXl0cW_cGx0lp7So90RY1v60d8AKLIt6fwedgcAktdOjSvUfxPzxUFkAbxOg92PRu9Qq_lwCdukAoacFyJdOQc4pRw9GsqhSCNIlAIFfW5TcK7cHQiHT1Y7WUqp13AJ3xZFFao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد صداوسیما از عراقچی و تیم مذاکره کننده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659031" target="_blank">📅 17:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659030">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_1Bd6BQFMWtcKbvR-8iq-9zSdP1RCRxObXnAJKsKpT1DwIvE-4ihCAdNoJauyEbQlweOM9Re-qE9_bYmAUJOLs8BGQ73kd-WIidgugc5d3HDEs47q2KPQ_iv1DfwIRTycX0UFGNspjfha-guNi0WNv-40zage3Z4SxQ-EaSyfZmSxbOy958SaJFWTavp3uHZZF2xCGMHNF4dgvdhAJT2ilO0buNk9VcBxqi1WdG8VsILAnX47shlBiIS_uGlPzIVDgXsannle71Tu2WpZ8qQ2NiO6O020NPhXoqu2cnHQ5sO93EQAWifZtGgKlFz5AKvPrsfbkDn9nM2uZ9B03P_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فاصله ۴۵ درصدی قیمت خودرو از کارخانه تا خیابان!
🔹
به گفته بسیاری از کارشناسان، مهم‌ترین عامل ایجاد این وضعیت، کمتر بودن عرضه نسبت به تقاضای واقعی بازار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659030" target="_blank">📅 17:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659029">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یحیی گل‌محمدی سرمربی دهوک
عراق شد.
🔹
درهای دانشگاه قضایی دوباره به روی زنان باز شد
🔹
محور قدیم کرج–چالوس برای عملیات تورسنگی از فردا موقت مسدود شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/659029" target="_blank">📅 17:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659028">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdo-8W1tmjD9DNbP05u9l7gsWeR0eOWoygZgpnShMIjwM_xT6FqpuMS8R4UiPYQ_m6U77-wgrsFUCzYBbQ0AEuWRH2CCoczqjxBJEIL-6Ixxrye3J15-wRRX8ehCgKJl7hHhM8pQarOWvPgUAb4LMqs1d5XyAEnNTV3kgJNkCi5AJwH2InTzPpmojbrwtPPgBpYBh0XbufJxaAIGf8QYNHxMFP_kMDfFeoJb7PR9Z4mHKLCs4sDyuQGL6f5488jOV1KZpHpMowgtzD-BBYd-a7_aydUohbQC0BpXJ58eIFiFV99z65xAC-rbtqqPSM9JlY2k4POvzauupOoekWng0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علیرضا فغانی به عنوان داور بازی فرانسه - سنگال انتخاب شد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/659028" target="_blank">📅 16:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659027">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
جزئیات پیشنهاد قطر برای آزادسازی دارایی‌های بلوکه‌شده ایران ۶ میلیارد دلار آزادسازی، ۶ میلیارد دلار خط اعتباری
🔹
۶ میلیارد دلار آزادشده طبق توافق ۱۴۰۲ فقط برای امور بشردوستانه قابل استفاده است و ایران محل مصرف خط اعتباری ۶ میلیارد دلاری را تعیین می‌کند.…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/659027" target="_blank">📅 16:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659026">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
سخنگوی مرکز توسعه تجارت الکترونیک وزارت صمت: درگاه برخی فروشگاه‌های آنلاین متخلف در حوزه دخانیات، گردشگری طلا و مکمل‌های دارویی و فروش VPN مسدود شد./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/659026" target="_blank">📅 16:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659025">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۱۱۶۶ خانوار جنگ‌زده هنوز در هتل‌های شهر تهران اقامت دارند
علی نصیری، رییس سازمان پیشگیری و مدیریت بحران شهر تهران در
#گفتگو
با خبرفوری:
🔹
مجموعا ۲هزار و ۹۸۸ خانوار و بیش از ۹ هزار و ۳۸۷ نفر در ۴۶ هتل سکونت اضطراری داده شدند که افراد گروه‌های «ب»، «ج» و «د» مشمول اسکان اضطراری هستند.
🔹
در حال حاضر ۱۱۶۶ خانوار و ۳۷۹۳ نفر همچنان در ۴۶ هتل حضور دارند. تاکنون ۱۴۶۷ خانوار ودیعه مسکن و اجاره دریافت کرده اند.
🔹
ودیعه مسکن با میانگین مبلغ ۲ میلیارد تومان و اجاره ماهانه میانگین ۴۰ میلیون تومان است که بیشتر از این عدد هم اختیارات به شهرداران داده شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/659025" target="_blank">📅 16:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659024">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای اکسیوس: موضوع دارایی‌های بلوکه‌شده ممکن است در قالب یک توافق محرمانه جانبی حل‌وفصل شده باشد
🔹
به گفته یک مقام آمریکایی و یک منبع از کشورهای میانجی، آمریکا، ایران و قطر در روزهای اخیر درباره سازوکاری گفت‌وگو کرده‌اند که بر اساس آن ایران بتواند برای…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/659024" target="_blank">📅 16:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659023">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9805bc1a1e.mp4?token=d6NyCtDZ5-04pF4NDJbVdthbiQaolDmSGn0EI3s8yxihih5VpmP5QqIrB6BDChXy9kkWZnqPhd6dpk95mjwBPB4y3z1GBzjUAYHsdNyDsjBWLfPU1LhzqOrB6xhPmCqJm6UnM5c3TZdTKU9fYwoB5sjFQmvt527m2i2Cn_dy_I4N81-68zUW3WxK8yosIq20S-SFI3B15YIKp1af9zDUJFtjUCeVl25GVL9KyhOH9OpZdberBwp_TR7oHLHwhoZUrzTyvmx0izE1QFHVYAGpkr7sf1mo_-HCuEMIh0RIr3WDma2ip7-upw1VJI_zvAjHwuwdulPUam3V0YgX9N5a2FL0uqz_R8xWpWSxDv9wLowG_f7it4Cn_9QDa0kA4-h-BpT-mvxTlhwf0uhWtUezZlH55nbcnPlHdldlmGQGUR7qeQsMIYe1pUDJWuRoYXYi4lYs0uKf-Y_KpYu94zPfQao4g0CykDoIizdtkG3k1cMhFu7lmqehnuDgkzIOXPbR81uiPHzeJGgdi6kxGvdgxRtAot3uVkZeiBVgfnzKtW548zA9Jt_bEUkCTFKOTvtCg3nQzxlb_2CWazfItH1le6tyXAYDHA8VWAHOcQpL-4i_ynVXc-yEOUV5evtoGImcNYNfeDYn4mkjXvOr4lhUTgeYipfLwIHzL-qZoo8DH-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9805bc1a1e.mp4?token=d6NyCtDZ5-04pF4NDJbVdthbiQaolDmSGn0EI3s8yxihih5VpmP5QqIrB6BDChXy9kkWZnqPhd6dpk95mjwBPB4y3z1GBzjUAYHsdNyDsjBWLfPU1LhzqOrB6xhPmCqJm6UnM5c3TZdTKU9fYwoB5sjFQmvt527m2i2Cn_dy_I4N81-68zUW3WxK8yosIq20S-SFI3B15YIKp1af9zDUJFtjUCeVl25GVL9KyhOH9OpZdberBwp_TR7oHLHwhoZUrzTyvmx0izE1QFHVYAGpkr7sf1mo_-HCuEMIh0RIr3WDma2ip7-upw1VJI_zvAjHwuwdulPUam3V0YgX9N5a2FL0uqz_R8xWpWSxDv9wLowG_f7it4Cn_9QDa0kA4-h-BpT-mvxTlhwf0uhWtUezZlH55nbcnPlHdldlmGQGUR7qeQsMIYe1pUDJWuRoYXYi4lYs0uKf-Y_KpYu94zPfQao4g0CykDoIizdtkG3k1cMhFu7lmqehnuDgkzIOXPbR81uiPHzeJGgdi6kxGvdgxRtAot3uVkZeiBVgfnzKtW548zA9Jt_bEUkCTFKOTvtCg3nQzxlb_2CWazfItH1le6tyXAYDHA8VWAHOcQpL-4i_ynVXc-yEOUV5evtoGImcNYNfeDYn4mkjXvOr4lhUTgeYipfLwIHzL-qZoo8DH-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیدمجید موسوی، فرمانده هوافضای سپاه: شهید محمود باقری زمینه‌ساز عملیات وعده صادق ۳ بود/ سالیان سال بچه‌های موشکی در حال آماده‌باش بودند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/659023" target="_blank">📅 16:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659022">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
بقائی: تفاهم نامه اسلام آباد بر خاتمه جنگ تمرکز دارد
سخنگوی وزارت خارجه:
🔹
تفاهم‌نامه اسلام‌آباد، توافق نهایی بین ایران و آمریکا نیست، بلکه تفاهمی است که رئوس کلی مباحث اختلافی را مطرح کرده و مشخص می‌کند که
جنگ خاتمه خواهد یافت.
🔹
موضوعاتی مانند امنیت کشتیرانی ایران و تنگه هرمز در مذاکرات مطرح است.
🔹
زمان امضای این تفاهم‌نامه هنوز قطعی نیست؛ اگرچه فردا انجام نمی‌شود، اما احتمال امضای آن در روزهای آینده وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/659022" target="_blank">📅 16:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659021">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
فقط ضروری‌ها ویزا گرفتند
🔹
وزارت امور خارجه آمریکا مدعی شد که «برای افراد ضروری» از جمله بازیکنان و کادر پشتیانی تیم ملی فوتبال ایران ویزای این کشور صادر شده است. #جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/659021" target="_blank">📅 16:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659020">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chBCl6lG4yB_hJ6ISgs8O_Lvz-FRf3P9pd0Vm-_H5PbEck1jlYvY4G2NkhK8FPni3yF7d3n-afNsQrbthCA1mo3OGhVC0ppVjF-OsU1Hvz7EM2smsqoiahCLQ4INhzCSr7dsQqEu1JqCQaBLT-k1EKcQUBwAHERynoSAv8YoHCTV7GfUQ5A3Z5N5FGj31tnXO4Foqjwqu48kF-zXEilGwt0lltcDE8DvTteY2ukNOhsSGUbr0LSOVrNfpL_E_6NmUsDwO1TV9qpVmupxMnh4poBLLSPiUO6miEg-QKo_KPnfk6c6Q4_Qv7DxbhPEEQQUCTBfG_uZuLAqMc-6oWalnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بزرگ‌ترین مسجدهای جهان کدام‌اند؟ حرم امام رضا (ع) در رتبه سوم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/659020" target="_blank">📅 16:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659019">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkK29OPH16XFVCRD4HwWUrzJ1qKnE0aBCpx7w3ncsFCj234p8aXT2g9_CSo_WWvQmG69XNFBsmVj-foLHJh-x_pe1nU1G7Lkr36-YUy4IDMwV_sldzb8NHYimFPQ0FNeASgMExqkhjwgxq7qqOZ_hY2VAaUT8tNN4YsB8B1C8w20qGuktFVT6H1Mpt1lHVfi-qAOH8ReHcWg-9Xj4SkS6H12tChvkBnGOQe1iKiHaUDt75--Y94cePW8N9aey7nHtbyYdWQpZ0zlHk-QUsQxRWb4B9dIocNA2dMQxFg2FBju3zttoMAMgftubmSMzp8fQl1JPH8gZUVBjWhK4vZubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وظایف مالی بچه‌ها براساس سن چیه؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/659019" target="_blank">📅 16:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659018">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1W4znHUR86YahmTqCfd4LpV7Ba9JpP7QCri-xmbrClMtuY-g27Aeh-XhAdTXrYtX6bFzDKQxKG1oH4ve22i8XDa0bTtYHX7ggwn7Dll8w_5TApUFzCJRsVuRjJpDBWQW9Pi-EpAprLEgCyl-PUwYfNBLKiVLfGshBabhHUoMrDJp7YE0_TTrh4hu6HuWYx6E24pJApWEWoLknKYg_1by3ePHwuj6C7G75cspGLt3obFvlxDFKOAXW5z4MiIdBLccAGXUvrNkfG8PVqVDkziYM35UkMnQomooAmszWWpINOd9kSv1OOvkfipCPawWiwe-HMguTbQHp78xQVuBkHwPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برادرزاده ترامپ: رئیس‌ کاخ سفید به وضوح به زوال عقل مبتلاست
مری ترامپ، روان‌شناس آمریکایی:
🔹
رئیس‌جمهور آمریکا مانند پدرش نشانه‌های زوال عقل را از خود بروز داده است که علائم آن به طور فزاینده‌ای تشدید می‌شود.
🔹
او در حال از دست دادن کنترل بدنش است.
🔹
برای «مشوقان چاپلوس» او سخت‌تر می‌شود که وانمود کنند همه چیز خوب است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/659018" target="_blank">📅 15:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659017">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12871ea7c0.mp4?token=tKGpG2PONJg9t1dtFDcUBG8NDjtgJFHN5AkncIOU01CiyNBexymoVF0mERwQzl3FlRfmlqD-51hpMiTbdUhlP6zMQQxMRjFxFfwwkoeClzl88i-IsyO9XB-1MtrzDD6yXpAmJK7u_yJBMitJJkWy18Jd6OdhDC4pepMDNbj7oB2oHz4w8xoL9uxjNJtxfiXAlwywxygcsbz3hBkfbQIN0np-UdhsXQY3Dk1YXcE0TsRYXbcgYHmKpOXaJUhBqtN4W09Ip0-r6gMCfgA57wrQ2CPg8cPQiBBYm4zbNNcy8c4tnCdCzGM4qx6gapYf0WCOqe_kfzAdkMlAT4VGXPDy1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12871ea7c0.mp4?token=tKGpG2PONJg9t1dtFDcUBG8NDjtgJFHN5AkncIOU01CiyNBexymoVF0mERwQzl3FlRfmlqD-51hpMiTbdUhlP6zMQQxMRjFxFfwwkoeClzl88i-IsyO9XB-1MtrzDD6yXpAmJK7u_yJBMitJJkWy18Jd6OdhDC4pepMDNbj7oB2oHz4w8xoL9uxjNJtxfiXAlwywxygcsbz3hBkfbQIN0np-UdhsXQY3Dk1YXcE0TsRYXbcgYHmKpOXaJUhBqtN4W09Ip0-r6gMCfgA57wrQ2CPg8cPQiBBYm4zbNNcy8c4tnCdCzGM4qx6gapYf0WCOqe_kfzAdkMlAT4VGXPDy1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حذف نام ترامپ از «مرکز کندی» در واشنگتن
🔹
با حکم دادگاه، نام دونالد ترامپ از نمای «مرکز کندی» در واشنگتن حذف شد. قاضی اعلام کرد تغییر نام این بنای تاریخی بدون مصوبۀ کنگره امکان‌پذیر نیست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/659017" target="_blank">📅 15:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659016">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdiNF_TKBGXGXUVsoO5_Z5ThdfoyQHRE0vVd3ZKjjB-CLsUu37Y4bCtOfRNwFuIv3CDga8LgHkgAkbpiKkv2-L0aFwO6MucCuMWu_yHodoaUFgml1-zOq7jB0NiayfWe9mpkWkqrTNx8NNdtt1_AMPDsQjgsDzE2hUrHKuiwz056WGyEndpGgJuhvGHjGCSSAOl4d_Hf4JugxVclYxEif7uHT7wSu_jnwq6WCkQ-oDZ-vHu17spHzlpvVnjqZ-X_w6csNxkBu3OGjpUzs41Wwk84t5ODtBMPjjbvUwAdyieY2Xd4Tu6eSa_HsSPKpywOc_HLwsWWHw5lD-nSDsrEXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم چه تنبیهی را برای رانندگان متخلف می‌پسندند؟
🔹
بیش از ۸۲ درصد مردم با ضبط گواهینامه رانندگان پرخطر موافق هستند.
🔹
توقیف خودرو برای رانندگی پرخطر و افزایش جریمه‌ها نیز با حمایت گسترده افکار عمومی همراه است.
🔹
کمترین میزان موافقت، به افزایش عمومی جریمه‌ها اختصاص دارد که همچنان نزدیک به نیمی از پاسخ‌دهندگان از آن حمایت کرده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/659016" target="_blank">📅 15:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659015">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVYvvsMDI3qCA7188TjqhuX9YpUmUSuVB_agK1pVeHUjSbGiv35fker1aFtnIP26-Tgr6Z12QSmD9dtOQQl0KVfserhnESH2zkR8VfT3DyQL0y0B8TYglE-l1hfd_NmT6EyhoqjoKfpoFmA34iAVlFjw4Y-2U31Qs2vsR_OjAWH8XPDQ8MKdFEdnID4rEUx_UBZ50pMq6usBK_aP7O-2Xro22-omhlOoYqt2R4QbRjZUN_DmjxkQR6s18L35NdBSmaSKtl-wqZc3GwFK6IdM2BFNWPqhTqO5ZnodLiQObtbqf8kMeOFBTOIBUFC-IVq46MuOfRkZk2bKuAFo5CkiRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
کاربر اسپانیایی: من زیاد از فوتبال سر در نمیارم، ولی می‌دونم تو این جام جهانی پشت کدوم تیم هستم
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/659015" target="_blank">📅 15:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659014">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5wxR8meuYhA4EhVPe4XX_sbTv5x9rof7cwR8uHNU_nTFsusfxKpDy1WdR8gAF2l5anVlStPubslitEpLBjOG9eWbiV7DfB8kkUENKfbjBPllKFbZWL8ZaJLQamqSAzI0CUkLif05mxsbz-2d8notw3KfCP6D6Kp5OSd9A7MFCi3ecRbmOZNCSE-Mdalb-QqtbAhmPaFtlSUofJwg8XuM99szUSlwPEPRuNR6PeQSGXIHxkyVzgu8RVnwK1NR5hCBI3Vta-v340lZOiQq0JWlk49VufnQ1_2Ur4adW8ZhoPVvRjg_BsDz2NFw3UoBCyiigaG8jEinP0qcufV09-z8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اطلاعیه شماره ۳ ستاد بزرگداشت عروج خونین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه  بسم الله الرّحمن الرّحیم
🔸
«مِنَ الْمُؤْمِنِینَ رِجَالٌ صَدَقُوا مَا عَاهَدُوا اللَّهَ عَلَیْهِ فَمِنْهُم مَّن قَضَى نَحْبَهُ وَمِنْهُم مَّن یَنتَظِرُ…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/659014" target="_blank">📅 15:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659013">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
هو کردن ترامپ در جام جهانی هنگام سخنرانی، به صورتیکه صدایش به تماشاچیان نمی‌رسید
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/659013" target="_blank">📅 15:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659012">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjeohZY2RVWmRjn8rwT9uePiPZEy3cJor7kcq-GnqLaXQngRxTYVENJ-FmhBwlN1x6TJLyF17JAXj8hz6j7345xbXFE5j746CvrFZ7t9EPYItuPJGpHVdQik_KzBEuKWXNFZF8lPAjSXhoXuskM5vZg67itcaJvvWsyC7X4edS1v9FIBni5FiQ9BA8Ijk3hHDYCUT-UWlu3z4d3rSmgIcPJykCwQbkB5cyDTMDCBTmObfRZ3iU5dLHAq1w9fiFxoQ0W9g_nVyiMVDwTg1AkibBTRjyv18vnUvPyFaoBHw5eF33y0w45ZnDi8_xjB7IJl6l98hfuUfgZzT2uJjFcZig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چشم نشریه انگلیسی مهاجم استقلال را گرفت؛ گاردین: عجب اسمی!
🔹
نشریه گاردین در ادامه گزارش‌های ویژه‌اش در خصوص جام جهانی، به داکنز نازون و رزومه جالب توجهش پرداخته است.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/659012" target="_blank">📅 15:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659011">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c928836e3.mp4?token=PNuxJk5UkWTKyEf3s898RfXYtwMlPIIWPffLC_yQhnh0R43S0kS1tYNxCzmPJN7fK8GLXIsInts30jC3LKSgvUIvye8uhKWpY1LhaOrXXu7xcr8iAxYY5LwmslyYOpwsKq2hjgwtko5ydAtdEVRfwA_HzNh53PjCNpCatNL6rbt69J5ar0crfBeuNmPr5JrwyK_DLac0rOaE2imBK1fzIl1AQcv9t7qyrHlTTOuJ7uXXiSe6qS23W34239HpquRUbXYAbRjgCs4JK5m_1r9rDMsp7CBkHOJZdWxEVnL48fWlYFQAupNWh9-1FbWH3VdofKwYK-goUbxZkOY-nyTgHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c928836e3.mp4?token=PNuxJk5UkWTKyEf3s898RfXYtwMlPIIWPffLC_yQhnh0R43S0kS1tYNxCzmPJN7fK8GLXIsInts30jC3LKSgvUIvye8uhKWpY1LhaOrXXu7xcr8iAxYY5LwmslyYOpwsKq2hjgwtko5ydAtdEVRfwA_HzNh53PjCNpCatNL6rbt69J5ar0crfBeuNmPr5JrwyK_DLac0rOaE2imBK1fzIl1AQcv9t7qyrHlTTOuJ7uXXiSe6qS23W34239HpquRUbXYAbRjgCs4JK5m_1r9rDMsp7CBkHOJZdWxEVnL48fWlYFQAupNWh9-1FbWH3VdofKwYK-goUbxZkOY-nyTgHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمدیــــــــد شــــد
‼️
🔶
پیرو درخواست سرمایه گذاران و سازندگان ارجمند؛ دومین نمایشگاه تخصصی زمین، مسکن و فرصت های ساخت و ساز تا روز یکشنبه 24 خرداد ماه 1405 تمدید شد
🕔
ساعت بازدید ۱۷ الی ۲۲
🕒
ساعت برگزاری مزایده حضوری ۱۵ الی ۱۷
✅
اگر دنبال یک فرصت واقعی برای سرمایه گذاری هستی، این همون فرصته؛ منتظر شما هستیم
‼️
جهت کسب اطلاعات بیشتر به کانال ایتا زیر مراجعه فرمایید
👇
🌐
@maliposhtibani</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/659011" target="_blank">📅 15:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659010">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
اختلال در خدمات چند بانک/ اقدامات فنی برای رفع اختلال آغاز شد
🔹
در پی بروز اختلال در خدمات برخی بانک‌های کشور از جمله بانک‌های ملی، صادرات، تجارت و توسعه صادرات، پیگیری‌ها نشان می‌دهد موضوع از سوی بخش‌های فنی در حال بررسی است.
🔹
از ساعات ابتدایی امروز برخی مشتریان شبکه بانکی از بروز اختلال در بخشی از خدمات غیرحضوری و سامانه‌های بانکی این بانک‌ها خبر داده‌اند.
🔹
پیگیری‌ها از این بانک‌ها حاکی است که اختلال ایجاد شده در حال بررسی از سوی بخش‌های فنی ذی‌ربط است و اقدامات لازم برای رفع مشکل در اسرع وقت در دست انجام قرار دارد.
🔹
بر اساس اعلام مسئولان مربوطه، تیم‌های فنی از زمان بروز اختلال در حال پیگیری موضوع هستند تا خدمات بانکی در کوتاه‌ترین زمان ممکن به وضعیت عادی بازگردد.
🔹
اختلال ایجادشده به‌زودی برطرف می‌شود و ارائه خدمات به روال عادی بازخواهد گشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/659010" target="_blank">📅 15:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659009">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmsZdvqct0BbHVuflvCt3ZAJm_iFxsKFA4CcQlyFG2WHHE_8yZuEOfpEVZW5ugWqOvFYdOj-gT75DfRMSPuFq1SlVjb2J3rlAYpucBTxJQL0Z-aoDY4QW9zGsV8YWn5Fj4SKm_vjO6Gk_E5pOj8w92bVfedVT5I6Enl-A9nTt3zL4ymvthQlvZL12o6t03IO9lf1YGCQKX6TRuasGHmJGGx5YsWz0rLmQqaxsNDb4MF2Ulj3Zn-aWn1XY-fbK2srqpIywUStdxVQ_t2B63826JHFNkPP4KzEiq0YHioOoBxLr5S73wfvQu19CnQWNk1FK0yRVOZ2BzbeJ_clwEGF4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران از جام‌‌جهانی حداقل ۹ میلیون دلار جایزه می‌برد
🔹
۱۶ تیمی که در مرحله گروهی حذف خواهند شد هر کدام ۹ میلیون دلار از فیفا جایزه خواهند گرفت. صعود از گروه و راهیابی به جمع ۳۲ تیم برتر جام، ۲ میلیون دلار پاداش اضافه خواهد داشت .
🔹
حضور درجمع ۱۶ تیم برتر، ۱۵ میلیون دلار و راه‌یابی به جمع ۸ تیم برتر این عدد را به ۱۹ میلیون دلار خواهند رساند. تیم اول ۵۰ میلیون دلار، دوم ۳۳ میلیون دلار، سوم ۲۹ میلیون دلار و چهارم ۲۷ میلیون دلار پاداش خواهند گرفت./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/659009" target="_blank">📅 15:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659008">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F31A0QcpYm45pEql-e1SQRJm3mpQDCrAeDBRfMIZEQ012Bk6El5dJfxVVeIvYNviAllrioyJOuXc3MPEOfrMqtd0Ik6YFnISLNyOybGxxeBtFNmnjvJr98eT8yB8Jvw6p4kf8Z59UU-KiNteOJk-qfZ9YazvJXUWjTSvX32qJNh-LLEFtX-7DjiLi6qpB03luCJ3vTnB0zzB41Dj9qAWkfaiDvaFKgYuL-o2PZ1IwVJ9DWJYAttiv5_PIVsg7774JhUesckFrXDoFeh2aLIuElGllV0ruBwTSDObrLhmR-yt1q7hW7scAZaU2HoqCCjNVUuRwhhU935C_zIZ3PUKUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه پاکستانی: توافق صلح فردا امضا می‌شود  منابع پاکستانی به روزنامه آبزرور:
🔹
احتمالاً ایالات متحده و ایران فردا (یکشنبه) در ژنو توافق صلح را امضا کنند و به همین خاطر هیئتی از پاکستان به سوئیس سفر خواهد کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/659008" target="_blank">📅 15:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659007">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88756deca2.mp4?token=kvK1_BAQ9kCsnZeBmopPpvBz2HOd0UnrBLV30JT-f-hexR5b9p3x4bDY24HBBI3MAHpdrvSkCFecIrLky8tNprpc05lUGDmMmpivgcWzW33KP6enUJNRsOJeyzIcZfr6dpJn2wYeJSy--dxudT06Xpnl-E5R902vF6zTXrbUdcDOPvve2N4MBR9UK39n5mYY1Bd_xljic4d2CxisP3JXgCIIxJ7btUe0-i_7-A5ou854Nil5yGdjludkJkXiGQ2JPH9QddhN7FM-rU8bHFsu1Oo8DXukRgn_y9fcCKfsH7wMUB5Ye5HA_53yCcclw4xQ0cm8DSM0c7wAaxFlWtS2DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88756deca2.mp4?token=kvK1_BAQ9kCsnZeBmopPpvBz2HOd0UnrBLV30JT-f-hexR5b9p3x4bDY24HBBI3MAHpdrvSkCFecIrLky8tNprpc05lUGDmMmpivgcWzW33KP6enUJNRsOJeyzIcZfr6dpJn2wYeJSy--dxudT06Xpnl-E5R902vF6zTXrbUdcDOPvve2N4MBR9UK39n5mYY1Bd_xljic4d2CxisP3JXgCIIxJ7btUe0-i_7-A5ou854Nil5yGdjludkJkXiGQ2JPH9QddhN7FM-rU8bHFsu1Oo8DXukRgn_y9fcCKfsH7wMUB5Ye5HA_53yCcclw4xQ0cm8DSM0c7wAaxFlWtS2DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برنامه‌ریزی برای برپایی همزمان هیئت‌ها با اجتماعات شبانه
باباخانی؛ رییس سازمان هیئات و تشکل های دینی:
🔹
همان طور که هیئتها پرچمدار حضور در میادین و و خونخواهی امام شهید و دفاع انقلاب بودند در محرم امسال برگزاری هیئات تقویت کننده حضور شبانه مردم در میادین خواهد شد.
🔹
همزمان با برگزاری اجتماعات شبانه و حضور مردم در میادین شهرها طوری برنامه ریزی می‌شود که هیئت‌ها نیز برپا شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/659007" target="_blank">📅 14:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659006">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HI1L9K2fhvVbWbjiTF7AbdPvFVqMDffNPiM_MfRTlJwOZAHrEgdbnE1S5J3qmhaT--jeFhIo1N8qmmx9QJDc9LH9L4KjDGAZLhv460yeOhjzqF32s_76NN1XfcalNs-pipjFVmzXuCg6OJKR54G6QCDtbI5SrsPwT5a8WY0ih5N0UyvvkYXIzGa8PpScuxLRzszMRwJUhYPOHDSjX6qeB_AmSp2Diur-8PfEvVZ0MWFpc7SPtIWyT2H7f4RsIKwkFtqrfY7fDKPLvbooXtZ-SjhWqtXW0hyAbvgXK7vx2vt-IUo8B28nRZ5fPInfdjW1KbIqr_5Pc1hGCQJzgzrx8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله به یک کشتی در تنگهٔ هرمز
سازمان عملیات تجارت دریایی انگلیس:
🔹
یک نفتکش در ۶ مایلی شرق عمان هدف اصابت یک پرتابهٔ ناشناخته قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/659006" target="_blank">📅 14:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659005">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ik6DALhbZ_23ulEPqntm69d_f-NS7yUvE4ze-booHNQP7CN-SXC125tAwRfBJ8GK9eBXGE-yppTedsliSzCzLn6ln5H668TYdbIEJ3WcaQfKvYrH1L4JI1rIZreJ-tDnYI21XHb-d5-rbv1H4DHj991xj-ts9xyWQzTbdVU3ecrLtMi1VGrQiA_jDya3U8_m42IYqm169s7fcgyqXzcvG04hTuvmWKyTqDx8MRAzwTmHfB6jr0qC-UrhL5eERYsB2pirhBjqxPp5sPG0eWmBq4QCnmQ5dapBc9u60Ewdag7kxVmdKFlBMxIe09jM3MPXZY4Og_35LtYLlOBQu5kInw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسپیس‌ایکس به‌تنهایی بیشتر از مجموع تمام شرکت‌ها و سازمان‌های فضایی جهان ماهواره به فضا پرتاب کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/659005" target="_blank">📅 14:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659004">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
احتمال حمله سایبری
🔹
برخی منابع از احتمال وقوع حمله سایبری خبر داده‌اند، اما تاکنون هیچ مقام رسمی این موضوع را تأیید یا رد نکرده و اطلاعات کافی برای اظهار نظر قطعی در این زمینه وجود ندارد./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/659004" target="_blank">📅 14:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659003">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b7dbca7c8.mp4?token=qW5MITYo7CHCaeDVoRDrfjnaa-plwimJmrcuTPP6ZeEsMw7C5EC04u1vbk2zxtrz3QpI10XEtZcqiAbXgwHsRURoe-cSI4JbZylWFapKUULaX907FjtcGX1CiL_1Zn-MnZKs87gqm_UJyulE9pYcRdOgOnNyvdKJFwXkEa2vJqZ7Khqn5cM_QImO-OxsmYC8m6WaKnBoAPvxrjmrK59BnCruj6VYFLOtiHHgTLUjrJ_DqjImK8OUrf5jtrsM4ygaCbBvaqIeVB5IDUN58-RKLhn41J4R1muceXzZq_7Do7u_glwFx5t7atkOE6Wt0CwVdVyVlA2SNck6MJEsfOo9FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b7dbca7c8.mp4?token=qW5MITYo7CHCaeDVoRDrfjnaa-plwimJmrcuTPP6ZeEsMw7C5EC04u1vbk2zxtrz3QpI10XEtZcqiAbXgwHsRURoe-cSI4JbZylWFapKUULaX907FjtcGX1CiL_1Zn-MnZKs87gqm_UJyulE9pYcRdOgOnNyvdKJFwXkEa2vJqZ7Khqn5cM_QImO-OxsmYC8m6WaKnBoAPvxrjmrK59BnCruj6VYFLOtiHHgTLUjrJ_DqjImK8OUrf5jtrsM4ygaCbBvaqIeVB5IDUN58-RKLhn41J4R1muceXzZq_7Do7u_glwFx5t7atkOE6Wt0CwVdVyVlA2SNck6MJEsfOo9FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هلدینگ تبلیغاتی رسانه‌ای باران برگزار می‌کند؛
"نقطه تصمیم "
🤝
همراه با مدیران و فعالان کسب‌وکار، از تجربه عبور از بحران و ساختن آینده بشنویم.
📅
یکشنبه ۲۴ خرداد | ساعت ۱۶
📍
هتل نوین پلاس
🔗
ثبت‌نام از طریق ایوند
https://evand.com/events/نقطه-تصمیم-015774</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/659003" target="_blank">📅 14:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659001">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاو‌ام‌پی فینکس | صرافی ارز دیجیتال</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqvIYxY6N9rAMm3LoEA8ddbk8CDX7Z2IjNXv8afQh9fgbfQS-351cyrHU7qD2LDDfHMZco_CnLRivM7eK7iDaSGG5lywfSKpfRa2TKu3Bt-s3R18F-ST3SPspSPxUXYqAXFOjgUyFE2KD5HCvEi6cGksi_TWPrR0xvMvZzqra1ZEgzHjlBtqKrzDvM1g1BTAQ5DNhj27V2713dAv8ZQCeRqctsH5T9BBGkBaSteDEVtAKeF7Vx1C-eTWKcnrLtGPzjIh4s-lxQMTadnw399rd4oIEijfirBnEjGss598puiHFuIfEij2Boakrz3RR7hZXBK9Tp0cdH7_rGGpRzyFRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
جشنواره «پول رو پول» اوام‌پی فینکس شروع شد
❗️
📣
از ۱۷ تا ۳۰ خرداد، با واریز رمزارزی و مشارکت در استخرهای طلا، تتر و بیت‌کوین اوام‌پی فینکس، علاوه‌بر دریافت سود روزشمار قطعی، به‌ازای هر واریز کریپتویی، هدیه بازگشت وجه هم می‌گیری!
🟡
استخر تتر: ۱۹.۴۵٪ سود
🟡
استخر بیت‌کوین: ۲.۲۸٪ سود
🟡
استخر طلا: ۱.۲٪ سود
🟡
تازه واریز و برداشت ارزی هم بدون محدودیته!
📌
حالا چطور ۲ دقیقه‌ای شروع کنیم؟
🟡
ثبت‌نام و احراز هویت
🟡
واریز رمزارز یا ریال
🟡
دریافت هدیه قطعی به ازای واریز رمزارز
🟡
مشارکت در استخرها و کسب سود روزشمار قطعی
🔗
شروع واریز و شرکت در جشنواره
❤️
@ompfinex</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/659001" target="_blank">📅 14:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659000">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
روزنامه پاکستانی: توافق صلح فردا امضا می‌شود
منابع پاکستانی به روزنامه آبزرور:
🔹
احتمالاً ایالات متحده و ایران فردا (یکشنبه) در ژنو توافق صلح را امضا کنند و به همین خاطر هیئتی از پاکستان به سوئیس سفر خواهد کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/659000" target="_blank">📅 14:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658999">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b37a176f41.mp4?token=X8WX_i23DShKGV_YbwY31wV6CQsTB9mOI9_Jv6VRwvnnKjG7Tvz6fEmcO3DaRyml-w_8TyYB1UpUFp4VqIA5MQvIjxTSnt3J29cghhj3o14CX2RZcG75Wx2FKdn433h8HaD19S0UGGnxm70ukJVYj-gZ2n_hIkHT_dUSXNhYzF2C44qO-BNNX6xxX2dG36d4E3eHjgpwAU36KrlZPLYhbYfhG_EzD57VPjrsnyBpX8Cl4vShXXEvU2wfJHWSy4AQ9SYC9-YfTP0tGq1weKIwMFtVhhVKScF_UK_jsP7pexWhjEG7sC_zSvCOd3rsfm6T89zzFwys6sMmXcU01ugCqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b37a176f41.mp4?token=X8WX_i23DShKGV_YbwY31wV6CQsTB9mOI9_Jv6VRwvnnKjG7Tvz6fEmcO3DaRyml-w_8TyYB1UpUFp4VqIA5MQvIjxTSnt3J29cghhj3o14CX2RZcG75Wx2FKdn433h8HaD19S0UGGnxm70ukJVYj-gZ2n_hIkHT_dUSXNhYzF2C44qO-BNNX6xxX2dG36d4E3eHjgpwAU36KrlZPLYhbYfhG_EzD57VPjrsnyBpX8Cl4vShXXEvU2wfJHWSy4AQ9SYC9-YfTP0tGq1weKIwMFtVhhVKScF_UK_jsP7pexWhjEG7sC_zSvCOd3rsfm6T89zzFwys6sMmXcU01ugCqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیش از هزار نفتکش منتظر اجازه ایران برای عبور از تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/658999" target="_blank">📅 14:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658998">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مالکی: هنوز ملاحظات ایران به‌طور کامل برطرف نشده/ ترامپ مرد توافق نیست
فداحسین مالکی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
آخرین دور مذاکره‌ای که در تهران با حضور مارشال عاصم صورت گرفت، قرار بود ملاحظات ایران به طور کامل برطرف بشود که بعد از آن هنوز اتفاقی نیفتاده است. ترامپ هروقت صحبت از مذاکره جدی می‌کند بعد از چند روز یک عملیات جدید انجام می‌دهد.
🔹
این تازه توافق اولیه است و اگر صورت بگیرد در ادامه، راه بسیار سختی برای توافق نهایی داریم. بعید می‌دانم ترامپ مرد این کار باشد که بتواند دنیا را از جنگ خانمان سوز نجات بدهد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/658998" target="_blank">📅 14:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658997">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
وزیر نیرو: جیره‌بندی آب در تابستان نداریم
🔹
باید آب را با صرفه‌جویی، خوب و بهینه مصرف کنیم.
🔹
در کشور حتی در زمان‌هایی که پر آب هستیم نیز وضعیت نامناسب است چراکه در اقلیم خشک هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/658997" target="_blank">📅 14:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658996">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
افزایش سقف وام ودیعه مسکن دانشجویان برای متقاضیان شهر تهران
🔹
بر این اساس سقف وام ودیعه مسکن برای متقاضیان در شهر تهران به ۳۵۰ میلیون تومان افزایش یافته است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/658996" target="_blank">📅 14:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658995">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
تیزر قسمت چهاردهم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای علیرضا غلامی که در لحظه نشستن روی مبل ناگهان روح از جسم جدا شده و در بیابان برزخی شاهد عذاب اعمالش توسط دو موجود وحشتناک می شود ولی با توسل به حضرت رقیه نجات می‌یابد و به جسم باز می‌گردد ولی آثار عذاب‌های متحمل شده در برزخ بر کالبد دنیایی او هویدا شده را نظاره می کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: علیرضا غلامی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/658995" target="_blank">📅 14:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658994">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ecf926c4.mp4?token=D1ZzcjDBBBcRmXshZ_Q9VV0poJMyu23zsgLMnGPsj809AloVJPh4ns0JakO-JDUc1M52k69YUxJQHnxBM1M-S7N1qTEv1HV-HuNTiDFE3wm5a46CwXkVwJNh8xD6jtvZ_yNnj78pUnfH38mUZeVcja1yn0Jv-b6qtWhY9OQvvF9dCMt0Oez0RyXrJDq7o5XgMyeOyKr3dqvK8g89vTa5amwFVLLCK3jB9Zn7PpzDOiu835drarL9VQ5teV21KTSTXCYEs8X1vAjXz5ZE3FBTa7X-S14R6eKWH1koge3l4Ht-k-mr9sGFZYN3I8kLGghrdt_2OtTPNIw5olfGH5SRhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ecf926c4.mp4?token=D1ZzcjDBBBcRmXshZ_Q9VV0poJMyu23zsgLMnGPsj809AloVJPh4ns0JakO-JDUc1M52k69YUxJQHnxBM1M-S7N1qTEv1HV-HuNTiDFE3wm5a46CwXkVwJNh8xD6jtvZ_yNnj78pUnfH38mUZeVcja1yn0Jv-b6qtWhY9OQvvF9dCMt0Oez0RyXrJDq7o5XgMyeOyKr3dqvK8g89vTa5amwFVLLCK3jB9Zn7PpzDOiu835drarL9VQ5teV21KTSTXCYEs8X1vAjXz5ZE3FBTa7X-S14R6eKWH1koge3l4Ht-k-mr9sGFZYN3I8kLGghrdt_2OtTPNIw5olfGH5SRhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موج اقتداریم
❤️
#ایران_من
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/658994" target="_blank">📅 14:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658993">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خبرفوری
pinned «
♦️
اطلاعیه شماره ۳ ستاد بزرگداشت عروج خونین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه  بسم الله الرّحمن الرّحیم
🔸
«مِنَ الْمُؤْمِنِینَ رِجَالٌ صَدَقُوا مَا عَاهَدُوا اللَّهَ عَلَیْهِ فَمِنْهُم مَّن قَضَى نَحْبَهُ وَمِنْهُم مَّن یَنتَظِرُ…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/658993" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658992">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
تا دقایقی دیگر، جزئیات مراسم وداع، تشییع و تدفین امام مجاهد شهید حضرت آیت‌الله العظمی خامنه‌ای قدس‌الله نفسه‌الزکیه با صدور اطلاعیه دفتر حفظ و نشر آثار رهبر شهید انقلاب اسلامی اعلام می‌شود./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/658992" target="_blank">📅 13:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658991">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejv1EWNoTzJQfNxlWcKAdD2c3rz78GA4LbDPaULFXXlLAEnW4n19dzMCl-hJjsNGHX9rR3ns-vEsw9GCr4OeDrArOmyIKrL3uwXTiR_Pead2dVhqGYI7wYB1IRZWEGvA_UITBH0itppDPhhWtTE614mfHzU2Dq-dVPw9nqblRr6vOSdcDk0lO5ffoGdUM7O33tE8zJK59DSM8agwhAY1fLFDH2QMfCOEmD-9PcLKGh5lB0hfrFwjEgW5xmAzvq_gs9jy0YMeEDQZS9gqmIxqInJ19V_dx1b0nZBO9-t15wZwXThP-WEqA3FxC29k1H03TT8MkpbqzfqQFNZZgreVzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: ‏به تأسی از شهدای جنگ ۱۲ روزه، تا پای جان برای پیروزی نهایی ایران عزیز ایستاده‌ایم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/658991" target="_blank">📅 13:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658990">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAKqokdo6a1rjt8cBnHb3qbpKwpNxILaJVjkY6cxvv2OdItVrmEfsJ-RVpzk9-f67mqAXSXx90RFo1Xgd50xlAATpQBYOj7-gjNd6KN1ZSIsYKBhQPOzuQdGDVYVgHcmQlncV1NFZ5ol6v4DXeHP3DmTtyHgjOkXir8BrAv7BBqPfWh2hwlGg5aVug9hAmZGvFtLR0rO5M2lAUijlEBiAhBVU6AuewVpARLIRyqUa6c7teh8WYwC3WLoVA3IoxOHTXmPNcvWNJPTbIhPMnhunK_VExXzx02HBKKnh9CSe3JfGxbj3dxPcX47QSXvVEs4SDsG4czHt1OIP6gp52PqTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تبعید زنان ایرانی حاضر در آمریکا به فقیرترین کشور آفریقا
ادعای آفریقانیوز:
🔹
دولت ترامپ، قصد دارد تعدادی از مهاجران حاضر در این کشور، از جمله حداقل دو زن ایرانی را به جمهوری آفریقای مرکزی تبعید کند. انتظار می‌رود در این پرواز، مهاجرانی از افغانستان و سوریه که در آمریکا پناهنده شده‌اند نیز حضور داشته باشند.
🔹
این اولین تبعید به این کشور بسیار فقیر آفریقایی خواهد بود که سال‌هاست با خشونت، نقض حقوق بشر و درگیری داخلی دست و پنجه نرم می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/658990" target="_blank">📅 13:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658989">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693e6c1189.mp4?token=L6bgJ3fJ-TAIWEn854ccR_HvFemOtY8AHiBTQjYtkRL-cjpOyfiNxU5Pcl-IBZqNAFaLDcrIQo_rfIOfredGLb8krlORi9iacZoA28lUcRW-0MNWPnA-9lCg-x5S00R7Uk8tGpBLO0-sELH_ZXsa4qRN9nBfxWtNwTaBENusNKASvIgp96fa0eA-nqZC_lVQHvQxiPS3hKJ-cpRRLDlSENXH_93y3wE5HEvhU1MXAjmsu9iuuo7MdM22M_EpWETh6XzL6oz7bkjbY7yHfGdbWqfbn7VLQoKiRjTVwvRpcY_owzQDQi0r-wOe_dSSYTM9ajP0RAdv1YX9wjbIdNzjpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693e6c1189.mp4?token=L6bgJ3fJ-TAIWEn854ccR_HvFemOtY8AHiBTQjYtkRL-cjpOyfiNxU5Pcl-IBZqNAFaLDcrIQo_rfIOfredGLb8krlORi9iacZoA28lUcRW-0MNWPnA-9lCg-x5S00R7Uk8tGpBLO0-sELH_ZXsa4qRN9nBfxWtNwTaBENusNKASvIgp96fa0eA-nqZC_lVQHvQxiPS3hKJ-cpRRLDlSENXH_93y3wE5HEvhU1MXAjmsu9iuuo7MdM22M_EpWETh6XzL6oz7bkjbY7yHfGdbWqfbn7VLQoKiRjTVwvRpcY_owzQDQi0r-wOe_dSSYTM9ajP0RAdv1YX9wjbIdNzjpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر رفاه: همه موافق هستند رقم کالابرگ افزایش پیدا کند اما در تامین منابع هنوز به نتیجه نرسیدیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/658989" target="_blank">📅 13:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658988">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
تا دقایقی دیگر، جزئیات مراسم وداع، تشییع و تدفین امام مجاهد شهید حضرت آیت‌الله العظمی خامنه‌ای قدس‌الله نفسه‌الزکیه با صدور اطلاعیه دفتر حفظ و نشر آثار رهبر شهید انقلاب اسلامی اعلام می‌شود./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/658988" target="_blank">📅 13:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658985">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htQa2YBuDpTajewO8a7-9t9BNBw2Ryiv6Rg6_Qfz-Q_c1WQ6z2W4vQQXdr0Nl5ge57Ejd2xoMFHEBgbOfCziesRFzRJ9u1cxs5TwHg2pd5_wVEPGLFUE72H7XHCgjlnTh4Yp-MFxOHf50LkGI48Fy1Inb7BG6wcQDBKaItvyqnTCuI94eUWY9dO_ceoWgCHAlruoJEMHCn-Rn_le3mByRP2-rBpVufB_bO5Qw15r5ArbEgxRscDVLOrOiweWVi5Qe1ECs7NCj8_Vr_pbPvPWvQiZYlgUfNw1p4E7XhF-q0yQnix8yFdIN4N17S7eIrGktN3vcnDwJzs_libpo4-unA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعرفه آبونمان تلفن ثابت تغییر کرد / مکالمات ثابت به ثابت خانگی رایگان شد
https://www.tci.ir/portal/home/?NEWS/235300/235321/558501/
@tci_iran</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/658985" target="_blank">📅 13:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658984">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTIj3LAW_M5w9vFVOUCRaxhpAip716YgdOiQCzZm17AAJuBHXm-mibBZzFDhg3qlB-5Tyln4KKLp0Tu3Te6jukLBk372F5dhh5ufuLgJdjhEQj2uuKQ398KaFKD6R4o6A78zm10-tPCrIFTq2PpKyd3HccQ0P_h9sBl8-5vU4gK2GKQvOBhzeSTxiQrTrF-uaqfH9FiHqgsbasrJQvsyk1av_-VAbvKp304RK7UY0pbDqTwxJVSiFRs5A7njdXgiBhz0bYlU3w_KCF63eZUVHlTenMJaZikpHZXcJXLG3hk3GSBndChJlELjTwBp3t2hkTcKVzoc_D6pSvJhzxBBcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دماوند باشکوه از کویر مرنجاب و بابلسر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/658984" target="_blank">📅 13:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658983">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70cd551883.mp4?token=mZfQX3Btbn_LHMmBqiW_83oJeAMf4PCmRZmOxXBJOp-cEMLsFeg6eR6s0pGsuL-EHOa1fdaZbLyunY6WnbOFer474k_P2mwGmv-PMRDTuojFahZgpWE_lh29i_n4HWGv3R3smHbIb5kUfBa7YwB0ax_F6PheQU6NJTN7cPHDyyCTKaqgFh8jBXph5vR6erL2uIdm6e2wJhOQnuyEk4MbRVnww1C-4Xir3OzPbl1c2njUn3ohms96fmsRLYTppJDAihJBAKB6lLeLx-OqfQJdcvE4XPRlDu87dv8vN5xsCkVkwPPJF_YnK6KSL1y0nnCxtqSiRw6OakM4gBU3CB3clg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70cd551883.mp4?token=mZfQX3Btbn_LHMmBqiW_83oJeAMf4PCmRZmOxXBJOp-cEMLsFeg6eR6s0pGsuL-EHOa1fdaZbLyunY6WnbOFer474k_P2mwGmv-PMRDTuojFahZgpWE_lh29i_n4HWGv3R3smHbIb5kUfBa7YwB0ax_F6PheQU6NJTN7cPHDyyCTKaqgFh8jBXph5vR6erL2uIdm6e2wJhOQnuyEk4MbRVnww1C-4Xir3OzPbl1c2njUn3ohms96fmsRLYTppJDAihJBAKB6lLeLx-OqfQJdcvE4XPRlDu87dv8vN5xsCkVkwPPJF_YnK6KSL1y0nnCxtqSiRw6OakM4gBU3CB3clg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم حضور سلبریتی‌های سرشناس در جام جهانی ۲٠۲۶ / از دیوید بکام و تونی کروز تا برد پیت و کیتی پری
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/658983" target="_blank">📅 13:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658982">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کسری بودجه دولت برای خرید گندم تامین شد
رحمدل بامری، دبیر کمیسیون کشاورزی در
#گفتگو
با خبرفوری:
🔹
دولت کسری بودجه ۱۵۰ هزار میلیاردی دولت برای خرید گندم دارد که بانک مرکزی این هزینه را تامین می‌کند.
🔹
در حال حاضر کمبود گندم وجود ندارد و در برداشت گندم مشکلی نداریم و ظرفیت تولید گندم ما ۸ میلیون تن است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/658982" target="_blank">📅 13:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658980">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
اختلال گسترده بانکی در چند بانک‌ داخلی
🔹
از صبح امروز شنبه ۲۳ خردادماه، سیستم بانکی تعدادی از بانک‌های داخلی دچار اختلال و قطعی شده و تا زمان ارسال این خبر همچنان مشکل ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/658980" target="_blank">📅 13:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658979">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKsJYcZ83jVLxpgPibKGizmgOPYus8tOHHLvKo2WI_2t0oGWGiCczCz_dgVNswiyq2uch8OTxV-uqn7cdt1Y7UPPlQgCbRM2kEaBT6ZZG1S5RywK5Z0LGLBqo6ry63poH0se7YSeR3lgkUCjXvqkWMAi-ulTJuKq5Ke5Gn74tBxPB9lwbRVYHsIURqMP5ARneUwf46EanU5UtHdt0TN1YgHM5oxDlQRp8glrL2xUuzO4dTz2w43Dq8NFhQTRXLygpVq89HHKZxC2vSwwdJ3j2cRjaz2y1EkgEIGo2IHmeuR-sov25wvZlAQu7IqNmvSGft-8Et14sQy44mtYBQEkrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند فکت جالب توجه از صنعت گل و گیاه ایران
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/658979" target="_blank">📅 13:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658978">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2NLuJQXgbTMYdJu3LaYaqG63eUSoov5-BM5s9bzAsnxd7kCdRyo_p4t6POjd8cvUsqb9dwG_qZ0RGcyi-goK8dLL3hJFgoqNZHtx8toDF3ykqtkQprMzc5dB2Q8_PovC2bh3c-rgooEUgqPyLT-mBlBJfL1XXbvA39yw4AncT51VVBZmLemYY0_88T9NRQsb--ymxIY6KyhYeBBGMPW5KaCLvPLfDVvRmuIH0IvD4Q7vt9rrBv9eIY5GzHnAiMD2NHlFmBj32PDJ8SRSjaV-cBDza2SHH-iX-peMQe5Fypu6idpbZzQgF4omeRcDnGWihd94pimSlwTHf-3b7Ay0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس روز ناسا
🔹
عکس روز ناسا دو عکس را از زمین به نمایش می‌گذارد که هر کدام از منظر دو سیاره متفاوت گرفته شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/658978" target="_blank">📅 12:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658977">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
اختلال گسترده بانکی در چند بانک‌ داخلی
🔹
از صبح امروز شنبه ۲۳ خردادماه، سیستم بانکی تعدادی از بانک‌های داخلی دچار اختلال و قطعی شده و تا زمان ارسال این خبر همچنان مشکل ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/658977" target="_blank">📅 12:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658976">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEjSa_jjbrMvBTHEVJrsFyLQ4AMYdwzr6Y4Vl8TZRVJ1F-CijDAZHWvaJbHOOs-ApvqxfS--NLBo-UhLOsuMmp_BRBZJGhG0rG5auys9c2xTAIy7iBk4REewL-13kHsgoYgAjIHH6t78YsTKOKbGXS14lOFDqYBD-QlKgq4P3nahZ8LAsjLUj2M0TDOIX-Fo8UFltHbXGb_29BaICkaUDvX_DNaZcYYQAPnvpA-d8-S63ujNQFUzKuElo9wTez3LCSCPibsJBrF94GJKMJT2_J-QYEqV6ql9ps9stqdxH91PWoqfHoll_JzIlJt1vWj94jmfnnEeTHoAUnjGAJ-inw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی الگوریتم‌ها خبرساز می‌شوند؛ چرا شایعات سریع‌تر از حقیقت منتشر می‌شوند؟ #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/658976" target="_blank">📅 12:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658975">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlC9zOupPAwCCHmdHf5AQcf-A1NL6A71U61bacpMDKyu3kRWMRzmBGklwOzkNCnMu7uK7tNswkk71jW9_8rlBtlNPqKxaFrno-fnbgKr2gn6FwgVJcfHIniTxu4F5dCEvKDeepwmLUY8cvI4PvAeIz8reh9Lik7skMED6eWozuQQkpg9bRhxyZkmMuOgQ71WQkKm_E5XkBR5OzDZwo-kRoG0TUBj6CjTlIMUTFwvstq-5s_njBnIqCRREUDsubm4T2xIa4cpQaxbbZ8Us83gve06LsbZv3teGOXQrLbsOkn5nYqHtvv_9-ztzLYJ8cAOVPiLv07A3MMKv2wQM_9H0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس با یک جهش سه‌رقمی دیگر رکورد تاریخی جدیدی ثبت کرد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۰۳ هزار واحدی به ۴ میلیون و ۶۹۶ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/658975" target="_blank">📅 12:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658967">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEJepDyC5xCwB5qDRj1IJUwkyrinmQTUdE8crRlPFT1uzOgY3eZ1R2N2UL7lUI7F27JuNafVQu-loNxun3UqgeZ7jWV556fW6XzBKBm5dkJaNN8LNyRqK1QdCeRZtHQZDl8OlNXUDqKA0NAUGhTooNgi2IksfdzEb01c5_qsSW6PpRfeS03QyueisIVyuprdL55XiOBL_jyEfxcr7wf_zVuQrsgE3GbXjrZMLfpME_CIYP4KWcfaizxSPxIZI3pL4Ao1J9hzST78hTTFXx8fnDevibDbhRt2e1XRNNX_EOpwwqQaxmYJRBoNqy4jUxMm_AG2lDxP7mCiYyIqOW07Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDK_2AsMAySBYgVCwjRh_FlhiErj4vfANd2MBc-6syXZm97rojVcxqMPe2ZKGVdQy5wqpY6WK4THGNRjl8hZ3Zpo5HuEAKOMt0UACqbLBtIst-Lh2OcglKPdsq668jKclNAhsTWFg8tB0LvLfUXfRNaxD-8RF1SBF_Q11jtGFS6mMeuCGaPEfIu_bzljaCStjWSeOrgbpcQMoT5pqD4p0zICj04tT_9ScGBv5Gwhw2Bes9kU6y9HLAprFG12XKFv2gkkl1rqHcPzVbQv7peLPlZIklx7Chv1qAEbpQD6SudmwU5FBt4zRTtniyl0IXFuLJLfiJU3GXyLyAFCsAh5FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FNK9sGjS3a35DonyZLenFrA6lnJdqEsDn4HAzLPl2FzpatdnawIp293VDpSPixArsxThHHzeTMpioxGp3hJQKJk_WDjQ6j8YT67iHE9qng47DZ8iahaMFfxxUWSdj4dLjQgsOUeUpLCbqfZHfj-DY25N5jsLM-WvqEWM4TI9UJJJq3U_-wm2zG6LETKuzPo7avBdZimgI8AVRQ8nK9DTeyGIN8pOXXlUj6i1mDlJPAwbh2VdjtAXWgIOdgRqczut0SrRJ7IPeFldEVKoLT2UqUBGzrXXqPaITcqI18vrNNZu9DzfdMEQ260DLEV1tcTPz48suBY892sQ2ESaPtAlVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fdSmazAByl-2u2W3mjkka9lW89FLGerQ_Zts18oizo6EicUMhiBqICyM8GGyK_JSm5G5Wyh0rbecCcrpJxQ-hUfXoN-c5-ptfUB67woOemn3V2Z1NcSjdL8xQgtQNdAaYVzZfctG1zLrHcdQCKvyc9UqO0XDYhoTGyC9qLge7uPTVCYZNn9gJow3epOWCFvI-FXMdboiMDO5z4FqTDnF3gUd1HiL2EEJ03E9y0dGZoJdKAPdjqfUTwMBONZiIi11MszygZR9AqOvEQZblvTaKQBIcbYWyMdsFD7ewd76FjzYyePrfDRIRPaNEeZzot6anI4n_WavLFPoNbsDsus_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDa8S0bedN2uqHVzprDuMRAu2dYIfn6JnWSBMwOx7da1AdpPtg12Jp9bijjWSJ9-MGQWVf-TRTe-TY9UaBj9noNZd41FR9PM0m-1rtGPF7kLV4sfoWz12aAP36eoMlPGY9-zjHKxU_p2Np5yTOxHvhWiW9RT0yybYsueQoFASDWIDw0IlsuFNLVn1WO68KV6jW-P9MEeU5uQxCd9_4zMmolvPIM6R0BX1a4_G5PYyq9LjkmvL5h6TJ2AlhKaZPyIa7zDshB1uKDoK8RIR1DP7CZs88ewDSlfJxPIlF_gQUDmnhbgrXGrYHaIIxpMWGsVeOiyqQ3JK6Jk75lHVmsERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DYWP7pb0CA3iVq_9UZSqx6UaeZAf1t9-yDcBWYSYG49FELoL2Vq96_7ybBMEIE3PKYiFpEKfE8chSaTlf1vjPWhpEVW_lg75OvCS1UQqpMU6UsYuNXDvmew_EOMLs-q4FkjSODSeTJycgtpmc3iQc_nUroixjpmv-iilf7ErBeMbIhLTGfeSiDK7eSbKbew1G45QIC0ojJ_O43qzlD0OQgv1-wOwrP1nT_EyNaFVrf2O7m7t_nubU8GD33iGp2wsc9y35-zeLRysmKMWq_6MbEB5b0Jlwsp3mMcB9ibY4FcEM0Vob60DZlVPZ2gDwtvYojpsFsKwH8BjjZmx-5oqCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mdbDtwb_SZP_3_nDGxb2frKmOMyV19NqQMjh4TZxh0DGm3yLiVGFX8IIe_nMhm6_rnnPW1EqoFAD9UOI0ZLEUPPwcMn0PeOx6Jnfz753v0nlzsINzSpAKDTjM0HsrjpozKD2rBby3iMqggbaPEDa1ukUM86xBkAOoi8iVqwYp2SkDMwoBWuA702hhLyPlZnaFxTLnpmxRe-z48EGGMj3fznuhjI6rUSEhgxKyl8G_f0mB9_HwfrW9MnOZulGCNfG-cCpt5_jKBmRwqbl8EWTXrujtnZpV277k_ng4nredNPqkopEBrt1PLDM-a0evS0A-L1UaPsxeRJleFus-Q9m2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GCvedrt4uZgkq-EmKr7iFcxTTlGcDufRessUwBLij034mfAEHAbQeS4kBdfSlApvssTgdFBopGxQc19AK7uyhqjH8EN-SX4Vu6eF-AiCpgxy_0_5Ubs0mg0H_ZHu5Oow5rDV46lmGAYjfiPqq-8cZ2cw2RFFVUtLfG4ZritqdhMqi3kcPbddN6pWjuvLAKWbwBlkIOKowZHAQzbqCI-o_zntu_yN3My410fxrCgGsEgm0sMggzB6gHleq7LB3tPwYi8HpoYRooOKPkSaWmX5l68-F3rSIqQIjiYXlp5TfWegAurGnYGaj_Wn5uOA9Rn1gXcgSAl6rhAhX-1u-J3cmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مشخص شدن هتل تیم ملی در لس آنجلس
🔹
فیفا هتل وست دریفت (Westdrift) را برای اسکان تیم ملی در لس آنجلس معرفی کرده و افاضلی به عنوان نماینده ایران قرار است از این هتل بازدید کند.فاصله هتل محل اقامت فعلی تیم ملی ایران در تیخوانا با هتل Westdrift در لس آنجلس ۲۶۵ کیلومتر و با ورزشگاه محل بازی ایران و نیوزیلند حدود ۱۰ کیلومتر و کمتر از ۱۵ دقیقه است.
🔸
تیم ملی ایران ۲۶ خردادماه به مصاف تیم نیوزیلند می‌رود.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/658967" target="_blank">📅 12:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658966">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
واقعیت پشت ماجرای تغییر آب‌و‌هوای ایران!
🔹
امسال باران زیاد بارید، بیشتر از ۷ سال اخیر! خیلی‌‌ها هنوز هم مدعی‌اند که همه این سال‌ها دشمن مانع ورود ابرها به ایران می‌شد.
🔹
پشت این ماجرا یک واقعیت علمی‌ست که در این ویدئو خواهید دید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/658966" target="_blank">📅 12:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658964">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDoeL2gu_Q7V6HAPVr1JxBhNoWF7Sk2RPLm-_XAGPpRCact3_gOYsotVlZXkY5AlsyeOYMqak4zoSm6cfnOM6F6tCwb6Om-Qmt4zt9MvkkpHk80iOKGGPuBzvBMsWnnYbETQjW92RFHv2wmTMrOYxruIxuO5-MbROWO0K4PZxStYPwEQSO_1w82J4BZIZfRCDjCUn8hkFOxIQmb41mwZkBx6T_mmtfy6Egfk9QdbxvedRxGRGvT2fIiIPkV2qusLCX0zWUvhCs411STTsCCtyMt6rQJ85MXJB-10D0T31lthiM7zUT47ua3l82g3f5bddUNXd5elKXnKQq6LTYNdDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم‌نامه همکاری ستاد طرح یکپارچه و هوشمند حمل‌ونقل و ترافیک شهری کشور و شرکت مخابرات ایران امضا شد
https://www.tci.ir/portal/home/?NEWS/235300/235321/558215/
@tci_iran</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/658964" target="_blank">📅 12:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658952">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
بمب آماری بنزین؛ ۱۴ میلیون وسیله فرسوده، یک‌سوم بنزین کشور را مصرف می‌کنند
🔹
۱۴ میلیون خودروی سواری و موتورسیکلت فرسوده سالانه بیش از ۲۰ میلیارد لیتر بنزین مصرف می‌کنند؛ معادل ۳۳٪ مصرف کل کشور.
🔹
کارشناسان می‌گویند با جایگزینی یک میلیون خودرو و ۴ میلیون موتورسیکلت فرسوده، سالانه ۳.۳ میلیارد لیتر بنزین صرفه‌جویی می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/658952" target="_blank">📅 12:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658951">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajh_iOvryV9-mrlgYwP__DeflmwoD2DlLkRBoKhzVrKKDId0cR4sOjrW_XnaudWtFRW9exlAMz442YpGmLPrSX16xYG78kPE4F6UVnQXUNtpmCMfDCH2YvjeFc_WkGsmpCBvykAiwHQy7nfvveL2CVUUAiB6PPI19Ni-g4-3K_nW6h0hhscEfQNsApOHCa0rvhda03i-leyyyQ_CrCcNM-LddRIQpuQVGBFk_IyTaW6K5e8A-TvrkzVvFSIDDI8YLfN9gUL0o7rF8jWajAfzZznGEzqPumTIP4xrlZt14Mmk8pX_y33S3IG5mBOv97pCsR4XG_lIHBhAszc5HEdaKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/658951" target="_blank">📅 12:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658949">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/593425e075.mp4?token=lZ1PVXZr2xwmwfHkSARcSqTHxrC38lWywnIHhoKpMzApgWrszsLA9b1BuxuAlVl95rMGce3jI4YOppN_Ggoy1tHPigv7AtcDBPLOr2GjSu6WxVF2Agf_1uws2j1foi479l-s69kJFzpJGVgSHqN32sX9Q0F1_EFM8u4JEDnpok9OMEjHvCoKkCwYZWsWrAOuodtnL7KmjAYp2wMKVOa5xuK89MHgxcZz76IOWYzEr6SJ5OwWB1ul0oOlyOtFbwgxVKEjUH7LaYsDR9mBtlMdaaXv1eYitb_aQ4xuG_-cjJtI_q2vifTC1RX14S1zH4_XIJQRgd1BVFW7Pdymqu4eIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/593425e075.mp4?token=lZ1PVXZr2xwmwfHkSARcSqTHxrC38lWywnIHhoKpMzApgWrszsLA9b1BuxuAlVl95rMGce3jI4YOppN_Ggoy1tHPigv7AtcDBPLOr2GjSu6WxVF2Agf_1uws2j1foi479l-s69kJFzpJGVgSHqN32sX9Q0F1_EFM8u4JEDnpok9OMEjHvCoKkCwYZWsWrAOuodtnL7KmjAYp2wMKVOa5xuK89MHgxcZz76IOWYzEr6SJ5OwWB1ul0oOlyOtFbwgxVKEjUH7LaYsDR9mBtlMdaaXv1eYitb_aQ4xuG_-cjJtI_q2vifTC1RX14S1zH4_XIJQRgd1BVFW7Pdymqu4eIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صمدزاده پژوهشگر امنیتی در برنامه وضعیت مدعی شد: یکی از افتخارات جمهوری اسلامی تأمین سلاح برای حشدالشعبی است؛ کارخانه‌های مهمات ایران در سال‌های ۲۰۱۴ تا ۲۰۱۶ سه شیفت برای تأمین مهمات گروه‌های مقاومت مشغول فعالیت بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/658949" target="_blank">📅 12:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658948">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1817a704a9.mp4?token=GYYzglVGyx1KbtJaRe-BwhmZd42fMOos6B81VItbaCNDTek0-aEZBpy3rfBE8Uo9cDB0Zrc8qmWzZP2VvSPxeG1XlqGvoadsAk0EDpX_6HOq_w4AmftcZg7_E2zR7RAciwI3agNb5Pfrh4y3B5sXt6qqUF7ERS2SVk-tSArz9x2N7zBD01Sai5qDiOX2WB9WzYXQqgOQa0pCEXBsRl54tNnfIj0ej6UdNj-s0AEQ08l9DZEUOSRSynK8OIZ4dCJjdutuvVhiMnJS2H0bSPdpfqE4rnQVksF5SlyH7obJwJ0LhUd22e13iwSe4Sri-B5zbKNLs9eDfv04jhUuzo1d2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1817a704a9.mp4?token=GYYzglVGyx1KbtJaRe-BwhmZd42fMOos6B81VItbaCNDTek0-aEZBpy3rfBE8Uo9cDB0Zrc8qmWzZP2VvSPxeG1XlqGvoadsAk0EDpX_6HOq_w4AmftcZg7_E2zR7RAciwI3agNb5Pfrh4y3B5sXt6qqUF7ERS2SVk-tSArz9x2N7zBD01Sai5qDiOX2WB9WzYXQqgOQa0pCEXBsRl54tNnfIj0ej6UdNj-s0AEQ08l9DZEUOSRSynK8OIZ4dCJjdutuvVhiMnJS2H0bSPdpfqE4rnQVksF5SlyH7obJwJ0LhUd22e13iwSe4Sri-B5zbKNLs9eDfv04jhUuzo1d2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مستربیست نخستین فرد تاریخ شد که از ۵۰۰ میلیون سابسکرایبر در یوتیوب عبور کرد
🔹
جیمی دونالدسون، معروف به MrBeast، در سال ۲۰۲۴ پربازدیدترین کانال یوتیوب شد، با ویدیوهای عظیم و چالش‌های پرهزینه‌ای مانند «Squid Game in Real Life» به شهرت جهانی رسیده و اکنون رکوردی تاریخی را ثبت کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/658948" target="_blank">📅 12:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658943">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hUP94-fVMRACZK5U980HTc-X0auONeMOSB6DihrL5v4JVz1Z_3efBo39Dy1_AkKWnL5L1UyuuPEPa0msY8azy91JDTY_EzwRmb0tPKSpSGMPLOvBgjb16om8BeoglnH28bB_MhwH2rYh4_C_j970uhSLzi7ZIDRFKOgXIl_ENAd0-9hQVNbOPkdTNKsf2E1lfKN2RkkJKrOvNbQETjjfsUeFBbrfuEOzjqjCqdktE1X6L1Z009BRiNsgUFdBryExEp9UhmtwOFAEiKBDSZ0Se1p_Ox82RuOwhj_jddMXrWkLzzIjFwBNgENRuRm83wrNkWMvNhmTYM47A4fwYCfnwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZyS18T4PGJEw2TGLQNErU6SgZcTEeUpiGCI12_7-HvFnw2i9K8wqIv3YjACuOkAL6Ps_JDFuIM41f_NboAWzrGS-Q-xn6CDx5TReaQVM7nX1o2zd5irV8jcZWVfRVpjxxplLIOm9-oOt-GAn7UaL3LuPi5nobvuzSdi8TZoQ2QKiVeu1p4H5Wqh0fF8eg3O7lDE8dBx5f1FvaaDYdprspte284jxfu6g_LmT1xOer4c7rqPF6SrajcJJjtyQhMBSaXFnhaRp0-qJ7XrEyMKIsuUf2E8EUXoXogA-szP3wozK5wJL039qyO1zFU-ryHW_PfwZj5ADQMeuI8170FIWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oRP5XBG2ybgAmD5owlNqy2bRRJRZbR0WPjL3Xx3pNbGU6DI1PRWZcgNwDxrZ8RTv_JYl51lihSB8p59YOaocCkcNOKWveb-bno7lw-tcN1tUUrJfsryvmxQTPbbekNq5GetMJNV7CTiDLlhjCzE1hnT6hV5WCqotg-fKkAnyJ9DHCchxn3rqjADJRMHVNj1EoKnhoir6G4IKYJx_xjq9qxVjWdX2GRYs4nFoFL0oPyVJRkrSuASfByd2uCmrDM-sakmiZSZ5aWWUC-JhKo-GbgBSspxag4EWlbBEpvHwrfXQw9efDo-fLW5oa65mow2AoaXEQA4JFbhDRNf437Bfjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AIaHz54JuuCldg_moJJP46RLi8uJXeBroVFS9_xSaUsOTHjvYuilIUrNmveqyHfb4pUZj64T6Jja18MMjNdCSxixj4RlyXRw21Ze52XFTFxxjAX26JkTse-N80534rCWxcYhRb1OF2KZ6XFstzSb0vU_xFzDuF2Ax8Rq5ziWHoIT2onKMmp3cxXTcBzL8uyiqewa8af1VMxQZjpFq_VoqsUzRkJl7mHUXJYtcwVEecqihP9tvonQEnfdxJeC2Kef_oDtDncE7RioRr1quiJ4o4BlQH-0eQumZ7yhzKNA1ABaNfzAea05AHVU_gq9BWNZYwQhcaBtA9Lf09osbQ2RrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPKWVUzq8stZ68Ul2BOib4-Z2Gd67a0khG4qrgn_uXILyJ1iBrobbZXwQWxjgRbdluOrcur9wfjOmUd2NaPj6mbfvTJ7nK_2c4DU5CcDb2OZNGHepoI3DsN-cj1IpqscUJk7zMHe2tViOWsAnE1ff29I9oASTry6FAUcJCHzasDYs7r6PHzN04xmBfyO--nKIsMRY4eH0aXI0ZI09hgbGzC3PHfSRd3Ppc5_OHZe_AV9tGqA4wIj6s-To96kueh1SOmz3qMBIhZR_5cyMGHTNoa6-BMa66pOZbTs42lYi85MTzoYLdcag1-54I4A7QNSEirPGK4SraPNvk4XnBXMxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر VARبود، قهرمان عوض می‌شد؟
/ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/658943" target="_blank">📅 12:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658942">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iarcLNUG651-UQ6bzOLaiUE3HjIY1KU18eVdQehGP_D-2b2w207ibtFsh0lKD31xiQkAnXNrPZ2EHnbmzge6HiXYLe6wsTf4WHpd6Uqab0ge20plK-sDuIqAhEzGWzyeFPQv7_Ys7Ag5jvvcupjSP-YorRlc7nWE4Wr5_C3O2xW1Og7uohXne6tzuKbHDiI1tHxYdd-Ygcnv3FB0zufbdli_cyPFjSLf-_V8LVCRGqKxD-o2ZeAzM-McCa6162hR_zRUtYC7niYk3HwnBFJxczMLTq-armu7tMgctKVspnXLaRikZjMNpNwXUOFdsDONrt-zMzXxryvOL2pX_sLg1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
اپل قابلیت جدیدی با نام «Drawing» را به iMessage اضافه کرده است
🔹
از این پس کاربران می‌توانند مستقیماً در محیط چت نقاشی بکشند، طرح‌های دست‌ساز خود را ایجاد کنند و آن‌ها را برای دیگران ارسال کنند. این قابلیت راهی خلاقانه و سرگرم‌کننده برای برقراری ارتباط در پیام‌ها فراهم می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/658942" target="_blank">📅 12:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658941">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5ul3F-O1pF0nmSN4nyalKiIJq1074tmXQ0sMUEdvL4K9uu9tEQZH6wnDGNfGp6Vl9_A00FbLDZln7YyEv7jrp6MePnGYPjEtS53XjPNy8Zv_SZZfLDy1MCLzTQ869LNkUd7w_xNx32bF4VNhe7XttT-CcLGIj39MRPUDle8boDxhc88BTRqsR8ouLGxoTGNi7kEOAJmRrnZ9kAI3mBQq4T6M7Zi9queT5sHuCl2eGdejY0EQ5he9rlqJr0em4gMK4iCquONMLAG5goMhq9nGp3W5HMToP1cqURFzvY1d81e0hMIbP5yotjE3ZGl7OxN3XNqmjP0F9uwMD0usOozqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
سلبریتی آمریکایی پرچم ایران را به اهتزار درآورد
🔹
«جکسون هینکل» اینفلوئنسر معروف آمریکایی امروز در تمرین تیم ملی فوتبال ایران در تیخوانا، مکزیک حضور پیدا کرد و حمایت خود را از شاگردان قلعه‌نویی در جام جهانی اعلام کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/658941" target="_blank">📅 11:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658935">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خشخاش به کمبود خورد؛ شقایق الیفرا بکارید!
حسین عبدلی، عضو کمیسیون بهداشت در
#گفتگو
با خبرفوری:
🔹
تولید قرص کدئین به دلیل مصرف بی‌رویه، قاچاق مواد کدئین‌دار و کاهش ساخت داروهای آلکالوئید دار در ایران، به علت کاهش کشفیات کمتر شده است.
🔹
میزان کشفیات خشخاش یک‌پنجم شده و میزان کشت در افغانستان بسیار کم شده و به‌جای کشت خشخاش می‌توان به شقایق الیفرا اشاره کرد که قابلیت جداسازی مواد مورفینی و سوء‌استفاده را ندارد و در کارگاه‌ها قابل جداسازی است.
🔹
تمام داروهای ایران، قابلیت قاچاق به همه کشورهای اطراف مثل عراق و افغانستان را دارند و داروهای ایرانی در آن‌جا ارزان هستند و آمپول‌های تزریقی که در بیمارستان‌ها استفاده می‌شود نیز کم شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/658935" target="_blank">📅 11:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658934">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40415b230d.mp4?token=DfyON8kgXOYmHVqybtrJF-p6zDd7UpF_iRCfi2nO0zIZXUj52CUJi7wQUTeyLGQGI5EPxworR8Ov9yCc9Hm4tGsDn6HLsr1BtGhShENP1ELkm7dUAr5p_yNtz_FMq6te-s0jr3n0Gd5QLrSoCx3Bzt5dAWsWeH1TO7jLf4M8AX-IfhBUDn43eRIJw8Ch5AMrfB2ht--4J53ot6FGXphk5KxWLWbv6pCUfgy3Lf6SIV8abbk3_ytpUdKBLzO_daS5ipw1XoUX-LYhQMGeSe52bRN56MuqX6gOllwiqreVj4Z8W37sgBhdwBQTlJW3R0r7EcBdexPyylIw7BdmnLVQQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40415b230d.mp4?token=DfyON8kgXOYmHVqybtrJF-p6zDd7UpF_iRCfi2nO0zIZXUj52CUJi7wQUTeyLGQGI5EPxworR8Ov9yCc9Hm4tGsDn6HLsr1BtGhShENP1ELkm7dUAr5p_yNtz_FMq6te-s0jr3n0Gd5QLrSoCx3Bzt5dAWsWeH1TO7jLf4M8AX-IfhBUDn43eRIJw8Ch5AMrfB2ht--4J53ot6FGXphk5KxWLWbv6pCUfgy3Lf6SIV8abbk3_ytpUdKBLzO_daS5ipw1XoUX-LYhQMGeSe52bRN56MuqX6gOllwiqreVj4Z8W37sgBhdwBQTlJW3R0r7EcBdexPyylIw7BdmnLVQQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرقت عجیب موبایل در یک اتوبان پایتخت
🔹
فردی پیاده در وسط اتوبان حکیم تهران موبایل یک راننده خودروی در حال حرکت را دزدید.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/658934" target="_blank">📅 11:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658933">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f507d88efd.mp4?token=bz6GcR89fnlcv0JxPZdu0ziCzvh8XYKbzh9yMbVgqHlklsWmApnWRiISNygyOWXJ5uII61KAMKqz9KHVQ_rVjlxew9A1bsMlM3EJ6bWsqP-0lNq_pz7w-Pwf5y2eQ5Fcj_pNd_SaE8WpmLLhTPk5tjatFhJHEky2zzM_AjK6fF5I9wIcA6ZMDgsahhGb6btsrymdnKcZ8U4tjiAppqYZBGr6ASxseH9gMR3xMpPEvnuO77hbTWn-64OkwHT7uHH8Aq0c37Njpl510QhihMRV222KJOSoinl2xJOxM3DyWatPIE-DvcgvrGJ8I9WH-rzB4Jb355ELhxMh2NRa8JR4yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f507d88efd.mp4?token=bz6GcR89fnlcv0JxPZdu0ziCzvh8XYKbzh9yMbVgqHlklsWmApnWRiISNygyOWXJ5uII61KAMKqz9KHVQ_rVjlxew9A1bsMlM3EJ6bWsqP-0lNq_pz7w-Pwf5y2eQ5Fcj_pNd_SaE8WpmLLhTPk5tjatFhJHEky2zzM_AjK6fF5I9wIcA6ZMDgsahhGb6btsrymdnKcZ8U4tjiAppqYZBGr6ASxseH9gMR3xMpPEvnuO77hbTWn-64OkwHT7uHH8Aq0c37Njpl510QhihMRV222KJOSoinl2xJOxM3DyWatPIE-DvcgvrGJ8I9WH-rzB4Jb355ELhxMh2NRa8JR4yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قهرمانان جام جهانی فوتبال ۲۰۲۶ دانش آموزان مدرسه میناب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/658933" target="_blank">📅 11:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658932">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b84ce7570.mp4?token=Lc8yfC6-X0BpZ61aVrMEbKeea-Cy7rSOfwvwLHiioxYZxM3RsCgOOJihZReFH7dT-iNKiH30mFCsA-nnRHzzfFvxBA_9foNGxPP8Gw1ZL1eFPR3Fng0O3C8u_wYJSVVZb4kE7iwMDzB_bkkzQvytHY84VcjM7ttCCeYCxsJnt3m9Xs8EpPEVbL37JdAu_ax4VQCZ6wtGqAGxqN51I69YWVXERI0Gxryf4WNbpagc51EgOrctmVDEM3kW7u0HlTC7vahscgCZQClpiteOxjN9NzUe0FITxmcCjIEv59iBOY8Hw4MYjv2uFJm2I0Yp7Em7gGX6cU3MY1CJf5_dJdlY3E7YfPSsVuA1htH5MtgmL_WZ-blvUrEuTdEd2HIuYvhBAOTgL_4pJbzQjowOVtBpqOIFR3HPDItX3NGBHA_WclaIpUBEkCBh_K7CjYdXs5YzKsOCrO_Vq2wTCY1sDaedX_n1YWJathko81XPE2H6p6Ty5PlWVBru5pcb1QDo32u4gHqO4N-ZqMvJQ-33OKtNUgIuDBJTLdkj7yuf_SNqN3J2GbU71aDTCJkYZn8zKyfGXIBv1Hu8GH99spJqxEUU1q2nSQPvJB2885dCvY9MIM92j-iQBz9aujKJ6PpXJCtvZmNX69lby_Z6DMLL1dDp5wzOw3W-niCeVeLHdCPMSaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b84ce7570.mp4?token=Lc8yfC6-X0BpZ61aVrMEbKeea-Cy7rSOfwvwLHiioxYZxM3RsCgOOJihZReFH7dT-iNKiH30mFCsA-nnRHzzfFvxBA_9foNGxPP8Gw1ZL1eFPR3Fng0O3C8u_wYJSVVZb4kE7iwMDzB_bkkzQvytHY84VcjM7ttCCeYCxsJnt3m9Xs8EpPEVbL37JdAu_ax4VQCZ6wtGqAGxqN51I69YWVXERI0Gxryf4WNbpagc51EgOrctmVDEM3kW7u0HlTC7vahscgCZQClpiteOxjN9NzUe0FITxmcCjIEv59iBOY8Hw4MYjv2uFJm2I0Yp7Em7gGX6cU3MY1CJf5_dJdlY3E7YfPSsVuA1htH5MtgmL_WZ-blvUrEuTdEd2HIuYvhBAOTgL_4pJbzQjowOVtBpqOIFR3HPDItX3NGBHA_WclaIpUBEkCBh_K7CjYdXs5YzKsOCrO_Vq2wTCY1sDaedX_n1YWJathko81XPE2H6p6Ty5PlWVBru5pcb1QDo32u4gHqO4N-ZqMvJQ-33OKtNUgIuDBJTLdkj7yuf_SNqN3J2GbU71aDTCJkYZn8zKyfGXIBv1Hu8GH99spJqxEUU1q2nSQPvJB2885dCvY9MIM92j-iQBz9aujKJ6PpXJCtvZmNX69lby_Z6DMLL1dDp5wzOw3W-niCeVeLHdCPMSaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تب فوتبال با جام جهانی/ از برد قاطع آمریکا تا اولین امتیاز تاریخ کانادا!
🔹
طرح
طلای
بیمه زندگی
پارسیان
▪️
آینده‌ای طلایی با سود طلایی
▪️
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/658932" target="_blank">📅 11:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658930">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed82a8cdb.mp4?token=FKje7jrOkuv7QVbiJOY2MF7L9tKf9LKK5nZEpaCDSpzOfNWXrFLTirw6Y-2Jo6LEqk-ZhDb1lfpZKK8xoZnZpX4s7qD4WaU5RDc-fwNrT1GJDVyTZ65aWGnrR7zNdRFJIFoWMxvwlLiD_9GU_hwfNMlH9TLcbIKD_UoCBJQFzIho-YPf9_iGIJqvU1H_MeSDcllQJEvwadn4aZR5nz5C9GowsdhdTMrZJlarOCVnFHLy36eT-LorM_i5zzTo9Tnh4j5gij2tJOr-92-SLO4OB4-reIOhUg4SgmhmLlxZaWDXCp-UQpioQwaRC5xX6nFZpEBTQBlPCqv1D80u1XSQrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed82a8cdb.mp4?token=FKje7jrOkuv7QVbiJOY2MF7L9tKf9LKK5nZEpaCDSpzOfNWXrFLTirw6Y-2Jo6LEqk-ZhDb1lfpZKK8xoZnZpX4s7qD4WaU5RDc-fwNrT1GJDVyTZ65aWGnrR7zNdRFJIFoWMxvwlLiD_9GU_hwfNMlH9TLcbIKD_UoCBJQFzIho-YPf9_iGIJqvU1H_MeSDcllQJEvwadn4aZR5nz5C9GowsdhdTMrZJlarOCVnFHLy36eT-LorM_i5zzTo9Tnh4j5gij2tJOr-92-SLO4OB4-reIOhUg4SgmhmLlxZaWDXCp-UQpioQwaRC5xX6nFZpEBTQBlPCqv1D80u1XSQrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریس رونالدو و یارانش در آمریکا
🔹
تیم ملی پرتغال وارد خاک آمریکا شد. #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/658930" target="_blank">📅 11:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658929">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWFppUqSQlNDtIXuPomFT05BX6X4TEoXT1qLTm7qN_O1mcqnSoOc9nI9XKGgb6gA0GO3ZdQe-sD9L7LxOLjXszFpf_1tZAQ5fOUL0CLz2guXRYXTud-4wW7ZY9fo5EJMywuPMsg9NoPHx5ZwNJc9Jf_3vkU3sKgJgisN2uVqvR51kkkBJgvguLkIG_G67aAI5IZu_Fbkqz-USuCieOfVMlaTSx7eTm8feYjPh4nw2vKd5vEYIfutddd47KfqOn60zTh42U4vAdPf2xD6D8isqBpcU8AZJl6efzgYC8rwT7Ogsif4Q6m3eTK7CzPVUMTZmVct1Bjp5MwHgPtPC11UzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بعد از کارت بازی داور برزیلی در افتتاحیه جام جهانی، این تصویر عجیب هم ثبت شد!
🔹
البته جدا از خشونت جام ۲۳ تا الان، کیفیت لباس‌ها زیر سوال رفت و ضربه اقتصادی عجیبی هم به کمپانی «پوما» وارد خواهد شد! #جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/658929" target="_blank">📅 11:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658928">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odHtLbIbN0uAH83TOFe7mOsYJy89aa6MLZ7jjlYtiM8fyinGh8VgAwygmdgwaH_6pC0PjPjEKI6eHDpcjMm_5QVXmoRUJIiM-1qo815jGDx5eEZD8Gs9fw7Yhq0kZj_7efMBGdBxvMUhU7RrsNs3BnUtKd1t61YM9Ppa9kDkxXUCShdY1KjX890Amm7BNIUsuv2Rpl-cq7-JJuRx5gFRZyshe7lfbV2GWruyHdWe8tXP6JhqDyzJRnA0PtnoqhDToUaMTfaVml1zvg2jAAIJDepfdxPY_WcIjRZTpb7yElylCk68o_pNJ2aRZHSrhr-ibHXYpz0VSMGEDZslcJ6bhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات ادعایی فاکس‌نیوز از توافق مدنظر ترامپ با ایران
ادعای فاکس‌نیوز:
🔹
طرح پیشنهادی دونالد ترامپ، شامل پنج بند کلیدی است:
۱. نابودی و حذف کامل مواد هسته‌ای ایران
۲. برچیده شدن برنامه هسته‌ای
۳. عدم آزادسازی هیچ دارایی ایران پیش از اجرای کامل تعهدات
۴. بازگشایی تنگه هرمز
۵. توقف تأمین مالی گروه‌های نیابتی از سوی ایران
🔹
این ادعا در حالی منتشر می‌شود که هنوز واکنش رسمی از سوی مقامات ایرانی به این مفاد اعلام نشده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/658928" target="_blank">📅 11:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658927">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Deo9W7AUg8Q3ws-6AmK_kxlcup08m2JQihmDmnAfqWouiN6vVJp_KFX8nu5n_LJbTOOcvpSYBH_dOkOuRnSKbzWyP7A40_I_MX6G_E0HGlePICQxSOK3bMCfanZTXXY6MW18-sRt6x7SQT_uYQjgakF_JP0oSoOvVgkaw8oIaxmhygpn9GxQ1FKh1TMrXXsqSQhg48EfwDVobXOqbb41PlUIP6fCG6Wqa8Dwmg65wfSvhey--dkyIqOfkz1JqW5EF76R0Piwf2iME4SlEHPvrip_-u9a-W6XtaEkiYtkXB-UVYXCt7U-cdDfRSKVSps2uXihFkddDGRCvNtXaIw00Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از بلندکردن شتر ۲۰۰ کیلویی در ترکستان قزاقستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/658927" target="_blank">📅 11:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658926">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
شرکت توانیر:
برق مشترکان اداری، تجاری و خانگی پرمصرف بدون تشریفات قطع می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/658926" target="_blank">📅 11:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658925">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHBCzcKIoH-GKmZ2HySEhP-NQstwb7IKDY9Af9ZnWLJdmK6hdjd8iOv_JgmnQ1ax-6F7QszoqyRqJNlgZAaB0bmqUdgm9F6cxcIUeMw_exq6hyEMeAYIlllZn8Hjf5JJvCaNy9mTb0YFTC8KLHBj74PRtxCDs9Uj8eq5LEGOhk-ZVQTvi-bTu0jFllr40Jt0NoEjWXL74n0Hhr43Pq1YEwbHS_37NDdbnFW6mgLUpoidoI5aghq9lyH3F56UP1iyAUnuUnhaohWwvgW0jYnTiyebbw4i6TyBKqjq__qie-_AJEQ7zARSVeINSpzLH4UVpNaz2PMQ_qamoaus1MMJ3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سبز ۱۰۰ درصدی؛ طوفان بی‌سابقه در بورس تهران!
🔹
آخرین هفته خرداد در بورس، با یک انفجار خرید آغاز شد.
🔹
پیش‌گشایش بورس تهران با صفوف خرید بیش از ۵۰ همتی رکورد زد. نیمه اول معاملات تمام شد و بازار کاملا سبزپوش است.
🔹
خریداران در ۸۱۴ نماد، صفوفی ۴۸ همتی به جای گذاشته‌اند.
🔹
شاخص کل ۲.۶٪ رشد کرد و به ارتفاع تاریخی ۴ میلیون و ۷۱۲ هزار واحد رسید.
🔹
ورود ۳.۶ همت نقدینگی حقیقی‌ها، ارزش معاملات خرد ۶.۳ همتی و خروج ۳.۷ همت از صندوقهای درآمد ثابت همه در نیمه اول امروز بورس رقم خورد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/658925" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658924">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWQeOnFGODsfa9oirw-qlrk8OYdExl1PXgaAqkzVAHLZfESDOrXIjN97ANb4_lT_dR9mrNHROA9qRZ3_3mU54GRnzfp1KTr-R3reUZCaqtvioJvm1FDILeri_aiLBEcs9k1q_IR7zxWjXXrgI60Y2UzMZQVx_j-PG4RUn_hEhzdk1F0LZW7BS5Di2LsHMn-7VxWjBti7wV_6jmId_hyqh99rQyJWo-1YFZDWFNYv-IDbNxkz-B4F-lS2RjTEGLNOT4zhRhj7Ug6m3QzZyCyKF1qOzVn4nSuJeUsS92ZnXhXg9aQ4gLIuVXLGs8ftY9ByVleYnXBt4GkTbrllWX5itA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا ترامپ امضای توافق با ایران را به معاونش ونس واگذار کرده و خودش پای مسابقه یو اف سی می‌نشیند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/658924" target="_blank">📅 11:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658922">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nad_qrnx1nK82VZSTa12SYsSi5SBxT8qcFBX6Fm0jBgGTkrALyXFsPIrPx4i8E_NfqO2uGtSJUb117QSjsjeX897107Tve7fT44zM7q3O1Cr9q1tId2NpMW87wKtlylveu3MXc4aH3GspyVCW_R5Xwt8QkrTOdYt-t0k3vfLAV58kJLXRudhfyLnpv2G0bghFy7ueq7SD0sI49Qk4FmEkh1Gh7ugM4hYq4dl-cbcCNWXaYP_UoRRorkQinjloCkukgwNi4x67adyM8doPLUyQE96jNIkb2mOHaLIfq2fq8YJD1qwFrXxZv-sY9-_yKJl_qO4YhJKzjrwx8NVOYq_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آینده از آن کسانی است که در «نقطه تصمیم» درست می‌اندیشند؛ جایی که یک انتخاب می‌تواند سازمان را تغییر دهد.
در رویداد تخصصی «نقطه تصمیم» جمعی از مدیران و کارآفرینان برجسته حوزه فناوری و اقتصاد دیجیتال، از تجربه‌های واقعی خود در مواجهه با بحران‌ها، تصمیم‌های دشوار و فرصت‌های پنهان بازار سخن خواهند گفت.
اگر به دنبال شنیدن تجربه مدیرانی هستید که در خط مقدم تصمیم‌گیری قرار داشته‌اند، این رویداد را از دست ندهید.
یکشنبه ۲۴ خردادماه ۱۴۰۵- ساعت ۱۶ – مشهد، هتل نوین پلاس
https://evand.com/events/نقطه-تصمیم-015774</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/658922" target="_blank">📅 11:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658919">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21a7ca6c94.mp4?token=ATIcLYakITgpXZjr7qaGr_0300dge-vT_XFXlOsRqp1hBRuBfwMluGHlgmmYTl7zkhhKU5uJwfFGdsA6iLTMliC0E1FK7R51cF5b58ssscgUxEy8pD8tZUr5tnY8ovDNND13E9-q4WWM2qcX8E_DuX6dcpUGKVu9qO_hEW6X2ibM1lARjsBmGQw7zQNYeYPh7yZ1L35Kj93eN04jEpjVSnEPi6i6e_mO-qmV9lXOtJsAuk3MRtaTSBiE3xYs9e3T5V3nv607FExYoPGC7qgzCHNLTyRBq4uXeuyJaw_8X94RQfwsVfXAM5iua3gDnaFtlqa98-yZpwK9S21mAXiMjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21a7ca6c94.mp4?token=ATIcLYakITgpXZjr7qaGr_0300dge-vT_XFXlOsRqp1hBRuBfwMluGHlgmmYTl7zkhhKU5uJwfFGdsA6iLTMliC0E1FK7R51cF5b58ssscgUxEy8pD8tZUr5tnY8ovDNND13E9-q4WWM2qcX8E_DuX6dcpUGKVu9qO_hEW6X2ibM1lARjsBmGQw7zQNYeYPh7yZ1L35Kj93eN04jEpjVSnEPi6i6e_mO-qmV9lXOtJsAuk3MRtaTSBiE3xYs9e3T5V3nv607FExYoPGC7qgzCHNLTyRBq4uXeuyJaw_8X94RQfwsVfXAM5iua3gDnaFtlqa98-yZpwK9S21mAXiMjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متفاوت‌ترین هوادار روز اول رقابت‌های جام ۲۰۲۶
🔹
پس از پیروزی مکزیک مقابل آفریقای جنوبی، یک اردک با پیراهن این تیم در حال راه رفتن بین هواداران دیده شد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/658919" target="_blank">📅 10:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658917">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQOVi2jgUmfKNHw7GkeQUucI7Lx9oDCWXS41ND2D-9Hs-S2Rhy850V5IU7IHcXetWiMx9dgGYvrxSLziY3u5_BtO1aA0H00zhEqMOaIjHhztk1YJpNpWgcpmDO-WIZswlArkKSi_zoB4s6T_fho6Y8ZYlgr3xo3RsNAtsyfa7XjuFURtO40bWgzpM5kGylPO1jZKAn-0TR5e7ge5lHpuJCxgzCszYZlglwQxMb5JHQTvzNDEHwVFVTXrcv707Okup7d-QnSZBWnepbR60PJ3vScflohW1AjZKYhcVxOxY4i7und-X-qWchBMPNcUY2jy733UglIMXC1MjBItvHWyQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴ مدل سالاد خوشمزه که وزنت رو هم متعادل می‌کنه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/658917" target="_blank">📅 10:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658916">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
فروش اینترنتی دارو غیرقانونی است/ با متخلفان برخورد قاطع می‌شود
سرپرست دفتر بازرسی سازمان غذا و دارو:
🔹
تاکنون به هیچ پلتفرم یا وب‌سایت عمومی مجوز فروش آنلاین دارو داده نشده است.
🔹
هرگونه عرضه دارو و مکمل در فضای مجازی خارج از زنجیره رسمی داروخانه‌ها، قاچاق محسوب می‌شود./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/658916" target="_blank">📅 10:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658915">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7746c19bf5.mp4?token=ple3yIOFJ8D3cMbXecwVa_-ktiX7DUBFY3yWEfGwYfoIe8i7Nx85FHDZfXnC9rbHWHhKLsSIWF_A5RHM9HygJ0rsNKgndTdgR03dXfo5xyMf5tHGUtD7idQsjuiNKkNbLSMSru0Gq34bD4cx1qpp8pa2baA9LOdkTmSNzOEFz9RnV06sCNDyI0iaUywlIOjycV8Z2EowwW8H6H8m5lOLFNpNXqfBfn-WChWDl01XcQiB_bzbjq9uZbZP8JVJuGH3HYe-x4rn2w6dskqDvgV6H8XjdovU-aX9Yh3Y2hLx18gLVX8qq7xtLltYhh-P4C8ndDols_bM5Di-4eZEOBWTgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7746c19bf5.mp4?token=ple3yIOFJ8D3cMbXecwVa_-ktiX7DUBFY3yWEfGwYfoIe8i7Nx85FHDZfXnC9rbHWHhKLsSIWF_A5RHM9HygJ0rsNKgndTdgR03dXfo5xyMf5tHGUtD7idQsjuiNKkNbLSMSru0Gq34bD4cx1qpp8pa2baA9LOdkTmSNzOEFz9RnV06sCNDyI0iaUywlIOjycV8Z2EowwW8H6H8m5lOLFNpNXqfBfn-WChWDl01XcQiB_bzbjq9uZbZP8JVJuGH3HYe-x4rn2w6dskqDvgV6H8XjdovU-aX9Yh3Y2hLx18gLVX8qq7xtLltYhh-P4C8ndDols_bM5Di-4eZEOBWTgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اهتزاز پرچم ایران در قلب لس‌آنجلس
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/658915" target="_blank">📅 10:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658914">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان درباره تله‌‌گذاری ایران برای حفاظت از ذخایر اورانیوم
سی‌ان‌ان:
🔹
ایران در هفته‌های اخیر به شکل چشمگیری تلاش‌هایش برای مسدود کردن دسترسی به ذخایر اورانیوم غنای بالای خود را افزایش داده، از جمله با فروریختن عمدی تونل‌ها و تله‌گذاری ورودی‌ها با مین‌های انفجاری.
🔹
دسترسی به حدود نیم تن اورانیوم با غنای بالای ایران اکنون بسیار دشوارتر، خطرناک‌تر و زمان‌برتر از یک ماه پیش شده است؛ زمانی که ترامپ علناً احتمال عملیات برای تصرف این مواد را مطرح می‌کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/658914" target="_blank">📅 10:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658910">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZgG-EutC0Wd_9r43V1X522HrUrvPD6Dn6ciD0xEaCeuPyAFuuxamXQgx5SZ6IP5jGhEo8xyRVXVE4gkbMDJt3l8qvof7an0Xj_CywSlWBBk2MlK52_FGw2voZ3vcCeMP4RkRfokzmaq8zsO8B-7aiqgWjbFNoY44bgqYTF3T5Es6vVj9AvBuEobCGSSUPz4_P9LC3UTnbA5nSm28CRYasgSkl4C5A4cRH-504HNlITag5lmIgzc22EszKq-amSYX1RQ8j9gprhLQ8JETClCZokwJpX_zBFcWa8P0T2_hCIAERFdhktuuUc_x1kg9ROmwRMQ8K97xH61jQN8sJm-Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L0qcnLs75kP4M018zhr3elxbXIl4K2A7HdcuejLKzOZMjpE4KAU6nZc2hkAgGB7gwal-6K5P8BkSN005ytjAzrnoOtV2DINekgXMYYY1Nryjee3xfwZtqr9ZU1-P48XqlKbXNU-nci2n5Yk0yynKm_QbYXMuCcbWAGpQdbOGvSrmdkFm4znt8o3LAdhXR0Lfr2hD6a3eWFTzzqi9PAOc2Pe5I-W8y7roZokaG8pD4psWVmYqmw7Fw0DACr5U3R62UBrt42geF6oG8Qq4NeiJoZl5lXqI1EkOMIunuOVU2rPtIa0obL3Eq6pttFYg2vHe7l-MyRE_G2qbvtffK-XJPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sieg7m12HIxaAPLYlc3csqY6romn5LHxmyvTpCxYf7ikio-bbQORhJAU5R5z2uYqYg04ROeQWgR-A2iYZCgByGhIaI0OKI4mLRbyQLN0GcNLxBuRCT2PrVYCdScCET2kfdTEsKp3nLCdiKTd0SiuHOaUE01v6HOg2WQ-WSsBzuFdUG7FZi0x7ZqmKg406k4HEYrhNEyxc4mw0PPo1pzPLGDOO0DrYmTzA9Iwx2goeihuXOJjmNW-FgIBBWn22cGJjYykZmx5MSh56janMIoK-My5mMNxmS4yniiFBVqJYrZRvgTBb5v5VFBO3jRbNimj4aBE9b3-GTutzFUWMwVv7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OrIHhAKdS-I9f3bNfeRcQDjDGahUyL9ceWLPglUGQW-IXrxNakrwLc1oZhEnWGMbhBCOekFmqadyobiC-0cqA679qwFse4wCTQ0uAkU7SLG2hETdn3R42b5Atcw1FWB9wPDHsG9QPEXigaGB0UimRaMMyF_kco4hUzMFm5lQcSv7vpcdUtS_LoYNKDcHCSh31QuvVSFbPKDa0JihSMxqNdugRH4-LcMPY13hyCZ-UeogodglzZtczeUr-x_rI-61FJP4E-ope-OUibyj7B_LwuBW56ICLKbywyXNXEJPFxzzBIxv09LRPWf9RZMGGcyX8lqKHL1BNToSN5CVQuQA1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری دیدنی از لحظه وقوع صاعقه در اسفراین
#اخبار_خراسان_شمالی
در فضای مجازی
👇
@akhbarkhorasanshomali</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/658910" target="_blank">📅 10:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658908">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b667de7ddc.mp4?token=VTG6voryPCegh6GCQ5zzCdRt-pCddBKCcK1x8b0iVMXQR_mKKrO6qVqg9dUhvcNx6mLpsgINri4sejV8wWETQa9OI74WV-wr19R9MM40um1VeUrKuPIUyke04Ox1jh-Ki2oFGC9m8-krsHsYNC_Bkl4YS56WOJqWWwJ5z_7fl748WI68Obo8_li9BmIuZveXvgYviIgZ4wV8MPO5tc1kvsV-AK_NFXVOUNHTlfnrQb8xuDJ87j7OTclMyYe0P-F2Ly84DhsWaasCVYweiBA8iCEtJCwVsmGEs1TxN3RHQYF-xMRhEgNcStO55-F1EsN-dU5h8gv4adBwCDB7wpZhGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b667de7ddc.mp4?token=VTG6voryPCegh6GCQ5zzCdRt-pCddBKCcK1x8b0iVMXQR_mKKrO6qVqg9dUhvcNx6mLpsgINri4sejV8wWETQa9OI74WV-wr19R9MM40um1VeUrKuPIUyke04Ox1jh-Ki2oFGC9m8-krsHsYNC_Bkl4YS56WOJqWWwJ5z_7fl748WI68Obo8_li9BmIuZveXvgYviIgZ4wV8MPO5tc1kvsV-AK_NFXVOUNHTlfnrQb8xuDJ87j7OTclMyYe0P-F2Ly84DhsWaasCVYweiBA8iCEtJCwVsmGEs1TxN3RHQYF-xMRhEgNcStO55-F1EsN-dU5h8gv4adBwCDB7wpZhGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر میخوای واقعا خودت رو شفا بدی، باید اول چهار نفر رو ببخشی
#سلامت_روان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/658908" target="_blank">📅 10:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658905">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a75dcaad.mp4?token=q9ZQjEYjhKSshSQ4fSukLCixUHjzuvIGxmtshbSyUt5oOZOm_M15sjuMgb6JWihBPB1DiIS5E-0pBDGE3WX-rpxbp2FFgJUKkdw8xa2LU6nk_n_3QobhxKP4IIlrqMhNuJDuKVsf6Y-xC6qgizVR_Ph8u9bmb2gcThRlKEcp-Hj_DTsR_45X9U7TsW5M34LJLy2w9vd-HcHopqy8OVkp-JUjavI6yLbnrkzpw13JBRwDD7_6DMNlB34ZofNsDMycCO1twHTozSbvRoR47pTOq6ARgzVMnudb9T-thgUByc4HTFaTpF1RdCJlbrns6ia7kDYkRijRtkPSWfvwr5PebTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a75dcaad.mp4?token=q9ZQjEYjhKSshSQ4fSukLCixUHjzuvIGxmtshbSyUt5oOZOm_M15sjuMgb6JWihBPB1DiIS5E-0pBDGE3WX-rpxbp2FFgJUKkdw8xa2LU6nk_n_3QobhxKP4IIlrqMhNuJDuKVsf6Y-xC6qgizVR_Ph8u9bmb2gcThRlKEcp-Hj_DTsR_45X9U7TsW5M34LJLy2w9vd-HcHopqy8OVkp-JUjavI6yLbnrkzpw13JBRwDD7_6DMNlB34ZofNsDMycCO1twHTozSbvRoR47pTOq6ARgzVMnudb9T-thgUByc4HTFaTpF1RdCJlbrns6ia7kDYkRijRtkPSWfvwr5PebTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حضور یک فیل، نماد حزب جمهوری‌خواه آمریکا، در کنوانسیون این حزب در ایالت تگزاس جنجالی شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/658905" target="_blank">📅 09:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658902">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c311e352e.mp4?token=BIVjKhjXzpt4riP62nKSA15CgVKohMjIvlia9Xt452lvVa6cDEKHQQ1kN86tgfyy4gIshqHbjfyN4YKTq7hNjYhpKORVmI8T168oSSy91m8IP2GO9t-eAwwJANxUfZtpQVBXJoRtcXcQmcXyNNc576TbtyJCmBEZmDJ5oPX-XD76RrvBkLaRGeJGcXLRSKuQV0SxsQEMlFw3ywJZt68ZdfrWgsfnid7ASLm6g2BoPX1j8-kh2-u4PIaNFMFGwFkhtqi15vw5edYcKIWYigz_OpAu1zBgo1PCMi8bJ93-B6hGOngSQSojVL-pQ1OF3xm8JGxPz8Nm8JqEd6zE86fq6Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c311e352e.mp4?token=BIVjKhjXzpt4riP62nKSA15CgVKohMjIvlia9Xt452lvVa6cDEKHQQ1kN86tgfyy4gIshqHbjfyN4YKTq7hNjYhpKORVmI8T168oSSy91m8IP2GO9t-eAwwJANxUfZtpQVBXJoRtcXcQmcXyNNc576TbtyJCmBEZmDJ5oPX-XD76RrvBkLaRGeJGcXLRSKuQV0SxsQEMlFw3ywJZt68ZdfrWgsfnid7ASLm6g2BoPX1j8-kh2-u4PIaNFMFGwFkhtqi15vw5edYcKIWYigz_OpAu1zBgo1PCMi8bJ93-B6hGOngSQSojVL-pQ1OF3xm8JGxPz8Nm8JqEd6zE86fq6Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی صحن‌های حرم حضرت عباس (ع) در آستانه محرم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/658902" target="_blank">📅 09:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658900">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
بازگشایی دانشگاه شریف از امروز
🔹
دانشگاه شریف از امروز به روی ۴۵۰۰ دانشجوی مقاطع تحصیلات تکمیلی باز شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/658900" target="_blank">📅 09:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658898">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb8rQV2v6_z91te-NbaOGAwbETL7RFSxtJ07joxmOMwr7hISNqf8CdUjcDtuxuqP0ErtjMtKAWRs3PqQdmfbvTEfzWDBLUFZA3iDnine4t1tjFXR9tDBCZFe1va9x1UGqLKCS_SJlD0CuQCP7CZUG7HhdvnAUM8oICz_tQOdpvGGzISEQWJabxt4GZxekdN1z8oW7YI56GDLaXo1JrWXHo6hGVHTIoQrm-OisxQh71_vU43KkcFaWPRNyzVmj3BrpQr2io3O2aYIcF1Na0_poBxulmKJBHkalKNGbHKVTgFzqHQYB6D7Rt1GqFGb7AdYjRIne82j1jiog4Uqn3f-zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشای جلسات محرمانه تیم ترامپ برای مهار بحران اپستین
🔹
روزنامه نیویورک تایمز در گزارشی اختصاصی فاش کرد که مقام‌های ارشد دولت ترامپ در ژوئیه سال گذشته چندین نشست محرمانه در اتاق وضعیت کاخ سفید برگزار کردند تا راهی برای کنترل بحران ناشی از پرونده جفری اپستین و تأثیر آن بر ریاست‌جمهوری ترامپ پیدا کنند.
🔹
این بحران پس از آن شدت گرفت که وزارت دادگستری و اف‌بی‌آی در یادداشتی مشترک اعلام کردند بررسی‌های آن‌ها هیچ فهرستی از مشتریان قدرتمند اپستین را پیدا نکرده است. این اقدام که قرار بود به سال‌ها گمانه‌زنی پایان دهد، با واکنش منفی بخش قابل توجهی از حامیان جنبش «ماگا» مواجه شد.
#جاسوس_موساد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/658898" target="_blank">📅 09:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658894">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUl-H9u3GBRSGv5BgGMVqPuq8LYLHixxehIuvjNdFta5cnKDqbaGIG2vNXTHnOpJbgB7LTweCmfJvMVTGqWukGm3cguDqfovPonr49LBjOn10ixOaU9iXH2rv5dJ75GDotuAAu7PTEgNunb9j7IGdF3nZLbm-_PZJKGLLp35xJKn7unlSSo-giLwZSbSr6dMJdimQhOYq5cxkBDwO-atS-ciR5rb8c8XL3cCvlwahnHM_2qPhyImDKJpttb8Ows6_tyF-MWF9kBkINcyluJT1w36jZsI9AURFTyEKW9rCIQxKtgUDx2_n8FyI24mXLSBe7girFl0we0BQmmdUcPvSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tgEcWR6NmsGe9J8Mi9-MSOOvNvsfSIArKbf6kuLt7BMv8NBjrXMZCTuqkAa9_lgH8DiPTKhX1XcBz5ReB1s2Vl2V7R575eCJ0Dtn36UElT4vGa1X87_rb30tC_5rnVWwyUPBxCZAbVo7WIBTVqOgAv4NEak3esBV2MzVFNMP89kYLO-wA6cqfx1Ng7f_yjaCwjAEuoU6Guos7DFB6qKz_hPpZgveyNuDF4bO376JxVq0PJHQzMfYZinCDFikI1OCig8DZZppW4NOg2hHkay6Tqa0X97DANDmslCgpJTzCn05NyFg-w-mhu_kYqw2dyCXoTWoSZrWTbFvmkqWG9nDvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Al6pUKSpbCZsOuhY1uop36eIBO2oLwQr4jThuLcwfYNlpmeSTV5ehMtnR9rZC61VmS6HXThwSjz2Lmov7Ko8HVfWdireVOE4umhOPO65a9FiWMuTX8ln0YpsbFCqPCGAgUNYtStheFZXSo687WbblB3JpNjAycBKxXhB8DxJJVXOjkNchbYnBVWl1e5wrztU1U60DpFCs8rHOVCkBKxmxkanhwBPMmQVeVeWWg5osZE51QiUrG6OTZgf3dHRUlJHecKMrNc9PwX2WIHWXJWKT5YW3Yd81Tb597ASppoj4YNeV7INQCah5a4fnX1WlJd5lh_ZzF6AMDtTpf1SzNiotw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ggOV4_omgIPn5KxqKx214_ieCHeiVQVDW6V0vApxI3pF2BQyKrmWRNVRj7oRjx517_W5lJYVeTyPk10RoIzdKCVYL3TLC8hGkFKy7Fq-6xYnw8_kZYj8sW9J18gx00n46--Tu7dQD3YQ8Y5UuEPB1Ank_5OnMwReuv6OQfo0oO5oVOwP-NamNY17lk3GC0ZEOe8O3mUSqBvTJI0-Sj0zmARgxeOoXYapvkJn3KU5jk5HjmairLZUhQOd18KTtlIE09dlmVqqtQNpYUV-VFyYhjKsF5URciPm6oR8E9-whNnfeHoClQx9rahJjivYQVu7QuR-ESdlILE9s-ipsytfcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کریس رونالدو و یارانش در آمریکا
🔹
تیم ملی پرتغال وارد خاک آمریکا شد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/658894" target="_blank">📅 09:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658893">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/122a593ce7.mp4?token=WurC7TZUvIBKa16FxWkWG6seacwQTsW1LgRJmJw32HV3IVqVoecBpvPbl8TFEdp2o2zIxKEGhmK4tU9awDvUoAG-K0jHwCG-x-A3vDH9ovLrZVVXf9QMEVOYImzJK3vPZjXoN0W3B_WQMXLHDiOuiHD3toYOHdWAH4wix7H63Szo2X1ukSR3JuwZ5Tv-SHPH4kSXMhW6I-Ba2t5fdFWf9nzGele6EawthU506U3wE5Fy3oRyCFEun8T_0mNW7t5r1POWIiQtoD2PAJvyBJggb6_OyFCTDGrq9fxMrLwiLYxUmfMYLb6sDm7vsQeeu5QpMFz_uUyDemYedI4fydeLJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/122a593ce7.mp4?token=WurC7TZUvIBKa16FxWkWG6seacwQTsW1LgRJmJw32HV3IVqVoecBpvPbl8TFEdp2o2zIxKEGhmK4tU9awDvUoAG-K0jHwCG-x-A3vDH9ovLrZVVXf9QMEVOYImzJK3vPZjXoN0W3B_WQMXLHDiOuiHD3toYOHdWAH4wix7H63Szo2X1ukSR3JuwZ5Tv-SHPH4kSXMhW6I-Ba2t5fdFWf9nzGele6EawthU506U3wE5Fy3oRyCFEun8T_0mNW7t5r1POWIiQtoD2PAJvyBJggb6_OyFCTDGrq9fxMrLwiLYxUmfMYLb6sDm7vsQeeu5QpMFz_uUyDemYedI4fydeLJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚫
*اتفاق عجیب روی آنتن زنده*
🚫
😮
توی شبکه سلامت مجری از یک کرم استفاده میکنه که مهمون برنامه گفته چین و چروک رو توی 2 دقیقه از بین میبره. منم تا نتیجه اش رو ندیدم باورم نشد ولی واقعا توی 2 دقیقه 10 سال جوون‌ترش کرد.
😳
☘
این محصول گیاهی توی ایران خودمون تولید میشه
🇮🇷
و متخصصاش دارن به مردم مشاوره 100 درصد رایگان میدن.این فرصت محدود رو از دست نده.
👇
👇
bam30.com/ads/landings/22748-2e958
bam30.com/ads/landings/22748-2e958
bam30.com/ads/landings/22748-2e958</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/658893" target="_blank">📅 09:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658889">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371fdb23d2.mp4?token=PmreqbAPgiL7Iz3L9cjj664POwwOz5ttgzBA0usAdgKOdGYqxcktkBgVRpg6eStTKjaX48v78kToWhjJhrioleai-IyaoxGF5cdADTCX-L-RqefnFiHZpoamYpfTidiwrouKBwZmXQSFFSTlxQsKVDIcWqRjW0XughgGctxxDDJV0lWf1R5rzgrEgVqHHHRdlxnaU2Xj6BHVW862Feh4T4nw14oXrUdKCFmiaS07svRQe130HmhwV4N1xqvn1_jFujn9dpJGD0vJWk3Hpb3tXi5zIDRdq20hhjrqlMM5C2g_UFTvgNkIVBHVERrGXJEJm3lUNS-DEFC9BxX6SnQuaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371fdb23d2.mp4?token=PmreqbAPgiL7Iz3L9cjj664POwwOz5ttgzBA0usAdgKOdGYqxcktkBgVRpg6eStTKjaX48v78kToWhjJhrioleai-IyaoxGF5cdADTCX-L-RqefnFiHZpoamYpfTidiwrouKBwZmXQSFFSTlxQsKVDIcWqRjW0XughgGctxxDDJV0lWf1R5rzgrEgVqHHHRdlxnaU2Xj6BHVW862Feh4T4nw14oXrUdKCFmiaS07svRQe130HmhwV4N1xqvn1_jFujn9dpJGD0vJWk3Hpb3tXi5zIDRdq20hhjrqlMM5C2g_UFTvgNkIVBHVERrGXJEJm3lUNS-DEFC9BxX6SnQuaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لیونل مسی، آماده برای حضور در ششمین جام جهانی زندگی‌اش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/658889" target="_blank">📅 08:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658885">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16b06d3d4.mp4?token=k-ALCnHdVvl4f35EIVYVb1EdlaK_Ucc3tESz6uykY6jPmbEFk0ucgr1eo_2o8foN7ZLY4AqpUnmTc8teQHU3IzbshsQ1G7mirxYCnrPtRQLTXz5LYfeCcGNl6w3dOOXCNZQ-3_mcDYBuQ4gBkmJthaTlYryhE9nPJ1-X7aq4tcJoTcb-o5dPA6GpKlsXWZWx7Jg4w8MnjcOX6tc5u6gSTdN8-Slz_iTvjopCoCxDGbvXdTA9CvTICWBtIKIk2WyLf_jQgOE0WZl3LKCxnklSOO_IVjZmaNqYWXSKOHXztngJ2-9FZG63qSWsUUvOeDVMXR6jRnVfSLfBQKA61O8mIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16b06d3d4.mp4?token=k-ALCnHdVvl4f35EIVYVb1EdlaK_Ucc3tESz6uykY6jPmbEFk0ucgr1eo_2o8foN7ZLY4AqpUnmTc8teQHU3IzbshsQ1G7mirxYCnrPtRQLTXz5LYfeCcGNl6w3dOOXCNZQ-3_mcDYBuQ4gBkmJthaTlYryhE9nPJ1-X7aq4tcJoTcb-o5dPA6GpKlsXWZWx7Jg4w8MnjcOX6tc5u6gSTdN8-Slz_iTvjopCoCxDGbvXdTA9CvTICWBtIKIk2WyLf_jQgOE0WZl3LKCxnklSOO_IVjZmaNqYWXSKOHXztngJ2-9FZG63qSWsUUvOeDVMXR6jRnVfSLfBQKA61O8mIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ تمرین زانو که برات معجزه میکنه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/658885" target="_blank">📅 08:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658884">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qm9jZrrLHpxng23h4P-TkuvrtCZdIGQ6DC9B6WQZZljYzfAXNc7sTovgu4vhJnuTDgwbD6WOiv6wpraV-zOEZ4YEsNYaA89-4xP7cepYFfa7D296eKZ9RjaPVjLxP9BkwhP5yzKoIOhklrt8ODaEqHETo92EL4SJUelwuLSCyk9H_jxQA9kpMkeyQmHukTqMAgeNV7SOCAKOOo_EnVOgSVPfVVpYkMI9fsq0-sajRnXk36Ir4OkMXEHv3-8V2Ba5wgnFrWlzvL0wN0xGH7-leKTc-Ptr_U22ucZRo96z346bx1wP2zCUgS2OCUVOMUmWgmIkBEINjjb7wJwlNPWzcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: توافق با ایران تا اوایل هفته آینده نهایی می‌شود
وزیر خزانه‌داری آمریکا:
🔹
با توجه به روند پیشرفت مذاکرات، انتظار می‌رود توافق صلح با ایران احتمالا تا پایان همین هفته (میلادی) یا اوایل هفته آینده نهایی شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/658884" target="_blank">📅 08:12 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
