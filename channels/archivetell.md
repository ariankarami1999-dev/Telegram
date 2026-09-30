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
<img src="https://cdn4.telesco.pe/file/R4TXz4bQ_2AeLuExWmroC0OHNCJqAfWssKInz8PYVFd7wAR0EZcwznkbe10kjjFenIwEzBC-CS5wJ90K60j7RI83LKRMk8Z4uNz014n_67CdqsC6UnYMedpYEirpw703Z9aHoU8yxdD1iMxpCy1eS0WbAifkdyj7mJUV2dv0qE8-xJBzwzjAHCc_I8Huj_B2Dm4glodClqJ7yoBcaCnidfhuUSuWvxI7-Ah6MMEYNlimWlatbsnRgwfBvIDJK4hvCro1KTGZEaXaJWA0sHv7nZ6y4CvPU7Py0XjsYskWvgnYvGdemS2l9fzMv844JUnE6HUOKGXx8L9ifamvx8nrrA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 00:24:30</div>
<hr>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s2hlcrEhqBqdsAV5AyGcNx8BAseq1ubiMvWYBE80pyZGdJk5Ebxe-q9hfn5NRfrJJ14AdSpYxDL-czFptvpAUKxSy8JoeLcH6b01voL-5OO5GkN27NJhRPfYRuY5MP0c30jE_SVpeAMKa-KDxV6PfCtnnP11h_HKJoPN2rAE3Asua6n2GFWtKDED0xzsELGQ2dHIZHayXXaGjc1u_cFj2gWmU__XVM-MsRb_wMJ3_wMZ2cfaQMrCphvuWHeChIILM3u6Tng9shsJ29ClFBGJHdmtZFyPqvCaJoUN3IVn4mm2tA6AO-sLdOZHDJo55b0_bhf67wpNnoekPVDV3TG7Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a8YTFGduc5tR7Ek5MMGGa-JfGtWVi4lbokyerz_9mp2xaJsrG14NOHOM9Fs9D8EogNeqs95-j-jhsdz8xZmJVvpCrjZuSWJDrgsftS65PiZYFMYNmbj-a5zytz5HqGZ1We4OH0oObaLzofCVPUgiwsHI3Crq3edqB4YWHxPoDVDKmTYiNtV02eSORSKfwQY5ayeAKLM0Sro4uXU5ieYnG-vmxpIcdiG77suQh3LRp5ZdIeCs1FhJdTeej3we-3H1jOlraijGcqxp9mpneB2qV0QTaZi9Rmk41v86vvBMJoko0cf0rHnH075CKfMSM0nIPxetZQu1Dh3073DttwKAaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 85 · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 460 · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brSy9xsrRDgqV5g6hlneHtWPO7lGSNCHvkuHJMbBBJKkh5AFm6GGtNklfVjg8Bh0sFm9UEm8JFywjC1_AYBdg89xleW3jzbsFKUdRK_24TfWMFNlyLBtDcNeARQSsPB7K9VUc_5furum6kRnZEmNuI4o-iRv_Iq98imGNbJ9lzHKaeqsVDINaTZRksUqD7_iOwti6DhfJEpLKL9FmIVtMW6qMAp8HEUnsrNeYUxpOPyYSzVagpB4Cfd2n6tS_Sn4XWQTF8y5C0viVPGYBl-WR0TBiWVPRkwqM7omU9m3V7L5Au8JFp2nsFRwYca_Ycs8CLUw8T0fQQFA9eMxh23N2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 553 · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUMaQipE0KrjJ6KEPhMnfY_QXxcYnHrts42NXKmtoWv7Faa7nPhmYBX6QBtTvKQseWrF-RotcFng1rEHH5Ps5WfTzUQc46EUsI5s0gRGdYQe-qxd7NlbivMlSMZmCFyzoCcd_kPdIyO6sPRYXeoPREpGl2PqLReZGE7vSp7gKjMKKc1D7RcvrTh357zHqtXiKgVs8o5mxUhFX16E449dMMTFyQTcg5STQ8FISwbF9l9bQeq0yple-7STXaHPt9FFtOfhm-1eCNHRgQTY93x-bDG_eO9t281SZbUoFUFZzrZ6rd29Y71-t7c-7vqgnbHQV3jHRf8Iv5-C5F6QrinNTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 602 · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I38Evbc-loTYSSl82oyb4jl4F2xy-I5J5WxgETXm4izp0ByQO7VB6rmJ4khUGWc8nh3r7Ll6mjRh5Pcjh-1uDLCK6XL0KRCWna2XGMzZyFOkKKfMt3eTpa6JVI1D7oYJLX91FHmtx9OXn4-y--XaU8pjUq0iCspOwnAfLYhy1hVBKoVqLAZoxnGXi6sjzul67vNnCky6jEn-tHh53c_-YXSl43k06PyIRoqVn_-aKTQF6b6rjsti3UyQ5_G2eTAjMWPNXQ-8bEFgl0gVYWfBTas6zwEMhB8s3YmU9ZbIw_u3hcMc6KQ8FMy5op5hkD8KMUuDxxg9G6A_QNYHD2LjyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5O3LejaFxxh5HZoS_DJWds6-Q7-2sSuqMq63pZYP4hyHajASvjRcEK-KSwW3qJECNSs_RqfpjV_zX77-eXIRZr72OlUfZVocUAzKu4ix-CmQDVD73-pzFu3yFLv8IS-gsvcgi1zrdggmFJ_nAc429IZ0cSGmM02yLh5X15Kg0PmXDemGdtotMgAWSaZjsYb-zvOGUrc5-HvsBAws_fC1NBNCfa71X0tec-Za-rtMHgQG3bdlRDsYMJPoo5zN_aiNed2t7xrK6aZrMkV8TRcpJ-whzeEudB-kCcl_yNfwbz3I7_qwTVmyK0zbG-JyP6bgeYXI5WIQhtaW2lxijxbnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚀
اسکیل‌های Gemini برای همه رایگان شد
‏⠀
‏گوگل قابلیت اسکیل‌ها را که قبلاً فقط برای کاربران پولی بود برای حساب‌های رایگان هم باز کرد.
‏⠀
‏
🫧
با اسلش در کادر چت، دستورهای سفارشی‌ات را سریع صدا بزن
‏
🫧
جم‌هایی که ساخته‌ای حفظ می‌مانند و از ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند
‏
🫧
فعلاً برای حساب‌های شخصی بالای ۱۸ سال است و انتشارش تدریجی پیش می‌رود
‏⠀
‏اسکیل‌ها نسخهٔ ارتقایافتهٔ جم‌ها هستند؛ به‌جای گشتن در فهرست بلند، کافی است در کادر چت اسلش بزنی و دستور دلخواه را انتخاب کنی. گوگل می‌گوید جم‌های قدیمی‌ات هم در مهاجرت ۱۷ نوامبر خودکار به اسکیل تبدیل می‌شوند.
‏انتشار هنوز برای همه کامل نشده و ممکن است دکمهٔ ساخت اسکیل را نبینی؛ چند روز دیگر دوباره سر بزن. ساخت اسکیل به حساب گوگل وصل است و حواست به داده‌هایی که وارد چت می‌کنی باشد.
‏⠀
‏برای چه کاری اولین اسکیلت را می‌سازی؟
👇
‏⠀
‏
📌
صفحهٔ ساخت اسکیل
‏
🌐
گزارش نئووین
‏⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vATKNX2oOYFcu37BsbV-v_zQB_qVgpjF2oR9K-mEY5jHJYsd8y7InFydGpQmVEZ4jAqE06Yhs5dcs-S7wY1pcnW9rmRsbs9JoiIlsHF8_Kex5cA4jvXrQkWwooUEfMjv4BaPZkFkKQi3LRodigrIiU4XCSm3m4_-G4iRI6Mi1BjCxPT7Gze7c3DrjRGgyhczI6JiXt8ykKXCVjonp5SvSqy0-VWYupcM-djy2FQ4AfQ_BTjYDoWcQX54INSQH-6zXx68Ej9v7cO7BYIIKbW4mO8gv0nSguidwdHVcy_98nlCVRG5E1chYd8xzKCB0746jL0DG_8SHrEVYzyFsKl23A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
حل قطعی مشکل باز نشدن Gemini در پنل 3x-ui (ارور ریجن و لوکیشن)
خیلی‌هامون این روزا با ارور رو اعصاب "Unsupported Country" تو جمینای درگیریم.
داستان چیه؟ گوگل آی‌پی‌های دیتاسنتر و IPv4 وارپ رو شناسایی و بلاک کرده.
😀
راه‌حل قطعی:
باید ترافیک گوگل رو از یک
IPv6 تمیز وارپ
عبور بدیم و برای کانکت شدن خود وارپ، endpoint رو به صورت
آی‌پی عددی
بنویسیم.
بریم سراغ آموزش قدم‌به‌قدم:
👇
قدم اول: تنظیمات خفن Outbound وارپ
تو پنل 3x-ui برید بخش Outbounds، یه اوت warp بسازید  و اضافه کنید، بعدش روی ویرایش کلیک کنید
🧪
سه تا فوت کوزه‌گری مهم
تو بخش ویرایش:
۱. حتماً تو قسمت
endpoint
از آی‌پی عددی (
162.159.192.1:2408
) استفاده کنید، نه دامنه!
۲. حتماً
domainStrategy
رو روی
ForceIPv6v4
بذارید تا ترافیکتون برای گوگل فوق‌العاده تمیز بشه.
۳. مقدار
mtu
رو بذارید روی
1280
که پکت‌لاست ندید.
آخرشم بلدین دیگه تو Routing rules بزنین کل سرور از اوت باند warp رد شه
هسته و پنل رو یه دور ریستارت کنید اعمال شه.
🚀
بفرست برای اون رفیقت که سرورش تو جمینای بلاک شده!
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚀
شرکت OpenAI از "داتس" (Dots) رونمایی کرد، دستیارهای هوش مصنوعی شخصی‌سازی‌شده که در ChatGPT در دسترس خواهند بود.
آنچه تا کنون می‌دانیم:
🫧
با استفاده از فناوری Astra!
🫧
داتس می‌تواند در انجام وظایف طولانی به کار خود ادامه دهد.
🫧
احتمالاً فقط در طرح‌های Pro 200 در دسترس خواهد بود.
🫧
از مکالمات صوتی پشتیبانی می‌کند.
🫧
دارای یک ماشین مجازی (VM) اختصاصی در فضای ابری است.
🫧
کاربران از امروز با یک داتس شروع خواهند کرد.
🫧
به زودی از طریق پیام‌رسان‌ها قابل دسترسی خواهد بود.
🫧
از بیش از 4000 اتصال (کانکتور) پشتیبانی می‌کند.
🫧
بسیار قابل تنظیم است!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UNw6nWIr7V5_P9r8D0UzqRwbMhZ2VBN8lSGKaTZG7j1qD1R-73NRoHGxFTyu2ekvfujz0ZILzDN-W5W33HNCP5XQ7pSQyx33M5zYMQEA9azD8fiHF3Hz4M4UgGRnoeTevEGjRFp0I4xr5gz9tomhCQEKQvOkutKYL1ERznrYVd9QO_ol_obFgaEj87pa8_2ZEVD-i9uHk9PfX9FLh0st8ZDqSiNItIq6lCjgPe-9NjmhFkc9MEFYTUVp7LbIN1i0mgV6D-t1BT9W6LlYHwRIqOdF1j9A45q5VCiGTaVCPFWKD8hvQKTn8vSt9EK7ObARcRB_cdcnfNIrD6jsdmPlqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UgdpsjMpfPz2pS-QZOWdp2QctP8wKOQQh4K1r3eAUJypDRBCNCD-vwC4pytlq_hO2P96CcHHk-OWNNYOBYx70YcFKZJ3MJvB_qSHJq5orMJkL2upxXZxlxYz0y1rJWSQ1BRrM5pGSFH6T0XdcBPiITgsD7VR8AIvARcabwmEVUI4qqKldlvxPO6U4wxmo3zRBCk_Hf0vp2klgIXyh6aTvbEeCT5D_k7jQWnV8HiUfJOi6wnvD5OqcjmYgao5B4FpXVdXhlorRAf-E0WRfQz1AOEogztz5q3N1H4bZ5KXW2cXbPdcSN-E2S8visiVuIe2S-vC7E-R9q6Uy6REvC1z6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GjTxGW6t7Pw3gcCaYTo2sANtTSVQJkzRFNRy8iFA8L3QzX057Qux2nQtswfhoy8KIn6culoQEasrTTYeVIAuwyTZZNfB5cZRj3QlGScTXFceLmqKkTwxzV5Oi0K25b8-VNysB0hoCORhre_LFg6JcVYhW_B1qK8D0ST9V0WaTEj62jG3jqIc75NBGSTg_d1MnxarrsV_5UyIYpWx9o-RMhAy9e650z4dXn3Iiaj1xmqaGmNn0VoMhmsyW0j5xixHfVXnPHm5dGFsadUGXbPpoYEhZTULiHj7PuJGB2QPq36kN1RPEnDELyK4UB8qtL7Nk4vJ1ZaN3yRFwAi3dO5Omw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b1wlUqTnYisEcJloY2CPrGGDruEreiVbVDxjW7LGyYsdeJVOPmNYnpmcIjKX6wHHhUBRmZO_6FEEuBM8GOlBHjfhRZ9L_9-sj50Ibhq7XqTbWFw0RVlvc5bmEb0uIwU9QiRSiUksfQjOHBPYX_XMy6SoGFBLFa8hM1eGiv79pP-kwWU0tb3CNxNgV_zy0fWeFubJpPfiYnv8GnP-NTesjWx-LEcnElsHUF9G4D5Y7H5qd3QHlqzf4j1GpVNwF_-WNPzg2HPV6n5T9jmdvkQ8w3pBAmNaeZxqS2UytGvD4zTaXRTuP-8MkOrRHz78rzob3U5c6IGS1r_DroYhzaFQpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rReJD72wX7fEOEcLL-mlRNIZPCTvMffR907G3VezfhSy1cDuMo2vsHJ6Y38IvuVQSOXGnt2yYtevovpWgOGeNLxm7Wai524q1Whk2cVow7cBraaa_OLzHBT3g5mu-BC85xv4Ypn5UTo_n8v-jXPVk0kvniMMjkVv5PI7U0ap1mbQgdKpk8MDgRumj47jPEGdPxtrtdt0b1hJqiSPJiEZqThW9sPe-KvmonPqEU8RsTQzkYoYs0tvd8Ka6kRNt5dSdr2k2_Js1LYyMUjV6_U0fK8Weg2S4g9Vzwd8aemtpwaRLGVDL2OjIRNQ_VVXBqh6_SBOOyLjFdZouHFra48Lyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6dvejKpLqwbZN_sNHt2IJb_H2_Sc94vVQRT4ktfsPmNMjIyc67Oa7L9QML6xJvUYdmjVx6DnRJDi-w8iPqrpA-krA8pEW6jSfHNprZZeKtI86t0Kfv2OOrEJD2RI1uRO0QD40hHoyCoPTlE758HhxMtK5DXZY4uiSHTPq7rlwWRJ8sGLdm69UKA7YoYP1910QXKqCCOtJCjnAVbFD-di3zQySRg6hPP59_lqMnPMxkL3Zgiqe6WXKK2VfDAZfSmpB-3e9fcQ3LSUs2ZkMwvSHuL7WWBFlX9HMXoqqbwDuPj5L2x33xkMQlvXONUET_jNwDXirybiTvbIyiI0YmfKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYdqERSlk4n3NUMuaFQb9UYjT_e1v_mTRcwgGav95EKWJUhiJLv9Zs7Z6XfG_RQvnD3bCO7mX0ik34GXZ7Opk6BhOXEOBkuUWM7O_34GzKFTYlog_ivSy5apIlgfYgkCyC2fOoKd_6ayADB1xZ922J9cs3nu3fmrxjPZOI5aw99VSeOj38qX2QHP-uDLxgPSpXZLpgQ4pJkMANdxpwrfPxvwuZ2koNwp2OSL0XlLruEXdvVrgJKr-wUYaGGQuMc3ivNRGISWhbPLcN6X0YA23wGjhnk95OSu6Mdq2i2gZteC8Kp2YrFskTDzk1lJMOscwdGlN7sZ3ZD_8kVn8ODZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Relapse – PS5 Jailbreak Exploit
🎮
یک زنجیره
Exploit
با نام
Relapse
برای
Jailbreak
کردن
PS5
منتشر شده که
Firmware
های
7.00
تا
13.60
را هدف قرار می‌دهد
🎯
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hX-BvWKpGLIhjxRTn7dVkWVTbPw8UVzuECzceH6JF1CqXqlGe5wUjs3sKqIEEtnlNZUvmz9krK54xvZ9pSpYho--RCflHh0aXo3BCwsvfEKqPz-jVNnDsAOoZqkXn7Tr2_8ipwYc1IVcOWR8_F-bkrBQZ6TPq5arRoIB0OX-lQCPWJ9ZTps5-FGCaKieMREzFm5aXvXWrc_XIUr92dv4EKewi7cErWI9ofr_hLlf7hPgJxUwJPsD-s7miWnme5D5SorK02NoEE7ErVt5LmNMb7Af54yFnVzT71JxZZf3TfWkvlDFFh32sX9AE2abioaMUMzwel8nZ6vEDyzJqTuerA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های زیر
💥
🆓
Opus 5 | Opus 4.8
✅
با این سایت میتونید 100 دلار API برای مدل های بالا دریافت کنید
✅
⚙
پیش‌نیاز ها :
اکانت گیتهاب 1 ساله + یک اکانت دیسکورد
💵
هزینه مدل ها :
ورودی 2 دلار خروجی 10 دلار بابت هر میلیون توکن
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqmxkYWOnHYyztrYEkY1lzPxzYIrQChjqH6aAjSKFeQBkytZO9ARo07pCG52kM7tu0szdBZx3l7jBiluYO2ET6SaC8ma2MQkaFtu1yFcPyXCp6toNGtI7NQED8D7_0FqjSldm1Ym7ZYxr0r5NbTuCeZJ3s5f9q9cyvfzlKgmAGe3gjrq1_VK2QstczoOvu1Ds9dGHNF1hpR1G5TUYb8UDfmJxCaPZFDXeizrEauETSWdzfZAQac_nOKTeZ7VIHbOV8FGhMMTpWRmo7Xpop5h5K-yJshxV_aQv5W7lXq94RI_h0Qj1ad-7oSNSRXv0_AXaqRigpVvLM-91DS-uLdKeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📥
دانلودر دسکتاپی deviload برای یوتیوب
⠀
‏یه برنامهٔ دسکتاپی که yt-dlp رو پشت یک رابط گرافیکی ساده می‌ذاره و دانلود رو به چند کلیک کم می‌کنه.
⠀
‏
🎬
دانلود ویدیو در MP4/MKV/WebM و صدای MP3 و FLAC با انتخاب کیفیت
‏
📃
پلی‌لیست، زیرنویس، SponsorBlock و تفکیک بر اساس چپترها
‏
📺
ضبط پخش زنده و رصد کانال‌ها برای دانلود خودکار موارد تازه
‏
🎛
ادیتور Devil Cut برای برش، ترنزیشن، سرعت و تغییر نسبت تصویر
‏
🔄
کانورتر با هدف حجم مشخص برای دیسکورد و واتساپ و ایمیل
‏
📱
فرستادن فایل به گوشی با اسکن QR روی شبکهٔ محلی
⠀
‏لاگین یوتیوب و اینستاگرام داخل خود برنامه انجام می‌شه و کوکی‌ها همون‌جا می‌مونه. صف دانلود تا ۸ مورد هم‌زمان می‌گیره و خطاها رو خودش دوباره امتحان می‌کنه.
⠀
‏با Rust و Tauri نوشته شده، yt-dlp و FFmpeg همراهشه، تلمتری نمی‌فرسته و رایگانه. ویندوز نسخهٔ اصلیه و مک و لینوکس هم بیلد دارن.
⠀
‌‏
🐱
مخزن پروژه
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏
🧠
اکوسیستم GLM و راه‌ های رایگان استفاده
⠀
‏مدل GLM 5.3 شرکت
Z.ai
حالا یه اکوسیستم کامل داره از جمله چت، کدنویسی، ایجنت و API
⠀
‏
🧩
روی همون بیس GLM 5.2 سوار شده و همه پیشرفتش از پست‌ ترینینگ اومده
‏ به گفته خود سازنده، بهترین مدل اوپن‌ ویت برای کدنویسی و ۵۰٪ جلوتر از نسخه قبل
‏
🪟
کانتکست تا یک میلیون توکن و ۷۵۳ میلیارد پارامتر
‏
✅
صدرنشین بنچمارک
CyberGym
در کشف آسیب‌پذیری با نمره ۸۴٫۵
‏
💸
قیمت رسمی هر میلیون توکن: ۱٫۴ دلار ورودی و ۴٫۴ دلار خروجی
⠀
‏
⭐️
برای تست بدون هزینه،
NVIDIA
Build
همین مدل رو با کانتکست یک‌میلیونی و endpoint سازگار با OpenAI می‌ده
روی API خود
Z.ai
هم مدل‌های
GLM-4.7 Flash
و
GLM 4.5
Flash
و
GLM 4.6V Flash
همیشه رایگان هستن و وزن‌های خانواده
GLM
روی هاگینگ‌ فیس منتشر می‌شه
💥
⠀
‏
📝
معرفی رسمی GLM 5.3
‏
📊
قیمت‌ها و مدل‌های رایگان
‏
🟢
تست رایگان در NVIDIA Build
‏
📥
وزن‌ها روی هاگینگ‌ فیس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJfFbGW9rwaIo2IqU1jQXgcx5UFoKUZMk6yvsTM1MRDVPIgATpk68VtoIWKBlIF8QyHcCFw2QBNKMY7ZSo24C3qbuLvWu6R4mJlrBIUeZXiyb6aIqyVDoFRw38e2Dwr62Ke_0zljVaDQDc3-oJxCvUdAy78h_QAdYYRgcFmWiRyeLuWMmvuszrbYrbD0XSNIph9-RjjNC_GGs0jZ0iiYB_w8zEV-ckhGvkYZNEGezc1dp5miRHdCEwvPpTguL0nN2NSsHsgEdO3F6krg_NRAypgvIFX_gPxf-H4ZZgPV4ReCvuTUqMeRb7RNs-JASSI3vC_q1EqAvLLz28LBL3-aPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dOIuJVTBtdZ6saPjqOtOu_C6QVzEtTgXQicW3DFHaLCbzqCDuEUJR-WXrsJ-PQWwtwBzAGDd09T01hO5v5wCITCynNZlOFItA77wTShiGoR3QiBeThM6ZL0WUiXGJclsoJJdlR6N4xEXJsK_mCzqCOwCzs5FwRqxy4LBx72Cn6VcukQ-EU-LWt51lb5DBG102yqahl7-TYoqEcQSe0BkN1QaAWexBJDUSmSdN8II4P6Rw7vhjnJG9XqxnEnthebvSdyMsK098j7EoZGnYk64M1wRIfj90cXkHWEydcCksglBWghcghD7POMZxgUoVFtIYy9xn_4BmqbJfVVOVRev_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-73q6Ho49hTCM-6DwXqcC9HyGvx7nI49QIftcLzFLXXKyE7TR8az8S0ceEbJXXwxlrS3jYwXZA_O3LpOZIiwOo1AVRdRlC3lgNUL17AYPkeUW6_5HEuePWAlmuzzPnO74TPLpLy_5I3e4yte2RTlb5rQ6jftPxhT1jhFvOxRwyqHLTrJR3yQFJyKMC4HDP1Na_npriOTH3SBmG-OMsYEtUAf4UuJH1IW3KiLm353EmBPOsyMRT68ct1RUB-wwUv6Jg0mBF383kt0B1GMcbtQV0-yHo986Y6YyyZHka41Wb_EhspIvUV18E415xwDPu2wqY_akV3oARY4j3HnEbFtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhCdAS1zEoyoIQtGLxLXA4t9RGgjHpU1MuWgWOypMiaflu2dR3dBkBCofZhg5Ktx0CzKXTyY8vp4zlvCW4r_TnSUnNCCPj_tXESXgqULIjXEH3myg8eEsoeih-lrcE2NcT0Hp138-3Qyz-oNzzIBY1Ikh7m3gC9lJ7PnxoTbhouZOs6GGxOdr3N2cydzGCm7sh1z9wIXn-GNnrKq24cP6J8gShs0fKdk5Y9wVzMDD5KuLFipwC1MOaIxXHDgCJKewRWbxfgwBeY4ilcWUXtg2K_8OsL-Vb7T-dKJXKWlaEmqDZkG-UcC2rBRGIrMbpu9iwGoxAAKHr5LdTUscxekNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GyJ3G4KbADc7dhrSFWgjL4p-DsY-uShijpgT8S25aPDDlYeVEvVaz_VPpeofY6rrKrf8ZOq9B5Tc6pYK7HlHJiSGnXNL0GOXcGSybNDyF4BcO3mmVWy8C7Mm-lswsFb-GdhYZoxze2VIf56Pv854jTP8RAOaEmJeYpJzyaAV_TsBda6vnkX_mVjxdiccP-wG_rkIv0TsgR6InCNiAN3ukD6ekyZ-Ne1ND6iMOdgYply6YPKGP2rJP73ePh5Ks69iXuTfiO632QtjEA0T0rMR35g2pPaV0VS9ocVXn3U6MK1GVme6WVCNdxb6T69DiLyxdxvOoGz53Se2vcCSZvHiRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klyCGHgggy20oXSvG6R7DQbdF9J05snQe2m5PN-_5XVeRUxZlluQrn9qAwpI4tESwlJNgNZSnThm7HSFxtX-t7bhgUDLXD-Ki9AUyQyBo3k1qDQeXqovy5q5CDEEvMO7GzK81UbD5vLIMP4SwLaWZD3n4Fpy6m_N9ZEGXmyGr6PQD0h0JACtWfrsfvDLDboK3dxca3GZrcC9EWswtIXdVDwT5GR_jZdLoWbCmeqrX6diHki0kZSQwTn2fKpil5UXg5wRG2qnot4MpcNlCtPtmh4uG7BZc8rvFqor28mOKR2M4XJTocs20Drspn92d7fjaYUBMgtKYmnbHFZBajToNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBCzj61ryIaxPR8C4K61u40u5PmpRzrkVLowaJjY9EeNkTDfe-6Suy0FX35ibv79qSaaNnh4OZ9UGl8QAkFdbIUxywUtbB8BCugTWAZEqEZ658e6z03fqk7MlIe6nLdwrdCmXsve2HDYLAh3C7dD14QdO6-xnos8fkiN_cPl9VfB5KkhQm4Jbp3cKKvqRZThltSi9vCrJuc1-1HY9Ul6gGsCHm-lhuO88TiyBpnusPoQgBjWLwcGuTnhm2tH2UDRmEG1pszlHJ7lNfm3lGqezbFc8ys05jCyRfX1b37BoO-ie0Ht9tvCUITQjnJzH2BaHS1xSf-QeVjCTCqHOtjJMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAGkKWQ54YVEN28VgTsPTBXLieqH4rZR8D6q0Hmr7CsHxcWPXod-fqacnNo6fLJ1UsEq20vTyv6ZrzVLRizyaJIAuoHagsNpw5JcA_i2eMhPZAfK42aB0HaW0joyXg5WKuBRMoLwgO8k53BnYCv0nXWR57DR41XXe-O0DYdXRjewRnrk3uLkIRMB3L6KC4KlBanoAAxl7-S_HzqHl_usIhl-JRc9FpzCNBn_d1-dPUxMyRRKtU4VkBAcnPSlBLLG-fMCag3wsxPm0wzNwQuzxBS_58fLNQ1xvE18WvQu0LNLEDVh4FqtNBRRqN-MuEmfahcdkFnNHn6G48CzfIbjKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTaWqejfatf7wzPb2MaYczWdIWAoHnLHBBlSkbU9qHdOhG5TlM11RknTQjQZcUKqdwYH05ZsE_GkeIx9-_sUs1q_YvwzEgHNvGg57eJW1KV8i2yfPNZRiiELUJrx0MDJ9x69FVwxGapP2X42y7lek1TcY0xqr4Rq0dYSB0M65CgLAuDHjVhZ6ZNlBIIVLGxUZdBpVt_dzwHUIZFVQKwEFRdyD_8XJUhoQ2QEzvJCGat8VdLTkCDQxGxqjCOdru6gfyNOeH6RxX_D_KBduR0QKFQyh-0wtjAhb6oa6JY8Ws9jT82zO5YEK3dMbn0EE2RzhYihRDEk_iGnF1XmJLnDjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
ادعای نشت اطلاعات کاربران صرافی والکس
⠀
‏لیک‌فا، سامانهٔ ردیابی نشت اطلاعات ایرانیان، از دیده‌شدن حدود ۷۵۰ هزار رکورد از داده‌های کاربران والکس خبر داده.
⠀
‏
🗂
داده‌ها مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱ عنوان شده
‏
🪪
نام، شماره ملی، تاریخ تولد، تلفن، آدرس، ایمیل و مدارک احراز هویت
‏
🏦
شماره کارت، شبا و مشخصات صاحب حساب
‏
👛
آدرس و موجودی کیف‌پول‌های رمزارزی
‏
🤓
حساب کارکنان و بخشی از داده‌های سامانه‌های داخلی
⠀
‏این مجموعه تو فهرست فروشنده‌های دیتابیس غیرمجاز دیده شده و لیک‌فا می‌گه نمونه‌ای ازش رو بررسی کرده و صحت داده‌ها تأیید شده. والکس تا این لحظه واکنش رسمی نشون نداده.
⠀
‏اگه اون سال‌ها تو والکس حساب داشتید، کارت بانکی قدیمی‌تون رو تعویض کنید، ورود دومرحله‌ای رو روشن نگه دارید و مراقب تماس و پیام و لینک مشکوک باشید.
⠀
‏
🔎
جستجوی نشت اطلاعات خودتون
‏
📝
فهرست نشت‌های ثبت‌شده
‏
🌐
سایت رسمی والکس
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FA5OLluCBEg4ubjMA3WUrUtHxv04b7aVJaTEDeiwP9juwex5vAixLoEntn1xMdVA9_I-RE6Gkjj0jclcxx50r8Fd6mCNe81rYkKMqFd9Lf22bPLQLB0XIOEYeW5uJGZlr1svC_5_r824ATzd8DEdB2Itkm0NPHtqUMvMIRAts5l9Ye5TCUhFBVoki_VjL2Tm7lI2JcKwbpsF9J0H78uvsDLXp9ysCcCL1tI4c4rzdBG0wTCULWSJs7y0B8wjZeLwBxPHjQ0dTXarjLy8je48eYq4BKcp8ZRC72y-14TfhTQimZh8twHoTnZizp0F4-ytN6qK0tRWRWEMESiWxiODEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎬
اسکرین رکورد با Recordly و ادیت خودکار
⠀
‏یه اسکرین رکوردر دسکتاپ که خودش لحظه‌های مهم رو پیدا می‌کنه و روشون زوم می‌ده.
⠀
‏
💻
نصب روی macOS 14.0+‏، ویندوز 10 نسخهٔ 19041+ و لینوکس با محدودیت
‏
🪄
زوم خودکار از حرکت کرسر، اسموث شدن حرکت، موشن بلور و افکت کلیک
‏
📷
وبکم شناور با تنظیم جا، گردی، سایه و زوم واکنشی
‏
🎛
تایم‌لاین با کات، ناحیهٔ زوم و اسپید، متن و عکس و شکل
‏
📤
اکسپورت MP4 و GIF با کنترل کیفیت و فریم و سایز
‏
🧩
سیستم پلاگین با مارکت جداگانه
⠀
‏بک‌گراند و گرادینت و پدینگ و سایزهای آمادهٔ شبکه‌های اجتماعی هم داره، یعنی ویدیوی آموزشی رو بدون ابزار جانبی تحویل می‌گیری.
⠀⠀
‏
🐙
مخزن اصلی در گیت‌هاب
‏
🌐
سایت رسمی
‏
📥
نسخه‌های آمادهٔ دانلود
‏
🧩
مارکت پلاگین‌ها
⠀
‎
✈️
@ArchiveTel
l</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8NJlOxhz6RZstdkhf1pQDY6lWdom0nA7GHCyTCjgc-C7cf5yxCKyRU3JF3rLmMsWlTm1LcNhcEfNoWDfJ4X864zjy4IAI0U_NYlPuhmk0TBTW-tZNBvzHpKl4_pCJ65ZAa42VFE1eEZ2dpfkVnGx4Gsgz0rcSnK4ulZYxdptxHLKhLLIgMJ0W5uzSjrXpyKwJADtSdfX4YF7OSQh1e9HhMupD1hJemb4Is06j3brn1bR7BYUTV2uw75CZOJ4bj256-2oFzwoOAiAYJ38tRt1Dz4caX0XLwqvlg1Ah_7pDdiYvQ0wtyR5eSNrIjDRw2hdIRrahGWU6J0mR85K6galw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به بهترین مدل های جهان برای چت کردن
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این سایت میتونید یک تریال ۵ روزه بگیرید تا با نسخه اصلی این مدل های بسیار قدرتمند در درون سایت چت کنید
✅
این سایت یک ویژگی دیگه هم داره ، شما میتونید با مدل های GPT Image 2.5 Flare و GPT Image 2.5 Sunburst تصویر بسازید
🚀
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=OVo4387m5W3U2ktqpImjRiAMCpLyYt97eT8nWc7tWJq0iDEzCbePkqfxlJVj_k9usE4uFqYKTVwTcy7gHHQ6JhUOYjsdC-WAT-6zo94c7Nj9c_vMyYc55bHUFBzPAE4pNJKp1KZXhDUB8CS31X78JxficBufEPc63edhpLWqBG5GaN5yOCXBm12qRvaJnYBtBMKC8Ap-1BniVyP-lgAzstdGFG0mTUA6-0hkv6DNSAq53weIHrJXI297cjmElmV2xmDSgL2Xwx3-ZApcafB8sHUsETyuuVewHrHRe3CMOmPKoNGZPDnOsW0yOxpXPxu2OnaQcU7D3l6G8rqUJompWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=OVo4387m5W3U2ktqpImjRiAMCpLyYt97eT8nWc7tWJq0iDEzCbePkqfxlJVj_k9usE4uFqYKTVwTcy7gHHQ6JhUOYjsdC-WAT-6zo94c7Nj9c_vMyYc55bHUFBzPAE4pNJKp1KZXhDUB8CS31X78JxficBufEPc63edhpLWqBG5GaN5yOCXBm12qRvaJnYBtBMKC8Ap-1BniVyP-lgAzstdGFG0mTUA6-0hkv6DNSAq53weIHrJXI297cjmElmV2xmDSgL2Xwx3-ZApcafB8sHUsETyuuVewHrHRe3CMOmPKoNGZPDnOsW0yOxpXPxu2OnaQcU7D3l6G8rqUJompWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
کتابخونهٔ رایگان Melies برای تکنیک‌های سینمایی
یک کتابخونهٔ آنلاین با ۴۲۴ تکنیک سینمایی، از حرکت دوربین تا نورپردازی و رنگ، هر کدوم با پرامپت آماده.
هر تکنیک شامل:
🔍
تعریف ساده
🎭
اثرش روی حس فیلم
🎥
مثال ویدیویی
✍️
پرامپت آماده برای کپی
این مجموعه رایگانه و نیازی به ثبت‌نام نداره، ولی خود سایت Melies یه سرویس ساخت فیلم و ویدیوی هوش مصنوعی هم داره که پولیه.
اگه دنبال اینی که یه حس یا نمای خاص رو توی ذهنت داری ولی نمی‌دونی چطور توصیفش کنی، این کتابخونه دقیقاً برای همینه.
📌
کتابخونهٔ تکنیک‌های سینمایی
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAktyii9F5kB7-OayvtlqU3jlXevJy30NiOjA_0ZIj1v4vMdw2FQ3Q6f0MKXRYznfoESmr5raf7gXmHIOGvaWtl6z-kefG6GEHeDXqowy6k1x_Xy9E4SwMVUc7yk-LAD-PCkNbx2GqjKcTSTazNfCr0d02kFqNtwYQuK_En3OwlR5pbrSeB6iOGdd6z10OUF3QTcKEGqHxV5prlqE-tbqy0I1HoFeKij2srxzbN4QL7XEnGy53r0HdeeCqYXNzclY7BIxkAyBsDp4Kzd5yz5YAGyrbP1aFwKBArYW7M1U8x-umtPEBCr0U-fXDZrFvuPcqrtvvLGupupcF0OateVQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🆕
مدل MiniMax M3.1-Flash-Preview بی‌صدا منتشر شد
⠀
‏مینی‌مکس مدل سریع تازه‌اش را فقط داخل MiniMax Code فعال کرده، نه روی API عمومی.
⠀
‏
⚡️
ساخته شده برای کار روزمرهٔ کدنویسی، از رفع باگ سریع تا پیاده‌سازی یک قابلیت کامل
‏
🎛
در انتخاب‌گر مدلِ MiniMax Code کنار M3 و M2.7 نشسته و حالا گزینهٔ پیش‌فرضه
‏
🎁
ورود روزانه ۴۰۰ پوینت می‌ده و روزهای چهارم و هفتم ۱۰۰۰ پوینت؛ یک هفتهٔ کامل ۴۰۰۰ پوینت
‏
⏳
پوینت‌ها ۳۰ روز اعتبار دارن و روی کدنویسی و سند و تصویر و صدا و ویدیو خرج می‌شن
⠀
‏قیمت و سرعت خودِ این مدل رسمی اعلام نشده؛ عدد ۱۰۰ توکن در ثانیه در مستندات برای M3 ثبت شده. روی API عمومی هم M3 با تخفیف دائمی ۵۰ درصد، هر میلیون توکن ورودی ۰.۳۰ و خروجی ۱.۲۰ دلار حساب می‌شه.
⠀
‏به گفتهٔ PANews از ۲۸ سپتامبر تا ۷ اکتبر اعتبار ورود روزانه دو برابر می‌شه و سهمیهٔ Token Plan هم ریست شده.
⠀⠀
‏
🟢
ورود به MiniMax Code
‏
📝
سند پوینت‌ها و اعتبار
‏
💵
تعرفهٔ پرداخت به‌مصرف
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrtkg7xPAJFGcJu8_-SbQKBukGy6Z5yVLqcN9NLSVtZpH0MATDHvBQHpnoKPYjX9azl6Jcx7Tf3WC1wUxzqFEuOxBTnU-KM77GiObSTzAcH98g-WGJLWZX_I29cJVErjBhpci9IXPdp6Zhdex_wecWxdS_1okM75YiCv_Aw8w_FQMkEFSZOxN0DU8MMGqA7D5qUtBYGivYXFTl-X-hbQIY1pVHFGwd9ZRrmOxj1iApUx1eR9-HBAccgVIoBVmFgxOcGmDjWp-iqQk95jKujINxeeZutZHsmfZd6BQkJI9Hu4-CXSpETsQ5QgBvkYFgp_dWgid2Fl69fCy1lDhLjWnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Railway.new
یک VM لینوکسی رایگان در فضای ابری
💻
از حالا railway یک ماشین مجازی لینوکسی به شما ارائه میده که از طریق SSH میتونید بهش وصل بشید
💥
برای استارتش فقط کافیه داخل ترمینال خودتون دستور زیر رو وارد کنید
⌨️
ssh railway.new
⚙
مشخصاتی که این VM در اختیارتون میزاره :
• ۲
هسته پردازشی
• ۲ گیگابایت RAM
• محیط لینوکس
• دسترسی SSH
• Python
• Node.js
• Git و GitHub CLI
• Chromium و Playwright
• Railway CLI
• چندین ابزار AI برای کدنویسی
🤖
بخش جذاب ماجرا چیه ؟
چند
AI Coding Agent
هم از قبل روی محیط آماده شده‌اند؛ بنابراین می‌توانی
Agent
را اجرا کنی، پروژه‌ات رو به اون بدی و داخل همان VM کدنویسی و اجرای پروژه را انجام بدی
⚡️
🌐
برای پروژه‌هایی که اجرا می‌کنی، امکان ایجاد
Preview
آنلاین هم وجود دارد
👎
تنها عیبی که داره :
شما فقط 60 دقیقه فرصت دارید ازش استفاده کنید ، وقتی 60 دقیقه شما تموم میشه به شما 24 ساعت فرصت این رو میده که فایل های که باهاش ساختید رو claim کنید تا در ادامه بتونید ازش استفاده کنید
❕
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2rWU4dmeRgf350OXy7zpM2kPKchF9mIuzrBg-9SPcaDZLMay5Ry1tdcT_eFT0Yr6RYFAxw2tbMXXkFOgklw_Xt3rLBFBBoV5dAHBiD_9lDp5_R5botZJcKkIRgG2jQQgUy38KT3PzJu9_oX3VrBcqP8MwRZoDu155y0TxDjRIN46jZJi4HxvazFx1C7o1kDDj-rCR9dXcF00UeUTkgiDaSm_1CyP-0uQlw37rkVIfbF1aXHahyqUpJkf02tcQ3xesi8H5rFpgSqlOW6X6nXHYxCT5jhdteil-Ea5UuMrB9lyB40OtThjHzyyGiLq4vIP0hX7egC94K0UVpXf5eXmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#حمایتی
‏
🏔
آرشیو Afsaneha برای افسانه‌های محلی ایران
⠀
‏یک سایت متن‌باز که افسانه‌های شهر و روستای هر کسی را با نام خودش ثبت می‌کنه.
⠀
‏
🗺
نقشهٔ استانی ایران با SVG خالص؛ روی هر استان بزنی افسانه‌هایش میاد
‏
📨
ثبت افسانه بدون حساب گیت‌هاب؛ فرم سایت با Cloudflare Worker خودش Pull Request باز می‌کنه
‏
🗄
هر افسانه یک فایل Markdown در پوشهٔ استان خودشه، پس با رفتن سایت هم آرشیو می‌مونه
‏
🎙
پشتیبانی از فایل صوتی برای روایت با لهجهٔ محلی
‏
📱
نسخهٔ PWA و حالت آفلاین، دو زبانه با چیدمان راست‌چین و چپ‌چین
‏
📖
حالت مطالعهٔ بی‌حاشیه و تم‌های فصلی مثل شب یلدا
⠀
‏فعلاً فقط سه افسانهٔ نمونه از تهران و فارس و کرمانشاه روی سایت هست و نویسندهٔ همه‌شان «نمونه»ست؛ یعنی آرشیو تازه راه افتاده و جای افسانه‌های واقعی خالیه.
⠀
‏
👇
اولین افسانه‌ای که از شهر خودت شنیدی چی بود؟ همینطور شما اسپوف‌نژاد؟
😊
⠀
‏
🌐
سایت افسانه‌ها
‏
📌
فرم ثبت افسانهٔ جدید
‏
🐱
مخزن پروژه در گیت‌هاب
⠀
‎
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddaxOZeXqUSTIVDzPKYYOSsKrIo_SUIN99GUFZHJKTVma1oJmW6kLm9Q2Ibw7Quu6iYqr_9kva5yXMBL_E4FzbudmHqSy59Kj7nSdPO3pMCcn0BtyRLXGX1E-gOHMmmSQSl2-qDj1kZJqjMeCa-CXLaGK-imsZHujOLVame5pFPCER5EI3r4nCwuqKrYUPvOkyNBRceDFtp0NxbaDlSzx2s8hzRigOVU3lB4aUdHVS5h_T9kLLK_4ZcvEHtFUNXLjFhVOipGefJYlN0Z099Z-6H8PKyNLzn-DxTI3cktIYre0J0UQy7q-QFIk3IO-gGc3sx_Hy2uHzoxX3tehPi5cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API برترین مدل های جهان
💥
Opus 5.5 | Fable 5.1 |  GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 Pro 0813 | Sonnet 5 | Gemini 3.6 Falsh
✅
با این سایت میتونید ۵ میلیون توکن بابت تست مدل های بالا دریافت کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMB1PdUx2vTw95wemvHOAu56Hk6b4z6kqmi1kSinEs_ISDUF5WrN0ONpkSrVcYv5EmMX8neR6tbZccv8p8Ht1C3XMcw3fzNpTrFuUL6DZ-_WiPyl8g0mjlAUiXw6fAQrIuESq20qQSgw7aRShM8lWU8bevy_cukAOCGXn5pR9k9WAy0A46jnyPtlXwiYprln77Aka_SGF4xqeKcEpTLsW8BHH3Q_P1_xwZswLSvaxQABpeJJx0mB0Idjm3V3Mo-OfZDM5n5JwTq5fY2n2nnt3acvaXsPO7eJrF9YYj7iLNfcV8g9Xu_FMw_-4WKAys6icWK3qXm51OIj87osipN33w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به مدل‌های هوش مصنوعی زیر
💥
🆓
Opus 5 | Sonnet 5 | GPT 5.5
✅
این سایت بهتون یک پلن تریال ۱۴ روزه حاوی ۲۰۰۰ کریدیت میده تا شما بتونید این مدل هارو استفاده کنید
✅
📌
برای دریافت کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2ZAuJl-7-4HHnkwbYgwPiay1Q9yTwREvhcneiXrTMPdMwtNTf8pxyqw9-c2i1qcr2uIhLJBQ9URshRj9Pn4nnaiJas4nYs7w0psFh1kkhK5OKKpc06fPy69b4g-rhjPcaobXkXsgYczBMxxts07J2kLwuZa4qsDhGEusfpcy9hohCAQcwu7L0Mk4bHnbmDchZRVoqMSVqg9C-N9KmVRhPjpY9vWxaTMQu3kEZWtQwZ8VLPAhD_966zfK2jcGwIMR6LrHCWVEccNQyDtgSxOaXt7OpHcb9wQKArjPEhyYqm2W8qUkorZIQhykjCCTEgSaByKQx4iQC1L4wWK7AlEZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
ادعای نشت اطلاعات JumpJump هنوز تأییدنشده
⠀
تصویر فروش دیتابیس کاربران این فیلترشکن دست به دست شد، ولی هیچ منبع مستقلی پشتش نیست.
⠀
💳
شمارهٔ کارت ۶۰۳۷۹۹۱۲۳۴۵۶۷۸۹۰ آزمون Luhn را رد میکنه
🏦
پیش شمارهٔ ۶۰۳۷۹۹ مال بانک ملیه، ولی زیر شماره اسم Bank Mellat اومده
⠀
آزمون Luhn یک حساب ساده: رقمهای یکی در میان را دو برابر و همه را جمع می‌کنی و جواب کارت واقعی بر ۱۰ بخش‌پذیره؛ اینجا ۷۷ درمیاد، پس شماره ساختار درستی نداره. ساعت ۹:۴۱ و محو بودن دادهها هم نشانهٔ قوی ماکاپ بودنه، نه مدرک قطعی جعل.
⠀
اندیشه معاصر نوشت هیچ منبع مستقلی اصالت دیتابیس را تأیید نکرده و شرکت ادعا را بی اساس خونده. بررسی Tom's Guide هم سابقهٔ نشتی پیدا نکرده، ولی ۴۸ از ۱۰۰ داده: سیاست لاگ مبهم و بدون بررسی امنیتی مستقل.
⠀
پس ترجیحاً از سرویس های بررسی شده استفاده کنید و اطلاعات کارت را داخل فیلترشکن وارد نکنید.
⠀
📌
گزارش اندیشه معاصر دربارهٔ این ادعا
🌐
بررسی Tom's Guide از این فیلترشکن
🏦
جدول پیش شمارهٔ کارت بانکهای ایران
⠀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLENNiMaGXyuXHlcO8Qb7JjTrJYcNm9N_xzbvNDZ-Z_DHH4ZNkhv2l40_o4AKHs324PZYbWGBL2MnWRLsI3_3X4c-QKNmSWH3TegfQ2iS-IH0W6kVIBZUiLrz_JswJIcOv9Q1LvHiwpvScq3tz1Ao6BDbMEjBK8dzp18eQ4174PQqzDzQoEOxafQpidhOIdB71_Wt7BXYPZmv_CoxNzJHJ24OzFNwJZrn-XfC65uilW_Nm83ajN0PhT5_Z8EM_m6cMvu_NGP---09oSrwqNe3PLSPm-dAg5AJ2WEl6pV76p7Ru4rYZASg7pD_Vn8wQhB9YeTnaoXH8XysVfP-1sZFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های SI در یک بنچمارک سلامت روان، از پزشکان متخصص امتیاز بالاتری گرفتن
‼️
- اپن OpenAI نتایج یک بنچمارک جدید در حوزه سلامت روان منتشر کرده که توی اون، چند مدل پیشرفته هوش مصنوعی تونستن امتیاز بالاتری از پاسخ‌های نوشته‌ شده توسط متخصصان سلامت روان کسب کنن.
🤖
مدل GPT-6 Astra: ۵۷.۳
💠
مدلClaude Opus 5.5: ۵۲.۴
✨
پاسخ متخصصان: ۳۸.۵
- البته جالبه که متخصصان بالینی در واقع جریمه‌های کمتری دریافت کردن. طبق توضیح OpenAI، دلیل پایین‌تر بودن امتیازشون تا حد زیادی این بوده که مثل زمانی که واقعا با یک مراجعه‌کننده روبه‌رو هستن، خیلی کوتاه جواب می‌دادن؛ گاهی حتی فقط با یک سؤال یا یک جمله.
😁
- در مقابل، مدل‌های AI پاسخ‌های مفصل‌تر و کامل‌تری تولید کرده‌اند و همین باعث شده در این بنچمارک امتیاز بالاتری بگیرند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNuMxOCl7jrPWz4crDbV8KuXuGgfOF_TCKBxdLNWuPjmoWs52Es295D3gbjQdLNedR8rpp-1OI_8f7z-ccMcb_Hc-wwqYOPZHgX4UDbN3TNmaGSdS36tzhOP9UHETO4CAa3fLS9OnDbyY64DUf29uwD7Us34adgiJTjEFPy72foZ_yzvP5veztkhg68AQGCuhk17DJVDwg4Gu7k9wD9KzP8SXONJz496PiplWBbkfp80amMP93CyxfeUgT_gN6M7NKXIDhXPDaY8YmwANuGt5mdUmefeSKz5RiR3tlDbssN15gt8VqYdTqW9M0F86hpM0ahvMYOk29Rmi2pNDPc2aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
مهساNG ویروس نیست — ماجرای اون عکس چیه؟
چند روزه یه عکس از مقالهٔ MVPNalyzer دست‌به‌دست می‌شه و می‌گن «مهساNG ۳ تا از ۵ لایهٔ امنیتی رو رد نکرده». مقاله رو کامل خوندیم؛ اینطور نیست.
اول از همه:
این مقاله اصلاً بدافزار بررسی نکرده. فقط رفتار شبکه‌ای ۲۸۱ تا VPN رایگان گوگل‌پلی رو سنجیده. پس «ویروسه یا نه» اصلاً موضوعش نبوده.
دوم، اون ۳ تا اشتباهه — ۲ تاست:
تو جدول مقاله، «Leak (29)» و «DNS Leak (24)» یه ماژول‌ان؛ دومی زیرمجموعهٔ اولیه. کسی که شمرده، یه ایراد رو دوبار حساب کرده.
واقعیت از ۵ ماژول مقاله:
❌
ترافیک رمزنگاری‌نشده
❌
نشت DNS
✅
نشت ترافیک کاربر — پاکه
✅
قابل‌شناسایی بودن (۱۴۳ اپ گیر کردن) — پاکه
✅
ردیابی و Advertising ID (۷۶ اپ گیر کردن) — پاکه
✅
کانفیگ ناامن OpenVPN (۱۰۷ اپ گیر کردن) — پاکه، چون اصلاً Xray استفاده می‌کنه
یعنی نسبت به بقیهٔ دیتاست، جزو بهتراست نه بدترا.
اون ۲ تا ایراد یعنی چی؟
🔹
نشت DNS: محتوای مرورت رمزنگاری‌شده می‌مونه، ولی ISP می‌بینه چه سایت‌هایی رو باز می‌کنی. برای فیلترشکن ایراد جدیه.
🔹
ترافیک cleartext: مال خودِ اپه (مثلاً گرفتن لوکیشن از
ip-api.com
)، نه ترافیک مرور تو.
یه نکتهٔ مهم:
داده‌ها مال نوامبر ۲۰۲۴ و با تنظیمات پیش‌فرضه. اپ از اون موقع بارها آپدیت شده و نویسنده‌ها هم ایرادها رو به توسعه‌دهنده گزارش دادن.
✅
کاری که باید بکنی:
۱. بعد اتصال،
dnsleaktest.com
رو چک کن؛ نشت داشت، DoH یا Remote DNS رو روشن کن.
۲. سرورها دست آدمای ناشناسه — بانکداری و اکانت حساس روش انجام نده.
۳. خطر واقعی، APK تقلبیه. فقط از گوگل‌پلی یا گیت‌هاب رسمی نصب کن.
💡
و یه حرف با کانالای عزیز: ترسوندن مردم ممبر میاره، ولی اعتبار نمی‌سازه. وقتی یه مقالهٔ علمی رو نخونده تیتر می‌کنی، به همون کاربری ضربه می‌زنی که ادعا داری ازش مراقبت می‌کنی.
اصالت مهم‌تر از ویوئه.
پستتم ریپلای نمیکنم. اینکه خودت اپلیکیشن مود شده خودتو میذاری چنل معلومه چقدر به فکر پرایوسی و ترکر هستی.
📌
فایل کامل مقاله
🌐
صفحهٔ مقاله در NDSS
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjVnxx3E6JI-LY_7qfD3fpKHx6yn3Cy9ziokCJk_VN89Ne0f9kGTiO4YY02vm8aKeqZpC4Gq_EN1HZ0o2KRCUtu67Dciw4gofM7FSg4IcgoU1TIFbePK0Y__dbtP-FXvm-0o5tAG-zdvTr1tLoM7gBkRrqtWagDeu3zUUNQtW_-aESjTgHrRwO2wFjZomn2HZs-QXhO9GL9s98MqYkm_ifmDxXNuG0qmxWsJNPQUYsx6flg4rP5v2LE3kpPLFrRRax1SFbXi4xfZl7XYQia1CW3FTYq8bpqfzYxVwXioAe3P5ehLI8O8gOk6WvCu9COTomFaLUC6CIvs28enP0Qbkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">500 دلار برای دسترسی رایگان به برترین مدل های جهان
💥
🆓
Opus 5.5 | Fable 5.1 | GPT 6 Astra
✅
با این متد میتونید از سایت معرفی شده ۵۰۰ دلار برای ۱ ماه برای تست بسیاری از مدل ها دریافت کنید
✅
📌
دیدن آموزش فعالسازی
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTA1-nF2mhPj4KmLuHTw-tM6PbwPtgGPaaiBj-awx8DcuTmkl9XlvQUWZKxObZju2fH9DB-P492-5Bvs17ty6w1wXVt6-asT3ekGL21moNgQpt8xAK-AQVODyFC3SAvLth7YuzA92D6e-79XnyLbLLh7cq-dIM5zG6InBF_VKzgiXjRJgapqXQB3GaC2X3Ct64dt3tZ8V23YUdzw0xrHBTfgWXn9lO0B2zLznTrejbnpxE0q5I--CNTLEvmSuneUQQCuiguanaNr8qBp4tojAG-0zPo4AA1_W7iEKbp7amO8ALjCNCKW6baISQTVBGB4QnH6DF4ZXlT0Rjp77zxRrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwkrdezXDL8IURZ9zeKyKDd6AaJGuY0Q23_ALroUUL4TrrSjoM7hNJNHbtL9qB2nP-pJ0Z_zQvTMKDEPe-hCfoh4aX34i8n40dkUK1ZeSM3cILJqCLkFG65axhs2ft7yIV63QeCeOylJoKTbzwE8PpleVJ74b0EXVm_L-OnBbDyHYxbEbPOQavNiL4KLnoMcpWtlK6RrWnYcjU9XYfX3Ixriu-hFDzsGmMf9tneEQpaNwE9XtCdA4tTWom7xUZ8P9T89YV0iF6VPQ7vQJ0J9nDILiEe4JI78bO1NqVl3zCBb0xVuiCQpNKLT7SGqgjL36qTIjwyqrXkDjbh8JuKsuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌈
کنترل نور قطعات با FullRGB بدون نصب
برنامهٔ FullRGB نورپردازی قطعات رایانه را با یک فایل اجرایی و بدون دسترسی ادمین کنترل می‌کند.
🤔
۱۲ افکت
: کالیبراسیون جداگانه برای هر زون نوری
🤔
پوشش قطعات
: مادربرد، رم، خنک‌کننده‌ها و فن‌ها
🤔
دوزبانه
: رابط انگلیسی و فارسی
🤔
فقط ویندوز
: نسخه‌ای برای لینوکس یا مک اعلام نشده
💡
نکته
: موتور OpenRGB داخل همان فایل تعبیه شده و نصب جداگانه نمی‌خواهد
📌
صفحهٔ پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpd6KwprEBcHhmjAYzGupOQL4TWFFb1AQvZmfYJ8qiZrziMFCOxqfWj_TBEqp38vXYdu2Ywuno02hWesnuDrnWYsW97Mfo0OYCnXX9odvxvIVqfwdnsR2sg3ChwkRlRSoFL3SMf0VtEGBJjV473_S9C_Sr7FD312Zyw2x3gKvMzy_r5luuSMTI7u1y6pebi6-uH8fNra7u2wtdbAH3xNOIlVre24BZIT7rHiWNvwMEg4bhUK4u8wnfXtdpoSgDIYXiBpv0DseCnGbm_h2ZdPGPefKOMvfCHdtS8zZyEQbeupV2NngO3EzUKG3Y__2A1vlMBbdIJg0zEPpo_-DVCvgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🧩
#حمایت
| پچ راست‌چین هوشمند آنتی‌گراویتی؛ خوراک بچه‌های برنامه‌نویس!
‏رفقایی که از آنتی گراویتی استفاده میکنن این ابزار خیلی کارشون رو راه می‌اندازه تا بتونن فارسی رو درست و حسابی و راست‌به‌چپ بنویسن بدون اینکه کدهای انگلیسی‌شون به هم بریزه.
‏•
🧠
هوش مصنوعی دوزبانه: با فرمول نسبت ۷۰ درصدی حروف، متن‌های فارسی رو راست‌چین می‌کنه و کدهای ‌LTR⁩ رو دست‌نزده نگه می‌داره.
‏•
📦
فونت‌های ۱۰۰٪ آفلاین: وزیرمتن، شبنم، ساحل و صمیم به صورت ‌Base64⁩ تعبیه شدن و منتظر اینترنت نمی‌مونن.
‏•
🛡️
امنیت کامل کدها: پنل‌های ادیتور، ترمینال و لاگ‌ها کاملاً سالم و چپ‌به‌چپ باقی می‌مونن.
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQImL41KS90l5wq5JsOUCObRyzr5gCdY_sXgmQlK9EHPAU00IPiFF6ttC5GI6L6OH_jzx03TMiavLVodD2DDHivBbvaMd9bphCAMHVoOf3JeuQtNFfuTX3t8BF79GPWfqXE17uh60LaqFKaZBDuTGPa-yygm9W_oWHcRmv1ALBRjNEGGXuO9u_w55lIF9d34IqDk1H4pJN5n6TxlWe9VQqi3SiiLQcY35s2GuX2eKHPuCk-1ZrorEwHh70PMfl9f33L4eAQnRoUGXHYA9plMtydGpyF7DJG80YkRmZaekC2twIBguxwZznQ1CsYj8mykAR8HWOdSJYV0mOMCanTzYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2OJs1XfzPCz28G8KyGBS04TcpSCIfzl1eWe6C8apmSxeTl7uIdJY6rhUDLW723-oYb_WJtJrxA2MC-B9p6Qv6pxuBmaJ5VVuuYZThYpJuJtcjIBzxgPBSlIFqiCukmJZuxl8XVMvy45zecRQR_KrdKdU2YSb74IZGrizXr-oV-3p63P-F99C3sk-Y6vRGCwRTrtai4XQ2F8NwMzjYYEAp7Y5ocJs3KpenulEbwmuOjpHVSHkVScDcovLCUruYweCZAl6wLCOURyTjPyHRltTX-4ZmKlqSHt3sq-j2He_1s42gPpcG5OxTTL_4ROJlZDXI3kB7e_VN0YI91KU-f7ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
در
یافت رایگان ایمیل دانشجویی اسپانیا
با این روش می‌تونید یک
ایمیل دانشجویی اسپانیایی
به‌صورت رایگان دریافت کنید و از اون برای
وریفای برخی سایت‌ها و پلتفرم‌ها
استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell
| METHOD</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
نکته مهم برای کاربرای Antigravity
اگه اکانتی که باهاش کار می‌کنید عضو یک
Family
باشه، حواستون به این موضوع باشه:
لیمیتتون در حالت فمیلی، به‌صورت
اشتراکی
بین تمام اعضا محاسبه می‌شه. به این معنی که اگر فقط یکی از اعضای فمیلی مصرفش پر بشه و لیمیت بخوره، کل اعضای اون فمیلی هم‌زمان لیمیت می‌شن و دسترسی‌شون محدود می‌شه!
💡
پیشنهاد:
برای جلوگیری از این مشکل، حتماً از اکانت‌های مستقل و خارج از فمیلی برای Antigravity استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1A7SoIWTR4xxYQ_CEpKNfRQ7sXuXlrhphctFEZEuiTSKiYsSAwpYkp-j9thzOvwQvrTlUip04N7rT3LzkApQK1O4OkgzAtVaavUdp5H3fvhftjFOZ5wXue0tELqATg-eQG_c9fd7lC-Dfn6ikNotdN-0IXkPhMz2mXgXlXqjg21avYCct7jFgpLM5DDp4bFinGIhAGJxjKqso-lHWE5B3udGzXFcqL8J_1fKkH33tVjqwKlFeXgcuziY6l_0taiZZ-aXnRe9IYKQoTWDSn5QlLTbGVzIQhepeaO5RvmcBkJr8YPrVaq5TtV8bmYUaqbGlY8AIlI7ExQGavSUp921g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
طوفان جدید گوگل، جمینای ۴ به زودی...
💎
کوری کاووکچوغلو، از مدیران ارشد و مغزهای متفکر گوگل دیپ‌مایند، بالاخره سکوت رو شکست و تایم‌لاین اس آی به شدت مورد انتظار
Gemini 4
رو فاش کرد!
🤯
اگه فکر می‌کردید هوش مصنوعی تا الان پیشرفت کرده، کمربندها رو ببندید چون گوگل قراره بازی رو کلاً عوض کنه.
⚡️
چرا این خبر مثل بمب صدا کرده؟
🤔
پرش کوانتومی در منطق:
جمنای ۴ فقط یک آپدیت ساده نیست؛ قراره مرزهای استدلال و پردازش داده‌ها رو به طرز وحشتناکی جابجا کنه.
🤔
تیر خلاص به رقبا:
با این تایم‌لاینی که DeepMind منتشر کرده، گوگل رسماً شمشیر رو برای بقیه غول‌های هوش مصنوعی از رو بسته تا بازار رو کاملاً قبضه کنه.
🤔
یکپارچگی بی‌سابقه:
حدس زده میشه که این نسخه خیلی عمیق‌تر از همیشه با زندگی روزمره و اکوسیستم ابزارهای ما ترکیب بشه.
نانو بنانا ۲.۵
هم احتمالا باش عرضه بشه شایعات میگن
۱ اکتبر
میاد تقریبا یه هفته بعد
👇
به نظرتون Gemini 4 می‌تونه رقباش رو برای همیشه کیش و مات کنه؟ نظرتو تو کامنت‌ها بگو!
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnORrKQziAqCSihEF3crYU96VKNETLwr4dbzFGUuVlaT1CGjwOF-e-jr4431irXx3mGFikaQs7-b4cVKkVvJdLUwGDXQVWzLQCtHNDEjASzH5hkq_JBWyU4cOpjVniwQT96W98nbQPCQxF09svu5WKjAkVTDFLZ4JMU0aWaaIE51jhF_DsxtpZ-d109d4Uu0v9agceoqLVHBTKT9qKscd0eW52G3ObxmGtfyN9gna2Jxm2MkfFZ0LOS69OokeMA4i-aTom2diR7v2ChwCm8DjxqaRd9vCwKEWKg2sFqcO9ftn50T-x3sVcrqn415O6jALqgZMGJKTPXl7Nz3xur5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت
| کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی
به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک
: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
داوری میان گزینه‌ها
: چند راهکار یا مسیر پیشنهادی را می‌سنجد و برنده را می‌گوید
🤔
شکستن حلقهٔ تکرار
: وقتی دستیار یک کار شکست‌خورده را تکرار می‌کند، متوقفش می‌کند
🤔
نیاز به کلید پولی
: هر میلیارد توکن ورودی ۴۲ دلار و نصب با پایتون
💡
نکته
: مجوز MIT برای خود کتابخانه است، نه سرویس پولی TypeSafe پشت آن
این پروژه یکی از ممبر های چنل هستش.
جهت ارسال پروژه هاتون به دایرکت پیام بدید
❤️
📌
سورس پروژه در گیت‌هاب
🌐
راهنمای رسمی فارسی پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7868" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7867">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPwQYEzpxOl7zmRSurzhcUNaH9SDxBu2C1In9gsR8HywyF2dze_hWrYnGhdF8hTm3ueGcBsm7cil__gKbPrVgUIeiFG465Y0sUBpbMIuxsaZdDXxmPq00UV2qm5brPMXEfsfh9VXoZa4lKshRdh2r-T8EfUSTKfsL-hnKQKbVW2Y4TBiRlYKdD0JgPIinoEJBkptJZuxz62193ZCsSjcrHZqWcnvyiNE3JS1uOwwDv3nCoSnUfqnuYrrn4ibbAH-3JiSZegqMnElthEFMroSjrKemLf5b_b6923SGPPWu2Xfaze-aqISdRYxPp7WMYnOJhUYlgvB26lA1XPvobOZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💻
ابزار Perfect Windows 11 برای بهینه‌سازی برگشت‌پذیر ویندوز
با دسترسی مدیر روی ویندوز ۱۱ اجرا می‌شود و از یک منو هر بهینه‌سازی را جدا روشن یا خاموش می‌کنید.
🔺
بستن ردیابی و تبلیغات
: تله‌متری، جمع‌آوری داده و تبلیغات نوار وظیفه خاموش می‌شوند
🔺
پیش‌نمایش پیش از اعمال
: فهرست تغییرها را ببینید، بعد اعمال یا بازگردانی کنید
🔺
پشتیبان‌گیری خودکار
: نقطهٔ بازگردانی ویندوز و نسخهٔ پشتیبان رجیستری ساخته می‌شود
🔺
خاموش‌کردن هایبرنیت
: فضای دیسک آزاد می‌شود ولی راه‌اندازی سریع ویندوز از کار می‌افتد
💡
نکته
: مجوز MIT دارد؛ استفادهٔ تجاری با نگه‌داشتن اعلان حق‌نشر و متن مجوز مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7867" target="_blank">📅 16:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7866">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkv5XrsN2Vh0RNh-cViGIppH_BdUD5ttxD8HXVI76lT65loc1fCSS77vwrgYAbMKu95YOXw0v0-cD_b3Xjghb-fEM6iqxz2489e5K-V690gz8HRfgQ5Jr4ivt6yp8SSdnxVupmonyijLTBUv5xHcFCxk2e5gpSN0TxLvFw5YN03obs9PPI-EtMyq2cdquOlNJAs0sK25yyLmbU3AT1g9MDwOA4XckeBEu7pszCfokiRIuVq6SsjFaK04yw5oNi0bE5-dbKRZ6Y5GYrDMh5n1k1EWj3m8EK34-42mjbHurNzThc1_yHPpt16dGZVUoDaWNb8yAV_frfjSFZvsXFB_zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧮
مدل Laya که به‌جای نوشتن جواب، تصمیم می‌گیرد
یک ایمیل و چند پرسش می‌دهید و برای هرکدام گزینه، نمره یا بله و خیر با احتمال می‌گیرید.
🤔
پاسخ در ۳۳ میلی‌ثانیه
: زمان اندازه‌گیری‌شده برای یک پرسش روی کارت گرافیک
🤔
بیش از ۱۰۰ زبان
: خودش زبان متن را می‌شناسد و مدل مناسب را برمی‌گزیند
🤔
دانلود مدل و اجرای محلی
: بعد از نخستین دانلود، روی دستگاه خودتان کار می‌کند
🤔
نیاز به پایتون ۳٫۱۰ یا بالاتر
: با دستور
pip install laya
نصب می‌شود
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با نگه‌داشتن متن مجوز و اعلان‌ها مجاز است
📌
اجرای زندهٔ نمونه در مرورگر
🌐
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7866" target="_blank">📅 13:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7859">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dr_l01_wnlPBQQ59OV6uOdnmlWsmiJ0eOFKXbcq2sYAziLHz2BW2c8cl_vkOMa9FfBuRmVroGjyXXKWCUjPGd-Aoo5GnFwOdWdGUGQ4hC-105UQgYfSYTJjF3QNNgQo_B6jcC_iCJBbIj_h6lHGiEq55dzx-NZykDDQDNseI-LOJG6Zl5vB7iUWD0VcokwN9EvtGCgaZCX11GhBoWJXJqMrkkUg6Gmw5z270kMNbq7WNFRo-VHNsRsf1THf68TOkSGKjfMJWX08kr5b8j-KdyIiz-Ldsv8EDdj2xn-Jpb3rZXIueOD34W56uMJO3TQME89DdRU0jZq-va_oHG1iuTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aVFIrupCyHh-zBRwL9Q0FOfk0GBLgu3pFMKEkR6dsvWCtQZ68vW19vm7D_HEh7weWeaTDA2Ajpb3Pd9RXp3E4zU9gV9eNQzocJYLYuw2sclGhe5NCyAgQar7pHqRiPhgmhcAn13f2HTBeFDv9nliNEGHH1wlsavFp-uqFXnwAabsboZK1ks7Snhay5h2FlqPqw_Xufzl169X02chg5ePVXjpQmo2zG7OnfeobDqot-bkM19CUMHf5fHCEQUwig7G-7I86h5IdenlLQsu6a1RDTtX8mKbSM_qjnXNNnXZTOv4dmsTITFKKcQbXRFjZxHHU3oNw9hGD2I6nxq-29YlmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VDHxINz-zIexMtxEzqPMsn01nWhq1hfotnpvTCAPjfRAD6Qz47DAtwrjcvGUq3b7EZ4omq4NeVhWXGWAFhFrZU45cbR0_zBOEnxw6-pmvZgpRQZsOtU2tuEmkuZ6b0bRvaIn56UHdrFXqHiw0cK07NqZAvmn1FSMlLX9GpGSdi_vfONHHzGNCmRJgDDuNR6v842-t_lY44cq4qbwxYV3vF2fgrOM6JYccjNT4Yp8TFTf-3wQMvfGI5gWdDSOexfTo9NsXhH2Llvh5uSlF-vS3cPry-lsX1EuwvlbF-W0j-AdFx4rgmuAdwcviic3PA-HecTbWbD7F7Um_BBmoIfJfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=v2JLrmXBw7Eij2JrZ3Veh712jPEJSk8UTVMJp8-LCDBS_K42OfwPLLpY0nRLDy9ETOkbgnPNPktEczqwFJ6x7sMlxo5nakTlJsQ4BqHUFkuL5JMkJHfetBgP3VezTm2dBHODnnS7n31YniLiVpJZwuXhoc4M59-k13C-uohlmBfk3cXpdqYX-p34ItzBJVl7uQW0TqLAm-jphL0nc3-3J6-9X5DRXVyN8uz_w65GOS05YhyRhYwxca3G0eDB8hq70dWLjlgArWNwCq7bSpT1UN5-EGUyPk09ZbQqbhtxKfGmtrxCzYcAUAbaLnKJawAFXjMd_PUOAr4x8SFtNHVCww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=v2JLrmXBw7Eij2JrZ3Veh712jPEJSk8UTVMJp8-LCDBS_K42OfwPLLpY0nRLDy9ETOkbgnPNPktEczqwFJ6x7sMlxo5nakTlJsQ4BqHUFkuL5JMkJHfetBgP3VezTm2dBHODnnS7n31YniLiVpJZwuXhoc4M59-k13C-uohlmBfk3cXpdqYX-p34ItzBJVl7uQW0TqLAm-jphL0nc3-3J6-9X5DRXVyN8uz_w65GOS05YhyRhYwxca3G0eDB8hq70dWLjlgArWNwCq7bSpT1UN5-EGUyPk09ZbQqbhtxKfGmtrxCzYcAUAbaLnKJawAFXjMd_PUOAr4x8SFtNHVCww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
مدل مخفی Space Bunny Alpha رایگان شد
مدل مخفی Space Bunny Alpha اکنون روی OpenRouter و OpenCode در دسترس است و فعلاً رایگان ارائه می‌شود.
🔺
پنجرهٔ متن تا ۱ میلیون توکن و خروجی حداکثر ۵۲۴ هزار توکن
🔺
پردازش ورودی متن، تصویر و ویدیو با تلاش استدلالی قابل تنظیم
💡
نکته
: رایگان‌بودن این مدل روی OpenCode فقط برای مدتی محدود اعلام شده
📌
صفحهٔ مدل در
OpenRouter
🌐
مستندات رسمی
OpenCode
✈️
@ArchiveTell
#Ai
#هوش_مصنوعی</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7858">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNulMcIqBQa5O2DTOcYbvmLKfNu6xbpanRG8i3sGLS8gx5-0Wk5B7l46v2NNIdb-Qe6CHJLqfke6wv3V1AL6QcivGhaaXQ8v8-BtJwCZ8obd60z1ofc46OEyrj70zPwIJCA-HnKxlcA3y--G_4AVBcIzgyHN-rc7tMhVYWhgN5vJb_Oqs0Q5Hl4GrOmfV6ZJNu6gJ_PPJBp20-7hWwg14UHub2bBbKh9Em1IfqhgfZwHBoQGqg4Ck7T-3xSLoWoGrWKL9UY7XaJpKZDa_k9G456sWyJTi6rz5gpfDZESzDuRjBaDZ8u6-JkNdImBSmpTZ7vXdLXgq_DRCxsDoVl4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام دوباره یه قابلیت جذاب اضافه کرده
💥
🔥
حالا وقتی وارد پروفایل کسی می‌شین، بالای صفحه می‌تونین ببینین شخص معمولاً چقدر طول میکشه تا جواب پیام هارو بده
🥵
حتی یه رتبه‌بندی هم نشون می‌ده که سرعت جواب‌دادنشون نسبت به بقیه چطوره
🤐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/ArchiveTell/7858" target="_blank">📅 20:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7857">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEm9tGOaolE76nc9w3762AEnu_lXqiJI3c0KMkfqC2KQxDgxaq7K6aEAENKLSg2Jq9ypB1ONJplen0Ko9sY9mfwF3qQfziUS8XdvNCxBURhDzrOnzquvICbwVaemZNtwL5D6iuek-LzFTIDCOHTcU-ZRd19oCQWQHq35-oeXE27b5a37yJQcUDCTmPm7FBePES73bh7nicF5Qr40Yu5Tg6kvcVkjKh9QsRgdvt0sdUBxxr1uXZ3v9G92eOG8Fa9j0D6fYv4-tWJLKADYHJV38nTk60Q5xUeDu-JvQdGzmjIbTgwGiYHJVtGeIHOwbXPuBruIrx3kickWxarBxdWtgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✈️
نرم‌افزار TeleDrive برای تبدیل تلگرام به فضای ابری شخصی
فایل‌های شما را در یک کانال خصوصی ذخیره می‌کند و ویدیوهای ۲۰ گیگابایتی را یکپارچه نشان می‌دهد.
🔺
پخش مستقیم رسانه
: ویدیو و صدا را بدون نیاز به دانلود کامل پخش می‌کند
🔺
رمزنگاری انتخابی
: نام فایل‌ها، محتوا و پوشه‌ها را با استاندارد AES-256 قفل می‌کند
🔺
همگام‌سازی آفلاین
: فهرست فایل‌ها روی دستگاه می‌ماند تا جست‌وجو بدون اینترنت کار کند
🔺
نیاز به کلید API
: برای اجرا باید شناسه و هش شخصی تلگرامتان را بدهید
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری با حفظ متن مجوز و اعلان‌ها مجاز است
📌
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7857" target="_blank">📅 16:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7856">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7856" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7854">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3invTh-jkLVQPr3mjTJR4Hne3ojOgJg5yR1flowS5f-1I0dcA_n-H-Pib1Uxk1GkFmdV6WVpmQEnPGfTzeoHm5jSSsczwS0H93kQmDoWmVNAZgLWMyBHHQEk43Pz4mVVdN609c9hO0lpdVTpkx7OEdYuSRBkDWpzHfDeSSYA4CPOVvMNiMeneVjGWZaoQKuR3Er4JkPE_OxdoX8FLp9aAqYBADm_embaHrslnAWlpqBK9qehhacIQiOP9k3SOdtaSSvtJ-SZg1zXZLtiUEZOcu8QgM217OsCJCuQQBfNmbsoQF4LRAx29UmuEiPIJX4kJb3hiG95d3INaDtWeiIoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7854" target="_blank">📅 12:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7853">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7849">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=k8LaXaqBfpZLQoXrN_Q67ds326GfcclN9w4kKl75AgbCovXMm26K7cTF0pyCuCDsy2RU7e_lUeDLcsLoAECaI2JCtmaztQBFVnf5cJkfmq6WA0ZsJdoHwjhxhuNKB7ruiszFNroaIhi8wJ4IHiz1bNDF4nYzZNu0A7oxGYk8836Wc0QM1_kLUdDu5RhQ9e7k5TOgMXX51jR6LGmfYfpgJgpoDN_9kGQpp3V90_Y_wi1DJmQ4zpQEJZVWY9yPre0ggASfFqi9l-gKOplBJnTv4rbklcQES3vB04clr06wk64fUDVqil4HDcxYdSJ0juqURv53ChI1utK5jObWldqAnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=k8LaXaqBfpZLQoXrN_Q67ds326GfcclN9w4kKl75AgbCovXMm26K7cTF0pyCuCDsy2RU7e_lUeDLcsLoAECaI2JCtmaztQBFVnf5cJkfmq6WA0ZsJdoHwjhxhuNKB7ruiszFNroaIhi8wJ4IHiz1bNDF4nYzZNu0A7oxGYk8836Wc0QM1_kLUdDu5RhQ9e7k5TOgMXX51jR6LGmfYfpgJgpoDN_9kGQpp3V90_Y_wi1DJmQ4zpQEJZVWY9yPre0ggASfFqi9l-gKOplBJnTv4rbklcQES3vB04clr06wk64fUDVqil4HDcxYdSJ0juqURv53ChI1utK5jObWldqAnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7848">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">چند API رایگان LLM که شاید کمتر شنیده باشید
🆓
💥
اگر به دنبال API رایگان برای مدل‌های زبانی هستید، چند گزینه کمترشناخته‌شده وجود دارد که در حال حاضر دسترسی جالبی ارائه می‌دهند.
🚀
🔺
Atria
بعد از ثبت‌نام، 100 میلیون توکن رایگان در اختیار حساب قرار می‌گیرد. مدل Atria-Dawn-Preview با کانتکست 256K و حدود 50 درخواست در دقیقه در دسترس است.
🔺
Routeway
چند مدل رایگان بدون نیاز به شارژ حساب ارائه می‌شود. سهمیه فعلی شامل 5 درخواست در دقیقه و 200 درخواست در روز است.
🔺
Selora
یک پلن رایگان 14 روزه با مدل‌هایی مثل Claude، GPT و Kimi دارد. سقف استفاده 30 درخواست در دقیقه و حداکثر 5 دلار اعتبار در هر 4 ساعت است.
🔺
ShareLLM
120 درخواست در 5 ساعت و 600 درخواست در هفته ارائه می‌کند و مجموعه متنوعی از مدل‌های GPT، Gemini، Kimi، Qwen و... در دسترس است.
🔺
Vireonix
بدون ثبت‌نام و API Key قابل استفاده است. یک route به نام "auto" دارد و طبق محدودیت اعلام‌شده، تا 20 میلیون توکن ورودی در ساعت ارائه می‌کند.
🔺
OdiRouter
مجموعه‌ای از route های "free-*" برای مدل‌هایی مثل Claude، Gemini، Qwen و MiniMax دارد. البته پایداری مدل‌ها یکسان نیست و بعضی مسیرها ممکن است با خطا مواجه شوند.
📌
جمع‌بندی:
برای تست API، پروژه‌های شخصی و ساخت نمونه‌های اولیه، این سرویس‌ها می‌توانند گزینه‌های جالبی باشند. Atria از نظر حجم توکن، ShareLLM از نظر تنوع مدل‌ها و Vireonix از نظر عدم نیاز به ثبت‌نام، ویژگی‌های قابل‌توجهی دارند.
✅
⚠️
سهمیه، مدل‌ها و محدودیت سرویس‌های رایگان ممکن است تغییر کنند؛ بنابراین قبل از استفاده جدی، اطلاعات به‌روز هر سرویس را بررسی کنید.
﻿
✈️
@ArchiveTell
|
#API
#AI</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7848" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7847">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ek7bG0IrzKUyn6w0YxNSz1fUc_U0qYmUu5oxnbAZkH41M_m_DY0r8bQArVuzs1u_Pj62t4hMP9MhovyIIIonhEwYruC9T_9h8uHPz9zkVeHl-ymGs-B39wNjJceHSEMOeOHcssWUyZq6IXHF3TIFlDmX_SwP9GEJ1Gd7vNph5aVGwzMW3Ukz8Cn36DYu0FemfqqF5S_GRqaTDCCcmb5oYlSGvUDh2UL_GdBIGcRR-lu7gfduPMXp4seH4VUqK_pLAC1M5H_1_LZ7rG5Ud67rM5rokXtu5CjL_CUkqJGvOUfnkcqXM_w6TIJt374pJ_hV3kEdq8WKO81XDvX_xzvMkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک 3 مدل منتشر شده امشب
🚀
مدل Opus 5.5 با اختلاف زیاد در صدر جدول
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7847" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7842">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pkCs4kG4UiUMsM-OUxZPL2dsbygBoJ_T6Gp_64tBODXlzWV3Yvml-ETuuyWf7LwcsSi02xxC5dw5QPQIWpqGyDg9lmSnssZ0QmifB0hpgYLoHT_AliFxdk8ReY6VqDYvPgWqLs3BXtATYBiFMBPZ-bYWKxHjjYm2IR4En1FfC1lF9hyuZYAepfTumfXadiYQrQI41ZQZdjTXnlPtml89Lvdl-kKd30JrfhBd6bkReIGYmd-XWNh7u-aBowFAvQAspyf60PCWcZ3S8U1pWZTPeWYBvJJdcTkl_qHA7cSZEhFBT-LtL0PD1Zzb0UI5ujwnDDQ1aOqQ-1l14ejFHSuUmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfce0h7WCW7mZecBA6dHulbZLHVrW4zKprOlIHWJMPzDiUHvMR991JjXDl4LsXQANk8Fl9xbX884KkTOFKm-mk2U_AplL2jKnyGqUrfHEptsDMWjTcBwERtsCDAVcZ4bmtgwe-_j_iJUjZfzF_HNsFEfJszvfNElW5WJ4d1VuKTOZhIQQnLVKoKOAAUY0szRLNP29EHhuRa-LZcEb9wgrfewHTg643Aoyf_UuOQhkVfvGKvvc_ij_NIWMdngnoFeSYplqHmpVBhwM1jZim3zpFbaDrl4XqVkYtreDLd8ZXy3cP4LnUahsRfSD-yPzp2r9y1kEv8Kg_kPyrkOd7aFrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ccvil2L6ocYqQYDdJJIRmjHbdWOcbdKquQJRlAzJWqMHxnJz-TvUrb67wY4uJ69BY8lPbqtiCTeGUI6s05a2Ov3T7W61etwBmW9nw8NO18WZFqe4owd0Hh5HqknavsTBexf3ChCUqQ9PGBt5LDwBh3fmcMwTB3pGW1rpV4bE8v6p0nQz0MnfiQhXn3mM-s8SxaE3kRjL3rFqOoEG_ndE8h5lkEebcna0C9NNsZnQlm9OdZo5U8Cthh-1nDAw9T7Uc1cRP_Cx9bHsMSE48JHzmBJwwhA9yxNJ1gm8ggJeZeJ0lKOGtMB069fqPdkW1HYAVfCFCgW7lRZ1kP2ABfF9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DD3Nc51gUKF8N1Y-E-dKNB7kgMS3bUBObCDSkjAWQ6QeJ4I0vFsSGo5hoW1EJDU51F4GiEB8jp1pkUtfI0Z9XwoIC4Yx74eEi81-BEX10BmjSyCfFHJvoo6zlhBxUhVF59SVlabkLvgpTk9Rsk6CL4KG76eGqvkZN8MlHYlnm5qOXOUEieGd5TCFw8drazmqVFNI_yrust8pua9q0tzGKRympo_XzpX-QPLm9O_RDO7yuaLod8kvOCfCw7l4t3R--d9UkPmxrcxwV1YWZ1iPpKV0YrL3eVqjPfYPWigv9GO_jbBL2DbgK0UB5v3JjNj4IGXFYRsPWPygnZ_wE-5zCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iVP9wbfUJvmSHVpYi1bSnIVP5NHYKVgmWWIlcPDJNzUNDlA641jMhhdU_KeeLayqiwwniIfsGCveAqrpvF_zYnIYVtcLczjEauW_ED6laVem8GkaRj0Dl3j2kqTmJkNnn0IaEO3nmO5NlTRIb6k2RZ3jREQAldpwR4vIm5bsodEqwxcuqhOC52ww5TUJ6rNCxy2Hy97va8vrK9_UL92em2JKB-Qqf-LOqRmQTMM02IRemsZzWrKFRyJaw9A8umMntlqddqPFGS3naRDMgOO-Bgym-Eov6pm68J6jdsmyFHIfLcwpIRqjsLUNNie6DlsPtPUZqZwDJsL2gCR3Ol8E4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHsW5leCPznjwHGWTFDXh3-LnH2p54lhc_jPRzuYJZwmjWbT0ObUdqT_x5mcmXxEfAy_OsIcRQfMnQOJAj1h3U7HmUizCqoYoKfYgRsWznhImcmYr62lslAFgZKbLbGydadmFGpk5LBt9ILKOqxZeilSLQusSvbWwYHVdJbUV50TQyWLxH-v8MUazsZ65KVRIyKtp24wPb_sEXwk1mFMccXmwsDZS1AKN2xPSuMXNRkkDZjEWIT0k_bHG6T-ZDsWcCs5uXQoN5kNQo8e3Du09ZUF_7nR9epfxt1xAnCHUet-xh8EX57rJG-jeWktSoTfEQWUInLq-P8j8g5q6ygGrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7841" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7834">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=qisSApRRFX19JsUUnwCu1oDh0WlYkZn7ysgPCK2hRuy1p4sp81tCio74aEza4Tuz5FJ0S9p6w5R-AKOlcNUQdmmCSO8nfxZpwIMcYw7TVo4H0yFPDKUNxymQEhUhPay8kXRvnBFMSX1YsCeAnfN3qhZCex-3x3yqJVXtRrATHPUVkFHjeSI9SRt4hfnD9wuUVU5jTEDI_YdkJXKCUoqiX9EGNttuHDHD-7-4BhmXatK9_RGtOmElSDxPq5wTG4g0By5DSErIy50rB08_B-aaRnzZDj1CDrQMh5iT55XuuhmxB-W4RX9HumyGIv2nbXcNNjabx1x0h7MrSIOGf1ht0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=qisSApRRFX19JsUUnwCu1oDh0WlYkZn7ysgPCK2hRuy1p4sp81tCio74aEza4Tuz5FJ0S9p6w5R-AKOlcNUQdmmCSO8nfxZpwIMcYw7TVo4H0yFPDKUNxymQEhUhPay8kXRvnBFMSX1YsCeAnfN3qhZCex-3x3yqJVXtRrATHPUVkFHjeSI9SRt4hfnD9wuUVU5jTEDI_YdkJXKCUoqiX9EGNttuHDHD-7-4BhmXatK9_RGtOmElSDxPq5wTG4g0By5DSErIy50rB08_B-aaRnzZDj1CDrQMh5iT55XuuhmxB-W4RX9HumyGIv2nbXcNNjabx1x0h7MrSIOGf1ht0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5Dqnh-f8KzrTpkjWb3DIWc7PkLhSFh_8sAQC3EEyfb9cZ7VWzgXpZNDuqhIh2jMMIwBtHfQyL_FR3sA7dtXTFB9AGO2d91uJX_O_d9nBkj86-wlpkIQ56qUXTU28ok-byIj64je7w9a48EcCYV46xw3oC9Pl--dcx7YMTLVGepS0lXJlIngstF_yPHIlFg7DS2Rqe5W_cSO7N8WjEkTCHAKt0SmXJI_IyvPd2WqPiMJcdJ9eRoOIh5vGemmccSSr4QMu3PMG_uqZv8pWBa98J2Oi3fNlwYLUNQBj1QWk7DDxV_AI0aVQHo5uZcWwahMFEQxU1nQoH1SRE-hL0afPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود آپوس 5.5 منتشر شد — شرکت Anthropic، مدل پیشرفته خود را عرضه کرد تا با OpenAI رقابت کند.
بر اساس تست‌های انجام شده، این مدل از Fable 5.1 و GPT-6 بهتر عمل می‌کند. همچنین، 20 درصد ارزان‌تر از نسخه قبلی است.
این مدل رو
اینجا
تست کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7826" target="_blank">📅 20:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7824">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiXcJXv6wVATY8Tz-355hZHDfozPcUjOiOHnkt0RCnPs7ogSlC38fUG2KRiYDW6Rtlwajp7ptdSVIekRlDkh3KFnb6UEVmYtQhQj7Q6JHBgTKJgAbQ-OyqTb1PErRD0xGAWQ5Q9LPezbZk1n4GpuwkNA7eG-_OL370K0qhBLsEbFO9R4GtZ9eSjYIMNcyM_S6pVvL1mhqw1_ErRdbezLIo8ip0znS6moVGqTYto6t8slBfXgRBKzvY4RwpXoR9qUlaI-6c7jUaWtQPxnYRyMoDElydzFqum4dajPS_44VrbQYjxpvFw-b9N_kTxaf0Y5qo72wx3esi6x5oylJwFHeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
10 میلیارد کلید API رایگان MiniMax M3
👾
📌
مدل‌های موجود:
🤔
MiniMax-M3
🤔
MiniMax-M2.7-highspeed
🤔
MiniMax-M2.5 و مدل‌های پایین‌تر
💎
کلید API:
🆓
sk-cp-jqkYZKrokpSo6XdjlPb7cHA2kZfLdhdZwgtX15DsiwBAbFjb221rKvZtuZvPk0xEy7AaEZnD94ugiuDisZ8U1sLs5qfzCAHog6ti5fjjUsqZprpRqiNzdBg
⭐️
Base URL:
https://api.minimax.io/v1
(سازگار با OpenAI)
🍀
✍️
همچنین با موارد زیر کار می‌کند:
👀
🤔
MiniMax-H3 / H3-Max (ویدیو تا کیفیت 2K)
🤔
speech-2.8-hd / speech-2.8-turbo
🤔
image-01 (تولید و ویرایش تصویر)
⚠️
نکات مهم:
🚩
سهمیه هر 5 ساعت یکبار ریست می‌شود.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7824" target="_blank">📅 15:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7823">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiW_51MmWx2X0E9-HLb4TKJXWPEeR2IxHa4ilIkjnjnFgWWV5EuSSBMMVsPr_aj8aI4ZJP4oh8Bd9RdS62BKAs7xwNVBsLVKZeqqZtnX4rP-bCL7DUBxiFKRejIroJsm_Ip1Qo_KpibEsucZDAE_8vevS_2nEUE4B66NTwUolIukElMcDIxmtDe2dzGlJrFYn72VQvYYfVGlukQCq8KEHiIAp9ffBnZjMRCYmRxu6sZHb6oC0SAk8TXYkETFIAZd7_xxgdxa9o0lpvOYuUr5xrSYCxILd__PuzlI2TLP6XZveVg4cqBG-pMSspO-b9e2beJ_5WxzlDThSlbGAhpTgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚙
موتور Agent Executor گوگل برای اجرای انبوه عامل‌های هوشمند
هر عامل مثل یک فرآیند سبک اجرا می‌شود، پس یک مجموعه سرور میلیاردها نشست هم‌زمان را می‌برد.
🔺
خواب و بیداری زیر ۱ ثانیه
: عامل منتظر تأیید انسان، هیچ منبعی مصرف نمی‌کند
🔺
چیدن خودکار محیط
: مخزن کد، سرورهای ابزار MCP و مهارت‌ها را خودش نصب می‌کند
🔺
جعبهٔ ایزوله
: کد ناامن با سقف پردازنده و حافظه و شبکهٔ فهرست‌سفید اجرا می‌شود
🔺
هنوز نسخهٔ آلفا
: روی سرور خودتان با فایل پیکربندی
ax.io/v1alpha1
بالا می‌آید
💡
نکته
: مجوز Apache-2.0 دارد؛ استفادهٔ تجاری مجاز است و اعلان‌ها باید بمانند
📌
سورس و راهنمای شروع در گیت‌هاب
🌐
صفحهٔ رسمی پروژه
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7823" target="_blank">📅 14:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7822">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXjihVs9MHjOeYHAzS0jXQitOHKc1dv0iGWoBT5zPGiDWqOnz4fCi-VeICJC2a2kYPTviEvisYu21wZ3JphrWMUJKj-mw0WXdaMYAlCznmpI2dAR2NpMTckJAnAxEpylePVfTVre0cMJvjfDpUJO2_DFzGQoWrMoQBKoNGn5OkrAPkAIL8oRvz6R2M2taqOoyBR4NAEbGpHmW-qPN-87J40yz2cB3OKdoA7ezjguPZNBZ56iqfEpZkX1MyX2xCZy6TjQx-UM7j44j8KTTYWr72ByMj-7U7clFINYM75YJKJzNx8AnElAGn308SeckdNaJtTSWCIYJRLnuuYoo2AgNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
وضعیت فعلی بازار هوش مصنوعی
💀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7822" target="_blank">📅 12:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7821">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🥹
2 روش برای استفاده رایگان از Grok 4.7
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
1️⃣
Grok Build (رسمی)
نصب Grok Build
ترمینال را باز کنید.
دستور زیر را اجرا کنید:
curl -fsSL x.ai/cli/install.sh | bash
به پوشه پروژه بروید.
دستور grok را تایپ کنید.
وارد شوید و از آن استفاده کنید.
💬
نسخه 4.7 از Grok در Grok Build پشتیبانی می‌شود.
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
2️⃣
XPLabs
به
platform.xplabs.ai
مراجعه کنید.
لیست مدل‌ها را باز کنید.
؛Grok 4.7 Free را پیدا کنید.
آن را انتخاب کنید.
از آن استفاده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7821" target="_blank">📅 11:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7818">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n4DpwQdj6J-KQ1edwt3xOdenuyo3wmP7YKQp_d3zx9GiRt2YXS3OZs6xueaGZu8LAF2ZePjLt4BfBXySYfdXxHEcPzYyoOJZpIvOLlRg1wMOPKC-Sv0jZgr03wTXf6ojxCoD4NgvyrMwOeM3GCwaGCD6FA-vTHUbC0Og94VFUaFePIUuLkmY4aJhlh2s5nXsV1PcyUtVQ2Rbp4bz_ZK-59aVMmFPv8NLb7VdSPY-wVIuE-aEm60mYqjUv2Y5iAQ-e4CkC7wDThGUtq6MKki3umSHJyH5aXN8RMVcTU10X4cMSE9bgO4otYQegxLI6F0F2DleGxc7kztykW6--maTKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_o-ZgvgZOqi4Eq83k9np1diW5TgiX9BgullpOfwwkDtzl0jmnVCazjXc9C5qq73cDVVvChZFhVYKHcWfu9C2j56uTqxnuLET0S33MHgsIM7TtW9n5lxGJSfPQwKpXp0Wl6TuTdG_6PeCm-W3FvNjTt6dDfKYz6YZsHkKelEO_shFLSoOzxBTT6Ir-HB0kS2mzffri-FfIoPXC-ewgfIyRuYuk0qKvSrnU7wKz0ei27WU7_xR8_WGBWy3S1iPx2nVWhpGphisz4HcAUJcNS1AkG4xKu4EwMYnkUldECfrKdgOOdlHvX8YHxDF1i6yt08u96Cqf2p8i7axCUnmI-l5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntE7Ud8g2dO5BTiLU5hq9LZAYF8oyvrVaheAWZJX_bWitEoVcQy2LdqSG9VF6C54TqYthkjEDTvpUicUw6LLX5LOTi158Vq6QVIkPD8c_h2hfqhIb7cG5g7Tr5IosoBC_h0NI_1SSBPdcraDwlKrUqdMwao6v-GMatrFBr7_-T9i9-MUl2nBYz4KEgYVhTQMJ8c_hKIKDoXW9mTqnrIs2jpfVJgfSKmBNRTnQaMcV-Y6tUjGmT1uH30M5WFd901E9ee4FR1f5v6L4WoBJLDJfhlFO1-iZPYMt5mhBjAZYhFDzNnWAMpVN5Zer0KYjkJ7VDvsY5c6_XvTIPFZ9-eQJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😎
دسترسی رایگان به mimo-v2.6-flash-free
🤔
نام مدل: mimo-v2.6-flash-free
🤔
ارائه دهنده: Xiaomi MiMo از طریق OpenCode Zen
🤔
رایگان برای مدت محدود
🤔
صفحه مدل:
https://mimo.xiaomi.com/mimo-v2-6
🤔
OpenCode Zen:
https://opencode.ai/console
🤔
مستندات:
https://opencode.ai/docs/zen
🤔
برای استفاده از OpenCode CLI:
curl -fsSL https://opencode.ai/install | bash
🔥
تنظیم مدل: mimo-v2.6-flash-free
⚡️
میتونید این مدل رو در
MiMo Studio
تست کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7818" target="_blank">📅 10:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7817">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Md4EwTZW5u5TaEgc1U6URNM2F1lFQpuClNjoRBdmeS7mUfS9Hf7WQxQBS4rTKVuZFWqY4DvSMprJzoHMQejwftjN0XH4imH3i78-DnblSVlZSe7Dw1JZGZ9k3svX1XOjf51VpSJiQJRsRiVyKRLIAhMOUmFkFHM5kYgs6VIUmXMfAPaLxX8S4lAsK71ZQU33Fu26zWDJGna6m4g0Oirb8JBTm2lu3FfhWGCjcbixlj5NAFZllA9GuM3cPLo2c2HdDCgmgoQwhExhf-yofqh2mQkN8hOmVCmBi2Kr_vdGaaYRgDetwl2xze7SPHo7AdBNvCdD2t9uNaK-MQX0s1oLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی
یه پرامپت از ساخت بازی مار بازی توی حالت ultra speed mimo 2.6
توی کمتر از یک دقیقه واقعا پشمام
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7817" target="_blank">📅 01:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7816">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQ3UDD1gqOwV5CkMwrV6Hep8Irplda8ywl4An01-f-xQmKX1tvcmo1f8MT5kUxlqED2GpF4Ex2vNgKOi21pmyZFth5tmoL_k3B24CZv0XZo6ijp70RnZMEupFHIUDo_Eksy1epC15FfY6mRvsMxMMzuRcsy-et977ATWZyY1JW-pM827F86P_JokWOJt8Cho2RfWNM3LWbzzIAWeyuYOax0R4834OHBCPgwpcLR9CrRkib8klnYbRH0v77rbCDDvTKuU3QAsEH0Jpm5OWyEmMPXFH32BGgwghsTFXitNV5SUi6jGjOxZCplkz4Fa2ejYXagudT5UdNtifH9HW9Ax4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد   درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در…</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7816" target="_blank">📅 01:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7815">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد
درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در API منتشر کرد. سه نقطه پایانی (endpoint) جدید در کنسول توسعه‌دهندگان ظاهر شدند:
؛ mimo-v2.6-flash، mimo-v2.6-pro و مدل پرچمدار با سرعت بالا mimo-v2.6-pro-ultraspeed.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7815" target="_blank">📅 01:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7814">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=X7iGW46acE2zlfcbX-h98-FkNufOkwC-JhRXXD49X469ixx5eLTN3ZxE46OUs7Mi6QXaPYG3iwy4ddZ4kjnMmR6hCIc1gZjyLx9TNekysKsfJ8ozklicatTvXTP7iVSd08E6a42nDalo0RdLZoceJWeIGE6Q-2zortKIDgAhJDYS1Ye3URRUIF-GAaeevJrhF6DpybBN6I8OYij6WRscVdrX_gB8L3XISBq69L9cljpvIx1oiI6nf7LOEj2UDwr3OKqst1wYdpyV-RP5A56ky4AW9Bf9v1MIJeXdxIY--lhlAj29pR_YL93l4S9vLu-QkPcNIRQrRrJA_aShDaHWfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=X7iGW46acE2zlfcbX-h98-FkNufOkwC-JhRXXD49X469ixx5eLTN3ZxE46OUs7Mi6QXaPYG3iwy4ddZ4kjnMmR6hCIc1gZjyLx9TNekysKsfJ8ozklicatTvXTP7iVSd08E6a42nDalo0RdLZoceJWeIGE6Q-2zortKIDgAhJDYS1Ye3URRUIF-GAaeevJrhF6DpybBN6I8OYij6WRscVdrX_gB8L3XISBq69L9cljpvIx1oiI6nf7LOEj2UDwr3OKqst1wYdpyV-RP5A56ky4AW9Bf9v1MIJeXdxIY--lhlAj29pR_YL93l4S9vLu-QkPcNIRQrRrJA_aShDaHWfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل در حال ترین کردن
Gemini 4 pro
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7814" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7813">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">😎
از 265,000 اعتبار رایگان برای استفاده از مدل‌های برتر مانند GPT 6 ASTRA، CLAUDE FABLE 5.1، GLM 5.3، و غیره بهره‌مند شوید.  یک حساب کاربری جدید ایجاد کنید و فوراً 250,000 اعتبار دریافت کنید. با ورود روزانه 15,000 اعتبار دیگر کسب کنید و با انجام وظایف، اعتبار…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7813" target="_blank">📅 22:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7811">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⚡️
یک خبر خوب برای طرفداران VS Code و GitHub Copilot!
اکستنشن
🔀
Router Models منتشر شد!
با این اکستنشن می‌تونید مدل‌های مختلف AI و Providerهای
OpenAI-compatible
رو مستقیماً داخل
Copilot Chat
استفاده کنید؛ از OpenRouter و Ollama گرفته تا APIهای شخصی و مدل‌های Local.
🤯
🔥
قابلیت‌هایی مثل:
🤔
مدیریت چند API Key و Failover
🤔
تشخیص و فیلتر مدل‌های رایگان
🤔
پشتیبانی از VS Code Settings Sync
🤔
؛Import تنظیمات 9router / OmniRouter
🤔
ذخیره امن API Keyها در Secure Storage
با دادن
🌟
دلگرمی بدید.
🔗
GitHub:
https://github.com/web-elite/router-models
✈️
@ArchiveTell
|
#SHOWCASE</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7811" target="_blank">📅 22:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7810">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wbj5P5kdr6YT73mYSIY5mLWQqoKP2QKjpU14YlMfCPt2WKBYFq-LNIikZKnLmBUkfNYQIb2MB0G_YzgVyyt_k3D0YJNax3-MAU3L7IHBIqhiTypHdaV8jsbKXQhMVANMroN0nEkFDyTkCEGIbGdoV7BelTqSOkgOtURPjql-gdRErgEAy_XfbljTg2Th4_auquP1oMJMVjWgmc6O84IZ5rUkJv_ewQN-6JM3c-7vLp3vQGx7-A-oOI9hKqtqI3goa1B_GUJ1FRoZDzvncW5JxX5wmx7KzZ6OUxRtrDLMDXnndYoxoqLnJ96SePnNR1TWDyuZZb1muIOfbRfMUrM-Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥹
نسخه 4.7 از Grok منتشر شد — قدرتمندترین نسخه Grok
🤔
پیشرفت چشمگیری نسبت به نسخه 4.6 در تمام جنبه‌ها
🤔
عملکرد عالی در حفظ متن‌های طولانی، کار با کد و اسناد
🤔
مهم‌ترین نکته: قیمت بسیار مناسب — قیمت همان نسخه 4.6 است.
🤔
با توجه به پیشرفت‌های چشمگیر، نسخه 4.8 از Grok به زودی منتشر خواهد شد.
🤔
برای
تست
اینجا کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7810" target="_blank">📅 20:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7809">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnvTQxkwpA8dWjoGF6NWUEwp4HOnJxyO6Guj1cb81Y3KLEYOn1_mtw-qGCkhIQZ0Bt1yHzKwmzhZq--uUBm2T2HFQuXkhs0I23HzPZTkAK9-E3odArBFa7kXRjhZgV-sXU9vj4_t_P10ag_oC0hzuXnoiqJZZ2xVZzB_T-QfMZskUwUDXWsT7ZSm9W3F_1CUXRYYVUifn2w92wW6HUwwc2dCT-on2kieNnc-Q1bTSccxZV-mktpXvy6vjFjscORAvaT2lVkqsLbdICQWZpC3m3IoyXE8dCOgMXw0LhpkBkibwzqbGS1Zq99m2y_EnBar2TAR95TgKhSPbcH-ZB58jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
500 میلیون توکن GLM 5.3 Flash
؛AutoClaw دوباره توکن توزیع می‌کند، این بار به طور همزمان 500 میلیون توکن در دو روز
21 سپتامبر: 200 میلیون
22 سپتامبر: 300 میلیون دیگر
درون آن، GLM 5.3 Flash، Deepseek V4.1-Flash و V4-Pro وجود دارد.
🤔
دانلود
AutoClaw
و ورود به سیستم را انجام دهید.
🤔
بخش Credits را باز کنید و روی Redeem کلیک کنید.
🤔
روی Claim کلیک کنید.
⌨️
انجام شد! حالا ما نیم میلیارد توکن داریم! مهم این است که آن‌ها را در طول روز خرج کنید، زیرا در پایان کمپین (23 سپتامبر) از بین می‌روند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7809" target="_blank">📅 19:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7808">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hi7XgYS2zhtI17PUxVjM9NqBT7o-axKdW7Ea7GjPOs81-I0pLCcK-E2xHfYX2ulChQH2fMFAN6DQ6PVa8tjlBsy0ARwbQXfq0Osma49BdLka53iN-yaG78Q4vHL7BuTZMes9ikyraW1rh61juoiI39XO4wTU8eh_rdIxowat9xLLJyOHc7pK7zAntq7xEuZAeWr3YmC2_3SZ9FlyvSNVA2ZD-Zc0n-nMP3KD4yMIm4TE6_AH81bmL7EtxYg6FPNTzHiLslJ9Mzft0ZqVvWMIEuu8sVZDtIn-caBojdBVOl4CdmSoqe5iUsLEJ55Eq1MO7Lc_3ZHMqk9hHJWDQ_XiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
مرورگر Sigma؛ ایجنت هوش مصنوعی داخل خود مرورگر
مرورگر Sigma روی Chromium ساخته شده و ایجنتی داره که به‌جای شما توی صفحه کلیک می‌کنه، فرم پر می‌کنه و کار رو تا آخر می‌بره. هدف رو توصیف می‌کنی، خودش مرحله‌ها رو جلو می‌بره.
🔒
مدل محلی Eclipse داخل مرورگر اجرا می‌شه؛ طبق ادعای سایت، پرامپت‌ها روی همون دستگاه پردازش می‌شن و آفلاین هم کار می‌کنه
🧪
حالت Deep Research برای جمع‌کردن منابع و خروجی ساختاریافته، به‌علاوهٔ چت با هر صفحه و ترجمهٔ سریع متن انتخابی
🗂
ادبلاک داخلی، تشخیص فیشینگ، رمزنگاری سرتاسری و پشتیبانی از افزونه‌های معمول
⚡
در بنچمارک Speedometer 3.0 روی مک‌بوک پرو M4، سازنده مدعیه ۱٫۱۳ برابر سریع‌تر از کروم و ۱٫۳۰ برابر سریع‌تر از سافاری بوده
💡
نکته:
نسخهٔ فعلی برای مک و ویندوز (149.0.7827.117) و همچنین iOS و اندروید موجوده؛ نسخهٔ لینوکس هنوز منتشر نشده. بنچمارک‌ها هم تست خود شرکته، نه مستقل.
📌
دانلود
🌐
سایت رسمی
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7808" target="_blank">📅 18:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7807">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcYhnYLRo9dDYM2x1n_dAIfIgwemEEUMKvsqkPUFixU1-RewX1bf0qJcH7JfhCqWbrVwC0CpTlFh6PfvPGkvi9tBACNgZ_D6LBzidNu04y5MrWQmAdalrjs2XWmhWRnFuDC0mUIMYq8nf0AG9C5xLMS9qcdrvp2Hs7NGHPTUGF3QLWAxKaw0z8vALIZUL2tIkbIhmKDXLTtt8vRse-8EzIpsUdcoL02oS-zwc09ohSeY29AyKE91Xby1XO8mcY3D8id4ICWLGKmiE0nRNV4yxS3HDFhTAnt_hdNf8AW5_uk200BsfKihA3aMkhTBIWQQUqKYf4l8xDbC1EDjc7O__Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Jev رو رایگان کردن
🤣
console.typesafe.ai
120 میلیون توکن رایگان میده تا هس برین بگیرین، درباره کاربردش بعدا صحبت میکنیم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7807" target="_blank">📅 13:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7806">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddcRtD8eg43E1zLQbjvqjkfz44d_BscB6gr0ptoAhd8BOK3ebiCmbyyZ4CZmOPCh_axTuVb_Mez8Pp5pdumrSEpckMk_GoUMfjPeDMsJmcTjWVu-S1Teqj8N9Da7s8obwJJ920Wa8vGxymtfNeGlZr5X_jR_F9kOhQ4hFkndIcn-9ODihL7aVqP5cHWTn3S7nEk-fZgVDzqn_S0blTurSlgkGxG4i0CInngUZRhHv3dOpaCe-P5EtZy3R-u6g3AGy-9XZLB68qvWXAbKxpm7BNWqemeqxuaDqjKEUIypN1P_HWFDxjajozo4i16k1znLxnOCuGv4HjOSixXj9IrbDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود iso ویندوز و آفیس + فعالسازی رسمی رایگان!
همش در وبسایت زیر:
✅
https://massgrave.dev/
سایت قدیمی و معروفیه، سافت ۹۸ و اینا همشون از اینجا اسکی میرن
😱
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7806" target="_blank">📅 00:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7805">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwlP4u9g2FtC0aTSPTJ7aB80AzleJx0PsKDTu3RcGv5n6bm314sF5q7RHcdBrM2-qjpoJD_y_k0MaIiFPFcaic0Vd_C0qn6ZUirb0ElDXCRWprUm86oyROw15pUCVhhlfSmvOpNgwEOrxTkcQ046awROy8qRVC3ZMLMkT5bNWFpuSoiepTrMvWRDslJmp_RordLU8QFjyd4xeBAB43rX6cweL5Wpwl5DMv7vtt1wg3Y4inizpH5Tuz7DwJBBVcNTe_BmG6fpYfqh_VfDzjDgskZqYAwoPE_BTmj3nos2N5UVK-0oWHMpI5F56o5tXGLMUuEcQ9BCtcK3qvPJ01DKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Cloudflare Quick Tunnel
☁️
یک قابلیت کاربردی از
Cloudflare
برای ایجاد یک تونل موقت بین سرویس لوکال و اینترنت، بدون نیاز به باز کردن پورت یا تنظیم
DNS
✅
با استفاده از
cloudflared
می‌تونی سرویس لوکالت رو با یک آدرس
trycloudflare
در اینترنت در دسترس قرار بدی
🌐
🔺
بدون نیاز به دامنه
🔺
بدون Port Forwarding
🔺
مناسب برای تست API، Webhook و سرویس‌های لوکال
🔺
راه‌اندازی سریع و ساده
📌
این قابلیت بیشتر برای تست و توسعه طراحی شده و برای سرویس‌های دائمی مناسب نیست
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7805" target="_blank">📅 21:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7803">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZlDU1UdcWH7sRObhipzF7NM_c4wBdACRnErKpPFneqZeXvdS9FQUhq-hLVmRoedvPuW58O6aqx6wYjPp_1F4VGNC73DFJtHQUS96_N4f5sj4zCL8aCQxRpVb8GUakdTZEJfo7E02je2jqVTC1thm-UmaTRIG-BY3GYUXuwlm02dQiZh_RGjMFowGNJl8br9YuM5Am1oIQu3VH-hFssJ0XrljQSSbeq9wJoasUJeren7aMWf0kWsGe7F7A1yK9WecMTsInqrS1fp7egqkV17TMAVseM9Id7rIOrLd3G7hXcR1ijIHUkZY3OSHvVjcvjRr-8dF5j4gIrzy3YJCq03BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پکیج طلایی API هوش مصنوعی | قسمت اول
🤖
سایت‌هایی که برای ثبت‌نام اعتبار هدیه می‌دن!
بچه‌ها یه لیست پر و پیمون از سرویس‌های ارائه‌دهنده API آماده کردم که بهتون اعتبار تستی می‌دن؛ خوراک استفاده توی کلاینت‌های مختلف برای دسترسی بی‌دردسر به مدل‌های پولی!
🔥
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
1️⃣
سایت Modeloc
👑
└ خفن‌ترین گزینه لیست؛ همون اول
۱۰ دلار
اعتبار تستی می‌ده!
2️⃣
سایت AAAwinn
└
۱ دلار
اعتبار هدیه ثبت‌نام
🤒
اکانت گیت‌هابتون باید بالای ۹۰ روز عمر داشته باشه.
3️⃣
سایت Jucodex
└
۱ دلار
اعتبار هدیه ثبت‌نام
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
👀
قسمت دوم به‌زودی...
سایت‌هایی که مدل‌های
کاملاً رایگان
دارن و
هر روز
بهتون اعتبار می‌دن
🔜
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7803" target="_blank">📅 13:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7802">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔥
دانلود فایل های پولی، کاملا رایگان
- بخش دوم
خوب سری قبل گفتم تورنت چطوری کنیم لینکاشم گذاشتم، حالا یکی میگه من حال نمیکنم تورنت کنم چی کنم؟
یه سایتایی هستن که سرور های قوی دارن مخصوص تورنت، شما لینک تورنت رو میدی به اونا، اونا خودشون  فایل رو دان میکنن، بهت لینک مستقیم میدن!! و شما به راحتی با لینک مستقیم دانلود میکنین!
سایت سیدر یکی از از این سایت هاس برید توش ثبت نام کنین:
✅
www.seedr.cc
✅
با این لینک برید ۲.۵ گیگ بهتون فضا میده، ولی برین تو بخش Get space میتونین تا ۷ گیگ افزایشش بدین با انجام کار هایی که میگه
🏃‍♂️
خب حالا من لینک تورنت رو پیست میکنم تو این وبسایت و فایل ها رو بم نمایش میده، روش میزنم copy link و لینکش رو کپی میکنم، و میام تو تلگرام وارد هر ربات url to file بشین جوابه مثل ربات زیر:
@uploadbot
لینک رو بش میدم! و به همین راحتی فایل تورنت اومد تلگرام.
برای تست فیلم سریع و خشن رو از تورنت میارم تل که ببینین تو کامنتا شمام تورنتاتونو بفرستین
❤️
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7802" target="_blank">📅 10:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7801">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7PXNDG-34NiGxrIdSzxsD8Pkp_KgDws2BmE35wznkEw2HKZZNHviTzo7tEKQgFycxEbmURdoKyAMtAwc9o8W0Xj6IEvKvdclJVt49tjl0p1i_vvDUtwdn6Q2uHbF0drWkdOUyRZnKZ2-K5vndNu8K1yaEm_8tRHAIY_9dhslMaqMoOeWW8LF1U8J_5dwWQmE0eYEu0DSQtJMwHWA7csiLPE9SNGCcB7HygrIxoLdCha4x8PttXywP_IqYP2biMOJSZU_XRn63hUr52k76oWhKTY6SJhl-D7m8sM-ldHwPPTxOvt9uv_FQIQ4VDo1dBnQnJUhA328WKLBc45DEleWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
دانلود هر فایل پولی، کاملاً رایگان!
🔥
اصلن به این فک کردین چنلا و سایتای ایرانی(فیلیمو، فارسروید، سافت ۹۸و ...) اینهمه فیلم خارجی و برنامه های کرک شده و کتاب و اینها رو از کجا پیدا میکنن؟
بعله منبع ۹۰ درصد این فایل ها چیزی هس که قراره بگم و کاملا رایگانه!
از جدیدترین فیلم‌های روی پرده با کیفیت اصلی و دوره‌های آموزشی چند صد دلاری کورسرا گرفته، تا برنامه‌های کرک‌شده ویندوز، اندروید و هر محتوای پریمیوم، نایاب و بدون سانسوری که فکرش رو بکنی
🔞
💎
( آره حتی اونام اینجا کاملش هس
🤣
🙈
)
اصلاً داستان از چه قراره؟
اینترنت یه شبکه بی‌نظیر داره به اسم
تورنت (Torrent)
. اینجا خبری از سرورهای مرکزی و محدودیت نیست! همه کاربران دنیا سیستم‌هاشون رو به هم وصل کردن. وقتی تو فایلی رو دانلود می‌کنی، در واقع داری تکه‌های اون رو از هزاران سیستم دیگه در سراسر جهان می‌گیری و همزمان بخش‌های دانلود شده رو به بقیه هم میدی. نتیجه؟ سرعت بالا، بدون قطعی و کاملاً آزاد و غیر قابل فیلتر شدن
🌎
🔗
🛠
قدم اول:
نصب کلاینت
برای وصل شدن به این شبکه، به یک برنامه نیاز داری که کار جمع کردن فایل‌ها رو برات انجام بده. کار باهاش به شدت سادس؛ لینک رو بهش میدی، خودش بقیه کارها رو میکنه.
📱
دانلود نسخه اندروید
💻
دانلود نسخه ویندوز
🌐
قدم دوم: لینکای دانلودش کجاس؟
لینکا اینجاس
🤣
آقا یکی میگف من با تورنت حال نمیکنم. میشه مستقیم تو تلگرام دانلودش کرد؟ بعله اینم تو پست بعدی میگم. نحوه انتقال فایل تورنت به تلگرام
😜
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7801" target="_blank">📅 01:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7800">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🤖
JIJI AI
مدل‌های موجود:
⚡️
GPT-6-astra
⚡️
GPT-5.6-sol
🧠
Claude Fable 5
✨
gemini-3.8-flash
🚀
glm-5.3
🔥
deepseek-v4-pro
روش دریافت API :
1️⃣
وارد سایت بشید و با گوگل لاگین کنید
2️⃣
وارد بخش API بشید و کلید جدید بسازید
3️⃣
شناسه (ID) مدل‌ها داخل پنل سایت مشخص شده
Base URL :
برای GPT:
https://api-slb.jiji.cc/v1
برای سایر مدل‌ها:
https://www.jiji.cc
🔗
www.jiji.cc
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7800" target="_blank">📅 23:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7799">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZpnMdzgC82kRupni_LEmK9PwC_DCVh0r3rxpB-CUTMNLw4swb5c0SOGUHVeRah0JR2JeZRKjoHqMrWVm2Ef2xyh2n_v_Hna28q5VVn1gAzARmsMNhyGgCpMtRVv1-Q0J4Yh5rlPnCOtyX2IaCi_Q93l6j1yJH29EFN3Od1QFNxOQM_xoM5vtRF2lBFa2DC4gbHox4RHm2yePjqf04pBkoCy5S8JtUJcaNxHK5b4DcFA4x2Ze9ovkxeAaJ2Pe8tteuHS-nkJzB2fiGgn6AzcvgYLFvKSd_e-EcXuwQ1Hg7W8gJFUiUosH-hheqRRWdWAHz84xexkw8IDSd5k6czshg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7799" target="_blank">📅 23:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7798">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5XUla8CnjW_lNcn-MTa7rwqixANnkSSwCoNKAEUQAu8JRNaZSDmFwSSqxbkHqThI3TMbj9bq4Vx7xgKTPNgw5T4FGO7zCHBUD5B3m4e7cbqkVVfPEROQzRaRx4reYRxAYXusGJ1EMx0Ht_lUJyjt-WatbczMoiiK2Mvfi5FAG3cTYuLPDJTZlCJgSxU_FWpWTyiILLvhDoCN5hyX1q1epJJOTWqTVvyUzPnvaW3QlkLr5d3v4_S5bzOIUNgLjAWkpnU6kMJKaNo1fN1uNfvdKl3eKY6vFvM6OC9muV8unGFvGsRxoN77cfayHCtAl0dQ-hDu2E3VKXi7HMlrJyKQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7798" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7796">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hzi_FiHbBxgG936tmaIqjRhRrBrNhbvbj4LMA5n89A7zxp5SiKwaQrIhjGu_sROHw7pLr2p0x55zC2Nbnpk658eEdxtHSKZ_YvHviAqMRpHI8649FkjCRVM-C0g6NDcAxae-rSuuhPHVSO_9ghi2BxiVPMbyuYXjCyB_J26E2QpbAnfG7b2QLSgfz7AEx6DWE44U76PhfbxJPPxdtsoNN5BeFGLOh5TfAKeOFfo9zjhrD2VFSkDzVJ2lox5SAg2YQmo0NVsTehyxfoYUiKoaTLYnJLJcxnvwz6ci8l0W7zjCkioeIjQdywxk7vAtBkzZfs3IK7WQIaYoHFAuUwu3NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
مدل GPT-6 ASTRA به صورت رایگان در MiniApps در دسترس است!
قدرتمندترین مدل شرکت OpenAI، بدون هیچ هزینه‌ای.
آنچه دریافت خواهید کرد:
✦ مدل GPT-6 Astra به صورت رایگان
✦ قابلیت‌های استدلال، کدنویسی و انجام وظایف پیچیده
✦ اجرا در مرورگر، بدون نیاز به نصب
نحوه شروع:
1. این
لینک
را باز کنید.
2. ثبت‌نام کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7796" target="_blank">📅 17:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7795">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PY_DVFuJXnU-xDnU_fRj4HM7u7Un2e_XZAFNSOWnRU3BqL2_sOYtj332YSv-9h8RMUTNPK_yYgaUu7HKHr2Y9gyfQeBfc_vw0N6jIyWCHtkj8oupDWyE3lKpArTNo_T7vPZxnqdEIePO49epgAPaLf4LZn1SXg4g3en9Em3wlq1RVidYjr4kUVlyl-pwGuvdEoqzV_HI_kj-yWiL239nHY4fx4qxQqDCESxqok2P5koFWifttwU2jXf6sB3fw6GdvpxQaeMGRRivq9fbBLQtW3imB5BbwnNh9atLRwyVeRnRuDxYGNSPERPfZtukFxrOaiEPsFXwpW6fHkQvHoGTHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
مقایسه‌ی تصویری GPT-6 Astra Max در برابر Claude Fable 5.1 Max در تست کدنویسی Code Arena
به طور خلاصه: Astra در انجام وظایف تحلیلی، محصولی و محتوایی عملکرد بهتری دارد. Fable 5.1 در جنبه‌های بصری و تعاملی عملکرد خوبی دارد.
در حال حاضر، GPT-6 Astra Max در مجموع، رتبه اول را دارد. می‌توانید جدول رتبه‌بندی کامل را از طریق
این لینک
مشاهده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7795" target="_blank">📅 16:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7794">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxJy70QKvabajYzj1JkMTeRnymlSqavzNu--E0jyGhP2PYP6Yfo_t3FOlNyaTtXLuwuf2n8btIVlDsXqKwYKyQjJgeqtFwNiWhPLlxoVW9WWKq_IDGpSLs-AaOrFV8G9_ytafhhNHNyZ3iVC9wK30JJC-FlR6b6KlJ-tKcatXBBs-M0LKo5ExJ1FL-7jwiwSG_paFU-fQlSLVVpfYYhEDxWMeC39Z4p4w_MmYLU_uyq-OHKV99EzmuoQ9nKHI19XcOgcOU5A__s_QqfxcnsXeIp4v15AcGck0_Gem2-5M0b8ymiSnRH5iy5uygKSj50k7Ma5Jo2ojU7ft3oCWt18nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
؛Qwen3.8-Flash رایگان تا 30 سپتامبر با 0.0× اعتبار
مراحل:
یک حساب کاربری شخصی در
Qoder
ایجاد کنید یا وارد حساب خود شوید.
یک محصول واجد شرایط از Qoder را باز کنید و Qwen3.8-Flash را به عنوان مدل انتخاب کنید. برای اطلاع از قوانین این طرح، به
صفحه رسمی تبلیغاتی
مراجعه کنید.
از Qwen3.8-Flash استفاده کنید. نرخ 0.0× به طور خودکار در طول این طرح اعمال می‌شود، بنابراین استفاده از آن هیچ اعتباری مصرف نمی‌کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7794" target="_blank">📅 15:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7793">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCeHGkCmrSTKR8CWlYX99YC7Uf-JrWhjOAbVgaHy_6JMvW5m8vnSt2mQJCfdXY4lS0rylnJ1fvU2gK51DiH0sooAHPKVnjvqb7M22j2uIVoK1Fi8SuT2y0tLZPkBugZmssWYze8pdhOS0X31yTllO9t8L898dBa5rpLxdfJ2KvdaqzRbBk7gIeZN6M37AwNOkPsGzGp7x_0sDnG9DWGLzEt_GIKLUyg38702LvsEc16EOVpsooAtlRaicuazcLP8oK4BxhqoJ0EWeYhUQbUg3f5bkuWCcojDOyIbNNHAOgRfx_JoB-A4wSO6CDl_5MkdKI6PWh2qHOEjopp8azAouA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
چت + تولید تصاویر و ویدیو با Kleo
🔥
آموزش
مدل‌ها:
➡️
GPT-6-Astra
➡️
GPT-Image-2.5
➡️
Kling 3.0 Pro
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7793" target="_blank">📅 15:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7792">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6341cb8e8e.mp4?token=uPvVSt01gqdVhm18aM_AuZRuoKKUwHpEJ1EjcNC_dDlBNzGUdmtV2-Mq1KsqosMMqWZn1c2zZ4XWVgJPZLOoI9hLPlE2kpsAxKWVcbAEMlw3CAkfjGXDD1hkFdT49nYk9rMCO3o9CQIw5djroW9DbNMebsknOTcnsu8pSn4DvaRNpSDVGwJrv_2O-ZwJUxLDSd40wMCpSr45_YJmYZJCuSoumuYrNNY8_kMSG1HqIwV-iRdttXzF2MXz6Y7G-GicH2Ls4mnhHBZBG4aUvBFiNlLHiG2dNA749t4JwiafWhgxyS4HwRH1aZKEayDNXCAmXoUP1IEP0d1dvfZ6KNvb_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6341cb8e8e.mp4?token=uPvVSt01gqdVhm18aM_AuZRuoKKUwHpEJ1EjcNC_dDlBNzGUdmtV2-Mq1KsqosMMqWZn1c2zZ4XWVgJPZLOoI9hLPlE2kpsAxKWVcbAEMlw3CAkfjGXDD1hkFdT49nYk9rMCO3o9CQIw5djroW9DbNMebsknOTcnsu8pSn4DvaRNpSDVGwJrv_2O-ZwJUxLDSd40wMCpSr45_YJmYZJCuSoumuYrNNY8_kMSG1HqIwV-iRdttXzF2MXz6Y7G-GicH2Ls4mnhHBZBG4aUvBFiNlLHiG2dNA749t4JwiafWhgxyS4HwRH1aZKEayDNXCAmXoUP1IEP0d1dvfZ6KNvb_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
مدل Kimi K3 به صورت رایگان در Cline Desktop در دسترس است!
🤔
شرکت Cline به تازگی مدل Kimi K3 را به خط تولید مدل‌های رایگان خود اضافه کرده است.
🤔
دسترسی رایگان برای مدت محدود.
🤔
از مدل Kimi K3 مستقیماً در داخل Cline Desktop استفاده کنید.
🤔
مناسب برای برنامه‌نویسی و گردش کار هوش مصنوعی.
✨
؛Cline Desktop همچنین از سایر مدل‌های رایگان نیز پشتیبانی می‌کند.
⌨️
برای شروع
اینجا
کلیک کنید
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7792" target="_blank">📅 13:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7789">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/SodrOBs-sEiVFGQ0I9xuF6PqQbdUz2GVRYXfJbs4AwR3A949w953BbcdoYWg0Va5lRKeT8tUP7lRTvrNqoJdVQePlsDEkD5mUtNVzDG3gH-I8VacanPS8Q-3E9HD5w4pmda1ZT5uUiaNAwZjoJOQzvE5sL8r0OPmD-QALxTpAmRU1U9Y_uhnajNFeEErrV1lvjkh1I4HxobW4ikPHaw6nslR0Q5TZecXLD4hhMd3m64GRPjYn796cOgol33wFUWmQOsYf9t-GStawfe-ySFMUNDthamPtgWZLclcer7oNA393UD03J-jCcaRDm2KulpQUkNEQE9HxmwXRwVU1ODhZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dIhgZetIsv8fRHszrJmoNTL8EYBVNwAGlnePkm4hEVGFhkLDN3u045OlQLC9yGOXwtdSOn3T-PtpHqIpbeNrTg5qubM6mxPlAOQkR9NtmxmiNOEu7CKLUgAtkIa1YflETz-vTlRciGbpRio40Fu9In8Y3D_4AEo7VoqCTbg9CpyUPhum_upQqHRapj0i8eOTxW73hnFHgW6Mz6s6m5qNALWIk7EvBS6lbM5D-e1QIxNoAFB3F1t32Vq19zQjjgVYI2m8lxZaMc3LSSqWs3euDASCg8zix2LPWbSJS6Aex81HUjPQcOhf_maODs7-fUkg00KspZWToV-IH7bbKIZaMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">seekAI
$2,000 credits
API key:
sk-Ok0xV7Zp4vfigk6qXL8M6hQSeVGa5cRhhfkZ06yre2RUIAfN
base url:
https://seekai.cc/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7789" target="_blank">📅 12:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7788">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aprecSqwNs-EdAOfJ_jaoxHM984wfFQPa7G1WbfOwyNVZbafGduNOtRf8W3wwyZs5utmzH04DTQGMUEcSVn4UJIH3yM7WMgB4LqbLtXFIzCQrPtgFjSJUA3WntT8BJfEobIHcHJO_pIjkz8nqvh26xFapAOCKkRaD3q8UNi-3H1SrjGYPDfhHm89DZAwqTAsgnsVaKvXbugaxdzvQzqUkStP9Oa9IX_gHBxK592_Bv2L3IrMYkEJZvW_pnZ6l-41uAJX5ZljE5eBEIuAbkhbP9iHyyU9hXadp3Vjw8KSOoaMzUpEzWLTn2-BXLDFW6nKij2pTvcp2dNZIz2iMYzrhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Fable 5.1 به صورت رایگان در Freebuff CLI در حال حاضر در دسترس است.
👾
📢
؛Freebuff یک ابزار کدنویسی کاملاً رایگان است که در ترمینال شما اجرا می‌شود (مانند Claude Code / Cursor، اما با قیمت 0 دلار)
🆓
✍️
مدل‌های رایگان دیگر موجود:
🔍
🤔
GLM 5.3 Flash (پیش‌فرض، بدون محدودیت)
🤔
DeepSeek V4.1 Flash
🤔
MiMo 2.5
🤔
GPT-5.6 Luna
🤔
Solar Pro 4 (به مدت محدود)
🤔
Muse Spark 1.2
📌
نحوه شروع:
🤔
ترمینال خود را باز کنید.
🤔
؛Freebuff را نصب کنید:
npm i -g freebuff
🤔
به پوشه پروژه خود بروید:
cd your-project
🤔
دستور زیر را اجرا کنید:
freebuff
🤔
از لیست مدل‌ها، Claude Fable 5.1 را انتخاب کنید.
⚠️
نسخه آزمایشی محدود — فقط 500 جلسه در مجموع (1 جلسه برای هر کاربر)
🚀
از این فرصت استفاده کنید تا زمانی که باقی است!
⭐️
🔗
اطلاعات بیشتر
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7788" target="_blank">📅 11:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7787">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اگه موقع ورود به gemini یا سایر سایت های تحریم به ارور ۴۰۳ برخورد میکنید، میتونید از dns های زیر برای دور زدن تحریم استفاده کنید
👇
dns 1
111.88.96.50
dns2
111.88.96.51
dns1
45.155.204.190
dns2
37.230.192.51
dns1
83.220.169.155</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7787" target="_blank">📅 11:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7786">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♊️
جمینای گوگل سه شرکت واقعی را هک کرد !!!
جمینای در جریان تست امنیتی ماه مه ۲۰۲۶ به‌ صورت ناخواسته به اینترنت دسترسی پیدا می‌کند و شرکت خیالی مورد نظر خود را با شرکت‌های واقعی هم‌ نام اشتباه گرفته و با استفاده از اطلاعات ورود لو‌ رفته در سراسر اینترنت وارد سیستم‌ آن‌ها شده و نفوذ می‌کند،  پس از پی بردن به واقعی بودن شرکت‌ها، خود به خود عملیات نفوذ را متوقف می‌کند.
گوگل اعلام کرده هیچ آسیبی به این شرکت‌ها وارد نشده است
✅
منبع
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7786" target="_blank">📅 09:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7785">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سلام بِرارون و خوارون عزیز
حال دلتون خووِه؟
🌟
فردا یه آموزش خفن داریم که حسابی به کارتون میاد!
🚀
مو فردا مِخام یَگ آموزش مَشتی راجب «تورنت» براتون بزارم که کِف کِنِن ینی قشنگ بِتُم مِگُم چطوری انواع و اقسام فایل‌هارِ، هم اوریجینال و هم مُفتِ مُجانی گیر بیارِن و حالِشِ ببرِن.
😎
🔥
بِراگَم، گیانِ دل! از بهترین کیفیت فیلم‌های خارجی بگیر تا همون فیلمای پرده‌ای که تازه لو رفته... اصلاً هرچی برنامه کرکی، موزیک، فیلم و کتاب نیاز داری رو یادت میدم چطوری سه‌سوته رو هوا بزنی!
🎬
🎵
📚
پس فردا حواستون به کانال باشه یاشاسین بچه‌های گل خودمون قشنگ هر فایلی که ایستیسَن رو بدون یه قرون پول دادن یادتون میدم دانلود کنین. منتظر باشین که قراره بدجوری بترکونیم، ساغ‌اولون!
💣</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7785" target="_blank">📅 23:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7784">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚀
Ashna AI
قابلیت چت مستقیم و یا کلید API
🤖
مدل‌های موجود:
⚡️
gpt-6-astra
🧠
fable-5.1
✨
مدل‌های متنوع دیگه
روش فعال‌سازی:
1️⃣
وارد سایت بشید و ثبت‌نام کنید
2️⃣
اطلاعات حساب رو تکمیل کنید
3️⃣
از بخش Integrate وارد API Keys بشید
4️⃣
روی Create key بزنید
5️⃣
گزینه Dynamic model routing رو روی Off قرار بدید
( نیاز به تایید شماره نیست ولی اگر خواست از این
سایت
دریافت کنید )
base url :
https://api.ashna.ai/v1/api
🔗
app.ashna.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7784" target="_blank">📅 23:18 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
