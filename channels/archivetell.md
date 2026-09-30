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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 19:40:29</div>
<hr>

<div class="tg-post" id="msg-7934">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I38Evbc-loTYSSl82oyb4jl4F2xy-I5J5WxgETXm4izp0ByQO7VB6rmJ4khUGWc8nh3r7Ll6mjRh5Pcjh-1uDLCK6XL0KRCWna2XGMzZyFOkKKfMt3eTpa6JVI1D7oYJLX91FHmtx9OXn4-y--XaU8pjUq0iCspOwnAfLYhy1hVBKoVqLAZoxnGXi6sjzul67vNnCky6jEn-tHh53c_-YXSl43k06PyIRoqVn_-aKTQF6b6rjsti3UyQ5_G2eTAjMWPNXQ-8bEFgl0gVYWfBTas6zwEMhB8s3YmU9ZbIw_u3hcMc6KQ8FMy5op5hkD8KMUuDxxg9G6A_QNYHD2LjyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی رایگان به Claude Sonnet 5.5 به مدت 2 روز در
arena.ai
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 374 · <a href="https://t.me/ArchiveTell/7934" target="_blank">📅 19:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7933">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 791 · <a href="https://t.me/ArchiveTell/7933" target="_blank">📅 17:58 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7932">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i29PHiaKQRcPFXyQWVKKhZCSGWPr-wYLxnub18yLWF7wEVaRQ0jK_uTfD7rvMI0kn428BOoJ3ZJ_7s2mNft5WfbP-OJwFc8u2aTI4eALvxOQCaYHKq5YJZ0wbbKmuMsyx1U00UzSr-a9ewegY8h5bIpcSbwRmr0Ssvw2wisHATZKgcQxs5Q45pBIHfNXtTYxiSI2LpAAXXb-K5nTOSzRio00xPgoWMlddOmQyL-fRs31UEqYtPnL-IibAFIDuuQaUj3CO1YGpjcfXcf-wL8VnHfpc1PorvBcUUj9Sjjh7JxxYZVlRI1Z_s_5h3V42hw4e5QqScoRCI1OVjKb6YHwsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/ArchiveTell/7932" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7929">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7929" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7924">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tj92ucQpxx3QC1S0BKQkNNqtdDJe9-3OgG1oRgtaJLZzGLjtpZn9Wu9O5QLaFuvvB73lW7b7bMV4X8fnF40-Jw89irR42bjXlEY7-760ZAEOkaS7Y7vKM_B0KY-Yt96ovCWHanh0u00P87cpgDPuJ4YOMvjOThoFxI0OjpO2UeKp7HYXRiE3sHfEltcNoNv0rbz7PeCJwKj5ZKMcUijem-5yZEliL-4aqGoiulQ1AXWqvb5-XESXbOqxnIbhnusoqMnBjASXG1l9LzZTDsvw6-I57CbohC-oMtja-7t0g2Dr2Se_uK1x7dV6lHgr0-L0e-ZSo27VFY8G5n64HDV2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hX38EOIkBiy3HEazpWc8MNWcegGlEv7ug9H_HtVbrNK1ujIcRS3t7Z0jkfGS9OVzQPA8vBq9OiKMB7d-0p4BSJayHJGq78LTB_RhdQvBy15FlKwSmV96-QeAJv98SncBiBcZHhMvHDcu06cL_FcCKo8erSDU_oZY7g8aclqwAUX7vrWpZVLNVt3NxoTTWIxuL4QzTFegVYWcTPgV_r9kzSGWNxjbWpIqKjKpzYIbDaKd4LInq9G8785cDsfehvI9Z-mzzFa3wx4GvMpc_cqhTY0yUIndwR7TJBUgTOEzaHgL351i6HSdXM-_RvgBXrllZwk08utWiqZrNqwIjOlPJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fl7W0iyGXtUdfaZPFYRdvq9PdsOKaJPsda0GRuIIcOnZbiti0VlRYC7PVo80sLF0j0_Fzq2dkb4bCvqowTv4F5AyfohnxOaBbXy_xAvQop5heXP_GNvo7GoV8kMTguKDSXUEYiwdg5g9ec7LjcmeLvF0xQMrpeng2NUHXjSQ4F9r1lQlMcK_xAyC2puMcoQVcw4I1go0tO2AZUdlwrTpZTeFoSv25wZpeVi14Z8wExanaGXXy_-mexBcU4KDn5D72L_iiUHjxJT2gmSvAcw4n5IG5O4CbO7se89kE9ApxqMZseVXFjq5E1k5Ssuo-tsaOxVoPHUM6ZLAFV-0RktL3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jP9w8obLMPQenuPCxlunaXT17bruupU-wL1TEzqLkaxNdmQfwfFJBhhfBG5KH_VhLzhlvCn5nBF-a5oewOUmO8qkFkuMdnRXv3e5nHrYQYtpCnVDl6lAxVz9d6c_yqh9sfFixqsFKQYksATVJLcRZ-ECX_BkVoJznOAABKwyzuWR6IwnbgaUIU6Dsm9Q3-OjML8mNK0oFwhKJ-uY7kgIP4gns-pVicGvbqx8SIz7nGfz9VwgQpoXByWzO_bmA0-RFGdqpiBpRD9F2H0_Hp9SGvPIpIQNSAteAcrUOdGuhJi6-nIg4WU060A3DsXefmc-EL5syZAs-jxO23fDEIGmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z1CsBwos-3gs-G5NmrQF43uaK3GebjZDkwQIthotayHhmv84m0IpkdAax-uzy9uZRTjTg_91QFuXuyEISevIpSw9BAEg2zTGAtbjgRBbGofoJEAhP7P-880lKabs_Q5-jYb1MT9VRKTawtzpYDjy5LbQdHLNQndDzWbdgh5HU1uBv9GpDhABRKDlMxGxp9NibPQqF15rX8B_EfN4Xq8H4gmerCbGcEQuYCfJAD76Ha3WLg49LJ9bYj91aNVmJ-S4wcVtBatWDAFXjpzGhF4XLViRviyvk2VR_Ic-cdp8d8ZUqjmFrAhGD-65L7b2ZwLDq_EjmyuAsfxGx9HcjF47vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.  این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.  پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7924" target="_blank">📅 20:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7923">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3PL_cZzahhvsTi-2pisvJzRCFkSrHfrV94OD83-M9lZCjj-1K0mk0CTZFHcvuz0g2ucZ4MzrP_-Op-jn2bf0-acuusxuAXSTNdDoNxYdMep9l8JyIg2_e-viC28pDckb4_181ziWza5uUpDD9Z4okg18bPsMZCD15YWC5RLHTx_TieB3NYKDW8V8r-MPRF2oZssnD89EkYIY_WHlhzpVIiB9aLJ4jjy-Y07tTB5T36G22W2xMhRukD9T_mnvnac9tKMM1xMdH_sdJGng3sKuceRU_JMyJ-zTihfWZOysOaZT1e3ozTflkEvwCCSOJV6-oR0464tJo0z4jZ3CeTDxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6.1 Sol عرضه شد — آلتمن قدرتمندترین مدل را برای برنامه‌نویسی و کارهای تخصصی منتشر کرد.
این مدل از نظر عملکرد با Astra برابری می‌کند، اما قیمت بسیار پایین‌تری دارد.
پاییز امسال شاهد انتشارهای زیادی هستیم.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7923" target="_blank">📅 20:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7922">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7922" target="_blank">📅 17:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7920">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/ArchiveTell/7920" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7919">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/ArchiveTell/7919" target="_blank">📅 15:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7917">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7917" target="_blank">📅 23:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7912">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F11WH2XRtPdQM2XguGlmFJKtJ99ktogRT_XJ7DkgQEP0IB7cBThewrvwdiI2EHmYSfNX8uQTAFvHhp9uJ40euPnvJEicOjcrwBZrbB1vXt5HP-6DuUGkvbzuO_joly9Sg--_VitijFsZwMz8KFIJ8ujxrFww06ktHeAe3BqF32xSvJSDdukJrV6hbxp5EOOFtoKJrtSSgN59vR_XgSZPxtb3wEZoBwy40wADRmqc7jym-lRPXJKPa7PGfNjQpvUCeBljDwmDjIqaJGuStG-pZIkExqTZOmjhkkT2j1lmDEYqeVpPEcxsUJUjkIwW2ILgs_2TNi0tx7tHzg_X2DB03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nMyU5AeYGgVKuhNQ9nHQbx8kKpxosjioPJCGMU9NH6p-13OiyMMJe4OJw9mYEwbn0Ko5nfCMLTTQCKRNftibcw13wSRWUILwmEq-kUkTYY1Uqk_H8ILStT2FhiBegRtu6yc2ww0b7XAfsdcxdP8FloHGju41k8pFy15q8HoOptxOIcq4P4weACagVaMjEqOBzIWIFOz8l_ElqResQBv8wBhzWrh_NdLbwCN05xNaJ7IOTi7Ah5DOieP04cFGhtIjtzJNhnvEs3qu2Idp9pQAWfelJ1nEngLxYtzjX4dmKVuMQtqyK5oj5X0AiuBhGJZVpDCxyNvYMxkbTa8x_iDWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gu0xJq_fYs0AfrjenwGW4sW_FfIM_PxNJY8kAS2Y_c97Wa7b4UWU_jbxCPaPsAuUCdw4pqnxCaS3Ep4gyJKxx1JJJOKN8dxpa0PXBb0xxrIfH3-tMWa6ThJZt4QdmldHHd_HppVr7YPO6IyRgzlrNfZwSdL4AnDo3lvLG8TjPAEZH-F_e-q-yLZ39mzexV0dGVvHyvFQ_bz6ct6SE5l4emKI-koGUt9pmTc53O8pBB8rND-5IMkTtllMpkXKM1daEbH8XQvrwy5vfmqYpA0WSSseFmzw6h2DBnoCUXACn8a3ofGbEC3O1jKrDNvFk8u-hbwvdhjMxDxrfQlPYlUiTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRHE0lu_Y5vkejTwWm0Six7cCGZzhJImTnQ-CCSKNUaOp6FPQ12ubIZfPdT7IiBatTvXSvp0QSKbPCWV9kSqd_B1if5hdlpuvhbM3Mkuu7GjreDWyHd1XsuizfML4UD1sjBILfFH0cKkN9xFumgfCdaeRg1IvixB90wqZqjy2nzymrgIsY7U7fkgHpm-7Iizc1tx5JMcMUYTDgpfEKLX5QPtrXnsUdLKr6mQjYNEyEZEOGUIvSSn3QPBp7Rj9EEelHlQYqhFTbA0UjDnNjdiEDV4gEyOUjHXDGUeYUhr320E2ysCba7f7Xj7AYGmUNaQA_2DNz3zhkhTExX0KqW0zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SO7J2MLRsZ9FCudqevoUTOtk7FKSfvfWHDW0OvMbJToIo_xfcUq6W6k3xDcp8_Oo644F59h2kT6kcac58esOK0NlNaIf7qJJeJqSA0JGOegi56yzJHF8gXqCx1V_PIcs7IGQ_IYyEbwb-iKx9se_HrfUqQQosADvenyj87_LTCx7kkdoFDEe_PZ6SSCVpsnaUXiPli6EMQcYk4htBfkSauPZ1G79ieexr3MhZl8fV9haCJMKlBndqiK95lhKxnwZy-MDZM5lkyXmSfacurAtzJ9PSv0pEeaPEzZ5qEvXqZ8wvepbPo1xydYuSvcd4W7fA064qWeHvf89WHHyoLWltQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.  برای تست به اینجا مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7912" target="_blank">📅 22:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7911">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn8yikBMy6frNGJ4PiiV8kdj-A60NUWCLgxJIv7nyeYWGOE6BppeN3DKVJhSFwpPxcvNiCeEfqvSFZxnYDD2gNIwAHXGtX_0e9NYtYsnn5N0-gPAEikoWMXD6_a4I-WCvUUh1DwTbJX4KkJdjZMhHm3BodrWjzUqErgrJs0frlbEbMbmIPZLPYPmZgGhx0TlXJWmnEM4hNcC2Za2fDyXTF_7S6R1rLG9hlzJngP9ZCI8HsBFjQG1rM5zyB3vTJPJnPhEjtCvxV2YJLFyg4w1ZAt_Fdaz-rqkLEAQGCfVb5qLe_cVA250nY6pEU5al1JFplIkwIOgc_8MavAXNHfR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
؛ GPT-6 Sol به مدت یک روز به صورت رایگان در دسترس قرار گرفت
شرکت Arena این مدل را برای همه علاقه‌مندان به صورت رایگان ارائه کرده است.
برای تست کردن
اینجا
کلیک کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7911" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7910">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKkjtALhz4cNw0KLcSf5wVjvLrCMf-_4WWTiianZL1JNUMvOzrc6TI-vEIgpMJLyoF2np-Koe66MLqQ4gWJSKD8ib6zGLipJd8EFRYNX3zOEe7qcXB6C8CeiVg58mqo3k4kJEZpIMmiuT-C82tlijtbEfcmybG2soVFhdh85dEDh8ltzVBU-4hjSRZEBpdJTRx8XLnFqmhe7st7Ksj9uOOuxFWhia19MxfJUUTAdIrS04qiL1CQNJwnEFD2VTOeuJK1Mc-JQDVD-WjikmhlMeP08t8yV6lA4kZs5Kd9mS_o8US_FiEgqbizdLiLORTVMGT2niKVNtxp7cRi1cURYJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
کلود سونت 5.5 منتشر شد — این مدل اکنون برای استفاده و در API در دسترس است.
برای تست به
اینجا
مراجعه کنید.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7910" target="_blank">📅 21:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7909">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZLvOz1C0VgEuxJV9SPtjqsGh3rawY6wS-GU1M3jPesur_qopvXzXlwiS0M1gEOQN0R1qG7xF6AKGOHYDZR5-5jTvE0-VtiEKNZSKZs29vqM1H4DPGWGTwanyahVoPJUiGzLK80P5RXiTIkvEX_MlcZdEkzEJMhl6nz-s5QGriqaJqShn06_tD0RUoRiyPKDI2SRCQHTLzuW1i22sYHMU9hGeMNBzh-mphWnHjR_mj0lbyUSmHy_R2P3sbw6nCYdzDqU46bwa4-d7W9_vJW11QGVsCN91bddwn99FfeGtSbmIT1m3al2_dt2H8QwzOUcL1caKa35GbMPqlOjks_hwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7909" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7908">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خب ی پست سمی بریم
🦆
🗿</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7908" target="_blank">📅 21:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7907">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">جیگرا اون پستایی که خیلی باهاش حال کردین، قلب بیشتری بدین
❤️
ببینیم چی بیشتر بذاریم
🤤</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7907" target="_blank">📅 15:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7906">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkdqxBGlYXwprKzPTMEwSb_1OZlefOt_715E3i_HPJn3QZ8L0Tte--jggBpgljdFFzYx7mn6guEK8KhtbpGOsU9FOqspL5fU0pPvfz0anENZNZ4zfgXVF4oO0ZNpwMS9JTknw_pKOhT8-HO-6DK68X3XNgjJkI2oBjq9OCP3OT-g6_Y5u3IEFA2aZq3ozlINEmqlAaY4w2bFy4AaM9FlOgcjqDGZuvf5a8IdGXnVJfwLWgS-_0ce-3nVzLE_1nmByPie5hfII3tYTY8LiPJZwf1VIH08gVxnw6HHp8jdixr1MIOV5e3-etNU7PtIahyCFrqgITK_w5Zmq74VjcnY1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/ArchiveTell/7906" target="_blank">📅 14:56 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7904">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkKuDAUu6HzaE0NKXLmbOp2_YXSJsx1EkSnzoEIiod04PQw5v2krqXYyramJdpsafZB6W2qFPfPFladwv5BuG7C7xiYMhFntejdsRljeu-ZUeHvwnY-gWPT2g0qrVBcmkcGY7sIeHm5Ym8UgWPG1WwwA3HmfLQ54JSJCUfzgRDa96XC4IvV7o_R1pZ4syPg0FtqlPveFg18xmwUp-0LBcu25-K9YguB4H3ycLEoj5LdahZCmzOrxn7HAizpi8msty4R6ryFnfL28tl8za9tykS6F6l6Xq0d5VYclpSWsPGT7MmGQyOXb6xirro_QJxX77NebxVD7XZwI36y5SgLmlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7904" target="_blank">📅 13:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7901">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcqE4xm_63tHlwrMNESI6SNedYDdKuZ7p8N0sEOFWo57S4TGHtBXuZoujXJHaRflw8oIqIenwnq_qvO9PEsnrjMAAZTYQgD-QOwOZHbVIJwyhcp6S6qO12ZExKmE1AGk3-zjuO6Z3SMDBPhtzg2bxOai92Ah3XnCKz-2mdx9Lt-7na4FAU21MZvn2sR7vwR-3poxG-VHB6FQ4R9gnuSnfYY24uAwaRfK2JXCBJD17EQOaSRLRxb39N--niMNstl5IvIxEa3JV2Kf4ANQVSW0P2KrhP2k8KbPFD2mg8ZA9GWZf-mN7xj_XXGT3l95-XpSAHbNpH4yP6ZrrRfZ5_Vokw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7901" target="_blank">📅 01:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7900">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=a5c7-odGMICiqfHYg56LTHkx0Xwa9gdtThY0dswdW-j8EQVKggIHIreGBRyw-ZOAT_n-1NRJY-X_fJIJDrp1owGV7sOIFZj_gnzYBONeYfeys9Hb061aqno4opov6PQo1UVWWXjBeijVoBdKYfPwxQ8obFqat7J02jUsbBrGjh8V41m_STcBTqMulaK8oaNjPTnYQgz2DBthZeOPDGG6dhA9nAykBoGQAip9Ja-qOU4chRMNzP_fPsYdNuMqC0Z6-0aFtIag280BTyV5EMK_3-OwIwxOApya56IvG9uT_ha6H3dG2f-f0J_LqiI7yjwhjMZooZq0gH1xEcpQNXRQXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81476afb3a.mp4?token=a5c7-odGMICiqfHYg56LTHkx0Xwa9gdtThY0dswdW-j8EQVKggIHIreGBRyw-ZOAT_n-1NRJY-X_fJIJDrp1owGV7sOIFZj_gnzYBONeYfeys9Hb061aqno4opov6PQo1UVWWXjBeijVoBdKYfPwxQ8obFqat7J02jUsbBrGjh8V41m_STcBTqMulaK8oaNjPTnYQgz2DBthZeOPDGG6dhA9nAykBoGQAip9Ja-qOU4chRMNzP_fPsYdNuMqC0Z6-0aFtIag280BTyV5EMK_3-OwIwxOApya56IvG9uT_ha6H3dG2f-f0J_LqiI7yjwhjMZooZq0gH1xEcpQNXRQXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/ArchiveTell/7900" target="_blank">📅 22:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7899">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsiJVgPE5CM3oWI057szYmBKXJiw1V3FQKG-TqtKoGdQ23hlPsCHg8DJglBxE5hJ4UjYuvhvo3BR8r5-anwAjjmU3vV_ttokNjsGdz-tCl50aEUBR24h5k19B0p7vwLQGU78oK-q-ixikiufG5kzdjWyHTJ7oNU4UTr34TodeaNppZg2Ff6fggMY7L-EQzaymvitQweECKVhgNlIBxmVb1KSzUuBRXNXxH_v-mg4u1JpPCxdr0IzlzACroLMZPZOZV1Zb_AWX0NGTNzkfvqEHIPsXsAS3rMwUMYtCoWrCdMp28SG832Utvrsx7M8Yrif2EqP8bMuWSXbI0tb5KyCow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7899" target="_blank">📅 22:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7898">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JD0DzUoKlGy0Nh_1svP9qGN2fsgVrArW9ogCe-w7x4OOC5njNBLREfMKSaqetd1YhR6--CLfnKUoojnNnphOp_FYa0qFZL2kMduAmy_15sOW5NyMc5HcclE90UggzOdnz4Dv6CdsvvbKko3bOaRBXjaxzpEmN7zQddaP_r-uO7buRkW8wh1D3rZTndnMoiisyz9oLMH49xthwgBUXSMF15tHb1_TZcS_ChGoa3k7VH81Vvk2a0O5ZFdj948rHvcsXtAlC7IL0VWg3TYA6NP0Nw8IAtbe5cs_nhaCMfnY6lWBx-yR_NKHKmE301jjB4452559DxbD7uf65qsyVLIdpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7898" target="_blank">📅 20:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7897">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">NekoboxPlus_Backup_Aug 2, 2026 (140 Subs & Groups).json</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7897" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7896">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/ArchiveTell/7896" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7895">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enDKHWB4F3k7vOMswHQxwA-wdgyN4sWP4uVHV3o9sGeBPOZatRSV88L0KwYaZvxHGVm-RSN5hlER69y_QmXLF298FYiMU3c2kqt57VqCI9nbDfWj2eAk5EvIaCoAnXtjclJzVEvOET1XIECo8hGxY2emDRmDG8O5yyhDpAx_LSn0n7BBq8Ih8E_7MmxTVy_7PSyh_4wxyH9x_dL3r8G301VgOhvimP2UdHXPhLDF2Y430I5YxYB0x09l9sTGsPIvqrj1zIRiT72yvqefpzxyQeYa6W9BWnriEKHVQmqIDkTqj82RzoL8D9MihGE8ZqqJOBRm7olJx51JEDTYUGAEyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7895" target="_blank">📅 15:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7893">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🌐
اوضاع نتا چطوره؟
👍
👎
بقیه ایموجی ها هم مجازه
🫶
☺️</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7893" target="_blank">📅 23:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7888">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbOfV3udNPfBM-3zQRKZqJ-ONhKgy9JdmsMe4dQ3Y-qQRkE2qlUwIJcFD3-dLcgwCdKyHT8-9hftIdEZM4wiqaqyuvhUL40ntvBFWP0zYeJqYM0mMI-38q030Ez-u0KIGpAfGGISAz-rqEeFSIBEK9iGZOEMJ_wQr_498NRMQdRjorHEEUfP_Q6YBloP76DDqCPZOt_ThbolTfA13QgCFPE1LuRc7jQUOveHFDbhJ1UBcFtfjrUaSOLVZf4jZTYdg3X5ujxZT2ATrDiiDC0wySF60gMa3mn-DAQrwIFzwWXuqGztEAAQPTG9z9KO2eHJA0UydFnHVfPhPdE1ikmZWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7888" target="_blank">📅 20:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7887">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZOShDduxujauyD2ei6u_FPRhBVw1H_nXGxMKcCoCTvlnAIfFTqknxFOzmmuGubQ4Vk_eEIiNQROhZGXPgXc-z0-bK4BepOa7Qjp8h8zuodkGXvKNKPi-l7p3_X5E5HV6e3jQLeGxOe5zPhOT_itCQDSETV7kXWMFdgYcG6WzRUfAF41v-xX8tpqJO3sCYGcMpHHb0JV8MN01Lj3x50P3u1tlR5XFkcor8sEYC-IK7lJX_gl1y24fsTfFjHS3_GB8WE67Sc2W_JiL443o6oNodoyLhb-3zbEwayy5sAxBbb6uo7XiWupybFq3ZW3ZfBfbLIFMk8712fwT-ljmViC9w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7887" target="_blank">📅 19:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7886">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مایل به Opus 5 ؟
( ریکشنا بترکه )
🔥</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7886" target="_blank">📅 18:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7885">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taSmsBQ0cAqI-8bpG21BDDnNZIghVEI4bJdmTJITQHv-oUCcYaCRxVlDcWvZ_qS37Lskd8mX9vxGkjl03ojPRkJvbe47zXwwykd2yrSPrVbZfPFmFTezmrrBrpYZfS-CUXRJ9xrpSoxf5z1YpVIcUEC034pFoxM3IgvRN4zvVunUtPj7v7c5E_ieuMYcbb761DK3yBRdDIlVIqXMhK9pf61a_AkC0N6P9DCDIBb0uSUtnfkyLK3OW7s2XjNFleR7-f3cW4QB_gHRmt-v3D7u349-v-I13of_vTcZmyeXHuSUS7S2yDJWr2QYc3tzrdT34idxejQdilRu92aKp6Zdmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/ArchiveTell/7885" target="_blank">📅 17:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7884">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cievx1unOvHOuuixB36kiTBvr2zDhbdLrExcAJVRIZ89BE-_OSaFAfJ35lVSW9m33EE61uUKYifuiZSNeMjey1xfA7ixdEmonQiHTux8Cu1--SadfIcqMWBUqRXGkR91jSi5kH12b7kSrsVrzQavsoOLrVYcCmC_gGAfmnap1JTZibExbHNTLZrG3yQcqWjT4ZBcR-1Y_48vvhWrMtoiQ-120YDY039fj1NT3gvq_rWkVrYmLEIqhqi-qjtM2tS9EsBFb4toTUfS66rfNe0XB3wuEzQLF8X0vQO84NVAoBE3NUpWfkk3LLfxPgQHoD-ENfLZCIxRhYUsHqmaOHtTqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7884" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7883">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐯𝐩𝐧_𝐩𝐫𝐨𝐱𝐲𝟒𝟎𝟏</strong></div>
<div class="tg-text">اینو چنل دوستمون زحمت کشیده در جواب بعضی چنلای مثلا مدعی مردم (پیتزا) گذاشته که همگی بعنوان کلاهبردار ازش شناخت داریم من در مورد کلاینت مهسا حرفی نمیزنم اما اون چنلی که مدعی مردم هس بارها شاهد کلاهبرداری و اسکی و غیره... ازش بودیم تازگی که بوی گند جامپ جامپ در اومد مدعی شد که هیچوقت مودشو چنل نذاشته اما من که میدونم نه تنها جامپ و خیلی فیلترشکنای که مودشو میذاری که اونم اسکی میری و خودت مود نمیکنی ویروسیه بنام فیلترشکن مود
نظرات کارشناسیت هم گوزیه مث خودت پیتزا
زمان تو هم فراخواهد رسید دیر یا زود</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7883" target="_blank">📅 11:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7882">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pccc4AAE3R_MjHpgeb-ZqtuuVwPxL3WZlRuP4ikbMYVYPI40WBuSTDNNhce64hhc-ZdStvRawb1ahVudZrSI4wqnW2fSDk-1cTv0sPQfsWqNM7gipcH6XH8vfWD0H7n2PWGrLMkGLS0jQjGC7Pem9qgyB2xIavOxklhIT46eYbtVXj12mdxCxAEePoM2v37LkzGSJp7k6wpDF75lrra6rzsHR--bCsh7wsDVmuloMxfqw7ayJTGXBqLVO6jscKhceceGiQnxcZIaLFgzg5jG99VkYQ4EjFcFGc_XR1oeqIYMeFESLLeprP8EFtQlbuG-vgQLit2qgwgAABrZxc3KHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/ArchiveTell/7882" target="_blank">📅 01:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7881">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGA7vOzxAuUIGrDiHjsSgvBhscBiT__dd-kuZjUzyxn_FvFqZSNM6c_PfIOlY4s-82G9YCDnZOJUt1JAma9c-nUvrSNSjutzyJE8ijTlvWsNwX6SZ4ftfRpwlnqbhV5Pm8QOEMpB3bO04TdyvYxuVzxoG9zs8PJy3Oell0yKbsueyDjGJqu44Fh02nM28FpbTWWZKIU1iU7096-wTH9pH0ebLqK_GVkiP97M-jFMrKIxbD6EXd8W_VyTspp0nTA51vIBTuwQbPB4tUquQ94HT221ySVuetG5tvjn4Ld2_GFtmm6xAiclmMpmBv4soLoMYLKto0xJHq14HOKBZtxTqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7881" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7880">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcFNXXDUzNxjU81aIQ99biCFJgZpmgi1C0PI2RCddGRwJcrwj6LsL7AqoSghr-GVyU9finVP4VaLL91JZQHbRgWbnxNh5f9AYm8hYLbZfR5QTvedy_uDWihUm1e2usTCxn39OzN5RYnXzPFWiS1pjJTqeUOcVqDHvXYrjquOFJEt6JkPWPcsfuEofL8-ReY4L-fPICeYyj_N0kATLxwFvXiLoKrAAWXnF-tvr86nJaG44xZbxjJS6wLMIpdPzrERX72IKzh2UmUc9ZklbtpHyqPi_W3x2q_s-8_HzPazlejilydHqyvw0StjGZ97sdBDwWM0BPhhnyGSZvCCX7s4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلل الخالق
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7880" target="_blank">📅 20:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7879">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irm2TDJxEqYbPmDvFs8TL5qpPDXmS_1E_dc19t2kGmt08FDvF-eYXQ2yEyGdBCTMmYHmCG6nAaZpzJaFLFY9owJ4iODz5tsf9aVTEVFH5MsojtYchm4RjRHLmEQK7l7DN7gylcoApY56etTVxCbESorX5D7LuTFr1VTiuiz0B9NdQajZf3KPl6pr0qO4KeSleJged1kT3Kg-HxR41ujBb55dt2jYRjeYLkzf-vM2Y277bBWvXrpkNdX1EUPtNenK4aTL14OCP8kZ0PWGg-_X_QdY9x-4fAmlaLCtx2ecAuLdRjkkco4Vj1mC_4vnLYzNlCJTOV_T-YZhbAUeVb3uKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7879" target="_blank">📅 18:26 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7878">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbHzu-u5dlnK6qUYo2QGFNvgOqKgCK-sJtVYeFj6oUUYvnDjopkAnTkaUbWG5XM4SN6JzvC_v7yLmhkBnA3gY152KMRF2MhAb1wL9Glt9j8AtvBoB95Bw5RdZh3R18EWh59-bUAHEmLRCI8LgTN75ovhMbgmmuZ8OCMU5XLFdhPdMCrDfQQvnSU_Uai2zvpNBCiG8zKZMxWnyVJtS2_9wF1bh9HT_jgqZVQO2feArJW8GEm2bwcMh5yETWf7g8tWpcBSMA09DfHZss77vkkO2wzhYZy_NjpHhAWtID05kvCtb_74flIDlHc_X8yC8DXPqHaYSu8UA-2iGJklrsgfrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7878" target="_blank">📅 13:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7877">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ArchiveTel
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/ArchiveTell/7877" target="_blank">📅 13:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7875">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8C9ugUY8U4o_i84SUIVvbdrE7aUuqSZbYn0hHwyg6nLRO88WMCEULVXi3ZrYjCocd6w8vvZ7411zvlXHaTjJPgIfx1AGNaascHDfj3dRtmhXL4sPOveyt3rwylY1Q60FXbhm17eu4CVaU4bkxNFkWT_wiWr64bLfvDh7NTnxoc70CS6kknctyb_6BzbLua6AyLQbZm-q6GkBJ2KGezuhphQuenCimYMdgKtaDtJYw2O2CAuW1-UkfABGXj8jOrfDry99RsNq4i3ousEcAnEBtLRBZN1joW5cI8t49wrd_3OkLNXFhYu3lkUeYkYW-zX4tc7l3YiwUtlDMM-PfsoAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
#حمایت | کتابخانهٔ jev-pilot برای تصمیم‌های سریع دستیارهای هوش مصنوعی به‌جای پرسیدن از مدل زبانی بزرگ، تصمیم را به‌گفتهٔ سازنده در حدود ۰٫۳ ثانیه و با عدد احتمال می‌دهد.
🤔
سد فرمان خطرناک: دستورهای نابودکننده و حذف پایگاه داده را پیش از اجرا می‌بندد
🤔
…</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7875" target="_blank">📅 07:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7874">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🎓
دریافت رایگان ایمیل دانشجویی اسپانیا  با این روش می‌تونید یک ایمیل دانشجویی اسپانیایی به‌صورت رایگان دریافت کنید و از اون برای وریفای برخی سایت‌ها و پلتفرم‌ها استفاده کنید.
🆓
📌
آموزش کامل دریافت ( کلیک کنید )
✈️
@ArchiveTell | METHOD</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7874" target="_blank">📅 01:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7873">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvgV98d1UX3A4bzBiRslig9PULHD5tXrxkmVdYJT0Ft2MQ5TPADmWuTua9w-Cxgc-uBuLjmzY5BwYoD-npO44IiZyvLefuuj5neqrXmge3YWO44Y_Cd_802Jjai3LUho7dwjFdGVxknVTCdUeF3e-MoU_JeVJHGZnANjhNY6w2FvXhftU0t-fHh8Bz2ozs1O3HOR-4Y6z28oD5oAJaQ_4bwnKYc29PbA7FCoyd0VarNvLbv8ZYmohlTEIlTAdvLZtghXL2Uvqi7fej1IeZLsb0VpXXsOoN1Qj5ovuCs7A6jAjUCBhQjkXpRhoOUQjZ54OmCGTug3xDCGeYixomTRGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/ArchiveTell/7873" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7872">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">احمد سوسیسا رو تیکه تیکه کرد و من گذاشتمش تو فر و وگاس میخاد سس بزنه بهش</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/ArchiveTell/7872" target="_blank">📅 01:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7871">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خب اونایی که شبا بیدارن و چنل مارو زود نیگا میکنن جایزه دارن
☺️</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7871" target="_blank">📅 01:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7870">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7870" target="_blank">📅 23:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7869">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHp0QNi6S9CZjCowYb1hzN1BJKB2p2FJemnthRQQ2KRdttsZnfk88hXGR5-6C35XONvAGpHgE7Jrjs6a2yvsuaQnYYD3KLvidvWEXN20LpWsamNCwsT9BtxZ8w-QiP4jADhmFZj24q0q21AOUgpfuCAcgCoqygUNkrBFNXLXdjDQYeBD3OOCpfDKzB9a31um83IHtYWbfERjxvYqvxrS_tJpv-jIKWt1NnO-9hpNn8akSx9k1GBHrZSPMZ9aGxNj6aSO6yCbvoAS_pIcdWP0GPS2OLtaeh4cavsOOoefLgDfl_2now8k8eMshjO6BVRlwbKDnpXlAFoykFq5-4juYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7869" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7868">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmPMGw_CXHbroM314u9KUXMFpfPqUI60C--2A77JeMy5EvupNDGQCZyLJepnWKfPKh1sMn89huYgUvKCRFh92Mtz5fY5RAu-xr9ehb6uo360xdQ3a_5SmKHNlSCcNtwjYMT45--6yQS-G5tXoGa9Ib6R_GNtk4T2sdgbMt0OeGGqowHPuDI9W1GqkPv17wVEB4sqGR_A9VXFE69qQVNoJ5VE_MajBWoJaQ7bwICNoYI4F_-h9r0G2-hiy45Om8n-TXt4qssLeTxmwAMG4HdESGpIWSYdPCDv7_biJjpgOC00duTkvAvs6nURTwfldFgsNcwGdKNBjTeI5afYXWMe2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jT1PS1msLEPUMVpwTnJBM0Fv-BRjr8mJ6kcmXICCGSNAClmj3H5cvKr1N8yI64SQRo4lTpHmLLtEbeyrAMCIeWqm41xO-llj-btItcT54vF8MXkqD0zHajeR0lc5zwJYG7CoNq5rMLeEX5f97-OSq4LdhE7gMaUERqPSG6jEnWmOerVRi0mK9ZCz8qEn-aL2oBpPbxQVk3DWWQtshr90fZA48-rjqfokf6z8_CsZFPTYhBkHYJop8xhVclH5nxYs0YfVI_mdINlQUoxMlbwa470umjkXLiEpdjsBAvC74ES1H463hetZEO5XlRK_y87pgacl0WbBaIbuqAZt0IN0Yw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7867" target="_blank">📅 16:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7866">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3Us7Ac0deZN_x2J_nkQNcLkwx93pPCzXOtmPHyZnbfWWLEBLjGX_rI3ykTSrxPYdNR3XDIlWS2Qs9ndluGhZqmK4kCNKYBNTYXxNfdxShAZ3DE-RqoC6V6JBCqbLaqr3HHYQKGNG2N95hQ5vSmFEFuIY7Uzwp41t8pvMo3f0s2HBRnrTNIHpH7sRvMaTE3Lgma_C_WfYtmhBCQWmrwqFfYFDhkqNuUVmoY9aX9nLwScopRUe9QGKUDQiGL4zREbEp_S8t_h5WMGOEBfEZQyYKlKNjpHX1PZ5Dpax1hhQ97CIa8-KBMjvXPgJLT7kHksB_Ll6o47r4T7i9OZwsFAQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7866" target="_blank">📅 13:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7859">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BrOCbSG8apxFv0I7IHyBVGp-hlgm5wQnZNCpJ6KWBmwrWdOK6I-txzlewGtAdu3HE8jj7b89E5hX14ic_-Kn9ei_xG7O7E-jfT8jFP5ivi2-d_GkNNnJxv9paRB0d_InYhgDPOFvz3jpXlRUky5kEgkJuD9bG5pjpftjzS4B880Qwv_fheTlerOMyjANnZnyLrGxsBvHMeYLPZHuXNVFgEZOqmxzGy11l35gVWKzN6-jC8ldzhYRq-s1EvhHAOC78AfdJ9DXbfst0E_MlyFbt-f5Ajx4BEYUD7VFru0ny1iYNl1lXtxv3jL1HBFQHsOrTLDcWGUNyyjZpTJENeXZXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VwjLjnj1Y45KNprrHAwc_9-2_2TDc4iojNGmvhtNsiFJgnEXEzjngz_BNpPbMnp9zLpfh8wZFH06uRyJbCtGP5vilDsS6omSiOsMj1qAHz4lmfPpTP5Eua-zpZ31MI7eLBYuRGySnwIQ5AmEvURfJYEq5u66ev6Dtj-woEXqjFlTZqHHplgaJkF8uWae95JVbCsbiihY_pbuJzHRUMN5Ch_jnIUI1uNdffwohGI9Fb7JL4owi3uofJfmCWQ6OmXbb3f-WtRNf2DIMcXJgkoC8WK1RXb1L0qoUoOOxy2QjKPk0hMmdyGSU7kYQccBw03uM3QroXQ6saxfxpSiaseA5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iDncnWZnHWqhg2GLU29ZdMWiITD9Q44GoXv-DB-yw2W63FibCB19HuAIW8jjOuEJ07_LsdXpr9uzJRMN9-lNj_rrXXHYVOo-Bui-F6FwRuNtMe1X8QSffCaAZiWgzQ2gHrmiRjqjilQ7vBt_G8dzupJ5C4QtAOYIZHyY57N_fRlZJRv_D-4_rCLyduzlAoGryTmrc29L1pDVOapzGxVfOzm7Ww2CsZcNqAqkwC-i9sPgvG2Ptktxaasl0x1g4BeqlNz7Z6mOWzWFCAg1xoPFARO5JMW_6Bht42Cmnfac80HkAPttCcr8k1TZoVXXjc727RQN7zaMwYsAI2ayTtdRWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1228320104.mp4?token=B34aQ1tAHMUPTK-FXgKmVokxmKARYZa8adZY7ljy0Re0ZYKzu5ZbaU7jHP3r7cuAluQbgXN-1JQUFyxxdmqH_TyPGsEFxj50ER5mqYtuN5AYc3bO-8rt95i_beqvxGy071aACutZU2C2VaQYoI0glroLmAPSm-kZcLFYWBPbGTrAn7mpDdC51S3XG-TXLk3Mtgt1OfohnX-lU1v82qb06TUKcxU0_-YaFFXcqkQf5EZ0dXKwWL7tq3qN1MJBaVGCEZXLiPM9ge6diD3sMuV-CYwew4woui4Ih4vYZSDOuFnPz7r54m2BeqfVQLbzsjdpDnbLy0tlYMsiQcpQ8Flu5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1228320104.mp4?token=B34aQ1tAHMUPTK-FXgKmVokxmKARYZa8adZY7ljy0Re0ZYKzu5ZbaU7jHP3r7cuAluQbgXN-1JQUFyxxdmqH_TyPGsEFxj50ER5mqYtuN5AYc3bO-8rt95i_beqvxGy071aACutZU2C2VaQYoI0glroLmAPSm-kZcLFYWBPbGTrAn7mpDdC51S3XG-TXLk3Mtgt1OfohnX-lU1v82qb06TUKcxU0_-YaFFXcqkQf5EZ0dXKwWL7tq3qN1MJBaVGCEZXLiPM9ge6diD3sMuV-CYwew4woui4Ih4vYZSDOuFnPz7r54m2BeqfVQLbzsjdpDnbLy0tlYMsiQcpQ8Flu5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7859" target="_blank">📅 22:07 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7858">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASJHc0LdP59-RpL1MDoxQvjgmGn7wk8sF7EBSeD7zLV6EMvY379x0vbGJdoShyiGjC3wLrU3jAtQJXIo2ul2Hpgm8Ftyfkb97Q37APEW5uG-UCsuzRK53TVCSbHiIoJbiO2VfAa-3fZd5gu-eoXAam9EKtBbscha1WIul5dGXf79Pd_kFXeGsCW_uPOb95VmKV8jaTFfo78ZAIDi6HLyNUNiHWLJ3m4o9dGe-sBpSXHDpgs06dIsY4MQMYJRuFex1Uu3pLzabuLPR5JAtHtHUZViX0hb-ow2930zYVPuPPUuY4Yi0ToGQ456f5TTaF-jDlBkiJlLl82qYQT76iEm4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام دوباره یه قابلیت جذاب اضافه کرده
💥
🔥
حالا وقتی وارد پروفایل کسی می‌شین، بالای صفحه می‌تونین ببینین شخص معمولاً چقدر طول میکشه تا جواب پیام هارو بده
🥵
حتی یه رتبه‌بندی هم نشون می‌ده که سرعت جواب‌دادنشون نسبت به بقیه چطوره
🤐
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7858" target="_blank">📅 20:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7857">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruFBg9tUnBTpipxztfJdMUUN-V442v2OczHfF6wwy9jzOyk4ldKimi8mZNTtjValUHzzLzKr5c-gcEt5BL05u52BoMcrTFnDyoLYOrWTrTUhSEnxk-MXXkBZVHOczaClPypFFM2lUXQ90uEqB21wsdnLeSPQGRdtgisaniA8OAyV3yVPMtVOWUlK04G0jlhpb-Rfry1md6S6-M8Zh4pNa0GuqSPT-3BC5mvMHF2sgHa6QPrOxnp2oEZgfEv7pECExpc1TNOKsU0HMOrtjj-B_dv3mI5zu34WjWVI8SEAkBamjBXFEBOMkj1RWoVgf3L6tQgQxHwKeVsdti4Q5D_gxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7857" target="_blank">📅 16:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7856">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7856" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7854">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXsoZ09X5wXR8hZlfFmeazsRanOnmdos4w0iYTGVZ2GSoHbPYQ5E-k9eyd8LStYJnAboWX3q_UPdfYQDyFGCvhHDv8lT580tMu2N1NpX0kCj6gFDrz4I3z6vtSSfhW1hM6lU2goI4esh2eC5cluPgoNfdqMyVqks5HI23vHbI6kqAbbKn-cDYB75LAJB1iqfaMu7A6T9HFpkhuYTCCVF9vx7Phpqihvpm17uza3epEOAHdPEcnrhwrAP3A3S1144dMjskLDPMo9uv2C6WTRJ3OvPu6isutgwzJnJcCuscwJ02GauLt5_TW8BoNTQs0VqhhOP2SWoShl9dIQoHsvmpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
نسخه Claude Opus 5.5 هم اکنون رایگان است
🆓
اینجا بزن گلم
😂
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7854" target="_blank">📅 12:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7853">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">Opus 5.5
کاملا رایگان فقط در آرشیوتل
❤️
☺️</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7853" target="_blank">📅 12:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7852">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7852" target="_blank">📅 10:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7849">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=OqY_vCc1mkgElLgYHDCybb5qWJqq8ttPFGcMB7HSsRR9OzpTR8gyfevGGhRpURQrkSEwcx5Ve-R7R9OAaPkyziUTboK2-5A7ZOwec49NIG1mSIkGZEzENb9ZTW3sksuNhkFbIEgpCVPESIAA9XFQLM0LE93kYTFXCnbAxyY7ayz7nSwWWklho8yWjh46PLwwWjLMM9J0RgGJoN5x6SEV2qmXClak6Xn_LUrJz5p12XI6FrbLgehxn7wdlYtnZIfLcXj4hkkN9mF2Dlm0bH_enpai6gw2HzfiPCQXAzG3JGQtf5rpzJS7J4Um2zXtY2BGR51l5s9z4oG_lAo-xJASsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54de4db4a9.mp4?token=OqY_vCc1mkgElLgYHDCybb5qWJqq8ttPFGcMB7HSsRR9OzpTR8gyfevGGhRpURQrkSEwcx5Ve-R7R9OAaPkyziUTboK2-5A7ZOwec49NIG1mSIkGZEzENb9ZTW3sksuNhkFbIEgpCVPESIAA9XFQLM0LE93kYTFXCnbAxyY7ayz7nSwWWklho8yWjh46PLwwWjLMM9J0RgGJoN5x6SEV2qmXClak6Xn_LUrJz5p12XI6FrbLgehxn7wdlYtnZIfLcXj4hkkN9mF2Dlm0bH_enpai6gw2HzfiPCQXAzG3JGQtf5rpzJS7J4Um2zXtY2BGR51l5s9z4oG_lAo-xJASsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦀
کلاد Opus 5.5 می‌تواند انیمیشن‌هایی را از کد تولید کند.
کافی است موضوع را توصیف کنید و از آن بخواهید از پایتون یا جاوا اسکریپت استفاده کند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/ArchiveTell/7849" target="_blank">📅 10:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-7848">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUTZXLeh9ybOVV7o7zro8WT5adaG21y_8pdB9c1TAQy4OdP6xLL0LwAJS6Z0kBTETrn66EPbNe2wCZRNKeLJw8_qsAnIqmd-yjxnOsNRZJzUMyKH3xSWUFbKvewvHXgPal7Y2wHUedqFYPoUyFemTAQfNYqTuX6MnZ7pGw3uPdFKNtacO6S9QLLLYorYvwbqqWlH0Ur9Z6EvOB9fAKGxsCWJbPw3rAw0-jRqhj7Gh06iJsgzX4XmUaL_nXdwHwzKjGv5Y-cedpDW7sXBImbdfHJo3caO4miHYG3ry3vSTQ-Pzs8ulB4okZcuFviReywWxJWIYNFUeER3R1MSBSYcpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک 3 مدل منتشر شده امشب
🚀
مدل Opus 5.5 با اختلاف زیاد در صدر جدول
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7847" target="_blank">📅 22:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7842">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NlcA_ZM6Il9Kbt5-oH-hcRmYGB02N1GQBQNlO8O-50X9tR_P-JJsvRmr2nvirgQUxZ1gEtkXi_myIuQUs2sQfpGHbu1AFNPb_feMgzLosvOyc9DRFR0H98UwubkiM-ujvZpSvxKZnJ8YKJcpqwShfW9jG_gKXAsTOVfMc-Tyge6Wa9rCQ9rm6z1RVkTDU_VDgp9_Ll3ygNZWWLH_QBpjkUMTRl9gcfTrIank4Fc80tyeuSTfVQGDHNLUrdDia_S2QvNgcqRl_agDp_5FSvgkskvPSH9iGIRCYOIsg3nOFKzkzvwVDm0QcZjRqy4quQU10xRi88gjDFfOFZyEHOT1qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HHxyMAoJL-xw_i2hE0iKs3LI2diNfiJzLmyyBvhoJICTrZGhYC8vtxpva7c0rB7I-oxGRDFnS5RI87icfz_uqTwOXaIZX_LmnlLNGZUYTca6YPejQRBv5Dgi_FioO9gSQ-shbjCOU84ybKqcMZGfsIF6LvwUyv_JX3R7Z3rbrB1kLiljSCJ4k7DHOmRYkKSsJ0HeHl93BMJ2ITbOQp7WWn7gMqfY8SQxTcBmr3hzI1mktHfnh5VimhPQ4we-cr19q1zigmA4IuzcL9bZdvNMIMbwDlNcIhvs-_oBSpaw6XfJcd9LrZj_pqfX8BXOYSUzbOuZAzhEjyPNGVspgsGLnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quMeQ5OiiYr2ELRFDvOLoXXwOe6abrzxyxxaLg0XMvPVkHTspbxJ6eVjsKM9UO-4TVBCV8tA7cfbBy86vkViIcPNDXTwTL5tSjCZ2XNEilM4s0eXPt6EpkUjFb1ba8_7GjhvOFWk7JOFuXiMLZ5U9xnsjoDhSej6DLl9sDTZx1AHnjRddyeMtNrmkeIRJoM4XFP0G7EM29s37GHly1RPkU3YGXzS8UeVQifCWQM4cl5RzhDEhvO6DCb5IpN5QmrApEHkz_ttypjNWFAGzBvo4Y9tKn12jMBHWPmSl2NN1c2V4NmMprhCeqzw3kxeFNJO7855NmI0oAjf6exewuO33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lM7ygD2Cv6Oz0eGVbq9lMEK6nOVCAZ5iQufVrGWY7bNDAAp5Xip7U2SXcoYo0HIwmU6d1GmGbvIz3FWtDURuke2UrXG8R9EtwJpBF15jRxb10IWFP3fdkoNY5LpSs_stqTxDtO8-kyIca2fojH0pXN1yzez_npoHoOm71kwNj9b_DVQs4M4pevDoGiXTtSnIpdv3I4147Mdb-aIE5T0piqajHbvNDvan1UY0RvqIwU0yd6A17R5bZh_T08rF3PTiUKCn-TNZ0t5BI6zjJfcPVee43EgFEAdmvmwWt6sRMilv0-8rZ82Xw0gIJeYGtTTSNeCBCQ5Cn7rVApm9u7HOtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RKkDGfqLgtqsftY8bk6XaCaEYizvqxV43FkrOfB7foCshsujjAIqPyTP9EKmCv1KsXn4leuLsO5PYvy-_OX7W7jJvEs4vmd2pWdqXvndW9VMaXQxUIvbowTLdHFeNpYFPXnv3N0TF-AQdh76UQ3I5mgl6ROGVPDggrUOH8BM5uHcf-nYSwemzBwA4yM0SxUz-Vdb-k8A2r8v4zXqQD5xgkz_U9a8FrL4nO7DwfzZ3IC7aZt9LBrSAvVxY1mZ2D4FJ8gwvoHXyaP6qrs9ef5jxx-drinBa5m0_oSR35J05-LgFBwX1gU6AJZDlAyttmqDApCI88EtgVyWqhBSfoeY9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7842" target="_blank">📅 21:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7841">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKLAUrLktzhmsMvoIshq6XOY5RPFPsvj1cuKfdohWxgrZiqn1X-w4IcuVvDe9D_PS3EufNvZX2fLOoSIlGHOvu0m7xz2Kp1Q3hsnSeM4reLtlifi6aatg1d86m58PS_JkehQv5gjJFxLIapHy7wuO6mYA-6YqvNw5UuHbF1iBPU4q3GnvV_TiJtCLs9_4nl1AoKNf1AeP1aV4VE-a4qih80Pwn5m7Pm46z54NhFWsk22rqMoRTvHoP7e2QHRWBP9allZ0_ObQil04SqK2F9hkWTVxsRfc5oP3caD4Epz7NKqzyMIEHHHcQSRx209SnI_qLy7UB1JagQSUcX6aqdF5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل‌های GPT 6 Sol و GPT 6 Luna عرضه شدند.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7841" target="_blank">📅 21:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7834">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8059db989b.mp4?token=dHPsyXXmm3kpGDCugksKxYBwH55hhOS7StXWUFomDx4NkZoqnB52t54qzZNVcNbF_0cV0RCWJv1MwWVGnGLwitrLOV7E9qMtFAnxbqI32NTMZFYLettocBAsJHqjKi8KkeNW93YOtNSiZwoYWmU2xzP0jGt2nh_k_Les3EUQbdUZsLYs9fhbzWvOD09xFHoRUGXepyfhYel8X83-Su4BlocvwJEqDdF0M6DuSeJRvoo4tpg3GmAcQ6UN4fknOzH-1GXhzUvXdcmlIz5evN0SUFpGTdUdnK28m1yimyt3NB-P_sJ-CTHyUlKEbE8N3PYamjfnF3ZdNaiWUtng3tLroA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8059db989b.mp4?token=dHPsyXXmm3kpGDCugksKxYBwH55hhOS7StXWUFomDx4NkZoqnB52t54qzZNVcNbF_0cV0RCWJv1MwWVGnGLwitrLOV7E9qMtFAnxbqI32NTMZFYLettocBAsJHqjKi8KkeNW93YOtNSiZwoYWmU2xzP0jGt2nh_k_Les3EUQbdUZsLYs9fhbzWvOD09xFHoRUGXepyfhYel8X83-Su4BlocvwJEqDdF0M6DuSeJRvoo4tpg3GmAcQ6UN4fknOzH-1GXhzUvXdcmlIz5evN0SUFpGTdUdnK28m1yimyt3NB-P_sJ-CTHyUlKEbE8N3PYamjfnF3ZdNaiWUtng3tLroA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😎
چندتا کلیپ باحال در مورد معرفی Claude Opus 5.5
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7834" target="_blank">📅 21:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7826">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvT8QURglKYdbdCXPJaWgOJF5TFKl_s04t9XdlELV4wqClgbz7PJz2acSygXiObKYmJx6_It6d0QA4cHkzVZeRRKZ2S7mQwzUbFkRaHxsMlzKRNpVQwUnwE8V5feSekoDGR2XHKSnV_SS04-3h9UVywxcnIr9kKhG52S_B7ngVvYYXfdeickvOqRqlxCHXdh2PIAG8ZR9e0OxFTFYzxdhr3zHPhka2f0XLLC6l5nVlZcnIiznp33NbOsDAuwntYorFAvLpR2ZnZvwOz2EwViKd3A4Hfm1yXwgYUPUK0CwaEsAk75ejVxTUeTwDDzOUFM0rvUJyw_p0dHK8dV4rGzYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbXEElwfhAGZVcdCKA4di2nhysjlf6Gyw9EF9ZSJqy6BS3PNpicr4TPDRN_hsR9PMyeI2Ym3JEbeuzUlf-2uOtp58VGJs5KHWEo1bIBZVfhlNQBj4StRm8JViknifXI7O-7D4f5hUYLzRcDo5Rsmv7O8APwUqziPA4DRbhOhemdhA0HbrGtN46aJc98FRfPrpLxDmnMu-E4UNLdrdB28AToZX-VcvNPr1QmMa3Ltv8kKgVJyOJ_NA5VZRw46QYwDyw-YdmUXew3q1DBqAKgQoFpQxQi-TX3-CZy5XEc8AOauQAR2pBmgZAIBfv5Qzqz5RkTf-O4h92R1rNz7jstmpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/ArchiveTell/7824" target="_blank">📅 15:22 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7823">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-0ciZVLM32c7VuN64lvOFDBOMJ2aPAR8xS2FPJ7iyJGsbX117ORIA0cFQfNDqnp5FaTAztLKxgWUyT5FY7bqDfvGFCpuVjncCjdD8O1JijSP2W3DGMdOTvELug7XN6owaP9mTe1Ouah-JUMNm4C0DWfMDxiETwmXl_j3n-uxBV_85GRyPdr75d2wwqbAOEUQwdQPOvPMMb1ZlfymMKs32mnAikdmeyW-Wtt7ufUF_4HGcHoggR6Sv-5F8_lqVo0qWyD5c5tFWovpCA78pjl_p-71dNBRoU3Pku8xMAneSCd6GXLYtEbqxq-560tQyyNSdIZqy4hh5TZwDgzuls0Yg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pi1OqcluMDWErhYwEvLOw55QlTc4xBssieBsVaCzUCb57vOirELLZ2IjYiqqNB_52-W0f92etKTTl_NE5zghXiyhrgiGHxejRcLVqQRrw-d6cDUzfidiQ15l0x6C3C147ATPnc8hjEEC4ye-3BZv4T6Cypv-f7g24McmJWn-lEiBZlg6p0a9hBDTYRvgC1D0Jv1aY8gTUoDOCvDyP_s7sBtIykJBCanE0_QB_IpGi-8nrBy9FWcql1U01qvgEKUk54ivPOXjtph56ZjVLM5in3cz20gNYS4qBxKC6KLyfHd8Q3OFj-Q-d7Lvoplj7dGL9NTnp32dgvvTKr7LQh8Kgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
وضعیت فعلی بازار هوش مصنوعی
💀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7822" target="_blank">📅 12:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7821">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7821" target="_blank">📅 11:07 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7818">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwVsbidheFbCDd_ULnY6vikyc-4KlIsw0bMqEmxptXcdaw9BOAnLKiIii9oAiWdTgLYbhXktNx0bVU2iHeggewdlizHk_qZH6HGSzq9zq5BAgiYcVzf1D8LjSn3gRL_5qeN69XneguTMS8DVbpuqgui162MawTSnH5W-Kn4a2D1LNIWA7SNmRc8I2yOKhot6NdjOoeX1Anfx_cWfAuyosMpSKXy6xw1Sx-3-iDWFu182voCc9Wb7totv1ISF-BNcAOBj94MOx6KQor319qhZkCtfTsgOczwfpdRhwuzpahW9GkeaQrIUXWjglegZiex0eL2RdyFvVGp9I3h93dczqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NhXoZES91RX_VC5vyUvr6r5CtoIVYsdl9Olg-x1bKJ74MTk9_NFurzMPgJgX4LeU0H-TCDGWAN8p8gLpG04SYUY6-ZdCt-T8Z_pyfI8HKunqq9ITq1BBZVPrxdId0mCnEr56ThWHzbKvmkfyT9z2fS6t1kuQREa3v3GONtWQz9JuSo1H3i0lgMBcQGrtuM_s-VORsq8geTvtFMXamGl16usXmUoSaThxgN23DB3gG1CMPYvZfftx0ozfJ1yW9GjiqFiEnPs1MS9SMTxogwHJYbam19d5mI58C_o2bWzfm16MaFkGlYuBOZj_87pDoqRRbCBBI85i4e_XcmwTd5qzRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ckbWTo6T1puQPcVfUBFxnQ_hlllOvg5tlUt4lL4KLC5KFKFqKJ3yNm2vOYEfw4d_O6UrSEoo_pceEvT74_Jsp-SEp4Qow37gbvl_CwPqHfJds8ei51iqNfyFqXbkvrtvJRQMNDC3nboQOSqTLQmU4bY4OAISmXuiWxBBuBNy01-z89u3vDNlOTUWqaKEGANq4kRs_zuXVPaWpVR7xvF22bG2CAZELfLupLGSp5M8qqkbMjLtA8YsX7mbweRJ1B0Zpxsg0QjSebL9HhYNEwKpTS1I9enJZloIZJk5ePOt_-I8ajKNK6WSh-3pTNf7fHc_fTfDlnL3nf2UMsOPorLN5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7818" target="_blank">📅 10:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7817">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H68VzrvMurLC7mRmt18wC_E7y4VWVq59FRUop30ToaVATxK0DDTQidqew3O3G2ePXIRhoWs53qUHqe31L4CynXN4oqFnSA6HweNCiSObWYMWixtqG5KKvgmjG1shoHYjjr8wzRcPzFeY6KHnSfwqnkGBgH0EXxwV_HwuLj1737SUX0KCRcOk-kZ1HL4lOU4s9OL9S-7_bLHUqXQ8gD6cDwwVBDYJnTMjehTqU2ZqeXdwyJ61SsguXPJD2lKFDJVMLR5hIeVMPmFa0aeLs898pvsMMGdraftt0auM91b6iOcMV9btrUyy72gIkwEWBV0lYTaAWcLFcQtDEoKeGzKmVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی
یه پرامپت از ساخت بازی مار بازی توی حالت ultra speed mimo 2.6
توی کمتر از یک دقیقه واقعا پشمام
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/ArchiveTell/7817" target="_blank">📅 01:43 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7816">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYHsqC0eiU6t8DyvThQPjCkdgt5MaesnZNE7KIxLADYBQVZmhCuueYVDFFxiI3RztaWVRQQ6f-QJKtDt7Qx4w0pFg2O_TqxgNxcPMoaNLgi76NuVxJV_Jdfa8eUmb1sqHM6qGKY-UzEKWY9DDsRTuO9itaUUGprbqouZpu81pxetgzXNColIaWy7sDUrC52Q1vwFm9H7Q4y5UazlkgMj8KrWfEgonp9QrzbWVi2fhu0TslHk2xH0jluHouDKtpvEPIvYvDxqb23jpNMnko-865hoIxTxhyn6Ne5emis_wJwFBAM-WNe7zX7kBXYT7brNLKLrwigdrfaaZXrDGPRe1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد   درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در…</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7816" target="_blank">📅 01:17 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7815">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔥
شرکت شیائومی 3.5 میلیون دلار را به صورت زنده سوزاند و بلافاصله مدل‌های MiMo-V2.6 را در API منتشر کرد
درست چند ساعت پس از پایان پخش زنده پنج روزه آموزش RL که در داشبورد عمومی قرار داشت، شرکت شیائومی بدون هیچگونه تبلیغ، کل مجموعه مدل‌های MiMo-V2.6 را در API منتشر کرد. سه نقطه پایانی (endpoint) جدید در کنسول توسعه‌دهندگان ظاهر شدند:
؛ mimo-v2.6-flash، mimo-v2.6-pro و مدل پرچمدار با سرعت بالا mimo-v2.6-pro-ultraspeed.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/ArchiveTell/7815" target="_blank">📅 01:00 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7814">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=M9DF0jf7aLxnSm76K39YBk8PDy5NWcsZRTkc0SmnTMs6BBoRnq_ca0fTXdbC8XUQmdDm2-EbY6ckrRpHh7m8Piw8AbsXuFaS-4rtAt9yPMOPEh3nooMslsF_cESn58lEWHCEgVbPG-SO3ZJrG9YECplW1P072e04pnjmi7HHe4KawZxFxcEA2v40hYoictAsRlxwT24Jd2coM5Co0d2tvNDZWbKsZEh6o3A_7uS1au7JSN7w0J-NjTFhsZBhzGSxf-6fq-5qFjVtw7OLX7RisjO83Qv-UcnOituzIE7oGlOYJ3YNgOjrQSGetatOY4tNdEkeV-t2rX7O0b1jr2xtJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e0691862.mp4?token=M9DF0jf7aLxnSm76K39YBk8PDy5NWcsZRTkc0SmnTMs6BBoRnq_ca0fTXdbC8XUQmdDm2-EbY6ckrRpHh7m8Piw8AbsXuFaS-4rtAt9yPMOPEh3nooMslsF_cESn58lEWHCEgVbPG-SO3ZJrG9YECplW1P072e04pnjmi7HHe4KawZxFxcEA2v40hYoictAsRlxwT24Jd2coM5Co0d2tvNDZWbKsZEh6o3A_7uS1au7JSN7w0J-NjTFhsZBhzGSxf-6fq-5qFjVtw7OLX7RisjO83Qv-UcnOituzIE7oGlOYJ3YNgOjrQSGetatOY4tNdEkeV-t2rX7O0b1jr2xtJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل در حال ترین کردن
Gemini 4 pro
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7814" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7813">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">😎
از 265,000 اعتبار رایگان برای استفاده از مدل‌های برتر مانند GPT 6 ASTRA، CLAUDE FABLE 5.1، GLM 5.3، و غیره بهره‌مند شوید.  یک حساب کاربری جدید ایجاد کنید و فوراً 250,000 اعتبار دریافت کنید. با ورود روزانه 15,000 اعتبار دیگر کسب کنید و با انجام وظایف، اعتبار…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7813" target="_blank">📅 22:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7811">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/ArchiveTell/7811" target="_blank">📅 22:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7810">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KV5iokXMxwOXDCmSOJJjmMsx9lq876BngBgzwMrF57VvoTvmfP0EX6IR9dn4zAWgnFKoaHHjq9ab0ekqxwokXl3Wqu6SzMUCoNdZYMS_bID45NixIX4XYqDD4KaAAeG7uGbWw5rwkjZL2dcFgNATf1pv6t5Q7Qbfwpjbo3bBqssVWE9Yu8Q7mRkGyWN_7EpZXYgnBnoJfYODo2orLsnjc4sau5JRB82ct1c4lYJf_hfDMQMxvpJHu7Ra7_3ExFAZTOHNEedhMUw62MZX_tB1hzuG6uEfkQU4_QU1gNUeTyZzWY9QYyj3ktWD9oY5yNbvAG5l1eEJXNCQNV02-GmPZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7_Ckayw1-lYveqoiDEezOJXZ3q_ob8_a9LcTkuGTqf6Mh9QHdiXXAEfoV0iymafu53glNkT3kbltdWnJSW38b9biYC1_r4m1Iu7_pkLxVFMfzkGAeFUdxUIgrludPb8phHXsr9fFaEAZWhOMc1rVElMbEKi3yzz5Q6JEabbwzdWUOD58MfyJ9JikYB0sW4gEuLFu5-0wkeU7FcZdNL9Z7Na4wriVaXTbJ1FB2pnAsfgJl3XP5OiWdifQWywr6IY0qmFIe5rf452MFGg1X2PI6mF_ZTj1S3SEpq0JNwQf047GaaQQ_xVBho-cYPMXS3Uuf9AOB1jqx4vVH1eD530rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sks0u8_iJjjgEHbPp71eOwCYYhxhX9iaPPLOD_M4SoYA_WJj34Xf67Wcdi0J0zHxl4v94f7ENp2nmvNRBmBbXyIkRPVZx4sQItaB6K-bjIUn8IZtRcnGouywWGwKyF_xKOfYNi40z-vsFK5ulZfSh_P6C4QnNPZZ86IBGoljAa8I0kSaN98wYHNmDM6kEzm2wA68v6MP9emrbeUS0dyvQP_D7x3ziJXTpGzw_GFQnragsjVOE6021Oi9RMGC4DFh0GXmrmves8A7LhVBKuL3PVCJOZZPmBInVUZQbbgNb_FbcFsWQFtEk8s29CyCdewh2pqkJJ46h58Jte2fBZjJfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzxNx3i9pY5UgnINIom9s-cyMOwLAK5tc0hraNNV02GA5CVyv-BSD29k_vfKbdlxVlHJTUTpKMPdxPjN799ifNjuabWwjnUnb01pPdBG1WlJWa_yalF3v6HEHTnqx4vT19Q_kBojg7DE92grxl9E_JOHsmtjA2KFapNq7xQ4_NaDnpAkdB8AzPdinyhR7k-6jiu7zYSzrt4aPxJ2Mz92iKYN_bXZvMOVbS0sjWIBOsxv9BWiVCL5aHf21dZacQ-ikxvOe8GMcRAfyOmDOTEMPSooDMBCFSUMaA38ktXX-RcWOg_uAzfAX1TfnSoiyaVgxNhtFjWNlmAUyLfjS74fmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSqpzi-mUZA0yJE4e4CUU9LyfeccTjKN_HxDBG9gjvxRAAZXopj6nOB8yZ5jST8lK03G9_CSQhhLuUYKhFO2P-uGzPhGefbV6GyvJAiZ_YQCvjTp92JpjaHqSWjU6ZGk3iYG9uETTX4A--E9z5s2JP4SXjAAbumhri-nClt6c8CXrYTOLBVEXLK6kZnVH4cM-692988Zahhps6pq6PO1PK9OnB0C5tvMjXoT15CJqdFRS33yjbM3H-DAz5P0emZYQ3iPLKtYPx7viArVaQIKOM15WQj6z5fnnAdpSoaS9sN0XL4gyLTar4FX-YKfID8CSJK1_QiOQk_Rl-2GD0J5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانلود iso ویندوز و آفیس + فعالسازی رسمی رایگان!
همش در وبسایت زیر:
✅
https://massgrave.dev/
سایت قدیمی و معروفیه، سافت ۹۸ و اینا همشون از اینجا اسکی میرن
😱
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/ArchiveTell/7806" target="_blank">📅 00:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7805">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZ-sy6mI9WCPa-DvmfONCkJlUWLfKq6-miDqhaHqgLiVIFYoiufso2gI7k55HBmPyzX1d1qJIGlE8SPAUIkqWYQOdHMt1uXcSfqaIAtc7uyPSQ42vLN4EOMLXRNh3fdHqv_UX1RJPBh98HU5Dqr_sS1qnrUo2J_SauMNrI5ppA4AUSeAbJWRV5hnNJ-o3wIkwNS916uhuP98PnuOP5aAVDFqpqxwDT-AjqU8nHLk3oQPKm8JBLVHncOqtk-T0amrNSZwH5gNc4cfHCIrf7zlJhFLgwlQ1tx-lj1Q_AvDzuyxHAEFvHJ3SPyN-0TYraKgym_kAhkjponDxUiNTTTlFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgb9ekpWREebdJ2mbXOV3DFp6-PbKf1HurMd-i7S7Lp0pRTxeuLlo0BCTScNMU9gUrvZjxjuv0QVnq3pP5ZLNZgRZdHjFjcMlUrVvNgLtVKHl-CYp9wkaveV83xrBAFlFyx6LcW5aQZ-bn_L33ME1uroC0zstTOarWxF-feJj1-v_a8yzPbs8j1H4ux_sQH99kk0fMWtqcNR73E_e7_7CDORqz2l92K8j-3y3zciC_l2trMXWx3TRXBb4aJl8xOhDK3tfmL-YRI4lUKJQm-ZoBl0AEW-DE7bn1AFBUxYLXANNEHy8YFXamhoxklUykB5vXuMSXeME2Ci-E7uO0RWqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7803" target="_blank">📅 13:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7802">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7802" target="_blank">📅 10:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7801">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XD8YbKrtnKs7TEyXUrgk5EG1wzFrZaATVplKnrnRf__krHCOLQcVbR7VCZ80w67fMli1LiNYCsj_ubNQ6GN9-TrhhrfLIzdQZE-se_yrKhijW9_BSO-eLQ1v6-I07KWlWH2IVzq0ieGFAFsSPvtEBzTwc6BOolT0Nm6kPZ9DBSupLT7YdzCrFMVZFbQRB44_BdQCZO0xxA69BvaDQx2ELUtCEyprEnNvfPbAvPnpMm31SDC4pAgimMhIRx8RUgIrXhmw7iz5YXLvl7bNI4hPrk1IcSG0nVdzVzf7kRD6xy0nrcEHqtwryWwqAo6Z7ZK7VUDYSxIhXOsZO5-GnTrJ8w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7801" target="_blank">📅 01:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7800">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5mD56US2IOrQEiFwEi7EmxEIsYm-kW0EkagWa_WuicyCBbpY5sor5pg_VNRNIJdc1tkqFS_FPunTYmxbH9yLQAe9O6CrXnvUBNHkE595w0Se-JMrCA_5QS94DN8EX56-zynEtemzIDGUSUxCvzUatmxx9CNJrB4NClMfhnG1Jr2kZuM30LSF_F5GpVVs3z_cgyVIYOsl7571kfZ_fmcZPj1x8gmToxHAq5T5hKsgI13EZvMLz9lwAXTovIYrlUxGH2KiIsTaukWVkowLZhQticK2yarlpjJymIrKTwU0PfcEpbPUAZtanjATyc8Wkpp4AT2IP47GCUKNMexaIJ-JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/ArchiveTell/7799" target="_blank">📅 23:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7798">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MO85W22o8A_ZERw3uDMdp1DzmDc2PXGdDOdA7c9orbap7IRW_Xqf2sx1r37AxuQlEimPJmMWPJ1zYbMNEracQW0iJe5QgJjfGfVzkQPNAB5ETB9wy4KMRzZZSQ5E0axrlo8HSN66_3OG6InFaWldN_2lJAUIRz3rMe-6M2dE3yS97lrOQGl3aSbR_Tta9rWZEOO6HIJr5OGXsuj04U92u0an4P8ocPz4w2uEqnfZbuNsriMGH69evapN20tbIYMEt-eRCam7z_z19vKF6LV0rF0FuCIfajn9ZWEWO48WTJatCIiOxbXsrDXcMDnFfIE-zSGQAE07TebPpqv9TIySkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که پروژه تمیز دارن و نیاز به دیده شدن دارن بیان دایرکت یا کاملا رایگان باشه یا فریمیوم با کمال میل بدون دریافت هزینه پروژه اشون رو میذاریم اگه کسی رو میشناسین که پروژه اش دنبال دیده شدنه، این پست رو فوروارد کنین براش
❤️‍🔥
✈️
@ArchiveTell | #SHOWCASE</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7798" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7796">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cg7pxAEO3NAqUbKQuDRQo0kcI2woQQCjSSXhIbCTubamwwBCiUs2qMJV6GazR0RGQ_PEpCrN6Q8RgNX7BUAlHOfWoAByTwpke-znpYRQogzn-JgY4vEoNSKmJXOIM4KfSS4I1fQv1HQ_hyfmUdNLFGmKyg1L5EznJ2_yv9PHW86mWusbcQSpex9Jj7jVw1pvW90OHXQi3cCSork250OiPrTuyN7XkTFFaV9qYNIx3_Bi3NbiPObxcLHbtrqMAnypEZwpMIBtmqzxgGtgFSdpO4zDbE-sMkUuVCCR-hzOTnFulJQg6tn6rfclKR4xfSbAKYToLtCHOvj2tNQs30fv0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtzMSDm-7aKt5blFhr2Hv-pmgL86_g35HhgbvmDffvEen0EjhlRTt0XRmr7aYRnqqksWOXLKnXTEkW1Pgn5hKytftkqhgwRSCmiS6PjxoWh8YCMQeqREvl3RPCi6z2HvfVG5fTtBnyUGAYQau1I42PTXpQFmX9--X73ZbcmD7P0NWEVtMy-J3-k1cW-7mvA_QgdqgO1qzwwqPxXeXGdojnAqw89uEcuhMBw3DJSEGv73Zbb4wMO7pbGOqEl3RpZjnJb51AQli_DIhq2xJaQHAy2OTUdYrqr4eMhoQLdjUYKkjeyqC9uwdRfZq0KwCS02XYv5RK578UFDuns6ctcDWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAATVDXrWhBvEv1qBqAivIGUCyVu36Tl6hI5uK-ZuFOh5xUVS0XBaQ_LoggAegJ6NCLaclH41AYRwrLzPDxyknlgMICRb0rBO0jj9txbsLVIHrGnAqXKHSqJuKAy2ri-scgbRp6lJPv9FbmDZyRQufaHyI7P54eKQACGvzxuBrXsbuHrx26i0C9k23S0JiDmOkNJbLf_BaS9nQaMsrA4wCeV-kckivJPQ811Y3HDmrTmd2v0t2x1k2iamAjx_Euu53W65QTh2bEDdd_SQlPxs8M8JIYFQs7hpRKyxRbD-xsq5wNF_weVyYgwLuc6TK3PioV30-9er_SfaLwTPRY_IA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7794" target="_blank">📅 15:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7793">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FfqWsUfobIUT8aOfW84W9sYwFzX6VlXEqdT95M4sJYXwCYdn2Y7ke3sA_Bq6gB5d5OYWgT_m5cQ19r49TechkaWIX1ydpGW0OqXIeTeD-v8A_bFMx7NJSJ7gxWA0qZcD9YujTqpx7C3Jhu-St0sGAWdalYwDWE1imoZHNuc8tF2f79dm1YcUCWEKtObcg8tRanXdyZZoha407wdrW-bjRCDwNqucRLX5cuIpieJGeSS7pGHSwX3lWsiYHwvIlcEtkZ4-Nu-DJMd2e5K4iJskhS9qVS0ricocNVe1_YOIw2GmHShlHt6ZHhjdr7GlUZ9jjBivgEPz64ga2dhpqaRxbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/ArchiveTell/7793" target="_blank">📅 15:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7792">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6341cb8e8e.mp4?token=mQoLjw858vTpQ6dNmuB8-0wwAtzyV-Qq831pWgX7kqKZP7vOVnAKml8BCEHxsk3JVXTEgxzSQ_GlEdWVMaosI7eN3038B9SLPdv1lrBUm15zC0lj0zuvph-Zao7US_tAAB9DJ8TtrNkK7VXQHeNX2fQznamPCiJD-AaBq9GXnchvrPq3O_-zaHcCpeRc6g_LNXQVE5Oh-PmFZkARZLw7S6y_QdR8GuuoMzre08VM18OSEYHdnOiLYzn-_E-bB3Y8X3C38haTmtGLtZjrF23WCvJV4HoZGGvyImlsOm-vi4zjyKqTVrqAWm8zVQGpJ17W1Ovoq8cITdaeZ0Mr2_9RVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6341cb8e8e.mp4?token=mQoLjw858vTpQ6dNmuB8-0wwAtzyV-Qq831pWgX7kqKZP7vOVnAKml8BCEHxsk3JVXTEgxzSQ_GlEdWVMaosI7eN3038B9SLPdv1lrBUm15zC0lj0zuvph-Zao7US_tAAB9DJ8TtrNkK7VXQHeNX2fQznamPCiJD-AaBq9GXnchvrPq3O_-zaHcCpeRc6g_LNXQVE5Oh-PmFZkARZLw7S6y_QdR8GuuoMzre08VM18OSEYHdnOiLYzn-_E-bB3Y8X3C38haTmtGLtZjrF23WCvJV4HoZGGvyImlsOm-vi4zjyKqTVrqAWm8zVQGpJ17W1Ovoq8cITdaeZ0Mr2_9RVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7792" target="_blank">📅 13:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7789">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/H28BsmWWH8GloYGyxwZLLopBp2B2PHjrIFZGq8gmN0fd23qOJ-Mu8T1uaIDyoCFjk7J6Kc9XQRCW7j2mKY2ZYeyXJtTjxo-0PQXn0_S-J44KWlOw1nxATty-oYNsO5tucdragN13jYkbPsH_i1BrwY0R0vYjcNlMtbu808SL9LC4kKmi25aQ5P2b-Sf3ov_60SuIJN7Paz8xp-q0kXdE1SaARJ9oShU0pIRXvhwaDr3QBe6w8XqSGqntMF9nFq0NOT0AB-YoHZt_OGaK7D0db4tlAJ_KBfq6C4miURNzLO0zp7aNDc9VbOU6Hu1BzqZJ4y09gSCD3mZmmjYqz-YEVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UhEeM9Hfc2X626BGxV8auuIEiYxBA-YIBum8SI-qA4cdZnrtiQXFZKebJVBZrCaikMGULElmNE6WbaZnzy-UeIKKVd6QoRNDicr-IGSM2sIAkQA9CNdc2MF2ZjZpHSpl7kcbmOxEztTtk5G1TghBduu4tzArC44vf2BTGk-Te37609IaDOqerO--siAhEzhEirpTa_YpULDVZUb4bktzoZkq-ybGFKejeBWujXxk5qwS9t1_rjzKjU1lVwGOoD6fW8w68QMEaJmXvOo4vozf603QGDHKh2gRZxP7L-KWwyh0t4PnZi3dfYhJce-rfr498CM8oiSqJbU8QbJ3zIOV9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiNKDk_MIqS7ClIf3zBrf25dYN-ixaPjUnJLTk5TmoUHxKwi0_twn8a7CttqHQMN9xJEuvu1RiYQbqnLarEPujchVilTEiXYxukh8cEYbPclQEjsNTIs-M_zUfUfpmMLPH3Ds3TQOTMMOsTyRr8UNxG5yJB7dy1I595Aj3Z9RTxB1HhBFB-c1TlzvQrJKBHuFoZte01dPHmErJli73SIkavx5Z8spjIuSYcI5T-wi_IwBpTLwZb278zkUM2bylDFVemTf5yk-2JTAq_uFWW9D9gQEDkOU-e4k3O1Z7fH0-aNEbgdyOS9N7w8-b3_I-lQRamro7HONkGLOOUPhDutXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7788" target="_blank">📅 11:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7787">
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/ArchiveTell/7787" target="_blank">📅 11:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7786">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♊️
جمینای گوگل سه شرکت واقعی را هک کرد !!!
جمینای در جریان تست امنیتی ماه مه ۲۰۲۶ به‌ صورت ناخواسته به اینترنت دسترسی پیدا می‌کند و شرکت خیالی مورد نظر خود را با شرکت‌های واقعی هم‌ نام اشتباه گرفته و با استفاده از اطلاعات ورود لو‌ رفته در سراسر اینترنت وارد سیستم‌ آن‌ها شده و نفوذ می‌کند،  پس از پی بردن به واقعی بودن شرکت‌ها، خود به خود عملیات نفوذ را متوقف می‌کند.
گوگل اعلام کرده هیچ آسیبی به این شرکت‌ها وارد نشده است
✅
منبع
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7786" target="_blank">📅 09:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7785">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
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

<div class="tg-post" id="msg-7782">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsxEF5ZEJkUymzGqhXM4whNN0G_djT2sPWNKeG6rwVGO93J9MW7Y7E3GZhuc0pjbuCTVQ8rS3pw5cSQK50ZXD8T-wkGv4xp57k_ywD22FnJUn3S5vKq7A_Ug4sKGOZyLIUKhL1VBrnT7TdWG4v5uXt5mILAE5akvf4yPP2P0y65PNKf5W_SkkHaV09F31iH_sh_FxVku_QrWble2n6ciLk-DDmN9ETN9qG6Prd0VN2HoVTbuSWsFgsEb1U3PcinqQfk4WomRjQVDYba__9PCGTzfWdoaTSwVN1Zh2YUzDr5F5JP4Xa5OaUfgIxvUqvEZnunAsUNPBlRKU3eGMRT67Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gemini 4 pro is out now
💪
😎
گوگل بالاخره پر قدرت به بازی برگشت
تست کنین نظرتونو تو کامنتا بگین
(این پست طنز میباشد)
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/ArchiveTell/7782" target="_blank">📅 20:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7781">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-1QQP37EtLx5CBrfVhf37fvg9jBOj_MJWLUmWoYhX6YcidfCYx6FyaZLbyy_yIHuw6nBc4jTMkqvOsvHt9aZzqOlncH4N9ZleOoX2lRFQx0ARS5m0xDlGU1h6ubh-0hFAK7-1uQKTRdeIkrh7RPT_DLf1mRkhXUVwuY7HGlpLdRQ3uXiOZJPBQgHiI2VxeaISavo1SGVLoQTpkp5KDsefoli4fPJOUYKbRy6Rtvzu2ucGtoCjMhtKJtcePdvTIi25SMVEqA3XgFTQZwCiRB09OIBdcDbOJrbs9Edpt_KhTmbt2ZSDdQHAykULh7hhw5qHWmE_deTNnaYUQTgTq61w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تبدیل ایجنت‌های هوش مصنوعی به کارشناس امنیت با ابزار Cloudflare!
بچه‌ها کلودفلر یه اسکیل امنیتی خفن
منتشر کرده که در واقع بیس اصلی سیستم کشف باگ و آسیب‌پذیری خودشونه و هوش مصنوعی رو به یه هکر کلاه‌سفید تبدیل می‌کنه.
✨
ویژگی‌های کلیدی:
🔺
ا
دیت ۶ مرحله‌ای:
ایجنت رو گام‌به‌گام از اسکن و تحلیل کد تا شناسایی عمیق آسیب‌پذیری‌ها جلو می‌بره.
🔺
گزارش‌دهی کامل:
در نهایت یه گزارش تحلیلی، تمیز و ساختاریافته از تمام باگ‌ها تحویلتون میده.
🔺
راه‌اندازی ساده:
کل ساختار در قالب یه پوشه از پرامپت‌ها و دستورالعمل‌هاست که راحت روی ایجنتتون سوار میشه.
💡
نکته/استفاده:
خوراک دولوپرها و تیم‌های DevSecOps که می‌خوان قبل از ریلیز، کدها رو با ایجنت‌های متنی ممیزی امنیتی کنن.
🔗
سورس پروژه در گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7781" target="_blank">📅 20:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7780">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">💎
دسترسی به مقالات و کتاب های
پولی خارجی به صورت کاملا غیر قانونی
https://libgen.im/
https://z-lib.id/
https://annas-archive.org/
https://sci-hub.se/
https://libgen.is/
دوتا اولی فوق العادن
😱
، علاوه بر مقاله، کتاب های پولی رو همشو داره. هر کتابی بخاین.
کاملا غیر قانونی
😂
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/ArchiveTell/7780" target="_blank">📅 18:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7779">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ارسالی
http://64.23.188.133/v1
gpt-6-astra          ←
⭐️
تأیید هویت شده
gpt-5.6-sol
gpt-5.6-terra        ← سریع (۵.۳s) و باکیفیت
gpt-5.6-luna
gpt-5.5
codex-auto-review
gpt-image-1.5
gpt-image-2
API key خالی
سریع بزنین تا تموم نشده
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/ArchiveTell/7779" target="_blank">📅 17:25 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
