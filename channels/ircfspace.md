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
<img src="https://cdn1.telesco.pe/file/CAr9q4bDteEc3lGlwULoMy37DqPqtruCR8IUZTg_E4DEKXmRtz_xPo_gItXEMuFkTE73m8RkImoNwlwzqHMDHiaJ1u4ehOwtx1qiDUwpKyEANJwwwNTP_VcsKH9nqtY_gpKMgSPVtwstP_-jqg34E4LPV82s_Sy2dBQ0xEeD7tq0gNjIIqlBp27Wn1vbeBUFd08VmSxMTbd8V3d27b_UzhyAdskEj96MSf3huDU3UDS0W-u0S92kb-mRR0iGyVsb8ewP6Ci-3MvwbGFyXW8JzxQxIs-nONj-ptoWqhlhsM-oWdGL3T53YRn3diVmuXy_J9y8wIlaZMr32rbwZ-6pXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.3K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 15:07:06</div>
<hr>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iPcwbYHYGalEzPSDJ70O0IvNwTca-EPugOfT3OjaKvzQMR7pcpiRCqFHO2PQEqd8tjKKWrbEu0m26lTxxOagLP76teKMP62u9G434sWSdP-Fa2J8HpA0o4yfi18BcBq3lhkfA1NTBztNON-EorhzZ1MY7RK9lQgR8R67ZwpFEw6qku3uj415JiXTsmru6ZfQ6axqwQx9FbHmGehSQOGvzaTEkTn9wOjqQawBELJlyHOsQ5y25TcUjNTK8-f-8F1tp3FWJp5USUhlM4jqFU3h1IN_HcncSww8vuJbpp-sd30mDBmEalpNSSughcvoy__wrGL_q9NO6w3UoEelMMV3aQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rgnwQr6xebL3pjkJN-Wfcw2X1OMYJ-RwiiYxY0dfmB4feRUvzM1D9LP5mlkciH5qiDbtXLGhfiQf6_PfLWw_sPOrwPrmthre-_P1Wn2OQrfrKeFfFOGAe77f5tILsD0fIWQ3qp5AKLhfPB6TJAWP84VNcwQzQ8qmG0TOEIrCCl10CsqsLKRC5pPoUgu2gzjVtBou2KBxXFSES7GG0Xg-hohcLWlG4FjJlQlATnv4Hy7SULq7LuVtePd3EW3cvbsnZ63ySPmgj8pN3Xa7SqHZjdmhUZ0BiXRtL1AkwkzUbWdyRKi4UGgNt2j9UsWHpIeKDbzeMBvJZjg-FamcPcmp5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kp-TbTcAXZRIE037E-HmzsJPJlQnhExbE-5nsJv2dvTN0LBTt0KfeWmZtwBpNm8Hp6jsOhr6zqaTpthc-fFm-f3_Ru_tr7UUhNa7kpIoOmDtZLthjgyat_ZmKUVlZeUSQs_Gs9aDNGTZfJJNnkJlfAihBZZDN0M7aL-zdJxVDUg6xAKV6zFFFQHcFMYR0dK2mpLdwzPsmLzf70nk0LlhRqvGQlM35fqw1ZHFR7JNdXtW337oiFl4h5YLyQuDZtJJsfYEs7X57JDfzg-_Y5FrOumTT_TWgvFyvDE09JYq7aOWF-IOatenquCt8_4eaYjWEtUiPogcF_UmG61b-saAGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sinUO5gFZkoJEPUteJZyO4dssrGqLdGVyFVGu40_qxytAjIijswgNxUOxCfOizysC2KstAtyxs3YfOL9gC2ZphDYCsxUWyOnpb_hZuBeyK2UTnhq0BbGLBQrGRmCVkF6iZNE6MhV6DWOv9tmJI3JcEsW8KqSDvbCZzGnk8KYFxc-OgqP9MPIxVi7ixpt3ntdRHK7BuyxPiXjLb9_0nN66XysMm7cV2KzDHrqstgXyLFFt-5G_0RIOYMYICQaMYXvyD3O2gFwSejKukx1xio2y1Bt-uMq9RqMd2svKRcnsrhgaq0M1J2FgDAnOdf25MrlZz8S1btXkerKCBH8TZPdRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y2e86ng279HzqCpCzIQ-gGjUyijg9f2T8OROMC3vxGiuBOq9xlwWIVtHLOrjT7K5XhnHLLVuVaRdDQIR93-2SSECt8WE_iIDMQpWtsRmIjypffK9f5LtlO3AazitRmf4V6gQ6WXH949CVKiJkY0Yl6F4Wm6u85zJhPx_cD8irpzqznCzVmYQZyzpfvUCDpuZKHa4KwfKuiUOdtcFMrS-ackUd7TDKgFyeT7CvmU0d7PZofZJspszLCIjaLClQmTIetlpYXoPMILoOmM4MPy2noNdrKQGNjjyJsxHVcZuJ_BMiuMeF49ZFHcJrI8dS_QyJ0h2iY_VHE1Pat0QzgxOcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OupY1mlOcp5BBZY2tZLH3a2jI1XDsxfs_d9g8KudKvYv96UbrsRcfUuRlxLvvDXXxgVe6LEpJkM6IITIANHtLcvRug725mX-sxlZ4qRtekJeDGCIKXZ4dVDt6ljPZ61dOYI5-7yl47HX2KC49HATLODn-eScP6r8PykS49PZcLQRoePMYwIZKLjxUAyxKzbbjNWUHNQmkn3z-6sqHbi4K4dLLpmURFRpyAn11Sa2c7oqf-DU0gn30mBeYdUy1wzuBJ-I5DhvRH5HcT8yFhQDpdmVeFrZy_KBmEDt_9ENjMJEEgeRlxhPsFITe402OQby1M1JbKr-aK80_TwEKY2kFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CXaqw5tjwRQFb4RzqFekh80A3xXCPMiv5LPy_rUYV-e4g3XYOZjU330nFrQ2NgHqImMgv-k4bnBsFFd9Sw_lRlFNPgs5EZVBBX5-paOQyvTdXc8fdByLLTnommq5qM_XH0QcpoWJqdtX4ip8AbjyqQYyeGV16CeMwSLy17_z9z1Q7nDm5zk1_1EZYSk1PI84qIMr0xSS7wAfTpl-hahotiT4GSD8APF5tjztpcDjU_VG7uDxTUrWPBecLMqSppQB6e0bQ2vHDK70-SyUuLGTeKpd1UgD2bMw_fUg2jVjYnsvkR25Ds8kjAV16TsmCil09n6fOMDORpp_PSzGlS42zA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e9PdFAIYF2YQIQX1rn7eqiabH-QEMVSnZZVEYjeoQ3LQYQHfw3eG0ulHiRWP1VvVRe4JO3wACamEXX7uwJ9hQUca291O3q513IJ-Sduabo3gALRGcoGJKz4mu313SOvVUQkJGb-nlIuEjBs4wJ9p4-juwY6vH2bFyvFi9nSjdznMqXtzvBPd9q432n9c0My6RMF2knuBwoB3oIRhFs32JsXM0QoU3EWG8hnjifsl37S9VlToaFsAqtgDt1oL4yGAhBOag55Vc3gCImje1cPvt1PRJtYZRZ0AjN_hlwszPvml4ciafDgTCiwu6ec8QXdaRcMmWgNQP6dFuf7mIPbuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p7BAX23G9xKPYibldoAw0PoPsSuatd6cKsPm9GCt6uxAqEKXqlZvKOI5SS5YCCmkvVC_CLkRRzPuG8ti0G6N7Xp8DAxQBEHP2YgUUO3V7IcTeve_1C3tmsQqfuPnNhLyA9JY5N5j15I8eQfDo0F5XYV7W5hKXag8qdL7nPYyXP0GzWLbdxAGn6cQEkqaFOwKrrE2Wp8EMAZtPkQbJiw3ISJS4a07dvjQcT8hbI83aps_E7D658gVyq1Sx4Xf1UHlENNw7ZiASSfS-_aP2-rM_OrZUTlYHBVyWMEkPOJUuTKGhV0kv7N5rTRdTE4Yn1yxPjnfoC-SegvmA91b6B7h8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AnnYamGUZY6oqdGrDjOELHZVPeuhzEnndwisrl40gJwk3rxW0nxmjyLMKEbC22ejaIDX1Rpm96zrKjmeJlKPhn7Hafy6d_ZlCMUETkCZ7xqiTKKn9eXzkdyBY9ROIG5lVgsvwIbz2dhTZzcHutdBfmpeVMBgl5ExJHA_tp369Src-rz1SkrPS8RwZmZ3tx-TkegpWqDocoq-71IykSG_tsBGBtx9h_EHwwDRLAtMFWr3lP9LUdu6p4J7kF83MmRlfTg3oYH6_3pJZsx3qPMviicZ_Z8pFvU54JppKHX824PTtUaihZhcWLbEBlieOxRpkeMk0xFmIf3OA1O5f4Culw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oGh-Crhez6OwBlPWJt7Pzr9K-DkU3iLmtn2dWI93g2GfsruOtzdHkP8lw4MHYHIitZbJ-yewMgHWzqV7xB-flJa8UZWt75AGkjJCtnmzSZm2wWF4pwsM8GNblF0ph7BG8G04Ujw0jenD4EKKUECLxzakJKc8QYxtfbjULhRAHGP_JjLoH0MKqlIcxKZ4Rr3QHkv0ug3On_IoI6xtb2TftocfOchPyw-6860l-1QIYUVL6Mdom_42XaZMGUZ6MeV7TcIaaToEcKwag1wP-Y2OehMo8-IcbHYDLIK6uBuhrvybR62jLu2FBDgYcemYfncqDXcvuRIP4QRmHift6Ki6Cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dtC9Od-JIuh5h12oJkh6Ovqnbz0iWeAIZxin4rD6Q4RIJyF9uHpHzyOt5ogDkvaUYSFqN3l9cpjFn9VtbtlumJpuWjTO_kyP8O2fpEryhL2TPmYTwcWByUTRv8yZB8zWv7g0VdCq6fx63vYh0nSE85KWW3wpDA4wt5wZ_r9su_an_h213t1nvQwgp06Y3V59Ue1-2UNz5zG4imRa9lNq8DVlBN7UGjGKfqjD5Z_BPqYRlS6pqSn_7iedx0eA8Cy2eO6m2CmxilIPXyZB6xb-vD7F34Mnz3QeWZzgXBIiaI2Cf7FORSEXOWSDWxl4Nn_irGvbe80ev70if8dBK00peg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hNwYGUhIWT0RFtu2BvUgIJfdtxBZyT6ms_yPFr6sd2faq2R3fzkTyMdetAJUP2Y92OQ7Laxh6zg9p5hcR2Y4VF96cniaWXK3GwHvSVIplF1dOGg0BPJps_LyRuaTumBLpXZuJPtkDGTcxm3qWdE61NlaGshE7eUToD51t_r8gGtNQWK9DDypEdID8LXMTN_WtA9-oJJqiYznXv3hYWiZwN_HkIdlGukLn5E7APJ8MmHRY_kN-v786Ngk8j-40s6aRQCANPDcEoDBchcbGcdzsuJKhDZ021Pbk76w4Ny0lPrCr9NAZ_aUI7Y4EarptsW7SPcRBKFxBIRcYZJmB4REFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bgFFqACnAG47NprMtMsEAacp9csjYUJA2tmPwWDxSZ5aKHlw16GPi8oVc6yjEAdlAMQ6KJBAxSKTZ28z-u8BPRUVqvXhsPFNrIfWYAmsb4khuhgzkP6N3S6aIKEBKeyihytIuog8ZEr82uZNZIqslLoTkapr99hq9SklbSMhGwC-FTEnJedFns72LfwmrgA1XCMbc9-Hmobo_zWCvR2eFOl3pYBTpCW9mbGqruUQXZ-VHnE7bM76tW2M5x9if9C87EpnwGCGvmJtvwvRMQD3yLyx7HnEEc26sEPZhHfeCz_hndK7rmqTQ_nbgsOLWevg1xc7c1NRDSO_37kmtDlq8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gQqHvXDRbuJ22Rp8xEWfA40ojRYJdY2J0rKK3v8yrMg5m10K8f9m4Hm3Nh7ASs8MzDShNaCWnuC5AbqR-71KPpEraJtXsL770HGcwYi47rRAYAa910Bhc_Kuv65PEByRvNcJCuYMxv3CGTGtz0Ty2VLqvm3YBS3vUv1-yUH5sS8uNhQxN2-2SuwLdHFyJ0g57kJHtlJqYQNp-WG_CYOzVrdFkN19xuGXoN5650bx3KYXvXtc96hFQHXDGKuEjSDibuiCq1odK7hU5lb-vFMZiN5TfwDydh9B2sl9fGLyzt6sT35HwX5E_YgNasoXcT7k7tI1uosJy6p0MZrm-R-eSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vOxWxddNuRfgRXwwvrnVGEbdX3sjMKBXiZN4OA9lYNjGryG8BPwXzqZ90EbcE9ns8Ju4wLn9wOkdbOZk7zSDDsYWa2S6fy77Dtrfii6-KZ_69oRDFt6Cwwf9xu8Se5jiWdohOez6tagRM2F9lI8IjVykgKoZyFRCvDtX-0trqzrme-VbTCc5BvlpCaW8b72FpicquxZ77NdRAuQDiCwcVZ1LdWu1Mf08Y20V2BglvtkxN0rgBU7v17bbYyY8zxljF1_v4bQnCb5jWKukZGCC1gwWyynQMbkPE8Z8PevhEGQQeBcOzct1og-EZ0yNeQK6u-G3fqszgY4Np6bxY0ZmeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vSSdGl3_iRh_PSFUjh6P94jBS9K8MDIeqVd9t0LNQX3Pxi2UtPZh8fVUJx8Q2SX2HGI9o9ZzhHK52O0soDPXsLTRNlTmChjH1AOq6e3GL4tQa2nEvIJFXSkYrnwhY7ooWH82XicLAMRAFfQt8X6lV2B9JRbqyJtQqHRNCBF9kegam2NOVrRIcz_uD_xSv3uzIExQI34R8C0g2OaAobnOnfcL3n9Z0egfKDrpvpCq5Nvsa2Wx4K6XCLa_5ABsMvRCUQUKM0Vy5bhFmNvcP_y95KF6fuQGq-bqm2Xy6k7CiI992nbpWU7vO9UZFYMZPsOhYqN6ySplJylXUhhI1Cg7HQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bjmmgR7khqWmz1oR2A9B2yUd4ttozKtzC-TkV4kOVFb1YJNMnojzfkVb72pYFF9r3BhhW2ktBZI7e8eA77uZ-5xg0XzfoPn7ESbM3EW8P6QJ3D_3REYN1x4FFbhmscP1dKDBiJcihkPm1WvjQYMEaSyrU69aWMjwAh9GvPqr03_NUw2lzHjgI42KuYK1Tel1mil65L2mv_SK384kepWug365mUEUMct0nO2V0Fl7WAv9_17LVAKadi1xU9HVSVZHlnfmyV0wadZX87YP4yoKbUkDQRwfY6dGZGvInvPYpw6Mn4SI1yT9fwa1B6_WDXXztLlkVmQIFnE3xNoWeO1Ndw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rU_78LGTm0ai-4iMsOngilrDcWG8OzFVReWP6jCJBow-8fcAGTX2Fvr7mmAvdTP1eQVmEQvr3OZdCzqaiJ_nlUJsb8oeRzHUdLuU4az7RanNYBDjTF07_HAgggYt_E8FWl3j33paIPkcyrboCj9fVJsoKe1pX368fILG3KBaLG_j7F1lhSndgpG1-oG2jMZy9CQ6VEGtMnFzTECmQ8bshah40ToUu6PUeBEMRcrU4FGYY-NhkXagui51bmPWH44Qckn4kCNA47pZrTf9Bb7KDhJtOSUJRDLezV8DxwliLM3Zr_SNfCZHlqqI27FioFuTpYyLDYK9D_uzEd4kT6OixA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oZKxue9qSCO5IUfKWVSUgwdDepJOuIerkxxFOGEH994fLj7KCuOxlyKsBjtO_bh48U-kSgoeh59zeUjamTPK1mwXPrykBRWFOYV0mhFeY_siWa06r4K4Ii0vkkQJhbRDppfrCIkW-qFdPyzmKMK7tlyfaFattk0EerkJn9OhqPF8QWWP816uBu6E4KrdT-U3Amxfp7fy0Y02QvgiB9HnOnBFKkJgQAR6w2_FKvuaX8q5_l8FbZ6eL8BKH2Wwxul-idRunqDWqm0Oi6FcSSs2nBcrjggeBvuytDOlNk3YwvOE2W_4OyF91GLGLixjStmMs2hhzLkQNjY_BnGs0GD17Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V3bEyxlurEAwRhLaX_D8WuZQXuIbkXaGZhPdiewJfgIVAII12uSc0DspGCORbbhQ3UwJ3JlUBman5awRV_IasLFSk1lVbRnaWooSY-g0Zzctdvt9DdtpyhUMgtjGlrxCaSNMfhAmnLHwEWc0LSZir0x4cjPIVt50jvWNP0SEuOR5CcA4PVatriv71Cd7HiUJpcpJi0MtrXWYpGqt7S3-nVqrkUZglIlMYS6AvoC6rLAAO-K1FYyOx78P5OFOFj2vcpsZoXuCiQBmvis7ZJebN3sqQbRDZAOKJUDnuFzQe2XweFcjNBTaya3KiMeUS7Vt_PdImvjRSmFXTO8spLOQbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tHhTHqeQMAY7DeSIxNbGi2Xcs9biBCC4Ag53zABnefHoKEBtO673k4aw3aWoEDxIsrQzqusrbDZTu6NzXMn3N3usThahQeK3WZcQ65k9adUSuON6tmMFiosnpbXfHjOkul_duaPcxsVmgNulEFKeiPzZf0d6wg4dUl-ljt_JbGKaJUbeWc39-tHFhtkAYCULoQzYakA-RnpoZ0xbXy-Z9Nn0sMSGf95_cjbs5Vijrlfl9IVYiGmnMDPjwGCdJUkHaAkPaKL83GIqoFFhFOVudcN6lOC5iMk00TjRQ23gb6wPbaXKPkU2drG-MBoJt_PRqkxo_E-QIaw2NFSS3R4D5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NFhfcwzYZnsJ_EQsQovjOlcEpAa-YxIky45eYmHNkBcpC8HuVN4dbcfR8W_dRuB1V0J6lUwMsAkV5y3cVYp6pbJeDZOUUi2tYmhHJY-G80WOET1NrEd1jpeLpQIZbzUiAUzv3DZbBxgHHbkkMST9M3L2zycQrrYjbAN_b9Rh95u1Z46vd81j5ntTofyqNyxy5QZGmy0k4yNuJKaRQd_s3HPuB9qkm39WeCeyo9KOMsWtx9Cpa4u17eVh3Vrty5FoFtXCoACzAJMQmZDcca2zhE8PAvaCVDEnnlAU5qRLnkBvSIDXNrahrYcXuneYiccdQl6UWUExtUtgrgtYI3-zbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KDcvKx74qxkAAREaZQVMK1wWx6HBrwX1EQfB7X_Vo0ZCCHRgxni_06Rxx6e3wInstaZo655VduUDmaWMs5YPLs1IYqwuyF6otdZuEoeFkqKoU3U_ItVgchRV2s8UY4HmYAsacHasqdL8CHbm7X78Rne52eUkP0Gc3Y1TTaSeu08UhiU42FLvwAcR490oTI_MsrhLp2zfAErUXs-8QoQbUFlhx0ZaCD-bj65USFeIE5cksUUzahQOiPaqlbeavVBJEgueLK1T90tIxP5htKXPyYA7-O1wZq64aBVMitEG3G3ILZUaQXFrOyEAjmV7yVTQdn_5i_k7p5o3fCgtrDVPSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c_uZibDrn21zYZcVjVCjssbxf1ZhoezzUxZ7RqRf0PZ2OEeI9CxMYQyN0BMSpY5zeCcs7fI5_tIahidW0e42j2Zi7U9A3eFB2UffjpQ6kPdEXyZHQMBvt0U2GgOUme1M1fVGuO8Bb2bAsbhsxJ0sGVMgp6zBab6GkjKneoVHFob97KuJ1REYLl_8TDEOQM-Nq-nWhwvvKncunhiWNu6oHmOUZkMzOtubOzI4jZTPMmqWgVFEXZG_xvsy0Fusp2ZED-BNGlU-fK66Elb9V3bMAm8CiS96K_fg46mKSMh0CU79Lb11-KuByePKkJvcJlXH4n3K7KGSgJantbpUiUaNow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ivN4tUVQ0zCQDSkriqYoqKmYj-O8WDSYLGV2_3vjEu7gXtSbQ74E3Ya0kBwsuFtcuowFTk6Y_n4qB3k92flavRk9q3VxGsp10rIY2JNBfaHw0xjtDa35wCwiT0Ckd8batvieDjwsEd5o2vvY1z6HarG7_wcYAFs8fIw9biDDpx1XLdqKzyX9BC2W8ziTK_CD-mcMOzkkz41LdzZcCGaUwsTkU1qaDB85bmTbEm3GsWn5BDgFRSX8EmcawbIc9TUo2_biPOG4azAGBZLqoHSNPTCD39gTZnTciNUc22ef5TBaCPQq26Knk13iAALCx5gyAg3niTFlqLE76jTusnSe6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RjPJr-vQQwLrac4_I6fRnEjKb55bWm1Ax5gxncBR0nGQ5oMnR-tThhRuWIvXB7Qe1LXl_0GxXcrpqHW984rwnMCrZ2Lq4ixUxne9YuXs8r_Pwqg-C9DrITi3KInpT7AOW8qUvAcyCPXoqOBvVm2IJsJgaGx5HRI2NvqMpBxFqz_44tXCkMBoC14aV5qihukHavQ1vfgavGoh5IL7xNjEaqWwYpP0mfyoZlQMSxrQO0pDsEnuGni1ewZKS84Wwief2JfOEaHiBfbqxHk9gffeA4k4Az0cYR7tkkC1vur9pzMbfAmYBCemKGk3GlCJuIcl9a-k26lbsbUmCfpPy7WltQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nzgHc2wPKa-1IqbSwgP6RJ9p1ChdUr3INAMAiLs5jmlQH1hj-B1LYpKIYllDVCw_TXwubToYduc3AyiUjU33Fi6ASIHMvhQu2rZR--LLUVa0v5j4T_3yZvorfYxWdva9ji-P_KM_dEaTK8yjW46j22UGqj1BVC-iJpe2rEscA5uzgu3MfGFs_eErQDMalYnywcX5iufHhZKr3MaZnlKxoHP12wJA2MZhAeoccozL_lQm14icYGRzKzhE7S8ATVKXBG2RPAUMgqqaCU5Igar7ozsZrl4Esjq1HGr7JRHVBx_ACugB4XD4P_bCgHPo6Um3XKeISvoXJeZHiiz16uAsVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mqBA1KsDI3KW08va2qlI2Nxz4AU52B7GRbrE3eUL96q8cRo7caP1LopjatCOIHx-bLZaYkiq3BUhaf7iVqEFeWqCswvYhz-4lOuMPL78VJzQLO3EueAdxWWA_nttO2sUn-ETtDoPFpJmeXR0t4ZIm9fIlzYR2gprZIIdu5WQPvwdoK7Z7ImsEelBnY2W8UPfsMoqwDVimIZl6oykqUsyFBwWKg9T3Nrq9qamR4i_yWfR0v1JdHVGgdLmoJb8Cm3fz2Uj5bNw8QPTYSAkKDT8rRLS_9ShhbwF8QoL4QNeA8jTLteH3aotwjSSfYJWZ3M1aheHiTKGrFYem7V6dS2GPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QngR7CVbFj7_UPWx2AN3xkFa9Ib_WfCndayo9c54vgZ_fCE6juXXhqIWSAvxrqLXxKPPK1hsJBQ-FT7qT9LF5aTvbkx3FbhUc_3r7oCSCGYUKZQQlLORjHlZMGw16AL9ZKOMvSCExg7uSKWAvueMmz_AnnMAV5jeXArRYg4Yo_zKzFoOsARO37mttCrxuzD_L37gy0vMOTF4wSPoVVzttI4aMTolDGdcBadJWhHMYCKPzA8x2n8MimZ3BF-1f51XQs8Jy5j5IOyGmb3UFuViS9aEo7-ecA-LI9b9slN4_6MjTf2kEdsa3iKlKGdhMWc-hHVeHp3QScJz28SW4hLN5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mya0geGy5n-HPczgV25vVy_HkD0iXDY6r7PRofpyj9eM8jj2suOwMGXT6nDRabRfh-xCtjKaWsSleBy3Sra-ZlVL0dYL-y9Kq7Rym1XjLNkilsYW2DY9j4PaTaJp-1Yaw_-OeqphAR-oZYe0QFr-KHPBknxTkXBOCVohh29cF7QozPdbPWyZAwigyzG9wAcDXoD_aLDZ5n29LwpVAlP0gywncJAOjAJ5SfIS9in2eZTQDsxqdkvr6HJUa8E6GpcixrnG1FyeczrQPftVuV0rpjO0gsG7Wr_yT7bjU-Kt9kSCWfQTrUMKg4NhpqODbtU6JRebntpmGnmuqGIyPLILBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U2IZn4nyssesXzHvRNEPZHF6TB59pPJwTbs135mH6lTjibUMcJJUXUwC8yYpU72wYKsr8Q99pRWPgQkOCf0kCoG20p5zi60Dqnh_fhAkbhJ5xibtF773apMG2MrKwMUy7J_ka9L8lpAfopfp_-sWKwR9_Ti1-GZpCsoFbaj8VaNz0_G89k_scuTcPygaQlsWJxnvdQICq59ZFgDUKJe9JCkUlSV9D2TzTHVNRl1SKyBs4XD7YcsTAe3SIaKJ6V4IF9A53J-J2QTnv7BsAAN7GwRW-MYwmGMprGs4ns4DfonrOKx_yx8t1MBzm-blLvgo2rYSxGUMl4CanGygFjWvxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d2o9GG14y7hSOpPBoRKismkYS8vjVjhyDBY6MMu-voDDiP_qaTXgv35FzT5iKIyGnf6grY_LtFYOwJsGvE1o62cy4jwOZH4e_jh6rS1F6OCDTbVgac-opqOq-Cp0TrWCCVFXe67wRunXgojNXUK2eXrvnNLpt6TCCg1s4oTv3M4bRTnOW005XpiW4sEPIvAQUAFnqPnQqpaiwrXqRg5MnAmWHItaJAATXP9CQZpCgvsncCjmxwAR8IS1FbYKv1772KBM2kJS6P00QMk-Lzz9SHzi_wMcq_gqXkALk59HlOArczSF47DMEZ8RdweN9pthi-QTOseZPT1nKaJtyunX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jsOWNszp0CTeTQKDzRBHSrzL74F1FmRgk8Dw5guNapSN5GdbQEVCCJVCME8svC2ouPNdseQe0K3TT0CThrrhZbHf0Q7d4j5jchILbPiIsj4leWnl0_u0WWlL_y5gtUh7rFGF2ZIcG2GkSBbAh-29R0ek8HJCXrKzzwADFjQHKAJR4363gdNOAoA2wTpPA4EoF7lPz-1HtIMRgWsolnnpNRaG-YOjolVYQgmeL3KpRlAg0jOg1mWpzqCOYJcrt2PoWMVE3N9-ioKKsVAEYLXTJe7Fty8_NKx2D5UoLqc7K-lIcq2aZA04hreRaaa_ldcQty2uS1VEYX00RIF9_FGSPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K0RULB_WvbeGaEkZkassFn7DwhV128g9582eyCGdFQI_TKJd5DdXy4f56BwxyUEq3r5OezpweiiXwVebGi3XJtim48vLLG6n5d47yxwG1TirnFxCDDOqXYoa6vJFpXj7AnfYHg4uaiNYmG21wKwYhexdFowlQJjX3oMnp3usC_VtZmgNKXE2O65Ch4Ug-O2OqQ2D-lpcxv5Hr4heIdpCKjk5GyFFNsFOp9XBCVtoRxSHl650n-Pie3NJTgk8o9pYC5zKz1aZI6stc2j0FJzsdLmjAur_8d1KMlb-xWLrg-H-w8r2jHCSs1Ycw1gTP4voxi_724FojY90CG8MwVWx5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=NRPu1y-IHalHjkPdQsR-FrAxbiXUNv7f_LnbsEBBmIRRzm7BuCfZOHSESHADoBOwnNI5PGV9CsRd2gW5awL8AhhIvz9k0vK3mbrQNNUjpl-jtaXnR7JH7pdRpzTZ08KWQsrPXbVVVTv6pTc5bipVKuiZN0BZ2bLQytEWNZv_M_xYMlKcn_ebiKgwCh2ttuUttdn6bqJrapXb8STEyrR4JhUyiMpzEU3_BHyJQ2pMqn-swJZEvIPTHmX4fnWLn0HAopLyx8BbXFNja6qJljxKyiXHi6gZsqQxgGxmqM-XzWoC6R09BUmEUqECKueFQOQTSDdPbUAMBHwsdd1dbM-3sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=NRPu1y-IHalHjkPdQsR-FrAxbiXUNv7f_LnbsEBBmIRRzm7BuCfZOHSESHADoBOwnNI5PGV9CsRd2gW5awL8AhhIvz9k0vK3mbrQNNUjpl-jtaXnR7JH7pdRpzTZ08KWQsrPXbVVVTv6pTc5bipVKuiZN0BZ2bLQytEWNZv_M_xYMlKcn_ebiKgwCh2ttuUttdn6bqJrapXb8STEyrR4JhUyiMpzEU3_BHyJQ2pMqn-swJZEvIPTHmX4fnWLn0HAopLyx8BbXFNja6qJljxKyiXHi6gZsqQxgGxmqM-XzWoC6R09BUmEUqECKueFQOQTSDdPbUAMBHwsdd1dbM-3sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YZ9WpYW7a0RDPI9eAd5y0887IdjQaTTQajct1jR304Q2PjcUC8Yrx7_z3qWY8UESyda0gablB7RKN6fM9d8L-Sjk_CF2YM8f5B-yqzPAiksSakKYNB4o-ryKMFIvnkNWMWVKiHCk1IHRlVsJmJ6GmU6tn4_3Z-jvA__Trhdcr7M8dRWHt0_3bc-WC0HCNBmyOkVfuf_jg00sdHonA4ajBMzAEX9JhoyJnul5911wV8v4kmwwtuTpPxpJm4kxWNqAQNp6jcczkhQVstKjN1G2YBVOFXhjyDAwZw8VuEgp6OZNGOoCTgnIZ0nDwZQToRssUdCLDEUi2TJ9ODcURa5nkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tJ7l4HJ9MgheryNn8RtkZwORFjxfqE4O_hs3gLZ-iUomcmZ1gtJ9VLTtlA7uSzTqlEjvI-A9nvURJwx8yceNJFpRMPB8o9azgpULJjIpIxi3utC3CKZVOSZL1A34UXlwzsJD7YIetzxfZ1ELNt7vo7PFoEQ6APuyt2rPrsISVciE-Z2uie57VuBH8bRNVi7EvokdOPlk7v9T8OzZP0EF-osx1IZx1zRtw1DWQ1hqFxieQJYA2G6Za8iJbPpBf_EFlt6PWroylYYwGOKQGJnjtT5gIKFZ9q8FkamY36H38MQESo7RKRtEEY-5sz7LJaDnFdfU3slzJugRnSa2_2tRyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/etwepUEqv8_yDW-rZw2FDhOuYX6W8gAuyYRAOactz15AHaF0AFLCFKuZQCJBJv6_Tqj_Fl08w02d2qZ4Yt-UUejWWETvE5lcnSkoPYxHkk9XKLcnKUp0GZFk5WCqClRt-M32urYBCEwnUIoHPU3L1gpPpgnO1oJK7pUIWZbwID_9FO968P2D2lGfbObZkTr5JzcezaaqFOlvGrQTa0gNOX7KFOY9KeP-RDdN9gfyzwfSThozW_4QRzsT_T80s_YNxuwBmlbOlTaJlLdnrLnVinmLCWv-2JNYqtcUu03vgzCbBN1T1U4X9DcUh6XD9knneolVunLToLKT0AfbmgyVFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f9K8sx1YhmVmyEg9elqsgaGIbRzhRY6uFqAWYM0u5yQiYo_7pwTxcuIUk6z3s8K4P4jBqyOerb-YVn5oSDm7nZL0c8tjWADKf364xVmuoa5ImFhJ1wXp0Qhishycby42bR-AIz95hfCKWBV--Y8dwgO0nYNuk3uhLwCPb0UMnhQB4GtI7QrfOJY2iEzLdrE4-x3XJ9RJhDR8qKd5X_tj_6QAskdshtCNOl0af565CYrQnz9o31Yt7JlIiL6ZpwS1PUhjfd5uNW4-6xu-QfKPnm786uvOEDmQUG_sScI2tord4-s7u8T_91QmuuRG_Ka9l-qvltTZGOnCSEIcc4Qb1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WXoBuq9CEEmJFi74Sai0tGAvlTXJS55fIWzkXJarOD8EvyiASczKqZaA4Z3MNEvcfIlNxXVR5ihI009KKYTERq2eoFgW9Dc1GZQvLmXzBS7nIbJpeP4mEd-rEFfCHB_L9Q9Lg25K1y5TiX88_wRBxqZV_bgRU5iT_sr1HqGeVDoGh0AaqCNt-9ucctBplnZ1qrMh3auNukq0E8AmPXM5moWwWQpX0yo1rLSt3iumq92CEDq-kwfT8Rml_H5qphBfCYvq52o7YBmqMLP8PaamcVl8PWJ3UqgT2NNPFj-h-LXHgekPl4pma5TjwRPcYHkij01QgAESj1IkdvSuOdfnUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U0Neg0SspFBXeVICz_SNZ8DYNsuAYT2EeJbsXvKb3jWZEj02B5BKZ2ufIxPnXrzWbGrjQn-HuBtcjFs9oRy716mSyQmg4nTjnnRMkDe6JU1IfcM28X73YrYW4J_p-L-zPYJWGJp2obvbe78ct8hN5WxJEo7A_XyXzrWJ9NsOghHRYCajRt4m0UoSPnteuTdKBpr3tZJmbW-4ZDsnOIl8VE3R9v_MuVEFP7xf-Gc1mHBIjuENfc8ikC9IXsdfRbGXLz6SbAujzULIqMGB3GizUM_RD-EvtGZ5UXfDvQiOXIKvUenTFIuLshrIovm0C3spC8AbIn55q8gVDkM7MX2MdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GUxI1puQhdTPUl0-CEHspgfMgSO-iajrNaXApzqBDjHJbcZ9w52Y-IjHd8L3YCUUCYvJHGlst2EKSJ3fD1Zhq4qxDWBht8X7P2HanhrrrXRP-vNpJPtkF-E2-gQ4t6E0F_a_AY-2fyu6W7tGx1SdTsd-9j6HrbQZ__5iczdNqsfUk4mKy_JIS7dPyt3AJmJ8WeCaUZClxNGZ5ZrIn14uKFEkJFmtbalo-D6fAzNAHBHNjOtTBjhZtiO0h9w2t0Xlw0aG1PoSC-C21P9DREAZLI0-2CL7Vq3sk9BWgCREl2hqoLa8es1heoqMuSyBjIYzsAoDIqeh7h97T9nCuDszGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZJpcV9_ur7iBgrngD2fvNsqmSu1AQTvpae_f50MB8oWz43_yhD3m5jN-1DHBugX5hbFzvMYqgUx0UNBqmsGJ2DFil1qNEuYWg9W9jslOuZcseBFo4J8eDN7zOibE-iyHHJKn7sH9GmNRe4a0sfxMN4l_v_BAb1TC38dZYsazVXeK7czO5SS9836uhpBQfUwtyOAfXj-U5uMkSVvFblP0noI3hrL3G0V9DpVBK8unrc630hxzK8bDTdLPgRHxigcgq8P3q7V0B66XHSPXG7M6ujI9W1B-ki8pMCwDE9MA3mJOx9b6x8QTvekLa7hOHrhaQ2q4GbpRWKV5eSXMhYkLjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VBo6gEleopLvi_avrgqTlGoXHZ9EzxMUJLy-dt7MUdj4KSKRa2tYlNhZGAyAG2r6AHE8FDHWyYMF_81hVkGWWLQkR8T-vy3hiQI6eiGe38Na8ahDkfzs8m4NAywmd30McTdxh8MMrN36X796qngrBaKyjcuH-UZRIz3VZnyhnYEBBVRZdZti_smFOXt92VtwzFiMx8OZvk0XQZd-vmhG4Ii5zRKxmybPHVEHpnM-WyCVAkJn0zVXfjthX1tV2QyY6qwKmSzaD87XxS6YScz-dkHHKHLazXeCmg-cMKJWMCIfyHKExgVEp38LFcn5sqoAWUoOESayCDc97hR4Nsi85A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KL8wWxbh2t1t3z4tf_2nHFOAbHGzwiJZlJb47pgRuGZFkI0r5VPCaplcRepv5S3r6IE8E4suafN3TYZ-Fm3ToCWf7wCz0wBApY9LiV3sfg3D-ooT7Jdto5dvdPLZ8_tirjEdw7umWqhPouE_VQoGCZ2iFu7I3vYYe7aq8d8IxGeCIpB51bVhktr0HCeZD8zHheUhHab-iVgTu4g8V5BGaU6U6WeG3c4e6NeQMXgIEsw73ADLWzeQN1bMVyOND4LIpLcW5x5eUTdjJGqwhUXb17LZPShQdlawEObliQd2NCkV3_1AbWkWRb54y_3YougFHi1TkMM-ixHEcgmwVco0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IK-OkkjgXrAxGAuSXe0jaOq2-HR5vbVTwFLZhqZcQOWJ6O50rWjCl2nsTu73GX9rgynAh8y6ERt_j7RG5-wXyNNdnlfYQtSoonBSWrUv_umJawj2LOElIVeq7a8boL5_yzpiw8ZA7lwle_5Y4su-CGIp00dht3liuAUXDfqaYHZKlZGdGA2onR6MEtTVfAcTbQINuLLAeRUnyvHKHyJjUlpSb4iY2PtvSxjgJMqm_jJyP-PL0HGiEkJGsSvs_GJXYBF_ciBacVcLtuClIMzvYWd0XpsDekKAE1qg2lEdXqcbgVN_0MRnjyzLyKufJ3rP7iEUOCCWBUAP8sP2UccAGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J_qGZzVwGQX7QRWBzWiLbvwBvPZsBP153TR0ALDMudR-c9qDNrvY8ojFN-JTz2Ib-jtk3UZf94ws_PEscFWHFois_GSiE8SeD4UZAaHFz840eCD89grIbpgVyX6ZR0Pcjqc01-5JauNEZom7NivydbjckGkAg9Je1RKMOM2Mep1MECyJo-6q-lAb131APPgqDF0PQlKT8T7FD8x0g82NDjn_JGTGkzB3kRHtKp-LNRw-oAGGmy-RWwXqpLwahV7Dj__2bAzdswISbGDdpEsowc7q1JD0V65Ht9d1SGXDqGMtvzVCpeF3ARkabadOMVY2lUNAj7joDHR1TvQVgLMSow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MJB8OEmPCpgOTGUgYWREemb_zG6RcylcGeFlfnnqdhEKwK0m29jlwSUTpSBmAngf9nIlYsPzyG4TAA1pOvYcg7mNZA273LikpInO9FIfyTebIXiwmEfdeg3OsdNzK7x_yb1m4hoDiidFISggX5f7HB2jjME6XB2OlcFUB0wO1VuFFC8DuhYQbliOU_dqxiHsNC_71-yCKNmpCIcuF9IvVD-RQHpqva62vrgNXyHcI7bQs3EJ6r6L0WbRKVXEKp6BsUOSXHq41st8xaDWgdCDkCNaUzkJKgEuTICFo2AvxJ8JZNi7AE3J3vtNScPF0y2IkUWecsE7aBBVKr22625s-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vCWKVv2WB_HxFKKwRQ9LbXWFqOVnlbKY7ggUgwItDAeeaFR3qZE3Nlxu-F4iIrItkMrAvaCk2mx5eWmAKgrmlCJ70cV2-tM3wQvqMiYzoSWYlnOB4-x4z3foyDKa9_R9WHg8fWwzTVbnB4jqJSJICTDvqJrak2WvXnQdnjMYpyMIX3CoyvAKnnZ9humHaVnGZCW4W2E08xgogOxK873gc28EA3uzRg5L3lIhMRKW2r2jXUfflbbJP4PK-3CZruh7Ke43_u6TzVqn2HW-sW4A59HuXF_vaykOTnNXxgVx3vJJxjIVxPl8vAjgma660Q8Lmf7DseOitQC8GXvY3p5Gcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MC72X7eD96Un5tbD6qtPlwlqmmZQLdIKcVy3KyoFSk5N3uafnIkYFmcC3n6AkRS9WsatrEEahirJxFOtjDLKAHlIv09A4uDX6cmt9UQHzqixTOQyhADxnSVAt17nMWdP-bG8qkVyOB_OFZ_a34t-WHy28dzQoB1NGEyPAwYB7RcAW9XKYcSMXzTz-QxROV2C_ORWYFNzc9vOmAa0rOwEygNlZLolPwlw9FgD4boRB-58t736FWTAhprwRSAM0sO-Q7TL9PapwNJ-Sy7lS0_KfsjGZYgW3U5BmYD8u84mYkRbtLpjT1xqJ_iNirb4QZ4dx6adle4HYlljWCZJGC2IFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NyDNJ45PLs5Ue-fuUN-v15FSIZW2uAuZUdl89EDi-2bKeseTpvvg9JdPih4pzHuhAw_a0xyBovPICZEHTLvbKNg_mWQSpwOocI7oQmt7NlUhy8PDpsIAjAIhlUcIqMBrTDEebHBMEQRJEHmdVIVxTFEF16gRnwNmx0CVb42L3RPHbjBHRYAiEmcYKOh6SyujX0clhKg1nt-I5JyBddgmx0C-VaeGOqo-OXOE4Ch3ey1Ija-sCU78s32YqH79QrYuDeIxmXyjRTkNcvAfThhUFmV7uXKv5TgIm6rftKR13Tg_QYFWN8ClvH1gCE-ojTGx5CYiBziEg0J24DIPTW-UDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uoYVnRlbIFRvzfjsKsQdl6gsLelWqFx5LekbgMI_jQrlieBHNCUAJLF0bA6Ksrt1O0lteqieFjSB1xwsN3aKma-LGdwTFT2vp9UwaOkJByW6gw2GLcZXT0NFrSl3jQIchvGwKBEL_W_HbXoYofmont0M0YeZS4dlHyxiSrN-8cY_b-mhlgJorCZoSAbbsRSCoZ6Q2qp3SWfDJzJmqD3jP5R5_bWIlRgjt6V8LSYOAMGcQEJHM7P1b9lCgSr03olNUUVjVKzc6wGS0kbVwn9zz7iAGX1EyCZOd23Rjt0HmM52HLiLeKXhIVG0XcLDb27vMZjlI-SU5h3-sPXeOj2FTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gs_7mBSJlmjGqLAxtIQX-Yk8uqMdi2xaFb7z4hrhVh6cBjdV2nIAhC3OFBQ6LvuLjCSq3vE9k_OOhUOAN-E1u_ZtMsCgelCzQBQ4Teawvcm2mJa-qIs2NBx-PDhISeJlmuCs7T50pmX-uQirEPCqcm6dI0Wgd2_fvPdeL1Qsg9rXvkl_OxW-he42D-VHWGx8NEPwCgibZfOK_AKf7RJW271PGGoV_-94sb-nS6kI-lcUzbCSxJ6hx_dn2RJMnQrZi7OrziF5meKHkoUMEScsxP5uTG5VacfuS8x0aZYUuAhFl-ze7rDPiHQ6SJ3t4hqIAYQZ3jVYuYvwlAXWINBhAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bhmKL0Ly-V2-eriol6MoKSTFIue6FgzhzdufR1njcWBqRyhAuysI47txkbdmugvWL8uuEA1yg12BLBOoWduf5R9sJ_rsVnFmNdxVaeyWuXgvW0YnHLNnWxx0wju9WAXXJ0ao72p-iTxoNR6Q6hboyp2wdMJZyxG1gRL1feiSJynNQcSI9LpA--o6LA3HccK_2s2mDf_urMVgoShNzOW9mNZUtunF4vdbEw8Ognbo3604BtafRns77oD9ROr5EzLXpfb43gU2M1ZGgkrVECUMIA0NUWvr25FCpRCaGosaeCmsQ5ljIxccVnF1R0EPDljR1NTVUYb072PsgfJlMuQsrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EpiXZXvHHbJuvTTvY_3iSpGwdhlHjQJhulzRUcUf_Jn7AaEGKJNotmKRdX_t2CQU2uTSKcEaYAeKfyyb_AUN4PTzgkDS3eqEOYpfnhwPDeHomJHJNhCUVowpjUKqXLqjvbJPaQs9HNYtVCBcKiJkZpPnyUw8ZE6K62mQ6l4IKu0-Ctk_vEjThZvbav2nO7sY8OzbBAcIqcziuPLVOqGcHRjKqMlvJqvYV74IwGh4-cMI7ElgS2G8QgnIeYbY5-glpFzgM9rIOvYapbGUpyOnzwGDaGXBYX3d8FOHr1796O3DhNQ_XvxP7hKlhLhR_xLLgR55UwJJ3kuropZkWYYcEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tbTHyEQdNSDE_G_EKKlYmySlK8ntz9gAU3RulBBHmp352HM0lWtbd8i_H_7X-DtIWY9ydtyArlztSM0fsMb6xJVaS5yYY7UzBMKjwA2378tvyPjZEgLWQitOxv79gJli19DpzXueyUssi6O3g77HA_Q-JBqYc1nqPuoR1LcNqy2b9ZxvGFrZysWi0mB5Wpt3WK56Eos9BN5qikyFN2o2phoaMzJLKg90SqvsSJDbLsIcezUsiurcNkQ5FR328nGwztNT5ICIWhMY_LKLZ49598BgeqPxaTGnVB1FNVHIxP-4eRxxEfRKthV-C70Dfs5_ZKbPoFOEoGIRFzWwL2Zu4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PEDBtlCXPr9jCrRGHCm2XdvtIZ6bBeXYCAWzd77KM3froEdqxAU_mA7P9nK57sa_Xtgb8N-hRZhgQKIr9OlfGgDg9bp7Wb-tI2X6F6N4FegmeavnR8COlvFHuFsp_mKkdQ6T32DoefCZHuO-jIZN0PZW1Hjgrvp5jABtbmUhHOICeIvT9YA1DFTvawHLu08GW_df-RSCLLM7f98H3PRkgBK7dlkXXQA1I3GtUf2Fgn15s2lQ1oUVUyvNiEySlHByJXMr-7qrwJGp3NmeSHAcSpmrvTve8aSIzgC89tQRh3VJBbO1hJhB0PPp5LT7ifw8XbUBozmK-i2ETa9pq2xrrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jor6L1w1HJw2j_2PWOqy3I7fqj_1Yahju7-mBbX6tey_tzz-lq-NCD5UF4qiN927wLdpK7HeemnGIDXJ3GSGT7eztwgd8cPFKjaX7_qay2H-pMFF8wcL0Tt3nMYjxeKMs--uAC6wDHEpX4B0uboNFIdNcpFQiUe3TbxrZ1-oaemr17vXeDAtMOXN7EMphQCw4p3Aqp_oYAEN_IGKLzekGlxVguyxkPoV8mUzjFR8UP4NqlJ7Mp7OEMWBEYzdBwV2x3MzL_jkBHw8bZPvrQm1_tlJpXTe1I-jP7FPvM4mdki9tMv5WPnyHRToaW2GdCFOV3TprlkQN573SYKir4glVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ue0lxsKrkxzji48pFI1LA7WNbTUNkHbzTWone7hWPb9kRgmM8D9R8qdYyOWP282gyu_caYeZ27fbYdhSTIyezHmNuFJKh55d6MxloHNsEp7fCWdwfP-MlsR6aHPN-po4bi-SEh4-77sALcOmQzZntWBWFIuaQ86Rm7v1BIU38a5GmVEiwXSGC-S7Ny01BT7wyIHwgeHb8P8V5yH-VXSNnF9UcLgt46ByXJv7bqPtuG5sAEEgfL8S3xwgp8a11kHRHdAQio0PCILGTI0c2ylNm4VL-S4cQ7mCHNe45cE80_ec5lrXnrnQSy-SmAB0h073tvI1rUa9Ioa1GFB2E80JJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JN1RHJD_pehUMvkLBxnTULcjRphfeG6u-5wuljjS3CdUujF3ZGMLd7zswTAdHkf7q5IU-kkH3ELhXo1_ThgJuguECvu1qn3PlLczBLOZ57OT2OgpY2UGbQBumipPTn9Gyx526raZ46U46nMgtiK6XznWJz8cqfLuynUl9J74ohSydkDl0007kESouxtfy8Za9eNHtnubSxSpQsWDDDQPI3uCcQiZhNTYTrb8T0Mga6VKquOKuHzYDg3p1mHin-M61zRGjidLijmKVGsfe9neyxREo0jJVgn_bLitAXKrTCZfQ7SBT8vAKvSevPul_cbbTMZotGlY4-9hWu6h_0ydGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DPqj_EsS4m7N9FAvfzs0hvCpFaKre7GFaR08PoQpoOVBLveIG-WzD1Up6NZt5IskEAGBFWkPQ2-sbi9zYc5gfDL7NyfCpcAhQhpRuJjZS_R1SJ288Aby6_nJV4V4s4oL8xEgKebFJt0ayqm-bhZwqvL4Fb8qU5VYLVI8u5H1DoBDoflq2sbdCZUYnJZLfg_8ZBK6acBb9WIAPv8iC9vJ-m98RdaMi5c0UPTc_KdQ_vEDlr-mvH-dDzODjrHsEQOVVmTjNpOx61Mzn9PIXhhi5FgED7CWCN6rPMFCva4nq4raVF0QbkcS06bfkX5WgxO0Wq2cJT1ONlYnXnKb08mX_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KxrOyDDW0youuPNRIRjxBmUGwwynqd_pYx82QW2Ol1m65a5YkYdfHd5GmWtHyoD8G8WC1bOJPE3_F3U6XLTvJWRacOwboBVqNiWfzGHqQCyGvUuzflXaei8M5uLHj4G5Z4sVjHUXtlqLdGFxW7M5EJU_pRiOVvqn1hkh4bQcWs7-SVW0pBrmTdlhUYhiGXZEtQ5EK0nt6WBCLuyVnn3dwNG0HDrRRHm-sJEOsihj--ZjhH4FGiYNfgdejmnvightPSg3vBKSu0zmahXPeymrDZnUytoeINjDm5ew9Wrika-XN3iWiJ3VskbIc49UuTvTRg98d6rcVots2iO-70vPSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AtyIAlCu7Yq08SArQSswgs85H_e-9PnvMWg56dgEbTRH3djw7UNBT05T4LYzveeARzMF-vtXZApidJO6EQAQDcA314W-lbKwv7_bWZNyhoycT5b9ZTW1OUomP1HJOzON5D4zC3z3d3cCvZUPg9_puCM5VBRgj2xzGbEa9b1UqaVVyBug88cKIgrS6AYkEbZyhULSWSDA6u4H62DO8H4kkk_l920UjDHm3BWTlem46ieAbeL6og2p5UBfih9bdPzKxxFcP_J0KF1Z83M-iSofu6FXTef9LwGXcCIVj6vN9HNnCQw3HUlB2NukYdVju7fWAz03rHpCIoY26bEYqqw6rA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jdTJmiMElBzjMfJ5VGEZl_9GnR7gQdOWsyveqPs3lkjlg6vaBGDRAKuM6OhLjQAlc1Ad05qOAYUtsW4h1jUvDZpizOsZBbLxTzdYlVmU6JU8dDpUFxN5WjOTq_o3Eij4vc4wJEvmoK3apB4E4TCXMk_anyXnvxggKfh03lWoDoAB6gMm2DbuoV7S0w7QgdR70apADqtxEX9Nyo1_ufVid8xrWV_xUhQA3P4IjrO5jQTBd4S9E1A1CfmQHCH83G9Cy0Js2CmD4h_cW3bFZJHh7_E5hrnG-fF5UXM5qiyDGstQm4ydUqEqMB_CvCZ41xoASgXJBpaQvEFV7lvlYm-SkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S65tGNUZ-asuBMHsX-LBtyA6S8-Jpx7z9xVf9jfivmXd6Z0oFYEtvUGw4iH97IYbI8atH8eApNBFn9_GkvbPNea5pSNPgYsu6GykUMCpBZ_h7XC6Z2dato5YMxroazxj-eM8eVz2CbHt4htcSYbaCasXoGn44RxJyrOne1N_vnuYQliZRfLEPXs5dd2LOwBOazDvGrI58nDKewKGMqQNSdMAWS3-p1esh9TZTA3AvEXzOvCh0-4c_JgOwS-SiqTsOSr_huLBaOF-PyKrjfL9rP3M8mMz798ZQWpAzDnJMeBFVuTPpGuOdCw6Iade_1w8YxQ0M-MITVI9CSNYgcb2NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E7QVlIUGgP1hi3fwPc3dflrHvBzj55XYEwIY6Sy97PjtSXc0vx3jETeeiLBV_JbEYRg82ICxUR8doYx5D8qCAdNmuRsd08Ja46AQsVSvE36Wh_cUDpaepN8tlhdYqcLxR131iNc84mLxt6tu22AYyG2FeEDcfgOt8oXIDIq5TsAGp-X-TANJEjlUfVOZqGA7ig0bYXppBNXKproWc4BdlvkU1FuKeAJbSuBDZUyvP3sDwbcAGHrUKe5Lo8hvHPzvX7XneJ5qO5UPcBjzgp-quKUh3BUNtVMDIR8Pr_mxEGAMF_mUQuX5TZN07wYSKgxtAMsqfKL9b0Q2LuWy1F8U2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dohRHTk0pTDzvoUmw6s9bIWEnqcxuLdDy1jVMjgXXRRPl7joMzi2FX1D66lqEam9QHwN3L5Bj4l2pKY0XR73GQTlZAkD8in6lz4CSihwik2_4A_Q5lpIIJGbCTVVWvyQYfH_Hsm04SfnBYg6G-fg4Yfxe52a4BQPTWtTnewbK2SepuRrBq4Qvb-xLMtPlVXvQ7T8GeIKm0jVqt544c5r4kGdmdKVOYKOmOjgmuZL7jBpZkRzkpW_44osuxarKwKy9Sr41SZgdvQ_QqkR0GbBu-2YIM8RFiQ_Sr5ynOT6sqpAhzMd9NDRsZdoUlX_tMtD7zOzeDk56ETCqYQjm4H7tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gjY8QW16jVbpAPU-ztDdSTBcWRaTyT07DdAQzle7FZP5wXkUOk-wxegvgacGlJeTIMd-5ER9bbJmeG0aWvdZjHsujYJ-sJOVCHU9DnvWzWPsntrvRMQ7neug3HQzV1vzdurVjv0eMYc_P2NxH5eyzuvJIm37vJlU9hf1UNoc-AtWh8BbVtv9TprML77f1Q5P235Nn119bqh6L0D6hKThsONWuY8-iDuusM4S2F_2XdbsMBlIRrXrgF6DL4TZHwQeMojKlbsiVAd-a3Qhdb-sOh_HnCdVHnrimQTIxXpi_t7sBZxvvtPumVJNN9gkQoganh2fmwif4xlTEdXSBg2GTg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JTfLFOe8zxrEaOeqmIAl7N6pzeeBtNLcWVabJ5uZXZi6LH-oYw4K40Qrm6yDBkQxwsanp9KbpbyclYhtb_wbeQH6vXE68Sl2ASiUe35sW513Qmq18T4oVUUrpaONcfW8r6---HvYvZYPvxJIT_4ddJB9j_0sRMp2KhxdEJiLCkMS5ImZFx473REsgCWagMTvDAPN1qbVJQ4JFgTFJdQge8ZtQ-MC2p2tocabeElqY8DtlX72RQdaa9fdMBHZuv_Z_GE-4L546EVQyXan8fQZfWF9qZGLwwkAAg07-pnNqdUKjPDjo12Nm3NlCDe5kXQo535DhFw6OINsPbqxVY-5sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cMYCrKvNMpqTm4HzeKPyFziLqk7-HUzsrno_nP_9hng5LHcMhV6gcGceJGiM3upITrbSGpTpi1z0URRugJA6G8Lvvg5iptw7hmD4D7KqjiMOts96d_Ks7fGUI_Bxmw7fTwzlELLY7yxCc1vk0PzBYc4P9_6VRxO6HQB2ONTJZ_-J_m-tzP-5Wv2kTey2jundjEuULlNAT__eov8L3E6E4HSDdIOfJzpBvyrD_8PN_okX263N7mM7VsBzcs5ISQKANNQZ-Li91DVkFkPKDmNGOjSn78bNciEn_d_omBMVC0yBZ7A6IyUUhrUPaoOEKrdXaJQCz_2IKoSITgrz1rOPlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MNJ989piWNhADJu5EGi624z1pzBRjGhBmXOervdf6BYK49MeP1QBZv_Ks_9dp8cD9hE2na__Vp8ZusREnqL1LzXGw5kTLNYgPaRsC6WAfND2wR4YXcXI4F8nhVSBHNxZzkDJ4_1GOhiDkuKHZMdyqjA41lZKzqTn2XD8JMzfQTIGvSZEvL3E3igr98JjIbH47bk5ttefslSUhjgHcdwFJ5VFFz0tZiWhtpUbDPUih9yl8cmqOXX3KHM_2DTNxsVoF1JJemdZNPE0I_GuLMmF4r1Y1qsL2LI8nJXbTJQv_YJXCgHuCrFLCrwxyPLxPT_OtC3p9HXJGKBew96KHOjAww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
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
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/anyYO-lAQRco0M7BqGBy1jwxz5HC_qBlYhZM5eRpzwQ4lOiQw1GSwrl8ykwhdioxcs5hhRoIAnC-WqmQvDwfjBnGD9pA9Rcxl9RyxY3qFBNq5WQ65gkOPbC27dVqz-TkBQo_LgRvjFUxW_rdroCIMlUkQSw4TjlLV0tZ7HM799ISORaLQbBWZKRSJT5hBOthcWwebhUbqHIrqvL18NsqyNE5-XoO5-qc8bIN6-_nczO0AO0WWMyTpP759-6iJjVS1WqaqzWzJJwKflUygq8K2XYv64WgZDyiBbBIkvXmL7mYAUp29Blzc_I77-NocorAR3xZMC7NXJbOG-SwoGUdkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pJ_6uWsFgdCKAkIWFJ4benkCKJBlGPy43FuJ1x_3UZ6WiWUe63HXUxtMgurl4xkfUTIHJFdbuH7qopsWpsezoU84N95c9tU9EO29dzaoBfR2SPLuEfuwqqugG56MMVkXsm2tOcayKiP1UbPHoRY5hU6M9ZF5mV1PSM4YfHISvA7i_tR9pKKTjWC8oZULW9OAxm2eHIOQC0V5x-_-OgA92FOBJtHUUbZC_BbJAcq3ifjCcuzf0BbPeIkNw5OVZ-NrvuD2cIMTEdd6vCCLs65zMQrj0KfAGl28ERzLMjWmwzzGGq5joAc1-gnio7HdnmRT0zbn9XOJMY8MFH0J_AJXrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YWJ9c8SwzwW6taYY1d9JDa_kWF4JqKWwLK9iO1Cxhrhktrdj_FQ4thAd6UKaQA39NJ6PCQSCLU88TqtMuji_TTP84zGadkCVamkz2MWrTDGH58mzp9hSlfNvuPbdzPvx_NABMY2pGOxJn6gKyJe84jmps6VFMaiE91qvSirq_YLpif7f8eEoJrgTPiL4THohyIYZBJYM2Z3dXv9cMCmQSU_T6hJTqPCFzMTfOkWTsO4fRUQHqpeKZkqx-mMeZB78adkd7qCJnP7fD8O-stWsvsctCYopea67TPIQ3462OeCt6IM0cc1G_Ygk7DJxRactfGAM45zKaA0mXSrfZ-xGHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
