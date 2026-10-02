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
<img src="https://cdn1.telesco.pe/file/m0BZc26qeUYlrUM5n8nucJTHTbIw760_SbD_9Z-EHcF-Ey3l1RuVtXRTI_cy7Gvp4F4UVQwjTkpJUJqVj0FXSSBv1k2yldyGsFyoFIX6azoMQqg4IgAmcaI94b8l-ypG0wDO7NaIo1GmsX8W5FmCJVwZZuYoMESPxchyPrjngbZqUS051l5WWkZ1SXw38XJC3hN02FYOXv3nuZ2CmrJgBXlreiqLU59l4GL_1_NV2SQXTVGWAj2sR1VgIZBmxLRcHrCktGx1oScu2G3B_77LA6hPQkTqFyMXSb4zo0JqD7_27YBSqqYjVv0N3bUy1DB_5NIXyazK_N-w9L-CHr79Og.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 95.7K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 18:42:43</div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/ircfspace/2633" target="_blank">📅 19:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GiH_mF8vfYh9h0xb26JBghonPOi7Vbqq7uJJhGuzx5vmmr-zWxdIxaaTt6WOE5Ktxz6-vCZcoZuZrhClaY85RN8JLdRMiIX-AyJARoEQEaP0n_VewLXmStqu9EDMj-zhnl0pXze8geqMmO1JCB1oze7pQT3_vvMl_s55vQRz3w_LFxj6FvKGfMjK9W-WYjdZR_mLNp9h_bnku8AcuRziDg5F0CNiJ_yHK1YbkxDJOVYaWLWizuQG9RB7VMpgYnJABftfIxlUoo5JpW0rvIEHtmCHScoVQFLPKTTdMAFkuPq6CzSS_-FLHybw6bHksKvghlXfftylyzUsbXPkE_1Vlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/ircfspace/2632" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SaCJCCzBEmRswHUo5JWQL5GsEYl_ebQDFOjCnDQfU-MmMEtBZWSZbNRj3004Deg9yTl9V6CBKk9NKHpDwxtVUQUa41tuYbg0Bmidl4VhTW2LpdXAEXs6YoybdBvV6PZION-OwLT0BL9PqUH6efOIaA9yzuZ1HwA5fHR23gwGb-7uOFBY5wxczubxoRIyvLxYXB9IAdsQXpSJ1VvmNakL2pHBkuPvnW4a9HTTcwB4z1oqgQBC7LLQhyTEqxVb28Zlntg4MSep-EdmLlVwdcuIIbx_IOC-GVPdsRfOtKaSpxw5-ZdpI84H0MUX2a2nyHd7cFgHi_h9-oa8yhXBhwHEXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/ircfspace/2631" target="_blank">📅 18:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W6TL_Bn--Ir9_tRgLX-q8tE3WaIfiEOVM2w5UDMd_s5KxzHxlNagFMzwvoleMAggZ45Mudr2VyU6m5zOj_E7_SlZJVJiEyT4zQ15tiOzPhJl2eoA0cM_6-U-bBCG9tJOsWInK44AhRs66tpg8q4s08dtWKSzYg7u2DYK7qty5Q4U1wdJvBl5v5ernGD2r-XfUBszzaGnfcUDv_lBp_AWKpneGYo5Wp8GhNq69GMeKNCmgbzstSKsn3eURNjn_51X5rygpjg0rqCOv-dYxRatuw0qLlnYcJdr6HcxgGLHv9Agw0CPOSEXXoItz0gUVwGP2CQ2h1BOm9OjsNis-Dwqvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/ircfspace/2630" target="_blank">📅 18:46 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/ircfspace/2629" target="_blank">📅 07:37 · 09 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/ircfspace/2628" target="_blank">📅 21:06 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/ircfspace/2627" target="_blank">📅 20:16 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/ircfspace/2626" target="_blank">📅 20:13 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/ircfspace/2625" target="_blank">📅 20:09 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/ircfspace/2623" target="_blank">📅 20:05 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/ircfspace/2622" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/ircfspace/2621" target="_blank">📅 19:52 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/ircfspace/2620" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2619" target="_blank">📅 07:48 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2618" target="_blank">📅 07:38 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2617" target="_blank">📅 07:44 · 04 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WGUcfB8T3FFhJzWY3qDwYn9afrPWmLZ2SmQhkUsnsWbuddHFd4tlffQJcOTkbQkQZNuFkDeUfv6nW6NBt26uS64Xc1AkwJc--1sT7DO_Ti0tWzEcV0s6_dQY928W2eY-K54LYKGE01kb2L5Mv2Yo_ziG_4O__A7Iv9dL85eYTp7itsL2zMZpdy1f7qA6A8m0bmkSGroRDyMAKdfImhzxKQw4Ac_PSZBXZ9E9YQ--PqFWAlhubXYNbHt2EfhTIRayLqEN4_ZqcRm15YR5vjGV9DVhwKc5LHDxf0aq_i7R7zrP-KW4Ppw645Ecp9tuMp3ZDkWe3EROYiqUC3x_GoqUzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qf7fH9UU_sfB3UCSRIPVrbq8-zfFnIAMQuVx3OWmxW6zG2NV9tCNO2xho42bjntpbCdrA9_ProEGbFJBZfoFuxgk9ojrMUJlK4mfqMwol06aPQQRdakG3_E6QvhXRis6UYHP88dUDFyhKQeL8jsw0ZPCABhzG3BPKm7mjeItFxYpm7Ts9unyWAeIB5WzIHZhvnENJKKuxUDjwU5f5uS8sFfermp-aWco7FA1ssRkdWSeejw2SC5NaSwHPpWGDXIio6xv6yc_-aB_6KqXPJbFRFh6FutYDyI3qJHHWNh0ckrLcyeIbNasly11h-4opcfEp8dNj6eaCVXDYqrwb19jXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QUAnS3EuZh8ZUtEMxqLRoOJ9-xPGQjiBQ4wr7s5-1BMns9PYxcvAmdg49X6fBfaGBd3eTAdz1EbwoGY6Z58gtdx4iDjYHLEONpMC5wzt3_lbHx5IFVQt9OC1sfo5v3gYIRgU89_-gQbOLDXO3YES8cZi-kDXAu3y-l5r2ZPUAJu9_ziP5L1iIn-vQViwLJgprjx7wbUNFAsRPA8BwExEJ4XbJs5FO0DAxnY6EdXh7t-3cY7MYsxXW8f3zDJkE81InyPLKJ5u2P0Jl-mAyRGu-oh2tv0hw6Zi3cee9F75UXJkOR7uVjmyR4kWaBAuOp3T-sGv-CJ2CMhY_2kzq4_ynA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dTGGdIwE0By8EtRBBwSMyAcjDT94fwLo85ovixzsFmwegStfOWxPmJyqi5ROgFgELfAdpmfJvXylQ9oHHvysUycKOXOl8BtO0kqDAUihknwOhDAz-9PjM4kJBP9QtSaWglyrIdETwN41-zJBHDIyxWuHzacY9lBXqRzkz8AYaKuuxkJ0g6lBFDVW1dhuqQt6OkWW5YWw6OPBb88d83Cq8F-QiSVScOVj2WMpecQJSPbCCWeXITfi_NpZltJOfztRJKX4yTcWYqjpYmSTR8kIc18XwZ3ru2Fn_BJwf_RFTVrwSqVtf8EDpLa3g7n1mq1qNk0L045WQuC9-tE2ULx7Gg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nzGQ9ygekTFL3xvNQKBJOj40GFFYUp7ptfxDdQDTSPxGlWSm8TQHkpNYAslRmqq3jlQHceTPy-aaKpV_ZCPiMXNF3Xsr4nv5glBBZGmV87mKFDpshAytt9Rf47SBcx3JIEV3gWWHufXlp1ez7_HEoLkT_WEhXl7KA8mnzo2uuJy5JB2oSWYlf5gFJguKysSI2oHQCV8NEFX-zcYt5XHPdfs9C_mkp_DCgdqnpv5pGSYIzmSFto-7Jpj2pjOuzC4HF3ombJDd-IPYIUz9uhK_TkooIxO1EAcG8ZbVhcNY0Rxlx_VEJBKUpK4E0CTDZ7nt7RRLE3TykDuWCzIiHiA87Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/blCbQSxeTeql35wTHVtT4nlwXppdbWs0cdQcUHfH4sJYQb58u0zz8Ij-nIITTCXdXBC9MY51TCxAZQR_y4apqExEIf1zmfFUppIj2h0WE9hCgN45OctRPXiORIJAxYGVOFrs3IZGBjTHWe_JDd6TORp3FsPcr_Q2Uoa850-zrjxtwy9_dgdQkusCgnk20cIeYvZZBLoH8MVsqUwOvAoMpLO0hNPGjZLNbC-dKC2v4PScoaq9WmMc_eXEBBAV9cZ7pDM1Gq6aKQ7A_mbDsYcy1CsfZEYYBvhTBt8XJ_bJnaK4U_Sg6e4lyoFMRsyJ9n1KEgDYjGgFizoeEBdM3R-zkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d_3UB20RhLgtFUlvUDDFBuuAoL4j1xZvTUNBAtuEfCoL8PElajy_aTAFFwPymPOY63KD03IN0UovywTCRW1QbxL1YEGxdY2zbOdXcm0R9fkfTfo429WL12HHQXRIlimIVlYprT-zesuRxotxkFxPj-UbM0a7wKW8ErsISSZOniTk2g5HPd7HnHNKUre0qvV-I4FJnmcKKRMPFpTq-5N0tL8IyHVHfN23oTAm1cHr-DoqP1p3SdY0A_u8nygiY3shrL5VZ8aCGV80TBYcJpvxBP9slV2ZGHP46mCDTsF9FndIsTS-6K8mCOl0uJqh7UHz4JAS6bN8RA0LUYvfvvhnbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sei8mfAgvsudiIks5MKi0ecGJJRzZnj5H6Ba_HObqc5S8_A4pAnZbXUBU737aATNcuRm6ehwLwpMR9Gpv5aSQxvvj6OshpSK46L7TG7CFXyXgd-nSc_S6SoklDOkWsjL0b7MtMel0pNqbr2he_DAHrp24Lr7cHMWkzBPR8JnGAQrE9Y0WaQh-tWalzXOcTtVwTlGPYIpYr_1y5t1qNa4AVsoC7Ctw9flplIA_lKSYhB2NCWx4DL03BxBMa_CdgYZ2_LjYq0X_o1ZZkoi-c2fugWFN24VehoxG-lTuZoq71K8XQxQxxJeGhDxJCZjedVYtoTMzVMH16Zhc8BxzB5ufA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ODLwdqBN-UdkXIh0AX64tNlzNHqs7xdthv1in8djJV_5eN2pbLUMHXLce0g13JixrxPkK-SCcWDhY1dp4INx74IPugIo4kysBC9AXZHtzKodf6KxQXyHRxgtQqrXDlPDqsbxMgjDTnjKJYu1cwKlnoKl15xZa-U_jzuTQyvaivoVN1-ReoDV7OphqfAMVjgQuCwyijrEJ8OYKycL5hSVZ5JelMQN8PNjyv4KoOmlyF0tIKNqeYMwny9IMvxmxrVKt0u82W27n0nK8oxzIvEW0j9dbByeq2J0t85AsWMHKIl_hYk1NDx4xLLeS1N_5qwCrVUcBo9ia0aX7l8ri9V9Ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fo1lgyiA7kkdg-dbET6AU9-gai8-Kb3sex2zDapXIdjx_2ALZDuLjyYoD-RirCQQLQ307oPD_V53DdXDcGM7Gv7PA09BgIFZbwxwT7WsxuwxMB9JeJPBukzSYnwtwYyZu7ue9RUndujq0yQ3jJ-po9AdFAHslj0Nx2xpjzDC8JJi7TBQqf1s3VItFJnR1rIiLlCgpPX4jc3zfZcA8HGLH9CwawDRhnZ3eG9VnQXYZXJkYbDYlkh3qQNJcHzW7xOa0Y761oBeYlGRDdHE_P3vslVnBeYeYipiwoD6M44UI9x83PVnAUhSoO5o2gvTFG32oHPkMr1P_mCzvmcu8peN7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jSlXjdCbbV4tbovW42pZwvloUXI_45jNT07F5wt8F0KCkR4Yv5DpjhuouFvDAyApoxEftfgylnGG9YFQZuHCvNdIxUFgMzsseMeLA3gT8YlcLviKyLE2Sq1LLJQYSReS_mUwT91rXH_rffPkpGSrpny9tWhSa91JUwy_1CQR0AVdC9NlkJLBL3t5IBLqwohs0wm1bKVhY1sC0W208knsyZamk44mNC7pKsmW1VpYuJBRC9tHa9y4bZEc_bG7ojrgKnpT70WBrdszLMETnhKoeX3eiulUyQuVinsE-A7AQvOdvNoEUiHYD7VtUBFpEB5ATtq4h9i_ZOROPb8vLPbIIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mvgGN9SjakO8GCqxSrGSZPXUne69gjLjU4iyKTCA2wuFjcAzKUGwDLaj8blqluqtjd2pI-i3L8VJzUHUJ7ntZ9-ZS3fDNxa9-iSRVJCZ43arcSF4LOvNWXK90qiIuGvrO4CGw1a0jMoeGC-Glw7y30XEJ_nebB4qD6wZF1wtrKySTJmHp14Pd1kCd03mQwyHdjbYF0c621gJ3t6COBGh03PK51QD0X-QsdLLtDDjJGT7vl80xdT-bDixTiqW1TqUle-jc8gZYRv6RqfRsyW-HMrvdjtKPsBuK4zWSD23kaJLw7E-nAKt9rCl32XzG_pODW6pt0EjVr5Z8T5hCfDouA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mr3cdzMMVdiU9FzN3FdxhowbuGWoK5LW6P6-JsqRIbqpSU6EOubG6rQ7zHn0mqasdUDuCV0xAtlvKtbDobGL0L260Ct5FfCVKbPhETLSyxhcpr7Oknr5j1rcRusoLLozHuClQyx-oMlCdTRW1qvyI54NLFh8dR6pMa2oEroAes5UwvzJ64P9A7kcoaIfxXbK-UIPaCRxn0He8mMV2x7SJMOQTxCkCY3uoksj43o9dxxfZzynnatatGtoIX09C1hcncOPO5hw_54YaOwMVin2xH9W13tsF9R3aL2nsIKm68-NaGj7rR8MtIOj0bqlzul9F7JiiOcY9GO1S8WWEc6MfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VSM8xnMf35_S-O3czFGePwBstes6-L9KumPQ6uMzblTxXMJLjUm86iXyWAB1ZyARbyv_YGwVIl_eSSJ1NEP3JvSxUXsg5XSv-7dgqwUE6oqAzGF-u4q63NBOV8B--5hBpnYh-EVKP61hsxq2ys_apbAu6dbxfnW94kcqCHBz4AYI-LCNqB_GcDNeswAiTjUF1ZgYHLSM4I5zYolqG_p_Y44L_CZlTn0O4PLdOBNKGvol658ywpr_UWn_ad2PmNR4r5loAF74NAGSAagw3QJqd2nkLvDwDGN8p6Sdn4FLySmd_vNpxQN9V3RPnvTqnhnwbQIOYyGeVCKRgEeFoi_kow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K55su6sGRIsh9Xoipt9qVWljzWiUnxV2i5HbPmqZUAHLv5gUsCo15EmO4CRgeKund-ihAIXuBagRpDxoo_FYY_CQs64eEJ8sQjjaXvOeXOv3G5X9Pt_aHLvrvfiVrAg8sZ9GyXCekG6H-D0bcL1qjFtjhyYEup22CGCO-lbFGOydg9WZ5Ewj_bdgVGCLMF4h_SiOuQHFVQPr03DeR_DIB08bp3leIB-BXoV1e2g1hYvNg4Au9upVSA0zl3AiklCQIRx4AhHhnRvL9WT0Vp9rzq2Jx_PwQFkB8TkKNBwPkkkbj6UPSzWqUBw5UuJLPWB1DX0hI62i40hZ-kGC085Cew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uJpv4K7uHnQb6E0oQZsiv6NvPsQdOkeg2julQYG4J7R2l_931VtL8Gp9suy7-vt3Es-zyl6Nj0KpT8PuD-GLZbiXAY7RamwBhLBgSLyd1fOLKn3UUv7_VN8u87ggxvKQEUVjWy2ZH7pfpOO4t3HZJJMaA5WEuuTOiN7oxE3LZckbrQRg-MdCwA6r4xcPttrPNtfPJti8_TVmkaeuzp4AO36yOZ6yGt0vgEj3eKyoMPONTv1foI4-cESWFWPAnp5nIvJnfshoUNGCoh0XqJOJUR9OrtgFRiDYeFSd3o4UchJSxvguiEIP3qK5qZ7s42M99pkgATrp6SAn2uqvpME3Aw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P4f1uhdpTdrS-No5J8jREvvhvyWTQ9jchLg97SljfFK4giEPHzyv0o5dWWHsxsMxqN7grTt1OosrhZxILRxxqdnHJsP-H6hVbFgX7OSMtFc3iLqCnrS1WEpwjUn-6B3QM10W3SJzlSmq5MXHFZ_Ep2YvEnP5IzmNcs6Jyv-nMXFKLJB96yhSuJgxmg0Oebkj4QVw92QkqBev_2FVBVnQPZ5fxtXwUM1yDyyoJVY2FcvVQtdzLV-0QxG7wMQASXunMAW7iITJGogUg_Tub_6LaAftrxLIVINEV-6_3vpuB-wH3LdbctAnhM1nSbRatgZcDJF1Nge_ox7CBrfzqz6D3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=WwAbWA-44nq8cchpuCnEsQ6AzkH7LfnvoUHhFXGpSLre36IuRW-1xRrp87BWeW9amynHqUdJ60Oc2yfD_clw987ve-56YoJzmsQWIir6aowYk3sxRpoUUwELaaDQtk0oyAdlkvtzX89bUXa0UbpMOJDZrzVSymRXUZ0bMFLqWvKUXClZ2tvLVP9p6iI600LKkPelqlbadzSh5-oBKhGtxoMLT_Xs9S_LeP0DoZ4vj7V3L3D2bBzEEsPiR9ezmUfpKMd10D-FWquBfNbaT5rCpoZfzF56QP9_pzCcDneCAB_F2EnsFdulZzLbkNCm-TDasiUgCVzwG33Cyr5QRzn0JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=WwAbWA-44nq8cchpuCnEsQ6AzkH7LfnvoUHhFXGpSLre36IuRW-1xRrp87BWeW9amynHqUdJ60Oc2yfD_clw987ve-56YoJzmsQWIir6aowYk3sxRpoUUwELaaDQtk0oyAdlkvtzX89bUXa0UbpMOJDZrzVSymRXUZ0bMFLqWvKUXClZ2tvLVP9p6iI600LKkPelqlbadzSh5-oBKhGtxoMLT_Xs9S_LeP0DoZ4vj7V3L3D2bBzEEsPiR9ezmUfpKMd10D-FWquBfNbaT5rCpoZfzF56QP9_pzCcDneCAB_F2EnsFdulZzLbkNCm-TDasiUgCVzwG33Cyr5QRzn0JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VWOoec7rIJ3c5_5NaTIiFh-NAkFC8oc2M5jrVWga6zh_RCFEiZP29s01pXbQQ6SzIATVjiJke7rAiYssylLKkAlcvoNM0D3hJ_ABaT8Ncv7w1rQn7JhOBX4vA7n4QqyHu-4AMs0DUMTyogkHVc8UWzd9xNP4j3aZQxyuvYfNeWij-sscgNUzPpDtvtqTPQMbr-jMS7dqax-0W8EK7qHUpZ3NNGzMTf7Y9AZXSkxgXUvfwfSYQhTYYc7i76wQRPd6_qF1d4K-Sqs9FbNiHUhQLwg8dfTBpS_l94t2QsMf4sOsEAMwgCer9VmP8FhJxeyEoDqoHzKjDwItFYFQdrkjKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s_jayKOH6ybb5hJjUaTKRbpm2_RyiUL4GkCJy8uqW3I5wu6tUcilQKSOyWa-NZXYAlrqmSaIuuX5TC19Dj2ZGxdvmOJPRVokvyKYZhT1yr62rj7FnrhQaE_c5G13sNi4RG-wDoBRxZJ39QCdJWNOow3gCyhp0psKkpnWQZseOnnxLopJqIpAy9_DvobCUkjZ11XAWCDoMFVRnQ6IsXkVfuzlm8BJzjoz3vAFHmpQuOPaCj5K2ipD2bt3z2qTBXOnQKBpQHuqjDIVgH_Qb0dXBtI0mkzGs8UInItl6JqoSXbqiP-oEM_aF3geqiB0ql2H7AcGJ_1BeKMBewrNxSTS3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XMO2TiyazY66pyQvg9XYE5c0DlNNKKm1L_U917-oERog5pw3jAOn3_bjsJPrEiyJnqFq2zRhL51eNmJ_mw7UbTClibelM0jawOVAH3SG8nC1kAsTYqMAQ1I8CWFGANmhvs1VW6bo_V0kqlKfE2Y8Nd30uHacDMTsHkycYWGh5ut2m4VUQ3jWoacwI6-_SWXwdRQetPUwEjZuwqjdjlf5kwyXKB2aPFG0xu_eDAZNj_dsK__xIDeJ8SfwSPijQXxVx7zR6tPxviKlHv_4M4hUBbmRBiXTiXJe78OutYmuovRuoD7ifOmBGyocGJM329gyT5ZE0snh52xE-0_A1RzLnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TYqEymypp0UqEz_DxymZCYEcmvNrkZfatfoC52NBVYZB-cdKAV1ogPOmOTIbi41wBlE2-rVM_P4Ab-TADjngcByYidwdijitoV5Ve6h7t2lbsUmp_xyg1Ym3f_RukcycEOyewp4hn3suiR8UfNixeYLbyldPutSIn-5hG7pEBxfu-3G9mHAGeQoL-vsifsyRO-6M7Pi1yHXTQi4SU8XtYO9LU_5KEc-crtYXHT05ON_XUf4_0S63TRlkcopREq2lDHAh97By6oJGbGh74XCr9iEqIpGzlnAIWd8-KKh1g47gonDU6XkK9fO41huuc4Luhnyx9U91a4YoXl8uBD35-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NHyjOxgJCBE5l_6oMFQqNTg2CHYEAI6a3BbS6m7iXK5-YKqZ90EoXK7LVdwJgxbGmaR00mCSAZZexarTbfK5zOBmhYGkGhVN-6TGUbNedJz4a6I4eOs7GfESefIW_kP5JjYexVAIlgyqiT7kmGyDJHqb4jiyWn-w90mZpNPHe5waMU0qP1b0sOuJZokwOUA1EJHsIOqpOr1paZEgOngdOvgwtrfWTDU6SXbXVAyfq_VYnjQ8tqiIx6oaSCWk8w8EUz4_lLsIzjZ4iVjxX6l4x5HWwqRoYeizySOWSMeRN820vF42l__yxkBMAVlBWmo2LPssw-pRYeU94MD4JNK_WQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GBIahc3Oau2hIaVoWPbQxYvWYwrQJNO0nYv336Kbm02oIclYNwEPCZsZ2wGkqu3FVylrk815-Ogzjyv_WuU-b-q4NVEWvw-hU_H6A6mJ3P1U_6NNjAk1P-CTqNTNo92aq2yOkxBdTf65V23RCAHry1w4UZqhIdLtolaURg4eKzNR9n5PEf9EcFL4SZu-_nnd0KzKwuVxImm89w32im6McANWm_XEdw34zQnjyZZd2WvIIR9hHD2YYyPoqbk5RF8CSQsnkZBlwm2BGyjceqfOaQWDKbgyJU72sQpMQCsFCzWP6ThQB-ehpDLflRH022YeOwHK8wynxphnpP_2rnchdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GPRBp3jNEcyvkk8WUdZUreCmagLj9n0immg8XX5dX0GBj7HfhjEhySI2awEh5Q_v4dphRZhUXFMWaUsap6PNGgL5Xih8no5NnBxEDkaNi_OQnecM6gPhhyib9OLJwOsN33yNEWrXarIqR4Xz54ro3Oz2v72wu5YBvDn38r3eBKjedGkoHtdmqzuvjPxHwB2MtfoCYtmspU63hDhDg0GuAMOogNCj3LhAhWvl4LzRNa9COdYQPs20NHBIAAcJ4a-AklNj_pEon1zZVr8Ogb30DzOX7kEoR4jCd70jr6lQlE7_RCFGLNfJ_K8MLMPg9kGGLANHVJXcSdatx7y6Y0IaIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sU7XNYCtihfFRKNiRgqjS2txHob9eSynUs9uO6thSQY8I9_kIh8Iy9Q5b960wZyM-d8SoW93kNoJDHqW-hkmen-LwgCcsV2RD1wwBBxvIjMiPtIway4cgw7WoqZjbs94tzvTipw9kCuploUOk3OGerYEgs_DVz0Pfs8al9Smw3ShLFJ-hryqazHHyXrVu0hWNOKuI0jYFkT5nAt2zP5TPz39LKZWmQ2w_Iw0qWipEdcQZ9YM_tsyjX-j5M9h3gQsqhwXRWcj5HGgmtvsXhFC7UyBF5XTjWWzdDffmPSGgIj15A0XcFNt4f69qCESi--ZBx4pzf5igtb-RYmUICYjOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ir6L4Tp6oE5ryWqg3CSQXE2AZYMQNfz8aZWRmxTvB8wROiLPbmXsjNDtBebqIaNo20RaCllpWCv7RdQZ5y6zajOGTPSKehU7p3AZ1NPw8LqI1HFFW2Bpw6su0WLJ098Wa6b4UJm_NhIpkGZ-yaa9Mi-LYmJiIQWEXuo8clPb9bPg6dFeq62Wn8C8Y79QWo07DwPgITdvvUXSoOQ3mxxrylh3LbjJBwwsqdpm2oy-FWsPGhQSTzcyAVMEO300UFMP3is37HMcE4NhRVxEBHF3N8BAuKmNpEmtte3TCFHosqDxjs3plAX-ZphaEEZDNUeecXiwpjP3NCO9osy91OwU7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u_Bo-QyDdYj2nhHOoS_GttpLLCw6VBIhNSbMWb-2bDnnqatCzTqoNojVV_2VBioXPQg22USzj28B1BuAnQzFcUPsUNi1vFTYZRCGkBZiXd7lL2blKKeBiKV2QpEECn3oId39ZXF5lSQTsbJ7R_QI09jRG3Sh0sOyB-5duEftSfey0x6Hfx1GW0nnBOU3JlzBY4V4r7bC5u1tqNkDqDYIipDH2_5vYUfwxKyAuFAAJfjoc5EwKVtiNFbxlkPivCuosckOXeZHiUh6Bjtwk5jnBMZDxVzjJLi3K8-F5sFVdilOl9axy_2_mMZ4mMEwgVnyRSoe4SAmo66-XHCPjOowzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GOCSUzcpn-bpNuQgF6HqKWH8Jr2aOOfMAjnkDzozN13tOs8jPVl4fpiiFtLQeGxC-cSEZ89neBuDwY0GxrOJuQvGsT3J6N4usiccuxqypKyMqhXd0H7h1dWEs83kTkxWOM8TPVhJ5DWIdnYJlkKa0PmojTt0psGqTHqfCxIzjBxpJDNWswMVJlHI7c5qKnlb9BcyQZIOGF_bQzkf6Wrp-rF-pnEUkAxK3sCbtn_46lUYuBW6EQ8Wl-Nkj5PlD4z02e2qAdg5mprGSrVJna2g1lewrXwRlxIV5P9661aeAbUkuJw0qbspyhNJDp81I_Ae10bGedGntoh5iXn_uvEn_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i0Dga0mD8dOkwl3BibiTnUcOMF6qEGrL9ENyEAZyU-S4hBniRHUV4PHZzHAUntDJDSRrrKTi9jLxddv2zEzj-NJUTONQc2AOehoiTNxt1SLfJFEtQU9USqQ_hgf2kIflkJh5Qd_STsWziiGbcnHvLO9WGLRCAiJAKJeTEKrbG8FyzS4EwTUqrXSz3kHCvLGE-LJWFWAAD0p6Tklq786X6zQsP1BxsXGkbp9hMe6sjkzVZs1pnnsoAUdGH2E8mmkOR8hkG-77zyba4eixkCNtSx4Cc85nsItZ-kvoXCt5YBRp_7xmYg3dEqyz3NoaKF1AuDQP6Taja1lEVvp2YWltGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qOTIy4kN2IuB4XCgq_92NqOSltQAVB9TRBvBFoJw5yINzwVBKHLMncZBEtuKQkeKlyYsnbq-97i7bkGgM13b6meW0usLdp1lfclBywhjUQsV-phKIO7j-OBJszCpJSucqFVLAOFcEWFqrJi2TXQTilI-298eupOJH-5YvDgOGHaFgdG1A6-Lmd21uMgw9lB9bKRNsBG17Sh_42YKMlIaS_b8SfSqp2fkccoP4cVkggj5axk9funLrjDxYLVdVvyK30RDpgsHI4XUHrfcuwuh7X0mZBjPgQKoPnzenHD0OnShFSEP3DbUa3nzKlZoTa6MPb8DsSlNEuPCNLectsXjEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AWY0ZKk3hRUfGh-h1KtbHy7G2oMdp6_aQ61ckf3sixSCdEwz1DSfwvot8hsXvJO-5XuigB8GS1BgJMfsrR5cD3e-naBawRmpX1g121c4MXulM8mgs-KFYRYflySVAYtyijS7LM00_BEZjbJ55V0j2GjX_wJaDA7MIkhDMxCwNRkGiwupsOpWALQ2JXG3zJgV4ZNV9s5r8sRN84pZ_yTSkIs-rr86wvidtXW0l-HDAaP4TKskT1F1dUry6HAGTy_ERIxXY3QiPVIUq3Zs4HQAgb3ARFFKpr-j_Wonmb0FyaeAwvMrBKdOTxhLs6ufbGNWpjMvWJ8erQqezhfqSJO5qw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PEfL9v9zs1g37VicUSUnQ3IcbTiCcVrSo4T9oYIz2DMWIjvcDhYYcMPRiUuuA8FC132S4CkyaINcITR13zyL51D182mtGD-Se9lHLc1nwd4q7zhKDRoxDhedqKHFdQMPdiprhbE4nJYXnHGNTHaxpuyF44X1h2YZFl-QJevhhzHX8EzJXDafj8tDnQZ7eOLNhpIXoqe7phIQdtxKGu0WJQdzuki-uDFYv3kIx1J4PD_Wex1eLJzDGZ1RbdYtW2AyWOlu_UTx48D-AY5yrZAmQQnMWDZeA50HxLLAxX6wP8V-XbvSx3V3h9byAvEIuH5Fv0IHOxmyqMplSXcxxhAjXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dsvop3uQpAz2W6wt8z4ykgF6xhshP1hx-bTUpcHcz6eZ5o2mNcSE9jf46CFZfEKcwKrWZpNCIt_s9ApiLYyouOt8pN--w9aYva0c8wdWUscDKqfw0AotI82ox5C4HKra5-ZmuW5sIWyrWXKrOqKq9ezFJRspTyDD2szTSPYzkgnaODsOt_SIB6WlTYg-J9jsRt80_0K0BqN7BHocWr5j8UVHmyEFGgDtJcSQpUFJ0DVltZPC8BW4qVAyOK0nP2Ous5d8uj8faR6Eh7BhChAhhh8RuU_yQ0l0OVTdDTjP0OUdwgdLKGu0y_MoBe-7Pq0xG6LFefphvWWngyPssnSh1w.jpg" alt="photo" loading="lazy"/></div>
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
