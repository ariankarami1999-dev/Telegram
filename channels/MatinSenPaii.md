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
<img src="https://cdn1.telesco.pe/file/Wd2Ej-hwZEaZVZD1ZqCbQLy6xIRjKUk4378MwiF23eZDfGIBn93emmE4E0htqYSZMaOCGHaMsRWwzKiPL2l-o2c2zy6t5mEZGLg3fEC-thO6O5-ye5_spgEndsz5mQHp_va0ewvh9Z5bXjejuPo81ppDNzGRSlzIOOYhe_9p5SX71uhKlKwEZRrwSZRg5DWxPQh79Bk8zbL5Jh3NHpVKsthwFOpyMYRgDeHlqQxkpgzPf8119cfh5RpPEne155o8rlfVDHGrQnXFPzd1ntpLf57_DgDRGn6HQurqVLPeUPDalFapVRHOXtPUrmHNWpzA0aYgl-vEdFVGI0co5k5_UQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)ارتباط با من:https://linktr.ee/matinsenpai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 09:36:27</div>
<hr>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity https://github.com/MatinSenPai/Gemini-Config-Checker  " دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید: https://t.me/MatinSenPaii/2881 "  کانفیگ‌های…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/MatinSenPaii/5496" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cfp2UmGrBrEzae8qNAviwDQ0w_1UJepJS6eF25N4vsArGogeAv1301aYInj53SgXaenyP4wulXp6JJkls-ZSshDW3CVcRV3fIQzazv4Sv0Qdvn52yk60hhz9KREB392_net4eVIX6zuyS5kaFqAuhVOfwOExI83OMYdHbnXbC-UMfQFVYj8SJv4j2jPcYZ3zi0UxJ5RnkYKwBHrDzEK2AAJelbE4xyTXq_vzpLfexY-SIDWQntWVFPtOF1gIqQUZGo0czpY5w-v0d6H_tI28xp0W9RjYtEi0p2Vl77--Q5W5TO5b8RQJUnTKNi_vwLsQUXCVS4ACVzfiqW7LG77a4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity
https://github.com/MatinSenPai/Gemini-Config-Checker
" دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید:
https://t.me/MatinSenPaii/2881
"
کانفیگ‌های رایگان زیاد هست، ولی کدومشون واقعا Gemini و AI Studio رو برای جیمیل خودت باز می‌کنه؟
این ابزار هر کانفیگ رو همون‌طوری تست می‌کنه که یه آدم استفاده می‌کنه: با حساب Google واقعی خودت، توی مرورگر خودت، از مسیری که واقعاً ازش وصل می‌شی. چون Google ریجن رو فقط برای حساب واردشده و بعد از لود شدن صفحه تعیین می‌کنه، تست‌های ساده‌ی «پینگ و API» همیشه همه‌چیز رو سالم نشون می‌دن و دروغ می‌گن.
🔹
دو حالت ساده و پیشرفته برای انواع شرایط
• ساده: کانفیگ‌های خودت یا لیست کانفیگ‌های رایگان (لینک، ساب، base64) مستقیم و بدون زنجیره تست می‌شن
• پیشرفته: کانفیگ‌های رایگان از پشت کانفیگ پایه‌ی خودت تست می‌شن (تو ← کانفیگ پایه ← کانفیگ رایگان ← Google)
🔹
تست واقعی ریجن
• ورود با حساب Google کاملاً لوکال، با Chrome / Edge / Brave خودت؛ نشست فقط داخل حافظه‌ی برنامه می‌مونه، چیزی جایی ارسال نمی‌شه
• AI Studio و Gemini جدا بررسی می‌شن و می‌تونی انتخاب کنی «سالم» یعنی کدوم‌ها
• اول اتصال سنجیده می‌شه تا کانفیگ‌های مرده زود حذف بشن، بعد فقط بقیه به مرورگر می‌رسن
🔹
پروفایل ضد فیلتر
• Finalmask (fragment)، Fingerprint، ALPN، Cipher suites و IP تمیز
• مقدارها رو از خود کانفیگ یا لینک می‌خونه؛ کپی‌پیست کن و تمام
🔹
خروجی
• «کپی با Chain»: کانفیگ کامل و مستقل، آماده‌ی PattN / v2rayN و Xray استاندارد
• خروجی لینک، JSON، و ذخیره در فایل
• انتخاب کانفیگ‌ها، مرتب‌سازی بر اساس تأخیر، و چک‌کردن دوباره
🔹
همه‌جا اجرا می‌شه
• ویندوز، مک، لینوکس: اپ دسکتاپ و نسخه‌ی وب (برای سرور)
• اندروید (APK): فقط تست اتصال؛ اندروید اجازه نمی‌ده برنامه مرورگر رو کنترل کنه، پس بررسی ریجن واقعی رو روی کامپیوتر انجام بده
• رابط فارسی با تم تیره و روشن
• متن‌باز، با موتور Xray-core داخل خود برنامه
این پروژه، به لطف این پروژه‌ها و آدم‌ها ساخته شد (حتما اگر دوست داشتید استار بدید):
• patterniha: PattN / PattNG و مقدارهای ضد فیلتر (Finalmask)
• 0xRadikal/Free-v2ray-Configs: لیست‌های کانفیگ رایگان
• bia-pain-bache/BPB-Worker-Panel
📥
دانلود و راهنمای کامل (فارسی و انگلیسی):
https://github.com/MatinSenPai/Gemini-Config-Checker
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/MatinSenPaii/5495" target="_blank">📅 22:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/MatinSenPaii/5494" target="_blank">📅 22:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">وقتی یه مدل رایگان لوکال پیدا کردی و پروژه رو باهاش می‌بری جلو...
@Linuxor</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/MatinSenPaii/5493" target="_blank">📅 22:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CktH1JwO0eh0SzO2IVvl-vTEh_xmEwFR0j2RZstCPeH4qoB6ANMenqdZaT_9b0t9Apceydx3O38KDvd5F6UbQLyVMf3xzkuS4AgtJOo4iBz01Ah3063ma9Di1aWbzgkvvq7MQ_YCsqp5VBUYREh14E-V92ePbyD90BORwZVl2Ewa_032ZG-6CjNh4E1N-5Pt0dV9w5A4jLWAXOX1OgjUCR1fC7nWWXufmWjpNdKYFwAC9YmOk0fP7QErAY3mAJHllVylPg2qvi9dlHFhxEmyUcN1wq_RFMqaRgT8ZSTvvuLtenqWl5y_poSHYc0YROOUsnH5PlsFDluH2N42iKEjAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه دسکتاپ Cline برای لینوکس، منتشر شد
روی Cline می‌تونید از مدلهایی نظیر
Muse spark 1.3
Deepseek 4.1 flash
Mimo 2.6 flash
به رایگان برای کدنویسی استفاده کنید
https://cline.bot/desktop
ویندوز، مک و لینوکس
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/MatinSenPaii/5492" target="_blank">📅 19:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=qqQZv-M42-tdJ01F8eikCg_hP7ezb69WeBdFHnq99_L9QhueZuCb2jQtGblksLJqRzJFKnL6WTp62deHvq07eX997sveFUp2yvteEd8vrvHBhWmRTGdny001tWAax55F-B_yH-chfX5e3fmbXFw2tkHmbmyHlVzPgSnvbnRxqaT-wnIl0gGU2LnUMu9caSoyrADrzGNFI6WUqLpqJj3mXmM3SXlEvmPu9jmAbEjQGMcvHfDDeVtVCdggANova1rFcN7rL1qtOvyEr8HvV3wTmumsKhAO1C9I-b75LbvwO8ZGAWW8goRxHoyoSf8mqSoDg0E4rl18r2ogkPkqkzQysA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6249e0466.mp4?token=qqQZv-M42-tdJ01F8eikCg_hP7ezb69WeBdFHnq99_L9QhueZuCb2jQtGblksLJqRzJFKnL6WTp62deHvq07eX997sveFUp2yvteEd8vrvHBhWmRTGdny001tWAax55F-B_yH-chfX5e3fmbXFw2tkHmbmyHlVzPgSnvbnRxqaT-wnIl0gGU2LnUMu9caSoyrADrzGNFI6WUqLpqJj3mXmM3SXlEvmPu9jmAbEjQGMcvHfDDeVtVCdggANova1rFcN7rL1qtOvyEr8HvV3wTmumsKhAO1C9I-b75LbvwO8ZGAWW8goRxHoyoSf8mqSoDg0E4rl18r2ogkPkqkzQysA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه اندروید کوچولو هم براش زدم
سعی می‌کنم تا شب منتشر بشه</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/MatinSenPaii/5491" target="_blank">📅 19:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MyeC-TyLUxu5wVnZ96MHF3N-yFDmiuXZnXHQDsupq8n2oZyltZSziiUvD5Jm_0yFwhOFUOxM25zj8IohwFsyanhUBy0SCW1bSGzPoJnQtp4rTsTbbYZp6IfWakuplYFXS63jvT1TQDSL2GK37EQ4WhyAt9gfHILrWUlvsXqooaioN57pEboIiJ5jhyJINoDXppo4IFPdWaqzeGPeOUghg5WxFUiHxRroLUNNMpGZtW6CxxA2Ndw6DXXsdHRKfTrp5D-hjsdFMVVo1umVgRVZThN6dgxqFjDa3ZImSOBtX-ki9sM9xk9AfJ5rAR-jLOf963SbxkFdIx4cMU_kci_3OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر میخواد تبدیل به یک مرجع عمومی صدور گواهی دیجیتال (CA) بشه و در قدم بعد، گواهی‌های جدیدی به اسم Merkle Tree Certificates رو هم در مقیاس بالا صادر کنه.
هدف اصلی این کار آماده‌کردن زیرساخت وب برای دوران کامپیوترهای کوانتومیه؛ چون الگوریتم‌های فعلی مثل RSA و ECC در برابر کامپیوترهای کوانتومی قدرتمند آسیب‌پذیر میشن. MTCها کمک می‌کنن گواهی‌های پساکوانتومی بدون اینکه حجم و فشار رمزنگاری روی اینترنت به شکل شدیدی زیاد بشه، قابل استفاده باشن. کلودفلر گفته هدفش اینه که این گواهی‌ها رو از اوایل ۲۰۲۷ وارد محیط عملیاتی کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/MatinSenPaii/5490" target="_blank">📅 18:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cvEaJYWqwrOVb6GLalhXW--tu6xY00gXErHFMB6jueMK3lTWF0DpJT2IncyrOMNIIOKH3Q4F7pGrKmNbasjzEyFdyg9Pl_4bZ5rIpB-yIdTZXNdOXUfqgHFxosaXbDSYARPgF_x7QJah4Gs83rhbQm1H73eQ7jEC-vU84QcEq_581m4bmTrnfHTAwENy_nInWbXsuQ534XBczqysrGdSYI2hSswcN9o26qEkOWXXPb-w_czVnFGgIIpRygCSUuoojoOg_dRvdTpTlj5zw5x1kiBxeeOSpr7aOZkgSEOiGsm3UQLwQwyEDonsAaOTWQAY24UbMl77WYgB0AefJuMpcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Lo2XHFiRSPPUKWxZE9gR2w1rEwXbURhj1X4ASO1B5T11rwid4Kjht0CaKz7wMvRKkqIru1roWvw0AuNNuWauGlIkD4mTWopjuldcX5ALa7B7Mi2iAPfXkYtOGMfFGAugaAHA5SluZ4ewwgnqzv8-b7gGvKyNbMCXhfkbhC8s-vrXPUxE-BfeY6g0vXtPrbN6BIQWKITNiqiu2wV54PIsod_cwPRlkpo3msTcM5bm0M31QVzac6V9N9nKXnxi_w1XtZk0IZNqa1UkF4HevXxpNA6Da3zbApWnmMaabIYaOBQ9K7fV2uiOEBTziLk1H9nbe8iaq-z4tPsP-Mgb1__ZjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/5488" target="_blank">📅 16:18 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTaleo Comics | مانگا، مانهوا، ناول و کامیک</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gsowjA_eXMYh8vPtOUwWSbvBmTLXOC-NfkbWffbkz5io6LQDkj0Ko0u0VFg6no3GSXVRAPbyoticw-oy0NUWo_1mv4fPRppkdqJmfxYwhb4gkxYrprOK6r2ccjP87DVfZeqH07QYQOBmT8cXQqBuBseSRn_pgMRqq1cv4kJSHAAIzwBFLyN_yO6gKDvd76pMLZQBb195QyekVtuNipov_rxrvQfImJOXbL4slHF5JzZCb9a0wVNiA7z9J4Mgx61G1hSDnMZgFi1Ruuzpp6-XrlbHJ3wjDN1qjpcKn2intrKcwSE0mcHIFwgCy_3jy_KjlChhpaKmvguBvEe_INyJ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔤
🔤
🔤
🔤
🔤
استخدام ادیتور مانگا و مانهوا در تیم تِیلو
😳
شرایط:
1- تسلط به Photoshop(برای ادیت با کامپیوتر) و یا ابزارهای مربوطه در گوشی موبایل
2- حداقل 3 ساعت تایم خالی در روز
3- مسئولیت‌پذیری
4- کار کلین(پاکسازی متن) و تایپ‌ست(جایگذاری متن)
به همراه یکدیگر
انجام می‌شود.
5-
استفاده از هر مدل AI برای بخش Clean، هیچ مانعی ندارد.
وقت شما برای ما ارزشمند است.
حداقل حقوق
به ازای هر چپتر مانگا/کامیک: 60 هزار تومان
حداقل حقوق
به ازای هر چپتر مانهوا/مانها: 40 هزار تومان
نکته‌ی مهم:  پس از استخدام، یک ToolKit کامل افزونه‌ی تایپ اختصاصی برنامه‌نویسی شده‌ی فتوشاپ + اپلیکیشن کلین با هوش مصنوعی در اختیار ادیتور قرار می‌گیرد تا کار، ساده‌تر شود
برای انجام تست اینجا کلیک کنید
🥺
t.me/TaleoCo</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/5487" target="_blank">📅 14:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دنبال راه رایگان، عمومی و بدون دردسر برای دور زدن تحریم Gemini و AiStudio بدون نیاز به Veepn و این ابزارهای ناامن هستم. تونستم دورش بزنم، صرفا در تلاشم یه ابزار بنویسم که عمومی بتونید استفاده کنید بدون نیاز به VPS و..</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/MatinSenPaii/5486" target="_blank">📅 14:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIb2t0ihGOIMcOmWciIGAMA-k4YxDKgHnekm5G7YWVb0-d9fUj3o1IY3YOQ2v4BCybuWTr2oRG5RVRFLMtk3ABXXTh9FSpzc8-r9K2Q1HNOhiNG1E7N3dMOAPHCmNE3YPqfSaI84iWzBjFEDlN61zkdi_OZUyVnvXRICyY9BHu-8MtJxB_ia5pWn3Ds49ND5jjZ64AX_BVOn36hvzAmQvq_zcLT8HobxFpesB1eiPRMG8fjeA8G1EMCh18NaIwINGY93r04eqZ4JXu3A6hpeD0Yfm6O2yw0LzINlfnnI9-JkUvKRf5KLLuC21THiZA92GtlOfT9xLpfkGqPUhwbLfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان دوران بارکدهای سنتی و آغاز سلطه کدهای دوبعدی
بارکدهای تک‌بعدی خطی که ۵۰ سال پیش اولین بار روی آدامس ریگلی تست شدند، کم‌کم از بسته‌بندی‌ها حذف می‌شوند. طبق ابتکار Sunrise 2027 سازمان استانداردهای جهانی GS1، بارکدهای سنتی جایشان را به کدهای دوبعدی مانند QR Code می‌دهند که می‌توانند ۲۰۰ برابر دیتای بیشتری برای رهگیری زنجیره تامین، هشدارهای فراخوان سلامت و تاریخ انقضا در خود نگه دارند.
من هم قبلا یه ویدئوی کامل راجب داستان بارکد و اینکه چطور اختراع شد و سیستمش چطوری کار میکنه، ساختم توی یوتوب:
https://youtu.be/PAHA55mHLWs
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/5485" target="_blank">📅 13:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PdlTFsxvjKhUsnuYINzE62hYmr8VvEaRlgZAl-5MoGVvsBWalOMyecSoApt39JV21drP-lyPsbnaiL3k6K27GOS2l3MhnN95HX-rc654mx2Xxfh1U8admTxthaZ9BDsxk2whD9tEB3eUK6-RR71YLEv9nfbB7WKMoF_gGuaYOjUcxkjHiuKlNfQpZpaCyXzJL9PQFJEZJZ6ZFlIqGzd0NyrN6z-Epvr2r7aSqjaTZXk9kCEsWeI5xqaMJmxTT-Kg0eir0zXQ2bNfVs7PSRtjQSTbgy7hea_iLujTClflRjKMmF7f7OCks7GwvNBVqu2JXr4LOkRjRMHE5isdQLVSSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
عزیزانی که با WhiteAether سخت وصل میشن یا مدام قطع و وصل دارید، این روش رو حتماً تست کنید.
به‌دلیل اختلالات شبکه، ممکنه Endpoint انتخاب‌شده مرتب قطع بشه و Fallback به‌صورت خودکار Endpoint دیگه‌ای رو انتخاب کنه؛ همین سوییچ‌ها می‌تونه باعث کندی و ناپایداری اتصال بشه.
🛠
برای رفع این موضوع :
1️⃣
وارد بخش Routes بشید و از پایین صفحه وارد Endpoint بشید.
2️⃣
اسکن Endpoint رو انجام بدید.
3️⃣
بهترین Endpoint از نظر Ping رو انتخاب کنید و روی اون بزنید تا Pin بشه.
4️⃣
گزینه Fallback رو خاموش کنید.
🚀
حالا دوباره Connect کنید و نتیجه رو تست کنید.
چند نفر با همین تغییر مشکلشون برطرف شده؛ ممکنه برای شما هم در شرایط فعلی شبکه بهتر جواب بده.
@whitedns</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/5483" target="_blank">📅 10:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVIirLAQBjH_Mb3Pv93TttYuUlmY0urdPXbTI14BuLFhzRufk5_TbtZ33bRAyc61aRozI0wZWKuKby1w7X-oUmGM5pkLLJAHUn_ck4NAV0R1yYL8FCQIa9cJveJf5VW3AQmHgSgUW7TEUzn52_7pEFIv3sU-D_Uu-McOiwubOIHjJ47ZPpoit-b9LuJhztBk07yfjEjXothimwXM5O2a-BS0mrnV-1Yd-yHBUMp7krhdbPvqo5iKJ9NYEOHIpC2k8eM65dYuw0v3M_7hEpprnyQuRd5yxKyT_KZgQaoS7v9cd_vMaLheF7uGdK80D_JdGMcR_V7NtTSKIIJffqq-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل رسماً سراغ سوئیفت سمت سرور رفت
گوگل کلاینت‌لایبرری‌های Google Cloud API برای سوئیفت را منتشر کرد؛ مخصوص سوئیفت ۶.۲ به بالا با SwiftNIO، مولتی‌پلکس HTTP/2، انتقال gRPC و ایمنی race در کامپایل‌تایم. گوگل می‌گوید با کانکارنسی سخت‌گیرانه سوئیفت ۶، این زبان با ایمنی شبه‌راست و پرفورمنس قابل‌پیش‌بینی ARC برای میکروسرویس با Hummingbird و Vapor و زیرساخت ابری ایده‌آل شده.
مبارک سوئیفتیا
🎨
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5482" target="_blank">📅 09:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/es1B1OFzfvTaFzeKRfZr2au8p1WM4oD9vXwFPBgJ7xhTXYCGk_d2KHDpfSv65cPCGCZwyJQ88Hl_6MUOYYhQh2B5WT43krWwQHlsMWHijct4rCaxTSdsukZWCtMh1YMBtPoD29dUK4KQ-0UPVlxpO9HKN9hehZTeG19XCyRiXUZJo3pcz9Vn6TBNiYbxiiTAo64AmDemZbJEmRzHRuHyYDuM1zPxQLDDJCHtCT_84dEhefuFBhCbOG5PGxq0kQZAgmp83ElpZyO0dKuDOI6qijKfkEy_LkTlNgqYY56Ux9fuRUe7eTM8U1o7GBuYpgt9KbbeUXJ-CF21iZxd9UBjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA  من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5481" target="_blank">📅 18:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VjOTNHGVtDwAo9vN7TC9Bll-Os0w2qkIbxLpQlhybXq8zGOQ6PD2dn0ltCaYqe1ZK5kiOyzxNaBEB3WUK3_9WxNCPIJJMd7vMEsvy-RQhfwr9PXASi1sHRkVbI4zRYPYyfGlCYKxqXWY3_aYTzSe7OxkAJJ9si9EN89UtZOqBicZ2Ys2ockGyEVKVBvmYEvofxvoflMFEfT_X2NzqvoVCtq3M6XtJoxM0XsC4gAQRH3Q9gBwBMrJLJTW06qI7UhmlONnypeKnZ2Q-DDPTFFniNaszsDeQEJ1TeIQatfNvMg3jJKZ_BvkwT4v1SJ97rJ1rl4-dFiGdr_LI06RH-9mBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fJUpxOn_rj-QPlhGJ_AzfFJGqxuNyyE61oV69FXwAbghwsf-v4KILIFOeREwNMPIHsnFEALyzN6FjtVg7hVtCFgK42kSvwzfBIrc0ert-UAAqQ4pLHtZe5rNOMTYO6UPiYz6QOU4r7LEkGRTipM232ODy9jC5PwXZUhyaLiYG9ZtNisk0D92uQHwYlEQo4IXBEBEwuO8o85ln-2UNKLHbc8i7wrLcsHEvgEFm8R_yXb9obvVOmh3HjPRsccvK_U_1wnrQ9hPlQ4PdNR5YSoEfqi_4XY5ENfZB0RZhzjnoFyE0pIaqjziwzmmvgjI_m2nQOihzADNsv-XcncrITRT9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5479" target="_blank">📅 18:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aNbioMwVxBro2a0OSOGFR01jdzlF0qAtAv2ktjkOnQEmy5Dh9FIqSBajMaisq11pNsJ1yUbNl8qDOEmARjM7xpSFSVLES1czikjhmCXrOoGSyR1Y1uLd6G7vQceI7C8wMiewz1tan4A_KfMJoLIuMZDBpiFEfN-h3yald4Yyr7ybWnhp20HvJ6UZvcvY0vWaTdW7QvEdbvQ_zXT3Dn-gUN5tF8fpZeBkMT4-I0DhQc_S4-TVmY2BHD_OfXL2IuQo8zxxSzCf4TYKXcRZVm3WhJ8o6ZU9RQLJgMIJvqzFlFk_nnXIh2tYZe_LDw2WijuUs62HA62_S8mYrOqtZOMNmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجرای آفلاین LLMها، روی سیستم شخصی! | مدلهای هوش مصنوعی Local با OLLAMA
من این کار رو توی دوران قطعی نت کرده بودم و بدون هزینه، هوش مصنوعی داشتم روی سیستمم و همونطور که توی ویدئو توضیح دادم، ازش استفاده کردم. الان، تکنولوژی‌های جدیدتری اومده و توی ویدئو یاد دادم چه شکلی ازشون استفاده کنید و حتی با اینترنت ملی هم بتونید دانلودش کنید.
امیدوارم که مفید باشه واستون
❤️
دانلود Ollama:
https://ollama.com/download
📹
تماشا در یوتوب:
https://youtu.be/EAF-hMPUMYc</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5478" target="_blank">📅 18:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5477" target="_blank">📅 17:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXrDIndqGoNv245o8NEGXtc35YgR-LtdwTuOPnS_sV5NOz6usePQTagYQ72yaDMxP9UwlAl5dtBc4c122P0iX3nyvDmXsK_rk9ERRZ-2sNEwu8Tyq4HlCIRqBXN_0ybGf9QQ3IHR9fWWu0XvjnMbxuDJgP4ZIA9_6NB-Mnx0Os7_AyDNwA1NBNsS9o7dRgOIrLoRWHYk8xtzjImjA63P4gPI9p_OGdemtzI25Eqdjf8V5ZLXgtjLBm_qSUFoWgkYko63PWzZb176qOPduRgG0snoPOt-N8qmbJTEj7W9sfEYvNEizzqIFpfunmZNlhmqAHPaqMcJaaOyBkJKBs-yRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به جای توضیح دادن «اون دکمه رو می‌گم»، روش کلیک کن
👀
اگه با Codex یا Claude Code رابط کاربری می‌سازین، احتمالا پیش اومده نصف پرامپتتون صرف توضیح دادن این بشه که دقیقا کدوم قسمت صفحه باید تغییر کنه
😅
ابزار Agentation یه نوار ابزار به پروژه اضافه می‌کنه؛ روی المان موردنظر کلیک می‌کنین و می‌نویسین چه تغییری می‌خواین.
مثلا:
«فاصله این دکمه از عنوان، ۱۶ پیکسل باشه و توی حالت loading عرضش تغییر نکنه.»
⭐️
نکته کاربردیش اینه که بازخورد رو همراه selector و اطلاعات المان به agent می‌رسونه. می‌تونین خروجی Markdown رو کپی کنین یا با تنظیم MCP، کامنت‌ها رو مستقیم در اختیار agent بذارین.
برای Claude Code یه skill راه‌اندازی هم داره:
npx skills add benjitaylor/agentation
بعد داخل Claude Code دستور /agentation رو اجرا می‌کنین.
فعلا به React 18+ و مرورگر دسکتاپ نیاز داره و بهتره فقط توی محیط توسعه فعال باشه. تغییر کد رو agent انجام می‌ده؛ نتیجه رو هم همچنان باید بررسی کنین.
برای رفت‌وبرگشت‌های ریز طراحی، ایده کاربردی‌ایه
🔥
معرفی و دمو
·
راهنمای نصب</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/5476" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCluvexStudio</strong></div>
<div class="tg-text">در کنار بلاک/فیلتر شدن دامین دریافت کلید وارپ، اومدن sni مسک (Masque) فعلا فقط h2 رو بلاک کردن :))</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5475" target="_blank">📅 13:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5474" target="_blank">📅 10:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">چطور فاصله‌ی بین Hermes و دستیارهای اختصاصی Dots و Grok رو پر کنیم؟
یکی از کاربرا توی یه راهنمای کاربردی از اکوسیستم هرمس توی ردیت، بررسی کرده که چطور می‌شه بدون نیاز به پلتفرم‌های بسته(مثل grok bot و dots و muse و...)، قابلیت‌های پیشرفته Dots و بات‌های گروک رو توی ستاپ Hermes پیاده کرد. راهکارهاش شامل لایه‌ی مسئولیت‌های موندگار (persistent responsibilities)، سیستم دیده‌بان پرواکتیو (Scout) برای وب و دیتا، مدیریت وضعیت تسک‌ها با SQLite، و تعیین سیاست‌های دسترسی قبل از اجرای ابزارهاست.
که البته خیلی از ۱۱-۱۲ تا قابلیتی که گفته همین الانش هم هست، صرفا دسترسی باید راحتتر بشه توی UX خود هرمس و به نظرم کم کم به اون سمت هم میره
👍
پستش رو توی ردیت بخونید، بد نیست:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5473" target="_blank">📅 09:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مهار دزدی و Distillation Attack مدل‌ها توسط OpenAI
شرکت OpenAI اعلام کرد یه کمپین گسترده و سازمان‌یافته برای استخراج و تقطیر (یا همون Distillation خودمون) قابلیت‌های استدلالی مدل‌های پیشرفته خودش رو متوقف کرده. گویا مهاجم‌ها با کوئری‌های پیچیده در صدد کپی‌برداری غیرمجاز از متدولوژی استدلال منطقی مدل‌ها بودن. اوپن‌ای‌آی دفاعیات و سپرهای نظارتی جدیدی رو برای شناسایی و خنثی‌سازی تریک‌های Adversarial Distillation مستقر کرده.
(ببخشید برادران چینی. راههای جدیدی پیدا کنید
😭
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5472" target="_blank">📅 01:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5471" target="_blank">📅 23:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آرنا توی این ویدئو، قدرت Gemini-4 Argon رو بیشتر توی زمینه‌ی 3D و قدرت پیاده‌سازی گیم‌ها و محیط‌های مختلف بررسی کرده
که خب کامل نیست و باید توی تسک‌های ایجنتیک و کدنویسی و بکند و... ببینیم
انگار که کلا قدرتش کمی پایینتر از GPT 6 sol هست که خب، ازم بپذیرید که قابل قبول نیست برای گوگل، اونم بعد از اینهمه غیبت کبری
توی دیزاینایی که نشون میده، قدرت Sonnet 5.5 هم می‌بینید
😂
خداست این مدل
https://www.youtube.com/watch?v=h5EL5zThKaI</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5470" target="_blank">📅 23:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CG-6gm7m9VE4hsxVJaCpGTlaBVChRR_TkyG3Wv9ARgAiVNeGaf5oW5Q0ZwrBY1ksklwIhI7xmTdD_t5oFmxltEy-z_YxucY4qECKOsh0dZog_kPn-AtAXaXPl_eVCQTXP-1jt1tT9vzgRLOJ1zp8f-bnG0uOA-3okxOb4aJgWHOVuA1kbus_7iwt9C75gf4ZAUWNv2myxl0B_jlisHRP5z_okF2QLBvpyXnkZAePbe085ldRiVRRGeXMbmCVDNI-PxPXiCGW1OMtJfyW1_UBerrBPCmCD8cXM_0iN4a9e2bvcuQYX7ug9zMUtaiosLc-kd3A_jXqLzsQFNDtAScgYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)
1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا
https://github.com/patterniha/PattNG/releases
)
یا نرم‌افزار PattN(برای ویندوز از اینجا
https://github.com/patterniha/PattN/releases
)
دانلود کنید.
2- کانفیگ V2ray خودتون که با Worker کلودفلر ساختید(آموزش ساخت کانفیگ رایگانش اینجاست:
https://youtu.be/iAbYpjXyLpY
) رو وارد اپلیکیشن(PattNG یا PattN) کنید
3- توی اپلیکیشن اندروید، روی مداد سمت راست کانفیگ و توی اپلیکیشن ویندوز، دوبار روی کانفیگِ وارد شده کلیک کنید تا پنجره‌ی تغییر تنظیماتش باز بشه
4- توی بخش Finalmask raw json، این مقدار رو وارد کنید:
{"tcp": [{"type": "fragment", "settings": {"packets": "tlshello", "lengths": ["0", "104", "1"], "delays": ["0"], "maxSplit": "0"}},{"type": "fragment", "settings": {"packets": "1-1", "lengths": ["114", "1"], "delays": ["1"], "maxSplit": "11"}}]}
5- توی بخش Fingerprint، مقدار رو روی
Unsafe
تنظیم کنید.
6- مقدار Alpn رو روی http/1.1 تنظیم کنید
7- توی بخش Cipher Suits، این مقدار رو کپی پیست کنید:
TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
8- کانفیگ رو ذخیره کنید و پینگ بگیرید. دقت کنید تمام موارد رو انجام بدید. آیپی تمیز
188.114.97.6
عموما کار می‌کنه. اگر کار نکرد، از اسکنر
https://github.com/MatinSenPai/SenPaiScanner/releases
که هم نسخه اندروید داره هم ویندوز و مک و لینوکس، استفاده کنید و آیپی تمیز پیدا کنید.
مقادیر ممکنه عوض بشن، مقادیر جدید رو می‌ذارم خدمتتون.
موفق باشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5469" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzgvcr4dUXBLpYDHyMzKyYBy54Z4HDXHBJXrfdMdvVer_s9JwMITIIo-68C2lBKfvtYRDLTRS3uO8r3NLhTP9-YFcpVD5XKIBQCdlelGNOZ51dPFplJEensxeWkUnCCCu70Zm8M8nxCQVj3HEghDr7apMs-Vff6Uj2tF0IR4nYk7eo_GSwNNlmMGjHWwiOFO_n3KqbH2F38__mdE7Aps1_D9yrOUl53VSGmyOitzDCiA9VAaq36ka6823QFVAtB9WumfWbWaI6zmI02VB86PU12T16K05msuFftqGGe5ZSZR7JwPgJAo11SFsDPH0wfZ3fRXcOo9WCB_hcNNpyuvkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل Airbnb: ایجنت‌های هوش مصنوعی به سیستم‌عامل اختصاصی نیاز دارن
برایان چسکی، مدیرعامل Airbnb، توی گفتگوی جدیدش تأکید کرده که
پارادایم اپلیکیشن‌های فعلی پاسخگوی نیاز ایجنت‌های خودمختار نیست و دنیای هوش مصنوعی نیازمند سیستم‌عاملی مستقل و AI-Native هست تا هماهنگی بین ایجنت‌ها و خدمات به شکلی پایدار صورت بگیره.
خب مشتی یه کاری بکن. ما هم میدونیم
😂
طرح نیاز که خیلی وقته شده
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5468" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بزرگترین مزیتی که ایجنت‌های شرکتی(Muse, Grokbot و Dots) دارن اینه که با مدل خود کمپانی یکپارچه هستن
برای هرمس، یه کم چون دستمون توی انتخاب مدل بازه ممکنه گاهی اوقات گیج بزنه یا دو نفر با کار یکسان، تجربه‌ی متفاوتی داشته باشن
اما همچنان هرمس رو ترجیحش میدم</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5467" target="_blank">📅 19:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">قراره با هم یه اپلیکیشن تمرین زبان با روش Shadowing بسازیم.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5466" target="_blank">📅 18:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gsSzKAYOuE6FoRaGEmnsWxhQ-_z4UKF8r4RVAhrGekMog6l6RtjlOSxNzXlSEkRJpBQjDFv2d7-kAsyWsBkaBHc4cvjF28dd0e6MnxPX4FJGijItE_jYYy6KMOzqrIjTlpkbBrAbfVuV0bzS40QnrKIOT1pblmxoJ3EINygRoBqst1iw3i6Mo1YgotlREhkMPeFfLbcrC3sPdpodQJ0WjAO_n0_aCAkfgV2WBp5m1J8iMGh50YfozUFY1gUjbTPM7X67hUKyaWXFK4qkW6ZotyM0-26TPL6Lxhsgnk7wtO9KeRS7Tyn9oMULn27J-Czb-W53DvdPETtFZuUYXmP3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردیت فیدهای RSS را متوقف و دسترسی عمومی به API را مسدود می‌کند
ردیت اعلام کرد که به دلیل اسکرپ گسترده داده‌ها توسط بات‌های هوش مصنوعی، پشتیبانی از تمامی فیدهای RSS را از ۱۳ نوامبر به پایان می‌رساند. این شرکت همچنین تاریخ توقف کامل دسترسی به API عمومی را مارس ۲۰۲۷ تعیین کرده است. این تصمیم در شرایطی گرفته می‌شود که فروش داده‌های کاربران به غول‌های هوش مصنوعی به بخش پرسودی از درآمدهای ردیت تبدیل شده و این پلتفرم دسترسی رایگان را کاملا محدود می‌کند.
که خبر بدیه برای ما
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5465" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">امروز زیاد ازش استفاده کردم
گفتم یه توضیحی راجبش بدم</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5464" target="_blank">📅 18:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یکی از قابلیت‌های بامزه‌ی یوتوب، Hide user from channel هست
این شکلی که وقتی کسی کامنت دری‌وری می‌ذاره، زمانی که هاید میشه، هنوز می‌تونه کامنت بذاره، اما کامنت‌هاش رو فقط خودش می‌بینه
نه من می‌بینم
نه بقیه
اصلا هم متوجه نمیشه که هاید شده
😂</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5463" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FoMyQFCenFsG9thDMo6an9jOgnCO61Iqe0cbHnD0-kVxo9hKsgkU6VsC_G5ldOEsbVscyLLTDHcNV9GDoUHDZ5lZZ5F-zU8zro9a6446SDe2FuTSDNsY_40Xl3WlIXB-B9dFJQtPVB3-cfMoj6Oexc18J64gYseJy_v7ZXuR6M4P02c_Ac4hHOcdPMJU9hm3-91PqnIi0UbEAoXKU0E7zb7RqNu1-jMuxlwJN6lRXHetjJ0BmczhE55F7P5Wi-VJTExJoQSsVqhbmZEuLm96ky7BGoIeJ3uzRoZHlzIoK09X3THB3chHCfCB2DtLc94rWICyPIMRhV3coaXHSagk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5462" target="_blank">📅 18:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wk9rGK8Y3tCmfStrC-MRSd-SRbRYPLfygP2IutXM4ONUz2qAbv2iMph1bS6vDRgKuJnHf_0f4s6_HyP14vKw89WGL0v4DgoE518nKFDJYOEvEw7q8qOArN1RSBKbUAdWIvygb1OY30RBuEST7phB81T8kMyxPJln8FH6HkRGUGRNzxf4ks5OPQWthZ948Y5JyNZFdfO4tzQcExQQd9vOq143zIwcTrvhF0reC5Bt3QNtp7Bn9TVe4dEums0Zs-Vx0gQ9GAvZRbty2VATKv7q0013bMgHR9BWUpu0uNB1R0fk-3rmvbt1hEUNFeDPIQzuV2lzCf1-nVgXqqFWS2C07Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Decisions API توسط OpenAI برای اتوماسیون فوق‌سریع تصمیم‌گیری در ایجنت‌ها
سم آلتمن از عرضه قابلیت جدیدی به نام Decisions API خبر داد که ساختاری مشابه مدل سریع Jev از استارتاپ TypeSafe دارد. این رابط برنامه‌نویسی به توسعه‌دهندگان اجازه می‌دهد مجموعه‌ای مشخص از گزینه‌ها را به مدل Luna بدهند تا با سرعت بسیار بالا و هزینه بسیار ناچیز، به صورت احتمالی بهترین تصمیم یا اکشن را انتخاب کند. این رویکرد به ویژه برای کنترل ازدحام ایجنت‌ها و اتوماسیون لحظه‌ای نرم‌افزارها کاربرد دارد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5461" target="_blank">📅 17:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GlbC5LwEyVxvJ-ykdqWUM7sFdJ8vHgVxGWIQkZP9UD_o5M6hUzE6S8E9Wm6ri4OzLxrxADEtVwLnXZMAcTSoxL3hL0bn7lliDXnFVKJ6if6Oft9_m5-4PMJNAnPOgOToumkz1HR-VRbz7SccHgd6HJmhziQYjYHSTy_8sAmLKn-i6EXpHCxrqwtz3SMFL5h5okRzyOXQXZZpu2FTTgbkf5V5399FdoTFYv95uooy8JN9sIjHSZK5iJn95ay0eZjHU-j8lPSeg61fctx_lDj1kzaxjKQ2lGthGS616k83tFnYkTZ9Nlz2paalRUtHohO2D9RCKPLMXMhAsNHfxEocIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به قول Theo، چرا واقعا OpenAI هنوز داره از GPT-5.6 Sol استفاده میکنه توی چتش:))
نه تنها 6 sol اومد، بلکه 6.1 sol رو هم دادن و چت هنوز روی 5.6 گیر کرده
اولین باریه همچین چیزی رو میبینم حقیقتا بین کمپانیا</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5460" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R9YIMhgn7EYSyzhjh1NcJ2ePgaf5ZmCrF6kgWHl-D-MGmJvH3tZLUml2y2SiMarBhrEwkqtre5lUWb2EAss4GLx1R3483dkJ6-opfqAuPO_C_yzhBmSTZRp5ddvpAib1dybhFEBqZEzisDn0df2Fxi3k0nyqieQcNxSnRL_8lAA5ilz6FqInw2IFU4dZpI1EAqLCk6mjUIZiNtX181oqTAyXZmI9qbD71L-mlLGJGVyCELHonBdn_EiLNCZu_jA0t1Jvl0SvDRD3TS9XDK_Zmkd-Lk7K-fLJeb3m9RLjcbOxfP4pYSdNa9EnlMr34b3m6lNGQ6VsGr_7mxhjT2mVqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله ما نسل Z هستیم
😂</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5459" target="_blank">📅 12:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oQfD7EmExEjLl2aViEor7JHoAvZ0_9sr7fxfat8guyp1pRxKOtJlkfaM_m6ZmtcxbxxYg1AalEa99eaSquibjQN_eNGSg-SP9Q9QifV-NQ9_PRKR5q1YZKla5wmydL-m5dDRXUvA7AK8Ludib_rRGnt_gvFbYGu5AY_64uzVBBAiQj3J54Ny--eHaSC5HcZx89yeE4hLaQwwWhzZM6b4zXgZBsM2EjHwgvwo54rT6Lf5RmZLeU-LSETVPw4GTpFVdPwZdoZ9dpTgK7zf8CpGAfbLBl_LsCB9uaWODZ7BLb08Cnw2MWQAiki-BO5jmIfmeG2LQt0MjfcmY_HKiLPXIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate
توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب:
https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5458" target="_blank">📅 12:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شدیدا حس میکنم مدلهای چینی اوایل که اومدن غول بودن، بعد از عرضه یهو ضعیف شدن
مثلا هممون به Ox Alpha دسترسی داشتیم، بعدش که glm 5.3 flash معرفی شد اصلا اون هوش رو نداشت.
یا من به Qwen 3.8 preview دسترسی داشتم و خارق‌العاده بود. سرچ کنید توی چنل نوشتم از تجربیاتم. اما الان Qwen 3.8 max وقتی ریلیز شد هم از مدلهای Frontier خیلی عقبت‌تره هم توی بنچمارک و هم توی عمل</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5457" target="_blank">📅 11:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/foQdDorZObcEaHf0JsT3l5Zd3PC8nj0Lgg6rhRq5aNO59RwgBa90sKjOAM2P_3aGQ3gTtCngMjSo9W-fS1p31-399Zzj5uS5QdZ80V--hfW1Y2Pz6jtnd81dmKC8VIWaVyEboi-_fm8r7fTlIae7q0A_9iMfTaC3mmO1PzOmUOAn_upcFh3Cyeb3xKmRJS8Wu8ff5bJiiz5msqHE_-EO7Aere1nY-sSqj_9TRXq-PlC08K_GWGaWJ0oGU5xkCP52DuKitnuXwc7jlCl6PRVKqvnQwE3TktH3sXh5eEE-v-c1zUpR_fT_FSmzdVZvMf5eGraQMNgM_1Dn9MIbWhnZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم به نوبه‌ی خودش عالیه
Hallucination یعنی توهم زدن ai
که این یعنی جمنای 4 به ندرت از خودش یه چیزی رو در میاره</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5456" target="_blank">📅 08:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کلا هر مدلی که میاد
این قضیه‌ی Benchmaxxing پیش میاد
نگران نباشید
میگن توی کدنویسی اونقدر هم خوب نیست انگار و باید منتظر موند و دید تا فردا پس‌فردا که شایعات و تست‌ها به کجا می‌بره ما رو</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5455" target="_blank">📅 07:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qr-eXW0PvRJ7qYGzmrHL9FWFaIW2qq8JpZnsc3JiQtgCJ1_3d67lsTsw-a3m3fUkoTBdxQz3KHqxnBb-a5M1YEWpHVAJpsuKv2_yKz1XyFVeYqYvz5-CzX10s2J0UeRzBdiiP2kWJxapNxGkQStDBmAlvKiP-0VO-O0ZFYfNxaRTo6glzXJ4Ra41bP13t6RwvqR9aU9U_OdcaRrNXPhSSn-Po9R6tZAY3OTS-dDEGDeKMuTW7Gd7WTpU2EhZqbWQUPKPYZVMZfneF--ZiNH8eQJfRgeBud7QEd3o3jOpqoGciNA5Clg-KR09_5VY64LWzKWkHsm7f00IHD0LBYRQnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uJLru7fdQbDPnLNIPFdyRCz7bGAVgHP3_j0YO0rP2yEqbfIY6B67IateaH-r3YKkOgG-ORTEsGjriqyKG187WpgZ1VvSNCKjRR-dmzph73rJAYYTetpNqwtKEuH2HyZgjfGkEqLp_p1B1ZVOUQP2v6YeSyVWOwMJUIsqqWPJSfLXa-fMdDAgHIvmCIinFoZksATX5yHcvlruuWj4dWOLBpzg3ZzDbO1LQVEqklkKicXR2q0_qN22Bq42HTpW3HDIkto0byHpQpBl5cGigGz3UEsKmBgIx1uLrSck23odYN_w5GUwZ7nMYydyLowHtBwVleDaex4-EcOiwYpM6jBdow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tG8NhSU2M20mCxv7nRq7h4zhgvkl_z9UJoNmXc-0U5lzxHx8S_V5PWKRBGZUsB7l5A2seYJhA8yAJp8WNTUV57RAlHTawIKzUrSU5h-83uf-5JInUdWfrqlSPOTluTkmL5z587kqCjOJvxf-xZSz0KJ8xqeFVsGG7gWRqcvkeInmbRoYOxmcwgU-m2wIg1aGl0NmJklsMWF98r63kVTcw7iSaFI0rmsLOz6K8oJCQ2OGrzHjzDxawj1rYHVyTnom02hXL7hZxwu0Qv91D3YW1X38HoOtmyunw_m4EwWGyyrKWxH1r4X4e2C9sT9WLhzss2D13NLmxYBjessCsgA0YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/o3e7K7omlublrwT3Hhtpas4-b6SGfldYgiqCrIyFoxup9O5iuG5fvXLvRxupfO5G4AD8m77SQMPM7BTymX6yVPICMKDcfdjMpnd-bDx9K2iMnfCgkJer6VIi7Hh2yL9NNK0Dw6XlrdVMQ2TBngUeWLczA8dvANCCONGlA0pb9-Bix1pq3_RzNWR5jXSy_mcO8hDvw3hkNsLzceiEoXhlhjcNRmQtc4ZZXYkC9Qo-Hp1JKBerZzZIfar0VAVPbkqjByx2mpzEZviDYsxhZq8rsPlNq7DBzmBCdokYyaPRCJj7w1D-oxFU2ffo4eBd8GKvcuVoKwD9F8CWy0ay735O_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری  گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5451" target="_blank">📅 01:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=odhMFU7fJLC0TUqUsp8v7mJtcFULOzyqxsqDzUAlxtGf6mAE76noIXYwSD2lUyBuQwSIv8bs03f3_eEYL8L6Jkb60O1rm_XCt_0_l4qQXYn7cElqdOWUrWRAbDpn6UEpstuvL3c_44ymfxFemH0qGZGVlyY8W0LmsC8OFY4jebkMJLfdVLmN0TaR1tjfKGoyqSCYMLRQT9x9qU0PMnXNYEhCyrbLpS51wawZjw87nnxsg45kdSvoQB_fJkRQUokNrjDkEHMo4Ov1XiOq5uoSqopIzGPH1widK6l7tgK4Tyyep4WR3VAzfmjZSR0wO1UUCwl5lBUIQbppv9fiDXzjaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=odhMFU7fJLC0TUqUsp8v7mJtcFULOzyqxsqDzUAlxtGf6mAE76noIXYwSD2lUyBuQwSIv8bs03f3_eEYL8L6Jkb60O1rm_XCt_0_l4qQXYn7cElqdOWUrWRAbDpn6UEpstuvL3c_44ymfxFemH0qGZGVlyY8W0LmsC8OFY4jebkMJLfdVLmN0TaR1tjfKGoyqSCYMLRQT9x9qU0PMnXNYEhCyrbLpS51wawZjw87nnxsg45kdSvoQB_fJkRQUokNrjDkEHMo4Ov1XiOq5uoSqopIzGPH1widK6l7tgK4Tyyep4WR3VAzfmjZSR0wO1UUCwl5lBUIQbppv9fiDXzjaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5450" target="_blank">📅 01:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/goHt8_BTMuNmIWUZxApVazPxJJhxuSMFOoCSa5VGvNu12j6uSqRUIOxCcI_HwtEAJJUolks3MQibSQ-DT7lPWQZZHe0uD1K-gsr2owroznn3iFQdwGhQ6R4lVn0Ahx4PN22OrdGArkTUZWsiM1uItBaICp0qw85UJPEBd35-OrbMaSst9Kxy68k34-rIgVk_ddQnJfoU3Htdfngm-U8SYf5IiiM4F83JCMPpKOx4t0S1xeK07AYUp0Xfs18KjLDa5M6569_bs8SljAydVv3_vsgcjaqPuBY4nXvkExebOc9vug2yz1k-Jwkywp_Jrc5d12DuOqD1cqw6F6L4Szy65Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری
گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای اکثر مدلا) تولید می‌کنه و توی بنچمارک‌های مهندسی نرم‌افزار (امتیاز ۷۷.۹٪ در DeepSWE v1.1) و امنیت سایبری پیشتاز شده که به زودی می‌ذارمش. آرگون با هدف کارهای سنگین کدنویسی، تحلیل دیتابیس‌های حجیم و کشف خودکار آسیب‌پذیری‌های امنیتی طراحی شده.
هزینه‌اش برای دوره معرفی، قیمت خیره‌کننده‌ی
2$/10$
و بعد از اون،
4$/20$
اعلام شده. با 0.1$(بعدش 0.2$) برای هر یک میلیون Cache ورودی
دقیقا هم‌قیمت با Opus 5.5
باید فردا ببرمش زیر تست ببینم گوگل واقعا پرقدرت برگشت یا هایپ الکیه:)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5449" target="_blank">📅 01:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بیدار شید بیدار شید
جمنای 4 اومدد</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5448" target="_blank">📅 00:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BXZ-9vZ7gB7xIWW5-JyBb43SuCFMs5wB53qEyaiwBdwkh6W-aM7Y-ISIYIZ09JbxecRaozIX0WIJBLzEkX06wxWMyZTLa6osuw3KydzX01pMylV2vkViT5rFy7MbZ_sRegeXLj5DI1Ad-Zfwm_b5Ez_oKztqPDhQi3ZMf3FcKTCqtL94GG5kmOZXXRiqevxKC_xqDiozP4lGP1G_U2NbF9fQ6yApnjCVJ3fxkViM12yXiHwl_MXYhMjJEAO1AW5p7b0rboBs3duxQdlSbjVRyZjTkMazOSWUYgDt0eP4MEyW0rC63XZMgXXRsAY-cbbvVDiFdyXj2bCSmdYk1NU8sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش هزینه‌های هوش‌مصنوعی با Auto Router در Cloudflare
کلودفلر قابلیت جدید Auto Router رو به سرویس AI Gateway اضافه کرده. این سیستم توی لبه شبکه (Edge) پیچیدگی هر درخواست رو می‌سنجه و به‌صورت خودکار بهینه‌ترین مدل رو انتخاب می‌کنه؛ یعنی برای پرامپت‌های ساده مدل‌های سبک و ارزون‌تر رو صدا می‌زنه و فقط کارهای پیچیده رو به مدل‌های گرون می‌سپاره تا بدون افت کیفیت، هزینه‌های پردازش به‌شدت کم بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5447" target="_blank">📅 23:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">من معتقدم با مدلهای رایگان، مدلهای چینی و ابزارهای رایگان هم میشه به خوبی کد نوشت و ابزار ساخت
و به زودی برای اثباتش، یه سری کار انجام میدم
چون میبینم دور و اطرافم کسایی رو که هیچ کاری نمی‌کنن، تلاشی نمی‌کنن، به بهونه‌ی اینکه من اشتراک Claude یا GPT plus ندارم و...
و این کارو انجام خواهم داد که شاید انگیزه‌ای بشه، و شاید ترغیب بشن یه سری افراد که شروع کنن ایده‌هاشون رو بسازن</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5446" target="_blank">📅 21:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ویژگی‌ای که Dots و Cues و Grok Bot دارن نسبت به هرمس اینه که اومدن قابلیت‌ها رو محدود کردن!
بله درست شنیدین
همین محدود کردن قابلیت‌ها خودش فیچر خوبی بوده(برای اکثر مردم و برای مارکتینگ خودشون) و باعث شده کارهایی که میشه باهاش انجام داد ساده‌تر به نظر بیاد و سرراست تر بشه. از اون طرف، چون با LLM خودشون سازگاری صد درصد داره، به 99 درصد ارورهای مدل‌ها و api و... بر نمی‌خورید. VPS هم که نیاز ندارید دیگه
اونور قضیه، هرمس به شما "کنترل" و "هزینه صفر(روی لوکال)" میده که اون هم ارزشمنده برای قشر عظیمی</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5445" target="_blank">📅 16:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بچه‌ها ما قراره استریم داشته باشیم راجب دانشگاه و انتخاب رشته
اگر سؤالی دارید، می‌تونید به ایمیل matinsdungeon@gmail.com سؤالتون رو بفرستید با Subject استریم
روی استریم می‌خونیم سؤالاتتون و جواب می‌دیم با مهمونای گل</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5444" target="_blank">📅 14:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YnQ86LkbFFC2W7rk_qWOQag8LBsr9MY4U6p3psYY3KzPZcNWN5LMCRA6nqrDktPODLFTRpuK-6XaNTVX5ywFq3XHQIvIFgNQHjvylNcUho5ria8jrj-TMW2XxadN88IflM6-_H7vYmMYuhOqOkPe8vdRc3Z6YK4lsTutd3-YxHfOmhD0dzR6SilaO3X26XTPA8x3OQ_uX09tt4w50MKu2aN6p5ljiIKg9buA70bst9HHPaQguFKAUK7Y5f1iphc4Kg-LIvb88zuguCZkytKad8biHE82tsULXB0etpyzZQJSXaitzjZkSUFM2WQp5_I1kQuBvecjWDlHsEKDsf7-xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری رسمی OpenAI با پلتفرم Hermes
در اعلامیه‌ای جدید، همکاری رسمی OpenAI با اکوسیستم ایجنت هوشمند Hermes(Nous Research) تأیید شده است تا قابلیت‌های مدل‌های جدید و ابزارهای کدکس به شکلی منسجم‌تر در اختیار کاربران و توسعه‌دهندگان این پلتفرم قرار گیرد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5443" target="_blank">📅 14:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بچه‌ها پدی 2500 دلار کردیت OpenAI داره که میخواد باهاش یه اپ بنویسه به انتخاب شما
رأی من زمین بازی سیستم دیزاینه
😂
❤️</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5442" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5441">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-poll">
<h4>📊 کدوم ایده رو با هم بسازیم؟</h4>
<ul>
<li>✓ تمرین انگلیسی با Shadowing</li>
<li>✓ زمین بازی سیستم‌دیزاین</li>
<li>✓ تبدیل کانال تلگرام به وب‌سایت</li>
<li>✓ ایده‌ی خودت رو بگو💡</li>
</ul>
</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5441" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QQ5y_1NsYYMQA3_N_XAL4wq_anxTaIs2hpZ6IMj9O6LmOQPjLI9EdmJMolzC-JZuD_jUuO_2cdbQRH2YoUHn3IcCfE4b0S9jIJXzaswlRV_UVHi1L0WljmVdbPZId8VjKtC-hS57y1w8HPB7B4WFmqcxn27XSEwHGEspPfV_11RfPI0-Dg_ekzroxbyauGHwC59AIPbF6rTO1ANdQ6F4giPEZrlPqrAzGEZzryri4df8qnrflxodN1q-EzrZPl08VQb6_grew6l-FID0Ncc9f5nMD3kh5TTOcb7jhE0vWx6MCxO_oVx7LR4K9V5bunSvIxQ-GJod-CJ1e0DHgH6W5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gv9yHs1GzC9DE4I2g2qKlYSokM1ZNzfYDH7fffWjFRJ6j7TufjwtLT6KBZ3DnaKe7FcOvj-rem5XQenKp4iiMhTKHcAaSnV9u9QV7KZoPKghA8Km_hz9ylGnKAb37-dpDESWm37Hq5oSjZ_ehtXYBPn9SPDmff4mgtwJDroAqRScZECOQFhAedJtaDWn4vNe3dbPeD35WKSY0L-hzy4TzOITkTFTN2JfWz1Z9QrDZTTBVF9Mb8bS2yuW8ahWo-TaK8H_0enspjumeJWEj4qRnKLDY34N_DniV-zXLAC2ymFwfcXDgMbEdsH-mWEETlsyB6iS0jbQgbPX3AqhtdD1Yg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قبلا برای این کار شاید 20 دقیقه زمان می‌ذاشتیم.
پیشرفت ai واقعا عالیه</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5439" target="_blank">📅 14:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5437">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pGZfd9R77Lvzmqvmp-bfZK5gYD3hWIDFwf5gWsv-xM-OyIcC99iFijXhmMTXPpQtB-yrCG3bgDlkGw1A-7Mjepo00DAd3cw9AlrCMGlA1Agmk7-u1d6V7Bb4jykQT4TklmAAR5UC2KXGkDCk_Ak0utTrcIaYz84V9R10FyKz6TZKBG8cmW_zexjT6yJxCzV2kYPQWqVTOJk3A6ftPN35E2UZe1QCd9aasSoiEM3bYT86RTMEQ9OzabFwQs1pP8QSss8TcFfieucpIks6SuthCD2h7hS21oE0VzGXktVB0H5v94FXGbQdPbRVrWBO-qOyUPCwSmlDBYuIkU-7iezF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PPAh_aaRQ7tf-woKuum1j-VkRn_qWl9GcoxbPdjKdGt7fS66tfTIxxps8hnRWhLeVGPOyUWyO-ysrnvEhp2jF_zRog74xLc7XMCw8G_vNSjuHQ_0knSRg9to513YzYaQicXsmOwo9lctJcYzHSyjpDveNWXYDNKFTUPwtkf-pIJlUAsPcwkCi4SArs3lWqwlG4hqXXbIjS18kpe6BISwMic2TNa4LCsouNc6XUy2zXWyBBOaj0hINOk3OQenrVoQflCSWbfWgyxN3FotK-qW97QCKdt1ybPToN7KTpovQGpNyl0wvAaJEDAbXwDSA25W5yCdsmmJIHUC2dr_wh-Qiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز Manus پلتفرم Cues رو رونمایی کرد
چند ساعت بعدش، OpenAI از Dots
و طراحی بصری ساب ایجنت‌های بامزشون خیلی شبیه هم دیگه‌ست
😂
نمیدونم چه توطئه‌ای در کاره</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5437" target="_blank">📅 12:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گویا همه روی GPT 6.1 Sol مصرف توکن کمتر + قدرت بیشتر تجربه کردن</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5436" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">عرضه نسخه ابری OpenAI Codex در رویداد DevDay
اوپن‌ای‌آی بالاخره بعد از شیشصد سال که رقیبش آنتروپیک این قابلیت رو آورده بود، توی رویداد DevDay بالاخره مدل Codex رو به فضای ابری آورد تا توسعه‌دهنده‌ها محدود به اجرای محلی روی سیستم خودشون نباشن و بتونن از راه دور با گوشی یا هر دستگاه دیگه‌ای ازش استفاده کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5435" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=sj5vIEJ8XtsQCzdrY00LzGwFp9KUbiV53DRwVSXsH9N5cA3mKjK6KF_BgsAKU2C6IaqtemDVGlESx5fF4smRZD4Eo09o3XLuIVKoDt1Z4CnrJGn2Bub72t8ijL0da2KTm1TwRWXp9u74IXcJP0XkT0-2WFUJ2Kn2WNeEZg0F29pGQFqxbJqiQSJ1udeBcxkJPGPmrZrFpZHF0QASyu_qWh_qy6Fz2PXz8_sR2EBYQ02CjF51m93xshS_izleqK65HYgAf_teaFXPzXPydrsSWCpO6n1lwH436AqPUrmMxp78F7D5V1TPZDg7EypIc6me8uSIqxnIkbmauTvSl9w89Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=sj5vIEJ8XtsQCzdrY00LzGwFp9KUbiV53DRwVSXsH9N5cA3mKjK6KF_BgsAKU2C6IaqtemDVGlESx5fF4smRZD4Eo09o3XLuIVKoDt1Z4CnrJGn2Bub72t8ijL0da2KTm1TwRWXp9u74IXcJP0XkT0-2WFUJ2Kn2WNeEZg0F29pGQFqxbJqiQSJ1udeBcxkJPGPmrZrFpZHF0QASyu_qWh_qy6Fz2PXz8_sR2EBYQ02CjF51m93xshS_izleqK65HYgAf_teaFXPzXPydrsSWCpO6n1lwH436AqPUrmMxp78F7D5V1TPZDg7EypIc6me8uSIqxnIkbmauTvSl9w89Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5434" target="_blank">📅 08:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">حس می‌کنم یه رقابت خیلی سخت بین سرعت ریلیز مدلهای جدید AI و بالا رفتن قیمت دلار شکل گرفته</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5433" target="_blank">📅 08:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5432" target="_blank">📅 00:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مدل Ember-1 از Fireworks: کارایی Kimi K3 با 40% توکن کمتر
تیم تحقیقاتی Fireworks مدل استدلالی Ember-1 رو بر پایه‌ی Kimi K3 منتشر کرد. تمرکز اصلی روی حل مشکل بزرگ مدل‌های reasoning بوده: تکرار بیش‌ازحد مسیر فکر توی خروجی که گاهی بخش اعظم هزینه‌ی توکن‌ها رو می‌بلعید.
چیزی که من خودمم توی ویدئوی کلاد رایگان، سر اون بازی سه بعدی تجربه‌اش کردم و واقعا افتضاح بود. مدل توی thinking خودش گیر میکرد ده‌ها دقیقه.
امبر با بیش از ۵۰ آزمایش و ۲۰۰ ارزیابی جوری آموزش دیده که شاخه‌های غیرضروری استدلال رو حذف کنه و بدون افت کیفیت و دقت کدنویسی، همون نتایج بنچمارک‌ها رو با حدود ۴۰ درصد توکن کمتر تحویل بده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5431" target="_blank">📅 00:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5430" target="_blank">📅 22:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن
به اسم Dots
تقریبا شبیه Muse، یا Grok Bot
https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5429" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5428">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HoNddHq02I98kwOvQwFRMV7g1H_Zd6-vt-mhGj4TLY1jfCVgDJv05cCrkI-Mdq1f4n5iO3orBPOqEbxP5jAEaPeiz6esrig4v17UF7HepXE_wDAHxh4iOIb0e1e7Rpanp4gi0X2o0PEEGO4dm_N-jhjr4-ZKgtfX10PMphJVukmVqvvZSPiZF8-IaXi-xRNI3zo5xDVwXy22xDaqmV5VMwld2euz441AtNwmPQH4PmzYKBrqmcbQw_nt3zLjSIBwcFgA-5vovGLPHkcvSDrhAzzzH9lb8RjFmobWw52Pf9Zc9yD5JwmUg59qYG0IpyedhjVuY8KGSKWw03tKIi9_YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی خندیدم
توییتر OpenAI کلی گفته بود که امروز به مناسبت Dev Day قراره یه چیز خیلیییی خفن بیاد.
کلی توییت زده بودن
هایپ کرده بودن
حالا حدس بزنین چی دادن؟
GPT 6.1 Sol
😂
😂
😂</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5428" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/isEoceRT4TpsPvKUJif63GzruXC_RsX_L26OEDFU2r2KUoub6bPKvzs8qt2DGRb9jvVZC0ZTh-8z0aKt-EfcYquySdLzukNmr9P1dqSSzXYeigQsfl48kJ9KLgR0ej4Rtal2OZEJYgsdTv6c3ePDGTsx_vulVB82DOpYuxGVxZ3LsXT7wD6bTRC4yQ0_hDxZiguR8acGN9n5PG9GCnV7LNv7LrRv0dVcz8DrvdQHv1k3idjkhea8OUQc1u_TH4vyU6ceuHRF49RK0Bak2Khy3c7HMnPXn4X2ykCu0bWNM5iV5sKJ-iWiQCILREyQGbEhG9sB_QUQpnN1_BiQJIwIgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qIShtDFrXdaAvazv-vKcpKbCN5VXvvdF_m3c63eF_Grz1dj_K6NUopaeAenc6yffdF7TkRQz9x6vGfyu-_JLkbAGKxrrTwdAzVjNHsPp5mDBqZ5B2bGwvnqNKfaUfg5a5POMi-ECi4B91AsXqFBteiVmpcqQsB5Vu0LzlBz-PvVM0sxQ_pLOgNgzLhrDtv2chv-pA2jvLKuHrlV2yTdp2IFWqGQ_6-nmHgAH-MJ9-f2PRl6C17ZngxvEulIcfiql7kvC8VMEGTVezSV_bWmgOP7EX7rMcGbKKJ0pYOoQSuCDo3-kyaap5z_5hWb7uDDJ-h9_96vHk_igZhoDGlRuCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کلی ارتقاش دادم از دیروز که الان داره با یه مدل خیلی ارزون، کارایی انجام میده که Astra نتونسته بود. یه پنل تحت وب نوشتم براش که اینونتوری رو ببینم، یه مدل سوپروایزر براش گذاشتم که بالای سر پلنر باشه و تصمیماتش رو هدایت کنه، بهش حمله کردن و دفاع کردن مقابل…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5426" target="_blank">📅 19:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Aq8IFChWo8Wu3YDbBJCZ6ea8cqL6ziWNN_bHI9XiI9Y_DT-WXF7zzO3tOnpsCi0pZBUljwpVDSVYCX49G2oMU3tE_vEwL3mOmUdI70Ls6urlDFUD08aCi2JP33Wgh909Dk3HsqjJv4jdV9i2a8r1z75m6j4qnEuJ7JchOV1fQgc8s_Sb2lJK7COcfRDNK78J1treqpfpC51OgwmPIuqyQQ--kW_7LCiMr0NmL4yyWxY_bsRPuzo0ROuqofdJ-n696XgPFIm7_2NM_oFJPgWEMrg7qiEkL-k9yrn2trmecGQ5tb2s1dflc_mm6S6vdouz-em_QhxdiTmO9rQISxGScw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستیار جدید ماریسا مایر فقط از روی عکس‌های گوشیت می‌فهمه کی هستی
ماریسا مایر، مدیرعامل سابق یاهو، بعد از راند ۸ میلیون دلاریِ seed بالاخره Dazzle رو معرفی کرد:
یه دستیار AI که برخلاف Muse و Instinct، نه خبرنامه‌ات رو می‌خونه نه تقویمت رو؛ کل context از Camera Roll می‌آد. از روی عکس‌ها می‌فهمه چی دوست داری، آخرین سفرت کجا بوده و بچه‌هات به چی علاقه‌مندن.
مثلاً از عکس‌های خود مایر فهمیده خانواده‌اش escape room دوست دارن و چند جایی که نمی‌شناخته پیشنهاد داده
😂
😂
کمی ترسناکه حقیقتا
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5425" target="_blank">📅 18:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ایده بیزنس: یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال" قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط بعدش از…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5424" target="_blank">📅 17:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ایده بیزنس:
یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال"
قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار
هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط
بعدش از سودت برای تبلیغات توی کل شهر استفاده کن و دوباره پول در بیار
سرمایه‌ات که رفت بالا و بالاتر و مردم اعتماد کردن، یهو پول رو بردار و دفترات رو هم جمع کن و فرار کن، همه چیز رو هم بنداز گردن بانک مرکزی و فرار کن د برو که رفتیم</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5423" target="_blank">📅 17:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">در مورد آزمون تورینگ و مقاله‌ی Computing Machinery and Intelligence سرچ کنید و بخونید. جالبه. با اینکه انتقادهای بسیاری بهش وارده که دوست دارم یه روز بشینیم با هم صحبت کنیم راجبش
و دقیقا پرسشیه که اوایل سریال West world مطرح میشه.
"If you can't say I'm human or robot, does it even matter anymore to ask this?"</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5422" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یه جورایی حس مور مور میده ویدئو
از شدت پیشرفت علم کامپیوتر، اینترنت، ai و...</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5421" target="_blank">📅 14:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=GauyU0fpQYHhFKBTbpxmJOL2vtKgBOUETS56O2pdHdzGWb7ig98eCm7zNdrBX3Gi2jeXCW_d_YuBVkp2TTXD9O4LUy5gbZ3QXcVL_sUhTiKZxno5d0edq-dKP9uopCvb_L2rnrpMZTRrhfVVlj00TxS00dJOxNtGLf-kqCEbw2AXb4nvRVv8JH9NyWMJ_Hvd7S0zqmSzBZUt6yVSjvHc2uzhEzMsV2Av3-uv9mWLmvuqStgvwDr61IY6rDyQeDL3yObLO1uEBFdyQi-vKSY5JuQwvzpJAryYpvFCcZzZw0d-PJgXzUPTjXWWER8TNwU2USQCbfMi2NaplmmIgJdeLw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=GauyU0fpQYHhFKBTbpxmJOL2vtKgBOUETS56O2pdHdzGWb7ig98eCm7zNdrBX3Gi2jeXCW_d_YuBVkp2TTXD9O4LUy5gbZ3QXcVL_sUhTiKZxno5d0edq-dKP9uopCvb_L2rnrpMZTRrhfVVlj00TxS00dJOxNtGLf-kqCEbw2AXb4nvRVv8JH9NyWMJ_Hvd7S0zqmSzBZUt6yVSjvHc2uzhEzMsV2Av3-uv9mWLmvuqStgvwDr61IY6rDyQeDL3yObLO1uEBFdyQi-vKSY5JuQwvzpJAryYpvFCcZzZw0d-PJgXzUPTjXWWER8TNwU2USQCbfMi2NaplmmIgJdeLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«کلاد ساننت 5.5 این رو ساخت. فقط با کد»
این داداشمون
این ویدئو رو توییت کرده و اینطور گفته
ویدئو در مورد پرسشیه که آلن تورینگ، پدر علوم کامپیوتر مدرن و هوش مصنوعی چهار سال قبل از مرگش مطرح کرد:
- آیا ماشین‌ها می‌تونن «فکر» کنن؟
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5420" target="_blank">📅 13:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=g07uBKPwSoPJZesf4VI3bOasC6upxZ1EjIFH0yiVQAfyuRaj-IUDBswT8roVKB0kiA1GOsZYxHaieKqOWSyqA2HMzB5KCE0cwdI-P5O8tLrEz90pwzms-PU5KyOlx8BTKVPcGnF-pHi8fmTGeGAufgNZy5OxeaQmhsWN5gXzKz8d1WistOfhqJvgPyySstYiyqSTNw9VkzVjOfcCBJUl9fCuLBWDhlHfX9e4451NfgI1nPX8vuiEDqKaihbWf6J1yhO40hztY-Hs67cag-b4-F5bEgmZXBl2yMtMr-uoJtH6Wx40oZSiv16jsWzGuz1-F0b0ujXNLT4sZDVEmn6Ofg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=g07uBKPwSoPJZesf4VI3bOasC6upxZ1EjIFH0yiVQAfyuRaj-IUDBswT8roVKB0kiA1GOsZYxHaieKqOWSyqA2HMzB5KCE0cwdI-P5O8tLrEz90pwzms-PU5KyOlx8BTKVPcGnF-pHi8fmTGeGAufgNZy5OxeaQmhsWN5gXzKz8d1WistOfhqJvgPyySstYiyqSTNw9VkzVjOfcCBJUl9fCuLBWDhlHfX9e4451NfgI1nPX8vuiEDqKaihbWf6J1yhO40hztY-Hs67cag-b4-F5bEgmZXBl2yMtMr-uoJtH6Wx40oZSiv16jsWzGuz1-F0b0ujXNLT4sZDVEmn6Ofg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Claude sonnet ۵.۵ توی بنچمارک Terminal-Bench 4.0 نمره‌ی ۷۰.۶٪ گرفت.
بعد این پرامپت معروف بهش داده شد:
«یه کد به HTML بنویس که یه انیمیشن دوبعدی از یه پلیکان سوار دوچرخه رو با گرافیک SVG نمایش بده. نیازی به تست اضافی نیست.»
توی حالت xhigh: یه SVG سالم توی ۴۱ ثانیه، به قیمت ۰.۰۵۷ دلار.
اما توی حالت max: تمام ۱۲۸ هزار توکن خروجی کاملا خرجِ فکر کردن شد، ۱.۲۸ دلار سوخت، و SVG‌ای هم در نیومد.
گاهی سطح Effort/Reasoning بیشتر، فقط یعنی «شکست» با هزینه‌ی بیشتر.
پس الکی درجه‌ی Effort رو بالا نذارید. برای مدلهایی مثل sonnet، همون High-medium کافیه واقعا
🔗
‌
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5419" target="_blank">📅 12:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DJ7NLLC-7rShOagXT35-nbE5VKFe8IPhp8qT09CF6TL2fBWtVANFEW22Vs544bTUTmMNdfcE18txp2f-CIGscb9Aklj7EqPxtK1wvKI7427yNjJWVeZ6sCDrF-zvVbySHUIOHQrZlzHQMYvVRTG8Zu7lvA_ygibJLZmo1yY9Z8opmvr1LEZh_v2idNBOQGMbHUJ2W04Il8PpBoFjT8kHTRlSk4bv7Iz-n2EUbeQj18VK4pRIX25RwmLh6Igd85FPNv3d2jGqoerB-GC7YP7-CnjpvStGKrW9w7MbNPYdjD7MPYhi8g6unthrcD0b2M6k-aRURQHGoHUAIa50kGzJTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J1gBF_arhKeYQ9Ef_tvHK2ugyVFkqGS9OUv6NuPAd-1TTsszwz6SOjL_yex-5JwVNo7ZiZ_uNO6T8-oPd6SE7R5UTMNY_inIX4-F3P1zKDXfj6jpgTuIPqY5TdzOmezSjgpWe8LIe9V2O0XDVlNy2gMlWEMN_G8RJ9jWVB9pYKbpROid9YfPqJ5CP4RbXcF8cRpq9TGBkMydHmw59xGQi4KYVs89FDjC7tYQN8YEx3CjREjTcb7VZgxDJSZm5wefJq4ho_DcyUzLh-JhylX7I2Fkj5WlPw1X3LcaY0mgdJImrdxbESSangpJanJAzySKmScW6m84h4OwnO77rtDliQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این نسخه از WhiteVPN می‌تونید مشکل فیلترینگ ورکر رو دور بزنید</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5417" target="_blank">📅 10:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5414">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5414" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bExxsA38eFZCfIKvJ1aUbLEtAj1NhKXLQuNV-cqub_o3elKnbbSt7cQB_OfutD5jlcVCP-rm9H4qpRCiPXXXyY5Mnu5O-mYZQ2114zkt9IVxl12Kj-yW3-HUX8QanFJVd3N3A3vzuxyN6xYu6z_NyP2u3NUGucT1cHFZGbPHxYk2TsajDphHs8ch9DY8Kd6R7LsmhTcchjNFS4vFUchBIZqseOmpIGsradGC8L4sGpjdKjFjU3bMwm7Ykyp2b_afQy0wlw-XqLA39wnmEUBaSjON_kZBQm-EXVBdbZ26eAmNOKL-6tFBhuD0VrSJ_HY9Q1XHTnQC6hcRlNG4JVE4JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید WhiteVPN منتشر شد (نسخه 1.6.10)
در این نسخه، مشکل نمایش وضعیت «متصل» در شرایطی که ترافیک در شبکه‌های دارای فیلترینگ شدید از تونل عبور نمی‌کرد، به‌طور کامل برطرف شده است.
تغییرات و بهبودهای این نسخه:
تأیید واقعی اتصال:
وضعیت اتصال تنها پس از تأیید نهایی دسترسی به اینترنت آزاد و پایدار ثبت می‌شود.
سوئیچ خودکار هوشمند:
در صورتی که سرور تنها پراکسی محلی ایجاد کند اما دسترسی واقعی به اینترنت نداشته باشد، برنامه بدون وقفه به سرور پایدار بعدی سوئیچ می‌کند.
بازیابی خودکار اتصال:
بررسی‌های ناموفق مداوم پس از اتصال، مستقیماً وارد چرخه بازیابی و اتصال مجدد خودکار می‌شوند.
ثبات سیستم امنیتی:
حفظ و پایداری رفتارهای قبلی در بازیابی آفلاین و مدیریت خطاهای گواهی (Certificate).
افزایش امنیت اشتراک:
الزام و اعتبارسنجی دقیق لینک‌های اشتراک خصوصی در بیلد‌های رسمی برنامه.
📥
هم‌اکنون می‌توانید نسخه 1.6.10 را دانلود یا به‌روزرسانی کنید.
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🆔
@Whitedns</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5413" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BQBV41grBpMgQKqG2u2bi-gJY4lgdm8g2Ne6vbvVuIhq2gsFlM79ODsLzrfdhmzmsTXsrpHUYs0gdzluOoSAGM5f6rdri0PLlOhPXFxVNxoZOQeZB36qhwxmdcxIjZFkkPLYS0sV3JcqgT7t36JWJ2kyVQ08sdzyQt2gljslobDfjh4a9kJhQtqU0cks6_OILbO7BgO9_iKCqvjG9VV9AMZVKiNWWhz7ILrpk_91s1SbHy_cUVaMsEFbYJvy4i0yxva4URWvQ5p1TF8mEVEdxhUG7RTZj-h-K-YT1W39dWLrkZmROFJM-L-EIrFbHJo69ZMnDM428BHZbBdnX99mgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10
اسکیل برتر OpenCode
جامعه کاربری OpenCode فهرستی از ۱۰ ریپوی برتر Skillها برای ایجنت‌های کدنویسی جمع کردن که شامل پکیج‌های اتوماسیون تست، دیباگ خودکار و سینک شدن با دیتابیس که کار روزمره دولوپرها رو خیلی سریع‌تر و روون‌تر می‌کنه.
(حواستون به SuperPowers باشه که خیلی توکن می‌بره)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5412" target="_blank">📅 07:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">Matin SenPai
pinned «
اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید: https://youtu.be/dQKfkXnThCE  به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5411" target="_blank">📅 03:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LGO4ljrqank1_oPcr6S4EomFEVPvIJr1XYVeRw5GH98oW_HgMGUoNf8AkzfoivGwNJkvbc6zO-F4b70CoJucs03KMlY2yIIMp5Ckp9B-67CkkbdC1jSHNM4x5Ipg60Qs2Q3BJhhGhEkxOgWReKOHk1IyTs3FScVM1ev3yyvudA9s6_Huzi2kgo0DTNrAIlj0rETREjod2aCm8-tA0pTNt_MVR9cf7ahB787nVRHfynrCLfqN-RK8x9h98sQhLUazZHmIM3-Y_QbzfYxbUVz3kCsxznvAYpBsXavIYJyjSfu5Rph2i5Swzig63AVUkTxQNJFPOGkzwSjy9XoNE_aX6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5410" target="_blank">📅 03:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tv8XxVMfjAbC81ZFTi_1bBuMGUF7EAhfC07Xmdnbx4JR7S5Bma-zMLVwZlib5_ak-Di1wIca4LzPPOw2jWEAv9gBxYEYKwvBNAm16o4jdKhFuJJYVIeIH-5k7w1QCSPLXxP0PYSc6YftEPU15epGAuYn46EE53OH8GgagmUAPcUF3UtvQhXuq39MnsZzAHvMnTa1d2xx7-AANjiJIdDZdbQ2lVpqIDzcBXGSy1Uc8Ex_nDRxA3PDUOr58TGZgTL1P-hBsK_WDeuu55p-PzRF7I81Z_0TcxS-xVW-WRNK4yTVLy0ZnXJDO1CBKLOUWaGaycMkCcBN_Dwyc65BBB_gIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5409" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">هرمس خوبیش اینه که سمجه. اگر از ترکیب هرمس + مدل رایگان(مثل mimo) استفاده کنید، واقعا غصه‌ی توکن سوزی یا انجام کارهای سختتون رو ندارید</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5408" target="_blank">📅 23:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مدل Claude Sonnet 5.5 معرفی شد. هم قیمت با GPT-6 Sol، اما به شدت قدرتمندتر! نزدیک به Opus 5.5  • $2/M input • $10/M output • $0.20/M cache reads 1M context + 128K max output
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5407" target="_blank">📅 23:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ftbWYtgI6mwCue4IKzHg0oOBMh1Y8MSjH6r5fexwsIshLPUPAD05erwqnpQaElD6ap76eWM3tDl3r_HcujN5-VxOuebH5wz4eshz6WC7DdEno_3i6Ey39iVeEf8jNIoP6BRmxnlKG5Ch9UcTXPDv1mDqOhErpq0J7xi4yRQOxnu-7m__-4GyGpt441qtMbO1eF67YaMgs8swndcWZY87XSirltutrJHcURCnBrj2PGaBFSvJnefO1X5QWNZCXO-nqmdIvI13Q9_bdd4nRmy4pPab-yge5HIQzUIgrwMJObSE_ZBtQ5LBw23ljPfQ_dLr5evl_HXJCOglGL3JgUiNDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RHV1izdeLb1NWABpscDvT08BGcl4PXDG-2yg-wdbje2uRLwdaik7MNwtjOb27-3fD0MLvvfp2uZLI0O2or6gdJ2zh9a7r1sl1eCouhI7iqqa2_T-Qd7slrFZLiEMY-yZES1SBkO8roJ-VqknXjUH67YaM8q4qMEdoWEmAy36QvNwpPACF8HCu1BKnHSKCbZEU8y9UAJHJeOUIcrQ4L5Xuy5PIHrzvQMqpM5_9zYfFRp_zXurPJCGVr1ZCMW_1HoQdx-3tEUNUUTNkgA2vMlv87nsFxv1RuvM8uqXm8cs2yiZhcxOPYadXJgLe_GK-PJB4mPCluZeEcRfkouo1FE3KQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5405" target="_blank">📅 22:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5  از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.  هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید. https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5404" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82410567b8.mp4?token=WhaEJczGte04vTxUPuqMM-kgdIp3EHFrfNVRbVgWUUOP_1BMNYw0EpCDgGURymuoEDDrz2JepNXM6crI2L-MS93wCjxUE_C2YQIkyVLB49BLWWw3W2vGS1sLkaS6frjIVLS7YgCo5x2vLP-J4XqowEnr7HwmwkyC6jt8jQ6VKbusxiQEyBDveeqNFuAVio2FDzQaTU680tETwsbCHxCpuRbp4Da955GoRiV7d40mAix1RLleEaYQuddzaUWSoDeRAKywVTF2ch433CN9mRJJYe32zHr5L3kgJESalacj2dnHk14zjLnl2szFuYxgPigzq485NPM5bTznyN3MPDNdqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82410567b8.mp4?token=WhaEJczGte04vTxUPuqMM-kgdIp3EHFrfNVRbVgWUUOP_1BMNYw0EpCDgGURymuoEDDrz2JepNXM6crI2L-MS93wCjxUE_C2YQIkyVLB49BLWWw3W2vGS1sLkaS6frjIVLS7YgCo5x2vLP-J4XqowEnr7HwmwkyC6jt8jQ6VKbusxiQEyBDveeqNFuAVio2FDzQaTU680tETwsbCHxCpuRbp4Da955GoRiV7d40mAix1RLleEaYQuddzaUWSoDeRAKywVTF2ch433CN9mRJJYe32zHr5L3kgJESalacj2dnHk14zjLnl2szFuYxgPigzq485NPM5bTznyN3MPDNdqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5
از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.
هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید.
https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5403" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید:
https://youtu.be/dQKfkXnThCE
به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5402" target="_blank">📅 19:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vyr75ZEuUIorZolr8bOQfMV2JzmF25rAwuvjGL9xvFrlXZ8AjhNyDrD3_ghGkhpJWHoxEtqS9NOUWYwzn8STeh8JZhRrQZ7KdGK5WBxIvYffyjnWdZOr8e3LANAyx_Np_cg-dq2DmbHZIQDbTEZ2L9tSbCbi3d_BfKFVTu4raG15bFrg87bP734TTnA5-RUQQJ4XlksRy60PrYcDacmSzkeELZyrskmHxTtSJqOrpKjRAp4w0MzMweykCNj4EhO7Kihadv0yUVXtvz7E4ibhOqYPCWy4h2zmt0e9f4WAlZ9k9lAMGePeKJ0NCFt5rlxbLUDUOYIp-WJs0pxFK1NmIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه‌ی Hermes: از
MEMORY.md
متنی تا گراف دانش
نویسنده این پست ردیت گفته بودش که مثل خیلی‌ها به دیوار
MEMORY.md
دو هزار و دویست کاراکتری خورده بود (۹۹٪ پر و مدام درگیر نوشته‌های کهنه‌ی توی کانتکست). پس برای همین تصمیم گرفت plugin مربوط به ارائه‌دهنده‌ی حافظه‌ی Hindsight رو توی یه کانتینر Docker جدا راه بندازه؛ بعد از کلی تنظیمات مختلف، اولین اجرا و تجمیع گراف تموم شد.
که این باعث میشه:
1- دیگه محدودیت
Memory.md
رو نداشته باشیم
2- سرعت خوندن از حافظه وحشتناک بالا بره
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5401" target="_blank">📅 19:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QFoQMHB0INsPCnsxL-fBVTiwDYJ9p0vOqn_1zYeaAabwD_gm9Evbmh6pcETg_p9VzkKYjt6j2-Tocren3CRwZhspKMG1L-A6DmkY_JIWltp3izpHaVEpRf_3vapMALpV8byrARpF00gZWyqgX4IePGx_rn1yjTnqkLhMJL7P-LRF0HkQkCTaoQafWDFRZD1IRSXqOkB0gXP99ghxJnPVsaxN56M4oSvqts1aP1HI-CUdV_V6NnrILFBYJ8vuU1poOhTZDBSGZBFEUbmh68uzK31iJFaNjzqugXIpGATMuvSyiiWfLiy-k97Qz-45mb8t2Rcx6vdCL3rCEZk1vZ_YKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر کنم گوگل چند صد میلیارد توکن از نسخه 4.6 ساننت و اوپوس خریده برای Antigravity و نمیدونه باید باهاش چیکار کنه
😂
مشتی 5.5 اومد 6 هم به زودی میاد ولمون کن دیگه</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5400" target="_blank">📅 18:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TsqnZYf-o3AQtzuHsi2LiAkgGAOBB4jcOJiQpDAUQwDOCdu6yDzBnSixi95olMb3wxTo7Bs4JJANHwMQu_xEHQNvElsny2c-jTsFjWdCiWZyJi6hsN57vSDJDN3P73yDLlMjYpg4_0k1Lj47GWp_CQZvcrX_U3VfU-oHnsHusdB3xxJfMl2hZ8ZZ5_X1MHtoYHz9XOl3S3t3bFXQUkrzE30P80DCZPC1TREW8JAcKkuSGs7e9dM8n1vhMzac6_KsW-YHnoDlrwXWuAZ4rFcWg4_hBXHnu3A5217IQ0J32cvwozTpFekXJ2mwsdwH_M90TPrv1aKb7woa7FfXXv8cPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی ساخت نرم‌افزار رو آسون کرد، دیده شدن رو سخت‌تر
قبل از AI برای ساختن به توسعه‌دهنده نیاز بود؛ حالا آدم‌های بیشتری همون چیز رو راحت می‌سازن. ولی تعداد کسایی که حاضرن پول بدن، یهو چند برابر نشده. نتیجه: وقتی ساختن برای همه ارزون می‌شه، مزیت واقعی از ساختن می‌ره سمت توزیع، ایده و شناخت مشتری.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5399" target="_blank">📅 17:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UXaosq3uMBNS6EROd0nQlJ9BPEF6j1ABpTlJ97EAMlR9Kvv31qSa5J_x4m22w2CvQP2n6OcUJvbCkY7X4Py1AP4hXW4en8wllQRXCbyOsZxkp7jMOj8bEUcl6cw9YIthR-z02a08DYb3gXSP0DFMjz2Qz4ZuUFmIKb6YVzhdvCYIf1AMPKIBHAAEyL0pxI0ckX3voWm3F62cO3dCa1HUau2bhW-1BefoVO4TwL41u4Ph6iz4VO7tEemge4CEspPA5Q8BLCCGT4_-WDjMYktlm-_W20slsaEFdXTliodGEcw9TuBU70xinnIlJ4J9lm38udhB1Wtdb0Zmb_ybf0b_mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lpCZ2IKBJ_Qz5y-ThihULDTcJk91TiyO430XFS_LtZWTMdpg0FiAzl4A1yX5n355ozvREkksqwNQkdsCb2E5xj_neGm_7UzadbAj5p5244EOWwme8p82Hhi3YpNomYsKAK0WGD2MbIAgeRFkxFfyxkKI74mGRlrU7eE9lcr55bgRQq_0qyUZclps54-totYHuvzTB6wxcF2IoRD6w8S1odDxWVUTjVPSl-Vo4XbsQGOLCsNVgnkMo2OZ6Fw6hNGpDK9RWiaox6QRR79d4g2ZHUNXpR5AXR8v7rnU7rDTV1ZUEx8TgoD2lrdRSisUpRoXMPBlKC43FsczIvJZMAE2lQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این فتوشاپ اوپن سورس که مسخره‌اش کردن یه دوره، سازندش اومد توی ردیت درآمدشو از دونیت‌هاش گذاشت و گفت محصولم خیلی پرطرفدار شده
😂
لینک این فتوشاپ اوپن سورس که اسمش Photon هست:
https://tenzen.studio/photon
لینک پست ردیت:
https://www.reddit.com/r/SaaS/comments/1wsac6d/i_replaced_adobe_photoshop_with_a_free_better/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5397" target="_blank">📅 17:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست
با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5396" target="_blank">📅 16:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">محدودیت آپلود
۶
پکت رو دوباره دارن اعمال میکنن.
از چند روز پیش برخی سرورهای شخصی دچار این محدودیت شدن.
از دیشب وبسوکتِ (alpn/1.1) کلودفلر هم برای برخی دامنه ها مثل
workers.dev
.* دچار همین محدودیت ۶ پکت شده.
در نتیجه کانفیگ‌های ورکر کلودفلر به صورت عادی در دسترس نیستند.
با ech ,
fragment+fingerprint
و چندین روش دیگه میشه این محدودیت رو بر روی کلودفلر دور زد.
فعلا تغییری در وضعیت warp هم مشاهده نشده.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/MatinSenPaii/5395" target="_blank">📅 16:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H5SG6P24sDk1E2a1fml0TeaGzPn_eLfeX_m3bMLrP4M0t2k0Vx-uC7q8f7kmDENDgv09Xu6bbgVhqSzecEcM4--DVz2NOnVWqFIMITirmtckZjBSf_1FbFW25PWx4kJbtH711uWa27koDWZ9aWxIBtne2WfDbfm9aJUIbbD_htTf91snuDGGNp_c4t3T8bjMcFKz7dac0N25nVh8Vikmr62qRtGjPudzWk7xo4TseeEA81e_nBTNfXJqILSXYDZO5iyAj6Ai6x9b_xhv2pszUUyvp3TZHZfPzdUfDbsmNSttPdZGVDudwTJLGvsFENiMx66eO5yzNaxraHD9kEsd6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5394" target="_blank">📅 15:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JRfXu6ytmQCxuVc9OCQs2A7pX7vCtZ_G2j67cN7DpY-thK6UUBkXiKOTiLZRDHN3N9T0APTcTzlKmSl7S08w_2p0RAphawn8kYRzNMOoeD-6I2ywvUWEV3XFq4FP3jiAbmdAmbvmMhF518A2eD4dOyeCfy7rFMEJtrKYYJJhMWJt3USG_fBMPU6hJIVi3bzLKnPWdPD7sBQ-hrmDWdtm7sbiRh6X1meOIwA95iW0fHRPckbXxUB2RWuA24xqf8hIHjREzGJasiaEyI8g1h0JEhPJyCbTdznaQMlnpJraZ-IFjSd-djvZkPtsaMdAtLkC6xs2V4E3XOIfuNNSNd_9HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک خسته‌کننده نمی‌خواید؟ بشینید جنگ مدلها رو ببینید
🤣
سایت TinyAIArena یه صفحه‌ی ۸×۸ هست که چهار مدل توش دارن واقعی با هم می‌جنگن؛ نه یه جدول امتیاز خشک و خالی. روی هر مچ کلیک کنی می‌تونی تماشاشون کنی و ببینی بالاخره کدوم‌شون باهوش‌تره. کل پروژه هم روی GitHub عمومیه. البته این صرفا سرگرمیه و جدی نیست، اما همچنان برای دیدن اینکه مدل‌ها توی یه محیط محدود چیکار می‌کنن بامزست.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5393" target="_blank">📅 07:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">قضیه‌ی «انسان در حلقه» خودش داره از دور خارج میشه
مارگارت مچل و همکاراش توی یه مقاله استدلال می‌کنن که راه‌حل «انسان رو نگه داریم وسط کار» توی عصر AI، اون‌قدرها هم ساده نیست:
هم طراحی فعلی ایجنت‌ها نظارت مؤثر رو سخت می‌کنه، هم استفاده‌ی طولانی مدت از همین ابزارها، توانایی‌های شناختی خودِ ناظر انسانی رو هم کم‌کم از کار می‌اندازه. پیشنهادشون اینه که نیازهای ناظر رو به‌اندازه‌ی توانایی خودِ ایجنت جدی بگیریم؛ تا هم توی طراحی محصول و هم قضاوت انتقادی تمرین کنه، و هم توی سازمان‌ها با پروتکل‌هایی که اثر اتوماسیون رو جبران کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5392" target="_blank">📅 23:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5391" target="_blank">📅 23:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سندباکس‌های ابری Docker برای ایجنت‌های کدنویسی
داکر سرویس Cloud Sandboxes رو منتشر کرده: محیط‌های اجرای امن و میزبانی‌شده روی زیرساخت خودش، با ایزوله‌سازی microVM توی سطح سخت‌افزار. با یه دستور میشه سندباکس رو بین لپ‌تاپ و سرور جابه‌جا کنیم طوری که فایل‌سیستمش هم منتقل بشه؛ یعنی کار رو محلی شروع کنیم و قبل از خاموش کردن لپ‌تاپ بسپاریمش به کلود. هدف، ایجنت‌هاییه که ساعت‌ها کار می‌کنن و می‌خوایم چندتاشون موازی پیش برن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5390" target="_blank">📅 22:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5389" target="_blank">📅 16:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJSHilLOVl0yQj9KsTsiiwH_gJs5FShSUBNWHedThVoRBGsD_uo3r336ib98fppH7BIx-W4BDwlP7oBPU5V_JTPmDV0B1eNiv3zgnPZLyC4G7rSQPbBYaTo9f_RWRrThVGYpQmR4VMD3kvpqv8Pm-4tMLjQIBtGBmGG8iOvl-J0aBSuJuLPwwyrSHDPjWobuDZdRuGFkdrH3HdJKOB9smzbEezfL7wLhAVqPIehMNfuW9i8Lp5ke_dWbQSZGjkkGFMWGTrXJQBc3XvvZhtJZMIsB_VF_3QSaOhXLbQgDNzq5B1grD00vtuSzFqxE_Pi6rerv-2kUoQFouyox_pQhaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر بلاگش رو از WordPress کوچ داد به EmDash
کلودفلر جزئیات کوچ دادن بلاگ اصلی‌ش از WordPress به EmDash — سیستم مدیریت محتوای متن‌بازی که خودش داخلی ساخته — رو منتشر کرده. EmDash با TypeScript نوشته شده، روی Worker خود کلودفلر اجرا می‌شه و تا ۷۰۰۰ درخواست در ثانیه تست شده، در حالی که بلاگ معمولا ۷۵ درخواست در ثانیه داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5388" target="_blank">📅 15:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cUUFxd7-EO7rl-2-wNhJdeF9hozT1BrdsqbM0x7Bo96h5_8VcGnhwCc5HK8w__gp9OKzwFHdaHXzHPuIAR3Y7CGGmeYP6OMplNczlZhWFHFB7dRDzBHQat-viuIG6M4_BFUkHgzTgBbAloi5tiOqFRKacBF4m_l8oqUYcZqfKTlGZvMR9x8XQcB2HRMFTl5wJGE7SYUrFYSIKG00IrDofk0c9DyHv1XygLtiquuid_F8soDN3oN-RKOduW3VWYFPs7HbJgzB5cubLasGYECfbZuIIaMnfKaDY0ub1ElA0BiKvVqS_At-bDnG7mwOcPu2i9YazDoDSSW-0RIeUEl_qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا حس می‌کنیم هر مدل جدیدی که میاد، انقدر از مدل‌های قدیمی قدرتمندتره؟
باید بگم که این بیشتر از منطقی بودن، «کلک» شرکت‌هاست برای مارکتینگ
اگه یادتون باشه، 2 هفته پیش همه‌ی این بنچمارک‌ها(خصوصا سه بعدی) جوری از GPT Astra تعریف می‌کردن و چیزای خفن می‌ساختن که انگار خدای همه‌ی مدل‌هاست.
بعد که Claude Opus 5.5 اومد، خروجی‌هاش رو جوری نشون دادن انگار اون مقابلش پیامبره.
حالا این قضیه برای هر دوی اونا در مورد Gemini 4 Pro داره تکرار می‌شه
به این کار اکانت‌های بنچمارک و Ai Enthusiast ، قضیه‌ی Strawman Fallacy می‌گن. یعنی مغالطه‌ی آدمکِ پوشالی
توی فلسفه، Strawman fallacy یعنی از رقیب قدرتمندت، یه فرض پوشالی بسازی جلوی مخاطب، شکستش بدی، و بعد خودت رو پیروز جلوه بدی
هم خود کمپانی‌ها، هزینه می‌کنن که اکانت‌های توییتری/ردیتی این کار رو انجام بدن؛ هم خود آدما خیلی وقتا این کارو سر هایپ و ... انجام می‌دن.
چه شکلی انجام می‌شه؟
1- مدل رقیب با پرامپت ساده یا بد تست می‌شه، ولی مدل خودشون با پرامپت بهینه‌شده.
2- قابلیت‌های رقیب مثل reasoning، ابزارها یا context بلند خاموش می‌شه.
3- هایپرپارامترهای رقیب به درستی تنظیم نمی‌شه ولی مال خودشون با دقت tune می‌شه.
این شکلیه که می‌گم هیچوقت به بنچمارک‌های این شکلی توییتری، نمی‌شه اعتماد کرد.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5387" target="_blank">📅 14:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4xntp9Q_pzpcp1ZqDCiRNiH90KcWVcvds-z7KlH4Y2KZTXMGNqKBJuRDUdIVN4H4j1CzX-6PL1HTinMR0i_vRQv8E0IjWng0sbF4KtJSSAn1Nx9Jpe4VpzMZjppC0s-pXL5N-7IQ0mJZn0lHPt13lIuQr0MEpPQk1eSXEX32SQBxwinUIVyMQE-oceypPIopVYir0eAqm6f3K_ZM1J3ralX_8Sz7gZu9ycXWNHZHr3ZLb8Mw3t0K6RHv1BQ2OLpDvu9Rm8EShwLd6bM1qeIm-skWJ3oR8cqmYiNz9z_dZuI9aSrP7TM5ekjkRhuO62gVvFLSf0AIFLUCo98CSCsuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ هزار دیتابیس Supabase داده‌های مردم رو لو داده
پژوهش شرکت UpGuard نشون داده حدود ۱۶ هزار دیتابیس میزبانی‌شده روی Supabase بخشی از داده‌های شخصی‌شون رو عمومی کرده: اسم، آدرس، شماره تلفن و گاهی پسورد و توکن.
و بین اینها دیتابیس یه کنسولگری دولتی توی فرانسه هست، پلاک هزاران خودروی یه پارکینگ، و دیتابیسی که برای دریافت رمز یک‌بارمصرف کلاهبرداری استفاده می‌شده. Supabase که امسال به ارزش ۱۰ میلیارد دلار رسیده می‌گه پروژه‌ها پیش‌فرض امنن و امنیت یه مسئولیت مشترکه.
بخشی از ماجرا هم کدهای Vibe Code شده هستن که بدون پیکربندی درست، داده‌های کاربر رو  لو دادن(شبیه یه بنده خدایی که یه بار پروژه اوپن سورس گذاشته بود با به به و چه چه و بعد دیدیم apiهاش توی کد فلاترش هاردکد شده. (طرف مخالف سرسخت ai بود و میگفت به کد ai نمیشه اعتماد کرد)).
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5386" target="_blank">📅 11:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=cL9t3WqnA-BZiJTFH4BtEapi5ZV7_s1CHxvX38yzlxJsV8ckGTjgM7EGYCSm9iP-c8k0mTPKzea-mM3jVeb1yx9PVad5tdLHf7RUDdyQrTz--ZzUzC1c1RhMMX5LXtspPfjSwRwWwF_oBYt7P3QJ7n8Sj2OHLhXddyc_PabrH0jg2uIG_RYPvNmAukgXpU4FvyFDl3a49oRjVqm4mfA-iV7vzDmdzWGnt9YqWWUaHVdkVIC1b5wOyrjgvenCQqo82bNscvublJltxgoeQUltWO6GpC7KYWGfSceDGKnZfIiQ09zPGIaEYy-hodL5XI8AczpTk-q0qAPlN529hb9faVRTkX6diLhrEW5KU8VaixxBYm4_zwfYi_ApS27fwrhYkwRS-3_lRm4zpWB3eKEOo-aHC7xBXSKXoiBFhYJ-tM5TAM3Ku1GqsdHXz1MSxS7XhLUQeMKP03zWTwj3KNESh2ueYYTsgA6ADMflhggWVCKW1bAl3Sw1ZCcj-O7ktfbwvVBHH6ivrK1SIELCUghGmFTQ8HuvhkSXTd0cmaldD6hnekl0S5sMbP8qsSj5YN0QZiZD6PrrdBfqNhTg5IvKWFgvelb1kEXJj_NkwIWXy1gSXOIFODeTNkK2T_z8--Z7PMgBSHAhIKB2i1GgmYmskT4TCtfBVJl2j4c2wiIP3lc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=cL9t3WqnA-BZiJTFH4BtEapi5ZV7_s1CHxvX38yzlxJsV8ckGTjgM7EGYCSm9iP-c8k0mTPKzea-mM3jVeb1yx9PVad5tdLHf7RUDdyQrTz--ZzUzC1c1RhMMX5LXtspPfjSwRwWwF_oBYt7P3QJ7n8Sj2OHLhXddyc_PabrH0jg2uIG_RYPvNmAukgXpU4FvyFDl3a49oRjVqm4mfA-iV7vzDmdzWGnt9YqWWUaHVdkVIC1b5wOyrjgvenCQqo82bNscvublJltxgoeQUltWO6GpC7KYWGfSceDGKnZfIiQ09zPGIaEYy-hodL5XI8AczpTk-q0qAPlN529hb9faVRTkX6diLhrEW5KU8VaixxBYm4_zwfYi_ApS27fwrhYkwRS-3_lRm4zpWB3eKEOo-aHC7xBXSKXoiBFhYJ-tM5TAM3Ku1GqsdHXz1MSxS7XhLUQeMKP03zWTwj3KNESh2ueYYTsgA6ADMflhggWVCKW1bAl3Sw1ZCcj-O7ktfbwvVBHH6ivrK1SIELCUghGmFTQ8HuvhkSXTd0cmaldD6hnekl0S5sMbP8qsSj5YN0QZiZD6PrrdBfqNhTg5IvKWFgvelb1kEXJj_NkwIWXy1gSXOIFODeTNkK2T_z8--Z7PMgBSHAhIKB2i1GgmYmskT4TCtfBVJl2j4c2wiIP3lc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه. - عاااااشقش شدممم. با کدوم ابزار ساختیش؟ + الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5385" target="_blank">📅 09:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CeCzYSX33jZF-6BPhwYNXxiZwIBpqJ23B1pe84DH9Y_LCemUqjk6FKo-pdUueTJbBPHkxegQv4EigttK5BATjcckbeWqjr8_eJDRM4BuoTLdqjjkMRgCRsK72WXYpF7ernf9STomDSdkahnNY-ndM3QmpHHNUXYq_I1w2nxPD_WukBIPgYO1gNzIZ4dcHrr1l34ZsbxMnSl5jtBVHW2HBv7gzyVNOxNuAKpV8GPst48vWv3BsZm3oA04NY3ie2DTSaEIW_dw4RrwO74yCMvwxPM2TbuS6iwxrU4zwiO1gWqb4wlIHzHj1MHHjElJts3vT69WMg3bynvl0TrzLjO1Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه.
- عاااااشقش شدممم. با کدوم ابزار ساختیش؟
+ الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5384" target="_blank">📅 09:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LH52gWKXoCUaCCTsNjlFOqUys4gc3A_ey9Y1Hp-ECERvEOwO3APa62n8p0LAmeIqwsUViFT8SWc5jRrJengYWGnnP-5r_5NJbjfrPYrEZYqENhC_mvWk6Ww_vNJqU6B-eQlbfQNgKHIO1-__6pIDx0lY1V0tGv-5KMUoPFyrllz7-QCcn8m2GedKjGo7Vfj0voeUIONDsU8Wb-k07bJbSfmAPWiu4ZassNHFPwX7dMzXubpcY8RvUF57SVN0WXRaciO2Uq5qmFfJHoRTXgrQU9KB9XoTZmOwHxM1pC2nQSZrObc7VwsyEUkLTFCshceOcvLX3k6JmDV3BrkWc8YCHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولایا (Ollaya)؛ مثل Ollama ولی برای مدل‌های تصمیم‌گیری
خود Ollama، اپلیکیشنیه برای اجرای مدل‌های Open Weight روی سیستم خودتون. حالا Ollaya، همون Decision Models که Jev ساخته رو می‌خواد لوکال و متن‌باز اجرا کنه: سوال تایپ‌شده از هر متن یا JSON میدی و جواب کالیبره‌شده رو توی چند میلی‌ثانیه می‌گیری. جواب از یه پاس روبه‌جلو میاد، نه از تولید توکن‌به‌توکن: حدود ۸ تا ۱۰ میلی‌ثانیه برای ۵ تا سؤال روی RTX 4090، در برابر ۲۳۶ تا ۲۷۶ میلی‌ثانیه‌ی API عمومی Jev. با API سازگار با TypeSafe کار می‌کنه، پس SDK رسمیش بدون تغییر وصل می‌شه و مدل‌ها هم همونطور که گفتم، open-weight هستن.
اما یه بحثی که وجود داره، API خود Jev انقدر ارزونه که فعلا من با اینهمه کار باهاش 5 دلارمو هنوز تموم نکردم. لوکال اجرا کردن لایا هم خوبه اما شاید بهترین گزینه نباشه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5383" target="_blank">📅 07:25 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
