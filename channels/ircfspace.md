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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 02:47:57</div>
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
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bKjqU-sKFptK6doYTlQkXluEXKzLrHHYV3NI6V1HaknDd84voqbKzECGMYw0t22jkWMTLlnmUsiIIUN-7bEK_p5aZf4DeuUSHX3qeGMV3QfSUm38U68T8IE8BHKT8IyPHFZjsYWjd7RONNRFxSsgCi9jEN7pvhoJ9ZpXK3UjqBNpLkx_tctCpWcC9Ab0w2NrjIndxdWQs2Bn77XnejBtJCVkipKgk2UEu8MY1mX2ii_1qiDubb50pJZSFF22NocIFBRUF7B2hCBTKK2lF8Ovly5P_OjCX5BegcUP0dPZrGfhFUN4qwtthM2NNsMh5ccJmV_WVhMm2-7ETgqjQXqLag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TaKYLsWUx6us8RUOdcC806zxrs7rs3UWrbbaY6I0Hmk2_nrAaDNT0GsgzhYuL82dtpdgUrFD8BmFj2vejezCrRqTIWFUl2n6CAmf2bKvQ_GlW-AIif2Q--9wfmFUYSsy-P0pdef9giI05Oedut3AoRoa7v2foYvm7a7lJwuhyBiP0zzY5mHtT5AirsaftBJ8b0LeDS72tib56yiSV_Wlve27hkaOqakC06oDRBs_Pw-XZPABZHjLEK0UOw4Ebh9XTkjzAdFdiN2GKgCO-oyGqGx1-uqc-aBwE5CKXJBWptWs6G2v3OpsuRV2loghx578L2Apb6-eOJliLypIewxB_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R9RXSaTkVxHaC4m8FVJIM8uaBsoQcHKcnMeS3YjrPpCfxW-gksHfoegf7T6gH6PVyYms4ojUU4suELRB4WUZPvK2AWuPB4rTGEQxYVV3hhOk18EbSQ29jTrws6GWcXKaLRg-JKvU9cnl4SqUrMCw9PASCUu_aUmbpw_3YgZR-hYxdS3Y0UnSLlkmuemeMa8DDucI4JWZuMG4bHIjeY18bIYhYzbotz-_kY0xKIF9zTuGmk3mcp6rwjzG01XA5zkAQmDayzkfU9T5wUZaMRBzClRCYbcYqm4fXuXR1DtHJoMhcp5HUMXbu_bKP28LoZlIAj8Vg8WEzQD7L5lfSFpBqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CiT414-Q6XJ-7KdrhwLaUEyY9DiiqnmvOkETycHP5pfs5yyqhB3uQWMDDO-GZGBVqCzhJRzqCPQEo2C9AdoMtoa7sgytB-eXkDU0DLXyXqL1DHSVripS9JhcHO6BbfqHmhsZbtIh0Q6BGhuemik_o7htx_hGjJHorqenxhSITHHqXvj5OZ06NyIar6zlmZQzX-InBDX4Y3UYtHvqLrmJ2547yMEsevnX_ypb8wKiAGKlHkvMWVnYV9Sl-_SKMPBtbwY104zEL7dNXkYPUmOBdZKWoG2_0AwrDadBuzHeHw_fR5xEP1E7QpR2phFTWunmHRl0uacqcyo-4ZxW2Cmgpw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GzsxNTHWxiK_aa_4kSFBu27ggFxRiG37XmLFso5U7Lo2LOUl66RLVb3GbTh4GmglBJb_YgGvae8PFzG1QZ2CcttyIHsQMRfGCDcZ4T_BmnJ5wt7V64kWTf0xFlC4zTtVQBBuUsXG7iiMlmuFkh2fV08ragni2BTD0l_2B8wMSokZS4vvwPYCz2kXOA_RQd3C_py2Xr_ExSIEuj1B4F4a-MReIHopYGG0A9VfYJqzWRW-urKAHu1qjMu-jkSGjIuKkYOJiktGQye4AC3PZ_Y6tZeXFsipNjK_tQ_nG-vNKmZWOZ4EdfL7HBS3XIboKRU1BjgIvFDumCoRLk23s2e8dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RHsM8UK4KSVYSaM9sC0H6HTSHaAeiHvup9x-1IIbxXRE3pohx_sDg236BerkexTcBpLCZxZNqfdwyOZ5as2QP3aFMhhTNPkT12otDx81luLDjD7t_zqW2nowL7uJak4v-jTJIJRLWNNhWATodnAqyKYTHfMYNGwcEh917Uqh8Zo3fmb7dSoeICOLqDl2md4RD_odYPfSmSG-U92gD3M0xmCzEpH60_GIDW4AYBv9EEJ8CF27DjIsDnvArd_uBAQiSCgfQgJFKZjTNnyVcozMVhFtCbdgQzfZ6QLHKTdrwZBA0dA-nUu8wY1p-sKx-1ztWQB3kw2kWB62aKN1Wn3V1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X9mPvd_N9y96z_1gLV51c4bZYf63a3XdyFrkuYDXpAz_thRpY-1_fdFqc7plKgdKumgMNp9b8O4rVlIU08M4anRtC8TO9zwIyeOXwOxX-KH-8rAE_PAa0fu_uWEJ4pMat4mu3qcfMGMw1u7CfG4KCOjd42YwtT7M-gL4JSYz830qQfMhijWlfJ8WY98kWJ4XhdQ9eu3SNHflnqBD7CPZy9UVQ1qVKeasccP1ilE3QqwcwWaLkbG46Bv-s42r_mNT79jBzzX2n7eUB5y4r3_YPJcwKiJX0b96dYp4u0lTA1bGSW0v0SH2-Cxutmfc0-3DV0I4M62VCqosRrZizED06g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ii6hpTqXq9kR7j2-9FQwwSJsCiSbSRsyGiiEZHVqgMsvaTk_bShWp2Y6iIL5U33HdVTChOu-uE0AGEEHgZ-nplJ23MMWvut_mNnuHlBRErzHEq0r7cVvXPTRD89yWXtw3Kg9EyqYeUxWZDau-sGvCFfPjdl34OO0VduDg6fNswsYbScVdpwpA4DV-icor0Mgo_RKmgFmcZqBNQZeC9kIMYsMRpH04CZr2UnoI7nG1yLq5F4WHbLP4YnvH_xOHf-yyq-Cdw0HvgWXNwvBLkVO6hGN3fHAWE57lGLyV1GtVVGgrgvQbjVL7BYhW1IBdI5DcKjeTH1eHQM6wSOYdUbo-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mDMRupGHuSU0_7gLYdazW5cUFyIDytcb-Y_LQgxrJ1R_FovmAC0luyTH4SnHvy-tzwO4GnglYLXzHB1Hy8IflBmGJnu_cC1N0RG4yOCq_SrDu8i_HGSf243sVT4Jv5wOlww5ZanJvIXf8ukPxG0urF3cADT5Fy9WMEFeY4tg0KII2fy-NNhyUnCgY4Ft1lGVIx9Of9KziiXpVs14hj2oLNYjSHABWV5THlcv12tNsJ_ZsvCxPAZZyFTuj2kJ_NpGx7BP6IlJn5ON1KvNLlczJ_wEWWPfPdmFZpkKKSjmPdtt0jnLq9HmHkrcEoZ-54zRUPWtZKcvZooopgrZ7gw9Tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AL6Bk1UJ6rpXvtMny3Oc9WMIba_hK7tYx1zWqJYEaJ7uhTAU96wnTVIewuVvQAaTzcJBsuI_RxGiVjYwas5tesP_2lhQ5NqD2iWxYCsc7hutRtck2fbnhltQDhidInuyCbbrl4mhu6huEttLV2f_WQ6bBAgCUb4Ssbk3DZJqBwlOp6g4CIOK9eMz52LHbvLQ1cbwFfpXqQPz3ocGH2bYbHE3JS_LiwZQeJgr5hBet23sDLzvD_mYBHOl6YlqQLr73gQC5Bt-FZYVjvmdrTqjpEHmgGUs_TH9NVv9rbNonEdTiKU6cSZ1AbaJDiwjS3EYqQvz1_2kiBp6m0AP7z8a1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uuoo6FJ799qvHkN7GWdsO7g3hPupnB1dF1En6vW89YgOYP_Ug-ze7VOfhKvrS_UGiZw6I15ZgQ1zs1spl0X7SUL3WIrn29y9w7dSw6lLqnvy-59xd46AfX3Q2OlZdDhQkSzMUhECkLtyKUwp2HKtS5PE2qMik59IoJzMPF-SqDBzQHV3iooLfEQh6dL1OrFPswiMNcE1Eu7vTxPUwEF76MxtdFIHh4vPCJsxvic_wdC6XD7Uh7w8psfaQ4_RlER6IrSvF9YJxqkN2kG_crAUQ0va36bOdC9q94k_2H18t2a8k3DmW_-vI9LGr-M3egCRvzG7n0xSrJKxGnG3-VgyaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sHavrOM9BoZcN6ulGalwX5CJJiR9amCG0AoKMXsNx2JWWnx1a1EvdYBqiLvm_1gHaqeF7xCDpYxCDFk2-UGyZY5myQAhJO5kLA4Z0bcpFSfSBF6y6w9EOzxbVkXrLsNqLgD7fRqbS98LpUR4ELI-AmS0ZCFiiPIIo_LvqVULnC6jnBE_txeMCOxYQ7i8xah1Qbta1PScXjvDRmCpui376L8-YKvXs16ST70OXwiTEOOGYBsGc6clzWNJ0iElXzjlqkf1JzKrfzEV4xhYRJeZYUKoU1mtNJXGpR7_BI3cbOops4H3lrlXvy1sEywbC0RyTKyDU2r3b0UVURxIEADyrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rnbi8qArZaZrLACABNTU9GwnmOHn2Y4p_ter0lIkKVRv-UCSiF9LYP2_FJkwFsmKWSa7tZEv-HZoL83sPc3rlZKPKCbaLhuwAzIm38_O_fAriWcNXFdw-SbKNeF1Pd4UjOTIxDy9QOqTqNH1PHSwu7PwHPFYjyQ4oiyYZgm7DqmZPcc9jlyI2muzog9BVdcR-OM8SmC1Dav1OLZfySBOtb8Y49gGXy6hxz9Z7czfO08KMqvQkJ4XR9gVIJX2dk6MhQybI26_v4OSzv8xxQ-1whswDRFYzYRscI4cjtF_DC9N2llkBhKEBcSyU9_qsrN8yUvlgMHPh0ep002PyNu9BA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BcXoBVrmWeofpF15wO2z8HsnHr-e7FHYKs_i36fJ8UNV1SwxmCRNCwLX7EnhXQuQB-4l051-HbP3dRxfe7Fnb8UhXy42M2DDrabss6wSyRdcHJXKVvbaVGHPrRjvzVuOfTs4kRVwu2S2BeRySjJXt-fsCbUqVshTZmGGMlpFBOTKOM2SF_nRgi3gxH8Dp7_EXHIefItwPqvhNVYw-wQodLDYsr6TLdQKolg0qHhHw-hkYNiD_scV4NL-9sC3UCZnm9s9p7LkSNMIWMD7yCcGv0FDz3tuN_OMJuhnNZSVEWqSD5_wuiXY4Z-usqw_Kssd9b1ag-anKe3HSK9eDb4rsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vuFHcBNSKiw1Kz5ANhNoOV2lY5dH31cUp-MfLtYuO9J32OVi5PfQ6iwKePg5z3-ZlOOltKrTddWNEw275Ju3sCfJSCJS1WrDXZeQUrku7LtQxGSegN4QuLc02g6xeX3121jgA7A2Po5EzBBAoay9RsRphUNTIzE2oPNOaASgKFOb7GZ5CKkQmxb8Kpv21vHRGclSU6T-dm_X-xxrHTE5daumFoQ9Xe_k1xw2Y0KnPE61PgEdwZ-ICOyLSuGfYMQJ968bN0DBNQDj2TBfUXzmYACHhskM5fqNV0xsjgpm7rsq41hy7gvnYszANmE8FPOfhP4J1DwpKJR9omAEjyCw6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vAwrw3Wxm6kd1QRw5XfmJWz8Fi0_4T4jp1A63XbyhJL7kN1WY5FBuXLyKDSlu2R8JWMBcKLWrEVM_UCkR3mKhjKql2fun5D2-1zB--CliCrj9qy9POUr7EYp8977kHPbJJftKjzWQrnKFfcE_aI87oj06O3oKti0eLpA8HABcU8TZmA4mqPf7TM8CK8wqsUmhNkRSMxPm2bGwOFxjlnN8FoeedtYTXQSWmx7fs3kkhQTFQiI0pDVoYdgo-hH6eNOAxtjs86a2R6sSowJa8eu_p3ECsSW_OvywKa397hWrqfcml1vjOvEZhwCxF3S71VAxFYUefepRoMu04g-BE9zUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KptoHiMqqusOBrKALbQQKjxKSQ_OTT9qrexK6Qzf9TP1xgaIyaOXi2Z8QyI2gKntu6_wOwm7fRbr9LwdafekUHMbepDt76ynnOB_zb0XrIp632W3OFxuq2zpYNiJ_sTmG2oy4YgzU5jI4Y5M89m0WeBbpFLH7LYzhH6XFO8Cq2NemYtTpNlYjm78AU4Zbo33dTfNsGnAwBeMjReMuvEARuodfAXEgQ9MlHKGtl0JKq7txpkJ7PIuJKaXY2m-R6-4EjW-RuwPGVeBPwG9ktwIOQV758W6CdjBZSjwbJHHa-HnVRmeRnjapod0mLJj8yhU9-wU8WANeyPMfcPBdaB7ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FS6drUG1P5NHQ8oj3KIk4JXWCn5CADfzrfCHey3OmH5rCvuJ-LBsZLU7OYy-Gjm3THaHgtBIx7dQ60llFkdve3fRVKv35tAaSe0mPE-mpm1YX8XNU1deOhZz9me5kJ5niUBneIu9fiddYx3oT_rn-qkSN-z-0jjSpEBkzUGFzLa1VZ-NLRN5jgdXD_0Aow6L8sPeoX5LcwMhYGE09MGpBIxVCOcbbyMUzFtKFTmLa4zgS92lvmolHj_g6NpPz71NjkMAgWiD6OoKL1uGEAhvVR6QxBcGAWvGIf-MlVBQMAvjDgPxlkcWZLwM7Bxn09oEKUkMRiIcU4mVdss7HHx6Yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KYpl7yXFI-9msD6vzY7URNo0rbai7ck-j7rzccogo-T4CoyGG6JJ2ySwiRpPaqCoaYr594p_O0o0fnB8fxtHjJFaphbjRt07xTdHVovUdHfNjdmrB_mT6ifJcuJyhjtojxJ9gyMsxw8bYLkbIpbzfr0bM6XiUucgk39zZ3LZVUvUuJZqQjF6w1QOlyEzGsoGdmPTlQDW5xIitqe09fdWCeG-nuJFRX1RynjvtWHH7gVBLqKGE9oHCpL4Ib59vUxsZObuMRa4_HsfxkGPIIYgM7loDjUhxczt7O2ff_PLuLeIk5Ajbxf39e6r827ANNvNvbFZ_DoRKshuxUvpo2A68g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hj7voQ7MKfG37Kv8taY31XUA5erxI6Xz3lDk_zdg91OlmcvlJZSmLaujQjU34v4duxkrFX3Ks-itQy6dTaOjaUdJ9fCljYorVDAcSo35k1ZQybVQKLJblGxsSB1FBnYvEiZ3UtqSCLOshJuZsGHd3-qgUlLI964r0WUIVNT40XzrwXtRfas2gcaCF9da3BJpv2ZiHBnhQeGCITqwxMQKsaPnqbYz7-bvanSosJdfn4TQewezOcZp1-NcHjtrXcsutAl6FyFBZ98LzbKhj58lwPiQlTnCBTvZ80MHmMPQ7CbXmBRjhz_vawgwYodkHB0f5YsX_RPB7BZudKW6CGr9sA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ngqg8PnmUwRtH1_akjZUSTreksQN6kRSa9qmlKAuvS0w0ABiZnuJnpyxN-mOxlF_buW0U1gDGNd1PlJkQ0kV6eatYQrUONyaqvXCJxVYFmCC5FZvYfeIPQWP9mxjAKqTKCOhGSsfyQEBijpcIH-wE6S0oP89_9XtpDp14-ULsJaJzyzQKU051JGHEvKWFaSOKby7w1RsZxUYbU51ze6HnkCDrc8wjhN5VtSlwGkQrHs7RPiys9zI63kU1O47n20IgjentGPcyNU5mDUtXtx27wc500wGGRywddIiK5_00u-ApmTe8a0LL4TXZbJkDaKyZqLYvPVF1edYpOojEQNihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mxxOJkoiNHkpKzxXMkQ4gXrspKghe4oNopvvxwu7vLMA5xp2FR4K_Xn9ZJx5jBQEMJjQu8bwzuT5LMih2mK0Gmoao05s4IVkW3i9g5rvPURlMPH-FFEW-J65FDK8ntU0mf5h1EvDHRHCKdLiSifI2wgZlM9NMAueXCEIfNL2G1S11KRHgYghi7E0udYrKiwjCiqbKdfOY9jW-eCqmCEL5PLaNqO-ItVbERvwIUqqPwRbT6heO6ultrXAUp9AGWCikr_cN7FRf7LY4MdWqEuPM4morgE7xiJHTBez7lg3lY5yBJr8ZCBVf0t8mGA-5g3VWNRkBsNkBe5-b6U6YjgLvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JWMsMhXH95ajKrAaAZaj11XBv_xrj5-gJGc5eaEN1qQyIZx1u9CES0Rad0mp0yDKcxsIatU2ktUZ-P-5GcNYUThPeimcOXsxZmnhv4mqQYgzKgLVa9Jsh-malpaEDGe1kD7DyyrAI_sqYLpm0opWnm7nVQ2a3hF21o-mSp4ZH3fXIik8XyE8gHdkoo42gtS05HAetGu-609p-Lt8MEf4cLxypNeHO6OeV0PotaWGbHIvsCkJLW4oFQDn2ZTvT1onJzN3mZk1RtqpvJuy7QaMhkqax-a3v2ic1uGIKuftO4zUzv9XE-kA35FArr--bla0A-k02_wAyWSsppzm46ia-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q5WmZUnZbNqrRa2uiVUtNlc3lem_3ytaC4u_SXEJ2HnupL_kIOnmz-q4OInlZTlvrb7Z56_xKOdrJKUJ7ar4Y5Y6hwm4G1Yu-tt0OU2xaICVvonSlMZ1havPTXg6l4OEEslKZP2-s6nwfSN4b0d1D2EF_5yB1Z6nKOplrEs8nlz30h5BWgRF3K0WFhB87OgdSfEEyMFP_rWHRSK_XyswCkoZb3xhpldfr8OJl21igRTFHe5KfCQKI5XW9qwbmN4gGh8ZQ9Obb0vClL9p-fLcLf3pdH4oOqAIipnvePeloyRN4rT4fAcwmhHdJe8jWsL_OhYIolK4T2a6NPn3Og0McA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kBJhnHbcpjZ_hzL2ANTlGVP6ujCk2hGi6FSOS0mbQ1fEykjdqklGAC1NJFGySL9QCuYhw74b9kqIDISw2K3dtuQdZOCgcpg8P-nw6N5WeN59UPUkU1TCfAeiFum4no2wRyOpUqvrAmHIp9HFmCrAEvrZxn13cVRXYmAXF67jkhcdEIt6e4qkujujg3vsPLNffHJZ7ce28sddioD47emyB423fMy402Jt9G1UJyC86GaLGHnuMmfOz2iJQGYCMY5g6SmUfc7pdxqu8y4IsZT32cGw-5GyHRvx0rf9MrWVcp3qj9ELWcGDfJV_hWZrIzpHHavy-uTu5Ztyt4-LX6pC6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nrGQg0DLob9vBIYRwbnc4S3GYGjj_bJ8jQfYatMHhW7NLZKBfDFg2ZNt1Ttpv0uHekxMhFDxdDhEitoDe-Pb64NT0PIk1FFv-cSspdQxMbxMuhh9o4G8BqRXqtCPhT4Bk3uRQbngUo85QrvSw2-2hmXL9LR1taMDZLzFo1ZstafrddtJWJHaKcFGlB6ICQEmnfkj41Oc6yIBi48mtHRiUDQsRjMOV5XpqrFxamtXPeqh6uJFwvv2UHNYMcaB_HaC3jpzIZ__hhoixAh29mpdTxWdlEDp6z-yIRtWcYEOeOBS0--6B5QPPK9EudjfS88xloSsENUCZQhPQQuSOzE5_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uij3qQNZOV38STTRT5GK2Na44dJv_7XETQUT1PRwoS0dafds24RrBZyMhxaCOWYpgnhv5cKq0RxCTX3xvEqhuzxYC7gXiNlNUH43dPVffSDidO9pYLnqC9bAavFjSvOzQWJQr7BHDbLZhVGKo5qcXo-WwbzuwnqgSnjSvoZDfwi7KJHxq-Wshf2Abs3rKzeun_luIVgrfJ7HJ0Z166zK3YNajNxXe8RhWYB_z4xVAQbZz2VKpGUqC7YH5ifxklNuU1pmcX4kitKqD_velcIjPF31PFVu2oKbi3O2kY1JUzHJWToxPjHe-eMbiasdIkuNm3aFe3qwYKxZiCDOmH0NVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DRc0IRE8eu2aimAYL3Jx11oNJQIjrtFEZVL1xOvbpP3MMjSBddbCePJTxS1bUiDJA4AYwJndB9R32ujktHC2rMve6ch4T3as4Ink5ih5_C2iYi6eIHFAt9x0RDyRigLcuMuFWk6i_94ZXZ1aEZ9mFb5BcAEV2yBVokGVdpwDsqW_WiazQi1Z1A8M8VbQmWq2IqpB5JzxFvsCX1RpNbvKVFllioD4nHelYj4YUn0Ik94O1FU73IV_a1uL7G2kn3JTo0VPd4qdPB1TH5e2D4mld0BCa5nSPjYdvE-FTTxdoEo1FcErwAmufb7_LWMaAH6rsRpf9rq-6n5M4LjRUDqw8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b5p85BsVslaOnqlnxqVGStnwSkGyiH1xVcRb0pQRV5-zz1OOlR-5nxEuX13SHFx-vxgMLzbSqLHlMn-w3fclbrEsBKter7eCaU2dk7V7p4h2saXoZMY56Q1DrcCcifJnPBdyKUQXBO5T_vWv_F5NIRLwwdkAlH2s9qyCc2r2IqEsrVomTEcJ670ADS0H-tJdFPYncoOpHz4j0SSgN3xJ0x2-CHMxem_mwj5BNKUfN4ldDbwVmws89cdRSNMqr1KN-w3qG60-aN0zKV1boXme3TSH-sR7NPI7w-M_LNHy77dq7_wweBOlTyXXsL9cjxQc8T39wgk5bJQeDTkjxrRbnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CLMdUIULs5pRN-xI5ewPBTT5IAL4q3CpzX6C5gUmvv8mE2sA1xFgxT97EqM5MgW96meA8xr4jjhIrJlxc116db9KJ-eBgaNdwL5mVZI1zEQlROUrHjl2spwnyJh_fvMkoBt7YdrjdEJAlj3abYQcYPBbP11fw-yughsmfRGivDiVuOqMecRmMNowu2MiJDQxin_lvklRb3DY3e6bAxwYjZosQ-a5nmpXhi4IzS5Mp49o6YI7Rriw4sImMtlSQ2DLAk6hIHJEyeW4xmcjseDxBWDrkCC93JX9Ik_2CFwx0LJvgZDy7y9AudjLYR66LlnF3xd425amIVKkQLl57IgLJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/esBDV_hi20Xpms3y2ySOXTcJvlytLREgZR9VrRoZwgW8riqrPVDXBeqk2bceuQKQtl10hfRd-S0qzbHcnlj9iaPcvLifEljyhvqZS8xxs-ewPWqYGBGUmNLBMa0GeMewIn004Krrbaff3H1lTmhq1Mz5bIjXNvPj2lIqpn0C1PMSFrDubhRsxae2uEwiu38GTTUk0xlc3NrFNP-kkj7DSy3Qm12qTA4O8ek_dErdojYdQayRAPoARjiI89AFoyzR5R8Xe2nji5sdtzmMeujiRbgOjDIduUv4bHqJyEarE9NBdbd4bM6nWaLplhP0Xyz7dXm0_eqsXO4linUMUoE3EQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=gC7rOT3sSoJsrq3BNirvFLiMVgEBhW9KWf8kFZraXkqmqg8VdTMwV4VJvoMlSKBcUrB2hnM_ZuyJdzW-p_YjZv98lJjrAxLEzm3ChtnvHhaTzWW3588WaZ_KkjQ90XJ6YYOgV0mTs7PHIR7JTllgL88Hn8qmbxW-HojrFvE-JtrkTDSaT15r7o6RRTlrXJR1rSw0kaQCLpTtfZtnG8moXjLOBrN-0H0fsl5u2boRBcAnHMOnyxHKk1TKDwUKS8lo9teUuQyCTKasRigS70n9ayGE_Z538FUdBnMpSlc6c3-FepgNSBoi-ieA5E3xRfQBFhc58R9Bkq1XF9GV2dstWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=gC7rOT3sSoJsrq3BNirvFLiMVgEBhW9KWf8kFZraXkqmqg8VdTMwV4VJvoMlSKBcUrB2hnM_ZuyJdzW-p_YjZv98lJjrAxLEzm3ChtnvHhaTzWW3588WaZ_KkjQ90XJ6YYOgV0mTs7PHIR7JTllgL88Hn8qmbxW-HojrFvE-JtrkTDSaT15r7o6RRTlrXJR1rSw0kaQCLpTtfZtnG8moXjLOBrN-0H0fsl5u2boRBcAnHMOnyxHKk1TKDwUKS8lo9teUuQyCTKasRigS70n9ayGE_Z538FUdBnMpSlc6c3-FepgNSBoi-ieA5E3xRfQBFhc58R9Bkq1XF9GV2dstWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pz2HoA7HcvMrSRlGjGxAX9TWdEOODiZPbPVMFrZEqpvN_AHcH8qLlrrkL-CfcDt4yp_CW7y6Zmzs7WO6B4bTFre2AHeRiteogUpb0Aj2oa1cZXKEauroFYSpDqlukfqIzrAfCB65g8M3epUk56sY5rX3o_vvZc3hNqAcYyqo9Drv9ilFrOsNYnc7q0cMgHy87DP9CeD3tAmNZhSogiGFoD0aWZgDfk5mHyNh8YA8rIonNZn7aGg2lTre90TLXxfHHBaRbTZq60xYc8Pf6JkwhNv1W8Uvjq5PhLm_gqdMs4cMHelA3A0y3yR_DrD-waxQhD2DrJUVLaZ1AFwCEk_ltg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/unJFp3OWeEzq0G6RsSvaxfeJ0pgHve9Ys3HVYbRjWuJxoM45MSKjYO6vrmudtcfm3lyrmh38Q5zLD3xR3f5oK_B9DteSP9TtTKv2rvuWDVlv_c2uOnpW24S7jS9pTjx4TCa1iULPcTnxEuce7wFp95SMvQhJ0BHh9r05wXN15MTNc1xUvZsgorLGrRiygc2LkLHPcwyJyRYoevFiE4UJEu453jok8tSuGs6yECY59l0thQ4nEZjhkjSRqZi_5JTONKhWh36h3Xnus2mvX4K9S_dEBMZ7cYjCeYhtWlNg9ojOl9SP7UiGFCtRUIaKyKqj38kDFtVmBQCax18ZQ6nUfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hzAIbqiWK3NTUUKhPm4tTtk7XKDXoxzjKClWpvZ2S0Ac6fvH4zeN2bi71FUbJBPSJOZj59-TWYr1XKBiCdhB3jVvVYazui270TJhH0PDCc7bpROiixu9hHfsTET19Yy78slRDVWn-8Rp8dBcfJUw0DJs3dX-H5eVNIxFwG8YXSYMZ4kghQkyf6JY7QHf-1whGgcquARWvmRPc_JQ4FHkpTNDLNE2Cks6GP_WaQumHGbtwx0BRmqxs8sN64VLZtxgM19TGbkd3D4xZybtHfaUuKEBNX3690zls7dcFhi7qdthsfJ23-kIJP_HfrJwwYAPowv2gHHnsPH2rtvoMnyNFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HUGtiLAajTrZg2sdLI6deZFnU0mWmcwB535simcF8AqAqdk6cs9BuyUPp5r4pPXlBFWFtWROGWevN1pm5QMDbkieaK_WzfNo0z97Agm2BLALN-OZzontuj1TURLZU31FT5XNcrlRkgmqyVq21ItzzVWIT3uunZ-m-F9oubnjPZnNrWNjh5noaIhXwNACWxPzmxZZEsvmbAI6GfTw3JaAwF_YzVthYetHtNHB1VCB1EjTapxpteRbh20UlZL940UHVSAaud-X5CkkD1zVdz3hwBIVUofEWDfKlAyvE5mvqZ2fDQ7BSE1AK78GtK085gOHx_P5CYF81alaiB4oSpQoDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GkjF8VXDc6kpz_lZcK0PGl89kQQpkPZmF49Qqd5N2HrT9PQwbbXIMnhln-Unyuq-tLnaBe_Pd3KKMIncXu3Jk7apTFf7K2QSVHIk9HecZkgUkHR_KBfU3O-NH1IVv_4fkXW5g0Apop05Q3ViQ20lmunuTfs015OtYDXlvBUQTK8grEqEpM6Pf-k8_39_noyKcpXtsvHOAR3TmPtvogSqz_c-Tnlm8ejuPMtI1qHe8rAiTXu_lF1KTPCY8ZwsG5GdZGAXuwZ07wbYeqXb6uEiqUs_L82xpLNBX5_ttFQlvnVYc0rvYfTVUB_-3eQ6rX4Tkdn0QGbrcv7g2e9sto0ecA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ujQSdMVTPB4N_WWJa-psw94tGpZAK9akNvoBKKX5MM1E6zFeUZB34V-vUxtk9CrG-h69tZur13rYomqSOull0SL39QKF0X4Pl_amvWoV1yV8fK5wRof8GxtNvM-tNDbK0a8-9BvfbOuWcMenjsstUSnGQTUrAzwY0S_PT6Zr4y2y61uK6pHS0vhfgeFWDq1_JBWbegv7Ac_OczCRfw1QrjM471mxhS6ADpejN3wJ0YCqBxNZ0cGZU9_k8wru6OrWjUwvFPcVL_JDuzzCdx-0afSO94Yz-UciPwd8YfdaLCYl0arX1uub-3BL-rErml1K40owUgecYHmb6imRk-J4YQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cpaIAhxk8MuOyQo_3CyMwxE2942vWaHfShaehCBdG-AHlKDEo2YjCIoptS86K4YmSdy6rTRvjs0G9E9R4JdKZCDX9MOucfTgYuTEwGnfbcdW1yT5-YB8TxggiSLYlb8PDwwn35nqsEPmTcuF7pe1mmLnlG0C-nSPcUXAojYDzmyKmMU_gohwAcPToCyPGojqFWgOLu-bBAhwmXYA0up_Bc2rQtfe6TXYbySJekFMSq2FzUhfa8mE7vmJvN01v4sd8PyouR0eHYs76FJ4vOx0bZOh5GCONAinn3FdKRnczZBt9cS1Vh0i6V2DakcpW2LoJOaB7nblpe85RZs7TSd71Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IepzpGsq1WYa-6ypMjRIOrPxUI8sTD0CnO0kI6lOuBqs8uKOUi1GJ0_xKKZooDnbwwFpPrqzsdfIrJclPJiyjJKPs2nhwpfZ2vwG26FAoZj7p90kIRT-e28eeMPadhS3AG065wtyxqqLXHYJsgWoQxqUy8uAjjDilpElNV3yY0iJ23zomhkmApSbkNKpvruvKrzcG_MQ3QHn5itBNbM29dQzMQPehMKdXF2dMYjBzMk5_6HQg4YrBpqaQquwhWEdaKaGYAMq_ZOVgsTAcqs5n4vhvKto0I_280f6pHpeNNvGOvu3hDNar5BcLu3QcIyfO-BHmOGKljaJZZ5Y6LYylw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/muRU-qi_Lz8-JctDjxLqqT8Dpvdnnqwr4bnsMG9a6RVaXoUa2FAzsQxDesnbccSeixoMrMEsvDFvAIsBAKb66WzTcl62lAGx9Hj2FnyqmF46DK6fYw0QDMO5_XqePRXkyWzuGXLeO6UYltg93dNUR7yCwgy48KWLIaJV2qVk7_iNGNwi4SzB_KV1xuFwa5lwC9bltz6yMgHUSB9EekjD9jsnn2hWzt03_Abb52nSt-BiuXKyDogmkjefXMSKWQ4MgR5nd3FJeJo8e2JmC1ymBhFKXXAaeHrHDPkW0uL6vPuG1Cs8ZHJRHPctlPnixWOPkZ9zJFXKCkIl1BIxD-42bA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JqrQ-Ub8HaSNULsmCY-NBTd0MSK4Qt9li3YN9rrq70NcqJ7xoyvkOhoEFWmJyAJiZd9Qz8zYpXW0nf83Uya2R3Gtmtuy18ZqAjf3eTMUws05vFfRHiGf2sBfHBOf8rvZmWBedNHzLxNMDyWcpM9dQrFtdGW4u2y_oeaMamDFm74PVn_kb-86d3XRovdMJq-YFcBEknG8SgKhCBqOYClWu-I8GsbUfrXj93U3QGliMOHoNFXMS-ncwOzuvhtuufcXMfJgDNfoVpApaqIAHqq0Q8nQz1pETPdVvCSgNNgCtoN3uoAKOzQ4q0zzv5nLKISj-R8wEVYPPbRbGO8YfqQseQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vNLRn4UbNXjUTv3sMqPjlmrKS67Dx6u3EvZUnkzp1CvM_E0MSS_bBwZKUOrqTs9JCPqGjzrI19zXsMfCMt8cRXBr_1uMW98ECr6toHgKQUG4i7l8TIfqQiCqFo7Zw-BObriLhSUcBgglsv07zS9rG98wzr0uzGoXV5fZLQExOUmFmUPn5m3SnlRMOlgass-CusEdzkdkkVJLfkjN3qOIsDnPUqpuGhjTlmRKBGDREOoEmItjHtRHtn1D_S04vcfCeL3llbXHD92iV8pUJMGRJ4JRSWNmWB3XcWdwsKGV1KoZZGqtvZlkSu745nu9bfip_h7YgjWOchr7H_DY718TDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M9kSSCaAttCiuUvJQNj3w-DsaeG2SM1wpf_uqzrlWIxuUepiH9ulk1tlKclNTjeiaFh9bo1V5DNXXxga_9II8v-x7NX6VTcbrTSDTrwibM91NAYzI5iThXUoiShtKy6Oa5K2mL9P5wSgHyHxOdnHEIIcyp5OGrN1kgssPNcbsVnC_vtpbxgd3HP9CYVV0oHxTbtvmdXdf5p0uqc8r8CmffnJac7UfsGuUrkmKomqyDadtygP0KCgrJjMAF8AccxMyH3LhFr6f9JgBpMCVrLgF-LHaqrqka29nalCKATyj-b2zeuR9yK1gFguthLTwlx9J2hdu1cSD1479jlNUeO7cA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TD7fPtbwK-fRIwmd-5fzn4NbKWXN_5BiOZFRRzOjyYSZ0AOQTgG0wuggKNyoYxDsnZeQ6oCm0uamoZS_dhu4KOsUII-RNVJ-PQwdoEFteznKnxCSDDmBTm0qNbuHd4XFhuiazMZh7AyeZBjiBMoA8D1L5RqfoWeOO95NVt1_e5dchhjgSWT3rhg8EG8BrV1iiOf683Q5jZgPpV0B5Tef1Vp9IINDTtDQe-hf16pwyqSCXWqSIwkyhUvCSP_AbGfMD4JWg2LBqj5WG1DuPikS-OraCK3HN5O8n1zZaYxYB58IFM_DXlPHaGU3Oky6AmGbAXi0r4127MJzfoPEbIQVrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sf6v24F16Zh8aMTFTButETxROxdoPM7VRDPyhtJeE6NpZHu2LRoX-4QLx9AWI6DxkihnKRiMsrRwU26jD2lmoIC7RpSfRiIaZiiuU2zUiQjZJkRaAxykwI9Eued2RfcLKno7185uhz-fAtgWxjS6Ri8JZl6F_z2P7u3tSKsEp-4-bTQ1g66XS7tgg32zS7n3GlPJa_eEvBV3N9T7T1bXgkrbQM0Uh6gqlqHxATacFH3gG6mqdOfPVlqV9tC4NRcqUmI-wAeHUWG8WZKskxo7YUM0WLY6ZvaiFm5SDZv55cLDXjQroDX-g6o5ZI8E8K7lSyMDMbZnwgApih4BoMhIvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ue5C44YDhdSpHsNMAs9rmQ4ZBHoSXLbrNcBKFIwg8oqFd6blcn0pEhGQ6NKINkRUoXv5IzJvhzxkV_AWgKgiZVH44dWZE5LW5kPuH9ynTJ7XLODXpICVpjKKkw5w6K4MF-YRgztGEOnqU9pou_8zf68teLOXFsifyMgFOXTFAJxFQB4uH96lKEkrk81L_ptQSJ5L2nris3QszzGuWl-EhL7SxVi8JG5IC_6I6ZyLMRVdEYVw_HHQzmdFi2s3jU899FyGNuV6Ptow8sUKxyPF-cTSTvF9IidhOClNWKP-Apldo6S7RWDQ0WIRSheprCf3l0dS9eIcrqaSlP3sSXLzOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
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
