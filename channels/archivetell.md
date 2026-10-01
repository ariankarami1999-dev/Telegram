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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 09:45:22</div>
<hr>

<div class="tg-post" id="msg-7940">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5Awo-LbeGECrh22HUKfKx3YwVJ9esMnkAD0l5QSPm3pwBlHs9GNeesMwkjipmChUWubVATIEmkpCMeD7DVmxtaoxJzJI8qDmnZHPcMHXmAS0z3_Sfk15TBVO_sXxhAqpcwlbO8gybkW9q4e6QrwF6wBx940UTLq16sNhfkv2aMm93v_fBAC0TNrq7LMgOjMi9LhfPw9famo1H5j94rChAea-1rysN7L5e9cdhXGqvST5Fe4wk9DuHWMQxKPNUcwMA1IGiLnruW7bgTQszfHE6pXjau3YZaaxHqy7Hn7N-Tl-pLJsgUwfK9sNA4dYTyLc3bAxERKE_ReIxnJYq7djg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
بنچمارک های Gemini 4 Argon تو آرنا
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 906 · <a href="https://t.me/ArchiveTell/7940" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s2hlcrEhqBqdsAV5AyGcNx8BAseq1ubiMvWYBE80pyZGdJk5Ebxe-q9hfn5NRfrJJ14AdSpYxDL-czFptvpAUKxSy8JoeLcH6b01voL-5OO5GkN27NJhRPfYRuY5MP0c30jE_SVpeAMKa-KDxV6PfCtnnP11h_HKJoPN2rAE3Asua6n2GFWtKDED0xzsELGQ2dHIZHayXXaGjc1u_cFj2gWmU__XVM-MsRb_wMJ3_wMZ2cfaQMrCphvuWHeChIILM3u6Tng9shsJ29ClFBGJHdmtZFyPqvCaJoUN3IVn4mm2tA6AO-sLdOZHDJo55b0_bhf67wpNnoekPVDV3TG7Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a8YTFGduc5tR7Ek5MMGGa-JfGtWVi4lbokyerz_9mp2xaJsrG14NOHOM9Fs9D8EogNeqs95-j-jhsdz8xZmJVvpCrjZuSWJDrgsftS65PiZYFMYNmbj-a5zytz5HqGZ1We4OH0oObaLzofCVPUgiwsHI3Crq3edqB4YWHxPoDVDKmTYiNtV02eSORSKfwQY5ayeAKLM0Sro4uXU5ieYnG-vmxpIcdiG77suQh3LRp5ZdIeCs1FhJdTeej3we-3H1jOlraijGcqxp9mpneB2qV0QTaZi9Rmk41v86vvBMJoko0cf0rHnH075CKfMSM0nIPxetZQu1Dh3073DttwKAaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/ArchiveTell/7938" target="_blank">📅 00:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7937">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚀
بنچمارک</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/ArchiveTell/7937" target="_blank">📅 00:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brSy9xsrRDgqV5g6hlneHtWPO7lGSNCHvkuHJMbBBJKkh5AFm6GGtNklfVjg8Bh0sFm9UEm8JFywjC1_AYBdg89xleW3jzbsFKUdRK_24TfWMFNlyLBtDcNeARQSsPB7K9VUc_5furum6kRnZEmNuI4o-iRv_Iq98imGNbJ9lzHKaeqsVDINaTZRksUqD7_iOwti6DhfJEpLKL9FmIVtMW6qMAp8HEUnsrNeYUxpOPyYSzVagpB4Cfd2n6tS_Sn4XWQTF8y5C0viVPGYBl-WR0TBiWVPRkwqM7omU9m3V7L5Au8JFp2nsFRwYca_Ycs8CLUw8T0fQQFA9eMxh23N2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/ArchiveTell/7936" target="_blank">📅 23:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUMaQipE0KrjJ6KEPhMnfY_QXxcYnHrts42NXKmtoWv7Faa7nPhmYBX6QBtTvKQseWrF-RotcFng1rEHH5Ps5WfTzUQc46EUsI5s0gRGdYQe-qxd7NlbivMlSMZmCFyzoCcd_kPdIyO6sPRYXeoPREpGl2PqLReZGE7vSp7gKjMKKc1D7RcvrTh357zHqtXiKgVs8o5mxUhFX16E449dMMTFyQTcg5STQ8FISwbF9l9bQeq0yple-7STXaHPt9FFtOfhm-1eCNHRgQTY93x-bDG_eO9t281SZbUoFUFZzrZ6rd29Y71-t7c-7vqgnbHQV3jHRf8Iv5-C5F6QrinNTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل Gemini 4 Argon عرضه شده است، منتظر پست بعدی باشید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/ArchiveTell/7935" target="_blank">📅 23:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I38Evbc-loTYSSl82oyb4jl4F2xy-I5J5WxgETXm4izp0ByQO7VB6rmJ4khUGWc8nh3r7Ll6mjRh5Pcjh-1uDLCK6XL0KRCWna2XGMzZyFOkKKfMt3eTpa6JVI1D7oYJLX91FHmtx9OXn4-y--XaU8pjUq0iCspOwnAfLYhy1hVBKoVqLAZoxnGXi6sjzul67vNnCky6jEn-tHh53c_-YXSl43k06PyIRoqVn_-aKTQF6b6rjsti3UyQ5_G2eTAjMWPNXQ-8bEFgl0gVYWfBTas6zwEMhB8s3YmU9ZbIw_u3hcMc6KQ8FMy5op5hkD8KMUuDxxg9G6A_QNYHD2LjyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6dvejKpLqwbZN_sNHt2IJb_H2_Sc94vVQRT4ktfsPmNMjIyc67Oa7L9QML6xJvUYdmjVx6DnRJDi-w8iPqrpA-krA8pEW6jSfHNprZZeKtI86t0Kfv2OOrEJD2RI1uRO0QD40hHoyCoPTlE758HhxMtK5DXZY4uiSHTPq7rlwWRJ8sGLdm69UKA7YoYP1910QXKqCCOtJCjnAVbFD-di3zQySRg6hPP59_lqMnPMxkL3Zgiqe6WXKK2VfDAZfSmpB-3e9fcQ3LSUs2ZkMwvSHuL7WWBFlX9HMXoqqbwDuPj5L2x33xkMQlvXONUET_jNwDXirybiTvbIyiI0YmfKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JJfFbGW9rwaIo2IqU1jQXgcx5UFoKUZMk6yvsTM1MRDVPIgATpk68VtoIWKBlIF8QyHcCFw2QBNKMY7ZSo24C3qbuLvWu6R4mJlrBIUeZXiyb6aIqyVDoFRw38e2Dwr62Ke_0zljVaDQDc3-oJxCvUdAy78h_QAdYYRgcFmWiRyeLuWMmvuszrbYrbD0XSNIph9-RjjNC_GGs0jZ0iiYB_w8zEV-ckhGvkYZNEGezc1dp5miRHdCEwvPpTguL0nN2NSsHsgEdO3F6krg_NRAypgvIFX_gPxf-H4ZZgPV4ReCvuTUqMeRb7RNs-JASSI3vC_q1EqAvLLz28LBL3-aPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dOIuJVTBtdZ6saPjqOtOu_C6QVzEtTgXQicW3DFHaLCbzqCDuEUJR-WXrsJ-PQWwtwBzAGDd09T01hO5v5wCITCynNZlOFItA77wTShiGoR3QiBeThM6ZL0WUiXGJclsoJJdlR6N4xEXJsK_mCzqCOwCzs5FwRqxy4LBx72Cn6VcukQ-EU-LWt51lb5DBG102yqahl7-TYoqEcQSe0BkN1QaAWexBJDUSmSdN8II4P6Rw7vhjnJG9XqxnEnthebvSdyMsK098j7EoZGnYk64M1wRIfj90cXkHWEydcCksglBWghcghD7POMZxgUoVFtIYy9xn_4BmqbJfVVOVRev_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A-73q6Ho49hTCM-6DwXqcC9HyGvx7nI49QIftcLzFLXXKyE7TR8az8S0ceEbJXXwxlrS3jYwXZA_O3LpOZIiwOo1AVRdRlC3lgNUL17AYPkeUW6_5HEuePWAlmuzzPnO74TPLpLy_5I3e4yte2RTlb5rQ6jftPxhT1jhFvOxRwyqHLTrJR3yQFJyKMC4HDP1Na_npriOTH3SBmG-OMsYEtUAf4UuJH1IW3KiLm353EmBPOsyMRT68ct1RUB-wwUv6Jg0mBF383kt0B1GMcbtQV0-yHo986Y6YyyZHka41Wb_EhspIvUV18E415xwDPu2wqY_akV3oARY4j3HnEbFtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ceuVt63-7ejOccjhqZ4eS2GrmG93K6CXn1Zqkali4c1PpGFstSV2K7_yH8EFkxpsXfCXSpleFGtqTjavGIDwAmUEHv85dk8lKN84wkwRI80sqsECVxEUiK8iuOkgrHzIG_4g7x3sXJgchV0rLGTUZPup8xPxIGLmduTluNvW44aeFTsA9TgaZv1ts1JQ3a7U8dCdLAAqPw27g1jDARSWIsOwHhLR0-UPIJ8v9bzVtiRfa6dP0MLRteL0oYCMHCytAG5PVIQgQzUbjx6yaIvWRhSDpFG7EGNCT0j_RRuRD9KIrH2clsHtWLhmBmNanS1Xyk-4Pf5uGbdG679kaP5vHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GyJ3G4KbADc7dhrSFWgjL4p-DsY-uShijpgT8S25aPDDlYeVEvVaz_VPpeofY6rrKrf8ZOq9B5Tc6pYK7HlHJiSGnXNL0GOXcGSybNDyF4BcO3mmVWy8C7Mm-lswsFb-GdhYZoxze2VIf56Pv854jTP8RAOaEmJeYpJzyaAV_TsBda6vnkX_mVjxdiccP-wG_rkIv0TsgR6InCNiAN3ukD6ekyZ-Ne1ND6iMOdgYply6YPKGP2rJP73ePh5Ks69iXuTfiO632QtjEA0T0rMR35g2pPaV0VS9ocVXn3U6MK1GVme6WVCNdxb6T69DiLyxdxvOoGz53Se2vcCSZvHiRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEMqjjj1g4295te0MMVM_PjMZvuSNgw5kiFJ4I3FQzWw-bPqitBNUqRtDiQq70SO1H4t9Zw-hWDn7zII_ZsmeC34vQPzxTN2fYjlZfKeTQk6K1lC-u5me8i1NiD2HCFoF9rMk_Oikx1figJtxJ2dfDWW48HHXRI_Y7AuEX9CxTN1MtyOF0nXeNkVuC1Vec8o99WQ39P4NNEWDQCVkbHtv1aLdkJGzJNW-8R9SGS86ODXskz5mDA5XWaYrZ7iseeJBRb8VggxaO-GLMjD_vtNZBzOgVe6gR68zWCSJyQgHaXJQejz5wQr5yBHgyckg0ejtYC1j32Tc0N8F26SijYScA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJi4cgro3f_mHgb0zNAs4UwVitFuy30WWlCct8MxzYJwKQTfosy1Sbru2IndZjN57UD61WbZsVk9bXmqhRxsGNa08McZuIM-RLhKaiwOd1tspQe0MR0hJ5682WRnzX3Z-Vy0b9qj1eWAnJ2s5k4TN6Jg8UWfC8yGFA6NzkhD5T30BeGPAe09_fGm97GzkjwJLhJ1zqpPa1lroHNdztpXZ7X4HlOdWkh_MlwCUvdf7EAWVdUu-mnJfQWE432F-oPejWALH1Kg1x31t0MP0ckLtVIagDXO1OtThx3vbIdUclDV6wANhf07wiLhuBRwUL65ZaXnVxvTS5_8CAHHhV5i9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0kdlcv-Ut3s4kOoauzQrs2P1R3PBZT1703cSvqWFbZeiOAgqvle5lPIcKHcmZRJVERTEfazikXY-Bh_beowJjhG67IPPqGk6gB86EYaG2JJpMPSUoUz2HlLx8HHbhyaJgIJS52LFbDcMRfqrznElIiO-eYMw_4MRCPTOnapwsS-n1uAO1CqZzz9KX3WgipX-Ke-TTd9Quj_zvPRHLA2j9tEZGdhl8lYXDd4kZ3tsbeXjTVUZdNBnmceeeu3uhxwbqh4bqhdEdgxwf40KtWKE1oHD0GNltTiFJkMVj5JKuXewrQeVzdLNJtqUZTEENTEOU4sR3UNDHLUWu2XCl42IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpEd6ppINjUQg1LuSy87q7ESJGGWyJPaEjk1SPmlQJevRssaDqSap1l797vfanrtVzOEl0wA3IijeY67lUVclN5XOkCcxh3WNBTA359MWwBUfO0Alot25SSHtRfcsrLoYY_nVVEzHkP41giRJVY3A1d4WzP-mr9jt_j5XJc2bvCJ1YC11t_wUWItSdR97Rxv0c9Q7Hgo0sjfLt3Lp-4VqoNC7ZkYCQb4ToURMRjnRUvGnESPGRzHKQQh2zajmnnikKAi3QJamudSuIGntPYwXhJND-R0G4GoZBKifSTKFbr87bVFxndJAp8_6Gi9Fb9BV-xS5ccgRgEv55S7_DaUbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfiMpnWfcT6OZj7QOkCUgENBsnJFQNK0UPhHwYG70HoOqlgWlBVnG17PVTsZwwf3eNLv0RaHU4-ZqXi09uBKQLtrwv7bVE3ZCqrrHzMwZ0nRWhI2FYgOd1kRBq15WEgCx-2Jg6HOeS1QEZxnIFgffr92vPmebe2-RjXCxIISrAk8Gbr7Urr0ayg3z8pRsrPFEE27js1FmC3yeeeiERjsnpttaSDOx6sneQCYMf-yao3PiIPbUSVBU_Oj5fPQKP2Us0l_lrssJQo9MvEQeXVOLbclr6sber8GpTU5gb1IEVW5geXQ0QH91B6KWGzglrqcd1EaYOVAqk-zUKvU9jVJwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGBtjDQ0xJPRF5wtj4QZCOqjzVGMi1Ws_nQYUfyOqHgH4UUsd6mMvgpKwJY9lgmNXS9ifM1x6ZiLFh99sjhnF1kkUgUXfCcAtnvGvbP4BP8nz10Wp7FvuL7xuPoagYolfRQUcjVYK-jVkrxSk7u4UXtXFcfJx7MHqJ1itO717QtEV3GbGkadlYsWzClFe3pKgKI8lIReQPb7koA_EnstNa2Y8YDsfzVJVRHtxi1iNueoSsw_2A8Nmss8GvLGSF-JpNj17MKwXh5oABPf1Si4MlSDfBHQjMjj5JP62yk9jzyIcwKlpiuaMcDh3GwaXjoJ2zvPHyUy_WR_KAgbs_bbNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfjOld284jZOTWUhOb4WBcOP_GaWu3Ystc4WkUttWtMWPV7f4nZkD90gQL5d8CCVRNLEdcSWWBBGcmg-6A3JwbAwTcjNpxMxZQTWzr0OsZTAeHNULsx9PmCj__cl9ZknwQ-DH2LEvCNVC2tXDqL8SHg9SWsKNgCip0hpKXvc-noscSwM1guZXlDyayMuuTnxCPB0A65-B90OCAbmI3JjzAMLOsxVJGbkZxHhCTjGGrezaXAVHkizF-GFissFl-ZcopJryrq5vRiEVEPW6CH-zcceebtd0M3UTKoboTc145bTt2ng6R1Oee7UET3DkvvLRtxq7WLZFNbpJRI1KkdPMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTA1-nF2mhPj4KmLuHTw-tM6PbwPtgGPaaiBj-awx8DcuTmkl9XlvQUWZKxObZju2fH9DB-P492-5Bvs17ty6w1wXVt6-asT3ekGL21moNgQpt8xAK-AQVODyFC3SAvLth7YuzA92D6e-79XnyLbLLh7cq-dIM5zG6InBF_VKzgiXjRJgapqXQB3GaC2X3Ct64dt3tZ8V23YUdzw0xrHBTfgWXn9lO0B2zLznTrejbnpxE0q5I--CNTLEvmSuneUQQCuiguanaNr8qBp4tojAG-0zPo4AA1_W7iEKbp7amO8ALjCNCKW6baISQTVBGB4QnH6DF4ZXlT0Rjp77zxRrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKN8M6NKNiNhhZDW6lW6j45KY1sHH9AjiD0yKEf6cBW7YxJ1w7zy3wQ9QVVmFzRwrrdHMgyEF-jOA09_oIeC027CZBx7g5xiHxKOtRaVh1o_TEUFCyTyGgIslyXqD1f01HHJaVGOwy8C0_19WTB5Jrzbur-GdIpv6UIY9ahNrV_KnVCp_UAANs8gZsgIOb5P3Z2BCWFojelHmlp0fxP-yxDdxxM9kOFW-_eAEl97qMEFUEqdAw_sdup9IZtmLhx7bE8u5J73AIr0MgsZob42NFbswSnwU7HNg7qR7LDq1EhRzBUe-J34eTWeJhj23LPmlzidymOtn1m0WMD004lydA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYetohYBctJG24T4IdCXQMJ9dK52eJnu_a5kGYoe2ki4Mh8GEzoD8LwMsyDoY_DjT1kO9jdBGaeRmj5OrZFjGf-hZUv_9PM730vfphPP7lw-DQwnTYnTBZ97ddJjhXB2eGejrGI5ke4hEqzyNrA-QHCeOHIII_OODzxV_rxVlOXN3xIP6zcD8CDdRvpBOrI4QZRhrKT-LI2CgrYjq2fyqkgfF_ziUa5yuJj67q90Yf4fbakS3j8qNYfS68u98SBm5xCRv53qw-wXcX2bYa_-cn9Tpe5cGi-6vfIR8-m9BjpHGYojmFV8Cb9zXOhzK3Zko6hx3_WOQ9-E6kS0VK8mCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQImL41KS90l5wq5JsOUCObRyzr5gCdY_sXgmQlK9EHPAU00IPiFF6ttC5GI6L6OH_jzx03TMiavLVodD2DDHivBbvaMd9bphCAMHVoOf3JeuQtNFfuTX3t8BF79GPWfqXE17uh60LaqFKaZBDuTGPa-yygm9W_oWHcRmv1ALBRjNEGGXuO9u_w55lIF9d34IqDk1H4pJN5n6TxlWe9VQqi3SiiLQcY35s2GuX2eKHPuCk-1ZrorEwHh70PMfl9f33L4eAQnRoUGXHYA9plMtydGpyF7DJG80YkRmZaekC2twIBguxwZznQ1CsYj8mykAR8HWOdSJYV0mOMCanTzYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFvU3FSLMe4miisEV0DKAO2pesr7J7k25Bj_MnykwhQ3ZskGBZPT6dqNVBAG0xlbqp7yPO0B0U_dKFOK0pAPDyFyZ1_tPrl-fgmq0X73GeJaqjfdUhOJIJLOU2mHp6_rin6GT2Qb_L64ZvTUgD_uboJIfhdFQ2aFqtnYwLzGxp41YnPxrqU8uyDgNzEXvKMQGUT9OKiQreScHSzOLowBj3Q_ocREiLCOktp-L7K2XO-oXk7-rsCkELFE2MKH2zPaCTTzdtyHCPMw8_TPgCr4lJaJQ_KuSFaNQNqsYqUu7MKZceoYHw7lJT8i6IlWWSh3cETdlFbfk1wuS55PxWLuGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7868" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7867">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riNbfmIA64daQmk87zsbrFmGKXzJ5nZrXd-t3H2nceAoyFm-xyTlqHJ6ON7VNq0Zo2pBTOpRV2K9_mTR2UtQvRmPur5BNU5Nld1inJ-Jvi-BiLmstuN5dYQgwG0gacxHMl-xMu0QWzIi9_5QnUVznVsOzWUCpyOhEnDFkBAsDu39wq404TyreGn1AGFJHMRXhDO3gUyWMrXtGIiXDs-RQHLxYRaoKtUDOnlgkTlY_-fBlMpCe60dqDY_jkJXcDgmRxndCIbem1yQXtjbaZsEfwRqMSY9SdnReFso40_3H_T3FYFIzYDuKcC7Vah5jd7pi43L0OLiplRYiPrcYQFllA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7867" target="_blank">📅 16:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7866">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7866" target="_blank">📅 13:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7859">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dr_l01_wnlPBQQ59OV6uOdnmlWsmiJ0eOFKXbcq2sYAziLHz2BW2c8cl_vkOMa9FfBuRmVroGjyXXKWCUjPGd-Aoo5GnFwOdWdGUGQ4hC-105UQgYfSYTJjF3QNNgQo_B6jcC_iCJBbIj_h6lHGiEq55dzx-NZykDDQDNseI-LOJG6Zl5vB7iUWD0VcokwN9EvtGCgaZCX11GhBoWJXJqMrkkUg6Gmw5z270kMNbq7WNFRo-VHNsRsf1THf68TOkSGKjfMJWX08kr5b8j-KdyIiz-Ldsv8EDdj2xn-Jpb3rZXIueOD34W56uMJO3TQME89DdRU0jZq-va_oHG1iuTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aVFIrupCyHh-zBRwL9Q0FOfk0GBLgu3pFMKEkR6dsvWCtQZ68vW19vm7D_HEh7weWeaTDA2Ajpb3Pd9RXp3E4zU9gV9eNQzocJYLYuw2sclGhe5NCyAgQar7pHqRiPhgmhcAn13f2HTBeFDv9nliNEGHH1wlsavFp-uqFXnwAabsboZK1ks7Snhay5h2FlqPqw_Xufzl169X02chg5ePVXjpQmo2zG7OnfeobDqot-bkM19CUMHf5fHCEQUwig7G-7I86h5IdenlLQsu6a1RDTtX8mKbSM_qjnXNNnXZTOv4dmsTITFKKcQbXRFjZxHHU3oNw9hGD2I6nxq-29YlmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VDHxINz-zIexMtxEzqPMsn01nWhq1hfotnpvTCAPjfRAD6Qz47DAtwrjcvGUq3b7EZ4omq4NeVhWXGWAFhFrZU45cbR0_zBOEnxw6-pmvZgpRQZsOtU2tuEmkuZ6b0bRvaIn56UHdrFXqHiw0cK07NqZAvmn1FSMlLX9GpGSdi_vfONHHzGNCmRJgDDuNR6v842-t_lY44cq4qbwxYV3vF2fgrOM6JYccjNT4Yp8TFTf-3wQMvfGI5gWdDSOexfTo9NsXhH2Llvh5uSlF-vS3cPry-lsX1EuwvlbF-W0j-AdFx4rgmuAdwcviic3PA-HecTbWbD7F7Um_BBmoIfJfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=V8zHt2ysW9GgSe_JaNwfGaxxMj7NvoVLx0N6golrVcWUSMu4lWhdnzWgZz38hTNvSnwhW-3EObVAEZhwZUTwZ_f5QMDpZhzOUkfZGp3IH1evSlBYyDkYF3yndpherEgoYJgmspmmqBO1_pA4RvNjEpoXsllfd3GR5TnFOHTX4kY8uepUGVJR7j0w7qU8KbfCV7MgAf-d5h3onKTVZod4FYHUeCW6RPE9e8lsLw7HHMx9U2vDz1Wa-AsGidVugD3l_SxFsQbwejx7FwJg0vPdxTEXsyLpDy7ctmDMvk5mRActGJZWA_ZkSIA-QM5s0hmP39WSxG9CV35gV4TEL3iKaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=V8zHt2ysW9GgSe_JaNwfGaxxMj7NvoVLx0N6golrVcWUSMu4lWhdnzWgZz38hTNvSnwhW-3EObVAEZhwZUTwZ_f5QMDpZhzOUkfZGp3IH1evSlBYyDkYF3yndpherEgoYJgmspmmqBO1_pA4RvNjEpoXsllfd3GR5TnFOHTX4kY8uepUGVJR7j0w7qU8KbfCV7MgAf-d5h3onKTVZod4FYHUeCW6RPE9e8lsLw7HHMx9U2vDz1Wa-AsGidVugD3l_SxFsQbwejx7FwJg0vPdxTEXsyLpDy7ctmDMvk5mRActGJZWA_ZkSIA-QM5s0hmP39WSxG9CV35gV4TEL3iKaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7858">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZPYKlWgKeBRdCAaJgQRMZ0h2qcyhaCaElggnpGY27xatbh8N3xiC_0nzSSjFL9dj3puNahIb3BOyd-tIQRwO8yUv7KdAguv0W-nJh2s4AVaKaBO0Vkw73aPn8-r0O0oXl0z0Ng_0UOIJzrC5U8I2mYLBK7pDcp1SbZ61UfVR8yjmSjFv7IKg5O563L9P5uB8975v4lKOFmOzUfbyah5Ze2-iyBXE5Ztxeh7-pKavSpnyX2ocfyMgVEAlu3A9ErA5lehsmlf22FjK5DbqforLbBoSWChOVCMWRexuxrK02hdrSupOpVglnAavPLr8CedMe4AsgWPynmx8QNGSS1dvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام دوباره یه قابلیت جذاب اضافه کرده
💥
🔥
حالا وقتی وارد پروفایل کسی می‌شین، بالای صفحه می‌تونین ببینین شخص معمولاً چقدر طول میکشه تا جواب پیام هارو بده
🥵
حتی یه رتبه‌بندی هم نشون می‌ده که سرعت جواب‌دادنشون نسبت به بقیه چطوره
🤐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/ArchiveTell/7858" target="_blank">📅 20:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7857">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7857" target="_blank">📅 16:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7856">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaPiVphV9uJxYz7tEf1H41CzgoMgyHJLz2lwR2Q-PaCBiCu7-GGCG5wsi5ogQv92mZpXfq6EQw5GOCEpTp41bFIgMyPH9oNvQ7ONKoszKEoxsuUHOkUeXySYyWduqpvS0EF5n1tfeqLgD3gZHPoCOCKQLoKM6AO21E6TBBhSMdLK-vFus53WpgJaNYSnv9K6dvCdCyHy3aYV1DnovpsPJae4GZDhOlT8aWcLV76uzJ5lD9sAXDjHMGwMY5rDASIDjXSyRw3p72iqnZrfVLVLaqs0Jk3skgIqew54cko9gRym2j3WKsWUFb_Ij6zdsTnfEwv2o6TaLdiAHhZ92vOicw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7854" target="_blank">📅 12:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7853">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7849">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=XlWQkPXyYwfPoup-d9rTHAFRJw-Jy7vUl6LLGDfULfvjo8_bdJK1kJNH-T-4gix4oMtc-_xiQvH14W5A60bpM0N0Q3_lj9pA5M797njmqo7DDJjHGL8rDifyzAZUsWvXdWPK2IFE7sX7xHPF003u6-DVZokOGijDO52_T1wx4LaRqTfTgLBV7n_ZiWUE3GYIDvHnBoKYEKKLSHeD1uyBqDDJQgIzGJTnbys7x9zdGG2WYF29oKD9CHRVtbkT-fxRJVNj0Xfc3dxKx2nHHA8ov4dyJ-LY7zjEpKPVuP-gq25QPMcl8OGtOtNP_nCmBRj1yScExsJEqYTbHAqazpWttQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=XlWQkPXyYwfPoup-d9rTHAFRJw-Jy7vUl6LLGDfULfvjo8_bdJK1kJNH-T-4gix4oMtc-_xiQvH14W5A60bpM0N0Q3_lj9pA5M797njmqo7DDJjHGL8rDifyzAZUsWvXdWPK2IFE7sX7xHPF003u6-DVZokOGijDO52_T1wx4LaRqTfTgLBV7n_ZiWUE3GYIDvHnBoKYEKKLSHeD1uyBqDDJQgIzGJTnbys7x9zdGG2WYF29oKD9CHRVtbkT-fxRJVNj0Xfc3dxKx2nHHA8ov4dyJ-LY7zjEpKPVuP-gq25QPMcl8OGtOtNP_nCmBRj1yScExsJEqYTbHAqazpWttQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7848">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7848" target="_blank">📅 23:09 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7847">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hH-cxwx4RkCP5elugF-RX7qu4yGGT89gKNyMMMBkGF2JtJH9wlv-o8I_EQgNFTb3m_SKRwpP3faBCVnSG8D6dqo5L3gMNcsEXchzWYzi0aLowTeQ6tUPXNIpoMdjBu6BUyuMtL06uXTLda9sOm9KHWSWi3cbuYJg1Ricrn3jj_RhdcRE1BybWVljSXFot2GWSd5rw6Y6z4jB6tVIkKQ83VrbTkxI0HVsmc-Lo9zMHaYIMF23bbOMtc_Qxki2KIprZKCvtAy8ZUxMkDo-UXDAqpcfw0o1vzYNs5tauGiJnjmBCMOc7uVmVvtUXfTB4zVaWNRmca6Gske62M1hXE396w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک 3 مدل منتشر شده امشب
🚀
مدل Opus 5.5 با اختلاف زیاد در صدر جدول
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7847" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7842">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXlzqKy_pi29EX3yfx9xlFl8hStw6LKZsVBjgY7A5Xf_inly7-HANQhxpfAjb7e4oJhbIh3KhyZGXb4JjXJHzG-83ZBGBxJg6R8S30Beco8kxRYlz3CFo7QNN1y651Sb8B_qCvo595W6pI-f450G2CQ141eOh3_UEItKW5HujWWc6mr6U7ELz3ovQjgmNEI_aa258kJHgLM-4LgagVDjQnpM-gJXVd8V7ECHuwpPmD3622wkr1-sujmMh2aKniHhbOjGIatxk0oNUQuKpY7jFOYj0QlCLD6V5U4EhADaZz5C4e5wCncPDgl483eYU863FIR9sHUuaekIfjID1o60Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MBXcwo2VfMfGANO8C6VkFoxLOaNUQ2MSGqKrat9RO2BGGERYdGSJYQ9895oJK6aJgEJUNi1EqvDFvNXaWL0p5hLPdSXOo_8Q1tSbN_C2BzANwbGf6MBforsOFU4S-hAO1e3vJTF4PtcqPUsheUrMnDzp5gSowPFXCSkjflnYxeeXDuvrpYdwLFRa1lQTmMn_VQHbzO2ewktWLzYLBCYm1jWguNKCEjFnO9v4g0tmeB9iPwJ_mkBNQqbE2XUFmL7ft8ByhYaZskM6Q_WQaFZob8nw2sHBL1sG4fi0I1K-4us-vA-VgeTtM-cXrCj43NryGzZ7bwtIyZ7qbSCvdQNDig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIqNiyi0y4QwtDhLZVcWDiIKw7lCM6tKvreZ5gKnh33Lmoq6Es8y1ee7Hd-eEJ-60jiqHVWT5_k_seZtmvlvc0z4a4TpJL-rLyg45V9wDhdjVv7rRK__zuyNF8xBrJKeBwyEPPY6yuhctDXJCHqiC2EjgzPurYzfRDN3zt34he_QIu5xPOlVlM1N8ATLVkVpoOp-zD4E10RjMA9rbdtserhfkuGuwcLc8RoUv1ovZ91nDfg01UCmXq4AtbL9JMU53qNpmxjbW7O75ET5OjMnRmBNOMtz2xyvvkTJ6y3M7zejUN3ojm_UAThiCGz7OmiesQznerj1MFvphQ5KBrfeQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DD3Nc51gUKF8N1Y-E-dKNB7kgMS3bUBObCDSkjAWQ6QeJ4I0vFsSGo5hoW1EJDU51F4GiEB8jp1pkUtfI0Z9XwoIC4Yx74eEi81-BEX10BmjSyCfFHJvoo6zlhBxUhVF59SVlabkLvgpTk9Rsk6CL4KG76eGqvkZN8MlHYlnm5qOXOUEieGd5TCFw8drazmqVFNI_yrust8pua9q0tzGKRympo_XzpX-QPLm9O_RDO7yuaLod8kvOCfCw7l4t3R--d9UkPmxrcxwV1YWZ1iPpKV0YrL3eVqjPfYPWigv9GO_jbBL2DbgK0UB5v3JjNj4IGXFYRsPWPygnZ_wE-5zCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jYIOcfIvlOJpes2bKA_lDLK1qVGXihj-vgT5QPLIkCFnp-3H18upRtkJUSz7CW9KDP2NBznQrucyYXgZPgP9B2VM6ZEoFEVTPLbA0bLwgr2pcrkd88o9RmqRBhvth-qE8Y5sU83jvZ8-rBQUq5PCfiINMuOlSse6aCJfhKX8Nt9mmtqAk6eaw5UPF9Fdh2DhpPOcz6Rmv6wcZTVry7DaBxBy6k0MX44GAXxz1yVNGV6uj3luZsyTO9BBWtytbRjrZHvntGkCY2t6Hw56kRvvpTabV9MAIYkAibF2rA7F5zonHx65Bx1544-nYnFNoasNqOtaZGvPQGcZEcXwat0bjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vhc559DBoQozmd8i1k9rYB4iaYUynHlvGQ7tyof4k0HXLOrTjafKKoowpLBFlWoVKHVJheEcstmFNEDZ0NhCCwuKEKXxIcB-Ovdp4TRk1zPEnzGlfKemWITAHZfnZ40KaQNP_JMtIIAMvNCD3qfNpQrpk4v1-c3UEKIdbFbEw5ky0BQy0XKz0YQ6zyir8-it20Ce5pgjorJOP089mMAXa0U3ZbGPbveAxKcifghl0rZtjVFmJJR4vVKs6YST1BzzjXC3NmMXJSMv5wEJ1LZKk6OmY5lyLfc9DCwTYb_QC-WxQCJZnv7zuuSxush51mL3sXMjKvqYwNAjXY7IlWo72g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7841" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7834">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=Yeotf3RBxlo3YleDOf0nu2N8bRfoYJg2ceppX2Tcskfor-ZGTt6I0_9Dg-vrZpH-pJQzdxRYR3BwLnrSNA3RbUDn0uz44YhH_d0Tg9W9M0VNovowdOgtzVfpwxNE4eAPgAxj44Iaah4z8qj5eT9vEAKJNkwN3Ew9FomZgn_LINSrlno-_QKLNEDO5p8TC_KHAU1zXBGa_cjdE12pK9wVlB5YdVav-IcHJSxsBxYECOFRqG0bIeMyOwLyUBZXdvz3rP6ZfiT35U026nJmHuM4Q_xW4bgLK_vGs7giAPdMpL-rbf9jSFopXoPuKcu8Om7AOWMYkyznv64VrgSL_Wl9vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=Yeotf3RBxlo3YleDOf0nu2N8bRfoYJg2ceppX2Tcskfor-ZGTt6I0_9Dg-vrZpH-pJQzdxRYR3BwLnrSNA3RbUDn0uz44YhH_d0Tg9W9M0VNovowdOgtzVfpwxNE4eAPgAxj44Iaah4z8qj5eT9vEAKJNkwN3Ew9FomZgn_LINSrlno-_QKLNEDO5p8TC_KHAU1zXBGa_cjdE12pK9wVlB5YdVav-IcHJSxsBxYECOFRqG0bIeMyOwLyUBZXdvz3rP6ZfiT35U026nJmHuM4Q_xW4bgLK_vGs7giAPdMpL-rbf9jSFopXoPuKcu8Om7AOWMYkyznv64VrgSL_Wl9vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVkfeOdzkkR2zArwsQ3SJ5NYLCGlQiHex5oCmc0wIFlfAwnv5A5LoteR-HlTwMC3pC2tzRX0WB7lghv0UdVuf_SAZ7fqIdZVOofGVDSanOTNwc3S7SyY7Dq-mSntQVhQEazTN0oDhyPdh1Zxn0M06ly2xg0aaUQjZgCUywfwFTSjaeP-QV6sitigim1QPGPIg_AFRCSS3W7ut8l0PAlPDXjR1cOvBZTV0fJmFGXZGm_xRxlVkTXpD0s-TaLHZSFF9jrW3NDwlv9NbMuO6wFVlFz-726fUj5avdZ9S8ZhJUmhJmr-uGjjPqsweGHvj6Zy6fn8vu6lpOa7tgeXnlQK1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود آپوس 5.5 منتشر شد — شرکت Anthropic، مدل پیشرفته خود را عرضه کرد تا با OpenAI رقابت کند.
بر اساس تست‌های انجام شده، این مدل از Fable 5.1 و GPT-6 بهتر عمل می‌کند. همچنین، 20 درصد ارزان‌تر از نسخه قبلی است.
این مدل رو
اینجا
تست کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7826" target="_blank">📅 20:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7824">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZLzzJNhU3dPqbhUYq5UVHbmxDOIbCzMbEK-Hup6FzcImnZ5yaO3_eNDTCux2IM13WUOjf6clA9t3OSXBDKrqoYTGQmhLMCz9A-rV-0Yl4KtpwDVnqHFGMPBMwxtbOLjWrVSABWJkazIU6IQjghzgNLXQ7VtAS6k7l-JF9Uf921s3wG2Lv6Gz1PJAFGOgW4X3GPBilqis-sje0_ZX7qAP1jBwZ3PyPsDgk4q7vYzhpTb9mlgGEHZwG85xseXuKK-8kqSaJMvNSR3D7n7hw0BJKIW84OX76j1bFzhAg-nRMiYK3KbG5qWRZN9trGZchFlTdTFjm3EicM8SlVKlbeZXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efMoewoEkxswEq92fY1ynoMtJ0vadjZEbbhsu_kDJrT2nQi8Y_9vu2Y1bxhdpcgc2hPBFffatw_n1kY4Y5RaV8L92X1yNqyLG3ADC7Ot8zgQNm4ndw0QAc8q76AurOlJ6xDaAHRcV9u-PZtzUJgieK78evZLBysgyx_3_YVYJvz4DlVXwMTWgaFWmL1jEqYv_kB57kEVl1EwN20VLzfYVYrV5q090yX7wwq5_iYe5ZX2iFfPAXHAbupE6cFAj5fCg91dGpyYDwugb610BYVIUMSRSckN1lYY3zgn0xubFvN-hkIm7lJlfyCV93oZpJ8jgNBQuyja9Dy2ySXD4J_ZNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/ArchiveTell/7823" target="_blank">📅 14:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7822">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndzZEIUyuNPJa7bH5Wszwvt_bfkT5KX1RXI_5UnQIxJpX5SPZ0LWJOya1bEDbLRh3ulN7vrcGLuEYX10sCy39CsfOODh2E8XUlR0qvg_296Vnz-jCMEJNDXDogDPc9eWQE5dJu7lPYqhuBpth3tY0oEeRJgOVEoRw_rIaB4cWVUWEOuFhXdxOkY3DPt2x1CHI5ZfStBqO-iwrOdDCBtE_b_Y_x-dWelddfsA0_G7g9P_ggnRlRukkJlR_DBOPCAQyibL-WT11Rj5KJefVvcqUX9WVu_Vsc0z16r80NxdfEryKzixivKbKADXfXPWiCuRe8YUGZFByOhhZnntfFvx1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
وضعیت فعلی بازار هوش مصنوعی
💀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7822" target="_blank">📅 12:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7821">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3J_QeoQ1ZuVThVZ6TJ5MPs9zgUVEsRlVz4JmhR70wCmgLnwGHAfnCc3RHtAnPi5OHMJUGrTsbkRzqOTj3HmVkLKNSlJCbiT_ou2DnP16QJopaK_ypoVd8Mh31R7GU0UVRdnLHVWFkvH5j7MNczsPxKeDov6n-fEwz5sppk08QV9vl-VnJkO7kCFGCv8NGEK_2g_76f-SSr6cUOkK6d6_uxahqw_ZoTYkRCxMhLuNDrVz9EkW5rJsXpqKbp9DJgcnt_Q-RCjIIJ03ym5NLw_i4ATxzE9Yp101ntnuQUGE8tOK22sbhc3hYIPQV3LsChyBGzn0bim9LLrMwg5JBmNPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RnDEgxOvhDo4GjHYszDZGbYb5naWTLRtEQtf12dCweu99vOMgkkRuB4Jcv3gTqjEN_iRH1pKjK-nuE3Vq7E8SUaCzDthuBukjKja37ysStMbZnrxf-XQJQroSsshE0MMkG-2wP3dJlsUwL3LaQfHu94iBRCw4RgQ4qGh9-5LDtSngISQORi426MybKMr4V0npwu4O-gGi-xsQvqUd-tUBqR9VE1PR9fsFuTdO1Z9f1Nv1v3rjXL6XHRUff5FmmniNtmOOzX-FqhG-wbwuiSlc31I-18HSRi1YYoT9sFugLKKRKXur7_QfdIfMxWIof4ELIQPTf8AOw8F60G23zDQcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SLBKPXfGrTWhTsaQ_00oXLZfmChdOfGVdIP0VSzGjda7Vd2XF-4Bn5bjwvE4mRjT20Uhw_jivJc3keG52ETKwwaAbbEA35limEh3UwyQOWKinNZ7ESf3si0nRxmEOX42eqVCykWPOfzYxDcg6MCqRtVoA8JCtIXPWnkvCMSFq77LcCoIbW7-8OeZ6UUKQFrH1ux4v0ODFBs2z5l8dg7nxM_5q09Ow2adHU38MdFuKozjlcZDIU8QRQOLflmDvCr66oLFTsSOaya6X_DYq9oEz0Nmv4gZcwgvvSC5N3J9N-Zl1sFCLF1vhPsI4PcalEV4QeAkNms6nPRa-nRq-cDI_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mt4DCydD3hTMry2NAP-pb7sCGRqlpZBVPVVa8hIg_4y6zx18u38YU42nzqE4qxvekZN0gABMeb_AdtPcItXA-vwEwbIdp8BNTHnqZWYSS7dJJYWEAOC4v1hTWfT4T7b1bJz1bpp_szQeH533DbLFCDDKV7ew6tvLEOlTRbkBSscCBUfvDLbQQw-5M0znzj7CF1eHCLBpNRzjpEdxBjxpjzTXNrwepQ7b_249kDffPvDlWlJho1bhRNE4arNFRpBM-XGd7sfCnHjWfISnK2i6ByoJ55gAQV8sAVXV64bK_qohm19E7xGx790JjxQhIi7EIrvjeTqKCG-4lYD1B2Qdsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی
یه پرامپت از ساخت بازی مار بازی توی حالت ultra speed mimo 2.6
توی کمتر از یک دقیقه واقعا پشمام
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7817" target="_blank">📅 01:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7816">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xd_mcT5UewtfaeDm2iFbnclSXQ8QFpuwHEB1GskPJt8YNeB8YQHqIGTB213g5f8FURGfvjpuZBiHET4VBDUm_3ue3RLOBJzHnwzFMUV7dK4KMZRcsCnOHSwqe7uFfkQy-lwJShqe51mZpxI_XPe2WxGlgr4VkJSMEYhHkC9L-Rm83TKSjN--vICT3ddOiL2W4vqsBTy0Adh5u9exT9sVGIPloT9vi5AiRzrkhkQ3OTlolEb4f6CfupcSiq1DswxdV8PwN3lEr5y1KH7oA2vPw-XGqh88tj0urtrRNKjZy4YAT8W_uFCkyeoACizdyD0NwWAWk_R3exaj4NVjSioOFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد   درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در…</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7816" target="_blank">📅 01:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7815">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد
درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در API منتشر کرد. سه نقطه پایانی (endpoint) جدید در کنسول توسعه‌دهندگان ظاهر شدند:
؛ mimo-v2.6-flash، mimo-v2.6-pro و مدل پرچمدار با سرعت بالا mimo-v2.6-pro-ultraspeed.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7815" target="_blank">📅 01:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7814">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=re16P2V7lFNfuWQ_1Hwc3T68dPTVVsdCSBUQRj50_X2nUfKOa7kxHoR7x2py4nNTa7OaFOyM78ufZn_v2MI6lIcMNMLRbxmFbvkPMUm7c7ZBO5RVHm4Dh3zixi5CDXO3GV13FF-uZopzXAG5s2aqwLC7KQXsZxC3WmhvKlmuz1hzIriRMf7mc8Fke8iwGFJDaTlHq6SloFhrvj5EdwUdD8uH-WncG57JBJZhKjjna81xMMb7E1g6Ng76Dscwg-3KklD55lTKFfJdM35Zv9KscLMfG8dSo4pZWXA94OtIh6oIIb2fg_sjjih58R7eicuUh6-93yZ2toBq6MWqP43WLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=re16P2V7lFNfuWQ_1Hwc3T68dPTVVsdCSBUQRj50_X2nUfKOa7kxHoR7x2py4nNTa7OaFOyM78ufZn_v2MI6lIcMNMLRbxmFbvkPMUm7c7ZBO5RVHm4Dh3zixi5CDXO3GV13FF-uZopzXAG5s2aqwLC7KQXsZxC3WmhvKlmuz1hzIriRMf7mc8Fke8iwGFJDaTlHq6SloFhrvj5EdwUdD8uH-WncG57JBJZhKjjna81xMMb7E1g6Ng76Dscwg-3KklD55lTKFfJdM35Zv9KscLMfG8dSo4pZWXA94OtIh6oIIb2fg_sjjih58R7eicuUh6-93yZ2toBq6MWqP43WLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل در حال ترین کردن
Gemini 4 pro
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7814" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7813">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">😎
از 265,000 اعتبار رایگان برای استفاده از مدل‌های برتر مانند GPT 6 ASTRA، CLAUDE FABLE 5.1، GLM 5.3، و غیره بهره‌مند شوید.  یک حساب کاربری جدید ایجاد کنید و فوراً 250,000 اعتبار دریافت کنید. با ورود روزانه 15,000 اعتبار دیگر کسب کنید و با انجام وظایف، اعتبار…</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7813" target="_blank">📅 22:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7811">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/ArchiveTell/7811" target="_blank">📅 22:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7810">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QETVqWRIBhjq2bAWE7vDWI9HEB4_pkmnVA3gKEXKINGOLM-Syl2rRO52-NyHgCbZQ1yLPy1nLm8oZvY4EssxuptCT8bGE-prmpZ_om8Zvt3jm2PPajTpJyI7huzlx5Y2CMOG56BTzLQBNGIChWmMGAExtHDLZeQCekaR1qtTZNH9Uai2ylxI4OJIQ3-HRCGFSsYdEEnrQgYS8L-iiaZD8bIcG-aUGIcHncEz8taJa4RTGb6WyQaPi3TtQgo2g8msCGoA2502UkRVcVpI2QKfjAEKlntoAxkEW5YFow74GbdpPkmB0jlB-hoBTG8gvAduDxsm3abtdgsk8m5J44RWvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7810" target="_blank">📅 20:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7809">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtrg__G2AKHBFOeAd7jyzO5fTkrGQ_cnW4Wyu8Wmu4A2HQTH2TLFxktOHg2Brmu7feA7tr1rhjoJIFc4mus161f97idSzUAGUPpyYaLYHP-6Le3LFOt4X7xnsxZhCpP7nojDj-cCX8iM8fd7fEAsPamwxz3796tB_GdcSJILGC-5uFRsJVwhHKt31O9xkmy89lWfZxVub1mC40HStzpQiehPBFBtEPx8fr9IbZ__wHXuqLO3tgDNpbPnzkma9xvM6pFlyNHNTd2yoBEb-16sTwUedeN98O8aPrh_ydym_dh5Zym3gF2p6eVkHbpxMtuSygiNoLMgqBMQbs6bRfP0Gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7809" target="_blank">📅 19:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7808">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPxGQWJlY9F7DUyvI1lTKD8q8iZgwdV3RzHaTkwYeyYCFSL-B3ZmPU7NLfPlzXsfbnx9lUOjjyQOMntAMeOCOTO3CzD3UnCocm_o_ARoMlBBU1dkimg_pHsovWaEZGMotSFWeQ2zTLL1-TRXaNc2_4s2YzXuYQtYl7_ablepogP_wtCEzoyVZRv6oUf9npTURPoUMyYhAPAKv2OZ93FFLRAWaTPZLB3Jen3tGL_AYAr13ygTuSEIWsiKuLXgj8HjwGWqn1gW4S4B1Co5Xr94ARc3NtNUtodePrTgdnZIBO9rsDI9s1eFqJNnJHVoiIqtduBz2vL0sZijTfIzj_tHIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGoHkPmYTqJEGtLCD1A4V6cnbAPXiG5Q05WfIQLqOi93h94geTHc4BA6Mxwv8YYxv721GimXSCCrBnBKYUQhZ7uGqXcc5VC9yGodk84hKJWxeyE8zmqAbzGJGjy4nQWkQQY4_BzdzD9daPsNudylN9iTfv3u_dQd-42pP8FexveZ3_911xvU-8E4KATe-ES1DfzeE47iOxUKDeOon3qYwZSus_UaXJb38q1t-A57TpRpMxp4eNsn6qTyTF4vJliOUkghfA0zawwfHEPw_UWpJEF30SuXrqiAa8DhyCU7KVdHpneZXqMeq8UxvZ8FXqLLKHba0DhfcJZP5eVBDChNVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Jev رو رایگان کردن
🤣
console.typesafe.ai
120 میلیون توکن رایگان میده تا هس برین بگیرین، درباره کاربردش بعدا صحبت میکنیم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7807" target="_blank">📅 13:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7806">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZCZi1rUK8PLdXb4vJrBPUJCvQ5Pxc-shfE24wNTLmJyrScOnBTBwhSofov1FtgLIqeMQJiFz6j6aJ-PHfZJX8tIh-CBkq6KMjgBW0MBUPSQpeORNIPXcjAyk_QAEDT6WuLXC6CCOmRKZ1qIraF1UtEMTc2Lgs66sL3bR-47ualTRp4o3KEox99hz2Du20SJpXrEcuQJVDrexClgyX5HuvhB22ZFhjYWErkxJ7pmIPXFkTtY1_iWcnIjj3GlDtqjYg4d_wl7Fuyr6iBqdLOx4f-48xhIUj7-brP28FjPg5FNR6ud4ZXlfhsT4018rvbIyt5KJCbIm77gkoNXUCmT7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود iso ویندوز و آفیس + فعالسازی رسمی رایگان!
همش در وبسایت زیر:
✅
https://massgrave.dev/
سایت قدیمی و معروفیه، سافت ۹۸ و اینا همشون از اینجا اسکی میرن
😱
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7806" target="_blank">📅 00:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7805">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd5cJ9DO3fWU0aRYcCueJE9qfDx8hxgrM5FtDQkGUa4ofCUaX7IKGFmMh38kjSzKlbzlUXWMIvWnCU31oOdctWW4skq640aPZbdd8JJ9LSAlAEH8cOR3vcw_BjOF5Kt3Fqcs741HhBeLp9uLpLtF-FiYW75NfeEzOfpoi6CTnV9fPWRhl2T97CBsOLOIgViE4gXegcU6zgowNrWdFOJeXv0UWGvIOL6VJLvOk4SjegjUuKbqb23yN30KfQ_tReV5hzDQK89aJyuWKoIrF0zV6OgQ3UXOc-gjrIoyVEThX-zoBK2CpQELbV18gphXX6n_l-6BcDM11EPda-eEgm7cQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7805" target="_blank">📅 21:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7803">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hB9J95wKsMoEqZJS9vV5_8eztHe4iQTiFiz6HBiCUCwDBoSSSV3KCcPRulrByGwrOEcFc-KsBEbVx3XzGkh1QoN-nhw69ts_kQYFDT7EeeQOKyPMEDipJHqm8SPlsMD5_CyztolN0CHWmbKt5D5qgRSNVdq3N1B1U8_6ItoO8WvzsdEaPmC8YxF9jW3-G_OHyof7RmGiyY7MuSQpmMiMovdnAmIYxui9dY7bF4R3bBqTlplUL_4xteII81TvFhU4HkaZFPOawuui1cydLg08Is5tXPWPid2MvPbqJmJoRYsffmCR8TpJfsY0wOB8aP6bO7q8szuqMDhBG4c7UpiyPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQdH3M20zMFVD9BgdDpn2YoVwZTDfeZwsDTKmSnehUFzvQIpuDDTG4c4AkMC9UcybUjTBnZFveq4pjfD7_His04WN6byaGrJosLM8XPGZzM4RipkTHgs4g7NR9IkifPsmlpos1F7ewdG0iDpnOta5_RUP94RYbjhpDUHBTk158dFTz_faLhkZ4m4EPDDeBgLTT6QA1EPqj0j6yVVYtlkHMiWTJoK7kJxGdyxIJHsF_ZLkdfN-iAEQddOw_BjkAr7LkvFNgDjyjvy4h6m7VYOYUpjlRrZcG3j6dxbMbJ6hPP8jjaERF95mcOXNa2gJVSKaCar0rdHh1rS2wcUK2SaUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKeuj3WlyjjVaAqfQCpe265a46WUlIQFNORCOqLb8jKVVnOvSMfeoi5lv2Ypb7pESCchfLiIywpVQG2DERlu_4SuOcaYK95dSx9zLkDYNQC3m0eiJcKnZsN-kpZPK3WWMCX2279d0xi1nUTS1ibOrIIKdx9lZ_eygQX0dSqDfo5GJWlcmQCGRZxhgltMDdTrIBbAkwDPmCOWWribHlxJbN_pp4DIRT7XZPhFY2n459EycEeK_RM4FqB_KimcPRP_fujcgpQp3BGXAlNvTI1PEpc4G6Mut9bNfPK0-v3ZuatQz5xYKHHVjB1v0-rzNdpq61JgDT3ecQkwrds6hx0KVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7799" target="_blank">📅 23:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7798">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btfcPfESlwuseoaRp6Cw8W1Y3RMsXhyYeJUXQwmBlUcYo9d25g17fDjKNnHwHRR0XlFl_G83P7j0AVvb14P1toAlQ9dgszM6PXhbczuuxvSfbyLPI88QzL5cNxuT2EJS-LJjULKqNyMGTOhyh8rtQ_drYFNMlWEf1W2DQVh0_ftvwY-25Y49PDiJlyP7Oz7PB3N_QrbVaDKg_Oke4Xg2l9xYGKWWt4s1Neza2TuMGQJJ0VmPkiWhfbMmkrv3koPKNSzqeJ2QoawAqbF-qdGVG5Wm7BSGBK8r9sO1vEcMyAFyx6uZUx5XPRV2PpmPFDFTU-0_aVDQCsNRIzcyn68B7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7798" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7796">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dO9RhEn0BBKO1UE8lFpXRpJtqb1vJeLtzBhSJ7PcPzpZNKtFXp_h5iiGwhzNZCR8XmJB1rEtnzuT3cOnr9UCRB7irnF63G9CUI1kyedWFaAMhVIMehxMwhWG1qdb9xYkK2HZV3l1RfS6HWZ3kXPfrLqiJhuHlm-rxFteQq5iP1h4uGQ0QaLJwrhs32JlB5saAySNj_CyKVuQKxKM20-vkbT_hEwmc57O6BU6UtVfh-LXZw-fYngSVSHfjWi4VNcRt6IoSNkDzq7v84ooKGj-Y04B_1RwIN__TXGBfysoICL5zeoYCT00UPpmsdPmi1NvSieeLd2WnE4ZtiVrdIHH4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPeOipSP4GsxG78LWgM9r2EPsl61DJ52dpW_VWGPCt9s4BNg8rNorP75qcb7hq-SlV9u3t-YC8vunx3Zv_ljkwQeRM-6vrmZT6yXYgpRM1OtjjpNfwJ5m-CA1pe4zE8RY1Xp6m6lE5EZH49TlgRtI3GFlnFkUCBPacrYXh7gL8uT5fGhTrihFBRSrfTsh08SRg5UNYE_MlPgWlFTStvatSVpyjoOUG3ShSZGqa5KYXpi5H8SsS7_wbo9MYWwH5iGACf22w313tnHaV217Myf1jgSGA-d0yH8b-ei0SSSyJiggfJ7I3Fxfq2O4kE0PcDgDWUJGWjZAEBbMAumJ6HRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⌨️
مقایسه‌ی تصویری GPT-6 Astra Max در برابر Claude Fable 5.1 Max در تست کدنویسی Code Arena
به طور خلاصه: Astra در انجام وظایف تحلیلی، محصولی و محتوایی عملکرد بهتری دارد. Fable 5.1 در جنبه‌های بصری و تعاملی عملکرد خوبی دارد.
در حال حاضر، GPT-6 Astra Max در مجموع، رتبه اول را دارد. می‌توانید جدول رتبه‌بندی کامل را از طریق
این لینک
مشاهده کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7795" target="_blank">📅 16:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7794">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7HubS3gqBhKub4sU_nU33ZmoiJ1YoCK4gqSw9dyOInulugrCs86zfjeDSFmPvaPYZBi4Nd1XraIfvvtaBpSbWfvAdh7_l0_IdSQC4xVtQK_Imno5jaOCnAaAQKeiCqcYwdrWTN1Hxpj0dxCV_VaYXsHnkXk7BVZCQX_6EYMPAmkhpN8ll3WnVWz_3IrWLz_0hc7fjmXwSgJpBCy7vN-8sZnycEyrkGUdccXTdURFtPPRbQ37a5VIecOWuLPBvyr4vzhlbsmrTDPvi_gjmYyoetxUdtkHaeEQqVpsXpVe1sd9FSEs7DSnDcP7-b-qhq2KL7g0dD_MsYZxyWp-he6dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7nfulwWdSLoyseUrj6tzIT9ppjrIeAllurqd2TcGJzGoV86ywOZDtSu3BfrjK2VU6RYN7z9bGQZORUAMuwtGVH2jdQohT1iGN5uAT7BbB6FDevGAdNJKvURiigTL_BTAVo7wzjtKEzP-N2VjkX3ycOPheE7j5Om_-GQG2vWX_WI5Rzlge1rciKsyLrl70lSpq4rCL4smlVVs_n1KPe3kXo3aFOkA-p35PmHP_9QcLO4Fp5r1iYJx43_pphM181zuEYZrMC78Ir2iUvQPa-7U4ex43J2DvwuYE0GjAmn8p4lznKvs8IJJ6rseZPTvlPGNEbQB1Oc76z4Ex2pmC6g2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6341cb8e8e.mp4?token=qcgZQ7snq1HM1nngH8mTi9jOuGFP1FtTShFeg8Cr71dW1IAlVyqOOPkqljfanfcr6pj959-O5bztVz9ZL0E7v_8ZsPuiwvamHbZM6B2OFPemw5QMgq7GaKX-h4BR10Ad3SltgsKuqHz2qTuKAMv6BUIjrXpdqUgrcvsFtvG6r9q75n46LyQ1lHw0C0WA6lSIBVvxnXR9fd9aBGSFSVDHHZdRHUbRqnyqCZCiE2_Uo8hbmfHsHNG21MVQ0G9xpu5ZcpcTgPeoBjbmxL1uPfAl5WiMVz1iQY1Vrtjm69BXt4u2YT1Y4tCaecrYqPt9pK0QquMK0vW1GCMMuNVOTFPbGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6341cb8e8e.mp4?token=qcgZQ7snq1HM1nngH8mTi9jOuGFP1FtTShFeg8Cr71dW1IAlVyqOOPkqljfanfcr6pj959-O5bztVz9ZL0E7v_8ZsPuiwvamHbZM6B2OFPemw5QMgq7GaKX-h4BR10Ad3SltgsKuqHz2qTuKAMv6BUIjrXpdqUgrcvsFtvG6r9q75n46LyQ1lHw0C0WA6lSIBVvxnXR9fd9aBGSFSVDHHZdRHUbRqnyqCZCiE2_Uo8hbmfHsHNG21MVQ0G9xpu5ZcpcTgPeoBjbmxL1uPfAl5WiMVz1iQY1Vrtjm69BXt4u2YT1Y4tCaecrYqPt9pK0QquMK0vW1GCMMuNVOTFPbGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/RNXm6uUGjvlP7vcxr_d7JhQJTlyGJEnTftSqwKw1-L67QMBaz_A6uW3zfFrO93aCHg8K2PIlD_M1m6G6iO7tcjFZF0SH_NmR02055xRJMgzzzGx5pQsbNEjmYx_Bsl6IA1t23pdmtm_MWfipKXaerVuiYxrqlE-XYieS6EbURC5y1hQCVUJdYz6lINc3CwKJ6CZ4jx8pESg5EQ5WCBvkzDxQof1bsyj0rukN4uUvFQVpZ0CD3Z21tstXmubNGaXNL0g0Lcn-Q5djN55wYgPjdUjWF5aKuu2LROdMI892EQJrxWF8fma5P8ohGit1LBgdGOdeMAvc8upKay9CcWcifQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QsA54rh6PFr4JEu1qJpffrYI7xUqL2okShXxXBbU48Gl4cpugQv7OZePaDYDVU9eBtTs26e_XvV6kkaoQBRZw5FDYIjQTxARwH3HPgE8got-nmYEfJ7gshbdLutYoSeoruGjDU6tQjQ2m2YBqV_4UBPAAeRF2VzqV_4pVjBpa1I9frgGYZPSrO6-6VJOExdglJt7s5FVl4HqiEbPdrnUC8OZZEiiU0k5p1hG1smolUHyOIODoCUYzrX2Yps7rosAKF_l0OCFH_qhvU9_w84C3JBnF4aZpyM7mmILqEEEvpPjgReyAjgiiOjpz8hXNErOHCffft1CWRx8cbN5uQt5Ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">seekAI
$2,000 credits
API key:
sk-Ok0xV7Zp4vfigk6qXL8M6hQSeVGa5cRhhfkZ06yre2RUIAfN
base url:
https://seekai.cc/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/ArchiveTell/7789" target="_blank">📅 12:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7788">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRhfnkavFcXBRoJqDwdOFbE8H3ErWRq2s3w0wMtfr0J7Yr9aNNUZaBlbITINBqZukIxYTscV0Q7Y_tugFodB3LtLs5rq8OKZgzI5bQrmOA7CNCLze2DyJ93EEhDO6Zkq31NN2MHZ8zvb1TKwaj0MRNEguwqkPHHn4y0judC8y6f5uVjV5TeFd_tMyHcJK32Wmku5Z7u0SPc9hUZHgKNS9HoNq6MUiK6KcCHP0SBwHgE7bCISW8A1Or6unGcUxvO4HKAwzzly_XK-uGsakRtZkBopESbZyZSRryYP02n6UkqcnFnht-XVJyUFnPwIeOGhs2ilBf96cjof0AfmXpeCBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7787" target="_blank">📅 11:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7786">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♊️
جمینای گوگل سه شرکت واقعی را هک کرد !!!
جمینای در جریان تست امنیتی ماه مه ۲۰۲۶ به‌ صورت ناخواسته به اینترنت دسترسی پیدا می‌کند و شرکت خیالی مورد نظر خود را با شرکت‌های واقعی هم‌ نام اشتباه گرفته و با استفاده از اطلاعات ورود لو‌ رفته در سراسر اینترنت وارد سیستم‌ آن‌ها شده و نفوذ می‌کند،  پس از پی بردن به واقعی بودن شرکت‌ها، خود به خود عملیات نفوذ را متوقف می‌کند.
گوگل اعلام کرده هیچ آسیبی به این شرکت‌ها وارد نشده است
✅
منبع
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7786" target="_blank">📅 09:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7785">
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
