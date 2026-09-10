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
<img src="https://cdn1.telesco.pe/file/tapQR63Rw-mPTjwrC-ZAVAQqLszxhv9N8zQO_qrXFd8P_pKCCMRzPAjqCzsREwKOF4z7jMhl-72DwBllgoksBoJXjWpVDpaLTAq1LP5AV5OcbUQUK0a4Tp8vkYQXIiPyu3KU96x_jv0hZXnF_uMJpziXekQScOPm7fVNjbElZqegRxxkJ-ctOeklnLuqfO3vQvAkzHoOUrh7lcTe5de6CShMCQsoYxYfUjgUcGNcyz3qa2JQ6PoqqAbca5TygjPD79HoMoKh8Wvzouv6NuXsime7g0tElORVXuzwQl1-Eynm9CdwypQsbPAg2A9FwtUEiAHGqkTaxorT5fwLhO6_Fg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.4K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 15:05:25</div>
<hr>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QNFow7VZ9IrtkcNFnRr-HohuHh5uiA6-Cfb0Vr9ABRCa_iWWYEyYJW0LVLy1KhKvTcIfEW2hwHEA23U0G21SvQoKyoHcOYiL25Jq4wBZ2MkETwYfGcgIEo8n72Uo8R7x7SNs44PtFr3Gg3gOx_gxEFYSXrHWXR5sy5jpAczBIMqWJ-LypWvLvzI8GpsKmATxW20zPPB5YZMi5sRrGxRUNgWtIrbca8E8Uh3muzfuyKLyJ7sELeuyXU5iS1EM_O1MYazj4jg1zkhRwTPxO76I7cT2tgiWLTmI4_XQvuYcbMTuWq5LmiBTjQ-PC3L6WmcbP6wWwAw-a8f-q9Qiido4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رئیس‌جمهور گفته "۸۳ درصد رتبه‌های برتر کنکور در ایران مانده‌اند. این موضوع نشان می‌دهد بخش قابل توجهی از استعدادهای برتر کشور در داخل فعالیت می‌کنند".
البته نگفته ۸۸ روز اینترنت رو قطع کردیم، هزاران نفر رو در خیابون کشتیم و خیلی از همون‌هایی که کشته یا سرکوب شدن، از استعدادهای برتر همین کشور بودن.
نگفته راه خروج از کشور رو برای خیلی‌ها سخت‌تر و پرهزینه‌تر کردیم، عوارض خروج گذاشتیم، ارزش ریال رو در برابر دلار به پایین‌ترین سطح ممکن رسوندیم و انقدر محدودیت‌های مختلف ایجاد کردیم که بخش قابل توجهی از آدم‌ها اصلاً امکان رفتن پیدا نکنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JFvqQ-q8SD1v-znwHi4A85ZiA-eaqXOJQ6w4KnET9dWvQjDMBD4umrAl4KQKxfC1w9jT1c6lW6leQpwTPdqYpKit53rVpPun-JevG5L_HO6-mbQYt9_E-Foj-HdHInjRq9xJPSzHY0IV6r24rUD5udCUxcalxZblHf0XHp3SjyMOyTCmYST00lDK2VJ8H1usHhhE1vRNNo1aQIJzXd1ocEoueGrxdDrMBHjqfqdJK58XOPoIo-Els9cxuoh8JsYX_jtz-dPLEla6QwRXcEqS9WseoEkjhWRkwwCF_fwPfvzG4VC3o-ldyQ3WdbOOQZGbaDuQgKjyEQrN4XeI0JLcjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اسم JumpJump قبلاً چندین بار در گزارش‌ها بعنوان یک اپ ناامن و مشکوک مطرح شده بود. بنابراین اگر از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/scqKTLDdTD5rXk1zXxiuvgWBnNnc6HW-TM9lFYSd6hII7CVk1HU7fhFVu0UsXxws958g7bPIygnBhfO_aLW1gEhCbcofT7MMa8iKWTsxdoxv7WtdjGBcF0cX60YO73p4KFVP1SsC6gJE0F606nXSyVFkKT_knqXq9WqTHtSHxwh3byNVZ1ea8n8cB5guu6cDyr4a8xQk0r7P1pSHQQY2RIm2IZB_Bsm1bmsyOIlr8O_Yjut58YsS_uYOlUwAWJEGFq_0b7ibk2e2vpKtLOhK8TD-bebQ4LRshnFnYaDdlxLLNY8qFviWFS4SaBNSL_f0GUsL7EiFwCB0cXib2GOxbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y_sVI3EzGiN0kFbc_TwzMoquz13r1PSxl1b02MW-UoAdFBYoNuuJA0XpeMvTvSsRGv4pRaASKxtiVEHHWyHGNl46t-e2bvpVbje5zEDuIdVC62y-mwgpQaGKSeRv60YYJ3LzPfKWYmBfP4iSJfnKJDCyo99n8bCITA0e0TVs9osmC2FkF8S2DpPguKcF6zTRpbOA56pcRpml_JIaEkToQwQKuxFzvlwIyoJTDteMOiF68ZAnR9Zh58ZngsaTTGQ2lUEik2_hfNAbBcKZ44V3utZvEpdflflmZXtqAthmajrEeojjPlcrgxXNNvIAWunUA8-Of_P5dkvQAaF8iEr77Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از مدت‌ها وقفه، بالاخره فیلترشکن Oblivion به مسیر توسعه برگشت.
در این نسخه که برای اندروید منتشر شده، هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
👉
play.google.com/store/apps/details?id=org.bepass.oblivion
💡
github.com/bepass-org/oblivion/releases/latest
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XirKbP5Su3LwceUBfQC6YO740vL_sVfcWUYs_kQ3saPI506yaTmp3OOkrsFoJIIGchUWnJZxXVOzfZ1-VJV6fbeCCr781AslSR5OiFC2QVt6IwbyPMmmTbU28cS2mOGUyPWmWCz7nl5pVrVjx5fJa_vM4vArI9u7WHXi9zHjHWdbQcl4nhS00q3hcPeoWo624L30m0T805vfxvyezoXUGILZ_sPJ2lp8g8ULxqQMIrI4CgC9F2a1ajAMigGt1X_o8C1-iey2CvtqCai2ZO-Upr-d5Zk9mGC_5-YV0ZHM7DjArQ3OasthMXzuR8gWm-SGGnY2DAUH3FcLeM8mixmE3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل یک آسیب‌پذیری روز صفر با شناسه CVE-2026-85046 را در موتور V8 کروم تأیید کرده و هشدار داده که هکرها از آن در حملات واقعی سوءاستفاده می‌کنند.
این نقص ممکن است با هدایت کاربر به یک صفحه آلوده فعال شود و مهاجمان را قادر به اجرای کد مخرب، سرقت اطلاعات یا از کار انداختن مرورگر کند.
لازم است پس از به‌روزرسانی، مرورگر را حتماً دوباره راه‌اندازی کنید.
/فیلتربان
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ILs1kB9hZavBb3pXxB_N27SuwKkqemlHictn1vMRqtQavKsPPQcmmFs-IFThQV3yDCtCrQDzXpdcyczHWiZ_WNI1FcEgHbtZNA4VrjbnBXeiV6EA7U_P9fl8b1ZawLumkRnCupI0Fvldxv4cCUv7xNgQA0C6l8ucKIEo9Va95epZTgiwh9PQSf9bUNQaJ4C3UsvlhZCTWQecEKf1G-WYTC03p9eYhBufD7ffaI4QgWE3IsNYxPnYNp47N-KH-AcaAes21jzg-LV1LLjUlmgauyLV43LJk-1z_PJiWP8JOHAg5ZB39X-M_CpXCxH93z1X_UeycRQTmFtKJJ3YFtTImg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیفیکس اعلام کرده که این فیلترشکن توسط تیم امنیت
پس‌کوچه
مورد ممیزی امنیتی قرار گرفته و تیم توسعه درحال بررسی نتایج و کار روی چندین بروزرسانی کوچک و بزرگه، تا در کنار حفظ عملکرد و تجربه کاربری، کیفیت و امنیت برنامه رو بیشتر بهبود بده.
این تیم گفته ممیزی‌های مستقل و همکاری بین تیم‌های امنیت و توسعه، یکی از بهترین راه‌ها برای ساختن نرم‌افزارهای امن‌تر و قابل‌اعتمادتره. هدف این فرآیند، شناسایی و برطرف کردن مشکلات پیش از سوءاستفاده احتمالیه و انتشار خبر این ممیزی هم بخشی از شفافیتی محسوب میشه که به‌گفته دیفیکس، کاربرانش در چین، روسیه، ایران و ... که با فیلترینگ دست‌وپنجه نرم می‌کنن، باید ازش مطلع باشن.
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jqtY7yi_rZBTnpM_cIb6BCdDshWZ-aeDkh8Pn0TTj9Jvn_tL0M3ivED5E9KlL_JP6GnxVKi5-m_ELndKyE7Ggq0L8m84xYsU6OWXRLR0_-fJqNuhNoK5OUahA4h8f5MPxbL1voINnivhBRuWOteYaXGHJhdOyP_mBflVxjfadwpvF0VShowPwSfDlGNaaHe-LvbjIRd3rcJYxFPFK179zwAwcHh4Vd2l3xxYr9_EnsUDZvpPDAto8DwiAw5DnMhcAorKc6qHXA5rWM5owr8rcGDQ-puPVUzbGegwb87F1xnIvc8SgrrQmPNSh7rqBS2IIJ4lwuRxiEcgVV0a9eft7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LkaZVjc7E9S65Zmlq9slfBaKCZulUV7D4q2fExLluu_4dfzWhtpvikK8lC4UCb8EpDLYIr4mbrX_CPVYrBzwLF-3PoX5-b7GQCDoiSD_oAVZ9rZSL7jpG3uUgFm74AJhw9NNqYRN_vTmOG16YOxLXFjv1DAi7lrLsrfOaUmzUw_c48v37vIBtvD_Hn2rnbUFII7WC03kU7hYeiqp6u-iieXunlZCk5wwJZ6gKB7_7dMHXk-c5bJv1b4TGJ_cXquDpsfiEzTUedNgyBVByoBPDuVOD5dDeAqovJbSk6QSe5i6Xnb7i60bLIZTEcWz7kSbik-2K6971kJNy5Na8ucGHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سم جدید
😃
☠️
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oKdylahADu236OMvshDfuoEcain_uPVbtAYREiAuyp2yICyR8_dnDTE7L8pPYut3i9BrykQWHQUKtMejbZpBtDjXG6u6j3IcNAEBphUNRRFYNt5z_Q7rsJRSfzOB_im48QLZ1FwWjU-BlxldE8bIvSQ8ZUlOrl9rbfVcgY0xMlUSidPI9_qI28quuhWd-0PCU7O38jvPMEGN7xlAbG3CxhaIhCf5r1-2r_LMz8Ts-myK3EuPhJ7YlfTFWJHOahQm7XTXmVrOudBgYKr9YHo4_8gt5_Vw4cpVjBFKvnNmydU0g0W5JTgEUGJMBWvmGYDiyMHcV_9cELm8iFkCW5DGtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات معتقده "قیمت
#ملانت
به اندازه سایر کالاها گرون نشده" و احتمالا باید بیشتر از این دستشون رو توی جیب ملت فرو کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P2cguGzuqbsF1Jx0HluWuErQ7CQ7NteXgxIHesgmWtnzDjKv1ZHrzeGZUQMxxPNbYlmBjkzB8-7lg3X0h7Ae3YWV0DraoL7NHiPwyp_iCi1yduHPVAOREKpj4BbjgmR9Qh-MfUyBmVdh9IQQXOypVvVAFRpdXDwJ4I1Ac7ZM2daaFES4YMqHAmA8z3QpX53Qck_-gHzQLnhBGSk-_WrhiWHDUUKXAIlxCqdRZ9C9rxmyrYmj8DO0nd49FuAH5_dfRQ4CZLzjjkrR1a4AofEJXLQPqOStyGyrF_PIYTXlu1wq1In30MsditzollGwZrVuxvWwGHtNXo4vraJ5DI3CdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد امنیت تیم پس‌کوچه در ماه‌های اخیر حرکت حمایتی قشنگی‌رو شروع کرده و اپ‌های VPN متن‌باز (که در ایران مورد استقبال قرار گرفتن) رو تحت ممیزی امنیتی قرار میده.
طبق آماری که دارم گزارش این ممیزی‌ها تا الان بصورت محرمانه برای ۷ فرد یا تیم توسعه فرستاده شده. اکثر این اپ‌ها درحال کار روی بروزرسانی‌های جدیدشون هستن و بیشتر از نصفشون آپدیت‌های کوچک و بزرگ داشتن.
این‌قضیه تقریبا برای توسعه‌دهنده‌ها و جامعه‌ی هدف برد-برد هست. اون فیلترشکن‌هایی هم که نسبت به مشکلات گزارش‌شده بی‌اعتنا باشن، به مرور از چرخه اطلاع‌رسانی و توصیه به افراد کنار گذاشته میشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SSPnSYq1NU1UygZfoanfOVq7nUhYS6BoDaiRRD5KbupuK4XT20osmlG-JjrA3m-dBDL6zDTV3GZT7SK9oAg4EW5JBYYDPpDvKiJ0iOX2L_mwjhWVhTS_Mm80ITPjxhgyOpdvAfIt1SJfM_CH2GMsS9qqQTCAFBvhfDLs-BC6lBBgI7_SAClrQ5FTdC--pXhwo3tcL5LHJBR8SB30B3CuO0mp3OZhg7w6g9fFGflx7GRiW4LuqQJrQ99EEYjhGskDInTQ_UrYHF5w5dJZGIDj0qFlB45pvRvqp7caWRKsJthziPyGfBu9OiAvPy-szORocd9QQ_8cSeUCK3ZG6lhYLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ig5zjKgaNrkUGsGG0YJh-OxuTEtGUxGKrvIW9CjUU8KLNUGNfwsEHTU4bKo7-MZb8CYMS34LMF0OSQ0fnuMoQOY6ZSetrQl4DmFDPiKcQkGWuUJpb64OmgZZA2lUSbSOIsOPnhNRkmNXWLxY2C3iHOJ9D1PA3We59uBgvUilBFMl45rPLy6XVIMEG-SzB6ICwCLOgwNSKuw5-ezNt9fb2jgtDBpSJXu_YOSfQgOHGWAtEKhJTJLyHrAm7I0hVUw6i9bWCJvAmAh3IiOpa-DdloMhvkD5Jc_UEHtn8jSMYt1-FqIbtvSH5zOt2lWxQg-LOg-AnjpLynAvYIo63wMB8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OyfGUixlJxyXnrPAiJZKSDS4kdlohzHPAc0p4yRwO6QUfZyY-3gRk1LGYIdw2PsTvl6E4oR3qsm2MBNg8ynX7KqfzcgWou0z2zLhNnwxvR0od8r1V9UtjNMUSdVyIS7PTZKDgofRQZLptBhVips52ORUIhL4Q2Ek_ZyZmjbr6O9XJvCsXgkHwm8Xn6DExCc-yd5NUJ9c9Jj8zIh3Op_Uj5xtzVHNxEOcG1YrBVSt-BIs8q5SbqOiA9yYEFdEI6tqfCeDyo79e8F-37mLimYB8Lnk3HQeHQTDchWKJu1__F_AO_XmGgFmdS0FhiQOyf3UI5FXvENvKiGs9Hq3DCx4qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسپین یه ابزار رایگان و متن‌باز برای ویندوز، مک، لینوکس و رزبری‌پای هست، که دستگاهتون رو به یک هات‌اسپات مجهز به VPN تبدیل می‌کنه تا بتونین فیلترشکن رو با همه دستگاه‌های خونه به اشتراک بذارین.
کافیه لینک VLESS، VMess، Trojan، Shadowsocks یا Hysteria2 خودتون رو وارد کنید، تا ترافیک دستگاه‌هایی که به Wifi کاسپین وصل میشن، از تانل Xray رد بشه؛ بدون اینکه لازم باشه روی تک‌تک دستگاه‌ها VPN یا پروکسی نصب کنین. درضمن اگه تانل قطع بشه، کاسپین دسترسی اینترنت دستگاه‌های متصل رو قطع می‌کنه.
👉
github.com/Iman/caspian/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jabOhcOlOzQFAt_usMkUySwlZ0rFGTRC9KmroTT0VuHLf7Bf5AgDa6ZP30R6LECEZzgFBKmP4L9faDS2oYsFXGGX6fkS7JCW8VNBFHrv5sOjJ_fSJ26IC9knyJHGes8Ftu7LpjnYn16oKylvrXyL4WANV7ltYqYIXGP-qplhuaCpIyE7ngCAK3lOB6hgVgbgHtU_4ljH6zb7pn8KPoW0vT2WQeBt5MZPIOw4aKTdcWRud0f57EWtdNSluOKkulT_8yW9L-fhcxCJR-9eMeDtFnZKqzXU9dpitnL86S6MjB52F3fvGgLyVWIx1PGS3w7LJAmejPkezqH9h4v7RnbodA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Misga یک پیامک‌خوان متن‌باز و رایگان برای اندروید هست، که به شما اجازه میده پیامک‌های اسپم، تبلیغاتی و کلاهبرداری رو بصورت دلخواه فیلتر و مدیریت کنین.
این برنامه چند فیلتر داخلی برای اسپم‌ها و کلاهبرداری‌های رایج داره که می‌تونید نگهشون دارید، تغییر بدید یا کلاً حذف کنید و فیلترهای خودتون رو از صفر بسازید. با Filter Studio هم می‌تونید با Regex یا متن ساده، قانون‌های جدید تعریف کنین و حتی از هوش مصنوعی برای ساخت الگوی فیلتر کمک بگیرین.
👉
github.com/mirarr-app/Misga/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gGLR2bbGfgr5T7h8cCKfut9EGAnluapaCpyPR3okyUaMVs3fpUs3yzaN524sJSqxQoK4dQu0ndO15no5_iZv_688kaYThxbHIgXaCAcLhvfU2et6CXg2rkbTPI0T38VTf5ABH7oorAre6Y1iCA0M_ovj8VkkzoKr_UjaB8h0C8CB65MkvVmRSZpY2bwIANRmgNgdyBaD5MXZ37WkMPk5ZAc0wI_r4WR7XS8yfl8NBv4DU5XonXnZyPMphdZ0rNyEZZacJSKuA604HvZS59xZ3X-AeIrQoclK8ovHxIda5sQ3nIly3zOfVnlu1hIEwft_RebRCzoKOg_dbeMjBGbVzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند آسیب‌پذیری بحرانی در RouterOS پیدا شده که بعضی از اونها در قالب زنجیره‌ای به اسم MikroTrick در حملات واقعی هم مورد سوءاستفاده قرار گرفتن و می‌تونن در شرایطی دسترسی کامل به روتر بدن.
از طرفی Shadowserver در اسکن اخیرش بیش از ۱۲۲ هزار MikroTik با SSH باز روی اینترنت پیدا کرده که حدود ۳ هزار موردش مربوط به ایرانه. این عدد لزوماً به معنی آسیب‌پذیر بودن همه این دستگاه‌ها نیست، ولی نشون میده تعداد قابل‌توجهی از روترها مستقیماً از اینترنت قابل دسترسیه.
اگه MikroTik دارید، حتماً RouterOS رو هرچه سریع‌تر آپدیت کنید و بعدش لاگ‌ها، یوزرها، Scriptها و سرویس‌های ناشناس رو بررسی کنین. SSH و WebFig هم بهتره مستقیماً روی اینترنت باز نباشن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cVB-giZtFsKIoDt4LaBvaMohk8eOni6sXfyarzU2q0xcnmC0zJ9L0ekU9hdz8sjaeYBlcIdi7ePiq2vsTFF-WEohnvTw1-lPD5F-7eaLHevuPVrr_rUkaEm7eIXZppdnMkInGF4nIWKDD6grxr_sYXSXF2Mp9N_SRTZOXoxug_HNDMbWo6QmZroGE0AGqeT0dq8hmOwKKlWf7wbSuMAfi36fv_xfg2dgtw7Jle4N0-8JxlTbjBNHB67SRi-vqAcI_cESGFsX-adu1h0j34Y6w18iQAsnR_B3aU5ANd23zDQ5Hb2_2GQow0u7rUekwf1byKZGMNuayTwSVVPwfMxMEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه یکی از زیردامنه‌های gov[.]ir به افراد دارای مدرک فوق‌دیپلم یا پایین‌تر اجازه ورود نمیده و حتما باید لیسانس داشته باشین
😁
©
SePeHr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BOvJkxihYiPMuV3rBbMz_gE8PG-87zCX8sxwvXciLh1k2WS2MMCjvxhZ4zvfORpq7uQmHSvVETTtihYuxf05pbZQx2Oaufh6BLFV1hPP4tqm3qFk2zLTyYDjeZ04pet5U8X9vrjoJXQKW1ETnw-dbz_z-R9RLtAxl84PCGtEB-3Cf-va-t8nu4EZrlMrTqWpWTTqa3kkN680G3TIzxAGQ87szwcvXdPDkexp6Ix-cvvMGHs8oZUDRknMXGLR8mUXirpWP66ujtpyRYB6negRYBChQUIWUdTzNYPR_IIlTJR14_WPowOYqtoGmm9dKFv-Y3BTTdVnqt_EDaw00e7qHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن متن‌باز و رایگان دیفیکس اطلاع‌رسانی کرده که امکان تغییر زبان رو در گزینه Diagnostics & Experiments مربوط به بخش "ترجیحات" این‌برنامه قرار داده و حالا کاربرانی که به چینی، روسی و فارسی صحبت می‌کنن، می‌تونن DefyxVPN رو به زبان مورد نظرشون تغییر بدن.
البته این‌بروزرسانی بصورت آزمایشی از طریق گیت‌هاب در دسترسه و بزودی از طریق استور هم در دسترس قرار می‌گیره.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ایسنا خبر داده که
#قوه_عاقله
بخشنامه مربوط به "ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها" رو لغو کرد.
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنترها است.
در این طرح شماره موبایل + شماره ملی + آیپی به هم وصل می‌شوند و بدون ثبت آیپی در سامانه شاهکار، دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qczFj8qwemKX_47xmSE-7247npo7FLm3cJ8Rlznt2uZmB9tQJ8XSuGM6gsz847fFl6OFEmhF_MBaLh_o1d_O03-7DfKiluOz_w77wGmHUmwBdjhGhI_M6nSv9W788czoPK8SGEIQmoSGQzgv1csFfBvogasDSseJ7p50-hB-jK1TgVv9mp41lk8egqN4YVYsW5U-5P-81DvxrEX-yU4Fi38Lvx5t_ib04AIbQA9j-KxOADzvHRQabr_MNoZly0syn3kHqfsLiLCEq62tb1Zb7c_yW6n-ODkAzM6AQxgYt4Lj6Br-XzD5IkOTlszI_ns9A9gIQsHQH5uNfa4_-8cieQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether با تمرکز روی بهبود سرعت و عملکرد منتشر شده و مهمترین تغییر، فیکس شدن مشکل سرعت MASQUE روی HTTP/2 هست، که حالا با اصلاح پنجره Flow Control، مسیر ارسال، فریم‌بندی پکت‌ها و MTU داخلی، باید در شرایط مختلف عملکرد بهتری داشته باشه.
از طرف دیگه، محدودیتی که بخاطر بافر دریافت TCP در Netstack روی همه ترنسپورت‌ها وجود داشت برطرف شده و این بافر حالا بزرگتره. ضمن اینکه می‌تونین مقدار بافر دریافت و ارسال رو بصورت دستی تنظیم کنین. البته برای WARP-in-WARP چندین دستور جدید هم اضافه شده، که اجازه میده اندپوینت‌های مختلف رو بصورت دستی مشخص کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NMF3AZAhZzr-Tmxoj726GsEYqeAvDGND9tO2LVHQ09zejFQ2DfamwGGlULdoEAJVcbs9J6Rd7Eq3d_7IxB1EwgtYRpkOOIJfleJ_xE7bKIjS9cFxa2QOvfRI72PDOFXMjswE-10x7qT-ToTikus_P_RIOUJGYQNp5W0YelY5WO1adgqedDJCb5LGCB1IrWNc5G_3M0g1y-kQsC1oQO00MNfRmJyPJC0OV1oNwomHjnzQ_3LpXbaZKC2qKitrDFAhxdJV7mlT8TvQ9TGhiTJyw5XXOls8qTMTv1A89waReuXmtHhxozEsqNvRnvBBSTdIMmGzdNTI8-9y1ABk3SOyNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jb9XDCn67mWhOOpWmH0eI1K-9oviOmBRzImUqnnsH0tXxS4VKNyWPUnBc-31_bmw-pU-TGfhQxy4qtBkdDOnubm1m4AW-jVM5Q1kFdsyb1vKzgqoHHypltjW7DNhMmJiCwd8ZJPPEcne9OwfCB8uNI6MfoubKv3Vgae3rzjX9yNVSEbvZHA1SV7qM863sQcOcMX6Y1DWCQjwBFRxJOSD4JarITFd73LLNXfencXI91eOrwazq4AUpxzO_B96F_KcLAHFvcU5XZGj3opFgTiCV4x-CYqLuoi5gnicDfl7uklHKGPaJJmS3TI_fNWuVd7QU_QHF1ymX70_ncZ4sEzqKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه باگ توی واتس‌اپ اندروید پیدا شده که روی بعضی گوشی‌ها می‌تونه اجازه بده بدون باز کردن قفل گوشی، به گالری و عکس‌های شخصی دسترسی پیدا بشه. این کار نه هک پیچیده‌ای میخواد و نه دانش فنی؛ فقط فرد باید گوشی رو در اختیار داشته باشه.
ماجرا از طریق تماس ویدیویی واتس‌اپ و گزینه‌های Meta AI انجام میشه و روی گوشی‌هایی مثل Pixel 6 Pro و Oppo K13 جواب داده، اما مثلاً Galaxy S25 Ultra جلوی این دسترسی رو می‌گیره.
©
notebookcheck
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">معاون سیاسی دفتر رئیس‌جمهور گفته "پزشکیان معتقده دوره محدودیت و فیلترینگ گذشته و اینترنت طبقاتی و فروش فیلترشکن به هیچ وجه قابل قبول نیست".
حالا حدس بزنین رئیس‌جمهور و رئیس شورای عالی فضای مجازی کیه؟
جواب درسته؛ مسعود پزشکیان
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IM38kmWeRUUrR1l5FxFaCrCTkljKKZ-A_pe19jI2MC01tVE9F2V-XuRNlH-qgBfRbuJeEylzqEPMlCt9q9LdZ9hxiAuaQ3C8RHcgEyEbOCJzKdqsSbBwOycD5gIaBYidfNCXBUMXBE5wmOf6P7v67pUGuN9doT05QzaS5j6jijscabb-gyP7M2fhciC7HHc1-SLAYkdk5ow5bSIMhOXmWhbMStC6QZs3Q24Tyfzv7NwbaxT6pAeuvC3VhtWf9HcJKDqV3JdvJeiCMBzU2Wxc-D3cy5NSr4x5WYIlM5Kc8dGWVRgNoBez1u4H_lEl2QI_UPnwdZGaHHcqG0572UO_Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Echoes یه ابزار متن‌باز و رایگان برای کارهای شبکه و توسعه هست، که چندین ابزار کاربردی رو یکجا در اختیارمون میذاره. از جمله امکاناتش میشه به پینگ، اسکن پورت، اتصال SSH به سرورها، بررسی اطلاعات DNS، WHOIS و IP/GeoIP، ارسال درخواست‌های HTTP و مدیریت DNSهای کلودفلر اشاره کرد. همچنین امکان بررسی وضعیت سرورها از نقاط مختلف دنیا و مانیتور کردن آپ‌تایم اونهارو داره.
👉
github.com/SinaXhpm/Echoes/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q9x0cShKmmJnAeKZQxmQreJm5fV898d4mpRwpv09vS1rd8NvBPmR3uZM8jbdnFFIwzxdG5ARtRL_g1UcyAiXwCIkuKDEH14MvrfYsOhGMVkeACIIZH2jN6G00xMhAIUpAYCBJG9qjzKaqC8PjZh_ZKkC7FGrL4bQtsEZRXABk-QYgp9s8uZpgccmL-_n-_kpY8tmzr6v7nUUtapsCI9ypur3fFhNL1yfVB291J22_ysgq5VWNONQXbWwsh4ECR5PZuGSCKCbv2vV0b7h_PzxzGknHJvnLTwPGnku3kkPbd2d7ecxSB4NcHTyd2csaWe4FHqcoge5fA2Saq9rSQyv4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بانک مهر ایران!
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sExhXUQGc3Avll0PFLBlPzXvY9-Tqe3Un_BiR46NxfOedOxZ8bWvaFxRiJZXhGLyEO1gRME8p3lUgVHtqvRlmlVLsQRRlm8i9G1GbHwz6NBaZOy6a3r8WsKVmnqEbwzG5bXHkdN9_9Rkbd9A1R-JC6KJBe5Ozztrft6V1qXMP-xDLCxwf-bhdwCKwmo2-qqKqzQ26dmHj2U_RpEOtH4wFp5_n7njltl1sndo-aQIgHLmpGk6oODbTBUhuyV0SxqbF2cXFcUQjfvy-Uyb-xyUuwU7xPYh3WamTS6LdV9ZKQdPnmfShzkP8b94IgOc_vOLXc8dm0dQfZ6O8Fqw891hyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که بانک مسکن داره، ستودنیه!
کاربران پیش از نصب نسخه اپلیکیشن همراه بانک لازم است، ابتدا هش نسخه دانلود شده از سایت بانک یا سایر منابع را با استفاده از الگوریتم استاندارد MD5 به یکی از طرق معمول محاسبه نموده و مقدار بدست آمده را با هش زیر، مقایسه و در صورت یکسان بودن مقادیر از اصالت و یکپارچگی نسخه دانلود شده، اطمینان حاصل و سپس نسبت به نصب نسخه اقدام نمایند.
©
alirazzazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jnvdi8c8q9Io_6GQrXsRv9hd3BB0LtuWER7xaqcDuNnMmiw2B4pEVzNAeUeUlLFKp3gCLckxiKkG9VxvOth8lC7MejVNk30RU1n4qxgCzI6aMiqW09vqfJzPflHgdCjgoKGo7BHScGB6Dfp-SrU-y4OsUY7pivAkQImUWf_hFcr635fsp-zcLlMjZKveLvLUhrcCKHTQGgujgn3oEtOHE4wHHOg9LNtczO_Nvz0U_fXXnv6UULf0P1rTxRSWyNnF9G4znc5Mjg8d9yi8l9VC0pe_krkdX87O0Nqj3HOTzVC8N13Puynw6Xf0opPXlckOhejH1AW0vwA3W90c1v9Dsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دستور پیگیری فوری
#ترافیک‌خواری
اپراتورها به کجا رسید؟
چندبرابر پول اینترنت میدیم، چندبرابر هزینه VPN میشه؛ تهشم آشغال‌نت تحویل می‌گیریم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ozb7bCmxcSGNU7-Gbs7L3eoDzUlnsnCNzTfBrfj2SOs_HzGU8N9PZCADJwuB04fUuxoRsKX5IJpBNMD3HY3aMSXNMcr5y7d1RgQq7dVZG_koQxOLJeyb7jcQSkekfn-74cprSenJRd9FR2XV6q1xFbMsLoMchwBwyq4H9CVsE3yOkukMiKxIgX0Zv6zSEVgB9fTQkeZ8Q0-wwRkSxUrLGTQwC7tIYuGt9jZrLoR2ArWs9m-6yTvwncGCJSoZzzsPJtGgF2SkPGYA9lJZm_hWipswm8HYQmpZ9v1Fq15LuKz1ObN2d4y9YU2Bhwqod0k7gTnhNmk6YxH_K3PU7gXz6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پانتگنوس یه ابزار متن‌باز و رایگانه که برای پژوهش و بررسی‌های امنیتی روی فایل‌های کانفیگ VPN و پروکسی ساخته شده. این ابزار بصورت خط فرمان و نسخه تحت وب در دسترسه و می‌تونه فایل‌های رمزنگاری‌شده با فرمت‌های اختصاصی بعضی کلاینت‌های اندروید و دسکتاپ رو بررسی و اطلاعات قابل خوندن مثل مشخصات سرور و تنظیمات کانفیگ رو از داخلشون استخراج کنه.
ابزار Pantegnos از فرمت‌های مختلفی مثل SlipNet، HTTP Injector، DarkTunnel، NapsternetV، NetMod و Happ Proxy پشتیبانی می‌کنه و برای تحلیل و بررسی کانفیگ‌هایی که توسط بعضی کانال‌ها و منابع مشکوک منتشر میشن، می‌تونه مفید باشه.
👉
github.com/FrontierTM/Pantegnos/releases
💡
frontiertm.github.io/Pantegnos
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uHyY_ajBHzcGcPz6eKv9l1OP4eEQGBn_AktUiFbw65ceBHsC1RLfA03gRsue4cx6OluKT4r-Ck2zUtgxucikTdp46YnXWdsbBy-qIZj56p2twdI-Xpsjf9mffWEBlAZ8Y68UjfK8RQOA1SVJhld9al4KChmx8YJ94wuETaUjgyKn-Abi5NCUZA4Gtw_ye4AeJ94m8-QzHovcSRjmcFbFUy8leMP83NBa-JH4ykhJ8UzMZYZAoz6wDWjHFXbAl-JLn4vAeyMBtjoNdTZ3pgwpvTfWQdV8Msp3bgOursQreCz1qDoRSq6iXhH0SV0RR00e38zO6yCE1NdBuzFrZfuAyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/knrDNqrcHH-N8Q_1uuFXAzSBcyrqZgOSfufvAMWaLPxG1REAqFMFK-bJQ6dY0FiGHkj2_IeLiIhfppkcWg-arnOJrROIGSiPwBAo1muIxfDulD_shRcLmu9qyyc53Kxmy-y4CYsEFZOB1yoPsDEZrYWzJKUsOWE8zp1tREs2Or4TiJ2O-L7-DLw8kT-WNJfSCfCC4tRNStzuR7PDLYZtTPB6N02GCVy_Iff9KOIAHMLV1SObo6fTxzr5n6oI2MkL3WAv7-mnNOySdgG2N6p7NUSfu7xCL0tB2jQrcSZSr-C-39-9r6b790pqn_I56aYnADMpu-9Xo5wc89TDNnuagA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NjmYorThwAFvd3IEGXdWQw00FJxsVG4CnfAcEmnu-BOBAdxWiPcGqjusFnRzQ7epqSQCkv3u6bkvSV-UhAadxdd-ziBzEs2mKbJGf5Jv5ZWvFoXdCn5w-2Es0i1OafuyYBe5nk_QYOeH1KqMFsicX_eptp_px_OzQvexVrIl4Qn-eHytBhI02kiUhELwp5eJL7gXNeLO42ugFULJiGXzbx5Kliu33HiMN1TNIGlcrjM3zK-Y2_SjM6Rw5GpQovk_QNFWTNXPDZGVRRxyBurqA_eWkdT463l-7Px6VK2-bsscrdCRNKlojGThy3ugsDlwDwwJcsPk-rYFbyXfhlx8mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d367oR7vytiC2RVu-eV8QdqbE01wlnFAH3193wP185-ay2Aucy7Zofg-rM-cBhLxVnHBSbCoxjP6qLq2XyO_r5GrsEc22WkT_VJMQmAzUA7X2h6jQ0C2iSKTnxsjbY3uLZs0LleIXF7QhIqAN_oySfiFHO2q7uiUCh5zgla26knY_TxBVny-dm0r-ejpWHlK4Jnq9BSvc8a4jVwRQ-wmGBAk4h8WKwsFVs1ZOfz709zt6aI4nq7h8qFR-z4wbU2jg6eAVlbGg77lrBMRvKFdN8iAImWO2LQGyAvzj429fu8VjEQI7kymT6QUfZ9V4tZ7PRDVBelofUM24tfoBWP9wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sdnhpbZSkTOlqaa1rahKHLh0xBCdagzdcJNIzckyXXqHQIHaDr7FVXk0oPjuh7r2Kk_1hnaKUjGhAFkDeGgYmeS9HDqzJKHwmDTPOuuGUmS96igCoIztx2YLrMDX-aaokOagfAh-P_gNuONA-PPZ2R1kSJjjmY2ZnVy69KgoUhVjvGS8J8hIogm4MVTFASdPDHTm64nsnxJpgAEhIL0wr1wUIxNk4o-EKqgkEhpUsfxNXzKCOsQFnrBNzzlq3NvLZf9h-9Yg7q9OkeeVQWXXMlpkbKcoD02VpZNcSCwbWsfvNNM7EKETCm07PQc5fqpFueZrx--4DWRf4qXAkzl5DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f9vb71EH5tNLDbwKSozlu5wXOVqIH_yt7DGi_dKVfW95lY0fHmJE2GlEqTmzeo-yIIkZz1-MknB9nbFFN2Jt5BQBusgafE6O5FB9szzY6ae6aMuoHKiqgZ2IFuAyNi4-KXnPDokk3G8Av1D5hUyxk28D-1Qi4MGoc2ffzv-AGuBKI3oMcbXP3OO9lTCCER5SpYueg_e7_gDEDR6yruxldns_bfAy9upiYKzgxeMu83MfNDe2pr1cet7QTI4Eh-GYIUq_b98-IpBtll_jkg2L1Wz1hPw1BcbNzWvJoAvFTlrsKNKZ5CzTxAx25Ry5azbNdumF3AQSZLF6uqJnhFn8Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fd4FBUqcnCKWVgbX7WTHUyTdOzWgBj8qwebRai-uisK39K5nQAHDoD2nXR9fBeuW11GaOvkWxnOSCQYD8HuIE-Zg88-iEkLSxnirbfwrQAkBpYxcxNcH06dYpOuRVPTd6sZVrf3yQoK4pnCO2NLjisv2bQm3sbmyhYduJlZh9LvHeNaMVyzpuPVq48g9Wz8mZtnaM6J_ZZDlX1wLVT05lnAdyaAfDgmK4Lfu7alKA7-aHFPuD8eHwMNxX_Nzq8ciseIp9WItseeO1o1nIhtEp3unvB5q3plpFCbnyb4BKSVFacAj0ooURH8AJPHxYYCr3VLKsUnDwsereOnIDFYrfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VIt8NntMOEvHCauDua5wj_Am-bVBgyeM7PaA_SIrI83HyrBMHuGDB5e9RA0SfhoZD9NjNtn26d6CpbEnXBDY620GoIc0tRxFroShgHMRtJekFe3WxJpfZnqW5YFtn7Jy2sJVUJVffWa9Y0BQbKQFF2fXdv0__DG6S5WZ7Ft-SoAwyQo4fr60xG_Kss-JOavzzbkHv4ys5IN1q1NTKLBqZZjvmQ5o9bnCG4F1J-ibi8Qvxs1o8i_NSvT3IAm4tYoY_M-YqGqer6ZsMl2lwpklnZzFIm6SuemyrXstColp_ue5powa1d5JD21Ls8MpkAvDlT20gYgAuylnkD_U4XE4Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FKIz6r2JQyFTOIG0b-pV5IAGmom2Y3GloaEWmC65F34vDn5tK1b4sxHBGC4erHQQ-q7UWC5VxrbOZM6--PjX4cgg5gXNfOVWFzG1g0ohQ5DN4yJxM4av2s7HlwEvjmqTxWxEPRPwDlEDGMa8XHDinm0n_G6q_C9m7N0xuJf7VgRWyqmsZ_GE8-gxj_hmpmHcY-cXNC0ggapTrd90jPZ4eKjVGnbeHGI4bsW4K7Ce5mSF-fu8INdAlR0mTWtD8xm3gzNJCMTzzfJ0kPsZ4dmbZLvns-88H8Y36nx61LvZybHwn8gmUFYdcThQTSAHlCvzKeS7v6GKn2-6FilRPr0CEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=mKSoOAvzic7ZZdvVSWntLa4huCM3IUOp3sGhRwJXbN5UvLVm05Vh9_IkbAxFMeXfQEss5ldgpMwLH-9U8C64XeVbqwTKDRT3dtTEsw1vfWqrxNkMSWyH3Zu56ESwvk6XCdkdgMenkWe6AsYY6mnanyDKhLX0o3JwXF9SDkVQA5aKAywL0Zg0_AfbVdge6Tq3qRB1ghbSG1jLP7RzD3sJFjh9dcG2B_AqORQShHJn_GUkAMpnBi163gkequpYoreQtJ_m4aSK0fnGqSmfc_dSgutSdadPH_sLgIZpoAylfeCbbXcn0QdBPhrz92rrqUAA-OxMclg9TMYuFgpESL4wdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=mKSoOAvzic7ZZdvVSWntLa4huCM3IUOp3sGhRwJXbN5UvLVm05Vh9_IkbAxFMeXfQEss5ldgpMwLH-9U8C64XeVbqwTKDRT3dtTEsw1vfWqrxNkMSWyH3Zu56ESwvk6XCdkdgMenkWe6AsYY6mnanyDKhLX0o3JwXF9SDkVQA5aKAywL0Zg0_AfbVdge6Tq3qRB1ghbSG1jLP7RzD3sJFjh9dcG2B_AqORQShHJn_GUkAMpnBi163gkequpYoreQtJ_m4aSK0fnGqSmfc_dSgutSdadPH_sLgIZpoAylfeCbbXcn0QdBPhrz92rrqUAA-OxMclg9TMYuFgpESL4wdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cgBtgGfh-nnuTlOFPZzKECGk88MDT-h5uWoVEX5HNfJuCEY4te9-lqmBn-YIW1zm1szPUWzeiM8zcraLmyObH8_uiEropm87KKdOAqlrhvPC52upnm6ofyvAgq0FvRV7d43FvAhPGdXJcQktbBo_xQyglDXoxycfrMId6ryjjIUTtYjT0svsGQrX-E2kHDVN78N7TzGIISTMihOJPmrTAbE3ho5LNykMQbrYNvj7g6xcs32FWmLK-MOAuymauBNtr12NJq4Y49aOHENALGE2pZqBR40VUyDrfl5ci1Cm4LzdlmRdxvJKg63lFFH2GEo_wS6lOuxc-DRN5MEvfUX_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PYlPb3jvABZvWPmgbWc92_6a8myn1v9b-J0vYjuJX5FQvVQpAnxXeI3qdf1oVmkE3qw9MJljNI54HSDsLDW9uyeDj73dvxqiNWEV-Is-7hvUvtaGv53hmHV07-h0_Wj3H492Qg8aRNEwr5o2wSBLRyEVk8wYl1cS1yogQ0VCxkKv6fDRB9mJk5DEX612-3M7lIFir6iTPzV410LSpVPPqiwqUFPLMpzHcBGbuD3Tb9xwEErH2Gkd_xyqpQRnX5bRCvXYGKtOiCx4242jZqPthSqmXbrjQq4CgLta85j6RFkLHL2x8W4uaMrwDtzkjaSy9v9bfqBq1cBnBECCer9mTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y1roAEceCH4wjWx27-fqJrKYvyJ05j686_xCqBVXUaQhfjpz9I2L6NpKV9AAeQu6OR93-JRQReuc6JzAG-9VlGK6QsIln4k5483t-IRi25dXSCGCXEMSqiYcyyuBUEPPngjHbSeYZCbn7byceCzG63J8roMv7UZb-W53SBBaqR3dpuVFcWFAfMZSGhT_cyaIXNCejNRITnYmGwsuPWQyFWrJhEoArAE1Ebfa_aTINsDd_cdhTEOBhmkWh-TZXljsewZOJ_iB9sDqO3uK6Ns337IDXz2faMi8CznWp_ufPHhWQUn8EQ93v3AvsrEODQRb3EkUELzgjSJWGYTKSHE77g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GOjk9d7-FzHMyNXWvXrS1WsNEmbGv9Yd9DSvVc5k5k12bvSil1o9FmbTdzq60tD6EzCekAgfWdhhyNnG21nPqrU2WHGFVa7HjGtP45GDUL7sxVtKOo5OHEeCs_K7T75lLMFrtK4VYFALbYYJX6i4mCmLPMsWeONExPUEkf6FMJ78hPjGApiPGHH1iSKWbNq5J5MzqIYjPGp8w_KVy8Qd183OGgCbApIhH7jxPt7l-TX230ie4BTro_T36R1XWo5OTPjYUlGv804ci24SdnV8E0cSHYqRfgW5QkPUZsT8jdrwOLFrRpFpX_KQwHq6182Nt_mywUKmR6RmVl_OBTtcgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BxMStQs0JgHSStcr4Usoo061LYRQ2kcf3WWqiE0BxC2TmsaKavJXjWS69lpT0Bq0QNe5ZA1pHEn45R_LY4IUS37Oi_HIjX-NeowuDKZv09Gl67evBa3monTKFevKhVajAcJeHSSx897OBNoc-umemTV87y3b1OuQ6-mytLB_MbXxDAWeixG8MSZaxZXQVzvH5R8gDRmiQLHqnYX3Kheck1DHT4gJbt9NeSJMvabvpUtPO5eIVkMQDC3RH4AiZI9_Zy4_HEix9HnYyVAXfvwRROIksOqbtXIUQt9BatAX37XZgKsQPozIzQLKX9TT1xdxo3w_WV8GrLTHk8dLzcapvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dg2u22nGMOrWjj0IiYd0X3lsgd1Qhzsv-_rk6jQMfH4LTizfihG6OIw34ujonkcE2_ELFvE6b3Or4RyLxgGIcZUhTRELEoogml73IYhXov9D5h4gSKSUYTO_AeHZItO_xtHdnW_M94EsXeC21tL-QdfXbjLE8Z7PBsqoBGTRAD--cYKKn5W3Ca8CJhoo87l8M8YeCzPXqwm4jvfZmxSdAwnRVPvJ15damtlPv44v_JAQASpaTXgjwrEy1cdLEDhCY1f1_IrQFB3S__6bTLJDYte_kzIA8wgnWQ6G-xZErcoO4ciTeTghLIuiyS0FIxXrXhHmPHQKPV44jY3r6hmgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AvKM-g5rK6TcoUG3FFnvYorfSyYXL-U4aQWNuauMVN_5h4IA7fm11KY3_ODy3GKq_nHMqIllQWKbQnqcgBM_OsPD3HZLaLB_p7aWo2f3YNYgK1q4f4PLjV7gFWeYl636wypgoc_mTBLZyqX02uPtVGwZHArUX2PEL9V5bSwYgnJ5UNRnV8KWLUUcdtx_gMpIa13Y-7-6Deg9bhG9u5kAKstrN-tCQP6sJSnlf6i44_q8tmWhSOc8TKW6T1A3aAS0GeA8pqwY7l7F4067uVlu5Fm91-dRHwznItz3UBPMq3L_NlAV_Y7MO_JbKykkXqAWfMoBQ4YhnZqvo5L4Pzx95w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hK5WZ1GP4ZiPSFzNhMn9ZYKnKA6LBzAM1y7jyA_YQh_BWhuHrjF-v49K_NHAzmen2L8cwo52BE6EilVD-z8pcC4YfqoaUs1ijHG0K7KMlTlxH1Png-of_Vrty3LO80_INPN2xcuUONiVCH3dvCm4tT3EGgDt4Zi4X6iDkyYeky2Lh3eLw4HYAadhDBKNcG_E4eSjUIA6NwGo7XQohQpc6DN82i1NCRrWoTw7v1Zk0tPSJEax6CIiHjEMcMmqlUGiOTWVWlnU7au3wxyO0W6IRBKQ2V9zsrNWiNkQg4Ydt9kjBfJmxWpFpnDmNfUGCNB9Yah49C2RLq2SEToxqarZ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vMynFDWQ9lsE_2qVIeveurX7EajoE_PhodGADOnX6Jw28LEgah2iF3b0z1FVBvc9nB7XV7RimH3Jerzqose6IsBf7NCBCBrn-qnAOpvMv3C99oKHXdFk2Z_aHX12vrJZtk8yVkpe1_ZBfQr3h8LTOp49n4AZ36LcOfMw9iwLopx8wRSkBcrjj12N_8nc6gVmswNN-W9JHcmqB_wtTPMhxcma4TaEr1xYLXQgz9vvXF5YWhKWSYfr3kstjzdTE_rA__skIpzjgxIurr78k-OwOrnhfdPluhTe7sUd2f9GnYO_QQsH31jRn9r2ytDLIXBwUgbUawdjaXZwCSA-js_R-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MSJoaSr9GPmorWCypYV5ntegHIWqLoQ1H1_n3FQ9A5N-haTke5Faqjzs5hlSM7mmZXzYNq80wgetWyGtZyaPyxB5LNM8xlqVBTuVKRo2cj6HL1FXoxiDj-EqwKOhYJd5XAh2nF-BBkyt_4-KqIraRfboBwRHfX3kXf3ua6wHXViSnA_HhAvy6TVphBweEFbMoeAWA5DnsB2yECK-GE0YqM0PrxokhX4yluPkY-8f4IKxMKVYn7I5N1w1Tnxo9CNd_8EexJ6BAo0ha85fx4oQHkZbWNvTwViWuY1aUY-JDhzVAZaPDDsPAQokug9gr3bCMuYuxQnlVa7aBwxUGMwYqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pgvgy6Gi8lIUXRgoKShzpma9tgDdoap9GA9LzPi2PhFDL_reIpE5vgHrgqHnFFT6plIAEB0RnzHxj1satfC61QpWnCpZkYpky6g8VGUNpsrtvZMnNv2KBYubO5bnUmLOhrxcaQ8u29srau_jIkAzuM0Pqh--C8S8rQyZFpJQ6Y1TqXYaNkP8yVdrbXEvizJXdTT1hfJBwUMl3GsV-alhnMt170bR_fM6UVmgV7YY3RxSaTRw7DVnSX5RenrNS0-o42ZCk1JOj0H5aajzm4qH9zg5gguGlQ7F4YvNw-87wVoFPM04pQ27_1nLFW03_4PyqxPaazV6qPlX4-4L0xf4pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AQ1H5vOd01I_l6MT3m2p4A3R9mde0EqW41TCDvtNQE0d29ZwkLFSHHgY_NkzawdGcOEYSwTjZ7H3wJP0iKrBuVSB3c81dBL6eDyRTBGbpMdpoYXzOD7RhozXR9z_n-4IzFsum1ho9MneJwIAYNFflZjS1N4q3X-jkpXK0d5BlZ1qDEbXJmoImHc2E9uTZLkZNq1VUh_REN73MSJ_Gq72EmLVTzs23sonprtnwd6EV2WI2HC13Nd7WV6d2UE2W9fvbms2ffgzTLG991-rIJSxdPEuYFe1YqHu0XJNCZkQfhNiVyWLYscPrW2rymlXg5tUuFcoiVwQvp9MXYH6SK0hqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/llWJ8Ve7yMD-LZWnam3tXlYovCD4ADJErl3kzrgeCJ_mkx5pjvtUspmDJveFKl7dKygRFp-qzprVSiuzKbtMAooV8T2jVtsv5057wt6fjh50hp4gW5fhYxBgaJoe0vMRczpVnsJZbpSw2gxiuhmcvBo1x2P0l9sp7X2aJInUIo_Duz4yOJ_jpKOurMhw0UovcHNGe4n3L9vd9W8UZ732yLZgEJWmYPedTHrbh6bWMcZxkefuXd3XP3BlDuegO1BGGRyMP965ItVXA3g_SAWA-j-ws_a1YlMSn29VjsZ-x6N74QkZKiu17UPWD8tqX6vWtlb8UA9fKAWJ2mtg0JjlZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HoIakiUwrhSe0KhD-A_z8n72pOOkqBkR5Uf9PcoH_XyqJjPzo3OZ7_s6AQCUcRD_wUwflgJFibpaNIEdU1WvNwBHvRfA1rAuBn89Xn4rK0N2d_udegpsxV3aujHh5Z6IA0daLq6H0jgWoVSREoAxF5cYDY4NU5C-ZW240J9dnu74dc4bFOFVxHp9tkjLK2pAXCzj596piwqkDXC2uJWL87Is_17QfpZ4zMtbcKl65sHhc8gpUtuTEF1BAzHQFE97chUBjIIbl2sNs3izacT-cdam5jaizm23HSPctPj2t2-jAPitCvScDiVw29ROy-GTmScMiTg5Pj60s352-ZVu4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/igR4Ov-hYThdrF7bYf64uW5xfhclR_AiGGm3QP9GajosLvmiGC0GUouXIkz4DxUiEVdkILN5FvCkqRDkNbz-1rfdCQ7gRF70D3y8_kvZHcSiv9w6IKrYwEQ9bCSF8WhoZNdVxzPk66OGdvTOsshdNI4f-98vwyiuKC5N1OUxCXDlvdySGIaUKPSff173tshKxepPqbiX2-iiJ1Tsn8A62V-ATYIW5foses83gG_nt8SYHJMgRdYFu7L7_4hC1-ivm84C7MvJ-x5dNFLxh3n8_TI569xJfRe10YRDqboDY_MFThVQ9IzN4U_Ro5swAIJHbcpw3fQW2BKI885J4F9uKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tjkeattqK88WW3rwIJp_9D6lrb92R9R-AxYKPSGpeWYKEnvLC27Pxgyu2q_4-7EpAlkc-0KnD7HKyBB4Jp0VTjftaK8RbBCkZzBFe_g9eVz_LA4uirlzaxrX0Oyz4R-YINh_Kl9EaQ_wKQxklT35-wybdi2oML5UY0N3gxKOVm7RJCBra7BR9bqvcdSKTEGSgTp5abUgShcE87MoTvGD-3M6uaa2lt6e-tvl3ihT_1OKuGYjyQAku7b7uLErPR1ZvkT0xcwAPbS36Xd3TL7oqwgcfy8iA0Mq94A19iPXdthsYF391noJZFvDOXy6fEB5Tm2jztWJHss7bossTr_HlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HMKC6prMNJd2eh-XXb4_yEfc36Hk642iX1i_uuYkvczfV5UVWEWfeozKcv0dA8cwauHXkiC2zAgMadKve6bQrigkDaj3ajV4Igm-BVI9cmVLG8lMphL8gk8nPRtSGQUI7qyQPTO79fuRGrImIdmxmAVgUmtBzl1MltWWPgojL_kV6tW4JZQtBWvR6r2CoAcUBa_DQaspmSidLzG3F2_UDIhhJB8wa5Yy1A8bPGSA_WsGEVpfJcg98BKi7BB6kuT-emIckVL2Tl1F2C57whhU7zmjYx8pw60Ui8BFUc-typPagjyz9ohvTuzouVk_5mEA6B4Zp-r_7uNlWUGxbDZlXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CLa9VfvZwk7X_68WahsxBcyVyDtWAke2Uw-ZbsUi9tcjp44Uavvgs8MLHIErPzJUamjT8bXCUZw-kQlpqtPYp07_VTRpYH5jhlMTEL-XKuWFqJIxVxOAEXgXA5duCM3E63SGAae64n8HKKmmJ7a4O542W7UtaTSVYsnz23ARteGJu6Q9lHxYbpwpqSIAr8HbhcU0c2H-aGlNi-bDTtZvfUIAhE54iJJ0bY4MUBPpuLnkUndbY0cAn3KzIDLW9jTaZWEVh1cd8p3jsfLB42LaP7eT3QOFPRM1I-NoZarzewMHRY2cJp1xlb-NyLpzFUZL7NcvIskQUMveKt_gpHJHbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F-gHdP7UJH-yooo5JpQy1Wx1YEH0MeWLqTAd-IypXVHO_rNTRTCHPKgKpHBD83ehe_ijSh8sywrZ_xmsgwqSEV1O232u9P_PfBcRTWUrVTG_KpewDfrgVgWU16gvYPrEXB5f3E0dHSSCx1YxbEObrhQfQ2bQOX8y77qqqfA0UNg4Ko6-K697-LD700VZ7wjxYtrSmjP6jWTch1Obdg6LN0GQhh1Mz-f7ZPRtu82E7NKJF9qyE5eK1FH8ZqW2bxXu2g_QPVtFv4G7BVYj24-QNXcki1r0KqBkIHAVQbYo0VVeD9Apu_3PbExeC7fOW7FJjH6yxIPZ7oZtZnlsFDZc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P7euj3LO26Bq_uQIdXEDX1SL7FyIEkAXRCagT8So91QHw1tnbtKEKv5-6MEP1N6BnOn7hcwCTBGKZzg6X1wDK5KbkjtTos7QRnPMZLj3zIJ8oX0JM485v-bXaP2qMD5TZ5yjyQ2j9Gs4AFMWMy61UjL2RGwYYO_hEoJxfvCdVXdJLnJGDMwW4-gMhfdTfZHpIoWMA0JsEt2DzbgdlV4ul0GBUDRyEmJqsiESQrrjA5VjmohHK3xBMP-bkAEHmfsOysyUtWK0bo9tEAP6EUCGNHUW2hygYYYyNcuxdnVxXKfttdkzu3gN1EtCpV5VIQo0ONMbmvm7luxlT0de1PMW_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hQ08CBIHoSooq8pwK0F4xQ1Vsaqgo-JwHLn6xQ9MaM5QTpQ8xn9bMfc6DIj4GapLzCLx69QLSqOhG9cKAtKO8aIgAab8OReCezNjsbSWLuYJ8gGojRI9MMCbOLGBVObmG0eiSj7lPlagyADY9rzZdqxFLrqCIEBs5KQkZ6sWOpam70RdW_PLPtwVssne8Otq_tPTHQbXtLDt415MG2-X0P-t-BwLTnguDhKnmcijTjyD1CFM869Yu7L292SToUrS0eHm0jrtt-qYyBV5g6XeqHfLjQoMK6flUF6uXXaFLX5aGU3jKDCGaNwZZsAhWF_419a827CgcnvTJDW29FN9Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZB0Rh5NQzxP9isKTxFDtKyXoZ3vo-R61eFsidTaDP5nlBkTJsfb-Ze5Fro35nO22WcjWhIduZzhG4xdM-XE8mSe-IKpr7WzLl9FwRzY0KNpZOerQ_gSrdAW4tKqQSx2FRJu3toeuLQR22Jh6KNSx-pMzgzPUgIYD6ihgqR59mdPYjG_z2w-tLI6iNKCq3XUPAxcWXd0Y7b5TNryFbOfQf4iUq7tGXUWKsXox_stOrHK_thPiJiE8Lv4KBgg6dyQS4wdqbAFz9abI4xrXGbAK7Yc2V3EPr6vWINtYOGleSwit4FfRlYODunuJ23XvG6bqcYb1tmwqC5GlNVCIjqse9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KjCiljbfc0Fn0slyw5jAdMpKacmzl9iDCRH1KReQyhxmPKYOZwWMi8Ec1aZLsBxhAnzBPg6gKMkC0EL0XZe_6Opaj2uxWWM8gITWDMZ2s7Ztq92iN5A770bw9Fl0pPZq9lqvdxMwYe7JiHa-GZYeWerdHM4GKT9JZH5yLtknQBZMug0uh-6ETyisCgHCqQPNM743NbQ7C0k2QZbxTH9JYEsfpL0on5YYlZtzHl000Xi8A_fE0tzSJbhSTrZHzZRLIJAhHoAE_cSafC_ZuRip0wjSGCCS3v7cEmUujX4x4WhMCH0FgvlyogXfiEOwO8noZ6XUmrx-DmBtPvvwrZzzuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vp8PAGTjPWN7N7xYqhjPCVa357W1p0HHioKRlkoNyAD9WWV4J11U4aFGAhIetC_rYlH30xboH0n2lwBc37_31idWU4RVIVLQzGXQVEBMGFwOEXjZkOBe0P91lKdN3anPygA5gvzQP9zvR4_rB0h-25ClNc9-vdsV8TDwV3obkdh1LZGyHORk1H7-rva73cMlf4tGfVU4myNVWVjaVVsRWkwaDN0cuagFROusrBSewGI7JLdD1wicTqLkLMKdzLG960bdnjKcZi7pkZkiQOgubX18-aAUa1IWVuzghuN0hGcngroIG8_0uHRSVVp5GqQuT46VHje_uxD_yeXNck1sqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qFSvqVt8ZGygGczENU-nTAJU-c_UcV9dv2Nix3YkFB5_4RK_uvs4xi5Nxvk96O-v9jiVMPEBw-bbHpZ1GofWw0ff4sYPpOwmhYZbVPLBkfcw6Ffwuk1G_9T94LHdDjy2QwRWupf9BySFKkOMVg0l_CS--FflibnD2vfpxEbeSBKzixavc8sl5XjtZ9w2VehLbWLJgbDxPsuJDlyHclzctoeV9kLCgN-PFUQTtBVllwrKq2Y4zHp3h0fhTQBv4Gho1CR2eMkGMxT5hErtq2tZ9xywh6iV15f8YFwddaiyYilCnCtHIsHi9a_qC3sZTH0K2Tnr1JhY2sbU1g-7Uo_kUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k8NNDk-cM_4nBDmV0JwJKr-wGXRr8aPKp4-LD8Y0-II3GNt9byED4QqjbL-Iwy-HwEeicpxrpm_5okA16AImDkxReOauq-lwHCZMvSrhC6SMNg3LnluM1TgwOBHDYeLtUTP7VgkOk0y0uYIknC9WGImU39syErrFitQ5FpuUR6GrFFZ5QQUBLV_PCYYkYybrOgPxWTxmm_SnH0pqttPk3EMXkPYm_MxMl1ySYc59hjHNPfkTWOR6JrocZ-XZsDBxL5mGoDownw4kCFW8KTgL3Uk_ZAfMGRn5HmDaiZwtV2j_1SROc8yaARGUxTOdVVnhb6enZ7NmHFRBgSlsHqesZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k60fvp1UpNXoQJvxWw_SaIO18jJPj9hX_TVA9qBRk19Vm7b_kZrur_br-m0fZRDdfzXXElmnOFHu9-ANQi8bcz93Is60QK-tjXEFi7O9z-T0HYfnpChxkaRJ9TLNqad6Lanr07drYesSiQEqvLNi45vu9n_yc-B4LPTCXOYIlHBNM7iPcxQSBm1dKEa9k9YzSiA8yFYWrWUEtDD10iJvwgdLtrWARaq6-f_o8SMYYHIeTPoEIX9sSXMHP4zlkqvNiRR6rAuMGjfBEMfgE7diu57POspPaj_XFmZ7plclR8UrP-p545Oj89wBuKve8_WdeBNaylZas90sLxHQ-NMxEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XnQBm85Q8LrnRyTEYmTb-TR9-aOqeH6JuVL_Q8iAifyTiwc-We3C2VsFuiIwd4SKqwirFFBDTbxy-0YuABK_t8TCxFmcIOMv5wcekVK0hLqYvnNJeQpHqiT9v994PNR5y2oGkNgsApFw_w456s4gyVrz83YGPFQvup8j4-E5hbCIeJLYEvf6H3tsMOqngiVxeE8ulH4R3ewJuejIcQBQzCm96mlhF4L40AUvoeA_m1g8lbeGe5OvIZClDB-N_0p5qYeaIAIpiTiNZSEmMzK5PhEj3FbOCr4wEOwafklNcZz3RhFaKP1ahyai5OsM8IH5ilH3PstLWJCpaH1fvRF9ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Phbhc6fvp4UZ5tkHQEyKFtmYCAIkZCXa8O-bXDGkmoa0Bg7s4_ebAQryNCI6AVxTDq3G5PsflM5qfvqUFKaCT9lB-pDm4n9EIZAv92psBFZWaOg3Nbz2_GJaZP3ROz8BuX4igQPh9ZJ8sQc-6GQgBw-RDH4iXlq0ZqDsir1bD-tzaRA6ZQhOH821l-hNq9_13NX8VP4dRT4L3qsQLKUya9ZIofwGy-kq-W9JXupmj60bjTkqla1FB8H-pWbl4ei9DLPRZvk7B0ryT6op8Veqh05d5joz6Q3NAE7h-A--GfDKkQ-63N6ba2eP7sFXGpbnq9dCgXs5MrDYjj3ucZNLuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R_7WRgRhOxkZyqY4OZuTPo2y5GDiBoG80Fq_XR-Y84PxGxUT0QSLk9jmSYfGVhcADDemg8976Sernwj9ZKSxZEEnxet9FbX3CdLkPLNWQc5JO7iej8qQilNTngERWgACsyCdiPQNZggl42ThnsE3GZIcaE7jsmWQ3ExzCI_Wo54vn08NATE2bKh0DOJvXEEx1dlGfKYCrAfvl8klGf3-RuZoJxTrOxBbPrtFH9f-ooO7AQidESGf0og59QrVkKz0Zv58zuJ7jD3A0tSN_1RQEEt2Eaybyl1C3n9cNM3PAEh5qfPueruaAapzcFMxm9cIGU6VQdltsMRv1Hnh62-b0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W_m0mH79OzuAgqofcTtEdWtQ6nTbJvzSNv8o9qA-9woWxFHyrPHZJkcfeyJEj-5kfFmzh-bhxO3FOXAgtKZTPR1SrbQ3Tb72_zEVAFl0VpGVOBIf3y4ng2LRXJp4Uazjl1mCkb8Tqfojt1eiMNCxwZ9jgVz3V5As4vmlehKenL3sIhSImYJa9_gzwXDY3SdsPnKhfuUwZFrjnXXlKwrLWs4xcGQ-nd12yyOEMc-Ik-mlka4addDH_p4_ELD3ZNHNTdxvlFxZqmwWPNh-psNGUlm_PRILZimBF-g6XdfhYPQVkBC1bg8rgKzespNmeV6R-UwFDLlb_nvPSHeid3l5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PThhktkOw68b9pvhIAcWZYbP7qckaC8hkG0jgF8Gyvwe_AkTP0IdvfHiL22PU4yNT_4qd4Vrgf17IMdOdNPmo1DHRpX5b22VRerS0M_qDLABRQVxxYHCZV2pSNawgLMlco8t1Kl16cs1p3-NygS7rXljUbzUgHFnOt-R1RxSjKiR10WgIgo-E_Mp4i1Z5xSkcVl1vLi5bUSnD16BXDd_goWckI4UkOf2AwK2zO27zc9Cg_xUa7ZQaGkQoMiAz4UqP02O4_uH4_nivk6Bo2sSgNfjpmo70c-tvY4JKq1jlfIUFY51QDtlphxT8KFc-71jQ-f4Qtbgc4FdMKNYyEeAFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DgorTZIk6IjTsPhbteS_OrbY7C1ndHfFy_i7jO70Z4B2a5cYk5n7x3MPq8StEV4tZkUNeMlh2DNN4be_J-d7ahSl28ePobm06Ri1I9k1XWFyB-6YwN5xrlLXoepHr2_nvz3rIBySnriAoU-tcGBS65tfXZu58oRvIaMlgzMWrZDC7wZlW3m-FbMaLbEokQw6QoOq9p8C5Xz0YV3Fywx8m_u2DsFdTuYg-clyQoDmiZ8waYPJITKtuQQS1ZFFJSUgQ1WLc1yeOdd5e2FWDDoLF_NtlYFSIxqdcy8PFUkeJEW-geTmu7HXrcZVfG1x4cXra718Xnvx0Ly726d2d5n61g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gjltrfyVP1Q-5X29mVECoRFVfpiVfrIfuD_Cn2-vT3KW7Rv7RAW4nz0ymaaTP6VilgnviGg92N0f4S5YrmCPZExH93_21mTU1osCydY1kNOLF2Wpo5qdHpJwasV6EhdJU-knt-yb9kc9rM69jo8_q5QTTl9_QCSxEmIDvGuvDmT9j3o3JinV0Uss8VqLnR6ewsccg4Xnas8lb5b6Spyij-e26c2gtNsQ-NXeYAgq1oA5fd9wxldikSpW15KkwP-_LZSFhfPRudMkJZiR100qhfXZKZH8lDt3nmp1Fui9ilGsZ2oIR-ma7f0-GEMJg0ecnqQgveSJdn_ZtzoEFhhsnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hov6VEIj7-IOm8tePAdmJHvwXgYFsQl3Eswf0KSVPDCjcsQujfW2o9-slNDZYeZc3fcTWnVETgP2RxXhobk_oytkr3EJrMdy3EnaCXG5YJ5XqoET7mnfcKm3dmAvI1SXCd7tCv8REr-PFRgl1Lc196eLP92cxtZ1oA5xL9uYKTre0v-4bgv8SpEIqt1lxSskEP4exk7G93fygmuUbJkUGXYyCJY0gNRyBSg3SZljqrFiOSaqJ_tx6V9Ehjr1KrLPOK2LWo1LR_6kX3PNvtNfFqYNiap7h0aMVOPg0-b6Xq31gFLwKrJtPpTNZ7rK7PhxE8w3w6Lp3qsMtcTrsbPg5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kfev7smGKOfPow3bMODiUOr-t01GuGQ7byAJBBC4pSTkDTJ72nqK4xAsh3L9tcN_xupMNGSgjadnfNuZP_svN2DKu0NdMARhUL-uZUxs1rVzes4NVZYhaWPg_74wPtdK65JXY27ZMekYTyrQ5D4IIT3kh9DDnqI2aP-Bb0HruyrhuoaINVdI9Mea3hNjkAnM3qe8EpiB0k2zFpQQtlY06GNUPdeMBS-NE1sbJaYpcxEIQsctkaExqLd0FSig2dA2gB9ToOWBnjMQtzlUx7T_v0ZKUjUHKwd1y0xaElynu---ccZrmT-Ddgqq6OvncG1j9uU21Ra3-dAYhEE5KXz-2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ldd7EREi_MqZUes81Kn-22CqD_ukGTSuYxurtDX49BNHX5qaqe6yVBlEa47yZgM1_DZSmO6qmLZ6-PYhCzQjkt5o64HIu5syZkf5dyNcp44CSMx2xWvHEDUPHRBdrXGpfOyl3p2fxOdvAy39rSp6bLIDV7OuNTNrbC9aRiAYfRBrl-4OaxnGFfxHwytER1OlE2efsWSOmNRCEqNbF2Qi_4sqR8sidInpMtV05JDUhHmvDxul-5B6uB2C4jqN_uxqnJfWZ5_1DtrZIfKK3yJQ9cCL-SfPoKrIROjWxpoCN3SOO0aqfmY8eeeiGPvZVqnnJShGfIRfQ0RXyVJuTzQrUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/imZdHg2giinmIp8Kb4AeKug2jNl_1bz4Qykl3kMaLv_Tkx5moDWktbAPFWJUm5YTfRJRU075zBzL3ER1VuZTuCf5kqC6VskZN9jFyOp2vq8PWhdAc8E5fML7UhpETOvxQOzlGVscUzAYJtcoF5lfXX6RKHGNr6UYv8uE7fWkK_Xqpv1TKRV5Hx5LpVcqBuY_rQkSETlXeUx9vp8ttAx5DTQhMbrSV9aMKP2l6gw2IDqt9uISgYVOIetwS5ohxAkSLOnlKCW4vXS_lXt0mrnuF-ak-s5HjwE3rZp4KSiBTNBZV-FOADayE_I97020WlNF9tjD8JC01GSrB4iLZNPFSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pGlUC_IyjULvSF4WcPPYWFcb3Zi36CRf5kCW_aZg18isvj9hZUwfKdvtDDn6Qryrex06o_huu64L95iEtxHeDn-yy32-IhXTV0apOjRYFpW9TniegGItd4G24sm8riA-ohOxgoTH910C3H9omIROnWeCXiukw_tgSSY7or8jgQ6v7uWng56eyFFuROJZYUnUKHgAWq7VYgWs0CHHhwCNHqkr88iTEd4w52_UquzC1nN85NIeEy8UyRjszbovrJdeKm2R6UXb84xZsxv-cCv6Q2Tg9xnuJ2PYHBkLUWNoUThyQZpRq3feWifVQUn45TN9DqpQ92oJZhPT2rUG3wzyYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jQVtcRF3mmtuW4u0eOaEki5vOfRjPgVl37D6Fuh_x1jrULfciL89qI7xYGZH3U7f_uVPE22XtAQrv0pOt9CmBgFsfWmXOPhPdbGAzOVPA2GGzIpgcX0yx8R90g1SK5fDEKes9DZ6UmHmpxSOYe8rGDTavp0hHj2zYmdN51qZHzbtzCHZmSkKe5_5Cb3sS1D2hgGsg1kRwtlSlE0FMtGEF-esHG_trmA48jqtzB9oEhxD7PxdrT7dYtIeWpe1nShYKldLTvwF-jdH13oLV9Volo17kHF2Z_bjkppK2P6d9Y5ua6vEiIjD8Y2WBpIt4D5Zf448grtTa7dV6Oq1o97aLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
