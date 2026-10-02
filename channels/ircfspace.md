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
<img src="https://cdn1.telesco.pe/file/UnS_YtWfzG-BG7nodp-uJgDLBSTNXUwwGlsZmmBD4pis1par1S3mafgiJiwFsnYUFGxjcPdmEXPWX_JQ0IwaFBSXFmubtjbJMCKdXsXS6GfOxnDqVuq_EbO6zWAdhME1Yo_7KXNijwfKuf2tPhhoUwq0qxn_dn-gzs8-JzHzTgS1rEuOChOT4da8gjwk_Q9O3clPuQpvfTdn1KUghri-i9rg1Jji9b4EyL5wtTf0tRljCooVZvZonNFUuBdVf_lHLrDMxaGN-5dKu0EvPaF4Z7aKStwALy48QYyYKWbpE2nIjYZ2IZeRt7wLbuGwPD7YRs6QtaOO973nTIr9gB3cKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 95.8K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 12:14:42</div>
<hr>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dOcX9Erw7R8MxR7EU7DzlIb_lFfB8RmPuB5pbesK6G9VHpHTUALaIu2l62VCd72vugkZxcAXcD6cV_ma6vpJznDH_zpTgaPqHl9V7STflYNYNN5VsOyOGYbQtnWy48wQm3qXbQO7UghghIDetgECdj3mnXHtnwSROzexGWZaJyrFWA6lVd3iWyXmPig-cDh25gatkvPJgxRYS-SdhSNuxj-3aTSlR93RZC05c7GvJ26YQSCoznF8qh6qt3OvKN-IxApzPR4lTo_mnZPoITHNK62MxanfhOQ20JYU5_cqlvdcq3KX3LC1IrqnkmcfNp0LuEyoUR9njaNH-PgAIDOQNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه از TeamViewer استفاده می‌کنین، چند آسیب‌پذیری امنیتی با شدت بالا پیدا شده که در بعضی شرایط می‌تونه به مهاجم اجازه دسترسی غیرمجاز و حتی اجرای کد روی سیستم رو بده، که مهمترین مورد CVE-2026-92370 با امتیاز ۸.۸ هست.
فعلاً TeamViewer گفته شواهدی از سوءاستفاده فعال یا انتشار کد اکسپلویت عمومی برای این آسیب‌پذیری‌ها ندیده، اما در نسخه ۱۵.۸۲ این مشکلات رو برطرف کردن و لازمه آپدیت کنید.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DYrwEpX6hP9itjOI3Wj-3hcxsQ10sCNABHtNkK5L5PG7ovyJjme39urbq8G4kWaUYBECeEUWARpn3p7m9nwC4hwLmMpdHrOzXXcPlRsYq6LOx4e3r8fhczdXnAqd-LPt-ty8HTStDXy9nm3irurS5VgsdaB3zOOramy5uJsx2-eHgY35aTE3elKa22fn2V9dv7b9XO82bJQmWsHlKgwBmGhx05yeUxG-9I9jGQEHS_12dUyNlTD0MSiZyWJJ0WMj5Xoz8NvNZRz5mTBqwQGSjLbX2eJ-GbZV3eici32GKfZ176umml2Ay506m9ip9PasWfmNYLcE1c7RKEwjQX6cGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ج.ا در سال ۲۰۲۶ رسیده به راهکار ماه‌های پایانی حکومت قذافی در برخورد با مخالفان: قطع سراسری برق!
©
ArminSoleimany
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BnSG1PqbgelnEeoQvafsYYNSE-YaNWU28J269DWOKeQaaGlJE8LgusGIfIzoKAasv7qRYNn1VFqh5xskuoVmkPR4nJl1oBnk3Xx1yaSF1-j28ckV3BOexDvb7J2LCDwKDuWBT_OKA3__Os-jfbbTSFDeN17_PnsUOgaRPHUPedmmsh7OBgwbFE5xw_14dfhlXOY3QAQYU7SmSZAtE6S4K_bYb0KwwswRcbgCPvVuCHyhvWjBpG-k8wQTjiwDCdSfWVBgemQkzQrwg7htxNwCHzWuiwFiCHEeEPVvFqJ_8f545l8AFlseuuXOOEmwih-DGi98qFXb0YTnnS4mIl7ZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتیجه این و اون خبر چند وقت پیش در مورد تغییر شرایط استفاده letsencrypt می‌شه گواهی ریشه داخلی و پایان بازی. از مسائل فنی اجرایی صرف نظر کنیم، بحث‌های مهمی باقی است: «حریم شخصی» و «امنیت».
در کشوری که با مداخله در پیامک احراز هویت ۲ مرحله‌ای حساب کاربری مردم رو تصاحب می‌کنند و پاسخگویی هم در نبود قانون و ضمانت اجرایی نیست، امکان جعل گواهی برای شنود به خصوص برای موارد بدون SSL pin هست.
©
Hamed
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bHgWUft9qWchYJS-dT8sOw45LLiYht9ZoLOGfoTzV--nfckF-RtoNw8Tvy2D_Ok8XniqiiySDYytojB_9BZAypiKnskapLsRieVcJy0NU0wzCar6zjf4PBsSMDukEBMnFTI-2MAyrpZYVQaqRtyiMUaXPUjHfjmcN1dscEl4Q8UgRorahHjRh7svgROAuhx6VUqIwxo8jBgc1-QrDkv2gxHypOgn8TdcEq8VN5EUpHIyalqZjqC4TwxzOxC2PRF2qU4UpX_28tM28bZYy0VxvDph87ZXkJiLBIUh4fbaCq7rvyRSdAEyN7WCZsM1K55q_-Wgu7D2tri1wiDbTk7qaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهکارشون برای مدیریت قیمت تتر چی بود؟
نمودار قیمت رو غیرفعال کردن!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2629">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کاربران در چند روز اخیر قطعی، ایران‌اکسس شدن و اختلال مضاعفی رو در اینترنت تلفن‌همراه و ثابت گزارش کردن و میگن آشغال‌نت چندروزه که شدیدا اسهال گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QgnFVCEF8UIsRiMn42bvLIJVXN4A0k_hKDrDnUMStPX59ynMAukxeZlDZnNlAV6RPskp-gwFwst1syWF7Fd_S_LqYJz36Y4qRKLHTXhOeInpECih3NG-9ZakBYFO2Whvt6ASn6jSTtU8qtk9er7sNlTc7-7vyaUpuXKvl0JD7jOnFOop9HCtdl0IUhFwQkiTOJkokT66ZodVhQBX6RPISDbwRR4wkr80h4E06-73rB_wVGVxMUN5AgncAew00-SZ_4y2SpJS0Vg3eMDBnk0Unpy6_1AmJ4GT5DrVBxW-DS9KGr14g9L7P9IjAv-8ZNC1GgwQDZS6Ffar7FILeCM_OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Group-IB، یک بدافزار ویندوزی به اسم HEAVYGRAM شناسایی شده که از تلگرام بعنوان کانال ارتباطی و کنترل (C2) استفاده می‌کنه. این بدافزار از پاییز ۲۰۲۳ برای هدف گرفتن روزنامه‌نگارها، مخالفان و منتقدان جمهوری اسلامی استفاده شده و می‌تونه از راه دور روی سیستم قربانی دستور اجرا کنه، فایل و اطلاعات بدزده و حتی از صفحه‌نمایش اسکرین‌شات بگیره.
نکته جالبش اینه که مهاجم به‌جای سرور C2 معمولی، از بات‌ها، اکانت‌ها و گروه‌های تلگرام برای کنترل بدافزار و خارج کردن اطلاعات استفاده می‌کنه. Group-IB در گزارشش ۲۹ نمونه جدید از این بدافزار و ابزارهای مرتبطش پیدا کرده و با اطمینان متوسط این فعالیت رو به گروه حنظله نسبت داده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اتفاقات امروز و تصمیمات هوشمندانه‌ای که برای مدیریت اقتصادی کشور گرفته میشه، کله هممون رو خراب کرده احتمالا.
ساتوشی می‌تونست وایت‌پیپر بیت‌کوین رو خیلی کوتاه‌تر بنویسه: دست به دست هم دهیم و دستگاه چاپ پول رو در
ماتحت
بانک‌های مرکزی فرو کنیم.
حالا تقاضا رو سرکوب کن، حساب‌هارو ببند یا سلطان فلان و بیسار رو اعدام کن، این باتلاقیه که خودتون درست کردید، توش دست و پا می‌زنید و ازش خلاصی نیست. این وسط، عمر ما هم رفت سر ایدئولوژی شما.
©
GrizzlyBTCloverr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2626">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Eb6qtnbORO7tiFpWiTuxIa1otiLGmgbEodd2jxpu5EyZV45WxiWYLxt40RdT6vgoOWFm4b2pYM6mDuR6FoArFr3HDF_bwKFKQIk1txHuwOTL70L8fHVv58xPFLka7XpKeBdmzp2G7QnFUgZdwq_sMyVhfuOvYeMIEv2kXfP7iWzj0FpQ6Bjb9tpmhA1XkxsJqGgYN-KKQFvLW0D97ozoS211KatcI0cgh3zcXu0hMVyz_KDAwS1dIiwoouJk7xNSzQXysvlUvwhIGqTXN669EuF_9rZyxtUSv_Abv6GxqKDInyC3KEkl0NCzQ5_D1ldGAJ0Bh62FDPMMKbySariZ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از دیوار چنین پیامکی گرفتین، ازش بی‌تفاوت رد نشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L2imjP5H_cxgu4HhT0lowxvjREtGK2u2QvN1AQQfow-yBzaZrTeqRmKp9QtTVysekwihNc4QwjIjBykjx6X7bJJTzXDhB2gmwmq_SomkBmReMJZ3OegZC4Z4Jfr1Osqs3O9rL6b2DS4D0NQxB6zUvvyB8KGSXDxpobGXPSM9unDi0nxwqodSO_bgMC_bCX6NF9CPfUXm1Mkw7jKTg69BHNFLrFTm7bo2LA2E0GP1d5oeXtk83jjCCcmTzKERRLzW4HhFXDqXvRm2Pya5O9y-7Rv4yxszztr0UDtNC8jpLYHnI6vlDj192SdbLNj_gXl5HRxDRW1ZC9Q6XGtQvlGVkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرامه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مجموعه‌ای در حدود ۷۵۰ هزار رکورد از اطلاعات مرتبط با کاربران صرافی ارز دیجیتال والکس مربوط به سال‌های ۱۳۹۷ تا ۱۴۰۱، در فهرست فروشندگان بانک‌های اطلاعاتی غیرمجاز مشاهده شده.
این داده‌ها شامل اطلاعات هویتی مانند نام، نام خانوادگی، شماره ملی، تاریخ تولد، شماره تلفن، آدرس، ایمیل، اطلاعات مرتبط با احراز هویت و همچنین اطلاعات مالی از جمله شماره کارت بانکی، شماره شبا، اطلاعات صاحب حساب، آدرس و موجودی کیف‌پول‌های رمزارزی و سایر اطلاعات مرتبط با کاربران است.
افشای این اطلاعات می‌تواند زمینه‌ساز فیشینگ هدفمند، کلاهبرداری مالی، مهندسی اجتماعی و سوءاستفاده از اطلاعات هویتی و بانکی کاربران شود. به کاربران توصیه می‌شود در صورت فعال بودن کارت، برای تعویض آن اقدام کنند، نسبت به تماس‌ها، پیام‌ها و لینک‌های مشکوک هوشیار باشند و از ارائه اطلاعات شخصی خود به افراد ناشناس خودداری کنند.
©
leakfarsi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tf7bA0qQpCv8luCiLrN9tNXVB2IyRIF7pHRPTFA0JrcisyvYP3iSpzzgNxwuVJ5Q2PrrH9EfabTq7jiNS_a1iJzhUL5GrM-NefJMwVix0UgXjc1pidMLqxfeD0xFt6h0UrbJWG5Lh2nf3ja5VBWGtyLYL13MeR13JrR7PCH3h2Z5Y1HbVbXFVbE3ioTdO2aNpRqnNoa94BBWZa4gsT4yqcUKM_1UV8YUnvR8wvJT5jaBZ5DN62IOy8-xPmxcBuJkurM-_6mzTxXibI2HVEQCmW8CZ5XT_1nHyrcwPL3SNp7ALsCa3nu_VFCK_Fq7Ev9IKiGepiDPDtBbVxkVsbJ1FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر قطع‌ارتباطات گفته "فراگیری استارلینک میخ آخر را بر تابوت حکمرانی فضای مجازی می‌کوبد".
۸۸ روز اینترنت رو قطع کردین و نگران حکمرانی فضای مجازی هستین؟ بابت ده‌ها هزار خونی که ریخته شد، باید منتظر کوبیدن میخ آخر بر تابوت ج.ا باشین!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rSFaGJ7j5xTht9WzZvxc3Riln4MQst0XhvQgfkFsQbQFXg5DaFlMImfENtJ-oSmCTFiT6qt3AdcBred7jgbgh2TaGXaWdHU5CeSCLXLe62Z7Rv3VYA5GLXsd4eckp2xwHJkZ32B3VNSCt0JIaf3wm0_JThpeynZxAfGfgiloy8Iwy0ATGtYkA6Bu0fgOsHeEFWgGy6X3zqVq6hTXJckGHPzBNTeyPLU_PryrBqPe__B3lgWkNXlQ-vjIwN929zsqhsbrb61gSUy4MqlR1lrK99SXsUSJ-7AOeRtO-Lqh64mVf-6KPBDFM7BYTvAWGs9fRYDWshaE4vNY-4NyWZyMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی با ابلاغ یک بخشنامه‌ی رسمی، ارائه‌ی هرگونه تسهیلات بانکی برای خرید طلا، ارز و انواع رمزارز را بطور کامل ممنوع اعلام کرد.
این بخشنامه بر ممنوعیت مطلق پرداخت تسهیلات، چه بصورت مستقیم و چه غیرمستقیم، تأکید کرده و مقررات یادشده شامل پرداخت وام از طریق شعب بانکی یا بسترهای دیجیتال برای خرید طلا، ارزهای خارجی نظیر دلار، رمزارزها و همچنین فعالیت در سکوهای مبادلاتی مرتبط با دارایی‌های دیجیتال می‌شود. /تسنیم
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/of1Rt1WLhlCaT0JBs1KKYe-Yf97sICETeFUPafkfgMGTH5nLvjzVsOLgp0KUrZZOnTC55ZOyGLLnmU2vC8aLZIIeuMb2qXHPAwlg4QyPcg1eNIJBfjH66YTfOfSewl95SZYTKyUKYfKJ1-FvHel1Oe6tP7DjxtEmpC5nXMZcNhRAt4rIUpsntX8bZNS0U_I779nwO74g2L9hyN8XoExahqaeIlWAwsufQ-rf-bMofjPlnam5VS1QsAXmYwuspvqeeT0lDNlaqmUG-HkTFYmhnIgmT1QMx5MXd7YC3R38KAkEAtr5qROVKzXxmIO1dQv5P-XzDWLb_Aqu6vSgZ6A_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت تتر به تازگی اعلام کرد "به مسدودسازی نزدیک به ۵۵۰ میلیون دلار دارایی مرتبط با بانک مرکزی جمهوری اسلامی و شبکه‌های تحریم‌شده کمک کرده".
الانم با عبور دلار از ۲۵۵ هزار تومان، صرافی‌های رمزارز (با دستور مراجع) معاملات تتر رو از ساعت ۲۱ تا ۹ صبح روز بعد متوقف کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">هم خبر تحریم ساخت ایمیل برای ایرانی‌ها توسط گوگل قدیمیه، هم خبر مسدود کردن ۶۰ اکانت مرتبط با صداوسیما توسط گوگل.
فعلاً اون لجنی که توشیم هیچ تغییر جدیدی نکرده
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RysTGmzlMXGdc8dJmIv4r9wY3p90nH4seQA8amrJGgSCVpaY3gRkk05doUsSrfuT0QYLfGZoFW0fow0wlRszzNnf-6NSNPvmr_zM41FxSRldJDWDH9XZzE1OBKj7DHY_cC05ZdTgcDdGTonvKNlJKpZ_4dOAewLQJ4QcZgTtHrzzfTJAmhvsMN48Wd--q-IlwAIfSKX74vEK7E_24gZKiohsaTzGXQuH-Vqa_Q44Cz1JjmV2jRxCZpe5KJskgHvbu7Kj-LcTUqwDGlrt5PXHiOkhNgfTindu128S2CRS-97fB3Kgwg7D9MLMDT9mXfNFzp8rxawvs73sLBhTkaz-qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ sushTun یک کلاینت متن‌باز و رایگان برای هسته ایکس‌ری هست، که از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard پشتیبانی می‌کنه و تمام ترافیک سیستم رو از طریق تانل ایکس‌ری عبور میده.
یکی از بخش‌های کاربردی این‌برنامه که برای ویندوز، لینوکس و مک ارائه شده، مسیریابی هوشمنده؛ تا بتونین مشخص کنین ترافیک ایران، روسیه، چین، تبلیغات و دامنه‌ها یا IPهای دلخواه از تانل عبور نکنن. امکان تنظیم DNS، فرگمنت برای TLS، Multiplexing و چند قابلیت دیگه هم وجود داره. حالت کم‌مصرف هم اجازه میده ترافیک‌های پس‌زمینه سیستم مثل Telemetry و آپدیت‌ها مستقیماً به اینترنت وصل بشن و از پروکسی عبور نکنن.
👉
github.com/soroushdeimi/sushTun/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ePQlXmnyLORhf6Qwnl4UEW-CHIMsZ1twCFVha9YcoeUkc0ssqhNWcZrf1LlRr4DWQwF4sGxt_h9I7QdkoZTP1WH7AjmK8jrmcsYPAiNs57QPXF2iVkdS8tivdeyFcvhRctjcfuOvxf4IZvNOlqbEXS2FGvD7B47YR8d1iBZ8e1enbaW57GQD2mm70xtVmz--_j-WRKPRonIHdoMvdpYSKy62gsDGtatY29msV1xvzbAPr_qblUmYditziol9kvLODXO97xQM6BPE1LGo6fWQMJb4NWt1wn_LZYomR62s-T24MaPCKL2VHn4BYgY4QKQdcwX6dpJdEXZOY75XofmOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت Satelite یک اپ پروکسی متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که می‌تونه بین هسته‌‌های sing-box، Xray و mihomo سوییچ کنه.
از وارد کردن انواع سابسکریپشن و کانفیگ گرفته، تا Rule-based Routing، پراکسی‌چین، DNS هوشمند، System Proxy و TUN رو پوشش میده و یکی از قابلیت‌های جالبش، حالت Multi-Core هست که اجازه میده چند هسته همزمان کنار هم کار کنن؛ مثلاً سینگ‌باکس هسته اصلی باشه و بعضی پروتکل‌ها رو به ایکس‌ری یا mihomo بسپره.
انتخاب هوشمند نودها، تست تأخیر و IP خروجی، مدیریت DNS و Hosts، تشخیص اتوماتیک پروسه‌ها و اجرای دائمی در System Tray هم از دیگر امکاناتشه.
👉
github.com/zn0wii/satelite-proxy/releases
💡
github.com/zn0wii/satelite-one/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fAAorSg2X0PQiOEeoupczJJI3vOnZ3FKrp4DatfvtgdYs662_QeLfhLI8-GUXHthfP0iFgPcKUuwJUwY9uqv7tK6QJTFx3WpU7kfivxks-IxO2tEHfIEhCTY73UI9XyFQ4QPyJzpLvyLVXkDRrua8V8QbFqGGqLqyOq4vGtNp1CFqJZImunccDhNS7mpZ05Iez5VOXKM3vcl_7cFsdT0IkLyy4_kgeFjv9IJKZ2BmncsUgHVQdY3Vy77bV62Rrh2ehajV-YgZ__u2PzBxbwXu3ApXlJDpaQlFEUoF0QCRPKtfO1iiY7TSg4a8I5OzcMKoSQlfhF1VmzabcP7Va_olg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی فقط دسترسی به شبکه‌های اجتماعی را محدود نمی‌کند؛ محتوای حساب‌های شخصی را هم زیر کنترل می‌برد.
شماری از کاربران با انتشار پرچم حکومت نوشته‌اند که درباره فعالیت‌های «غیرمجاز» توجیه شده و تعهد داده‌اند در چارچوب قوانین جمهوری اسلامی فعالیت کنند. پیش‌تر، انتشار لوگوی پلیس فتا در صفحات اینفلوئنسرها و کسب‌وکارها نشانه توقیف یا محدودسازی آن‌ها بود. حالا انتشار این تعهدنامه‌ها، نگرانی از تبدیل حساب‌های شخصی به محل نمایش اطاعت را بیشتر می‌کند؛ جایی که مخاطب نمی‌داند آنچه می‌خواند، انتخاب صاحب حساب است یا حاصل فشار بر او.
©
filterbaan
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XswCuAizWceegPUUQPUTpuJfP4wHYlhSo-nE1dNyAqN-2LwH-hE-qdYoDSyd1Llm7II7QAm8iDIz3j-2BFBBjn8geoI47lR1MdDsX14G18ReipXiV4_QkosbLakXU636J1bWWQBoBlyhe5x0MVKvAe6Jgapa6-LDYDwxeUFy1l70KSQaDzhNCKQ7kT8V_OxzBjfQACJd7GPWJTv6UE1-iv6Fw7bPfKo8z56uL02xNh0NAGTLs_xiJ3waRltVq0R9nSoOhkr2snTHhrDk7hz440cBR1GDa1wAw5FaHS8F4X05gjBR56R_A75aR1HY-HaIW53t0jRtnmL2XSNjrs_Mqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Qrator Radar، شبکه همراه اول با شناسه AS197207 در ساعت ۱۳ روز ۲۹ شهریور، بطور ناگهانی ۱۹۰ پیشوند شبکه رو اعلام کرد که باعث ایجاد ۱۰٬۸۶۵ تداخل مسیریابی با ۱٬۵۲۴ شبکه در ۱۰۰ کشور شد.
این رخداد که بعنوان BGP Hijack ثبت شده، در ۲ مرحله اتفاق افتاد؛ مرحله اول حدود ۸ دقیقه و مرحله دوم حدود ۱۵ دقیقه طول کشید و حداکثر انتشار اون به ۱۰۰ درصد رسید.
وقوع BGP Hijack میتونه باعث قطع دسترسی، انحراف ترافیک، اختلال گسترده و در بعضی شرایط شنود یا دستکاری ارتباطات بشه!
البته در این‌مورد مشخص نیست که بصورت عمدی بوده، یا خطای فنی ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بانک مرکزی نصب «گواهی ریشه داخلی» روی دستگاه مشتریان را یکی از راه‌های ادامه خدمات بانکی مطرح کرده است!
اما مسئله فقط رفع هشدار اینترنت‌بانک نیست؛ اگر این اعتماد در سطح کل دستگاه ایجاد شود، می‌تواند فراتر از سایت بانک اثر بگذارد و در شرایط مشخص، زمینه رهگیری ارتباطات رمزگذاری‌شده را فراهم کند.
مرورگر زمانی گواهی یک سایت را معتبر می‌داند که زنجیره آن به یک مرجع ریشه مورد اعتماد برسد. اگر کاربر یک ریشه داخلی را به سیستم‌عامل اضافه کند، دستگاه ممکن است گواهی‌های دیگری را هم که همان مرجع صادر کرده معتبر بشناسد.
خطر زمانی ایجاد می‌شود که آن مرجع برای یک سایت گواهی جعلی صادر کند و مهاجم نیز بتواند در مسیر ترافیک قرار بگیرد. در چنین شرایطی، مرورگر می‌تواند بدون هشدار معمول به واسطه اعتماد کند و حمله «مرد میانی» امکان رمزگشایی ارتباط را فراهم کند.
نصب گواهی ریشه به‌تنهایی به معنای شنود نیست؛ مسئله اصلی دامنه اختیاری است که به آن مرجع داده می‌شود.
البته راه کم‌خطرتر وجود دارد؛ اپ بانک می‌تواند فقط برای سرویس‌ها و دامنه‌های خودش به یک مرجع داخلی اعتماد کند، بدون تغییر فهرست اعتماد کل دستگاه.
پرسش اصلی طرح بانک مرکزی همین است: برای حل اختلال خدمات بانکی، چرا باید اعتماد یک مرجع تازه احتمالا به ارتباطات خارج از بانک هم گسترش پیدا کند؟
©
raaznet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OjMxEElpVAn5653-HS_gT6Fp0GL3wA7Nz1J9j-mIRNfNMLIhNR44l8bJ4I9v6N341ymN1q48-ffF56ghIv0K9wY4upZi7hsMyCQEbeLtsVe5gAedxHZ6Fr7Jf4HKTfpZ1eqKIUYYH5PmG1m2RnvA5YKOYhNP1ViVj2Dsss8gU2gWGzP6yVR13PXMOeBk1fO2H770usUfHeIgt38C3lt1GNwaoa9MIlqP0QBpvfG1YH6bqr_6p_DUn8BZVhYnQGMavi7LIf8SX9g0-E5ZxCl2UYWGEJkyT8eRDA9ZkCZth8BME_lVYPtD-SfKYVKUc6o7qrOrPT9fZ4szaIpzDiLoJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراقب این نوع هک باشید!
یه صفحه جعلی شبیه Cloudflare میگه برای تأیید ربات نبودن، Win + R رو باز کن و Ctrl + V بزن.
چون شبیه تأییدیه‌های معمول کلودفلره، ممکنه طبق عادت انجامش بدید، اما در واقع دارید یه دستور مخرب رو اجرا می‌کنید.
©
milad_joodi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ofqu_gt5A_yckBx1oE8_ZKS53RYIB-L521wxoV-cLoNf4H9Xjz10fF7yPpOwP1gM0hfYh6Tr2PBQQJJJpfFgs5h-_DoC7wjx4XpeNudXo7VNC-WX80103LySmdRlc5TYShrMeb445Spw61jHy5gReEc4968ZF4PyH4l17qkXSeZ_r_kTFarm0YwHv8GEDotdkPiuaajZIaf1Ri9DYrKtxL07GCANq_qGfzmaU6FC5jGlea1luZILvM6PV6BMw0ELQe9KVXjIz7Tp_6uCp4Ff7RZAn2hJ_PRT7vI_B_7ZTG0pmdghpmpL2fP-8Jb-7-FpMl-RiG1aK3LmuSoFUV8bjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زپتون یه موتور شبکه‌ی جدید، متن‌باز و بدون وابستگیه که با Zig نوشته شده و برای کار با رابط‌های TUN طراحی شده. ایده‌اش اینه که ترافیکی رو که سیستم‌عامل وارد TUN می‌کنه، مدیریت کنه و اون رو به ارتباط‌های TCP، UDP و ICMP تبدیل کنه؛ بعد هم ترافیک رو مستقیم یا از طریق SOCKS5 در اختیار برنامه‌ی دیگه‌ای قرار بده.
پروژه Zeptun امکاناتی مثل پشتیبانی همزمان از IPv4 و IPv6، NAT، مدیریت DNS، مسیریابی خودکار، فوروارد ICMP و پردازش چندصفی TUN رو داره و برای Linux، Android، Windows، macOS، iOS و FreeBSD ساخته شده. طبق بنچمارکی که روی یک رانر گیت‌هاب گرفته شده، زپتون عملکرد بهتری نسبت به Sing-box، Hev و Tun2socks داشته.
این مدل هسته‌های مستقل، می‌تونه برای پروژه‌هایی که نمیخوان تمام شبکه و TUN خودشون رو به هسته‌هایی مثل سینگ‌باکس وابسته کنن جالب باشه؛ مخصوصاً با توجه به اینکه استفاده و توزیع کدهای پروژه‌های دیگه می‌تونه الزامات لایسنس و کپی‌رایت خودش رو برای توسعه‌دهندگان داشته باشه.
👉
github.com/Noisemux/zeptun
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KNk4o8H4OcPwoseve7615XwxsVcsTR-fg9cmGhvqogoUgVy9zHdcDG9FNog_alLHttxsuDb5c-3WBAFr027Z9FEsvdjd6r4otY8PxWVr3O7TN-Fl4gUYmltewPLA3N75PVCD5moMicruwHV5N_wuMbwazxOy7VGQFVcRLiKFhzVWvFgmVbmQB2xtKFTD22nhWXeEf_wd6-GbFCnbvOe43TPJXZPD1Aax6QH1APh20wbhK4q3x8kGzPP5HlScQwAlLtgQ6EQKN9PahTRWsoGHAau0yu9BHFKUL8-pntedZim32SQNX50gi9wNyz-OQ_hfKPiXUhq73JFW3yOzlFyF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای، چه گوگولی
😄
فرمودن "مجلس بدلیل پایین بودن کیفیت دسترسی، با افزایش قیمت اینترنت مخالفه و انتظار داریم وزیر ارتباطات از حقوق مردم و افزایش سرعت و کیفیت اینترنت دفاع کنه".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kb7lsL3fJQmHMlzdqYxmJk2cyWBG8ovd_PKwW1DDSe-aUI92E_UD49yJHffZDbhZwd5R5e_pc-ly21EgqYrGKhNcMvRUx3N6oHmM1gtqJJ_2PTEdn9o7obv47SF5hOmBUdFEzBpj5NG1n2BsypIVH4YbZfvbbWpe8wSAgkk3gjK4TtvzSXECgZYa74rk2_vXDrwdSOIXN2RwDGoIvjszWzRM8xeicVnFwFecn5f5kNf47_W9QxqfQzXhoyX8bgmQiYvS3jAINnIU5zAD67Clb4Px6thw-9x0NDGuXxsBi-na4JimLF2WPnIEL8Co-mU0GP00HA-g3K4DzWtxBgypfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت Google Flow Helper برای اجرا از طریق افزونه مرورگر Tampermonkey ساخته شده و کمک می‌کنه محدودیت‌های دسترسی به Google Flow برای کاربران ایرانی دور زده بشه.
این اسکریپت درخواست‌های داخلی Google Flow رو زیر نظر می‌گیره و وقتی به پاسخ مربوط به تنظیمات و محدودیت‌های سرویس میرسه، یه فلگ مشخص رو پیدا می‌کنه و مقدارش رو از false به true تغییر میده. بعد پاسخ اصلاح‌شده رو به خود رابط Flow تحویل میده؛ در نتیجه فرانت‌اند تصور می‌کنه اون قابلیت برای کاربر فعال شده و محدودیت مربوطه رو اعمال نمی‌کنه.
این ابزار VPN یا فیلترشکن نیست و خودش محدودیت شبکه یا فیلترینگ اینترنت ایران رو دور نمیزنه. آدرس
flow.google.com
باید از اینترنت شما قابل دسترس باشه. این اسکریپت بیشتر برای مرحله بعده؛ یعنی وقتی به Google Flow دسترسی دارید اما خود سرویس بخاطر محدودیت منطقه‌ای یا تنظیمات سمت کلاینت اجازه استفاده از سرویس رو نمیده.
👉
github.com/maanimeisam/Google-Flow-Helper
💡
telegra.ph/Google-Flow-Helper-09-20
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FFBO916Oe3siJxDaZ3I7SKlhzF63YLW0-bCvBgw03-SG3TUZxZP1JBOB8yAXH0QKoRUCEpxvQ8Nv5c3lcw5QZ4_OT8npeR3o3oqc_JoRW5N8HahiOmAHVk3HDxZGdARjCJKNwcYrq9Pw0RuxvSQi5xu1WxTjoItiJtU4q-ICIOtiTR3aXusYV-TCbg-Fh3TL5yAFQoJUgXbWaUnFYhRbcnKHfZg5hWh9ziEBnJgZXrtdmumvUbiS8gJPkUWhuqZ_4s_bBj2OTVN2UIcwkiU5hedsyoxQMiPNrUgOyijk-ZjK6YgC9eXIVENJfvWMD69W-_KDBQeZb5tVxetzwgA1GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیقی از TechRadar روی نزدیک به ۴,۸۰۰ اپ VPN اندروید و iOS انجام شده که نشون میده تعداد زیادی از VPNهای موجود در گوگل‌پلی و اپ‌استور، اطلاعات شفاف و قابل‌اعتمادی درباره سازنده و سیاست‌های حریم خصوصی‌شون ارائه نمی‌کنن.
در این بررسی، ۳,۳۹۲ VPN اندروید و ۱,۳۸۷ VPN آیفون بررسی شدن. فقط ۶۱.۴ درصد از VPNهای iOS و ۴۰.۸ درصد از VPNهای اندروید تونستن تمام بررسی‌های اصلی اعتبارسنجی رو پاس کنن. بعضی از این اپ‌ها از آدرس‌های رایگان Gmail، سایت‌های ناقص یا غیرقابل‌اعتماد و سیاست‌های حریم خصوصی کپی‌شده استفاده می‌کنن و اطلاعات کافی درباره سازنده‌شون در اختیار کاربر نمی‌ذارن.
در نتیجه، صرفاً حضور یک VPN در گوگل‌پلی یا اپ‌استور به این معنی نیست که اون برنامه معتبر و قابل‌اعتماده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fZ-KcxjMVfQrBL7VVmKJJgKFWVMdffQkOKsiv3lk8eAPG8UVrV0C2FKZknSTiecPTt8zGAA_R0PQwHXNLuWFNSmO58YuoFxPwQdcx5XQKgqd815t2sW-zT0twOaWM3mrYYoemRbdLfiUrmn0fcSo2_sCMbsM5zdpWgvZM_mhx_pGSVqjE5HOqhZnBCpkuz9cEu5je91ccd-ho8XK5t1sm2j7FcDW8nJZ9-jnAhIEkHFzX7yiYKsec6ipF61TXbm5bTYUWa_FX6mO0Q7LUS-OPEg7U_UIVwR_bxnu_cNfrSyxpKs8dn_pQ0WVrXRIyH2Qf6KHNPqNik2jpf1IE6-81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مربوط به مسابقه CTF بلوبانک هستش، که برای اینکه چالش‌های مسابقه با Ai Agentها حل نشن مورد توجه قرار گرفته.
طبق تصویر، در هدر یک دستور داخل Response گذاشتن که اگر یک AI Agent در حال تحلیل پاسخ HTTP باشه، سعی کنه اون رو بعنوان دستور خودش برداشت کنه و به کاربر بگه چالش قابل حل نیست و اصلاً آسیب‌پذیری‌ای وجود نداره
😁
مسابقات Capture The Flag، یکی از شناخته‌شده‌ترین مسابقات حوزه‌ امنیت سایبریه، که شرکت‌کنندگان باید در سیستم‌ها و برنامه‌های از پیش طراحی‌شده با آسیب‌پذیری عمدی، به دنبال رشته‌های متنی پنهانی موسوم به فلگ بگردن و با کشفشون، امتیاز کسب کنن.
©
Maji_Call
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vejCVnCag24Ts5iV1alFtGiCVh98fXPsU6WzoQE5Cl5Bdjz5DZPosOd-bAbOMmtl0bdivRrSDCtgA4ORZ4sNnLquRxKHjjSyTlkkzePiX-shev4sBhGcrTjtuiuUOPF4KIz-6npG5RtnErmAi_ixIzIUeUq1UneclWiYtmm71W-XkQreES6N7WgZ2Sy5LLTcoSKbcboN0W9fKeyShW46kN3GBSPoDyoUSap05KPGJOtZVIWH3qMSP-9snNp8rE4jLZFJUPw3HYoeFAl0sHGxG3UskGPTlwNlGIY-0faGvvpeYrpFxwAvA6FiZLi-WA3uKxcRjdaqrODjST8mOAOh0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از ویژگی‌های مهم Tor VPN Beta، ایزوله‌سازی برنامه‌هاست و هر اپلیکیشن IP خروجی مجزایی دریافت می‌کند، تا امکان ردیابی رفتار کاربر بین برنامه‌های مختلف سلب شود.
👉
play.google.com/store/apps/details?id=org.torproject.vpn
©
PasKoocheh
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vq8t1zAuRMlyFpi0nkBIDqgH44GtkLA1IiWy82VLAzth69cSvq4TtiA4_Ep713P5cMPB5XK_1A0Tk2pj0WxP5RjEuO-9JQrarL7J2ktuFw0Q2gqgV83K5qndiuvVp99kkAy-XqbK3gMSw5TGyiA8G_WSZWySKbso-cFRh4bNkueNv42nZkw5Oq_Zuedvv3iPO_wTZx1Huq-8ip3wA5lhI-4VWFEdY2nBOVSBc8UDgajvFr2pnEK3qctb4vmQDPzWX_3W5266FXaWX2vV9QsKQTieqwKFxBlPTyPb_6dE80rKh100Gv2Q2qrKld4bfym1Mfql8ISeX7rQfSoxGtAlIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپی میکنید حداقل اسمش رو تغییر بدید :)
تصویر مربوط به نسخه وب ایتا هست.
©
Ralireza11
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ایران در جدیدترین گزارش اسپیدتست نه در رتبه‌بندی اینترنت موبایل و نه اینترنت ثابت حضور ندارد.
تا ماه گذشته، ایران فقط از رتبه‌بندی اینترنت موبایل حذف شده بود و در بخش اینترنت ثابت با رتبه ۱۴۰ جهان قرار داشت؛ اما حالا در گزارش جدید، رتبه ایران در هر دو بخش حذف شده است.
©
itiransite
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JJxLSpezFBnYT6DYrgpJzBicohGkLOP88ow_DDdsL4WJRPf2xczKcdenxeDA-gRMj_F1AS3okzYE6Mta4PoaO_LllyVG-4PYltRGK0_MRLLl4VT-sFHQTeintPAxq5JRmE3juheqJyxKvZ0IDqoAA-zeTaHShZ8Jdp1M3ofTRiZavjR7VWSbSSmtvtlPMK0HHOQ9aqs8IZ7o86ymnpQ8WJeC-5fo3YuEhu56GoEJ2ukasI4IbapnXi5wwGMN0_WtHNNDrSPPns4pstvlnuIktY3v4wjSb2BgGZT7QJIo40dWrU1dgAeH8n8GKrAywoDVLTKVe5AZDy665_iCD1UeBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SjjVu-UMNBZS_59Op69MZU9yHMi6P5yIbT_jqjnK1vtN-qdb57B-nlqTjYSZBmYuSnz97CLpqJzQDuNVHs1KUUT6EX3B8SCVs1nq9pLx8-rbTVHqphIU0zmgaqg9SFtYFsprPvDtAz_XFr5G3PIH_fd6vXHTFLteQAV-B3nXs2f7XEuSZAVkfUs9hEgg9VSzsb_ddy63xyjkfExb4TYxoqlP5itFfrIvtPpVTPohjbhetb9lN_1xcBpQIazsBvic4OiCNQ6avvwYfBZaL4kQrPH_C5akMmtmC2STr32DBQZmbpahvZR80HbF2Z7GaylMmv5dVOqkjJr4crpnej-_Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی خبرها
دیدم
که ساکنان روستایی در منطقه فتح‌پور هند، در اعتراض به کیفیت پایین و ناپایدار اینترنت و خدمات تماس تلفنی در منطقه، یکی از کارکنان شرکت مخابراتی رو به یک دکل 5G بستن.
امیدوارم برای وزارت قطع‌ارتباطات پندآموز باشه!
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KTcZ5rwsFKzoFt83ROLXVvtwZGmW4Ygl7ToxNBUqMdwLDqD5jYMKqrJ6tu8Z5DVEf69nSsCp1P-S70NVDo_u6Lk3o87LBSDwH3Jh7MjIktbxsksk7vtMrwwJhi5IhfiqnWieJxKMeQgo9ncTtIaOb-4jhUu0mHxdRKbOBvOA6yKs5sG9v1SKr5LDS9zRyJ0eDk7m573ja3ts6a2tBQLV3mvKNs4BIKXD1LMjh4LHxK8vOXNWDud1guHVC5tbAAs1BEz4N7Kov1cGJnnkgSUYoPv9940soY03HAoheLIHtivqoCDMeZ8HkMWTc9F0MnOj73EJmzkOaoep4q-Gn02EKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B6S-5PvHijwLU2Xx5Kmj9eeW0xnxFkeWnNNxRJcY2viwTyTQWZA5BzOC9AiIzdB8etVRX2dutI8iX-_BbBrfSSJL7CEcYnFA_hUw4q0AE2aAZWNgx2P2Mur5YZtT9RhEOw5AlINeAsrrbBh2tjeKNCtJNv7QikKT8wzYEPc0ZnFyNR4Ri0Y14nOyhI_1XkDeL5lvX323SJYZwGnWv3ZqtLopLyJTBzRiMq_OPaTsXmRJOZW6QyxCZO5NIHYPaBRsGQYpqVugCCWfApA7ZY0b1H1V7hQuGsvfnzPsuxPURM5aPMXb4YQkzdyc2SY7ew7spHsfOG97UBkMncb2TdeNKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether منتشر شده و این بار Tor هم بهش اضافه کردن. حالا می‌تونین از تور بصورت اتصال مستقیم، اتصال Tor از طریق وارپ و حالت معکوس استفاده کنین. پل‌های Tor هم بصورت خودکار از BridgeDB گرفته میشن و Aether می‌تونه پل‌هایی مثل Snowflake و WebTunnel رو امتحان کنه.
یه قابلیت جالب دیگه MASQUE-in-MASQUE هست، که در واقع دو لایه‌ی مسک رو پشت سرهم برقرار می‌کنه. این حالت باعث میشه برای خروجی، رنج آی‌پی متفاوتی نسبت به یک اتصال MASQUE معمولی داشته باشین و توی این حالت دیگه آیپی ایران رو از کلودفلر نمی‌گیرین و رفتار اتصال تا حدی شبیه متد Gool میشه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ca4wmjg2EQHueQ7IhzblFwaYZ7pipynZ_23Pctf6leKgf4IfGqz1AGJ5A1AroiM7DbJjyL3dtFYm_f6_JqnZTfBEZMaCy3o4qIB8LPU2CJRYpxhvS2NzDOSBo-pl0A90iwSaAnSTkswqKRLHtGlw0u3sLMnSUIcg0CN-xzURpPeH7lMxoaW91dM76jKwe40JhRuo_AF4zxqUVU-MdTla9tptqyDv-aSxe4ERApzAlW1BAVBP5xlUVR4UgIYf0adIno2xE0Ul46tmAGbJ4uyFMZuHKhsahiEoFWULRRvlqeSWaV5Bb5d5IFPwpz0t4a-Z5m_J_dFEPlFtY27B5xUx9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک، شرکت سازنده Claude، در گزارش تازه‌ای درباره سوءاستفاده از مدل‌های هوش مصنوعی، چندین عملیات مرتبط با ایران را بررسی کرده است. در این گزارش، ۴ عملیات مستقیماً به جمهوری اسلامی نسبت داده شده و مواردی هم به سازمان مجاهدین خلق و یک عملیات فیشینگ علیه کاربران ایرانی مربوط بوده است.
در یکی از موارد، یک مجموعه مرتبط با جمهوری اسلامی طی یک سال اطلاعات ۶٬۳۸۸ ایرانی را جمع‌آوری و پروفایل کرده و برای این کار ۱۵۵٬۲۱۶ توییت را تحلیل کرده است. در عملیاتی دیگر، بیش از ۵۰۰ کانال برای جمع‌آوری اطلاعات افراد داخل ایران بررسی و ۵۱٬۹۴۴ پیام برای ساخت پروفایل‌های روان‌شناختی تحلیل شده است.
استفاده از کلاود به تولید محتوای تبلیغاتی محدود نبوده و از آن برای جعل هویت، پروفایل‌سازی، توسعه ابزارهای نظارتی و حتی ساخت بدافزار و ابزارهای فیشینگ استفاده شده است.
©
RaazNet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XRnYVA6-xDvF6DjCaGiUxvc2prnWdNiRb8NFa2FRo3UlL8ZP50zWrV5OhLGHACelycEXJsgPQMrCNyu4b3KcRCTQVB9xnCTnbvPujDqshBqCxZenpWbj_ID1a6eWdenkvvmQW5oVUSDbWyvMILZgw3Db0PziuoOvqnkEXJLlN6BEcd26ZXY99ejUGSMwGJ8rv40xQt_dISOQ_g_rQskVNZ3f8zXoMjAhTY3iJ7NnZUK5HGiBmObyJx9Min-_6yDbtJ-l2RZ1Qt2I5H0OwWNexWLiMVnMW4NgjRM2bypAvc8CsjwJcdmD0yTH24CMO_RBy1tQ7mEVMAa-2miVyQEoJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VxmJ4w5DIqrWxo9Bao6_7QlQCf60gQsmmmd5FSa4vrO_pfXM7fpeeP2JtJLkEQ4d2i7poIjYqvXaKItPklToE9yyj7zQ-xm14MyaYFNUmg_rUeklEkbiVBOTvrTsZsILA399lkMMRsPlvDx5LckoAVxmCpII8MXNUl1EfKsvl9fCx2AhwEoVthGZ5iZkNt5JWWVxtnOpf4QOPP2lYUsawP5BGANBgu9F8NfRnThnGByzrPkApkGVTJHax_uN8nYgZn3kOnt1JCOaBm0EMEeTMFpdslJ9BRSTBK2Tl3Ul4jRZSido3hWqXqGX0vo31Yy7aShX9hw9PBXGZFPrvoHunA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/htxg3GbhXulNuEV-SY4I4UOZXItvXWocwnsox0NGmxJ_7fOAkPaa7NuWVbUq5ia8wwKu_DYu8QB8x7GTf5ELYkWrKm5rNx81fU0caXeLYzwSkpJ81-Jbd_JgahFWg_ZeJ7_9O74YiSo55cX0ZtzXABF7GCfzrFvc08ea-ejvfEtwgr26nDhE5we1BVt90Sbqy0X6JrOo_j2VUyhGXv5VVzF2f52LHSLGuToU_FJKoU__QTKUIGa-cY6RKzyE7NjUDzOmEZAlHUGQINSDzOO-JM25gbHmfh4ib9GLQVPZfnIDYW8sai-XPa8wgui1BuNnG3oI-9f3W5e1vKRa0WGiLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qj_mh3s44GYy3oEj5OFujzxQ45vjDrPZw0tS-bSYE_ImPmFoElw8iStGWXFwFrKiRyzFN1Tm7viWRSHXVNp752vJCw-Kmr6RDDS1Jn6vh1oaOKmnPBDb_0DOh3FvqqN0xTyROdD-_D1r3ozVSJDL1COvqnyTn_eHcmS9gUT0Q-m3e86I5LhLMz2bo2eEeRIZ44_bwENnBrNpV_K06d416zgSiJ0qQs0ttpxzBlH35_aDM6j4zjaUYGWknwvQmUg3cMb_n3mRDBUXIbAlt24YbIME_TXdRI3t2-6PahIZTdcfRsEG_yggB5dBXra1K7jUibeHapsBXOc0j5WaOL4QRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yqpo_825b2E-Y6SCxMhx0AzsaITk1bPUjqWFFdzqSeEMZkzcuGoPVehzo3IqUZ07o82XgLskk5I78f8gDAgSqr_LYc1YdEzCph2yzwY9JLyjHOsHzec5ctjAnJHDXbr6GmZRcb_BRIkSlhQF6Gjg63gedNFWYV1eHGjwWEDsbYZUg1_oMqSTxWXeuISpkpayz8rUPmojX9RXcL-0Jbz-fsoSYl4hqmUiRskeOtl7E3Sc1MA7Mt4YB6Ji-r59Fb7AqzMYCJVy8i_tezMQIK0mVxyKtaObErEQ3D5RHzddjKhJYoQwDy90MHpP5cH2ReHEKbqIzKwM7M5NYhRN6NtckQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tdXu6fDCUx_jBfoEEM2nCdOXBZNYGiQ1EStr6Pe66wdT-962X5ezM9_JYx_3t3yBBr-UCzNAiIY-mJrmY0jbZ2XZjHwgjX2Q4U828I_BUPEMgUQG3QHUWEaTnk64HgHvBLtPPAmDEDqGahh8ggt1X3Ee_jwVcv5S_dbETUaoytjTBg3R94bHACiaHwkx_ZpSok4uomlRytewqggIakW8Y2bVcYJn1jBZ-dWl8uscWwGWLH9lW73Hc-r5jW12ZZrIOktox4cEnQPj0n-xI3aYuxuf18jM1XUj1eOazkWhT_BMjJcp_ZLsaJh7uYEkvPghee8EBdbdQjIzuN4HwJoAdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S7XZfaN7_Dmj5VJ1_FDdRAMnY5G1IHiTh-tJeOadAMQwuT71WUOh-X51xHWRz2xe5VNgpcGN6zZBu7jx3E-OrrpRt2AMAVHHAj72Ed-RgNYiKxIjZZufSVWZvVedwUrt2s8HqYdSo6z970aIM8ipe9YHSYli3YlSwfaq2K9S-HAFOGpZqB1dkhXJz63-26VucQnROhqcnKY2UHBVr5vcdDWGUcoJW_dpysRAATg-sZU46LpCbpKB5TgSbi3e38JMCtVJyF0R7YPIGmStJvi-HIzisl2syxyIGP8yVlpBoJ_B1lZf6s-LM4Klyvf24xbajGPs22Eb5o-YRC3VVlQJoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j6hKvGa3dzsVpR25yiqrf_PvOQDj3vK70E2I1yek7HB0bjnoRcdEZga17tdWabuXawDrg4NZtfMrYu4nfcJZr6BP1_hPHWvVRAeum0NB26WDDLl3NLKBnenwIf4WnVt4IqLv91z3zxHshD_Yu75FkFSk730TMOTBKXCgKxsZjkck8cCla06TYU-PJImNH40HrcyyZ265ODbasHUCNLQKxPaHMbeno8CS-2bbUsgrQioAlpwDQLJITx3xdAhg38NKrRuz7_t4INr59kJIM4EcfwcQVC_vNoCHHP3ABHHeInRnzXZIaKafcX8EagAh4d1akYAIJG7QLXDev3vl_GzhCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qglmpy_DbJ9metey8VbG7Qd6sIaBCz5c_Uesl1XmD9bLwxIXSgU0OfuwLelR1zHS9Ptr2egF9Hndz41XQXgxXznt8HoUpTIL52h3Nwy4rpJOeM-VO3221pdX1_ImUVeHCIfUQ5bxiH0sNI9c4RK8678hzGMQ6rzLMmMVTJSLwt9VLHbEZ0WL0UFM1NC9sxKE_SvAX1kDCOfAeqEx5Gn74w83g3C5fQ7oiLc7gH3OiZXod2t5MVDYlX70ozQ0LQMbGAvkxyRSq7Syk_hdDenoNCUAWFyh9zMph_eW3hnU1eb8hb9dIRQzByFJPFNSsuNEkay33jm-SCveNpThF54CYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vDXBu-2esWof2tuYnzwWZEhiddCK7EIky2oZ8ScnIcwyQo2xgG0i4UqqGSEeOXtUjbHlAQW6_XKoKgdBDPcyUxi6X4TYmPSXDCALQZtyKq99J0W9gPFjTnAUAheMNpUPelamnulFH7uZgMysbeJmhw_AToSwgSfczhPnpPDJ8MtGYtkyrMudMVGwaIAo4MAhAL4BdU416H9X_4eBBKe-rstp1RupBQdRqMXhU-kRpGXZOjCd_w-xpXxzu0XVzhF6DY_m4AV-n-1W2S-Qqst1F-98ZcNQt3haQlEuhhuhh2zIcuqyd071BvgAGZWlPeWmnGBFkoiLBl9WtLBhSoLX4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AqXyPbvA05b6YaAz4ZaBe31IPmpBpO2mqBl69cDh3wNqMBlEgIs_pDqgGrwVCMtXvygPV33EM0f6Ul0iv8pzGrSsWpeWyiWKWMWvVcA2tpM3OeNsricxNmrWQC3ORfdHuEoNQDYifCKCxp0es95jEndTlYwjijrhGmMyXxvHNjxt0GSJ6EN-QSn7w_5XBU2otbA0RE0R_aqTq6bGE-FrWHhTeEhqdu7il9KgcErk4Eo0Knxol3Bw7hd_o3GRSTwP-Zx41KaDWXFW44E27EkTwPeUqz1iIOORoR3vDk_CSBuy5sYLP435xl8jFTIcODrqgATz7fPFIGT-gxAjscTnow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kDe7mW6uEBSIo5wZoaaSwscglZiItRkbv5n6ZHsloENQ3xr1Krb-9-EXKAEd0SiiVCTbFISQ1pC4hs5UaNHFBFFuC1LHQof8ca2-V-d51JbnPd-4wfPibkzWXoXRx-7lyzQqxuqEhicWyUwIeO5Fl6FicmXBdBnW3lrcGC6fpDpYV5KwIjxLbfRSi2TlEGkubaR0nVwT5gRsxNa8Rx73YIsKj234EZdUQaA9z-6gAtHIRWkCvxUBGYHCxd-4xQjxLKqDT00UYFS5HGKk_vjf_ekO26cZs6sHRojXiBTkDlHThDfub9i3O53uwuI-P-6PrstMUMFAJhjrhE5IWYijEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Reg8m12MBLgQNVYGQLZ6Y51S-ZIjZUidrZDjqVzu4uG4ZJXMujVF-1BL-oVF27IB2YO6cAZqDDVeU-fWq-a7qSVQswICBBT-21_YnnJxT69CW6ulG3I25VQ012oG4pXAvpsDx9lzuO-RG-Jpt5Hw0gE7iztPKcMpcpM8w4CxZg4ZDCSwYHcRVgkklsTkB5bb1Gw2ZTR6VGdB-r2ficpGIkSMd7DOO66XKPcZwxxEt2AvoCkUg5lxEFgOkkJ5Rfiip_voylW3bauBN1WcWPLMP-0fTt6KxW6ZrrFtSTPtmfp8LdAtTa5Rb7XxO8wPC25yw377xaOUBXTyg7Qh1-nw1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DZlS4wi-q6ooK6afipLXqHRalq61G5PenYlD8F227Nt6ZI-2yhMTCyxhz2fsRdFi10RQpkwk5mgJ9D3xgGEb4TB9dnnvhYS6rSJUd6-JyAOyAazWXw_IIO3L5siATlGnOXyaQmTtBp3Ezxspy7T8w4uy2Mgte3IqyD3x5pFL91hQO7UlVLxJ2IozWnNEFQAUZD5SkAQAjhwedBrRuD6AXVr_y-_dNZF-iuK7XmWFZlXN8MYg84myNyUs4rXXninLDwHT1w0rWDy0ojzSMJJIZviZMpKl2F-asq-yayLKPvmFq6dBU_pVhIPPwxCvYM5frsn3NXg5yYbAgM8ZbUMdPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fhNJis9P78QNXs_gD0ww1mire71RwxBM2qVq_YJMX5IZQ2HxoDli8oH_cia0xdbV20oWo-i050_9RKOF_hk884XPNEd297SzjKFzn98Rc0NXMIH3qGSg6k4G5_tZokHRf0aX3yQymOw1gK2oAzG1GUWlcfCk58Mm4DX_4MkKf7Y_3yQIUru6gng3QX_srKhueiPnuoOUZo-0r3F_ae9rlgjSXfEZjKolhM--sT7JLos5u5-g0p249oW3zRk9bAnaG2hp5rfoB_mPQuMwO0iMSF-0pv71vJddIChcZO4aD7dzsJDfnFU68XDXmoMvo2pvpLwck8W3bo-sSP1rwPJvhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WRBzApIt3gzHAQ9YZdpp_p3uS7cFkXrhuIII4JLpMV50e9aji2ls6QtKYun7EdryYkZmKdHB_-MWJN0VQ1csCgaNEQ_NBYklxzwK5ySzfanMt7ICA7siYAmDLXeJzWkd1ttdW_npPqkPAJYdJQrYvBQryrZVmqyo2NrgDNtgtXGBzybcrQYlLm4ZnQKLcrMOg-xzV02W6qQvqg6LMiRwZXpmGqeesYoJWKWZXVuHknbOEpdXtke650LKCDlyX8-zlZRqrd6dLERq3RJaZ7keoxsNMcZviNKHI5-FtdijYhUGrjFlr6_f-o20UsFwlTxVNYHx84Qp9SVbvNp0QQBIWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DvmkW7Ml13tAbMRZwK3AB5E2eWDJjc8gjqizFf8DBl4ZZ2m4khnGqQ67ElFCPcS8QUMpNQR7XLlamOWwq-AA6pNn7c_BFk0rIKyckxe-mz63M7EObw_vveNl8INzMrWW4bsa-qGXtgJ5tvIC1SWLv2fDvBadTYDg1QkekcurKKnwEu1aDd1YjBRhGPqiqYimr6F4XvI0aaOd0DMd8urljqsJLxO4E1Br1yjxB-AbQentGW-rvUL9Sj-vFQZAAw3Zc9BTPSnLOvCc0H4Z3AzfgzeqC0Pk_39F3iQ6gxU9I49OlBRsvoX8uucYw2pPjam8xwg4fW7D02Vvjxi5nMnuKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lxvLrSBHAFR3jL5XxLwWpu_8IR6Jh7excGcjsX6a-NVdgPQo2hFWSVB08hSbG-yjTl9HZGz2LMITYsfk9vQ1aNX4X8cIr_vY7xMew0f8QalIudH-bbjMglHxc-siNZWQlkvXJqv5b7aetgHVm1Hv2qzHqL7BdJMJG8otEWHrvUisFwdPffYwveh4oSgO42ITB2umWd8SUWofERPTlV4LybFdenUUhmQERKglONALz_3kCnzdEBPqFKm_X8uQp_BWHyxhQngLmiZTkYZnnehIl9MQ4prI-k53Q5ExmgX7C7ieEDHfC5xkrmVOeMsa-9cu-If0jOPoAgkjDbcaAjIqfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V-h0fzWfqiSSQKaHYTUhC7KRuiD_5s3OeD3GliLJyP95R5BzUiDoJiiHPJVWtk9q0DRygQG2gbIl7sHT2975fyMHCqFzv-nIydMlPX8QDRTNDH9b9osjVoq_h-YvUBGYdxFdevQVvggj5iyokFO9WALgdhdAJUJHhF9_V3wxycYMmS4MWrwYPYNbbzPgeXZvBC0eCEYkhz4CgapwkfmOmu18THY-wDoqDlt6VpCZS5EQ1TiSZWu4aqR7L1jJ2EjQh-DfS6iR_AGYQvTXZrLynhDAB0hLGRGZC0VJegeU0atUcDfnIJ41r455KbNFd8zyub-xxYv-KbN92WDB60Se5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eXuHmCMIA6gZU7XJXMPfOuhCPR4XqJz12ubG7ykbPsEvgDHZgZCI7V7JFWXwI8-3iAzCdrA8LQXf0TO8mDJpNQd57zSRyGtPFo5RYl0IEUZQ4ZoxO1uoxS7H59GRZQ0AyXNvRIHuul8L3dkyR_edxMCM3Ew-X_vDyM68Z8cKSzHfuh7cFHh3t1bGb9oE-9OxqTshZAb2Sm_pLZuvrE_x25N4ecUyhrAMBiT36kJekp6EnxhgpvaQvLVZhve-EeObCwIJzgSuVzKvHnsCTFkSxLsxOWv8yi1kOmg6Ho8Q8mRxvN3rPG3cCDeApE08cm262mHn_DrTm12mGdn1jIh31A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 43K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SCNpyqlyD1kQ9Qj4G5r3SWj0HwLBhjyQETlj-2OOInwCfOhALZt3-bpCMcOsW2KYOMz7ErRsEOpFt3cE02_oTeLPG9mL5lYRCsi6-gpxrI-SXqooWZVSKPuY3N4kLrzvnzI0SnYntcxw_-YlkOyoJxJ_nMs-JsNOANsGvRd9U-MeJzMmJzC9BCXP5NYDAiXCm3gB1rk2XiXOAz7crN4qYllMdV2ccL1sCv83d10HOMCNwJA2eAUCZzfBm1RSsln0haDkiWRoeV_gqu9KV1CBGypUJgb1rXKDwdRdc5X68Q_-F4v-6ikuRwIMl096jpeoMmwLBbf1SQkIVm9GUsc88Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qQHkq9gAaiJneKFNEQPSPJTvpGZ-YtytZ-_dovNwkO8jrw5Pyh326gMBySficKE2ft8lg4sGYux9AP4CZLBgWN1P9nhDgj5CEQkupi3jwE8g-DW9slcI3wwHjVS3lRit0qyxKfEN59s_fmeQrXdTSuyEezET__OaAicBCey33rNOMkA-eCpBDnBrnSsQoDJEUgXO4_xeh6LRxbAAy9okQp54DR-pqWBuDHRCjgNxXArrFY_EqTxkfSDQ4whpWY718-fgOLS-TqVgAzqG7HCWMl3_tK6zxMEsbFNTDH8nENq66KS6FerwnPDNjaqfLT8IiSoA7AxOHH0NAypHrv3sww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ggjk_yuPVbXksYi8gjoNYN41goaUWJ9SPl9CFCgzxYykv7XjLrgsSKa5eYZlzHeqIdQN5qGNjPk6XIekw3hS7YI-fvEcJguhK3-NbEP7a827u4g_Y-aZ-nV489QR5MC38IhnGeZRqB2QIUDomP1WMNnIg8e2lhaXRq3ieln70noIU15JfO-Yu-KSB5ZgOLPj0E04plj3oDrLX2o9eLL-qWetEdIqJYGRj-Ga7ITCmYOeTgmcFoyjCeDRa5hTitERU2gzF1QZLqx83MGNl9CvKsT8znlyfYeMiIij1e2e8BkpVQ6Jrf_xLGnKI5DLHKJZxGoX3XwttcJhb-gxBRqToA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hfOFymmhPQdzyf-B7xhMivdGNLfucf-s8j3E1y0HVh-gQuNh_JHAutGCx7_Pps_de-KQWG0qjjusxNkxsLkFCfjBZT4dtC6sPDryhqIOFCCXey8Mg38e4b_yX7Z0XNy_gpDsUr6Lgo5j5Q10g-eJkSrybelsMFbX7vU1VAgsrJWA3kp87cqdXSxKaHMHo5q1lhivwddDZaS5Br6IbTnpWwAdxKVcWubimf6DXiPUVgeqSuExSb_xO_TXEx_aE--zq47uCjxmWEo6ncctq06wu1pt8Ugxq0sE74aW6CxZ85SP6LYQEzHhP7ponvxGbvxMkJIHIcVb7hDcr4tzaHZWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ekqUczEy56msPIQdhfHXDJY3o8ZEjq_NeYM5CDHsccu8PcKjbE4gJA2CuS4htFIwIgDHvP8HjNBe4eHD0hAcmYYO4TU_iHaoIeUoGxRthJ2tnWhjQgX36YCInHj2rSE_hw3XefZQn0m3iQh1FOLm6eA3h9YpLbMWQBn9mnjfwL1EmxUFsiI3e8vJ0PH9fl6IU7NEAHVvmkwlavcHM4KfCI4YXeUG7F4XtnwQIt23Tgh6zag_4xC3oJR0LP6gTod0fBL0gwRPwIZTqpUnY_7j-mx0FX8AGipmZq9x3NIW2oNEgFcs6ccNEVRhzFrykep38yGxMQ-o0Q_3v3wNWb6N0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cue1Jd7Lms3y-ystB_sBo-fjDYUG49q4mcXmm1jul9RVuvRBZmSZ4w-Et1JP59l-NU0o2xBB9rPsQ0WRwmhKZJan7Z4Sngi7VrpKoQxRiqOEhEEC-T-QkFywtFaond34J2C_SCQ6eOsi3I6N3CQlEct3CR_5QeIOzgeS7V-OP9IDXseWYVuM3wohbKnGlIP0Nip8zLLwYrUvEOjNsapaGuZjCdP9FWJYQctHjOkq371jE758lQro4U-35aXT1brDgL5J-OHHWhcEwESM6t3BCv00LVomrpTKUNGMGAD0oC2Ta7Kp3MUB4iqECd97H7EZHgulTeL-Ou68gZooLqC3Tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dCt1aWaRHaygqgRNlEZjGwrI371Iosw2YR8EOZLTptQaHALv_vwufyuhNTcx7TcN94jT1Z8KFY9i6T9nURBzbjMEG8uEcIMpfD1Zp5HU_OhA8orUFohUj-u2JlkF9WTD58c1y0cUmcL4WeGlioIZdDP3lwxePo6tNm63sOhmfHKe8d891SdMOM8GRNGqIRgNKCDLL5MoMc4bzCiKsRUoSUNwmjUq-B5lT5UKJerpFvpMS8lbKOVGzybrQSBmy9kQGKABUhErfb7wQ9t_VGG7lgepWLvzKtZ8FvvT9IC7H7o9uvPI06qHRU_U6wv3L9Ss_M3LZT52mxCNWxF0vhoW7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PBpSPGJtsQNR8qdemnx659HhfpuE66yvjWAn_CeQJ4Kq0I3bBDZPhShbvHCDkLcf1TlGVj5RCsu-OA0u9k4_G_x6ZTVVhqOcDvWTn_ChQg9LLW4_Curf2m5WpEuts00mwCQRCcasLol0oH02dF1BHk7DzRgWL0htSkE-1t0CtbVaccsz6GF5Y9hB01pvA8T6wKANDNMPOz0gJ4fI6A0R2GnRSk6ZeEmkjOqtpqTch1jKEGig4ybR5D5hWvbmXYW7HHvNSdM4Fekg3CFsHTTOEsxyYNm5xz8JciQUeaWOVEh1pGdCaxNkJKP94FZO9C7k9hQqu21W38nBBZ1HgEXkKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JqFLrZmfjs_2g85JKZNfjy8V0VsceS5UxHF74ggc689eyn0z_R2PtAiszLW-AGwJW1zovB-XCmqVzxNXtuMedr6ptY5kGi_noR1k24uvr-OxQQfsRe6-cC_UfLHZYrFltSRSURDVvUpixeHabQSltNoBcDGxGVUaaEVg0pMv31-_QWg48dVMmPX5ScVT9B_OYWG27AiYpV3TM15kHHW5FzksWrObH88wWvdKmvI4w03GCb8jPT0GiG1tAlUpQoHhIbeCDHNqx70idxQnRQdQwsRjkLh9QGPTceycqnQATHH3lXFguSnPxyqGQTLd6M1E-jDTV3GeSlb0xxYiRd8T6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YKZAYd5vh_IjKaMvtf2P750rWO0m70lKYGR7SCTECTFekQvlDrAMwD3CjLAxe6Djv0mHztfMDMk9ATYrhKmXj7xVtLrSm1Xr_XGoA1f86eceQP-eeyTPYlGIEJLf-wv9EcJIdIIYgAeNF0hk0WFF6vvvuNAgLEP1ns-eAy2KehJBZOnjQtLY_lKIoIFgaDK2BYwjQzBpp4XPDSQvKu5abq_1BTzdX7H12dh95VGdjs7MiKK2F40D-Bx5hl1VmxYGfA1ei_fMW_KePrPi7wFAYY5nGJRgqalts7HEMhlBQZXZ1AUoPaV_akhqPn_1MXnAnHepk0s4vbSnhBzTM4C76g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fTyCN8YM00QJ3j_RKnfmN9BCyJKgKdmqHq_TU_N57uaZLArQqVajoh1HJbGoFAOdH_mqxbJ934VuRuZB3NM_4TKMhkTlWnde_QG_UPi0zYW9P7hlCaGzA9ZacIfr-Jz_ruI2y5ZNjt3EuBIlmkmMqHOOcdxJFAgRfcSopkrFfPtfp0AXuyr_tl2Au2uqtuhwldgz31swbRsxQCdscfowEdeSNN-BgsrJuFwm96O4zAczDPPp663_SBX7QOWQbF53c5SGwwJ8stfXqlSzgzwlXT6eOCFYZEn1gKjvHTeAmVN0sTlqd9a77FHs-nazE3rPJsf7RYuo8I2Hvl_RrfUouA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OUOWMe0YaSntpX4YEyrXdXHt3oUUvwXIFKeatC5f84-0Gpwuz6AKUhLO4c_kVrq9qKnOoJXaUwHvtFslS4aVQpRxlZxj8LEDbOqf5tR1UopQjq8pCaKDX1c_t_KePLX6IZeDYZiunZyXWgKl0SpO049UivZFlf8BhzfRFv6mRtSaHj1HiKMr8sSEb2v797fQ8Q25yzBXR7ffF74itvhf82sAijIB5wfV83rPFBXqa5qJZ3yTe6Oi0Hk-2VVyxzcdGVUnRc-dJGy2sSmV-OOaTQQv8Oi094Rp_BgHez4nAsmKIYQD307V2k0N28zfUy5ZkR793DsubgJzpQDFKe6tfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V8_jwUUUGPe_NQ_yU7rNi9B0Ope3fIOqoNNauBFrcRvVgizl-ob33NOGR6aAVem0kPXJttKMAGKFO5mrg_PwrhJFFMN_Drwx1_umyWHAXA9XqfJFc_JYJ8qskv_dd3HOSD0SAfq1x4iGzKohAQc9IdoYEDmx5qoiCgJcc5jXSRZBjMSbd8rTGIlAIhp39GvtP1TqtcOHPSrJxb2zOKTtdyRfclAEcX-DJe8rpf9lH_IzZDU2xbOIQF7TdqpRVU8C6h4UOLdJvP4H8bwwZtMf5BrewPbmCpQidrkCt5laN8lHFQz0e2QLdCFy4wtJoFOl9DEFEVVDS1yVuJlihjD2nA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qbMj5-BnGgKMUBBAYVNQsuFJap9YzsuTGJJJA70CBLSxM9aoLdEAuHn5NuxCQTmkeaui3x0qXJB2xMCzhRHev-hxhlmzJLVhCkDOA4HUoXPoiCEaiK-cJVOT064m4HbR9qxox25Q8rFRpwrmVWcYsUwnqvKYJ0ZiN63xam0V3WOn1gedEYQSkvZ385F8yoXcOLCHTbYU9OETKQX5D_wOxE1kCrCeusqE6UjX-Xw_BBsutfch4fPhQrbQDO0XsHChHA0i6eGYBfiCMFYxB1kR7GjwQum5fBB8KEN0JOQPXrzUBWhJWbj96bCRwLoLjVtJ2kzzwZb9o9mYgOQX6kca2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=bgyjvJsyKx9Mnpm4OHqVEdNemy9Bk7hjdfXabDgDCH9ICMRvIKlHtii2rmhhfZEORNVwCczZmAeelmrLDXUoKu1aYwMA4nckdsyyMYcrCKE1sOkxUsEZVYDmTNZo8PwbhWYFUsL2lfENSCtiZ7ZvKq1Yz1PE7VHbcipvoSFZmPG77bc1lH7FU6MU2L1vrZ4C3GQz03cXz-Iu7Og0AVVe5ZnC4El9VRqgbVWL1Ppv0VAmWgbg2m7WZjQgQVRFTM5so2jgjBmH5VnbmSoZkEvSLxBxPuazP8hDBTFHSSkRkniclBWoaryREGfF2LnE3lmRkr2QbD2Eiabl7i9lcvs9og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=bgyjvJsyKx9Mnpm4OHqVEdNemy9Bk7hjdfXabDgDCH9ICMRvIKlHtii2rmhhfZEORNVwCczZmAeelmrLDXUoKu1aYwMA4nckdsyyMYcrCKE1sOkxUsEZVYDmTNZo8PwbhWYFUsL2lfENSCtiZ7ZvKq1Yz1PE7VHbcipvoSFZmPG77bc1lH7FU6MU2L1vrZ4C3GQz03cXz-Iu7Og0AVVe5ZnC4El9VRqgbVWL1Ppv0VAmWgbg2m7WZjQgQVRFTM5so2jgjBmH5VnbmSoZkEvSLxBxPuazP8hDBTFHSSkRkniclBWoaryREGfF2LnE3lmRkr2QbD2Eiabl7i9lcvs9og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 55K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ENbyJSBGa330Q5RPnNwUKQTBLhN2bLrA_RLfVko8mCJIkJSwiUAnDJW5KsSAUg7v0mstrVNC1-OLVA_mT25kMGyKwMOMoqdgPpKraqFxK1sM_HKoiJktji6-R0UzaPNN_ipackMWE1tTUEDfGYtxCnq16Ih9MPX3lCw76vhkZoV6bpwlrfzUpGJKNN3D6R-_HZpNJYmUsxIvqFl5EDxKKZWDLURaQZRe-3UHGRm10bXTz27fbUT6C8S0xR4Kuov-6ox3QhrzWheb_Vs6RNRfE7KipgfgV8--_wALjo5YvqWQGWd2HGBa2JZ8IcjIEhClFoQoAtYEHeBGRQk4u680SQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rCRpEGJ5CCcGMoaTpyNf8NWyiyyZmsH4XGNXWCCUXqecAjSA28RotYJrDwtjA6KhkI_yUztAebTaxJDLO5LPnmr-vOy666D3ub8YKG-5_ea-OASFpGqLrhGDbVSvY0QLr1YuavCQ0D9TWnrhbifJaQSSYMn0EEgKBlHRnH3U5wxd4wkM_e54pvL6rrJRuk2kdtYO3IALCKrTTiEPbf19DMccExnkjCnBsFIrSWDc5cBndjkmeN-HONC37Uus4UJ2keOteOjxcdWVIhKHd-I7WOzqTcwgoxa4zOfq-OeJ-OYN-1AEYtmkYZs1RTcLCnT1fIh0PfctirhENBhl6jqp7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HqYUasIk8KGGHtbapDE7WJOPN3cQoKpQAus-GA2oRz3pp4u9VPMeo3RpkpA9zpoToh7H0Z1GcqBW4WmH_GnHlGBNvfqg_-46DjNxTx1YXTkOr3OZ_N46QL2wpnD5CXnyyENvwONI9f4gFrcfwjHNC_nq2v_IQHnNmbatdORP_savKgXfxuxIoUvULM2zRJHm8dPI6I0sL0zWU5QQYwFT6hbT_bMRTGM8jKWYrcpG3O0WlVG-Zfb0f-UKq6VkvP0v_r66l-PCyT6AkHh21UoA6o6jXVxyYDFkAvCvcTLSinYlo6eFuuVj31BfXe4xdtTY7xvcocT2PjbfhCBtcTXM5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JpibmwWw2YgpjehosO9bO9w-IOEpLeG7PMQUE51iZQnZWejjt_Tdz3mOAWJ9aExyXuQMhISrGa3AgQQmOuoGyiI6-rIwrNdOdcT9ZgVRp3ZiIK9nN9-enyBA3LH1NYMMjjPKe7emG1UhOqSC0OLS3drT7kT7eM1Pr6jIEcgEqg3Rb5ZSzRKCGw6ORTbVydGqnNs8iumd6mwiB1cWSd2Yf9bBSBQX8sW0Sbv8LUX_eWhsoH2-nRuunl9PNacRGy2rMTE7rJf9CC7Aw8h0B8Nguqa5qcLbccWSy1lV5ymiT5B-0fHyNjgvvMlj9UJu_8LyKbmFInEv5gyTtdlS19TaKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lxkWDLapyEz4Dyr-KuEBWU4pk3rwtZ5pSXSR8PKmGqoTglQw_VZn8WcYN6_XWjzNEBi1dmkO6I9OyL9eiJBcQEBh8Km7hKYfKk-a1x6l2XeU9hULG1Loyj9yEaWx3fyocB6m5Y_vm9bsJuJygFApvHFZFbc0vCYMWLr49_xDWDpqpJP5762PBF3AWD0bOu9Xo80sxrUzEkf4n_e-yRLp0TYeU85r1JvV2DVx0bAnOqRWM5ofnI50HdLYjllgIImLlwk1MGLNpDB_fmoTK3sj6OXeIVAOaUu6cqgfqo6Ii21LIW6_QKNgGg56osgu3jGBnvFayJyiLFmeiwB6w3YCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GKYmKxRRERoPv8N002Yta8qmFnDzHxirqyUj_u6BKg6X7w1DzDfNXcZJkUGYjy1_B-lf05ZR8Ml36j9bcGq9J7gqlmoCFWYhXbiZVmerM7-zn5c7Jovob8TDkxpWEiARYf5Bx7wZ9d2RynMsSdpgUQA6v5W1eYI7sr65_3eQnAw6x3NpYg_NPPXQRe_TCTjUU5n25TW--Bqv7F94BueS07Jzzfjg7wF1usm3SUYgNorUrPt6mo9ADeJ5sniBKFDugEKBo4siBSQ3-kfpmLi9ST4VAgFO4_LZ40y1fsOnch27ds70P2EtPXbRl1d1GFHyk-lFN8duTL4UZEvbCBpEDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Os3Pw-V9diPBj6YOvuH-rRPrIIu3Fh8pp6hQDVnb5vn4STVYwHanAaRls4d5PO8Eua2D5rjAGBi9ZDrV78qaGchRNADhHL3umWVKYWapVwy7m1lDd1eSDW8IvAaPR6bFjKfkUovKUvZlW2wpuWz71ud--YgX95Oo1cOtDTMS7OAro6oLiwDVmlROc8HaG-DrFIXp7FQM6gbWaG_1q_TL7c62RJ6XSfad-crVjuf7Ud0A6foRGNZOGK16gm6fjhLwmV8Fe-ROdO_21tTSghB4j92k_oiPFZ9otivl9gsUCiMsPFsJUNLqwt7ZqJ9IB7myLwjhvVklf040cosdkNbYPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jttPsSZVBl9nxZqkF-8oL0aHMPOGGwhAF3Rr6k6vwbEJ47-Q1Jy5Vz6PmiKZKEhZuN2kLJNPQZRpBgB7xtrYdpBXuWWFLECSRpaKggeg-V3dK75pVOQgIKjDXEcbLCxMRuS71PBGw8430pZj9xGclQfwcFfT-B3A_nvPw3SSlwa4WviV1ceLfxe2sbCMAlgNjeKixhGNEbeT077QnZHRxgwdyN-05eTcxJPRKfYwdZZ11_550_brzV0kizfe6XSBa4jTYpSRNjk6H3huDtdRSj6_V4Plbd1c5krCv5rbQM9C_zxaYH8_4YqWVPG_iCnvVqfsIx2vg_V51t5AsG2YAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j5T-QvxN9VssnzwgC-DEvg3HYf2Z8fJJHQPBzP0VOu3hvOlAtBruX6O3mVyxGXMm1JIHs1FQ6tVjB82EBdOjQchty03xg0bkVIuOhsvjJhHpMKmX_xqyMNWbpFzbiWux7EThEGUbZKrsaRaAFVX89-XL_-5ZqVUfkGEntk6OphCg79f_4nee_3vcjfCTtVZKPTNL1yKxzF1IpZiqJVaDZR1tv9TPphTyG0A2OXnzcOeYOMTiQfjFyU_C8Jgrn8XLFRALIVRm4azqeIqr37q-DDn65Nia_U88Vx9rm6uj0GPbNT2hJxLfMPTZ7TRhq4YDnyBbeTixdgf1ko25u8bATw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KHneNGlQat473NIcFLsh1uNmC7SpEoI9VztQgXc1abpUbo7eChA_C_-PWHA4Bw6LuV_-0sC6AbvGuR3wezUuNrlUFJuiIu5R9u0cpTZyDqi12qXtZtZtFNOUcjMrX6ukPgo_Sb3KVa5zsT4KWEYBeo-82_x87TbWg_POnHTMBXOuTpAzyGfHoCDk-KIFG3eBW6jwd4uSnnMkvLulAI-Kxm6xUEL_l39qggxrW7PR65rK6Q8jdXx2eao9YoMAT07WJk9b89gpt8-L0ZApRK6cjRnqYb0-Xda6FDgPJRi8m_vcij1WdzFPgjBqWgf5TwWiDOR7T6XGyqLLZOk_XI2XIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l-hwB7eXofzoq3HfEZaA26LpkUp4jEn6o-XR3OxA7BAtSXp2yQ0nfQaGVk7ZwddgR1jAvpXYxNGE1OWjDoVw1_uuvKogfFl6QAL0c3rXqqla4R79cSJZJ2My9F9Yn_XRxcYh2rhQmEQf66wkZ81T6q9Nnf3EstZVX40n2mmY60lrjbtaCO8f3n3gzeVmvOu6HXlOsbkcmcSJUNckVDUICAob-rsJIu69QZAp06kntp6mAJ8ezY_RtiWYUogMF8ecD1f0ayeaH_2TtfkWuh8oVas-20U20wcE7U93YY2uSGCo1WILFsyXOO_6KvZT8qcQ36K0EOuIxUY-3i1sMFUh7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HGrcWxtdzLc4ngY3ZaiZTY1vsGKnqh1ZnAAeHhMyFc4Ouu89k1PS8Zh6qPCa9p8_dE7fkFcm8A9qp4puwyeZuY3PmwBHXP545WuZyWqlsGezsG8ryBU6gNBQlOMR37JeBF2WhT18VRTklLxPBp6Y5xw69Rpn4zsAziaYkFg1EWp90CQyCHZ96GtF5-5_SPiTvuwjfovoKVciNWYtZ909w9Yce1azqIc8owX13Zpna57-v_RVd3QZshTLUEdPPc5uDCRoTy84V15FqHzlSbjPyZAMZaY6q7iyNzdIyOm9uhCHUFmbt3p_QXRkuuYtTSxbQwAsmATRlvmTiUn0D5Za9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DjN5-XCQIpKzOX-y38_WUVtbaBFBbKNdHrsUlm8jkuxpcR3fjieLKNAbVpzoHsdD3sgUGjpqBMcfpEkAN96Qwl6IJ1ZZgrke2P8yMPFoQgAKMlXXY4h77JHvUVVfz-wtpSDe57KaAPLmzDlNV3Hzvg_-ICxyGKZ6QE--0WIlqb5q8C2PBjUMJy8akKQ2iEzVnpN5oGG7LIQRXKUPnV9uMjFwAMy3fyr35XLogW_5GSmWHgVftGZs1UPW2K7oSKYDSH5v2GSaWPF8GeUG23Kylrmrwh9P6205N4xuUuDSEDSVlcM7pFqAlRUyf9jFsW02J9MfW-QQzLHOBHN82Ro-8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MyA_Ed7DGUDXPEjOxGqZtKsbXioNi_JQOw11LnpzYaOKGnwheawXXrxnSQGA5RyWmuiDpr_7X7jmR9P6DZtIuFgtF4a5h4S0yGADjeoC0jFDxP7jirEOXrkvTeXpxcKIyyVtOdudUokYH0TfY4kMBOyXeaXne0DLZqnVe_XliVEy05PVxrzuv7LKbN0OwSjcEj72CVH5G4-PuMHfJPXc44nyYs1LhGmU2sNkRAoyKiBlDo9Q2UxaWc7BojL2UQ9GOZ29BIsfbG0Ofwpg2nGYLTG_KRdTDZEV9U0oOdGNkVE2WC5YamtH_Om5AVwcs_3a5VpQRlY-XQEZMI36VKhFSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JNpyMPj6oM-p99qI275Nca6gZtjuiEFSkPfIiSl96yY6iGGWzZUujQ0rThEGQolzBvZqgMY2x5DpIsNtYDIJj6dfIwXbQufPSepLSKFX5TtKwIZtYor0f4HrtxBa6R7wAHSCPB7e2SI8M9-Im5Ohqjvi-KAXL8W888gC8V1yj1E3qT9l8TI0UnEvbZdbSd4zcCPGipqc0ZHoVQ82ANJuu4BIQ-t7cqVm7NTGzOF_phDLPpBr0EHJiEg38zqXCPDnAzpCuIyFPeWOGOYlg5EjbxwmLxdeNiq0-9U1EiOY-h7Nj5qxZ3sjEPMTUgrcytn0YkpZCHOS-RDqUAfnazEqUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W-kCG6Qg3hIY2MgBqZVabs4Rb18Cc_8Lsj93sk_VvFsbii5hQlN1gF85ho13bE0xJ2rl4QhJs_FFt5EvBQRhWdSDszSR9n-sMsAMwWoxejBFQhtm0e_NZwCEmQsQ8wOmdWFb1S0x9m3HbSU70jCENpZFDoD7UWffnyt9CFDZtX77CrDgcnBvo3ZGcA4tNhqIU8LCPs0pU5DCR1YcKAhyBVHHW4ENVEWefr6kKUEJKT86QZEw_BY6Uephnj_k_dsfjDi7e8B-vxBEX6VyU_vnFwQutwnYUtnK20l_EKmsKwh9_ETfVxc4TSb3k3RhfomwXIyi5fD1keJyrWFkQBqQYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
